# -*- coding: utf-8 -*-
"""〈工程災難與事故調查〉（eda_）共用：課程包裝與 EDALIB 互動元件（class="eda-w"）。

  flutter  顫振：風速 → 橋面扭轉振幅隨時間（氣動阻尼由正轉負）
  fatigue  疲勞裂紋：應力範圍、初始裂紋、檢查間隔 → 帕里斯定律的裂紋成長與檢查能否及時發現
  oring    挑戰者號：O 型環損傷與發射溫度（只看有損傷的 vs 全部）→ 邏輯迴歸外推
  swiss    瑞士乳酪模型：防護層數、每層的漏洞機率、共同原因 → 事故機率
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

EDA_NOTE = (u"本課程討論真實的事故與罹難者，數字以官方調查報告與常見的估計為主；互動模擬為教學用的簡化模型。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def edw(cfg, maxw=680):
    return wdg("eda-w", cfg, maxw)


EDALIB = r"""
(function () {
  if (window.__edaLib) return; window.__edaLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }

  function initFlutter(root, cfg) {
    head(root, cfg.q); var P = { v: 40 }, view = el('div'), inf, Vc = 55;
    var u = slider(root, '風速（公里／小時）', 0, 90, 1, P.v, function (x) { return x + ' km/h'; }, null, function (x) { P.v = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var z = 0.05 * (1 - P.v / Vc), w = 2 * Math.PI * 0.2, d = [], th = 1, om = 0, dt = 0.05, mx = 0, gust = 0;
      for (var i = 0; i < 2400; i++) { var t = i * dt, f = P.v > 5 ? 0.02 * Math.sin(1.7 * t) * P.v / 60 : 0; var acc = -2 * z * w * om - w * w * th + f; om += acc * dt; th += om * dt; th = Math.max(-40, Math.min(40, th)); if (i % 4 === 0) d.push([t, th]); mx = Math.max(mx, Math.abs(th)); }
      view.innerHTML = chart(640, 230, [{ d: d, c: z < 0 ? RD : BL, n: '橋面的扭轉角（度）', w: 1.4 }], { x0: 0, x1: 120, y0: -Math.max(mx, 2) * 1.1, y1: Math.max(mx, 2) * 1.1, xl: '時間（秒）' });
      inf.innerHTML = '風速 ' + P.v + ' km/h：總阻尼比 ≈ <b>' + f2(z * 100) + '%</b>。' +
        (z < 0 ? '<br><b>顫振</b>：風不只是推動橋面，而是隨著橋面的扭轉改變對它的力，每一個循環都「餵」它更多能量——阻尼變成<b>負的</b>。振幅指數增長，直到結構破壞。塔科馬海峽吊橋在 1940 年 11 月 7 日，就是在約 64 km/h 的風中這樣扭斷的。' :
          P.v > Vc * 0.8 ? '<br>接近臨界風速：風帶走的能量越來越少，振動衰減得越來越慢。' : '<br>結構本身與空氣的阻尼，讓振動逐漸衰減。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">（單一自由度的教學模型，臨界風速設為約 ' + Vc + ' km/h；真實的顫振分析需要風洞試驗。）</span>'; }
    u();
  }

  function initFatigue(root, cfg) {
    head(root, cfg.q); var P = { ds: 100, a0: 0.5, ins: 8000 }, view = el('div'), inf;
    var us = [slider(root, '每次循環的應力範圍 Δσ（MPa）', 40, 200, 1, P.ds, function (x) { return x + ' MPa'; }, null, function (x) { P.ds = x; draw(); }),
      slider(root, '初始裂紋長度（毫米）', 0.1, 3, 0.05, P.a0, function (x) { return f2(x) + ' mm'; }, null, function (x) { P.a0 = x; draw(); }),
      slider(root, '檢查間隔（循環數，例如飛行次數）', 1000, 30000, 500, P.ins, function (x) { return x.toLocaleString() + ' 次'; }, null, function (x) { P.ins = x; draw(); })];
    root.appendChild(view); inf = info(root);
    var C = 5e-11, m = 3, Y = 1.12, KIC = 30, smaxRatio = 1.0, adet = 2;
    function draw() { var smax = P.ds * smaxRatio, ac = Math.pow(KIC / (Y * smax), 2) / Math.PI * 1000, a = P.a0, N = 0, d = [[0, a]], dN = 50, det = null, ins = [];
      while (a < ac && N < 400000) { var dK = Y * P.ds * Math.sqrt(Math.PI * a / 1000); a += C * Math.pow(dK, m) * dN * 1000; N += dN; if (N % 500 === 0) d.push([N, Math.min(a, ac * 1.05)]); if (det === null && a >= adet && N % P.ins < dN) det = N; }
      for (var k = P.ins; k <= N; k += P.ins) ins.push({ x: k, c: GY, n: '' });
      var fail = a >= ac ? N : null, firstIns = Math.ceil(Math.max(1, (function () { var aa = P.a0, nn = 0; while (aa < adet && nn < 400000) { aa += C * Math.pow(Y * P.ds * Math.sqrt(Math.PI * aa / 1000), m) * dN * 1000; nn += dN; } return nn; })()) / P.ins) * P.ins;
      var caught = fail && firstIns < fail;
      view.innerHTML = chart(640, 240, [{ d: d, c: RD, n: '裂紋長度（毫米）', w: 2.2 }], { x0: 0, x1: Math.max(N, P.ins) * 1.05, y0: 0, y1: Math.max(ac * 1.1, 3), xl: '循環數', hl: [{ y: ac, c: RD, n: '臨界長度：斷裂' }, { y: adet, c: GN, n: '檢查能發現的長度' }], vl: ins.length <= 30 ? ins : [] });
      inf.innerHTML = '帕里斯定律：每次循環裂紋成長 da/dN = C(ΔK)^m，ΔK = YΔσ√(πa)。裂紋越長，長得越快。' +
        '<br>臨界長度約 <b>' + f1(ac) + ' mm</b>；從 ' + f2(P.a0) + ' mm 長到斷裂需約 <b>' + (fail ? fail.toLocaleString() : '> 400,000') + '</b> 次循環。' +
        (fail ? '<br>每 ' + P.ins.toLocaleString() + ' 次檢查一次（灰線）：' + (caught ? '<b>來得及</b>——在第 ' + firstIns.toLocaleString() + ' 次循環的檢查時，裂紋已超過 2 mm 可以被發現。' : '<b>來不及</b>——裂紋在下一次檢查之前就斷了。必須縮短檢查間隔。') : '') +
        '<br>這就是「<b>損傷容限</b>」設計：假設裂紋一定存在，確保它在變危險之前一定會被檢查到。<span style="font-size:0.9em;color:var(--text-muted)">（材料參數為鋁合金的示意值。）</span>'; }
    us.forEach(function (u) { u(); });
  }

  var FL = [[66, 0], [70, 1], [69, 0], [68, 0], [67, 0], [72, 0], [73, 0], [70, 0], [57, 1], [63, 1], [70, 1], [78, 0], [67, 0], [53, 2], [67, 0], [75, 0], [70, 0], [81, 0], [76, 0], [79, 0], [75, 2], [76, 0], [58, 1]];
  function initOring(root, cfg) {
    head(root, cfg.q); var P = { all: 0 }, view = el('div'), inf;
    var b = bar(root); [['只看有損傷的發射（1986 年那一晚的圖）', 0], ['看全部 23 次發射', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.all = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    root.appendChild(view); inf = info(root);
    var w0 = 0, w1 = 0; (function () { for (var it = 0; it < 50; it++) { var g0 = 0, g1 = 0, h00 = 0, h01 = 0, h11 = 0; FL.forEach(function (f) { var x = (f[0] - 32) / 1.8, y = f[1] > 0 ? 1 : 0, p = 1 / (1 + Math.exp(-(w0 + w1 * x))), wgt = p * (1 - p); g0 += y - p; g1 += (y - p) * x; h00 += wgt; h01 += wgt * x; h11 += wgt * x * x; });
      var det = h00 * h11 - h01 * h01; w0 += (h11 * g0 - h01 * g1) / det; w1 += (-h01 * g0 + h00 * g1) / det; } })();
    function draw() { var pts = FL.filter(function (f) { return P.all || f[1] > 0; }).map(function (f) { return { x: (f[0] - 32) / 1.8, y: f[1], c: f[1] ? RD : BL, n: '' }; }), cur = [];
      for (var c = -4; c <= 30; c += 0.2) cur.push([c, 2.6 / (1 + Math.exp(-(w0 + w1 * c)))]);
      var S = [{ d: [[-10, -1]], c: RD, n: '每次發射中有熱損傷的 O 型環數', w: 3 }]; if (P.all) S.push({ d: cur, c: PU, n: '邏輯迴歸：任何損傷的機率（× 2.6 顯示）', w: 1.6, dash: '5,4' });
      view.innerHTML = chart(640, 240, S, { x0: -4, x1: 30, y0: -0.2, y1: 3, xl: '發射時的溫度（°C）', pts: pts, vl: [{ x: -0.6, c: RD, n: '預測溫度 31°F（−0.6°C）' }] });
      var p31 = 1 / (1 + Math.exp(-(w0 + w1 * -0.6)));
      inf.innerHTML = P.all ? '加上<b>沒有損傷</b>的 16 次發射（藍點），趨勢一目了然：溫度高於約 22°C（72°F）的發射中，只有一次有損傷；低於約 18°C 的四次發射，<b>全部</b>都有損傷。挑戰者號發射前的預測溫度約 −0.6°C（31°F），發射時氣溫約 2°C，都比過去最冷的發射（約 12°C）冷了十度以上。用邏輯迴歸外推到 31°F，損傷的機率約 <b>' + Math.round(p31 * 100) + '%</b>。' :
        '1986 年 1 月 27 日晚上的電話會議中，討論的資料只有<b>發生過損傷</b>的 7 次發射。看起來，損傷在冷與熱的時候都發生——「溫度沒有明顯的關係」。' + '<br>按上面的另一個按鈕，加上沒有損傷的那些發射。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">資料：發射前 23 次飛行中，固態火箭助推器 O 型環出現熱損傷的數量（常用的教科書資料集）。</span>'; }
    draw();
  }

  function initSwiss(root, cfg) {
    head(root, cfg.q); var P = { n: 4, p: 0.1, c: 0 }, view = el('div'), inf;
    var us = [slider(root, '防護層數', 1, 6, 1, P.n, function (x) { return x + ' 層'; }, null, function (x) { P.n = x; draw(); }),
      slider(root, '每一層的漏洞機率', 0.01, 0.5, 0.01, P.p, function (x) { return Math.round(x * 100) + '%'; }, null, function (x) { P.p = x; draw(); }),
      slider(root, '共同原因（例如同一個管理文化讓所有防護一起變弱）', 0, 1, 0.01, P.c, function (x) { return Math.round(x * 100) + '%'; }, null, function (x) { P.c = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var W = 640, H = 170, g = '', sp = (W - 120) / Math.max(1, P.n); var seed = 5; function r() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
      for (var i = 0; i < P.n; i++) { var x = 70 + i * sp; g += '<rect x="' + n1(x) + '" y="20" width="22" height="130" rx="6" fill="#f2c94c" stroke="#c9a227"/>'; var holes = Math.max(1, Math.round(P.p * 12)); for (var k = 0; k < holes; k++) { var y = 30 + r() * 110; g += '<ellipse cx="' + n1(x + 11) + '" cy="' + n1(y) + '" rx="6" ry="' + n1(4 + 8 * P.p) + '" fill="var(--surface)"/>'; } }
      g += tx(30, 90, '危害', 11) + tx(W - 30, 90, '事故', 11, RD) + ln(45, 85, W - 50, 85, RD, 1.2, 'stroke-dasharray="4 4" marker-end="url(#ar)"');
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var pInd = Math.pow(P.p, P.n), pCom = P.p, pTot = (1 - P.c) * pInd + P.c * pCom;
      inf.innerHTML = '如果每一層<b>獨立</b>，危害要穿過全部 ' + P.n + ' 層的機率是 ' + Math.round(P.p * 100) + '%^' + P.n + ' ≈ <b>' + (pInd < 1e-4 ? pInd.toExponential(1) : f2(pInd * 100) + '%') + '</b>。多一層防護，風險就乘上一個小數字——這是「縱深防禦」的力量。' +
        '<br>但如果有 ' + Math.round(P.c * 100) + '% 的情況是<b>共同原因</b>讓所有的層一起失效（例如同一場海嘯淹沒了所有的備用發電機、同一個趕進度的文化讓所有的檢查都放水），整體的機率變成約 <b>' + (pTot < 1e-4 ? pTot.toExponential(1) : f2(pTot * 100) + '%') + '</b>。' +
        (P.c > 0.05 ? '<br>共同原因讓多層防護的效果大打折扣——這是許多重大事故真正的原因。' : ''); }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.eda-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ flutter: initFlutter, fatigue: initFatigue, oring: initOring, swiss: initSwiss })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"⚠️", EDA_NOTE, EDALIB, "eda-w")

FLUTTER = edw({"t": "flutter", "q": u"顫振：風怎麼把一座橋扭斷"})
FATIGUE = edw({"t": "fatigue", "q": u"金屬疲勞：裂紋會長大，檢查來得及嗎"})
ORING = edw({"t": "oring", "q": u"挑戰者號的 O 型環：溫度與損傷"})
SWISS = edw({"t": "swiss", "q": u"瑞士乳酪模型：為什麼多層防護還是會失效"})
