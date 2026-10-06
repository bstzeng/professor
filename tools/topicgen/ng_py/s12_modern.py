# -*- coding: utf-8 -*-
"""第 37 課：比較 GPT-2 風格與 Llama 風格（RoPE、RMSNorm、SwiGLU）。"""
import torch
from sample import load, write
from tokenizer import CharTokenizer

tok = CharTokenizer.load("tokenizer.json")
text = open("data/tang.txt", encoding="utf-8").read()
data = torch.tensor(tok.encode(text))
val = data[int(len(data) * 0.95):]
torch.manual_seed(0)
ix = torch.randint(len(val) - 81, (200,))
x = torch.stack([val[i:i + 80] for i in ix])
y = torch.stack([val[i + 1:i + 81] for i in ix])
for name, path in [("GPT-2 風格", "ckpt.pt"), ("Llama 風格", "ckpt_modern.pt")]:
    m = load(path)
    with torch.no_grad():
        loss = sum(m(x[i:i + 50], y[i:i + 50])[1].item() for i in range(0, 200, 50)) / 4
    torch.manual_seed(3)
    print("%s：參數 %.2fM，驗證損失 %.3f，範例：%s" % (name, m.num_params() / 1e6, loss, write(m, tok, "秋")))
