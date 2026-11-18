# -*- coding: utf-8 -*-
"""金融泡沫與危機史的規格。"""
import bub_a, bub_f, bub_ref

TOPIC = {
    "id": "financial-crises",
    "category": "finance",
    "title": u"金融泡沫與危機史：從鬱金香到矽谷銀行",
    "short": u"金融泡沫與危機",
    "crumb": u"泡沫與危機",
    "icon": u"🫧",
    "description": u"泡沫的定義與五個階段、槓桿與擠兌、明斯基的金融不穩定假說；鬱金香狂熱與史實、約翰・羅與密西西比、南海泡沫與牛頓、鐵路狂熱；1929 年股災、大蕭條、布列敦森林、拉美債務危機、1987 黑色星期一、日本泡沫、台灣錢淹腳目與 1990 年崩盤；"
                   u"亞洲金融風暴、LTCM、網路泡沫、2008 金融海嘯、歐債危機；加密貨幣與 FTX、GameStop、矽谷銀行；泡沫的心理學、監理的極限。附槓桿、擠兌、泡沫模擬與崩盤比較四個互動工具。",
}

MODULES = bub_a.MODULES + bub_f.MODULES
REFERENCES = bub_ref.REFERENCES
