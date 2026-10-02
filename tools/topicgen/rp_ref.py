# -*- coding: utf-8 -*-
"""隨機過程與馬可夫鏈：參考頁——互動實驗室、公式速查。"""
from rp_common import LS, RPLIB, rpw

LAB = {
    "file": "lab.html", "title": u"隨機過程互動實驗室", "h1": u"隨機過程互動實驗室", "icon": u"🧪",
    "description": u"樣本路徑、賭徒破產、高爾頓板、天氣馬可夫鏈、蛇梯棋、PageRank、分支過程、幾何布朗運動、文字產生器",
    "body": [
        ("raw", u"<script>%s</script>" % RPLIB),
        ("p", u"所有模擬都在你的瀏覽器裡執行，每次結果略有不同。"),
        ("h", u"1. 樣本路徑（第 4 課）"), rpw({"t": "paths"}),
        ("h", u"2. 賭徒破產（第 8 課）"), rpw({"t": "ruin"}),
        ("h", u"3. 高爾頓板（第 12 課）"), rpw({"t": "galton"}),
        ("h", u"4. 天氣馬可夫鏈（第 15 課）"), rpw({"t": "chain"}),
        ("h", u"5. 蛇梯棋（第 19 課）"), rpw({"t": "snake"}),
        ("h", u"6. PageRank（第 26 課）"), rpw({"t": "pr"}),
        ("h", u"7. 分支過程（第 32 課）"), rpw({"t": "branch"}),
        ("h", u"8. 幾何布朗運動（第 39 課）"), rpw({"t": "gbm"}),
        ("h", u"9. 馬可夫文字產生器（第 43 課）"), rpw({"t": "text"}),
    ],
}

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"隨機過程公式速查", "h1": u"隨機過程公式速查", "icon": u"🗂️",
    "description": u"核心公式與術語",
    "body": [
        ("h", u"1. 核心公式"),
        ("t", [u"公式", u"意義", u"課"],
         [[u"E[Sₙ] = n(p − q)，Var = 4npq", u"簡單隨機漫步", LS(7)], [u"P = (1 − (q/p)^a)/(1 − (q/p)^N)", u"賭徒破產", LS(8)],
          [u"P(Xₙ₊₁ | Xₙ, …, X₀) = P(Xₙ₊₁ | Xₙ)", u"馬可夫性質", LS(14)], [u"πₙ = π₀Pⁿ", u"分布的演化", LS(16)],
          [u"N = (I − Q)⁻¹", u"吸收鏈的基本矩陣", LS(19)], [u"πP = π", u"平穩分布", LS(22)], [u"πᵢPᵢⱼ = πⱼPⱼᵢ", u"細緻平衡", LS(25)],
          [u"PR(j) = (1−d)/N + d Σ PR(i)/out(i)", u"PageRank", LS(26)], [u"誤差 ≈ |λ₂|ⁿ", u"收斂速度", LS(27)],
          [u"P(N(t)=k) = (λt)ᵏe^(−λt)/k!", u"卜瓦松過程", LS(28)], [u"πQ = 0", u"連續時間平穩分布", LS(30)], [u"q = G(q)", u"分支過程滅絕機率", LS(32)],
          [u"(dW)² = dt", u"二次變分", LS(36)], [u"df = f′dX + ½f″σ²dt", u"伊藤引理", LS(38)], [u"S(t) = S₀ exp((μ − σ²/2)t + σW)", u"幾何布朗運動", LS(39)],
          [u"V(s) = maxₐ [r + γ Σ P V(s′)]", u"貝爾曼方程", LS(42)], [u"E[Mₙ₊₁ | 過去] = Mₙ", u"鞅", LS(44)]]),
        ("h", u"2. 術語"),
        ("t", [u"術語", u"英文", u"課"],
         [[u"樣本路徑", u"sample path", LS(4)], [u"轉移矩陣", u"transition matrix", LS(15)], [u"常返／暫態", u"recurrent / transient", LS(17)],
          [u"吸收態", u"absorbing state", LS(17)], [u"不可約", u"irreducible", LS(18)], [u"平穩分布", u"stationary distribution", LS(22)],
          [u"遍歷", u"ergodic", LS(23)], [u"混合時間", u"mixing time", LS(24)], [u"生成矩陣", u"generator matrix", LS(30)],
          [u"維納過程", u"Wiener process", LS(34)], [u"隱馬可夫模型", u"hidden Markov model", LS(41)], [u"鞅", u"martingale", LS(44)]]),
        ("p", u"涉及金融的內容僅為教育用途，不構成投資建議。"),
    ],
}

REFERENCES = [LAB, CHEATSHEET]
