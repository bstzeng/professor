# -*- coding: utf-8 -*-
"""〈黑洞〉（bhl_）共用：課程包裝與 BHLLIB 互動元件（class="bhl-w"）。

  rays    光線彎曲：衝擊參數 → 史瓦西黑洞旁的光線軌跡、光子球與陰影
  veff    有效位能：角動量 → 有效位能曲線、穩定與不穩定圓軌道、ISCO
  tidal   潮汐與時間膨脹：黑洞質量、距離 → 頭腳的潮汐加速度差、時間變慢的倍數
  vlbi    事件視界望遠鏡：望遠鏡數、觀測時數、是否用重建演算法 → uv 覆蓋與影像
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

BHL_NOTE = (u"本課的推導以主要步驟為主（多採用 G = c = 1 的幾何單位）；互動模擬為教學用的簡化版本。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def bhw(cfg, maxw=680):
    return wdg("bhl-w", cfg, maxw)


BHLLIB = r"""
(function () {
  if (window.__bhlLib) return; window.__bhlLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }

  /* 光線：u = 1/r，u'' = -u + 3u²（M = 1），從 x = -30 射入 */
  function trace(b) { var u = 1e-6, phi = 0, du = 1 / b, h = 0.004, pts = [], cap = false;
    for (var i = 0; i < 20000; i++) { var r = 1 / u; pts.push([-r * Math.cos(phi), r * Math.sin(phi)]);
      if (u > 0.5) { cap = true; break; } if (u < 0 && i > 10) break;
      var k1u = du, k1d = -u + 3 * u * u, k2u = du + h / 2 * k1d, k2d = -(u + h / 2 * k1u) + 3 * Math.pow(u + h / 2 * k1u, 2),
        k3u = du + h / 2 * k2d, k3d = -(u + h / 2 * k2u) + 3 * Math.pow(u + h / 2 * k2u, 2), k4u = du + h * k3d, k4d = -(u + h * k3u) + 3 * Math.pow(u + h * k3u, 2);
      u += h / 6 * (k1u + 2 * k2u + 2 * k3u + k4u); du += h / 6 * (k1d + 2 * k2d + 2 * k3d + k4d); phi += h; if (phi > 12) break; }
    return { pts: pts, cap: cap, phi: phi }; }
  function initRays(root, cfg) {
    head(root, cfg.q); var P = { b: 6 }, view = el('div'), inf;
    var u = slider(root, '衝擊參數 b（光線與黑洞中心的垂直距離，單位 GM/c²）', 2, 15, 0.01, P.b, f2, null, function (x) { P.b = x; draw(); });
    root.appendChild(view); inf = info(root);
    var bg = []; [3, 4, 5, 5.5, 7, 9, 12].forEach(function (b) { bg.push(trace(b)); });
    function draw() { var W = 640, H = 360, sc = 11, cx = 330, cy = 180, g = '';
      function P2(p) { return n1(cx + p[0] * sc) + ',' + n1(cy - p[1] * sc); }
      g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + n1(5.196 * sc) + '" fill="none" stroke="' + PU + '" stroke-dasharray="4 4"/>';
      g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + n1(3 * sc) + '" fill="none" stroke="' + OR + '" stroke-dasharray="3 3"/>';
      g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + n1(2 * sc) + '" fill="#111"/>';
      bg.forEach(function (t) { g += '<polyline points="' + t.pts.filter(function (p, i) { return i % 6 === 0; }).map(P2).join(' ') + '" fill="none" stroke="' + GY + '" stroke-width="1" opacity="0.6"/>'; });
      var t = trace(P.b); g += '<polyline points="' + t.pts.filter(function (p, i) { return i % 3 === 0; }).map(P2).join(' ') + '" fill="none" stroke="' + (t.cap ? RD : BL) + '" stroke-width="2.2"/>';
      g += tx(20, 20, '光從左邊射來', 11, null, 'start') + tx(cx, cy + 2 * sc + 14, '事件視界 r = 2', 10, '#888') ;
      g += '<rect x="440" y="290" width="12" height="2" fill="' + OR + '"/>' + tx(458, 295, '光子球 r = 3', 10, null, 'start') + '<rect x="440" y="310" width="12" height="2" fill="' + PU + '"/>' + tx(458, 315, '陰影半徑 b = 3√3 ≈ 5.2', 10, null, 'start');
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, '<rect width="' + W + '" height="' + H + '" fill="var(--surface)"/>' + g);
      var defl = (t.phi - Math.PI) * 180 / Math.PI;
      inf.innerHTML = (t.cap ? '<b>被黑洞捕獲</b>：b < 3√3 ≈ 5.196，光繞進光子球之內，再也出不來。從遠處看，這個範圍是一片黑——黑洞的<b>陰影</b>，半徑約是事件視界的 2.6 倍。' :
        '<b>逃了出去</b>，偏折約 <b>' + f1(defl) + '°</b>。' + (P.b < 6 ? '越接近 b = 5.196，光繞黑洞的圈數越多——它在光子球附近盤旋。' : '離得越遠，偏折越小（弱場時約 4GM/(c²b) 弧度）。')) +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">（數值積分光線方程式 d²u/dφ² = −u + 3u²，u = GM/(c²r)。）</span>'; }
    u();
  }

  function initVeff(root, cfg) {
    head(root, cfg.q); var P = { L: 4 }, view = el('div'), inf;
    var u = slider(root, '單位質量的角動量 L（單位 GM/c）', 3, 6, 0.01, P.L, f2, null, function (x) { P.L = x; draw(); });
    root.appendChild(view); inf = info(root);
    function V(r, L) { return (1 - 2 / r) * (1 + L * L / (r * r)); }
    function Vn(r, L) { return 1 - 2 / r + L * L / (r * r); }
    function draw() { var L = P.L, d = [], dn = [];
      for (var r = 2.05; r <= 40; r += 0.05) { d.push([r, V(r, L)]); dn.push([r, Vn(r, L)]); }
      var disc = L * L * L * L - 12 * L * L, pts = [], txt;
      if (disc >= 0) { var rs = (L * L + Math.sqrt(disc)) / 2, ru = (L * L - Math.sqrt(disc)) / 2; pts.push({ x: rs, y: V(rs, L), c: GN, n: '穩定 r=' + f1(rs) }); if (ru > 2.05) pts.push({ x: ru, y: V(ru, L), c: RD, n: '不穩定 r=' + f1(ru) });
        txt = '有兩個圓軌道：r = <b>' + f2(rs) + '</b>（谷底，穩定）與 r = <b>' + f2(ru) + '</b>（山頂，不穩定）。'; }
      else txt = '<b>沒有任何圓軌道</b>：曲線沒有谷底，任何物體都會一路掉進黑洞。';
      view.innerHTML = chart(640, 260, [{ d: d, c: BL, n: '廣義相對論的有效位能', w: 2.2 }, { d: dn, c: GY, n: '牛頓近似', w: 1.4, dash: '5,4' }], { x0: 2, x1: 40, y0: 0.8, y1: 1.3, xl: 'r（單位 GM/c²）', pts: pts, vl: [{ x: 6, c: OR, n: 'ISCO r=6' }] });
      inf.innerHTML = txt + '<br>牛頓力學中，角動量造成的「離心位障」永遠能擋住物體；廣義相對論多了一項 −2L²/r³，讓位障在近處<b>消失</b>。當 L < √12 ≈ 3.46，谷底與山頂合而為一——這就是<b>最內穩定圓軌道</b>（ISCO），r = 6GM/c²，事件視界的 3 倍。吸積盤的內緣就在這裡。'; }
    u();
  }

  function initTidal(root, cfg) {
    head(root, cfg.q); var P = { lm: 1, x: 3 }, view = el('div'), inf;
    var b = bar(root), us; [['恆星級黑洞（10 倍太陽）', 1], ['人馬座 A*（430 萬）', Math.log10(4.3e6)], ['M87*（65 億）', Math.log10(6.5e9)]].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { P.lm = o[1]; us[0](); }; b.appendChild(x); });
    us = [slider(root, '黑洞質量（太陽質量，以 10 為底的對數）', 0, 10, 0.01, P.lm, function (x) { var m = Math.pow(10, x); return m < 1e4 ? f1(m) : m.toExponential(1); }, null, function (x) { P.lm = x; draw(); }),
      slider(root, '距離（事件視界半徑的幾倍）', 1.01, 20, 0.01, P.x, f2, null, function (x) { P.x = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var Mkg = Math.pow(10, P.lm) * 1.989e30, G = 6.674e-11, c = 2.998e8, rs = 2 * G * Mkg / (c * c), r = P.x * rs, da = 2 * G * Mkg * 2 / (r * r * r), dil = Math.sqrt(1 - 1 / P.x), d = [];
      for (var k = 0; k <= 200; k++) { var lm = k / 20, Mk = Math.pow(10, lm) * 1.989e30, rk = 2 * G * Mk / (c * c); d.push([lm, Math.log10(2 * G * Mk * 2 / (rk * rk * rk) / 9.8)]); }
      view.innerHTML = chart(640, 220, [{ d: d, c: RD, n: 'log₁₀（在事件視界上，頭腳加速度差 ÷ 地球重力）', w: 2 }], { x0: 0, x1: 10, y0: -10, y1: 10, xl: 'log₁₀（黑洞質量 / 太陽質量）', hl: [{ y: 1, c: OR, n: '約 10 g：人體受不了' }], pts: [{ x: P.lm, y: Math.log10(da / 9.8), c: BL, n: '' }] });
      inf.innerHTML = '事件視界半徑 <b>' + (rs < 1e6 ? f1(rs / 1000) + ' 公里' : (rs / 1.496e11).toFixed(rs > 1.496e12 ? 0 : 2) + ' 天文單位') + '</b>。在 ' + f2(P.x) + ' 倍的距離：' +
        '<br>一個 2 公尺高的人，頭腳的加速度差約 <b>' + (da / 9.8 < 0.01 ? (da / 9.8).toExponential(1) : f1(da / 9.8)) + ' g</b>' + (da / 9.8 > 10 ? '——早已被拉成麵條。' : '——感覺不到什麼。') +
        '<br>這裡的時鐘走得比遠處慢：遠處的 1 秒，這裡只過 <b>' + f2(dil) + '</b> 秒（越靠近視界越慢）。' +
        '<br>關鍵：視界上的潮汐力與質量的<b>平方成反比</b>。小黑洞在視界外就把你撕碎；超大質量黑洞的視界上，你可能什麼都感覺不到。'; }
    us.forEach(function (u) { u(); });
  }

  function fft(re, im) { var n = re.length, i, j = 0, k, l, t; for (i = 1; i < n; i++) { var bit = n >> 1; for (; j & bit; bit >>= 1) j ^= bit; j ^= bit; if (i < j) { t = re[i]; re[i] = re[j]; re[j] = t; t = im[i]; im[i] = im[j]; im[j] = t; } }
    for (l = 2; l <= n; l <<= 1) { var a = -2 * Math.PI / l, wr = Math.cos(a), wi = Math.sin(a); for (i = 0; i < n; i += l) { var cr = 1, ci = 0; for (k = 0; k < l / 2; k++) { var p = i + k + l / 2, vr = re[p] * cr - im[p] * ci, vi = re[p] * ci + im[p] * cr;
      re[p] = re[i + k] - vr; im[p] = im[i + k] - vi; re[i + k] += vr; im[i + k] += vi; var nr = cr * wr - ci * wi; ci = cr * wi + ci * wr; cr = nr; } } } }
  function fft2(re, im, n, inv) { function rows() { for (var y = 0; y < n; y++) { var r = re.slice(y * n, y * n + n), q = im.slice(y * n, y * n + n); if (inv) q = q.map(function (v) { return -v; }); fft(r, q); if (inv) q = q.map(function (v) { return -v; });
        for (var x = 0; x < n; x++) { re[y * n + x] = r[x]; im[y * n + x] = q[x]; } } }
    function tr(a) { for (var y = 0; y < n; y++) for (var x = y + 1; x < n; x++) { var t = a[y * n + x]; a[y * n + x] = a[x * n + y]; a[x * n + y] = t; } }
    rows(); tr(re); tr(im); rows(); tr(re); tr(im); if (inv) for (var i = 0; i < n * n; i++) { re[i] /= n * n; im[i] /= n * n; } }
  var ST = [['ALMA（智利）', -23.0, -67.8], ['SMT（亞利桑那）', 32.7, -109.9], ['IRAM 30m（西班牙）', 37.1, -3.4], ['JCMT／SMA（夏威夷）', 19.8, -155.5], ['LMT（墨西哥）', 19.0, -97.3], ['SPT（南極）', -89.99, 0], ['NOEMA（法國）', 44.6, 5.9], ['GLT（格陵蘭）', 76.5, -68.7]];
  function initVLBI(root, cfg) {
    head(root, cfg.q); var P = { n: 8, hr: 12, rec: 0 }, N = 64, view = el('div', 'display:flex;gap:8px;flex-wrap:wrap;justify-content:center'), inf;
    var b = bar(root); [['直接反轉換（髒圖）', 0], ['加上重建演算法', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.rec = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    var us = [slider(root, '參與的望遠鏡數', 2, 8, 1, P.n, function (x) { return x + ' 座'; }, null, function (x) { P.n = x; draw(); }),
      slider(root, '觀測時數（地球自轉讓基線掃過更多方向）', 0.5, 24, 0.5, P.hr, function (x) { return x + ' 小時'; }, null, function (x) { P.hr = x; draw(); })];
    root.appendChild(view); inf = info(root);
    var img = []; for (var y = 0; y < N; y++) for (var x = 0; x < N; x++) { var dx = x - N / 2, dy = y - N / 2, r = Math.sqrt(dx * dx + dy * dy), th = Math.atan2(dy, dx); img.push(Math.exp(-Math.pow((r - 9) / 2.2, 2)) * (1 + 0.7 * Math.sin(th))); }
    var T = { re: img.slice(), im: new Array(N * N).fill(0) }; fft2(T.re, T.im, N, false);
    function pic(a, px) { var mx = Math.max.apply(null, a), mn = Math.min(0, Math.min.apply(null, a)), g = ''; for (var y = 0; y < N; y++) for (var x = 0; x < N; x++) { var v = (a[y * N + x] - mn) / (mx - mn || 1); v = Math.max(0, Math.min(1, v));
        g += '<rect x="' + x * px + '" y="' + y * px + '" width="' + px + '" height="' + px + '" fill="rgb(' + Math.round(255 * Math.min(1, v * 1.4)) + ',' + Math.round(200 * v * v) + ',' + Math.round(60 * v) + ')"/>'; }
      return svgw('0 0 ' + N * px + ' ' + N * px, '<g shape-rendering="crispEdges">' + g + '</g>'); }
    function draw() { var dec = 12.4 * Math.PI / 180, S = ST.slice(0, P.n).map(function (s) { var la = s[1] * Math.PI / 180, lo = s[2] * Math.PI / 180; return [Math.cos(la) * Math.cos(lo), Math.cos(la) * Math.sin(lo), Math.sin(la), la, lo]; });
      var mask = {}, uv = [], K = 13;
      for (var t = 0; t < P.hr; t += 0.1) { var H0 = t / 24 * 2 * Math.PI;
        for (var i = 0; i < S.length; i++) for (var j = i + 1; j < S.length; j++) {
          var ok = [S[i], S[j]].every(function (s) { var h = H0 + s[4]; return Math.sin(s[3]) * Math.sin(dec) + Math.cos(s[3]) * Math.cos(dec) * Math.cos(h) > 0.17; }); if (!ok) continue;
          var bx = S[i][0] - S[j][0], by = S[i][1] - S[j][1], bz = S[i][2] - S[j][2], uu = bx * Math.sin(H0) + by * Math.cos(H0), vv = -bx * Math.sin(dec) * Math.cos(H0) + by * Math.sin(dec) * Math.sin(H0) + bz * Math.cos(dec);
          uv.push([uu, vv]); [[uu, vv], [-uu, -vv]].forEach(function (q) { var ku = Math.round(q[0] / 2 * K), kv = Math.round(q[1] / 2 * K); mask[((kv + N) % N) * N + ((ku + N) % N)] = 1; }); } }
      mask[0] = 1; var keys = Object.keys(mask).map(Number);
      var re = new Array(N * N).fill(0), im = new Array(N * N).fill(0); keys.forEach(function (k) { re[k] = T.re[k]; im[k] = T.im[k]; });
      var r2 = re.slice(), i2 = im.slice(); fft2(r2, i2, N, true); var out = r2;
      if (P.rec) { for (var it = 0; it < 60; it++) { var a = out.map(function (v, k) { var x = k % N - N / 2, y = Math.floor(k / N) - N / 2; return (x * x + y * y > 400) ? 0 : Math.max(0, v); }), ai = new Array(N * N).fill(0);
          fft2(a, ai, N, false); keys.forEach(function (k) { a[k] = T.re[k]; ai[k] = T.im[k]; }); fft2(a, ai, N, true); out = a; }
        out = out.map(function (v, k) { var x = k % N - N / 2, y = Math.floor(k / N) - N / 2; return (x * x + y * y > 400) ? 0 : Math.max(0, v); }); }
      var g = '<circle cx="100" cy="100" r="96" fill="none" stroke="var(--border)"/>' + ln(4, 100, 196, 100, 'var(--border)') + ln(100, 4, 100, 196, 'var(--border)');
      uv.forEach(function (q, i) { if (i % 2) return; g += '<circle cx="' + n1(100 + q[0] * 47) + '" cy="' + n1(100 - q[1] * 47) + '" r="1.2" fill="' + BL + '"/><circle cx="' + n1(100 - q[0] * 47) + '" cy="' + n1(100 + q[1] * 47) + '" r="1.2" fill="' + BL + '"/>'; });
      function box(h, c) { return '<div style="width:200px;text-align:center">' + h + '<div style="font-size:0.85em;color:var(--text-muted)">' + c + '</div></div>'; }
      view.innerHTML = box(pic(img, 3.125), '真實的黑洞（示意）') + box(svgw('0 0 200 200', g), 'uv 覆蓋（量到的空間頻率）') + box(pic(out, 3.125), P.rec ? '重建（非負、有限大小）' : '髒圖（直接反轉換）');
      inf.innerHTML = '參與的望遠鏡：' + ST.slice(0, P.n).map(function (s) { return s[0]; }).join('、') + '。共 ' + (P.n * (P.n - 1) / 2) + ' 條基線。' +
        '<br>每一對望遠鏡在每一刻只量到影像傅立葉轉換中的<b>一個點</b>（中間的圖）。地球自轉讓基線的方向改變，點連成弧線。uv 覆蓋越完整，影像越清楚。' +
        (P.rec ? '<br>重建演算法加入了「影像不能是負的、黑洞只佔天空一小塊」等先驗，填補沒量到的頻率——真正的 EHT 用更複雜的方法，並由四組團隊各自獨立重建。' : '<br>只用量到的點直接反轉換，得到的是充滿假影的「<b>髒圖</b>」。試試按「加上重建演算法」。'); }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.bhl-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ rays: initRays, veff: initVeff, tidal: initTidal, vlbi: initVLBI })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🕳️", BHL_NOTE, BHLLIB, "bhl-w")

RAYS = bhw({"t": "rays", "q": u"黑洞旁的光線：彎曲、繞圈、被吞噬"})
VEFF = bhw({"t": "veff", "q": u"有效位能：為什麼離黑洞太近就沒有穩定的軌道"})
TIDAL = bhw({"t": "tidal", "q": u"掉進黑洞會怎樣：潮汐力與時間膨脹"})
VLBI = bhw({"t": "vlbi", "q": u"地球大小的望遠鏡：事件視界望遠鏡怎麼拍出黑洞"})
