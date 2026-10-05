# -*- coding: utf-8 -*-
"""第 51 課：更長時程的自主代理——從「幾分鐘的任務」走向「幾小時、幾天的任務」。
關鍵技術：進度檔（讓代理跨越多個上下文視窗接力）、定期驗證、可中斷可恢復。
這裡模擬一個代理在「每個上下文視窗只做得完 2 項工作」的限制下，靠進度檔完成 7 項工作。"""
import json
import os
import tempfile

PROGRESS = os.path.join(tempfile.gettempdir(), "long_task_progress.json")
if os.path.exists(PROGRESS):
    os.remove(PROGRESS)
FEATURES = ["使用者註冊", "登入", "購物車", "結帳", "訂單查詢", "退貨", "管理後台"]
PER_WINDOW = 2                                       # 一個上下文視窗大約只做得完 2 項

def one_session(n):
    """每個 session 都是全新的上下文：先讀進度檔，再接著做，最後寫回進度與交接筆記。"""
    p = json.load(open(PROGRESS, encoding="utf-8")) if os.path.exists(PROGRESS) else {"done": [], "notes": []}
    todo = [f for f in FEATURES if f not in p["done"]]
    if not todo:
        return False
    did = todo[:PER_WINDOW]
    p["done"] += did
    p["notes"].append("session %d：完成 %s；下一步：%s" % (n, "、".join(did), todo[PER_WINDOW] if len(todo) > PER_WINDOW else "無"))
    json.dump(p, open(PROGRESS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("Session %d（全新上下文）讀進度 → 已完成 %d/%d → 這次做：%s" % (n, len(p["done"]) - len(did), len(FEATURES), "、".join(did)))
    return True

n = 1
while one_session(n):
    n += 1
print("\n進度檔最後的交接筆記：")
for line in json.load(open(PROGRESS, encoding="utf-8"))["notes"]:
    print("  ", line)
print("\n人類工程師換班時會寫交接；長時程代理也一樣——把狀態寫在檔案裡，而不是只放在腦子（上下文）裡。")
