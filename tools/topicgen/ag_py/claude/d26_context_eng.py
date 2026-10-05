# -*- coding: utf-8 -*-
"""第 26 課（Claude API 版）：context editing（beta）——自動清除較舊的工具結果，讓長時間執行的代理保持精簡。
與 compaction（摘要）不同：它是直接剪掉，不是濃縮。"""
import anthropic

client = anthropic.Anthropic()
tools = [{"name": "read_file", "description": "讀取檔案；可指定行號範圍以免結果過長",
          "input_schema": {"type": "object", "properties": {"path": {"type": "string"},
                                                            "start": {"type": "integer"}, "end": {"type": "integer"}},
                           "required": ["path"]}}]
r = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    betas=["context-management-2025-06-27"],
    context_management={"edits": [{"type": "clear_tool_uses_20250919"}]},
    system="專案檔案索引：\nsrc/auth.py（600 行）\nsrc/db.py（1000 行）\n需要時用 read_file 讀取，只讀需要的範圍。",
    tools=tools,
    messages=[{"role": "user", "content": "登入失敗的錯誤可能在哪裡？"}],
)
for b in r.content:
    print(b.type, getattr(b, "input", "") or getattr(b, "text", ""))
