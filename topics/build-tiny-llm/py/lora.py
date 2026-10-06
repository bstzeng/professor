# -*- coding: utf-8 -*-
"""第 40 課：從零實作 LoRA，教唐詩模型聽懂〔體裁 主題字〕的指令。

  python lora.py            # 讀 ckpt.pt，只訓練 LoRA 參數，存成 lora.pt
"""
import math
import torch
import torch.nn as nn
from sample import load
from tokenizer import CharTokenizer


class LoRALinear(nn.Module):
    """y = W x + (B A x) · (alpha / r)。W 凍結，只訓練很小的 A、B。"""

    def __init__(self, base: nn.Linear, r=8, alpha=16):
        super().__init__()
        self.base, self.scale = base, alpha / r
        self.A = nn.Parameter(torch.randn(r, base.in_features) / math.sqrt(base.in_features))
        self.B = nn.Parameter(torch.zeros(base.out_features, r))     # B 從 0 開始：一開始完全不改變原模型

    def forward(self, x):
        return self.base(x) + (x @ self.A.T @ self.B.T) * self.scale


def add_lora(model, r=8):
    for p in model.parameters():
        p.requires_grad = False                                       # 凍結整個原模型
    for blk in model.blocks:
        blk.attn.qkv = LoRALinear(blk.attn.qkv, r)
        blk.attn.proj = LoRALinear(blk.attn.proj, r)
    return model


def lora_state(model):
    return {k: v for k, v in model.state_dict().items() if k.endswith(".A") or k.endswith(".B")}


if __name__ == "__main__":
    torch.manual_seed(0)
    tok = CharTokenizer.load("tokenizer.json")
    model = add_lora(load("ckpt.pt"))
    train = [r for r in open("data/instruct.txt", encoding="utf-8").read().split("\n") if r][:-500]   # 最後 500 筆留給評估
    n_all = model.num_params()
    n_train = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print("全部參數 %d，要訓練的 LoRA 參數 %d（%.1f%%）" % (n_all, n_train, 100 * n_train / n_all))
    opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=2e-3)
    T = model.cfg.block_size
    model.train()
    for step in range(601):
        rows = [train[i] for i in torch.randint(len(train), (32,)).tolist()]
        ids = [tok.encode("\n" + r + "\n")[:T + 1] for r in rows]      # 前後都是換行，和 write() 的格式一致
        L = max(len(s) for s in ids)
        x = torch.full((32, L - 1), 0)
        y = torch.full((32, L - 1), -100)                              # -100：不計算損失的位置
        for i, s in enumerate(ids):
            x[i, :len(s) - 1] = torch.tensor(s[:-1])
            y[i, :len(s) - 1] = torch.tensor(s[1:])
            y[i, :s.index(tok.stoi["〕"])] = -100                        # 只對「詩」的部分算損失，指令本身不用學
        logits, _ = model(x)
        loss = nn.functional.cross_entropy(logits.reshape(-1, logits.size(-1)), y.reshape(-1), ignore_index=-100)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if step % 100 == 0:
            print("step %3d  loss %.3f" % (step, loss.item()))
    torch.save(lora_state(model), "lora.pt")
    print("LoRA 權重存成 lora.pt，大小約 %.0f KB" % (n_train * 4 / 1024))
