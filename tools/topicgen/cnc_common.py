# -*- coding: utf-8 -*-
"""〈癌症：從細胞到免疫療法〉（cnc_）共用：課程包裝與 CNCLIB 互動元件（class="cnc-w"）。

  growth  腫瘤生長：倍增時間、指數與岡珀茲模型、從一個細胞到可偵測與致命的時間
  twohit  努森的二次打擊：遺傳型與偶發型視網膜母細胞瘤的累積發病曲線
  screen  篩檢的貝氏計算：盛行率、敏感度、特異度 → 陽性預測值
  resist  抗藥性演化：敏感與抗藥細胞在連續給藥與適應性治療下的消長
  lead    存活率的陷阱：領先時間偏差與過度診斷如何讓存活率「看起來」變好
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

CNC_NOTE = u"本課程為科普與教育用途，不能取代醫療建議；有任何健康問題，請諮詢醫師。互動模擬為教學用的簡化模型。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def cw(cfg, maxw=680):
    return wdg("cnc-w", cfg, maxw)


CNCLIB = r"""
(function () {
  if (window.__cncLib) return; window.__cncLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }

  function initGrowth(root, cfg) {
    head(root, cfg.q); var P = { td: 100, gz: 0 }, view = el('div'), inf;
    var b = bar(root); [['指數成長', 0], ['岡珀茲成長（越大越慢）', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.gz = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    var u = slider(root, '倍增時間（天）', 20, 400, 5, P.td, function (x) { return x + ' 天'; }, null, function (x) { P.td = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var d = [], K = 13, r = Math.LN2 / P.td, tdet = null, tdie = null, Y = 25;
      for (var t = 0; t <= Y * 365; t += 10) { var l; if (!P.gz) l = t * r / Math.LN10; else { var a = r / (K * Math.LN10) * 1.6; l = K * (1 - Math.exp(-a * t)); }
        d.push([t / 365, Math.min(l, 13)]); if (tdet === null && l >= 9) tdet = t; if (tdie === null && l >= 12) tdie = t; }
      view.innerHTML = chart(640, 250, [{ d: d, c: RD, n: 'log₁₀（腫瘤細胞數）', w: 2.4 }], { x0: 0, x1: Y, y0: 0, y1: 13, xl: '從第一個癌細胞開始的年數', hl: [{ y: 9, c: OR, n: '約 10 億個細胞 ≈ 1 公分：影像可偵測' }, { y: 12, c: PU, n: '約 1 兆個細胞 ≈ 1 公斤：常致命' }] });
      function yr(t) { return t === null ? '超過 ' + Y + ' 年' : f1(t / 365) + ' 年'; }
      inf.innerHTML = '從一個細胞長到可以被偵測的 1 公分，需要約 <b>30 次倍增</b>（2<sup>30</sup> ≈ 10 億）——以倍增時間 ' + P.td + ' 天計，約 <b>' + yr(tdet) + '</b>；長到約 1 公斤，再 10 次倍增，約 <b>' + yr(tdie) + '</b>。' +
        '<br>關鍵的啟示：一個「剛被發現」的腫瘤，其實已經存在了很多年，經歷了它一生中<b>四分之三</b>的倍增。從偵測到致命，往往只剩最後的十次倍增。' +
        (P.gz ? '<br><b>岡珀茲曲線</b>：真實的腫瘤長大後，血液供應與空間不足，生長逐漸變慢——這也讓大腫瘤對化療較不敏感（分裂中的細胞比例較低）。' : '') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">不同癌症的倍增時間差異極大：從數週（某些白血病、淋巴瘤）到數年（某些攝護腺癌）。</span>'; }
    u();
  }

  function initTwohit(root, cfg) {
    head(root, cfg.q); var P = { m: 0.5 }, view = el('div'), inf;
    var u = slider(root, '突變發生的速率（相對值）', 0.1, 2, 0.05, P.m, function (x) { return f2(x); }, null, function (x) { P.m = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var h = [], s = [], a = 0.45 * P.m, bq = 0.0045 * P.m * P.m;
      for (var t = 0; t <= 10.001; t += 0.1) { h.push([t, 100 * (1 - Math.exp(-a * t))]); s.push([t, 100 * 0.012 * (1 - Math.exp(-bq * 12 * t * t))]); }
      var hs = h.map(function (p) { return [p[0], p[1] / Math.max(1e-9, h[h.length - 1][1]) * 100]; }), ss = s.map(function (p) { return [p[0], p[1] / Math.max(1e-9, s[s.length - 1][1]) * 100]; });
      view.innerHTML = chart(640, 240, [{ d: hs, c: RD, n: '遺傳型：已帶一個突變，只需再一次「打擊」', w: 2.4 }, { d: ss, c: BL, n: '偶發型：同一個細胞需要兩次打擊', w: 2.4 }], { x0: 0, x1: 10, y0: 0, y1: 105, xl: '年齡（歲）', yl: '已發病者的累積比例（%）' });
      inf.innerHTML = '1971 年，努森比較了<b>視網膜母細胞瘤</b>（一種兒童眼癌）的發病年齡：遺傳型的孩子發病早，累積曲線一開始就<b>直線上升</b>（只需要一次事件）；偶發型的孩子發病晚，曲線<b>先平後陡</b>（像 t² 一樣——需要兩次獨立的事件同時發生在同一個細胞）。' +
        '<br>他由此推論：這個基因（後來發現是 <b>RB1</b>）的<b>兩個拷貝都必須失去</b>，癌症才會發生——遺傳型的孩子天生就少了一個。這是抑癌基因的第一個模型，也解釋了為什麼遺傳型常常<b>兩眼</b>都發病。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">兩條曲線都以 10 歲時的累積人數為 100%，只比較形狀。</span>'; }
    u();
  }

  var SP = [['乳房攝影（示意）', 0.005, 0.85, 0.9], ['糞便潛血檢查（示意）', 0.005, 0.7, 0.93], ['高風險族群的低劑量 CT（示意）', 0.01, 0.9, 0.8], ['自訂', null]];
  function initScreen(root, cfg) {
    head(root, cfg.q); var P = { p: 0.005, se: 0.85, sp: 0.9 }, view = el('div'), inf, us;
    var b = bar(root); SP.forEach(function (o, i) { if (!o[1]) return; var x = btn(o[0], i); x.onclick = function () { set(o); mark(b, i); }; b.appendChild(x); }); mark(b, 0);
    us = [slider(root, '盛行率（受檢者中真的有癌症的比例）', 0.0005, 0.05, 0.0005, P.p, function (x) { return f2(x * 100) + '%'; }, 'p', function (x) { P.p = x; draw(); }),
      slider(root, '敏感度（有癌症時檢查陽性的機率）', 0.5, 0.99, 0.01, P.se, function (x) { return Math.round(x * 100) + '%'; }, 'se', function (x) { P.se = x; draw(); }),
      slider(root, '特異度（沒有癌症時檢查陰性的機率）', 0.7, 0.999, 0.001, P.sp, function (x) { return f1(x * 100) + '%'; }, 'sp', function (x) { P.sp = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function set(o) { [['p', o[1]], ['se', o[2]], ['sp', o[3]]].forEach(function (kv, i) { root.querySelector('input[data-k="' + kv[0] + '"]').value = kv[1]; us[i](); }); }
    function draw() { var N = 10000, sick = N * P.p, tp = sick * P.se, fn = sick - tp, fp = (N - sick) * (1 - P.sp), tn = N - sick - fp, ppv = tp / (tp + fp), g = '', W = 640;
      var parts = [['真陽性', tp, RD], ['偽陰性', fn, OR], ['偽陽性', fp, BL], ['真陰性', tn, '#cfd8e3']], x = 20;
      parts.forEach(function (p) { var w = Math.max(p[1] > 0 ? 2 : 0, p[1] / N * 600); g += '<rect x="' + n1(x) + '" y="20" width="' + n1(w) + '" height="40" fill="' + p[2] + '"/>'; x += w; });
      var pos = tp + fp, w1 = tp / Math.max(1e-9, pos) * 600; g += tx(20, 82, '檢查結果是陽性的人：', 11, 'currentColor', 'start') + '<rect x="20" y="90" width="' + n1(w1) + '" height="34" fill="' + RD + '"/><rect x="' + n1(20 + w1) + '" y="90" width="' + n1(600 - w1) + '" height="34" fill="' + BL + '"/>' +
        tx(26, 112, '真的有癌症 ' + Math.round(tp), 11, '#fff', 'start') + tx(614, 112, '其實沒有 ' + Math.round(fp), 11, '#fff', 'end');
      view.innerHTML = svgw('0 0 ' + W + ' 135', g);
      inf.innerHTML = '一萬人接受篩檢：其中約 <b>' + Math.round(sick) + '</b> 人真的有癌症。檢查陽性的人共約 <b>' + Math.round(pos) + '</b> 人，其中真的有癌症的只有 <b>' + Math.round(tp) + '</b> 人。' +
        '<br>所以，<b>篩檢陽性時，真的有癌症的機率（陽性預測值）只有約 ' + f1(ppv * 100) + '%</b>。陰性時沒有癌症的機率約 ' + f2(tn / (tn + fn) * 100) + '%。' +
        '<br>原因是：在一般人中，癌症很<b>罕見</b>，即使特異度很高，少數的偽陽性乘上龐大的健康人數，仍然比真陽性多。所以篩檢陽性，下一步是<b>進一步檢查確認</b>，不必過度驚慌——但也一定不能忽略。（這就是貝氏定理，見〈貝氏統計〉。）'; }
    us.forEach(function (u) { u(); });
  }

  function initResist(root, cfg) {
    head(root, cfg.q); var P = { m: 0, k: 0.6 }, view = el('div'), inf;
    var b = bar(root); [['連續給藥（最大劑量）', 0], ['適應性治療（腫瘤縮小就暫停）', 1], ['不治療', 2]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.m = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    var u = slider(root, '藥物對敏感細胞的殺傷力', 0.1, 1, 0.05, P.k, function (x) { return f2(x); }, null, function (x) { P.k = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var S = 1e9 * (1 - 1e-5), R = 1e9 * 1e-5, K = 1e12, rs = 0.03, rr = 0.025, ds = [], dr = [], dt = [], on = P.m === 0, t0 = null, N0 = S + R;
      for (var t = 0; t <= 900; t++) { var N = S + R, f = 1 - N / K;
        if (P.m === 1) { if (N > N0) on = true; if (N < N0 * 0.5) on = false; } var kill = (P.m === 2 || !on) ? 0 : P.k * 0.1;
        S += S * (rs * f - kill); R += R * (rr * f); S = Math.max(S, 1); if (t % 5 === 0) { ds.push([t, Math.log10(S)]); dr.push([t, Math.log10(R)]); dt.push([t, Math.log10(S + R)]); }
        if (t0 === null && t > 30 && S + R > N0 * 2) t0 = t; }
      view.innerHTML = chart(640, 250, [{ d: dt, c: '#333', n: '腫瘤總數', w: 2.6 }, { d: ds, c: BL, n: '對藥物敏感的細胞', w: 1.6 }, { d: dr, c: RD, n: '抗藥的細胞', w: 1.6 }], { x0: 0, x1: 900, y0: 0, y1: 12.5, xl: '天數', yl: 'log₁₀（細胞數）', hl: [{ y: 9, c: OR, n: '開始治療時的大小' }] });
      inf.innerHTML = '開始治療時，十億個癌細胞中，只有約一萬個天生帶有<b>抗藥突變</b>。' +
        (P.m === 0 ? '連續給藥時，敏感的細胞被大量殺死，腫瘤迅速縮小——但這也<b>清除了抗藥細胞的競爭者</b>。抗藥細胞接管了腫瘤，' + (t0 ? '約在第 <b>' + t0 + '</b> 天長回治療前的兩倍大' : '最後捲土重來') + '，而且這次藥物完全無效。' :
          P.m === 1 ? '<b>適應性治療</b>：腫瘤縮小到一半就暫停用藥，長回原來大小再用。保留一部分敏感的細胞，讓它們與抗藥細胞<b>競爭</b>空間與資源，延緩抗藥細胞的接管。' + (t0 ? '腫瘤約在第 ' + t0 + ' 天才超過兩倍。' : '在這段期間內，腫瘤被控制在一定的大小。') :
          '不治療時，腫瘤持續成長，敏感細胞始終佔絕大多數。') +
        '<br>這就是「治療選擇出抗藥性」的演化原理——與細菌的抗生素抗藥性相同。對策包括：多種藥物合併（同時對多個抗藥突變都有抗性的機率極低）、追蹤抗藥突變、以及這種仍在研究中的適應性治療。';
    }
    u();
  }

  function initLead(root, cfg) {
    head(root, cfg.q); var P = { L: 2, od: 0 }, view = el('div'), inf;
    var us = [slider(root, '篩檢讓診斷提早了幾年（領先時間）', 0, 5, 0.25, P.L, function (x) { return x + ' 年'; }, null, function (x) { P.L = x; draw(); }),
      slider(root, '篩檢找到的「永遠不會致命」的病例比例（過度診斷）', 0, 0.6, 0.05, P.od, function (x) { return Math.round(x * 100) + '%'; }, null, function (x) { P.od = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var m = 3, lam = Math.LN2 / m, a = [], b = []; function s0(t) { return Math.exp(-lam * t); }
      function s1(t) { var real = t < P.L ? 1 : s0(t - P.L); return (1 - P.od) * real + P.od * 1; }
      for (var t = 0; t <= 12.001; t += 0.1) { a.push([t, 100 * s0(t)]); b.push([t, 100 * s1(t)]); }
      var f0 = s0(5), f1v = s1(5);
      view.innerHTML = chart(640, 240, [{ d: a, c: BL, n: '有症狀才診斷', w: 2.2 }, { d: b, c: RD, n: '篩檢時診斷', w: 2.2 }], { x0: 0, x1: 12, y0: 0, y1: 105, xl: '從「診斷」開始的年數', yl: '存活率（%）', vl: [{ x: 5, c: GY, n: '五年' }] });
      inf.innerHTML = '五年存活率：有症狀才診斷 <b>' + Math.round(f0 * 100) + '%</b>，篩檢時診斷 <b>' + Math.round(f1v * 100) + '%</b>。' +
        '<br>但在這個模擬中，篩檢<b>完全沒有改變任何一個人的死亡時間</b>！' + (P.L > 0 ? '存活率提高，只是因為診斷的時間點提早了 ' + P.L + ' 年——「計時器」提早開始了。這叫<b>領先時間偏差</b>。' : '') + (P.od > 0 ? '再加上篩檢找到了許多永遠不會致命的「癌症」，它們全都「存活」，讓存活率進一步膨脹——這是<b>過度診斷</b>。' : '') +
        '<br>所以，判斷篩檢是否真的有效，要看<b>死亡率</b>（每十萬人中死於該癌症的人數）有沒有下降，最好是用隨機對照試驗——而不是看存活率。'; }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.cnc-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ growth: initGrowth, twohit: initTwohit, screen: initScreen, resist: initResist, lead: initLead })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🎗️", CNC_NOTE, CNCLIB, "cnc-w")

GROWTH = cw({"t": "growth", "q": u"腫瘤生長：從一個細胞到一個腫瘤"})
TWOHIT = cw({"t": "twohit", "q": u"努森的二次打擊：為什麼遺傳型發病比較早"})
SCREEN = cw({"t": "screen", "q": u"篩檢陽性，真的有癌症的機率是多少"})
RESIST = cw({"t": "resist", "q": u"抗藥性：治療如何選擇出抗藥的細胞"})
LEAD = cw({"t": "lead", "q": u"存活率的陷阱：領先時間偏差與過度診斷"})
