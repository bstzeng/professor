# -*- coding: utf-8 -*-
"""第 41 課：評估微調前後——模型有沒有照指令寫？"""
import random
import re
import torch
from lora import add_lora
from sample import load, write
from tokenizer import CharTokenizer

tok = CharTokenizer.load("tokenizer.json")
base = load("ckpt.pt")
tuned = add_lora(load("ckpt.pt"))
tuned.load_state_dict(torch.load("lora.pt"), strict=False)
tuned.eval()

SPEC = {"五言絕句": (5, 4), "七言絕句": (7, 4), "五言律詩": (5, 8), "七言律詩": (7, 8)}


def check(prompt, out):
    form, theme = prompt[1:-1].split()
    poem = out[len(prompt):]
    sents = [s for s in re.split("[，。]", poem) if s]
    n, k = SPEC[form]
    return len(sents) == k and all(len(s) == n for s in sents), theme in poem


random.seed(1)
prompts = ["〔%s %s〕" % (random.choice(list(SPEC)), random.choice("春秋月山水風花雪雨夜江雲柳酒鶴")) for _ in range(60)]
for name, m in [("微調前", base), ("微調後（LoRA）", tuned)]:
    torch.manual_seed(0)
    ok_form = ok_theme = 0
    outs = []
    for p in prompts:
        out = write(m, tok, p, temperature=0.8, top_p=0.9)
        f, t = check(p, out)
        ok_form += f
        ok_theme += t
        outs.append(out)
    print("%s：體裁正確 %d/%d，包含主題字 %d/%d" % (name, ok_form, len(prompts), ok_theme, len(prompts)))
    for o in outs[:3]:
        print("   ", o)
