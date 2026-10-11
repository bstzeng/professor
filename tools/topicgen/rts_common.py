# -*- coding: utf-8 -*-
"""即時戰略攻略四主題（bw_ 星海一、sc2_ 星海二、wc3_ 魔獸三、aoe_ 世紀帝國）共用：
沿用 NVLIB（時間軸、卡片），另加 RTSLIB——開局播放器（bo）、經濟模擬（eco）、相剋表（counter）、
決策樹（tree）、運營節奏訓練（macro）、魔獸維修費（upkeep）。"""
from nv_common import *
from nv_common import NVLIB

RTSLIB = r"""
(function () {
  if (window.__rtsLib) return; window.__rtsLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function mmss(t) { t = Math.max(0, Math.round(t)); return Math.floor(t / 60) + ':' + ('0' + t % 60).slice(-2); }

  /* ---------- 開局播放器 ---------- */
  function initBo(root, cfg) {
    head(root, cfg.q); var t = 0, k = -1, timer = null, speed = 1;
    var clock = el('div', 'font:bold 1.6em ui-monospace,Menlo,monospace;margin:4px 0'), list = el('div', 'max-height:340px;overflow-y:auto;border:1px solid var(--border);border-radius:8px'), bb = bar(root);
    root.insertBefore(clock, bb); root.appendChild(list);
    var bp = btn('▶ 播放'), bs = btn('⏸ 暫停'), br = btn('↺ 重來'), bn = btn('下一步 →'); [bp, bs, br, bn].forEach(function (b) { bb.appendChild(b); });
    var sb, noSup = cfg.steps.every(function (s) { return !s[1] || String(s[1]) === String(s[0]); }), cw = 3.2;
    if (cfg.mode === 'pop') cfg.steps.forEach(function (s) { var w = 0.6; String(s[0] === null ? '' : s[0]).split('').forEach(function (ch) { w += ch.charCodeAt(0) > 0x2e80 ? 1 : 0.62; }); cw = Math.max(cw, Math.min(6, w)); });
    var p = info(root); p.innerHTML = cfg.note || '按「播放」跟著時間走，或按「下一步」逐步看。時間為遊戲內時間（約略值）。';
    function rows() { list.innerHTML = ''; cfg.steps.forEach(function (s, i) { var on = i === k, done = i < k;
      var r = el('div', 'display:flex;gap:10px;padding:6px 10px;border-bottom:1px solid var(--border);' + (on ? 'background:var(--accent-soft);font-weight:bold' : done ? 'opacity:0.55' : ''),
        '<div style="flex:0 0 ' + cw + 'em' + ';font-family:ui-monospace,Menlo,monospace">' + (s[0] === null ? '' : (cfg.mode === 'pop' ? s[0] : mmss(s[0]))) + '</div>' + (noSup ? '' : '<div style="flex:0 0 3.4em;color:var(--text-muted)">' + (s[1] || '') + '</div>') + '<div style="flex:1;line-height:1.55">' + s[2] + '</div>');
      list.appendChild(r); if (on) r.scrollIntoView({ block: 'nearest' }); }); }
    function sync() { var nk = -1; cfg.steps.forEach(function (s, i) { if (s[0] !== null && (cfg.mode === 'pop' ? false : s[0] <= t)) nk = i; }); if (nk > k) k = nk; draw(); }
    function draw() { clock.textContent = cfg.mode === 'pop' ? ('第 ' + (k + 1) + ' / ' + cfg.steps.length + ' 步') : mmss(t); rows(); }
    function stop() { if (timer) { clearInterval(timer); timer = null; } }
    bp.addEventListener('click', function () { if (cfg.mode === 'pop') { bn.click(); return; } if (timer) return; timer = setInterval(function () { t += speed; sync(); if (t > (cfg.steps[cfg.steps.length - 1][0] || 0) + 10) stop(); }, 1000); });
    bs.addEventListener('click', stop); br.addEventListener('click', function () { stop(); t = 0; k = -1; draw(); });
    bn.addEventListener('click', function () { if (k < cfg.steps.length - 1) { k++; if (cfg.mode !== 'pop' && cfg.steps[k][0] !== null) t = Math.max(t, cfg.steps[k][0]); draw(); } });
    sb = el('span'); var sl = el('span', 'margin-left:8px;font-size:0.85em;color:var(--text-muted)', '速度'); bb.appendChild(sl); bb.appendChild(sb);
    [1, 2, 4].forEach(function (s) { var b = btn(s + '×', 's' + s); b.addEventListener('click', function () { speed = s; mark(sb, 's' + s); }); sb.appendChild(b); }); mark(sb, 's1');
    if (cfg.mode === 'pop') { bp.style.display = 'none'; bs.style.display = 'none'; sb.style.display = 'none'; sl.style.display = 'none'; }
    draw();
  }

  /* ---------- 經濟模擬（持續生產農民 vs 偷懶） ---------- */
  function income(w, c) { var P = c.P, per = w / P, a = Math.min(per, c.k), b = Math.max(0, Math.min(per, c.m) - c.k); return P * (a * c.r1 + b * c.r2) / 60; }
  function sim(c, delay, stopAt) { var res = c.res0, w = c.w0, prog = -1, wait = 0, mined = 0, pts = [[0, 0]], wpts = [[0, w]];
    for (var t = 1; t <= c.T; t++) { var g = income(w, c); res += g; mined += g;
      if (prog >= 0) { prog += 1; if (prog >= c.bt) { w += 1; prog = -1; wait = delay; } }
      else if (wait > 0) wait -= 1;
      else if (w < stopAt && res >= c.cost) { res -= c.cost; prog = 0; }
      if (t % 10 === 0) { pts.push([t / 60, mined]); wpts.push([t / 60, w]); } }
    return { mined: mined, w: w, pts: pts, wpts: wpts }; }
  window.__rtsSim = sim;
  function initEco(root, cfg) {
    head(root, cfg.q); var c = cfg.c, delay = 5, stopAt = c.wmax, out = el('div'), ch = el('div');
    var u1 = slider(root, '每生產一個' + c.wn + '之後，發呆幾秒才生下一個', 0, 30, 1, delay, function (v) { return v + ' 秒'; }, 'd', function (v) { delay = v; draw(); });
    var u2 = slider(root, c.wn + '生到幾個就停止', c.w0, c.wmax, 1, stopAt, function (v) { return v + ' 個'; }, 's', function (v) { stopAt = v; draw(); });
    root.appendChild(out); root.appendChild(ch); var p = info(root); p.innerHTML = cfg.note || ''; u1(); u2();
    function draw() { var a = sim(c, 0, c.wmax), b = sim(c, delay, stopAt);
      out.innerHTML = '<div style="margin-top:6px;line-height:1.7">模擬 ' + mmss(c.T) + '（單一' + c.base + '）：<br>完美運營：' + c.wn + ' <b>' + a.w + '</b> 個，共採集 <b>' + Math.round(a.mined) + '</b> ' + c.unit +
        '<br>你的設定：' + c.wn + ' <b>' + b.w + '</b> 個，共採集 <b>' + Math.round(b.mined) + '</b> ' + c.unit + '（少了 <b style="color:#d0564f">' + Math.round(a.mined - b.mined) + '</b>，約 ' + Math.round((a.mined - b.mined) / Math.max(1, a.mined) * 100) + '%）</div>';
      ch.innerHTML = chart(640, 220, [{ d: a.pts, c: '#4a9a5e', n: '完美運營' }, { d: b.pts, c: '#d0564f', n: '你的設定', dash: '5 4' }], { xl: '遊戲時間（分鐘）', yl: '累積採集', y0: 0 }); }
    draw();
  }

  /* ---------- 相剋表 ---------- */
  function initCounter(root, cfg) {
    head(root, cfg.q); var gb = bar(root), ub = el('div', 'margin-top:6px'), p; root.appendChild(ub); p = info(root); var g = cfg.groups[0][0];
    cfg.groups.forEach(function (x) { var b = btn(x[1], x[0]); b.addEventListener('click', function () { g = x[0]; mark(gb, g); units(); }); gb.appendChild(b); }); mark(gb, g);
    function units() { ub.innerHTML = ''; cfg.units.filter(function (u) { return u[1] === g; }).forEach(function (u) { var b = btn(u[0], u[0]); b.addEventListener('click', function () { mark(ub, u[0]); show(u); }); ub.appendChild(b); }); p.innerHTML = '點一個單位，看它剋制誰、怕誰。'; }
    function show(u) { p.innerHTML = '<b>' + u[0] + '</b>' + (u[4] ? '　<span style="font-size:0.88em;color:var(--text-muted)">' + u[4] + '</span>' : '') + '<br>💪 <b>擅長對付</b>：' + (u[2] || '—') + '<br>⚠️ <b>害怕</b>：' + (u[3] || '—'); }
    units();
  }

  /* ---------- 決策樹 ---------- */
  function initTree(root, cfg) {
    head(root, cfg.q); var view = el('div'), path = ['start']; root.appendChild(view);
    function bs(t, a) { return '<button type="button" ' + a + ' style="display:block;width:100%;text-align:left;margin:4px 0;padding:8px 10px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit">' + t + '</button>'; }
    function draw() { var id = path[path.length - 1], n = cfg.nodes[id], h = '';
      if (path.length > 1) h += '<div style="font-size:0.82em;color:var(--text-muted);margin-bottom:6px">' + path.slice(0, -1).map(function (k, i) { var o = cfg.nodes[k].o.filter(function (o) { return o[1] === path[i + 1]; })[0]; return esc(o ? o[0] : ''); }).join(' → ') + '</div>';
      if (n.a) h += '<div style="padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7">' + n.a + '</div>';
      else { h += '<div style="font-weight:bold;margin-bottom:6px">' + n.q + '</div>'; n.o.forEach(function (o) { h += bs(o[0], 'data-n="' + o[1] + '"'); }); }
      if (path.length > 1) h += '<div style="margin-top:8px"><button type="button" data-back="1">← 上一步</button> <button type="button" data-home="1">↺ 從頭</button></div>';
      view.innerHTML = h;
      view.querySelectorAll('[data-back],[data-home]').forEach(function (b) { b.style.cssText = 'padding:4px 10px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit;font-size:0.88em'; });
      view.querySelectorAll('button[data-n]').forEach(function (b) { b.addEventListener('click', function () { path.push(b.getAttribute('data-n')); draw(); }); });
      var bk = view.querySelector('[data-back]'); if (bk) bk.addEventListener('click', function () { path.pop(); draw(); });
      var hm = view.querySelector('[data-home]'); if (hm) hm.addEventListener('click', function () { path = ['start']; draw(); }); }
    draw();
  }

  /* ---------- 運營節奏訓練 ---------- */
  function initMacro(root, cfg) {
    head(root, cfg.q); var t = 0, timer = null, due = {}, late = [], missed = 0, L = cfg.len || 90;
    var clock = el('div', 'font:bold 1.4em ui-monospace,Menlo,monospace;margin:4px 0'), grid = el('div', 'display:flex;flex-wrap:wrap;gap:8px'), bb = bar(root); root.insertBefore(clock, bb); root.appendChild(grid); var p = info(root);
    var bp = btn('▶ 開始 ' + L + ' 秒挑戰'), br = btn('↺ 重來'); bb.appendChild(bp); bb.appendChild(br);
    var B = cfg.tasks.map(function (x, i) { var b = el('button', 'flex:1 1 140px;padding:14px 8px;border-radius:10px;border:2px solid var(--border);background:var(--surface);color:var(--text);font:inherit;font-weight:bold;cursor:pointer', x[0]);
      b.addEventListener('click', function () { if (!timer) return; if (due[i] !== undefined && due[i] <= t) { late.push(t - due[i]); due[i] = t + x[1]; } paint(); }); grid.appendChild(b); return b; });
    function paint() { clock.textContent = Math.floor(t / 60) + ':' + ('0' + t % 60).slice(-2) + ' / ' + Math.floor(L / 60) + ':' + ('0' + L % 60).slice(-2);
      B.forEach(function (b, i) { var ready = timer && due[i] !== undefined && due[i] <= t; b.style.borderColor = ready ? '#d0564f' : 'var(--border)'; b.style.background = ready ? '#d0564f22' : 'var(--surface)';
        b.innerHTML = cfg.tasks[i][0] + '<div style="font-weight:normal;font-size:0.8em;color:var(--text-muted)">' + (ready ? '現在！已延遲 ' + (t - due[i]) + ' 秒' : timer ? '下一次在 ' + Math.max(0, due[i] - t) + ' 秒後' : '每 ' + cfg.tasks[i][1] + ' 秒') + '</div>'; }); }
    function end() { clearInterval(timer); timer = null; var idle = 0; cfg.tasks.forEach(function (x, i) { if (due[i] <= L) idle += L - due[i]; }); var tot = late.reduce(function (s, v) { return s + v; }, 0) + idle;
      p.innerHTML = '挑戰結束！共完成 ' + late.length + ' 次，平均延遲 <b>' + (late.length ? (late.reduce(function (s, v) { return s + v; }, 0) / late.length).toFixed(1) : '—') + ' 秒</b>，累積浪費 <b>' + tot + ' 秒</b>的生產時間。' + (cfg.tip || '') ; paint(); }
    bp.addEventListener('click', function () { if (timer) return; t = 0; late = []; cfg.tasks.forEach(function (x, i) { due[i] = x[2] || 0; }); timer = setInterval(function () { t += 1; if (t >= L) end(); else paint(); }, 1000); paint(); p.innerHTML = '紅色的按鈕代表「該做了」——盡快按下去！'; });
    br.addEventListener('click', function () { if (timer) clearInterval(timer); timer = null; t = 0; late = []; due = {}; paint(); p.innerHTML = cfg.note || ''; });
    p.innerHTML = cfg.note || ''; paint();
  }

  /* ---------- 魔獸三維修費 ---------- */
  function initUpkeep(root, cfg) {
    head(root, cfg.q); var food = 40, out = el('div'), ch = el('div');
    var u = slider(root, '目前使用的人口', 0, 100, 1, food, function (v) { return v + ' / 100'; }, 'f', function (v) { food = v; draw(); });
    root.appendChild(out); root.appendChild(ch); var p = info(root); p.innerHTML = cfg.note || ''; u();
    function rate(f) { return f <= 50 ? 1 : f <= 80 ? 0.7 : 0.4; }
    function draw() { var r = rate(food), lab = r === 1 ? '無維修費' : r === 0.7 ? '低維修費（Low Upkeep）' : '高維修費（High Upkeep）';
      out.innerHTML = '<div style="margin-top:6px;line-height:1.7">狀態：<b>' + lab + '</b>　採金效率 <b>' + Math.round(r * 100) + '%</b>（每 10 金只收到 ' + (10 * r) + ' 金）<br>木材不受影響。</div>';
      var d = []; for (var f = 0; f <= 100; f++) d.push([f, rate(f) * 100]);
      ch.innerHTML = chart(640, 200, [{ d: d, c: '#d9822b', n: '採金效率 %' }], { xl: '人口', y0: 0, y1: 110, pts: [{ x: food, y: r * 100, c: '#3a6ea5', n: '' }] }); }
    draw();
  }

  function initAll() { document.querySelectorAll('.rts-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ bo: initBo, eco: initEco, counter: initCounter, tree: initTree, macro: initMacro, upkeep: initUpkeep })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def rtsw(cfg, maxw=720):
    return wdg("rts-w", cfg, maxw)


def rts_lesson(icon, note):
    base = make_lesson(icon, note, NVLIB, "nv-w")

    def lesson(*a, **k):
        L = base(*a, **k)
        if any(isinstance(b, tuple) and b[0] == "raw" and 'class="rts-w' in b[1] for b in L.body):
            L.body.insert(0, ("raw", u"<script>%s</script>" % RTSLIB))
        L.body = [b for b in L.body if not (isinstance(b, tuple) and b[0] == "raw" and b[1] == KATEX)]
        return L
    return lesson


def bo(q, steps, mode="time", note=None):
    """開局：steps = [(秒或 None, 人口, 說明)]。"""
    c = {"t": "bo", "q": q, "mode": mode, "steps": [list(s) for s in steps]}
    if note:
        c["note"] = note
    return rtsw(c)


def tree(q, nodes):
    return rtsw({"t": "tree", "q": q, "nodes": nodes})


def counter(q, groups, units):
    return rtsw({"t": "counter", "q": q, "groups": groups, "units": [list(u) for u in units]})


def LORE(tid, name):
    return u'<a href="../%s/index.html">〈%s〉</a>' % (tid, name)
