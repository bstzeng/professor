# -*- coding: utf-8 -*-
"""〈古典力學〉（cmc_）共用：課程包裝與 CMLIB 互動元件（class="cm-w"）。

  proj    拋體：真空 vs. 線性阻力 vs. 二次阻力
  osc     阻尼與受迫振動：x(t) 與共振曲線
  orbit   中心力軌道：初速決定圓、橢圓、拋物線、雙曲線
  phase   單擺相空間：振盪、分界線、旋轉
  dpend   雙擺：初始角度差 10⁻ⁿ 的兩個雙擺如何分道揚鑣
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

CM_NOTE = (u"本課的推導以物理直覺為主，省略部分數學嚴格性；數值為教學用的近似值。"
           u"只想看概念的讀者，可以跳過推導，直接看圖、互動與「重點」。")


def X(tid, name, text=None):
    """連到站上其他主題。"""
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def cmw(cfg, maxw=680):
    return wdg("cm-w", cfg, maxw)


CMLIB = r"""
(function () {
  if (window.__cmLib) return; window.__cmLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', PU = '#8a5cb8', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function pth(pts, sx, sy) { return pts.map(function (p, i) { return (i ? 'L' : 'M') + n1(sx(p[0])) + ' ' + n1(sy(p[1])); }).join(''); }

  /* ---------- 拋體 ---------- */
  function initProj(root, cfg) {
    head(root, cfg.q); var P = { v: 30, a: 45, k: 0.02 }, view = el('div'), inf;
    var us = [slider(root, '初速 v₀', 5, 60, 1, P.v, function (x) { return x + ' m/s'; }, null, function (x) { P.v = x; draw(); }),
      slider(root, '仰角 θ', 5, 85, 1, P.a, function (x) { return x + '°'; }, null, function (x) { P.a = x; draw(); }),
      slider(root, '阻力強度（k/m）', 0, 0.1, 0.005, P.k, function (x) { return x === 0 ? '0（真空）' : f2(x * 1000) / 1000 + ''; }, null, function (x) { P.k = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function run(mode) { var g = 9.8, th = P.a * Math.PI / 180, x = 0, y = 0, vx = P.v * Math.cos(th), vy = P.v * Math.sin(th), dt = 0.002, t = 0, pts = [[0, 0]], ym = 0, kk = P.k;
      while (t < 60) { var sp = Math.sqrt(vx * vx + vy * vy), ax, ay;
        if (mode === 0) { ax = 0; ay = -g; } else if (mode === 1) { ax = -kk * 10 * vx; ay = -g - kk * 10 * vy; } else { ax = -kk * sp * vx; ay = -g - kk * sp * vy; }
        vx += ax * dt; vy += ay * dt; x += vx * dt; y += vy * dt; t += dt; if (y > ym) ym = y; if (y < 0) break; if (Math.round(t / dt) % 10 === 0) pts.push([x, y]); }
      pts.push([x, Math.max(y, 0)]); return { p: pts, R: x, H: ym, T: t }; }
    function draw() { var r0 = run(0), r1 = run(1), r2 = run(2), W = 640, H = 260, L = 40, B = 30, T = 16;
      var xm = Math.max(r0.R, 1) * 1.05, ymx = Math.max(r0.H, 1) * 1.1, s = Math.min((W - L - 10) / xm, (H - T - B) / ymx);
      function sx(v) { return L + v * s; } function sy(v) { return H - B - v * s; }
      var g = ln(L, H - B, W - 10, H - B, '#999') + ln(L, T, L, H - B, '#999');
      nice(0, xm, 6).forEach(function (v) { if (sx(v) < W - 10) g += tx(sx(v), H - B + 14, v, 9, 'var(--text-muted)'); });
      g += tx(W - 12, H - 4, '水平距離（m）', 9.5, 'var(--text-muted)', 'end');
      var on = P.k > 0;
      g += '<path d="' + pth(r0.p, sx, sy) + '" fill="none" stroke="' + BL + '" stroke-width="2.2"/>';
      if (on) { g += '<path d="' + pth(r1.p, sx, sy) + '" fill="none" stroke="' + GN + '" stroke-width="2" stroke-dasharray="6 4"/>';
        g += '<path d="' + pth(r2.p, sx, sy) + '" fill="none" stroke="' + RD + '" stroke-width="2.2"/>'; }
      g += ln(L + 10, T + 6, L + 26, T + 6, BL, 2.5) + tx(L + 30, T + 10, '真空（拋物線）', 9.5, 'currentColor', 'start');
      if (on) g += ln(L + 130, T + 6, L + 146, T + 6, GN, 2.5, 'stroke-dasharray="6 4"') + tx(L + 150, T + 10, '線性阻力', 9.5, 'currentColor', 'start') + ln(L + 220, T + 6, L + 236, T + 6, RD, 2.5) + tx(L + 240, T + 10, '二次阻力（真實空氣）', 9.5, 'currentColor', 'start');
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var R0 = P.v * P.v * Math.sin(2 * P.a * Math.PI / 180) / 9.8;
      inf.innerHTML = '真空：射程 <b>' + f1(r0.R) + ' m</b>（公式 v₀² sin2θ / g = ' + f1(R0) + ' m）、最高 ' + f1(r0.H) + ' m、飛行 ' + f2(r0.T) + ' s。' +
        (on ? '<br>二次阻力：射程 <b style="color:' + RD + '">' + f1(r2.R) + ' m</b>（只剩 ' + Math.round(r2.R / r0.R * 100) + '%）、最高 ' + f1(r2.H) + ' m。軌跡不再對稱：上升平緩、下墜陡峭。' : '') +
        '<br>' + (on ? '有阻力時，最遠的角度<b>小於 45°</b>——試著把仰角調低幾度看看射程是否變遠。' : '真空中 45° 射最遠；30° 和 60° 的射程一樣（sin2θ 對稱）。');
    }
    us.forEach(function (u) { u(); });
  }

  /* ---------- 阻尼與受迫振動 ---------- */
  function initOsc(root, cfg) {
    head(root, cfg.q); var P = { z: cfg.z !== undefined ? cfg.z : 0.1, w: cfg.w !== undefined ? cfg.w : 0, F: cfg.drive ? 1 : 0 }, view = el('div'), view2 = el('div'), inf;
    var bar = el('div', 'margin:4px 0'); [['自由振動（不推）', 0], ['受迫振動（週期性推）', 1]].forEach(function (o) { var b = btn(o[0], o[1]); b.onclick = function () { P.F = o[1]; mark(bar, o[1]); draw(); }; bar.appendChild(b); }); root.appendChild(bar); mark(bar, P.F);
    var us = [slider(root, '阻尼比 ζ', 0, 2, 0.01, P.z, function (x) { return f2(x) + (x < 1 ? '（欠阻尼）' : x === 1 ? '（臨界阻尼）' : '（過阻尼）'); }, null, function (x) { P.z = x; draw(); }),
      slider(root, '驅動頻率 Ω / ω₀', 0.1, 3, 0.01, P.w || 1, function (x) { return f2(x); }, null, function (x) { P.w = x; draw(); })];
    root.appendChild(view); root.appendChild(view2); inf = info(root);
    function draw() { var w0 = 2 * Math.PI, z = P.z, W = P.w * w0, x = P.F ? 0 : 1, v = 0, dt = 0.002, d = [], t;
      for (t = 0; t <= 12; t += dt) { if (Math.round(t / dt) % 10 === 0) d.push([t, x]); var a = -2 * z * w0 * v - w0 * w0 * x + (P.F ? w0 * w0 * Math.cos(W * t) : 0); v += a * dt; x += v * dt; }
      var amp = 1 / Math.sqrt(Math.pow(1 - P.w * P.w, 2) + Math.pow(2 * z * P.w, 2)), ym = P.F ? Math.max(1.2, Math.min(amp * 1.25, 12)) : 1.2;
      view.innerHTML = chart(640, 200, [{ d: d, c: BL, n: '位移 x(t)' }], { x0: 0, x1: 12, y0: -ym, y1: ym, xl: '時間（以自然週期為單位）' });
      if (P.F) { var c = []; for (var r = 0.05; r <= 3; r += 0.01) c.push([r, Math.min(1 / Math.sqrt(Math.pow(1 - r * r, 2) + Math.pow(2 * z * r, 2)), 12)]);
        view2.innerHTML = chart(640, 170, [{ d: c, c: RD, n: '穩態振幅（共振曲線）' }], { x0: 0, x1: 3, y0: 0, y1: Math.min(Math.max.apply(null, c.map(function (p) { return p[1]; })) * 1.1, 13), xl: 'Ω / ω₀', pts: [{ x: P.w, y: Math.min(amp, 12), c: OR }] }); }
      else view2.innerHTML = '';
      inf.innerHTML = P.F ? '穩態振幅是靜態位移的 <b>' + f2(amp) + ' 倍</b>。' + (Math.abs(P.w - 1) < 0.08 ? '驅動頻率接近自然頻率——<b>共振</b>！阻尼越小，峰越高越尖。' : '把驅動頻率調到 1 附近看看。') + (z < 0.05 ? '<br>阻尼極小時，共振振幅可以大到結構承受不了。' : '') + '<br>Q 值 ≈ 1/(2ζ) = ' + (z > 0 ? f1(1 / (2 * z)) : '∞') + '：Q 越高，共振越尖銳。'
        : (z === 0 ? '沒有阻尼：永遠振盪下去（簡諧運動）。' : z < 1 ? '<b>欠阻尼</b>：一邊振盪一邊衰減，振幅按 e<sup>−ζω₀t</sup> 縮小。' : z === 1 ? '<b>臨界阻尼</b>：最快回到平衡、不越過——汽車避震器與門弓器的設計目標。' : '<b>過阻尼</b>：慢吞吞地爬回平衡，阻尼太大反而變慢。');
    }
    us.forEach(function (u) { u(); });
  }

  /* ---------- 軌道 ---------- */
  function initOrbit(root, cfg) {
    head(root, cfg.q); var P = { v: cfg.v || 1 }, view = el('div'), inf;
    var u = slider(root, '近日點速度 ÷ 圓軌道速度', 0.3, 1.6, 0.01, P.v, function (x) { return f2(x); }, null, function (x) { P.v = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var x = 1, y = 0, vx = 0, vy = P.v, dt = 0.002, pts = [[x, y]], t = 0, E = P.v * P.v / 2 - 1, e = Math.abs(P.v * P.v - 1), bound = E < 0;
      var Tmax = bound ? 2 * Math.PI * Math.pow(1 / (2 * -E), 1.5) * 1.02 : 12;
      for (t = 0; t < Tmax; t += dt) { var r = Math.sqrt(x * x + y * y), a = -1 / (r * r * r); vx += a * x * dt; vy += a * y * dt; x += vx * dt; y += vy * dt; if (Math.round(t / dt) % 5 === 0) pts.push([x, y]); if (r > 12) break; }
      var Wd = 640, Hd = 300, vis = pts.filter(function (p) { return p[0] * p[0] + p[1] * p[1] < 36; }), x0 = 0, x1 = 1, y0 = 0, y1 = 0;
      vis.forEach(function (p) { x0 = Math.min(x0, p[0]); x1 = Math.max(x1, p[0]); y0 = Math.min(y0, p[1]); y1 = Math.max(y1, p[1]); }); pts = vis;
      var S = Math.min((Wd - 40) / (x1 - x0 || 1), (Hd - 40) / (y1 - y0 || 1)), cx = Wd / 2 - S * (x0 + x1) / 2, cy = Hd / 2 + S * (y0 + y1) / 2;
      function sx(v) { return cx + v * S; } function sy(v) { return cy - v * S; }
      var g = '<rect x="0" y="0" width="' + Wd + '" height="' + Hd + '" fill="none"/>';
      g += '<path d="' + pth(pts, sx, sy) + '" fill="none" stroke="' + (bound ? BL : RD) + '" stroke-width="2"/>';
      g += '<circle cx="' + n1(sx(0)) + '" cy="' + n1(sy(0)) + '" r="9" fill="' + OR + '"/>' + tx(sx(0), sy(0) + 24, '太陽', 10, OR);
      g += '<circle cx="' + n1(sx(1)) + '" cy="' + n1(sy(0)) + '" r="5" fill="' + BL + '"/>' + ln(sx(1), sy(0), sx(1), sy(0) - 34 * P.v, GN, 2) + tx(sx(1) + 6, sy(0) - 34 * P.v, 'v₀', 10, GN, 'start');
      view.innerHTML = svgw('0 0 ' + Wd + ' ' + Hd, g);
      var kind = Math.abs(P.v - 1) < 0.005 ? '圓' : P.v < Math.SQRT2 - 0.005 ? '橢圓' : Math.abs(P.v - Math.SQRT2) <= 0.005 ? '拋物線' : '雙曲線';
      inf.innerHTML = '軌道形狀：<b>' + kind + '</b>，離心率 e = |v²/v꜀² − 1| = <b>' + f2(e) + '</b>；比能量 E = v²/2 − GM/r = <b>' + f2(E) + '</b>（' + (bound ? '負值：被束縛，永遠繞回來' : '≥ 0：逃逸，不再回來') + '）。' +
        (bound ? '<br>半長軸 a = ' + f2(1 / (2 * -E)) + '，週期 T ∝ a<sup>3/2</sup> = 圓軌道的 ' + f2(Math.pow(1 / (2 * -E), 1.5)) + ' 倍（克卜勒第三定律）。' : '') +
        '<br>速度到圓軌道的 √2 ≈ 1.414 倍，就是<b>逃逸速度</b>。';
    }
    u();
  }

  /* ---------- 單擺相空間 ---------- */
  function initPhase(root, cfg) {
    head(root, cfg.q); var P = { E: cfg.E !== undefined ? cfg.E : 0.5 }, view = el('div'), inf;
    var u = slider(root, '能量 E（以 mgL 為單位，最低點為 0）', 0.05, 3, 0.01, P.E, function (x) { return f2(x); }, null, function (x) { P.E = x; draw(); });
    root.appendChild(view); inf = info(root);
    function curve(E) { var up = [], dn = []; for (var th = -Math.PI; th <= Math.PI + 1e-9; th += 0.01) { var s = 2 * (E - (1 - Math.cos(th))); var w = s >= 0 ? Math.sqrt(s) : NaN; up.push([th, w]); dn.push([th, -w]); } return [up, dn]; }
    function draw() { var S = [];
      [0.2, 0.6, 1.0, 1.4, 1.8, 2.6].forEach(function (E) { var c = curve(E); S.push({ d: c[0], c: GY, w: 0.8 }); S.push({ d: c[1], c: GY, w: 0.8 }); });
      var sep = curve(2); S.push({ d: sep[0], c: OR, w: 1.6, dash: '5 4' }); S.push({ d: sep[1], c: OR, w: 1.6, dash: '5 4' });
      var c = curve(P.E); S.push({ d: c[0], c: BL, w: 2.6 }); S.push({ d: c[1], c: BL, w: 2.6 });
      view.innerHTML = chart(640, 280, S, { x0: -Math.PI, x1: Math.PI, y0: -2.6, y1: 2.6, xl: '角度 θ（弧度，−π 到 π）', yl: '角速度 ω' });
      inf.innerHTML = (P.E < 2 ? '<b>E &lt; 2：振盪</b>。軌跡是一個封閉圈：來回擺動，在最高點速度歸零。' + (P.E < 0.3 ? '能量很小時，圈幾乎是橢圓——這就是小角度近似下的簡諧運動。' : '能量越大，圈越扁、週期越長，不再是簡諧運動。')
        : Math.abs(P.E - 2) < 0.03 ? '<b>E ≈ 2：分界線</b>（橘色虛線）。擺錘剛好爬到正上方，要花無限長的時間才到——這條線把兩種運動分開。'
        : '<b>E &gt; 2：旋轉</b>。擺錘翻過頂點，一直往同一方向轉，軌跡不再封閉（θ = −π 和 π 是同一點）。') +
        '<br>相空間中每一點代表系統的一個完整狀態（位置＋速度）；能量守恆讓軌跡只能沿著等能量線走，<b>軌跡永不相交</b>。';
    }
    u();
  }

  /* ---------- 雙擺 ---------- */
  function initDpend(root, cfg) {
    head(root, cfg.q); var P = { a: 120, n: 6, T: 20 }, view = el('div'), view2 = el('div'), inf;
    var us = [slider(root, '初始角度 θ₁ = θ₂', 10, 170, 1, P.a, function (x) { return x + '°'; }, null, function (x) { P.a = x; draw(); }),
      slider(root, '第二個雙擺的初始偏差（10⁻ⁿ 弧度）', 1, 12, 1, P.n, function (x) { return '10⁻' + x + ' 弧度'; }, null, function (x) { P.n = x; draw(); })];
    root.appendChild(view); root.appendChild(view2); inf = info(root);
    function f(s) { var t1 = s[0], t2 = s[1], w1 = s[2], w2 = s[3], d = t1 - t2, g = 9.8, den = 3 - Math.cos(2 * d);
      var a1 = (-g * 3 * Math.sin(t1) - g * Math.sin(t1 - 2 * t2) - 2 * Math.sin(d) * (w2 * w2 + w1 * w1 * Math.cos(d))) / den;
      var a2 = (2 * Math.sin(d) * (w1 * w1 * 2 + g * 2 * Math.cos(t1) + w2 * w2 * Math.cos(d))) / den; return [w1, w2, a1, a2]; }
    function rk(s, h) { var k1 = f(s), k2 = f(s.map(function (v, i) { return v + h / 2 * k1[i]; })), k3 = f(s.map(function (v, i) { return v + h / 2 * k2[i]; })), k4 = f(s.map(function (v, i) { return v + h * k3[i]; }));
      return s.map(function (v, i) { return v + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]); }); }
    function draw() { var a = P.a * Math.PI / 180, A = [a, a, 0, 0], Bs = [a, a + Math.pow(10, -P.n), 0, 0], h = 0.002, dA = [], dB = [], sep = [], tA = [], tB = [], tdiv = null;
      for (var i = 0, t = 0; t <= P.T; i++, t += h) { if (i % 10 === 0) { dA.push([t, A[1]]); dB.push([t, Bs[1]]); var dd = Math.abs(A[0] - Bs[0]) + Math.abs(A[1] - Bs[1]); sep.push([t, Math.log(Math.max(dd, 1e-16)) / Math.LN10]); if (tdiv === null && dd > 0.5) tdiv = t;
          if (i % 20 === 0) { tA.push([Math.sin(A[0]) + Math.sin(A[1]), -Math.cos(A[0]) - Math.cos(A[1])]); tB.push([Math.sin(Bs[0]) + Math.sin(Bs[1]), -Math.cos(Bs[0]) - Math.cos(Bs[1])]); } }
        A = rk(A, h); Bs = rk(Bs, h); }
      view.innerHTML = chart(640, 190, [{ d: dA, c: BL, n: '雙擺 A 的 θ₂', w: 1.6 }, { d: dB, c: RD, n: '雙擺 B 的 θ₂', w: 1.6, dash: '4 3' }], { x0: 0, x1: P.T, xl: '時間（秒，擺長 1 m）' });
      view2.innerHTML = chart(640, 150, [{ d: sep, c: PU, n: 'log₁₀（兩者狀態差）' }], { x0: 0, x1: P.T, y0: -13, y1: 1, xl: '時間（秒）' });
      inf.innerHTML = '一開始兩條曲線完全重疊。' + (tdiv !== null ? '大約在 <b>' + f1(tdiv) + ' 秒</b>時，兩個雙擺已經走上完全不同的路。' : '在這段時間內兩者仍然接近——試著把初始角度調大。') +
        '<br>下圖的紫線在對數座標上近似一條<b>斜直線</b>：誤差隨時間<b>指數成長</b>（李亞普諾夫指數）。初始誤差每小 10 倍，只多換來固定的一小段可預測時間。' + (P.a < 40 ? '<br>小角度時雙擺接近兩個耦合振子（第 21 課），運動規則、不混沌。' : '');
    }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.cm-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ proj: initProj, osc: initOsc, orbit: initOrbit, phase: initPhase, dpend: initDpend })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🪐", CM_NOTE, CMLIB, "cm-w")

PROJ = cmw({"t": "proj", "q": u"拋體模擬：調整初速、仰角與空氣阻力"})
OSC_FREE = cmw({"t": "osc", "q": u"阻尼振動：調整阻尼比，看系統怎麼回到平衡", "z": 0.1})
OSC_DRIVE = cmw({"t": "osc", "q": u"受迫振動與共振：調整驅動頻率與阻尼", "z": 0.05, "w": 0.8, "drive": 1})
ORBIT = cmw({"t": "orbit", "q": u"軌道模擬：只改變初速，軌道就從圓變成橢圓、拋物線、雙曲線"})
PHASE = cmw({"t": "phase", "q": u"單擺的相空間：調整能量，看軌跡的三種形態"})
DPEND = cmw({"t": "dpend", "q": u"雙擺的蝴蝶效應：兩個幾乎一模一樣的雙擺"})
