# -*- coding: utf-8 -*-
"""韓國各市道主題的規格。"""
import krp_a, krp_data, krp_ref

TOPIC = {
    "id": "korea-regions",
    "category": "geography",
    "title": u"韓國各市道：首爾、釜山到濟州",
    "short": u"韓國各市道",
    "crumb": u"韓國各市道",
    "icon": u"🇰🇷",
    "description": u"一地一課介紹韓國 17 個市道：首爾特別市、六個廣域市、世宗特別自治市和九個道。每課有位置地圖、一句話記憶、"
                   u"韓文與名稱由來、主要地區、地理歷史、方言、美食與伴手禮、世界遺產、慶典，以及旅遊建議與從台灣怎麼去。"
                   u"另有行政區制度、地形氣候、地名的念法、各地比較與世界遺產總表、美食地圖和韓國與台灣，附互動地圖、找地測驗與速查表。",
}

MODULES = [krp_a.MODULE_A] + krp_data.MODULES + [krp_a.MODULE_H]

REFERENCES = krp_ref.REFERENCES
