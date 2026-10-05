# -*- coding: utf-8 -*-
"""第 4 課：工作流（程式決定步驟）vs 代理（模型決定步驟）。
同一個任務：「整理客訴信並決定要不要退款」。"""
import json
from mockllm import MockClient, text, tool_use

ORDERS = {"A123": {"paid": 1200, "days": 3, "status": "已到貨"}}

# ── 工作流：步驟寫死在程式裡，LLM 只負責其中幾格 ──
def workflow(email):
    llm = MockClient(lambda ctx: text("A123" if "訂單" in ctx.system else "產品瑕疵"))
    oid = llm.messages.create(model="mock", max_tokens=50, system="擷取訂單編號",
                              messages=[{"role": "user", "content": email}]).content[0].text      # 步驟 1
    reason = llm.messages.create(model="mock", max_tokens=50, system="分類客訴原因",
                                 messages=[{"role": "user", "content": email}]).content[0].text   # 步驟 2
    order = ORDERS[oid]                                                                           # 步驟 3
    ok = order["days"] <= 7 and reason == "產品瑕疵"                                              # 步驟 4（規則）
    return "工作流：訂單 %s，原因 %s → %s（固定 %d 步）" % (oid, reason, "退款" if ok else "轉人工", 4)

# ── 代理：給模型目標與工具，由它決定查什麼、查幾次 ──
def agent_policy(ctx):
    done = [r[0] for r in ctx.all_results()]
    if "lookup_order" not in done:
        return [text("先查訂單。"), tool_use("lookup_order", {"order_id": "A123"})]
    if "refund" not in done:
        o = json.loads(ctx.all_results()[0][1])
        if o["days"] <= 7:
            return [text("7 天內、屬瑕疵，可退款。"), tool_use("refund", {"order_id": "A123", "amount": o["paid"]})]
    return text("已為訂單 A123 退款，並回覆客戶致歉。")

def agent(email):
    oid = {"order_id": {"type": "string"}}
    tools = [{"name": "lookup_order", "description": "查訂單金額、天數與狀態", "input_schema": {"type": "object", "properties": oid}},
             {"name": "refund", "description": "退款給客戶", "input_schema": {"type": "object", "properties": dict(oid, amount={"type": "number"})}},
             {"name": "escalate", "description": "轉給真人客服", "input_schema": {"type": "object", "properties": oid}}]
    impl = {"lookup_order": lambda a: ORDERS[a["order_id"]], "refund": lambda a: {"ok": True, **a}}
    llm, msgs, steps = MockClient(agent_policy), [{"role": "user", "content": email}], 0
    while True:
        r = llm.messages.create(model="mock", max_tokens=300, messages=msgs, tools=tools)
        msgs.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":
            return "代理：%s（模型自己走了 %d 步工具）" % (r.content[-1].text, steps)
        res = []
        for b in r.content:
            if b.type == "tool_use":
                steps += 1
                print("   代理動作 %d：%s %s" % (steps, b.name, b.input))
                res.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(impl[b.name](b.input), ensure_ascii=False)})
        msgs.append({"role": "user", "content": res})

email = "你好，我的訂單 A123 收到的杯子有裂痕，請處理。"
print(workflow(email))
print(agent(email))
print("工作流：可預測、便宜、好除錯。代理：有彈性，但成本與行為較難預測。")
