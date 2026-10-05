# -*- coding: utf-8 -*-
"""第 40 課（Claude API 版）：在工具迴圈中加入核准關卡。被拒絕時一樣要回 tool_result（is_error），Claude 才知道要調整。"""
import anthropic

client = anthropic.Anthropic()
RISK = {"read_file": "low", "delete_file": "high"}
tools = [{"name": "read_file", "description": "讀取檔案", "input_schema": {
              "type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
         {"name": "delete_file", "description": "刪除檔案（不可復原）", "input_schema": {
              "type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}]


def execute(name, args):
    return "（示範）已執行 %s %s" % (name, args)


messages = [{"role": "user", "content": "看一下 old.log 的內容，如果沒用就刪掉。"}]
while True:
    r = client.messages.create(model="claude-opus-5-5", max_tokens=16000, tools=tools, messages=messages)
    messages.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    results = []
    for b in r.content:
        if b.type != "tool_use":
            continue
        if RISK[b.name] == "high" and input("允許執行 %s %s？[y/N] " % (b.name, b.input)).strip().lower() != "y":
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": "使用者拒絕了這個動作", "is_error": True})
        else:
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": execute(b.name, b.input)})
    messages.append({"role": "user", "content": results})
print(next(b.text for b in r.content if b.type == "text"))
