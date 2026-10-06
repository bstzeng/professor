# -*- coding: utf-8 -*-
"""〈多模態與生成式 AI〉（mm_）共用工具與互動元件（MMLIB）。"""
from cc_common import *
from qt_common import BASEJS

MM_NOTE = (u"本課的互動工具在瀏覽器裡即時計算，使用的是教學用的小例子；CLIP 相似度等數值為示意。"
           u"各模型與產品的推出年份以發表或公開時間為準，功能與授權條款變動很快，使用前請查詢官方最新說明。")

MMLIB = r"""
(function () {
  if (window.__mmLib) return; window.__mmLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('p', 'margin:6px 0 0;line-height:1.65'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function rng(seed) { var s = seed >>> 0; return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }
  function gauss(r) { var u = 1 - r(), v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  function canvas(w, h, cssw) { var c = document.createElement('canvas'); c.width = w; c.height = h; c.style.cssText = 'width:' + (cssw || w) + 'px;max-width:100%;display:block;margin:6px auto;border:1px solid var(--border);border-radius:6px;image-rendering:pixelated'; return c; }
  function scene(N) { var c = document.createElement('canvas'); c.width = c.height = N; var g = c.getContext('2d'), s = N / 64;
    var gr = g.createLinearGradient(0, 0, 0, N); gr.addColorStop(0, '#6fa8dc'); gr.addColorStop(0.6, '#cfe2f3'); g.fillStyle = gr; g.fillRect(0, 0, N, N);
    g.fillStyle = '#f6b26b'; g.beginPath(); g.arc(48 * s, 14 * s, 7 * s, 0, 6.283); g.fill();
    g.fillStyle = '#6aa84f'; g.beginPath(); g.moveTo(0, 46 * s); g.lineTo(18 * s, 26 * s); g.lineTo(34 * s, 44 * s); g.lineTo(46 * s, 32 * s); g.lineTo(64 * s, 46 * s); g.lineTo(64 * s, 64 * s); g.lineTo(0, 64 * s); g.fill();
    g.fillStyle = '#e06666'; g.fillRect(22 * s, 42 * s, 14 * s, 12 * s); g.fillStyle = '#990000'; g.beginPath(); g.moveTo(20 * s, 43 * s); g.lineTo(29 * s, 34 * s); g.lineTo(38 * s, 43 * s); g.fill();
    g.fillStyle = '#ffd966'; g.fillRect(26 * s, 46 * s, 4 * s, 4 * s); g.fillStyle = '#783f04'; g.fillRect(31 * s, 47 * s, 3 * s, 7 * s); return c; }

  /* ---------- 擴散：加噪與去噪 ---------- */
  function initNoise(root, cfg) {
    head(root, cfg.q); var N = 64, src = scene(N).getContext('2d').getImageData(0, 0, N, N).data, r = rng(9), eps = new Float32Array(N * N * 3), x0 = new Float32Array(N * N * 3);
    for (var i = 0; i < N * N; i++) for (var c = 0; c < 3; c++) { x0[i * 3 + c] = src[i * 4 + c] / 127.5 - 1; eps[i * 3 + c] = gauss(r); }
    var T = 1000, ab = [], a = 1; for (var t = 0; t < T; t++) { a *= 1 - (1e-4 + (0.02 - 1e-4) * t / (T - 1)); ab.push(a); }
    var t0 = cfg.t0 || 0, wrap = el('div', 'display:flex;gap:10px;justify-content:center;flex-wrap:wrap'), cv = canvas(N, N, 220), ce = canvas(N, N, 220), w1 = el('div', 'text-align:center;font-size:0.85em'), w2 = el('div', 'text-align:center;font-size:0.85em');
    w1.appendChild(cv); w1.appendChild(el('div', '', '第 t 步的圖 xₜ')); w2.appendChild(ce); w2.appendChild(el('div', '', '加進去的雜訊 ε')); wrap.appendChild(w1); wrap.appendChild(w2);
    var u = slider(root, '時間步 t（0＝原圖，1000＝純雜訊）', 0, 999, 1, t0, function (v) { return v; }, 't', function (v) { t0 = v; draw(); });
    var bb = bar(root), b1 = btn('▶ 播放：加噪（往右）', 'f'), b2 = btn('◀ 播放：去噪（往左）', 'b'); bb.appendChild(b1); bb.appendChild(b2); root.appendChild(wrap); var p = info(root), timer = null;
    function paint(cv2, f) { var g = cv2.getContext('2d'), im = g.createImageData(N, N); for (var i = 0; i < N * N; i++) { for (var c = 0; c < 3; c++) im.data[i * 4 + c] = Math.max(0, Math.min(255, (f(i * 3 + c) + 1) * 127.5)); im.data[i * 4 + 3] = 255; } g.putImageData(im, 0, 0); }
    function play(dir) { if (timer) clearInterval(timer); timer = setInterval(function () { var s = root.querySelector('input[data-k=t]'), v = +s.value + dir * 25; if (v < 0 || v > 999 || !root.isConnected) { clearInterval(timer); timer = null; v = Math.max(0, Math.min(999, v)); } s.value = v; s.dispatchEvent(new Event('input')); }, 40); }
    b1.addEventListener('click', function () { play(1); }); b2.addEventListener('click', function () { play(-1); });
    ce.getContext('2d'); paint(ce, function (k) { return eps[k] * 0.5; });
    function draw() { var A = ab[t0], sa = Math.sqrt(A), sn = Math.sqrt(1 - A); paint(cv, function (k) { return sa * x0[k] + sn * eps[k]; });
      p.innerHTML = 'xₜ ＝ <b>' + sa.toFixed(3) + '</b> × 原圖 ＋ <b>' + sn.toFixed(3) + '</b> × 雜訊（訊號佔比 ᾱₜ ＝ ' + (A * 100).toFixed(1) + '%）。' +
        '<br>訓練時：隨機挑一張圖、一個 t、一份雜訊 ε，讓模型看 xₜ 去猜 ε。生成時：從純雜訊開始，每一步用模型猜出的雜訊扣掉一點，往左一路走回 t＝0。' +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">「去噪」播放這裡是用真正的 ε 倒推，等於假設模型猜得完全正確；真實模型猜得不完美，所以每次生成的細節都不同。雜訊排程用 DDPM（2020）的線性設定。</span>'; }
    u();
  }

  /* ---------- Classifier-free guidance（二維玩具） ---------- */
  function initCFG(root, cfg) {
    head(root, cfg.q); var CL = { cat: [[-1.6, 0.4], [-0.9, 1.4]], dog: [[1.5, 0.2], [0.8, -1.2]] }, S0 = 0.35, w = cfg.w === undefined ? 1 : cfg.w, view = el('div'), p, pts = [];
    var u = slider(root, '引導強度 w（CFG scale）', 0, 8, 0.5, w, function (v) { return v === 0 ? '0（不看提示）' : f1(v); }, 'w', function (v) { w = v; run(); });
    var bb = bar(root), b = btn('🎲 重新取樣 300 個點', 'r'); bb.appendChild(b); root.appendChild(view); p = info(root); b.addEventListener('click', run);
    function score(x, y, comps, s2) { var num = [0, 0], den = 0; comps.forEach(function (m) { var dx = m[0] - x, dy = m[1] - y, g = Math.exp(-(dx * dx + dy * dy) / (2 * s2)); num[0] += g * dx / s2; num[1] += g * dy / s2; den += g; }); return den > 1e-300 ? [num[0] / den, num[1] / den] : [0, 0]; }
    function run() { var r = rng(77 + Math.floor(Math.random() * 1000)), all = CL.cat.concat(CL.dog); pts = [];
      for (var n = 0; n < 300; n++) { var x = gauss(r) * 3, y = gauss(r) * 3;
        for (var L = 0; L < 40; L++) { var sig = 3 * Math.pow(0.05 / 3, L / 39), s2 = S0 * S0 + sig * sig, al = 0.08 * sig * sig;
          for (var k = 0; k < 4; k++) { var su = score(x, y, all, s2), sc = score(x, y, CL.cat, s2), gx = su[0] + w * (sc[0] - su[0]), gy = su[1] + w * (sc[1] - su[1]); x += al * gx + Math.sqrt(2 * al) * gauss(r); y += al * gy + Math.sqrt(2 * al) * gauss(r); } }
        pts.push([x, y]); } draw(); }
    function draw() { function sx(x) { return 320 + x * 80; } function sy(y) { return 150 - y * 60; } var o = '', cat = 0;
      [['cat', '#d9822b', '「貓」的資料'], ['dog', '#3a6ea5', '「狗」的資料']].forEach(function (q) { CL[q[0]].forEach(function (m) { o += '<ellipse cx="' + sx(m[0]) + '" cy="' + sy(m[1]) + '" rx="' + (S0 * 2 * 80) + '" ry="' + (S0 * 2 * 60) + '" fill="' + q[1] + '" opacity="0.15"/>'; }); });
      pts.forEach(function (q) { if (q[0] < 0) cat++; o += '<circle cx="' + n1(sx(q[0])) + '" cy="' + n1(sy(q[1])) + '" r="2.5" fill="#333" opacity="0.7"/>'; });
      o += tx(sx(-1.25), 20, '貓（提示＝「貓」）', 11, '#d9822b') + tx(sx(1.15), 290, '狗', 11, '#3a6ea5');
      view.innerHTML = svgw('0 0 640 300', o);
      var sp = 0, mx = 0, my = 0, c2 = pts.filter(function (q) { return q[0] < 0; }); c2.forEach(function (q) { mx += q[0]; my += q[1]; }); mx /= c2.length || 1; my /= c2.length || 1; c2.forEach(function (q) { sp += (q[0] - mx) * (q[0] - mx) + (q[1] - my) * (q[1] - my); }); sp = Math.sqrt(sp / (c2.length || 1));
      p.innerHTML = '提示是「貓」。300 個樣本裡有 <b>' + Math.round(cat / 3) + '%</b> 落在貓的區域，貓樣本的分散程度 ' + sp.toFixed(2) + '。' +
        '<br>引導公式：<b>方向 ＝ 無條件 ＋ w ×（有條件 − 無條件）</b>。w＝0 完全不看提示（貓狗各半）；w＝1 是正常的條件生成；w 更大時，樣本被推得更「像貓」也更遠離狗，但多樣性下降——對應到圖像生成，就是更貼題、更飽和，卻也更單調。' +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">這是二維的玩具資料，用退火 Langevin 取樣實際算出來的；真實模型的「方向」由神經網路預測，空間是數萬維。</span>'; }
    u();
  }

  /* ---------- ViT：把圖切成 patch ---------- */
  function initPatch(root, cfg) {
    head(root, cfg.q); var res = 224, ps = 16, view = canvas(448, 448, 320), p, sc = scene(448);
    var bb = bar(root); [8, 14, 16, 32].forEach(function (k) { var x = btn('patch ' + k + '×' + k, k); x.addEventListener('click', function () { ps = k; mark(bb, k); draw(); }); bb.appendChild(x); }); mark(bb, ps);
    var u = slider(root, '輸入解析度', 112, 1024, 112, res, function (v) { return v + '×' + v; }, 'res', function (v) { res = v; draw(); });
    root.appendChild(view); p = info(root);
    function draw() { var g = view.getContext('2d'); g.drawImage(sc, 0, 0); var n = Math.round(res / ps), step = 448 / n; g.strokeStyle = 'rgba(255,255,255,0.85)'; g.lineWidth = n > 60 ? 0.5 : 1;
      for (var i = 1; i < n; i++) { g.beginPath(); g.moveTo(i * step, 0); g.lineTo(i * step, 448); g.stroke(); g.beginPath(); g.moveTo(0, i * step); g.lineTo(448, i * step); g.stroke(); }
      var tok = n * n, d = ps * ps * 3;
      p.innerHTML = res + '×' + res + ' 的圖切成 ' + ps + '×' + ps + ' 的小方塊：每邊 ' + n + ' 塊，共 <b>' + tok.toLocaleString() + ' 個 patch</b>，每個 patch 攤平是 ' + ps + '×' + ps + '×3 ＝ ' + d + ' 個數字，再用一個線性層投影成 token 向量。' +
        '<br>對 LLM 來說，這張圖就像一段 <b>' + tok.toLocaleString() + ' 個 token</b> 的文字（實際數字依模型而定，很多模型還會再合併相鄰 patch 來減少 token）。解析度加倍，token 數變成 4 倍，注意力的計算量變成約 16 倍。'; }
    u();
  }

  /* ---------- CLIP：圖文相似度 ---------- */
  function initClip(root, cfg) {
    head(root, cfg.q); var IM = ['🐱', '🐶', '🚗', '🍎', '🌙'], TX = ['一張貓的照片', '一張狗的照片', '一輛紅色汽車', '一顆蘋果', '夜空中的月亮'];
    var E = [[0.9, 0.3, 0.05, 0.05, 0.1], [0.35, 0.9, 0.05, 0.05, 0.05], [0.05, 0.1, 0.92, 0.25, 0.05], [0.05, 0.05, 0.3, 0.92, 0.1], [0.1, 0.05, 0.05, 0.1, 0.95]], Tt = [[1, 0.25, 0, 0, 0.05], [0.25, 1, 0, 0, 0], [0, 0, 1, 0.3, 0], [0, 0, 0.25, 1, 0.05], [0.05, 0, 0, 0.05, 1]];
    function nrm(v) { var s = Math.sqrt(v.reduce(function (a, b) { return a + b * b; }, 0)); return v.map(function (x) { return x / s; }); }
    E = E.map(nrm); Tt = Tt.map(nrm); var sel = 0, temp = 0.07, view = el('div'), p;
    var bb = bar(root); IM.forEach(function (e, i) { var x = btn(e, i); x.style.fontSize = '1.3em'; x.addEventListener('click', function () { sel = i; mark(bb, i); draw(); }); bb.appendChild(x); }); mark(bb, sel);
    var u = slider(root, '溫度 τ（CLIP 訓練時學出來的，約 0.01）', 0.01, 0.5, 0.01, temp, f2, 'tau', function (v) { temp = v; draw(); });
    root.appendChild(view); p = info(root);
    function draw() { var M = E.map(function (e) { return Tt.map(function (t) { return e.reduce(function (s, x, k) { return s + x * t[k]; }, 0); }); });
      var o = '<div class="table-wrap" style="overflow-x:auto"><table><thead><tr><th></th>' + TX.map(function (t) { return '<th style="font-size:0.85em">' + t + '</th>'; }).join('') + '</tr></thead><tbody>';
      M.forEach(function (row, i) { o += '<tr' + (i === sel ? ' style="outline:2px solid #d0564f"' : '') + '><td style="font-size:1.4em;text-align:center">' + IM[i] + '</td>' + row.map(function (v, j) { return '<td style="text-align:center;background:rgba(58,110,165,' + (Math.max(0, v - 0.2) * 1.1).toFixed(2) + ');color:' + (v > 0.7 ? '#fff' : 'inherit') + '">' + v.toFixed(2) + '</td>'; }).join('') + '</tr>'; });
      o += '</tbody></table></div>'; var row = M[sel], ex = row.map(function (v) { return Math.exp(v / temp); }), s = ex.reduce(function (a, b) { return a + b; }, 0);
      o += '<div style="margin-top:8px">' + TX.map(function (t, j) { var pr = ex[j] / s; return '<div style="display:flex;align-items:center;gap:6px;font-size:0.9em"><span style="width:9em;text-align:right">' + t + '</span><span style="flex:1;min-width:0"><span style="display:block;height:12px;border-radius:3px;background:#d0564f;width:' + (pr * 100).toFixed(1) + '%"></span></span><span style="width:3.5em">' + (pr * 100).toFixed(1) + '%</span></div>'; }).join('') + '</div>';
      view.innerHTML = o;
      p.innerHTML = '表格是圖片向量和文字向量的<b>餘弦相似度</b>。CLIP 訓練的目標是讓對角線（配對正確）越大越好、其他格越小越好。' +
        '<br>零樣本分類：把每個類別寫成一句話，看哪句和圖片最像，再用溫度 τ 做 softmax——不用為「貓狗分類」另外訓練模型。<span style="font-size:0.88em;color:var(--text-muted)">（向量是手工設定的示意值，真實的 CLIP 向量有 512～1024 維。）</span>'; }
    u();
  }

  /* ---------- 頻譜圖 ---------- */
  function initSpec(root, cfg) {
    head(root, cfg.q); var SR = 16000, sig = cfg.s || 'vowel', mel = false, bb = bar(root), names = { tone: '純音 440 Hz', chord: 'C 大調和弦', chirp: '掃頻 200→3000 Hz', vowel: '人聲母音（模擬）', noise: '白噪音' }, cur;
    Object.keys(names).forEach(function (k) { var x = btn(names[k], k); x.addEventListener('click', function () { sig = k; mark(bb, k); draw(); }); bb.appendChild(x); }); mark(bb, sig);
    var b2 = bar(root), pl = btn('🔊 播放', 'play'), mb = btn('頻率軸：線性', 'mel'); b2.appendChild(pl); b2.appendChild(mb);
    var wave = el('div'), cv = canvas(320, 160, 640), p; root.appendChild(wave); root.appendChild(cv); p = info(root); cv.style.imageRendering = 'auto';
    mb.addEventListener('click', function () { mel = !mel; mb.textContent = '頻率軸：' + (mel ? 'Mel（接近人耳）' : '線性'); draw(); });
    pl.addEventListener('click', function () { try { var AC = window.AudioContext || window.webkitAudioContext, ac = new AC(), buf = ac.createBuffer(1, cur.length, SR); buf.getChannelData(0).set(cur); var s = ac.createBufferSource(); s.buffer = buf; s.connect(ac.destination); s.start(); } catch (e) { } });
    function gen() { var n = SR, x = new Float32Array(n), r = rng(5); for (var i = 0; i < n; i++) { var t = i / SR, v = 0;
        if (sig === 'tone') v = Math.sin(2 * Math.PI * 440 * t);
        else if (sig === 'chord') v = (Math.sin(2 * Math.PI * 261.6 * t) + Math.sin(2 * Math.PI * 329.6 * t) + Math.sin(2 * Math.PI * 392 * t)) / 3;
        else if (sig === 'chirp') { var f0 = 200, f1 = 3000; v = Math.sin(2 * Math.PI * (f0 * t + (f1 - f0) * t * t / 2)); }
        else if (sig === 'vowel') { var f = 140 * (1 + 0.03 * Math.sin(2 * Math.PI * 5 * t)); for (var h = 1; h <= 25; h++) { var fh = h * f, amp = Math.exp(-Math.pow((fh - 750) / 160, 2)) + 0.6 * Math.exp(-Math.pow((fh - 1200) / 200, 2)) + 0.25 * Math.exp(-Math.pow((fh - 2600) / 300, 2)) + 0.02; v += amp * Math.sin(2 * Math.PI * fh * t + h); } v *= 0.35; }
        else v = (r() * 2 - 1) * 0.5;
        x[i] = v * 0.5 * Math.min(1, t * 20, (1 - t) * 20); } return x; }
    function fft(re, im) { var n = re.length; for (var i = 1, j = 0; i < n; i++) { var bit = n >> 1; for (; j & bit; bit >>= 1) j ^= bit; j ^= bit; if (i < j) { var t = re[i]; re[i] = re[j]; re[j] = t; t = im[i]; im[i] = im[j]; im[j] = t; } }
      for (var len = 2; len <= n; len <<= 1) { var ang = -2 * Math.PI / len, wr = Math.cos(ang), wi = Math.sin(ang); for (var i2 = 0; i2 < n; i2 += len) { var cr = 1, ci = 0; for (var k = 0; k < len / 2; k++) { var ur = re[i2 + k], ui = im[i2 + k], vr = re[i2 + k + len / 2] * cr - im[i2 + k + len / 2] * ci, vi = re[i2 + k + len / 2] * ci + im[i2 + k + len / 2] * cr;
              re[i2 + k] = ur + vr; im[i2 + k] = ui + vi; re[i2 + k + len / 2] = ur - vr; im[i2 + k + len / 2] = ui - vi; var nr = cr * wr - ci * wi; ci = cr * wi + ci * wr; cr = nr; } } } }
    function draw() { cur = gen(); var o = '', W = 640; for (var i = 0; i < 640; i++) { var k = Math.floor(i * 800 / 640); o += (i ? 'L' : 'M') + i + ' ' + n1(30 - cur[k] * 50); } wave.innerHTML = svgw('0 0 640 60', '<path d="' + o + '" fill="none" stroke="#3a6ea5" stroke-width="1"/>' + tx(636, 56, '前 0.05 秒的波形', 9, 'var(--text-muted)', 'end'));
      var NF = 512, frames = 320, hop = Math.floor((SR - NF) / frames), g = cv.getContext('2d'), im = g.createImageData(320, 160), S = [], mx = -1e9;
      for (var f = 0; f < frames; f++) { var re = new Float64Array(NF), imv = new Float64Array(NF), st = f * hop; for (var n = 0; n < NF; n++) { var v = cur[st + n] || 0; re[n] = v * (0.5 - 0.5 * Math.cos(2 * Math.PI * n / (NF - 1))); } fft(re, imv);
        var col = []; for (var b = 0; b < 160; b++) { var hz = mel ? 700 * (Math.pow(10, (b / 159 * 2595 * Math.log10(1 + 4000 / 700)) / 2595) - 1) : b / 159 * 4000, bin = Math.min(NF / 2 - 1, Math.round(hz / SR * NF)), m = Math.log10(re[bin] * re[bin] + imv[bin] * imv[bin] + 1e-9); col.push(m); if (m > mx) mx = m; } S.push(col); }
      for (var f2 = 0; f2 < frames; f2++) for (var b2i = 0; b2i < 160; b2i++) { var v2 = Math.max(0, Math.min(1, (S[f2][b2i] - mx + 6) / 6)), q = ((159 - b2i) * 320 + f2) * 4; im.data[q] = Math.round(255 * Math.min(1, v2 * 1.6)); im.data[q + 1] = Math.round(255 * Math.max(0, v2 * 1.6 - 0.6)); im.data[q + 2] = Math.round(90 * (1 - v2) + 40); im.data[q + 3] = 255; }
      g.putImageData(im, 0, 0);
      p.innerHTML = '下面是<b>頻譜圖</b>：橫軸是時間（1 秒）、縱軸是頻率（0～4000 Hz，下低上高）、越亮代表該頻率越強。做法是把聲音切成很多短片段，每段做傅立葉轉換。' +
        (sig === 'vowel' ? '<br>母音有一條條等距的<b>諧波</b>，其中幾段特別亮的區域叫<b>共振峰</b>——不同的母音（啊、咿、嗚）共振峰位置不同，語音辨識模型就是從這種圖學會分辨的。' : sig === 'chirp' ? '<br>頻率隨時間升高，所以是一條斜線。' : sig === 'chord' ? '<br>三個音同時響，就是三條水平線。' : sig === 'noise' ? '<br>白噪音在所有頻率都一樣強，所以整片都亮。' : '<br>純音只有一個頻率，就是一條水平線。') +
        '<br>切換成 Mel 刻度，低頻被拉開、高頻被壓縮，比較接近人耳的感受。Whisper 等語音模型的輸入就是 Mel 頻譜圖。'; }
    draw();
  }

  /* ---------- 圖像潛空間的壓縮 ---------- */
  function initLatent(root, cfg) {
    head(root, cfg.q); var res = 512, f = 8, ch = 4, view = el('div'), p;
    var u1 = slider(root, '圖片解析度', 256, 2048, 128, res, function (v) { return v + '×' + v; }, 'res', function (v) { res = v; draw(); });
    var u2 = slider(root, 'VAE 縮小倍數 f', 4, 16, 4, f, function (v) { return v + ' 倍'; }, 'f', function (v) { f = v; draw(); });
    var u3 = slider(root, '潛空間通道數', 4, 16, 4, ch, function (v) { return v; }, 'ch', function (v) { ch = v; draw(); });
    root.appendChild(view); p = info(root);
    function draw() { var px = res * res * 3, lt = (res / f) * (res / f) * ch, r = px / lt, W = 600;
      view.innerHTML = svgw('0 0 640 90', '<rect x="20" y="16" width="' + W + '" height="26" fill="#3a6ea5" opacity="0.75"/>' + tx(26, 33, '像素：' + px.toLocaleString() + ' 個數字', 10, '#fff', 'start') +
        '<rect x="20" y="52" width="' + Math.max(2, W / r).toFixed(1) + '" height="26" fill="#d9822b"/>' + tx(26 + Math.max(2, W / r), 69, '　潛空間：' + lt.toLocaleString() + ' 個（' + (res / f) + '×' + (res / f) + '×' + ch + '）', 10, 'currentColor', 'start'));
      p.innerHTML = '在像素上直接做擴散，每一步都要處理 ' + px.toLocaleString() + ' 個數字。<b>Latent Diffusion</b> 先用 VAE 把圖壓縮 ' + Math.round(r) + ' 倍，在小得多的潛空間裡擴散，最後再解碼回像素。' +
        (res === 512 && f === 8 && ch === 4 ? '<br>這正是 Stable Diffusion 1.x 的設定：512×512×3 → 64×64×4。SDXL、SD3、Flux 等後來的模型改用更多通道（例如 16）保留更多細節。' : ''); }
    u1(); u2(); u3();
  }

  function initAll() { document.querySelectorAll('.mm-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ noise: initNoise, cfg: initCFG, patch: initPatch, clip: initClip, spec: initSpec, latent: initLatent })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def mmw(cfg, maxw=680):
    return wdg("mm-w", cfg, maxw)


mmlesson = make_lesson(u"🎨", MM_NOTE, MMLIB, "mm-w")
