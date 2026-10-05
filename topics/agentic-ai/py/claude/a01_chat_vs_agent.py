# -*- coding: utf-8 -*-
"""第 1 課（Claude API 版）：同一段代理迴圈，換成真的 Claude。
執行前：pip install anthropic，並設定 ANTHROPIC_API_KEY。"""
import json
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"


def get_weather(city):
    # 示範用的假資料；實務上這裡會去呼叫真正的氣象 API
    return {"city": city, "temp_c": 27, "rain_prob": 0.7}


tools = [{"name": "get_weather", "description": "查詢城市即時天氣，回傳攝氏溫度與降雨機率（0～1）。",
          "input_schema": {"type": "object", "properties": {"city": {"type": "string", "description": "城市名稱，例如：台北"}},
                           "required": ["city"]}}]
messages = [{"role": "user", "content": "台北現在幾度？要帶傘嗎？"}]

while True:
    r = client.messages.create(model=MODEL, max_tokens=16000, tools=tools, messages=messages)
    messages.append({"role": "assistant", "content": r.content})   # 原封不動接回去
    if r.stop_reason != "tool_use":
        break
    results = []
    for b in r.content:
        if b.type == "tool_use":
            print("Claude 要求執行：", b.name, b.input)
            results.append({"type": "tool_result", "tool_use_id": b.id,
                            "content": json.dumps(get_weather(**b.input), ensure_ascii=False)})
    messages.append({"role": "user", "content": results})

print(next(b.text for b in r.content if b.type == "text"))
