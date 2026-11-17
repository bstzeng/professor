# -*- coding: utf-8 -*-
"""〈神經科學：大腦如何運作〉（brn_）共用：課程包裝與 BRNLIB 互動元件（class="brn-w"）。

  brain   大腦地圖：點選腦區（外側面）與深部結構，看功能說明
  ap      動作電位：霍奇金—赫胥黎模型，刺激強度、短脈衝或持續電流、河豚毒素
  rf      感受野：視網膜神經節細胞的中心—周邊，與初級視覺皮質簡單細胞的方向選擇性
  rpe     獎勵預測誤差：時序差分學習模擬多巴胺神經元的反應
  memory  遺忘曲線與間隔複習：不同複習排程的記憶保留率
"""
from cc_common import make_lesson, wdg, LS, M, D
from qt_common import BASEJS

BRN_NOTE = u"本課程為科普與教育用途，不能取代醫療建議；互動模擬為教學用的簡化模型。"


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def bw(cfg, maxw=680):
    return wdg("brn-w", cfg, maxw)


BRNLIB = r"""
(function () {
  if (window.__brnLib) return; window.__brnLib = 1;
""" + BASEJS + r"""
  var BL = '#3a6ea5', OR = '#d9822b', RD = '#d0564f', GN = '#4a9a5e', GY = '#9aa3ad', PU = '#8a5bb5';
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div', 'margin:4px 0'); root.appendChild(b); return b; }
  function poly(p) { return p.map(function (q) { return q[0] + ',' + q[1]; }).join(' '); }

  var REG = [
    ['pf', '前額葉皮質', '#e8a0a0', [[60, 0], [200, 0], [185, 175], [60, 210]], '計畫、決策、自我控制、工作記憶、社會行為。是人類大腦中最晚成熟的區域（約 25 歲）。費尼斯・蓋吉的事故（第 29 課）讓人們第一次理解它的功能。'],
    ['fr', '前運動區', '#f0c27a', [[200, 0], [300, 0], [268, 182], [185, 175]], '規劃與準備動作的順序，例如準備伸手拿杯子。'],
    ['m1', '初級運動皮質', '#e88a5a', [[300, 0], [330, 0], [295, 184], [268, 182]], '發出指令控制身體各部位的肌肉。不同的位置對應不同的身體部位（運動小人，第 19 課）。'],
    ['s1', '初級體感覺皮質', '#7fc6a4', [[330, 0], [360, 0], [322, 180], [295, 184]], '接收觸覺、溫度、痛覺與身體位置的訊息，也有一個「感覺小人」的對應圖（第 17 課）。'],
    ['pa', '頂葉', '#9cc3e6', [[360, 0], [480, 0], [470, 150], [390, 172], [322, 180]], '整合感覺、空間感與注意力：東西在哪裡、我的手在哪裡。右側頂葉受損可能造成「半側忽略」：忽略左半邊的世界。'],
    ['oc', '枕葉（視覺皮質）', '#b9a3e3', [[480, 0], [620, 0], [620, 320], [470, 240], [470, 150]], '處理視覺。初級視覺皮質（V1）在最後端，之後的區域分別處理形狀、顏色、運動（第 14 課）。'],
    ['te', '顳葉', '#f2d38a', [[60, 210], [185, 175], [295, 184], [390, 172], [470, 150], [470, 240], [420, 300], [60, 320]], '聽覺（初級聽覺皮質在上緣）、語言理解、辨識物體與臉孔。內側藏著海馬迴與杏仁核。']];
  var SPOT = [['br', '布洛卡區', [210, 168, 26, 18], '語言的產生。1861 年布洛卡發現，這裡受損的病人能理解語言，卻幾乎說不出話（第 3 課）。通常在左腦。'],
    ['we', '韋尼克區', [425, 182, 28, 18], '語言的理解。這裡受損的病人能流利地說話，但內容沒有意義，也聽不懂別人的話。通常在左腦。']];
  var DEEP = [['hc', '海馬迴', [380, 205, 45, 12], '形成新的長期記憶，以及空間導航（位置細胞）。H.M. 失去了兩側的海馬迴後，再也無法記住新的事情（第 25、27 課）。'],
    ['am', '杏仁核', [318, 200, 14, 12], '情緒，特別是恐懼。快速地評估危險，觸發戰或逃的反應（第 28 課）。'],
    ['th', '視丘', [330, 135, 26, 18], '感覺訊息的「中繼站」：除了嗅覺，所有的感覺都經過這裡才到大腦皮質。'],
    ['hy', '下視丘', [298, 172, 16, 10], '調節體溫、飢餓、口渴、睡眠與荷爾蒙，維持身體的恆定。'],
    ['bg', '基底核', [275, 120, 40, 26], '選擇與啟動動作、習慣的形成。帕金森氏症與這裡的多巴胺不足有關（第 21 課）。'],
    ['cc', '胼胝體', [330, 92, 110, 18], '連接左右大腦半球的兩億多條神經纖維。切斷它，會產生「裂腦人」（第 33 課）。']];
  function initBrain(root, cfg) {
    head(root, cfg.q); var P = { k: 'pf' }, view = el('div'), inf;
    var b = bar(root); b.innerHTML = '<span style="font-size:0.88em;color:var(--text-muted)">深部結構（從外面看不到）：</span>'; DEEP.forEach(function (d) { var x = btn(d[1], d[0]); x.onclick = function () { P.k = d[0]; draw(); }; b.appendChild(x); });
    root.appendChild(view); inf = info(root);
    function draw() { var g = '<defs><clipPath id="nbc"><ellipse cx="320" cy="150" rx="238" ry="128"/></clipPath></defs>';
      g += '<ellipse cx="445" cy="272" rx="82" ry="40" fill="' + (P.k === 'cb' ? '#f7b267' : '#d9c2a5') + '" stroke="#8a7a66" data-k="cb" style="cursor:pointer"/>' + tx(470, 285, '小腦', 11, '#5a4a36');
      g += '<path d="M360 245 L402 245 L398 335 L366 335 Z" fill="' + (P.k === 'bs' ? '#f7b267' : '#cbb79c') + '" stroke="#8a7a66" data-k="bs" style="cursor:pointer"/>' + tx(382, 320, '腦幹', 10.5, '#5a4a36');
      g += '<g clip-path="url(#nbc)">'; REG.forEach(function (r) { g += '<polygon points="' + poly(r[3]) + '" fill="' + r[2] + '" opacity="' + (P.k === r[0] ? 1 : 0.62) + '" stroke="#fff" stroke-width="1.5" data-k="' + r[0] + '" style="cursor:pointer"/>'; }); g += '</g>';
      g += '<ellipse cx="320" cy="150" rx="238" ry="128" fill="none" stroke="#7a6a5a" stroke-width="2"/>';
      SPOT.forEach(function (s) { var e = s[2]; g += '<ellipse cx="' + e[0] + '" cy="' + e[1] + '" rx="' + e[2] + '" ry="' + e[3] + '" fill="' + (P.k === s[0] ? RD : 'rgba(208,86,79,0.35)') + '" stroke="' + RD + '" data-k="' + s[0] + '" style="cursor:pointer"/>'; });
      DEEP.forEach(function (d) { if (P.k !== d[0]) return; var e = d[2]; g += '<ellipse cx="' + e[0] + '" cy="' + e[1] + '" rx="' + e[2] + '" ry="' + e[3] + '" fill="rgba(58,110,165,0.45)" stroke="' + BL + '" stroke-width="2" stroke-dasharray="5 3"/>'; });
      [['前額葉', 120, 90], ['額葉', 240, 70], ['頂葉', 420, 70], ['枕葉', 520, 150], ['顳葉', 300, 235]].forEach(function (t) { g += tx(t[1], t[2], t[0], 12, '#333'); });
      g += tx(60, 330, '← 前方（臉）', 10, 'var(--text-muted)', 'start');
      view.innerHTML = svgw('0 0 640 340', g);
      view.querySelectorAll('[data-k]').forEach(function (e) { e.addEventListener('click', function () { P.k = e.getAttribute('data-k'); draw(); }); });
      var all = REG.map(function (r) { return [r[0], r[1], r[4]]; }).concat(SPOT.map(function (s) { return [s[0], s[1], s[3]]; }), DEEP.map(function (d) { return [d[0], d[1], d[3] + '（虛線是它大約的位置，實際在大腦深處。）']; }),
        [['cb', '小腦', '協調動作、平衡與時機；也參與學習動作技能。只佔大腦體積的約 10%，卻有全腦約 80% 的神經元（第 20 課）。'], ['bs', '腦幹', '呼吸、心跳、血壓、意識清醒等生命功能；連接大腦與脊髓。']]);
      var it = all.filter(function (a) { return a[0] === P.k; })[0]; inf.innerHTML = '<b>' + it[1] + '</b>：' + it[2] + '<br><span style="font-size:0.9em;color:var(--text-muted)">點選左側大腦外側面的區域，或上方的按鈕。圖為示意，區域的邊界是簡化的。</span>'; }
    draw();
  }

  function initAP(root, cfg) {
    head(root, cfg.q); var P = { I: 10, mode: 0, ttx: 0 }, view = el('div'), cv = el('div'), inf;
    var b = bar(root); [['短脈衝（1 毫秒）', 0], ['持續電流', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.mode = o[1]; mark(b, o[1]); run(); }; b.appendChild(x); }); mark(b, 0);
    var tb = btn('加入河豚毒素（阻斷鈉通道）'); tb.onclick = function () { P.ttx ^= 1; tb.style.fontWeight = P.ttx ? 'bold' : 'normal'; tb.style.background = P.ttx ? 'var(--accent-soft)' : 'var(--surface)'; run(); }; b.appendChild(tb);
    var u = slider(root, '刺激電流強度（µA/cm²）', 0, 40, 0.5, P.I, function (x) { return x; }, null, function (x) { P.I = x; run(); });
    root.appendChild(view); root.appendChild(cv); inf = info(root);
    function ex(x) { return Math.abs(x) < 1e-6 ? 1 : x / (1 - Math.exp(-x)); }
    function run() { var V = -65, dt = 0.01, gNa = P.ttx ? 0 : 120, gK = 36, gL = 0.3, ENa = 50, EK = -77, EL = -54.387;
      function am(V) { return ex((V + 40) / 10); } function bm(V) { return 4 * Math.exp(-(V + 65) / 18); } function ah(V) { return 0.07 * Math.exp(-(V + 65) / 20); } function bh(V) { return 1 / (1 + Math.exp(-(V + 35) / 10)); }
      function an(V) { return 0.1 * ex((V + 55) / 10); } function bn(V) { return 0.125 * Math.exp(-(V + 65) / 80); }
      var m = am(V) / (am(V) + bm(V)), h = ah(V) / (ah(V) + bh(V)), n = an(V) / (an(V) + bn(V)), dv = [], dna = [], dk = [], spikes = 0, up = false, vmax = -100;
      for (var i = 0; i < 6000; i++) { var t = i * dt, I = (P.mode === 0 ? (t >= 5 && t < 6) : (t >= 5 && t < 55)) ? P.I : 0;
        var INa = gNa * m * m * m * h * (V - ENa), IK = gK * n * n * n * n * (V - EK), IL = gL * (V - EL);
        V += dt * (I - INa - IK - IL); m += dt * (am(V) * (1 - m) - bm(V) * m); h += dt * (ah(V) * (1 - h) - bh(V) * h); n += dt * (an(V) * (1 - n) - bn(V) * n);
        if (!up && V > 0) { spikes++; up = true; } if (V < -30) up = false; vmax = Math.max(vmax, V);
        if (i % 10 === 0) { dv.push([t, V]); dna.push([t, gNa * m * m * m * h]); dk.push([t, gK * n * n * n * n]); } }
      view.innerHTML = chart(640, 220, [{ d: dv, c: BL, n: '膜電位（mV）', w: 2 }], { x0: 0, x1: 60, y0: -90, y1: 60, xl: '時間（毫秒）', hl: [{ y: -65, c: GY, n: '靜止電位' }], vl: [{ x: 5, c: OR, n: '刺激開始' }] });
      cv.innerHTML = chart(640, 150, [{ d: dna, c: RD, n: '鈉離子通道的導通', w: 1.6 }, { d: dk, c: GN, n: '鉀離子通道的導通', w: 1.6 }], { x0: 0, x1: 60, y0: 0, y1: 45, xl: '時間（毫秒）' });
      inf.innerHTML = (P.ttx ? '<b>河豚毒素</b>阻斷了電壓門控的鈉通道：不論刺激多強，都<b>不會</b>產生動作電位，只有被動的電位變化。這就是河豚毒素致命的原因——神經無法傳遞訊號，呼吸肌麻痺。' :
        spikes ? '產生了 <b>' + spikes + '</b> 個動作電位，最高約 ' + Math.round(vmax) + ' mV。鈉通道先迅速打開（紅線，鈉離子湧入，電位上升），接著關閉；鉀通道較慢地打開（綠線，鉀離子流出），讓電位回落，甚至短暫低於靜止電位。' :
        '刺激<b>沒有超過閾值</b>：電位稍微上升後就回到靜止電位，沒有產生動作電位。') +
        '<br>試試看：慢慢調整強度——動作電位是<b>全有或全無</b>的：要嘛完整地發生，要嘛完全不發生，大小幾乎一樣。在「持續電流」下，刺激越強，發射的<b>頻率</b>越高：神經用頻率編碼強度。' +
        '<br><span style="font-size:0.9em;color:var(--text-muted)">霍奇金—赫胥黎模型（1952，烏賊巨大軸突）。本模型的靜止電位約 −65 mV。</span>'; }
    u();
  }

  function initRF(root, cfg) {
    head(root, cfg.q); var P = { m: 0, d: 4, th: 45 }, view = el('div'), cv = el('div'), inf;
    var b = bar(root); [['視網膜：中心—周邊（ON 中心）', 0], ['視覺皮質：簡單細胞', 1]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.m = o[1]; mark(b, o[1]); sh(); }; b.appendChild(x); }); mark(b, 0);
    var s1 = el('div'), s2 = el('div'); root.appendChild(s1); root.appendChild(s2);
    var u1 = slider(s1, '光點的直徑', 0, 20, 0.5, P.d, function (x) { return x; }, null, function (x) { P.d = x; draw(); });
    var u2 = slider(s2, '光棒的角度', 0, 180, 1, P.th, function (x) { return x + '°'; }, null, function (x) { P.th = x; draw(); });
    root.appendChild(view); root.appendChild(cv); inf = info(root);
    function resp(d) { var r = d / 2; return Math.max(0, 10 + 80 * ((1 - Math.exp(-r * r / 2)) - 0.9 * (1 - Math.exp(-r * r / 18)))); }
    function ori(t) { var dd = Math.abs(((t - 45) % 180 + 180) % 180); dd = Math.min(dd, 180 - dd); return 5 + 75 * Math.exp(-dd * dd / (2 * 18 * 18)); }
    function sh() { s1.style.display = P.m ? 'none' : ''; s2.style.display = P.m ? '' : 'none'; draw(); }
    function draw() { var g = '', cx = 320, cy = 120, S = 9;
      if (!P.m) { g += '<circle cx="' + cx + '" cy="' + cy + '" r="' + 6 * S + '" fill="rgba(208,86,79,0.18)" stroke="' + RD + '" stroke-dasharray="4 3"/>' + '<circle cx="' + cx + '" cy="' + cy + '" r="' + 2 * S + '" fill="rgba(74,154,94,0.3)" stroke="' + GN + '"/>' +
          '<circle cx="' + cx + '" cy="' + cy + '" r="' + n1(P.d / 2 * S) + '" fill="#ffe680" opacity="0.75"/>' + tx(cx, cy + 6 * S + 18, '綠：ON 中心　紅：OFF 周邊　黃：光點', 10, 'var(--text-muted)');
        var r = resp(P.d), d = []; for (var x = 0; x <= 20; x += 0.25) d.push([x, resp(x)]);
        cv.innerHTML = chart(640, 170, [{ d: d, c: BL, n: '神經節細胞的發射率（次／秒）', w: 2 }], { x0: 0, x1: 20, y0: 0, y1: 90, xl: '光點的直徑', pts: [{ x: P.d, y: r, c: RD }] });
        inf.innerHTML = '發射率：<b>' + Math.round(r) + '</b> 次／秒（沒有光時約 10）。<br>光點剛好填滿<b>中心</b>時反應最強；再變大，光照到了抑制性的<b>周邊</b>，反應反而減弱。均勻的大面積光線，幾乎不引起反應。<br>視網膜送給大腦的，不是每一點的亮度，而是<b>對比</b>與<b>邊緣</b>——這是 1953 年庫弗勒在貓的視網膜上發現的。'; }
      else { var a = P.th * Math.PI / 180, pa = 45 * Math.PI / 180, hw = 70;
        g += '<g transform="rotate(' + (-45) + ' ' + cx + ' ' + cy + ')"><rect x="' + (cx - 90) + '" y="' + (cy - 30) + '" width="180" height="18" fill="rgba(208,86,79,0.25)" stroke="' + RD + '"/><rect x="' + (cx - 90) + '" y="' + (cy - 9) + '" width="180" height="18" fill="rgba(74,154,94,0.35)" stroke="' + GN + '"/><rect x="' + (cx - 90) + '" y="' + (cy + 12) + '" width="180" height="18" fill="rgba(208,86,79,0.25)" stroke="' + RD + '"/></g>';
        g += ln(cx - hw * Math.cos(a), cy + hw * Math.sin(a), cx + hw * Math.cos(a), cy - hw * Math.sin(a), '#e6b800', 9, 'stroke-linecap="round" opacity="0.85"') + tx(cx, cy + 115, '綠：ON 區　紅：OFF 區　黃：光棒', 10, 'var(--text-muted)');
        var r2 = ori(P.th), d2 = []; for (var t = 0; t <= 180; t += 2) d2.push([t, ori(t)]);
        cv.innerHTML = chart(640, 170, [{ d: d2, c: BL, n: '簡單細胞的發射率（次／秒）', w: 2 }], { x0: 0, x1: 180, y0: 0, y1: 90, xl: '光棒的角度（度）', pts: [{ x: P.th, y: r2, c: RD }] });
        inf.innerHTML = '發射率：<b>' + Math.round(r2) + '</b> 次／秒。這個細胞「偏好」<b>45°</b> 的光棒——光棒剛好落在它狹長的 ON 區時反應最強，角度偏離越多，反應越弱。<br>1959 年，休伯爾與威澤爾在貓的初級視覺皮質中發現了這種<b>方向選擇性</b>：大腦把影像拆解成許多小小的「線段」，再一層層組合成形狀與物體。他們因此獲得 1981 年諾貝爾生理醫學獎。'; }
      view.innerHTML = svgw('0 0 640 240', g); }
    u1(); u2(); sh();
  }

  function initRPE(root, cfg) {
    head(root, cfg.q); var P = { n: 1, om: 0 }, view = el('div'), inf;
    var u = slider(root, '學習的次數（第幾次嘗試）', 1, 60, 1, P.n, function (x) { return '第 ' + x + ' 次'; }, null, function (x) { P.n = x; draw(); });
    var b = bar(root), ob = btn('這一次不給獎勵'); ob.onclick = function () { P.om ^= 1; ob.style.fontWeight = P.om ? 'bold' : 'normal'; ob.style.background = P.om ? 'var(--accent-soft)' : 'var(--surface)'; draw(); }; b.appendChild(ob);
    root.appendChild(view); inf = info(root);
    var T = 24, C = 4, R = 16, al = 0.25;
    function trial(Vv, omit, learn) { var d = []; for (var t = 0; t < T; t++) d.push(0); d[C] = Vv[0];
      for (var k = 0; C + k + 1 < T; k++) { var r = (C + k === R && !omit) ? 1 : 0, dl = r + Vv[k + 1] - Vv[k]; d[C + k] += 0; d[C + k + 1] = dl; if (learn) Vv[k] += al * dl; } return d; }
    function draw() { var Vv = []; for (var k = 0; k < T; k++) Vv.push(0);
      for (var i = 1; i < P.n; i++) trial(Vv, false, true);
      var d = trial(Vv.slice(), P.om, false), ser = [], pts = []; for (var t = 0; t < T; t++) ser.push([t, d[t]]);
      view.innerHTML = chart(640, 230, [{ d: ser, c: BL, n: '多巴胺神經元的反應（預測誤差）', w: 2.4 }], { x0: 0, x1: T - 1, y0: -1.1, y1: 1.2, xl: '時間', vl: [{ x: C, c: OR, n: '提示（燈亮）' }, { x: R + 1, c: GN, n: P.om ? '（沒有獎勵）' : '獎勵（果汁）' }], hl: [{ y: 0, c: GY, n: '' }] });
      var dc = d[C], dr = d[R + 1];
      inf.innerHTML = '一隻猴子先看到燈亮，過一段時間後得到果汁。第 ' + P.n + ' 次：提示時的反應 ' + f2(dc) + '，獎勵時的反應 ' + f2(dr) + '。' +
        (P.om ? '<br>預期的獎勵<b>沒有出現</b>：在原本該有獎勵的時刻，多巴胺神經元的活動<b>低於</b>基準——「比預期的差」。' :
          P.n <= 3 ? '<br>一開始，猴子不知道燈代表什麼。果汁是<b>意外的</b>，多巴胺神經元在獎勵出現時強烈反應。' : dr < 0.15 ? '<br>學會之後，反應<b>移到了提示</b>出現的時刻；獎勵本身已經被預期到了，不再引起反應。' : '<br>學習進行中：反應逐漸從獎勵的時刻，往提示的時刻移動。') +
        '<br>多巴胺編碼的不是「快樂」，而是<b>獎勵預測誤差</b>：實際 − 預期。這與強化學習中的時序差分誤差 δ = r + V(下一刻) − V(現在) 完全一致（舒爾茨、戴揚、蒙塔古，1997）。'; }
    u();
  }

  var SCH = [['不複習', []], ['集中複習（第 0 天連讀 3 次）', [0.04, 0.08]], ['間隔複習（第 1、3、7、14 天）', [1, 3, 7, 14]], ['考前抱佛腳（第 27、28 天）', [27, 28]]];
  function initMemory(root, cfg) {
    head(root, cfg.q); var P = { s: 2 }, view = el('div'), inf;
    var b = bar(root); SCH.forEach(function (o, i) { var x = btn(o[0], i); x.onclick = function () { P.s = i; mark(b, i); draw(); }; b.appendChild(x); }); mark(b, P.s);
    root.appendChild(view); inf = info(root);
    function sim(rv) { var S = 1, last = 0, d = [], k = 0, out = {}; for (var t = 0; t <= 60.001; t += 0.05) { if (k < rv.length && t >= rv[k] - 1e-9) { var R = Math.exp(-(t - last) / S); S = S * (1 + 4 * (1 - R)) + 0.1; last = t; k++; } var R2 = Math.exp(-(t - last) / S); d.push([t, R2 * 100]); if (Math.abs(t - 30) < 0.025) out.a = R2; if (Math.abs(t - 60) < 0.025) out.b = R2; } out.d = d; return out; }
    function draw() { var cur = sim(SCH[P.s][1]), base = sim([]);
      view.innerHTML = chart(640, 240, [{ d: base.d, c: GY, n: '不複習', w: 1.4, dash: '4,3' }, { d: cur.d, c: BL, n: SCH[P.s][0], w: 2.2 }], { x0: 0, x1: 60, y0: 0, y1: 105, xl: '天數', yl: '記得的比例（%）', vl: [{ x: 30, c: RD, n: '考試（第 30 天）' }] });
      inf.innerHTML = '第 30 天還記得約 <b>' + Math.round(cur.a * 100) + '%</b>，第 60 天約 <b>' + Math.round(cur.b * 100) + '%</b>。' +
        '<br>1885 年，艾賓浩斯用無意義的音節測試自己，畫出了<b>遺忘曲線</b>：學過的東西在最初幾天忘得最快。' +
        '<br>模型的關鍵假設：<b>快要忘記時複習</b>，記憶的穩定度增加得最多（「必要的困難」）。所以連續讀三次的效果很小；而間隔越來越長的複習，讓記憶越來越牢固——這是<b>間隔效應</b>，心理學中最可靠的發現之一。抱佛腳能撐過考試，但很快就會忘記。<br><span style="font-size:0.9em;color:var(--text-muted)">（簡化的模型，數字僅供示意。）</span>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.brn-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ brain: initBrain, ap: initAP, rf: initRF, rpe: initRPE, memory: initMemory })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""

lesson = make_lesson(u"🧠", BRN_NOTE, BRNLIB, "brn-w")

BRAIN = bw({"t": "brain", "q": u"大腦地圖：點選一個區域"})
AP = bw({"t": "ap", "q": u"動作電位：霍奇金—赫胥黎模型"})
RF = bw({"t": "rf", "q": u"感受野：視覺神經元「看」什麼"})
RPE = bw({"t": "rpe", "q": u"多巴胺與獎勵預測誤差"})
MEMORY = bw({"t": "memory", "q": u"遺忘曲線與間隔複習"})
