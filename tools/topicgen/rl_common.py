# -*- coding: utf-8 -*-
"""〈伊斯蘭教〉〈印度教〉共用工具與互動元件（RLLIB）。"""
from cc_common import *
from qt_common import BASEJS

IS_NOTE = (u"本課程是<strong>宗教史與宗教學的介紹</strong>，目的在理解，不在傳教或評價信仰。"
           u"教義部分以多數穆斯林的主流理解為準，並註明遜尼派與什葉派等差異；歷史年代與人數多為學界常用的約略值。")
HI_NOTE = (u"本課程是<strong>宗教史與宗教學的介紹</strong>，目的在理解，不在傳教或評價信仰。"
           u"「印度教」內部極為多元，任何概括都有例外；經典年代多為學界的約略推估，傳統說法另行註明。")

RLLIB = r"""
(function () {
  if (window.__rlLib) return; window.__rlLib = 1;
""" + BASEJS + r"""
  function info(root) { var p = el('p', 'margin:6px 0 0;line-height:1.7'); root.appendChild(p); return p; }
  function bar(root) { var b = el('div'); root.appendChild(b); return b; }
  function bt(b, t, k, f) { var x = btn(t, k); x.addEventListener('click', f); b.appendChild(x); return x; }

  /* ---------- 1. 伊斯蘭曆換算（表格曆法） ---------- */
  var HM = ['穆哈蘭姆月（1 月）', '色法爾月（2 月）', '賴比爾·敖外魯月（3 月）', '賴比爾·阿色尼月（4 月）', '主馬達·敖外魯月（5 月）', '主馬達·阿色尼月（6 月）',
    '賴哲卜月（7 月）', '舍爾邦月（8 月）', '賴買丹月（9 月，齋戒月）', '閃瓦魯月（10 月）', '都爾嘎爾德月（11 月）', '都爾黑哲月（12 月，朝覲月）'];
  function g2jd(y, m, d) { if (m <= 2) { y -= 1; m += 12; } var a = Math.floor(y / 100), b = 2 - a + Math.floor(a / 4);
    return Math.floor(365.25 * (y + 4716)) + Math.floor(30.6001 * (m + 1)) + d + b - 1524.5; }
  function jd2g(jd) { var z = Math.floor(jd + 0.5), a = Math.floor((z - 1867216.25) / 36524.25); a = z + 1 + a - Math.floor(a / 4);
    var b = a + 1524, c = Math.floor((b - 122.1) / 365.25), d = Math.floor(365.25 * c), e = Math.floor((b - d) / 30.6001);
    var day = b - d - Math.floor(30.6001 * e), mo = e < 14 ? e - 1 : e - 13, yr = mo > 2 ? c - 4716 : c - 4715; return [yr, mo, day]; }
  function h2jd(y, m, d) { return d + Math.ceil(29.5 * (m - 1)) + (y - 1) * 354 + Math.floor((3 + 11 * y) / 30) + 1948439.5 - 1; }
  function jd2h(jd) { jd = Math.floor(jd) + 0.5; var y = Math.floor((30 * (jd - 1948439.5) + 10646) / 10631);
    var m = Math.min(12, Math.ceil((jd - (29 + h2jd(y, 1, 1))) / 29.5) + 1); var d = jd - h2jd(y, m, 1) + 1; return [y, m, d]; }
  window.__rlHijri = { g2jd: g2jd, jd2g: jd2g, h2jd: h2jd, jd2h: jd2h };
  function initHijri(root, cfg) {
    head(root, cfg.q); var box = el('div', 'display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:4px 0');
    var inp = document.createElement('input'); inp.type = 'date'; inp.style.cssText = 'padding:4px;border:1px solid var(--border);border-radius:6px;background:var(--surface);color:var(--text);font:inherit';
    var now = new Date(); inp.value = now.getFullYear() + '-' + ('0' + (now.getMonth() + 1)).slice(-2) + '-' + ('0' + now.getDate()).slice(-2);
    box.appendChild(el('span', '', '西曆日期：')); box.appendChild(inp); root.appendChild(box); var p = info(root);
    function fmt(g) { return g[0] + ' 年 ' + g[1] + ' 月 ' + g[2] + ' 日'; }
    function draw() { var v = inp.value.split('-').map(Number); if (v.length < 3 || !v[0]) return;
      var h = jd2h(g2jd(v[0], v[1], v[2])), y = h[0];
      var ram = jd2g(h2jd(y, 9, 1)), fitr = jd2g(h2jd(y, 10, 1)), adha = jd2g(h2jd(y, 12, 10)), ny = jd2g(h2jd(y + 1, 1, 1));
      if (h[1] > 9) ram = jd2g(h2jd(y + 1, 9, 1)), fitr = jd2g(h2jd(y + 1, 10, 1));
      if (h[1] === 12 && h[2] > 10) adha = jd2g(h2jd(y + 1, 12, 10));
      p.innerHTML = '伊斯蘭曆：<b>' + y + ' 年 ' + HM[h[1] - 1] + ' ' + h[2] + ' 日</b>' +
        '<br>下一個齋戒月開始：約 ' + fmt(ram) + '　開齋節：約 ' + fmt(fitr) +
        '<br>宰牲節（朝覲月 10 日）：約 ' + fmt(adha) + '　伊斯蘭新年：約 ' + fmt(ny) +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">這是用「表格曆法」的算術公式推算。實際的月份開始多以觀察新月決定，各國可能相差 1～2 天。' +
        '伊斯蘭曆一年約 354 天，比西曆少約 11 天，所以齋戒月每年提早約 11 天，大約 33 年繞西曆一圈。</span>'; }
    inp.addEventListener('input', draw); draw();
  }

  /* ---------- 2. 伊斯蘭教派關係 ---------- */
  var SECTS = [
    ['伊斯蘭教', 320, 30, '', '全球約 19～20 億信徒。所有派別都承認《古蘭經》、認主獨一與穆罕默德的先知地位；分歧主要在先知之後由誰領導社群，以及由此衍生的法學與神學差異。'],
    ['遜尼派', 150, 100, '伊斯蘭教', '約占 85～90%。認為領袖應由社群推選，承認前四位哈里發（艾布·伯克爾、歐麥爾、奧斯曼、阿里）都是正統。重視先知的「遜奈」（慣行）與社群公議。'],
    ['什葉派', 470, 100, '伊斯蘭教', '約占 10～15%，主要在伊朗、伊拉克、巴林、亞塞拜然、黎巴嫩。認為領導權應由先知的堂弟兼女婿阿里及其後裔（伊瑪目）繼承。'],
    ['哈瓦利吉派', 320, 100, '伊斯蘭教', '早期從阿里陣營出走的激進派別，認為犯大罪者不再是穆斯林。主體已消失，溫和的分支易巴德派今日仍在阿曼為主流。'],
    ['四大法學派', 60, 175, '遜尼派', '哈乃斐派（土耳其、中亞、南亞、中國）、馬立克派（北非、西非）、沙斐儀派（東非、東南亞）、罕百里派（阿拉伯半島）。彼此承認對方是正統，差異多在細節。'],
    ['蘇菲主義', 175, 175, '遜尼派', '重視內在修行與對真主之愛的神祕主義傳統，以導師與道團傳承。不是獨立教派，遜尼派與什葉派中都有蘇菲。'],
    ['十二伊瑪目派', 415, 175, '什葉派', '什葉派最大分支，伊朗的國教。相信第十二位伊瑪目於 874 年隱遁，將在末日以「馬赫迪」身分再臨。'],
    ['伊斯瑪儀派', 540, 175, '什葉派', '在第七位伊瑪目的繼承上分出。曾建立法蒂瑪王朝（開羅）；今日的尼扎里派由阿迦汗領導，分布於全球。'],
    ['栽德派', 640, 175, '什葉派', '在第五位伊瑪目的繼承上分出，教義最接近遜尼派。主要在葉門北部。'],
    ['易巴德派', 290, 175, '哈瓦利吉派', '哈瓦利吉派中溫和的一支，是今日阿曼的主流派別，也見於北非部分地區。']];
  function initSects(root, cfg) {
    head(root, cfg.q); var view = el('div'), p; root.appendChild(view); p = info(root); var sel = 0;
    function draw() { var g = '', W = 680, H = 210;
      SECTS.forEach(function (s) { if (s[3]) { var par = SECTS.filter(function (x) { return x[0] === s[3]; })[0]; g += ln(par[1], par[2] + 14, s[1], s[2] - 14, 'var(--border)', 1.5); } });
      SECTS.forEach(function (s, i) { var w = s[0].length * 13 + 18, on = i === sel;
        g += '<g data-i="' + i + '" style="cursor:pointer"><rect x="' + n1(s[1] - w / 2) + '" y="' + (s[2] - 14) + '" width="' + n1(w) + '" height="28" rx="7" fill="' + (on ? 'var(--accent-soft)' : 'var(--surface)') + '" stroke="' + (on ? 'var(--accent)' : 'var(--border)') + '" stroke-width="1.5"/>' + tx(s[1], s[2] + 4, s[0], 12, 'currentColor') + '</g>'; });
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      view.querySelectorAll('[data-i]').forEach(function (c) { c.addEventListener('click', function () { sel = +c.getAttribute('data-i'); draw(); }); });
      p.innerHTML = '<b>' + SECTS[sel][0] + '</b>：' + SECTS[sel][4] + '<br><span style="font-size:0.88em;color:var(--text-muted)">點選圖中的方塊查看說明。比例為常見的約略估計。</span>'; }
    draw();
  }

  /* ---------- 3. 歷史時間軸 ---------- */
  var TLS = {
    is: { cats: { o: ['起源', '#2e7d4f'], e: ['帝國與王朝', '#3a6ea5'], c: ['文化與思想', '#b7791f'], m: ['近現代', '#8a3b3b'] },
      ev: [[570, 'o', '穆罕默德出生於麥加（約略年代）', '出身古萊什部落的哈希姆家族，幼年失去雙親，由祖父與伯父撫養。'],
        [610, 'o', '希拉山洞的第一次啟示', '傳統記載，四十歲左右的穆罕默德在麥加附近的山洞冥想時，聽到天使吉卜利勒傳達「你要宣讀」。'],
        [622, 'o', '遷徙（希吉拉）到麥地那', '在麥加受到迫害後，穆罕默德與追隨者遷往葉斯里卜（後稱麥地那），建立第一個穆斯林社群。伊斯蘭曆以這一年為元年。'],
        [630, 'o', '穆斯林進入麥加', '幾乎沒有流血就進入麥加，清除卡巴天房中的偶像。'],
        [632, 'o', '穆罕默德去世', '社群推舉艾布·伯克爾為第一位哈里發，繼承問題成為日後遜尼派與什葉派分歧的源頭。'],
        [650, 'c', '《古蘭經》奧斯曼定本（約略年代）', '第三任哈里發奧斯曼下令整理出統一的標準本，分送各大城市，其他異本被銷毀。'],
        [661, 'e', '伍麥亞王朝建立', '阿里遇刺後，穆阿威葉建立以大馬士革為首都的世襲王朝，版圖一度從西班牙延伸到中亞。'],
        [680, 'e', '卡爾巴拉事件', '阿里之子侯賽因與其家人在卡爾巴拉被伍麥亞軍隊殺害，成為什葉派認同的核心記憶。'],
        [750, 'e', '阿拔斯王朝取代伍麥亞', '首都遷往新建的巴格達。伍麥亞王族的倖存者逃到西班牙，建立後伍麥亞王朝（哥多華）。'],
        [830, 'c', '巴格達的智慧宮與翻譯運動（約略年代）', '大量希臘、波斯、印度的學術著作被譯成阿拉伯文；花拉子米寫出代數學的經典著作。'],
        [1095, 'e', '第一次十字軍東征開始', '1099 年十字軍攻下耶路撒冷；1187 年薩拉丁收復。十字軍運動持續到 1291 年。'],
        [1111, 'c', '安薩里去世', '這位神學家調和了正統教法與蘇菲修行，被尊為「伊斯蘭的證明」。'],
        [1258, 'e', '蒙古攻陷巴格達', '旭烈兀的軍隊屠城，阿拔斯哈里發被處死，常被視為古典伊斯蘭文明的終結點。'],
        [1273, 'c', '魯米去世', '波斯語的蘇菲詩人，著有《瑪斯納維》，他的追隨者形成以旋轉舞聞名的梅夫拉維道團。'],
        [1453, 'e', '鄂圖曼帝國攻陷君士坦丁堡', '改名伊斯坦堡，成為帝國首都。'],
        [1492, 'e', '格拉納達陷落', '伊比利半島最後的穆斯林政權結束，安達魯斯時代落幕。'],
        [1501, 'e', '薩法維王朝建立', '在伊朗以十二伊瑪目派什葉伊斯蘭為國教，奠定今日伊朗的宗教面貌。'],
        [1526, 'e', '蒙兀兒帝國建立', '巴布爾在印度建立帝國，阿克巴時期以宗教寬容聞名，留下泰姬瑪哈陵等建築。'],
        [1744, 'm', '瓦哈卜與紹德家族結盟', '提倡回歸早期伊斯蘭的改革運動與政治力量結合，日後成為沙烏地阿拉伯的基礎。'],
        [1924, 'm', '土耳其廢除哈里發制度', '鄂圖曼帝國在一戰後瓦解（1922），新成立的土耳其共和國廢除延續千年的哈里發。'],
        [1928, 'm', '穆斯林兄弟會成立', '哈桑·班納在埃及創立，是二十世紀政治伊斯蘭運動的重要源頭。'],
        [1979, 'm', '伊朗伊斯蘭革命', '何梅尼領導推翻巴勒維王朝，建立由教法學家監護的伊斯蘭共和國。'],
        [2001, 'm', '九一一事件', '激進組織蓋達發動攻擊。全球主要的穆斯林學者與組織都譴責恐怖主義，但伊斯蘭的形象從此常與暴力連在一起。']] },
    hi: { scale: [[-2600, 0], [-500, 0.25], [500, 0.45], [1200, 0.62], [1800, 0.8], [2000, 1]], cats: { o: ['起源與吠陀', '#2e7d4f'], t: ['經典與思想', '#b7791f'], e: ['王朝與社會', '#3a6ea5'], m: ['近現代', '#8a3b3b'] },
      ev: [[-2600, 'o', '印度河文明的成熟期（約略年代）', '哈拉帕、摩亨約達羅等城市有整齊的街道與排水系統；文字至今無法解讀，與後世印度教的關係仍有爭議。'],
        [-1500, 'o', '吠陀時代開始（約略年代）', '說印歐語的群體進入印度西北部；《梨俱吠陀》的頌歌在此後數百年間形成，以口傳保存。'],
        [-800, 't', '早期奧義書（約略年代）', '思想重心從外在的祭祀轉向內在的探問：「梵」與「我」的關係、業與輪迴、解脫。'],
        [-500, 'e', '佛陀與大雄的時代（約略年代）', '沙門運動興起，佛教與耆那教挑戰婆羅門祭祀與種姓的權威。'],
        [-268, 'e', '阿育王即位（約略年代）', '孔雀王朝的阿育王支持佛教，但也保護婆羅門與其他宗教。'],
        [0, 't', '兩大史詩與《摩奴法典》逐漸成形（約略年代）', '《摩訶婆羅多》（含《薄伽梵歌》）與《羅摩衍那》大約在西元前 4 世紀到西元 4 世紀之間寫定。'],
        [320, 'e', '笈多王朝（約 320～550 年）', '常被稱為古典印度教的黃金時代：往世書、神廟建築、梵文文學與數學都有重要發展。'],
        [788, 't', '商羯羅（傳統年代 788～820）', '吠檀多不二論的代表人物，據說在印度四方建立了修道院。'],
        [1010, 'e', '坦賈武爾大神廟完成', '南印度朱羅王朝興建的濕婆神廟，是印度最宏偉的神廟之一。'],
        [1137, 't', '羅摩努闍去世（傳統年代）', '提出「有限不二論」，為毗濕奴派的虔信提供哲學基礎。'],
        [1206, 'e', '德里蘇丹國建立', '北印度進入伊斯蘭政權統治的數百年，印度教與伊斯蘭文化長期共存與互動。'],
        [1469, 'e', '錫克教創始人那納克出生', '在印度教與伊斯蘭教之間開創新的信仰，主張一神與平等。'],
        [1574, 't', '杜勒西達斯寫作《羅摩功行之湖》（約略年代）', '用民間語言重述羅摩的故事，是北印度最受歡迎的宗教文學之一。'],
        [1828, 'm', '梵社成立', '羅姆·摩罕·羅易推動改革：反對寡婦殉葬、偶像崇拜，提倡理性的一神信仰。'],
        [1893, 'm', '辨喜在芝加哥世界宗教大會演講', '把吠檀多介紹給西方，也重塑了現代印度教的自我形象。'],
        [1947, 'm', '印巴分治與印度獨立', '分治造成大規模遷徙與暴力。1948 年甘地被一名印度教民族主義者刺殺。'],
        [1950, 'm', '印度憲法生效', '宣告廢除「不可接觸者」制度（第 17 條），並保障宗教自由；起草委員會主席是出身達利特的安貝德卡。'],
        [1966, 'm', '國際奎師那知覺協會（ISKCON）在紐約成立', '把對黑天的虔信帶到西方，就是街頭常見的「哈瑞奎師那」。'],
        [1992, 'm', '阿約提亞清真寺被拆毀', '印度教民族主義者主張該地是羅摩的出生地，引發全國性的宗教衝突；2024 年羅摩神廟在原址落成。']] } };
  function initTimeline(root, cfg) {
    head(root, cfg.q); var T = TLS[cfg.set], f = 'all', sel = 0, b = bar(root), view = el('div'), p;
    bt(b, '全部', 'all', function () { f = 'all'; mark(b, 'all'); draw(); });
    Object.keys(T.cats).forEach(function (k) { bt(b, T.cats[k][0], k, function () { f = k; mark(b, k); var i = T.ev.findIndex(function (e) { return e[1] === k; }); if (i >= 0) sel = i; draw(); }); });
    root.appendChild(view); p = info(root);
    function draw() { var W = 680, H = 120, y0 = T.ev[0][0], y1 = T.ev[T.ev.length - 1][0], L = 20, R = 20;
      var sc = T.scale || [[y0, 0], [y1, 1]];
      function sx(y) { var k = 1; while (k < sc.length - 1 && y > sc[k][0]) k++;   // 分段線性：古代壓縮、近代放大
        var a = sc[k - 1], c = sc[k], t = (y - a[0]) / (c[0] - a[0]); return L + (a[1] + t * (c[1] - a[1])) * (W - L - R); }
      var g = ln(L, 60, W - R, 60, 'var(--border)', 2);
      var ticks = cfg.set === 'is' ? [600, 800, 1000, 1200, 1400, 1600, 1800, 2000] : [-2000, -1000, 0, 1000, 1500, 1800, 1900, 2000];
      ticks.forEach(function (t) { if (t < y0 || t > y1) return; g += ln(sx(t), 56, sx(t), 64, 'var(--text-muted)', 1) + tx(sx(t), 80, t < 0 ? '前 ' + (-t) : t, 10, 'var(--text-muted)'); });
      T.ev.forEach(function (e, i) { if (f !== 'all' && e[1] !== f) return; var c = T.cats[e[1]][1], on = i === sel;
        g += '<circle data-e="' + i + '" cx="' + n1(sx(e[0])) + '" cy="60" r="' + (on ? 8 : 5.5) + '" fill="' + c + '" stroke="' + (on ? 'currentColor' : 'none') + '" stroke-width="2" style="cursor:pointer"/>'; });
      var lx = 20; Object.keys(T.cats).forEach(function (k) { g += '<circle cx="' + lx + '" cy="104" r="5" fill="' + T.cats[k][1] + '"/>' + tx(lx + 9, 108, T.cats[k][0], 10, 'currentColor', 'start'); lx += 24 + T.cats[k][0].length * 11; });
      view.innerHTML = svgw('0 0 ' + W + ' ' + H, g);
      var nav = el('div'), pv = btn('◀ 上一則', 'prev'), nx = btn('下一則 ▶', 'nextE');
      pv.addEventListener('click', function () { step(-1); }); nx.addEventListener('click', function () { step(1); }); nav.appendChild(pv); nav.appendChild(nx); view.appendChild(nav);
      view.querySelectorAll('[data-e]').forEach(function (c) { c.addEventListener('click', function () { sel = +c.getAttribute('data-e'); draw(); }); });
      var e = T.ev[sel]; p.innerHTML = '<b style="color:' + T.cats[e[1]][1] + '">' + (e[0] < 0 ? '西元前 ' + (-e[0]) : e[0]) + ' 年　' + e[2] + '</b><br>' + e[3]; }
    function step(d) { var k = sel; do { k = (k + d + T.ev.length) % T.ev.length; } while (f !== 'all' && T.ev[k][1] !== f); sel = k; draw(); }
    mark(b, 'all'); draw();
  }

  /* ---------- 4. 毗濕奴十化身 ---------- */
  var AVA = [['摩蹉', '魚', '大洪水時化身為魚，拯救人類始祖摩奴與吠陀經典。', '保存知識與生命'],
    ['俱利摩', '龜', '眾神與阿修羅攪拌乳海取甘露時，化身巨龜以背撐住當作攪棒的曼陀羅山。', '支撐世界的穩定'],
    ['筏羅訶', '野豬', '惡魔把大地拖入宇宙之海，毗濕奴化身野豬，用獠牙把大地托出水面。', '拯救大地'],
    ['那羅辛哈', '人獅', '惡魔王得到「不被人或獸、不在白天或夜晚、不在屋內或屋外殺死」的恩賜。毗濕奴化身半人半獅，在黃昏、門檻上將他撕裂，保護虔信的王子缽羅訶羅陀。', '保護虔信者，智慧勝過漏洞'],
    ['伐摩那', '侏儒', '化身侏儒婆羅門，向阿修羅王巴利乞求「三步之地」，隨即變成巨人，兩步跨越天地，第三步踩在巴利頭上。', '以謙卑化解傲慢'],
    ['持斧羅摩', '持斧的婆羅門', '手持斧頭的婆羅門戰士，消滅濫用權力的剎帝利國王。', '懲罰濫權'],
    ['羅摩', '理想的王子', '《羅摩衍那》的主角：被放逐森林、妻子悉多被魔王羅波那擄走，與猴神哈奴曼一同救回她。被視為「法」的典範。', '責任與正義'],
    ['黑天（克里希納）', '牧童與導師', '童年是調皮的牧童，青年與牧女嬉戲，在《摩訶婆羅多》中為阿周那駕車，說出《薄伽梵歌》。許多信徒視他為最高神本身。', '愛與智慧'],
    ['佛陀', '覺悟者', '多數中世紀以後的清單把佛陀列為第九個化身（有些清單改為黑天的哥哥大力羅摩）。這反映了印度教對佛教的吸納，佛教徒本身並不接受這種說法。', '慈悲（印度教的詮釋）'],
    ['迦爾吉', '騎白馬者', '尚未降臨的化身：在當前的「爭鬥時」結束時騎白馬、持劍出現，消滅邪惡，開啟新的循環。', '終結與更新']];
  function initAvatar(root, cfg) {
    head(root, cfg.q); var k = 0, b = bar(root), view = el('div'), p; root.appendChild(view); p = info(root);
    AVA.forEach(function (a, i) { bt(b, (i + 1) + '. ' + a[0], i, function () { k = i; mark(b, i); draw(); }); });
    function draw() { var g = '', W = 680;
      AVA.forEach(function (a, i) { var x = 34 + i * 68, on = i === k, h = 30 + i * 6;
        g += '<rect x="' + (x - 22) + '" y="' + (110 - h) + '" width="44" height="' + h + '" rx="6" fill="' + (on ? '#b7791f' : 'rgba(183,121,31,0.25)') + '"/>' + tx(x, 128, i + 1, 11, 'currentColor'); });
      g += tx(340, 18, '常見的「十化身」順序：從水中生物、動物、半人半獸，到人與未來的救世者', 10.5, 'var(--text-muted)');
      view.innerHTML = svgw('0 0 ' + W + ' 140', g);
      var a = AVA[k]; p.innerHTML = '<b>第 ' + (k + 1) + ' 化身：' + a[0] + '（' + a[1] + '）</b><br>' + a[2] + '<br><span style="color:var(--text-muted)">常見的象徵意義：' + a[3] + '</span>' +
        '<br><span style="font-size:0.88em;color:var(--text-muted)">有人把這個順序比喻成「生物演化」，但這是現代的詮釋，不是經典的原意。不同經典的化身清單與數目並不一致（《薄伽梵往世書》就列出 22 個以上）。</span>'; }
    mark(b, 0); draw();
  }

  /* ---------- 5. 人生四階段與四目標 ---------- */
  var STAGES = [['學生期', '約 8～25 歲', '跟隨老師學習吠陀與技藝，守貞，培養紀律。', [5, 1, 0, 1]],
    ['家住期', '約 25～50 歲', '結婚、工作、養育子女、供養其他三個階段的人。被許多經典稱為社會的支柱。', [4, 5, 4, 1]],
    ['林棲期', '約 50～75 歲', '把家業交給子女，逐漸退出世俗事務，轉向靈性修行（傳統上與配偶一同隱居森林）。', [4, 1, 0, 3]],
    ['遁世期', '75 歲以後', '放棄財產與社會身分，成為雲遊的修行者，專心追求解脫。', [3, 0, 0, 5]]];
  var AIMS = [['法', '責任、倫理、宇宙秩序', '#2e7d4f'], ['利', '財富、事業、權力', '#3a6ea5'], ['欲', '愛、享樂、美感', '#c0392b'], ['解脫', '脫離輪迴', '#b7791f']];
  function initAshrama(root, cfg) {
    head(root, cfg.q); var k = 1, b = bar(root), view = el('div'), p; root.appendChild(view); p = info(root);
    STAGES.forEach(function (s, i) { bt(b, s[0], i, function () { k = i; mark(b, i); draw(); }); });
    function draw() { var s = STAGES[k], g = '', W = 680;
      AIMS.forEach(function (a, i) { var y = 20 + i * 34, w = s[3][i] / 5 * 420;
        g += tx(150, y + 17, a[0] + '（' + a[1] + '）', 11, 'currentColor', 'end') + '<rect x="160" y="' + y + '" width="420" height="22" rx="4" fill="var(--border)" opacity="0.4"/>' +
          '<rect x="160" y="' + y + '" width="' + n1(w) + '" height="22" rx="4" fill="' + a[2] + '"/>'; });
      view.innerHTML = svgw('0 0 ' + W + ' 160', g);
      p.innerHTML = '<b>' + s[0] + '（' + s[1] + '）</b>：' + s[2] + '<br><span style="font-size:0.88em;color:var(--text-muted)">長條表示這個階段相對著重的目標（教學示意，不是經典給的數字）。' +
        '四階段是經典（特別是法論文獻）為上層種姓男性設計的理想模型，現實中很少人完整走完；「法」則貫穿每個階段，規範追求利與欲的方式。</span>'; }
    mark(b, 1); draw();
  }

  function initAll() { document.querySelectorAll('.rl-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ hijri: initHijri, sects: initSects, timeline: initTimeline, avatar: initAvatar, ashrama: initAshrama })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def rlw(cfg, maxw=700):
    return wdg("rl-w", cfg, maxw)


islesson = make_lesson(u"☪️", IS_NOTE, RLLIB, "rl-w")
hilesson = make_lesson(u"🕉️", HI_NOTE, RLLIB, "rl-w")
