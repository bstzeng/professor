# -*- coding: utf-8 -*-
"""（課程頁面用）匯出唐詩模型的 logit lens 與注意力圖，給〈AI 的內心與邊界〉的互動工具。不屬於課程範例。"""
import json
import torch
import torch.nn.functional as F
from sample import load
from tokenizer import CharTokenizer

tok, model = CharTokenizer.load("tokenizer.json"), load()
out = {"lens": {}, "attn": {}}
for prompt in ["床前明月光，疑是地上", "白日依山盡，黃河入海", "春風"]:
    ids = torch.tensor([tok.encode("\n" + prompt)])
    rows = []
    with torch.no_grad():
        x = model.tok_emb(ids) + model.pos_emb(torch.arange(ids.size(1)))
        states = [x]
        attns = []
        for blk in model.blocks:
            h = blk.ln1(x)
            B, T, C = h.shape
            q, k, v = blk.attn.qkv(h).split(C, dim=2)
            q, k = [t.view(B, T, blk.attn.n_head, blk.attn.hd).transpose(1, 2) for t in (q, k)]
            a = (q @ k.transpose(-2, -1)) / blk.attn.hd ** 0.5
            a = F.softmax(a.masked_fill(~blk.attn.mask[:T, :T], float("-inf")), -1)
            attns.append(a[0].tolist())
            x = blk(x)
            states.append(x)
        for L, s in enumerate(states):
            p = F.softmax(model.head(model.ln_f(s))[0, -1], -1)
            top = torch.topk(p, 5)
            rows.append([[tok.itos[i], round(v, 3)] for v, i in zip(top.values.tolist(), top.indices.tolist())])
    out["lens"][prompt] = rows
    out["attn"][prompt] = {"tokens": ["⏎"] + list(prompt), "layers": [[[[round(v, 3) for v in r] for r in head] for head in layer] for layer in attns]}
json.dump(out, open("_out/lens.json", "w", encoding="utf-8"), ensure_ascii=False)
for prompt, rows in out["lens"].items():
    print(prompt, "→", " | ".join("L%d:%s" % (i, r[0][0]) for i, r in enumerate(rows)))
