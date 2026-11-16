# -*- coding: utf-8 -*-
"""〈微中子〉（neu_）共用：課程包裝與 NEULIB 互動元件（class="neu-w"）。

  osc     兩味振盪：距離、能量、混合角、質量平方差 → 振盪機率
  reac    反應爐電子反微中子的存活機率（三味近似）：大亞灣與 KamLAND
  cher    契忍可夫光環：緲子的銳利光環與電子的模糊光環
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

NEU_NOTE = (u"本課的推導省略部分嚴格性；振盪參數採用近年全球擬合的約略值，互動模擬為教學用的簡化模型。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def PAPER(text, ref):
    return u"%s（<span style=\"font-family:ui-monospace,Menlo,monospace;font-size:0.92em\">%s</span>）" % (text, ref)


def nuw(cfg, maxw=680):
    return wdg("neu-w", cfg, maxw)


NEULIB = r"""
(function () {
  if (window.__neuLib) return; window.__neuLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function randn() { var u = 1 - Math.random(), v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }

  function initOsc(root, cfg) {
    head(root, cfg.q); var P = { th: 45, dm: 2.5, E: 1 }, view = el('div'), inf;
    var us = [slider(root, '混合角 θ', 0, 45, 0.5, P.th, function (x) { return f1(x) + '°'; }, null, function (x) { P.th = x; draw(); }),
      slider(root, '質量平方差 Δm²（×10⁻³ eV²）', 0.05, 5, 0.05, P.dm, function (x) { return f2(x); }, null, function (x) { P.dm = x; draw(); }),
      slider(root, '微中子能量 E（GeV）', 0.1, 5, 0.05, P.E, function (x) { return f2(x) + ' GeV'; }, null, function (x) { P.E = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var s2 = Math.pow(Math.sin(2 * P.th * Math.PI / 180), 2), d = [], dm = P.dm * 1e-3, Lmax = 13000;
      for (var L = 0; L <= Lmax; L += 20) d.push([L, s2 * Math.pow(Math.sin(1.267 * dm * L / P.E), 2)]);
      var Losc = Math.PI * P.E / (1.267 * dm);
      view.innerHTML = chart(640, 220, [{ d: d, c: BL, n: 'P(ν_μ → ν_τ)：變成另一種的機率' }], { x0: 0, x1: Lmax, y0: 0, y1: 1.05, xl: '飛行距離（公里；地球直徑約 12,700 公里）',
        vl: [{ x: 295, c: OR, n: 'T2K' }, { x: 810, c: GN, n: 'NOvA' }] });
      inf.innerHTML = 'P = sin²2θ · sin²(1.27 Δm² L / E)。振盪的最大幅度由混合角決定（sin²2θ = <b>' + f2(s2) + '</b>），振盪的「波長」由 Δm² 與能量決定：完整振盪一次約 <b>' + Math.round(Losc).toLocaleString() + ' 公里</b>。' +
        '<br>大氣微中子從頭頂來時只飛了約 15 公里，幾乎沒振盪；從地球另一邊穿過來時飛了約 13,000 公里，已經振盪了很多次——這就是超級神岡看到的「上下不對稱」（第 16 課）。' +
        (P.th === 0 ? '<br>θ = 0：沒有混合，就不會振盪。' : '') + (P.dm < 0.1 ? '<br>Δm² 很小：要飛得非常遠才會振盪。如果微中子沒有質量（Δm² = 0），就永遠不會振盪。' : ''); }
    us.forEach(function (u) { u(); });
  }

  function initReac(root, cfg) {
    head(root, cfg.q); var P = { s13: 0.085, E: 4 }, view = el('div'), inf;
    var us = [slider(root, 'sin²2θ₁₃', 0, 0.2, 0.005, P.s13, function (x) { return f2(x * 1000) / 1000; }, null, function (x) { P.s13 = x; draw(); }),
      slider(root, '反微中子能量（MeV）', 2, 8, 0.1, P.E, function (x) { return f1(x) + ' MeV'; }, null, function (x) { P.E = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var d = [], s12 = 0.85, c13 = Math.pow(Math.cos(Math.asin(Math.sqrt(P.s13)) / 2), 4), Ek = P.E * 1e-3;
      for (var lg = -1; lg <= 2.5; lg += 0.005) { var L = Math.pow(10, lg), p = 1 - P.s13 * Math.pow(Math.sin(1.267 * 2.5e-3 * L / Ek), 2) - c13 * s12 * Math.pow(Math.sin(1.267 * 7.5e-5 * L / Ek), 2); d.push([lg, p]); }
      view.innerHTML = chart(640, 230, [{ d: d, c: BL, n: '電子反微中子的存活機率' }], { x0: -1, x1: 2.5, y0: 0, y1: 1.05, xl: 'log₁₀（距離／公里）：−1 = 100 公尺、0 = 1 公里、1 = 10 公里、2 = 100 公里',
        vl: [{ x: Math.log10(1.65), c: OR, n: '大亞灣遠站' }, { x: Math.log10(53), c: GN, n: 'JUNO' }, { x: Math.log10(180), c: RD, n: 'KamLAND' }] });
      inf.innerHTML = '曲線上有兩個尺度的振盪：約 <b>1～2 公里</b>處的淺凹陷，由 θ₁₃ 與「大」的質量差 Δm²₃₁ 造成；約 <b>50～200 公里</b>處的深凹陷，由 θ₁₂ 與「小」的質量差 Δm²₂₁ 造成。' +
        '<br>大亞灣把偵測器放在約 1.6 公里處，量淺凹陷的深度，2012 年得到 sin²2θ₁₃ ≈ 0.09。把 sin²2θ₁₃ 調成 0，淺凹陷就消失——在 2012 年之前，很多人以為它可能就是 0。' +
        '<br>JUNO 在約 53 公里處，同時看兩種振盪疊加的細節，用來判斷微中子的質量順序。'; }
    us.forEach(function (u) { u(); });
  }

  function initCher(root, cfg) {
    head(root, cfg.q); var P = { t: 'mu', p: 500 }, view = el('div', 'max-width:420px;margin:0 auto'), inf;
    var b = el('div', 'margin:4px 0'); [['緲子', 'mu'], ['電子', 'e']].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.t = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); root.appendChild(b); mark(b, 'mu');
    var u = slider(root, '動量（MeV/c）', 50, 2000, 10, P.p, function (x) { return x + ' MeV/c'; }, null, function (x) { P.p = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var m = P.t === 'mu' ? 105.7 : 0.511, E = Math.sqrt(P.p * P.p + m * m), beta = P.p / E, n = 1.33, c = 1 / (n * beta), on = c < 1, ang = on ? Math.acos(c) : 0, R = 150 * Math.tan(ang) / Math.tan(Math.acos(1 / n)), g = '';
      g += '<rect x="10" y="10" width="380" height="380" fill="none" stroke="var(--border)"/>';
      if (on) { var k = P.t === 'mu' ? 260 : 380; for (var i = 0; i < k; i++) { var th = Math.random() * 2 * Math.PI, rr = R * (P.t === 'mu' ? (1 + 0.02 * randn()) : (0.75 + 0.35 * Math.random())) * (P.t === 'e' && Math.random() < 0.3 ? 0.4 + 0.6 * Math.random() : 1);
          g += '<circle cx="' + n1(200 + rr * Math.cos(th)) + '" cy="' + n1(200 + rr * Math.sin(th)) + '" r="3" fill="' + (P.t === 'mu' ? BL : OR) + '" opacity="0.75"/>'; } }
      g += tx(200, 380, '偵測器內壁上被打亮的光電倍增管（示意）', 10, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 400 400', g);
      inf.innerHTML = on ? '速度 β = ' + f2(beta * 1000) / 1000 + '，比水中的光速（1/1.33 ≈ 0.75）還快，放出契忍可夫光，光錐的半角 θ = arccos(1/(nβ)) = <b>' + f1(ang * 180 / Math.PI) + '°</b>（上限約 41°）。' +
        (P.t === 'mu' ? '<br><b>緲子</b>：很重，直直地前進，留下一個<b>邊緣銳利</b>的光環。' : '<br><b>電子</b>：很輕，在水中不斷散射並產生簇射，光環的邊緣<b>模糊</b>、還有內部的散點。') +
        '<br>從光環的形狀可以分辨是緲子微中子還是電子微中子造成的事件——超級神岡的錯誤分類率只有約 1%。'
        : '速度 β = ' + f2(beta * 1000) / 1000 + '，<b>沒有</b>超過水中的光速，不會放出契忍可夫光。這個「門檻」讓緲子在動量約 120 MeV/c 以下時看不見。'; }
    u();
  }

  function initAll() { document.querySelectorAll('.neu-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ osc: initOsc, reac: initReac, cher: initCher })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"👻", NEU_NOTE, NEULIB, "neu-w")

OSC = nuw({"t": "osc", "q": u"兩味振盪：微中子飛得越遠，越可能「變身」"})
REAC = nuw({"t": "reac", "q": u"反應爐微中子：在不同距離，還剩下多少電子反微中子？"})
CHER = nuw({"t": "cher", "q": u"契忍可夫光環：緲子與電子留下不同的「指紋」"})
