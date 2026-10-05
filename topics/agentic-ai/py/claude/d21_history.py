# -*- coding: utf-8 -*-
"""第 21 課（Claude API 版）：伺服器端壓縮（compaction，beta）。對話接近門檻時，API 自動摘要較早的內容。
重點：一定要把 response.content「整個」接回歷史，壓縮區塊才會被保留。"""
import anthropic

client = anthropic.Anthropic()
messages = []


def chat(user_message):
    messages.append({"role": "user", "content": user_message})
    r = client.beta.messages.create(
        betas=["compact-2026-01-12"],
        model="claude-opus-5-5",
        max_tokens=16000,
        messages=messages,
        context_management={"edits": [{"type": "compact_20260112"}]},
    )
    messages.append({"role": "assistant", "content": r.content})   # 不要只存文字！
    return next(b.text for b in r.content if b.type == "text")


print(chat("幫我規劃一個 Python 網路爬蟲"))
print(chat("加上處理 JavaScript 動態頁面的功能"))
