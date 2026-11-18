# -*- coding: utf-8 -*-
"""系統類課程共用的 SYSLIB 互動元件（class="sys-w"）：
seq 時序圖步進器、luhn 卡號檢查碼、fee 手續費拆分、bgp 路由模擬、lat 傳輸延遲、curve 彎道超速、stab 船舶穩定性。"""
from cc_common import wdg
from qt_common import BASEJS

SYSLIB = r"""
(function () {
  if (window.__sysLib) return; window.__sysLib = 1;
""" + BASEJS + r"""
  function box() { return el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); }
  function cell(s, css) { return '<td style="padding:4px 6px;border-top:1px solid var(--border);' + (css || '') + '">' + s + '</td>'; }

  /* ---------- 時序圖 ---------- */
  function initSeq(root, cfg) { head(root, cfg.q); var sc = 0, st = 0;
    var bar = el('div', 'margin:4px 0'); cfg.sc.forEach(function (s, i) { var x = btn(s.n, i); x.onclick = function () { sc = i; st = 0; mark(bar, i); draw(); }; bar.appendChild(x); }); if (cfg.sc.length > 1) root.appendChild(bar); mark(bar, 0);
    var nav = el('div', 'margin:4px 0'), bp = btn('◀ 上一步'), bn = btn('下一步 ▶'), ba = btn('全部顯示'), br = btn('重來'); [bp, bn, ba, br].forEach(function (b) { nav.appendChild(b); }); root.appendChild(nav);
    bp.onclick = function () { if (st > 0) st--; draw(); }; bn.onclick = function () { if (st < cfg.sc[sc].m.length) st++; draw(); }; ba.onclick = function () { st = cfg.sc[sc].m.length; draw(); }; br.onclick = function () { st = 0; draw(); };
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function draw() { var S = cfg.sc[sc], n = S.p.length, xs = [], rh = 30, H = 46 + S.m.length * rh + 10, o = '', w = n > 4 ? 92 : 104;
      for (var i = 0; i < n; i++) xs.push(n === 1 ? 320 : 62 + i * 516 / (n - 1));
      xs.forEach(function (x, i) { o += '<rect x="' + (x - w / 2) + '" y="6" width="' + w + '" height="26" rx="6" fill="var(--accent-soft)" stroke="var(--border)"/>' + tx(x, 24, S.p[i], 11.5, 'var(--text)') + '<line x1="' + x + '" y1="32" x2="' + x + '" y2="' + (H - 4) + '" stroke="var(--border)" stroke-dasharray="3 3"/>'; });
      S.m.forEach(function (m, k) { if (k >= st) return; var y = 50 + k * rh, a = xs[m[0]], b = xs[m[1]], cur = k === st - 1, dash = m[4] === 'm', c = dash ? '#4a9a5e' : (cur ? '#d0564f' : '#3a6ea5');
        if (a === b) { o += '<rect x="' + (a - 60) + '" y="' + (y - 14) + '" width="120" height="20" rx="5" fill="' + (cur ? '#fde8e6' : 'var(--surface)') + '" stroke="' + c + '"/>' + tx(a, y, m[2], 10.5, c); return; }
        var dir = b > a ? 1 : -1;
        o += '<line x1="' + a + '" y1="' + y + '" x2="' + (b - dir * 6) + '" y2="' + y + '" stroke="' + c + '" stroke-width="' + (cur ? 2.4 : 1.6) + '"' + (dash ? ' stroke-dasharray="6 4"' : '') + '/>';
        o += '<path d="M' + b + ',' + y + ' l' + (-dir * 8) + ',-4 l0,8 z" fill="' + c + '"/>';
        if (dash && m[5]) o += '<path d="M' + a + ',' + y + ' l' + (dir * 8) + ',-4 l0,8 z" fill="' + c + '"/>';
        o += tx((a + b) / 2, y - 5, m[2], 10.5, c); });
      view.innerHTML = svgw('0 0 640 ' + H, o);
      inf.innerHTML = st === 0 ? (S.d || '按「下一步」，一步一步地看。') : '<b>第 ' + st + ' 步：' + S.m[st - 1][2] + '</b><br>' + S.m[st - 1][3] + (st === S.m.length && S.e ? '<br><br>' + S.e : ''); }
    draw();
  }

  /* ---------- 卡號檢查碼（Luhn） ---------- */
  function brand(d) { var s = d.join(''); if (/^4/.test(s)) return 'Visa'; if (/^(5[1-5]|2(2[2-9]|[3-6]\d|7[01]|720))/.test(s)) return 'Mastercard'; if (/^3[47]/.test(s)) return 'American Express'; if (/^35(2[89]|[3-8])/.test(s)) return 'JCB'; if (/^62/.test(s)) return '銀聯'; return '（無法判斷）'; }
  function initLuhn(root, cfg) { head(root, cfg.q); var inp = el('input'); inp.type = 'text'; inp.value = '4111 1111 1111 1111'; inp.style.cssText = 'width:100%;max-width:320px;padding:6px 8px;font-size:1.05em;border:1px solid var(--border);border-radius:6px;background:var(--surface);color:var(--text)';
    var bar = el('div', 'margin:6px 0'), b1 = btn('產生一組測試卡號'), b2 = btn('改錯一個數字'); bar.appendChild(b1); bar.appendChild(b2); root.appendChild(inp); root.appendChild(bar);
    var view = el('div', 'margin-top:6px;overflow-x:auto'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function chk(d) { var s = 0; for (var i = d.length - 1, k = 0; i >= 0; i--, k++) { var v = d[i]; if (k % 2 === 1) { v *= 2; if (v > 9) v -= 9; } s += v; } return s; }
    b1.onclick = function () { var d = [4]; for (var i = 0; i < 14; i++) d.push(Math.floor(Math.random() * 10)); var s = chk(d.concat([0])); d.push((10 - s % 10) % 10); inp.value = d.join('').replace(/(\d{4})(?=\d)/g, '$1 '); draw(); };
    b2.onclick = function () { var d = inp.value.replace(/\D/g, '').split(''); if (d.length < 2) return; var i = Math.floor(Math.random() * (d.length - 1)); d[i] = String((+d[i] + 1) % 10); inp.value = d.join('').replace(/(\d{4})(?=\d)/g, '$1 '); draw(); };
    inp.addEventListener('input', draw);
    function draw() { var d = inp.value.replace(/\D/g, '').split('').map(Number); if (d.length < 2) { view.innerHTML = ''; inf.innerHTML = '請輸入至少兩位數字。'; return; }
      var r1 = '', r2 = '', r3 = '', s = 0;
      for (var i = 0; i < d.length; i++) { var k = d.length - 1 - i, v = d[i], dbl = k % 2 === 1, w = v; if (dbl) { w = v * 2; if (w > 9) w -= 9; } s += w;
        var bg = dbl ? 'background:#fdf3e0' : ''; r1 += '<td style="text-align:center;padding:3px 5px;' + bg + '">' + v + '</td>'; r2 += '<td style="text-align:center;padding:3px 5px;color:var(--text-muted);' + bg + '">' + (dbl ? '×2' : '') + '</td>'; r3 += '<td style="text-align:center;padding:3px 5px;font-weight:bold;' + bg + '">' + w + '</td>'; }
      view.innerHTML = '<table style="border-collapse:collapse;font-size:0.92em"><tr><td style="padding:3px 6px;color:var(--text-muted)">數字</td>' + r1 + '</tr><tr><td style="padding:3px 6px;color:var(--text-muted)">處理</td>' + r2 + '</tr><tr><td style="padding:3px 6px;color:var(--text-muted)">結果</td>' + r3 + '</tr></table>';
      var ok = s % 10 === 0;
      inf.innerHTML = '從最右邊數來，每隔一位（橘色）乘以 2，超過 9 就減 9；全部加起來 = <b>' + s + '</b>。' + (ok ? '<b style="color:#4a9a5e">是 10 的倍數：檢查碼正確。</b>' : '<b style="color:#d0564f">不是 10 的倍數：這個卡號打錯了。</b>') +
        '<br>開頭判斷的卡組織：<b>' + brand(d) + '</b>；前 6～8 位是「發卡機構識別碼」（BIN），代表發卡的銀行與卡種。<br><span style="font-size:0.88em;color:var(--text-muted)">檢查碼只能抓出打錯字，不能證明卡片真的存在或可以使用。4111 1111 1111 1111 是業界常用的測試號碼，請勿輸入真實卡號。</span>'; }
    draw();
  }

  /* ---------- 刷卡手續費拆分 ---------- */
  function initFee(root, cfg) { head(root, cfg.q); var P = { a: 1000, m: 2.0, i: 1.2, s: 0.15 };
    var u1 = slider(root, '消費金額', 100, 10000, 100, P.a, function (x) { return x.toLocaleString() + ' 元'; }, null, function (x) { P.a = x; draw(); });
    var u2 = slider(root, '商店支付的手續費率（假設）', 1.0, 3.5, 0.1, P.m, function (x) { return x.toFixed(1) + '%'; }, null, function (x) { P.m = x; draw(); });
    var u3 = slider(root, '其中給發卡行的交換費率（假設）', 0.3, 2.0, 0.1, P.i, function (x) { return x.toFixed(1) + '%'; }, null, function (x) { P.i = x; draw(); });
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function draw() { var i = Math.min(P.i, P.m - P.s), fee = P.a * P.m / 100, iss = P.a * i / 100, sch = P.a * P.s / 100, acq = Math.max(0, fee - iss - sch), net = P.a - fee;
      var parts = [['商店實收', net, '#3a6ea5'], ['發卡行（交換費）', iss, '#d9822b'], ['卡組織', sch, '#8a5cb8'], ['收單行', acq, '#4a9a5e']], x = 20, o = '', W = 600;
      var fx = function (v) { return v / P.a * W; }, big = W * 0.86;
      o += '<rect x="20" y="20" width="' + n1(fx(net)) + '" height="30" fill="#3a6ea5"/>' + tx(20 + fx(net) / 2, 40, '商店實收 ' + Math.round(net).toLocaleString() + ' 元', 12, '#fff');
      var fz = 140; x = 20; o += '<text x="20" y="78" font-size="11" fill="var(--text-muted)">手續費 ' + n1(fee) + ' 元的分配（放大）：</text>';
      [['發卡行', iss, '#d9822b'], ['卡組織', sch, '#8a5cb8'], ['收單行', acq, '#4a9a5e']].forEach(function (p) { var w = p[1] / fee * W; o += '<rect x="' + n1(x) + '" y="88" width="' + n1(w) + '" height="28" fill="' + p[2] + '"/>' + (w > 60 ? tx(x + w / 2, 107, p[0] + ' ' + n1(p[1]) + ' 元', 11, '#fff') : ''); x += w; });
      view.innerHTML = svgw('0 0 640 126', o);
      inf.innerHTML = '刷 ' + P.a.toLocaleString() + ' 元：商店付手續費 <b>' + n1(fee) + ' 元</b>（' + P.m.toFixed(1) + '%）。其中交換費約 <b>' + n1(iss) + ' 元</b>給發卡行（用來支付刷卡回饋、壞帳與營運）、卡組織約 ' + n1(sch) + ' 元、收單行約 ' + n1(acq) + ' 元。<br><span style="font-size:0.88em;color:var(--text-muted)">所有費率都是示意用的假設值；實際的費率依卡別、商店類型、國家與合約而不同。</span>'; }
    u1(); u2(); u3();
  }

  /* ---------- BGP 路由 ---------- */
  function initBgp(root, cfg) { head(root, cfg.q); var mode = 0, rpki = false;
    var N = { 100: [70, 140, '你的業者'], 200: [220, 60, ''], 300: [220, 220, ''], 400: [400, 60, ''], 500: [560, 140, '銀行網站所在'], 666: [400, 220, '攻擊者'] };
    var E = [[100, 200], [100, 300], [200, 400], [400, 500], [300, 500], [300, 666]];
    var bar = el('div', 'margin:4px 0'); [['正常', 0], ['300↔500 線路中斷', 1], ['AS666 劫持', 2]].forEach(function (o) { var b = btn(o[0], o[1]); b.onclick = function () { mode = o[1]; mark(bar, o[1]); draw(); }; bar.appendChild(b); }); root.appendChild(bar); mark(bar, 0);
    var b2 = el('label', 'display:block;font-size:0.9em;margin:4px 0'), cb = document.createElement('input'); cb.type = 'checkbox'; b2.appendChild(cb); b2.appendChild(document.createTextNode(' AS300 啟用路由來源驗證（RPKI）')); cb.onchange = function () { rpki = cb.checked; draw(); }; root.appendChild(b2);
    var view = el('div'), tab = el('div', 'overflow-x:auto'), inf = box(); root.appendChild(view); root.appendChild(tab); root.appendChild(inf);
    function edges() { return E.filter(function (e) { return !(mode === 1 && ((e[0] === 300 && e[1] === 500) || (e[0] === 500 && e[1] === 300))); }); }
    function paths(src, dst, block) { var out = [], es = edges(); function nb(a) { var r = []; es.forEach(function (e) { if (e[0] === a) r.push(e[1]); if (e[1] === a) r.push(e[0]); }); return r; }
      function dfs(a, p) { if (a === dst) { out.push(p.slice()); return; } if (p.length > 5) return; nb(a).forEach(function (b) { if (p.indexOf(b) < 0 && !(block && block(a, b))) { p.push(b); dfs(b, p); p.pop(); } }); } dfs(src, [src]); return out.sort(function (a, b) { return a.length - b.length || a[1] - b[1]; }); }
    function draw() { var R = [], p1 = paths(100, 500); R.push(['203.0.113.0/24', 'AS500', p1.length ? p1[0] : null, '合法的宣告']);
      var hij = mode === 2, hp = hij ? paths(100, 666, function (a, b) { return rpki && a === 300 && b === 100; }) : [];
      if (hij) R.push(['203.0.113.0/25', 'AS666', hp.length ? hp[0] : null, rpki ? 'AS300 驗證失敗，<b>丟棄</b>這條宣告' : '更細的網段（/25），依「最長前綴優先」會被選用']);
      var use = hij && hp.length ? hp[0] : (p1.length ? p1[0] : null), o = '';
      E.forEach(function (e) { var cut = mode === 1 && e[0] === 300 && e[1] === 500, on = use && use.some(function (x, k) { return k > 0 && ((use[k - 1] === e[0] && x === e[1]) || (use[k - 1] === e[1] && x === e[0])); });
        var a = N[e[0]], b = N[e[1]]; o += '<line x1="' + a[0] + '" y1="' + a[1] + '" x2="' + b[0] + '" y2="' + b[1] + '" stroke="' + (cut ? '#bbb' : on ? (hij && use === hp[0] ? '#d0564f' : '#4a9a5e') : 'var(--border)') + '" stroke-width="' + (on ? 5 : 2) + '"' + (cut ? ' stroke-dasharray="5 5"' : '') + '/>'; });
      Object.keys(N).forEach(function (k) { var q = N[k], bad = k === '666'; o += '<circle cx="' + q[0] + '" cy="' + q[1] + '" r="26" fill="' + (bad ? '#fde8e6' : 'var(--accent-soft)') + '" stroke="' + (bad ? '#d0564f' : '#3a6ea5') + '" stroke-width="2"/>' + tx(q[0], q[1] + 4, 'AS' + k, 11, 'var(--text)') + (q[2] ? tx(q[0], q[1] + 42, q[2], 10.5, 'var(--text-muted)') : ''); });
      view.innerHTML = svgw('0 0 640 270', o);
      var h = '<table style="width:100%;border-collapse:collapse;font-size:0.88em"><tr><th style="text-align:left;padding:4px">網段</th><th style="text-align:left">宣告者</th><th style="text-align:left">AS 路徑</th><th style="text-align:left">說明</th></tr>';
      R.forEach(function (r) { h += '<tr>' + cell(r[0]) + cell(r[1]) + cell(r[2] ? r[2].map(function (x) { return 'AS' + x; }).join(' → ') : '（無路徑）') + cell(r[3]) + '</tr>'; }); tab.innerHTML = h + '</table>';
      inf.innerHTML = mode === 0 ? '正常情況：AS100 收到兩條通往銀行網段的路徑，選擇 <b>AS 路徑較短</b>的那一條（綠色）。' : mode === 1 ? '線路中斷：原本的路徑消失，BGP 自動改走另一條較長的路徑——網路的韌性就來自這裡。' :
        (rpki ? '啟用 RPKI：AS300 檢查發現 AS666 沒有權利宣告這個網段，丟棄了假的宣告，流量仍然送到真正的銀行。' : '<b style="color:#d0564f">劫持！</b>AS666 宣告了一個更細的網段。路由器依「最長前綴優先」的規則，把送往銀行的一半流量送給攻擊者（紅色）。BGP 預設相信鄰居的宣告，這就是它的弱點。'); }
    draw();
  }

  /* ---------- 傳輸延遲 ---------- */
  function initLat(root, cfg) { head(root, cfg.q); var P = { d: 2100 };
    var bar = el('div', 'margin:4px 0'); cfg.pre.forEach(function (p, i) { var b = btn(p[0], i); b.onclick = function () { mark(bar, i); root.querySelector('input[data-k="d"]').value = p[1]; u(); }; bar.appendChild(b); }); root.appendChild(bar);
    var u = slider(root, '兩地的直線距離', 100, 20000, 100, P.d, function (x) { return x.toLocaleString() + ' 公里'; }, 'd', function (x) { P.d = x; draw(); });
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function draw() { var fib = 2 * P.d * 1.3 / 200000 * 1000, geo = 4 * 35786 / 300000 * 1000, leo = 4 * 550 / 300000 * 1000 + 2 * P.d * 1.1 / 300000 * 1000, vac = 2 * P.d / 300000 * 1000;
      var rows = [['光在真空中（理論下限）', vac, '#888'], ['海底光纖（含繞路，約）', fib, '#3a6ea5'], ['低軌衛星（約 550 公里，簡化）', leo, '#4a9a5e'], ['同步衛星（約 35,786 公里）', geo, '#d0564f']], mx = Math.max(geo, fib) * 1.05, o = '';
      rows.forEach(function (r, i) { var y = 14 + i * 34, w = r[1] / mx * 400; o += tx(10, y + 15, r[0], 11, 'var(--text)', 'start') + '<rect x="230" y="' + y + '" width="' + n1(w) + '" height="20" fill="' + r[2] + '"/>' + tx(236 + w, y + 15, Math.round(r[1]) + ' 毫秒', 11, 'var(--text)', 'start'); });
      view.innerHTML = svgw('0 0 640 150', o);
      inf.innerHTML = '來回時間（RTT）：光在光纖中約每秒 20 萬公里（真空的三分之二），電纜也不會走直線，所以這裡假設路徑比直線長 30%。距離 ' + P.d.toLocaleString() + ' 公里，光纖的來回時間至少約 <b>' + Math.round(fib) + ' 毫秒</b>——這是物理的極限，再快的設備也無法突破。<br>同步衛星太高，來回至少約 ' + Math.round(geo) + ' 毫秒，所以國際網路主要依靠海底電纜。<br><span style="font-size:0.88em;color:var(--text-muted)">簡化估算：未計入路由器、排隊與處理的延遲；低軌衛星的估算假設衛星之間以雷射直接轉送。</span>'; }
    u();
  }

  /* ---------- 彎道超速 ---------- */
  function initCurve(root, cfg) { head(root, cfg.q); var P = { g: 1067, r: 300, c: 90, v: 70 };
    var bar = el('div', 'margin:4px 0'); [[1067, '窄軌 1,067 mm（台鐵、日本在來線）'], [1435, '標準軌 1,435 mm（高鐵、歐洲）']].forEach(function (o) { var b = btn(o[1], o[0]); b.onclick = function () { P.g = o[0]; mark(bar, o[0]); draw(); }; bar.appendChild(b); }); root.appendChild(bar); mark(bar, 1067);
    var u1 = slider(root, '彎道半徑', 150, 3000, 10, P.r, function (x) { return x.toLocaleString() + ' 公尺'; }, null, function (x) { P.r = x; draw(); });
    var u2 = slider(root, '超高（外軌比內軌高）', 0, 180, 5, P.c, function (x) { return x + ' 毫米'; }, null, function (x) { P.c = x; draw(); });
    var u3 = slider(root, '列車速度', 20, 320, 2, P.v, function (x) { return x + ' km/h'; }, null, function (x) { P.v = x; draw(); });
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function draw() { var g = 9.8, G = P.g / 1000, v = P.v / 3.6, ac = v * v / P.r, ah = g * P.c / P.g, au = ac - ah, h = P.g === 1067 ? 1.5 : 1.7, at = g * (G / 2) / h;
      var vt = Math.sqrt(P.r * (ah + at)) * 3.6, vc = Math.sqrt(P.r * (ah + 0.8)) * 3.6, ratio = au / at;
      var o = '', W = 560, f = function (x) { return 40 + Math.max(0, Math.min(1.4, x)) / 1.4 * W; };
      o += '<rect x="40" y="30" width="' + W + '" height="22" fill="var(--border)" rx="4"/><rect x="40" y="30" width="' + n1(f(Math.max(0, ratio)) - 40) + '" height="22" fill="' + (ratio >= 1 ? '#d0564f' : ratio > 0.6 ? '#d9822b' : '#4a9a5e') + '" rx="4"/>';
      o += '<line x1="' + n1(f(1)) + '" y1="22" x2="' + n1(f(1)) + '" y2="60" stroke="#d0564f" stroke-width="2"/>' + tx(f(1), 74, '靜態翻覆門檻', 11, '#d0564f') + tx(f(0.8 / at), 18, '舒適上限', 10, '#4a9a5e') + '<line x1="' + n1(f(0.8 / at)) + '" y1="22" x2="' + n1(f(0.8 / at)) + '" y2="56" stroke="#4a9a5e" stroke-dasharray="3 3"/>';
      view.innerHTML = svgw('0 0 640 84', o);
      inf.innerHTML = '向外的離心加速度 ' + ac.toFixed(2) + ' m/s²，超高抵銷了 ' + ah.toFixed(2) + ' m/s²，剩下的「未平衡加速度」是 <b>' + au.toFixed(2) + ' m/s²</b>。<br>這個彎道在乘客舒適的範圍內，速度約可到 <b>' + Math.round(vc) + ' km/h</b>；依簡化的靜態模型，約 <b>' + Math.round(vt) + ' km/h</b> 時外側車輪會開始離開鋼軌。' +
        (ratio >= 1 ? '<br><b style="color:#d0564f">超過翻覆門檻：列車會向外側翻覆出軌。</b>' : ratio > 0.6 ? '<br><b style="color:#d9822b">已接近危險範圍。</b>' : '') +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">簡化的靜態模型（假設車輛重心高度約 ' + h + ' 公尺），沒有考慮懸吊、晃動、軌道不整與風；真實的翻覆會在<b>比這更低</b>的速度發生。彎道的限速會再保留很大的安全餘裕。</span>'; }
    u1(); u2(); u3();
  }

  /* ---------- 船舶穩定性 ---------- */
  function initStab(root, cfg) { head(root, cfg.q); var P = { h: 0.5, s: 0, b: 0, w: 30 };
    var bar = el('div', 'margin:4px 0'); [['一般狀態', [0.5, 0, 0, 30]], ['加建上層＋貨物堆高＋減少壓艙水', [2.4, 1, 1, 30]], ['甲板上加裝大量救生艇', [0.5, 1, 0, 20]]].forEach(function (o, i) { var b = btn(o[0], i); b.onclick = function () { P.s = o[1][1]; P.b = o[1][2]; mark(bar, i); cs.checked = !!P.s; cb.checked = !!P.b; root.querySelector('input[data-k="h"]').value = o[1][0]; root.querySelector('input[data-k="w"]').value = o[1][3]; uh(); uw(); }; bar.appendChild(b); }); root.appendChild(bar); mark(bar, 0);
    var uh = slider(root, '貨物堆放的高度', 0, 3, 0.1, P.h, function (x) { return x.toFixed(1); }, 'h', function (x) { P.h = x; draw(); });
    var uw = slider(root, '側風與轉向的傾斜力量', 0, 100, 5, P.w, function (x) { return x; }, 'w', function (x) { P.w = x; draw(); });
    function chk(lab, k) { var l = el('label', 'display:block;font-size:0.9em;margin:3px 0'), c = document.createElement('input'); c.type = 'checkbox'; l.appendChild(c); l.appendChild(document.createTextNode(' ' + lab)); c.onchange = function () { P[k] = c.checked ? 1 : 0; draw(); }; root.appendChild(l); return c; }
    var cs = chk('在上層加建客艙（重量加在高處）', 's'), cb = chk('減少船底的壓艙水', 'b');
    var view = el('div', 'margin-top:6px'), inf = box(); root.appendChild(view); root.appendChild(inf);
    function draw() { var KM = 8.0, KG = 6.0 + P.h * 0.6 + P.s * 0.9 + P.b * 0.8, GM = KM - KG, th;
      if (GM <= 0.05) th = 75; else th = Math.min(75, Math.atan(P.w * 0.012 / GM) * 180 / Math.PI);
      var o = '<rect x="0" y="150" width="640" height="70" fill="#cfe3ee"/>', cx = 320, cy = 150;
      o += '<g transform="rotate(' + n1(th) + ' ' + cx + ' ' + cy + ')"><path d="M220,150 L420,150 L400,190 L240,190 Z" fill="#8a6a4a"/><rect x="250" y="' + (110 - P.s * 30) + '" width="140" height="' + (40 + P.s * 30) + '" fill="#e8e1d2" stroke="#8a6a4a"/>' +
        '<rect x="270" y="' + (150 - 10 - P.h * 12) + '" width="100" height="' + (10 + P.h * 12) + '" fill="#d9822b" opacity="0.8"/>' + '<circle cx="320" cy="' + n1(190 - KG * 7) + '" r="5" fill="#d0564f"/>' + tx(334, 190 - KG * 7 + 4, 'G 重心', 10, '#d0564f', 'start') +
        '<circle cx="320" cy="' + n1(190 - KM * 7) + '" r="5" fill="#3a6ea5"/>' + tx(306, 190 - KM * 7 + 4, '穩心 M', 10, '#3a6ea5', 'end') + '</g>';
      view.innerHTML = svgw('0 0 640 220', o);
      inf.innerHTML = '重心高度 KG = ' + KG.toFixed(1) + ' 公尺，穩心高度 KM = ' + KM.toFixed(1) + ' 公尺，<b>穩心高度差 GM = ' + GM.toFixed(2) + ' 公尺</b>。' + (GM <= 0.05 ? '<br><b style="color:#d0564f">GM 小於或等於零：船失去了恢復直立的能力，一點點外力就會翻覆。</b>' : '<br>在這個傾斜力量下，船約傾斜 <b>' + th.toFixed(0) + '°</b>。' + (th > 25 ? '<b style="color:#d0564f">傾斜太大，貨物可能移位、海水可能灌入，非常危險。</b>' : '')) +
        '<br>原則：重心（G）必須低於穩心（M）。重量加在越高的地方、船底越輕，重心就越高，船就越容易翻。<br><span style="font-size:0.88em;color:var(--text-muted)">極度簡化的示意模型，數字不代表任何真實的船。</span>'; }
    uh(); uw();
  }

  function initAll() { document.querySelectorAll('.sys-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ seq: initSeq, luhn: initLuhn, fee: initFee, bgp: initBgp, lat: initLat, curve: initCurve, stab: initStab })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def sw(cfg):
    w = wdg("sys-w", cfg)
    return ("raw", w[1] + u"<script>%s</script>" % SYSLIB)


def M(a, b, label, note, kind="s", both=False):
    return [a, b, label, note, kind, 1 if both else 0]


def SEQ(q, scs):
    return sw({"t": "seq", "q": q, "sc": scs})
