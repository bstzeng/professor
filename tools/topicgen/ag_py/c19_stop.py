# -*- coding: utf-8 -*-
"""第 19 課：何時停止？——代理一定要有「煞車」：步數上限、token 預算、重複偵測、時間限制。"""
import json
import time
from mockllm import MockClient, tool_use

class Budget(object):
    def __init__(self, max_steps=8, max_tokens=3000, max_seconds=5):
        self.max_steps, self.max_tokens, self.max_seconds = max_steps, max_tokens, max_seconds
        self.steps = self.tokens = 0
        self.t0 = time.time()
        self.seen = []

    def check(self, resp):
        self.steps += 1
        self.tokens += resp.usage.input_tokens + resp.usage.output_tokens
        calls = [json.dumps([b.name, b.input], sort_keys=True) for b in resp.content if b.type == "tool_use"]
        if calls and self.seen[-2:] == [calls, calls]:
            return "偵測到重複：同樣的呼叫連續出現 3 次"
        self.seen.append(calls)
        if self.steps >= self.max_steps:
            return "達到步數上限 %d" % self.max_steps
        if self.tokens >= self.max_tokens:
            return "超過 token 預算（已用 %d）" % self.tokens
        if time.time() - self.t0 > self.max_seconds:
            return "超過時間限制"
        return None

# 一個「卡住」的假模型：一直重複搜尋同樣的東西
stuck = MockClient(lambda ctx: tool_use("search", {"q": "不存在的資料"}))
tools = [{"name": "search", "description": "搜尋", "input_schema": {"type": "object", "properties": {"q": {"type": "string"}}}}]
msgs, b = [{"role": "user", "content": "找出不存在的資料"}], Budget()
while True:
    r = stuck.messages.create(model="mock", max_tokens=500, tools=tools, messages=msgs)
    reason = b.check(r)
    print("第 %d 步，累計 %d tokens" % (b.steps, b.tokens))
    if reason:
        print("🛑 停止：" + reason)
        break
    msgs += [{"role": "assistant", "content": r.content},
             {"role": "user", "content": [{"type": "tool_result", "tool_use_id": r.content[0].id, "content": "查無結果"}]}]
print("注意：每一步的 input tokens 會越來越多——因為整段歷史每次都重送。")
