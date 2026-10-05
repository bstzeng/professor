# -*- coding: utf-8 -*-
"""第 33 課：為什麼要多代理？最大的理由是「上下文隔離」。
主代理把『讀大量資料』的工作交給子代理；子代理在自己全新的上下文裡讀完，只回傳一段摘要。
主代理的上下文因此保持乾淨。"""
import json
from mockllm import MockClient, text, tool_use, count_tokens

DOCS = {"財報.txt": "營收…" * 3000, "競品分析.txt": "A 公司…" * 3000, "用戶訪談.txt": "受訪者說…" * 3000}
SUMMARY = {"財報.txt": "營收年增 12%，毛利率下滑 2 點。", "競品分析.txt": "A 公司降價 15%，搶走中階市場。",
           "用戶訪談.txt": "用戶最在意續航與價格。"}

def subagent(task, doc):
    """子代理：全新對話、只看到一份文件，回傳精簡摘要。"""
    sub = MockClient(lambda ctx: text(SUMMARY[doc]))
    r = sub.messages.create(model="mock", max_tokens=300, messages=[{"role": "user", "content": task + "\n\n" + DOCS[doc]}])
    return r.content[0].text, r.usage.input_tokens

# 方案 A：單一代理自己讀全部
single = [{"role": "user", "content": "分析市場"}] + [{"role": "user", "content": d} for d in DOCS.values()]
print("單一代理：主上下文 %d tokens" % count_tokens(single))

# 方案 B：主代理用 delegate 工具派工
main_ctx, sub_total = [{"role": "user", "content": "分析市場"}], 0
for doc in DOCS:
    summary, used = subagent("讀這份文件，用一句話摘要重點", doc)
    sub_total += used
    main_ctx.append({"role": "user", "content": "[%s] %s" % (doc, summary)})
    print("  子代理讀 %-8s（用了 %d tokens）→ %s" % (doc, used, summary))
print("多代理：主上下文只有 %d tokens（子代理合計 %d tokens，各自用完即丟）" % (count_tokens(main_ctx), sub_total))
print("代價：總 token 數沒有變少，甚至更多；換來的是主代理思路清楚、子代理可以平行。")
