# -*- coding: utf-8 -*-
"""〈全球物流系統〉（lg_）共用工具與互動元件（LGLIB）。"""
import json
from cc_common import *
from qt_common import BASEJS
from lg_geo import WORLD, TAIWAN, WORLD_VB

LG_NOTE = (u"本課的運費、時間、碳排等數字為概略量級，實際會因航線、油價、景氣與季節大幅變動；"
           u"公司排名、船隊規模等以 2024～2025 年前後的公開資料為準。互動工具在瀏覽器中即時計算。")

LGLIB = r"""
(function () {
  if (window.__lgLib) return; window.__lgLib = 1;
""" + BASEJS + r"""
  var WORLD = __WORLD__, TAIWAN = __TAIWAN__;
  function info(root) { var p = el('p', 'margin:6px 0 0;line-height:1.65'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function rng(seed) { var s = seed >>> 0; return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }
  function P(lon, lat) { return [(lon + 180) * 2, (80 - lat) * 2]; }
  function hav(a, b) { var R = 3440.1, t = Math.PI / 180, dl = (b[1] - a[1]) * t, dn = (b[0] - a[0]) * t, x = Math.sin(dl / 2) * Math.sin(dl / 2) + Math.cos(a[1] * t) * Math.cos(b[1] * t) * Math.sin(dn / 2) * Math.sin(dn / 2); return 2 * R * Math.asin(Math.sqrt(x)); }

  /* ---------- 航線地圖 ---------- */
  var ROUTES = {
    suez: { n: '上海 → 鹿特丹（經蘇伊士運河）', c: '#d0564f', w: [[121.8, 31.2], [120.6, 24.5], [112, 12], [104.3, 1.2], [98, 5.6], [80.5, 5.6], [60, 12], [45, 12.3], [43.4, 12.6], [38.5, 20], [33.6, 27.5], [32.5, 30], [32.3, 31.4], [20, 34], [10, 37.5], [-5.6, 35.95], [-9.5, 38], [-9.6, 43.5], [-5, 48.6], [1.5, 50.6], [4, 51.95]] },
    cape: { n: '上海 → 鹿特丹（繞好望角）', c: '#d9822b', w: [[121.8, 31.2], [120.6, 24.5], [112, 12], [104.3, 1.2], [98, 5.6], [88, 0], [60, -20], [35, -34], [18.4, -35.2], [8, -25], [-5, -5], [-21, 14], [-18, 28], [-11.5, 37], [-9.6, 43.5], [-5, 48.6], [1.5, 50.6], [4, 51.95]] },
    pac: { n: '高雄 → 洛杉磯（跨太平洋）', c: '#3a6ea5', w: [[120.3, 22.6], [122.5, 25], [140, 34], [160, 42], [180, 46], [-160, 47], [-140, 43], [-125, 36], [-118.3, 33.7]] },
    pana: { n: '上海 → 紐約（經巴拿馬運河）', c: '#4a9a5e', w: [[121.8, 31.2], [135, 31], [160, 28], [180, 25], [-150, 20], [-115, 13], [-95, 10], [-79.6, 8.9], [-79.9, 9.4], [-78, 14], [-75.5, 22], [-74.5, 32], [-74, 40.5]] } };
  var PORTS = [['上海', 121.8, 31.2], ['高雄', 120.3, 22.6], ['新加坡', 103.8, 1.3], ['鹿特丹', 4, 51.95], ['洛杉磯', -118.3, 33.7], ['紐約', -74, 40.6], ['蘇伊士運河', 32.5, 30.2], ['巴拿馬運河', -79.7, 9.1], ['好望角', 18.4, -34.4], ['曼德海峽', 43.4, 12.6]];
  function routeLen(w) { var s = 0; for (var i = 1; i < w.length; i++) s += hav(w[i - 1], w[i]); return s; }
  function initMap(root, cfg) {
    head(root, cfg.q); var sel = cfg.r ? cfg.r.split(',') : ['suez', 'cape'], kn = 16, bb = bar(root), view = el('div'), p;
    Object.keys(ROUTES).forEach(function (k) { var x = btn(ROUTES[k].n, k); x.addEventListener('click', function () { var i = sel.indexOf(k); if (i >= 0) sel.splice(i, 1); else sel.push(k); x.style.fontWeight = sel.indexOf(k) >= 0 ? 'bold' : 'normal'; draw(); }); x.style.fontWeight = sel.indexOf(k) >= 0 ? 'bold' : 'normal'; bb.appendChild(x); });
    var u = slider(root, '船速', 12, 24, 1, kn, function (v) { return v + ' 節（' + Math.round(v * 1.852) + ' 公里／小時）'; }, 'kn', function (v) { kn = v; draw(); }); root.appendChild(view); p = info(root);
    function line(w) { var segs = [], cur = []; for (var i = 0; i < w.length; i++) { if (i && Math.abs(w[i][0] - w[i - 1][0]) > 180) { var a = w[i - 1], b = w[i], b2 = [b[0] + (b[0] < a[0] ? 360 : -360), b[1]], t = ((a[0] < 0 ? -180 : 180) - a[0]) / (b2[0] - a[0]), mid = a[1] + t * (b[1] - a[1]);
          cur.push(P(a[0] < 0 ? -180 : 180, mid)); segs.push(cur); cur = [P(a[0] < 0 ? 180 : -180, mid)]; } cur.push(P(w[i][0], w[i][1])); } segs.push(cur);
      return segs.map(function (s) { return 'M' + s.map(function (q) { return n1(q[0]) + ',' + n1(q[1]); }).join('L'); }).join(''); }
    function draw() { var o = '<rect width="720" height="280" fill="#dfeaf5"/><path d="' + WORLD + '" fill="#c9d1c3" stroke="#fff" stroke-width="0.3"/><path d="' + TAIWAN + '" fill="#d0564f"/>', rows = [];
      sel.forEach(function (k) { var r = ROUTES[k], d = routeLen(r.w); o += '<path d="' + line(r.w) + '" fill="none" stroke="' + r.c + '" stroke-width="2"/>'; rows.push('<span style="color:' + r.c + '">■</span> ' + r.n + '：約 <b>' + Math.round(d).toLocaleString() + '</b> 浬（' + Math.round(d * 1.852).toLocaleString() + ' 公里），以 ' + kn + ' 節航行約 <b>' + f1(d / kn / 24) + '</b> 天'); });
      PORTS.forEach(function (q) { var a = P(q[1], q[2]); o += '<circle cx="' + n1(a[0]) + '" cy="' + n1(a[1]) + '" r="2.4" fill="#333"/>' + tx(a[0] + 4, a[1] - 3, q[0], 7.5, '#333', 'start'); });
      view.innerHTML = svgw('0 0 720 280', o);
      p.innerHTML = rows.join('<br>') + (sel.indexOf('suez') >= 0 && sel.indexOf('cape') >= 0 ? '<br>繞好望角比走蘇伊士運河多出約 <b>' + Math.round(routeLen(ROUTES.cape.w) - routeLen(ROUTES.suez.w)).toLocaleString() + '</b> 浬，多花一到兩週，燃料與船期成本大增（第 42 課）。' : '') +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">航線以轉折點概略繪製，實際航程依航線安排與停靠港而不同；另加上港口作業時間。</span>'; }
    u();
  }

  /* ---------- 運輸方式比較 ---------- */
  var MODES = [['海運（貨櫃）', '#3a6ea5', 0.008, 800, 10, 12], ['鐵路', '#8a5cb8', 0.04, 800, 5, 25], ['卡車', '#d9822b', 0.12, 700, 1, 80], ['空運', '#d0564f', 2.2, 8000, 2, 550]];
  function initModes(root, cfg) {
    head(root, cfg.q); var kg = 1000, km = 10000, view = el('div'), p;
    var u1 = slider(root, '貨物重量', 1, 5, 0.01, Math.log10(kg), function (v) { var w = Math.pow(10, v); return w >= 1000 ? f1(w / 1000) + ' 公噸' : Math.round(w) + ' 公斤'; }, 'kg', function (v) { kg = Math.pow(10, v); draw(); });
    var u2 = slider(root, '距離', 500, 20000, 100, km, function (v) { return v.toLocaleString() + ' 公里'; }, 'km', function (v) { km = v; draw(); });
    root.appendChild(view); p = info(root);
    function draw() { var t = kg / 1000, rows = MODES.map(function (m) { return { n: m[0], c: m[1], cost: t * km * m[2], days: km / m[3] + m[4], co2: t * km * m[5] / 1000 }; }), o = '';
      [['cost', '運費（美元）'], ['days', '天數'], ['co2', '碳排放（公斤 CO₂）']].forEach(function (q, gi) { var mx = Math.max.apply(null, rows.map(function (r) { return r[q[0]]; })), y0 = gi * 112;
        o += tx(10, y0 + 14, q[1], 11, 'currentColor', 'start'); rows.forEach(function (r, i) { var w = r[q[0]] / mx * 430; o += tx(120, y0 + 34 + i * 19, r.n, 10, 'currentColor', 'end') + '<rect x="126" y="' + (y0 + 23 + i * 19) + '" width="' + n1(Math.max(w, 1)) + '" height="14" rx="3" fill="' + r.c + '"/>' + tx(132 + w, y0 + 34 + i * 19, r[q[0]] >= 100 ? Math.round(r[q[0]]).toLocaleString() : f1(r[q[0]]), 9.5, 'currentColor', 'start'); }); });
      view.innerHTML = svgw('0 0 640 336', o);
      p.innerHTML = '同一批貨運 ' + km.toLocaleString() + ' 公里：空運最快，但運費約是海運的 <b>' + Math.round(MODES[3][2] / MODES[0][2]) + ' 倍</b>、碳排約 <b>' + Math.round(MODES[3][5] / MODES[0][5]) + ' 倍</b>。所以高價值、急件、輕巧的東西（晶片、手機、生鮮、藥品）走空運，大宗貨物走海運。' +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">每噸公里的運費、速度（含港口與轉運時間）、碳排都是概略的典型量級；卡車跨洋的情況只供比較。實際運價波動很大。</span>'; }
    u1(); u2();
  }

  /* ---------- 長鞭效應（啤酒遊戲） ---------- */
  function initBull(root, cfg) {
    head(root, cfg.q); var al = cfg.a || 0.5, share = false, view = el('div'), p, bb = bar(root), sb = btn('共享終端銷售資料：關', 's'); bb.appendChild(sb);
    sb.addEventListener('click', function () { share = !share; sb.textContent = '共享終端銷售資料：' + (share ? '開' : '關'); draw(); });
    var u = slider(root, '補貨的積極程度（每期要補回目標差距的幾成）', 0.1, 1, 0.05, al, function (v) { return Math.round(v * 100) + '%'; }, 'a', function (v) { al = v; draw(); });
    root.appendChild(view); p = info(root);
    function sim() { var T = 40, L = 2, N = 4, inv = [], back = [], pipe = [], F = [], orders = [], rec;
      for (var i = 0; i < N; i++) { inv.push(12); back.push(0); pipe.push([4, 4]); F.push(4); orders.push([]); }
      for (var t = 0; t < T; t++) { var dem = t < 5 ? 4 : 8, incoming = dem;
        for (var i2 = 0; i2 < N; i2++) { var arrive = pipe[i2].shift(); inv[i2] += arrive; var need = incoming + back[i2], ship = Math.min(inv[i2], need); inv[i2] -= ship; back[i2] = need - ship;
          F[i2] = 0.7 * F[i2] + 0.3 * (share ? dem : incoming); var target = F[i2] * (L + 2), posi = inv[i2] - back[i2] + pipe[i2].reduce(function (a, b) { return a + b; }, 0);
          var o = Math.max(0, Math.round(F[i2] + al * (target - posi))); orders[i2].push(o); incoming = o; pipe[i2].push(i2 === N - 1 ? o : o); }
      } return orders; }
    function draw() { var o = sim(), names = ['零售店', '批發商', '經銷商', '工廠'], cols = ['#4a9a5e', '#3a6ea5', '#d9822b', '#d0564f'], S = [{ d: o[0].map(function (_, t) { return [t, t < 5 ? 4 : 8]; }), c: '#999', n: '消費者需求', dash: '5 3' }];
      o.forEach(function (s, i) { S.push({ d: s.map(function (v, t) { return [t, v]; }), c: cols[i], n: names[i] + '的訂單' }); });
      var mx = o.map(function (s) { return Math.max.apply(null, s); });
      view.innerHTML = chart(640, 280, S, { x0: 0, x1: 39, y0: 0, xl: '週' });
      p.innerHTML = '消費者需求只從每週 4 箱變成 8 箱（虛線）。但往上游看，各層的最大訂單是：零售店 <b>' + mx[0] + '</b>、批發商 <b>' + mx[1] + '</b>、經銷商 <b>' + mx[2] + '</b>、工廠 <b>' + mx[3] + '</b>。' +
        '<br>每一層只看得到下游的訂單，又因為交貨要等 2 週而「多訂一點以防萬一」，波動就一層層放大——這就是<b>長鞭效應</b>。試著降低補貨積極程度、或打開「共享終端銷售資料」。'; }
    u();
  }

  /* ---------- 經濟訂購量與安全庫存 ---------- */
  function initEOQ(root, cfg) {
    head(root, cfg.q); var D = 12000, S = 2000, H = 40, sd = 15, LT = 7, z = 1.645, view = el('div'), p;
    var u1 = slider(root, '年需求量 D', 1000, 50000, 500, D, function (v) { return v.toLocaleString() + ' 個'; }, 'D', function (v) { D = v; draw(); });
    var u2 = slider(root, '每次訂貨成本 S（運費、處理）', 200, 10000, 100, S, function (v) { return v.toLocaleString() + ' 元'; }, 'S', function (v) { S = v; draw(); });
    var u3 = slider(root, '每個貨品每年的持有成本 H（倉租、資金、損耗）', 5, 200, 1, H, function (v) { return v + ' 元'; }, 'H', function (v) { H = v; draw(); });
    var u4 = slider(root, '每日需求的標準差', 0, 60, 1, sd, function (v) { return v + ' 個'; }, 'sd', function (v) { sd = v; draw(); });
    var u5 = slider(root, '交貨前置時間', 1, 60, 1, LT, function (v) { return v + ' 天'; }, 'lt', function (v) { LT = v; draw(); });
    var bb = bar(root); [[1.282, '服務水準 90%'], [1.645, '95%'], [2.326, '99%']].forEach(function (q) { var x = btn(q[1], q[0]); x.addEventListener('click', function () { z = q[0]; mark(bb, q[0]); draw(); }); bb.appendChild(x); }); mark(bb, 1.645);
    root.appendChild(view); p = info(root);
    function draw() { var q = Math.sqrt(2 * D * S / H), d1 = [], d2 = [], d3 = []; for (var Q = q * 0.2; Q <= q * 3; Q += q * 0.05) { d1.push([Q, D / Q * S]); d2.push([Q, Q / 2 * H]); d3.push([Q, D / Q * S + Q / 2 * H]); }
      var ss = z * sd * Math.sqrt(LT), rop = D / 365 * LT + ss;
      view.innerHTML = chart(640, 230, [{ d: d1, c: C1(), n: '訂貨成本' }, { d: d2, c: '#d9822b', n: '持有成本' }, { d: d3, c: '#d0564f', n: '總成本', w: 3 }], { y0: 0, xl: '每次訂多少（Q）', vl: [{ x: q, c: '#4a9a5e', n: 'EOQ' }] });
      p.innerHTML = '訂太少要訂很多次（訂貨成本高），訂太多倉庫堆滿（持有成本高）。兩者加總最低的點是<b>經濟訂購量</b> EOQ ＝ √(2DS／H) ＝ <b>' + Math.round(q).toLocaleString() + ' 個</b>，一年約訂 ' + f1(D / q) + ' 次。' +
        '<br>需求有波動、交貨要 ' + LT + ' 天，所以要多放<b>安全庫存</b> ＝ z × σ × √前置時間 ＝ <b>' + Math.round(ss) + ' 個</b>；庫存降到 <b>' + Math.round(rop) + ' 個</b>時就該下單（再訂購點）。服務水準從 95% 提高到 99%，安全庫存要多約四成。'; }
    function C1() { return '#3a6ea5'; }
    u1(); u2(); u3(); u4(); u5();
  }

  /* ---------- 路徑最佳化（旅行推銷員） ---------- */
  function initTSP(root, cfg) {
    head(root, cfg.q); var pts = [], tour = [], seed = 3, view = el('div'), p, msg = '';
    var bb = bar(root), b0 = btn('🎲 新的 15 個送貨點', 'n'), b1 = btn('最近鄰居法', 'nn'), b2 = btn('2-opt 改善', 'opt'), b3 = btn('清空（自己點地圖加點）', 'c'); [b0, b1, b2, b3].forEach(function (b) { bb.appendChild(b); });
    root.appendChild(view); p = info(root);
    function gen() { var r = rng(seed++); pts = [[320, 150]]; for (var i = 0; i < 14; i++) pts.push([30 + r() * 580, 20 + r() * 260]); tour = []; msg = ''; draw(); }
    function len(t) { var s = 0; for (var i = 0; i < t.length; i++) { var a = pts[t[i]], b = pts[t[(i + 1) % t.length]]; s += Math.hypot(a[0] - b[0], a[1] - b[1]); } return s; }
    b0.addEventListener('click', gen); b3.addEventListener('click', function () { pts = [[320, 150]]; tour = []; msg = ''; draw(); });
    b1.addEventListener('click', function () { var left = pts.map(function (_, i) { return i; }).slice(1), t = [0]; while (left.length) { var c = pts[t[t.length - 1]], bi = 0, bd = 1e9; left.forEach(function (j, k) { var d = Math.hypot(pts[j][0] - c[0], pts[j][1] - c[1]); if (d < bd) { bd = d; bi = k; } }); t.push(left.splice(bi, 1)[0]); } tour = t; msg = '最近鄰居法：每次都去最近的下一個點。'; draw(); });
    b2.addEventListener('click', function () { if (tour.length < 4) return; var before = len(tour), imp = true, n = tour.length; while (imp) { imp = false; for (var i = 1; i < n - 1; i++) for (var k = i + 1; k < n; k++) { var t2 = tour.slice(0, i).concat(tour.slice(i, k + 1).reverse(), tour.slice(k + 1)); if (len(t2) < len(tour) - 1e-6) { tour = t2; imp = true; } } }
      msg = '2-opt：把兩條交叉的路線「解開」，總長從 ' + Math.round(before) + ' 降到 ' + Math.round(len(tour)) + '（少了 ' + Math.round((1 - len(tour) / before) * 100) + '%）。'; draw(); });
    view.addEventListener('click', function (e) { var s = view.querySelector('svg'); if (!s) return; var r = s.getBoundingClientRect(), x = (e.clientX - r.left) / r.width * 640, y = (e.clientY - r.top) / r.height * 300; pts.push([x, y]); tour = []; msg = ''; draw(); });
    function fact(n) { var f = 1; for (var i = 2; i <= n; i++) f *= i; return f; }
    function draw() { var o = '<rect width="640" height="300" fill="var(--surface)"/>'; if (tour.length) o += '<path d="M' + tour.map(function (i) { return n1(pts[i][0]) + ',' + n1(pts[i][1]); }).join('L') + 'Z" fill="none" stroke="#3a6ea5" stroke-width="2"/>';
      pts.forEach(function (q, i) { o += i ? '<circle cx="' + n1(q[0]) + '" cy="' + n1(q[1]) + '" r="5" fill="#d9822b"/>' : '<rect x="' + (q[0] - 7) + '" y="' + (q[1] - 7) + '" width="14" height="14" fill="#d0564f"/>' + tx(q[0], q[1] - 11, '倉庫', 10, '#d0564f'); });
      view.innerHTML = '<div style="cursor:crosshair">' + svgw('0 0 640 300', o) + '</div>'; var n = pts.length - 1;
      p.innerHTML = (msg ? msg + '<br>' : '') + '倉庫加上 ' + n + ' 個送貨點。' + (tour.length ? '目前路線總長 <b>' + Math.round(len(tour)) + '</b>。' : '') + '要嘗試所有可能的路線，共有 (n−1)!／2 ＝ <b>' + (n > 1 ? (fact(n) / 2 >= 1e12 ? (fact(n) / 2).toExponential(1) : Math.round(fact(n) / 2).toLocaleString()) : 1) + '</b> 種——點數一多就算不完，所以實務上用最近鄰居、2-opt 這類「夠好又夠快」的方法。'; }
    gen();
  }


  /* ---------- 貨櫃裝載：體積滿還是重量滿 ---------- */
  var BOX = [['20 呎', 33.2, 28.2], ['40 呎', 67.7, 26.7], ['40 呎高櫃', 76.3, 26.5]];
  function initPack(root, cfg) {
    head(root, cfg.q); var den = 300, fill = 0.85, view = el('div'), p;
    var u1 = slider(root, '貨物密度（每立方公尺幾公斤）', 30, 2500, 10, den, function (v) { var e = v < 120 ? '（如泡棉、羽絨衣）' : v < 400 ? '（如成衣、家電）' : v < 900 ? '（如紙張、飲料）' : '（如機械零件、磁磚）'; return v + ' 公斤' + e; }, 'd', function (v) { den = v; draw(); });
    var u2 = slider(root, '實際能塞滿的比例（紙箱間空隙、棧板）', 0.6, 0.95, 0.01, fill, function (v) { return Math.round(v * 100) + '%'; }, 'f', function (v) { fill = v; draw(); });
    root.appendChild(view); p = info(root);
    function draw() { var o = '', rows = [];
      BOX.forEach(function (b, i) { var byV = b[1] * fill * den / 1000, t = Math.min(byV, b[2]), y = 20 + i * 70, wf = Math.min(byV / b[2], 1), vf = Math.min(b[2] / byV, 1) * fill;
        o += tx(10, y + 14, b[0], 11, 'currentColor', 'start') + tx(10, y + 30, b[1] + ' m³／' + b[2] + ' t', 9, 'var(--text-muted)', 'start');
        o += '<rect x="130" y="' + y + '" width="460" height="18" fill="none" stroke="#999"/><rect x="130" y="' + y + '" width="' + n1(460 * vf) + '" height="18" fill="#3a6ea5"/>' + tx(596, y + 13, '體積 ' + Math.round(vf * 100) + '%', 9.5, 'currentColor', 'start');
        o += '<rect x="130" y="' + (y + 24) + '" width="460" height="18" fill="none" stroke="#999"/><rect x="130" y="' + (y + 24) + '" width="' + n1(460 * wf) + '" height="18" fill="#d9822b"/>' + tx(596, y + 37, '重量 ' + Math.round(wf * 100) + '%', 9.5, 'currentColor', 'start');
        rows.push(b[0] + '：裝 <b>' + f1(t) + '</b> 公噸，' + (byV > b[2] ? '<b style="color:#d9822b">重量先到上限</b>（空間還沒滿）' : '<b style="color:#3a6ea5">空間先塞滿</b>（重量還有餘裕）')); });
      view.innerHTML = svgw('0 0 680 230', o);
      p.innerHTML = rows.join('<br>') + '<br>密度約 ' + Math.round(26.7 / (67.7 * fill) * 1000) + ' 公斤／立方公尺是 40 呎櫃的分界：比它輕的貨「材積」先滿（運費常按體積算），比它重的貨「重量」先滿，這時改用 20 呎櫃反而划算。' +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">容積與最大載重為常見規格的近似值，各船公司、櫃型略有不同；道路限重也可能更嚴。</span>'; }
    u1(); u2();
  }

  function initAll() { document.querySelectorAll('.lg-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ map: initMap, modes: initModes, bull: initBull, eoq: initEOQ, tsp: initTSP, pack: initPack })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
""".replace("__WORLD__", json.dumps(WORLD)).replace("__TAIWAN__", json.dumps(TAIWAN))


def lgw(cfg, maxw=720):
    return wdg("lg-w", cfg, maxw)


lglesson = make_lesson(u"🚢", LG_NOTE, LGLIB, "lg-w")
