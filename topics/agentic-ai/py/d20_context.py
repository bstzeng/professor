# -*- coding: utf-8 -*-
"""第 20 課：上下文視窗＝代理的工作記憶。每次呼叫送進去的東西都佔空間：
system + 工具定義 + 整段對話歷史（含每一次工具結果）。"""
from mockllm import count_tokens

WINDOW = 200_000                                 # 假設的上下文視窗大小（tokens）
system = "你是程式助理。" * 50
tools = [{"name": "read_file", "description": "讀檔" * 30, "input_schema": {"type": "object"}}] * 8
file_content = "def f(x):\n    return x * 2\n" * 1500  # 一個約 1 萬 token 的檔案

history = [{"role": "user", "content": "幫我重構這個專案"}]
print("%-6s %-10s %-10s %s" % ("回合", "本輪新增", "累計", "佔視窗"))
for turn in range(1, 16):
    history.append({"role": "assistant", "content": "讀取 file_%d.py" % turn})
    history.append({"role": "user", "content": file_content})           # 每讀一個檔，結果就留在歷史裡
    total = count_tokens(system) + count_tokens(tools) + count_tokens(history)
    if turn in (1, 2, 5, 10, 15):
        print("%-8d %-12d %-12d %5.1f%% %s" % (turn, count_tokens(file_content), total, 100.0 * total / WINDOW,
                                               "█" * int(30 * total / WINDOW)))
print("\n讀 15 個檔案就吃掉大半視窗。後果：成本上升、速度變慢，而且內容越多，模型越容易忽略重點（context rot）。")
