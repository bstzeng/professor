# -*- coding: utf-8 -*-
"""星艦迷航記：參考頁——作品一覽、互動圖鑑。"""
from nv_common import LS, NVLIB
import stk_common as C

WORKS_PAGE = {
    "file": "works.html", "title": u"作品一覽", "h1": u"星艦迷航記作品一覽", "icon": u"🎬",
    "description": u"影集與電影的年份、主角與特色",
    "body": [
        ("t", [u"作品", u"年份", u"主角", u"課"], [
            [u"原初系列（The Original Series）", u"1966～1969", u"寇克", LS(5)], [u"動畫系列", u"1973～1974", u"寇克", LS(5)], [u"原班人馬電影（六部）", u"1979～1991", u"寇克", LS(6)],
            [u"銀河飛龍（The Next Generation）", u"1987～1994", u"畢凱", LS(7)], [u"深太空九號（Deep Space Nine）", u"1993～1999", u"席斯可", LS(8)], [u"TNG 電影（四部）", u"1994～2002", u"畢凱", LS(7)],
            [u"重返地球（Voyager）", u"1995～2001", u"珍妮薇", LS(9)], [u"企業號（Enterprise）", u"2001～2005", u"亞契", LS(10)], [u"重啟電影（三部）", u"2009～2016", u"寇克（新）", LS(11)],
            [u"發現號（Discovery）", u"2017～2024", u"伯納姆", LS(12)], [u"畢凱（Picard）", u"2020～2023", u"畢凱", LS(12)], [u"下層艦員（Lower Decks）", u"2020～2024", u"馬里納等", LS(12)],
            [u"天才少年（Prodigy）", u"2021～2024", u"達爾等", LS(12)], [u"奇異新世界（Strange New Worlds）", u"2022～", u"派克", LS(12)], [u"星艦學院（Starfleet Academy）", u"2026～", u"學員們", LS(12)],
        ]),
        ("p", u"中文片名以台灣常見的譯名為主，部分作品沒有固定的中文譯名；年份與播出資訊以官方公告為準。"),
    ],
}

GUIDE = {
    "file": "guide.html", "title": u"星艦互動圖鑑", "h1": u"星艦迷航記互動圖鑑", "icon": u"🗺️",
    "description": u"作品年表、艦橋人物、種族、銀河地圖與曲速計算器",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 作品年表（第 1 課）"), C.WORKS,
        ("h", u"2. 兩代企業號的艦橋（第 5 課）"), C.CREW,
        ("h", u"3. 種族圖鑑（第 20 課）"), C.SPECIES,
        ("h", u"4. 銀河的四個象限（第 20 課）"), C.MAP,
        ("h", u"5. 曲速計算器（第 21 課）"), C.WARP,
    ],
}

REFERENCES = [WORKS_PAGE, GUIDE]
