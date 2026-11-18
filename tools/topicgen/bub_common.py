# -*- coding: utf-8 -*-
"""〈金融泡沫與危機史〉（bub_）共用：課程包裝與 BUBLIB 互動元件（class="bub-w"）。

  lev     槓桿：價格下跌多少就會賠光
  run     銀行擠兌：恐慌的傳染與存款保險
  bubble  泡沫模擬：基本面投資人與追漲投資人
  crash   歷次崩盤的跌幅比較
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

BUB_NOTE = u"本課程為歷史與經濟學的教育內容，不構成任何投資建議。互動模擬為教學用的簡化模型。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def bw(cfg, maxw=680):
    return wdg("bub-w", cfg, maxw)


BUBLIB = r"""
(function () {
  if (window.__bubLib) return; window.__bubLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }

  function initLev(root, cfg) {
    head(root, cfg.q); var P = { L: 5, d: -10 }, view = el('div'), inf;
    var us = [slider(root, '槓桿倍數（總部位 ÷ 自有資金）', 1, 40, 1, P.L, function (x) { return x + ' 倍'; }, null, function (x) { P.L = x; draw(); }),
      slider(root, '資產價格的變化', -50, 50, 1, P.d, function (x) { return (x > 0 ? '+' : '') + x + '%'; }, null, function (x) { P.d = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var L = P.L, eq = 100, pos = eq * L, debt = pos - eq, pos2 = pos * (1 + P.d / 100), eq2 = pos2 - debt, r = eq2 / eq - 1, wipe = 100 / L, g = '';
      var sc = 1.6, base = 200, x0 = 60, w = 150;
      function barr(x, h, c, t) { var y = h >= 0 ? base - h * sc : base; g += '<rect x="' + x + '" y="' + n1(y) + '" width="' + w + '" height="' + n1(Math.abs(h) * sc) + '" fill="' + c + '"/>' + tx(x + w / 2, h >= 0 ? y - 6 : y + Math.abs(h) * sc + 14, t, 11); }
      barr(x0, 100, BL, '自有資金 100'); barr(x0 + 200, Math.max(-60, Math.min(110, eq2)), eq2 >= 0 ? GN : RD, '變化後 ' + Math.round(eq2));
      g += ln(40, base, 600, base, '#999') + tx(500, 60, '總部位 ' + Math.round(pos) + '（借款 ' + Math.round(debt) + '）', 11, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 640 260', g);
      inf.innerHTML = '用 100 元自有資金，借錢買進 ' + Math.round(pos) + ' 元的資產（' + L + ' 倍槓桿）。價格 ' + (P.d >= 0 ? '上漲' : '下跌') + ' ' + Math.abs(P.d) + '%，你的資金變成 <b>' + Math.round(eq2) + '</b>，報酬率 <b style="color:' + (r >= 0 ? GN : RD) + '">' + (r >= 0 ? '+' : '') + Math.round(r * 100) + '%</b>。' +
        '<br>槓桿把漲跌都放大 ' + L + ' 倍：價格只要下跌 <b>' + f1(wipe) + '%</b>，本金就全部賠光' + (eq2 < 0 ? '，而且還<b>倒欠</b> ' + Math.round(-eq2) + ' 元' : '') + '。在真實市場中，跌到一定程度時券商就會「追繳保證金」或強制賣出——大家同時被迫賣出，價格跌得更兇。'; }
    us.forEach(function (u) { u(); });
  }

  function initRun(root, cfg) {
    head(root, cfg.q); var P = { r: 15, p: 8, ins: 0 }, view = el('div'), inf;
    var us = [slider(root, '銀行手上的現金準備（存款的 %）', 5, 50, 1, P.r, function (x) { return x + '%'; }, null, function (x) { P.r = x; draw(); }),
      slider(root, '第一天恐慌提款的存戶', 0, 30, 1, P.p, function (x) { return x + '%'; }, null, function (x) { P.p = x; draw(); })];
    var b = el('div', 'margin:4px 0'), ib = btn('存款保險：無'); ib.onclick = function () { P.ins ^= 1; ib.textContent = '存款保險：' + (P.ins ? '有' : '無'); draw(); }; b.appendChild(ib); root.appendChild(b);
    root.appendChild(view); inf = info(root);
    function draw() { var dep = 100, cash = P.r, sell = 100 - P.r, wd = P.p, days = [], cashS = [], depS = [], failed = null;
      for (var t = 0; t <= 10; t++) { cashS.push([t, cash]); depS.push([t, dep]); if (failed !== null) break;
        var want = Math.min(dep, wd); cash -= want; dep -= want;
        if (cash < 0) { var need = -cash, fire = need / 0.7; if (fire > sell) { failed = t + 1; cash = 0; } else { sell -= fire; cash = 0; } }
        var fear = (100 - dep) / 100; wd = P.ins ? Math.max(0, wd * 0.3) : Math.min(dep, wd * (1 + 1.6 * fear) + fear * 10); }
      view.innerHTML = chart(640, 230, [{ d: depS, c: BL, n: '剩餘存款', w: 2.2 }, { d: cashS, c: GN, n: '手上的現金', w: 2.2 }], { x0: 0, x1: 10, y0: 0, y1: 105, xl: '天', vl: failed !== null ? [{ x: failed, c: RD, n: '倒閉' }] : [] });
      inf.innerHTML = (failed !== null ? '銀行在第 <b>' + failed + '</b> 天倒閉。' : '銀行撐過了這次恐慌。') + '銀行只保留一小部分存款作為現金，其餘借出或投資。當提款的人變多，其他存戶開始擔心「再不領就領不到了」，於是更多人去提款——<b>恐慌會自我實現</b>。銀行被迫低價拋售資產（這裡假設只能拿回七成），損失更大。' +
        (P.ins ? '<br><b>存款保險</b>讓存戶相信錢一定拿得回來，恐慌很快平息。' : '<br>試試打開「存款保險」。') + '<span style="font-size:0.9em;color:var(--text-muted)">（參考戴蒙—迪布維格模型的概念，大幅簡化。）</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initBubble(root, cfg) {
    head(root, cfg.q); var P = { c: 65, seed: 3 }, view = el('div'), inf;
    var us = [slider(root, '追漲投資人的比例', 0, 80, 1, P.c, function (x) { return x + '%'; }, null, function (x) { P.c = x; draw(); })];
    var b = el('div', 'margin:4px 0'), sb = btn('換一組隨機消息'); sb.onclick = function () { P.seed++; draw(); }; b.appendChild(sb); root.appendChild(b);
    root.appendChild(view); inf = info(root);
    function draw() { var s = P.seed * 7919 + 17; function rnd() { s = (s * 16807) % 2147483647; return s / 2147483647; }
      var F = 100, p = [100, 100], c = P.c / 100, f = 1 - c, d = [], fd = [], mx = 100, mn = 100;
      for (var t = 2; t <= 300; t++) { var trend = p[t - 1] - p[t - 2], dev = Math.log(p[t - 1] / F), news = (rnd() - 0.5) * 3;
        var dp = f * 0.06 * (F - p[t - 1]) + c * 2.0 * Math.tanh(trend / 3) * 3 + news + (t > 40 && t < 60 ? 1.5 : 0); var np = Math.max(5, p[t - 1] + dp); p.push(np); mx = Math.max(mx, np); mn = Math.min(mn, np); }
      for (var k = 0; k < p.length; k++) { d.push([k, p[k]]); fd.push([k, F]); }
      view.innerHTML = chart(640, 240, [{ d: fd, c: GY, n: '基本價值', w: 1.4, dash: '5,4' }, { d: d, c: RD, n: '市場價格', w: 2 }], { x0: 0, x1: 300, y0: 0, y1: Math.max(200, mx * 1.05), xl: '時間' });
      inf.innerHTML = '市場上有兩種人：<b>基本面投資人</b>在價格高於價值時賣出、低於時買進，把價格拉回；<b>追漲投資人</b>看到價格上漲就買、下跌就賣。第 40～60 天出現一段好消息。最高價約為基本價值的 <b>' + f1(mx / F) + ' 倍</b>，最低約 <b>' + f1(mn / F) + ' 倍</b>。' +
        '<br>追漲的人越多，好消息就越容易被放大成泡沫，接著崩盤、跌過頭。<span style="font-size:0.9em;color:var(--text-muted)">（異質投資人模型的簡化示意。）</span>'; }
    us.forEach(function (u) { u(); });
  }

  var CR = [['1929 美國股災（道瓊）', 89, 1929, '1929 年 9 月高點到 1932 年 7 月低點。名目上直到 1954 年才回到高點。'], ['1987 黑色星期一（單日）', 22.6, 1987, '道瓊工業指數在一天之內下跌 22.6%，至今仍是最大的單日跌幅。'],
    ['1989 日本泡沫（日經）', 80, 1989, '1989 年底的 38,915 點，到 2009 年的低點下跌約八成；直到 2024 年才回到高點。'], ['1990 台灣股市', 80, 1990, '1990 年 2 月的 12,682 點，八個月內跌到 2,485 點左右。'],
    ['2000 網路泡沫（那斯達克）', 78, 2000, '2000 年 3 月高點到 2002 年 10 月，下跌約 78%；2015 年才回到高點。'], ['2008 金融海嘯（標普 500）', 57, 2008, '2007 年 10 月高點到 2009 年 3 月低點。'],
    ['2021 比特幣', 77, 2021, '2021 年 11 月高點約 6.9 萬美元，到 2022 年 11 月約 1.55 萬美元。之後又再創新高。']];
  function initCrash(root, cfg) {
    head(root, cfg.q); var P = { s: 3 }, view = el('div'), inf; root.appendChild(view); inf = info(root);
    function draw() { var g = '', y0 = 14, h = 30; CR.forEach(function (c, i) { var y = y0 + i * (h + 8), w = c[1] / 100 * 380, on = i == P.s;
        g += '<g data-i="' + i + '" style="cursor:pointer"><rect x="230" y="' + y + '" width="' + n1(w) + '" height="' + h + '" fill="' + (on ? RD : '#e6a49f') + '"/>' + tx(222, y + h / 2 + 4, c[0], 11, 'currentColor', 'end') + tx(236 + w, y + h / 2 + 4, '−' + c[1] + '%', 11, on ? RD : 'currentColor', 'start') + '</g>'; });
      view.innerHTML = svgw('0 0 640 ' + (y0 + CR.length * (h + 8)), g);
      view.querySelectorAll('g[data-i]').forEach(function (e) { e.onclick = function () { P.s = +e.getAttribute('data-i'); draw(); }; });
      var c = CR[P.s]; inf.innerHTML = '<b>' + c[0] + '</b>：從高點下跌約 <b>' + c[1] + '%</b>。' + c[3] + '<br>注意：跌 80% 之後，要<b>漲 400%</b> 才能回到原點。<span style="font-size:0.9em;color:var(--text-muted)">（點選長條；數字為約略值。）</span>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.bub-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ lev: initLev, run: initRun, bubble: initBubble, crash: initCrash })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🫧", BUB_NOTE, BUBLIB, "bub-w")

LEV = bw({"t": "lev", "q": u"槓桿：放大獲利，也放大虧損"})
RUN = bw({"t": "run", "q": u"銀行擠兌：恐慌如何自我實現"})
BUBBLE = bw({"t": "bubble", "q": u"泡沫是怎麼吹起來的：基本面投資人與追漲投資人"})
CRASH = bw({"t": "crash", "q": u"歷次崩盤：從高點下跌了多少"})
