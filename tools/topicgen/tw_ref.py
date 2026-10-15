# -*- coding: utf-8 -*-
"""認識台灣的樹：參考頁——工具箱與樹種速查。"""
from tw_common import *
import tw_a, tw_e

GUIDE = {
    "file": "guide.html", "title": u"認樹工具箱", "h1": u"認樹工具箱", "icon": u"🧰",
    "description": u"認樹檢索表、開花月曆與葉的示意圖",
    "body": [
        ("raw", u"<script>%s</script><script>%s</script>" % (KDLIB, TWLIB)),
        ("h", u"1. 認樹檢索表（第 49 課）"), KEY,
        ("h", u"2. 開花與賞葉月曆（第 30 課）"), CALW(4),
        ("h", u"3. 葉序（第 2 課）"), fig_arrange(),
        ("h", u"4. 單葉與複葉（第 2 課）"), fig_compound(),
        ("h", u"5. 葉形與葉緣（第 3 課）"), fig_shape(), fig_margin(),
        ("h", u"6. 台灣的森林帶（第 37 課）"), fig_forest(),
    ],
}

_rows = []
_LES = {"rong": 7, "zhang": 8, "jiadong": 9, "luan": 10, "heiban": 11, "dalan": 12, "xiaolan": 12, "zitan": 13, "shuihuang": 13, "puti": 14, "guangla": 15, "fengxiang": 16,
        "kulian": 17, "querong": 18, "shanying": 19, "mumian": 20, "yanzijing": 21, "liusu": 22, "youtong": 23, "abole": 24, "fenghuang": 25, "daziwei": 26, "jiuqiong": 26,
        "meiren": 27, "huangjin": 28, "haimeng": 28, "pingpo": 29, "mumahuang": 31, "lintou": 31, "qipan": 31, "fumu": 32, "dawang": 33, "pukui": 33, "xiangsi": 34,
        "goushu": 35, "xuetong": 35, "mangguo": 36, "hongkuai": 38, "bianbai": 38, "taiwanshan": 39, "xiaonan": 40, "ersong": 42, "ju": 43, "yinhehuan": 46, "baiqian": 46}
for k, n in _LES.items():
    zh, sci, org, _ = SP[k]
    _rows.append([zh, u"<i>%s</i>" % sci, org, LS(n)])

GLOSSARY = {
    "file": "glossary.html", "title": u"樹種與名詞速查", "h1": u"樹種與名詞速查", "icon": u"📖",
    "description": u"本課程樹種的學名、來源，以及認樹的常用名詞",
    "body": [
        ("h", u"樹種一覽"),
        ("t", [u"樹種", u"學名", u"來源", u"課"], _rows),
        ("h", u"名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"互生、對生、輪生", u"每節一片、兩片相對、三片以上", LS(2)], [u"單葉、複葉", u"一個葉柄一片葉；一個葉柄多片小葉", LS(2)], [u"三出脈", u"葉基附近分出三條主脈（樟樹）", LS(3)],
          [u"滴水葉尖", u"延長的葉尖，使雨水快速流走（菩提樹）", LS(3)], [u"盾狀葉", u"葉柄長在葉片中間（血桐）", LS(3)], [u"假葉", u"扁平化的葉柄（相思樹）", LS(3)],
          [u"隱頭花序、隱花果", u"花藏在囊狀花托內（榕屬）", LS(4)], [u"原生種、特有種", u"本來就在台灣；只分布在台灣", LS(5)], [u"外來種、入侵種", u"人為引進；大量擴散危害生態", LS(5)],
          [u"先驅樹、演替", u"最早長進空地的樹；森林組成隨時間改變", LS(35)], [u"雲霧帶", u"中海拔常有雲霧的山區，檜木生長處", LS(37)], [u"台灣五木", u"紅檜、扁柏、台灣杉、肖楠、香杉", LS(41)],
          [u"受保護樹木", u"依《森林法》樹木保護專章公告的樹", LS(44)], [u"學名、二名法", u"屬名＋種小名的拉丁文名稱", LS(47)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
