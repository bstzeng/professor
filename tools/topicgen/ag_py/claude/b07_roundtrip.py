# -*- coding: utf-8 -*-
"""第 7 課（Claude API 版）：手動完成一次 tool_use → tool_result 往返。"""
import json
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"
tools = [{"name": "get_exchange_rate", "description": "查詢匯率：1 單位 base 貨幣可換多少 quote 貨幣（ISO 代碼，如 USD、TWD）",
          "input_schema": {"type": "object", "properties": {"base": {"type": "string"}, "quote": {"type": "string"}},
                           "required": ["base", "quote"]}}]
messages = [{"role": "user", "content": "200 美元可以換多少台幣？"}]

r = client.messages.create(model=MODEL, max_tokens=16000, tools=tools, messages=messages)
print("stop_reason =", r.stop_reason)
call = next(b for b in r.content if b.type == "tool_use")
print("Claude 要求：", call.name, call.input, call.id)

messages.append({"role": "assistant", "content": r.content})
messages.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": call.id,
                                              "content": json.dumps({"rate": 32.1})}]})
r = client.messages.create(model=MODEL, max_tokens=16000, tools=tools, messages=messages)
print(next(b.text for b in r.content if b.type == "text"))
