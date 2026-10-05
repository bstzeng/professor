# -*- coding: utf-8 -*-
"""第 30 課（Claude API 版）：MCP 連接器（beta）——直接把遠端 MCP 伺服器交給 Claude，
API 會自己做 tools/list 與 tools/call。兩半都要給：mcp_servers 與對應名稱的 mcp_toolset。
（本機的 stdio MCP 伺服器則可用 SDK 的 anthropic.lib.tools.mcp 輔助函式轉成工具，交給 tool_runner。）"""
import anthropic

client = anthropic.Anthropic()
r = client.beta.messages.create(
    model="claude-opus-5-5",
    max_tokens=16000,
    betas=["mcp-client-2025-11-20"],
    mcp_servers=[{"type": "url", "url": "https://example.com/mcp", "name": "notes"}],   # 換成你的 MCP 伺服器
    tools=[{"type": "mcp_toolset", "mcp_server_name": "notes"}],
    messages=[{"role": "user", "content": "我的會議筆記寫了什麼？"}],
)
for b in r.content:
    print(b.type, getattr(b, "text", "") or getattr(b, "input", ""))
