# -*- coding: utf-8 -*-
"""〈核融合〉（fus_）共用：課程包裝與 FUSLIB 互動元件（class="fus-w"）。

  gamow   伽莫夫峰：反應、溫度 → 馬克士威分布尾巴 × 穿隧機率，與反應率
  lawson  勞森判據：溫度、nτ → 與 D-T 點火曲線比較
  qval    Q 值：融合輸出、加熱輸入、效率 → 科學 Q 與工程 Q
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

FUS_NOTE = (u"本課的推導以主要步驟為主；互動模擬為教學用的簡化版本，數字為約略值。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def fsw(cfg, maxw=680):
    return wdg("fus-w", cfg, maxw)


FUSLIB = r"""
(function () {
  if (window.__fusLib) return; window.__fusLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function sv(T, r) { var t3 = Math.pow(T, 1 / 3); return r === 'dd' ? 2.33e-20 * Math.pow(T, -2 / 3) * Math.exp(-18.76 / t3) : 3.68e-18 * Math.pow(T, -2 / 3) * Math.exp(-19.94 / t3); }

  var RX = { dt: { n: 'D-T（氘—氚）', EG: 1175, lo: 1, hi: 100, T0: 10 }, dd: { n: 'D-D（氘—氘）', EG: 986, lo: 1, hi: 100, T0: 10 }, pp: { n: 'p-p（太陽核心）', EG: 493, lo: 0.3, hi: 10, T0: 1.35 } };
  function initGamow(root, cfg) {
    head(root, cfg.q); var P = { r: 'dt', T: 10 }, view = el('div'), inf, u;
    var b = bar(root); ['dt', 'dd', 'pp'].forEach(function (k) { var x = btn(RX[k].n, k); x.onclick = function () { P.r = k; P.T = RX[k].T0; mark(b, k); u(); }; b.appendChild(x); }); mark(b, 'dt');
    u = slider(root, '溫度 kT（keV，以 10 為底的對數；1 keV ≈ 1160 萬度）', -0.6, 2, 0.01, Math.log10(P.T), function (x) { var t = Math.pow(10, x); return f2(t) + ' keV（約 ' + Math.round(t * 11.6) + ' 百萬度）'; }, null, function (x) { P.T = Math.pow(10, x); draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var R = RX[P.r], T = P.T, E0 = Math.pow(R.EG * T * T / 4, 1 / 3), Emax = Math.max(6 * E0, 8 * T), mb = [], tn = [], pr = [], pmax = 0, mbmax = 0, tmax = 0;
      for (var i = 1; i <= 400; i++) { var E = Emax * i / 400, a = Math.exp(-E / T), t = Math.exp(-Math.sqrt(R.EG / E)); mb.push([E, a]); tn.push([E, t]); pr.push([E, a * t]); pmax = Math.max(pmax, a * t); mbmax = Math.max(mbmax, a); tmax = Math.max(tmax, t); }
      mb = mb.map(function (p) { return [p[0], p[1] / mbmax]; }); tn = tn.map(function (p) { return [p[0], p[1] / tmax]; }); pr = pr.map(function (p) { return [p[0], p[1] / pmax]; });
      view.innerHTML = chart(640, 250, [{ d: mb, c: BL, n: '有這麼多能量的粒子比例（馬克士威）', w: 1.6 }, { d: tn, c: OR, n: '穿隧機率', w: 1.6 }, { d: pr, c: RD, n: '兩者相乘：真正發生融合的能量（伽莫夫峰）', w: 2.4 }], { x0: 0, x1: Emax, y0: 0, y1: 1.05, xl: '碰撞能量（keV）', vl: [{ x: E0, c: RD, n: 'E₀ ≈ ' + f1(E0) + ' keV' }] });
      var rate = P.r === 'pp' ? '' : '<br>反應率 ⟨σv⟩ ≈ <b>' + sv(T, P.r).toExponential(1) + ' m³/s</b>' + (P.r === 'dt' ? '（D-D 在同溫度約為它的 ' + Math.round(sv(T, 'dt') / sv(T, 'dd')) + ' 分之一）' : '') + '。';
      inf.innerHTML = R.n + '：溫度 ' + f2(T) + ' keV 時，大部分的融合發生在約 <b>' + f1(E0) + ' keV</b>——是平均熱能的約 ' + f1(E0 / T) + ' 倍，但遠低於約數百 keV 的庫侖障壁。' +
        '<br>只有極少數跑得特別快的粒子（藍線的尾巴），又剛好穿隧成功（橘線），才會融合。' + rate +
        (P.r === 'pp' ? '<br>太陽核心只有約 1.35 keV。p-p 反應還需要一次弱交互作用（質子變中子），所以一個質子平均要等約百億年才會融合——太陽因此能穩定燃燒百億年。' : ''); }
    u();
  }

  function initLawson(root, cfg) {
    head(root, cfg.q); var P = { lt: Math.log10(15), ln: 20 }, view = el('div'), inf;
    var us = [slider(root, '溫度 T（keV，對數）', 0, 2, 0.01, P.lt, function (x) { return f1(Math.pow(10, x)) + ' keV'; }, null, function (x) { P.lt = x; draw(); }),
      slider(root, 'n τ_E（秒／立方公尺，以 10 為底的對數）', 17, 22, 0.01, P.ln, function (x) { return '10^' + f2(x); }, null, function (x) { P.ln = x; draw(); })];
    root.appendChild(view); inf = info(root);
    var CB = 3.34e-21, Ea = 3520;
    function need(T) { var d = Ea * sv(T, 'dt') - 4 * CB * Math.sqrt(T); return d > 0 ? 12 * T / d : Infinity; }
    function draw() { var c = []; for (var i = 0; i <= 200; i++) { var lt = i / 100, T = Math.pow(10, lt), nn = need(T); if (isFinite(nn) && nn < 1e23) c.push([lt, Math.log10(nn)]); }
      var T = Math.pow(10, P.lt), nn = need(T), ok = Math.pow(10, P.ln) >= nn;
      view.innerHTML = chart(640, 260, [{ d: c, c: RD, n: 'D-T 點火所需的 nτ_E', w: 2.4 }], { x0: 0, x1: 2, y0: 17, y1: 22, xl: 'log₁₀ 溫度（keV）', yl: 'log₁₀ nτ', pts: [{ x: P.lt, y: P.ln, c: ok ? GN : BL, n: ok ? '可以點火' : '' }, { x: 1, y: Math.log10(3.7e20), c: OR, n: 'ITER 設計（Q=10）' }] });
      var best = 1e99, bT = 0; for (i = 0; i <= 200; i++) { var tt = Math.pow(10, i / 100), q = need(tt) * tt; if (q < best) { best = q; bT = tt; } }
      inf.innerHTML = '溫度 ' + f1(T) + ' keV（約 ' + Math.round(T * 11.6) + ' 百萬度）時，點火需要 nτ_E ≥ <b>' + (isFinite(nn) ? nn.toExponential(1) : '∞') + '</b> s/m³。你的電漿：' + Math.pow(10, P.ln).toExponential(1) + ' → ' + (ok ? '<b>可以點火</b>：α 粒子的加熱足以抵銷所有損失，不再需要外部加熱。' : '<b>還不夠</b>。') +
        (T < 4.5 ? '<br>溫度太低：軔致輻射損失的能量比融合產生的還多，再好的約束也沒用。' : '') +
        '<br>三重積 nTτ_E 在約 <b>' + f1(bT) + ' keV</b> 附近最容易達到，約需 <b>' + best.toExponential(1) + ' keV·s/m³</b>——這是托卡馬克設計的目標溫度。'; }
    us.forEach(function (u) { u(); });
  }

  function initQ(root, cfg) {
    head(root, cfg.q); var P = { out: 3.15, inp: 2.05, eh: 0.007, et: 0.4 }, view = el('div'), inf, us;
    var pre = [['NIF 2022 年 12 月', [3.15, 2.05, 0.007]], ['NIF 2025 年 4 月', [8.6, 2.08, 0.007]], ['JET 1997', [16, 24, 0.3]], ['JET 2023（69 MJ）', [69, 210, 0.3]], ['ITER 目標', [500, 50, 0.4]], ['未來的電廠', [2500, 50, 0.5]]];
    var b = bar(root); pre.forEach(function (p) { var x = btn(p[0]); x.onclick = function () { P.out = p[1][0]; P.inp = p[1][1]; P.eh = p[1][2]; us.forEach(function (u) { u(); }); }; b.appendChild(x); });
    us = [slider(root, '融合產生的能量（相對單位，對數）', -1, 3.5, 0.01, Math.log10(P.out), function (x) { return f2(Math.pow(10, x)); }, null, function (x) { P.out = Math.pow(10, x); draw(); }),
      slider(root, '送進燃料的加熱能量（同單位，對數）', -1, 3.5, 0.01, Math.log10(P.inp), function (x) { return f2(Math.pow(10, x)); }, null, function (x) { P.inp = Math.pow(10, x); draw(); }),
      slider(root, '加熱系統的效率（從電網到燃料）', 0.005, 0.7, 0.001, P.eh, function (x) { return f1(x * 100) + '%'; }, null, function (x) { P.eh = x; draw(); }),
      slider(root, '熱轉電的效率', 0.3, 0.5, 0.01, P.et, function (x) { return Math.round(x * 100) + '%'; }, null, function (x) { P.et = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var Qs = P.out / P.inp, grid = P.inp / P.eh, elec = (P.out + P.inp) * P.et, Qe = elec / grid, W = 640, H = 120, mx = Math.max(grid, elec, P.out) * 1.05, sx = function (v) { return 150 + v / mx * (W - 170); }, g = '';
      [['從電網取用的電', grid, RD], ['送進燃料的能量', P.inp, OR], ['融合產生的能量', P.out, GN], ['可以發出的電', elec, BL]].forEach(function (r, i) { var y = 8 + i * 27; g += tx(140, y + 14, r[0], 11, null, 'end') + '<rect x="150" y="' + y + '" width="' + n1(Math.max(1, sx(r[1]) - 150)) + '" height="18" fill="' + r[2] + '" opacity="0.8"/>' + tx(sx(r[1]) + 4, y + 14, f1(r[1]), 10, null, 'start'); });
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      inf.innerHTML = '<b>科學 Q</b> = 融合輸出 ÷ 送進燃料的能量 = <b>' + f2(Qs) + '</b>' + (Qs >= 1 ? '（≥ 1：燃料本身產生的能量比得到的多——「點火」或「科學損益兩平」）' : '') + '。' +
        '<br><b>工程 Q</b> = 發出的電 ÷ 從電網取用的電 = <b>' + (Qe < 0.01 ? Qe.toExponential(1) : f2(Qe)) + '</b>' + (Qe >= 1 ? '——整座設施終於有淨發電。' : '——整座設施仍是<b>耗電</b>的。') +
        '<br>一座商業電廠大約需要工程 Q 在 5～10 以上（還要扣掉冷卻、磁鐵、泵浦的用電）。科學 Q 大於 1 是里程碑，但離發電還很遠。'; }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.fus-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ gamow: initGamow, lawson: initLawson, qval: initQ })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"☀️", FUS_NOTE, FUSLIB, "fus-w")

GAMOW = fsw({"t": "gamow", "q": u"伽莫夫峰：太陽怎麼在「太冷」的溫度下融合"})
LAWSON = fsw({"t": "lawson", "q": u"勞森判據：多熱、多密、多久，才能點火"})
QVAL = fsw({"t": "qval", "q": u"Q 值：點火了，為什麼還不能發電"})
