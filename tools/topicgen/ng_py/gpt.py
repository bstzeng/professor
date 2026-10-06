# -*- coding: utf-8 -*-
"""一個完整的 GPT（decoder-only Transformer）。

modern=False：GPT-2 風格（學出來的位置 embedding、LayerNorm、GELU）
modern=True ：Llama 風格（RoPE、RMSNorm、SwiGLU）
"""
import math
from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F


@dataclass
class GPTConfig:
    vocab_size: int = 8000
    block_size: int = 128       # 最長的上下文長度
    n_layer: int = 4
    n_head: int = 4
    n_embd: int = 192
    dropout: float = 0.1
    modern: bool = False


class RMSNorm(nn.Module):
    def __init__(self, d, eps=1e-6):
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(d))

    def forward(self, x):
        return x * torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps) * self.weight


def rope(x, pos):
    """旋轉位置編碼：把每兩個維度當成一個平面，依位置旋轉不同角度。x: (B, H, T, D)"""
    d = x.shape[-1]
    freq = 1.0 / (10000 ** (torch.arange(0, d, 2, device=x.device).float() / d))
    ang = pos[:, None].float() * freq[None, :]                  # (T, D/2)
    cos, sin = ang.cos(), ang.sin()
    x1, x2 = x[..., 0::2], x[..., 1::2]
    out = torch.stack([x1 * cos - x2 * sin, x1 * sin + x2 * cos], dim=-1)
    return out.flatten(-2)


class CausalSelfAttention(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        assert cfg.n_embd % cfg.n_head == 0
        self.n_head, self.hd, self.modern = cfg.n_head, cfg.n_embd // cfg.n_head, cfg.modern
        self.qkv = nn.Linear(cfg.n_embd, 3 * cfg.n_embd, bias=not cfg.modern)   # 一次算出 Q、K、V
        self.proj = nn.Linear(cfg.n_embd, cfg.n_embd, bias=not cfg.modern)
        self.drop = nn.Dropout(cfg.dropout)
        self.register_buffer("mask", torch.tril(torch.ones(cfg.block_size, cfg.block_size)).bool())

    def forward(self, x, cache=None, start=0):
        B, T, C = x.shape
        q, k, v = self.qkv(x).split(C, dim=2)
        q, k, v = [t.view(B, T, self.n_head, self.hd).transpose(1, 2) for t in (q, k, v)]   # (B, H, T, hd)
        if self.modern:
            pos = torch.arange(start, start + T, device=x.device)
            q, k = rope(q, pos), rope(k, pos)
        if cache is not None:                       # KV cache：把之前的 K、V 接在前面
            if "k" in cache:
                k = torch.cat([cache["k"], k], dim=2)
                v = torch.cat([cache["v"], v], dim=2)
            cache["k"], cache["v"] = k, v
        S = k.shape[2]
        att = (q @ k.transpose(-2, -1)) / math.sqrt(self.hd)       # (B, H, T, S)
        att = att.masked_fill(~self.mask[S - T:S, :S], float("-inf"))   # 因果遮罩
        att = self.drop(F.softmax(att, dim=-1))
        y = (att @ v).transpose(1, 2).contiguous().view(B, T, C)    # 把各頭接回來
        return self.drop(self.proj(y))


class MLP(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.modern = cfg.modern
        if cfg.modern:                              # SwiGLU：隱藏層約 8/3 倍，讓參數量和 4 倍的 GELU 相近
            h = int(8 * cfg.n_embd / 3)
            self.w1 = nn.Linear(cfg.n_embd, h, bias=False)
            self.w3 = nn.Linear(cfg.n_embd, h, bias=False)
            self.w2 = nn.Linear(h, cfg.n_embd, bias=False)
        else:
            self.fc = nn.Linear(cfg.n_embd, 4 * cfg.n_embd)
            self.proj = nn.Linear(4 * cfg.n_embd, cfg.n_embd)
        self.drop = nn.Dropout(cfg.dropout)

    def forward(self, x):
        if self.modern:
            return self.drop(self.w2(F.silu(self.w1(x)) * self.w3(x)))
        return self.drop(self.proj(F.gelu(self.fc(x))))


class Block(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        Norm = RMSNorm if cfg.modern else nn.LayerNorm
        self.ln1, self.attn = Norm(cfg.n_embd), CausalSelfAttention(cfg)
        self.ln2, self.mlp = Norm(cfg.n_embd), MLP(cfg)

    def forward(self, x, cache=None, start=0):
        x = x + self.attn(self.ln1(x), cache, start)     # 殘差連接
        x = x + self.mlp(self.ln2(x))
        return x


class GPT(nn.Module):
    def __init__(self, cfg):
        super().__init__()
        self.cfg = cfg
        self.tok_emb = nn.Embedding(cfg.vocab_size, cfg.n_embd)
        self.pos_emb = None if cfg.modern else nn.Embedding(cfg.block_size, cfg.n_embd)
        self.drop = nn.Dropout(cfg.dropout)
        self.blocks = nn.ModuleList([Block(cfg) for _ in range(cfg.n_layer)])
        self.ln_f = RMSNorm(cfg.n_embd) if cfg.modern else nn.LayerNorm(cfg.n_embd)
        self.head = nn.Linear(cfg.n_embd, cfg.vocab_size, bias=False)
        self.head.weight = self.tok_emb.weight          # 權重綁定：輸入和輸出共用同一張 embedding 表
        self.apply(self._init)

    @staticmethod
    def _init(m):
        if isinstance(m, (nn.Linear, nn.Embedding)):
            nn.init.normal_(m.weight, mean=0.0, std=0.02)
        if isinstance(m, nn.Linear) and m.bias is not None:
            nn.init.zeros_(m.bias)

    def forward(self, idx, targets=None, caches=None, start=0):
        B, T = idx.shape
        x = self.tok_emb(idx)
        if self.pos_emb is not None:
            x = x + self.pos_emb(torch.arange(start, start + T, device=idx.device))
        x = self.drop(x)
        for i, blk in enumerate(self.blocks):
            x = blk(x, None if caches is None else caches[i], start)
        logits = self.head(self.ln_f(x))
        loss = None
        if targets is not None:
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.view(-1))
        return logits, loss

    def num_params(self):
        return sum(p.numel() for p in self.parameters())

    @torch.no_grad()
    def generate(self, idx, max_new_tokens, temperature=1.0, top_k=None, top_p=None, stop=None, use_cache=True):
        """逐字生成。stop：遇到這個 token id 就停（例如換行）。"""
        self.eval()
        caches = [dict() for _ in self.blocks] if use_cache else None
        start = 0
        for _ in range(max_new_tokens):
            if idx.size(1) >= self.cfg.block_size:          # 超過上下文長度就只看最後一段，並重建快取
                idx_in, caches, start = idx[:, -self.cfg.block_size + 1:], ([dict() for _ in self.blocks] if use_cache else None), 0
            elif use_cache and start > 0:
                idx_in = idx[:, -1:]                         # 有快取：只需送入最新的一個 token
            else:
                idx_in = idx
            logits, _ = self(idx_in, caches=caches, start=start)
            if use_cache:
                start += idx_in.size(1)
            logits = logits[:, -1, :] / max(temperature, 1e-6)
            if top_k:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, [-1]]] = float("-inf")
            probs = F.softmax(logits, dim=-1)
            if top_p:
                sp, si = torch.sort(probs, descending=True)
                drop = sp.cumsum(-1) - sp > top_p              # 保留累積機率剛好達到 top_p 的最小集合
                sp[drop] = 0
                probs = torch.zeros_like(probs).scatter(-1, si, sp)
                probs = probs / probs.sum(-1, keepdim=True)
            nxt = torch.argmax(probs, -1, keepdim=True) if temperature == 0 else torch.multinomial(probs, 1)
            idx = torch.cat([idx, nxt], dim=1)
            if stop is not None and nxt.item() == stop:
                break
        return idx
