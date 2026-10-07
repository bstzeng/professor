# -*- coding: utf-8 -*-
"""〈氣的輸送〉（qi_）共用工具與互動元件（QILIB）。"""
from cc_common import *
from qt_common import BASEJS

QI_NOTE = (u"本課程介紹中醫理論中「氣」的模型，並對照現代研究證據；「輸送現象」的說法是整理思路用的類比，不代表氣是可以量測的流體。"
           u"內容不是診斷或治療建議，身體不適請就醫；練習呼吸與導引時若頭暈、胸悶或疼痛，請立即停止。")

QILIB = r"""
(function () {
  if (window.__qiLib) return; window.__qiLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  /* 十二經：名稱、縮寫、時辰、起始小時、手足陰陽、表裡經、顏色、說明 */
  var M = [['手太陰肺經', '肺', '寅', 3, '手三陰', '大腸', '#8a8a8a', '起於中焦，出於胸，沿上肢內側前緣到拇指。主氣、司呼吸，十二經流注的起點。'],
    ['手陽明大腸經', '大腸', '卯', 5, '手三陽', '肺', '#8a8a8a', '起於食指，沿上肢外側前緣上行到鼻旁。'],
    ['足陽明胃經', '胃', '辰', 7, '足三陽', '脾', '#b8941f', '起於鼻旁，經面、胸腹前面，沿下肢外側前緣到第二趾。是「多氣多血」之經。'],
    ['足太陰脾經', '脾', '巳', 9, '足三陰', '胃', '#b8941f', '起於大趾，沿下肢內側上行，入腹屬脾。脾主運化，是後天之氣的來源。'],
    ['手少陰心經', '心', '午', 11, '手三陰', '小腸', '#d0564f', '起於心中，出腋下，沿上肢內側後緣到小指。'],
    ['手太陽小腸經', '小腸', '未', 13, '手三陽', '心', '#d0564f', '起於小指，沿上肢外側後緣上行到肩胛、面頰。'],
    ['足太陽膀胱經', '膀胱', '申', 15, '足三陽', '腎', '#3a6ea5', '起於目內眥，上頭頂，沿背部脊柱兩側下行到小趾。是最長、穴位最多的經脈，背部的「背俞穴」都在這條經上。'],
    ['足少陰腎經', '腎', '酉', 17, '足三陰', '膀胱', '#3a6ea5', '起於足底湧泉，沿下肢內側後緣上行，屬腎。腎藏先天之精與元氣。'],
    ['手厥陰心包經', '心包', '戌', 19, '手三陰', '三焦', '#d9822b', '起於胸中，沿上肢內側中線到中指。內關穴在此經上。'],
    ['手少陽三焦經', '三焦', '亥', 21, '手三陽', '心包', '#d9822b', '起於無名指，沿上肢外側中線上行到耳、眉梢。'],
    ['足少陽膽經', '膽', '子', 23, '足三陽', '肝', '#4a9a5e', '起於目外眥，繞頭側，沿身體側面下行到第四趾。'],
    ['足厥陰肝經', '肝', '丑', 1, '足三陰', '膽', '#4a9a5e', '起於大趾，沿下肢內側上行，繞陰器、抵小腹、布脅肋，最後上注於肺，完成一個循環。']];

  /* ---------- 子午流注時辰圖 ---------- */
  function initZiwu(root, cfg) {
    head(root, cfg.q); var h = cfg.h || 8, view = el('div'), p;
    var u = slider(root, '時間', 0, 23.5, 0.5, h, function (v) { var hh = Math.floor(v), mm = v % 1 ? '30' : '00'; return (hh < 10 ? '0' : '') + hh + ':' + mm; }, 'h', function (v) { h = v; draw(); });
    root.appendChild(view); p = info(root);
    function idx(t) { for (var i = 0; i < 12; i++) { var s = M[i][3], e = (s + 2) % 24; if (s < e ? (t >= s && t < e) : (t >= s || t < e)) return i; } return 0; }
    function draw() { var cx = 200, cy = 170, R = 135, r = 82, o = '', k = idx(h);
      for (var i = 0; i < 12; i++) { var a0 = (M[i][3] / 24) * 2 * Math.PI - Math.PI / 2, a1 = ((M[i][3] + 2) / 24) * 2 * Math.PI - Math.PI / 2, on = i === k;
        var x0 = cx + R * Math.cos(a0), y0 = cy + R * Math.sin(a0), x1 = cx + R * Math.cos(a1), y1 = cy + R * Math.sin(a1), x2 = cx + r * Math.cos(a1), y2 = cy + r * Math.sin(a1), x3 = cx + r * Math.cos(a0), y3 = cy + r * Math.sin(a0);
        o += '<path d="M' + n1(x0) + ',' + n1(y0) + ' A' + R + ',' + R + ' 0 0 1 ' + n1(x1) + ',' + n1(y1) + ' L' + n1(x2) + ',' + n1(y2) + ' A' + r + ',' + r + ' 0 0 0 ' + n1(x3) + ',' + n1(y3) + ' Z" fill="' + M[i][6] + '" fill-opacity="' + (on ? 0.85 : 0.22) + '" stroke="var(--surface)" stroke-width="2"/>';
        var am = (a0 + a1) / 2; o += tx(cx + (R + r) / 2 * Math.cos(am), cy + (R + r) / 2 * Math.sin(am) + 4, M[i][1], 12, on ? '#fff' : 'currentColor') + tx(cx + (R + 16) * Math.cos(am), cy + (R + 16) * Math.sin(am) + 4, M[i][2], 10.5, 'var(--text-muted)'); }
      var ah = (h / 24) * 2 * Math.PI - Math.PI / 2; o += ln(cx, cy, cx + (r - 8) * Math.cos(ah), cy + (r - 8) * Math.sin(ah), '#d0564f', 3) + '<circle cx="' + cx + '" cy="' + cy + '" r="5" fill="#d0564f"/>';
      o += tx(cx, 326, '子（23–1 時）在上、午（11–13 時）在下', 9.5, 'var(--text-muted)');
      var m = M[k]; o += tx(380, 70, m[0], 15, m[6], 'start') + tx(380, 96, m[2] + '時（' + m[3] + '–' + ((m[3] + 2) % 24) + ' 時）', 12, 'currentColor', 'start') + tx(380, 120, m[4] + '；與' + m[5] + '經互為表裡', 11, 'var(--text-muted)', 'start');
      o += tx(380, 160, '下一經：' + M[(k + 1) % 12][0], 11, 'currentColor', 'start') + tx(380, 184, '上一經：' + M[(k + 11) % 12][0], 11, 'var(--text-muted)', 'start');
      view.innerHTML = svgw('0 0 640 336', o);
      p.innerHTML = '<b>' + m[0] + '</b>：' + m[7] + '<br><span style="font-size:0.9em;color:var(--text-muted)">子午流注把十二經與十二時辰對應，認為氣血在一天中依序「當令」於各經。這是宋金時期發展出的時間理論，用於針灸取穴的時間選擇；現代並沒有證據顯示人體有這樣的十二段流動，但生理功能確實有晝夜節律（第 24、40 課）。</span>'; }
    u();
  }

  /* ---------- 營衛運行 ---------- */
  function initYW(root, cfg) {
    head(root, cfg.q); var h = 12, view = el('div'), p;
    var u = slider(root, '時間', 0, 24, 0.25, h, function (v) { var hh = Math.floor(v) % 24, mm = Math.round((v % 1) * 60); return (hh < 10 ? '0' : '') + hh + ':' + (mm < 10 ? '0' : '') + mm; }, 'h', function (v) { h = v; draw(); });
    root.appendChild(view); p = info(root);
    function draw() { var o = '', day = h >= 6 && h < 18, ying = h / 24 * 50, wei = day ? (h - 6) / 12 * 25 : ((h + 6) % 24) / 12 * 25;
      o += '<rect x="20" y="30" width="600" height="40" rx="6" fill="#e8b84a" fill-opacity="0.25"/><rect x="20" y="30" width="150" height="40" rx="6" fill="#3a3a6a" fill-opacity="0.25"/><rect x="470" y="30" width="150" height="40" rx="6" fill="#3a3a6a" fill-opacity="0.25"/>';
      for (var t = 0; t <= 24; t += 6) o += tx(20 + t / 24 * 600, 88, t + ':00', 10, 'var(--text-muted)');
      o += tx(95, 54, '夜（陰）', 11, 'currentColor') + tx(320, 54, '晝（陽）', 11, 'currentColor') + tx(545, 54, '夜（陰）', 11, 'currentColor');
      o += ln(20 + h / 24 * 600, 24, 20 + h / 24 * 600, 76, '#d0564f', 2.5);
      o += tx(20, 120, '營氣（行於脈中）', 12, '#d0564f', 'start'); o += '<rect x="170" y="108" width="450" height="14" rx="4" fill="none" stroke="var(--border)"/><rect x="170" y="108" width="' + n1(ying / 50 * 450) + '" height="14" rx="4" fill="#d0564f" fill-opacity="0.7"/>' + tx(170, 140, '已循環 ' + f1(ying) + '／50 周（每周約 28.8 分鐘）', 10.5, 'currentColor', 'start');
      o += tx(20, 178, '衛氣（行於脈外）', 12, '#3a6ea5', 'start'); o += '<rect x="170" y="166" width="450" height="14" rx="4" fill="none" stroke="var(--border)"/><rect x="170" y="166" width="' + n1(wei / 25 * 450) + '" height="14" rx="4" fill="#3a6ea5" fill-opacity="0.7"/>' + tx(170, 198, (day ? '白天行於陽分：' : '夜間行於陰分（五臟）：') + f1(wei) + '／25 周', 10.5, 'currentColor', 'start');
      view.innerHTML = svgw('0 0 640 215', o);
      p.innerHTML = '《靈樞・營衛生會》：「營在脈中，衛在脈外，營周不休，五十而復大會。」又說衛氣「行於陰二十五度，行於陽二十五度，分為晝夜」。' +
        '<br>衛氣白天行於體表（陽），人就清醒、能抵禦外邪；夜間入於五臟（陰），人就入睡——這是古人對<b>睡眠與清醒</b>的解釋。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">示意以 6 時至 18 時為晝。對照：現代測得血液繞全身一周約需 1 分鐘左右，與營氣「一日五十周」的數字並不相同（第 13 課）。</span>'; }
    u();
  }

  /* ---------- 氣機升降 ---------- */
  var QJ = [['肝', 150, 160, '#4a9a5e', '升（主疏泄、升發，「肝生於左」）', '肝氣鬱結：脅肋脹痛、情緒抑鬱；肝氣上逆：頭痛、目赤、易怒'],
    ['肺', 490, 160, '#8a8a8a', '降（主肅降、宣發，「肺藏於右」）', '肺氣上逆：咳嗽、氣喘；肺氣不宣：胸悶、鼻塞'],
    ['心', 320, 60, '#d0564f', '心火下降，溫煦腎水', '心火亢盛、心腎不交：失眠、心煩'],
    ['腎', 320, 300, '#3a6ea5', '腎水上濟，滋潤心火；腎主納氣', '腎不納氣：呼多吸少、動則氣喘'],
    ['脾', 250, 220, '#b8941f', '升（升清：把水穀精微往上送到肺）', '脾氣下陷：久瀉、內臟下垂、脫肛'],
    ['胃', 390, 220, '#d9822b', '降（降濁：把食物往下送）', '胃氣上逆：噁心、嘔吐、打嗝、反酸']];
  function initQiji(root, cfg) {
    head(root, cfg.q); var sel = cfg.s || 0, view = el('div'), p; root.appendChild(view); p = info(root);
    function arrow(x, y, up, c) { return '<path d="M' + x + ',' + (y + (up ? 22 : -22)) + ' L' + x + ',' + (y + (up ? -22 : 22)) + '" stroke="' + c + '" stroke-width="3"/><path d="M' + (x - 7) + ',' + (y + (up ? -14 : 14)) + ' L' + x + ',' + (y + (up ? -24 : 24)) + ' L' + (x + 7) + ',' + (y + (up ? -14 : 14)) + '" fill="none" stroke="' + c + '" stroke-width="3"/>'; }
    function draw() { var o = '<ellipse cx="320" cy="180" rx="230" ry="160" fill="none" stroke="var(--border)" stroke-dasharray="4 4"/>';
      o += '<path d="M180 250 Q120 160 180 90" fill="none" stroke="#4a9a5e" stroke-width="2" stroke-dasharray="6 3"/><path d="M460 90 Q520 160 460 250" fill="none" stroke="#8a8a8a" stroke-width="2" stroke-dasharray="6 3"/>';
      o += tx(110, 110, '左升', 11, '#4a9a5e') + tx(530, 110, '右降', 11, '#8a8a8a') + tx(320, 345, '中焦脾胃為樞紐：脾升胃降', 10.5, 'var(--text-muted)');
      QJ.forEach(function (q, i) { var on = i === sel, up = /^升|上濟/.test(q[4]); o += '<g data-i="' + i + '" style="cursor:pointer"><circle cx="' + q[1] + '" cy="' + q[2] + '" r="' + (on ? 30 : 25) + '" fill="' + q[3] + '" fill-opacity="' + (on ? 0.9 : 0.35) + '"/>' + tx(q[1], q[2] + 6, q[0], 16, on ? '#fff' : 'currentColor') + '</g>' + arrow(q[1] + 44, q[2], up, q[3]); });
      view.innerHTML = svgw('0 0 640 360', o);
      view.querySelectorAll('g[data-i]').forEach(function (g) { g.addEventListener('click', function () { sel = +g.getAttribute('data-i'); draw(); }); });
      var q = QJ[sel]; p.innerHTML = '<b style="color:' + q[3] + '">' + q[0] + '</b>：正常是<b>' + q[4] + '</b>。<br>失常時（中醫的描述）：' + q[5] + '。<br><span style="font-size:0.9em;color:var(--text-muted)">點選圓圈切換臟腑。這是中醫「氣機」的理論模型；臟腑名稱指的是功能系統，不完全等於解剖學的器官。</span>'; }
    draw();
  }

  /* ---------- 十二經循環圖 ---------- */
  function initRing(root, cfg) {
    head(root, cfg.q); var sel = 0, view = el('div'), p; root.appendChild(view); p = info(root);
    function draw() { var cx = 320, cy = 190, R = 150, o = '', pts = [];
      for (var i = 0; i < 12; i++) { var a = i / 12 * 2 * Math.PI - Math.PI / 2; pts.push([cx + R * Math.cos(a), cy + R * Math.sin(a)]); }
      for (var j = 0; j < 12; j++) { var a1 = pts[j], b1 = pts[(j + 1) % 12], mx = (a1[0] + b1[0]) / 2, my = (a1[1] + b1[1]) / 2; o += ln(a1[0], a1[1], b1[0], b1[1], '#bbb', 1.5) + '<circle cx="' + n1(mx + (b1[0] - a1[0]) * 0.15) + '" cy="' + n1(my + (b1[1] - a1[1]) * 0.15) + '" r="3" fill="#999"/>'; }
      var pr = [sel, M.findIndex(function (m) { return m[1] === M[sel][5]; })]; o += ln(pts[pr[0]][0], pts[pr[0]][1], pts[pr[1]][0], pts[pr[1]][1], '#d0564f', 2, 'stroke-dasharray="5 4"');
      M.forEach(function (m, i) { var on = i === sel; o += '<g data-i="' + i + '" style="cursor:pointer"><circle cx="' + n1(pts[i][0]) + '" cy="' + n1(pts[i][1]) + '" r="' + (on ? 27 : 23) + '" fill="' + m[6] + '" fill-opacity="' + (on ? 0.9 : 0.3) + '" stroke="' + m[6] + '"/>' + tx(pts[i][0], pts[i][1] + 5, m[1], 13, on ? '#fff' : 'currentColor') + '</g>'; });
      o += tx(cx, cy - 6, '十二經首尾相接', 11, 'var(--text-muted)') + tx(cx, cy + 12, '如環無端', 11, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 640 380', o);
      view.querySelectorAll('g[data-i]').forEach(function (g) { g.addEventListener('click', function () { sel = +g.getAttribute('data-i'); draw(); }); });
      var m = M[sel]; p.innerHTML = '<b style="color:' + m[6] + '">' + m[0] + '</b>（' + m[4] + '）：' + m[7] + '<br>紅色虛線連到它的<b>表裡經</b>：' + m[5] + '經。灰色箭頭是流注方向：手三陰從胸走手 → 手三陽從手走頭 → 足三陽從頭走足 → 足三陰從足走腹胸。'; }
    draw();
  }

  /* ---------- 源—流—匯類比模型 ---------- */
  function initModel(root, cfg) {
    head(root, cfg.q); var st = { S: 1, R: 1, C: 1, D: 1, dir: 1 }, view = el('div'), p, us = [];
    var bb = bar(root); [['正常', [1, 1, 1, 1, 1]], ['氣虛', [0.45, 1, 1, 1, 1]], ['氣滯', [1, 3.5, 1, 1, 1]], ['氣陷', [1, 1, 0.3, 1, 1]], ['氣逆', [1, 1, 1, 1, -0.6]]].forEach(function (q, i) {
      var b = btn(q[0], i); b.addEventListener('click', function () { var v = q[1]; st.S = v[0]; st.R = v[1]; st.C = v[2]; st.D = v[3]; st.dir = v[4]; ['S', 'R', 'C', 'D', 'dir'].forEach(function (k) { root.querySelector('input[data-k=' + k + ']').value = st[k]; }); mark(bb, i); us.forEach(function (f) { f(); }); }); bb.appendChild(b); }); mark(bb, 0);
    us.push(slider(root, '來源（脾胃、肺、腎生成氣的能力）', 0.1, 2, 0.05, 1, f2, 'S', function (v) { st.S = v; draw(); }));
    us.push(slider(root, '通道阻力（經絡是否通暢）', 0.3, 5, 0.05, 1, f2, 'R', function (v) { st.R = v; draw(); }));
    us.push(slider(root, '儲存與固攝（能不能「留得住」）', 0.1, 2, 0.05, 1, f2, 'C', function (v) { st.C = v; draw(); }));
    us.push(slider(root, '需求（活動、勞累）', 0.3, 2, 0.05, 1, f2, 'D', function (v) { st.D = v; draw(); }));
    us.push(slider(root, '方向（+1 順暢；負值＝逆行）', -1, 1, 0.05, 1, f2, 'dir', function (v) { st.dir = v; draw(); }));
    root.appendChild(view); p = info(root);
    function sim() { var P = 0.5, out = [], up = [], dt = 0.05; for (var t = 0; t <= 20; t += dt) { var leak = (1 - Math.min(st.C, 1)) * 0.6 * P, Q = st.dir * P / st.R, use = Math.min(Q > 0 ? Q : 0, st.D);
        P += dt * (st.S * 0.6 - Math.abs(Q) * 0.6 - leak); P = Math.max(P, 0); out.push([t, Math.max(Q, -1.5)]); up.push([t, P]); } return [up, out]; }
    function draw() { var r = sim(), P = r[0][r[0].length - 1][1], Q = r[1][r[1].length - 1][1], sup = Q / st.D, lab;
      if (st.dir < 0) lab = '<b>氣逆</b>：流動方向反了，該降的往上衝（例如胃氣上逆的嘔吐、肺氣上逆的咳喘）。';
      else if (st.R > 2 && P > 0.9) lab = '<b>氣滯</b>：上游「壓力」堆積、下游流量不足——中醫說的「脹、悶、痛」，以及「不通則痛」。';
      else if (st.C < 0.6) lab = '<b>氣陷／不固</b>：留不住，一部分從「漏」出去，下游供應不足（中醫說的下垂、自汗、久瀉）。';
      else if (sup < 0.75) lab = '<b>氣虛</b>：供應跟不上需求——疲倦、無力、少氣懶言，動一下就累。';
      else lab = '<b>平衡</b>：來源、通道、儲存與需求匹配。';
      view.innerHTML = chart(640, 240, [{ d: r[0], c: '#d9822b', n: '上游儲量（類比「壓力」）', w: 2.4, dash: '6 4' }, { d: r[1], c: '#3a6ea5', n: '流量（類比「氣行」）', w: 2.4 }], { x0: 0, x1: 20, y0: -1, y1: 2.5, xl: '時間（任意單位）', hl: [{ y: st.D, c: '#4a9a5e', n: '需求' }] });
      p.innerHTML = lab + '<br>穩態流量約為需求的 <b>' + Math.round(Math.max(sup, 0) * 100) + '%</b>。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">⚠ 這是借用工程上「源—流—匯」與「壓力／流量／阻力」關係（類似電路或管路）所做的<b>類比模型</b>，用來整理中醫氣虛、氣滯、氣陷、氣逆四種概念的邏輯差異。它不是對人體的物理描述，也不能用來判斷自己的體質。</span>'; }
    us.forEach(function (f) { f(); });
  }

  /* ---------- 呼吸節拍器 ---------- */
  function initBreath(root, cfg) {
    head(root, cfg.q); var ins = cfg.i || 4, ex = cfg.e || 6, run = false, t0 = 0, raf = 0, view = el('div'), p, bb = bar(root);
    var b1 = btn('▶ 開始', 'go'); bb.appendChild(b1);
    var u1 = slider(root, '吸氣秒數', 2, 6, 0.5, ins, function (v) { return v + ' 秒'; }, 'i', function (v) { ins = v; tell(); });
    var u2 = slider(root, '吐氣秒數', 3, 9, 0.5, ex, function (v) { return v + ' 秒'; }, 'e', function (v) { ex = v; tell(); });
    root.appendChild(view); p = info(root);
    function frame(ts) { if (!run) return; var c = ins + ex, t = ((ts - t0) / 1000) % c, phase = t < ins, k = phase ? t / ins : 1 - (t - ins) / ex, r = 40 + 70 * (0.5 - 0.5 * Math.cos(Math.PI * k));
      view.innerHTML = svgw('0 0 640 260', '<circle cx="320" cy="130" r="' + n1(r) + '" fill="#3a6ea5" fill-opacity="0.25" stroke="#3a6ea5" stroke-width="2"/>' + tx(320, 136, phase ? '吸氣' : '吐氣', 18, '#3a6ea5') + tx(320, 250, '剩 ' + Math.ceil(phase ? ins - t : c - t) + ' 秒', 11, 'var(--text-muted)'));
      raf = requestAnimationFrame(frame); }
    function still() { view.innerHTML = svgw('0 0 640 260', '<circle cx="320" cy="130" r="60" fill="#3a6ea5" fill-opacity="0.15" stroke="#3a6ea5" stroke-width="2"/>' + tx(320, 136, '按「開始」', 15, '#3a6ea5')); }
    b1.addEventListener('click', function () { run = !run; b1.textContent = run ? '■ 停止' : '▶ 開始'; if (run) { t0 = performance.now(); raf = requestAnimationFrame(frame); } else { cancelAnimationFrame(raf); still(); } });
    function tell() { var bpm = 60 / (ins + ex); p.innerHTML = '每分鐘約 <b>' + f1(bpm) + '</b> 次呼吸（一般安靜時約 12～20 次）。吐氣比吸氣長，有助於放鬆。' +
      '<br>練習時：用鼻子吸氣、肚子自然鼓起；嘴巴或鼻子慢慢吐氣、肚子收回。<b>不要憋氣、不要用力</b>，覺得頭暈或胸悶就停下來恢復自然呼吸。每次 3～5 分鐘即可。'; }
    u1(); u2(); still();
  }

  function initAll() { document.querySelectorAll('.qi-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ ziwu: initZiwu, yw: initYW, qiji: initQiji, ring: initRing, model: initModel, breath: initBreath })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def qiw(cfg, maxw=700):
    return wdg("qi-w", cfg, maxw)


qilesson = make_lesson(u"☯", QI_NOTE, QILIB, "qi-w")

TCM = u'<a href="../chinese-medicine/index.html">〈中醫完整知識課程〉</a>'
