# -*- coding: utf-8 -*-
"""系統動力學主題的規格。"""
import sy_a, sy_e, sy_ref

TOPIC = {
    "id": "system-dynamics",
    "category": "math",
    "title": "系統動力學：為什麼好意常帶來壞結果？",
    "short": "系統動力學",
    "crumb": "系統動力學",
    "icon": "🔄",
    "description": "系統思考與冰山模型、政策抵抗；存量與流量、浴缸模型與 MIT 浴缸測驗；增強與調節迴路、S 型曲線、延遲造成的振盪；"
                   "六種行為模式、臨界點與非線性；七個系統基模（成長上限、捨本逐末、公地悲劇……）；啤酒遊戲、SIR、獵物掠食者、"
                   "巴斯擴散、城市動力學與《成長的極限》；建模流程、工具、驗證與梅多斯的槓桿點。附浴缸與十種模型的互動模擬。",
}

MODULES = sy_a.MODULES + sy_e.MODULES

REFERENCES = sy_ref.REFERENCES
