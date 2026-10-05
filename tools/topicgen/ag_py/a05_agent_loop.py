# -*- coding: utf-8 -*-
"""第 5 課：代理迴圈的骨架——感知 → 思考 → 行動 → 觀察，直到完成。
這 25 行就是所有代理（包括 Claude Code、Codex）的核心。"""
import json
from mockllm import MockClient, text, tool_use, script

def calculator(expression):
    # 只允許數字與運算符號，避免執行任意程式碼
    if not set(expression) <= set("0123456789+-*/(). "):
        raise ValueError("不合法的算式")
    return eval(expression)

TOOLS = {"calculator": calculator}
schemas = [{"name": "calculator", "description": "計算四則運算算式",
            "input_schema": {"type": "object", "properties": {"expression": {"type": "string"}}, "required": ["expression"]}}]

def run_agent(client, task, max_steps=10):
    messages = [{"role": "user", "content": task}]                         # 感知：任務進入
    for step in range(1, max_steps + 1):
        r = client.messages.create(model="mock", max_tokens=1000, messages=messages, tools=schemas)  # 思考
        messages.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":                                    # 不再要工具 → 完成
            return r.content[-1].text, step
        results = []
        for b in r.content:
            if b.type == "tool_use":
                out = TOOLS[b.name](**b.input)                             # 行動
                print("  第 %d 輪 行動：%s(%s) → 觀察：%s" % (step, b.name, b.input, out))
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": str(out)})
        messages.append({"role": "user", "content": results})              # 觀察：結果回到對話
    return "超過步數上限，停止", max_steps

client = MockClient(script(
    [text("先算總價。"), tool_use("calculator", {"expression": "3*120 + 2*85"})],
    lambda c: [text("再打九折。"), tool_use("calculator", {"expression": "%s * 0.9" % c.data()})],
    lambda c: text("總共要付 %s 元。" % c.data()),
))
answer, steps = run_agent(client, "3 杯 120 元的咖啡加 2 個 85 元的蛋糕，打九折後多少錢？")
print("答案：%s（共 %d 輪）" % (answer, steps))
