# -*- coding: utf-8 -*-
"""第 11 課：好工具 vs 壞工具。用一個簡單的「檢查器」幫工具定義打分數。"""

def lint_tool(t):
    issues = []
    d = t.get("description", "")
    if len(d) < 20:
        issues.append("描述太短：要說明『做什麼、何時用、回傳什麼』")
    if not t["name"].replace("_", "").isalnum() or t["name"] in ("do", "run", "tool", "process"):
        issues.append("名稱太模糊：用動詞＋名詞，如 search_orders")
    props = t["input_schema"].get("properties", {})
    for k, v in props.items():
        if "description" not in v and "enum" not in v:
            issues.append("參數 %s 沒有說明" % k)
        if v.get("type") == "string" and any(w in k for w in ("date", "time")) and "format" not in v and "格式" not in v.get("description", ""):
            issues.append("參數 %s 沒說日期格式" % k)
    if len(props) > 6:
        issues.append("參數太多（%d 個）：考慮拆成多個工具" % len(props))
    if "required" not in t["input_schema"]:
        issues.append("沒有標出必填參數")
    return issues

bad = {"name": "do", "description": "查東西",
       "input_schema": {"type": "object", "properties": {"q": {"type": "string"}, "date": {"type": "string"}}}}
good = {"name": "search_orders",
        "description": "依客戶 email 與日期區間搜尋訂單，回傳訂單編號、金額與狀態的清單（最多 20 筆）。客戶詢問訂單狀況時使用。",
        "input_schema": {"type": "object", "properties": {
            "email": {"type": "string", "description": "客戶 email"},
            "start_date": {"type": "string", "description": "起始日期，格式 YYYY-MM-DD"},
            "status": {"type": "string", "enum": ["pending", "shipped", "delivered"]}},
            "required": ["email"]}}
for t in (bad, good):
    issues = lint_tool(t)
    print("%-14s 分數 %d/10" % (t["name"], max(0, 10 - 2 * len(issues))))
    for i in issues:
        print("   ✗", i)
print("\n原則：把工具當成寫給『新進同事』的說明書——模型只能讀到這些字。")
print("回傳也要精簡：只給模型需要的欄位，別把 5 萬字的原始 JSON 全丟回去。")
