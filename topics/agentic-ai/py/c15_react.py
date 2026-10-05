# -*- coding: utf-8 -*-
"""第 15 課：ReAct（Reason + Act）——在原生工具呼叫出現前，代理是靠「文字格式」運作的：
模型輸出 Thought / Action / Action Input，程式用正規表達式解析、執行，再把 Observation 接回去。"""
import re

KB = {"台灣最高的山": "玉山", "玉山高度": "3952 公尺", "富士山高度": "3776 公尺"}

def search(q):
    return KB.get(q, "查無資料")

# 假模型：根據目前的 scratchpad 產生下一段文字
def fake_llm(scratch):
    n = scratch.count("Observation:")
    return ["Thought: 先找出台灣最高的山。\nAction: search\nAction Input: 台灣最高的山",
            "Thought: 是玉山，再查它的高度。\nAction: search\nAction Input: 玉山高度",
            "Thought: 也要查富士山來比較。\nAction: search\nAction Input: 富士山高度",
            "Thought: 3952 − 3776 = 176。\nFinal Answer: 玉山（3952 公尺）比富士山高 176 公尺。"][n]

scratch = "Question: 台灣最高的山比富士山高多少？\n"
for step in range(6):
    out = fake_llm(scratch)
    scratch += out + "\n"
    print(out)
    if "Final Answer:" in out:
        break
    act = re.search(r"Action: (\w+)\nAction Input: (.+)", out)        # 解析文字 → 動作
    obs = {"search": search}[act.group(1)](act.group(2).strip())
    scratch += "Observation: %s\n" % obs
    print("Observation:", obs)
print("\n缺點：格式一錯就解析失敗。現代 API 改用結構化的 tool_use 區塊，但『想一步、做一步』的精神沒變。")
