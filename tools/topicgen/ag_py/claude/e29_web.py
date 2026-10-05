# -*- coding: utf-8 -*-
"""第 29 課（Claude API 版）：伺服器端的 web_search 與 web_fetch 工具，搜尋與擷取都在 Anthropic 端完成。
可用 allowed_domains / blocked_domains 限制範圍、max_uses 限制次數。"""
import anthropic

client = anthropic.Anthropic()
r = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    tools=[{"type": "web_search_20260209", "name": "web_search", "max_uses": 5},
           {"type": "web_fetch_20260209", "name": "web_fetch", "max_uses": 3}],
    messages=[{"role": "user", "content": "台灣目前再生能源發電占比大約多少？請附來源。"}],
)
if r.stop_reason == "pause_turn":      # 伺服器端工具跑太久會暫停，把 r.content 接回去再送一次即可繼續
    print("（回合暫停，需要續送）")
for b in r.content:
    if b.type == "text":
        print(b.text, end="")
    elif b.type == "server_tool_use":
        print("\n[%s] %s" % (b.name, b.input))
print()
