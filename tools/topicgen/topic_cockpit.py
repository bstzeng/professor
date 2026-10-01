# -*- coding: utf-8 -*-
"""駕駛艙儀表全圖解主題的規格。"""
import ck_a, ck_c, ck_f, ck_ref

TOPIC = {
    "id": "cockpit-panels",
    "category": "tech",
    "title": "駕駛艙儀表全圖解：飛機上每一塊面板在做什麼",
    "short": "駕駛艙儀表全圖解",
    "crumb": "駕駛艙儀表",
    "icon": "🎛️",
    "description": "用一張可以點擊的駕駛艙地圖，逐區認識客機駕駛艙：六大儀表、主飛行顯示器、導航顯示器（氣象雷達、TCAS、地形）、"
                   "引擎與中央警告系統、自動駕駛面板、中央操縱台與頭頂面板的電力、液壓、燃油、空調、防冰、火警、氧氣。"
                   "附六大儀表、PFD、ND、ECAM 與自動駕駛面板的互動模擬器；圖為通用示意，不代表特定機型。",
}

MODULES = ck_a.MODULES + ck_c.MODULES + ck_f.MODULES

REFERENCES = ck_ref.REFERENCES
