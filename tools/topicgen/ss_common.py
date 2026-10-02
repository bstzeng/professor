# -*- coding: utf-8 -*-
"""〈統計物理與相變〉共用工具與互動元件（SSLIB）。"""
from cc_common import *
from qt_common import BASEJS

SS_NOTE = (u"推導段落省略了部分嚴格條件，只想理解概念的讀者可以跳過公式，看圖、互動與「重點」。"
           u"模擬都是在瀏覽器裡執行的小型簡化版本，數值會有隨機起伏。")

SSLIB = r"""
(function () {
  if (window.__ssLib) return; window.__ssLib = 1;
""" + BASEJS + r"""
  function canvas(root, w, h) { var c = document.createElement('canvas'); c.width = w; c.height = h; c.style.cssText = 'width:100%;max-width:' + w + 'px;display:block;margin:0 auto;border-radius:8px;border:1px solid var(--border);image-rendering:pixelated'; root.appendChild(c); return c; }
  function lnC(n, k) { var s = 0; for (var i = 1; i <= k; i++) s += Math.log((n - k + i) / i); return s; }

  /* ---------- 隨機漫步 ---------- */
  function initWalk(root, cfg) {
    head(root, cfg.q); var cv = canvas(root, 640, 300), bar = el('div'), view = el('div'), info = el('p', 'margin:6px 0 0'), P, t, hist, run = true;
    root.appendChild(bar); root.appendChild(view); root.appendChild(info);
    var bp = btn('⏸ 暫停', 'p'); bp.addEventListener('click', function () { run = !run; bp.textContent = run ? '⏸ 暫停' : '▶ 繼續'; }); bar.appendChild(bp);
    var br = btn('↺ 重新開始', 'r'); br.addEventListener('click', reset); bar.appendChild(br);
    function reset() { P = []; for (var i = 0; i < 400; i++) P.push([0, 0]); t = 0; hist = []; }
    function draw() { var g = cv.getContext('2d'); g.fillStyle = 'rgba(14,17,22,1)'; g.fillRect(0, 0, 640, 300); g.fillStyle = 'rgba(120,200,255,0.8)';
      var s2 = 0; P.forEach(function (p) { g.fillRect(320 + p[0] * 2 - 1, 150 + p[1] * 2 - 1, 2.5, 2.5); s2 += p[0] * p[0] + p[1] * p[1]; });
      var r = Math.sqrt(s2 / P.length); g.strokeStyle = '#e8a33d'; g.beginPath(); g.arc(320, 150, r * 2, 0, 6.3); g.stroke();
      if (t % 5 === 0) hist.push([t, r]);
      var th = []; for (var k = 0; k <= Math.max(t, 1); k += Math.max(1, Math.round(t / 100))) th.push([k, Math.sqrt(k)]);
      view.innerHTML = chart(640, 180, [{ d: hist, c: '#e8a33d', n: '模擬的均方根距離' }, { d: th, c: '#3a6ea5', n: '√（步數）', dash: '5 4' }], { x0: 0, y0: 0, xl: '步數' });
      info.innerHTML = '400 個粒子從中心出發，每一步隨機往上下左右走一格。走了 <b>' + t + '</b> 步，平均離開中心約 <b>' + f1(r) + '</b> 格，接近 √' + t + ' ≈ ' + f1(Math.sqrt(t)) + '。橘色圓圈是均方根距離：<b>走 4 倍的步數，只走遠 2 倍</b>——這就是擴散。'; }
    reset();
    setInterval(function () { if (!root.isConnected || !run || t >= 2000) return; P.forEach(function (p) { var r = Math.random() * 4 | 0; if (r === 0) p[0]++; else if (r === 1) p[0]--; else if (r === 2) p[1]++; else p[1]--; }); t++; draw(); }, 40);
  }

  /* ---------- 自由膨脹與熵 ---------- */
  function initExpand(root, cfg) {
    head(root, cfg.q); var N = cfg.n || 40, cv = canvas(root, 640, 200), bar = el('div'), view = el('div'), info = el('p', 'margin:6px 0 0'), P, open = false, hist, t;
    root.appendChild(bar); root.appendChild(view);
    var bo = btn('🚪 拉開隔板', 'o'); bo.addEventListener('click', function () { open = true; }); bar.appendChild(bo);
    var br = btn('↺ 重來', 'r'); br.addEventListener('click', reset); bar.appendChild(br);
    var u = slider(root, '分子數 N', 4, 200, 1, N, function (v) { return v; }, 'n', function (v) { N = v; reset(); }); root.appendChild(info);
    function reset() { P = []; for (var i = 0; i < N; i++) P.push({ x: Math.random() * 300 + 5, y: Math.random() * 190 + 5, vx: (Math.random() - 0.5) * 6, vy: (Math.random() - 0.5) * 6 }); open = false; hist = []; t = 0; }
    function step() { P.forEach(function (p) { p.x += p.vx; p.y += p.vy; if (p.y < 3 || p.y > 197) p.vy *= -1; if (p.x < 3) p.vx = Math.abs(p.vx); if (p.x > 637) p.vx = -Math.abs(p.vx);
        if (!open) { if (p.x > 317 && p.vx > 0) p.vx = -Math.abs(p.vx); } }); t++; }
    function draw() { var g = cv.getContext('2d'); g.fillStyle = '#0e1116'; g.fillRect(0, 0, 640, 200); if (!open) { g.fillStyle = '#e8a33d'; g.fillRect(318, 0, 4, 200); }
      var nl = 0; g.fillStyle = '#78c8ff'; P.forEach(function (p) { if (p.x < 320) nl++; g.beginPath(); g.arc(p.x, p.y, N > 80 ? 2.5 : 4, 0, 6.3); g.fill(); });
      if (t % 3 === 0) { hist.push([t, nl]); if (hist.length > 300) hist.shift(); }
      var S = lnC(N, nl), Smax = lnC(N, Math.floor(N / 2));
      view.innerHTML = chart(640, 170, [{ d: hist, c: '#3a6ea5', n: '左半邊的分子數' }], { y0: 0, y1: N, xl: '時間', hl: [{ y: N / 2, c: '#e0605a', n: 'N/2' }] });
      info.innerHTML = '左邊 <b>' + nl + '</b>、右邊 ' + (N - nl) + '。這個分配方式有 C(N, n<sub>左</sub>) 種排法，熵 S/k = ln W ≈ <b>' + f1(S) + '</b>（最大 ' + f1(Smax) + '）。' +
        '全部分子回到左邊的機率是 (1/2)<sup>N</sup> = <b>' + (N <= 20 ? '1/' + Math.pow(2, N) : '10<sup>−' + Math.round(N * 0.301) + '</sup>') + '</b>。' + (N <= 10 ? '　分子很少時，偶爾真的會全跑回左邊！' : '　N 很大時，「回去」實際上永遠不會發生——這就是熵增加的統計意義。'); }
    reset(); setInterval(function () { if (!root.isConnected) return; step(); draw(); }, 40);
    u();
  }

  /* ---------- 馬克士威—波茲曼速度分布 ---------- */
  var GAS = { '氦 He': 4, '氮 N₂': 28, '氧 O₂': 32, '二氧化碳 CO₂': 44, '氙 Xe': 131 };
  function initMB(root, cfg) {
    head(root, cfg.q); var T = 300, g = '氮 N₂', bar = el('div'), view = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(bar); root.appendChild(view);
    Object.keys(GAS).forEach(function (k) { var b = btn(k, k); b.addEventListener('click', function () { g = k; mark(bar, k); draw(); }); bar.appendChild(b); }); mark(bar, g);
    var u = slider(root, '溫度', 50, 2000, 10, T, function (v) { return v + ' K（' + Math.round(v - 273) + '°C）'; }, 'T', function (v) { T = v; draw(); }); root.appendChild(info);
    function f(v, m, T) { var a = m * 1.6605e-27 / (2 * 1.380649e-23 * T); return 4 * Math.PI * Math.pow(a / Math.PI, 1.5) * v * v * Math.exp(-a * v * v); }
    function draw() { var m = GAS[g], A = [], B = []; for (var v = 0; v <= 3000; v += 10) { A.push([v, f(v, m, T) * 1000]); B.push([v, f(v, m, 300) * 1000]); }
      var kT = 1.380649e-23 * T, M = m * 1.6605e-27, vp = Math.sqrt(2 * kT / M), va = Math.sqrt(8 * kT / (Math.PI * M)), vr = Math.sqrt(3 * kT / M);
      view.innerHTML = chart(640, 240, [{ d: B, c: '#999', n: '300 K 參考', dash: '5 4', w: 1.5 }, { d: A, c: '#e0605a', n: g + ' 在 ' + T + ' K' }], { x0: 0, x1: 3000, y0: 0, xl: '速率（m/s）', yl: '機率密度', vl: [{ x: vp, c: '#3a6ea5', n: '最可能' }] });
      info.innerHTML = '最可能速率 <b>' + Math.round(vp) + '</b> m/s、平均 ' + Math.round(va) + ' m/s、均方根 ' + Math.round(vr) + ' m/s。分子越輕、溫度越高，分布越寬、越往右。空氣分子在室溫下的平均速率比音速（343 m/s）還快！' +
        ' 氦分子跑得快，這也是地球大氣留不住氦和氫的原因之一。'; }
    u();
  }

  /* ---------- 二能階系統與負溫度 ---------- */
  function initTwo(root, cfg) {
    head(root, cfg.q); var p = cfg.p || 0.2, view = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view);
    var u = slider(root, '處在高能階的比例', 0.01, 0.99, 0.01, p, function (v) { return Math.round(v * 100) + '%'; }, 'p', function (v) { p = v; draw(); }); root.appendChild(info);
    function S(x) { return -(x * Math.log(x) + (1 - x) * Math.log(1 - x)); }
    function draw() { var A = []; for (var x = 0.005; x < 1; x += 0.005) A.push([x * 100, S(x)]); var T = 1 / Math.log((1 - p) / p);
      var o = ''; for (var i = 0; i < 40; i++) { var up = i < Math.round(p * 40); o += '<circle cx="' + (30 + (i % 20) * 14) + '" cy="' + (up ? 20 : 78) + '" r="5" fill="' + (up ? '#e0605a' : '#3a6ea5') + '"/>'; }
      o = ln(20, 20, 300, 20, '#999', 1, 'stroke-dasharray="3 3"') + ln(20, 78, 300, 78, '#999', 1, 'stroke-dasharray="3 3"') + o + tx(310, 24, '高能階 ε', 9.5, 'currentColor', 'start') + tx(310, 82, '低能階 0', 9.5, 'currentColor', 'start');
      view.innerHTML = '<div style="display:flex;flex-wrap:wrap;gap:6px;align-items:center"><div style="flex:0 0 260px">' + svgw('0 0 370 100', o) + '</div><div style="flex:1 1 330px">' +
        chart(380, 200, [{ d: A, c: '#8e6bbf', n: '熵 S/Nk' }], { x0: 0, x1: 100, y0: 0, y1: 0.8, xl: '高能階比例（%）＝ 能量', pts: [{ x: p * 100, y: S(p), c: '#e0605a' }], vl: [{ x: 50, c: '#999', n: '' }] }) + '</div></div>';
      info.innerHTML = '溫度定義為 1/T = ∂S/∂E（熵曲線的斜率）。現在 k<sub>B</sub>T/ε = <b>' + (Math.abs(p - 0.5) < 0.006 ? '±∞' : f2(T)) + '</b>。' +
        (p < 0.5 ? '斜率為正：一般的正溫度。' : p > 0.5 ? '<b>斜率為負 → 負溫度！</b>高能階的粒子比低能階多（居量反轉）。負溫度不是「比 0 K 冷」，而是比無限高溫還「熱」：它和正溫度的物體接觸時會放出能量。雷射就是靠居量反轉。' : '剛好一半：溫度為無限大。'); }
    u();
  }

  /* ---------- 量子統計 ---------- */
  function initQS(root, cfg) {
    head(root, cfg.q); var kt = 0.1, view = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view);
    var u = slider(root, '溫度 k_BT（以費米能 E_F 為單位）', 0.005, 1, 0.005, kt, f2, 'kt', function (v) { kt = v; draw(); }); root.appendChild(info);
    function draw() { var A = [], B = [], C = []; for (var e = 0; e <= 2.5; e += 0.005) { var x = (e - 1) / kt; A.push([e, 1 / (Math.exp(x) + 1)]); B.push([e, e > 1 ? Math.min(2, 1 / (Math.exp(x) - 1)) : NaN]); C.push([e, Math.min(2, Math.exp(-x))]); }
      view.innerHTML = chart(640, 240, [{ d: A, c: '#3a6ea5', n: '費米—狄拉克（費米子）' }, { d: B, c: '#e0605a', n: '玻色—愛因斯坦（玻色子）', dash: '5 4' }, { d: C, c: '#999', n: '古典（波茲曼）', dash: '2 3', w: 1.5 }],
        { x0: 0, x1: 2.5, y0: 0, y1: 1.6, xl: '能量 E / E_F（化學勢 μ = E_F）', yl: '平均佔據數', vl: [{ x: 1, c: '#888', n: 'μ' }] });
      info.innerHTML = 'k<sub>B</sub>T = ' + f2(kt) + ' E<sub>F</sub>。費米子最多一個粒子佔一個狀態，所以佔據數不超過 1：低溫時像一個<b>陡峭的台階</b>——費米能以下全滿、以上全空，只有 ±k<sub>B</sub>T 範圍內的電子能被激發。' +
        '金屬的費米能約數 eV（數萬 K），室溫下 k<sub>B</sub>T ≈ 0.01 E<sub>F</sub>，所以電子幾乎「凍結」——這解釋了為什麼金屬電子對比熱貢獻很小。高能量處三種分布趨於一致（古典極限）。'; }
    u();
  }

  /* ---------- 伊辛模型 ---------- */
  function initIsing(root, cfg) {
    head(root, cfg.q); var L = 100, T = cfg.T || 2.27, S = new Int8Array(L * L), cv = canvas(root, L, L), bar = el('div'), view = el('div'), info = el('p', 'margin:6px 0 0'), hist = [], sweep = 0, img;
    cv.style.maxWidth = '360px'; cv.style.width = '100%'; root.appendChild(bar); root.appendChild(view);
    var b1 = btn('隨機（高溫狀態）', 'r'); b1.addEventListener('click', function () { for (var i = 0; i < L * L; i++) S[i] = Math.random() < 0.5 ? 1 : -1; hist = []; sweep = 0; }); bar.appendChild(b1);
    var b2 = btn('全部朝上', 'u'); b2.addEventListener('click', function () { S.fill(1); hist = []; sweep = 0; }); bar.appendChild(b2);
    var u = slider(root, '溫度 k_BT / J', 0.5, 5, 0.01, T, f2, 'T', function (v) { T = v; hist = []; }); root.appendChild(info);
    for (var i = 0; i < L * L; i++) S[i] = Math.random() < 0.5 ? 1 : -1;
    var g = cv.getContext('2d'); img = g.createImageData(L, L);
    function sweepOnce() { var e4 = Math.exp(-4 / T), e8 = Math.exp(-8 / T);
      for (var n = 0; n < L * L; n++) { var k = Math.random() * L * L | 0, x = k % L, y = (k / L) | 0, s = S[k];
        var nb = S[y * L + (x + 1) % L] + S[y * L + (x + L - 1) % L] + S[((y + 1) % L) * L + x] + S[((y + L - 1) % L) * L + x], dE = 2 * s * nb;
        if (dE <= 0 || Math.random() < (dE === 4 ? e4 : e8)) S[k] = -s; } sweep++; }
    function draw() { var m = 0; for (var i = 0; i < L * L; i++) { m += S[i]; var c = S[i] > 0 ? [58, 110, 165] : [240, 240, 235]; img.data[i * 4] = c[0]; img.data[i * 4 + 1] = c[1]; img.data[i * 4 + 2] = c[2]; img.data[i * 4 + 3] = 255; }
      g.putImageData(img, 0, 0); m /= L * L; hist.push([sweep, Math.abs(m)]); if (hist.length > 300) hist.shift();
      view.innerHTML = chart(640, 160, [{ d: hist, c: '#e0605a', n: '|磁化強度 m|' }], { y0: 0, y1: 1, xl: '蒙地卡羅步（每格自旋各更新一次）' });
      info.innerHTML = 'T = ' + f2(T) + '（臨界溫度 T<sub>c</sub> = 2/ln(1+√2) ≈ <b>2.269</b>）。目前 |m| ≈ <b>' + f2(Math.abs(m)) + '</b>。' + (T < 2.1 ? '低溫：鄰居傾向同向，形成大片磁區，最後整片同一個方向——<b>自發磁化</b>。' : T > 2.5 ? '高溫：熱擾動打亂秩序，自旋接近隨機，m ≈ 0。' : '<b>接近臨界點</b>：各種大小的磁區同時存在、不斷變化，沒有特徵尺度——像碎形一樣。'); }
    setInterval(function () { if (!root.isConnected) return; sweepOnce(); draw(); }, 50);
    u();
  }

  /* ---------- 區塊自旋（粗粒化） ---------- */
  function initBlock(root, cfg) {
    head(root, cfg.q); var bar = el('div'), view = el('div', 'display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:6px'), info = el('p', 'margin:6px 0 0'); root.appendChild(bar); root.appendChild(view); root.appendChild(info);
    [['低溫 T = 1.8', 1.8], ['臨界 T = 2.27', 2.269], ['高溫 T = 3.2', 3.2]].forEach(function (p, i) { var b = btn(p[0], 'b' + i); b.addEventListener('click', function () { mark(bar, 'b' + i); run(p[1]); }); bar.appendChild(b); });
    function sim(L, T, sw) { var S = new Int8Array(L * L); for (var i = 0; i < L * L; i++) S[i] = T < 2 ? 1 : (Math.random() < 0.5 ? 1 : -1); var e4 = Math.exp(-4 / T), e8 = Math.exp(-8 / T);
      for (var s = 0; s < sw; s++) for (var n = 0; n < L * L; n++) { var k = Math.random() * L * L | 0, x = k % L, y = (k / L) | 0, v = S[k];
        var nb = S[y * L + (x + 1) % L] + S[y * L + (x + L - 1) % L] + S[((y + 1) % L) * L + x] + S[((y + L - 1) % L) * L + x], dE = 2 * v * nb; if (dE <= 0 || Math.random() < (dE === 4 ? e4 : e8)) S[k] = -v; } return S; }
    function block(S, L) { var l = L / 3, B = new Int8Array(l * l); for (var y = 0; y < l; y++) for (var x = 0; x < l; x++) { var s = 0; for (var j = 0; j < 3; j++) for (var i = 0; i < 3; i++) s += S[(y * 3 + j) * L + x * 3 + i]; B[y * l + x] = s > 0 ? 1 : -1; } return B; }
    function paint(S, L, lab) { var c = document.createElement('canvas'); c.width = L; c.height = L; c.style.cssText = 'width:190px;height:190px;image-rendering:pixelated;border:1px solid var(--border);border-radius:6px'; var g = c.getContext('2d'), im = g.createImageData(L, L);
      for (var i = 0; i < L * L; i++) { var v = S[i] > 0 ? [58, 110, 165] : [240, 240, 235]; im.data[i * 4] = v[0]; im.data[i * 4 + 1] = v[1]; im.data[i * 4 + 2] = v[2]; im.data[i * 4 + 3] = 255; } g.putImageData(im, 0, 0);
      var d = el('div', 'text-align:center;font-size:0.85em'); d.appendChild(c); d.appendChild(el('div', '', lab)); return d; }
    function run(T) { view.innerHTML = '<p>計算中…</p>'; setTimeout(function () { var S0 = sim(243, T, 250), S1 = block(S0, 243), S2 = block(S1, 81);
      view.innerHTML = ''; view.appendChild(paint(S0, 243, '原始 243×243')); view.appendChild(paint(S1, 81, '第一次粗粒化 81×81')); view.appendChild(paint(S2, 27, '第二次粗粒化 27×27'));
      info.innerHTML = '每 3×3 個自旋用「多數決」合成一個大自旋，再放大到同樣大小來看。' + (T < 2 ? '低溫：越粗粒化越整齊，流向「全部同向」。' : T > 2.5 ? '高溫：越粗粒化越像純雜訊，流向「完全隨機」。' : '<b>臨界溫度：粗粒化後看起來和原來「很像」</b>——統計上沒有變化。這種在縮放下不變的性質，就是重整化群的不動點。'); }, 30); }
    mark(bar, 'b1'); run(2.269);
  }

  /* ---------- 滲流 ---------- */
  function initPerc(root, cfg) {
    head(root, cfg.q); var L = 80, p = 0.59, R = new Float32Array(L * L), cv = canvas(root, L, L), info = el('p', 'margin:6px 0 0'), bar = el('div');
    cv.style.maxWidth = '360px'; cv.style.width = '100%'; root.appendChild(bar);
    var b = btn('🎲 換一組隨機數', 'r'); b.addEventListener('click', function () { gen(); draw(); }); bar.appendChild(b);
    var u = slider(root, '每一格「通」的機率 p', 0, 1, 0.005, p, function (v) { return f2(v); }, 'p', function (v) { p = v; draw(); }); root.appendChild(info);
    function gen() { for (var i = 0; i < L * L; i++) R[i] = Math.random(); }
    function draw() { var lab = new Int32Array(L * L).fill(-1), sizes = [], top = {}, bot = {}, id = 0;
      for (var i = 0; i < L * L; i++) { if (R[i] >= p || lab[i] >= 0) continue; var st = [i], n = 0; lab[i] = id;
        while (st.length) { var k = st.pop(), x = k % L, y = (k / L) | 0; n++; if (y === 0) top[id] = 1; if (y === L - 1) bot[id] = 1;
          [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]].forEach(function (q) { if (q[0] < 0 || q[1] < 0 || q[0] >= L || q[1] >= L) return; var j = q[1] * L + q[0]; if (R[j] < p && lab[j] < 0) { lab[j] = id; st.push(j); } }); }
        sizes.push(n); id++; }
      var big = 0; sizes.forEach(function (s, i) { if (s > sizes[big]) big = i; }); var span = -1; for (var c in top) if (bot[c]) { span = +c; break; }
      var g = cv.getContext('2d'), im = g.createImageData(L, L);
      for (i = 0; i < L * L; i++) { var v = lab[i] < 0 ? [235, 235, 230] : lab[i] === span ? [224, 96, 90] : lab[i] === big ? [232, 163, 61] : [140, 170, 205]; im.data[i * 4] = v[0]; im.data[i * 4 + 1] = v[1]; im.data[i * 4 + 2] = v[2]; im.data[i * 4 + 3] = 255; }
      g.putImageData(im, 0, 0);
      info.innerHTML = 'p = ' + f2(p) + '：最大團塊有 <b>' + (sizes.length ? sizes[big] : 0) + '</b> 格（占 ' + Math.round((sizes.length ? sizes[big] : 0) / (L * L) * 100) + '%）。' + (span >= 0 ? '<b style="color:#e0605a">紅色團塊從上連到下了！</b>' : '還沒有團塊從上連到下（橘色是最大團塊）。') +
        ' 正方形格子的滲流閾值 p<sub>c</sub> ≈ <b>0.593</b>：低於它只有零散的小團塊，高於它突然出現貫穿整個系統的「無限團塊」——這是一種幾何的相變。可以想成森林火災能否燒過整片森林、疫情能否擴散到整個城市。'; }
    gen(); u();
  }

  function initAll() { document.querySelectorAll('.ss-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ walk: initWalk, expand: initExpand, mb: initMB, two: initTwo, qs: initQS, ising: initIsing, block: initBlock, perc: initPerc })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def ssw(cfg, maxw=680):
    return wdg("ss-w", cfg, maxw)


sslesson = make_lesson(u"🎲", SS_NOTE, SSLIB, "ss-w")
