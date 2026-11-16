# -*- coding: utf-8 -*-
"""〈曼哈頓計畫〉（mhp_）共用：課程包裝與 MHPLIB 互動元件（class="mhp-w"）。

  crit   臨界質量：材料、濃縮度、質量、反射層、壓縮 → k 值（單群擴散的教學簡化模型）
  blast  爆炸效應：當量 → 火球、5 psi、1 psi、三度灼傷半徑（立方根縮放）
  stock  核彈頭數量：美國與蘇聯／俄羅斯 1945～2024 的庫存估計與條約
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

MHP_NOTE = (u"本課程涉及戰爭與大量平民死傷的歷史。數字以常見的學術估計為主，不同來源可能有出入；"
            u"互動模擬為教學用的極度簡化模型，只求量級正確，不能用於任何實際設計。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def mhw(cfg, maxw=680):
    return wdg("mhp-w", cfg, maxw)


MHPLIB = r"""
(function () {
  if (window.__mhpLib) return; window.__mhpLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }

  /* 單群擴散簡化：k = k∞ / (1 + (πL/R_eff)²)，R_eff = R + δ（反射層節省），壓縮 c 倍時 L、δ 變為 1/c */
  var MAT = { u: { n: '鈾 235', rho: 19.05, kinf: function (e) { return 2.3 * e / (e + 0.1 * (1 - e)); }, L: function (e) { return 3.16 / Math.pow(e, 0.4); } },
              p: { n: '鈽 239（δ 相）', rho: 15.8, kinf: function () { return 2.9; }, L: function () { return 2.74; } } };
  function kOf(m, e, kg, refl, c) { var A = MAT[m], rho = A.rho * c, R = Math.pow(kg * 1000 / rho * 3 / (4 * Math.PI), 1 / 3), L = A.L(e) / c, d = refl ? 1.5 / c : 0;
    return { k: A.kinf(e) / (1 + Math.pow(Math.PI * L / (R + d), 2)), R: R, kinf: A.kinf(e) }; }
  function initCrit(root, cfg) {
    head(root, cfg.q); var P = { m: 'u', e: 0.8, kg: 64, refl: 1, c: 1 }, view = el('div'), inf, ue;
    var b = bar(root); [['鈾 235', 'u'], ['鈽 239', 'p']].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.m = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); mark(b, 'u');
    var b2 = bar(root); [['裸球（無反射層）', 0], ['有反射層（填塞）', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.refl = o[1]; mark(b2, o[1]); draw(); }; b2.appendChild(x); }); mark(b2, 1);
    var b3 = bar(root); [['小男孩（鈾、槍式）', 'lb'], ['胖子（鈽、內爆）', 'fm']].forEach(function (o) { var x = btn('預設：' + o[0], o[1]); x.onclick = function () { if (o[1] === 'lb') { P.m = 'u'; P.e = 0.8; P.kg = 64; P.c = 1; } else { P.m = 'p'; P.e = 1; P.kg = 6.2; P.c = 1; } P.refl = 1; mark(b, P.m); mark(b2, 1); us.forEach(function (u) { u(); }); }; b3.appendChild(x); });
    var us = [ue = slider(root, '鈾 235 的濃縮度', 0.05, 1, 0.01, P.e, function (x) { return Math.round(x * 100) + '%'; }, null, function (x) { P.e = x; draw(); }),
      slider(root, '材料的質量', 1, 150, 0.1, P.kg, function (x) { return f1(x) + ' kg'; }, null, function (x) { P.kg = x; draw(); }),
      slider(root, '內爆壓縮（密度變為幾倍）', 1, 3, 0.05, P.c, function (x) { return f2(x) + ' 倍'; }, null, function (x) { P.c = x; draw(); })];
    root.appendChild(view); inf = info(root);
    function draw() { var e = P.m === 'u' ? P.e : 1, cur = kOf(P.m, e, P.kg, P.refl, P.c), d = [], mc = null;
      for (var i = 0; i <= 300; i++) { var kg = 0.5 + i * 0.5, k = kOf(P.m, e, kg, P.refl, P.c).k; d.push([kg, k]); if (mc === null && k >= 1) mc = kg; }
      view.innerHTML = chart(640, 230, [{ d: d, c: BL, n: 'k 值（每次分裂平均引發幾次下一代分裂）', w: 2 }], { x0: 0, x1: 150, y0: 0, y1: 3, xl: '質量（kg）', hl: [{ y: 1, c: RD, n: 'k = 1（臨界）' }], pts: [{ x: Math.min(P.kg, 150), y: cur.k, c: OR, n: 'k = ' + f2(cur.k) }] });
      var st = cur.k < 0.98 ? '<b>次臨界</b>：中子逃出去的太多，連鎖反應會自己熄滅。' : cur.k < 1.02 ? '<b>剛好臨界</b>：反應維持穩定——這是核反應爐要的狀態，不是炸彈。' : '<b>超臨界</b>：每一代的分裂數乘以 ' + f2(cur.k) + '。一代約 10 奈秒，' + (cur.k > 1.05 ? '約 ' + Math.round(Math.log(2.5e24) / Math.log(cur.k)) + ' 代（約 ' + f1(Math.log(2.5e24) / Math.log(cur.k) * 0.01) + ' 微秒）就能分裂掉約一公斤的核燃料。k 越大，越快；材料一受熱膨脹，反應就停了，所以速度決定了效率。' : '但增長太慢，材料會先把自己炸開。');
      inf.innerHTML = MAT[P.m].n + (P.m === 'u' ? '（濃縮度 ' + Math.round(e * 100) + '%）' : '') + '：無限大時 k∞ = ' + f2(cur.kinf) + (cur.kinf <= 1 ? '——<b>連無限大都無法臨界</b>，所以低濃縮鈾不能做炸彈。' : '') + '。球半徑 ' + f1(cur.R) + ' cm。' +
        (mc ? '<br>在目前的條件下，臨界質量約 <b>' + f1(mc) + ' kg</b>。' : '') + '<br>' + st +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">（單群擴散的教學簡化模型，數字只求量級正確。）</span>'; }
    us.forEach(function (u) { u(); });
  }

  function initBlast(root, cfg) {
    head(root, cfg.q); var P = { ly: Math.log10(15) }, view = el('div'), inf;
    var pre = [['小男孩', 15], ['胖子', 21], ['W88 彈頭', 475], ['常春藤麥克', 10400], ['城堡喝采', 15000], ['沙皇炸彈', 50000]];
    var b = bar(root), u; pre.forEach(function (p) { var x = btn(p[0]); x.onclick = function () { P.ly = Math.log10(p[1]); u(); }; b.appendChild(x); });
    u = slider(root, '當量', 0, Math.log10(60000), 0.01, P.ly, function (x) { var y = Math.pow(10, x); return y < 1000 ? f1(y) + ' 千噸' : f2(y / 1000) + ' 百萬噸'; }, null, function (x) { P.ly = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var Y = Math.pow(10, P.ly), s = Y / 15, r = [[0.2 * Math.pow(s, 0.4), '火球', '#f2c14e'], [1.7 * Math.pow(s, 1 / 3), '5 psi：大部分建築倒塌', RD], [1.9 * Math.pow(s, 0.41), '三度灼傷', OR], [4.6 * Math.pow(s, 1 / 3), '1 psi：玻璃碎裂', BL]];
      var mx = Math.max.apply(null, r.map(function (q) { return q[0]; })), W = 640, H = 300, cx = 200, cy = 150, sc = 135 / mx, g = '';
      r.slice().sort(function (a, b2) { return b2[0] - a[0]; }).forEach(function (q) { g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + n1(q[0] * sc) + '" fill="' + q[2] + '" fill-opacity="0.22" stroke="' + q[2] + '" stroke-width="2"/>'; });
      var tpR = Math.sqrt(272 / Math.PI) * sc, tpOn = tpR <= 145; if (tpOn) g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + n1(tpR) + '" fill="none" stroke="currentColor" stroke-dasharray="4 4" opacity="0.6"/>';
      r.forEach(function (q, i) { g += '<rect x="370" y="' + (40 + i * 34) + '" width="14" height="14" fill="' + q[2] + '"/>' + tx(392, 52 + i * 34, q[1] + '：' + (q[0] < 1 ? Math.round(q[0] * 1000) + ' 公尺' : f1(q[0]) + ' 公里'), 13, null, 'start'); });
      g += ln(370, 186, 384, 186, 'currentColor', 1.5, 'stroke-dasharray="4 4"') + tx(392, 190, tpOn ? '虛線：與台北市面積相同的圓' : '台北市（半徑約 9.3 公里）比整張圖還大', 12, null, 'start');
      var bk = Math.pow(10, Math.floor(Math.log10(mx))); g += ln(cx - 135, 290, cx - 135 + bk * sc, 290, 'currentColor', 2) + tx(cx - 135 + bk * sc / 2, 284, bk + ' 公里', 11);
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      inf.innerHTML = '當量 <b>' + (Y < 1000 ? f1(Y) + ' 千噸' : f2(Y / 1000) + ' 百萬噸') + '</b> TNT（以廣島約 15 千噸、最佳空爆高度的估計等比例縮放）。' +
        '<br>當量變成 1000 倍，爆炸壓力的半徑只變成 10 倍（立方根），但面積變成 100 倍。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">（實際傷害取決於爆炸高度、地形、天氣與建築，這裡只是量級的示意。）</span>'; }
    u();
  }

  var US = [[1945, 2], [1946, 9], [1947, 13], [1948, 50], [1949, 170], [1950, 299], [1952, 841], [1954, 1703], [1956, 3692], [1958, 7345], [1960, 18638], [1962, 25540], [1964, 29463], [1966, 31175], [1967, 31255], [1970, 26008], [1975, 27519], [1980, 23764], [1985, 23135], [1990, 21392], [1995, 10904], [2000, 10577], [2005, 8360], [2010, 5066], [2015, 4571], [2020, 3750], [2024, 3708]];
  var RU = [[1949, 1], [1950, 5], [1955, 200], [1960, 1605], [1965, 6129], [1970, 11643], [1975, 19055], [1980, 30062], [1985, 39197], [1986, 40159], [1990, 37000], [1995, 27000], [2000, 21500], [2005, 17000], [2010, 12000], [2015, 7500], [2020, 6375], [2024, 5580]];
  var TR = [[1963, '部分禁止核試條約'], [1968, '核不擴散條約簽署'], [1972, '第一階段限武條約'], [1987, '中程飛彈條約'], [1991, '第一階段削減戰略武器條約'], [2010, '新削減戰略武器條約']];
  function interp(D, y) { if (y < D[0][0]) return 0; for (var i = 1; i < D.length; i++) if (y <= D[i][0]) { var a = D[i - 1], b = D[i]; return a[1] + (b[1] - a[1]) * (y - a[0]) / (b[0] - a[0]); } return D[D.length - 1][1]; }
  function initStock(root, cfg) {
    head(root, cfg.q); var P = { y: 1986 }, view = el('div'), inf;
    var u = slider(root, '年份', 1945, 2024, 1, P.y, function (x) { return x; }, null, function (x) { P.y = x; draw(); });
    root.appendChild(view); inf = info(root);
    function draw() { var a = Math.round(interp(US, P.y)), b2 = Math.round(interp(RU, P.y));
      view.innerHTML = chart(640, 260, [{ d: US, c: BL, n: '美國', w: 2.2 }, { d: RU, c: RD, n: '蘇聯／俄羅斯', w: 2.2 }], { x0: 1945, x1: 2024, y0: 0, y1: 42000, xl: '年份', vl: [{ x: P.y, c: GY, n: '' }].concat(TR.map(function (t) { return { x: t[0], c: GN, n: '' }; })) });
      var tr = TR.filter(function (t) { return t[0] <= P.y; }).map(function (t) { return t[0] + ' ' + t[1]; });
      inf.innerHTML = '<b>' + P.y + ' 年</b>：美國約 <b>' + a.toLocaleString() + '</b> 枚、' + (P.y < 1949 ? '蘇聯還沒有核武' : (P.y < 1992 ? '蘇聯' : '俄羅斯') + '約 <b>' + b2.toLocaleString() + '</b> 枚') + '（總庫存，含待拆除）。' +
        (tr.length ? '<br>綠色線：已簽署的條約——' + tr.slice(-3).join('、') + '。' : '') +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">資料：美國科學家聯盟與《原子科學家公報》的估計，數字為約略值。</span>'; }
    u();
  }

  function initAll() { document.querySelectorAll('.mhp-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ crit: initCrit, blast: initBlast, stock: initStock })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"☢️", MHP_NOTE, MHPLIB, "mhp-w")

CRIT = mhw({"t": "crit", "q": u"臨界質量：多少材料、多濃、怎麼擺，連鎖反應才會失控"})
BLAST = mhw({"t": "blast", "q": u"爆炸效應的範圍：當量與半徑的立方根定律"})
STOCK = mhw({"t": "stock", "q": u"核彈頭數量：美蘇軍備競賽的八十年"})
