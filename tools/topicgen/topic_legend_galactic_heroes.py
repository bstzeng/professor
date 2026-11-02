# -*- coding: utf-8 -*-
"""銀河英雄傳說主題的規格。"""
import lgh_a, lgh_c, lgh_e, lgh_ref

TOPIC = {
    "id": "legend-galactic-heroes",
    "category": "fantasy",
    "title": u"銀河英雄傳說：帝國與同盟",
    "short": u"銀河英雄傳說",
    "crumb": u"銀河英雄傳說",
    "icon": u"🌌",
    "description": u"田中芳樹正傳十卷完整導讀（完整劇透）：作者與動畫、帝國同盟費沙與兩條迴廊、魯道夫與海尼森的前史；萊因哈特、楊威利、吉爾菲艾斯、帝國雙璧、奧貝斯坦、楊艦隊、同盟政客、費沙與地球教；"
                   u"黎明篇到落日篇與外傳逐卷導讀；亞斯提、伊謝爾倫、亞姆立札、李普休達特與威斯塔朗特、多利亞、要塞對要塞、巴米利恩、迴廊之戰、希瓦等經典戰役解析；民主與專制、戰略與戰術、與真實歷史的對照、地球教、忠誠與背叛、軍事設定與影響。",
}

MODULES = lgh_a.MODULES + lgh_c.MODULES + lgh_e.MODULES
REFERENCES = lgh_ref.REFERENCES
