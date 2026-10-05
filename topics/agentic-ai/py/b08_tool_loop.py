# -*- coding: utf-8 -*-
"""第 8 課：通用的工具迴圈——任何工具、任何步數都適用的寫法。"""
import json
from mockllm import MockClient, text, tool_use

# 一個小型「檔案系統」與三個工具
FILES = {"todo.txt": "買牛奶\n繳電費\n寫報告", "notes.txt": "週五開會"}

def list_files():
    return sorted(FILES)

def read_file(path):
    return FILES[path]

def count_lines(text):
    return len(text.splitlines())

REGISTRY = {f.__name__: f for f in (list_files, read_file, count_lines)}
TOOLS = [{"name": "list_files", "description": "列出所有檔案", "input_schema": {"type": "object", "properties": {}}},
         {"name": "read_file", "description": "讀取檔案內容", "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
         {"name": "count_lines", "description": "計算文字行數", "input_schema": {"type": "object", "properties": {"text": {"type": "string"}}, "required": ["text"]}}]

def policy(ctx):                          # 假模型：依照「目前知道了什麼」決定下一步
    seen = {name: json.loads(out) for name, out, _ in ctx.all_results()}
    if "list_files" not in seen:
        return tool_use("list_files", {})
    if "read_file" not in seen:
        target = next(f for f in seen["list_files"] if "todo" in f)
        return tool_use("read_file", {"path": target})
    if "count_lines" not in seen:
        return tool_use("count_lines", {"text": seen["read_file"]})
    return text("待辦清單有 %d 項：%s" % (seen["count_lines"], "、".join(seen["read_file"].splitlines())))

def run(client, task, max_turns=8):
    messages = [{"role": "user", "content": task}]
    for turn in range(max_turns):
        r = client.messages.create(model="mock", max_tokens=1000, tools=TOOLS, messages=messages)
        messages.append({"role": "assistant", "content": r.content})
        if r.stop_reason == "end_turn":
            return next(b.text for b in r.content if b.type == "text")
        results = []
        for b in r.content:
            if b.type != "tool_use":
                continue
            out = REGISTRY[b.name](**b.input)                      # 依名稱分派到對應函式
            print("  turn %d → %s%s = %s" % (turn + 1, b.name, tuple(b.input.values()), out))
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(out, ensure_ascii=False)})
        messages.append({"role": "user", "content": results})
    raise RuntimeError("超過最大輪數")

print(run(MockClient(policy), "我的待辦清單有幾項？"))
