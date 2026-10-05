# -*- coding: utf-8 -*-
"""第 30 課：MCP（Model Context Protocol）——工具的「USB 介面標準」。
工具提供者寫一個 MCP 伺服器；任何支援 MCP 的代理（客戶端）都能用同一套協定發現並呼叫它。
MCP 底層是 JSON-RPC 2.0。這裡在同一個行程裡做一個迷你伺服器與客戶端，看清楚往返的訊息。"""
import json

# ───── 伺服器端（工具提供者）─────
NOTES = {"購物": "牛奶、雞蛋", "會議": "週五 10 點"}
SERVER_TOOLS = [{"name": "get_note", "description": "依標題讀取筆記",
                 "inputSchema": {"type": "object", "properties": {"title": {"type": "string"}}, "required": ["title"]}}]

def server_handle(raw):
    req = json.loads(raw)
    m, rid = req["method"], req.get("id")
    if m == "initialize":
        res = {"protocolVersion": "2025-06-18", "capabilities": {"tools": {}}, "serverInfo": {"name": "notes-server", "version": "1.0"}}
    elif m == "tools/list":
        res = {"tools": SERVER_TOOLS}
    elif m == "tools/call":
        title = req["params"]["arguments"]["title"]
        res = {"content": [{"type": "text", "text": NOTES.get(title, "沒有這則筆記")}], "isError": title not in NOTES}
    else:
        return json.dumps({"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "Method not found"}})
    return json.dumps({"jsonrpc": "2.0", "id": rid, "result": res}, ensure_ascii=False)

# ───── 客戶端（代理這一側）─────
class MCPClient(object):
    def __init__(self, transport):
        self.send, self.n = transport, 0

    def request(self, method, params=None):
        self.n += 1
        raw = json.dumps({"jsonrpc": "2.0", "id": self.n, "method": method, "params": params or {}}, ensure_ascii=False)
        print("→", raw)
        resp = self.send(raw)
        print("←", resp)
        return json.loads(resp)["result"]

c = MCPClient(server_handle)          # 真實情況的傳輸層是 stdio（本機子行程）或 HTTP
c.request("initialize", {"protocolVersion": "2025-06-18", "capabilities": {}, "clientInfo": {"name": "my-agent", "version": "0.1"}})
# （完整流程中，客戶端接著會送一個 notifications/initialized 通知，這裡省略）
tools = c.request("tools/list")["tools"]

# 把 MCP 工具轉成 LLM API 的工具格式：只差在 inputSchema → input_schema
api_tools = [{"name": t["name"], "description": t["description"], "input_schema": t["inputSchema"]} for t in tools]
print("\n轉成 API 工具：", json.dumps(api_tools, ensure_ascii=False))

# 當模型要求 get_note({"title": "會議"}) 時，代理轉送給 MCP 伺服器：
out = c.request("tools/call", {"name": "get_note", "arguments": {"title": "會議"}})
print("\n要放進 tool_result 的內容：", out["content"][0]["text"])
