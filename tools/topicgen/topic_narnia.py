# -*- coding: utf-8 -*-
"""納尼亞傳奇主題的規格。"""
import nr_a, nr_e, nr_ref

TOPIC = {
    "id": "narnia",
    "category": "fantasy",
    "title": "納尼亞傳奇：衣櫥後面的世界",
    "short": "納尼亞傳奇",
    "crumb": "納尼亞",
    "icon": "🦁",
    "description": "C·S·路易斯七部曲完整導讀：路易斯生平、托爾金與墨水會、閱讀順序之爭、納尼亞的地圖與時間；"
                   "《獅子·女巫·魔衣櫥》《賈思潘王子》《黎明行者號》《銀椅》《奇幻馬和傳說》《魔法師的外甥》《最後的戰役》逐部解析；"
                   "寓言與假想、七行星理論、蘇珊問題、卡羅門與東方主義、戰爭與死亡；BBC 影集、迪士尼電影與 Netflix 新版。附地圖、年表與人物卡。",
}

MODULES = nr_a.MODULES + nr_e.MODULES

REFERENCES = nr_ref.REFERENCES
