# -*- coding: utf-8 -*-
"""〈GitHub 從零到協作〉（gh_）共用工具：實跑的 Git 範例（gex）與互動元件（GHLIB）。"""
import io
import json
import os
from cc_common import *
from qt_common import BASEJS
import builder as B

HERE = os.path.dirname(os.path.abspath(__file__))
_EX = json.load(io.open(os.path.join(HERE, "gh_ex_out.json"), encoding="utf-8"))

GH_NOTE = (u"本課程的 Git 指令範例都在 Git 2.43 實際執行過，畫面上的輸出就是當時的結果（日期固定，所以雜湊值可重現）；"
           u"範例中的「GitHub 遠端」是用本機的裸倉庫模擬的，指令與真正連到 GitHub 時相同，只有網址不同。"
           u"GitHub 網站的按鈕位置與名稱偶爾會改版，以官方說明為準。")


def _term(pairs):
    out = []
    for cmd, body in pairs:
        out.append(u'<span style="color:#7ee2a8">$</span> <span style="color:#ffd479">%s</span>' % B.esc(cmd))
        if body:
            out.append(B.esc(body))
    return ("raw", u'<div class="code-block" style="background:#14181f;color:#d8dde6">%s</div>' % u"\n".join(out).replace("\n", "&#10;"))


def gex(name, a=0, b=None, label=None):
    """嵌入範例 name 的第 a～b 個指令（含實際輸出）。"""
    pairs = _EX[name][a:b]
    head = ("raw", u'<p style="margin:16px 0 4px"><strong>▶ %s</strong>　<span style="color:var(--text-muted);font-size:0.88em">實際執行的輸出</span></p>' % (label or u"動手做"))
    return [head, _term(pairs)]


def cmd(text):
    """只顯示指令（沒有實跑輸出，例如需要真正連線 GitHub 的指令）。"""
    return ("raw", u'<div class="code-block" style="background:#14181f;color:#d8dde6">%s</div>'
            % u"\n".join(u'<span style="color:#7ee2a8">$</span> <span style="color:#ffd479">%s</span>' % B.esc(l) if not l.startswith("#") else
                         u'<span style="color:#8b95a5">%s</span>' % B.esc(l) for l in text.strip().split("\n")).replace("\n", "&#10;"))


GHLIB = r"""
(function () {
  if (window.__ghLib) return; window.__ghLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  var MONO = 'font-family:ui-monospace,Menlo,Consolas,monospace;';
  var COLS = ['#3a6ea5', '#2e8b57', '#d0564f', '#8e5bb5', '#d08a2a', '#2a9d9d', '#777'];

  /* ---------- 三個區域 ---------- */
  function initAreas(root, cfg) {
    head(root, cfg.q);
    var F, logs, view = el('div'), out = el('div', MONO + 'margin-top:8px;padding:8px 10px;border-radius:8px;background:#14181f;color:#d8dde6;font-size:0.85em;white-space:pre-wrap;min-height:3.2em'), bb;
    function reset() { F = [{ n: 'README.md', w: 1, i: 1, r: 1 }, { n: 'app.py', w: 1, i: 1, r: 1 }, { n: 'notes.txt', w: 1, i: null, r: null }]; logs = []; }
    reset(); root.appendChild(view); root.appendChild(out); bb = bar(root);
    var bc = btn('git commit', 'c'); bc.addEventListener('click', function () { commit(); }); bb.appendChild(bc);
    var bs = btn('git status --short', 's'); bs.addEventListener('click', function () { log('git status --short', status() || '（乾淨，沒有任何變更）'); }); bb.appendChild(bs);
    var br = btn('重來', 'r'); br.addEventListener('click', function () { reset(); draw(); }); bb.appendChild(br);
    var p = info(root);
    p.innerHTML = '點檔案下方的按鈕：<b>編輯</b>改工作目錄、<b>add</b> 放進暫存區、<b>commit</b> 存進儲存庫。檔名旁的數字是「版本」，看它在三個區域之間怎麼流動。';
    function code(f) { if (f.r === null && f.i === null) return '??'; var x = f.i !== f.r ? (f.r === null ? 'A' : 'M') : ' ', y = f.w !== f.i ? 'M' : ' '; return (x + y === '  ') ? '' : x + y; }
    function status() { return F.map(function (f) { var c = code(f); return c ? c + ' ' + f.n : ''; }).filter(Boolean).join('\n'); }
    function log(c, t) { logs.push('$ ' + c + (t ? '\n' + t : '')); logs = logs.slice(-3); out.textContent = logs.join('\n'); draw(); }
    function commit() { var ch = F.filter(function (f) { return f.i !== null && f.i !== f.r; }); if (!ch.length) { log('git commit -m "…"', 'nothing to commit（暫存區沒有新東西）'); return; }
      ch.forEach(function (f) { f.r = f.i; }); log('git commit -m "…"', ch.length + ' file(s) changed：' + ch.map(function (f) { return f.n; }).join('、')); }
    function chip(f, v, area) { var col = v === null ? 'var(--border)' : (area === 'w' && f.w !== f.i) || (area === 'i' && f.i !== f.r) ? '#d0564f' : '#2e8b57';
      return '<div style="margin:4px 0;padding:3px 6px;border-radius:6px;border:2px solid ' + col + ';' + (v === null ? 'opacity:0.35;' : '') + MONO + 'font-size:0.8em;word-break:break-all">' + esc(f.n) + (v === null ? '' : ' <b>v' + v + '</b>') + '</div>'; }
    function draw() { var h = '<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px">';
      [['w', '📝 工作目錄', '你正在編輯的檔案'], ['i', '📦 暫存區（index）', '下一個 commit 的內容'], ['r', '🗄️ 儲存庫（.git）', '已存檔的歷史']].forEach(function (a) {
        h += '<div style="padding:6px;border-radius:8px;background:var(--surface);border:1px solid var(--border);min-width:0"><div style="font-weight:bold;font-size:0.92em">' + a[1] + '</div><div style="font-size:0.78em;color:var(--text-muted)">' + a[2] + '</div>';
        F.forEach(function (f) { h += chip(f, f[a[0]], a[0]); }); h += '</div>'; });
      h += '</div><div style="margin-top:8px;display:flex;flex-wrap:wrap;gap:6px">';
      F.forEach(function (f, k) { h += '<div style="font-size:0.85em;padding:4px 6px;border:1px dashed var(--border);border-radius:8px"><b>' + esc(f.n) + '</b>：' +
        '<button type="button" data-a="e" data-f="' + k + '">編輯</button> <button type="button" data-a="a" data-f="' + k + '">add</button> <button type="button" data-a="u" data-f="' + k + '">restore</button> <button type="button" data-a="s" data-f="' + k + '">restore --staged</button></div>'; });
      view.innerHTML = h + '</div>';
      view.querySelectorAll('button[data-a]').forEach(function (b) { b.style.cssText = 'font:inherit;font-size:0.85em;padding:2px 6px;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer';
        b.addEventListener('click', function () { var f = F[+b.getAttribute('data-f')], a = b.getAttribute('data-a');
          if (a === 'e') { f.w = Math.max(f.w, f.i || 0, f.r || 0) + 1; log('（用編輯器修改 ' + f.n + '）', ''); }
          else if (a === 'a') { f.i = f.w; log('git add ' + f.n, ''); }
          else if (a === 'u') { if (f.i === null) { log('git restore ' + f.n, 'error: pathspec \'' + f.n + '\' did not match any file(s) known to git（未追蹤的檔案沒有可以還原的版本）'); return; } f.w = f.i; log('git restore ' + f.n, '（工作目錄回到暫存區的版本 v' + f.i + '，剛才的修改丟掉了）'); }
          else { if (f.r === null) { f.i = null; log('git restore --staged ' + f.n, '（從暫存區移除，變回未追蹤）'); } else { f.i = f.r; log('git restore --staged ' + f.n, '（暫存區回到儲存庫的版本 v' + f.r + '；工作目錄不受影響）'); } } }); });
    }
    draw();
  }

  /* ---------- reset 三種模式 ---------- */
  function initReset(root, cfg) {
    head(root, cfg.q); var bb = bar(root), view = el('div'); root.appendChild(view); var p = info(root);
    var M = { soft: ['C 的修改', 'C 的修改', '—', '只移動分支指標。C 的修改還在暫存區，馬上可以重新 commit（常用來「把幾個 commit 合成一個」）。'],
      mixed: ['C 的修改', '—', '—', '預設模式。移動分支指標並清空暫存區；C 的修改留在工作目錄，變成「尚未 add」。'],
      hard: ['—', '—', '—', '移動分支指標，暫存區與工作目錄也一起改回 B。C 的修改<b>從檔案中消失</b>（只能靠 reflog 救回 commit；從未 commit 的修改則救不回來）。'] };
    ['soft', 'mixed', 'hard'].forEach(function (k) { var b = btn('git reset --' + k + ' HEAD~1', k); b.addEventListener('click', function () { mark(bb, k); draw(k); }); bb.appendChild(b); });
    function draw(k) { var m = M[k], g = '';
      [['A', 60], ['B', 180], ['C', 300]].forEach(function (c, i) { var dead = c[0] === 'C'; g += (i ? ln(c[1] - 90, 50, c[1] - 22, 50, '#999', 2) : '') + '<circle cx="' + c[1] + '" cy="50" r="20" fill="' + (dead ? 'var(--surface)' : '#3a6ea5') + '" stroke="#3a6ea5" stroke-width="2"' + (dead ? ' stroke-dasharray="4 3"' : '') + '/>' + tx(c[1], 55, c[0], 14, dead ? '#3a6ea5' : '#fff'); });
      g += '<rect x="150" y="88" width="60" height="22" rx="5" fill="#2e8b57"/>' + tx(180, 103, 'main', 11, '#fff') + tx(300, 103, '（原本 main 在這）', 10, 'var(--text-muted)');
      var labs = ['工作目錄', '暫存區', '儲存庫（HEAD→B）']; labs.forEach(function (l, i) { var x = 400 + i * 0; });
      g += tx(470, 30, '工作目錄：' + m[0], 12, 'currentColor', 'start') + tx(470, 56, '暫存區：' + m[1], 12, 'currentColor', 'start') + tx(470, 82, '儲存庫：HEAD 指向 B', 12, 'currentColor', 'start');
      view.innerHTML = svgw('0 0 680 120', g); p.innerHTML = m[3]; }
    mark(bb, 'mixed'); draw('mixed');
  }

  /* ---------- Git 分支模擬器 ---------- */
  function sh(n) { return ('0000000' + (((n + 7) * 2654435761) >>> 0).toString(16)).slice(-7); }
  function initGraph(root, cfg) {
    head(root, cfg.q);
    var S, view = el('div', 'overflow-x:auto'), term = el('div', MONO + 'margin-top:8px;padding:8px 10px;border-radius:8px;background:#14181f;color:#d8dde6;font-size:0.84em;white-space:pre-wrap;max-height:10em;overflow-y:auto');
    var inp = el('input'); inp.type = 'text'; inp.placeholder = '輸入指令，例如 git switch -c feature'; inp.style.cssText = MONO + 'width:100%;box-sizing:border-box;padding:6px 8px;margin-top:6px;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text)';
    root.appendChild(view); root.appendChild(term); root.appendChild(inp); var bb = bar(root);
    var sug = cfg.cmds || ['git commit', 'git switch -c feature', 'git commit', 'git switch main', 'git commit', 'git merge feature', 'git rebase main', 'git reset --hard HEAD~1', 'git log'];
    sug.forEach(function (c) { var b = btn(c); b.style.fontFamily = 'ui-monospace,Menlo,Consolas,monospace'; b.addEventListener('click', function () { run(c); }); bb.appendChild(b); });
    var br = btn('↺ 重來'); br.addEventListener('click', function () { init(); }); bb.appendChild(br);
    var p = info(root);
    p.innerHTML = '可用指令：<code>git commit</code>、<code>git branch 名稱</code>、<code>git switch 名稱</code>、<code>git switch -c 名稱</code>、<code>git merge 名稱</code>、<code>git rebase 名稱</code>、<code>git reset --hard HEAD~1</code>、<code>git revert HEAD</code>、<code>git cherry-pick 雜湊</code>、<code>git branch -d 名稱</code>、<code>git log</code>。圓圈是 commit，彩色標籤是分支，<b>HEAD</b> 標示你目前所在的分支；虛線圓圈是已經沒有分支指到的 commit（還能用 reflog 找回）。';
    inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') { run(inp.value); inp.value = ''; } });
    function init() { S = { c: {}, order: [], br: {}, lane: {}, head: 'main', n: 0, out: [] };
      var a = mk([], '初始提交', 0), b = mk([a], '加入 app.py', 0); S.br.main = b; S.lane.main = 0; (cfg.init || []).forEach(function (c) { run(c, true); }); S.out = []; draw(); }
    function mk(par, msg, lane) { var id = sh(S.n++); S.c[id] = { p: par, m: msg, lane: lane, x: S.order.length }; S.order.push(id); return id; }
    function anc(a, b) { /* a 是否為 b 的祖先（含相同） */ var st = [b], seen = {}; while (st.length) { var x = st.pop(); if (x === a) return true; if (seen[x]) continue; seen[x] = 1; S.c[x].p.forEach(function (q) { st.push(q); }); } return false; }
    function reach(b) { var st = [b], seen = {}; while (st.length) { var x = st.pop(); if (seen[x]) continue; seen[x] = 1; S.c[x].p.forEach(function (q) { st.push(q); }); } return seen; }
    function say(t) { S.out.push(t); }
    function cur() { return S.br[S.head]; }
    function laneOf(name) { if (S.lane[name] === undefined) { var used = {}; Object.keys(S.lane).forEach(function (k) { if (S.br[k] !== undefined) used[S.lane[k]] = 1; }); var l = 0; while (used[l]) l++; S.lane[name] = l; } return S.lane[name]; }
    var CN = 0;
    function run(raw, quiet) { var c = raw.trim().replace(/\s+/g, ' '); if (!c) return; say('$ ' + c); var w = c.split(' '); if (w[0] !== 'git') { say('只支援 git 指令'); return draw(); }
      var op = w[1], a = w.slice(2);
      try {
        if (op === 'commit') { var m = (c.match(/-m ["']?([^"']*)/) || [])[1] || ('第 ' + (++CN) + ' 次修改'); var id = mk([cur()], m, laneOf(S.head)); S.br[S.head] = id; say('[' + S.head + ' ' + id + '] ' + m); }
        else if (op === 'branch' && (a[0] === '-d' || a[0] === '-D')) { var n = a[1]; if (S.br[n] === undefined) throw 'error: branch \'' + n + '\' not found'; if (n === S.head) throw 'error: 不能刪除目前所在的分支 \'' + n + '\''; if (a[0] === '-d' && !anc(S.br[n], cur())) throw 'error: the branch \'' + n + '\' is not fully merged（還沒合併；確定要刪就用 -D）'; say('Deleted branch ' + n + ' (was ' + S.br[n] + ').'); delete S.br[n]; }
        else if (op === 'branch' && !a.length) { Object.keys(S.br).forEach(function (k) { say((k === S.head ? '* ' : '  ') + k); }); }
        else if (op === 'branch') { if (S.br[a[0]] !== undefined) throw 'fatal: a branch named \'' + a[0] + '\' already exists'; S.br[a[0]] = cur(); laneOf(a[0]); }
        else if ((op === 'switch' && a[0] === '-c') || (op === 'checkout' && a[0] === '-b')) { if (!a[1]) throw '需要分支名稱'; if (S.br[a[1]] !== undefined) throw 'fatal: a branch named \'' + a[1] + '\' already exists'; S.br[a[1]] = cur(); laneOf(a[1]); S.head = a[1]; say('Switched to a new branch \'' + a[1] + '\''); }
        else if (op === 'switch' || op === 'checkout') { if (S.br[a[0]] === undefined) throw 'fatal: invalid reference: ' + a[0]; S.head = a[0]; say('Switched to branch \'' + a[0] + '\''); }
        else if (op === 'merge') { var t = S.br[a[0]]; if (t === undefined) throw 'merge: ' + a[0] + ' - not something we can merge';
          if (anc(t, cur())) say('Already up to date.'); else if (anc(cur(), t)) { say('Updating ' + cur() + '..' + t + '\nFast-forward（快轉：' + S.head + ' 直接往前移，沒有新的 commit）'); S.br[S.head] = t; }
          else { var id2 = mk([cur(), t], 'Merge branch \'' + a[0] + '\'', laneOf(S.head)); S.br[S.head] = id2; say('Merge made by the \'ort\' strategy.（產生合併 commit ' + id2 + '）'); } }
        else if (op === 'rebase') { var u = S.br[a[0]]; if (u === undefined) throw 'fatal: invalid upstream \'' + a[0] + '\''; var R = reach(u), list = [], st = cur();
          while (st && !R[st]) { list.unshift(st); st = S.c[st].p[0]; }
          if (!list.length) { if (anc(cur(), u) && cur() !== u) { S.br[S.head] = u; say('Successfully rebased and updated refs/heads/' + S.head + '.（快轉到 ' + a[0] + '）'); } else say('Current branch ' + S.head + ' is up to date.'); }
          else { var base = u; list.forEach(function (x) { base = mk([base], S.c[x].m, laneOf(S.head)); }); S.br[S.head] = base; say('Successfully rebased and updated refs/heads/' + S.head + '.（' + list.length + ' 個 commit 被複製成新的 commit，雜湊值都變了）'); } }
        else if (op === 'reset') { var r = (c.match(/HEAD~(\d+)/) || [])[1]; if (!r) throw '這個模擬器只支援 git reset --hard HEAD~N'; var x = cur(); for (var k = 0; k < +r; k++) { if (!S.c[x].p.length) throw 'fatal: 已經到最早的 commit 了'; x = S.c[x].p[0]; } S.br[S.head] = x; say('HEAD is now at ' + x + ' ' + S.c[x].m); }
        else if (op === 'revert') { var h = cur(); var id3 = mk([h], 'Revert "' + S.c[h].m + '"', laneOf(S.head)); S.br[S.head] = id3; say('[' + S.head + ' ' + id3 + '] Revert "' + S.c[h].m + '"（新增一個「反向」的 commit，歷史不會被改寫）'); }
        else if (op === 'cherry-pick') { var src = S.c[a[0]] ? a[0] : S.br[a[0]]; if (!src || !S.c[src]) throw 'fatal: bad revision \'' + a[0] + '\''; var id4 = mk([cur()], S.c[src].m, laneOf(S.head)); S.br[S.head] = id4; say('[' + S.head + ' ' + id4 + '] ' + S.c[src].m + '（複製 ' + src + ' 的修改）'); }
        else if (op === 'log') { var y = cur(); while (y) { say(y + ' ' + S.c[y].m); y = S.c[y].p[0]; } }
        else if (op === 'status') { say('On branch ' + S.head); }
        else throw '這個模擬器不支援 git ' + op;
      } catch (e) { say(String(e)); }
      if (!quiet) draw(); }
    function draw() { var R = {}; Object.keys(S.br).forEach(function (b) { var r = reach(S.br[b]); Object.keys(r).forEach(function (k) { R[k] = 1; }); });
      var W = Math.max(640, 80 + S.order.length * 62), maxl = 0; S.order.forEach(function (id) { maxl = Math.max(maxl, S.c[id].lane); });
      var H = 70 + (maxl + 1) * 70, g = '';
      function X(id) { return 40 + S.c[id].x * 62; } function Y(id) { return 50 + S.c[id].lane * 70; }
      S.order.forEach(function (id) { S.c[id].p.forEach(function (q, i) { var x1 = X(q), y1 = Y(q), x2 = X(id), y2 = Y(id), d = y1 === y2 ? 'M' + x1 + ',' + y1 + ' L' + x2 + ',' + y2 : 'M' + x1 + ',' + y1 + ' C' + (x1 + 30) + ',' + y1 + ' ' + (x2 - 30) + ',' + y2 + ' ' + x2 + ',' + y2;
        g += '<path d="' + d + '" fill="none" stroke="' + (R[id] ? COLS[S.c[id].lane % 7] : '#bbb') + '" stroke-width="2.5"' + (R[id] ? '' : ' stroke-dasharray="4 4"') + '/>'; }); });
      S.order.forEach(function (id) { var on = R[id], col = COLS[S.c[id].lane % 7];
        g += '<g><title>' + esc(id + ' ' + S.c[id].m) + '</title><circle cx="' + X(id) + '" cy="' + Y(id) + '" r="15" fill="' + (on ? col : 'var(--surface)') + '" stroke="' + (on ? col : '#bbb') + '" stroke-width="2"' + (on ? '' : ' stroke-dasharray="3 3"') + '/>' + tx(X(id), Y(id) + 4, id.slice(0, 3), 9, on ? '#fff' : '#999') + '</g>'; });
      var stack = {}; Object.keys(S.br).forEach(function (b) { var id = S.br[b], k = stack[id] || 0; stack[id] = k + 1; var isH = b === S.head, lab = (isH ? 'HEAD→' : '') + b, w = lab.length * 7 + 14, x = X(id) - w / 2, y = Y(id) - 40 - k * 22;
        g += '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="18" rx="5" fill="' + COLS[(S.lane[b] || 0) % 7] + '"' + (isH ? ' stroke="currentColor" stroke-width="2"' : '') + '/>' + tx(X(id), y + 13, esc(lab), 10.5, '#fff'); });
      var top = 0; Object.keys(stack).forEach(function (id) { top = Math.max(top, stack[id]); });
      var off = Math.max(0, (top - 1) * 22);
      view.innerHTML = '<svg viewBox="0 ' + (-off) + ' ' + W + ' ' + (H + off) + '" style="width:' + Math.max(100, W / 6.4) + '%;min-width:100%;display:block;color:var(--text)">' + g + '</svg>';
      term.textContent = S.out.slice(-14).join('\n') || '（在下方輸入指令，或按按鈕）'; term.scrollTop = 1e6; }
    init();
  }

  /* ---------- 合併衝突練習 ---------- */
  function initConflict(root, cfg) {
    head(root, cfg.q);
    var ours = cfg.ours, theirs = cfg.theirs, pre = cfg.pre || '', post = cfg.post || '', br = cfg.br || 'feature';
    var marked = pre + '<<<<<<< HEAD\n' + ours + '\n=======\n' + theirs + '\n>>>>>>> ' + br + '\n' + post;
    var ta = el('textarea'); ta.style.cssText = MONO + 'width:100%;box-sizing:border-box;min-height:11em;padding:8px;border-radius:8px;border:1px solid var(--border);background:#14181f;color:#d8dde6;font-size:0.88em'; ta.spellcheck = false; root.appendChild(ta);
    var bb = bar(root), p = info(root);
    [['採用 HEAD（目前分支）', function () { return pre + ours + '\n' + post; }], ['採用 ' + br, function () { return pre + theirs + '\n' + post; }], ['兩者都保留', function () { return pre + ours + '\n' + theirs + '\n' + post; }], ['還原成衝突狀態', function () { return marked; }]]
      .forEach(function (o) { var b = btn(o[0]); b.addEventListener('click', function () { ta.value = o[1](); check(false); }); bb.appendChild(b); });
    var bc = btn('✔ 我改好了，檢查'); bc.style.fontWeight = 'bold'; bc.addEventListener('click', function () { check(true); }); bb.appendChild(bc);
    function check(full) { var v = ta.value, bad = /^(<{7}|={7}|>{7})/m.test(v);
      if (bad) { p.innerHTML = '⚠️ 檔案裡還有衝突標記（<code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code>、<code>=======</code>、<code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code>）。把它們刪掉、留下你要的內容。Git 不會阻止你提交含標記的檔案——那會讓程式壞掉。'; return; }
      p.innerHTML = full ? '✅ 沒有衝突標記了。接下來在終端機執行：<br><code>git add ' + esc(cfg.file || 'app.py') + '</code>（標記為已解決）<br><code>git commit</code>（完成合併）<br>最後的檔案內容：<pre style="' + MONO + 'margin:6px 0 0;white-space:pre-wrap">' + esc(v) + '</pre>' : '已套用。可以再手動修改，然後按「檢查」。'; }
    ta.value = marked; p.innerHTML = '這是 <code>git merge ' + esc(br) + '</code> 之後的 <code>' + esc(cfg.file || 'app.py') + '</code>。<code>&lt;&lt;&lt;&lt;&lt;&lt;&lt; HEAD</code> 到 <code>=======</code> 之間是你目前分支的版本，<code>=======</code> 到 <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> 之間是要合併進來的版本。直接在框裡編輯，或用按鈕。';
  }

  /* ---------- 決策樹 ---------- */
  function initTree(root, cfg) {
    head(root, cfg.q); var view = el('div'), path = []; root.appendChild(view);
    function go(id) { path.push(id); draw(); }
    function draw() { var id = path[path.length - 1], n = cfg.nodes[id], h = '';
      if (path.length > 1) h += '<div style="font-size:0.82em;color:var(--text-muted);margin-bottom:6px">' + path.slice(0, -1).map(function (k, i) { var q = cfg.nodes[k]; var lab = q.o.filter(function (o) { return o[1] === path[i + 1]; })[0]; return esc(lab ? lab[0] : ''); }).join(' → ') + '</div>';
      if (n.a) h += '<div style="padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7">' + n.a + '</div>';
      else { h += '<div style="font-weight:bold;margin-bottom:6px">' + n.q + '</div>'; n.o.forEach(function (o) { h += '<button type="button" data-n="' + o[1] + '" style="display:block;width:100%;text-align:left;margin:4px 0;padding:8px 10px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit">' + o[0] + '</button>'; }); }
      if (path.length > 1) h += '<button type="button" data-back="1" style="margin-top:8px;padding:4px 10px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit;font-size:0.88em">← 上一步</button> <button type="button" data-home="1" style="margin-top:8px;padding:4px 10px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit;font-size:0.88em">↺ 從頭</button>';
      view.innerHTML = h;
      view.querySelectorAll('button[data-n]').forEach(function (b) { b.addEventListener('click', function () { go(b.getAttribute('data-n')); }); });
      var bk = view.querySelector('[data-back]'); if (bk) bk.addEventListener('click', function () { path.pop(); draw(); });
      var hm = view.querySelector('[data-home]'); if (hm) hm.addEventListener('click', function () { path = [cfg.start || 'start']; draw(); }); }
    path = [cfg.start || 'start']; draw();
  }

  /* ---------- 指令卡（搜尋＋分類） ---------- */
  function initCards(root, cfg) {
    head(root, cfg.q); var g = 'all', bb = bar(root), s = el('input'), view = el('div', 'display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:8px;margin-top:8px');
    s.type = 'search'; s.placeholder = '搜尋指令或用途…'; s.style.cssText = 'width:100%;box-sizing:border-box;padding:6px 8px;margin-top:6px;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text);font:inherit';
    var ba = btn('全部', 'all'); ba.addEventListener('click', function () { g = 'all'; mark(bb, g); draw(); }); bb.appendChild(ba);
    cfg.groups.forEach(function (x) { var b = btn(x[1], x[0]); b.addEventListener('click', function () { g = x[0]; mark(bb, g); draw(); }); bb.appendChild(b); });
    root.appendChild(s); root.appendChild(view); mark(bb, g); s.addEventListener('input', draw);
    var col = {}; cfg.groups.forEach(function (x) { col[x[0]] = x[2]; });
    function draw() { var q = s.value.trim().toLowerCase(), h = '', n = 0;
      cfg.cards.forEach(function (c) { if (g !== 'all' && c[1] !== g) return; if (q && (c[0] + c[2]).toLowerCase().indexOf(q) < 0) return; n++;
        h += '<div style="padding:8px 10px;border-radius:8px;border:1px solid var(--border);border-top:4px solid ' + col[c[1]] + ';background:var(--surface)"><div style="' + MONO + 'font-weight:bold;font-size:0.88em;word-break:break-all">' + esc(c[0]) + '</div><div style="font-size:0.85em;margin-top:4px;line-height:1.6">' + c[2] + '</div></div>'; });
      view.innerHTML = h || '<div style="color:var(--text-muted)">找不到符合的指令。</div>'; }
    draw();
  }

  /* ---------- 流程步驟 ---------- */
  function initSteps(root, cfg) {
    head(root, cfg.q); var k = 0, row = el('div', 'display:flex;flex-wrap:wrap;gap:6px'), p; root.appendChild(row); p = info(root);
    cfg.steps.forEach(function (s, i) { var b = btn((i + 1) + '. ' + s[0], i); b.addEventListener('click', function () { k = i; draw(); }); row.appendChild(b); });
    var nb = bar(root), pv = btn('← 上一步'), nx = btn('下一步 →'); nb.appendChild(pv); nb.appendChild(nx);
    pv.addEventListener('click', function () { if (k > 0) { k--; draw(); } }); nx.addEventListener('click', function () { if (k < cfg.steps.length - 1) { k++; draw(); } });
    function draw() { mark(row, k); var s = cfg.steps[k]; p.innerHTML = '<b>' + (k + 1) + '. ' + s[0] + '</b>' + (s[2] ? '　<span style="font-size:0.85em;color:var(--text-muted)">' + s[2] + '</span>' : '') + '<br>' + s[1]; }
    draw();
  }

  /* ---------- SHA-1 與 blob 物件 ---------- */
  function sha1(bytes) { var H = [0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0], l = bytes.length, n = ((l + 8) >> 6) + 1, W = new Array(n * 16).fill(0), i;
    for (i = 0; i < l; i++) W[i >> 2] |= bytes[i] << (24 - (i % 4) * 8); W[l >> 2] |= 0x80 << (24 - (l % 4) * 8); W[n * 16 - 1] = l * 8;
    function rol(x, c) { return (x << c) | (x >>> (32 - c)); }
    for (var b = 0; b < W.length; b += 16) { var w = W.slice(b, b + 16), a = H[0], bb = H[1], c = H[2], d = H[3], e = H[4];
      for (i = 16; i < 80; i++) w[i] = rol(w[i - 3] ^ w[i - 8] ^ w[i - 14] ^ w[i - 16], 1);
      for (i = 0; i < 80; i++) { var f, k; if (i < 20) { f = (bb & c) | (~bb & d); k = 0x5A827999; } else if (i < 40) { f = bb ^ c ^ d; k = 0x6ED9EBA1; } else if (i < 60) { f = (bb & c) | (bb & d) | (c & d); k = 0x8F1BBCDC; } else { f = bb ^ c ^ d; k = 0xCA62C1D6; }
        var t = (rol(a, 5) + f + e + k + w[i]) | 0; e = d; d = c; c = rol(bb, 30); bb = a; a = t; }
      H[0] = (H[0] + a) | 0; H[1] = (H[1] + bb) | 0; H[2] = (H[2] + c) | 0; H[3] = (H[3] + d) | 0; H[4] = (H[4] + e) | 0; }
    return H.map(function (x) { return ('00000000' + (x >>> 0).toString(16)).slice(-8); }).join(''); }
  window.__ghSha1 = sha1;
  function initHash(root, cfg) {
    head(root, cfg.q); var ta = el('textarea'); ta.value = cfg.v || '# 我的專案'; ta.spellcheck = false;
    ta.style.cssText = MONO + 'width:100%;box-sizing:border-box;min-height:5em;padding:8px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text)'; root.appendChild(ta);
    var lab = el('label', 'display:block;font-size:0.88em;margin-top:6px'), cb = document.createElement('input'); cb.type = 'checkbox'; cb.checked = true; lab.appendChild(cb); lab.appendChild(document.createTextNode(' 檔案結尾有換行（大多數編輯器會自動加）')); root.appendChild(lab);
    var out = el('div', MONO + 'margin-top:8px;padding:8px 10px;border-radius:8px;background:#14181f;color:#d8dde6;font-size:0.84em;white-space:pre-wrap;word-break:break-all'); root.appendChild(out);
    function draw() { var body = new TextEncoder().encode(ta.value + (cb.checked ? '\n' : '')), hd = new TextEncoder().encode('blob ' + body.length + '\0'), all = new Uint8Array(hd.length + body.length); all.set(hd); all.set(body, hd.length);
      var h = sha1(all); out.innerHTML = 'Git 實際計算雜湊的內容：<span style="color:#ffd479">blob ' + body.length + '\\0</span>' + esc(ta.value).replace(/\n/g, '\\n') + (cb.checked ? '\\n' : '') + '\n\n物件 ID（SHA-1）：<span style="color:#7ee2a8;font-weight:bold">' + h + '</span>\n存放位置：.git/objects/' + h.slice(0, 2) + '/' + h.slice(2) + '\n\n內容改一個字，雜湊就完全不同；內容相同，雜湊一定相同。'; }
    ta.addEventListener('input', draw); cb.addEventListener('change', draw); draw();
  }

  /* ---------- .gitignore 測試器 ---------- */
  function g2re(p) { var r = '', i = 0; while (i < p.length) { var c = p[i];
      if (c === '*' && p[i + 1] === '*') { if (p[i + 2] === '/') { r += '(?:.*/)?'; i += 3; } else { r += '.*'; i += 2; } }
      else if (c === '*') { r += '[^/]*'; i++; } else if (c === '?') { r += '[^/]'; i++; }
      else if (c === '[') { var j = p.indexOf(']', i + 1); if (j < 0) { r += '\\['; i++; } else { r += '[' + p.slice(i + 1, j).replace(/^!/, '^').replace(/\\/g, '\\\\') + ']'; i = j + 1; } }
      else if (c === '\\' && i + 1 < p.length) { r += p[i + 1].replace(/[.*+?^${}()|[\]\\\/]/g, '\\$&'); i += 2; }
      else { r += c.replace(/[.*+?^${}()|[\]\\\/]/g, '\\$&'); i++; } }
    return new RegExp('^' + r + '$'); }
  function parseIgn(txt) { var R = []; txt.split('\n').forEach(function (line, k) { var s = line.replace(/\r$/, ''); if (!s.trim() || s[0] === '#') return; s = s.replace(/(^|[^\\])\s+$/, '$1');
      var neg = false; if (s[0] === '!') { neg = true; s = s.slice(1); } else if (s[0] === '\\') s = s.slice(1);
      var dir = false; if (s.length > 1 && s[s.length - 1] === '/') { dir = true; s = s.slice(0, -1); }
      var anch = s.indexOf('/') >= 0; if (s[0] === '/') s = s.slice(1);
      R.push({ re: g2re(s), neg: neg, dir: dir, anch: anch, line: k + 1, src: line.trim() }); }); return R; }
  function ignored(R, path) { var isDir = /\/$/.test(path); path = path.replace(/\/$/, ''); var parts = path.split('/');
    for (var lv = 1; lv <= parts.length; lv++) { var pre = parts.slice(0, lv).join('/'), dirHere = lv < parts.length || isDir, base = parts[lv - 1], hit = null;
      R.forEach(function (r) { if (r.dir && !dirHere) return; if ((r.anch ? r.re.test(pre) : r.re.test(base))) hit = r; });
      if (lv < parts.length) { if (hit && !hit.neg) return { ig: true, r: hit, via: pre + '/' }; }
      else return hit ? { ig: !hit.neg, r: hit } : { ig: false, r: null }; }
    return { ig: false, r: null }; }
  window.__ghIgnore = function (pat, path) { var r = ignored(parseIgn(pat), path); return r.ig ? (r.r ? r.r.line : 0) : -(r.r ? r.r.line : 0); };
  function initIgnore(root, cfg) {
    head(root, cfg.q);
    var grid = el('div', 'display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:8px'); root.appendChild(grid);
    function box(t, v) { var d = el('div'), l = el('div', 'font-size:0.88em;font-weight:bold;margin-bottom:4px', t), ta = el('textarea'); ta.value = v; ta.spellcheck = false;
      ta.style.cssText = MONO + 'width:100%;box-sizing:border-box;min-height:9em;padding:8px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);font-size:0.85em'; d.appendChild(l); d.appendChild(ta); grid.appendChild(d); return ta; }
    var a = box('.gitignore 的內容', cfg.pat || 'build/\n*.log\n!important.log\n.env\n/config.local\nnode_modules/\n**/tmp/'), b = box('專案中的檔案路徑（一行一個）', cfg.paths || 'app.py\nbuild/out.bin\nlogs/debug.log\nlogs/important.log\n.env\nsrc/.env\nconfig.local\nsrc/config.local\nnode_modules/react/index.js\nsrc/tmp/cache.txt');
    var out = el('div', 'margin-top:8px'); root.appendChild(out);
    function draw() { var R = parseIgn(a.value), h = '<table style="width:100%;border-collapse:collapse;font-size:0.86em">';
      b.value.split('\n').filter(function (x) { return x.trim(); }).forEach(function (pth) { var r = ignored(R, pth.trim());
        h += '<tr style="border-bottom:1px solid var(--border)"><td style="padding:4px 6px;' + MONO + 'word-break:break-all">' + esc(pth.trim()) + '</td><td style="padding:4px 6px;white-space:nowrap;color:' + (r.ig ? '#d0564f' : '#2e8b57') + ';font-weight:bold">' + (r.ig ? '忽略' : '追蹤') + '</td><td style="padding:4px 6px;color:var(--text-muted)">' +
          (r.r ? '第 ' + r.r.line + ' 行 <code>' + esc(r.r.src) + '</code>' + (r.via ? '（整個 ' + esc(r.via) + ' 被忽略）' : '') : '沒有規則符合') + '</td></tr>'; });
      out.innerHTML = h + '</table><div style="font-size:0.82em;color:var(--text-muted);margin-top:6px">規則由上往下看，<b>最後一條符合的規則</b>決定結果；<code>!</code> 開頭是「不要忽略」，但如果上層資料夾已經被忽略，裡面的檔案就救不回來。</div>'; }
    a.addEventListener('input', draw); b.addEventListener('input', draw); draw();
  }

  function initAll() { document.querySelectorAll('.gh-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ areas: initAreas, reset: initReset, graph: initGraph, conflict: initConflict, tree: initTree, cards: initCards, steps: initSteps, hash: initHash, ignore: initIgnore })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def ghw(cfg, maxw=720):
    return wdg("gh-w", cfg, maxw)


_lesson = make_lesson(u"🐙", GH_NOTE, GHLIB, "gh-w")


def lesson(*a, **k):
    """本課程沒有數學公式；GHLIB 的正規表示式會讓 make_lesson 誤載 KaTeX，這裡拿掉。"""
    L = _lesson(*a, **k)
    L.body = [b for b in L.body if not (isinstance(b, tuple) and b[0] == "raw" and b[1] == KATEX)]
    return L
