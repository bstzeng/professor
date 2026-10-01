# -*- coding: utf-8 -*-
"""皇帝的一天主題的規格。"""
import em_a, em_d, em_g, em_i, em_ref

TOPIC = {
    "id": "emperor-life",
    "category": "history",
    "title": "皇帝的一天：中國歷代帝王的生活",
    "short": "皇帝的一天",
    "crumb": "皇帝的一天",
    "icon": "👑",
    "description": "根據起居注、實錄、奏摺硃批、膳底檔與回憶錄，重建歷代皇帝從起床到就寢的一天："
                   "秦始皇的一百二十斤竹簡、唐太宗與魏徵、宋仁宗忍住的宵夜、朱元璋的奏章山、萬曆的罷工、雍正的硃批、溥儀的自行車。"
                   "也談稱號、宮殿、御膳、後宮、皇子教育與御醫，並分清正史、野史與戲劇。附稱號解碼器、日程對照表與「皇帝 vs 百姓」。",
}

MODULES = em_a.MODULES + em_d.MODULES + em_g.MODULES + em_i.MODULES

REFERENCES = em_ref.REFERENCES
