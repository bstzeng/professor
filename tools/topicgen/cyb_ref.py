# -*- coding: utf-8 -*-
"""資安事件全紀錄：參考頁。"""
from nv_common import LS, NVLIB
import cyb_common as C

_G = dict((g[0], g[1]) for g in C.GROUPS)
TABLE = {"file": "table.html", "title": u"事件總表", "h1": u"資安事件總表", "icon": u"📋", "description": u"依年份排列的事件與一句話摘要",
  "body": [("t", [u"年份", u"事件", u"類別", u"一句話", u"課"], [[c[0], c[1], _G[c[2]], c[3], LS(c[4])] for c in C._sorted]),
           ("p", u"國家級攻擊的歸因，均為各國政府或資安公司的判斷，被指控的一方多半否認。")]}
GUIDE = {"file": "guide.html", "title": u"互動圖鑑", "h1": u"資安事件互動圖鑑", "icon": u"🗺️", "description": u"年表、事件圖鑑、攻擊鏈與改進關係圖",
  "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 年表（第 2 課）"), C.TIMELINE, ("h", u"2. 事件圖鑑"), C.CARDS,
           ("h", u"3. 勒索軟體攻擊鏈（第 1 課）"), C.SEQ_CHAIN, ("h", u"4. 改進關係圖（第 32 課）"), C.GRAPH]}
REFERENCES = [TABLE, GUIDE]
