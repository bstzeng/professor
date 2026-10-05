# -*- coding: utf-8 -*-
"""第 32 課（Claude API 版）：迷你程式代理。用法：
    python e32_mini_coder.py 專案目錄 "要完成的任務"
Claude 會用 list_files / read_file / edit_file / run_tests 四個工具自己完成任務。
⚠ 它會修改目錄裡的檔案、執行測試：請在 git 版本控制或副本上使用，並在可信任的專案中執行。"""
import json
import subprocess
import sys
from pathlib import Path
import anthropic

client = anthropic.Anthropic()
WS = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
TASK = sys.argv[2] if len(sys.argv) > 2 else "執行測試，找出失敗原因並修好，直到全部通過。"


def safe(path):
    p = (WS / path).resolve()
    if not p.is_relative_to(WS):
        raise PermissionError("路徑超出專案目錄")
    return p


def list_files():
    return "\n".join(str(p.relative_to(WS)) for p in sorted(WS.rglob("*.py")) if ".git" not in p.parts)


def read_file(path):
    return safe(path).read_text(encoding="utf-8")


def edit_file(path, old, new):
    p = safe(path)
    s = p.read_text(encoding="utf-8")
    if s.count(old) != 1:
        raise ValueError("old 必須剛好出現一次（目前 %d 次），請多帶一點上下文" % s.count(old))
    p.write_text(s.replace(old, new), encoding="utf-8")
    return "已修改"


def run_tests():
    p = subprocess.run([sys.executable, "-m", "unittest", "-q"], cwd=WS, capture_output=True, text=True, timeout=120)
    return (p.stdout + p.stderr)[-4000:] or "（沒有輸出）"


IMPL = {"list_files": list_files, "read_file": read_file, "edit_file": edit_file, "run_tests": run_tests}
TOOLS = [
    {"name": "list_files", "description": "列出專案中所有 .py 檔", "input_schema": {"type": "object", "properties": {}}},
    {"name": "read_file", "description": "讀取一個檔案的完整內容", "input_schema": {
        "type": "object", "properties": {"path": {"type": "string", "description": "相對於專案根目錄的路徑"}}, "required": ["path"]}},
    {"name": "edit_file", "description": "把檔案中唯一出現一次的 old 字串換成 new。old 要包含足夠上下文以確保唯一。",
     "input_schema": {"type": "object", "properties": {"path": {"type": "string"}, "old": {"type": "string"}, "new": {"type": "string"}},
                      "required": ["path", "old", "new"]}},
    {"name": "run_tests", "description": "用 unittest 執行全部測試，回傳輸出結尾", "input_schema": {"type": "object", "properties": {}}},
]
SYSTEM = ("你是程式代理，在使用者的專案目錄中工作。先了解現況再修改；每次修改後都要跑測試驗證。"
          "不要修改測試來讓它通過。完成後用兩三句話說明你改了什麼、為什麼。")

messages = [{"role": "user", "content": TASK}]
for step in range(30):
    r = client.messages.create(model="claude-opus-5-5", max_tokens=16000, system=SYSTEM, tools=TOOLS, messages=messages)
    messages.append({"role": "assistant", "content": r.content})
    for b in r.content:
        if b.type == "text" and b.text.strip():
            print("🤖", b.text)
    if r.stop_reason != "tool_use":
        break
    results = []
    for b in r.content:
        if b.type != "tool_use":
            continue
        print("   🔧", b.name, json.dumps(b.input, ensure_ascii=False)[:120])
        try:
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": IMPL[b.name](**b.input)})
        except Exception as e:
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": "錯誤：%s" % e, "is_error": True})
    messages.append({"role": "user", "content": results})
