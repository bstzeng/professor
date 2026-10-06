# -*- coding: utf-8 -*-
"""美國五十州：參考頁——互動地圖、五十州速查表、州旗一覽。"""
from ust_common import *
from ust_flags import flag

GUIDE = {
    "file": "guide.html", "title": u"美國五十州互動地圖", "h1": u"美國五十州互動地圖", "icon": u"🗺️",
    "description": u"點選查詢、找州測驗、加入順序動畫、排行比較",
    "body": [
        ("raw", u"<script>%s</script>" % STLIB),
        ("h", u"1. 點選查詢"), stw({"t": "explore", "q": u"點任何一州看基本資料，並可直接跳到該州的課程。"}),
        ("h", u"2. 找州測驗"), stw({"t": "quiz", "q": u"依照題目在地圖上點出那個州。可以選全部或只考某個區域。"}),
        ("h", u"3. 加入聯邦的順序"), stw({"t": "join", "q": u"按「播放」看 1787～1959 年各州依序加入。"}),
        ("h", u"4. 排行比較"), stw({"t": "rank", "q": u"依人口、面積或人口密度排序。"}),
    ],
}


def _rows():
    rows = []
    for c in ORDER:
        b = BASIC[c]
        rows.append([LS(LESSON[c], b[0]), c, REGIONS[b[2]][0], b[3], b[5], wan(b[6]).replace(u"約 ", u""), u"%d（%d）" % (b[8], b[9]), b[10]])
    return rows


TABLE = {
    "file": "states.html", "title": u"五十州速查表", "h1": u"五十州速查表", "icon": u"📋",
    "description": u"五十州的縮寫、區域、首府、最大城市、人口、加入年份與綽號",
    "body": [
        ("p", u"人口為 2020 年人口普查數字；「加入」欄括號內是第幾個加入的州。點州名可以跳到該州的課程。"),
        ("t", [u"州", u"縮寫", u"區域", u"首府", u"最大城市", u"人口", u"加入", u"綽號"], _rows()),
        ("h", u"首府不是最大城市的常見例子"),
        ("p", u"紐約州的首府是奧爾巴尼（不是紐約市）、加州是沙加緬度（不是洛杉磯）、德州是奧斯汀（不是休士頓）、佛羅里達是塔拉哈西（不是邁阿密）、"
              u"伊利諾是春田（不是芝加哥）、賓州是哈里斯堡（不是費城）、華盛頓州是奧林匹亞（不是西雅圖）、內華達是卡森市（不是拉斯維加斯）。"),
    ],
}


def _flag_grid():
    cells = []
    for c in sorted(ORDER, key=lambda k: BASIC[k][1]):
        s, w, h = flag(c)
        cells.append(u'<a href="lesson-%02d.html" style="text-decoration:none;color:inherit;text-align:center;font-size:0.85em">'
                     u'<svg viewBox="0 0 %d %d" style="width:100%%;display:block" xmlns="http://www.w3.org/2000/svg">%s</svg>%s</a>'
                     % (LESSON[c], w, h, s, BASIC[c][0]))
    return (u'<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:14px 12px">%s</div>' % "".join(cells))


FLAGS_PAGE = {
    "file": "flags.html", "title": u"五十州州旗一覽", "h1": u"五十州州旗一覽", "icon": u"🚩",
    "description": u"依英文州名排列的五十面州旗（簡化示意圖）",
    "body": [
        ("p", u"以下是簡化的示意圖。圖案簡單的州旗照實畫出；中央是複雜州徽的州旗，只畫出底色和構圖。點州旗可以跳到該州的課程，看州旗的詳細說明。"),
        ("raw", _flag_grid()),
        ("h", u"州旗的幾種類型"),
        ("ul", [u"<strong>藍底配州徽</strong>：最常見，約有二十個州，常被批評「看起來都一樣」。",
                u"<strong>簡潔的幾何設計</strong>：德州、阿拉斯加、科羅拉多、新墨西哥、亞利桑那，常被評為最好看的州旗。",
                u"<strong>近年換新旗</strong>：密西西比（2021）、明尼蘇達（2024）、猶他（2024）。",
                u"<strong>獨一無二</strong>：俄亥俄是燕尾形；奧勒岡正反面不同；華盛頓州是綠底且有總統肖像；夏威夷含有英國國旗。"]),
    ],
}

REFERENCES = [GUIDE, TABLE, FLAGS_PAGE]
