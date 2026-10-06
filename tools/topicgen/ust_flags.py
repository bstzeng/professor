# -*- coding: utf-8 -*-
"""美國五十州州旗的簡化示意圖（150×100）。圖案簡單的照實畫，州徽複雜的只畫底色與構圖。"""
import math

W, H = 150, 100
NAVY = "#002868"
RED = "#bf0a30"
GOLD = "#f2b632"
WHITE = "#ffffff"


def star(x, y, r, c=WHITE, rot=0, n=5):
    pts = []
    for i in range(2 * n):
        a = math.pi / 2 + rot + i * math.pi / n
        rr = r if i % 2 == 0 else r * (0.38 if n == 5 else 0.5)
        pts.append("%.1f,%.1f" % (x + rr * math.cos(a), y - rr * math.sin(a)))
    return '<polygon points="%s" fill="%s"/>' % (" ".join(pts), c)


def rect(x, y, w, h, c):
    return '<rect x="%g" y="%g" width="%g" height="%g" fill="%s"/>' % (x, y, w, h, c)


def text(x, y, s, size=9, c=WHITE, w="bold"):
    return ('<text x="%g" y="%g" font-size="%g" font-weight="%s" fill="%s" text-anchor="middle" '
            'font-family="Georgia,serif">%s</text>' % (x, y, size, w, c, s))


def frame(inner, w=W, h=H):
    return (inner + '<rect x="0.5" y="0.5" width="%g" height="%g" fill="none" stroke="#888" stroke-width="1"/>' % (w - 1, h - 1), w, h)


def seal(cx=75, cy=50, r=24, ring=GOLD, fill="#f4ecd2", inner="#8a6d3b"):
    """一般州徽的示意：同心圓。"""
    return ('<circle cx="%g" cy="%g" r="%g" fill="%s" stroke="%s" stroke-width="3"/>' % (cx, cy, r, fill, ring) +
            '<circle cx="%g" cy="%g" r="%g" fill="none" stroke="%s" stroke-width="0.8"/>' % (cx, cy, r - 6, inner) +
            '<path d="M%g,%g q%g,-%g %g,0" fill="none" stroke="%s" stroke-width="1.5"/>' % (cx - r + 10, cy + 6, r - 10, r * 0.6, 2 * r - 20, inner))


def generic(field=NAVY, top=None, bottom=None, ring=GOLD, tc=WHITE, **k):
    s = rect(0, 0, W, H, field) + seal(ring=ring, **k)
    if top:
        s += text(75, 18, top, 9, tc)
    if bottom:
        s += text(75, 92, bottom, 9, tc)
    return frame(s)


def union_jack(x, y, w, h):
    s = rect(x, y, w, h, "#012169")
    s += ('<path d="M%g,%g L%g,%g M%g,%g L%g,%g" stroke="%s" stroke-width="%g"/>' % (x, y, x + w, y + h, x + w, y, x, y + h, WHITE, h / 5))
    s += ('<path d="M%g,%g L%g,%g M%g,%g L%g,%g" stroke="%s" stroke-width="%g"/>' % (x, y, x + w, y + h, x + w, y, x, y + h, "#C8102E", h / 15))
    s += rect(x + w / 2 - h / 6, y, h / 3, h, WHITE) + rect(x, y + h / 2 - h / 6, w, h / 3, WHITE)
    s += rect(x + w / 2 - h / 10, y, h / 5, h, "#C8102E") + rect(x, y + h / 2 - h / 10, w, h / 5, "#C8102E")
    return s


def F_AL():
    return frame(rect(0, 0, W, H, WHITE) + '<path d="M0,0 L150,100 M150,0 L0,100" stroke="#b22234" stroke-width="16"/>')


def F_AK():
    s = rect(0, 0, W, H, "#0f204b")
    for x, y in [(24, 72), (40, 70), (54, 64), (66, 58), (82, 60), (86, 75), (70, 79)]:   # 北斗七星
        s += star(x, y, 4.5, GOLD)
    return frame(s + star(122, 24, 8, GOLD))


def F_AZ():
    s = rect(0, 50, W, 50, NAVY)
    for i in range(13):
        a0 = math.pi * i / 13
        a1 = math.pi * (i + 1) / 13
        c = RED if i % 2 == 0 else "#fed700"
        s += '<path d="M75,50 L%g,%g L%g,%g Z" fill="%s"/>' % (75 - 120 * math.cos(a0), 50 - 120 * math.sin(a0), 75 - 120 * math.cos(a1), 50 - 120 * math.sin(a1), c)
    s += '<rect x="0" y="0" width="150" height="50" fill="none"/>'
    s = '<clipPath id="azc"><rect width="150" height="100"/></clipPath><g clip-path="url(#azc)">' + s + '</g>'
    return frame(s + star(75, 50, 18, "#ce5c17"))


def F_AR():
    s = rect(0, 0, W, H, RED) + '<polygon points="75,8 136,50 75,92 14,50" fill="%s"/>' % NAVY
    s += '<polygon points="75,16 124,50 75,84 26,50" fill="%s"/>' % WHITE
    s += text(75, 55, "ARKANSAS", 10, NAVY) + star(75, 34, 5, NAVY) + star(62, 67, 4, NAVY) + star(75, 70, 4, NAVY) + star(88, 67, 4, NAVY)
    return frame(s)


def F_CA():
    s = rect(0, 0, W, H, WHITE) + rect(0, 86, W, 14, "#b22234") + star(20, 16, 9, "#b22234")
    s += '<ellipse cx="78" cy="52" rx="30" ry="13" fill="#6b4226"/><circle cx="108" cy="46" r="8" fill="#6b4226"/>'
    s += rect(56, 58, 7, 12, "#6b4226") + rect(92, 58, 7, 12, "#6b4226") + rect(48, 70, 62, 3, "#5a7d2a")
    return frame(s + text(75, 82, "CALIFORNIA REPUBLIC", 8.5, "#6b4226"))


def F_CO():
    s = rect(0, 0, W, H, "#002868") + rect(0, 33.3, W, 33.4, WHITE)
    s += '<circle cx="60" cy="50" r="13" fill="#ffd700"/>'
    s += '<path d="M83,38 A25,25 0 1 0 83,62" fill="none" stroke="#bf0a30" stroke-width="15"/>'
    return frame(s)


def F_DE():
    s = rect(0, 0, W, H, "#5b91c6") + '<polygon points="75,16 120,50 75,84 30,50" fill="#e6c48a"/>'
    s += '<rect x="64" y="36" width="22" height="26" rx="4" fill="#5b91c6" opacity="0.6"/>'
    return frame(s + text(75, 96, "DECEMBER 7, 1787", 7, WHITE))


def F_FL():
    s = rect(0, 0, W, H, WHITE) + '<path d="M0,0 L150,100 M150,0 L0,100" stroke="#bf0a30" stroke-width="14"/>'
    return frame(s + seal(r=17, ring="#7a5c2e"))


def F_GA():
    s = rect(0, 0, W, H, RED) + rect(0, 33.3, W, 33.4, WHITE) + rect(0, 0, 66.7, 66.7, NAVY)
    s += '<path d="M23,46 L23,30 Q33.3,18 43.6,30 L43.6,46" fill="none" stroke="%s" stroke-width="3"/>' % GOLD
    for i in range(13):
        a = math.pi * 2 * i / 13 - math.pi / 2
        s += star(33.3 + 24 * math.cos(a), 33.3 + 24 * math.sin(a), 2.6)
    return frame(s)


def F_HI():
    cols = [WHITE, RED, "#012169"]
    s = "".join(rect(0, i * 12.5, W, 12.5, cols[i % 3]) for i in range(8))
    return frame(s + union_jack(0, 0, 75, 50))


def F_IN():
    s = rect(0, 0, W, H, NAVY) + rect(72, 40, 6, 32, GOLD) + '<path d="M75,40 q-8,-10 0,-20 q8,10 0,20" fill="%s"/>' % GOLD
    for i in range(19):
        a = math.pi * (0.9 + 1.2 * i / 18)
        s += star(75 + 38 * math.cos(a), 54 + 32 * math.sin(a), 2.5, GOLD)
    return frame(s + text(75, 14, "INDIANA", 8.5, GOLD))


def F_IA():
    s = rect(0, 0, 50, H, NAVY) + rect(50, 0, 50, H, WHITE) + rect(100, 0, 50, H, RED)
    s += '<path d="M60,44 q15,-14 30,0 q-15,-6 -30,0" fill="#5a3a1a"/>' + text(75, 66, "IOWA", 10, RED)
    return frame(s)


def F_MD():
    s = ""
    for qx, qy, kind in [(0, 0, 1), (75, 0, 2), (0, 50, 2), (75, 50, 1)]:
        if kind == 1:          # 卡爾弗特家族紋章：金黑相間，斜帶上顏色對調
            cid = "mdq%d%d" % (qx, qy)
            for i in range(6):
                s += rect(qx + i * 12.5, qy, 12.5, 50, "#000" if i % 2 else GOLD)
            s += '<clipPath id="%s"><polygon points="%g,%g %g,%g %g,%g %g,%g"/></clipPath><g clip-path="url(#%s)">' % (
                cid, qx, qy, qx + 18, qy, qx + 75, qy + 38, qx + 75, qy + 50, cid)
            for i in range(6):
                s += rect(qx + i * 12.5, qy, 12.5, 50, GOLD if i % 2 else "#000")
            s += '</g>'
        else:                  # 克羅斯蘭家族紋章：紅白四分，十字顏色對調
            for sx, sy, c in [(0, 0, RED), (37.5, 0, WHITE), (0, 25, WHITE), (37.5, 25, RED)]:
                o = WHITE if c == RED else RED
                x0, y0 = qx + sx, qy + sy
                s += rect(x0, y0, 37.5, 25, c)
                bx = qx + 34 if sx == 0 else qx + 37.5
                by = qy + 21.5 if sy == 0 else qy + 25
                s += rect(bx, y0 + (6 if sy == 0 else 0), 3.5, 19, o) + rect(x0 + (18 if sx == 0 else 0), by, 19.5, 3.5, o)
    return frame(s)


def F_MN():
    s = rect(0, 0, W, H, "#52c9e8")
    s += '<path d="M0,0 L44,0 L44,14 L58,44 L50,62 L60,100 L0,100 Z" fill="#002d5d"/>'
    return frame(s + star(24, 50, 12, WHITE, n=8))


def F_MS():
    s = rect(0, 0, W, H, "#cf2a27") + rect(30, 0, 90, H, "#ffd700") + rect(33, 0, 84, H, "#0f3e7a")
    for i in range(20):
        a = 2 * math.pi * i / 20 - math.pi / 2
        s += star(75 + 30 * math.cos(a), 50 + 30 * math.sin(a), 2.6)
    s += star(75, 20, 4.5, "#ffd700")
    for i in range(5):
        a = 2 * math.pi * i / 5 - math.pi / 2
        s += '<ellipse cx="%g" cy="%g" rx="7" ry="11" fill="%s" transform="rotate(%g %g %g)"/>' % (75 + 9 * math.cos(a), 52 + 9 * math.sin(a), WHITE, math.degrees(a) + 90, 75 + 9 * math.cos(a), 52 + 9 * math.sin(a))
    return frame(s + '<circle cx="75" cy="52" r="4" fill="#ffd700"/>')


def F_MO():
    s = rect(0, 0, W, 33.3, RED) + rect(0, 33.3, W, 33.4, WHITE) + rect(0, 66.7, W, 33.3, NAVY)
    s += '<circle cx="75" cy="50" r="24" fill="%s"/>' % NAVY
    for i in range(24):
        a = 2 * math.pi * i / 24
        s += star(75 + 20 * math.cos(a), 50 + 20 * math.sin(a), 1.8)
    return frame(s + seal(r=14, ring=WHITE))


def F_NV():
    s = rect(0, 0, W, H, "#003da5") + star(28, 30, 10, "#c0c0c0")
    s += '<path d="M10,14 Q28,6 46,14" fill="none" stroke="#ffd700" stroke-width="5"/>'
    s += text(28, 16, "BATTLE BORN", 4, "#003da5") + text(28, 50, "NEVADA", 7, "#c0c0c0")
    s += '<path d="M10,40 Q28,62 46,40" fill="none" stroke="#5a8a3a" stroke-width="2"/>'
    return frame(s)


def F_NM():
    s = rect(0, 0, W, H, "#ffd700") + '<circle cx="75" cy="50" r="10" fill="none" stroke="#bf0a30" stroke-width="5"/>'
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for off in (-6, -2, 2, 6):
            if dx:
                x1 = 75 + dx * 14
                s += '<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="#bf0a30" stroke-width="2.6"/>' % (x1, 50 + off, x1 + dx * (24 if abs(off) < 4 else 20), 50 + off)
            else:
                y1 = 50 + dy * 14
                s += '<line x1="%g" y1="%g" x2="%g" y2="%g" stroke="#bf0a30" stroke-width="2.6"/>' % (75 + off, y1, 75 + off, y1 + dy * (24 if abs(off) < 4 else 20))
    return frame(s)


def F_NC():
    s = rect(0, 0, 50, H, NAVY) + rect(50, 0, 100, 50, "#bf0a30") + rect(50, 50, 100, 50, WHITE)
    s += star(25, 49, 7) + text(10, 54, "N", 11, GOLD) + text(40, 54, "C", 11, GOLD)
    s += rect(8, 22, 34, 7, GOLD) + rect(8, 72, 34, 7, GOLD)
    return frame(s)


def F_OH():
    s = '<clipPath id="ohc"><path d="M0,0 L150,0 L120,50 L150,100 L0,100 Z"/></clipPath><g clip-path="url(#ohc)">'
    for i in range(5):
        s += rect(0, i * 20, W, 20, "#bf0a30" if i % 2 == 0 else WHITE)
    s += '</g><path d="M0,0 L66,50 L0,100 Z" fill="%s"/>' % NAVY
    s += '<circle cx="26" cy="50" r="10" fill="%s"/><circle cx="26" cy="50" r="6" fill="#bf0a30"/>' % WHITE
    for i in range(17):
        a = 2 * math.pi * i / 17
        s += star(26 + 18 * math.cos(a), 50 + 18 * math.sin(a), 1.8)
    return ('<path d="M0.5,0.5 L149.5,0.5 L120,50 L149.5,99.5 L0.5,99.5 Z" fill="none" stroke="#888"/>' + s, W, H)


def F_OK():
    s = rect(0, 0, W, H, "#5b9bd5") + '<ellipse cx="75" cy="48" rx="30" ry="22" fill="#d2b48c" stroke="#6b4226" stroke-width="1.5"/>'
    for x in (60, 75, 90):
        s += '<path d="M%g,40 v8 M%g,44 h8" stroke="#6b4226" stroke-width="1.5"/>' % (x, x - 4)
    s += '<line x1="45" y1="48" x2="105" y2="48" stroke="#5a3a1a" stroke-width="2"/>'
    return frame(s + text(75, 90, "OKLAHOMA", 10, WHITE))


def F_RI():
    s = rect(0, 0, W, H, WHITE)
    for i in range(13):
        a = 2 * math.pi * i / 13 - math.pi / 2
        s += star(75 + 34 * math.cos(a), 46 + 34 * math.sin(a), 3, GOLD)
    s += '<path d="M75,26 v38 M66,32 h18 M58,52 q17,20 34,0" fill="none" stroke="%s" stroke-width="4"/>' % GOLD
    s += '<circle cx="75" cy="24" r="4" fill="none" stroke="%s" stroke-width="2.5"/>' % GOLD
    s += rect(56, 74, 38, 10, "#1f4e9c") + text(75, 82, "HOPE", 7.5, GOLD)
    return frame(s)


def F_SC():
    s = rect(0, 0, W, H, "#002e6d") + '<path d="M18,14 A9,9 0 0 0 36,14" fill="none" stroke="%s" stroke-width="3"/>' % WHITE
    s += rect(82, 38, 6, 48, WHITE)
    for a in range(-80, 81, 20):
        r = math.radians(a)
        s += '<path d="M85,40 Q%g,%g %g,%g" fill="none" stroke="%s" stroke-width="3.5"/>' % (85 + 14 * math.sin(r), 30, 85 + 24 * math.sin(r), 40 + 10 * abs(math.sin(r)), WHITE)
    return frame(s)


def F_TN():
    s = rect(0, 0, W, H, "#cc0000") + rect(136, 0, 2, H, WHITE) + rect(138, 0, 12, H, "#002868")
    s += '<circle cx="68" cy="50" r="24" fill="#002868" stroke="%s" stroke-width="2.5"/>' % WHITE
    s += star(68, 37, 7) + star(57, 58, 7) + star(79, 58, 7)
    return frame(s)


def F_TX():
    s = rect(0, 0, 50, H, "#002868") + rect(50, 0, 100, 50, WHITE) + rect(50, 50, 100, 50, "#bf0a30")
    return frame(s + star(25, 50, 14))


def F_WA():
    s = rect(0, 0, W, H, "#00843d") + seal(r=30, ring=GOLD, fill="#f6e7a8")
    s += '<circle cx="75" cy="47" r="10" fill="#6b4226"/><path d="M60,68 q15,-18 30,0" fill="#6b4226"/>'
    return frame(s)


def F_WV():
    s = rect(0, 0, W, H, "#002e6d") + rect(5, 5, 140, 90, WHITE) + seal(r=20, ring="#5a8a3a", fill="#f4f4f4")
    return frame(s + text(75, 18, "STATE OF WEST VIRGINIA", 6.5, "#002e6d"))


def F_WY():
    s = rect(0, 0, W, H, "#bf0a30") + rect(5, 5, 140, 90, WHITE) + rect(10, 10, 130, 80, "#002868")
    s += '<path d="M45,52 q4,-20 30,-18 q22,0 30,8 l6,0 q4,6 0,12 l-6,2 q-2,12 -8,12 h-4 v-6 h-26 v6 h-6 q-8,-4 -6,-12 z" fill="%s"/>' % WHITE
    return frame(s + '<circle cx="78" cy="50" r="7" fill="#bf0a30"/>')


def F_UT():
    s = rect(0, 0, W, H, WHITE)
    s += '<polygon points="75,30 95,41 95,63 75,74 55,63 55,41" fill="#002868" stroke="%s" stroke-width="2"/>' % WHITE
    s += '<path d="M66,62 h18 l-2,-6 h-14 z M68,55 h14 l-2,-6 h-10 z M70,48 h10 a5,5 0 0 0 -10,0 z" fill="%s"/>' % GOLD
    return frame(s)


FLAGS = {
    "AL": F_AL, "AK": F_AK, "AZ": F_AZ, "AR": F_AR, "CA": F_CA, "CO": F_CO, "DE": F_DE, "FL": F_FL, "GA": F_GA,
    "HI": F_HI, "IN": F_IN, "IA": F_IA, "MD": F_MD, "MN": F_MN, "MS": F_MS, "MO": F_MO, "NV": F_NV, "NM": F_NM,
    "NC": F_NC, "OH": F_OH, "OK": F_OK, "RI": F_RI, "SC": F_SC, "TN": F_TN, "TX": F_TX, "WA": F_WA, "WV": F_WV,
    "WY": F_WY, "UT": lambda: F_UT(),
    "CT": lambda: generic(NAVY, bottom="QUI TRANSTULIT SUSTINET", ring=WHITE, fill="#ffffff"),
    "ID": lambda: generic(NAVY, bottom="STATE OF IDAHO", tc=GOLD),
    "IL": lambda: generic(WHITE, bottom="ILLINOIS", tc=NAVY, ring="#4a6b2a"),
    "KS": lambda: generic(NAVY, top="", bottom="KANSAS", tc=GOLD),
    "KY": lambda: generic(NAVY, top="COMMONWEALTH OF KENTUCKY", tc=GOLD),
    "LA": lambda: generic(NAVY, bottom="UNION JUSTICE CONFIDENCE", ring=WHITE, fill=NAVY, inner=WHITE),
    "ME": lambda: generic(NAVY, top="DIRIGO", bottom="MAINE", tc=GOLD),
    "MA": lambda: generic(WHITE, ring="#1f4e9c", fill="#1f4e9c", inner=GOLD),
    "MI": lambda: generic(NAVY, top="TUEBOR"),
    "MT": lambda: generic(NAVY, top="MONTANA", tc=GOLD),
    "NE": lambda: generic(NAVY, ring=GOLD, fill="#e8d9a8"),
    "NH": lambda: generic(NAVY, ring=GOLD),
    "NJ": lambda: generic("#e6c48a", ring="#5b91c6", fill="#5b91c6", inner=GOLD),
    "NY": lambda: generic(NAVY, bottom="EXCELSIOR", tc=WHITE),
    "ND": lambda: generic(NAVY, bottom="NORTH DAKOTA", ring="#8a6d3b", fill="#6b4226", inner=GOLD, tc="#e8c06a"),
    "OR": lambda: generic(NAVY, top="STATE OF OREGON", bottom="1859", tc=GOLD, fill=NAVY, inner=GOLD),
    "PA": lambda: generic(NAVY, ring=GOLD),
    "SD": lambda: generic("#5b9bd5", top="SOUTH DAKOTA", bottom="THE MOUNT RUSHMORE STATE", tc=GOLD),
    "VT": lambda: generic(NAVY, bottom="VERMONT", tc=GOLD, fill="#e9f0dc", inner="#4a6b2a"),
    "VA": lambda: generic(NAVY, bottom="VIRGINIA", ring=WHITE, fill="#ffffff", inner="#4a6b2a"),
    "WI": lambda: generic(NAVY, top="WISCONSIN", bottom="1848"),
}


def flag(c):
    return FLAGS[c]()
