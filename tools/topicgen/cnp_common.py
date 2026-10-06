# -*- coding: utf-8 -*-
"""〈中國各省〉（cnp_）共用資料、地圖與每課的組裝工具。"""
from cc_common import *
from geo_common import cn_xy, centroid, bbox_of, static_map, legend, geolib, HL as HL_, NEAR as NEAR_, BASE as BASE_
from cnp_geo import CN_VB, CN_PATHS

CP_NOTE = (u"本課程是<strong>地理、文化與旅遊的入門介紹</strong>。人口為 2020 年第七次全國人口普查數字（香港、澳門為同年官方數字），"
           u"面積為約略值；世界遺產以截至 2025 年的名錄為準。地圖已簡化，僅供看位置，不代表對任何疆界爭議的立場。")

TW_AREA = 3.62       # 萬平方公里

REGIONS = {"N": (u"華北", "#3a6ea5"), "NE": (u"東北", "#5b8fb9"), "E": (u"華東", "#2e8b57"), "C": (u"華中", "#b7791f"),
           "S": (u"華南", "#c0504d"), "SW": (u"西南", "#8e5aa8"), "NW": (u"西北", "#a0522d")}

# code: (名稱, 簡稱, 類型, 區域, 省會, (緯度, 經度), 面積(萬 km²), 人口(萬, 2020), 鄰接)
BASIC = {
    "BJ": (u"北京市", u"京", u"直轄市", "N", u"北京", (39.90, 116.40), 1.64, 2189, "TJ HE"),
    "TJ": (u"天津市", u"津", u"直轄市", "N", u"天津", (39.13, 117.20), 1.20, 1387, "BJ HE"),
    "HE": (u"河北省", u"冀", u"省", "N", u"石家莊", (38.04, 114.51), 18.88, 7461, "BJ TJ SD HA SX NM LN"),
    "SX": (u"山西省", u"晉", u"省", "N", u"太原", (37.87, 112.55), 15.67, 3492, "HE HA SN NM"),
    "NM": (u"內蒙古自治區", u"內蒙古", u"自治區", "N", u"呼和浩特", (40.84, 111.75), 118.3, 2405, "HL JL LN HE SX SN NX GS"),
    "LN": (u"遼寧省", u"遼", u"省", "NE", u"瀋陽", (41.80, 123.43), 14.8, 4259, "JL HE NM"),
    "JL": (u"吉林省", u"吉", u"省", "NE", u"長春", (43.82, 125.32), 18.74, 2407, "HL LN NM"),
    "HL": (u"黑龍江省", u"黑", u"省", "NE", u"哈爾濱", (45.80, 126.53), 47.3, 3185, "JL NM"),
    "SH": (u"上海市", u"滬（又稱申）", u"直轄市", "E", u"上海", (31.23, 121.47), 0.63, 2487, "JS ZJ"),
    "JS": (u"江蘇省", u"蘇", u"省", "E", u"南京", (32.06, 118.80), 10.72, 8475, "SH ZJ AH SD"),
    "ZJ": (u"浙江省", u"浙", u"省", "E", u"杭州", (30.27, 120.15), 10.55, 6457, "SH JS AH JX FJ"),
    "AH": (u"安徽省", u"皖", u"省", "E", u"合肥", (31.82, 117.23), 14.01, 6103, "JS ZJ JX HB HA SD"),
    "FJ": (u"福建省", u"閩", u"省", "E", u"福州", (26.07, 119.30), 12.4, 4154, "ZJ JX GD"),
    "JX": (u"江西省", u"贛", u"省", "E", u"南昌", (28.68, 115.86), 16.69, 4519, "ZJ FJ GD HN HB AH"),
    "SD": (u"山東省", u"魯", u"省", "E", u"濟南", (36.65, 117.12), 15.79, 10153, "HE HA AH JS"),
    "HA": (u"河南省", u"豫", u"省", "C", u"鄭州", (34.75, 113.62), 16.7, 9937, "HE SX SN HB AH SD"),
    "HB": (u"湖北省", u"鄂", u"省", "C", u"武漢", (30.59, 114.30), 18.59, 5775, "HA AH JX HN CQ SN"),
    "HN": (u"湖南省", u"湘", u"省", "C", u"長沙", (28.23, 112.94), 21.18, 6644, "HB JX GD GX GZ CQ"),
    "GD": (u"廣東省", u"粵", u"省", "S", u"廣州", (23.13, 113.26), 17.97, 12601, "FJ JX HN GX HK MO"),
    "GX": (u"廣西壯族自治區", u"桂", u"自治區", "S", u"南寧", (22.82, 108.37), 23.76, 5013, "GD HN GZ YN"),
    "HI": (u"海南省", u"瓊", u"省", "S", u"海口", (20.04, 110.20), 3.54, 1008, ""),
    "HK": (u"香港特別行政區", u"港", u"特別行政區", "S", u"—", (22.28, 114.16), 0.11, 747, "GD"),
    "MO": (u"澳門特別行政區", u"澳", u"特別行政區", "S", u"—", (22.19, 113.54), 0.0033, 68.3, "GD"),
    "CQ": (u"重慶市", u"渝", u"直轄市", "SW", u"重慶", (29.56, 106.55), 8.24, 3205, "SC GZ HN HB SN"),
    "SC": (u"四川省", u"川（又稱蜀）", u"省", "SW", u"成都", (30.57, 104.07), 48.6, 8367, "CQ GZ YN XZ QH GS SN"),
    "GZ": (u"貴州省", u"黔（又稱貴）", u"省", "SW", u"貴陽", (26.65, 106.63), 17.62, 3856, "CQ SC YN GX HN"),
    "YN": (u"雲南省", u"滇（又稱雲）", u"省", "SW", u"昆明", (25.04, 102.71), 39.41, 4721, "SC GZ GX XZ"),
    "XZ": (u"西藏自治區", u"藏", u"自治區", "SW", u"拉薩", (29.65, 91.13), 122.8, 365, "XJ QH SC YN"),
    "SN": (u"陝西省", u"陝（又稱秦）", u"省", "NW", u"西安", (34.34, 108.94), 20.56, 3953, "SX HA HB CQ SC GS NX NM"),
    "GS": (u"甘肅省", u"甘（又稱隴）", u"省", "NW", u"蘭州", (36.06, 103.83), 42.58, 2502, "NM NX SN SC QH XJ"),
    "QH": (u"青海省", u"青", u"省", "NW", u"西寧", (36.62, 101.78), 72.23, 592, "GS SC XZ XJ"),
    "NX": (u"寧夏回族自治區", u"寧", u"自治區", "NW", u"銀川", (38.49, 106.23), 6.64, 720, "NM SN GS"),
    "XJ": (u"新疆維吾爾自治區", u"新", u"自治區", "NW", u"烏魯木齊", (43.83, 87.62), 166.49, 2585, "GS QH XZ"),
}

ORDER = ["BJ", "TJ", "HE", "SX", "NM", "LN", "JL", "HL", "SH", "JS", "ZJ", "AH", "FJ", "JX", "SD", "HA", "HB", "HN",
         "GD", "GX", "HI", "HK", "MO", "CQ", "SC", "GZ", "YN", "XZ", "SN", "GS", "QH", "NX", "XJ"]
LESSON = {c: i + 5 for i, c in enumerate(ORDER)}          # 第 5～37 課
SMALL = {"BJ", "TJ", "SH", "HK", "MO", "NX", "HI"}
SHORTN = {"NM": u"內蒙古", "GX": u"廣西", "XZ": u"西藏", "NX": u"寧夏", "XJ": u"新疆", "HK": u"香港", "MO": u"澳門"}


def nm(c):
    return BASIC[c][0]


def short(c):
    return SHORTN.get(c, BASIC[c][0][:-1])


def cap_xy(c):
    lat, lon = BASIC[c][5]
    return cn_xy(lon, lat)


def wan(x):
    if x >= 100:
        return u"約 %s 萬" % format(int(round(x)), ",")
    return u"約 %.1f 萬" % x


def area_txt(a):
    r = a / TW_AREA
    if a < 0.05:
        return u"約 %d 平方公里（約台北市的八分之一）" % round(a * 10000)
    if a < 1:
        return u"約 %s 平方公里（約台灣的 %d%%）" % (format(int(round(a * 10000, -1)), ","), round(r * 100))
    cmp_ = (u"約台灣的 %.1f 倍" % r) if r >= 1.15 else (u"和台灣差不多大" if r >= 0.85 else u"約台灣的 %d%%" % round(r * 100))
    return u"約 %s 萬平方公里（%s）" % (("%.2f" % a).rstrip("0").rstrip("."), cmp_)


# ---------- 地圖 ----------
TW_FILL = "#e3e7ec"


def _tw_extra(label=True):
    """台灣：只畫淺灰色輪廓作為地理參考。"""
    s = '<path d="%s" fill="%s" stroke="#9aa5b1" stroke-width="0.8" stroke-dasharray="2 2"/>' % (CN_PATHS["TW"], TW_FILL)
    if label:
        x0, y0, x1, y1 = bbox_of(CN_PATHS["TW"])
        s += ('<text x="%d" y="%d" font-size="10" fill="var(--text-muted)" stroke="var(--surface)" stroke-width="3" paint-order="stroke">台灣</text>'
              % (x1 + 4, (y0 + y1) / 2 + 4))
    return s


PATHS = {k: v for k, v in CN_PATHS.items() if k != "TW"}


def locmap(c):
    near = BASIC[c][8].split()
    lx, ly = centroid(PATHS[c])
    x0, y0, x1, y1 = bbox_of(PATHS[c])
    small = c in SMALL
    if c in ("HK", "MO"):
        lab = (short(c), x1 + 40 if c == "HK" else x0 - 40, y1 + 26)
    elif small:
        lab = (short(c), x1 + 34, (y0 + y1) / 2 + 5)
    else:
        lab = (short(c), lx, ly + 18 if (y1 - y0) > 40 else y0 - 6)
    star = None if c in ("HK", "MO") else cap_xy(c)
    g, vb = static_map(CN_VB, PATHS, c, near, star=star, label=lab, small=small, extra=_tw_extra())
    capn = {u"省": u"省會", u"自治區": u"首府"}.get(BASIC[c][2], u"市中心")
    items = [(HL_, short(c))] + ([(NEAR_, u"鄰接省區")] if near else []) + ([("star", capn + u" " + BASIC[c][4])] if star else [])
    g += legend(14, CN_VB[1] - 10, items)
    cap = u"%s的位置（紅色）。" % nm(c) + (u"橘色是相鄰的省級行政區。" if near else u"") + (u"★ 是%s。" % capn if star else u"") + \
        (u"香港在珠江口東側、澳門在西側，兩地由 2018 年通車的港珠澳大橋相連。" if c in ("HK", "MO") else u"")
    figs = [("fig", g, vb, cap)]
    return figs


def overview_map(fill, labels=(), cap=u"", legend_items=None, extra=""):
    g = [_tw_extra()]
    for k, d in sorted(PATHS.items()):
        g.append('<path d="%s" fill="%s" stroke="var(--surface)" stroke-width="0.8"/>' % (d, fill.get(k, BASE_)))
    g.append(extra)
    for t, x, y in labels:
        g.append('<text x="%d" y="%d" font-size="11" text-anchor="middle" fill="var(--text)" stroke="var(--surface)" '
                 'stroke-width="3" paint-order="stroke">%s</text>' % (x, y, t))
    if legend_items:
        g.append(legend(14, CN_VB[1] - 10, legend_items))
    return ("fig", "\n".join(g), "0 0 %d %d" % tuple(CN_VB), cap)


def name_labels(skip=("HK", "MO", "TJ", "BJ", "SH")):
    out = []
    for c in ORDER:
        if c in skip:
            continue
        x, y = centroid(PATHS[c])
        out.append((BASIC[c][1][0] if c != "NM" else u"蒙", x, y + 4))
    return out


def _dataset():
    items = []
    for c in ORDER:
        b = BASIC[c]
        x, y = centroid(PATHS[c])
        items.append({"c": c, "n": short(c), "e": b[0], "p": PATHS[c], "x": int(x), "y": int(y), "L": LESSON[c], "g": b[3],
                      "v": {"pop": b[7], "area": round(b[6], 2), "den": round(b[7] / b[6], 0) if b[6] else 0},
                      "f": [[u"簡稱", b[1]], [u"省會", b[4]], [u"類型", b[2]], [u"人口", wan(b[7])], [u"面積", u"%s 萬 km²" % b[6]]]})
    return {"vb": CN_VB, "items": items, "unit": u"省區", "groups": {k: list(v) for k, v in REGIONS.items()},
            "extra": _tw_extra(),
            "metrics": [["pop", u"人口", u"萬人", 0, u"2020 年第七次人口普查。台灣約 2,340 萬人。"],
                        ["area", u"面積", u"萬 km²", 2, u"台灣約 3.6 萬平方公里。"],
                        ["den", u"人口密度", u"人/km²", 0, u"台灣約每平方公里 650 人。"]]}


CPLIB = geolib("__cnpLib", _dataset())


def cpw(cfg, maxw=760):
    return wdg("__cnpLib-w", cfg, maxw)


cplesson = make_lesson(u"🗺️", CP_NOTE, CPLIB, "__cnpLib-w")


# ---------- 每省一課 ----------
DATA = {}


def prov_lesson(c, d):
    DATA[c] = d
    """d：sub、one、abbr(簡稱由來)、cities、geo、hist、lang、snack、wh、ich、season、days、route、myth、q"""
    b = BASIC[c]
    name = b[0]
    is_sar = c in ("HK", "MO")
    rows = [[u"類型", b[2]], [u"簡稱", b[1] + (u"：" + d["abbr"] if d.get("abbr") else u"")],
            [u"省會" if b[2] == u"省" else (u"首府" if b[2] == u"自治區" else u"政府所在地"), d.get("capital", b[4])],
            [u"面積", area_txt(b[6])], [u"人口（2020）", wan(b[7]) + u"人"], [u"所屬地理分區", REGIONS[b[3]][0]],
            [u"鄰接", u"、".join(nm(x) for x in b[8].split()) or u"四面環海，不和其他省區陸地相鄰"]]
    if is_sar:
        rows = [r for r in rows if r[0] not in (u"政府所在地",)]
    body = list(locmap(c))
    body += [("note", u"💡 一句話記住%s" % short(c), [("p", d["one"])]),
             ("h", u"基本資料"), ("t", [u"項目", u"內容"], rows),
             ("h", u"大城市與古稱"), ("t", [u"城市", u"古稱／別稱", u"特色"], [list(r) for r in d["cities"]]),
             ("h", u"地理"), ("p", d["geo"]),
             ("h", u"歷史沿革"), ("ul", d["hist"]),
             ("h", u"方言與民族"), ("p", d["lang"]),
             ("h", u"代表小吃"), ("ul", [u"<strong>%s</strong>：%s" % r for r in d["snack"]]),
             ("h", u"世界遺產")]
    body.append(("ul", d["wh"]) if d["wh"] else ("p", u"目前沒有列入名錄的世界遺產。" + d.get("wh_note", u"")))
    if d["wh"] and d.get("wh_note"):
        body.append(("p", d["wh_note"]))
    body += [("h", u"非物質文化遺產"), ("ul", d["ich"]),
             ("h", u"旅遊建議"), ("t", [u"項目", u"建議"], [[u"最佳季節", d["season"]], [u"建議天數", d["days"]], [u"經典路線", d["route"]]]),
             ("note", u"🤔 常見誤解", [("ul", d["myth"])])]
    goals = [u"在地圖上找到%s，說出簡稱、%s和鄰接省區" % (short(c), u"省會" if not is_sar else u"位置"),
             u"認識%s的大城市、古稱、地理與歷史" % short(c), u"知道%s的小吃、世界遺產、非遺與旅遊重點" % short(c)]
    point = d.get("pt") or (d["one"] + (u" 簡稱「%s」，省會%s。" % (b[1][0], b[4]) if not is_sar else u""))
    check = [u"%s的簡稱是什麼？%s" % (short(c), u"省會在哪裡？" if not is_sar else u"位在哪裡？"), u"%s有哪些世界遺產或非物質文化遺產？舉一個例子。" % short(c), d["q"]]
    title_ = u"%s：%s" % (short(c), d["sub"])
    return cplesson(title_, d.get("desc", d["sub"]), goals, body, point, check)


def P(c, **d):
    return prov_lesson(c, d)
