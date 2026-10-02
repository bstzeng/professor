# -*- coding: utf-8 -*-
"""〈電漿物理〉共用工具與互動元件（PZLIB）。"""
from cc_common import *
from qt_common import BASEJS

PZ_NOTE = (u"「電漿」（plasma）在中國大陸稱為「等離子體」，兩者指同一件事。本課的數值多為代表性的數量級；"
           u"推導段落可以跳過，只看圖、互動與「重點」也能掌握概念。")

PZLIB = r"""
(function () {
  if (window.__pzLib) return; window.__pzLib = 1;
""" + BASEJS + r"""
  function sci(v) { if (v === 0) return '0'; var e = Math.floor(Math.log10(Math.abs(v))), m = v / Math.pow(10, e); return (Math.round(m * 10) / 10) + '×10' + String(e).split('').map(function (c) { return c === '-' ? '⁻' : '⁰¹²³⁴⁵⁶⁷⁸⁹'[+c]; }).join(''); }

  /* ---------- 薩哈電離 ---------- */
  var DEN = { '星際雲（10⁸ /m³）': 1e8, '日冕（10¹⁴ /m³）': 1e14, '太陽光球（10²³ /m³）': 1e23, '地面空氣（2.5×10²⁵ /m³）': 2.5e25 };
  function initSaha(root, cfg) {
    head(root, cfg.q); var d = cfg.d || '太陽光球（10²³ /m³）', T = 10000, bar = el('div'), view = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(bar); root.appendChild(view);
    Object.keys(DEN).forEach(function (k) { var b = btn(k, k); b.addEventListener('click', function () { d = k; mark(bar, k); draw(); }); bar.appendChild(b); }); mark(bar, d);
    var u = slider(root, '溫度', 2000, 40000, 100, T, function (v) { return v + ' K'; }, 'T', function (v) { T = v; draw(); }); root.appendChild(info);
    function x(T, n) { var r = 2.415e21 * Math.pow(T, 1.5) * Math.exp(-157800 / T) / n; return (-r + Math.sqrt(r * r + 4 * r)) / 2; }
    function draw() { var n = DEN[d], A = [], h = null; for (var t = 2000; t <= 40000; t += 100) { var v = x(t, n); A.push([t, v * 100]); if (h === null && v >= 0.5) h = t; }
      var xv = x(T, n);
      view.innerHTML = chart(640, 240, [{ d: A, c: '#8e6bbf', n: '氫的電離比例（%）' }], { x0: 2000, x1: 40000, y0: 0, y1: 105, xl: '溫度（K）', vl: h ? [{ x: h, c: '#e0605a', n: '50% 電離 ≈ ' + h + ' K' }] : [], pts: [{ x: T, y: xv * 100, c: '#e8a33d' }] });
      info.innerHTML = '密度 ' + d + '、溫度 ' + T + ' K：氫有 <b>' + (xv < 0.001 ? '不到 0.1' : f1(xv * 100)) + '%</b> 被電離。氫的電離能是 13.6 eV（相當於約 15.8 萬 K），但因為高速尾巴與「熵」的作用，<b>遠低於這個溫度就能大量電離</b>；而且密度越低，越容易電離（電子和離子不容易碰在一起復合）。這就是為什麼稀薄的太空幾乎都是電漿。'; }
    u();
  }

  /* ---------- 德拜屏蔽 ---------- */
  function initDebye(root, cfg) {
    head(root, cfg.q); var ld = 1, view = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view);
    var u = slider(root, '德拜長度 λ_D（相對單位）', 0.3, 3, 0.05, ld, f2, 'ld', function (v) { ld = v; draw(); }); root.appendChild(info);
    var pts = []; for (var i = 0; i < 260; i++) pts.push([Math.random() * 300, Math.random() * 220, Math.random()]);
    function draw() { var A = [], B = []; for (var r = 0.05; r <= 5; r += 0.02) { A.push([r, 1 / r]); B.push([r, Math.exp(-r / ld) / r]); }
      var o = '<rect x="0" y="0" width="300" height="220" fill="#0e1116" rx="8"/>';
      pts.forEach(function (p) { var dx = p[0] - 150, dy = p[1] - 110, r = Math.sqrt(dx * dx + dy * dy) / 40, pe = 0.5 + 0.45 * Math.exp(-r / ld), neg = p[2] < pe;
        o += '<circle cx="' + n1(p[0]) + '" cy="' + n1(p[1]) + '" r="3" fill="' + (neg ? '#78c8ff' : '#ff9a7a') + '"/>'; });
      o += '<circle cx="150" cy="110" r="' + n1(ld * 40) + '" fill="none" stroke="#e8a33d" stroke-dasharray="4 3"/><circle cx="150" cy="110" r="8" fill="#ff5a3a"/>' + tx(150, 114, '+', 12, '#fff') + tx(150, 210, 'λ_D', 10, '#e8a33d');
      view.innerHTML = '<div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center"><div style="flex:0 0 260px">' + svgw('0 0 300 220', o) + '</div><div style="flex:1 1 340px">' +
        chart(380, 220, [{ d: A, c: '#999', n: '真空中的庫侖位勢 1/r', dash: '5 4' }, { d: B, c: '#3a6ea5', n: '電漿中：e^(−r/λ_D)/r' }], { x0: 0, x1: 5, y0: 0, y1: 4, xl: '距離 r' }) + '</div></div>';
      info.innerHTML = '放進一個正電荷（中央紅點），附近的電子（藍）被吸過來、正離子（橘）被推開，形成一層帶負電的「雲」，把正電荷的電場遮住。超過約 λ<sub>D</sub> 的地方幾乎感覺不到它——這叫<b>德拜屏蔽</b>。λ<sub>D</sub> ≈ 69 √(T/n) 公尺（T 以 K、n 以 /m³ 計）：溫度越高、密度越低，屏蔽距離越長。'; }
    u();
  }

  /* ---------- 帶電粒子運動與漂移 ---------- */
  function initGyro(root, cfg) {
    head(root, cfg.q); var mode = cfg.mode || 'exb', cv = document.createElement('canvas'); cv.width = 640; cv.height = 300; cv.style.cssText = 'width:100%;display:block;background:#0e1116;border-radius:8px'; root.appendChild(cv);
    var bar = el('div'), info = el('p', 'margin:6px 0 0;min-height:3em'), P; root.appendChild(bar); root.appendChild(info);
    var M = { gyro: '純迴旋（只有磁場）', exb: 'E×B 漂移（加電場）', grad: '梯度漂移（磁場不均勻）' };
    Object.keys(M).forEach(function (k) { var b = btn(M[k], k); b.addEventListener('click', function () { mode = k; mark(bar, k); reset(); }); bar.appendChild(b); }); mark(bar, mode);
    var TXT = { gyro: '磁場垂直螢幕（⊙）。勞侖茲力 qv×B 永遠垂直於速度，粒子繞圈：離子（橘）圈大、轉得慢；電子（藍）圈小、轉得快，而且方向相反。',
      exb: '加上向下的電場 E。粒子在圈的一側被加速、另一側被減速，半徑時大時小，結果整個圓心往旁邊移動——<b>E×B 漂移</b>。注意：離子和電子往<b>同一個方向</b>漂移，速度都是 E/B，與電荷、質量無關。',
      grad: '磁場越往上越強（背景越亮）。上方半徑較小、下方較大，圓心於是橫向漂移，而且<b>離子和電子方向相反</b>——這會產生電流。地球磁層的環電流就是這樣來的。' };
    function reset() { P = [{ x: 200, y: 150, vx: 0, vy: 1.6, q: 1, m: 1, c: '#ff9a7a', tr: [] }, { x: 200, y: 150, vx: 0, vy: 1.6 * 4, q: -1, m: 1 / 16, c: '#78c8ff', tr: [] }];
      if (mode !== 'gyro') { P[0].x = 120; P[1].x = 120; } info.innerHTML = TXT[mode]; }
    function B(y) { return mode === 'grad' ? 0.04 * (1 + (300 - y) / 150) : 0.05; }
    function step() { P.forEach(function (p) { for (var s = 0; s < 4; s++) { var b = B(p.y) * p.q / p.m, Ex = 0, Ey = mode === 'exb' ? 0.015 * p.q / p.m : 0, dt = 1;
          var vx = p.vx + Ex * dt / 2, vy = p.vy + Ey * dt / 2, t = b * dt / 2, s2 = 2 * t / (1 + t * t), vpx = vx + vy * t, vpy = vy - vx * t; vx += vpy * s2; vy -= vpx * s2; vx += Ex * dt / 2; vy += Ey * dt / 2;
          p.vx = vx; p.vy = vy; p.x += vx * dt; p.y += vy * dt; } p.tr.push([p.x, p.y]); if (p.tr.length > 600) p.tr.shift();
        if (p.x > 660 || p.x < -20) { p.x = p.x > 660 ? -10 : 650; p.tr = []; } }); }
    function draw() { var g = cv.getContext('2d'); g.fillStyle = '#0e1116'; g.fillRect(0, 0, 640, 300);
      if (mode === 'grad') for (var y = 0; y < 300; y += 6) { g.fillStyle = 'rgba(232,163,61,' + (0.02 + 0.12 * (300 - y) / 300) + ')'; g.fillRect(0, y, 640, 6); }
      g.fillStyle = 'rgba(255,255,255,0.25)'; for (var i = 30; i < 640; i += 60) for (var j = 30; j < 300; j += 60) { g.beginPath(); g.arc(i, j, 3, 0, 6.3); g.fill(); }
      if (mode === 'exb') { g.strokeStyle = '#5aa469'; g.fillStyle = '#5aa469'; g.font = '13px sans-serif'; g.fillText('E ↓', 600, 30); }
      P.forEach(function (p) { g.strokeStyle = p.c; g.lineWidth = 1.5; g.beginPath(); p.tr.forEach(function (q, i) { i ? g.lineTo(q[0], q[1]) : g.moveTo(q[0], q[1]); }); g.stroke(); g.fillStyle = p.c; g.beginPath(); g.arc(p.x, p.y, 4, 0, 6.3); g.fill(); });
      g.fillStyle = '#ddd'; g.font = '12px sans-serif'; g.fillText('⊙ 磁場 B 指向螢幕外', 12, 20); }
    reset(); setInterval(function () { if (!root.isConnected) return; step(); draw(); }, 30);
  }

  /* ---------- 磁鏡 ---------- */
  function initMirror(root, cfg) {
    head(root, cfg.q); var th = 45, R = 4, view = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view);
    var u1 = slider(root, '粒子在中央的投射角（速度與磁場的夾角）', 2, 88, 1, th, function (v) { return v + '°'; }, 'th', function (v) { th = v; draw(); });
    var u2 = slider(root, '鏡比 R = B_max / B_min', 1.5, 10, 0.1, R, f1, 'R', function (v) { R = v; draw(); }); root.appendChild(info);
    function Bz(z) { return 1 + (R - 1) * z * z; }
    function draw() { var s0 = Math.sin(th * Math.PI / 180), Z = [], z = 0, v = Math.cos(th * Math.PI / 180), dir = 1, esc = false, dt = 0.01;
      for (var t = 0; t <= 20; t += dt) { var acc = -0.5 * s0 * s0 * 2 * (R - 1) * z; v += acc * dt; z += v * dt; if (Math.abs(z) > 1) { esc = true; Z.push([t, z > 0 ? 1.05 : -1.05]); break; } Z.push([t, z]); }
      var lc = Math.asin(Math.sqrt(1 / R)) * 180 / Math.PI, o = '';
      for (var k = -3; k <= 3; k++) { var d = ''; for (var x = -1; x <= 1.0001; x += 0.02) { var yy = 70 + k * 16 / Math.sqrt(Bz(x)); d += (d ? 'L' : 'M') + n1(150 + x * 130) + ' ' + n1(yy); } o += '<path d="' + d + '" fill="none" stroke="#3a6ea5" stroke-width="1.2"/>'; }
      o += '<rect x="12" y="20" width="14" height="100" fill="#e8a33d" opacity="0.5"/><rect x="274" y="20" width="14" height="100" fill="#e8a33d" opacity="0.5"/>' + tx(150, 140, '磁鏡：兩端磁場較強', 9.5, 'var(--text-muted)');
      view.innerHTML = '<div style="display:flex;flex-wrap:wrap;gap:6px;align-items:center"><div style="flex:0 0 260px">' + svgw('0 0 300 150', o) + '</div><div style="flex:1 1 340px">' +
        chart(380, 210, [{ d: Z, c: esc ? '#e0605a' : '#5aa469', n: '粒子沿磁場方向的位置' }], { x0: 0, x1: 20, y0: -1.2, y1: 1.2, xl: '時間', hl: [{ y: 1, c: '#e8a33d', n: '磁鏡端' }, { y: -1, c: '#e8a33d', n: '' }] }) + '</div></div>';
      info.innerHTML = '磁矩 μ = mv⊥²/2B 守恆：粒子走進強磁場區時 v⊥ 變大，平行速度 v∥ 只好變小，最後反彈。損失錐角 = arcsin(√(1/R)) ≈ <b>' + f1(lc) + '°</b>。' +
        (esc ? '<b style="color:#e0605a">投射角太小，粒子在損失錐內，從端點逃走了。</b>' : '<b style="color:#5aa469">粒子被困在兩端之間來回彈跳。</b>') + '地球的范艾倫輻射帶就是一個天然的磁鏡。'; }
    u1(); u2();
  }

  /* ---------- 電漿截止頻率（電離層） ---------- */
  function initDisp(root, cfg) {
    head(root, cfg.q); var ln10 = 12, f = 7, view = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view);
    var u1 = slider(root, '電離層電子密度', 10, 12.6, 0.02, ln10, function (v) { return sci(Math.pow(10, v)) + ' /m³'; }, 'n', function (v) { ln10 = v; draw(); });
    var u2 = slider(root, '無線電頻率', 1, 30, 0.1, f, function (v) { return f1(v) + ' MHz'; }, 'f', function (v) { f = v; draw(); }); root.appendChild(info);
    function draw() { var fp = 8.98 * Math.sqrt(Math.pow(10, ln10)) / 1e6, A = [], L = []; for (var k = 0; k <= 30; k += 0.1) { A.push([k, Math.sqrt(fp * fp + k * k)]); L.push([k, k]); }
      var pass = f > fp, o = '<rect x="0" y="0" width="640" height="150" fill="var(--surface)"/>' + '<rect x="0" y="20" width="640" height="40" fill="#8e6bbf" opacity="0.18"/>' + tx(630, 44, '電離層', 10, '#8e6bbf', 'end') + ln(0, 140, 640, 140, '#5aa469', 3) + tx(10, 134, '地面', 9.5, '#5aa469', 'start');
      o += ln(120, 138, 320, pass ? 0 : 48, '#e0605a', 2) + (pass ? '' : ln(320, 48, 520, 138, '#e0605a', 2, 'stroke-dasharray="6 4"')) + '<circle cx="120" cy="136" r="5" fill="#e0605a"/>' + (pass ? tx(330, 14, '穿透到太空', 10, '#e0605a', 'start') : '<circle cx="520" cy="136" r="5" fill="#3a6ea5"/>' + tx(520, 128, '遠方接收', 9.5, '#3a6ea5'));
      view.innerHTML = svgw('0 0 640 150', o) + chart(640, 200, [{ d: A, c: '#3a6ea5', n: '電漿中：ω² = ω_p² + c²k²' }, { d: L, c: '#999', n: '真空：ω = ck', dash: '5 4' }], { x0: 0, x1: 30, y0: 0, y1: 40, xl: '波數（換算成 MHz）', yl: '頻率（MHz）', hl: [{ y: fp, c: '#e0605a', n: '電漿頻率 f_p = ' + f1(fp) + ' MHz' }, { y: f, c: '#e8a33d', n: '你的訊號' }] });
      info.innerHTML = '電漿頻率 f<sub>p</sub> ≈ 8.98 √n Hz = <b>' + f1(fp) + ' MHz</b>。頻率低於 f<sub>p</sub> 的電磁波在電漿中無法傳播（波數變成虛數），會被<b>反射</b>；高於的可以穿透。' +
        (pass ? '你的 ' + f1(f) + ' MHz 訊號穿過電離層進入太空——這就是衛星通訊與 GPS 使用高頻（GHz）的原因。' : '你的 ' + f1(f) + ' MHz 短波被電離層反射回地面，可以傳到地平線以外很遠的地方——業餘無線電與短波廣播就是這樣跨洋傳送的。') +
        ' 白天電離層密度較高，夜間較低，可用的頻率也跟著改變。'; }
    u1(); u2();
  }

  /* ---------- 勞森判據 ---------- */
  var SV = [[1, 6.3e-27], [2, 2.9e-25], [3, 1.6e-24], [5, 1.35e-23], [7, 4.0e-23], [10, 1.14e-22], [15, 2.65e-22], [20, 4.3e-22], [30, 6.6e-22], [50, 8.5e-22], [70, 8.7e-22], [100, 8.4e-22]];
  function sv(T) { for (var i = 1; i < SV.length; i++) if (T <= SV[i][0]) { var a = SV[i - 1], b = SV[i], f = (Math.log(T) - Math.log(a[0])) / (Math.log(b[0]) - Math.log(a[0])); return Math.exp(Math.log(a[1]) + f * (Math.log(b[1]) - Math.log(a[1]))); } return SV[SV.length - 1][1]; }
  function initLawson(root, cfg) {
    head(root, cfg.q); var T = 25, n = 10, tau = 1, view = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view);
    var us = [slider(root, '離子溫度', 1, 100, 0.5, T, function (v) { return v + ' keV（約 ' + Math.round(v * 11.6) + ' 百萬度）'; }, 'T', function (v) { T = v; draw(); }),
      slider(root, '密度', 1, 100, 1, n, function (v) { return v + ' ×10¹⁹ /m³'; }, 'n', function (v) { n = v; draw(); }),
      slider(root, '能量約束時間 τ_E', 0.1, 10, 0.1, tau, function (v) { return f1(v) + ' 秒'; }, 'tau', function (v) { tau = v; draw(); })];
    root.appendChild(info);
    function need(T) { return 12 * T * T / (3500 * sv(T)); }
    function draw() { var A = []; for (var t = 2; t <= 100; t *= 1.04) A.push([Math.log10(t), Math.log10(need(t))]);
      var tp = n * 1e19 * T * tau, req = need(T), pts = [{ x: Math.log10(T), y: Math.log10(tp), c: tp >= req ? '#5aa469' : '#e8a33d', n: '你的設定' },
        { x: Math.log10(16), y: Math.log10(1.5e21), c: '#3a6ea5', n: 'JT-60U 紀錄（約）' }, { x: Math.log10(10), y: Math.log10(8e20), c: '#8e6bbf', n: 'JET（約）' }];
      view.innerHTML = chart(640, 260, [{ d: A, c: '#e0605a', n: 'D-T 自持燃燒（點火）所需' }], { x0: 0.3, x1: 2, y0: 19, y1: 23.5, xl: 'log₁₀ 溫度（keV）', yl: 'log₁₀ 三重積 nTτ（keV·s/m³）', pts: pts });
      info.innerHTML = '三重積 nTτ<sub>E</sub> = <b>' + sci(tp) + '</b> keV·s/m³；這個溫度下點火需要 ' + sci(req) + '。' + (tp >= req ? '<b style="color:#5aa469">達到點火條件：α 粒子的加熱足以維持電漿溫度！</b>' : '尚未點火（' + Math.round(tp / req * 100) + '%）。') +
        ' 所需三重積在約 14 keV（1.6 億度）時最低，約 3×10²¹。溫度太低反應太少，太高則反應率不再增加而輻射損失變大。圖中點是磁約束實驗的大約紀錄（示意）。'; }
    us.forEach(function (f) { f(); });
  }

  function initAll() { document.querySelectorAll('.pz-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ saha: initSaha, debye: initDebye, gyro: initGyro, mirror: initMirror, disp: initDisp, lawson: initLawson })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def pzw(cfg, maxw=680):
    return wdg("pz-w", cfg, maxw)


pzlesson = make_lesson(u"⚡", PZ_NOTE, PZLIB, "pz-w")
