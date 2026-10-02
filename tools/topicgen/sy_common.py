# -*- coding: utf-8 -*-
"""〈系統動力學〉共用工具與互動元件（SYLIB）。"""
from cc_common import *
from qt_common import BASEJS

SY_NOTE = (u"本課的模型都是教學用的簡化版本，用來說明結構如何產生行為，不是對真實世界的精確預測。")

SYLIB = r"""
(function () {
  if (window.__syLib) return; window.__sdLib = 1;
""" + BASEJS + r"""
  /* ---------- 浴缸：存量與流量 ---------- */
  function initTub(root, cfg) {
    head(root, cfg.q); var inf = 6, outf = 4, S = 30, t = 0, hist = [], run = true, view = el('div'), info = el('p', 'margin:6px 0 0;min-height:2.6em');
    root.appendChild(view); var bar = el('div'); root.appendChild(bar);
    var bp = btn('⏸ 暫停', 'p'); bp.addEventListener('click', function () { run = !run; bp.textContent = run ? '⏸ 暫停' : '▶ 繼續'; }); bar.appendChild(bp);
    var br = btn('↺ 重設', 'r'); br.addEventListener('click', function () { S = 30; t = 0; hist = []; }); bar.appendChild(br);
    var u1 = slider(root, '流入（水龍頭）', 0, 10, 0.5, inf, function (v) { return v + ' 公升／秒'; }, 'in', function (v) { inf = v; if (typeof draw === 'function') draw(); });
    var u2 = slider(root, '流出（排水孔）', 0, 10, 0.5, outf, function (v) { return v + ' 公升／秒'; }, 'out', function (v) { outf = v; if (typeof draw === 'function') draw(); });
    root.appendChild(info); u1(); u2();
    function draw() { var h = S / 100 * 120, o = '';
      o += '<rect x="60" y="' + n1(150 - h) + '" width="160" height="' + n1(h) + '" fill="#7fb3e0"/>' + '<path d="M60 26 V150 H220 V26" fill="none" stroke="#555" stroke-width="3"/>';
      o += '<rect x="40" y="12" width="40" height="10" fill="#888"/>' + (inf > 0 ? '<rect x="72" y="22" width="' + n1(2 + inf * 0.6) + '" height="' + n1(128 - h) + '" fill="#7fb3e0" opacity="0.8"/>' : '');
      o += (outf > 0 && S > 0 ? '<rect x="196" y="150" width="' + n1(2 + outf * 0.6) + '" height="24" fill="#7fb3e0"/>' : '') + tx(140, 186, '存量 ' + Math.round(S) + ' 公升', 11);
      o += tx(30, 40, '流入 ' + inf, 10, '#3a6ea5', 'end') + tx(190, 172, '流出 ' + outf, 10, '#e0605a', 'end');
      var ch = chart(380, 196, [{ d: hist.map(function (p) { return [p[0], p[1]]; }), c: '#3a6ea5', n: '存量' }], { x0: Math.max(0, t - 60), x1: Math.max(60, t), y0: 0, y1: 100, xl: '時間（秒）' });
      view.innerHTML = '<div style="display:flex;gap:8px;align-items:flex-start;flex-wrap:wrap"><div style="flex:0 0 250px">' + svgw('0 0 260 196', o) + '</div><div style="flex:1 1 300px">' + ch + '</div></div>';
      var net = inf - outf;
      info.innerHTML = '淨流量 = 流入 − 流出 = <b>' + (net > 0 ? '+' : '') + net + '</b> 公升／秒。' + (net > 0 ? '存量上升' : net < 0 ? '存量下降' : '流入等於流出：存量<b>維持不變</b>（動態平衡）') + '。注意：你調的是<b>流量</b>，存量只能慢慢跟著變——就算把水龍頭關掉，浴缸也不會瞬間變空。' + (S >= 100 ? '　💦 滿出來了！' : ''); }
    setInterval(function () { if (!root.isConnected || !run) return; S = Math.max(0, Math.min(100, S + (inf - outf) * 0.1)); t += 0.1; if (Math.round(t * 10) % 5 === 0) { hist.push([t, S]); if (hist.length > 200) hist.shift(); } draw(); }, 100);
    draw();
  }

  /* ---------- MIT 浴缸測驗 ---------- */
  function initBtest(root, cfg) {
    head(root, cfg.q); var view = el('div'), bar = el('div'), info = el('p', 'margin:6px 0 0'), shown = false; root.appendChild(view); root.appendChild(bar); root.appendChild(info);
    var b = btn('👀 顯示存量的答案', 'ans'); b.addEventListener('click', function () { shown = !shown; b.textContent = shown ? '隱藏答案' : '👀 顯示存量的答案'; draw(); }); bar.appendChild(b);
    function fin(t) { return t <= 4 ? 50 + 25 * t / 4 * 0 + 25 * Math.sin(Math.PI * t / 8) * 0 + (t < 4 ? 50 + 25 * (t / 4) - 50 : 75) : 0; }
    var IN = [], OUT = [], ST = [], s = 100;
    for (var t = 0; t <= 16; t += 0.1) { var i = 50 + 25 * Math.sin(2 * Math.PI * t / 16); IN.push([t, i]); OUT.push([t, 50]); ST.push([t, s]); s += (i - 50) * 0.1; }
    function draw() { var se = [{ d: IN, c: '#3a6ea5', n: '流入' }, { d: OUT, c: '#e0605a', n: '流出', dash: '6 4' }];
      view.innerHTML = chart(640, 210, se, { x0: 0, x1: 16, y0: 0, y1: 100, xl: '時間（分鐘）', yl: '流量（公升／分）' }) + (shown ? chart(640, 190, [{ d: ST, c: '#5aa469', n: '存量（浴缸裡的水）' }], { x0: 0, x1: 16, y0: 80, y1: 280, xl: '時間（分鐘）', yl: '存量（公升）', vl: [{ x: 8, c: '#5aa469', n: '最高點：流入＝流出' }] }) : '');
      info.innerHTML = shown ? '存量在第 <b>8</b> 分鐘最高（流入剛好降回等於流出），在第 0 和第 16 分鐘最低。很多人以為存量會在<b>流入最大</b>的第 4 分鐘最高——那是把流量和存量混為一談。只要流入大於流出，存量就一直在增加。' :
        '浴缸一開始有 100 公升水，流入與流出如上圖。<b>問題：浴缸裡的水什麼時候最多？什麼時候最少？</b>先想一想再按按鈕。'; }
    draw();
  }

  /* ---------- 通用模型模擬器 ---------- */
  var M = {};
  M.exp = { p: [['r', '每期成長率', 1, 20, 1, 7, function (v) { return v + '%'; }]], run: function (P) {
    var a = [], b = [], s = 100, l = 100, T = 50; for (var t = 0; t <= T; t++) { a.push([t, s]); b.push([t, l]); s *= 1 + P.r / 100; l += 100 * P.r / 100; }
    return { s: [{ d: a, c: '#e0605a', n: '複利（增強迴路）' }, { d: b, c: '#3a6ea5', n: '每期固定增加', dash: '6 4' }], o: { xl: '期數', y0: 0 },
      i: '成長率 ' + P.r + '%：大約每 <b>' + f1(70 / P.r) + '</b> 期翻倍（70 法則）。50 期後，複利是 <b>' + fmtT(a[T][1]) + '</b>，固定增加只有 ' + fmtT(b[T][1]) + '。一開始兩條線幾乎重疊——這就是指數成長最危險的地方：前期看不出來。' }; } };
  M.logi = { p: [['r', '內在成長率', 0.1, 1, 0.05, 0.4, f2], ['K', '承載量 K', 200, 1000, 50, 800, function (v) { return v; }]], run: function (P) {
    var a = [], f = [], s = 5; for (var t = 0; t <= 50; t += 0.25) { var fl = P.r * s * (1 - s / P.K); a.push([t, s]); f.push([t, fl * 5]); s += fl * 0.25; }
    var mi = 0; f.forEach(function (p, i) { if (p[1] > f[mi][1]) mi = i; });
    return { s: [{ d: a, c: '#3a6ea5', n: '存量（例如使用者數）' }, { d: f, c: '#e8a33d', n: '淨流入 × 5', dash: '5 3' }], o: { xl: '時間', y0: 0, y1: P.K * 1.1, hl: [{ y: P.K, c: '#e0605a', n: '承載量 K' }], vl: [{ x: f[mi][0], c: '#888', n: '轉折點' }] },
      i: '前半段像指數成長（<b>增強迴路</b>主導）；存量到 K/2 = ' + P.K / 2 + ' 時成長最快，之後<b>調節迴路</b>接手，成長逐漸變慢，最後停在承載量。這就是 S 型曲線：同一個結構，主導迴路換手。' }; } };
  M.goal = { p: [['G', '目標', 50, 150, 5, 120, function (v) { return v; }], ['tau', '調整時間', 1, 20, 1, 5, function (v) { return v + ' 週'; }]], run: function (P) {
    var a = [], s = 40; for (var t = 0; t <= 40; t += 0.25) { a.push([t, s]); s += (P.G - s) / P.tau * 0.25; }
    return { s: [{ d: a, c: '#3a6ea5', n: '庫存' }], o: { xl: '週', y0: 0, y1: 160, hl: [{ y: P.G, c: '#e0605a', n: '目標' }] },
      i: '每週補上「差距 ÷ 調整時間」：差距大時補得多，越接近目標補得越少，所以曲線<b>越來越平</b>，理論上永遠差一點點。大約經過 3 倍調整時間（' + 3 * P.tau + ' 週）可以補上 95% 的差距。' }; } };
  M.shower = { p: [['D', '水管延遲（從轉開關到感覺水溫）', 0, 6, 0.5, 3, function (v) { return v + ' 秒'; }], ['tau', '你調整的耐心（調整時間）', 0.5, 10, 0.5, 1.5, function (v) { return v + ' 秒'; }]], run: function (P) {
    var dt = 0.05, n = Math.round(P.D / dt), u = [], T = [], a = [], tap = 20, G = 38;
    for (var k = 0; k <= 60 / dt; k++) { var temp = k - n >= 0 ? u[k - n] : 20; u.push(tap); if (k % 4 === 0) a.push([k * dt, temp]); tap += (G - temp) / P.tau * dt; tap = Math.max(10, Math.min(70, tap)); }
    var mx = Math.max.apply(null, a.map(function (p) { return p[1]; }));
    return { s: [{ d: a, c: '#e0605a', n: '感覺到的水溫' }], o: { xl: '秒', y0: 0, y1: 75, hl: [{ y: G, c: '#5aa469', n: '想要的 38°C' }] },
      i: '最高曾到 <b>' + f1(mx) + '°C</b>。' + (mx > 41 ? '延遲加上心急，就會<b>忽冷忽熱</b>：你根據「舊的」水溫調整，等熱水到了，已經轉過頭。' : '沒有明顯振盪：延遲短，或你夠有耐心。') + '　試試把延遲調長、耐心調短。' }; } };
  M.over = { p: [['r', '人口成長率', 0.05, 0.5, 0.01, 0.25, f2], ['D', '察覺資源不足的延遲', 0, 20, 1, 8, function (v) { return v + ' 年'; }], ['e', '超載時對資源的破壞', 0, 0.3, 0.01, 0.08, f2]], run: function (P) {
    var dt = 0.25, n = Math.round(P.D / dt), Ph = [], p = 10, K = 1000, a = [], b = [];
    for (var k = 0; k <= 160 / dt; k++) { var pd = k - n >= 0 ? Ph[k - n] : p; Ph.push(p); if (k % 4 === 0) { a.push([k * dt, p]); b.push([k * dt, K]); }
      var dp = P.r * p * (1 - pd / K), dK = 0.02 * (1000 - K) - P.e * Math.max(0, p - K); p = Math.max(0.1, p + dp * dt); K = Math.max(1, K + dK * dt); }
    var mx = Math.max.apply(null, a.map(function (q) { return q[1]; }));
    return { s: [{ d: a, c: '#3a6ea5', n: '人口（或漁船數、使用量）' }, { d: b, c: '#5aa469', n: '承載量（資源）', dash: '6 4' }], o: { xl: '年', y0: 0 },
      i: '人口最高到 <b>' + Math.round(mx) + '</b>。' + (P.D < 2 ? '沒有延遲時，成長會平順地停在承載量（S 型）。' : P.e < 0.02 ? '有延遲但資源不會被破壞：<b>超越後振盪</b>，最後回到承載量附近。' : '延遲讓人口<b>衝過頭</b>，超載又<b>侵蝕了資源</b>，承載量下降，人口跟著崩潰——「超越後崩潰」。') }; } };
  M.sir = { p: [['beta', '每天有效接觸傳染率 β', 0.1, 1, 0.02, 0.4, f2], ['days', '平均傳染期', 2, 14, 1, 7, function (v) { return v + ' 天'; }], ['cut', '第 30 天起減少接觸', 0, 80, 5, 0, function (v) { return v + '%'; }]], run: function (P) {
    var S = 0.999, I = 0.001, R = 0, g = 1 / P.days, dt = 0.2, a = [], b = [], c = [], pk = 0, pd = 0;
    for (var k = 0; k <= 200 / dt; k++) { var t = k * dt, be = P.beta * (t >= 30 ? 1 - P.cut / 100 : 1); if (k % 5 === 0) { a.push([t, S * 100]); b.push([t, I * 100]); c.push([t, R * 100]); } if (I > pk) { pk = I; pd = t; }
      var inf = be * S * I, rec = g * I; S -= inf * dt; I += (inf - rec) * dt; R += rec * dt; }
    var R0 = P.beta / g;
    return { s: [{ d: a, c: '#3a6ea5', n: '易感 S' }, { d: b, c: '#e0605a', n: '感染中 I' }, { d: c, c: '#5aa469', n: '康復 R' }], o: { xl: '天', y0: 0, y1: 100, yl: '人口 %' },
      i: '基本再生數 R₀ = β × 傳染期 = <b>' + f2(R0) + '</b>。' + (R0 <= 1 ? 'R₀ ≤ 1，疫情無法擴散。' : '高峰在第 <b>' + Math.round(pd) + '</b> 天，同時感染 <b>' + f1(pk * 100) + '%</b>；最終約 <b>' + Math.round(R * 100) + '%</b> 的人被感染。群體免疫門檻 1 − 1/R₀ = ' + Math.round((1 - 1 / R0) * 100) + '%。') +
        (P.cut > 0 ? '　減少接觸可以<b>壓平曲線</b>，讓高峰變低、變晚。' : '') }; } };
  M.lv = { p: [['a', '兔子繁殖率', 0.3, 1.5, 0.05, 1, f2], ['c', '狐狸死亡率', 0.2, 1.2, 0.05, 0.5, f2]], run: function (P) {
    var x = 40, y = 9, b = 0.05, d = 0.02, dt = 0.01, A = [], B = []; function f(x, y) { return [P.a * x - b * x * y, d * x * y - P.c * y]; }
    for (var k = 0; k <= 60 / dt; k++) { if (k % 10 === 0) { A.push([k * dt, x]); B.push([k * dt, y]); } var k1 = f(x, y), k2 = f(x + k1[0] * dt / 2, y + k1[1] * dt / 2), k3 = f(x + k2[0] * dt / 2, y + k2[1] * dt / 2), k4 = f(x + k3[0] * dt, y + k3[1] * dt);
      x += dt / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]); y += dt / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]); }
    return { s: [{ d: A, c: '#3a6ea5', n: '兔子（獵物）' }, { d: B, c: '#e0605a', n: '狐狸（掠食者）' }], o: { xl: '年', y0: 0 },
      i: '兔子多 → 狐狸食物多、跟著變多 → 兔子被吃少 → 狐狸餓死變少 → 兔子又變多。兩個族群<b>週期性振盪</b>，狐狸的高峰總是落後兔子。平衡點：兔子 ' + Math.round(P.c / d) + '、狐狸 ' + Math.round(P.a / b) + '。' }; } };
  M.bass = { p: [['p', '創新係數 p（廣告、外部影響）', 0.002, 0.05, 0.002, 0.01, function (v) { return v.toFixed(3); }], ['q', '模仿係數 q（口碑）', 0.05, 0.8, 0.05, 0.4, f2]], run: function (P) {
    var N = 0, a = [], b = [], pk = 0, py = 0; for (var t = 0; t <= 30; t++) { var n = (P.p + P.q * N / 100) * (100 - N); a.push([t, n * 4]); b.push([t, N]); if (n > pk) { pk = n; py = t; } N += n; }
    return { s: [{ d: b, c: '#3a6ea5', n: '累計採用者 %' }, { d: a, c: '#e8a33d', n: '當年新採用 % × 4' }], o: { xl: '年', y0: 0, y1: 100 },
      i: '新採用者在第 <b>' + py + '</b> 年達到高峰（每年 ' + f1(pk) + '% 的市場）。p 決定起步快慢；q 越大，口碑的<b>增強迴路</b>越強，曲線越陡。市場飽和後，調節迴路（剩下的潛在客戶越來越少）讓成長停止。' }; } };
  M.beer = { p: [['al', '補庫存的積極程度 α', 0.1, 1, 0.05, 0.5, f2], ['be', '有沒有算進「已訂未到」的貨 β', 0, 1, 0.1, 0.2, f2]], run: function (P) {
    var K = 4, inv = [12, 12, 12, 12], bl = [0, 0, 0, 0], ship = [[4, 4], [4, 4], [4, 4], [4, 4]], last = [4, 4, 4, 4], Lh = [4, 4, 4, 4], sl = [12, 12, 12, 12], O = [[], [], [], []], dem = [], cost = 0;
    for (var w = 1; w <= 36; w++) { var cd = w < 5 ? 4 : 8; dem.push([w, cd]); var now = [0, 0, 0, 0], incoming = [];
      for (var k = 0; k < K; k++) { var rcv = ship[k].shift(); inv[k] += rcv; sl[k] -= rcv; incoming.push(k === 0 ? cd : last[k - 1]); }
      for (k = 0; k < K; k++) { var need = incoming[k] + bl[k], s = Math.min(inv[k], need); inv[k] -= s; bl[k] = need - s; if (k > 0) ship[k - 1].push(s); cost += inv[k] * 0.5 + bl[k];
        Lh[k] = 0.25 * incoming[k] + 0.75 * Lh[k]; var o = Math.max(0, Lh[k] + P.al * (12 - (inv[k] - bl[k])) + P.al * P.be * (Lh[k] * 3 - sl[k])); now[k] = o; sl[k] += o; O[k].push([w, o]); }
      ship[3].push(last[3]); last = now; }
    var nm = ['零售商', '批發商', '經銷商', '工廠'], cl = ['#3a6ea5', '#5aa469', '#e8a33d', '#e0605a'], se = [{ d: dem, c: '#888', n: '顧客需求', dash: '4 3', w: 2.5 }], mx = [];
    for (k = 0; k < K; k++) { se.push({ d: O[k], c: cl[k], n: nm[k], w: 1.8 }); mx.push(Math.max.apply(null, O[k].map(function (q) { return q[1]; }))); }
    return { s: se, o: { xl: '週', yl: '每週訂貨量', y0: 0, x0: 1, x1: 36 },
      i: '顧客需求只在第 5 週從 4 箱變成 8 箱，之後一直不變。各階層最大訂單：' + nm.map(function (n, i) { return n + ' <b>' + Math.round(mx[i]) + '</b>'; }).join('、') + '。越上游波動越大——這就是<b>長鞭效應</b>。總成本 ' + Math.round(cost) + '。' +
        (P.be < 0.5 ? '　試著把 β 調高：記得「已經訂了還沒到的貨」，波動就小很多。' : '') }; } };

  function initModel(root, cfg) {
    head(root, cfg.q); var m = M[cfg.m], P = {}, view = el('div'), info = el('p', 'margin:6px 0 0'), us = []; root.appendChild(view);
    m.p.forEach(function (q) { P[q[0]] = cfg[q[0]] !== undefined ? cfg[q[0]] : q[5]; us.push(slider(root, q[1], q[2], q[3], q[4], P[q[0]], q[6], q[0], function (v) { P[q[0]] = v; draw(); })); });
    root.appendChild(info);
    function draw() { var r = m.run(P); view.innerHTML = chart(640, 250, r.s, r.o); info.innerHTML = r.i; }
    us.forEach(function (f) { f(); });
  }

  function initAll() { document.querySelectorAll('.sy-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ tub: initTub, btest: initBtest, model: initModel })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def syw(cfg, maxw=680):
    return wdg("sy-w", cfg, maxw)


sylesson = make_lesson(u"🔄", SY_NOTE, SYLIB, "sy-w")
