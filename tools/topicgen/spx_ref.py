# -*- coding: utf-8 -*-
"""太空事故全紀錄：參考頁。"""
from nv_common import LS, NVLIB
import spx_a as C

_G = dict((g[0], g[1]) for g in C.GROUPS)
TABLE = {"file": "table.html", "title": u"事故總表", "h1": u"太空事故總表", "icon": u"📋", "description": u"依年份排列的事故與一句話摘要",
  "body": [("t", [u"年份", u"事故", u"類別", u"一句話", u"課"], [[c[0], c[1], _G[c[2]], c[3], LS(c[4])] for c in C._sorted]),
           ("p", u"部分事故（如尼德林災難、長征三號乙）的死亡人數，官方公布與外界估計不同；本課程以常見的說法為準。")]}
GUIDE = {"file": "guide.html", "title": u"互動圖鑑", "h1": u"太空事故互動圖鑑", "icon": u"🗺️", "description": u"年表、事故圖鑑與改進關係圖",
  "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 年表（第 1 課）"), C.TIMELINE, ("h", u"2. 事故圖鑑（第 2 課）"), C.CARDS,
           ("h", u"3. 改進關係圖（第 26 課）"), C.GRAPH]}
REFERENCES = [TABLE, GUIDE]
