# -*- coding: utf-8 -*-
"""第 33 課：KV cache 有沒有用？比較速度，並確認輸出完全一樣。"""
import time
import torch
from sample import load
from tokenizer import CharTokenizer

tok, model = CharTokenizer.load("tokenizer.json"), load()
idx = torch.tensor([tok.encode("\n山")])
for use in (False, True):
    t = time.time()
    for _ in range(5):
        out = model.generate(idx, 70, temperature=0, use_cache=use)
    dt = (time.time() - t) / 5
    print("%s KV cache：生成 70 字平均 %.3f 秒  →  %s" % ("有" if use else "沒有", dt, tok.decode(out[0, 1:].tolist()).split("\n")[0]))
a = model.generate(idx, 70, temperature=0, use_cache=False)
b = model.generate(idx, 70, temperature=0, use_cache=True)
print("兩種方式的輸出完全相同：", torch.equal(a, b))
