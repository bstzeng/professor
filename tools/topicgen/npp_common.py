# -*- coding: utf-8 -*-
"""〈現代核電廠設計〉（npp_）共用：課程包裝與 NPLIB 互動元件。

逐步推導（steps）與數值驗證（check）沿用 md_common 的 MDLIB；本檔的 NPLIB（class="np-w"）提供：
  layout   壓水式核電廠配置圖（點元件看說明）   chain    連鎖反應：k 值、世代時間與緩發中子
  kin      點動態：反應度插入與溫度回饋           rod      控制棒積分／微分價值（S 曲線）
  xenon    氙毒：降載或停機後的碘坑               decay    衰變熱曲線與沸騰掉的水量
  chan     熱通道：冷卻水、被覆管、燃料中心溫度   natcirc  自然循環流量
  eff      熱效率：卡諾、Curzon–Ahlborn 與實際電廠  did      縱深防禦五層與多重屏障
  pra      事件樹：冗餘、共因失效與爐心損壞頻率   lcoe     均化發電成本試算
"""
from md_common import make_with, S, steps, check, mw, star, MDLIB
from cc_common import wdg, LS, XL, M, D, KATEX
from qt_common import BASEJS

NP_NOTE = (u"本課程介紹核電廠設計的原理與工程概念，數字為公開文獻中的代表值或教學用的簡化模型，"
           u"不是任何實際電廠的設計規範或安全分析。")


def nv(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("np-w", cfg)


NPLIB = r"""
(function () {
  if (window.__npLib) return; window.__npLib = 1;
""" + BASEJS + r"""
  var _sl = slider; slider = function (root, lab, min, max, step, val, fmt, k, cb) { var u = _sl(root, lab, min, max, step, val, fmt, k, cb); var b = root.lastChild && root.lastChild.querySelector('b'); if (b) b.textContent = fmt(val); return u; };
  var BL = '#3a6ea5', OR = '#e07a2f', GR = '#4caf50', RD = '#e0605a', PU = '#8e5bd1', GY = '#7a8590', GD = '#c9a227';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function sci(v, d) { if (!isFinite(v)) return '—'; if (v === 0) return '0'; var e = Math.floor(Math.log10(Math.abs(v))), m = v / Math.pow(10, e);
    if (e >= -2 && e <= 5) return (Math.round(v * 1000) / 1000).toLocaleString(); return m.toFixed(d === undefined ? 2 : d) + ' × 10<sup>' + e + '</sup>'; }
  function sup(e) { var S = '⁰¹²³⁴⁵⁶⁷⁸⁹'; return String(e).replace('-', '⁻').replace(/[0-9]/g, function (d) { return S[+d]; }); }
  function pct(v) { return (v * 100 >= 10 ? f1(v * 100) : (Math.round(v * 10000) / 100).toString()) + '%'; }
  function table(rows, headr) { var h = '<table style="width:100%;border-collapse:collapse;margin-top:8px;font-size:0.92em">';
    if (headr) h += '<tr>' + headr.map(function (c) { return '<th style="text-align:left;padding:3px 6px;border-bottom:1px solid var(--border)">' + c + '</th>'; }).join('') + '</tr>';
    rows.forEach(function (r) { h += '<tr>' + r.map(function (c, i) { return '<td style="padding:3px 6px;border-bottom:1px solid var(--border);' + (i ? 'text-align:right;font-family:ui-monospace,monospace' : '') + '">' + c + '</td>'; }).join('') + '</tr>'; });
    return h + '</table>'; }
  var BETA = 0.0065, LAMB = 0.08;

  /* ---------- 電廠配置圖 ---------- */
  var PARTS = {
    rpv: ['反應爐壓力槽', '裝著爐心的厚鋼槽（壁厚約 20～25 公分），一次側冷卻水在 15.5 MPa 下流過燃料，從約 290 °C 加熱到約 325 °C。', 19],
    core: ['爐心', '一百多束燃料組件、數萬根燃料棒。核分裂產生的熱在這裡交給冷卻水；控制棒從上方插入調整反應度。', 13],
    pzr: ['調壓器', '一次側唯一有汽液界面的地方，用電熱器與噴灑維持 15.5 MPa，吸收冷卻水熱脹冷縮造成的壓力變化。', 20],
    sg: ['蒸汽產生器', '上萬根 U 形管把一次側的熱交給二次側；二次側的水在管外沸騰成約 6 MPa、280 °C 左右的飽和蒸汽。兩側的水不會混合。', 20],
    rcp: ['反應器冷卻水泵', '推動一次側冷卻水循環，每台每秒數噸到上萬公斤。停泵後靠自然循環仍能帶走衰變熱。', 20],
    cont: ['圍阻體', '最後一道實體屏障：鋼殼或預力混凝土結構，設計成在事故時承受數個大氣壓並限制洩漏。', 35],
    turb: ['汽輪機', '高壓缸與低壓缸，蒸汽膨脹推動葉片。壓水式電廠的蒸汽溫度較低，汽輪機特別巨大。', 23],
    gen: ['發電機', '與汽輪機同軸，每分鐘 1500 或 1800 轉（四極），輸出約二十多 kV 再升壓送上電網。', 38],
    cond: ['冷凝器', '把汽輪機排汽冷凝回水，維持很低的背壓；約三分之二的熱量從這裡排到環境。', 39],
    fwp: ['給水泵', '把冷凝水加壓、經過給水加熱器送回蒸汽產生器，完成二次側的朗肯循環。', 23],
    sea: ['最終熱沉', '海水、河水或冷卻塔。正常運轉時帶走廢熱，事故時也是衰變熱的最終去處。', 39]
  };
  function initLayout(root, cfg) {
    head(root, cfg.q); var v = el('div'), inf = info(root); root.insertBefore(v, inf);
    function g(k, inner) { return '<g data-k="' + k + '" style="cursor:pointer">' + inner + '</g>'; }
    function R(x, y, w, h, c, rx) { return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" rx="' + (rx || 4) + '" fill="' + c + '" fill-opacity="0.22" stroke="' + c + '" stroke-width="1.6"/>'; }
    var s = '';
    s += g('cont', '<path d="M20 290 L20 90 Q20 18 160 18 Q300 18 300 90 L300 290 Z" fill="' + GY + '" fill-opacity="0.07" stroke="' + GY + '" stroke-width="2"/>' + tx(160, 36, '圍阻體', 11, GY));
    s += ln(110, 140, 175, 140, RD, 5) + ln(190, 230, 150, 250, BL, 5) + ln(130, 250, 110, 230, BL, 5) + ln(192, 200, 192, 230, BL, 5);
    s += ln(192, 62, 192, 50, OR, 4) + ln(192, 50, 345, 50, OR, 4) + ln(345, 50, 345, 70, OR, 4);
    s += ln(400, 125, 400, 168, OR, 3) + ln(390, 215, 390, 240, BL, 3) + ln(390, 240, 300, 240, BL, 3) + ln(285, 240, 210, 240, BL, 3) + ln(210, 240, 210, 190, BL, 3);
    s += ln(440, 185, 560, 185, '#2a9d8f', 3) + ln(440, 200, 560, 200, '#2a9d8f', 3) + ln(127, 110, 127, 140, RD, 3);
    s += g('rpv', R(60, 100, 50, 150, BL, 18) + tx(85, 268, '壓力槽', 10, BL));
    s += g('core', R(68, 160, 34, 60, RD, 3) + tx(85, 194, '爐心', 10, RD));
    s += g('pzr', R(115, 58, 24, 52, PU, 10) + tx(127, 52, '調壓器', 10, PU));
    s += g('sg', R(170, 62, 44, 138, OR, 18) + tx(192, 214, '蒸汽產生器', 10, OR) + tx(192, 132, 'U 形管', 9, 'var(--text-muted)'));
    s += g('rcp', '<circle cx="140" cy="250" r="13" fill="' + BL + '" fill-opacity="0.22" stroke="' + BL + '" stroke-width="1.6"/>' + tx(140, 280, '冷卻水泵', 10, BL));
    s += g('turb', '<path d="M330 70 L460 60 L460 125 L330 115 Z" fill="' + GD + '" fill-opacity="0.22" stroke="' + GD + '" stroke-width="1.6"/>' + tx(395, 97, '汽輪機', 11, GD));
    s += ln(460, 92, 490, 92, GY, 4) + g('gen', R(490, 70, 62, 44, GR, 8) + tx(521, 97, '發電機', 11, GR));
    s += g('cond', R(345, 168, 95, 47, '#2a9d8f', 6) + tx(392, 196, '冷凝器', 11, '#2a9d8f'));
    s += g('fwp', '<circle cx="292" cy="240" r="11" fill="' + BL + '" fill-opacity="0.22" stroke="' + BL + '" stroke-width="1.6"/>' + tx(292, 266, '給水泵', 10, BL));
    s += g('sea', R(560, 160, 66, 60, '#2a9d8f', 6) + tx(593, 186, '海水／', 10, '#2a9d8f') + tx(593, 200, '冷卻塔', 10, '#2a9d8f'));
    s += tx(142, 133, '熱管段', 9, RD) + tx(268, 44, '主蒸汽', 9, OR) + tx(500, 180, '冷卻水', 9, '#2a9d8f');
    v.innerHTML = '<div style="overflow-x:auto"><div style="min-width:520px">' + svgw('0 0 640 300', s) + '</div></div>';
    function show(k) { var p = PARTS[k]; inf.innerHTML = '<b>' + p[0] + '</b>：' + p[1] + '（第 ' + p[2] + ' 課）';
      v.querySelectorAll('g[data-k]').forEach(function (e) { e.style.opacity = e.getAttribute('data-k') === k || e.getAttribute('data-k') === 'cont' ? 1 : 0.55; }); }
    v.querySelectorAll('g[data-k]').forEach(function (e) { e.addEventListener('click', function (ev) { ev.stopPropagation(); show(e.getAttribute('data-k')); }); });
    inf.innerHTML = '點圖中的元件看說明。紅色是一次側熱管段、藍色是冷管段與給水、橘色是蒸汽、綠色是冷卻水。'; }

  /* ---------- 連鎖反應 ---------- */
  function initChain(root, cfg) {
    head(root, cfg.q); var k = 1.001, L = -4, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '增殖因數 k', 0.995, 1.01, 0.0005, k, function (q) { return q.toFixed(4); }, 'k', function (q) { k = q; draw(); });
    slider(root, '瞬發中子世代時間 ℓ（對數，秒）', -5, -3, 0.1, L, function (q) { var v = Math.pow(10, q), e = Math.floor(q + 1e-9); return (v / Math.pow(10, e)).toFixed(2) + ' × 10' + sup(e) + ' s'; }, 'l', function (q) { L = q; draw(); });
    function draw() { var l = Math.pow(10, L), dk = k - 1, Tp = dk !== 0 ? l / dk : Infinity, Td;
      if (dk === 0) Td = Infinity; else if (dk < BETA) Td = (l + BETA / LAMB) / dk; else Td = l / (dk - BETA);
      var d1 = [], d2 = [], tm = 30;
      for (var t = 0; t <= tm + 1e-9; t += tm / 200) { d1.push([t, t / Tp / Math.LN10]); d2.push([t, t / Td / Math.LN10]); }
      v.innerHTML = chart(640, 230, [{ d: d1, c: RD, n: '只有瞬發中子' }, { d: d2, c: BL, n: '加上緩發中子' }], { y0: -1, y1: 3, xl: '時間（秒）', yl: 'log₁₀（中子數倍數）' });
      inf.innerHTML = '反應度 ρ ≈ k − 1 = <b>' + Math.round(dk * 1e5) + ' pcm</b>。只算瞬發中子：週期 ℓ/(k−1) = <b>' + (isFinite(Tp) ? sci(Tp) + ' s' : '∞') + '</b>；' +
        '考慮緩發中子：週期約 <b>' + (isFinite(Td) ? sci(Td) + ' s' : '∞') + '</b>' + (dk >= BETA ? '<br><b style="color:' + RD + '">k − 1 超過 β = 0.0065：瞬發臨界，緩發中子救不了，功率在毫秒尺度暴增。</b>' : dk > 0 ? '。緩發中子讓有效世代時間從 ' + sci(l) + ' 秒拉長到約 0.08 秒，控制系統來得及反應。' : dk < 0 ? '。k < 1：中子數逐漸衰減（次臨界）。' : '：剛好臨界，中子數不變。'); }
    draw(); }

  /* ---------- 點動態 ---------- */
  function initKin(root, cfg) {
    head(root, cfg.q); var rho = 100, a = 2, fb = true, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    var bar = el('div'), bOn = btn('有溫度回饋', 1), bOff = btn('沒有回饋', 0); bar.appendChild(bOn); bar.appendChild(bOff); root.insertBefore(bar, v);
    bOn.onclick = function () { fb = true; mark(bar, 1); draw(); }; bOff.onclick = function () { fb = false; mark(bar, 0); draw(); }; mark(bar, 1);
    slider(root, '插入的反應度 ρ（pcm；β = 650 pcm）', -600, 600, 10, rho, function (q) { return q + ' pcm（' + f2(q / 650) + ' 元）'; }, 'r', function (q) { rho = q; draw(); });
    slider(root, '燃料溫度係數 |α|（pcm/K，負回饋）', 0.5, 5, 0.1, a, function (q) { return '−' + q; }, 'a', function (q) { a = q; draw(); });
    var LAM = 2e-5, TAU = 5, K = 300;
    function draw() { var n = 1, C = BETA / (LAM * LAMB), dT = 0, dt = 0.005, d = [], mx = 1, r0 = rho * 1e-5;
      for (var i = 0; i <= 12000; i++) { var t = i * dt; if (i % 40 === 0) d.push([t, n * 100]); mx = Math.max(mx, n);
        var r = r0 - (fb ? a * 1e-5 * dT : 0), A = (r - BETA) / LAM, B = BETA / LAM, m11 = 1 - dt * A, m12 = -dt * LAMB, m21 = -dt * B, m22 = 1 + dt * LAMB, det = m11 * m22 - m12 * m21;
        var nn = (n * m22 - m12 * C) / det, CC = (m11 * C - m21 * n) / det; n = nn; C = CC; dT += dt * (K * (n - 1) - dT) / TAU; if (n > 1e6) break; }
      var top = Math.min(mx * 100 * 1.1, 2000);
      v.innerHTML = chart(640, 230, [{ d: d, c: BL, n: '功率（初始 = 100%）' }], { y0: 0, y1: Math.max(top, 120), xl: '時間（秒）', hl: [{ y: 100, c: GY, n: '初始功率' }] });
      var pj = r0 < BETA ? BETA / (BETA - r0) : Infinity, per = r0 > 0 && r0 < BETA ? (BETA - r0) / (LAMB * r0) : null;
      inf.innerHTML = (r0 >= BETA ? '<b style="color:' + RD + '">瞬發臨界！</b>' : '瞬發跳躍：功率在幾十毫秒內跳到 β/(β−ρ) = <b>' + pct(pj) + '</b>，之後以' + (per ? '約 <b>' + f1(per) + ' 秒</b>的週期' : '緩慢的速度') + (r0 > 0 ? '上升' : '下降') + '。') +
        (fb && r0 > 0 ? '<br>有負的溫度回饋：溫度上升 ΔT 讓反應度減少 |α|ΔT，最後停在 ρ = |α|ΔT，也就是功率約 <b>' + pct(1 + r0 / (a * 1e-5 * K)) + '</b> 的新平衡（這裡假設功率每增加 100%，燃料平均溫度約升高 300 K）。' : !fb && r0 > 0 ? '<br>沒有回饋時，功率會一直指數上升，只能靠控制棒或急停。' : ''); }
    draw(); }

  /* ---------- 控制棒價值 ---------- */
  function initRod(root, cfg) {
    head(root, cfg.q); var z = 50, W = 1200, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '插入深度（爐心高度的 %）', 0, 100, 1, z, function (q) { return q + '%'; }, 'z', function (q) { z = q; draw(); });
    slider(root, '全插入總價值（pcm）', 300, 3000, 50, W, function (q) { return q + ' pcm'; }, 'w', function (q) { W = q; draw(); });
    function I(x) { return x - Math.sin(2 * Math.PI * x) / (2 * Math.PI); }
    function draw() { var d1 = [], d2 = [];
      for (var x = 0; x <= 1.0001; x += 0.01) { d1.push([x * 100, W * I(x)]); d2.push([x * 100, W * 2 * Math.pow(Math.sin(Math.PI * x), 2) / 100]); }
      var x = z / 100, w = W * I(x), dw = W * 2 * Math.pow(Math.sin(Math.PI * x), 2) / 100;
      v.innerHTML = chart(640, 230, [{ d: d1, c: BL, n: '積分價值（pcm）' }, { d: d2, c: OR, n: '微分價值（pcm/%）× 100', dash: '5 4' }].map(function (s, i) { if (i) s.d = s.d.map(function (p) { return [p[0], p[1] * 100]; }); return s; }),
        { y0: 0, y1: W * 2.05, xl: '插入深度（%）', pts: [{ x: z, y: w, c: BL }] });
      inf.innerHTML = '插入 ' + z + '% 時已加入 <b>' + Math.round(w) + ' pcm</b> 的負反應度（' + f2(w / 650) + ' 元）；此處每再插 1% 約 <b>' + f1(dw) + ' pcm</b>。' +
        '<br>中子通量在爐心中間最大，所以控制棒在中段最「有效」，頭尾幾乎沒作用——積分價值呈 S 形。'; }
    draw(); }

  /* ---------- 氙毒 ---------- */
  function initXenon(root, cfg) {
    head(root, cfg.q); var p2 = 0, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '在 t = 0 把功率從 100% 改成', 0, 100, 5, p2, function (q) { return q + '%'; }, 'p', function (q) { p2 = q; draw(); });
    var lI = Math.LN2 / 6.57, lX = Math.LN2 / 9.14, sp = 0.286, gI = 0.0639, gX = 0.0024;
    function draw() { var I = gI / lI, X = (gI + gX) / (lX + sp), X0 = X, p = p2 / 100, dt = 0.02, d = [], mn = 0, pk = 0, tp = 0;
      for (var i = 0; i <= 72 / dt; i++) { var t = i * dt, w = -2800 * X / X0; if (i % 10 === 0) d.push([t, w]); if (w < mn) { mn = w; tp = t; }
        var dI = gI * p - lI * I, dX = gX * p + lI * I - lX * X - sp * p * X; I += dt * dI; X += dt * dX; }
      var Xe = p > 0 ? (gI + gX) * p / (lX + sp * p) : 0;
      v.innerHTML = chart(640, 230, [{ d: d, c: PU, n: '氙的反應度（pcm）' }], { y0: Math.min(mn * 1.1, -3000), y1: 0, xl: '時間（小時）', hl: [{ y: -2800, c: GY, n: '100% 功率的平衡值' }] });
      inf.innerHTML = '最負出現在第 <b>' + f1(tp) + ' 小時</b>，約 <b>' + Math.round(mn) + ' pcm</b>' + (mn < -2850 ? '（比滿功率平衡時再多 ' + Math.round(-2800 - mn) + ' pcm）' : '') + '；新平衡約 ' + Math.round(-2800 * Xe / X0) + ' pcm。' +
        (p2 === 0 ? '<br>停機後碘-135（半衰期 6.6 小時）繼續衰變成氙，而氙不再被中子「燒掉」，所以氙先增加、約十小時後達到峰值，再慢慢衰減。如果剩餘反應度不夠抵銷這個峰值，反應爐要等一兩天才能重新起動，稱為<b>碘坑</b>。' : '<br>降載後也會出現較小的氙峰，造成功率分布擺動（氙振盪），需要用控制棒或硼調整。'); }
    draw(); }

  /* ---------- 衰變熱 ---------- */
  function initDecay(root, cfg) {
    head(root, cfg.q); var P0 = cfg.P0 || 3400, D = 540, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '運轉時的熱功率（MWt）', 100, 4600, 50, P0, function (q) { return q + ' MWt'; }, 'p', function (q) { P0 = q; draw(); });
    slider(root, '停機前連續運轉（天）', 10, 1500, 10, D, function (q) { return q + ' 天'; }, 'd', function (q) { D = q; draw(); });
    function f(t) { var T = D * 86400; return 0.066 * (Math.pow(t, -0.2) - Math.pow(t + T, -0.2)); }
    function draw() { var d = [];
      for (var e = 0; e <= 7.01; e += 0.05) d.push([e, f(Math.pow(10, e)) * 100]);
      v.innerHTML = chart(640, 230, [{ d: d, c: RD, n: '衰變熱（% 額定功率）' }], { y0: 0, y1: 7, xl: '停機後時間（log₁₀ 秒）：0 = 1 秒、1.8 = 1 分、3.6 = 1 小時、4.9 = 1 天、6.4 = 1 個月',
        vl: [{ x: 1.78, c: GY, n: '1 分' }, { x: 3.56, c: GY, n: '1 時' }, { x: 4.94, c: GY, n: '1 天' }, { x: 6.41, c: GY, n: '1 月' }] });
      var rows = [['1 秒', 1], ['1 分鐘', 60], ['1 小時', 3600], ['1 天', 86400], ['1 週', 604800], ['1 個月', 2.592e6]].map(function (r) { var P = f(r[1]) * P0;
        return [r[0], pct(f(r[1])), f1(P) + ' MW', f1(P * 1e6 / 2.55e6 * 3.6) + ' m³/h']; });
      inf.innerHTML = '用 Way–Wigner 近似 P/P₀ = 0.066 [t<sup>−0.2</sup> − (t+T)<sup>−0.2</sup>]（誤差約 ±20%）。最後一欄是：如果沒有其他冷卻，每小時要沸騰掉多少水（從 40 °C 加熱再沸騰，每公斤約 2.55 MJ）。' +
        table(rows, ['停機後', '比例', '功率', '沸騰的水']); }
    draw(); }

  /* ---------- 熱通道 ---------- */
  function initChan(root, cfg) {
    head(root, cfg.q); var q = 30, m = 0.34, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '最大線功率 q′ₘₐₓ（kW/m）', 10, 60, 1, q, function (x) { return x + ' kW/m'; }, 'q', function (x) { q = x; draw(); });
    slider(root, '每根燃料棒的冷卻水流量（kg/s）', 0.15, 0.5, 0.01, m, f2, 'm', function (x) { m = x; draw(); });
    var H = 4.27, He = 4.6, cp = 5800, Tin = 290, Ts = 345, ro = 0.00475, ri = 0.00418, rf = 0.0041, h = 35000, kc = 17, hg = 5000, kf = 3.0;
    function draw() { var Q = q * 1000, c1 = [], c2 = [], c3 = [], mxF = 0, mxC = 0, zF = 0, A = Q * He / (Math.PI * m * cp), s0 = Math.sin(Math.PI * H / (2 * He));
      for (var z = 0; z <= H + 1e-9; z += H / 120) { var zz = z - H / 2, ql = Q * Math.cos(Math.PI * zz / He), Tc = Math.min(Tin + A * (Math.sin(Math.PI * zz / He) + s0), Ts);
        var Tw = Tc + ql / (2 * Math.PI * ro * h), Tci = Tw + ql * Math.log(ro / ri) / (2 * Math.PI * kc), Tf = Tci + ql / (2 * Math.PI * rf * hg) + ql / (4 * Math.PI * kf);
        c1.push([z, Tc]); c2.push([z, Tw]); c3.push([z, Tf]); if (Tf > mxF) { mxF = Tf; zF = z; } mxC = Math.max(mxC, Tin + A * (Math.sin(Math.PI * zz / He) + s0)); }
      v.innerHTML = chart(640, 250, [{ d: c3, c: RD, n: '燃料中心' }, { d: c2, c: OR, n: '被覆管外表面' }, { d: c1, c: BL, n: '冷卻水' }], { y0: 250, y1: Math.max(2000, mxF * 1.08), xl: '離燃料棒底端的高度（m）', hl: [{ y: 2800, c: RD, n: 'UO₂ 熔點約 2800 °C' }, { y: Ts, c: BL, n: '飽和溫度 345 °C' }] });
      inf.innerHTML = '燃料中心最高 <b>' + Math.round(mxF) + ' °C</b>（在 ' + f2(zF) + ' m，中點以上一點：冷卻水愈往上愈熱）；冷卻水出口' + (mxC >= Ts ? '<b style="color:' + RD + '">達到飽和溫度：這根熱通道出現整體沸騰，偏離核沸騰（DNB）的風險大增，必須降功率或加大流量。</b>' : ' <b>' + Math.round(mxC) + ' °C</b>，仍低於飽和溫度。') +
        '<br>溫度差的大部分落在燃料丸本身：q′/(4πk) = ' + Math.round(Q / (4 * Math.PI * kf)) + ' K——UO₂ 是很差的導熱體。'; }
    draw(); }

  /* ---------- 自然循環 ---------- */
  function initNat(root, cfg) {
    head(root, cfg.q); var Q = 50, Hh = 10, K = 20, A = 0.3, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '要帶走的熱 Q（MW）', 1, 200, 1, Q, function (x) { return x + ' MW'; }, 'q', function (x) { Q = x; draw(); });
    slider(root, '熱源與冷源的高度差 H（m）', 1, 30, 0.5, Hh, function (x) { return x + ' m'; }, 'h', function (x) { Hh = x; draw(); });
    slider(root, '迴路的總阻力係數 K', 5, 100, 1, K, function (x) { return x; }, 'k', function (x) { K = x; draw(); });
    var rho = 740, be = 2.8e-3, cp = 5500, g = 9.81;
    function md(q) { return Math.cbrt(2 * rho * rho * A * A * be * g * Hh * q * 1e6 / (K * cp)); }
    function draw() { var d = [], m = md(Q), dT = Q * 1e6 / (m * cp);
      for (var x = 0; x <= 200; x += 2) d.push([x, md(x)]);
      v.innerHTML = chart(640, 220, [{ d: d, c: BL, n: '自然循環流量（kg/s）' }], { y0: 0, xl: '熱功率 Q（MW）', pts: [{ x: Q, y: m, c: RD, n: Math.round(m) + ' kg/s' }] });
      inf.innerHTML = 'ṁ = [2ρ²A²βgHQ/(K c<sub>p</sub>)]<sup>1/3</sup> = <b>' + Math.round(m) + ' kg/s</b>，冷熱段溫差 ΔT = Q/(ṁc<sub>p</sub>) = <b>' + f1(dT) + ' K</b>。' +
        '<br>流量只隨 Q 的<b>立方根</b>增加，所以 ΔT ∝ Q<sup>2/3</sup>：熱愈多、溫差愈大。把熱交換器放高（H 大）、管路做短做粗（K 小），是被動式設計的關鍵。' + (dT > 60 ? '<br><b style="color:' + RD + '">溫差太大：熱段可能沸騰，需要更大的高度差或更小的阻力。</b>' : ''); }
    draw(); }

  /* ---------- 熱效率 ---------- */
  function initEff(root, cfg) {
    head(root, cfg.q); var Th = 280, Tc = 30, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '進汽輪機的熱源溫度 T<sub>h</sub>（°C）', 200, 950, 5, Th, function (x) { return x + ' °C'; }, 'h', function (x) { Th = x; draw(); });
    slider(root, '冷源溫度 T<sub>c</sub>（°C）', 5, 50, 1, Tc, function (x) { return x + ' °C'; }, 'c', function (x) { Tc = x; draw(); });
    var P = [['輕水爐', 283, 34], ['鈉冷', 500, 40], ['HTR-PM', 567, 42]];
    function draw() { var c = [], ca = [], K = 273.15;
      for (var t = 150; t <= 1000; t += 10) { c.push([t, 100 * (1 - (Tc + K) / (t + K))]); ca.push([t, 100 * (1 - Math.sqrt((Tc + K) / (t + K)))]); }
      var e1 = 1 - (Tc + K) / (Th + K), e2 = 1 - Math.sqrt((Tc + K) / (Th + K));
      v.innerHTML = chart(640, 240, [{ d: c, c: BL, n: '卡諾上限' }, { d: ca, c: OR, n: 'Curzon–Ahlborn（最大功率時）', dash: '5 4' }], { y0: 0, y1: 80, xl: '熱源溫度（°C）', yl: '效率 %',
        pts: P.map(function (p) { return { x: p[1], y: p[2], c: GR, n: p[0] }; }).concat([{ x: Th, y: e1 * 100, c: RD }]) });
      inf.innerHTML = '卡諾效率 1 − T<sub>c</sub>/T<sub>h</sub> = <b>' + pct(e1) + '</b>；Curzon–Ahlborn 1 − √(T<sub>c</sub>/T<sub>h</sub>) = <b>' + pct(e2) + '</b>（溫度要用絕對溫度）。' +
        '<br>3400 MWt 的反應爐若以 Curzon–Ahlborn 效率運轉，約可發 <b>' + Math.round(3400 * e2) + ' MWe</b>，排出 ' + Math.round(3400 * (1 - e2)) + ' MW 廢熱。綠點是實際電廠的淨效率（超超臨界燃煤約 600 °C、46%）。'; }
    draw(); }

  /* ---------- 縱深防禦 ---------- */
  var DID = [
    ['第一層：預防異常', '保守的設計、高品質的製造與施工、良好的運轉維護。目標：讓異常根本不要發生。', '材料規格、品質保證、運轉人員訓練、定期檢查'],
    ['第二層：控制異常', '偵測偏離正常的狀況並把它拉回來，避免演變成事故。', '控制系統、限制器、警報、技術規範的運轉限制'],
    ['第三層：控制設計基準事故', '假設事故還是發生了，靠安全系統把後果控制在設計基準內：爐心不損壞、放射性不外洩。', '急停、緊急爐心冷卻、輔助給水、圍阻體隔離'],
    ['第四層：減緩嚴重事故', '連安全系統都失效、爐心開始損壞時，保護圍阻體的完整性，限制放射性外釋。', '爐心捕集器或壓力槽內滯留、氫氣控制、圍阻體排氣過濾、FLEX 移動設備'],
    ['第五層：場外緊急應變', '萬一大量放射性外釋，保護民眾。', '緊急計畫區、疏散與掩蔽、碘片、環境監測']];
  var BAR = [['燃料丸', '陶瓷 UO₂ 把大部分分裂產物鎖在晶格裡'], ['被覆管', '鋯合金管密封燃料丸，擋住氣態分裂產物'], ['一次側壓力邊界', '壓力槽、管路、蒸汽產生器 U 形管'], ['圍阻體', '鋼殼或預力混凝土，最後一道實體屏障']];
  function initDid(root, cfg) {
    head(root, cfg.q); var v = el('div'), inf = info(root), bar = el('div'); root.insertBefore(bar, inf); root.insertBefore(v, bar);
    var s = '', cs = [GY, BL, PU, OR];
    for (var i = 3; i >= 0; i--) s += '<g data-b="' + i + '" style="cursor:pointer"><circle cx="150" cy="120" r="' + (30 + i * 26) + '" fill="' + cs[i] + '" fill-opacity="0.12" stroke="' + cs[i] + '" stroke-width="2"/>' + tx(150, 120 - (30 + i * 26) + 15, BAR[i][0], 10, cs[i]) + '</g>';
    s += '<circle cx="150" cy="120" r="9" fill="' + RD + '"/>';
    s += DID.map(function (d, i) { var y = 22 + i * 44; return '<g data-l="' + i + '" style="cursor:pointer"><rect x="310" y="' + y + '" width="310" height="36" rx="6" fill="' + [GR, BL, PU, OR, RD][i] + '" fill-opacity="' + (0.12 + i * 0.05) + '" stroke="' + [GR, BL, PU, OR, RD][i] + '"/>' + tx(322, y + 23, d[0], 11.5, 'currentColor', 'start') + '</g>'; }).join('');
    v.innerHTML = '<div style="overflow-x:auto"><div style="min-width:520px">' + svgw('0 0 640 245', s) + '</div></div>';
    v.querySelectorAll('[data-l]').forEach(function (e) { e.addEventListener('click', function () { var d = DID[+e.getAttribute('data-l')]; inf.innerHTML = '<b>' + d[0] + '</b>：' + d[1] + '<br><span style="color:var(--text-muted)">手段：' + d[2] + '</span>'; }); });
    v.querySelectorAll('[data-b]').forEach(function (e) { e.addEventListener('click', function (ev) { ev.stopPropagation(); var b = BAR[+e.getAttribute('data-b')]; inf.innerHTML = '<b>屏障：' + b[0] + '</b>——' + b[1] + '。'; }); });
    inf.innerHTML = '左邊是四道<b>實體屏障</b>（由內而外），右邊是五層<b>防禦</b>。點任何一個看說明：屏障是「牆」，縱深防禦是「保護牆的策略」。'; }

  /* ---------- 事件樹 ---------- */
  function initPra(root, cfg) {
    head(root, cfg.q); var ie = -2, lp = -2, n = 2, b = 0.05, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '起始事件頻率（次／年，對數）', -4, 0, 0.1, ie, function (x) { return sci(Math.pow(10, x)); }, 'i', function (x) { ie = x; draw(); });
    slider(root, '每一串（train）失效機率（對數）', -4, -1, 0.1, lp, function (x) { return sci(Math.pow(10, x)); }, 'p', function (x) { lp = x; draw(); });
    slider(root, '冗餘串數 n', 1, 4, 1, n, function (x) { return x + ' 串'; }, 'n', function (x) { n = x; draw(); });
    slider(root, '共因失效比例 β', 0, 0.2, 0.01, b, f2, 'b', function (x) { b = x; draw(); });
    function draw() { var I = Math.pow(10, ie), p = Math.pow(10, lp), Q = n === 1 ? p : Math.pow((1 - b) * p, n) + b * p, s1 = I * (1 - Q) * (1 - Q), s2 = I * (1 - Q) * Q, s3 = I * Q, cdf = s2 + s3;
      var g = tx(60, 24, '起始事件', 11) + tx(230, 24, '注水', 11) + tx(400, 24, '長期再循環', 11) + tx(560, 24, '結果（次／年）', 11);
      g += ln(20, 120, 140, 120, GY, 2) + ln(140, 120, 140, 70, GY, 2) + ln(140, 120, 140, 200, GY, 2) + ln(140, 70, 310, 70, GR, 2) + ln(140, 200, 480, 200, RD, 2) + ln(310, 70, 310, 50, GY, 2) + ln(310, 70, 310, 110, GY, 2) + ln(310, 50, 480, 50, GR, 2) + ln(310, 110, 480, 110, RD, 2);
      g += tx(60, 112, sci(I).replace(/<\/?sup>/g, ''), 10) + tx(225, 62, '成功 ' + (1 - Q).toFixed(4), 9.5, GR) + tx(225, 214, '失效 Q', 9.5, RD) + tx(395, 44, '成功', 9.5, GR) + tx(395, 124, '失效 Q', 9.5, RD);
      g += tx(560, 54, '安全 ' + sci(s1).replace(/<sup>/, '^').replace(/<\/sup>/, ''), 10, GR) + tx(560, 114, '爐心損壞 ' + sci(s2).replace(/<sup>/, '^').replace(/<\/sup>/, ''), 10, RD) + tx(560, 204, '爐心損壞 ' + sci(s3).replace(/<sup>/, '^').replace(/<\/sup>/, ''), 10, RD);
      v.innerHTML = '<div style="overflow-x:auto"><div style="min-width:520px">' + svgw('0 0 640 230', g) + '</div></div>';
      inf.innerHTML = '每個安全功能的不可用度 Q ≈ ' + (n === 1 ? 'p' : '[(1−β)p]<sup>n</sup> + βp') + ' = <b>' + sci(Q) + '</b>' + (n > 1 && b * p > Math.pow((1 - b) * p, n) ? '（由<b>共因失效</b>主導：再加串數也沒用）' : '') + '。' +
        '<br>這個事件的爐心損壞頻率 = <b>' + sci(cdf) + ' 次／年</b>' + (cdf < 1e-6 ? '，低於第三代電廠常見的目標（總和小於 10⁻⁵）。' : cdf < 1e-4 ? '。' : '，<b style="color:' + RD + '">太高了</b>。'); }
    draw(); }

  /* ---------- LCOE ---------- */
  function initLcoe(root, cfg) {
    head(root, cfg.q); var oc = 6000, r = 7, N = 7, cf = 90, L = 60, fu = 8, om = 22, v = el('div'), inf = info(root); root.insertBefore(v, inf);
    slider(root, '隔夜建造成本（美元／kW）', 2000, 15000, 250, oc, function (x) { return '$' + x.toLocaleString(); }, 'o', function (x) { oc = x; draw(); });
    slider(root, '資金成本（實質利率 %）', 1, 12, 0.5, r, function (x) { return x + '%'; }, 'r', function (x) { r = x; draw(); });
    slider(root, '建造工期（年）', 3, 15, 1, N, function (x) { return x + ' 年'; }, 'n', function (x) { N = x; draw(); });
    slider(root, '容量因數（%）', 50, 95, 1, cf, function (x) { return x + '%'; }, 'c', function (x) { cf = x; draw(); });
    slider(root, '經濟壽命（年）', 20, 80, 5, L, function (x) { return x + ' 年'; }, 'l', function (x) { L = x; draw(); });
    function lc(rr) { var i = rr / 100, idc = 0; for (var k = 0; k < N; k++) idc += Math.pow(1 + i, N - k - 0.5) / N;
      var crf = i / (1 - Math.pow(1 + i, -L)), cap = oc * idc * crf / (8.76 * cf / 100 * 1000) * 1000; return [cap, idc]; }
    function draw() { var a = lc(r), cap = a[0], tot = cap + fu + om, d = [];
      for (var x = 1; x <= 12; x += 0.25) d.push([x, lc(x)[0] + fu + om]);
      v.innerHTML = chart(640, 210, [{ d: d, c: BL, n: '均化發電成本（美元／MWh）' }], { y0: 0, xl: '實質利率（%）', pts: [{ x: r, y: tot, c: RD, n: '$' + Math.round(tot) }] });
      inf.innerHTML = '建造期間利息使成本變為隔夜成本的 <b>' + f2(a[1]) + ' 倍</b>。每 MWh：資本 <b>$' + Math.round(cap) + '</b>、運維 $' + om + '、燃料 $' + fu + '，合計 <b>$' + Math.round(tot) + '</b>（資本佔 ' + Math.round(cap / tot * 100) + '%）。' +
        '<br>核電是「先付錢、後發電」：利率和工期對成本的影響，比燃料價格大得多。'; }
    draw(); }

  var INIT = { layout: initLayout, chain: initChain, kin: initKin, rod: initRod, xenon: initXenon, decay: initDecay, chan: initChan, natcirc: initNat, eff: initEff, did: initDid, pra: initPra, lcoe: initLcoe };
  function boot() { document.querySelectorAll('.np-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"⚛️", note=NP_NOTE):
    return make_with(icon, note, [("np-w", NPLIB)])
