# -*- coding: utf-8 -*-
"""塔羅：兩個參考頁——78 張牌速查表、互動抽牌器。"""
import json
from dv_common import LS, SUITS
from ta_data import MAJORS, MINORS, RANKS, SUIT_ORDER, all_cards

_MAJ_ROWS = [[u'<span id="M%d">%d %s</span>' % (n, n, name), en, astro, up, rev]
             for n, name, en, up, rev, astro in MAJORS]


def _suit_rows(s):
    return [[u'<span id="%s%d">%s%s</span>' % (s, i + 1, s, RANKS[i]), up, rev]
            for i, (up, rev) in enumerate(MINORS[s])]


_body = [
    ("p", u"本表整理 78 張牌的傳統牌義關鍵字（以偉特-史密斯牌為準），供快速查閱。"
          u"牌義會依牌陣位置與上下文而變化（" + LS(25) + u"），請把關鍵字當作起點，而不是標準答案。"
          u"也可以到<a href=\"tarot-reader.html\">互動抽牌器</a>實際抽牌練習。"),
    ("h", u"1. 大阿爾克那（22 張）"),
    ("t", [u"牌", u"英文", u"對應（黃金黎明）", u"正位", u"逆位"], _MAJ_ROWS),
]
for j, s in enumerate(SUIT_ORDER):
    el, col, kw = SUITS[s]
    _body.append(("h", u"%d. %s（%s元素：%s）" % (j + 2, s, el, kw)))
    _body.append(("t", [u"牌", u"正位", u"逆位"], _suit_rows(s)))
_body += [
    ("h", u"6. 數字與宮廷牌速記"),
    ("t", [u"數字／角色", u"主題"],
     [[u"王牌", u"開始、種子"], [u"2", u"平衡、選擇"], [u"3", u"成長、合作"], [u"4", u"穩定、停頓"],
      [u"5", u"衝突、失去"], [u"6", u"和諧、恢復"], [u"7", u"評估、考驗"], [u"8", u"行動、精進"],
      [u"9", u"接近完成"], [u"10", u"完成、負擔"], [u"侍者", u"學習、訊息"], [u"騎士", u"行動、追求"],
      [u"皇后", u"內在的掌握"], [u"國王", u"外在的掌握"]]),
]

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"78 張牌速查表",
    "h1": u"塔羅 78 張牌速查表",
    "icon": u"🃏",
    "description": u"大阿爾克那與四種花色小牌的正位、逆位關鍵字，以及數字與宮廷牌速記",
    "body": _body,
}

# ---------- 互動抽牌器 ----------

SPREADS = {
    "one": [u"今天的提醒"],
    "three": [u"過去", u"現在", u"未來"],
    "sit": [u"狀況", u"阻礙", u"建議"],
    "choice": [u"現況", u"選項 A", u"選項 B", u"A 的發展", u"B 的發展"],
    "celtic": [u"1 現況", u"2 挑戰", u"3 意識／目標", u"4 潛意識／根基", u"5 過去", u"6 近未來",
               u"7 自己", u"8 環境", u"9 希望與恐懼", u"10 結果"],
}
SPREAD_NAMES = [("one", u"單張"), ("three", u"三張：過去現在未來"), ("sit", u"三張：狀況阻礙建議"),
                ("choice", u"二選一（五張）"), ("celtic", u"凱爾特十字（十張）")]

_COLORS = {u"大阿爾克那": "#a9802e"}
_COLORS.update(dict((s, SUITS[s][1]) for s in SUIT_ORDER))
_CARDS = [[cid, name, kind, up, rev, _COLORS[kind]] for cid, name, kind, up, rev, note in all_cards()]

_BTN = (u'style="font:inherit;padding:8px 16px;margin:4px 8px 4px 0;border-radius:8px;cursor:pointer;'
        u'border:1px solid var(--border);background:var(--surface);color:var(--text)"')

_OPTIONS = u"".join(u'<option value="%s">%s</option>' % (k, v) for k, v in SPREAD_NAMES)

_READER_HTML = u"""<div class="content-figure" style="text-align:left">
  <div style="display:flex;flex-wrap:wrap;gap:8px;align-items:center">
    <label>牌陣：<select id="tr-spread" style="font:inherit;padding:6px;border-radius:6px;border:1px solid var(--border);background:var(--surface);color:var(--text)">%(opts)s</select></label>
    <label style="display:inline-flex;gap:6px;align-items:center"><input type="checkbox" id="tr-rev"> 使用逆位</label>
  </div>
  <div style="margin-top:8px">
    <button type="button" id="tr-draw" %(btn)s>洗牌並抽牌</button>
    <button type="button" id="tr-next" %(btn)s>翻開下一張</button>
    <button type="button" id="tr-all" %(btn)s>全部翻開</button>
  </div>
  <div id="tr-cards" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px;margin-top:12px"></div>
  <p id="tr-summary" style="margin:12px 0 0;color:var(--text-muted)">選擇牌陣後按「洗牌並抽牌」。</p>
</div>
<script>
(function () {
  var CARDS = %(cards)s;
  var SPREADS = %(spreads)s;
  var hand = [], shown = 0;
  var box = document.getElementById('tr-cards');
  var sum = document.getElementById('tr-summary');
  function rnd(n) {
    try { var a = new Uint32Array(1); window.crypto.getRandomValues(a); return a[0] %% n; }
    catch (e) { return Math.floor(Math.random() * n); }
  }
  function shuffle() {
    var d = CARDS.slice();
    for (var i = d.length - 1; i > 0; i--) { var j = rnd(i + 1), t = d[i]; d[i] = d[j]; d[j] = t; }
    return d;
  }
  function esc(s) { return String(s).replace(/[&<>]/g, function (c) { return {'&': '&amp;', '<': '&lt;', '>': '&gt;'}[c]; }); }
  function render() {
    box.innerHTML = '';
    hand.forEach(function (h, i) {
      var div = document.createElement('div');
      div.style.cssText = 'border:1.5px solid ' + (i < shown ? h.c[5] : 'var(--border)') + ';border-radius:10px;padding:10px;background:var(--surface);min-height:120px';
      var head = '<div style="font-size:0.85em;color:var(--text-muted)">' + esc(h.pos) + '</div>';
      if (i < shown) {
        var kw = h.rev ? h.c[4] : h.c[3];
        div.innerHTML = head +
          '<div style="font-weight:bold;color:' + h.c[5] + ';margin:4px 0">' + esc(h.c[1]) + (h.rev ? '<span style="color:#e0605a">（逆位）</span>' : '') + '</div>' +
          '<div style="font-size:0.8em;color:var(--text-muted)">' + esc(h.c[2]) + '</div>' +
          '<div style="font-size:0.9em;margin-top:6px">' + esc(kw) + '</div>' +
          '<div style="margin-top:6px;font-size:0.8em"><a href="cheatsheet.html#' + encodeURIComponent(h.c[0]) + '">查看牌義</a></div>';
      } else {
        div.innerHTML = head + '<div style="margin-top:24px;text-align:center;font-size:1.8em;color:var(--text-muted)">🂠</div>';
      }
      box.appendChild(div);
    });
    if (hand.length && shown === hand.length) summarize();
    else if (hand.length) sum.textContent = '已翻開 ' + shown + '／' + hand.length + ' 張。先讀位置，再讀牌。';
  }
  function summarize() {
    var major = 0, suits = {};
    hand.forEach(function (h) { if (h.c[2] === '大阿爾克那') major++; else suits[h.c[2]] = (suits[h.c[2]] || 0) + 1; });
    var parts = Object.keys(suits).map(function (k) { return k + ' ' + suits[k]; });
    var avg = (hand.length * 22 / 78).toFixed(1);
    sum.textContent = '全部翻開：大阿爾克那 ' + major + ' 張（平均約 ' + avg + ' 張）' + (parts.length ? '；' + parts.join('、') : '') +
      '。接著看牌與牌的組合，並把它們串成一段故事。';
  }
  document.getElementById('tr-draw').addEventListener('click', function () {
    var pos = SPREADS[document.getElementById('tr-spread').value];
    var useRev = document.getElementById('tr-rev').checked;
    var deck = shuffle();
    hand = pos.map(function (p, i) { return {pos: p, c: deck[i], rev: useRev && rnd(2) === 1}; });
    shown = 0; render();
  });
  document.getElementById('tr-next').addEventListener('click', function () { if (shown < hand.length) { shown++; render(); } });
  document.getElementById('tr-all').addEventListener('click', function () { shown = hand.length; render(); });
})();
</script>""" % {"btn": _BTN, "opts": _OPTIONS,
               "cards": json.dumps(_CARDS, ensure_ascii=False),
               "spreads": json.dumps(SPREADS, ensure_ascii=False)}

READER = {
    "file": "tarot-reader.html",
    "title": u"互動抽牌器",
    "h1": u"互動抽牌器：選牌陣、洗牌、翻牌",
    "icon": u"🔮",
    "description": u"選擇單張、三張、二選一或凱爾特十字，洗牌後逐張翻開，顯示位置、牌名、正逆位與關鍵字",
    "body": [
        ("p", u"先寫下一個具體、開放的問題（" + LS(20) + u"），選擇牌陣，再按「洗牌並抽牌」。"
              u"建議一張一張翻開，先讀位置、再讀牌（" + LS(25) + u"）。"),
        ("raw", _READER_HTML),
        ("h", u"使用提醒"),
        ("ul", [u"洗牌使用瀏覽器的亂數，每張牌被抽到的機率相同；勾選「使用逆位」時，每張牌有一半機率為逆位（" + LS(22) + u"）。",
                u"畫面上的關鍵字只是起點，請結合位置、組合與整體統計來解讀（" + LS(26) + u"、" + LS(27) + u"）。",
                u"同一個問題不要一再重抽。",
                u"抽牌的結果適合當作反思的起點，不能取代專業意見（" + LS(35) + u"）。"]),
    ],
}

REFERENCES = [CHEATSHEET, READER]
