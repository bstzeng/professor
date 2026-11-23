# -*- coding: utf-8 -*-
import tib_a
from nv_common import NVLIB

ATLAS = {"file": "atlas.html", "title": u"泰伯倫圖鑑", "h1": u"泰伯倫系列圖鑑", "icon": u"📜",
         "description": u"時間軸與人物關係圖",
         "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 時間軸"), tib_a.STORY, ("h", u"2. 人物關係圖"), tib_a.PEOPLE]}

TOPIC = {
    "id": "tiberian-saga", "category": "games",
    "title": u"泰伯倫系列全劇情：從終極動員令到泰伯倫黃昏",
    "short": u"泰伯倫系列", "crumb": u"泰伯倫系列", "icon": u"☢️",
    "description": u"泰伯倫、GDI、Nod 兄弟會與凱恩；終極動員令的第一次泰伯倫戰爭、賽斯之死、離子炮與隱密行動的恐龍任務；叛逆者的哈沃克；泰伯倫之日的 2030 年、麥克尼爾與斯拉維克、被遺忘者與塔西佗斯；烈焰風暴的 CABAL；泰伯倫戰爭的藍黃紅區、離子炮悲劇與斯克林；凱恩之怒的 LEGION 與馬西昂；泰伯倫黃昏的控制網路與凱恩的飛昇；喬·庫坎與兩條世界線（含完整劇透）。附時間軸與人物關係圖。",
}
MODULES = tib_a.MODULES
REFERENCES = [ATLAS]
