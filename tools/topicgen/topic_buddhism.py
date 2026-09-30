# -*- coding: utf-8 -*-
"""佛教入門:教義、歷史,以及《心經》《大悲咒》解說。"""
import bd_a, bd_b, bd_c, bd_d, bd_e, bd_f, bd_h, bd_i, bd_ref

TOPIC = {
    "id": "buddhism",
    "category": "religion",
    "title": "佛教入門:教義、歷史,以及《心經》《大悲咒》解說",
    "short": "佛教入門",
    "crumb": "佛教入門",
    "icon": "🪷",
    "description": "從佛陀的生平與時代講起,介紹四聖諦、八正道、緣起、五蘊、業與輪迴、涅槃等核心教義;"
                   "走過部派、南傳與大乘,佛教傳入中國與天台、華嚴、淨土、禪,藏傳與台灣佛教;"
                   "再逐句解說《心經》,並介紹《大悲咒》的出處、結構與梵文研究。以介紹與理解為目的,"
                   "並列傳統說法與學術觀點。附名詞速查、互動《心經》逐句讀與《大悲咒》分段對照。",
}

MODULES = (bd_a.MODULES + bd_b.MODULES + bd_c.MODULES + bd_d.MODULES + bd_e.MODULES
           + bd_f.MODULES + bd_h.MODULES + bd_i.MODULES)

REFERENCES = bd_ref.REFERENCES
