# -*- coding: utf-8 -*-
"""衛星通訊主題的規格。"""
import sc_a, sc_e, sc_ref

TOPIC = {
    "id": "satellite-comms",
    "category": "tech",
    "title": u"衛星通訊：天上的訊號怎麼連到你的手機",
    "short": u"衛星通訊",
    "crumb": u"衛星通訊",
    "icon": u"🛰️",
    "description": u"為什麼需要衛星、從克拉克到 Starlink；軌道力學、低軌中軌與地球同步、仰角與覆蓋、傾角與太陽同步、星系與太空垃圾；"
                   u"頻段、天線、鏈路預算、分貝與路徑損耗、夏農容量、雨衰；取樣、調變、錯誤更正碼、多工、延遲；衛星結構、轉頻器、相位陣列、雷射鏈路、遙測指令；"
                   u"衛星電視、海空通訊、衛星電話、GPS、福衛、搜救、軍事、物聯網；Starlink、手機直連、5G NTN、烏克蘭與台灣的數位韌性；地面站、發射、產業鏈與未來。附軌道計算、鏈路預算、星系覆蓋等五個互動工具。",
}

MODULES = sc_a.MODULES + sc_e.MODULES

REFERENCES = sc_ref.REFERENCES
