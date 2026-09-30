# -*- coding: utf-8 -*-
"""道教入門:三個參考頁——名詞速查、台灣常見神明速查(可篩選)、《道德經》精選章節。"""
import json
from tao_common import LS, NOTE
from tao_gods import GODS, TAGS
from tao_ddj import DDJ

_NOTE_RAW = ("raw", u'<p style="color:var(--text-muted);font-size:0.9em">☯️ %s</p>' % NOTE)

_TERMS = [
    [u"道", u"萬物的本源與運行規律", LS(1)],
    [u"道家/道教/民間信仰", u"哲學/宗教/地方信仰實踐,相關但不相同", LS(2)],
    [u"黃老之學", u"漢初以清靜無為治國的思想", LS(4)],
    [u"天師道(五斗米道)", u"張道陵所創,道教正式成立的標誌", LS(5)],
    [u"無為", u"不妄為、不強求,順應本性", LS(8)],
    [u"上善若水", u"最高的善像水,利萬物而不爭", LS(9)],
    [u"反者道之動", u"相反相成,物極必反", LS(10)],
    [u"逍遙", u"無待的心靈自由", LS(14)],
    [u"齊物", u"是非彼此相對,萬物與我為一", LS(15)],
    [u"三清", u"元始天尊、靈寶天尊、道德天尊", LS(18)],
    [u"先天神/後天神", u"與天地同生的神/由人而成的神", LS(19)],
    [u"陰陽五行", u"木火土金水相生相剋的宇宙框架", LS(20)],
    [u"精氣神", u"道教所說的生命三寶", LS(21)],
    [u"外丹/內丹", u"燒煉丹藥/以身為爐修煉精氣神", LS(22)],
    [u"承負", u"先人的善惡由後人承受", LS(23)],
    [u"功過格", u"記錄善惡點數的修身簿", LS(23)],
    [u"齋醮", u"清淨身心與設壇祭神的儀式", LS(24)],
    [u"科儀", u"道教儀式的程序", LS(24)],
    [u"高功", u"主持科儀的道士", LS(24)],
    [u"道藏", u"道教典籍總集,三洞四輔", LS(25)],
    [u"善書", u"勸人為善的書,如《太上感應篇》", LS(26)],
    [u"正一派/全真派", u"火居、符籙科儀/出家、內丹戒律", LS(34)],
    [u"主祀/配祀", u"廟的主神/其他供奉的神明", LS(37)],
    [u"天公爐", u"廟門口朝天的香爐,祭拜玉皇大帝", LS(37)],
    [u"三元", u"上元、中元、下元,三官大帝誕辰", LS(38)],
    [u"做牙/尾牙", u"初二、十六拜土地公;十二月十六為尾牙", LS(41)],
    [u"代天巡狩", u"王爺奉命巡視人間、驅除瘟疫", LS(42)],
    [u"分靈/進香", u"從祖廟分出香火/回祖廟維繫香火", LS(46)],
    [u"火居道士", u"可結婚、住家中的道士", LS(47)],
    [u"聖筊/笑筊/陰筊", u"擲筊的三種結果", LS(49)],
    [u"建醮", u"大型祈福儀式,如慶成醮、平安醮、王醮", LS(50)],
    [u"安太歲", u"犯太歲之年向太歲星君祈求平安", LS(51)],
    [u"鸞堂/扶鸞", u"以乩筆傳達神明訓示的信仰傳統", LS(52)],
]

CHEATSHEET = {
    "file": "cheatsheet.html",
    "title": u"道教名詞速查表",
    "h1": u"道教名詞速查表",
    "icon": u"📇",
    "description": u"無為、三清、內丹、齋醮、承負、分靈、擲筊、安太歲… 一頁查完本課的關鍵名詞",
    "body": [
        ("p", u"這一頁整理課程中的關鍵名詞。神明的資料請見<a href=\"deities.html\">台灣常見神明速查</a>,"
              u"老子原文請見<a href=\"daodejing.html\">《道德經》精選章節</a>。"),
        ("h", u"1. 關鍵名詞"),
        ("t", [u"名詞", u"簡要說明", u"課程"], _TERMS),
        ("h", u"2. 三個最該記住的重點"),
        ("ol", [u"<strong>道家、道教、民間信仰</strong>相關但不相同:哲學、宗教、地方信仰實踐(" + LS(2) + u")。",
                u"<strong>無為不是不作為</strong>:是不妄為、順應本性(" + LS(8) + u")。",
                u"<strong>台灣廟宇是三教交融的</strong>:一座廟常同時供奉佛、道與民間神明(" + LS(52) + u")。"]),
        _NOTE_RAW,
    ],
}

# ---------- 神明速查(可篩選) ----------

_GDATA = json.dumps([dict(g) for g in GODS], ensure_ascii=False).replace("</", "<\\/")
_TDATA = json.dumps(TAGS, ensure_ascii=False)

_GODS_HTML = u"""<div class="content-figure" style="text-align:left">
  <p style="margin:0 0 10px">點選想祈求的事,下方只顯示相關的神明;再點一次或按「全部」可取消。</p>
  <div id="gd-tags" style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px"></div>
  <div id="gd-count" style="color:var(--text-muted);font-size:0.9em;margin-bottom:8px"></div>
  <div id="gd-list" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px"></div>
</div>
<script>
(function () {
  var G = __GODS__, TAGS = __TAGS__, cur = null;
  var tagBox = document.getElementById('gd-tags');
  function btn(label, on) {
    return '<button data-t="' + label + '" style="padding:5px 12px;border-radius:16px;cursor:pointer;font-size:0.92em;border:1px solid ' +
      (on ? 'var(--accent);background:var(--accent);color:#fff' : 'var(--border);background:var(--surface);color:var(--text)') + '">' + label + '</button>';
  }
  function render() {
    tagBox.innerHTML = btn('全部', cur === null) + TAGS.map(function (t) { return btn(t, cur === t); }).join('');
    var list = G.filter(function (g) { return cur === null || g.tags.indexOf(cur) !== -1; });
    document.getElementById('gd-count').textContent = (cur ? '「' + cur + '」相關的神明:' : '全部神明:') + list.length + ' 位';
    document.getElementById('gd-list').innerHTML = list.map(function (g) {
      return '<div style="border:1px solid var(--border);border-radius:10px;padding:12px 14px;background:var(--surface);line-height:1.7">' +
        '<div style="font-weight:bold;font-size:1.05em">' + g.name + '</div>' +
        '<div style="color:var(--text-muted);font-size:0.88em">' + g.alias + '</div>' +
        '<div style="margin-top:6px"><b>職司:</b>' + g.role + '</div>' +
        '<div><b>誕辰:</b>' + g.bday + '</div>' +
        '<div><b>代表廟宇:</b>' + g.temples + '</div>' +
        '<div style="margin-top:6px;font-size:0.88em">' + g.tags.map(function (t) {
          return '<span style="display:inline-block;margin:2px 4px 0 0;padding:1px 8px;border-radius:10px;border:1px solid var(--border)">' + t + '</span>';
        }).join('') + '</div>' +
        '<div style="margin-top:6px;font-size:0.9em"><a href="lesson-' + (g.lesson + '').padStart(2, '0') + '.html">→ 第 ' + g.lesson + ' 課</a></div>' +
        '</div>';
    }).join('');
  }
  tagBox.addEventListener('click', function (e) {
    var b = e.target.closest('[data-t]');
    if (!b) return;
    var t = b.getAttribute('data-t');
    cur = (t === '全部' || t === cur) ? null : t;
    render();
  });
  render();
})();
</script>""".replace("__GODS__", _GDATA).replace("__TAGS__", _TDATA)

DEITIES = {
    "file": "deities.html",
    "title": u"台灣常見神明速查",
    "h1": u"台灣常見神明速查",
    "icon": u"🏮",
    "description": u"媽祖、關公、土地公、城隍、保生大帝、文昌、月老…可依「求學、求財、姻緣、健康」等篩選,查職司、誕辰與代表廟宇",
    "body": [
        ("p", u"這裡整理了台灣廟宇中常見的 %d 位神明。可以依想祈求的事篩選,每張卡片都連到對應課程。"
              u"神明的整體架構請見" % len(GODS) + LS(37) + u"。"),
        ("raw", _GODS_HTML),
        ("h", u"完整列表"),
        ("t", [u"神明", u"別稱", u"主要職司", u"誕辰(農曆)", u"代表廟宇(舉例)"],
         [[g["name"], g["alias"], g["role"], g["bday"], g["temples"]] for g in GODS]),
        ("p", u"提醒:誕辰依台灣通行說法,各地、各廟可能不同;代表廟宇僅為舉例,不代表排名。"
              u"篩選分類是為了方便查詢的概略歸類,各地信眾的祈求內容其實更為多元。"),
        _NOTE_RAW,
    ],
}

# ---------- 《道德經》精選 ----------

_DDJ_ROWS = []
for n, t, text, plain, les, part in DDJ:
    _DDJ_ROWS.append(("h", u"第 %d 章｜%s%s" % (n, t, u"(節錄)" if part else u"")))
    _DDJ_ROWS.append(("raw", u'<blockquote style="font-size:1.08em;line-height:1.9;border-left:4px solid var(--accent);'
                             u'padding:8px 16px;margin:10px 0;background:var(--surface)">%s</blockquote>' % text))
    _DDJ_ROWS.append(("p", u"<strong>白話:</strong>" + plain + u"(相關課程:" + LS(les) + u")"))

DDJPAGE = {
    "file": "daodejing.html",
    "title": u"《道德經》精選章節",
    "h1": u"《道德經》精選章節",
    "icon": u"📜",
    "description": u"《道德經》十多個最常被引用的章節,原文、白話對照,並連到對應課程",
    "body": [
        ("p", u"以下選錄《道德經》中最常被引用的 %d 個章節,原文採<strong>通行本(王弼本)</strong>,附白話與相關課程。"
              u"各版本(帛書本、郭店楚簡本等)的用字與章序有差異(" % len(DDJ) + LS(6) + u");白話為幫助理解的概略翻譯,歷代註解說法很多。"),
        ("t", [u"章", u"標題", u"名句"],
         [[u"%d" % d[0], d[1], d[2][:18] + (u"……" if len(d[2]) > 18 else u"")] for d in DDJ]),
    ] + _DDJ_ROWS + [_NOTE_RAW],
}

REFERENCES = [CHEATSHEET, DEITIES, DDJPAGE]
