# -*- coding: utf-8 -*-
"""〈空難全紀錄〉（acr_）共用：案例課的版型、年表、圖鑑、改進關係圖與瑞士乳酪模型（acr-w）。"""
import re
from nv_common import *
from cc_common import wdg
from qt_common import BASEJS

lesson = nv_lesson(u"🛩️")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def F(date, flight, ac, place, toll):
    return [[u"日期", date], [u"班次", flight], [u"機型", ac], [u"地點", place], [u"死傷", toll]]


def _plain(s):
    return re.sub(u"<[^>]+>", u"", s).replace(u"<", u"&lt;")


DEFAULT_Q = [u"這起事故的直接原因是什麼？", u"有哪些因素讓情況惡化，或讓人得以生還？", u"事故之後，航空界做了哪些改進？"]


def case(title, sub, facts, bg, steps, causes, fixes, moral, q=None, extra=None, status=None):
    """一起事故＝一課：基本資料、背景、經過、原因、後續改進、一句話教訓。"""
    body = [("t", [u"項目", u"內容"], facts)]
    if status:
        body.append(("note", u"調查進度", [("p", status)]))
    body += [("h", u"背景"), ("p", bg), ("h", u"經過"), ("ol", steps), ("h", u"原因"), ("ul", causes)]
    if extra:
        body += extra
    body += [("h", u"後續改進"), ("ul", fixes), ("note", u"一句話教訓", [("p", moral)])]
    point = _plain(u"%s（%s）。背景：%s 原因：%s。改進：%s。教訓：%s" % (title, sub, bg, u"；".join(causes), u"；".join(fixes), moral))
    goals = [u"了解%s的背景與經過" % title, u"理解調查認定的原因", u"認識事故之後的改進"]
    return lesson(title, sub, goals, body, point, q or DEFAULT_Q)


# 70 起事故：(年份, 名稱, 類別, 一句話, 課)
CASES = [
    (u"1954", u"彗星客機", "s", u"金屬疲勞從窗角裂開，世界第一款噴射客機接連解體", 3),
    (u"1981", u"遠東航空 103（三義）", "s", u"機腹嚴重腐蝕，在空中解體", 4),
    (u"1985", u"日航 123", "s", u"壓力隔板修理不當，四套液壓全失，520 人罹難", 5),
    (u"1988", u"阿囉哈 243", "s", u"老舊機身的屋頂在飛行中被掀開", 6),
    (u"1989", u"聯合航空 811", "s", u"貨艙門在飛行中打開", 7),
    (u"1989", u"聯合航空 232（蘇城）", "s", u"引擎碟片碎裂，液壓全失，靠油門操控迫降", 8),
    (u"2000", u"協和號 4590", "s", u"跑道上的金屬條割破輪胎，油箱破裂起火", 9),
    (u"2002", u"華航 611（澎湖）", "s", u"二十二年前的修理留下裂紋，空中解體", 10),
    (u"1974", u"土耳其航空 981", "d", u"DC-10 貨艙門設計缺陷，地板塌陷切斷操縱線", 11),
    (u"1979", u"美國航空 191", "d", u"維修捷徑弄裂吊架，引擎在起飛時脫落", 12),
    (u"1991／1994", u"聯合 585、全美 427", "d", u"737 方向舵反向的謎團", 13),
    (u"1996", u"伯根航空 301", "d", u"空速管被堵，儀表互相矛盾", 14),
    (u"1996", u"秘魯航空 603", "d", u"靜壓孔上的膠帶忘了撕", 15),
    (u"2000", u"阿拉斯加航空 261", "d", u"水平安定面螺桿缺乏潤滑而磨損", 16),
    (u"2001", u"美國航空 587", "d", u"過度使用方向舵，垂直尾翼斷裂", 17),
    (u"1972", u"東方航空 401", "h", u"整組人員盯著一顆燈泡，沒人在飛飛機", 18),
    (u"1978", u"聯合航空 173", "h", u"機長專注於起落架，燃油耗盡——CRM 的起點", 19),
    (u"1990", u"亞維安卡 52", "h", u"沒有說出「緊急」兩個字", 20),
    (u"1994", u"華航 140（名古屋）", "h", u"與自動駕駛搏鬥", 21),
    (u"1995", u"美國航空 965（卡利）", "h", u"飛航管理電腦中選錯了一個字母", 22),
    (u"1997", u"大韓航空 801（關島）", "h", u"疲勞、文化與被關掉的警告", 23),
    (u"1998", u"華航 676（大園）", "h", u"重飛失敗，墜入民宅", 24),
    (u"2000", u"新航 006（桃園）", "h", u"颱風夜從關閉的跑道起飛", 25),
    (u"2009", u"科爾根航空 3407", "h", u"疲勞與錯誤的失速改正", 26),
    (u"2013", u"韓亞航空 214", "h", u"以為自動油門會管速度", 27),
    (u"1983", u"加航 143（吉姆利滑翔機）", "a", u"公斤與磅的換算錯誤，燃油耗盡後滑翔落地", 28),
    (u"2005", u"太陽神航空 522", "a", u"增壓開關沒歸位，全機缺氧", 29),
    (u"2009", u"法航 447", "a", u"空速管結冰後的高空失速", 30),
    (u"2009", u"土耳其航空 1951", "a", u"故障的無線電高度表讓油門收到慢車", 31),
    (u"1982", u"英航 9（火山灰）", "w", u"四具引擎全部熄火後重新啟動", 32),
    (u"1982", u"佛羅里達航空 90", "w", u"結冰的飛機撞上波多馬克河的橋", 33),
    (u"1985", u"達美航空 191", "w", u"微爆氣流", 34),
    (u"1994", u"美鷹航空 4184", "w", u"過冷大水滴的結冰", 35),
    (u"2009", u"全美航空 1549（哈德遜河）", "w", u"雙發鳥擊後河面迫降，全員生還", 36),
    (u"1980", u"沙烏地航空 163", "f", u"成功落地，卻沒有人逃出", 37),
    (u"1983", u"加航 797", "f", u"廁所起火與閃燃", 38),
    (u"1985", u"英國空中旅遊 28M（曼徹斯特）", "f", u"起飛中斷後的火災與撤離", 39),
    (u"1996", u"瓦盧傑 592", "f", u"貨艙中的過期氧氣產生器", 40),
    (u"1996", u"環球航空 800", "f", u"中央油箱爆炸", 41),
    (u"1998", u"瑞士航空 111", "f", u"娛樂系統線路與易燃隔熱毯", 42),
    (u"1956", u"大峽谷空中相撞", "c", u"催生了美國聯邦航空總署", 43),
    (u"1977", u"特內里費", "c", u"史上死亡人數最多的空難", 44),
    (u"1996", u"恰爾基達德里空中相撞", "c", u"史上死亡人數最多的空中相撞", 45),
    (u"2001", u"米蘭林納特", "c", u"濃霧中的跑道入侵", 46),
    (u"2002", u"于伯林根空中相撞", "c", u"防撞系統與管制員的指令相反", 47),
    (u"1983", u"大韓航空 007", "x", u"偏航後被蘇聯擊落；GPS 開放民用", 48),
    (u"1985", u"印度航空 182", "x", u"行李中的炸彈", 49),
    (u"1988", u"伊朗航空 655", "x", u"被美國軍艦誤認為戰機", 50),
    (u"1988", u"泛美 103（洛克比）", "x", u"收音機裡的炸彈", 51),
    (u"2001", u"九一一", "x", u"劫機成為武器", 52),
    (u"2014", u"馬航 MH370", "r", u"消失在印度洋", 53),
    (u"2014", u"馬航 MH17", "r", u"在烏克蘭東部被飛彈擊落", 54),
    (u"2014", u"復興航空 GE222（澎湖）", "r", u"低於最低高度繼續進場", 55),
    (u"2014", u"亞洲航空 QZ8501", "r", u"重設電腦後的失速", 56),
    (u"2015", u"復興航空 GE235（基隆河）", "r", u"關錯了引擎", 57),
    (u"2015", u"德國之翼 9525", "r", u"副駕駛蓄意墜機", 58),
    (u"2016", u"LaMia 2933", "r", u"為了省錢不加油", 59),
    (u"2018", u"獅子航空 610", "r", u"MCAS 第一次出事", 60),
    (u"2019", u"衣索比亞航空 302", "r", u"MCAS 再次出事，737 MAX 全球停飛", 61),
    (u"2020", u"烏克蘭國際航空 752", "r", u"被伊朗革命衛隊擊落", 62),
    (u"2020", u"印度快運 1344（卡利卡特）", "r", u"雨中的桌面跑道", 63),
    (u"2022", u"東方航空 MU5735", "r", u"近乎垂直的俯衝；最終報告未公布", 64),
    (u"2023", u"雪人航空 691（博卡拉）", "r", u"拉錯了操縱桿，螺旋槳順槳", 65),
    (u"2024", u"日航 516（羽田）", "r", u"跑道上的相撞與 18 分鐘的撤離", 66),
    (u"2024", u"Voepass 2283", "r", u"嚴重積冰後的螺旋", 67),
    (u"2024", u"亞塞拜然航空 8243", "r", u"被俄羅斯防空飛彈擊傷", 68),
    (u"2024", u"濟州航空 2216（務安）", "r", u"鳥擊、機腹著陸與跑道盡頭的土堤", 69),
    (u"2025", u"美鷹航空 5342（華盛頓）", "r", u"與軍用直升機在河面上空相撞", 70),
    (u"2025", u"印度航空 171", "r", u"起飛後兩個燃油開關被切斷", 71),
    (u"2025", u"UPS 2976", "r", u"引擎與吊架脫落，與 1979 年的悲劇相似", 72),
]

GROUPS = [["s", u"結構與材料", CR], ["d", u"設計與維修", CO], ["h", u"人為因素", CB], ["a", u"自動化與系統", CT],
          ["w", u"天氣與自然", CG], ["f", u"火災", CY], ["c", u"相撞與跑道", CP], ["x", u"擊落與恐攻", CK], ["r", u"近年", "#c0392b"]]

_sorted = sorted(CASES, key=lambda c: (int(c[0][:4]), c[4]))

TIMELINE = nvw({"t": "timeline", "q": u"本課程的 70 起事故（依年份排列；點一列看說明，可依類別篩選）：", "yw": 96, "mh": 600,
  "groups": GROUPS,
  "ev": [ev(c[0], c[1], u"%s（第 %d 課）" % (c[3], c[4]), c[2]) for c in _sorted]})

CARDS = nvw({"t": "cards", "q": u"事故圖鑑：可依類別篩選，或搜尋班次、地點、關鍵字：",
  "groups": GROUPS,
  "cards": [card(c[1], c[2], u"%s。第 %d 課。" % (c[3], c[4]), c[0]) for c in CASES]})

_L, _R = 120, 500
_acc = [("gc", u"大峽谷 1956", 43), ("comet", u"彗星客機 1954", 3), ("ten", u"特內里費 1977", 44), ("ua173", u"聯合 173 1978", 19),
        ("kal", u"大韓 007 1983", 48), ("ac797", u"加航 797 1983", 38), ("dl191", u"達美 191 1985", 34), ("aloha", u"阿囉哈 243 1988", 6),
        ("pa103", u"洛克比 1988", 51), ("twa", u"環球 800 1996", 41), ("ueb", u"于伯林根 2002", 47), ("911", u"九一一 2001", 52),
        ("colgan", u"科爾根 3407 2009", 26), ("af447", u"法航 447 2009", 30), ("mh370", u"MH370 2014", 53), ("max", u"737 MAX 2018～19", 61)]
_imp = [("faa", u"FAA 成立、雷達管制", u"1958 年《聯邦航空法》成立 FAA，把航路納入雷達管制。"),
        ("fat", u"疲勞試驗與損傷容限", u"全尺寸疲勞試驗、圓角窗戶、損傷容限設計成為標準。"),
        ("crm", u"組員資源管理（CRM）", u"打破機長的權威，鼓勵全體組員發言、交叉確認。"),
        ("gps", u"GPS 開放民用", u"美國宣布把 GPS 開放給民間使用。"),
        ("fire", u"煙霧偵測與地板照明", u"廁所煙霧偵測器、自動滅火器、地板逃生指示燈、阻燃座椅。"),
        ("ws", u"風切警告", u"都卜勒氣象雷達與機載預測式風切警告。"),
        ("age", u"老舊飛機計畫", u"高使用次數飛機的強制檢查與結構補強。"),
        ("bag", u"託運行李全面檢查", u"行李與旅客核對、全面安檢。"),
        ("inert", u"油箱惰化", u"以氮氣降低油箱內可燃蒸氣。"),
        ("tcas", u"TCAS 優先於管制指令", u"防撞系統的指示必須優先遵守。"),
        ("door", u"強化駕駛艙門", u"防彈、防闖入的駕駛艙門與安檢機構。"),
        ("1500", u"1,500 小時與疲勞規定", u"副駕駛資格門檻與新的值勤時間規定。"),
        ("stall", u"高空失速與空速不可靠訓練", u"模擬機訓練加入高空失速改正。"),
        ("track", u"全球航班追蹤", u"每 15 分鐘回報位置、自主遇險追蹤。"),
        ("cert", u"認證制度改革", u"檢討飛機製造商自我認證的制度。")]
_edges = [("gc", "faa"), ("comet", "fat"), ("ten", "crm"), ("ua173", "crm"), ("kal", "gps"), ("ac797", "fire"), ("dl191", "ws"), ("aloha", "age"),
          ("pa103", "bag"), ("twa", "inert"), ("ueb", "tcas"), ("911", "door"), ("colgan", "1500"), ("af447", "stall"), ("af447", "track"), ("mh370", "track"), ("max", "cert")]

GRAPH = nvw({"t": "graph", "h": 560, "q": u"每一條規則背後的事故——點選看說明（左：事故；右：改進）：",
  "nodes": [node(a[0], a[1], _L, 20 + i * 34, CR, u"見第 %d 課。" % a[2]) for i, a in enumerate(_acc)]
         + [node(m[0], m[1], _R, 30 + i * 36, CG, m[2]) for i, m in enumerate(_imp)],
  "edges": [[a, b, u"", CK] for a, b in _edges],
  "hint": u"點選事故或改進，查看說明。幾乎每一條飛安規則，都是用生命換來的。"})

ACRLIB = r"""
(function () {
  if (window.__acrLib) return; window.__acrLib = 1;
""" + BASEJS + r"""
  var NAMES = ['設計', '維修', '訓練', '程序', '管制', '警告系統'];
  function init(root) { var cfg = JSON.parse(root.getAttribute('data-cfg')); head(root, cfg.q); var P = { n: 4, h: 0.12 };
    var bar = el('div', 'margin:4px 0'), b1 = btn('⚡ 來一次危險'), b2 = btn('🔁 模擬 10,000 次'); bar.appendChild(b1); bar.appendChild(b2); root.appendChild(bar);
    var u1 = slider(root, '防線數量', 1, 6, 1, P.n, function (x) { return x + ' 層'; }, null, function (x) { P.n = x; trial(); });
    var u2 = slider(root, '每層漏洞的大小', 0.02, 0.3, 0.01, P.h, function (x) { return Math.round(x * 100) + '%（每層兩個洞）'; }, null, function (x) { P.h = x; trial(); });
    var view = el('div', 'margin-top:6px'), inf = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em');
    root.appendChild(view); root.appendChild(inf); var sim = '';
    function holes() { var H = [], hh = P.h * 180; for (var i = 0; i < P.n; i++) { H.push([20 + Math.random() * (180 - hh), 20 + Math.random() * (180 - hh)]); } return H; }
    function stop(H, y) { var hh = P.h * 180; for (var i = 0; i < H.length; i++) { if (!((y >= H[i][0] && y <= H[i][0] + hh) || (y >= H[i][1] && y <= H[i][1] + hh))) return i; } return -1; }
    function xs() { var a = []; for (var i = 0; i < P.n; i++) a.push(P.n === 1 ? 320 : 120 + i * 400 / (P.n - 1)); return a; }
    function trial() { var H = holes(), y = 20 + Math.random() * 180; draw(H, y, stop(H, y)); }
    function prob() { return Math.pow(Math.min(1, 2 * P.h), P.n); }
    function fp(p) { return p < 1e-4 ? p.toExponential(1) : (p * 100).toFixed(p < 0.01 ? 3 : 1) + '%'; }
    function draw(H, y, s) { var X = xs(), hh = P.h * 180, o = '';
      X.forEach(function (x, i) { o += '<rect x="' + (x - 14) + '" y="20" width="28" height="180" rx="6" fill="#f2c94c" stroke="#c9a227"/>';
        H[i].forEach(function (t) { o += '<ellipse cx="' + x + '" cy="' + n1(t + hh / 2) + '" rx="9" ry="' + n1(hh / 2) + '" fill="#fffaf0" stroke="#c9a227"/>'; });
        o += tx(x, 216, NAMES[i], 11, 'var(--text-muted)'); });
      var end = s < 0 ? 625 : X[s] - 14, c = s < 0 ? '#d0564f' : '#3a6ea5';
      o += '<line x1="10" y1="' + n1(y) + '" x2="' + n1(end) + '" y2="' + n1(y) + '" stroke="' + c + '" stroke-width="3"/><circle cx="' + n1(end) + '" cy="' + n1(y) + '" r="6" fill="' + c + '"/>';
      view.innerHTML = svgw('0 0 640 226', o);
      inf.innerHTML = (s < 0 ? '<b style="color:#d0564f">危險穿過了所有防線——事故發生了。</b>' : '危險被第 ' + (s + 1) + ' 層（' + NAMES[s] + '）擋了下來。') +
        '<br>每一層都有漏洞，但只有當所有的洞剛好連成一線時，事故才會發生。理論上，危險穿過全部 ' + P.n + ' 層的機率約為 (2×' + Math.round(P.h * 100) + '%)<sup>' + P.n + '</sup> ≈ <b>' + fp(prob()) + '</b>。' +
        (sim ? '<br>' + sim : '') + '<br><span style="font-size:0.88em;color:var(--text-muted)">簡化模型：假設各層的漏洞獨立且隨機。真實世界中，漏洞常常是相關的（例如同一家公司的文化同時削弱了訓練與維修）。</span>'; }
    b1.onclick = function () { sim = ''; trial(); };
    b2.onclick = function () { var k = 0, N = 10000; for (var i = 0; i < N; i++) { var H = holes(); if (stop(H, 20 + Math.random() * 180) < 0) k++; } sim = '模擬 10,000 次：事故 <b>' + k + '</b> 次（' + fp(k / N) + '）。'; trial(); };
    u1(); u2();
  }
  function all() { document.querySelectorAll('.acr-w').forEach(function (w) { if (w.__d) return; w.__d = 1; init(w); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', all); else all();
})();
"""

_w = wdg("acr-w", {"q": u"瑞士乳酪模型：每一層防線都有漏洞，只有漏洞連成一線時，事故才會發生："})
SWISS = ("raw", _w[1] + u"<script>%s</script>" % ACRLIB)
