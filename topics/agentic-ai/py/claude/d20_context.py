# -*- coding: utf-8 -*-
"""第 20 課（Claude API 版）：用 count_tokens 在送出前精準計算 token 數（tokenizer 依模型而不同，不要用別家的工具估）。"""
import anthropic

client = anthropic.Anthropic()
MODEL = "claude-opus-5-5"
tools = [{"name": "read_file", "description": "讀取檔案內容",
          "input_schema": {"type": "object", "properties": {"path": {"type": "string"}}, "required": ["path"]}}]
messages = [{"role": "user", "content": "def f(x):\n    return x * 2\n" * 400}]

n = client.messages.count_tokens(model=MODEL, system="你是程式助理。", tools=tools, messages=messages)
info = client.models.retrieve(MODEL)
print("這次請求：%d tokens；模型上下文視窗：%s tokens" % (n.input_tokens, info.max_input_tokens))
