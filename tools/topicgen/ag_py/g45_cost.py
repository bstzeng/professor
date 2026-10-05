# -*- coding: utf-8 -*-
"""第 45 課：成本與延遲——代理的成本＝（每輪輸入＋輸出）× 輪數，而每輪輸入會隨歷史變長。
常見的省錢手段：提示快取、較低的 effort、精簡工具結果、小任務用小模型、批次處理。"""
PRICE = {"Opus 5.5": (4.0, 20.0), "Sonnet 5.5": (2.0, 10.0), "Haiku 4.5": (1.0, 5.0)}   # 美元／百萬 tokens

def run_cost(model, turns=20, base=12000, growth=2500, out=600, cache=False, trim=1.0):
    pin, pout = PRICE[model]
    total = 0.0
    for t in range(turns):
        ctx = base + growth * trim * t
        if cache and t > 0:          # 舊內容讀快取約 0.1 倍、新內容寫入快取約 1.25 倍（實際以官方價目表為準）
            cached = base + growth * trim * (t - 1)
            total += (cached * 0.1 + (ctx - cached) * 1.25) * pin / 1e6
        else:
            total += ctx * pin / 1e6
        total += out * pout / 1e6
    return total

base = run_cost("Opus 5.5")
rows = [("基準：Opus 5.5，20 輪", base),
        ("＋提示快取", run_cost("Opus 5.5", cache=True)),
        ("＋工具結果精簡一半", run_cost("Opus 5.5", cache=True, trim=0.5)),
        ("改用 Sonnet 5.5（＋快取＋精簡）", run_cost("Sonnet 5.5", cache=True, trim=0.5)),
        ("改用 Haiku 4.5（＋快取＋精簡）", run_cost("Haiku 4.5", cache=True, trim=0.5))]
for name, c in rows:
    print("%-30s $%6.3f  %s" % (name, c, "█" * int(40 * c / base)))
print("\n注意：便宜的模型如果要多跑好幾輪、或常常做錯要重來，『每完成一件任務的成本』不一定比較低。")
print("延遲：每輪 = 等待首字 + 輸出時間 + 工具時間；可平行的工具要平行跑，能用工作流就別用代理。")
