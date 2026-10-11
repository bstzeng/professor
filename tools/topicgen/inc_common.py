# -*- coding: utf-8 -*-
"""〈開公司〉（inc_）共用工具：互動元件（INCLIB）與 lesson 包裝。"""
from cc_common import *
from qt_common import BASEJS

INC_NOTE = (u"本課程依台灣（中華民國）現行法規撰寫，稅率與金額以 115 年度（2026 年所得、2027 年申報）為準，並於 2026 年 10 月查證；"
            u"法規與數字每年可能調整，內容<strong>僅供學習參考，不構成法律或稅務意見</strong>，實際情況請以全國法規資料庫、財政部公告為準，並諮詢會計師或律師。")

# 綜所稅參數：年度 → (免稅額, 標準扣除額(單身), 薪資特別扣除額, 級距上限, 稅率)
TAXYEAR = {
    "115": [101000, 136000, 227000, [610000, 1380000, 2770000, 5190000], [0.05, 0.12, 0.20, 0.30, 0.40]],
    "114": [97000, 131000, 218000, [590000, 1330000, 2660000, 4980000], [0.05, 0.12, 0.20, 0.30, 0.40]],
}

INCLIB = r"""
(function () {
  if (window.__incLib) return; window.__incLib = 1;
""" + BASEJS + r"""
  var TY = __TY__;
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function money(v) { return Math.round(v).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); }
  function wan(v) { return (Math.round(v / 1000) / 10).toString() + ' 萬'; }

  /* ---------- 稅額計算（與 Python 版 inc_tax.py 對照測試） ---------- */
  function progressive(net, y) { var p = TY[y], lim = p[3], r = p[4], t = 0, lo = 0; if (net <= 0) return 0;
    for (var i = 0; i < r.length; i++) { var hi = i < lim.length ? lim[i] : Infinity; if (net > lo) t += (Math.min(net, hi) - lo) * r[i]; lo = hi; } return t; }
  function pit(sal, other, divComb, y) { var p = TY[y], salNet = Math.max(0, sal - Math.min(sal, p[2])), net = salNet + other + divComb - p[0] - p[1]; return progressive(net, y); }
  function cit(ti) { if (ti <= 120000) return 0; return Math.min(ti * 0.2, (ti - 120000) / 2); }
  function personal(P, y) { return { tax: pit(0, P, 0, y) }; }
  function corp(P, S, ratio, y) {
    S = Math.min(S, P); var ti = P - S, c = cit(ti), after = ti - c, reserve = after * 0.1, D = Math.max(0, (after - reserve) * ratio), U = Math.max(0, after - reserve - D), undist = U * 0.05;
    var base = pit(S, 0, 0, y), comb = pit(S, 0, D, y) - Math.min(D * 0.085, 80000), sep = base + D * 0.28, useSep = sep < comb, ind = useSep ? sep : comb;
    var nhi = D >= 20000 ? Math.min(D, 10000000) * 0.0211 : 0;
    return { ti: ti, cit: c, after: after, D: D, undist: undist, ind: ind, sep: useSep, nhi: nhi, total: c + undist + ind + nhi, keep: after - D - undist, take: S + D - ind - nhi };
  }
  window.__incTax = { pit: pit, cit: cit, corp: corp, personal: personal };

  function initCalc(root, cfg) {
    head(root, cfg.q); var y = '115', P = cfg.P || 3000000, S = cfg.S || 600000, R = cfg.R === undefined ? 1 : cfg.R, out = el('div'), ch = el('div'), yb = bar(root);
    ['115', '114'].forEach(function (k) { var b = btn(k + ' 年度', k); b.addEventListener('click', function () { y = k; mark(yb, k); draw(); }); yb.appendChild(b); }); mark(yb, y);
    var u1 = slider(root, '一年的淨利（收入扣除成本費用，尚未付老闆薪水）', 300000, 10000000, 100000, P, function (v) { return money(v) + ' 元'; }, 'P', function (v) { P = v; if (S > P) S = P; draw(); });
    var u2 = slider(root, '公司付給你（老闆）的年薪', 0, 6000000, 50000, S, function (v) { return money(v) + ' 元'; }, 'S', function (v) { S = v; draw(); });
    var u3 = slider(root, '稅後盈餘發成股利的比例', 0, 1, 0.05, R, function (v) { return Math.round(v * 100) + '%'; }, 'R', function (v) { R = v; draw(); });
    root.appendChild(out); root.appendChild(ch); var p = info(root);
    u1(); u2(); u3();
    p.innerHTML = '簡化假設：單身、無扶養、只有這份所得、用標準扣除額；公司方案未計勞健保、營業稅、雇主補充保費與基本稅額，薪水也必須是「合理」的金額。<b>只用來理解結構，不能當報稅依據。</b>';
    function draw() { var a = personal(P, y), c = corp(P, S, R, y);
      var h = '<table style="width:100%;border-collapse:collapse;font-size:0.88em;margin-top:8px"><tr><th style="text-align:left;padding:4px">項目</th><th style="text-align:right;padding:4px">個人／行號</th><th style="text-align:right;padding:4px">有限公司</th></tr>';
      function row(n, a1, b1, bold) { h += '<tr style="border-top:1px solid var(--border)' + (bold ? ';font-weight:bold' : '') + '"><td style="padding:4px;text-align:left">' + n + '</td><td style="text-align:right;padding:4px">' + a1 + '</td><td style="text-align:right;padding:4px">' + b1 + '</td></tr>'; }
      row('營利事業所得稅', '—（行號免繳，併入個人）', money(c.cit)); row('未分配盈餘加徵 5%', '—', money(c.undist));
      row('你的綜合所得稅', money(a.tax), money(c.ind) + (c.D > 0 ? '（股利' + (c.sep ? '分開 28%' : '合併計稅') + '）' : ''));
      row('股利補充保費 2.11%', '—', money(c.nhi)); row('稅費合計', money(a.tax), money(c.total), true);
      row('實際進到你口袋', money(P - a.tax), money(c.take), true); row('留在公司的錢', '—', money(c.keep));
      out.innerHTML = h + '</table>';
      var pts = [], best = null; for (var s = 0; s <= P; s += Math.max(50000, Math.round(P / 60 / 50000) * 50000)) { var t = corp(P, s, R, y).total; pts.push([s / 10000, t / 10000]); if (!best || t < best[1]) best = [s, t]; }
      ch.innerHTML = chart(640, 220, [{ d: pts, c: '#3a6ea5', n: '公司方案稅費合計（萬元）' }, { d: [[0, a.tax / 10000], [P / 10000, a.tax / 10000]], c: '#d0564f', n: '個人（萬元）', dash: '5 4' }],
        { xl: '老闆年薪（萬元）', y0: 0, pts: [{ x: S / 10000, y: c.total / 10000, c: '#2e8b57', n: '目前' }] }) +
        '<div style="font-size:0.85em;color:var(--text-muted)">在這個股利比例下，稅費最低的年薪約 ' + wan(best[0]) + '，合計約 ' + wan(best[1]) + '。注意：「留在公司的錢」未來發出來時還要再繳稅。</div>'; }
    draw();
  }

  /* ---------- 紅線判斷測驗 ---------- */
  function initQuiz(root, cfg) {
    head(root, cfg.q); var k = 0, score = 0, done = {}, box = el('div'), p; root.appendChild(box); p = info(root); var nb = bar(root);
    var pv = btn('← 上一題'), nx = btn('下一題 →'); nb.appendChild(pv); nb.appendChild(nx);
    pv.addEventListener('click', function () { if (k > 0) { k--; draw(); } }); nx.addEventListener('click', function () { if (k < cfg.items.length - 1) { k++; draw(); } });
    var L = { ok: '✅ 可以', no: '⛔ 不行', dep: '⚠️ 看情況' };
    function draw() { var it = cfg.items[k], h = '<div style="font-size:0.85em;color:var(--text-muted)">第 ' + (k + 1) + ' / ' + cfg.items.length + ' 題　答對 ' + score + ' 題</div><div style="margin:6px 0 8px;font-weight:bold;line-height:1.7">' + it[0] + '</div>';
      ['ok', 'no', 'dep'].forEach(function (a) { h += '<button type="button" data-a="' + a + '" style="margin:4px 6px 0 0;padding:6px 12px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit">' + L[a] + '</button>'; });
      box.innerHTML = h; p.innerHTML = done[k] ? done[k] : '先想一想，再選一個答案。';
      box.querySelectorAll('button[data-a]').forEach(function (b) { b.addEventListener('click', function () { var a = b.getAttribute('data-a'), right = a === it[1];
        if (!done[k] && right) score++; done[k] = (right ? '<b>答對了！</b>' : '<b>正確答案是：' + L[it[1]] + '</b>') + '<br>' + it[2]; draw(); }); }); }
    draw();
  }

  /* ---------- 勾選清單（記住進度） ---------- */
  function initCheck(root, cfg) {
    head(root, cfg.q); var key = 'inc-check-' + cfg.id, st = {}; try { st = JSON.parse(localStorage.getItem(key) || '{}'); } catch (e) { st = {}; }
    var prog = el('div', 'font-size:0.88em;margin-bottom:6px'), list = el('div'); root.appendChild(prog); root.appendChild(list); var n = 0;
    cfg.groups.forEach(function (g, gi) { list.appendChild(el('div', 'font-weight:bold;margin:10px 0 4px', esc(g[0])));
      g[1].forEach(function (it, ii) { var id = gi + '-' + ii, lab = el('label', 'display:flex;gap:8px;align-items:flex-start;padding:5px 8px;margin:3px 0;border-radius:8px;border:1px solid var(--border);background:var(--surface);cursor:pointer;line-height:1.6'), c = document.createElement('input'); n++;
        c.type = 'checkbox'; c.checked = !!st[id]; c.style.marginTop = '5px'; lab.appendChild(c); lab.appendChild(el('span', '', it)); list.appendChild(lab);
        c.addEventListener('change', function () { st[id] = c.checked; try { localStorage.setItem(key, JSON.stringify(st)); } catch (e) {} upd(); }); }); });
    var rb = btn('全部清除'); rb.addEventListener('click', function () { st = {}; try { localStorage.removeItem(key); } catch (e) {} list.querySelectorAll('input').forEach(function (c) { c.checked = false; }); upd(); }); root.appendChild(rb);
    function upd() { var m = list.querySelectorAll('input:checked').length; prog.innerHTML = '完成 <b>' + m + ' / ' + n + '</b>' + (m === n ? '　🎉 全部完成！' : ''); }
    upd();
  }

  /* ---------- 年度行事曆 ---------- */
  function initCal(root, cfg) {
    head(root, cfg.q); var bb = el('div', 'display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:4px'), p; root.appendChild(bb); p = info(root); var m = cfg.m || 1;
    for (var i = 1; i <= 12; i++) (function (i) { var b = btn(i + ' 月', i); b.style.margin = '0'; b.addEventListener('click', function () { m = i; draw(); }); bb.appendChild(b); })(i);
    function draw() { mark(bb, m); var h = '<b>' + m + ' 月要注意的事</b><ul style="margin:6px 0 0;padding-left:1.3em">';
      cfg.ev.forEach(function (e) { if (e[0].indexOf(m) >= 0) h += '<li>' + e[1] + '</li>'; }); p.innerHTML = h + '</ul>'; }
    draw();
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

  /* ---------- 流程步驟 ---------- */
  function initSteps(root, cfg) {
    head(root, cfg.q); var k = 0, row = el('div', 'display:flex;flex-wrap:wrap;gap:6px'), p; root.appendChild(row); p = info(root);
    cfg.steps.forEach(function (s, i) { var b = btn((i + 1) + '. ' + s[0], i); b.addEventListener('click', function () { k = i; draw(); }); row.appendChild(b); });
    var nb = bar(root), pv = btn('← 上一步'), nx = btn('下一步 →'); nb.appendChild(pv); nb.appendChild(nx);
    pv.addEventListener('click', function () { if (k > 0) { k--; draw(); } }); nx.addEventListener('click', function () { if (k < cfg.steps.length - 1) { k++; draw(); } });
    function draw() { mark(row, k); var s = cfg.steps[k]; p.innerHTML = '<b>' + (k + 1) + '. ' + s[0] + '</b>' + (s[2] ? '　<span style="font-size:0.85em;color:var(--text-muted)">' + s[2] + '</span>' : '') + '<br>' + s[1]; }
    draw();
  }

  /* ---------- 組織型態比較（點選欄位） ---------- */
  function initCompare(root, cfg) {
    head(root, cfg.q); var bb = bar(root), view = el('div'); root.appendChild(view); var sel = cfg.cols.map(function (c, i) { return i < 3; });
    cfg.cols.forEach(function (c, i) { var b = btn(c); b.addEventListener('click', function () { sel[i] = !sel[i]; if (!sel.some(Boolean)) sel[i] = true; draw(); }); bb.appendChild(b); });
    function draw() { bb.querySelectorAll('button').forEach(function (b, i) { b.style.background = sel[i] ? 'var(--accent-soft)' : 'var(--surface)'; b.style.fontWeight = sel[i] ? 'bold' : 'normal'; });
      var h = '<div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:0.86em;margin-top:8px"><tr><th style="text-align:left;padding:5px;min-width:5em"></th>';
      cfg.cols.forEach(function (c, i) { if (sel[i]) h += '<th style="text-align:left;padding:5px">' + esc(c) + '</th>'; }); h += '</tr>';
      cfg.rows.forEach(function (r) { h += '<tr style="border-top:1px solid var(--border)"><td style="padding:5px;font-weight:bold;vertical-align:top;text-align:left">' + r[0] + '</td>'; r.slice(1).forEach(function (v, i) { if (sel[i]) h += '<td style="padding:5px;vertical-align:top;line-height:1.6;text-align:left">' + v + '</td>'; }); h += '</tr>'; });
      view.innerHTML = h + '</table></div><div style="font-size:0.82em;color:var(--text-muted);margin-top:4px">點上方按鈕選擇要比較的型態（可多選）。</div>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.inc-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ calc: initCalc, quiz: initQuiz, check: initCheck, cal: initCal, tree: initTree, steps: initSteps, compare: initCompare })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
""".replace("__TY__", __import__("json").dumps(TAXYEAR))


def incw(cfg, maxw=720):
    return wdg("inc-w", cfg, maxw)


_lesson = make_lesson(u"🏢", INC_NOTE, INCLIB, "inc-w")


def lesson(*a, **k):
    L = _lesson(*a, **k)
    L.body = [b for b in L.body if not (isinstance(b, tuple) and b[0] == "raw" and b[1] == KATEX)]
    return L


def LAW(name, art, text=None):
    """法條引用（純文字標示）。"""
    return u'<span style="white-space:nowrap">〈%s〉第 %s 條</span>' % (name, art) + (u"：" + text if text else u"")


# ---------- Python 對照版（測試用） ----------
def py_progressive(net, y):
    lim, r = TAXYEAR[y][3], TAXYEAR[y][4]
    t, lo = 0.0, 0
    if net <= 0:
        return 0.0
    for i, rate in enumerate(r):
        hi = lim[i] if i < len(lim) else float("inf")
        if net > lo:
            t += (min(net, hi) - lo) * rate
        lo = hi
    return t


def py_cit(ti):
    return 0 if ti <= 120000 else min(ti * 0.2, (ti - 120000) / 2.0)
