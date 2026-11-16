# -*- coding: utf-8 -*-
"""〈重力波〉（gwv_）共用：課程包裝與 GWVLIB 互動元件（class="gwv-w"）。

  chirp   雙黑洞合併的啾聲：兩個質量 → 啾聲質量、頻率與波形
  mf      匹配濾波：把訊號埋進雜訊，再用範本找出來
  mich    邁克生干涉儀：臂長差 → 輸出亮度
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

GWV_NOTE = (u"本課的推導以主要步驟為主，省略部分嚴格性；互動模擬使用牛頓近似（只到合併前），"
            u"數字為約略值，事件參數以 LIGO–Virgo–KAGRA 公開的論文為準。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def PAPER(text, ref):
    return u"%s（<span style=\"font-family:ui-monospace,Menlo,monospace;font-size:0.92em\">%s</span>）" % (text, ref)


def gww(cfg, maxw=680):
    return wdg("gwv-w", cfg, maxw)


GWVLIB = r"""
(function () {
  if (window.__gwvLib) return; window.__gwvLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function randn() { var u = 1 - Math.random(), v = Math.random(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  var TSUN = 4.925e-6;
  function freq(tau, Mc) { return Math.pow(5 / (256 * tau), 0.375) * Math.pow(Mc * TSUN, -0.625) / Math.PI; }
  function chirpWave(m1, m2, T, fs) { var M = m1 + m2, Mc = Math.pow(m1 * m2, 0.6) / Math.pow(M, 0.2), fisco = 1 / (Math.pow(6, 1.5) * Math.PI * M * TSUN), t = [], h = [], f = [], ph = 0, dt = 1 / fs;
    for (var i = 0; i < T * fs; i++) { var tau = T - i * dt + 1e-4, fr = freq(tau, Mc); if (fr > fisco) { t.push(i * dt); h.push(0); f.push(NaN); continue; } ph += 2 * Math.PI * fr * dt; t.push(i * dt); h.push(Math.pow(fr / 100, 2 / 3) * Math.cos(ph)); f.push(fr); }
    return { t: t, h: h, f: f, Mc: Mc, fisco: fisco, M: M }; }

  function initChirp(root, cfg) {
    head(root, cfg.q); var P = { m1: 36, m2: 29 }, view = el('div'), view2 = el('div'), inf;
    var us = [slider(root, '黑洞 1 的質量（太陽質量）', 1.2, 80, 0.1, P.m1, function (x) { return f1(x); }, null, function (x) { P.m1 = x; draw(); }),
      slider(root, '黑洞 2 的質量（太陽質量）', 1.2, 80, 0.1, P.m2, function (x) { return f1(x); }, null, function (x) { P.m2 = x; draw(); })];
    root.appendChild(view); root.appendChild(view2); inf = info(root);
    function draw() { var W = chirpWave(P.m1, P.m2, 0.5, 4096), d = [], fd = [];
      for (var i = 0; i < W.t.length; i += 2) { d.push([W.t[i] - 0.5, W.h[i]]); if (isFinite(W.f[i])) fd.push([W.t[i] - 0.5, W.f[i]]); }
      var ym = Math.max.apply(null, W.h.map(Math.abs)) * 1.1 || 1;
      view.innerHTML = chart(640, 190, [{ d: d, c: BL, n: '應變 h(t)（任意單位）', w: 1.2 }], { x0: -0.5, x1: 0, y0: -ym, y1: ym, xl: '距離合併的時間（秒）' });
      view2.innerHTML = chart(640, 170, [{ d: fd, c: RD, n: '重力波頻率（Hz）' }], { x0: -0.5, x1: 0, y0: 0, y1: Math.min(W.fisco * 1.1, 2000), xl: '距離合併的時間（秒）' });
      var t20 = 5 / 256 * Math.pow(Math.PI * 20, -8 / 3) * Math.pow(W.Mc * TSUN, -5 / 3);
      inf.innerHTML = '啾聲質量 𝓜 = (m₁m₂)<sup>3/5</sup>/(m₁+m₂)<sup>1/5</sup> = <b>' + f1(W.Mc) + '</b> 太陽質量。合併前的最高頻率約 <b>' + Math.round(W.fisco) + ' Hz</b>（最內穩定圓軌道）。' +
        '<br>從 20 Hz（LIGO 開始聽得到）到合併，訊號在偵測器中停留約 <b>' + (t20 < 1 ? f2(t20) + ' 秒' : t20 < 120 ? f1(t20) + ' 秒' : f1(t20 / 60) + ' 分鐘') + '</b>。' +
        '<br>頻率與振幅越來越快、越來越大，像一聲往上滑的鳥叫——所以叫「啾聲」。' + (P.m1 < 3 && P.m2 < 3 ? '<br>這是兩顆<b>中子星</b>的質量：訊號在偵測器中停留很久，頻率高到超出圖的範圍（GW170817 被追蹤了約 100 秒）。' : P.m1 + P.m2 > 100 ? '<br>總質量很大：合併的頻率很低，偵測器只聽得到最後幾個週期（例如 GW190521）。' : '');
    }
    us.forEach(function (u) { u(); });
  }

  function initMF(root, cfg) {
    head(root, cfg.q); var P = { snr: 12 }, view = el('div'), view2 = el('div'), inf;
    var u = slider(root, '訊號強度（最佳訊雜比）', 0, 25, 0.5, P.snr, function (x) { return f1(x); }, null, function (x) { P.snr = x; run(); });
    var b = el('div', 'margin:4px 0'), go = btn('重新產生雜訊'); go.onclick = run; b.appendChild(go); root.appendChild(b); root.appendChild(view); root.appendChild(view2); inf = info(root);
    var FS = 1024, N = 4096, tmpl = chirpWave(30, 30, 0.6, FS).h, L = tmpl.length, nrm = Math.sqrt(tmpl.reduce(function (a, v) { return a + v * v; }, 0));
    tmpl = tmpl.map(function (v) { return v / nrm; });
    function run() { var t0 = 1200 + Math.floor(Math.random() * 2000), data = []; for (var i = 0; i < N; i++) data.push(randn());
      for (i = 0; i < L; i++) data[t0 + i] += P.snr * tmpl[i];
      var out = [], best = 0, at = 0; for (var s = 0; s + L <= N; s += 2) { var c = 0; for (var k = 0; k < L; k += 1) c += data[s + k] * tmpl[k]; out.push([(s + L) / FS, c]); if (Math.abs(c) > best) { best = Math.abs(c); at = (s + L) / FS; } }
      var d = []; for (i = 0; i < N; i += 2) d.push([i / FS, data[i]]);
      view.innerHTML = chart(640, 170, [{ d: d, c: GY, n: '偵測器資料（雜訊＋可能藏著的訊號）', w: 0.8 }], { x0: 0, x1: N / FS, xl: '時間（秒）', vl: [{ x: (t0 + L) / FS, c: OR, n: '真正的合併時間' }] });
      view2.innerHTML = chart(640, 170, [{ d: out, c: BL, n: '匹配濾波輸出（訊雜比）', w: 1.2 }], { x0: 0, x1: N / FS, xl: '時間（秒）', hl: [{ y: 8, c: RD, n: '門檻 8' }] });
      inf.innerHTML = '上圖：肉眼完全看不出訊號在哪裡。下圖：把已知的波形範本沿著資料滑動、逐點相乘相加，在範本和訊號對齊的那一刻，輸出出現一個尖峰。' +
        '<br>最大的輸出值 <b>' + f1(best) + '</b>，出現在 ' + f2(at) + ' 秒（真正的合併在 ' + f2((t0 + L) / FS) + ' 秒）。' + (best > 8 && Math.abs(at - (t0 + L) / FS) < 0.05 ? '<b>找到了！</b>' : P.snr < 6 ? '訊號太弱，尖峰被雜訊的漲落淹沒。' : '') +
        '<br>純雜訊的輸出大約在 ±3 之間漲落，所以 LIGO 常把單一偵測器的門檻設在訊雜比約 8。GW150914 的訊雜比約 24。'; }
    u();
  }

  function initMich(root, cfg) {
    head(root, cfg.q); var P = { d: 0 }, view = el('div', 'max-width:520px;margin:0 auto'), inf;
    var u = slider(root, '兩臂的長度差（以雷射波長為單位）', -0.5, 0.5, 0.005, P.d, function (x) { return f2(x * 1000) / 1000 + ' λ'; }, null, function (x) { P.d = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var I = Math.pow(Math.sin(2 * Math.PI * P.d), 2), g = '', c = 'rgba(208,86,79,';
      g += '<rect x="20" y="150" width="50" height="30" rx="4" fill="' + OR + '"/>' + tx(45, 200, '雷射', 10, 'var(--text-muted)');
      g += '<line x1="70" y1="165" x2="200" y2="165" stroke="' + RD + '" stroke-width="3"/>';
      g += '<line x1="185" y1="150" x2="215" y2="180" stroke="var(--text-muted)" stroke-width="3"/>' + tx(200, 140, '分光鏡', 10, 'var(--text-muted)');
      var ex = 470 + P.d * 120; g += '<line x1="200" y1="165" x2="' + ex + '" y2="165" stroke="' + RD + '" stroke-width="3" opacity="0.8"/><rect x="' + ex + '" y="148" width="8" height="34" fill="' + BL + '"/>' + tx(470, 140, 'X 臂（4 公里）', 10, 'var(--text-muted)');
      g += '<line x1="200" y1="165" x2="200" y2="30" stroke="' + RD + '" stroke-width="3" opacity="0.8"/><rect x="183" y="22" width="34" height="8" fill="' + BL + '"/>' + tx(255, 30, 'Y 臂', 10, 'var(--text-muted)', 'start');
      g += '<line x1="200" y1="165" x2="200" y2="270" stroke="' + c + (0.15 + 0.85 * I) + ')" stroke-width="3"/>';
      g += '<circle cx="200" cy="290" r="18" fill="' + c + (0.08 + 0.9 * I) + ')" stroke="var(--border)"/>' + tx(240, 294, '光偵測器', 10, 'var(--text-muted)', 'start');
      view.innerHTML = svgw('0 0 560 320', g);
      inf.innerHTML = '輸出亮度 = sin²(2π × 長度差 / λ) = <b>' + Math.round(I * 1000) / 10 + '%</b>。' +
        '<br>兩臂等長時，從兩臂回來的光在偵測器處剛好<b>相消</b>，一片漆黑（「暗紋」）。重力波讓一臂伸長、另一臂縮短，光就漏出來一點點。' +
        '<br>LIGO 的雷射波長 1064 奈米；GW150914 只讓 4 公里的臂長改變約 4×10⁻¹⁸ 公尺——是波長的<b>約三千億分之一</b>。要量到這麼小的變化，靠的是共振腔、高功率雷射與極低的雜訊（模組 E）。'; }
    u();
  }

  function initAll() { document.querySelectorAll('.gwv-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ chirp: initChirp, mf: initMF, mich: initMich })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🌊", GWV_NOTE, GWVLIB, "gwv-w")

CHIRP = gww({"t": "chirp", "q": u"雙黑洞合併的啾聲：調整兩個黑洞的質量"})
MF = gww({"t": "mf", "q": u"匹配濾波：在雜訊中找出看不見的訊號"})
MICH = gww({"t": "mich", "q": u"邁克生干涉儀：臂長差一點點，光就漏出來"})
