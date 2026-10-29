# -*- coding: utf-8 -*-
"""〈土木測量〉（svy_）共用：課程包裝與 SVYLIB 互動元件（class="svy-w"）。

  bubble   三腳架整平：轉三個腳螺旋讓圓氣泡置中
  errsim   準確度與精度：系統誤差、偶然誤差與平均值
  edm      電子測距的相位法
  curv     地球曲率與大氣折光
  level    水準測量模擬器：後視、前視、高差、閉合差與改正
  coord    座標正算與反算
  traverse 閉合導線：角度閉合差、方位角推算、縱橫距、羅盤法則
  gps      衛星距離交會、接收器時鐘誤差與幾何精度（DOP）
  gnss     單點、差分、RTK、靜態定位的精度比較
  contour  等高線產生器
  earth    方格法土方計算與平衡高程
  curve    圓曲線要素與偏角法放樣
公式的數值驗證沿用 md_common 的 check()。
"""
from md_common import make_with, check, MDLIB
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

SVY_NOTE = u"本課程的公式以教學為主，實際作業請依內政部國土測繪中心等主管機關的最新規範；互動圖中的資料皆為示意。"


def vw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("svy-w", cfg)


F = D

SVYLIB = r"""
(function () {
  if (window.__svyLib) return; window.__svyLib = 1;
""" + BASEJS + r"""
  var _sl = slider; slider = function (root, lab, min, max, step, val, fmt, k, cb) { var u = _sl(root, lab, min, max, step, val, fmt, k, cb); var b = root.lastChild && root.lastChild.querySelector('b'); if (b) b.textContent = fmt(val); return u; };
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#9aa3ad', TL = '#2a9d8f', YL = '#d4a017', BR = '#a0704a';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root, items, cur, cb) { var b = el('div'); items.forEach(function (s) { var x = btn(s[0], s[1]); x.onclick = function () { cb(s[1]); mark(b, s[1]); }; b.appendChild(x); }); mark(b, cur); root.appendChild(b); return b; }
  function bt(par, t, cb) { var b = btn(t); b.onclick = cb; par.appendChild(b); return b; }
  function row(root) { var d = el('div'); root.appendChild(d); return d; }
  function setS(root, k, v) { var e = root.querySelector('input[data-k="' + k + '"]'); if (e) { e.value = v; e.dispatchEvent(new Event('input')); } }
  function rng(seed) { var s = seed >>> 0; return function () { s = (s + 0x6D2B79F5) >>> 0; var t = s; t = Math.imul(t ^ t >>> 15, 1 | t); t = (t + Math.imul(t ^ t >>> 7, 61 | t)) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function gs(r) { var u = 0; while (u === 0) u = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * r()); }
  function fx(v, d) { if (!isFinite(v)) return '—'; d = d === undefined ? 3 : d; var s = v.toFixed(d); return s === (-0).toFixed(d) ? (0).toFixed(d) : s; }
  function dms(a) { var sg = a < 0 ? '−' : ''; a = Math.abs(a); var d = Math.floor(a), m = Math.floor((a - d) * 60), s = (a - d - m / 60) * 3600; if (s >= 59.95) { s = 0; m++; } if (m >= 60) { m = 0; d++; } return sg + d + '°' + (m < 10 ? '0' : '') + m + '′' + (s < 9.95 ? '0' : '') + s.toFixed(1) + '″'; }
  function n360(a) { a = a % 360; return a < 0 ? a + 360 : a; }
  var MK = '<defs><marker id="svah" viewBox="0 0 10 10" refX="10" refY="5" markerWidth="8" markerHeight="8" markerUnits="userSpaceOnUse" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888"/></marker></defs>';
  function arr(x1, y1, x2, y2, c, w) { return ln(x1, y1, x2, y2, c || '#888', w || 1.6, 'marker-end="url(#svah)"'); }
  function cell(s, css) { return '<td style="padding:3px 7px;text-align:right;white-space:nowrap;' + (css || '') + '">' + s + '</td>'; }
  function tbl(head, rows) { return '<div style="overflow-x:auto"><table style="border-collapse:collapse;margin:6px auto;width:auto;min-width:0;font-size:0.86em;font-variant-numeric:tabular-nums"><tr>' + head.map(function (h) { return '<th style="padding:3px 7px;font-weight:normal;color:var(--text-muted);border-bottom:2px solid var(--border)">' + h + '</th>'; }).join('') + '</tr>' + rows.join('') + '</table></div>'; }

  /* ---------- 整平 ---------- */
  function initBubble(root, cfg) {
    head(root, cfg.q); var h = [0, 0, 0], g0 = [3.2, -4.1], v = el('div'), inf, ks = ['A', 'B', 'C'];
    ks.forEach(function (k, i) { slider(root, '腳螺旋 ' + k + '（往上轉為正）', -10, 10, 0.1, 0, function (x) { return x.toFixed(1); }, k, function (x) { h[i] = x; draw(); }); });
    var d = row(root); bt(d, '換一個傾斜的地面', function () { g0 = [Math.round((Math.random() * 10 - 5) * 10) / 10, Math.round((Math.random() * 10 - 5) * 10) / 10]; ks.forEach(function (k) { setS(root, k, 0); }); draw(); }); bt(d, '螺旋歸零', function () { ks.forEach(function (k) { setS(root, k, 0); }); });
    root.appendChild(v); inf = info(root);
    function draw() { var px = (h[2] - h[1]) / 1.732, py = (h[0] - (h[1] + h[2]) / 2) / 1.5, gx = g0[0] + px, gy = g0[1] + py, mag = Math.hypot(gx, gy), cx = 340, cy = 168, R = 110, k = 13, bx = gx * k, by = gy * k, bm = Math.hypot(bx, by);
      if (bm > R - 18) { bx *= (R - 18) / bm; by *= (R - 18) / bm; } var g = '';
      g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" fill="#e8f4ea" stroke="' + GY + '" stroke-width="3"/><circle cx="' + cx + '" cy="' + cy + '" r="20" fill="none" stroke="#333" stroke-width="1.5"/>';
      g += '<circle cx="' + n1(cx + bx) + '" cy="' + n1(cy - by) + '" r="16" fill="' + (mag < 0.3 ? GN : '#b8dff5') + '" fill-opacity="0.9" stroke="#5a8fb0" stroke-width="1.5"/>';
      [[0, 1], [-0.866, -0.5], [0.866, -0.5]].forEach(function (p, i) { var x = cx + p[0] * (R + 38), y = cy - p[1] * (R + 38); g += '<circle cx="' + n1(x) + '" cy="' + n1(y) + '" r="15" fill="' + BL + '"/>' + tx(x, y + 4, ks[i], 12, '#fff') + tx(x + (p[0] >= 0 ? 22 : -22), y + 4, h[i].toFixed(1), 10, 'var(--text-muted)', p[0] >= 0 ? 'start' : 'end'); });
      v.innerHTML = svgw('0 0 680 335', g);
      inf.innerHTML = '儀器傾斜約 <b>' + (mag * 20).toFixed(0) + '″</b>（示意單位）。' + (mag < 0.3 ? '<b style="color:' + GN + '">氣泡已進入圓圈，整平完成 ✓</b>' : '氣泡永遠跑向<b>比較高</b>的那一側。') + '<br>口訣：先把兩個腳螺旋（例如 B、C）<b>同時向內或向外</b>轉，讓氣泡沿著 B–C 方向移到中線；再只轉第三個螺旋 A，把氣泡拉到中心。氣泡移動的方向和<b>左手大拇指</b>轉動的方向相同。'; }
    draw();
  }

  /* ---------- 準確度與精度 ---------- */
  function initErrsim(root, cfg) {
    head(root, cfg.q); var bias = cfg.bias || 0, sig = cfg.sig || 3, n = 20, seed = 1, v = el('div'), inf;
    slider(root, '系統誤差（往右偏，mm）', 0, 15, 0.5, bias, function (x) { return x.toFixed(1); }, 'b', function (x) { bias = x; draw(); });
    slider(root, '偶然誤差標準差 σ（mm）', 0.2, 10, 0.1, sig, function (x) { return x.toFixed(1); }, 's', function (x) { sig = x; draw(); });
    slider(root, '觀測次數 n', 2, 200, 1, n, String, 'n', function (x) { n = x; draw(); });
    var d = row(root); bt(d, '🎲 重新觀測', function () { seed++; draw(); }); root.appendChild(v); inf = info(root);
    function draw() { var r = rng(seed * 13), P = [], i, mx = 0, my = 0; for (i = 0; i < n; i++) P.push([bias + sig * gs(r), sig * gs(r)]); P.forEach(function (p) { mx += p[0]; my += p[1]; }); mx /= n; my /= n;
      var sx = 0; P.forEach(function (p) { sx += Math.pow(p[0] - mx, 2); }); sx = Math.sqrt(sx / (n - 1));
      var cx = 170, cy = 150, S = 6.5, g = ''; [60, 40, 20].forEach(function (rr, j) { g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + rr * 2 + '" fill="' + ['#f6e3e3', '#f9eecf', '#e3f1e6'][j] + '" stroke="' + GY + '"/>'; });
      g += ln(cx - 125, cy, cx + 125, cy, GY, 0.6) + ln(cx, cy - 125, cx, cy + 125, GY, 0.6);
      P.forEach(function (p) { g += '<circle cx="' + n1(cx + p[0] * S) + '" cy="' + n1(cy - p[1] * S) + '" r="3" fill="' + BL + '" fill-opacity="0.75"/>'; });
      g += '<circle cx="' + n1(cx + mx * S) + '" cy="' + n1(cy - my * S) + '" r="6" fill="none" stroke="' + RD + '" stroke-width="2.5"/>' + tx(cx, 292, '十字中心 = 真值；紅圈 = 平均值', 10, 'var(--text-muted)');
      var bins = [], B = 20, lo = -20, w = 2; for (i = 0; i < B; i++) bins.push(0); P.forEach(function (p) { var k = Math.floor((p[0] - lo) / w); if (k >= 0 && k < B) bins[k]++; }); var mb = Math.max.apply(null, bins.concat([1]));
      bins.forEach(function (c, k) { var hh = c / mb * 180; g += '<rect x="' + (370 + k * 14) + '" y="' + n1(250 - hh) + '" width="12" height="' + n1(hh) + '" fill="' + BL + '" fill-opacity="0.7"/>'; });
      g += ln(370 + (0 - lo) / w * 14, 60, 370 + (0 - lo) / w * 14, 255, GN, 2) + tx(370 + (0 - lo) / w * 14, 54, '真值', 10, GN) + tx(510, 272, '橫向誤差分布（mm）', 10, 'var(--text-muted)') + tx(370, 265, lo, 9, 'var(--text-muted)') + tx(650, 265, '+' + (lo + B * w), 9, 'var(--text-muted)');
      v.innerHTML = svgw('0 0 680 300', g);
      inf.innerHTML = '平均值偏離真值 <b>' + fx(mx, 2) + ' mm</b>（反映<b>準確度</b>，主要來自系統誤差）；觀測值的標準差 s = <b>' + fx(sx, 2) + ' mm</b>（反映<b>精度</b>）。<br>平均值的中誤差 = s / √n = ' + fx(sx / Math.sqrt(n), 2) + ' mm：多觀測幾次可以壓低偶然誤差，但<b>系統誤差不會因為多量幾次而消失</b>，必須靠改正或觀測方法抵消。'; }
    draw();
  }

  /* ---------- 電子測距 相位法 ---------- */
  function initEdm(root, cfg) {
    head(root, cfg.q); var Dm = 23.47, v = el('div'), inf;
    slider(root, '儀器到稜鏡的距離 D（m）', 1, 99, 0.01, Dm, function (x) { return x.toFixed(2); }, 'd', function (x) { Dm = x; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var U = 10, lam = 2 * U, path = 2 * Dm, N = Math.floor(path / lam), frac = path / lam - N, ph = frac * 360, g = MK, x0 = 30, W = 620, sx = W / Math.max(path, 40), y = 90;
      g += tx(x0, 30, '光走的總路徑 2D = ' + path.toFixed(2) + ' m（來回）；精測尺調變波長 λ = ' + lam + ' m', 11, 'currentColor', 'start');
      var pts = ''; for (var s = 0; s <= path; s += 0.25) pts += n1(x0 + s * sx) + ',' + n1(y - 26 * Math.sin(2 * Math.PI * s / lam)) + ' '; g += '<polyline points="' + pts + '" fill="none" stroke="' + BL + '" stroke-width="2"/>';
      for (var k = 0; k <= N; k++) g += ln(x0 + k * lam * sx, y - 36, x0 + k * lam * sx, y + 36, GY, 1, 'stroke-dasharray="3 3"');
      g += '<rect x="' + n1(x0 + N * lam * sx) + '" y="' + (y - 40) + '" width="' + n1(frac * lam * sx) + '" height="80" fill="' + OR + '" fill-opacity="0.2"/>' + ln(x0, y + 50, x0 + path * sx, y + 50, '#333', 1.5) + tx(x0 + N * lam * sx / 2, y + 66, 'N = ' + N + ' 個完整波長（相位計量不到）', 10, 'var(--text-muted)') + tx(x0 + (N + frac / 2) * lam * sx, y - 46, 'Δφ = ' + ph.toFixed(1) + '°', 10, OR);
      var c1 = (Dm % 1000), coarse = Math.round(c1 / 10) * 10, fine = (frac * U);
      v.innerHTML = svgw('0 0 680 170', g);
      inf.innerHTML = '相位計只能量出「不足一個波長」的部分：Δφ = ' + ph.toFixed(1) + '° → 精測讀數 = (Δφ/360°) × λ/2 = <b>' + fine.toFixed(3) + ' m</b>。<br>完整波長的個數 N 是未知的（<b>整周模糊</b>）。所以儀器再用一個長波長（例如 λ/2 = 1000 m）的粗測頻率測一次，粗略知道 D ≈ ' + (Math.floor(Dm / 10) * 10 + fine).toFixed(1) + ' m，從中取出「十位以上」的數字，再接上精測的尾數：<br>D = N × λ/2 + 精測讀數 = ' + N + ' × ' + U + ' + ' + fine.toFixed(3) + ' = <b>' + (N * U + fine).toFixed(3) + ' m</b>。'; }
    draw();
  }

  /* ---------- 地球曲率與折光 ---------- */
  function initCurv(root, cfg) {
    head(root, cfg.q); var Dk = 1, k = 0.14, v = el('div'), inf;
    slider(root, '視線距離 D（km）', 0.05, 10, 0.05, Dk, function (x) { return x.toFixed(2); }, 'd', function (x) { Dk = x; draw(); });
    slider(root, '大氣折光係數 k', 0, 0.3, 0.01, k, function (x) { return x.toFixed(2); }, 'k', function (x) { k = x; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var R = 6371, c = Dk * Dk / (2 * R) * 1000, r = k * c, h = (1 - k) * c, g = '';
      var d1 = [], d2 = [], d3 = []; for (var x = 0; x <= 2; x += 0.02) { var cc = x * x / (2 * R) * 1e6; d1.push([x, cc]); d2.push([x, k * cc]); d3.push([x, (1 - k) * cc]); }
      var cx = 60, cy = 60, W = 560; g += ln(cx, cy, cx + W, cy, OR, 2) + tx(cx + W, cy - 6, '水平視線', 10, OR, 'end');
      var pts = ''; for (var t = 0; t <= 1.0001; t += 0.02) pts += n1(cx + t * W) + ',' + n1(cy + 90 * t * t) + ' '; g += '<polyline points="' + pts + '" fill="none" stroke="' + GN + '" stroke-width="3"/>' + tx(cx + W - 6, cy + 106, '水準面（地球表面，誇大）', 10, GN, 'end');
      var pr = ''; for (t = 0; t <= 1.0001; t += 0.02) pr += n1(cx + t * W) + ',' + n1(cy + 90 * k / 0.3 * 0.5 * t * t) + ' '; g += '<polyline points="' + pr + '" fill="none" stroke="' + PU + '" stroke-width="2" stroke-dasharray="5 4"/>' + tx(cx + W - 6, cy + 90 * k / 0.3 * 0.5 + 16, '實際（被折彎的）視線', 10, PU, 'end');
      g += '<circle cx="' + cx + '" cy="' + cy + '" r="6" fill="#333"/>' + tx(cx, cy - 12, '儀器', 10, 'currentColor');
      v.innerHTML = svgw('0 0 680 170', g) + chart(680, 210, [{ d: d1, c: GN, n: '地球曲率 c' }, { d: d2, c: PU, n: '折光 r', dash: '5 4' }, { d: d3, c: RD, n: '合併 (1−k)c' }], { x0: 0, x1: 2, y0: 0, y1: 320, xl: '距離（km）', yl: 'mm' });
      inf.innerHTML = 'D = ' + Dk.toFixed(2) + ' km 時：地球曲率使水準面比水平視線低 c = D²/2R = <b>' + (c * 1000).toFixed(1) + ' mm</b>；大氣折光把視線往下彎，抵消一部分 r = k·c = ' + (r * 1000).toFixed(1) + ' mm；合併影響 <b>' + (h * 1000).toFixed(1) + ' mm</b>。<br>100 m 時只有 0.7 mm，1 km 就約 68 mm。這就是水準測量要讓<b>前後視距離相等</b>的原因：前後兩根尺受到一樣的影響，相減就抵消了。'; }
    draw();
  }

  /* ---------- 水準測量模擬 ---------- */
  function initLevel(root, cfg) {
    head(root, cfg.q); var ns = 4, sig = 1, seed = 2, v = el('div'), inf;
    slider(root, '測站數', 2, 8, 1, ns, String, 'n', function (x) { ns = x; draw(); }); slider(root, '每次讀數的誤差 σ（mm）', 0, 3, 0.1, sig, function (x) { return x.toFixed(1); }, 's', function (x) { sig = x; draw(); });
    var d = row(root); bt(d, '🎲 換一組地形與讀數', function () { seed++; draw(); }); root.appendChild(v); inf = info(root);
    function draw() { var r = rng(seed * 7), H = [52.317], i; for (i = 1; i <= ns; i++) H.push(H[i - 1] + (r() - 0.45) * 2.6);
      var Hend = H[ns], BS = [], FS = [], HI = []; for (i = 0; i < ns; i++) { var hi = Math.max(H[i], H[i + 1]) + 1.2 + r() * 0.4; HI.push(hi); BS.push(hi - H[i] + sig / 1000 * gs(r)); FS.push(hi - H[i + 1] + sig / 1000 * gs(r)); }
      BS = BS.map(function (x) { return Math.round(x * 1000) / 1000; }); FS = FS.map(function (x) { return Math.round(x * 1000) / 1000; });
      var calc = [H[0]]; for (i = 0; i < ns; i++) calc.push(calc[i] + BS[i] - FS[i]); var f = calc[ns] - Hend, K = ns * 0.1, allow = 10 * Math.sqrt(K);
      var rows = [], sb = 0, sf = 0; for (i = 0; i <= ns; i++) { var corr = -f * i / ns; if (i < ns) sb += BS[i]; if (i > 0) sf += FS[i - 1];
        rows.push('<tr>' + cell(i === 0 ? 'BM1' : i === ns ? 'BM2' : 'TP' + i, 'text-align:left') + cell(i < ns ? BS[i].toFixed(3) : '') + cell(i > 0 ? FS[i - 1].toFixed(3) : '') + cell(i > 0 ? (BS[i - 1] - FS[i - 1] >= 0 ? '+' : '') + (BS[i - 1] - FS[i - 1]).toFixed(3) : '') + cell(calc[i].toFixed(3)) + cell(i > 0 ? (corr * 1000 >= 0 ? '+' : '') + (corr * 1000).toFixed(1) : '') + cell('<b>' + (calc[i] + corr).toFixed(3) + '</b>') + '</tr>'); }
      rows.push('<tr style="border-top:2px solid var(--border)">' + cell('合計', 'text-align:left') + cell(sb.toFixed(3)) + cell(sf.toFixed(3)) + cell((sb - sf >= 0 ? '+' : '') + (sb - sf).toFixed(3)) + cell('') + cell('') + cell('') + '</tr>');
      var W = 640, x0 = 20, lo = Math.min.apply(null, H) - 0.5, hi2 = Math.max.apply(null, HI) + 0.5, Y = function (z) { return 210 - (z - lo) / (hi2 - lo) * 190; }, X = function (j) { return x0 + j * W / ns; }, g = '';
      var tp = ''; for (i = 0; i <= ns; i++) tp += n1(X(i)) + ',' + n1(Y(H[i])) + ' '; g += '<polygon points="' + n1(X(0)) + ',220 ' + tp + n1(X(ns)) + ',220" fill="' + BR + '" fill-opacity="0.25"/><polyline points="' + tp + '" fill="none" stroke="' + BR + '" stroke-width="2"/>';
      for (i = 0; i < ns; i++) { var xm = (X(i) + X(i + 1)) / 2; g += ln(X(i), Y(HI[i]), X(i + 1), Y(HI[i]), OR, 1.3, 'stroke-dasharray="4 3"') + ln(xm, Y(HI[i]) + 4, xm - 8, Y((H[i] + H[i + 1]) / 2) + 14, '#555', 1.5) + ln(xm, Y(HI[i]) + 4, xm + 8, Y((H[i] + H[i + 1]) / 2) + 14, '#555', 1.5) + '<rect x="' + (xm - 8) + '" y="' + n1(Y(HI[i]) - 6) + '" width="16" height="9" fill="' + BL + '"/>'; }
      for (i = 0; i <= ns; i++) { g += '<rect x="' + n1(X(i) - 3) + '" y="' + n1(Y(H[i] + 4)) + '" width="6" height="' + n1(Y(H[i]) - Y(H[i] + 4)) + '" fill="' + YL + '" stroke="#555" stroke-width="0.5"/>' + tx(X(i), Y(H[i]) + 14, i === 0 ? 'BM1' : i === ns ? 'BM2' : 'TP' + i, 10, 'currentColor'); }
      v.innerHTML = svgw('0 0 680 236', g) + tbl(['點', '後視 BS', '前視 FS', '高差 ΔH', '計算高程', '改正（mm）', '改正後高程'], rows);
      var ok = Math.abs(f * 1000) <= allow;
      inf.innerHTML = '起點 BM1 = ' + H[0].toFixed(3) + ' m，終點 BM2 的已知高程 = ' + Hend.toFixed(3) + ' m。高差 = 後視 − 前視；ΣBS − ΣFS = ' + (sb - sf).toFixed(3) + ' m。<br>' +
        '閉合差 f = 計算的 BM2 − 已知 BM2 = <b>' + (f * 1000).toFixed(1) + ' mm</b>；路線長約 ' + K.toFixed(1) + ' km，以容許值 ±10√K mm = ±' + allow.toFixed(1) + ' mm 判斷：' + (ok ? '<b style="color:' + GN + '">合格</b>，按測站數平均分配改正（反號）。' : '<b style="color:' + RD + '">超限，要重測</b>。'); }
    draw();
  }

  /* ---------- 座標正算與反算 ---------- */
  function initCoord(root, cfg) {
    head(root, cfg.q); var mode = cfg.mode || 'fwd', A = [120, 80], az = 58.5, Ds = 95.3, B = [190, 175], v = el('div'), inf, box = el('div');
    bar(root, [['正算：已知方位角與距離 → 座標', 'fwd'], ['反算：已知兩點座標 → 方位角與距離', 'inv']], mode, function (k) { mode = k; ui(); draw(); });
    root.appendChild(box); root.appendChild(v); inf = info(root);
    function ui() { box.innerHTML = ''; slider(box, 'A 點 E（m）', 0, 300, 0.1, A[0], function (x) { return x.toFixed(1); }, 'ae', function (x) { A[0] = x; draw(); }); slider(box, 'A 點 N（m）', 0, 300, 0.1, A[1], function (x) { return x.toFixed(1); }, 'an', function (x) { A[1] = x; draw(); });
      if (mode === 'fwd') { slider(box, '方位角 α（度，由北順時針）', 0, 359.9, 0.1, az, function (x) { return dms(x); }, 'az', function (x) { az = x; draw(); }); slider(box, '水平距離 D（m）', 1, 200, 0.1, Ds, function (x) { return x.toFixed(1); }, 'ds', function (x) { Ds = x; draw(); }); }
      else { slider(box, 'B 點 E（m）', 0, 300, 0.1, B[0], function (x) { return x.toFixed(1); }, 'be', function (x) { B[0] = x; draw(); }); slider(box, 'B 點 N（m）', 0, 300, 0.1, B[1], function (x) { return x.toFixed(1); }, 'bn', function (x) { B[1] = x; draw(); }); } }
    function draw() { var P = mode === 'fwd' ? [A[0] + Ds * Math.sin(az * Math.PI / 180), A[1] + Ds * Math.cos(az * Math.PI / 180)] : B, dE = P[0] - A[0], dN = P[1] - A[1], dist = Math.hypot(dE, dN), a = n360(Math.atan2(dE, dN) * 180 / Math.PI);
      var e0 = Math.min(A[0], P[0]) - 40, e1 = Math.max(A[0], P[0]) + 40, m0 = Math.min(A[1], P[1]) - 40, m1 = Math.max(A[1], P[1]) + 80, S = Math.min(620 / (e1 - e0), 340 / (m1 - m0)), ec = (e0 + e1) / 2, mc = (m0 + m1) / 2,
        X = function (e) { return 340 + (e - ec) * S; }, Y = function (n) { return 200 - (n - mc) * S; }, g = MK, i, step = S > 2 ? 10 : S > 0.8 ? 25 : 50;
      for (i = Math.floor((ec - 400 / S) / step) * step; i <= ec + 400 / S; i += step) g += ln(X(i), 0, X(i), 400, 'var(--border)', 0.5);
      for (i = Math.floor((mc - 250 / S) / step) * step; i <= mc + 250 / S; i += step) g += ln(0, Y(i), 680, Y(i), 'var(--border)', 0.5);
      g += ln(X(A[0]), Y(A[1]), X(A[0]), Y(A[1] + 60), GY, 1.2, 'stroke-dasharray="4 3"') + tx(X(A[0]), Y(A[1] + 66), 'N', 11, GY);
      g += ln(X(A[0]), Y(A[1]), X(P[0]), Y(A[1]), OR, 1.5, 'stroke-dasharray="5 3"') + ln(X(P[0]), Y(A[1]), X(P[0]), Y(P[1]), PU, 1.5, 'stroke-dasharray="5 3"') + arr(X(A[0]), Y(A[1]), X(P[0]), Y(P[1]), BL, 2.5);
      var r0 = 30, pth = ''; for (i = 0; i <= 30; i++) { var t = a * i / 30 * Math.PI / 180; pth += (i ? 'L' : 'M') + n1(X(A[0]) + r0 * Math.sin(t)) + ' ' + n1(Y(A[1]) - r0 * Math.cos(t)); } g += '<path d="' + pth + '" fill="none" stroke="' + RD + '" stroke-width="1.5"/>';
      g += '<circle cx="' + n1(X(A[0])) + '" cy="' + n1(Y(A[1])) + '" r="5" fill="' + GN + '"/>' + tx(X(A[0]) - 10, Y(A[1]) + 16, 'A', 12, GN) + '<circle cx="' + n1(X(P[0])) + '" cy="' + n1(Y(P[1])) + '" r="5" fill="' + RD + '"/>' + tx(X(P[0]) + 12, Y(P[1]) - 6, 'B', 12, RD);
      g += tx((X(A[0]) + X(P[0])) / 2, Y(A[1]) + 16, 'ΔE', 11, OR) + tx(X(P[0]) + 8, (Y(A[1]) + Y(P[1])) / 2, 'ΔN', 11, PU, 'start');
      v.innerHTML = svgw('0 0 680 400', g);
      inf.innerHTML = (mode === 'fwd' ? '<b>座標正算</b>：ΔE = D·sin α = ' + Ds.toFixed(1) + ' × sin(' + dms(az) + ') = ' + fx(dE) + ' m；ΔN = D·cos α = ' + fx(dN) + ' m。<br>B = (' + fx(P[0]) + ', ' + fx(P[1]) + ')。'
        : '<b>座標反算</b>：ΔE = ' + fx(dE) + '、ΔN = ' + fx(dN) + '。<br>距離 D = √(ΔE² + ΔN²) = <b>' + fx(dist) + ' m</b>；方位角 α = atan2(ΔE, ΔN) = <b>' + dms(a) + '</b>（' + (dE >= 0 ? (dN >= 0 ? '第一象限' : '第二象限，ΔN < 0') : (dN < 0 ? '第三象限' : '第四象限')) + '）。') +
        '<br>注意測量的座標是 (E, N)，方位角從<b>北</b>開始<b>順時針</b>量，所以 E 用 sin、N 用 cos，和數學課的 (x, y) 剛好相反。'; }
    ui(); draw();
  }

  /* ---------- 閉合導線 ---------- */
  function initTraverse(root, cfg) {
    head(root, cfg.q); var sa = 8, sd = 5, seed = 3, v = el('div'), inf, T = [[1000, 1000], [1012.5, 1145.2], [1150.8, 1210.4], [1265.3, 1102.6], [1198.2, 968.7]];
    slider(root, '測角誤差 σ（秒）', 0, 30, 1, sa, function (x) { return x + '″'; }, 'a', function (x) { sa = x; draw(); }); slider(root, '測距誤差 σ（mm）', 0, 30, 1, sd, function (x) { return x + ' mm'; }, 'd', function (x) { sd = x; draw(); });
    var d = row(root); bt(d, '🎲 換一組觀測', function () { seed++; draw(); }); root.appendChild(v); inf = info(root);
    function azm(p, q) { return n360(Math.atan2(q[0] - p[0], q[1] - p[1]) * 180 / Math.PI); }
    function draw() { var r = rng(seed * 11), n = T.length, i, azT = [], Dt = [], B = [], Bo = [], Do = [];
      for (i = 0; i < n; i++) { azT.push(azm(T[i], T[(i + 1) % n])); Dt.push(Math.hypot(T[(i + 1) % n][0] - T[i][0], T[(i + 1) % n][1] - T[i][1])); }
      for (i = 0; i < n; i++) { var b = n360(azT[(i + n - 1) % n] + 180 - azT[i]); B.push(b); Bo.push(b + sa / 3600 * gs(r)); Do.push(Dt[i] + sd / 1000 * gs(r)); }
      var sum = Bo.reduce(function (a, b) { return a + b; }, 0), fb = (sum - (n - 2) * 180) * 3600, Bc = Bo.map(function (b) { return b - fb / 3600 / n; });
      var az = [azT[0]]; for (i = 1; i < n; i++) az.push(n360(az[i - 1] + 180 - Bc[i]));
      var dN = [], dE = [], sN = 0, sE = 0, sD = 0; for (i = 0; i < n; i++) { dN.push(Do[i] * Math.cos(az[i] * Math.PI / 180)); dE.push(Do[i] * Math.sin(az[i] * Math.PI / 180)); sN += dN[i]; sE += dE[i]; sD += Do[i]; }
      var fl = Math.hypot(sN, sE), C = [[T[0][0], T[0][1]]], U = [[T[0][0], T[0][1]]], rows = [];
      for (i = 0; i < n; i++) { U.push([U[i][0] + dE[i], U[i][1] + dN[i]]); var cN = -sN * Do[i] / sD, cE = -sE * Do[i] / sD; C.push([C[i][0] + dE[i] + cE, C[i][1] + dN[i] + cN]);
        rows.push('<tr>' + cell('P' + (i + 1), 'text-align:left') + cell(dms(Bo[i])) + cell(dms(Bc[i])) + cell(dms(az[i])) + cell(Do[i].toFixed(3)) + cell(dN[i].toFixed(3)) + cell(dE[i].toFixed(3)) + cell((cN * 1000).toFixed(1) + ' / ' + (cE * 1000).toFixed(1)) + cell(i < n - 1 ? C[i + 1][1].toFixed(3) + ', ' + C[i + 1][0].toFixed(3) : '回到 P1') + '</tr>'); }
      var S = 1.0, X = function (e) { return 70 + (e - 1000) * S; }, Y = function (nn) { return 290 - (nn - 960) * S; }, g = MK, pts = T.map(function (p) { return n1(X(p[0])) + ',' + n1(Y(p[1])); }).join(' ');
      g += '<polygon points="' + pts + '" fill="' + BL + '" fill-opacity="0.08" stroke="' + BL + '" stroke-width="2"/>'; T.forEach(function (p, j) { g += '<circle cx="' + n1(X(p[0])) + '" cy="' + n1(Y(p[1])) + '" r="5" fill="' + BL + '"/>' + tx(X(p[0]) + (j === 0 || j === 1 ? -14 : 14), Y(p[1]) + 4, 'P' + (j + 1), 11, BL); });
      var ix = 520, iy = 150, mag = 2000; g += '<circle cx="' + ix + '" cy="' + iy + '" r="70" fill="var(--surface)" stroke="' + GY + '"/>' + tx(ix, iy - 80, '閉合差向量（極度放大）', 10, 'var(--text-muted)') + '<circle cx="' + ix + '" cy="' + iy + '" r="3" fill="' + GN + '"/>';
      var vx = sE * mag, vy = -sN * mag, vm = Math.hypot(vx, vy); if (vm > 65) { vx *= 65 / vm; vy *= 65 / vm; } if (vm > 1) g += arr(ix, iy, ix + vx, iy + vy, RD, 2.5); g += tx(ix + 6, iy + 88, '1 cm', 9, 'var(--text-muted)', 'start');
      g += ln(ix - 20, iy + 85, ix, iy + 85, '#333', 2.5);
      v.innerHTML = svgw('0 0 680 320', g) + tbl(['測站', '觀測角', '改正後角', '方位角', '距離', 'ΔN', 'ΔE', '改正 N/E (mm)', '改正後 N, E'], rows);
      var ratio = fl > 0 ? Math.round(sD / fl) : Infinity;
      inf.innerHTML = '① <b>角度閉合差</b>：Σβ = ' + dms(sum) + '，理論值 (n−2)×180° = ' + ((n - 2) * 180) + '°，f<sub>β</sub> = <b>' + fb.toFixed(1) + '″</b>，平均分配到 ' + n + ' 個角（每角 ' + (-fb / n).toFixed(1) + '″）。<br>' +
        '② <b>推算方位角</b>：α<sub>下一邊</sub> = α<sub>上一邊</sub> + 180° − β（順時針方向的導線、β 為內角）。<br>' +
        '③ <b>縱橫距閉合差</b>：ΣΔN = ' + (sN * 1000).toFixed(1) + ' mm、ΣΔE = ' + (sE * 1000).toFixed(1) + ' mm，線性閉合差 = <b>' + (fl * 1000).toFixed(1) + ' mm</b>，精度 = 1/' + (isFinite(ratio) ? ratio.toLocaleString() : '∞') + '（總長 ' + sD.toFixed(1) + ' m）。<br>' +
        '④ <b>羅盤法則</b>：每邊的改正量與邊長成正比，反號分配。'; }
    draw();
  }

  /* ---------- GPS 距離交會 ---------- */
  function initGps(root, cfg) {
    head(root, cfg.q); var bias = 25, noise = 0, spread = 120, solve = false, v = el('div'), inf, seed = 1;
    slider(root, '接收器時鐘誤差（換算成距離，m）', -60, 60, 1, bias, function (x) { return x + ' m'; }, 'b', function (x) { bias = x; draw(); });
    slider(root, '距離量測雜訊（m）', 0, 10, 0.5, noise, function (x) { return x.toFixed(1) + ' m'; }, 'n', function (x) { noise = x; draw(); });
    slider(root, '衛星分布的張角（度）', 20, 170, 5, spread, function (x) { return x + '°'; }, 's', function (x) { spread = x; draw(); });
    var d = row(root); var sb = bt(d, '解出位置與時鐘誤差', function () { solve = !solve; sb.textContent = solve ? '顯示原始的偽距圓' : '解出位置與時鐘誤差'; draw(); }); bt(d, '🎲 換一組雜訊', function () { seed++; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var rcv = [0, 0], r = rng(seed * 5), S = [], i; for (i = 0; i < 3; i++) { var ang = (90 + (i - 1) * spread / 2) * Math.PI / 180; S.push([260 * Math.cos(ang), 260 * Math.sin(ang)]); }
      var rho = S.map(function (s) { return Math.hypot(s[0] - rcv[0], s[1] - rcv[1]) + bias + noise * gs(r); });
      var x = [0, 120, 0]; for (var it = 0; it < 15; it++) { var A = [], L = []; S.forEach(function (s, j) { var dd = Math.hypot(x[0] - s[0], x[1] - s[1]); A.push([(x[0] - s[0]) / dd, (x[1] - s[1]) / dd, 1]); L.push(rho[j] - dd - x[2]); });
        var M = [[0, 0, 0], [0, 0, 0], [0, 0, 0]], b = [0, 0, 0]; A.forEach(function (a, j) { for (var p = 0; p < 3; p++) { b[p] += a[p] * L[j]; for (var q = 0; q < 3; q++) M[p][q] += a[p] * a[q]; } });
        var det = M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0]) + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]); if (Math.abs(det) < 1e-12) break;
        var inv = [[(M[1][1] * M[2][2] - M[1][2] * M[2][1]) / det, (M[0][2] * M[2][1] - M[0][1] * M[2][2]) / det, (M[0][1] * M[1][2] - M[0][2] * M[1][1]) / det], [(M[1][2] * M[2][0] - M[1][0] * M[2][2]) / det, (M[0][0] * M[2][2] - M[0][2] * M[2][0]) / det, (M[0][2] * M[1][0] - M[0][0] * M[1][2]) / det], [(M[1][0] * M[2][1] - M[1][1] * M[2][0]) / det, (M[0][1] * M[2][0] - M[0][0] * M[2][1]) / det, (M[0][0] * M[1][1] - M[0][1] * M[1][0]) / det]];
        var dx = [0, 1, 2].map(function (p) { return inv[p][0] * b[0] + inv[p][1] * b[1] + inv[p][2] * b[2]; }); x = [x[0] + dx[0], x[1] + dx[1], x[2] + dx[2]]; var Q = inv; }
      var dop = Q ? Math.sqrt(Q[0][0] + Q[1][1]) : NaN, sc = 0.55, cx = 340, cy = 270, g = '';
      g += ln(0, cy, 680, cy, BR, 2) + tx(20, cy + 16, '地面', 10, BR, 'start');
      S.forEach(function (s, j) { var R0 = solve ? rho[j] - x[2] : rho[j]; g += '<circle cx="' + n1(cx + s[0] * sc) + '" cy="' + n1(cy - s[1] * sc) + '" r="' + n1(R0 * sc) + '" fill="none" stroke="' + [BL, OR, PU][j] + '" stroke-width="1.6"/>' + '<rect x="' + n1(cx + s[0] * sc - 8) + '" y="' + n1(cy - s[1] * sc - 5) + '" width="16" height="10" fill="' + [BL, OR, PU][j] + '"/>' + tx(cx + s[0] * sc, cy - s[1] * sc - 10, '衛星 ' + (j + 1), 10, [BL, OR, PU][j]); });
      g += '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="' + GN + '"/>' + (solve ? '<circle cx="' + n1(cx + x[0] * sc) + '" cy="' + n1(cy - x[1] * sc) + '" r="7" fill="none" stroke="' + RD + '" stroke-width="2.5"/>' : '');
      v.innerHTML = svgw('0 0 680 300', g); var err = Math.hypot(x[0], x[1]);
      inf.innerHTML = (solve ? '以三個偽距同時解出 (x, y, 時鐘誤差)：時鐘誤差 = <b>' + x[2].toFixed(1) + ' m</b>，位置誤差 <b>' + err.toFixed(2) + ' m</b>（紅圈；綠點是真正位置）。扣掉時鐘誤差後，三個圓交於一點。' : '每個圓的半徑是「偽距」= 真實距離 + 時鐘誤差。時鐘誤差讓三個圓都一樣變大，<b>交不到同一點</b>。按「解出」，把時鐘誤差當成第三個未知數。') +
        '<br>這是二維的示意：未知數 (x, y, 時鐘) 需要 3 顆衛星；真實世界是三維，(x, y, z, 時鐘) 需要 <b>4 顆</b>。<br>幾何精度因子 HDOP ≈ <b>' + fx(dop, 2) + '</b>：衛星擠在同一個方向時（張角小），圓幾乎平行相交，小小的雜訊就會造成很大的位置誤差。'; }
    draw();
  }

  /* ---------- GNSS 精度比較 ---------- */
  var GM = { sp: ['單點定位', 3, '手機與車用導航：只用一台接收器'], dg: ['差分 DGPS', 0.5, '用附近基準站的改正量修正'], rtk: ['RTK', 0.02, '即時載波相位差分：公分級'], st: ['靜態後處理', 0.004, '長時間觀測、事後精密計算：毫米級'] };
  function initGnss(root, cfg) {
    head(root, cfg.q); var m = 'sp', seed = 1, v = el('div'), inf;
    bar(root, Object.keys(GM).map(function (k) { return [GM[k][0], k]; }), m, function (k) { m = k; draw(); }); var d = row(root); bt(d, '🎲 重新觀測', function () { seed++; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var s = GM[m][1], r = rng(seed * 3 + s * 1000), P = [], i, cx = 340, cy = 160, pix = 120 / (3 * s), g = '';
      for (i = 0; i < 200; i++) P.push([s * gs(r) * 0.7, s * gs(r) * 0.7]); var e = P.map(function (p) { return Math.hypot(p[0], p[1]); }).sort(function (a, b) { return a - b; }), cep = e[100], r95 = e[190];
      g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + n1(cep * pix) + '" fill="none" stroke="' + OR + '" stroke-width="2"/><circle cx="' + cx + '" cy="' + cy + '" r="' + n1(r95 * pix) + '" fill="none" stroke="' + RD + '" stroke-dasharray="5 4"/>';
      P.forEach(function (p) { g += '<circle cx="' + n1(cx + p[0] * pix) + '" cy="' + n1(cy - p[1] * pix) + '" r="2.5" fill="' + BL + '" fill-opacity="0.6"/>'; }); g += ln(cx - 6, cy, cx + 6, cy, GN, 2) + ln(cx, cy - 6, cx, cy + 6, GN, 2);
      var unit = s >= 1 ? [1, '1 m'] : s >= 0.1 ? [0.1, '10 cm'] : s >= 0.01 ? [0.01, '1 cm'] : [0.001, '1 mm']; g += ln(540, 290, 540 + unit[0] * pix, 290, '#333', 3) + tx(540 + unit[0] * pix / 2, 282, unit[1], 10, 'currentColor');
      v.innerHTML = svgw('0 0 680 305', g);
      inf.innerHTML = '<b>' + GM[m][0] + '</b>：' + GM[m][2] + '。200 次定位，有一半落在橘色圓內（半徑 <b>' + (cep < 0.1 ? (cep * 1000).toFixed(1) + ' mm' : cep.toFixed(2) + ' m') + '</b>），95% 落在紅色虛線內（' + (r95 < 0.1 ? (r95 * 1000).toFixed(1) + ' mm' : r95.toFixed(2) + ' m') + '）。<br>注意比例尺：四種方法的圖看起來差不多，但比例尺相差上千倍。'; }
    draw();
  }

  /* ---------- 等高線 ---------- */
  function initContour(root, cfg) {
    head(root, cfg.q); var ci = 5, seed = 4, prof = true, v = el('div'), inf, NX = 48, NY = 30;
    bar(root, [['等高距 1 m', 1], ['2 m', 2], ['5 m', 5], ['10 m', 10]], ci, function (k) { ci = k; draw(); }); var d = row(root); bt(d, '🎲 換一塊地形', function () { seed++; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var r = rng(seed * 17), G = [], hills = [], i, j; for (i = 0; i < 5; i++) hills.push([r() * NX, r() * NY, 15 + r() * 35, 5 + r() * 9, r() < 0.25 ? -1 : 1]);
      var tx0 = (r() - 0.5) * 0.6, ty0 = (r() - 0.5) * 0.6, mn = 1e9, mx = -1e9;
      for (j = 0; j <= NY; j++) { G.push([]); for (i = 0; i <= NX; i++) { var z = 120 + tx0 * i + ty0 * j; hills.forEach(function (h) { z += h[4] * h[2] * Math.exp(-((i - h[0]) * (i - h[0]) + (j - h[1]) * (j - h[1])) / (2 * h[3] * h[3])); }); G[j].push(z); mn = Math.min(mn, z); mx = Math.max(mx, z); } }
      var cs = 13, ox = 28, oy = 8, g = '';
      for (j = 0; j < NY; j++) for (i = 0; i < NX; i++) { var zc = (G[j][i] + G[j][i + 1] + G[j + 1][i] + G[j + 1][i + 1]) / 4, t = (zc - mn) / (mx - mn); g += '<rect x="' + (ox + i * cs) + '" y="' + (oy + j * cs) + '" width="' + (cs + 0.5) + '" height="' + (cs + 0.5) + '" fill="hsl(' + Math.round(120 - 100 * t) + ',45%,' + Math.round(78 - 20 * t) + '%)"/>'; }
      var lv = Math.ceil(mn / ci) * ci, nl = 0; for (; lv <= mx; lv += ci) { nl++; var idx = Math.round(lv / ci) % 5 === 0, path = '';
        for (j = 0; j < NY; j++) for (i = 0; i < NX; i++) { var c = [G[j][i], G[j][i + 1], G[j + 1][i + 1], G[j + 1][i]], P = [[i, j], [i + 1, j], [i + 1, j + 1], [i, j + 1]], pts = [];
          for (var e = 0; e < 4; e++) { var a = c[e], b = c[(e + 1) % 4]; if ((a < lv) !== (b < lv)) { var f = (lv - a) / (b - a), p0 = P[e], p1 = P[(e + 1) % 4]; pts.push([p0[0] + f * (p1[0] - p0[0]), p0[1] + f * (p1[1] - p0[1])]); } }
          if (pts.length >= 2) { path += 'M' + n1(ox + pts[0][0] * cs) + ' ' + n1(oy + pts[0][1] * cs) + 'L' + n1(ox + pts[1][0] * cs) + ' ' + n1(oy + pts[1][1] * cs); if (pts.length === 4) path += 'M' + n1(ox + pts[2][0] * cs) + ' ' + n1(oy + pts[2][1] * cs) + 'L' + n1(ox + pts[3][0] * cs) + ' ' + n1(oy + pts[3][1] * cs); } }
        g += '<path d="' + path + '" fill="none" stroke="#5b4630" stroke-width="' + (idx ? 1.8 : 0.7) + '"/>'; }
      var pj = Math.round(NY / 2), pr = []; for (i = 0; i <= NX; i++) pr.push([i * 10, G[pj][i]]); g += ln(ox, oy + pj * cs, ox + NX * cs, oy + pj * cs, RD, 1.5, 'stroke-dasharray="6 4"') + tx(ox + NX * cs - 4, oy + pj * cs - 5, 'A–A′ 剖面', 10, RD, 'end');
      v.innerHTML = svgw('0 0 680 ' + (oy * 2 + NY * cs), g) + chart(680, 170, [{ d: pr, c: BR }], { x0: 0, x1: NX * 10, y0: Math.floor(mn / 10) * 10, y1: Math.ceil(mx / 10) * 10, xl: '沿 A–A′ 的距離（m）', yl: '高程 m' });
      inf.innerHTML = '等高距 ' + ci + ' m，共 ' + nl + ' 條等高線；粗線是每 ' + (5 * ci) + ' m 一條的<b>計曲線</b>。最高 ' + mx.toFixed(1) + ' m、最低 ' + mn.toFixed(1) + ' m。<br>讀圖：<b>線越密越陡</b>；閉合的同心圈是山頂（或窪地）；線往高處凸是山谷、往低處凸是山脊。下方是沿紅色虛線切開的地形剖面。'; }
    draw();
  }

  /* ---------- 方格法土方 ---------- */
  function initEarth(root, cfg) {
    head(root, cfg.q); var NXc = 5, NYc = 4, a = 20, seed = 6, Hd = 50, H = [], v = el('div'), inf;
    slider(root, '設計（整地）高程（m）', 44, 58, 0.01, Hd, function (x) { return x.toFixed(2); }, 'h', function (x) { Hd = x; draw(); });
    var d = row(root); bt(d, '設為挖填平衡的高程', function () { setS(root, 'h', bal().toFixed(2)); }); bt(d, '🎲 換一塊地', function () { seed++; gen(); setS(root, 'h', 50); });
    root.appendChild(v); inf = info(root);
    function gen() { var r = rng(seed * 23); H = []; var sx = (r() - 0.5) * 0.25, sy = (r() - 0.5) * 0.25; for (var j = 0; j <= NYc; j++) { H.push([]); for (var i = 0; i <= NXc; i++) H[j].push(Math.round((50 + sx * i * a + sy * j * a + (r() - 0.5) * 3) * 100) / 100); } }
    function w(i, j) { return (i === 0 || i === NXc ? 1 : 2) * (j === 0 || j === NYc ? 1 : 2); }
    function bal() { var s = 0, ws = 0; for (var j = 0; j <= NYc; j++) for (var i = 0; i <= NXc; i++) { s += w(i, j) * H[j][i]; ws += w(i, j); } return s / ws; }
    function draw() { var cut = 0, fill = 0, cs = 104, ox = 50, oy = 24, g = '', i, j;
      for (j = 0; j < NYc; j++) for (i = 0; i < NXc; i++) { var hs = [H[j][i], H[j][i + 1], H[j + 1][i], H[j + 1][i + 1]].map(function (h) { return h - Hd; }), c = 0, f = 0; hs.forEach(function (x) { if (x > 0) c += x; else f -= x; }); c *= a * a / 4; f *= a * a / 4; cut += c; fill += f;
        var net = c - f; g += '<rect x="' + (ox + i * cs) + '" y="' + (oy + j * cs) + '" width="' + cs + '" height="' + cs + '" fill="' + (net > 0 ? RD : BL) + '" fill-opacity="' + Math.min(0.55, Math.abs(net) / 1500 + 0.06).toFixed(2) + '" stroke="' + GY + '"/>' + tx(ox + i * cs + cs / 2, oy + j * cs + cs / 2 + 4, (net > 0 ? '挖 ' : '填 ') + Math.abs(net).toFixed(0), 10, 'currentColor'); }
      for (j = 0; j <= NYc; j++) for (i = 0; i <= NXc; i++) { var dh = H[j][i] - Hd; g += '<circle cx="' + (ox + i * cs) + '" cy="' + (oy + j * cs) + '" r="3" fill="#333"/>' + tx(ox + i * cs + 4, oy + j * cs - 5, H[j][i].toFixed(2), 9, 'currentColor', 'start') + tx(ox + i * cs + 4, oy + j * cs + 13, (dh >= 0 ? '+' : '') + dh.toFixed(2), 9, dh >= 0 ? RD : BL, 'start'); }
      v.innerHTML = svgw('0 0 680 ' + (oy * 2 + NYc * cs), g);
      inf.innerHTML = '每格 ' + a + ' m × ' + a + ' m；黑字是現況高程，紅／藍字是與設計高程的差（+ 要挖、− 要填）。每格的量 ≈ 面積 × 四角高差平均（挖、填分開計算的近似）。<br>挖方 <b style="color:' + RD + '">' + cut.toFixed(0) + ' m³</b>、填方 <b style="color:' + BL + '">' + fill.toFixed(0) + ' m³</b>，淨值 ' + (cut - fill >= 0 ? '多出 ' + (cut - fill).toFixed(0) + ' m³ 要運走' : '不足 ' + (fill - cut).toFixed(0) + ' m³ 要運進來') + '。<br>挖填平衡高程 = Σ(權重 × 高程) / Σ權重 = <b>' + bal().toFixed(2) + ' m</b>（角點權重 1、邊點 2、內點 4，即每個點被幾格共用）。'; }
    gen(); draw();
  }

  /* ---------- 圓曲線放樣 ---------- */
  function initCurve(root, cfg) {
    head(root, cfg.q); var R = 300, De = 40, st = 20, BC = 1234.56, v = el('div'), inf;
    slider(root, '半徑 R（m）', 50, 1000, 5, R, function (x) { return x + ' m'; }, 'r', function (x) { R = x; draw(); }); slider(root, '交角 Δ（度）', 5, 120, 0.5, De, function (x) { return x + '°'; }, 'd', function (x) { De = x; draw(); });
    bar(root, [['每 20 m 一樁', 20], ['每 10 m 一樁', 10]], st, function (k) { st = k; draw(); }); root.appendChild(v); inf = info(root);
    function sta(m) { var k = Math.floor(m / 1000), r = m - k * 1000; return k + '+' + (r < 100 ? (r < 10 ? '00' : '0') : '') + r.toFixed(2); }
    function draw() { var d = De * Math.PI / 180, T = R * Math.tan(d / 2), L = R * d, E = R * (1 / Math.cos(d / 2) - 1), Mm = R * (1 - Math.cos(d / 2)), LC = 2 * R * Math.sin(d / 2), EC = BC + L;
      var list = [BC], m = Math.ceil(BC / st) * st; if (m - BC < 1e-6) m += st; for (; m < EC - 1e-6; m += st) list.push(m); list.push(EC);
      var rows = list.map(function (s) { var l = s - BC, dl = l / (2 * R) * 180 / Math.PI, ch = 2 * R * Math.sin(l / (2 * R)); return '<tr>' + cell(s === BC ? 'BC ' + sta(s) : s === EC ? 'EC ' + sta(s) : sta(s), 'text-align:left') + cell(l.toFixed(2)) + cell(dms(dl)) + cell(ch.toFixed(3)) + '</tr>'; });
      var cd = Math.cos(d / 2), sc = Math.min(560 / LC, 190 / (R * (1 / cd - cd))), Rs = R * sc, Yc = 30 + Rs / cd, g = MK;
      var P = function (t) { var th = -d / 2 + t; return [340 + Rs * Math.sin(th), Yc - Rs * Math.cos(th)]; }, A = P(0), B = P(d), PI = [340, 30], pts = '';
      for (var t = 0; t <= d + 1e-9; t += d / 60) { var p = P(t); pts += n1(p[0]) + ',' + n1(p[1]) + ' '; }
      var ext = function (Q) { var dx = Q[0] - PI[0], dy = Q[1] - PI[1], L0 = Math.hypot(dx, dy); return [Q[0] + dx / L0 * 50, Q[1] + dy / L0 * 50]; }, eA = ext(A), eB = ext(B);
      g += ln(eA[0], eA[1], PI[0], PI[1], GY, 1.5, 'stroke-dasharray="6 4"') + ln(eB[0], eB[1], PI[0], PI[1], GY, 1.5, 'stroke-dasharray="6 4"');
      g += ln(A[0], A[1], B[0], B[1], PU, 1, 'stroke-dasharray="3 3"') + '<polyline points="' + pts + '" fill="none" stroke="' + BL + '" stroke-width="3"/>';
      list.forEach(function (s2) { var pp = P((s2 - BC) / R); g += '<circle cx="' + n1(pp[0]) + '" cy="' + n1(pp[1]) + '" r="3.5" fill="' + OR + '"/>'; });
      g += tx(A[0], A[1] + 18, 'BC', 11, GN) + tx(B[0], B[1] + 18, 'EC', 11, RD) + tx(PI[0], PI[1] - 8, 'PI', 11, 'currentColor') + tx(340, A[1] + 16, '長弦 LC', 10, PU);
      var oy = Math.max(A[1] + 10, eA[1] - 10);
      v.innerHTML = svgw('0 0 680 ' + Math.max(170, oy + 30), g) + tbl(['樁號', '距 BC 弧長', '偏角 δ = l/2R', '自 BC 的弦長'], rows);
      inf.innerHTML = '切線長 T = R·tan(Δ/2) = <b>' + T.toFixed(3) + ' m</b>；曲線長 L = RΔ = <b>' + L.toFixed(3) + ' m</b>；外距 E = ' + E.toFixed(3) + ' m；中距 M = ' + Mm.toFixed(3) + ' m；長弦 LC = ' + LC.toFixed(3) + ' m。<br>' +
        '假設 BC 在樁號 ' + sta(BC) + '，則 EC = BC + L = <b>' + sta(EC) + '</b>（注意 EC 不是 PI + T，因為曲線比兩條切線短）。<br>偏角法放樣：儀器架在 BC、後視 PI，依序轉表中的偏角，量出弦長就是每一支樁的位置。'; }
    draw();
  }

  var INIT = { bubble: initBubble, errsim: initErrsim, edm: initEdm, curv: initCurv, level: initLevel, coord: initCoord, traverse: initTraverse, gps: initGps, gnss: initGnss, contour: initContour, earth: initEarth, curve: initCurve };
  function boot() { document.querySelectorAll('.svy-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"📐", note=SVY_NOTE):
    return make_with(icon, note, [("svy-w", SVYLIB)])


lesson = make()
