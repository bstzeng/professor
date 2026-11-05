# -*- coding: utf-8 -*-
"""〈藥是怎麼作用的〉（phm_）共用：課程包裝與 PHLIB 互動元件（class="ph-w"）。

  pk   血中濃度模擬：劑量、間隔、半衰期、情境（忘了吃、吃兩倍、肝功能變差、代謝被抑制、負荷劑量）
  dr   劑量—反應曲線：完全致效劑、部分致效劑、競爭型與非競爭型拮抗劑
"""
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

PH_NOTE = (u"本課程為藥理學的科普介紹，不構成醫療建議，也不取代醫師或藥師的指示；任何用藥的開始、調整或停止，都應該與醫療專業人員討論。"
           u"課程以藥物的類別與作用原理為主，不推薦任何品牌或產品；互動工具為簡化的教學模型。")
F = D


def phw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("ph-w", cfg)


PHLIB = r"""
(function () {
  if (window.__phLib) return; window.__phLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root, lab, opts, get, set) { var b = el('div', 'margin:6px 0'); if (lab) b.appendChild(el('span', 'font-size:0.85em;color:var(--text-muted);margin-right:4px', lab)); opts.forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { set(o[1]); mark(b, o[1]); }; b.appendChild(x); }); root.appendChild(b); mark(b, get()); return b; }
  function note(s) { return '<br><span style="color:var(--text-muted);font-size:0.9em">' + s + '</span>'; }

  /* ---------- 血中濃度 ---------- */
  function sim(doses, th, ka, T) { var ke = Math.LN2 / th, out = [];
    for (var t = 0; t <= T + 1e-9; t += 0.25) { var c = 0; doses.forEach(function (d) { var dt = t - d[0]; if (dt >= 0) c += d[1] * ka / (ka - ke) * (Math.exp(-ke * dt) - Math.exp(-ka * dt)); }); out.push([t, c]); } return out; }
  function initPK(root, cfg) { head(root, cfg.q); var P = { th: 6, tau: 8, d: 1, sc: 'n' }, v = el('div'), inf, KA = 1.5, T = 96;
    var us = [slider(root, '半衰期', 1, 48, 1, P.th, function (x) { return x + ' 小時'; }, null, function (x) { P.th = x; draw(); }),
      slider(root, '每隔幾小時吃一次', 4, 24, 2, P.tau, function (x) { return x + ' 小時'; }, null, function (x) { P.tau = x; draw(); }),
      slider(root, '每次劑量', 0.5, 2, 0.25, P.d, function (x) { return '× ' + x; }, null, function (x) { P.d = x; draw(); })];
    bar(root, '情境：', [['正常', 'n'], ['忘了一次', 'miss'], ['想起來補吃兩倍', 'dbl'], ['肝功能變差', 'liver'], ['加上抑制代謝的藥或食物', 'inh'], ['先給負荷劑量', 'load']], function () { return P.sc; }, function (k) { P.sc = k; draw(); });
    root.appendChild(v); inf = info(root);
    var ref = sim((function () { var a = []; for (var t = 0; t <= 200; t += 8) a.push([t, 1]); return a; })(), 6, KA, 200), ss = ref.filter(function (p) { return p[0] > 150; }), avg = ss.reduce(function (s, p) { return s + p[1]; }, 0) / ss.length;
    var MEC = 0.55 * avg, MTC = 1.75 * avg;
    function draw() { var th = P.th * (P.sc === 'liver' ? 2 : P.sc === 'inh' ? 2.5 : 1), doses = [], k = 0;
      for (var t = 0; t <= T; t += P.tau, k++) { var d = P.d; if (P.sc === 'miss' && k === 4) d = 0; if (P.sc === 'dbl' && k === 4) d = 0; if (P.sc === 'dbl' && k === 5) d = 2 * P.d; if (P.sc === 'load' && k === 0) d = P.d * Math.max(1.5, Math.min(4, 1 / (1 - Math.exp(-Math.LN2 / th * P.tau)))); if (d) doses.push([t, d]); }
      var S = sim(doses, th, KA, T), base = P.sc === 'n' ? null : sim((function () { var a = []; for (var t = 0; t <= T; t += P.tau) a.push([t, P.d]); return a; })(), P.th, KA, T);
      var inW = 0, hi = 0, lo = 0; S.forEach(function (p) { if (p[0] < 24) return; if (p[1] > MTC) hi++; else if (p[1] < MEC) lo++; else inW++; }); var n = inW + hi + lo;
      var ser = (base ? [{ d: base, c: GY, n: '正常服用', dash: '5 4' }] : []).concat([{ d: S, c: BL, n: '血中濃度', w: 2.5 }]);
      v.innerHTML = chart(680, 260, ser, { x0: 0, x1: T, y0: 0, y1: Math.max(MTC * 1.5, Math.max.apply(null, S.map(function (p) { return p[1]; })) * 1.1), xl: '小時', hl: [{ y: MTC, c: RD, n: '中毒濃度' }, { y: MEC, c: GN, n: '最低有效濃度' }] });
      var tss = 4.5 * th, msg = { n: '', miss: '<br><b>忘了一次</b>：濃度掉到有效範圍以下一段時間——對抗生素、抗癲癇藥、抗凝血藥這類需要穩定濃度的藥特別重要。', dbl: '<br><b>補吃兩倍</b>：濃度一下子衝高，可能超過中毒濃度。多數藥物的說明是：想起來時如果已經接近下一次的時間，就跳過，不要加倍——但仍應依仿單或藥師的說明。', liver: '<br><b>肝功能變差</b>：藥物分解變慢、半衰期變長，同樣的劑量會越積越高——這是肝腎功能不佳或年長者常需要調整劑量的原因（第 5、29 課）。', inh: '<br><b>代謝被抑制</b>：另一種藥或某些食物（例如葡萄柚）抑制了代謝酵素，效果類似肝功能變差（第 26、27 課）。', load: '<br><b>負荷劑量</b>：第一次先給較大的劑量，讓濃度立刻進入有效範圍，不必等好幾個半衰期——半衰期很長的藥常用這個方法。' }[P.sc];
      inf.innerHTML = '半衰期 ' + f1(th) + ' 小時，每 ' + P.tau + ' 小時一次：大約要 <b>' + f1(tss) + ' 小時</b>（4～5 個半衰期）才會達到穩定狀態。第一天之後，濃度在治療範圍內的時間約 <b>' + Math.round(inW / n * 100) + '%</b>' + (hi ? '，超過中毒濃度約 ' + Math.round(hi / n * 100) + '%' : '') + (lo ? '，低於有效濃度約 ' + Math.round(lo / n * 100) + '%' : '') + '。' + msg +
        '<br>試試：把半衰期調短、間隔拉長，濃度會像鋸齒一樣大起大落；這就是為什麼有些藥一天要吃三次，有些一天一次就夠（第 6 課）。' +
        note('教學模型：口服、一室模型、吸收與排除為一級動力學；有效與中毒濃度是示意的數值。真實的藥物差異很大，劑量請依醫囑。');
    }
    us.forEach(function (u) { u(); }); }

  /* ---------- 劑量—反應 ---------- */
  function initDR(root, cfg) { head(root, cfg.q); var P = { m: 'full', b: 0 }, v = el('div'), inf;
    bar(root, '情境：', [['完全致效劑', 'full'], ['部分致效劑', 'part'], ['加上競爭型拮抗劑', 'comp'], ['加上非競爭型拮抗劑', 'non']], function () { return P.m; }, function (k) { P.m = k; draw(); });
    var u1 = slider(root, '拮抗劑的濃度', 0, 100, 5, P.b, function (x) { return x === 0 ? '無' : '× ' + x; }, null, function (x) { P.b = x; draw(); });
    root.appendChild(v); inf = info(root);
    function E(d, em, ec) { return em * d / (d + ec); }
    function draw() { var A = [], B = [], em = 100, ec = 1;
      if (P.m === 'part') em = 40; if (P.m === 'comp') ec = 1 + P.b; if (P.m === 'non') em = 100 / (1 + P.b / 10);
      for (var x = -3; x <= 3.001; x += 0.05) { var d = Math.pow(10, x); A.push([x, E(d, 100, 1)]); B.push([x, E(d, em, ec)]); }
      v.innerHTML = chart(680, 260, [{ d: A, c: GY, n: '完全致效劑（單獨）', dash: '5 4' }, { d: B, c: P.m === 'part' ? OR : P.m === 'full' ? BL : RD, n: '目前情境', w: 2.5 }], { x0: -3, x1: 3, y0: 0, y1: 105, xl: '劑量（對數刻度：每格 ×10）', yl: '效果 %', hl: [{ y: 50, c: GY, n: '50%' }] });
      var t = { full: '<b>完全致效劑</b>：結合受體後能引起最大的反應。曲線是 S 形：低劑量幾乎沒效果，中間一段效果快速上升，高劑量後再加也不會更有效（飽和），只會增加副作用。', part: '<b>部分致效劑</b>：即使所有受體都被佔滿，也只能產生部分的反應（這裡最多 40%）。它和完全致效劑一起出現時，反而會<b>擋住</b>完全致效劑——某些戒癮治療就利用這個特性。', comp: '<b>競爭型拮抗劑</b>：和藥物搶同一個位置。曲線<b>向右移</b>：需要更高的劑量才有同樣的效果，但只要劑量夠高，仍然能達到最大效果。鴉片類解毒劑就是這樣搶走受體的（第 11 課）。', non: '<b>非競爭型拮抗劑</b>：從別的位置破壞受體的作用。曲線<b>往下壓</b>：再高的劑量也達不到原本的最大效果。' }[P.m];
      inf.innerHTML = t + (P.m === 'comp' || P.m === 'non' ? '' : '<br>拮抗劑的濃度滑桿只在「拮抗劑」情境中有作用。') + note('教學模型：以簡單的結合模型繪製；實際的受體作用常更複雜。');
    }
    u1(); }

  var INIT = { pk: initPK, dr: initDR };
  function boot() { document.querySelectorAll('.ph-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"💊", note=PH_NOTE):
    return make_with(icon, note, [("ph-w", PHLIB)])


lesson = make()

PK = phw("pk", u"血中濃度模擬：劑量、間隔與半衰期")
DR = phw("dr", u"劑量—反應曲線：致效劑與拮抗劑")
