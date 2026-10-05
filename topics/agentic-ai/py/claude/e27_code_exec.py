# -*- coding: utf-8 -*-
"""第 27 課（Claude API 版）：伺服器端程式執行工具——程式在 Anthropic 的沙箱容器裡跑，你不用自己架環境。"""
import anthropic

client = anthropic.Anthropic()
r = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    tools=[{"type": "code_execution_20260120", "name": "code_execution"}],
    messages=[{"role": "user", "content": "計算 12, 7, 3, 25, 8 的平均與樣本標準差，請實際執行程式。"}],
)
for b in r.content:
    if b.type == "text":
        print(b.text)
    elif b.type == "server_tool_use":
        print("[執行]", b.input)
    elif b.type == "bash_code_execution_tool_result":
        res = b.content
        if res.type == "bash_code_execution_result":
            print("[stdout]", res.stdout, "[return_code]", res.return_code)
