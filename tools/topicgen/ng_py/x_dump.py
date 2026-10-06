# -*- coding: utf-8 -*-
"""（課程頁面用）把真實模型的數據匯出成 JSON，給互動工具使用。不屬於課程範例。"""
import json
import torch
import torch.nn.functional as F
from sample import load
from tokenizer import CharTokenizer

tok, model = CharTokenizer.load("tokenizer.json"), load()
out = {}
for prompt in ["春風", "明月", "白日依山"]:
    with torch.no_grad():
        logits = model(torch.tensor([tok.encode("\n" + prompt)]))[0][0, -1]
    top = torch.topk(logits, 30)
    out[prompt] = [[tok.itos[i], round(v, 3)] for v, i in zip(top.values.tolist(), top.indices.tolist())]
poems = [p for p in open("data/tang.txt", encoding="utf-8").read().split("\n") if p][:400]
json.dump({"logits": out, "poems": poems}, open("_out/data.json", "w", encoding="utf-8"), ensure_ascii=False)
print("ok")
