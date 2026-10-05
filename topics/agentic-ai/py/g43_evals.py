# -*- coding: utf-8 -*-
"""第 43 課：評估（evals）——沒有量測，就不知道改了提示是變好還是變壞。
一組測試案例 + 自動評分（規則或 LLM 評審）+ 通過率；每次修改後都重跑。"""
import json
from mockllm import MockClient, text

CASES = [
    {"q": "訂單 A123 到哪了？", "expect_tool": "get_order", "must": ["A123"]},
    {"q": "我要退貨", "expect_tool": "start_return", "must": []},
    {"q": "你們的營業時間？", "expect_tool": None, "must": ["9"]},
    {"q": "幫我把帳號刪掉", "expect_tool": "escalate", "must": []},
    {"q": "訂單 B777 可以改地址嗎？", "expect_tool": "get_order", "must": ["B777"]},
]

def agent_v1(q):                       # 版本 1：簡單的關鍵字規則（模擬一個較弱的提示）
    if "訂單" in q:
        return {"tool": "get_order", "args": {"id": q.split("訂單 ")[1][:4]}, "reply": ""}
    if "退" in q:
        return {"tool": "start_return", "args": {}, "reply": ""}
    return {"tool": None, "args": {}, "reply": "請問還有什麼可以幫忙？"}

def agent_v2(q):                       # 版本 2：改進後的提示（補上營業時間與刪帳號要轉人工）
    r = agent_v1(q)
    if "營業" in q:
        r["reply"] = "我們的營業時間是 9:00～18:00。"
    if "刪" in q:
        r = {"tool": "escalate", "args": {}, "reply": ""}
    return r

def grade(case, out):
    ok_tool = out["tool"] == case["expect_tool"]
    blob = json.dumps(out, ensure_ascii=False)
    ok_must = all(m in blob for m in case["must"])
    return ok_tool and ok_must

for name, agent in [("v1", agent_v1), ("v2", agent_v2)]:
    res = [grade(c, agent(c["q"])) for c in CASES]
    print("%s 通過率 %d/%d  %s" % (name, sum(res), len(res), " ".join("✓" if r else "✗" for r in res)))

# LLM 當評審：適合沒有標準答案的開放題（要給明確評分標準，並抽樣人工檢查評審本身）
judge = MockClient(lambda ctx: text(json.dumps({"score": 4, "reason": "有回答時間，但沒提假日"}, ensure_ascii=False)))
v = judge.messages.create(model="mock", max_tokens=200, system="依 1～5 分評分：正確、完整、語氣。輸出 JSON。",
                          messages=[{"role": "user", "content": "問：營業時間？答：我們的營業時間是 9:00～18:00。"}])
print("LLM 評審：", v.content[0].text)
