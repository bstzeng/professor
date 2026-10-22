# -*- coding: utf-8 -*-
"""曲速引擎的詳細計算主題的規格。"""
import wd_a, wd_c, wd_e, wd_g, wd_ref

TOPIC = {
    "id": "warp-drive",
    "category": "science",
    "title": u"曲速引擎的詳細計算：為什麼需要巨大能量",
    "short": u"曲速引擎的計算",
    "crumb": u"曲速引擎",
    "icon": u"🛸",
    "description": u"從火箭方程式與光速因果出發，用 3+1 分解完整推導阿庫別瑞度規的外曲率、哈密頓約束與能量密度，"
                   u"積分出總能量 E ≈ −(c⁴/G)β²R²/(18Δ)，再加入福特–羅曼量子不等式，算出 Pfenning–Ford 的 10⁶² 公斤；"
                   u"比較 Van Den Broeck、Natário、White、Lentz、Bobrick–Martire 與 2024 年等速正能量解；推導卡西米爾效應；"
                   u"最後看視界、量子不穩定、粒子累積、時間機器與重力波。附能量計算器、能量密度熱圖、卡西米爾與量子不等式工具。",
}

MODULES = wd_a.MODULES + wd_c.MODULES + wd_e.MODULES + wd_g.MODULES

REFERENCES = wd_ref.REFERENCES
