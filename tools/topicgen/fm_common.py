# -*- coding: utf-8 -*-
"""〈菲爾茲獎〉（fm_）共用：課程版型（比照諾貝爾獎系列的六段式精讀）、資料表、統計圖與 FMLIB 互動元件。

FMLIB 元件（class="fm-w"）：
  perc    正方格點滲流：開放機率 p 與「有沒有貫穿」
  primes  質數與質數間隔：計數、孿生質數、最大間隔、間隔分布
  kakeya  掛谷針問題：針在圓、三角形、三尖瓣線內轉 180°
"""
from gen import Lesson
from cc_common import wdg, D, M, LS, _attr
from qt_common import BASEJS
from nv_common import NVLIB, nvw, ev, card, CB, CG, CO, CR, CP, CT, CY, CK
from fm_data import M as MED, ORDER, FIELDS

_DIG = u"〇一二三四五六七八九"


def cy(y):
    return u"".join(_DIG[int(c)] for c in str(y))


FM_NOTE = (u"本課程依國際數學聯盟（IMU）公布的得主與表彰說明整理，獎項理由為中文意譯；生平年份與數學內容參考官方說明、大學新聞與學術文獻（2026 年 10 月查證）。"
           u"數學內容以說明直覺為主，不涉及證明細節。")

TOPICS = {"cx": (u"complex-numbers", u"複數到底在做什麼"), "chaos": (u"chaos-theory", u"混沌理論"), "tc": (u"computability", u"計算理論"),
          "stp": (u"statistical-physics", u"統計物理與相變"), "rp": (u"stochastic-processes", u"隨機過程與馬可夫鏈"), "mc": (u"monte-carlo", u"蒙地卡羅方法"),
          "st": (u"string-theory", u"超弦理論入門"), "rel": (u"relativity", u"廣義相對論"), "qm": (u"quantum-mechanics", u"量子力學"),
          "qc": (u"quantum-computing", u"量子電腦"), "gt": (u"game-theory", u"賽局理論"), "cr": (u"cryptography", u"密碼學全解析"),
          "np": (u"nobel-physics", u"諾貝爾物理獎"), "ne": (u"nobel-economics", u"諾貝爾經濟學獎")}


def XT(key, note=u""):
    tid, name = TOPICS[key]
    return u'<a href="../%s/index.html">〈%s〉</a>%s' % (tid, name, (u"——" + note) if note else u"")


FMLIB = r"""
(function () {
  if (window.__fmLib) return; window.__fmLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function rng(seed) { var s = seed >>> 0; return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }
  function cv(w, h, mw) { var c = document.createElement('canvas'); c.width = w; c.height = h; c.style.cssText = 'width:100%;max-width:' + (mw || w) + 'px;display:block;margin:6px auto;border:1px solid var(--border);border-radius:6px;background:var(--surface)'; return c; }
  function comma(v) { return Math.round(v).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); }

  /* ---------- 滲流 ---------- */
  function initPerc(root, cfg) {
    head(root, cfg.q); var n = cfg.n || 40, p = cfg.p || 0.59, seed = 3, c = cv(400, 400, 400), pi;
    var u1 = slider(root, '每個格點「開放」的機率 p', 0.3, 0.85, 0.01, p, f2, 'p', function (v) { p = v; run(); });
    var u2 = slider(root, '格子大小 n × n', 10, 100, 2, n, function (v) { return v + ' × ' + v; }, 'n', function (v) { n = v; run(); });
    var bb = bar(root), b1 = btn('換一組隨機格點', 'r'), b2 = btn('估計貫穿機率（200 次）', 'e'); bb.appendChild(b1); bb.appendChild(b2);
    root.appendChild(c); pi = info(root); var est = '';
    function sample(sd) { var r = rng(sd), g = new Uint8Array(n * n); for (var i = 0; i < n * n; i++) g[i] = r() < p ? 1 : 0; return g; }
    function flood(g) { var lab = new Uint8Array(n * n), st = []; for (var x = 0; x < n; x++) if (g[x]) { lab[x] = 1; st.push(x); }
      while (st.length) { var k = st.pop(), i = Math.floor(k / n), j = k % n; [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]].forEach(function (q) { if (q[0] < 0 || q[0] >= n || q[1] < 0 || q[1] >= n) return; var kk = q[0] * n + q[1]; if (g[kk] && !lab[kk]) { lab[kk] = 1; st.push(kk); } }); }
      var cross = false; for (var y = 0; y < n; y++) if (lab[(n - 1) * n + y]) cross = true; return { lab: lab, cross: cross }; }
    function run() { var g = sample(seed), f = flood(g), ctx = c.getContext('2d'), s = 400 / n; ctx.clearRect(0, 0, 400, 400);
      for (var i = 0; i < n; i++) for (var j = 0; j < n; j++) { var k = i * n + j; if (!g[k]) continue; ctx.fillStyle = f.lab[k] ? (f.cross ? '#d0564f' : '#d9822b') : 'rgba(58,110,165,0.55)'; ctx.fillRect(j * s, i * s, s - (n < 60 ? 0.6 : 0), s - (n < 60 ? 0.6 : 0)); }
      pi.innerHTML = '藍色：開放的格點；橘色：與最上面一列相連的格點；若它一路連到最下面一列，整團變成<b style="color:#d0564f">紅色</b>（貫穿）。<br>目前：' + (f.cross ? '<b>有貫穿</b>' : '沒有貫穿') + '。正方格點「格點滲流」的臨界機率約 p<sub>c</sub> ≈ 0.5927：p 低於它時大團簇很少，高於它時幾乎必然貫穿；格子越大，轉變越陡。' + est; }
    b1.addEventListener('click', function () { seed = (seed * 37 + 17) % 100003; est = ''; run(); });
    b2.addEventListener('click', function () { var k = 0; for (var t = 0; t < 200; t++) if (flood(sample(1000 + t * 7919)).cross) k++; est = '<br>估計：在 ' + n + ' × ' + n + '、p ＝ ' + f2(p) + ' 時，200 次中有 <b>' + k + '</b> 次貫穿（約 ' + Math.round(k / 2) + '%）。'; run(); });
    u1(); u2(); run();
  }

  /* ---------- 質數與間隔 ---------- */
  function initPrimes(root, cfg) {
    head(root, cfg.q); var lg = cfg.lg || 5, out = el('div'), ch = el('div'), pi;
    var u1 = slider(root, '範圍上限 N', 3, 7, 0.1, lg, function (v) { return comma(Math.pow(10, v)); }, 'n', function (v) { lg = v; draw(); });
    root.appendChild(out); root.appendChild(ch); pi = info(root);
    function draw() { var N = Math.floor(Math.pow(10, lg)), s = new Uint8Array(N + 1), P = [], i, j;
      for (i = 2; i <= N; i++) { if (!s[i]) { P.push(i); for (j = i * i; j <= N; j += i) s[j] = 1; } }
      var tw = 0, mg = 0, mgAt = 0, H = {}; for (i = 1; i < P.length; i++) { var g = P[i] - P[i - 1]; if (g === 2) tw++; if (g > mg) { mg = g; mgAt = P[i - 1]; } if (g <= 40) H[g] = (H[g] || 0) + 1; }
      var D = [], Lr = []; for (var gg = 2; gg <= 40; gg += 2) { D.push([gg, H[gg] || 0]); }
      out.innerHTML = '<div style="margin-top:8px;line-height:1.85">N 以內的質數：<b>' + comma(P.length) + '</b> 個（質數定理估計 N/ln N ≈ ' + comma(N / Math.log(N)) + '）' +
        '<br>孿生質數（差 2）：<b>' + comma(tw) + '</b> 對　最大的質數間隔：<b>' + mg + '</b>（從 ' + comma(mgAt) + ' 開始），約為 (ln N)² ＝ ' + f1(Math.pow(Math.log(N), 2)) + ' 的 ' + f2(mg / Math.pow(Math.log(N), 2)) + ' 倍</div>';
      ch.innerHTML = chart(640, 200, [{ d: D, c: '#3a6ea5', n: '相鄰質數間隔的次數' }], { xl: '間隔大小', y0: 0 });
      pi.innerHTML = '質數平均間隔約 ln N，但間隔有大有小。<b>有界間隔</b>問的是：是否有無限多對相鄰質數的間隔不超過某個固定數？2013 年張益唐證明了 7,000 萬以內；梅納德隨即用更簡單的方法得到 600，合作計畫再降到 246。孿生質數猜想（間隔 2 無限多次）仍未解決。'; }
    u1(); draw();
  }

  /* ---------- 掛谷針 ---------- */
  function initKakeya(root, cfg) {
    head(root, cfg.q); var shape = 'disk', t = 0, timer = null, c = cv(400, 400, 400), pi;
    var bb = bar(root); [['disk', '圓（繞中心轉）'], ['tri', '正三角形（三次樞轉）'], ['delt', '三尖瓣線']].forEach(function (o) { var b = btn(o[1], o[0]); b.addEventListener('click', function () { shape = o[0]; mark(bb, shape); t = 0; draw(); }); bb.appendChild(b); }); mark(bb, 'disk');
    var b2 = bar(root), bp = btn('▶ 轉一圈半（180°）', 'p'), br = btn('↺ 重來', 'z'); b2.appendChild(bp); b2.appendChild(br);
    root.appendChild(c); pi = info(root);
    var S = 260, O = [200, 215];
    function P(x, y) { return [O[0] + x * S, O[1] - y * S]; }
    var r = 0.25, DL = []; for (var k = 0; k <= 720; k++) { var a = 2 * Math.PI * k / 720; DL.push([2 * r * Math.cos(a) + r * Math.cos(2 * a), 2 * r * Math.sin(a) - r * Math.sin(2 * a)]); }
    function inside(x, y, poly) { var ins = false; for (var i = 0, j = poly.length - 1; i < poly.length; j = i++) { var xi = poly[i][0], yi = poly[i][1], xj = poly[j][0], yj = poly[j][1]; if (((yi > y) !== (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi) + xi)) ins = !ins; } return ins; }
    var h = 1, sd = 2 / Math.sqrt(3), TA = [0, 2 / 3], TB = [-sd / 2, -1 / 3], TC = [sd / 2, -1 / 3];
    function needle(u) { /* u: 0..1 */
      if (shape === 'disk') { var th = Math.PI * u; return [[-0.5 * Math.cos(th), -0.5 * Math.sin(th)], [0.5 * Math.cos(th), 0.5 * Math.sin(th)]]; }
      if (shape === 'tri') { var V = [TA, TC, TB, TA], ph = u * 6, i = Math.min(5, Math.floor(ph)), f = ph - i, piv = V[Math.floor(i / 2)], nx = V[Math.floor(i / 2) + 1], prv = V[(Math.floor(i / 2) + 2) % 3];
        function dir(a, b) { var dx = b[0] - a[0], dy = b[1] - a[1], L = Math.hypot(dx, dy); return [dx / L, dy / L]; }
        if (i % 2 === 0) { var d0 = dir(piv, prv), d1 = dir(piv, nx), a0 = Math.atan2(d0[1], d0[0]), a1 = Math.atan2(d1[1], d1[0]); var da = a1 - a0; while (da > Math.PI) da -= 2 * Math.PI; while (da < -Math.PI) da += 2 * Math.PI; var a = a0 + da * f; return [piv, [piv[0] + Math.cos(a), piv[1] + Math.sin(a)]]; }
        var d = dir(piv, nx), slide = (sd - 1) * f, s0 = [piv[0] + d[0] * slide, piv[1] + d[1] * slide]; return [s0, [s0[0] + d[0], s0[1] + d[1]]]; }
      var tt = 2 * Math.PI * u, px = 2 * r * Math.cos(tt) + r * Math.cos(2 * tt), py = 2 * r * Math.sin(tt) - r * Math.sin(2 * tt), ux = -Math.cos(tt / 2), uy = Math.sin(tt / 2), e = [];
      [1, -1].forEach(function (sg) { var s = 0.004; while (s < 1.2 && inside(px + sg * ux * s, py + sg * uy * s, DL)) s += 0.004; e.push([px + sg * ux * s, py + sg * uy * s]); }); return e; }
    function draw() { var ctx = c.getContext('2d'); ctx.clearRect(0, 0, 400, 400); ctx.lineWidth = 2; ctx.strokeStyle = '#5aa469'; ctx.fillStyle = 'rgba(90,164,105,0.15)'; ctx.beginPath();
      if (shape === 'disk') { var q = P(0, 0); ctx.arc(q[0], q[1], 0.5 * S, 0, 7); }
      else if (shape === 'tri') { [TA, TB, TC].forEach(function (v, i) { var q = P(v[0], v[1]); if (i) ctx.lineTo(q[0], q[1]); else ctx.moveTo(q[0], q[1]); }); ctx.closePath(); }
      else DL.forEach(function (v, i) { var q = P(v[0], v[1]); if (i) ctx.lineTo(q[0], q[1]); else ctx.moveTo(q[0], q[1]); });
      ctx.fill(); ctx.stroke();
      var nd = needle(t), a = P(nd[0][0], nd[0][1]), b = P(nd[1][0], nd[1][1]); ctx.strokeStyle = '#d0564f'; ctx.lineWidth = 4; ctx.beginPath(); ctx.moveTo(a[0], a[1]); ctx.lineTo(b[0], b[1]); ctx.stroke();
      var A = { disk: ['π/4', Math.PI / 4], tri: ['1/√3', 1 / Math.sqrt(3)], delt: ['π/8', Math.PI / 8] }[shape];
      pi.innerHTML = '紅線是長度 1 的針，綠色區域是它轉向所需的空間。目前形狀面積：<b>' + A[0] + ' ≈ ' + A[1].toFixed(3) + '</b>（圓 0.785、正三角形 0.577、三尖瓣線 0.393）。' +
        '<br>1928 年 Besicovitch 證明：面積可以要多小有多小——但這樣的集合非常「破碎」。<b>掛谷猜想</b>問的是它的<b>維度</b>：在 n 維空間中，包含每個方向單位線段的集合，維度是否一定是 n？2025 年王虹與 Zahl 證明了三維的情形。'; }
    bp.addEventListener('click', function () { if (timer) return; t = 0; timer = setInterval(function () { t += 0.006; if (t >= 1) { t = 1; clearInterval(timer); timer = null; } draw(); }, 30); });
    br.addEventListener('click', function () { if (timer) { clearInterval(timer); timer = null; } t = 0; draw(); });
    draw();
  }

  function initAll() { document.querySelectorAll('.fm-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ perc: initPerc, primes: initPrimes, kakeya: initKakeya })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

_KATEX = (u'<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">'
          u'<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>'
          u'<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>'
          u'<script>window.addEventListener("load",function(){if(window.renderMathInElement)renderMathInElement(document.body,'
          u'{delimiters:[{left:"\\\\[",right:"\\\\]",display:true},{left:"\\\\(",right:"\\\\)",display:false}]});});</script>')


def fmw(cfg, maxw=680):
    return wdg("fm-w", cfg, maxw)


PERC = fmw({"t": "perc", "q": u"滲流實驗：每個格點以機率 p 開放，開放的格點能不能從上連到下？"}, 440)
PRIMES = fmw({"t": "primes", "q": u"質數與質數間隔：調整範圍，看質數、孿生質數與間隔分布"})
KAKEYA = fmw({"t": "kakeya", "q": u"掛谷針問題：讓長度 1 的針轉向 180°，最少需要多大的面積？"}, 440)


def _finish(body):
    raws = [b[1] for b in body if isinstance(b, tuple) and b[0] == "raw"]
    if any('class="fm-w' in r for r in raws):
        body.insert(0, ("raw", u"<script>%s</script>" % FMLIB))
    if any('class="nv-w' in r for r in raws):
        body.insert(0, ("raw", u"<script>%s</script>" % NVLIB))
    if "\\\\(" in repr(body) or "\\\\[" in repr(body):
        body.append(("raw", _KATEX))
    body.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🏅 %s</p>' % FM_NOTE))
    return body


def lesson(title_, desc, goals, body, check, nxt=None):
    return Lesson(title_, desc, goals, _finish(list(body)), check, nxt)


def age(key):
    y, _, _, b, _, _, _, _ = MED[key]
    return None if b is None else y - b


def who(key):
    y, zh, en, b, d, c, f, cit = MED[key]
    life = u"%d–%s" % (b, d if d else u"") if b else u"—"
    return u"%s（%s，%s）" % (zh, en, life)


def F(key, topic, goals, what, before, timeline, impact, links, check, nxt, extra=None, gapnote=u""):
    """逐人精讀的六段式課程。"""
    y, zh, en, b, d, c, f, cit = MED[key]
    a = age(key)
    rows = [[u"得主", who(key)], [u"國籍", c], [u"獲獎屆別", u"%d 年%s" % (y, u"（1983 年華沙大會頒發）" if y == 1982 else u"")],
            [u"獲獎年齡", (u"約 %d 歲" % a) if a is not None else u"未滿 40 歲"], [u"領域", FIELDS[f]], [u"表彰重點", cit]]
    body = [("h", u"1. 得主與官方表彰"), ("t", [u"項目", u"內容"], rows), ("h", u"2. 那到底是什麼")]
    body += [("p", x) if isinstance(x, str) else x for x in what]
    if extra:
        body += extra
    body.append(("h", u"3. 在此之前的困境"))
    body.append(("ul", [x for x in before if not x.startswith(u"§")]))
    body += [("p", x[1:]) for x in before if x.startswith(u"§")]
    body += [("h", u"4. 從成果到獲獎"), ("t", [u"時間", u"事件"], [list(t) for t in timeline])]
    if gapnote:
        body.append(("p", gapnote))
    body += [("h", u"5. 今天的影響"), ("ul", impact)]
    if links:
        body += [("h", u"6. 站上延伸連結"), ("ul", links)]
    return lesson(u"%s年：%s——%s" % (cy(y), zh, topic), u"%d 年菲爾茲獎得主 %s" % (y, en), goals, body, check, nxt)


def era_table(keys):
    rows = []
    for k in keys:
        y, zh, en, b, d, c, f, cit = MED[k]
        a = age(k)
        rows.append([str(y), u"%s<br><span style='font-size:0.85em;color:var(--text-muted)'>%s</span>" % (zh, en), c, (u"%d" % a) if a is not None else u"—", FIELDS[f], cit])
    return ("t", [u"屆", u"得主", u"國籍", u"約略年齡", u"領域", u"表彰重點"], rows)


def era_keys(y0, y1):
    return [k for k in ORDER if y0 <= MED[k][0] <= y1]


def timeline_all(q=u"歷屆菲爾茲獎得主（點一列看說明；可依領域篩選）："):
    groups = [[k, v, c] for (k, v), c in zip(FIELDS.items(), [CB, CO, CP, CG, CR, CT, CY, CK, "#888", "#c26"])]
    evs = []
    for k in ORDER:
        y, zh, en, b, d, c, f, cit = MED[k]
        evs.append(ev(str(y), u"%s（%s）" % (zh, en), u"%s。%s" % (c, cit), f))
    return nvw({"t": "timeline", "q": q, "yw": 52, "groups": groups, "ev": evs})


def cards_all():
    groups = [[k, v, c] for (k, v), c in zip(FIELDS.items(), [CB, CO, CP, CG, CR, CT, CY, CK, "#888", "#c26"])]
    cs = [card(u"%s（%d）" % (MED[k][1], MED[k][0]), MED[k][6], u"%s。%s" % (MED[k][5], MED[k][7]), MED[k][2]) for k in ORDER]
    return nvw({"t": "cards", "q": u"68 位得主速查（可依領域篩選或搜尋）：", "groups": groups, "cards": cs})


def age_chart():
    """獲獎年齡分布長條圖（靜態 SVG）。"""
    ages = [age(k) for k in ORDER if age(k) is not None]
    bins = list(range(26, 41))
    cnt = [sum(1 for a in ages if a == b) for b in bins]
    W, H, L, B, T = 640, 230, 36, 34, 20
    mx = max(cnt)
    bw = (W - L - 10) / float(len(bins))
    g = []
    for i, (b, n) in enumerate(zip(bins, cnt)):
        h = (H - B - T) * n / float(mx)
        x = L + i * bw
        g.append(u'<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#3a6ea5" rx="2"/>' % (x + 3, H - B - h, bw - 6, h))
        if n:
            g.append(u'<text x="%.1f" y="%.1f" font-size="11" fill="currentColor" text-anchor="middle">%d</text>' % (x + bw / 2, H - B - h - 4, n))
        g.append(u'<text x="%.1f" y="%d" font-size="11" fill="var(--text-muted)" text-anchor="middle">%d</text>' % (x + bw / 2, H - B + 15, b))
    g.append(u'<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#999"/>' % (L, H - B, W - 10, H - B))
    g.append(u'<text x="%d" y="%d" font-size="11" fill="var(--text-muted)" text-anchor="middle">獲獎年齡（屆別年份 − 出生年，可能比實際年齡多 1 歲）</text>' % (W / 2, H - 4))
    svg_ = u'<svg viewBox="0 0 %d %d" style="width:100%%;display:block;color:var(--text)">%s</svg>' % (W, H, u"".join(g))
    mean = sum(ages) / float(len(ages))
    return ("raw", u'<div class="content-figure" style="max-width:680px;margin:0 auto 16px">%s<p style="text-align:center;font-size:0.9em;color:var(--text-muted)">已知出生年的 %d 位得主，平均獲獎年齡約 %.1f 歲；最年輕的是 1954 年的塞爾（獲獎時 27 歲）。</p></div>' % (svg_, len(ages), mean))


def field_table():
    rows = []
    for fk, fname in FIELDS.items():
        ks = [k for k in ORDER if MED[k][6] == fk]
        if not ks:
            continue
        rows.append([fname, str(len(ks)), u"、".join(MED[k][1] for k in ks)])
    rows.sort(key=lambda r: -int(r[1]))
    return ("t", [u"領域（本課程的粗分）", u"人數", u"得主"], rows)


def country_table():
    from collections import Counter
    cnt = Counter()
    for k in ORDER:
        c = MED[k][5]
        for part in c.replace(u"（", u"／").replace(u"）", u"").split(u"／"):
            part = part.strip()
            if part.startswith(u"生於") or part.endswith(u"背景") or part == u"無國籍":
                continue
            cnt[part] += 1
    rows = [[k, str(v)] for k, v in cnt.most_common()]
    return ("t", [u"國籍（雙重國籍分別計入）", u"人次"], rows)
