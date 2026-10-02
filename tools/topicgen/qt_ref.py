# -*- coding: utf-8 -*-
"""排隊理論：參考頁——互動實驗室、公式速查表。"""
from qt_common import LS, QTLIB, qtw

LAB = {
    "file": "lab.html", "title": u"排隊理論互動實驗室", "h1": u"排隊理論互動實驗室", "icon": u"🧪",
    "description": u"壅塞曲線、卜瓦松到達、M/M/c 動畫模擬、一條隊 vs. 各排各的、爾朗 C 人力計算、生產線瓶頸",
    "body": [
        ("raw", u"<script>%s</script>" % QTLIB),
        ("p", u"所有模擬都在你的瀏覽器裡執行；每次結果會因隨機性略有不同。"),
        ("h", u"1. 壅塞曲線與服務變異（第 21、31 課）"), qtw({"t": "rho", "pk": 1}),
        ("h", u"2. 卜瓦松到達（第 9 課）"), qtw({"t": "pois"}),
        ("h", u"3. M/M/c 動畫模擬（第 23、24 課）"), qtw({"t": "sim", "c": 2, "cs": 1, "lam": 1.6, "mu": 1}),
        ("h", u"4. 一條隊伍 vs. 各排各的（第 26 課）"), qtw({"t": "pool"}),
        ("h", u"5. 客服中心人力計算（第 25 課）"), qtw({"t": "erl"}),
        ("h", u"6. 生產線瓶頸（第 37 課）"), qtw({"t": "line"}),
    ],
}

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"排隊理論公式速查", "h1": u"排隊理論公式速查", "icon": u"🗂️",
    "description": u"符號、核心公式與術語",
    "body": [
        ("h", u"1. 符號"),
        ("t", [u"符號", u"意義"],
         [[u"λ", u"到達率（每單位時間來幾個）"], [u"μ", u"一個服務台的服務率（＝ 1 ÷ 平均服務時間 S）"], [u"c", u"服務台數"],
          [u"ρ = λ/(cμ)", u"使用率"], [u"L、Lq", u"系統內、隊伍中的平均人數"], [u"W、Wq", u"系統內、隊伍中的平均時間"],
          [u"A = λ/μ", u"話務量（爾朗）"], [u"cₐ、cₛ", u"到達間隔、服務時間的變異係數"]]),
        ("h", u"2. 核心公式"),
        ("t", [u"公式", u"適用", u"課"],
         [[u"L = λW，Lq = λWq", u"所有穩定系統（利特爾定律）", LS(13)], [u"W = Wq + S", u"所有系統", LS(20)],
          [u"Pₙ = (1−ρ)ρⁿ", u"M/M/1", LS(19)], [u"L = ρ/(1−ρ)，W = 1/(μ−λ)", u"M/M/1", LS(20)],
          [u"Wq = ρ/(1−ρ) × (1+cₛ²)/2 × S", u"M/G/1（P-K 公式）", LS(31)], [u"Wq ≈ ρ/(1−ρ) × (cₐ²+cₛ²)/2 × S", u"G/G/1（金曼近似）", LS(10)],
          [u"Wq = C(c,A) / (cμ − λ)", u"M/M/c（爾朗 C）", LS(25)], [u"B(k) = A·B(k−1) / (k + A·B(k−1))", u"M/M/c/c（爾朗 B）", LS(28)],
          [u"c ≈ A + β√A", u"平方根人力法則", LS(29)], [u"λ有效 = λ(1 − P_K)", u"有容量限制", LS(27)]]),
        ("h", u"3. M/M/1 等待倍數（排隊時間 ÷ 服務時間）"),
        ("t", [u"使用率", u"50%", u"70%", u"80%", u"90%", u"95%", u"99%"],
         [[u"倍數", u"1", u"2.3", u"4", u"9", u"19", u"99"]]),
        ("h", u"4. 術語"),
        ("t", [u"術語", u"英文", u"課"],
         [[u"卜瓦松過程", u"Poisson process", LS(7)], [u"無記憶性", u"memoryless", LS(8)], [u"檢查站悖論", u"inspection paradox", LS(11)],
          [u"肯德爾記號", u"Kendall notation", LS(17)], [u"生死過程", u"birth–death process", LS(18)], [u"服務水準", u"service level", LS(25)],
          [u"資源共享效應", u"pooling", LS(29)], [u"拒排／放棄", u"balking / reneging", LS(35)], [u"瓶頸", u"bottleneck", LS(37)],
          [u"尾端延遲", u"tail latency", LS(42)], [u"離散事件模擬", u"discrete-event simulation", LS(45)]]),
    ],
}

REFERENCES = [LAB, CHEATSHEET]
