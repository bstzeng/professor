# -*- coding: utf-8 -*-
"""離散數學：從邏輯、證明到圖論與 P vs NP（dsc_）。"""
import dsc_a, dsc_c, dsc_e, dsc_g, dsc_ref

TOPIC = {
    "id": "discrete-math",
    "category": "math",
    "title": u"離散數學：從邏輯、證明、計數到圖論與 P vs NP",
    "short": u"離散數學",
    "crumb": u"離散數學",
    "icon": u"🔢",
    "description": u"電腦科學的數學基礎：命題邏輯與量詞、各種證明方法與歸納法、集合函數與關係、數論到 RSA、排列組合與鴿籠排容、遞迴與大 O、離散機率、圖論演算法（歐拉、最短路徑、最小生成樹、配對、著色、網路流），一路到有限自動機與 P vs NP，附真值表、圖論遊樂場等互動元件。",
}

MODULES = dsc_a.MODULES + dsc_c.MODULES + dsc_e.MODULES + dsc_g.MODULES
REFERENCES = dsc_ref.REFERENCES
