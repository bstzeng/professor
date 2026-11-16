# -*- coding: utf-8 -*-
"""貝氏統計主題的規格。"""
import bay_a, bay_f, bay_ref

TOPIC = {
    "id": "bayesian-statistics",
    "category": "math",
    "title": u"貝氏統計：用機率更新你的信念",
    "short": u"貝氏統計",
    "crumb": u"貝氏統計",
    "icon": u"🎲",
    "description": u"頻率派與貝氏派、貝氏定理推導、醫學檢驗悖論、蒙提霍爾、莎莉・克拉克案；Beta—二項式、常態—常態與卡爾曼濾波、卜瓦松—伽瑪、可信區間、先驗的選擇；"
                   u"貝葉斯與拉普拉斯、費雪、圖靈與恩尼格瑪、搜尋氫彈與法航 447；MCMC、吉布斯、HMC 與 NUTS、收斂診斷、變分推論；"
                   u"貝氏迴歸、八所學校階層模型、貝氏因子、奧坎剃刀；p 值與重現危機、林德利悖論、5σ；垃圾郵件、A/B 測試、天氣、選舉、臨床試驗、重力波；貝氏神經網路、高斯過程、貝氏大腦。附四個互動模擬。",
}

MODULES = bay_a.MODULES + bay_f.MODULES
REFERENCES = bay_ref.REFERENCES
