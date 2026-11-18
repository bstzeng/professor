# -*- coding: utf-8 -*-
"""〈GPU 與平行運算〉（gpu_）共用：課程包裝與 GPULIB 互動元件（class="gpu-w"）。

  amdahl  阿姆達定律：可平行的比例與核心數
  warp    warp 與分支發散
  roof    Roofline 模型：運算強度與效能上限
  tile    矩陣乘法的 tiling：全域記憶體讀取量
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

GPU_NOTE = u"互動模擬為教學用的簡化模型；硬體數字為代表性的量級，實際依產品與世代而異。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def gw(cfg, maxw=680):
    return wdg("gpu-w", cfg, maxw)


def code(s):
    return ("code", s.strip("\n"))


GPULIB = r"""
(function () {
  if (window.__gpuLib) return; window.__gpuLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }

  function initAmdahl(root, cfg) {
    head(root, cfg.q); var P = { p: 95, n: 7 }, view = el('div'), inf;
    var us = [slider(root, '可以平行的比例 p', 50, 99.9, 0.1, P.p, function (x) { return f1(x) + '%'; }, null, function (x) { P.p = x; draw(); }),
      slider(root, '處理器核心數 N', 0, 14, 1, P.n, function (x) { return Math.pow(2, x).toLocaleString(); }, null, function (x) { P.n = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function S(p, N) { return 1 / ((1 - p) + p / N); }
    function draw() { var p = P.p / 100, N = Math.pow(2, P.n), ser = [];
      [[0.5, GY], [0.9, OR], [0.99, GN], [p, RD]].forEach(function (q, i) { var d = []; for (var k = 0; k <= 14; k += 0.1) d.push([k, S(q[0], Math.pow(2, k))]); ser.push({ d: d, c: q[1], n: i == 3 ? 'p = ' + f1(P.p) + '%' : 'p = ' + q[0] * 100 + '%', w: i == 3 ? 2.6 : 1.4, dash: i == 3 ? null : '4,3' }); });
      view.innerHTML = chart(640, 250, ser, { x0: 0, x1: 14, y0: 0, y1: Math.min(Math.max(S(p, 16384) * 1.15, 12), 120), xl: '核心數（log₂N：0 = 1 核，10 = 1,024 核，14 = 16,384 核）', yl: '加速倍數', pts: [{ x: P.n, y: S(p, N), c: RD, n: f1(S(p, N)) + ' 倍' }] });
      inf.innerHTML = '加速倍數 S = 1 / [(1 − p) + p/N] = <b>' + f1(S(p, N)) + ' 倍</b>（' + N.toLocaleString() + ' 核）。核心再多，也不會超過 1/(1 − p) = <b>' + f1(1 / (1 - p)) + ' 倍</b>。' +
        '<br>只要有 5% 的工作必須依序執行，就算有無限多的核心，最多也只能快 20 倍。所以 GPU 適合的是「幾乎全部都能平行」的工作：像素、矩陣、神經網路。'; }
    us.forEach(function (u) { u(); });
  }

  var WP = [['全部走同一條分支', function (i) { return 0; }], ['一半一半（i < 16）', function (i) { return i < 16 ? 1 : 0; }], ['奇偶交錯（i % 2）', function (i) { return i % 2; }], ['只有 1 個執行緒不同', function (i) { return i == 7 ? 1 : 0; }], ['依資料隨機', function (i) { return ((i * 7919 + 13) % 11) < 4 ? 1 : 0; }]];
  function initWarp(root, cfg) {
    head(root, cfg.q); var P = { k: 1, a: 4, b: 6 }, view = el('div'), inf;
    var bb = bar(root); WP.forEach(function (o, i) { var x = btn(o[0], i); x.onclick = function () { P.k = i; mark(bb, i); draw(); }; bb.appendChild(x); }); mark(bb, 1);
    var us = [slider(root, 'if 分支的指令數', 1, 10, 1, P.a, function (x) { return x; }, null, function (x) { P.a = x; draw(); }), slider(root, 'else 分支的指令數', 1, 10, 1, P.b, function (x) { return x; }, null, function (x) { P.b = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var f = WP[P.k][1], c = [0, 0], g = '', cw = 17, x0 = 60, y0 = 18, rh = 12;
      for (var i = 0; i < 32; i++) c[f(i)]++;
      var steps = (c[1] ? P.a : 0) + (c[0] ? P.b : 0), used = c[1] * P.a + c[0] * P.b, eff = used / (32 * steps);
      for (var i2 = 0; i2 < 32; i2++) { var br = f(i2), x = x0 + i2 * cw; g += tx(x + cw / 2 - 1, 12, i2, 7, 'var(--text-muted)');
        for (var s = 0; s < steps; s++) { var inIf = c[1] && s < P.a, active = inIf ? br == 1 : br == 0; g += '<rect x="' + x + '" y="' + (y0 + s * rh) + '" width="' + (cw - 2) + '" height="' + (rh - 2) + '" fill="' + (active ? (inIf ? OR : BL) : '#e3e3e3') + '"/>'; } }
      if (c[1]) g += tx(x0 - 6, y0 + P.a * rh / 2 + 3, 'if', 10, OR, 'end'); if (c[0]) g += tx(x0 - 6, y0 + ((c[1] ? P.a : 0) + P.b / 2) * rh + 3, 'else', 10, BL, 'end');
      view.innerHTML = svgw('0 0 640 ' + (y0 + steps * rh + 6), g);
      inf.innerHTML = '一個 warp 的 32 個執行緒，在同一時間只能執行<b>同一條指令</b>。走 if 的有 ' + c[1] + ' 個、走 else 的有 ' + c[0] + ' 個。' + (c[0] && c[1] ? '兩條分支必須<b>先後</b>執行，另一半的執行緒只能等待（灰色）。' : '所有執行緒走同一條路，沒有浪費。') +
        '<br>總共花 <b>' + steps + '</b> 個步驟，硬體使用率 <b>' + Math.round(eff * 100) + '%</b>。即使只有 1 個執行緒不同，整個 warp 也要多跑一整條分支——這就是<b>分支發散</b>。'; }
    us.forEach(function (u) { u(); });
  }

  var KN = [['向量相加', 1 / 12, GY], ['矩陣×向量（LLM 逐字生成）', 0.5, OR], ['卷積', 30, GN], ['大型矩陣乘法', 500, PU]];
  function initRoof(root, cfg) {
    head(root, cfg.q); var P = { pk: 1000, bw: 3, ai: 8 }, view = el('div'), inf;
    var us = [slider(root, '峰值運算（TFLOPS）', 50, 2000, 50, P.pk, function (x) { return x + ' TFLOPS'; }, null, function (x) { P.pk = x; draw(); }),
      slider(root, '記憶體頻寬（TB/s）', 0.5, 8, 0.1, P.bw, function (x) { return f1(x) + ' TB/s'; }, null, function (x) { P.bw = x; draw(); }),
      slider(root, '你的 kernel 的運算強度（log）', -2, 3.3, 0.05, Math.log10(P.ai), function (x) { var v = Math.pow(10, x); return (v < 1 ? f2(v) : Math.round(v)) + ' FLOP/byte'; }, null, function (x) { P.ai = Math.pow(10, x); draw(); })];
    root.appendChild(view); inf = info(root);
    function perf(ai) { return Math.min(P.pk, P.bw * ai); }
    function draw() { var d = []; for (var l = -2; l <= 3.3; l += 0.02) d.push([l, Math.log10(perf(Math.pow(10, l)))]);
      var ridge = P.pk / P.bw, pts = KN.map(function (k) { return { x: Math.log10(k[1]), y: Math.log10(perf(k[1])), c: k[2], n: k[0] }; });
      pts.push({ x: Math.log10(P.ai), y: Math.log10(perf(P.ai)), c: RD, n: '你的 kernel' });
      view.innerHTML = chart(640, 280, [{ d: d, c: BL, n: '效能上限（屋頂）', w: 2.6 }], { x0: -2, x1: 3.3, y0: -2, y1: 3.6, xl: '運算強度 log₁₀(FLOP/byte)', yl: 'log₁₀(TFLOPS)', vl: [{ x: Math.log10(ridge), c: GY, n: '轉折點 ' + Math.round(ridge) }], pts: pts });
      var p = perf(P.ai), mb = P.ai < ridge;
      inf.innerHTML = '可達的效能 = min(峰值運算, 頻寬 × 運算強度) = <b>' + (p < 1 ? f2(p) : Math.round(p)) + ' TFLOPS</b>（峰值的 ' + f1(p / P.pk * 100) + '%）。' +
        (mb ? '<br>你的 kernel 在轉折點左邊：<b>受記憶體頻寬限制</b>。運算單元大部分時間在等資料——增加運算能力沒有用，要減少資料搬運（重複使用、tiling、融合 kernel、降低精度）。' : '<br>你的 kernel 在轉折點右邊：<b>受運算能力限制</b>。這是理想的狀態，大型矩陣乘法屬於這一類。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">運算強度＝每從記憶體讀寫一個位元組，做幾次浮點運算。預設數字代表近年資料中心 GPU 的量級（低精度矩陣運算）。</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initTile(root, cfg) {
    head(root, cfg.q); var P = { n: 4096, t: 32 }, view = el('div'), inf;
    var us = [slider(root, '矩陣大小 N（N × N）', 9, 14, 1, 12, function (x) { return Math.pow(2, x).toLocaleString(); }, null, function (x) { P.n = Math.pow(2, x); draw(); }),
      slider(root, 'tile 大小 T', 0, 7, 1, 5, function (x) { return Math.pow(2, x); }, null, function (x) { P.t = Math.pow(2, x); draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var N = P.n, T = P.t, flops = 2 * N * N * N, naive = 2 * N * N * N * 4, tiled = 2 * N * N * N / T * 4, g = '', s = 10, ox = 30, oy = 20;
      for (var r = 0; r < 16; r++) for (var c = 0; c < 16; c++) g += '<rect x="' + (ox + c * s) + '" y="' + (oy + r * s) + '" width="' + (s - 1) + '" height="' + (s - 1) + '" fill="#dde6f0"/>';
      var tw = Math.min(T / 8, 16) * s; g += '<rect x="' + ox + '" y="' + oy + '" width="' + n1(tw) + '" height="' + n1(tw) + '" fill="' + OR + '" opacity="0.85"/>';
      g += tx(ox + 80, oy + 175, '一個 tile（' + T + '×' + T + '）；每格代表 8×8 個元素', 10);
      var mx = Math.log10(naive), bars = [['不分塊', naive, GY], ['tiling', tiled, GN]];
      bars.forEach(function (b, i) { var w = Math.log10(b[1]) / mx * 330, y = oy + 30 + i * 60; g += '<rect x="250" y="' + y + '" width="' + n1(w) + '" height="30" fill="' + b[2] + '"/>' + tx(250, y - 6, b[0] + '：約 ' + (b[1] / 1e9 >= 1000 ? f1(b[1] / 1e12) + ' TB' : f1(b[1] / 1e9) + ' GB') + ' 的全域記憶體讀取', 10.5, 'currentColor', 'start'); });
      view.innerHTML = svgw('0 0 640 210', g);
      inf.innerHTML = '計算 ' + N.toLocaleString() + '×' + N.toLocaleString() + ' 的矩陣乘法需要約 <b>' + (flops >= 1e12 ? f1(flops / 1e12) + ' 兆' : Math.round(flops / 1e8).toLocaleString() + ' 億') + '</b>次浮點運算。如果每次乘法都從全域記憶體讀兩個數（4 位元組），要讀約 ' + f1(naive / 1e12) + ' TB；' +
        '把矩陣切成 ' + T + '×' + T + ' 的小塊，載入晶片上的共享記憶體後重複使用 ' + T + ' 次，讀取量減少為 <b>1/' + T + '</b>。' +
        '<br>運算量不變，搬運量大減——運算強度提高 ' + T + ' 倍，從 Roofline 的左邊（等記憶體）移向右邊（全速運算）。<span style="font-size:0.9em;color:var(--text-muted)">（長條為對數長度；簡化估算，未計入快取。）</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.gpu-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ amdahl: initAmdahl, warp: initWarp, roof: initRoof, tile: initTile })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🟩", GPU_NOTE, GPULIB, "gpu-w")

AMDAHL = gw({"t": "amdahl", "q": u"阿姆達定律：核心越多就越快嗎？"})
WARP = gw({"t": "warp", "q": u"一個 warp 的 32 個執行緒遇到 if-else"})
ROOF = gw({"t": "roof", "q": u"Roofline 模型：你的程式被什麼卡住？"})
TILE = gw({"t": "tile", "q": u"矩陣乘法的 tiling：把資料搬進晶片裡重複使用"})
