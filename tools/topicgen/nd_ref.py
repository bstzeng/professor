# -*- coding: utf-8 -*-
"""國債課程:兩個參考頁——關鍵名詞速查表、互動債務/GDP 計算機。"""
from nd_common import LS, NOTE

_TERMS = [
    [u"赤字 Deficit", u"某一年「支出 > 收入」的差額(流量)", LS(2)],
    [u"債務 Debt", u"歷年赤字累積的總量(存量),「36 兆」指這個", LS(2)],
    [u"盈餘 Surplus", u"某一年「收入 > 支出」,與赤字相反", LS(2)],
    [u"GDP", u"一國一年的經濟總產出,像國家的「年收入」", LS(5)],
    [u"債務/GDP", u"看國債負擔最重要的指標,美國約 120%+", LS(5)],
    [u"公債 Treasury", u"政府的借據:T-Bill、T-Note、T-Bond", LS(6)],
    [u"殖利率 Yield", u"買債券實際能拿到的年報酬率;與價格反向", LS(8)],
    [u"公眾持有債務", u"欠外部(民眾、外國、Fed)的部分,最受重視", LS(9)],
    [u"強制性支出", u"法律規定要付的(福利、醫療、利息),最難砍", LS(12)],
    [u"可裁量支出", u"每年國會決定的(國防、教育…),占比較小", LS(12)],
    [u"利息支出", u"為了付利息而花的錢,會滾雪球、近年暴增", LS(14)],
    [u"結構性赤字", u"制度上支出天生傾向大於收入,非偶發", LS(15)],
    [u"債務上限", u"國會給的借錢額度;政治角力,控不了債務", LS(20)],
    [u"聯準會 Fed", u"美國央行,管利率與貨幣(貨幣政策)", LS(21)],
    [u"財政部", u"政府錢包,收稅發債(財政政策)", LS(21)],
    [u"量化寬鬆 QE", u"Fed 買債放錢、壓低利率;≠印錢還債", LS(22)],
    [u"債務貨幣化", u"央行一直買債替政府融資,易致通膨", LS(23)],
    [u"避風港", u"危機時資金湧入的最安全資產,如美債", LS(26)],
    [u"美元霸權", u"美元作為世界貿易/儲備/結算貨幣的地位", LS(27)],
    [u"無風險利率", u"美債殖利率,全球資產定價的基準", LS(28)],
    [u"過度特權", u"美國能用本幣、低利大量借錢的特殊能力", LS(29)],
    [u"主權違約", u"國家還不出債;借外幣的國家風險高", LS(31)],
    [u"利息排擠", u"利息吃掉預算,擠掉其他支出", LS(32)],
    [u"r vs. g", u"利率 vs. 成長率;g>r 則債務可持續", LS(33)],
    [u"信用評等", u"評等機構給債券的信用分數,最高 AAA", LS(34)],
]

_CHEAT_BODY = [
    ("p", u"這一頁把課程裡的關鍵名詞整理成一張表,方便隨時查閱。想親手玩玩「利率、成長率、赤字如何影響債務走勢」,"
          u"可以到<a href=\"debt-calculator.html\">互動債務計算機</a>。"),
    ("h", u"1. 關鍵名詞速查"),
    ("t", [u"名詞", u"白話解釋", u"課程"], _TERMS),
    ("h", u"2. 三個最該記住的重點"),
    ("ol", [u"<strong>赤字 ≠ 債務</strong>:赤字是今年的差額,債務是累積的總量。只要還有赤字,債務就繼續增加(" + LS(2) + u")。",
            u"<strong>看比例,不看金額</strong>:債務/GDP 才反映真正的負擔;「36 兆」這個絕對數字會誤導(" + LS(5) + u")。",
            u"<strong>r vs. g 是關鍵</strong>:成長率高於利率(g>r),債務就能被稀釋;反之則失控(" + LS(33) + u")。"]),
    ("h", u"3. 破解五個常見迷思"),
    ("t", [u"迷思", u"正解", u"課程"],
     [[u"「美國快破產了」", u"能發本幣的國家幾乎不會被迫違約", LS(31)],
      [u"「都是某黨害的」", u"減稅與增支都加債,是跨黨派困境", LS(18)],
      [u"「外國一拋售就完蛋」", u"外國僅占兩成多,最大債主是美國自己人", LS(10)],
      [u"「破 100% 就崩」", u"沒有絕對門檻,日本 250% 也沒崩", LS(30)],
      [u"「印錢還債就好」", u"會引發通膨甚至惡性通膨", LS(23)]]),
    ("raw", u'<p style="color:var(--text-muted);font-size:0.9em">📊 %s</p>' % NOTE),
]

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"國債關鍵名詞速查表",
    "h1": u"國債關鍵名詞速查表",
    "icon": u"💵",
    "description": u"赤字、債務、殖利率、QE、債務上限、r vs. g… 一頁看懂國債的關鍵名詞,加上三個重點與五個迷思",
    "body": _CHEAT_BODY,
}

# ---------- 互動債務/GDP 計算機 ----------

_CALC_HTML = u"""<div class="content-figure" style="text-align:left">
  <p style="margin:0 0 12px">拉動下面的滑桿,看未來 30 年<strong>債務佔 GDP</strong>的走勢會怎麼變。
  這是一個<strong>簡化的教學模型</strong>,用來體會「r vs. g」和赤字的威力,不是精確預測。</p>
  <div style="display:grid;grid-template-columns:1fr;gap:14px;max-width:520px">
    <label>名目經濟成長率 g:<b id="dc-g-v">4.0%</b>
      <input type="range" id="dc-g" min="0" max="8" step="0.1" value="4" style="width:100%"></label>
    <label>公債平均利率 r:<b id="dc-r-v">3.0%</b>
      <input type="range" id="dc-r" min="0" max="8" step="0.1" value="3" style="width:100%"></label>
    <label>基本赤字(不含利息)佔 GDP:<b id="dc-d-v">3.0%</b>
      <input type="range" id="dc-d" min="-3" max="8" step="0.1" value="3" style="width:100%"></label>
    <label>起始債務/GDP:<b id="dc-s-v">120%</b>
      <input type="range" id="dc-s" min="40" max="160" step="1" value="120" style="width:100%"></label>
  </div>
  <div id="dc-chart" style="margin-top:16px"></div>
  <p id="dc-msg" style="margin:10px 0 0;font-weight:bold"></p>
</div>
<script>
(function () {
  var ids = ['g', 'r', 'd', 's'];
  function val(id) { return parseFloat(document.getElementById('dc-' + id).value); }
  function project() {
    var g = val('g') / 100, r = val('r') / 100, prim = val('d') / 100, debt = val('s') / 100;
    var pts = [debt];
    for (var yr = 1; yr <= 30; yr++) {
      // 債務/GDP 動態:d_{t+1} = d_t * (1+r)/(1+g) + 基本赤字/GDP
      debt = debt * (1 + r) / (1 + g) + prim;
      if (debt < 0) debt = 0;
      pts.push(debt);
    }
    return pts;
  }
  function draw() {
    document.getElementById('dc-g-v').textContent = val('g').toFixed(1) + '%';
    document.getElementById('dc-r-v').textContent = val('r').toFixed(1) + '%';
    document.getElementById('dc-d-v').textContent = val('d').toFixed(1) + '%';
    document.getElementById('dc-s-v').textContent = val('s').toFixed(0) + '%';
    var pts = project();
    var maxV = Math.max(200, Math.ceil(Math.max.apply(null, pts) * 100 / 50) * 50);
    var W = 520, H = 220, padL = 44, padB = 28, padT = 10, padR = 10;
    var pw = W - padL - padR, ph = H - padT - padB;
    function sx(i) { return padL + i / 30 * pw; }
    function sy(v) { return padT + ph - (v * 100 / maxV) * ph; }
    var path = 'M' + pts.map(function (v, i) { return sx(i).toFixed(1) + ' ' + sy(v).toFixed(1); }).join(' L');
    var grid = '';
    for (var y = 0; y <= maxV; y += 50) {
      grid += '<line x1="' + padL + '" y1="' + sy(y / 100) + '" x2="' + (W - padR) + '" y2="' + sy(y / 100) + '" stroke="var(--border)" stroke-width="0.6"/>';
      grid += '<text x="' + (padL - 6) + '" y="' + (sy(y / 100) + 3) + '" text-anchor="end" font-size="9" fill="var(--text-muted)">' + y + '%</text>';
    }
    var last = pts[pts.length - 1] * 100;
    var col = last > pts[0] * 100 ? '#e0605a' : '#5aa469';
    var svg = '<svg viewBox="0 0 ' + W + ' ' + H + '" style="width:100%;max-width:520px;border:1px solid var(--border);border-radius:8px;background:var(--surface)">' +
      grid +
      '<line x1="' + padL + '" y1="' + (H - padB) + '" x2="' + (W - padR) + '" y2="' + (H - padB) + '" stroke="var(--text-muted)" stroke-width="1"/>' +
      '<text x="' + padL + '" y="' + (H - 6) + '" font-size="9" fill="var(--text-muted)">現在</text>' +
      '<text x="' + (W - padR) + '" y="' + (H - 6) + '" text-anchor="end" font-size="9" fill="var(--text-muted)">30 年後</text>' +
      '<path d="' + path + '" fill="none" stroke="' + col + '" stroke-width="2.5"/>' +
      '</svg>';
    document.getElementById('dc-chart').innerHTML = svg;
    var msg = document.getElementById('dc-msg');
    var gap = val('r') - val('g');
    if (last > pts[0] * 100 + 2) {
      msg.innerHTML = '<span style="color:#e0605a">30 年後債務/GDP 升到約 ' + last.toFixed(0) + '%——走勢往上。</span>' +
        (gap > 0 ? '（利率 r 高於成長 g,債務自我推升）' : '（赤字太大,即使 g>r 也壓不住）');
    } else if (last < pts[0] * 100 - 2) {
      msg.innerHTML = '<span style="color:#5aa469">30 年後債務/GDP 降到約 ' + last.toFixed(0) + '%——走勢往下!</span>（成長與紀律讓債務被稀釋）';
    } else {
      msg.innerHTML = '30 年後債務/GDP 約 ' + last.toFixed(0) + '%——大致穩住。';
    }
  }
  ids.forEach(function (id) { document.getElementById('dc-' + id).addEventListener('input', draw); });
  draw();
})();
</script>"""

CALCULATOR = {
    "file": "debt-calculator.html",
    "title": u"互動債務計算機",
    "h1": u"互動債務計算機:玩玩看 r、g 與赤字的威力",
    "icon": u"🧮",
    "description": u"拉動利率、成長率、赤字的滑桿,看未來 30 年債務佔 GDP 的走勢怎麼變,直觀感受「r vs. g」的關鍵",
    "body": [
        ("p", u"這個簡化的教學模型,讓你親手體會為什麼「利率 vs. 成長率」(" + LS(33) + u")那麼關鍵。"
              u"試試看:把利率 r 調到高於成長率 g,看債務怎麼失控;再把 g 調高,看它怎麼被稀釋。"),
        ("raw", _CALC_HTML),
        ("h", u"幾個值得試的情境"),
        ("ul", [u"<strong>g > r 且赤字小</strong>:債務/GDP 會慢慢下降——這是最健康的組合(" + LS(33) + u")。",
                u"<strong>r > g</strong>:即使基本赤字為零,債務/GDP 也會自我推升(" + LS(24) + u")。",
                u"<strong>赤字很大</strong>:就算 g > r,龐大的赤字仍可能讓債務持續上升(" + LS(15) + u")。",
                u"把 r 從 3% 慢慢拉高,感受「利率一升,走勢就翻轉」——這正是近年的擔憂所在。"]),
        ("p", u"提醒:這是<strong>教學用的簡化模型</strong>(用債務動態方程式 d′＝d×(1+r)/(1+g)＋基本赤字),"
              u"真實世界還有通膨、政策反應、經濟循環等許多因素。它的價值在於<strong>建立直覺</strong>,不是精確預測。"),
        ("raw", u'<p style="color:var(--text-muted);font-size:0.9em">📊 %s</p>' % NOTE),
    ],
}

REFERENCES = [CHEATSHEET, CALCULATOR]
