# -*- coding: utf-8 -*-
"""第 14 課：先想再答。回應裡多了一種 thinking 區塊；代理在每次呼叫工具之前也可以先想。
這個假模型示範：不想 → 直覺答錯；先想 → 拆步驟答對。"""
from mockllm import MockClient, text, thinking

Q = "球棒和球共 110 元，球棒比球貴 100 元，球多少錢？"

def policy(ctx):
    if ctx.extra.get("thinking"):
        return [thinking("設球 x 元，球棒 x+100。x + (x+100) = 110 → 2x = 10 → x = 5。驗算：5 + 105 = 110 ✓"),
                text("球 5 元。")]
    return text("球 10 元。")                      # 直覺答案（錯）

client = MockClient(policy)
for think in (False, True):
    kw = {"thinking": {"type": "adaptive"}} if think else {}
    r = client.messages.create(model="mock", max_tokens=2000, messages=[{"role": "user", "content": Q}], **kw)
    print("思考%s：" % ("開" if think else "關"))
    for b in r.content:
        print("   [%s] %s" % (b.type, b.thinking if b.type == "thinking" else b.text))
    print("   output tokens = %d（思考也要算錢）" % r.usage.output_tokens)
