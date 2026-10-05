# -*- coding: utf-8 -*-
"""mockllm.py — 離線用的「假 LLM」，介面刻意模仿 Anthropic Python SDK。

真正的 LLM 是一個機率模型；這裡用「規則／劇本」代替，讓你不用 API 金鑰、
不用網路，就能把代理（agent）的每一個動作跑一遍、看清楚資料怎麼流動。

用法和真的 SDK 幾乎一樣：
    client = MockClient(policy)            # 真的：client = anthropic.Anthropic()
    resp = client.messages.create(model=..., max_tokens=..., messages=..., tools=...)
    resp.content      -> [TextBlock / ToolUseBlock / ThinkingBlock ...]
    resp.stop_reason  -> "end_turn" 或 "tool_use"
    resp.usage        -> input_tokens / output_tokens
policy 是一個函式：policy(ctx) -> 區塊清單；ctx 讓你讀到對話、工具與工具結果。
"""
import json
import itertools

_ids = itertools.count(1)


class Block(object):
    """模仿 SDK 的內容區塊：用屬性存取（b.type、b.text、b.name、b.input、b.id）。"""
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        d = dict(self.__dict__)
        return "%s(%s)" % (d.pop("type"), ", ".join("%s=%r" % kv for kv in d.items()))

    def to_dict(self):
        return dict(self.__dict__)


def text(s):
    return Block(type="text", text=s)


def thinking(s):
    return Block(type="thinking", thinking=s)


def tool_use(name, input, id=None):
    return Block(type="tool_use", id=id or "toolu_%02d" % next(_ids), name=name, input=input)


def get(b, key, default=None):
    """同時支援 Block 物件與 dict（使用者端訊息通常是 dict）。"""
    if isinstance(b, dict):
        return b.get(key, default)
    return getattr(b, key, default)


def count_tokens(obj):
    """粗估 token 數：英文約 4 字元一個 token，中日韓字約 1 字一個 token。"""
    s = obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False, default=lambda o: get(o, "__dict__", str(o)))
    cjk = sum(1 for ch in s if ord(ch) > 0x2E80)
    return max(1, cjk + (len(s) - cjk) // 4)


class Usage(object):
    def __init__(self, i, o, cr=0, cw=0):
        self.input_tokens, self.output_tokens = i, o
        self.cache_read_input_tokens, self.cache_creation_input_tokens = cr, cw

    def __repr__(self):
        return "Usage(input=%d, output=%d, cache_read=%d)" % (self.input_tokens, self.output_tokens, self.cache_read_input_tokens)


class Message(object):
    def __init__(self, content, stop_reason, usage, model):
        self.role, self.type = "assistant", "message"
        self.content, self.stop_reason, self.usage, self.model = content, stop_reason, usage, model


class Ctx(object):
    """policy 看得到的東西：和真的模型一樣，只有『這次請求送進來的內容』。"""
    def __init__(self, messages, tools, system, extra):
        self.messages, self.tools, self.system, self.extra = messages, tools or [], system or "", extra

    @property
    def turn(self):
        """目前是第幾次回應（從 0 起算）＝已經有幾則 assistant 訊息。"""
        return sum(1 for m in self.messages if get(m, "role") == "assistant")

    def blocks(self, m):
        c = get(m, "content")
        return [text(c)] if isinstance(c, str) else list(c or [])

    def user_text(self, first=False):
        """最近（或第一則）使用者文字。"""
        seq = self.messages if first else reversed(self.messages)
        for m in seq:
            if get(m, "role") == "user":
                for b in self.blocks(m):
                    if get(b, "type") == "text":
                        return get(b, "text")
        return ""

    def results(self):
        """上一則 user 訊息裡的工具結果：[(工具名稱, 結果內容, 是否錯誤)]。"""
        names = {}
        for m in self.messages:
            if get(m, "role") == "assistant":
                for b in self.blocks(m):
                    if get(b, "type") == "tool_use":
                        names[get(b, "id")] = get(b, "name")
        last = self.messages[-1] if self.messages else None
        out = []
        if last is not None and get(last, "role") == "user":
            for b in self.blocks(last):
                if get(b, "type") == "tool_result":
                    out.append((names.get(get(b, "tool_use_id"), "?"), get(b, "content"), bool(get(b, "is_error", False))))
        return out

    def all_results(self):
        """整段對話中所有工具結果（依時間順序）。"""
        names, out = {}, []
        for m in self.messages:
            for b in self.blocks(m):
                t = get(b, "type")
                if t == "tool_use":
                    names[get(b, "id")] = get(b, "name")
                elif t == "tool_result":
                    out.append((names.get(get(b, "tool_use_id"), "?"), get(b, "content"), bool(get(b, "is_error", False))))
        return out

    def data(self, i=0):
        """把上一輪第 i 個工具結果當 JSON 解析（解析不了就原樣回傳）。"""
        c = self.results()[i][1]
        try:
            return json.loads(c)
        except (TypeError, ValueError):
            return c

    def tool_names(self):
        return [get(t, "name") for t in self.tools]


class _Messages(object):
    def __init__(self, client):
        self._c = client

    def create(self, model, max_tokens, messages, tools=None, system=None, **extra):
        if not messages or get(messages[0], "role") != "user":
            raise ValueError("第一則訊息必須是 user")
        for m in messages:                             # 和真的 API 一樣：工具結果要是字串（或內容區塊清單）
            for b in (get(m, "content") if isinstance(get(m, "content"), list) else []):
                if get(b, "type") == "tool_result" and not isinstance(get(b, "content"), (str, list)):
                    raise TypeError("tool_result 的 content 必須是字串，請先 json.dumps()")
        ctx = Ctx(messages, tools, system, extra)
        out = self._c.policy(ctx)
        if isinstance(out, str):
            out = [text(out)]
        elif isinstance(out, Block):
            out = [out]
        out = list(out)
        for b in out:                                  # 模型只能呼叫「有提供」的工具
            if b.type == "tool_use" and b.name not in ctx.tool_names():
                raise ValueError("模型呼叫了不存在的工具：%s" % b.name)
        stop = "tool_use" if any(b.type == "tool_use" for b in out) else "end_turn"
        prompt = {"system": system, "tools": tools, "messages": messages}
        i, o = count_tokens(prompt), count_tokens([b.to_dict() for b in out])
        if o > max_tokens:
            stop = "max_tokens"
        self._c.calls += 1
        self._c.total_in += i
        self._c.total_out += o
        return Message(out, stop, Usage(i, o), model)


class MockClient(object):
    def __init__(self, policy):
        self.policy = policy
        self.messages = _Messages(self)
        self.calls = self.total_in = self.total_out = 0


def script(*steps):
    """最簡單的 policy：第 n 次被呼叫就執行第 n 個步驟（步驟可以是函式或固定區塊）。"""
    def policy(ctx):
        st = steps[min(ctx.turn, len(steps) - 1)]
        return st(ctx) if callable(st) else st
    return policy


def show(resp):
    """把一次回應印得清楚一點。"""
    for b in resp.content:
        if b.type == "text":
            print("  [text] " + b.text)
        elif b.type == "thinking":
            print("  [thinking] " + b.thinking)
        elif b.type == "tool_use":
            print("  [tool_use] %s(%s)  id=%s" % (b.name, json.dumps(b.input, ensure_ascii=False), b.id))
    print("  stop_reason=%s  %r" % (resp.stop_reason, resp.usage))
