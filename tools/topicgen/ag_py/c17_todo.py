# -*- coding: utf-8 -*-
"""第 17 課：待辦清單工具——讓代理把大任務拆成小項目並追蹤進度（Claude Code 的 TodoWrite 就是這個概念）。"""
import json
from mockllm import MockClient, text, tool_use

TODOS = []

def todo_write(todos):
    """整份清單覆寫：模型每次送出完整的最新狀態。"""
    TODOS[:] = todos
    icon = {"pending": "☐", "in_progress": "▶", "completed": "☑"}
    print("   " + "  ".join("%s %s" % (icon[t["status"]], t["content"]) for t in TODOS))
    return "ok"

def work(name):
    return "%s 完成" % name

ITEMS = ["讀需求", "寫程式", "寫測試", "跑測試"]

def policy(ctx):
    k = ctx.turn                             # 第 0 輪建立清單；之後每兩輪：標記進行中 → 做事並標記完成
    if k == 0:
        return tool_use("todo_write", {"todos": [{"content": c, "status": "pending"} for c in ITEMS]})
    idx, phase = divmod(k - 1, 2)
    if idx >= len(ITEMS):
        return text("全部 %d 項都完成了。" % len(ITEMS))
    st = lambda j: "completed" if j < idx or (j == idx and phase == 1) else ("in_progress" if j == idx else "pending")
    calls = [tool_use("todo_write", {"todos": [{"content": c, "status": st(j)} for j, c in enumerate(ITEMS)]})]
    if phase == 0:
        calls.append(tool_use("work", {"name": ITEMS[idx]}))
    return calls

tools = [{"name": "todo_write", "description": "更新待辦清單", "input_schema": {"type": "object", "properties": {"todos": {"type": "array"}}}},
         {"name": "work", "description": "執行一項工作", "input_schema": {"type": "object", "properties": {"name": {"type": "string"}}}}]
impl = {"todo_write": todo_write, "work": work}
client, msgs = MockClient(policy), [{"role": "user", "content": "幫我加一個登入功能"}]
while True:
    r = client.messages.create(model="mock", max_tokens=800, tools=tools, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    msgs.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(impl[b.name](**b.input), ensure_ascii=False)}
                                             for b in r.content if b.type == "tool_use"]})
print(r.content[0].text, "清單讓代理（和你）隨時知道：做到哪、還剩什麼。")
