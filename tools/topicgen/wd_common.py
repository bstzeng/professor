# -*- coding: utf-8 -*-
"""〈曲速引擎的詳細計算〉（wd_）共用：課程包裝與 WDLIB 互動元件。

逐步推導（steps）與數值驗證（check）沿用 md_common 的 MDLIB；本檔的 WDLIB（class="wd-w"）提供：
  rocket   火箭方程式（古典與相對論）       stiff    時空的剛性：曲率半徑 ↔ 需要的密度
  shape    形狀函數 f(r) 與 f′(r)            field    泡周圍的膨脹率 θ／能量密度 ρ 熱圖
  energy   曲速泡總能量計算器                casimir  卡西米爾效應計算器
  qi       量子不等式：負能量與持續時間       horizon  超光速時泡內光訊號的速度與視界
  ladder   能量階梯（數量級比較）
"""
from md_common import make_with, S, steps, check, mw, star, MDLIB
from cc_common import wdg, LS, XL, M, D, KATEX
from qt_common import BASEJS

WD_NOTE = (u"本課程的計算採用文獻中的標準模型與教學用的近似（例如薄壁近似），數量級可靠、係數依定義不同會有幾倍差異；"
           u"曲速引擎目前只是廣義相對論方程式的解，沒有任何實驗證據顯示它能被建造。")


def wv(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("wd-w", cfg)


WDLIB = r"""
(function () {
  if (window.__wdLib) return; window.__wdLib = 1;
""" + BASEJS + r"""
  var _sl = slider; slider = function (root, lab, min, max, step, val, fmt, k, cb) { var u = _sl(root, lab, min, max, step, val, fmt, k, cb); var b = root.lastChild && root.lastChild.querySelector('b'); if (b) b.textContent = fmt(val); return u; };
  var c = 2.99792458e8, G = 6.674e-11, hb = 1.054571817e-34, LP = 1.616e-35;
  var BL = '#3a6ea5', OR = '#e07a2f', GR = '#4caf50', RD = '#e0605a', PU = '#8e5bd1';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function sci(v, d) { if (v === Infinity) return '超過 10<sup>308</sup>（計算機的上限）'; if (!isFinite(v)) return '—'; if (v === 0) return '0'; var e = Math.floor(Math.log10(Math.abs(v))), m = v / Math.pow(10, e);
    if (e >= -3 && e <= 5) return (Math.round(v * 1000) / 1000).toLocaleString(); return m.toFixed(d === undefined ? 2 : d) + ' × 10<sup>' + e + '</sup>'; }
  function sciT(v) { var e = Math.floor(Math.log10(Math.abs(v))); if (e >= -3 && e <= 5) return (Math.round(v * 1000) / 1000).toLocaleString(); var m = v / Math.pow(10, e), S = '⁰¹²³⁴⁵⁶⁷⁸⁹';
    return m.toFixed(2) + ' × 10' + String(e).replace('-', '⁻').replace(/[0-9]/g, function (d) { return S[+d]; }); }
  function f(r, R, s) { return (Math.tanh(s * (r + R)) - Math.tanh(s * (r - R))) / (2 * Math.tanh(s * R)); }
  function fp(r, R, s) { var a = 1 / Math.cosh(s * (r + R)), b = 1 / Math.cosh(s * (r - R)); return s * (a * a - b * b) / (2 * Math.tanh(s * R)); }
  var REF = [['全世界一年用電與燃料（約 6 × 10²⁰ J）', 6e20], ['沙皇炸彈（約 2.1 × 10¹⁷ J）', 2.1e17], ['太陽一秒鐘的輸出（3.8 × 10²⁶ J）', 3.8e26],
    ['木星的靜止能量 Mc²', 1.898e27 * c * c], ['太陽的靜止能量 Mc²', 1.989e30 * c * c], ['銀河系（含暗物質，約 1.5 × 10⁴² kg）', 1.5e42 * c * c], ['可觀測宇宙的一般物質（約 10⁵³ kg）', 1.5e53 * c * c]];
  function compare(E) { var a = Math.abs(E), best = null; REF.forEach(function (r) { if (a >= r[1] * 0.3) best = r; });
    return best ? '約為「' + best[0] + '」的 <b>' + sci(a / best[1]) + '</b> 倍' : '比全世界一年的能源用量還小'; }

  /* ---------- 火箭方程式 ---------- */
  function initRocket(root, cfg) {
    head(root, cfg.q); var lb = -1, ve = 1, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    var V = [['化學火箭', 4500], ['核分裂（熱核火箭）', 9000], ['核融合（理想）', 0.04 * c], ['物質–反物質（理想光子火箭）', c]], bar = el('div'); root.insertBefore(bar, v);
    V.forEach(function (x, i) { var b = btn(x[0], i); b.onclick = function () { ve = i; mark(bar, i); draw(); }; bar.appendChild(b); }); mark(bar, ve);
    slider(root, '目標速度 v / c（對數刻度）', -3, -0.0004, 0.01, lb, function (q) { return Math.pow(10, q).toPrecision(3); }, 'b', function (q) { lb = q; draw(); });
    function draw() { var b = Math.pow(10, lb), u = V[ve][1], cl = Math.exp(b * c / u), rel = Math.pow((1 + b) / (1 - b), c / (2 * u));
      var gam = 1 / Math.sqrt(1 - b * b), yrs = 4.37 / b, ship = yrs / gam;
      v.innerHTML = '<table style="width:100%;border-collapse:collapse;margin-top:8px">' +
        '<tr><td style="padding:4px">排氣速度</td><td style="text-align:right;font-family:monospace">' + sci(u) + ' m/s（' + (u / c).toPrecision(3) + ' c）</td></tr>' +
        '<tr><td style="padding:4px">古典質量比 e<sup>Δv/u</sup></td><td style="text-align:right;font-family:monospace">' + sci(cl) + '</td></tr>' +
        '<tr><td style="padding:4px">相對論質量比 [(1+β)/(1−β)]<sup>c/2u</sup></td><td style="text-align:right;font-family:monospace"><b>' + sci(rel) + '</b></td></tr>' +
        '<tr><td style="padding:4px">到半人馬座 α（4.37 光年），地球上看</td><td style="text-align:right;font-family:monospace">' + sci(yrs) + ' 年</td></tr>' +
        '<tr><td style="padding:4px">船上的人經過的時間</td><td style="text-align:right;font-family:monospace">' + sci(ship) + ' 年</td></tr></table>';
      inf.innerHTML = '質量比是「出發時總質量 ÷ 酬載」。這裡只算加速；要在目的地停下來，質量比還要再平方。' + (rel > 1e6 ? '<br>質量比超過一百萬：幾乎整艘船都是燃料。' : ''); }
    draw(); }

  /* ---------- 時空的剛性 ---------- */
  function initStiff(root, cfg) {
    head(root, cfg.q); var L = 2, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '想要的曲率半徑（對數，公尺）', -3, 12, 0.05, L, function (q) { return sciT(Math.pow(10, q)) + ' m'; }, 'L', function (q) { L = q; draw(); });
    var M = [['水', 1000], ['鉛', 11340], ['太陽核心', 1.5e5], ['白矮星', 1e9], ['原子核（中子星）', 2.3e17]];
    function draw() { var Lm = Math.pow(10, L), rho = c * c / (8 * Math.PI * G * Lm * Lm), rows = '';
      M.forEach(function (m) { rows += '<tr><td style="padding:3px 6px">' + m[0] + '</td><td style="text-align:right;font-family:monospace">' + sci(m[1]) + '</td><td style="text-align:right;font-family:monospace">' + (rho / m[1] > 1 ? '需要 ' + sci(rho / m[1]) + ' 倍' : '<span style="color:' + GR + '">足夠</span>') + '</td></tr>'; });
      v.innerHTML = '<p style="margin:6px 0">需要的質量密度 ρ ≈ c²/(8πG L²) = <b>' + sci(rho) + ' kg/m³</b></p><table style="width:100%;border-collapse:collapse"><tr><th style="text-align:left">物質</th><th>密度 kg/m³</th><th>夠不夠</th></tr>' + rows + '</table>';
      inf.innerHTML = '要讓時空在 ' + sci(Lm) + ' 公尺的尺度上明顯彎曲，所需的密度' + (rho > 2.3e17 ? '比原子核還高——地球上沒有任何東西做得到。' : rho > 1000 ? '超過一般物質。' : '連水都綽綽有餘（所以地球、太陽這種大尺度才看得到重力）。'); }
    draw(); }

  /* ---------- 形狀函數 ---------- */
  function initShape(root, cfg) {
    head(root, cfg.q); var R = 1, s = 8, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '泡的半徑 R', 0.5, 2, 0.05, R, f2, 'R', function (q) { R = q; draw(); });
    slider(root, '陡度 σ（愈大壁愈薄）', 1, 40, 0.5, s, f1, 's', function (q) { s = q; draw(); });
    function draw() { var d1 = [], d2 = [], mx = 0;
      for (var r = 0; r <= 3.001; r += 0.005) { d1.push([r, f(r, R, s)]); var q = fp(r, R, s); d2.push([r, q]); mx = Math.max(mx, Math.abs(q)); }
      d2 = d2.map(function (p) { return [p[0], p[1] / mx]; });
      v.innerHTML = chart(640, 240, [{ d: d1, c: BL, n: 'f(r)' }, { d: d2, c: OR, n: 'f′(r)（縮放到 −1）', dash: '5 4' }], { y0: -1.1, y1: 1.15, xl: '離泡中心的距離 r' });
      inf.innerHTML = '泡內 f ≈ 1（跟著泡走）、泡外 f ≈ 0（不受影響），只在 r ≈ R 的薄壁上變化。壁厚約 2/σ = <b>' + f2(2 / s) + '</b>；f′ 的峰值約 σ/2 = ' + f2(s / 2) + '，能量密度正比於 (f′)²，所以全部集中在壁上。'; }
    draw(); }

  /* ---------- 膨脹率／能量密度熱圖 ---------- */
  function initField(root, cfg) {
    head(root, cfg.q); var mode = cfg.m || 'theta', s = 6, R = 1, bar = el('div'), cv = document.createElement('canvas'), inf = info(root);
    root.insertBefore(bar, inf); cv.width = 480; cv.height = 300; cv.style.cssText = 'width:100%;max-width:560px;display:block;margin:6px auto;border-radius:6px'; root.insertBefore(cv, inf);
    [['theta', '體積膨脹率 θ'], ['rho', '能量密度 ρ']].forEach(function (x) { var b = btn(x[1], x[0]); b.onclick = function () { mode = x[0]; mark(bar, mode); draw(); }; bar.appendChild(b); }); mark(bar, mode);
    slider(root, '陡度 σ', 2, 20, 0.5, s, f1, 's', function (q) { s = q; draw(); });
    function draw() { var ctx = cv.getContext('2d'), W = cv.width, H = cv.height, img = ctx.createImageData(W, H), vals = [], mx = 0, X = 2.4, Y = X * H / W;
      for (var j = 0; j < H; j++) for (var i = 0; i < W; i++) { var x = -X + 2 * X * i / W, y = Y - 2 * Y * j / H, r = Math.sqrt(x * x + y * y) || 1e-9, d = fp(r, R, s), val;
        val = mode === 'theta' ? (x / r) * d : -(y * y) / (r * r) * d * d; vals.push(val); mx = Math.max(mx, Math.abs(val)); }
      for (var k = 0; k < vals.length; k++) { var t = vals[k] / (mx || 1), p = 4 * k, a = Math.min(1, Math.abs(t));
        var col = t >= 0 ? [224, 96, 90] : [58, 110, 165]; img.data[p] = Math.round(255 - (255 - col[0]) * a); img.data[p + 1] = Math.round(255 - (255 - col[1]) * a); img.data[p + 2] = Math.round(255 - (255 - col[2]) * a); img.data[p + 3] = 255; }
      ctx.putImageData(img, 0, 0); ctx.fillStyle = '#222'; ctx.font = '13px sans-serif'; ctx.fillText('→ 前進方向 x', W - 100, H - 10); ctx.fillText('ρ = √(y² + z²)', 6, 16);
      ctx.beginPath(); ctx.arc(W / 2, H / 2, 3, 0, 7); ctx.fill();
      inf.innerHTML = mode === 'theta' ? '<span style="color:' + BL + '">藍</span>：θ < 0，空間收縮（前方）；<span style="color:' + RD + '">紅</span>：θ > 0，空間擴張（後方）。θ = v·(x/r)·f′(r)，泡內與泡外都是 0。' :
        '能量密度 ρ ∝ −(y² + z²)/r² · (f′)²：處處 ≤ 0（藍色），集中在壁上、而且是<b>繞著前進方向的環</b>——正前方與正後方（y = z = 0）反而是 0。'; }
    draw(); }

  /* ---------- 總能量計算器 ---------- */
  function initEnergy(root, cfg) {
    head(root, cfg.q); var lR = 2, lD = cfg.d === undefined ? 0 : cfg.d, b = 1, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '泡的半徑 R（對數，公尺）', -1, 4, 0.05, lR, function (q) { return sciT(Math.pow(10, q)) + ' m'; }, 'R', function (q) { lR = q; draw(); });
    slider(root, '壁厚 Δ（對數，公尺；−32.8 是 100 倍普朗克長度）', -32.8, 1, 0.1, lD, function (q) { return sciT(Math.pow(10, q)) + ' m'; }, 'D', function (q) { lD = q; draw(); });
    slider(root, '速度 v / c', 0.01, 10, 0.01, b, f2, 'v', function (q) { b = q; draw(); });
    function draw() { var R = Math.pow(10, lR), Dl = Math.pow(10, lD), E = -Math.pow(c, 4) / G * b * b * R * R / (18 * Dl), m = E / (c * c);
      var thin = R / Dl > 5;
      v.innerHTML = '<table style="width:100%;border-collapse:collapse;margin-top:6px"><tr><td style="padding:4px">總能量 E ≈ −(c⁴/G)·β²R²/(18Δ)</td><td style="text-align:right;font-family:monospace"><b>' + sci(E) + ' J</b></td></tr>' +
        '<tr><td style="padding:4px">換成質量 E/c²</td><td style="text-align:right;font-family:monospace">' + sci(m) + ' kg</td></tr>' +
        '<tr><td style="padding:4px">太陽質量的幾倍</td><td style="text-align:right;font-family:monospace">' + sci(Math.abs(m) / 1.989e30) + '</td></tr></table>';
      inf.innerHTML = '負能量的總量' + compare(E) + '。' + (thin ? '' : '<br><span style="color:' + RD + '">注意：壁厚已經和半徑差不多，薄壁近似不再準確。</span>') +
        '<br>R 加倍 → 能量 ×4；壁厚減半 → 能量 ×2；速度加倍 → 能量 ×4。'; }
    draw(); }

  /* ---------- 卡西米爾 ---------- */
  function initCasimir(root, cfg) {
    head(root, cfg.q); var la = -6, lA = 0, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '兩板間距 a（對數，公尺）', -9, -4, 0.05, la, function (q) { return sciT(Math.pow(10, q)) + ' m'; }, 'a', function (q) { la = q; draw(); });
    slider(root, '板面積 A（對數，平方公尺）', -8, 6, 0.1, lA, function (q) { return sciT(Math.pow(10, q)) + ' m²'; }, 'A', function (q) { lA = q; draw(); });
    function draw() { var a = Math.pow(10, la), A = Math.pow(10, lA), k = Math.PI * Math.PI * hb * c, E = -k * A / (720 * a * a * a), P = -k / (240 * Math.pow(a, 4)), u = E / (A * a);
      v.innerHTML = '<table style="width:100%;border-collapse:collapse;margin-top:6px"><tr><td style="padding:4px">能量 E = −π²ħcA/(720a³)</td><td style="text-align:right;font-family:monospace"><b>' + sci(E) + ' J</b></td></tr>' +
        '<tr><td style="padding:4px">負能量密度 E/(Aa)</td><td style="text-align:right;font-family:monospace">' + sci(u) + ' J/m³</td></tr>' +
        '<tr><td style="padding:4px">吸引壓力 π²ħc/(240a⁴)</td><td style="text-align:right;font-family:monospace">' + sci(-P) + ' Pa</td></tr>' +
        '<tr><td style="padding:4px">換成質量 |E|/c²</td><td style="text-align:right;font-family:monospace">' + sci(-E / (c * c)) + ' kg</td></tr></table>';
      inf.innerHTML = '把間距縮小 10 倍，能量密度變大 10⁴ 倍；但就算間距只有 1 奈米（幾個原子寬），負能量密度也只有約 ' + sci(Math.PI * Math.PI * hb * c / 720 / 1e-36) + ' J/m³。曲速泡壁（R = 100 m、Δ = 1 m、v = c）需要約 10⁴² J/m³。'; }
    draw(); }

  /* ---------- 量子不等式 ---------- */
  function initQi(root, cfg) {
    head(root, cfg.q); var lt = -15, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '負能量要維持的時間 t₀（對數，秒）', -40, 0, 0.1, lt, function (q) { return sciT(Math.pow(10, q)) + ' s'; }, 't', function (q) { lt = q; draw(); });
    function bound(t) { return 3 * hb / (32 * Math.PI * Math.PI * Math.pow(c, 3) * Math.pow(t, 4)); }
    function draw() { var d = []; for (var x = -40; x <= 0.001; x += 0.5) d.push([x, Math.log10(bound(Math.pow(10, x)))]);
      var t = Math.pow(10, lt), B = bound(t);
      v.innerHTML = chart(640, 230, [{ d: d, c: BL, n: 'log₁₀ 允許的最大負能量密度（J/m³）' }], { xl: 'log₁₀ t₀（秒）', pts: [{ x: lt, y: Math.log10(B), c: OR, n: sci(B) }] });
      inf.innerHTML = '無質量純量場的福特–羅曼不等式：平均負能量密度不能低於 −3ħ/(32π²c³t₀⁴)。想維持 ' + sci(t) + ' 秒，負能量密度最多約 <b>' + sci(B) + ' J/m³</b>。時間拉長 10 倍，允許的負能量小 10⁴ 倍。'; }
    draw(); }

  /* ---------- 視界 ---------- */
  function initHorizon(root, cfg) {
    head(root, cfg.q); var b = 2, s = 4, R = 1, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '泡的速度 v / c', 0.2, 4, 0.05, b, f2, 'v', function (q) { b = q; draw(); });
    function draw() { var d = [], hz = null;
      for (var x = 0; x <= 2.5; x += 0.005) { var w = b * (f(x, R, s) - 1) + 1; d.push([x, w]); if (hz === null && w <= 0) hz = x; }
      v.innerHTML = chart(640, 230, [{ d: d, c: BL, n: '往前打的光相對於泡中心的速度（單位 c）' }], { y0: Math.min(-0.2, 1 - b), y1: 1.3, xl: '離泡中心往前的距離（R = 1）', hl: [{ y: 0, c: RD, n: '速度 0：光停住了' }], vl: hz === null ? [] : [{ x: hz, c: OR, n: '視界' }] });
      inf.innerHTML = '光的座標速度是 v·f + c，相對於泡中心是 c − v(1 − f)。' + (b > 1 ? '速度超過光速時，在泡壁裡 f = 1 − c/v = ' + f2(1 - 1 / b) + ' 的地方，往前的光速降到 0：<b>船上發出的任何訊號都到不了前方的泡壁</b>，船員無法控制或關閉前緣。' : '速度低於光速時，光總是能往前跑到泡外，沒有視界。'); }
    draw(); }

  /* ---------- 能量階梯 ---------- */
  function initLadder(root, cfg) {
    head(root, cfg.q); var v = el('div'), inf = info(root); root.insertBefore(v, inf);
    var L = [['卡西米爾：1 m² 板、間距 1 μm', 4.3e-10, GR], ['全世界一年的能源', 6e20, GR], ['太陽一秒的輸出', 3.8e26, GR], ['木星 Mc²', 1.7e44, GR],
      ['太陽 Mc²', 1.79e47, GR], ['Van Den Broeck 版（數個太陽質量）', 5e47, OR], ['R=100 m、Δ=1 m、v=c 的阿庫別瑞泡', 6.7e46, OR],
      ['銀河系 Mc²', 1.35e59, GR], ['可觀測宇宙一般物質 Mc²', 1.35e70, GR], ['Pfenning–Ford：R=100 m、Δ≈100 普朗克長度', 5.6e79, RD]];
    L.sort(function (a, b) { return a[1] - b[1]; });
    var W = 640, H = 28 * L.length + 30, x0 = 250, g = '';
    L.forEach(function (r, i) { var y = 18 + i * 28, w = (Math.log10(r[1]) + 10) / 92 * (W - x0 - 20);
      g += tx(x0 - 6, y + 14, r[0], 11, 'currentColor', 'end') + '<rect x="' + x0 + '" y="' + (y + 3) + '" width="' + n1(Math.max(2, w)) + '" height="16" rx="3" fill="' + r[2] + '" fill-opacity="0.6"/>' + tx(x0 + w + 4, y + 15, '10^' + Math.round(Math.log10(r[1])) + ' J', 10, 'var(--text-muted)', 'start'); });
    v.innerHTML = '<div style="overflow-x:auto"><div style="min-width:560px">' + svgw('0 0 ' + W + ' ' + H, g) + '</div></div>';
    inf.innerHTML = '長條長度是能量的<b>對數</b>：每多一格就是 10 倍。紅、橘是曲速需要的負能量，綠是參考值。最上和最下差了大約 90 個數量級。'; }

  var INIT = { rocket: initRocket, stiff: initStiff, shape: initShape, field: initField, energy: initEnergy, casimir: initCasimir, qi: initQi, horizon: initHorizon, ladder: initLadder };
  function boot() { document.querySelectorAll('.wd-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🚀", note=WD_NOTE):
    return make_with(icon, note, [("wd-w", WDLIB)])
