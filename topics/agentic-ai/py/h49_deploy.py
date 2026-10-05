# -*- coding: utf-8 -*-
"""第 49 課：把代理部署上線——網路會斷、API 會限流、工具會逾時、程式會重啟。
重點：重試與退避、冪等性（重做不會重複扣款）、檢查點（重啟能接著做）、逾時。"""
import json
import os
import random
import tempfile
import time

class RateLimitError(Exception):
    pass

def flaky_api(rng):
    """模擬一個不穩定的 API：30% 機率回 429。"""
    if rng.random() < 0.3:
        raise RateLimitError("429 Too Many Requests")
    return "ok"

def with_retry(fn, max_tries=5, base=0.05, jitter=random.Random(0)):
    for i in range(max_tries):
        try:
            return fn()
        except RateLimitError as e:
            wait = base * (2 ** i) * (1 + jitter.random() * 0.2)     # 指數退避＋隨機抖動
            print("   重試 %d：%s，等 %.2f 秒" % (i + 1, e, wait))
            time.sleep(wait)
    raise RuntimeError("重試 %d 次仍失敗" % max_tries)

rng = random.Random(3)
print("呼叫結果：", with_retry(lambda: flaky_api(rng)))

# 冪等性：用 idempotency key 記錄已完成的副作用，重跑時不會重複執行
DONE = set()
def charge(order_id, amount):
    key = "charge:%s" % order_id
    if key in DONE:
        return "已處理過，略過（不會重複扣款）"
    DONE.add(key)
    return "扣款 %d 元" % amount
print(charge("A1", 500), "｜", charge("A1", 500))

# 檢查點：每完成一步就存檔，程式重啟後從中斷處繼續
CK = os.path.join(tempfile.gettempdir(), "agent_checkpoint_demo.json")
if os.path.exists(CK):
    os.remove(CK)
STEPS = ["下載資料", "清理", "分析", "產生報告"]

def run(crash_at=None):
    state = json.load(open(CK)) if os.path.exists(CK) else {"done": []}
    for s in STEPS:
        if s in state["done"]:
            continue
        if s == crash_at:
            print("   💥 在「%s」時程式當掉" % s)
            return
        state["done"].append(s)
        json.dump(state, open(CK, "w"), ensure_ascii=False)
        print("   ✓", s)

print("第一次執行："); run(crash_at="分析")
print("重啟後："); run()
