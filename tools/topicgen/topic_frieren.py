# -*- coding: utf-8 -*-
"""葬送的芙莉蓮主題的規格。"""
import frn_a, frn_c, frn_ref

TOPIC = {
    "id": "frieren",
    "category": "anime",
    "title": u"葬送的芙莉蓮：勇者打倒魔王之後",
    "short": u"葬送的芙莉蓮",
    "crumb": u"葬送的芙莉蓮",
    "icon": u"🌸",
    "description": u"山田鐘人與阿部司的原作、Madhouse 的動畫；勇者一行、魔法體系、魔族的本質、女神與僧侶、大陸魔法協會與旅程的目的地；"
                   u"辛美爾之死、費倫與修塔爾克、庫瓦爾、斷頭台的阿烏拉、贊恩、一級魔法使考試，以及北方高原、黃金鄉與帝國篇概要（含漫畫劇透）；芙莉蓮、費倫、修塔爾克、辛美爾、芙拉梅與賽莉耶、一級魔法使與魔族群像；時間與壽命、記憶與後悔、無用的魔法、善意的傳承、無法理解的他者與後日談奇幻。",
}

MODULES = frn_a.MODULES + frn_c.MODULES
REFERENCES = frn_ref.REFERENCES
