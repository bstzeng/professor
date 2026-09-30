# -*- coding: utf-8 -*-
"""疾病形成機制：共用工具。沿用 ho_common 的 lesson() 與 SVG 小工具，
另外提供跨主題連結、就醫警訊 callout，以及「器官 × 疾病 × 機制」地圖。"""
from ho_common import *

PURPLE = "#9c89d6"

# 致病機制標籤 → 顏色；第二部的疾病地圖與表格都用這組分類
MECH = {
    u"感染": GREEN,
    u"發炎／免疫": RED,
    u"血流障礙": BLUE,
    u"代謝": GOLD,
    u"退化": PURPLE,
    u"腫瘤": ACC,
    u"遺傳": ORANGE,
    u"結構／阻塞": MUTED,
    u"功能失調": "#5fa8a8",
}


def ORG(n, text=None):
    """連到《人體器官運作機制》的某一課。"""
    return u'<a href="../human-organs/lesson-%02d.html">%s</a>' % (
        n, text or u"《人體器官運作機制》第 %d 課" % n)


def LS(n, text=None):
    """連到本主題的某一課。"""
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


def warn(items):
    return ("note", u"⚠️ 需要就醫的警訊", [("ul", items)])


def dmap(heading, center, items):
    """器官疾病地圖：中央是器官，左右各最多 4 個疾病，框線顏色代表主要機制。
    items = [(疾病名, 機制標籤), ...]，最多 8 個。"""
    out = [title(heading)]
    out.append(box(250, 110, 140, 56, center, None, TXT, 13, fill="var(--accent-soft)"))
    left, right = items[:(len(items) + 1) // 2], items[(len(items) + 1) // 2:]
    for side, group in ((0, left), (1, right)):
        n = len(group)
        for i, (name, tag) in enumerate(group):
            y = 40 + i * (190.0 / max(n, 1)) + (190.0 / max(n, 1) - 40) / 2
            x = 20 if side == 0 else 440
            c = MECH[tag]
            out.append(box(x, y, 180, 40, name, tag, c, 10.5, 8.5))
            if side == 0:
                out.append(P("M200 %g L250 138" % (y + 20), LINE))
            else:
                out.append(P("M440 %g L390 138" % (y + 20), LINE))
    used = []
    for _, tag in items:
        if tag not in used:
            used.append(tag)
    step = 600.0 / len(used)
    for i, tag in enumerate(used):
        cx = 20 + step * i + step / 2
        out.append(R(cx - 40, 252, 12, 12, MECH[tag], MECH[tag], 3, op=0.35))
        out.append(T(cx - 24, 262, tag, 9, MUTED, "start"))
    return svg(*out)


def mtable(rows):
    """疾病 × 機制表：rows = [(疾病, 機制標籤字串, 相關課程 HTML), ...]"""
    return ("t", [u"疾病", u"主要機制", u"機制回顧"], [list(r) for r in rows])
