# -*- coding: utf-8 -*-
"""第 9 課（Claude API 版）：Claude 預設可以在一則回應裡發出多個 tool_use。
平行執行後，把所有 tool_result 放在同一則 user 訊息送回。"""
import json
from concurrent.futures import ThreadPoolExecutor
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"
TEMPS = {"台北": 27, "東京": 22, "首爾": 18}
tools = [{"name": "get_weather", "description": "查一個城市的目前氣溫（攝氏）",
          "input_schema": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}]
messages = [{"role": "user", "content": "台北、東京、首爾哪裡最暖？"}]

while True:
    r = client.messages.create(model=MODEL, max_tokens=16000, tools=tools, messages=messages)
    messages.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    calls = [b for b in r.content if b.type == "tool_use"]
    print("這一輪有 %d 個工具呼叫" % len(calls))
    with ThreadPoolExecutor() as pool:
        results = list(pool.map(lambda b: {"type": "tool_result", "tool_use_id": b.id,
                                           "content": json.dumps({"temp_c": TEMPS.get(b.input["city"])})}, calls))
    messages.append({"role": "user", "content": results})

print(next(b.text for b in r.content if b.type == "text"))
