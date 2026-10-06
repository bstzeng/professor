# -*- coding: utf-8 -*-
"""〈日本 47 都道府縣〉（jpp_）共用資料、地圖與每課的組裝工具。"""
from cc_common import *
from geo_common import jp_xy, centroid, bbox_of, static_map, legend, geolib, HL as HL_, NEAR as NEAR_, BASE as BASE_
from jpp_geo import JP_VB, JP_PATHS

JP_NOTE = (u"本課程是<strong>地理、文化與旅遊的入門介紹</strong>。人口為 2020 年日本國勢調查數字，面積為約略值；"
           u"世界遺產以截至 2025 年的名錄為準，航班與交通資訊可能變動，出發前請再確認。地圖已簡化，僅供看位置。")

TW_AREA = 36197

REGIONS = {"HK": (u"北海道", "#5b8fb9"), "TH": (u"東北", "#2e8b57"), "KT": (u"關東", "#c0392b"), "CB": (u"中部", "#d68910"),
           "KK": (u"近畿", "#8e5aa8"), "CG": (u"中國", "#16a085"), "SK": (u"四國", "#a0522d"), "KY": (u"九州・沖繩", "#3a6ea5")}

# code: (名稱, 假名讀音, 羅馬拼音, 地方, 都道府縣廳所在地, (緯度, 經度), 面積 km², 人口(萬, 2020), 舊國名, 鄰接)
BASIC = {
    "01": (u"北海道", u"ほっかいどう", "Hokkaidō", "HK", u"札幌市", (43.06, 141.35), 83424, 522.5, u"蝦夷地（明治後劃為 11 國）", ""),
    "02": (u"青森縣", u"あおもりけん", "Aomori", "TH", u"青森市", (40.82, 140.74), 9646, 123.8, u"陸奧（北部）", "03 05"),
    "03": (u"岩手縣", u"いわてけん", "Iwate", "TH", u"盛岡市", (39.70, 141.15), 15275, 121.1, u"陸奧（陸中）", "02 04 05"),
    "04": (u"宮城縣", u"みやぎけん", "Miyagi", "TH", u"仙台市", (38.27, 140.87), 7282, 230.2, u"陸奧（陸前）", "03 05 06 07"),
    "05": (u"秋田縣", u"あきたけん", "Akita", "TH", u"秋田市", (39.72, 140.10), 11638, 96.0, u"出羽（羽後）", "02 03 04 06"),
    "06": (u"山形縣", u"やまがたけん", "Yamagata", "TH", u"山形市", (38.24, 140.36), 9323, 106.8, u"出羽（羽前）", "04 05 07 15"),
    "07": (u"福島縣", u"ふくしまけん", "Fukushima", "TH", u"福島市", (37.75, 140.47), 13784, 183.3, u"陸奧（岩代、磐城）", "04 06 08 09 10 15"),
    "08": (u"茨城縣", u"いばらきけん", "Ibaraki", "KT", u"水戶市", (36.34, 140.45), 6097, 286.7, u"常陸", "07 09 11 12"),
    "09": (u"栃木縣", u"とちぎけん", "Tochigi", "KT", u"宇都宮市", (36.57, 139.88), 6408, 193.3, u"下野", "07 08 10 11"),
    "10": (u"群馬縣", u"ぐんまけん", "Gunma", "KT", u"前橋市", (36.39, 139.06), 6362, 193.9, u"上野", "07 09 11 15 20"),
    "11": (u"埼玉縣", u"さいたまけん", "Saitama", "KT", u"埼玉市", (35.86, 139.65), 3798, 734.5, u"武藏（北部）", "08 09 10 12 13 19 20"),
    "12": (u"千葉縣", u"ちばけん", "Chiba", "KT", u"千葉市", (35.61, 140.12), 5157, 628.4, u"下總、上總、安房", "08 11 13"),
    "13": (u"東京都", u"とうきょうと", "Tōkyō", "KT", u"新宿區", (35.69, 139.69), 2194, 1404.8, u"武藏（中部）", "11 12 14 19"),
    "14": (u"神奈川縣", u"かながわけん", "Kanagawa", "KT", u"橫濱市", (35.45, 139.64), 2416, 923.7, u"相模、武藏（東南部）", "13 19 22"),
    "15": (u"新潟縣", u"にいがたけん", "Niigata", "CB", u"新潟市", (37.90, 139.02), 12584, 220.1, u"越後、佐渡", "06 07 10 16 20"),
    "16": (u"富山縣", u"とやまけん", "Toyama", "CB", u"富山市", (36.70, 137.21), 4248, 103.5, u"越中", "15 17 20 21"),
    "17": (u"石川縣", u"いしかわけん", "Ishikawa", "CB", u"金澤市", (36.59, 136.63), 4186, 113.3, u"加賀、能登", "16 18 21"),
    "18": (u"福井縣", u"ふくいけん", "Fukui", "CB", u"福井市", (36.07, 136.22), 4191, 76.7, u"越前、若狹", "17 21 25 26"),
    "19": (u"山梨縣", u"やまなしけん", "Yamanashi", "CB", u"甲府市", (35.66, 138.57), 4465, 81.0, u"甲斐", "11 13 14 20 22"),
    "20": (u"長野縣", u"ながのけん", "Nagano", "CB", u"長野市", (36.65, 138.18), 13562, 204.8, u"信濃", "10 11 15 16 19 21 22 23"),
    "21": (u"岐阜縣", u"ぎふけん", "Gifu", "CB", u"岐阜市", (35.39, 136.72), 10621, 197.9, u"美濃、飛驒", "16 17 18 20 23 24 25"),
    "22": (u"靜岡縣", u"しずおかけん", "Shizuoka", "CB", u"靜岡市", (34.98, 138.38), 7777, 363.3, u"駿河、遠江、伊豆", "14 19 20 23"),
    "23": (u"愛知縣", u"あいちけん", "Aichi", "CB", u"名古屋市", (35.18, 136.91), 5173, 754.2, u"尾張、三河", "20 21 22 24"),
    "24": (u"三重縣", u"みえけん", "Mie", "KK", u"津市", (34.73, 136.51), 5774, 177.0, u"伊勢、伊賀、志摩", "21 23 25 26 29 30"),
    "25": (u"滋賀縣", u"しがけん", "Shiga", "KK", u"大津市", (35.00, 135.87), 4017, 141.4, u"近江", "18 21 24 26"),
    "26": (u"京都府", u"きょうとふ", "Kyōto", "KK", u"京都市", (35.02, 135.76), 4612, 257.8, u"山城、丹後、丹波（東部）", "18 24 25 27 28 29"),
    "27": (u"大阪府", u"おおさかふ", "Ōsaka", "KK", u"大阪市", (34.69, 135.52), 1905, 883.8, u"攝津（東部）、河內、和泉", "26 28 29 30"),
    "28": (u"兵庫縣", u"ひょうごけん", "Hyōgo", "KK", u"神戶市", (34.69, 135.18), 8401, 546.5, u"攝津（西部）、播磨、但馬、丹波（西部）、淡路", "26 27 31 33"),
    "29": (u"奈良縣", u"ならけん", "Nara", "KK", u"奈良市", (34.69, 135.83), 3691, 132.4, u"大和", "24 26 27 30"),
    "30": (u"和歌山縣", u"わかやまけん", "Wakayama", "KK", u"和歌山市", (34.23, 135.17), 4725, 92.3, u"紀伊", "24 27 29"),
    "31": (u"鳥取縣", u"とっとりけん", "Tottori", "CG", u"鳥取市", (35.50, 134.24), 3507, 55.3, u"因幡、伯耆", "28 32 33 34"),
    "32": (u"島根縣", u"しまねけん", "Shimane", "CG", u"松江市", (35.47, 133.05), 6708, 67.1, u"出雲、石見、隱岐", "31 34 35"),
    "33": (u"岡山縣", u"おかやまけん", "Okayama", "CG", u"岡山市", (34.66, 133.93), 7114, 188.8, u"備前、備中、美作", "28 31 34"),
    "34": (u"廣島縣", u"ひろしまけん", "Hiroshima", "CG", u"廣島市", (34.40, 132.46), 8479, 280.0, u"安藝、備後", "31 32 33 35"),
    "35": (u"山口縣", u"やまぐちけん", "Yamaguchi", "CG", u"山口市", (34.19, 131.47), 6113, 134.2, u"周防、長門", "32 34"),
    "36": (u"德島縣", u"とくしまけん", "Tokushima", "SK", u"德島市", (34.07, 134.56), 4147, 72.0, u"阿波", "37 38 39"),
    "37": (u"香川縣", u"かがわけん", "Kagawa", "SK", u"高松市", (34.34, 134.04), 1877, 95.0, u"讚岐", "36 38"),
    "38": (u"愛媛縣", u"えひめけん", "Ehime", "SK", u"松山市", (33.84, 132.77), 5676, 133.5, u"伊予", "36 37 39"),
    "39": (u"高知縣", u"こうちけん", "Kōchi", "SK", u"高知市", (33.56, 133.53), 7104, 69.2, u"土佐", "36 38"),
    "40": (u"福岡縣", u"ふくおかけん", "Fukuoka", "KY", u"福岡市", (33.61, 130.42), 4987, 513.5, u"筑前、筑後、豐前（北部）", "41 43 44"),
    "41": (u"佐賀縣", u"さがけん", "Saga", "KY", u"佐賀市", (33.25, 130.30), 2441, 81.1, u"肥前（東部）", "40 42"),
    "42": (u"長崎縣", u"ながさきけん", "Nagasaki", "KY", u"長崎市", (32.74, 129.87), 4131, 131.2, u"肥前（西部）、壹岐、對馬", "41"),
    "43": (u"熊本縣", u"くまもとけん", "Kumamoto", "KY", u"熊本市", (32.79, 130.74), 7409, 173.8, u"肥後", "40 44 45 46"),
    "44": (u"大分縣", u"おおいたけん", "Ōita", "KY", u"大分市", (33.24, 131.61), 6341, 112.4, u"豐後、豐前（南部）", "40 43 45"),
    "45": (u"宮崎縣", u"みやざきけん", "Miyazaki", "KY", u"宮崎市", (31.91, 131.42), 7735, 107.0, u"日向", "43 44 46"),
    "46": (u"鹿兒島縣", u"かごしまけん", "Kagoshima", "KY", u"鹿兒島市", (31.56, 130.56), 9187, 158.8, u"薩摩、大隅", "43 45"),
    "47": (u"沖繩縣", u"おきなわけん", "Okinawa", "KY", u"那霸市", (26.21, 127.68), 2282, 146.7, u"琉球", ""),
}

ORDER = ["%02d" % i for i in range(1, 48)]
LESSON = {c: i + 4 for i, c in enumerate(ORDER)}          # 第 4～50 課
SMALL = {"13", "27", "37", "14", "11", "41", "25", "29"}


def nm(c):
    return BASIC[c][0]


def short(c):
    n = BASIC[c][0]
    return n if c == "01" else n[:-1]


def part(c):
    return "oki" if c == "47" else "main"


def cap_xy(c):
    lat, lon = BASIC[c][5]
    return jp_xy(lon, lat, part(c))


def wan(x):
    if x >= 100:
        return u"約 %s 萬" % format(int(round(x)), ",")
    return u"約 %.1f 萬" % x


def area_txt(a):
    r = a / float(TW_AREA)
    cmp_ = (u"約台灣的 %.1f 倍" % r) if r >= 1.15 else (u"和台灣差不多大" if r >= 0.85 else u"約台灣的 %d%%" % round(r * 100))
    return u"%s 平方公里（%s）" % (format(a, ","), cmp_)


# ---------- 地圖 ----------
_OB = bbox_of(JP_PATHS["47"])
OKI_FRAME = ('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="var(--text-muted)" stroke-width="0.8" stroke-dasharray="4 3"/>'
             '<text x="%d" y="%d" font-size="10" fill="var(--text-muted)">沖繩（位置移動，實際在九州西南方）</text>'
             % (_OB[0] - 6, _OB[1] - 6, _OB[2] - _OB[0] + 12, _OB[3] - _OB[1] + 12, _OB[0] - 6, _OB[3] + 18))


def locmap(c):
    near = BASIC[c][9].split()
    lx, ly = centroid(JP_PATHS[c])
    x0, y0, x1, y1 = bbox_of(JP_PATHS[c])
    small = c in SMALL
    if small:                                   # 以主島（最大的一塊）為中心畫圈，避免東京的離島把圈撐大
        from geo_common import rings_of, _area_c
        a, cx, cy = max((_area_c(r) for r in rings_of(JP_PATHS[c])), key=lambda t: t[0])
        x0, y0, x1, y1 = cx - 8, cy - 8, cx + 8, cy + 8
        lab = (short(c), x1 + 30, y1 + 18)
    elif c == "47":
        lab = (short(c), _OB[2] + 40, (_OB[1] + _OB[3]) / 2 + 5)
    else:
        lab = (short(c), lx, ly + 18 if (y1 - y0) > 40 else y0 - 6)
    star = cap_xy(c)
    g, vb = static_map(JP_VB, JP_PATHS, c, near, star=star, label=lab, extra=OKI_FRAME)
    if small:
        g += '<circle cx="%d" cy="%d" r="20" fill="none" stroke="%s" stroke-width="2"/>' % ((x0 + x1) / 2, (y0 + y1) / 2, HL_)
    items = [(HL_, short(c))] + ([(NEAR_, u"鄰接")] if near else []) + [("star", (u"都廳" if c == "13" else u"道廳" if c == "01" else u"府廳" if c in ("26", "27") else u"縣廳") + u" " + BASIC[c][4])]
    g += legend(JP_VB[0] - 280, JP_VB[1] - 12, items)
    cap = u"%s的位置（紅色）。" % nm(c) + (u"橘色是陸地相鄰的都府縣。" if near else u"") + u"★ 是%s廳所在地。" % (
        u"都" if c == "13" else u"道" if c == "01" else u"府" if c in ("26", "27") else u"縣")
    return ("fig", g, vb, cap)


def overview_map(fill, labels=(), cap=u"", legend_items=None):
    g = [OKI_FRAME]
    for k, d in sorted(JP_PATHS.items()):
        g.append('<path d="%s" fill="%s" stroke="var(--surface)" stroke-width="0.6"/>' % (d, fill.get(k, BASE_)))
    for t, x, y in labels:
        g.append('<text x="%d" y="%d" font-size="10" text-anchor="middle" fill="var(--text)" stroke="var(--surface)" '
                 'stroke-width="2.5" paint-order="stroke">%s</text>' % (x, y, t))
    if legend_items:
        rows = [legend_items[:4], legend_items[4:]] if len(legend_items) > 4 else [legend_items]
        for i, row in enumerate(rows):
            g.append(legend(JP_VB[0] - 300, JP_VB[1] - 12 - 16 * (len(rows) - 1 - i), row))
    return ("fig", "\n".join(g), "0 0 %d %d" % tuple(JP_VB), cap)


def _dataset():
    items = []
    for c in ORDER:
        b = BASIC[c]
        x, y = centroid(JP_PATHS[c])
        items.append({"c": c, "n": b[0], "e": u"%s　%s" % (b[1], b[2]), "p": JP_PATHS[c], "x": int(x), "y": int(y), "L": LESSON[c], "g": b[3],
                      "v": {"pop": b[7], "area": b[6], "den": round(b[7] * 10000 / b[6])},
                      "f": [[u"廳所在地", b[4]], [u"人口", wan(b[7])], [u"面積", u"%s km²" % format(b[6], ",")], [u"舊國名", b[8]]]})
    return {"vb": JP_VB, "items": items, "unit": u"都道府縣", "groups": {k: list(v) for k, v in REGIONS.items()}, "extra": OKI_FRAME,
            "metrics": [["pop", u"人口", u"萬人", 1, u"2020 年國勢調查。台灣約 2,340 萬人。"],
                        ["area", u"面積", u"km²", 0, u"台灣約 36,000 平方公里。"],
                        ["den", u"人口密度", u"人/km²", 0, u"台灣約每平方公里 650 人。"]]}


JPLIB = geolib("__jppLib", _dataset())


def jpw(cfg, maxw=760):
    return wdg("__jppLib-w", cfg, maxw)


jplesson = make_lesson(u"🗾", JP_NOTE, JPLIB, "__jppLib-w")

DATA = {}


def pref_lesson(c, d):
    """d：sub、one、origin、mascot、cities、geo、hist、dialect、food、omiyage、wh、matsuri、onsen、season、days、route、access、myth、fun、q"""
    DATA[c] = d
    b = BASIC[c]
    office = u"都廳" if c == "13" else u"道廳" if c == "01" else u"府廳" if c in ("26", "27") else u"縣廳"
    rows = [[u"日文讀音", u"%s（%s）" % (b[1], b[2])], [u"地方", REGIONS[b[3]][0]], [office + u"所在地", b[4]],
            [u"面積", area_txt(b[6])], [u"人口（2020）", wan(b[7]) + u"人"], [u"舊國名", b[8]], [u"名稱由來", d["origin"]],
            [u"吉祥物", d.get("mascot", u"—")],
            [u"陸地鄰接", u"、".join(nm(x) for x in b[9].split()) or u"無（四面環海）"]]
    body = [locmap(c),
            ("note", u"💡 一句話記住%s" % short(c), [("p", d["one"])]),
            ("h", u"基本資料"), ("t", [u"項目", u"內容"], rows),
            ("h", u"主要城市與觀光地"), ("t", [u"地點", u"特色"], [list(r) for r in d["cities"]]),
            ("h", u"地理與氣候"), ("p", d["geo"]),
            ("h", u"歷史重點"), ("ul", d["hist"]),
            ("h", u"方言"), ("p", d["dialect"]),
            ("h", u"美食與伴手禮"), ("ul", [u"<strong>%s</strong>：%s" % r for r in d["food"]])]
    if d.get("omiyage"):
        body.append(("p", u"🎁 常見伴手禮：" + d["omiyage"]))
    body += [("h", u"世界遺產")]
    body.append(("ul", d["wh"]) if d["wh"] else ("p", u"目前沒有列入名錄的世界遺產。" + d.get("wh_note", u"")))
    body += [("h", u"祭典"), ("ul", [u"<strong>%s</strong>：%s" % r for r in d["matsuri"]])]
    if d.get("onsen"):
        body += [("h", u"溫泉"), ("p", d["onsen"])]
    body += [("h", u"旅遊建議"), ("t", [u"項目", u"建議"], [[u"最佳季節", d["season"]], [u"建議天數", d["days"]], [u"經典路線", d["route"]],
                                                        [u"從台灣怎麼去", d["access"]]]),
             ("note", u"🤔 常見誤解", [("ul", d["myth"])])]
    if d.get("fun"):
        body.append(("note", u"✨ 冷知識", [("ul", d["fun"])]))
    goals = [u"在地圖上找到%s，說出%s所在地與鄰接的都府縣" % (short(c), office), u"認識%s的城市、地理、歷史與方言" % short(c),
             u"知道%s的美食、世界遺產、祭典與旅遊重點" % short(c)]
    point = d.get("pt") or (d["one"] + u" %s在%s，舊國名是%s。" % (office, b[4], b[8]))
    check = [u"%s的%s在哪裡？舊國名是什麼？" % (short(c), office), u"舉出%s的一樣代表美食或一個祭典。" % short(c), d["q"]]
    return jplesson(u"%s：%s" % (nm(c), d["sub"]), d.get("desc", d["sub"]), goals, body, point, check)


def J(c, **d):
    return pref_lesson(c, d)
