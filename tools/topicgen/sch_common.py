# -*- coding: utf-8 -*-
"""〈搜尋引擎與推薦系統〉（sch_）共用：課程包裝與 SCHLIB 互動元件（class="sch-w"）。

  index  倒排索引與 BM25 排序
  pr     PageRank 與連結農場
  cf     協同過濾推薦
  vec    向量搜尋：餘弦相似度
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

SCH_NOTE = u"互動工具使用極小的示範資料，用來說明原理；真實的搜尋引擎與推薦系統規模大上許多個數量級。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def sw(cfg, maxw=680):
    return wdg("sch-w", cfg, maxw)


SCHLIB = r"""
(function () {
  if (window.__schLib) return; window.__schLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  var DOCS = [['台北 夜市 美食 推薦 小吃 夜市', '台北夜市美食推薦'], ['台南 小吃 牛肉湯 美食', '台南小吃地圖'], ['台北 捷運 路線 時刻', '台北捷運路線圖'], ['高雄 夜市 海鮮 美食', '高雄夜市海鮮'],
    ['夜市 歷史 文化 台灣', '台灣夜市的歷史'], ['美食 部落格 食譜 甜點', '美食部落格：甜點食譜'], ['台北 101 景點 夜景', '台北 101 夜景']];
  function initIndex(root, cfg) {
    head(root, cfg.q); var P = { q: '台北 夜市' }, view = el('div'), inf;
    var b = bar(root); ['台北 夜市', '美食', '小吃 台南', '捷運 時刻', '夜景'].forEach(function (q, i) { var x = btn(q, i); x.onclick = function () { P.q = q; mark(b, i); draw(); }; b.appendChild(x); }); mark(b, 0);
    root.appendChild(view); inf = info(root);
    var toks = DOCS.map(function (d) { return d[0].split(' '); }), N = DOCS.length, avg = toks.reduce(function (s, t) { return s + t.length; }, 0) / N, idx = {};
    toks.forEach(function (t, i) { t.forEach(function (w) { (idx[w] = idx[w] || []); if (idx[w].indexOf(i) < 0) idx[w].push(i); }); });
    function draw() { var qs = P.q.split(' '), k1 = 1.5, bb = 0.75, sc = [], h = '<div style="display:flex;gap:12px;flex-wrap:wrap"><div style="flex:1;min-width:220px"><div style="font-size:0.85em;color:' + BL + ';font-weight:bold">倒排索引（部分）</div><table style="font-size:0.88em;border-collapse:collapse">';
      qs.forEach(function (w) { var pl = idx[w] || []; h += '<tr><td style="padding:2px 8px;border-bottom:1px solid var(--border)"><b>' + esc(w) + '</b></td><td style="padding:2px 8px;border-bottom:1px solid var(--border)">→ ' + (pl.length ? pl.map(function (i) { return 'D' + (i + 1); }).join(', ') : '（沒有）') + '</td></tr>'; });
      h += '</table></div><div style="flex:1.4;min-width:260px"><div style="font-size:0.85em;color:' + RD + ';font-weight:bold">BM25 排序結果</div>';
      for (var i = 0; i < N; i++) { var s = 0; qs.forEach(function (w) { var n = (idx[w] || []).length; if (!n) return; var f = toks[i].filter(function (x) { return x == w; }).length; if (!f) return; var idf = Math.log(1 + (N - n + 0.5) / (n + 0.5)); s += idf * f * (k1 + 1) / (f + k1 * (1 - bb + bb * toks[i].length / avg)); }); if (s > 0) sc.push([i, s]); }
      sc.sort(function (a, b2) { return b2[1] - a[1]; }); var mx = sc.length ? sc[0][1] : 1;
      sc.forEach(function (r, k) { h += '<div style="margin:3px 0;font-size:0.9em">' + (k + 1) + '. D' + (r[0] + 1) + '〈' + DOCS[r[0]][1] + '〉<div style="height:6px;background:' + RD + ';opacity:0.7;width:' + Math.round(r[1] / mx * 100) + '%;border-radius:3px"></div><span style="font-size:0.85em;color:var(--text-muted)">分數 ' + f2(r[1]) + '</span></div>'; });
      if (!sc.length) h += '<div style="color:var(--text-muted)">沒有符合的文件</div>';
      view.innerHTML = h + '</div></div>';
      inf.innerHTML = '搜尋引擎事先建好<b>倒排索引</b>：每個詞指向「出現這個詞的文件清單」，查詢時只要把幾個清單合併，不必掃描所有文件。<br>BM25 的分數考慮三件事：詞在文件中出現的<b>次數</b>（但效果遞減）、詞的<b>稀有程度</b>（「夜市」比「美食」少見，分數更高）、文件的<b>長度</b>（短文件中出現更有意義）。<span style="font-size:0.9em;color:var(--text-muted)">（文件已事先斷詞。）</span>'; }
    draw();
  }

  var PG = ['A', 'B', 'C', 'D', 'E', 'F'], PL = { A: ['B', 'C'], B: ['C'], C: ['A'], D: ['C'], E: ['A', 'D'], F: ['E'] }, POS = { A: [140, 70], B: [320, 40], C: [300, 170], D: [470, 140], E: [160, 230], F: [440, 250] };
  function initPR(root, cfg) {
    head(root, cfg.q); var P = { d: 0.85, farm: 0 }, view = el('div'), inf;
    var us = [slider(root, '阻尼係數 d（繼續點連結的機率）', 0.5, 0.95, 0.01, P.d, function (x) { return f2(x); }, null, function (x) { P.d = x; draw(); })];
    var b = bar(root), fb = btn('連結農場：關'); fb.onclick = function () { P.farm ^= 1; fb.textContent = '連結農場：' + (P.farm ? '開（10 個垃圾網頁都連向 F）' : '關'); draw(); }; b.appendChild(fb);
    root.appendChild(view); inf = info(root);
    function draw() { var nodes = PG.slice(), links = {}; nodes.forEach(function (n) { links[n] = PL[n].slice(); });
      if (P.farm) for (var k = 0; k < 10; k++) { var s = 'S' + k; nodes.push(s); links[s] = ['F']; }
      var N = nodes.length, r = {}; nodes.forEach(function (n) { r[n] = 1 / N; });
      for (var it = 0; it < 60; it++) { var nr = {}; nodes.forEach(function (n) { nr[n] = (1 - P.d) / N; }); nodes.forEach(function (n) { var out = links[n]; if (!out.length) { nodes.forEach(function (m) { nr[m] += P.d * r[n] / N; }); } else out.forEach(function (m) { nr[m] += P.d * r[n] / out.length; }); }); r = nr; }
      var tot = 0; PG.forEach(function (n) { tot += r[n]; }); var g = '';
      PG.forEach(function (n) { PL[n].forEach(function (m) { var a = POS[n], c = POS[m], dx = c[0] - a[0], dy = c[1] - a[1], L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L; g += ln(a[0] + ux * 26, a[1] + uy * 26, c[0] - ux * 30, c[1] - uy * 30, '#999', 1.6) + '<path d="M' + n1(c[0] - ux * 30) + ' ' + n1(c[1] - uy * 30) + ' L' + n1(c[0] - ux * 40 - uy * 5) + ' ' + n1(c[1] - uy * 40 + ux * 5) + ' L' + n1(c[0] - ux * 40 + uy * 5) + ' ' + n1(c[1] - uy * 40 - ux * 5) + 'Z" fill="#888"/>'; }); });
      if (P.farm) g += tx(560, 300, '← 10 個垃圾網頁', 10, RD, 'middle') + ln(500, 290, 470, 268, RD, 1.6);
      var mx = 0; PG.forEach(function (n) { mx = Math.max(mx, r[n]); });
      PG.forEach(function (n) { var p = POS[n], rad = 14 + 22 * r[n] / mx; g += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="' + n1(rad) + '" fill="' + (n == 'F' ? OR : BL) + '" opacity="0.85"/>' + tx(p[0], p[1] + 5, n, 13, '#fff') + tx(p[0], p[1] + rad + 14, f1(r[n] / tot * 100) + '%', 10); });
      view.innerHTML = svgw('0 0 640 320', g);
      var top = PG.slice().sort(function (a, b2) { return r[b2] - r[a]; });
      inf.innerHTML = 'PageRank 想像一位「隨機上網者」：每一步以 d 的機率點擊目前網頁上的某個連結，以 1 − d 的機率跳到任意網頁。長期下來，他停留在各網頁的機率就是 PageRank。排名：' + top.join(' ＞ ') + '。' +
        '<br>C 被許多網頁連結，分數最高；被高分網頁連結的 A 也很高。' + (P.farm ? '<b>打開連結農場後</b>，F 的分數大幅上升——這就是早期的 SEO 作弊，搜尋引擎後來用許多方法偵測與懲罰。' : '試著打開「連結農場」。'); }
    us.forEach(function (u) { u(); });
  }

  var MV = ['鬼滅之刃', '進擊的巨人', '你的名字', '神隱少女', '玩命關頭', '不可能的任務'], US = ['小明', '小華', '小美', '阿傑', '你'];
  var R0 = [[5, 5, 2, 1, 1, 0], [4, 5, 0, 2, 0, 1], [1, 2, 5, 5, 0, 1], [1, 0, 1, 2, 5, 4], [5, 0, 0, 1, 0, 0]];
  function initCF(root, cfg) {
    head(root, cfg.q); var R = R0.map(function (r) { return r.slice(); }), view = el('div'), inf; root.appendChild(view); inf = info(root);
    function cos(a, b2) { var s = 0, na = 0, nb = 0; for (var i = 0; i < a.length; i++) if (a[i] && b2[i]) { s += a[i] * b2[i]; na += a[i] * a[i]; nb += b2[i] * b2[i]; } return na && nb ? s / Math.sqrt(na * nb) : 0; }
    function draw() { var me = R[4], sims = [0, 1, 2, 3].map(function (u) { return cos(me, R[u]) * (R[u].filter(function (v, i) { return v && me[i]; }).length > 1 ? 1 : 0.6); });
      var pred = MV.map(function (m, i) { if (me[i]) return null; var s = 0, w = 0; for (var u = 0; u < 4; u++) if (R[u][i]) { s += sims[u] * R[u][i]; w += sims[u]; } return w ? s / w : null; });
      var h = '<table style="width:100%;border-collapse:collapse;font-size:0.88em;text-align:center"><tr><th></th>' + MV.map(function (m) { return '<th style="padding:3px;font-weight:normal;font-size:0.9em">' + m + '</th>'; }).join('') + '<th style="font-weight:normal">相似度</th></tr>';
      R.forEach(function (row, u) { h += '<tr><td style="padding:3px;text-align:left"><b>' + US[u] + '</b></td>'; row.forEach(function (v, i) { var isMe = u == 4, p = isMe && !v ? pred[i] : null;
          h += '<td data-u="' + u + '" data-i="' + i + '" style="padding:4px;border:1px solid var(--border);' + (isMe ? 'cursor:pointer;' : '') + (v ? 'background:rgba(217,130,43,' + (v / 6) + ')' : p ? 'background:rgba(74,154,94,0.15);color:' + GN : '') + '">' + (v ? '★' + v : p ? '預測 ' + f1(p) : '·') + '</td>'; });
        h += '<td>' + (u < 4 ? f2(sims[u]) : '—') + '</td></tr>'; });
      view.innerHTML = h + '</table>';
      view.querySelectorAll('td[data-u="4"]').forEach(function (td) { td.onclick = function () { var i = +td.getAttribute('data-i'); R[4][i] = (R[4][i] + 1) % 6; draw(); }; });
      var best = -1, bi = -1; pred.forEach(function (p, i) { if (p !== null && p > best) { best = p; bi = i; } });
      inf.innerHTML = '點「你」那一列的格子，給電影打分數（每點一次加一顆星，到 5 再回到空白）。系統找出和你口味最相似的使用者（餘弦相似度），用他們的評分預測你還沒看過的電影。' + (bi >= 0 ? '<br>目前最推薦：<b>' + MV[bi] + '</b>（預測 ' + f1(best) + ' 顆星）。' : '') + '<br>這就是<b>以使用者為基礎的協同過濾</b>：不需要知道電影的內容，只靠「和你相似的人喜歡什麼」。'; }
    draw();
  }

  var VS = [['貓', 0.9, 0.2, '動物'], ['狗', 0.85, 0.3, '動物'], ['老虎', 0.75, 0.05, '動物'], ['蘋果', 0.22, 0.92, '食物'], ['香蕉', -0.08, 0.86, '食物'], ['披薩', 0.3, 0.75, '食物'], ['寵物飼料', 0.65, 0.6, '兩者之間'], ['iPhone', -0.6, 0.55, '科技'], ['筆電', -0.75, 0.35, '科技'], ['程式', -0.85, 0.1, '科技']];
  function initVec(root, cfg) {
    head(root, cfg.q); var P = { q: 0 }, view = el('div'), inf;
    var b = bar(root); VS.forEach(function (v, i) { var x = btn(v[0], i); x.onclick = function () { P.q = i; mark(b, i); draw(); }; b.appendChild(x); }); mark(b, 0);
    root.appendChild(view); inf = info(root);
    function draw() { var q = VS[P.q], cx = 320, cy = 200, S = 160, g = '', sims = VS.map(function (v, i) { return [i, (v[1] * q[1] + v[2] * q[2]) / (Math.hypot(v[1], v[2]) * Math.hypot(q[1], q[2]))]; }).filter(function (s) { return s[0] != P.q; }).sort(function (a, b2) { return b2[1] - a[1]; });
      g += ln(cx - 190, cy, cx + 190, cy, '#ccc') + ln(cx, cy - 190, cx, cy + 20, '#ccc');
      VS.forEach(function (v, i) { var x = cx + v[1] * S, y = cy - v[2] * S, top = sims.slice(0, 3).some(function (s) { return s[0] == i; }), me = i == P.q;
        g += ln(cx, cy, x, y, me ? RD : top ? GN : '#ddd', me ? 2.5 : top ? 2 : 1) + '<circle cx="' + n1(x) + '" cy="' + n1(y) + '" r="' + (me ? 7 : 5) + '" fill="' + (me ? RD : top ? GN : GY) + '"/>' + tx(x + (v[1] < 0 ? -8 : 8), y - 6, v[0], 11, me ? RD : 'currentColor', v[1] < 0 ? 'end' : 'start'); });
      view.innerHTML = svgw('0 0 640 230', g);
      inf.innerHTML = '每個詞（或文件）被表示成一個<b>向量</b>，意思相近的向量指向相近的方向。查詢「' + q[0] + '」時，用<b>餘弦相似度</b>（兩個向量夾角的 cos）找最接近的：' + sims.slice(0, 3).map(function (s) { return VS[s[0]][0] + '（' + f2(s[1]) + '）'; }).join('、') + '。' +
        '<br>即使沒有任何相同的字，向量搜尋也能找到意思相近的內容。<span style="font-size:0.9em;color:var(--text-muted)">（真實的嵌入向量有數百到數千維，這裡用二維示意。）</span>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.sch-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ index: initIndex, pr: initPR, cf: initCF, vec: initVec })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🔎", SCH_NOTE, SCHLIB, "sch-w")

INDEX = sw({"t": "index", "q": u"倒排索引與 BM25：搜尋引擎怎麼找、怎麼排"})
PR = sw({"t": "pr", "q": u"PageRank：被重要的網頁連結，就更重要"})
CF = sw({"t": "cf", "q": u"協同過濾：和你口味相似的人喜歡什麼"})
VEC = sw({"t": "vec", "q": u"向量搜尋：用「方向」找意思相近的內容"})
