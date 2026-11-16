# -*- coding: utf-8 -*-
"""〈系外行星〉（exo_）共用：課程包裝與 EXOLIB 互動元件（class="exo-w"）。

  transit  凌日光變曲線：行星半徑比、衝擊參數、臨邊昏暗、雜訊 → 光變曲線與深度
  rv       徑向速度：行星質量、週期、離心率、傾角 → 恆星的速度曲線與振幅 K
  hz       可居住帶：恆星類型 → 可居住帶範圍，與已知行星的位置
  bls      找凌日：隱藏的週期與雜訊 → 光變曲線、折疊、BLS 週期圖
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

EXO_NOTE = (u"本課的推導以主要步驟為主；互動模擬為教學用的簡化版本，行星資料為約略值。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def exw(cfg, maxw=680):
    return wdg("exo-w", cfg, maxw)


EXOLIB = r"""
(function () {
  if (window.__exoLib) return; window.__exoLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  var seed = 1; function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
  function randn() { var u = 1 - rnd(), v = rnd(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }

  /* 凌日：數值積分被遮住的亮度（二次臨邊昏暗） */
  function flux(d, p, u1) { var I = function (r) { return 1 - u1 * (1 - Math.sqrt(Math.max(0, 1 - r * r))); }, tot = 0, blk = 0, N = 60;
    for (var i = 0; i < N; i++) { var r = (i + 0.5) / N, w = 2 * Math.PI * r / N * I(r); tot += w;
      if (d + p <= r || r <= d - p) continue; var f; if (r <= p - d) f = 1; else { var c = (r * r + d * d - p * p) / (2 * r * d); f = Math.acos(Math.max(-1, Math.min(1, c))) / Math.PI; } blk += w * f; }
    return 1 - blk / tot; }
  function initTransit(root, cfg) {
    head(root, cfg.q); var P = { p: 0.1, b: 0.2, u: 0.5, nz: 300 }, view = el('div'), view2 = el('div'), inf;
    var bb = bar(root), us; [['木星繞太陽', 0.1], ['海王星', 0.035], ['地球繞太陽', 0.0092], ['地球繞紅矮星', 0.06]].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { P.p = o[1]; us[0](); }; bb.appendChild(x); });
    us = [slider(root, '行星半徑 ÷ 恆星半徑', 0.005, 0.2, 0.0005, P.p, function (x) { return x.toFixed(4); }, null, function (x) { P.p = x; draw(); }),
      slider(root, '衝擊參數 b（0 = 正中央穿過）', 0, 1.1, 0.01, P.b, f2, null, function (x) { P.b = x; draw(); }),
      slider(root, '臨邊昏暗係數', 0, 1, 0.01, P.u, f2, null, function (x) { P.u = x; draw(); }),
      slider(root, '每點的雜訊（ppm，百萬分之一）', 0, 2000, 10, P.nz, function (x) { return x + ' ppm'; }, null, function (x) { P.nz = x; draw(); })];
    root.appendChild(view); root.appendChild(view2); inf = info(root);
    function draw() { seed = 7; var d = [], m = [], mn = 1;
      for (var i = 0; i <= 300; i++) { var t = -1.5 + 3 * i / 300, dd = Math.sqrt(t * t + P.b * P.b), f = flux(dd, P.p, P.u); mn = Math.min(mn, f); m.push([t, (f - 1) * 1e6]); d.push([t, (f - 1) * 1e6 + P.nz * randn()]); }
      var dep = (1 - mn) * 1e6, ylo = -Math.max(dep * 1.4, 3 * P.nz + 50, 200);
      view.innerHTML = chart(640, 230, [{ d: d, c: GY, n: '量到的資料', w: 0.8 }, { d: m, c: BL, n: '模型', w: 2.2 }], { x0: -1.5, x1: 1.5, y0: ylo, y1: Math.max(3 * P.nz + 50, 100), xl: '時間（以凌日的半長為單位）', yl: 'ppm' });
      var g = '<circle cx="100" cy="60" r="50" fill="#f2c14e"/>' + '<circle cx="' + n1(100) + '" cy="' + n1(60 + P.b * 50) + '" r="' + n1(Math.max(1.2, P.p * 50)) + '" fill="#222"/>' + ln(30, 60 + P.b * 50, 170, 60 + P.b * 50, '#666', 1, 'stroke-dasharray="3 3"');
      view2.innerHTML = '<div style="max-width:200px;margin:4px auto">' + svgw('0 0 200 120', g) + '</div>';
      var snr = P.nz ? dep / P.nz * Math.sqrt(60) : Infinity;
      inf.innerHTML = '凌日深度約 <b>' + Math.round(dep) + ' ppm</b>（' + (dep / 1e4).toFixed(3) + '%）；簡單估計 (Rp/R*)² = ' + Math.round(P.p * P.p * 1e6) + ' ppm' + (P.u > 0 ? '，臨邊昏暗讓中央穿過時稍深、邊緣穿過時較淺' : '') + '。' +
        (P.b > 1 + P.p ? '<br><b>沒有凌日</b>：行星從恆星旁邊經過。' : P.b > 1 - P.p ? '<br><b>擦邊凌日</b>：只遮住一部分，曲線呈 V 形。' : '<br>完整凌日：曲線呈平底的 U 形，進出的斜坡長度反映行星的大小。') +
        '<br>在凌日期間約 60 個資料點中，訊雜比約 <b>' + (isFinite(snr) ? f1(snr) : '∞') + '</b>' + (snr < 7 ? '——太低，要疊加好幾次凌日才看得出來。' : '。') +
        '<br>地球繞太陽只有約 84 ppm：從地面幾乎不可能，必須上太空、並疊加多次凌日。'; }
    us.forEach(function (u) { u(); });
  }

  function initRV(root, cfg) {
    head(root, cfg.q); var P = { m: 0.47, P: 4.23, e: 0, i: 90, ms: 1 }, view = el('div'), inf;
    var bb = bar(root), us; [['飛馬座 51 b', [0.47, 4.23, 0]], ['木星', [1, 4333, 0.05]], ['地球', [0.00315, 365.25, 0.017]], ['偏心的熱木星', [3, 20, 0.6]]].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { P.m = o[1][0]; P.P = o[1][1]; P.e = o[1][2]; us.forEach(function (u) { u(); }); }; bb.appendChild(x); });
    us = [slider(root, '行星質量（木星質量）', 0.001, 10, 0.001, P.m, function (x) { return x < 0.03 ? f2(x * 317.8) + ' 地球質量' : f2(x) + ' 木星質量'; }, null, function (x) { P.m = x; draw(); }),
      slider(root, '週期（天）', 1, 5000, 0.01, P.P, function (x) { return f1(x) + ' 天'; }, null, function (x) { P.P = x; draw(); }),
      slider(root, '離心率', 0, 0.9, 0.01, P.e, f2, null, function (x) { P.e = x; draw(); }),
      slider(root, '軌道傾角（90° = 側面看）', 1, 90, 1, P.i, function (x) { return x + '°'; }, null, function (x) { P.i = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var Mj = 1.898e27, Ms = 1.989e30, G = 6.674e-11, Pd = P.P * 86400, mp = P.m * Mj, sini = Math.sin(P.i * Math.PI / 180);
      var K = Math.pow(2 * Math.PI * G / Pd, 1 / 3) * mp * sini / Math.pow(Ms + mp, 2 / 3) / Math.sqrt(1 - P.e * P.e), d = [], w = 1;
      for (var k = 0; k <= 400; k++) { var ph = k / 200, Mn = 2 * Math.PI * ph, E = Mn; for (var it = 0; it < 30; it++) E = E - (E - P.e * Math.sin(E) - Mn) / (1 - P.e * Math.cos(E));
        var nu = 2 * Math.atan2(Math.sqrt(1 + P.e) * Math.sin(E / 2), Math.sqrt(1 - P.e) * Math.cos(E / 2)); d.push([ph, K * (Math.cos(nu + w) + P.e * Math.cos(w))]); }
      var yr = Math.max(K * 1.6, 2);
      view.innerHTML = chart(640, 240, [{ d: d, c: RD, n: '恆星的視線速度（m/s）', w: 2.2 }], { x0: 0, x1: 2, y0: -yr, y1: yr, xl: '相位（兩個週期）', hl: yr <= 15 ? [{ y: 1, c: GN, n: 'HARPS 約 1 m/s' }, { y: 0.1, c: OR, n: 'ESPRESSO 目標 0.1 m/s' }] : [] });
      inf.innerHTML = '恆星被行星拉著繞共同質心擺動，速度振幅 <b>K ≈ ' + (K < 1 ? K.toFixed(2) : f1(K)) + ' m/s</b>' + (K > 1 ? '（約 ' + f1(K * 3.6) + ' 公里／小時）' : '') + '。' +
        (P.e > 0.2 ? '<br>離心軌道：曲線不再是正弦波，在近星點附近急遽變化。' : '') +
        (P.i < 90 ? '<br>傾角 ' + P.i + '° 時只量到 sin i = ' + f2(sini) + ' 的分量——徑向速度法量到的是 <b>m sin i</b>，只是質量的下限。' : '') +
        '<br>' + (K < 0.1 ? '<b>目前的儀器還量不到</b>（地球讓太陽擺動只有約 9 公分／秒）。' : K < 1 ? '需要最頂尖的光譜儀，且恆星本身的活動雜訊常常比訊號還大。' : '現代的光譜儀可以量到。'); }
    us.forEach(function (u) { u(); });
  }

  var STARS = { G: { n: '太陽型（G2，5780 K）', L: 1, T: 5780 }, K: { n: '橙矮星（K5，4400 K）', L: 0.16, T: 4400 }, M: { n: '紅矮星（M5，3100 K）', L: 0.005, T: 3100 }, F: { n: '較熱的 F 型（6500 K）', L: 3, T: 6500 } };
  var PL = { G: [['金星', 0.72], ['地球', 1], ['火星', 1.52]], K: [['克卜勒 442 b', 0.41]], M: [['比鄰星 b', 0.049], ['TRAPPIST-1 d', 0.022], ['TRAPPIST-1 e', 0.029], ['TRAPPIST-1 f', 0.038], ['TRAPPIST-1 g', 0.047]], F: [] };
  function initHZ(root, cfg) {
    head(root, cfg.q); var P = { s: 'G' }, view = el('div'), inf;
    var b = bar(root); ['F', 'G', 'K', 'M'].forEach(function (k) { var x = btn(STARS[k].n, k); x.onclick = function () { P.s = k; mark(b, k); draw(); }; b.appendChild(x); }); mark(b, 'G');
    root.appendChild(view); inf = info(root);
    function draw() { var S = STARS[P.s], tS = S.T - 5780, seff = function (s0, a, bb) { return s0 + a * tS + bb * tS * tS; };
      var inner = Math.sqrt(S.L / seff(1.107, 1.332e-4, 1.58e-8)), outer = Math.sqrt(S.L / seff(0.356, 6.171e-5, 1.698e-9));
      var amax = outer * 2.2, W = 640, H = 170, sx = function (a) { return 40 + a / amax * (W - 70); }, g = '';
      g += '<rect x="' + n1(sx(inner)) + '" y="40" width="' + n1(sx(outer) - sx(inner)) + '" height="90" fill="' + GN + '" opacity="0.25"/>';
      var col = S.T > 6000 ? '#f8f4e8' : S.T > 5000 ? '#f6d860' : S.T > 4000 ? '#f0a040' : '#e06040'; g += '<circle cx="40" cy="85" r="16" fill="' + col + '" stroke="#b08030"/>';
      g += ln(40, 85, W - 20, 85, GY, 1) + tx(n1((sx(inner) + sx(outer)) / 2), 34, '可居住帶', 12, GN);
      (PL[P.s] || []).forEach(function (p, i) { var x = sx(p[1]); g += '<circle cx="' + n1(x) + '" cy="85" r="5" fill="' + BL + '"/>' + tx(x, 112 + (i % 2) * 14, p[0], 10); });
      [0.25, 0.5, 1, 2, 4].forEach(function (a) { if (a < amax) g += ln(sx(a), 140, sx(a), 146, '#888') + tx(sx(a), 158, a + ' AU', 9, 'var(--text-muted)'); });
      [0.01, 0.02, 0.05, 0.1].forEach(function (a) { if (amax < 0.3 && a < amax) g += ln(sx(a), 140, sx(a), 146, '#888') + tx(sx(a), 158, a + ' AU', 9, 'var(--text-muted)'); });
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var Pyr = Math.sqrt(Math.pow((inner + outer) / 2, 3) / Math.pow(S.L, 0.5 * 1) * 1) ;
      inf.innerHTML = S.n + '：亮度約為太陽的 ' + S.L + ' 倍。可居住帶約在 <b>' + inner.toFixed(inner < 0.1 ? 3 : 2) + ' 到 ' + outer.toFixed(outer < 0.1 ? 3 : 2) + ' 天文單位</b>之間（保守估計，依 Kopparapu 等人的公式）。' +
        '<br>距離約與 √L 成正比：恆星越暗，可居住帶越近。' + (P.s === 'M' ? '<br>紅矮星的可居住帶近到行星幾乎一定會被<b>潮汐鎖定</b>（一面永遠白天），而且恆星常有強烈的閃焰——這對生命是好是壞，仍有爭論。好處是：行星近、凌日深、週期短，最容易被我們找到與研究。' : ''); }
    draw();
  }

  function initBLS(root, cfg) {
    head(root, cfg.q); var P = { dep: 700, nz: 500, per: 3.7 }, view = el('div'), view2 = el('div'), view3 = el('div'), inf;
    var us = [slider(root, '凌日深度（ppm）', 50, 2000, 10, P.dep, function (x) { return x + ' ppm'; }, null, function (x) { P.dep = x; draw(); }),
      slider(root, '每點雜訊（ppm）', 100, 3000, 10, P.nz, function (x) { return x + ' ppm'; }, null, function (x) { P.nz = x; draw(); }),
      slider(root, '真正的週期（天）', 1, 9, 0.01, P.per, function (x) { return f2(x) + ' 天'; }, null, function (x) { P.per = x; draw(); })];
    root.appendChild(view); root.appendChild(view2); root.appendChild(view3); inf = info(root);
    function draw() { seed = 11; var N = 1300, T = 27, t = [], f = [], dur = 0.12;
      for (var i = 0; i < N; i++) { var ti = i * T / N, ph = ((ti - 0.6) % P.per + P.per) % P.per, inT = ph < dur || ph > P.per - 0 && false; t.push(ti); f.push(-(ph < dur ? P.dep : 0) + P.nz * randn()); }
      var best = { p: 0, s: -1 }, pg = [];
      for (var pp = 0.8; pp <= 10; pp += 0.004) { var nb = Math.max(20, Math.round(pp / dur)), sum = new Array(nb).fill(0), cnt = new Array(nb).fill(0);
        for (i = 0; i < N; i++) { var k = Math.floor(((t[i] % pp) / pp) * nb); sum[k] += f[i]; cnt[k]++; }
        var tot = 0; for (k = 0; k < nb; k++) tot += sum[k]; var mean = tot / N, smax = 0;
        for (k = 0; k < nb; k++) if (cnt[k] > 3) { var dlt = mean - sum[k] / cnt[k], s = dlt * Math.sqrt(cnt[k]); if (s > smax) smax = s; }
        pg.push([pp, smax]); if (smax > best.s) best = { p: pp, s: smax }; }
      view.innerHTML = chart(640, 170, [{ d: t.map(function (v, i) { return [v, f[i]]; }), c: GY, n: '光變曲線（27 天，像 TESS 的一個區段）', w: 0.6 }], { x0: 0, x1: 27, y0: -P.dep - 3 * P.nz, y1: 3 * P.nz, xl: '時間（天）', yl: 'ppm' });
      var bins = 80, bs = new Array(bins).fill(0), bc = new Array(bins).fill(0); for (i = 0; i < N; i++) { var b2 = Math.floor(((t[i] - 0.6 + 0.3 * best.p) % best.p + best.p) % best.p / best.p * bins); bs[b2] += f[i]; bc[b2]++; }
      var fd = []; for (i = 0; i < bins; i++) if (bc[i]) fd.push([i / bins, bs[i] / bc[i]]);
      view2.innerHTML = chart(640, 200, [{ d: pg, c: BL, n: 'BLS 週期圖（訊號強度）', w: 1.2 }], { x0: 0.8, x1: 10, xl: '試驗的週期（天）', vl: [{ x: P.per, c: GN, n: '真正的週期' }], pts: [{ x: best.p, y: best.s, c: RD, n: '最高峰 ' + f2(best.p) + ' 天' }] });
      view3.innerHTML = chart(640, 170, [{ d: fd, c: OR, n: '用最高峰的週期折疊、分組平均', w: 2 }], { x0: 0, x1: 1, xl: '相位', yl: 'ppm' });
      var ok = Math.abs(best.p - P.per) < 0.03 || Math.abs(best.p - P.per / 2) < 0.02 || Math.abs(best.p - 2 * P.per) < 0.05;
      inf.innerHTML = '每個凌日的深度只有雜訊的 ' + f2(P.dep / P.nz) + ' 倍——在原始資料中幾乎看不見。' +
        '<br>BLS 演算法試遍每一個可能的週期，把資料折疊起來，找出「一段比平均低的方塊」。最高峰在 <b>' + f2(best.p) + ' 天</b>：' + (ok ? (Math.abs(best.p - P.per) < 0.03 ? '<b>找到了</b>真正的週期。' : '找到的是真正週期的<b>倍數或一半</b>——實務上要再檢查。') : '<b>沒找到</b>：訊號太弱，最高峰只是雜訊。') +
        '<br>折疊之後，許多次凌日疊在一起，雜訊被平均掉，凌日就浮現出來了。'; }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.exo-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ transit: initTransit, rv: initRV, hz: initHZ, bls: initBLS })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🪐", EXO_NOTE, EXOLIB, "exo-w")

TRANSIT = exw({"t": "transit", "q": u"凌日：行星從恆星前面經過時，星光暗了多少"})
RVW = exw({"t": "rv", "q": u"徑向速度：行星拉著恆星擺動"})
HZW = exw({"t": "hz", "q": u"可居住帶：哪裡的溫度能讓水保持液態"})
BLSW = exw({"t": "bls", "q": u"從雜訊中找凌日：BLS 週期搜尋"})
