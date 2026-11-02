# -*- coding: utf-8 -*-
"""氣象學與颱風預報（wx_）。"""
import wx_a, wx_d, wx_f, wx_ref

TOPIC = {
    "id": "weather-typhoon",
    "category": "science",
    "title": u"氣象學與颱風預報：從一團空氣到颱風路徑",
    "short": u"氣象學與颱風預報",
    "crumb": u"氣象與颱風",
    "icon": u"🌀",
    "description": u"大氣的組成與觀測；輻射收支、壓高公式、潛熱、飽和水氣壓、絕熱過程與雲底、大氣穩定度與 CAPE、雲雨形成；氣壓梯度力、科氏力、地轉風、邊界層、熱力風與噴流、渦度與羅士比波、全球環流與季風；"
                   u"鋒面、溫帶氣旋、寒流、梅雨、雷雨、龍捲風、焚風與台灣一年的天氣；颱風的形成、結構、強度、路徑、中央山脈的影響、西南氣流與共伴效應、警報與颱風假、經典颱風；原始方程、數值預報、參數化、資料同化、混沌與系集；AI 氣象模型、氣候變遷、聖嬰與空氣品質。附公式與 7 個互動工具。",
}

MODULES = wx_a.MODULES + wx_d.MODULES + wx_f.MODULES
REFERENCES = wx_ref.REFERENCES
