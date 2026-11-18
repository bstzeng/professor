# -*- coding: utf-8 -*-
"""手機是怎麼連上網的 的規格。"""
import mob_a, mob_ref

TOPIC = {
    "id": "mobile-networks", "category": "tech",
    "title": u"手機是怎麼連上網的：基地台、SIM 卡、換手與 5G",
    "short": u"手機怎麼連上網", "crumb": u"行動網路", "icon": u"📱",
    "description": u"蜂巢的概念、基地台的構造、OFDM 與排程；SIM 卡與 IMSI、認證與加密、eSIM、號碼與攜碼；開機註冊、待機與省電、呼叫、換手、核心網路、封包的隧道與 IP、國際漫遊；簡訊、VoLTE、國家級警報的細胞廣播、手機定位；"
                   u"5G 的新特性、網路切片與邊緣運算、Open RAN、衛星直連手機；收訊不好的原因、跨年塞網、假基地台、SIM 卡挾持與信令漏洞、台灣的行動網路。附開機、呼叫、換手、簡訊、漫遊的流程動畫與換手模擬。",
}
MODULES = mob_a.MODULES
REFERENCES = mob_ref.REFERENCES
