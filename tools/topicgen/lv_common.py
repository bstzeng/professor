# -*- coding: utf-8 -*-
"""〈開槓的藝術〉的互動元件（LVLIB，class="lv-w"）：
decay 波動拖累、margin 斷頭價、kelly 最適槓桿、ladder 跌幅分批、voltgt 波動率目標、bt 情境回測。"""
from cc_common import make_lesson, wdg, LS
from qt_common import BASEJS


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def lw(cfg, maxw=680):
    return wdg("lv-w", cfg, maxw)


LVLIB = r"""
(function () {
  if (window.__lvLib) return; window.__lvLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5', TL = '#2a9d8f';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function small(s) { return '<br><span style="font-size:0.88em;color:var(--text-muted)">' + s + '</span>'; }
  function presets(root, list, cb, k0) { var b = bar(root); list.forEach(function (o, i) { var x = btn(o[0], i); x.onclick = function () { mark(b, i); cb(o, i); }; b.appendChild(x); }); mark(b, k0 === undefined ? 0 : k0); return b; }
  function setS(root, k, v) { var s = root.querySelector('input[data-k="' + k + '"]'); if (s) s.value = v; }
  function pct(v) { return (v >= 0 ? '+' : '') + f1(v * 100) + '%'; }
  function rng(seed) { var s = seed; return function () { s = (s * 1103515245 + 12345) % 2147483648; return s / 2147483648; }; }
  function gauss(r) { var u = Math.max(r(), 1e-9), v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }

  /* 1. 波動拖累 */
  function initDecay(root, cfg) { head(root, cfg.q); var P = { m: 0, v: 20, mu: 0 }, view = el('div');
    presets(root, [['盤整（漲跌交替）'], ['隨機走勢']], function (o, i) { P.m = i; draw(); });
    var u1 = slider(root, '年化波動率', 5, 50, 1, P.v, function (x) { return x + '%'; }, null, function (x) { P.v = x; draw(); });
    var u2 = slider(root, '指數的年化報酬（隨機走勢）', -10, 20, 1, P.mu, function (x) { return x + '%'; }, null, function (x) { P.mu = x; draw(); });
    root.appendChild(view); var inf = info(root);
    function draw() { var N = 252 * 3, sd = P.v / 100 / Math.sqrt(252), r = rng(7), a = [1], b = [1], c = [1], d1 = [[0, 1]], d2 = [[0, 1]], d3 = [[0, 1]], i, x;
      for (i = 1; i <= N; i++) { x = P.m === 0 ? (i % 2 ? sd : -sd) : (P.mu / 100 / 252 + sd * gauss(r)); a.push(a[i - 1] * (1 + x)); b.push(Math.max(b[i - 1] * (1 + 2 * x), 0)); c.push(Math.max(c[i - 1] * (1 + 3 * x), 0)); if (i % 2 === 0) { d1.push([i / 252, a[i]]); d2.push([i / 252, b[i]]); d3.push([i / 252, c[i]]); } }
      var mx = Math.max.apply(null, d1.concat(d2, d3).map(function (p) { return p[1]; }));
      view.innerHTML = chart(640, 230, [{ d: d1, c: GY, n: '指數（1 倍）' }, { d: d2, c: BL, n: '每日 2 倍' }, { d: d3, c: RD, n: '每日 3 倍' }], { x0: 0, x1: 3, y0: 0, y1: Math.min(mx * 1.05, 8), xl: '年', yl: '淨值（起點 = 1）' });
      var s2 = Math.pow(P.v / 100, 2);
      inf.innerHTML = '三年後：指數 <b>' + pct(a[N] - 1) + '</b>、2 倍 <b>' + pct(b[N] - 1) + '</b>、3 倍 <b>' + pct(c[N] - 1) + '</b>。' + (P.m === 0 ? '<br>指數每天漲跌同樣的幅度，幾乎原地踏步；但槓桿越大，淨值<b>越磨越少</b>——這就是「<b>波動拖累</b>」。' : '<br>每日重設的槓桿產品，長期的報酬大約是：L × 指數報酬 − (L² − L) × 波動率² ÷ 2。波動率 ' + P.v + '% 時，2 倍每年約多被磨掉 <b>' + f1(s2 * 100) + '%</b>，3 倍約 <b>' + f1(3 * s2 * 100) + '%</b>。') + '<br>趨勢明確的上漲中，槓桿會「超過」2 倍；震盪或下跌中，則遠遠不如。' + small('模擬未計入管理費與借貸成本；隨機走勢為固定種子的示意路徑，不是預測。'); }
    u1(); u2();
  }

  /* 2. 斷頭價計算機 */
  function initMargin(root, cfg) { head(root, cfg.q); var P = { t: 0, ltv: 60, own: 100 }, view = el('div');
    presets(root, [['融資（上市）'], ['股票質押'], ['台指期（小台）']], function (o, i) { P.t = i; setS(root, 'ltv', i === 0 ? 60 : i === 1 ? 50 : 30); P.ltv = i === 0 ? 60 : i === 1 ? 50 : 30; u1(); });
    var u1 = slider(root, '借款成數／保證金比例', 10, 80, 1, P.ltv, function (x) { return P.t === 2 ? '帳戶權益是契約價值的 ' + x + '%' : x + '%'; }, 'ltv', function (x) { P.ltv = x; draw(); });
    root.appendChild(view); var inf = info(root);
    function draw() { var o = '', L, call, msg;
      if (P.t < 2) { var loan = P.ltv / 100, eq = 1 - (P.t === 0 ? loan : 0), pos = P.t === 0 ? 1 : 1 + loan; // 融資：自備 eq 買 1 單位；質押：持有 1 單位股票，借 loan 再買 loan 單位
        if (P.t === 0) { L = 1 / eq; } else { L = pos; } call = 1.3 * loan;
        msg = P.t === 0 ? '融資自備 ' + Math.round(eq * 100) + '%、借 ' + P.ltv + '%：實際槓桿約 <b>' + f2(L) + ' 倍</b>。<br>維持率 = 股票市值 ÷ 融資金額，低於 <b>130%</b> 就會被追繳。股價從買進價下跌 <b>' + f1((1 - call) * 100) + '%</b> 時觸及追繳線。' : '用原本的持股質押，借出市值的 ' + P.ltv + '% 再全部買進股票：總曝險約 <b>' + f2(L) + ' 倍</b>。<br>維持率 = 擔保品（原本的持股）市值 ÷ 借款，低於 <b>130%</b> 會被追繳。股價下跌 <b>' + f1((1 - call) * 100) + '%</b> 時觸及追繳線。'; }
      else { L = 100 / P.ltv; var dropF = Math.max(P.ltv / 100 - 0.093, 0.005); msg = '帳戶權益是契約價值的 ' + P.ltv + '%：槓桿約 <b>' + f1(L) + ' 倍</b>。<br>以原始保證金約為契約價值的 12%、維持保證金約為原始的 77%（約契約價值的 9.3%）估算：指數下跌約 <b>' + f1(dropF * 100) + '%</b> 時，權益就跌到維持保證金，需要補繳。只放原始保證金（約 8 倍槓桿）的話，指數跌約 3% 就會被追繳。'; call = 1 - dropF; }
      var drop = 1 - call, W = 520; o += rect(60, 40, W, 26, 'rgba(74,154,94,0.25)') + rect(60 + W * Math.min(drop / 0.6, 1), 40, W - W * Math.min(drop / 0.6, 1), 26, 'rgba(208,86,79,0.25)') + ln(60 + W * Math.min(drop / 0.6, 1), 30, 60 + W * Math.min(drop / 0.6, 1), 76, RD, 2.5) + tx(60 + W * Math.min(drop / 0.6, 1), 24, '追繳線：−' + f1(drop * 100) + '%', 11, RD);
      [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6].forEach(function (d) { o += tx(60 + W * d / 0.6, 92, '−' + Math.round(d * 100) + '%', 9, 'var(--text-muted)'); });
      [[0.2, '一般修正'], [0.3, '空頭'], [0.5, '股災']].forEach(function (q) { o += ln(60 + W * q[0] / 0.6, 66, 60 + W * q[0] / 0.6, 80, GY) + tx(60 + W * q[0] / 0.6, 108, q[1], 9, GY); });
      view.innerHTML = svgw('0 0 640 116', o);
      inf.innerHTML = msg + '<br>台股歷史上，指數從高點下跌 20%～30% 的修正並不罕見，2008 年更下跌約 60%——追繳線越近，越容易被迫在最低點賣出。' + small('簡化計算：假設單一標的、不計利息與手續費；融資追繳後通常須補足到 166%，否則可能被處分；實際規定與成數依券商與主管機關公告。'); }
    function rect(x, y, w, h, f) { return '<rect x="' + n1(x) + '" y="' + n1(y) + '" width="' + n1(Math.max(w, 0)) + '" height="' + n1(h) + '" fill="' + f + '"/>'; }
    u1();
  }

  /* 3. 凱利與最適槓桿 */
  function initKelly(root, cfg) { head(root, cfg.q); var P = { mu: 8, s: 18, r: 3, L: 1 }, view = el('div');
    var u1 = slider(root, '預期年報酬（股市）', 2, 15, 0.5, P.mu, function (x) { return f1(x) + '%'; }, null, function (x) { P.mu = x; draw(); });
    var u2 = slider(root, '年化波動率', 8, 40, 1, P.s, function (x) { return x + '%'; }, null, function (x) { P.s = x; draw(); });
    var u3 = slider(root, '借錢的利率', 0, 8, 0.25, P.r, function (x) { return f2(x) + '%'; }, null, function (x) { P.r = x; draw(); });
    var u4 = slider(root, '你選擇的槓桿', 0, 4, 0.1, P.L, function (x) { return f1(x) + ' 倍'; }, null, function (x) { P.L = x; draw(); });
    root.appendChild(view); var inf = info(root);
    function g(L) { var mu = P.mu / 100, r = P.r / 100, s2 = Math.pow(P.s / 100, 2); return r + L * (mu - r) - L * L * s2 / 2; }
    function draw() { var d = [], L; for (L = 0; L <= 4.001; L += 0.05) d.push([L, g(L) * 100]); var k = (P.mu - P.r) / 100 / Math.pow(P.s / 100, 2), gv = g(P.L) * 100;
      view.innerHTML = chart(640, 220, [{ d: d, c: BL, n: '長期複利成長率（年化）' }], { x0: 0, x1: 4, y0: -10, y1: Math.max(12, g(k) * 100 * 1.2), xl: '槓桿倍數', yl: '%', hl: [{ y: 0, c: GY, n: '' }], vl: [{ x: Math.min(k, 4), c: GN, n: '凱利：' + f2(k) + ' 倍' }, { x: Math.min(k / 2, 4), c: OR, n: '半凱利' }], pts: [{ x: P.L, y: gv, c: RD, n: f1(gv) + '%' }] });
      inf.innerHTML = '在這些假設下，<b>凱利最適槓桿</b>約 <b>' + f2(k) + ' 倍</b>（=（預期報酬 − 利率）÷ 波動率²）。你選的 ' + f1(P.L) + ' 倍，長期複利成長率約 <b>' + f1(gv) + '%</b>。' + (P.L > k * 2 ? '<br><b style="color:#d0564f">超過凱利的兩倍，長期成長率會低於不借錢——槓桿越大反而越窮。</b>' : P.L > k ? '<br>超過凱利值：報酬增加的速度追不上波動帶來的拖累，風險大增但長期成長反而變少。' : '') + '<br>問題在於：預期報酬與波動都只能<b>估計</b>，估錯一點，最適值就差很多。所以實務上多半只用<b>半凱利</b>或更低——成長只少一點，回撤卻小得多。' + small('連續時間的簡化模型：長期成長率 ≈ r + L(μ−r) − L²σ²/2；假設報酬常態、可隨時調整、無斷頭。'); }
    u1(); u2(); u3(); u4();
  }

  /* 4. 跌幅分批加槓桿 */
  function initLadder(root, cfg) { head(root, cfg.q); var P = { dd: 25 }, view = el('div');
    var S = [[0, 1.0], [10, 1.1], [20, 1.25], [30, 1.4], [40, 1.5]];
    var u = slider(root, '指數從高點的跌幅', 0, 60, 1, P.dd, function (x) { return '−' + x + '%'; }, null, function (x) { P.dd = x; draw(); });
    root.appendChild(view); var inf = info(root);
    function lev(dd) { var l = 1; S.forEach(function (s) { if (dd >= s[0]) l = s[1]; }); return l; }
    function draw() { var d = [], dd, nav = 1, prev = 0, navs = []; for (dd = 0; dd <= 60; dd += 1) { var px1 = 1 - prev / 100, px2 = 1 - dd / 100; if (dd > 0) nav *= 1 + lev(prev) * (px2 / px1 - 1); d.push([dd, lev(dd)]); navs.push([dd, nav]); prev = dd; }
      var cur = navs[P.dd][1], L = lev(P.dd);
      view.innerHTML = chart(640, 200, [{ d: d, c: OR, n: '槓桿倍數' }, { d: navs.map(function (p) { return [p[0], p[1] * 1.5]; }), c: BL, n: '帳戶淨值（×1.5 顯示）', dash: '4 3' }], { x0: 0, x1: 60, y0: 0, y1: 1.6, xl: '從高點的跌幅（%）', yl: '倍', pts: [{ x: P.dd, y: L, c: RD, n: f2(L) + ' 倍' }] });
      var need = 1 / (1 - P.dd / 100) - 1, back = (1 / cur - 1);
      inf.innerHTML = '一套<b>跌幅階梯</b>：跌 10% 加到 1.1 倍、跌 20% 加到 1.25 倍、跌 30% 加到 1.4 倍、跌 40% 加到 1.5 倍（上限）。<br>指數跌 ' + P.dd + '% 時，槓桿 <b>' + f2(L) + ' 倍</b>，帳戶淨值約剩 <b>' + Math.round(cur * 100) + '%</b>（若一直不加槓桿則剩 ' + (100 - P.dd) + '%）。<br>指數要漲 ' + Math.round(need * 100) + '% 才回到高點；因為低點持有更多部位，你的帳戶只需要更少的反彈就回本——但如果繼續下跌，損失也會更大。' + small('示意：假設逐步下跌、每到門檻立即調整；未計利息。階梯的檔位只是例子，實際要依自己的承受度與斷頭線設計（見第 23 課）。'); }
    u();
  }

  /* 5. 波動率目標法 */
  function initVoltgt(root, cfg) { head(root, cfg.q); var P = { t: 15, cap: 1.5 }, view = el('div');
    var u1 = slider(root, '目標波動率', 8, 25, 1, P.t, function (x) { return x + '%'; }, null, function (x) { P.t = x; draw(); });
    var u2 = slider(root, '槓桿上限', 1, 2, 0.1, P.cap, function (x) { return f1(x) + ' 倍'; }, null, function (x) { P.cap = x; draw(); });
    root.appendChild(view); var inf = info(root);
    var V = []; (function () { for (var m = 0; m <= 48; m++) { var v = 13 + 3 * Math.sin(m / 3); if (m >= 18 && m <= 22) v = [25, 45, 38, 28, 22][m - 18]; if (m > 22 && m < 30) v = 20 - (m - 23); V.push([m, v]); } })();
    function draw() { var L = V.map(function (p) { return [p[0], Math.min(P.cap, P.t / p[1])]; }), avg = L.reduce(function (s, p) { return s + p[1]; }, 0) / L.length;
      view.innerHTML = chart(640, 200, [{ d: V.map(function (p) { return [p[0], p[1] / 20]; }), c: GY, n: '市場波動率（÷20 顯示）', dash: '4 3' }, { d: L, c: BL, n: '槓桿倍數' }], { x0: 0, x1: 48, y0: 0, y1: 2.4, xl: '月', yl: '倍', hl: [{ y: 1, c: GN, n: '1 倍' }] });
      var minL = Math.min.apply(null, L.map(function (p) { return p[1]; }));
      inf.innerHTML = '<b>槓桿 = 目標波動率 ÷ 市場目前的波動率</b>（不超過上限 ' + f1(P.cap) + ' 倍）。平靜的時候（波動約 10%～16%）自動加到 ' + f2(Math.min(P.cap, P.t / 10)) + ' 倍左右；危機爆發、波動衝到 45% 時，自動降到 <b>' + f2(minL) + ' 倍</b>。平均槓桿約 ' + f2(avg) + ' 倍。<br>研究發現，市場的大跌常伴隨波動的暴增，所以這個方法通常能在崩盤<b>初期</b>就降低槓桿，減少最大回撤。缺點是：波動高點常常也接近市場的低點，它可能讓你在反彈的初期部位偏低。' + small('示意的波動率路徑，第 18～22 個月模擬一次危機；實務上常用過去 1～3 個月的實際波動率估計。'); }
    u1(); u2();
  }

  /* 6. 情境回測 */
  function initBt(root, cfg) { head(root, cfg.q); var P = { k: 0 }, view = el('div');
    var SC = [['泡沫與崩盤', [0.012, 0.012, 0.015, 0.02, 0.02, 0.01, -0.03, -0.06, -0.1, -0.08, -0.12, -0.05, 0.04, 0.06, 0.03, 0.05, 0.02, 0.03, 0.02, 0.025, 0.01, 0.02]], ['V 型急跌', [0.01, 0.015, 0.01, 0.012, 0.01, -0.08, -0.15, 0.1, 0.07, 0.05, 0.04, 0.03, 0.02, 0.02, 0.015, 0.01, 0.02, 0.01]], ['長期盤整', [0.04, -0.04, 0.05, -0.05, 0.03, -0.03, 0.04, -0.05, 0.05, -0.04, 0.03, -0.03, 0.04, -0.04, 0.05, -0.05, 0.03, -0.02]], ['穩定牛市', [0.015, 0.01, 0.02, -0.01, 0.015, 0.02, 0.01, -0.02, 0.02, 0.015, 0.01, 0.02, -0.01, 0.015, 0.02, 0.01, 0.015, 0.02]]];
    presets(root, SC, function (o, i) { P.k = i; draw(); });
    root.appendChild(view); var inf = info(root);
    function run(rets, mode) { var nav = 1, px = 1, hi = 1, out = [[0, 1]], mdd = 0, peak = 1, ma = [1];
      rets.forEach(function (q, i) { for (var d = 0; d < 21; d++) { var r = Math.pow(1 + q, 1 / 21) - 1, L;
          var dd = 1 - px / hi, m6 = ma.slice(-126), avg = m6.reduce(function (s, v) { return s + v; }, 0) / m6.length;
          if (mode === 0) L = 1; else if (mode === 1) L = 2; else { L = dd >= 0.3 ? 1.4 : dd >= 0.2 ? 1.25 : dd >= 0.1 ? 1.1 : 1.0; if (px < avg && dd < 0.2) L = Math.min(L, 0.8); if (px / Math.min.apply(null, ma.slice(-252)) > 1.6) L = Math.min(L, 0.9); }
          nav *= 1 + L * r - (L > 1 ? (L - 1) * 0.04 / 252 : 0); px *= 1 + r; hi = Math.max(hi, px); ma.push(px); peak = Math.max(peak, nav); mdd = Math.max(mdd, 1 - nav / peak); }
        out.push([i + 1, nav]); });
      return { d: out, end: nav, mdd: mdd }; }
    function draw() { var s = SC[P.k][1], a = run(s, 0), b = run(s, 1), c = run(s, 2);
      view.innerHTML = chart(640, 230, [{ d: a.d, c: GY, n: '不開槓（1 倍）' }, { d: b.d, c: RD, n: '固定 2 倍（每日重設）' }, { d: c.d, c: BL, n: '規則化調整' }], { x0: 0, x1: s.length, y0: 0, xl: '月', yl: '淨值' });
      function row(n, r) { return n + '：期末 <b>' + f2(r.end) + '</b>、最大回撤 <b>' + Math.round(r.mdd * 100) + '%</b>'; }
      inf.innerHTML = row('不開槓', a) + '<br>' + row('固定 2 倍', b) + '<br>' + row('規則化調整', c) + '<br>規則：跌幅階梯加碼（最多 1.4 倍），跌破半年均線時降到 0.8 倍，一年內上漲超過六成時降到 0.9 倍。<br>沒有一種方法在所有情境都最好：<b>穩定牛市</b>中固定 2 倍最賺；<b>泡沫崩盤</b>中被重創、<b>盤整</b>中被波動拖累磨損。規則的價值在於<b>避開最壞的結果</b>，而不是賺最多。' + small('完全虛構的教學情境，不是任何真實市場的歷史資料；借款成本以年 4% 估計。'); }
    draw();
  }

  function initAll() { document.querySelectorAll('.lv-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ decay: initDecay, margin: initMargin, kelly: initKelly, ladder: initLadder, voltgt: initVoltgt, bt: initBt })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def make(icon, note):
    return make_lesson(icon, note, LVLIB, "lv-w")


def guide(title, h1, items, desc):
    body = [("raw", u"<script>%s</script>" % LVLIB)]
    for i, (h, w) in enumerate(items):
        body += [("h", u"%d. %s" % (i + 1, h)), w]
    return {"file": "guide.html", "title": title, "h1": h1, "icon": u"🧪", "description": desc, "body": body}
