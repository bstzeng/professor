# -*- coding: utf-8 -*-
"""〈睡眠的科學〉（slp_）共用：課程包裝與 SLLIB 互動元件（class="sl-w"）。

  hypno    睡眠週期圖（一夜的睡眠階段）
  twoproc  兩歷程模型（睡眠壓力＋生理時鐘）
  caff     咖啡因殘留計算
  debt     睡眠負債與社交時差
  jetlag   時差調整計畫
"""
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

SL_NOTE = u"本課程為衛教知識介紹，不能取代醫療診斷；長期失眠、嚴重打鼾或白天過度嗜睡，請諮詢睡眠專科或家醫科醫師。互動工具為簡化模型，數值僅供參考。"
F = D


def sw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("sl-w", cfg)


SLLIB = r"""
(function () {
  if (window.__slLib) return; window.__slLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#9aa3ad', TL = '#2a9d8f', YL = '#d4a017';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function row(root) { var d = el('div'); root.appendChild(d); return d; }
  function fx(v, d) { return (+v).toFixed(d === undefined ? 1 : d); }
  function sl(root, lab, mn, mx, st, val, fmt, cb) { return slider(root, lab, mn, mx, st, val, fmt || function (x) { return x; }, null, cb); }
  function hm(h) { h = ((h % 24) + 24) % 24; var H = Math.floor(h + 1e-9), m = Math.round((h - H) * 60); if (m === 60) { H = (H + 1) % 24; m = 0; } return (H < 10 ? '0' : '') + H + ':' + (m < 10 ? '0' : '') + m; }
  function hrs(h) { var H = Math.floor(h + 1e-9), m = Math.round((h - H) * 60); return H + ' 小時' + (m ? ' ' + m + ' 分' : ''); }

  /* ---------- 睡眠週期圖 ---------- */
  var ST = { W: [0, '清醒', RD], R: [1, '快速動眼期（REM）', PU], N1: [2, 'N1 淺睡', '#7fb3d5'], N2: [3, 'N2 淺睡', BL], N3: [4, 'N3 深睡', '#1f3b63'] };
  function initHypno(root, cfg) { head(root, cfg.q); var P = { bed: 23.5, len: 7.5, old: 0 }, v = el('div'), inf, ups = [];
    var b = row(root); [['年輕成人', 0], ['長者', 1]].forEach(function (q) { var x = btn(q[0], q[1]); x.onclick = function () { P.old = q[1]; mark(b, P.old); draw(); }; b.appendChild(x); }); mark(b, P.old);
    ups.push(sl(root, '就寢時間', 21, 26, 0.25, P.bed, hm, function (x) { P.bed = x; draw(); }));
    ups.push(sl(root, '睡眠時長', 4, 10, 0.25, P.len, hrs, function (x) { P.len = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function plan() { var seg = [['W', P.old ? 20 : 12]], t = seg[0][1], i = 0, tot = P.len * 60 + seg[0][1];
      while (t < tot) { var f = P.old ? 0.35 : 1, b3 = Math.max(0, (45 - 15 * i)) * f, r = Math.min(10 + 9 * i, 40), a = 20, c = Math.max(5, 90 - 5 - a - b3 - r);
        [['N1', 5], ['N2', a], ['N3', b3], ['N2', c], ['R', r]].concat(P.old && i > 0 ? [['W', 4]] : []).forEach(function (s) { if (s[1] > 0 && t < tot) { var d = Math.min(s[1], tot - t); seg.push([s[0], d]); t += d; } }); i++; }
      return { seg: seg, cyc: i, tot: tot }; }
    function draw() { var p = plan(), X = function (m) { return 70 + m / p.tot * 590; }, Y = function (k) { return 20 + ST[k][0] * 34; }, g = '', t = 0, d = '', sum = { W: 0, R: 0, N1: 0, N2: 0, N3: 0 }, last = null;
      Object.keys(ST).forEach(function (k) { g += tx(64, Y(k) + 4, ST[k][1].split('（')[0], 10.5, ST[k][2], 'end') + ln(70, Y(k), 660, Y(k), 'var(--border)', 0.5, 'stroke-dasharray="2 3"'); });
      p.seg.forEach(function (s, i) { var x1 = X(t), x2 = X(t + s[1]); d += (i ? 'L' + n1(x1) + ' ' + n1(Y(s[0])) : 'M' + n1(x1) + ' ' + n1(Y(s[0]))) + 'L' + n1(x2) + ' ' + n1(Y(s[0])); g += '<rect x="' + n1(x1) + '" y="' + n1(Y(s[0]) - 4) + '" width="' + n1(Math.max(0.5, x2 - x1)) + '" height="8" fill="' + ST[s[0]][2] + '"/>'; sum[s[0]] += s[1]; t += s[1]; last = s[0]; });
      g = '<path d="' + d + '" fill="none" stroke="var(--text-muted)" stroke-width="1" opacity="0.6"/>' + g;
      for (var h = Math.ceil(P.bed); h <= P.bed + p.tot / 60 + 0.01; h++) g += tx(X((h - P.bed) * 60), 196, hm(h).slice(0, 2) + '點', 9.5, 'var(--text-muted)');
      for (var c = 1; c < p.cyc; c++) { var xc = X((P.old ? 20 : 12) + c * 90); if (xc < 660) g += ln(xc, 12, xc, 182, GY, 0.8, 'stroke-dasharray="3 3"'); }
      v.innerHTML = svgw('0 0 680 205', g); var sleepMin = p.tot - sum.W;
      var pct = function (k) { return fx(sum[k] / sleepMin * 100, 0) + '%'; };
      inf.innerHTML = '約 <b>' + fx(sleepMin / 90, 1) + '</b> 個 90 分鐘的週期（虛線）。深睡 N3 ' + pct('N3') + '、REM ' + pct('R') + '、淺睡 N1＋N2 ' + fx((sum.N1 + sum.N2) / sleepMin * 100, 0) + '%。<br>' +
        '<b>前半夜深睡多、後半夜 REM 多</b>：所以少睡最後兩小時，損失的主要是 REM。' + (P.old ? '長者的深睡明顯減少、夜間醒來的次數增加，這是正常的老化現象。' : '') + '<br>鬧鐘響在 <b>' + hm(P.bed + p.tot / 60) + '</b>，此時正處於「' + ST[last][1] + '」。' + (last === 'N3' ? '從深睡中被叫醒，「睡眠慣性」最強，會特別昏沉。' : last === 'R' || last === 'N1' ? '從淺睡或 REM 醒來，通常比較清醒。' : '') +
        '<br><span style="color:var(--text-muted);font-size:0.9em">示意模型：真實的週期長度約 70～120 分鐘，每個人、每一晚都不同；「算準週期起床」的效果，研究證據有限。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 兩歷程模型 ---------- */
  function initTwo(root, cfg) { head(root, cfg.q); var P = { wake: 7, bed: 23.5, ph: 0, ad: 0 }, v = el('div'), inf, ups = [];
    var b = row(root); [['正常作息', 0], ['昨晚熬夜沒睡', 1]].forEach(function (q) { var x = btn(q[0], q[1]); x.onclick = function () { P.ad = q[1]; mark(b, P.ad); draw(); }; b.appendChild(x); }); mark(b, P.ad);
    ups.push(sl(root, '起床時間', 4, 12, 0.25, P.wake, hm, function (x) { P.wake = x; draw(); }));
    ups.push(sl(root, '就寢時間', 20, 28, 0.25, P.bed, hm, function (x) { P.bed = x; draw(); }));
    ups.push(sl(root, '時型（生理時鐘的早晚）', -2, 2, 0.5, P.ph, function (x) { return x === 0 ? '一般' : x < 0 ? '晨型（提早 ' + (-x) + ' 小時）' : '夜型（延後 ' + x + ' 小時）'; }, function (x) { P.ph = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function C(t) { return 0.25 * Math.cos(2 * Math.PI * (t - 18.5 - P.ph) / 24) + 0.12 * Math.cos(4 * Math.PI * (t - 9 - P.ph) / 24); }
    function draw() { var dt = 0.05, S = 0.3, res = [], bed = P.bed, wk = P.wake, len = bed - wk;
      if (len <= 2) len = 2;
      for (var day = 0; day < 6; day++) for (var h = 0; h < 24; h += dt) { var t = day * 24 + h, ht = h, awake;
        var rel = ((ht - wk) % 24 + 24) % 24; awake = rel < len; if (P.ad && day === 4 && !awake && ht >= 12) awake = true; if (P.ad && day === 5 && ht < wk) awake = true;
        S = awake ? 1 - (1 - S) * Math.exp(-dt / 18.2) : S * Math.exp(-dt / 4.2); if (day >= 4) res.push([t - 96, S, awake]); }
      var sp = [], cp = [], dp = [], bestT = null, best = -9, low = null, lowV = 9, dipT = null, dipV = -9;
      res.forEach(function (r) { var c = C(r[0] % 24), z = r[1] - c; sp.push([r[0], r[1]]); cp.push([r[0], 0.55 + c]); dp.push([r[0], r[2] ? z : NaN]);
        if (r[2] && r[0] >= 24 && r[0] < 48) { var since = ((r[0] - wk) % 24 + 24) % 24; if (z > best) { best = z; bestT = r[0]; } if (since > 1 && z < lowV) { lowV = z; low = r[0]; } var hh = r[0] % 24; if (hh >= 12 && hh <= 17 && z > dipV) { dipV = z; dipT = r[0]; } } });
      var vl = []; for (var d = 0; d < 2; d++) { vl.push({ x: d * 24 + wk, c: GN, n: '起床' }); vl.push({ x: d * 24 + bed, c: PU, n: '就寢' }); }
      v.innerHTML = chart(680, 260, [{ d: sp, c: OR, n: '睡眠壓力 S（腺苷累積）' }, { d: cp, c: BL, n: '生理時鐘 C（清醒訊號）', dash: '6 4' }, { d: dp, c: RD, n: '想睡程度（S 減 C，清醒時）', w: 2.5 }],
        { x0: 0, x1: 48, y0: -0.3, y1: 1.15, xl: '時間（小時，兩天）', vl: vl.filter(function (q) { return q.x <= 48; }) });
      var sleepH = Math.max(0, 24 - len);
      inf.innerHTML = '每天睡 <b>' + hrs(sleepH) + '</b>。第二天清醒時，<b>最清醒</b>約在 ' + hm(low) + '，<b>最想睡</b>約在 ' + hm(bestT) + (dipT !== null ? '；下午的低潮約在 ' + hm(dipT) : '') + '。<br>' +
        '睡眠壓力（橙）醒著時上升、睡著時下降；生理時鐘（藍）在傍晚發出最強的清醒訊號（所以睡前兩三小時常常反而很清醒），清晨最弱。兩者相減，就是你感覺到的睏。剛起床的那一小時因為「睡眠慣性」，實際感受會比模型更昏沉。' + (P.ad ? '<br><b>熬夜之後</b>：睡眠壓力衝到很高，即使隔天生理時鐘的清醒訊號回來，你仍然很睏——而且凌晨三四點時最難熬。' : '') +
        (sleepH < 7 ? '<br><b style="color:' + RD + '">睡不到 7 小時</b>：睡眠壓力每晚都清不乾淨，累積成睡眠負債（第 18、32 課）。' : '') +
        '<br><span style="color:var(--text-muted);font-size:0.9em">Borbély（1982）兩歷程模型的簡化版：S 以時間常數約 18 小時上升、約 4 小時下降；C 加入 12 小時的小諧波，模擬下午的低潮。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 咖啡因 ---------- */
  var DR = [['美式咖啡（中杯）', 150], ['拿鐵（中杯）', 120], ['濃縮一份', 75], ['手搖奶茶', 100], ['紅茶', 50], ['綠茶', 30], ['能量飲料', 80], ['可樂（330 毫升）', 35]];
  function initCaff(root, cfg) { head(root, cfg.q); var P = { at: 14, hl: 5, bed: 23.5 }, list = [[8, 150, '美式咖啡（中杯）'], [14, 100, '手搖奶茶']], v = el('div'), inf, ups = [];
    ups.push(sl(root, '飲用時間', 6, 22, 0.5, P.at, hm, function (x) { P.at = x; }));
    var b = row(root); DR.forEach(function (d) { var x = btn('＋' + d[0]); x.onclick = function () { list.push([P.at, d[1], d[0]]); list.sort(function (a, c) { return a[0] - c[0]; }); draw(); }; b.appendChild(x); });
    var b2 = row(root); var cl = btn('清空'); cl.onclick = function () { list = []; draw(); }; b2.appendChild(cl);
    ups.push(sl(root, '半衰期（因人而異）', 2, 9, 0.5, P.hl, function (x) { return x + ' 小時' + (x <= 3 ? '（吸菸者常較短）' : x >= 7 ? '（懷孕、口服避孕藥常較長）' : ''); }, function (x) { P.hl = x; draw(); }));
    ups.push(sl(root, '就寢時間', 20, 26, 0.25, P.bed, hm, function (x) { P.bed = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function amt(t) { var s = 0; list.forEach(function (d) { if (t >= d[0]) { var k = t - d[0], ab = Math.min(1, k / 0.75); s += d[1] * ab * Math.pow(0.5, Math.max(0, k - 0.75) / P.hl); } }); return s; }
    function draw() { var pts = []; for (var t = 6; t <= 30; t += 0.1) pts.push([t, amt(t)]); var tot = list.reduce(function (s, d) { return s + d[1]; }, 0), atBed = amt(P.bed);
      v.innerHTML = chart(680, 230, [{ d: pts, c: OR, n: '體內咖啡因（毫克）' }], { x0: 6, x1: 30, y0: 0, xl: '時間（24 以後為隔天凌晨）', vl: [{ x: P.bed, c: PU, n: '就寢' }].concat(list.map(function (d) { return { x: d[0], c: GY, n: '' }; })), hl: [{ y: 50, c: GN, n: '約 50 毫克' }] }) +
        '<div style="font-size:0.88em;margin-top:4px">今天喝的：' + (list.length ? list.map(function (d, i) { return '<span style="white-space:nowrap">' + hm(d[0]) + ' ' + d[2] + '（約 ' + d[1] + ' 毫克）</span>'; }).join('；') : '（無）') + '</div>';
      inf.innerHTML = '今天總共約 <b>' + tot + ' 毫克</b>' + (tot > 300 ? '，<b style="color:' + RD + '">超過台灣衛福部建議的成人每日 300 毫克</b>' : '') + '。就寢時體內還有約 <b>' + fx(atBed, 0) + ' 毫克</b>' + (atBed >= 50 ? '——相當於睡前喝了 ' + fx(atBed / 75, 1) + ' 份濃縮咖啡，可能讓你較難入睡，或深睡變少。' : '，影響相對小。') +
        '<br>半衰期約 ' + P.hl + ' 小時：每過一個半衰期，體內的量減半。下午兩點的一杯，到晚上十二點還剩下約 ' + fx(100 * Math.pow(0.5, 10 / P.hl), 0) + '%。很多人覺得「喝咖啡照樣睡得著」，但研究發現，睡前 6 小時攝取咖啡因，仍可能讓總睡眠時間減少。' +
        '<br><span style="color:var(--text-muted);font-size:0.9em">各飲料的咖啡因含量差異很大，數值為約略值；模型假設約 45 分鐘完全吸收、一級動力學代謝。</span>'; }
    ups.forEach(function (u) { u(); }); draw(); }

  /* ---------- 睡眠負債與社交時差 ---------- */
  function initDebt(root, cfg) { head(root, cfg.q); var P = { need: 8, wb: 24, ww: 6.5, eb: 25.5, ew: 10 }, v = el('div'), inf, ups = [];
    ups.push(sl(root, '你需要的睡眠', 6, 10, 0.25, P.need, hrs, function (x) { P.need = x; draw(); }));
    ups.push(sl(root, '平日就寢', 20, 28, 0.25, P.wb, hm, function (x) { P.wb = x; draw(); }));
    ups.push(sl(root, '平日起床', 4, 11, 0.25, P.ww, hm, function (x) { P.ww = x; draw(); }));
    ups.push(sl(root, '週末就寢', 20, 29, 0.25, P.eb, hm, function (x) { P.eb = x; draw(); }));
    ups.push(sl(root, '週末起床', 5, 14, 0.25, P.ew, hm, function (x) { P.ew = x; draw(); }));
    root.appendChild(v); inf = info(root);
    function draw() { var dW = P.ww + 24 - P.wb, dE = P.ew + 24 - P.eb; if (dW <= 0) dW = 0.5; if (dE <= 0) dE = 0.5;
      var days = ['一', '二', '三', '四', '五', '六', '日'], cum = 0, g = '', mx = 0, arr = [];
      days.forEach(function (d, i) { var s = i < 5 ? dW : dE; cum += P.need - s; arr.push([d, s, cum]); mx = Math.max(mx, Math.abs(cum)); });
      mx = Math.max(mx, 4); var neg = arr.some(function (q) { return q[2] < 0; }), pos = arr.some(function (q) { return q[2] > 0; }), Y0 = neg && pos ? 110 : neg ? 40 : 185, sc = (neg && pos ? 80 : 150) / mx;
      g += ln(40, Y0, 660, Y0, 'var(--border)', 1) + tx(36, Y0 + 4, '0', 10, 'var(--text-muted)', 'end') + tx(40, 14, '累積睡眠負債（小時，正值＝欠睡）', 10, 'var(--text-muted)', 'start');
      arr.forEach(function (a, i) { var x = 70 + i * 85, h = a[2] * sc; g += '<rect x="' + x + '" y="' + n1(h > 0 ? Y0 - h : Y0) + '" width="50" height="' + n1(Math.abs(h)) + '" rx="4" fill="' + (a[2] > 0 ? RD : GN) + '" opacity="0.8"/>' +
        tx(x + 25, h > 0 ? Y0 - h - 6 : Y0 - h + 14, (a[2] > 0 ? '+' : '') + fx(a[2], 1), 10.5, 'currentColor') + tx(x + 25, 210, '週' + a[0], 11, 'currentColor') + tx(x + 25, 224, '睡 ' + fx(a[1], 1) + ' 時', 9.5, 'var(--text-muted)'); });
      v.innerHTML = svgw('0 0 680 232', g);
      var msw = (P.wb + dW / 2), mse = (P.eb + dE / 2), sj = Math.abs(mse - msw), wkDebt = 5 * (P.need - dW);
      inf.innerHTML = '平日每晚睡 <b>' + hrs(dW) + '</b>，週末每晚睡 <b>' + hrs(dE) + '</b>。週一到週五累積的睡眠負債約 <b>' + fx(Math.max(0, wkDebt), 1) + ' 小時</b>，到週日結束時還剩 <b>' + fx(arr[6][2], 1) + ' 小時</b>。<br>' +
        '<b>社交時差</b>（平日與週末睡眠中點的差）約 <b>' + fx(sj, 1) + ' 小時</b>' + (sj >= 2 ? '：相當於每個週末都飛到另一個時區再飛回來，週一早上特別難起床（「週一症候群」）。' : sj >= 1 ? '：有一點落差。' : '：作息相當規律。') +
        '<br>週末補眠可以減輕一部分的睏，但研究發現，它無法完全抵銷平日睡眠不足對注意力與代謝的影響。比較好的方式是：平日早一點睡，讓週末起床時間和平日相差不超過一小時。' +
        '<br><span style="color:var(--text-muted);font-size:0.9em">睡眠需求因人而異，多數成人約 7～9 小時；本工具以「躺在床上的時間」估算，實際睡著的時間通常再少一些。</span>'; }
    ups.forEach(function (u) { u(); }); }

  /* ---------- 時差 ---------- */
  var CITY = [['東京', 1], ['首爾', 1], ['雪梨', 2], ['新加坡', 0], ['曼谷', -1], ['巴黎', -7], ['倫敦', -8], ['紐約', -13], ['洛杉磯', -16]];
  function initJet(root, cfg) { head(root, cfg.q); var k = 6, v = el('div'), inf, b = row(root), P = { wake: 7 };
    CITY.forEach(function (c, i) { var x = btn('台北 → ' + c[0], i); x.onclick = function () { k = i; mark(b, k); draw(); }; b.appendChild(x); }); mark(b, k);
    var up = sl(root, '你在台灣平常的起床時間', 5, 10, 0.5, P.wake, hm, function (x) { P.wake = x; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var off = CITY[k][1], east = off > 0, dir = off, abs = Math.abs(off);
      if (off < -10) { dir = 24 + off; east = true; abs = dir; }  /* 往西超過 10 小時：身體多半改用「提早」的方式調整 */
      var rate = east ? 1 : 1.5, days = abs === 0 ? 0 : Math.ceil(abs / rate), rows = [], lag = abs;
      for (var d = 1; d <= Math.min(days + 1, 11); d++) { var bodyWake = east ? P.wake - lag : P.wake + lag;
        rows.push('<tr><td style="padding:2px 8px">第 ' + d + ' 天</td><td style="padding:2px 8px">當地 ' + hm(P.wake) + ' 起床時，身體覺得是 ' + hm(bodyWake) + '</td><td style="padding:2px 8px;color:var(--text-muted)">' + (lag < 0.5 ? '大致適應' : '還差約 ' + fx(lag, 1) + ' 小時') + '</td></tr>'); lag = Math.max(0, lag - rate); }
      var cbt = P.wake - 2, light, avoid;
      if (east) { light = '抵達後的前幾天，<b>上午</b>曬太陽（身體時間早上 ' + hm(cbt) + ' 之後的光，會把時鐘往前撥）'; avoid = '避免傍晚到睡前的強光'; }
      else { light = '抵達後的前幾天，<b>傍晚到晚上</b>多接觸光線（把時鐘往後撥）'; avoid = '避免太早曬到強烈的晨光'; }
      v.innerHTML = abs === 0 ? '<p style="margin-top:8px">新加坡與台灣沒有時差，不需要調整。</p>' : '<table style="border-collapse:collapse;margin-top:8px;font-size:0.9em;width:100%">' + rows.join('') + '</table>';
      inf.innerHTML = abs === 0 ? '同一個時區，只有飛行的疲勞，沒有生理時鐘的時差。' : '台北到' + CITY[k][0] + '，時鐘要' + (east ? '<b>提早</b>' : '<b>延後</b>') + '約 <b>' + abs + ' 小時</b>' + (CITY[k][1] < -10 ? '（往西 ' + (-CITY[k][1]) + ' 小時太多，身體常常改成往前調 ' + abs + ' 小時）' : '') + '。' +
        (east ? '往東飛（時鐘要提早）比較難，大約一天只能調 1 小時。' : '往西飛（時鐘要延後）比較容易，大約一天可以調 1～1.5 小時。') + '估計約 <b>' + days + ' 天</b>大致適應。<br>' +
        '<b>建議</b>：' + light + '；' + avoid + '。出發前 2～3 天，可以每天' + (east ? '提早' : '延後') + '約一小時睡覺與起床；抵達後立刻依當地時間吃飯、作息。短期出差（2～3 天）也可以考慮維持台灣的作息。' +
        '<br><span style="color:var(--text-muted);font-size:0.9em">簡化模型，未考慮夏令時間與個人差異；光照的最佳時機與「核心體溫最低點」（約平常起床前兩小時）有關。</span>'; }
    up(); }

  var INIT = { hypno: initHypno, twoproc: initTwo, caff: initCaff, debt: initDebt, jetlag: initJet };
  function boot() { document.querySelectorAll('.sl-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"😴", note=SL_NOTE):
    return make_with(icon, note, [("sl-w", SLLIB)])


lesson = make()
