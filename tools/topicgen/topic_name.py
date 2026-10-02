# -*- coding: utf-8 -*-
"""姓名學主題的規格。"""
import xm_a, xm_e, xm_ref

TOPIC = {
    "id": "name-study",
    "category": "divination",
    "title": "姓名學：筆畫、五格與好名字的語言學",
    "short": "姓名學",
    "crumb": "姓名學",
    "icon": "✍️",
    "description": "姓名學完整導讀：古代名字號與避諱、五格剖象法的日本起源與台灣改名潮；康熙筆畫、部首還原、數字字與複姓；"
                   "天人地外總五格、八十一數理、三才與內部矛盾；八字、生肖、字音、字形等流派；聲調、諧音、典故、冷僻字等好名字的語言學；"
                   "取名流程、改名法規、英文名與品牌命名；名字效應研究與理性檢視。附一萬三千字康熙筆畫的五格計算器。",
}

MODULES = xm_a.MODULES + xm_e.MODULES

REFERENCES = xm_ref.REFERENCES
