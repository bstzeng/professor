# -*- coding: utf-8 -*-
"""第 7 課：一次完整的「tool_use → tool_result」往返，逐則印出訊息內容。"""
import json
from mockllm import MockClient, text, tool_use, script, show

def get_exchange_rate(base, quote):
    return {"USD/TWD": 32.1, "JPY/TWD": 0.215}.get(base + "/" + quote)

tools = [{"name": "get_exchange_rate", "description": "查詢匯率：1 單位 base 可換多少 quote",
          "input_schema": {"type": "object", "properties": {"base": {"type": "string"}, "quote": {"type": "string"}},
                           "required": ["base", "quote"]}}]
client = MockClient(script(
    [text("我來查匯率。"), tool_use("get_exchange_rate", {"base": "USD", "quote": "TWD"}, id="toolu_A1")],
    lambda c: text("200 美元約可換 %.0f 新台幣。" % (200 * float(c.data())))))

messages = [{"role": "user", "content": "200 美元可以換多少台幣？"}]
print("① 送出 user 訊息"); r = client.messages.create(model="mock", max_tokens=500, messages=messages, tools=tools); show(r)

messages.append({"role": "assistant", "content": r.content})
call = next(b for b in r.content if b.type == "tool_use")
result = get_exchange_rate(**call.input)
print("\n② 我們的程式執行 %s → %s" % (call.name, result))
messages.append({"role": "user", "content": [
    {"type": "tool_result", "tool_use_id": call.id, "content": json.dumps(result)}]})   # id 必須對得上
print("③ 把 tool_result 放在 user 訊息送回：", messages[-1]["content"][0])

r = client.messages.create(model="mock", max_tokens=500, messages=messages, tools=tools)
print("\n④ 模型看到結果後回答"); show(r)
print("\n整段對話角色：", [m["role"] for m in messages + [{"role": "assistant"}]])
