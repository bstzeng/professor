# -*- coding: utf-8 -*-
"""國債課程:共用工具。

lesson() 每課結尾自動補上「想一想」callout 與一行「數字會變動」提醒。
沿用檔案格式課的 SVG／圖表小工具(line_chart、bars、box、flow、layout…)。
"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, layout, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)

NOTE = (u"本課用來理解<strong>機制與概念</strong>,呈現不同觀點,不偏袒任何政黨或立場;"
        u"文中的金額、比率是<strong>概略值</strong>,實際數字每天變動,請以官方最新資料(如美國財政部)為準。")


def lesson(title_, desc, goals, body, think, check, fig=None, nxt=None):
    blocks = []
    for b in body:
        if b == "FIG":
            blocks.append(("fig", fig[0], fig[1], fig[2]))
        elif isinstance(b, tuple) and b[0] == "FIGX":
            blocks.append(("fig", b[1], b[2], b[3]))
        else:
            blocks.append(b)
    blocks.append(("note", u"想一想", [("p", think)]))
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">📊 %s</p>' % NOTE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)
