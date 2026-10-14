# -*- coding: utf-8 -*-
"""〈皇宮裡的人與官〉（pg_）共用：課程包裝與 PGLIB 互動元件。

PGLIB 元件（class="pg-w"）：
  map    紫禁城互動平面圖（示意，大致比例）
  org    歷代中央官制組織圖
  rank   清代品級：補服、頂戴、俸祿與代表官職
  pop    皇宮人口：史料記載與學者估計（對數尺度）
  roof   屋頂等級與屋脊走獸
另沿用 kd_common 的 tree（情境決策樹）與 nv_common 的卡片、時間軸。
"""
from cc_common import make_lesson, wdg, LS
from qt_common import BASEJS
from nv_common import NVLIB, nvw, ev, card, CB, CG, CO, CR, CP, CT, CY, CK
from kd_common import KDLIB, tree, XO

PG_NOTE = (u"本課程整理正史、會典、清宮檔案與當代研究（2026 年 10 月查證）。古代的人數常有誇大或記載不全，課文會盡量把<strong>史料記載</strong>與<strong>學者估計</strong>分開說明；"
           u"官名與職掌在同一朝代內也常有變化，表格呈現的是代表性的情況。")

EM = XO("emperor-life", u"皇帝的一天")

PGLIB = r"""
(function () {
  if (window.__pgLib) return; window.__pgLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }

  /* ---------- 紫禁城平面圖 ---------- */
  function initMap(root, cfg) {
    head(root, cfg.q); var G = cfg.groups, B = cfg.b, sel = null, flt = 'all', bb = bar(root), out = el('div', 'max-width:520px;margin:8px auto 0'), p;
    var bt = btn('全部', 'all'); bt.addEventListener('click', function () { flt = 'all'; mark(bb, 'all'); draw(); }); bb.appendChild(bt);
    Object.keys(G).forEach(function (k) { var b = btn(G[k][0], k); b.addEventListener('click', function () { flt = k; mark(bb, k); draw(); }); bb.appendChild(b); });
    root.appendChild(out); p = info(root);
    function draw() { var g = '<rect x="20" y="20" width="360" height="460" fill="none" stroke="#a33" stroke-width="5"/>' +
        '<rect x="8" y="8" width="384" height="484" fill="none" stroke="#6aa3c9" stroke-width="5" opacity="0.5"/>' + ln(200, 20, 200, 480, '#c9a', 1, 'stroke-dasharray="4 4"');
      B.forEach(function (b, i) { var on = flt === 'all' || b[5] === flt, c = G[b[5]][1], s = sel === i;
        g += '<g data-i="' + i + '" style="cursor:pointer"><rect x="' + b[1] + '" y="' + b[2] + '" width="' + b[3] + '" height="' + b[4] + '" rx="2" fill="' + c + '" fill-opacity="' + (on ? (s ? 0.95 : 0.6) : 0.12) + '" stroke="' + (s ? '#222' : c) + '" stroke-width="' + (s ? 2 : 0.8) + '"/>';
        if (b[7]) g += tx(b[1] + b[3] / 2, b[2] + b[4] / 2 + 3.5, b[0], b[7], on ? '#222' : '#999');
        g += '</g>'; });
      g += tx(200, 500, '↑ 北（神武門）　示意圖，大致比例　午門（南）↓', 9, 'var(--text-muted)');
      out.innerHTML = svgw('0 0 400 506', g);
      out.querySelectorAll('g[data-i]').forEach(function (n) { n.addEventListener('click', function () { sel = +n.getAttribute('data-i'); draw(); }); });
      if (sel === null) p.innerHTML = '點平面圖上的建築看說明。紅框是宮城城牆（南北約 961 公尺、東西約 753 公尺），外圈藍色是寬約 52 公尺的護城河（筒子河）。虛線是<b>中軸線</b>。';
      else { var b = B[sel]; p.innerHTML = '<b style="color:' + G[b[5]][1] + '">' + b[0] + '</b>　<span style="font-size:0.85em;color:var(--text-muted)">' + G[b[5]][0] + '</span><br>' + b[6]; } }
    mark(bb, 'all'); draw();
  }

  /* ---------- 歷代官制組織圖 ---------- */
  function initOrg(root, cfg) {
    head(root, cfg.q); var D = cfg.d, keys = Object.keys(D), cur = cfg.start || keys[0], bb = bar(root), out = el('div', 'margin-top:8px'), p;
    keys.forEach(function (k) { var b = btn(k, k); b.addEventListener('click', function () { cur = k; mark(bb, k); draw(); }); bb.appendChild(b); });
    root.appendChild(out); p = info(root);
    var flat = [];
    function node(n, d) { var i = flat.length; flat.push(n); var kids = n[2] || [], c = ['#b8862b', '#3a6ea5', '#5aa469', '#9c89d6'][Math.min(d, 3)];
      var h = '<div style="margin:4px 0 4px ' + (d ? 14 : 0) + 'px;border-left:' + (d ? '2px solid var(--border)' : 'none') + ';padding-left:' + (d ? 8 : 0) + 'px">' +
        '<button type="button" data-o="' + i + '" style="padding:4px 10px;border-radius:8px;border:1px solid ' + c + ';border-left:5px solid ' + c + ';background:var(--surface);color:var(--text);cursor:pointer;font:inherit;font-size:0.92em;text-align:left">' + n[0] + '</button>';
      if (kids.length) { var row = kids.every(function (k) { return !(k[2] && k[2].length); }) && kids.length > 2;
        h += '<div style="' + (row ? 'display:flex;flex-wrap:wrap;gap:0 2px;' : '') + '">' + kids.map(function (k) { return node(k, d + 1); }).join('') + '</div>'; }
      return h + '</div>'; }
    function draw() { flat = []; out.innerHTML = node(D[cur].tree, 0);
      out.querySelectorAll('button[data-o]').forEach(function (b) { b.addEventListener('click', function () { var n = flat[+b.getAttribute('data-o')];
        out.querySelectorAll('button[data-o]').forEach(function (x) { x.style.background = 'var(--surface)'; }); b.style.background = 'var(--accent-soft)';
        p.innerHTML = '<b>' + n[0] + '</b>：' + n[1]; }); });
      p.innerHTML = D[cur].note; }
    mark(bb, cur); draw();
  }

  /* ---------- 清代品級 ---------- */
  function initRank(root, cfg) {
    head(root, cfg.q); var R = cfg.r, lv = 1, mil = false, b1 = bar(root), b2 = bar(root), out = el('div', 'display:flex;flex-wrap:wrap;gap:12px;align-items:flex-start;margin-top:8px'), p;
    for (var i = 1; i <= 9; i++) (function (i) { var b = btn(['一', '二', '三', '四', '五', '六', '七', '八', '九'][i - 1] + '品', 'l' + i); b.addEventListener('click', function () { lv = i; mark(b1, 'l' + i); draw(); }); b1.appendChild(b); })(i);
    [['文官', 'c'], ['武官', 'm']].forEach(function (x) { var b = btn(x[0], x[1]); b.addEventListener('click', function () { mil = x[1] === 'm'; mark(b2, x[1]); draw(); }); b2.appendChild(b); });
    root.appendChild(out); p = info(root);
    function draw() { var r = R[lv - 1], an = mil ? r.m : r.c, col = mil ? '#7a4b2a' : '#2a5c7a';
      var badge = '<rect x="6" y="6" width="128" height="128" rx="6" fill="#1d2a44" stroke="#c9a23b" stroke-width="4"/><rect x="16" y="16" width="108" height="108" rx="4" fill="none" stroke="#c9a23b" stroke-width="1" stroke-dasharray="3 3"/>' +
        '<circle cx="104" cy="34" r="12" fill="#d0564f"/>' + '<path d="M16 110 Q40 96 70 110 T124 110" fill="none" stroke="#6aa3c9" stroke-width="3"/>' +
        tx(70, 80, an, an.length > 2 ? 22 : 28, '#f3e3b5') + tx(70, 104, mil ? '武官補子' : '文官補子', 10, '#c9a23b');
      var hat = '<path d="M20 70 Q70 30 120 70 Z" fill="#333"/><rect x="18" y="68" width="104" height="10" rx="5" fill="#222"/><path d="M40 66 Q70 50 100 66" stroke="#b33" stroke-width="7" fill="none"/>' +
        '<circle cx="70" cy="32" r="12" fill="' + r.hc + '" stroke="#333"/>' + tx(70, 100, r.h, 11, 'currentColor');
      out.innerHTML = '<div style="flex:0 0 140px">' + svgw('0 0 140 140', badge) + '</div><div style="flex:0 0 140px">' + svgw('0 0 140 110', hat) + '</div>' +
        '<div style="flex:1 1 220px;line-height:1.7"><b style="color:' + col + ';font-size:1.1em">' + ['一', '二', '三', '四', '五', '六', '七', '八', '九'][lv - 1] + '品' + (mil ? '武官' : '文官') + '</b><br>補子圖案：<b>' + an + '</b><br>朝冠頂珠：<b>' + r.h + '</b><br>' +
        (mil ? '' : '年俸（正' + ['一', '二', '三', '四', '五', '六', '七', '八', '九'][lv - 1] + '品）：<b>銀 ' + r.s + ' 兩</b><br>') + '代表官職：' + (mil ? r.me : r.ce) + '</div>';
      p.innerHTML = '口訣：「<b>文禽武獸</b>」——文官補子繡鳥，武官補子繡獸。同一品分「正」「從」兩級，九品共十八級。<br><span style="font-size:0.88em;color:var(--text-muted)">圖案為清代制度（明代略有不同）；頂珠顏色是示意。俸銀為《大清會典》所載文官正品年俸，京官另有約同數的祿米；雍正以後地方官另有遠高於俸銀的「養廉銀」。</span>'; }
    mark(b1, 'l1'); mark(b2, 'c'); draw();
  }

  /* ---------- 皇宮人口（對數尺度） ---------- */
  function initPop(root, cfg) {
    head(root, cfg.q); var D = cfg.d, keys = ['全部'].concat(cfg.dyn), cur = '全部', bb = bar(root), out = el('div', 'margin-top:8px;overflow-x:auto'), p;
    var K = { r: ['史料記載', '#3a6ea5'], e: ['學者估計', '#5aa469'], c: ['傳聞或可能誇大', '#d9822b'] };
    keys.forEach(function (k) { var b = btn(k, k); b.addEventListener('click', function () { cur = k; mark(bb, k); draw(); }); bb.appendChild(b); });
    root.appendChild(out); p = info(root);
    function draw() { var rows = D.filter(function (d) { return cur === '全部' || d[0] === cur; }), W = 640, L = 210, Rr = 78, rh = 30, H = rows.length * rh + 46, g = '';
      function sx(v) { return L + (Math.log10(v) - 2) / 3 * (W - L - Rr); }
      [100, 1000, 10000, 100000].forEach(function (v) { g += ln(sx(v), 14, sx(v), H - 26, 'var(--border)', 0.8, 'stroke-dasharray="3 3"') + tx(sx(v), H - 12, v.toLocaleString(), 10, 'var(--text-muted)'); });
      rows.forEach(function (d, i) { var y = 20 + i * rh, c = K[d[4]][1];
        g += tx(L - 8, y + 12, d[0] + '｜' + d[1], 10.5, 'currentColor', 'end');
        if (d[2] === d[3]) g += '<circle cx="' + n1(sx(d[2])) + '" cy="' + (y + 8) + '" r="6" fill="' + c + '"/>';
        else g += '<rect x="' + n1(sx(d[2])) + '" y="' + (y + 2) + '" width="' + n1(Math.max(4, sx(d[3]) - sx(d[2]))) + '" height="12" rx="6" fill="' + c + '"/>';
        g += tx(sx(d[3]) + 8, y + 12, d[2] === d[3] ? d[2].toLocaleString() : d[2].toLocaleString() + '～' + d[3].toLocaleString(), 9.5, c, 'start'); });
      out.innerHTML = '<div style="min-width:520px">' + svgw('0 0 ' + W + ' ' + H, g) + '</div>';
      p.innerHTML = Object.keys(K).map(function (k) { return '<span style="display:inline-block;width:10px;height:10px;border-radius:5px;background:' + K[k][1] + ';margin-right:4px"></span>' + K[k][0]; }).join('　') +
        '<br>' + rows.map(function (d) { return '<b>' + d[0] + '｜' + d[1] + '</b>：' + d[5]; }).join('<br>') + '<br><span style="font-size:0.88em;color:var(--text-muted)">橫軸是對數尺度：每一格是十倍。</span>'; }
    mark(bb, cur); draw();
  }

  /* ---------- 屋頂等級與走獸 ---------- */
  function initRoof(root, cfg) {
    head(root, cfg.q); var R = cfg.roofs, k = 0, n = 10, b1 = bar(root), out = el('div', 'max-width:420px;margin:8px auto 0'), p1 = info(root), h2 = el('div', 'margin-top:12px;font-weight:bold', '屋脊走獸：選數目'), b2, out2 = el('div', 'margin-top:6px'), p2;
    R.forEach(function (r, i) { var b = btn((i + 1) + '. ' + r[0], 'r' + i); b.addEventListener('click', function () { k = i; mark(b1, 'r' + i); draw(); }); b1.appendChild(b); });
    root.appendChild(out); root.appendChild(p1); root.appendChild(h2); b2 = bar(root); root.appendChild(out2); p2 = info(root);
    [10, 9, 7, 5, 3, 1].forEach(function (v) { var b = btn(v + ' 隻', 'n' + v); b.addEventListener('click', function () { n = v; mark(b2, 'n' + v); draw2(); }); b2.appendChild(b); });
    function roof(t) { var Y = '#e0b43b', S = '#8a6a20', w = '<rect x="90" y="150" width="220" height="60" fill="#b33"/>' + '<rect x="80" y="210" width="240" height="10" fill="#ccc"/>', r = '';
      function hip(y0, y1, x0, x1, xr0, xr1) { return '<polygon points="' + x0 + ',' + y1 + ' ' + x1 + ',' + y1 + ' ' + xr1 + ',' + y0 + ' ' + xr0 + ',' + y0 + '" fill="' + Y + '" stroke="' + S + '"/>' + ln(xr0, y0, xr1, y0, S, 3); }
      if (t === 'w2') r = hip(118, 150, 70, 330, 110, 290) + hip(60, 108, 100, 300, 150, 250) + '<rect x="110" y="108" width="180" height="12" fill="#b33"/>';
      else if (t === 'x2') r = hip(118, 150, 70, 330, 110, 290) + '<rect x="110" y="96" width="180" height="22" fill="#b33"/>' + hip(76, 98, 96, 304, 130, 270) + '<polygon points="140,76 260,76 230,40 170,40" fill="' + Y + '" stroke="' + S + '"/>' + ln(170, 40, 230, 40, S, 3);
      else if (t === 'w1') r = hip(70, 150, 70, 330, 140, 260);
      else if (t === 'x1') r = hip(110, 150, 70, 330, 110, 290) + '<polygon points="130,110 270,110 240,62 160,62" fill="' + Y + '" stroke="' + S + '"/>' + '<polygon points="150,110 170,62 170,110" fill="#c9952b" opacity="0.6"/>' + ln(160, 62, 240, 62, S, 3);
      else if (t === 'xs') r = '<polygon points="66,150 334,150 334,60 66,60" fill="none"/>' + '<polygon points="66,150 200,64 334,150" fill="' + Y + '" stroke="' + S + '"/>' + ln(66, 150, 90, 150, S, 2) + ln(310, 150, 334, 150, S, 2) + tx(200, 140, '屋頂兩端伸出山牆', 10, '#333');
      else if (t === 'ys') r = '<rect x="84" y="80" width="18" height="72" fill="#888"/><rect x="298" y="80" width="18" height="72" fill="#888"/>' + '<polygon points="90,150 200,66 310,150" fill="' + Y + '" stroke="' + S + '"/>' + tx(200, 140, '山牆與屋頂齊平', 10, '#333');
      else if (t === 'cj') r = '<polygon points="80,150 320,150 200,40" fill="' + Y + '" stroke="' + S + '"/><circle cx="200" cy="38" r="8" fill="#c9a23b" stroke="' + S + '"/>';
      return svgw('0 0 400 230', r + w); }
    function draw() { var r = R[k]; out.innerHTML = roof(r[1]); p1.innerHTML = '<b>' + r[0] + '</b>　' + r[2] + '<br>例：' + r[3]; }
    function draw2() { var A = cfg.beasts, h = '<div style="display:flex;flex-wrap:wrap;gap:4px;align-items:center"><span style="padding:4px 8px;border-radius:6px;background:#9c89d6;color:#fff;font-size:0.9em">騎鳳仙人</span>';
      for (var i = 0; i < n; i++) h += '<span style="padding:4px 8px;border-radius:6px;background:#e0b43b;color:#3a2a00;font-size:0.9em">' + (i + 1) + '. ' + A[i] + '</span>';
      out2.innerHTML = h + '</div>'; p2.innerHTML = n === 10 ? '<b>10 隻只有太和殿</b>，是全中國古建築中唯一的例子，多出的第十隻是「行什」（一位帶翅膀、像猴子的神將）。' :
        '其他建築依等級遞減，多用 9、7、5、3、1 這樣的單數；等級越高，數目越多。走獸前面的「騎鳳仙人」不算在數目裡。<br><span style="font-size:0.88em;color:var(--text-muted)">走獸固定在屋脊末端，本身也有保護瓦釘、防止瓦片滑落的實際功能。</span>'; }
    mark(b1, 'r0'); mark(b2, 'n10'); draw(); draw2();
  }

  function initAll() { document.querySelectorAll('.pg-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ map: initMap, org: initOrg, rank: initRank, pop: initPop, roof: initRoof })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def pgw(cfg, maxw=720):
    return wdg("pg-w", cfg, maxw)


# ---------- 紫禁城建築（名稱, x, y, w, h, 群組, 說明, 標籤字級 0=不標） ----------
_GROUPS = {"o": [u"外朝", "#d0564f"], "i": [u"內廷正殿", "#e0a030"], "l": [u"后妃、太后居所", "#c8506a"], "w": [u"辦公與機構", "#3a6ea5"], "g": [u"花園、宗教、城門", "#5aa469"]}
_B = [
    [u"午門", 150, 446, 100, 30, "g", u"紫禁城正門，平面呈「凹」字形，俗稱「五鳳樓」。頒布曆書、出征與凱旋獻俘的典禮在這裡舉行；明代曾在午門外執行「廷杖」。戲曲中的「推出午門斬首」是誤解，死刑一般在城外的刑場執行。", 10],
    [u"金水橋", 165, 422, 70, 10, "g", u"內金水河上的五座漢白玉橋，中間一座是皇帝走的「御路橋」。金水河兼具排水與防火取水的功能。", 0],
    [u"太和門", 165, 395, 70, 18, "o", u"外朝的正門。明代與清初，皇帝有時在這裡「御門聽政」；清代康熙以後改在乾清門。", 8],
    [u"太和殿", 140, 293, 120, 40, "o", u"俗稱「金鑾殿」，紫禁城等級最高、規模最大的建築：重簷廡殿頂、屋脊走獸 10 隻。登基、大婚、元旦、冬至、皇帝生日等大典在這裡舉行；平常並不在此辦公。明代稱奉天殿、皇極殿，清順治二年（1645）改稱太和殿；現存建築是康熙年間重建。", 11],
    [u"中和殿", 180, 272, 40, 16, "o", u"方形的攢尖頂小殿。皇帝去太和殿參加大典前在這裡休息、接受執事官員行禮。", 7],
    [u"保和殿", 150, 247, 100, 20, "o", u"除夕與元宵宴請王公大臣的地方；乾隆後期起，科舉最高一級的「殿試」在這裡舉行。", 9],
    [u"乾清門", 170, 222, 60, 12, "i", u"內廷的正門，也是外朝與內廷的分界。清代康熙常在這裡「御門聽政」，清晨聽各部院官員奏事。", 7],
    [u"乾清宮", 160, 189, 80, 26, "i", u"明代與清初皇帝的寢宮兼日常辦公處。殿內高懸順治御書「正大光明」匾；雍正以後，祕密立儲的傳位詔書就藏在匾後。雍正起皇帝改住養心殿，這裡仍用來召見、舉行內廷典禮。", 9],
    [u"交泰殿", 182, 170, 36, 14, "i", u"方形小殿。清代存放皇帝的二十五方寶璽（印章）；皇后生日在這裡受賀。", 6],
    [u"坤寧宮", 162, 145, 76, 20, "i", u"明代皇后的寢宮。清代改成薩滿祭祀的場所，東側暖閣作為皇帝大婚的洞房。", 8],
    [u"御花園", 140, 76, 120, 56, "g", u"內廷北端的皇家花園，有亭台、假山、古柏與「堆秀山」。後宮的人能在這裡散步賞景；清代選秀女時也曾在附近進行。", 10],
    [u"神武門", 170, 22, 60, 16, "g", u"紫禁城北門，明代稱玄武門，清代為避康熙名諱（玄燁）改稱神武門。宮女、太監與日常物資多由這裡進出；今天是故宮博物院的出口。", 8],
    [u"養心殿", 120, 178, 34, 26, "w", u"雍正以後清代皇帝真正的寢宮與辦公室，八位皇帝住過。東暖閣是慈禧「垂簾聽政」的地方；西暖閣有乾隆的書房「三希堂」。", 7],
    [u"軍機處", 158, 222, 10, 10, "w", u"乾清門西側一排簡樸的平房，是軍機大臣的值班房。雍正年間設立後，成為清代實際處理機要的中樞，離皇帝住的養心殿只有幾十步。", 0],
    [u"西六宮", 74, 104, 64, 70, "l", u"內廷西側的六座宮院（如永壽宮、翊坤宮、儲秀宮、長春宮），是后妃的住處；慈禧早年就住在儲秀宮。", 9],
    [u"東六宮", 262, 104, 64, 70, "l", u"內廷東側的六座宮院（如景仁宮、承乾宮、鍾粹宮、延禧宮），是后妃的住處。", 9],
    [u"慈寧宮", 54, 206, 52, 46, "l", u"太后居住的宮殿，西側有慈寧宮花園。康熙的祖母孝莊太皇太后曾住在這裡。", 8],
    [u"壽康宮", 40, 160, 30, 30, "l", u"乾隆為母親崇慶皇太后所建，之後是太妃們的住所。", 6],
    [u"建福宮花園", 34, 92, 36, 34, "g", u"乾隆時修建的花園，1923 年大火燒毀，近年已重建。", 5],
    [u"武英殿", 70, 380, 60, 26, "w", u"外朝西側。清代設「武英殿修書處」，編校、刻印書籍，所印的書稱為「殿本」。", 8],
    [u"內務府", 34, 320, 44, 36, "w", u"清代管理皇家事務的龐大機構（衙署在西華門內一帶），下設七司三院，負責皇室的財務、飲食、工程、典禮與包衣人員。", 7],
    [u"文華殿", 270, 380, 60, 26, "w", u"外朝東側。明代曾是太子的宮殿，後來用作「經筵」——大臣為皇帝講解經史的課堂。今天是陶瓷館。", 8],
    [u"文淵閣", 285, 350, 32, 18, "w", u"乾隆年間仿寧波天一閣建造，用來收藏《四庫全書》。", 6],
    [u"箭亭", 280, 280, 34, 22, "w", u"清代皇帝與皇子練習騎射、考核武舉的地方，提醒子孫不要忘記「騎射」家法。", 7],
    [u"奉先殿", 248, 200, 30, 30, "g", u"皇家在宮內的家廟，供奉祖先牌位。", 6],
    [u"寧壽宮區", 330, 60, 44, 230, "l", u"乾隆為自己退位後的生活而建的一整區宮殿：皇極殿、寧壽宮、養性殿、樂壽堂與「乾隆花園」，前面有著名的九龍壁。今天是珍寶館。", 8],
    [u"東華門", 370, 386, 12, 22, "g", u"紫禁城東門。清代大臣上朝多由此進出；清代皇帝、皇后的靈柩也從東華門出宮。", 0],
    [u"西華門", 18, 386, 12, 22, "g", u"紫禁城西門，通往西苑（今中南海）與內務府一帶。", 0],
    [u"角樓", 22, 22, 14, 14, "g", u"城牆四角各有一座角樓，造型複雜，常以「九梁十八柱七十二條脊」形容，是紫禁城最常被拍攝的建築之一。", 0],
    [u"角樓（東北）", 364, 22, 14, 14, "g", u"城牆四角的角樓之一。", 0],
    [u"角樓（西南）", 22, 464, 14, 14, "g", u"城牆四角的角樓之一。", 0],
    [u"角樓（東南）", 364, 464, 14, 14, "g", u"城牆四角的角樓之一。", 0],
]
MAP = pgw({"t": "map", "q": u"紫禁城互動平面圖：點建築看用途；上方按鈕可以只顯示某一類", "groups": _GROUPS, "b": _B}, 620)


# ---------- 官制組織圖 ----------
def N(name, desc, kids=None):
    return [name, desc] + ([kids] if kids else [])


_ORG = {
    u"秦漢": {"note": u"秦朝建立、漢朝沿用的<b>三公九卿</b>：丞相總管行政，太尉管軍事，御史大夫負責監察並協助丞相。九卿分管具體事務，其中好幾個其實是在管「皇帝家」的事。點任一方塊看說明。",
           "tree": N(u"皇帝", u"國家最高統治者，自秦始皇起稱「皇帝」。", [
               N(u"三公", u"最高的三位大臣，地位最高、俸祿最多。", [N(u"丞相", u"總理全國行政，是百官之首。漢武帝以後權力逐漸被內朝分走。"), N(u"太尉", u"最高軍事長官，但調兵仍需皇帝的虎符。"), N(u"御史大夫", u"副丞相兼監察百官，管理圖籍與奏章。")]),
               N(u"九卿", u"三公以下分管具體事務的九位長官（漢代名稱多經更改，以下列漢代常用名）。", [
                   N(u"太常", u"宗廟祭祀與禮儀，也管太史、太醫、博士。"), N(u"光祿勳", u"宮殿門戶與皇帝身邊的侍從、郎官。"), N(u"衛尉", u"宮門與宮城的警衛。"),
                   N(u"太僕", u"皇帝的車馬與全國馬政。"), N(u"廷尉", u"最高司法官，審理重大案件。"), N(u"大鴻臚", u"接待諸侯與外族使節（相當於外交與民族事務）。"),
                   N(u"宗正", u"管理皇族事務與宗室名冊。"), N(u"大司農", u"國家財政：田租、糧食、鹽鐵。"), N(u"少府", u"皇室的財政與宮中用度、手工業，屬下還有尚書。")]),
               N(u"內朝（中朝）", u"漢武帝起，皇帝身邊的親信與秘書逐漸組成「內朝」，分走外朝丞相的決策權。", [N(u"尚書", u"原是少府下管文書的小官，東漢時「尚書台」成為實際的中樞。"), N(u"侍中、中常侍", u"皇帝身邊的近侍；東漢的中常侍由宦官擔任，權力極大。"), N(u"大將軍", u"西漢中後期常由外戚擔任，統領內朝，如霍光。")])])},
    u"唐": {"note": u"隋朝建立、唐朝完善的<b>三省六部制</b>：中書省起草詔令，門下省審核（可以退回，稱「封駁」），尚書省執行並下轄六部。宰相權力分給三省長官，互相牽制。",
          "tree": N(u"皇帝", u"唐代皇帝與宰相在政事堂共同議事。", [
              N(u"中書省", u"秉承皇帝旨意起草詔令，長官為中書令。負責「出令」。"),
              N(u"門下省", u"審核中書省的詔令，認為不妥可以「封駁」退回；長官為侍中。"),
              N(u"尚書省", u"執行機關，長官為尚書令（因唐太宗曾任此職，後來不再授人，由左右僕射主持）。", [
                  N(u"吏部", u"官員的選拔、考核、升降。下轄吏部、司封、司勳、考功四司。"), N(u"戶部", u"戶口、土地、賦稅、財政。下轄戶部、度支、金部、倉部四司。"),
                  N(u"禮部", u"禮儀、祭祀、學校、科舉、外交接待。"), N(u"兵部", u"武官選拔、軍籍、兵器、驛站。"), N(u"刑部", u"刑法、審核案件、監獄。"), N(u"工部", u"工程、屯田、水利、手工業。")]),
              N(u"御史台", u"監察百官，長官為御史大夫。"), N(u"九寺五監", u"處理事務性工作的機構，例如太常寺（禮樂）、大理寺（審案）、鴻臚寺（外賓）、國子監（教育）、將作監（營造）。"),
              N(u"內侍省", u"管理宮中事務的宦官機構。唐中期以後宦官掌握禁軍（神策軍），甚至能廢立皇帝。")])},
    u"宋": {"note": u"宋代為了防止大臣專權，把權力拆得更細：<b>二府三司</b>——中書門下管行政、樞密院管軍事、三司管財政，三者互不統屬，都直接對皇帝負責。神宗元豐年間改制，又恢復了三省的名稱。",
          "tree": N(u"皇帝", u"宋代皇帝重用文官，相傳太祖立下「不殺士大夫」的祖訓。", [
              N(u"中書門下（政事堂）", u"宰相機構，宰相稱「同中書門下平章事」，副相稱「參知政事」。管行政。"),
              N(u"樞密院", u"最高軍事機構，管調兵與軍政，但不直接統兵；統兵的將領由皇帝另派。與中書門下合稱「二府」。"),
              N(u"三司", u"最高財政機構，號稱「計相」。", [N(u"鹽鐵", u"工商業收入、鹽鐵專賣、兵器。"), N(u"度支", u"財政收支與糧食運輸。"), N(u"戶部", u"戶口、賦稅、酒稅。")]),
              N(u"御史台與諫院", u"監察百官與批評朝政；宋代「台諫」的地位很高。"), N(u"翰林學士院", u"替皇帝起草重要詔令的文學侍從，常被視為宰相的儲備人選。")])},
    u"明": {"note": u"明太祖朱元璋在 1380 年廢除中書省與丞相，六部直接對皇帝負責。後來設<b>內閣</b>協助處理奏章（「票擬」），宦官的<b>司禮監</b>代皇帝用紅筆批示（「批紅」），形成文官與宦官互相制衡、也互相依賴的結構。",
          "tree": N(u"皇帝", u"明代皇帝名義上直接統領六部，工作量極大。", [
              N(u"內閣", u"由翰林出身的「大學士」組成，替皇帝閱讀奏章、草擬處理意見（票擬）。首輔權力大時近似宰相，如張居正。"),
              N(u"司禮監", u"宦官二十四衙門之首。秉筆太監代皇帝「批紅」，掌印太監管理內外文書，權勢極大，如王振、劉瑾、魏忠賢。"),
              N(u"六部", u"吏、戶、禮、兵、刑、工，長官為尚書，直接對皇帝負責。", [N(u"吏部", u"官員任免考核，尚書稱「天官」。"), N(u"戶部", u"戶口、田賦、財政。"), N(u"禮部", u"禮儀、科舉、外交。"), N(u"兵部", u"軍政與武官。"), N(u"刑部", u"刑法與審判。"), N(u"工部", u"工程與營造。")]),
              N(u"都察院", u"最高監察機關，御史「風聞奏事」；與刑部、大理寺合稱「三法司」。"), N(u"六科給事中", u"對應六部的監察官，可以封還詔書、稽查六部。"),
              N(u"通政使司", u"收受全國奏章、轉呈皇帝。"), N(u"大理寺", u"複核刑案。"), N(u"翰林院", u"文學侍從、修史；內閣大學士多由此出身。"),
              N(u"五軍都督府", u"統領軍隊，但調兵權在兵部，形成互相牽制。"), N(u"錦衣衛、東廠", u"皇帝直屬的偵緝機構，錦衣衛由武官、東廠由宦官主持。")])},
    u"清": {"note": u"清代沿用明代的內閣與六部，但雍正年間設立<b>軍機處</b>，成為實際的決策中樞：軍機大臣每天在養心殿面見皇帝，承旨後直接寄發「廷寄」給地方大員。內廷事務則交由<b>內務府</b>管理，宦官權力受到嚴格限制。",
          "tree": N(u"皇帝", u"清代皇帝勤於批閱奏摺，雍正尤其以大量硃批聞名。", [
              N(u"軍機處", u"雍正年間為西北用兵而設，後成常設中樞。軍機大臣由皇帝挑選，人數不定，「跪受筆錄」，承旨辦事；值房就在乾清門西側。"),
              N(u"內閣", u"名義上的最高行政機構，大學士為正一品；軍機處設立後，主要處理例行公文。"),
              N(u"六部", u"吏、戶、禮、兵、刑、工；各部尚書、侍郎滿漢各一人（滿漢複職）。"),
              N(u"理藩院", u"管理蒙古、西藏、新疆等地事務。"), N(u"都察院", u"監察機關，與刑部、大理寺合稱三法司。"),
              N(u"宗人府", u"管理皇族的名冊、爵位、婚喪與懲處，長官由親王擔任。"), N(u"翰林院", u"文學侍從、修書；進士中的優秀者入翰林院為庶吉士。"),
              N(u"內務府", u"管理皇家事務的龐大機構，下設七司三院，由滿洲包衣人員組成。", [N(u"七司", u"廣儲司（庫藏）、會計司（帳目與莊園）、掌儀司（禮儀與太監）、都虞司（武職與漁獵）、慎刑司（內廷刑案）、營造司（修繕）、慶豐司（牛羊牧群）。"), N(u"三院", u"上駟院（御馬）、武備院（兵器、帳篷）、奉宸苑（園林）。"), N(u"敬事房等", u"敬事房管理太監、宮中事務與時間；另有御膳房、御茶房、造辦處、織造等。")]),
              N(u"欽天監", u"天文、曆法、擇日；清初由傳教士湯若望、南懷仁主持。"), N(u"太醫院", u"宮廷醫療。"), N(u"侍衛處", u"領侍衛內大臣統領皇帝的貼身侍衛。")])},
}
ORG = pgw({"t": "org", "q": u"歷代中央官制組織圖：選一個朝代，點方塊看各機構管什麼", "d": _ORG})


def ORGD(k):
    return pgw({"t": "org", "q": u"官制組織圖（可切換朝代，點方塊看說明）", "d": _ORG, "start": k})


# ---------- 清代品級 ----------
_RANK = [
    {"c": u"仙鶴", "m": u"麒麟", "h": u"紅寶石", "hc": "#c0182a", "s": "180", "ce": u"大學士（正一品）；各部尚書、都察院左都御史（從一品）", "me": u"領侍衛內大臣（正一品）；將軍、提督（從一品）"},
    {"c": u"錦雞", "m": u"獅", "h": u"珊瑚", "hc": "#e2553a", "s": "155", "ce": u"各部侍郎、總督（正二品）；巡撫、布政使（從二品）", "me": u"總兵、副都統（正二品）；副將（從二品）"},
    {"c": u"孔雀", "m": u"豹", "h": u"藍寶石", "hc": "#2546a8", "s": "130", "ce": u"按察使、順天府尹、大理寺卿（正三品）；鹽運使（從三品）", "me": u"參將、一等侍衛（正三品）；游擊（從三品）"},
    {"c": u"雲雁", "m": u"虎", "h": u"青金石", "hc": "#3b5a9a", "s": "105", "ce": u"道員（正四品）；知府、國子監祭酒（從四品）", "me": u"都司、二等侍衛（正四品）"},
    {"c": u"白鷴", "m": u"熊", "h": u"水晶", "hc": "#dfe9f2", "s": "80", "ce": u"六部郎中、同知（正五品）；知州（從五品）", "me": u"守備、三等侍衛（正五品）"},
    {"c": u"鷺鷥", "m": u"彪", "h": u"硨磲", "hc": "#f2efe6", "s": "60", "ce": u"六部主事、通判（正六品）；翰林院修撰（從六品）", "me": u"千總、藍翎侍衛（正六品）"},
    {"c": u"鸂鶒", "m": u"犀牛", "h": u"素金", "hc": "#d8b24a", "s": "45", "ce": u"知縣、翰林院編修（正七品）", "me": u"把總（正七品）"},
    {"c": u"鵪鶉", "m": u"犀牛", "h": u"陰文鏤花金", "hc": "#c9a23b", "s": "40", "ce": u"縣丞、府學教授（正八品）", "me": u"外委千總（正八品）"},
    {"c": u"練雀", "m": u"海馬", "h": u"陽文鏤花金", "hc": "#b8942f", "s": "33.114", "ce": u"主簿（正九品）；巡檢、典史（從九品，部分未入流）", "me": u"外委把總（正九品）"},
]
RANK = pgw({"t": "rank", "q": u"清代品級對照器：選品級與文武，看補子、頂珠、俸祿與代表官職", "r": _RANK})


# ---------- 皇宮人口 ----------
_POP = [
    [u"唐", u"開元、天寶年間宮嬪", 40000, 40000, "c", u"《新唐書．宦者傳》記開元、天寶中「宮嬪大率至四萬」，可能包括各地離宮與宮中各類女性人員，數字是概略的說法。"],
    [u"唐", u"同期「黃衣以上」宦官", 3000, 3000, "r", u"同一段記載說宦官「黃衣以上三千員」，穿朱紫高級官服的還有一千多人。"],
    [u"明", u"康熙轉述的明末宦官", 100000, 100000, "c", u"《清聖祖實錄》記康熙聽前朝老太監說，明朝內監多達十萬。學者多認為有誇大，但規模確實驚人。"],
    [u"明", u"萬曆朝四次選入宦官", 13320, 13320, "r", u"萬曆年間四次選入太監共 13,320 人；天啟朝又選入 7,200 人（據閻崇年等學者整理）。"],
    [u"明", u"中後期宦官總數（估計）", 10000, 70000, "e", u"包括京城二十四衙門、皇陵、南京與各地鎮守太監。學者估計從一萬多到數萬人不等，確切數字難以考證。"],
    [u"明", u"光祿寺廚役", 3400, 9400, "r", u"明初廚役曾超過 9,400 人，後來逐漸裁減，明代後期約 3,400 人（台大歷史學報研究）；他們負責宮中約一萬多名宮女、宦官與辦事人員的飯食。"],
    [u"清", u"宮中太監", 2000, 3000, "e", u"清代鑑於明朝教訓，嚴格限制宦官，學者估計清宮太監約二、三千人。"],
    [u"清", u"內務府全盛時員役", 22000, 22000, "e", u"內務府全盛時期雇用約兩萬兩千名男女人員（包括各司院、造辦處、莊園等），不全在宮內。"],
    [u"清", u"1924 年出宮時太監", 470, 470, "c", u"1924 年溥儀被逐出紫禁城時，據一說宮中還有太監四百七十多人、宮女一百多人；此前 1923 年溥儀已遣散大批太監。"],
]
POP = pgw({"t": "pop", "q": u"皇宮裡有多少人：史料記載、學者估計與可能誇大的數字（選朝代篩選）", "d": _POP, "dyn": [u"唐", u"明", u"清"]})


# ---------- 屋頂 ----------
_ROOFS = [
    [u"重簷廡殿頂", "w2", u"最高等級：兩層屋簷，四面坡、一條正脊與四條垂脊（共五條脊，又稱「五脊殿」）。只用於皇宮最重要的殿堂與重要的寺廟大殿。", u"太和殿、乾清宮、坤寧宮"],
    [u"重簷歇山頂", "x2", u"第二等級：兩層屋簷，上半部是三角形的山花、下半部是四面坡，共九條脊。", u"保和殿、天安門、午門城樓"],
    [u"單簷廡殿頂", "w1", u"一層屋簷的廡殿頂。", u"紫禁城中一些重要的配殿、宮門"],
    [u"單簷歇山頂", "x1", u"一層屋簷的歇山頂，使用很廣。", u"東西六宮的一些宮殿、各地衙署的主要建築"],
    [u"懸山頂", "xs", u"兩面坡，屋頂兩端伸出山牆之外。", u"一般的廂房、民居"],
    [u"硬山頂", "ys", u"兩面坡，屋頂與山牆齊平，等級最低，最為普遍。", u"宮中的值房、庫房與大量民居"],
    [u"攢尖頂", "cj", u"屋頂匯聚到一個尖頂，不在主序列之中，多用於亭子或特殊建築。", u"中和殿、交泰殿、御花園的亭子"],
]
ROOF = pgw({"t": "roof", "q": u"屋頂的等級：點按鈕切換屋頂形式（由高到低）", "roofs": _ROOFS,
            "beasts": [u"龍", u"鳳", u"獅子", u"天馬", u"海馬", u"狻猊", u"押魚", u"獬豸", u"斗牛", u"行什"]}, 620)


def make(icon, note):
    base = make_lesson(icon, note, PGLIB, "pg-w")

    def lesson(*a, **k):
        L = base(*a, **k)
        raws = [b[1] for b in L.body if isinstance(b, tuple) and b[0] == "raw"]
        if any('class="kd-w' in r for r in raws):
            L.body.insert(0, ("raw", u"<script>%s</script>" % KDLIB))
        if any('class="nv-w' in r for r in raws):
            L.body.insert(0, ("raw", u"<script>%s</script>" % NVLIB))
        return L
    return lesson
