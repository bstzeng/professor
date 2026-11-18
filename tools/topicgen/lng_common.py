# -*- coding: utf-8 -*-
"""〈老化與長壽科學〉（lng_）共用：課程包裝與 LNGLIB 互動元件（class="lng-w"）。

  gomp     岡珀茲死亡率：存活曲線與「減緩老化」的效果
  telo     端粒與海佛烈克極限
  animal   動物的體重與最長壽命
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

LNG_NOTE = u"本課程為科普與教育用途，不構成醫療建議；任何藥物或補充品請先與醫師討論。互動模擬為教學用的簡化模型。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def lw(cfg, maxw=680):
    return wdg("lng-w", cfg, maxw)


LNGLIB = r"""
(function () {
  if (window.__lngLib) return; window.__lngLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }

  function initGomp(root, cfg) {
    head(root, cfg.q); var P = { a: 1, d: 11 }, view = el('div'), inf;
    var us = [slider(root, '起始死亡率（與現代人相比的倍數）', 0.25, 4, 0.05, P.a, function (x) { return f2(x) + ' 倍'; }, null, function (x) { P.a = x; draw(); }),
      slider(root, '死亡率倍增時間（老化的速度）', 5, 16, 0.5, P.d, function (x) { return f1(x) + ' 年'; }, null, function (x) { P.d = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function surv(A, Dt) { var G = Math.log(2) / Dt, l = 1, d = [], le = 0, med = null; for (var x = 30; x <= 130; x += 0.25) { d.push([x, l * 100]); le += l * 0.25; var mu = A * Math.exp(G * (x - 30)); l *= Math.exp(-mu * 0.25); if (med === null && l < 0.5) med = x; } return { d: d, le: 30 + le, med: med }; }
    function draw() { var A0 = 0.0006, base = surv(A0, 8), s = surv(A0 * P.a, P.d);
      view.innerHTML = chart(640, 260, [{ d: base.d, c: GY, n: '基準（約現代已開發國家）', w: 1.6, dash: '5,4' }, { d: s.d, c: RD, n: '你的設定', w: 2.6 }], { x0: 30, x1: 130, y0: 0, y1: 100, xl: '年齡', yl: '仍存活（%）', hl: [{ y: 50, c: GY, n: '一半' }] });
      inf.innerHTML = '從 30 歲算起：基準的存活中位數約 <b>' + Math.round(base.med) + '</b> 歲；你的設定約 <b>' + (s.med ? Math.round(s.med) : '> 130') + '</b> 歲。' +
        '<br>岡珀茲定律：成年後的死亡率大約每 <b>8 年加倍</b>。把起始死亡率減半（例如更好的醫療、少抽菸），曲線只往右移幾年；但若能<b>延長倍增時間</b>（真正減緩老化），曲線會大幅往右延伸——這是老化研究追求的目標。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">純岡珀茲模型的示意，未計入意外與極高齡時死亡率趨緩的現象。</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initTelo(root, cfg) {
    head(root, cfg.q); var P = { loss: 100, tert: 0 }, view = el('div'), inf;
    var us = [slider(root, '每次分裂縮短（鹼基對）', 30, 200, 10, P.loss, function (x) { return x + ' bp'; }, null, function (x) { P.loss = x; draw(); })];
    var b = el('div', 'margin:4px 0'), tb = btn('端粒酶：關'); tb.onclick = function () { P.tert ^= 1; tb.textContent = '端粒酶：' + (P.tert ? '開（例如幹細胞、癌細胞）' : '關'); draw(); }; b.appendChild(tb); root.appendChild(b);
    root.appendChild(view); inf = info(root);
    function draw() { var L = 10000, crit = 5000, d = [], stop = null; for (var n = 0; n <= 120; n++) { d.push([n, L]); if (L <= crit && stop === null) { stop = n; } if (stop === null || P.tert) L = P.tert ? Math.max(L - P.loss + P.loss * 0.95, crit + 500) : L - P.loss; else L = L; }
      if (stop !== null && !P.tert) d = d.slice(0, stop + 1);
      view.innerHTML = chart(640, 240, [{ d: d, c: P.tert ? GN : BL, n: '端粒長度', w: 2.6 }], { x0: 0, x1: 120, y0: 0, y1: 11000, xl: '細胞分裂次數', yl: '端粒長度（bp）', hl: [{ y: crit, c: RD, n: '臨界長度：停止分裂（衰老）' }], vl: !P.tert && stop !== null ? [{ x: stop, c: RD, n: '第 ' + stop + ' 次' }] : [] });
      inf.innerHTML = (P.tert ? '有<b>端粒酶</b>時，端粒在每次分裂後被補回，細胞可以持續分裂。生殖細胞、部分幹細胞，以及約九成的癌細胞都有活躍的端粒酶。' :
        '每次分裂，染色體末端的端粒變短約 ' + P.loss + ' 個鹼基對。縮到臨界長度時，細胞停止分裂（進入<b>衰老</b>）：約在第 <b>' + stop + '</b> 次分裂。這就是<b>海佛烈克極限</b>（人類纖維母細胞約 40～60 次）。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">數字為示意；真實的端粒長度與縮短速度因細胞與個人而異。</span>'; }
    us.forEach(function (u) { u(); });
  }

  var AN = [['小鼠', 0.03, 4, GY, '實驗室中通常只活 2～3 年，最長約 4 年。'], ['大鼠', 0.4, 4, GY, '最長約 4 年。'], ['裸鼴鼠', 0.035, 37, OR, '和小鼠差不多大，卻能活超過 37 年，而且死亡率幾乎不隨年齡上升，也極少得癌症。'],
    ['布氏鼠耳蝠', 0.007, 41, OR, '只有幾公克重，野外紀錄活了 41 年。蝙蝠普遍比同體型的哺乳類長壽很多。'], ['狗', 30, 24, GY, '大型犬反而比小型犬短命。'], ['黑猩猩', 50, 68, GY, ''], ['人類', 65, 122, RD, '有可靠紀錄的最長壽者：法國的珍妮・卡爾芒，122 歲。'],
    ['亞洲象', 4000, 86, GY, ''], ['弓頭鯨', 80000, 211, PU, '用眼睛水晶體中的胺基酸估計，有個體超過 200 歲。'], ['格陵蘭鯊', 1000, 392, PU, '用眼睛水晶體的放射性碳定年，估計可活約 270～500 年，是已知最長壽的脊椎動物。'],
    ['加拉巴哥象龜', 250, 177, GN, '許多龜類的死亡率幾乎不隨年齡增加。'], ['家貓', 4, 30, GY, '']];
  function initAnimal(root, cfg) {
    head(root, cfg.q); var P = { s: 2 }, view = el('div'), inf; root.appendChild(view); inf = info(root);
    function draw() { var W = 640, H = 300, L = 48, R = 14, T = 14, B = 34, g = '';
      function sx(m) { return L + (Math.log10(m) + 3) / 8 * (W - L - R); } function sy(y) { return H - B - (Math.log10(y) - 0) / 3 * (H - T - B); }
      [-2, 0, 2, 4].forEach(function (e) { g += tx(sx(Math.pow(10, e)), H - B + 14, e < 0 ? '10 g' : e == 0 ? '1 kg' : e == 2 ? '100 kg' : '10 公噸', 9, 'var(--text-muted)'); });
      [1, 10, 100, 1000].forEach(function (y) { g += ln(L, sy(y), W - R, sy(y), 'var(--border)', 0.6, 'stroke-dasharray="2 3"') + tx(L - 5, sy(y) + 3, y + ' 年', 9, 'var(--text-muted)', 'end'); });
      g += ln(L, H - B, W - R, H - B, '#999') + ln(L, T, L, H - B, '#999') + tx((L + W) / 2, H - 4, '體重（對數）', 9.5, 'var(--text-muted)');
      g += ln(sx(0.005), sy(11.5 * Math.pow(0.005, 0.2)), sx(100000), sy(11.5 * Math.pow(100000, 0.2)), GY, 1.2, 'stroke-dasharray="5 4"') + tx(sx(30000), sy(11.5 * Math.pow(30000, 0.2)) + 16, '依體重預期的趨勢', 9, GY);
      AN.forEach(function (a, i) { var on = i == P.s; g += '<g data-i="' + i + '" style="cursor:pointer"><circle cx="' + n1(sx(a[1])) + '" cy="' + n1(sy(a[2])) + '" r="' + (on ? 8 : 6) + '" fill="' + a[3] + '" stroke="' + (on ? '#222' : 'none') + '" stroke-width="2"/>' + (sx(a[1]) > 560 ? tx(sx(a[1]) - 9, sy(a[2]) - 7, a[0], 10, 'currentColor', 'end') : tx(sx(a[1]) + 9, sy(a[2]) - 7, a[0], 10, 'currentColor', 'start')) + '</g>'; });
      view.innerHTML = svgw('0 0 640 300', g);
      view.querySelectorAll('g[data-i]').forEach(function (e) { e.onclick = function () { P.s = +e.getAttribute('data-i'); draw(); }; });
      var a = AN[P.s]; inf.innerHTML = '<b>' + a[0] + '</b>：最長壽命約 <b>' + a[2] + '</b> 年。' + a[4] + '<br>一般而言，體型越大的動物越長壽（虛線）。但<b>高於虛線</b>的物種——裸鼴鼠、蝙蝠、人類、某些鯨與鯊——特別值得研究：牠們可能擁有對抗老化的機制。<br><span style="font-size:0.9em;color:var(--text-muted)">點選圓點看說明。數值為文獻中常見的約略值。</span>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.lng-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ gomp: initGomp, telo: initTelo, animal: initAnimal })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"⏳", LNG_NOTE, LNGLIB, "lng-w")

GOMP = lw({"t": "gomp", "q": u"岡珀茲定律：如果老化變慢，存活曲線會怎麼變"})
TELO = lw({"t": "telo", "q": u"端粒：細胞分裂的計數器"})
ANIMAL = lw({"t": "animal", "q": u"動物的體型與壽命：誰特別長壽？"})
