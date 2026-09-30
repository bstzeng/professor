# -*- coding: utf-8 -*-
"""心率與有氧運動：共用的課程包裝、心率公式與圖表小工具。

- lesson()：每課結尾自動補上「訓練小提醒」callout 與運動安全提醒
- 心率公式（最大心率、儲備心率、區間）集中在這裡，課文與計算器共用同一套數字
- line_chart() / bars()：畫簡單的座標圖，讓各課的曲線圖風格一致
"""
from gen import Lesson
from ho_common import (T, R, C, E, P, A, box, flow, svg, title,
                       RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT)

PURPLE = "#9c89d6"
TEAL = "#5fa8a8"
GRAY = "#8a8f98"

# 五區間的代表色：由冷到熱
ZC = [GRAY, BLUE, GREEN, ORANGE, RED]

SAFETY = (u"本課為一般運動生理與訓練知識，<strong>不能取代醫師或專業教練的個別評估</strong>。"
          u"有心臟病、高血壓、糖尿病、懷孕或正在服藥，開始新的運動計畫前請先諮詢醫師；"
          u"運動中出現胸痛、昏厥、異常喘或心悸，請立即停止並就醫。")


def lesson(title_, desc, goals, body, tip, check, fig=None, nxt=None):
    blocks = []
    for b in body:
        if b == "FIG":
            blocks.append(("fig", fig[0], fig[1], fig[2]))
        else:
            blocks.append(b)
    if fig and "FIG" not in body:
        blocks.insert(1, ("fig", fig[0], fig[1], fig[2]))
    blocks.append(("note", u"訓練小提醒", [("p", tip)]))
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🩺 %s</p>' % SAFETY))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


def ORG(n, text):
    """連到「人體器官運作機制」主題的某一課。"""
    return u'<a href="../human-organs/lesson-%02d.html">%s</a>' % (n, text)


# ---------- 心率公式 ----------

MAXHR_FORMULAS = [
    (u"Fox（220 − 年齡）", lambda a: 220 - a),
    (u"Tanaka（208 − 0.7 × 年齡）", lambda a: 208 - 0.7 * a),
    (u"Gellish（207 − 0.7 × 年齡）", lambda a: 207 - 0.7 * a),
    (u"Nes（211 − 0.64 × 年齡）", lambda a: 211 - 0.64 * a),
]

# 五區間（最大心率百分比）：名稱、下限、上限、感受、主要目的
ZONES = [
    (u"Z1 恢復", 50, 60, u"非常輕鬆，可以唱歌", u"熱身、緩和、積極恢復"),
    (u"Z2 有氧基礎", 60, 70, u"輕鬆，可以完整聊天", u"粒線體、微血管、脂肪利用、耐力基礎"),
    (u"Z3 節奏", 70, 80, u"有點喘，只能說短句", u"有氧效率、配速耐力"),
    (u"Z4 閾值", 80, 90, u"吃力，只能說幾個字", u"提高乳酸閾值"),
    (u"Z5 最大攝氧", 90, 100, u"非常吃力，說不出話", u"提高最大攝氧量（VO₂max）"),
]

# 乳酸閾值心率（LTHR）百分比區間（跑步，參考 Joe Friel 的分法並簡化成五區）
LT_ZONES = [(u"Z1", 0, 85), (u"Z2", 85, 90), (u"Z3", 90, 95), (u"Z4", 95, 100), (u"Z5", 100, 106)]


def karvonen(maxhr, rest, pct):
    return rest + (maxhr - rest) * pct / 100.0


def pct_max(maxhr, pct):
    return maxhr * pct / 100.0


# ---------- 圖表小工具 ----------

def line_chart(x, y, w, h, xr, yr, series, xticks=(), yticks=(), xlabel=u"", ylabel=u"",
               bands=(), grid=True):
    """series = [(點列表 [(xv, yv)], 顏色, 標籤, 標籤位置 (xv, yv) 或 None, 虛線)]；
    bands = [(y1, y2, 顏色, 文字)] 畫水平色帶。座標以資料值表示，自動換算。"""
    x0, x1 = xr
    y0, y1 = yr

    def sx(v):
        return x + (v - x0) * w / float(x1 - x0)

    def sy(v):
        return y + h - (v - y0) * h / float(y1 - y0)

    out = []
    for b in bands:
        a, c, col, lab = b
        out.append(R(x, sy(c), w, sy(a) - sy(c), col, col, 0, 0, op=0.13))
        if lab:
            out.append(T(x + w - 4, sy(c) + 11, lab, 8.5, col, "end"))
    if grid:
        for v, lab in yticks:
            out.append(P("M%g %g H%g" % (x, sy(v), x + w), LINE, sw=0.6, dash="2 3"))
    out.append(P("M%g %g V%g H%g" % (x, y, y + h, x + w), MUTED, sw=1.2))
    for v, lab in xticks:
        out.append(T(sx(v), y + h + 14, lab, 8.5))
    for v, lab in yticks:
        out.append(T(x - 5, sy(v) + 3, lab, 8.5, MUTED, "end"))
    if xlabel:
        out.append(T(x + w / 2.0, y + h + 28, xlabel, 9.5))
    if ylabel:
        out.append('<text x="%g" y="%g" text-anchor="middle" font-size="9.5" fill="%s" '
                   'transform="rotate(-90 %g %g)">%s</text>' % (x - 34, y + h / 2.0, MUTED,
                                                                 x - 34, y + h / 2.0, ylabel))
    for s in series:
        pts, col, lab, lp = s[0], s[1], s[2], s[3]
        dash = s[4] if len(s) > 4 else None
        d = "M" + " L".join("%.1f %.1f" % (sx(a), sy(b)) for a, b in pts)
        out.append(P(d, col, sw=2.2, dash=dash))
        if lab and lp:
            out.append(T(sx(lp[0]), sy(lp[1]), lab, 9.5, col, "start"))
    return out


def bars(x, y, w, h, items, vmax, labsize=9, valfmt=u"%s", horizontal=False):
    """items = [(標籤, 數值, 顏色)]。直條圖（預設）或橫條圖。"""
    out = []
    n = len(items)
    if horizontal:
        bh = h / float(n)
        for i, (lab, v, col) in enumerate(items):
            yy = y + i * bh
            bw = w * v / float(vmax)
            out.append(R(x, yy + bh * 0.18, bw, bh * 0.64, col, col, 3, 1, op=0.75))
            out.append(T(x - 6, yy + bh / 2.0 + 3.5, lab, labsize, MUTED, "end"))
            out.append(T(x + bw + 5, yy + bh / 2.0 + 3.5, valfmt % v, labsize, col, "start"))
    else:
        bw = w / float(n)
        for i, (lab, v, col) in enumerate(items):
            xx = x + i * bw
            bhh = h * v / float(vmax)
            out.append(R(xx + bw * 0.2, y + h - bhh, bw * 0.6, bhh, col, col, 3, 1, op=0.75))
            out.append(T(xx + bw / 2.0, y + h + 14, lab, labsize))
            out.append(T(xx + bw / 2.0, y + h - bhh - 5, valfmt % v, labsize, col))
        out.append(P("M%g %g H%g" % (x, y + h, x + w), MUTED, sw=1.2))
    return out


def zone_bar(x, y, w, h, labels=None, lo=50, hi=100):
    """把五區間畫成一條色帶（最大心率 50%～100%）。"""
    out = []
    for i, (name, a, b, feel, goal) in enumerate(ZONES):
        xa = x + (a - lo) * w / float(hi - lo)
        xb = x + (b - lo) * w / float(hi - lo)
        out.append(R(xa, y, xb - xa, h, ZC[i], ZC[i], 0, 1, op=0.55))
        out.append(T((xa + xb) / 2.0, y + h / 2.0 + 4, (labels or [z[0] for z in ZONES])[i], 9.5, TXT))
    for p in range(lo, hi + 1, 10):
        out.append(T(x + (p - lo) * w / float(hi - lo), y + h + 14, u"%d%%" % p, 8.5))
    return out


def svg(*parts):
    """同 ho_common.svg，但允許巢狀清單（列表推導式裡再產生清單）。"""
    lines = []

    def add(p):
        if isinstance(p, (list, tuple)):
            for q in p:
                add(q)
        elif p:
            lines.append(p)
    for p in parts:
        add(p)
    return "\n".join("          " + ln for ln in lines)
