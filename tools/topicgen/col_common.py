# -*- coding: utf-8 -*-
"""〈大型對撞機〉（col_）共用：課程包裝與 COLLIB 互動元件（class="col-w"）。

  bump    不變質量峰值搜尋：訊號強度、累積亮度 → 觀察到的直方圖與顯著性
  pois    卜瓦松計數實驗：預期背景 b、觀察到 n → p 值與 Z
  lee     別處效應：純背景的隨機資料中，最大的局部顯著性有多大
  cls     CLs 排除上限：計數實驗的 95% 上限，與 CLs+b 比較
  track   磁場中的徑跡：動量、磁場 → 曲率半徑與矢高
  dimu    雙緲子不變質量譜：η、ρ/ω、φ、J/ψ、ψ′、Υ、Z
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

COL_NOTE = (u"本課的數字以 LHC 與各實驗公開的設計值、論文為準，部分為約略值；互動模擬為教學用的簡化模型，"
            u"不是真實的實驗資料。推導省略了部分嚴格性。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def PAPER(text, ref):
    """論文引用：text 為說明，ref 為期刊或 arXiv 編號（純文字）。"""
    return u"%s（<span style=\"font-family:ui-monospace,Menlo,monospace;font-size:0.92em\">%s</span>）" % (text, ref)


def colw(cfg, maxw=680):
    return wdg("col-w", cfg, maxw)


COLLIB = r"""
(function () {
  if (window.__colLib) return; window.__colLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', PU = '#8a5cb8', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function randn() { var u = 1 - Math.random(), v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  function pois(l) { if (l > 50) return Math.max(0, Math.round(l + Math.sqrt(l) * randn())); var L = Math.exp(-l), k = 0, p = 1; do { k++; p *= Math.random(); } while (p > L); return k - 1; }
  function lgam(x) { var c = [76.18009172947146, -86.50532032941677, 24.01409824083091, -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5], y = x, t = x + 5.5; t -= (x + 0.5) * Math.log(t); var s = 1.000000000190015; for (var j = 0; j < 6; j++) s += c[j] / ++y; return -t + Math.log(2.5066282746310005 * s / x); }
  function pmf(k, l) { return l <= 0 ? (k === 0 ? 1 : 0) : Math.exp(k * Math.log(l) - l - lgam(k + 1)); }
  function cdf(n, l) { var s = 0; for (var k = 0; k <= n; k++) s += pmf(k, l); return Math.min(1, s); }
  function sf(n, l) { if (n <= 0) return 1; var s = 0, k, t; if (n > l + 60 * Math.sqrt(l + 1) + 60) return 0; for (k = n; k < n + 400 + 20 * Math.sqrt(l); k++) { t = pmf(k, l); s += t; if (t < 1e-30 * s && k > l) break; } return Math.min(1, s); }
  function erfc(x) { var z = Math.abs(x), t = 1 / (1 + z / 2), r = t * Math.exp(-z * z - 1.26551223 + t * (1.00002368 + t * (0.37409196 + t * (0.09678418 + t * (-0.18628806 + t * (0.27886807 + t * (-1.13520398 + t * (1.48851587 + t * (-0.82215223 + t * 0.17087277))))))))); return x >= 0 ? r : 2 - r; }
  function pOfZ(z) { return 0.5 * erfc(z / Math.SQRT2); }
  function zOfP(p) { if (p >= 0.5) return 0; if (p <= 0) return 40; var lo = 0, hi = 40; for (var i = 0; i < 80; i++) { var m = (lo + hi) / 2; if (pOfZ(m) > p) lo = m; else hi = m; } return (lo + hi) / 2; }
  function zAsimov(s, b) { return b > 0 && s > 0 ? Math.sqrt(2 * ((s + b) * Math.log(1 + s / b) - s)) : 0; }
  function sci(p) { if (p >= 0.001) return f2(p * 1000) / 1000 + ''; var e = Math.floor(Math.log10(p)), m = p / Math.pow(10, e); return f1(m) + '×10<sup>' + e + '</sup>'; }
  function hist(W, H, edges, data, opt) { opt = opt || {}; var L = 52, R = 12, T = 22, B = 34, n = data.length, ymax = opt.ymax || Math.max.apply(null, data.concat(opt.curves ? opt.curves.reduce(function (a, c) { return a.concat(c.d.map(function (p) { return p[1]; })); }, []) : [])) * 1.15 || 1;
    var x0 = edges[0], x1 = edges[n]; function sx(v) { return L + (v - x0) / (x1 - x0) * (W - L - R); } function sy(v) { return H - B - v / ymax * (H - T - B); }
    var g = ''; nice(0, ymax, 4).forEach(function (v) { g += ln(L, sy(v), W - R, sy(v), 'var(--border)', 0.6, 'stroke-dasharray="2 3"') + tx(L - 5, sy(v) + 3, v >= 1000 ? f1(v / 1000) + 'k' : v, 9, 'var(--text-muted)', 'end'); });
    nice(x0, x1, 6).forEach(function (v) { g += tx(sx(v), H - B + 14, v, 9, 'var(--text-muted)'); });
    g += ln(L, T - 4, L, H - B, '#999') + ln(L, H - B, W - R, H - B, '#999');
    if (opt.xl) g += tx((L + W - R) / 2, H - 4, opt.xl, 9.5, 'var(--text-muted)'); if (opt.yl) g += tx(L - 46, T - 8, opt.yl, 9.5, 'var(--text-muted)', 'start');
    (opt.band || []).forEach(function (bd) { g += '<rect x="' + n1(sx(bd[0])) + '" y="' + T + '" width="' + n1(sx(bd[1]) - sx(bd[0])) + '" height="' + (H - T - B) + '" fill="' + bd[2] + '" opacity="0.12"/>'; });
    (opt.curves || []).forEach(function (c) { var d = ''; c.d.forEach(function (p, i) { d += (i ? 'L' : 'M') + n1(sx(p[0])) + ' ' + n1(sy(p[1])); }); g += '<path d="' + d + '" fill="none" stroke="' + c.c + '" stroke-width="' + (c.w || 2) + '"' + (c.dash ? ' stroke-dasharray="' + c.dash + '"' : '') + '/>'; });
    for (var i = 0; i < n; i++) { var xc = (edges[i] + edges[i + 1]) / 2, v = data[i]; g += '<circle cx="' + n1(sx(xc)) + '" cy="' + n1(sy(v)) + '" r="2.3" fill="currentColor"/>'; if (v > 0) g += ln(sx(xc), sy(v + Math.sqrt(v)), sx(xc), sy(Math.max(0, v - Math.sqrt(v))), 'currentColor', 0.8); }
    var lx = L + 8; (opt.curves || []).forEach(function (c) { if (!c.n) return; g += ln(lx, T + 2, lx + 16, T + 2, c.c, 2.5, c.dash ? 'stroke-dasharray="' + c.dash + '"' : '') + tx(lx + 20, T + 6, c.n, 9.5, 'currentColor', 'start'); lx += 34 + c.n.length * 10.5; });
    return svgw('0 0 ' + W + ' ' + H, g); }

  /* ---------- 峰值搜尋 ---------- */
  function initBump(root, cfg) {
    head(root, cfg.q); var P = { mu: 1, L: 20 }, view = el('div'), inf, data = null;
    var us = [slider(root, '訊號強度 μ（1 = 標準模型的希格斯）', 0, 3, 0.1, P.mu, function (x) { return f1(x); }, null, function (x) { P.mu = x; gen(); }),
      slider(root, '累積亮度', 1, 300, 1, P.L, function (x) { return x + ' fb⁻¹'; }, null, function (x) { P.L = x; gen(); })];
    var b = bar(root), go = btn('重新產生一次資料（新的隨機漲落）'); go.onclick = gen; b.appendChild(go); root.appendChild(view); inf = info(root);
    var E = []; for (var m = 100; m <= 160.001; m += 1.5) E.push(m); var NB = E.length - 1;
    function bkg(m) { return 1050 * Math.exp(-(m - 100) / 33); } function sig(m) { return 70 * Math.exp(-0.5 * Math.pow((m - 125) / 1.7, 2)); }
    function gen() { var k = P.L / 20, obs = [], cb = [], cs = []; for (var i = 0; i < NB; i++) { var mc = (E[i] + E[i + 1]) / 2, bb = bkg(mc) * k, ss = P.mu * sig(mc) * k; obs.push(pois(bb + ss)); }
      for (var x = 100; x <= 160; x += 0.5) { cb.push([x, bkg(x) * k]); cs.push([x, (bkg(x) + P.mu * sig(x)) * k]); }
      var S = 0, Bk = 0, N = 0; for (i = 0; i < NB; i++) { var c = (E[i] + E[i + 1]) / 2; if (Math.abs(c - 125) < 3.4) { S += P.mu * sig(c) * k; Bk += bkg(c) * k; N += obs[i]; } }
      var zexp = zAsimov(S, Bk), zobs = N > Bk ? zAsimov(N - Bk, Bk) : 0;
      view.innerHTML = hist(640, 260, E, obs, { xl: '雙光子不變質量 mγγ（GeV）', yl: '事件數 / 1.5 GeV', band: [[121.6, 128.4, OR]], curves: [{ d: cb, c: BL, n: '只有背景', dash: '6 4' }, { d: cs, c: RD, n: '背景＋訊號' }] });
      inf.innerHTML = '在 125 ± 3.4 GeV 的視窗內（橘色）：預期背景 <b>' + Math.round(Bk) + '</b>、預期訊號 <b>' + Math.round(S) + '</b>、實際觀察 <b>' + N + '</b> 個事件。' +
        '<br>預期顯著性 <b>' + f1(zexp) + 'σ</b>；這一次的「資料」對應的顯著性約 <b style="color:' + (zobs >= 5 ? RD : 'inherit') + '">' + f1(zobs) + 'σ</b>' + (zobs >= 5 ? '——達到「發現」的 5σ！' : zobs >= 3 ? '——達到「證據」的 3σ。' : '。') +
        '<br>訊號只是背景上一個小小的突起。顯著性大約和 <b>S/√B</b> 成正比，而 S 與 B 都和亮度成正比，所以顯著性 ∝ <b>√亮度</b>：資料量變成 4 倍，顯著性才變成 2 倍。<br>（教學模型只用一個質量窗口；真實分析把事件分成十多個類別，同樣的資料能得到更高的顯著性。）' + (P.mu === 0 ? '<br>μ = 0 時沒有訊號，但背景的隨機漲落有時也會在某處冒出一個小峰——這就是第 45 課的別處效應。' : ''); }
    us.forEach(function (u) { u(); });
  }

  /* ---------- 卜瓦松計數 ---------- */
  function initPois(root, cfg) {
    head(root, cfg.q); var P = { b: cfg.b || 3.2, n: cfg.n || 10 }, view = el('div'), inf;
    var us = [slider(root, '預期背景 b', 0.1, 50, 0.1, P.b, function (x) { return f1(x); }, null, function (x) { P.b = x; draw(); }),
      slider(root, '實際觀察到的事件數 n', 0, 100, 1, P.n, function (x) { return x; }, null, function (x) { P.n = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var K = Math.max(20, Math.ceil(P.b + 6 * Math.sqrt(P.b) + 5), P.n + 3), E = [], d = []; for (var k = 0; k <= K; k++) { E.push(k - 0.5); d.push(pmf(k, P.b)); } E.push(K + 0.5);
      var W = 640, H = 220, L = 46, R = 12, T = 16, B = 32, ym = Math.max.apply(null, d) * 1.15, g = '';
      function sx(v) { return L + (v + 0.5) / (K + 1) * (W - L - R); } function sy(v) { return H - B - v / ym * (H - T - B); }
      for (k = 0; k <= K; k++) g += '<rect x="' + n1(sx(k - 0.45)) + '" y="' + n1(sy(d[k])) + '" width="' + n1(sx(0.45) - sx(-0.45)) + '" height="' + n1(H - B - sy(d[k])) + '" fill="' + (k >= P.n ? RD : BL) + '" opacity="' + (k >= P.n ? 0.85 : 0.45) + '"/>';
      g += ln(L, H - B, W - R, H - B, '#999'); nice(0, K, 8).forEach(function (v) { g += tx(sx(v), H - B + 14, v, 9, 'var(--text-muted)'); }); g += tx((L + W - R) / 2, H - 4, '如果只有背景，會觀察到幾個事件', 9.5, 'var(--text-muted)');
      g += ln(sx(P.n - 0.5), T, sx(P.n - 0.5), H - B, RD, 1.5, 'stroke-dasharray="4 3"') + tx(sx(P.n - 0.5) + 4, T + 10, '觀察到 n = ' + P.n, 10, RD, 'start');
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var p = sf(P.n, P.b), z = zOfP(p);
      inf.innerHTML = 'p 值 = P(只靠背景就看到 ≥ ' + P.n + ' 個) = 紅色長條的總面積 = <b>' + sci(p) + '</b>，相當於 <b>' + f2(z) + 'σ</b>。' +
        (z >= 5 ? '<br>超過 5σ：在粒子物理中，可以宣稱「<b>發現</b>」。' : z >= 3 ? '<br>超過 3σ：可以稱為「<b>證據</b>」，但還不能說發現。' : '<br>不到 3σ：很可能只是背景的漲落。') +
        '<br>粗略估計 (n − b)/√b = ' + f2((P.n - P.b) / Math.sqrt(P.b)) + 'σ。' + (P.b < 5 ? '背景很小時，這個常態近似很不準，要用卜瓦松分布精確計算。' : '背景大時，常態近似就不錯了。'); }
    us.forEach(function (u) { u(); });
  }

  /* ---------- 別處效應 ---------- */
  function initLEE(root, cfg) {
    head(root, cfg.q); var P = { nb: 60 }, view = el('div'), inf, last = null;
    var u = slider(root, '搜尋範圍內的質量區間數（「看了幾個地方」）', 5, 120, 5, P.nb, function (x) { return x + ' 個'; }, null, function (x) { P.nb = x; one(); });
    var b = bar(root), b1 = btn('產生一次純背景資料'), b2 = btn('做 2000 次假實驗'); b.appendChild(b1); b.appendChild(b2); root.appendChild(view); inf = info(root);
    var BG = 100;
    function scan(obs) { var best = 0, at = 0; for (var i = 0; i < obs.length - 2; i++) { var n = obs[i] + obs[i + 1] + obs[i + 2], z = n > 3 * BG ? zOfP(sf(n, 3 * BG)) : 0; if (z > best) { best = z; at = i; } } return [best, at]; }
    function one() { var obs = [], E = []; for (var i = 0; i < P.nb; i++) { obs.push(pois(BG)); E.push(i); } E.push(P.nb); var s = scan(obs);
      view.innerHTML = hist(640, 220, E, obs, { xl: '質量（任意單位）', yl: '事件數', ymax: BG * 1.6, band: [[s[1], s[1] + 3, OR]], curves: [{ d: [[0, BG], [P.nb, BG]], c: BL, n: '真正的背景（沒有任何訊號）', dash: '6 4' }] });
      last = s; inf.innerHTML = '這份資料<b>完全沒有訊號</b>。但掃過所有位置後，最大的「峰」（橘色）的局部顯著性是 <b>' + f2(s[0]) + 'σ</b>。<br>按「做 2000 次假實驗」，看看純背景中出現這種峰有多常見。'; }
    function many() { var c3 = 0, c2 = 0, N = 2000; for (var r = 0; r < N; r++) { var obs = []; for (var i = 0; i < P.nb; i++) obs.push(pois(BG)); var z = scan(obs)[0]; if (z >= 3) c3++; if (z >= 2) c2++; }
      var pg = c3 / N; inf.innerHTML = '2000 次純背景的假實驗中：最大局部顯著性 ≥ 2σ 的有 <b>' + Math.round(c2 / N * 100) + '%</b>，≥ 3σ 的有 <b>' + Math.round(pg * 1000) / 10 + '%</b>。' +
        '<br>只看一個位置，≥ 3σ 的機率只有 0.13%；但看了 ' + P.nb + ' 個地方，機率變成約 ' + Math.round(pg * 1000) / 10 + '%。換算成<b>全域顯著性</b>，一個 3σ 的局部峰只相當於約 <b>' + f1(zOfP(Math.max(pg, 1e-6))) + 'σ</b>。' +
        '<br>搜尋範圍越大（滑桿往右），假峰越常見。這就是為什麼要求 5σ，以及為什麼要報告「全域」顯著性。'; }
    b1.onclick = one; b2.onclick = many; u();
  }

  /* ---------- CLs ---------- */
  function initCLs(root, cfg) {
    head(root, cfg.q); var P = { b: 5, n: 5 }, view = el('div'), inf;
    var us = [slider(root, '預期背景 b', 0.5, 30, 0.5, P.b, function (x) { return f1(x); }, null, function (x) { P.b = x; draw(); }),
      slider(root, '實際觀察到的事件數 n', 0, 40, 1, P.n, function (x) { return x; }, null, function (x) { P.n = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function clsb(s) { return cdf(P.n, s + P.b); } function cls(s) { return clsb(s) / cdf(P.n, P.b); }
    function lim(f) { var lo = 0, hi = 200; if (f(0) < 0.05) return 0; for (var i = 0; i < 60; i++) { var m = (lo + hi) / 2; if (f(m) > 0.05) lo = m; else hi = m; } return (lo + hi) / 2; }
    function draw() { var S1 = [], S2 = [], ul = lim(cls), ub = lim(clsb), smax = Math.max(ul * 1.6, 8);
      for (var s = 0; s <= smax; s += smax / 120) { S1.push([s, cls(s)]); S2.push([s, clsb(s)]); }
      view.innerHTML = chart(640, 220, [{ d: S1, c: BL, n: 'CLs' }, { d: S2, c: RD, n: 'CLs+b', dash: '6 4' }], { x0: 0, x1: smax, y0: 0, y1: 1, xl: '假設的訊號事件數 s', hl: [{ y: 0.05, c: GY, n: '0.05' }], vl: [{ x: ul, c: BL, n: 'CLs 上限' }] });
      inf.innerHTML = '觀察到 n = ' + P.n + '、預期背景 b = ' + f1(P.b) + '。95% 信心水準的訊號上限：<b style="color:' + BL + '">CLs：s &lt; ' + f2(ul) + '</b>；<span style="color:' + RD + '">CLs+b：s &lt; ' + f2(ub) + '</span>。' +
        (P.n < P.b ? '<br>觀察到的比背景還少（向下漲落）。CLs+b 會給出一個<b>過分嚴格</b>的上限' + (ub < 0.01 ? '，甚至把 s = 0 也排除了——這顯然不合理。' : '。') + 'CLs 除以 CLb，避免「因為運氣好而排除了自己根本沒有能力看到的訊號」。' : '<br>CLs 永遠比 CLs+b 保守。把 n 調得比 b 小，看看兩者的差別。') +
        '<br>上限乘以截面與亮度的換算，就是論文中「排除某某質量以下的新粒子」的那條線。'; }
    us.forEach(function (u) { u(); });
  }

  /* ---------- 徑跡 ---------- */
  function initTrack(root, cfg) {
    head(root, cfg.q); var P = { p: 5, B: 3.8, q: 1 }, view = el('div', 'max-width:440px;margin:0 auto'), inf;
    var us = [slider(root, '橫向動量 p<sub>T</sub>（GeV）', 0.3, 200, 0.1, P.p, function (x) { return f1(x) + ' GeV'; }, null, function (x) { P.p = x; draw(); }),
      slider(root, '磁場 B（特斯拉）', 0.5, 4, 0.1, P.B, function (x) { return f1(x) + ' T'; }, null, function (x) { P.B = x; draw(); })];
    var b = bar(root), b1 = btn('正電荷', 1), b2 = btn('負電荷', -1); [b1, b2].forEach(function (x) { x.onclick = function () { P.q = +x.getAttribute('data-k'); mark(b, P.q); draw(); }; b.appendChild(x); }); mark(b, 1);
    root.appendChild(view); inf = info(root);
    function draw() { var R = P.p / (0.3 * P.B), S = 160 / 1.2, C = 210, g = '<circle cx="' + C + '" cy="' + C + '" r="' + (1.2 * S) + '" fill="none" stroke="var(--border)" stroke-width="1.5"/>';
      [0.05, 0.1, 0.3, 0.5, 0.8, 1.1].forEach(function (r) { g += '<circle cx="' + C + '" cy="' + C + '" r="' + n1(r * S) + '" fill="none" stroke="var(--border)" stroke-dasharray="3 3"/>'; });
      var d = '', hits = []; for (var t = 0; t <= 1.2; t += 0.004) { var ph = t / R, x = P.q * R * (1 - Math.cos(ph)), y = R * Math.sin(ph); if (Math.sqrt(x * x + y * y) > 1.2 || ph > Math.PI) break; d += (t ? 'L' : 'M') + n1(C + x * S) + ' ' + n1(C - y * S); }
      g += '<path d="' + d + '" fill="none" stroke="' + (P.q > 0 ? RD : BL) + '" stroke-width="2.5"/>' + '<circle cx="' + C + '" cy="' + C + '" r="4" fill="' + OR + '"/>';
      g += tx(C, 2 * C - 4, '⊙ 磁場方向：垂直紙面朝外', 10, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 ' + (2 * C) + ' ' + (2 * C), g);
      var L = 1.1, sag = L * L / (8 * R);
      inf.innerHTML = '曲率半徑 R = p<sub>T</sub> / (0.3 B) = <b>' + (R < 10 ? f2(R) : f1(R)) + ' m</b>。' + (2 * R < 1.2 ? '動量太低，粒子在徑跡偵測器裡<b>繞圈</b>（「捲曲」），出不去。' : '') +
        '<br>在 1.1 公尺長的徑跡中，偏離直線的矢高 s = L²/(8R) ≈ <b>' + (sag * 1000 > 10 ? f1(sag * 1000) : f2(sag * 1000)) + ' mm</b>。' +
        '<br>動量越高，徑跡越直，矢高越小，越難量準：動量的相對誤差大約和 <b>p<sub>T</sub></b> 成正比，和 <b>B·L²</b> 成反比。這就是 CMS 用 3.8 T 強磁場、ATLAS 在外圍再加一套大型環形磁鐵量緲子的原因。'; }
    us.forEach(function (u) { u(); });
  }

  /* ---------- 雙緲子譜 ---------- */
  function initDimu(root, cfg) {
    head(root, cfg.q); var view = el('div'), inf, P = { log: 1 };
    var b = bar(root), b1 = btn('對數座標', 1), b2 = btn('線性座標（只看 2～12 GeV）', 0); [b1, b2].forEach(function (x) { x.onclick = function () { P.log = +x.getAttribute('data-k'); mark(b, P.log); draw(); }; b.appendChild(x); }); mark(b, 1);
    root.appendChild(view); inf = info(root);
    var RES = [['η', 0.548, 0.006, 3], ['ρ/ω', 0.78, 0.012, 3], ['φ', 1.019, 0.008, 2.5], ['J/ψ', 3.097, 0.03, 8], ['ψ(2S)', 3.686, 0.035, 0.4], ['Υ(1S)', 9.46, 0.09, 0.06], ['Υ(2S)', 10.02, 0.1, 0.02], ['Υ(3S)', 10.36, 0.1, 0.012], ['Z', 91.19, 2.4, 0.0015]];
    function cont(m) { return 3.0 * Math.pow(m, -2.6); }
    function f(m) { var v = cont(m); RES.forEach(function (r) { v += r[3] * Math.exp(-0.5 * Math.pow((m - r[1]) / r[2], 2)); }); return v; }
    function draw() { var W = 640, H = 260, L = 52, R = 12, T = 16, B = 34, g = '', xs, ys, pts = [];
      if (P.log) { var a = Math.log10(0.3), z = Math.log10(150); xs = function (m) { return L + (Math.log10(m) - a) / (z - a) * (W - L - R); };
        var yl = -6.5, yh = 2.2; ys = function (v) { return H - B - (Math.log10(Math.max(v, 1e-9)) - yl) / (yh - yl) * (H - T - B); };
        [0.3, 1, 3, 10, 30, 100].forEach(function (m) { g += tx(xs(m), H - B + 14, m, 9, 'var(--text-muted)') + ln(xs(m), T, xs(m), H - B, 'var(--border)', 0.5, 'stroke-dasharray="2 3"'); });
        for (var lm = a; lm <= z; lm += 0.0025) { var m = Math.pow(10, lm), v = f(m) * (1 + 0.06 * randn()); pts.push([xs(m), ys(v)]); } }
      else { xs = function (m) { return L + (m - 2) / 10 * (W - L - R); }; var mx = f(3.097) * 1.1; ys = function (v) { return H - B - v / mx * (H - T - B); };
        [2, 4, 6, 8, 10, 12].forEach(function (m) { g += tx(xs(m), H - B + 14, m, 9, 'var(--text-muted)'); });
        for (var m2 = 2; m2 <= 12; m2 += 0.01) { var v2 = f(m2) * (1 + 0.04 * randn()); pts.push([xs(m2), ys(v2)]); } }
      g += ln(L, H - B, W - R, H - B, '#999') + ln(L, T, L, H - B, '#999') + tx((L + W - R) / 2, H - 4, '兩個緲子的不變質量（GeV）', 9.5, 'var(--text-muted)') + tx(L - 6, T + 4, '事件數', 9.5, 'var(--text-muted)', 'end');
      g += '<path d="' + pts.map(function (p, i) { return (i ? 'L' : 'M') + n1(p[0]) + ' ' + n1(p[1]); }).join('') + '" fill="none" stroke="' + BL + '" stroke-width="1.3"/>';
      RES.forEach(function (r) { if (r[0] === 'Υ(2S)' || r[0] === 'Υ(3S)') return; if (!P.log && (r[1] < 2 || r[1] > 12)) return; var x = xs(r[1]), y = ys(f(r[1])); g += tx(x + (r[0] === 'ψ(2S)' ? 8 : 0), Math.max(T + 8, y - 8), r[0] === 'Υ(1S)' ? 'Υ(1S, 2S, 3S)' : r[0], 10.5, RD); });
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      inf.innerHTML = '把每個事件中兩個緲子的能量與動量，算成「如果它們來自同一個粒子，那個粒子的質量是多少」（不變質量），再畫成直方圖。平滑下降的是背景，每一根<b>尖峰</b>就是一種曾經存在過、衰變成兩個緲子的粒子。' +
        '<br>這張圖幾乎濃縮了半個世紀的粒子物理：φ（1960 年代）、J/ψ（1974 年的十一月革命）、Υ（1977 年，底夸克）、Z（1983 年）。' +
        '<br>（示意圖：形狀依公開的 CMS 雙緲子質譜描繪，不是真實數據。）'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.col-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ bump: initBump, pois: initPois, lee: initLEE, cls: initCLs, track: initTrack, dimu: initDimu })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"💥", COL_NOTE, COLLIB, "col-w")

BUMP = colw({"t": "bump", "q": u"峰值搜尋：在雙光子不變質量中找希格斯"})
POIS = colw({"t": "pois", "q": u"計數實驗：只靠背景，看到這麼多事件的機率有多小？"})
LEE = colw({"t": "lee", "q": u"別處效應：在完全沒有訊號的資料中「找到」新粒子"})
CLS = colw({"t": "cls", "q": u"CLs 方法：沒找到時，能排除多大的訊號？"})
TRACK = colw({"t": "track", "q": u"磁場中的徑跡：從彎曲程度量出動量"})
DIMU = colw({"t": "dimu", "q": u"雙緲子質譜：一張圖看見半世紀的發現"})
