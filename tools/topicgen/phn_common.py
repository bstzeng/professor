# -*- coding: utf-8 -*-
"""〈電話系統全解析〉（phn_）共用：課程包裝、年表，以及 PHNLIB 互動元件（class="phn-w"）。"""
import json
from nv_common import *
from cc_common import wdg
from qt_common import BASEJS

lesson = nv_lesson(u"☎️", NOTE_SYS)


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


HISTORY = nvw({"t": "timeline", "q": u"電話系統的歷史（點一列看說明；可依類型篩選）：", "yw": 96, "mh": 560,
  "groups": [["a", u"類比與交換機", CO], ["d", u"數位與信令", CB], ["v", u"網路電話", CG], ["t", u"台灣", CR]],
  "ev": [ev(u"1876", u"貝爾的電話", u"3 月取得專利，幾天後打出第一通電話：「華生先生，過來，我要見你。」", "a"),
         ev(u"1878", u"第一座商用交換機", u"美國康乃狄克州紐哈芬，由接線生用插線把用戶接起來。", "a"),
         ev(u"1891", u"史端喬的自動交換機", u"用戶撥號就能自動接通，不再需要接線生。", "a"),
         ev(u"1962", u"T1 數位傳輸", u"把多通電話數位化，放在同一條線上傳送。", "d"),
         ev(u"1963", u"按鍵式電話（DTMF）", u"每個按鍵發出兩個頻率組成的聲音。", "d"),
         ev(u"1965", u"程式控制交換機", u"交換機由電腦程式控制，可以加入轉接、保留等新功能。", "d"),
         ev(u"1980 年代", u"7 號信令（SS7）", u"信令與語音分開，在專用的網路上傳送。", "d"),
         ev(u"1996", u"H.323", u"最早被廣泛使用的網路電話標準之一。", "v"),
         ev(u"1999", u"SIP；Asterisk", u"SIP 協定第一版發表（2002 年修訂為 RFC 3261）；開放原始碼的總機軟體 Asterisk 誕生。", "v"),
         ev(u"2003", u"Skype", u"網路電話進入一般家庭。", "v"),
         ev(u"2011", u"WebRTC", u"在瀏覽器裡直接通話，不必安裝軟體。", "v"),
         ev(u"2005", u"台灣手機號碼可攜", u"換電信業者可以保留原來的手機號碼。", "t"),
         ev(u"2017～2018", u"台灣關閉 2G、3G", u"手機語音全面轉向 4G 的 VoLTE。", "t"),
         ev(u"2023", u"中華電信終止 0204", u"2023 年 10 月 31 日起停止提供 0204 付費語音資訊服務。", "t")]})


PHNLIB = r"""
(function () {
  if (window.__phnLib) return; window.__phnLib = 1;
""" + BASEJS + r"""
  function box(css) { return el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em;' + (css || '')); }

  /* ---------- 取樣與量化 ---------- */
  function initPcm(root, cfg) { head(root, cfg.q); var P = { f: 1000, fs: 8000, b: 8 };
    var bar = el('div', 'margin:4px 0'); [[4000, '4 kHz'], [8000, '8 kHz（電話）'], [16000, '16 kHz（高清語音）'], [44100, '44.1 kHz（CD）']].forEach(function (o) { var x = btn(o[1], o[0]); x.onclick = function () { P.fs = o[0]; mark(bar, o[0]); draw(); }; bar.appendChild(x); }); root.appendChild(bar); mark(bar, 8000);
    var u1 = slider(root, '聲音的頻率', 200, 5000, 100, P.f, function (x) { return x + ' Hz'; }, null, function (x) { P.f = x; draw(); });
    var u2 = slider(root, '每個樣本的位元數', 2, 8, 1, P.b, function (x) { return x + ' 位元（' + Math.pow(2, x) + ' 個等級）'; }, null, function (x) { P.b = x; draw(); });
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function draw() { var W = 640, H = 200, T = 2, X = function (t) { return 30 + t / T * 590; }, Y = function (v) { return 100 - v * 80; }, o = '';
      o += '<line x1="30" y1="100" x2="620" y2="100" stroke="var(--border)"/>';
      var d = ''; for (var i = 0; i <= 400; i++) { var t = i / 400 * T; d += (i ? 'L' : 'M') + n1(X(t)) + ',' + n1(Y(Math.sin(2 * Math.PI * P.f * t / 1000))); } o += '<path d="' + d + '" fill="none" stroke="#3a6ea5" stroke-width="2"/>';
      var L = Math.pow(2, P.b), dt = 1000 / P.fs, s = '', pts = '';
      for (var t = 0, k = 0; t <= T + 1e-9; t += dt, k++) { var v = Math.sin(2 * Math.PI * P.f * t / 1000), q = Math.round((v + 1) / 2 * (L - 1)) / (L - 1) * 2 - 1;
        var x1 = X(t), x2 = X(Math.min(T, t + dt)); s += (k ? 'L' + n1(x1) + ',' + n1(Y(q)) : 'M' + n1(x1) + ',' + n1(Y(q))) + 'L' + n1(x2) + ',' + n1(Y(q));
        if (P.fs <= 16000) pts += '<circle cx="' + n1(x1) + '" cy="' + n1(Y(q)) + '" r="3" fill="#d9822b"/>'; }
      o += '<path d="' + s + '" fill="none" stroke="#d9822b" stroke-width="1.6" opacity="0.85"/>' + pts;
      o += tx(325, 196, '時間（0～2 毫秒）', 11, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 640 200', o);
      var rate = P.fs * P.b, ali = P.f > P.fs / 2;
      inf.innerHTML = '藍線：原本的聲音；橘線：取樣並量化後的數位訊號。<br>位元率 = ' + P.fs.toLocaleString() + ' 次／秒 × ' + P.b + ' 位元 = <b>' + (rate / 1000).toFixed(1) + ' kbps</b>' + (P.fs === 8000 && P.b === 8 ? '——這正是傳統數位電話一路通話的 64 kbps。' : '。') +
        (ali ? '<br><b style="color:#d0564f">取樣太慢了！</b>聲音頻率超過取樣率的一半（' + (P.fs / 2) + ' Hz），還原出來的會是錯誤的低頻聲音（混疊）。電話只傳 300～3,400 Hz，所以 8 kHz 取樣就夠了。' : '<br>取樣率至少要是聲音最高頻率的兩倍（取樣定理）。') +
        (P.b <= 4 ? '<br>位元數太少，量化的誤差很大，聽起來會有明顯的雜音。' : ''); }
    u1(); u2();
  }

  /* ---------- 按鍵音 DTMF ---------- */
  function initDtmf(root, cfg) { head(root, cfg.q); var R = [697, 770, 852, 941], C = [1209, 1336, 1477, 1633], K = [['1', '2', '3', 'A'], ['4', '5', '6', 'B'], ['7', '8', '9', 'C'], ['*', '0', '#', 'D']];
    var g = el('div', 'display:grid;grid-template-columns:70px repeat(4,1fr);gap:6px;max-width:420px'), inf = box(), ac = null;
    g.appendChild(el('div')); C.forEach(function (c) { g.appendChild(el('div', 'text-align:center;font-size:0.8em;color:var(--text-muted)', c + ' Hz')); });
    R.forEach(function (r, i) { g.appendChild(el('div', 'font-size:0.8em;color:var(--text-muted);align-self:center', r + ' Hz'));
      C.forEach(function (c, j) { var b = btn(K[i][j]); b.style.cssText += ';padding:10px 0;font-size:1.1em;' + (j === 3 ? 'opacity:0.6' : ''); b.onclick = function () { play(r, c); inf.innerHTML = '按鍵 <b>' + K[i][j] + '</b> = 低頻 <b>' + r + ' Hz</b> ＋ 高頻 <b>' + c + ' Hz</b> 同時發出。<br>交換機或語音選單只要聽出這兩個頻率，就知道你按了哪一個鍵。' + (j === 3 ? '<br>A、B、C、D 這一欄在一般電話上沒有，主要用於軍方與專業設備。' : ''); }; g.appendChild(b); }); });
    root.appendChild(g); root.appendChild(inf); inf.innerHTML = '點一個按鍵，看看它由哪兩個頻率組成（瀏覽器允許的話，也會發出聲音）。';
    function play(a, b) { try { ac = ac || new (window.AudioContext || window.webkitAudioContext)(); var gn = ac.createGain(); gn.gain.value = 0.08; gn.connect(ac.destination);
        [a, b].forEach(function (f) { var o = ac.createOscillator(); o.frequency.value = f; o.connect(gn); o.start(); o.stop(ac.currentTime + 0.25); }); } catch (e) {} }
  }

  /* ---------- SIP 時序圖 ---------- */
  function initSip(root, cfg) { head(root, cfg.q); var sc = 0, st = 0;
    var bar = el('div', 'margin:4px 0'); cfg.sc.forEach(function (s, i) { var x = btn(s.n, i); x.onclick = function () { sc = i; st = 0; mark(bar, i); draw(); }; bar.appendChild(x); }); if (cfg.sc.length > 1) root.appendChild(bar); mark(bar, 0);
    var nav = el('div', 'margin:4px 0'), bp = btn('◀ 上一步'), bn = btn('下一步 ▶'), ba = btn('全部顯示'), br = btn('重來'); [bp, bn, ba, br].forEach(function (b) { nav.appendChild(b); }); root.appendChild(nav);
    bp.onclick = function () { if (st > 0) st--; draw(); }; bn.onclick = function () { if (st < cfg.sc[sc].m.length) st++; draw(); }; ba.onclick = function () { st = cfg.sc[sc].m.length; draw(); }; br.onclick = function () { st = 0; draw(); };
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function draw() { var S = cfg.sc[sc], n = S.p.length, xs = [], rh = 30, H = 46 + S.m.length * rh + 10, o = '';
      for (var i = 0; i < n; i++) xs.push(n === 1 ? 320 : 70 + i * 500 / (n - 1));
      xs.forEach(function (x, i) { o += '<rect x="' + (x - 52) + '" y="6" width="104" height="26" rx="6" fill="var(--accent-soft)" stroke="var(--border)"/>' + tx(x, 24, S.p[i], 12, 'var(--text)') + '<line x1="' + x + '" y1="32" x2="' + x + '" y2="' + (H - 4) + '" stroke="var(--border)" stroke-dasharray="3 3"/>'; });
      S.m.forEach(function (m, k) { if (k >= st) return; var y = 50 + k * rh, a = xs[m[0]], b = xs[m[1]], cur = k === st - 1, media = m[4] === 'm', c = media ? '#4a9a5e' : (cur ? '#d0564f' : '#3a6ea5'), dir = b > a ? 1 : -1;
        o += '<line x1="' + a + '" y1="' + y + '" x2="' + (b - dir * 6) + '" y2="' + y + '" stroke="' + c + '" stroke-width="' + (cur ? 2.4 : 1.6) + '"' + (media ? ' stroke-dasharray="6 4"' : '') + '/>';
        o += '<path d="M' + b + ',' + y + ' l' + (-dir * 8) + ',-4 l0,8 z" fill="' + c + '"/>';
        if (media) o += '<path d="M' + a + ',' + y + ' l' + (dir * 8) + ',-4 l0,8 z" fill="' + c + '"/>';
        o += tx((a + b) / 2, y - 5, m[2], 11, c); });
      view.innerHTML = svgw('0 0 640 ' + H, o);
      inf.innerHTML = st === 0 ? (S.d || '按「下一步」，一則一則地看訊息。') : '<b>第 ' + st + ' 步：' + S.m[st - 1][2] + '</b><br>' + S.m[st - 1][3] + (st === S.m.length && S.e ? '<br><br>' + S.e : ''); }
    draw();
  }

  /* ---------- 兩段通話 ---------- */
  function initLegs(root, cfg) { head(root, cfg.q); var st = 0;
    var bar = el('div', 'margin:4px 0'); cfg.s.forEach(function (s, i) { var x = btn((i + 1) + '. ' + s.n, i); x.onclick = function () { st = i; mark(bar, i); draw(); }; bar.appendChild(x); }); root.appendChild(bar); mark(bar, 0);
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    var N = { A: [80, 130], S: [320, 130], B: [560, 60], C: [560, 200] };
    function draw() { var S = cfg.s[st], o = '';
      S.l.forEach(function (l) { var a = N[l[0]], b = N[l[1]], c = l[2] === 'a' ? '#3a6ea5' : l[2] === 'h' ? '#b8941f' : l[2] === 'x' ? '#bbb' : '#4a9a5e';
        o += '<line x1="' + a[0] + '" y1="' + a[1] + '" x2="' + b[0] + '" y2="' + b[1] + '" stroke="' + c + '" stroke-width="' + (l[2] === 'x' ? 2 : 5) + '"' + (l[2] === 'x' ? ' stroke-dasharray="6 5"' : '') + ' stroke-linecap="round"/>';
        o += tx((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 - 10, l[3], 11, c); });
      [['A', '來電者 A'], ['B', '客服 B'], ['C', '專員 C']].forEach(function (p) { var q = N[p[0]], on = S.on.indexOf(p[0]) >= 0;
        o += '<circle cx="' + q[0] + '" cy="' + q[1] + '" r="24" fill="' + (on ? 'var(--accent-soft)' : 'var(--surface)') + '" stroke="' + (on ? '#3a6ea5' : 'var(--border)') + '" stroke-width="2"/>' + tx(q[0], q[1] + 5, p[0], 16, 'var(--text)') + tx(q[0], q[1] + 42, p[1], 11, 'var(--text-muted)'); });
      o += '<rect x="262" y="104" width="116" height="52" rx="8" fill="#fdf3e0" stroke="#d9822b" stroke-width="2"/>' + tx(320, 126, '交換機', 13, '#8a5a1a') + tx(320, 144, '（PBX）', 11, '#8a5a1a');
      if (S.mu) o += tx(200, 160, '♪ 等候音樂', 12, '#b8941f');
      view.innerHTML = svgw('0 0 640 250', o); inf.innerHTML = S.d; }
    draw();
  }

  /* ---------- 語音選單 ---------- */
  function initIvr(root, cfg) { head(root, cfg.q); var D = 0, path = [], sec = 0, node;
    var bar = el('div', 'margin:4px 0'); cfg.d.forEach(function (d, i) { var x = btn(d.n, i); x.onclick = function () { D = i; mark(bar, i); reset(); }; bar.appendChild(x); }); root.appendChild(bar); mark(bar, 0);
    var wrap = el('div', 'display:flex;gap:12px;flex-wrap:wrap;align-items:flex-start'), pad = el('div', 'display:grid;grid-template-columns:repeat(3,52px);gap:6px'), scr = el('div', 'flex:1;min-width:220px;padding:10px 12px;border-radius:8px;border:1px solid var(--border);line-height:1.7;font-size:0.93em');
    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '0', '#'].forEach(function (k) { var b = btn(k); b.style.cssText += ';padding:10px 0;font-size:1.1em'; b.onclick = function () { press(k); }; pad.appendChild(b); });
    wrap.appendChild(pad); wrap.appendChild(scr); root.appendChild(wrap); var inf = box(); root.appendChild(inf);
    function say(t) { sec += Math.ceil(t.replace(/<[^>]+>/g, '').length / 4); }
    function reset() { path = []; sec = 0; node = cfg.d[D].m; say(node.p); show(''); }
    function press(k) { if (node.end) return; var g = cfg.d[D].g || {};
      if (g[k] && !(node.o && node.o[k])) { var t = g[k]; if (t === 'back') { if (path.length) { path.pop(); node = cfg.d[D].m; path.forEach(function (p) { node = node.o[p]; }); } say(node.p); show('回到上一層。'); return; } if (t === 'repeat') { say(node.p); show('重聽一次。'); return; } node = t; path.push(k); say(node.p); show(''); return; }
      if (node.any && /[0-9]/.test(k)) { path.push(k); sec += 1; show('（輸入中……）'); return; }
      if ((!node.o || !node.o[k]) && node.k && node.k.indexOf(k) >= 0 && node.x) { path.push(k); node = node.x; say(node.p); show(''); return; }
      if (!node.o || !node.o[k]) { say('輸入錯誤，請重新輸入。'); show('<span style="color:#d0564f">輸入錯誤，請重新輸入。</span>'); return; }
      path.push(k); node = node.o[k]; say(node.p); show(''); }
    function show(msg) { scr.innerHTML = (msg ? msg + '<br>' : '') + '🔊 ' + node.p + (node.end ? '<br><b>' + node.end + '</b>' : '');
      inf.innerHTML = '按鍵路徑：<b>' + (path.join(' → ') || '（剛撥通）') + '</b>　｜　聽語音大約花了 <b>' + sec + ' 秒</b>' + (sec > 60 ? '<br><span style="color:#d0564f">已經超過一分鐘了——很多來電者會在這時候直接掛斷。</span>' : '') + '<br><span style="font-size:0.88em;color:var(--text-muted)">' + (cfg.d[D].h || '') + '</span>'; }
    reset();
  }

  /* ---------- 話務中心人力（Erlang C） ---------- */
  function initErl(root, cfg) { head(root, cfg.q); var P = { c: 300, h: 240, t: 20, s: 80 };
    var u1 = slider(root, '每小時來電數', 30, 1500, 10, P.c, function (x) { return x + ' 通'; }, null, function (x) { P.c = x; draw(); });
    var u2 = slider(root, '平均處理時間', 60, 900, 10, P.h, function (x) { return Math.floor(x / 60) + ' 分 ' + (x % 60) + ' 秒'; }, null, function (x) { P.h = x; draw(); });
    var u3 = slider(root, '目標：多少秒內接起', 5, 60, 5, P.t, function (x) { return x + ' 秒'; }, null, function (x) { P.t = x; draw(); });
    var u4 = slider(root, '目標：接起的比例', 60, 95, 5, P.s, function (x) { return x + '%'; }, null, function (x) { P.s = x; draw(); });
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function ec(N, A) { var B = 1; for (var k = 1; k <= N; k++) B = A * B / (k + A * B); return N * B / (N - A * (1 - B)); }
    function draw() { var A = P.c * P.h / 3600, n0 = Math.floor(A) + 1, best = -1, h = '<table style="width:100%;border-collapse:collapse;font-size:0.9em"><tr><th style="text-align:left;padding:4px">人數</th><th>需要等待的機率</th><th>' + P.t + ' 秒內接起</th><th>平均等待</th><th>忙碌程度</th></tr>';
      for (var N = n0; N < n0 + 10; N++) { var pw = ec(N, A), sl = 1 - pw * Math.exp(-(N - A) * P.t / P.h), asa = pw * P.h / (N - A), ok = sl * 100 >= P.s; if (ok && best < 0) best = N;
        h += '<tr style="' + (N === best ? 'background:var(--accent-soft);font-weight:bold' : '') + '"><td style="padding:4px;border-top:1px solid var(--border)">' + N + ' 人</td><td style="text-align:center;border-top:1px solid var(--border)">' + (pw * 100).toFixed(1) + '%</td><td style="text-align:center;border-top:1px solid var(--border);color:' + (ok ? '#4a9a5e' : '#d0564f') + '">' + (sl * 100).toFixed(1) + '%</td><td style="text-align:center;border-top:1px solid var(--border)">' + asa.toFixed(1) + ' 秒</td><td style="text-align:center;border-top:1px solid var(--border)">' + (A / N * 100).toFixed(0) + '%</td></tr>'; }
      view.innerHTML = h + '</table>';
      inf.innerHTML = '話務量 A = 每小時來電數 × 平均處理時間 ÷ 3600 = <b>' + A.toFixed(1) + ' 厄朗</b>（相當於平均同時有 ' + A.toFixed(1) + ' 通電話在進行）。<br>' + (best > 0 ? '要達到「' + P.s + '% 的來電在 ' + P.t + ' 秒內接起」，至少需要 <b>' + best + ' 人</b>同時在線。' : '表中的人數還不夠，請降低目標或增加人力。') +
        '<br>注意：人數只比話務量多一點點時，等待會非常長；再多加幾個人，等待就急劇縮短。這就是為什麼話務中心不能讓每個人都接近 100% 忙碌。<br><span style="font-size:0.88em;color:var(--text-muted)">使用 Erlang C 模型：假設來電隨機到達、來電者不會放棄等待。實務上還要再加上休息、訓練等「排班損耗」。</span>'; }
    u1(); u2(); u3(); u4();
  }

  /* ---------- 0204 計費 ---------- */
  function initPrem(root, cfg) { head(root, cfg.q); var P = { r: 60, m: 6, s: 50 };
    var u1 = slider(root, '節目費率（每分鐘）', 10, 100, 5, P.r, function (x) { return x + ' 元'; }, null, function (x) { P.r = x; draw(); });
    var u2 = slider(root, '通話時間', 0, 20, 0.5, P.m, function (x) { return x + ' 分鐘'; }, null, function (x) { P.m = x; draw(); });
    var u3 = slider(root, '內容業者分到的比例（假設）', 20, 80, 5, P.s, function (x) { return x + '%'; }, null, function (x) { P.s = x; draw(); });
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function draw() { var pre = 20, sec = P.m * 60, capT = pre + 500 / P.r * 60, end = Math.min(sec, capT), fee = Math.max(0, end - pre) / 60 * P.r; fee = Math.min(500, fee);
      var W = 580, x = function (t) { return 30 + t / 1200 * W; }, o = '';
      o += '<rect x="' + x(0) + '" y="40" width="' + (x(pre) - x(0)) + '" height="26" fill="#4a9a5e"/>' + tx((x(0) + x(pre)) / 2, 34, '免費前言', 11, '#4a9a5e');
      if (end > pre) o += '<rect x="' + x(pre) + '" y="40" width="' + (x(end) - x(pre)) + '" height="26" fill="#d9822b"/>';
      if (capT <= 1200) o += '<line x1="' + x(capT) + '" y1="30" x2="' + x(capT) + '" y2="80" stroke="#d0564f" stroke-width="2"/>' + tx(x(capT), 94, '500 元上限：強制斷話', 11, '#d0564f');
      for (var t = 0; t <= 1200; t += 300) o += tx(x(t), 112, (t / 60) + ' 分', 10, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 640 120', o);
      var cut = sec > capT;
      inf.innerHTML = '這通電話的費用：<b>' + Math.round(fee) + ' 元</b>' + (cut ? '（在 ' + Math.floor(capT / 60) + ' 分 ' + Math.round(capT % 60) + ' 秒時達到 500 元上限，<b>被強制斷話</b>）' : '') + '。<br>以每分鐘 ' + P.r + ' 元計，最多大約講 ' + (capT / 60).toFixed(1) + ' 分鐘就會被斷線。<br>假設內容業者分到 ' + P.s + '%：業者收入約 <b>' + Math.round(fee * P.s / 100) + ' 元</b>，電信業者約 <b>' + Math.round(fee * (100 - P.s) / 100) + ' 元</b>。<br><span style="font-size:0.88em;color:var(--text-muted)">費率上限依 NCC 公布的規定：每分鐘最高 100 元、每通最高 500 元；前言約 20 秒免費。實際的計費單位與分成比例依合約而定，這裡為示意。</span>'; }
    u1(); u2(); u3();
  }

  function initAll() { document.querySelectorAll('.phn-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ pcm: initPcm, dtmf: initDtmf, sip: initSip, legs: initLegs, ivr: initIvr, erl: initErl, prem: initPrem })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def pw(cfg):
    w = wdg("phn-w", cfg)
    return ("raw", w[1] + u"<script>%s</script>" % PHNLIB)


PCM = pw({"t": "pcm", "q": u"把聲音變成數字：調整取樣率與位元數，看看數位化的結果："})
DTMF = pw({"t": "dtmf", "q": u"按鍵音（DTMF）：每個按鍵都是兩個頻率的組合："})


def M(a, b, label, note, kind="s"):
    return [a, b, label, note, kind]

SC_BASIC = {"n": u"一般通話", "p": [u"A 的電話", u"SIP 代理伺服器", u"B 的電話"],
  "d": u"A 撥電話給 B。所有的信令都經過代理伺服器；聲音則直接在兩支電話之間傳送。按「下一步」開始。",
  "m": [M(0, 1, u"INVITE（附 SDP）", u"A 發出邀請：「我要打給 B」。訊息中的 SDP 寫著 A 的 IP 位址、接收聲音的連接埠，以及 A 支援的語音編碼。"),
        M(1, 0, u"100 Trying", u"代理伺服器回覆：「收到了，正在處理」，避免 A 一直重送。"),
        M(1, 2, u"INVITE", u"代理伺服器查詢 B 目前註冊在哪裡，把邀請轉送給 B。"),
        M(2, 1, u"180 Ringing", u"B 的電話開始響鈴。"),
        M(1, 0, u"180 Ringing", u"A 聽到回鈴音（嘟——嘟——）。"),
        M(2, 1, u"200 OK（附 SDP）", u"B 接起電話。回覆中的 SDP 寫著 B 的位址、連接埠與選定的編碼——雙方「談好了條件」。"),
        M(1, 0, u"200 OK", u"代理伺服器把 B 的回覆轉給 A。"),
        M(0, 2, u"ACK", u"A 確認收到。三方交握完成，通話建立。"),
        M(0, 2, u"RTP 語音（雙向）", u"聲音以 RTP 封包，直接在 A 與 B 之間傳送，不經過代理伺服器。", "m"),
        M(2, 0, u"BYE", u"B 掛斷電話。"),
        M(0, 2, u"200 OK", u"A 確認，通話結束。")],
  "e": u"重點：<b>信令</b>（INVITE、200 OK、BYE……）和<b>聲音</b>（RTP）走的是不同的路。這是理解保留與轉接的關鍵。"}

SC_HOLD = {"n": u"保留與恢復", "p": [u"A 的電話", u"B 的電話"],
  "d": u"A 和 B 正在通話。B 按下「保留」。保留並不是斷線，而是重新談一次條件。",
  "m": [M(0, 1, u"RTP 語音（雙向）", u"通話進行中。", "m"),
        M(1, 0, u"re-INVITE（a=sendonly）", u"B 發出新的 INVITE（在同一通電話中，所以叫 re-INVITE），SDP 寫著 sendonly：「我只送、不收」。B 可能送出等候音樂，或什麼都不送。"),
        M(0, 1, u"200 OK（a=recvonly）", u"A 同意：「好，我只收」。"),
        M(1, 0, u"ACK", u"確認。這通電話仍然存在，只是聲音的方向改變了。"),
        M(1, 0, u"等候音樂（單向）", u"A 聽到等候音樂。", "m"),
        M(1, 0, u"re-INVITE（a=sendrecv）", u"B 按下「恢復」：再談一次條件，恢復雙向。"),
        M(0, 1, u"200 OK（a=sendrecv）", u"A 同意。"),
        M(1, 0, u"ACK", u"確認。"),
        M(0, 1, u"RTP 語音（雙向）", u"恢復通話。", "m")],
  "e": u"保留的本質：<b>同一通電話、同一組信令對話</b>，只是用 re-INVITE 改變了媒體的方向。所以保留不會斷線。"}

SC_BLIND = {"n": u"直接轉接（REFER）", "p": [u"來電者 A", u"客服 B", u"專員 C"],
  "d": u"A 打給客服 B，B 要把 A 直接轉給專員 C。在 SIP 中，B 會「請 A 自己去撥給 C」。",
  "m": [M(0, 1, u"RTP 語音（A↔B）", u"A 與 B 通話中。", "m"),
        M(1, 0, u"re-INVITE（保留）", u"B 先把 A 保留。"),
        M(0, 1, u"200 OK", u"A 同意被保留。"),
        M(1, 0, u"REFER（Refer-To: C）", u"B 送出 REFER：「請你去撥給 C」。"),
        M(0, 1, u"202 Accepted", u"A 的電話同意照做。"),
        M(0, 2, u"INVITE", u"A 的電話自動發出新的 INVITE 給 C——這是一通<b>新的</b>電話，但 A 的使用者不需要做任何事。"),
        M(0, 1, u"NOTIFY（180 Ringing）", u"A 回報 B：「C 正在響鈴」。"),
        M(2, 0, u"200 OK", u"C 接起電話。"),
        M(0, 2, u"ACK", u"A 與 C 的通話建立。"),
        M(0, 2, u"RTP 語音（A↔C）", u"A 和 C 開始通話。", "m"),
        M(0, 1, u"NOTIFY（200 OK）", u"A 回報 B：「轉接成功」。"),
        M(1, 0, u"BYE", u"B 掛掉自己與 A 的那通電話。"),
        M(0, 1, u"200 OK", u"轉接完成。")],
  "e": u"A 的使用者覺得電話「沒有斷」，因為在 A 與 B 的通話結束之前，A 與 C 的通話就已經接上了；而且是電話機自動完成的。"}

SC_ATT = {"n": u"先問再轉（Replaces）", "p": [u"來電者 A", u"客服 B", u"專員 C"],
  "d": u"B 先打給 C 說明情況（諮詢），再把 A 轉過去。關鍵是 Replaces：讓 A 的新電話「取代」B 與 C 的那通電話。",
  "m": [M(0, 1, u"RTP 語音（A↔B）", u"A 與 B 通話中。", "m"),
        M(1, 0, u"re-INVITE（保留）", u"B 把 A 保留。A 聽到等候音樂。"),
        M(1, 2, u"INVITE（諮詢）", u"B 另外撥一通電話給 C。"),
        M(2, 1, u"200 OK", u"C 接起。"),
        M(1, 2, u"RTP 語音（B↔C）", u"B 對 C 說：「有一位客戶要找你，是關於……」", "m"),
        M(1, 0, u"REFER（Refer-To: C；Replaces=B↔C）", u"B 請 A 撥給 C，並附上 Replaces：「用你的新電話，取代我和 C 的那通」。"),
        M(0, 1, u"202 Accepted", u"A 同意。"),
        M(0, 2, u"INVITE（Replaces）", u"A 撥給 C，並說明要取代 B↔C 的通話。"),
        M(2, 0, u"200 OK", u"C 的電話自動接受——不會再響一次鈴。"),
        M(2, 1, u"BYE", u"C 自動掛掉被取代的 B↔C 通話。"),
        M(0, 2, u"RTP 語音（A↔C）", u"A 與 C 直接通話。", "m"),
        M(0, 1, u"NOTIFY（200 OK）", u"A 回報 B 轉接成功。"),
        M(1, 0, u"BYE", u"B 掛掉與 A 的通話。")],
  "e": u"Replaces 讓轉接看起來天衣無縫：C 不必再接一次電話，A 也不會聽到響鈴或斷線。"}

SC_B2B = {"n": u"總機在中間改接（B2BUA）", "p": [u"來電者 A", u"總機（B2BUA）", u"客服 B", u"專員 C"],
  "d": u"在大部分的企業總機中，總機是「背對背使用者代理」（B2BUA）：A 的電話只和總機通話，總機再另外打給 B。轉接時，只有總機另一側在變動。",
  "m": [M(0, 1, u"INVITE", u"A 打進來，A 的電話只跟總機建立通話（第 1 段）。"),
        M(1, 2, u"INVITE", u"總機另外打給 B（第 2 段）。"),
        M(2, 1, u"200 OK", u"B 接起。"),
        M(1, 0, u"200 OK", u"總機告訴 A：接通了。"),
        M(0, 2, u"語音（經總機橋接）", u"A 的聲音送到總機，總機轉送給 B；反之亦然。", "m"),
        M(2, 1, u"轉接要求（REFER 或按鍵）", u"B 要求把電話轉給 C。這個要求送給總機，而不是送給 A。"),
        M(1, 3, u"INVITE", u"總機打給 C（第 3 段）。"),
        M(3, 1, u"200 OK", u"C 接起。"),
        M(1, 2, u"BYE", u"總機掛掉與 B 的第 2 段。"),
        M(0, 3, u"語音（經總機橋接）", u"總機把第 1 段改接到第 3 段。A 的第 1 段<b>從頭到尾都沒有改變</b>。", "m")],
  "e": u"這就是「電話不會斷」最直接的原因：<b>A 的那一段通話一直接在總機上</b>，總機只是把另一端從 B 換成 C。A 的電話甚至不知道發生了轉接（最多收到一個 re-INVITE 更新來電顯示或媒體位址）。"}


def SIP(q, scs):
    return pw({"t": "sip", "q": q, "sc": scs})


LEGS = pw({"t": "legs", "q": u"一通電話其實是好幾段：看看轉接時，交換機怎麼把它們重新接起來：", "s": [
  {"n": u"通話中", "on": "AB", "l": [["A", "S", "a", u"第 1 段"], ["S", "B", "b", u"第 2 段"]], "d": u"A 打進客服中心。A 只和交換機之間有一段通話（第 1 段，藍色），交換機另外接到 B（第 2 段）。在交換機內部，這兩段被「橋接」在一起，所以 A 和 B 能互相聽到。"},
  {"n": u"B 按保留", "on": "B", "mu": 1, "l": [["A", "S", "h", u"第 1 段（聽音樂）"], ["S", "B", "b", u"第 2 段"]], "d": u"B 按下保留：交換機把第 1 段與第 2 段<b>分開</b>，改把等候音樂送進第 1 段。第 1 段仍然存在，A 沒有斷線。"},
  {"n": u"B 諮詢 C", "on": "BC", "mu": 1, "l": [["A", "S", "h", u"第 1 段（聽音樂）"], ["S", "B", "b", u"第 2 段"], ["S", "C", "c", u"第 3 段"]], "d": u"B 撥給 C：交換機建立第 3 段，把第 2 段與第 3 段橋接起來，讓 B 和 C 先講話。A 仍在聽音樂。"},
  {"n": u"完成轉接", "on": "AC", "l": [["A", "S", "a", u"第 1 段"], ["S", "B", "x", u"第 2 段已掛斷"], ["S", "C", "c", u"第 3 段"]], "d": u"B 按下轉接（或掛斷）：交換機把<b>第 1 段與第 3 段</b>橋接起來，然後結束第 2 段。<br><b>A 的第 1 段從頭到尾都沒有中斷</b>——這就是轉接時電話不會掛掉的原因。"}]})

_BAD = {"p": u"歡迎致電某某公司。本公司成立於二十年前，致力於提供最優質的服務。為了保障您的權益，本通話可能會被錄音。我們的服務項目有所調整，請仔細聆聽以下選項。帳務問題請按 1，產品資訊請按 2，維修服務請按 3，其他服務請按 4。", "k": "1234", "x": {"p": u"這個項目請上本公司網站查詢。謝謝您的來電。", "end": u"被請去看網站，電話被掛斷了。"}, "o": {
  "1": {"p": u"帳務問題。查詢帳單請按 1，繳費方式請按 2，帳單地址變更請按 3，其他帳務問題請按 4。", "k": "1234", "x": {"p": u"這個項目請上本公司網站查詢。謝謝您的來電。", "end": u"被請去看網站，電話被掛斷了。"}, "o": {
    "1": {"p": u"請輸入您的十位數客戶編號，再按井字鍵。", "any": 1, "o": {"#": {"p": u"您的帳單金額是一千兩百元。", "end": u"選單結束——但你本來只是想問一個帳單上看不懂的項目。"}}},
    "4": {"p": u"其他帳務問題，請上本公司網站查詢。謝謝您的來電。", "end": u"被請去看網站，電話被掛斷了。"}}},
  "3": {"p": u"維修服務。家用產品請按 1，商用產品請按 2。", "k": "12", "x": {"p": u"這個項目請上本公司網站查詢。謝謝您的來電。", "end": u"被請去看網站，電話被掛斷了。"}, "o": {"1": {"p": u"家用產品。電視請按 1，冰箱請按 2，洗衣機請按 3，冷氣請按 4，其他請按 5。", "k": "12345", "x": {"p": u"請輸入產品背面的十二位數序號，再按井字鍵。", "any": 1, "o": {"#": {"p": u"目前客服人員忙線中，請稍後再撥。", "end": u"輸入了一長串序號，最後還是沒有接到真人。"}}}, "o": {
    "5": {"p": u"目前客服人員忙線中，請稍後再撥。", "end": u"繞了三層，最後沒有接到真人。"}}}}},
  "4": {"p": u"目前客服人員忙線中，請稍後再撥。", "end": u"沒有接到真人。"}}}
_GOOD = {"p": u"某某公司，您好。帳務請按 1，維修請按 2，找客服人員請按 0。", "o": {
  "1": {"p": u"查帳單金額請按 1，其他帳務問題請按 0 轉接客服。", "o": {"1": {"p": u"您目前的帳單金額是一千兩百元，繳費期限是本月二十號。", "end": u"兩個按鍵就解決了。"}}},
  "2": {"p": u"已為您轉接維修專員，預計等候約兩分鐘。", "end": u"直接排進維修專員的佇列，並告知等候時間。"}}}
_GOODG = {"0": {"p": u"為您轉接客服人員，目前預計等候一分鐘。", "end": u"任何時候按 0 都能找到真人。"}, "*": "back", "#": "repeat"}

IVR = pw({"t": "ivr", "q": u"語音選單模擬器：用按鍵實際走一遍，比較兩種設計（試著「查帳單」或「找真人」）：", "d": [
  {"n": u"不好的設計", "m": _BAD, "h": u"問題：開場白太長、選項太多、層數太深、沒有「找真人」的捷徑、需要輸入很長的號碼。"},
  {"n": u"好的設計", "m": _GOOD, "g": _GOODG, "h": u"原則：開場白簡短、常用的選項放前面、每層不超過三到四個選項、隨時按 0 找真人、按 * 回上一層、按 # 重聽。"}]})

ERL = pw({"t": "erl", "q": u"話務中心需要幾個人？用 Erlang C 模型計算："})
PREM = pw({"t": "prem", "q": u"0204 這類付費語音的帳單怎麼算？（依 NCC 的上限規定示意）"})
