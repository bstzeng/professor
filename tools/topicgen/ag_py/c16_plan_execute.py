# -*- coding: utf-8 -*-
"""第 16 課：先規劃、再執行（Plan-and-Execute）。
規劃者一次產生完整計畫（結構化 JSON），執行者逐步完成；某步失敗時才請規劃者「重新規劃」。"""
import json
from mockllm import MockClient, text

def planner_policy(ctx):
    if "失敗" in ctx.user_text():
        return text(json.dumps(["用備用來源 B 下載資料", "清理資料", "產生圖表", "寫摘要"], ensure_ascii=False))
    return text(json.dumps(["從來源 A 下載資料", "清理資料", "產生圖表", "寫摘要"], ensure_ascii=False))

planner = MockClient(planner_policy)

def execute(step):
    if "來源 A" in step:
        raise ConnectionError("來源 A 連不上")
    return "完成：" + step

def plan(goal, feedback=""):
    r = planner.messages.create(model="mock", max_tokens=500, system="把目標拆成步驟，只輸出 JSON 陣列",
                                messages=[{"role": "user", "content": goal + feedback}])
    return json.loads(r.content[0].text)

goal = "做一份上個月營收的分析報告"
steps, done = plan(goal), []
print("初始計畫：", steps)
i = 0
while i < len(steps):
    try:
        done.append(execute(steps[i]))
        print("  ✓", done[-1])
        i += 1
    except Exception as e:
        print("  ✗ %s → %s，請規劃者重新規劃" % (steps[i], e))
        steps = plan(goal, "\n已完成：%s\n失敗：%s（%s）" % (done, steps[i], e))
        print("新計畫：", steps)
        i = 0
        done = []
print("共呼叫規劃者 %d 次。優點：省 token、步驟清楚；缺點：計畫趕不上變化時要重規劃。" % planner.calls)
