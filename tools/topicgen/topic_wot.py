# -*- coding: utf-8 -*-
"""時光之輪主題的規格。"""
import wt_a, wt_e, wt_ref

TOPIC = {
    "id": "wheel-of-time",
    "category": "fantasy",
    "title": "時光之輪：轉生真龍與永恆輪迴的史詩",
    "short": "時光之輪",
    "crumb": "時光之輪",
    "icon": "☸️",
    "description": "羅伯特·喬丹與布蘭登·山德森的十五本奇幻史詩完整導讀：作者與出版歷程、閱讀策略與泥沼期；時光之輪、紋路與時代輪迴、"
                   "至上力、暗帝、被棄者與真龍預言；白塔七宗、護法、艾伊爾、光之子、聖桑與暗影；兩河五人組；全系列劇情從冬夜到最後之戰；"
                   "性別、神話、救世主的負擔、寫作風格、Amazon 影集與影響。附大陸地圖、勢力卡、人物圖與比較表。",
}

MODULES = wt_a.MODULES + wt_e.MODULES

REFERENCES = wt_ref.REFERENCES
