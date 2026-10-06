# -*- coding: utf-8 -*-
"""韓國各市道：參考頁——互動地圖、17 市道速查表。"""
from krp_common import *
import krp_a   # noqa: F401  確保 DATA 已載入

GUIDE = {
    "file": "guide.html", "title": u"韓國各市道互動地圖", "h1": u"韓國各市道互動地圖", "icon": u"🗺️",
    "description": u"點選查詢、找地測驗、排行比較",
    "body": [
        ("raw", u"<script>%s</script>" % KRLIB),
        ("h", u"1. 點選查詢"), krw({"t": "explore", "q": u"點任何一個市道看基本資料，並可直接跳到該地的課程。"}),
        ("h", u"2. 找地測驗"), krw({"t": "quiz", "q": u"依照題目在地圖上點出那個市道。可以選全部或只考某個地區。"}),
        ("h", u"3. 排行比較"), krw({"t": "rank", "q": u"依人口、面積或人口密度排序。"}),
    ],
}


def _rows():
    return [[LS(LESSON[c], BASIC[c][0]), BASIC[c][1], BASIC[c][3], REGIONS[BASIC[c][4]][0], BASIC[c][5], wan(BASIC[c][8]).replace(u"約 ", u""),
             format(BASIC[c][7], ","), DATA[c]["season"].split(u"；")[0].split(u"。")[0]] for c in ORDER]


TABLE = {
    "file": "regions.html", "title": u"17 市道速查表", "h1": u"17 市道速查表", "icon": u"📋",
    "description": u"韓文、類型、地區、廳舍所在地、人口、面積與推薦季節",
    "body": [
        ("p", u"人口為 2024 年前後的住民登錄人口約略值，面積單位為平方公里。點名稱可以跳到該市道的課程。"),
        ("t", [u"市道", u"韓文", u"類型", u"地區", u"廳舍所在地", u"人口", u"面積", u"推薦季節"], _rows()),
    ],
}

REFERENCES = [GUIDE, TABLE]
