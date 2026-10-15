# -*- coding: utf-8 -*-
"""〈認識台灣的樹〉（tw_）共用：照片（維基共享資源外連）、示意圖與 TWLIB 互動元件。

照片：以 Special:FilePath 外連維基共享資源的檔案，點圖可到原始頁面查看作者與授權；
     載入失敗時顯示替代說明。沒有確認檔名的樹種，只提供「到維基共享資源搜尋」的連結。
TWLIB 元件（class="tw-w"）：
  cal   開花與賞葉月曆
另沿用 kd_common 的 tree（作為檢索表）與 nv_common 的卡片。
"""
from urllib.parse import quote, unquote
from cc_common import make_lesson, wdg, LS
from qt_common import BASEJS
from nv_common import NVLIB, nvw, ev, card, CB, CG, CO, CR, CP, CT, CY, CK
from kd_common import KDLIB, tree

TW_NOTE = (u"照片來自維基共享資源（Wikimedia Commons）的開放授權檔案，直接從維基共享資源載入；點照片可查看原始頁面上的作者與授權。"
           u"部分照片拍攝於台灣以外的地方，但為同一樹種。開花月份會因地區、海拔與當年氣候而前後變動。")

# 樹種：key -> (中文名, 學名, 原生/外來, [(檔名, 說明), ...])
SP = {
 "rong": (u"榕樹", "Ficus microcarpa", u"原生", [("Ficus_microcarpa.jpg", u"榕樹"), ("Ficus_microcarpa_-_Stem_&_leaves.jpg", u"枝葉與氣生根")]),
 "zhang": (u"樟樹", "Cinnamomum camphora", u"原生", [("Cinnamomum_camphora_-_camphor_tree.jpg", u"樟樹樹形"), ("Cinnamomum_camphora_tree_of_Seida_Okusu_B.jpg", u"日本愛知縣的樟樹老樹")]),
 "jiadong": (u"茄苳", "Bischofia javanica", u"原生", [("Bischofia_javanica_10.JPG", u"茄苳")]),
 "luan": (u"台灣欒樹", "Koelreuteria elegans", u"特有亞種", [("Chinese-Golden-rain_tree_(Koelreuteria_elegans),_Sao_Paulo_Brazil.jpg", u"欒樹開花（攝於巴西）")]),
 "heiban": (u"黑板樹", "Alstonia scholaris", u"外來", [("Alstonia_scholaris_by_kadavoor.JPG", u"黑板樹（攝於印度）"), ("Blackboard_Tree_(Alstonia_scholaris)_1.jpg", u"黑板樹")]),
 "dalan": (u"大葉欖仁", "Terminalia catappa", u"原生", [("Terminalia_catappa_1.jpg", u"大葉欖仁"), ("Desi_Badam_(Terminalia_catappa)_tree_in_Kolkata_W_IMG_2207.jpg", u"大葉欖仁樹形")]),
 "xiaolan": (u"小葉欖仁", "Terminalia mantaly", u"外來", [("Terminalia_mantaly_in_Hong_Kong.jpg", u"小葉欖仁（攝於香港）"), ("Terminalia_mantaly_(Philippines)_01.jpg", u"小葉欖仁的葉")]),
 "zitan": (u"印度紫檀", "Pterocarpus indicus", u"外來", [("Narra_tree_(Pterocarpus_indicus).jpg", u"印度紫檀"), ("Angsana_tree_fruit.jpg", u"有翅的圓盤狀果實")]),
 "shuihuang": (u"水黃皮", "Millettia pinnata", u"原生", [("Millettia_pinnata_1.jpg", u"水黃皮的花"), ("Pongamia_pinnata.jpg", u"水黃皮")]),
 "puti": (u"菩提樹", "Ficus religiosa", u"外來", [("Ficus_religiosa_Bo.jpg", u"菩提樹"), ("Bodhi_Baum_(Ficus_religiosa).jpg", u"菩提樹")]),
 "guangla": (u"光蠟樹", "Fraxinus griffithii", u"原生", []),
 "fengxiang": (u"楓香", "Liquidambar formosana", u"原生", [("Chinese_Sweet_Gum_(Liquidambar_formosana)_(23193757901).jpg", u"楓香的秋色（攝於日本神戶）")]),
 "kulian": (u"苦楝", "Melia azedarach", u"原生", [("Melia_azedarach_flower.JPG", u"苦楝的花"), ("Fruits_of_Melia_azedarach.jpg", u"苦楝的果實")]),
 "querong": (u"雀榕", "Ficus subpisocarpa", u"原生", []),
 "shanying": (u"山櫻花", "Prunus campanulata", u"原生", [("Prunus_cerasoides_var._canpanulata_04.jpg", u"山櫻花（緋寒櫻）"), ("Taiwan_Cherry_Blossom.JPG", u"陽明山的櫻花")]),
 "mumian": (u"木棉", "Bombax ceiba", u"外來", [("Silk_Cotton_Tree_(_Bombax_ceiba)_flowers.JPG", u"盛開的木棉"), ("Bombax_ceiba_-_Shimul_Flower.jpg", u"木棉花")]),
 "yanzijing": (u"艷紫荊", "Bauhinia × blakeana", u"外來", [("Bauhinia_blakeana_(Hong_Kong_Orchid_Tree).jpg", u"艷紫荊的花"), ("2010_07_21150_6757_Da'an_District,_Taipei,_Daan_Park,_Bauhinia_x_blakeana,_Taiwan.JPG", u"台北大安森林公園的艷紫荊")]),
 "liusu": (u"流蘇", "Chionanthus retusus", u"原生", [("Chinese_Fringe_Tree_--_Chionanthus_retusus.jpg", u"開花的流蘇"), ("Chionanthus_retusus3.jpg", u"流蘇的花")]),
 "youtong": (u"油桐", "Vernicia montana / V. fordii", u"外來", []),
 "abole": (u"阿勃勒", "Cassia fistula", u"外來", [("Golden_Shower_tree_(486405809).jpg", u"阿勃勒滿樹黃花"), ("Cassia_fistula_flowers.jpg", u"阿勃勒的花")]),
 "fenghuang": (u"鳳凰木", "Delonix regia", u"外來", [("Delonix_regia_(Flanboyant_tree).Ghana.JPG", u"鳳凰木（攝於迦納）"), ("Acacia_roja_-_Flamboyant_(Delonix_regia)_-_Flor_(14343692959).jpg", u"鳳凰木的花")]),
 "daziwei": (u"大花紫薇", "Lagerstroemia speciosa", u"外來", [("Banaba_Flower_(Lagerstroemia_speciosa).jpg", u"大花紫薇的花"), ("Inflorescence_of_Lagerstroemia_speciosa.JPG", u"大花紫薇的花序")]),
 "jiuqiong": (u"九芎", "Lagerstroemia subcostata", u"原生", [("Lagerstroemia_subcostata.jpg", u"九芎")]),
 "meiren": (u"美人樹", "Ceiba speciosa", u"外來", [("Ceiba_speciosa-3-cubbon_park-bangalore-India.jpg", u"開花的美人樹（攝於印度）"), ("C._speciosa-5.JPG", u"美人樹的花")]),
 "huangjin": (u"黃槿", "Hibiscus tiliaceus", u"原生", [("Hibiscus_tiliaceus,_Koh_Lipe_Thailand.jpg", u"黃槿"), ("Fou_-_sea_hibiscus_(Hibiscus_tiliaceus)_flowers_(Niue).jpg", u"黃槿的花")]),
 "haimeng": (u"海檬果", "Cerbera manghas", u"原生", [("Starr_050517-1485_Cerbera_manghas.jpg", u"海檬果的花與果（果實有劇毒）")]),
 "pingpo": (u"掌葉蘋婆", "Sterculia foetida", u"外來", [("Starr_080305-3289_Sterculia_foetida.jpg", u"掌葉蘋婆的果實"), ("Poon_tree_(2334256069).jpg", u"掌葉蘋婆")]),
 "mumahuang": (u"木麻黃", "Casuarina equisetifolia", u"外來", [("Casuarina_equesitifolia_tree.jpg", u"木麻黃")]),
 "lintou": (u"林投", "Pandanus odorifer", u"原生", [("Pandanu_odori_111025-19689_bml.JPG", u"林投的果實"), ("Pandan_Laut.jpg", u"海邊的林投")]),
 "qipan": (u"棋盤腳", "Barringtonia asiatica", u"原生", [("Barringtonia_asiatica_-_twin_flower.JPG", u"夜晚開放的棋盤腳花"), ("Barringtonia_asiatica,_Box_Fruit_Tree_(13883670469).jpg", u"四稜的果實")]),
 "fumu": (u"福木", "Garcinia subelliptica", u"原生", [("Fukugi_Tree_(Garcinia_subelliptica)_1.jpg", u"福木")]),
 "dawang": (u"大王椰子", "Roystonea regia", u"外來", [("Roystonea_regia.jpg", u"大王椰子"), ("Roystonea_regia_1.JPG", u"大王椰子")]),
 "pukui": (u"蒲葵", "Livistona chinensis", u"原生", [("Palma_livistonia_(Livistona_chinensis)_(14342419499).jpg", u"蒲葵")]),
 "xiangsi": (u"相思樹", "Acacia confusa", u"原生", [("Starr-090617-0941-Acacia_confusa-habit_view_bay-Kakipi_Gulch_Haiku-Maui_(24597530249).jpg", u"相思樹樹形（攝於夏威夷）"), ("Acacia_confusa_seeds.jpg", u"相思樹的種子")]),
 "goushu": (u"構樹", "Broussonetia papyrifera", u"原生", [("Broussonetia_papyrifera_-_Paper_mulberry_02.jpg", u"構樹的果實"), ("Broussonetia_papyrifera_-_fleurs_m%C3%A2les.jpg", u"構樹的雄花序")]),
 "xuetong": (u"血桐", "Macaranga tanarius", u"原生", [("Macaranga_tanarius_Leaves_and_Fruit_1.jpg", u"血桐的盾狀葉與果實"), ("Macaranga_tanarius_Tree_1.jpg", u"血桐")]),
 "mangguo": (u"芒果", "Mangifera indica", u"外來", [("Mango_tree_in_full_bloom_01.jpg", u"開花的芒果樹"), ("Mangifera_indica_flowers2.JPG", u"芒果的花")]),
 "hongkuai": (u"紅檜", "Chamaecyparis formosensis", u"特有", [("Chamaecyparis_formosensis.jpg", u"阿里山香林神木（紅檜）"), ("Taiwan_Red_Cypress.jpg", u"阿里山的紅檜"), ("No.28_Giant_Tree_in_Alishan.jpg", u"阿里山的巨木")]),
 "bianbai": (u"台灣扁柏", "Chamaecyparis obtusa var. formosana", u"特有變種", []),
 "taiwanshan": (u"台灣杉", "Taiwania cryptomerioides", u"原生", [("Taiwania_cryptomerioides_0zz.jpg", u"台灣杉（攝於美國國家樹木園）"), ("Taiwania_cryptomerioides_-_Mendocino_Coast_Botanical_Gardens_-_DSC02059.JPG", u"台灣杉（攝於美國加州）")]),
 "xiaonan": (u"台灣肖楠", "Calocedrus formosana", u"特有", []),
 "ersong": (u"台灣二葉松", "Pinus taiwanensis", u"特有", []),
 "ju": (u"台灣櫸", "Zelkova serrata", u"原生", [("Zelkova_serrata.JPG", u"櫸木（攝於韓國）"), ("Giant_zelkova_tree_of_Mount_Mitake_Ome_Tokyo.jpg", u"櫸木巨木（攝於日本）")]),
 "yinhehuan": (u"銀合歡", "Leucaena leucocephala", u"外來入侵", [("Leucaena_leucocephala.jpg", u"銀合歡"), ("Subabool_(Leucaena_leucocephala)_dried_pods_in_Kolkata_W_IMG_4301.jpg", u"銀合歡大量的豆莢")]),
 "baiqian": (u"白千層", "Melaleuca leucadendra", u"外來", [("Melaleuca_leucadendra_1.jpg", u"白千層與白色的樹皮"), ("White_Tea_tree_(4591134659).jpg", u"白千層")]),
 "alishan": (u"阿里山神木", "Chamaecyparis formosensis", u"特有", [("Alishan_Sacred_Tree_1920.jpg", u"1920 年代的阿里山神木"), ("Alisan_old_god_tree.JPG", u"阿里山的神木")]),
}


def _fp(f):
    return quote(unquote(f).replace(" ", "_"), safe="_().,'-")


def P(key, n=2, cap=None):
    """樹種照片區塊：最多 n 張，附來源連結與「更多照片」搜尋連結。"""
    zh, sci, org, files = SP[key]
    srch = u"https://commons.wikimedia.org/w/index.php?title=Special:MediaSearch&type=image&search=" + quote(sci.split(" /")[0])
    figs = []
    for f, c in files[:n]:
        page = u"https://commons.wikimedia.org/wiki/File:" + _fp(f)
        img = u"https://commons.wikimedia.org/wiki/Special:FilePath/" + _fp(f) + u"?width=640"
        figs.append(
            u'<figure style="flex:1 1 230px;margin:0;min-width:0"><a href="%s" target="_blank" rel="noopener" style="display:block;text-decoration:none">'
            u'<img src="%s" alt="%s" loading="lazy" referrerpolicy="no-referrer" style="width:100%%;height:230px;object-fit:cover;border-radius:8px;background:var(--accent-soft);display:block" '
            u'onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'">'
            u'<span style="display:none;height:230px;border-radius:8px;background:var(--accent-soft);align-items:center;justify-content:center;text-align:center;padding:12px;color:var(--text-muted);font-size:0.9em">照片暫時無法載入<br>點這裡到維基共享資源看原圖</span></a>'
            u'<figcaption style="font-size:0.82em;color:var(--text-muted);margin-top:4px;line-height:1.5">%s<br>來源：Wikimedia Commons（點照片看作者與授權）</figcaption></figure>'
            % (page, img, zh + u"：" + c, c))
    head = u'<div style="font-weight:bold;margin-bottom:6px">%s <i style="font-weight:normal;color:var(--text-muted)">%s</i>　<span style="font-size:0.82em;padding:1px 8px;border-radius:10px;background:var(--accent-soft)">%s</span></div>' % (zh, sci, org)
    body = u'<div style="display:flex;flex-wrap:wrap;gap:10px">%s</div>' % u"".join(figs) if figs else \
        u'<div style="padding:10px 12px;border-radius:8px;background:var(--accent-soft);color:var(--text-muted)">這個樹種本課暫未附照片，請參考下方的辨識重點與示意圖。</div>'
    more = u'<div style="font-size:0.85em;margin-top:6px"><a href="%s" target="_blank" rel="noopener">🔎 到維基共享資源搜尋更多「%s」的照片</a></div>' % (srch, zh)
    return ("raw", u'<div class="content-figure" style="text-align:left;margin:12px 0;padding:10px;border:1px solid var(--border);border-radius:10px">%s%s%s</div>' % (head, body, more))


def ID(rows):
    """辨識重點表：[[項目, 內容], ...]"""
    return ("t", [u"辨識重點", u""], rows)


# ---------- 示意圖（SVG） ----------
G = "#5aa469"
D = "#2f6b3a"


def _leaf(cx, cy, w, h, rot=0, fill=G):
    return (u'<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="%s" stroke="%s" stroke-width="1" transform="rotate(%g %g %g)"/>'
            % (cx, cy, w / 2.0, h / 2.0, fill, D, rot, cx, cy))


def _t(x, y, s, sz=12):
    return u'<text x="%g" y="%g" font-size="%g" text-anchor="middle" fill="currentColor">%s</text>' % (x, y, sz, s)


def _svg(vb, inner, cap):
    return ("raw", u'<figure class="content-figure" style="margin:12px auto;max-width:680px"><svg viewBox="%s" style="width:100%%;display:block;color:var(--text)">%s</svg>'
                   u'<figcaption style="font-size:0.85em;color:var(--text-muted);text-align:center">%s</figcaption></figure>' % (vb, inner, cap))


def fig_arrange():
    g = u""
    for i, (x, name) in enumerate([(80, u"互生"), (240, u"對生"), (400, u"輪生")]):
        g += u'<line x1="%g" y1="30" x2="%g" y2="210" stroke="#7a5a3a" stroke-width="4"/>' % (x, x)
        for k in range(4):
            y = 50 + k * 42
            if name == u"互生":
                s = -1 if k % 2 == 0 else 1
                g += _leaf(x + s * 30, y, 50, 18, s * 20)
            elif name == u"對生":
                g += _leaf(x - 30, y, 50, 18, -20) + _leaf(x + 30, y, 50, 18, 20)
        if name == u"輪生":
            for y in (70, 160):
                for a in (-40, 0, 40, 180):
                    import math
                    r = math.radians(a)
                    g += _leaf(x + 34 * math.cos(r), y - 12 * math.sin(r), 50, 16, -a)
        g += _t(x, 235, name, 15)
    g += _t(80, 255, u"每節一片，左右交錯", 11) + _t(240, 255, u"每節兩片，相對", 11) + _t(400, 255, u"每節三片以上", 11)
    return _svg("0 0 480 265", g, u"葉序：葉在枝條上的排列方式")


def fig_compound():
    g = u""
    # 單葉
    g += _leaf(60, 110, 50, 110) + u'<line x1="60" y1="165" x2="60" y2="200" stroke="#7a5a3a" stroke-width="3"/>' + _t(60, 230, u"單葉", 13)
    # 三出複葉
    g += u'<line x1="170" y1="200" x2="170" y2="110" stroke="#7a5a3a" stroke-width="3"/>' + _leaf(170, 80, 34, 70) + _leaf(140, 120, 28, 60, -50) + _leaf(200, 120, 28, 60, 50) + _t(170, 230, u"三出複葉", 13)
    # 羽狀複葉
    g += u'<line x1="290" y1="200" x2="290" y2="40" stroke="#7a5a3a" stroke-width="3"/>'
    for k in range(4):
        y = 60 + k * 34
        g += _leaf(268, y, 36, 16, -15) + _leaf(312, y, 36, 16, 15)
    g += _leaf(290, 36, 16, 34) + _t(290, 230, u"羽狀複葉", 13)
    # 掌狀複葉
    import math
    g += u'<line x1="410" y1="200" x2="410" y2="130" stroke="#7a5a3a" stroke-width="3"/>'
    for a in (-70, -35, 0, 35, 70):
        r = math.radians(a - 90)
        g += _leaf(410 + 42 * math.cos(r), 130 + 42 * math.sin(r), 22, 66, a)
    g += _t(410, 230, u"掌狀複葉", 13)
    g += _t(240, 255, u"判斷技巧：複葉的小葉基部沒有芽；整片複葉的葉柄基部才有芽", 11)
    return _svg("0 0 480 265", g, u"單葉與複葉：單葉（榕樹、樟樹）、三出複葉（茄苳）、羽狀複葉（苦楝、光蠟樹）、掌狀複葉（木棉、美人樹）")


def fig_shape():
    g = u""
    shapes = [(u"卵形", 40, 80), (u"橢圓形", 34, 90), (u"心形", 0, 0), (u"披針形", 18, 100), (u"掌狀裂", 0, 0)]
    for i, (n, w, h) in enumerate(shapes):
        x = 55 + i * 92
        if n == u"心形":
            g += u'<path d="M%g 60 C%g 30 %g 50 %g 80 C%g 110 %g 135 %g 150 C%g 135 %g 110 %g 80 C%g 50 %g 30 %g 60 Z" fill="%s" stroke="%s"/>' % (
                x, x - 18, x - 42, x - 40, x - 38, x - 10, x, x + 10, x + 38, x + 40, x + 42, x + 18, x, G, D)
            g += u'<path d="M%g 150 L%g 175" stroke="%s" stroke-width="2"/>' % (x, x + 8, D)
        elif n == u"掌狀裂":
            g += u'<path d="M%g 150 L%g 100 L%g 55 L%g 95 L%g 45 L%g 95 L%g 55 L%g 100 Z" fill="%s" stroke="%s"/>' % (x, x - 40, x - 30, x - 12, x, x + 12, x + 30, x + 40, G, D)
        else:
            g += _leaf(x, 100, w, h)
        g += _t(x, 200, n, 13)
    g += _t(240, 225, u"例：茄苳（卵形小葉）、樟樹（橢圓形）、菩提樹與黃槿（心形）、相思樹（披針形的假葉）、楓香（掌狀三裂）", 10)
    return _svg("0 0 480 235", g, u"常見的葉形")


def fig_margin():
    g = u""
    def edge(x, kind):
        pts = []
        import math
        for k in range(0, 21):
            t = k / 20.0
            y = 40 + 140 * t
            w = 38 * math.sin(math.pi * t)
            if kind == "s" and 0 < k < 20 and k % 2:
                w += 6
            if kind == "w":
                w += 5 * math.sin(k * 1.3)
            pts.append((x + w, y))
        left = [(2 * x - px, py) for px, py in reversed(pts)]
        d = "M" + " L".join("%g %g" % p for p in pts + left) + " Z"
        return u'<path d="%s" fill="%s" stroke="%s"/>' % (d, G, D)
    for i, (k, n) in enumerate([("e", u"全緣"), ("s", u"鋸齒緣"), ("w", u"波狀緣")]):
        x = 90 + i * 150
        g += edge(x, k) + _t(x, 205, n, 13)
    return _svg("0 0 480 215", g, u"葉緣：全緣（榕樹、大葉欖仁）、鋸齒緣（茄苳、山櫻花、台灣櫸）、波狀緣（樟樹的葉緣常略呈波狀）")


def fig_forest():
    zones = [(u"高山植群", u"3600 公尺以上", u"玉山圓柏、高山杜鵑", "#c9d6e2"), (u"冷杉林帶", u"約 3100–3600", u"台灣冷杉", "#7fa3a8"),
             (u"鐵杉雲杉林帶", u"約 2500–3100", u"台灣鐵杉、台灣雲杉、台灣二葉松", "#6f9a7a"), (u"櫟林帶（含檜木林）", u"約 1500–2500", u"紅檜、扁柏、殼斗科樹木；雲霧帶", "#5d8c5e"),
             (u"楠櫧林帶", u"約 500–1500", u"樟科（楠木類）、殼斗科（櫧類）、台灣杉、肖楠", "#4f7f4a"), (u"榕楠林帶", u"約 500 公尺以下", u"榕樹、茄苳、相思樹、構樹", "#3f6e3a")]
    g = u""
    for i, (n, h, sp, c) in enumerate(zones):
        y0, y1 = 10 + i * 50, 10 + (i + 1) * 50
        xl0, xr0 = 200 - (y0 - 10) * 190 / 300.0 - 20, 200 + (y0 - 10) * 190 / 300.0 + 20
        xl1, xr1 = 200 - (y1 - 10) * 190 / 300.0 - 20, 200 + (y1 - 10) * 190 / 300.0 + 20
        g += u'<polygon points="%g,%g %g,%g %g,%g %g,%g" fill="%s" stroke="#fff"/>' % (xl0, y0, xr0, y0, xr1, y1, xl1, y1, c)
        g += u'<text x="200" y="%g" font-size="%g" text-anchor="middle" fill="%s" font-weight="bold">%s</text>' % (y0 + 31, 13 if i else 11, "#123" if i < 2 else "#fff", n)
    rows = u"".join(u'<tr><td style="padding:3px 6px;white-space:nowrap"><span style="display:inline-block;width:10px;height:10px;background:%s;margin-right:4px"></span>%s</td><td style="padding:3px 6px">%s</td><td style="padding:3px 6px">%s</td></tr>' % (c, n, h, sp) for n, h, sp, c in zones)
    return ("raw", u'<figure class="content-figure" style="margin:12px auto;max-width:680px"><svg viewBox="0 0 400 315" style="width:100%%;max-width:440px;display:block;margin:auto">%s</svg>'
                   u'<div style="overflow-x:auto"><table style="border-collapse:collapse;font-size:0.85em;width:100%%;margin-top:6px"><tr><th style="text-align:left;padding:3px 6px">森林帶</th><th style="text-align:left;padding:3px 6px">海拔</th><th style="text-align:left;padding:3px 6px">代表樹種</th></tr>%s</table></div>'
                   u'<figcaption style="font-size:0.85em;color:var(--text-muted);text-align:center">台灣的森林帶（依常見的植群分類，各帶的海拔界線會因南北、坡向而不同）</figcaption></figure>' % (g, rows))


# ---------- 開花與賞葉月曆 ----------
CAL = [
    [u"山櫻花", [1, 2], "#d9467a", 19, u"花"], [u"木棉", [2, 3], "#e2552b", 20, u"花"], [u"洋紫荊", [3, 4], "#c77ab8", 21, u"花"], [u"艷紫荊", [10, 11, 12, 1, 2, 3], "#a8327a", 21, u"花"],
    [u"苦楝", [3, 4], "#a28bd6", 17, u"花"], [u"流蘇", [3, 4], "#9aa", 22, u"花（白）"], [u"印度紫檀", [3, 4], "#d9b02b", 13, u"花"], [u"油桐", [4, 5], "#9aa", 23, u"花（白）"],
    [u"相思樹", [4, 5], "#d9b02b", 34, u"花"], [u"水黃皮", [4, 5, 6], "#b8a0d9", 13, u"花"], [u"阿勃勒", [5, 6, 7], "#e6c21e", 24, u"花"], [u"鳳凰木", [5, 6, 7], "#e2442b", 25, u"花"],
    [u"大花紫薇", [5, 6, 7], "#9b6bd1", 26, u"花"], [u"九芎", [6, 7, 8], "#9aa", 26, u"花（白）"], [u"黃槿", [5, 6, 7, 8], "#e6c21e", 28, u"花"], [u"台灣欒樹", [9, 10], "#e6c21e", 10, u"花（黃）"],
    [u"台灣欒樹", [10, 11], "#c0573f", 10, u"蒴果（紅褐）"], [u"美人樹", [10, 11, 12], "#e07aa8", 27, u"花"], [u"羊蹄甲", [9, 10, 11], "#c77ab8", 21, u"花"],
    [u"楓香", [11, 12, 1], "#d9822b", 16, u"紅葉"], [u"大葉欖仁", [12, 1, 2], "#c0392b", 12, u"紅葉"], [u"芒果", [1, 2, 3], "#c9b04a", 36, u"花"], [u"黑板樹", [10, 11, 12], "#9aa", 11, u"花（氣味濃）"],
]
TWLIB = r"""
(function () {
  if (window.__twLib) return; window.__twLib = 1;
""" + BASEJS + r"""
  function initCal(root, cfg) { head(root, cfg.q); var C = cfg.c, m = cfg.start || 4, bb = el('div'), out = el('div', 'margin-top:8px');
    root.appendChild(bb); root.appendChild(out);
    for (var i = 1; i <= 12; i++) (function (i) { var b = btn(i + ' 月', 'm' + i); b.addEventListener('click', function () { m = i; mark(bb, 'm' + i); draw(); }); bb.appendChild(b); })(i);
    function draw() { var r = C.filter(function (c) { return c[1].indexOf(m) >= 0; });
      var h = '<div style="font-weight:bold;margin-bottom:6px">' + m + ' 月可以看：' + r.length + ' 種</div><div style="display:flex;flex-wrap:wrap;gap:8px">';
      r.forEach(function (c) { h += '<a href="lesson-' + (c[3] < 10 ? '0' : '') + c[3] + '.html" style="text-decoration:none;color:var(--text);display:flex;align-items:center;gap:6px;padding:6px 10px;border:1px solid var(--border);border-radius:20px"><span style="width:14px;height:14px;border-radius:7px;background:' + c[2] + ';display:inline-block"></span>' + c[0] + '<span style="font-size:0.8em;color:var(--text-muted)">' + c[4] + '</span></a>'; });
      h += '</div><div style="margin-top:10px;overflow-x:auto"><table style="border-collapse:collapse;font-size:0.8em;min-width:520px"><tr><th style="text-align:left;padding:2px 6px">樹種</th>';
      for (var k = 1; k <= 12; k++) h += '<th style="width:26px;' + (k === m ? 'background:var(--accent-soft)' : '') + '">' + k + '</th>';
      h += '</tr>'; C.forEach(function (c) { h += '<tr><td style="padding:2px 6px;white-space:nowrap">' + c[0] + (c[4].indexOf('花') === 0 ? '' : '（' + c[4] + '）') + '</td>';
        for (var k = 1; k <= 12; k++) h += '<td style="padding:1px;' + (k === m ? 'background:var(--accent-soft)' : '') + '"><div style="height:12px;border-radius:3px;background:' + (c[1].indexOf(k) >= 0 ? c[2] : 'transparent') + '"></div></td>';
        h += '</tr>'; }); out.innerHTML = h + '</table></div><div style="font-size:0.82em;color:var(--text-muted);margin-top:6px">月份為台灣平地常見的大致時間，各地、各年會前後變動。點樹名可以到該課。</div>'; }
    mark(bb, 'm' + m); draw(); }
  function initAll() { document.querySelectorAll('.tw-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ cal: initCal })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def CALW(start=4):
    return wdg("tw-w", {"t": "cal", "q": u"開花與賞葉月曆：選月份，看當月可以欣賞的樹", "c": CAL, "start": start}, 720)


# ---------- 檢索表（沿用情境決策樹元件） ----------
def _a(name, n, why):
    return {"a": u"<b>可能是：%s</b>（第 %d 課）<br>%s" % (name, n, why)}


KEY = tree(u"認樹檢索表：依序回答問題，一步步找出可能的樹種（收錄本課程的常見樹種）", {
  "start": {"q": u"葉子是什麼樣子？", "o": [[u"像針或鱗片（松、柏、杉類）", "con"], [u"巨大的扇形或羽毛形，長在樹幹頂端（椰子、棕櫚）", "palm"], [u"一般的葉片", "leaf"]]},
  "con": {"q": u"葉的形狀？", "o": [[u"細長的針，兩根一束", "pine2"], [u"細長、分節的綠色小枝（不是真正的針葉），像松但長在海邊", "mumahuang"], [u"扁平的鱗片狀小葉，像柏", "kuai"], [u"短而硬、略彎的鑽形葉", "taiwanshan"]]},
  "pine2": _a(u"台灣二葉松（山上）或琉球松（平地造林）", 42, u"松樹靠「一束幾根針」來分：二葉松兩根一束，五葉松、華山松五根一束。"),
  "mumahuang": _a(u"木麻黃", 31, u"綠色的細枝其實是枝條，真正的葉退化成小鱗片，拉開會看到一節一節的。"),
  "kuai": _a(u"紅檜、台灣扁柏或台灣肖楠", 38, u"檜木的鱗葉排成扁平的枝片；肖楠的鱗葉較長、枝片也扁平，需要看毬果細節分辨（第 40 課）。"),
  "taiwanshan": _a(u"台灣杉", 39, u"葉為鑽形、略彎而堅硬，樹幹通直高大。"),
  "palm": {"q": u"葉的形狀？", "o": [[u"扇形（像一把扇子）", "pukui"], [u"羽毛形，樹幹灰白光滑、中段膨大", "dawang"]]},
  "pukui": _a(u"蒲葵", 33, u"葉大如扇，從前常用來做扇子（蒲扇）。"),
  "dawang": _a(u"大王椰子", 33, u"樹幹灰白、像水泥柱，中段常略為膨大；台大椰林大道就是牠。"),
  "leaf": {"q": u"是單葉還是複葉？（複葉：一根葉柄上長著好幾片小葉）", "o": [[u"單葉", "s"], [u"複葉", "c"]]},
  "c": {"q": u"複葉的形式？", "o": [[u"三片小葉（三出複葉）", "jiadong"], [u"小葉像手掌般從同一點長出（掌狀複葉）", "palmate"], [u"小葉排成兩列（羽狀複葉）", "pinnate"]]},
  "jiadong": _a(u"茄苳", 9, u"三出複葉、葉緣有鈍鋸齒，樹皮紅褐色、會片狀剝落。"),
  "palmate": {"q": u"樹幹的特徵？", "o": [[u"粗壯，枝條水平展開，早春先開大紅花再長葉", "mumian"], [u"樹幹綠色、有瘤狀的刺，秋天開粉紅花", "meiren"], [u"花有臭味，果實紅色像船", "pingpo"]]},
  "mumian": _a(u"木棉", 20, u"二、三月開橙紅色大花，五月棉絮飄落。"),
  "meiren": _a(u"美人樹", 27, u"樹幹綠色、有刺，常呈酒瓶狀；秋冬開粉紅色花。"),
  "pingpo": _a(u"掌葉蘋婆", 29, u"學名 foetida 就是「有臭味」的意思。"),
  "pinnate": {"q": u"葉是怎麼排在枝上的？", "o": [[u"對生（左右兩兩相對）", "guangla"], [u"互生", "pin2"]]},
  "guangla": _a(u"光蠟樹", 15, u"奇數羽狀複葉、對生；樹皮光滑、有白色斑塊，夏天常有獨角仙吸食樹液。"),
  "pin2": {"q": u"小葉是否還再分成小羽片（二回以上的羽狀複葉）？", "o": [[u"是，葉很細碎", "pin3"], [u"否，一回羽狀", "pin4"]]},
  "pin3": {"q": u"花的顏色？", "o": [[u"淡紫色小花，春天開；冬天掛黃色小果", "kulian"], [u"秋天開黃花，接著結紅褐色像燈籠的果實", "luan"], [u"夏天開火紅色大花", "fenghuang"], [u"小白花球，到處都有、豆莢很多", "yinhehuan"]]},
  "kulian": _a(u"苦楝", 17, u"二至三回羽狀複葉，小葉有鋸齒；台語叫「苦苓」。"),
  "luan": _a(u"台灣欒樹", 10, u"二回羽狀複葉，秋天依序出現黃花、紅褐色蒴果。"),
  "fenghuang": _a(u"鳳凰木", 25, u"二回羽狀複葉，小葉非常細小；長長的扁莢果。"),
  "yinhehuan": _a(u"銀合歡", 46, u"外來入侵種，二回羽狀複葉，白色球狀花，豆莢成串。"),
  "pin4": {"q": u"花或果的特徵？", "o": [[u"夏天長串的黃花垂下，果實像長棍子", "abole"], [u"春天滿樹小黃花，果實圓盤狀有翅", "zitan"], [u"粉紫或白色的蝶形花，豆莢扁平，常見於海邊", "shuihuang"]]},
  "abole": _a(u"阿勃勒", 24, u"一回偶數羽狀複葉，花序下垂如黃金雨，莢果圓筒狀可長達數十公分。"),
  "zitan": _a(u"印度紫檀", 13, u"奇數羽狀複葉，小葉互生；春天一次開滿黃花，很快就謝。"),
  "shuihuang": _a(u"水黃皮", 13, u"奇數羽狀複葉，小葉對生、較大；耐鹽，常見於海邊與公園。"),
  "s": {"q": u"葉是怎麼排在枝上的？", "o": [[u"互生", "sa"], [u"對生", "so"], [u"輪生（一個節上有三片以上）", "heiban"]]},
  "heiban": _a(u"黑板樹", 11, u"四到七片葉輪生，樹形層層分明；秋冬開花時氣味濃烈。"),
  "so": {"q": u"其他特徵？", "o": [[u"葉厚而亮，樹形整齊，常種成防風綠籬", "fumu"], [u"四月開滿白色細長的花，像下雪", "liusu"], [u"樹皮非常光滑、斑駁，夏天開白花或紫花", "jiuqiong"]]},
  "fumu": _a(u"福木", 32, u"葉厚革質、對生，枝葉茂密，是很好的防風樹。"),
  "liusu": _a(u"流蘇", 22, u"單葉對生，四月開白花，有「四月雪」之稱。"),
  "jiuqiong": _a(u"九芎或大花紫薇", 26, u"九芎樹皮光滑，被稱為「猴不爬」；大花紫薇夏天開紫色大花。"),
  "sa": {"q": u"葉的形狀或特徵？", "o": [[u"心形，葉尖拉成長尾巴", "puti"], [u"心形或圓形，葉柄長在葉片中間（盾狀）", "xuetong"], [u"心形，海邊常見，開黃花", "huangjin"], [u"掌狀裂（像手掌），秋冬變紅", "fengxiang"], [u"葉像兩片合在一起，前端裂開成羊蹄狀", "zijing"], [u"其他形狀", "sa2"]]},
  "puti": _a(u"菩提樹", 14, u"葉尖延長成「滴水葉尖」，是最好認的特徵之一。"),
  "xuetong": _a(u"血桐", 35, u"盾狀葉；折斷枝條流出的汁液接觸空氣後變成紅色。"),
  "huangjin": _a(u"黃槿", 28, u"心形葉，花黃色、中心暗紅，一朵花只開一天；葉可墊粿。"),
  "fengxiang": _a(u"楓香", 16, u"掌狀三裂葉、互生；槭樹（真正的「楓」）則是對生。"),
  "zijing": _a(u"羊蹄甲類（洋紫荊、艷紫荊、羊蹄甲）", 21, u"葉先端二裂、形似羊蹄；看花期與是否結果來分。"),
  "sa2": {"q": u"有沒有氣生根，或摘下葉子有白色乳汁？", "o": [[u"有氣生根、有乳汁", "fig"], [u"沒有", "sa3"]]},
  "fig": {"q": u"葉的特徵？", "o": [[u"葉較小、厚，倒卵形，終年常綠", "rong"], [u"葉較大、薄，一年會換好幾次葉，新芽包在紅色苞片中", "querong"]]},
  "rong": _a(u"榕樹", 7, u"台灣最常見的行道樹與老樹之一。"),
  "querong": _a(u"雀榕", 18, u"新芽像紅色的筍，換葉時常整棵光禿。"),
  "sa3": {"q": u"揉碎葉子聞聞看？", "o": [[u"有濃濃的樟腦味；葉有三條明顯的主脈", "zhang"], [u"沒有特別氣味", "sa4"]]},
  "zhang": _a(u"樟樹", 8, u"離基三出脈，脈腋常有小小的腺點。"),
  "sa4": {"q": u"葉片大小與枝條形態？", "o": [[u"大葉（可達 30 公分），枝條一層層水平展開，冬天葉轉紅", "dalan"], [u"小葉、匙形，枝條水平輪生成一層層的傘", "xiaolan"], [u"葉其實是鐮刀形的「假葉」，春天開黃色毛球花", "xiangsi"], [u"葉形多變（有的有裂），夏天結紅色毛球狀果實", "goushu"], [u"樹皮白色、一層層像海綿", "baiqian"]]},
  "dalan": _a(u"大葉欖仁", 12, u"葉大、倒卵形，冬天變紅後落葉。"),
  "xiaolan": _a(u"小葉欖仁", 12, u"枝條水平輪生，樹形像一層層的寶塔。"),
  "xiangsi": _a(u"相思樹", 34, u"「葉」其實是扁平的葉柄（假葉），真正的羽狀複葉只在幼苗時出現。"),
  "goushu": _a(u"構樹", 35, u"葉形多變，有毛；雌株夏天結紅色的聚合果。"),
  "baiqian": _a(u"白千層", 46, u"樹皮白色、多層而鬆軟，可以一片片剝下。"),
})


def make(icon, note):
    base = make_lesson(icon, note, TWLIB, "tw-w")

    def lesson(*a, **k):
        L = base(*a, **k)
        raws = [b[1] for b in L.body if isinstance(b, tuple) and b[0] == "raw"]
        if any('class="kd-w' in r for r in raws):
            L.body.insert(0, ("raw", u"<script>%s</script>" % KDLIB))
        if any('class="nv-w' in r for r in raws):
            L.body.insert(0, ("raw", u"<script>%s</script>" % NVLIB))
        return L
    return lesson
