# -*- coding: utf-8 -*-
"""〈兒童成長心理學〉（cd_）與〈家長教養〉（pa_）共用：課程包裝與 KDLIB 互動元件。

KDLIB 元件（class="kd-w"）：
  ms      發展里程碑：選年齡看各領域「大多數孩子會做的事」（參考 CDC 2022 版里程碑）
  tree    情境決策樹：一步步選擇，看建議的回應方式
  styles  教養風格象限：溫暖回應 × 要求與結構
"""
from cc_common import make_lesson, wdg, LS, D, M
from qt_common import BASEJS
from nv_common import NVLIB, nvw, ev, card, node, CB, CG, CO, CR, CP, CT, CY, CK

CD_NOTE = (u"本課程是發展心理學的一般知識整理，內容參考教科書、經典研究、美國疾病管制與預防中心（CDC）、美國兒科醫學會（AAP）、世界衛生組織（WHO）與台灣衛福部的公開資料（2026 年 10 月查證）。"
           u"每個孩子的發展速度不同，<strong>本課程不能取代醫師、心理師或早療人員的評估</strong>；若有疑慮，請諮詢兒科醫師或兒童發展聯合評估中心。")
PA_NOTE = (u"本課程整理教養研究與官方建議（AAP、WHO、台灣衛福部與教育部等，2026 年 10 月查證），提供的是原則與選項，不是唯一正解；"
           u"每個家庭的情況不同。涉及健康、安全或心理危機時，請尋求專業協助：保護專線 113、安心專線 1925、生命線 1995、張老師 1980。")

MILESTONES = [
 (2, "soc", u"被抱起或聽到說話聲時會安靜下來"), (2, "soc", u"看著你的臉"), (2, "soc", u"你對他說話或微笑時，會回以微笑"), (2, "lang", u"發出哭以外的聲音"), (2, "lang", u"對很大的聲音有反應"),
 (2, "cog", u"會注視移動的人或物"), (2, "mot", u"趴著時能抬頭"), (2, "mot", u"手腳會揮動"),
 (4, "soc", u"會主動微笑來吸引你的注意"), (4, "soc", u"你逗他時會咯咯笑"), (4, "lang", u"發出「啊、喔」之類的聲音"), (4, "lang", u"聽到聲音會轉頭"), (4, "cog", u"餓了看到奶瓶或乳房會張嘴"),
 (4, "mot", u"被抱著時頭能穩穩地不晃"), (4, "mot", u"放在手中的玩具會握住"), (4, "mot", u"趴著時能用手肘撐起上身"),
 (6, "soc", u"認得熟悉的人"), (6, "soc", u"喜歡看鏡子裡的自己"), (6, "soc", u"會笑出聲"), (6, "lang", u"會跟你一來一往地「對話」發聲"), (6, "lang", u"吹口水泡泡、尖叫"),
 (6, "cog", u"把東西放進嘴裡探索"), (6, "cog", u"伸手去拿想要的玩具"), (6, "mot", u"能從趴著翻成躺著"), (6, "mot", u"坐著時會用手撐地"),
 (9, "soc", u"對陌生人害羞、黏人或害怕"), (9, "soc", u"臉上有多種表情（高興、難過、生氣、驚訝）"), (9, "soc", u"叫他名字時會看你"), (9, "lang", u"發出「媽媽媽、爸爸爸」等重複音節"), (9, "lang", u"舉起雙手要人抱"),
 (9, "cog", u"會找掉到看不見的地方的東西"), (9, "cog", u"拿兩個東西互相敲"), (9, "mot", u"能自己坐起來、不用扶也能坐穩"), (9, "mot", u"東西能從一手換到另一手"),
 (12, "soc", u"會玩「躲貓貓」「拍手」之類的互動遊戲"), (12, "lang", u"會揮手說再見"), (12, "lang", u"有意義地叫「爸爸」「媽媽」"), (12, "lang", u"聽得懂「不」"), (12, "cog", u"會把東西放進容器"),
 (12, "cog", u"會去找你藏起來的東西"), (12, "mot", u"能扶著東西站起來"), (12, "mot", u"扶著家具走"), (12, "mot", u"用拇指和食指捏起小東西"),
 (18, "soc", u"會走開一點，但會回頭確認你在附近"), (18, "soc", u"用手指指出有趣的東西給你看"), (18, "lang", u"除了爸爸媽媽，還會試著說 3 個以上的詞"), (18, "lang", u"不用手勢也能聽懂一個步驟的指令"),
 (18, "cog", u"模仿你做家事（例如掃地）"), (18, "mot", u"不用扶就能走"), (18, "mot", u"會亂畫"), (18, "mot", u"試著用湯匙"),
 (24, "soc", u"注意到別人受傷或難過"), (24, "soc", u"做新的事時會看你的反應"), (24, "lang", u"把兩個詞連起來說（例如「還要牛奶」）"), (24, "lang", u"指出至少兩個身體部位"), (24, "cog", u"一手拿東西、另一手做別的事"),
 (24, "cog", u"同時玩一個以上的玩具"), (24, "mot", u"會踢球"), (24, "mot", u"會跑"), (24, "mot", u"扶著或不扶走上幾階樓梯"),
 (30, "soc", u"在其他孩子旁邊玩，有時一起玩"), (30, "soc", u"會照著簡單的日常程序做"), (30, "lang", u"大約會說 50 個詞"), (30, "lang", u"會用「我」「我們」這類詞"), (30, "cog", u"會假扮遊戲（例如餵娃娃吃飯）"),
 (30, "cog", u"能聽懂兩個步驟的指令"), (30, "cog", u"至少認得一種顏色"), (30, "mot", u"雙腳離地跳"), (30, "mot", u"一頁一頁翻書"),
 (36, "soc", u"你離開後 10 分鐘內能平靜下來"), (36, "soc", u"注意到其他孩子並加入他們"), (36, "lang", u"能來回對話至少兩輪"), (36, "lang", u"會問「誰、什麼、哪裡、為什麼」"), (36, "lang", u"說的話多半能讓別人聽懂"),
 (36, "cog", u"看示範後能畫一個圓"), (36, "cog", u"被提醒後會避開燙的東西"), (36, "mot", u"會自己穿上一些衣服"), (36, "mot", u"會用叉子"),
 (48, "soc", u"玩的時候會假裝成別的角色"), (48, "soc", u"別人難過時會安慰"), (48, "lang", u"說出 4 個詞以上的句子"), (48, "lang", u"能說說今天發生的一件事"), (48, "cog", u"說得出幾種顏色"),
 (48, "cog", u"知道熟悉的故事接下來會發生什麼"), (48, "cog", u"畫人時至少畫出 3 個身體部位"), (48, "mot", u"大多能接住大球"), (48, "mot", u"會解開一些釦子"),
 (60, "soc", u"玩遊戲時會遵守規則、輪流"), (60, "soc", u"會做簡單的家事"), (60, "lang", u"能講一個有兩件事以上的故事"), (60, "lang", u"能來回對話三輪以上"), (60, "lang", u"會用「昨天」「明天」等時間詞"),
 (60, "cog", u"能數到 10"), (60, "cog", u"能專心做一件事 5～10 分鐘"), (60, "cog", u"會寫自己名字中的一些字"), (60, "mot", u"會扣一些釦子"), (60, "mot", u"單腳跳"),
]

KDLIB = r"""
(function () {
  if (window.__kdLib) return; window.__kdLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  /* ---------- 發展里程碑 ---------- */
  function initMs(root, cfg) {
    head(root, cfg.q); var data = cfg.data, ages = [], cur, view = el('div', 'margin-top:8px'), p;
    data.forEach(function (d) { if (ages.indexOf(d[0]) < 0) ages.push(d[0]); });
    var D = { soc: ['社會與情緒', '#d9822b'], lang: ['語言與溝通', '#3a6ea5'], cog: ['認知（學習、思考、解決問題）', '#9c89d6'], mot: ['動作與身體', '#5aa469'] };
    function lab(m) { return m < 24 ? m + ' 個月' : (m % 12 ? (Math.floor(m / 12) + ' 歲半') : (m / 12 + ' 歲')); }
    var bb = bar(root); ages.forEach(function (a) { var b = btn(lab(a), 'a' + a); b.addEventListener('click', function () { cur = a; mark(bb, 'a' + a); draw(); }); bb.appendChild(b); });
    root.appendChild(view); p = info(root); cur = cfg.start || ages[0]; mark(bb, 'a' + cur);
    function draw() { var h = '<div style="display:flex;flex-wrap:wrap;gap:10px">', i = ages.indexOf(cur), nxt = ages[i + 1];
      Object.keys(D).forEach(function (k) { var items = data.filter(function (d) { return d[0] === cur && d[1] === k; }); if (!items.length) return;
        h += '<div style="flex:1 1 260px;border:1px solid var(--border);border-left:4px solid ' + D[k][1] + ';border-radius:8px;padding:8px 12px"><b style="color:' + D[k][1] + '">' + D[k][0] + '</b><ul style="margin:6px 0 0;padding-left:18px">' + items.map(function (d) { return '<li>' + esc(d[2]) + '</li>'; }).join('') + '</ul></div>'; });
      view.innerHTML = h + '</div>';
      p.innerHTML = '這些是<b>大約 4 分之 3 的孩子在 ' + lab(cur) + '時已經會做</b>的事（參考 CDC 2022 年修訂的里程碑，中文為意譯）。沒做到其中一兩項不代表有問題；若多項都還沒出現，或孩子<b>失去了原本會的能力</b>，請和兒科醫師討論。' +
        (nxt ? '<br>下一個檢查點：' + lab(nxt) + '。台灣未滿 7 歲兒童有政府補助的兒童預防保健（2026 年 7 月起為 9 次），可以利用這些時機請醫師評估。' : '<br>5 歲之後，發展的差異越來越大，較少用「里程碑」檢核，改以學習、社交與情緒的整體表現來觀察。'); }
    draw();
  }

  /* ---------- 情境決策樹 ---------- */
  function initTree(root, cfg) {
    head(root, cfg.q); var path = ['start'], view = el('div', 'margin-top:6px'); root.appendChild(view);
    function bs(t, a) { return '<button type="button" ' + a + ' style="display:block;width:100%;text-align:left;margin:4px 0;padding:8px 10px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit">' + t + '</button>'; }
    function draw() { var id = path[path.length - 1], n = cfg.nodes[id], h = '';
      if (path.length > 1) h += '<div style="font-size:0.82em;color:var(--text-muted);margin-bottom:6px">' + path.slice(0, -1).map(function (k, i) { var o = cfg.nodes[k].o.filter(function (o) { return o[1] === path[i + 1]; })[0]; return esc(o ? o[0] : ''); }).join(' → ') + '</div>';
      if (n.a) h += '<div style="padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7">' + n.a + '</div>';
      else { h += '<div style="font-weight:bold;margin-bottom:6px">' + n.q + '</div>'; n.o.forEach(function (o) { h += bs(o[0], 'data-n="' + o[1] + '"'); }); }
      if (path.length > 1) h += '<div style="margin-top:8px"><button type="button" data-back="1">← 上一步</button> <button type="button" data-home="1">↺ 從頭</button></div>';
      view.innerHTML = h;
      view.querySelectorAll('[data-back],[data-home]').forEach(function (b) { b.style.cssText = 'padding:4px 10px;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit;font-size:0.88em'; });
      view.querySelectorAll('button[data-n]').forEach(function (b) { b.addEventListener('click', function () { path.push(b.getAttribute('data-n')); draw(); }); });
      var bk = view.querySelector('[data-back]'); if (bk) bk.addEventListener('click', function () { path.pop(); draw(); });
      var hm = view.querySelector('[data-home]'); if (hm) hm.addEventListener('click', function () { path = ['start']; draw(); }); }
    draw();
  }

  /* ---------- 教養風格象限 ---------- */
  function initStyles(root, cfg) {
    head(root, cfg.q); var w = 0.7, s = 0.7, out = el('div'), p;
    var u1 = slider(root, '溫暖與回應（傾聽、接納情緒、表達愛）', 0, 1, 0.05, w, function (v) { return Math.round(v * 100) + '%'; }, 'w', function (v) { w = v; draw(); });
    var u2 = slider(root, '要求與結構（規矩、期待、一致的後果）', 0, 1, 0.05, s, function (v) { return Math.round(v * 100) + '%'; }, 's', function (v) { s = v; draw(); });
    root.appendChild(out); p = info(root);
    var S = { aut: ['權威型（民主型）', '#5aa469', '溫暖又有規矩：解釋理由、傾聽孩子，也堅持重要的界線。研究中與較好的學業、社交與心理健康最一致地相關。'],
              autr: ['專制型', '#d0564f', '規矩多但溫暖少：「因為我說了算」。孩子可能服從，但較容易焦慮、自尊較低，或在外面反叛。'],
              perm: ['寬容型（放任型）', '#d9822b', '很溫暖但缺乏界線：什麼都好。孩子可能較難自我控制、較衝動。'],
              negl: ['忽視型', '#888', '既少溫暖也少要求：不太參與孩子的生活。研究中與最多不良結果相關。'] };
    function draw() { var k = w >= 0.5 ? (s >= 0.5 ? 'aut' : 'perm') : (s >= 0.5 ? 'autr' : 'negl'), W = 300, H = 300, g = '';
      var cells = [['autr', 0, 0], ['aut', 150, 0], ['negl', 0, 150], ['perm', 150, 150]];
      cells.forEach(function (c) { g += '<rect x="' + c[1] + '" y="' + c[2] + '" width="150" height="150" fill="' + S[c[0]][1] + '" opacity="' + (c[0] === k ? 0.35 : 0.1) + '"/>' + tx(c[1] + 75, c[2] + 78, S[c[0]][0].replace(/（.*）/, ''), 13, S[c[0]][1]); });
      g += '<circle cx="' + (w * 300) + '" cy="' + ((1 - s) * 300) + '" r="8" fill="#3a6ea5" stroke="#fff" stroke-width="2"/>';
      g += tx(150, 316, '溫暖與回應 →', 11, 'var(--text-muted)') + '<text x="-150" y="-8" transform="rotate(-90)" font-size="11" fill="var(--text-muted)" text-anchor="middle">要求與結構 →</text>';
      out.innerHTML = '<div style="max-width:340px;margin:10px auto">' + svgw('-20 -4 330 330', g) + '</div>';
      p.innerHTML = '<b style="color:' + S[k][1] + '">' + S[k][0] + '</b>：' + S[k][2] + '<br><span style="font-size:0.9em;color:var(--text-muted)">Baumrind（1966、1971）提出前三型，Maccoby 與 Martin（1983）加入忽視型。真實的家長多半落在中間、而且會隨情境改變；文化背景也會影響各型的效果。</span>'; }
    u1(); u2(); draw();
  }

  function initAll() { document.querySelectorAll('.kd-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ ms: initMs, tree: initTree, styles: initStyles })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def kdw(cfg, maxw=720):
    return wdg("kd-w", cfg, maxw)


def ms(start=None, ages=None):
    data = [list(m) for m in MILESTONES if (ages is None or m[0] in ages)]
    cfg = {"t": "ms", "q": u"發展里程碑：選一個年齡，看大多數孩子在這時會做的事", "data": data}
    if start:
        cfg["start"] = start
    return kdw(cfg)


def tree(q, nodes):
    return kdw({"t": "tree", "q": q, "nodes": nodes})


STYLES = kdw({"t": "styles", "q": u"教養風格象限：拖動兩個滑桿，看你落在哪一型"}, 560)

SLEEP = ("t", [u"年齡", u"建議每天睡眠（含小睡）", u"來源"],
         [[u"4～12 個月", u"12～16 小時", u"美國睡眠醫學會（AASM，2016）"], [u"1～2 歲", u"11～14 小時", u"同上"], [u"3～5 歲", u"10～13 小時", u"同上"],
          [u"6～12 歲", u"9～12 小時", u"同上"], [u"13～18 歲", u"8～10 小時", u"同上"]])

SCREEN = ("t", [u"年齡", u"美國兒科醫學會（AAP，2016）", u"世界衛生組織（WHO，2019）", u"台灣國健署"],
          [[u"未滿 18 個月", u"除了視訊通話外避免使用", u"2 歲以下不建議久坐看螢幕", u"2 歲以下避免使用"], [u"18～24 個月", u"如要使用，選高品質內容並由大人陪看", u"同上", u"同上"],
           [u"2～5 歲", u"每天不超過 1 小時高品質內容，大人陪看", u"2～4 歲每天不超過 1 小時", u"每次不超過 30 分鐘"], [u"6 歲以上", u"與家人訂定一致的使用規則，確保睡眠、運動不被排擠", u"—", u"護眼「3010」原則：用眼 30 分鐘休息 10 分鐘"]])


def make(icon, note):
    base = make_lesson(icon, note, KDLIB, "kd-w")

    def lesson(*a, **k):
        L = base(*a, **k)
        if any(isinstance(b, tuple) and b[0] == "raw" and 'class="nv-w' in b[1] for b in L.body):
            L.body.insert(0, ("raw", u"<script>%s</script>" % NVLIB))
        return L
    return lesson


def XO(tid, name):
    return u'<a href="../%s/index.html">〈%s〉</a>' % (tid, name)
