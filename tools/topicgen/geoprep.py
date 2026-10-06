# -*- coding: utf-8 -*-
"""把公開的邊界 GeoJSON 投影、簡化，寫成 ust_geo.py（美國各州）與 cnp_geo.py（中國各省）。

資料來源（下載到 geo/ 目錄後執行 python3 geoprep.py geo/）：
  美國：https://raw.githubusercontent.com/python-visualization/folium/main/examples/data/us-states.json
  中國：https://raw.githubusercontent.com/longwosion/geojson-map-china/master/china.json
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


if __name__ == "__main__":
    g = sys.argv[1]
    prep_us(os.path.join(g, "us-states.json"))
    prep_cn(os.path.join(g, "china.json"))
