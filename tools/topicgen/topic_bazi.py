# -*- coding: utf-8 -*-
"""八字命理主題的規格。"""
import bz_a, bz_e, bz_ref

TOPIC = {
    "id": "bazi",
    "category": "divination",
    "title": "八字命理：一套關於時間的符號系統",
    "short": "八字命理",
    "crumb": "八字",
    "icon": "☯️",
    "description": "四柱八字的完整導讀：歷史與文化角色；陰陽五行、天干地支、藏干、六十甲子與合沖刑害；以立春與節氣排年月、五虎遁五鼠遁、"
                   "真太陽時與夏令時間、大運流年；十神與六親；日主強弱、格局、用神、十二長生、神煞、宮位；合婚、擇日、取名；"
                   "雙胞胎、巴納姆效應、時間雙胞胎研究等理性檢視；東亞比較與消費提醒。附天文公式節氣排盤器（已與萬年曆程式交叉驗證）。",
}

MODULES = bz_a.MODULES + bz_e.MODULES

REFERENCES = bz_ref.REFERENCES
