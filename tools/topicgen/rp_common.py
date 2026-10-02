# -*- coding: utf-8 -*-
"""〈隨機過程與馬可夫鏈〉共用工具與互動元件（RPLIB）。"""
from cc_common import *
from qt_common import BASEJS

RP_NOTE = (u"推導段落可以跳過，只看圖、互動與「重點」也能掌握概念。模擬結果每次會因隨機性略有不同。"
           u"涉及股價與金融的內容僅為教育用途，不構成投資建議。")

RPLIB = r"""
(function () {
  if (window.__rpLib) return; window.__rpLib = 1;
""" + BASEJS + r"""
  function randn() { var u = 1 - Math.random(), v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  var COL = ['#3a6ea5', '#e0605a', '#5aa469', '#e8a33d', '#8e6bbf', '#2a9d8f', '#c06c84', '#6c757d'];

  /* ---------- 樣本路徑 ---------- */
  function initPaths(root, cfg) {
    head(root, cfg.q); var kind = cfg.k || 'rw', n = 200, m = 8, bar = el('div'), view = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(bar); root.appendChild(view);
    var K = { rw: '隨機漫步（±1）', poi: '卜瓦松計數', bm: '布朗運動' };
    Object.keys(K).forEach(function (k) { var b = btn(K[k], k); b.addEventListener('click', function () { kind = k; mark(bar, k); draw(); }); bar.appendChild(b); }); mark(bar, kind);
    var b2 = btn('🎲 重新產生', 'g'); b2.addEventListener('click', draw); bar.appendChild(b2);
    var u = slider(root, '路徑數', 1, 30, 1, m, function (v) { return v; }, 'm', function (v) { m = v; draw(); }); root.appendChild(info);
    function draw() { var S = [], ends = [];
      for (var j = 0; j < m; j++) { var x = 0, d = [[0, 0]]; for (var t = 1; t <= n; t++) { if (kind === 'rw') x += Math.random() < 0.5 ? 1 : -1; else if (kind === 'poi') x += (Math.random() < 0.1 ? 1 : 0); else x += randn() * 1; d.push([t, x]); }
        S.push({ d: d, c: COL[j % COL.length], w: 1.3 }); ends.push(x); }
      var mean = ends.reduce(function (a, b) { return a + b; }, 0) / m;
      view.innerHTML = chart(640, 260, S, { x0: 0, x1: n, xl: '時間（步）', hl: kind === 'poi' ? [{ y: 20, c: '#999', n: '期望值 λt = 20' }] : [{ y: 0, c: '#999', n: '' }] });
      info.innerHTML = K[kind] + '：' + m + ' 條路徑，終點平均 ' + f1(mean) + '。同一個隨機過程，每次執行都是不同的「劇本」（樣本路徑）。' +
        (kind === 'rw' ? '隨機漫步每步 ±1，平均留在 0 附近，但散開的寬度隨 √t 增加。' : kind === 'poi' ? '卜瓦松過程只會往上跳，每次跳 1，跳的時間點是隨機的（每步機率 0.1）。' : '布朗運動是隨機漫步的連續版本：路徑處處連續，但非常崎嶇。'); }
    u();
  }

  /* ---------- 賭徒破產 ---------- */
  function initRuin(root, cfg) {
    head(root, cfg.q); var a = 10, N = 20, p = 0.49, view = el('div'), bar = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view); root.appendChild(bar);
    var b = btn('▶ 模擬 2000 場', 'go'); b.addEventListener('click', draw); bar.appendChild(b);
    var us = [slider(root, '起始本金 a', 1, 49, 1, a, function (v) { return v + ' 元'; }, 'a', function (v) { a = Math.min(v, N - 1); draw(); }),
      slider(root, '目標 N（贏到就離場）', 2, 50, 1, N, function (v) { return v + ' 元'; }, 'N', function (v) { N = Math.max(v, a + 1); draw(); }),
      slider(root, '每局贏的機率 p', 0.3, 0.7, 0.005, p, function (v) { return f2(v * 100) / 100 + ''; }, 'p', function (v) { p = v; draw(); })];
    root.appendChild(info);
    function theory() { if (Math.abs(p - 0.5) < 1e-9) return a / N; var r = (1 - p) / p; return (1 - Math.pow(r, a)) / (1 - Math.pow(r, N)); }
    function draw() { var win = 0, len = 0, S = []; for (var g = 0; g < 2000; g++) { var x = a, t = 0, d = g < 6 ? [[0, x]] : null; while (x > 0 && x < N) { x += Math.random() < p ? 1 : -1; t++; if (d) d.push([t, x]); } if (x >= N) win++; len += t; if (d) S.push({ d: d, c: COL[g], w: 1.3 }); }
      var mx = Math.max.apply(null, S.map(function (s) { return s.d.length; }));
      view.innerHTML = chart(640, 230, S, { x0: 0, x1: mx, y0: 0, y1: N, xl: '局數', yl: '本金', hl: [{ y: N, c: '#5aa469', n: '目標 ' + N }, { y: 0, c: '#e0605a', n: '破產' }] });
      info.innerHTML = '2000 場模擬中贏到目標的比例 <b>' + f1(win / 20) + '%</b>（理論 ' + f1(theory() * 100) + '%），平均玩 ' + Math.round(len / 2000) + ' 局。' +
        (p < 0.5 ? '每局只稍微不利（' + f1(p * 100) + '%），長期下來卻很難贏：賭場不需要大優勢，只需要你一直玩。' : p > 0.5 ? '優勢在你這邊時，即使本金少也很有機會。' : '公平賭局：贏的機率剛好是 a/N。'); }
    us.forEach(function (f) { f(); });
  }

  /* ---------- 高爾頓板 ---------- */
  function initGalton(root, cfg) {
    head(root, cfg.q); var R = 12, cv = document.createElement('canvas'); cv.width = 640; cv.height = 340; cv.style.cssText = 'width:100%;display:block;background:var(--surface);border:1px solid var(--border);border-radius:8px'; root.appendChild(cv);
    var bar = el('div'), info = el('p', 'margin:6px 0 0'), balls = [], bins = [], tot = 0, run = true; root.appendChild(bar); root.appendChild(info);
    var bp = btn('⏸ 暫停', 'p'); bp.addEventListener('click', function () { run = !run; bp.textContent = run ? '⏸ 暫停' : '▶ 繼續'; }); bar.appendChild(bp);
    var br = btn('↺ 清空', 'r'); br.addEventListener('click', reset); bar.appendChild(br);
    function reset() { balls = []; bins = []; for (var i = 0; i <= R; i++) bins.push(0); tot = 0; }
    function draw() { var g = cv.getContext('2d'); g.clearRect(0, 0, 640, 340); g.fillStyle = '#888';
      for (var r = 0; r < R; r++) for (var k = 0; k <= r; k++) { g.beginPath(); g.arc(320 + (k - r / 2) * 22, 20 + r * 14, 2.5, 0, 6.3); g.fill(); }
      g.fillStyle = '#3a6ea5'; balls.forEach(function (b) { g.beginPath(); g.arc(320 + (b.k - b.r / 2) * 22, 14 + b.r * 14, 4, 0, 6.3); g.fill(); });
      var mx = Math.max.apply(null, bins.concat([1]));
      for (var i = 0; i <= R; i++) { var x = 320 + (i - R / 2) * 22, h = bins[i] / mx * 150; g.fillStyle = 'rgba(58,110,165,0.55)'; g.fillRect(x - 9, 330 - h, 18, h); }
      if (tot > 20) { g.strokeStyle = '#e0605a'; g.lineWidth = 2; g.beginPath(); var C = 1; for (i = 0; i <= R; i++) { var pr = C / Math.pow(2, R), y = 330 - pr * tot / mx * 150, xx = 320 + (i - R / 2) * 22; i ? g.lineTo(xx, y) : g.moveTo(xx, y); C = C * (R - i) / (i + 1); } g.stroke(); }
      info.innerHTML = '已落下 <b>' + tot + '</b> 顆球。每顆球碰到釘子時，往左、往右各 50%，經過 ' + R + ' 排後落入某一格。位置是 ' + R + ' 個獨立隨機變數的總和，分布是二項分布（紅線），而且越來越像<b>常態分布</b>的鐘形曲線——這就是<b>中央極限定理</b>。'; }
    reset(); var k = 0;
    setInterval(function () { if (!root.isConnected || !run) return; if (k++ % 2 === 0) balls.push({ r: 0, k: 0 }); balls.forEach(function (b) { b.r++; if (Math.random() < 0.5) b.k++; });
      balls = balls.filter(function (b) { if (b.r >= R) { bins[b.k]++; tot++; return false; } return true; }); draw(); }, 40);
  }

  /* ---------- 三狀態馬可夫鏈（天氣） ---------- */
  var ST = ['☀️ 晴', '☁️ 陰', '🌧️ 雨'];
  function initChain(root, cfg) {
    head(root, cfg.q); var P = [[0.7, 0.2, 0.1], [0.3, 0.4, 0.3], [0.2, 0.4, 0.4]], start = 2, n = 0, view = el('div'), bar = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view); root.appendChild(bar);
    ST.forEach(function (s, i) { var b = btn('從' + s + '開始', 's' + i); b.addEventListener('click', function () { start = i; mark(bar, 's' + i); draw(); }); bar.appendChild(b); }); mark(bar, 's2');
    var us = [slider(root, '晴天隔天仍晴的機率', 0.1, 0.9, 0.05, P[0][0], f2, 'p00', function (v) { var r = 1 - v; P[0] = [v, r * 2 / 3, r / 3]; draw(); }),
      slider(root, '雨天隔天仍雨的機率', 0.1, 0.9, 0.05, P[2][2], f2, 'p22', function (v) { var r = 1 - v; P[2] = [r / 3, r * 2 / 3, v]; draw(); }),
      slider(root, '經過幾天', 0, 15, 1, n, function (v) { return v + ' 天'; }, 'n', function (v) { n = v; draw(); })];
    root.appendChild(info);
    function step(d) { return [0, 1, 2].map(function (j) { return d[0] * P[0][j] + d[1] * P[1][j] + d[2] * P[2][j]; }); }
    function draw() { var d = [0, 0, 0]; d[start] = 1; var H = [[], [], []]; for (var t = 0; t <= 15; t++) { for (var j = 0; j < 3; j++) H[j].push([t, d[j]]); if (t === n) var dn = d.slice(); d = step(d); }
      var pi = [1 / 3, 1 / 3, 1 / 3]; for (var i = 0; i < 300; i++) pi = step(pi);
      var o = ''; [[90, 60], [260, 160], [430, 60]].forEach(function (p, i) { o += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="30" fill="var(--surface)" stroke="' + COL[i] + '" stroke-width="2"/>' + tx(p[0], p[1] + 6, ST[i], 15); });
      var pos = [[90, 60], [260, 160], [430, 60]];
      for (var a = 0; a < 3; a++) for (var b2 = 0; b2 < 3; b2++) { if (a === b2) { o += tx(pos[a][0], pos[a][1] - 38, '自己 ' + f2(P[a][a]), 12, COL[a]); continue; }
        var x1 = pos[a][0], y1 = pos[a][1], x2 = pos[b2][0], y2 = pos[b2][1], mxp = (x1 + x2) / 2 + (y2 - y1) * 0.18, myp = (y1 + y2) / 2 - (x2 - x1) * 0.18;
        o += '<path d="M' + x1 + ' ' + y1 + ' Q' + n1(mxp) + ' ' + n1(myp) + ' ' + x2 + ' ' + y2 + '" fill="none" stroke="' + COL[a] + '" stroke-width="1" opacity="0.6"/>' + tx(n1((x1 + 2 * mxp + x2) / 4), n1((y1 + 2 * myp + y2) / 4), f2(P[a][b2]), 12, COL[a]); }
      view.innerHTML = '<div style="display:flex;flex-wrap:wrap;gap:6px;align-items:center"><div style="flex:1 1 340px">' + svgw('0 0 520 210', o) + '</div><div style="flex:1 1 300px">' +
        chart(360, 210, [0, 1, 2].map(function (j) { return { d: H[j], c: COL[j], n: ST[j] }; }), { x0: 0, x1: 15, y0: 0, y1: 1, xl: '天數', vl: [{ x: n, c: '#888', n: '' }] }) + '</div></div>';
      info.innerHTML = '從' + ST[start] + '開始，' + n + ' 天後：晴 <b>' + Math.round(dn[0] * 100) + '%</b>、陰 <b>' + Math.round(dn[1] * 100) + '%</b>、雨 <b>' + Math.round(dn[2] * 100) + '%</b>。' +
        '不論從哪一天開始，大約一週後都會收斂到同一個<b>平穩分布</b>：晴 ' + Math.round(pi[0] * 100) + '%、陰 ' + Math.round(pi[1] * 100) + '%、雨 ' + Math.round(pi[2] * 100) + '%——系統「忘記」了起點。'; }
    us.forEach(function (f) { f(); });
  }

  /* ---------- 蛇梯棋 ---------- */
  var JUMP = { 3: 22, 5: 8, 11: 26, 20: 29, 17: 4, 19: 7, 21: 9, 27: 1 };
  function initSnake(root, cfg) {
    head(root, cfg.q); var view = el('div'), bar = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view); root.appendChild(bar);
    var b = btn('▶ 模擬 5000 局', 'go'); b.addEventListener('click', draw); bar.appendChild(b); root.appendChild(info);
    function nxt(s, d) { var t = s + d; if (t >= 30) return 30; return JUMP[t] || t; }
    function expect() { var E = []; for (var i = 0; i <= 30; i++) E.push(0); for (var it = 0; it < 2000; it++) { for (i = 29; i >= 0; i--) { var s = 0; for (var d = 1; d <= 6; d++) s += E[nxt(i, d)]; E[i] = 1 + s / 6; } } return E[0]; }
    function draw() { var cnt = {}, tot = 0, mx = 0; for (var g = 0; g < 5000; g++) { var s = 0, k = 0; while (s < 30 && k < 500) { s = nxt(s, 1 + (Math.random() * 6 | 0)); k++; } cnt[k] = (cnt[k] || 0) + 1; tot += k; if (k > mx) mx = k; }
      var A = []; for (var k2 = 1; k2 <= Math.min(mx, 60); k2++) A.push([k2, (cnt[k2] || 0) / 50]);
      var o = ''; for (var i = 1; i <= 30; i++) { var r = Math.floor((i - 1) / 6), c = (i - 1) % 6; if (r % 2) c = 5 - c; var x = 10 + c * 40, y = 190 - r * 38;
        o += '<rect x="' + x + '" y="' + y + '" width="38" height="36" fill="' + (JUMP[i] ? (JUMP[i] > i ? 'rgba(90,164,105,0.25)' : 'rgba(224,96,90,0.25)') : 'var(--surface)') + '" stroke="var(--border)"/>' + tx(x + 19, y + 15, i, 9, 'var(--text-muted)') + (JUMP[i] ? tx(x + 19, y + 30, (JUMP[i] > i ? '↗' : '↘') + JUMP[i], 9, JUMP[i] > i ? '#5aa469' : '#e0605a') : ''); }
      view.innerHTML = '<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center"><div style="flex:0 0 250px">' + svgw('0 0 260 230', o) + '</div><div style="flex:1 1 340px">' +
        chart(380, 220, [{ d: A, c: '#3a6ea5', n: '幾次擲骰結束（%）' }], { x0: 0, x1: 60, y0: 0, xl: '擲骰次數' }) + '</div></div>';
      info.innerHTML = '綠色是梯子、紅色是蛇。把每一格當成馬可夫鏈的一個狀態，終點是<b>吸收態</b>。用首次步分析解方程組，平均要擲 <b>' + f1(expect()) + '</b> 次；5000 局模擬平均 ' + f1(tot / 5000) + ' 次，最長一局 ' + mx + ' 次。分布有一條長長的尾巴：偶爾會被蛇吞好幾次。'; }
    draw();
  }

  /* ---------- PageRank ---------- */
  var PG = [[90, 60, 'A'], [250, 40, 'B'], [400, 80, 'C'], [80, 190, 'D'], [240, 170, 'E'], [400, 200, 'F']], LK = [[0, 1], [1, 2], [2, 0], [3, 0], [3, 4], [4, 1], [4, 2], [5, 2], [5, 4], [1, 4], [0, 4]];
  function initPR(root, cfg) {
    head(root, cfg.q); var d = 0.85, view = el('div'), info = el('p', 'margin:6px 0 0'), cnt, cur, steps; root.appendChild(view);
    var u = slider(root, '阻尼係數 d（繼續點連結的機率）', 0.05, 0.99, 0.01, d, f2, 'd', function (v) { d = v; cnt = [0, 0, 0, 0, 0, 0]; steps = 0; }); root.appendChild(info);
    cnt = [0, 0, 0, 0, 0, 0]; cur = 0; steps = 0;
    function pr() { var n = 6, r = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]; for (var it = 0; it < 100; it++) { var nr = r.map(function () { return (1 - d) / n; });
        for (var i = 0; i < n; i++) { var out = LK.filter(function (l) { return l[0] === i; }); if (!out.length) { for (var j = 0; j < n; j++) nr[j] += d * r[i] / n; } else out.forEach(function (l) { nr[l[1]] += d * r[i] / out.length; }); } r = nr; } return r; }
    function walk() { for (var s = 0; s < 20; s++) { var out = LK.filter(function (l) { return l[0] === cur; }); if (Math.random() > d || !out.length) cur = Math.random() * 6 | 0; else cur = out[Math.random() * out.length | 0][1]; cnt[cur]++; steps++; } }
    function draw() { var r = pr(), o = '';
      LK.forEach(function (l) { var a = PG[l[0]], b = PG[l[1]], dx = b[0] - a[0], dy = b[1] - a[1], L = Math.hypot(dx, dy), ex = b[0] - dx / L * 24, ey = b[1] - dy / L * 24;
        o += '<line x1="' + a[0] + '" y1="' + a[1] + '" x2="' + n1(ex) + '" y2="' + n1(ey) + '" stroke="#999" stroke-width="1.2" marker-end="url(#pra)"/>'; });
      o = '<defs><marker id="pra" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0L10 5L0 10z" fill="#999"/></marker></defs>' + o;
      PG.forEach(function (p, i) { var rr = 12 + r[i] * 60; o += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + n1(rr) + '" fill="' + (i === cur ? '#e8a33d' : 'rgba(58,110,165,0.25)') + '" stroke="#3a6ea5" stroke-width="1.5"/>' + tx(p[0], p[1] + 4, p[2], 12); });
      var bars = ''; PG.forEach(function (p, i) { var w = r[i] * 500, w2 = steps ? cnt[i] / steps * 500 : 0; bars += tx(10, 22 + i * 30, p[2], 11, 'currentColor', 'start') + '<rect x="30" y="' + (10 + i * 30) + '" width="' + n1(w) + '" height="10" fill="#3a6ea5"/>' + '<rect x="30" y="' + (21 + i * 30) + '" width="' + n1(w2) + '" height="6" fill="#e8a33d"/>' + tx(36 + Math.max(w, w2), 21 + i * 30, Math.round(r[i] * 1000) / 10 + '%', 9, 'currentColor', 'start'); });
      view.innerHTML = '<div style="display:flex;flex-wrap:wrap;gap:6px;align-items:center"><div style="flex:0 0 300px">' + svgw('0 0 480 240', o) + '</div><div style="flex:1 1 300px">' + svgw('0 0 320 190', bars) + '</div></div>';
      info.innerHTML = '藍條是 PageRank（平穩分布），橘條是「隨機上網者」實際停留的比例（已走 ' + steps + ' 步），兩者會越來越接近。上網者以機率 d 點一條隨機連結，以 1 − d 隨便跳到任一頁。<b>被重要的網頁連到，自己就重要</b>：圓圈越大分數越高。'; }
    setInterval(function () { if (!root.isConnected) return; walk(); draw(); }, 120);
    u();
  }

  /* ---------- 分支過程 ---------- */
  function initBranch(root, cfg) {
    head(root, cfg.q); var lam = 1.2, view = el('div'), bar = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view); root.appendChild(bar);
    var b = btn('🎲 重新模擬', 'go'); b.addEventListener('click', draw); bar.appendChild(b);
    var u = slider(root, '每人平均子代數 λ（卜瓦松分布）', 0.5, 2, 0.05, lam, f2, 'lam', function (v) { lam = v; draw(); }); root.appendChild(info);
    function poi(l) { var L = Math.exp(-l), k = 0, p = 1; do { k++; p *= Math.random(); } while (p > L); return k - 1; }
    function draw() { var S = [], dead = 0, R = 400; for (var r = 0; r < R; r++) { var z = 1, d = [[0, 1]]; for (var g = 1; g <= 20; g++) { var nz = 0; for (var i = 0; i < z && nz < 5000; i++) nz += poi(lam); z = nz; if (r < 10) d.push([g, z]); if (z === 0) break; } if (z === 0) dead++; if (r < 10) S.push({ d: d, c: COL[r % 8], w: 1.4 }); }
      var q = 0; for (var it = 0; it < 500; it++) q = Math.exp(lam * (q - 1));
      view.innerHTML = chart(640, 230, S, { x0: 0, x1: 20, y0: 0, y1: lam > 1 ? Math.min(200, Math.pow(lam, 20) * 2) : 6, xl: '世代', yl: '人數' });
      info.innerHTML = 'λ = ' + f2(lam) + '：400 次模擬中有 <b>' + Math.round(dead / 4) + '%</b> 在 20 代內滅絕；理論上最終滅絕機率是方程式 q = e^(λ(q−1)) 的最小解 = <b>' + Math.round(q * 100) + '%</b>。' +
        (lam <= 1 ? 'λ ≤ 1 時一定會滅絕（就算平均每人剛好一個孩子也一樣！）。' : 'λ > 1 時有機會無限成長，但仍有相當機率在早期就意外滅絕。') + '這是高爾頓 1874 年研究「貴族姓氏為什麼會消失」的問題，也適用於病毒傳播、核連鎖反應。'; }
    u();
  }

  /* ---------- 幾何布朗運動 ---------- */
  function initGBM(root, cfg) {
    head(root, cfg.q); var mu = 0.07, sig = 0.2, view = el('div'), bar = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view); root.appendChild(bar);
    var b = btn('🎲 重新模擬', 'go'); b.addEventListener('click', draw); bar.appendChild(b);
    var us = [slider(root, '年化報酬率（漂移）μ', -0.05, 0.15, 0.01, mu, function (v) { return Math.round(v * 100) + '%'; }, 'mu', function (v) { mu = v; draw(); }),
      slider(root, '年化波動率 σ', 0.05, 0.6, 0.01, sig, function (v) { return Math.round(v * 100) + '%'; }, 'sig', function (v) { sig = v; draw(); })];
    root.appendChild(info);
    function draw() { var S = [], ends = [], T = 20, dt = 1 / 12; for (var j = 0; j < 300; j++) { var s = 100, d = [[0, s]]; for (var t = 1; t <= T * 12; t++) { s *= Math.exp((mu - sig * sig / 2) * dt + sig * Math.sqrt(dt) * randn()); if (j < 12) d.push([t / 12, s]); } ends.push(s); if (j < 12) S.push({ d: d, c: COL[j % 8], w: 1.2 }); }
      ends.sort(function (a, b) { return a - b; }); var mean = ends.reduce(function (a, b) { return a + b; }, 0) / ends.length, med = ends[150], lose = ends.filter(function (v) { return v < 100; }).length / 3;
      S.push({ d: [[0, 100], [T, 100 * Math.exp(mu * T)]].map(function (p, i) { return p; }), c: '#000', n: '期望值', dash: '5 4', w: 1.5 });
      var em = []; for (var t2 = 0; t2 <= T; t2 += 0.5) em.push([t2, 100 * Math.exp(mu * t2)]); S[S.length - 1].d = em;
      view.innerHTML = chart(640, 250, S, { x0: 0, x1: T, y0: 0, y1: Math.min(ends[285] * 1.1, 2000), xl: '年', yl: '價格（起始 100）' });
      info.innerHTML = '幾何布朗運動 dS = μS dt + σS dW。300 條路徑 20 年後：平均 <b>' + Math.round(mean) + '</b>、中位數 <b>' + Math.round(med) + '</b>、低於起點的比例 <b>' + Math.round(lose) + '%</b>。' +
        '注意<b>中位數低於平均</b>：少數路徑漲得極多，把平均拉高；典型的結果其實由 μ − σ²/2 決定。波動越大，這個差距越大。<br><span style="color:var(--text-muted);font-size:0.9em">教育用的簡化模型，真實市場有跳躍、肥尾與波動率變化；不構成投資建議。</span>'; }
    us.forEach(function (f) { f(); });
  }

  /* ---------- 馬可夫文字產生器 ---------- */
  var CORPUS = '今天早上天氣很好，太陽從東邊升起，天空很藍。我走到公園，看到很多人在散步。公園裡有一棵很老的大樹，樹下有人在下棋。下午天空變陰了，開始下起小雨。' +
    '雨下了一會兒就停了，天空又出現了太陽。晚上我在家裡看書，書裡寫著很多有趣的故事。故事裡有一個老人每天早上都到公園散步，他說散步讓他很快樂。' +
    '明天天氣可能會下雨，我想我會在家裡看書。如果明天天氣很好，我就到公園去走走，看看那棵老樹，再看看下棋的人。下棋的人很安靜，看棋的人說話很多。' +
    '機率告訴我們明天下雨的可能，但沒有人知道明天一定會怎樣。我們只知道今天，而明天只跟今天有關。';
  function initText(root, cfg) {
    head(root, cfg.q); var k = 2, bar = el('div'), view = el('div', 'padding:10px;border:1px solid var(--border);border-radius:8px;min-height:5em;line-height:1.8'), info = el('p', 'margin:6px 0 0'); root.appendChild(bar); root.appendChild(view); root.appendChild(info);
    [1, 2, 3, 4].forEach(function (o) { var b = btn(o + ' 階（看前 ' + o + ' 字）', 'k' + o); b.addEventListener('click', function () { k = o; mark(bar, 'k' + o); gen(); }); bar.appendChild(b); }); mark(bar, 'k2');
    var bg = btn('🎲 再產生一段', 'g'); bg.addEventListener('click', gen); bar.appendChild(bg);
    function gen() { var M = {}; for (var i = 0; i + k < CORPUS.length; i++) { var key = CORPUS.substr(i, k); (M[key] = M[key] || []).push(CORPUS[i + k]); }
      var keys = Object.keys(M), cur = CORPUS.substr(0, k), out = cur; for (var j = 0; j < 90; j++) { var nx = M[cur]; if (!nx) { cur = keys[Math.random() * keys.length | 0]; out += '／'; continue; } var c = nx[Math.random() * nx.length | 0]; out += c; cur = (cur + c).slice(-k); }
      view.textContent = out;
      info.innerHTML = k + ' 階馬可夫鏈：下一個字只看前 ' + k + ' 個字。' + (k === 1 ? '看得太少，句子東拼西湊。' : k >= 4 ? '看得太多，幾乎是在照抄原文——樣本太少時，模型只會背誦。' : '開始像中文，但意思會飄移。') +
        ' 夏農在 1948 年就用這個方法示範英文的統計結構；今天的大型語言模型看的是前面數十萬個字，而且用神經網路學習機率，但「根據前文預測下一個字」的精神相同。'; }
    gen();
  }

  function initAll() { document.querySelectorAll('.rp-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ paths: initPaths, ruin: initRuin, galton: initGalton, chain: initChain, snake: initSnake, pr: initPR, branch: initBranch, gbm: initGBM, text: initText })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def rpw(cfg, maxw=680):
    return wdg("rp-w", cfg, maxw)


rplesson = make_lesson(u"🎲", RP_NOTE, RPLIB, "rp-w")
