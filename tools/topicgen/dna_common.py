# -*- coding: utf-8 -*-
"""〈基因與 DNA〉（dna_）共用：課程包裝與 GNLIB 互動元件（class="gn-w"）。

  punnett    遺傳格子：單基因、雙基因、X 性聯遺傳
  translate  中心法則轉譯器：DNA → mRNA → 胺基酸，含點突變、無義突變、移碼突變
  poly       多基因模擬：基因數、環境變異 → 性狀分布與遺傳率
"""
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS

DNA_NOTE = (u"本課程為科普教學，不構成醫療或遺傳諮詢建議；基因檢測與疾病風險請諮詢醫師或遺傳諮詢師。"
            u"數字（基因數、帶因率、突變率等）為大約值，會隨研究更新。")
F = D


def gnw(t, q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("gn-w", cfg)


GNLIB = r"""
(function () {
  if (window.__gnLib) return; window.__gnLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#e07a2f', GN = '#2e9e5b', RD = '#e0505a', PU = '#8e5bd1', GY = '#9aa3ad';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root, lab, opts, get, set) { var b = el('div', 'margin:6px 0'); if (lab) b.appendChild(el('span', 'font-size:0.85em;color:var(--text-muted);margin-right:4px', lab)); opts.forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { set(o[1]); mark(b, o[1]); }; b.appendChild(x); }); root.appendChild(b); mark(b, get()); return b; }
  function note(s) { return '<br><span style="color:var(--text-muted);font-size:0.9em">' + s + '</span>'; }

  /* ---------- 遺傳格子 ---------- */
  function gam(g) { /* g: array of genes, each 2-char string like 'Aa'; returns list of gametes */
    var out = ['']; g.forEach(function (p) { var n = []; out.forEach(function (o) { n.push(o + p[0]); n.push(o + p[1]); }); out = n; }); return out; }
  function norm(a, b) { /* combine two gametes into genotype per gene, uppercase first */
    var s = ''; for (var i = 0; i < a.length; i++) { var x = a[i], y = b[i]; s += (x <= y ? x + y : y + x); } return s; }
  function initPunnett(root, cfg) { head(root, cfg.q); var P = { m: 'one', p1: 'Aa', p2: 'Aa', d1: 'AaBb', d2: 'AaBb', x1: 'Hh', x2: 'H' }, ctl = el('div'), v = el('div'), inf;
    bar(root, '模式：', [['單基因（顯性／隱性）', 'one'], ['雙基因（自由組合）', 'two'], ['X 性聯（例：蠶豆症）', 'x']], function () { return P.m; }, function (k) { P.m = k; build(); });
    root.appendChild(ctl); root.appendChild(v); inf = info(root);
    function build() { ctl.innerHTML = '';
      if (P.m === 'one') { bar(ctl, '父：', [['AA', 'AA'], ['Aa', 'Aa'], ['aa', 'aa']], function () { return P.p1; }, function (k) { P.p1 = k; draw(); }); bar(ctl, '母：', [['AA', 'AA'], ['Aa', 'Aa'], ['aa', 'aa']], function () { return P.p2; }, function (k) { P.p2 = k; draw(); }); }
      if (P.m === 'two') { var o = [['AABB', 'AABB'], ['AaBb', 'AaBb'], ['Aabb', 'Aabb'], ['aaBb', 'aaBb'], ['aabb', 'aabb']]; bar(ctl, '父：', o, function () { return P.d1; }, function (k) { P.d1 = k; draw(); }); bar(ctl, '母：', o, function () { return P.d2; }, function (k) { P.d2 = k; draw(); }); }
      if (P.m === 'x') { bar(ctl, '母親：', [['正常 XᴴXᴴ', 'HH'], ['帶因 XᴴXʰ', 'Hh'], ['患者 XʰXʰ', 'hh']], function () { return P.x1; }, function (k) { P.x1 = k; draw(); }); bar(ctl, '父親：', [['正常 XᴴY', 'H'], ['患者 XʰY', 'h']], function () { return P.x2; }, function (k) { P.x2 = k; draw(); }); }
      draw(); }
    function cell(t, c) { return '<td style="border:1px solid var(--border);padding:6px 8px;text-align:center;background:' + c + '22;font-family:monospace;font-size:1.05em">' + t + '</td>'; }
    function th(t) { return '<th style="border:1px solid var(--border);padding:6px 8px;background:var(--surface);font-family:monospace">' + t + '</th>'; }
    function draw() { var h = '', cnt = {}, tot = 0, rows, cols, f;
      if (P.m === 'x') { rows = ['X' + (P.x1[0] === 'H' ? 'ᴴ' : 'ʰ'), 'X' + (P.x1[1] === 'H' ? 'ᴴ' : 'ʰ')]; cols = ['X' + (P.x2 === 'H' ? 'ᴴ' : 'ʰ'), 'Y'];
        h = '<table style="border-collapse:collapse;margin:8px auto"><tr>' + th('母＼父') + cols.map(th).join('') + '</tr>';
        rows.forEach(function (r, i) { h += '<tr>' + th(r); cols.forEach(function (c, j) { var mom = P.x1[i], dad = j === 0 ? P.x2 : null, lab, col;
          if (dad === null) { lab = mom === 'H' ? '兒子・正常' : '兒子・<b>患者</b>'; col = mom === 'H' ? GN : RD; }
          else { var hh = (mom === 'h') + (dad === 'h'); lab = hh === 0 ? '女兒・正常' : hh === 1 ? '女兒・帶因' : '女兒・<b>患者</b>'; col = hh === 0 ? GN : hh === 1 ? OR : RD; }
          var k = lab.replace(/<[^>]+>/g, ''); cnt[k] = (cnt[k] || 0) + 1; tot++; h += cell(r + c + '<br><span style="font-family:inherit;font-size:0.82em">' + lab + '</span>', col); }); h += '</tr>'; }); h += '</table>';
        v.innerHTML = h;
        inf.innerHTML = '每一格機率 25%：' + Object.keys(cnt).map(function (k) { return k + ' ' + (cnt[k] / tot * 100) + '%'; }).join('、') + '。' +
          '<br>男性只有一條 X 染色體，只要帶到一個致病基因就會表現；女性要兩條都帶到才會發病，只帶一條則是<b>帶因者</b>。所以 X 性聯隱性疾病（如蠶豆症、紅綠色盲、血友病）<b>男性遠多於女性</b>。' +
          note('台灣的新生兒篩檢包含 G6PD 缺乏症（蠶豆症）。實際上女性帶因者也可能因 X 染色體去活化而有輕微症狀（第 21 課）。');
        return; }
      var g1 = P.m === 'one' ? [P.p1] : [P.d1.slice(0, 2), P.d1.slice(2)], g2 = P.m === 'one' ? [P.p2] : [P.d2.slice(0, 2), P.d2.slice(2)];
      rows = gam(g2); cols = gam(g1);
      function ph(gt) { var s = ''; for (var i = 0; i < gt.length; i += 2) { var up = gt[i] === gt[i].toUpperCase() || gt[i + 1] === gt[i + 1].toUpperCase(); s += up ? gt[i].toUpperCase() + '_' : gt[i].toLowerCase() + gt[i].toLowerCase(); } return s; }
      var pcol = { 'A_': BL, 'aa': OR, 'A_B_': BL, 'A_bb': GN, 'aaB_': PU, 'aabb': OR };
      h = '<table style="border-collapse:collapse;margin:8px auto"><tr>' + th('母＼父') + cols.map(th).join('') + '</tr>';
      rows.forEach(function (r) { h += '<tr>' + th(r); cols.forEach(function (c) { var gt = norm(c, r), p = ph(gt); cnt[p] = (cnt[p] || 0) + 1; tot++; h += cell(gt, pcol[p] || GY); }); h += '</tr>'; }); h += '</table>';
      v.innerHTML = h;
      var lab = { 'A_': '顯性性狀', 'aa': '隱性性狀', 'A_B_': '兩個顯性', 'A_bb': 'A 顯性、b 隱性', 'aaB_': 'a 隱性、B 顯性', 'aabb': '兩個隱性' };
      var ks = Object.keys(cnt).sort();
      inf.innerHTML = '子代表現型比例：' + ks.map(function (k) { return '<b style="color:' + pcol[k] + '">' + lab[k] + '</b> ' + cnt[k] + '/' + tot + '（' + Math.round(cnt[k] / tot * 1000) / 10 + '%）'; }).join('、') + '。' +
        (P.m === 'one' && P.p1 === 'Aa' && P.p2 === 'Aa' ? '<br>兩個<b>帶因者</b>（Aa）生下的孩子，有 1/4 機率是隱性的 aa——這就是父母都正常，孩子卻可能罹患隱性遺傳疾病（如地中海型貧血重型）的原因（第 24 課）。' : '') +
        (P.m === 'two' && P.d1 === 'AaBb' && P.d2 === 'AaBb' ? '<br>這就是孟德爾著名的 <b>9：3：3：1</b>：兩對基因位在不同的染色體上時，會各自獨立分配。' : '') +
        note('格子中的每一格代表一種精卵組合，機率相等；真實的家庭只有少數幾個孩子，比例會偏離理論值。');
    }
    build(); }

  /* ---------- 轉譯器 ---------- */
  var AA = { F: '苯丙胺酸 Phe', L: '白胺酸 Leu', I: '異白胺酸 Ile', M: '甲硫胺酸 Met', V: '纈胺酸 Val', S: '絲胺酸 Ser', P: '脯胺酸 Pro', T: '蘇胺酸 Thr', A: '丙胺酸 Ala', Y: '酪胺酸 Tyr', H: '組胺酸 His', Q: '麩醯胺酸 Gln', N: '天冬醯胺 Asn', K: '離胺酸 Lys', D: '天冬胺酸 Asp', E: '麩胺酸 Glu', C: '半胱胺酸 Cys', W: '色胺酸 Trp', R: '精胺酸 Arg', G: '甘胺酸 Gly', '*': '終止' };
  var B = 'UCAG', CODE = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG';
  function tr(c) { return CODE[B.indexOf(c[0]) * 16 + B.indexOf(c[1]) * 4 + B.indexOf(c[2])]; }
  function initTranslate(root, cfg) { head(root, cfg.q); var ORIG = 'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCC', P = { s: ORIG }, inp = el('input'), v = el('div'), inf;
    inp.type = 'text'; inp.value = P.s; inp.style.cssText = 'width:100%;font-family:monospace;padding:6px;border:1px solid var(--border);border-radius:6px;background:var(--surface);color:var(--text);box-sizing:border-box';
    root.appendChild(el('div', 'font-size:0.85em;color:var(--text-muted);margin:4px 0', 'DNA 編碼股（5′→3′，只接受 A、T、C、G）：')); root.appendChild(inp);
    var b = el('div', 'margin:6px 0'); [['原始序列（β-球蛋白開頭）', ORIG], ['鐮刀型貧血（GAG→GTG）', ORIG.slice(0, 19) + 'T' + ORIG.slice(20)], ['無義突變（AAG→TAG）', ORIG.slice(0, 24) + 'T' + ORIG.slice(25)], ['移碼突變（插入一個 A）', ORIG.slice(0, 12) + 'A' + ORIG.slice(12)], ['同義突變（CTG→CTA）', ORIG.slice(0, 11) + 'A' + ORIG.slice(12)]].forEach(function (o) { var x = btn(o[0]); x.onclick = function () { inp.value = o[1]; draw(); }; b.appendChild(x); }); root.appendChild(b);
    root.appendChild(v); inf = info(root); inp.addEventListener('input', draw);
    function prot(s) { var m = s.replace(/T/g, 'U'), out = []; for (var i = 0; i + 3 <= m.length; i += 3) { var c = m.slice(i, i + 3), a = tr(c); out.push([c, a]); if (a === '*') break; } return out; }
    function draw() { var s = inp.value.toUpperCase().replace(/[^ACGT]/g, ''), p = prot(s), o = prot(ORIG), h = '<div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:6px">', diff = 0;
      p.forEach(function (x, i) { var same = o[i] && o[i][1] === x[1], col = x[1] === '*' ? RD : same ? BL : OR; if (!same) diff++;
        h += '<div style="border:1.5px solid ' + col + ';border-radius:6px;padding:3px 6px;text-align:center;min-width:54px"><div style="font-family:monospace;font-size:0.95em">' + x[0] + '</div><div style="font-size:0.78em;color:' + col + '">' + (AA[x[1]] || '?').split(' ')[0] + '</div><div style="font-family:monospace;font-size:0.8em;color:' + col + '">' + x[1] + '</div></div>'; });
      h += '</div>'; v.innerHTML = '<div style="font-family:monospace;font-size:0.85em;word-break:break-all;margin-top:6px;color:var(--text-muted)">mRNA：' + s.replace(/T/g, 'U') + '</div>' + h;
      var stop = p.length && p[p.length - 1][1] === '*';
      inf.innerHTML = '共 ' + p.length + ' 個密碼子' + (stop ? '，在第 ' + p.length + ' 個遇到<b style="color:' + RD + '">終止密碼子</b>，蛋白質提早結束' : '') + '；與原始序列相比，有 <b>' + diff + '</b> 個胺基酸不同（橘色）。' +
        '<br>試試上面的按鈕：<b>鐮刀型貧血</b>只改了一個字母，讓一個麩胺酸（Glu）變成纈胺酸（Val）——就足以讓血紅素黏在一起、紅血球變形。<b>同義突變</b>改了字母卻沒改胺基酸（密碼的「簡併性」）。<b>移碼突變</b>讓之後的讀法全部錯位。' +
        note('簡化：真實的基因有內含子需要剪接（第 10 課），轉譯也從 mRNA 上的起始密碼子開始。這段序列取自人類 β-球蛋白基因的開頭（含起始的甲硫胺酸）。');
    }
    draw(); }

  /* ---------- 多基因 ---------- */
  function rng(seed) { return function () { seed |= 0; seed = seed + 0x6D2B79F5 | 0; var t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
  function initPoly(root, cfg) { head(root, cfg.q); var P = { n: 1, e: 0 }, v = el('div'), inf;
    var us = [slider(root, '影響性狀的基因數', 1, 30, 1, P.n, function (x) { return x + ' 個'; }, null, function (x) { P.n = x; draw(); }),
      slider(root, '環境的影響（營養、疾病、隨機）', 0, 3, 0.25, P.e, function (x) { return x === 0 ? '沒有' : '標準差 ' + x; }, null, function (x) { P.e = x; draw(); })];
    root.appendChild(v); inf = info(root);
    function draw() { var R = rng(7), N = 3000, xs = [], nb = 40;
      for (var i = 0; i < N; i++) { var g = 0; for (var k = 0; k < P.n * 2; k++) if (R() < 0.5) g++; var z = 0; if (P.e) { var u = 1 - R(), w = R(); z = Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * w) * P.e * Math.sqrt(P.n / 2); } xs.push((g - P.n) / Math.sqrt(P.n / 2) + z); }
      var lo = Math.min.apply(null, xs), hi = Math.max.apply(null, xs), w = (hi - lo) / nb || 1, hst = []; for (var b = 0; b < nb; b++) hst.push(0); xs.forEach(function (x) { hst[Math.min(nb - 1, Math.floor((x - lo) / w))]++; });
      var mx = Math.max.apply(null, hst), W = 680, H = 200, g = '';
      hst.forEach(function (c, b) { var bh = c / mx * (H - 30); g += '<rect x="' + n1(20 + b * (W - 40) / nb) + '" y="' + n1(H - 20 - bh) + '" width="' + n1((W - 40) / nb - 1.5) + '" height="' + n1(bh) + '" fill="' + BL + '"/>'; });
      g += ln(20, H - 20, W - 20, H - 20, '#999') + tx(20, H - 4, '矮', 11, 'var(--text-muted)', 'start') + tx(W - 20, H - 4, '高', 11, 'var(--text-muted)', 'end') + tx(W / 2, H - 4, '性狀（例如身高）', 11, 'var(--text-muted)');
      v.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var vg = 1, ve = P.e * P.e, h2 = vg / (vg + ve);
      inf.innerHTML = (P.n <= 2 && !P.e ? '只有 ' + P.n + ' 個基因時，性狀分成幾個<b>明顯的類別</b>——這就是孟德爾看到的「高莖、矮莖」。' : '基因越多、再加上環境，分布就越接近平滑的<b>鐘形曲線</b>——這就是身高、膚色這類「連續性狀」的樣子。') +
        '<br>在這個模擬中，<b>遺傳率</b>約為 ' + Math.round(h2 * 100) + '%：族群中的差異，有這麼多比例來自基因的差異。' +
        note('教學模型：每個基因有兩個等位基因、效果相同且可加成，環境獨立。真實的身高與數千個基因變異有關，各自的效果極小（第 17、18 課）。');
    }
    us.forEach(function (u) { u(); }); }

  var INIT = { punnett: initPunnett, translate: initTranslate, poly: initPoly };
  function boot() { document.querySelectorAll('.gn-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); var fn = INIT[cfg.t]; if (fn) fn(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def make(icon=u"🧬", note=DNA_NOTE):
    return make_with(icon, note, [("gn-w", GNLIB)])


lesson = make()

PUNNETT = gnw("punnett", u"遺傳格子：選擇父母的基因型，看看孩子的機率")
TRANSLATE = gnw("translate", u"中心法則轉譯器：DNA → mRNA → 胺基酸")
POLY = gnw("poly", u"多基因模擬：從「高莖與矮莖」到「身高的鐘形曲線」")
