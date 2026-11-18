# -*- coding: utf-8 -*-
"""〈編譯器：程式碼怎麼變成機器碼〉（cmp_）共用：課程包裝與 CMPLIB 互動元件（class="cmp-w"）。

  lex    詞法分析：把算式切成 token
  ast    遞迴下降剖析：畫出抽象語法樹
  pipe   完整流程：三位址碼、常數摺疊、堆疊機組合語言與執行
  reg    暫存器配置：干涉圖著色
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

CMP_NOTE = u"互動工具實作了一個極小的算式語言（數字、變數、+ − × ÷ ^ 與括號），用來示範編譯器的各個階段。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def cw(cfg, maxw=680):
    return wdg("cmp-w", cfg, maxw)


def code(s):
    return ("code", s.strip("\n"))


CMPLIB = r"""
(function () {
  if (window.__cmpLib) return; window.__cmpLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function input(root, val, cb) { var i = document.createElement('input'); i.type = 'text'; i.value = val; i.spellcheck = false;
    i.style.cssText = 'width:100%;box-sizing:border-box;padding:6px 10px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:1em;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text);margin:4px 0 8px';
    i.addEventListener('input', function () { cb(i.value); }); root.appendChild(i); return i; }
  var VARS = { x: 2, y: 3, z: 5 };
  function lex(src) { var t = [], i = 0; while (i < src.length) { var c = src[i];
      if (/\s/.test(c)) { i++; continue; }
      if (/[0-9.]/.test(c)) { var j = i; while (j < src.length && /[0-9.]/.test(src[j])) j++; t.push({ k: 'NUM', v: src.slice(i, j), p: i }); i = j; continue; }
      if (/[A-Za-z_]/.test(c)) { var j2 = i; while (j2 < src.length && /[A-Za-z_0-9]/.test(src[j2])) j2++; t.push({ k: 'ID', v: src.slice(i, j2), p: i }); i = j2; continue; }
      if ('+-*/^()'.indexOf(c) >= 0) { t.push({ k: c == '(' || c == ')' ? 'PAREN' : 'OP', v: c, p: i }); i++; continue; }
      throw { m: '無法辨識的字元「' + c + '」', p: i }; }
    t.push({ k: 'EOF', v: '', p: src.length }); return t; }
  function parse(src) { var t = lex(src), i = 0;
    function pk() { return t[i]; } function nx() { return t[i++]; }
    function expect(v) { if (pk().v !== v) throw { m: '這裡應該是「' + v + '」，卻看到「' + (pk().v || '結尾') + '」', p: pk().p }; nx(); }
    function expr() { var n = term(); while (pk().v == '+' || pk().v == '-') { var o = nx().v; n = { op: o, a: n, b: term() }; } return n; }
    function term() { var n = factor(); while (pk().v == '*' || pk().v == '/') { var o = nx().v; n = { op: o, a: n, b: factor() }; } return n; }
    function factor() { var n = unary(); if (pk().v == '^') { nx(); return { op: '^', a: n, b: factor() }; } return n; }
    function unary() { if (pk().v == '-') { nx(); return { op: 'neg', a: unary() }; } return primary(); }
    function primary() { var k = pk(); if (k.k == 'NUM') { nx(); if (isNaN(+k.v)) throw { m: '數字格式錯誤「' + k.v + '」', p: k.p }; return { num: +k.v }; } if (k.k == 'ID') { nx(); return { id: k.v }; }
      if (k.v == '(') { nx(); var n = expr(); expect(')'); return n; } throw { m: '這裡應該是數字、變數或「(」，卻看到「' + (k.v || '結尾') + '」', p: k.p }; }
    var r = expr(); if (pk().k != 'EOF') throw { m: '多出了「' + pk().v + '」', p: pk().p }; return r; }
  function errBox(e, src) { return '<span style="color:' + RD + '"><b>錯誤</b>：' + esc(e.m || e) + '</span>' + (e.p !== undefined ? '<br><code>' + esc(src) + '</code><br><code>' + '&nbsp;'.repeat(e.p) + '^</code>' : ''); }
  function lbl(n) { return n.num !== undefined ? String(n.num) : n.id !== undefined ? n.id : n.op == 'neg' ? '−' : n.op == '*' ? '×' : n.op == '/' ? '÷' : n.op; }
  function kids(n) { return n.op ? (n.op == 'neg' ? [n.a] : [n.a, n.b]) : []; }

  function initLex(root, cfg) {
    head(root, cfg.q); var view = el('div', 'line-height:2.2'), inf;
    input(root, cfg.src || 'total = 3.14 * (r + 2)', draw); root.appendChild(view); inf = info(root);
    var COL = { NUM: OR, ID: BL, OP: RD, PAREN: GY };
    function draw(src) { try { var src2 = src.replace('=', ' '), t = lex(src2.replace(/[=;]/g, ' ')); var h = '';
        t.forEach(function (k) { if (k.k == 'EOF') return; h += '<span style="display:inline-block;margin:0 4px 4px 0;padding:0 8px;border-radius:6px;border:1.5px solid ' + COL[k.k] + ';font-family:ui-monospace,monospace"><small style="color:' + COL[k.k] + '">' + k.k + '</small> ' + esc(k.v) + '</span>'; });
        view.innerHTML = h; inf.innerHTML = '詞法分析器從左到右掃描字元，把它們分組成 <b>' + (t.length - 1) + '</b> 個 token：<span style="color:' + OR + '">NUM</span> 數字、<span style="color:' + BL + '">ID</span> 識別字、<span style="color:' + RD + '">OP</span> 運算子、括號。空白被丟掉了。' +
          '<br>試試看：輸入 <code>3.14.15</code> 或 <code>2 $ 3</code>，看看詞法分析器怎麼回應。<span style="font-size:0.9em;color:var(--text-muted)">（為了簡單，等號與分號在這裡被當作空白。）</span>'; }
      catch (e) { view.innerHTML = ''; inf.innerHTML = errBox(e, src); } }
    draw(cfg.src || 'total = 3.14 * (r + 2)');
  }

  function initAst(root, cfg) {
    head(root, cfg.q); var view = el('div'), inf;
    input(root, cfg.src || '1 + 2 * (x - 3) ^ 2', draw); root.appendChild(view); inf = info(root);
    function draw(src) { try { var tr = parse(src), leaf = 0, depth = 0, pos = [];
        (function lay(n, d) { depth = Math.max(depth, d); var ks = kids(n); if (!ks.length) { n._x = leaf++; } else { ks.forEach(function (k) { lay(k, d + 1); }); n._x = ks.reduce(function (s, k) { return s + k._x; }, 0) / ks.length; } n._d = d; })(tr, 0);
        var W = 640, gap = Math.min(70, (W - 40) / Math.max(leaf, 1)), x0 = (W - gap * (leaf - 1)) / 2, H = 50 + depth * 56, g = '';
        function X(n) { return x0 + n._x * gap; } function Y(n) { return 26 + n._d * 56; }
        (function edges(n) { kids(n).forEach(function (k) { g += ln(X(n), Y(n), X(k), Y(k), '#999', 1.5); edges(k); }); })(tr);
        (function nodes(n) { var leafn = !kids(n).length; g += '<circle cx="' + n1(X(n)) + '" cy="' + Y(n) + '" r="16" fill="' + (leafn ? (n.num !== undefined ? '#fbe3c9' : '#d6e4f3') : '#f3d6d4') + '" stroke="' + (leafn ? (n.num !== undefined ? OR : BL) : RD) + '" stroke-width="1.5"/>' + tx(X(n), Y(n) + 4, esc(lbl(n)), 12); kids(n).forEach(nodes); })(tr);
        view.innerHTML = svgw('0 0 640 ' + H, g);
        inf.innerHTML = '這棵<b>抽象語法樹</b>由遞迴下降剖析器產生。越<b>下層</b>的運算越<b>先</b>算：括號、^（次方）、× ÷、最後才是 + −。注意 <code>2 ^ 3 ^ 2</code> 是<b>右結合</b>（先算 3 ^ 2），而 <code>8 − 3 − 2</code> 是左結合。' +
          '<br>試著輸入不完整的算式（例如 <code>(1 + 2</code>），看看剖析器的錯誤訊息。'; }
      catch (e) { view.innerHTML = ''; inf.innerHTML = errBox(e, src); } }
    draw(cfg.src || '1 + 2 * (x - 3) ^ 2');
  }

  function initPipe(root, cfg) {
    head(root, cfg.q); var P = { fold: 1, src: cfg.src || 'x * (2 + 3) + y * 4 - 0 * z' }, view = el('div'), inf;
    input(root, P.src, function (v) { P.src = v; draw(); });
    var b = el('div', 'margin:0 0 6px'), fb = btn('常數摺疊與化簡：開'); fb.onclick = function () { P.fold ^= 1; fb.textContent = '常數摺疊與化簡：' + (P.fold ? '開' : '關'); draw(); }; b.appendChild(fb); root.appendChild(b);
    root.appendChild(view); inf = info(root);
    function fold(n) { if (!n.op) return n; var a = fold(n.a), bb = n.b ? fold(n.b) : null;
      if (n.op == 'neg') return a.num !== undefined ? { num: -a.num } : { op: 'neg', a: a };
      if (a.num !== undefined && bb.num !== undefined) { var v = n.op == '+' ? a.num + bb.num : n.op == '-' ? a.num - bb.num : n.op == '*' ? a.num * bb.num : n.op == '/' ? a.num / bb.num : Math.pow(a.num, bb.num); return { num: v }; }
      if (n.op == '*' && (a.num === 0 || bb.num === 0)) return { num: 0 };
      if (n.op == '*' && a.num === 1) return bb; if ((n.op == '*' || n.op == '/') && bb.num === 1) return a;
      if (n.op == '+' && a.num === 0) return bb; if ((n.op == '+' || n.op == '-') && bb.num === 0) return a;
      if (n.op == '^' && bb.num === 2) return { op: '*', a: a, b: a, sq: 1 };
      return { op: n.op, a: a, b: bb }; }
    function tac(tr) { var code = [], k = 0; function g(n) { if (n.num !== undefined) return String(n.num); if (n.id !== undefined) return n.id;
        if (n.op == 'neg') { var a = g(n.a), t = 't' + (++k); code.push(t + ' = −' + a); return t; }
        var a2 = g(n.a), b2 = n.sq ? a2 : g(n.b), t2 = 't' + (++k), o = n.op == '*' ? '×' : n.op == '/' ? '÷' : n.op; code.push(t2 + ' = ' + a2 + ' ' + o + ' ' + b2); return t2; }
      var r = g(tr); if (!code.length) code.push('t1 = ' + r); return code; }
    function asm(tr) { var c = []; function g(n) { if (n.num !== undefined) { c.push('PUSH  ' + n.num); return; } if (n.id !== undefined) { c.push('LOAD  ' + n.id); return; }
        if (n.op == 'neg') { g(n.a); c.push('NEG'); return; } g(n.a); if (n.sq) c.push('DUP'); else g(n.b); c.push({ '+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV', '^': 'POW' }[n.op]); }
      g(tr); return c; }
    function run(c) { var st = []; c.forEach(function (ins) { var p = ins.split(/\s+/), op = p[0];
        if (op == 'PUSH') st.push(+p[1]); else if (op == 'LOAD') st.push(VARS[p[1]] !== undefined ? VARS[p[1]] : 1); else if (op == 'NEG') st.push(-st.pop()); else if (op == 'DUP') st.push(st[st.length - 1]);
        else { var b = st.pop(), a = st.pop(); st.push(op == 'ADD' ? a + b : op == 'SUB' ? a - b : op == 'MUL' ? a * b : op == 'DIV' ? a / b : Math.pow(a, b)); } }); return st[0]; }
    function box(t, lines, c) { return '<div style="flex:1;min-width:180px"><div style="font-size:0.85em;color:' + c + ';font-weight:bold;margin-bottom:2px">' + t + '</div><pre style="margin:0;padding:8px;border-radius:6px;background:var(--surface);border:1px solid var(--border);font-size:0.85em;line-height:1.45;overflow-x:auto">' + esc(lines.join('\n')) + '</pre></div>'; }
    function draw() { try { var tr = parse(P.src), t0 = tac(tr), tr2 = P.fold ? fold(tr) : tr, t1 = tac(tr2), a = asm(tr2), r = run(a);
        view.innerHTML = '<div style="display:flex;gap:10px;flex-wrap:wrap">' + box('三位址碼（未最佳化）', t0, GY) + box('三位址碼（' + (P.fold ? '最佳化後' : '未最佳化') + '）', t1, GN) + box('堆疊機組合語言', a, PU) + '</div>';
        inf.innerHTML = '最佳化前 <b>' + t0.length + '</b> 條指令，' + (P.fold ? '最佳化後 <b>' + t1.length + '</b> 條。編譯器在編譯時就把 2 + 3 算成 5、把 0 × z 變成 0、把 + 0 與 × 1 刪掉。' : '沒有最佳化。') +
          '<br>執行堆疊機程式（x = 2、y = 3、z = 5，其他變數 = 1）：結果 = <b>' + (Math.round(r * 1e6) / 1e6) + '</b>。最佳化不改變結果，只讓程式更短、更快。'; }
      catch (e) { view.innerHTML = ''; inf.innerHTML = errBox(e, P.src); } }
    draw();
  }

  var RV = ['a', 'b', 'c', 'd', 'e', 'f', 'g'], RE = [['a', 'b'], ['a', 'c'], ['b', 'c'], ['b', 'd'], ['c', 'd'], ['c', 'e'], ['d', 'e'], ['d', 'f'], ['e', 'f'], ['e', 'g'], ['f', 'g'], ['a', 'd']];
  var RC = ['#e88a6a', '#7cb7e8', '#8fd19e', '#d6b4f0', '#f5d06a', '#9adbd0'];
  function initReg(root, cfg) {
    head(root, cfg.q); var P = { k: 3 }, view = el('div'), inf;
    var us = [slider(root, '可用的暫存器數 k', 1, 5, 1, P.k, function (x) { return x; }, null, function (x) { P.k = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var adj = {}; RV.forEach(function (v) { adj[v] = []; }); RE.forEach(function (e) { adj[e[0]].push(e[1]); adj[e[1]].push(e[0]); });
      var order = RV.slice().sort(function (p, q) { return adj[q].length - adj[p].length; }), col = {}, spill = [];
      order.forEach(function (v) { var used = adj[v].map(function (u) { return col[u]; }); for (var c = 0; c < P.k; c++) if (used.indexOf(c) < 0) { col[v] = c; return; } spill.push(v); });
      var pos = {}, g = ''; RV.forEach(function (v, i) { var a = -Math.PI / 2 + i * 2 * Math.PI / RV.length; pos[v] = [320 + 170 * Math.cos(a), 130 + 105 * Math.sin(a)]; });
      RE.forEach(function (e) { g += ln(pos[e[0]][0], pos[e[0]][1], pos[e[1]][0], pos[e[1]][1], '#aaa', 1.5); });
      RV.forEach(function (v) { var s = spill.indexOf(v) >= 0; g += '<circle cx="' + n1(pos[v][0]) + '" cy="' + n1(pos[v][1]) + '" r="20" fill="' + (s ? '#fff' : RC[col[v]]) + '" stroke="' + (s ? RD : '#555') + '" stroke-width="' + (s ? 3 : 1.5) + '" ' + (s ? 'stroke-dasharray="4 3"' : '') + '/>' + tx(pos[v][0], pos[v][1] + 5, v, 14) + tx(pos[v][0], pos[v][1] + 34, s ? '溢出' : 'R' + col[v], 10, s ? RD : 'var(--text-muted)'); });
      view.innerHTML = svgw('0 0 640 270', g);
      inf.innerHTML = '每個圓圈是一個變數，連線代表兩個變數<b>同時存活</b>（干涉），不能放在同一個暫存器。用 ' + P.k + ' 種顏色（暫存器）著色：' + (spill.length ? '有 <b>' + spill.length + '</b> 個變數無法分配（' + spill.join('、') + '），必須<b>溢出</b>到記憶體，每次使用都要額外的載入與儲存。' : '<b>全部</b>都分配到了暫存器！') +
        '<br>這是經典的<b>圖著色</b>問題（NP 完全），編譯器使用貪婪的近似方法：先處理連線最多的變數。'; }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.cmp-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ lex: initLex, ast: initAst, pipe: initPipe, reg: initReg })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🛠️", CMP_NOTE, CMPLIB, "cmp-w")

LEX = cw({"t": "lex", "q": u"詞法分析器：輸入一行程式，看它被切成哪些 token"})
AST = cw({"t": "ast", "q": u"遞迴下降剖析器：輸入算式，看它的抽象語法樹"})
PIPE = cw({"t": "pipe", "q": u"一個迷你編譯器：從算式到三位址碼、最佳化與堆疊機組合語言"})
REG = cw({"t": "reg", "q": u"暫存器配置：用圖著色把變數分配到暫存器"})
