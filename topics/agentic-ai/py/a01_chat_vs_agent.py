# -*- coding: utf-8 -*-
"""第 1 課：聊天機器人 vs 代理——差別在「有沒有迴圈和工具」。"""
import json
from mockllm import MockClient, text, tool_use, script

# ① 聊天：問一次、答一次。模型不知道今天的天氣，只能猜或拒答。
chat = MockClient(lambda ctx: text("我無法得知即時天氣，建議你查氣象局網站。"))
r = chat.messages.create(model="mock", max_tokens=200,
                         messages=[{"role": "user", "content": "台北現在幾度？要帶傘嗎？"}])
print("【聊天】", r.content[0].text)

# ② 代理：模型可以「要求」我們幫它執行工具，看到結果後再決定下一步。
def get_weather(city):                      # 一個真正會被執行的 Python 函式
    return {"city": city, "temp_c": 27, "rain_prob": 0.7}

agent = MockClient(script(
    tool_use("get_weather", {"city": "台北"}),                        # 第 1 步：先查資料
    lambda ctx: text("台北現在 %d°C，降雨機率 %d%%，建議帶傘。" % (
        ctx.data()["temp_c"], ctx.data()["rain_prob"] * 100)),       # 第 2 步：讀工具結果再回答
))
tools = [{"name": "get_weather", "description": "查詢城市即時天氣",
          "input_schema": {"type": "object", "properties": {"city": {"type": "string"}}, "required": ["city"]}}]
messages = [{"role": "user", "content": "台北現在幾度？要帶傘嗎？"}]
while True:                                 # ← 這個迴圈就是「代理」的核心
    r = agent.messages.create(model="mock", max_tokens=500, messages=messages, tools=tools)
    messages.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    for b in r.content:
        if b.type == "tool_use":
            print("【代理】模型要求執行：%s(%s)" % (b.name, b.input))
            result = get_weather(**b.input)
            messages.append({"role": "user", "content": [
                {"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(result, ensure_ascii=False)}]})
print("【代理】", r.content[0].text)
print("模型被呼叫了 %d 次" % agent.calls)
