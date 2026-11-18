# -*- coding: utf-8 -*-
"""〈引擎原理：從蒸汽機到噴射引擎〉（eng_）共用：課程包裝與 ENGLIB 互動元件（class="eng-w"）。

  pv      P-V 圖：奧圖循環與狄塞爾循環的熱效率
  stroke  四行程引擎：曲軸角度與活塞、氣門
  bypass  渦輪扇的旁通比與推進效率
  rocket  火箭方程式：比衝與質量比
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

ENG_NOTE = u"互動模擬為理想化的教學模型，真實引擎的效率會因摩擦、散熱與不完全燃燒而較低。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def ew(cfg, maxw=680):
    return wdg("eng-w", cfg, maxw)


ENGLIB = r"""
(function () {
  if (window.__engLib) return; window.__engLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }

  function initPV(root, cfg) {
    head(root, cfg.q); var P = { m: 0, r: 10, rc: 2 }, view = el('div'), inf, us2;
    var b = bar(root); [['奧圖循環（汽油引擎）', 0], ['狄塞爾循環（柴油引擎）', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.m = o[1]; mark(b, o[1]); if (P.m && P.r < 14) { P.r = 18; } draw(); }; b.appendChild(x); }); mark(b, 0);
    var us = [slider(root, '壓縮比 r', 4, 22, 0.5, P.r, function (x) { return f1(x) + ' : 1'; }, null, function (x) { P.r = x; draw(); }),
      slider(root, '狄塞爾的切斷比（燃油噴射持續的程度）', 1.2, 3.5, 0.1, P.rc, function (x) { return f1(x); }, null, function (x) { P.rc = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var g = 1.4, r = P.r, V1 = 1, V2 = 1 / r, P1 = 1, d = [], eta, T3;
      function adia(Va, Pa, Vb) { var pts = []; for (var k = 0; k <= 40; k++) { var v = Va + (Vb - Va) * k / 40; pts.push([v, Pa * Math.pow(Va / v, g)]); } return pts; }
      var c1 = adia(V1, P1, V2), P2 = c1[c1.length - 1][1], P3, V3 = V2, c2;
      if (!P.m) { P3 = P2 * 2.8; d = c1.concat([[V2, P3]]).concat(adia(V2, P3, V1)).concat([[V1, P1]]); eta = 1 - Math.pow(r, 1 - g); }
      else { V3 = V2 * P.rc; P3 = P2; d = c1.concat([[V3, P3]]).concat(adia(V3, P3, V1)).concat([[V1, P1]]); eta = 1 - Math.pow(r, 1 - g) * (Math.pow(P.rc, g) - 1) / (g * (P.rc - 1)); }
      var mx = 0; d.forEach(function (p) { mx = Math.max(mx, p[1]); });
      view.innerHTML = chart(640, 250, [{ d: d, c: RD, n: P.m ? '狄塞爾循環' : '奧圖循環', w: 2.4 }], { x0: 0, x1: 1.05, y0: 0, y1: mx * 1.08, xl: '汽缸容積（相對值）', yl: '壓力（相對值）' });
      inf.innerHTML = '理想熱效率 ≈ <b>' + Math.round(eta * 100) + '%</b>（γ = 1.4 的空氣標準循環）。曲線圍起來的面積，就是每個循環做的<b>功</b>。' +
        (P.m ? '<br>柴油引擎只壓縮空氣，壓縮比可以高達 15～22，燃油在壓縮後噴入、自行點燃，燃燒時大致維持定壓（水平的線）。切斷比越大（噴油越久），效率越低，但每次做的功越多。' : '<br>汽油引擎在壓縮到最小容積時點火，燃燒非常快，近似「定容加熱」（垂直的線）。壓縮比越高效率越高，但太高會<b>爆震</b>，一般汽油引擎約 10～14。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">真實引擎的熱效率約為理想值的六到七成：汽油引擎約 30～40%，柴油引擎約 40～45%。</span>'; }
    us.forEach(function (u) { u(); });
  }

  var PH = [['進氣', '活塞下行，進氣門打開，吸入空氣與燃油的混合氣', BL], ['壓縮', '兩個氣門都關閉，活塞上行，把混合氣壓縮', PU], ['動力', '火星塞點火，燃燒的氣體膨脹，把活塞往下推——唯一做功的行程', RD], ['排氣', '排氣門打開，活塞上行，把廢氣推出去', GY]];
  function initStroke(root, cfg) {
    head(root, cfg.q); var P = { a: 30, run: 0 }, view = el('div'), inf, timer = null, u;
    var b = bar(root), pb = btn('▶ 播放'); pb.onclick = function () { P.run ^= 1; pb.textContent = P.run ? '⏸ 暫停' : '▶ 播放'; if (P.run) timer = setInterval(function () { P.a = (P.a + 6) % 720; sl.value = P.a; draw(); }, 50); else clearInterval(timer); }; b.appendChild(pb);
    u = slider(root, '曲軸角度', 0, 719, 1, P.a, function (x) { return x + '°'; }, null, function (x) { P.a = x; draw(); }); var sl = root.querySelectorAll('input[type=range]'); sl = sl[sl.length - 1];
    root.appendChild(view); inf = info(root);
    function draw() { var a = P.a * Math.PI / 180, R = 40, Lr = 110, cx = 230, cy = 270, ph = Math.floor(P.a / 180), g = '';
      var crankX = cx + R * Math.sin(a), crankY = cy - R * Math.cos(a), pistonY = crankY - Math.sqrt(Lr * Lr - Math.pow(crankX - cx, 2));
      g += '<rect x="' + (cx - 46) + '" y="40" width="92" height="210" fill="none" stroke="#666" stroke-width="3"/>';
      var gas = ph == 2 ? '#f6b26b' : ph == 1 ? '#c9b8ea' : ph == 0 ? '#bcd6f0' : '#ccc';
      g += '<rect x="' + (cx - 44) + '" y="42" width="88" height="' + n1(pistonY - 20 - 42) + '" fill="' + gas + '" opacity="0.8"/>';
      g += '<rect x="' + (cx - 44) + '" y="' + n1(pistonY - 20) + '" width="88" height="34" fill="#888" stroke="#555"/>';
      g += ln(cx, pistonY, crankX, crankY, '#555', 6) + '<circle cx="' + cx + '" cy="' + cy + '" r="' + (R + 8) + '" fill="none" stroke="#bbb" stroke-dasharray="3 3"/>' + ln(cx, cy, crankX, crankY, '#333', 8) + '<circle cx="' + n1(crankX) + '" cy="' + n1(crankY) + '" r="6" fill="#333"/>';
      var inOpen = ph == 0, exOpen = ph == 3;
      g += ln(cx - 28, 40, cx - 28, inOpen ? 58 : 44, BL, 5) + ln(cx + 28, 40, cx + 28, exOpen ? 58 : 44, GY, 5) + tx(cx - 28, 32, '進氣門', 10, BL) + tx(cx + 28, 32, '排氣門', 10, GY);
      if (ph == 2 && P.a % 180 < 25) g += '<circle cx="' + cx + '" cy="48" r="10" fill="#ffd34d"/>' + tx(cx, 52, '⚡', 12);
      PH.forEach(function (p, i) { var on = i == ph; g += '<rect x="380" y="' + (50 + i * 50) + '" width="220" height="40" rx="8" fill="' + (on ? p[2] : '#eee') + '" opacity="' + (on ? 0.85 : 1) + '"/>' + tx(490, 75 + i * 50, (i + 1) + '. ' + p[0] + '（' + i * 180 + '°～' + (i + 1) * 180 + '°）', 12, on ? '#fff' : '#666'); });
      view.innerHTML = svgw('0 0 640 330', g);
      inf.innerHTML = '<b>' + PH[ph][0] + '行程</b>：' + PH[ph][1] + '。<br>四個行程需要曲軸轉<b>兩圈</b>（720°），只有一個行程產生動力，所以靠飛輪的慣性帶過其他三個行程；多汽缸引擎讓各缸錯開點火，輸出更平順。'; }
    u();
  }

  function initBypass(root, cfg) {
    head(root, cfg.q); var P = { b: 9 }, view = el('div'), inf;
    var us = [slider(root, '旁通比（外涵道空氣 ÷ 核心空氣）', 0, 15, 0.5, P.b, function (x) { return f1(x) + ' : 1'; }, null, function (x) { P.b = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function eff(B) { var V0 = 240, F = 1, mc = 1 / 600, m = mc * (1 + B), dV = F / m, Vj = V0 + dV; return { vj: Vj, ep: 2 * V0 / (V0 + Vj) }; }
    function draw() { var d = []; for (var B = 0; B <= 15; B += 0.25) d.push([B, eff(B).ep * 100]); var e = eff(P.b), e0 = eff(0);
      view.innerHTML = chart(640, 230, [{ d: d, c: BL, n: '推進效率（%）', w: 2.4 }], { x0: 0, x1: 15, y0: 0, y1: 100, xl: '旁通比', pts: [{ x: P.b, y: e.ep * 100, c: RD, n: Math.round(e.ep * 100) + '%' }], vl: [{ x: 0, c: GY, n: '渦輪噴射' }] });
      inf.innerHTML = '在巡航速度（約 240 m/s）下產生相同的推力：旁通比 ' + f1(P.b) + ' 時，噴出的氣流速度約 <b>' + Math.round(e.vj) + ' m/s</b>，推進效率約 <b>' + Math.round(e.ep * 100) + '%</b>；純渦輪噴射（旁通比 0）的噴流約 ' + Math.round(e0.vj) + ' m/s，效率只有 ' + Math.round(e0.ep * 100) + '%。' +
        '<br>關鍵在於：<b>推動大量的空氣、加一點點速度</b>，比推動少量的空氣、加很多速度更省能量（動能與速度平方成正比）。所以現代客機的引擎越來越「胖」——風扇的直徑越來越大，噪音也大幅降低。<br><span style="font-size:0.9em;color:var(--text-muted)">簡化模型：固定核心氣流與推力，只計推進效率；大風扇也會帶來重量與阻力。</span>'; }
    us.forEach(function (u) { u(); });
  }

  var EN = [['固體火箭', 260], ['煤油＋液氧', 330], ['甲烷＋液氧', 360], ['液氫＋液氧', 450], ['離子推進器', 3000]];
  function initRocket(root, cfg) {
    head(root, cfg.q); var P = { e: 3, mr: 8 }, view = el('div'), inf;
    var b = bar(root); EN.forEach(function (o, i) { var x = btn(o[0], i); x.onclick = function () { P.e = i; mark(b, i); draw(); }; b.appendChild(x); }); mark(b, 3);
    var us = [slider(root, '質量比（點火時 ÷ 燃料用完時）', 1.5, 25, 0.5, P.mr, function (x) { return f1(x); }, null, function (x) { P.mr = x; draw(); })];
    root.appendChild(view); inf = info(root);
    var TG = [['低地球軌道', 9.4, BL], ['＋前往月球', 12.5, PU], ['＋前往火星', 13.0, RD]];
    function draw() { var isp = EN[P.e][1], dv = isp * 9.81 * Math.log(P.mr) / 1000, g = '', W = 560, sc = W / 16;
      g += '<rect x="40" y="30" width="' + n1(Math.min(dv, 16) * sc) + '" height="34" fill="' + OR + '"/>' + tx(46 + Math.min(dv, 16) * sc, 52, 'Δv ≈ ' + f1(dv) + ' km/s', 12, 'currentColor', 'start');
      TG.forEach(function (t, i) { var x = 40 + t[1] * sc; g += ln(x, 20, x, 130 - i * 0, t[2], 2, 'stroke-dasharray="5 4"') + tx(x, 92 + i * 16, t[0] + ' ' + t[1], 10, t[2], 'middle'); });
      g += ln(40, 75, 40 + W, 75, '#999'); for (var k = 0; k <= 16; k += 2) g += tx(40 + k * sc, 145, k, 9, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 640 155', g);
      inf.innerHTML = '齊奧爾科夫斯基火箭方程式：Δv = I<sub>sp</sub> · g₀ · ln(質量比)。' + EN[P.e][0] + '的比衝約 <b>' + isp + ' 秒</b>，質量比 ' + f1(P.mr) + ' 時，速度變化約 <b>' + f1(dv) + ' km/s</b>。' +
        '<br>對數讓火箭非常「吃虧」：要多一倍的 Δv，質量比要<b>平方</b>。所以真實的火箭要分成好幾<b>節</b>，把用完的燃料槽丟掉。離子推進器的比衝極高，但推力非常小，只能在太空中慢慢加速。<br><span style="font-size:0.9em;color:var(--text-muted)">目標 Δv 為含重力與空氣阻力損失的約略值。</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.eng-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ pv: initPV, stroke: initStroke, bypass: initBypass, rocket: initRocket })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🔥", ENG_NOTE, ENGLIB, "eng-w")

PV = ew({"t": "pv", "q": u"P-V 圖：壓縮比與熱效率"})
STROKE = ew({"t": "stroke", "q": u"四行程引擎：拖動曲軸，或按播放"})
BYPASS = ew({"t": "bypass", "q": u"渦輪扇引擎：為什麼風扇越來越大"})
ROCKET = ew({"t": "rocket", "q": u"火箭方程式：要多少燃料才能上太空"})
