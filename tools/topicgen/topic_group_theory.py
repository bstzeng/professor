# -*- coding: utf-8 -*-
"""群論主題的規格。"""
import grp_a, grp_f, grp_ref

TOPIC = {
    "id": "group-theory",
    "category": "math",
    "title": u"群論：對稱的數學",
    "short": u"群論",
    "crumb": u"群論",
    "icon": u"🔷",
    "description": u"對稱是動作：二面體群、群的公理；循環群與模算術、子群、置換與奇偶、拉格朗日定理、同構、同態、正規子群與商群；"
                   u"魔術方塊群與上帝之數、十五數字推盤、17 種壁紙群、230 種空間群與準晶體、正多面體、密碼學；三次方程式的恩怨、阿貝爾、伽羅瓦的決鬥、伽羅瓦群、A₅ 與五次方程式、尺規作圖；"
                   u"李群、諾特定理、SU(2) 與自旋、八重道與夸克、規範對稱；有限單群分類、怪獸月光。附五個互動元件。",
}

MODULES = grp_a.MODULES + grp_f.MODULES
REFERENCES = grp_ref.REFERENCES
