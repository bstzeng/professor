# -*- coding: utf-8 -*-
"""第 44 課：可觀測性——把代理的每一步（模型呼叫、工具、耗時、token）記成「追蹤（trace）」，
出事時才查得出：它看到什麼、為什麼這樣做、卡在哪一步。"""
import functools
import json
import time
import itertools
from mockllm import MockClient, text, tool_use

TRACE = []
_stack = []
_ids = itertools.count(1)

def span(kind):
    """裝飾器：記錄一個步驟的開始、結束、耗時、輸入摘要、父子關係。"""
    def deco(fn):
        @functools.wraps(fn)
        def wrap(*a, **kw):
            sid = "s%d" % next(_ids)
            rec = {"id": sid, "parent": _stack[-1] if _stack else None, "kind": kind, "name": fn.__name__,
                   "input": str(kw or a)[:60]}
            _stack.append(sid)
            t0 = time.perf_counter()
            try:
                out = fn(*a, **kw)
                rec["status"] = "ok"
                return out
            except Exception as e:
                rec["status"] = "error: %s" % e
                raise
            finally:
                rec["ms"] = round((time.perf_counter() - t0) * 1000, 1)
                _stack.pop()
                TRACE.append(rec)
        return wrap
    return deco

@span("tool")
def search(q):
    time.sleep(0.05)
    return ["結果 1", "結果 2"]

@span("tool")
def fetch(url):
    time.sleep(0.12)
    raise TimeoutError("連線逾時")

client = MockClient(lambda ctx: [tool_use("search", {"q": "agent"}), tool_use("fetch", {"url": "https://x.example"})]
                    if ctx.turn == 0 else text("搜尋成功，但讀取網頁逾時。"))

@span("llm")
def call_llm(msgs):
    r = client.messages.create(model="mock", max_tokens=500, messages=msgs,
                               tools=[{"name": n, "input_schema": {"type": "object"}} for n in ("search", "fetch")])
    TRACE.append({"kind": "usage", "in": r.usage.input_tokens, "out": r.usage.output_tokens})
    return r

@span("agent")
def run(task):
    msgs = [{"role": "user", "content": task}]
    while True:
        r = call_llm(msgs)
        msgs.append({"role": "assistant", "content": r.content})
        if r.stop_reason != "tool_use":
            return r.content[0].text
        res = []
        for b in r.content:
            if b.type == "tool_use":
                try:
                    res.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(globals()[b.name](**b.input), ensure_ascii=False)})
                except Exception as e:
                    res.append({"type": "tool_result", "tool_use_id": b.id, "content": str(e), "is_error": True})
        msgs.append({"role": "user", "content": res})

run(task="研究 agent")
print("追蹤紀錄（可存成 JSON Lines，送進 OpenTelemetry 等工具）：")
for r in TRACE:
    if r["kind"] == "usage":
        print("   · tokens in=%d out=%d" % (r["in"], r["out"]))
    else:
        print("   %-6s %-9s %6.1f ms  parent=%-6s %s" % (r["kind"], r["name"], r["ms"], r["parent"], r["status"]))
