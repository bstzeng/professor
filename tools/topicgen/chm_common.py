# -*- coding: utf-8 -*-
"""〈化學：元素與化學鍵〉（chm_）共用：課程包裝與 CHMLIB 互動元件（class="chm-w"）。

  ptable  互動週期表：分類／電負度著色，點元素看電子組態
  shape   分子形狀（VSEPR）：可旋轉的 3D 投影
  rate    反應速率：溫度、活化能、催化劑與波茲曼分布
  titr    酸鹼滴定曲線：強酸、弱酸，以 0.1 M NaOH 滴定
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

CHM_NOTE = u"互動模擬為教學用的簡化模型；實驗操作請在有老師指導與安全設備的實驗室進行。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def cw(cfg, maxw=680):
    return wdg("chm-w", cfg, maxw)


CHMLIB = r"""
(function () {
  if (window.__chmLib) return; window.__chmLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }

  var SYM = 'H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og'.split(' ');
  var NM = '氫氦鋰鈹硼碳氮氧氟氖鈉鎂鋁矽磷硫氯氬鉀鈣鈧鈦釩鉻錳鐵鈷鎳銅鋅鎵鍺砷硒溴氪銣鍶釔鋯鈮鉬鎝釕銠鈀銀鎘銦錫銻碲碘氙銫鋇鑭鈰鐠釹鉕釤銪釓鋱鏑鈥鉺銩鐿鎦鉿鉭鎢錸鋨銥鉑金汞鉈鉛鉍釙砈氡鍅鐳錒釷鏷鈾錼鈽鋂鋦鉳鉲鑀鐨鍆鍩鐒'.split('');
  var EN = [2.20,0,0.98,1.57,2.04,2.55,3.04,3.44,3.98,0,0.93,1.31,1.61,1.90,2.19,2.58,3.16,0,0.82,1.00,1.36,1.54,1.63,1.66,1.55,1.83,1.88,1.91,1.90,1.65,1.81,2.01,2.18,2.55,2.96,3.00,0.82,0.95,1.22,1.33,1.6,2.16,1.9,2.2,2.28,2.20,1.93,1.69,1.78,1.96,2.05,2.1,2.66,2.6,0.79,0.89];
  var CAT = { am: ['鹼金屬', '#f2a07b'], ae: ['鹼土金屬', '#f5cf7a'], tm: ['過渡金屬', '#e9b8b8'], pt: ['後過渡金屬', '#c9d4e0'], md: ['類金屬', '#b9dcb0'], nm: ['非金屬', '#9fd3c7'], ha: ['鹵素', '#a9c8ef'], ng: ['惰性氣體', '#cdb8ea'], la: ['鑭系', '#f0c4de'], ac: ['錒系', '#e3c2a6'] };
  function cat(z) { if ([3,11,19,37,55,87].indexOf(z) >= 0) return 'am'; if ([4,12,20,38,56,88].indexOf(z) >= 0) return 'ae'; if ([2,10,18,36,54,86,118].indexOf(z) >= 0) return 'ng';
    if ([9,17,35,53,85,117].indexOf(z) >= 0) return 'ha'; if ([1,6,7,8,15,16,34].indexOf(z) >= 0) return 'nm'; if ([5,14,32,33,51,52].indexOf(z) >= 0) return 'md';
    if (z >= 57 && z <= 71) return 'la'; if (z >= 89 && z <= 103) return 'ac'; if ([13,31,49,50,81,82,83,84,113,114,115,116].indexOf(z) >= 0) return 'pt'; return 'tm'; }
  function pos(z) { if (z == 1) return [1, 1]; if (z == 2) return [18, 1];
    var P = [[3, 10, 2], [11, 18, 3], [19, 36, 4], [37, 54, 5], [55, 86, 6], [87, 118, 7]];
    for (var i = 0; i < P.length; i++) { var a = P[i][0], b = P[i][1], p = P[i][2]; if (z < a || z > b) continue; var k = z - a;
      if (p <= 3) return [k < 2 ? k + 1 : k + 18 - (b - a), p];
      if (p <= 5) return [k + 1, p];
      if (k < 2) return [k + 1, p]; if (k <= 16) return [k + 1, p + 2.6]; return [k - 14 + 1, p]; } return [1, 1]; }
  var ORB = [['1s', 2], ['2s', 2], ['2p', 6], ['3s', 2], ['3p', 6], ['4s', 2], ['3d', 10], ['4p', 6], ['5s', 2], ['4d', 10], ['5p', 6], ['6s', 2], ['4f', 14], ['5d', 10], ['6p', 6], ['7s', 2], ['5f', 14], ['6d', 10], ['7p', 6]];
  var SUP = '⁰¹²³⁴⁵⁶⁷⁸⁹'; function sup(n) { return String(n).split('').map(function (c) { return SUP[+c]; }).join(''); }
  function conf(z) { var r = [], left = z; for (var i = 0; i < ORB.length && left > 0; i++) { var n = Math.min(left, ORB[i][1]); r.push(ORB[i][0] + sup(n)); left -= n; } return r.join(' '); }
  function initPT(root, cfg) {
    head(root, cfg.q); var P = { m: 0, s: 6 }, view = el('div'), inf;
    var b = bar(root); [['分類', 0], ['電負度', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.m = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    root.appendChild(view); inf = info(root);
    function enCol(v) { if (!v) return '#e4e4e4'; var t = Math.min(Math.max((v - 0.7) / 3.3, 0), 1); return 'hsl(' + Math.round(220 - 220 * t) + ',65%,' + Math.round(78 - 18 * t) + '%)'; }
    function draw() { var g = '', W = 34, H = 34, x0 = 14, y0 = 8;
      for (var z = 1; z <= 118; z++) { var p = pos(z), x = x0 + (p[0] - 1) * W, y = y0 + (p[1] - 1) * H, c = P.m ? enCol(EN[z - 1]) : CAT[cat(z)][1];
        g += '<g data-z="' + z + '" style="cursor:pointer"><rect x="' + n1(x) + '" y="' + n1(y) + '" width="' + (W - 2) + '" height="' + (H - 2) + '" rx="3" fill="' + c + '" stroke="' + (z == P.s ? '#333' : 'none') + '" stroke-width="2"/>' +
          tx(x + 4, y + 10, z, 7.5, '#444', 'start') + tx(x + W / 2 - 1, y + 25, SYM[z - 1], 12, '#222') + '</g>'; }
      g += tx(x0 + 2 * W + 16, y0 + 5 * H + 22, '57–71', 8, '#666') + tx(x0 + 2 * W + 16, y0 + 6 * H + 22, '89–103', 8, '#666');
      if (!P.m) { var lx = x0 + 2.2 * W, ly = y0 + 3, k = 0; for (var c in CAT) { g += '<rect x="' + n1(lx + (k % 5) * 92) + '" y="' + n1(ly + Math.floor(k / 5) * 16) + '" width="10" height="10" fill="' + CAT[c][1] + '"/>' + tx(lx + (k % 5) * 92 + 14, ly + Math.floor(k / 5) * 16 + 9, CAT[c][0], 9, 'currentColor', 'start'); k++; } }
      else g += tx(x0 + 2.2 * W, y0 + 18, '電負度：藍（低）→ 紅（高）；灰色＝本圖未列數值', 9.5, 'currentColor', 'start');
      view.innerHTML = svgw('0 0 640 ' + (y0 + 9.7 * H), g);
      view.querySelectorAll('g[data-z]').forEach(function (e) { e.onclick = function () { P.s = +e.getAttribute('data-z'); draw(); }; });
      var z = P.s, p = pos(z), per = p[1] > 7 ? Math.round(p[1] - 2.6) : p[1], en = EN[z - 1];
      inf.innerHTML = '<b>' + SYM[z - 1] + '　' + (NM[z - 1] || '（超重元素）') + '</b>　原子序 ' + z + '　第 ' + per + ' 週期' + (z >= 57 && z <= 71 || z >= 89 && z <= 103 ? '' : '、第 ' + p[0] + ' 族') + '　' + CAT[cat(z)][0] +
        '<br>電子組態（依構築原理）：' + conf(z) + (en ? '<br>鮑林電負度：<b>' + en + '</b>' : '') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">少數元素（例如鉻、銅）的真實組態與構築原理的預測不同，因為半滿或全滿的 d 軌域特別穩定。</span>'; }
    draw();
  }

  var SH = { CH4: ['甲烷 CH₄', '四面體', '109.5°', 0, [[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]], 'C', 'H'],
    NH3: ['氨 NH₃', '三角錐', '約 107°', 1, [[1, 1, 1], [1, -1, -1], [-1, 1, -1]], 'N', 'H', [[-1, -1, 1]]],
    H2O: ['水 H₂O', '彎曲形', '約 104.5°', 2, [[1, 1, 1], [1, -1, -1]], 'O', 'H', [[-1, 1, -1], [-1, -1, 1]]],
    CO2: ['二氧化碳 CO₂', '直線形', '180°', 0, [[1.6, 0, 0], [-1.6, 0, 0]], 'C', 'O'],
    BF3: ['三氟化硼 BF₃', '平面三角形', '120°', 0, [[1.6, 0, 0], [-0.8, 1.386, 0], [-0.8, -1.386, 0]], 'B', 'F'],
    PCl5: ['五氯化磷 PCl₅', '雙三角錐', '90°、120°', 0, [[0, 0, 1.6], [0, 0, -1.6], [1.6, 0, 0], [-0.8, 1.386, 0], [-0.8, -1.386, 0]], 'P', 'Cl'],
    SF6: ['六氟化硫 SF₆', '八面體', '90°', 0, [[1.6, 0, 0], [-1.6, 0, 0], [0, 1.6, 0], [0, -1.6, 0], [0, 0, 1.6], [0, 0, -1.6]], 'S', 'F'] };
  function initShape(root, cfg) {
    head(root, cfg.q); var P = { k: 'CH4', a: 30, e: 20 }, view = el('div'), inf;
    var b = bar(root); Object.keys(SH).forEach(function (k) { var x = btn(SH[k][0].split(' ')[1], k); x.onclick = function () { P.k = k; mark(b, k); draw(); }; b.appendChild(x); }); mark(b, 'CH4');
    var us = [slider(root, '水平旋轉', 0, 360, 1, P.a, function (x) { return x + '°'; }, null, function (x) { P.a = x; draw(); }),
      slider(root, '俯仰', -80, 80, 1, P.e, function (x) { return x + '°'; }, null, function (x) { P.e = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var s = SH[P.k], A = P.a * Math.PI / 180, E = P.e * Math.PI / 180, cx = 320, cy = 150, R = 70;
      function pr(v) { var n = Math.hypot(v[0], v[1], v[2]), u = [v[0] / n * 1.6, v[1] / n * 1.6, v[2] / n * 1.6];
        var x = u[0] * Math.cos(A) - u[1] * Math.sin(A), y = u[0] * Math.sin(A) + u[1] * Math.cos(A), z = u[2];
        var y2 = y * Math.cos(E) - z * Math.sin(E), z2 = y * Math.sin(E) + z * Math.cos(E); return [cx + x * R, cy - z2 * R, y2]; }
      var items = s[4].map(function (v) { var p = pr(v); return { p: p, t: 'a' }; }).concat((s[7] || []).map(function (v) { var p = pr(v); return { p: [cx + (p[0] - cx) * 0.62, cy + (p[1] - cy) * 0.62, p[2]], t: 'l' }; }));
      items.sort(function (a, b) { return b.p[2] - a.p[2]; });
      var g = '', ctr = '<circle cx="' + cx + '" cy="' + cy + '" r="22" fill="#555"/>' + tx(cx, cy + 5, s[5], 14, '#fff');
      var drawn = false; items.forEach(function (it) { if (!drawn && it.p[2] < 0) { g += ctr; drawn = true; }
        var sc = 1 - it.p[2] * 0.12;
        if (it.t == 'a') g += ln(cx, cy, it.p[0], it.p[1], '#888', 6) + '<circle cx="' + n1(it.p[0]) + '" cy="' + n1(it.p[1]) + '" r="' + n1(16 * sc) + '" fill="' + (s[6] == 'H' ? '#eee' : s[6] == 'O' ? '#e06060' : '#7cc47c') + '" stroke="#666"/>' + tx(it.p[0], it.p[1] + 4, s[6], 11, '#222');
        else g += '<ellipse cx="' + n1(it.p[0]) + '" cy="' + n1(it.p[1]) + '" rx="' + n1(13 * sc) + '" ry="' + n1(9 * sc) + '" fill="#cdb8ea" opacity="0.8"/>' + tx(it.p[0], it.p[1] + 3, '‥', 11, '#553'); });
      if (!drawn) g += ctr;
      view.innerHTML = svgw('0 0 640 300', g);
      inf.innerHTML = '<b>' + s[0] + '</b>：中心原子周圍有 ' + (s[4].length + s[3]) + ' 個電子對區域（' + s[4].length + ' 個鍵結、' + s[3] + ' 個孤對電子）→ 形狀是<b>' + s[1] + '</b>，鍵角 ' + s[2] + '。' +
        (s[3] ? '<br>紫色的是<b>孤對電子</b>：它們不是原子，但同樣佔據空間，而且排斥力比鍵結電子更強，把鍵角「擠」得比 109.5° 小。' : '<br>電子對彼此排斥，會盡量互相遠離——這就是 VSEPR（價殼層電子對互斥）理論的核心。'); }
    us.forEach(function (u) { u(); });
  }

  function initRate(root, cfg) {
    head(root, cfg.q); var P = { T: 300, Ea: 50, cat: 0 }, view = el('div'), inf;
    var us = [slider(root, '溫度', 250, 450, 5, P.T, function (x) { return x + ' K（' + (x - 273) + ' °C）'; }, null, function (x) { P.T = x; draw(); }),
      slider(root, '活化能', 20, 100, 1, P.Ea, function (x) { return x + ' kJ/mol'; }, null, function (x) { P.Ea = x; draw(); })];
    var b = bar(root), cb = btn('催化劑：無'); cb.onclick = function () { P.cat ^= 1; cb.textContent = '催化劑：' + (P.cat ? '有（活化能降低 40%）' : '無'); draw(); }; b.appendChild(cb);
    root.appendChild(view); inf = info(root);
    var R = 8.314e-3;
    function fd(E, kT) { return 2 * Math.sqrt(E / Math.PI) * Math.pow(kT, -1.5) * Math.exp(-E / kT); }
    function sci(v) { if (v >= 1e-3) return f2(v * 100) + '%'; var e = Math.floor(Math.log10(v)), m = v / Math.pow(10, e); return f1(m) + '×10<sup>' + e + '</sup>'; }
    function draw() { var Ea = P.Ea * (P.cat ? 0.6 : 1), kT = R * P.T, X1 = Math.max(Ea * 1.5, 25), mx = 0, d = [], d0 = [], dm = [];
      for (var E = 0; E <= X1; E += X1 / 300) { var f = fd(E, kT); d.push([E, f]); d0.push([E, fd(E, R * 300)]); if (f > mx) mx = f; }
      var fa = fd(Ea, kT), N = Math.pow(10, Math.max(0, Math.floor(Math.log10(0.6 * mx / Math.max(fa, 1e-300)))));
      for (var E2 = Ea; E2 <= X1; E2 += X1 / 300) dm.push([E2, fd(E2, kT) * N]);
      var frac = Math.exp(-Ea / kT) * (1 + Ea / kT), ref = Math.exp(-P.Ea / (R * 300)) * (1 + P.Ea / (R * 300)), rel = frac / ref;
      var S = [{ d: d0, c: GY, n: '300 K（參考）', w: 1.2, dash: '4,3' }, { d: d, c: BL, n: '分子動能的分布（' + P.T + ' K）', w: 2.2 }, { d: dm, c: RD, n: '超過活化能的部分' + (N > 1 ? '（放大 ' + (N >= 1e4 ? '10^' + Math.round(Math.log10(N)) : N) + ' 倍）' : ''), w: 2.6 }];
      view.innerHTML = chart(640, 230, S, { x0: 0, x1: X1, y0: 0, y1: mx * 1.15, xl: '分子的動能（kJ/mol）', vl: [{ x: Ea, c: RD, n: '活化能 ' + f1(Ea) }] });
      inf.innerHTML = '能量超過活化能的分子比例約 <b>' + sci(frac) + '</b>——非常少，所以紅色的尾巴必須放大才看得見。和 300 K、沒有催化劑相比，反應速率約為 <b>' + (rel >= 100 ? Math.round(rel).toLocaleString() : f2(rel)) + ' 倍</b>。' +
        '<br>阿瑞尼斯方程式：k = A·e<sup>−Ea/RT</sup>。溫度升高，曲線的尾巴變長；活化能降低（催化劑），門檻往左移——兩者都讓更多分子「跨過門檻」。<br><span style="font-size:0.9em;color:var(--text-muted)">經驗法則：許多反應在室溫附近，溫度每升高 10 °C，速率約增加為 2～3 倍。</span>'; }
    us.forEach(function (u) { u(); });
  }

  var AC = [['強酸（鹽酸）', 1e3], ['弱酸（醋酸，pKa 4.76）', 1.74e-5], ['很弱的酸（pKa 9.2）', 6.3e-10]];
  function initTitr(root, cfg) {
    head(root, cfg.q); var P = { a: 1, v: 12.5 }, view = el('div'), inf;
    var b = bar(root); AC.forEach(function (o, i) { var x = btn(o[0], i); x.onclick = function () { P.a = i; mark(b, i); draw(); }; b.appendChild(x); }); mark(b, 1);
    var us = [slider(root, '加入的 0.1 M NaOH', 0, 50, 0.5, P.v, function (x) { return x + ' mL'; }, null, function (x) { P.v = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function pH(Ka, V) { var Va = 25, C = 0.1, tot = Va + V, Ca = C * Va / tot, Na = C * V / tot, lo = -15, hi = 1;
      for (var i = 0; i < 80; i++) { var m = (lo + hi) / 2, H = Math.pow(10, m), f = H + Na - Ca * Ka / (Ka + H) - 1e-14 / H; if (f > 0) hi = m; else lo = m; } return -(lo + hi) / 2; }
    function draw() { var Ka = AC[P.a][1], d = []; for (var V = 0; V <= 50; V += 0.25) d.push([V, pH(Ka, V)]);
      var p = pH(Ka, P.v), pe = pH(Ka, 25);
      view.innerHTML = chart(640, 240, [{ d: d, c: PU, n: '滴定曲線：25 mL 0.1 M 的酸', w: 2.4 }], { x0: 0, x1: 50, y0: 0, y1: 14, xl: '加入的 NaOH（mL）', yl: 'pH', hl: [{ y: 7, c: GY, n: 'pH 7' }], vl: [{ x: 25, c: OR, n: '當量點' }], pts: [{ x: P.v, y: p, c: RD, n: 'pH ' + f1(p) }] });
      inf.innerHTML = '加入 ' + P.v + ' mL 時，pH ≈ <b>' + f1(p) + '</b>；當量點（25 mL）的 pH ≈ <b>' + f1(pe) + '</b>。' +
        (P.a == 0 ? '<br>強酸完全解離：曲線在當量點附近「垂直跳升」，當量點 pH = 7。' : P.a == 1 ? '<br>弱酸：一開始 pH 較高；在加到一半（12.5 mL）時 pH = pKa——這一段曲線平緩，就是<b>緩衝區</b>。當量點的溶液含有醋酸根，呈弱鹼性，所以要用在鹼性範圍變色的酚酞當指示劑。' : '<br>酸太弱時，當量點附近的跳躍很小，很難用指示劑判斷終點。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">以質量平衡與電荷平衡數值計算，假設 25 °C、理想溶液。</span>'; }
    mark(b, 1); us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.chm-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ ptable: initPT, shape: initShape, rate: initRate, titr: initTitr })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"⚗️", CHM_NOTE, CHMLIB, "chm-w")

PTABLE = cw({"t": "ptable", "q": u"互動週期表：點選元素，看它的位置、分類與電子組態"})
SHAPE = cw({"t": "shape", "q": u"分子的形狀：拖動拉桿旋轉分子"})
RATE = cw({"t": "rate", "q": u"為什麼溫度越高、反應越快：分子動能的分布與活化能"})
TITR = cw({"t": "titr", "q": u"酸鹼滴定曲線：用 0.1 M 氫氧化鈉滴定 25 mL 的 0.1 M 酸"})
