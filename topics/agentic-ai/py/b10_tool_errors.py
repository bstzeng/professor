# -*- coding: utf-8 -*-
"""第 10 課：工具出錯怎麼辦？——不要讓程式當掉，把錯誤「告訴模型」(is_error=True)，讓它自己修正。"""
import json
from mockllm import MockClient, text, tool_use

STOCK = {"apple": 12, "banana": 0}

def check_stock(item):
    if item not in STOCK:
        raise ValueError("找不到商品 '%s'。可用商品：%s" % (item, ", ".join(STOCK)))
    return STOCK[item]

def policy(ctx):
    res = ctx.results()
    if ctx.turn == 0:
        return tool_use("check_stock", {"item": "蘋果"})              # 第一次：用了中文名稱（錯）
    name, out, err = res[0]
    if err:                                                          # 看到錯誤訊息 → 自我修正
        return [text("名稱要用英文，我改用 apple 再查一次。"), tool_use("check_stock", {"item": "apple"})]
    return text("蘋果還有 %s 個。" % out)

def execute(b):
    """把例外轉成 tool_result，而不是讓整個代理崩潰。"""
    try:
        return {"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(check_stock(**b.input))}
    except Exception as e:
        return {"type": "tool_result", "tool_use_id": b.id, "content": "錯誤：%s" % e, "is_error": True}

tools = [{"name": "check_stock", "description": "查商品庫存（商品名稱用英文小寫）",
          "input_schema": {"type": "object", "properties": {"item": {"type": "string"}}, "required": ["item"]}}]
client, messages = MockClient(policy), [{"role": "user", "content": "蘋果還有貨嗎？"}]
while True:
    r = client.messages.create(model="mock", max_tokens=500, tools=tools, messages=messages)
    messages.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    results = [execute(b) for b in r.content if b.type == "tool_use"]
    for x in results:
        print("  tool_result%s：%s" % ("（is_error）" if x.get("is_error") else "", x["content"]))
    messages.append({"role": "user", "content": results})
print(r.content[-1].text)
