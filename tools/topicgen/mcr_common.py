# -*- coding: utf-8 -*-
"""〈Minecraft 紅石電路：用遊戲學計算機〉（mcr_）共用：課程包裝與 MCRLIB 互動元件（class="mcr-w"）。

  signal  紅石粉的訊號強度：每格減 1，中繼器補回 15 並延遲 1 刻
  gate    邏輯閘：NOT、OR、AND、NAND、NOR、XOR，切換拉桿看輸出與真值表
  adder   四位元漣波進位加法器：切換 A、B 的每一個位元，看進位如何傳遞
  latch   閂鎖與正反器：RS 閂鎖、D 正反器、T 正反器，記錄波形
  cpu     迷你 CPU：程式計數器、暫存器、指令，單步或連續執行
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

MCR_NOTE = u"本課程以 Minecraft Java 版的紅石機制為主（基岩版有些許不同）；互動元件是簡化的模擬。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def mw(cfg, maxw=680):
    return wdg("mcr-w", cfg, maxw)


MCRLIB = r"""
(function () {
  if (window.__mcrLib) return; window.__mcrLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5', RS = '#e0302a';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function red(s) { return s > 0 ? 'hsl(2,' + (55 + s * 3) + '%,' + (22 + s * 2.4) + '%)' : '#5a2a28'; }
  function lever(x, y, on, lab) { return '<rect x="' + (x - 14) + '" y="' + (y - 10) + '" width="28" height="20" rx="3" fill="#8a8a8a"/>' + ln(x, y, x + (on ? 9 : -9), y - 16, '#6b4a2b', 4, 'stroke-linecap="round"') + '<circle cx="' + (x + (on ? 9 : -9)) + '" cy="' + (y - 16) + '" r="3.5" fill="' + (on ? RS : '#5a2a28') + '"/>' + (lab ? tx(x, y + 26, lab, 11) : ''); }
  function lamp(x, y, on) { return '<rect x="' + (x - 16) + '" y="' + (y - 16) + '" width="32" height="32" rx="4" fill="' + (on ? '#ffd76a' : '#6b5a3a') + '" stroke="#3a2e1e" stroke-width="2"/>' + (on ? '<rect x="' + (x - 22) + '" y="' + (y - 22) + '" width="44" height="44" rx="8" fill="none" stroke="#ffd76a" stroke-width="2" opacity="0.6"/>' : ''); }

  function initSignal(root, cfg) {
    head(root, cfg.q); var P = { n: 20, k: 0, on: 1 }, view = el('div'), inf;
    var us = [slider(root, '紅石粉的長度（格）', 1, 40, 1, P.n, function (x) { return x + ' 格'; }, null, function (x) { P.n = x; draw(); }),
      slider(root, '每隔幾格放一個中繼器（0 = 不放）', 0, 16, 1, P.k, function (x) { return x ? '每 ' + x + ' 格' : '不放'; }, null, function (x) { P.k = x; draw(); })];
    var b = bar(root), lb = btn('拉桿：開'); lb.onclick = function () { P.on ^= 1; lb.textContent = '拉桿：' + (P.on ? '開' : '關'); draw(); }; b.appendChild(lb);
    root.appendChild(view); inf = info(root);
    function draw() { var cells = [], s = P.on ? 15 : 0, rep = 0;
      for (var i = 0; i < P.n; i++) { if (P.k && i > 0 && i % P.k === 0) { cells.push({ r: 1, s: s > 0 ? 15 : 0 }); rep++; s = s > 0 ? 15 : 0; } cells.push({ r: 0, s: s }); s = Math.max(0, s - 1); }
      var per = 20, rows = Math.ceil((cells.length + 2) / per), g = '', W = 640, cw = 29;
      function pos(k) { var r = Math.floor(k / per), c = k % per; return [18 + c * cw + 4, 14 + r * 46]; }
      var p0 = pos(0); g += lever(p0[0] + 10, p0[1] + 24, P.on, '');
      cells.forEach(function (c, i) { var p = pos(i + 1); if (c.r) g += '<rect x="' + p[0] + '" y="' + (p[1] + 6) + '" width="' + (cw - 3) + '" height="' + (cw - 3) + '" rx="3" fill="#9a9a9a"/>' + '<path d="M' + (p[0] + 6) + ' ' + (p[1] + 19) + ' h14 l-4 -4 m4 4 l-4 4" fill="none" stroke="' + (c.s ? RS : '#5a2a28') + '" stroke-width="2"/>' + tx(p[0] + 13, p[1] + 44, '中繼', 8.5, 'var(--text-muted)');
        else g += '<rect x="' + p[0] + '" y="' + (p[1] + 6) + '" width="' + (cw - 3) + '" height="' + (cw - 3) + '" rx="3" fill="' + red(c.s) + '"/>' + tx(p[0] + 13, p[1] + 24, c.s, 10, c.s > 6 ? '#fff' : '#d99'); });
      var last = cells[cells.length - 1].s, pl = pos(cells.length + 1); g += lamp(pl[0] + 13, pl[1] + 19, last > 0);
      view.innerHTML = svgw('0 0 ' + W + ' ' + (rows * 46 + 14), g);
      inf.innerHTML = '紅石粉從拉桿旁邊的強度 <b>15</b> 開始，每經過一格就<b>減 1</b>。' + (last > 0 ? '末端的強度是 <b>' + last + '</b>，紅石燈亮著。' : (P.on ? '訊號在第 16 格就變成 0 了——<b>燈不會亮</b>。' : '拉桿關著，沒有訊號。')) +
        (rep ? '<br>放了 ' + rep + ' 個<b>中繼器</b>：每個中繼器把訊號補回 15，但會增加至少 1 個紅石刻（0.1 秒）的延遲，總延遲至少 ' + f1(rep * 0.1) + ' 秒。' : '<br>試試看：把長度拉到 20 格以上，再每 15 格放一個中繼器。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">真實的電路也一樣：訊號在導線中會衰減，長距離傳輸需要「放大器」重新整形——但每經過一級，就多一點延遲。</span>'; }
    us.forEach(function (u) { u(); });
  }

  var GT = { NOT: { n: 1, f: function (a) { return !a; }, d: '一支紅石火把插在方塊上：方塊被充能時，火把熄滅；沒有充能時，火把亮著。輸出永遠和輸入<b>相反</b>。' },
    OR: { n: 2, f: function (a, b) { return a || b; }, d: '把兩條紅石粉<b>接在一起</b>就是 OR：任何一條有訊號，輸出就有訊號。最簡單的閘。' },
    AND: { n: 2, f: function (a, b) { return a && b; }, d: '兩個輸入各接一支火把（反相），兩支火把的輸出接在一起（OR），再接一支火把（反相）：NOT(NOT A OR NOT B) = A AND B。這是笛摩根定律。' },
    NAND: { n: 2, f: function (a, b) { return !(a && b); }, d: 'AND 少掉最後一支火把：NOT A OR NOT B。只要有一個輸入是 0，輸出就是 1。所有的邏輯都可以只用 NAND 組出來。' },
    NOR: { n: 2, f: function (a, b) { return !(a || b); }, d: '兩條訊號接在一起，再接一支火把：兩個都是 0 時才輸出 1。阿波羅導航電腦幾乎只用 NOR 閘做成。' },
    XOR: { n: 2, f: function (a, b) { return a !== b; }, d: '「互斥或」：兩個輸入<b>不同</b>時才輸出 1。紅石中有好幾種做法，常見的是用 AND、OR、NOT 組合，或用比較器。加法器的核心。' } };
  function initGate(root, cfg) {
    head(root, cfg.q); var P = { g: cfg.g || 'AND', a: 0, b: 0 }, view = el('div'), inf;
    var b0 = bar(root); Object.keys(GT).forEach(function (k) { var x = btn(k, k); x.onclick = function () { P.g = k; mark(b0, k); draw(); }; b0.appendChild(x); }); mark(b0, P.g);
    var b1 = bar(root), xa = btn('切換 A'), xb = btn('切換 B'); xa.onclick = function () { P.a ^= 1; draw(); }; xb.onclick = function () { P.b ^= 1; draw(); }; b1.appendChild(xa); b1.appendChild(xb);
    root.appendChild(view); inf = info(root);
    function draw() { var G = GT[P.g], two = G.n === 2, out = G.f(!!P.a, !!P.b), g = '';
      g += lever(70, 60, P.a, 'A') + ln(90, 52, 250, two ? 85 : 100, P.a ? RS : '#5a2a28', 5);
      if (two) g += lever(70, 150, P.b, 'B') + ln(90, 142, 250, 115, P.b ? RS : '#5a2a28', 5); else xb.style.display = 'none';
      if (two) xb.style.display = '';
      g += '<rect x="250" y="60" width="140" height="80" rx="10" fill="var(--accent-soft)" stroke="' + BL + '" stroke-width="2"/>' + tx(320, 108, P.g, 22, BL);
      g += ln(390, 100, 520, 100, out ? RS : '#5a2a28', 5) + lamp(545, 100, out);
      view.innerHTML = svgw('0 0 640 190', g);
      var rows = two ? [[0, 0], [0, 1], [1, 0], [1, 1]] : [[0], [1]], t = '<table style="border-collapse:collapse;margin:6px 0">' + '<tr>' + (two ? '<th style="padding:2px 10px">A</th><th style="padding:2px 10px">B</th>' : '<th style="padding:2px 10px">A</th>') + '<th style="padding:2px 10px">輸出</th></tr>';
      rows.forEach(function (r) { var cur = r[0] === P.a && (!two || r[1] === P.b); t += '<tr style="background:' + (cur ? 'rgba(224,48,42,0.18)' : 'transparent') + '">' + r.map(function (v) { return '<td style="padding:2px 10px;text-align:center">' + v + '</td>'; }).join('') + '<td style="padding:2px 10px;text-align:center;font-weight:bold">' + (G.f(!!r[0], !!r[1]) ? 1 : 0) + '</td></tr>'; });
      inf.innerHTML = '<b>' + P.g + '</b>：' + G.d + '<br>真值表（目前的狀態標成紅色）：' + t + '</table>'; }
    draw();
  }

  function initAdder(root, cfg) {
    head(root, cfg.q); var P = { a: [1, 0, 1, 1], b: [0, 1, 1, 0] }, view = el('div'), inf;
    root.appendChild(view); inf = info(root);
    function draw() { var g = '', c = 0, s = [], cs = [0], W = 640;
      for (var i = 3; i >= 0; i--) { var a = P.a[i], b = P.b[i], sum = a ^ b ^ c, co = (a & b) | (c & (a ^ b)); s[i] = sum; c = co; cs.push(co); }
      for (i = 0; i < 4; i++) { var x = 40 + i * 145, bit = 3 - i;
        g += '<g data-k="a' + i + '" style="cursor:pointer">' + '<rect x="' + (x + 10) + '" y="10" width="44" height="30" rx="5" fill="' + (P.a[i] ? RS : '#5a2a28') + '"/>' + tx(x + 32, 30, 'A' + bit + '=' + P.a[i], 11, '#fff') + '</g>';
        g += '<g data-k="b' + i + '" style="cursor:pointer">' + '<rect x="' + (x + 64) + '" y="10" width="44" height="30" rx="5" fill="' + (P.b[i] ? RS : '#5a2a28') + '"/>' + tx(x + 86, 30, 'B' + bit + '=' + P.b[i], 11, '#fff') + '</g>';
        g += '<rect x="' + (x + 8) + '" y="70" width="104" height="56" rx="8" fill="var(--accent-soft)" stroke="' + BL + '" stroke-width="2"/>' + tx(x + 60, 102, '全加器', 12, BL);
        g += ln(x + 32, 40, x + 32, 70, P.a[i] ? RS : '#5a2a28', 3) + ln(x + 86, 40, x + 86, 70, P.b[i] ? RS : '#5a2a28', 3);
        g += ln(x + 60, 126, x + 60, 160, s[i] ? RS : '#5a2a28', 3) + lamp(x + 60, 178, s[i]) + tx(x + 60, 212, 'S' + bit, 11);
        var cin = cs[4 - i - 1 + 0]; }
      for (i = 0; i < 4; i++) { var xx = 40 + i * 145, carryIn = cs[3 - i]; if (i < 3) g += ln(xx + 153, 98, xx + 112, 98, carryIn ? RS : '#5a2a28', 3, 'marker-end=""') + tx(xx + 132, 92, 'C', 9, carryIn ? RS : 'var(--text-muted)'); }
      var cout = cs[4]; g += ln(48, 98, 20, 98, cout ? RS : '#5a2a28', 3) + tx(16, 92, '進位', 9, cout ? RS : 'var(--text-muted)', 'end');
      view.innerHTML = svgw('0 0 ' + W + ' 225', g);
      view.querySelectorAll('g[data-k]').forEach(function (e) { e.addEventListener('click', function () { var k = e.getAttribute('data-k'), j = +k[1]; P[k[0]][j] ^= 1; draw(); }); });
      var av = parseInt(P.a.join(''), 2), bv = parseInt(P.b.join(''), 2), sv = parseInt(s.join(''), 2) + cout * 16, chain = 0, cur = 0;
      for (i = 1; i <= 4; i++) { if (cs[i]) { cur++; chain = Math.max(chain, cur); } else cur = 0; }
      inf.innerHTML = '點上方的方塊切換位元。<b>' + P.a.join('') + '</b>（' + av + '）＋ <b>' + P.b.join('') + '</b>（' + bv + '）＝ <b>' + (cout ? '1' : '') + s.join('') + '</b>（' + sv + '）' + (cout ? '——超過 4 位元，最左邊的<b>進位</b>亮了（溢位）。' : '。') +
        '<br>每個全加器把 A、B 與右邊傳來的進位相加，輸出這一位的和 S，並把進位傳給左邊。進位像骨牌一樣<b>從右往左</b>傳遞：最壞的情況（例如 1111 + 0001），要等進位依序經過每一個全加器——這叫<b>漣波進位</b>。' +
        '<br>在紅石中，每個全加器需要好幾個紅石刻，所以位元越多，加法越慢。真實的 CPU 用「進位預看」電路，同時算出所有的進位。'; }
    draw();
  }

  function initLatch(root, cfg) {
    head(root, cfg.q); var P = { m: 0, q: 0, d: 0, h: [] }, view = el('div'), inf;
    var b0 = bar(root); [['RS 閂鎖', 0], ['D 正反器', 1], ['T 正反器', 2]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.m = o[1]; P.q = 0; P.d = 0; P.h = []; mark(b0, o[1]); sh(); }; b0.appendChild(x); }); mark(b0, 0);
    var b1 = bar(root); root.appendChild(view); inf = info(root);
    function push(row) { P.h.push(row); if (P.h.length > 16) P.h.shift(); draw(); }
    function sh() { b1.innerHTML = ''; var bs = P.m === 0 ? [['設定 S（按一下）', 's'], ['重設 R（按一下）', 'r'], ['什麼都不做', 'n']] : P.m === 1 ? [['切換 D', 'd'], ['時脈脈衝 ↑', 'c']] : [['時脈脈衝 ↑', 'c']];
      bs.forEach(function (o) { var x = btn(o[0]); x.onclick = function () { act(o[1]); }; b1.appendChild(x); }); push(snap('')); }
    function snap(e) { return { s: e === 's' ? 1 : 0, r: e === 'r' ? 1 : 0, c: e === 'c' ? 1 : 0, d: P.d, q: P.q }; }
    function act(k) { if (P.m === 0) { if (k === 's') P.q = 1; if (k === 'r') P.q = 0; push(snap(k)); }
      else if (P.m === 1) { if (k === 'd') { P.d ^= 1; push(snap('')); } else { P.q = P.d; push(snap('c')); } }
      else { P.q ^= 1; push(snap('c')); } }
    function draw() { var rows = P.m === 0 ? [['S', 's'], ['R', 'r'], ['Q', 'q']] : P.m === 1 ? [['D', 'd'], ['CLK', 'c'], ['Q', 'q']] : [['CLK', 'c'], ['Q', 'q']], g = '', W = 640, cw = 34;
      rows.forEach(function (r, j) { var y = 20 + j * 50, d = ''; g += tx(30, y + 18, r[0], 12, 'currentColor', 'end');
        P.h.forEach(function (h, i) { var v = h[r[1]], x = 45 + i * cw, yy = y + (v ? 4 : 28); d += (i ? 'L' : 'M') + x + ' ' + yy + ' L' + (x + cw) + ' ' + yy; });
        g += '<path d="' + d + '" fill="none" stroke="' + (r[1] === 'q' ? RS : BL) + '" stroke-width="2.4"/>'; });
      g += lamp(W - 40, 40, P.q) + tx(W - 40, 80, 'Q = ' + P.q, 12);
      view.innerHTML = svgw('0 0 ' + W + ' ' + (rows.length * 50 + 20), g);
      inf.innerHTML = (P.m === 0 ? '<b>RS 閂鎖</b>：按一下 S，Q 變成 1，<b>放開之後仍然保持</b>；按一下 R，Q 變成 0。這就是最基本的<b>記憶</b>：電路「記住」了最後一次被設定的值。紅石中，最簡單的 RS 閂鎖是兩支互相連接的火把（兩個 NOR 閘），或者一個黏性活塞推動紅石方塊。' :
        P.m === 1 ? '<b>D 正反器</b>：D 可以隨時改變，但 Q 只有在<b>時脈脈衝</b>來的那一刻，才會變成 D 的值。它讓整個電路在同一個節拍下更新——這是暫存器與記憶體的基本單位。紅石中常用中繼器的「鎖定」功能做成。' :
        '<b>T 正反器</b>：每來一個時脈脈衝，Q 就<b>翻轉</b>一次。兩個脈衝，Q 才回到原狀——它把頻率除以 2。把幾個 T 正反器串起來，就是一個二進位<b>計數器</b>。紅石中常用黏性活塞或投擲器與比較器做成。') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">波形圖：每一格是一次操作，紅線是輸出 Q。</span>'; }
    sh();
  }

  var PROGS = { fib: { n: '費波那契數列', c: [['LDI', 'A', 0], ['LDI', 'B', 1], ['OUT', 'A'], ['ADD'], ['SWP'], ['JNC', 2], ['HLT']] },
    cnt: { n: '倒數計時', c: [['LDI', 'A', 5], ['OUT', 'A'], ['DEC'], ['JNZ', 1], ['OUT', 'A'], ['HLT']] } };
  var DESC = { LDI: function (i) { return '把數字 ' + i[2] + ' 載入暫存器 ' + i[1]; }, OUT: function () { return '把暫存器 A 的值送到輸出（亮起一排紅石燈）'; }, ADD: function () { return 'A ← A + B（超過 255 時設定進位旗標 C）'; },
    SWP: function () { return '交換 A 與 B'; }, DEC: function () { return 'A ← A − 1（結果為 0 時設定零旗標 Z）'; }, JNC: function (i) { return '如果沒有進位，跳到位址 ' + i[1]; }, JNZ: function (i) { return '如果 A 不是 0，跳到位址 ' + i[1]; }, HLT: function () { return '停止'; } };
  function initCPU(root, cfg) {
    head(root, cfg.q); var P = { p: 'fib' }, S, view = el('div'), inf, timer = null;
    var b0 = bar(root); Object.keys(PROGS).forEach(function (k) { var x = btn('程式：' + PROGS[k].n, k); x.onclick = function () { P.p = k; mark(b0, k); reset(); }; b0.appendChild(x); }); mark(b0, 'fib');
    var b1 = bar(root); [['單步執行', 'step'], ['連續執行', 'run'], ['重設', 'reset']].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { if (o[1] === 'step') { stop(); step(); } else if (o[1] === 'run') run(); else reset(); }; b1.appendChild(x); });
    root.appendChild(view); inf = info(root);
    function reset() { stop(); S = { A: 0, B: 0, pc: 0, C: 0, Z: 0, out: [], halt: 0, last: '按「單步執行」開始。', n: 0 }; draw(); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    function run() { stop(); timer = setInterval(function () { if (S.halt || !root.isConnected) { stop(); return; } step(); }, 350); }
    function step() { if (S.halt) return; var prog = PROGS[P.p].c, ins = prog[S.pc], at = S.pc, op = ins[0], next = S.pc + 1;
      if (op === 'LDI') S[ins[1]] = ins[2]; else if (op === 'OUT') S.out.push(S.A); else if (op === 'ADD') { var t = S.A + S.B; S.C = t > 255 ? 1 : 0; S.A = t & 255; } else if (op === 'SWP') { var tmp = S.A; S.A = S.B; S.B = tmp; }
      else if (op === 'DEC') { S.A = (S.A + 255) & 255; S.Z = S.A === 0 ? 1 : 0; } else if (op === 'JNC') { if (!S.C) next = ins[1]; } else if (op === 'JNZ') { if (S.A !== 0) next = ins[1]; } else if (op === 'HLT') { S.halt = 1; next = S.pc; }
      S.n++; S.last = '第 ' + S.n + ' 步　<b>取指</b>：從位址 ' + at + ' 讀出指令 <code>' + ins.join(' ') + '</code>；<b>解碼並執行</b>：' + DESC[op](ins) + '。' + (op === 'JNC' || op === 'JNZ' ? (next === ins[1] ? '條件成立，跳躍。' : '條件不成立，繼續往下。') : '');
      S.pc = next; draw(); }
    function bits(v) { var s = ''; for (var i = 7; i >= 0; i--) s += '<span style="display:inline-block;width:12px;height:12px;margin:0 1px;border-radius:2px;background:' + ((v >> i) & 1 ? RS : '#5a2a28') + '"></span>'; return s; }
    function draw() { var prog = PROGS[P.p].c, lst = prog.map(function (ins, i) { return '<div style="padding:1px 8px;font-family:ui-monospace,Menlo,monospace;font-size:0.9em;border-radius:4px;background:' + (i === S.pc ? 'rgba(224,48,42,0.2)' : 'transparent') + '">' + (i === S.pc ? '▶ ' : '　') + i + ': ' + ins.join(' ') + '</div>'; }).join('');
      view.innerHTML = '<div style="display:flex;gap:14px;flex-wrap:wrap"><div style="min-width:170px;padding:8px;border:1px solid var(--border);border-radius:8px"><b style="font-size:0.9em">程式記憶體</b>' + lst + '</div>' +
        '<div style="flex:1;min-width:220px;padding:8px;border:1px solid var(--border);border-radius:8px;font-size:0.92em;line-height:1.9">' +
        '<div>程式計數器 PC：<b>' + S.pc + '</b></div><div>暫存器 A：' + bits(S.A) + ' <b>' + S.A + '</b></div><div>暫存器 B：' + bits(S.B) + ' <b>' + S.B + '</b></div>' +
        '<div>旗標：進位 C = ' + S.C + '，零 Z = ' + S.Z + (S.halt ? '　<b style="color:' + RD + '">已停止</b>' : '') + '</div><div>輸出：<b>' + (S.out.length ? S.out.join(', ') : '（無）') + '</b></div></div></div>';
      inf.innerHTML = S.last + '<br><span style="font-size:0.9em;color:var(--text-muted)">這台 8 位元的迷你 CPU 只有 8 種指令。每一步都是「取指 → 解碼 → 執行」，程式計數器指向下一條指令——玩家在 Minecraft 中用紅石建造的電腦，原理完全相同，只是慢了數百萬倍。</span>'; }
    reset();
  }

  function initAll() { document.querySelectorAll('.mcr-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ signal: initSignal, gate: initGate, adder: initAdder, latch: initLatch, cpu: initCPU })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🟥", MCR_NOTE, MCRLIB, "mcr-w")

SIGNAL = mw({"t": "signal", "q": u"紅石粉的訊號強度：每格減 1"})
GATE = mw({"t": "gate", "q": u"邏輯閘：切換拉桿 A、B，看輸出"})
GATE_NAND = mw({"t": "gate", "q": u"NAND 閘", "g": "NAND"})
GATE_XOR = mw({"t": "gate", "q": u"XOR 閘：不同時才輸出 1", "g": "XOR"})
ADDER = mw({"t": "adder", "q": u"四位元加法器：點方塊切換位元"})
LATCH = mw({"t": "latch", "q": u"閂鎖與正反器：電路如何記住一個位元"})
CPU = mw({"t": "cpu", "q": u"迷你 CPU：一步一步執行程式"})
