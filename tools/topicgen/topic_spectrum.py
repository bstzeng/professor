# -*- coding: utf-8 -*-
"""電波頻譜的世界主題的規格。"""
import rf_a, rf_e, rf_ref

TOPIC = {
    "id": "radio-spectrum",
    "category": "tech",
    "title": u"電波頻譜的世界：看不見的無線電資源",
    "short": u"電波頻譜的世界",
    "crumb": u"電波頻譜",
    "icon": u"📡",
    "description": u"我們生活在電波之中：電磁頻譜全圖、頻率波長與能量、游離與非游離輻射、頻譜為何稀缺；傳播、穿牆、電離層、多路徑、都卜勒、天線；"
                   u"從潛艦長波、AM、短波、FM 與航空、UHF 黃金頻段、2.4 GHz 與微波爐、5／6 GHz Wi-Fi、2G～5G、毫米波、衛星頻段、雷達到無線電天文；"
                   u"調變、頻寬、OFDM、波束成形、動態共享；ITU、頻率分配表、執照與免執照、頻譜拍賣、NCC 與數位發展部、5G 與高度計爭議；基地台、Wi-Fi、悠遊卡、GPS 干擾、電子戰、業餘無線電；"
                   u"電磁波與健康的研究證據、頻譜與國安、6G。附頻譜互動圖、Wi-Fi 頻道重疊等六個互動工具。",
}

MODULES = rf_a.MODULES + rf_e.MODULES

REFERENCES = rf_ref.REFERENCES
