# -*- coding: utf-8 -*-
"""第 32 課：temperature、top-k、top-p 對生成的影響。"""
import torch
import torch.nn.functional as F
from sample import load, write
from tokenizer import CharTokenizer

tok, model = CharTokenizer.load("tokenizer.json"), load()

# 先看模型對「春風」後面那個字的機率分布
idx = torch.tensor([tok.encode("\n春風")])            # 開頭的換行代表「新的一首詩」
with torch.no_grad():
    logits = model(idx)[0][0, -1]
for T in (0.5, 1.0, 1.5):
    p = F.softmax(logits / T, -1)
    top = torch.topk(p, 5)
    print("T=%.1f  前五名：%s" % (T, "  ".join("%s %.0f%%" % (tok.itos[i], v * 100) for v, i in zip(top.values.tolist(), top.indices.tolist()))))

print()
for T, k, pp in [(0, None, None), (0.6, None, None), (1.0, None, None), (1.5, None, None), (1.0, 20, None), (1.0, None, 0.8)]:
    torch.manual_seed(1)
    label = "貪婪（T=0）" if T == 0 else "T=%.1f" % T + (" top-k=%d" % k if k else "") + (" top-p=%.1f" % pp if pp else "")
    print("%-18s %s" % (label, write(model, tok, "春風", T, k, pp)))
