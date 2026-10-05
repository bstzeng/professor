# -*- coding: utf-8 -*-
"""第 2 課：LLM 的本質——一次預測一個 token。
用一個極小的「二元語法（bigram）」模型示範：統計『下一個字』的機率，再一個一個接下去。"""
import random
from collections import Counter, defaultdict

corpus = ("代理會呼叫工具。代理會讀取結果。代理會決定下一步。"
          "模型會預測下一個字。模型會呼叫工具。工具會回傳結果。")
nxt = defaultdict(Counter)
for a, b in zip(corpus, corpus[1:]):
    nxt[a][b] += 1                       # 「a 後面接 b」出現幾次

def probs(ch):
    c = nxt[ch]
    total = sum(c.values())
    return {k: v / total for k, v in c.most_common()}

print("「會」後面可能接：", {k: round(v, 2) for k, v in probs("會").items()})

def generate(start, n, temperature=1.0, seed=0):
    rnd = random.Random(seed)
    out = start
    for _ in range(n):
        p = probs(out[-1])
        if not p:
            break
        # temperature 越低越「保守」（偏向最常見的字），越高越「隨機」
        w = [v ** (1.0 / temperature) for v in p.values()]
        out += rnd.choices(list(p.keys()), weights=w)[0]
        if out[-1] == "。":
            break
    return out

for t in (0.2, 1.0, 2.0):
    print("temperature=%.1f →" % t, [generate("代", 12, t, seed=s) for s in range(3)])
print("重點：模型本身只會『接下一個字』。它不會自己上網、不會自己執行程式——")
print("　　　要讓它『做事』，得靠外面的程式把它包進一個迴圈，並提供工具。")
