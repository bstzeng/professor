# -*- coding: utf-8 -*-
"""第 40 課：人在迴路（human-in-the-loop）——危險動作執行前先問人。
依風險分級：讀取＝自動放行；寫入＝問一次；不可逆（刪除、付款、寄信）＝每次都問。"""
import json
from mockllm import MockClient, text, tool_use

RISK = {"read_file": "low", "write_file": "medium", "delete_file": "high", "send_email": "high"}
FS = {"draft.md": "草稿", "old.log": "舊紀錄"}
approved_once = set()

def ask_human(name, args, answers):
    """真實程式用 input()；這裡用預先準備的答案模擬使用者的選擇。"""
    ans = answers.pop(0)
    print("   🙋 代理想執行 %s(%s)，允許嗎？[y/n] → %s" % (name, json.dumps(args, ensure_ascii=False), ans))
    return ans == "y"

def gate(name, args, answers):
    r = RISK[name]
    if r == "low" or (r == "medium" and name in approved_once):
        return True
    ok = ask_human(name, args, answers)
    if ok and r == "medium":
        approved_once.add(name)
    return ok

IMPL = {"read_file": lambda path: FS[path], "write_file": lambda path, text: FS.__setitem__(path, text) or "ok",
        "delete_file": lambda path: FS.pop(path) and "deleted", "send_email": lambda to, body: "sent"}
PLAN = [tool_use("read_file", {"path": "draft.md"}), tool_use("write_file", {"path": "draft.md", "text": "定稿"}),
        tool_use("delete_file", {"path": "old.log"}), tool_use("send_email", {"to": "boss@co.com", "body": "定稿完成"})]

client = MockClient(lambda ctx: PLAN[ctx.turn] if ctx.turn < len(PLAN) else text("處理完畢（被拒絕的動作已略過）。"))
tools = [{"name": n, "description": n, "input_schema": {"type": "object"}} for n in RISK]
msgs, answers = [{"role": "user", "content": "把草稿定稿、清掉舊紀錄，然後寄信給老闆"}], ["y", "y", "n"]
while True:
    r = client.messages.create(model="mock", max_tokens=500, tools=tools, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    b = r.content[0]
    if gate(b.name, b.input, answers):
        res = {"type": "tool_result", "tool_use_id": b.id, "content": str(IMPL[b.name](**b.input))}
        print("   ✓ 執行 %s（風險：%s）" % (b.name, RISK[b.name]))
    else:      # 被拒絕也要回 tool_result，讓模型知道並調整
        res = {"type": "tool_result", "tool_use_id": b.id, "content": "使用者拒絕了這個動作", "is_error": True}
        print("   ✗ 使用者拒絕 %s" % b.name)
    msgs.append({"role": "user", "content": [res]})
print(r.content[0].text, "目前檔案：", FS)
