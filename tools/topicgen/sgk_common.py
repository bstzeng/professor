# -*- coding: utf-8 -*-
"""〈日本戰國時代〉（sgk_）共用：課程包裝與 SGLIB 勢力版圖互動元件（class="sg-w"）。

  map   勢力版圖時間軸：1560～1615 年，各時期主要大名的勢力範圍（以現代都府縣近似舊國）
"""
import json
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS
from jpp_geo import JP_PATHS, JP_VB
from geo_common import centroid

SG_NOTE = u"本課程以通俗的歷史敘述為主，人物的言行與數字有不少來自後世的軍記物語與傳說，課程中會盡量標明。勢力圖以現代都府縣近似當時的「國」，只能呈現大致的勢力範圍。"
F = D

FAC = {
    "oda": (u"織田", "#d64541"), "toyo": (u"豐臣（羽柴）", "#e67e22"), "toku": (u"德川", "#d4ac0d"), "takeda": (u"武田", "#8e44ad"),
    "uesugi": (u"上杉", "#3498db"), "hojo": (u"北條", "#1abc9c"), "imagawa": (u"今川", "#a0522d"), "saito": (u"齋藤", "#6c5ce7"),
    "asakura": (u"淺井・朝倉", "#5d6d7e"), "miyoshi": (u"三好", "#2c3e50"), "honganji": (u"本願寺（一向一揆）", "#f1948a"), "mori": (u"毛利", "#1e8449"),
    "amago": (u"尼子", "#85929e"), "chosokabe": (u"長宗我部", "#c39bd3"), "otomo": (u"大友", "#5dade2"), "ryuzoji": (u"龍造寺", "#76d7c4"),
    "shimazu": (u"島津", "#1b2631"), "date": (u"伊達", "#6e2c00"), "east": (u"東軍（德川方）", "#d4ac0d"), "west": (u"西軍（石田・毛利方）", "#2471a3"),
    "shogun": (u"幕府直轄・親藩・譜代", "#d4ac0d"), "tozama": (u"外樣大名", "#7fb3d5"), "ezo": (u"蝦夷地（不在大名體制內）", "#eef0f2"),
}


def _m(**kw):
    out = {}
    for fac, codes in kw.items():
        for c in codes.split():
            out[c] = fac
    out.setdefault("01", "ezo")
    return out


STEPS = [
    (1560, u"桶狹間之戰前後", u"群雄割據：今川義元是東海道最強的大名，卻在桶狹間被織田信長奇襲身亡。三好長慶控制京都周邊，毛利元就剛併吞周防、長門。",
     _m(oda="23", imagawa="22", saito="21", takeda="19 20", uesugi="15", hojo="11 13 14", asakura="18", honganji="17",
        miyoshi="26 27 29 36 37", amago="31 32", mori="34 35", otomo="40 43 44", ryuzoji="41", shimazu="46", date="06"), 15),
    (1570, u"信長上洛之後", u"信長擁立足利義昭進入京都（1568），控制尾張、美濃、伊勢與近畿。德川家康取得遠江；武田信玄攻佔駿河。這一年，信長在姊川擊敗淺井・朝倉聯軍，石山合戰也揭開序幕。",
     _m(oda="21 23 24 26 27 29", toku="22", takeda="10 19 20", uesugi="15", hojo="11 13 14", asakura="18 25", honganji="17",
        miyoshi="36 37", mori="31 32 34 35", chosokabe="39", otomo="40 43 44", ryuzoji="41", shimazu="46", date="06"), 18),
    (1575, u"長篠之戰", u"淺井、朝倉在 1573 年滅亡，室町幕府也實質結束。1575 年，織田・德川聯軍在長篠以鐵砲重創武田勝賴。毛利成為信長在西國的最大對手。",
     _m(oda="18 21 23 24 25 26 27 29", toku="22", takeda="10 19 20", uesugi="15", hojo="11 13 14", honganji="17",
        mori="31 32 34 35", chosokabe="39", otomo="40 43 44", ryuzoji="41", shimazu="46", date="06"), 19),
    (1582, u"本能寺之變", u"信長在三月消滅武田，勢力達到頂點；六月卻在京都本能寺被明智光秀所殺。此時羽柴秀吉正在備中圍攻毛利，長宗我部幾乎統一四國，島津在九州急速擴張。",
     _m(oda="10 16 17 18 19 20 21 23 24 25 26 27 28 29 31 33", toku="22", uesugi="15", hojo="11 13 14", mori="32 34 35",
        chosokabe="36 37 39", otomo="40 44", ryuzoji="41 42 43", shimazu="45 46", date="06"), 22),
    (1585, u"秀吉成為關白", u"秀吉在山崎、賤岳擊敗對手，繼承信長的霸業，1585 年就任關白，並征服四國與越中。德川家康取得甲斐、信濃，與秀吉和解。九州則幾乎被島津統一。",
     _m(toyo="16 17 18 21 23 24 25 26 27 28 29 30 31 33 36 37 38", toku="19 20 22", uesugi="15", hojo="10 11 13 14", mori="32 34 35",
        chosokabe="39", otomo="40 44", ryuzoji="41 42", shimazu="43 45 46", date="06 07"), 26),
    (1590, u"天下統一", u"秀吉在 1587 年降伏島津，1590 年圍攻小田原滅北條，奧州諸大名也臣服，日本歸於統一。德川家康被移封到關東八州，以江戶為據點。",
     _m(toyo="02 03 05 07 08 09 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 33 36 37 38 40 41 42 43 44 45", toku="10 11 12 13 14",
        uesugi="15", mori="31 32 34 35", chosokabe="39", shimazu="46", date="04 06"), 26),
    (1600, u"關原之戰", u"秀吉死後，德川家康與石田三成對立。1600 年 9 月 15 日，東軍與西軍在美濃關原決戰，小早川秀秋倒戈，東軍一日之內大勝。圖中以各地大名的主要立場近似表示。",
     _m(east="04 06 09 10 11 12 13 14 15 16 17 19 20 22 23 36 38 40 43", west="07 18 21 25 26 27 28 29 30 31 32 33 34 35 39 46"), 31),
    (1615, u"大坂之陣後：江戶幕府", u"家康在 1603 年成為征夷大將軍，1615 年大坂夏之陣滅豐臣家。全國分為幕府直轄、親藩、譜代與外樣大名，外樣大名多被配置在遠離江戶的地方。",
     _m(shogun="08 09 10 11 12 13 14 15 18 19 20 21 22 23 25 26 27 29",
        tozama="02 03 04 05 06 07 16 17 24 28 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46"), 33),
]

_C = {c: centroid(p) for c, p in JP_PATHS.items() if c != "47"}


def _labels(m):
    groups = {}
    for c, f in m.items():
        if f in ("ezo",) or c not in _C:
            continue
        groups.setdefault(f, []).append(c)
    out = []
    for f, cs in groups.items():
        if f in ("east", "west", "shogun", "tozama"):
            continue
        xs = [_C[c][0] for c in cs]
        ys = [_C[c][1] for c in cs]
        out.append([f, int(sum(xs) / len(xs)), int(sum(ys) / len(ys))])
    return out


DATA = {
    "vb": JP_VB, "paths": {c: p for c, p in JP_PATHS.items() if c != "47"},
    "fac": {k: list(v) for k, v in FAC.items()},
    "steps": [{"y": y, "t": t, "d": d, "m": m, "L": L, "lab": _labels(m)} for (y, t, d, m, L) in STEPS],
}

SGLIB = r"""
(function () {
  if (window.__sgLib) return; window.__sgLib = 1;
""" + BASEJS + r"""
  var DATA = """ + json.dumps(DATA, ensure_ascii=False, separators=(",", ":")) + r""";
  function initMap(root, cfg) { head(root, cfg.q); var i = cfg.s || 0, bar = el('div', 'margin:4px 0'), v = el('div'), lg = el('div', 'margin-top:6px;font-size:0.85em;line-height:1.9'), inf = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em');
    root.appendChild(bar); DATA.steps.forEach(function (s, k) { var b = btn(String(s.y), k); b.onclick = function () { i = k; draw(); }; bar.appendChild(b); });
    var nav = el('div', 'margin:4px 0'), pv = btn('← 前一個時期'), nx = btn('下一個時期 →'); nav.appendChild(pv); nav.appendChild(nx); root.appendChild(nav);
    pv.onclick = function () { i = Math.max(0, i - 1); draw(); }; nx.onclick = function () { i = Math.min(DATA.steps.length - 1, i + 1); draw(); };
    root.appendChild(v); root.appendChild(lg); root.appendChild(inf);
    function draw() { mark(bar, i); var s = DATA.steps[i], g = '', used = {};
      Object.keys(DATA.paths).forEach(function (c) { var f = s.m[c] || null, col = f ? DATA.fac[f][1] : '#d5d8dc'; used[f || 'other'] = 1;
        g += '<path d="' + DATA.paths[c] + '" fill="' + col + '" stroke="var(--surface)" stroke-width="0.7"><title>' + (f ? DATA.fac[f][0] : '其他勢力') + '</title></path>'; });
      s.lab.forEach(function (l) { g += '<text x="' + l[1] + '" y="' + l[2] + '" font-size="13" font-weight="bold" text-anchor="middle" fill="var(--text)" stroke="var(--surface)" stroke-width="3" paint-order="stroke">' + DATA.fac[l[0]][0].split('（')[0] + '</text>'; });
      g += '<text x="20" y="40" font-size="30" font-weight="bold" fill="var(--text)" opacity="0.8">' + s.y + ' 年</text><text x="20" y="64" font-size="15" fill="var(--text-muted)">' + s.t + '</text>';
      v.innerHTML = svgw('0 0 ' + DATA.vb[0] + ' ' + DATA.vb[1], g);
      lg.innerHTML = Object.keys(used).map(function (f) { var n = f === 'other' ? '其他勢力・小大名' : DATA.fac[f][0], c = f === 'other' ? '#d5d8dc' : DATA.fac[f][1];
        return '<span style="display:inline-block;margin-right:12px;white-space:nowrap"><span style="display:inline-block;width:12px;height:12px;border-radius:2px;vertical-align:-1px;margin-right:4px;border:1px solid var(--border);background:' + c + '"></span>' + n + '</span>'; }).join('');
      inf.innerHTML = '<b>' + s.y + ' 年｜' + s.t + '</b>（第 ' + s.L + ' 課）<br>' + s.d + '<br><span style="color:var(--text-muted);font-size:0.9em">以現代都府縣近似當時的「國」，一個縣內常有多個勢力，圖中只標示主要的一方；沖繩（當時的琉球王國）未列入。</span>'; }
    draw(); }
  function boot() { document.querySelectorAll('.sg-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); if (cfg.t === 'map') initMap(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def sgw(t=u"map", q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("sg-w", cfg)


def make(icon=u"🏯", note=SG_NOTE):
    return make_with(icon, note, [("sg-w", SGLIB)])


lesson = make()
