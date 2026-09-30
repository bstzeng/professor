# -*- coding: utf-8 -*-
"""人體器官運作機制：共用的課程包裝與 SVG 小工具。

lesson() 會在每課正文後面自動補上「生活連結」callout 與醫療提醒，
SVG 小工具讓各課的圖解保持一致的風格（寬 640、使用站上的 CSS 變數）。
"""
import math
from gen import Lesson

RED = "#e0605a"      # 動脈血、發炎、交感
BLUE = "#4a90c2"     # 靜脈血、水分、副交感
GREEN = "#5aa469"    # 營養、合成、正常
ORANGE = "#ff8a65"   # 能量、警示
ACC = "var(--accent)"
GOLD = "var(--gold)"
MUTED = "var(--text-muted)"
LINE = "var(--border)"
TXT = "var(--text)"

DISCLAIMER = (u"本課內容為一般衛教與生理學知識，<strong>不能取代醫師的診斷與治療</strong>；"
              u"身體有不舒服或異常時，請諮詢專業醫療人員。")


def lesson(title, desc, goals, body, life, check, fig=None, nxt=None):
    """fig = (svg, viewBox, 圖說)，會插在正文第一個 h2 之後的段落群前面（即 body 中 ("FIG",) 的位置）。"""
    blocks = []
    for b in body:
        if b == "FIG":
            blocks.append(("fig", fig[0], fig[1], fig[2]))
        else:
            blocks.append(b)
    if fig and "FIG" not in body:
        blocks.insert(1, ("fig", fig[0], fig[1], fig[2]))
    blocks.append(("note", u"生活連結", [("p", life)]))
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">⚕️ %s</p>' % DISCLAIMER))
    return Lesson(title, desc, goals, blocks, check, nxt)


# ---------- SVG 小工具 ----------

def T(x, y, s, size=10, color=MUTED, anchor="middle", weight=None):
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%g" y="%g" text-anchor="%s" font-size="%g" fill="%s"%s>%s</text>' % (
        x, y, anchor, size, color, w, s)


def R(x, y, w, h, stroke=LINE, fill="var(--surface)", rx=8, sw=1.5, op=None):
    o = ' fill-opacity="%g"' % op if op is not None else ""
    return '<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s"%s stroke="%s" stroke-width="%g"/>' % (
        x, y, w, h, rx, fill, o, stroke, sw)


def C(cx, cy, r, stroke=LINE, fill="var(--surface)", sw=1.5, op=None):
    o = ' fill-opacity="%g"' % op if op is not None else ""
    return '<circle cx="%g" cy="%g" r="%g" fill="%s"%s stroke="%s" stroke-width="%g"/>' % (
        cx, cy, r, fill, o, stroke, sw)


def E(cx, cy, rx, ry, stroke=LINE, fill="var(--surface)", sw=1.5, op=None):
    o = ' fill-opacity="%g"' % op if op is not None else ""
    return '<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="%s"%s stroke="%s" stroke-width="%g"/>' % (
        cx, cy, rx, ry, fill, o, stroke, sw)


def P(d, stroke=LINE, fill="none", sw=1.5, op=None, dash=None):
    o = ' fill-opacity="%g"' % op if op is not None else ""
    da = ' stroke-dasharray="%s"' % dash if dash else ""
    return '<path d="%s" fill="%s"%s stroke="%s" stroke-width="%g"%s/>' % (d, fill, o, stroke, sw, da)


def A(x1, y1, x2, y2, color=LINE, sw=1.5, head=7, dash=None):
    """直線箭頭，箭頭尖端落在 (x2, y2)。"""
    ang = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(ang), y2 - head * math.sin(ang)
    px, py = -math.sin(ang) * head * 0.5, math.cos(ang) * head * 0.5
    da = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%g"%s/>'
            '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>') % (
        x1, y1, bx, by, color, sw, da, x2, y2, bx + px, by + py, bx - px, by - py, color)


def box(x, y, w, h, title, sub=None, color=ACC, size=11, subsize=9, fill="var(--surface)"):
    out = [R(x, y, w, h, stroke=color, fill=fill)]
    if sub:
        subs = sub if isinstance(sub, (list, tuple)) else [sub]
        top = y + h / 2.0 - (len(subs) * (subsize + 3)) / 2.0 + 2
        out.append(T(x + w / 2.0, top, title, size, color))
        for i, s in enumerate(subs):
            out.append(T(x + w / 2.0, top + (i + 1) * (subsize + 4) + 1, s, subsize))
    else:
        out.append(T(x + w / 2.0, y + h / 2.0 + size * 0.35, title, size, color))
    return "".join(out)


def flow(items, y, h=52, x0=20, x1=620, gap=26, colors=None):
    """水平流程：items = [(標題, 副標), ...]，自動等寬排列並加箭頭。"""
    n = len(items)
    w = (x1 - x0 - gap * (n - 1)) / float(n)
    out = []
    for i, it in enumerate(items):
        t, s = (it if isinstance(it, tuple) else (it, None))
        c = colors[i] if colors else ACC
        x = x0 + i * (w + gap)
        out.append(box(x, y, w, h, t, s, c))
        if i < n - 1:
            out.append(A(x + w + 3, y + h / 2.0, x + w + gap - 3, y + h / 2.0))
    return "".join(out)


def svg(*parts):
    """把零件串成 figure 需要的內文（每個元素一行、10 格縮排）。"""
    lines = []
    for p in parts:
        if isinstance(p, (list, tuple)):
            lines.extend(p)
        else:
            lines.append(p)
    return "\n".join("          " + ln for ln in lines if ln)


def title(s, y=18):
    return T(320, y, s, 12, MUTED)
