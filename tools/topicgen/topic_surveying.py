# -*- coding: utf-8 -*-
"""土木測量：從三腳架到衛星與光達（svy_）。"""
import svy_a, svy_c, svy_f, svy_h, svy_ref

TOPIC = {
    "id": "surveying",
    "category": "tech",
    "title": u"土木測量：從路邊的三腳架到衛星定位、光達與數位孿生",
    "short": u"土木測量",
    "crumb": u"土木測量",
    "icon": u"📐",
    "description": u"路邊的三腳架到底在量什麼？從距離、角度、高差三個基本量出發：地球形狀與台灣的 TWD97 座標、誤差與平差、捲尺與電子測距、水準測量與地層下陷、經緯儀與全站儀、導線與交會、GPS 原理與 RTK、e-GNSS、地形與土方、施工放樣、道路曲線、隧道貫通、變形監測、地籍鑑界與都市計畫樁，到航空攝影、無人機、光達、InSAR 與 BIM。附整平、水準、導線、GPS 交會、等高線、土方、曲線放樣等互動工具，以及完整公式。",
}

MODULES = svy_a.MODULES + svy_c.MODULES + svy_f.MODULES + svy_h.MODULES
REFERENCES = svy_ref.REFERENCES
