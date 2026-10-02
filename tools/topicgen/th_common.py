# -*- coding: utf-8 -*-
"""〈人類科技發展史〉共用工具：課程包裝、時間軸圖、互動元件（THLIB）。"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)
from fo_common import fig, _attr
from sa_common import cells

NOTE = (u"年代多為考古或文獻的<strong>大約值</strong>，新的發現常會把年代往前推；「誰最早發明」在許多案例上學界仍有不同看法，"
        u"本課採用通行說法並註明爭議。")

_XT = {"co": (u"computing-origins", u"計算機的起源"), "sf": (u"spaceflight", u"太空飛行"),
       "llm": (u"llm-models", u"大型語言模型"), "ch": (u"chinese-history", u"中國歷史"),
       "ad": (u"ancient-daily-life", u"穿越古代過一天"), "em": (u"electromagnetism", u"電磁學"),
       "np": (u"nobel-physics", u"諾貝爾物理獎"), "os": (u"os-dev", u"作業系統是怎麼寫出來的"),
       "net": (u"networking", u"網路"), "cs": (u"computer-science", u"計算機概論"),
       "hm": (u"human-organs", u"人體器官"), "tr": (u"train-driver", u"駕駛台灣的火車"),
       "fo": (u"flight-ops", u"一趟航班的幕後"), "ww2": (u"wwii", u"第二次世界大戰"), "chip": (u"chip-layout", u"晶片佈局")}


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


def XL(key, text=None):
    tid, name = _XT[key]
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def lesson(title_, desc, goals, body, why, point, check, nxt=None):
    """why：「為什麼在這時候、這裡出現」的分析。"""
    blocks = []
    for b in body:
        if isinstance(b, tuple) and b[0] == "FIGX":
            blocks.append(("fig", b[1], b[2], b[3]))
        else:
            blocks.append(b)
    blocks.append(("note", u"🤔 為什麼在這時候、這裡出現？", [("p", why)]))
    blocks.append(("note", u"🧭 這一課的重點", [("p", point)]))
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🔥 %s</p>' % NOTE))
    if any(isinstance(b, tuple) and b[0] == "raw" and 'class="th-w' in b[1] for b in blocks):
        blocks.insert(0, ("raw", u"<script>%s</script>" % THLIB))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def widget(cfg, maxw=680):
    return ("raw", u'<div class="th-w content-figure" style="text-align:left;max-width:%dpx;margin-left:auto;margin-right:auto" data-cfg="%s"></div>'
            % (maxw, _attr(cfg)))


def mtl(head, items, color=BLUE, h=150):
    """模組小時間軸：items = [(年代, 標籤)]，等距排列、上下交錯。"""
    n = len(items)
    x0, x1, y = 40, 600, 82
    out = [title(head), A(20, y, 624, y, color), P("M20 %d H620" % y, color, sw=2.5)]
    for i, (d, lab) in enumerate(items):
        x = x0 + (x1 - x0) * i / float(max(n - 1, 1))
        up = i % 2 == 0
        out.append(C(x, y, 5, color, "#fff", 2))
        out.append(P("M%g %g V%g" % (x, y + (-8 if up else 8), y + (-22 if up else 22)), MUTED, sw=1))
        if up:
            out += [T(x, y - 40, d, 9, MUTED), T(x, y - 27, lab, 10, TXT)]
        else:
            out += [T(x, y + 35, lab, 10, TXT), T(x, y + 48, d, 9, MUTED)]
    return svg(*out)


def MTL(head, items, cap, color=BLUE):
    return fig(mtl(head, items, color), 150, cap)


# ---------- 總時間軸資料：[西元年（負＝西元前）, 日期文字, 名稱, 課, 類別] ----------
# 類別：t 工具材料、f 食物農業、i 資訊通訊、e 能源動力、m 運輸、s 科學醫學、c 計算
EVENTS = [
    [-3300000, u"約 330 萬年前", u"最早的石器（洛梅奎）", 4, "t"],
    [-2600000, u"約 260 萬年前", u"奧杜韋石器", 4, "t"],
    [-1760000, u"約 176 萬年前", u"阿舍利手斧", 4, "t"],
    [-1000000, u"約 100 萬年前", u"用火的早期證據", 5, "e"],
    [-400000, u"約 40 萬年前", u"經常性用火", 5, "e"],
    [-64000, u"約 6.4 萬年前", u"弓箭", 6, "t"],
    [-45000, u"約 4.5 萬年前", u"洞穴壁畫、骨針", 7, "i"],
    [-18000, u"約 2 萬年前", u"陶器（中國仙人洞）", 9, "t"],
    [-9500, u"約 1.15 萬年前", u"農業開始（肥沃月彎）", 8, "f"],
    [-7000, u"西元前 7000 年", u"加泰土丘", 10, "f"],
    [-5000, u"西元前 5000 年", u"冶煉銅", 11, "t"],
    [-3500, u"西元前 3500 年", u"輪子與車", 13, "m"],
    [-3200, u"西元前 3200 年", u"楔形文字", 12, "i"],
    [-3000, u"西元前 3000 年", u"青銅器普及", 11, "t"],
    [-2560, u"西元前 2560 年", u"吉薩大金字塔", 15, "t"],
    [-1250, u"西元前 1250 年", u"甲骨文", 12, "i"],
    [-1200, u"西元前 1200 年", u"鐵器普及", 16, "t"],
    [-250, u"西元前 3 世紀", u"阿基米德", 17, "s"],
    [-221, u"西元前 221 年", u"秦統一度量衡", 20, "s"],
    [-100, u"西元前 1 世紀", u"安提基特拉機械", 18, "c"],
    [105, u"105 年", u"蔡倫改良造紙", 21, "i"],
    [132, u"132 年", u"張衡地動儀", 22, "s"],
    [628, u"628 年", u"婆羅摩笈多：零的運算", 26, "c"],
    [820, u"約 820 年", u"花拉子米《代數學》", 25, "c"],
    [868, u"868 年", u"《金剛經》雕版印本", 24, "i"],
    [1044, u"1044 年", u"《武經總要》火藥配方", 29, "e"],
    [1088, u"1088 年", u"蘇頌水運儀象台", 28, "s"],
    [1117, u"約 1117 年", u"航海羅盤的記載", 28, "m"],
    [1300, u"約 1300 年", u"歐洲機械鐘", 27, "s"],
    [1450, u"約 1450 年", u"古騰堡印刷機", 30, "i"],
    [1492, u"1492 年", u"哥倫布橫渡大西洋", 31, "m"],
    [1543, u"1543 年", u"哥白尼《天體運行論》", 33, "s"],
    [1609, u"1609 年", u"伽利略的望遠鏡", 32, "s"],
    [1656, u"1656 年", u"惠更斯擺鐘", 35, "s"],
    [1687, u"1687 年", u"牛頓《原理》", 34, "s"],
    [1712, u"1712 年", u"紐科門蒸汽機", 37, "e"],
    [1761, u"1761 年", u"哈里森航海鐘 H4", 35, "m"],
    [1769, u"1769 年", u"瓦特分離式冷凝器", 37, "e"],
    [1796, u"1796 年", u"琴納牛痘疫苗", 46, "s"],
    [1830, u"1830 年", u"利物浦—曼徹斯特鐵路", 39, "m"],
    [1831, u"1831 年", u"法拉第電磁感應", 41, "e"],
    [1844, u"1844 年", u"摩斯電報", 43, "i"],
    [1856, u"1856 年", u"柏塞麥煉鋼法", 45, "t"],
    [1876, u"1876 年", u"電話", 43, "i"],
    [1879, u"1879 年", u"愛迪生電燈", 42, "e"],
    [1886, u"1886 年", u"賓士汽車", 44, "m"],
    [1903, u"1903 年", u"萊特兄弟飛機", 44, "m"],
    [1913, u"1913 年", u"哈伯—博施法量產", 45, "f"],
    [1928, u"1928 年", u"青黴素", 46, "s"],
    [1942, u"1942 年", u"第一座核反應爐", 48, "e"],
    [1945, u"1945 年", u"ENIAC", 52, "c"],
    [1947, u"1947 年", u"電晶體", 49, "c"],
    [1953, u"1953 年", u"DNA 雙螺旋", 51, "s"],
    [1957, u"1957 年", u"史普尼克衛星", 50, "m"],
    [1958, u"1958 年", u"積體電路", 49, "c"],
    [1969, u"1969 年", u"登月、ARPANET", 50, "m"],
    [1971, u"1971 年", u"微處理器", 49, "c"],
    [1981, u"1981 年", u"IBM PC", 52, "c"],
    [1991, u"1991 年", u"全球資訊網公開", 52, "i"],
    [2007, u"2007 年", u"iPhone", 53, "i"],
    [2012, u"2012 年", u"深度學習突破", 54, "c"],
    [2017, u"2017 年", u"Transformer", 55, "c"],
    [2022, u"2022 年", u"ChatGPT", 55, "c"],
]

# 前置技術關係圖：id → [名稱, 課, 前置]
DEPS = {
    "fire": [u"用火", 5, []], "stone": [u"石器", 4, []], "lang": [u"語言與符號", 7, []],
    "agri": [u"農業與定居", 8, ["stone", "fire"]], "pot": [u"陶器與窯", 9, ["fire"]],
    "metal": [u"冶金", 11, ["pot", "fire"]], "write": [u"文字", 12, ["lang", "agri"]],
    "math": [u"數學與曆法", 14, ["write"]], "wheel": [u"輪子", 13, ["agri", "metal"]],
    "paper": [u"造紙", 21, ["write"]], "print": [u"印刷", 30, ["paper", "metal"]],
    "zero": [u"位值記數與零", 26, ["math"]], "glass": [u"玻璃與透鏡", 32, ["fire", "pot"]],
    "sci": [u"科學方法", 33, ["print", "math"]], "newton": [u"牛頓力學與微積分", 34, ["sci", "zero", "glass"]],
    "clock": [u"精密計時", 35, ["metal", "newton"]], "steam": [u"蒸汽機", 37, ["metal", "sci"]],
    "rail": [u"鐵路", 39, ["steam", "steel"]], "steel": [u"大量煉鋼", 45, ["metal", "sci"]],
    "em": [u"電磁學", 41, ["newton", "metal"]], "grid": [u"發電與電網", 42, ["em", "steam"]],
    "tele": [u"電報與電話", 43, ["em"]], "radio": [u"無線電", 43, ["em", "newton"]],
    "ice": [u"內燃機", 44, ["steel", "chem"]], "plane": [u"飛機", 44, ["ice", "newton"]],
    "chem": [u"化學工業", 45, ["sci"]], "qm": [u"量子力學", 49, ["em", "newton"]],
    "silicon": [u"高純度矽", 49, ["chem"]], "trans": [u"電晶體", 49, ["qm", "silicon", "grid"]],
    "ic": [u"積體電路", 49, ["trans"]], "comp": [u"電腦", 52, ["ic", "zero", "tele"]],
    "rocket": [u"火箭與衛星", 50, ["ice", "newton", "comp"]], "net": [u"網際網路", 52, ["comp", "tele"]],
    "relat": [u"相對論", 50, ["em", "newton"]], "gps": [u"GPS", 50, ["rocket", "clock", "relat", "radio"]],
    "battery": [u"鋰電池", 53, ["chem"]], "phone": [u"智慧型手機", 53, ["ic", "radio", "battery", "net", "gps"]],
    "data": [u"網路上的海量資料", 54, ["net", "phone"]], "gpu": [u"GPU 運算", 54, ["ic"]],
    "dl": [u"深度學習", 54, ["comp", "gpu", "data"]], "llm": [u"大型語言模型", 55, ["dl", "net"]],
}

THLIB = r"""
(function () {
  if (window.__thLib) return; window.__thLib = 1;
  function btn(t, k) { var b = document.createElement('button'); b.type = 'button'; b.textContent = t; if (k !== undefined) b.setAttribute('data-k', k);
    b.style.cssText = 'padding:4px 10px;margin:4px 6px 0 0;border-radius:8px;border:1px solid var(--border);background:var(--surface);color:var(--text);cursor:pointer;font:inherit;font-size:0.9em'; return b; }
  function head(root, q) { if (q) { var p = document.createElement('p'); p.style.margin = '0 0 8px'; p.innerHTML = q; root.appendChild(p); } }
  function el(tag, css, html) { var e = document.createElement(tag); if (css) e.style.cssText = css; if (html !== undefined) e.innerHTML = html; return e; }
  function n1(v) { return Math.round(v * 10) / 10; }
  function tx(x, y, s, sz, c, anc, ex) { return '<text x="' + n1(x) + '" y="' + n1(y) + '" font-size="' + sz + '" fill="' + (c || 'currentColor') + '" text-anchor="' + (anc || 'middle') + '" ' + (ex || '') + '>' + s + '</text>'; }
  function rc(x, y, w, h, f, s, ex) { return '<rect x="' + n1(x) + '" y="' + n1(y) + '" width="' + n1(w) + '" height="' + n1(h) + '" fill="' + (f || 'none') + '" stroke="' + (s || 'none') + '" ' + (ex || '') + '/>'; }
  function ln(x1, y1, x2, y2, c, w, ex) { return '<line x1="' + n1(x1) + '" y1="' + n1(y1) + '" x2="' + n1(x2) + '" y2="' + n1(y2) + '" stroke="' + c + '" stroke-width="' + (w || 1) + '" ' + (ex || '') + '/>'; }
  var CAT = { t: ['#e8a33d', '工具材料'], f: ['#5aa469', '食物農業'], i: ['#3a6ea5', '資訊通訊'], e: ['#e0605a', '能源動力'], m: ['#2a9d8f', '運輸'], s: ['#8e6bbf', '科學醫學'], c: ['#d17a9b', '計算'] };

  /* ---------- 總時間軸 ---------- */
  function initTL(root, cfg) {
    head(root, cfg.q); var E = cfg.e, NOW = 2026, mode = cfg.mode || 'log';
    var bar = el('div'); root.appendChild(bar); var view = el('div', 'margin-top:6px'); root.appendChild(view);
    var info = el('p', 'margin:6px 0 0;min-height:2.6em'); root.appendChild(info);
    var leg = el('div', 'font-size:0.82em;color:var(--text-muted);margin-top:4px'); root.appendChild(leg);
    leg.innerHTML = Object.keys(CAT).map(function (k) { return '<span style="white-space:nowrap;margin-right:10px"><span style="color:' + CAT[k][0] + '">●</span> ' + CAT[k][1] + '</span>'; }).join('');
    var MODES = [['log', '對數尺度：全部'], ['-3400000', '全部（等比例）'], ['-12000', '最近 1.2 萬年'], ['0', '西元以來'], ['1700', '1700 年以後'], ['1940', '1940 年以後']];
    MODES.forEach(function (m) { var b = btn(m[1], m[0]); b.addEventListener('click', function () { mode = m[0]; draw(); }); bar.appendChild(b); });
    function draw() {
      bar.querySelectorAll('button').forEach(function (b) { var on = b.getAttribute('data-k') === mode; b.style.background = on ? 'var(--accent-soft)' : 'var(--surface)'; b.style.fontWeight = on ? 'bold' : 'normal'; });
      var X0 = 20, X1 = 640, Y = 120, o = '', fx, ticks = [];
      if (mode === 'log') { var L = Math.log(3500000) / Math.LN10; fx = function (y) { var ago = Math.max(NOW - y, 1); return X0 + (1 - Math.log(ago) / Math.LN10 / L) * (X1 - X0); };
        [[1000000, '100 萬年前'], [100000, '10 萬年前'], [10000, '1 萬年前'], [1000, '1000 年前'], [100, '100 年前'], [10, '10 年前']].forEach(function (t) { ticks.push([fx(NOW - t[0]), t[1]]); }); }
      else { var s = +mode; fx = function (y) { return X0 + (y - s) / (NOW - s) * (X1 - X0); };
        var span = NOW - s, step = span > 1e6 ? 1e6 : span > 10000 ? 2000 : span > 1500 ? 500 : span > 200 ? 50 : 20;
        for (var t = Math.ceil(s / step) * step; t <= NOW; t += step) ticks.push([fx(t), t < -10000 ? Math.round((NOW - t) / 10000) + ' 萬年前' : t < 0 ? '前' + (-t) : String(t)]); }
      o += ln(X0, Y, X1, Y, '#888', 2);
      ticks.forEach(function (t) { o += ln(t[0], Y - 4, t[0], Y + 4, '#888') + tx(t[0], Y + 18, t[1], 9, 'var(--text-muted)'); });
      var vis = E.map(function (e, i) { return [fx(e[0]), i]; }).filter(function (p) { return p[0] >= X0 - 1 && p[0] <= X1 + 1; }).sort(function (a, b) { return a[0] - b[0]; });
      var rows = [-1e9, -1e9, -1e9, -1e9], shown = 0;
      vis.forEach(function (p, k) { var e = E[p[1]], c = CAT[e[4]][0], w = e[2].length * 11.5 + 6, r = -1;
        for (var j = 0; j < 4; j++) if (rows[j] < p[0] - w / 2 - 4) { r = j; break; }
        if (r >= 0) { rows[r] = p[0] + w / 2; var ly = r < 2 ? Y - 26 - r * 30 : Y + 46 + (r - 2) * 30;
          var anc = p[0] + w / 2 > 652 ? 'end' : p[0] - w / 2 < 6 ? 'start' : 'middle', lx = anc === 'end' ? Math.min(p[0] + 6, 656) : anc === 'start' ? Math.max(p[0] - 6, 4) : p[0];
          o += ln(p[0], Y, p[0], r < 2 ? ly + 4 : ly - 12, c, 1, 'opacity="0.5"') + tx(lx, ly, e[2], 11, c, anc); shown++; }
        o += '<circle data-i="' + p[1] + '" cx="' + n1(p[0]) + '" cy="' + Y + '" r="6" fill="' + c + '" stroke="#fff" stroke-width="1.5" style="cursor:pointer"/>'; });
      view.innerHTML = '<svg viewBox="0 0 660 230" style="width:100%;display:block;color:var(--text)">' + o + '</svg>';
      view.querySelectorAll('circle[data-i]').forEach(function (cEl) { cEl.addEventListener('click', function () { var e = E[+cEl.getAttribute('data-i')];
        info.innerHTML = '<b>' + e[1] + '</b>　' + e[2] + '　<a href="lesson-' + (e[3] < 10 ? '0' : '') + e[3] + '.html">→ 第 ' + e[3] + ' 課</a>'; }); });
      if (!info.innerHTML || info.getAttribute('data-auto')) { info.setAttribute('data-auto', '1');
        info.innerHTML = '畫面中有 <b>' + vis.length + '</b> 個事件（顯示 ' + shown + ' 個標籤；擠不下的只畫圓點）。點圓點看詳細與課程連結。' + (mode === '-3400000' ? '<br>⚠️ 等比例尺度下，幾乎所有發明都擠在最右邊的一小段——這就是「加速」。' : mode === 'log' ? '<br>對數尺度：每一大格代表「十倍時間」，才能把三百萬年和十年放在同一張圖上。' : ''); }
    }
    draw();
  }

  /* ---------- 蒸汽機：紐科門 vs 瓦特 ---------- */
  function initSteam(root, cfg) {
    head(root, cfg.q); var mode = 'newcomen', t = 0, strokes = 0, coal = 0, last = 0;
    var bar = el('div'); root.appendChild(bar); var view = el('div', 'margin-top:6px'); root.appendChild(view); var info = el('p', 'margin:6px 0 0;min-height:3em'); root.appendChild(info);
    [['newcomen', '紐科門機（1712）'], ['watt', '瓦特機（1769）']].forEach(function (m) { var b = btn(m[1], m[0]); b.addEventListener('click', function () { mode = m[0]; strokes = 0; coal = 0; }); bar.appendChild(b); });
    setInterval(function () { t += 0.11; var ph = (Math.sin(t) + 1) / 2, cyc = Math.floor((t + Math.PI / 2) / (2 * Math.PI));
      if (cyc !== last) { last = cyc; strokes++; coal += mode === 'newcomen' ? 3 : 1; }
      var down = Math.cos(t) < 0, o = '', W = mode === 'watt';
      var cool = !W && down, cylC = cool ? '#5b9bd5' : '#e0605a';
      o += rc(60, 150, 90, 50, '#555', 'none', 'rx="6"') + tx(105, 222, '鍋爐', 11) + ln(105, 150, 105, 130, '#999', 4);
      o += rc(70, 40, 70, 90, cylC, '#444', 'rx="3" opacity="0.75"') + tx(105, 30, '汽缸', 11);
      var py = 50 + ph * 60, yL = py - 30, yR = 2 * 40 - yL;
      o += rc(72, py, 66, 10, '#333') + ln(105, py, 105, yL, '#333', 4) + ln(105, yL, 495, yR, '#8a5a2b', 8) + '<polygon points="300,40 285,190 315,190" fill="#8a5a2b" opacity="0.8"/>';
      o += tx(300, 206, '橫梁支點', 11) + ln(495, yR, 495, yR + 40, '#333', 4) + rc(470, yR + 40, 50, 60, '#3a6ea5', 'none', 'opacity="0.5"') + tx(495, 224, '抽水幫浦', 11);
      if (W) { o += rc(170, 100, 60, 40, '#5b9bd5', '#444', 'rx="3"') + tx(200, 158, '冷凝器', 11) + ln(140, 110, 170, 110, '#999', 4); if (down) o += tx(200, 92, '❄ 蒸汽在這裡凝結', 10, '#3a6ea5'); }
      else if (cool) o += tx(105, 145, '❄ 噴冷水', 10, '#fff');
      o += tx(636, 176, '來回 ' + strokes + ' 次', 12, 'currentColor', 'end') + tx(636, 196, '燒煤 ' + coal + ' 單位', 12, '#e0605a', 'end');
      view.innerHTML = '<svg viewBox="0 0 640 230" style="width:100%;display:block;color:var(--text)">' + o + '</svg>';
      info.innerHTML = W ? '<b>瓦特機</b>：蒸汽被抽到旁邊<b>一直保持冰冷</b>的冷凝器裡凝結，汽缸本身<b>一直保持高溫</b>。不必每次重新加熱汽缸，同樣的工作大約只要三分之一的煤。'
        : '<b>紐科門機</b>：蒸汽推動活塞後，直接往<b>汽缸裡</b>噴冷水讓蒸汽凝結、形成真空，大氣壓把活塞壓下。每一次都把汽缸冷卻，下一次又要用新蒸汽把它燒熱——大量的煤浪費在「重新加熱汽缸」上（汽缸變藍＝被冷卻）。';
    }, 50);
  }

  /* ---------- 前置技術關係圖 ---------- */
  function initDeps(root, cfg) {
    head(root, cfg.q); var D = cfg.d, cur = cfg.start || 'phone';
    var bar = el('div'); root.appendChild(bar); var view = el('div', 'margin-top:8px;line-height:1.7;font-size:0.93em'); root.appendChild(view);
    (cfg.targets || ['phone', 'llm', 'gps', 'plane', 'comp']).forEach(function (k) { var b = btn(D[k][0], k); b.addEventListener('click', function () { cur = k; draw(); }); bar.appendChild(b); });
    function link(k) { var n = D[k][1]; return '<a href="lesson-' + (n < 10 ? '0' : '') + n + '.html">' + D[k][0] + '</a>'; }
    function draw() { bar.querySelectorAll('button').forEach(function (b) { var on = b.getAttribute('data-k') === cur; b.style.background = on ? 'var(--accent-soft)' : 'var(--surface)'; b.style.fontWeight = on ? 'bold' : 'normal'; });
      var seen = {}, all = {};
      function walk(k, d) { var h = '<div style="padding-left:' + (d * 18) + 'px">' + (d ? '└ ' : '🎯 ') + link(k);
        if (seen[k]) return h + ' <span style="color:var(--text-muted)">（見上）</span></div>'; seen[k] = 1; if (d) all[k] = 1; h += '<\/div>';
        D[k][2].forEach(function (c) { h += walk(c, d + 1); }); return h; }
      var tree = walk(cur, 0), keys = Object.keys(all).sort(function (a, b) { return D[a][1] - D[b][1]; });
      var roots = keys.filter(function (k) { return !D[k][2].length; }).map(function (k) { return D[k][0]; });
      var direct = D[cur][2].map(link).join('、');
      view.innerHTML = '<p style="margin:0 0 6px">「' + D[cur][0] + '」直接需要：' + direct + '。<br>往下一路追，總共至少牽涉 <b>' + keys.length + '</b> 項前置技術，最底層是：' + roots.join('、') + '。</p>' +
        '<div style="display:flex;flex-wrap:wrap;gap:4px">' + keys.map(function (k) { return '<span style="border:1px solid var(--border);border-radius:12px;padding:1px 8px;font-size:0.9em">' + link(k) + ' <span style="color:var(--text-muted)">第 ' + D[k][1] + ' 課</span></span>'; }).join('') + '</div>' +
        '<details style="margin-top:8px"><summary style="cursor:pointer">展開完整的樹狀依賴</summary>' + tree + '</details>'; }
    draw();
  }

  function initAll() { document.querySelectorAll('.th-w').forEach(function (w) { if (w.__d) return; w.__d = 1; var cfg = JSON.parse(w.getAttribute('data-cfg'));
    ({ tl: initTL, steam: initSteam, deps: initDeps })[cfg.t](w, cfg); }); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();
"""


def timeline(mode="log", q=u""):
    return widget({"t": "tl", "e": EVENTS, "mode": mode, "q": q})


def deps(start="phone", q=u"", targets=None):
    cfg = {"t": "deps", "d": DEPS, "start": start, "q": q}
    if targets:
        cfg["targets"] = targets
    return widget(cfg)
