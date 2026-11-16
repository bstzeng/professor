# -*- coding: utf-8 -*-
"""〈貝氏統計〉（bay_）共用：課程包裝與 BAYLIB 互動元件（class="bay-w"）。

  medtest  醫學檢驗：盛行率、敏感度、特異度 → 1000 人方格與陽性預測值
  beta     Beta—二項式：先驗 a、b 與觀察到的成功次數 → 先驗、似然、後驗與可信區間
  mcmc     梅特羅波利斯演算法：步長、步數 → 軌跡與直方圖
  lindley  p 值與貝氏因子：擲硬幣次數與正面比例 → p 值、貝氏因子、H0 的後驗機率
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

BAY_NOTE = (u"本課的推導以主要步驟為主；互動模擬為教學用的小型版本。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def byw(cfg, maxw=680):
    return wdg("bay-w", cfg, maxw)


BAYLIB = r"""
(function () {
  if (window.__bayLib) return; window.__bayLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function lgam(x) { var c = [76.18009172947146, -86.50532032941677, 24.01409824083091, -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5], y = x, t = x + 5.5; t -= (x + 0.5) * Math.log(t); var s = 1.000000000190015; for (var j = 0; j < 6; j++) s += c[j] / ++y; return -t + Math.log(2.5066282746310005 * s / x); }
  function lbeta(a, b) { return lgam(a) + lgam(b) - lgam(a + b); }
  function bpdf(x, a, b) { if (x <= 0 || x >= 1) return 0; return Math.exp((a - 1) * Math.log(x) + (b - 1) * Math.log(1 - x) - lbeta(a, b)); }
  function pct(v) { return (Math.round(v * 1000) / 10) + '%'; }

  function initMed(root, cfg) {
    head(root, cfg.q); var P = { prev: cfg.prev || 0.01, sens: cfg.sens || 0.9, spec: cfg.spec || 0.91 }, view = el('div'), inf;
    var us = [slider(root, '盛行率（人群中真正有病的比例）', 0.001, 0.5, 0.001, P.prev, pct, null, function (x) { P.prev = x; draw(); }),
      slider(root, '敏感度（有病的人驗出陽性的機率）', 0.5, 1, 0.01, P.sens, pct, null, function (x) { P.sens = x; draw(); }),
      slider(root, '特異度（沒病的人驗出陰性的機率）', 0.5, 1, 0.005, P.spec, pct, null, function (x) { P.spec = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var N = 1000, sick = Math.round(N * P.prev), tp = Math.round(sick * P.sens), fn = sick - tp, healthy = N - sick, fp = Math.round(healthy * (1 - P.spec)), tn = healthy - fp;
      var cells = []; for (var i = 0; i < tp; i++) cells.push(RD); for (i = 0; i < fn; i++) cells.push('#e9b3ae'); for (i = 0; i < fp; i++) cells.push(OR); for (i = 0; i < tn; i++) cells.push('#d6dbe1');
      var g = '', cw = 15.5, cols = 40; cells.forEach(function (c, i) { var x = (i % cols) * cw + 6, y = Math.floor(i / cols) * cw + 6; g += '<rect x="' + n1(x) + '" y="' + n1(y) + '" width="12" height="12" rx="3" fill="' + c + '"/>'; });
      var lg = [[RD, '有病、陽性（' + tp + '）'], ['#e9b3ae', '有病、陰性（' + fn + '）'], [OR, '沒病、陽性（' + fp + '）'], ['#d6dbe1', '沒病、陰性（' + tn + '）']], ly = 25 * cw + 18;
      lg.forEach(function (l, i) { g += '<rect x="' + (6 + i * 158) + '" y="' + ly + '" width="12" height="12" rx="3" fill="' + l[0] + '"/>' + tx(22 + i * 158, ly + 11, l[1], 12, null, 'start'); });
      view.innerHTML = svgw('0 0 640 ' + (ly + 22), g);
      var exact = P.prev * P.sens / (P.prev * P.sens + (1 - P.prev) * (1 - P.spec));
      inf.innerHTML = '1000 人中，約 <b>' + sick + '</b> 人有病。驗出陽性的共 <b>' + (tp + fp) + '</b> 人，其中真的有病的只有 <b>' + tp + '</b> 人。' +
        '<br>所以：<b>驗出陽性時，真的有病的機率 = ' + pct(exact) + '</b>（陽性預測值）。' +
        (exact < 0.5 ? '<br>即使檢驗相當準確，因為疾病很罕見，<b>大部分的陽性是假警報</b>——沒病的人太多了，就算只有一小部分驗錯，也比真正有病的人多。' : '<br>盛行率夠高時，陽性結果就比較可信。'); }
    us.forEach(function (u) { u(); });
  }

  function initBeta(root, cfg) {
    head(root, cfg.q); var P = { a: cfg.a || 1, b: cfg.b || 1, n: cfg.n || 10, k: cfg.k || 7 }, view = el('div'), inf, uk;
    var us = [slider(root, '先驗 a（想像中已看過的「成功」次數 + 1）', 0.5, 50, 0.5, P.a, f1, null, function (x) { P.a = x; draw(); }),
      slider(root, '先驗 b（想像中已看過的「失敗」次數 + 1）', 0.5, 50, 0.5, P.b, f1, null, function (x) { P.b = x; draw(); }),
      slider(root, '試驗次數 n', 0, 200, 1, P.n, function (x) { return x; }, null, function (x) { P.n = x; if (P.k > x) { P.k = x; } uk && uk(); draw(); })];
    uk = slider(root, '成功次數 k', 0, 200, 1, P.k, function (x) { return x; }, null, function (x) { P.k = Math.min(x, P.n); draw(); });
    root.appendChild(view); inf = info(root);
    function interval(a, b) { var M = 2000, c = 0, lo = null, hi = null, tot = 0, xs = []; for (var i = 1; i < M; i++) { var x = i / M; xs.push(bpdf(x, a, b)); tot += xs[i - 1]; }
      for (i = 1; i < M; i++) { c += xs[i - 1] / tot; if (lo === null && c >= 0.025) lo = i / M; if (hi === null && c >= 0.975) hi = i / M; } return [lo, hi]; }
    function draw() { var k = Math.min(P.k, P.n), a2 = P.a + k, b2 = P.b + P.n - k, pr = [], li = [], po = [], ymax = 0, lmax = 0, L = [];
      for (var i = 1; i < 400; i++) { var x = i / 400, l = P.n ? Math.exp(k * Math.log(x) + (P.n - k) * Math.log(1 - x) - lbeta(k + 1, P.n - k + 1)) : 1; L.push(l); }
      for (i = 1; i < 400; i++) { x = i / 400; var p1 = bpdf(x, P.a, P.b), p2 = bpdf(x, a2, b2); pr.push([x, p1]); po.push([x, p2]); li.push([x, L[i - 1]]); ymax = Math.max(ymax, p2, Math.min(p1, 30), Math.min(L[i - 1], 30)); }
      ymax = Math.min(ymax * 1.1, 30);
      var ci = interval(a2, b2), mean = a2 / (a2 + b2);
      view.innerHTML = chart(640, 250, [{ d: pr, c: GY, n: '先驗', w: 1.8, dash: '5,4' }, { d: li, c: GN, n: '似然（資料）', w: 1.6 }, { d: po, c: BL, n: '後驗', w: 2.4 }], { x0: 0, x1: 1, y0: 0, y1: ymax, xl: '成功機率 θ', vl: [{ x: ci[0], c: BL, n: '' }, { x: ci[1], c: BL, n: '' }] });
      inf.innerHTML = '先驗 Beta(' + f1(P.a) + ', ' + f1(P.b) + ')，觀察到 ' + P.n + ' 次中成功 ' + k + ' 次 → 後驗 <b>Beta(' + f1(a2) + ', ' + f1(b2) + ')</b>。只要把成功次數加到 a、失敗次數加到 b。' +
        '<br>後驗平均 = <b>' + f2(mean) + '</b>；95% 可信區間 = <b>[' + f2(ci[0]) + ', ' + f2(ci[1]) + ']</b>（θ 有 95% 的機率落在這裡）。' +
        '<br>' + (P.n < 20 ? '資料少的時候，先驗的影響很明顯。把 n 調大，後驗會越來越窄，越來越貼近資料。' : '資料多了，先驗的影響越來越小：不同先驗的人，最後會得到差不多的結論。'); }
    us.forEach(function (u) { u(); }); uk();
  }

  function initMCMC(root, cfg) {
    head(root, cfg.q); var P = { s: 1, n: 2000 }, view = el('div'), view2 = el('div'), inf;
    var b = bar(root); var rb = btn('重新執行'); rb.onclick = function () { draw(); }; b.appendChild(rb);
    var us = [slider(root, '提議的步長', 0.05, 10, 0.05, P.s, f2, null, function (x) { P.s = x; draw(); }),
      slider(root, '步數', 100, 20000, 100, P.n, function (x) { return x; }, null, function (x) { P.n = x; draw(); })];
    root.appendChild(view); root.appendChild(view2); inf = info(root);
    function tgt(x) { return 0.7 * Math.exp(-0.5 * (x + 1.5) * (x + 1.5) / 0.36) / 0.6 + 0.3 * Math.exp(-0.5 * (x - 2) * (x - 2) / 0.64) / 0.8; }
    function randn() { var u = 1 - Math.random(), v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
    function draw() { var x = 4, acc = 0, ch = []; for (var i = 0; i < P.n; i++) { var y = x + P.s * randn(); if (Math.random() < tgt(y) / tgt(x)) { x = y; acc++; } ch.push(x); }
      var tr = []; var st = Math.max(1, Math.floor(P.n / 600)); for (i = 0; i < P.n; i += st) tr.push([i, ch[i]]);
      var bins = 60, lo = -5, hi = 5, h = new Array(bins).fill(0); ch.forEach(function (v) { var k = Math.floor((v - lo) / (hi - lo) * bins); if (k >= 0 && k < bins) h[k]++; });
      var bw = (hi - lo) / bins, hd = [], td = [], Z = 0.7 * Math.sqrt(2 * Math.PI) + 0.3 * Math.sqrt(2 * Math.PI);
      for (i = 0; i < bins; i++) { var c = lo + (i + 0.5) * bw, v2 = h[i] / (P.n * bw); hd.push([lo + i * bw, v2]); hd.push([lo + (i + 1) * bw, v2]); }
      for (i = 0; i <= 200; i++) { var xx = lo + i * (hi - lo) / 200; td.push([xx, tgt(xx) / Z]); }
      view.innerHTML = chart(640, 170, [{ d: tr, c: BL, n: '軌跡（每一步的位置）', w: 1 }], { x0: 0, x1: P.n, y0: -5, y1: 5, xl: '步數' });
      view2.innerHTML = chart(640, 200, [{ d: hd, c: OR, n: '樣本的直方圖', w: 1.6 }, { d: td, c: GY, n: '真正的分布', w: 2, dash: '5,4' }], { x0: lo, x1: hi, y0: 0, y1: 0.75, xl: 'θ' });
      var ar = acc / P.n;
      inf.innerHTML = '接受率：<b>' + pct(ar) + '</b>。' + (P.s < 0.3 ? '<br>步長太<b>小</b>：幾乎每一步都被接受，但每步只移動一點點，像在原地踏步，很難跨到另一個峰。' : P.s > 4 ? '<br>步長太<b>大</b>：大部分的提議跳到機率很低的地方被拒絕，鏈常常卡在原地不動。' : '<br>步長適中：鏈能在兩個峰之間來回移動，直方圖逐漸逼近真正的分布。') +
        '<br>鏈從 θ = 4 出發，開頭的一段還沒「找到」高機率的區域——實務上會丟掉這段（燒入期）。'; }
    us.forEach(function (u) { u(); });
  }

  function binP(n, k) { var z = (Math.abs(k - n / 2) - 0.5) / Math.sqrt(n / 4); if (z < 0) return 1; var t = 1 / (1 + 0.2316419 * z), d = 0.3989423 * Math.exp(-z * z / 2), q = d * t * (0.3193815 + t * (-0.3565638 + t * (1.781478 + t * (-1.821256 + t * 1.330274)))); return Math.min(1, 2 * q); }
  function initLind(root, cfg) {
    head(root, cfg.q); var P = { ln: 4, z: 2.2 }, view = el('div'), inf;
    var us = [slider(root, '擲硬幣次數 n（以 10 為底的對數）', 1.5, 6, 0.1, P.ln, function (x) { return Math.round(Math.pow(10, x)).toLocaleString(); }, null, function (x) { P.ln = x; draw(); }),
      slider(root, '正面次數偏離一半多少個標準差（z）', 0, 4, 0.05, P.z, f2, null, function (x) { P.z = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function calc(n, z) { var k = Math.round(n / 2 + z * Math.sqrt(n) / 2); k = Math.max(0, Math.min(n, k));
      var lb = lgam(n + 1) - lgam(k + 1) - lgam(n - k + 1), l0 = lb + n * Math.log(0.5), l1 = -Math.log(n + 1), bf01 = Math.exp(l0 - l1); return { k: k, p: binP(n, k), bf: bf01, post: bf01 / (1 + bf01) }; }
    function draw() { var n = Math.round(Math.pow(10, P.ln)), r = calc(n, P.z), cur = [];
      for (var i = 15; i <= 60; i++) { var nn = Math.round(Math.pow(10, i / 10)), rr = calc(nn, P.z); cur.push([i / 10, rr.post]); }
      view.innerHTML = chart(640, 230, [{ d: cur, c: PU, n: 'H₀（硬幣公平）的後驗機率', w: 2.2 }], { x0: 1.5, x1: 6, y0: 0, y1: 1, xl: 'log₁₀(擲硬幣次數)', hl: [{ y: 0.5, c: GY, n: '' }], pts: [{ x: P.ln, y: r.post, c: RD, n: '' }] });
      inf.innerHTML = '擲 <b>' + n.toLocaleString() + '</b> 次，正面 <b>' + r.k.toLocaleString() + '</b> 次（' + f2(r.k / n * 100) + '%）。' +
        '<br>p 值 = <b>' + (r.p < 0.001 ? r.p.toExponential(1) : r.p.toFixed(3)) + '</b>' + (r.p < 0.05 ? '：小於 0.05，「拒絕硬幣公平的假設」。' : '：不顯著。') +
        '<br>貝氏因子 BF₀₁ = <b>' + (r.bf > 1000 || r.bf < 0.001 ? r.bf.toExponential(1) : f2(r.bf)) + '</b>；先驗各半時，硬幣公平的後驗機率 = <b>' + pct(r.post) + '</b>。' +
        (r.p < 0.05 && r.post > 0.5 ? '<br><b>林德利悖論</b>：p 值說「顯著」，貝氏分析卻說「硬幣多半是公平的」。固定 z，擲得越多次，H₀ 的後驗機率越高。' : '<br>固定 z（例如 2，p ≈ 0.05），把 n 往右拉，看 H₀ 的後驗機率怎麼變。'); }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.bay-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ medtest: initMed, beta: initBeta, mcmc: initMCMC, lindley: initLind })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🎲", BAY_NOTE, BAYLIB, "bay-w")

MEDTEST = byw({"t": "medtest", "q": u"醫學檢驗：驗出陽性，真的有病的機率是多少", "prev": 0.01, "sens": 0.9, "spec": 0.91})
BETAW = byw({"t": "beta", "q": u"Beta—二項式：先驗 + 資料 = 後驗", "a": 2, "b": 2, "n": 10, "k": 7})
MCMCW = byw({"t": "mcmc", "q": u"梅特羅波利斯演算法：隨機漫步出一個分布"})
LINDLEY = byw({"t": "lindley", "q": u"p 值與貝氏因子：同樣的 p 值，不同的結論"})
