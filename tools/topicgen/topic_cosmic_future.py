# -*- coding: utf-8 -*-
"""宇宙的未來主題的規格。"""
import cf_a, cf_e, cf_ref

TOPIC = {
    "id": "cosmic-future",
    "category": "science",
    "title": "宇宙的未來：從明天到時間的盡頭",
    "short": "宇宙的未來",
    "crumb": "宇宙的未來",
    "icon": "🌌",
    "description": "用現有科學推測未來：冰期、超大陸、月球遠離、太陽變亮與海洋消失；太陽變成紅巨星、白矮星，地球是否被吞沒；"
                   "太陽系的混沌與路過的恆星；銀河系與仙女座的碰撞（2025 年新研究：約一半機率）；加速膨脹、暗能量、DESI 新線索與"
                   "熱寂、大撕裂、大擠壓；恆星時代結束、質子衰變、黑洞蒸發到 10¹⁰⁰ 年的黑暗時代。每項推測都標示把握程度，附六個互動模擬。",
}

MODULES = cf_a.MODULES + cf_e.MODULES

REFERENCES = cf_ref.REFERENCES
