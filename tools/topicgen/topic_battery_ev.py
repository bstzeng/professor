# -*- coding: utf-8 -*-
"""電池與電動車主題的規格。"""
import bat_a, bat_c, bat_e, bat_ref

TOPIC = {
    "id": "battery-ev",
    "category": "tech",
    "title": u"電池與電動車：從電化學到能源轉型",
    "short": u"電池與電動車",
    "crumb": u"電池與電動車",
    "icon": u"🔋",
    "description": u"氧化還原、電壓與容量、能量與功率、C 率；鋰離子的運作、NMC 與 LFP、石墨負極、電解液與 SEI、電芯形式、能量密度、BMS 與熱管理；熱失控、衰退、充電習慣、溫度與快充；"
                   u"固態、鈉離子、矽負極、4680 與刀片電池；馬達與逆變器、回生制動、續航、充電標準、台灣的換電與充電、特斯拉與比亞迪、總持有成本；關鍵礦產、回收、V2G、電網儲能、台灣產業與政策、生命週期碳排。含續航、充電曲線、能源成本與電池衰退互動模擬。",
}

MODULES = bat_a.MODULES + bat_c.MODULES + bat_e.MODULES
REFERENCES = bat_ref.REFERENCES
