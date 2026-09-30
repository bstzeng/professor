# -*- coding: utf-8 -*-
"""佛教入門:共用工具。

lesson() 每課結尾自動補上「想一想」callout 與一行「介紹與理解、多元觀點」提醒。
沿用檔案格式課的 SVG 小工具(box、flow、layout、mono…)。
"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, layout, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)

NOTE = (u"本課以<strong>介紹與理解</strong>為目的,不勸信也不貶抑;"
        u"佛教各傳承與宗派對同一教義常有不同詮釋,文中會標明<strong>傳統說法</strong>與<strong>學術觀點</strong>;"
        u"年代多為學界概略推定,經文字句以通行版本為準,各地誦本偶有用字差異。")


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
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🪷 %s</p>' % NOTE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


def fig(svgtext, h, cap):
    return ("FIGX", svgtext, "0 0 640 %d" % h, cap)
