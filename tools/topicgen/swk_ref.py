# -*- coding: utf-8 -*-
"""船難全紀錄：參考頁。"""
from nv_common import LS, NVLIB
import swk_common as C

_G = dict((g[0], g[1]) for g in C.GROUPS)
TABLE = {"file": "table.html", "title": u"船難總表", "h1": u"船難總表", "icon": u"📋", "description": u"依年份排列的船難與一句話摘要",
  "body": [("t", [u"年份", u"船難", u"類別", u"一句話", u"課"], [[c[0], c[1], _G[c[2]], c[3], LS(c[4])] for c in C._sorted]),
           ("p", u"罹難人數多為估計值，不同來源可能不同；詳見各課。")]}
TERMS = {"file": "terms.html", "title": u"海事名詞", "h1": u"海事名詞對照", "icon": u"📚", "description": u"本課程常見的海事名詞",
  "body": [("t", [u"中文", u"英文", u"說明"], [
    [u"國際海事組織", u"IMO", u"聯合國負責海事的專門機構"], [u"海上人命安全公約", u"SOLAS", u"船舶安全的基本國際公約"], [u"國際海上避碰規則", u"COLREG", u"船舶之間如何避讓"],
    [u"防止船舶汙染公約", u"MARPOL", u"油汙與廢棄物的規範"], [u"國際安全管理章程", u"ISM Code", u"航運公司的安全管理系統"], [u"船員訓練與當值公約", u"STCW", u"船員訓練與發證"],
    [u"滾裝船", u"Ro-Ro", u"車輛直接開上開下的船"], [u"穩心高度差", u"GM", u"穩心高於重心的距離"], [u"自由液面效應", u"Free surface effect", u"船內流動的液體降低穩定性"],
    [u"壓艙水", u"Ballast water", u"放在船底以調整重心與吃水的水"], [u"權宜船", u"Flag of convenience", u"在規定寬鬆的國家登記的船"], [u"港口國管制", u"Port State Control", u"港口國對外國船舶的檢查"]])]}
GUIDE = {"file": "guide.html", "title": u"互動圖鑑", "h1": u"船難互動圖鑑", "icon": u"🗺️", "description": u"年表、船難圖鑑、穩定性模擬與改進關係圖",
  "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 年表（第 2 課）"), C.TIMELINE, ("h", u"2. 船難圖鑑"), C.CARDS,
           ("h", u"3. 穩定性模擬（第 1 課）"), C.STAB, ("h", u"4. 改進關係圖（第 28 課）"), C.GRAPH]}
REFERENCES = [TABLE, TERMS, GUIDE]
