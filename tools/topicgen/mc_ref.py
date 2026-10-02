# -*- coding: utf-8 -*-
"""蒙地卡羅方法：參考頁——互動實驗室、公式速查。"""
from mc_common import LS, MCLIB, mcw

LAB = {
    "file": "lab.html", "title": u"蒙地卡羅互動實驗室", "h1": u"蒙地卡羅互動實驗室", "icon": u"🧪",
    "description": u"蒲豐投針、丟點估 π、接受—拒絕、誤差收斂、準蒙地卡羅、梅特羅波利斯、模擬退火、柔和陰影算圖、選擇權、退休規劃",
    "body": [
        ("raw", u"<script>%s</script>" % MCLIB),
        ("p", u"所有模擬都在你的瀏覽器裡執行，每次結果略有不同。金融相關模擬僅供教育用途，不構成投資建議。"),
        ("h", u"1. 蒲豐投針（第 3 課）"), mcw({"t": "buffon"}),
        ("h", u"2. 丟點估計 π（第 4 課）"), mcw({"t": "pi"}),
        ("h", u"3. 接受—拒絕法（第 12 課）"), mcw({"t": "reject"}),
        ("h", u"4. 誤差收斂 1/√N（第 14 課）"), mcw({"t": "conv"}),
        ("h", u"5. 準蒙地卡羅（第 18 課）"), mcw({"t": "qmc"}),
        ("h", u"6. 梅特羅波利斯演算法（第 21 課）"), mcw({"t": "metro"}),
        ("h", u"7. 模擬退火（第 28 課）"), mcw({"t": "anneal"}),
        ("h", u"8. 柔和陰影算圖（第 34 課）"), mcw({"t": "ray"}),
        ("h", u"9. 選擇權定價（第 39 課）"), mcw({"t": "option"}),
        ("h", u"10. 退休規劃（第 41 課）"), mcw({"t": "retire"}),
    ],
}

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"蒙地卡羅公式速查", "h1": u"蒙地卡羅公式速查", "icon": u"🗂️",
    "description": u"核心公式、方法比較與術語",
    "body": [
        ("h", u"1. 核心公式"),
        ("t", [u"公式", u"意義", u"課"],
         [[u"μ̂ = (1/N) Σ f(Xᵢ)", u"蒙地卡羅估計", LS(5)], [u"SE = σ/√N", u"標準誤", LS(5)], [u"π ≈ 4 × 圓內比例", u"丟點估 π", LS(4)],
          [u"P(壓線) = 2ℓ/(πd)", u"蒲豐投針", LS(3)], [u"xₙ₊₁ = (a xₙ + c) mod m", u"線性同餘法", LS(8)], [u"X = F⁻¹(U)", u"反函數法", LS(11)],
          [u"Z = √(−2 ln U₁) cos(2πU₂)", u"Box–Muller", LS(12)], [u"∫f = (b−a) E[f(X)]", u"蒙地卡羅積分", LS(13)],
          [u"E_g[f/g]", u"重要性抽樣", LS(16)], [u"μ̂ − c(ĥ − μ_h)", u"控制變數", LS(17)], [u"μ̂ ± 1.96 s/√N", u"95% 信賴區間", LS(19)],
          [u"α = min(1, p(x′)/p(x))", u"梅特羅波利斯", LS(21)], [u"N_eff = N/τ", u"有效樣本數", LS(24)],
          [u"e^(−ΔE/T)", u"模擬退火接受率", LS(28)], [u"w/n + c√(ln N / n)", u"UCB（MCTS）", LS(29)], [u"C = e^(−rT) E[max(S_T − K, 0)]", u"選擇權定價", LS(39)]]),
        ("h", u"2. 變異數縮減方法"),
        ("t", [u"方法", u"想法", u"課"],
         [[u"重要性抽樣", u"在重要的地方多抽，用權重修正", LS(16)], [u"分層抽樣", u"每一層各抽固定數量", LS(17)],
          [u"控制變數", u"用答案已知的相似量抵消誤差", LS(17)], [u"對偶變數", u"同時用 U 與 1 − U", LS(17)], [u"準蒙地卡羅", u"低差異序列", LS(18)]]),
        ("h", u"3. 術語"),
        ("t", [u"術語", u"英文", u"課"],
         [[u"偽隨機數", u"pseudo-random number", LS(7)], [u"種子", u"seed", LS(7)], [u"接受—拒絕法", u"acceptance–rejection", LS(12)],
          [u"維度的詛咒", u"curse of dimensionality", LS(15)], [u"低差異序列", u"low-discrepancy sequence", LS(18)],
          [u"馬可夫鏈蒙地卡羅", u"MCMC", LS(20)], [u"細緻平衡", u"detailed balance", LS(22)], [u"吉布斯抽樣", u"Gibbs sampling", LS(23)],
          [u"預燒期", u"burn-in", LS(24)], [u"哈密頓蒙地卡羅", u"Hamiltonian Monte Carlo", LS(26)], [u"模擬退火", u"simulated annealing", LS(28)],
          [u"蒙地卡羅樹搜尋", u"MCTS", LS(29)], [u"路徑追蹤", u"path tracing", LS(34)], [u"系集預報", u"ensemble forecasting", LS(37)],
          [u"風險值", u"Value at Risk", LS(40)], [u"預期短缺", u"Expected Shortfall", LS(40)]]),
    ],
}

REFERENCES = [LAB, CHEATSHEET]
