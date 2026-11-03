# -*- coding: utf-8 -*-
"""〈行為經濟學與投資心理〉（bhv_）共用：課程包裝與 BHLIB 互動元件（class="bh-w"）。

  prospect  展望理論：價值函數、機率加權與賭局評估
  quiz      認知偏誤小測驗
  dispo     處分效應自我測驗：賣還是抱？
  mental    心理帳戶情境題
"""
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

BH_NOTE = u"本課程介紹行為經濟學的研究與觀念，不構成任何投資建議；投資有風險，過去的績效不代表未來。互動工具為教學用的簡化模型與情境，不能用來預測市場。"
F = D


def bhw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("bh-w", cfg)


BHLIB = r"""
(function () {
  if (window.__bhLib) return; window.__bhLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function row(root) { var d = el('div', 'margin:4px 0'); root.appendChild(d); return d; }
  function sl(root, lab, mn, mx, st, val, fmt, cb) { return slider(root, lab, mn, mx, st, val, fmt || function (x) { return x; }, null, cb); }
  function money(x) { return (x < 0 ? '−' : '') + Math.abs(Math.round(x)).toLocaleString() + ' 元'; }
  function card(html) { return '<div style="border:1px solid var(--border);border-radius:8px;padding:10px 12px;margin:6px 0;background:var(--surface);line-height:1.7">' + html + '</div>'; }

  /* ---------- 展望理論 ---------- */
  function initProspect(root, cfg) { head(root, cfg.q); var P = { a: 0.88, l: 2.25, g: 0.61, win: 1500, lose: 1000, p: 0.5 }, v = el('div'), inf, us = [];
    us.push(sl(root, '敏感度遞減 α（越小，越「麻木」）', 0.3, 1, 0.01, P.a, function (x) { return (+x).toFixed(2); }, function (x) { P.a = x; draw(); }));
    us.push(sl(root, '損失趨避 λ（損失的痛是獲得的幾倍）', 1, 4, 0.05, P.l, function (x) { return (+x).toFixed(2); }, function (x) { P.l = x; draw(); }));
    us.push(sl(root, '機率扭曲 γ（1 = 不扭曲）', 0.3, 1, 0.01, P.g, function (x) { return (+x).toFixed(2); }, function (x) { P.g = x; draw(); }));
    root.appendChild(el('div', 'margin-top:10px;font-weight:bold;font-size:0.95em', '賭局：擲一次'));
    us.push(sl(root, '贏的機率', 0.01, 0.99, 0.01, P.p, function (x) { return Math.round(x * 100) + '%'; }, function (x) { P.p = x; draw(); }));
    us.push(sl(root, '贏了得到', 100, 5000, 100, P.win, money, function (x) { P.win = x; draw(); }));
    us.push(sl(root, '輸了失去', 100, 5000, 100, P.lose, money, function (x) { P.lose = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function val(x) { return x >= 0 ? Math.pow(x, P.a) : -P.l * Math.pow(-x, P.a); }
    function w(p) { var g = P.g; return Math.pow(p, g) / Math.pow(Math.pow(p, g) + Math.pow(1 - p, g), 1 / g); }
    function draw() { var V = [], L = [], W = [], D = [];
      for (var x = -1000; x <= 1000; x += 10) { V.push([x, val(x) / Math.pow(1000, P.a) * 1000]); L.push([x, x]); }
      for (var p = 0; p <= 1.0001; p += 0.01) { W.push([p * 100, w(Math.min(p, 1)) * 100]); D.push([p * 100, p * 100]); }
      v.innerHTML = '<div style="display:flex;flex-wrap:wrap;gap:8px"><div style="flex:1 1 320px">' + chart(340, 260, [{ d: L, c: GY, n: '理性（直線）', dash: '4 4' }, { d: V, c: RD, n: '價值函數 v(x)', w: 2.5 }], { x0: -1000, x1: 1000, y0: -2500, y1: 1200, xl: '相對參考點的得失（元）' }) +
        '</div><div style="flex:1 1 320px">' + chart(340, 260, [{ d: D, c: GY, n: '客觀機率', dash: '4 4' }, { d: W, c: BL, n: '決策權重 w(p)', w: 2.5 }], { x0: 0, x1: 100, y0: 0, y1: 100, xl: '客觀機率（%）' }) + '</div></div>';
      var ev = P.p * P.win - (1 - P.p) * P.lose, pv = w(P.p) * val(P.win) + w(1 - P.p) * val(-P.lose), acc = pv > 0;
      inf.innerHTML = '期望值（理性的算法）＝ ' + Math.round(P.p * 100) + '% × ' + money(P.win) + ' − ' + Math.round((1 - P.p) * 100) + '% × ' + money(P.lose) + ' ＝ <b>' + money(ev) + '</b>　→ 理性上' + (ev > 0 ? '<b>應該接受</b>' : ev < 0 ? '應該拒絕' : '無差異') + '。<br>' +
        '展望理論的主觀價值 ≈ <b style="color:' + (acc ? GN : RD) + '">' + (pv > 0 ? '+' : '') + pv.toFixed(0) + '</b>　→ 一般人很可能會<b>' + (acc ? '接受' : '拒絕') + '</b>。' +
        (ev > 0 && !acc ? '<br>這就是<b>損失趨避</b>：期望值是正的，但損失的痛讓人不想賭。在 λ ≈ 2 的情況下，大部分的人要「贏的金額」約為「輸的金額」的兩倍，才願意接受 50:50 的賭局。' : '') +
        (P.p <= 0.05 && acc && ev < 0 ? '<br>小機率被<b>高估</b>了（右圖藍線在對角線上方）——這就是樂透與保險同時暢銷的原因之一。' : '') +
        '<br><span style="color:var(--text-muted);font-size:0.9em">預設參數來自特沃斯基與康納曼（1992）的估計：α ≈ 0.88、λ ≈ 2.25、γ ≈ 0.61。左圖的縱軸是主觀價值（已縮放）。為了簡化，損失與獲得使用同一個 γ。</span>'; }
    us.forEach(function (u) { u(); }); }

  /* ---------- 偏誤小測驗 ---------- */
  var QZ = [
    { q: '琳達 31 歲，單身、直言、非常聰明，主修哲學，學生時代關心歧視與社會正義，參加過反核遊行。下列哪一個比較<b>可能</b>？', o: ['琳達是銀行行員', '琳達是銀行行員，而且是女性主義運動的參與者'], a: 0, t: '合取謬誤（代表性捷思）', e: '「A 且 B」的機率不可能大於「A」。但第二個選項更「像」琳達，所以約八成五的受試者選了它（特沃斯基與康納曼，1983）。' },
    { q: '一支球棒和一顆球總共 110 元，球棒比球貴 100 元。球多少錢？', o: ['10 元', '5 元'], a: 1, t: '系統一的直覺', e: '直覺的答案是 10 元，但那樣球棒就是 110 元，總共 120 元。正確答案是 5 元（球棒 105 元）。這是「認知反射測驗」的題目，許多名校的學生也答錯（弗雷德里克，2005）。' },
    { q: '某種疾病的盛行率是千分之一。一種檢驗的準確度：生病的人 100% 會驗出陽性，沒生病的人有 5% 會被誤驗為陽性。小明驗出陽性，他真的生病的機率大約是？', o: ['約 95%', '約 50%', '約 2%'], a: 2, t: '忽略基率', e: '1000 人中，1 人生病（陽性），999 個健康的人中約 50 人誤驗陽性。所以 51 個陽性中只有 1 人真的生病，約 2%。直覺常常忽略了「千分之一」這個基率。' },
    { q: '輪盤連續開出了 8 次紅色。下一次開黑色的機率？', o: ['比較高，「該輪到黑色了」', '和平常一樣', '比較低，紅色正「熱」'], a: 1, t: '賭徒謬誤', e: '每一次都是獨立的，輪盤沒有記憶。1913 年蒙地卡羅賭場曾連續開出 26 次黑色，賭客們押紅色輸了大筆的錢。' },
    { q: '政府準備對付一種預計會造成 600 人死亡的疾病。方案 A：確定救活 200 人。方案 B：三分之一的機率救活 600 人，三分之二的機率沒有人獲救。你選？', o: ['方案 A', '方案 B'], a: -1, t: '框架效應', e: '多數人（約 72%）選 A。但如果換個說法——方案 C：確定有 400 人死亡；方案 D：三分之一的機率沒有人死亡，三分之二的機率 600 人死亡——多數人（約 78%）改選 D。A 與 C、B 與 D 其實完全相同，只是用「救活」或「死亡」描述（特沃斯基與康納曼，1981）。' },
    { q: '你花 500 元買了電影票，看了 20 分鐘發現非常難看。你會？', o: ['看完，不然 500 元就浪費了', '離開，去做別的事'], a: 1, t: '沉沒成本謬誤', e: '不論你留下還是離開，500 元都拿不回來了（沉沒成本）。理性的決策只看「接下來的兩小時，看爛片和做別的事，哪個比較好」。' },
    { q: '擲一枚公平的硬幣：正面你贏 1,200 元，反面你輸 1,000 元。你願意賭嗎？', o: ['願意', '不願意'], a: -1, t: '損失趨避', e: '期望值是 +100 元，理性上應該接受。但多數人拒絕：輸 1,000 元的痛，大於贏 1,200 元的快樂。研究顯示，一般人要贏的錢約是輸的兩倍左右，才願意賭（第 14 課）。' },
    { q: '請先想想你手機號碼的最後兩位數字。接著估計：台灣有多少座海拔三千公尺以上的山？（只是估計，用來示範）', o: ['我的估計受到最後兩位數的影響？大概不會', '可能會'], a: -1, t: '錨定效應', e: '實驗顯示，即使是明顯無關的數字（例如轉盤上的隨機數字），也會把人們的估計往那個方向拉（第 5 課）。台灣的「百岳」以外，三千公尺以上的山峰有兩百多座——你的估計和手機號碼有關嗎？' },
  ];
  function initQuiz(root, cfg) { head(root, cfg.q); var i = 0, ans = [], card0 = el('div'), opts = el('div', 'margin:4px 0'), inf, nav = row(root);
    root.insertBefore(card0, nav); root.insertBefore(opts, nav); inf = info(root);
    var pv = btn('← 上一題'), nx = btn('下一題 →'); nav.appendChild(pv); nav.appendChild(nx);
    pv.onclick = function () { i = (i + QZ.length - 1) % QZ.length; show(); }; nx.onclick = function () { i = (i + 1) % QZ.length; show(); };
    function show() { var q = QZ[i]; card0.innerHTML = card('<div style="font-size:0.85em;color:var(--text-muted)">第 ' + (i + 1) + ' / ' + QZ.length + ' 題</div>' + q.q); opts.innerHTML = '';
      q.o.forEach(function (o, k) { var b = btn(o, k); b.onclick = function () { ans[i] = k; mark(opts, k); res(); }; opts.appendChild(b); }); if (ans[i] !== undefined) mark(opts, ans[i]); res(); }
    function res() { var q = QZ[i]; if (ans[i] === undefined) { inf.innerHTML = '先選一個答案。'; return; }
      inf.innerHTML = (q.a < 0 ? '' : ans[i] === q.a ? '<b style="color:' + GN + '">答對了！</b>' : '<b style="color:' + RD + '">很多人和你一樣。</b>') + '<b>' + q.t + '</b>：' + q.e; }
    show(); }

  /* ---------- 處分效應自我測驗 ---------- */
  function initDispo(root, cfg) { head(root, cfg.q); var seed = 7, R = 0, N = 10, log = [], cur, card0 = el('div'), bb = row(root), inf;
    root.insertBefore(card0, bb); inf = info(root);
    var sell = btn('賣出'), hold = btn('繼續持有'), again = btn('重新開始'); bb.appendChild(sell); bb.appendChild(hold); bb.appendChild(again);
    function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
    function gauss() { var u = 0; for (var k = 0; k < 6; k++) u += rnd(); return (u - 3) / Math.sqrt(0.5); }
    function make() { var p = [100], k, cost = 100; for (k = 1; k <= 60; k++) p.push(p[k - 1] * Math.exp(0.025 * gauss())); var fut = [p[60]]; for (k = 1; k <= 30; k++) fut.push(fut[k - 1] * Math.exp(0.025 * gauss())); return { p: p, f: fut, cost: cost }; }
    function show() { if (R >= N) return final(); cur = make(); var last = cur.p[60], gain = (last / cur.cost - 1) * 100, pts = cur.p.map(function (y, x) { return [x, y]; });
      card0.innerHTML = card('<div style="font-size:0.85em;color:var(--text-muted)">第 ' + (R + 1) + ' / ' + N + ' 檔股票</div>你在 60 天前以 <b>100 元</b>買進這檔股票，現在是 <b>' + last.toFixed(1) + ' 元</b>（' + (gain >= 0 ? '<span style="color:' + RD + '">帳面獲利 ' : '<span style="color:' + GN + '">帳面虧損 ') + Math.abs(gain).toFixed(1) + '%</span>）。你需要一些現金，要賣掉它嗎？') +
        chart(680, 200, [{ d: pts, c: BL, n: '股價', w: 2 }], { x0: 0, x1: 60, xl: '天數', hl: [{ y: 100, c: GY, n: '買進價 100' }] });
      inf.innerHTML = '做出選擇。（台灣習慣：<span style="color:' + RD + '">紅色是漲</span>、<span style="color:' + GN + '">綠色是跌</span>）'; }
    function pick(s) { if (R >= N) return; var last = cur.p[60], fut = cur.f[30] / last - 1; log.push({ g: last >= 100, s: s, fut: fut }); R++; show(); }
    function final() { var gw = log.filter(function (x) { return x.g; }), gl = log.filter(function (x) { return !x.g; }), sw = gw.filter(function (x) { return x.s; }).length, sl2 = gl.filter(function (x) { return x.s; }).length;
      var pgr = gw.length ? sw / gw.length : 0, plr = gl.length ? sl2 / gl.length : 0;
      card0.innerHTML = card('<b>結果</b><br>獲利的股票 ' + gw.length + ' 檔，你賣了 ' + sw + ' 檔（實現獲利比率 PGR ≈ <b>' + Math.round(pgr * 100) + '%</b>）<br>虧損的股票 ' + gl.length + ' 檔，你賣了 ' + sl2 + ' 檔（實現虧損比率 PLR ≈ <b>' + Math.round(plr * 100) + '%</b>）');
      inf.innerHTML = (pgr > plr ? '你比較傾向<b>賣出賺錢的、抱住賠錢的</b>——這正是<b>處分效應</b>。歐登（1998）分析一萬個券商帳戶，發現投資人實現獲利的比率（約 15%）明顯高於實現虧損的比率（約 10%）。' : pgr < plr ? '你比較傾向賣掉賠錢的股票——和多數人相反。' : '你賣出賺錢與賠錢股票的比例差不多。') +
        '<br><b>關鍵</b>：在這個模擬中，每一檔股票未來的走勢都是<b>隨機</b>的，和你的買進價完全無關。「我買在 100 元」只是你心中的參考點，市場並不知道，也不在乎。賣不賣，應該只看這檔股票<b>從現在開始</b>的前景。<br><span style="color:var(--text-muted);font-size:0.9em">簡化的隨機漫步模型，不代表真實的股價行為。真實世界還有稅務、交易成本等考量。</span>'; }
    sell.onclick = function () { pick(true); }; hold.onclick = function () { pick(false); }; again.onclick = function () { seed = Math.floor(Math.random() * 1e6) + 1; R = 0; log = []; show(); };
    show(); }

  /* ---------- 心理帳戶 ---------- */
  var MQ = [
    { q: '你要去看一場 1,000 元的演唱會。到了門口，發現<b>弄丟了一張 1,000 元的鈔票</b>（票還沒買）。你還會買票進場嗎？', o: ['會', '不會'], key: 'cash' },
    { q: '你事先花 1,000 元買了演唱會的票。到了門口，發現<b>票弄丟了</b>（不能補發），現場還能用 1,000 元再買一張。你會再買嗎？', o: ['會', '不會'], key: 'ticket' },
    { q: '你想買一個 500 元的計算機，店員說：開車 20 分鐘到分店，同一個計算機只要 <b>300 元</b>。你會去嗎？', o: ['會', '不會'], key: 'calc' },
    { q: '你想買一件 15,000 元的外套，店員說：開車 20 分鐘到分店，同一件外套只要 <b>14,800 元</b>。你會去嗎？', o: ['會', '不會'], key: 'coat' },
    { q: '你拿到一筆 2 萬元的<b>年終獎金</b>，和每個月的薪水相比，你花掉它的方式會比較「大方」嗎？', o: ['會，這是額外的錢', '不會，錢就是錢'], key: 'bonus' },
  ];
  function initMental(root, cfg) { head(root, cfg.q); var ans = {}, box = el('div'), inf; root.appendChild(box); inf = info(root);
    MQ.forEach(function (m, k) { var c = el('div'); c.innerHTML = card('<div style="font-size:0.85em;color:var(--text-muted)">情境 ' + (k + 1) + '</div>' + m.q); var r = el('div', 'margin:-2px 0 8px'); m.o.forEach(function (o, j) { var b = btn(o, j); b.onclick = function () { ans[m.key] = j; mark(r, j); up(); }; r.appendChild(b); }); c.appendChild(r); box.appendChild(c); });
    function up() { var t = [];
      if (ans.cash !== undefined && ans.ticket !== undefined) t.push('<b>情境 1 與 2</b>：兩者你都少了 1,000 元，處境<b>完全相同</b>。但在經典的實驗中，丟了現金的人約 88% 仍會買票，丟了票的人只有約 46% 會再買——因為丟票的人把損失記在「演唱會」這個帳戶裡，覺得看一場演唱會要花 2,000 元。' + (ans.cash !== ans.ticket ? '你的兩個答案不同，正是心理帳戶的效果。' : '你的答案一致，很理性！'));
      if (ans.calc !== undefined && ans.coat !== undefined) t.push('<b>情境 3 與 4</b>：兩者都是「開 20 分鐘的車省 200 元」。但多數人願意為了計算機跑一趟，卻不願意為了外套跑——因為我們比較的是<b>比例</b>（省 40% vs 省 1.3%），而不是絕對金額。' + (ans.calc !== ans.coat ? '你的選擇也是如此。' : '你的答案一致。'));
      if (ans.bonus !== undefined) t.push('<b>情境 5</b>：許多人把獎金、退稅、發票中獎的錢放進「意外之財」的帳戶，花得比較隨便。但每一塊錢的購買力都一樣——年終獎金如果拿來還高利率的卡債，可能比任何投資都划算。');
      inf.innerHTML = t.length ? t.join('<br>') : '回答上面的情境，看看心理帳戶如何影響你的決定（有些情境要成對比較）。'; }
    up(); }

  var INIT = { prospect: initProspect, quiz: initQuiz, dispo: initDispo, mental: initMental };
  function boot() { document.querySelectorAll('.bh-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🧠", note=BH_NOTE):
    return make_with(icon, note, [("bh-w", BHLIB)])


lesson = make()
