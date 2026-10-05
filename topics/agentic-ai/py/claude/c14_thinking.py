# -*- coding: utf-8 -*-
"""第 14 課（Claude API 版）：adaptive thinking 與 effort。
Claude Opus 5.5 的思考一律開啟（由模型自行決定想多少），用 output_config.effort 控制深度；
display="summarized" 會回傳可讀的思考摘要（預設是 omitted，thinking 文字為空）。"""
import anthropic

client = anthropic.Anthropic()
Q = "球棒和球共 110 元，球棒比球貴 100 元，球多少錢？"

for effort in ("low", "high"):
    r = client.messages.create(
        model="claude-opus-5-5",
        max_tokens=16000,
        thinking={"type": "adaptive", "display": "summarized"},
        output_config={"effort": effort},
        messages=[{"role": "user", "content": Q}],
    )
    print("== effort=%s  output_tokens=%d" % (effort, r.usage.output_tokens))
    for b in r.content:
        if b.type == "thinking":
            print("[思考摘要]", b.thinking[:200])
        elif b.type == "text":
            print("[回答]", b.text)
