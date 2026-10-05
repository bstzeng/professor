# -*- coding: utf-8 -*-
"""第 22 課：嵌入向量（embedding）——把文字變成一串數字，意思相近的文字，向量方向也相近。
真正的嵌入模型是神經網路；這裡用「字元雙字組（bigram）計數」做一個看得懂的簡化版。"""
import math
from collections import Counter

def embed(s, dim=256):
    """把文字的每個雙字組雜湊到 dim 維中的一格（hashing trick），再正規化成長度 1。"""
    v = [0.0] * dim
    s = s.replace(" ", "")
    for a, b in zip(s, s[1:]):
        v[(ord(a) * 31 + ord(b)) % dim] += 1
    n = math.sqrt(sum(x * x for x in v)) or 1
    return [x / n for x in v]

def cosine(u, v):
    return sum(a * b for a, b in zip(u, v))      # 都已正規化，內積就是餘弦相似度

docs = ["如何重設登入密碼", "忘記密碼怎麼辦", "退貨與退款政策", "運費怎麼計算", "帳號被鎖住無法登入"]
q = "我忘了密碼不能登入"
qv = embed(q)
print("查詢：「%s」→ 向量前 8 維：%s" % (q, [round(x, 2) for x in qv[:8]]))
for d, s in sorted(((d, cosine(qv, embed(d))) for d in docs), key=lambda x: -x[1]):
    print("  %.3f  %s %s" % (s, "█" * int(s * 30), d))
print("\n限制：這個簡化版只看『字面重疊』；真正的嵌入模型能理解『鎖住』和『無法登入』語意相近，即使沒有共同的字。")
print("（Anthropic 不提供嵌入模型；常見做法是搭配 Voyage AI 等嵌入服務，或開源模型。）")
