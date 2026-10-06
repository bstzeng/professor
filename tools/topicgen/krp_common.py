# -*- coding: utf-8 -*-
"""〈韓國各市道〉（krp_）共用資料、地圖與每課的組裝工具。"""
from cc_common import *
from geo_common import kr_xy, centroid, bbox_of, static_map, legend, geolib, rings_of, _area_c, HL as HL_, NEAR as NEAR_, BASE as BASE_
from krp_geo import KR_VB, KR_PATHS

KR_NOTE = (u"本課程是<strong>地理、文化與旅遊的入門介紹</strong>。人口為 2024 年前後的住民登錄人口約略值，面積為約略值；"
           u"世界遺產以截至 2025 年的名錄為準，航班與交通資訊可能變動，出發前請再確認。地圖使用 2018 年的行政區資料並經簡化，"
           u"2023 年軍威郡由慶尚北道改隸大邱的變動沒有反映在地圖上。")

TW_AREA = 36197

REGIONS = {"SG": (u"首都圈", "#c0392b"), "GW": (u"江原", "#2e8b57"), "CC": (u"忠清", "#d68910"), "HN": (u"湖南（全羅）", "#8e5aa8"),
           "YN": (u"嶺南（慶尚）", "#3a6ea5"), "JJ": (u"濟州", "#16a085")}

# code: (名稱, 韓文, 羅馬拼音, 類型, 地區, 廳舍所在地, (緯度, 經度), 面積 km², 人口(萬), 鄰接)
BASIC = {
    "11": (u"首爾特別市", u"서울특별시", "Seoul", u"特別市", "SG", u"中區", (37.566, 126.978), 605, 940, "23 31"),
    "23": (u"仁川廣域市", u"인천광역시", "Incheon", u"廣域市", "SG", u"南洞區", (37.456, 126.705), 1067, 300, "11 31"),
    "31": (u"京畿道", u"경기도", "Gyeonggi-do", u"道", "SG", u"水原市", (37.289, 127.054), 10199, 1363, "11 23 32 33 34"),
    "32": (u"江原特別自治道", u"강원특별자치도", "Gangwon", u"特別自治道", "GW", u"春川市", (37.885, 127.730), 16830, 152, "31 33 37"),
    "25": (u"大田廣域市", u"대전광역시", "Daejeon", u"廣域市", "CC", u"西區", (36.350, 127.385), 540, 144, "29 33 34"),
    "29": (u"世宗特別自治市", u"세종특별자치시", "Sejong", u"特別自治市", "CC", u"世宗市", (36.480, 127.289), 465, 39, "25 33 34"),
    "33": (u"忠清北道", u"충청북도", "Chungcheongbuk-do", u"道", "CC", u"清州市", (36.635, 127.491), 7407, 159, "25 29 31 32 34 35 37"),
    "34": (u"忠清南道", u"충청남도", "Chungcheongnam-do", u"道", "CC", u"洪城郡（內浦新都市）", (36.659, 126.673), 8247, 213, "25 29 31 33 35"),
    "24": (u"光州廣域市", u"광주광역시", "Gwangju", u"廣域市", "HN", u"西區", (35.160, 126.851), 501, 142, "36"),
    "35": (u"全北特別自治道", u"전북특별자치도", "Jeonbuk", u"特別自治道", "HN", u"全州市", (35.820, 127.109), 8072, 175, "33 34 36 37 38"),
    "36": (u"全羅南道", u"전라남도", "Jeollanam-do", u"道", "HN", u"務安郡（南岳新都市）", (34.816, 126.463), 12348, 180, "24 35 38"),
    "21": (u"釜山廣域市", u"부산광역시", "Busan", u"廣域市", "YN", u"蓮堤區", (35.180, 129.075), 770, 330, "26 38"),
    "22": (u"大邱廣域市", u"대구광역시", "Daegu", u"廣域市", "YN", u"中區", (35.871, 128.601), 1499, 237, "37 38"),
    "26": (u"蔚山廣域市", u"울산광역시", "Ulsan", u"廣域市", "YN", u"南區", (35.539, 129.311), 1062, 110, "21 37 38"),
    "37": (u"慶尚北道", u"경상북도", "Gyeongsangbuk-do", u"道", "YN", u"安東市（慶北道廳新都市）", (36.576, 128.505), 18420, 255, "22 26 32 33 35 38"),
    "38": (u"慶尚南道", u"경상남도", "Gyeongsangnam-do", u"道", "YN", u"昌原市", (35.238, 128.692), 10541, 325, "21 22 26 35 36 37"),
    "39": (u"濟州特別自治道", u"제주특별자치도", "Jeju", u"特別自治道", "JJ", u"濟州市", (33.489, 126.498), 1850, 67, ""),
}

ORDER = ["11", "23", "31", "32", "25", "29", "33", "34", "24", "35", "36", "21", "22", "26", "37", "38", "39"]
LESSON = {c: i + 4 for i, c in enumerate(ORDER)}          # 第 4～20 課
SMALL = {"11", "25", "29", "24", "22", "26", "21", "23"}
SHORT = {"11": u"首爾", "23": u"仁川", "31": u"京畿", "32": u"江原", "25": u"大田", "29": u"世宗", "33": u"忠北", "34": u"忠南", "24": u"光州",
         "35": u"全北", "36": u"全南", "21": u"釜山", "22": u"大邱", "26": u"蔚山", "37": u"慶北", "38": u"慶南", "39": u"濟州"}


def nm(c):
    return BASIC[c][0]


def short(c):
    return SHORT[c]


def office(c):
    return u"市廳" if BASIC[c][3] in (u"特別市", u"廣域市", u"特別自治市") else u"道廳"


def cap_xy(c):
    lat, lon = BASIC[c][6]
    return kr_xy(lon, lat)


def wan(x):
    if x >= 100:
        return u"約 %s 萬" % format(int(round(x)), ",")
    return u"約 %d 萬" % round(x)


def area_txt(a):
    r = a / float(TW_AREA)
    if r < 0.05:
        return u"%s 平方公里（約台北市的 %.1f 倍）" % (format(a, ","), a / 272.0)
    return u"%s 平方公里（約台灣的 %d%%）" % (format(a, ","), round(r * 100))


# ---------- 地圖 ----------
def locmap(c):
    near = BASIC[c][9].split()
    lx, ly = centroid(KR_PATHS[c])
    x0, y0, x1, y1 = bbox_of(KR_PATHS[c])
    small = c in SMALL
    if small:
        a, cx, cy = max((_area_c(r) for r in rings_of(KR_PATHS[c])), key=lambda t: t[0])
        lab = (short(c), cx + (46 if c not in ("23",) else -48), cy + 28)
    else:
        lab = (short(c), lx, ly + 18)
    star = cap_xy(c)
    g, vb = static_map(KR_VB, KR_PATHS, c, near, star=star, label=lab)
    if small:
        g += '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="2"/>' % (cx, cy, max(14, (x1 - x0) / 2 + 6), HL_)
    items = [(HL_, short(c))] + ([(NEAR_, u"鄰接")] if near else []) + [("star", office(c))]
    g += legend(KR_VB[0] - 220, KR_VB[1] - 14, items)
    cap = u"%s的位置（紅色）。" % nm(c) + (u"橘色是陸地相鄰的市道。" if near else u"") + u"★ 是%s所在地。" % office(c)
    return ("fig", g, vb, cap)


def overview_map(fill, labels=(), cap=u"", legend_items=None):
    g = []
    for k, d in sorted(KR_PATHS.items()):
        g.append('<path d="%s" fill="%s" fill-rule="evenodd" stroke="var(--surface)" stroke-width="0.8"/>' % (d, fill.get(k, BASE_)))
    for t, x, y in labels:
        g.append('<text x="%d" y="%d" font-size="12" text-anchor="middle" fill="var(--text)" stroke="var(--surface)" '
                 'stroke-width="3" paint-order="stroke">%s</text>' % (x, y, t))
    if legend_items:
        rows = [legend_items[:3], legend_items[3:]] if len(legend_items) > 3 else [legend_items]
        for i, row in enumerate(rows):
            g.append(legend(KR_VB[0] - 250, KR_VB[1] - 14 - 16 * (len(rows) - 1 - i), row))
    return ("fig", "\n".join(g), "0 0 %d %d" % tuple(KR_VB), cap)


def labels(skip=()):
    out = []
    for c in ORDER:
        if c in skip:
            continue
        x, y = centroid(KR_PATHS[c])
        out.append((short(c), x, y + 4))
    return out


def _dataset():
    items = []
    for c in ORDER:
        b = BASIC[c]
        x, y = centroid(KR_PATHS[c])
        items.append({"c": c, "n": b[0], "e": u"%s　%s" % (b[1], b[2]), "p": KR_PATHS[c], "x": int(x), "y": int(y), "L": LESSON[c], "g": b[4],
                      "v": {"pop": b[8], "area": b[7], "den": round(b[8] * 10000 / b[7])},
                      "f": [[u"類型", b[3]], [office(c), b[5]], [u"人口", wan(b[8])], [u"面積", u"%s km²" % format(b[7], ",")]]})
    return {"vb": KR_VB, "items": items, "unit": u"市道", "groups": {k: list(v) for k, v in REGIONS.items()},
            "metrics": [["pop", u"人口", u"萬人", 0, u"台灣約 2,340 萬人。"], ["area", u"面積", u"km²", 0, u"台灣約 36,000 平方公里。"],
                        ["den", u"人口密度", u"人/km²", 0, u"台灣約每平方公里 650 人。"]]}


KRLIB = geolib("__krpLib", _dataset())


def krw(cfg, maxw=640):
    return wdg("__krpLib-w", cfg, maxw)


krlesson = make_lesson(u"🇰🇷", KR_NOTE, KRLIB, "__krpLib-w")

DATA = {}


def kr_lesson(c, d):
    """d：sub、one、origin、cities、geo、hist、dialect、food、omiyage、wh、fest、season、days、route、access、myth、fun、q"""
    DATA[c] = d
    b = BASIC[c]
    rows = [[u"韓文", u"%s（%s）" % (b[1], b[2])], [u"類型", b[3]], [u"地區", REGIONS[b[4]][0]], [office(c) + u"所在地", b[5]],
            [u"面積", area_txt(b[7])], [u"人口", wan(b[8]) + u"人"], [u"名稱由來", d["origin"]],
            [u"陸地鄰接", u"、".join(nm(x) for x in b[9].split()) or u"無（四面環海）"]]
    body = [locmap(c),
            ("note", u"💡 一句話記住%s" % short(c), [("p", d["one"])]),
            ("h", u"基本資料"), ("t", [u"項目", u"內容"], rows),
            ("h", u"主要地區與觀光地"), ("t", [u"地點", u"特色"], [list(r) for r in d["cities"]]),
            ("h", u"地理與氣候"), ("p", d["geo"]),
            ("h", u"歷史重點"), ("ul", d["hist"]),
            ("h", u"方言"), ("p", d["dialect"]),
            ("h", u"美食與伴手禮"), ("ul", [u"<strong>%s</strong>：%s" % r for r in d["food"]])]
    if d.get("omiyage"):
        body.append(("p", u"🎁 常見伴手禮：" + d["omiyage"]))
    body += [("h", u"世界遺產")]
    body.append(("ul", d["wh"]) if d["wh"] else ("p", u"目前沒有列入名錄的世界遺產。"))
    body += [("h", u"慶典"), ("ul", [u"<strong>%s</strong>：%s" % r for r in d["fest"]]),
             ("h", u"旅遊建議"), ("t", [u"項目", u"建議"], [[u"最佳季節", d["season"]], [u"建議天數", d["days"]], [u"經典路線", d["route"]],
                                                        [u"從台灣怎麼去", d["access"]]]),
             ("note", u"🤔 常見誤解", [("ul", d["myth"])])]
    if d.get("fun"):
        body.append(("note", u"✨ 冷知識", [("ul", d["fun"])]))
    goals = [u"在地圖上找到%s，說出%s所在地與鄰接的市道" % (short(c), office(c)), u"認識%s的地理、歷史與方言" % short(c),
             u"知道%s的美食、世界遺產、慶典與旅遊重點" % short(c)]
    point = d.get("pt") or d["one"]
    check = [u"%s的%s在哪裡？和哪些市道相鄰？" % (short(c), office(c)), u"舉出%s的一樣代表美食或一個慶典。" % short(c), d["q"]]
    return krlesson(u"%s：%s" % (nm(c), d["sub"]), d.get("desc", d["sub"]), goals, body, point, check)


def K(c, **d):
    return kr_lesson(c, d)
