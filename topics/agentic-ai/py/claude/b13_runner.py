# -*- coding: utf-8 -*-
"""第 13 課（Claude API 版）：SDK 內建的 Tool Runner（beta）。你只寫工具，迴圈交給 SDK。"""
import anthropic
from anthropic import beta_tool

client = anthropic.Anthropic()


@beta_tool
def add(a: float, b: float) -> str:
    """兩數相加。

    Args:
        a: 第一個數
        b: 第二個數
    """
    return str(a + b)


@beta_tool
def multiply(a: float, b: float) -> str:
    """兩數相乘。

    Args:
        a: 第一個數
        b: 第二個數
    """
    return str(a * b)


runner = client.beta.messages.tool_runner(
    model="claude-opus-5-5",
    max_tokens=16000,
    tools=[add, multiply],
    messages=[{"role": "user", "content": "(17+25)×3 是多少？請用工具計算。"}],
)
for message in runner:                     # 每一輪都會 yield 一則 Claude 的回應
    for b in message.content:
        if b.type == "tool_use":
            print("工具：", b.name, b.input)
        elif b.type == "text":
            print("Claude：", b.text)
