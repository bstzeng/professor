# -*- coding: utf-8 -*-
"""第 13 課：Tool Runner——把迴圈包起來，你只要寫工具函式。
這裡自己做一個迷你版 @tool 裝飾器與 run_tools()，理解 SDK 的 tool_runner 在做什麼。"""
import inspect
import json
from mockllm import MockClient, text, tool_use

REG = {}

def tool(fn):
    """裝飾器：自動從簽名產生 schema，並登記到 REG。"""
    props = {n: {"type": {int: "integer", float: "number"}.get(p.annotation, "string")}
             for n, p in inspect.signature(fn).parameters.items()}
    fn.schema = {"name": fn.__name__, "description": inspect.getdoc(fn),
                 "input_schema": {"type": "object", "properties": props, "required": list(props)}}
    REG[fn.__name__] = fn
    return fn

@tool
def add(a: float, b: float):
    """兩數相加"""
    return a + b

@tool
def multiply(a: float, b: float):
    """兩數相乘"""
    return a * b

def tool_runner(client, messages, tools, max_iterations=10):
    """產生器：每一輪 yield 一則模型訊息；工具自動執行並接回。"""
    for _ in range(max_iterations):
        r = client.messages.create(model="mock", max_tokens=1000, messages=messages, tools=[t.schema for t in tools])
        yield r
        messages.append({"role": "assistant", "content": r.content})
        calls = [b for b in r.content if b.type == "tool_use"]
        if not calls:
            return
        messages.append({"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(REG[b.name](**b.input))} for b in calls]})

def policy(ctx):
    if ctx.turn == 0:
        return tool_use("add", {"a": 17, "b": 25})
    if ctx.turn == 1:
        return tool_use("multiply", {"a": ctx.data(), "b": 3})
    return text("(17 + 25) × 3 = %s" % ctx.data())

for msg in tool_runner(MockClient(policy), [{"role": "user", "content": "(17+25)×3 = ?"}], [add, multiply]):
    print([("%s%s" % (b.name, b.input)) if b.type == "tool_use" else b.text for b in msg.content])
