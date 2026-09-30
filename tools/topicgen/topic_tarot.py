# -*- coding: utf-8 -*-
"""塔羅牌占卜主題的規格：把 ta_p1…ta_p5 的模組與兩個參考頁串起來。"""
import ta_p1, ta_p2, ta_p3, ta_p4, ta_p5, ta_ref

TOPIC = {
    "id": "tarot",
    "category": "divination",
    "title": "塔羅牌占卜：牌是怎麼抽、怎麼讀的",
    "short": "塔羅牌占卜",
    "crumb": "塔羅牌占卜",
    "icon": "🃏",
    "description": "從 15 世紀義大利的紙牌遊戲談起，認識 78 張牌的結構、愚人之旅與四種花色；"
                   "學會設定問題、洗牌抽牌、正逆位與各種牌陣，練習位置、組合、統計與敘事的解牌技巧；"
                   "最後從心理學角度理解它為什麼「感覺很準」，以及如何健康地使用。",
}

MODULES = ta_p1.MODULES + ta_p2.MODULES + ta_p3.MODULES + ta_p4.MODULES + ta_p5.MODULES

REFERENCES = ta_ref.REFERENCES
