# -*- coding: utf-8 -*-
"""把公開的邊界 GeoJSON 投影、簡化，寫成 ust_geo.py（美國各州）與 cnp_geo.py（中國各省）。

資料來源（下載到 geo/ 目錄後執行 python3 geoprep.py geo/）：
  美國：https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json
  中國：https://raw.githubusercontent.com/longwosion/geojson-map-china/master/china.json
  日本：https://raw.githubusercontent.com/dataofjapan/land/master/japan.geojson
  韓國：https://raw.githubusercontent.com/southkorea/southkorea-maps/master/kostat/2018/json/skorea-provinces-2018-geo.json（存成 korea.json）
  歐洲：https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_50m_admin_0_countries.geojson（存成 ne50.geojson）
"""
import io
import json
import math
import os
import sys

import geo_common as G


def dp(pts, tol):
    """Douglas-Peucker 折線簡化。"""
    if len(pts) < 3:
        return pts
    keep = [False] * len(pts)
    keep[0] = keep[-1] = True
    stack = [(0, len(pts) - 1)]
    while stack:
        a, b = stack.pop()
        ax, ay = pts[a]
        bx, by = pts[b]
        dx, dy = bx - ax, by - ay
        L = math.hypot(dx, dy) or 1e-9
        best, bi = -1, -1
        for i in range(a + 1, b):
            px, py = pts[i]
            d = abs(dy * (px - ax) - dx * (py - ay)) / L
            if d > best:
                best, bi = d, i
        if best > tol:
            keep[bi] = True
            stack += [(a, bi), (bi, b)]
    return [p for p, k in zip(pts, keep) if k]


def dpring(r, tol):
    """封閉環：先在離起點最遠的點切開，兩段各自簡化。"""
    if r[0] == r[-1]:
        r = r[:-1]
    if len(r) < 4:
        return r
    x0, y0 = r[0]
    k = max(range(len(r)), key=lambda i: (r[i][0] - x0) ** 2 + (r[i][1] - y0) ** 2)
    a = dp(r[:k + 1], tol)
    b = dp(r[k:] + [r[0]], tol)
    return a[:-1] + b[:-1]


def area(r):
    return abs(sum(r[i][0] * r[i - 1][1] - r[i - 1][0] * r[i][1] for i in range(len(r)))) / 2


def rings(geom):
    polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
    return [p[0] for p in polys]          # 只取外圈；這兩份資料沒有需要的內洞


def path(rs):
    out = []
    for r in rs:
        out.append("M" + "L".join("%d,%d" % (round(x), round(y)) for x, y in r) + "Z")
    return "".join(out)


def bbox(pts):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def write(name, doc, data):
    src = u"# -*- coding: utf-8 -*-\n\"\"\"%s（由 geoprep.py 產生，請勿手改）。\"\"\"\n" % doc
    for k, v in data:
        src += u"%s = %s\n" % (k, json.dumps(v, ensure_ascii=False, sort_keys=True) if not isinstance(v, str) else repr(v))
    io.open(name, "w", encoding="utf-8").write(src)


def prep_us(fn):
    d = json.load(io.open(fn, encoding="utf-8"))
    raw = {}
    for f in d["features"]:
        code = f["id"]
        part = code if code in ("AK", "HI") else "48"
        f_ = {"48": G._US48, "AK": G._USAK, "HI": G._USHI}[part]
        rs = []
        for r in rings(f["geometry"]):
            rs.append([f_(lon - 360 if lon > 0 else lon, lat) for lon, lat in r])
        raw[code] = (part, rs)
    K = G.US_K

    def pts(part):
        return [(x * K, -y * K) for c, (p, rs) in raw.items() if p == part for r in rs for x, y in r]
    b48 = bbox(pts("48"))
    sak = 0.35
    bak = bbox([(x * sak, y * sak) for x, y in pts("AK")])
    bhi = bbox(pts("HI"))
    m = 10
    # 本土 48 州放在 (m, m) 開始；阿拉斯加在左下，夏威夷在它右邊
    T = {"48": (1.0, m - b48[0], m - b48[1])}
    T["AK"] = (sak, m - bak[0], b48[3] - b48[1] + m - (bak[3] - bak[1]) + 10 - bak[1])
    akw = bak[2] - bak[0]
    T["HI"] = (1.0, m + akw + 8 - bhi[0], b48[3] - b48[1] + m - (bhi[3] - bhi[1]) + 28 - bhi[1])
    out, allp = {}, []
    for code, (part, rs) in sorted(raw.items()):
        s, dx, dy = T[part]
        rr = []
        for r in rs:
            q = [(x * K * s + dx, -y * K * s + dy) for x, y in r]
            if area(q) < (4 if code not in ("RI", "DE", "HI") else 0.3):
                continue
            q = dpring(q, 0.7)
            if len(q) >= 3:
                rr.append(q)
                allp += q
        out[code] = path(rr)
    bb = bbox(allp)
    W, H = int(bb[2] + m), int(bb[3] + m)
    write("ust_geo.py", u"美國各州的 SVG 路徑", [("US_VB", [W, H]), ("US_T", T), ("US_PATHS", out)])
    print("US", W, H, sum(len(v) for v in out.values()), "bytes")


CN_CODE = {"11": "BJ", "12": "TJ", "13": "HE", "14": "SX", "15": "NM", "21": "LN", "22": "JL", "23": "HL",
           "31": "SH", "32": "JS", "33": "ZJ", "34": "AH", "35": "FJ", "36": "JX", "37": "SD", "41": "HA",
           "42": "HB", "43": "HN", "44": "GD", "45": "GX", "46": "HI", "50": "CQ", "51": "SC", "52": "GZ",
           "53": "YN", "54": "XZ", "61": "SN", "62": "GS", "63": "QH", "64": "NX", "65": "XJ", "71": "TW",
           "81": "HK", "82": "MO"}


def prep_cn(fn):
    d = json.load(io.open(fn, encoding="utf-8"))
    raw = {}
    for f in d["features"]:
        code = CN_CODE[f["properties"]["id"]]
        raw[code] = [[G._CN(lon, lat) for lon, lat in r] for r in rings(f["geometry"])]
    K = G.CN_K
    allr = [(x * K, -y * K) for rs in raw.values() for r in rs for x, y in r]
    b = bbox(allr)
    m = 10
    T = (m - b[0], m - b[1])
    out, allp = {}, []
    for code, rs in sorted(raw.items()):
        rr = []
        for r in rs:
            q = [(x * K + T[0], -y * K + T[1]) for x, y in r]
            if area(q) < (3 if code not in ("HK", "MO") else 0.01):
                continue
            q = dpring(q, 0.6 if code not in ("HK", "MO") else 0.05)
            if len(q) >= 3:
                rr.append(q)
                allp += q
        out[code] = path(rr)
    bb = bbox(allp)
    W, H = int(bb[2] + m), int(bb[3] + m)
    write("cnp_geo.py", u"中國各省級行政區的 SVG 路徑", [("CN_VB", [W, H]), ("CN_T", list(T)), ("CN_PATHS", out)])
    print("CN", W, H, sum(len(v) for v in out.values()), "bytes")


def prep_jp(fn):
    d = json.load(io.open(fn, encoding="utf-8"))
    raw = {}
    for f in d["features"]:
        code = int(f["properties"]["id"])
        part = "oki" if code == 47 else "main"
        rs = []
        for r in rings(f["geometry"]):
            if part == "main" and min(lat for lon, lat in r) < 30.5:     # 小笠原等遠島不畫
                continue
            rs.append([G._JP(lon, lat) for lon, lat in r])
        raw[code] = (part, rs)
    K = G.JP_K

    def pts(part):
        return [(x * K, -y * K) for c, (p, rs) in raw.items() if p == part for r in rs for x, y in r]
    bm = bbox(pts("main"))
    m = 10
    T = {"main": (1.0, m - bm[0], m - bm[1])}
    bo = bbox(pts("oki"))
    # 沖繩放在左上角（日本海一帶的空白處），外加框線
    T["oki"] = (1.0, m + 8 - bo[0], m + 8 - bo[1])
    out, allp = {}, []
    for code, (part, rs) in sorted(raw.items()):
        s, dx, dy = T[part]
        rr = []
        for r in rs:
            q = [(x * K * s + dx, -y * K * s + dy) for x, y in r]
            if area(q) < (2.5 if code != 47 else 0.8):
                continue
            q = dpring(q, 0.55)
            if len(q) >= 3:
                rr.append(q)
                allp += q
        out["%02d" % code] = path(rr)
    bb = bbox(allp)
    W, H = int(bb[2] + m), int(bb[3] + m)
    write("jpp_geo.py", u"日本各都道府縣的 SVG 路徑", [("JP_VB", [W, H]), ("JP_T", T), ("JP_PATHS", out)])
    print("JP", W, H, sum(len(v) for v in out.values()), "bytes")


def prep_kr(fn):
    d = json.load(io.open(fn, encoding="utf-8"))
    raw = {}
    for f in d["features"]:
        geom = f["geometry"]
        polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        # 保留內圈：光州廣域市是全羅南道裡的一個「洞」
        raw[f["properties"]["code"]] = [[G._KR(lon, lat) for lon, lat in r] for p in polys for r in p]
    K = G.KR_K
    b = bbox([(x * K, -y * K) for rs in raw.values() for r in rs for x, y in r])
    m = 10
    T = (m - b[0], m - b[1])
    out, allp = {}, []
    for code, rs in sorted(raw.items()):
        rr = []
        for r in rs:
            q = [(x * K + T[0], -y * K + T[1]) for x, y in r]
            if area(q) < 1.5:
                continue
            q = dpring(q, 0.6)
            if len(q) >= 3:
                rr.append(q)
                allp += q
        out[code] = path(rr)
    bb = bbox(allp)
    W, H = int(bb[2] + m), int(bb[3] + m)
    write("krp_geo.py", u"韓國各市道的 SVG 路徑", [("KR_VB", [W, H]), ("KR_T", list(T)), ("KR_PATHS", out)])
    print("KR", W, H, sum(len(v) for v in out.values()), "bytes")


def clip_rect(r, x0, y0, x1, y1):
    """Sutherland–Hodgman：把多邊形裁切到矩形內。"""
    def clip(pts, inside, inter):
        out = []
        for i in range(len(pts)):
            a, b = pts[i - 1], pts[i]
            ia, ib = inside(a), inside(b)
            if ib:
                if not ia:
                    out.append(inter(a, b))
                out.append(b)
            elif ia:
                out.append(inter(a, b))
        return out

    def ix(xv):
        return lambda a, b: (xv, a[1] + (b[1] - a[1]) * (xv - a[0]) / ((b[0] - a[0]) or 1e-9))

    def iy(yv):
        return lambda a, b: (a[0] + (b[0] - a[0]) * (yv - a[1]) / ((b[1] - a[1]) or 1e-9), yv)
    pts = r
    for ins, inter in [(lambda p: p[0] >= x0, ix(x0)), (lambda p: p[0] <= x1, ix(x1)),
                       (lambda p: p[1] >= y0, iy(y0)), (lambda p: p[1] <= y1, iy(y1))]:
        if not pts:
            break
        pts = clip(pts, ins, inter)
    return pts


EU_MAIN = ("ALB AND AUT BEL BGR BIH BLR CHE CYP CZE DEU DNK ESP EST FIN FRA GBR GRC HRV HUN IRL ISL ITA KOS LIE LTU LUX LVA MCO MDA "
           "MKD MLT MNE NLD NOR POL PRT ROU RUS SMR SRB SVK SVN SWE TUR UKR VAT").split()
EU_MERGE = {"ALD": "FIN", "FRO": "DNK", "CYN": "CYP"}


def prep_eu(fn):
    d = json.load(io.open(fn, encoding="utf-8"))
    K = G.EU_K
    # 視窗：西到冰島、東到東經 45 度、南到北緯 34 度、北到北緯 71.5 度
    corners = [G._EU(lon, lat) for lon in (-25, -10, 15, 30, 45) for lat in (34, 71.5)]
    xs = [x * K for x, y in corners]
    ys = [-y * K for x, y in corners]
    X0, X1 = G._EU(-25, 60)[0] * K, G._EU(45, 45)[0] * K
    Y0, Y1 = -G._EU(15, 71.5)[1] * K, -G._EU(15, 34)[1] * K
    m = 0
    T = (-X0, -Y0)
    W, H = int(X1 - X0), int(Y1 - Y0)
    main, ctx = {}, []
    for f in d["features"]:
        a3 = f["properties"]["ADM0_A3"]
        a3 = EU_MERGE.get(a3, a3)
        geom = f["geometry"]
        polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        rr = []
        for p in polys:
            for r in p:
                if a3 == "RUS" and all(32.3 < lon < 36.8 and 44.2 < lat < 46.3 for lon, lat in r):
                    # 克里米亞：依國際普遍承認的邊界畫入烏克蘭（2014 年起由俄羅斯實際控制，課文中說明）
                    q = [(G._EU(lon, lat)[0] * K + T[0], -G._EU(lon, lat)[1] * K + T[1]) for lon, lat in r]
                    main.setdefault("UKR", []).append(dpring(q, 0.5))
                    continue
                q = [(G._EU(lon, lat)[0] * K + T[0], -G._EU(lon, lat)[1] * K + T[1]) for lon, lat in r]
                q = clip_rect(q, -2, -2, W + 2, H + 2)
                if len(q) < 3 or area(q) < (0.3 if a3 in ("VAT", "MCO", "SMR", "LIE", "AND", "MLT", "LUX") else 1.2):
                    continue
                q = dpring(q, 0.5 if a3 not in ("VAT", "MCO", "SMR") else 0.05)
                if len(q) >= 3:
                    rr.append(q)
        if not rr:
            continue
        if a3 in EU_MAIN:
            main.setdefault(a3, []).extend(rr)
        else:
            ctx.extend(rr)
    out = {k: path(v) for k, v in main.items()}
    write("eup_geo.py", u"歐洲各國的 SVG 路徑", [("EU_VB", [W, H]), ("EU_T", list(T)), ("EU_PATHS", out), ("EU_CTX", path(ctx))])
    print("EU", W, H, sum(len(v) for v in out.values()), len(path(ctx)), "bytes", sorted(set(EU_MAIN) - set(out)))


if __name__ == "__main__":
    g = sys.argv[1]
    prep_us(os.path.join(g, "us-states.json"))
    prep_cn(os.path.join(g, "china.json"))
    prep_jp(os.path.join(g, "japan.geojson"))
    prep_kr(os.path.join(g, "korea.json"))
    prep_eu(os.path.join(g, "ne50.geojson"))
