# -*- coding: utf-8 -*-
"""〈免疫系統與疫苗〉（imm_）共用：課程包裝與 IMLIB 互動元件（class="im-w"）。

  sir    SIR 傳染病模型（R₀、疫苗覆蓋率、疫苗效力）
  ab     初次與二次抗體反應（IgM、IgG，對數刻度）
  herd   群體免疫：400 人的傳播模擬
"""
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

IM_NOTE = u"本課程為衛教與科普知識介紹，不能取代醫療建議；疫苗接種與疾病治療請諮詢醫師。互動工具為簡化的教學模型，數值僅用來建立直覺，不能用來預測真實的疫情。"
F = D


def imw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("im-w", cfg)


IMLIB = r"""
(function () {
  if (window.__imLib) return; window.__imLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function row(root) { var d = el('div', 'margin:4px 0'); root.appendChild(d); return d; }
  function sl(root, lab, mn, mx, st, val, fmt, cb) { return slider(root, lab, mn, mx, st, val, fmt || function (x) { return x; }, null, cb); }
  function pc(x, d) { return (x * 100).toFixed(d === undefined ? 0 : d) + '%'; }
  var PRE = [['季節性流感', 1.3], ['COVID-19 原始株', 2.8], ['COVID-19 Delta', 5], ['天花', 5.5], ['麻疹', 15]];

  /* ---------- SIR ---------- */
  function initSir(root, cfg) { head(root, cfg.q); var P = { r0: 2.8, cov: 0, ve: 0.9 }, v = el('div'), inf, ups = [], b = row(root);
    b.appendChild(el('span', 'font-size:0.85em;color:var(--text-muted);margin-right:4px', '疾病：'));
    PRE.forEach(function (q, k) { var x = btn(q[0], k); x.onclick = function () { var rg = root.querySelector('input[type=range]'); rg.value = q[1]; s0(); }; b.appendChild(x); });
    var s0 = slider(root, '基本再生數 R₀', 1, 18, 0.1, P.r0, function (x) { return (+x).toFixed(1); }, null, function (x) { P.r0 = x; draw(); });
    var s1 = sl(root, '疫苗覆蓋率（爆發前已接種的比例）', 0, 1, 0.01, P.cov, function (x) { return pc(x); }, function (x) { P.cov = x; draw(); });
    var s2 = sl(root, '疫苗效力（接種者得到保護的比例）', 0, 1, 0.01, P.ve, function (x) { return pc(x); }, function (x) { P.ve = x; draw(); });
    root.appendChild(v); inf = info(root); ups = [s0, s1, s2];
    function sim() { var D = 7, g = 1 / D, b = P.r0 * g, imm = P.cov * P.ve, S = 1 - imm - 1e-4, I = 1e-4, R = imm, dt = 0.1, out = [], peak = 0, pd = 0;
      for (var t = 0; t <= 300; t += dt) { if (Math.abs(t - Math.round(t)) < dt / 2) out.push([Math.round(t), S, I, R]); var nI = b * S * I * dt, nR = g * I * dt; S -= nI; I += nI - nR; R += nR; if (I > peak) { peak = I; pd = t; } }
      return { out: out, peak: peak, pd: pd, att: R - imm + I, imm: imm }; }
    function draw() { var r = sim(), Re = P.r0 * (1 - r.imm), th = 1 - 1 / P.r0, need = P.ve > 0 ? th / P.ve : Infinity;
      var S = [], I = [], R = []; r.out.forEach(function (p) { S.push([p[0], p[1] * 100]); I.push([p[0], p[2] * 100]); R.push([p[0], p[3] * 100]); });
      v.innerHTML = chart(680, 260, [{ d: S, c: BL, n: '易感者 S' }, { d: I, c: RD, n: '感染者 I', w: 2.5 }, { d: R, c: GN, n: '康復／免疫 R' }], { x0: 0, x1: 300, y0: 0, y1: 100, xl: '天數（假設平均傳染期 7 天）', yl: '% 人口' });
      inf.innerHTML = '有效再生數 <b>R<sub>e</sub> ≈ ' + Re.toFixed(2) + '</b>（' + (Re < 1 ? '<b style="color:' + GN + '">小於 1：疫情無法擴大</b>' : '大於 1：疫情會擴散') + '）。' +
        (Re >= 1 ? '感染高峰約在第 <b>' + Math.round(r.pd) + '</b> 天，同時有 <b>' + pc(r.peak, 1) + '</b> 的人正在感染；最終約 <b>' + pc(r.att) + '</b> 的人口被感染。' : '少數病例會出現，但傳播鏈會逐漸斷掉。') +
        '<br>群體免疫門檻 1 − 1/R₀ ≈ <b>' + pc(th) + '</b>；以 ' + pc(P.ve) + ' 效力的疫苗，需要約 <b>' + (need > 1 ? '超過 100%（不可能只靠疫苗達成）' : pc(need)) + '</b> 的覆蓋率。' +
        '<br><span style="color:var(--text-muted);font-size:0.9em">注意：即使疫情停止時，最終被感染的人也會「超過」門檻——疫情衝過頭。簡化模型：人群均勻混合、免疫不會消失、沒有出生死亡與行為改變。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 抗體反應 ---------- */
  function curve(t, t0, lag, tp, peak, half) { if (t < t0 + lag) return 0; if (t < t0 + tp) { var u = (t - t0 - lag) / (tp - lag); return peak * Math.pow(u, 2); } return peak * Math.pow(0.5, (t - t0 - tp) / half); }
  function initAb(root, cfg) { head(root, cfg.q); var P = { second: 1, gap: 60 }, v = el('div'), inf, b = row(root);
    [['只接觸一次', 0], ['再次接觸（或打加強劑）', 1]].forEach(function (q) { var x = btn(q[0], q[1]); x.onclick = function () { P.second = q[1]; mark(b, P.second); draw(); }; b.appendChild(x); }); mark(b, P.second);
    var ug = sl(root, '第二次接觸的時間', 20, 180, 5, P.gap, function (x) { return '第 ' + x + ' 天'; }, function (x) { P.gap = x; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var M = [], G = [], T = 240;
      for (var t = 0; t <= T; t += 1) { var m = curve(t, 0, 4, 10, 60, 6), g = curve(t, 0, 6, 18, 100, 25);
        if (P.second) { m += curve(t, P.gap, 2, 6, 30, 5); g += curve(t, P.gap, 2, 9, 3000, 45); }
        M.push([t, Math.log10(1 + m)]); G.push([t, Math.log10(1 + g)]); }
      var vl = [{ x: 0, c: GY, n: '第一次' }]; if (P.second) vl.push({ x: P.gap, c: PU, n: '第二次' });
      v.innerHTML = chart(680, 260, [{ d: M, c: OR, n: 'IgM（先出現、很快消退）' }, { d: G, c: BL, n: 'IgG（主力、持久）', w: 2.5 }], { x0: 0, x1: T, y0: 0, y1: 4, xl: '天數', yl: 'log₁₀ 抗體濃度（示意）', vl: vl });
      inf.innerHTML = '<b>初次反應</b>：接觸後約一週才出現抗體，先是 IgM，再轉換為 IgG，高峰較低。這段延遲，正是病原體有機會讓人生病的時間。' +
        (P.second ? '<br><b>二次反應</b>：記憶 B 細胞讓抗體在<b>幾天內</b>就大量出現，IgG 的高峰約為初次的數十倍，而且持續更久——這就是免疫記憶，也是疫苗與加強劑的原理（圖的縱軸是對數刻度，每一格是十倍）。' : '<br>按「再次接觸」看看免疫記憶的效果。') +
        '<br><span style="color:var(--text-muted);font-size:0.9em">示意曲線：真實的時間與濃度因病原體、疫苗與個人而異。</span>'; }
    mark(b, P.second); ug(); }

  /* ---------- 群體免疫模擬 ---------- */
  function initHerd(root, cfg) { head(root, cfg.q); var P = { r0: 3, cov: 0.5 }, v = el('div'), inf, seed = 1;
    var h1 = sl(root, '每位感染者平均接觸並可能傳染的人數 R₀', 1, 8, 0.5, P.r0, function (x) { return (+x).toFixed(1); }, function (x) { P.r0 = x; run(); });
    var h2 = sl(root, '已免疫的比例', 0, 0.95, 0.05, P.cov, function (x) { return pc(x); }, function (x) { P.cov = x; run(); });
    var bb = row(root), again = btn('重新模擬'); again.onclick = function () { seed++; run(); }; bb.appendChild(again);
    root.appendChild(v); inf = info(root);
    function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
    function run() { var N = 400, st = [], q = [], gen = [], k, i; seed = (seed % 1000) + 7;
      for (i = 0; i < N; i++) st.push(rnd() < P.cov ? 'V' : 'S');
      var first = 0; while (st[first] === 'V' && first < N - 1) first++; st[first] = 'I'; q.push(first); gen[first] = 0;
      var maxg = 0;
      while (q.length) { var c = q.shift(), n = Math.floor(P.r0) + (rnd() < P.r0 - Math.floor(P.r0) ? 1 : 0);
        for (k = 0; k < n; k++) { var j = Math.floor(rnd() * N); if (st[j] === 'S') { st[j] = 'I'; gen[j] = gen[c] + 1; maxg = Math.max(maxg, gen[j]); q.push(j); } } }
      var g = '', cnt = { S: 0, V: 0, I: 0 }; for (i = 0; i < N; i++) { cnt[st[i]]++; var x = 14 + (i % 25) * 26, y = 14 + Math.floor(i / 25) * 26, col = st[i] === 'V' ? GN : st[i] === 'I' ? RD : '#d5d8dc';
        g += '<circle cx="' + x + '" cy="' + y + '" r="9" fill="' + col + '"' + (i === first ? ' stroke="#000" stroke-width="2"' : '') + '/>'; }
      v.innerHTML = svgw('0 0 660 420', g);
      var th = 1 - 1 / P.r0;
      inf.innerHTML = '<span style="color:' + RD + '">●</span> 被感染 <b>' + cnt.I + '</b> 人　<span style="color:' + GN + '">●</span> 已免疫 <b>' + cnt.V + '</b> 人　<span style="color:#aab">●</span> 未感染的易感者 <b>' + cnt.S + '</b> 人（黑框是第一位病人）。傳播了 ' + maxg + ' 代。<br>' +
        '理論的群體免疫門檻是 1 − 1/R₀ ≈ <b>' + pc(th) + '</b>。' + (P.cov >= th ? '目前已超過門檻：傳播鏈通常很快就斷了，<b>沒有免疫的人也被間接保護</b>——這就是群體免疫。' : '目前低於門檻：疫情往往會擴散到大部分的易感者。') +
        '<br><span style="color:var(--text-muted);font-size:0.9em">每次模擬都有隨機性，多按幾次「重新模擬」。在門檻附近，結果特別不穩定。</span>'; }
    h1(); h2(); }

  var INIT = { sir: initSir, ab: initAb, herd: initHerd };
  function boot() { document.querySelectorAll('.im-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🦠", note=IM_NOTE):
    return make_with(icon, note, [("im-w", IMLIB)])


lesson = make()
