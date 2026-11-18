# -*- coding: utf-8 -*-
"""〈異塵餘生 Fallout 全紀錄〉（flo_）共用：課程包裝與互動元件（nv_common 的 nv-w，加上 S.P.E.C.I.A.L. 配點器 flo-w）。"""
from nv_common import *
from cc_common import wdg
from qt_common import BASEJS

lesson = nv_lesson(u"☢️")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


SPOIL = lambda what: ("note", u"⚠️ 暴雷提醒", [("p", u"本課會談到%s的重要劇情。還沒玩（看）過、又不想被暴雷的人，可以先跳過標示的段落。" % what)])

GAMES = nvw({"t": "timeline", "q": u"Fallout 系列的發行年表（點一列看說明；可依類型篩選）：", "yw": 96, "mh": 560,
  "groups": [["m", u"本傳", CR], ["s", u"外傳", CB], ["t", u"影集", CP], ["x", u"大事", CG]],
  "ev": [ev(u"1988", u"《廢土》（Wasteland）", u"Interplay 的核戰後角色扮演遊戲，Fallout 的精神前身。", "x"),
         ev(u"1997", u"《異塵餘生》（Fallout）", u"Interplay 推出。南加州，2161 年，尋找淨水晶片的避難所居民。", "m"),
         ev(u"1998", u"《異塵餘生 2》", u"黑島工作室。北加州，2241 年，尋找 G.E.C.K. 的天選之人。", "m"),
         ev(u"2001", u"《Fallout Tactics》", u"戰術小隊戰鬥的外傳，舞台在美國中西部。", "s"),
         ev(u"2003", u"黑島關閉，「Van Buren」取消", u"黑島版的 Fallout 3 胎死腹中，但凱撒軍團、胡佛水壩等構想後來在《新維加斯》復活。", "x"),
         ev(u"2004～2007", u"Bethesda 取得版權", u"2004 年取得開發續作的授權，2007 年買下整個品牌。", "x"),
         ev(u"2008", u"《異塵餘生 3》", u"Bethesda。華盛頓特區，2277 年。改為第一人稱開放世界。", "m"),
         ev(u"2010", u"《異塵餘生：新維加斯》", u"黑曜石娛樂。莫哈維沙漠，2281 年。被許多玩家視為劇本最好的一代。", "m"),
         ev(u"2015", u"《Fallout Shelter》", u"經營避難所的免費手機遊戲。", "s"),
         ev(u"2015", u"《異塵餘生 4》", u"波士頓，2287 年。加入聚落建造。", "m"),
         ev(u"2018", u"《異塵餘生 76》", u"線上多人遊戲。西維吉尼亞，2102 年。首發災情慘重，之後逐步翻身。", "s"),
         ev(u"2024", u"影集第一季", u"Amazon Prime Video。洛杉磯，2296 年。", "t"),
         ev(u"2024", u"《Fallout: London》", u"粉絲團隊製作的大型免費模組，舞台在倫敦。", "x"),
         ev(u"2025～2026", u"影集第二季", u"2025 年 12 月開播，舞台移到新維加斯。第三季已確定製作。", "t")]})

LORE = nvw({"t": "timeline", "q": u"Fallout 世界的歷史（遊戲中的設定；點一列看說明）：", "yw": 104, "mh": 560,
  "groups": [["o", u"舊世界", CO], ["p", u"大戰後", CB]],
  "ev": [ev(u"1945 年之後", u"歷史的分歧", u"二戰後，這個世界的科技走向真空管與原子能，文化停留在 1950 年代的風格。", "o"),
         ev(u"2052", u"資源戰爭爆發", u"石油日漸枯竭，歐洲聯邦與中東開戰；聯合國解體。", "o"),
         ev(u"2053", u"新瘟疫", u"致命的傳染病讓各國實施隔離，恐慌蔓延。", "o"),
         ev(u"2066", u"中國入侵阿拉斯加", u"為了石油，中美戰爭爆發。", "o"),
         ev(u"2076", u"美國併吞加拿大", u"為了資源與輸油管。", "o"),
         ev(u"2077 年 1 月", u"安克拉治光復", u"穿著動力裝甲的美軍奪回阿拉斯加。", "o"),
         ev(u"2077 年 10 月 23 日", u"大戰", u"核彈在約兩小時內落下，舊世界毀滅。至今沒有人知道是誰先發射的。", "o"),
         ev(u"2102", u"76 號避難所開啟", u"「重建日」，居民回到西維吉尼亞（《76》）。", "p"),
         ev(u"2161", u"避難所居民", u"13 號避難所的淨水晶片故障（初代）。", "p"),
         ev(u"2180 年代", u"新加州共和國成立", u"以夏迪森茲為核心。", "p"),
         ev(u"2241", u"天選之人", u"英克雷的陰謀與石油鑽井平台（《2》）。", "p"),
         ev(u"2277", u"首都廢土", u"101 號避難所的孤獨流浪者（《3》）；同年第一次胡佛水壩戰役。", "p"),
         ev(u"2281", u"莫哈維", u"信使與白金晶片（《新維加斯》）。", "p"),
         ev(u"2287", u"聯邦", u"唯一倖存者尋找兒子（《4》）。", "p"),
         ev(u"2296", u"洛杉磯", u"33 號避難所的露西（影集）。", "p")]})

VAULTS = nvw({"t": "cards", "q": u"避難所的「社會實驗」（可篩選或搜尋）：",
  "groups": [["e", u"實驗", CR], ["c", u"控制組", CG], ["t", u"影集", CP]],
  "cards": [card(u"8 號避難所", "c", u"控制組，照計畫開啟。居民後來建立了「避難所城」。", u"Vault 8"),
            card(u"11 號避難所", "e", u"居民被告知每年必須獻祭一個人，否則全員會死。最後一年，倖存者拒絕獻祭——門外的錄音告訴他們：拒絕的人才能活下來。", u"Vault 11"),
            card(u"12 號避難所", "e", u"大門刻意設計成無法完全關閉，研究輻射的影響。居民變成了屍鬼，建立了「死城」（初代）。", u"Vault 12"),
            card(u"13 號避難所", "e", u"預定封閉 200 年，研究長期隔離。淨水晶片故障，主角被迫出門（初代）。", u"Vault 13"),
            card(u"21 號避難所", "e", u"所有爭議都用賭博來解決。後來成了新維加斯的旅館。", u"Vault 21"),
            card(u"68／69 號避難所", "e", u"一個裡面有 999 名男性與 1 名女性，另一個則相反。", u"Vault 68 / 69"),
            card(u"77 號避難所", "e", u"只有一個人，和一箱木偶。", u"Vault 77"),
            card(u"101 號避難所", "e", u"監督者被命令永遠不能開門，研究獨裁的領袖（《3》）。", u"Vault 101"),
            card(u"106 號避難所", "e", u"通風系統在封閉十天後釋放迷幻藥劑。", u"Vault 106"),
            card(u"108 號避難所", "e", u"住滿了名叫「蓋瑞」的複製人。", u"Vault 108"),
            card(u"111 號避難所", "e", u"居民被冷凍，表面上是保存人類（《4》）。", u"Vault 111"),
            card(u"112 號避難所", "e", u"居民被關在虛擬實境「寧靜小巷」中，受一名博士擺布（《3》）。", u"Vault 112"),
            card(u"31／32／33 號避難所", "t", u"影集的舞台。三座相連的避難所，背後藏著 Vault-Tec 主管們的計畫。", u"Vault 31 / 32 / 33")]})

_US = (u'<rect x="0" y="0" width="640" height="400" fill="#dde9ef" rx="8"/>'
       u'<path d="M60,50 L250,50 L330,55 L390,80 L430,75 L470,90 L540,70 L600,40 L612,70 L565,128 L556,170 L532,212 L520,260 L492,300 L506,368 L486,374 L462,322 L410,322 L372,332 L346,380 L312,352 L282,312 L222,302 L150,292 L110,262 L82,212 L60,140 Z" fill="#efe6cc" stroke="#a89060"/>'
       u'<rect x="14" y="300" width="72" height="72" fill="#efe6cc" stroke="#a89060" rx="4"/><text x="50" y="390" font-size="10" fill="#5a7080" text-anchor="middle">阿拉斯加（示意）</text>')

MAP = nvw({"t": "map", "h": 400, "q": u"Fallout 的舞台（示意圖，不按比例）：", "bg": _US,
  "pts": [pt(90, 236, u"洛杉磯", u"初代的「大教堂」與「骨場」；影集第一季的舞台。附近的 13 號避難所是系列的起點。", CR, None, "start"),
          pt(66, 150, u"舊金山", u"《異塵餘生 2》的終盤；附近有英克雷的石油鑽井平台。", CR, None, "start"),
          pt(78, 92, u"阿羅由", u"《異塵餘生 2》主角的故鄉部落。", CO, None, "start"),
          pt(132, 206, u"新維加斯", u"豪斯先生的城市；胡佛水壩在附近。《新維加斯》與影集第二季的舞台。", CP, None, "start"),
          pt(420, 112, u"芝加哥", u"《Fallout Tactics》的舞台。", CB, None, "middle"),
          pt(492, 186, u"西維吉尼亞", u"《76》的舞台，充滿天蛾人等阿帕拉契民間傳說。", CG, None, "end"),
          pt(528, 172, u"華盛頓特區", u"《異塵餘生 3》的「首都廢土」：傑佛遜紀念堂的淨水計畫。", CR, None, "start"),
          pt(594, 96, u"波士頓", u"《異塵餘生 4》的「聯邦」：鑽石城（芬威球場）與地底的「學院」。", CR, None, "end"),
          pt(50, 335, u"安克拉治", u"大戰前中美戰爭的戰場（《3》的「安克拉治作戰」）。", CK, None, "middle")],
  "hint": u"點選地點，查看它是哪一代的舞台。"})

FACTIONS = nvw({"t": "graph", "h": 380, "q": u"Fallout 的主要勢力——點選看說明：",
  "nodes": [node("vt", u"Vault-Tec", 320, 40, CY, u"建造避難所的公司，在避難所中進行秘密的社會實驗。"),
            node("enc", u"英克雷", 520, 50, CK, u"舊美國政府的殘黨，自認是「純正」的人類，想消滅受輻射影響的其他人（《2》《3》）。"),
            node("master", u"主宰", 110, 40, CG, u"與 FEV 病毒融合的怪物，想把人類都變成超級變種人（初代）。"),
            node("bos", u"鋼鐵兄弟會", 320, 160, CB, u"由叛逃軍人創立的科技騎士團，蒐集並守護戰前的科技。"),
            node("ncr", u"新加州共和國", 120, 150, CO, u"廢土上最大的民主國家，正在向東擴張（《2》《新維加斯》）。"),
            node("legion", u"凱撒軍團", 90, 290, CR, u"模仿羅馬帝國的奴隸制軍事集團（《新維加斯》）。"),
            node("house", u"豪斯先生", 260, 300, CP, u"戰前的科技富豪，靠維生裝置活了兩百多年，統治新維加斯。"),
            node("inst", u"學院", 470, 250, CT, u"波士頓地底的科學家組織，製造擬真的合成人（《4》）。"),
            node("rr", u"鐵路", 580, 330, CK, u"幫助合成人逃離學院的地下組織（《4》）。"),
            node("mm", u"民兵", 570, 160, CG, u"保護聚落的民間武力（《4》）。")],
  "edges": [["vt", "enc", u"秘密合作", CY, 1], ["master", "bos", u"對抗", CG, 1], ["bos", "enc", u"宿敵", CB], ["ncr", "legion", u"胡佛水壩", CR],
            ["ncr", "bos", u"戰爭", CO, 1], ["house", "ncr", u"利用", CP, 1], ["house", "legion", u"敵對", CP], ["bos", "inst", u"摧毀", CB],
            ["inst", "rr", u"敵對", CT], ["mm", "inst", u"可對抗", CG, 1]],
  "hint": u"點選勢力，查看說明。實線表示正面衝突，虛線表示較複雜的關係。"})

FLOLIB = r"""
(function () {
  if (window.__floLib) return; window.__floLib = 1;
""" + BASEJS + r"""
  var K = [['S', '力量', 'Strength'], ['P', '感知', 'Perception'], ['E', '耐力', 'Endurance'], ['C', '魅力', 'Charisma'], ['I', '智力', 'Intelligence'], ['A', '敏捷', 'Agility'], ['L', '幸運', 'Luck']];
  function init(root) { var cfg = JSON.parse(root.getAttribute('data-cfg')); head(root, cfg.q); var v = [5, 5, 5, 5, 5, 5, 5], POOL = 40;
    var rows = el('div'), sum = el('div', 'margin:6px 0;font-weight:bold'), view = el('div'), inf = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em');
    var bar = el('div', 'margin:4px 0'); [['重設（全部 5）', 0], ['戰士', 1], ['說客', 2], ['神槍手', 3], ['笨蛋', 4]].forEach(function (o) { var x = btn(o[0], o[1]); x.onclick = function () { v = [[5, 5, 5, 5, 5, 5, 5], [9, 6, 8, 2, 4, 7, 4], [4, 5, 4, 9, 9, 5, 4], [4, 9, 5, 3, 6, 8, 5], [9, 5, 9, 4, 1, 6, 6]][o[1]].slice(); draw(); }; bar.appendChild(x); });
    root.appendChild(bar); root.appendChild(rows); root.appendChild(sum); root.appendChild(view); root.appendChild(inf);
    function draw() { var used = v.reduce(function (a, b) { return a + b; }, 0), left = POOL - used; rows.innerHTML = '';
      K.forEach(function (k, i) { var r = el('div', 'display:flex;align-items:center;gap:8px;margin:3px 0');
        r.appendChild(el('div', 'width:7.5em', '<b>' + k[0] + '</b> ' + k[1]));
        var m = btn('−'), p = btn('+'); m.onclick = function () { if (v[i] > 1) { v[i]--; draw(); } }; p.onclick = function () { if (v[i] < 10 && left > 0) { v[i]++; draw(); } };
        var b = el('div', 'flex:1;height:12px;border-radius:6px;background:var(--border);overflow:hidden', '<div style="height:100%;width:' + (v[i] * 10) + '%;background:' + (v[i] <= 2 ? '#d0564f' : v[i] >= 9 ? '#3a8a5a' : '#3a6ea5') + '"></div>');
        r.appendChild(m); r.appendChild(b); r.appendChild(el('div', 'width:1.6em;text-align:right;font-weight:bold', '' + v[i])); r.appendChild(p); rows.appendChild(r); });
      sum.innerHTML = '剩餘點數：<span style="color:' + (left ? '#d0564f' : '#3a8a5a') + '">' + left + '</span>（總共 40 點，每項 1～10）';
      var S = v[0], P = v[1], E = v[2], C = v[3], I = v[4], A = v[5], L = v[6];
      var d = [['生命值', 15 + S + 2 * E], ['行動點數', 5 + Math.floor(A / 2)], ['負重（磅）', 25 + 25 * S], ['每級技能點', 5 + 2 * I], ['先攻順序', 2 * P], ['爆擊率', L + '%'], ['防禦等級', A]];
      var h = '<table style="width:100%;border-collapse:collapse;font-size:0.92em"><tr>'; d.forEach(function (x) { h += '<td style="padding:4px;border:1px solid var(--border);text-align:center"><div style="color:var(--text-muted);font-size:0.85em">' + x[0] + '</div><b>' + x[1] + '</b></td>'; });
      view.innerHTML = h + '</tr></table>';
      var t = [];
      if (I <= 3) t.push('<b>智力 ' + I + '</b>：對話選項會變成結結巴巴的傻話，NPC 也會用對待孩子的方式跟你說話——系列著名的「低智力玩法」。');
      else if (I >= 8) t.push('<b>高智力</b>：每級技能點多，還會出現科學、醫學的特殊對話選項。');
      if (C >= 8) t.push('<b>高魅力</b>：適合用口才說服敵人，甚至不戰而勝——初代可以說服主宰自我毀滅。');
      if (S >= 8 && E >= 7) t.push('<b>高力量與耐力</b>：血厚、能扛重武器，正面衝突的坦克。');
      if (A >= 8) t.push('<b>高敏捷</b>：每回合的行動點數多，戰鬥中能多開好幾槍。');
      if (L >= 8) t.push('<b>高幸運</b>：爆擊頻繁，賭場裡也特別順手。');
      if (Math.min.apply(null, v) <= 2 && I > 3) t.push('有一項屬性很低：Fallout 鼓勵「有缺陷」的角色，弱點也是角色扮演的一部分。');
      if (!t.length) t.push('平均型的角色：什麼都能做一點，但沒有特別擅長的方式。試著把點數集中，看看衍生數值怎麼變。');
      inf.innerHTML = t.join('<br>') + '<br><span style="font-size:0.88em;color:var(--text-muted)">衍生數值以初代《異塵餘生》的公式計算；各代的規則略有不同。</span>'; }
    draw();
  }
  function all() { document.querySelectorAll('.flo-w').forEach(function (w) { if (w.__d) return; w.__d = 1; init(w); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', all); else all();
})();
"""

_w = wdg("flo-w", {"q": u"S.P.E.C.I.A.L. 配點器：分配 40 點，看看你的角色會是什麼樣子："})
SPECIAL = ("raw", _w[1] + u"<script>%s</script>" % FLOLIB)
