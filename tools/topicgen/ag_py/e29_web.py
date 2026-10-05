# -*- coding: utf-8 -*-
"""第 29 課：上網搜尋與擷取——search 回傳標題與網址（短），fetch 才讀全文（長）。
代理的好習慣：先搜尋、挑最相關的再讀，而不是把每一頁都讀進來。這裡用本地的「假網路」示範（晴川市是虛構城市）。"""
import json
from mockllm import MockClient, text, tool_use

WEB = {"https://ex.com/a": ("晴川市 2026 年再生能源占比", "（虛構資料）晴川市 2026 年上半年再生能源發電占比約 15%……" * 5),
       "https://ex.com/b": ("太陽能板清潔小技巧", "用清水與軟刷……" * 5),
       "https://ex.com/c": ("離岸風電進度報告", "第三階段區塊開發……占比預計持續上升……" * 5)}

def web_search(query):
    words = [w for w in query.split() if w]
    hits = [{"url": u, "title": t} for u, (t, _) in WEB.items() if any(w in t for w in words)]
    return hits[:5]

def web_fetch(url):
    if url not in WEB:
        raise ValueError("只能讀取搜尋結果中出現過的網址")         # 降低被誘導去奇怪網址的風險
    return WEB[url][1][:300]

def policy(ctx):
    if ctx.turn == 0:
        return tool_use("web_search", {"query": "再生能源 占比"})
    if ctx.turn == 1:
        best = ctx.data()[0]["url"]
        return [text("第一筆最相關，讀全文。"), tool_use("web_fetch", {"url": best})]
    return text("根據搜尋到的資料，晴川市 2026 年上半年再生能源發電占比約 15%。（來源：https://ex.com/a）")

IMPL = {"web_search": web_search, "web_fetch": web_fetch}
tools = [{"name": "web_search", "description": "搜尋網路，回傳標題與網址", "input_schema": {"type": "object", "properties": {"query": {"type": "string"}}}},
         {"name": "web_fetch", "description": "讀取網頁全文", "input_schema": {"type": "object", "properties": {"url": {"type": "string"}}}}]
client, msgs = MockClient(policy), [{"role": "user", "content": "晴川市的再生能源現在占多少？"}]
while True:
    r = client.messages.create(model="mock", max_tokens=800, tools=tools, messages=msgs)
    msgs.append({"role": "assistant", "content": r.content})
    if r.stop_reason != "tool_use":
        break
    b = next(x for x in r.content if x.type == "tool_use")
    out = IMPL[b.name](**b.input)
    print("[%s] %s → %s" % (b.name, b.input, json.dumps(out, ensure_ascii=False)[:80] + "…"))
    msgs.append({"role": "user", "content": [{"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(out, ensure_ascii=False)}]})
print(r.content[-1].text)
