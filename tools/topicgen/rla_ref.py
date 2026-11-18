# -*- coding: utf-8 -*-
"""鐵路事故全紀錄：參考頁。"""
from nv_common import LS, NVLIB
import rla_common as C

_G = dict((g[0], g[1]) for g in C.GROUPS)
TABLE = {"file": "table.html", "title": u"事故總表", "h1": u"鐵路事故總表", "icon": u"📋", "description": u"依年份排列的事故與一句話摘要",
  "body": [("t", [u"年份", u"事故", u"類別", u"一句話", u"課"], [[c[0], c[1], _G[c[2]], c[3], LS(c[4])] for c in C._sorted]),
           ("p", u"死傷人數與原因請見各課；調查尚未結案的事故，以各課開頭的「調查進度」為準。")]}
TERMS = {"file": "terms.html", "title": u"鐵路安全名詞", "h1": u"鐵路安全名詞對照", "icon": u"📚", "description": u"本課程常見的鐵路安全名詞",
  "body": [("t", [u"中文", u"英文", u"說明"], [
    [u"閉塞", u"Block", u"一個區間同時只允許一列車"], [u"連鎖", u"Interlocking", u"號誌與轉轍器之間的安全關聯"], [u"軌道電路", u"Track circuit", u"以電流偵測區間內是否有列車"],
    [u"自動停車裝置", u"ATS", u"闖越停止號誌時自動煞車"], [u"列車自動防護", u"ATP", u"持續監控速度，超速自動煞車"], [u"自動警告系統", u"AWS", u"英國的號誌警告系統"],
    [u"列車防護警告系統", u"TPWS", u"英國在紅燈前自動煞車的系統"], [u"歐洲列車控制系統", u"ETCS", u"歐洲標準化的列車控制"], [u"主動式列車控制", u"PTC", u"美國法定的列車控制系統"],
    [u"闖越號誌", u"SPAD", u"列車越過停止號誌"], [u"超高", u"Cant / Superelevation", u"彎道外軌比內軌高"], [u"轉轍器", u"Switch / Turnout", u"讓列車改變路線的道岔"],
    [u"故障導向安全", u"Fail-safe", u"故障時進入安全的狀態"], [u"熱軸偵測器", u"Hot box detector", u"偵測過熱的車輪軸承"]])]}
GUIDE = {"file": "guide.html", "title": u"互動圖鑑", "h1": u"鐵路事故互動圖鑑", "icon": u"🗺️", "description": u"年表、事故圖鑑、彎道超速計算器與改進關係圖",
  "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 年表（第 2 課）"), C.TIMELINE, ("h", u"2. 事故圖鑑"), C.CARDS,
           ("h", u"3. 彎道超速計算器（第 9 課）"), C.CURVE, ("h", u"4. 改進關係圖（第 34 課）"), C.GRAPH]}
REFERENCES = [TABLE, TERMS, GUIDE]
