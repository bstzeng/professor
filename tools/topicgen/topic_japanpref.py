# -*- coding: utf-8 -*-
"""日本 47 都道府縣主題的規格。"""
import jpp_a, jpp_n, jpp_k, jpp_c, jpp_kk, jpp_w, jpp_ky, jpp_ref

TOPIC = {
    "id": "japan-prefectures",
    "category": "geography",
    "title": u"日本 47 都道府縣：位置、美食、祭典與旅行",
    "short": u"日本都道府縣",
    "crumb": u"日本都道府縣",
    "icon": u"🗾",
    "description": u"一縣一課，依北海道、東北、關東、中部、近畿、中國、四國、九州・沖繩八大地方介紹 47 都道府縣：每課有位置地圖、一句話記憶、"
                   u"讀音與舊國名、主要城市、地理歷史、方言、美食與伴手禮、世界遺產、祭典、溫泉，以及旅遊建議與從台灣怎麼去。"
                   u"另有都道府縣制度、地形四季、舊國名、各縣比較、世界遺產總表、鄉土料理與「日本與台灣」，附互動地圖、找縣測驗與速查表。",
}

MODULES = ([jpp_a.MODULE_A] + jpp_n.MODULES + jpp_k.MODULES + jpp_c.MODULES + jpp_kk.MODULES + jpp_w.MODULES + jpp_ky.MODULES
           + [jpp_a.MODULE_J])

REFERENCES = jpp_ref.REFERENCES
