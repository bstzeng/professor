# -*- coding: utf-8 -*-
"""〈群論：對稱的數學〉（grp_）共用：課程包裝與 GRPLIB 互動元件（class="grp-w"）。

  dihedral  正多邊形的對稱：旋轉 r、翻轉 s，記錄元素 r^a s^b；凱萊表
  cyclic    循環群：Z_n 的加法軌道與 (Z/nZ)* 的乘法軌道，元素的階、生成元
  perm      置換：雙行記法、箭頭圖、循環分解、奇偶性、階；完美洗牌
  fifteen   十五數字推盤：可玩，打亂、交換 14 與 15，判斷可解性
  wallpaper 壁紙群：選擇群，看同一個圖形被對稱操作鋪滿平面
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

GRP_NOTE = u"本課程從直觀出發，盡量少用形式化的證明；互動元件可以直接操作。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def gw(cfg, maxw=680):
    return wdg("grp-w", cfg, maxw)


GRPLIB = r"""
(function () {
  if (window.__grpLib) return; window.__grpLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function hue(i, n) { return 'hsl(' + Math.round(360 * i / n) + ',60%,55%)'; }
  function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { var t = a % b; a = b; b = t; } return a; }
  function lcm(a, b) { return a / gcd(a, b) * b; }
  function sup(k) { return k === 1 ? '' : '<sup>' + k + '</sup>'; }
  function ename(a, b, n) { a = ((a % n) + n) % n; var s = a === 0 ? (b ? '' : 'e') : 'r' + sup(a); return s + (b ? 's' : ''); }

  function initDihedral(root, cfg) {
    head(root, cfg.q); var P = { n: 5, a: 0, b: 0, pos: [], word: [], tab: 0 }, view = el('div'), inf, tabv = el('div', 'overflow-x:auto');
    function reset() { P.a = 0; P.b = 0; P.word = []; P.pos = []; for (var i = 0; i < P.n; i++) P.pos.push(i); }
    var u = slider(root, '正多邊形的邊數 n', 3, 8, 1, P.n, function (x) { return x + '（二面體群 D' + x + '，共 ' + 2 * x + ' 個元素）'; }, null, function (x) { P.n = x; reset(); draw(); });
    var b = bar(root); [['旋轉 r', 'r'], ['翻轉 s', 's'], ['重設', 'z'], ['顯示／隱藏凱萊表', 't']].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { act(o[1]); }; b.appendChild(x); });
    root.appendChild(view); inf = info(root); root.appendChild(tabv);
    function act(k) { var n = P.n, np = [], i;
      if (k === 'r') { for (i = 0; i < n; i++) np[(i + n - 1) % n] = P.pos[i]; P.pos = np; P.a += 1; P.word.push('r'); }
      else if (k === 's') { for (i = 0; i < n; i++) np[(n - i) % n] = P.pos[i]; P.pos = np; P.a = -P.a; P.b ^= 1; P.word.push('s'); }
      else if (k === 'z') reset(); else P.tab ^= 1; P.a = ((P.a % n) + n) % n; if (P.word.length > 14) P.word = P.word.slice(-14); draw(); }
    function draw() { var n = P.n, W = 640, H = 280, cx = 320, cy = 140, R = 105, g = '', pts = [];
      for (var i = 0; i < n; i++) { var t = Math.PI / 2 - 2 * Math.PI * i / n; pts.push([cx + R * Math.cos(t), cy - R * Math.sin(t)]); }
      g += '<polygon points="' + pts.map(function (p) { return n1(p[0]) + ',' + n1(p[1]); }).join(' ') + '" fill="var(--accent-soft)" stroke="' + BL + '" stroke-width="2"/>';
      g += ln(cx, cy - R - 22, cx, cy + R + 22, GY, 1, 'stroke-dasharray="4 4"') + tx(cx + 6, cy + R + 22, '翻轉 s 的軸', 10, 'var(--text-muted)', 'start');
      g += '<path d="M ' + n1(cx + 40) + ' ' + n1(cy) + ' A 40 40 0 0 0 ' + n1(cx + 40 * Math.cos(2 * Math.PI / n)) + ' ' + n1(cy - 40 * Math.sin(2 * Math.PI / n)) + '" fill="none" stroke="' + OR + '" stroke-width="1.5"/>' + tx(cx + 52, cy - 14, 'r：' + f1(360 / n) + '°', 10, OR, 'start');
      pts.forEach(function (p, i) { var lab = P.pos[i]; g += '<circle cx="' + n1(p[0]) + '" cy="' + n1(p[1]) + '" r="15" fill="' + hue(lab, n) + '"/>' + tx(p[0], p[1] + 5, lab + 1, 13, '#fff'); });
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      inf.innerHTML = '操作紀錄：' + (P.word.length ? P.word.join(' → ') : '（尚無）') + '<br>目前的元素：<b>' + ename(P.a, P.b, n) + '</b>' +
        '（先翻轉 ' + (P.b ? '1' : '0') + ' 次，再旋轉 ' + P.a + ' 次）。<br>不管按幾次，結果一定是 ' + n + ' 種旋轉或 ' + n + ' 種翻轉之一，共 <b>' + 2 * n + '</b> 種——這就是 D<sub>' + n + '</sub>。試試看：先 r 再 s，與先 s 再 r，結果一樣嗎？（不一樣：這個群<b>不交換</b>。）';
      if (!P.tab) { tabv.innerHTML = ''; return; }
      var els = []; for (var a = 0; a < n; a++) els.push([a, 0]); for (a = 0; a < n; a++) els.push([a, 1]);
      function idx(a, b) { return b * n + ((a % n) + n) % n; }
      var h = '<table style="border-collapse:collapse;font-size:0.82em;margin-top:8px"><tr><td style="padding:2px 5px">∘</td>' + els.map(function (e) { return '<td style="padding:2px 5px;font-weight:bold">' + ename(e[0], e[1], n) + '</td>'; }).join('') + '</tr>';
      els.forEach(function (x) { h += '<tr><td style="padding:2px 5px;font-weight:bold">' + ename(x[0], x[1], n) + '</td>'; els.forEach(function (y) { var a = x[0] + (x[1] ? -y[0] : y[0]), b2 = x[1] ^ y[1], k = idx(a, b2);
        h += '<td style="padding:2px 5px;text-align:center;background:' + (b2 ? 'hsla(10,70%,60%,0.25)' : 'hsla(210,70%,60%,0.22)') + '">' + ename(a, b2, n) + '</td>'; }); h += '</tr>'; });
      tabv.innerHTML = h + '</table><p style="font-size:0.85em;color:var(--text-muted);margin:4px 0">凱萊表：第 x 列、第 y 行是 x∘y（先做 y 再做 x）。藍色是旋轉，紅色是翻轉。每一列、每一行都恰好出現每個元素一次。</p>'; }
    u();
  }

  function initCyclic(root, cfg) {
    head(root, cfg.q); var P = { n: 12, g: 5, mul: 0 }, view = el('div'), inf;
    var b = bar(root); [['加法：Z_n', 0], ['乘法：(Z/nZ)*', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.mul = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    var us = [slider(root, 'n（時鐘上的數字個數）', 2, 24, 1, P.n, function (x) { return x; }, null, function (x) { P.n = x; draw(); }),
      slider(root, '元素 g', 1, 23, 1, P.g, function (x) { return x; }, null, function (x) { P.g = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var n = P.n, gg = P.g % n, W = 640, H = 300, cx = 320, cy = 150, R = 115, g = '', orb = [], cur = P.mul ? 1 % n : 0, seen = {};
      if (P.mul && gcd(gg, n) !== 1) { orb = []; } else { while (!seen[cur]) { seen[cur] = 1; orb.push(cur); cur = P.mul ? (cur * gg) % n : (cur + gg) % n; } }
      function pos(k) { var t = Math.PI / 2 - 2 * Math.PI * k / n; return [cx + R * Math.cos(t), cy - R * Math.sin(t)]; }
      g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + R + '" fill="none" stroke="var(--border)"/>';
      for (var i = 0; i + 1 < orb.length; i++) { var p = pos(orb[i]), q = pos(orb[i + 1]); g += ln(p[0], p[1], q[0], q[1], OR, 1.6); }
      if (orb.length > 1) { var p2 = pos(orb[orb.length - 1]), q2 = pos(orb[0]); g += ln(p2[0], p2[1], q2[0], q2[1], OR, 1.6, 'stroke-dasharray="4 3"'); }
      for (var k = 0; k < n; k++) { var pp = pos(k), on = seen[k], unit = gcd(k, n) === 1; g += '<circle cx="' + n1(pp[0]) + '" cy="' + n1(pp[1]) + '" r="12" fill="' + (on ? OR : (P.mul && !unit ? 'var(--surface)' : 'var(--accent-soft)')) + '" stroke="' + (P.mul && !unit ? GY : BL) + '"' + (P.mul && !unit ? ' stroke-dasharray="2 2"' : '') + '/>' + tx(pp[0], pp[1] + 4, k, 11, on ? '#fff' : 'currentColor'); }
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var phi = 0; for (k = 1; k <= n; k++) if (gcd(k, n) === 1) phi++;
      if (!P.mul) { var ord = n / gcd(gg, n); inf.innerHTML = '從 0 出發，每次加 ' + gg + '（模 ' + n + '）：' + orb.join(' → ') + ' → 0。<br>g = ' + gg + ' 的<b>階</b>是 ' + ord + ' = ' + n + ' ÷ gcd(' + n + ', ' + gg + ')。' +
        (ord === n ? '它走遍了所有的數字：g 是 Z<sub>' + n + '</sub> 的<b>生成元</b>。' : '它只走到一部分：這些數字形成一個大小為 ' + ord + ' 的<b>子群</b>，而 ' + ord + ' 整除 ' + n + '（拉格朗日定理）。') + '<br>Z<sub>' + n + '</sub> 共有 φ(' + n + ') = ' + phi + ' 個生成元：與 ' + n + ' 互質的數。'; }
      else if (!orb.length) inf.innerHTML = 'g = ' + gg + ' 與 ' + n + ' 不互質，在乘法下沒有反元素，不屬於 (Z/' + n + 'Z)*（虛線圈的數字）。請換一個與 ' + n + ' 互質的 g。';
      else { var o2 = orb.length; inf.innerHTML = '從 1 出發，每次乘以 ' + gg + '（模 ' + n + '）：' + orb.join(' → ') + ' → 1。<br>(Z/' + n + 'Z)* 有 φ(' + n + ') = ' + phi + ' 個元素（實線圈）。g 的階是 ' + o2 + '，整除 ' + phi + '。' +
        (o2 === phi ? '<br>g 走遍了所有的單位元：' + gg + ' 是模 ' + n + ' 的<b>原根</b>，這個群是循環群。' : '<br>g 不是原根。（只有 n = 1、2、4、p<sup>k</sup>、2p<sup>k</sup> 時才有原根。）') + '<br>這正是費馬小定理與 RSA 的基礎：g<sup>φ(n)</sup> ≡ 1。'; } }
    us.forEach(function (x) { x(); });
  }

  function cycles(p) { var n = p.length, seen = [], cs = []; for (var i = 0; i < n; i++) { if (seen[i]) continue; var c = [], j = i; while (!seen[j]) { seen[j] = 1; c.push(j); j = p[j]; } cs.push(c); } return cs; }
  function initPerm(root, cfg) {
    head(root, cfg.q); var P = { n: 7, p: [3, 0, 4, 1, 2, 6, 5] }, view = el('div'), inf;
    var u = slider(root, '元素個數 n', 3, 12, 1, P.n, function (x) { return x; }, null, function (x) { if (x !== P.n) { P.n = x; rnd(); } draw(); });
    var b = bar(root); [['隨機置換', 'r'], ['自己乘自己（σ²）', 'q'], ['完美洗牌（外洗）', 'f'], ['恆等置換', 'e']].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { act(o[1]); }; b.appendChild(x); });
    root.appendChild(view); inf = info(root);
    function rnd() { var a = []; for (var i = 0; i < P.n; i++) a.push(i); for (i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } P.p = a; }
    function act(k) { var n = P.n, i; if (k === 'r') rnd(); else if (k === 'q') P.p = P.p.map(function (x) { return P.p[x]; });
      else if (k === 'e') { P.p = []; for (i = 0; i < n; i++) P.p.push(i); }
      else { var m = Math.ceil(n / 2), q = []; for (i = 0; i < n; i++) q[i] = i < m ? 2 * i : 2 * (i - m) + 1; P.p = q; } draw(); }
    function draw() { var n = P.n, W = 640, H = 170, g = '', dx = 560 / Math.max(1, n - 1), cs = cycles(P.p);
      var cyc = cs.filter(function (c) { return c.length > 1; }), col = []; cs.forEach(function (c, i) { c.forEach(function (x) { col[x] = c.length > 1 ? hue(i, cs.length) : GY; }); });
      for (var i = 0; i < n; i++) { var x0 = 40 + i * dx, x1 = 40 + P.p[i] * dx; g += ln(x0, 40, x1, 128, col[i], 2, 'marker-end=""') + '<circle cx="' + n1(x0) + '" cy="30" r="13" fill="' + col[i] + '"/>' + tx(x0, 35, i + 1, 12, '#fff') +
        '<circle cx="' + n1(40 + i * dx) + '" cy="140" r="13" fill="var(--surface)" stroke="' + GY + '"/>' + tx(40 + i * dx, 145, i + 1, 12); }
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var two = '<table style="border-collapse:collapse;font-size:0.9em"><tr>' + P.p.map(function (x, i) { return '<td style="padding:1px 6px;text-align:center">' + (i + 1) + '</td>'; }).join('') + '</tr><tr>' + P.p.map(function (x) { return '<td style="padding:1px 6px;text-align:center;border-top:1px solid var(--border)">' + (x + 1) + '</td>'; }).join('') + '</tr></table>';
      var ord = cs.reduce(function (a, c) { return lcm(a, c.length); }, 1), sgn = (n - cs.length) % 2 === 0;
      inf.innerHTML = '雙行記法（上面的 i 被送到下面的 σ(i)）：' + two +
        '循環分解：<b>' + (cyc.length ? cyc.map(function (c) { return '(' + c.map(function (x) { return x + 1; }).join(' ') + ')'; }).join('') : 'e（恆等）') + '</b>' + (cs.length > cyc.length ? '，其餘 ' + (cs.length - cyc.length) + ' 個不動點' : '') +
        '<br>循環型：' + cs.map(function (c) { return c.length; }).sort(function (a, b) { return b - a; }).join('+') + ' = ' + n + '。<b>階</b> = 各循環長度的最小公倍數 = <b>' + ord + '</b>（重複做 ' + ord + ' 次會回到原狀）。' +
        '<br><b>' + (sgn ? '偶' : '奇') + '置換</b>：可以寫成 ' + (n - cs.length) + ' 個對換的乘積（n − 循環個數）。偶置換形成交錯群 A<sub>' + n + '</sub>，佔了 S<sub>' + n + '</sub> 的一半。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">「完美洗牌」把前半疊與後半疊一張一張交錯。52 張牌做 8 次外洗會回到原來的順序。</span>'; }
    u();
  }

  function initFifteen(root, cfg) {
    head(root, cfg.q); var S = [], view = el('div', 'display:flex;justify-content:center'), inf, moves = 0;
    var b = bar(root); [['重設', 'z'], ['合法地打亂', 'm'], ['交換 14 和 15（洛伊德的謎題）', 'x']].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { act(o[1]); }; b.appendChild(x); });
    root.appendChild(view); inf = info(root);
    function reset() { S = []; for (var i = 1; i < 16; i++) S.push(i); S.push(0); moves = 0; }
    function nb(i) { var r = Math.floor(i / 4), c = i % 4, a = []; if (r > 0) a.push(i - 4); if (r < 3) a.push(i + 4); if (c > 0) a.push(i - 1); if (c < 3) a.push(i + 1); return a; }
    function act(k) { if (k === 'z') reset(); else if (k === 'm') { for (var t = 0; t < 300; t++) { var z = S.indexOf(0), a = nb(z), j = a[Math.floor(Math.random() * a.length)]; S[z] = S[j]; S[j] = 0; } moves = 0; }
      else { var p = S.indexOf(14), q = S.indexOf(15); S[p] = 15; S[q] = 14; } draw(); }
    function click(i) { var z = S.indexOf(0); if (nb(z).indexOf(i) >= 0) { S[z] = S[i]; S[i] = 0; moves++; draw(); } }
    function draw() { var g = el('div', 'display:grid;grid-template-columns:repeat(4,56px);gap:5px;padding:8px;border-radius:10px;background:var(--accent-soft)');
      S.forEach(function (v, i) { var c = el('div', 'height:56px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:1.25em;font-weight:bold;' + (v ? 'cursor:pointer;background:' + (v === i + 1 ? BL : OR) + ';color:#fff' : 'background:transparent'), v || ''); if (v) c.onclick = function () { click(i); }; g.appendChild(c); });
      view.innerHTML = ''; view.appendChild(g);
      var inv = 0, a = S.filter(function (x) { return x; }); for (var i = 0; i < a.length; i++) for (var j = i + 1; j < a.length; j++) if (a[i] > a[j]) inv++;
      var rb = 4 - Math.floor(S.indexOf(0) / 4), ok = (inv + rb) % 2 === 1, done = S.every(function (v, i) { return i === 15 ? v === 0 : v === i + 1; });
      inf.innerHTML = (done ? '<b>完成！</b>' : '點空格旁的方塊來移動（已移動 ' + moves + ' 步）。') + '<br>逆序數（較大的數排在較小的數前面的對數）= ' + inv + '；空格在從下數第 ' + rb + ' 列。' +
        '<br>每一步滑動，都讓「逆序數 + 空格的列數」的奇偶性保持不變。目前的和是 ' + (inv + rb) + '，' + (ok ? '<b>奇數：可以解</b>。' : '<b>偶數：不可能解</b>——無論怎麼滑都不行。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">原因：每一步都是一個對換，而合法的狀態只佔所有排列的一半（16!/2 種）。1880 年代，洛伊德聲稱懸賞解開「14 和 15 對調」的版本——它是不可能的。</span>'; }
    reset(); draw();
  }

  var WG = {
    p1: { h: 0, t: [[1, 0, 0, 1, 0, 0]], d: '只有平移。沒有旋轉、沒有鏡射。' },
    p2: { h: 0, t: [[1, 0, 0, 1, 0, 0], [-1, 0, 0, -1, 0, 0]], d: '平移加上 180° 旋轉（二重旋轉中心）。' },
    pm: { h: 0, t: [[1, 0, 0, 1, 0, 0], [-1, 0, 0, 1, 0, 0]], d: '平移加上互相平行的鏡射線。' },
    pg: { h: 0, t: [[1, 0, 0, 1, 0, 0], [-1, 0, 0, 1, 0, 0.5]], d: '平移加上<b>滑移反射</b>（鏡射後再沿鏡射線平移半格），像左右交替的腳印。' },
    cm: { h: 0, t: [[1, 0, 0, 1, 0, 0], [-1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0.5, 0.5], [-1, 0, 0, 1, 0.5, 0.5]], d: '鏡射加上滑移反射，鏡射線之間夾著滑移線（像磚牆的人字紋）。' },
    pmm: { h: 0, t: [[1, 0, 0, 1, 0, 0], [-1, 0, 0, 1, 0, 0], [1, 0, 0, -1, 0, 0], [-1, 0, 0, -1, 0, 0]], d: '兩組互相垂直的鏡射線，交點是二重旋轉中心。' },
    p4: { h: 0, t: [[1, 0, 0, 1, 0, 0], [0, -1, 1, 0, 0, 0], [-1, 0, 0, -1, 0, 0], [0, 1, -1, 0, 0, 0]], d: '90° 旋轉（四重旋轉中心），沒有鏡射。' },
    p4m: { h: 0, t: [[1, 0, 0, 1, 0, 0], [0, -1, 1, 0, 0, 0], [-1, 0, 0, -1, 0, 0], [0, 1, -1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [-1, 0, 0, 1, 0, 0], [0, -1, -1, 0, 0, 0], [1, 0, 0, -1, 0, 0]], d: '四重旋轉加上鏡射，包括對角線方向的鏡射（像棋盤格的地磚）。' },
    p3: { h: 1, r: 3, m: 0, d: '120° 旋轉（三重旋轉中心），六角形的晶格，沒有鏡射。' },
    p6: { h: 1, r: 6, m: 0, d: '60° 旋轉（六重旋轉中心），沒有鏡射。' },
    p6m: { h: 1, r: 6, m: 1, d: '六重旋轉加上六個方向的鏡射——對稱性最高的壁紙群，像雪花。' } };
  var MOT = [[0.12, 0.03], [0.4, 0.03], [0.4, 0.18], [0.35, 0.18], [0.35, 0.08], [0.3, 0.08], [0.3, 0.14], [0.25, 0.14], [0.25, 0.08], [0.12, 0.08]];
  function initWall(root, cfg) {
    head(root, cfg.q); var P = { k: 'p4m' }, view = el('div'), inf;
    var b = bar(root); Object.keys(WG).forEach(function (k) { var x = btn(k, k); x.onclick = function () { P.k = k; mark(b, k); draw(); }; b.appendChild(x); }); mark(b, P.k);
    root.appendChild(view); inf = info(root);
    function draw() { var G = WG[P.k], W = 640, H = 340, S = 62, g = '', T = G.t;
      if (G.h) { T = []; for (var i = 0; i < G.r; i++) { var a = 2 * Math.PI * i / G.r, c = Math.cos(a), s = Math.sin(a); T.push([c, -s, s, c, 0, 0]); if (G.m) T.push([c, s, s, -c, 0, 0]); } }
      var v1 = [1, 0], v2 = G.h ? [0.5, Math.sqrt(3) / 2] : [0, 1];
      for (var I = -7; I <= 7; I++) for (var J = -4; J <= 4; J++) { var ox = I * v1[0] + J * v2[0], oy = I * v1[1] + J * v2[1], X0 = W / 2 + ox * S, Y0 = H / 2 - oy * S; if (X0 < -60 || X0 > W + 60 || Y0 < -60 || Y0 > H + 60) continue;
        T.forEach(function (m) { var det = m[0] * m[3] - m[1] * m[2];
          var d = MOT.map(function (p, k) { var x = m[0] * p[0] + m[1] * p[1] + m[4] + ox, y = m[2] * p[0] + m[3] * p[1] + m[5] + oy; return (k ? 'L' : 'M') + n1(W / 2 + x * S) + ' ' + n1(H / 2 - y * S); }).join(' ') + 'Z';
          g += '<path d="' + d + '" fill="' + (det > 0 ? BL : RD) + '" fill-opacity="0.85"/>'; }); }
      g += '<path d="M' + n1(W / 2) + ' ' + n1(H / 2) + ' l' + n1(v1[0] * S) + ' ' + n1(-v1[1] * S) + ' l' + n1(v2[0] * S) + ' ' + n1(-v2[1] * S) + ' l' + n1(-v1[0] * S) + ' ' + n1(v1[1] * S) + 'Z" fill="none" stroke="' + OR + '" stroke-width="1.5" stroke-dasharray="4 3"/>';
      view.innerHTML = '<div style="border-radius:8px;overflow:hidden;border:1px solid var(--border)">' + svgw('0 0 ' + W + ' ' + H, g) + '</div>';
      inf.innerHTML = '<b>' + P.k + '</b>：' + G.d + '<br>同一個不對稱的小圖形，被這個群的所有對稱操作鋪滿平面。<span style="color:' + BL + '">藍色</span>是原本的方向，<span style="color:' + RD + '">紅色</span>是被鏡射（左右顛倒）過的。橘色虛線是一個晶格單位。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">平面上的週期圖案只有 <b>17 種</b>對稱群（這裡展示其中 11 種）；只允許 2、3、4、6 重旋轉——五重旋轉不能鋪滿平面（晶體限制定理）。</span>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.grp-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ dihedral: initDihedral, cyclic: initCyclic, perm: initPerm, fifteen: initFifteen, wallpaper: initWall })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🔷", GRP_NOTE, GRPLIB, "grp-w")

DIHEDRAL = gw({"t": "dihedral", "q": u"正多邊形的對稱：按「旋轉」和「翻轉」，看頂點怎麼移動"})
CYCLIC = gw({"t": "cyclic", "q": u"時鐘上的群：一直加（或乘）同一個數，會走到哪裡"})
PERM = gw({"t": "perm", "q": u"置換：把 n 個東西重新排列"})
FIFTEEN = gw({"t": "fifteen", "q": u"十五數字推盤：哪些排列解得開"})
WALLPAPER = gw({"t": "wallpaper", "q": u"壁紙群：同一個圖形，不同的對稱"})
