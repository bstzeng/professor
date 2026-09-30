# -*- coding: utf-8 -*-
"""電腦是怎麼從零開始的:共用工具。

lesson() 每課結尾自動補上「想一想」callout 與一行「內容為機制說明」提醒。
沿用檔案格式課的 SVG／圖表小工具(line_chart、bars、box、flow、layout、mono…)。
"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, layout, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)

NOTE = (u"本課重在理解<strong>原理與機制</strong>,而非背年份或型號;"
        u"歷史事件(如公司併購、產品發表)只作陳述、不加立場,細節請以權威資料為準;"
        u"部分技術描述為<strong>簡化示意</strong>,真實硬體/系統更複雜,目的是先建立正確直覺。")


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
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🧭 %s</p>' % NOTE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)
