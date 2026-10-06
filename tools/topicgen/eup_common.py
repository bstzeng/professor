# -*- coding: utf-8 -*-
"""〈歐洲各國〉（eup_）共用資料、地圖、國旗與每課的組裝工具。"""
from cc_common import *
from geo_common import eu_xy, centroid, bbox_of, static_map, legend, geolib, rings_of, _area_c, HL as HL_, NEAR as NEAR_, BASE as BASE_
from eup_geo import EU_VB, EU_PATHS, EU_CTX
from eup_flags import flag, EMBLEM

EU_NOTE = (u"本課程是<strong>地理、文化與旅遊的入門介紹</strong>。人口為 2024 年前後的約略值，面積為約略值；世界遺產以截至 2025 年的名錄為準，"
           u"簽證與航班資訊可能變動，出發前請查詢外交部領事事務局與航空公司公告。地圖依據 Natural Earth 資料並經簡化，僅供看位置，"
           u"有爭議的領土以國際間較普遍承認的邊界繪製，並在課文中說明。")

TW_AREA = 36197

REGIONS = {"W": (u"西歐", "#3a6ea5"), "C": (u"中歐", "#2e8b57"), "S": (u"南歐", "#d68910"), "N": (u"北歐", "#5b8fb9"),
           "E": (u"波羅的海與東歐", "#8e5aa8"), "B": (u"巴爾幹與土耳其", "#c0504d"), "M": (u"迷你國家", "#7f8c8d")}

Y, N_ = True, False
# code: (中文名, 當地名稱, 首都, (緯度, 經度), 面積 km², 人口(萬), 地區, 官方語言, 貨幣, 歐盟, 申根, 北約, 鄰國)
BASIC = {
    "GBR": (u"英國", u"United Kingdom", u"倫敦", (51.507, -0.128), 243610, 6900, "W", u"英語", u"英鎊", N_, N_, Y, "IRL"),
    "IRL": (u"愛爾蘭", u"Éire / Ireland", u"都柏林", (53.35, -6.26), 70273, 530, "W", u"愛爾蘭語、英語", u"歐元", Y, N_, N_, "GBR"),
    "FRA": (u"法國", u"France", u"巴黎", (48.857, 2.352), 551695, 6850, "W", u"法語", u"歐元", Y, Y, Y, "BEL LUX DEU CHE ITA MCO ESP AND"),
    "BEL": (u"比利時", u"België / Belgique", u"布魯塞爾", (50.85, 4.35), 30689, 1180, "W", u"荷蘭語、法語、德語", u"歐元", Y, Y, Y, "FRA LUX DEU NLD"),
    "NLD": (u"荷蘭", u"Nederland", u"阿姆斯特丹", (52.37, 4.90), 41850, 1790, "W", u"荷蘭語", u"歐元", Y, Y, Y, "BEL DEU"),
    "LUX": (u"盧森堡", u"Lëtzebuerg", u"盧森堡市", (49.61, 6.13), 2586, 67, "W", u"盧森堡語、法語、德語", u"歐元", Y, Y, Y, "BEL FRA DEU"),
    "DEU": (u"德國", u"Deutschland", u"柏林", (52.52, 13.405), 357592, 8400, "C", u"德語", u"歐元", Y, Y, Y, "DNK POL CZE AUT CHE FRA LUX BEL NLD"),
    "AUT": (u"奧地利", u"Österreich", u"維也納", (48.21, 16.37), 83879, 915, "C", u"德語", u"歐元", Y, Y, N_, "DEU CZE SVK HUN SVN ITA CHE LIE"),
    "CHE": (u"瑞士", u"Schweiz / Suisse / Svizzera", u"伯恩", (46.95, 7.45), 41285, 900, "C", u"德語、法語、義大利語、羅曼什語", u"瑞士法郎", N_, Y, N_, "DEU AUT LIE ITA FRA"),
    "POL": (u"波蘭", u"Polska", u"華沙", (52.23, 21.01), 312696, 3670, "C", u"波蘭語", u"波蘭茲羅提", Y, Y, Y, "DEU CZE SVK UKR BLR LTU RUS"),
    "CZE": (u"捷克", u"Česko", u"布拉格", (50.08, 14.44), 78871, 1090, "C", u"捷克語", u"捷克克朗", Y, Y, Y, "DEU POL SVK AUT"),
    "SVK": (u"斯洛伐克", u"Slovensko", u"布拉提斯拉瓦", (48.15, 17.11), 49035, 545, "C", u"斯洛伐克語", u"歐元", Y, Y, Y, "CZE POL UKR HUN AUT"),
    "HUN": (u"匈牙利", u"Magyarország", u"布達佩斯", (47.50, 19.04), 93028, 960, "C", u"匈牙利語", u"福林", Y, Y, Y, "AUT SVK UKR ROU SRB HRV SVN"),
    "ESP": (u"西班牙", u"España", u"馬德里", (40.42, -3.70), 505990, 4880, "S", u"西班牙語（各地另有加泰隆尼亞語、巴斯克語等）", u"歐元", Y, Y, Y, "PRT FRA AND"),
    "PRT": (u"葡萄牙", u"Portugal", u"里斯本", (38.72, -9.14), 92212, 1060, "S", u"葡萄牙語", u"歐元", Y, Y, Y, "ESP"),
    "ITA": (u"義大利", u"Italia", u"羅馬", (41.90, 12.50), 302073, 5890, "S", u"義大利語", u"歐元", Y, Y, Y, "FRA CHE AUT SVN SMR"),
    "GRC": (u"希臘", u"Ελλάδα", u"雅典", (37.98, 23.73), 131957, 1040, "S", u"希臘語", u"歐元", Y, Y, Y, "ALB MKD BGR TUR"),
    "MLT": (u"馬爾他", u"Malta", u"瓦勒他", (35.90, 14.51), 316, 56, "S", u"馬爾他語、英語", u"歐元", Y, Y, N_, ""),
    "CYP": (u"賽普勒斯", u"Κύπρος / Kıbrıs", u"尼古西亞", (35.17, 33.36), 9251, 135, "S", u"希臘語、土耳其語", u"歐元", Y, N_, N_, ""),
    "DNK": (u"丹麥", u"Danmark", u"哥本哈根", (55.68, 12.57), 42933, 600, "N", u"丹麥語", u"丹麥克朗", Y, Y, Y, "DEU"),
    "NOR": (u"挪威", u"Norge", u"奧斯陸", (59.91, 10.75), 385207, 555, "N", u"挪威語", u"挪威克朗", N_, Y, Y, "SWE FIN RUS"),
    "SWE": (u"瑞典", u"Sverige", u"斯德哥爾摩", (59.33, 18.07), 450295, 1060, "N", u"瑞典語", u"瑞典克朗", Y, Y, Y, "NOR FIN"),
    "FIN": (u"芬蘭", u"Suomi", u"赫爾辛基", (60.17, 24.94), 338455, 560, "N", u"芬蘭語、瑞典語", u"歐元", Y, Y, Y, "SWE NOR RUS"),
    "ISL": (u"冰島", u"Ísland", u"雷克雅維克", (64.15, -21.94), 103000, 39, "N", u"冰島語", u"冰島克朗", N_, Y, Y, ""),
    "EST": (u"愛沙尼亞", u"Eesti", u"塔林", (59.44, 24.75), 45339, 137, "E", u"愛沙尼亞語", u"歐元", Y, Y, Y, "LVA RUS"),
    "LVA": (u"拉脫維亞", u"Latvija", u"里加", (56.95, 24.11), 64589, 188, "E", u"拉脫維亞語", u"歐元", Y, Y, Y, "EST LTU BLR RUS"),
    "LTU": (u"立陶宛", u"Lietuva", u"維爾紐斯", (54.69, 25.28), 65300, 286, "E", u"立陶宛語", u"歐元", Y, Y, Y, "LVA BLR POL RUS"),
    "UKR": (u"烏克蘭", u"Україна", u"基輔", (50.45, 30.52), 603550, 3500, "E", u"烏克蘭語", u"格里夫納", N_, N_, N_, "POL SVK HUN ROU MDA BLR RUS"),
    "BLR": (u"白俄羅斯", u"Беларусь", u"明斯克", (53.90, 27.56), 207600, 915, "E", u"白俄羅斯語、俄語", u"白俄羅斯盧布", N_, N_, N_, "POL LTU LVA RUS UKR"),
    "MDA": (u"摩爾多瓦", u"Moldova", u"奇西瑙", (47.01, 28.86), 33846, 245, "E", u"羅馬尼亞語", u"摩爾多瓦列伊", N_, N_, N_, "ROU UKR"),
    "RUS": (u"俄羅斯", u"Россия", u"莫斯科", (55.76, 37.62), 17098246, 14600, "E", u"俄語", u"盧布", N_, N_, N_, "NOR FIN EST LVA LTU POL BLR UKR"),
    "SVN": (u"斯洛維尼亞", u"Slovenija", u"盧比安納", (46.06, 14.51), 20271, 212, "B", u"斯洛維尼亞語", u"歐元", Y, Y, Y, "ITA AUT HUN HRV"),
    "HRV": (u"克羅埃西亞", u"Hrvatska", u"札格瑞布", (45.81, 15.98), 56594, 386, "B", u"克羅埃西亞語", u"歐元", Y, Y, Y, "SVN HUN SRB BIH MNE"),
    "BIH": (u"波士尼亞與赫塞哥維納", u"Bosna i Hercegovina", u"塞拉耶佛", (43.86, 18.41), 51209, 320, "B", u"波士尼亞語、克羅埃西亞語、塞爾維亞語", u"可兌換馬克", N_, N_, N_, "HRV SRB MNE"),
    "SRB": (u"塞爾維亞", u"Србија", u"貝爾格勒", (44.79, 20.45), 77474, 660, "B", u"塞爾維亞語", u"塞爾維亞第納爾", N_, N_, N_, "HUN ROU BGR MKD KOS MNE BIH HRV"),
    "MNE": (u"蒙特內哥羅", u"Crna Gora", u"波德里查", (42.44, 19.26), 13812, 62, "B", u"蒙特內哥羅語", u"歐元", N_, N_, Y, "HRV BIH SRB KOS ALB"),
    "MKD": (u"北馬其頓", u"Северна Македонија", u"史高比耶", (42.00, 21.43), 25713, 184, "B", u"馬其頓語、阿爾巴尼亞語", u"馬其頓第納爾", N_, N_, Y, "SRB KOS ALB GRC BGR"),
    "ALB": (u"阿爾巴尼亞", u"Shqipëria", u"地拉那", (41.33, 19.82), 28748, 240, "B", u"阿爾巴尼亞語", u"列克", N_, N_, Y, "MNE KOS MKD GRC"),
    "BGR": (u"保加利亞", u"България", u"索菲亞", (42.70, 23.32), 110994, 640, "B", u"保加利亞語", u"歐元（2026 年起）", Y, Y, Y, "ROU SRB MKD GRC TUR"),
    "ROU": (u"羅馬尼亞", u"România", u"布加勒斯特", (44.43, 26.10), 238397, 1900, "B", u"羅馬尼亞語", u"羅馬尼亞列伊", Y, Y, Y, "UKR MDA BGR SRB HUN"),
    "KOS": (u"科索沃", u"Kosova / Kosovo", u"普里斯提納", (42.66, 21.17), 10887, 159, "B", u"阿爾巴尼亞語、塞爾維亞語", u"歐元", N_, N_, N_, "SRB MNE ALB MKD"),
    "TUR": (u"土耳其", u"Türkiye", u"安卡拉", (39.93, 32.86), 783562, 8500, "B", u"土耳其語", u"土耳其里拉", N_, N_, Y, "GRC BGR"),
    "VAT": (u"梵蒂岡", u"Città del Vaticano", u"梵蒂岡城", (41.903, 12.453), 0.49, 0.08, "M", u"義大利語、拉丁語", u"歐元", N_, N_, N_, "ITA"),
    "SMR": (u"聖馬利諾", u"San Marino", u"聖馬利諾市", (43.94, 12.45), 61, 3.4, "M", u"義大利語", u"歐元", N_, N_, N_, "ITA"),
    "MCO": (u"摩納哥", u"Monaco", u"摩納哥", (43.74, 7.42), 2.08, 3.9, "M", u"法語", u"歐元", N_, N_, N_, "FRA"),
    "LIE": (u"列支敦斯登", u"Liechtenstein", u"瓦都茲", (47.14, 9.52), 160, 4.0, "M", u"德語", u"瑞士法郎", N_, Y, N_, "CHE AUT"),
    "AND": (u"安道爾", u"Andorra", u"安道爾城", (42.51, 1.52), 468, 8.5, "M", u"加泰隆尼亞語", u"歐元", N_, N_, N_, "FRA ESP"),
}

ORDER = ["GBR", "IRL", "FRA", "BEL", "NLD", "LUX", "DEU", "AUT", "CHE", "POL", "CZE", "SVK", "HUN", "ESP", "PRT", "ITA", "GRC", "MLT", "CYP",
         "DNK", "NOR", "SWE", "FIN", "ISL", "EST", "LVA", "LTU", "UKR", "BLR", "MDA", "RUS", "SVN", "HRV", "BIH", "SRB", "MNE", "MKD", "ALB",
         "BGR", "ROU", "KOS", "TUR"]
MICRO = ["VAT", "SMR", "MCO", "LIE", "AND"]
LESSON = {c: i + 4 for i, c in enumerate(ORDER)}           # 第 4～45 課
LESSON.update({"VAT": 46, "SMR": 46, "MCO": 46, "LIE": 47, "AND": 47})
SMALL = {"LUX", "MLT", "SVN", "MNE", "KOS", "MKD", "BEL", "CYP", "ALB"}


def nm(c):
    return BASIC[c][0]


def cap_xy(c):
    lat, lon = BASIC[c][3]
    return eu_xy(lon, lat)


def wan(x):
    if x >= 100:
        return u"約 %s 萬" % format(int(round(x)), ",")
    if x >= 1:
        return u"約 %.1f 萬" % x
    return u"約 %d 人" % round(x * 10000)


def area_txt(a):
    if a < 1:
        return u"約 %.2f 平方公里" % a
    r = a / float(TW_AREA)
    if r >= 1.15:
        return u"%s 平方公里（約台灣的 %.1f 倍）" % (format(int(a), ","), r)
    if r >= 0.85:
        return u"%s 平方公里（和台灣差不多大）" % format(int(a), ",")
    if r >= 0.01:
        return u"%s 平方公里（約台灣的 %d%%）" % (format(int(a), ","), round(r * 100))
    return u"%s 平方公里（約台北市的 %.1f 倍）" % (format(a, ","), a / 272.0)


def yn(v):
    return u"✅ 是" if v else u"—"


# ---------- 地圖 ----------
CTX = '<path d="%s" fill="#e6e9ed" stroke="var(--surface)" stroke-width="0.5"/>' % EU_CTX


def locmap(c):
    near = [x for x in BASIC[c][12].split() if x in EU_PATHS]
    lx, ly = centroid(EU_PATHS[c])
    x0, y0, x1, y1 = bbox_of(EU_PATHS[c])
    small = c in SMALL
    if c == "RUS":
        lab = (nm(c), cap_xy(c)[0] + 40, cap_xy(c)[1] - 30)
    elif small:
        a, cx, cy = max((_area_c(r) for r in rings_of(EU_PATHS[c])), key=lambda t: t[0])
        lab = (nm(c), cx + 42, cy + 30)
    else:
        lab = (nm(c), lx, ly + 18)
    star = cap_xy(c)
    g, vb = static_map(EU_VB, EU_PATHS, c, near, star=star, label=lab, extra=None)
    g = CTX + g
    if small:
        g += '<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="2"/>' % (cx, cy, max(12, (x1 - x0) / 2 + 6), HL_)
    items = [(HL_, nm(c))] + ([(NEAR_, u"鄰國")] if near else []) + [("star", u"首都 " + BASIC[c][2])]
    g += '<rect x="%d" y="%d" width="%d" height="22" fill="var(--surface)" opacity="0.85"/>' % (EU_VB[0] - 320, EU_VB[1] - 30, 316)
    g += legend(EU_VB[0] - 312, EU_VB[1] - 14, items)
    cap = u"%s的位置（紅色）。" % nm(c) + (u"橘色是陸地相鄰的歐洲國家。" if near else u"") + u"★ 是首都。淺灰色是歐洲以外的國家。"
    return ("fig", g, vb, cap)


def overview_map(fill, labels=(), cap=u"", legend_items=None, extra=""):
    g = [CTX]
    for k, d in sorted(EU_PATHS.items()):
        g.append('<path d="%s" fill="%s" fill-rule="evenodd" stroke="var(--surface)" stroke-width="0.6"/>' % (d, fill.get(k, BASE_)))
    g.append(extra)
    for t, x, y in labels:
        g.append('<text x="%d" y="%d" font-size="10" text-anchor="middle" fill="var(--text)" stroke="var(--surface)" '
                 'stroke-width="2.5" paint-order="stroke">%s</text>' % (x, y, t))
    if legend_items:
        rows = [legend_items[:4], legend_items[4:]] if len(legend_items) > 4 else [legend_items]
        g.append('<rect x="%d" y="%d" width="%d" height="%d" fill="var(--surface)" opacity="0.85"/>' % (EU_VB[0] - 380, EU_VB[1] - 14 - 16 * len(rows), 376, 16 * len(rows) + 10))
        for i, row in enumerate(rows):
            g.append(legend(EU_VB[0] - 372, EU_VB[1] - 12 - 16 * (len(rows) - 1 - i), row))
    return ("fig", "\n".join(g), "0 0 %d %d" % tuple(EU_VB), cap)


def labels(codes=None, skip=("LUX", "MLT", "SVN", "MNE", "KOS", "MKD", "BEL", "LIE", "AND", "MCO", "SMR", "VAT")):
    out = []
    for c in (codes or ORDER):
        if c in skip or c not in EU_PATHS:
            continue
        x, y = centroid(EU_PATHS[c]) if c != "RUS" else (cap_xy(c)[0] + 30, cap_xy(c)[1])
        out.append(({"BIH": u"波赫", "GBR": u"英國"}.get(c, nm(c)), x, y + 4))
    return out


def _dataset():
    items = []
    for c in ORDER + ["LIE", "AND"]:     # 梵蒂岡、聖馬利諾、摩納哥太小，無法點選
        b = BASIC[c]
        x, y = centroid(EU_PATHS[c]) if c != "RUS" else cap_xy(c)
        items.append({"c": c, "n": b[0], "e": b[1], "p": EU_PATHS[c], "x": int(x), "y": int(y), "L": LESSON[c], "g": b[6],
                      "v": {"pop": b[5], "area": b[4], "den": round(b[5] * 10000 / b[4]) if b[4] else 0},
                      "f": [[u"首都", b[2]], [u"人口", wan(b[5])], [u"語言", b[7]], [u"貨幣", b[8]],
                            [u"歐盟", u"是" if b[9] else u"否"], [u"申根", u"是" if b[10] else u"否"]]})
    return {"vb": EU_VB, "items": items, "unit": u"國", "groups": {k: list(v) for k, v in REGIONS.items()}, "extra": CTX,
            "metrics": [["pop", u"人口", u"萬人", 0, u"台灣約 2,340 萬人。俄羅斯、土耳其以全國人口計。"],
                        ["area", u"面積", u"km²", 0, u"台灣約 36,000 平方公里。俄羅斯、土耳其以全國面積計。"],
                        ["den", u"人口密度", u"人/km²", 0, u"台灣約每平方公里 650 人。"]]}


EULIB = geolib("__eupLib", _dataset())


def euw(cfg, maxw=760):
    return wdg("__eupLib-w", cfg, maxw)


eulesson = make_lesson(u"🇪🇺", EU_NOTE, EULIB, "__eupLib-w")


def flag_fig(c, maxw=260):
    s, w, h = flag(c)
    cap = u"%s國旗" % nm(c) + (u"（國徽部分為簡化示意）" if c in EMBLEM else u"")
    return ("raw", u'<div class="content-figure" style="max-width:%dpx;margin-left:auto;margin-right:auto">'
                   u'<svg class="content-diagram" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">%s</svg>'
                   u'<figcaption>%s</figcaption></div>' % (maxw, w, h, s, cap))


DATA = {}


def basic_rows(c, d):
    b = BASIC[c]
    return [[u"當地名稱", b[1]], [u"首都", b[2]], [u"面積", area_txt(b[4])], [u"人口", wan(b[5]) + u"人"], [u"官方語言", b[7]], [u"貨幣", b[8]],
            [u"歐盟／申根／北約", u"%s ／ %s ／ %s" % (yn(b[9]), yn(b[10]), yn(b[11]))],
            [u"陸地鄰國", u"、".join(nm(x) for x in b[12].split()) + (u"（以上為歐洲部分）" if c in ("RUS", "TUR") else u"") or u"無（島國）"]] + d.get("extra_rows", [])


def country_lesson(c, d):
    """d：sub、one、flag、cities、geo、hist、hello、food、omiyage、wh、fest、season、days、route、access、myth、fun、q"""
    DATA[c] = d
    body = [locmap(c),
            ("note", u"💡 一句話記住%s" % nm(c), [("p", d["one"])]),
            ("h", u"國旗"), flag_fig(c), ("p", d["flag"]),
            ("h", u"基本資料"), ("t", [u"項目", u"內容"], basic_rows(c, d)),
            ("h", u"主要城市與景點"), ("t", [u"地點", u"特色"], [list(r) for r in d["cities"]]),
            ("h", u"地理與氣候"), ("p", d["geo"]),
            ("h", u"歷史重點"), ("ul", d["hist"]),
            ("h", u"語言小教室"), ("t", [u"中文", u"當地語言", u"讀音"], [[u"你好", d["hello"][0], d["hello"][1]], [u"謝謝", d["hello"][2], d["hello"][3]]]),
            ("h", u"美食與伴手禮"), ("ul", [u"<strong>%s</strong>：%s" % r for r in d["food"]])]
    if d.get("omiyage"):
        body.append(("p", u"🎁 常見伴手禮：" + d["omiyage"]))
    body += [("h", u"世界遺產")]
    body.append(("ul", d["wh"]) if d["wh"] else ("p", u"目前沒有列入名錄的世界遺產。"))
    body += [("h", u"節慶"), ("ul", [u"<strong>%s</strong>：%s" % r for r in d["fest"]]),
             ("h", u"旅遊建議"), ("t", [u"項目", u"建議"], [[u"最佳季節", d["season"]], [u"建議天數", d["days"]], [u"經典路線", d["route"]],
                                                        [u"從台灣怎麼去", d["access"]]]),
             ("note", u"🤔 常見誤解", [("ul", d["myth"])])]
    if d.get("fun"):
        body.append(("note", u"✨ 冷知識", [("ul", d["fun"])]))
    goals = [u"在地圖上找到%s，說出首都與鄰國" % nm(c), u"認識%s的國旗、地理與歷史" % nm(c), u"知道%s的美食、世界遺產與旅遊重點" % nm(c)]
    check = [u"%s的首都在哪裡？和哪些國家相鄰？" % nm(c), u"%s的國旗有什麼特色？" % nm(c), d["q"]]
    return eulesson(u"%s：%s" % (nm(c), d["sub"]), d.get("desc", d["sub"]), goals, body, d.get("pt") or d["one"], check)


def C(c, **d):
    return country_lesson(c, d)
