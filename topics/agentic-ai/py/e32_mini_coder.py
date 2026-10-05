# -*- coding: utf-8 -*-
"""第 32 課：實作一個迷你程式代理（mini coding agent）——讀檔、跑測試、修改、再跑測試，直到全部通過。
這就是 Claude Code、Codex 這類工具最核心的迴圈。這個檔案可以直接執行，不需要 API 金鑰。"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from mockllm import MockClient, text, tool_use

# ── 1. 準備一個有 bug 的小專案 ──
WS = Path(tempfile.mkdtemp(prefix="mini_coder_")).resolve()
(WS / "pricing.py").write_text('''def total(prices, discount=0):
    """加總價格後套用折扣（discount 為 0～1 的比例）。"""
    s = sum(prices)
    return round(s - discount, 2)
''', encoding="utf-8")
(WS / "test_pricing.py").write_text('''import unittest
from pricing import total

class T(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(total([100, 50]), 150)
    def test_discount(self):
        self.assertEqual(total([100, 100], 0.1), 180)
''', encoding="utf-8")

# ── 2. 工具 ──
def safe(path):
    p = (WS / path).resolve()
    if not p.is_relative_to(WS):
        raise PermissionError("路徑超出專案目錄")
    return p

def read_file(path):
    return safe(path).read_text(encoding="utf-8")

def edit_file(path, old, new):
    p = safe(path)
    s = p.read_text(encoding="utf-8")
    if s.count(old) != 1:
        raise ValueError("old 必須剛好出現一次（目前 %d 次）" % s.count(old))
    p.write_text(s.replace(old, new), encoding="utf-8")
    return "已修改 %s" % path

def run_tests():
    p = subprocess.run([sys.executable, "-m", "unittest", "-q"], cwd=WS, capture_output=True, text=True, timeout=30)
    return (p.stdout + p.stderr)[-1500:]

IMPL = {"read_file": read_file, "edit_file": edit_file, "run_tests": run_tests}
TOOLS = [{"name": "read_file", "description": "讀取專案中的檔案", "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}},
         {"name": "edit_file", "description": "把檔案中唯一出現的 old 字串換成 new", "input_schema": {"type": "object", "properties": {
             "path": {"type": "string"}, "old": {"type": "string"}, "new": {"type": "string"}}, "required": ["path", "old", "new"]}},
         {"name": "run_tests", "description": "執行全部單元測試並回傳輸出", "input_schema": {"type": "object", "properties": {}}}]

# ── 3. 假模型：真的「讀」工具輸出來決定下一步（不是寫死的劇本）──
def policy(ctx):
    hist = ctx.all_results()
    last_name, last_out = (hist[-1][0], json.loads(hist[-1][1])) if hist else (None, None)
    if last_name is None:
        return [text("先跑測試看看現況。"), tool_use("run_tests", {})]
    if last_name == "run_tests":
        if re.search(r"\bOK\b", last_out) and "FAILED" not in last_out:
            return text("所有測試都通過了。修正內容：折扣應該是乘上 (1 - discount)，而不是減去 discount。")
        return [text("有測試失敗，讀被測的程式碼。"), tool_use("read_file", {"path": "pricing.py"})]
    if last_name == "read_file":
        if "s - discount" in last_out:
            return [text("bug 找到了：把比例當成金額減掉。"),
                    tool_use("edit_file", {"path": "pricing.py", "old": "s - discount", "new": "s * (1 - discount)"})]
    return [text("修好了，再跑一次測試確認。"), tool_use("run_tests", {})]

# ── 4. 代理迴圈 ──
client, msgs = MockClient(policy), [{"role": "user", "content": "test_pricing 有測試沒過，請修好。"}]
for step in range(1, 11):
    r = client.messages.create(model="mock", max_tokens=2000, tools=TOOLS, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})
    for b in r.content:
        if b.type == "text":
            print("🤖", b.text)
    if r.stop_reason != "tool_use":
        break
    results = []
    for b in r.content:
        if b.type == "tool_use":
            try:
                out, err = IMPL[b.name](**b.input), False
            except Exception as e:
                out, err = "錯誤：%s" % e, True
            print("   🔧 %s%s\n      %s" % (b.name, json.dumps(b.input, ensure_ascii=False) if b.input else "()",
                                        out.strip().splitlines()[-1] if out.strip() else ""))
            results.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(out, ensure_ascii=False), "is_error": err})
    msgs.append({"role": "user", "content": results})
print("\n修改後的 pricing.py：\n" + read_file("pricing.py"))
