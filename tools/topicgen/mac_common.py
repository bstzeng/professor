# -*- coding: utf-8 -*-
"""macOS 使用邏輯課程：共用工具。

lesson() 每課結尾自動補上「動手試試」callout。
沿用檔案格式課的 SVG 小工具，另加幾個 UI 風格的零件（鍵帽、視窗、選單列）。
"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, layout, mono, bars,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)


def lesson(title_, desc, goals, body, tryit, check, fig=None, nxt=None):
    blocks = []
    for b in body:
        if b == "FIG":
            blocks.append(("fig", fig[0], fig[1], fig[2]))
        elif isinstance(b, tuple) and b[0] == "FIGX":
            blocks.append(("fig", b[1], b[2], b[3]))
        else:
            blocks.append(b)
    blocks.append(("note", u"動手試試", [("p", tryit)]))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


def FMT(n, text):
    """連到《檔案格式解剖學》。"""
    return u'<a href="../file-formats/lesson-%02d.html">%s</a>' % (n, text)


# ---------- UI 風格 SVG 零件 ----------

def key(x, y, label, w=44, h=40, color=ACC, size=13, sub=None):
    """畫一個鍵帽。"""
    out = [R(x, y, w, h, color, "var(--surface)", 8, 1.6)]
    if sub:
        out.append(T(x + w / 2.0, y + h / 2.0 - 2, label, size, color))
        out.append(T(x + w / 2.0, y + h / 2.0 + 12, sub, 8, MUTED))
    else:
        out.append(T(x + w / 2.0, y + h / 2.0 + size * 0.35, label, size, color))
    return out


def keys(x, y, seq, gap=8, plus=True):
    """一排鍵帽，中間用 + 連接。seq = [(label, width, color, sub), ...] 或 [(label,)]。"""
    out = []
    cx = x
    for i, item in enumerate(seq):
        label = item[0]
        w = item[1] if len(item) > 1 else 44
        color = item[2] if len(item) > 2 else ACC
        sub = item[3] if len(item) > 3 else None
        out.extend(key(cx, y, label, w, 40, color, 13, sub))
        cx += w
        if plus and i < len(seq) - 1:
            out.append(T(cx + gap / 2.0, y + 24, u"+", 14, MUTED))
            cx += gap + 12
        else:
            cx += gap
    return out


def window(x, y, w, h, titlebtns=True, titletext=u"", accent=LINE):
    """畫一個 macOS 風格的視窗（含左上角三個燈）。"""
    out = [R(x, y, w, h, accent, "var(--surface)", 10, 1.5)]
    out.append(P("M%g %g h%g" % (x, y + 26, w), LINE, sw=1))
    if titlebtns:
        out.append(C(x + 16, y + 13, 5, "#e0605a", "#e0605a", 0))
        out.append(C(x + 32, y + 13, 5, "#e0c15a", "#e0c15a", 0))
        out.append(C(x + 48, y + 13, 5, "#5aa469", "#5aa469", 0))
    if titletext:
        out.append(T(x + w / 2.0, y + 17, titletext, 9.5, MUTED))
    return out


def menubar(x, y, w, items):
    """螢幕最上方的選單列。"""
    out = [R(x, y, w, 22, LINE, "var(--accent-soft)", 5, 1)]
    out.append(T(x + 14, y + 15, u"", 11, TXT, "start"))
    cx = x + 16
    out.append(C(x + 14, y + 11, 5, ACC, ACC, 0))    # apple 位置示意
    cx = x + 30
    for it in items:
        out.append(T(cx, y + 15, it, 9.5, TXT, "start"))
        cx += len(it) * 12 + 16
    return out
