# -*- coding: utf-8 -*-
"""第 46 課：該用哪一種架構？從最簡單的開始，只有在必要時才升級。"""

def recommend(steps_known, needs_tools, open_ended, parallel, high_stakes):
    if not needs_tools and steps_known:
        arch = "單次 LLM 呼叫（分類、摘要、擷取）"
    elif steps_known:
        arch = "工作流：程式決定步驟（串接、路由、平行）"
    elif open_ended and parallel:
        arch = "多代理：協調者＋工作者"
    else:
        arch = "單一代理：模型在迴圈中自己選工具"
    if high_stakes:
        arch += "；危險動作加上人工核准與沙箱"
    return arch

CASES = [("把客服信分成 5 類", dict(steps_known=True, needs_tools=False, open_ended=False, parallel=False, high_stakes=False)),
         ("每天抓匯率→算報表→寄信", dict(steps_known=True, needs_tools=True, open_ended=False, parallel=False, high_stakes=False)),
         ("修好這個 repo 裡失敗的測試", dict(steps_known=False, needs_tools=True, open_ended=True, parallel=False, high_stakes=True)),
         ("調查 20 家競爭對手寫報告", dict(steps_known=False, needs_tools=True, open_ended=True, parallel=True, high_stakes=False))]
for task, f in CASES:
    print("%-18s → %s" % (task, recommend(**f)))
print("\n四個問題：任務夠複雜嗎？價值夠高嗎？模型做得到嗎？出錯能被發現並補救嗎？——有一個答案是否，就退回更簡單的做法。")
