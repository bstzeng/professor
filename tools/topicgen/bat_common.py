# -*- coding: utf-8 -*-
"""〈電池與電動車〉（bat_）共用：課程包裝與 BTLIB 互動元件（class="bt-w"）。

  range    續航計算：車速、氣溫、空調（電阻加熱／熱泵）
  charge   充電時間與充電曲線：電池容量、充電樁功率、起訖電量、電池溫度
  cost     每百公里能源成本：電動車與油車
  degrade  電池衰退模擬：化學體系、溫度、快充比例、充電上限
"""
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

BT_NOTE = u"本課程介紹電池與電動車的原理與產業概況，不構成購車或投資建議；用電安全與車輛保養請依原廠說明。互動工具為簡化的教學模型，數值只用來建立直覺，實際表現因車款、環境與使用方式而有很大差異。"
F = D


def btw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("bt-w", cfg)


BTLIB = r"""
(function () {
  if (window.__btLib) return; window.__btLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function row(root, lab) { var d = el('div', 'margin:6px 0'); if (lab) d.appendChild(el('span', 'font-size:0.85em;color:var(--text-muted);margin-right:4px', lab)); root.appendChild(d); return d; }
  function bar(root, lab, opts, get, set) { var b = row(root, lab); opts.forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { set(o[1]); mark(b, o[1]); }; b.appendChild(x); }); mark(b, get()); return b; }
  function sl(root, lab, mn, mx, st, val, fmt, cb) { return slider(root, lab, mn, mx, st, val, fmt, null, cb); }
  function f0(x) { return Math.round(x).toLocaleString('en-US'); }
  function f1(x) { return (Math.round(x * 10) / 10).toFixed(1); }
  function note(s) { return '<br><span style="color:var(--text-muted);font-size:0.9em">' + s + '</span>'; }

  /* ---------- 續航 ---------- */
  function cons(v, T, hv) { /* Wh/km at speed v km/h, temp T, hvac mode */
    var ms = v / 3.6, m = 1900, crr = 0.009 * (T < 0 ? 1.15 : 1), cda = 0.6, rho = 1.293 * 273 / (273 + T), eta = 0.83;
    var Fr = crr * m * 9.81, Fa = 0.5 * rho * cda * ms * ms, drive = (Fr + Fa) / 3.6 / eta; /* N -> Wh/km : N*1000m/3600 */
    var aux = 0.3, hvac = 0;
    if (hv === 'ac') hvac = Math.max(0, T - 22) * 0.12 + (T > 22 ? 0.3 : 0);
    if (hv === 'heat') hvac = Math.max(0, 20 - T) * 0.16 + (T < 20 ? 0.3 : 0);
    if (hv === 'hp') hvac = (Math.max(0, 20 - T) * 0.16) / Math.max(1.4, 3 - Math.max(0, 10 - T) * 0.06) + (T < 20 ? 0.3 : 0);
    if (hv === 'auto') hvac = T >= 22 ? Math.max(0, T - 22) * 0.12 + 0.3 : (T < 18 ? (Math.max(0, 20 - T) * 0.16) / Math.max(1.4, 3 - Math.max(0, 10 - T) * 0.06) + 0.3 : 0);
    return { d: drive, a: (aux + hvac) * 1000 / v, roll: Fr / 3.6 / eta, aero: Fa / 3.6 / eta, hvac: hvac };
  }
  function usable(T) { return T >= 20 ? 1 : Math.max(0.75, 1 - (20 - T) * 0.004); }
  function initRange(root, cfg) { head(root, cfg.q); var P = { kwh: 75, v: 100, T: 25, hv: 'off' }, v = el('div'), inf;
    var u1 = sl(root, '電池可用容量', 40, 110, 5, P.kwh, function (x) { return x + ' kWh'; }, function (x) { P.kwh = x; draw(); });
    var u2 = sl(root, '定速車速', 30, 150, 5, P.v, function (x) { return x + ' km/h'; }, function (x) { P.v = x; draw(); });
    var u3 = sl(root, '氣溫', -20, 40, 1, P.T, function (x) { return x + ' °C'; }, function (x) { P.T = x; draw(); });
    bar(root, '空調：', [['關閉', 'off'], ['冷氣', 'ac'], ['暖氣（電阻式）', 'heat'], ['暖氣（熱泵）', 'hp']], function () { return P.hv; }, function (k) { P.hv = k; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var A = [], B = [];
      for (var s = 30; s <= 150; s += 5) { var c = cons(s, P.T, P.hv), c0 = cons(s, 20, 'off'); A.push([s, P.kwh * 1000 * usable(P.T) / (c.d + c.a)]); B.push([s, P.kwh * 1000 / (c0.d + c0.a)]); }
      var c = cons(P.v, P.T, P.hv), wh = c.d + c.a, R = P.kwh * 1000 * usable(P.T) / wh, c0 = cons(P.v, 20, 'off'), R0 = P.kwh * 1000 / (c0.d + c0.a);
      v.innerHTML = chart(680, 260, [{ d: B, c: GY, n: '理想（20°C、空調關閉）', dash: '5 4' }, { d: A, c: BL, n: '目前條件', w: 2.5 }], { x0: 30, x1: 150, y0: 0, xl: '定速車速（km/h）', yl: '續航（km）', pts: [{ x: P.v, y: R, c: RD, n: f0(R) + ' km' }] });
      var tot = c.roll + c.aero + c.a;
      inf.innerHTML = '在 ' + P.v + ' km/h、' + P.T + '°C 的條件下，耗電約 <b>' + f1(wh / 10) + ' kWh/100 km</b>，續航約 <b>' + f0(R) + ' km</b>（理想條件下 ' + f0(R0) + ' km，' + (R < R0 ? '減少 ' + Math.round((1 - R / R0) * 100) + '%' : '差不多') + '）。' +
        '<br>耗電組成：滾動阻力 ' + Math.round(c.roll / tot * 100) + '%、<b>空氣阻力 ' + Math.round(c.aero / tot * 100) + '%</b>、空調與車上電器 ' + Math.round(c.a / tot * 100) + '%' + (P.T < 20 ? '；低溫時電池可用容量約剩 ' + Math.round(usable(P.T) * 100) + '%' : '') + '。' +
        '<br>空氣阻力與車速的<b>平方</b>成正比：高速時它是最大的耗能來源；低速時，空調等固定功率的耗電，攤到每公里上反而變得明顯。' +
        note('簡化模型：一台約 1.9 噸的休旅車、平路定速、無風；未計入市區的加減速、坡度、輪胎與載重。熱泵在低溫下效率會降低。');
    }
    [u1, u2, u3].forEach(function (u) { u(); }); }

  /* ---------- 充電 ---------- */
  function carP(soc, pmax, chem) { /* kW the car accepts at SOC (0..1) */
    if (chem === 'lfp') { if (soc < 0.6) return pmax; if (soc < 0.9) return pmax * (1 - (soc - 0.6) / 0.3 * 0.55); return pmax * 0.45 * (1 - (soc - 0.9) / 0.1 * 0.8); }
    if (soc < 0.1) return pmax * (0.7 + soc * 3); if (soc < 0.5) return pmax; if (soc < 0.8) return pmax * (1 - (soc - 0.5) / 0.3 * 0.6); return pmax * 0.4 * (1 - (soc - 0.8) / 0.2 * 0.8);
  }
  function initCharge(root, cfg) { head(root, cfg.q); var P = { kwh: 75, pile: 150, car: 170, s0: 10, s1: 80, T: 25, chem: 'nmc' }, v = el('div'), inf;
    var u1 = sl(root, '電池容量', 40, 110, 5, P.kwh, function (x) { return x + ' kWh'; }, function (x) { P.kwh = x; draw(); });
    bar(root, '充電樁：', [['家用 7 kW', 7], ['直流 50 kW', 50], ['直流 150 kW', 150], ['直流 250 kW', 250], ['直流 350 kW', 350]], function () { return P.pile; }, function (k) { P.pile = k; draw(); });
    var u2 = sl(root, '車輛可接受的最大直流功率', 50, 300, 10, P.car, function (x) { return x + ' kW'; }, function (x) { P.car = x; draw(); });
    var u3 = sl(root, '起始電量', 0, 90, 5, P.s0, function (x) { return x + '%'; }, function (x) { P.s0 = x; if (P.s1 <= x) { P.s1 = x + 5; } draw(); });
    var u4 = sl(root, '目標電量', 10, 100, 5, P.s1, function (x) { return x + '%'; }, function (x) { P.s1 = x; draw(); });
    var u5 = sl(root, '電池溫度', -10, 40, 5, P.T, function (x) { return x + ' °C'; }, function (x) { P.T = x; draw(); });
    bar(root, '電池：', [['三元鋰（NMC）', 'nmc'], ['磷酸鋰鐵（LFP）', 'lfp']], function () { return P.chem; }, function (k) { P.chem = k; draw(); });
    root.appendChild(v); inf = info(root);
    function tf(T) { return T >= 20 ? 1 : T >= 10 ? 0.75 : T >= 0 ? 0.45 : 0.25; }
    function pw(soc) { if (P.pile <= 22) return Math.min(P.pile * 0.92, soc < 0.95 ? 11 : 11 * (1 - (soc - 0.95) / 0.05 * 0.7)); return Math.min(P.pile, carP(soc, P.car, P.chem) * tf(P.T)); }
    function draw() { var s1 = Math.max(P.s1, P.s0 + 5) / 100, s = P.s0 / 100, t = 0, dt = 1 / 60, C = [], S = [[0, s * 100]], e = 0;
      for (var q = 0; q <= 100; q += 1) C.push([q, pw(q / 100)]);
      while (s < s1 && t < 30) { var p = pw(s); s += p * dt / P.kwh; e += p * dt; t += dt; if (Math.abs((t * 60) % 2) < 1e-6 || s >= s1) S.push([t * 60, Math.min(s, s1) * 100]); }
      var mins = t * 60, avg = e / t, km = e / 0.16;
      var hf = mins > 180;
      v.innerHTML = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:6px">' +
        '<div>' + chart(340, 220, [{ d: C, c: OR, n: '充電功率（kW）', w: 2.5 }], { x0: 0, x1: 100, y0: 0, xl: '電量 %', vl: [{ x: P.s0, c: GY, n: '起' }, { x: Math.max(P.s1, P.s0 + 5), c: GN, n: '止' }] }) + '</div>' +
        '<div>' + chart(340, 220, [{ d: hf ? S.map(function (p) { return [p[0] / 60, p[1]]; }) : S, c: BL, n: '電量 %', w: 2.5 }], { x0: 0, y0: 0, y1: 100, xl: hf ? '小時' : '分鐘' }) + '</div></div>';
      inf.innerHTML = '從 ' + P.s0 + '% 充到 ' + Math.max(P.s1, P.s0 + 5) + '%：約 <b>' + (mins >= 120 ? f1(mins / 60) + ' 小時' : Math.round(mins) + ' 分鐘') + '</b>，充入約 <b>' + f0(e) + ' kWh</b>（約可行駛 ' + f0(km) + ' km），平均功率約 ' + f0(avg) + ' kW。' +
        (P.pile <= 22 ? '<br>家用交流充電：功率由車上的充電器決定（本模型上限約 11 kW），適合過夜慢充。' : '<br>直流快充：實際功率取決於充電樁、車輛與電池狀態<b>三者中最低</b>的。電量越高，車輛會主動<b>降低功率</b>以保護電池——所以快充通常只充到 80% 左右。') +
        (P.T < 20 && P.pile > 22 ? '<br><b>電池太冷</b>：低溫時鋰離子移動變慢，快充容易造成鋰析出，車輛會大幅限制功率；許多車會在導航到充電站時先預熱電池。' : '') +
        note('示意曲線：不同車款的充電曲線差異很大；本模型以一般三元鋰與磷酸鋰鐵電池的形狀粗略近似，並假設耗電 16 kWh/100 km。');
    }
    [u1, u2, u3, u4, u5].forEach(function (u) { u(); }); }

  /* ---------- 成本 ---------- */
  function initCost(root, cfg) { head(root, cfg.q); var P = { ev: 16, home: 3.5, pub: 10, share: 20, ice: 8, gas: 30, km: 15000 }, v = el('div'), inf;
    var us = [
      sl(root, '電動車耗電', 11, 25, 0.5, P.ev, function (x) { return x + ' kWh/100 km'; }, function (x) { P.ev = x; draw(); }),
      sl(root, '家中充電電價', 1.5, 8, 0.1, P.home, function (x) { return 'NT$ ' + (+x).toFixed(1) + '/度'; }, function (x) { P.home = x; draw(); }),
      sl(root, '公共快充價格', 5, 20, 0.5, P.pub, function (x) { return 'NT$ ' + (+x).toFixed(1) + '/度'; }, function (x) { P.pub = x; draw(); }),
      sl(root, '在公共快充的比例', 0, 100, 5, P.share, function (x) { return x + '%'; }, function (x) { P.share = x; draw(); }),
      sl(root, '油車油耗', 4, 14, 0.5, P.ice, function (x) { return x + ' L/100 km'; }, function (x) { P.ice = x; draw(); }),
      sl(root, '油價', 20, 45, 0.5, P.gas, function (x) { return 'NT$ ' + (+x).toFixed(1) + '/L'; }, function (x) { P.gas = x; draw(); }),
      sl(root, '每年行駛', 5000, 40000, 1000, P.km, function (x) { return f0(x) + ' km'; }, function (x) { P.km = x; draw(); })];
    root.appendChild(v); inf = info(root);
    function draw() { var loss = 1.1, price = P.home * (1 - P.share / 100) + P.pub * P.share / 100, e100 = P.ev * loss * price, g100 = P.ice * P.gas, ey = e100 * P.km / 100, gy = g100 * P.km / 100;
      var mx = Math.max(ey, gy) * 1.15, W = 680, g = '', bw = 520;
      [['電動車', ey, BL], ['油車', gy, OR]].forEach(function (r, i) { var y = 20 + i * 52, w = r[1] / mx * bw; g += tx(8, y + 22, r[0], 13, 'currentColor', 'start') + '<rect x="70" y="' + y + '" width="' + n1(w) + '" height="32" rx="4" fill="' + r[2] + '"/>' + tx(78 + w, y + 21, 'NT$ ' + f0(r[1]) + '／年', 12, 'currentColor', 'start'); });
      v.innerHTML = svgw('0 0 ' + W + ' 128', g);
      var d = gy - ey;
      inf.innerHTML = '平均電價約 NT$ ' + price.toFixed(1) + '/度（含約 10% 的充電損失）。每 100 km：電動車約 <b>NT$ ' + f0(e100) + '</b>，油車約 <b>NT$ ' + f0(g100) + '</b>。' +
        '<br>每年 ' + f0(P.km) + ' km：' + (d > 0 ? '電動車的能源費用約<b>省下 NT$ ' + f0(d) + '</b>，十年約 NT$ ' + f0(d * 10) + '。' : '<b>電動車的能源費用反而較高</b>（' + f0(-d) + ' 元／年）——常在主要依賴公共快充時發生。') +
        '<br>試試把「公共快充比例」調到 100%：<b>能不能在家充電</b>，是電動車使用成本最大的變數之一。' +
        note('只比較能源費用；未計入車價、保險、稅費（台灣的電動車牌照稅與燃料費目前有減免或不同的規定，請查詢最新規定）、保養與殘值。電價與油價請依實際費率調整。');
    }
    us.forEach(function (u) { u(); }); }

  /* ---------- 衰退 ---------- */
  function initDeg(root, cfg) { head(root, cfg.q); var P = { chem: 'nmc', T: 25, fc: 20, top: 80, km: 15000 }, v = el('div'), inf;
    bar(root, '電池：', [['三元鋰（NMC）', 'nmc'], ['磷酸鋰鐵（LFP）', 'lfp']], function () { return P.chem; }, function (k) { P.chem = k; draw(); });
    bar(root, '平時充電上限：', [['60%', 60], ['80%', 80], ['90%', 90], ['每天充滿 100%', 100]], function () { return P.top; }, function (k) { P.top = k; draw(); });
    var us = [
      sl(root, '平均電池溫度（環境與停車條件）', 10, 40, 1, P.T, function (x) { return x + ' °C'; }, function (x) { P.T = x; draw(); }),
      sl(root, '直流快充佔充電的比例', 0, 100, 5, P.fc, function (x) { return x + '%'; }, function (x) { P.fc = x; draw(); }),
      sl(root, '每年行駛', 5000, 50000, 1000, P.km, function (x) { return f0(x) + ' km'; }, function (x) { P.km = x; draw(); })];
    root.appendChild(v); inf = info(root);
    function cap(y, p) { var lfp = p.chem === 'lfp', fT = Math.pow(2, (p.T - 25) / 10), fS = lfp ? { 60: 0.9, 80: 1, 90: 1.05, 100: 1.15 }[p.top] : { 60: 0.8, 80: 1, 90: 1.15, 100: 1.45 }[p.top];
      var cal = (lfp ? 1.8 : 2.4) * fT * fS * Math.sqrt(y), efc = p.km * y * 0.16 / 70, cyc = efc * (lfp ? 0.0035 : 0.009) * (1 + p.fc / 100 * (lfp ? 0.5 : 0.9)) * (p.T > 35 ? 1.3 : 1);
      return Math.max(40, 100 - cal - cyc); }
    function draw() { var A = [], B = [], y80 = null, y70 = null, base = { chem: P.chem, T: 25, fc: 0, top: 80, km: P.km };
      for (var y = 0; y <= 15.001; y += 0.25) { var c = cap(y, P); A.push([y, c]); B.push([y, cap(y, base)]); if (y80 === null && c < 80) y80 = y; if (y70 === null && c < 70) y70 = y; }
      var c8 = cap(8, P);
      v.innerHTML = chart(680, 260, [{ d: B, c: GY, n: '溫和使用（25°C、80%、不快充）', dash: '5 4' }, { d: A, c: P.chem === 'lfp' ? GN : BL, n: '目前條件', w: 2.5 }], { x0: 0, x1: 15, y0: 50, y1: 100, xl: '年', yl: '剩餘容量 %', hl: [{ y: 80, c: OR, n: '80%' }, { y: 70, c: RD, n: '70%（常見保固門檻）' }], pts: [{ x: 8, y: c8, c: RD, n: Math.round(c8) + '%' }] });
      inf.innerHTML = '8 年後（約 ' + f0(P.km * 8) + ' km）剩餘容量約 <b>' + Math.round(c8) + '%</b>；' + (y80 !== null ? '約第 <b>' + f1(y80) + '</b> 年降到 80%' : '15 年內不會降到 80%') + (y70 !== null ? '，約第 ' + f1(y70) + ' 年降到 70%。' : '。') +
        '<br>衰退有兩個來源：<b>日曆老化</b>（就算不開也會老，受溫度與停放時的電量影響）與<b>循環老化</b>（充放電的次數，快充會加速）。在台灣，<b>高溫</b>常是最重要的因素。' +
        note('高度簡化的經驗模型，參數只用來呈現趨勢；實際的衰退取決於電芯設計、電池管理系統與熱管理，個體差異很大。許多電動車的電池保固約 8 年、保證容量約 70%，條件依車廠而異。');
    }
    us.forEach(function (u) { u(); }); }

  var INIT = { range: initRange, charge: initCharge, cost: initCost, degrade: initDeg };
  function boot() { document.querySelectorAll('.bt-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🔋", note=BT_NOTE):
    return make_with(icon, note, [("bt-w", BTLIB)])


lesson = make()
