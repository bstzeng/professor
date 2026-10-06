# -*- coding: utf-8 -*-
"""日本都道府縣：參考頁——互動地圖、47 都道府縣速查表。"""
from jpp_common import *
import jpp_a   # noqa: F401  確保 DATA 已載入

GUIDE = {
    "file": "guide.html", "title": u"日本都道府縣互動地圖", "h1": u"日本都道府縣互動地圖", "icon": u"🗾",
    "description": u"點選查詢、找縣測驗、排行比較",
    "body": [
        ("raw", u"<script>%s</script>" % JPLIB),
        ("h", u"1. 點選查詢"), jpw({"t": "explore", "q": u"點任何一個都道府縣看基本資料，並可直接跳到該縣的課程。"}),
        ("h", u"2. 找縣測驗"), jpw({"t": "quiz", "q": u"依照題目在地圖上點出那個都道府縣。可以選全部或只考某個地方。"}),
        ("h", u"3. 排行比較"), jpw({"t": "rank", "q": u"依人口、面積或人口密度排序。"}),
    ],
}


def _rows():
    rows = []
    for c in ORDER:
        b = BASIC[c]
        d = DATA[c]
        rows.append([LS(LESSON[c], b[0]), b[1], REGIONS[b[3]][0], b[4], wan(b[7]).replace(u"約 ", u""), format(b[6], ","), b[8],
                     d["season"].split(u"、")[0].split(u"；")[0]])
    return rows


TABLE = {
    "file": "prefectures.html", "title": u"47 都道府縣速查表", "h1": u"47 都道府縣速查表", "icon": u"📋",
    "description": u"讀音、地方、廳所在地、人口、面積、舊國名與推薦季節",
    "body": [
        ("p", u"人口為 2020 年國勢調查數字，面積單位為平方公里。點名稱可以跳到該都道府縣的課程。"),
        ("t", [u"都道府縣", u"讀音", u"地方", u"廳所在地", u"人口", u"面積", u"舊國名", u"推薦季節"], _rows()),
        ("h", u"廳所在地不是縣名的地方"),
        ("p", u"岩手（盛岡）、宮城（仙台）、茨城（水戶）、栃木（宇都宮）、群馬（前橋）、神奈川（橫濱）、山梨（甲府）、石川（金澤）、愛知（名古屋）、"
              u"三重（津）、滋賀（大津）、兵庫（神戶）、島根（松江）、香川（高松）、愛媛（松山）、沖繩（那霸），以及北海道（札幌）、東京都（新宿區）。"),
    ],
}

REFERENCES = [GUIDE, TABLE]
