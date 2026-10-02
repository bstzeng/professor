# -*- coding: utf-8 -*-
"""〈八字命理〉共用工具與互動元件（BZLIB）。排盤引擎見 bz_engine.js（已以 lunar_python 交叉驗證）。"""
import os
from cc_common import *
from qt_common import BASEJS

BZ_NOTE = (u"本課程介紹八字命理的傳統規則與文化脈絡。命理沒有經過科學驗證，"
           u"內容僅供文化與知識參考，不構成人生、醫療、婚姻或投資決策的建議。")

_ENGINE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "bz_engine.js"), encoding="utf-8").read()
_ENGINE = _ENGINE.replace("if (typeof module !== 'undefined') module.exports = BZ;", "")

NAYIN = u"海中金爐中火大林木路旁土劍鋒金山頭火澗下水城頭土白蠟金楊柳木泉中水屋上土霹靂火松柏木長流水沙中金山下火平地木壁上土金箔金覆燈火天河水大驛土釵釧金桑柘木大溪水沙中土天上火石榴木大海水"

BZLIB = r"""
(function () {
  if (window.__bzLib) return; window.__bzLib = 1;
""" + BASEJS + _ENGINE + r"""
  var G = BZ.GAN, Z = BZ.ZHI, SX = '鼠牛虎兔龍蛇馬羊猴雞狗豬', NY = '""" + NAYIN + r"""';
  var WXC = { 木: '#4a9a5e', 火: '#d0564f', 土: '#b8941f', 金: '#8a8a8a', 水: '#3a6ea5' };
  function nayin(g, z) { var i = BZ.mod(6 * g - 5 * z, 60); return NY.substr(Math.floor(i / 2) * 3, 3); }
  function wxSpan(ch, wx, big) { return '<span style="color:' + WXC[wx] + ';font-weight:bold;font-size:' + (big || 1) + 'em">' + ch + '</span>'; }
  function cell(css, html) { return '<td style="padding:6px 4px;text-align:center;border:1px solid var(--border);' + (css || '') + '">' + html + '</td>'; }
  function fmtDate(t) { return t.y + '/' + t.m + '/' + t.d + ' ' + ('0' + Math.floor(t.h)).slice(-2) + ':' + ('0' + Math.floor((t.h % 1) * 60)).slice(-2); }
  function input(lab, type, val, css) { var w = el('label', 'display:inline-block;margin:4px 10px 4px 0;font-size:0.9em', lab + ' '), i = document.createElement(type === 'select' ? 'select' : 'input');
    if (type !== 'select') i.type = type; i.value = val; i.style.cssText = 'padding:3px 6px;border:1px solid var(--border);border-radius:6px;background:var(--surface);color:var(--text);font:inherit;' + (css || ''); w.appendChild(i); return [w, i]; }

  /* ---------- 排盤器 ---------- */
  function initPan(root, cfg) {
    head(root, cfg.q); var form = el('div'), out = el('div'), now = new Date();
    var fD = input('出生日期', 'date', cfg.date || '1990-06-15'), fT = input('時間', 'time', cfg.time || '08:30'), fS = input('性別', 'select', ''), fZ = input('時區', 'select', ''),
      fDst = input('夏令時間', 'checkbox', ''), fTs = input('真太陽時', 'checkbox', ''), fL = input('經度', 'number', '121.5', 'width:5em'), fZi = input('子時', 'select', '');
    fS[1].innerHTML = '<option value="1">男</option><option value="0">女</option>';
    fZ[1].innerHTML = '<option value="8">UTC+8（台灣、中國、香港、新加坡）</option><option value="9">UTC+9（日本、韓國）</option><option value="7">UTC+7（泰國、越南）</option><option value="-5">UTC−5（美東）</option><option value="-8">UTC−8（美西）</option><option value="0">UTC+0（英國）</option>';
    fZi[1].innerHTML = '<option value="early">23 點換日（子初換日）</option><option value="late">0 點換日（晚子時日柱不變）</option>';
    [fD, fT, fS, fZ, fDst, fTs, fL, fZi].forEach(function (f) { form.appendChild(f[0]); f[1].addEventListener('change', draw); f[1].addEventListener('input', draw); });
    root.appendChild(form); root.appendChild(out);
    function draw() { var dv = fD[1].value.split('-'), tv = fT[1].value.split(':'); if (dv.length < 3 || tv.length < 2) return;
      var c = BZ.chart({ y: +dv[0], m: +dv[1], d: +dv[2], h: +tv[0], mi: +tv[1], tz: +fZ[1].value, dst: fDst[1].checked, lon: fTs[1].checked ? +fL[1].value : null, male: fS[1].value === '1', zi: fZi[1].value });
      var names = ['年柱', '月柱', '日柱', '時柱'], o = '<table style="border-collapse:collapse;width:100%;margin-top:8px;font-size:0.95em"><tr>' + cell('font-weight:bold;width:4.5em', '') + names.map(function (n) { return cell('font-weight:bold', n); }).join('') + '</tr>';
      o += '<tr>' + cell('color:var(--text-muted)', '十神') + c.P.map(function (p, i) { return cell('', i === 2 ? '<b>日主</b>' : BZ.shiShen(c.dg, p[0])); }).join('') + '</tr>';
      o += '<tr>' + cell('color:var(--text-muted)', '天干') + c.P.map(function (p) { return cell('', wxSpan(G[p[0]], BZ.GAN_WX[p[0]], 1.8)); }).join('') + '</tr>';
      o += '<tr>' + cell('color:var(--text-muted)', '地支') + c.P.map(function (p) { return cell('', wxSpan(Z[p[1]], BZ.ZHI_WX[p[1]], 1.8) + '<div style="font-size:0.75em;color:var(--text-muted)">' + SX[p[1]] + '</div>'); }).join('') + '</tr>';
      o += '<tr>' + cell('color:var(--text-muted)', '藏干') + c.P.map(function (p) { return cell('font-size:0.85em', BZ.HIDE[p[1]].split('').map(function (h) { var gi = G.indexOf(h); return wxSpan(h, BZ.GAN_WX[gi]) + '<span style="color:var(--text-muted)">' + BZ.shiShen(c.dg, gi) + '</span>'; }).join('<br>')); }).join('') + '</tr>';
      o += '<tr>' + cell('color:var(--text-muted)', '納音') + c.P.map(function (p) { return cell('font-size:0.85em', nayin(p[0], p[1])); }).join('') + '</tr></table>';
      var tot = 0; for (var k in c.wx) tot += c.wx[k];
      o += '<div style="display:flex;gap:4px;margin-top:10px;align-items:flex-end;height:70px">' + Object.keys(c.wx).map(function (k) { var h = c.wx[k] / tot * 160; return '<div style="flex:1;text-align:center;font-size:0.8em"><div style="background:' + WXC[k] + ';height:' + n1(h) + 'px;border-radius:4px 4px 0 0;opacity:0.8"></div>' + k + ' ' + f1(c.wx[k]) + '</div>'; }).join('') + '</div>';
      o += '<p style="font-size:0.8em;color:var(--text-muted);margin:2px 0 8px">五行力量的粗略統計（天干 1、地支本氣 0.6、中氣與餘氣 0.3）。實際論命還要看月令、通根與組合，第 24 課起說明。</p>';
      o += '<div style="font-size:0.9em"><b>大運</b>（' + (c.fwd ? '順行' : '逆行') + '，約 ' + f1(c.startAge) + ' 歲起運）</div><div style="display:flex;flex-wrap:wrap;gap:4px;margin-top:4px">' +
        c.dy.map(function (d) { return '<div style="padding:4px 8px;border:1px solid var(--border);border-radius:6px;text-align:center;font-size:0.85em">' + wxSpan(G[d.g], BZ.GAN_WX[d.g]) + wxSpan(Z[d.z], BZ.ZHI_WX[d.z]) + '<div style="color:var(--text-muted)">' + Math.floor(d.age) + '～' + Math.floor(d.age + 9) + ' 歲</div></div>'; }).join('') + '</div>';
      var pj = c.dt(c.prevJie.j), nj = c.dt(c.nextJie.j);
      o += '<p style="font-size:0.85em;margin:8px 0 0;color:var(--text-muted)">出生前的節：' + c.jieName(c.prevJie) + '（' + fmtDate(pj) + '，UTC+8）；之後的節：' + c.jieName(c.nextJie) + '（' + fmtDate(nj) + '）。' +
        (fTs[1].checked ? '真太陽時修正約 ' + (c.corr >= 0 ? '+' : '') + Math.round(c.corr) + ' 分鐘，換算後為 ' + fmtDate(c.solar) + '。' : '') +
        (Math.min(Math.abs(c.ut - c.prevJie.j), Math.abs(c.nextJie.j - c.ut)) * 24 < 2 ? '<br><b style="color:#d0564f">出生時間距離節氣交接不到兩小時，月柱可能因出生時間的誤差而不同，請特別確認。</b>' : '') + '</p>';
      o += '<p style="font-size:0.8em;color:var(--text-muted);margin:6px 0 0">節氣以 VSOP87 天文公式計算（與萬年曆誤差約一分鐘內）。本工具僅供學習八字的結構，不構成任何建議。</p>';
      out.innerHTML = o; }
    draw();
  }

  /* ---------- 干支年份查詢 ---------- */
  function initYear(root, cfg) {
    head(root, cfg.q); var out = el('div', 'margin-top:6px'), y = 2026;
    var u = slider(root, '西元年', 1900, 2100, 1, y, function (v) { return v; }, 'y', function (v) { y = v; draw(); }); root.appendChild(out);
    function draw() { var i = BZ.mod(y - 4, 60), g = i % 10, z = i % 12;
      out.innerHTML = '<div style="font-size:2.2em;text-align:center">' + wxSpan(G[g], BZ.GAN_WX[g], 1) + wxSpan(Z[z], BZ.ZHI_WX[z], 1) + '</div><p style="text-align:center;margin:4px 0">' + y + ' 年是<b>' + G[g] + Z[z] + '</b>年，生肖屬<b>' + SX[z] + '</b>，納音「' + nayin(g, z) + '」，六十甲子中的第 ' + (i + 1) + ' 位。<br><span style="color:var(--text-muted);font-size:0.9em">注意：八字的年份以<b>立春</b>（約 2 月 4 日）為界，而不是農曆新年。</span></p>'; }
    u();
  }

  /* ---------- 十神查詢 ---------- */
  function initShen(root, cfg) {
    head(root, cfg.q); var bar = el('div'), out = el('div'), dg = 0; root.appendChild(bar); root.appendChild(out);
    G.split('').forEach(function (g, i) { var b = btn(g, i); b.addEventListener('click', function () { dg = i; mark(bar, i); draw(); }); bar.appendChild(b); });
    function draw() { var o = '<table style="border-collapse:collapse;width:100%;margin-top:8px;font-size:0.92em"><tr>' + cell('font-weight:bold', '其他天干') + cell('font-weight:bold', '五行') + cell('font-weight:bold', '與日主的關係') + cell('font-weight:bold', '十神') + '</tr>';
      var rel = ['同我', '我生', '我剋', '剋我', '生我'];
      for (var g = 0; g < 10; g++) { var a = BZ.mod(Math.floor(g / 2) - Math.floor(dg / 2), 5); o += '<tr>' + cell('', wxSpan(G[g], BZ.GAN_WX[g], 1.2)) + cell('', BZ.GAN_WX[g] + (g % 2 ? '（陰）' : '（陽）')) + cell('', rel[a] + (g % 2 === dg % 2 ? '，同性' : '，異性')) + cell('font-weight:bold', g === dg ? '比肩（日主本身）' : BZ.shiShen(dg, g)) + '</tr>'; }
      out.innerHTML = o + '</table><p style="font-size:0.88em;margin:6px 0 0">日主是<b>' + G[dg] + '</b>（' + BZ.GAN_WX[dg] + '，' + (dg % 2 ? '陰' : '陽') + '）。十神由「五行關係」與「陰陽是否相同」兩個條件決定。</p>'; }
    mark(bar, 0); draw();
  }

  /* ---------- 地支關係 ---------- */
  function initRel(root, cfg) {
    head(root, cfg.q); var bar = el('div'), out = el('div', 'margin-top:8px;line-height:1.7'), sel = []; root.appendChild(bar); root.appendChild(out);
    var HE = [[0, 1, '土'], [2, 11, '木'], [3, 10, '火'], [4, 9, '金'], [5, 8, '水'], [6, 7, '火（或土）']], CH = [[0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]], HAI = [[0, 7], [1, 6], [2, 5], [3, 4], [8, 11], [9, 10]];
    var SAN = [[[8, 0, 4], '水'], [[11, 3, 7], '木'], [[2, 6, 10], '火'], [[5, 9, 1], '金']], HUI = [[[2, 3, 4], '東方木'], [[5, 6, 7], '南方火'], [[8, 9, 10], '西方金'], [[11, 0, 1], '北方水']];
    var XING = [[[2, 5, 8], '無恩之刑'], [[1, 10, 7], '恃勢之刑'], [[0, 3], '無禮之刑']], SELF = [4, 6, 9, 11];
    Z.split('').forEach(function (z, i) { var b = btn(z + SX[i], i); b.addEventListener('click', function () { var k = sel.indexOf(i); if (k >= 0) sel.splice(k, 1); else { sel.push(i); if (sel.length > 3) sel.shift(); } upd(); }); bar.appendChild(b); });
    function has(arr) { return arr.every(function (x) { return sel.indexOf(x) >= 0; }); }
    function upd() { bar.querySelectorAll('button').forEach(function (b) { var on = sel.indexOf(+b.getAttribute('data-k')) >= 0; b.style.background = on ? 'var(--accent-soft)' : 'var(--surface)'; b.style.fontWeight = on ? 'bold' : 'normal'; });
      var r = []; HE.forEach(function (h) { if (has([h[0], h[1]])) r.push('<b>六合</b>：' + Z[h[0]] + Z[h[1]] + '合' + h[2]); });
      CH.forEach(function (h) { if (has(h)) r.push('<b style="color:#d0564f">六沖</b>：' + Z[h[0]] + Z[h[1]] + '相沖'); });
      HAI.forEach(function (h) { if (has(h)) r.push('<b>六害</b>：' + Z[h[0]] + Z[h[1]] + '相害'); });
      SAN.forEach(function (h) { var n = h[0].filter(function (x) { return sel.indexOf(x) >= 0; }).length; if (n === 3) r.push('<b>三合</b>：' + h[0].map(function (x) { return Z[x]; }).join('') + '三合' + h[1] + '局'); else if (n === 2 && sel.indexOf(h[0][1]) >= 0) r.push('<b>半合</b>：' + h[0].filter(function (x) { return sel.indexOf(x) >= 0; }).map(function (x) { return Z[x]; }).join('') + '半合' + h[1] + '（含中間的「旺支」）'); });
      HUI.forEach(function (h) { if (has(h[0])) r.push('<b>三會</b>：' + h[0].map(function (x) { return Z[x]; }).join('') + '會' + h[1]); });
      XING.forEach(function (h) { var n = h[0].filter(function (x) { return sel.indexOf(x) >= 0; }).length; if (n === h[0].length || (h[0].length === 3 && n === 2)) r.push('<b>刑</b>：' + h[0].filter(function (x) { return sel.indexOf(x) >= 0; }).map(function (x) { return Z[x]; }).join('') + '（' + h[1] + (n < h[0].length ? '，不全' : '') + '）'); });
      SELF.forEach(function (x) { if (sel.filter(function (s) { return s === x; }).length > 1) r.push('自刑'); });
      out.innerHTML = sel.length < 2 ? '請選擇兩到三個地支。' : (r.length ? r.join('<br>') : '這幾個地支之間沒有傳統的合、沖、刑、害關係。'); }
    upd();
  }

  /* ---------- 時辰與真太陽時 ---------- */
  function initShichen(root, cfg) {
    head(root, cfg.q); var lon = 121.5, h = 7, m = 0, view = el('div'), out = el('p', 'margin:6px 0 0'); root.appendChild(view);
    var u1 = slider(root, '鐘錶時間', 0, 1439, 5, h * 60 + m, function (v) { return ('0' + Math.floor(v / 60)).slice(-2) + ':' + ('0' + v % 60).slice(-2); }, 't', function (v) { h = Math.floor(v / 60); m = v % 60; draw(); });
    var u2 = slider(root, '出生地經度（UTC+8 標準經線為 120°E）', 73, 135, 0.5, lon, function (v) { return v + '°E'; }, 'lon', function (v) { lon = v; draw(); }); root.appendChild(out);
    var places = [[87.6, '烏魯木齊'], [104.1, '成都'], [114.2, '香港'], [116.4, '北京'], [120.3, '高雄'], [121.5, '台北'], [126.6, '哈爾濱']];
    function draw() { var corr = (lon - 120) * 4, t = h * 60 + m + corr, tt = BZ.mod(t, 1440), hz = Math.floor(BZ.mod(tt / 60 + 1, 24) / 2), hz0 = Math.floor(BZ.mod((h * 60 + m) / 60 + 1, 24) / 2);
      var o = ''; for (var i = 0; i < 12; i++) { var x = 20 + i * 50; o += '<rect x="' + x + '" y="20" width="48" height="40" rx="6" fill="' + (i === hz ? 'var(--accent-soft)' : 'var(--surface)') + '" stroke="' + (i === hz ? '#3a6ea5' : 'var(--border)') + '"/>' + tx(x + 24, 46, Z[i], 15, i === hz ? '#3a6ea5' : 'currentColor') + tx(x + 24, 76, ('0' + BZ.mod(i * 2 - 1, 24)).slice(-2) + '–' + ('0' + BZ.mod(i * 2 + 1, 24)).slice(-2), 9, 'var(--text-muted)'); }
      view.innerHTML = svgw('0 0 640 90', o);
      var near = places.reduce(function (a, b) { return Math.abs(b[0] - lon) < Math.abs(a[0] - lon) ? b : a; });
      out.innerHTML = '經度修正 ' + (corr >= 0 ? '+' : '') + Math.round(corr) + ' 分鐘（每差 1 度差 4 分鐘；附近城市：' + near[1] + '）。地方平太陽時約 ' + ('0' + Math.floor(tt / 60)).slice(-2) + ':' + ('0' + Math.floor(tt % 60)).slice(-2) + '，屬<b>' + Z[hz] + '時</b>' +
        (hz !== hz0 ? '——<b style="color:#d0564f">和直接用鐘錶時間（' + Z[hz0] + '時）不同！</b>' : '。') + '<br><span style="font-size:0.88em;color:var(--text-muted)">嚴格的真太陽時還要加上「均時差」（一年中在 −14 到 +16 分鐘之間變化），排盤器會自動計算。</span>'; }
    u1(); u2();
  }

  function initAll() { document.querySelectorAll('.bz-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ pan: initPan, year: initYear, shen: initShen, rel: initRel, shichen: initShichen })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def bzw(cfg, maxw=680):
    return wdg("bz-w", cfg, maxw)


bzlesson = make_lesson(u"☯️", BZ_NOTE, BZLIB, "bz-w")
