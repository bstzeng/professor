# -*- coding: utf-8 -*-
"""遊戲劇情主題（仙劍 pj_、軒轅劍 xy_）共用：沿用 NVLIB（時間軸、關係圖、角色卡、地圖），
另加 GMLIB——結局對照（ending）與前世今生鏈（chain）；並提供神州、歐亞示意地圖底圖。"""
from nv_common import *
from nv_common import NVLIB

GMLIB = r"""
(function () {
  if (window.__gmLib) return; window.__gmLib = 1;
""" + BASEJS + r"""
  var TAGS = { d: ['犧牲／死亡', '#d0564f', '✝'], l: ['存活', '#4a9a5e', '●'], r: ['轉世／重生', '#8a5cb8', '↻'], s: ['封印／囚禁', '#3a6ea5', '⛓'], p: ['分離', '#d9822b', '◐'] };
  function initEnding(root, cfg) {
    head(root, cfg.q); var bar = el('div'), f = el('div', 'margin-top:4px'), box = el('div', 'margin-top:8px'), sum = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.65'), gi = 0, ft = 'all';
    root.appendChild(bar); root.appendChild(f); root.appendChild(box); root.appendChild(sum);
    cfg.games.forEach(function (g, i) { var b = btn(g.n, i); b.addEventListener('click', function () { gi = i; mark(bar, i); draw(); }); bar.appendChild(b); });
    var b0 = btn('全部', 'all'); b0.addEventListener('click', function () { ft = 'all'; mark(f, 'all'); draw(); }); f.appendChild(b0);
    Object.keys(TAGS).forEach(function (k) { var b = btn(TAGS[k][2] + ' ' + TAGS[k][0], k); b.addEventListener('click', function () { ft = k; mark(f, k); draw(); }); f.appendChild(b); });
    mark(bar, 0); mark(f, 'all');
    function draw() { var g = cfg.games[gi]; box.innerHTML = ''; var n = 0;
      g.rows.forEach(function (r) { if (ft !== 'all' && r[1] !== ft) return; n++; var t = TAGS[r[1]];
        box.appendChild(el('div', 'display:flex;gap:10px;align-items:flex-start;padding:7px 10px;margin:4px 0;border-radius:8px;border:1px solid var(--border);border-left:5px solid ' + t[1],
          '<div style="flex:0 0 7.5em;font-weight:bold">' + r[0] + '<div style="font-weight:normal;font-size:0.82em;color:' + t[1] + '">' + t[2] + ' ' + t[0] + '</div></div><div style="flex:1;line-height:1.6">' + r[2] + '</div>')); });
      if (!n) box.appendChild(el('div', 'color:var(--text-muted);padding:6px', '這一代沒有這類結局的角色。'));
      var c = {}; cfg.games.forEach(function (gg) { gg.rows.forEach(function (r) { c[r[1]] = (c[r[1]] || 0) + 1; }); });
      sum.innerHTML = (g.note ? '<b>' + g.n + '</b>：' + g.note + '<br>' : '') + '<span style="font-size:0.9em;color:var(--text-muted)">全系列統計（本表收錄的主要角色）：' +
        Object.keys(TAGS).map(function (k) { return TAGS[k][0] + ' ' + (c[k] || 0); }).join('、') + '。</span>'; }
    draw();
  }

  function initChain(root, cfg) {
    head(root, cfg.q); var wrap = el('div'), info = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);min-height:2.6em;line-height:1.65'); root.appendChild(wrap); root.appendChild(info);
    cfg.chains.forEach(function (ch, ci) { var row = el('div', 'margin:8px 0'), title = el('div', 'font-weight:bold;margin-bottom:4px;color:' + ch.c, ch.n), line = el('div', 'display:flex;flex-wrap:wrap;align-items:center;gap:4px');
      ch.s.forEach(function (s, si) { if (si) line.appendChild(el('span', 'color:var(--text-muted);font-size:1.1em', s[3] || '→'));
        var b = el('button', 'border:2px solid ' + ch.c + ';background:var(--surface);color:var(--text);border-radius:10px;padding:4px 10px;cursor:pointer;font:inherit;font-size:0.92em;line-height:1.35;text-align:center',
          '<b>' + s[0] + '</b><div style="font-size:0.8em;color:var(--text-muted)">' + s[1] + '</div>');
        b.addEventListener('click', function () { wrap.querySelectorAll('button').forEach(function (x) { x.style.background = 'var(--surface)'; x.style.color = 'var(--text)'; }); b.style.background = ch.c; b.style.color = '#fff';
          info.innerHTML = '<b style="color:' + ch.c + '">' + s[0] + '</b>（' + s[1] + '）：' + s[2]; });
        line.appendChild(b); });
      row.appendChild(title); row.appendChild(line); wrap.appendChild(row); });
    info.innerHTML = cfg.hint || '點選任一個名字，看這一世的故事。';
  }

  function initAll() { document.querySelectorAll('.gm-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ ending: initEnding, chain: initChain })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def gmw(cfg, maxw=700):
    return wdg("gm-w", cfg, maxw)


def gm_lesson(icon, note):
    base = make_lesson(icon, note, NVLIB, "nv-w")

    def lesson(*a, **k):
        L = base(*a, **k)
        if any(isinstance(b, tuple) and b[0] == "raw" and 'class="gm-w' in b[1] for b in L.body):
            L.body.insert(0, ("raw", u"<script>%s</script>" % GMLIB))
        return L
    return lesson


# ---------- 神州示意底圖（經度 80～130、緯度 18～50；x = 20 + (經度−80)×12，y = 20 + (50−緯度)×12；超出範圍的部分被裁掉） ----------
def cxy(lon, lat):
    return int(round(20 + (lon - 80) * 12)), int(round(20 + (50 - lat) * 12))


_CN = [(124, 40), (121.5, 39), (118, 39.2), (119, 37.3), (122.5, 37.2), (120, 35), (121.5, 32), (122, 30), (120, 27), (117.5, 23.6), (114, 22.3),
       (110, 21), (108, 21.6), (106.5, 22.5), (102, 22), (98, 24), (97.5, 28), (92, 28), (85, 28), (80, 30.5), (78.5, 32.5), (76, 36), (74, 39),
       (80, 42.5), (83, 45), (87, 49), (90.5, 47.5), (97, 42.8), (105, 41.8), (111, 43.5), (116, 46.5), (119.5, 47.5), (120, 52.5), (126, 52.7),
       (131, 48), (134.5, 48), (131, 43), (128, 42), (124, 40)]
_HUANGHE = [(96, 35), (101, 36), (103.5, 36), (105, 37.5), (106.5, 39.5), (110, 40.5), (110.5, 38), (110.5, 35), (114, 34.8), (117, 36.5), (119, 37.7)]
_CHANGJIANG = [(92, 33.5), (97, 33), (100, 29), (102.5, 28.5), (104.5, 28.8), (106.5, 29.6), (110, 30.8), (112, 30), (114.3, 30.6), (117, 30.8), (118.8, 32), (121.5, 31.4)]


def _poly(pts):
    return " ".join("%d,%d" % cxy(a, b) for a, b in pts)


CN_BG = (u'<rect x="0" y="0" width="640" height="400" fill="#3a6ea5" fill-opacity="0.07"/>'
         u'<polygon points="%s" fill="#d9822b" fill-opacity="0.10" stroke="#b8941f" stroke-width="1.2"/>'
         u'<polyline points="%s" fill="none" stroke="#b8941f" stroke-width="1.6" opacity="0.7"/>'
         u'<polyline points="%s" fill="none" stroke="#3a6ea5" stroke-width="1.6" opacity="0.6"/>'
         u'<text x="%d" y="%d" font-size="10" fill="#b8941f" opacity="0.8">黃河</text><text x="%d" y="%d" font-size="10" fill="#3a6ea5" opacity="0.8">長江</text>'
         u'<text x="600" y="390" font-size="9" fill="#888" text-anchor="end">示意圖，今日海岸與河道，位置為大約</text>'
         % ((_poly(_CN), _poly(_HUANGHE), _poly(_CHANGJIANG)) + cxy(107, 41.3) + cxy(111, 29.4)))


def cpt(lon, lat, n, d, c=None, a=None):
    x, y = cxy(lon, lat)
    return pt(x, y, n, d, c, a=a)


# ---------- 歐亞示意底圖（經度 −5～125、緯度 15～55；x = 20 + (經度+5)×4.6，y = 20 + (55−緯度)×9） ----------
def exy(lon, lat):
    return int(round(20 + (lon + 5) * 4.6)), int(round(20 + (55 - lat) * 9))


EU_BG = (u'<rect x="0" y="0" width="640" height="400" fill="#3a6ea5" fill-opacity="0.07"/>'
         u'<path d="M%d,%d Q%d,%d %d,%d" fill="none" stroke="#b8941f" stroke-width="10" opacity="0.12" stroke-linecap="round"/>'
         u'<text x="%d" y="%d" font-size="11" fill="#b8941f" opacity="0.8">絲路</text>'
         u'<text x="%d" y="%d" font-size="10" fill="#888">地中海</text><text x="%d" y="%d" font-size="10" fill="#888">波斯灣</text>'
         u'<text x="600" y="390" font-size="9" fill="#888" text-anchor="end">示意圖，非精確比例</text>'
         % (exy(12, 45) + exy(60, 48) + exy(109, 34) + exy(52, 47) + exy(17, 35) + exy(50, 27)))


def ept(lon, lat, n, d, c=None, a=None):
    x, y = exy(lon, lat)
    return pt(x, y, n, d, c, a=a)


def chain(n, c, steps):
    """steps: [(名字, 所在作品, 說明[, 連接符號])]"""
    return {"n": n, "c": c, "s": [list(s) for s in steps]}


def game(n, rows, note=None):
    g = {"n": n, "rows": [list(r) for r in rows]}
    if note:
        g["note"] = note
    return g
