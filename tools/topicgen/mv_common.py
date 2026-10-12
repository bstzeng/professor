# -*- coding: utf-8 -*-
"""〈多模態 LLM 與影片生成的內部運作〉（mv_）共用：課程包裝與 MVLIB 互動元件。

MVLIB 元件（class="mv-w"）：
  tok    圖片／影片 token 計算器
  attn   注意力成本計算器
  flow   二維 flow matching 去噪（高斯混合的精確速度場）
  sched  噪音排程、log-SNR 與時間步平移
  clip   對比學習相似度矩陣（InfoNCE 與 sigmoid 損失）
  frames 影片抽幀與 token 預算
  vram   影片模型 VRAM 估算
  tabs   分頁切換（架構比較等）
"""
from cc_common import *
from qt_common import BASEJS
from nv_common import NVLIB

MV_NOTE = (u"本課的互動工具在瀏覽器裡即時計算，使用教學用的小例子與約略估算；模型架構與數字以原始論文、技術報告與官方模型卡為準"
           u"（2026 年 10 月查證），不同版本可能不同。推導採用常見的記號慣例，不同論文的時間方向（t=0 是資料或是噪音）可能相反，課文中會註明。")

MVLIB = r"""
(function () {
  if (window.__mvLib) return; window.__mvLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function rng(seed) { var s = seed >>> 0; return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }
  function gauss(r) { var u = 1 - r(), v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  function big(v) { var a = Math.abs(v); if (a >= 1e15) return f2(v / 1e15) + ' P'; if (a >= 1e12) return f2(v / 1e12) + ' T'; if (a >= 1e9) return f2(v / 1e9) + ' G'; if (a >= 1e6) return f2(v / 1e6) + ' M'; if (a >= 1e3) return f1(v / 1e3) + ' k'; return f1(v); }
  function comma(v) { return Math.round(v).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); }

  /* ---------- token 計算器 ---------- */
  function initTok(root, cfg) {
    head(root, cfg.q); var out = el('div'), p;
    if (cfg.mode === 'img') {
      var H = cfg.h || 336, W = cfg.w || 336, P = cfg.p || 14, Mg = 1;
      var u1 = slider(root, '圖片高度（像素）', 112, 2048, 16, H, function (v) { return v + ' px'; }, 'h', function (v) { H = v; draw(); });
      var u2 = slider(root, '圖片寬度（像素）', 112, 2048, 16, W, function (v) { return v + ' px'; }, 'w', function (v) { W = v; draw(); });
      var u3 = slider(root, 'patch 邊長 p', 8, 32, 2, P, function (v) { return v + ' px'; }, 'p', function (v) { P = v; draw(); });
      var bb = bar(root); bb.appendChild(el('span', 'font-size:0.88em;margin-right:6px', '相鄰合併：'));
      [[1, '不合併'], [2, '2×2 合併'], [4, '4×4 合併']].forEach(function (o) { var b = btn(o[1], 'm' + o[0]); b.addEventListener('click', function () { Mg = o[0]; mark(bb, 'm' + Mg); draw(); }); bb.appendChild(b); }); mark(bb, 'm1');
      root.appendChild(out); p = info(root);
      function draw() { var gh = Math.ceil(H / P), gw = Math.ceil(W / P), n = gh * gw, m = Math.ceil(gh / Mg) * Math.ceil(gw / Mg);
        out.innerHTML = '<div style="margin-top:8px;line-height:1.8">patch 網格：<b>' + gh + ' × ' + gw + '</b> ＝ ' + comma(n) + ' 個 patch' + (Mg > 1 ? '　→ 合併後 <b>' + comma(m) + '</b> 個 token' : '') +
          '<br>送進 LLM 的視覺 token：<b style="font-size:1.2em">' + comma(m) + '</b>　自注意力的配對數 N²：' + big(m * m) + '</div>';
        p.innerHTML = 'token 數 ＝ ⌈H/p⌉ × ⌈W/p⌉ ÷ (合併倍率)²。長寬各放大 2 倍，token 變 4 倍、注意力配對變 16 倍。' + (cfg.note || ''); }
      u1(); u2(); u3(); draw(); return;
    }
    var sec = cfg.sec || 5, fps = cfg.fps || 16, res = cfg.res || '720', ft = cfg.ft || 4, fs = cfg.fs || 8, ps = cfg.ps || 2, C = cfg.c || 16;
    var R = { '480': [480, 832], '720': [720, 1280], '1080': [1080, 1920] };
    var b1 = bar(root); b1.appendChild(el('span', 'font-size:0.88em;margin-right:6px', '解析度：'));
    ['480', '720', '1080'].forEach(function (k) { var b = btn(k + 'p', 'r' + k); b.addEventListener('click', function () { res = k; mark(b1, 'r' + res); draw(); }); b1.appendChild(b); }); mark(b1, 'r' + res);
    var b2 = bar(root); b2.appendChild(el('span', 'font-size:0.88em;margin-right:6px', 'VAE 空間壓縮：'));
    [8, 16].forEach(function (k) { var b = btn(k + '×' + k, 's' + k); b.addEventListener('click', function () { fs = k; mark(b2, 's' + fs); draw(); }); b2.appendChild(b); }); mark(b2, 's' + fs);
    var v1 = slider(root, '影片長度', 1, 20, 1, sec, function (v) { return v + ' 秒'; }, 'sec', function (v) { sec = v; draw(); });
    var v2 = slider(root, '幀率', 8, 30, 1, fps, function (v) { return v + ' fps'; }, 'fps', function (v) { fps = v; draw(); });
    var v3 = slider(root, 'VAE 時間壓縮倍率', 1, 8, 1, ft, function (v) { return v + '×'; }, 'ft', function (v) { ft = v; draw(); });
    var v4 = slider(root, 'DiT patch（空間邊長，時間方向為 1）', 1, 4, 1, ps, function (v) { return '1×' + v + '×' + v; }, 'ps', function (v) { ps = v; draw(); });
    root.appendChild(out); p = info(root);
    function draw() { var hw = R[res], F = ft * Math.ceil(sec * fps / ft) + 1, T = (F - 1) / ft + 1, h = Math.ceil(hw[0] / fs), w = Math.ceil(hw[1] / fs),
        N = T * Math.ceil(h / ps) * Math.ceil(w / ps), px = F * hw[0] * hw[1] * 3, lat = T * h * w * C;
      out.innerHTML = '<div style="margin-top:8px;line-height:1.85">像素影片：' + F + ' 幀 × ' + hw[0] + ' × ' + hw[1] + ' × 3 ＝ ' + big(px) + ' 個數值' +
        '<br>VAE 潛空間：' + T + ' × ' + h + ' × ' + w + ' × ' + C + ' 通道 ＝ ' + big(lat) + ' 個數值（壓縮 ' + f1(px / lat) + ' 倍）' +
        '<br>DiT 的 token 數 N：' + T + ' × ' + Math.ceil(h / ps) + ' × ' + Math.ceil(w / ps) + ' ＝ <b style="font-size:1.2em">' + comma(N) + '</b>' +
        '<br>注意力分數矩陣 N²：' + big(N * N) + ' 個（以 2 bytes 存要 ' + big(N * N * 2) + 'B——所以必須用 FlashAttention 分塊計算）</div>';
      p.innerHTML = '幀數取 ' + ft + 'k+1（因果 VAE 的第一幀單獨編碼）：F ＝ ' + F + '，潛空間幀數 T ＝ (F−1)/' + ft + ' + 1 ＝ ' + T + '。' + (cfg.note || ''); }
    v1(); v2(); v3(); v4(); draw();
  }

  /* ---------- 注意力成本 ---------- */
  function initAttn(root, cfg) {
    head(root, cfg.q); var lgN = cfg.lgn || 16.2, d = cfg.d || 5120, L = cfg.l || 40, K = cfg.k || 40, cfgx = true, out = el('div'), ch = el('div'), p;
    var u1 = slider(root, 'token 數 N（對數刻度）', 8, 18, 0.1, lgN, function (v) { return comma(Math.pow(2, v)); }, 'n', function (v) { lgN = v; draw(); });
    var u2 = slider(root, '隱藏維度 d', 1024, 6144, 256, d, function (v) { return v; }, 'd', function (v) { d = v; draw(); });
    var u3 = slider(root, '層數 L', 12, 60, 1, L, function (v) { return v; }, 'l', function (v) { L = v; draw(); });
    var u4 = slider(root, '去噪步數', 1, 60, 1, K, function (v) { return v + ' 步'; }, 'k', function (v) { K = v; draw(); });
    var bb = bar(root), bc = btn('CFG（每步算兩次）：開', 'c'); bb.appendChild(bc); bc.addEventListener('click', function () { cfgx = !cfgx; bc.textContent = 'CFG（每步算兩次）：' + (cfgx ? '開' : '關'); draw(); });
    root.appendChild(out); root.appendChild(ch); p = info(root);
    function fl(N) { return { lin: 24 * N * d * d, att: 4 * N * N * d }; }
    function draw() { var N = Math.pow(2, lgN), f = fl(N), per = L * (f.lin + f.att), tot = per * K * (cfgx ? 2 : 1), sec = tot / 4e14;
      out.innerHTML = '<div style="margin-top:8px;line-height:1.85">每層：線性部分 24Nd² ＝ ' + big(f.lin) + 'FLOP，注意力部分 4N²d ＝ ' + big(f.att) + 'FLOP（注意力佔 <b>' + f1(100 * f.att / (f.lin + f.att)) + '%</b>）' +
        '<br>一次前向 ＝ ' + big(per) + 'FLOP；整支影片 ＝ ' + big(tot) + 'FLOP' +
        '<br>以每秒 400 TFLOP 的有效算力估計：約 <b>' + (sec >= 120 ? f1(sec / 60) + ' 分鐘' : f1(sec) + ' 秒') + '</b></div>';
      var D = []; for (var x = 8; x <= 18.001; x += 0.1) { var g = fl(Math.pow(2, x)); D.push([x, 100 * g.att / (g.lin + g.att)]); }
      ch.innerHTML = chart(640, 200, [{ d: D, c: '#d0564f', n: '注意力占總計算的百分比' }], { xl: 'log₂ N', y0: 0, y1: 100, pts: [{ x: lgN, y: 100 * f.att / (f.lin + f.att), c: '#3a6ea5' }], vl: [{ x: Math.log2(6 * d), c: '#888', n: 'N ＝ 6d' }] });
      p.innerHTML = '當 N ＞ 6d 時，4N²d 超過 24Nd²，注意力成為主要成本。圖片（數千 token）多半在線左邊；高解析度長影片（數萬到數十萬 token）在線右邊。' + (cfg.note || ''); }
    u1(); u2(); u3(); u4(); draw();
  }

  /* ---------- 二維 flow matching ---------- */
  function initFlow(root, cfg) {
    head(root, cfg.q); var comps = cfg.comps || [[-2, -1.2], [2, -1.2], [0, 2]], sg = cfg.sigma || 0.35, K = cfg.k || 20, tv = 0.5, showF = true, n = 360, out, p;
    var cv = document.createElement('canvas'); cv.width = 400; cv.height = 400; cv.style.cssText = 'width:100%;max-width:400px;display:block;margin:6px auto;border:1px solid var(--border);border-radius:6px;background:var(--surface)';
    var u1 = slider(root, '取樣步數 K（Euler 法）', 1, 60, 1, K, function (v) { return v + ' 步'; }, 'k', function (v) { K = v; run(); });
    var u2 = slider(root, '顯示速度場的時刻 t（0＝噪音，1＝資料）', 0, 0.98, 0.02, tv, f2, 't', function (v) { tv = v; drawAll(); });
    var bb = bar(root), b1 = btn('換一組噪音', 'n'), b2 = btn('速度場：顯示', 'f'); bb.appendChild(b1); bb.appendChild(b2);
    root.appendChild(cv); p = info(root); var seed = 7, X0 = [], paths = [], fin = [];
    function vel(x, y, t) { var lw = [], mx = -1e9, i; for (i = 0; i < comps.length; i++) { var m = comps[i], s2 = (1 - t) * (1 - t) + t * t * sg * sg, dx = x - t * m[0], dy = y - t * m[1], l = -(dx * dx + dy * dy) / (2 * s2) - Math.log(s2); lw.push(l); if (l > mx) mx = l; }
      var Z = 0, vx = 0, vy = 0; for (i = 0; i < comps.length; i++) { var w = Math.exp(lw[i] - mx); Z += w; var m2 = comps[i], s22 = (1 - t) * (1 - t) + t * t * sg * sg, c = (t * sg * sg - (1 - t)) / s22;
        vx += w * (m2[0] + c * (x - t * m2[0])); vy += w * (m2[1] + c * (y - t * m2[1])); } return [vx / Z, vy / Z]; }
    function sample() { var r = rng(seed); X0 = []; for (var i = 0; i < n; i++) X0.push([gauss(r), gauss(r)]); }
    function run() { paths = []; fin = []; X0.forEach(function (q, i) { var x = q[0], y = q[1], pt = [[x, y]]; for (var k = 0; k < K; k++) { var t = k / K, v = vel(x, y, t); x += v[0] / K; y += v[1] / K; if (i < 28) pt.push([x, y]); } fin.push([x, y]); if (i < 28) paths.push(pt); }); drawAll(); }
    function S(v) { return (v + 4) / 8 * 400; }
    function drawAll() { var c = cv.getContext('2d'), dark = matchMedia && matchMedia('(prefers-color-scheme: dark)').matches; c.clearRect(0, 0, 400, 400);
      comps.forEach(function (m) { c.beginPath(); c.arc(S(m[0]), 400 - S(m[1]), 2 * sg / 8 * 400, 0, 7); c.fillStyle = 'rgba(90,164,105,0.18)'; c.fill(); c.strokeStyle = 'rgba(90,164,105,0.7)'; c.stroke(); });
      if (showF) { c.strokeStyle = dark ? 'rgba(200,200,200,0.35)' : 'rgba(80,80,80,0.35)'; for (var gx = -3.6; gx <= 3.61; gx += 0.6) for (var gy = -3.6; gy <= 3.61; gy += 0.6) { var v = vel(gx, gy, tv), L = Math.hypot(v[0], v[1]) || 1, s = Math.min(0.28, L * 0.1) / L;
        var x1 = S(gx), y1 = 400 - S(gy), x2 = S(gx + v[0] * s), y2 = 400 - S(gy + v[1] * s); c.beginPath(); c.moveTo(x1, y1); c.lineTo(x2, y2); c.stroke(); c.beginPath(); c.arc(x2, y2, 1.4, 0, 7); c.fillStyle = c.strokeStyle; c.fill(); } }
      c.strokeStyle = 'rgba(58,110,165,0.55)'; paths.forEach(function (pt) { c.beginPath(); pt.forEach(function (q, j) { if (j) c.lineTo(S(q[0]), 400 - S(q[1])); else c.moveTo(S(q[0]), 400 - S(q[1])); }); c.stroke(); });
      c.fillStyle = '#d0564f'; fin.forEach(function (q) { c.fillRect(S(q[0]) - 1.3, 400 - S(q[1]) - 1.3, 2.6, 2.6); });
      var ok = 0, md = 0; fin.forEach(function (q) { var b = 1e9; comps.forEach(function (m) { b = Math.min(b, Math.hypot(q[0] - m[0], q[1] - m[1])); }); md += b; if (b < 2 * sg) ok++; });
      p.innerHTML = '綠圈：資料分布（三個高斯團，半徑 2σ）；紅點：從噪音出發、積分 ' + K + ' 步後的樣本；藍線：前 28 個樣本的軌跡；灰箭頭：t ＝ ' + f2(tv) + ' 的速度場。' +
        '<br>落在綠圈內的比例：<b>' + Math.round(100 * ok / fin.length) + '%</b>，到最近中心的平均距離：' + f2(md / fin.length) + '。' + (K === 1 ? '<br>只走 1 步時，所有樣本都被推向三個中心的平均位置——這就是「一步取樣會得到模糊的平均圖」的原因。' : ''); }
    b1.addEventListener('click', function () { seed = (seed * 31 + 11) % 100003; sample(); run(); });
    b2.addEventListener('click', function () { showF = !showF; b2.textContent = '速度場：' + (showF ? '顯示' : '隱藏'); drawAll(); });
    u1(); u2(); sample(); run();
  }

  /* ---------- 噪音排程 ---------- */
  function initSched(root, cfg) {
    head(root, cfg.q); var mode = cfg.mode || 'rf', sh = cfg.shift || 1, K = cfg.k || 20, c1 = el('div'), c2 = el('div'), p;
    var bb = bar(root); [['rf', '直線路徑（rectified flow）'], ['vp', '餘弦 VP（DDPM 類）']].forEach(function (o) { var b = btn(o[1], o[0]); b.addEventListener('click', function () { mode = o[0]; mark(bb, mode); draw(); }); bb.appendChild(b); }); mark(bb, mode);
    var u1 = slider(root, '時間步平移 s', 1, 10, 0.5, sh, f1, 's', function (v) { sh = v; draw(); });
    var u2 = slider(root, '取樣步數 K', 4, 50, 1, K, function (v) { return v + ' 步'; }, 'k', function (v) { K = v; draw(); });
    root.appendChild(c1); root.appendChild(c2); p = info(root);
    function ab(t) { return mode === 'rf' ? [1 - t, t] : [Math.cos(Math.PI * t / 2), Math.sin(Math.PI * t / 2)]; }
    function lam(t) { var q = ab(t); return 2 * Math.log(q[0] / q[1]); }
    function shift(t) { return sh * t / (1 + (sh - 1) * t); }
    function draw() { var A = [], B = [], Lm = [], i, t;
      for (i = 0; i <= 100; i++) { t = i / 100; var q = ab(t); A.push([t, q[0]]); B.push([t, q[1]]); if (t > 0.005 && t < 0.995) Lm.push([t, lam(t)]); }
      c1.innerHTML = chart(640, 190, [{ d: A, c: '#3a6ea5', n: 'α(t)：資料的係數' }, { d: B, c: '#d0564f', n: 'σ(t)：噪音的係數' }], { xl: 't（0＝乾淨資料，1＝純噪音）', y0: 0, y1: 1.05 });
      var pts = [], hi = 0; for (i = 0; i < K; i++) { t = shift(1 - i / K); t = Math.min(0.995, Math.max(0.005, t)); pts.push({ x: t, y: lam(t), c: '#5aa469' }); if (t > 0.5) hi++; }
      c2.innerHTML = chart(640, 210, [{ d: Lm, c: '#9c89d6', n: 'log-SNR λ(t) ＝ 2 ln(α/σ)' }], { xl: 't', y0: -12, y1: 12, pts: pts, hl: [{ y: 0, c: '#888', n: 'SNR ＝ 1' }] });
      p.innerHTML = '綠點是 ' + K + ' 個取樣時刻（經過平移 s ＝ ' + f1(sh) + '）。落在高噪音區（t ＞ 0.5）的有 <b>' + hi + '</b> 步（' + Math.round(100 * hi / K) + '%）。' +
        '<br>平移公式 t′ ＝ s·t ／ (1 + (s−1)·t)：s ＞ 1 把更多步數放在高噪音區，高解析度影片（像素彼此高度相關、需要更多噪音才能破壞結構）常用 s ＝ 3～8。'; }
    u1(); u2(); draw();
  }

  /* ---------- 對比學習 ---------- */
  function initClip(root, cfg) {
    head(root, cfg.q); var labs = cfg.labels || ['貓', '狗', '海灘', '披薩', '汽車', '雪山'], n = labs.length, D = 32, a = cfg.a || 0.35, tau = 0.07, b = -5, out = el('div'), p;
    var r = rng(11), I = [], Rn = [], i, j, k;
    function nrm(v) { var s = Math.sqrt(v.reduce(function (q, x) { return q + x * x; }, 0)) || 1; return v.map(function (x) { return x / s; }); }
    for (i = 0; i < n; i++) { var v = [], w = []; for (k = 0; k < D; k++) { v.push(gauss(r)); w.push(gauss(r)); } I.push(nrm(v)); Rn.push(nrm(w)); }
    var u1 = slider(root, '圖文對齊程度（訓練進度）', 0, 1, 0.05, a, f2, 'a', function (v) { a = v; draw(); });
    var u2 = slider(root, '溫度 τ', 0.01, 1, 0.01, tau, f2, 'tau', function (v) { tau = v; draw(); });
    var u3 = slider(root, 'sigmoid 損失的偏置 b', -15, 5, 0.5, b, f1, 'b', function (v) { b = v; draw(); });
    root.appendChild(out); p = info(root);
    function draw() { var T = Rn.map(function (rv, i) { return nrm(I[i].map(function (x, k) { return a * x + (1 - a) * rv[k]; })); }), S = [];
      for (i = 0; i < n; i++) { S.push([]); for (j = 0; j < n; j++) S[i].push(I[i].reduce(function (q, x, k) { return q + x * T[j][k]; }, 0)); }
      var Li = 0, Lt = 0, Ls = 0, P = [];
      for (i = 0; i < n; i++) { var row = S[i].map(function (s) { return s / tau; }), m = Math.max.apply(null, row), z = row.reduce(function (q, x) { return q + Math.exp(x - m); }, 0);
        P.push(row.map(function (x) { return Math.exp(x - m) / z; })); Li += -(row[i] - m - Math.log(z));
        var col = S.map(function (rw) { return rw[i] / tau; }), m2 = Math.max.apply(null, col), z2 = col.reduce(function (q, x) { return q + Math.exp(x - m2); }, 0); Lt += -(col[i] - m2 - Math.log(z2)); }
      for (i = 0; i < n; i++) for (j = 0; j < n; j++) { var zz = (i === j ? 1 : -1) * (S[i][j] / tau + b); Ls += zz > 0 ? Math.log(1 + Math.exp(-zz)) : -zz + Math.log(1 + Math.exp(zz)); }
      var h = '<div style="overflow-x:auto"><table style="border-collapse:collapse;margin:8px auto;font-size:0.85em"><tr><td></td>' + labs.map(function (l) { return '<td style="padding:3px 6px;text-align:center">文：' + l + '</td>'; }).join('') + '</tr>';
      for (i = 0; i < n; i++) { h += '<tr><td style="padding:3px 6px;text-align:right">圖：' + labs[i] + '</td>'; for (j = 0; j < n; j++) { var q = P[i][j];
          h += '<td style="min-width:40px;height:30px;text-align:center;border:1px solid var(--border);background:rgba(58,110,165,' + f2(0.08 + 0.85 * q) + ');color:' + (q > 0.55 ? '#fff' : 'inherit') + (i === j ? ';font-weight:bold' : '') + '">' + f2(S[i][j]) + '</td>'; } h += '</tr>'; }
      out.innerHTML = h + '</table></div>';
      p.innerHTML = '格子裡是餘弦相似度，顏色深淺是「這張圖選中這段文字」的 softmax 機率。對角線是正確配對。' +
        '<br>InfoNCE（CLIP，雙向平均）：<b>' + ((Li + Lt) / (2 * n)).toFixed(3) + '</b>（隨機猜的基準 ln ' + n + ' ＝ ' + f2(Math.log(n)) + '）　sigmoid 損失（SigLIP，每對平均）：<b>' + (Ls / (n * n)).toFixed(3) + '</b>' +
        '<br>溫度越小，softmax 越尖銳：對齊得好時損失更低，對齊得差時懲罰更重。'; }
    u1(); u2(); u3(); draw();
  }

  /* ---------- 影片抽幀 ---------- */
  function initFrames(root, cfg) {
    head(root, cfg.q); var len = cfg.len || 10, fps = cfg.fps || 1, tpf = cfg.tpf || 256, ctx = cfg.ctx || 128, out = el('div'), p;
    var u1 = slider(root, '影片長度', 0.5, 120, 0.5, len, function (v) { return v + ' 分鐘'; }, 'len', function (v) { len = v; draw(); });
    var u2 = slider(root, '抽幀頻率', 0.1, 4, 0.1, fps, function (v) { return f1(v) + ' 幀/秒'; }, 'fps', function (v) { fps = v; draw(); });
    var u3 = slider(root, '每幀的 token 數', 32, 1280, 32, tpf, function (v) { return v; }, 'tpf', function (v) { tpf = v; draw(); });
    var u4 = slider(root, '模型的上下文長度', 32, 2048, 32, ctx, function (v) { return v + 'k token'; }, 'ctx', function (v) { ctx = v; draw(); });
    root.appendChild(out); p = info(root);
    function draw() { var nf = Math.ceil(len * 60 * fps), tok = nf * tpf, cap = ctx * 1024 * 0.9, over = tok > cap, fmax = cap / (len * 60 * tpf), W = 640, g = '';
      g += '<rect x="10" y="20" width="620" height="22" rx="4" fill="var(--accent-soft)"/>';
      if (nf <= 400) { for (var i = 0; i < nf; i++) { var x = 10 + 620 * (i + 0.5) / nf; g += ln(x, 18, x, 44, over ? '#d0564f' : '#3a6ea5', 1); } }
      else g += '<rect x="10" y="20" width="620" height="22" rx="4" fill="' + (over ? '#d0564f' : '#3a6ea5') + '" opacity="0.55"/>';
      g += tx(10, 60, '0', 10, 'var(--text-muted)', 'start') + tx(630, 60, len + ' 分', 10, 'var(--text-muted)', 'end');
      out.innerHTML = svgw('0 0 ' + W + ' 66', g) + '<div style="line-height:1.85">抽出 <b>' + comma(nf) + '</b> 幀 × ' + tpf + ' token ＝ <b>' + comma(tok) + '</b> 個視覺 token（上下文的 ' + Math.round(100 * tok / (ctx * 1024)) + '%）</div>';
      p.innerHTML = over ? '⚠️ 超過上下文（保留 10% 給文字）。在這個長度下，抽幀頻率最多約 <b>' + f2(fmax) + ' 幀/秒</b>（每 ' + f1(1 / fmax) + ' 秒一幀），或把每幀 token 壓到 ' + Math.floor(cap / nf) + ' 以下。' :
        '✅ 放得下。還能提高到約 ' + f2(fmax) + ' 幀/秒。注意：抽幀太稀會漏掉短暫事件（例如 1 秒內的動作）。'; }
    u1(); u2(); u3(); u4(); draw();
  }

  /* ---------- VRAM 估算 ---------- */
  function initVram(root, cfg) {
    head(root, cfg.q); var P = cfg.p || 14, Pt = cfg.pt || 5.7, prec = 2, N = cfg.n || 75600, d = cfg.d || 5120, offT = false, offW = false, out = el('div'), p;
    var bb = bar(root); bb.appendChild(el('span', 'font-size:0.88em;margin-right:6px', '權重精度：'));
    [[4, 'FP32'], [2, 'BF16'], [1, 'FP8'], [0.5, 'INT4']].forEach(function (o) { var b = btn(o[1], 'p' + o[0]); b.addEventListener('click', function () { prec = o[0]; mark(bb, 'p' + prec); draw(); }); bb.appendChild(b); }); mark(bb, 'p2');
    var u1 = slider(root, 'DiT 參數量', 1, 30, 0.5, P, function (v) { return v + 'B'; }, 'p', function (v) { P = v; draw(); });
    var u2 = slider(root, '文字編碼器參數量', 0, 12, 0.1, Pt, function (v) { return f1(v) + 'B'; }, 'pt', function (v) { Pt = v; draw(); });
    var u3 = slider(root, '影片 token 數 N', 5000, 200000, 1000, N, comma, 'n', function (v) { N = v; draw(); });
    var b2 = bar(root), o1 = btn('文字編碼完就卸載：關', 'o1'), o2 = btn('權重逐層從記憶體載入：關', 'o2'); b2.appendChild(o1); b2.appendChild(o2);
    o1.addEventListener('click', function () { offT = !offT; o1.textContent = '文字編碼完就卸載：' + (offT ? '開' : '關'); draw(); });
    o2.addEventListener('click', function () { offW = !offW; o2.textContent = '權重逐層從記憶體載入：' + (offW ? '開' : '關'); draw(); });
    root.appendChild(out); p = info(root);
    function draw() { var w = P * prec * (offW ? 0.1 : 1), te = offT ? 0 : Pt * prec, vae = 0.5, act = N * d * 2 * 12 / 1e9, tot = w + te + vae + act, W = 640, g = '', x = 10, sc = 600 / Math.max(90, tot * 1.1);
      [[w, '#3a6ea5', 'DiT 權重'], [te, '#9c89d6', '文字編碼器'], [vae, '#5aa469', 'VAE'], [act, '#d0564f', '啟動值']].forEach(function (s) { if (s[0] <= 0) return; g += '<rect x="' + n1(x) + '" y="16" width="' + n1(s[0] * sc) + '" height="26" fill="' + s[1] + '"/>'; if (s[0] * sc > 46) g += tx(x + s[0] * sc / 2, 33, s[2], 10, '#fff'); x += s[0] * sc; });
      [8, 12, 16, 24, 32, 48, 80].forEach(function (gb) { var gx = 10 + gb * sc; if (gx > W - 6) return; g += ln(gx, 8, gx, 52, '#888', 1, 'stroke-dasharray="3 3"') + tx(gx, 64, gb + 'G', 9, 'var(--text-muted)'); });
      out.innerHTML = svgw('0 0 ' + W + ' 70', g) + '<div style="line-height:1.85">DiT 權重 ' + f1(w) + ' GB ＋ 文字編碼器 ' + f1(te) + ' GB ＋ VAE 約 ' + f1(vae) + ' GB ＋ 啟動值約 ' + f1(act) + ' GB ＝ <b style="font-size:1.15em">' + f1(tot) + ' GB</b></div>';
      p.innerHTML = '啟動值以「一次只保留一層、使用 FlashAttention」粗估為 N × d × 2 bytes × 12。實際還有 VAE 解碼高峰（可分塊解碼）、框架額外開銷等，數字僅供量級參考。' +
        (offW ? '<br>逐層載入能大幅降低顯存，但每一步都要從主記憶體搬權重，速度會慢上數倍。' : ''); }
    u1(); u2(); u3(); draw();
  }

  /* ---------- 分頁 ---------- */
  function initTabs(root, cfg) {
    head(root, cfg.q); var bb = bar(root), view = el('div', 'margin-top:8px');
    cfg.tabs.forEach(function (t, i) { var b = btn(t[0], 't' + i); b.addEventListener('click', function () { mark(bb, 't' + i); view.innerHTML = t[1]; }); bb.appendChild(b); });
    root.appendChild(view); mark(bb, 't0'); view.innerHTML = cfg.tabs[0][1];
  }

  function initAll() { document.querySelectorAll('.mv-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ tok: initTok, attn: initAttn, flow: initFlow, sched: initSched, clip: initClip, frames: initFrames, vram: initVram, tabs: initTabs })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def mvw(cfg, maxw=680):
    return wdg("mv-w", cfg, maxw)


_base = make_lesson(u"🎬", MV_NOTE, MVLIB, "mv-w")


def lesson(*a, **k):
    """在 make_lesson 之上：用到 nv-w（時間軸、卡片）時補上 NVLIB。"""
    L = _base(*a, **k)
    if any(isinstance(b, tuple) and b[0] == "raw" and 'class="nv-w' in b[1] for b in L.body):
        L.body.insert(0, ("raw", u"<script>%s</script>" % NVLIB))
    return L


def MM(link=None):
    """連到入門課〈多模態與生成式 AI〉。"""
    if link:
        return u'<a href="../multimodal-ai/lesson-%02d.html">〈多模態與生成式 AI〉第 %d 課</a>' % (link, link)
    return u'<a href="../multimodal-ai/index.html">〈多模態與生成式 AI〉</a>'
