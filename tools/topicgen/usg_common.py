# -*- coding: utf-8 -*-
"""〈美國政府怎麼運作〉（usg_）共用：課程包裝（不含互動工具）與「台灣怎麼做」小框。"""
from cc_common import make_lesson, LS, D, M, KATEX
F = D

USG_NOTE = (u"本課程介紹美國與台灣的政府制度與運作。對仍有爭議的議題，盡量並陳不同的觀點，不代表任何政治立場。"
            u"人事、席次與政策等現況資訊以文中標註的時間為準（本課程撰寫於 2026 年 11 月），之後可能已經改變；法條與數字請以官方最新資料為準。")

lesson = make_lesson(u"🦅", USG_NOTE, u"", u"usg-none")


def TW(*items):
    """每課結尾的「台灣怎麼做」：字串為段落，list 為條列。"""
    blocks = []
    for it in items:
        blocks.append(("ul", it) if isinstance(it, list) else ("p", it))
    return ("note", u"🇹🇼 台灣怎麼做", blocks)
