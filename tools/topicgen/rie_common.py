# -*- coding: utf-8 -*-
"""〈質數與黎曼猜想〉（rie_）共用：課程包裝與 RIELIB 互動元件（class="rie-w"）。

  sieve     埃拉托斯特尼篩法：篩到第幾個質數 → 1～200 的方格
  pix       質數計數：x → π(x)、x/ln x、Li(x) 與比值
  zline     臨界線：t 的範圍 → 哈代 Z 函數（|ζ(½+it)| 帶正負號）與零點
  explicit  顯式公式：零點個數 → 用零點重建的 ψ(x) 階梯
  spacing   零點間距：零點數量 → 正規化間距的直方圖，與 GUE、卜瓦松比較
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

RIE_NOTE = (u"本課的推導以主要步驟與直覺為主，省略部分嚴格的證明；互動模擬中的 ζ 零點以歐拉—麥克勞林公式與黎曼—席格公式即時計算，為數值近似。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def riw(cfg, maxw=680):
    return wdg("rie-w", cfg, maxw)


RIELIB = r"""
(function () {
  if (window.__rieLib) return; window.__rieLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  var PR = (function () { var N = 1100000, s = new Uint8Array(N + 1), p = []; for (var i = 2; i <= N; i++) { if (!s[i]) { p.push(i); for (var j = i * i; j <= N; j += i) s[j] = 1; } } return p; })();
  function piOf(x) { var lo = 0, hi = PR.length; while (lo < hi) { var m = (lo + hi) >> 1; if (PR[m] <= x) lo = m + 1; else hi = m; } return lo; }
  function Li(x) { if (x < 2) return 0; var s = 0, N = 2000, a = Math.log(2), b = Math.log(x); for (var i = 0; i < N; i++) { var u = a + (i + 0.5) * (b - a) / N; s += Math.exp(u) / u; } return s * (b - a) / N + 1.045; }
  function theta(t) { return t / 2 * Math.log(t / (2 * Math.PI)) - t / 2 - Math.PI / 8 + 1 / (48 * t) + 7 / (5760 * t * t * t); }
  function zem(t) { var N = Math.max(30, Math.ceil(t / 2)), re = 0, im = 0, n, l, m; for (n = 1; n < N; n++) { l = Math.log(n); m = Math.exp(-0.5 * l); re += m * Math.cos(t * l); im -= m * Math.sin(t * l); }
    var lN = Math.log(N), mN = Math.exp(-0.5 * lN), cr = Math.cos(t * lN), ci = -Math.sin(t * lN), ar = N * mN * cr, ai = N * mN * ci, den = 0.25 + t * t;
    re += (-0.5 * ar + ai * t) / den; im += (-0.5 * ai - ar * t) / den; re += mN * cr / 2; im += mN * ci / 2;
    var B = [1 / 6, -1 / 30, 1 / 42, -1 / 30, 5 / 66, -691 / 2730, 7 / 6], fact = 1, pr = 0.5, pi = t, tr = mN * cr / N, ti = mN * ci / N;
    for (var k = 1; k <= 7; k++) { if (k > 1) [2 * k - 3, 2 * k - 2].forEach(function (j) { var xr = 0.5 + j, nr = pr * xr - pi * t, ni = pr * t + pi * xr; pr = nr; pi = ni; });
      fact *= (2 * k) * (2 * k - 1); var c = B[k - 1] / fact; re += c * (pr * tr - pi * ti); im += c * (pr * ti + pi * tr); tr /= N * N; ti /= N * N; }
    var th = theta(t); return re * Math.cos(th) - im * Math.sin(th); }
  function Z(t) { if (t < 300) return zem(t); var a = Math.sqrt(t / (2 * Math.PI)), N = Math.floor(a), th = theta(t), s = 0; for (var n = 1; n <= N; n++) s += Math.cos(th - t * Math.log(n)) / Math.sqrt(n);
    var p = a - N, c0 = Math.cos(2 * Math.PI * (p * p - p - 1 / 16)) / Math.cos(2 * Math.PI * p); return 2 * s + (N % 2 ? 1 : -1) * Math.pow(t / (2 * Math.PI), -0.25) * c0; }
  var ZEROS = null; function zeros(tmax) { if (ZEROS && ZEROS.tmax >= tmax) return ZEROS.z; var z = [], h = 0.02, prev = Z(10), t;
    for (t = 10 + h; t < tmax; t += h) { var v = Z(t); if (v * prev < 0) { var a = t - h, b = t, fa = prev; for (var k = 0; k < 30; k++) { var m = (a + b) / 2, fm = Z(m); if (fm * fa < 0) b = m; else { a = m; fa = fm; } } z.push((a + b) / 2); } prev = v; }
    ZEROS = { tmax: tmax, z: z }; return z; }

  function initSieve(root, cfg) {
    head(root, cfg.q); var P = { k: 0 }, view = el('div'), inf, PS = [2, 3, 5, 7, 11, 13];
    var u = slider(root, '已經用來篩的質數', 0, 6, 1, P.k, function (x) { return x ? PS.slice(0, x).join('、') : '還沒開始'; }, null, function (x) { P.k = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var g = '', cols = 20, cw = 31, killed = 0, left = 0; for (var n = 1; n <= 200; n++) { var x = ((n - 1) % cols) * cw + 6, y = Math.floor((n - 1) / cols) * 26 + 4, by = null;
        for (var i = 0; i < P.k; i++) if (n !== PS[i] && n % PS[i] === 0) { by = i; break; }
        var isP = n > 1 && by === null, col = n === 1 ? GY : by !== null ? '#e4e7eb' : P.k >= 4 || PS.slice(0, P.k).indexOf(n) >= 0 ? GN : '#fff';
        if (by !== null) killed++; else if (n > 1) left++;
        g += '<rect x="' + x + '" y="' + y + '" width="' + (cw - 3) + '" height="22" rx="3" fill="' + col + '" stroke="#ccd"/>' + tx(x + (cw - 3) / 2, y + 15, n, 10, by !== null ? '#aab' : '#223'); }
      view.innerHTML = svgw('0 0 630 270', g);
      inf.innerHTML = (P.k ? '用 ' + PS.slice(0, P.k).join('、') + ' 劃掉它們的倍數。' : '從 2 開始：它是質數，劃掉它所有的倍數；下一個沒被劃掉的數就是下一個質數。') + '剩下 <b>' + left + '</b> 個數。' +
        (P.k >= 4 ? '<br>篩到 7 就夠了：√200 ≈ 14.1，而 11、13 的倍數中，比 200 小的合數早就被更小的質數劃掉了。剩下的 <b>46</b> 個數全是質數。' : ''); }
    u();
  }

  function initPix(root, cfg) {
    head(root, cfg.q); var P = { l: 3 }, view = el('div'), inf;
    var u = slider(root, 'x（以 10 為底的對數）', 1, 6, 0.01, P.l, function (x) { return Math.round(Math.pow(10, x)).toLocaleString(); }, null, function (x) { P.l = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var X = Math.pow(10, P.l), a = [], b = [], c = [], step = X / 300;
      for (var x = 2; x <= X; x += step) { a.push([x, piOf(x)]); b.push([x, x / Math.log(x)]); c.push([x, Li(x)]); }
      var pi = piOf(X), xl = X / Math.log(X), li = Li(X);
      view.innerHTML = chart(640, 250, [{ d: a, c: BL, n: 'π(x)：質數的個數', w: 2.2 }, { d: b, c: OR, n: 'x / ln x', w: 1.6, dash: '5,4' }, { d: c, c: RD, n: 'Li(x)', w: 1.6, dash: '2,3' }], { x0: 0, x1: X, xl: 'x' });
      inf.innerHTML = 'x = ' + Math.round(X).toLocaleString() + '：π(x) = <b>' + pi.toLocaleString() + '</b>，x/ln x ≈ ' + Math.round(xl).toLocaleString() + '（比值 ' + (pi / xl).toFixed(3) + '），Li(x) ≈ ' + Math.round(li).toLocaleString() + '（差 ' + Math.round(li - pi) + '）。' +
        '<br>比值 π(x)/(x/ln x) 慢慢趨近 1——這就是<b>質數定理</b>。Li(x) 近似得好得多：誤差只有約 √x 的量級，黎曼猜想就是在說這件事。'; }
    u();
  }

  function initZline(root, cfg) {
    head(root, cfg.q); var P = { t0: 0 }, view = el('div'), inf;
    var u = slider(root, '起點 t', 0, 900, 1, P.t0, function (x) { return x; }, null, function (x) { P.t0 = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var t0 = Math.max(10, P.t0), t1 = t0 + 60, d = [], z = zeros(t1).filter(function (v) { return v >= t0 && v <= t1; }), mx = 0;
      for (var t = t0; t <= t1; t += 0.05) { var v = Z(t); d.push([t, v]); mx = Math.max(mx, Math.abs(v)); }
      view.innerHTML = chart(640, 240, [{ d: d, c: BL, n: 'Z(t)：|ζ(½ + it)|，帶正負號', w: 1.6 }], { x0: t0, x1: t1, y0: -mx * 1.1, y1: mx * 1.1, xl: 't（虛部）', hl: [{ y: 0, c: GY, n: '' }], pts: z.map(function (r) { return { x: r, y: 0, c: RD, n: '' }; }) });
      var all = zeros(t1), Nt = function (T) { return T / (2 * Math.PI) * Math.log(T / (2 * Math.PI)) - T / (2 * Math.PI) + 7 / 8; };
      inf.innerHTML = '紅點是 ζ 函數在臨界線上的零點（Z(t) 穿過 0 的地方）。這一段有 <b>' + z.length + '</b> 個；' + (t0 <= 15 ? '第一個在 t ≈ <b>' + all[0].toFixed(4) + '</b>。' : '') +
        '<br>到 t = ' + Math.round(t1) + ' 為止，數到 <b>' + all.length + '</b> 個零點；黎曼—馮・曼戈爾特公式預測約 ' + Math.round(Nt(t1)) + ' 個。' +
        '<br>t 越大，零點越密（平均間距約 2π / ln(t/2π)），曲線的起伏也越大。'; }
    u();
  }

  function initExplicit(root, cfg) {
    head(root, cfg.q); var P = { k: 10 }, view = el('div'), inf;
    var u = slider(root, '使用的零點個數', 0, 100, 1, P.k, function (x) { return x + ' 個'; }, null, function (x) { P.k = x; draw(); });
    root.appendChild(view); inf = info(root);
    var zs = zeros(240); var psi = []; (function () { var s = 0, pts = []; for (var n = 2; n <= 60; n++) { var m = n, p = 0; for (var q = 2; q <= n; q++) { if (m % q === 0) { p = q; while (m % q === 0) m /= q; break; } } if (m === 1 && p) s += Math.log(p); pts.push([n, s]); } psi = pts; })();
    function draw() { var ap = [], st = []; psi.forEach(function (p, i) { st.push([p[0], i ? psi[i - 1][1] : 0]); st.push([p[0], p[1]]); });
      for (var x = 2; x <= 60; x += 0.04) { var s = x - Math.log(2 * Math.PI) - 0.5 * Math.log(1 - 1 / (x * x)), lx = Math.log(x), sq = Math.sqrt(x);
        for (var k = 0; k < Math.min(P.k, zs.length); k++) { var g = zs[k]; s -= 2 * sq * (0.5 * Math.cos(g * lx) + g * Math.sin(g * lx)) / (0.25 + g * g); } ap.push([x, s]); }
      view.innerHTML = chart(640, 260, [{ d: st, c: GY, n: 'ψ(x)：真正的階梯（在每個質數冪跳一階）', w: 2 }, { d: ap, c: RD, n: '用零點重建', w: 1.4 }], { x0: 2, x1: 60, y0: 0, y1: 62, xl: 'x' });
      inf.innerHTML = '黎曼的顯式公式：ψ(x) = x − Σ x^ρ/ρ − ln 2π − ½ ln(1 − x⁻²)。用了 <b>' + P.k + '</b> 個零點（及其共軛）。' +
        (P.k === 0 ? '<br>只有平滑的主項 x：看不到任何質數。' : P.k < 15 ? '<br>每加一個零點，就加上一道波浪。階梯的形狀開始浮現。' : '<br>零點越多，曲線越貼近階梯——在每個質數的位置都出現了跳躍。<b>質數的位置，完全由 ζ 的零點決定</b>。') ; }
    u();
  }

  function initSpacing(root, cfg) {
    head(root, cfg.q); var P = { T: 600 }, view = el('div'), inf;
    var u = slider(root, '計算到 t =', 100, 1500, 50, P.T, function (x) { return x; }, null, function (x) { P.T = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var z = zeros(P.T), sp = []; for (var i = 1; i < z.length; i++) { var m = (z[i] + z[i - 1]) / 2; sp.push((z[i] - z[i - 1]) * Math.log(m / (2 * Math.PI)) / (2 * Math.PI)); }
      var bins = 24, bw = 3 / bins, h = new Array(bins).fill(0); sp.forEach(function (s) { var k = Math.floor(s / bw); if (k >= 0 && k < bins) h[k]++; });
      var hd = []; for (i = 0; i < bins; i++) { var v = h[i] / (sp.length * bw); hd.push([i * bw, v]); hd.push([(i + 1) * bw, v]); }
      var gue = [], poi = []; for (var s = 0; s <= 3; s += 0.02) { gue.push([s, 32 / (Math.PI * Math.PI) * s * s * Math.exp(-4 * s * s / Math.PI)]); poi.push([s, Math.exp(-s)]); }
      view.innerHTML = chart(640, 250, [{ d: hd, c: BL, n: 'ζ 零點的正規化間距', w: 1.8 }, { d: gue, c: RD, n: 'GUE（隨機矩陣）', w: 2 }, { d: poi, c: GY, n: '卜瓦松（完全隨機）', w: 1.6, dash: '5,4' }], { x0: 0, x1: 3, y0: 0, y1: 1.2, xl: '間距（以平均間距為 1）' });
      inf.innerHTML = '用了 <b>' + z.length + '</b> 個零點。如果零點是完全隨機撒下的，間距會像灰色的卜瓦松分布：很小的間距最常見。' +
        '<br>但 ζ 的零點<b>互相排斥</b>：幾乎不會靠得很近，直方圖貼近紅色的 GUE 曲線——那是隨機厄米矩陣的特徵值、也是重原子核能階的間距分布。這是蒙哥馬利與戴森在 1972 年發現的連結。'; }
    u();
  }

  function initAll() { document.querySelectorAll('.rie-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ sieve: initSieve, pix: initPix, zline: initZline, explicit: initExplicit, spacing: initSpacing })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🔢", RIE_NOTE, RIELIB, "rie-w")

SIEVE = riw({"t": "sieve", "q": u"埃拉托斯特尼篩法：把合數一層層篩掉"})
PIX = riw({"t": "pix", "q": u"質數有多少：π(x) 與它的近似"})
ZLINE = riw({"t": "zline", "q": u"臨界線上的 ζ 函數與它的零點"})
EXPLICIT = riw({"t": "explicit", "q": u"零點就是質數的音樂：用 ζ 的零點重建質數階梯"})
SPACING = riw({"t": "spacing", "q": u"零點之間的距離：和隨機矩陣一模一樣"})
