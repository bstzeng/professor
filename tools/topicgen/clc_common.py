# -*- coding: utf-8 -*-
"""〈微積分：直覺與應用〉（clc_）共用：課程包裝與 CLCLIB 互動元件（class="clc-w"）。

  tangent  割線趨近切線：導數的定義
  riemann  黎曼和：用長方形逼近面積
  fence    最佳化：圍籬問題
  slope    斜率場與微分方程的解
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

CLC_NOTE = u"互動圖形以數值方法即時計算，用來建立直覺；嚴謹的推導請見〈數學公式是怎麼推導出來的〉。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def kw(cfg, maxw=680):
    return wdg("clc-w", cfg, maxw)


CLCLIB = r"""
(function () {
  if (window.__clcLib) return; window.__clcLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  var FN = [['x²', function (x) { return x * x; }, function (x) { return 2 * x; }, -2.5, 2.5, -1, 6, 'f′(x) = 2x'],
    ['x³ − 3x', function (x) { return x * x * x - 3 * x; }, function (x) { return 3 * x * x - 3; }, -2.5, 2.5, -4, 4, 'f′(x) = 3x² − 3'],
    ['sin x', Math.sin, Math.cos, -4, 4, -1.5, 1.5, 'f′(x) = cos x'],
    ['eˣ', Math.exp, Math.exp, -2.5, 2, -0.5, 7, 'f′(x) = eˣ']];

  function initTangent(root, cfg) {
    head(root, cfg.q); var P = { f: 0, x: 1, h: 1 }, view = el('div'), inf;
    var b = bar(root); FN.forEach(function (o, i) { var x = btn(o[0], i); x.onclick = function () { P.f = i; mark(b, i); draw(); }; b.appendChild(x); }); mark(b, 0);
    var us = [slider(root, '切點 x₀', -2, 2, 0.05, P.x, function (x) { return f2(x); }, null, function (x) { P.x = x; draw(); }),
      slider(root, '間距 h（拉到接近 0）', 0.01, 1.5, 0.01, P.h, function (x) { return f2(x); }, null, function (x) { P.h = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var F = FN[P.f], f = F[1], x0 = P.x, h = P.h, y0 = f(x0), x1 = x0 + h, y1 = f(x1), sec = (y1 - y0) / h, tan = F[2](x0), d = [], s = [], t = [];
      for (var x = F[3]; x <= F[4] + 1e-9; x += (F[4] - F[3]) / 200) { d.push([x, f(x)]); s.push([x, y0 + sec * (x - x0)]); t.push([x, y0 + tan * (x - x0)]); }
      view.innerHTML = chart(640, 280, [{ d: d, c: BL, n: 'y = ' + F[0], w: 2.4 }, { d: s, c: OR, n: '割線（斜率 ' + f2(sec) + '）', w: 1.8 }, { d: t, c: RD, n: '切線（斜率 ' + f2(tan) + '）', w: 1.4, dash: '5,4' }],
        { x0: F[3], x1: F[4], y0: F[5], y1: F[6], pts: [{ x: x0, y: y0, c: RD }, { x: x1, y: y1, c: OR }] });
      inf.innerHTML = '割線斜率 = [f(x₀+h) − f(x₀)] / h = <b>' + f2(sec) + '</b>；切線斜率（導數）f′(' + f2(x0) + ') = <b>' + f2(tan) + '</b>，差距 ' + f2(Math.abs(sec - tan)) + '。' +
        '<br>把 h 往 0 拉，橘色的割線會轉向、貼上紅色的切線——<b>導數就是 h → 0 時割線斜率的極限</b>。這個函數的導數：' + F[7] + '。'; }
    us.forEach(function (u) { u(); });
  }

  var RF = [['x²（0 到 2）', function (x) { return x * x; }, 0, 2, 8 / 3, '8/3'], ['sin x（0 到 π）', Math.sin, 0, Math.PI, 2, '2'], ['1/x（1 到 e）', function (x) { return 1 / x; }, 1, Math.E, 1, '1'], ['eˣ（0 到 1）', Math.exp, 0, 1, Math.E - 1, 'e − 1']];
  function initRiemann(root, cfg) {
    head(root, cfg.q); var P = { f: 0, n: 6, m: 0 }, view = el('div'), inf;
    var b = bar(root); RF.forEach(function (o, i) { var x = btn(o[0], i); x.onclick = function () { P.f = i; mark(b, i); draw(); }; b.appendChild(x); }); mark(b, 0);
    var b2 = bar(root); [['左端點', 0], ['右端點', 1], ['中點', 2]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.m = o[1]; mark(b2, o[1]); draw(); }; b2.appendChild(x); }); mark(b2, 0);
    var us = [slider(root, '長方形個數 n', 1, 100, 1, P.n, function (x) { return x; }, null, function (x) { P.n = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var F = RF[P.f], f = F[1], a = F[2], bb = F[3], n = P.n, w = (bb - a) / n, S = 0, ymax = 0, W = 640, H = 260, L = 40, R = 14, T = 14, B = 26, g = '';
      for (var x = a; x <= bb; x += (bb - a) / 200) ymax = Math.max(ymax, f(x)); ymax *= 1.1;
      function sx(x) { return L + (x - a) / (bb - a) * (W - L - R); } function sy(y) { return H - B - y / ymax * (H - T - B); }
      for (var i = 0; i < n; i++) { var xl = a + i * w, xs = P.m == 0 ? xl : P.m == 1 ? xl + w : xl + w / 2, y = f(xs); S += y * w;
        g += '<rect x="' + n1(sx(xl)) + '" y="' + n1(sy(y)) + '" width="' + n1(sx(xl + w) - sx(xl)) + '" height="' + n1(sy(0) - sy(y)) + '" fill="' + OR + '" fill-opacity="0.35" stroke="' + OR + '" stroke-width="' + (n > 60 ? 0.3 : 0.8) + '"/>'; }
      var d = ''; for (var k = 0; k <= 200; k++) { var xx = a + (bb - a) * k / 200; d += (k ? 'L' : 'M') + n1(sx(xx)) + ' ' + n1(sy(f(xx))); }
      g += '<path d="' + d + '" fill="none" stroke="' + BL + '" stroke-width="2.4"/>' + ln(L, sy(0), W - R, sy(0), '#999') + ln(L, T, L, sy(0), '#999') + tx(sx(a), H - 8, f2(a), 9, 'var(--text-muted)') + tx(sx(bb), H - 8, f2(bb), 9, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 640 260', g);
      var err = S - F[4];
      inf.innerHTML = n + ' 個長方形的面積總和 = <b>' + (Math.round(S * 10000) / 10000) + '</b>；真正的面積（積分）= ' + F[5] + ' ≈ <b>' + (Math.round(F[4] * 10000) / 10000) + '</b>，誤差 ' + (Math.abs(err) < 1e-4 ? '< 0.0001' : (err > 0 ? '+' : '') + (Math.round(err * 10000) / 10000)) + '。' +
        '<br>長方形越多、越窄，總和就越接近真正的面積——<b>積分就是 n → ∞ 時黎曼和的極限</b>。比較三種取點方法：中點法的誤差通常小得多。'; }
    us.forEach(function (u) { u(); });
  }

  function initFence(root, cfg) {
    head(root, cfg.q); var P = { x: 15, wall: 1 }, view = el('div'), cv = el('div'), inf, Lf = 100;
    var b = bar(root), wb = btn('一邊靠牆：是'); wb.onclick = function () { P.wall ^= 1; wb.textContent = '一邊靠牆：' + (P.wall ? '是' : '否'); draw(); }; b.appendChild(wb);
    var us = [slider(root, '寬度 x（與牆垂直的邊）', 1, 49, 0.5, P.x, function (x) { return f1(x) + ' 公尺'; }, null, function (x) { P.x = x; draw(); })];
    root.appendChild(view); root.appendChild(cv); inf = info(root);
    function A(x) { return P.wall ? x * (Lf - 2 * x) : x * (Lf / 2 - x); }
    function draw() { var x = P.x, len = P.wall ? Lf - 2 * x : Lf / 2 - x, xo = P.wall ? Lf / 4 : Lf / 4, ok = len > 0, sc = 3.2, g = '';
      if (P.wall) g += '<rect x="20" y="20" width="600" height="10" fill="#999"/>' + tx(320, 16, '牆', 10, '#666');
      if (ok) g += '<rect x="' + n1(320 - len * sc / 2) + '" y="30" width="' + n1(len * sc) + '" height="' + n1(x * sc) + '" fill="#cfe8cf" stroke="' + GN + '" stroke-width="2" ' + (P.wall ? 'stroke-dasharray="0"' : '') + '/>' + tx(320, 30 + x * sc / 2 + 4, '面積 ' + Math.round(A(x)) + ' m²', 12) + tx(320, 30 + x * sc + 14, n1(len) + ' m', 10) + tx(320 - len * sc / 2 - 6, 30 + x * sc / 2, n1(x) + ' m', 10, 'currentColor', 'end');
      view.innerHTML = svgw('0 0 640 210', g);
      var d = []; for (var t = 0.5; t <= (P.wall ? 49.5 : 49.5); t += 0.5) d.push([t, Math.max(A(t), 0)]);
      cv.innerHTML = chart(640, 180, [{ d: d, c: BL, n: '面積 A(x)', w: 2.2 }], { x0: 0, x1: 50, y0: 0, xl: '寬度 x（公尺）', vl: [{ x: xo, c: RD, n: '最大值' }], pts: [{ x: x, y: Math.max(A(x), 0), c: RD }] });
      inf.innerHTML = '用 100 公尺的圍籬圍出長方形' + (P.wall ? '（一邊靠牆，不用圍）：A(x) = x(100 − 2x)，A′(x) = 100 − 4x = 0 → x = <b>25</b>，最大面積 <b>1,250 m²</b>。' : '（四邊都要圍）：A(x) = x(50 − x)，A′(x) = 50 − 2x = 0 → x = <b>25</b>，是正方形，最大面積 <b>625 m²</b>。') +
        '<br>在最大值的地方，曲線的切線是<b>水平</b>的——導數等於零。這是用微積分做最佳化的核心想法。'; }
    us.forEach(function (u) { u(); });
  }

  var ODE = [['dy/dt = 0.5y（成長）', function (t, y) { return 0.5 * y; }, 0, 6, -1, 10, 1, 'y = y₀e<sup>0.5t</sup>：成長的速度與目前的大小成正比，越長越快。'],
    ['dy/dt = −0.5y（衰減）', function (t, y) { return -0.5 * y; }, 0, 6, -1, 6, 5, 'y = y₀e<sup>−0.5t</sup>：放射性衰變、藥物代謝。不論從哪裡出發，都以相同的「半衰期」減半。'],
    ['dy/dt = y(1 − y/8)（邏輯斯諦）', function (t, y) { return y * (1 - y / 8); }, 0, 10, -1, 10, 0.5, '族群成長受到環境的限制：一開始像指數成長，接近承載量 8 時慢下來，形成 S 形曲線。'],
    ['dy/dt = −0.3(y − 20)（冷卻）', function (t, y) { return -0.3 * (y - 20); }, 0, 15, 0, 100, 90, '牛頓冷卻定律：一杯 90 °C 的咖啡放在 20 °C 的房間，溫度與室溫的差距以指數方式縮小。']];
  function initSlope(root, cfg) {
    head(root, cfg.q); var P = { k: 0, y0: 1 }, view = el('div'), inf, us;
    var b = bar(root); ODE.forEach(function (o, i) { var x = btn(o[0], i); x.onclick = function () { P.k = i; mark(b, i); P.y0 = o[6]; rebuild(); }; b.appendChild(x); }); mark(b, 0);
    var sw = el('div'); root.appendChild(sw); root.appendChild(view); inf = info(root);
    function rebuild() { sw.innerHTML = ''; var E = ODE[P.k]; var u = slider(sw, '初始值 y(0)', E[4] < 0 ? 0 : E[4], E[5], (E[5] - E[4]) / 100, P.y0, function (x) { return f1(x); }, null, function (x) { P.y0 = x; draw(); }); u(); }
    function draw() { var E = ODE[P.k], f = E[1], t0 = E[2], t1 = E[3], ya = E[4], yb = E[5], W = 640, H = 300, L = 40, R = 14, T = 12, B = 26, g = '';
      function sx(t) { return L + (t - t0) / (t1 - t0) * (W - L - R); } function sy(y) { return H - B - (y - ya) / (yb - ya) * (H - T - B); }
      for (var i = 0; i <= 20; i++) for (var j = 0; j <= 14; j++) { var t = t0 + (t1 - t0) * i / 20, y = ya + (yb - ya) * j / 14, s = f(t, y), dx = (t1 - t0) / 20 * 0.35, dy = s * dx, px = sx(t + dx) - sx(t), py = sy(y + dy) - sy(y), nn = Math.hypot(px, py) || 1, l = 9;
        g += ln(sx(t) - px / nn * l, sy(y) - py / nn * l, sx(t) + px / nn * l, sy(y) + py / nn * l, GY, 1.2); }
      var y = P.y0, t2 = t0, dt = (t1 - t0) / 400, d = 'M' + n1(sx(t2)) + ' ' + n1(sy(y));
      for (var k = 0; k < 400; k++) { var k1 = f(t2, y), k2 = f(t2 + dt / 2, y + dt / 2 * k1), k3 = f(t2 + dt / 2, y + dt / 2 * k2), k4 = f(t2 + dt, y + dt * k3); y += dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4); t2 += dt; if (y > yb * 3 || y < ya - (yb - ya)) break; d += 'L' + n1(sx(t2)) + ' ' + n1(sy(y)); }
      g += '<clipPath id="slc"><rect x="' + L + '" y="' + T + '" width="' + (W - L - R) + '" height="' + (H - T - B) + '"/></clipPath><path clip-path="url(#slc)" d="' + d + '" fill="none" stroke="' + RD + '" stroke-width="2.6"/>';
      g += ln(L, H - B, W - R, H - B, '#999') + ln(L, T, L, H - B, '#999') + tx(W - R, H - 8, 't = ' + t1, 9, 'var(--text-muted)', 'end') + tx(L - 4, T + 8, yb, 9, 'var(--text-muted)', 'end') + tx(L - 4, H - B, ya, 9, 'var(--text-muted)', 'end');
      view.innerHTML = svgw('0 0 640 300', g);
      inf.innerHTML = '每一個灰色的小線段，標出那一點應有的<b>斜率</b>（微分方程告訴我們的）。紅色的解曲線，就是處處「順著」這些斜率走的曲線。<br>' + E[7]; }
    rebuild();
  }

  function initAll() { document.querySelectorAll('.clc-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ tangent: initTangent, riemann: initRiemann, fence: initFence, slope: initSlope })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"📈", CLC_NOTE, CLCLIB, "clc-w")

TANGENT = kw({"t": "tangent", "q": u"從割線到切線：導數是怎麼來的"})
RIEMANN = kw({"t": "riemann", "q": u"黎曼和：用長方形逼近曲線下的面積"})
FENCE = kw({"t": "fence", "q": u"圍籬問題：100 公尺的圍籬，怎麼圍出最大的面積"})
SLOPE = kw({"t": "slope", "q": u"斜率場：微分方程畫出的「流向圖」"})
