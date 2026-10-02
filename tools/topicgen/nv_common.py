# -*- coding: utf-8 -*-
"""小說／奇幻與科幻主題共用的互動元件（NVLIB）：關係圖、時間軸、閱讀順序、角色卡、地圖。"""
from cc_common import *
from qt_common import BASEJS

NV_NOTE = u"本課程包含完整劇情（有暴雷）。人名、地名以台灣通行譯本為主，括號附原文；引文皆為簡短摘引並附出處。"

NVLIB = r"""
(function () {
  if (window.__nvLib) return; window.__nvLib = 1;
""" + BASEJS + r"""
  function esc(s) { return String(s); }
  function wrapText(s, max) { var out = [], cur = ''; for (var i = 0; i < s.length; i++) { cur += s[i]; if (cur.length >= max) { out.push(cur); cur = ''; } } if (cur) out.push(cur); return out; }
  function infoBox() { return el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);min-height:2.6em;line-height:1.6'); }

  /* ---------- 關係圖 ---------- */
  function initGraph(root, cfg) {
    head(root, cfg.q); var H = cfg.h || 360, view = el('div'), info = infoBox(), sel = null; root.appendChild(view); root.appendChild(info);
    var N = {}; cfg.nodes.forEach(function (n) { N[n.id] = n; });
    function draw() { var o = '';
      cfg.edges.forEach(function (e) { var a = N[e[0]], b = N[e[1]], on = sel && (e[0] === sel || e[1] === sel), dim = sel && !on;
        o += ln(a.x, a.y, b.x, b.y, e[3] || '#999', on ? 2.6 : 1.4, (e[4] ? 'stroke-dasharray="5 4" ' : '') + 'opacity="' + (dim ? 0.15 : 0.85) + '"');
        if (e[2] && !dim) { var mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2; o += '<rect x="' + n1(mx - e[2].length * 5.2 - 3) + '" y="' + n1(my - 8) + '" width="' + n1(e[2].length * 10.4 + 6) + '" height="15" rx="3" fill="var(--surface)" opacity="0.92"/>' + tx(mx, my + 3.5, e[2], 9.5, e[3] || 'var(--text-muted)'); } });
      cfg.nodes.forEach(function (n) { var w = Math.max(54, n.label.length * 13 + 16), dim = sel && sel !== n.id && !cfg.edges.some(function (e) { return (e[0] === sel && e[1] === n.id) || (e[1] === sel && e[0] === n.id); });
        o += '<g data-id="' + n.id + '" style="cursor:pointer" opacity="' + (dim ? 0.3 : 1) + '"><rect x="' + n1(n.x - w / 2) + '" y="' + n1(n.y - 14) + '" width="' + n1(w) + '" height="28" rx="14" fill="' + (sel === n.id ? n.c : 'var(--surface)') + '" stroke="' + n.c + '" stroke-width="2"/>' +
          tx(n.x, n.y + 4.5, n.label, 12.5, sel === n.id ? '#fff' : n.c) + '</g>'; });
      view.innerHTML = svgw('0 0 640 ' + H, o);
      view.querySelectorAll('g[data-id]').forEach(function (g) { g.addEventListener('click', function () { var id = g.getAttribute('data-id'); sel = sel === id ? null : id; draw(); show(); }); }); }
    function show() { if (!sel) { info.innerHTML = cfg.hint || '點選任一節點，查看說明並突顯它的關係。'; return; } var n = N[sel], rel = [];
      cfg.edges.forEach(function (e) { if (e[0] === sel && e[2]) rel.push(N[e[1]].label + '（' + e[2] + '）'); else if (e[1] === sel && e[2]) rel.push(N[e[0]].label + '（' + e[2] + '）'); });
      info.innerHTML = '<b style="color:' + n.c + '">' + n.label + (n.en ? ' <span style="font-weight:normal;color:var(--text-muted);font-size:0.9em">' + n.en + '</span>' : '') + '</b>：' + n.d + (rel.length ? '<br><span style="font-size:0.9em;color:var(--text-muted)">關係：' + rel.join('、') + '</span>' : ''); }
    draw(); show();
  }

  /* ---------- 時間軸 ---------- */
  function initTimeline(root, cfg) {
    head(root, cfg.q); var bar = el('div'), list = el('div', 'margin-top:6px;max-height:' + (cfg.mh || 460) + 'px;overflow-y:auto;border:1px solid var(--border);border-radius:8px'), g = 'all'; root.appendChild(bar); root.appendChild(list);
    var groups = cfg.groups || [];
    if (groups.length) { var b0 = btn('全部', 'all'); b0.addEventListener('click', function () { g = 'all'; mark(bar, g); draw(); }); bar.appendChild(b0);
      groups.forEach(function (q) { var b = btn(q[1], q[0]); b.addEventListener('click', function () { g = q[0]; mark(bar, g); draw(); }); bar.appendChild(b); }); mark(bar, 'all'); }
    function col(k) { for (var i = 0; i < groups.length; i++) if (groups[i][0] === k) return groups[i][2]; return '#3a6ea5'; }
    function draw() { list.innerHTML = ''; cfg.ev.forEach(function (e) { if (g !== 'all' && e.g !== g) return; var r = el('div', 'display:flex;gap:10px;padding:8px 10px;border-bottom:1px solid var(--border);cursor:pointer'),
        y = el('div', 'flex:0 0 ' + (cfg.yw || 84) + 'px;font-weight:bold;color:' + col(e.g) + ';font-size:0.9em', e.y), body = el('div', 'flex:1'), t = el('div', '', e.t), d = el('div', 'display:none;margin-top:4px;font-size:0.92em;color:var(--text-muted);line-height:1.6', e.d);
        body.appendChild(t); body.appendChild(d); r.appendChild(y); r.appendChild(body); list.appendChild(r);
        r.addEventListener('click', function () { d.style.display = d.style.display === 'none' ? 'block' : 'none'; }); }); }
    draw(); var p = el('p', 'margin:6px 0 0;font-size:0.85em;color:var(--text-muted)', '點一下任一列可展開說明。'); root.appendChild(p);
  }

  /* ---------- 閱讀順序 ---------- */
  function initOrder(root, cfg) {
    head(root, cfg.q); var bar = el('div'), list = el('div', 'margin-top:8px'), info = el('p', 'margin:6px 0 0;font-size:0.92em'), keys = Object.keys(cfg.orders); root.appendChild(bar); root.appendChild(list); root.appendChild(info);
    keys.forEach(function (k, i) { var b = btn(k, i); b.addEventListener('click', function () { mark(bar, i); draw(k); }); bar.appendChild(b); });
    function draw(k) { list.innerHTML = ''; cfg.orders[k].forEach(function (t, i) { var b = cfg.books[t] || {}, r = el('div', 'display:flex;gap:10px;align-items:flex-start;padding:7px 10px;margin:4px 0;border-radius:8px;border:1px solid var(--border);border-left:5px solid ' + (b.c || '#3a6ea5'));
        r.appendChild(el('div', 'flex:0 0 26px;font-weight:bold;font-size:1.1em;color:' + (b.c || '#3a6ea5'), String(i + 1)));
        r.appendChild(el('div', 'flex:1', '<b>' + t + '</b>' + (b.y ? ' <span style="color:var(--text-muted);font-size:0.88em">（' + b.y + '）</span>' : '') + (b.d ? '<div style="font-size:0.9em;color:var(--text-muted);margin-top:2px">' + b.d + '</div>' : '')));
        list.appendChild(r); }); info.innerHTML = (cfg.notes || {})[k] || ''; }
    mark(bar, 0); draw(keys[0]);
  }

  /* ---------- 角色卡 ---------- */
  function initCards(root, cfg) {
    head(root, cfg.q); var bar = el('div'), search = el('input', 'width:100%;box-sizing:border-box;margin-top:6px;padding:6px 10px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);font:inherit'),
      grid = el('div', 'display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:8px;margin-top:8px'), g = 'all', groups = cfg.groups || [];
    search.placeholder = '搜尋名字或關鍵字…'; root.appendChild(bar); root.appendChild(search); root.appendChild(grid);
    var b0 = btn('全部', 'all'); b0.addEventListener('click', function () { g = 'all'; mark(bar, g); draw(); }); bar.appendChild(b0);
    groups.forEach(function (q) { var b = btn(q[1], q[0]); b.addEventListener('click', function () { g = q[0]; mark(bar, g); draw(); }); bar.appendChild(b); }); mark(bar, 'all');
    search.addEventListener('input', draw);
    function col(k) { for (var i = 0; i < groups.length; i++) if (groups[i][0] === k) return groups[i][2]; return '#3a6ea5'; }
    function draw() { var s = search.value.trim(); grid.innerHTML = ''; var n = 0; cfg.cards.forEach(function (c) { if (g !== 'all' && c.g !== g) return; if (s && (c.n + (c.en || '') + c.d).indexOf(s) < 0) return; n++;
        grid.appendChild(el('div', 'padding:8px 10px;border-radius:8px;border:1px solid var(--border);border-top:4px solid ' + col(c.g) + ';font-size:0.9em;line-height:1.55',
          '<b style="font-size:1.05em">' + c.n + '</b>' + (c.en ? '<div style="color:var(--text-muted);font-size:0.85em">' + c.en + '</div>' : '') + '<div style="margin-top:4px">' + c.d + '</div>')); });
      if (!n) grid.appendChild(el('div', 'color:var(--text-muted)', '找不到符合的角色。')); }
    draw();
  }

  /* ---------- 地圖 ---------- */
  function initMap(root, cfg) {
    head(root, cfg.q); var H = cfg.h || 400, view = el('div'), info = infoBox(), sel = -1; root.appendChild(view); root.appendChild(info);
    function draw() { var o = cfg.bg || ''; cfg.pts.forEach(function (p, i) { var on = i === sel;
        o += '<g data-i="' + i + '" style="cursor:pointer"><circle cx="' + p.x + '" cy="' + p.y + '" r="' + (on ? 8 : 6) + '" fill="' + (p.c || '#e0605a') + '" stroke="#fff" stroke-width="1.5"/>' +
          tx(p.x + (p.a === 'end' ? -10 : p.a === 'middle' ? 0 : 10), p.y + (p.a === 'middle' ? -11 : 4), p.n, on ? 12 : 11, on ? (p.c || '#e0605a') : 'var(--text)', p.a || 'start') + '</g>'; });
      view.innerHTML = svgw('0 0 640 ' + H, o);
      view.querySelectorAll('g[data-i]').forEach(function (g) { g.addEventListener('click', function () { sel = +g.getAttribute('data-i'); draw(); var p = cfg.pts[sel]; info.innerHTML = '<b style="color:' + (p.c || '#e0605a') + '">' + p.n + (p.en ? ' <span style="font-weight:normal;color:var(--text-muted);font-size:0.9em">' + p.en + '</span>' : '') + '</b>：' + p.d; }); }); }
    draw(); info.innerHTML = cfg.hint || '點選地圖上的地點查看說明。（示意圖，非精確比例）';
  }


  /* ---------- 心理史學：人越多越好預測 ---------- */
  function initCrowd(root, cfg) {
    head(root, cfg.q); var N = 10, view = el('div'), bar = el('div'), info = el('p', 'margin:6px 0 0'); root.appendChild(view); root.appendChild(bar);
    var b = btn('🎲 重跑 12 個平行宇宙', 'go'); b.addEventListener('click', draw); bar.appendChild(b);
    var u = slider(root, '人口數', 0, 6, 1, 1, function (v) { return Math.round(Math.pow(10, v)).toLocaleString() + ' 人'; }, 'N', function (v) { N = Math.round(Math.pow(10, v)); draw(); }); root.appendChild(info);
    function draw() { var S = [], ends = [], T = 50; for (var r = 0; r < 12; r++) { var d = [], p = 0.5;
        for (var t = 0; t <= T; t++) { var q = 0.3 + 0.4 * t / T, k; if (N <= 2000) { k = 0; for (var i = 0; i < N; i++) if (Math.random() < q) k++; } else { var sd = Math.sqrt(N * q * (1 - q)), u1 = 1 - Math.random(), u2 = Math.random(); k = N * q + sd * Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2); }
          d.push([t, Math.max(0, Math.min(100, 100 * k / N))]); } S.push({ d: d, c: 'rgba(58,110,165,0.55)', w: 1.2 }); ends.push(d[T][1]); }
      S.push({ d: [[0, 30], [T, 70]], c: '#d0564f', n: '心理史學的預測', w: 2.2, dash: '6 4' });
      view.innerHTML = chart(640, 240, S, { x0: 0, x1: T, y0: 0, y1: 100, xl: '時間', yl: '支持某政策的比例（%）' });
      var mn = Math.min.apply(null, ends), mx = Math.max.apply(null, ends);
      info.innerHTML = '每個人都隨機決定支持與否（支持的機率隨時間由 30% 升到 70%）。人口 <b>' + N.toLocaleString() + '</b> 時，12 個平行宇宙的最終結果介於 <b>' + f1(mn) + '%～' + f1(mx) + '%</b>。' +
        (N < 100 ? '人太少，每個宇宙的走向都不一樣，無法預測。' : N < 100000 ? '人越多，曲線越貼近紅線。' : '幾乎完全重合——個人無法預測，群體卻像物理定律一樣精確。這正是謝頓的心理史學想法，也是統計物理的核心。'); }
    u();
  }

  function initAll() { document.querySelectorAll('.nv-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ graph: initGraph, timeline: initTimeline, order: initOrder, cards: initCards, map: initMap, crowd: initCrowd })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def nvw(cfg, maxw=680):
    return wdg("nv-w", cfg, maxw)


def nv_lesson(icon):
    return make_lesson(icon, NV_NOTE, NVLIB, "nv-w")


def node(id_, label, x, y, c, d, en=None):
    n = {"id": id_, "label": label, "x": x, "y": y, "c": c, "d": d}
    if en:
        n["en"] = en
    return n


def card(n, g, d, en=None):
    c = {"n": n, "g": g, "d": d}
    if en:
        c["en"] = en
    return c


def ev(y, t, d, g=None):
    e = {"y": y, "t": t, "d": d}
    if g:
        e["g"] = g
    return e


def pt(x, y, n, d, c=None, en=None, a=None):
    p = {"x": x, "y": y, "n": n, "d": d}
    if c:
        p["c"] = c
    if en:
        p["en"] = en
    if a:
        p["a"] = a
    return p


# 互動元件 JS 中用的實際色碼（CSS 變數無法用在 data-cfg 的節點填色）
CR, CB, CG, CO, CP, CT, CY, CK = "#d0564f", "#3a6ea5", "#4a9a5e", "#d9822b", "#8a5cb8", "#2a9d9d", "#b8941f", "#666"
