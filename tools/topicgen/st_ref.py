# -*- coding: utf-8 -*-
"""股票的本質:兩個參考頁——名詞速查表、互動複利與成本計算機。"""
from st_common import LS, NOTE

_TERMS = [
    [u"股票", u"公司的一小塊所有權;台股 1000 股為一張", LS(1)],
    [u"IPO", u"公司第一次公開發行股票募資", LS(2)],
    [u"股利", u"公司把獲利分給股東;分現金股利與股票股利", LS(3)],
    [u"除權息", u"發股利時股價依股利金額向下調整", LS(41)],
    [u"填息", u"除息後股價漲回除息前的價格", LS(41)],
    [u"營收/毛利/淨利", u"損益表由上往下:收入、扣成本、扣費用與稅", LS(7)],
    [u"EPS", u"每股盈餘=稅後淨利 ÷ 股數", LS(8)],
    [u"本益比 P/E", u"股價 ÷ EPS;股價是獲利的幾倍", LS(8)],
    [u"股價淨值比 P/B", u"股價 ÷ 每股淨值;看股價是帳面家當的幾倍", LS(15)],
    [u"殖利率", u"每年現金股利 ÷ 股價", LS(15)],
    [u"負債比", u"總負債 ÷ 總資產", LS(9)],
    [u"自由現金流", u"營業現金流-資本支出;公司真正能自由運用的錢", LS(10)],
    [u"ROE", u"股東權益報酬率=稅後淨利 ÷ 股東權益", LS(11)],
    [u"護城河", u"讓競爭者難以搶走賺錢能力的優勢", LS(13)],
    [u"價值陷阱", u"看似便宜,其實是公司正在走下坡", LS(15)],
    [u"現金流折現 DCF", u"把未來現金流折回今天加總,得到內在價值", LS(16)],
    [u"安全邊際", u"價值與買價之間的緩衝", LS(17)],
    [u"T+2 交割", u"成交後第二個營業日扣款、股票入帳", LS(18)],
    [u"報酬指數", u"把股利再投入計算的指數", LS(19)],
    [u"空頭市場", u"一般指從高點下跌約 20% 以上", LS(20)],
    [u"效率市場", u"股價已反映可取得的資訊,難以持續打敗", LS(22)],
    [u"處分效應", u"賺的急著賣、賠的死抱著", LS(28)],
    [u"融資/維持率", u"向券商借錢買股;維持率過低會被追繳、斷頭", LS(27)],
    [u"風險溢酬", u"承擔較高風險所要求的額外報酬", LS(31)],
    [u"複利/72 法則", u"利滾利;72 ÷ 年報酬率 ≈ 翻倍年數", LS(32)],
    [u"系統性風險", u"整個市場的風險,無法靠分散消除", LS(33)],
    [u"指數化投資", u"買進整個市場,取得市場報酬", LS(36)],
    [u"定期定額", u"固定時間投入固定金額", LS(37)],
    [u"再平衡", u"把資產比例調回目標", LS(38)],
    [u"ETF", u"在交易所買賣、通常追蹤指數的基金", LS(44)],
    [u"費用率", u"基金每年從資產中扣除的費用比例", LS(44)],
    [u"折溢價", u"ETF 市價和淨值的差距", LS(44)],
    [u"倖存者偏差", u"只看到存活下來的,高估整體表現", LS(43)],
]

_CHEAT_BODY = [
    ("p", u"這一頁把課程裡的關鍵名詞整理成一張表,方便隨時查閱。想親手試試時間與成本的威力,"
          u"可以到<a href=\"compound-calculator.html\">互動複利與成本計算機</a>。"),
    ("h", u"1. 關鍵名詞速查"),
    ("t", [u"名詞", u"白話解釋", u"課程"], _TERMS),
    ("h", u"2. 三個最該記住的重點"),
    ("ol", [u"<strong>股票是公司的一部分</strong>:長期報酬來自公司獲利,短期價格常被情緒左右(" + LS(5) + u")。",
            u"<strong>賠錢多半來自成本與行為</strong>:追高殺低、頻繁交易、槓桿,比選錯股票更傷(" + LS(23) + u")。",
            u"<strong>簡單、分散、低成本、長期</strong>:再加上事先寫好的計畫(" + LS(48) + u")。"]),
    ("h", u"3. 破解常見迷思"),
    ("t", [u"迷思", u"正解", u"課程"],
     [[u"「本益比低就是便宜」", u"可能是獲利即將下滑的循環股", LS(14)],
      [u"「領股利就是賺到」", u"除權息時股價扣掉,要看總報酬", LS(41)],
      [u"「高殖利率很安全」", u"可能是股價暴跌造成的假象", LS(15)],
      [u"「定期定額一定賺」", u"標的長期向下,越買越賠", LS(37)],
      [u"「多交易多賺錢」", u"成本與錯誤會一起累積", LS(25)],
      [u"「融資可以賺更快」", u"也會讓你在低點被迫出場", LS(27)]]),
    ("raw", u'<p style="color:var(--text-muted);font-size:0.9em">📈 %s</p>' % NOTE),
]

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"股票名詞速查表",
    "h1": u"股票名詞速查表",
    "icon": u"📇",
    "description": u"EPS、本益比、殖利率、ROE、安全邊際、再平衡、費用率… 一頁看懂本課關鍵名詞,加上重點與常見迷思",
    "body": _CHEAT_BODY,
}

# ---------- 互動複利與成本計算機 ----------

_CALC_HTML = u"""<div class="content-figure" style="text-align:left">
  <p style="margin:0 0 12px">拉動下面的滑桿,看<strong>時間、報酬率和費用</strong>如何影響最後的金額。
  這是<strong>教學用的簡化模型</strong>:假設每年報酬固定,實際市場每年漲跌不一,也沒有計入稅與通膨。</p>
  <div style="display:grid;grid-template-columns:1fr;gap:14px;max-width:520px">
    <label>一開始投入:<b id="cc-p-v"></b>
      <input type="range" id="cc-p" min="0" max="300" step="5" value="0" style="width:100%"></label>
    <label>每月投入:<b id="cc-m-v"></b>
      <input type="range" id="cc-m" min="0" max="30000" step="1000" value="5000" style="width:100%"></label>
    <label>假設年報酬率(扣費用前):<b id="cc-r-v"></b>
      <input type="range" id="cc-r" min="0" max="12" step="0.5" value="6" style="width:100%"></label>
    <label>每年費用率:<b id="cc-f-v"></b>
      <input type="range" id="cc-f" min="0" max="3" step="0.1" value="1" style="width:100%"></label>
    <label>投資年數:<b id="cc-y-v"></b>
      <input type="range" id="cc-y" min="1" max="40" step="1" value="30" style="width:100%"></label>
  </div>
  <div id="cc-chart" style="margin-top:16px"></div>
  <div id="cc-out" style="margin-top:10px;line-height:1.9"></div>
</div>
<script>
(function () {
  function v(id) { return parseFloat(document.getElementById('cc-' + id).value); }
  function wan(x) { return (x / 10000).toFixed(x >= 1000000 ? 0 : 1) + ' 萬'; }
  function run(rate) {
    var bal = v('p') * 10000, m = v('m'), yrs = v('y');
    var rm = Math.pow(1 + rate, 1 / 12) - 1;
    var pts = [bal];
    for (var k = 1; k <= yrs * 12; k++) {
      bal = bal * (1 + rm) + m;
      if (k % 12 === 0) pts.push(bal);
    }
    return pts;
  }
  function draw() {
    var r = v('r') / 100, f = v('f') / 100, yrs = v('y');
    document.getElementById('cc-p-v').textContent = v('p') + ' 萬';
    document.getElementById('cc-m-v').textContent = v('m').toLocaleString() + ' 元';
    document.getElementById('cc-r-v').textContent = v('r').toFixed(1) + '%';
    document.getElementById('cc-f-v').textContent = v('f').toFixed(1) + '%';
    document.getElementById('cc-y-v').textContent = yrs + ' 年';
    var gross = run(r), net = run(r - f), paid = [];
    for (var i = 0; i <= yrs; i++) paid.push(v('p') * 10000 + v('m') * 12 * i);
    var top = Math.max(gross[yrs], paid[yrs], 1);
    var W = 520, H = 230, L = 58, B = 26, T = 12, Rr = 12;
    var pw = W - L - Rr, ph = H - T - B;
    function sx(i) { return L + (yrs === 0 ? 0 : i / yrs * pw); }
    function sy(x) { return T + ph - x / top * ph; }
    function path(a) { return 'M' + a.map(function (x, i) { return sx(i).toFixed(1) + ' ' + sy(x).toFixed(1); }).join(' L'); }
    var grid = '';
    for (var g = 0; g <= 4; g++) {
      var val = top * g / 4;
      grid += '<line x1="' + L + '" y1="' + sy(val) + '" x2="' + (W - Rr) + '" y2="' + sy(val) + '" stroke="var(--border)" stroke-width="0.6"/>';
      grid += '<text x="' + (L - 6) + '" y="' + (sy(val) + 3) + '" text-anchor="end" font-size="9" fill="var(--text-muted)">' + Math.round(val / 10000) + '萬</text>';
    }
    var svg = '<svg viewBox="0 0 ' + W + ' ' + H + '" style="width:100%;max-width:520px;border:1px solid var(--border);border-radius:8px;background:var(--surface)">' + grid +
      '<path d="' + path(paid) + '" fill="none" stroke="#8a8f98" stroke-width="2" stroke-dasharray="5 4"/>' +
      '<path d="' + path(gross) + '" fill="none" stroke="#5aa469" stroke-width="2.5"/>' +
      '<path d="' + path(net) + '" fill="none" stroke="#e0605a" stroke-width="2.5"/>' +
      '<text x="' + L + '" y="' + (H - 7) + '" font-size="9" fill="var(--text-muted)">現在</text>' +
      '<text x="' + (W - Rr) + '" y="' + (H - 7) + '" text-anchor="end" font-size="9" fill="var(--text-muted)">' + yrs + ' 年後</text>' +
      '</svg>';
    document.getElementById('cc-chart').innerHTML = svg;
    var lost = gross[yrs] - net[yrs];
    document.getElementById('cc-out').innerHTML =
      '<span style="color:#8a8f98">▬ 自己投入的本金:<b>' + wan(paid[yrs]) + '</b></span><br>' +
      '<span style="color:#5aa469">▬ 沒有費用時:<b>' + wan(gross[yrs]) + '</b></span><br>' +
      '<span style="color:#e0605a">▬ 扣掉 ' + v('f').toFixed(1) + '% 年費用後:<b>' + wan(net[yrs]) + '</b></span><br>' +
      '費用總共讓你少了約 <b>' + wan(lost) + '</b>' +
      (gross[yrs] > 0 ? '(約 ' + (lost / gross[yrs] * 100).toFixed(0) + '%)' : '') + '。';
  }
  ['p', 'm', 'r', 'f', 'y'].forEach(function (id) { document.getElementById('cc-' + id).addEventListener('input', draw); });
  draw();
})();
</script>"""

CALCULATOR = {
    "file": "compound-calculator.html",
    "title": u"互動複利與成本計算機",
    "h1": u"互動複利與成本計算機:時間與費用的威力",
    "icon": u"🧮",
    "description": u"拉動投入金額、報酬率、費用率與年數,看複利如何累積、費用又會在長期吃掉多少",
    "body": [
        ("p", u"這個簡化的教學模型,讓你親手體會兩件事:<strong>時間</strong>如何讓複利越滾越大(" + LS(32) + u"),"
              u"以及看似很小的<strong>費用率</strong>,長期會吃掉多少(" + LS(45) + u")。"),
        ("raw", _CALC_HTML),
        ("h", u"幾個值得試的情境"),
        ("ul", [u"<strong>只改年數</strong>:把 20 年拉到 30 年、40 年,看最後十年多出多少——複利的後段加速(" + LS(32) + u")。",
                u"<strong>只改費用率</strong>:從 0.2% 拉到 1.5%,看 30 年後差多少(" + LS(42) + u")。",
                u"<strong>晚十年開始</strong>:把年數減少 10 年,但每月投入加倍,看能不能追上(" + LS(32) + u")。",
                u"<strong>報酬率調低</strong>:試試 3%~4% 的保守假設,檢查你的計畫在較差情況下是否仍可接受(" + LS(35) + u")。"]),
        ("p", u"提醒:真實市場<strong>每年報酬都不同</strong>,可能連續虧損好幾年;本工具使用固定報酬率,只用來建立直覺,"
              u"<strong>不是報酬預測</strong>,也不構成投資建議。"),
        ("raw", u'<p style="color:var(--text-muted);font-size:0.9em">📈 %s</p>' % NOTE),
    ],
}

REFERENCES = [CHEATSHEET, CALCULATOR]
