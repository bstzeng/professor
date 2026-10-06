# -*- coding: utf-8 -*-
"""下載《全唐詩》（chinese-poetry 專案，MIT 授權）並整理成訓練用的純文字檔。

輸出：data/tang.txt，每行一首五言或七言的絕句、律詩。
"""
import json
import os
import re
import urllib.request

URL = "https://raw.githubusercontent.com/chinese-poetry/chinese-poetry/master/%E5%85%A8%E5%94%90%E8%AF%97/poet.tang.{}.json"
os.makedirs("data", exist_ok=True)
CACHE = os.path.join("data", "raw")
os.makedirs(CACHE, exist_ok=True)


def fetch(i):
    path = os.path.join(CACHE, "poet.tang.%d.json" % i)
    if not os.path.exists(path):
        urllib.request.urlretrieve(URL.format(i), path)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def clean(poem):
    """只留下「每句 5 或 7 字、共 4 或 8 句」的詩；不合格就回傳 None。"""
    text = "".join(poem["paragraphs"])
    if re.search(r"[^一-鿿，。]", text):      # 有缺字符號、註解或其他標點就跳過
        return None
    sents = [s for s in re.split(r"[，。]", text) if s]
    if len(sents) not in (4, 8):
        return None
    n = len(sents[0])
    if n not in (5, 7) or any(len(s) != n for s in sents):
        return None
    return text


poems = []
for i in range(0, 58000, 1000):
    for p in fetch(i):
        t = clean(p)
        if t:
            poems.append(t)

with open("data/tang.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(poems) + "\n")
print("整理出 %d 首詩，共 %d 個字" % (len(poems), sum(len(p) for p in poems)))
print("第一首：", poems[0])
