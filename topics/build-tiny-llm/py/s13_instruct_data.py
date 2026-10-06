# -*- coding: utf-8 -*-
"""第 39 課：做一份「指令資料」——〔體裁 主題字〕＋ 詩。"""
import random

THEMES = "春秋月山水風花雪雨夜江雲柳酒鶴"
FORM = {20: "五言絕句", 28: "七言絕句", 40: "五言律詩", 56: "七言律詩"}
random.seed(0)
rows = []
for p in open("data/tang.txt", encoding="utf-8").read().split("\n"):
    if not p:
        continue
    form = FORM[len(p.replace("，", "").replace("。", ""))]
    hits = [c for c in THEMES if c in p]
    if hits:
        rows.append("〔%s %s〕%s" % (form, random.choice(hits), p))
random.shuffle(rows)
with open("data/instruct.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(rows) + "\n")
print("指令資料 %d 筆，例如：" % len(rows))
for r in rows[:4]:
    print(" ", r)
