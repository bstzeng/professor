# -*- coding: utf-8 -*-
"""第 24 課：長期記憶——上下文視窗會清空，但檔案不會。
給代理 remember / recall 兩個工具，把重要事實寫進 JSON 檔，下一次對話再讀回來。"""
import json
import os
import tempfile
from mockllm import MockClient, text, tool_use

PATH = os.path.join(tempfile.gettempdir(), "agent_memory_demo.json")
if os.path.exists(PATH):
    os.remove(PATH)

def remember(key, value):
    mem = json.load(open(PATH, encoding="utf-8")) if os.path.exists(PATH) else {}
    mem[key] = value
    json.dump(mem, open(PATH, "w", encoding="utf-8"), ensure_ascii=False)
    return "已記住 %s" % key

def recall(query):
    mem = json.load(open(PATH, encoding="utf-8")) if os.path.exists(PATH) else {}
    return {k: v for k, v in mem.items() if any(w in k for w in query.split())} or "沒有相關記憶"

IMPL = {"remember": remember, "recall": recall}
TOOLS = [{"name": n, "description": d, "input_schema": {"type": "object", "properties": p}} for n, d, p in [
    ("remember", "把關於使用者的長期事實存起來", {"key": {"type": "string"}, "value": {"type": "string"}}),
    ("recall", "查詢先前記住的事實", {"query": {"type": "string"}})]]

def policy(ctx):
    q = ctx.user_text(first=True)
    if "吃素" in q and ctx.turn == 0:
        return [text("好的，我記下來。"), tool_use("remember", {"key": "飲食 偏好", "value": "吃素、對花生過敏"})]
    if "推薦" in q and ctx.turn == 0:
        return tool_use("recall", {"query": "飲食"})
    if "推薦" in q:
        return text("根據你的偏好（%s），推薦：蔬菜咖哩、豆腐蓋飯（都不含花生）。" % list(ctx.data().values())[0])
    return text("記好了！")

def session(user_msg):
    client, msgs = MockClient(policy), [{"role": "user", "content": user_msg}]   # 每次都是全新的對話
    while True:
        r = client.messages.create(model="mock", max_tokens=500, tools=TOOLS, messages=msgs)
        msgs.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":
            return r.content[-1].text
        res = []
        for b in r.content:
            if b.type == "tool_use":
                out = IMPL[b.name](**b.input)
                print("   [%s] %s → %s" % (b.name, b.input, out))
                res.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(out, ensure_ascii=False)})
        msgs.append({"role": "user", "content": res})

print("對話 1：", session("我吃素，而且對花生過敏。"))
print("（對話結束，上下文清空）")
print("對話 2：", session("晚餐推薦什麼？"))
print("記憶檔內容：", open(PATH, encoding="utf-8").read())
