# -*- coding: utf-8 -*-
"""第 33 課（Claude API 版）：把「子代理」包成一個工具。主代理呼叫 delegate(task) 時，
我們開一段全新的對話給子代理執行，只把它的最終摘要交回主代理。"""
import anthropic

client = anthropic.Anthropic()
DOCS = {"財報.txt": open(__file__, encoding="utf-8").read()}   # 換成你的大型文件


def read_doc(name):
    return DOCS.get(name, "找不到文件")


def run_subagent(task):
    """子代理：自己的上下文、自己的工具，只回傳結論。"""
    tools = [{"name": "read_doc", "description": "讀取文件全文", "input_schema": {
        "type": "object", "properties": {"name": {"type": "string"}}, "required": ["name"]}}]
    msgs = [{"role": "user", "content": task + "\n可用文件：" + "、".join(DOCS) + "\n最後用 100 字內回報結論。"}]
    while True:
        r = client.messages.create(model="claude-opus-5-5", max_tokens=16000, tools=tools, messages=msgs,
                                   output_config={"effort": "low"})          # 子任務單純：低 effort 省 token
        msgs.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":
            return "".join(b.text for b in r.content if b.type == "text")
        msgs.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": b.id, "content": read_doc(**b.input)}
                                                 for b in r.content if b.type == "tool_use"]})


main_tools = [{"name": "delegate", "description": "把一個需要大量閱讀的子任務交給子代理，回傳精簡結論",
               "input_schema": {"type": "object", "properties": {"task": {"type": "string"}}, "required": ["task"]}}]
messages = [{"role": "user", "content": "請分析我們的財報重點，給我三點建議。"}]
while True:
    r = client.messages.create(model="claude-opus-5-5", max_tokens=16000, tools=main_tools, messages=messages)
    messages.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    results = []
    for b in r.content:
        if b.type == "tool_use":
            print("主代理派工：", b.input["task"])
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": run_subagent(b.input["task"])})
    messages.append({"role": "user", "content": results})
print(next(b.text for b in r.content if b.type == "text"))
