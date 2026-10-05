# -*- coding: utf-8 -*-
"""第 21 課：對話太長怎麼辦？三種策略比較——
① 滑動視窗：只留最近 N 則  ② 摘要：把舊的濃縮成一段  ③ 清除舊工具結果：保留骨架、丟掉大段輸出"""
from mockllm import MockClient, text, count_tokens

history = []
for i in range(1, 11):
    history += [{"role": "user", "content": "第 %d 個問題：請分析 log_%d" % (i, i)},
                {"role": "assistant", "content": "（分析了 log_%d 的 2000 行輸出……）" % i + "細節" * 300}]
print("原始：%d 則訊息，約 %d tokens" % (len(history), count_tokens(history)))

def sliding_window(h, keep=4):
    return h[-keep:]

summarizer = MockClient(lambda ctx: text("【先前摘要】使用者請我依序分析 log_1～log_8，已完成；重點：log_3 有逾時、log_7 有記憶體不足。"))

def summarize(h, keep=4):
    old, recent = h[:-keep], h[-keep:]
    s = summarizer.messages.create(model="mock", max_tokens=300, system="把對話濃縮成要點",
                                   messages=[{"role": "user", "content": str(old)}]).content[0].text
    return [{"role": "user", "content": s}, {"role": "assistant", "content": "了解，我記得先前的重點。"}] + recent

def clear_old_outputs(h, keep=4):
    out = []
    for i, m in enumerate(h):
        if i < len(h) - keep and m["role"] == "assistant":
            m = {"role": "assistant", "content": "[舊的工具輸出已清除]"}
        out.append(m)
    return out

for name, fn in [("滑動視窗", sliding_window), ("摘要", summarize), ("清除舊輸出", clear_old_outputs)]:
    h = fn(history)
    print("%-6s → %2d 則，約 %5d tokens｜開頭：%s" % (name, len(h), count_tokens(h), h[0]["content"][:30]))
print("\n取捨：滑動視窗最簡單但會『失憶』；摘要保留重點但可能漏細節；清除輸出保留脈絡但看不到原文。")
