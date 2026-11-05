# -*- coding: utf-8 -*-
"""氣候變遷主題的規格。"""
import clm_a, clm_c, clm_e, clm_ref

TOPIC = {
    "id": "climate-change",
    "category": "science",
    "title": u"氣候變遷：證據、模型與爭議",
    "short": u"氣候變遷",
    "crumb": u"氣候變遷",
    "icon": u"🌡️",
    "description": u"天氣與氣候、能量收支、溫室效應的物理、碳循環、海洋、冰與反照率、回饋；溫度紀錄、基林曲線、冰芯、米蘭科維奇循環、古氣候事件、海平面與冰川、歸因科學；氣候模型、氣候敏感度、排放情境、模型的檢驗、IPCC 與不確定性；"
                   u"極端天氣、颱風、海洋酸化與珊瑚白化、生態系、糧食水與健康、臨界點、台灣的氣候變遷、氣候正義；減碳全貌、能源轉型、難減部門、碳移除、地球工程、碳定價與碳費、巴黎協定、台灣淨零；常見懷疑論點與真正的爭論。含二氧化碳與溫度、平衡暖化、碳預算互動工具。",
}

MODULES = clm_a.MODULES + clm_c.MODULES + clm_e.MODULES
REFERENCES = clm_ref.REFERENCES
