# -*- coding: utf-8 -*-
"""歐洲各國：參考頁——互動地圖、47 國速查表、國旗一覽。"""
from eup_common import *
import eup_a   # noqa: F401  確保 DATA 已載入
from eup_a import flag_grid

ALL = ORDER + MICRO

GUIDE = {
    "file": "guide.html", "title": u"歐洲各國互動地圖", "h1": u"歐洲各國互動地圖", "icon": u"🗺️",
    "description": u"點選查詢、找國家測驗、排行比較",
    "body": [
        ("raw", u"<script>%s</script>" % EULIB),
        ("h", u"1. 點選查詢"), euw({"t": "explore", "q": u"點任何一個國家看基本資料，並可直接跳到該國的課程。"}),
        ("h", u"2. 找國家測驗"), euw({"t": "quiz", "q": u"依照題目在地圖上點出那個國家。可以選全部或只考某個地區。"}),
        ("h", u"3. 排行比較"), euw({"t": "rank", "q": u"依人口、面積或人口密度排序。"}),
        ("p", u"梵蒂岡、聖馬利諾、摩納哥面積太小，地圖上無法點選，請見第 46 課。"),
    ],
}


def _rows():
    out = []
    for c in ALL:
        b = BASIC[c]
        tags = u"".join(t for t, v in ((u"盟", b[9]), (u"申", b[10]), (u"約", b[11])) if v) or u"—"
        out.append([LS(LESSON[c], b[0]), b[1], b[2], REGIONS[b[6]][0], wan(b[5]).replace(u"約 ", u""),
                    (u"%.2f" % b[4]) if b[4] < 1 else format(int(b[4]), ","), b[8], tags])
    return out


TABLE = {
    "file": "countries.html", "title": u"47 國速查表", "h1": u"47 國速查表", "icon": u"📋",
    "description": u"當地名稱、首都、地區、人口、面積、貨幣與歐盟／申根／北約",
    "body": [
        ("p", u"人口為 2024 年前後的約略值，面積單位為平方公里（俄羅斯、土耳其為全國數字）。最後一欄：盟＝歐盟、申＝申根區、約＝北約。點名稱可以跳到該國的課程。"),
        ("t", [u"國家", u"當地名稱", u"首都", u"地區", u"人口", u"面積", u"貨幣", u"組織"], _rows()),
    ],
}

FLAGS = {
    "file": "flags.html", "title": u"歐洲國旗一覽", "h1": u"歐洲國旗一覽", "icon": u"🏳️",
    "description": u"47 國國旗，依地區排列",
    "body": [("p", u"點國名可以跳到該國的課程。有國徽的國旗，國徽部分為簡化示意。")] +
            [b for k, v in REGIONS.items() for b in (("h", v[0]), flag_grid([c for c in ALL if BASIC[c][6] == k], 96))],
}

REFERENCES = [GUIDE, TABLE, FLAGS]
