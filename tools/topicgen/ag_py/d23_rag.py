# -*- coding: utf-8 -*-
"""第 23 課：RAG（檢索增強生成）——先從知識庫找出相關段落，再把它們放進提示，讓模型「看著資料回答」。
步驟：切塊 → 建索引（嵌入）→ 查詢時檢索 top-k → 組提示 → 生成（附出處）。"""
import math
from mockllm import MockClient, text

def embed(s, dim=256):
    v = [0.0] * dim
    for a, b in zip(s, s[1:]):
        v[(ord(a) * 31 + ord(b)) % dim] += 1
    n = math.sqrt(sum(x * x for x in v)) or 1
    return [x / n for x in v]

MANUAL = """退貨：商品到貨 7 天內可申請退貨，需保持包裝完整。
退款：退貨審核通過後，款項於 5 個工作天內退回原付款方式。
運費：訂單滿 1000 元免運，未滿收 80 元。
保固：電子產品享一年保固，人為損壞不在保固範圍。
會員：年消費滿 2 萬元升級金卡，享 95 折。"""

chunks = [c for c in MANUAL.split("\n") if c]                     # ① 切塊（這裡一行一塊）
index = [(c, embed(c)) for c in chunks]                           # ② 建索引

def retrieve(q, k=2):                                              # ③ 檢索
    qv = embed(q)
    return sorted(index, key=lambda cv: -sum(a * b for a, b in zip(qv, cv[1])))[:k]

def rag_policy(ctx):                                               # ⑤ 假模型：只根據提示中的資料回答
    p = ctx.user_text()
    if "5 個工作天" in p:
        return text("退貨審核通過後，退款會在 5 個工作天內退回原付款方式。[來源 2]")
    return text("資料中沒有提到，我無法確定。")

q = "退貨之後錢多久會退回來？"
hits = retrieve(q)
for i, (c, _) in enumerate(hits, 1):
    print("檢索 %d：%s" % (i, c))
prompt = "根據以下資料回答，並標註來源編號；資料沒有的就說不知道。\n\n" + \
         "\n".join("[來源 %d] %s" % (i, c) for i, (c, _) in enumerate(hits, 1)) + "\n\n問題：" + q   # ④ 組提示
print("\n送給模型的提示：\n" + prompt)
r = MockClient(rag_policy).messages.create(model="mock", max_tokens=300, messages=[{"role": "user", "content": prompt}])
print("\n回答：", r.content[0].text)
print("\n代理式 RAG：把 retrieve 包成工具，讓模型自己決定要不要查、查什麼、查幾次。")
