# -*- coding: utf-8 -*-
"""第 48 課：案例剖析——Claude Code 與 Codex 這類程式代理，本質上就是這門課教的架構：
一個代理迴圈 ＋ 檔案／搜尋／終端機工具 ＋ 待辦清單 ＋ 專案說明檔 ＋ 權限模式 ＋ 上下文壓縮 ＋ 子代理。
這裡用 60 行模擬一次『修 bug』任務的軌跡，標出每一步用到哪一課的概念。"""
from mockllm import MockClient, text, tool_use

PROJECT_MEMO = "# CLAUDE.md / AGENTS.md\n- 測試指令：python -m unittest\n- 不要修改 tests/ 底下的檔案"
PERMISSION = "ask_before_edit"          # 權限模式：plan（只看不改）/ ask_before_edit / auto

TRAJ = [
    ("todo_write", {"todos": ["重現錯誤", "找出原因", "修改", "驗證"]}, "第 17 課 待辦清單"),
    ("bash", {"command": "python -m unittest"}, "第 27 課 執行程式／第 41 課 沙箱"),
    ("grep", {"pattern": "def total"}, "第 26 課 按需載入上下文"),
    ("read", {"path": "pricing.py"}, "第 28 課 檔案工具"),
    ("edit", {"path": "pricing.py", "old": "s - discount", "new": "s * (1 - discount)"}, "第 28 課 str_replace／第 40 課 核准"),
    ("bash", {"command": "python -m unittest"}, "第 18 課 用外部回饋自我修正"),
]

def policy(ctx):
    if ctx.turn < len(TRAJ):
        name, args, _ = TRAJ[ctx.turn]
        return tool_use(name, args)
    return text("已修好：折扣算法錯誤，所有測試通過。")

FAKE = {"todo_write": "清單已更新", "grep": "pricing.py:1: def total(prices, discount=0):",
        "read": "…return round(s - discount, 2)", "edit": "已修改"}
bash_runs = [0]

def run_tool(name, args):
    if name == "bash":
        bash_runs[0] += 1
        return "FAILED (failures=1)" if bash_runs[0] == 1 else "OK"
    if name == "edit" and PERMISSION == "ask_before_edit":
        print("      🙋 權限模式 %s：詢問使用者 → 允許" % PERMISSION)
    return FAKE[name]

tools = [{"name": n, "description": n, "input_schema": {"type": "object"}} for n in ("todo_write", "bash", "grep", "read", "edit")]
client = MockClient(policy)
msgs = [{"role": "user", "content": "test_discount 失敗了，幫我修"}]
print("系統提示會自動附上專案說明檔：\n" + PROJECT_MEMO + "\n")
step = 0
while True:
    r = client.messages.create(model="mock", max_tokens=1000, system=PROJECT_MEMO, tools=tools, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    b = r.content[0]
    print("%d. %-10s %s\n      （%s）" % (step + 1, b.name, b.input, TRAJ[step][2]))
    out = run_tool(b.name, b.input)
    print("      → %s" % out)
    msgs.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": b.id, "content": out}]})
    step += 1
print("✅", r.content[0].text)
