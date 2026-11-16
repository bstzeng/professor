# -*- coding: utf-8 -*-
"""〈資訊理論〉（inf_）共用：課程包裝與 INFLIB 互動元件（class="inf-w"）。

  binent  二元熵：硬幣正面機率 p → H(p) 曲線
  huff    文字壓縮：輸入文字 → 字元頻率、熵、霍夫曼編碼與平均長度
  chan    雜訊通道：翻轉機率 p → 不編碼、三次重複、漢明(7,4) 的錯誤率與碼率，及通道容量
  kl      交叉熵與 KL 散度：真實分布 P、模型分布 Q → H(P)、H(P,Q)、KL
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

INF_NOTE = (u"本課的推導以主要步驟為主；互動模擬為教學用的小型版本。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def ifw(cfg, maxw=680):
    return wdg("inf-w", cfg, maxw)


INFLIB = r"""
(function () {
  if (window.__infLib) return; window.__infLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function lg(x) { return Math.log(x) / Math.LN2; }
  function H2(p) { return p <= 0 || p >= 1 ? 0 : -p * lg(p) - (1 - p) * lg(1 - p); }
  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

  function initBin(root, cfg) {
    head(root, cfg.q); var P = { p: 0.5 }, view = el('div'), inf;
    var u = slider(root, '硬幣出現正面的機率 p', 0, 1, 0.01, P.p, function (x) { return f2(x); }, null, function (x) { P.p = x; draw(); });
    root.appendChild(view); inf = info(root);
    var curve = []; for (var i = 0; i <= 200; i++) { var q = i / 200; curve.push([q, H2(q)]); }
    function draw() { var h = H2(P.p);
      view.innerHTML = chart(640, 240, [{ d: curve, c: BL, n: '熵 H(p)（位元）', w: 2 }], { x0: 0, x1: 1, y0: 0, y1: 1.05, xl: '正面的機率 p', pts: [{ x: P.p, y: h, c: RD, n: 'H = ' + f2(h) }] });
      var n = h > 0 ? Math.round(1000 * h) : 0;
      inf.innerHTML = '每次擲硬幣平均帶來 <b>' + f2(h) + ' 位元</b>的資訊。記錄 1000 次的結果，最少平均需要約 <b>' + n + ' 位元</b>（不壓縮要 1000 位元）。' +
        (P.p === 0.5 ? '<br>公平硬幣最難預測，熵最大：剛好 1 位元。' : P.p === 0 || P.p === 1 ? '<br>結果完全確定，沒有任何「驚訝」，熵為 0。' : '<br>越偏向一邊，結果越容易猜，平均的驚訝越小，熵越低。'); }
    u();
  }

  function huffman(freq) { var nodes = Object.keys(freq).map(function (c) { return { w: freq[c], c: c }; });
    if (nodes.length === 1) { var o = {}; o[nodes[0].c] = '0'; return o; }
    while (nodes.length > 1) { nodes.sort(function (a, b) { return a.w - b.w; }); var a = nodes.shift(), b = nodes.shift(); nodes.push({ w: a.w + b.w, l: a, r: b }); }
    var code = {}; (function walk(n, s) { if (n.c !== undefined) { code[n.c] = s; return; } walk(n.l, s + '0'); walk(n.r, s + '1'); })(nodes[0], ''); return code; }

  function initHuff(root, cfg) {
    head(root, cfg.q); var ta = document.createElement('textarea'); ta.rows = 3; ta.style.cssText = 'width:100%;box-sizing:border-box;font-size:1em;padding:6px;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text)';
    ta.value = cfg.text || 'abracadabra'; root.appendChild(ta);
    var b = bar(root); (cfg.presets || []).forEach(function (s) { var x = btn(s[0]); x.onclick = function () { ta.value = s[1]; draw(); }; b.appendChild(x); });
    var view = el('div', 'overflow-x:auto'), inf; root.appendChild(view); inf = info(root);
    function draw() { var s = Array.from(ta.value); if (!s.length) { view.innerHTML = ''; inf.innerHTML = '請輸入一些文字。'; return; }
      var f = {}; s.forEach(function (c) { f[c] = (f[c] || 0) + 1; }); var keys = Object.keys(f).sort(function (a, b) { return f[b] - f[a]; }), N = s.length, H = 0;
      keys.forEach(function (c) { var p = f[c] / N; H -= p * lg(p); }); var code = huffman(f), L = 0; keys.forEach(function (c) { L += f[c] / N * code[c].length; });
      var fixed = Math.max(1, Math.ceil(lg(keys.length)));
      var rows = keys.slice(0, 14).map(function (c) { var p = f[c] / N, nm = c === ' ' ? '（空格）' : c === '\n' ? '（換行）' : esc(c);
        return '<tr><td style="padding:2px 8px;text-align:center">' + nm + '</td><td style="padding:2px 8px;text-align:right">' + f[c] + '</td><td style="padding:2px 8px;text-align:right">' + f2(p * 100) + '%</td><td style="padding:2px 8px;text-align:right">' + f2(-lg(p)) + '</td><td style="padding:2px 8px;font-family:ui-monospace,monospace">' + code[c] + '</td></tr>'; }).join('');
      view.innerHTML = '<table style="border-collapse:collapse;font-size:0.88em;margin:8px auto"><tr style="border-bottom:1px solid var(--border)"><th style="padding:2px 8px">字元</th><th style="padding:2px 8px">次數</th><th style="padding:2px 8px">機率</th><th style="padding:2px 8px">資訊量（位元）</th><th style="padding:2px 8px">霍夫曼碼</th></tr>' + rows + '</table>' + (keys.length > 14 ? '<div style="text-align:center;font-size:0.85em;color:var(--text-muted)">（只列出最常見的 14 個，共 ' + keys.length + ' 種字元）</div>' : '');
      inf.innerHTML = '共 <b>' + N + '</b> 個字元、<b>' + keys.length + '</b> 種。用固定長度編碼，每個字元要 <b>' + fixed + '</b> 位元，總共 ' + fixed * N + ' 位元。' +
        '<br>熵 H = <b>' + f2(H) + '</b> 位元/字元（任何逐字元編碼的極限）；霍夫曼編碼平均 <b>' + f2(L) + '</b> 位元/字元，總共 ' + Math.round(L * N) + ' 位元。' +
        '<br>常見的字元拿到短碼、罕見的拿到長碼；霍夫曼的平均長度永遠在 H 與 H + 1 之間。'; }
    ta.oninput = draw; draw();
  }

  function binom(n, k) { var r = 1; for (var i = 1; i <= k; i++) r = r * (n - k + i) / i; return r; }
  function berRep(p) { return 3 * p * p * (1 - p) + p * p * p; }
  function berHam(p) { var s = 0; for (var k = 2; k <= 7; k++) s += binom(7, k) * Math.pow(p, k) * Math.pow(1 - p, 7 - k) * Math.min(1, (k + 1) / 7); return s; }
  function initChan(root, cfg) {
    head(root, cfg.q); var P = { p: 0.05 }, view = el('div'), view2 = el('div', 'font-family:ui-monospace,Menlo,monospace;font-size:0.85em;line-height:1.6;margin-top:6px;word-break:break-all'), inf;
    var u = slider(root, '通道翻轉每個位元的機率 p', 0, 0.3, 0.005, P.p, function (x) { return f2(x * 100) + '%'; }, null, function (x) { P.p = x; draw(); });
    root.appendChild(view); root.appendChild(view2); inf = info(root);
    var c0 = [], c1 = [], c2 = []; for (var i = 0; i <= 60; i++) { var q = i / 200; c0.push([q, q]); c1.push([q, berRep(q)]); c2.push([q, berHam(q)]); }
    var msg = []; for (i = 0; i < 48; i++) msg.push(Math.random() < 0.5 ? 1 : 0);
    function draw() { var p = P.p, C = 1 - H2(p);
      view.innerHTML = chart(640, 230, [{ d: c0, c: GY, n: '不編碼（碼率 1）', w: 1.6 }, { d: c2, c: GN, n: '漢明 (7,4)（碼率 0.57）', w: 2 }, { d: c1, c: OR, n: '三次重複（碼率 0.33）', w: 2 }],
        { x0: 0, x1: 0.3, y0: 0, y1: 0.3, xl: '通道翻轉機率 p', yl: '解碼後的位元錯誤率', vl: [{ x: p, c: RD, n: '' }] });
      var recv = msg.map(function (b) { return Math.random() < p ? 1 - b : b; }), errs = 0;
      view2.innerHTML = '傳送：' + msg.join('') + '<br>收到：' + recv.map(function (b, i) { if (b !== msg[i]) { errs++; return '<span style="color:' + RD + ';font-weight:bold">' + b + '</span>'; } return b; }).join('') + '　（' + errs + ' 個錯誤）';
      inf.innerHTML = '不編碼：錯誤率 <b>' + f2(p * 100) + '%</b>；三次重複：<b>' + (berRep(p) * 100).toFixed(2) + '%</b>（但只剩 1/3 的速度）；漢明 (7,4)：約 <b>' + (berHam(p) * 100).toFixed(2) + '%</b>（保留 4/7 的速度）。' +
        '<br>夏農的通道容量 C = 1 − H(p) = <b>' + f2(C) + '</b> 位元/次：只要碼率低於 ' + f2(C) + '，就<b>存在</b>能讓錯誤率任意接近 0 的編碼（第 16 課）。重複碼與漢明碼離這個極限都還很遠。'; }
    u();
  }

  function initKL(root, cfg) {
    head(root, cfg.q); var labs = cfg.labels, Pt = cfg.p, Q = cfg.q0.slice(), view = el('div'), inf;
    var us = labs.map(function (lb, i) { return slider(root, '模型給「' + lb + '」的權重', 0.01, 1, 0.01, Q[i], function (x) { return f2(x); }, null, function (x) { Q[i] = x; draw(); }); });
    var b = bar(root); var x1 = btn('模型 = 真實分布'); x1.onclick = function () { Pt.forEach(function (v, i) { Q[i] = v; }); us.forEach(function (u) { u(); }); }; b.appendChild(x1);
    var x2 = btn('模型 = 平均分布'); x2.onclick = function () { Q.forEach(function (v, i) { Q[i] = 1 / Q.length; }); us.forEach(function (u) { u(); }); }; b.appendChild(x2);
    root.appendChild(view); inf = info(root);
    function draw() { var s = Q.reduce(function (a, b) { return a + b; }, 0), q = Q.map(function (v) { return v / s; }), H = 0, CE = 0;
      Pt.forEach(function (p, i) { if (p > 0) { H -= p * lg(p); CE -= p * lg(q[i]); } }); var KL = CE - H;
      var W = 640, Hh = 200, n = labs.length, bw = (W - 80) / n, g = '';
      var mx = Math.max.apply(null, Pt.concat(q)), sc = 140 / mx; for (var i = 0; i < n; i++) { var x0 = 50 + i * bw, hp = Pt[i] * sc, hq = q[i] * sc;
        g += '<rect x="' + n1(x0 + bw * 0.18) + '" y="' + n1(170 - hp) + '" width="' + n1(bw * 0.3) + '" height="' + n1(hp) + '" fill="' + BL + '"/>' + '<rect x="' + n1(x0 + bw * 0.52) + '" y="' + n1(170 - hq) + '" width="' + n1(bw * 0.3) + '" height="' + n1(hq) + '" fill="' + OR + '"/>' + tx(x0 + bw / 2, 188, labs[i], 12); }
      g += ln(40, 170, W - 20, 170, GY) + '<rect x="50" y="6" width="12" height="10" fill="' + BL + '"/>' + tx(68, 15, '真實分布 P', 11, null, 'start') + '<rect x="160" y="6" width="12" height="10" fill="' + OR + '"/>' + tx(178, 15, '模型 Q', 11, null, 'start');
      view.innerHTML = svgw('0 0 ' + W + ' ' + Hh, g);
      inf.innerHTML = '真實分布的熵 H(P) = <b>' + f2(H) + '</b> 位元（最佳編碼的平均長度）。' +
        '<br>交叉熵 H(P, Q) = <b>' + f2(CE) + '</b> 位元：如果你<b>以為</b>分布是 Q、照 Q 設計編碼，實際平均要花的位元數。' +
        '<br>KL 散度 D(P‖Q) = H(P, Q) − H(P) = <b>' + f2(KL) + '</b> 位元：猜錯分布所多付的代價。' + (KL < 0.005 ? '模型完全正確時，KL = 0。' : '它永遠 ≥ 0，只有在 Q = P 時才等於 0。'); }
    us.forEach(function (u) { u(); });
  }

  function initAll() { document.querySelectorAll('.inf-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ binent: initBin, huff: initHuff, chan: initChan, kl: initKL })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"📡", INF_NOTE, INFLIB, "inf-w")

BINENT = ifw({"t": "binent", "q": u"一枚硬幣的熵：越難預測，資訊越多"})
HUFF = ifw({"t": "huff", "q": u"輸入任何文字，看它的熵與霍夫曼編碼", "text": u"she sells sea shells by the sea shore",
            "presets": [[u"英文句子", u"she sells sea shells by the sea shore"], [u"中文句子", u"資訊理論告訴我們資訊可以被量化，資訊的單位是位元"],
                        [u"重複的字", u"aaaaaaaaaaaaaaaaaaab"], [u"隨機字母", u"qzjxkvbwpfmyglcuhdrtsnoeia"]]})
CHAN = ifw({"t": "chan", "q": u"雜訊通道：重複碼與漢明碼能救回多少錯誤"})
KLW = ifw({"t": "kl", "q": u"交叉熵與 KL 散度：用錯的分布編碼要多付多少", "labels": [u"晴", u"多雲", u"雨", u"雪"],
           "p": [0.5, 0.25, 0.125, 0.125], "q0": [0.25, 0.25, 0.25, 0.25]})
