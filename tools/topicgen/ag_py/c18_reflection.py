# -*- coding: utf-8 -*-
"""第 18 課：反思與自我修正——產生 → 檢查 → 修改。
最可靠的「檢查」是外部回饋（測試、編譯器），其次才是讓模型自己評論。"""
from mockllm import MockClient, text

def writer_policy(ctx):
    fb = ctx.user_text()
    if "失敗" in fb:
        return text("def is_leap(y):\n    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)")
    return text("def is_leap(y):\n    return y % 4 == 0")                 # 第一版：漏掉世紀年規則

def run_tests(code):
    ns = {}
    exec(code, ns)                                                          # 教學示範；真實系統要在沙箱中執行
    cases = {2024: True, 2023: False, 1900: False, 2000: True}
    bad = ["is_leap(%d) 應為 %s" % (y, e) for y, e in cases.items() if ns["is_leap"](y) != e]
    return bad

writer = MockClient(writer_policy)
msgs = [{"role": "user", "content": "寫一個判斷閏年的 Python 函式 is_leap(y)"}]
for attempt in range(1, 4):
    code = writer.messages.create(model="mock", max_tokens=500, messages=msgs).content[0].text
    bad = run_tests(code)
    print("第 %d 版：%s" % (attempt, "全部通過 ✓" if not bad else "失敗 ✗ " + "；".join(bad)))
    if not bad:
        print(code)
        break
    msgs += [{"role": "assistant", "content": code},
             {"role": "user", "content": "測試失敗：%s。請修正。" % "；".join(bad)}]       # 把回饋接回對話
