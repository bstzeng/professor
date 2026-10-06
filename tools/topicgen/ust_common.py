# -*- coding: utf-8 -*-
"""〈美國五十州〉（ust_）共用資料、地圖與每課的組裝工具。"""
from cc_common import *
from geo_common import us_xy, centroid, bbox_of, static_map, legend, geolib, HL as HL_, NEAR as NEAR_
from ust_geo import US_VB, US_PATHS

ST_NOTE = (u"本課程是<strong>地理與文化的入門介紹</strong>。人口為 2020 年人口普查數字，面積為含水域的總面積；"
           u"企業總部、州旗等資訊可能變動，以截至 2025 年的狀況為準。地圖已簡化，僅供看位置。")

TW_AREA = 36197      # 台灣面積（平方公里）

REGIONS = {"NE": (u"東北部", "#3a6ea5"), "MW": (u"中西部", "#2e8b57"), "S": (u"南部", "#c8792a"), "W": (u"西部", "#8e5aa8")}

# code: (中文名, 英文名, 區域, 首府, (緯度, 經度), 最大城市, 人口(萬, 2020), 總面積 km², 加入年, 順序, 綽號, 鄰州)
BASIC = {
    "ME": (u"緬因州", "Maine", "NE", u"奧古斯塔", (44.31, -69.78), u"波特蘭", 136.2, 91633, 1820, 23, u"松樹州", "NH"),
    "NH": (u"新罕布夏州", "New Hampshire", "NE", u"康科德", (43.21, -71.54), u"曼徹斯特", 137.7, 24214, 1788, 9, u"花崗岩州", "ME VT MA"),
    "VT": (u"佛蒙特州", "Vermont", "NE", u"蒙彼利埃", (44.26, -72.58), u"伯靈頓", 64.3, 24906, 1791, 14, u"綠山州", "NH MA NY"),
    "MA": (u"麻薩諸塞州", "Massachusetts", "NE", u"波士頓", (42.36, -71.06), u"波士頓", 702.9, 27336, 1788, 6, u"海灣州", "RI CT NY VT NH"),
    "RI": (u"羅德島州", "Rhode Island", "NE", u"普羅維登斯", (41.82, -71.41), u"普羅維登斯", 109.7, 4001, 1790, 13, u"海洋州", "CT MA"),
    "CT": (u"康乃狄克州", "Connecticut", "NE", u"哈特福", (41.76, -72.68), u"布里奇波特", 360.6, 14357, 1788, 5, u"憲法州", "NY MA RI"),
    "NY": (u"紐約州", "New York", "NE", u"奧爾巴尼", (42.65, -73.76), u"紐約市", 2020.1, 141297, 1788, 11, u"帝國州", "VT MA CT NJ PA"),
    "NJ": (u"紐澤西州", "New Jersey", "NE", u"特倫頓", (40.22, -74.76), u"紐華克", 928.9, 22591, 1787, 3, u"花園州", "NY PA DE"),
    "PA": (u"賓夕法尼亞州", "Pennsylvania", "NE", u"哈里斯堡", (40.27, -76.88), u"費城", 1300.3, 119280, 1787, 2, u"拱心石州", "NY NJ DE MD WV OH"),
    "OH": (u"俄亥俄州", "Ohio", "MW", u"哥倫布", (39.96, -83.00), u"哥倫布", 1179.9, 116098, 1803, 17, u"七葉樹州", "PA WV KY IN MI"),
    "IN": (u"印第安納州", "Indiana", "MW", u"印第安納波利斯", (39.77, -86.16), u"印第安納波利斯", 678.6, 94326, 1816, 19, u"胡希爾州", "IL MI OH KY"),
    "IL": (u"伊利諾州", "Illinois", "MW", u"春田", (39.80, -89.65), u"芝加哥", 1281.2, 149995, 1818, 21, u"草原州", "WI IA MO KY IN"),
    "MI": (u"密西根州", "Michigan", "MW", u"蘭辛", (42.73, -84.56), u"底特律", 1007.7, 250487, 1837, 26, u"大湖州", "IN OH WI"),
    "WI": (u"威斯康辛州", "Wisconsin", "MW", u"麥迪遜", (43.07, -89.40), u"密爾瓦基", 589.4, 169635, 1848, 30, u"獾州", "MN IA IL MI"),
    "MN": (u"明尼蘇達州", "Minnesota", "MW", u"聖保羅", (44.95, -93.09), u"明尼亞波利斯", 570.6, 225163, 1858, 32, u"北星州", "ND SD IA WI"),
    "IA": (u"愛荷華州", "Iowa", "MW", u"狄蒙", (41.59, -93.62), u"狄蒙", 319.0, 145746, 1846, 29, u"鷹眼州", "MN WI IL MO NE SD"),
    "MO": (u"密蘇里州", "Missouri", "MW", u"傑佛遜城", (38.58, -92.17), u"堪薩斯城", 615.4, 180540, 1821, 24, u"「拿出證據」州", "IA IL KY TN AR OK KS NE"),
    "ND": (u"北達科他州", "North Dakota", "MW", u"俾斯麥", (46.81, -100.78), u"法哥", 77.9, 183108, 1889, 39, u"和平花園州", "MN SD MT"),
    "SD": (u"南達科他州", "South Dakota", "MW", u"皮爾", (44.37, -100.35), u"蘇族瀑布市", 88.7, 199729, 1889, 40, u"拉什莫爾山州", "ND MN IA NE WY MT"),
    "NE": (u"內布拉斯加州", "Nebraska", "MW", u"林肯", (40.81, -96.68), u"奧馬哈", 196.2, 200330, 1867, 37, u"剝玉米殼州", "SD IA MO KS CO WY"),
    "KS": (u"堪薩斯州", "Kansas", "MW", u"托皮卡", (39.05, -95.68), u"威奇托", 293.8, 213100, 1861, 34, u"向日葵州", "NE MO OK CO"),
    "DE": (u"德拉瓦州", "Delaware", "S", u"多佛", (39.16, -75.52), u"威明頓", 98.9, 6446, 1787, 1, u"第一州", "MD PA NJ"),
    "MD": (u"馬里蘭州", "Maryland", "S", u"安納波利斯", (38.98, -76.49), u"巴爾的摩", 617.7, 32131, 1788, 7, u"老防線州", "PA DE VA WV"),
    "VA": (u"維吉尼亞州", "Virginia", "S", u"里奇蒙", (37.54, -77.44), u"維吉尼亞海灘", 863.1, 110787, 1788, 10, u"老自治領", "MD WV KY TN NC"),
    "WV": (u"西維吉尼亞州", "West Virginia", "S", u"查爾斯頓", (38.35, -81.63), u"查爾斯頓", 179.4, 62756, 1863, 35, u"山州", "OH PA MD VA KY"),
    "NC": (u"北卡羅來納州", "North Carolina", "S", u"羅里", (35.78, -78.64), u"夏洛特", 1043.9, 139391, 1789, 12, u"焦油腳跟州", "VA TN GA SC"),
    "SC": (u"南卡羅來納州", "South Carolina", "S", u"哥倫比亞", (34.00, -81.03), u"查爾斯頓", 511.8, 82933, 1788, 8, u"矮棕櫚州", "NC GA"),
    "GA": (u"喬治亞州", "Georgia", "S", u"亞特蘭大", (33.75, -84.39), u"亞特蘭大", 1071.1, 153910, 1788, 4, u"桃子州", "FL AL TN NC SC"),
    "FL": (u"佛羅里達州", "Florida", "S", u"塔拉哈西", (30.44, -84.28), u"傑克遜維爾", 2153.8, 170312, 1845, 27, u"陽光州", "AL GA"),
    "KY": (u"肯塔基州", "Kentucky", "S", u"法蘭克福", (38.20, -84.87), u"路易維爾", 450.6, 104656, 1792, 15, u"藍草州", "IL IN OH WV VA TN MO"),
    "TN": (u"田納西州", "Tennessee", "S", u"納許維爾", (36.16, -86.78), u"納許維爾", 691.1, 109153, 1796, 16, u"志願者州", "KY VA NC GA AL MS AR MO"),
    "AL": (u"阿拉巴馬州", "Alabama", "S", u"蒙哥馬利", (32.38, -86.30), u"杭茨維爾", 502.4, 135767, 1819, 22, u"迪克西之心", "FL GA MS TN"),
    "MS": (u"密西西比州", "Mississippi", "S", u"傑克遜", (32.30, -90.18), u"傑克遜", 296.1, 125438, 1817, 20, u"木蘭州", "LA AR TN AL"),
    "AR": (u"阿肯色州", "Arkansas", "S", u"小岩城", (34.75, -92.29), u"小岩城", 301.2, 137732, 1836, 25, u"自然之州", "MO TN MS LA TX OK"),
    "LA": (u"路易斯安那州", "Louisiana", "S", u"巴頓魯治", (30.45, -91.19), u"紐奧良", 465.8, 135659, 1812, 18, u"鵜鶘州", "TX AR MS"),
    "OK": (u"奧克拉荷馬州", "Oklahoma", "S", u"奧克拉荷馬市", (35.47, -97.52), u"奧克拉荷馬市", 395.9, 181037, 1907, 46, u"搶先州", "KS MO AR TX NM CO"),
    "TX": (u"德克薩斯州", "Texas", "S", u"奧斯汀", (30.27, -97.74), u"休士頓", 2914.6, 695662, 1845, 28, u"孤星州", "NM OK AR LA"),
    "MT": (u"蒙大拿州", "Montana", "W", u"海倫娜", (46.59, -112.04), u"比林斯", 108.4, 380831, 1889, 41, u"寶藏州", "ID WY SD ND"),
    "WY": (u"懷俄明州", "Wyoming", "W", u"夏延", (41.14, -104.82), u"夏延", 57.7, 253335, 1890, 44, u"平等州", "MT SD NE CO UT ID"),
    "CO": (u"科羅拉多州", "Colorado", "W", u"丹佛", (39.74, -104.99), u"丹佛", 577.4, 269601, 1876, 38, u"百年州", "WY NE KS OK NM UT"),
    "NM": (u"新墨西哥州", "New Mexico", "W", u"聖塔菲", (35.69, -105.94), u"阿布奎基", 211.8, 314917, 1912, 47, u"魅力之地", "AZ CO OK TX"),
    "AZ": (u"亞利桑那州", "Arizona", "W", u"鳳凰城", (33.45, -112.07), u"鳳凰城", 715.2, 295234, 1912, 48, u"大峽谷州", "CA NV UT NM"),
    "UT": (u"猶他州", "Utah", "W", u"鹽湖城", (40.76, -111.89), u"鹽湖城", 327.2, 219882, 1896, 45, u"蜂巢州", "ID WY CO AZ NV"),
    "ID": (u"愛達荷州", "Idaho", "W", u"波夕", (43.62, -116.20), u"波夕", 183.9, 216443, 1890, 43, u"寶石州", "WA OR NV UT WY MT"),
    "NV": (u"內華達州", "Nevada", "W", u"卡森市", (39.16, -119.77), u"拉斯維加斯", 310.5, 286380, 1864, 36, u"銀州", "CA OR ID UT AZ"),
    "CA": (u"加利福尼亞州", "California", "W", u"沙加緬度", (38.58, -121.49), u"洛杉磯", 3953.8, 423967, 1850, 31, u"黃金州", "OR NV AZ"),
    "OR": (u"奧勒岡州", "Oregon", "W", u"塞勒姆", (44.94, -123.04), u"波特蘭", 423.7, 254799, 1859, 33, u"河狸州", "WA ID NV CA"),
    "WA": (u"華盛頓州", "Washington", "W", u"奧林匹亞", (47.04, -122.90), u"西雅圖", 770.5, 184661, 1889, 42, u"常青州", "ID OR"),
    "AK": (u"阿拉斯加州", "Alaska", "W", u"朱諾", (58.30, -134.42), u"安克拉治", 73.3, 1723337, 1959, 49, u"最後的邊疆", ""),
    "HI": (u"夏威夷州", "Hawaii", "W", u"檀香山", (21.31, -157.86), u"檀香山", 145.5, 28313, 1959, 50, u"阿囉哈州", ""),
}

ORDER = ["ME", "NH", "VT", "MA", "RI", "CT", "NY", "NJ", "PA",
         "OH", "IN", "IL", "MI", "WI", "MN", "IA", "MO", "ND", "SD", "NE", "KS",
         "DE", "MD", "VA", "WV", "NC", "SC", "GA", "FL", "KY", "TN", "AL", "MS", "AR", "LA", "OK", "TX",
         "MT", "WY", "CO", "NM", "AZ", "UT", "ID", "NV", "CA", "OR", "WA", "AK", "HI"]
LESSON = {c: i + 4 for i, c in enumerate(ORDER)}          # 第 4～53 課
SMALL = {"RI", "DE", "CT", "NJ", "MD", "MA", "NH", "VT"}
SCHEMATIC = {"DE", "FL", "MO", "WA", "WV", "WY", "CA", "OK"}     # 州旗中有州徽、只畫構圖的
SHORT = {"MA": u"麻州", "PA": u"賓州", "CA": u"加州", "TX": u"德州"}


def nm(c):
    return BASIC[c][0]


def part(c):
    return c if c in ("AK", "HI") else "48"


def cap_xy(c):
    lat, lon = BASIC[c][4]
    return us_xy(lon, lat, part(c))


def wan(x):
    """人口（萬）→ 文字。"""
    if x >= 100:
        return u"約 %s 萬" % format(int(round(x)), ",")
    return u"約 %.1f 萬" % x


def area_txt(a):
    r = a / float(TW_AREA)
    cmp_ = (u"約台灣的 %.1f 倍" % r) if r >= 1.15 else (u"和台灣差不多大" if r >= 0.85 else u"約台灣的 %d%%" % round(r * 100))
    return u"%s 平方公里（%s）" % (format(a, ","), cmp_)


# ---------- 位置圖 ----------
def locmap(c):
    near = BASIC[c][11].split()
    lx, ly = centroid(US_PATHS[c])
    x0, y0, x1, y1 = bbox_of(US_PATHS[c])
    small = c in SMALL
    if small:                       # 小州的名字放到海上，避免蓋住
        lab = (nm(c), min(x1 + 52, US_VB[0] - 40), (y0 + y1) / 2 + 22)
    elif c == "HI":
        lab = (nm(c), lx + 10, y0 - 8)
    else:
        lab = (nm(c), lx, ly + 18 if (y1 - y0) > 40 else y0 - 6)
    g, vb = static_map(US_VB, US_PATHS, c, near, star=cap_xy(c), label=lab, small=small)
    items = [(HL_, nm(c))] + ([(NEAR_, u"鄰州")] if near else []) + [("star", u"首府 " + BASIC[c][3])]
    g += legend(14 if c not in ("AK", "HI") else 470, US_VB[1] - 8, items)
    cap = u"%s的位置（紅色）。" % nm(c) + (u"橘色是相鄰的州；" if near else u"") + \
        (u"阿拉斯加與夏威夷不和本土相連，地圖上以縮小、移位的插圖畫在左下角（實際上阿拉斯加大得多）。" if c in ("AK", "HI") else u"") + u"★ 是首府。"
    return ("fig", g, vb, cap)




def overview_map(fill, labels=(), cap=u"", legend_items=None):
    """全美地圖：fill={code: 顏色}。"""
    g = []
    for k, d in sorted(US_PATHS.items()):
        g.append('<path d="%s" fill="%s" stroke="var(--surface)" stroke-width="0.8"/>' % (d, fill.get(k, "#b7c4d4")))
    for t, x, y in labels:
        g.append('<text x="%d" y="%d" font-size="10" text-anchor="middle" fill="var(--text)" stroke="var(--surface)" '
                 'stroke-width="3" paint-order="stroke">%s</text>' % (x, y, t))
    if legend_items:
        g.append(legend(14, US_VB[1] - 8, legend_items))
    return ("fig", "\n".join(g), "0 0 %d %d" % tuple(US_VB), cap)


# ---------- 互動地圖 ----------
def _dataset():
    items = []
    for c in ORDER:
        b = BASIC[c]
        x, y = centroid(US_PATHS[c])
        items.append({"c": c, "n": b[0], "e": b[1], "p": US_PATHS[c], "x": int(x), "y": int(y), "L": LESSON[c], "g": b[2],
                      "v": {"pop": b[6], "area": round(b[7] / 10000.0, 1), "den": round(b[6] * 10000 / b[7], 1), "year": b[8], "ord": b[9]},
                      "f": [[u"首府", b[3]], [u"最大城市", b[5]], [u"人口", wan(b[6])], [u"加入", u"%d 年（第 %d 州）" % (b[8], b[9])], [u"綽號", b[10]]]})
    return {"vb": US_VB, "items": items, "unit": u"州", "groups": {k: list(v) for k, v in REGIONS.items()},
            "metrics": [["pop", u"人口", u"萬人", 1, u"2020 年人口普查。"], ["area", u"面積", u"萬 km²", 1, u"台灣約 3.6 萬平方公里。"],
                        ["den", u"人口密度", u"人/km²", 1, u"台灣約每平方公里 650 人，比美國任何一州都密集。"]],
            "joinNote": {1787: u"德拉瓦第一個批准憲法，所以自稱「第一州」。", 1788: u"新罕布夏是第 9 個批准憲法的州，憲法因此正式生效。",
                         1790: u"羅德島最後一個批准，十三州到齊。", 1845: u"德州原本是獨立的「德克薩斯共和國」。",
                         1850: u"淘金熱讓加州跳過「領地」階段直接成為州。", 1863: u"南北戰爭期間，西維吉尼亞從維吉尼亞分出來加入北方。",
                         1912: u"本土 48 州到齊。", 1959: u"阿拉斯加與夏威夷加入，五十州到齊，國旗變成 50 顆星。"}}


STLIB = geolib("__ustLib", _dataset())


def stw(cfg, maxw=760):
    return wdg("__ustLib-w", cfg, maxw)


stlesson = make_lesson(u"🗺️", ST_NOTE, STLIB, "__ustLib-w")


# ---------- 每州一課 ----------
def _tbl(rows):
    return ("t", [u"項目", u"內容"], rows)


def state_lesson(c, d):
    """d：sub、one、flag、flagsvg(可省)、geo、hist、econ、firms、food、cn、see、fun、q、pt"""
    b = BASIC[c]
    name = b[0]
    title_ = u"%s：%s" % (SHORT.get(c, name.replace(u"州", u"")) + u"州" if c in SHORT else name, d["sub"])
    rows = [[u"英文名稱", u"%s（郵政縮寫 %s）" % (b[1], c)], [u"所屬區域", REGIONS[b[2]][0]],
            [u"首府", b[3]], [u"最大城市", b[5]], [u"人口（2020）", wan(b[6]) + u"人"], [u"總面積", area_txt(b[7])],
            [u"加入聯邦", u"%d 年，第 %d 個州" % (b[8], b[9])], [u"綽號", b[10]],
            [u"鄰州", u"、".join(nm(x) for x in b[11].split()) or u"無（不與其他州相鄰）"]]
    if d.get("extra_rows"):
        rows += d["extra_rows"]
    body = [locmap(c),
            ("note", u"💡 一句話記住%s" % name, [("p", d["one"])]),
            ("h", u"基本資料"), _tbl(rows),
            ("h", u"州旗")]
    from ust_flags import flag, FLAGS
    fs, fw, fh = flag(c)
    simple = not getattr(FLAGS[c], "__name__", "").startswith("<lambda") and c not in SCHEMATIC
    body.append(("raw", u'<div class="content-figure" style="max-width:300px;margin-left:auto;margin-right:auto">'
                 u'<svg class="content-diagram" viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg">%s</svg>'
                 u'<figcaption>%s</figcaption></div>' % (fw, fh, fs, u"%s州旗（簡化示意圖）" % name if simple else
                                                         u"%s州旗的構圖示意：中央州徽的細節請看下方文字" % name)))
    body.append(("p", d["flag"]))
    body += [("h", u"地理與氣候"), ("p", d["geo"]),
             ("h", u"歷史重點")]
    body.append(("ul", d["hist"]) if isinstance(d["hist"], list) else ("p", d["hist"]))
    body += [("h", u"經濟與大企業"), ("p", d["econ"])]
    if d.get("firms"):
        body.append(("t", [u"企業", u"產業", u"總部所在"], [list(r) for r in d["firms"]]))
    body += [("h", u"代表食物"), ("ul", [u"<strong>%s</strong>：%s" % r for r in d["food"]]),
             ("h", u"華人社群"), ("p", d["cn"]),
             ("h", u"景點"), ("ul", [u"<strong>%s</strong>：%s" % r for r in d["see"]]),
             ("note", u"🤔 冷知識", [("ul", d["fun"])])]
    goals = [u"在地圖上找到%s，說出它的鄰州與首府" % name, u"認識%s的地理、歷史與經濟特色" % name, u"知道%s的代表食物、華人社群與景點" % name]
    point = d.get("pt") or (d["one"] + u" 首府是%s，最大城市是%s。" % (b[3], b[5]))
    check = [u"%s位在美國的哪個區域？和哪些州相鄰？" % name if b[11] else u"%s為什麼不和任何州相鄰？" % name,
             u"%s的首府是哪裡？最大城市又是哪裡？" % name, d["q"]]
    return stlesson(title_, d.get("desc", d["sub"]), goals, body, point, check)


def S(c, **d):
    return state_lesson(c, d)
