# -*- coding: utf-8 -*-
"""第 25 課（Claude API 版）：開啟提示快取並檢查是否命中。
頂層 cache_control 會自動在最後一個可快取區塊設中斷點；固定內容放前面，會變的內容放後面。
前綴太短（低於模型的最小可快取長度）不會被快取。"""
import anthropic

client = anthropic.Anthropic()
BIG_SYSTEM = "你是公司內部的程式代理。以下是專案規範：\n" + "（很長的程式規範……）\n" * 2000
messages = []

for q in ["列出規範中關於命名的規則", "那測試相關的呢？"]:
    messages.append({"role": "user", "content": q})
    r = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        cache_control={"type": "ephemeral"},
        system=BIG_SYSTEM,                 # 不要在這裡放時間、亂數等每次都會變的內容
        messages=messages,
    )
    messages.append({"role": "assistant", "content": r.content})
    u = r.usage
    print("寫入快取 %d｜讀取快取 %d｜未快取 %d" % (u.cache_creation_input_tokens, u.cache_read_input_tokens, u.input_tokens))
