# -*- coding: utf-8 -*-
"""選擇權與 Black–Scholes 主題的規格。"""
import opt_a, opt_f, opt_ref

TOPIC = {
    "id": "options-black-scholes",
    "category": "finance",
    "title": u"選擇權與 Black–Scholes",
    "short": u"選擇權",
    "crumb": u"選擇權",
    "icon": u"📈",
    "description": u"衍生性商品的歷史、買權與賣權、損益圖與策略、買賣權平價；無套利複製、風險中性機率、多期二項樹、美式選擇權；"
                   u"巴舍利耶、布朗運動、幾何布朗運動、伊藤積分與伊藤引理、蒙地卡羅定價；Black–Scholes 方程式與公式、N(d₁) 與 N(d₂)、熱傳導方程式；"
                   u"希臘字母、Delta 避險、隱含波動度與微笑；台指選擇權與 2018 年選擇權之亂、VIX、1987 年股災、LTCM、肥尾與黑天鵝。附五個互動模擬。",
}

MODULES = opt_a.MODULES + opt_f.MODULES
REFERENCES = opt_ref.REFERENCES
