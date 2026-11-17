# -*- coding: utf-8 -*-
"""拓撲學主題的規格。"""
import top_a, top_f, top_ref

TOPIC = {
    "id": "topology",
    "category": "math",
    "title": u"拓撲學：甜甜圈與咖啡杯",
    "short": u"拓撲學",
    "crumb": u"拓撲學",
    "icon": u"🍩",
    "description": u"橡皮幾何與同胚、柯尼斯堡七橋、拓撲不變量；莫比烏斯帶、克萊因瓶、射影平面、可定向性、尤拉示性數、曲面分類、高斯—博內定理；"
                   u"布勞威爾不動點、毛球定理、波蘇克—烏拉姆、火腿三明治；基本群、纏繞數與代數基本定理、覆蓋空間、同調、三維球面；"
                   u"紐結、三色著色、瓊斯多項式、DNA 與分子機器；龐加萊猜想、幾何化、裴瑞爾曼、拓撲資料分析、拓撲物態。附五個互動元件。",
}

MODULES = top_a.MODULES + top_f.MODULES
REFERENCES = top_ref.REFERENCES
