# -*- coding: utf-8 -*-
"""第 50 課：代理常見的失敗模式，以及每一種的偵測方法（用規則掃描一段代理軌跡）。"""
import json
from collections import Counter

TRACE = [  # 一段（虛構的）有問題的代理軌跡
    {"tool": "search", "args": {"q": "Q3 營收"}, "result": "找到 3 筆"},
    {"tool": "read", "args": {"path": "q3.csv"}, "result": "錯誤：檔案不存在"},
    {"tool": "read", "args": {"path": "q3.csv"}, "result": "錯誤：檔案不存在"},
    {"tool": "read", "args": {"path": "q3.csv"}, "result": "錯誤：檔案不存在"},
    {"tool": "get_revenue_magic", "args": {}, "result": "錯誤：沒有這個工具"},
    {"tool": "final", "args": {"text": "Q3 營收為 1.2 億元，成長 30%。"}, "result": ""},
]

def detect(trace):
    issues = []
    calls = Counter(json.dumps([s["tool"], s["args"]], sort_keys=True) for s in trace)
    for k, n in calls.items():
        if n >= 3:
            issues.append("重複迴圈：%s 被呼叫了 %d 次（同樣的參數、同樣的錯誤）" % (k, n))
    for s in trace:
        if "沒有這個工具" in s["result"]:
            issues.append("幻想工具：呼叫了不存在的 %s" % s["tool"])
    ok_data = any(s["tool"] == "read" and "錯誤" not in s["result"] for s in trace)
    final = trace[-1]["args"].get("text", "")
    if any(ch.isdigit() for ch in final) and not ok_data:
        issues.append("無根據的結論：最終答案有具體數字，但從未成功讀到任何資料")
    return issues

for i in detect(TRACE):
    print("⚠", i)
print("""
其他常見失敗：
  · 過早宣告完成（說修好了，其實沒跑測試）  → 要求用外部驗證（測試、檢查清單）
  · 偏離任務（越做越多、改了不該改的檔案）    → 清楚的範圍說明＋權限限制
  · 上下文腐化（對話太長、忘了最初的要求）    → 待辦清單、摘要、子代理
  · 對工具結果過度信任（被注入、資料錯誤）    → 交叉驗證、標記不可信資料""")
