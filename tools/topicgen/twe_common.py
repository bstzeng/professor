# -*- coding: utf-8 -*-
"""〈台灣電力與能源現況〉（twe_）共用：資料、課程包裝與 TELIB 互動元件。

資料以經濟部能源署（原能源局）能源統計、台電公開資料、世界銀行商品價格（Pink Sheet）為主，截至 2026 年 10 月。
互動元件（class="te-w"）：
  mix      歷年發電結構（堆疊長條）           load     一日負載曲線示意（含鴨子曲線）
  imports  LNG／煤炭／原油進口來源             prices   國際燃料價格歷年走勢
  fuelcost 燃料價格 → 每度電燃料成本         sandbox  電源配比沙盤：碳排、進口依存、成本
  cf       容量因數：同樣 1 GW 能發多少電     lng      天然氣安全存量試算
  tariff   平均電價與台電盈虧
"""
import json
from cc_common import *
from qt_common import BASEJS

TE_NOTE = (u"本課程數據以經濟部能源署（原能源局）能源統計、台電公開資料與世界銀行商品價格為主，資料截至 2026 年 10 月；"
           u"不同統計口徑（全國／台電系統、稅前／稅後）數字會略有差異。中東情勢與電價政策仍在變動，最新數字請以官方公告為準。")

# 發電結構（全國口徑，%）：燃煤、燃氣、核能、再生能源、燃油＋抽蓄等其他
MIX = [
    [2016, 45.4, 32.4, 12.0, 4.8, 5.4], [2017, 46.6, 34.6, 8.3, 4.6, 5.9], [2018, 46.3, 34.6, 10.1, 4.6, 4.4],
    [2019, 46.0, 33.2, 11.8, 5.6, 3.4], [2020, 45.0, 35.7, 11.2, 5.4, 2.7], [2021, 44.3, 37.2, 9.6, 6.0, 2.9],
    [2022, 42.1, 38.8, 8.2, 8.3, 2.6], [2023, 42.2, 39.5, 6.3, 9.5, 2.5], [2024, 39.3, 42.5, 4.2, 11.6, 2.4],
    [2025, 35.4, 47.8, 1.1, 13.1, 2.6],
]
# 世界銀行年平均：布蘭特原油（美元/桶）、澳洲紐卡索燃煤（美元/公噸）、日本 LNG 進口價（美元/百萬英熱單位）
PRICES = [
    [2014, 98.9, 70.1, 16.0], [2015, 52.4, 57.5, 10.3], [2016, 44.0, 65.9, 6.9], [2017, 54.4, 88.5, 8.6],
    [2018, 71.1, 107.0, 10.7], [2019, 64.0, 77.9, 10.6], [2020, 42.3, 60.8, 8.3], [2021, 70.4, 138.1, 10.8],
    [2022, 99.8, 344.9, 18.4], [2023, 82.6, 172.8, 14.4], [2024, 80.7, 136.1, 12.8], [2025, 69.0, 108.4, 12.0],
]
IMPORTS = {
    "lng": [u"液化天然氣（2025 年）", [[u"卡達", 33.7], [u"澳洲", 33.5], [u"美國", 9.9], [u"其他（巴布亞紐幾內亞、奈及利亞、印尼、俄羅斯等）", 22.9]],
            u"2026 年 1～7 月因卡達停產，美國占比升到 25.3%，成為第二大來源。"],
    "coal": [u"燃煤（近年）", [[u"澳洲", 50], [u"印尼", 26], [u"俄羅斯", 8], [u"南非、加拿大、哥倫比亞等", 16]],
             u"約略比例：澳洲約一半、印尼約四分之一；俄羅斯煤從 2022 年約 11% 降到 2025 年上半年約 6%（台電 2022 年 8 月起停購）。"],
    "oil": [u"原油（2025 年 12 月單月）", [[u"沙烏地阿拉伯", 40.6], [u"美國", 21.1], [u"科威特", 17.0], [u"阿聯", 12.1], [u"卡達", 8.7]],
            u"單月數字會波動；長期約七成來自中東，近年美國比重明顯上升。"],
}
TARIFF = [[u"2018～2022.6", 2.6253], [u"2022.7", 2.8458], [u"2023.4", 3.1154], [u"2024.4", 3.4518], [u"2024.10", 3.7556], [u"2025.10", 3.7823]]
PROFIT = [[2022, -2223], [2023, -1977], [2024, -411], [2025, 729]]
# 台電 2025 年每度發電成本（元）
UNITCOST = [[u"水力（自發）", 1.32], [u"核能", 1.98], [u"燃煤（自發）", 2.20], [u"燃煤（購入）", 2.76], [u"燃氣（自發）", 2.76],
            [u"燃氣（購入）", 3.37], [u"太陽光電（自發）", 4.04], [u"陸域風力（自發）", 4.89], [u"離岸風電（購入）", 6.60]]


def tw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("te-w", cfg)


def pct_rows():
    return [[str(r[0]), u"%.1f%%" % r[1], u"%.1f%%" % r[2], u"%.1f%%" % r[3], u"%.1f%%" % r[4], u"%.1f%%" % r[5]] for r in MIX]


TELIB = r"""
(function () {
  if (window.__teLib) return; window.__teLib = 1;
""" + BASEJS + r"""
  var _sl = slider; slider = function (root, lab, min, max, step, val, fmt, k, cb) { var u = _sl(root, lab, min, max, step, val, fmt, k, cb); var b = root.lastChild && root.lastChild.querySelector('b'); if (b) b.textContent = fmt(val); return u; };
  var MIX = """ + json.dumps(MIX) + r""", PRICES = """ + json.dumps(PRICES) + r""", IMP = """ + json.dumps(IMPORTS, ensure_ascii=False) + r""";
  var TARIFF = """ + json.dumps(TARIFF, ensure_ascii=False) + r""", PROFIT = """ + json.dumps(PROFIT) + r""";
  var C = { coal: '#6b5b4b', gas: '#e07a2f', nuc: '#8e5bd1', re: '#4caf50', oth: '#9aa3ad', solar: '#e8b923', wind: '#2a9d8f', hydro: '#3a6ea5' };
  var NAMES = ['燃煤', '燃氣', '核能', '再生能源', '燃油＋抽蓄等'], COLS = [C.coal, C.gas, C.nuc, C.re, C.oth];
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function legend(names, cols) { return '<div style="display:flex;flex-wrap:wrap;gap:10px;font-size:0.82em;margin:6px 0">' + names.map(function (n, i) { return '<span><span style="display:inline-block;width:11px;height:11px;border-radius:2px;background:' + cols[i] + ';vertical-align:-1px"></span> ' + n + '</span>'; }).join('') + '</div>'; }
  function rect(x, y, w, h, c, t) { return '<rect x="' + n1(x) + '" y="' + n1(y) + '" width="' + n1(Math.max(0, w)) + '" height="' + n1(Math.max(0, h)) + '" fill="' + c + '"' + (t ? '><title>' + t + '</title></rect>' : '/>'); }

  /* ---------- 歷年發電結構 ---------- */
  function initMix(root, cfg) {
    head(root, cfg.q); var v = el('div'), inf = info(root); root.insertBefore(v, inf); var sel = MIX.length - 1;
    function draw() { var W = 640, H = 260, L = 40, B = 26, bw = (W - L - 10) / MIX.length, g = '';
      [0, 25, 50, 75, 100].forEach(function (p) { var y = H - B - p / 100 * (H - B - 10); g += ln(L, y, W - 10, y, 'var(--border)', 0.6) + tx(L - 4, y + 3, p + '%', 9, 'var(--text-muted)', 'end'); });
      MIX.forEach(function (r, i) { var x = L + i * bw + 4, y = H - B; for (var k = 1; k <= 5; k++) { var h = r[k] / 100 * (H - B - 10); y -= h; g += rect(x, y, bw - 8, h, COLS[k - 1], r[0] + ' ' + NAMES[k - 1] + ' ' + r[k] + '%'); }
        g += '<g data-i="' + i + '" style="cursor:pointer">' + '<rect x="' + n1(x - 3) + '" y="7" width="' + n1(bw - 2) + '" height="' + n1(H - B - 5) + '" rx="3" fill="transparent" stroke="' + (i === sel ? '#ff3df2' : 'transparent') + '" stroke-width="2"/>' + '</g>' + tx(x + (bw - 8) / 2, H - 8, r[0], 9.5, i === sel ? 'currentColor' : 'var(--text-muted)'); });
      v.innerHTML = legend(NAMES, COLS) + svgw('0 0 ' + W + ' ' + H, g);
      v.querySelectorAll('[data-i]').forEach(function (e) { e.addEventListener('click', function () { sel = +e.getAttribute('data-i'); draw(); }); });
      var r = MIX[sel], p = MIX[0];
      inf.innerHTML = '<b>' + r[0] + ' 年</b>：燃煤 ' + r[1] + '%、燃氣 ' + r[2] + '%、核能 ' + r[3] + '%、再生能源 ' + r[4] + '%、其他 ' + r[5] + '%。' +
        (sel ? '<br>和 ' + p[0] + ' 年相比：燃煤 ' + f1(r[1] - p[1]) + '、燃氣 +' + f1(r[2] - p[2]) + '、核能 ' + f1(r[3] - p[3]) + '、再生能源 +' + f1(r[4] - p[4]) + ' 個百分點。' : '') + '（點長條切換年份）'; }
    draw(); }

  /* ---------- 一日負載曲線（示意） ---------- */
  function initLoad(root, cfg) {
    head(root, cfg.q); var season = 1, sol = 16, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    var bar = el('div'); [['春秋', 0], ['夏季', 1], ['冬季', 2]].forEach(function (s) { var b = btn(s[0], s[1]); b.onclick = function () { season = s[1]; mark(bar, season); draw(); }; bar.appendChild(b); }); root.insertBefore(bar, v); mark(bar, 1);
    slider(root, '太陽光電裝置容量（GW）', 0, 40, 1, sol, function (x) { return x + ' GW'; }, 's', function (x) { sol = x; draw(); });
    function demand(h) { var b = [25, 29, 24][season], a1 = [9, 12, 7][season], a2 = [7, 9, 7.5][season], d;
      d = b + a1 * Math.exp(-Math.pow((h - 14) / 4.5, 2)) + a2 * Math.exp(-Math.pow((h - 20) / 2.8, 2)) + a2 * Math.exp(-Math.pow((h + 4) / 2.8, 2));
      return d - 2 * Math.exp(-Math.pow((h - 4) / 2.5, 2)); }
    function solar(h) { var cf = [0.62, 0.68, 0.5][season]; return h < 6 || h > 18 ? 0 : sol * cf * Math.pow(Math.sin(Math.PI * (h - 6) / 12), 1.6); }
    function draw() { var W = 640, H = 250, L = 40, B = 28, T = 10, mx = 46, g = '', sx = function (h) { return L + h / 24 * (W - L - 10); }, sy = function (p) { return H - B - p / mx * (H - B - T); };
      for (var p = 0; p <= 45; p += 10) g += ln(L, sy(p), W - 10, sy(p), 'var(--border)', 0.6) + tx(L - 4, sy(p) + 3, p, 9, 'var(--text-muted)', 'end');
      for (var h = 0; h <= 24; h += 3) g += tx(sx(h), H - 10, h + '時', 9, 'var(--text-muted)');
      var dD = '', dN = '', aS = '', mn = 99, mxn = 0, tmn = 0, tmx = 0;
      for (var x = 0; x <= 24.001; x += 0.25) { var d = demand(x), s = solar(x), n = d - s; dD += (x ? 'L' : 'M') + n1(sx(x)) + ' ' + n1(sy(d)); dN += (x ? 'L' : 'M') + n1(sx(x)) + ' ' + n1(sy(n));
        if (n < mn) { mn = n; tmn = x; } if (x >= 15 && n > mxn) { mxn = n; tmx = x; } }
      aS = dD + ' ' + dN.replace(/M/, 'L').split('L').slice(1).reverse().map(function (p) { return 'L' + p; }).join(' ') + ' Z';
      g += '<path d="' + aS + '" fill="' + C.solar + '" fill-opacity="0.35"/>' + '<path d="' + dD + '" fill="none" stroke="' + C.gas + '" stroke-width="2"/>' + '<path d="' + dN + '" fill="none" stroke="' + C.coal + '" stroke-width="2.4"/>';
      v.innerHTML = legend(['總用電負載', '扣掉太陽光電後的淨負載（其他電源要供應的）', '太陽光電出力'], [C.gas, C.coal, C.solar]) + svgw('0 0 ' + W + ' ' + H, g + tx(L - 36, T + 2, 'GW', 9, 'var(--text-muted)', 'start'));
      inf.innerHTML = '淨負載最低在 <b>' + f1(tmn) + ' 時</b>（約 ' + f1(mn) + ' GW），傍晚 <b>' + f1(tmx) + ' 時</b>升到約 ' + f1(mxn) + ' GW：其他電源要在幾小時內爬升 <b>' + f1(mxn - mn) + ' GW</b>。' +
        '<br>這就是「鴨子曲線」：光電愈多，中午的鴨肚子愈深、傍晚的鴨脖子愈陡，需要燃氣機組、抽蓄水力與電池快速補上。（形狀為教學示意，量級參考台灣近年夏季尖峰約 41～43 GW。）'; }
    draw(); }

  /* ---------- 進口來源 ---------- */
  function initImports(root, cfg) {
    head(root, cfg.q); var k = cfg.k || 'lng', v = el('div'), inf = info(root), bar = el('div'); root.insertBefore(bar, inf); root.insertBefore(v, inf);
    [['液化天然氣', 'lng'], ['燃煤', 'coal'], ['原油', 'oil']].forEach(function (s) { var b = btn(s[0], s[1]); b.onclick = function () { k = s[1]; mark(bar, k); draw(); }; bar.appendChild(b); }); mark(bar, k);
    var cs = ['#3a6ea5', '#e07a2f', '#4caf50', '#8e5bd1', '#c9a227', '#9aa3ad'];
    function draw() { var d = IMP[k], g = '', y = 8;
      d[1].forEach(function (r, i) { var w = r[1] / 60 * 380; g += tx(170, y + 15, r[0].length > 12 ? r[0].slice(0, 11) + '…' : r[0], 11, 'currentColor', 'end') + rect(178, y + 3, w, 18, cs[i]) + tx(184 + w, y + 16, r[1] + '%', 11, 'currentColor', 'start'); y += 28; });
      v.innerHTML = '<div style="font-weight:600;margin:6px 0">' + d[0] + '</div>' + svgw('0 0 640 ' + (y + 6), g);
      inf.innerHTML = d[1].map(function (r) { return r[0] + ' ' + r[1] + '%'; }).join('、') + '。<br>' + d[2]; }
    draw(); }

  /* ---------- 國際燃料價格 ---------- */
  function initPrices(root, cfg) {
    head(root, cfg.q); var v = el('div'), inf = info(root); root.insertBefore(v, inf);
    function idx(j) { var b = PRICES.filter(function (r) { return r[0] === 2019; })[0][j]; return PRICES.map(function (r) { return [r[0], r[j] / b * 100]; }); }
    v.innerHTML = chart(640, 250, [{ d: idx(1), c: C.coal, n: '原油（布蘭特）' }, { d: idx(2), c: '#333', n: '燃煤（紐卡索）', dash: '5 3' }, { d: idx(3), c: C.gas, n: 'LNG（日本進口價）' }], { y0: 0, xl: '年（2019 年 = 100）', hl: [{ y: 100, c: 'var(--text-muted)', n: '2019' }] });
    inf.innerHTML = '三種燃料都以 2019 年為 100 換算成指數，方便比較漲跌幅。2022 年俄烏戰爭時燃煤漲到 2019 年的 <b>4.4 倍</b>、LNG <b>1.7 倍</b>；2026 年中東戰事又讓原油一度超過每桶 100 美元、亞洲現貨 LNG 在 10 月升到每百萬英熱單位約 30 美元（尚未列入年平均）。'; }

  /* ---------- 每度電燃料成本 ---------- */
  function initFuelcost(root, cfg) {
    head(root, cfg.q); var fu = 'gas', pr = 12, eff = 55, fx = 31, v = el('div'), inf = info(root), bar = el('div'); root.insertBefore(bar, inf); root.insertBefore(v, inf);
    var F = { gas: ['LNG（美元/百萬英熱單位）', 3, 40, 0.5, 12, 55, 1.055], coal: ['燃煤（美元/公噸，6000 kcal/kg）', 50, 400, 5, 108, 40, 25120], oil: ['原油或重油（美元/桶）', 30, 150, 1, 69, 38, 6119] };
    var sp, se;
    [['燃氣', 'gas'], ['燃煤', 'coal'], ['燃油', 'oil']].forEach(function (s) { var b = btn(s[0], s[1]); b.onclick = function () { fu = s[1]; mark(bar, fu); pr = F[fu][4]; eff = F[fu][5]; build(); }; bar.appendChild(b); }); mark(bar, fu);
    var box = el('div'); root.insertBefore(box, inf);
    function build() { box.innerHTML = ''; var f = F[fu];
      sp = slider(box, f[0], f[1], f[2], f[3], pr, function (x) { return '$' + x; }, 'p', function (x) { pr = x; draw(); });
      se = slider(box, '發電效率（%）', 25, 62, 1, eff, function (x) { return x + '%'; }, 'e', function (x) { eff = x; draw(); });
      slider(box, '匯率（新台幣/美元）', 27, 35, 0.5, fx, function (x) { return x; }, 'x', function (x) { fx = x; draw(); }); draw(); }
    function draw() { var f = F[fu], heatPerKWh = 3.6 / (eff / 100), usd;
      if (fu === 'gas') usd = pr * heatPerKWh / 1055.06; else if (fu === 'coal') usd = pr * heatPerKWh / 25120; else usd = pr * heatPerKWh / 6119;
      var ntd = usd * fx; v.innerHTML = '';
      inf.innerHTML = '每度電（1 kWh = 3.6 MJ）在效率 ' + eff + '% 下需要 ' + f2(heatPerKWh) + ' MJ 燃料熱量。燃料成本約 <b>' + f2(usd * 100) + ' 美分</b>，即 <b>新台幣 ' + f2(ntd) + ' 元/度</b>。' +
        '<br>換算：1 百萬英熱單位 = 1,055 MJ；6000 kcal/kg 燃煤每公噸約 25,120 MJ；1 桶原油約 6,119 MJ。這只是燃料費，還沒有加上建廠、維護、輸配電。'; }
    build(); }

  /* ---------- 電源配比沙盤 ---------- */
  function initSandbox(root, cfg) {
    head(root, cfg.q); var s = { coal: 35, gas: 48, nuc: 1, re: 13 }, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    var EF = { coal: 0.88, gas: 0.38, nuc: 0.012, re: 0.03, oth: 0.75 }, COST = { coal: 2.5, gas: 3.1, nuc: 1.98, re: 4.5, oth: 5 }, IMPF = { coal: 1, gas: 1, nuc: 1, re: 0, oth: 0.6 };
    [['燃煤 %', 'coal'], ['燃氣 %', 'gas'], ['核能 %', 'nuc'], ['再生能源 %', 're']].forEach(function (r) {
      slider(root, r[0], 0, 80, 1, s[r[1]], function (x) { return x + '%'; }, r[1], function (x) { s[r[1]] = x; draw(); }); });
    root.appendChild(inf);
    function draw() { var tot = s.coal + s.gas + s.nuc + s.re, oth = Math.max(0, 100 - tot), sc = tot > 100 ? 100 / tot : 1, m = { coal: s.coal * sc, gas: s.gas * sc, nuc: s.nuc * sc, re: s.re * sc, oth: oth };
      var ef = 0, co = 0, im = 0; for (var k in m) { ef += m[k] / 100 * EF[k]; co += m[k] / 100 * COST[k]; im += m[k] / 100 * IMPF[k]; }
      var g = '', x = 0; ['coal', 'gas', 'nuc', 're', 'oth'].forEach(function (k, i) { var w = m[k] / 100 * 620; g += rect(10 + x, 6, w, 30, COLS[i]); if (w > 30) g += tx(10 + x + w / 2, 26, Math.round(m[k]) + '%', 11, '#fff'); x += w; });
      v.innerHTML = legend(NAMES, COLS) + svgw('0 0 640 42', g);
      inf.innerHTML = (tot > 100 ? '<b style="color:#e0605a">合計超過 100%，已等比例縮放。</b><br>' : '') + '每度電碳排放約 <b>' + f2(ef) + ' 公斤 CO₂</b>（官方公告的電力排碳係數近年約 0.47～0.50）；進口燃料發電比例約 <b>' + Math.round(im * 100) + '%</b>；' +
        '以台電 2025 年各電源每度成本粗估，平均約 <b>' + f2(co) + ' 元/度</b>。<br><span style="color:var(--text-muted)">排放係數為粗估（燃煤 0.88、燃氣 0.38 kg/kWh）；成本為帳面發電成本的簡化，不含電網整合、儲能與備用容量。再生能源比例愈高，需要的儲能與電網投資也愈多。</span>'; }
    draw(); }

  /* ---------- 容量因數 ---------- */
  function initCf(root, cfg) {
    head(root, cfg.q); var v = el('div'), inf = info(root); root.insertBefore(v, inf);
    var D = [['核能', 0.90, C.nuc], ['燃煤', 0.75, C.coal], ['燃氣（複循環）', 0.60, C.gas], ['離岸風電', 0.38, C.wind], ['陸域風電', 0.28, C.wind], ['太陽光電', 0.14, C.solar], ['水力（川流式）', 0.30, C.hydro]];
    var g = '', y = 6; D.forEach(function (r) { var w = r[1] * 400; g += tx(150, y + 15, r[0], 11, 'currentColor', 'end') + rect(158, y + 3, w, 18, r[2]) + tx(164 + w, y + 16, Math.round(r[1] * 100) + '% → ' + f1(r[1] * 8.76) + ' 億度', 10.5, 'currentColor', 'start'); y += 27; });
    v.innerHTML = svgw('0 0 640 ' + (y + 6), g);
    inf.innerHTML = '同樣 <b>1 GW（100 萬瓩）</b>的裝置容量，一年最多能發 8.76 億度（全年滿載）。容量因數 = 實際發電量 ÷ 最大可能發電量。上面是台灣代表性的大約數值（實際每年隨天候、調度與檢修變動）。' +
        '<br>所以太陽光電佔再生能源裝置容量約三分之二，但要發同樣多的電，需要的裝置容量是核能的六倍以上。'; }

  /* ---------- 天然氣安全存量 ---------- */
  function initLng(root, cfg) {
    head(root, cfg.q); var st = 11, use = 6.3, ship = 1, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '儲槽中的存量（天份）', 5, 20, 0.5, st, function (x) { return x + ' 天'; }, 's', function (x) { st = x; draw(); });
    slider(root, '每天用量（萬噸，2025 年平均約 6.3）', 4, 9, 0.1, use, function (x) { return x; }, 'u', function (x) { use = x; draw(); });
    slider(root, '每隔幾天有一船到港（每船約 7 萬噸）', 0.5, 10, 0.5, ship, function (x) { return x + ' 天'; }, 'h', function (x) { ship = x; draw(); });
    function draw() { var cap = st * 6.3, inflow = 7 / ship, net = inflow - use, d = [], s = cap, t, empty = null;
      for (t = 0; t <= 30; t += 0.25) { d.push([t, Math.max(0, s)]); if (s <= 0 && empty === null) empty = t; s += net * 0.25; }
      v.innerHTML = chart(640, 220, [{ d: d, c: C.gas, n: '儲槽存量（萬噸）' }], { y0: 0, xl: '天', hl: [{ y: cap, c: 'var(--text-muted)', n: '起始' }] });
      inf.innerHTML = '每天進港 ' + f1(inflow) + ' 萬噸、用掉 ' + f1(use) + ' 萬噸：' + (net >= 0 ? '<b>存量維持或增加</b>。' : '每天淨減少 ' + f1(-net) + ' 萬噸，約 <b>' + f1(cap / -net) + ' 天</b>後見底。') +
        '<br>平常大約每天就有一船進港。LNG 無法像煤或石油那樣大量堆存：法定安全存量為 11 天，2027 年起提高到 14 天。所以船期一中斷，天然氣是最先告急的燃料。'; }
    draw(); }

  /* ---------- 電價與台電盈虧 ---------- */
  function initTariff(root, cfg) {
    head(root, cfg.q); var v = el('div'), inf = info(root); root.insertBefore(v, inf);
    var W = 640, H = 230, g = '', bw = 280 / TARIFF.length;
    TARIFF.forEach(function (r, i) { var h = r[1] / 4.5 * 170, x = 30 + i * bw; g += rect(x, 190 - h, bw - 10, h, '#3a6ea5') + tx(x + (bw - 10) / 2, 185 - h, r[1].toFixed(2), 9.5, 'currentColor') + tx(x + (bw - 10) / 2, 205, r[0], 8.5, 'var(--text-muted)'); });
    g += tx(170, 222, '平均電價（元/度）', 10, 'currentColor');
    PROFIT.forEach(function (r, i) { var h = Math.abs(r[1]) / 2300 * 80, x = 360 + i * 68; g += rect(x, r[1] < 0 ? 110 : 110 - h, 50, h, r[1] < 0 ? '#e0605a' : '#4caf50') + tx(x + 25, r[1] < 0 ? 110 + h + 12 : 104 - h, (r[1] > 0 ? '+' : '') + r[1], 9.5, 'currentColor') + tx(x + 25, 102 + (r[1] < 0 ? -2 : 18), r[0], 9, 'var(--text-muted)'); });
    g += ln(355, 110, 630, 110, '#999', 1) + tx(495, 222, '台電年度損益（億元）', 10, 'currentColor');
    v.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
    inf.innerHTML = '2022 年起國際燃料價格飆漲，電價沒有完全反映成本，台電連續三年虧損；2025 年燃料價格回落轉為獲利 729 億元，但累計虧損仍約 3,500 億元。' +
        '<br>2026 年 9 月審議會試算「應有調幅」12.83%（平均每度 3.78 → 4.27 元），決議 10 月凍漲、優先爭取政府追加撥補，12 月再議。（各年損益依報導，稅前／稅後口徑略有不同。）'; }

  var INIT = { mix: initMix, load: initLoad, imports: initImports, prices: initPrices, fuelcost: initFuelcost, sandbox: initSandbox, cf: initCf, lng: initLng, tariff: initTariff };
  function boot() { document.querySelectorAll('.te-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""

lesson = make_lesson(u"⚡", TE_NOTE, TELIB, "te-w")


def src(s):
    return ("raw", u'<p style="font-size:0.85em;color:var(--text-muted);margin-top:4px">資料來源：%s</p>' % s)
