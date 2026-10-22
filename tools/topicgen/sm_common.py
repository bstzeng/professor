# -*- coding: utf-8 -*-
"""〈從材料力學到建築承重〉（sm_）共用：課程包裝與 SMLIB 互動元件。

逐步推導（steps）與數值驗證（check）沿用 md_common 的 MDLIB；本檔的 SMLIB（class="sm-w"）提供：
  lj        原子間位能與力 → 彈性模數、理論強度       ss       應力–應變曲線（鋼、混凝土）
  mohr      莫爾圓與主應力                           beam     梁的剪力圖、彎矩圖、撓度
  section   斷面慣性矩比較                           buckle   歐拉挫屈與短柱壓碎
  truss     桁架內力（節點法，自動求解）              loads    樓板載重與柱軸力計算
  rcbeam    RC 梁的彎矩強度（等值矩形應力塊）         scale    平方立方定律
  seismic   等值靜力法的基底剪力（教學簡化）          weibull  尺寸效應（威布爾統計）
  daf       共振與動力放大（含阻尼）
"""
from md_common import make_with, S, steps, check, mw, star, MDLIB
from cc_common import wdg, LS, XL, M, D, KATEX
from qt_common import BASEJS

SM_NOTE = (u"本課程為教學用的計算示範，數值取自常用教科書與台灣規範的公開條文；實際設計須依現行法規、由依法登記的結構技師或建築師辦理簽證。")


def sv(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("sm-w", cfg)


SMLIB = r"""
(function () {
  if (window.__smLib) return; window.__smLib = 1;
""" + BASEJS + r"""
  var _sl = slider; slider = function (root, lab, min, max, step, val, fmt, k, cb) { var u = _sl(root, lab, min, max, step, val, fmt, k, cb); var b = root.lastChild && root.lastChild.querySelector('b'); if (b) b.textContent = fmt(val); return u; };
  var BL = '#3a6ea5', OR = '#e07a2f', GR = '#4caf50', RD = '#e0605a', PU = '#8e5bd1', GY = '#888';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function f0(v) { return Math.round(v).toLocaleString(); }
  function g3(v) { if (!isFinite(v)) return '—'; var a = Math.abs(v); if (a !== 0 && (a < 1e-3 || a >= 1e6)) return v.toExponential(2); return (Math.round(v * 1000) / 1000).toLocaleString(); }
  function view(W, H, x0, x1, y0, y1, pad) { pad = pad || 0; var o = {}; if (y1 === null) y1 = y0 + (x1 - x0) * (H - 2 * pad) / (W - 2 * pad);
    o.x = function (v) { return pad + (v - x0) / (x1 - x0) * (W - 2 * pad); }; o.y = function (v) { return H - pad - (v - y0) / (y1 - y0) * (H - 2 * pad); };
    o.poly = function (p, fill, stroke, op, sw) { return '<polygon points="' + p.map(function (q) { return n1(o.x(q[0])) + ',' + n1(o.y(q[1])); }).join(' ') + '" fill="' + fill + '" fill-opacity="' + (op === undefined ? 0.3 : op) + '" stroke="' + (stroke || fill) + '" stroke-width="' + (sw || 1.2) + '"/>'; };
    o.path = function (p, c, w, ex) { var d = ''; p.forEach(function (q, i) { d += (i ? 'L' : 'M') + n1(o.x(q[0])) + ' ' + n1(o.y(q[1])); }); return '<path d="' + d + '" fill="none" stroke="' + c + '" stroke-width="' + (w || 2) + '" ' + (ex || '') + '/>'; };
    o.l = function (a, b, c, d, col, w, ex) { return ln(o.x(a), o.y(b), o.x(c), o.y(d), col, w, ex); };
    o.t = function (x, y, s, sz, c, anc) { return tx(o.x(x), o.y(y), s, sz || 11, c, anc); };
    o.dot = function (x, y, c, r) { return '<circle cx="' + n1(o.x(x)) + '" cy="' + n1(o.y(y)) + '" r="' + (r || 4) + '" fill="' + c + '"/>'; };
    o.circ = function (x, y, r, c, w) { return '<ellipse cx="' + n1(o.x(x)) + '" cy="' + n1(o.y(y)) + '" rx="' + n1(Math.abs(o.x(x + r) - o.x(x))) + '" ry="' + n1(Math.abs(o.y(y + r) - o.y(y))) + '" fill="none" stroke="' + c + '" stroke-width="' + (w || 2) + '"/>'; };
    o.svg = function (g) { return svgw('0 0 ' + W + ' ' + H, g); }; return o; }
  function arrow(V, x1, y1, x2, y2, c, w) { var a = Math.atan2(V.y(y2) - V.y(y1), V.x(x2) - V.x(x1)), X = V.x(x2), Y = V.y(y2), h = 7;
    return V.l(x1, y1, x2, y2, c, w || 2) + '<polygon points="' + n1(X) + ',' + n1(Y) + ' ' + n1(X - h * Math.cos(a - 0.4)) + ',' + n1(Y - h * Math.sin(a - 0.4)) + ' ' + n1(X - h * Math.cos(a + 0.4)) + ',' + n1(Y - h * Math.sin(a + 0.4)) + '" fill="' + c + '"/>'; }

  /* ---------- 原子間位能 ---------- */
  function initLj(root, cfg) {
    head(root, cfg.q); var eps = 0.4, sig = 2.3, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '鍵能 ε（eV）', 0.05, 1.5, 0.01, eps, f2, 'e', function (q) { eps = q; draw(); });
    slider(root, '原子尺度 σ（Å）', 1.5, 4, 0.05, sig, f2, 's', function (q) { sig = q; draw(); });
    function draw() { var e = eps * 1.602e-19, s = sig * 1e-10, r0 = Math.pow(2, 1 / 6) * s, k = 72 * e / (Math.pow(2, 1 / 3) * s * s), E = k / r0;
      var Fm = 0; for (var x = 1.0; x < 2.5; x += 0.0005) { var F = 24 * e / s * (Math.pow(1 / x, 7) - 2 * Math.pow(1 / x, 13)); Fm = Math.max(Fm, F); }
      var sth = Fm / (r0 * r0), U = [], Fd = [];
      for (x = 0.95; x <= 2.5; x += 0.005) { U.push([x, 4 * (Math.pow(1 / x, 12) - Math.pow(1 / x, 6))]); Fd.push([x, -24 * (2 * Math.pow(1 / x, 13) - Math.pow(1 / x, 7)) / 2.4]); }
      v.innerHTML = chart(640, 230, [{ d: U, c: BL, n: '位能 U / ε' }, { d: Fd, c: OR, n: '拉開需要的力（縮放）', dash: '5 4' }], { y0: -1.2, y1: 1.2, xl: '原子間距 r / σ', vl: [{ x: Math.pow(2, 1 / 6), c: GR, n: '平衡 r₀' }] }) +
        '<table style="width:100%;border-collapse:collapse;margin-top:6px"><tr><td style="padding:3px">平衡距離 r₀</td><td style="text-align:right;font-family:monospace">' + f2(r0 * 1e10) + ' Å</td></tr>' +
        '<tr><td style="padding:3px">鍵的彈簧常數 k = U″(r₀)</td><td style="text-align:right;font-family:monospace">' + g3(k) + ' N/m</td></tr>' +
        '<tr><td style="padding:3px">估計彈性模數 E ≈ k / r₀</td><td style="text-align:right;font-family:monospace"><b>' + g3(E / 1e9) + ' GPa</b></td></tr>' +
        '<tr><td style="padding:3px">理論強度 ≈ F<sub>max</sub> / r₀²</td><td style="text-align:right;font-family:monospace"><b>' + g3(sth / 1e9) + ' GPa</b>（E 的 ' + f2(sth / E * 100) + '%）</td></tr></table>';
      inf.innerHTML = '位能曲線底部的<b>曲率</b>決定彈性模數，曲線上「最陡的地方」決定把鍵拉斷要多大的力。不管怎麼調，理論強度都約是 E 的 3–4%（E/30 左右）；真實鋼材的降伏強度只有 E 的約 0.1%。'; }
    draw(); }

  /* ---------- 應力應變 ---------- */
  function initSs(root, cfg) {
    head(root, cfg.q); var m = cfg.m || 'steel', e = 0.001, bar = el('div'), v = el('div'), inf = info(root); root.insertBefore(bar, inf); root.insertBefore(v, inf);
    [['steel', '低碳鋼（拉伸）'], ['concrete', '混凝土（壓縮）']].forEach(function (x) { var b = btn(x[1], x[0]); b.onclick = function () { m = x[0]; mark(bar, m); draw(); }; bar.appendChild(b); }); mark(bar, m);
    var su; su = slider(root, '應變 ε（‰）', 0, 200, 0.1, 1, f1, 'e', function (q) { e = q / 1000; draw(); });
    function steel(x) { var E = 200000, fy = 250, eh = 0.02, fu = 400, eu = 0.15, ef = 0.2; if (x <= fy / E) return E * x; if (x <= eh) return fy;
      if (x <= eu) return fy + (fu - fy) * Math.sin((x - eh) / (eu - eh) * Math.PI / 2); if (x <= ef) return fu - 80 * Math.pow((x - eu) / (ef - eu), 2); return NaN; }
    function conc(x) { var fc = 28, e0 = 0.002, ecu = 0.0038; if (x <= e0) return fc * (2 * x / e0 - Math.pow(x / e0, 2)); if (x <= ecu) return fc * (1 - 0.15 * (x - e0) / (ecu - e0)); return NaN; }
    function draw() { var F = m === 'steel' ? steel : conc, xm = m === 'steel' ? 0.2 : 0.004, d = [], x = Math.min(e, xm);
      for (var t = 0; t <= xm * 1.0001; t += xm / 600) { var y = F(t); if (isFinite(y)) d.push([t * 1000, y]); }
      var y = F(x), phase = m === 'steel' ? (x <= 250 / 200000 ? '彈性區：應力 = E × 應變，卸載會回到原點' : x <= 0.02 ? '降伏平台：應變一直增加，應力幾乎不變（差排在滑動）' : x <= 0.15 ? '應變硬化：差排互相糾纏，要更大的力才能繼續變形' : x <= 0.2 ? '頸縮：某一段截面變細，名目應力下降，接著斷裂' : '已斷裂') :
        (x <= 0.0005 ? '接近線性：微裂縫還不多' : x <= 0.002 ? '微裂縫增加，曲線變平，在 ε ≈ 0.002 達到最大強度 fc′' : x <= 0.0038 ? '下降段：裂縫連成一片，規範取 ε = 0.003 為壓碎應變' : '已壓碎');
      v.innerHTML = chart(640, 240, [{ d: d, c: m === 'steel' ? BL : GY, n: m === 'steel' ? '低碳鋼（示意）' : '混凝土 fc′ = 28 MPa（示意）' }], { y0: 0, xl: '應變（‰）', yl: '應力 MPa', pts: isFinite(y) ? [{ x: x * 1000, y: y, c: OR, n: f1(y) + ' MPa' }] : [] });
      inf.innerHTML = phase + '。' + (m === 'steel' ? '<br>鋼的降伏應變只有 0.125%，但斷裂時可以伸長 20% 以上：這就是<b>韌性</b>。' : '<br>混凝土的抗拉強度只有抗壓的約 10%，而且很脆：這就是為什麼要放鋼筋。'); }
    draw(); }

  /* ---------- 莫爾圓 ---------- */
  function initMohr(root, cfg) {
    head(root, cfg.q); var sx = 80, sy = -20, txy = 40, th = 0, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, 'σx（MPa，拉為正）', -100, 100, 1, sx, f0, 'x', function (q) { sx = q; draw(); });
    slider(root, 'σy（MPa）', -100, 100, 1, sy, f0, 'y', function (q) { sy = q; draw(); });
    slider(root, 'τxy（MPa）', -80, 80, 1, txy, f0, 't', function (q) { txy = q; draw(); });
    slider(root, '元素旋轉角 θ', -90, 90, 1, th, function (q) { return q + '°'; }, 'th', function (q) { th = q; draw(); });
    function draw() { var c = (sx + sy) / 2, R = Math.sqrt(Math.pow((sx - sy) / 2, 2) + txy * txy), t = th * Math.PI / 180;
      var sxp = c + (sx - sy) / 2 * Math.cos(2 * t) + txy * Math.sin(2 * t), txp = -(sx - sy) / 2 * Math.sin(2 * t) + txy * Math.cos(2 * t), syp = 2 * c - sxp;
      var V = view(380, 300, -200, 200, -150, null, 8), g = V.l(-200, 0, 200, 0, GY, 1) + V.l(0, -150, 0, 150, GY, 1) + V.t(190, 8, 'σ', 12) + V.t(8, 140, 'τ', 12);
      g += V.circ(c, 0, R, BL) + V.dot(c, 0, BL, 3) + V.l(sx, txy, sy, -txy, GY, 1, 'stroke-dasharray="4 3"') + V.dot(sx, txy, GY, 4) + V.l(sxp, txp, syp, -txp, OR, 2) + V.dot(sxp, txp, OR, 5) + V.dot(syp, -txp, OR, 4);
      g += V.dot(c + R, 0, RD, 5) + V.dot(c - R, 0, RD, 5) + V.t(c + R, -14, 'σ₁', 11, RD) + V.t(c - R, -14, 'σ₂', 11, RD);
      var W = view(220, 220, -2, 2, -2, null, 4), q = 0.8, ct = Math.cos(t), st = Math.sin(t);
      function rot(p) { return [p[0] * ct - p[1] * st, p[0] * st + p[1] * ct]; }
      var sq = [[-q, -q], [q, -q], [q, q], [-q, q]].map(rot), h = W.poly(sq, OR, OR, 0.15);
      var nx = rot([1, 0]); h += arrow(W, nx[0] * q, nx[1] * q, nx[0] * (q + Math.sign(sxp) * 0.6 + 0.001), nx[1] * (q + Math.sign(sxp) * 0.6), OR);
      h += W.t(0, -1.8, '旋轉後的小方塊', 10);
      v.innerHTML = '<div style="display:flex;flex-wrap:wrap;gap:10px;align-items:center"><div style="flex:2;min-width:240px">' + V.svg(g) + '</div><div style="flex:1;min-width:140px;max-width:220px">' + W.svg(h) + '</div></div>';
      var tp = 0.5 * Math.atan2(2 * txy, sx - sy) * 180 / Math.PI;
      inf.innerHTML = '圓心 (σx+σy)/2 = ' + f1(c) + '、半徑 R = ' + f1(R) + ' MPa。主應力 σ₁ = <b>' + f1(c + R) + '</b>、σ₂ = <b>' + f1(c - R) + '</b>（在 θ = ' + f1(tp) + '° 時，剪應力為 0）；最大剪應力 = R = <b>' + f1(R) + '</b>。<br>旋轉 θ 後：σx′ = ' + f1(sxp) + '、τx′y′ = ' + f1(txp) + '——小方塊轉 θ，圓上的點轉 2θ。'; }
    draw(); }

  /* ---------- 梁 ---------- */
  function initBeam(root, cfg) {
    head(root, cfg.q); var type = cfg.s || 'ss', L = 6, P = 20, a = 0.5, w = 5, EI = 20000, bar = el('div'), v = el('div'), inf = info(root); root.insertBefore(bar, inf); root.insertBefore(v, inf);
    [['ss', '簡支梁'], ['cant', '懸臂梁']].forEach(function (x) { var b = btn(x[1], x[0]); b.onclick = function () { type = x[0]; mark(bar, type); draw(); }; bar.appendChild(b); }); mark(bar, type);
    slider(root, '集中載重 P（kN）', 0, 50, 1, P, f0, 'P', function (q) { P = q; draw(); });
    slider(root, 'P 的位置（跨度的比例）', 0.05, 1, 0.05, a, f2, 'a', function (q) { a = q; draw(); });
    slider(root, '均布載重 w（kN/m）', 0, 20, 0.5, w, f1, 'w', function (q) { w = q; draw(); });
    function draw() { var N = 600, dx = L / N, xs = [], Vv = [], Mv = [], xp = a * L, RA, MA = 0;
      if (type === 'ss') { RA = P * (L - xp) / L + w * L / 2; } else { RA = P + w * L; MA = -(P * xp + w * L * L / 2); }
      for (var i = 0; i <= N; i++) { var x = i * dx, Vx = RA - w * x - (x > xp ? P : 0), Mx = MA + RA * x - w * x * x / 2 - (x > xp ? P * (x - xp) : 0); xs.push(x); Vv.push(Vx); Mv.push(Mx); }
      var th = [], y = [], t0 = 0, y0 = 0;
      if (type === 'cant') { th[0] = 0; y[0] = 0; for (i = 1; i <= N; i++) { th[i] = th[i - 1] + (Mv[i] + Mv[i - 1]) / 2 * dx / EI; y[i] = y[i - 1] + (th[i] + th[i - 1]) / 2 * dx; } }
      else { var tt = [0], yy = [0]; for (i = 1; i <= N; i++) { tt[i] = tt[i - 1] + (Mv[i] + Mv[i - 1]) / 2 * dx / EI; yy[i] = yy[i - 1] + (tt[i] + tt[i - 1]) / 2 * dx; } var c1 = -yy[N] / L; for (i = 0; i <= N; i++) { y[i] = yy[i] + c1 * xs[i]; } }
      var Vd = xs.map(function (x, i) { return [x, Vv[i]]; }), Md = xs.map(function (x, i) { return [x, Mv[i]]; }), Yd = xs.map(function (x, i) { return [x, y[i] * 1000]; });
      var Mmax = 0, xm = 0; Mv.forEach(function (m, i) { if (Math.abs(m) > Math.abs(Mmax)) { Mmax = m; xm = xs[i]; } }); var ymax = 0; y.forEach(function (q) { if (Math.abs(q) > Math.abs(ymax)) ymax = q; });
      var Vb = view(640, 90, -0.3, L + 0.3, -1.2, 1.4, 4), g = Vb.l(0, 0, L, 0, '#555', 6);
      if (type === 'ss') g += Vb.poly([[0, 0], [-0.18, -0.9], [0.18, -0.9]], GY, GY, 0.6) + Vb.poly([[L, 0], [L - 0.18, -0.9], [L + 0.18, -0.9]], GY, GY, 0.6); else g += Vb.l(0, -1.1, 0, 1.1, '#555', 5);
      if (P > 0) g += arrow(Vb, xp, 1.3, xp, 0.15, RD, 2.5) + Vb.t(xp + 0.15, 1.05, 'P', 11, RD, 'start');
      if (w > 0) for (var k = 0; k <= 12; k++) g += arrow(Vb, k * L / 12, 0.7, k * L / 12, 0.12, OR, 1);
      v.innerHTML = Vb.svg(g) + chart(640, 150, [{ d: Vd, c: BL, n: '剪力 V（kN）' }], { xl: '' }) + chart(640, 150, [{ d: Md, c: RD, n: '彎矩 M（kN·m）' }], { xl: '' }) + chart(640, 150, [{ d: Yd, c: GR, n: '撓度（mm，EI = 20 MN·m²）' }], { xl: '位置 x（m），跨度 6 m' });
      inf.innerHTML = '支承反力 R = ' + f1(RA) + ' kN' + (type === 'cant' ? '、固定端彎矩 ' + f1(MA) + ' kN·m' : '') + '。最大彎矩 <b>' + f1(Mmax) + ' kN·m</b>（在 x = ' + f2(xm) + ' m），最大撓度 <b>' + f1(Math.abs(ymax) * 1000) + ' mm</b>。<br>觀察：剪力圖的斜率是 −w，彎矩圖的斜率是剪力；剪力為 0 的地方，彎矩最大。'; }
    draw(); }

  /* ---------- 斷面 ---------- */
  function initSection(root, cfg) {
    head(root, cfg.q); var shape = 'rect', A = 6000, M = 50, bar = el('div'), v = el('div'), inf = info(root); root.insertBefore(bar, inf); root.insertBefore(v, inf);
    var SH = [['rect', '扁平放的板'], ['rectv', '立起來的板'], ['square', '正方形'], ['ibeam', 'H 型鋼（工字）'], ['tube', '圓管']];
    SH.forEach(function (x) { var b = btn(x[1], x[0]); b.onclick = function () { shape = x[0]; mark(bar, shape); draw(); }; bar.appendChild(b); }); mark(bar, shape);
    slider(root, '彎矩 M（kN·m）', 5, 200, 1, M, f0, 'M', function (q) { M = q; draw(); });
    function props(s) { // 面積都約 6000 mm²
      if (s === 'rect') return { b: 300, h: 20, I: 300 * Math.pow(20, 3) / 12, c: 10, poly: [[[-150, -10], [150, -10], [150, 10], [-150, 10]]] };
      if (s === 'rectv') return { b: 20, h: 300, I: 20 * Math.pow(300, 3) / 12, c: 150, poly: [[[-10, -150], [10, -150], [10, 150], [-10, 150]]] };
      if (s === 'square') return { b: 77.5, h: 77.5, I: Math.pow(77.46, 4) / 12, c: 38.7, poly: [[[-38.7, -38.7], [38.7, -38.7], [38.7, 38.7], [-38.7, 38.7]]] };
      if (s === 'ibeam') { var B = 150, H = 400, tf = 10, tw = 8, I = B * Math.pow(H, 3) / 12 - (B - tw) * Math.pow(H - 2 * tf, 3) / 12;
        return { b: B, h: H, I: I, c: 200, poly: [[[-75, 190], [75, 190], [75, 200], [-75, 200]], [[-75, -200], [75, -200], [75, -190], [-75, -190]], [[-4, -190], [4, -190], [4, 190], [-4, 190]]] }; }
      var Ro = 160, Ri = Math.sqrt(Ro * Ro - 6000 / Math.PI), pts1 = [], pts2 = [];
      for (var i = 0; i <= 48; i++) { var t = 2 * Math.PI * i / 48; pts1.push([Ro * Math.cos(t), Ro * Math.sin(t)]); }
      return { b: 2 * Ro, h: 2 * Ro, I: Math.PI / 4 * (Math.pow(Ro, 4) - Math.pow(Ri, 4)), c: Ro, ring: [Ro, Ri], poly: [] }; }
    function draw() { var p = props(shape), Vv = view(320, 320, -220, 220, -220, null, 6), g = Vv.l(-215, 0, 215, 0, RD, 1, 'stroke-dasharray="5 4"') + Vv.t(212, 6, '中性軸', 10, RD, 'end');
      p.poly.forEach(function (q) { g += Vv.poly(q, BL, BL, 0.5); });
      if (p.ring) g += '<circle cx="' + Vv.x(0) + '" cy="' + Vv.y(0) + '" r="' + (Vv.x(p.ring[0]) - Vv.x(0)) + '" fill="' + BL + '" fill-opacity="0.5"/><circle cx="' + Vv.x(0) + '" cy="' + Vv.y(0) + '" r="' + (Vv.x(p.ring[1]) - Vv.x(0)) + '" fill="var(--surface)"/>';
      var sig = M * 1e6 * p.c / p.I, rows = '';
      SH.forEach(function (s) { var q = props(s[0]); rows += '<tr' + (s[0] === shape ? ' style="font-weight:bold;background:var(--accent-soft)"' : '') + '><td style="padding:3px 6px">' + s[1] + '</td><td style="text-align:right;font-family:monospace">' + g3(q.I / 1e6) + '</td><td style="text-align:right;font-family:monospace">' + f0(M * 1e6 * q.c / q.I) + '</td></tr>'; });
      v.innerHTML = '<div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center"><div style="flex:1;min-width:200px;max-width:300px">' + Vv.svg(g) + '</div><div style="flex:2;min-width:240px"><table style="width:100%;border-collapse:collapse"><tr><th style="text-align:left">斷面（面積都約 6000 mm²）</th><th>I（×10⁶ mm⁴）</th><th>最大應力 MPa</th></tr>' + rows + '</table></div></div>';
      inf.innerHTML = '同樣的材料用量，最大彎曲應力 σ = Mc/I 差了上百倍。關鍵是把材料放在<b>離中性軸遠的地方</b>：I 和距離的平方成正比。' + (sig > 250 ? '<br><span style="color:' + RD + '">現在的斷面應力 ' + f0(sig) + ' MPa 已經超過一般鋼材的降伏強度 250 MPa。</span>' : ''); }
    draw(); }

  /* ---------- 挫屈 ---------- */
  function initBuckle(root, cfg) {
    head(root, cfg.q); var L = 4, K = 1, v = el('div'), inf = info(root), bar = el('div'); root.insertBefore(bar, inf); root.insertBefore(v, inf);
    var KS = [[1, '兩端鉸接 K = 1'], [2, '一端固定一端自由 K = 2'], [0.7, '一端固定一端鉸接 K ≈ 0.7'], [0.5, '兩端固定 K = 0.5']];
    KS.forEach(function (x) { var b = btn(x[1], x[0]); b.onclick = function () { K = x[0]; mark(bar, K); draw(); }; bar.appendChild(b); }); mark(bar, K);
    slider(root, '柱長 L（m）', 0.5, 12, 0.1, L, f1, 'L', function (q) { L = q; draw(); });
    // H 型鋼 H150×150×7×10：A ≈ 4014 mm²、弱軸 r ≈ 37.5 mm、I_y ≈ 5.63×10⁶ mm⁴
    var E = 200000, A = 4014, r = 37.5, I = 5.63e6, fy = 250;
    function draw() { var lam = K * L * 1000 / r, Pcr = Math.PI * Math.PI * E * I / Math.pow(K * L * 1000, 2) / 1000, Py = fy * A / 1000, d1 = [], d2 = [];
      for (var x = 10; x <= 300; x += 2) { d1.push([x, Math.PI * Math.PI * E / (x * x)]); d2.push([x, fy]); }
      v.innerHTML = chart(640, 240, [{ d: d1, c: BL, n: '歐拉挫屈應力 π²E/λ²' }, { d: d2, c: RD, n: '降伏應力 250 MPa（壓碎）', dash: '5 4' }], { y0: 0, y1: 600, xl: '長細比 λ = KL / r', yl: 'MPa', pts: [{ x: lam, y: Math.min(Pcr * 1000 / A, 600), c: OR, n: 'λ = ' + f0(lam) }] });
      var gov = Pcr < Py ? '<b>挫屈</b>控制（長柱）' : '<b>壓碎（降伏）</b>控制（短柱）';
      inf.innerHTML = 'H150×150 型鋼（A ≈ 4,014 mm²、弱軸迴轉半徑 r ≈ 37.5 mm）：歐拉挫屈載重 P<sub>cr</sub> = π²EI/(KL)² = <b>' + f0(Pcr) + ' kN</b>，降伏壓碎載重 P<sub>y</sub> = f<sub>y</sub>A = ' + f0(Py) + ' kN → ' + gov + '。<br>兩條線交叉的長細比約 ' + f0(Math.PI * Math.sqrt(E / fy)) + '；實際鋼柱在交叉點附近因初始彎曲與殘餘應力，強度比兩條線都低（規範的柱強度曲線處理這段）。'; }
    draw(); }

  /* ---------- 桁架 ---------- */
  function solve(Am, b) { var n = b.length, M = Am.map(function (r, i) { return r.concat([b[i]]); });
    for (var c = 0; c < n; c++) { var p = c; for (var r = c + 1; r < n; r++) if (Math.abs(M[r][c]) > Math.abs(M[p][c])) p = r; var t = M[c]; M[c] = M[p]; M[p] = t;
      if (Math.abs(M[c][c]) < 1e-12) return null; for (r = 0; r < n; r++) if (r !== c) { var f = M[r][c] / M[c][c]; for (var k = c; k <= n; k++) M[r][k] -= f * M[c][k]; } }
    return M.map(function (r, i) { return r[n] / r[i]; }); }
  function initTruss(root, cfg) {
    head(root, cfg.q); var node = 2, P = 100, H = 3, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '載重位置（下弦第幾個節點）', 1, 3, 1, node, function (q) { return '第 ' + q + ' 個'; }, 'n', function (q) { node = q; draw(); });
    slider(root, '載重 P（kN）', 10, 200, 5, P, f0, 'P', function (q) { P = q; draw(); });
    slider(root, '桁架高度（m）', 1, 6, 0.5, H, f1, 'H', function (q) { H = q; draw(); });
    function draw() { var Lp = 4, N = [[0, 0], [4, 0], [8, 0], [12, 0], [16, 0], [4, H], [8, H], [12, H]];
      var Mb = [[0, 1], [1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [0, 5], [1, 5], [2, 6], [3, 7], [4, 7], [1, 6], [3, 6]];
      // 未知數：13 根桿 + 3 個反力（節點 0：Rx、Ry；節點 4：Ry）= 16 = 8 節點 × 2
      var n = 16, Am = [], b = [];
      for (var j = 0; j < 8; j++) { var rx = new Array(n).fill(0), ry = new Array(n).fill(0);
        Mb.forEach(function (m, k) { if (m[0] !== j && m[1] !== j) return; var o = m[0] === j ? m[1] : m[0], dx = N[o][0] - N[j][0], dy = N[o][1] - N[j][1], Lm = Math.hypot(dx, dy); rx[k] = dx / Lm; ry[k] = dy / Lm; });
        if (j === 0) { rx[13] = 1; ry[14] = 1; } if (j === 4) ry[15] = 1;
        Am.push(rx); b.push(0); Am.push(ry); b.push(j === node ? P : 0); }
      var s = solve(Am, b), V = view(640, 260, -1.5, 17.5, -2.2, null, 6), g = '';
      Mb.forEach(function (m, k) { var F = s[k], c = Math.abs(F) < 1e-6 ? GY : F > 0 ? BL : RD, w = 1.5 + Math.min(6, Math.abs(F) / P * 4);
        g += V.l(N[m[0]][0], N[m[0]][1], N[m[1]][0], N[m[1]][1], c, w) + V.t((N[m[0]][0] + N[m[1]][0]) / 2, (N[m[0]][1] + N[m[1]][1]) / 2 + 0.25, f0(F), 10, c); });
      N.forEach(function (p) { g += V.dot(p[0], p[1], '#333', 3.5); });
      g += arrow(V, N[node][0], -2, N[node][0], -0.3, OR, 2.5) + V.t(N[node][0] + 0.3, -1.6, 'P = ' + P + ' kN', 11, OR, 'start');
      g += V.poly([[0, 0], [-0.5, -0.8], [0.5, -0.8]], GY, GY, 0.6) + V.poly([[16, 0], [15.5, -0.8], [16.5, -0.8]], GY, GY, 0.6);
      v.innerHTML = V.svg(g);
      inf.innerHTML = '<span style="color:' + BL + '">藍色：拉力</span>、<span style="color:' + RD + '">紅色：壓力</span>（線愈粗力愈大，數字單位 kN）。支承反力：左 ' + f1(s[14]) + ' kN、右 ' + f1(s[15]) + ' kN。<br>桁架加高，上下弦的力變小（力臂變長）；上弦受壓、下弦受拉，就像一根梁的上下翼板。'; }
    draw(); }

  /* ---------- 載重計算 ---------- */
  function initLoads(root, cfg) {
    head(root, cfg.q); var t = 15, fin = 1.5, part = 1.0, LL = 2.0, nf = 4, trib = 25, bar = el('div'), v = el('div'), inf = info(root);
    root.insertBefore(v, inf);
    slider(root, '樓板厚度（cm）', 10, 25, 1, t, f0, 't', function (q) { t = q; draw(); });
    slider(root, '粉刷、地坪、天花（kN/m²）', 0.5, 3, 0.1, fin, f1, 'f', function (q) { fin = q; draw(); });
    slider(root, '隔間牆等效（kN/m²）', 0, 3, 0.1, part, f1, 'p', function (q) { part = q; draw(); });
    slider(root, '活載重（kN/m²；住宅約 2.0、辦公室約 3.0）', 1, 5, 0.1, LL, f1, 'L', function (q) { LL = q; draw(); });
    slider(root, '柱的受載面積（m²）', 5, 60, 1, trib, f0, 'a', function (q) { trib = q; draw(); });
    slider(root, '柱上方的樓層數', 1, 15, 1, nf, f0, 'n', function (q) { nf = q; draw(); });
    function draw() { var slab = 24 * t / 100, beam = 1.2, Dl = slab + fin + part + beam, w1 = 1.4 * Dl, w2 = 1.2 * Dl + 1.6 * LL, wu = Math.max(w1, w2), PD = Dl * trib * nf, PL = LL * trib * nf, Pu = wu * trib * nf;
      v.innerHTML = '<table style="width:100%;border-collapse:collapse"><tr><td style="padding:3px">樓板自重 24 kN/m³ × ' + t + ' cm</td><td style="text-align:right;font-family:monospace">' + f2(slab) + ' kN/m²</td></tr>' +
        '<tr><td style="padding:3px">梁的自重（攤到樓板，約）</td><td style="text-align:right;font-family:monospace">1.2 kN/m²</td></tr>' +
        '<tr><td style="padding:3px">粉刷、地坪、天花 + 隔間</td><td style="text-align:right;font-family:monospace">' + f2(fin + part) + ' kN/m²</td></tr>' +
        '<tr style="font-weight:bold"><td style="padding:3px">靜載重 D</td><td style="text-align:right;font-family:monospace">' + f2(Dl) + ' kN/m²</td></tr>' +
        '<tr style="font-weight:bold"><td style="padding:3px">活載重 L</td><td style="text-align:right;font-family:monospace">' + f2(LL) + ' kN/m²</td></tr>' +
        '<tr><td style="padding:3px">1.4D</td><td style="text-align:right;font-family:monospace">' + f2(w1) + ' kN/m²</td></tr>' +
        '<tr><td style="padding:3px">1.2D + 1.6L</td><td style="text-align:right;font-family:monospace">' + f2(w2) + ' kN/m²</td></tr>' +
        '<tr><td style="padding:3px">柱軸力（使用狀態 D + L）</td><td style="text-align:right;font-family:monospace">' + f0(PD + PL) + ' kN（約 ' + f1((PD + PL) / 9.81) + ' 公噸）</td></tr>' +
        '<tr style="font-weight:bold"><td style="padding:3px">柱軸力（設計用 U）</td><td style="text-align:right;font-family:monospace">' + f0(Pu) + ' kN</td></tr></table>';
      inf.innerHTML = '靜載重占了 ' + f0(Dl / (Dl + LL) * 100) + '%：一般住宅裡，<b>房子自己的重量遠大於人和家具</b>。設計用的載重組合取 1.4D 與 1.2D + 1.6L 的較大者（這裡只考慮重力；風與地震另外組合）。'; }
    draw(); }

  /* ---------- RC 梁 ---------- */
  function initRcbeam(root, cfg) {
    head(root, cfg.q); var b = 300, d = 540, n = 4, db = 22, fc = 28, fy = 420, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '梁寬 b（mm）', 200, 600, 10, b, f0, 'b', function (q) { b = q; draw(); });
    slider(root, '有效深度 d（mm）', 300, 900, 10, d, f0, 'd', function (q) { d = q; draw(); });
    slider(root, '主筋根數（D22，單根 387 mm²）', 2, 10, 1, n, f0, 'n', function (q) { n = q; draw(); });
    slider(root, '混凝土強度 fc′（MPa）', 21, 42, 1, fc, f0, 'c', function (q) { fc = q; draw(); });
    function draw() { var As = n * 387, b1 = fc <= 28 ? 0.85 : Math.max(0.65, 0.85 - 0.05 * (fc - 28) / 7), a = As * fy / (0.85 * fc * b), c = a / b1, et = 0.003 * (d - c) / c;
      var phi = et >= 0.005 ? 0.9 : et <= 0.002 ? 0.65 : 0.65 + 0.25 * (et - 0.002) / 0.003, Mn = As * fy * (d - a / 2) / 1e6, rho = As / (b * d), rmin = Math.max(0.25 * Math.sqrt(fc) / fy, 1.4 / fy);
      var V = view(620, 240, -50, 570, -40, null, 4), h = d + 60, sc = 180 / h, g = '', ox = 60;
      function Y(z) { return 200 - z * sc; }
      g += '<rect x="' + ox + '" y="' + Y(h) + '" width="' + (b * sc) + '" height="' + (h * sc) + '" fill="' + GY + '" fill-opacity="0.2" stroke="' + GY + '"/>';
      g += '<rect x="' + ox + '" y="' + Y(h) + '" width="' + (b * sc) + '" height="' + (a * sc) + '" fill="' + OR + '" fill-opacity="0.5"/>';
      for (var i = 0; i < Math.min(n, 6); i++) g += '<circle cx="' + (ox + (b * sc) * (i + 0.5) / Math.min(n, 6)) + '" cy="' + Y(h - d) + '" r="' + Math.max(3, 11 * sc) + '" fill="' + BL + '"/>';
      var sx = ox + b * sc + 60; g += ln(sx, Y(h), sx, Y(0), '#555', 1) + ln(sx, Y(h), sx + 60, Y(h), RD, 2) + ln(sx + 60, Y(h), sx - 60 * et / 0.003 * 0.3, Y(h - d), RD, 2) + ln(sx, Y(h - c), sx + 90, Y(h - c), GY, 1, 'stroke-dasharray="4 3"');
      g += tx(sx + 62, Y(h) - 4, 'εc = 0.003', 10, RD, 'start') + tx(sx + 92, Y(h - c) + 4, '中性軸 c = ' + f0(c) + ' mm', 10, GY, 'start') + tx(sx - 4, Y(h - d) + 16, 'εt = ' + (et * 1000).toFixed(1) + '‰', 10, RD, 'end');
      var cx = sx + 210; g += '<rect x="' + cx + '" y="' + Y(h) + '" width="60" height="' + (a * sc) + '" fill="' + OR + '" fill-opacity="0.5"/>' + tx(cx + 66, Y(h - a / 2) + 4, 'C = 0.85fc′ab', 10, OR, 'start') + ln(cx + 30, Y(h - d), cx + 84, Y(h - d), BL, 2) + '<polygon points="' + (cx + 90) + ',' + Y(h - d) + ' ' + (cx + 82) + ',' + (Y(h - d) - 4) + ' ' + (cx + 82) + ',' + (Y(h - d) + 4) + '" fill="' + BL + '"/>' + tx(cx + 96, Y(h - d) + 4, 'T = As·fy', 10, BL, 'start');
      v.innerHTML = svgw('0 0 620 230', g);
      inf.innerHTML = 'A<sub>s</sub> = ' + f0(As) + ' mm²（鋼筋比 ' + (rho * 100).toFixed(2) + '%，最小 ' + (rmin * 100).toFixed(2) + '%）。壓力區深度 a = A<sub>s</sub>f<sub>y</sub>/(0.85fc′b) = <b>' + f0(a) + ' mm</b>。<br>' +
        '標稱彎矩強度 M<sub>n</sub> = A<sub>s</sub>f<sub>y</sub>(d − a/2) = <b>' + f1(Mn) + ' kN·m</b>；拉力筋應變 ' + (et * 1000).toFixed(1) + '‰ → φ = ' + phi.toFixed(2) + '，設計強度 φM<sub>n</sub> = <b>' + f1(phi * Mn) + ' kN·m</b>。' +
        (et < 0.005 ? '<br><span style="color:' + RD + '">鋼筋太多：拉力筋還沒充分降伏混凝土就先壓碎（脆性破壞），規範用較小的 φ 懲罰這種設計。</span>' : '<br>拉力控制：鋼筋會先降伏、梁會先大幅變形，破壞前有明顯警訊。') + (rho < rmin ? '<br><span style="color:' + RD + '">低於最小鋼筋量。</span>' : ''); }
    draw(); }

  /* ---------- 平方立方定律 ---------- */
  function initScale(root, cfg) {
    head(root, cfg.q); var s = 1, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '放大倍數 λ', 1, 20, 0.1, s, f1, 's', function (q) { s = q; draw(); });
    function draw() { var d1 = [], d2 = [], d3 = []; for (var x = 1; x <= 20; x += 0.1) { d1.push([x, x * x * x]); d2.push([x, x * x]); d3.push([x, x]); }
      v.innerHTML = chart(640, 230, [{ d: d1, c: RD, n: '重量 ∝ λ³' }, { d: d2, c: BL, n: '截面積（強度）∝ λ²' }, { d: d3, c: OR, n: '應力 = 重量/面積 ∝ λ', dash: '5 4' }], { y0: 0, y1: 400, xl: '放大倍數 λ', pts: [{ x: s, y: Math.min(s * s * s, 400), c: RD, n: f0(s * s * s) + ' 倍重' }] });
      inf.innerHTML = '每個尺寸都放大 ' + f1(s) + ' 倍：重量變 <b>' + f0(s * s * s) + '</b> 倍，柱子的截面積只變 <b>' + f0(s * s) + '</b> 倍，所以柱子裡的應力變 <b>' + f1(s) + '</b> 倍。' +
        '<br>只靠自重：混凝土柱（fc′ = 28 MPa、24 kN/m³）最高約 ' + f0(28e6 / 24000) + ' m 就會壓碎自己；鋼柱（250 MPa、77 kN/m³）約 ' + f0(250e6 / 77000) + ' m。'; }
    draw(); }

  /* ---------- 地震力 ---------- */
  function initSeismic(root, cfg) {
    head(root, cfg.q); var hn = 14, SDS = 0.6, SD1 = 0.35, I = 1.0, R = 4.8, ay = 1.0, W = 4000, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '建築物高度 hₙ（m）', 3, 100, 1, hn, f0, 'h', function (q) { hn = q; draw(); });
    slider(root, '短週期設計譜加速度 S_DS（依工址，示意）', 0.3, 1.0, 0.05, SDS, f2, 'S', function (q) { SDS = q; draw(); });
    slider(root, '一秒週期設計譜加速度 S_D1（示意）', 0.15, 0.8, 0.05, SD1, f2, 'S1', function (q) { SD1 = q; draw(); });
    slider(root, '用途係數 I（一般 1.0、公眾 1.25、重要 1.5）', 1, 1.5, 0.25, I, f2, 'I', function (q) { I = q; draw(); });
    slider(root, '韌性容量 R（RC 韌性剛構約 4.8）', 1, 6, 0.1, R, f1, 'R', function (q) { R = q; draw(); });
    slider(root, '建築物總重 W（kN）', 500, 50000, 100, W, f0, 'W', function (q) { W = q; draw(); });
    function draw() { var T = 0.07 * Math.pow(hn, 0.75), T0 = SD1 / SDS, Sa = T <= 0.2 * T0 ? SDS * (0.4 + 3 * T / T0) : T <= T0 ? SDS : T <= 2.5 * T0 ? SD1 / T : 0.4 * SDS;
      var Ra = 1 + (R - 1) / 1.5, Fu = T >= T0 ? Ra : T >= 0.6 * T0 ? Math.sqrt(2 * Ra - 1) + (Ra - Math.sqrt(2 * Ra - 1)) * (T - 0.6 * T0) / (0.4 * T0) : T >= 0.2 * T0 ? Math.sqrt(2 * Ra - 1) : Math.sqrt(2 * Ra - 1) + (1 - Math.sqrt(2 * Ra - 1)) * (0.2 * T0 - T) / (0.2 * T0);
      var c = Sa * I / (1.4 * ay * Fu), d = []; for (var t = 0.02; t <= 3; t += 0.02) { var s = t <= 0.2 * T0 ? SDS * (0.4 + 3 * t / T0) : t <= T0 ? SDS : t <= 2.5 * T0 ? SD1 / t : 0.4 * SDS; d.push([t, s]); }
      v.innerHTML = chart(640, 220, [{ d: d, c: BL, n: '設計譜加速度係數 S_aD（示意）' }], { y0: 0, y1: 1.1, xl: '週期 T（秒）', pts: [{ x: T, y: Sa, c: OR, n: 'T = ' + f2(T) + ' s' }] });
      inf.innerHTML = '經驗週期 T = 0.07 hₙ<sup>3/4</sup> = <b>' + f2(T) + ' s</b>（RC 抗彎矩構架），S<sub>aD</sub> = ' + f2(Sa) + '，結構系統地震力折減係數 F<sub>u</sub> ≈ ' + f2(Fu) + '。<br>V = S<sub>aD</sub>·I / (1.4 α<sub>y</sub> F<sub>u</sub>) × W = <b>' + (c * 100).toFixed(1) + '% W = ' + f0(c * W) + ' kN</b>。' +
        '<br><span style="color:var(--text-muted)">教學簡化：規範另有 V*、V<sub>M</sub> 等檢核取大值，以及最小值、近斷層、用途等條件；α<sub>y</sub> 這裡取 1.0。</span>'; }
    draw(); }

  /* ---------- 威布爾 ---------- */
  function initWeibull(root, cfg) {
    head(root, cfg.q); var m = 10, r = 100, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '威布爾模數 m（愈大愈均勻；陶瓷 5–15、鋼 > 30）', 2, 40, 1, m, f0, 'm', function (q) { m = q; draw(); });
    slider(root, '體積放大倍數（對數）', 0, 6, 0.1, 2, function (q) { return Math.pow(10, q).toPrecision(3) + ' 倍'; }, 'r', function (q) { r = Math.pow(10, q); draw(); });
    function draw() { var d1 = [], d2 = [];
      for (var s = 0; s <= 1.6; s += 0.01) { d1.push([s, 1 - Math.exp(-Math.pow(s, m))]); d2.push([s, 1 - Math.exp(-r * Math.pow(s, m))]); }
      var ratio = Math.pow(1 / r, 1 / m);
      v.innerHTML = chart(640, 230, [{ d: d1, c: BL, n: '小試體：破壞機率' }, { d: d2, c: RD, n: '大構件（體積 × ' + r.toPrecision(3) + '）' }], { y0: 0, y1: 1.05, xl: '應力 / 小試體的特徵強度' });
      inf.innerHTML = '最弱環節理論：體積愈大，含有大裂縫的機會愈高。特徵強度變成小試體的 (1/' + r.toPrecision(3) + ')<sup>1/' + m + '</sup> = <b>' + (ratio * 100).toFixed(1) + '%</b>。<br>m 小（材料不均勻，如混凝土抗拉、陶瓷），尺寸效應明顯；m 大（鋼），幾乎沒有尺寸效應。'; }
    draw(); }

  /* ---------- 動力放大 ---------- */
  function initDaf(root, cfg) {
    head(root, cfg.q); var z = 0.05, r = 1, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '阻尼比 ζ（RC 建築約 5%）', 0.005, 0.5, 0.005, z, function (q) { return (q * 100).toFixed(1) + '%'; }, 'z', function (q) { z = q; draw(); });
    slider(root, '外力頻率 / 結構自然頻率', 0.1, 3, 0.01, r, f2, 'r', function (q) { r = q; draw(); });
    function D(x) { return 1 / Math.sqrt(Math.pow(1 - x * x, 2) + Math.pow(2 * z * x, 2)); }
    function draw() { var d = []; for (var x = 0.05; x <= 3; x += 0.01) d.push([x, D(x)]);
      v.innerHTML = chart(640, 230, [{ d: d, c: BL, n: '動力放大係數' }], { y0: 0, y1: Math.min(60, 1 / (2 * z) * 1.15 + 1), xl: '頻率比 ω / ωₙ', pts: [{ x: r, y: D(r), c: OR, n: f2(D(r)) + ' 倍' }] });
      inf.innerHTML = '同樣大小的外力，反覆推的頻率接近結構的自然頻率時，振幅放大 <b>' + f1(D(r)) + '</b> 倍（共振時約 1/(2ζ) = ' + f1(1 / (2 * z)) + ' 倍）。增加阻尼（例如調諧質量阻尼器）就是在壓低這個尖峰。'; }
    draw(); }

  var INIT = { lj: initLj, ss: initSs, mohr: initMohr, beam: initBeam, section: initSection, buckle: initBuckle, truss: initTruss, loads: initLoads, rcbeam: initRcbeam, scale: initScale, seismic: initSeismic, weibull: initWeibull, daf: initDaf };
  function boot() { document.querySelectorAll('.sm-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🏗️", note=SM_NOTE):
    return make_with(icon, note, [("sm-w", SMLIB)])
