# -*- coding: utf-8 -*-
"""〈氣候變遷〉（clm_）共用：課程包裝與 CLLIB 互動元件（class="cl-w"）。

  history  1850 年以來的二氧化碳濃度與全球溫度
  ebm      平衡氣候敏感度：二氧化碳、敏感度、氣膠 → 長期平衡暖化
  budget   排放路徑與碳預算：何時達到淨零 → 峰值暖化
"""
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

CL_NOTE = (u"本課程以政府間氣候變遷專門委員會（IPCC）的評估報告與主要科學機構的資料為基礎；數字為大約值，會隨新的觀測與研究更新。"
           u"互動工具為簡化的教學模型，不是氣候預測。")
F = D


def clw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("cl-w", cfg)


CLLIB = r"""
(function () {
  if (window.__clLib) return; window.__clLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function note(s) { return '<br><span style="color:var(--text-muted);font-size:0.9em">' + s + '</span>'; }

  /* ---------- 歷史 ---------- */
  var CO2 = [[1850, 285], [1870, 288], [1890, 294], [1900, 296], [1910, 300], [1920, 303], [1930, 307], [1940, 311], [1950, 311], [1958, 315], [1960, 317], [1970, 326], [1980, 339], [1990, 354], [2000, 369], [2010, 390], [2015, 401], [2020, 414], [2024, 424]];
  var TMP = [[1850, -0.05], [1860, -0.05], [1870, 0], [1880, -0.05], [1890, -0.1], [1900, 0], [1910, -0.15], [1920, -0.02], [1930, 0.08], [1940, 0.25], [1950, 0.12], [1960, 0.2], [1970, 0.22], [1980, 0.4], [1990, 0.55], [2000, 0.7], [2005, 0.85], [2010, 0.95], [2015, 1.1], [2016, 1.2], [2020, 1.25], [2023, 1.45], [2024, 1.55]];
  function initHistory(root, cfg) { head(root, cfg.q); var v = el('div'), inf; root.appendChild(v); inf = info(root);
    v.innerHTML = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:6px"><div>' +
      chart(340, 230, [{ d: CO2, c: OR, n: '二氧化碳濃度（ppm）', w: 2.5 }], { x0: 1850, x1: 2025, y0: 260, y1: 440, xl: '年', hl: [{ y: 280, c: GY, n: '工業革命前 ~280' }] }) + '</div><div>' +
      chart(340, 230, [{ d: TMP, c: RD, n: '全球溫度變化（°C，相對 1850–1900）', w: 2.5 }], { x0: 1850, x1: 2025, y0: -0.4, y1: 1.8, xl: '年', hl: [{ y: 1.5, c: GY, n: '1.5°C' }, { y: 0, c: GY, n: '' }] }) + '</div></div>';
    inf.innerHTML = '二氧化碳濃度從工業革命前約 <b>280 ppm</b>，上升到 2024 年約 <b>424 ppm</b>（增加約 50%），是至少 80 萬年來最高。同一時期，全球平均溫度上升了約 <b>1.3°C</b>（長期平均）；2024 年是有紀錄以來最熱的一年，也是第一個全年平均超過 1.5°C 的年份。' +
      '<br>注意溫度曲線的<b>起伏</b>：聖嬰、火山爆發等自然變化讓單一年份上下波動，但長期的趨勢很清楚（第 8 課）。' +
      note('數值為多個資料集（冰芯、夏威夷莫納羅亞觀測站、各大溫度資料集）的大約值，並經過簡化；精確的數字依資料集而略有不同。');
  }

  /* ---------- 能量平衡 ---------- */
  function initEBM(root, cfg) { head(root, cfg.q); var P = { c: 420, s: 3, a: -1.1, o: 1.6 }, v = el('div'), inf;
    var us = [slider(root, '二氧化碳濃度', 180, 1200, 10, P.c, function (x) { return x + ' ppm'; }, null, function (x) { P.c = x; draw(); }),
      slider(root, '平衡氣候敏感度（二氧化碳加倍的暖化）', 1.5, 6, 0.5, P.s, function (x) { return x + ' °C'; }, null, function (x) { P.s = x; draw(); }),
      slider(root, '其他溫室氣體與臭氧（輻射強迫）', 0, 3, 0.1, P.o, function (x) { return '+' + (Math.round(x * 10) / 10) + ' W/m²'; }, null, function (x) { P.o = x; draw(); }),
      slider(root, '氣膠的遮蔽（輻射強迫）', -2, 0, 0.1, P.a, function (x) { return (Math.round(x * 10) / 10) + ' W/m²'; }, null, function (x) { P.a = x; draw(); })];
    root.appendChild(v); inf = info(root);
    function dT(c, s, a) { return s / 3.7 * (5.35 * Math.log(c / 280) + a + P.o); }
    function draw() { var A = [], LO = [], HI = []; for (var c = 180; c <= 1200; c += 10) { A.push([c, dT(c, P.s, P.a)]); LO.push([c, dT(c, 2.5, P.a)]); HI.push([c, dT(c, 4, P.a)]); }
      var t = dT(P.c, P.s, P.a), f = 5.35 * Math.log(P.c / 280);
      v.innerHTML = chart(680, 260, [{ d: LO, c: GY, n: 'IPCC「可能」範圍下緣（2.5°C）', dash: '5 4' }, { d: HI, c: GY, n: '上緣（4°C）', dash: '2 3' }, { d: A, c: RD, n: '目前設定', w: 2.5 }], { x0: 180, x1: 1200, y0: -4, y1: 12, xl: '二氧化碳濃度（ppm）', yl: '平衡暖化 °C', vl: [{ x: 280, c: GY, n: '280' }, { x: 560, c: GY, n: '加倍' }], pts: [{ x: P.c, y: t, c: RD, n: (t >= 0 ? '+' : '') + f1(t) + '°C' }] });
      inf.innerHTML = '二氧化碳 ' + P.c + ' ppm 帶來的輻射強迫約 <b>' + f1(f) + ' W/m²</b>（F = 5.35 × ln(C/280)）；加上其他溫室氣體 +' + f1(P.o) + '、氣膠 ' + (Math.round(P.a * 10) / 10) + ' W/m²，長期的<b>平衡暖化</b>約 <b>' + f1(t) + '°C</b>。' +
        (P.c >= 400 && P.c <= 440 ? '<br>目前實際觀測到的暖化約 1.3°C，比平衡值低——因為海洋還在持續吸熱，地表的暖化會<b>落後</b>（第 5 課）。' : '') +
        '<br>注意曲線是<b>對數</b>的：每增加一倍二氧化碳，暖化增加的量大約相同。這也是氣候敏感度用「加倍」來定義的原因（第 17 課）。' +
        '<br>氣膠（空氣汙染中的微粒）會反射陽光、遮蔽部分的暖化。空氣變乾淨後，這層遮蔽會減少——這是減碳時常被忽略的一個效應。' +
        (P.c <= 200 ? '<br>冰期的二氧化碳約 180～190 ppm（試著把其他溫室氣體與氣膠都調到 0）。只看二氧化碳，降溫約 2°C；實際的冰期全球降溫約 4～7°C，因為還有冰原反照率等回饋（第 11 課）。' : '') +
        note('教學模型：其他溫室氣體與氣膠的預設值接近 IPCC 第六次評估對目前輻射強迫的估計（約 +1.6 與 −1.1 W/m²），改變二氧化碳時它們保持不變；「平衡」指海洋與大氣充分調整後的溫度，實際暖化會落後數十年到數百年。');
    }
    us.forEach(function (u) { u(); }); }

  /* ---------- 碳預算 ---------- */
  function initBudget(root, cfg) { head(root, cfg.q); var P = { p: 2030, z: 2070 }, v = el('div'), inf, E0 = 42, T0 = 1.4, K = 0.6;
    var us = [slider(root, '排放持平到哪一年開始下降', 2025, 2045, 1, P.p, function (x) { return x + ' 年'; }, null, function (x) { P.p = x; draw(); }),
      slider(root, '哪一年達到淨零排放', 2035, 2100, 1, P.z, function (x) { return x + ' 年'; }, null, function (x) { P.z = x; draw(); })];
    root.appendChild(v); inf = info(root);
    function draw() { var z = Math.max(P.z, P.p + 1), E = [], T = [], cum = 0, y15 = null, y20 = null;
      for (var y = 2025; y <= 2100; y++) { var e = y <= P.p ? E0 : y >= z ? 0 : E0 * (z - y) / (z - P.p); E.push([y, e]); cum += e; var t = T0 + K * cum / 1000; T.push([y, t]); if (y15 === null && t >= 1.5) y15 = y; if (y20 === null && t >= 2) y20 = y; }
      var pk = T0 + K * cum / 1000;
      v.innerHTML = '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:6px"><div>' +
        chart(340, 220, [{ d: E, c: OR, n: '年排放（十億公噸 CO₂）', w: 2.5 }], { x0: 2025, x1: 2100, y0: 0, y1: 50, xl: '年' }) + '</div><div>' +
        chart(340, 220, [{ d: T, c: RD, n: '暖化（°C）', w: 2.5 }], { x0: 2025, x1: 2100, y0: 1, y1: 3.2, xl: '年', hl: [{ y: 1.5, c: GN, n: '1.5°C' }, { y: 2, c: OR, n: '2°C' }] }) + '</div></div>';
      inf.innerHTML = '從 2025 年到淨零，累積排放約 <b>' + Math.round(cum * 10).toLocaleString('en-US') + ' 億公噸 CO₂</b>（約 ' + (Math.round(cum / 10) / 100) + ' 兆公噸），暖化在淨零時大約停在 <b>' + f1(pk) + '°C</b>。' +
        (y15 ? '<br>約在 <b>' + y15 + ' 年</b>超過 1.5°C' : '<br>沒有超過 1.5°C') + (y20 ? '，約在 <b>' + y20 + ' 年</b>超過 2°C。' : '。') +
        '<br>關鍵觀念：暖化大致與<b>累積</b>的二氧化碳排放成正比。排放降到<b>淨零</b>，暖化才會停止；只是「減少」排放，暖化仍會繼續（第 30 課）。目前全球每年排放約 400 多億公噸，以這個速度，1.5°C 的剩餘預算只剩幾年。' +
        note('教學模型：以約每 1 兆公噸 CO₂ 增加 0.6°C（包含其他溫室氣體的大致效果）粗略校準到 IPCC 與 2025 年更新的剩餘碳預算；起點約 1.4°C。真實的不確定性很大。');
    }
    us.forEach(function (u) { u(); }); }

  var INIT = { history: initHistory, ebm: initEBM, budget: initBudget };
  function boot() { document.querySelectorAll('.cl-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🌡️", note=CL_NOTE):
    return make_with(icon, note, [("cl-w", CLLIB)])


lesson = make()

HISTORY = clw("history", u"1850 年以來的二氧化碳濃度與全球溫度：")
EBM = clw("ebm", u"二氧化碳與長期平衡暖化：")
BUDGET = clw("budget", u"排放路徑與碳預算：什麼時候達到淨零，暖化會停在哪裡？")
