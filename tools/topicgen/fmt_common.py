# -*- coding: utf-8 -*-
"""檔案格式解剖學：共用的課程包裝與「十六進位解剖圖」工具。

- lesson()：每課結尾自動補上「動手試試」callout
- hexdump()：把一串位元組畫成 Hex 檢視器的樣子，並依區段上色、加圖例
- vlq()：MIDI 等格式使用的可變長度數量編碼
"""
from gen import Lesson
from ho_common import (T, R, C, E, P, A, box, flow, title,
                       RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT)
from hr_common import svg, bars, PURPLE, TEAL, GRAY


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


def hexbytes(data):
    return u" ".join(u"%02X" % b for b in data)


def vlq(n):
    """可變長度數量：每個位元組放 7 位元，最高位元 1 表示「後面還有」。"""
    out = [n & 0x7F]
    n >>= 7
    while n:
        out.insert(0, (n & 0x7F) | 0x80)
        n >>= 7
    return bytes(out)


def hexdump(data, regions, y0=34, cell=27, legend_cols=3, heading=None):
    """regions = [(起點, 終點（不含）, 顏色, 圖例文字)]。回傳 (svg 內容, 總高度)。"""
    out = []
    if heading:
        out.append(title(heading))
    x0 = 70
    rows = (len(data) + 15) // 16
    out.append(T(x0 - 12, y0 + 2, u"位移", 8.5, MUTED, "end"))
    for i in range(16):
        out.append(T(x0 + i * cell + cell / 2.0, y0 + 2, u"%X" % i, 8.5, MUTED))
    out.append(T(x0 + 16 * cell + 60, y0 + 2, u"ASCII", 8.5, MUTED))

    def color(k):
        for a, b, c, lab in regions:
            if a <= k < b:
                return c
        return None

    for r in range(rows):
        yy = y0 + 10 + r * 26
        out.append(T(x0 - 12, yy + 16, u"%04X" % (r * 16), 9, MUTED, "end"))
        asc = []
        for i in range(16):
            k = r * 16 + i
            if k >= len(data):
                break
            c = color(k)
            if c:
                out.append(R(x0 + i * cell + 1, yy + 1, cell - 2, 22, c, c, 3, 1, op=0.28))
            out.append('<text x="%g" y="%g" text-anchor="middle" font-size="10" fill="var(--text)" '
                       'font-family="ui-monospace,Menlo,Consolas,monospace">%02X</text>' % (
                           x0 + i * cell + cell / 2.0, yy + 16, data[k]))
            ch = data[k]
            asc.append(chr(ch) if 32 <= ch < 127 else u"·")
        s = u"".join(asc).replace(u"&", u"&amp;").replace(u"<", u"&lt;").replace(u">", u"&gt;")
        out.append('<text x="%g" y="%g" font-size="10" fill="var(--text-muted)" '
                   'font-family="ui-monospace,Menlo,Consolas,monospace">%s</text>' % (
                       x0 + 16 * cell + 14, yy + 16, s))
    ly = y0 + 10 + rows * 26 + 14
    colw = 600.0 / legend_cols
    for j, (a, b, c, lab) in enumerate(regions):
        cx = 24 + (j % legend_cols) * colw
        cy = ly + (j // legend_cols) * 20
        out.append(R(cx, cy, 12, 12, c, c, 2, 1, op=0.5))
        out.append(T(cx + 18, cy + 10, lab, 9.5, TXT, "start"))
    h = ly + ((len(regions) + legend_cols - 1) // legend_cols) * 20 + 6
    return out, h
