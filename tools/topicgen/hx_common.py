# -*- coding: utf-8 -*-
"""〈獵人〉（hx_）共用工具：沿用小說系列互動元件（NVLIB），另加念能力六角形與系別性格測驗（HXLIB）。"""
from nv_common import *
from nv_common import NVLIB

HX_NOTE = (u"本課程以冨樫義博的漫畫原作為準，包含完整劇情（有暴雷），寫到撰寫時已刊出的最新進度（第 410 話，2024 年底刊出），作品仍未完結。"
           u"人名與術語以台灣東立版譯名為主，譯名各版本不一時附上日文或英文；動畫則註明 1999 年版與 2011 年版的差異。"
           u"本課程為介紹與評論，不收錄原作圖片。")

HXLIB = r"""
(function () {
  if (window.__hxLib) return; window.__hxLib = 1;
""" + BASEJS + r"""
  var T6 = [['強化系', '#d0564f', '提升物體與自身原有的能力：力量、防禦、治癒。最均衡、最適合戰鬥。', '水量增加', '單純、一根筋', '小傑、窩金、尼特羅、芬克斯'],
    ['變化系', '#d9822b', '把氣的性質變成別的東西：電、橡膠、口香糖、棉花糖。', '水的味道改變', '反覆無常、愛說謊', '奇犽、西索、比司吉、瑪奇'],
    ['具現化系', '#b8941f', '用氣做出實體的物品：鎖鏈、鈕扣、針。', '水中出現雜質', '神經質、不輕易放鬆', '酷拉皮卡、柯特比、小滴'],
    ['特質系', '#8a5cb8', '不屬於其他系統的特殊能力：偷取別人的能力、預言、時間。', '其他變化', '個人主義、有領袖魅力', '庫洛洛、妮翁、尼飛彼多、酷拉皮卡（緋紅眼狀態）'],
    ['操作系', '#3a6ea5', '用氣操縱物體或生物：手機與天線、念獸、人偶。', '葉子移動', '理論派、我行我素', '伊路米、俠客、莫老五、修特'],
    ['放出系', '#4a9a5e', '讓氣離開身體仍然保持效果：念彈、瞬間移動、念獸。', '水的顏色改變', '急躁、不拘小節', '雷歐力、富蘭克林、拿酷魯']];
  function initHex(root, cfg) {
    head(root, cfg.q); var sel = cfg.s || 0, view = el('div'), info = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.65'); root.appendChild(view); root.appendChild(info);
    var pct = [100, 80, 60, 40, 60, 80];
    function P(i, r) { var a = -Math.PI / 2 + i * Math.PI / 3; return [200 + r * Math.cos(a), 170 + r * Math.sin(a)]; }
    function draw() { var o = '', poly = [];
      for (var i = 0; i < 6; i++) { var q = P(i, 120); poly.push(n1(q[0]) + ',' + n1(q[1])); }
      o += '<polygon points="' + poly.join(' ') + '" fill="none" stroke="var(--border)" stroke-width="1.5"/>';
      var sh = []; for (var j = 0; j < 6; j++) { var d = (j - sel + 6) % 6, r = pct[d] / 100 * 120, q2 = P(j, r); sh.push(n1(q2[0]) + ',' + n1(q2[1])); }
      o += '<polygon points="' + sh.join(' ') + '" fill="' + T6[sel][1] + '" fill-opacity="0.22" stroke="' + T6[sel][1] + '" stroke-width="2"/>';
      for (var k = 0; k < 6; k++) { var c = P(k, 120), lb = P(k, 150), dd = (k - sel + 6) % 6, on = k === sel;
        o += '<g data-i="' + k + '" style="cursor:pointer"><circle cx="' + n1(c[0]) + '" cy="' + n1(c[1]) + '" r="' + (on ? 9 : 7) + '" fill="' + T6[k][1] + '"/>' + tx(lb[0], lb[1] + 4, T6[k][0], 12.5, T6[k][1]) + tx(lb[0], lb[1] + 19, pct[dd] + '%', 11, 'currentColor') + '</g>'; }
      o += tx(470, 60, '主系別 100%', 12, 'currentColor', 'start') + tx(470, 84, '相鄰兩系 80%', 12, 'currentColor', 'start') + tx(470, 108, '隔一系 60%', 12, 'currentColor', 'start') + tx(470, 132, '對面 40%', 12, 'currentColor', 'start');
      o += tx(470, 170, '點選頂點切換主系別', 10.5, 'var(--text-muted)', 'start');
      view.innerHTML = svgw('0 0 640 340', o);
      view.querySelectorAll('g[data-i]').forEach(function (g) { g.addEventListener('click', function () { sel = +g.getAttribute('data-i'); draw(); }); });
      var t = T6[sel], opp = T6[(sel + 3) % 6][0], nb = T6[(sel + 1) % 6][0] + '、' + T6[(sel + 5) % 6][0];
      info.innerHTML = '<b style="color:' + t[1] + '">' + t[0] + '</b>：' + t[2] + '<br>水見式：<b>' + t[3] + '</b>　西索的性格說：' + t[4] + '<br>代表人物：' + t[5] +
        '<br>相鄰的' + nb + '最多能練到約八成；對面的' + opp + '只有約四成，而且學起來事倍功半。這些百分比是書中雲谷（Wing）與比司吉的說法，代表「修練效率與上限」，不是硬性規定。'; }
    draw();
  }

  var QZ = [['和朋友約好時間，你通常？', [['準時，說到做到', 0], ['看心情，可能臨時改計畫', 1], ['早到，順便把路線、備案都想好', 4], ['常常遲到，但到了就玩得最開心', 5]]],
    ['做一件事卡住了，你會？', [['硬幹，多做幾次一定會成功', 0], ['換個角度，用意想不到的方法繞過去', 1], ['先把工具準備到最完美', 2], ['相信直覺，走一條沒人走過的路', 3]]],
    ['朋友形容你最常用的一句話是？', [['單純、直來直往', 0], ['摸不透、愛開玩笑', 1], ['很細心、有點神經質', 2], ['很有個人風格，大家會跟著你', 3]]],
    ['團體報告時你扮演？', [['衝第一線，把最累的做完', 0], ['負責把大家的想法串起來，按照計畫走', 4], ['負責做出最漂亮的成品', 2], ['講完就走，細節交給別人', 5]]],
    ['你最受不了的是？', [['拐彎抹角', 0], ['被規定死', 1], ['東西亂七八糟', 2], ['和別人一模一樣', 3]]],
    ['生氣的時候你會？', [['當場爆發，很快就沒事', 5], ['笑笑的，但記在心裡', 1], ['冷靜分析對方哪裡錯', 4], ['一直想，越想越氣', 2]]],
    ['選一個你最想要的能力：', [['打不倒的身體', 0], ['可以改變任何東西的性質', 1], ['可以做出任何道具', 2], ['可以操控別人或物品', 4], ['可以瞬間移動、遠距攻擊', 5], ['獨一無二、沒人能模仿的能力', 3]]]];
  var TN = ['強化系', '變化系', '具現化系', '特質系', '操作系', '放出系'], TC = ['#d0564f', '#d9822b', '#b8941f', '#8a5cb8', '#3a6ea5', '#4a9a5e'];
  function initQuiz(root, cfg) {
    head(root, cfg.q); var ans = [], box = el('div'), res = el('div', 'margin-top:10px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(box); root.appendChild(res);
    QZ.forEach(function (q, i) { var p = el('p', 'margin:10px 0 4px;font-weight:bold', (i + 1) + '. ' + q[0]), b = el('div'); box.appendChild(p); box.appendChild(b);
      q[1].forEach(function (o, j) { var x = btn(o[0], 'q' + i + 'o' + j); x.addEventListener('click', function () { ans[i] = o[1]; mark(b, 'q' + i + 'o' + j); show(); }); b.appendChild(x); }); });
    function show() { var n = ans.filter(function (a) { return a !== undefined; }).length; if (n < QZ.length) { res.innerHTML = '已回答 ' + n + '／' + QZ.length + ' 題。全部答完會顯示結果。'; return; }
      var sc = [0, 0, 0, 0, 0, 0]; ans.forEach(function (a) { sc[a] += 2; sc[(a + 1) % 6] += 1; sc[(a + 5) % 6] += 1; }); var best = 0; sc.forEach(function (v, i) { if (v > sc[best]) best = i; });
      var o = ''; sc.forEach(function (v, i) { o += '<div style="display:flex;align-items:center;gap:8px;margin:2px 0"><span style="width:5em">' + TN[i] + '</span><span style="display:inline-block;height:12px;border-radius:3px;background:' + TC[i] + ';width:' + (v * 8) + 'px"></span><span>' + v + '</span></div>'; });
      res.innerHTML = '你的結果：<b style="color:' + TC[best] + ';font-size:1.15em">' + TN[best] + '</b>' + o +
        '<span style="font-size:0.9em;color:var(--text-muted)">這只是好玩的測驗，依據的是西索在友克鑫市篇說的「性格分析」（他自己也承認是血型占卜等級的東西）。作品中真正的判定方法是水見式：把手放在水杯兩側練氣，看水和葉子起什麼變化。</span>'; }
    show();
  }

  function initAll() { document.querySelectorAll('.hx-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ hex: initHex, quiz: initQuiz })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def hxw(cfg, maxw=680):
    return wdg("hx-w", cfg, maxw)


_base = make_lesson(u"🎯", HX_NOTE, NVLIB, "nv-w")


def hxlesson(*a, **k):
    L = _base(*a, **k)
    if any(isinstance(b, tuple) and b[0] == "raw" and 'class="hx-w' in b[1] for b in L.body):
        L.body.insert(0, ("raw", u"<script>%s</script>" % HXLIB))
    return L
