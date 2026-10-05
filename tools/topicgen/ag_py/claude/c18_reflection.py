# -*- coding: utf-8 -*-
"""第 18 課（Claude API 版）：產生程式 → 跑測試 → 把失敗訊息回饋給 Claude → 修正。"""
import re
import anthropic

client = anthropic.Anthropic()
CASES = {2024: True, 2023: False, 1900: False, 2000: True}


def run_tests(code):
    ns = {}
    exec(code, ns)   # 教學示範；正式環境請在沙箱（容器、子行程）中執行模型產生的程式碼
    return ["is_leap(%d) 應為 %s" % (y, e) for y, e in CASES.items() if ns["is_leap"](y) != e]


messages = [{"role": "user", "content": "寫一個判斷閏年的 Python 函式 is_leap(y)。只輸出一個 ```python 程式碼區塊。"}]
for attempt in range(1, 4):
    r = client.messages.create(model="claude-opus-5-5", max_tokens=16000, messages=messages)
    reply = next(b.text for b in r.content if b.type == "text")
    code = re.search(r"```python\n(.*?)```", reply, re.S).group(1)
    bad = run_tests(code)
    print("第 %d 版：%s" % (attempt, "通過" if not bad else bad))
    if not bad:
        print(code)
        break
    messages += [{"role": "assistant", "content": r.content},
                 {"role": "user", "content": "測試失敗：%s。請修正。" % "；".join(bad)}]
