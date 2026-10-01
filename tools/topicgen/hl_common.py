# -*- coding: utf-8 -*-
"""〈穿越古代過一天〉與〈皇帝的一天〉共用工具。

lesson() 每課結尾自動補上「📚 史料出處與可信度」與一行說明。
daybar() 畫出一天 24 小時、以十二時辰標示的時間條。
"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)

NOTE = (u"本課的人物與情節是依史料重建的<strong>模擬</strong>：生活細節盡量有出處，史料不足的地方是合理推測，"
        u"文中以「可能」「大約」或「傳說」標示。年代、數字以通行的學術說法為準，個別細節學界仍有爭議。")


def lesson(title_, desc, goals, body, src, check, nxt=None):
    """src：史料出處與可信度說明（字串或字串列表）。"""
    blocks = []
    for b in body:
        if isinstance(b, tuple) and b[0] == "FIGX":
            blocks.append(("fig", b[1], b[2], b[3]))
        else:
            blocks.append(b)
    if isinstance(src, (list, tuple)):
        blocks.append(("note", u"📚 史料出處與可信度", [("ul", list(src))]))
    else:
        blocks.append(("note", u"📚 史料出處與可信度", [("p", src)]))
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">📜 %s</p>' % NOTE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


_TOPICS = {
    "ch": (u"chinese-history", u"中國歷史全紀錄"),
    "dl": (u"ancient-daily-life", u"穿越古代過一天"),
    "em": (u"emperor-life", u"皇帝的一天"),
}


def XL(key, n=None, text=None):
    tid, name = _TOPICS[key]
    if n is None:
        return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)
    return u'<a href="../%s/lesson-%02d.html">%s</a>' % (tid, n, text or u"〈%s〉第 %d 課" % (name, n))


def fig(svgtext, h, cap):
    return ("FIGX", svgtext, "0 0 640 %d" % h, cap)


def bg(text):
    """「時代背景」小框：連回〈中國歷史全紀錄〉。"""
    return ("note", u"🏛️ 時代背景", [("p", text)])


def myth(items):
    """「傳說還是史實」小框。"""
    return ("note", u"🔍 傳說還是史實？", [("ul", items)])


BRANCHES = u"子丑寅卯辰巳午未申酉戌亥"


def daybar(head, segs, note=u"", y=56):
    """segs = [(開始小時, 結束小時, 顏色, 編號)]，小時 0～24。回傳 svg 字串（高度約 150）。
    時辰標在偶數小時（子 = 0 點、丑 = 2 點……），格線在奇數小時。"""
    x0, x1 = 30.0, 610.0
    w = (x1 - x0) / 24.0
    out = [title(head)]
    out.append(R(x0, y, x1 - x0, 30, LINE, "var(--surface)", 4))
    for h0, h1, col, num in segs:
        out.append(R(x0 + h0 * w, y, (h1 - h0) * w, 30, col, col, 0, 0.8, op=0.45))
        if (h1 - h0) * w >= 14:
            out.append(T(x0 + (h0 + h1) / 2.0 * w, y + 19, num, 10, TXT))
    for h in range(1, 24, 2):
        out.append(P("M%g %g V%g" % (x0 + h * w, y - 4, y + 34), MUTED, sw=0.7, dash="2 2"))
    for i in range(13):
        out.append(T(x0 + 2 * i * w, y - 8, BRANCHES[i % 12], 10, ACC))
    for h in range(0, 25, 3):
        out.append(T(x0 + h * w, y + 48, u"%d" % h, 8.5, MUTED))
    out.append(T(x1, y + 62, u"（今日時鐘）", 8.5, MUTED, "end"))
    if note:
        out.append(T(320, y + 84, note, 9.5, ACC))
    return svg(out)


def daytable(rows):
    """rows = [(編號, 時辰, 約今, 做什麼)] → 表格區塊。"""
    return ("t", [u"", u"時辰", u"約今", u"在做什麼"], [list(r) for r in rows])


def timeline(head, items, y=80, x0=40, x1=600, lo=None, hi=None, note=u""):
    """items = [(年份, 標籤, 顏色)]，年份可為負數（西元前）。標籤上下交錯。"""
    ys = [it[0] for it in items]
    lo = min(ys) if lo is None else lo
    hi = max(ys) if hi is None else hi
    out = [title(head), P("M%g %g H%g" % (x0, y, x1), MUTED, sw=1.5)]

    def sx(v):
        return x0 + (v - lo) * (x1 - x0) / float(hi - lo)

    for i, (yr, lab, col) in enumerate(items):
        x = sx(yr)
        up = (i % 2 == 0)
        out.append(C(x, y, 4, col, col))
        out.append(P("M%g %g V%g" % (x, y + (-6 if up else 6), y + (-22 if up else 22)), col, sw=1))
        yl = u"前 %d" % (-yr) if yr < 0 else u"%d" % yr
        if up:
            out.append(T(x, y - 38, lab, 9.5, col))
            out.append(T(x, y - 26, yl, 8.5, MUTED))
        else:
            out.append(T(x, y + 34, yl, 8.5, MUTED))
            out.append(T(x, y + 47, lab, 9.5, col))
    if note:
        out.append(T(320, y + 76, note, 9.5, ACC))
    return svg(out)
