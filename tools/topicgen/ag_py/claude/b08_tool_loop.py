# -*- coding: utf-8 -*-
"""第 8 課（Claude API 版）：通用工具迴圈。處理 end_turn、tool_use、max_tokens、refusal 等停止原因。"""
import json
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"
FILES = {"todo.txt": "買牛奶\n繳電費\n寫報告", "notes.txt": "週五開會"}
REGISTRY = {
    "list_files": lambda: sorted(FILES),
    "read_file": lambda path: FILES[path],
}
TOOLS = [{"name": "list_files", "description": "列出所有檔案名稱", "input_schema": {"type": "object", "properties": {}}},
         {"name": "read_file", "description": "讀取一個檔案的完整內容", "input_schema": {
             "type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}]


def run(task, max_turns=10):
    messages = [{"role": "user", "content": task}]
    for _ in range(max_turns):
        r = client.messages.create(model=MODEL, max_tokens=16000, tools=TOOLS, messages=messages)
        messages.append({"role": "assistant", "content": r.content})
        if r.stop_reason == "refusal":
            return "模型拒絕了這個請求"
        if r.stop_reason == "max_tokens":
            return "輸出被 max_tokens 截斷，請調高上限"
        if r.stop_reason != "tool_use":        # end_turn 等：完成
            return "".join(b.text for b in r.content if b.type == "text")
        results = []
        for b in r.content:
            if b.type == "tool_use":
                out = REGISTRY[b.name](**b.input)
                print("→", b.name, b.input)
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(out, ensure_ascii=False)})
        messages.append({"role": "user", "content": results})   # 所有結果放在同一則訊息
    raise RuntimeError("超過最大輪數")


print(run("我的待辦清單有幾項？"))
