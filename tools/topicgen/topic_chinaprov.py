# -*- coding: utf-8 -*-
"""中國各省主題的規格。"""
import cnp_a, cnp_n, cnp_e, cnp_c, cnp_w, cnp_ref

TOPIC = {
    "id": "china-provinces",
    "category": "geography",
    "title": u"中國各省：位置、古城、小吃與世界遺產",
    "short": u"中國各省",
    "crumb": u"中國各省",
    "icon": u"🏯",
    "description": u"一省一課，依華北、東北、華東、華中、華南、西南、西北七大分區介紹 31 個省、自治區、直轄市與香港、澳門："
                   u"每課有位置地圖、一句話記憶、簡稱與省會、大城市與古稱、地理與歷史、方言與民族、代表小吃、世界遺產、非物質文化遺產、"
                   u"旅遊建議（季節、天數、路線）與常見誤解。另有行政區劃、地形三級階梯、簡稱記憶、各省比較、世界遺產總表與八大菜系，"
                   u"附可點選的互動地圖、找省測驗與排行比較。",
}

MODULES = [cnp_a.MODULE_A] + cnp_n.MODULES + cnp_e.MODULES + cnp_c.MODULES + cnp_w.MODULES + [cnp_a.MODULE_I]

REFERENCES = cnp_ref.REFERENCES
