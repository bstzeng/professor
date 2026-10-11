# -*- coding: utf-8 -*-
"""蝦皮的商業模式主題的規格。"""
import shp_a, shp_e, shp_ref

TOPIC = {
    "id": "shopee-business",
    "category": "finance",
    "title": u"蝦皮的商業模式：從燒錢到獲利",
    "short": u"蝦皮的商業模式",
    "crumb": u"蝦皮的商業模式",
    "icon": u"🦐",
    "description": u"蝦皮怎麼從 2015 年的新創變成東南亞與台灣的電商龍頭？它靠什麼賺錢？從母公司 Sea 與 Garena 的資金、手機優先、免費上架與免運補貼、網路效應、在地化與遊戲化，"
                   u"到手續費、廣告、物流、金融與跨境的營收結構；2022 年的大撤退與轉虧為盈、近年財報解讀、台灣的店到店與賣家成本，以及 Lazada、TikTok Shop、Temu、momo 等對手。附大事記、平台飛輪、財報圖表與賣家費用試算器。",
}

MODULES = shp_a.MODULES + shp_e.MODULES

REFERENCES = shp_ref.REFERENCES
