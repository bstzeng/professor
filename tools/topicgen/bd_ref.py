# -*- coding: utf-8 -*-
"""佛教入門:三個參考頁——名詞速查、互動《心經》逐句讀、《大悲咒》分段對照。"""
import json
from bd_common import LS, NOTE
from bd_heart import HEART
from bd_dabei import LINES, SEGMENTS

_NOTE_RAW = ("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🪷 %s</p>' % NOTE)

_TERMS = [
    [u"佛陀", u"覺悟者;指釋迦牟尼佛", LS(3)],
    [u"三寶", u"佛、法、僧", LS(4)],
    [u"三藏", u"經(佛說)、律(戒律)、論(論述)", LS(5)],
    [u"四聖諦", u"苦、集、滅、道", LS(6)],
    [u"苦(dukkha)", u"不圓滿、不穩定;含苦苦、壞苦、行苦", LS(7)],
    [u"八正道", u"正見、正思惟、正語、正業、正命、正精進、正念、正定", LS(8)],
    [u"戒定慧", u"三學:行為、專注、智慧", LS(8)],
    [u"三法印", u"諸行無常、諸法無我、涅槃寂靜", LS(9)],
    [u"五蘊", u"色、受、想、行、識", LS(10)],
    [u"緣起", u"此有故彼有,此滅故彼滅", LS(11)],
    [u"十二因緣", u"無明、行、識、名色、六入、觸、受、愛、取、有、生、老死", LS(12)],
    [u"業", u"行為;關鍵在意圖(思)", LS(13)],
    [u"六道", u"天、人、阿修羅、畜生、餓鬼、地獄", LS(14)],
    [u"五戒", u"不殺生、不偷盜、不邪淫、不妄語、不飲酒", LS(15)],
    [u"止觀", u"止:安定專注;觀:如實觀察", LS(16)],
    [u"涅槃", u"「吹熄」:貪瞋癡止息的寂靜", LS(17)],
    [u"上座部/南傳", u"斯里蘭卡、東南亞的佛教傳承", LS(20)],
    [u"大乘", u"以菩薩道與成佛為理想", LS(21)],
    [u"菩薩", u"菩提薩埵:追求覺悟的有情", LS(21)],
    [u"六度", u"布施、持戒、忍辱、精進、禪定、般若", LS(22)],
    [u"空", u"緣起故無自性;不是虛無", LS(23)],
    [u"二諦", u"世俗諦與勝義諦", LS(23)],
    [u"唯識", u"八識、阿賴耶識、轉識成智", LS(24)],
    [u"五不翻", u"玄奘提出五種保留原音不意譯的情況", LS(25)],
    [u"淨土", u"念佛求生阿彌陀佛的極樂世界", LS(28)],
    [u"禪宗", u"直指人心,見性成佛;頓悟", LS(29)],
    [u"人間佛教", u"佛法落實於今生與社會", LS(31)],
    [u"般若", u"洞見實相的智慧", LS(35)],
    [u"波羅蜜多", u"到彼岸;圓滿", LS(35)],
    [u"觀自在/觀世音", u"同一位菩薩的兩種譯名", LS(35)],
    [u"阿耨多羅三藐三菩提", u"無上正等正覺", LS(40)],
    [u"陀羅尼", u"總持;較長的咒語", LS(43)],
    [u"娑婆訶(svāhā)", u"咒語常見結尾,意近成就、圓滿", LS(46)],
    [u"青頸(nīlakaṇṭha)", u"「那囉謹墀」;大悲咒的梵文名稱來源", LS(45)],
]

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"佛教名詞速查表",
    "h1": u"佛教名詞速查表",
    "icon": u"📇",
    "description": u"四聖諦、八正道、五蘊、緣起、空、六度、般若、陀羅尼… 一頁查完本課的關鍵名詞",
    "body": [
        ("p", u"這一頁把課程中的關鍵名詞整理成一張表。想逐句讀《心經》,請到"
              u"<a href=\"heart-sutra.html\">互動《心經》逐句讀</a>;想看《大悲咒》全文分段,請到"
              u"<a href=\"great-compassion-mantra.html\">《大悲咒》分段對照</a>。"),
        ("h", u"1. 關鍵名詞"),
        ("t", [u"名詞", u"簡要說明", u"課程"], _TERMS),
        ("h", u"2. 三個最該記住的重點"),
        ("ol", [u"<strong>佛教從「苦」的問題出發</strong>:四聖諦像醫生看病,重點在「苦可以止息、有方法」(" + LS(6) + u")。",
                u"<strong>緣起是核心洞見</strong>:無常、無我、空,都從「一切依條件而生」推出(" + LS(11) + u")。",
                u"<strong>智慧與慈悲並重</strong>:《心經》代表智慧,《大悲咒》代表慈悲,兩者的主角是同一位菩薩(" + LS(50) + u")。"]),
        _NOTE_RAW,
    ],
}

# ---------- 互動《心經》逐句讀 ----------

_DATA = json.dumps([{"t": h[0], "p": h[1], "k": h[2], "n": h[3]} for h in HEART],
                   ensure_ascii=False).replace("</", "<\\/")

_HEART_HTML = u"""<div class="content-figure" style="text-align:left">
  <p style="margin:0 0 10px">點選任一句經文,下方會顯示白話與要點。也可以用「上一句/下一句」依序讀。</p>
  <div id="hs-text" style="line-height:2.3;font-size:1.12em"></div>
  <div style="margin:12px 0;display:flex;gap:10px;align-items:center;flex-wrap:wrap">
    <button id="hs-prev" style="padding:6px 14px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer">← 上一句</button>
    <button id="hs-next" style="padding:6px 14px;border-radius:8px;border:1px solid var(--accent);background:var(--accent);color:#fff;cursor:pointer">下一句 →</button>
    <span id="hs-count" style="color:var(--text-muted);font-size:0.9em"></span>
  </div>
  <div id="hs-detail" style="padding:14px 16px;border:1px solid var(--border);border-radius:10px;background:var(--surface);line-height:1.8"></div>
</div>
<script>
(function () {
  var D = __DATA__;
  var cur = 0;
  var box = document.getElementById('hs-text');
  function render() {
    box.innerHTML = D.map(function (d, i) {
      var on = i === cur;
      return '<span data-i="' + i + '" style="cursor:pointer;padding:2px 3px;border-radius:4px;' +
        (on ? 'background:var(--accent);color:#fff' : 'border-bottom:1px dashed var(--border)') + '">' + d.t + '</span>';
    }).join(' ');
    var d = D[cur];
    document.getElementById('hs-detail').innerHTML =
      '<div style="font-weight:bold;margin-bottom:6px">' + d.t + '</div>' +
      '<div><b>白話:</b>' + d.p + '</div>' +
      '<div style="color:var(--text-muted);margin-top:6px"><b>要點:</b>' + d.k + '</div>' +
      '<div style="margin-top:8px"><a href="lesson-' + (d.n + '').padStart(2, '0') + '.html">→ 看第 ' + d.n + ' 課的完整解說</a></div>';
    document.getElementById('hs-count').textContent = '第 ' + (cur + 1) + ' / ' + D.length + ' 段';
    document.getElementById('hs-prev').disabled = cur === 0;
    document.getElementById('hs-next').disabled = cur === D.length - 1;
  }
  box.addEventListener('click', function (e) {
    var t = e.target.closest('[data-i]');
    if (t) { cur = +t.getAttribute('data-i'); render(); }
  });
  document.getElementById('hs-prev').addEventListener('click', function () { if (cur > 0) { cur--; render(); } });
  document.getElementById('hs-next').addEventListener('click', function () { if (cur + 1 < D.length) { cur++; render(); } });
  render();
})();
</script>""".replace("__DATA__", _DATA)

HEARTPAGE = {
    "file": "heart-sutra.html",
    "title": u"互動《心經》逐句讀",
    "h1": u"互動《心經》逐句讀",
    "icon": u"📜",
    "description": u"《般若波羅蜜多心經》玄奘譯本全文,點選任一句即可看白話與要點,並連到對應課程",
    "body": [
        ("p", u"經文採玄奘譯本(大正藏所收通行文字),全文 260 字,分成九段。"
              u"背景與結構見" + LS(32) + u"~" + LS(35) + u",逐句解說見" + LS(36) + u"~" + LS(41) + u"。"),
        ("raw", _HEART_HTML),
        ("h", u"全文"),
        ("raw", u'<blockquote style="line-height:2;border-left:4px solid var(--accent);padding:8px 16px;background:var(--surface)">'
                u"<strong>般若波羅蜜多心經</strong><br>" + u"".join(h[0] for h in HEART) + u"</blockquote>"),
        ("p", u"提醒:白話與要點是幫助理解的概略說明,各宗派與註解家的詮釋不盡相同;"
              u"「揭諦揭諦」等咒語傳統上不翻譯,白話僅供參考。"),
        _NOTE_RAW,
    ],
}

# ---------- 《大悲咒》分段對照 ----------

_ROWS = []
for a, b, skt, mean in SEGMENTS:
    txt = u"<br>".join(u"%d. %s" % (k, LINES[k - 1]) for k in range(a, b + 1))
    _ROWS.append([u"%d–%d" % (a, b) if a != b else u"%d" % a, txt,
                  u'<span style="font-style:italic">%s</span>' % skt, mean])

MANTRAPAGE = {
    "file": "great-compassion-mantra.html",
    "title": u"《大悲咒》分段對照",
    "h1": u"《大悲咒》分段對照",
    "icon": u"🪷",
    "description": u"《大悲咒》八十四句全文,依段落列出學者的梵文還原擬音與概略大意",
    "body": [
        ("p", u"下表列出《大悲咒》(伽梵達摩譯本,台灣常見的八十四句分法)全文,並依段落附上"
              u"<strong>學者的梵文還原擬音</strong>與<strong>概略大意</strong>。背景說明見" + LS(42) + u"~" + LS(47) + u"。"),
        ("note", u"閱讀前請注意", [("ul", [
            u"漢字依台灣寺院常見誦本,<strong>各地誦本偶有用字與讀音差異</strong>,持誦請以所在寺院或師長的版本為準。",
            u"梵文為<strong>學者的還原擬音</strong>,各家不同;標示「擬音不一」的部分,學界說法分歧較大。",
            u"大意是<strong>分段的概略理解</strong>,不是逐字翻譯。傳統上咒語保留原音、不作翻譯(" + LS(43) + u")。",
            u"84 句的分法與「每句一尊化身」的配圖,是後世形成的讀誦傳統(" + LS(42) + u")。"])]),
        ("h", u"分段對照"),
        ("t", [u"句", u"經文", u"梵文還原(擬音)", u"大意(概略)"], _ROWS),
        ("h", u"全文(不分段)"),
        ("raw", u'<blockquote style="line-height:2.1;border-left:4px solid var(--accent);padding:8px 16px;background:var(--surface)">'
                + u"。".join(LINES) + u"。</blockquote>"),
        _NOTE_RAW,
    ],
}

REFERENCES = [CHEATSHEET, HEARTPAGE, MANTRAPAGE]
