# -*- coding: utf-8 -*-
"""第 19 課（Claude API 版）：自己的煞車（步數、token）＋ API 的 task_budget（beta）。
task_budget 讓 Claude「知道」還剩多少預算，會自己調整節奏、優雅收尾；max_tokens 則是單次回應的硬上限。"""
import anthropic

client = anthropic.Anthropic()
MAX_STEPS, MAX_TOTAL_TOKENS = 20, 200_000
used = 0
messages = [{"role": "user", "content": "用三句話說明代理為什麼需要停止條件。"}]

for step in range(MAX_STEPS):
    with client.beta.messages.stream(
        model="claude-opus-5-5",
        max_tokens=64000,
        output_config={"effort": "high", "task_budget": {"type": "tokens", "total": 64000}},
        betas=["task-budgets-2026-03-13"],
        messages=messages,
    ) as stream:
        r = stream.get_final_message()
    used += r.usage.input_tokens + r.usage.output_tokens
    messages.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use" or used > MAX_TOTAL_TOKENS:   # 這個例子沒有工具，一輪就結束
        break
print(next(b.text for b in r.content if b.type == "text"))
print("累計 tokens：", used)
