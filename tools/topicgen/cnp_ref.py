# -*- coding: utf-8 -*-
"""中國各省：參考頁——互動地圖、省級行政區速查表。"""
from cnp_common import *
import cnp_a   # noqa: F401  確保 DATA 已載入

GUIDE = {
    "file": "guide.html", "title": u"中國各省互動地圖", "h1": u"中國各省互動地圖", "icon": u"🗺️",
    "description": u"點選查詢、找省測驗、排行比較",
    "body": [
        ("raw", u"<script>%s</script>" % CPLIB),
        ("h", u"1. 點選查詢"), cpw({"t": "explore", "q": u"點任何一個省區看基本資料，並可直接跳到該省的課程。"}),
        ("h", u"2. 找省測驗"), cpw({"t": "quiz", "q": u"依照題目在地圖上點出那個省區。可以選全部或只考某個分區。"}),
        ("h", u"3. 排行比較"), cpw({"t": "rank", "q": u"依人口、面積或人口密度排序。"}),
    ],
}


def _rows():
    rows = []
    for c in ORDER:
        b = BASIC[c]
        d = DATA[c]
        rows.append([LS(LESSON[c], b[0]), b[1], b[4], REGIONS[b[3]][0], wan(b[7]).replace(u"約 ", u""),
                     (u"%s 萬 km²" % b[6]) if b[6] >= 0.1 else u"約 33 km²", d["season"].split(u"；")[0].split(u"。")[0], d["days"].split(u"（")[0]])
    return rows


TABLE = {
    "file": "provinces.html", "title": u"省級行政區速查表", "h1": u"省級行政區速查表", "icon": u"📋",
    "description": u"33 個省區的簡稱、省會、分區、人口、面積、最佳季節與建議天數",
    "body": [
        ("p", u"人口為 2020 年第七次全國人口普查數字（香港、澳門為同年官方數字）。點省區名稱可以跳到該省的課程。"),
        ("t", [u"省區", u"簡稱", u"省會", u"分區", u"人口", u"面積", u"最佳季節", u"建議天數"], _rows()),
        ("h", u"容易搞錯的省會"),
        ("p", u"河北的省會是石家莊（不是保定）、吉林的省會是長春（不是吉林市）、山東是濟南（不是青島）、福建是福州（不是廈門）、"
              u"江蘇是南京（不是蘇州）、內蒙古是呼和浩特（不是包頭）、廣西是南寧（不是桂林）、海南是海口（不是三亞）。"),
    ],
}

REFERENCES = [GUIDE, TABLE]
