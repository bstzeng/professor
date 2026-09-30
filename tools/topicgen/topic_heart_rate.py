# -*- coding: utf-8 -*-
"""心率與有氧運動主題的規格：把 hr_p1…hr_p4 的模組與兩個參考頁串起來。"""
import hr_p1, hr_p2, hr_p3, hr_p4, hr_ref

TOPIC = {
    "id": "heart-rate-aerobic",
    "category": "biomed",
    "title": "心率與有氧運動：從心臟生理到心率區間訓練",
    "short": "心率與有氧運動",
    "crumb": "心率與有氧運動",
    "icon": "🏃",
    "description": "心臟怎麼調整心率、有氧與無氧能量系統如何分工、為什麼心率能代表運動強度；"
                   "學會計算最大心率與五個心率區間，理解 Zone 2、間歇與 80/20 訓練，"
                   "看懂天氣、藥物與穿戴裝置對心率的影響，最後設計自己的有氧計畫並掌握安全警訊。",
}

MODULES = hr_p1.MODULES + hr_p2.MODULES + hr_p3.MODULES + hr_p4.MODULES

REFERENCES = hr_ref.REFERENCES
