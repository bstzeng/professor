# -*- coding: utf-8 -*-
"""易經與塔羅兩個占卜主題的共用工具與資料。

- lesson()：每課結尾自動加上一個 callout（標題由各課指定）與一行文化說明
- 八卦、六十四卦資料（文王卦序），附自我檢查
- 畫卦（hexagram）與畫牌（tarot card）的 SVG 小工具
"""
from gen import Lesson
from ho_common import (T, R, C, E, P, A, box, flow, svg, title,
                       RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT)

PURPLE = "#9c89d6"
TEAL = "#5fa8a8"

NOTE_LINE = (u"本課介紹的是傳統占卜的方法、符號與文化；這些方法沒有經過科學驗證的預測力，"
             u"適合當作反思與文化認識的工具，重要決定請以實際資訊與專業意見為準。")


def lesson(title_, desc, goals, body, extra, check, fig=None, extra_title=u"動手試試", nxt=None):
    blocks = []
    for b in body:
        if b == "FIG":
            blocks.append(("fig", fig[0], fig[1], fig[2]))
        else:
            blocks.append(b)
    if fig and "FIG" not in body:
        blocks.insert(1, ("fig", fig[0], fig[1], fig[2]))
    blocks.append(("note", extra_title, [("p", extra)]))
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">📜 %s</p>' % NOTE_LINE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


# ---------- 八卦 ----------
# 爻由下往上排列，1＝陽爻、0＝陰爻
TRIGRAMS = {
    u"乾": ("111", u"☰", u"天", u"健", u"父", u"西北"),
    u"兌": ("110", u"☱", u"澤", u"悅", u"少女", u"西"),
    u"離": ("101", u"☲", u"火", u"麗", u"中女", u"南"),
    u"震": ("100", u"☳", u"雷", u"動", u"長男", u"東"),
    u"巽": ("011", u"☴", u"風", u"入", u"長女", u"東南"),
    u"坎": ("010", u"☵", u"水", u"陷", u"中男", u"北"),
    u"艮": ("001", u"☶", u"山", u"止", u"少男", u"東北"),
    u"坤": ("000", u"☷", u"地", u"順", u"母", u"西南"),
}
TRI_ORDER = [u"乾", u"兌", u"離", u"震", u"巽", u"坎", u"艮", u"坤"]   # 先天八卦數 1～8
TRI_BY_LINES = dict((v[0], k) for k, v in TRIGRAMS.items())

# 文王卦序：(卦名, 上卦, 下卦, 一句話卦意)
HEX = [
    (u"乾", u"乾", u"乾", u"剛健自強，開創與領導"),
    (u"坤", u"坤", u"坤", u"柔順包容，承載與配合"),
    (u"屯", u"坎", u"震", u"萬事起頭難，艱難中萌芽"),
    (u"蒙", u"艮", u"坎", u"蒙昧待啟，學習與教導"),
    (u"需", u"坎", u"乾", u"等待時機，耐心準備"),
    (u"訟", u"乾", u"坎", u"爭訟衝突，宜和解不宜爭到底"),
    (u"師", u"坤", u"坎", u"率眾出師，紀律與領導"),
    (u"比", u"坎", u"坤", u"親近依附，團結合作"),
    (u"小畜", u"巽", u"乾", u"小有積蓄，力量尚待累積"),
    (u"履", u"乾", u"兌", u"如履虎尾，謹慎守禮"),
    (u"泰", u"坤", u"乾", u"天地交流，通達安泰"),
    (u"否", u"乾", u"坤", u"天地不交，閉塞不通"),
    (u"同人", u"乾", u"離", u"與人同心，志同道合"),
    (u"大有", u"離", u"乾", u"大有所得，豐盛而需謙守"),
    (u"謙", u"坤", u"艮", u"謙虛退讓，終有所成"),
    (u"豫", u"震", u"坤", u"安樂愉悅，預先準備"),
    (u"隨", u"兌", u"震", u"隨順時勢，擇善而從"),
    (u"蠱", u"艮", u"巽", u"積弊已久，整治革新"),
    (u"臨", u"坤", u"兌", u"居高臨下，親臨照顧"),
    (u"觀", u"巽", u"坤", u"觀察省思，以身示範"),
    (u"噬嗑", u"離", u"震", u"咬合除障，明法斷事"),
    (u"賁", u"艮", u"離", u"文飾美化，重質也重文"),
    (u"剝", u"艮", u"坤", u"剝落衰退，宜守不宜進"),
    (u"復", u"坤", u"震", u"一陽來復，重新開始"),
    (u"無妄", u"乾", u"震", u"真誠無妄，不存僥倖"),
    (u"大畜", u"艮", u"乾", u"大有蓄積，厚積而發"),
    (u"頤", u"艮", u"震", u"頤養身心，慎言節食"),
    (u"大過", u"兌", u"巽", u"過度失衡，非常之時"),
    (u"坎", u"坎", u"坎", u"重重險陷，守信而行"),
    (u"離", u"離", u"離", u"光明依附，文明與熱情"),
    (u"咸", u"兌", u"艮", u"相互感應，真心交流"),
    (u"恆", u"震", u"巽", u"持之以恆，守常久遠"),
    (u"遯", u"乾", u"艮", u"適時退避，保全實力"),
    (u"大壯", u"震", u"乾", u"聲勢壯大，戒躁守正"),
    (u"晉", u"離", u"坤", u"光明上進，漸得晉升"),
    (u"明夷", u"坤", u"離", u"光明受傷，韜光養晦"),
    (u"家人", u"巽", u"離", u"家庭倫理，各守其位"),
    (u"睽", u"離", u"兌", u"乖離相違，求同存異"),
    (u"蹇", u"坎", u"艮", u"行路艱難，反求諸己"),
    (u"解", u"震", u"坎", u"困難解除，寬大化解"),
    (u"損", u"艮", u"兌", u"減損以益，捨得之道"),
    (u"益", u"巽", u"震", u"增益助人，把握時機"),
    (u"夬", u"兌", u"乾", u"果決去除，當斷則斷"),
    (u"姤", u"乾", u"巽", u"不期而遇，慎防誘惑"),
    (u"萃", u"兌", u"坤", u"人才薈萃，凝聚眾心"),
    (u"升", u"坤", u"巽", u"循序上升，積小成大"),
    (u"困", u"兌", u"坎", u"困境受阻，守志待時"),
    (u"井", u"坎", u"巽", u"井水養人，修德不窮"),
    (u"革", u"兌", u"離", u"變革除舊，順天應人"),
    (u"鼎", u"離", u"巽", u"鼎新立制，穩定成就"),
    (u"震", u"震", u"震", u"震動驚懼，警惕自省"),
    (u"艮", u"艮", u"艮", u"適可而止，靜定內省"),
    (u"漸", u"巽", u"艮", u"循序漸進，穩步發展"),
    (u"歸妹", u"震", u"兌", u"婚嫁之事，名分與分寸"),
    (u"豐", u"震", u"離", u"豐盛盛大，盛極防衰"),
    (u"旅", u"離", u"艮", u"羈旅在外，謹慎守正"),
    (u"巽", u"巽", u"巽", u"謙遜順入，潛移默化"),
    (u"兌", u"兌", u"兌", u"喜悅溝通，和悅待人"),
    (u"渙", u"巽", u"坎", u"渙散離析，重新凝聚"),
    (u"節", u"坎", u"兌", u"節制有度，不過不苦"),
    (u"中孚", u"巽", u"兌", u"內心誠信，以誠感人"),
    (u"小過", u"震", u"艮", u"小有過越，宜下不宜上"),
    (u"既濟", u"坎", u"離", u"事已成功，慎防轉變"),
    (u"未濟", u"離", u"坎", u"事未完成，仍有可為"),
]


def hex_lines(n):
    """第 n 卦（1～64）的六爻，由下往上，'1'＝陽。"""
    _, up, lo, _ = HEX[n - 1]
    return TRIGRAMS[lo][0] + TRIGRAMS[up][0]


LINES_TO_NUM = dict((hex_lines(i), i) for i in range(1, 65))


def _selfcheck():
    assert len(HEX) == 64 and len(LINES_TO_NUM) == 64, u"六十四卦必須兩兩不同"
    for i in range(1, 64, 2):                       # 文王卦序：每對卦互綜（上下顛倒）或互錯（陰陽全反）
        a, b = hex_lines(i), hex_lines(i + 1)
        comp = "".join("1" if c == "0" else "0" for c in a)
        assert b == a[::-1] or (a == a[::-1] and b == comp), (i, a, b)


_selfcheck()


# ---------- SVG：畫卦 ----------

def hexagram(x, y, lines, w=60, h=8, gap=6, color=TXT, moving=(), mcolor=RED):
    """在 (x, y) 畫一個卦；lines 由下往上；y 是最上一爻的頂端。moving 為變爻的索引（0＝初爻）。"""
    out = []
    n = len(lines)
    for i, c in enumerate(lines):
        yy = y + (n - 1 - i) * (h + gap)
        col = mcolor if i in moving else color
        if c == "1":
            out.append(R(x, yy, w, h, col, col, 1, 1))
        else:
            seg = w * 0.42
            out.append(R(x, yy, seg, h, col, col, 1, 1))
            out.append(R(x + w - seg, yy, seg, h, col, col, 1, 1))
    return "".join(out)


def hex_block(x, y, n, w=44, label=True, color=TXT):
    """畫第 n 卦並在下方標上卦序與卦名。"""
    s = hexagram(x, y, hex_lines(n), w, 6, 4, color)
    if label:
        s += T(x + w / 2.0, y + 72, u"%d %s" % (n, HEX[n - 1][0]), 10, color)
    return s


# ---------- SVG：畫塔羅牌 ----------

SUITS = {
    u"權杖": (u"火", ORANGE, u"行動、熱情、事業"),
    u"聖杯": (u"水", BLUE, u"情感、關係、直覺"),
    u"寶劍": (u"風", PURPLE, u"思考、衝突、溝通"),
    u"錢幣": (u"土", GREEN, u"物質、工作、身體"),
}


def suit_icon(cx, cy, suit, s=1.0, color=None):
    c = color or SUITS[suit][1]
    if suit == u"權杖":
        return (R(cx - 3 * s, cy - 18 * s, 6 * s, 36 * s, c, c, 2, 1, op=0.8)
                + C(cx, cy - 20 * s, 5 * s, c, c, op=0.8))
    if suit == u"聖杯":
        return (P("M%g %g Q%g %g %g %g Z" % (cx - 12 * s, cy - 14 * s, cx, cy + 10 * s, cx + 12 * s, cy - 14 * s),
                  c, c, 1.2, op=0.5)
                + R(cx - 2 * s, cy + 2 * s, 4 * s, 12 * s, c, c, 1, 1, op=0.8)
                + R(cx - 8 * s, cy + 14 * s, 16 * s, 3 * s, c, c, 1, 1, op=0.8))
    if suit == u"寶劍":
        return (P("M%g %g L%g %g L%g %g Z" % (cx - 3 * s, cy + 8 * s, cx, cy - 22 * s, cx + 3 * s, cy + 8 * s),
                  c, c, 1, op=0.7)
                + R(cx - 10 * s, cy + 8 * s, 20 * s, 3 * s, c, c, 1, 1, op=0.8)
                + R(cx - 2 * s, cy + 11 * s, 4 * s, 9 * s, c, c, 1, 1, op=0.8))
    # 錢幣：圓中五芒星
    pts = []
    import math
    for k in range(5):
        a = -math.pi / 2 + k * 4 * math.pi / 5
        pts.append("%.1f,%.1f" % (cx + 9 * s * math.cos(a), cy + 9 * s * math.sin(a)))
    return (C(cx, cy, 14 * s, c, c, op=0.2)
            + '<polygon points="%s" fill="none" stroke="%s" stroke-width="1.2"/>' % (" ".join(pts), c))


def card(x, y, name, top=u"", w=70, h=110, color=GOLD, suit=None, reversed_=False, sub=None):
    """一張簡化的塔羅牌：外框、上方編號、中間圖示或文字、下方牌名。"""
    out = [R(x, y, w, h, color, "var(--surface)", 6, 1.8),
           R(x + 5, y + 5, w - 10, h - 10, color, "none", 4, 0.8)]
    if top:
        out.append(T(x + w / 2.0, y + 20, top, 9, color))
    if suit:
        out.append(suit_icon(x + w / 2.0, y + h / 2.0 - 2, suit, 0.9))
    elif sub:
        out.append(T(x + w / 2.0, y + h / 2.0 + 3, sub, 18, color))
    out.append(T(x + w / 2.0, y + h - 12, name, 9.5 if len(name) < 5 else 8.5, TXT))
    s = "".join(out)
    if reversed_:
        s = '<g transform="rotate(180 %g %g)">%s</g>' % (x + w / 2.0, y + h / 2.0, s)
    return s
