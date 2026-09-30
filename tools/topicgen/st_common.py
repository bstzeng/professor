# -*- coding: utf-8 -*-
"""股票的本質:共用工具。

lesson() 每課結尾自動補上「想一想」callout 與一行「投資教育、非投資建議」提醒。
沿用檔案格式課的 SVG／圖表小工具(line_chart、bars、box、flow、layout、mono…)。
"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, layout, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)

NOTE = (u"本課為<strong>投資教育,不是投資建議</strong>,不推薦任何個股或金融商品;"
        u"文中的報酬率、稅費與數字是<strong>概略值或歷史示意</strong>,過去績效不代表未來,"
        u"稅制與交易規則請以主管機關與券商最新公告為準。投資有風險,請依自身狀況判斷。")


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
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">📈 %s</p>' % NOTE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)
