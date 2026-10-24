# -*- coding: utf-8 -*-
"""晶片的分區規劃主題的規格。"""
import cfp_a, cfp_e, cfp_ref

TOPIC = {
    "id": "chip-floorplan",
    "category": "tech",
    "title": u"晶片的分區規劃：Floorplan 怎麼排、怎麼連",
    "short": u"晶片分區規劃",
    "crumb": u"分區規劃",
    "icon": u"🧩",
    "description": u"一顆 SoC 裡有哪些區域、為什麼這樣擺、彼此怎麼連，每課完整推導：CPU、GPU、NPU、多媒體、安全區、系統控制；SRAM 巨集、快取階層、DDR 與 HBM、記憶體修復；"
                   u"I/O 環與凸塊、高速 PHY、類比與隔離、溫度感測、射頻；匯流排、交叉開關、NoC、快取一致性、長線與中繼器、金屬層、資料流預算；"
                   u"電源域與開關、電源網格壓降、時脈與跨時脈域、DVFS、散熱；放置演算法、Rent 定律、測試與良率、手機 SoC 與 AI 加速器案例、chiplet 與 UCIe。附 floorplan 拼圖等互動工具。",
}

MODULES = cfp_a.MODULES + cfp_e.MODULES

REFERENCES = cfp_ref.REFERENCES
