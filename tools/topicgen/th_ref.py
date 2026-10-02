# -*- coding: utf-8 -*-
"""人類科技發展史：參考頁——總時間軸、速查表。"""
from th_common import LS, THLIB, widget, timeline, deps, EVENTS
from th_f import _ERA

def _cat(c):
    return {"t": u"工具材料", "f": u"食物農業", "i": u"資訊通訊", "e": u"能源動力", "m": u"運輸", "s": u"科學醫學", "c": u"計算"}[c]

TIMELINE = {
    "file": "timeline.html", "title": u"科技總時間軸", "h1": u"人類科技總時間軸", "icon": u"⏳",
    "description": u"可縮放的互動時間軸、前置技術關係圖與時代比較表",
    "body": [
        ("raw", u"<script>%s</script>" % THLIB),
        ("h", u"1. 互動時間軸"),
        timeline("log", u"切換尺度：對數尺度能同時看見三百萬年與最近十年；等比例尺度則顯示發明如何越來越密集。"),
        ("h", u"2. 前置技術關係圖"),
        deps("phone", u"選一項現代發明，看它背後的技術系譜。", ["phone", "llm", "gps", "plane", "comp", "rail", "print"]),
        ("h", u"3. 時代比較表"),
        ("t", [u"時代", u"能源", u"材料", u"運輸", u"資訊"], _ERA),
    ],
}

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"科技史速查表", "h1": u"人類科技發展史：速查表", "icon": u"🗂️",
    "description": u"重要發明的年代、地點與課程，一頁查完",
    "body": [
        ("p", u"年代多為大約值；考古與文獻的新發現可能改變這些數字。"),
        ("t", [u"年代", u"發明或事件", u"類別", u"課"], [[e[1], e[2], _cat(e[4]), LS(e[3])] for e in EVENTS]),
    ],
}

REFERENCES = [TIMELINE, CHEATSHEET]
