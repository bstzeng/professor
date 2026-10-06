# -*- coding: utf-8 -*-
"""歐洲各國國旗（SVG）。圖案簡單的照比例畫出；含國徽的國旗，國徽部分以簡化圖形表示。"""
import math

W, H = 150, 100


def rect(x, y, w, h, c):
    return '<rect x="%g" y="%g" width="%g" height="%g" fill="%s"/>' % (x, y, w, h, c)


def star(x, y, r, c="#fff", rot=0, n=5, inner=0.38):
    pts = []
    for i in range(2 * n):
        a = math.pi / 2 + rot + i * math.pi / n
        rr = r if i % 2 == 0 else r * inner
        pts.append("%.1f,%.1f" % (x + rr * math.cos(a), y - rr * math.sin(a)))
    return '<polygon points="%s" fill="%s"/>' % (" ".join(pts), c)


def frame(s, w=W, h=H):
    return (s + '<rect x="0.5" y="0.5" width="%g" height="%g" fill="none" stroke="#888" stroke-width="1"/>' % (w - 1, h - 1), w, h)


def hstripes(cols, w=W, h=H, ratios=None):
    ratios = ratios or [1] * len(cols)
    tot = float(sum(ratios))
    s, y = "", 0
    for c, r in zip(cols, ratios):
        hh = h * r / tot
        s += rect(0, y, w, hh + 0.3, c)
        y += hh
    return s


def vstripes(cols, w=W, h=H):
    s = ""
    for i, c in enumerate(cols):
        s += rect(w * i / len(cols), 0, w / len(cols) + 0.3, h, c)
    return s


def nordic(bg, cross, border=None, w=W, h=H):
    s = rect(0, 0, w, h, bg)
    if border:
        s += rect(w * 0.27, 0, h * 0.24, h, border) + rect(0, h * 0.38, w, h * 0.24, border)
        s += rect(w * 0.27 + h * 0.06, 0, h * 0.12, h, cross) + rect(0, h * 0.44, w, h * 0.12, cross)
    else:
        s += rect(w * 0.3, 0, h * 0.2, h, cross) + rect(0, h * 0.4, w, h * 0.2, cross)
    return s


def shield(x, y, w, h, fill, stroke="#c9a227"):
    return ('<path d="M%g,%g h%g v%g q0,%g -%g,%g q-%g,-%g -%g,-%g z" fill="%s" stroke="%s" stroke-width="1.2"/>'
            % (x, y, w, h * 0.55, h * 0.35, w / 2, h * 0.45, w / 2, h * 0.1, w / 2, h * 0.45, fill, stroke))


def eagle(cx, cy, s, c):
    """簡化的雙頭鷹：兩個頭、展開的雙翼、身體與尾羽。"""
    g = '<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="%s"/>' % (cx, cy, s * 0.22, s * 0.45, c)
    g += '<polygon points="%g,%g %g,%g %g,%g %g,%g" fill="%s"/>' % (cx - s * 0.15, cy - s * 0.2, cx - s, cy - s * 0.7, cx - s * 0.85, cy + s * 0.1,
                                                                     cx - s * 0.15, cy + s * 0.2, c)
    g += '<polygon points="%g,%g %g,%g %g,%g %g,%g" fill="%s"/>' % (cx + s * 0.15, cy - s * 0.2, cx + s, cy - s * 0.7, cx + s * 0.85, cy + s * 0.1,
                                                                     cx + s * 0.15, cy + s * 0.2, c)
    g += '<circle cx="%g" cy="%g" r="%g" fill="%s"/><circle cx="%g" cy="%g" r="%g" fill="%s"/>' % (
        cx - s * 0.28, cy - s * 0.62, s * 0.14, c, cx + s * 0.28, cy - s * 0.62, s * 0.14, c)
    g += '<polygon points="%g,%g %g,%g %g,%g" fill="%s"/>' % (cx - s * 0.25, cy + s * 0.35, cx + s * 0.25, cy + s * 0.35, cx, cy + s * 0.8, c)
    return g


def union_jack(w=150, h=75):
    s = rect(0, 0, w, h, "#012169")
    s += '<path d="M0,0 L%g,%g M%g,0 L0,%g" stroke="#fff" stroke-width="%g"/>' % (w, h, w, h, h / 5)
    s += '<path d="M0,0 L%g,%g M%g,0 L0,%g" stroke="#C8102E" stroke-width="%g"/>' % (w, h, w, h, h / 15)
    s += rect(w / 2 - h / 6, 0, h / 3, h, "#fff") + rect(0, h / 2 - h / 6, w, h / 3, "#fff")
    s += rect(w / 2 - h / 10, 0, h / 5, h, "#C8102E") + rect(0, h / 2 - h / 10, w, h / 5, "#C8102E")
    return s


F = {}
F["GBR"] = lambda: frame(union_jack(), 150, 75)
F["IRL"] = lambda: frame(vstripes(["#169B62", "#fff", "#FF883E"]), 150, 75)
F["FRA"] = lambda: frame(vstripes(["#002654", "#fff", "#CE1126"]))
F["BEL"] = lambda: frame(vstripes(["#000", "#FDDA24", "#EF3340"], 150, 130), 150, 130)
F["NLD"] = lambda: frame(hstripes(["#AE1C28", "#fff", "#21468B"]))
F["LUX"] = lambda: frame(hstripes(["#EF3340", "#fff", "#00A3E0"], 150, 90), 150, 90)
F["DEU"] = lambda: frame(hstripes(["#000", "#DD0000", "#FFCE00"], 150, 90), 150, 90)
F["AUT"] = lambda: frame(hstripes(["#C8102E", "#fff", "#C8102E"]))
F["CHE"] = lambda: frame(rect(0, 0, 100, 100, "#DA291C") + rect(40, 19, 20, 62, "#fff") + rect(19, 40, 62, 20, "#fff"), 100, 100)
F["POL"] = lambda: frame(hstripes(["#fff", "#DC143C"], 150, 94), 150, 94)
F["CZE"] = lambda: frame(hstripes(["#fff", "#D7141A"]) + '<polygon points="0,0 75,50 0,100" fill="#11457E"/>')
F["SVK"] = lambda: frame(hstripes(["#fff", "#0B4EA2", "#EE1C25"]) + shield(30, 20, 34, 52, "#EE1C25", "#fff") +
                         rect(45, 28, 4, 30, "#fff") + rect(38, 34, 18, 4, "#fff") + rect(40, 43, 14, 4, "#fff") +
                         '<path d="M32,62 q8,-10 15,0 q8,-10 15,0 v8 h-30 z" fill="#0B4EA2"/>')
F["HUN"] = lambda: frame(hstripes(["#CD2A3E", "#fff", "#436F4D"]))
F["ESP"] = lambda: frame(hstripes(["#AA151B", "#F1BF00", "#AA151B"], ratios=[1, 2, 1]) + shield(36, 33, 22, 30, "#AA151B", "#c9a227") +
                         rect(30, 36, 4, 26, "#c9a227") + rect(60, 36, 4, 26, "#c9a227"))
F["PRT"] = lambda: frame(rect(0, 0, 60, 100, "#006600") + rect(60, 0, 90, 100, "#FF0000") +
                         '<circle cx="60" cy="50" r="20" fill="none" stroke="#FFE900" stroke-width="5"/>' + shield(50, 37, 20, 26, "#fff", "#FF0000"))
F["ITA"] = lambda: frame(vstripes(["#009246", "#fff", "#CE2B37"]))
F["GRC"] = lambda: frame(hstripes(["#0D5EAF", "#fff"] * 4 + ["#0D5EAF"]) + rect(0, 0, 55.6, 55.6, "#0D5EAF") +
                         rect(22.2, 0, 11.1, 55.6, "#fff") + rect(0, 22.2, 55.6, 11.1, "#fff"))
F["MLT"] = lambda: frame(rect(0, 0, 75, 100, "#fff") + rect(75, 0, 75, 100, "#CF142B") +
                         rect(14, 8, 8, 24, "#999") + rect(6, 16, 24, 8, "#999") + '<rect x="6" y="8" width="24" height="24" fill="none" stroke="#CF142B" stroke-width="1.5"/>')
F["CYP"] = lambda: frame(rect(0, 0, W, H, "#fff") + '<path d="M38,40 q20,-14 50,-8 q20,-2 30,-14 l4,4 q-10,14 -24,20 q-20,10 -40,8 q-14,0 -20,-10 z" fill="#D57800"/>' +
                         '<path d="M50,72 q25,14 50,0" fill="none" stroke="#4E5B31" stroke-width="4"/>')
F["DNK"] = lambda: frame(nordic("#C8102E", "#fff", w=148, h=112), 148, 112)
F["NOR"] = lambda: frame(nordic("#BA0C2F", "#00205B", "#fff", 154, 112), 154, 112)
F["SWE"] = lambda: frame(nordic("#006AA7", "#FECC00", w=150, h=94), 150, 94)
F["FIN"] = lambda: frame(nordic("#fff", "#002F6C", w=150, h=92), 150, 92)
F["ISL"] = lambda: frame(nordic("#02529C", "#DC1E35", "#fff", 150, 108), 150, 108)
F["EST"] = lambda: frame(hstripes(["#0072CE", "#000", "#fff"], 150, 95), 150, 95)
F["LVA"] = lambda: frame(hstripes(["#9E3039", "#fff", "#9E3039"], 150, 75, [2, 1, 2]), 150, 75)
F["LTU"] = lambda: frame(hstripes(["#FDB913", "#006A44", "#C1272D"], 150, 90), 150, 90)
F["UKR"] = lambda: frame(hstripes(["#0057B7", "#FFD700"]))
F["BLR"] = lambda: frame(hstripes(["#C8313E", "#4AA657"], 150, 75, [2, 1]) + rect(0, 0, 14, 75, "#fff") +
                         "".join('<path d="M7,%g l5,4.5 l-5,4.5 l-5,-4.5 z" fill="#C8313E"/>' % y for y in range(1, 70, 9)), 150, 75)
F["MDA"] = lambda: frame(vstripes(["#0046AE", "#FFD200", "#CC092F"]) + shield(66, 36, 18, 24, "#CC092F", "#7a5c2e") +
                         '<path d="M58,34 q17,-12 34,0 l-6,4 q-11,-6 -22,0 z" fill="#7a5c2e"/>')
F["RUS"] = lambda: frame(hstripes(["#fff", "#0039A6", "#D52B1E"]))
F["SVN"] = lambda: frame(hstripes(["#fff", "#005DA4", "#ED1C24"], 150, 75) + shield(30, 12, 22, 28, "#005DA4", "#ED1C24") +
                         '<path d="M32,32 l5,-8 l4,5 l4,-5 l5,8 z" fill="#fff"/>' + star(41, 18, 2.5, "#FFDD00") + star(36, 22, 2, "#FFDD00") + star(46, 22, 2, "#FFDD00"), 150, 75)
F["HRV"] = lambda: frame(hstripes(["#FF0000", "#fff", "#171796"], 150, 75) + "".join(
    rect(63 + (i % 5) * 4.8, 22 + (i // 5) * 5.4, 4.8, 5.4, "#FF0000" if (i + i // 5) % 2 == 0 else "#fff") for i in range(25)) +
    '<rect x="63" y="22" width="24" height="27" fill="none" stroke="#171796" stroke-width="1"/>' + rect(61, 14, 28, 7, "#171796"), 150, 75)
F["BIH"] = lambda: frame(rect(0, 0, 150, 75, "#002395") + '<polygon points="42,0 110,0 110,68" fill="#FECB00"/>' +
                         "".join(star(30 + i * 9.5, 2 + i * 9.5, 4.5) for i in range(9)), 150, 75)
F["SRB"] = lambda: frame(hstripes(["#C6363C", "#0C4076", "#fff"]) + shield(36, 22, 26, 34, "#C6363C", "#c9a227") +
                         eagle(49, 40, 10, "#fff"))
F["MNE"] = lambda: frame(rect(0, 0, W, H, "#C40308") + '<rect x="4" y="4" width="142" height="92" fill="none" stroke="#D4AF37" stroke-width="5"/>' +
                         eagle(75, 48, 22, "#D4AF37"))
F["MKD"] = lambda: frame(rect(0, 0, 150, 75, "#D20000") + "".join(
    '<polygon points="75,37.5 %g,%g %g,%g" fill="#FFE600"/>' % (75 + 120 * math.cos(math.radians(a - 7)), 37.5 + 120 * math.sin(math.radians(a - 7)),
                                                               75 + 120 * math.cos(math.radians(a + 7)), 37.5 + 120 * math.sin(math.radians(a + 7)))
    for a in range(0, 360, 45)) + '<circle cx="75" cy="37.5" r="13" fill="#FFE600" stroke="#D20000" stroke-width="3"/>' +
    '<clipPath id="mkc"><rect width="150" height="75"/></clipPath>', 150, 75)
F["ALB"] = lambda: frame(rect(0, 0, 140, 100, "#E41E20") + eagle(70, 52, 28, "#000"), 140, 100)
F["BGR"] = lambda: frame(hstripes(["#fff", "#00966E", "#D62612"], 150, 90), 150, 90)
F["ROU"] = lambda: frame(vstripes(["#002B7F", "#FCD116", "#CE1126"]))
F["KOS"] = lambda: frame(rect(0, 0, 140, 100, "#244AA5") + '<path d="M52,40 l10,-8 l14,2 l12,6 l4,12 l-6,10 l-12,6 l-14,-2 l-8,-10 z" fill="#D0A650"/>' +
                         "".join(star(70 + 34 * math.cos(math.radians(a)), 30 - 10 * math.sin(math.radians(a)) - 6, 4) for a in (150, 126, 102, 78, 54, 30)), 140, 100)
F["TUR"] = lambda: frame(rect(0, 0, W, H, "#E30A17") + '<circle cx="55" cy="50" r="25" fill="#fff"/><circle cx="61" cy="50" r="20" fill="#E30A17"/>' +
                         star(88, 50, 12, "#fff", rot=math.pi / 2))
F["VAT"] = lambda: frame(rect(0, 0, 50, 100, "#FFE000") + rect(50, 0, 50, 100, "#fff") +
                         '<path d="M62,70 L88,40 M88,70 L62,40" stroke="#c9a227" stroke-width="5"/>' + rect(68, 22, 14, 12, "#c9a227"), 100, 100)
F["SMR"] = lambda: frame(hstripes(["#fff", "#5EB6E4"], 150, 112) + shield(64, 36, 22, 30, "#5EB6E4", "#c9a227") + rect(72, 28, 6, 8, "#c9a227"), 150, 112)
F["MCO"] = lambda: frame(hstripes(["#CE1126", "#fff"], 150, 120), 150, 120)
F["LIE"] = lambda: frame(hstripes(["#002B7F", "#CE1126"], 150, 90) + '<path d="M26,30 l2,-12 l6,6 l6,-10 l6,10 l6,-6 l2,12 z" fill="#FFD83D"/>', 150, 90)
F["AND"] = lambda: frame(vstripes(["#10069F", "#FEDF00", "#D50032"], 150, 105) + shield(64, 36, 22, 30, "#FEDF00", "#c9a227") +
                         rect(66, 38, 8, 12, "#D50032") + rect(76, 38, 8, 12, "#D50032"), 150, 105)

EMBLEM = {"SVK", "ESP", "PRT", "MDA", "SVN", "HRV", "SRB", "MNE", "ALB", "CYP", "KOS", "VAT", "SMR", "LIE", "AND", "BLR"}


def flag(c):
    return F[c]()
