# -*- coding: utf-8 -*-
"""〈肥胖、代謝與 GLP-1 減重藥〉（glp_）共用：課程包裝與 GLPLIB 互動元件（class="glp-w"）。

  bmi     BMI 與腰圍：台灣的標準
  weight  體重變化模型：每天的熱量缺口 → 體重隨時間的變化（含代謝適應），與 7,700 大卡法則比較
  ogtt    口服葡萄糖耐受試驗：正常、胰島素阻抗、糖尿病、使用 GLP-1 藥物的血糖與胰島素曲線
  trial   臨床試驗的體重曲線：安慰劑與各種藥物；停藥後的復胖
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

GLP_NOTE = u"本課程為科普與教育用途，不能取代醫療建議；任何藥物的使用都必須經過醫師評估與處方。互動模擬為教學用的簡化模型。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def gw(cfg, maxw=680):
    return wdg("glp-w", cfg, maxw)


GLPLIB = r"""
(function () {
  if (window.__glpLib) return; window.__glpLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }

  function initBMI(root, cfg) {
    head(root, cfg.q); var P = { h: 170, w: 72, wc: 86, sex: 0 }, view = el('div'), inf;
    var b = bar(root); [['男性', 0], ['女性', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.sex = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    var us = [slider(root, '身高（公分）', 140, 200, 1, P.h, function (x) { return x + ' 公分'; }, null, function (x) { P.h = x; draw(); }),
      slider(root, '體重（公斤）', 35, 150, 0.5, P.w, function (x) { return x + ' 公斤'; }, null, function (x) { P.w = x; draw(); }),
      slider(root, '腰圍（公分）', 55, 140, 1, P.wc, function (x) { return x + ' 公分'; }, null, function (x) { P.wc = x; draw(); })];
    root.appendChild(view); inf = info(root);
    var Z = [[0, 18.5, '過輕', '#9cc3e6'], [18.5, 24, '健康體位', '#9fd3a8'], [24, 27, '過重', '#f2d38a'], [27, 30, '輕度肥胖', '#f0b27a'], [30, 35, '中度肥胖', '#e88a6a'], [35, 45, '重度肥胖', '#d0564f']];
    function draw() { var m = P.h / 100, bmi = P.w / (m * m), g = '', x0 = 20, W = 600, lo = 15, hi = 45;
      function sx(v) { return x0 + (Math.min(Math.max(v, lo), hi) - lo) / (hi - lo) * W; }
      Z.forEach(function (z) { var a = sx(Math.max(z[0], lo)), c = sx(z[1]); g += '<rect x="' + n1(a) + '" y="20" width="' + n1(c - a) + '" height="34" fill="' + z[3] + '"/>' + tx((a + c) / 2, 42, z[2], 10.5, '#333'); });
      [18.5, 24, 27, 30, 35].forEach(function (v) { g += tx(sx(v), 70, v, 10, 'var(--text-muted)'); });
      g += '<path d="M' + n1(sx(bmi)) + ' 14 l-7 -10 h14 z" fill="#333"/>' + tx(sx(bmi), 2, '', 10);
      view.innerHTML = svgw('0 0 640 80', g);
      var cat = Z.filter(function (z) { return bmi >= z[0] && bmi < z[1]; })[0] || Z[Z.length - 1], lim = P.sex ? 80 : 90, cw = P.wc >= lim, lw = 18.5 * m * m, hw = 24 * m * m;
      inf.innerHTML = 'BMI = 體重 ÷ 身高² = ' + P.w + ' ÷ ' + f2(m) + '² = <b>' + f1(bmi) + '</b>，屬於「<b>' + cat[2] + '</b>」。這個身高的健康體重範圍約 ' + f1(lw) + '～' + f1(hw) + ' 公斤。' +
        '<br>腰圍 ' + P.wc + ' 公分：' + (cw ? '<b>超過</b>' : '未超過') + '台灣的標準（' + (P.sex ? '女性' : '男性') + ' ' + lim + ' 公分）' + (cw ? '，代表<b>腹部肥胖</b>——內臟脂肪較多，與糖尿病、心血管疾病的風險更相關。' : '。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">BMI 只是篩檢工具：肌肉發達的人 BMI 可能偏高，而 BMI 正常的人也可能有過多的內臟脂肪。台灣的分級（24、27）比世界衛生組織的國際標準（25、30）低，因為亞洲人在較低的 BMI 就有較高的代謝風險。</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initWeight(root, cfg) {
    head(root, cfg.q); var P = { w0: 90, d: 500, ad: 1 }, view = el('div'), inf;
    var us = [slider(root, '開始的體重（公斤）', 60, 150, 1, P.w0, function (x) { return x + ' 公斤'; }, null, function (x) { P.w0 = x; draw(); }),
      slider(root, '每天少吃的熱量（大卡）', 100, 1000, 50, P.d, function (x) { return x + ' 大卡'; }, null, function (x) { P.d = x; draw(); })];
    var b = bar(root), ab = btn('代謝適應：開'); ab.onclick = function () { P.ad ^= 1; ab.textContent = '代謝適應：' + (P.ad ? '開' : '關'); draw(); }; b.appendChild(ab);
    root.appendChild(view); inf = info(root);
    function draw() { var rho = 7700, k = 22, W = P.w0, naive = [], model = [], days = 3 * 365, w1 = null, wInf = null;
      for (var t = 0; t <= days; t += 5) { naive.push([t / 365, P.w0 - P.d * t / rho]);
        model.push([t / 365, W]); for (var s = 0; s < 5; s++) { var dW = W - P.w0, adapt = P.ad ? Math.min(0.15 * P.d, 4 * -dW) : 0, gap = P.d - adapt + k * dW; W -= gap / rho; } if (w1 === null && t >= 365) w1 = W; }
      wInf = P.w0 - (P.d - (P.ad ? 0.15 * P.d : 0)) / k;
      view.innerHTML = chart(640, 250, [{ d: naive, c: GY, n: '「每 7,700 大卡瘦一公斤」的直覺', w: 1.6, dash: '5,4' }, { d: model, c: RD, n: '考慮代謝變化的模型', w: 2.4 }], { x0: 0, x1: 3, y0: Math.max(30, P.w0 - 60), y1: P.w0 + 3, xl: '年', yl: '體重（公斤）' });
      inf.innerHTML = '每天少吃 ' + P.d + ' 大卡：直覺的算法說一年會瘦 <b>' + f1(P.d * 365 / rho) + '</b> 公斤，而且會一直瘦下去。模型的結果是：一年後約瘦 <b>' + f1(P.w0 - w1) + '</b> 公斤，之後越來越慢，最後停在約 <b>' + f1(wInf) + '</b> 公斤。' +
        '<br>原因：體重變輕，身體每天消耗的能量也變少（大約每公斤每天 20 多大卡）——原本的「熱量缺口」逐漸被吃掉。' + (P.ad ? '再加上<b>代謝適應</b>：減重時身體會額外地「省電」，讓缺口更小。' : '') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">參考美國國家衛生研究院霍爾等人的動態模型概念，大幅簡化。真實的變化因人而異。</span>'; }
    us.forEach(function (u) { u(); });
  }

  var OG = [['正常', 0], ['胰島素阻抗', 1], ['第二型糖尿病', 2], ['糖尿病＋GLP-1 藥物', 3]];
  function initOGTT(root, cfg) {
    head(root, cfg.q); var P = { s: 0 }, view = el('div'), iv = el('div'), inf;
    var b = bar(root); OG.forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.s = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    root.appendChild(view); root.appendChild(iv); inf = info(root);
    function curve(base, peak, tp, w, tail) { var d = []; for (var t = 0; t <= 180; t += 3) { var g = base + peak * Math.exp(-Math.pow((t - tp) / w, 2)) + (t > tp ? tail * (1 - Math.exp(-(t - tp) / 60)) : 0); d.push([t, g]); } return d; }
    var G = [curve(90, 50, 40, 35, 0), curve(98, 75, 55, 45, 5), curve(140, 120, 75, 60, 20), curve(125, 70, 80, 70, 5)], I = [curve(8, 50, 35, 30, 0), curve(18, 120, 60, 45, 10), curve(15, 35, 90, 60, 0), curve(15, 70, 50, 45, 0)];
    var TXT = ['喝下 75 公克葡萄糖後，血糖約在 30～60 分鐘達到高峰，兩小時內回到 140 mg/dL 以下。胰島素迅速上升，把葡萄糖送進肌肉與肝臟。',
      '血糖仍大致正常，但胰腺必須分泌<b>多得多</b>的胰島素才能做到——細胞對胰島素「不敏感」了。這個階段可能持續多年，常與腹部肥胖同時出現。',
      '胰腺長期過勞，β 細胞的功能衰退：胰島素的分泌<b>又少又慢</b>，空腹血糖 ≥ 126、兩小時血糖 ≥ 200 mg/dL，就達到糖尿病的診斷標準。',
      'GLP-1 藥物讓胰腺在血糖高時分泌更多胰島素（不容易低血糖，因為它依賴血糖的高低），抑制升糖素，並延緩胃的排空——血糖的高峰變低、變平。'];
    function draw() { var s = P.s; view.innerHTML = chart(640, 200, [{ d: G[0], c: GY, n: '正常（參考）', w: 1.2, dash: '4,3' }, { d: G[s], c: RD, n: '血糖（mg/dL）', w: 2.4 }], { x0: 0, x1: 180, y0: 60, y1: 300, xl: '喝下葡萄糖後的分鐘數', hl: [{ y: 200, c: PU, n: '兩小時 200：糖尿病' }, { y: 140, c: OR, n: '140' }] });
      iv.innerHTML = chart(640, 160, [{ d: I[0], c: GY, n: '正常（參考）', w: 1.2, dash: '4,3' }, { d: I[s], c: BL, n: '胰島素（相對值）', w: 2.4 }], { x0: 0, x1: 180, y0: 0, y1: 150, xl: '分鐘' });
      inf.innerHTML = '<b>' + OG[s][0] + '</b>：' + TXT[s] + '<br><span style="font-size:0.9em;color:var(--text-muted)">示意曲線，非真實病人的數據。診斷請依醫師的檢查。</span>'; }
    draw();
  }

  var TR = [['安慰劑', 2.4, GY, 0], ['利拉魯肽（每天注射）', 7.5, PU, 1], ['口服 orforglipron', 12.4, GN, 1], ['司美格魯肽（每週注射）', 15, BL, 1], ['替爾泊肽（每週注射）', 21, RD, 1]];
  function initTrial(root, cfg) {
    head(root, cfg.q); var P = { stop: 0 }, view = el('div'), inf;
    var b = bar(root), sb = btn('在第 68 週停藥：關'); sb.onclick = function () { P.stop ^= 1; sb.textContent = '在第 68 週停藥：' + (P.stop ? '開' : '關'); draw(); }; b.appendChild(sb);
    root.appendChild(view); inf = info(root);
    function draw() { var S = TR.map(function (r) { var d = []; for (var w = 0; w <= (P.stop ? 120 : 72); w += 2) { var y = -r[1] * (1 - Math.exp(-w / 18)) / (1 - Math.exp(-68 / 18)); if (w > 68 && P.stop && r[3]) { var lost = r[1]; y = -lost + lost * (2 / 3) * (1 - Math.exp(-(w - 68) / 16)); } d.push([w, Math.max(y, -r[1] * 1.02)]); } return { d: d, c: r[2], n: r[0], w: 2 }; });
      view.innerHTML = chart(640, 260, S, { x0: 0, x1: P.stop ? 120 : 72, y0: -24, y1: 2, xl: '週數', yl: '體重變化（%）', vl: P.stop ? [{ x: 68, c: OR, n: '停藥' }] : [] });
      inf.innerHTML = '大型臨床試驗中，約一年半後的平均體重變化（配合飲食與運動）：安慰劑約 −2～3%、利拉魯肽約 −5～8%、口服 orforglipron（2026 年核准）最高劑量約 −12%、司美格魯肽約 −15%、替爾泊肽最高劑量約 −20%。這是過去任何減重藥物都達不到的效果。' +
        (P.stop ? '<br><b>停藥之後</b>：司美格魯肽的試驗追蹤發現，停藥一年後，平均<b>回復了約三分之二</b>減掉的體重，血壓、血糖等改善也跟著退回。這顯示肥胖是一種<b>慢性</b>疾病——藥物控制它，但沒有「治癒」它。' : '<br>按上方的按鈕，看看停藥後會發生什麼。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">示意曲線：依各試驗公布的平均值繪製，各試驗的設計、族群與時間不同，不宜直接比較；個人的反應差異很大。</span>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.glp-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ bmi: initBMI, weight: initWeight, ogtt: initOGTT, trial: initTrial })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"⚖️", GLP_NOTE, GLPLIB, "glp-w")

BMI = gw({"t": "bmi", "q": u"BMI 與腰圍：台灣的標準"})
WEIGHT = gw({"t": "weight", "q": u"每天少吃一點，一年會瘦多少"})
OGTT = gw({"t": "ogtt", "q": u"喝下一杯糖水之後：血糖與胰島素"})
TRIAL = gw({"t": "trial", "q": u"臨床試驗中的體重變化"})
