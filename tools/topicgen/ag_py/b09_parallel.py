# -*- coding: utf-8 -*-
"""第 9 課：平行工具呼叫——模型一次要求多個工具，我們同時執行，再「一起」送回。"""
import json
import time
from concurrent.futures import ThreadPoolExecutor
from mockllm import MockClient, text, tool_use

def get_weather(city):
    time.sleep(0.5)                            # 模擬網路延遲 0.5 秒
    return {"台北": 27, "東京": 22, "首爾": 18}[city]

def policy(ctx):
    if ctx.turn == 0:                          # 一次回應裡放 3 個 tool_use
        return [text("三個城市我同時查。")] + [tool_use("get_weather", {"city": c}) for c in ("台北", "東京", "首爾")]
    temps = {json.loads(r[1])["city"]: json.loads(r[1])["temp"] for r in ctx.results()}
    return text("最暖的是%s（%d°C）。" % max(temps.items(), key=lambda kv: kv[1]))

tools = [{"name": "get_weather", "description": "查氣溫", "input_schema": {"type": "object", "properties": {"city": {"type": "string"}}}}]
client = MockClient(policy)
messages = [{"role": "user", "content": "台北、東京、首爾哪裡最暖？"}]
r = client.messages.create(model="mock", max_tokens=500, tools=tools, messages=messages)
calls = [b for b in r.content if b.type == "tool_use"]
print("模型一次要求了 %d 個工具呼叫" % len(calls))

def run_one(b):
    return {"type": "tool_result", "tool_use_id": b.id,
            "content": json.dumps({"city": b.input["city"], "temp": get_weather(**b.input)}, ensure_ascii=False)}

t0 = time.time()
for b in calls:                                # 依序執行：約 1.5 秒
    run_one(b)
print("依序執行耗時 %.1f 秒" % (time.time() - t0))

t0 = time.time()
with ThreadPoolExecutor() as pool:             # 平行執行：約 0.5 秒
    results = list(pool.map(run_one, calls))   # map 會保持原本順序
print("平行執行耗時 %.1f 秒" % (time.time() - t0))

messages += [{"role": "assistant", "content": r.content},
             {"role": "user", "content": results}]   # 重點：所有 tool_result 放在「同一則」user 訊息
r = client.messages.create(model="mock", max_tokens=500, tools=tools, messages=messages)
print(r.content[0].text)
