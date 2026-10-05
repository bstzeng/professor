# -*- coding: utf-8 -*-
"""第 3 課（Claude API 版）：system + 多輪 messages。API 無狀態，每次送完整歷史。"""
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"
system = "用繁體中文、一句話回答。"
history = []


def send(msg):
    history.append({"role": "user", "content": msg})
    r = client.messages.create(model=MODEL, max_tokens=16000, system=system, messages=history)
    history.append({"role": "assistant", "content": r.content})
    reply = next(b.text for b in r.content if b.type == "text")
    print("使用者：%s\n Claude：%s  (input=%d, output=%d tokens)" % (msg, reply, r.usage.input_tokens, r.usage.output_tokens))


send("嗨，我叫小安。")
send("我的名字是什麼？")
