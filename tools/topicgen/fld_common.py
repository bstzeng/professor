# -*- coding: utf-8 -*-
"""〈流體力學與飛行〉（fld_）共用：課程包裝與 FLDLIB 互動元件（class="fld-w"）。

  venturi  文氏管：連續方程式與白努利定律
  reyn     雷諾數：層流與亂流
  wing     翼型：攻角、升力係數與失速
  mach     馬赫數：聲波波前與馬赫錐
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

FLD_NOTE = u"互動模擬為教學用的簡化模型，數值為示意。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def fw(cfg, maxw=680):
    return wdg("fld-w", cfg, maxw)


FLDLIB = r"""
(function () {
  if (window.__fldLib) return; window.__fldLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }

  function initVenturi(root, cfg) {
    head(root, cfg.q); var P = { v: 1, r: 0.6 }, view = el('div'), inf;
    var us = [slider(root, '入口流速', 0.5, 5, 0.1, P.v, function (x) { return f1(x) + ' m/s'; }, null, function (x) { P.v = x; draw(); }),
      slider(root, '窄處直徑 ÷ 入口直徑', 0.3, 1, 0.05, P.r, function (x) { return f2(x); }, null, function (x) { P.r = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var rho = 1000, v1 = P.v, v2 = v1 / (P.r * P.r), dp = 0.5 * rho * (v2 * v2 - v1 * v1), h = dp / (rho * 9.81), H0 = 2.0;
      var g = '', cy = 200, R1 = 50, R2 = 50 * P.r;
      function rad(x) { if (x < 160) return R1; if (x < 280) return R1 + (R2 - R1) * (x - 160) / 120; if (x < 360) return R2; if (x < 480) return R2 + (R1 - R2) * (x - 360) / 120; return R1; }
      var top = '', bot = ''; for (var x = 20; x <= 620; x += 10) { top += (x == 20 ? 'M' : 'L') + x + ' ' + n1(cy - rad(x)); bot += (x == 20 ? 'M' : 'L') + x + ' ' + n1(cy + rad(x)); }
      var fill = top + ' L620 ' + n1(cy + R1); for (var x2 = 620; x2 >= 20; x2 -= 10) fill += ' L' + x2 + ' ' + n1(cy + rad(x2)); g += '<path d="' + fill + 'Z" fill="#cfe3f5"/>' + '<path d="' + top + '" fill="none" stroke="#557" stroke-width="2"/><path d="' + bot + '" fill="none" stroke="#557" stroke-width="2"/>';
      for (var k = 0; k < 5; k++) { var fr = (k - 2) / 2.4, d = ''; for (var x3 = 20; x3 <= 620; x3 += 10) d += (x3 == 20 ? 'M' : 'L') + x3 + ' ' + n1(cy + fr * rad(x3)); g += '<path d="' + d + '" fill="none" stroke="' + BL + '" stroke-width="1" opacity="0.6"/>'; }
      var sc = 60; [[90, H0], [320, H0 - h], [550, H0]].forEach(function (m, i) { var hh = Math.max(m[1], 0) * sc, x = m[0], yb = cy - rad(x);
        g += '<rect x="' + (x - 6) + '" y="' + n1(yb - 150) + '" width="12" height="150" fill="none" stroke="#888"/>' + '<rect x="' + (x - 5) + '" y="' + n1(yb - Math.min(hh, 150)) + '" width="10" height="' + n1(Math.min(hh, 150)) + '" fill="' + BL + '" opacity="0.7"/>'; });
      g += tx(90, cy + 70, '入口 v = ' + f1(v1) + ' m/s', 11) + tx(320, cy + 70, '窄處 v = ' + f1(v2) + ' m/s', 11, RD) + tx(550, cy + 70, '出口', 11);
      view.innerHTML = svgw('0 0 640 290', g);
      inf.innerHTML = '連續方程式：A₁v₁ = A₂v₂。截面積變成 ' + f2(P.r * P.r) + ' 倍，流速就變成 <b>' + f1(1 / (P.r * P.r)) + ' 倍</b>。' +
        '<br>白努利定律：P + ½ρv² = 常數。窄處流速變快，壓力就<b>降低</b> ½ρ(v₂² − v₁²) ≈ <b>' + (dp >= 1000 ? f1(dp / 1000) + ' kPa' : Math.round(dp) + ' Pa') + '</b>，相當於水柱少了 ' + f2(h) + ' 公尺——中間那根管子的水位比較低。' +
        (H0 - h < 0 ? '<br>中間的壓力已經<b>低於大氣壓</b>，壓力計的水柱被吸了下去。' + (H0 - h < -8 ? '壓力接近真空時，水會在常溫下沸騰起泡（<b>空化</b>）——這正是船的螺旋槳會被侵蝕的原因。' : '') : '') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">假設不可壓縮、無黏滯的水，管子水平放置；壓力計的起始水柱設為 2 公尺。</span>'; }
    us.forEach(function (u) { u(); });
  }

  var FL = [['水（20 °C）', 1000, 1.0e-3], ['空氣', 1.2, 1.8e-5], ['蜂蜜', 1400, 10], ['血液', 1060, 3.5e-3]];
  function initReyn(root, cfg) {
    head(root, cfg.q); var P = { f: 0, v: 0.05, d: 2 }, view = el('div'), inf;
    var b = bar(root); FL.forEach(function (o, i) { var x = btn(o[0], i); x.onclick = function () { P.f = i; mark(b, i); draw(); }; b.appendChild(x); }); mark(b, 0);
    var us = [slider(root, '流速（log）', -3, 1, 0.05, Math.log10(P.v), function (x) { var v = Math.pow(10, x); return (v < 0.1 ? f2(v * 100) + ' cm/s' : f2(v) + ' m/s'); }, null, function (x) { P.v = Math.pow(10, x); draw(); }),
      slider(root, '管徑', 0.2, 10, 0.1, P.d, function (x) { return f1(x) + ' cm'; }, null, function (x) { P.d = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var F = FL[P.f], Re = F[1] * P.v * P.d / 100 / F[2], t = Math.min(Math.max((Re - 2300) / 1700, 0), 1), g = '', cy = 110;
      g += '<rect x="20" y="30" width="600" height="160" fill="#eef4fa" stroke="#557"/>';
      var seed = 7; function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280 - 0.5; }
      for (var k = 0; k < 9; k++) { var y0 = 45 + k * 16.5, d = 'M20 ' + y0, yy = y0;
        for (var x = 30; x <= 620; x += 10) { yy = y0 + t * (rnd() * 26 + 10 * Math.sin(x / 23 + k)); d += ' L' + x + ' ' + n1(Math.max(32, Math.min(188, yy))); }
        g += '<path d="' + d + '" fill="none" stroke="' + (t > 0.5 ? RD : BL) + '" stroke-width="1.4"/>'; }
      var lam = Re < 2300, reg = lam ? '層流' : Re < 4000 ? '過渡區' : '亂流';
      g += tx(320, 215, '雷諾數 Re ≈ ' + (Re >= 1e4 ? Math.round(Re).toLocaleString() : Re < 1 ? f2(Re) : Math.round(Re)) + '　→　' + reg, 13, lam ? BL : RD);
      view.innerHTML = svgw('0 0 640 230', g);
      inf.innerHTML = 'Re = ρvD/μ：慣性力（讓流體繼續衝）與黏滯力（讓流體規矩）的比值。圓管中，Re 小於約 2,300 通常是<b>層流</b>（平行的流線），大於約 4,000 通常變成<b>亂流</b>（漩渦與混合）。' +
        '<br>試試看：蜂蜜幾乎永遠是層流；空氣與水只要速度稍快、尺寸稍大，就變成亂流——所以飛機、船與河流的周圍幾乎都是亂流。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">流線為示意圖；轉換點會受管壁粗糙度與入口擾動影響。</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initWing(root, cfg) {
    head(root, cfg.q); var P = { a: 5, v: 70 }, view = el('div'), cv = el('div'), inf;
    var us = [slider(root, '攻角', -5, 25, 0.5, P.a, function (x) { return f1(x) + '°'; }, null, function (x) { P.a = x; draw(); }),
      slider(root, '空速', 30, 250, 5, P.v, function (x) { return x + ' m/s（' + Math.round(x * 3.6) + ' km/h）'; }, null, function (x) { P.v = x; draw(); })];
    root.appendChild(view); root.appendChild(cv); inf = info(root);
    function CL(a) { var c = 0.11 * (a + 2); if (a > 15) c = 0.11 * 17 - 0.06 * (a - 15) * (a - 15) / 3 - 0.05 * (a - 15); return Math.max(c, -0.5); }
    function draw() { var a = P.a, c = CL(a), stall = a > 15, rho = 1.2, S = 125, L = 0.5 * rho * P.v * P.v * S * c;
      var g = '', cx = 300, cy = 110, ar = a * Math.PI / 180, pts = [];
      for (var i = 0; i <= 40; i++) { var t = i / 40, x = t, yt = 0.6 * (0.2969 * Math.sqrt(t) - 0.126 * t - 0.3516 * t * t + 0.2843 * t * t * t - 0.1015 * Math.pow(t, 4)), yc = 0.04 * (t < 0.4 ? (2 * 0.4 * t - t * t) / 0.16 : ((1 - 0.8) + 2 * 0.4 * t - t * t) / 0.36);
        pts.push([x, yc + yt]); } for (var j = 40; j >= 0; j--) { var t2 = j / 40, yt2 = 0.6 * (0.2969 * Math.sqrt(t2) - 0.126 * t2 - 0.3516 * t2 * t2 + 0.2843 * t2 * t2 * t2 - 0.1015 * Math.pow(t2, 4)), yc2 = 0.04 * (t2 < 0.4 ? (2 * 0.4 * t2 - t2 * t2) / 0.16 : ((1 - 0.8) + 2 * 0.4 * t2 - t2 * t2) / 0.36); pts.push([t2, yc2 - yt2]); }
      var d = ''; pts.forEach(function (p, i) { var x = (p[0] - 0.3) * 260, y = -p[1] * 260, X = cx + x * Math.cos(ar) - y * Math.sin(ar), Y = cy + x * Math.sin(ar) + y * Math.cos(ar); d += (i ? 'L' : 'M') + n1(X) + ' ' + n1(Y); });
      for (var k = 0; k < 7; k++) { var y0 = 30 + k * 26, s = 'M20 ' + y0, dev = (y0 < cy ? -1 : 1) * 18 * Math.exp(-Math.abs(y0 - cy) / 40);
        for (var x2 = 30; x2 <= 620; x2 += 10) { var bump = Math.exp(-Math.pow((x2 - cx) / 90, 2)) * dev, dw = x2 > cx - 60 ? Math.sin(a * Math.PI / 180) * (x2 - cx + 60) * 0.3 * (stall ? 0.35 : 1) * Math.exp(-Math.abs(y0 - cy) / 90) : 0, wig = stall && y0 < cy + 10 && x2 > cx - 20 ? 9 * Math.sin(x2 / 9 + k) : 0;
          s += ' L' + x2 + ' ' + n1(y0 + bump + dw + wig); }
        g += '<path d="' + s + '" fill="none" stroke="' + BL + '" stroke-width="1" opacity="0.55"/>'; }
      g += '<path d="' + d + 'Z" fill="#888" stroke="#444"/>';
      var Lh = Math.max(-40, Math.min(90, c * 50)); g += ln(cx, cy, cx, cy - Lh, stall ? OR : GN, 4) + '<path d="M' + (cx - 7) + ' ' + n1(cy - Lh + (Lh > 0 ? 8 : -8)) + ' L' + cx + ' ' + n1(cy - Lh) + ' L' + (cx + 7) + ' ' + n1(cy - Lh + (Lh > 0 ? 8 : -8)) + '" fill="' + (stall ? OR : GN) + '"/>' + tx(cx + 12, cy - Lh, '升力', 11, stall ? OR : GN, 'start');
      if (stall) g += tx(470, 40, '失速！氣流從上表面分離', 13, RD);
      view.innerHTML = svgw('0 0 640 210', g);
      var cd = []; for (var x3 = -5; x3 <= 25; x3 += 0.5) cd.push([x3, CL(x3)]);
      cv.innerHTML = chart(640, 170, [{ d: cd, c: PU, n: '升力係數 CL', w: 2.2 }], { x0: -5, x1: 25, y0: -0.6, y1: 2.1, xl: '攻角（度）', vl: [{ x: 15, c: RD, n: '失速攻角' }], pts: [{ x: a, y: c, c: RD }] });
      inf.innerHTML = '升力 L = ½ρv²S·C<sub>L</sub>。以機翼面積 ' + S + ' m²（約一架窄體客機）計算：升力約 <b>' + Math.round(L / 9810) + ' 公噸力</b>。' +
        '<br>攻角增加，升力係數幾乎<b>線性</b>增加；超過約 15° 後，氣流無法沿著上表面流動而<b>分離</b>，升力驟降——這就是失速。速度加倍，升力變成四倍。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">升力係數曲線為典型有彎度翼型的示意，流線只是定性的示意圖。</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initMach(root, cfg) {
    head(root, cfg.q); var P = { m: 1.5 }, view = el('div'), inf;
    var us = [slider(root, '馬赫數', 0.3, 3, 0.05, P.m, function (x) { return 'M ' + f2(x); }, null, function (x) { P.m = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var M = P.m, g = '', sx = 470, sy = 140, c = 26, n = 8;
      for (var k = 1; k <= n; k++) { var r = c * k, x = sx - M * c * k; g += '<circle cx="' + n1(x) + '" cy="' + sy + '" r="' + n1(r) + '" fill="none" stroke="' + BL + '" stroke-width="1.2" opacity="' + n1(1 - k / (n + 2)) + '"/>' + '<circle cx="' + n1(x) + '" cy="' + sy + '" r="2" fill="#888"/>'; }
      if (M > 1) { var mu = Math.asin(1 / M), L = 600; g += ln(sx, sy, sx - L * Math.cos(mu), sy - L * Math.sin(mu), RD, 2) + ln(sx, sy, sx - L * Math.cos(mu), sy + L * Math.sin(mu), RD, 2); }
      g += '<path d="M' + (sx + 14) + ' ' + sy + ' L' + (sx - 10) + ' ' + (sy - 7) + ' L' + (sx - 10) + ' ' + (sy + 7) + 'Z" fill="#333"/>';
      view.innerHTML = svgw('0 0 640 280', '<clipPath id="mclip"><rect x="0" y="0" width="640" height="280"/></clipPath><g clip-path="url(#mclip)">' + g + '</g>');
      var mu2 = M > 1 ? Math.asin(1 / M) * 180 / Math.PI : 0;
      inf.innerHTML = '飛機每隔一段時間發出的聲波，以音速（海平面約 340 m/s）向外擴散。' + (M < 1 ? '飛機比聲音<b>慢</b>：前方的波前被擠在一起，但聲音仍跑在飛機前面。' : M < 1.05 ? '<b>接近音速</b>：所有波前在機頭疊在一起，形成強大的壓力牆——「音障」。' :
        '飛機比聲音<b>快</b>：波前疊成一個圓錐，叫做<b>馬赫錐</b>，半頂角 μ = arcsin(1/M) ≈ <b>' + f1(mu2) + '°</b>。圓錐掃過地面時，人們聽到「轟」的一聲——<b>音爆</b>。') +
        '<br>灰點是發出各個波前時飛機所在的位置。<span style="font-size:0.9em;color:var(--text-muted)">（平面示意圖）</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.fld-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ venturi: initVenturi, reyn: initReyn, wing: initWing, mach: initMach })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🌊", FLD_NOTE, FLDLIB, "fld-w")

VENTURI = fw({"t": "venturi", "q": u"文氏管：管子變窄時，流速與壓力怎麼變"})
REYN = fw({"t": "reyn", "q": u"雷諾數：同樣的管子，什麼時候是層流、什麼時候是亂流"})
WING = fw({"t": "wing", "q": u"機翼的升力：改變攻角與空速"})
MACH = fw({"t": "mach", "q": u"聲波與馬赫錐：飛得比聲音快時會發生什麼"})
