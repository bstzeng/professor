# -*- coding: utf-8 -*-
"""道教入門:共用工具。

lesson() 每課結尾自動補上「想一想」callout 與一行「介紹與理解、多元觀點」提醒。
沿用檔案格式課的 SVG 小工具(box、flow、layout、mono…)。
"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, layout, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)

NOTE = (u"本課以<strong>介紹與理解</strong>為目的,不勸信也不貶抑;"
        u"道家(哲學)、道教(宗教)、民間信仰三者相關但不相同,各派別與地方的說法、做法常有差異;"
        u"儀式與法術只說明由來與意義,不評斷效驗;養生內容為文化介紹,<strong>不是醫療建議</strong>;"
        u"年代與神明誕辰多依通行說法,各地可能不同。")


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
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">☯️ %s</p>' % NOTE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


def fig(svgtext, h, cap):
    return ("FIGX", svgtext, "0 0 640 %d" % h, cap)


def quote(text, src=None):
    tail = u'<div style="font-size:0.85em;color:var(--text-muted);margin-top:4px">—— %s</div>' % src if src else u""
    return ("raw", u'<blockquote style="font-size:1.08em;line-height:1.9;border-left:4px solid var(--accent);'
                   u'padding:8px 16px;margin:12px 0;background:var(--surface)">%s%s</blockquote>' % (text, tail))


def ddj(n, show_plain=True):
    """《道德經》第 n 章的引文(+白話)區塊清單。"""
    from tao_ddj import chap
    c = chap(n)
    out = [quote(c[2], u"《道德經》第 %d 章%s" % (n, u"(節錄)" if c[5] else u""))]
    if show_plain:
        out.append(("p", u"<strong>白話:</strong>" + c[3]))
    return out
