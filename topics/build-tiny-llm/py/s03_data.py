# -*- coding: utf-8 -*-
"""第 5 課：看看語料長什麼樣。"""
from collections import Counter

poems = open("data/tang.txt", encoding="utf-8").read().split("\n")
poems = [p for p in poems if p]
text = "".join(poems)
print("詩的數量：", len(poems))
print("總字數：", len(text))
print("不同的字：", len(set(text)))

kind = Counter()
for p in poems:
    n = len(p.replace("，", "").replace("。", ""))
    kind[{20: "五言絕句", 28: "七言絕句", 40: "五言律詩", 56: "七言律詩"}[n]] += 1
for k, v in kind.most_common():
    print("  %s：%d 首" % (k, v))

cnt = Counter(c for c in text if c not in "，。")
print("最常見的 20 個字：", "".join(c for c, _ in cnt.most_common(20)))
once = sum(1 for c, v in cnt.items() if v == 1)
print("只出現一次的字：%d 個（例如：%s）" % (once, "".join([c for c, v in cnt.items() if v == 1][:10])))
