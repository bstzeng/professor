# -*- coding: utf-8 -*-
"""〈克里斯多福・諾蘭電影全紀錄〉（nol_）共用：課程包裝與 NOLLIB 互動元件（class="nol-w"）。

  dream    《全面啟動》夢境層級：每層時間倍率 → 各層經過的主觀時間
  dilate   《星際效應》重力時間膨脹：離黑洞多近 → 在那裡 1 小時等於外面多久
  memento  《記憶拼圖》：彩色倒敘與黑白順敘的場景，依電影順序或故事順序排列
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

NOL_NOTE = u"本課程包含完整劇情（有暴雷）。片名以台灣上映時的通行譯名為主；科學解說為教學用的簡化。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def lw(cfg, maxw=680):
    return wdg("nol-w", cfg, maxw)


NOLLIB = r"""
(function () {
  if (window.__nolLib) return; window.__nolLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function dur(h) { if (h < 1) return f1(h * 60) + ' 分鐘'; if (h < 48) return f1(h) + ' 小時'; var d = h / 24; if (d < 14) return f1(d) + ' 天'; if (d < 60) return f1(d / 7) + ' 週'; if (d < 730) return f1(d / 30.4) + ' 個月'; return f1(d / 365.25) + ' 年'; }

  var LV = ['現實（飛機上）', '第一層：雨中的城市', '第二層：飯店', '第三層：雪山堡壘', '混沌域（Limbo）'];
  function initDream(root, cfg) {
    head(root, cfg.q); var P = { h: 10, m: 20, n: 3 }, view = el('div'), inf;
    var us = [slider(root, '現實中的時間（小時）', 1, 20, 0.5, P.h, function (x) { return x + ' 小時'; }, null, function (x) { P.h = x; draw(); }),
      slider(root, '每深一層，時間變慢幾倍', 2, 30, 1, P.m, function (x) { return x + ' 倍'; }, null, function (x) { P.m = x; draw(); }),
      slider(root, '往下幾層', 1, 4, 1, P.n, function (x) { return x + ' 層'; }, null, function (x) { P.n = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var g = '', W = 640, rows = P.n + 1, lmax = Math.log10(P.h * Math.pow(P.m, P.n));
      for (var i = 0; i < rows; i++) { var t = P.h * Math.pow(P.m, i), y = 18 + i * 52, w = 40 + 460 * (Math.log10(t) + 0.3) / (lmax + 0.3);
        g += '<rect x="' + (110 + i * 6) + '" y="' + y + '" width="' + n1(Math.max(20, w)) + '" height="34" rx="6" fill="' + ['#6f8fb3', '#7aa37a', '#c9a26b', '#b5b5c8', '#8a6a9a'][i] + '" opacity="0.88"/>' +
          tx(100 + i * 6, y + 22, LV[i].split('：')[0], 11, 'currentColor', 'end') + tx(118 + i * 6, y + 22, dur(t), 12.5, '#fff', 'start'); }
      view.innerHTML = svgw('0 0 ' + W + ' ' + (rows * 52 + 20), g);
      inf.innerHTML = '現實中的 ' + P.h + ' 小時，在第 ' + P.n + ' 層會感覺像 <b>' + dur(P.h * Math.pow(P.m, P.n)) + '</b>。（長條是對數比例。）' +
        '<br>電影中，雪梨飛往洛杉磯的航班約 10 小時，藥效讓每一層的時間變慢約 20 倍：第一層約一週、第二層約六個月、第三層約十年。再往下的<b>混沌域</b>，時間幾乎無限——柯柏與梅兒在那裡度過了「五十年」。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">這是電影的設定，不是真實的睡眠科學：真實的夢與清醒時的時間流速大致相同。</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initDilate(root, cfg) {
    head(root, cfg.q); var P = { lx: -1 }, view = el('div'), inf;
    var b = bar(root); [['離黑洞很遠（20 倍半徑）', 1.3], ['距離視界 1 倍半徑', 0], ['非常接近視界', -4], ['米勒星球（1 小時 = 7 年）', -9.575]].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { set(o[1]); }; b.appendChild(x); });
    var u = slider(root, '離視界多近：log₁₀(r/r_s − 1)', -11, 2, 0.01, P.lx, function (x) { return f2(x); }, 'lx', function (x) { P.lx = x; draw(); });
    root.appendChild(view); inf = info(root);
    function set(v) { var s = root.querySelector('input[data-k="lx"]'); s.value = v; u(); }
    function F(lx) { var x = Math.pow(10, lx); return Math.sqrt((1 + x) / x); }
    function draw() { var d = []; for (var l = -11; l <= 2.001; l += 0.05) d.push([l, Math.log10(F(l))]);
      var f = F(P.lx), yrs = f / 24 / 365.25;
      view.innerHTML = chart(640, 240, [{ d: d, c: BL, n: 'log₁₀（時間變慢的倍數）', w: 2.2 }], { x0: -11, x1: 2, y0: 0, y1: 6, xl: '離視界越近 ←　log₁₀(r/r_s − 1)', pts: [{ x: P.lx, y: Math.log10(f), c: RD }], hl: [{ y: Math.log10(61320), c: OR, n: '米勒星球：約 61,000 倍' }] });
      inf.innerHTML = '在這裡的 <b>1 小時</b>，遠方的人經過了 <b>' + (f < 1.01 ? f2(f) + ' 小時（幾乎沒差）' : f < 24 * 3 ? f1(f) + ' 小時' : f < 24 * 365 ? f1(f / 24) + ' 天' : f1(yrs) + ' 年') + '</b>（時間變慢約 ' + (f < 1000 ? f2(f) : Math.round(f).toLocaleString()) + ' 倍）。' +
        '<br>靜止在史瓦西黑洞外半徑 r 處的時鐘，變慢的倍數是 1 / √(1 − r<sub>s</sub>/r)。要達到米勒星球的「1 小時 = 7 年」（約 61,000 倍），必須離視界<b>極近</b>。' +
        '<br>索恩在《星際效應》的科學解說中指出：靜止或繞行一般黑洞的星球不可能這麼近還保持穩定，所以巨人（Gargantua）必須是一個<b>幾乎以最大速度自轉</b>的黑洞（質量約一億個太陽）——自轉讓穩定的軌道可以極度靠近視界。質量巨大也讓潮汐力溫和，星球不會被撕碎（見〈黑洞〉）。'; }
    u();
  }

  function initMemento(root, cfg) {
    head(root, cfg.q); var P = { m: 0 }, view = el('div'), inf, N = 11;
    var b = bar(root); [['依電影的順序', 0], ['依故事發生的順序', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.m = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 0);
    root.appendChild(view); inf = info(root);
    function draw() { var film = [], story = [], i;
      for (i = 0; i < N; i++) { film.push(['C', N - i]); film.push(['B', i + 1]); }
      for (i = 1; i <= N; i++) story.push(['B', i]); for (i = 1; i <= N; i++) story.push(['C', i]);
      var seq = P.m ? story : film, g = '', w = 600 / seq.length;
      seq.forEach(function (s, k) { var x = 20 + k * w, col = s[0] === 'C' ? 'hsl(' + (20 + s[1] * 12) + ',70%,' + (45 + s[1] * 2) + '%)' : 'hsl(0,0%,' + (25 + s[1] * 4) + '%)';
        g += '<rect x="' + n1(x) + '" y="30" width="' + n1(w - 2) + '" height="60" rx="3" fill="' + col + '"/>' + tx(x + w / 2 - 1, 65, (s[0] === 'C' ? '彩' : '黑') + s[1], 9.5, '#fff'); });
      g += tx(20, 18, P.m ? '故事時間 →' : '電影播放 →', 11, 'var(--text-muted)', 'start');
      if (!P.m) g += '<path d="M' + n1(20 + (seq.length - 1) * w + w / 2) + ' 95 v12 H' + n1(20 + w * 1.5) + ' v-12" fill="none" stroke="' + RD + '" stroke-dasharray="4 3"/>' + tx(320, 122, '最後一段黑白場景轉成彩色，接上故事的中點', 10, RD);
      view.innerHTML = svgw('0 0 640 135', g);
      inf.innerHTML = (P.m ? '依故事的順序：先發生所有的<b>黑白</b>場景（藍納在汽車旅館講電話，順著時間進行），接著是所有的<b>彩色</b>場景。' :
          '依電影的順序：<b>彩色</b>場景（彩 11、彩 10……）是<b>倒著</b>播的——每一段都在前一段的開頭之前結束；中間穿插的<b>黑白</b>場景則是<b>順著</b>播的。兩條線在電影的結尾會合。') +
        '<br>彩色的倒敘，讓觀眾和失去短期記憶的主角一樣：每一段開始時，都不知道「剛才」發生了什麼。<span style="font-size:0.9em;color:var(--text-muted)">（示意圖：實際的場景數量更多。）</span>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.nol-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ dream: initDream, dilate: initDilate, memento: initMemento })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🎬", NOL_NOTE, NOLLIB, "nol-w")

DREAM = lw({"t": "dream", "q": u"《全面啟動》：夢中夢的時間"})
DILATE = lw({"t": "dilate", "q": u"《星際效應》：黑洞旁的一小時"})
MEMENTO = lw({"t": "memento", "q": u"《記憶拼圖》的結構：彩色倒敘、黑白順敘"})
