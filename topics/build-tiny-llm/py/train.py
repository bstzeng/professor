# -*- coding: utf-8 -*-
"""訓練 GPT 寫唐詩。

  python train.py                     # 預設設定，約 3M 參數
  python train.py --modern            # Llama 風格（RoPE、RMSNorm、SwiGLU）
  python train.py --resume            # 從上次的存檔繼續
  python train.py --steps 300 --n_layer 2 --out ckpt_small.pt   # 自己做實驗
"""
import argparse
import math
import os
import time

import torch

from gpt import GPT, GPTConfig
from tokenizer import CharTokenizer

ap = argparse.ArgumentParser()
ap.add_argument("--data", default="data/tang.txt")
ap.add_argument("--out", default="ckpt.pt")
ap.add_argument("--steps", type=int, default=2000)
ap.add_argument("--batch", type=int, default=32)
ap.add_argument("--accum", type=int, default=1, help="梯度累積步數：等效批次 = batch × accum")
ap.add_argument("--block", type=int, default=80)
ap.add_argument("--n_layer", type=int, default=4)
ap.add_argument("--n_head", type=int, default=4)
ap.add_argument("--n_embd", type=int, default=192)
ap.add_argument("--lr", type=float, default=1e-3)
ap.add_argument("--warmup", type=int, default=100)
ap.add_argument("--eval_every", type=int, default=200)
ap.add_argument("--modern", action="store_true")
ap.add_argument("--resume", action="store_true")
ap.add_argument("--amp", action="store_true", help="混合精度：GPU 上用 bfloat16 自動轉型")
ap.add_argument("--seed", type=int, default=1337)
args = ap.parse_args()

torch.manual_seed(args.seed)
device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"

# ---- 資料：整份文字轉成一長串 token id，前 95% 訓練、後 5% 驗證 ----
text = open(args.data, encoding="utf-8").read()
if os.path.exists("tokenizer.json"):
    tok = CharTokenizer.load("tokenizer.json")
else:
    tok = CharTokenizer.train(text)
    tok.save("tokenizer.json")
data = torch.tensor(tok.encode(text), dtype=torch.long)
n = int(len(data) * 0.95)
train_data, val_data = data[:n], data[n:]


def get_batch(split):
    d = train_data if split == "train" else val_data
    ix = torch.randint(len(d) - args.block - 1, (args.batch,))
    x = torch.stack([d[i:i + args.block] for i in ix])
    y = torch.stack([d[i + 1:i + args.block + 1] for i in ix])      # 答案 ＝ 往右移一格
    return x.to(device), y.to(device)


# ---- 模型與優化器 ----
cfg = GPTConfig(vocab_size=tok.vocab_size, block_size=args.block, n_layer=args.n_layer, n_head=args.n_head,
                n_embd=args.n_embd, modern=args.modern)
model = GPT(cfg).to(device)
decay = [p for p in model.parameters() if p.dim() >= 2]            # 權重矩陣做權重衰減
no_decay = [p for p in model.parameters() if p.dim() < 2]          # 偏差、正規化層不做
opt = torch.optim.AdamW([{"params": decay, "weight_decay": 0.1}, {"params": no_decay, "weight_decay": 0.0}],
                        lr=args.lr, betas=(0.9, 0.95))
step0 = 0
if args.resume and os.path.exists(args.out):
    ck = torch.load(args.out, map_location=device)
    model.load_state_dict(ck["model"])
    opt.load_state_dict(ck["opt"])
    step0 = ck["step"]
    print("從第 %d 步繼續訓練" % step0)
print("裝置 %s，參數 %.2fM，詞彙 %d 字，訓練資料 %d 個 token" % (device, model.num_params() / 1e6, tok.vocab_size, len(train_data)))


def lr_at(step):
    """warmup 之後用 cosine 衰減到最大學習率的 10%。"""
    if step < args.warmup:
        return args.lr * (step + 1) / args.warmup
    t = (step - args.warmup) / max(1, args.steps - args.warmup)
    return args.lr * (0.1 + 0.9 * 0.5 * (1 + math.cos(math.pi * min(t, 1.0))))


@torch.no_grad()
def evaluate(iters=20):
    model.eval()
    out = {}
    for split in ("train", "val"):
        out[split] = sum(model(*get_batch(split))[1].item() for _ in range(iters)) / iters
    model.train()
    return out


amp = torch.autocast(device_type=device if device != "mps" else "cpu", dtype=torch.bfloat16, enabled=args.amp)
model.train()
t0 = time.time()
for step in range(step0, args.steps):
    for g in opt.param_groups:
        g["lr"] = lr_at(step)
    for _ in range(args.accum):                         # 梯度累積
        x, y = get_batch("train")
        with amp:
            _, loss = model(x, y)
        (loss / args.accum).backward()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)    # 梯度裁剪
    opt.step()
    opt.zero_grad(set_to_none=True)
    if step % args.eval_every == 0 or step == args.steps - 1:
        e = evaluate()
        print("step %5d | lr %.2e | train loss %.3f | val loss %.3f | %.0fs" % (step, lr_at(step), e["train"], e["val"], time.time() - t0))
        torch.save({"model": model.state_dict(), "opt": opt.state_dict(), "cfg": cfg.__dict__, "step": step + 1}, args.out)
print("已存檔到", args.out)
