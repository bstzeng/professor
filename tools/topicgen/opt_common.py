# -*- coding: utf-8 -*-
"""〈選擇權與 Black–Scholes〉（opt_）共用：課程包裝與 OPTLIB 互動元件（class="opt-w"）。

  payoff  選擇權策略損益圖：買賣權、價差、跨式、勒式、蝶式……到期損益與目前價值
  binom   二項樹：CRR 樹、歐式／美式、提前履約節點、收斂到 Black–Scholes
  bs      Black–Scholes 計算器：價格、d1/d2、希臘字母與它們對股價的曲線
  mc      蒙地卡羅：幾何布朗運動的路徑、到期價格分布、模擬價格與誤差
  hedge   Delta 避險：賣出買權後動態避險，避險頻率與實現波動度對損益分布的影響
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

OPT_NOTE = u"本課程僅供教育用途，不構成任何投資建議。選擇權具有高槓桿與高風險，數字與範例為教學用的簡化情境。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def ow(cfg, maxw=680):
    return wdg("opt-w", cfg, maxw)


OPTLIB = r"""
(function () {
  if (window.__optLib) return; window.__optLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function f3(v) { return (Math.round(v * 1000) / 1000).toString(); }
  function f4(v) { return (Math.round(v * 10000) / 10000).toString(); }
  function npdf(x) { return Math.exp(-x * x / 2) / Math.sqrt(2 * Math.PI); }
  function ncdf(x) { var t = 1 / (1 + 0.2316419 * Math.abs(x)), y = t * (0.319381530 + t * (-0.356563782 + t * (1.781477937 + t * (-1.821255978 + t * 1.330274429)))), p = 1 - npdf(x) * y; return x >= 0 ? p : 1 - p; }
  function bs(S, K, T, r, s, call) { if (T <= 1e-9) return { v: Math.max(call ? S - K : K - S, 0), d: call ? (S > K ? 1 : 0) : (S < K ? -1 : 0), g: 0, th: 0, ve: 0, d1: 0, d2: 0 };
    var sq = Math.sqrt(T), d1 = (Math.log(S / K) + (r + s * s / 2) * T) / (s * sq), d2 = d1 - s * sq, df = Math.exp(-r * T), v, d, th;
    if (call) { v = S * ncdf(d1) - K * df * ncdf(d2); d = ncdf(d1); th = -S * npdf(d1) * s / (2 * sq) - r * K * df * ncdf(d2); }
    else { v = K * df * ncdf(-d2) - S * ncdf(-d1); d = ncdf(d1) - 1; th = -S * npdf(d1) * s / (2 * sq) + r * K * df * ncdf(-d2); }
    return { v: v, d: d, g: npdf(d1) / (S * s * sq), th: th / 365, ve: S * npdf(d1) * sq / 100, d1: d1, d2: d2 }; }
  function gauss() { var u = 1 - Math.random(), v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  function hist(W, H, vals, nb, lo, hi, col, lines) { var c = [], i, mx = 0; for (i = 0; i < nb; i++) c.push(0); vals.forEach(function (v) { var k = Math.floor((v - lo) / (hi - lo) * nb); if (k >= 0 && k < nb) c[k]++; }); mx = Math.max.apply(null, c) || 1;
    var L = 40, R = 12, T = 14, B = 30, bw = (W - L - R) / nb, g = '';
    c.forEach(function (n, i) { var h = n / mx * (H - T - B); g += '<rect x="' + n1(L + i * bw + 0.5) + '" y="' + n1(H - B - h) + '" width="' + n1(bw - 1) + '" height="' + n1(h) + '" fill="' + col + '" opacity="0.8"/>'; });
    g += ln(L, H - B, W - R, H - B, '#999'); for (i = 0; i <= 4; i++) { var v = lo + (hi - lo) * i / 4; g += tx(L + (W - L - R) * i / 4, H - B + 14, f1(v), 9, 'var(--text-muted)'); }
    (lines || []).forEach(function (l) { var x = L + (l.x - lo) / (hi - lo) * (W - L - R); if (x >= L && x <= W - R) g += ln(x, T, x, H - B, l.c, 1.5, 'stroke-dasharray="5 4"') + tx(x + 3, T + 10, l.n, 9.5, l.c, 'start'); });
    return svgw('0 0 ' + W + ' ' + H, g); }

  var ST = [['買進買權', [['c', 0, 1]]], ['買進賣權', [['p', 0, 1]]], ['賣出買權', [['c', 0, -1]]], ['賣出賣權', [['p', 0, -1]]],
    ['掩護性買權', [['s', 0, 1], ['c', 1, -1]]], ['保護性賣權', [['s', 0, 1], ['p', -1, 1]]], ['多頭價差', [['c', 0, 1], ['c', 1, -1]]], ['空頭價差', [['p', 0, 1], ['p', -1, -1]]],
    ['買進跨式', [['c', 0, 1], ['p', 0, 1]]], ['買進勒式', [['c', 1, 1], ['p', -1, 1]]], ['賣出跨式', [['c', 0, -1], ['p', 0, -1]]], ['蝶式', [['c', -1, 1], ['c', 0, -2], ['c', 1, 1]]]];
  function initPayoff(root, cfg) {
    head(root, cfg.q); var P = { s: cfg.s || 0, K: 100, w: 10 }, view = el('div'), inf, S0 = 100, sg = 0.2, T = 30 / 365, r = 0.01;
    var b = bar(root); ST.forEach(function (s, i) { var x = btn(s[0], i); x.onclick = function () { P.s = i; mark(b, i); draw(); }; b.appendChild(x); }); mark(b, P.s);
    var us = [slider(root, '履約價 K', 80, 120, 1, P.K, function (x) { return x; }, null, function (x) { P.K = x; draw(); }),
      slider(root, '價差寬度（第二個履約價的距離）', 2, 20, 1, P.w, function (x) { return x; }, null, function (x) { P.w = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var legs = ST[P.s][1], cost = 0, desc = [];
      legs.forEach(function (l) { var K = P.K + l[1] * P.w; if (l[0] === 's') { cost += l[2] * S0; desc.push((l[2] > 0 ? '買進' : '賣出') + '標的（' + S0 + '）'); } else { var pr = bs(S0, K, T, r, sg, l[0] === 'c').v; cost += l[2] * pr; desc.push((l[2] > 0 ? '買進 ' : '賣出 ') + Math.abs(l[2]) + ' 口' + (l[0] === 'c' ? '買權' : '賣權') + ' K=' + K + '（權利金 ' + f2(pr) + '）'); } });
      function val(S, t) { var v = 0; legs.forEach(function (l) { var K = P.K + l[1] * P.w; v += l[2] * (l[0] === 's' ? S : bs(S, K, t, r, sg, l[0] === 'c').v); }); return v - cost; }
      var d1 = [], d2 = [], be = [], prev = null, mx = -1e9, mn = 1e9;
      for (var S = 60; S <= 140.001; S += 0.5) { var a = val(S, 0); d1.push([S, a]); d2.push([S, val(S, T)]); mx = Math.max(mx, a); mn = Math.min(mn, a); if (prev !== null && (prev[1] < 0) !== (a < 0) && Math.abs(a - prev[1]) > 1e-9) be.push(prev[0] + (S - prev[0]) * (-prev[1]) / (a - prev[1])); prev = [S, a]; }
      var lo = Math.min(-5, mn * 1.15), hi = Math.max(5, mx * 1.15);
      view.innerHTML = chart(640, 260, [{ d: [[60, 0], [140, 0]], c: GY, w: 1 }, { d: d2, c: OR, n: '目前（到期前 30 天）的損益', w: 1.6, dash: '5,4' }, { d: d1, c: BL, n: '到期時的損益', w: 2.4 }], { x0: 60, x1: 140, y0: lo, y1: hi, xl: '到期時的標的價格', vl: [{ x: S0, c: GY, n: '現價 ' + S0 }] });
      var sl = (d1[d1.length - 1][1] - d1[d1.length - 2][1]), sl0 = (d1[1][1] - d1[0][1]);
      inf.innerHTML = '<b>' + ST[P.s][0] + '</b>：' + desc.join('、') + '。<br>' + (cost > 0 ? '淨支付 ' : '淨收入 ') + f2(Math.abs(cost)) + (legs.some(function (l) { return l[0] === 's'; }) ? '（含標的）' : '（權利金）') + '。' +
        '<br>損益兩平點：' + (be.length ? be.map(function (x) { return '<b>' + f1(x) + '</b>'; }).join('、') : '（範圍內沒有）') + '。最大獲利：' + (sl > 0.01 ? '<b>無上限</b>' : '<b>' + f2(mx) + '</b>') + '；最大虧損：' + (sl < -0.01 || sl0 > 0.01 ? '<b>' + (sl < -0.01 ? '無上限' : '可能很大（標的跌到 0）') + '</b>' : '<b>' + f2(-mn) + '</b>') + '。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">權利金以 Black–Scholes 估算（現價 100、波動度 20%、30 天、利率 1%）。橘色虛線是到期前的價值——時間價值讓它比到期損益更「圓滑」。</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initBinom(root, cfg) {
    head(root, cfg.q); var P = { n: 3, s: 0.3, ty: 0 }, view = el('div'), cv = el('div'), inf, S0 = 100, K = 100, T = 1, r = 0.05;
    var b = bar(root); [['歐式買權', 0], ['歐式賣權', 1], ['美式賣權', 2]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.ty = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    var us = [slider(root, '期數 N', 1, 8, 1, P.n, function (x) { return x; }, null, function (x) { P.n = x; draw(); }),
      slider(root, '波動度 σ', 0.1, 0.6, 0.01, P.s, function (x) { return Math.round(x * 100) + '%'; }, null, function (x) { P.s = x; draw(); })];
    root.appendChild(view); root.appendChild(cv); inf = info(root);
    function tree(N) { var dt = T / N, u = Math.exp(P.s * Math.sqrt(dt)), d = 1 / u, p = (Math.exp(r * dt) - d) / (u - d), df = Math.exp(-r * dt), call = P.ty === 0, am = P.ty === 2, V = [], Sx = [], ex = [];
      for (var i = 0; i <= N; i++) { Sx[i] = []; for (var j = 0; j <= i; j++) Sx[i][j] = S0 * Math.pow(u, j) * Math.pow(d, i - j); }
      V[N] = Sx[N].map(function (s) { return Math.max(call ? s - K : K - s, 0); }); ex[N] = [];
      for (i = N - 1; i >= 0; i--) { V[i] = []; ex[i] = []; for (j = 0; j <= i; j++) { var c = df * (p * V[i + 1][j + 1] + (1 - p) * V[i + 1][j]), ix = Math.max(call ? Sx[i][j] - K : K - Sx[i][j], 0); if (am && ix > c + 1e-9) { V[i][j] = ix; ex[i][j] = 1; } else V[i][j] = c; } }
      return { V: V, S: Sx, ex: ex, u: u, d: d, p: p }; }
    function draw() { var N = P.n, t = tree(N), W = 640, H = 300, g = '', dx = 520 / N, dy = Math.min(110 / N, 34);
      function pos(i, j) { return [60 + i * dx, 150 - (2 * j - i) * dy]; }
      for (var i = 0; i < N; i++) for (var j = 0; j <= i; j++) { var a = pos(i, j), b1 = pos(i + 1, j + 1), c = pos(i + 1, j); g += ln(a[0], a[1], b1[0], b1[1], GY, 1) + ln(a[0], a[1], c[0], c[1], GY, 1); }
      for (i = 0; i <= N; i++) for (j = 0; j <= i; j++) { var q = pos(i, j), e = t.ex[i] && t.ex[i][j];
        if (N <= 4) g += '<rect x="' + n1(q[0] - 27) + '" y="' + n1(q[1] - 15) + '" width="54" height="30" rx="5" fill="' + (e ? RD : 'var(--surface)') + '" stroke="' + (e ? RD : BL) + '"/>' + tx(q[0], q[1] - 2, f1(t.S[i][j]), 9.5, e ? '#fff' : 'currentColor') + tx(q[0], q[1] + 10, f2(t.V[i][j]), 9.5, e ? '#fff' : OR);
        else g += '<circle cx="' + n1(q[0]) + '" cy="' + n1(q[1]) + '" r="5" fill="' + (e ? RD : BL) + '"/>'; }
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var cd = [], bsv = bs(S0, K, T, r, P.s, P.ty === 0).v; for (var n = 1; n <= 120; n++) cd.push([n, tree(n).V[0][0]]);
      cv.innerHTML = chart(640, 170, [{ d: cd, c: BL, n: '二項樹價格', w: 1.6 }].concat(P.ty < 2 ? [{ d: [[1, bsv], [120, bsv]], c: RD, n: 'Black–Scholes', w: 1.5, dash: '5,4' }] : []), { x0: 1, x1: 120, xl: '期數 N', y0: Math.min.apply(null, cd.map(function (p) { return p[1]; })) * 0.97, y1: Math.max.apply(null, cd.map(function (p) { return p[1]; })) * 1.03 });
      inf.innerHTML = 'S₀ = 100、K = 100、T = 1 年、r = 5%。每期上漲 u = ' + f3(t.u) + ' 倍或下跌 d = ' + f3(t.d) + ' 倍，<b>風險中性機率</b> p = ' + f3(t.p) + '。' + (N <= 4 ? '每個方塊上面是股價、下面是選擇權價值。' : '') +
        '<br>從最右邊（到期）的價值開始，一步步往回折現：V = e<sup>−rΔt</sup>[p·V<sub>上</sub> + (1−p)·V<sub>下</sub>]。' + (P.ty === 2 ? '<b>美式</b>選擇權在每個節點還要比較「立刻履約」的價值，<span style="color:' + RD + '">紅色</span>是提前履約比較划算的節點。' : '') +
        '<br>N = ' + N + ' 期的價格：<b>' + f2(t.V[0][0]) + '</b>' + (P.ty < 2 ? '；Black–Scholes：<b>' + f2(bsv) + '</b>。下圖：期數越多，二項樹越接近 Black–Scholes（會上下震盪地收斂）。' : '；同樣條件的歐式賣權（Black–Scholes）：' + f2(bs(S0, K, T, r, P.s, false).v) + '。美式比較貴，差額就是「提前履約的權利」的價值。'); }
    us.forEach(function (u) { u(); });
  }

  var GK = [['價值', 'v'], ['Delta', 'd'], ['Gamma', 'g'], ['Theta（每日）', 'th'], ['Vega（每 1%）', 've']];
  function initBS(root, cfg) {
    head(root, cfg.q); var P = { S: 100, K: 100, D: 60, s: 0.25, r: 0.02, c: 1, gk: 'v' }, view = el('div'), inf;
    var b = bar(root); [['買權', 1], ['賣權', 0]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.c = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 1);
    var us = [slider(root, '標的價格 S', 60, 140, 0.5, P.S, function (x) { return x; }, null, function (x) { P.S = x; draw(); }),
      slider(root, '履約價 K', 60, 140, 1, P.K, function (x) { return x; }, null, function (x) { P.K = x; draw(); }),
      slider(root, '距到期天數', 1, 365, 1, P.D, function (x) { return x + ' 天'; }, null, function (x) { P.D = x; draw(); }),
      slider(root, '波動度 σ', 0.05, 0.8, 0.01, P.s, function (x) { return Math.round(x * 100) + '%'; }, null, function (x) { P.s = x; draw(); }),
      slider(root, '無風險利率 r', 0, 0.1, 0.0025, P.r, function (x) { return f2(x * 100) + '%'; }, null, function (x) { P.r = x; draw(); })];
    var b2 = bar(root); GK.forEach(function (o) { var x = btn('畫出：' + o[0], o[1]); x.onclick = function () { P.gk = o[1]; mark(b2, o[1]); draw(); }; b2.appendChild(x); }); mark(b2, 'v');
    root.appendChild(view); inf = info(root);
    function draw() { var T = P.D / 365, o = bs(P.S, P.K, T, P.r, P.s, P.c), d = [], pay = [], k = P.gk;
      for (var S = 60; S <= 140.001; S += 0.5) { d.push([S, bs(S, P.K, T, P.r, P.s, P.c)[k]]); pay.push([S, Math.max(P.c ? S - P.K : P.K - S, 0)]); }
      var ser = [{ d: d, c: BL, n: GK.filter(function (g) { return g[1] === k; })[0][0], w: 2.2 }]; if (k === 'v') ser.unshift({ d: pay, c: GY, n: '到期損益（內含價值）', w: 1.2, dash: '4,3' });
      var ys = d.map(function (p) { return p[1]; }).concat(k === 'v' ? pay.map(function (p) { return p[1]; }) : []);
      view.innerHTML = chart(640, 230, ser, { x0: 60, x1: 140, y0: Math.min(0, Math.min.apply(null, ys)), y1: Math.max(1e-6, Math.max.apply(null, ys)) * 1.1 || 1, xl: '標的價格 S', pts: [{ x: P.S, y: o[k], c: RD }] });
      var iv = Math.max(P.c ? P.S - P.K : P.K - P.S, 0);
      inf.innerHTML = (P.c ? '買權' : '賣權') + '價格 = <b>' + f2(o.v) + '</b>（內含價值 ' + f2(iv) + ' + 時間價值 ' + f2(o.v - iv) + '）' +
        '<br>d₁ = ' + f2(o.d1) + '，d₂ = ' + f2(o.d2) + '，N(d₁) = ' + f3(ncdf(o.d1)) + '，N(d₂) = ' + f3(ncdf(o.d2)) + (P.c ? '（N(d₂) 是風險中性下「到期時價內」的機率）' : '') +
        '<br><b>Delta</b> ' + f3(o.d) + '　<b>Gamma</b> ' + f4(o.g) + '　<b>Theta</b> ' + f3(o.th) + '／天　<b>Vega</b> ' + f3(o.ve) + '／1% 波動度'; }
    us.forEach(function (u) { u(); });
  }

  function initMC(root, cfg) {
    head(root, cfg.q); var P = { n: 2000, s: 0.3 }, view = el('div'), hv = el('div'), inf, S0 = 100, K = 100, T = 1, r = 0.03;
    var us = [slider(root, '模擬的路徑數', 100, 20000, 100, P.n, function (x) { return x.toLocaleString(); }, null, function (x) { P.n = x; run(); }),
      slider(root, '波動度 σ', 0.1, 0.6, 0.01, P.s, function (x) { return Math.round(x * 100) + '%'; }, null, function (x) { P.s = x; run(); })];
    var b = bar(root), x0 = btn('重新抽樣'); x0.onclick = run; b.appendChild(x0);
    root.appendChild(view); root.appendChild(hv); inf = info(root);
    function run() { var steps = 50, dt = T / steps, ser = [], fin = [], sum = 0, sum2 = 0, df = Math.exp(-r * T);
      for (var k = 0; k < P.n; k++) { var S = S0, path = k < 30 ? [[0, S]] : null; for (var i = 1; i <= steps; i++) { S *= Math.exp((r - P.s * P.s / 2) * dt + P.s * Math.sqrt(dt) * gauss()); if (path) path.push([i * dt, S]); }
        if (path) ser.push({ d: path, c: 'hsla(' + (k * 37 % 360) + ',55%,50%,0.7)', w: 1 }); fin.push(S); var pay = df * Math.max(S - K, 0); sum += pay; sum2 += pay * pay; }
      var mean = sum / P.n, se = Math.sqrt(Math.max(0, sum2 / P.n - mean * mean) / P.n), bsv = bs(S0, K, T, r, P.s, true).v;
      view.innerHTML = chart(640, 200, ser, { x0: 0, x1: 1, y0: 20, y1: 260, xl: '時間（年）——前 30 條路徑', hl: [{ y: K, c: RD, n: '履約價 100' }] });
      hv.innerHTML = hist(640, 150, fin, 50, 0, 300, BL, [{ x: K, c: RD, n: 'K' }]);
      inf.innerHTML = '幾何布朗運動（風險中性，漂移 = r = 3%）。下圖是 ' + P.n.toLocaleString() + ' 條路徑的到期價格分布——<b>右偏</b>的對數常態分布：跌最多到 0，漲沒有上限。' +
        '<br>買權價格 = 平均（折現後的 max(S<sub>T</sub> − K, 0)）≈ <b>' + f2(mean) + '</b> ± ' + f2(1.96 * se) + '（95% 信賴區間）。Black–Scholes 公式：<b>' + f2(bsv) + '</b>。' +
        '<br>誤差與 1/√N 成正比：路徑數變成 4 倍，誤差才減半。這是蒙地卡羅方法的特性（見〈蒙地卡羅方法〉）。'; }
    us[1](); us[0]();
  }

  var HF = [['每月', 3], ['每週', 13], ['每天', 63], ['每天 4 次', 252]];
  function initHedge(root, cfg) {
    head(root, cfg.q); var P = { f: 2, rv: 0.2 }, view = el('div'), inf, S0 = 100, K = 100, T = 0.25, iv = 0.2;
    var b = bar(root); HF.forEach(function (o, i) { var x = btn('避險頻率：' + o[0], i); x.onclick = function () { P.f = i; mark(b, i); run(); }; b.appendChild(x); }); mark(b, P.f);
    var u = slider(root, '實際的（實現）波動度', 0.1, 0.4, 0.01, P.rv, function (x) { return Math.round(x * 100) + '%（定價用的隱含波動度 20%）'; }, null, function (x) { P.rv = x; run(); });
    var b2 = bar(root), x0 = btn('重新模擬'); x0.onclick = run; b2.appendChild(x0);
    root.appendChild(view); inf = info(root);
    function run() { var n = HF[P.f][1], dt = T / n, prem = bs(S0, K, T, 0, iv, true).v, pl = [];
      for (var k = 0; k < 600; k++) { var S = S0, del = bs(S, K, T, 0, iv, true).d, cash = prem - del * S;
        for (var i = 1; i <= n; i++) { S *= Math.exp(-P.rv * P.rv / 2 * dt + P.rv * Math.sqrt(dt) * gauss()); var tl = T - i * dt, nd = i < n ? bs(S, K, tl, 0, iv, true).d : (S > K ? 1 : 0); cash -= (nd - del) * S; del = nd; }
        pl.push(cash + del * S - Math.max(S - K, 0)); }
      var m = pl.reduce(function (a, b) { return a + b; }, 0) / pl.length, sd = Math.sqrt(pl.reduce(function (a, b) { return a + (b - m) * (b - m); }, 0) / pl.length);
      view.innerHTML = hist(640, 200, pl, 50, -6, 6, P.rv > iv + 0.01 ? RD : P.rv < iv - 0.01 ? GN : BL, [{ x: 0, c: GY, n: '0' }, { x: m, c: OR, n: '平均' }]);
      inf.innerHTML = '你以 ' + f2(prem) + ' 的權利金<b>賣出</b>一口 3 個月的平價買權（定價用 20% 的波動度），然後持有 Delta 股的標的來避險，' + HF[P.f][0] + '調整一次。上圖是 600 次模擬的最終損益分布。' +
        '<br>平均損益 <b>' + f2(m) + '</b>，標準差 <b>' + f2(sd) + '</b>。' +
        (Math.abs(P.rv - iv) < 0.01 ? '<br>實際波動度等於定價的波動度時，平均損益約為 0：避險完美地「複製」了選擇權。避險越頻繁，分布越窄——連續避險時，風險會完全消失，這正是 Black–Scholes 的核心論證。' :
          P.rv > iv ? '<br>實際波動度<b>高於</b>你賣出的波動度：你賣得太便宜了，避險的成本（不斷「買高賣低」）超過了收到的權利金，平均是<b>虧損</b>。' : '<br>實際波動度<b>低於</b>你賣出的波動度：你賣得比較貴，平均是<b>獲利</b>。選擇權交易，本質上是在交易波動度。'); }
    u();
  }

  function initAll() { document.querySelectorAll('.opt-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ payoff: initPayoff, binom: initBinom, bs: initBS, mc: initMC, hedge: initHedge })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"📈", OPT_NOTE, OPTLIB, "opt-w")

PAYOFF = ow({"t": "payoff", "q": u"選擇權損益圖：選一種策略，調整履約價"})
PAYOFF2 = ow({"t": "payoff", "q": u"選擇權策略：組合出不同形狀的損益", "s": 8})
BINOM = ow({"t": "binom", "q": u"二項樹定價：從到期往回推"})
BSCALC = ow({"t": "bs", "q": u"Black–Scholes 計算器與希臘字母"})
MC = ow({"t": "mc", "q": u"蒙地卡羅定價：模擬幾千條股價路徑"})
HEDGE = ow({"t": "hedge", "q": u"Delta 避險：賣出選擇權之後，能把風險避掉嗎"})
