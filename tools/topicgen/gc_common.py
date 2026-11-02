# -*- coding: utf-8 -*-
"""〈全球市值前 20 大公司〉（gc_）共用：公司資料、課程包裝與 GCLIB 互動元件（class="gc-w"）。

  race    市值排行賽跑（1989～2026 前十大）
  table   二十大比較總表（排序、篩選）
  seg     營收結構圖
  sim     成長情境模擬器（5／10／15 年）
  dcf     簡易估值計算器（含市場隱含成長率）
  moat    護城河雷達圖（兩家比較）
  day     你的一天：你碰到了哪幾家
"""
import json
from md_common import make_with
from cc_common import wdg, LS
from qt_common import BASEJS

GC_NOTE = u"市值為 2026 年 10 月底前後的約略值（每天都在變動），財務數字為各公司最近完整財年的約略值；未來展望是情境推演，不構成投資建議。"

# k, 排名, 中文名, 英文名, 國家, 產業組, 市值(兆美元), 營收(億美元), 財年, 淨利率(%), 主要營利模式, 消費者接觸點, 課
CO = [
    ["apple", 1, u"蘋果", "Apple", u"美國", u"科技平台", 5.0, 4160, u"FY2025（9 月）", 27, u"硬體銷售＋服務抽成與訂閱", u"iPhone、Mac、AirPods、App Store", 5],
    ["nvidia", 2, u"輝達", "NVIDIA", u"美國", u"AI 與半導體", 4.9, 2160, u"FY2026（2026 年 1 月）", 55, u"高毛利晶片與系統＋軟體生態", u"GeForce 顯示卡、Switch 2 晶片；AI 服務背後的算力", 10],
    ["microsoft", 3, u"微軟", "Microsoft", u"美國", u"科技平台", 3.9, 2820, u"FY2025（6 月）", 36, u"軟體訂閱＋雲端用量計費", u"Windows、Office、Teams、Xbox、Copilot", 6],
    ["alphabet", 4, u"Alphabet（Google）", "Alphabet", u"美國", u"科技平台", 3.4, 4030, u"2025", 32, u"廣告＋雲端＋訂閱", u"Google 搜尋、YouTube、Android、Gmail、地圖", 7],
    ["amazon", 5, u"亞馬遜", "Amazon", u"美國", u"科技平台", 2.6, 7170, u"2025", 11, u"零售差價＋平台抽成＋雲端＋廣告", u"Amazon 購物、Prime Video、Kindle、AWS 撐起的網站", 8],
    ["tsmc", 6, u"台積電", "TSMC", u"台灣", u"AI 與半導體", 2.0, 1220, u"2025", 45, u"晶圓代工（按片計價）", u"幾乎每支手機、電腦、AI 伺服器裡的晶片", 11],
    ["spacex", 7, u"SpaceX", "SpaceX", u"美國", u"新經濟", 1.8, 187, u"2025", -10, u"衛星網路訂閱＋發射服務＋AI", u"Starlink 衛星網路、X（推特）、Grok", 17],
    ["aramco", 8, u"沙烏地阿美", "Saudi Aramco", u"沙烏地阿拉伯", u"零售與能源", 1.7, 4100, u"2025", 23, u"開採原油與天然氣出售", u"汽油、柴油、塑膠原料背後的原油", 23],
    ["tesla", 9, u"特斯拉", "Tesla", u"美國", u"新經濟", 1.6, 950, u"2025", 4, u"賣車＋儲能＋軟體與服務", u"Model 3／Y、超級充電站、Powerwall", 16],
    ["meta", 10, u"Meta", "Meta Platforms", u"美國", u"科技平台", 1.6, 2010, u"2025", 30, u"免費服務換取注意力，賣廣告", u"Facebook、Instagram、WhatsApp、Threads、Ray-Ban Meta 眼鏡", 9],
    ["broadcom", 11, u"博通", "Broadcom", u"美國", u"AI 與半導體", 1.6, 640, u"FY2025（11 月）", 36, u"客製晶片＋網通晶片＋企業軟體授權", u"手機 Wi-Fi／藍牙晶片、Google TPU、VMware", 12],
    ["lilly", 12, u"禮來", "Eli Lilly", u"美國", u"醫療與金融", 1.3, 650, u"2025", 31, u"專利新藥銷售", u"猛健樂、Zepbound 減重與糖尿病藥、胰島素", 18],
    ["berkshire", 13, u"波克夏", "Berkshire Hathaway", u"美國", u"醫療與金融", 1.2, 3700, u"2025", 12, u"保險浮存金投資＋百家子公司獲利", u"GEICO 車險、DQ 冰淇淋、金頂電池、喜詩糖果", 19],
    ["samsung", 14, u"三星電子", "Samsung Electronics", u"韓國", u"AI 與半導體", 1.1, 2300, u"2025", 12, u"記憶體＋手機與家電＋面板", u"Galaxy 手機、電視、冰箱、洗衣機、SSD", 13],
    ["micron", 15, u"美光", "Micron", u"美國", u"AI 與半導體", 1.0, 370, u"FY2025（8 月）", 23, u"記憶體晶片（景氣循環）", u"電腦與手機裡的記憶體、AI 晶片旁的 HBM", 14],
    ["walmart", 16, u"沃爾瑪", "Walmart", u"美國", u"零售與能源", 1.0, 7050, u"FY2026（2026 年 1 月）", 3, u"薄利多銷的零售差價＋會員費＋廣告", u"沃爾瑪賣場、山姆會員店、線上購物", 22],
    ["jpmorgan", 17, u"摩根大通", "JPMorgan Chase", u"美國", u"醫療與金融", 0.9, 1820, u"2025", 31, u"存放款利差＋手續費＋投資銀行", u"Chase 信用卡與銀行帳戶、企業融資、跨國匯款", 20],
    ["amd", 18, u"超微", "AMD", u"美國", u"AI 與半導體", 0.9, 346, u"2025", 12, u"CPU、GPU 與客製晶片銷售", u"Ryzen 筆電、Radeon 顯示卡、PS5 與 Xbox 的晶片", 15],
    ["visa", 19, u"Visa", "Visa", u"美國", u"醫療與金融", 0.8, 400, u"FY2025（9 月）", 50, u"每筆刷卡收取網路服務費", u"Visa 信用卡、金融卡、手機感應支付", 21],
    ["exxon", 20, u"艾克森美孚", "ExxonMobil", u"美國", u"零售與能源", 0.8, 3300, u"2025", 9, u"油氣開採＋煉油＋化學品", u"美孚（Mobil）機油、汽油、塑膠與化學品", 24],
]
CODICT = {c[0]: c for c in CO}

# 營收結構（約略比例，%），以及計算基礎
SEG = {
    "apple": [u"依產品（FY2025）", [[u"iPhone", 50], [u"服務（App Store、iCloud、Apple Music…）", 26], [u"穿戴、居家與配件", 9], [u"Mac", 8], [u"iPad", 7]]],
    "nvidia": [u"依市場（FY2026）", [[u"資料中心（AI 加速器、網通）", 89], [u"遊戲（GeForce）", 8], [u"專業視覺化、車用與其他", 3]]],
    "microsoft": [u"依部門（FY2025）", [[u"生產力與商業流程（Office、LinkedIn、Dynamics）", 43], [u"智慧雲（Azure、伺服器軟體）", 38], [u"個人運算（Windows、Xbox、Surface、搜尋廣告）", 19]]],
    "alphabet": [u"依來源（2025）", [[u"Google 搜尋與其他廣告", 56], [u"Google Cloud", 15], [u"訂閱、平台與裝置（YouTube Premium、Play、Pixel）", 11], [u"YouTube 廣告", 10], [u"聯播網廣告", 7], [u"其他新創（Waymo 等）", 1]]],
    "amazon": [u"依類型（2025）", [[u"自營線上商店", 38], [u"第三方賣家服務", 24], [u"AWS 雲端", 18], [u"廣告", 9], [u"訂閱（Prime 等）", 7], [u"實體商店（Whole Foods 等）", 3], [u"其他", 1]]],
    "tsmc": [u"依應用平台（2025）", [[u"高效能運算（AI、伺服器、PC）", 58], [u"智慧型手機", 29], [u"物聯網", 5], [u"車用電子", 5], [u"消費性電子與其他", 3]]],
    "spacex": [u"依事業（2025，依公開資料估計）", [[u"Starlink 衛星網路", 61], [u"發射服務與其他", 22], [u"AI（xAI、X）", 17]]],
    "aramco": [u"依獲利來源（2025，約略）", [[u"上游：原油與天然氣開採", 90], [u"下游：煉油、化學品（含 SABIC）與行銷", 10]]],
    "tesla": [u"依事業（2025）", [[u"汽車（含碳權）", 73], [u"服務與其他（維修、充電、保險、二手車）", 14], [u"能源儲存與發電", 13]]],
    "meta": [u"依部門（2025）", [[u"應用程式家族（FB、IG、WhatsApp 等，幾乎全是廣告）", 99], [u"Reality Labs（Quest、智慧眼鏡）", 1]]],
    "broadcom": [u"依部門（FY2025）", [[u"半導體（客製 AI 晶片、網通、無線、寬頻）", 58], [u"基礎架構軟體（VMware 等）", 42]]],
    "lilly": [u"依產品（2025，約略）", [[u"替爾泊肽：Mounjaro 猛健樂＋Zepbound", 55], [u"Verzenio（乳癌）", 8], [u"Trulicity（糖尿病）", 5], [u"其他（Jardiance、Taltz、胰島素、Kisunla…）", 32]]],
    "berkshire": [u"依事業（約略）", [[u"製造、服務與零售（Pilot 加油站、McLane、精密零件…）", 60], [u"保險（GEICO、再保險）", 25], [u"能源公用事業", 7], [u"BNSF 鐵路", 6], [u"其他", 2]]],
    "samsung": [u"依部門（2025，約略）", [[u"裝置體驗：手機、電視、家電", 50], [u"半導體：記憶體、晶圓代工、系統晶片", 36], [u"顯示器面板", 9], [u"Harman 車用音響", 5]]],
    "micron": [u"依技術（FY2025）", [[u"DRAM（含 HBM）", 79], [u"NAND 快閃記憶體", 20], [u"其他", 1]]],
    "walmart": [u"依部門（FY2026）", [[u"沃爾瑪美國", 69], [u"國際（墨西哥、加拿大、中國、印度 Flipkart…）", 18], [u"山姆會員店（美國）", 13]]],
    "jpmorgan": [u"依部門（2025，約略）", [[u"消費者與社區銀行（Chase）", 41], [u"商業與投資銀行", 39], [u"資產與財富管理", 13], [u"公司其他", 7]]],
    "amd": [u"依部門（2025）", [[u"資料中心（EPYC、Instinct）", 48], [u"個人電腦與遊戲（Ryzen、Radeon、主機晶片）", 44], [u"嵌入式（Xilinx）", 8]]],
    "visa": [u"依收費類型（扣除客戶激勵前，約略）", [[u"資料處理費（按交易筆數）", 35], [u"服務費（按消費金額）", 32], [u"跨境交易費", 26], [u"其他加值服務", 7]]],
    "exxon": [u"依獲利來源（2025，約略）", [[u"上游：油氣探勘與生產", 70], [u"能源產品：煉油與燃料", 18], [u"特用產品：潤滑油、特用化學品", 7], [u"化學品", 5]]],
}

# 護城河評分（主觀，1～5）：網路效應、轉換成本、規模、技術、品牌、資源或法規
MOAT_AX = [u"網路效應", u"轉換成本", u"規模", u"技術", u"品牌", u"資源／法規"]
MOAT = {
    "apple": [4, 5, 5, 4, 5, 2], "nvidia": [4, 5, 4, 5, 4, 2], "microsoft": [4, 5, 5, 4, 4, 2], "alphabet": [5, 3, 5, 5, 5, 2],
    "amazon": [4, 3, 5, 4, 4, 2], "tsmc": [2, 5, 5, 5, 3, 3], "spacex": [3, 3, 4, 5, 4, 4], "aramco": [1, 1, 5, 3, 2, 5],
    "tesla": [2, 2, 3, 4, 4, 2], "meta": [5, 3, 5, 4, 3, 1], "broadcom": [2, 5, 4, 5, 2, 2], "lilly": [1, 2, 4, 5, 4, 5],
    "berkshire": [1, 2, 5, 2, 5, 3], "samsung": [2, 2, 5, 4, 4, 2], "micron": [1, 2, 4, 4, 2, 3], "walmart": [2, 2, 5, 3, 4, 1],
    "jpmorgan": [3, 4, 5, 3, 5, 4], "amd": [2, 3, 3, 4, 3, 2], "visa": [5, 4, 5, 3, 5, 4], "exxon": [1, 1, 5, 3, 3, 4],
}

# 成長情境預設（年增率 %）：悲觀、基準、樂觀
GROW = {
    "apple": [1, 5, 8], "nvidia": [0, 12, 25], "microsoft": [6, 11, 15], "alphabet": [3, 9, 14], "amazon": [5, 9, 13],
    "tsmc": [5, 13, 20], "spacex": [10, 25, 40], "aramco": [-4, 0, 3], "tesla": [-3, 10, 25], "meta": [2, 9, 15],
    "broadcom": [5, 15, 25], "lilly": [3, 12, 20], "berkshire": [2, 5, 7], "samsung": [-2, 5, 10], "micron": [-5, 8, 18],
    "walmart": [2, 4, 6], "jpmorgan": [1, 4, 7], "amd": [3, 14, 25], "visa": [5, 9, 12], "exxon": [-5, 0, 3],
}

# 「你的一天」：活動 → [直接接觸, 間接（藏在背後）]
DAY = [
    [u"早上用 iPhone 看訊息", ["apple"], ["tsmc", "broadcom", "samsung", "micron"]],
    [u"用三星或其他 Android 手機", ["samsung", "alphabet"], ["tsmc", "micron"]],
    [u"Google 搜尋、看地圖", ["alphabet"], ["broadcom", "tsmc"]],
    [u"看 YouTube", ["alphabet"], ["broadcom", "tsmc"]],
    [u"滑 Instagram、Facebook、Threads，用 WhatsApp", ["meta"], ["nvidia", "amd", "micron", "tsmc"]],
    [u"問 ChatGPT 或 Copilot 問題", ["microsoft"], ["nvidia", "tsmc", "micron", "samsung"]],
    [u"刷 X（推特）、問 Grok", ["spacex"], ["nvidia", "tsmc", "micron"]],
    [u"用 Word、Excel、Teams、Outlook 工作", ["microsoft"], ["amd", "tsmc"]],
    [u"在網路上購物、看 Netflix（網站架在 AWS）", ["amazon"], ["tsmc", "micron"]],
    [u"玩 PS5、Xbox 或 Switch 2", ["amd", "microsoft", "nvidia"], ["tsmc", "samsung", "micron"]],
    [u"刷 Visa 卡或用手機感應付款", ["visa"], ["jpmorgan"]],
    [u"騎機車或開車去加油", [], ["aramco", "exxon"]],
    [u"開或搭特斯拉電動車", ["tesla"], ["nvidia", "samsung", "tsmc"]],
    [u"用寶特瓶喝飲料、用塑膠袋", [], ["exxon", "aramco"]],
    [u"打糖尿病或減重針劑", ["lilly"], []],
    [u"吃 DQ 冰淇淋、換金頂電池", ["berkshire"], []],
    [u"在家看三星電視、用三星冰箱", ["samsung"], []],
    [u"換新筆電（Windows 或 Mac）", ["microsoft", "apple"], ["amd", "nvidia", "micron", "samsung", "tsmc"]],
    [u"出國到美國逛沃爾瑪或用美國銀行帳戶", ["walmart", "jpmorgan"], ["visa"]],
    [u"在山上、海上或飛機上用 Starlink 上網", ["spacex"], []],
]

# 歷年前十大（約略，十億美元）
RACE = {
    "1989": [[u"NTT", u"日本", 164], [u"日本興業銀行", u"日本", 72], [u"住友銀行", u"日本", 70], [u"富士銀行", u"日本", 67], [u"第一勸業銀行", u"日本", 66],
             [u"IBM", u"美國", 65], [u"三菱銀行", u"日本", 59], [u"艾克森", u"美國", 55], [u"東京電力", u"日本", 55], [u"荷蘭皇家殼牌", u"英荷", 54]],
    "1999": [[u"微軟", u"美國", 604], [u"奇異 GE", u"美國", 508], [u"思科", u"美國", 355], [u"沃爾瑪", u"美國", 308], [u"艾克森美孚", u"美國", 286],
             [u"英特爾", u"美國", 275], [u"朗訊", u"美國", 233], [u"NTT DoCoMo", u"日本", 230], [u"諾基亞", u"芬蘭", 210], [u"IBM", u"美國", 197]],
    "2010": [[u"艾克森美孚", u"美國", 369], [u"中國石油", u"中國", 303], [u"蘋果", u"美國", 296], [u"必和必拓", u"英澳", 247], [u"微軟", u"美國", 239],
             [u"中國工商銀行", u"中國", 233], [u"巴西石油", u"巴西", 229], [u"中國建設銀行", u"中國", 222], [u"荷蘭皇家殼牌", u"英荷", 208], [u"雀巢", u"瑞士", 203]],
    "2020": [[u"蘋果", u"美國", 2256], [u"沙烏地阿美", u"沙烏地", 1880], [u"微軟", u"美國", 1682], [u"亞馬遜", u"美國", 1634], [u"Alphabet", u"美國", 1185],
             [u"Facebook", u"美國", 778], [u"騰訊", u"中國", 690], [u"特斯拉", u"美國", 669], [u"阿里巴巴", u"中國", 630], [u"波克夏", u"美國", 543]],
    "2026": [[c[2] if len(c[2]) < 8 else c[3], c[4] if c[4] != u"沙烏地阿拉伯" else u"沙烏地", int(c[6] * 1000)] for c in CO[:10]],
}


def gw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("gc-w", cfg)


_DATA = json.dumps({"co": CO, "seg": SEG, "moat": MOAT, "ax": MOAT_AX, "grow": GROW, "day": DAY, "race": RACE}, ensure_ascii=False)

GCLIB = r"""
(function () {
  if (window.__gcLib) return; window.__gcLib = 1;
""" + BASEJS + r"""
  var DATA = """ + _DATA + r""";
  var CO = DATA.co, BY = {}; CO.forEach(function (c) { BY[c[0]] = c; });
  var PAL = ['#3a6ea5', '#e07a2f', '#2e9e5b', '#8e5bd1', '#e0505a', '#2a9d8f', '#d4a017', '#9aa3ad'];
  var CC = { '美國': '#3a6ea5', '日本': '#e0505a', '中國': '#d4a017', '台灣': '#2e9e5b', '韓國': '#8e5bd1', '沙烏地': '#2a9d8f', '沙烏地阿拉伯': '#2a9d8f', '英荷': '#e07a2f', '英澳': '#e07a2f', '巴西': '#7a9e2e', '瑞士': '#b0607a', '芬蘭': '#5a8fd1' };
  var SC = { '科技平台': '#3a6ea5', 'AI 與半導體': '#2e9e5b', '新經濟': '#8e5bd1', '醫療與金融': '#e07a2f', '零售與能源': '#9a7b4f' };
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function row(root) { var d = el('div'); root.appendChild(d); return d; }
  function cell(s, css) { return '<td style="padding:4px 8px;border-bottom:1px solid var(--border);' + (css || '') + '">' + s + '</td>'; }
  function tbl(head, rows, sortable) { return '<div style="overflow-x:auto"><table style="border-collapse:collapse;margin:6px 0;width:100%;font-size:0.85em"><tr>' + head.map(function (h, i) { return '<th data-i="' + i + '" style="padding:4px 8px;text-align:left;font-weight:normal;white-space:nowrap;color:var(--text-muted);border-bottom:2px solid var(--border);' + (sortable ? 'cursor:pointer' : '') + '">' + h + '</th>'; }).join('') + '</tr>' + rows.join('') + '</table></div>'; }
  function sel(root, cur, cb, lab) { var d = el('label', 'display:block;font-size:0.9em;margin:2px 0 6px', (lab || '選擇公司') + '：'); var s = el('select', 'padding:4px 6px;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text);font:inherit;font-size:0.95em');
    CO.forEach(function (c) { var o = document.createElement('option'); o.value = c[0]; o.textContent = c[1] + '. ' + c[2]; if (c[0] === cur) o.selected = true; s.appendChild(o); }); s.onchange = function () { cb(s.value); }; d.appendChild(s); root.appendChild(d); return s; }
  function money(v) { var a = Math.abs(v); return a >= 10000 ? f1(v / 10000) + ' 兆' : Math.round(v) + ' 億'; }

  /* ---------- 市值排行賽跑 ---------- */
  function initRace(root, cfg) { head(root, cfg.q); var yrs = ['1989', '1999', '2010', '2020', '2026'], cur = cfg.y || '2026', v = el('div'), inf;
    var b = row(root); yrs.forEach(function (y) { var x = btn(y === '1999' ? '2000 前後' : y === '1989' ? '1989' : y, y); x.onclick = function () { cur = y; mark(b, y); draw(); }; b.appendChild(x); }); mark(b, cur);
    root.appendChild(v); inf = info(root);
    var NOTE = { '1989': '日本泡沫經濟高峰：前十大有 7 家日本公司，其中 5 家是銀行。', '1999': '網路泡沫高峰：微軟、思科、英特爾、朗訊等科技與電信股主導。', '2010': '原物料與中國崛起：石油、礦業與中國的國營銀行、石油公司進入前十。', '2020': '平台時代：美國科技巨頭全面領先，騰訊、阿里巴巴代表中國網路業。', '2026': 'AI 時代：晶片（輝達、台積電、博通）與雲端平台主導，SpaceX 上市後直接進入前十。' };
    function draw() { var L = DATA.race[cur], mx = L[0][2], g = '', H = L.length * 30 + 20; L.forEach(function (r, i) { var y = 10 + i * 30, w = r[2] / mx * 420, c = CC[r[1]] || '#999';
        g += tx(150, y + 15, (i + 1) + '. ' + r[0], 12, 'currentColor', 'end') + '<rect x="160" y="' + y + '" width="' + n1(Math.max(w, 2)) + '" height="20" rx="3" fill="' + c + '"/>' + tx(166 + w, y + 15, (r[2] >= 1000 ? (r[2] / 1000).toFixed(1) + ' 兆' : (r[2] * 10).toLocaleString() + ' 億'), 11, 'var(--text-muted)', 'start') + tx(166 + w + 62, y + 15, r[1], 10, c, 'start'); });
      v.innerHTML = svgw('0 0 680 ' + H, g); var cnt = {}; L.forEach(function (r) { cnt[r[1]] = (cnt[r[1]] || 0) + 1; });
      inf.innerHTML = '<b>' + (cur === '1999' ? '2000 前後' : cur) + '</b>：' + NOTE[cur] + '<br>國家分布：' + Object.keys(cnt).map(function (k) { return '<span style="color:' + (CC[k] || '#999') + '">●</span> ' + k + ' ' + cnt[k]; }).join('　') + '<br><span style="color:var(--text-muted);font-size:0.9em">單位：美元，約略值。第一名的規模從約 1,640 億成長到約 5 兆，約 30 倍。</span>'; }
    draw(); }

  /* ---------- 二十大比較總表 ---------- */
  function initTable(root, cfg) { head(root, cfg.q); var f = '全部', key = 0, asc = true, v = el('div'), inf;
    var secs = ['全部', '科技平台', 'AI 與半導體', '新經濟', '醫療與金融', '零售與能源'], b = row(root);
    secs.forEach(function (s) { var x = btn(s, s); x.onclick = function () { f = s; mark(b, s); draw(); }; b.appendChild(x); }); mark(b, f);
    root.appendChild(v); inf = info(root);
    var H = ['#', '公司', '國家', '產業', '市值（兆美元）', '營收（億美元）', '淨利率', '主要營利模式', '你在哪裡碰到它'], IDX = [1, 2, 4, 5, 6, 7, 9, 10, 11];
    function draw() { var L = CO.filter(function (c) { return f === '全部' || c[5] === f; }).slice(); var j = IDX[key];
      L.sort(function (a, b) { var x = a[j], y = b[j]; var r = typeof x === 'number' ? x - y : String(x).localeCompare(String(y), 'zh-Hant'); return asc ? r : -r; });
      v.innerHTML = tbl(H.map(function (h, i) { return h + (i === key ? (asc ? ' ▲' : ' ▼') : ''); }), L.map(function (c) { return '<tr>' + cell(c[1]) + cell('<a href=\'lesson-' + (c[12] < 10 ? '0' : '') + c[12] + '.html\'><b>' + c[2] + '</b></a><br><span style="color:var(--text-muted);font-size:0.9em">' + c[3] + '</span>') + cell(c[4]) + cell('<span style="color:' + SC[c[5]] + '">●</span> ' + c[5], 'white-space:nowrap') + cell(c[6].toFixed(1), 'text-align:right') + cell(c[7].toLocaleString(), 'text-align:right') + cell(c[9] < 0 ? '虧損' : '約 ' + c[9] + '%', 'text-align:right;white-space:nowrap') + cell(c[10]) + cell(c[11]) + '</tr>'; }), true);
      v.querySelectorAll('th').forEach(function (th) { th.onclick = function () { var i = +th.getAttribute('data-i'); if (i === key) asc = !asc; else { key = i; asc = i < 4 || i === 7 || i === 8; } draw(); }; });
      var cap = L.reduce(function (s, c) { return s + c[6]; }, 0), rev = L.reduce(function (s, c) { return s + c[7]; }, 0);
      inf.innerHTML = '顯示 <b>' + L.length + '</b> 家，合計市值約 <b>' + f1(cap) + ' 兆美元</b>、合計年營收約 <b>' + money(rev) + '美元</b>。點欄位標題可以排序，點公司名稱可以到該公司的課。<br><span style="color:var(--text-muted);font-size:0.9em">營收為最近完整財年（各公司財年結束月份不同）；SpaceX 因 AI 部門投資而虧損；波克夏淨利以營業利益估計（投資損益波動很大）。</span>'; }
    draw(); }

  /* ---------- 營收結構 ---------- */
  function initSeg(root, cfg) { head(root, cfg.q); var cur = cfg.c || 'apple', v = el('div'), inf; if (!cfg.c) sel(root, cur, function (k) { cur = k; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var S = DATA.seg[cur], c = BY[cur], x = 10, g = '', L = S[1];
      L.forEach(function (s, i) { var w = s[1] / 100 * 660; g += '<rect x="' + n1(x) + '" y="10" width="' + n1(Math.max(w - 1, 1)) + '" height="34" fill="' + PAL[i % PAL.length] + '"/>' + (w > 34 ? tx(x + w / 2, 32, s[1] + '%', 11, '#fff') : ''); x += w; });
      L.forEach(function (s, i) { var y = 64 + i * 22; g += '<rect x="10" y="' + (y - 11) + '" width="14" height="14" rx="3" fill="' + PAL[i % PAL.length] + '"/>' + tx(30, y, s[0], 12, 'currentColor', 'start') + tx(670, y, '約 ' + s[1] + '%', 12, 'var(--text-muted)', 'end'); });
      v.innerHTML = svgw('0 0 680 ' + (64 + L.length * 22), g);
      inf.innerHTML = '<b>' + c[2] + '</b>：' + S[0] + '，最近財年營收約 <b>' + money(c[7]) + '美元</b>。最大的一塊占約 <b>' + L[0][1] + '%</b>' + (L[0][1] >= 60 ? '——收入高度集中，這是它最大的優勢，也是最大的風險。' : L[0][1] >= 40 ? '——有一個核心事業撐起大半。' : '——收入來源相對分散。'); }
    draw(); }

  /* ---------- 成長情境模擬器 ---------- */
  function initSim(root, cfg) { head(root, cfg.q); var cur = cfg.c || 'nvidia', v = el('div'), inf, g3, ups = [];
    sel(root, cur, function (k) { cur = k; g3 = DATA.grow[k].slice(); ups.forEach(function (u, i) { var s = root.querySelectorAll('input[type=range]')[i]; s.value = g3[i]; u(); }); }); g3 = DATA.grow[cur].slice();
    var lab = ['悲觀情境年增率（%）', '基準情境年增率（%）', '樂觀情境年增率（%）'];
    lab.forEach(function (l, i) { ups.push(slider(root, l, -10, 40, 1, g3[i], function (x) { return x + '%'; }, 'g' + i, function (x) { g3[i] = x; draw(); })); });
    root.appendChild(v); inf = info(root);
    function draw() { var c = BY[cur], b = c[7], S = [], col = ['#e0505a', '#3a6ea5', '#2e9e5b'], nm = ['悲觀', '基準', '樂觀'];
      for (var i = 0; i < 3; i++) { var d = []; for (var t = 0; t <= 15; t++) d.push([2026 + t, b * Math.pow(1 + g3[i] / 100, t)]); S.push({ d: d, c: col[i], n: nm[i] }); }
      v.innerHTML = chart(680, 300, S, { x0: 2026, x1: 2041, y0: 0, xl: '年份', yl: '營收（億美元）', vl: [{ x: 2031, n: '5 年', c: '#999' }, { x: 2036, n: '10 年', c: '#999' }] });
      var rows = [5, 10, 15].map(function (t) { return '<tr>' + cell((2026 + t) + '（' + t + ' 年）') + [0, 1, 2].map(function (i) { var x = b * Math.pow(1 + g3[i] / 100, t); return cell(money(x) + '<br><span style="color:var(--text-muted)">' + f1(x / b) + ' 倍</span>', 'text-align:right;color:' + col[i]); }).join('') + '</tr>'; });
      inf.innerHTML = '<b>' + c[2] + '</b>：以最近財年營收約 ' + money(b) + '美元為起點。' + tbl(['時間', '悲觀', '基準', '樂觀'], rows) + '<span style="color:var(--text-muted);font-size:0.9em">預設的成長率是本課程的情境假設，可以自己調整。注意：每年 15% 的成長，15 年後約是 8 倍；每年 25%，15 年後約是 28 倍——很少有大公司能長期維持這種速度。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 簡易估值 ---------- */
  function initDcf(root, cfg) { head(root, cfg.q); var cur = cfg.c || 'apple', P = {}, v = el('div'), ups = [];
    function dflt(k) { var c = BY[k]; P = { cf: Math.max(Math.round(c[7] * Math.max(c[9], 0) / 100), 0), g: DATA.grow[k][1], tg: 3, r: 9 }; }
    dflt(cur); sel(root, cur, function (k) { cur = k; dflt(k); var s = root.querySelectorAll('input[type=range]'); s[0].value = P.cf; s[1].value = P.g; s[2].value = P.tg; s[3].value = P.r; ups.forEach(function (u) { u(); }); });
    ups.push(slider(root, '今年可分給股東的現金（億美元，預設以淨利粗估）', 0, 3000, 10, P.cf, function (x) { return x + ' 億'; }, 'cf', function (x) { P.cf = x; draw(); }));
    ups.push(slider(root, '未來 10 年的年成長率', -10, 40, 1, P.g, function (x) { return x + '%'; }, 'g', function (x) { P.g = x; draw(); }));
    ups.push(slider(root, '10 年後的永續成長率', 0, 5, 0.5, P.tg, function (x) { return x + '%'; }, 'tg', function (x) { P.tg = x; draw(); }));
    ups.push(slider(root, '要求報酬率（折現率）', 6, 15, 0.5, P.r, function (x) { return x + '%'; }, 'r', function (x) { P.r = x; draw(); }));
    root.appendChild(v);
    function val(cf, g, tg, r) { var s = 0, c = cf; for (var t = 1; t <= 10; t++) { c *= 1 + g / 100; s += c / Math.pow(1 + r / 100, t); } var tv = c * (1 + tg / 100) / ((r - tg) / 100); return s + tv / Math.pow(1 + r / 100, 10); }
    function draw() { var c = BY[cur], cap = c[6] * 10000;
      if (P.cf <= 0) { v.innerHTML = '<div style="margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft)"><b>' + c[2] + '</b> 目前還在大量投資、沒有穩定可分配的現金，這種「把未來現金流折回今天」的估值方法不太適用。市場是用「未來可能變成什麼」來定價的——把現金調高看看需要多少才撐得起市值。</div>'; return; }
      if (P.r <= P.tg) { v.innerHTML = '<div style="margin-top:8px">要求報酬率必須高於永續成長率。</div>'; return; }
      var V = val(P.cf, P.g, P.tg, P.r), lo = -20, hi = 80; for (var k = 0; k < 60; k++) { var m = (lo + hi) / 2; if (val(P.cf, m, P.tg, P.r) < cap) lo = m; else hi = m; } var ig = (lo + hi) / 2;
      v.innerHTML = '<div style="margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.8"><b>' + c[2] + '</b>　估計價值約 <b>' + money(V) + '美元</b>，目前市值約 <b>' + c[6].toFixed(1) + ' 兆美元</b>（' + (V >= cap ? '估計值較高' : '市值較高') + '，相差 ' + f1(Math.abs(V / cap - 1) * 100) + '%）。<br>' +
        (ig >= 79 ? '在這組假設下，要撐起目前市值，未來 10 年每年需要超過 80% 的成長——市場顯然在用別的東西定價。' : '<b>市場隱含的成長率</b>：在其他假設不變下，目前市值相當於預期未來 10 年每年成長約 <b>' + f1(ig) + '%</b>。') +
        '<br><span style="color:var(--text-muted);font-size:0.9em">這是極度簡化的教學工具：真正的估值要看自由現金流、資本支出、負債、股票稀釋等。重點是體會「市值其實是對未來的押注」。</span></div>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 護城河雷達 ---------- */
  function initMoat(root, cfg) { head(root, cfg.q); var a = cfg.a || 'apple', b = cfg.b || 'nvidia', v = el('div'), inf;
    sel(root, a, function (k) { a = k; draw(); }, '公司 A（藍）'); sel(root, b, function (k) { b = k; draw(); }, '公司 B（橘）'); root.appendChild(v); inf = info(root);
    function draw() { var ax = DATA.ax, n = ax.length, cx = 340, cy = 160, R = 120, g = '';
      for (var lv = 1; lv <= 5; lv++) { var p = []; for (var i = 0; i < n; i++) { var t = -Math.PI / 2 + i * 2 * Math.PI / n; p.push(n1(cx + R * lv / 5 * Math.cos(t)) + ',' + n1(cy + R * lv / 5 * Math.sin(t))); } g += '<polygon points="' + p.join(' ') + '" fill="none" stroke="var(--border)"/>'; }
      for (var i = 0; i < n; i++) { var t = -Math.PI / 2 + i * 2 * Math.PI / n; g += ln(cx, cy, cx + R * Math.cos(t), cy + R * Math.sin(t), 'var(--border)') + tx(cx + (R + 26) * Math.cos(t), cy + (R + 22) * Math.sin(t) + 4, ax[i], 12, 'currentColor'); }
      [[a, '#3a6ea5'], [b, '#e07a2f']].forEach(function (z) { var s = DATA.moat[z[0]], p = []; for (var i = 0; i < n; i++) { var t = -Math.PI / 2 + i * 2 * Math.PI / n; p.push(n1(cx + R * s[i] / 5 * Math.cos(t)) + ',' + n1(cy + R * s[i] / 5 * Math.sin(t))); } g += '<polygon points="' + p.join(' ') + '" fill="' + z[1] + '" fill-opacity="0.18" stroke="' + z[1] + '" stroke-width="2"/>'; });
      v.innerHTML = svgw('0 0 680 320', g); var sa = DATA.moat[a], sb = DATA.moat[b], best = function (s) { var m = Math.max.apply(null, s); return ax.filter(function (_, i) { return s[i] === m; }).join('、'); };
      inf.innerHTML = '<span style="color:#3a6ea5">■</span> <b>' + BY[a][2] + '</b>：總分 ' + sa.reduce(function (x, y) { return x + y; }) + '／30，最強在 ' + best(sa) + '<br><span style="color:#e07a2f">■</span> <b>' + BY[b][2] + '</b>：總分 ' + sb.reduce(function (x, y) { return x + y; }) + '／30，最強在 ' + best(sb) + '<br><span style="color:var(--text-muted);font-size:0.9em">評分為本課程的主觀判斷（1～5），用來比較護城河的「形狀」，不是精確的量化指標。</span>'; }
    draw(); }

  /* ---------- 你的一天 ---------- */
  function initDay(root, cfg) { head(root, cfg.q); var on = {}, box = el('div', 'display:flex;flex-wrap:wrap;gap:4px 14px;font-size:0.9em'), v = el('div'), inf;
    DATA.day.forEach(function (d, i) { var l = el('label', 'display:flex;align-items:center;gap:4px;cursor:pointer;min-width:260px'); var c = document.createElement('input'); c.type = 'checkbox'; c.onchange = function () { on[i] = c.checked; draw(); }; l.appendChild(c); l.appendChild(document.createTextNode(d[0])); box.appendChild(l); });
    root.appendChild(box); var b = row(root); var all = btn('全選'); all.onclick = function () { box.querySelectorAll('input').forEach(function (c, i) { c.checked = true; on[i] = true; }); draw(); }; var no = btn('清除'); no.onclick = function () { box.querySelectorAll('input').forEach(function (c, i) { c.checked = false; on[i] = false; }); draw(); }; b.appendChild(all); b.appendChild(no);
    root.appendChild(v); inf = info(root);
    function draw() { var D = {}, I = {}; DATA.day.forEach(function (d, i) { if (!on[i]) return; d[1].forEach(function (k) { D[k] = 1; }); d[2].forEach(function (k) { I[k] = 1; }); });
      var g = '', W = 680; CO.forEach(function (c, i) { var x = 10 + (i % 5) * 134, y = 10 + Math.floor(i / 5) * 46, st = D[c[0]] ? 'd' : I[c[0]] ? 'i' : '';
        g += '<rect x="' + x + '" y="' + y + '" width="126" height="38" rx="8" fill="' + (st === 'd' ? '#3a6ea5' : st === 'i' ? 'var(--accent-soft)' : 'var(--surface)') + '" stroke="' + (st ? '#3a6ea5' : 'var(--border)') + '"' + (st === 'i' ? ' stroke-dasharray="4 3"' : '') + '/>' + tx(x + 63, y + 17, c[1] + '. ' + c[2].replace('（Google）', ''), 11.5, st === 'd' ? '#fff' : 'currentColor') + tx(x + 63, y + 31, st === 'd' ? '直接使用' : st === 'i' ? '藏在背後' : '', 9.5, st === 'd' ? '#fff' : 'var(--text-muted)'); });
      v.innerHTML = svgw('0 0 ' + W + ' 194', g); var nd = Object.keys(D).length, ni = Object.keys(I).filter(function (k) { return !D[k]; }).length;
      inf.innerHTML = '勾選你今天做過的事。直接使用了 <b>' + nd + '</b> 家，另外 <b>' + ni + '</b> 家藏在你用的產品背後（晶片、記憶體、雲端、原油……），合計 <b>' + (nd + ni) + '</b>／20 家。<br><span style="color:var(--text-muted);font-size:0.9em">實心＝你直接買或用它的產品；虛線＝它的產品藏在你用的東西裡面。</span>'; }
    draw(); }

  var INIT = { race: initRace, table: initTable, seg: initSeg, sim: initSim, dcf: initDcf, moat: initMoat, day: initDay };
  function boot() { document.querySelectorAll('.gc-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🏢", note=GC_NOTE):
    return make_with(icon, note, [("gc-w", GCLIB)])


lesson = make()


def company(k, title, desc, intro, quick, chain, products, money, moat, rivals, risks, taiwan, outlook, watch, point, questions, extra=None):
    """一家公司一課。products: [類別, 產品, 你在哪裡碰到]；outlook: [[時間, 基準, 樂觀, 悲觀], ...]"""
    c = CODICT[k]
    seg = SEG[k]
    body = [("p", intro),
            ("t", [u"項目", u"內容"], [[u"市值排名", u"第 %d 名，約 %.1f 兆美元（2026 年 10 月底）" % (c[1], c[6])],
                                      [u"最近財年營收", u"約 %s 美元（%s）" % (u"%.2f 兆" % (c[7] / 10000.0) if c[7] >= 10000 else u"{:,} 億".format(c[7]), c[8])]] + quick),
            ("h", u"它在產業裡站在哪裡"), ("p", chain),
            ("h", u"你買得到、用得到的產品"),
            ("t", [u"類別", u"產品", u"你在哪裡會碰到它"], products),
            ("h", u"錢從哪裡來"), gw("seg", c=k), ("ul", money),
            ("h", u"護城河：為什麼別人很難搶走"), ("ul", moat),
            ("h", u"競爭者與風險"), ("t", [u"主要競爭者", u"主要風險"], [[u"<br>".join(rivals), u"<br>".join(risks)]]),
            ("h", u"和台灣的關係"), ("p", taiwan)]
    if extra:
        body += extra
    body += [("h", u"未來展望：5 年、10 年、15 年"),
             ("t", [u"時間", u"基準情境", u"樂觀情境", u"悲觀情境"], outlook),
             ("note", u"要觀察的指標", [("ul", watch)])]
    goals = [u"認識%s的產業位置與你接觸得到的產品" % c[2], u"理解它怎麼賺錢、護城河在哪裡", u"評估它未來 5、10、15 年的可能發展"]
    return lesson(title, desc, goals, body, point, questions)
