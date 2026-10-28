# -*- coding: utf-8 -*-
"""〈國際太空站 ISS〉（iss_）共用：課程包裝與 ISSLIB 互動元件（class="isw-w"）。

  map     可點選的太空站示意圖；可加年份滑桿看組裝過程
  orbit   軌道高度 → 週期、速度、一天幾次日出；地面軌跡與傾角比較
  day     太空人一天的作息表
  loop    水與氧氣回收率 → 每年需要從地球補給多少
  decay   大氣阻力造成的軌道衰減與抬升
"""
from md_common import make_with, check, MDLIB
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

ISS_NOTE = (u"本課程依 NASA、ESA、JAXA、CSA、Roscosmos 等機構與主要媒體的公開資料整理；太空站的配置、任務與計畫經常更新，"
            u"數字多為約略值，以各機構最新公告為準。互動圖為示意，非實際比例。")


def iw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("isw-w", cfg)


F = D

# 艙段：[代號, 中文名, 英文名, 夥伴, 升空年, 移除年(0=仍在), x, y, w, h, 說明, 課]
MODS = [
    ["zvezda", u"星辰號服務艙", u"Zvezda", "RU", 2000, 0, 20, 205, 92, 36, u"俄羅斯段的核心：生活區、維生系統、推進器與俄方的指揮中心。後端有對接口，常停靠進步號貨運船。", 6],
    ["zarya", u"曙光號", u"Zarya（FGB）", "RU", 1998, 0, 114, 205, 72, 36, u"第一個升空的艙段（1998 年 11 月）。由俄羅斯製造、美國出資，早期提供電力與推進，現在主要用於儲物與燃料。", 6],
    ["unity", u"團結號（1 號節點艙）", u"Unity（Node 1）", "US", 1998, 0, 188, 203, 44, 40, u"第一個美國艙段（1998 年 12 月），六個方向都有連接口，把俄羅斯段與美國段接起來。", 7],
    ["destiny", u"命運號實驗室", u"Destiny（US Lab）", "US", 2001, 0, 234, 205, 82, 36, u"美國的主要實驗艙（2001 年），也有導航與控制設備。", 8],
    ["harmony", u"和諧號（2 號節點艙）", u"Harmony（Node 2）", "US", 2007, 0, 318, 203, 52, 40, u"連接哥倫布號與希望號，前端與上方裝有讓龍飛船等載具對接的國際對接轉接器，也有四個睡眠艙。", 7],
    ["columbus", u"哥倫布號", u"Columbus", "ESA", 2008, 0, 324, 245, 40, 64, u"歐洲太空總署的實驗艙（2008 年），艙外也有安裝實驗儀器的平台。", 9],
    ["kibo", u"希望號實驗艙", u"Kibo（JEM-PM）", "JAXA", 2008, 0, 324, 105, 40, 96, u"日本的實驗艙，是太空站上最大的單一艙段，有自己的氣閘與機械手臂，可以把立方衛星送出去。", 10],
    ["elm", u"希望號補給艙", u"JEM-ELM-PS", "JAXA", 2008, 0, 326, 80, 36, 24, u"裝在希望號上方的儲物艙（2008 年最早送上去的希望號組件）。", 10],
    ["jef", u"希望號艙外實驗平台", u"JEM-EF", "JAXA", 2009, 0, 370, 120, 60, 36, u"暴露在太空中的「陽台」，可以直接在真空、輻射環境中做實驗（2009 年）。", 10],
    ["quest", u"探索號氣閘艙", u"Quest", "US", 2001, 0, 196, 160, 30, 42, u"美國段的太空漫步出入口（2001 年），太空人在這裡穿上太空衣、減壓後出艙。", 8],
    ["tranq", u"寧靜號（3 號節點艙）", u"Tranquility（Node 3）", "US", 2010, 0, 186, 245, 48, 44, u"由歐洲為 NASA 建造（2010 年）。裝有維生系統、廁所與運動設備。", 7],
    ["cupola", u"穹頂觀測艙", u"Cupola", "ESA", 2010, 0, 194, 290, 32, 24, u"七扇窗的觀景台（2010 年），用來操作機械手臂、觀察對接，也是拍攝地球的最佳位置。", 11],
    ["bishop", u"Bishop 商業氣閘艙", u"Bishop Airlock", "US", 2020, 0, 156, 254, 28, 26, u"第一個商業氣閘艙（2020 年），用來釋放立方衛星與丟棄垃圾。", 11],
    ["pmm", u"李奧納多號多用途艙", u"Leonardo（PMM）", "ESA", 2011, 0, 236, 245, 36, 40, u"義大利製造，原本是太空梭的貨艙模組，2011 年改裝後永久留在太空站上當儲物間。", 11],
    ["beam", u"BEAM 充氣艙", u"BEAM", "US", 2016, 0, 196, 318, 26, 22, u"充氣式（可擴展）艙段的技術驗證（2016 年），原訂兩年，後來留下來當儲物空間。", 11],
    ["poisk", u"搜索號", u"Poisk（MRM-2）", "RU", 2009, 0, 40, 160, 40, 44, u"俄羅斯小型研究艙與對接口、太空漫步出入口（2009 年）。", 6],
    ["rassvet", u"黎明號", u"Rassvet（MRM-1）", "RU", 2010, 0, 114, 245, 38, 40, u"俄羅斯小型研究艙與對接口（2010 年，由太空梭送上去）。", 6],
    ["pirs", u"碼頭號（已移除）", u"Pirs", "RU", 2001, 2021, 40, 245, 40, 36, u"俄羅斯的對接艙與氣閘（2001 年）。2021 年被拆下並在大氣層燒毀，位置讓給科學號。", 6],
    ["nauka", u"科學號多功能實驗艙", u"Nauka（MLM）", "RU", 2021, 0, 34, 245, 52, 52, u"俄羅斯最新的大型艙段（2021 年），對接後推進器曾意外點火讓太空站旋轉（第 43 課）。外面裝有歐洲機械手臂。", 6],
    ["prichal", u"碼頭節點艙", u"Prichal", "RU", 2021, 0, 42, 300, 36, 32, u"俄羅斯的球形節點艙（2021 年），提供多個對接口。", 6],
    ["truss_c", u"中央桁架", u"S0／Z1 Truss", "US", 2000, 0, 236, 30, 74, 18, u"整合桁架是太空站的「脊椎」，長約 109 公尺，上面裝有太陽能板、散熱板、電力與冷卻管線。中央段在 2000～2002 年安裝。", 12],
    ["truss_s", u"右舷桁架與太陽能板", u"S1–S6 Truss", "US", 2002, 0, 312, 30, 350, 18, u"右舷桁架在 2002～2009 年分段安裝，末端兩組太陽能板翼。", 12],
    ["truss_p", u"左舷桁架與太陽能板", u"P1–P6 Truss", "US", 2000, 0, 6, 30, 228, 18, u"左舷桁架：最早的 P6 太陽能板在 2000 年就送上去（先裝在中央，2007 年才移到左端），其他段在 2002～2007 年安裝。", 12],
    ["arm", u"加拿大臂 2 號", u"Canadarm2", "CSA", 2001, 0, 270, 56, 60, 14, u"加拿大製造的 17.6 公尺機械手臂（2001 年），可以像尺蠖一樣在太空站上「走動」，抓取貨運船、搬運零件、協助太空漫步。", 13],
]

ISSLIB = r"""
(function () {
  if (window.__issLib) return; window.__issLib = 1;
""" + BASEJS + r"""
  var _sl = slider; slider = function (root, lab, min, max, step, val, fmt, k, cb) { var u = _sl(root, lab, min, max, step, val, fmt, k, cb); var b = root.lastChild && root.lastChild.querySelector('b'); if (b) b.textContent = fmt(val); return u; };
  var BL = '#3a6ea5', OR = '#e07a2f', GR = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#7a8590', TL = '#2a9d8f', GD = '#c9a227';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root, items, cur, cb) { var b = el('div'); items.forEach(function (s) { var x = btn(s[0], s[1]); x.onclick = function () { cb(s[1]); mark(b, s[1]); }; b.appendChild(x); }); mark(b, cur); root.appendChild(b); return b; }
  function fx(v, d) { if (!isFinite(v)) return '—'; d = d === undefined ? 1 : d; return (Math.round(v * Math.pow(10, d)) / Math.pow(10, d)).toFixed(d); }
  function rect(x, y, w, h, c, op, ex) { return '<rect x="' + n1(x) + '" y="' + n1(y) + '" width="' + n1(Math.max(0, w)) + '" height="' + n1(Math.max(0, h)) + '" fill="' + c + '"' + (op !== undefined ? ' fill-opacity="' + op + '"' : '') + (ex || '') + '/>'; }
  var PC = { US: '#3a6ea5', RU: '#e0505a', ESA: '#2a9d8f', JAXA: '#e07a2f', CSA: '#8e5bd1' }, PN = { US: 'NASA（美國）', RU: '俄羅斯', ESA: '歐洲太空總署', JAXA: '日本 JAXA', CSA: '加拿大 CSA' };

  /* ---------- 太空站示意圖 ---------- */
  function initMap(root, cfg) {
    head(root, cfg.q); var M = cfg.mods, year = cfg.year ? 1998 : 2025, sel = cfg.sel || 'unity', v = el('div'), inf;
    if (cfg.year) { slider(root, '年份', 1998, 2025, 1, year, function (x) { return x + ' 年'; }, 'y', function (x) { year = x; draw(); });
      var pb = btn('▶ 播放組裝過程'), tm = null; pb.onclick = function () { if (tm) { clearInterval(tm); tm = null; pb.textContent = '▶ 播放組裝過程'; return; } year = 1998; pb.textContent = '⏸ 暫停';
        tm = setInterval(function () { var e = root.querySelector('input[data-k="y"]'); e.value = year; e.dispatchEvent(new Event('input')); year++; if (year > 2025) { clearInterval(tm); tm = null; pb.textContent = '▶ 播放組裝過程'; } }, 500); }; root.appendChild(pb); }
    root.appendChild(v); inf = info(root);
    function on(m) { return m[4] <= year && (!m[5] || m[5] > year); }
    function draw() { var g = '';
      g += tx(670, 16, cfg.year ? year + ' 年' : '', 18, 'currentColor', 'end');
      M.forEach(function (m) { var a = on(m), isT = m[0].indexOf('truss') === 0, c = PC[m[3]];
        if (m[0] === 'arm') { g += '<g data-k="' + m[0] + '" style="cursor:pointer;opacity:' + (a ? 1 : 0.12) + '">' + ln(m[6], m[7] + 10, m[6] + 26, m[7], c, 4) + ln(m[6] + 26, m[7], m[6] + m[8], m[7] + 12, c, 4) + '<circle cx="' + (m[6] + 26) + '" cy="' + m[7] + '" r="4" fill="' + c + '"/></g>'; return; }
        g += '<g data-k="' + m[0] + '" style="cursor:pointer;opacity:' + (a ? 1 : 0.12) + '">' + rect(m[6], m[7], m[8], m[9], c, isT ? 0.55 : 0.8, ' rx="' + (isT ? 2 : 6) + '" stroke="' + (sel === m[0] ? '#111' : 'none') + '" stroke-width="2"');
        if (isT && m[0] !== 'truss_c') { var n = m[0] === 'truss_s' ? [[m[6] + 230, 2009], [m[6] + 300, 2007]] : [[m[6] + 10, 2007], [m[6] + 80, 2006]]; n.forEach(function (s) { if (s[1] <= year) { g += rect(s[0], m[7] - 22, 36, 18, '#1d3557', 0.85, ' rx="2"') + rect(s[0], m[7] + 22, 36, 18, '#1d3557', 0.85, ' rx="2"'); } }); }
        if (!isT && m[8] >= 36) g += tx(m[6] + m[8] / 2, m[7] + m[9] / 2 + 4, m[1].replace(/（.*）/, '').slice(0, m[8] > 70 ? 6 : 3), 10, '#fff');
        g += '</g>'; });
      if (year >= 2000) g += ln(272, 48, 272, 203, GY, 3);
      var lx = 10; Object.keys(PC).forEach(function (k) { g += rect(lx, 352, 12, 12, PC[k], 0.85) + tx(lx + 16, 362, PN[k], 10.5, 'currentColor', 'start'); lx += 130; });
      g += tx(670, 378, '示意圖：只表示連接關係，非實際比例與方向', 9.5, 'var(--text-muted)', 'end');
      v.innerHTML = svgw('0 0 680 382', g);
      v.querySelectorAll('g[data-k]').forEach(function (e) { e.addEventListener('click', function () { sel = e.getAttribute('data-k'); draw(); }); });
      var m = M.filter(function (x) { return x[0] === sel; })[0], cnt = M.filter(function (x) { return on(x) && x[0].indexOf('truss') !== 0 && x[0] !== 'arm'; }).length;
      inf.innerHTML = '<b>' + m[1] + '</b>（' + m[2] + '）・' + PN[m[3]] + '・' + m[4] + ' 年' + (m[5] ? '～' + m[5] + ' 年' : '') + '<br>' + m[10] + ' <a hr' + 'ef="lesson-' + (m[11] < 10 ? '0' : '') + m[11] + '.html">第 ' + m[11] + ' 課</a>' +
        '<br><span style="color:var(--text-muted)">' + (cfg.year ? year + ' 年時，太空站上有 ' + cnt + ' 個加壓艙段（圖中的主要艙段）。' : '') + '點選任何艙段看說明。' + (year >= 2000 && year < 2001 ? '2000 年 11 月 2 日，第一批長期駐留的太空人抵達，從此太空站上一直有人。' : '') + '</span>'; }
    draw();
  }

  /* ---------- 軌道 ---------- */
  function initOrbit(root, cfg) {
    head(root, cfg.q); var h = 410, inc = 51.6, v = el('div'), inf, MU = 398600.4418, RE = 6371;
    slider(root, '軌道高度（公里）', 200, 2000, 5, h, function (x) { return x + ' km'; }, 'h', function (x) { h = x; draw(); });
    bar(root, [['ISS 51.6°', 51.6], ['天宮 41.5°', 41.5], ['甘迺迪角直接東射 28.5°', 28.5], ['極軌道 98°', 98]], inc, function (x) { inc = x; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var a = RE + h, T = 2 * Math.PI * Math.sqrt(a * a * a / MU), vel = Math.sqrt(MU / a), n = 86400 / T, W = 680, H = 340, g = '';
      function X(lon) { return 10 + (lon + 180) / 360 * (W - 20); } function Y(lat) { return 10 + (90 - lat) / 180 * 300; }
      g += rect(10, 10, W - 20, 300, '#dbe9f5', 0.6);
      [-60, -30, 0, 30, 60].forEach(function (l) { g += ln(10, Y(l), W - 10, Y(l), '#9ab', 0.5, 'stroke-dasharray="2 3"') + tx(14, Y(l) - 2, (l > 0 ? '北' : l < 0 ? '南' : '') + Math.abs(l) + '°', 9, '#678', 'start'); });
      for (var lo = -120; lo <= 120; lo += 60) g += ln(X(lo), 10, X(lo), 310, '#9ab', 0.5, 'stroke-dasharray="2 3"');
      var ii = inc > 90 ? 180 - inc : inc; g += rect(10, Y(ii), W - 20, Y(-ii) - Y(ii), GD, 0.12);
      var omE = 360 / 86164, cols = [RD, OR, PU];
      for (var k = 0; k < 3; k++) { var d = '', last = null, t;
        for (t = 0; t <= T; t += T / 300) { var u = 2 * Math.PI * t / T, ir = inc * Math.PI / 180, lat = Math.asin(Math.sin(ir) * Math.sin(u)) * 180 / Math.PI, lon = Math.atan2(Math.cos(ir) * Math.sin(u), Math.cos(u)) * 180 / Math.PI - omE * (t + k * T) - 30;
          lon = ((lon + 540) % 360) - 180; var px = X(lon), py = Y(lat); d += (last !== null && Math.abs(px - last) > 300 ? 'M' : (d ? 'L' : 'M')) + n1(px) + ' ' + n1(py); last = px; }
        g += '<path d="' + d + '" fill="none" stroke="' + cols[k] + '" stroke-width="1.8"/>' + tx(W - 14, 26 + k * 13, '第 ' + (k + 1) + ' 圈', 10, cols[k], 'end'); }
      g += '<circle cx="' + n1(X(121)) + '" cy="' + n1(Y(23.7)) + '" r="4" fill="#111"/>' + tx(X(121) + 6, Y(23.7) + 4, '台灣', 10, '#111', 'start');
      g += tx(W / 2, 328, '地面軌跡（簡化：圓軌道、不含地圖輪廓）；黃色帶是太空站經過的緯度範圍', 10, 'var(--text-muted)');
      v.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var shift = T / 86164 * 360;
      inf.innerHTML = '高度 ' + h + ' 公里：繞一圈 <b>' + fx(T / 60, 1) + ' 分鐘</b>、速度 <b>' + fx(vel, 2) + ' km/s</b>（約 ' + Math.round(vel * 3600).toLocaleString() + ' km/h），一天繞 <b>' + fx(n, 1) + ' 圈</b>，也就是看到大約 ' + Math.round(n) + ' 次日出與日落。<br>' +
        '因為地球在自轉，每一圈的地面軌跡會往西偏約 ' + fx(shift, 1) + '°。傾角 ' + inc + '° 代表太空站最北只到北緯 ' + fx(inc > 90 ? 180 - inc : inc, 1) + '°' + (inc >= 23.7 ? '，台灣在範圍內，所以常常能看到它飛過。' : '，到不了台灣上空。') +
        '<br><span style="color:var(--text-muted)">ISS 選 51.6° 是為了讓俄羅斯拜科努爾發射場（北緯約 46°）也能直接發射，代價是從美國發射時能載的重量變少（第 1、3 課）。</span>'; }
    draw();
  }

  /* ---------- 一天作息 ---------- */
  function initDay(root, cfg) {
    head(root, cfg.q); var S = cfg.items, v = el('div'), inf, sel = 0;
    var CC = { sleep: '#5b6ea8', meal: '#e0a030', work: '#3a9d6a', ex: '#d0504a', pers: '#9a7ac0', conf: '#4aa3b5' };
    root.appendChild(v); inf = info(root);
    function draw() { var W = 680, g = '', L = 20, sc = (W - 40) / 24;
      S.forEach(function (s, i) { var x = L + s[0] * sc, w = (s[1] - s[0]) * sc; g += '<g data-i="' + i + '" style="cursor:pointer">' + rect(x, 30, w, 50, CC[s[2]], sel === i ? 1 : 0.75, ' stroke="#fff" stroke-width="1"') + (w > 34 ? tx(x + w / 2, 60, s[3].slice(0, Math.max(1, Math.floor(w / 12))), 10, '#fff') : '') + '</g>'; });
      for (var t = 0; t <= 24; t += 2) g += ln(L + t * sc, 82, L + t * sc, 88, GY) + tx(L + t * sc, 100, (t < 10 ? '0' : '') + t + ':00', 9, 'var(--text-muted)');
      var lx = L; [['sleep', '睡眠'], ['meal', '用餐'], ['work', '工作與實驗'], ['ex', '運動'], ['pers', '個人時間'], ['conf', '會議與準備']].forEach(function (c) { g += rect(lx, 112, 12, 12, CC[c[0]]) + tx(lx + 16, 122, c[1], 10, 'currentColor', 'start'); lx += 105; });
      g += tx(L, 20, '格林威治時間（GMT／UTC）', 10, 'var(--text-muted)', 'start');
      v.innerHTML = svgw('0 0 ' + W + ' 132', g);
      v.querySelectorAll('g[data-i]').forEach(function (e) { e.addEventListener('click', function () { sel = +e.getAttribute('data-i'); draw(); }); });
      var s = S[sel], h0 = Math.floor(s[0]), m0 = Math.round((s[0] - h0) * 60), h1 = Math.floor(s[1]), m1 = Math.round((s[1] - h1) * 60);
      function hm(h, m) { return (h < 10 ? '0' : '') + h + ':' + (m < 10 ? '0' : '') + m; }
      inf.innerHTML = '<b>' + hm(h0, m0) + '～' + hm(h1, m1) + '　' + s[3] + '</b><br>' + s[4] + '<br><span style="color:var(--text-muted)">點選時間軸上的任一段。這是典型平日的示意，實際排程每天由地面規劃，遇到太空漫步、貨運船對接時會大幅調整。</span>'; }
    draw();
  }

  /* ---------- 水與氧氣回收 ---------- */
  function initLoop(root, cfg) {
    head(root, cfg.q); var crew = 7, wr = 98, orr = 50, v = el('div'), inf;
    slider(root, '駐站人數', 2, 10, 1, crew, function (x) { return x + ' 人'; }, 'c', function (x) { crew = x; draw(); });
    slider(root, '水回收率', 0, 99, 1, wr, function (x) { return x + '%'; }, 'w', function (x) { wr = x; draw(); });
    slider(root, '二氧化碳中的氧回收比例（薩巴捷反應等）', 0, 90, 5, orr, function (x) { return x + '%'; }, 'o', function (x) { orr = x; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var wd = 3.6, od = 0.84, W = 680, g = '', yr = 365;
      var wNeed = crew * wd * yr, wMake = wNeed * (1 - wr / 100), oNeed = crew * od * yr, oWater = oNeed * 1.125 * (1 - orr / 100), total = wMake + oWater;
      function box(x, y, w, h, c, t1, t2) { return rect(x, y, w, h, c, 0.15, ' rx="10" stroke="' + c + '" stroke-width="1.5"') + tx(x + w / 2, y + 22, t1, 12, 'currentColor') + tx(x + w / 2, y + 42, t2, 11, c); }
      function arr(x1, y1, x2, y2, c, t) { return ln(x1, y1, x2, y2, c, 2, 'marker-end="url(#ah)"') + (t ? tx((x1 + x2) / 2, (y1 + y2) / 2 - 6, t, 10, c) : ''); }
      g += '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#888"/></marker></defs>';
      g += box(250, 10, 180, 54, BL, '太空人（' + crew + ' 人）', '每年用水約 ' + Math.round(wNeed / 1000 * 10) / 10 + ' 噸');
      g += box(20, 120, 190, 54, TL, '水回收系統', '尿液、汗水、冷凝水');
      g += box(470, 120, 190, 54, PU, '電解產氧', '水 → 氧氣＋氫氣');
      g += box(250, 210, 180, 54, OR, '從地球補給', '每年約 ' + fx(total / 1000, 2) + ' 噸水');
      g += arr(250, 50, 140, 118, BL, '廢水') + arr(150, 176, 250, 216, TL, '') + arr(210, 140, 250, 60, TL, '回收 ' + wr + '%');
      g += arr(430, 50, 520, 118, PU, '') + arr(520, 118, 430, 50, PU, '') + tx(510, 82, '氧氣', 10, PU, 'start') + arr(430, 236, 520, 176, OR, '補水') + arr(340, 208, 340, 68, OR, '');
      v.innerHTML = svgw('0 0 ' + W + ' 272', g);
      inf.innerHTML = '假設每人每天用水約 3.6 公斤（飲用、食物復水、衛生）、需要氧氣約 0.84 公斤（示意值）。<br>' +
        crew + ' 人一年用水約 <b>' + fx(wNeed / 1000, 1) + ' 噸</b>；回收率 ' + wr + '% 時，只需要補充約 <b>' + fx(wMake / 1000, 2) + ' 噸</b>。製造氧氣還要再用掉約 ' + fx(oWater / 1000, 2) + ' 噸水。<br>' +
        '合計每年要從地球送上來約 <b>' + fx(total / 1000, 2) + ' 噸</b>。把水回收率調到 0%，就知道為什麼回收系統是長期駐留的關鍵——一艘貨運船一次也只能送幾噸貨物（第 17、31 課）。'; }
    draw();
  }

  /* ---------- 軌道衰減 ---------- */
  function initDecay(root, cfg) {
    head(root, cfg.q); var sol = 'mid', boost = 1, every = 60, dv = 3, v = el('div'), inf;
    bar(root, [['太陽活動低', 'low'], ['中等', 'mid'], ['太陽活動高', 'high']], sol, function (x) { sol = x; draw(); });
    bar(root, [['有定期抬升', 1], ['停止抬升', 0]], boost, function (x) { boost = x; draw(); });
    slider(root, '每隔幾天抬升一次', 20, 180, 5, every, function (x) { return x + ' 天'; }, 'e', function (x) { every = x; draw(); });
    slider(root, '每次抬升的高度（公里）', 0.5, 8, 0.5, dv, function (x) { return x + ' km'; }, 'd', function (x) { dv = x; draw(); });
    root.appendChild(v); inf = info(root);
    function draw() { var k = { low: 0.03, mid: 0.07, high: 0.16 }[sol], h = 415, d = [[0, h]], i, low = null, fuel = 0;
      for (i = 1; i <= 730; i++) { h -= k * Math.exp(-(h - 400) / 50); if (boost && i % every === 0) { h += dv; fuel += dv; } if (h < 200) { d.push([i, 200]); if (low === null) low = i; break; } if (low === null && h < 300) low = i; d.push([i, h]); }
      v.innerHTML = chart(680, 260, [{ d: d, c: BL, n: '軌道高度（公里）' }], { x0: 0, x1: 730, y0: 200, y1: 440, xl: '天', hl: [{ y: 300, c: RD, n: '約 300 公里以下，衰減會越來越快' }] });
      inf.innerHTML = '在 400 公里高度，空氣雖然極稀薄，仍會讓太空站每天下降幾十到上百公尺；太陽活動強時，高層大氣受熱膨脹，阻力變大。<br>' +
        (boost ? '兩年內共抬升約 <b>' + fx(fuel, 1) + ' 公里</b>。' : '') + (low !== null ? '在這個設定下，約第 <b>' + low + '</b> 天就會掉到 300 公里以下。' : '兩年內都維持在 300 公里以上。') +
        '<br><span style="color:var(--text-muted)">簡化的指數大氣模型，只用來說明趨勢。實際上 ISS 靠進步號、星辰號、天鵝座號等的推進器抬升軌道（第 18 課），退役時則反過來，刻意讓它降低並墜入海洋（第 49 課）。</span>'; }
    draw();
  }

  var INIT = { map: initMap, orbit: initOrbit, day: initDay, loop: initLoop, decay: initDecay };
  function boot() { document.querySelectorAll('.isw-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🛰️", note=ISS_NOTE):
    return make_with(icon, note, [("isw-w", ISSLIB)])


lesson = make()


def MAP(q=u"點選艙段看說明：", sel="unity", year=False):
    return iw("map", q, mods=MODS, sel=sel, year=year)


DAY = iw("day", u"一位太空人的典型平日（點選各時段）：", items=[
    [0, 6, "sleep", u"睡眠", u"每天排定約 8.5 小時的睡眠時間（含前後的準備）。睡在牆上的睡袋裡，睡眠艙大小約一個電話亭。"],
    [6, 6.5, "pers", u"起床盥洗", u"起床、上廁所、刷牙洗臉、換衣服。"],
    [6.5, 7, "meal", u"早餐", u"從食物櫃挑選、加熱或加水。"],
    [7, 7.5, "conf", u"每日計畫會議", u"和地面的任務控制中心（休士頓、莫斯科、慕尼黑、筑波等）視訊，確認今天的工作。"],
    [7.5, 12, "work", u"上午工作", u"科學實驗、維修保養、清點物資。每項工作都有詳細的程序書，排程精確到分鐘。"],
    [12, 13, "meal", u"午餐", u"常是一天中大家聚在一起吃飯的時候。"],
    [13, 15, "work", u"下午工作", u"繼續實驗或維修；也可能是公共關係活動，例如和學校學生通話。"],
    [15, 17.5, "ex", u"運動", u"每天約 2.5 小時（包括準備與清潔），用跑步機、阻力訓練機、腳踏車，對抗骨質與肌肉流失。"],
    [17.5, 18.5, "work", u"收尾與準備", u"完成當天任務、準備隔天的工作。"],
    [18.5, 19, "conf", u"晚間會議", u"和地面回報當天狀況。"],
    [19, 20, "meal", u"晚餐", u"晚餐通常比較悠閒。"],
    [20, 21.5, "pers", u"個人時間", u"看窗外、拍照、看電影、寫電子郵件、和家人視訊（每週有排定的私人家庭通話）。"],
    [21.5, 24, "sleep", u"睡眠", u"就寢。週末通常安排較少工作，以清潔與個人時間為主。"]])
