# -*- coding: utf-8 -*-
"""第 24 課（Claude API 版）：Anthropic 定義的記憶工具（memory_20250818）。
Claude 會發出 view / create / str_replace 等指令，由你的程式在 /memories 目錄中實作。
SDK 提供 BetaAbstractMemoryTool：繼承並實作各指令即可交給 tool_runner。"""
import anthropic
from anthropic.lib.tools import BetaAbstractMemoryTool

client = anthropic.Anthropic()
STORE = {}   # 示範用：存在記憶體；實務請存檔案或資料庫，並防止路徑穿越（../）


class DictMemory(BetaAbstractMemoryTool):
    def view(self, command):
        if command.path.rstrip("/") == "/memories":          # 看目錄：列出所有檔案
            return "\n".join(STORE) or "（目前沒有記憶）"
        return STORE.get(command.path, "找不到檔案")

    def create(self, command):
        STORE[command.path] = command.file_text
        return "已建立 %s" % command.path

    def str_replace(self, command):
        STORE[command.path] = STORE[command.path].replace(command.old_str, command.new_str)
        return "已更新"

    def insert(self, command):
        lines = STORE[command.path].split("\n")
        lines.insert(command.insert_line, command.insert_text)
        STORE[command.path] = "\n".join(lines)
        return "已插入"

    def delete(self, command):
        STORE.pop(command.path, None)
        return "已刪除"

    def rename(self, command):
        STORE[command.new_path] = STORE.pop(command.old_path)
        return "已改名"


memory = DictMemory()
for msg in ["我吃素，而且對花生過敏，請記住。", "晚餐推薦什麼？"]:   # 兩次獨立的對話
    runner = client.beta.messages.tool_runner(model="claude-opus-5-5", max_tokens=16000, tools=[memory],
                                              messages=[{"role": "user", "content": msg}])
    for m in runner:
        for b in m.content:
            if b.type == "text":
                print(b.text)
print(STORE)
