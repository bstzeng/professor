# -*- coding: utf-8 -*-
"""〈美國五十州〉與〈中國各省〉共用的地圖投影與 SVG 地圖繪製工具。

邊界資料由 geoprep.py 投影、簡化後寫成 ust_geo.py / cnp_geo.py；
這裡只放投影公式（用來把首府經緯度畫到同一張圖上）與畫圖函式。
"""
import math


def albers(p1, p2, p0, l0):
    """回傳 Albers 等積圓錐投影函式 f(lon, lat) -> (x, y)（單位：地球半徑，y 向上）。"""
    r = math.radians
    n = (math.sin(r(p1)) + math.sin(r(p2))) / 2
    c = math.cos(r(p1)) ** 2 + 2 * n * math.sin(r(p1))
    rho0 = math.sqrt(c - 2 * n * math.sin(r(p0))) / n

    def f(lon, lat):
        rho = math.sqrt(c - 2 * n * math.sin(r(lat))) / n
        th = n * r(lon - l0)
        return rho * math.sin(th), rho0 - rho * math.cos(th)
    return f


# ---------- 美國：本土 48 州 + 阿拉斯加、夏威夷插圖 ----------
_US48 = albers(29.5, 45.5, 37.5, -96)
_USAK = albers(55, 65, 50, -154)
_USHI = albers(8, 18, 3, -157)
US_K = 1000.0           # 每地球半徑對應的 SVG 單位


def us_xy(lon, lat, part="48"):
    from ust_geo import US_T        # 各區的 (縮放, 平移 x, 平移 y)，由 geoprep.py 決定
    f = {"48": _US48, "AK": _USAK, "HI": _USHI}[part]
    x, y = f(lon, lat)
    s, dx, dy = US_T[part]
    return x * US_K * s + dx, -y * US_K * s + dy


# ---------- 中國 ----------
_CN = albers(25, 47, 35, 105)
CN_K = 1000.0


def cn_xy(lon, lat):
    from cnp_geo import CN_T
    x, y = _CN(lon, lat)
    return x * CN_K + CN_T[0], -y * CN_K + CN_T[1]


# ---------- 日本：本土 + 沖繩插圖 ----------
_JP = albers(30, 42, 36, 136)
JP_K = 2400.0


def jp_xy(lon, lat, part="main"):
    from jpp_geo import JP_T
    x, y = _JP(lon, lat)
    s, dx, dy = JP_T[part]
    return x * JP_K * s + dx, -y * JP_K * s + dy


# ---------- 幾何 ----------
import json as _json
import re as _re

_NUM = _re.compile(r"-?\d+")


def rings_of(path):
    """把 geoprep 產生的 "M..L..Z" 路徑拆回點列。"""
    out = []
    for seg in path.split("M")[1:]:
        nums = [int(v) for v in _NUM.findall(seg)]
        out.append(list(zip(nums[0::2], nums[1::2])))
    return out


def _area_c(r):
    a = cx = cy = 0.0
    for i in range(len(r)):
        x0, y0 = r[i - 1]
        x1, y1 = r[i]
        k = x0 * y1 - x1 * y0
        a += k
        cx += (x0 + x1) * k
        cy += (y0 + y1) * k
    if abs(a) < 1e-9:
        return 0.0, r[0][0], r[0][1]
    return abs(a) / 2, cx / (3 * a), cy / (3 * a)


def centroid(path):
    """最大的那一塊的形心，用來放文字。"""
    best = max((_area_c(r) for r in rings_of(path)), key=lambda t: t[0])
    return best[1], best[2]


def bbox_of(path):
    pts = [p for r in rings_of(path) for p in r]
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def inside(path, x, y):
    """點是否在路徑內（射線法）。"""
    hit = False
    for r in rings_of(path):
        for i in range(len(r)):
            x0, y0 = r[i - 1]
            x1, y1 = r[i]
            if (y0 > y) != (y1 > y) and x < (x1 - x0) * (y - y0) / (y1 - y0) + x0:
                hit = not hit
    return hit


def touching(paths, tol=2.5):
    """粗略的鄰接判斷：兩區的邊界點彼此距離小於 tol 的點數夠多就算相鄰。"""
    pts = {k: [p for r in rings_of(v) for p in r] for k, v in paths.items()}
    bb = {k: bbox_of(v) for k, v in paths.items()}

    def segd(px, py, a, b):
        ax, ay = a
        bx, by = b
        dx, dy = bx - ax, by - ay
        L = dx * dx + dy * dy
        t = 0 if L == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L))
        qx, qy = ax + t * dx, ay + t * dy
        return ((px - qx) ** 2 + (py - qy) ** 2) ** 0.5
    res = {}
    keys = sorted(paths)
    for i, a in enumerate(keys):
        for b in keys[i + 1:]:
            A, B = bb[a], bb[b]
            if A[0] > B[2] + tol or B[0] > A[2] + tol or A[1] > B[3] + tol or B[1] > A[3] + tol:
                continue
            n = 0
            for r in rings_of(paths[b]):
                for px, py in pts[a]:
                    if px < B[0] - tol or px > B[2] + tol or py < B[1] - tol or py > B[3] + tol:
                        continue
                    if any(segd(px, py, r[j - 1], r[j]) < tol for j in range(len(r))):
                        n += 1
            if n >= 2:
                res.setdefault(a, set()).add(b)
                res.setdefault(b, set()).add(a)
    return res


# ---------- 靜態地圖（每課的位置圖） ----------
BASE = "#b7c4d4"
NEAR = "#e9b98c"
HL = "#c0392b"
STROKE = "var(--surface)"


def static_map(vb, paths, hl, near=(), star=None, label=None, extra=None, small=None, crop=None, names=None):
    """回傳 (svg 內容, viewBox)。hl 紅色、near 橘色、其餘灰藍；star=(x,y) 首府；
    small=True 時在 hl 外圍畫一個圈，方便看出小州的位置；crop=(x0,y0,x1,y1) 只畫局部；
    names={code: (文字, x, y)} 額外標的地名。"""
    g = []
    for k, d in sorted(paths.items()):
        if k == hl:
            continue
        fill = NEAR if k in near else BASE
        g.append('<path d="%s" fill="%s" stroke="%s" stroke-width="0.8"/>' % (d, fill, STROKE))
    if extra:
        g.append(extra)
    g.append('<path d="%s" fill="%s" stroke="%s" stroke-width="1"/>' % (paths[hl], HL, STROKE))
    x0, y0, x1, y1 = bbox_of(paths[hl])
    if small:
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        r = max(x1 - x0, y1 - y0) / 2 + 9
        g.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="2"/>' % (cx, cy, r, HL))
    for k, (t, x, y) in (names or {}).items():
        g.append('<text x="%d" y="%d" font-size="11" text-anchor="middle" fill="var(--text)" '
                 'stroke="var(--surface)" stroke-width="3" paint-order="stroke">%s</text>' % (x, y, t))
    if label:
        t, lx, ly = label
        if star and abs(star[0] - lx) < 9 * len(t) and -22 < star[1] - ly < 8:
            ly = star[1] - 12 if star[1] - ly > -8 else star[1] + 24
        g.append('<text x="%d" y="%d" font-size="15" font-weight="bold" text-anchor="middle" fill="%s" '
                 'stroke="var(--surface)" stroke-width="4" paint-order="stroke">%s</text>' % (lx, ly, HL, t))
    if star:
        g.append(_star(star[0], star[1], 6.5))
    if crop:
        cx0, cy0, cx1, cy1 = crop
        return "\n".join(g), "%d %d %d %d" % (cx0, cy0, cx1 - cx0, cy1 - cy0)
    return "\n".join(g), "0 0 %d %d" % tuple(vb)


def _star(x, y, r):
    import math
    pts = []
    for i in range(10):
        a = math.pi / 2 + i * math.pi / 5
        rr = r if i % 2 == 0 else r * 0.45
        pts.append("%.1f,%.1f" % (x + rr * math.cos(a), y - rr * math.sin(a)))
    return '<polygon points="%s" fill="#f5c518" stroke="#3a2a00" stroke-width="0.8"/>' % " ".join(pts)


def legend(x, y, items):
    """items = [(顏色, 文字)]，回傳 svg 片段。"""
    g = []
    for c, t in items:
        if c == "star":
            g.append(_star(x + 6, y - 4, 6))
        else:
            g.append('<rect x="%d" y="%d" width="12" height="10" rx="2" fill="%s"/>' % (x, y - 9, c))
        g.append('<text x="%d" y="%d" font-size="11" fill="var(--text)">%s</text>' % (x + 17, y, t))
        x += 26 + 12 * len(t)
    return "\n".join(g)


# ---------- 互動地圖（GEOLIB） ----------
def geolib(flag, dataset):
    """dataset = {vb, items:[{c,n,p,x,y,sx,sy,L,g,v:{...},f:[[k,v]]}], groups:{g:[名,色]}, metrics:[[鍵,名,單位,小數]],
    extra:svg 片段, unit:'州', join: bool}"""
    from qt_common import BASEJS
    return (r"""
(function () {
  if (window.%s) return; window.%s = 1;
""" % (flag, flag) + BASEJS + r"""
  var D = """ + _json.dumps(dataset, ensure_ascii=False, separators=(",", ":")) + r""";
  var BASE = '#b7c4d4', HL = '#c0392b', OK = '#2e7d4f', BAD = '#e67e22';
  function byC(c) { for (var i = 0; i < D.items.length; i++) if (D.items[i].c === c) return D.items[i]; }
  function mapSvg(root, onClick) {
    var box = el('div', 'margin:6px 0'); root.appendChild(box);
    var g = (D.extra || '');
    D.items.forEach(function (it) { g += '<path data-c="' + it.c + '" d="' + it.p + '" fill="' + BASE + '" stroke="var(--surface)" stroke-width="0.8" style="cursor:pointer"><title>' + it.n + '</title></path>'; });
    g += '<g class="lab"></g>';
    box.innerHTML = svgw('0 0 ' + D.vb[0] + ' ' + D.vb[1], g);
    var svg = box.querySelector('svg');
    svg.querySelectorAll('path[data-c]').forEach(function (p) { p.addEventListener('click', function () { onClick(p.getAttribute('data-c')); }); });
    return {
      fill: function (f) { svg.querySelectorAll('path[data-c]').forEach(function (p) { p.setAttribute('fill', f(p.getAttribute('data-c')) || BASE); }); },
      label: function (list) { var s = ''; list.forEach(function (l) { s += '<text x="' + l[1] + '" y="' + l[2] + '" font-size="' + (l[3] || 13) + '" font-weight="bold" text-anchor="middle" fill="' + (l[4] || 'var(--text)') + '" stroke="var(--surface)" stroke-width="3.5" paint-order="stroke" pointer-events="none">' + l[0] + '</text>'; });
        svg.querySelector('.lab').innerHTML = s; }
    };
  }
  function infoHtml(it) {
    var s = '<b style="font-size:1.08em">' + it.n + '</b>' + (it.e ? '　<span style="color:var(--text-muted)">' + it.e + '</span>' : '') + '<br>';
    s += '<span style="display:inline-block;padding:0 6px;border-radius:6px;font-size:0.85em;color:#fff;background:' + D.groups[it.g][1] + '">' + D.groups[it.g][0] + '</span> ';
    it.f.forEach(function (kv) { s += '<span style="margin-right:12px">' + kv[0] + '：<b>' + kv[1] + '</b></span>'; });
    if (it.L) s += '<br><a href="' + (D.href || '') + 'lesson-' + (it.L < 10 ? '0' : '') + it.L + '.html">→ 看第 ' + it.L + ' 課的完整介紹</a>';
    return s;
  }
  function initExplore(root, cfg) {
    head(root, cfg.q); var b = el('div'); root.appendChild(b);
    var mode = 'g';
    var m = mapSvg(root, function (c) { show(c); });
    var p = el('div', 'margin:6px 0 0;line-height:1.8;min-height:3.4em'); root.appendChild(p);
    var lg = el('div', 'font-size:0.85em;color:var(--text-muted)'); root.appendChild(lg);
    var cur = null;
    function colorBy() { if (mode === 'g') { m.fill(function (c) { return c === cur ? HL : D.groups[byC(c).g][1]; });
        var s = ''; for (var k in D.groups) s += '<span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:' + D.groups[k][1] + ';margin:0 4px 0 10px"></span>' + D.groups[k][0]; lg.innerHTML = s; }
      else { var met = D.metrics[mode], vals = D.items.map(function (it) { return it.v[met[0]]; }), lo = Math.min.apply(null, vals), hi = Math.max.apply(null, vals);
        m.fill(function (c) { if (c === cur) return HL; var t = (Math.log(byC(c).v[met[0]] + 1) - Math.log(lo + 1)) / (Math.log(hi + 1) - Math.log(lo + 1) || 1);
          return 'rgb(' + Math.round(225 - 180 * t) + ',' + Math.round(235 - 140 * t) + ',' + Math.round(245 - 90 * t) + ')'; });
        lg.innerHTML = '顏色越深＝' + met[1] + '越大（對數刻度）'; } }
    function show(c) { cur = c; var it = byC(c); p.innerHTML = infoHtml(it); colorBy(); m.label([[it.n, it.x, it.y - 10, 14, HL]]); }
    var bb = btn('依地區上色', 'g'); bb.addEventListener('click', function () { mode = 'g'; mark(b, 'g'); colorBy(); }); b.appendChild(bb);
    D.metrics.forEach(function (met, i) { var x = btn('依' + met[1], i); x.addEventListener('click', function () { mode = i; mark(b, i); colorBy(); }); b.appendChild(x); });
    mark(b, 'g'); colorBy(); p.innerHTML = '<span style="color:var(--text-muted)">點地圖上的任一' + D.unit + '，看它的基本資料。</span>';
  }
  function initQuiz(root, cfg) {
    head(root, cfg.q); var b = el('div'); root.appendChild(b);
    var ask = el('p', 'margin:6px 0;font-size:1.1em;font-weight:bold'); root.appendChild(ask);
    var target, done = {}, ok = 0, tries = 0, wrong = 0, pool = [];
    var m = mapSvg(root, function (c) { if (!target) return; tries++;
      if (c === target.c) { ok++; done[c] = wrong ? BAD : OK; msg.innerHTML = '✅ 答對了！' + (wrong ? '（試了 ' + (wrong + 1) + ' 次）' : ''); next(); }
      else { wrong++; var w = byC(c); msg.innerHTML = '❌ 那是<b>' + w.n + '</b>，再找找看。' + (wrong >= 3 ? '（提示：' + D.groups[target.g][0] + '）' : '');
        m.fill(function (k) { return k === c ? '#e74c3c' : done[k]; }); m.label([[w.n, w.x, w.y - 8, 12, '#c0392b']]); } });
    var msg = el('p', 'margin:4px 0;min-height:1.6em'); root.appendChild(msg);
    var sc = el('p', 'margin:0;font-size:0.9em;color:var(--text-muted)'); root.appendChild(sc);
    function next() { m.fill(function (k) { return done[k]; }); m.label([]); wrong = 0;
      if (!pool.length) { target = null; ask.innerHTML = '🎉 全部完成！'; sc.textContent = '共 ' + D.items.length + ' 題，一次就答對 ' + Object.keys(done).filter(function (k) { return done[k] === OK; }).length + ' 題。'; return; }
      target = pool.pop(); ask.innerHTML = '請在地圖上找出：<span style="color:' + HL + '">' + target.n + '</span>';
      sc.textContent = '進度 ' + Object.keys(done).length + ' / ' + D.items.length + '（綠色＝一次答對，橘色＝試了幾次才答對）'; }
    function start(g) { done = {}; pool = D.items.filter(function (it) { return !g || it.g === g; }).slice();
      for (var i = pool.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = pool[i]; pool[i] = pool[j]; pool[j] = t; }
      msg.innerHTML = ''; next(); }
    var a = btn('全部', ''); a.addEventListener('click', function () { mark(b, ''); start(''); }); b.appendChild(a);
    for (var k in D.groups) (function (k) { var x = btn(D.groups[k][0], k); x.addEventListener('click', function () { mark(b, k); start(k); }); b.appendChild(x); })(k);
    mark(b, ''); start('');
  }
  function initJoin(root, cfg) {
    head(root, cfg.q); var ys = D.items.map(function (it) { return it.v.year; }), y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys), timer = null;
    var b = el('div'); root.appendChild(b);
    var m = mapSvg(root, function (c) { var it = byC(c); p.innerHTML = '<b>' + it.n + '</b>：' + it.v.year + ' 年加入，第 ' + it.v.ord + ' 個' + D.unit + '。'; });
    var p = el('p', 'margin:4px 0;min-height:3em;line-height:1.7'); root.appendChild(p);
    var upd = slider(root, '年份', y0, y1, 1, y0, function (v) { return v; }, 'yr', function (y) {
      var n = 0, now = [];
      m.fill(function (c) { var it = byC(c); if (it.v.year < y) { n++; return '#5b7fa6'; } if (it.v.year === y) { n++; now.push(it); return HL; } return null; });
      m.label(now.map(function (it) { return [it.n, it.x, it.y - 8, 12, HL]; }));
      p.innerHTML = '<b>' + y + ' 年</b>：共 ' + n + ' 個' + D.unit + (now.length ? '；這一年加入：' + now.map(function (it) { return '<b>' + it.n + '</b>（第 ' + it.v.ord + ' 個）'; }).join('、') : '') +
        (D.joinNote && D.joinNote[y] ? '<br><span style="color:var(--text-muted)">' + D.joinNote[y] + '</span>' : ''); });
    var s = root.querySelector('input[data-k="yr"]');
    var pl = btn('▶ 播放'); pl.addEventListener('click', function () { if (timer) { clearInterval(timer); timer = null; pl.textContent = '▶ 播放'; return; }
      if (+s.value >= y1) s.value = y0; pl.textContent = '⏸ 暫停';
      timer = setInterval(function () { var v = +s.value, nx = y1; ys.forEach(function (y) { if (y > v && y < nx) nx = y; }); s.value = nx; upd(); if (nx >= y1) { clearInterval(timer); timer = null; pl.textContent = '▶ 播放'; } }, 700); });
    b.appendChild(pl); upd();
  }
  function initRank(root, cfg) {
    head(root, cfg.q); var b = el('div'); root.appendChild(b); var box = el('div', 'margin-top:8px'), k = 0; root.appendChild(box);
    function draw() { var met = D.metrics[k], arr = D.items.slice().sort(function (a, c) { return c.v[met[0]] - a.v[met[0]]; }), mx = arr[0].v[met[0]];
      var s = '';
      arr.forEach(function (it, i) { var v = it.v[met[0]], w = Math.max(0.5, v / mx * 100);
        s += '<div style="display:flex;align-items:center;gap:6px;font-size:0.86em;line-height:1.5">' +
          '<span style="width:2.2em;text-align:right;color:var(--text-muted)">' + (i + 1) + '</span>' +
          '<span style="width:6.5em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + it.n + '</span>' +
          '<span style="flex:1;min-width:0"><span style="display:block;height:11px;border-radius:3px;width:' + w + '%;background:' + D.groups[it.g][1] + '"></span></span>' +
          '<span style="width:7em;text-align:right">' + (met[3] !== undefined ? v.toFixed(met[3]) : v) + ' ' + met[2] + '</span></div>'; });
      var lg = ''; for (var g in D.groups) lg += '<span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:' + D.groups[g][1] + ';margin:0 4px 0 10px"></span>' + D.groups[g][0];
      box.innerHTML = '<div style="font-size:0.85em;color:var(--text-muted);margin-bottom:4px">' + lg + '</div>' + s + (met[4] ? '<p style="font-size:0.85em;color:var(--text-muted)">' + met[4] + '</p>' : ''); }
    D.metrics.forEach(function (met, i) { var x = btn(met[1], i); x.addEventListener('click', function () { k = i; mark(b, i); draw(); }); b.appendChild(x); });
    mark(b, 0); draw();
  }
  function initAll() {
    document.querySelectorAll('.""" + flag + r"""-w').forEach(function (root) {
      if (root.getAttribute('data-done')) return; root.setAttribute('data-done', 1);
      var cfg = JSON.parse(root.getAttribute('data-cfg'));
      ({ explore: initExplore, quiz: initQuiz, join: initJoin, rank: initRank })[cfg.t](root, cfg);
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
""")
