# -*- coding: utf-8 -*-
"""晶片 layout 設計：共用工具。

沿用 ho_common 的 SVG 小工具（T、R、P、A、box、flow、svg、title 與顏色），
另外提供：每課的「產業現場」callout 包裝、跨主題連結，
以及畫 layout 俯視圖用的各層顏色與小工具。
"""
from gen import Lesson
from ho_common import (T, R, C, E, P, A, box, flow, svg, title,
                       RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT)

PURPLE = "#9c89d6"
TEAL = "#5fa8a8"


def lesson(title_, desc, goals, body, field, check, fig=None, nxt=None):
    """body 中的 "FIG" 會被換成 fig=(svg, viewBox, 圖說)；最後自動補上「產業現場」callout。"""
    blocks = []
    for b in body:
        if b == "FIG":
            blocks.append(("fig", fig[0], fig[1], fig[2]))
        else:
            blocks.append(b)
    if fig and "FIG" not in body:
        blocks.insert(1, ("fig", fig[0], fig[1], fig[2]))
    blocks.append(("note", u"產業現場", [("p", field)]))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def EL(n, text=None):
    return u'<a href="../electronics/lesson-%02d.html">%s</a>' % (
        n, text or u"《電子電路完整課程》第 %d 課" % n)


def CS(n, text=None):
    return u'<a href="../computer-science/lesson-%02d.html">%s</a>' % (
        n, text or u"《計算機概論》第 %d 課" % n)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


# ---------- layout 各層（俯視圖用） ----------
# 顏色參考常見 layout 工具的慣例配色，用半透明讓重疊處看得出來
LAYER = {
    "nwell":   ("#c9b458", 0.18, u"N-well"),
    "active":  (GREEN, 0.45, u"Active（擴散區）"),
    "poly":    (RED, 0.55, u"Poly（閘極）"),
    "contact": ("#333333", 0.9, u"Contact"),
    "m1":      (BLUE, 0.40, u"Metal 1"),
    "via":     ("#333333", 0.9, u"Via"),
    "m2":      (PURPLE, 0.40, u"Metal 2"),
    "nplus":   (ORANGE, 0.10, u"N+ 植入"),
    "pplus":   (TEAL, 0.10, u"P+ 植入"),
}


def lyr(kind, x, y, w, h):
    c, op, _ = LAYER[kind]
    if kind in ("contact", "via"):
        return R(x, y, w, h, c, c, 1, 1, op=op)
    return R(x, y, w, h, c, c, 2, 1.2, op=op)


def legend(kinds, y, x0=20, x1=620):
    step = (x1 - x0) / float(len(kinds))
    out = []
    for i, k in enumerate(kinds):
        cx = x0 + step * i + 8
        out.append(lyr(k, cx, y - 9, 12, 12))
        out.append(T(cx + 18, y + 1, LAYER[k][2], 9, MUTED, "start"))
    return "".join(out)
