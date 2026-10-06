# -*- coding: utf-8 -*-
"""〈衛星通訊〉（sc_）共用工具與互動元件（SCLIB）。"""
import json
from cc_common import *
from qt_common import BASEJS
from lg_geo import WORLD

SC_NOTE = (u"本課的衛星數量、速度、價格等數字以 2024～2025 年前後的公開資料為準，變化很快；鏈路預算、雨衰等互動工具使用簡化模型，"
           u"只用來理解量級與趨勢，不能取代正式的工程設計。")

SCLIB = r"""
(function () {
  if (window.__scLib) return; window.__scLib = 1;
""" + BASEJS + r"""
  var WORLD = __WORLD__, RE = 6371, MU = 398600.4418, CK = 299792.458, D2R = Math.PI / 180;
  function info(root) { var p = el('p', 'margin:6px 0 0;line-height:1.65'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function lg(v) { return Math.log(v) / Math.LN10; }
  function fmtk(v) { return v >= 10000 ? Math.round(v).toLocaleString() : v >= 100 ? Math.round(v).toString() : f1(v); }
  function lam(h, e) { e *= D2R; return Math.acos(RE * Math.cos(e) / (RE + h)) - e; }
  function slant(h, e) { e *= D2R; return Math.sqrt(Math.pow(RE + h, 2) - Math.pow(RE * Math.cos(e), 2)) - RE * Math.sin(e); }
  function gauss(r) { var u = 1 - r(), v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  function rng(seed) { var s = seed >>> 0; return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }

  /* ---------- 軌道高度 ---------- */
  var PRE = [['國際太空站', 420], ['Starlink', 550], ['銥衛星', 780], ['福衛五號', 720], ['O3b（中軌）', 8062], ['GPS', 20200], ['地球同步', 35786]];
  function initOrbit(root, cfg) {
    head(root, cfg.q); var h = cfg.h || 550, el0 = 25, bb = bar(root), view = el('div'), p, u;
    PRE.forEach(function (q) { var b = btn(q[0], q[1]); b.addEventListener('click', function () { h = q[1]; root.querySelector('input[data-k=h]').value = lg(h); u(); }); bb.appendChild(b); });
    u = slider(root, '軌道高度', lg(200), lg(40000), 0.0005, lg(h), function (v) { return fmtk(Math.pow(10, v)) + ' 公里'; }, 'h', function (v) { h = Math.round(Math.pow(10, v)); draw(); }); root.querySelector('input[data-k=h]').step = 0.0005;
    var u2 = slider(root, '地面天線最低仰角', 0, 60, 1, el0, function (v) { return v + '°'; }, 'e', function (v) { el0 = v; draw(); });
    root.appendChild(view); p = info(root);
    function draw() { mark(bb, h); var a = RE + h, T = 2 * Math.PI * Math.sqrt(a * a * a / MU), v = Math.sqrt(MU / a), L = lam(h, el0), sr = slant(h, el0), frac = (1 - Math.cos(L)) / 2;
      var sc = 120 / a, cx = 200, cy = 150, o = '', r = RE * sc;
      o += '<circle cx="' + cx + '" cy="' + cy + '" r="' + n1(a * sc) + '" fill="none" stroke="#999" stroke-dasharray="4 3"/>';
      var sx = cx, sy = cy - a * sc, lx = cx + r * Math.sin(L), ly = cy - r * Math.cos(L), rx = cx - r * Math.sin(L);
      o += '<path d="M' + n1(sx) + ',' + n1(sy) + 'L' + n1(lx) + ',' + n1(ly) + 'L' + n1(rx) + ',' + n1(ly) + 'Z" fill="#d9822b" fill-opacity="0.18" stroke="#d9822b" stroke-width="0.8"/>';
      o += '<circle cx="' + cx + '" cy="' + cy + '" r="' + n1(r) + '" fill="#3a6ea5" fill-opacity="0.85"/>';
      o += '<path d="M' + n1(rx) + ',' + n1(ly) + 'A' + n1(r) + ',' + n1(r) + ' 0 0 1 ' + n1(lx) + ',' + n1(ly) + '" fill="none" stroke="#e8b84a" stroke-width="4"/>';
      o += '<circle cx="' + n1(sx) + '" cy="' + n1(sy) + '" r="5" fill="#d0564f"/>' + tx(sx + 8, sy - 4, '衛星', 10, '#d0564f', 'start');
      var rows = [['高度', fmtk(h) + ' 公里'], ['繞地球一圈', T >= 3600 * 3 ? f1(T / 3600) + ' 小時' : f1(T / 60) + ' 分鐘'], ['速度', f2(v) + ' 公里／秒（時速約 ' + Math.round(v * 3600).toLocaleString() + ' 公里）'],
        ['一天繞幾圈', f1(86164 / T)], ['覆蓋範圍半徑', Math.round(L * RE).toLocaleString() + ' 公里（地表弧長）'], ['覆蓋地球表面', f1(frac * 100) + '%'],
        ['到覆蓋邊緣的距離', Math.round(sr).toLocaleString() + ' 公里'], ['單程延遲（正下方～邊緣）', f1(h / CK * 1000) + '～' + f1(sr / CK * 1000) + ' 毫秒'],
        ['同時覆蓋全球至少約', Math.max(1, Math.ceil(1.6 / frac)) + ' 顆（粗估）']];
      rows.forEach(function (q, i) { o += tx(360, 40 + i * 25, q[0], 11, 'var(--text-muted)', 'start') + tx(500, 40 + i * 25, q[1], 11, 'currentColor', 'start'); });
      view.innerHTML = svgw('0 0 720 290', o);
      p.innerHTML = Math.abs(T - 86164) < 600 ? '這個高度的週期剛好約等於地球自轉一圈（23 小時 56 分），衛星從地面看起來<b>靜止不動</b>——這就是地球同步軌道。' :
        h < 2000 ? '低軌衛星離地近：延遲短、訊號強，但每顆只能看到一小塊地球，而且約 ' + Math.round(T / 60) + ' 分鐘就繞一圈，從地面看每次只經過幾分鐘，所以需要很多顆接力。' :
        '越高，週期越長、速度越慢、看到的地球越大，但距離遠、訊號弱、延遲長。'; }
    u(); u2();
  }

  /* ---------- 鏈路預算與雨衰 ---------- */
  var KA = [[1, 0.0000387, 0.912], [4, 0.00065, 1.121], [6, 0.00175, 1.308], [10, 0.0101, 1.276], [12, 0.0188, 1.217], [15, 0.0367, 1.154], [20, 0.0751, 1.099], [30, 0.187, 1.021], [40, 0.35, 0.939]];
  function kalpha(f) { for (var i = 1; i < KA.length; i++) if (f <= KA[i][0]) { var a = KA[i - 1], b = KA[i], t = (lg(f) - lg(a[0])) / (lg(b[0]) - lg(a[0])); return [Math.pow(10, lg(a[1]) + t * (lg(b[1]) - lg(a[1]))), a[2] + t * (b[2] - a[2])]; } return [KA[KA.length - 1][1], KA[KA.length - 1][2]]; }
  function rainA(f, R, e) { if (R <= 0) return 0; var ka = kalpha(f), g = ka[0] * Math.pow(R, ka[1]), Ls = 4.5 / Math.sin(Math.max(e, 5) * D2R), LG = Ls * Math.cos(Math.max(e, 5) * D2R), r = 1 / (1 + LG / (35 * Math.exp(-0.015 * Math.min(R, 100)))); return g * Ls * r; }
  var LP = { geo: ['地球同步衛星電視（Ku 頻段）', 12, 35786, 52, 0.6, 36, 30], leo: ['低軌寬頻（Ku 頻段，類似 Starlink）', 12, 550, 38, 0.5, 240, 50], ka: ['地球同步 Ka 頻段寬頻', 20, 35786, 58, 0.75, 250, 35] };
  function initLink(root, cfg) {
    head(root, cfg.q); var st = { f: 12, h: 35786, eirp: 52, D: 0.6, B: 36, el: 30, R: 0, T: 150 }, bb = bar(root), view = el('div'), p, us = [];
    Object.keys(LP).forEach(function (k) { var b = btn(LP[k][0], k); b.addEventListener('click', function () { var q = LP[k]; st.f = q[1]; st.h = q[2]; st.eirp = q[3]; st.D = q[4]; st.B = q[5]; st.el = q[6];
      ['f', 'h', 'eirp', 'D', 'B', 'el'].forEach(function (key) { var i = root.querySelector('input[data-k=' + key + ']'); i.value = key === 'h' ? lg(st.h) : key === 'B' ? lg(st.B) : st[key]; }); mark(bb, k); us.forEach(function (f) { f(); }); }); bb.appendChild(b); });
    us.push(slider(root, '頻率', 1, 40, 0.5, st.f, function (v) { return v + ' GHz'; }, 'f', function (v) { st.f = v; draw(); }));
    us.push(slider(root, '衛星高度', lg(300), lg(36000), 0.0005, lg(st.h), function (v) { return fmtk(Math.pow(10, v)) + ' 公里'; }, 'h', function (v) { st.h = Math.pow(10, v); draw(); }));
    us.push(slider(root, '衛星發射功率＋天線增益（EIRP）', 20, 65, 1, st.eirp, function (v) { return v + ' dBW'; }, 'eirp', function (v) { st.eirp = v; draw(); }));
    us.push(slider(root, '地面碟形天線直徑', 0.2, 3, 0.05, st.D, function (v) { return f2(v) + ' 公尺'; }, 'D', function (v) { st.D = v; draw(); }));
    us.push(slider(root, '頻寬', 0, lg(500), 0.01, lg(st.B), function (v) { return fmtk(Math.pow(10, v)) + ' MHz'; }, 'B', function (v) { st.B = Math.pow(10, v); draw(); }));
    us.push(slider(root, '仰角', 5, 90, 1, st.el, function (v) { return v + '°'; }, 'el', function (v) { st.el = v; draw(); }));
    us.push(slider(root, '降雨強度', 0, 150, 1, st.R, function (v) { return v + ' 毫米／小時' + (v === 0 ? '（晴天）' : v < 10 ? '（小雨）' : v < 40 ? '（大雨）' : '（豪雨、午後雷陣雨）'); }, 'R', function (v) { st.R = v; draw(); }));
    root.appendChild(view); p = info(root); mark(bb, 'geo');
    function draw() { var d = slant(st.h, st.el), fspl = 20 * lg(d) + 20 * lg(st.f) + 92.45, G = 10 * lg(0.6 * Math.pow(Math.PI * st.D * st.f * 1e9 / 3e8, 2)), A = rainA(st.f, st.R, st.el),
        Tn = st.T + 280 * (1 - Math.pow(10, -A / 10)), cn0 = st.eirp - fspl - A + G - 10 * lg(Tn) + 228.6, cn = cn0 - 10 * lg(st.B * 1e6), cap = st.B * Math.log(1 + Math.pow(10, cn / 10)) / Math.LN2;
      var items = [['EIRP（衛星送出）', st.eirp, '#4a9a5e'], ['自由空間路徑損耗', -fspl, '#d0564f'], ['雨衰', -A, '#d9822b'], ['地面天線增益', G, '#3a6ea5'], ['雜訊溫度 −10log T', -10 * lg(Tn), '#8a5cb8'], ['波茲曼常數項', 228.6, '#999'], ['頻寬 −10log B', -10 * lg(st.B * 1e6), '#8a5cb8']];
      var o = '', run = 0, lo = 0, hi = 0; items.forEach(function (q) { run += q[1]; lo = Math.min(lo, run); hi = Math.max(hi, run); }); run = 0;
      var s = 420 / (hi - lo), x0 = 285 - lo * s; items.push(['結果 C/N', 0, 'currentColor']);
      items.forEach(function (q, i) { var y = 14 + i * 26, a = x0 + run * s, b = x0 + (run + q[1]) * s; if (i === items.length - 1) { a = x0; b = x0 + run * s; q[1] = run; run = 0; } o += tx(190, y + 13, q[0], 11, 'currentColor', 'end') + tx(198, y + 13, (q[1] >= 0 ? '+' : '') + f1(q[1]) + ' dB', 10, q[2], 'start');
        o += '<rect x="' + n1(Math.min(a, b)) + '" y="' + y + '" width="' + n1(Math.abs(b - a)) + '" height="17" fill="' + q[2] + '" fill-opacity="0.8"/>'; run += q[1]; });
      o += ln(x0, 6, x0, 226, '#999') + tx(x0, 238, '0 dB', 9, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 720 245', o);
      p.innerHTML = '距離 <b>' + Math.round(d).toLocaleString() + '</b> 公里，訊號在路上衰減 <b>' + f1(fspl) + ' dB</b>（約剩 10<sup>−' + Math.round(fspl / 10) + '</sup>）' + (A > 0.05 ? '，雨衰再扣 <b>' + f1(A) + ' dB</b>' : '') + '。' +
        '<br>最後的訊號雜訊比 C/N ＝ <b>' + f1(cn) + ' dB</b> → ' + (cn < 0 ? '<b style="color:#d0564f">訊號比雜訊還弱，大多數系統斷訊</b>' : cn < 5 ? '<b style="color:#d9822b">勉強，只能用很保守的調變</b>' : '<b style="color:#4a9a5e">可以穩定接收</b>') +
        '；夏農上限約 <b>' + (cap >= 1000 ? f2(cap / 1000) + ' Gbps' : f1(cap) + ' Mbps') + '</b>。' +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">簡化模型：天線效率 60%、接收系統雜訊溫度 150 K；雨衰採 ITU 的 k、α 係數近似，雨層高度 4.5 公里，未考慮大氣吸收、指向誤差與干擾。</span>'; }
    us.forEach(function (f) { f(); });
  }

  /* ---------- 星系覆蓋 ---------- */
  var CP = { sl: ['類似 Starlink 一層', 72, 22, 550, 53], ow: ['類似 OneWeb', 18, 36, 1200, 87.9], ir: ['銥衛星', 6, 11, 780, 86.4], gps: ['GPS', 6, 4, 20200, 55] };
  function initConst(root, cfg) {
    head(root, cfg.q); var st = { P: 72, S: 22, h: 550, i: 53, t: 0, e: 25 }, bb = bar(root), view = el('div'), p, us = [];
    Object.keys(CP).forEach(function (k) { var b = btn(CP[k][0], k); b.addEventListener('click', function () { var q = CP[k]; st.P = q[1]; st.S = q[2]; st.h = q[3]; st.i = q[4];
      root.querySelector('input[data-k=P]').value = st.P; root.querySelector('input[data-k=S]').value = st.S; root.querySelector('input[data-k=h]').value = lg(st.h); root.querySelector('input[data-k=i]').value = st.i; mark(bb, k); us.forEach(function (f) { f(); }); }); bb.appendChild(b); });
    us.push(slider(root, '軌道面數', 1, 80, 1, st.P, function (v) { return v; }, 'P', function (v) { st.P = v; draw(); }));
    us.push(slider(root, '每個軌道面的衛星數', 1, 40, 1, st.S, function (v) { return v; }, 'S', function (v) { st.S = v; draw(); }));
    us.push(slider(root, '高度', lg(300), lg(36000), 0.0005, lg(st.h), function (v) { return fmtk(Math.pow(10, v)) + ' 公里'; }, 'h', function (v) { st.h = Math.pow(10, v); draw(); }));
    us.push(slider(root, '軌道傾角', 0, 98, 0.5, st.i, function (v) { return v + '°'; }, 'i', function (v) { st.i = v; draw(); }));
    us.push(slider(root, '時間', 0, 120, 1, st.t, function (v) { return v + ' 分鐘'; }, 't', function (v) { st.t = v; draw(); }));
    root.appendChild(view); p = info(root); mark(bb, 'sl');
    function sats() { var a = RE + st.h, n = 2 * Math.PI / Math.sqrt(a * a * a / MU), out = [], inc = st.i * D2R, we = 2 * Math.PI / 86164;
      for (var pl = 0; pl < st.P; pl++) { var raan = pl / st.P * 2 * Math.PI; for (var s = 0; s < st.S; s++) { var u = s / st.S * 2 * Math.PI + pl * 2 * Math.PI / (st.P * st.S) + n * st.t * 60;
        var x = Math.cos(u), y = Math.sin(u) * Math.cos(inc), z = Math.sin(u) * Math.sin(inc), X = x * Math.cos(raan) - y * Math.sin(raan), Y = x * Math.sin(raan) + y * Math.cos(raan);
        var lat = Math.asin(z), lon = Math.atan2(Y, X) - we * st.t * 60; lon = ((lon / D2R + 540) % 360) - 180; out.push([lat / D2R, lon]); } } return out; }
    function P2(lon, lat) { return [(lon + 180) * 2, (80 - Math.max(-60, Math.min(80, lat))) * 2]; }
    function draw() { var ss = sats(), L = lam(st.h, st.e), o = '<rect width="720" height="280" fill="#dfeaf5"/><path d="' + WORLD + '" fill="#c9d1c3" stroke="#fff" stroke-width="0.3"/>', cov = 0, tot = 0, tw = 0;
      var cl = Math.cos(L), pts = ss.map(function (q) { var la = q[0] * D2R, lo = q[1] * D2R; return [Math.cos(la) * Math.cos(lo), Math.cos(la) * Math.sin(lo), Math.sin(la)]; });
      for (var la = -87.5; la < 90; la += 5) for (var lo = -177.5; lo < 180; lo += 5) { var w = Math.cos(la * D2R), v = [Math.cos(la * D2R) * Math.cos(lo * D2R), Math.cos(la * D2R) * Math.sin(lo * D2R), Math.sin(la * D2R)], hit = 0;
        for (var k = 0; k < pts.length; k++) if (pts[k][0] * v[0] + pts[k][1] * v[1] + pts[k][2] * v[2] >= cl) { hit = 1; break; } tot += w; cov += hit * w;
        if (!hit && la > -60 && la < 80) { var a = P2(lo, la); o += '<rect x="' + n1(a[0] - 5) + '" y="' + n1(a[1] - 5) + '" width="10" height="10" fill="#d0564f" fill-opacity="0.18"/>'; } }
      var twv = [Math.cos(23.7 * D2R) * Math.cos(121 * D2R), Math.cos(23.7 * D2R) * Math.sin(121 * D2R), Math.sin(23.7 * D2R)];
      pts.forEach(function (q) { if (q[0] * twv[0] + q[1] * twv[1] + q[2] * twv[2] >= cl) tw++; });
      var many = ss.length > 300;
      ss.forEach(function (q) { if (!many) { var ring = []; var la0 = q[0] * D2R, lo0 = q[1] * D2R; for (var j = 0; j <= 24; j++) { var b = j / 24 * 2 * Math.PI, la1 = Math.asin(Math.sin(la0) * Math.cos(L) + Math.cos(la0) * Math.sin(L) * Math.cos(b)), lo1 = lo0 + Math.atan2(Math.sin(b) * Math.sin(L) * Math.cos(la0), Math.cos(L) - Math.sin(la0) * Math.sin(la1)); ring.push([((lo1 / D2R + 540) % 360) - 180, la1 / D2R]); }
          var seg = '', prev = null; ring.forEach(function (r) { var a = P2(r[0], r[1]); seg += (prev && Math.abs(r[0] - prev[0]) < 180 ? 'L' : 'M') + n1(a[0]) + ',' + n1(a[1]); prev = r; }); o += '<path d="' + seg + '" fill="none" stroke="#3a6ea5" stroke-width="0.7" stroke-opacity="0.7"/>'; }
        if (q[0] > -60 && q[0] < 80) { var a = P2(q[1], q[0]); o += '<circle cx="' + n1(a[0]) + '" cy="' + n1(a[1]) + '" r="' + (many ? 1.4 : 2.5) + '" fill="#d0564f"/>'; } });
      var tp = P2(121, 23.7); o += '<circle cx="' + n1(tp[0]) + '" cy="' + n1(tp[1]) + '" r="4" fill="none" stroke="#111" stroke-width="1.5"/>';
      view.innerHTML = svgw('0 0 720 280', o);
      p.innerHTML = '共 <b>' + ss.length.toLocaleString() + '</b> 顆衛星，每顆覆蓋半徑約 ' + Math.round(L * RE).toLocaleString() + ' 公里（最低仰角 25°）。此刻覆蓋地球表面約 <b>' + Math.round(cov / tot * 100) + '%</b>（淡紅色格子是沒有衛星看得到的地方）；台灣（黑圈）上空看得到 <b>' + tw + '</b> 顆。' +
        (st.i < 60 ? '<br>傾角 ' + st.i + '° 的軌道到不了高緯度，所以南北極附近沒有覆蓋。' : '') + '<br><span style="font-size:0.88em;color:var(--text-muted)">簡化的圓軌道與均勻分布（Walker 星系），只用來比較量級。衛星數多時不畫覆蓋圈。</span>'; }
    us.forEach(function (f) { f(); });
  }

  /* ---------- QAM 星座圖 ---------- */
  function initQAM(root, cfg) {
    head(root, cfg.q); var M = cfg.m || 16, snr = 18, bb = bar(root), view = el('div'), p;
    [[4, 'QPSK（4 點）'], [16, '16-QAM'], [64, '64-QAM'], [256, '256-QAM']].forEach(function (q) { var b = btn(q[1], q[0]); b.addEventListener('click', function () { M = q[0]; mark(bb, M); draw(); }); bb.appendChild(b); });
    var u = slider(root, '訊號雜訊比（每個符號）', 0, 40, 0.5, snr, function (v) { return v + ' dB'; }, 'snr', function (v) { snr = v; draw(); });
    root.appendChild(view); p = info(root); mark(bb, M);
    function draw() { var m = Math.round(Math.sqrt(M)), lv = [], E = 0; for (var i = 0; i < m; i++) lv.push(2 * i - m + 1); lv.forEach(function (a) { lv.forEach(function (b) { E += a * a + b * b; }); }); E /= M;
      var sig = Math.sqrt(E / Math.pow(10, snr / 10) / 2), r = rng(7), err = 0, N = 1500, o = '', sc = 250 / (m + 1) / 2 * 0.95, cx = 140, cy = 140;
      o += ln(cx - 128, cy, cx + 128, cy, 'var(--border)') + ln(cx, cy - 128, cx, cy + 128, 'var(--border)');
      for (var k = 0; k < N; k++) { var ia = Math.floor(r() * m), qa = Math.floor(r() * m), x = lv[ia] + sig * gauss(r), y = lv[qa] + sig * gauss(r), di = Math.max(0, Math.min(m - 1, Math.round((x + m - 1) / 2))), dq = Math.max(0, Math.min(m - 1, Math.round((y + m - 1) / 2)));
        var bad = di !== ia || dq !== qa; if (bad) err++; if (k < 1200) o += '<circle cx="' + n1(cx + x * sc) + '" cy="' + n1(cy - y * sc) + '" r="1.3" fill="' + (bad ? '#d0564f' : '#3a6ea5') + '" fill-opacity="0.6"/>'; }
      lv.forEach(function (a) { lv.forEach(function (b) { o += '<circle cx="' + n1(cx + a * sc) + '" cy="' + n1(cy - b * sc) + '" r="' + (M > 64 ? 1.6 : 3) + '" fill="#111"/>'; }); });
      o += tx(cx + 132, cy + 4, 'I', 10, 'var(--text-muted)', 'start') + tx(cx, cy - 132, 'Q', 10, 'var(--text-muted)');
      var bits = Math.log(M) / Math.LN2, ser = err / N;
      o += tx(320, 50, '每個符號帶 ' + bits + ' 位元', 13, 'currentColor', 'start') + tx(320, 80, '符號錯誤率約 ' + (ser === 0 ? '< 0.1%' : f1(ser * 100) + '%'), 13, ser > 0.05 ? '#d0564f' : ser > 0.001 ? '#d9822b' : '#4a9a5e', 'start');
      o += tx(320, 110, '藍點：判斷正確；紅點：誤判成鄰近的點', 10.5, 'var(--text-muted)', 'start');
      view.innerHTML = svgw('0 0 640 285', o);
      p.innerHTML = '黑點是理想位置，雜訊讓收到的點散開。點越密（' + M + ' 個點），每個符號能帶越多位元，但點之間的距離越近，就需要越高的訊號雜訊比才不會誤判。' +
        '衛星訊號弱，所以常用 QPSK、8PSK；訊號好的時候系統會自動換成更高階的調變（自適應調變）。'; }
    u();
  }

  /* ---------- 延遲比較 ---------- */
  function initLat(root, cfg) {
    head(root, cfg.q); var D = cfg.d || 10000, view = el('div'), p;
    var u = slider(root, '兩地距離（地表）', 100, 20000, 100, D, function (v) { return v.toLocaleString() + ' 公里'; }, 'd', function (v) { D = v; draw(); });
    root.appendChild(view); p = info(root);
    function draw() { var geoUp = slant(35786, 30), rows = [
        ['海底光纖（路線約繞 1.3 倍）', 2 * D * 1.3 / 204190 * 1000 + 2, '#4a9a5e'],
        ['地球同步衛星（一跳）', 4 * geoUp / CK * 1000 + 2 * D * 0.3 / 204190 * 1000 + 30, '#d0564f'],
        ['中軌衛星（O3b，8,062 公里）', 4 * slant(8062, 30) / CK * 1000 + 2 * D * 0.6 / 204190 * 1000 + 15, '#d9822b'],
        ['低軌＋雷射星間鏈路（550 公里）', 2 * (2 * slant(550, 40) + D * 1.15 * (RE + 550) / RE) / CK * 1000 + 20, '#3a6ea5']], mx = 650, o = '';
      rows.forEach(function (q, i) { var y = 16 + i * 46, w = Math.min(q[1], mx) / mx * 420; o += tx(10, y + 12, q[0], 10.5, 'currentColor', 'start') + '<rect x="10" y="' + (y + 18) + '" width="' + n1(Math.max(w, 2)) + '" height="16" rx="3" fill="' + q[2] + '"/>' + tx(16 + w, y + 31, Math.round(q[1]) + ' 毫秒', 10.5, 'currentColor', 'start'); });
      view.innerHTML = svgw('0 0 640 200', o);
      p.innerHTML = '這是<b>來回延遲</b>（RTT）的粗估。地球同步衛星距離約 3.6 萬公里，訊號上下兩趟、來回四趟，光是傳播就要近 0.5 秒，打電話會「卡卡的」、玩線上遊戲很吃虧。' +
        '<br>光在真空中比在光纖中快約 47%，所以距離很遠時，低軌衛星用雷射在太空中接力，延遲可能比光纖還短。<br><span style="font-size:0.88em;color:var(--text-muted)">已加上簡化的處理與排隊時間；實際延遲依網路路由、壅塞與閘道站位置而定。</span>'; }
    u();
  }

  function initAll() { document.querySelectorAll('.sc-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ orbit: initOrbit, link: initLink, cons: initConst, qam: initQAM, lat: initLat })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
""".replace("__WORLD__", json.dumps(WORLD))


def scw(cfg, maxw=720):
    return wdg("sc-w", cfg, maxw)


sclesson = make_lesson(u"🛰️", SC_NOTE, SCLIB, "sc-w")
