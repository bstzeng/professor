# -*- coding: utf-8 -*-
"""第 28 課（Claude API 版）：Anthropic 定義的文字編輯工具（text_editor_20250728）。
不用寫 input_schema——Claude 已經知道怎麼用；你負責實作 view / create / str_replace / insert。"""
import tempfile
from pathlib import Path
import anthropic

client = anthropic.Anthropic()
ROOT = Path(tempfile.mkdtemp()).resolve()
(ROOT / "config.py").write_text("DEBUG = True\nPORT = 8000\n", encoding="utf-8")


def safe(path):
    p = (ROOT / path.lstrip("/")).resolve()
    if not p.is_relative_to(ROOT):
        raise PermissionError("路徑在專案目錄之外")
    return p


def editor(inp):
    cmd, p = inp["command"], safe(inp["path"])
    if cmd == "view":
        return p.read_text(encoding="utf-8") if p.is_file() else "\n".join(x.name for x in p.iterdir())
    if cmd == "create":
        p.write_text(inp["file_text"], encoding="utf-8")
        return "已建立"
    if cmd == "str_replace":
        s = p.read_text(encoding="utf-8")
        if s.count(inp["old_str"]) != 1:
            raise ValueError("old_str 必須剛好出現一次")
        p.write_text(s.replace(inp["old_str"], inp["new_str"]), encoding="utf-8")
        return "已修改"
    if cmd == "insert":
        lines = p.read_text(encoding="utf-8").split("\n")
        lines.insert(inp["insert_line"], inp["insert_text"])
        p.write_text("\n".join(lines), encoding="utf-8")
        return "已插入"
    raise ValueError("未知指令 " + cmd)


tools = [{"type": "text_editor_20250728", "name": "str_replace_based_edit_tool"}]
messages = [{"role": "user", "content": "把 /config.py 的 DEBUG 關掉，並把 PORT 改成 8080。"}]
while True:
    r = client.messages.create(model="claude-opus-5-5", max_tokens=16000, tools=tools, messages=messages)
    messages.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    results = []
    for b in r.content:
        if b.type == "tool_use":
            try:
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": editor(b.input)})
            except Exception as e:
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": str(e), "is_error": True})
    messages.append({"role": "user", "content": results})
print((ROOT / "config.py").read_text(encoding="utf-8"))
