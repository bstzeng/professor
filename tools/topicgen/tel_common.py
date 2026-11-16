# -*- coding: utf-8 -*-
"""〈從哈伯到韋伯〉（tel_）共用：課程包裝與 TELLIB 互動元件（class="tel-w"）。

  airy     解析度：口徑、波長、雙星角距、大氣擾動 → 兩顆星的亮度剖面與能否分辨
  redshift 紅移：紅移 z → 星系光譜中的譜線移到哪裡，哈伯與韋伯各能看到哪一段
  hlaw     哈伯定律：H0 → 距離—速度圖、宇宙年齡，與兩種方法的哈伯張力
  mirror   拼接鏡面：對準的進度 → 18 片鏡子的星像從分散、疊合到共相
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

TEL_NOTE = (u"本課的推導以主要步驟為主；互動模擬為教學用的簡化版本，數字為約略值。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def tlw(cfg, maxw=680):
    return wdg("tel-w", cfg, maxw)


TELLIB = r"""
(function () {
  if (window.__telLib) return; window.__telLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function J1(x) { var s = 0, N = 60; for (var k = 0; k < N; k++) { var t = (k + 0.5) * Math.PI / N; s += Math.cos(t - x * Math.sin(t)); } return s / N; }
  function airyI(x) { if (Math.abs(x) < 1e-6) return 1; var j = 2 * J1(x) / x; return j * j; }

  function initAiry(root, cfg) {
    head(root, cfg.q); var P = { D: 2.4, lam: 0.5, sep: 0.08, see: 0 }, view = el('div'), inf;
    var b = bar(root), us; [['哈伯（2.4 m，可見光）', [2.4, 0.5]], ['韋伯（6.5 m，2 微米）', [6.5, 2]], ['人眼（7 mm）', [0.007, 0.55]], ['極大望遠鏡（39 m）', [39, 1]]].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { P.D = o[1][0]; P.lam = o[1][1]; us[0](); us[1](); }; b.appendChild(x); });
    var b2 = bar(root); [['在太空（無大氣）', 0], ['地面（大氣模糊約 0.8 角秒）', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.see = o[1]; mark(b2, o[1]); draw(); }; b2.appendChild(x); }); mark(b2, 0);
    us = [slider(root, '口徑 D（公尺，對數刻度）', -2.3, 1.6, 0.01, Math.log10(P.D), function (x) { var d = Math.pow(10, x); return d < 0.1 ? f1(d * 1000) + ' mm' : f2(d) + ' m'; }, null, function (x) { P.D = Math.pow(10, x); draw(); }),
      slider(root, '波長（微米）', 0.3, 25, 0.01, P.lam, function (x) { return f2(x) + ' μm'; }, null, function (x) { P.lam = x; draw(); }),
      slider(root, '兩顆星的角距離（角秒）', 0.01, 3, 0.005, P.sep, function (x) { return x < 0.1 ? f2(x * 1000) / 1000 + '″' : f2(x) + '″'; }, null, function (x) { P.sep = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var rad = 4.8481e-6, theta = 1.22 * P.lam * 1e-6 / P.D / rad, see = 0.8, span = Math.max(4 * theta, 2.5 * P.sep, P.see ? 3 : 0, 0.2), d = [], s1 = [], s2 = [], mx = 0;
      var sig = see / 2.355;
      for (var i = 0; i <= 400; i++) { var a = -span + 2 * span * i / 400, f1v, f2v;
        if (P.see) { f1v = Math.exp(-Math.pow(a + P.sep / 2, 2) / (2 * sig * sig)); f2v = Math.exp(-Math.pow(a - P.sep / 2, 2) / (2 * sig * sig)); }
        else { f1v = airyI(Math.PI * P.D * (a + P.sep / 2) * rad / (P.lam * 1e-6)); f2v = airyI(Math.PI * P.D * (a - P.sep / 2) * rad / (P.lam * 1e-6)); }
        s1.push([a, f1v]); s2.push([a, f2v]); d.push([a, f1v + f2v]); mx = Math.max(mx, f1v + f2v); }
      var mid = d[200][1], dip = mid / mx, res = P.see ? P.sep > see : P.sep >= theta;
      view.innerHTML = chart(640, 230, [{ d: s1, c: GY, n: '星 A', w: 1, dash: '4,3' }, { d: s2, c: GY, n: '星 B', w: 1, dash: '4,3' }, { d: d, c: BL, n: '看到的總亮度', w: 2.2 }], { x0: -span, x1: span, y0: 0, y1: mx * 1.1, xl: '天空中的位置（角秒）' });
      inf.innerHTML = '繞射極限 θ = 1.22 λ/D ≈ <b>' + (theta < 0.01 ? (theta * 1000).toFixed(2) + ' 毫角秒' : f2(theta) + ' 角秒') + '</b>。' + (P.see ? '但在地面，大氣擾動把星像模糊到約 <b>0.8 角秒</b>，再大的望遠鏡也一樣（除非用自適應光學）。' : '') +
        '<br>兩顆星相距 ' + f2(P.sep) + ' 角秒：' + (res ? '<b>分得開</b>' + (dip < 0.9 ? '，中間有明顯的凹陷。' : '（剛好在瑞利判據附近）。') : '<b>分不開</b>，看起來像一顆星。') +
        '<br>口徑越大、波長越短，解析度越好。韋伯在 2 微米的解析度和哈伯在可見光差不多——口徑大了 2.7 倍，正好抵消了波長長了 4 倍。'; }
    us.forEach(function (u) { u(); });
  }

  var LINES = [['Lyα', 0.1216], ['[O II]', 0.3727], ['Hβ', 0.4861], ['[O III]', 0.5007], ['Hα', 0.6563], ['PAH 3.3', 3.3], ['PAH 7.7', 7.7]];
  function initRedshift(root, cfg) {
    head(root, cfg.q); var P = { z: 2 }, view = el('div'), inf;
    var b = bar(root), u; [['附近星系', 0.02], ['宇宙中年（z=2）', 2], ['哈伯深空的極限（z≈8）', 8], ['韋伯的紀錄（z≈14）', 14.3]].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { P.z = o[1]; u(); }; b.appendChild(x); });
    u = slider(root, '紅移 z', 0, 15, 0.01, P.z, f2, null, function (x) { P.z = x; draw(); });
    root.appendChild(view); inf = info(root);
    function age(z) { var H0 = 67.7, Om = 0.31, OL = 0.69, s = 0, N = 2000, amax = 1 / (1 + z); for (var i = 0; i < N; i++) { var a = (i + 0.5) / N * amax; s += 1 / (a * Math.sqrt(Om / (a * a * a) + OL)) * amax / N; } return s * 977.8 / H0; }
    function draw() { var W = 640, H = 210, lo = Math.log10(0.08), hi = Math.log10(30), sx = function (l) { return 30 + (Math.log10(l) - lo) / (hi - lo) * (W - 50); }, g = '';
      g += '<rect x="' + n1(sx(0.38)) + '" y="20" width="' + n1(sx(0.75) - sx(0.38)) + '" height="14" fill="url(#rb)"/>' + tx((sx(0.38) + sx(0.75)) / 2, 30, '可見光', 9, '#fff');
      g += '<defs><linearGradient id="rb"><stop offset="0" stop-color="#7a3cff"/><stop offset="0.5" stop-color="#3cc060"/><stop offset="1" stop-color="#e03c3c"/></linearGradient></defs>';
      g += '<rect x="' + n1(sx(0.1)) + '" y="42" width="' + n1(sx(1.7) - sx(0.1)) + '" height="16" fill="' + BL + '" opacity="0.35"/>' + tx(sx(0.1) + 4, 54, '哈伯（約 0.1～1.7 μm）', 10, null, 'start');
      g += '<rect x="' + n1(sx(0.6)) + '" y="64" width="' + n1(sx(28) - sx(0.6)) + '" height="16" fill="' + OR + '" opacity="0.35"/>' + tx(sx(0.6) + 4, 76, '韋伯（約 0.6～28 μm）', 10, null, 'start');
      var lb = 0.0912 * (1 + P.z); g += '<rect x="30" y="92" width="' + n1(Math.max(0, sx(Math.max(0.08, 0.1216 * (1 + P.z))) - 30)) + '" height="70" fill="#000" opacity="0.18"/>';
      LINES.forEach(function (L, i) { var l = L[1] * (1 + P.z); if (l < 0.08 || l > 30) return; var x = sx(l); g += ln(x, 92, x, 162, i === 0 ? RD : PU, 2) + tx(x, 176 + (i % 2) * 12, L[0], 9.5); });
      [0.1, 0.3, 1, 3, 10, 30].forEach(function (l) { g += ln(sx(l), 162, sx(l), 167, '#888') + tx(sx(l), 205, l + ' μm', 9, 'var(--text-muted)'); });
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var lya = 0.1216 * (1 + P.z), ag = age(P.z), lt = age(0) - ag;
      inf.innerHTML = '紅移 z = ' + f2(P.z) + '：所有的波長都被拉長 <b>' + f2(1 + P.z) + ' 倍</b>。光從那裡出發時，宇宙約 <b>' + (ag < 1 ? Math.round(ag * 1000) + ' 百萬年' : f2(ag) + ' 十億年') + '</b>；光走了約 ' + f1(lt) + ' 十億年。' +
        '<br>灰色區域：比 Lyman α（' + f2(lya) + ' μm）更短的光，被宇宙早期的中性氫吸收——星系在這些波長「消失」了。' +
        (lya > 1.7 ? '<br><b>哈伯看不到</b>這個星系的大部分光：它們都被推到了紅外線。這就是為什麼需要韋伯。' : lya > 0.75 ? '<br>它的光已經移出可見光，哈伯只能用近紅外線勉強看到。' : '<br>哈伯與韋伯都能看到。'); }
    u();
  }

  var SN = []; (function () { var s = 3; function r() { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }
    for (var i = 0; i < 40; i++) { var dmp = 20 + r() * 580, v = 73 * dmp * (1 + 0.07 * (r() + r() + r() - 1.5)); SN.push([dmp, v]); } })();
  function initHLaw(root, cfg) {
    head(root, cfg.q); var P = { H: 70 }, view = el('div'), inf;
    var u = slider(root, '你猜的哈伯常數 H₀（km/s/Mpc）', 50, 90, 0.1, P.H, f1, null, function (x) { P.H = x; draw(); });
    root.appendChild(view); inf = info(root);
    var sxy = 0, sxx = 0; SN.forEach(function (p) { sxy += p[0] * p[1]; sxx += p[0] * p[0]; }); var Hfit = sxy / sxx;
    function draw() { var line = [[0, 0], [620, 620 * P.H]], fit = [[0, 0], [620, 620 * Hfit]], cmb = [[0, 0], [620, 620 * 67.4]], chi = 0;
      SN.forEach(function (p) { chi += Math.pow(p[1] - P.H * p[0], 2); });
      view.innerHTML = chart(640, 260, [{ d: [[0, 0]], c: OR, n: '超新星（距離階梯，模擬資料）', w: 3 }, { d: line, c: BL, n: '你的 H₀', w: 2 }, { d: cmb, c: RD, n: '普朗克（宇宙微波背景）67.4', w: 1.4, dash: '5,4' }],
        { x0: 0, x1: 620, y0: 0, y1: 50000, xl: '距離（百萬秒差距，Mpc）', yl: '退行速度 km/s', pts: SN.map(function (p) { return { x: p[0], y: p[1], c: OR, n: '' }; }) });
      var age = 977.8 / P.H;
      inf.innerHTML = '哈伯定律 v = H₀ d。你的 H₀ = <b>' + f1(P.H) + '</b>，最佳擬合 = <b>' + f1(Hfit) + '</b>（' + (Math.abs(P.H - Hfit) < 1 ? '很接近了' : P.H > Hfit ? '太大了' : '太小了') + '）。' +
        '<br>1/H₀ ≈ <b>' + f1(age) + ' 十億年</b>——粗略的宇宙年齡（實際約 138 億年，還要考慮膨脹的歷史）。' +
        '<br><b>哈伯張力</b>：用造父變星與超新星（距離階梯）量到約 73；用普朗克衛星的宇宙微波背景加上標準宇宙模型推算出約 67.4。兩者差約 8%，超過了各自的誤差——是量測的問題，還是新物理？'; }
    u();
  }

  function initMirror(root, cfg) {
    head(root, cfg.q); var P = { s: 0 }, view = el('div', 'display:flex;gap:10px;flex-wrap:wrap;justify-content:center'), inf;
    var u = slider(root, '鏡面對準的進度', 0, 4, 0.01, P.s, function (x) { return ['展開後', '找到並辨識', '粗略對準', '疊合', '精細共相'][Math.round(x)]; }, null, function (x) { P.s = x; draw(); });
    root.appendChild(view); inf = info(root);
    var seg = []; for (var q = -2; q <= 2; q++) for (var r = -2; r <= 2; r++) { var s3 = -q - r; if (Math.abs(s3) > 2 || (q === 0 && r === 0)) continue; seg.push([q, r]); }
    seg = seg.slice(0, 18); var off = seg.map(function (p, i) { var a = i * 2.39996; return [Math.cos(a) * (60 + (i * 37) % 50), Math.sin(a) * (60 + (i * 53) % 50)]; });
    function draw() { var s = P.s, g = '', g2 = '';
      seg.forEach(function (p) { var x = 100 + 24.4 * (p[0] + p[1] / 2), y = 100 + 21.1 * p[1], pts = []; for (var k = 0; k < 6; k++) { var a = Math.PI / 6 + k * Math.PI / 3; pts.push(n1(x + 14 * Math.cos(a)) + ',' + n1(y + 14 * Math.sin(a))); }
        g += '<polygon points="' + pts.join(' ') + '" fill="#d4af37" stroke="#8a6d1f" stroke-width="1.2"/>'; });
      var spread = s < 1 ? 1 : s < 2 ? 1 : s < 3 ? 1 - (s - 2) : 0, blur = s < 1 ? 9 - 4 * s : s < 3 ? 5 - 1.5 * (s - 1) : Math.max(1.2, 2 - (s - 3) * 0.8), vis = s < 0.5 ? 0.35 : 1;
      off.forEach(function (o) { var x = 100 + o[0] * spread * 0.9, y = 100 + o[1] * spread * 0.9; g2 += '<circle cx="' + n1(x) + '" cy="' + n1(y) + '" r="' + n1(blur) + '" fill="#fff6c0" opacity="' + (s >= 3 ? 0.18 : 0.8 * vis) + '"/>'; });
      if (s >= 3) { var k2 = s - 3; g2 += '<circle cx="100" cy="100" r="' + n1(10 - 7 * k2) + '" fill="#fff6c0" opacity="' + n1(0.5 + 0.5 * k2) + '"/>'; for (var a = 0; a < 6; a++) { var th = a * Math.PI / 3; g2 += ln(100, 100, 100 + Math.cos(th) * (20 + 50 * k2), 100 + Math.sin(th) * (20 + 50 * k2), '#fff6c0', 1, 'opacity="' + n1(0.2 + 0.5 * k2) + '"'); } }
      view.innerHTML = '<div style="width:200px;text-align:center">' + svgw('0 0 200 200', g) + '<div style="font-size:0.85em;color:var(--text-muted)">18 片主鏡</div></div><div style="width:200px;text-align:center">' + svgw('0 0 200 200', '<rect width="200" height="200" fill="#05060a"/>' + g2) + '<div style="font-size:0.85em;color:var(--text-muted)">同一顆星的影像</div></div>';
      var st = Math.round(s); inf.innerHTML = ['剛展開時，18 片鏡子各自指向不同的方向，同一顆星產生 <b>18 個分散、模糊</b>的影像。', '先拍下一大片天空，找出這 18 個影像，並逐一移動鏡子，辨認哪個影像屬於哪片鏡子。', '調整每片鏡子的角度與曲率（每片背後有 7 個致動器，可以以奈米為單位移動），讓每個影像變小、變清楚。', '把 18 個影像移到同一點<b>疊合</b>——但光還沒有「同步」，就像 18 台小望遠鏡。', '<b>共相</b>：調整每片鏡子的前後位置到奈米級，讓 18 片的光波同步，像一面 6.5 公尺的整片鏡子。韋伯星像特有的 6 道（加 2 道）繞射光芒出現了。'][st]; }
    u();
  }

  function initAll() { document.querySelectorAll('.tel-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ airy: initAiry, redshift: initRedshift, hlaw: initHLaw, mirror: initMirror })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🔭", TEL_NOTE, TELLIB, "tel-w")

AIRY = tlw({"t": "airy", "q": u"望遠鏡的解析度：兩顆星能不能分開"})
REDSHIFT = tlw({"t": "redshift", "q": u"紅移：遙遠星系的光被推進紅外線"})
HLAW = tlw({"t": "hlaw", "q": u"哈伯定律：用距離與速度量宇宙的膨脹"})
MIRROR = tlw({"t": "mirror", "q": u"韋伯的 18 片鏡子：從 18 個星點到一顆星"})
