# -*- coding: utf-8 -*-
"""〈引導孩子學習〉（gl_）共用：課程包裝與 GLLIB 互動元件。

GLLIB 元件（class="gl-w"）：
  curve   遺忘曲線與複習排程模擬（教學用簡化模型）
  plan    間隔複習時間表產生器
  ladder  提問階梯（布魯姆分類修訂版六層次）
  cpa     具體 → 圖像 → 抽象（乘法、分數）
  timer   專注計時器（依年齡建議時間長度）
另沿用 kd_common 的 tree（情境決策樹）與 nv_common 的卡片、時間軸。
"""
from cc_common import make_lesson, wdg, LS
from qt_common import BASEJS
from nv_common import NVLIB, nvw, ev, card, CB, CG, CO, CR, CP, CT, CY, CK
from kd_common import KDLIB, tree, XO

GL_NOTE = (u"本課程整理學習科學的研究與教育實務（2026 年 10 月查證），提供的是原則與可以嘗試的做法；每個孩子不同，請依孩子的反應調整。"
           u"若懷疑孩子有學習障礙、注意力或情緒問題，請諮詢學校輔導室、特教鑑定或兒童心智科，<strong>本課程不能取代專業評估</strong>。")

CD = XO("child-development", u"兒童成長心理學")
PA = XO("parenting", u"家長教養")

GLLIB = r"""
(function () {
  if (window.__glLib) return; window.__glLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function pct(v) { return Math.round(v * 100) + '%'; }

  /* ---------- 遺忘曲線與複習排程 ---------- */
  /* 記憶保持率 R = (1 + Δt / (9S))^-1；每次複習時 S ← S × (1 + 6(1 − R))：忘得越多再想起來，穩定度增加越多（必要難度）。 */
  function sim(revs, T) { var S = 0.5, tl = 0, pts = [], i = 0, rs = revs.slice().sort(function (a, b) { return a - b; });
    for (var t = 0; t <= T + 1e-9; t += 0.05) { while (i < rs.length && rs[i] <= t + 1e-9) { var R0 = Math.pow(1 + (rs[i] - tl) / (9 * S), -1); pts.push([rs[i], R0]); S = S * (1 + 6 * (1 - R0)); tl = rs[i]; pts.push([rs[i], 1]); i++; }
      pts.push([t, Math.pow(1 + (t - tl) / (9 * S), -1)]); }
    function at(x) { var S2 = 0.5, t2 = 0; rs.forEach(function (r) { if (r <= x) { var R0 = Math.pow(1 + (r - t2) / (9 * S2), -1); S2 = S2 * (1 + 6 * (1 - R0)); t2 = r; } }); return Math.pow(1 + (x - t2) / (9 * S2), -1); }
    return { pts: pts, at: at }; }
  function initCurve(root, cfg) {
    head(root, cfg.q); var P = [['once', '只學一次', []], ['cram', '考前一天狂讀 3 遍', [6, 6.03, 6.06]], ['space', '間隔複習 3 次', [1, 3, 6]], ['daily', '每天讀一次（6 次）', [1, 2, 3, 4, 5, 6]]];
    var cur = 'space', revs = [1, 3, 6], bb = bar(root), out = el('div'), days = el('div', 'margin-top:6px;font-size:0.85em'), tb = el('div', 'overflow-x:auto;margin-top:8px'), p;
    P.forEach(function (x) { var b = btn(x[1], x[0]); b.addEventListener('click', function () { cur = x[0]; revs = x[2].slice(); mark(bb, cur); draw(); }); bb.appendChild(b); });
    root.appendChild(out); root.appendChild(days); root.appendChild(tb); p = info(root);
    days.innerHTML = '自訂：點日期加入或取消複習（第 7 天考試）<br>';
    for (var d = 1; d <= 29; d++) { (function (d) { var b = btn(String(d), 'd' + d); b.style.minWidth = '2.2em'; b.style.padding = '2px 4px'; b.addEventListener('click', function () { cur = 'custom'; mark(bb, 'x');
      var k = revs.indexOf(d); if (k >= 0) revs.splice(k, 1); else revs.push(d); draw(); }); days.appendChild(b); })(d); }
    function draw() { var s = sim(revs, 30), base = sim([], 30);
      var CW = root.clientWidth < 520 ? 330 : 640; out.innerHTML = chart(CW, CW < 500 ? 250 : 260, [{ d: base.pts.map(function (q) { return [q[0], q[1] * 100]; }), c: '#bbb', dash: '4 3', n: '只學一次' }, { d: s.pts.map(function (q) { return [q[0], q[1] * 100]; }), c: '#3a6ea5', n: '目前的排程' }],
        { x0: 0, x1: 30, y0: 0, y1: 100, xl: '第幾天', yl: '記得多少（%）', vl: [{ x: 7, c: '#d0564f', n: '考試' }, { x: 30, c: '#5aa469', n: '一個月後' }] });
      days.querySelectorAll('button').forEach(function (b) { var on = revs.indexOf(+b.textContent) >= 0; b.style.background = on ? '#3a6ea5' : 'var(--surface)'; b.style.color = on ? '#fff' : 'var(--text)'; });
      var h = '<table style="border-collapse:collapse;font-size:0.85em;width:100%"><tr><th style="text-align:left;padding:3px 6px">排程</th><th>複習次數</th><th>第 7 天考試</th><th>一個月後</th></tr>';
      P.concat(cur === 'custom' ? [['custom', '自訂', revs]] : []).forEach(function (x) { var q = sim(x[2], 30), n = x[2].filter(function (r) { return r <= 30; }).length;
        h += '<tr style="border-top:1px solid var(--border);' + (x[0] === cur ? 'background:var(--accent-soft);font-weight:bold' : '') + '"><td style="padding:3px 6px">' + x[1] + '</td><td style="text-align:center">' + n + '</td><td style="text-align:center">' + pct(q.at(7)) + '</td><td style="text-align:center">' + pct(q.at(30)) + '</td></tr>'; });
      tb.innerHTML = h + '</table>';
      p.innerHTML = '<b>看三件事：</b>① 考前狂讀在第 7 天分數很高，但一個月後掉得很快；② 間隔複習只用一半的次數，長期記憶就和每天讀差不多；③ 每次複習後，曲線下降得越來越慢。<br><span style="font-size:0.88em;color:var(--text-muted)">這是教學用的簡化模型（形式參考間隔複習軟體常用的記憶模型），數字只用來比較排程，不代表真實的分數。真實的記憶還取決於內容難度、理解程度、睡眠與複習時是否「主動回想」。</span>'; }
    mark(bb, cur); draw();
  }

  /* ---------- 間隔複習時間表 ---------- */
  function initPlan(root, cfg) {
    head(root, cfg.q); var D = 21, out = el('div', 'margin-top:8px'), p;
    var u = slider(root, '離考試還有幾天', 3, 60, 1, D, function (v) { return v + ' 天'; }, 'D', function (v) { D = v; draw(); });
    root.appendChild(out); p = info(root);
    function draw() { var rv = [], g = 1; while (g < D - 1) { rv.push(g); g = g < 2 ? 3 : g * 2 + 1; } if (rv.indexOf(D - 1) < 0) rv.push(D - 1);
      var h = '<div style="display:flex;flex-wrap:wrap;gap:3px">';
      for (var d = 0; d <= D; d++) { var t = d === 0 ? '學' : d === D ? '考' : rv.indexOf(d) >= 0 ? '複' : '', bg = d === 0 ? '#5aa469' : d === D ? '#d0564f' : t ? '#3a6ea5' : 'var(--surface)';
        h += '<div title="第 ' + d + ' 天" style="width:30px;height:38px;border:1px solid var(--border);border-radius:5px;background:' + bg + ';color:' + (t ? '#fff' : 'var(--text-muted)') + ';font-size:10px;text-align:center;line-height:1.25;padding-top:3px">' + d + '<br><b style="font-size:12px">' + t + '</b></div>'; }
      out.innerHTML = h + '</div>';
      var gap = Math.max(1, Math.round(D * 0.15));
      p.innerHTML = '第 0 天學新內容，之後在第 <b>' + rv.join('、') + '</b> 天複習（共 ' + rv.length + ' 次），間隔越拉越長；考前一天只做<b>快速自我測驗</b>，不再從頭讀。每次複習都用「先回想、再對答案」，而不是重讀。' +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">Cepeda 等人（2008）發現：想記到幾週後，兩次學習相隔約為「目標時間」的 10～20% 效果最好（目標是一年後時，約 5～10%）。以 ' + D + ' 天為例，第一輪間隔約 ' + gap + ' 天。實際排程可依科目與孩子的狀況調整。</span>'; }
    u(); draw();
  }

  /* ---------- 提問階梯 ---------- */
  function initLadder(root, cfg) {
    head(root, cfg.q); var keys = Object.keys(cfg.topics), cur = keys[0], bb = bar(root), out = el('div', 'margin-top:8px'), p;
    var L = [['記憶', '#9aa9b9', '是什麼？在哪裡？誰？'], ['理解', '#6aa3c9', '用自己的話說說看'], ['應用', '#5aa469', '換一個情況會怎樣用？'], ['分析', '#d9a12b', '比較、找原因、找關係'], ['評鑑', '#d9822b', '你同意嗎？哪個比較好？為什麼？'], ['創造', '#c8506a', '如果……你會怎麼設計？']];
    keys.forEach(function (k) { var b = btn(k, k); b.addEventListener('click', function () { cur = k; mark(bb, k); draw(); }); bb.appendChild(b); });
    root.appendChild(out); p = info(root);
    function draw() { var Q = cfg.topics[cur], h = '';
      for (var i = 5; i >= 0; i--) h += '<div style="display:flex;align-items:stretch;margin:3px 0 3px ' + (i * 4) + '%"><div style="flex:0 0 4.2em;background:' + L[i][1] + ';color:#fff;border-radius:6px 0 0 6px;padding:6px 8px;font-weight:bold;text-align:center">' + L[i][0] + '</div><div style="flex:1;border:1px solid ' + L[i][1] + ';border-left:none;border-radius:0 6px 6px 0;padding:6px 10px;line-height:1.5"><span style="font-size:0.8em;color:var(--text-muted)">' + L[i][2] + '</span><br>' + Q[i] + '</div></div>';
      out.innerHTML = h;
      p.innerHTML = '從下往上爬：先確認孩子知道「是什麼」，再一步步問到「為什麼」與「如果」。不需要每次都爬到頂，但日常對話中<b>多加一兩個上層的問題</b>，就能讓思考變深。<br><span style="font-size:0.88em;color:var(--text-muted)">六個層次來自布魯姆分類的修訂版（Anderson 與 Krathwohl，2001）。</span>'; }
    mark(bb, cur); draw();
  }

  /* ---------- CPA：具體 → 圖像 → 抽象 ---------- */
  function initCpa(root, cfg) {
    head(root, cfg.q); var mode = 'mul', a = 3, b = 4, n = 3, d = 4, bb = bar(root), ctl = el('div'), out = el('div', 'display:flex;flex-wrap:wrap;gap:10px;margin-top:8px'), p;
    [['mul', '乘法：幾個幾'], ['frac', '分數']].forEach(function (x) { var t = btn(x[1], x[0]); t.addEventListener('click', function () { mode = x[0]; mark(bb, mode); build(); }); bb.appendChild(t); });
    root.appendChild(ctl); root.appendChild(out); p = info(root);
    function panel(t, c, inner) { return '<div style="flex:1 1 180px;border:1px solid var(--border);border-top:4px solid ' + c + ';border-radius:8px;padding:6px 8px"><b style="color:' + c + '">' + t + '</b><div style="max-width:200px;margin:0 auto">' + inner + '</div></div>'; }
    function build() { ctl.innerHTML = ''; var u1, u2;
      if (mode === 'mul') { u1 = slider(ctl, '盤子數', 1, 5, 1, a, function (v) { return v + ' 盤'; }, 'a', function (v) { a = v; draw(); }); u2 = slider(ctl, '每盤餅乾', 1, 6, 1, b, function (v) { return v + ' 片'; }, 'b', function (v) { b = v; draw(); }); }
      else { u1 = slider(ctl, '分成幾等份（分母）', 2, 8, 1, d, function (v) { return v + ' 份'; }, 'd', function (v) { d = v; if (n > d) n = d; draw(); }); u2 = slider(ctl, '拿走幾份（分子）', 1, 8, 1, n, function (v) { return Math.min(v, d) + ' 份'; }, 'n', function (v) { n = Math.min(v, d); draw(); }); }
      u1(); u2(); draw(); }
    function draw() { var g1 = '', g2 = '', ab = '', i, j;
      if (mode === 'mul') {
        for (i = 0; i < a; i++) { var cx = 34 + (i % 3) * 64, cy = 34 + Math.floor(i / 3) * 64; g1 += '<ellipse cx="' + cx + '" cy="' + cy + '" rx="29" ry="26" fill="none" stroke="#999" stroke-width="2"/>';
          for (j = 0; j < b; j++) { var ang = j / b * 2 * Math.PI, r = b === 1 ? 0 : 13; g1 += '<circle cx="' + n1(cx + r * Math.cos(ang)) + '" cy="' + n1(cy + r * Math.sin(ang)) + '" r="6.5" fill="#c9883a" stroke="#8a5a20"/>'; } }
        for (i = 0; i < a; i++) for (j = 0; j < b; j++) g2 += '<circle cx="' + (16 + j * 26) + '" cy="' + (16 + i * 26) + '" r="9" fill="#3a6ea5"/>';
        for (i = 0; i < a; i++) g2 += tx(16 + b * 26 + 4, 20 + i * 26, b, 11, 'var(--text-muted)', 'start');
        ab = '<div style="font-size:1.6em;text-align:center;margin:18px 0 6px">' + a + ' × ' + b + ' = ' + (a * b) + '</div><div style="font-size:0.85em;color:var(--text-muted);text-align:center">' + Array(a + 1).join(b + ' + ').slice(0, -3) + ' = ' + (a * b) + '</div>';
        out.innerHTML = panel('具體：真的拿東西', '#c9883a', svgw('0 0 200 ' + (a > 3 ? 136 : 72), g1) + '<div style="font-size:0.82em;color:var(--text-muted)">' + a + ' 個盤子，每盤 ' + b + ' 片餅乾</div>') +
          panel('圖像：畫成點陣', '#3a6ea5', svgw('0 0 ' + (b * 26 + 24) + ' ' + (a * 26 + 6), g2) + '<div style="font-size:0.82em;color:var(--text-muted)">' + a + ' 列，每列 ' + b + ' 個；轉 90 度就是 ' + b + ' × ' + a + '</div>') +
          panel('抽象：算式', '#9c89d6', ab);
        p.innerHTML = '先用真的東西（積木、餅乾、硬幣）操作，再畫成圖，最後才寫算式——這就是 <b>CPA 教學法</b>。點陣圖還能讓孩子自己發現「' + a + ' × ' + b + ' 和 ' + b + ' × ' + a + ' 一樣多」（交換律），這比背出來更牢。'; }
      else {
        var cx2 = 70, cy2 = 70, R = 58;
        for (i = 0; i < d; i++) { var a0 = -Math.PI / 2 + i / d * 2 * Math.PI, a1 = a0 + 2 * Math.PI / d;
          g1 += '<path d="M' + cx2 + ' ' + cy2 + ' L' + n1(cx2 + R * Math.cos(a0)) + ' ' + n1(cy2 + R * Math.sin(a0)) + ' A' + R + ' ' + R + ' 0 0 1 ' + n1(cx2 + R * Math.cos(a1)) + ' ' + n1(cy2 + R * Math.sin(a1)) + ' Z" fill="' + (i < n ? '#e3a83b' : '#f4ead2') + '" stroke="#8a5a20" stroke-width="1.5"/>'; }
        var w = 180 / d; for (i = 0; i < d; i++) g2 += '<rect x="' + n1(4 + i * w) + '" y="20" width="' + n1(w) + '" height="34" fill="' + (i < n ? '#3a6ea5' : 'none') + '" stroke="#3a6ea5" stroke-width="1.5"/>';
        g2 += tx(94, 14, '一整條 = 1', 10, 'var(--text-muted)');
        out.innerHTML = panel('具體：切披薩', '#c9883a', svgw('0 0 140 140', g1) + '<div style="font-size:0.82em;color:var(--text-muted)">切成 ' + d + ' 塊一樣大的，拿走 ' + n + ' 塊</div>') +
          panel('圖像：長條圖', '#3a6ea5', svgw('0 0 190 64', g2) + '<div style="font-size:0.82em;color:var(--text-muted)">一整條平分成 ' + d + ' 段，塗 ' + n + ' 段</div>') +
          panel('抽象：分數', '#9c89d6', '<div style="text-align:center;margin:14px 0 4px;font-size:1.6em;line-height:1.1"><div>' + n + '</div><div style="border-top:2px solid currentColor;width:1.6em;margin:2px auto"></div><div>' + d + '</div></div><div style="font-size:0.85em;color:var(--text-muted);text-align:center">' + d + ' 分之 ' + n + (n === d ? '，也就是 1 整個' : '') + '</div>');
        p.innerHTML = '分數最常見的誤解是把它當成兩個獨立的數字（例如以為 1/8 比 1/4 大，因為 8 比 4 大）。先切披薩、折紙，讓孩子看到<b>分母越大，每一塊越小</b>，再寫成符號。注意強調「<b>一樣大</b>」的等份。'; }
    }
    mark(bb, mode); build();
  }

  /* ---------- 專注計時器 ---------- */
  function initTimer(root, cfg) {
    head(root, cfg.q); var A = [['幼兒園', 10, 5], ['小一～小二', 15, 5], ['小三～小四', 20, 5], ['小五～小六', 25, 5], ['國中', 30, 5], ['高中', 40, 10]];
    var k = 2, left = 0, phase = 'work', iv = null, bb = bar(root), face = el('div', 'font-size:3em;text-align:center;font-variant-numeric:tabular-nums;margin:8px 0 2px'), st = el('div', 'text-align:center;color:var(--text-muted);font-size:0.9em'), cb = bar(root), p;
    A.forEach(function (x, i) { var b = btn(x[0], 'g' + i); b.addEventListener('click', function () { k = i; mark(bb, 'g' + i); reset(); }); bb.appendChild(b); });
    root.appendChild(face); root.appendChild(st); root.appendChild(cb); cb.style.textAlign = 'center'; p = info(root);
    var bs = btn('▶ 開始', 'go'), bp = btn('⏸ 暫停', 'pa'), br = btn('↺ 重設', 're'); [bs, bp, br].forEach(function (b) { cb.appendChild(b); });
    function show() { var m = Math.floor(left / 60), s = left % 60; face.textContent = (m < 10 ? '0' : '') + m + ':' + (s < 10 ? '0' : '') + s;
      st.textContent = phase === 'work' ? '專心時間：一次只做一件事' : '休息時間：站起來、喝水、看遠方（不要滑手機）'; face.style.color = phase === 'work' ? 'var(--text)' : '#5aa469'; }
    function stop() { if (iv) { clearInterval(iv); iv = null; } }
    function reset() { stop(); phase = 'work'; left = A[k][1] * 60; show();
      p.innerHTML = '<b>' + A[k][0] + '</b>：建議先試 <b>' + A[k][1] + ' 分鐘專心 + ' + A[k][2] + ' 分鐘休息</b>，再依孩子的狀況調整。這是經驗上的起點，不是研究定出的標準；有的孩子 10 分鐘就需要動一動，有的投入時可以更久。<br><span style="font-size:0.88em;color:var(--text-muted)">「番茄鐘工作法」由 Cirillo 在 1980 年代提出，原版是 25 分鐘工作、5 分鐘休息。重點是讓「開始」變容易、讓休息有固定的節奏。</span>'; }
    bs.addEventListener('click', function () { if (iv) return; iv = setInterval(function () { left--; if (left <= 0) { if (phase === 'work') { phase = 'rest'; left = A[k][2] * 60; } else { phase = 'work'; left = A[k][1] * 60; stop(); } } show(); }, 1000); });
    bp.addEventListener('click', stop); br.addEventListener('click', reset);
    mark(bb, 'g' + k); reset();
  }

  function initAll() { document.querySelectorAll('.gl-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ curve: initCurve, plan: initPlan, ladder: initLadder, cpa: initCpa, timer: initTimer })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def glw(cfg, maxw=720):
    return wdg("gl-w", cfg, maxw)


CURVE = glw({"t": "curve", "q": u"遺忘曲線模擬：選一種讀書方式，看第 7 天考試和一個月後還記得多少"})
PLAN = glw({"t": "plan", "q": u"間隔複習時間表：拖動滑桿設定離考試的天數"})
CPA = glw({"t": "cpa", "q": u"CPA 教學法：同一個概念的三種表現方式"})
TIMER = glw({"t": "timer", "q": u"專注計時器：選孩子的年級，按開始"}, 560)

_TOPICS = {
    u"恐龍": [u"暴龍吃什麼？", u"為什麼說暴龍是肉食性的？你從哪裡看出來？", u"如果我們在公園挖到一顆牙齒，怎麼判斷它是吃肉還是吃草的動物？",
             u"暴龍和雷龍的身體有什麼不同？這些不同和牠們吃的東西有什麼關係？", u"你覺得恐龍滅絕的原因，哪一個說法最有說服力？為什麼？", u"如果恐龍沒有滅絕，現在的城市會長什麼樣子？畫一個能讓人和恐龍一起生活的城市。"],
    u"三隻小豬": [u"三隻小豬分別用什麼蓋房子？", u"為什麼大野狼吹不倒磚頭房子？", u"如果你要在颱風很多的地方蓋房子，會選什麼材料？",
              u"老大、老二和老三的想法有什麼不同？是什麼讓老三做出不同的選擇？", u"你覺得大野狼是壞人嗎？從大野狼的角度看，故事會不一樣嗎？", u"幫故事寫一個新的結局，讓三隻小豬和大野狼都能過得好。"],
    u"下雨": [u"雨是從哪裡來的？", u"用你自己的話說說看，水是怎麼跑到天上去的？", u"曬衣服的時候，為什麼有太陽、有風比較快乾？",
            u"台灣的梅雨和颱風雨有什麼不同？", u"有人說「多種樹可以減少淹水」，你同意嗎？有什麼證據？", u"設計一個能收集雨水、用來澆花的裝置。"],
    u"分數": [u"二分之一怎麼寫？", u"為什麼四分之一比二分之一小？用披薩說明。", u"三個人分兩個披薩，每個人拿到多少？",
            u"二分之一和四分之二有什麼關係？還有哪些分數也一樣大？", u"小明說「1/3 + 1/3 = 2/6」，你同意嗎？哪裡出錯了？", u"自己出一題分數的應用題，讓爸爸媽媽來解。"],
}
LADDER = glw({"t": "ladder", "q": u"提問階梯：選一個主題，看看從「是什麼」到「如果……」的六層問題", "topics": _TOPICS})


def make(icon, note):
    base = make_lesson(icon, note, GLLIB, "gl-w")

    def lesson(*a, **k):
        L = base(*a, **k)
        raws = [b[1] for b in L.body if isinstance(b, tuple) and b[0] == "raw"]
        if any('class="kd-w' in r for r in raws):
            L.body.insert(0, ("raw", u"<script>%s</script>" % KDLIB))
        if any('class="nv-w' in r for r in raws):
            L.body.insert(0, ("raw", u"<script>%s</script>" % NVLIB))
        return L
    return lesson
