# -*- coding: utf-8 -*-
"""易經：兩個參考頁——六十四卦速查表、互動起卦器。"""
import json
from dv_common import HEX, TRIGRAMS, TRI_ORDER, hex_lines, LINES_TO_NUM, LS
from ic_p3 import fullname


def mini_svg(n, w=26):
    """表格中用的小卦圖（inline SVG）。"""
    ls = hex_lines(n)
    rects = []
    for i, c in enumerate(ls):
        y = (5 - i) * 6
        if c == "1":
            rects.append('<rect x="0" y="%d" width="%d" height="4" fill="currentColor"/>' % (y, w))
        else:
            seg = int(w * 0.42)
            rects.append('<rect x="0" y="%d" width="%d" height="4" fill="currentColor"/>' % (y, seg))
            rects.append('<rect x="%d" y="%d" width="%d" height="4" fill="currentColor"/>' % (w - seg, y, seg))
    return ('<svg width="%d" height="34" viewBox="0 0 %d 34" aria-hidden="true" '
            'style="vertical-align:middle;color:var(--text)">%s</svg>') % (w, w, "".join(rects))


_ROWS = []
for n in range(1, 65):
    name, up, lo, mean = HEX[n - 1]
    _ROWS.append([u'<span id="h%d">%d</span>' % (n, n), mini_svg(n), fullname(n),
                  u"%s%s／%s%s" % (TRIGRAMS[up][1], up, TRIGRAMS[lo][1], lo), mean])

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"六十四卦速查表",
    "h1": u"六十四卦與八卦速查表",
    "icon": u"☯️",
    "description": u"依文王卦序列出六十四卦的卦象、全名、上下卦與一句話卦意，另附八卦對照",
    "body": [
        ("p", u"卦象由下往上讀。「一句話卦意」是本課程的簡要概括，僅供快速查閱；完整的卦辭、爻辭請參考《周易》原文。"
              u"起卦後可從<a href=\"iching-caster.html\">互動起卦器</a>直接連到對應的卦。"),
        ("h", u"1. 八卦"),
        ("t", [u"先天數", u"卦", u"自然", u"德性", u"家人", u"後天方位", u"五行"],
         [[u"%d" % (i + 1), u"%s %s" % (TRIGRAMS[k][1], k), TRIGRAMS[k][2], TRIGRAMS[k][3], TRIGRAMS[k][4], TRIGRAMS[k][5],
           {u"乾": u"金", u"兌": u"金", u"離": u"火", u"震": u"木", u"巽": u"木", u"坎": u"水", u"艮": u"土", u"坤": u"土"}[k]]
          for i, k in enumerate(TRI_ORDER)]),
        ("h", u"2. 六十四卦（文王卦序）"),
        ("t", [u"序", u"卦象", u"卦名", u"上卦／下卦", u"一句話卦意"], _ROWS),
        ("h", u"3. 朱熹依變爻數目的讀法"),
        ("t", [u"變爻數", u"讀什麼"],
         [[u"0", u"本卦卦辭"], [u"1", u"本卦變爻爻辭"], [u"2", u"本卦兩變爻爻辭，以上爻為主"],
          [u"3", u"本卦與之卦卦辭，以本卦為主"], [u"4", u"之卦兩不變爻爻辭，以下爻為主"],
          [u"5", u"之卦不變爻爻辭"], [u"6", u"乾用九、坤用六，其他讀之卦卦辭"]]),
        ("p", u"詳見" + LS(21) + u"。"),
    ],
}

# ---------- 互動起卦器 ----------

_DATA = {
    "l2n": LINES_TO_NUM,
    "hex": dict((n, [HEX[n - 1][0], fullname(n), HEX[n - 1][3]]) for n in range(1, 65)),
}

_BTN = (u'style="font:inherit;padding:8px 16px;margin:4px 8px 4px 0;border-radius:8px;cursor:pointer;'
        u'border:1px solid var(--border);background:var(--surface);color:var(--text)"')

_CASTER_HTML = u"""<div class="content-figure" style="text-align:left">
  <div>
    <button type="button" id="ic-one" %(btn)s>擲一次（一爻）</button>
    <button type="button" id="ic-all" %(btn)s>一次擲完</button>
    <button type="button" id="ic-reset" %(btn)s>重來</button>
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:20px;align-items:flex-start;margin-top:12px">
    <svg id="ic-hex" viewBox="0 0 120 150" width="120" height="150" style="flex:none"></svg>
    <ol id="ic-log" reversed style="margin:0;padding-left:1.6em;min-width:200px;flex:1;font-size:0.95em"></ol>
  </div>
  <div id="ic-result" style="margin-top:12px"></div>
  <p style="margin:10px 0 0;color:var(--text-muted);font-size:0.9em">每次擲三枚銅錢：正面記 3（陽）、反面記 2（陰），三枚相加。6 老陰與 9 老陽為變爻（紅色）。由下往上依序成爻。</p>
</div>
<script>
(function () {
  var D = %(data)s;
  var RULE = ['讀本卦卦辭', '讀本卦變爻的爻辭', '讀本卦兩個變爻的爻辭，以上面那爻為主',
              '讀本卦與之卦的卦辭，以本卦為主', '讀之卦中兩個不變爻的爻辭，以下面那爻為主',
              '讀之卦中唯一不變爻的爻辭', '乾讀用九、坤讀用六；其他卦讀之卦卦辭'];
  var POS = ['初', '二', '三', '四', '五', '上'];
  var NAME = {6: '老陰（變）', 7: '少陽', 8: '少陰', 9: '老陽（變）'};
  var vals = [];
  var svg = document.getElementById('ic-hex');
  var log = document.getElementById('ic-log');
  var res = document.getElementById('ic-result');
  function coin() {
    try {
      var a = new Uint8Array(1); window.crypto.getRandomValues(a); return (a[0] & 1) ? 3 : 2;
    } catch (e) { return Math.random() < 0.5 ? 3 : 2; }
  }
  function draw() {
    var ns = 'http://www.w3.org/2000/svg', h = '';
    for (var i = 0; i < vals.length; i++) {
      var v = vals[i], y = 130 - i * 24, col = (v === 6 || v === 9) ? '#e0605a' : 'currentColor';
      if (v === 7 || v === 9) h += '<rect x="10" y="' + y + '" width="100" height="12" rx="2" fill="' + col + '"/>';
      else h += '<rect x="10" y="' + y + '" width="42" height="12" rx="2" fill="' + col + '"/><rect x="68" y="' + y + '" width="42" height="12" rx="2" fill="' + col + '"/>';
    }
    svg.innerHTML = h;
    svg.style.color = getComputedStyle(document.body).color;
  }
  function link(n) {
    var h = D.hex[n];
    return '<a href="cheatsheet.html#h' + n + '">第 ' + n + ' 卦 ' + h[1] + '</a>（' + h[2] + '）';
  }
  function finish() {
    var ben = '', zhi = '', moving = [];
    for (var i = 0; i < 6; i++) {
      var v = vals[i];
      ben += (v === 7 || v === 9) ? '1' : '0';
      zhi += (v === 7 || v === 8) ? ((v === 7) ? '1' : '0') : ((v === 9) ? '0' : '1');
      if (v === 6 || v === 9) moving.push(POS[i]);
    }
    var b = D.l2n[ben], z = D.l2n[zhi];
    var html = '<p><strong>本卦：</strong>' + link(b) + '</p>';
    if (moving.length) {
      html += '<p><strong>變爻：</strong>' + moving.join('、') + '爻（共 ' + moving.length + ' 個）</p>';
      html += '<p><strong>之卦：</strong>' + link(z) + '</p>';
    } else {
      html += '<p><strong>變爻：</strong>無</p>';
    }
    html += '<p><strong>朱熹讀法：</strong>' + RULE[moving.length] + '</p>';
    res.innerHTML = html;
  }
  function one() {
    if (vals.length >= 6) return;
    var c = [coin(), coin(), coin()], s = c[0] + c[1] + c[2];
    vals.push(s);
    var li = document.createElement('li');
    li.textContent = POS[vals.length - 1] + '爻：' + c.join(' + ') + ' = ' + s + '　' + NAME[s];
    if (s === 6 || s === 9) li.style.color = '#e0605a';
    log.insertBefore(li, log.firstChild);
    draw();
    if (vals.length === 6) finish();
  }
  document.getElementById('ic-one').addEventListener('click', one);
  document.getElementById('ic-all').addEventListener('click', function () { while (vals.length < 6) one(); });
  document.getElementById('ic-reset').addEventListener('click', function () {
    vals = []; log.innerHTML = ''; res.innerHTML = ''; draw();
  });
})();
</script>""" % {"btn": _BTN, "data": json.dumps(_DATA, ensure_ascii=False)}

CASTER = {
    "file": "iching-caster.html",
    "title": u"互動起卦器",
    "h1": u"互動起卦器：三枚銅錢法",
    "icon": u"🪙",
    "description": u"模擬擲三枚銅錢六次，自動畫出本卦、標出變爻、求出之卦，並提示朱熹的讀法",
    "body": [
        ("p", u"這個工具模擬" + LS(16) + u"的三枚銅錢法。先在心中想好一個具體的問題（" + LS(23) + u"），"
              u"再按「擲一次」逐爻起卦，或按「一次擲完」。"),
        ("raw", _CASTER_HTML),
        ("h", u"使用提醒"),
        ("ul", [u"每一爻的結果由瀏覽器的亂數產生，機率與真實的三枚銅錢相同（" + LS(18) + u"）。",
                u"同一件事不要一再重擲（" + LS(23) + u"）。",
                u"得到卦之後，依朱熹的讀法查閱《周易》原文，並參考" + LS(24) + u"與" + LS(25) + u"的解卦流程。",
                u"占卜的結果適合當作反思的起點，不能取代專業意見（" + LS(41) + u"）。"]),
    ],
}

REFERENCES = [CHEATSHEET, CASTER]
