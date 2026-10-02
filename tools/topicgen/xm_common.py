# -*- coding: utf-8 -*-
"""〈姓名學〉共用工具與互動元件（XMLIB）。康熙筆畫由 Unihan 的 kRSKangXi（部首.餘畫）加上部首原形筆畫算出。"""
import os
from cc_common import *
from qt_common import BASEJS

_D = os.path.dirname(os.path.abspath(__file__))
STROKES = open(os.path.join(_D, "xm_strokes.txt"), encoding="utf-8").read()
TONES = open(os.path.join(_D, "xm_tones.txt"), encoding="utf-8").read()

XM_NOTE = (u"本課程介紹姓名學的傳統規則與文化脈絡。姓名學沒有經過科學驗證，"
           u"各流派的規則也互相矛盾，內容僅供文化與知識參考，不構成改名或人生決策的建議。")

# 八十一數理吉凶（熊崎氏系統的常見版本；各書略有出入）
SHU81 = u"吉凶吉凶吉吉吉吉凶凶吉凶吉凶吉吉吉吉凶凶吉凶吉吉吉半半凶吉半吉吉吉凶吉凶吉半吉凶吉凶凶凶吉凶吉吉凶凶半吉凶凶半凶吉半凶凶吉凶吉凶吉凶吉吉凶凶半凶半凶半凶半半凶凶吉"
assert len(SHU81) == 81

XMLIB = r"""
(function () {
  if (window.__xmLib) return; window.__xmLib = 1;
""" + BASEJS + r"""
  var SK = {}, TN = {};
  '""" + STROKES + r"""'.split('|').forEach(function (g) { var p = g.split(':'), n = +p[0]; for (var i = 0; i < p[1].length; i++) SK[p[1][i]] = n; });
  '""" + TONES + r"""'.split('|').forEach(function (g) { var p = g.split(':'), n = +p[0]; for (var i = 0; i < p[1].length; i++) TN[p[1][i]] = n; });
  SK['郎'] = 14;
  var S81 = '""" + SHU81 + r"""';
  var FU = ['歐陽', '司馬', '諸葛', '上官', '東方', '夏侯', '皇甫', '尉遲', '公孫', '慕容', '長孫', '宇文', '司徒', '司空', '令狐', '端木', '西門', '南宮', '張簡', '范姜', '周黃', '張廖', '簡黃', '劉張', '陳黃', '江謝', '徐辜'];
  var WX = ['水', '木', '木', '火', '火', '土', '土', '金', '金', '水'], WXC = { 木: '#4a9a5e', 火: '#d0564f', 土: '#b8941f', 金: '#8a8a8a', 水: '#3a6ea5' };
  var SHENG = { 木: '火', 火: '土', 土: '金', 金: '水', 水: '木' }, KE = { 木: '土', 土: '水', 水: '火', 火: '金', 金: '木' };
  function wxOf(n) { return WX[n % 10]; }
  function ji(n) { var k = ((n - 1) % 80) + 1; var c = S81[k - 1]; return c === '半' ? '半吉' : c; }
  function jic(s) { return s === '吉' ? '#4a9a5e' : s === '凶' ? '#d0564f' : '#d9822b'; }
  function rel(a, b) { if (a === b) return '比和'; if (SHENG[a] === b) return a + '生' + b; if (SHENG[b] === a) return b + '生' + a; if (KE[a] === b) return a + '剋' + b; return b + '剋' + a; }
  function wuge(sur, giv) { var s = sur, g = giv, T, R, D, W, Z = s.concat(g).reduce(function (a, b) { return a + b; }, 0);
    if (s.length === 1) { T = s[0] + 1; R = s[0] + g[0]; } else { T = s[0] + s[1]; R = s[1] + g[0]; }
    if (g.length === 1) D = g[0] + 1; else D = g[0] + g[1];
    if (s.length === 1 && g.length === 1) W = 2; else if (s.length === 1) W = g[g.length - 1] + 1; else if (g.length === 1) W = s[0] + 1; else W = s[0] + g[g.length - 1];
    return { 天格: T, 人格: R, 地格: D, 外格: W, 總格: Z }; }

  /* ---------- 五格計算器 ---------- */
  function initWuge(root, cfg) {
    head(root, cfg.q); var row = el('div'), inp = document.createElement('input'), sp = document.createElement('select'), grid = el('div', 'display:flex;flex-wrap:wrap;gap:6px;margin-top:8px'), out = el('div');
    inp.value = cfg.name || '陳家豪'; inp.style.cssText = 'font-size:1.3em;width:8em;padding:4px 8px;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text)';
    sp.innerHTML = '<option value="auto">自動判斷姓氏</option><option value="1">單姓</option><option value="2">複姓</option>'; sp.style.cssText = 'margin-left:8px;padding:4px;border:1px solid var(--border);border-radius:6px;background:var(--surface);color:var(--text)';
    row.appendChild(el('span', 'margin-right:6px', '姓名：')); row.appendChild(inp); row.appendChild(sp); root.appendChild(row); root.appendChild(grid); root.appendChild(out);
    var over = {};
    inp.addEventListener('input', function () { over = {}; draw(); }); sp.addEventListener('change', draw);
    function draw() { var nm = inp.value.replace(/\s/g, '').slice(0, 4), chars = nm.split(''); if (chars.length < 2) { out.innerHTML = '請輸入二到四個字的中文姓名。'; grid.innerHTML = ''; return; }
      var ns = sp.value === 'auto' ? (FU.indexOf(nm.slice(0, 2)) >= 0 && chars.length >= 3 ? 2 : 1) : +sp.value; if (chars.length - ns < 1) ns = 1;
      var st = chars.map(function (c, i) { return over[i] || SK[c] || 0; });
      grid.innerHTML = ''; chars.forEach(function (c, i) { var box = el('div', 'text-align:center;padding:6px 10px;border:1px solid var(--border);border-radius:8px;' + (i < ns ? 'background:var(--accent-soft)' : ''));
        box.appendChild(el('div', 'font-size:1.6em', c)); var n = document.createElement('input'); n.type = 'number'; n.min = 1; n.max = 64; n.value = st[i] || ''; n.style.cssText = 'width:3.4em;text-align:center;border:1px solid var(--border);border-radius:4px;background:var(--surface);color:var(--text)';
        n.addEventListener('change', function () { over[i] = +n.value; draw(); }); box.appendChild(n); box.appendChild(el('div', 'font-size:0.75em;color:var(--text-muted)', (SK[c] ? '' : '查無資料 ') + (TN[c] ? '第 ' + TN[c] + ' 聲' : '')));
        grid.appendChild(box); });
      if (st.some(function (x) { return !x; })) { out.innerHTML = '<p>有字查不到康熙筆畫，請在上方手動輸入。</p>'; return; }
      var r = wuge(st.slice(0, ns), st.slice(ns)), o = '<table style="border-collapse:collapse;width:100%;margin-top:10px;font-size:0.95em"><tr>' + ['格', '數', '五行', '八十一數理', '傳統含義'].map(function (h) { return '<th style="border:1px solid var(--border);padding:5px">' + h + '</th>'; }).join('') + '</tr>';
      var mean = { 天格: '祖先、家世（由姓決定，自己無法選擇）', 人格: '主運：個性與一生的核心', 地格: '前運：青少年時期、與子女部屬', 外格: '副運：人際、外在環境', 總格: '後運：中年以後的整體' };
      Object.keys(r).forEach(function (k) { var v = r[k], w = wxOf(v), j = ji(v); o += '<tr><td style="border:1px solid var(--border);padding:5px;text-align:center;font-weight:bold">' + k + '</td><td style="border:1px solid var(--border);text-align:center">' + v + '</td><td style="border:1px solid var(--border);text-align:center;color:' + WXC[w] + ';font-weight:bold">' + w + '</td><td style="border:1px solid var(--border);text-align:center;color:' + jic(j) + ';font-weight:bold">' + j + '</td><td style="border:1px solid var(--border);padding:5px;font-size:0.88em">' + mean[k] + '</td></tr>'; });
      o += '</table>';
      var t = wxOf(r.天格), h = wxOf(r.人格), d = wxOf(r.地格);
      o += '<p style="margin:8px 0 0"><b>三才</b>：天' + t + '－人' + h + '－地' + d + '。天格與人格：' + rel(t, h) + '；人格與地格：' + rel(h, d) + '。傳統上「生」與「比和」被視為較好，「剋」較差，但不同書的三才吉凶表彼此矛盾（第 14、17 課）。</p>';
      var tones = chars.map(function (c) { return TN[c] || 0; }), tn = tones.map(function (x) { return x ? x : '?'; }).join('－');
      var same = tones.length > 1 && tones.every(function (x) { return x === tones[0]; });
      o += '<p style="margin:6px 0 0"><b>聲調</b>：' + tn + (same ? '——<b>全部同聲調</b>，唸起來可能較單調（第 24 課）。' : '。') + '<span style="font-size:0.85em;color:var(--text-muted)">（讀音資料以 Unihan 的普通話標準為主，台灣讀音偶有不同）</span></p>';
      o += '<p style="font-size:0.8em;color:var(--text-muted);margin:6px 0 0">康熙筆畫依部首原形計算（例如氵算 4 畫、艹算 6 畫），一到十的數字依數字本身計算。各派算法略有不同，可以點數字修改。本工具僅供了解姓名學的算法，不構成改名建議。</p>';
      out.innerHTML = o; }
    draw();
  }

  /* ---------- 單字筆畫查詢 ---------- */
  function initChar(root, cfg) {
    head(root, cfg.q); var inp = document.createElement('input'), out = el('div', 'margin-top:8px;display:flex;flex-wrap:wrap;gap:6px');
    inp.value = cfg.s || '江淑芬達陳郭玲'; inp.style.cssText = 'font-size:1.2em;width:100%;box-sizing:border-box;padding:4px 8px;border:1px solid var(--border);border-radius:8px;background:var(--surface);color:var(--text)';
    root.appendChild(inp); root.appendChild(out); inp.addEventListener('input', draw);
    function draw() { out.innerHTML = ''; inp.value.split('').slice(0, 30).forEach(function (c) { if (/\s/.test(c)) return;
        out.appendChild(el('div', 'text-align:center;min-width:52px;padding:4px 6px;border:1px solid var(--border);border-radius:8px', '<div style="font-size:1.5em">' + c + '</div><div style="font-weight:bold">' + (SK[c] ? SK[c] + ' 畫' : '—') + '</div><div style="font-size:0.75em;color:' + (SK[c] ? WXC[wxOf(SK[c])] : 'var(--text-muted)') + '">' + (SK[c] ? '尾數屬' + wxOf(SK[c]) : '查無') + '</div>')); }); }
    draw();
  }

  /* ---------- 八十一數理 ---------- */
  function initShu(root, cfg) {
    head(root, cfg.q); var view = el('div'), info = el('p', 'margin:6px 0 0'), sel = 1; root.appendChild(view); root.appendChild(info);
    function draw() { var o = ''; for (var i = 1; i <= 81; i++) { var x = 14 + ((i - 1) % 9) * 68, y = 6 + Math.floor((i - 1) / 9) * 34, j = ji(i);
        o += '<g data-i="' + i + '" style="cursor:pointer"><rect x="' + x + '" y="' + y + '" width="64" height="30" rx="5" fill="' + jic(j) + '" opacity="' + (i === sel ? 1 : 0.28) + '" stroke="' + jic(j) + '"/>' + tx(x + 32, y + 20, i + ' ' + j, 11, i === sel ? '#fff' : 'currentColor') + '</g>'; }
      view.innerHTML = svgw('0 0 640 314', o); view.querySelectorAll('g[data-i]').forEach(function (g) { g.addEventListener('click', function () { sel = +g.getAttribute('data-i'); draw(); }); });
      var cnt = { 吉: 0, 凶: 0, 半吉: 0 }; for (var k = 1; k <= 81; k++) cnt[ji(k)]++;
      info.innerHTML = '<b>' + sel + '</b> 畫：' + ji(sel) + '，五行屬' + wxOf(sel) + '。全部 81 個數中，吉 ' + cnt.吉 + '、凶 ' + cnt.凶 + '、半吉 ' + cnt.半吉 + '。超過 81 的數減去 80 再看。<span style="font-size:0.88em;color:var(--text-muted)">（這是熊崎氏系統的常見版本，不同書籍有幾個數的吉凶判斷不同。）</span>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.xm-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ wuge: initWuge, char: initChar, shu: initShu })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def xmw(cfg, maxw=680):
    return wdg("xm-w", cfg, maxw)


xmlesson = make_lesson(u"✍️", XM_NOTE, XMLIB, "xm-w")
