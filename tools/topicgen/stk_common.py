# -*- coding: utf-8 -*-
"""〈星艦迷航記全紀錄〉（stk_）共用：課程包裝與互動元件（nv_common 的 nv-w，加上曲速計算器 stk-w）。"""
from nv_common import *
from cc_common import wdg
from qt_common import BASEJS

lesson = nv_lesson(u"🖖")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


WORKS = nvw({"t": "timeline", "q": u"星艦迷航記的影集與電影年表（點一列看說明；可依類型篩選）：", "yw": 96, "mh": 560,
  "groups": [["t", u"影集", CB], ["f", u"電影", CR], ["x", u"大事", CG]],
  "ev": [ev(u"1966～1969", u"原初系列（TOS）", u"寇克艦長、史巴克與麥考伊。三季 79 集，收視不佳而停播，卻在重播中成為經典。", "t"),
         ev(u"1973～1974", u"動畫系列", u"原班演員配音的動畫版。", "t"),
         ev(u"1976", u"太空梭「企業號」", u"粉絲寫信請願，NASA 的第一架太空梭測試機以「企業號」命名。", "x"),
         ev(u"1979～1991", u"原班人馬電影六部", u"其中 1982 年的第二集（可汗之怒）被公認為最佳。", "f"),
         ev(u"1987～1994", u"銀河飛龍（TNG）", u"畢凱艦長與新的企業號 D。七季，系列最成功的影集之一。", "t"),
         ev(u"1993～1999", u"深太空九號（DS9）", u"一座太空站上的政治、宗教與戰爭。", "t"),
         ev(u"1994～2002", u"TNG 電影四部", u"包括 1996 年的博格人電影《戰鬥巡航》（First Contact）。", "f"),
         ev(u"1995～2001", u"重返地球（Voyager）", u"珍妮薇艦長被拋到七萬光年外的德爾塔象限。", "t"),
         ev(u"2001～2005", u"企業號（Enterprise）", u"聯邦成立之前的前傳。", "t"),
         ev(u"2009～2016", u"亞伯拉罕重啟電影三部", u"「凱爾文時間線」：年輕的寇克與史巴克。", "f"),
         ev(u"2017～2024", u"發現號（Discovery）", u"串流時代的第一部影集。", "t"),
         ev(u"2020～2023", u"畢凱（Picard）", u"年老的畢凱重返；第三季讓 TNG 原班人馬重聚。", "t"),
         ev(u"2020～2024", u"下層艦員（Lower Decks）", u"以小人物為主角的喜劇動畫。", "t"),
         ev(u"2022～", u"奇異新世界（Strange New Worlds）", u"派克艦長的企業號，回歸「每集一個冒險」的形式。第五季將是最終季。", "t"),
         ev(u"2026", u"星艦學院（Starfleet Academy）", u"以星艦學院的學生為主角的新影集，2026 年 1 月開播。", "t")]})

CREW = nvw({"t": "graph", "h": 360, "q": u"兩代企業號的艦橋——點選看說明：",
  "nodes": [node("kirk", u"寇克", 160, 60, CY, u"TOS 艦長。衝動、魅力十足，相信直覺。"),
            node("spock", u"史巴克", 60, 170, CB, u"科學官，地球人與瓦肯人的混血，在理性與感情之間掙扎。"),
            node("mccoy", u"麥考伊", 260, 170, CB, u"醫官「老骨頭」，感情豐富，常與史巴克鬥嘴。"),
            node("scotty", u"史考特", 90, 290, CR, u"輪機長「史考提」。「傳送我上去，史考提」成為流行語（雖然劇中從未說過這句原話）。"),
            node("uhura", u"烏乎拉", 230, 290, CR, u"通訊官。黑人女性擔任艦橋軍官，在 1960 年代意義重大。"),
            node("picard", u"畢凱", 480, 60, CY, u"TNG 艦長。學者氣質、重視外交與原則，「Make it so」。"),
            node("riker", u"萊克", 380, 160, CR, u"大副，魅力型的「第一號」。"),
            node("data", u"Data", 580, 160, CY, u"仿生人，渴望理解人性。"),
            node("worf", u"沃夫", 400, 290, CR, u"第一位在星際艦隊服役的克林貢人。"),
            node("laforge", u"拉弗吉", 560, 290, CY, u"輪機長，盲人，戴著能看見電磁波的護目鏡。")],
  "edges": [["kirk", "spock", u"摯友", CB], ["kirk", "mccoy", u"摯友", CB], ["spock", "mccoy", u"鬥嘴", CB, 1], ["kirk", "scotty", u"", CR], ["kirk", "uhura", u"", CR],
            ["picard", "riker", u"艦長與大副", CR], ["picard", "data", u"導師", CY], ["data", "laforge", u"摯友", CY], ["riker", "worf", u"", CR], ["kirk", "picard", u"兩代艦長", CG, 1]],
  "hint": u"左邊是原初系列（1960 年代），右邊是銀河飛龍（1980～1990 年代）。"})

SPECIES = nvw({"t": "cards", "q": u"星艦迷航記的種族圖鑑（可依陣營篩選或搜尋）：",
  "groups": [["f", u"聯邦成員", CB], ["r", u"對手", CR], ["o", u"其他", CG]],
  "cards": [card(u"瓦肯人", "f", u"以邏輯壓抑強烈的情感。代表人物史巴克。舉手比出「V」字的瓦肯禮，搭配「生生不息，繁榮昌盛」。", u"Vulcan"),
            card(u"地球人", "f", u"聯邦的創始成員之一。2063 年首次曲速飛行後，與瓦肯人第一次接觸。", u"Human"),
            card(u"安多利亞人", "f", u"藍色皮膚、頭上有觸角的戰士種族，聯邦的創始成員之一。", u"Andorian"),
            card(u"貝塔索人", "f", u"擁有心電感應能力。TNG 的心理諮商師迪安娜・特洛伊是半貝塔索人。", u"Betazoid"),
            card(u"克林貢人", "r", u"重視榮譽與戰鬥的戰士民族。從冷戰時代的敵人，到 TNG 時代的盟友。", u"Klingon"),
            card(u"羅慕倫人", "r", u"瓦肯人的分支，多疑、擅長陰謀，使用隱形裝置。", u"Romulan"),
            card(u"博格人", "r", u"機械與生物結合的集合意識，「同化」其他種族。「抵抗是徒勞的」。", u"Borg"),
            card(u"卡達西人", "r", u"佔領巴喬五十年的軍事國家。", u"Cardassian"),
            card(u"自治領", "r", u"伽瑪象限的帝國，由能變形的「創始者」統治。", u"Dominion"),
            card(u"佛倫基人", "o", u"崇尚資本主義的商人種族，有一套〈獲利法則〉。", u"Ferengi"),
            card(u"巴喬人", "o", u"宗教虔誠的民族，經歷了卡達西的佔領。", u"Bajoran"),
            card(u"Q", "o", u"來自「Q 連續體」、全知全能卻愛惡作劇的存在。", u"Q")]})

MAP = nvw({"t": "map", "h": 420, "q": u"銀河系的四個象限（示意圖，不按比例）：",
  "bg": u'<rect x="0" y="0" width="640" height="420" fill="#e6ebf7" rx="8"/>'
        u'<ellipse cx="320" cy="210" rx="290" ry="185" fill="#cfd8f0" opacity="0.9"/><ellipse cx="320" cy="210" rx="180" ry="115" fill="#b8c6ea" opacity="0.8"/><circle cx="320" cy="210" r="22" fill="#e9d79a" opacity="0.8"/>'
        u'<line x1="320" y1="10" x2="320" y2="410" stroke="#7085bf" stroke-dasharray="6 6"/><line x1="20" y1="210" x2="620" y2="210" stroke="#7085bf" stroke-dasharray="6 6"/>'
        u'<text x="160" y="400" font-size="14" fill="#33447a" text-anchor="middle">阿爾法象限</text><text x="480" y="400" font-size="14" fill="#33447a" text-anchor="middle">貝塔象限</text>'
        u'<text x="160" y="30" font-size="14" fill="#33447a" text-anchor="middle">伽瑪象限</text><text x="480" y="30" font-size="14" fill="#33447a" text-anchor="middle">德爾塔象限</text>'
        u'<text x="320" y="245" font-size="10" fill="#7a6420" text-anchor="middle">銀河中心</text>',
  "pts": [pt(318, 330, u"地球（太陽系）", u"聯邦的中心，位在阿爾法與貝塔象限的交界附近。星際艦隊總部在舊金山。", CB, None, "end"),
          pt(380, 320, u"克林貢帝國", u"位在貝塔象限，聯邦的鄰居。", CR, None, "start"),
          pt(420, 280, u"羅慕倫星際帝國", u"貝塔象限，與聯邦之間有一道「中立區」。", CG, None, "start"),
          pt(215, 360, u"卡達西與巴喬", u"阿爾法象限。巴喬附近的蟲洞通往伽瑪象限。", CO, None, "end"),
          pt(150, 120, u"自治領", u"伽瑪象限的帝國，經由巴喬蟲洞與阿爾法象限相連，引發自治領戰爭。", CP, None, "middle"),
          pt(500, 110, u"博格", u"德爾塔象限是博格人的大本營。", CK, None, "middle"),
          pt(540, 160, u"重返地球號的起點", u"航海家號被「看守者」拋到德爾塔象限，距離地球約七萬光年。以航海家號能長時間維持的巡航速度，也要約 75 年才能回家。", CY, None, "end")],
  "hint": u"點選地點看說明。聯邦只佔銀河系的一小部分。"})

STKLIB = r"""
(function () {
  if (window.__stkLib) return; window.__stkLib = 1;
""" + BASEJS + r"""
  var TNG = [[1, 1], [2, 10], [3, 39], [4, 102], [5, 214], [6, 392], [7, 656], [8, 1024], [9, 1516], [9.2, 1649], [9.6, 1909], [9.9, 3053], [9.975, 5000], [9.99, 7912]];
  function tng(w) { for (var i = 1; i < TNG.length; i++) if (w <= TNG[i][0]) { var a = TNG[i - 1], b = TNG[i], t = (w - a[0]) / (b[0] - a[0]); return Math.exp(Math.log(a[1]) + t * (Math.log(b[1]) - Math.log(a[1]))); } return 7912; }
  var D = [['月球', 1.28 / 3.156e7], ['火星（平均）', 1.3e3 / 3.156e7], ['冥王星', 5.5 * 3600 / 3.156e7], ['半人馬座 α 星', 4.37], ['銀河中心', 26000], ['橫越銀河系', 100000], ['仙女座星系', 2.5e6]];
  function fmt(y) { var s = y * 3.156e7; if (s < 0.1) return '不到 0.1 秒'; if (s < 60) return f1(s) + ' 秒'; if (s < 3600) return f1(s / 60) + ' 分鐘'; if (s < 86400) return f1(s / 3600) + ' 小時'; if (y < 1) return f1(s / 86400) + ' 天'; if (y < 1000) return f1(y) + ' 年'; return Math.round(y).toLocaleString() + ' 年'; }
  function init(root) { var cfg = JSON.parse(root.getAttribute('data-cfg')); head(root, cfg.q); var P = { w: 6, s: 1 }, view = el('div'), inf = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em');
    var b = el('div', 'margin:4px 0'); [['TNG 的曲速表', 1], ['TOS 的公式 v = w³c', 0]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { P.s = o[1]; mark(b, o[1]); draw(); }; b.appendChild(x); }); root.appendChild(b); mark(b, 1);
    var u = slider(root, '曲速', 1, 9.99, 0.01, P.w, function (x) { return 'warp ' + f2(x); }, null, function (x) { P.w = x; draw(); });
    root.appendChild(view); root.appendChild(inf);
    function draw() { var c = P.s ? tng(P.w) : Math.pow(P.w, 3), h = '<table style="width:100%;border-collapse:collapse;font-size:0.92em">';
      D.forEach(function (d) { h += '<tr><td style="padding:4px 6px;border-bottom:1px solid var(--border)">' + d[0] + '</td><td style="padding:4px 6px;border-bottom:1px solid var(--border);text-align:right">光速：' + fmt(d[1]) + '</td><td style="padding:4px 6px;border-bottom:1px solid var(--border);text-align:right"><b>warp ' + f2(P.w) + '：' + fmt(d[1] / c) + '</b></td></tr>'; });
      view.innerHTML = h + '</table>';
      inf.innerHTML = 'warp ' + f2(P.w) + ' ≈ 光速的 <b>' + Math.round(c).toLocaleString() + ' 倍</b>（' + (P.s ? 'TNG 時代的設定：warp 10 代表無限大的速度，無法達到' : '原初系列的非正式公式') + '）。即使如此，橫越銀河系仍要許多年——這正是《重返地球》的故事前提。<br><span style="font-size:0.9em;color:var(--text-muted)">曲速的數值依各時期的設定資料而異；真實物理中，曲速引擎需要負能量，見〈曲速引擎的詳細計算〉。</span>'; }
    u();
  }
  function all() { document.querySelectorAll('.stk-w').forEach(function (w) { if (w.__d) return; w.__d = 1; init(w); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', all); else all();
})();
"""

_w = wdg("stk-w", {"q": u"曲速計算器：以不同的曲速，到各地要多久？"})
WARP = ("raw", _w[1] + u"<script>%s</script>" % STKLIB)
