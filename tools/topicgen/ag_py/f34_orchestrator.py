# -*- coding: utf-8 -*-
"""第 34 課：協調者－工作者（orchestrator-workers）。
協調者把任務拆成子任務 → 工作者平行執行 → 協調者整合。"""
import json
import time
from concurrent.futures import ThreadPoolExecutor
from mockllm import MockClient, text

orchestrator = MockClient(lambda ctx: text(json.dumps(
    ["調查日本市場的電動機車法規", "調查日本主要競爭品牌", "估算日本市場規模"], ensure_ascii=False))
    if ctx.turn == 0 and "拆解" in ctx.system else text("整合報告：\n" + ctx.user_text()))

# 工作者的「研究結果」（虛構的示範資料）
FINDINGS = {"法規": "需取得型式認證；不同車種的駕照規定不同。", "品牌": "本土品牌占多數市占。", "規模": "需依官方統計估算年銷量。"}

def worker(subtask):
    time.sleep(0.3)                                          # 模擬每個工作者要花時間
    w = MockClient(lambda ctx: text(next(v for k, v in FINDINGS.items() if k in ctx.user_text())))
    r = w.messages.create(model="mock", max_tokens=500, system="你是研究員，只負責一個子任務",
                          messages=[{"role": "user", "content": subtask}])
    return "【%s】%s" % (subtask, r.content[0].text)

goal = "我們要不要進軍日本電動機車市場？"
subtasks = json.loads(orchestrator.messages.create(model="mock", max_tokens=500, system="把目標拆解成可平行的子任務，輸出 JSON 陣列",
                                                   messages=[{"role": "user", "content": goal}]).content[0].text)
print("協調者拆出 %d 個子任務" % len(subtasks))
t0 = time.time()
with ThreadPoolExecutor(max_workers=len(subtasks)) as pool:
    results = list(pool.map(worker, subtasks))
print("工作者平行完成，耗時 %.1f 秒（依序做要 %.1f 秒）" % (time.time() - t0, 0.3 * len(subtasks)))
final = MockClient(lambda ctx: text("整合報告：\n" + ctx.user_text())).messages.create(
    model="mock", max_tokens=1000, messages=[{"role": "user", "content": "\n".join(results)}])
print(final.content[0].text)
