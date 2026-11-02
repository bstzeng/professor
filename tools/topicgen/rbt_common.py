# -*- coding: utf-8 -*-
"""〈機器人與自動駕駛〉（rbt_）共用：課程包裝與 RBTLIB 互動元件（class="rbt-w"）。

  pid      PID 調參
  kalman   一維卡爾曼濾波
  ik       兩軸機械手臂逆向運動學
  pf       粒子濾波定位（走廊與門）
  plan     A*、Dijkstra 與 RRT 路徑規劃
  sensor   感測器資料量計算
  compute  算力與記憶體頻寬需求
  power    人形機器人／Robotaxi 功耗與電池
  taxi     Robotaxi 單位經濟學
  roi      人形機器人回本期
  demand   全球硬體需求推算
"""
from md_common import make_with
from cc_common import wdg, LS
from qt_common import BASEJS

RBT_NOTE = u"本課程重直覺、輕推導，程式範例以 Python 為主。產業數字多來自 2025～2026 年的公司公告與研究機構彙整，各家數字常有出入，課中以「約」與資料日期標示；硬體規格以廠商公布值為準，實際可用效能通常低於標稱峰值。"


def rw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("rbt-w", cfg)


def PY(s):
    return ("code", s.strip("\n"))


RBTLIB = r"""
(function () {
  if (window.__rbtLib) return; window.__rbtLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#9aa3ad', TL = '#2a9d8f';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function row(root) { var d = el('div'); root.appendChild(d); return d; }
  function bt(par, t, cb) { var b = btn(t); b.onclick = cb; par.appendChild(b); return b; }
  function cell(s, css) { return '<td style="padding:3px 8px;border-bottom:1px solid var(--border);' + (css || '') + '">' + s + '</td>'; }
  function tbl(head, rows) { return '<div style="overflow-x:auto"><table style="border-collapse:collapse;margin:6px 0;width:100%;font-size:0.86em"><tr>' + head.map(function (h) { return '<th style="padding:3px 8px;text-align:left;font-weight:normal;color:var(--text-muted);border-bottom:2px solid var(--border)">' + h + '</th>'; }).join('') + '</tr>' + rows.join('') + '</table></div>'; }
  function rng(seed) { var s = seed >>> 0 || 1; return function () { s = (s * 1664525 + 1013904223) >>> 0; return s / 4294967296; }; }
  function gauss(R) { var u = Math.max(R(), 1e-9), v = R(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v); }
  function fx(v, d) { return (+v).toFixed(d === undefined ? 1 : d); }
  function big(v) { var a = Math.abs(v); return a >= 1e12 ? fx(v / 1e12) + ' 兆' : a >= 1e8 ? fx(v / 1e8) + ' 億' : a >= 1e4 ? Math.round(v / 1e4).toLocaleString() + ' 萬' : Math.round(v).toLocaleString(); }
  function sl(root, lab, mn, mx, st, val, fmt, cb) { return slider(root, lab, mn, mx, st, val, fmt || function (x) { return x; }, null, cb); }
  function bars(items, unit) { var mx = Math.max.apply(null, items.map(function (x) { return x[1]; })) || 1, g = '', H = items.length * 28 + 8;
    items.forEach(function (x, i) { var y = 6 + i * 28, w = x[1] / mx * 380; g += tx(170, y + 15, x[0], 11.5, 'currentColor', 'end') + '<rect x="180" y="' + y + '" width="' + n1(Math.max(w, 1)) + '" height="20" rx="3" fill="' + (x[2] || BL) + '"/>' + tx(186 + w, y + 15, x[3] || (fx(x[1], 2) + (unit || '')), 11, 'var(--text-muted)', 'start'); });
    return svgw('0 0 680 ' + H, g); }

  /* ---------- PID ---------- */
  function initPid(root, cfg) { head(root, cfg.q); var P = { kp: cfg.kp || 4, ki: cfg.ki || 0, kd: cfg.kd || 0, d: cfg.d === undefined ? 1 : cfg.d }, v = el('div'), inf, ups = [];
    ups.push(sl(root, 'Kp（比例）', 0, 30, 0.5, P.kp, null, function (x) { P.kp = x; draw(); }));
    ups.push(sl(root, 'Ki（積分）', 0, 20, 0.5, P.ki, null, function (x) { P.ki = x; draw(); }));
    ups.push(sl(root, 'Kd（微分）', 0, 10, 0.1, P.kd, null, function (x) { P.kd = x; draw(); }));
    ups.push(sl(root, '外力干擾（例如重力、負載）', 0, 3, 0.5, P.d, null, function (x) { P.d = x; draw(); }));
    var b = row(root); [['只用 P', [4, 0, 0]], ['PI', [4, 3, 0]], ['PID（調好）', [12, 6, 3]], ['P 太大', [30, 0, 0]]].forEach(function (p) { bt(b, p[0], function () { var s = root.querySelectorAll('input[type=range]'); s[0].value = p[1][0]; s[1].value = p[1][1]; s[2].value = p[1][2]; ups.forEach(function (u) { u(); }); }); });
    root.appendChild(v); inf = info(root);
    function draw() { var dt = 0.005, x = 0, vel = 0, I = 0, e0 = 1, d1 = [], d2 = [], mx = 0, st = 10, T = 8;
      for (var k = 0; k <= T / dt; k++) { var t = k * dt, e = 1 - x; I += e * dt; I = Math.max(-50, Math.min(50, I)); var de = (e - e0) / dt; e0 = e; var u = P.kp * e + P.ki * I + P.kd * (k ? de : 0); u = Math.max(-40, Math.min(40, u));
        var a = (u - 2 * vel - P.d) / 1; vel += a * dt; x += vel * dt; if (k % 8 === 0) { d1.push([t, x]); d2.push([t, u / 10]); } if (x > mx) mx = x; if (Math.abs(1 - x) > 0.02) st = t + dt; }
      v.innerHTML = chart(680, 260, [{ d: d1, c: BL, n: '位置' }, { d: d2, c: OR, n: '控制力 ÷10', dash: '4 3', w: 1.5 }], { x0: 0, x1: T, y0: Math.min(-0.2, Math.min.apply(null, d2.map(function (p) { return p[1]; }))), y1: Math.max(1.6, mx * 1.05), xl: '時間（秒）', hl: [{ y: 1, n: '目標', c: GN }] });
      var ess = 1 - x, os = Math.max(0, (mx - 1) * 100);
      inf.innerHTML = '超調量 <b>' + fx(os) + '%</b>　穩定時間（誤差 2% 內）<b>' + (st >= T ? '超過 ' + T + ' 秒' : fx(st, 2) + ' 秒') + '</b>　最終誤差 <b>' + fx(ess, 3) + '</b><br>' +
        (P.ki === 0 && P.d > 0 && Math.abs(ess) > 0.01 ? '只用 P 時，為了抵抗干擾一定要留一點誤差（穩態誤差）；加上 <b>I</b> 就能把它消掉。' : os > 25 ? '超調太大、來回晃動：試著加大 <b>D</b>（像阻尼）或降低 P。' : st >= T ? '反應太慢：試著加大 <b>P</b>。' : '不錯！又快又穩，誤差也小。') + '<br><span style="color:var(--text-muted);font-size:0.9em">模擬對象：一個有摩擦的質量（例如機器人關節），目標是移動到位置 1，並持續受到干擾力。控制力上限 ±40。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 卡爾曼濾波 ---------- */
  function initKalman(root, cfg) { head(root, cfg.q); var P = { r: 4, q: 0.05, seed: 7 }, v = el('div'), inf, ups = [];
    ups.push(sl(root, '量測雜訊（GPS 誤差，公尺）', 0.5, 10, 0.5, P.r, null, function (x) { P.r = x; draw(); }));
    ups.push(sl(root, '濾波器對「運動不確定」的假設', 0.01, 2, 0.01, P.q, null, function (x) { P.q = x; draw(); }));
    var b = row(root); bt(b, '重新產生一段路', function () { P.seed = (P.seed * 7 + 13) % 9973 + 1; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var R = rng(P.seed), N = 80, dt = 1, tr = [], ms = [], es = [], pos = 0, vel = 2, x = [0, 0], C = [[100, 0], [0, 10]], se = 0, sm = 0, qt = 0.1;
      for (var k = 0; k < N; k++) { vel += gauss(R) * Math.sqrt(qt); pos += vel * dt; var z = pos + gauss(R) * P.r;
        var xp = [x[0] + x[1] * dt, x[1]], q = P.q, Pp = [[C[0][0] + dt * (C[1][0] + C[0][1]) + dt * dt * C[1][1] + q * dt * dt * dt / 3, C[0][1] + dt * C[1][1] + q * dt * dt / 2], [C[1][0] + dt * C[1][1] + q * dt * dt / 2, C[1][1] + q * dt]];
        var S = Pp[0][0] + P.r * P.r, K = [Pp[0][0] / S, Pp[1][0] / S], y = z - xp[0]; x = [xp[0] + K[0] * y, xp[1] + K[1] * y];
        C = [[(1 - K[0]) * Pp[0][0], (1 - K[0]) * Pp[0][1]], [Pp[1][0] - K[1] * Pp[0][0], Pp[1][1] - K[1] * Pp[0][1]]];
        tr.push([k, pos]); ms.push([k, z]); es.push([k, x[0]]); if (k > 5) { se += (x[0] - pos) * (x[0] - pos); sm += (z - pos) * (z - pos); } }
      var dev = function (L) { return L.map(function (p, i) { return [p[0], p[1] - tr[i][1]]; }); };
      v.innerHTML = chart(680, 270, [{ d: dev(ms), c: GY, n: 'GPS 量測', w: 1 }, { d: dev(es), c: OR, n: '卡爾曼估計', w: 2.2 }, { d: tr.map(function (p) { return [p[0], 0]; }), c: GN, n: '真實位置', w: 1.5, dash: '5 3' }], { x0: 0, x1: N - 1, xl: '時間（秒）', yl: '與真實位置的誤差（公尺）' });
      var rm = Math.sqrt(sm / (N - 6)), re = Math.sqrt(se / (N - 6));
      inf.innerHTML = '量測的平均誤差約 <b>' + fx(rm, 2) + ' 公尺</b>，卡爾曼估計的平均誤差約 <b>' + fx(re, 2) + ' 公尺</b>（' + (re < rm ? '減少 ' + fx((1 - re / rm) * 100, 0) + '%' : '沒有改善') + '）。<br>' +
        (P.q < 0.03 ? '假設運動「很穩定」：估計很平滑，但車子真的加減速時會跟不上。' : P.q > 1 ? '假設運動「很不穩定」：濾波器幾乎只相信量測，估計跟著雜訊跳動。' : '在「相信預測」與「相信量測」之間取得平衡。') +
        '<br><span style="color:var(--text-muted);font-size:0.9em">圖中畫的是「誤差」：綠色虛線（0）是真實位置，越貼近越好。車子以約每秒 2 公尺行駛，速度會隨機變化。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 兩軸手臂逆向運動學 ---------- */
  function initIk(root, cfg) { head(root, cfg.q); var P = { x: 1.2, y: 0.8, l1: 1, l2: 0.8 }, v = el('div'), inf, ups = [];
    ups.push(sl(root, '目標 x（公尺）', -1.8, 1.8, 0.05, P.x, null, function (x) { P.x = x; draw(); }));
    ups.push(sl(root, '目標 y（公尺）', -0.6, 1.8, 0.05, P.y, null, function (x) { P.y = x; draw(); }));
    ups.push(sl(root, '上臂長 L1', 0.4, 1.2, 0.05, P.l1, null, function (x) { P.l1 = x; draw(); }));
    ups.push(sl(root, '前臂長 L2', 0.3, 1.2, 0.05, P.l2, null, function (x) { P.l2 = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function draw() { var S = 120, ox = 340, oy = 250, X = function (x) { return ox + x * S; }, Y = function (y) { return oy - y * S; }, g = '', d = Math.hypot(P.x, P.y), L1 = P.l1, L2 = P.l2;
      g += '<circle cx="' + ox + '" cy="' + oy + '" r="' + n1((L1 + L2) * S) + '" fill="' + BL + '" fill-opacity="0.05" stroke="' + BL + '" stroke-dasharray="4 4"/>';
      if (Math.abs(L1 - L2) > 0) g += '<circle cx="' + ox + '" cy="' + oy + '" r="' + n1(Math.abs(L1 - L2) * S) + '" fill="var(--surface)" stroke="' + GY + '" stroke-dasharray="3 3"/>';
      g += ln(0, oy, 680, oy, 'var(--border)') + '<rect x="' + (ox - 18) + '" y="' + oy + '" width="36" height="12" fill="' + GY + '"/>';
      var ok = d <= L1 + L2 && d >= Math.abs(L1 - L2), sols = [];
      if (ok) { var c2 = (d * d - L1 * L1 - L2 * L2) / (2 * L1 * L2); c2 = Math.max(-1, Math.min(1, c2)); [1, -1].forEach(function (s) { var t2 = s * Math.acos(c2), t1 = Math.atan2(P.y, P.x) - Math.atan2(L2 * Math.sin(t2), L1 + L2 * Math.cos(t2)); sols.push([t1, t2]); }); }
      sols.forEach(function (s, i) { var ex = L1 * Math.cos(s[0]), ey = L1 * Math.sin(s[0]), c = i ? GY : OR, w = i ? 4 : 8, op = i ? ' stroke-opacity="0.6" stroke-dasharray="6 4"' : '';
        g += '<line x1="' + ox + '" y1="' + oy + '" x2="' + n1(X(ex)) + '" y2="' + n1(Y(ey)) + '" stroke="' + c + '" stroke-width="' + w + '" stroke-linecap="round"' + op + '/><line x1="' + n1(X(ex)) + '" y1="' + n1(Y(ey)) + '" x2="' + n1(X(P.x)) + '" y2="' + n1(Y(P.y)) + '" stroke="' + c + '" stroke-width="' + w + '" stroke-linecap="round"' + op + '/><circle cx="' + n1(X(ex)) + '" cy="' + n1(Y(ey)) + '" r="5" fill="' + c + '"/>'; });
      g += '<circle cx="' + ox + '" cy="' + oy + '" r="6" fill="' + BL + '"/><circle cx="' + n1(X(P.x)) + '" cy="' + n1(Y(P.y)) + '" r="7" fill="none" stroke="' + (ok ? GN : RD) + '" stroke-width="2.5"/>';
      v.innerHTML = svgw('0 0 680 300', g);
      var deg = function (r) { return fx(r * 180 / Math.PI, 0) + '°'; };
      inf.innerHTML = ok ? '到目標的距離 ' + fx(d, 2) + ' 公尺，有<b>兩組解</b>：<br><span style="color:' + OR + '">■</span> 解 1（實線）：肩 ' + deg(sols[0][0]) + '、肘 ' + deg(sols[0][1]) + '　<span style="color:' + GY + '">■</span> 解 2（虛線）：肩 ' + deg(sols[1][0]) + '、肘 ' + deg(sols[1][1]) + '<br><span style="color:var(--text-muted);font-size:0.9em">逆向運動學常有多組解（手肘朝上或朝下），控制器要選一組：例如離目前姿勢最近、不撞到東西的那一組。虛線圓是手臂能碰到的範圍。</span>'
        : '<span style="color:' + RD + '"><b>無解</b></span>：目標距離 ' + fx(d, 2) + ' 公尺，' + (d > L1 + L2 ? '超過手臂全長 ' + fx(L1 + L2, 2) + ' 公尺，搆不到。' : '比 |L1 − L2| = ' + fx(Math.abs(L1 - L2), 2) + ' 公尺還近，手臂折不回來。') + '真實的機器人也會遇到這種「工作空間」限制。'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 粒子濾波 ---------- */
  function initPf(root, cfg) { head(root, cfg.q); var L = 100, doors = [12, 28, 61], N = 400, R, pts, robot, step, v = el('div'), inf, log;
    var b = row(root); bt(b, '移動 4 公尺並量測', function () { move(); draw(); }); bt(b, '重設（不知道自己在哪）', function () { reset(); draw(); });
    root.appendChild(v); inf = info(root);
    function isDoor(x) { return doors.some(function (d) { return Math.abs(x - d) < 3; }); }
    function reset() { R = rng(11); pts = []; for (var i = 0; i < N; i++) pts.push(R() * L); robot = 3; step = 0; log = '機器人知道走廊的地圖（三扇門的位置），但不知道自己在哪裡：粒子平均分布在整條走廊。'; }
    function move() { robot = (robot + 4) % L; step++; var z = isDoor(robot), w = [], sw = 0;
      pts = pts.map(function (p) { return ((p + 4 + gauss(R) * 0.8) % L + L) % L; });
      pts.forEach(function (p) { var ww = isDoor(p) === z ? 0.85 : 0.1; w.push(ww); sw += ww; });
      var np = [], c = [], acc = 0; w.forEach(function (x) { acc += x / sw; c.push(acc); }); for (var i = 0; i < N; i++) { var r = R(), j = 0; while (j < N - 1 && c[j] < r) j++; np.push(pts[j]); } pts = np;
      log = '第 ' + step + ' 步：感測器回報「' + (z ? '<b>看到門</b>' : '沒有門') + '」。和量測不符的粒子權重變低、在重抽樣時被淘汰。'; }
    function draw() { var S = 6.4, g = '', H = 170, hist = new Array(50).fill(0);
      pts.forEach(function (p) { hist[Math.min(49, Math.floor(p / 2))]++; }); var mx = Math.max.apply(null, hist) || 1;
      doors.forEach(function (d) { g += '<rect x="' + n1(20 + (d - 3) * S) + '" y="20" width="' + n1(6 * S) + '" height="40" fill="' + OR + '" fill-opacity="0.35"/>' + tx(20 + d * S, 16, '門', 10, OR); });
      g += '<rect x="20" y="60" width="' + (L * S) + '" height="4" fill="' + GY + '"/>';
      hist.forEach(function (h, i) { var bh = h / mx * 66; g += '<rect x="' + n1(20 + i * 2 * S) + '" y="' + n1(150 - bh) + '" width="' + n1(2 * S - 1) + '" height="' + n1(bh) + '" fill="' + BL + '" fill-opacity="0.7"/>'; });
      g += '<circle cx="' + n1(20 + robot * S) + '" cy="44" r="9" fill="' + GN + '"/>' + tx(20 + robot * S, 48, '🤖', 11, '#fff') + tx(20, 166, '0', 9, 'var(--text-muted)', 'start') + tx(20 + L * S, 166, L + ' 公尺', 9, 'var(--text-muted)', 'end') + tx(22, 78, '粒子分布', 9, 'var(--text-muted)', 'start');
      v.innerHTML = svgw('0 0 680 ' + H, g); var m = 0; pts.forEach(function (p) { m += p; }); m /= N; var sd = 0; pts.forEach(function (p) { sd += (p - m) * (p - m); }); sd = Math.sqrt(sd / N);
      inf.innerHTML = log + '<br>粒子分布的離散程度約 <b>' + fx(sd) + ' 公尺</b>' + (sd < 4 ? '——已經收斂，機器人「知道」自己在哪了（實際位置 ' + fx(robot) + ' 公尺）。' : '——還有好幾個可能的位置。多走幾步，經過幾扇門之後就會收斂。'); }
    reset(); draw(); }

  /* ---------- 路徑規劃 ---------- */
  function initPlan(root, cfg) { head(root, cfg.q); var W = 24, H = 14, mode = cfg.m || 'astar', seed = 3, grid, v = el('div'), inf;
    var b = row(root); [['A*', 'astar'], ['Dijkstra', 'dij'], ['RRT（連續空間）', 'rrt']].forEach(function (m) { var x = btn(m[0], m[1]); x.onclick = function () { mode = m[1]; mark(b, mode); draw(); }; b.appendChild(x); }); mark(b, mode);
    var b2 = row(root); bt(b2, '換一張地圖', function () { seed = seed * 5 % 997 + 2; mk(); draw(); });
    root.appendChild(v); inf = info(root);
    function mk() { var R = rng(seed); grid = []; for (var y = 0; y < H; y++) { grid.push([]); for (var x = 0; x < W; x++) grid[y].push(R() < 0.24 ? 1 : 0); } for (var k = 0; k < 4; k++) { var wx = 4 + Math.floor(R() * 16), wy = Math.floor(R() * 6); for (var y2 = wy; y2 < wy + 8 && y2 < H; y2++) grid[y2][wx] = 1; } grid[1][1] = grid[H - 2][W - 2] = 0; grid[1][2] = grid[2][1] = grid[H - 2][W - 3] = grid[H - 3][W - 2] = 0; }
    function search(astar) { var S = [1, 1], G = [W - 2, H - 2], key = function (x, y) { return y * W + x; }, open = [[0, 0, S[0], S[1]]], gs = {}, par = {}, seen = {}, n = 0; gs[key(S[0], S[1])] = 0;
      var hfn = function (x, y) { var dx = Math.abs(x - G[0]), dy = Math.abs(y - G[1]); return astar ? Math.max(dx, dy) + 0.414 * Math.min(dx, dy) : 0; };
      while (open.length) { open.sort(function (a, b) { return a[0] - b[0]; }); var c = open.shift(), cx = c[2], cy = c[3], k = key(cx, cy); if (seen[k]) continue; seen[k] = 1; n++;
        if (cx === G[0] && cy === G[1]) { var p = [], kk = k; while (kk !== undefined) { p.push([kk % W, Math.floor(kk / W)]); kk = par[kk]; } return { path: p, seen: seen, n: n, len: gs[k] }; }
        for (var dx = -1; dx <= 1; dx++) for (var dy = -1; dy <= 1; dy++) { if (!dx && !dy) continue; var nx = cx + dx, ny = cy + dy; if (nx < 0 || ny < 0 || nx >= W || ny >= H || grid[ny][nx]) continue; if (dx && dy && (grid[cy][nx] || grid[ny][cx])) continue;
          var ng = gs[k] + (dx && dy ? 1.414 : 1), nk = key(nx, ny); if (gs[nk] === undefined || ng < gs[nk]) { gs[nk] = ng; par[nk] = k; open.push([ng + hfn(nx, ny), ng, nx, ny]); } } }
      return { path: null, seen: seen, n: n }; }
    function rrt() { var R = rng(seed * 3 + 1), T = [[1.5, 1.5, -1]], goal = [W - 1.5, H - 1.5], free = function (x, y) { var gx = Math.floor(x), gy = Math.floor(y); return gx >= 0 && gy >= 0 && gx < W && gy < H && !grid[gy][gx]; }, it = 0, found = -1;
      var seg = function (a, b) { for (var t = 0; t <= 1; t += 0.05) if (!free(a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)) return false; return true; };
      while (it < 3000 && found < 0) { it++; var q = R() < 0.1 ? goal : [R() * W, R() * H], bi = 0, bd = 1e9; T.forEach(function (n, i) { var d = Math.hypot(n[0] - q[0], n[1] - q[1]); if (d < bd) { bd = d; bi = i; } });
        var nn = T[bi], st = Math.min(1, bd), nw = [nn[0] + (q[0] - nn[0]) / (bd || 1) * st, nn[1] + (q[1] - nn[1]) / (bd || 1) * st, bi]; if (!free(nw[0], nw[1]) || !seg(nn, nw)) continue; T.push(nw); if (Math.hypot(nw[0] - goal[0], nw[1] - goal[1]) < 1 && seg(nw, goal)) { T.push([goal[0], goal[1], T.length - 1]); found = T.length - 1; } }
      return { T: T, found: found, it: it }; }
    function draw() { var C = 26, g = '', ox = 28, oy = 6;
      for (var y = 0; y < H; y++) for (var x = 0; x < W; x++) if (grid[y][x]) g += '<rect x="' + (ox + x * C) + '" y="' + (oy + y * C) + '" width="' + C + '" height="' + C + '" fill="' + GY + '"/>';
      var msg;
      if (mode !== 'rrt') { var r = search(mode === 'astar'); Object.keys(r.seen).forEach(function (k) { var x = k % W, y = Math.floor(k / W); g += '<rect x="' + (ox + x * C + 2) + '" y="' + (oy + y * C + 2) + '" width="' + (C - 4) + '" height="' + (C - 4) + '" fill="' + BL + '" fill-opacity="0.18"/>'; });
        if (r.path) { var d = ''; r.path.forEach(function (p, i) { d += (i ? 'L' : 'M') + (ox + p[0] * C + C / 2) + ' ' + (oy + p[1] * C + C / 2); }); g += '<path d="' + d + '" fill="none" stroke="' + OR + '" stroke-width="4" stroke-linejoin="round"/>'; }
        msg = (mode === 'astar' ? '<b>A*</b>' : '<b>Dijkstra</b>') + '：探索了 <b>' + r.n + '</b> 格（淡藍色），' + (r.path ? '找到長度約 <b>' + fx(r.len) + '</b> 格的最短路徑。' : '找不到路徑，換一張地圖試試。') + (mode === 'astar' ? '<br>A* 用「到終點的估計距離」引導搜尋方向，所以探索的格子通常比 Dijkstra 少很多，但仍保證最短。' : '<br>Dijkstra 不知道終點在哪個方向，像水波一樣往四面八方擴散。切換到 A* 比較看看。'); }
      else { var r2 = rrt(); r2.T.forEach(function (n) { if (n[2] >= 0) { var p = r2.T[n[2]]; g += ln(ox + p[0] * C, oy + p[1] * C, ox + n[0] * C, oy + n[1] * C, BL, 1); } });
        if (r2.found >= 0) { var i = r2.found, d2 = ''; while (i >= 0) { var n = r2.T[i]; d2 += (d2 ? 'L' : 'M') + n1(ox + n[0] * C) + ' ' + n1(oy + n[1] * C); i = n[2]; } g += '<path d="' + d2 + '" fill="none" stroke="' + OR + '" stroke-width="4" stroke-linejoin="round"/>'; }
        msg = '<b>RRT</b>：隨機撒點、從樹上最近的節點往那裡長一小段，長了 <b>' + r2.T.length + '</b> 個節點' + (r2.found >= 0 ? '後碰到終點。' : '，還沒找到終點。') + '<br>RRT 不保證最短（路徑彎彎曲曲，實務上會再「拉直」），但在高維度空間（例如 7 軸手臂）中比網格搜尋實用得多。'; }
      g += '<circle cx="' + (ox + 1.5 * C) + '" cy="' + (oy + 1.5 * C) + '" r="9" fill="' + GN + '"/>' + tx(ox + 1.5 * C, oy + 1.5 * C + 4, '起', 10, '#fff') + '<circle cx="' + (ox + (W - 1.5) * C) + '" cy="' + (oy + (H - 1.5) * C) + '" r="9" fill="' + RD + '"/>' + tx(ox + (W - 1.5) * C, oy + (H - 1.5) * C + 4, '終', 10, '#fff');
      v.innerHTML = svgw('0 0 680 ' + (H * C + 12), g); inf.innerHTML = msg; }
    mk(); draw(); }

  /* ---------- 感測器資料量 ---------- */
  function initSensor(root, cfg) { head(root, cfg.q); var P = { cam: 8, mp: 5, fps: 30, bit: 12, lid: 1, pps: 2.4, rad: 5, fleet: 1000, hr: 12 }, v = el('div'), inf, ups = [];
    var b = row(root); [['特斯拉式（純鏡頭）', [8, 5, 36, 12, 0, 0, 0]], ['Waymo 式（鏡頭＋光達＋雷達）', [13, 5, 30, 12, 4, 2.4, 6]], ['人形機器人', [6, 2, 30, 10, 0, 0, 0]]].forEach(function (p) { bt(b, p[0], function () { var s = root.querySelectorAll('input[type=range]'); ['cam', 'mp', 'fps', 'bit', 'lid', 'pps', 'rad'].forEach(function (k, i) { s[i].value = p[1][i]; }); ups.forEach(function (u) { u(); }); }); });
    ups.push(sl(root, '鏡頭數量', 0, 16, 1, P.cam, null, function (x) { P.cam = x; draw(); }));
    ups.push(sl(root, '每顆鏡頭畫素（百萬）', 1, 12, 0.5, P.mp, null, function (x) { P.mp = x; draw(); }));
    ups.push(sl(root, '每秒幀數', 10, 60, 1, P.fps, null, function (x) { P.fps = x; draw(); }));
    ups.push(sl(root, '每個畫素的位元數（原始影像）', 8, 16, 1, P.bit, null, function (x) { P.bit = x; draw(); }));
    ups.push(sl(root, '光達數量', 0, 6, 1, P.lid, null, function (x) { P.lid = x; draw(); }));
    ups.push(sl(root, '每顆光達每秒點數（百萬點）', 0, 5, 0.1, P.pps, null, function (x) { P.pps = x; draw(); }));
    ups.push(sl(root, '毫米波雷達數量', 0, 8, 1, P.rad, null, function (x) { P.rad = x; draw(); }));
    ups.push(sl(root, '車隊規模（台）', 10, 100000, 10, P.fleet, function (x) { return x.toLocaleString(); }, function (x) { P.fleet = x; draw(); }));
    ups.push(sl(root, '每台每天運作時數', 1, 24, 1, P.hr, null, function (x) { P.hr = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function draw() { var cam = P.cam * P.mp * 1e6 * P.fps * P.bit, lid = P.lid * P.pps * 1e6 * 16 * 8, rad = P.rad * 10e6, tot = cam + lid + rad;
      v.innerHTML = bars([['鏡頭', cam / 1e9, BL, fx(cam / 1e9, 2) + ' Gbps'], ['光達', lid / 1e9, OR, fx(lid / 1e9, 2) + ' Gbps'], ['毫米波雷達', rad / 1e9, GN, fx(rad / 1e9, 2) + ' Gbps']]);
      var tbh = tot / 8 / 1e12 * 3600, day = tbh * P.hr * P.fleet;
      inf.innerHTML = '原始資料量合計約 <b>' + fx(tot / 1e9, 2) + ' Gbps</b>，每小時約 <b>' + fx(tbh, 2) + ' TB</b>（未壓縮）。<br>整個車隊每天約產生 <b>' + (day >= 1000 ? fx(day / 1000, 1) + ' PB' : fx(day, 1) + ' TB') + '</b>。' +
        '<br>所以實務上：車上的晶片要能<b>即時</b>處理每秒數 Gb 的資料；而且只有一小部分（有趣的、罕見的場景）會被壓縮後上傳到雲端訓練。<br><span style="color:var(--text-muted);font-size:0.9em">光達每點以約 16 位元組計（座標、強度、時間），雷達每顆以約 10 Mbps 粗估。實際系統多在感測器端做初步處理與壓縮，送進主晶片的資料量會小一些。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 算力與頻寬 ---------- */
  var CHIPS = [['Jetson AGX Orin（2022）', 138, 205, 64], ['Jetson AGX Thor（2025）', 517, 273, 128], ['資料中心 H100（參考）', 1979, 3350, 80]];
  function initCompute(root, cfg) { head(root, cfg.q); var P = { b: 3, byt: 1, tok: 800, hz: 10, ar: 20 }, v = el('div'), inf, ups = [];
    var b = row(root); [['小型 VLA（30 億參數）', [3, 1, 800, 10, 20]], ['大型 VLA（70 億參數）', [7, 1, 1000, 5, 20]], ['自駕端到端（10 億參數）', [1, 1, 3000, 30, 1]], ['「快慢腦」的慢腦（70 億參數）', [7, 0.5, 600, 2, 30]]].forEach(function (p) { bt(b, p[0], function () { var s = root.querySelectorAll('input[type=range]'); p[1].forEach(function (x, i) { s[i].value = x; }); ups.forEach(function (u) { u(); }); }); });
    ups.push(sl(root, '模型參數（十億）', 0.1, 70, 0.1, P.b, null, function (x) { P.b = x; draw(); }));
    ups.push(sl(root, '每個參數的位元組（FP16=2、FP8=1、FP4=0.5）', 0.5, 2, 0.5, P.byt, null, function (x) { P.byt = x; draw(); }));
    ups.push(sl(root, '每次推論輸入的 token 數（影像＋文字）', 100, 4000, 50, P.tok, null, function (x) { P.tok = x; draw(); }));
    ups.push(sl(root, '每秒推論幾次（控制頻率）', 1, 60, 1, P.hz, null, function (x) { P.hz = x; draw(); }));
    ups.push(sl(root, '每次要逐一產生幾個輸出 token（動作）', 1, 60, 1, P.ar, null, function (x) { P.ar = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function draw() { var fl = 2 * P.b * 1e9 * (P.tok + P.ar), tf = fl * P.hz / 1e12, mem = P.b * P.byt, bw = mem * P.ar * P.hz;
      var rows = CHIPS.map(function (c) { var byC = c[1] * 1e12 * 0.35 / fl, byB = c[2] / (mem * P.ar), hz = Math.min(byC, byB), fit = mem <= c[3] * 0.7;
        return '<tr>' + cell(c[0]) + cell(fit ? fx(hz, 1) + ' 次／秒' : '<span style="color:' + RD + '">放不下</span>', 'text-align:right') + cell(fit ? (byB < byC ? '<span style="color:' + OR + '">記憶體頻寬</span>' : '算力') : '記憶體容量', 'text-align:center') + cell(fit && hz >= P.hz ? '<span style="color:' + GN + '">✔ 夠用</span>' : '<span style="color:' + RD + '">✘ 不夠</span>', 'text-align:center') + '</tr>'; });
      v.innerHTML = bars([['需要的算力', tf, BL, fx(tf, 1) + ' TFLOPS（有效）'], ['權重大小', mem, OR, fx(mem, 1) + ' GB'], ['需要的頻寬', bw, PU, fx(bw, 0) + ' GB/s']]) + tbl(['晶片（有效算力約為標稱的 35%）', '最多每秒推論', '瓶頸', '是否滿足'], rows);
      inf.innerHTML = '每次推論約 <b>' + fx(fl / 1e12, 2) + ' 兆次浮點運算</b>；每秒 ' + P.hz + ' 次，需要約 <b>' + fx(tf, 1) + ' TFLOPS</b> 的有效算力。<br>產生動作時，每個輸出 token 都要把全部權重（' + fx(mem, 1) + ' GB）從記憶體讀一次，所以需要約 <b>' + fx(bw, 0) + ' GB/s</b> 的頻寬——<b>這常常才是真正的瓶頸</b>。' +
        '<br><span style="color:var(--text-muted);font-size:0.9em">粗估：每個參數每處理一個 token 約 2 次運算。晶片數字：Orin 以 INT8 密集約 138 TOPS、Thor 以 FP8 密集約 517 TFLOPS 估計（標稱 FP4 稀疏峰值 2,070）、H100 以 FP8 密集約 1,979 TFLOPS；頻寬分別約 205、273、3,350 GB/s。實際效能依軟體最佳化差異很大。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 功耗與電池 ---------- */
  function initPower(root, cfg) { head(root, cfg.q); var mode = cfg.m || 'hum', box = el('div'), v = el('div'), inf;
    var b = row(root); [['人形機器人', 'hum'], ['Robotaxi', 'taxi']].forEach(function (m) { var x = btn(m[0], m[1]); x.onclick = function () { mode = m[1]; mark(b, mode); build(); }; b.appendChild(x); }); mark(b, mode);
    root.appendChild(box); root.appendChild(v); inf = info(root); var P = {};
    function build() { box.innerHTML = ''; var ups = [];
      if (mode === 'hum') { P = { kwh: 2.3, walk: 400, stand: 120, cpu: 100, wf: 40 };
        ups.push(sl(box, '電池容量（kWh）', 0.5, 5, 0.1, P.kwh, null, function (x) { P.kwh = x; draw(); }));
        ups.push(sl(box, '行走時致動器功率（W）', 100, 1200, 20, P.walk, null, function (x) { P.walk = x; draw(); }));
        ups.push(sl(box, '站立與操作時致動器功率（W）', 30, 500, 10, P.stand, null, function (x) { P.stand = x; draw(); }));
        ups.push(sl(box, '運算與感測器功率（W）', 20, 400, 10, P.cpu, null, function (x) { P.cpu = x; draw(); }));
        ups.push(sl(box, '行走時間占比（%）', 0, 100, 5, P.wf, null, function (x) { P.wf = x; draw(); })); }
      else { P = { kwh: 75, whkm: 160, spd: 25, cpu: 1000, hr: 16 };
        ups.push(sl(box, '電池容量（kWh）', 40, 120, 5, P.kwh, null, function (x) { P.kwh = x; draw(); }));
        ups.push(sl(box, '車輛行駛耗電（Wh／公里）', 100, 250, 5, P.whkm, null, function (x) { P.whkm = x; draw(); }));
        ups.push(sl(box, '市區平均車速（公里／小時）', 10, 60, 1, P.spd, null, function (x) { P.spd = x; draw(); }));
        ups.push(sl(box, '自駕運算＋感測器＋散熱功率（W）', 100, 3000, 50, P.cpu, null, function (x) { P.cpu = x; draw(); })); }
      ups.forEach(function (u) { u(); }); }
    function draw() { if (mode === 'hum') { var act = P.walk * P.wf / 100 + P.stand * (1 - P.wf / 100), tot = act + P.cpu, h = P.kwh * 1000 * 0.9 / tot;
        v.innerHTML = bars([['致動器（平均）', act, OR, Math.round(act) + ' W'], ['運算與感測器', P.cpu, BL, Math.round(P.cpu) + ' W']]);
        inf.innerHTML = '平均總功率約 <b>' + Math.round(tot) + ' W</b>，一次充電約可工作 <b>' + fx(h, 1) + ' 小時</b>（保留 10% 電量）。電池重量約 <b>' + fx(P.kwh * 1000 / 220, 1) + ' 公斤</b>（以每公斤約 220 Wh 估計）。<br>' +
          (h < 4 ? '一個 8 小時班次需要中途換電池或充電——這是人形機器人進工廠的實際挑戰。' : h >= 8 ? '可以撐完一個 8 小時班次。' : '大約半個到一個班次，需要排定充電時間。') + '<br><span style="color:var(--text-muted);font-size:0.9em">參考：特斯拉 2022 年發表的 Optimus 原型使用 2.3 kWh 電池，公司宣稱靜坐約 100 W、快走約 500 W。</span>'; }
      else { var drv = P.whkm * P.spd, tot2 = drv + P.cpu, loss = P.cpu / tot2 * 100, rng0 = P.kwh * 1000 / P.whkm, rng1 = P.kwh * 1000 / (tot2 / P.spd), hrs = P.kwh * 1000 / tot2;
        v.innerHTML = bars([['行駛', drv, GN, Math.round(drv) + ' W'], ['自駕系統', P.cpu, BL, Math.round(P.cpu) + ' W']]);
        inf.innerHTML = '以平均時速 ' + P.spd + ' 公里行駛，車輛本身耗電約 ' + fx(drv / 1000, 2) + ' kW，自駕系統占總耗電的 <b>' + fx(loss, 0) + '%</b>。<br>續航從約 ' + Math.round(rng0) + ' 公里降到約 <b>' + Math.round(rng1) + ' 公里</b>（少 ' + fx((1 - rng1 / rng0) * 100, 0) + '%），一次充電可營運約 <b>' + fx(hrs, 1) + ' 小時</b>。<br>' +
          (loss > 15 ? '市區車速慢、停等多時，自駕系統的固定耗電影響特別大——這是 robotaxi 追求低功耗晶片的原因。' : '高速行駛時，自駕系統的耗電占比較小。') + '<br><span style="color:var(--text-muted);font-size:0.9em">早期 robotaxi 原型的運算與感測器常耗電數千瓦；新一代系統已大幅降低。</span>'; } }
    build(); }

  /* ---------- Robotaxi 經濟學 ---------- */
  function initTaxi(root, cfg) { head(root, cfg.q); var P = { car: 80000, life: 6, hr: 16, spd: 22, paid: 55, energy: 0.04, mnt: 0.12, ratio: 20, wage: 30, price: 1.2, drv: 30 }, v = el('div'), inf, ups = [];
    var b = row(root); [['早期（2020 年前後）', [180000, 5, 12, 20, 45, 0.05, 0.2, 3, 30, 1.6]], ['現在（2026 年前後）', [80000, 6, 16, 22, 55, 0.04, 0.12, 20, 30, 1.2]], ['目標（量產專用車）', [30000, 7, 18, 24, 60, 0.03, 0.08, 50, 30, 0.8]]].forEach(function (p) { bt(b, p[0], function () { var s = root.querySelectorAll('input[type=range]'); p[1].forEach(function (x, i) { s[i].value = x; }); ups.forEach(function (u) { u(); }); }); });
    ups.push(sl(root, '整車成本含感測器（美元）', 20000, 250000, 5000, P.car, function (x) { return '$' + x.toLocaleString(); }, function (x) { P.car = x; draw(); }));
    ups.push(sl(root, '使用年限（年）', 3, 10, 1, P.life, null, function (x) { P.life = x; draw(); }));
    ups.push(sl(root, '每天營運時數', 4, 22, 1, P.hr, null, function (x) { P.hr = x; draw(); }));
    ups.push(sl(root, '平均車速（公里／小時）', 10, 40, 1, P.spd, null, function (x) { P.spd = x; draw(); }));
    ups.push(sl(root, '載客里程比例（%）', 30, 80, 1, P.paid, null, function (x) { P.paid = x; draw(); }));
    ups.push(sl(root, '電費（美元／公里）', 0.01, 0.1, 0.01, P.energy, null, function (x) { P.energy = x; draw(); }));
    ups.push(sl(root, '維修、保險、清潔、場站（美元／公里）', 0.03, 0.4, 0.01, P.mnt, null, function (x) { P.mnt = x; draw(); }));
    ups.push(sl(root, '一位遠端協助人員負責幾台車', 1, 100, 1, P.ratio, null, function (x) { P.ratio = x; draw(); }));
    ups.push(sl(root, '遠端人員與司機時薪（美元）', 10, 50, 1, P.wage, null, function (x) { P.wage = x; draw(); }));
    ups.push(sl(root, '每載客公里收費（美元）', 0.4, 3, 0.05, P.price, null, function (x) { P.price = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function draw() { var km = P.hr * P.spd * 365, pkm = km * P.paid / 100, dep = P.car / P.life, en = km * P.energy, mn = km * P.mnt, ra = P.wage * P.hr * 365 / P.ratio, cost = dep + en + mn + ra, cpk = cost / pkm, rev = pkm * P.price, drvc = P.wage * P.hr * 365;
      v.innerHTML = bars([['折舊', dep / pkm, BL, '$' + fx(dep / pkm, 2)], ['電費', en / pkm, GN, '$' + fx(en / pkm, 2)], ['維修保險清潔', mn / pkm, OR, '$' + fx(mn / pkm, 2)], ['遠端協助', ra / pkm, PU, '$' + fx(ra / pkm, 2)], ['（對照）人類司機薪資', drvc / pkm, GY, '$' + fx(drvc / pkm, 2)]]);
      inf.innerHTML = '每台車一年行駛約 <b>' + Math.round(km).toLocaleString() + ' 公里</b>，其中載客約 ' + Math.round(pkm).toLocaleString() + ' 公里。<br>每載客公里成本約 <b>$' + fx(cpk, 2) + '</b>，收費 $' + fx(P.price, 2) + '，每台車每年 <b>' + (rev >= cost ? '獲利' : '虧損') + '約 $' + Math.round(Math.abs(rev - cost)).toLocaleString() + '</b>。<br>' +
        '如果改用人類司機（同樣時數），光薪資每載客公里就要約 $' + fx(drvc / pkm, 2) + '。<b>Robotaxi 的成本優勢，關鍵在三件事：車輛成本、利用率、一個遠端人員能管多少台車。</b>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 人形回本 ---------- */
  function initRoi(root, cfg) { head(root, cfg.q); var P = { price: 100000, mnt: 15, life: 5, shift: 2, prod: 25, wage: 60000 }, v = el('div'), inf, ups = [];
    var b = row(root); [['美國工廠，今天的價格與效率', [100000, 15, 5, 2, 25, 60000]], ['美國工廠，量產後', [30000, 8, 6, 2, 70, 60000]], ['台灣工廠，量產後', [30000, 8, 6, 2, 70, 25000]], ['低價人形（中國）', [16000, 12, 4, 2, 35, 15000]]].forEach(function (p) { bt(b, p[0], function () { var s = root.querySelectorAll('input[type=range]'); p[1].forEach(function (x, i) { s[i].value = x; }); ups.forEach(function (u) { u(); }); }); });
    ups.push(sl(root, '售價（美元）', 5000, 200000, 1000, P.price, function (x) { return '$' + x.toLocaleString(); }, function (x) { P.price = x; draw(); }));
    ups.push(sl(root, '每年維護與軟體費（售價的 %）', 0, 30, 1, P.mnt, null, function (x) { P.mnt = x; draw(); }));
    ups.push(sl(root, '使用年限（年）', 2, 10, 1, P.life, null, function (x) { P.life = x; draw(); }));
    ups.push(sl(root, '每天工作幾個 8 小時班次', 1, 3, 1, P.shift, null, function (x) { P.shift = x; draw(); }));
    ups.push(sl(root, '相對人類的工作效率（%）', 10, 120, 5, P.prod, null, function (x) { P.prod = x; draw(); }));
    ups.push(sl(root, '一位工人一年的人事成本（美元，含保險福利）', 8000, 100000, 1000, P.wage, function (x) { return '$' + x.toLocaleString(); }, function (x) { P.wage = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function draw() { var yearly = P.price * P.mnt / 100, save = P.wage * P.shift * P.prod / 100, net = save - yearly, pay = net > 0 ? P.price / net : Infinity, hrs = P.shift * 8 * 250, cph = (P.price / P.life + yearly) / hrs / (P.prod / 100), hph = P.wage / 2000;
      var d = [], acc = -P.price; for (var t = 0; t <= P.life; t++) { d.push([t, acc / 1000]); acc += net; }
      v.innerHTML = chart(680, 220, [{ d: d, c: net > 0 ? GN : RD, n: '累積淨效益（千美元）' }], { x0: 0, x1: P.life, y1: Math.max(10, d[d.length - 1][1] * 1.1), xl: '年', hl: [{ y: 0, n: '回本線', c: GY }] });
      inf.innerHTML = '每年可節省的人事成本約 <b>$' + Math.round(save).toLocaleString() + '</b>，扣掉維護費後淨效益約 $' + Math.round(net).toLocaleString() + '。<br>' + (isFinite(pay) ? '回本期約 <b>' + fx(pay, 1) + ' 年</b>' + (pay > P.life ? '，<span style="color:' + RD + '">超過使用年限，不划算</span>。' : '，使用年限內總共淨賺約 $' + Math.round(net * P.life - P.price).toLocaleString() + '。') : '<span style="color:' + RD + '">節省的成本不夠付維護費，永遠回不了本。</span>') +
        '<br>機器人每「等效工時」成本約 <b>$' + fx(cph, 1) + '</b>，人類約 $' + fx(hph, 1) + '。<br><span style="color:var(--text-muted);font-size:0.9em">關鍵變數是<b>工作效率</b>：今天的人形機器人在多數工作上速度與可靠度仍明顯低於人類；能做兩、三班則大幅改善經濟效益。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 全球需求推算 ---------- */
  function initDemand(root, cfg) { head(root, cfg.q); var P = { hum: 1000000, taxi: 200000, act: 40, kwh: 2.5, hcam: 6, tcam: 12, tlid: 3 }, v = el('div'), inf, ups = [];
    var b = row(root); [['2026 年前後', [50000, 20000]], ['保守的 2030 年', [300000, 100000]], ['樂觀的 2030 年', [2000000, 500000]], ['樂觀的 2035 年', [10000000, 3000000]]].forEach(function (p) { bt(b, p[0], function () { var s = root.querySelectorAll('input[type=range]'); s[0].value = p[1][0]; s[1].value = p[1][1]; ups.forEach(function (u) { u(); }); }); });
    ups.push(sl(root, '人形機器人年出貨量（台）', 10000, 20000000, 10000, P.hum, function (x) { return x.toLocaleString(); }, function (x) { P.hum = x; draw(); }));
    ups.push(sl(root, 'Robotaxi 年新增量（台）', 1000, 5000000, 1000, P.taxi, function (x) { return x.toLocaleString(); }, function (x) { P.taxi = x; draw(); }));
    ups.push(sl(root, '每台人形的致動器（關節）數', 20, 60, 1, P.act, null, function (x) { P.act = x; draw(); }));
    ups.push(sl(root, '每台人形的電池（kWh）', 1, 5, 0.1, P.kwh, null, function (x) { P.kwh = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function draw() { var acts = P.hum * P.act, bat = P.hum * P.kwh / 1e6, chips = P.hum + P.taxi * 2, cams = P.hum * P.hcam + P.taxi * P.tcam, lid = P.taxi * P.tlid, red = P.hum * P.act * 0.5, screw = P.hum * 14 * (P.act / 40);
      v.innerHTML = tbl(['硬體', '年需求量', '說明'], [
        '<tr>' + cell('致動器（馬達＋減速器＋驅動）') + cell(big(acts) + ' 組', 'text-align:right') + cell('每台 ' + P.act + ' 個關節') + '</tr>',
        '<tr>' + cell('其中精密減速器（諧波、行星）') + cell('約 ' + big(red) + ' 個', 'text-align:right') + cell('約一半的旋轉關節') + '</tr>',
        '<tr>' + cell('其中行星滾柱螺桿（線性致動器）') + cell('約 ' + big(screw) + ' 支', 'text-align:right') + cell('以特斯拉 2022 年原型的 14 個線性致動器比例估計') + '</tr>',
        '<tr>' + cell('電池') + cell(fx(bat, 2) + ' GWh', 'text-align:right') + cell('全球電動車電池需求約 1,000 GWh（2024 年前後）') + '</tr>',
        '<tr>' + cell('AI 運算模組') + cell(big(chips) + ' 顆', 'text-align:right') + cell('robotaxi 以每台 2 顆（冗餘）計') + '</tr>',
        '<tr>' + cell('鏡頭模組') + cell(big(cams) + ' 顆', 'text-align:right') + cell('人形 6 顆、robotaxi 12 顆') + '</tr>',
        '<tr>' + cell('光達') + cell(big(lid) + ' 顆', 'text-align:right') + cell('robotaxi 每台 3 顆（純視覺路線則為 0）') + '</tr>']);
      inf.innerHTML = '在這組假設下，光是人形機器人每年就需要約 <b>' + big(acts) + ' 組致動器</b>。對照：全球工業機器人一年安裝約 50 萬台、每台約 6 軸，相當於每年約 300 萬組關節。' +
        (acts > 3e6 ? '<br>也就是說，人形機器人若達到這個規模，<b>精密傳動零件的需求將是今天工業機器人市場的 ' + fx(acts / 3e6, 0) + ' 倍</b>——這正是減速器、螺桿、伺服馬達供應鏈（包括台灣的上銀、台達電等）受到關注的原因。' : '<br>這個規模下，現有的工業機器人供應鏈還應付得來。') +
        '<br><span style="color:var(--text-muted);font-size:0.9em">電池需求即使在樂觀情境下也遠小於電動車，所以電池不是瓶頸；真正的瓶頸在精密傳動零件與 AI 晶片。</span>'; }
    ups.forEach(function (u) { u(); }); }

  var INIT = { pid: initPid, kalman: initKalman, ik: initIk, pf: initPf, plan: initPlan, sensor: initSensor, compute: initCompute, power: initPower, taxi: initTaxi, roi: initRoi, demand: initDemand };
  function boot() { document.querySelectorAll('.rbt-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🤖", note=RBT_NOTE):
    return make_with(icon, note, [("rbt-w", RBTLIB)])


lesson = make()
