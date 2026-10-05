# -*- coding: utf-8 -*-
"""法西斯主義主題的規格。"""
import fa_a, fa_e, fa_ref

TOPIC = {
    "id": "fascism",
    "category": "history",
    "title": u"法西斯主義：起源、運作與教訓",
    "short": u"法西斯主義",
    "crumb": u"法西斯主義",
    "icon": u"📜",
    "description": u"以 Paxton、Griffin、Eco 等學者研究為基礎的法西斯主義歷史導讀：語源與定義、與威權及極權的區別；一戰與戰後危機；"
                   u"墨索里尼的崛起、進軍羅馬與法西斯義大利；威瑪共和、大蕭條與納粹選票、1933 年的一體化、種族迫害與大屠殺；"
                   u"西班牙、葡萄牙、奧地利、東歐與日本的比較；領袖崇拜、宣傳、暴力、群眾組織、經濟與菁英共謀；二戰、崩潰、紐倫堡與戰後民主的防衛；"
                   u"Paxton 五階段與民主如何保護自己。附五個互動工具。",
}

MODULES = fa_a.MODULES + fa_e.MODULES

REFERENCES = fa_ref.REFERENCES
