# -*- coding: utf-8 -*-
"""第 17 課（Claude API 版）：給 Claude 一個 todo_write 工具，要求它先列清單、邊做邊更新。"""
import json
import anthropic

client = anthropic.Anthropic()
TODOS = []
tools = [{
    "name": "todo_write",
    "description": "建立或更新整份待辦清單。開始多步驟工作前先列出清單；每開始或完成一項就送出完整的最新清單。",
    "input_schema": {"type": "object", "properties": {"todos": {"type": "array", "items": {
        "type": "object", "properties": {"content": {"type": "string"},
                                         "status": {"type": "string", "enum": ["pending", "in_progress", "completed"]}},
        "required": ["content", "status"]}}}, "required": ["todos"]},
}]
messages = [{"role": "user", "content": "規劃「把部落格從 WordPress 搬到靜態網站」的工作，用 todo_write 列出清單，並把第一項標成進行中。"}]
while True:
    r = client.messages.create(model="claude-opus-5-5", max_tokens=16000, tools=tools, messages=messages)
    messages.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    results = []
    for b in r.content:
        if b.type == "tool_use":
            TODOS[:] = b.input["todos"]
            for t in TODOS:
                print({"pending": "☐", "in_progress": "▶", "completed": "☑"}[t["status"]], t["content"])
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": "清單已更新"})
    messages.append({"role": "user", "content": results})
print(json.dumps(TODOS, ensure_ascii=False, indent=1))
