# -*- coding: utf-8 -*-
"""〈羅馬帝國興衰〉（rom_）共用：課程包裝與 RMLIB 疆域地圖互動元件（class="rm-w"）。

  map   疆域變化：從公元前 264 年到 1453 年，九個時期的羅馬（與拜占庭）疆域
疆域以手繪的近似多邊形表示，再以陸地輪廓裁切；只能呈現大致的範圍。
"""
import json
from md_common import make_with
from cc_common import wdg, LS, M, D, KATEX
from qt_common import BASEJS
from rom_geo import ROM_VB, ROM_PROJ, ROM_LAND

RM_NOTE = u"本課程以通俗的歷史敘述為主；古代的人口、兵力與傷亡數字多半是估計，不同的史料與學者常有很大的差異。疆域地圖以近似的範圍表示，邊界並不精確。"
F = D

_LON0, _LAT1, _C, _K = ROM_PROJ


def _xy(lon, lat):
    return ((lon - _LON0) * _C * _K, (_LAT1 - lat) * _K)


R = {
    "ita_s": [(9.5, 44.4), (12.6, 44.1), (14.5, 42.0), (19.0, 40.3), (18.5, 39.3), (16.8, 37.6), (15.5, 38.4), (11.0, 42.0), (9.6, 43.4)],
    "ita_n": [(6.6, 46.2), (10.5, 46.6), (13.8, 46.6), (13.9, 45.6), (12.4, 44.2), (9.5, 44.4), (7.5, 43.8), (6.6, 44.2)],
    "sicily": [(12.0, 38.4), (15.8, 38.4), (15.5, 36.4), (12.0, 37.4)],
    "sardcor": [(7.8, 43.2), (10.2, 43.2), (10.2, 38.7), (7.8, 38.7)],
    "hisp_e": [(-7.5, 36.0), (3.5, 36.0), (3.5, 42.5), (0.5, 42.8), (-1.5, 41.5), (-4.0, 39.5), (-7.5, 38.0)],
    "hisp_w": [(-10.5, 36.5), (-7.5, 36.0), (-7.5, 38.0), (-4.0, 39.5), (-1.5, 41.5), (0.5, 42.8), (-1.8, 43.6), (-10.5, 44.2)],
    "hisp_se": [(-6.2, 36.0), (-0.5, 37.4), (-0.2, 38.8), (-2.0, 38.0), (-5.5, 37.0)],
    "gaul_s": [(3.0, 42.4), (7.6, 43.7), (7.0, 45.5), (5.0, 46.0), (2.0, 44.0)],
    "gaul": [(-5.5, 48.8), (-1.0, 50.2), (2.2, 51.2), (4.0, 52.0), (6.0, 51.9), (8.2, 49.0), (7.6, 47.6), (6.0, 46.4), (7.0, 45.5), (5.0, 46.0), (2.0, 44.0), (1.0, 42.8), (-1.8, 43.4), (-2.5, 47.0)],
    "brit": [(-6.0, 49.8), (1.9, 50.9), (2.0, 53.0), (-1.5, 55.1), (-3.5, 55.0), (-5.3, 54.5), (-5.3, 51.5)],
    "afr": [(8.2, 37.6), (11.5, 37.6), (11.5, 34.0), (8.2, 34.5)],
    "numid": [(5.0, 37.2), (8.2, 37.6), (8.2, 34.5), (5.0, 34.5)],
    "afr_w": [(-9.5, 35.9), (5.0, 37.2), (5.0, 34.5), (3.0, 34.0), (-5.0, 33.5), (-9.5, 32.5)],
    "tripol": [(11.5, 34.0), (19.0, 33.5), (19.0, 30.6), (11.5, 31.8)],
    "cyren": [(19.0, 33.5), (25.0, 33.5), (25.0, 30.6), (19.0, 30.6)],
    "egypt": [(25.0, 31.8), (34.2, 31.8), (34.9, 29.5), (33.5, 24.0), (31.5, 24.0), (30.0, 29.0), (25.0, 30.6)],
    "levant": [(34.2, 31.3), (35.0, 29.5), (37.0, 31.0), (40.0, 34.5), (38.5, 37.0), (36.0, 36.9), (35.6, 35.2)],
    "arabia": [(35.0, 29.5), (37.0, 31.0), (38.0, 28.5), (35.0, 27.5)],
    "anat_w": [(26.0, 40.5), (25.5, 36.5), (29.5, 36.2), (30.5, 38.5), (29.5, 40.2), (27.5, 40.5)],
    "anat_n": [(29.0, 41.3), (35.5, 42.1), (36.5, 41.0), (33.0, 39.5), (31.0, 38.5), (30.5, 38.5), (29.5, 40.2)],
    "cilicia": [(29.5, 36.2), (36.2, 36.0), (36.2, 37.3), (32.0, 37.2), (30.5, 37.0)],
    "anat": [(26.0, 40.5), (25.5, 36.5), (36.2, 36.0), (38.5, 37.0), (40.5, 37.5), (41.8, 41.5), (41.5, 41.7), (29.0, 41.3)],
    "greece": [(19.3, 41.8), (21.5, 42.2), (24.5, 41.6), (24.8, 40.8), (26.0, 40.0), (26.5, 36.0), (21.5, 36.2), (19.3, 39.6)],
    "crete": [(23.4, 34.8), (26.4, 34.8), (26.4, 35.8), (23.4, 35.8)],
    "cyprus": [(32.2, 34.5), (34.7, 34.5), (34.7, 35.8), (32.2, 35.8)],
    "illyr": [(13.5, 45.6), (16.0, 46.0), (19.5, 44.0), (21.5, 42.2), (19.3, 41.8), (19.0, 41.5), (15.0, 44.0), (13.6, 45.0)],
    "dan_w": [(9.0, 47.6), (10.0, 48.5), (13.0, 48.6), (16.5, 48.2), (18.8, 47.8), (19.3, 46.0), (19.5, 44.0), (16.0, 46.0), (13.5, 45.6), (13.8, 46.6), (10.5, 46.6), (9.5, 47.0)],
    "dan_e": [(19.3, 46.0), (20.5, 44.8), (22.5, 44.5), (25.0, 43.8), (28.5, 44.2), (29.7, 45.2), (28.5, 43.0), (25.5, 42.5), (23.0, 42.0), (21.5, 42.2), (19.5, 44.0)],
    "thrace": [(23.0, 42.0), (25.5, 42.5), (28.0, 42.5), (29.2, 41.2), (26.2, 40.6), (24.5, 41.0)],
    "dacia": [(21.0, 45.0), (22.0, 47.0), (24.0, 47.7), (26.5, 46.5), (25.0, 45.5), (24.5, 43.8), (22.5, 44.5), (21.0, 44.8)],
    "agri": [(7.6, 47.6), (9.0, 47.6), (10.5, 48.8), (9.5, 50.2), (8.2, 50.3), (8.2, 49.0)],
    "mesop": [(38.5, 37.0), (40.5, 37.5), (44.5, 34.0), (48.0, 30.0), (47.0, 29.5), (43.0, 31.5), (40.0, 34.5)],
    "armen": [(40.5, 37.5), (41.8, 41.5), (46.0, 41.0), (45.0, 38.5), (43.0, 37.5)],
    "const": [(27.6, 41.6), (29.3, 41.4), (29.3, 40.8), (27.8, 40.9)],
    "morea": [(21.0, 36.3), (23.5, 36.3), (23.5, 38.4), (21.0, 38.4)],
}

FAC = {"rome": (u"羅馬", "#b03a2e"), "west": (u"西羅馬", "#b03a2e"), "east": (u"東羅馬（拜占庭）", "#7d3c98")}

_REP = "ita_s"
_133 = "ita_s ita_n sicily sardcor hisp_e afr greece anat_w"
_44 = _133 + " gaul_s gaul hisp_w numid tripol cyren levant anat_n cilicia crete cyprus illyr"
_14 = "ita_s ita_n sicily sardcor hisp_e hisp_w gaul_s gaul afr numid tripol cyren egypt levant anat greece crete cyprus illyr dan_w dan_e"
_117 = _14 + " brit afr_w thrace dacia agri arabia mesop armen"
_W395 = "ita_s ita_n sicily sardcor hisp_e hisp_w gaul_s gaul brit afr numid afr_w tripol illyr dan_w"
_E395 = "greece thrace dan_e anat levant arabia egypt cyren crete cyprus"
_J555 = _E395 + " ita_s ita_n sicily sardcor afr numid tripol illyr hisp_se"


def _m(**kw):
    out = {}
    for fac, regs in kw.items():
        for r in regs.split():
            out[r] = fac
    return out


STEPS = [
    (u"前 264", u"第一次布匿戰爭前夕", u"羅馬已統一義大利半島的中南部，以同盟網絡控制各城市。西西里與海上的霸權，屬於北非的迦太基。", _m(rome=_REP), 4),
    (u"前 133", u"格拉古兄弟的時代", u"擊敗迦太基與馬其頓後，羅馬成為地中海的霸主：西班牙、北非、希臘、小亞細亞西部都成為行省。財富湧入，社會的矛盾也開始爆發。", _m(rome=_133), 9),
    (u"前 44", u"凱撒遇刺", u"凱撒征服高盧，龐培平定東方（敘利亞、猶太），羅馬的疆域橫跨地中海。共和國的制度卻已無法統治這麼大的帝國。", _m(rome=_44), 14),
    (u"公元 14", u"奧古斯都去世", u"奧古斯都併入埃及，把邊界推到多瑙河，建立了元首制。他留下遺言：不要再擴張。", _m(rome=_14), 16),
    (u"公元 117", u"圖拉真時代：最大疆域", u"圖拉真征服達契亞與美索不達米亞，帝國達到最大的版圖，人口約五、六千萬。他的繼任者哈德良隨即放棄了美索不達米亞。", _m(rome=_117), 19),
    (u"公元 395", u"東西分治", u"狄奧多西一世死後，帝國由兩個兒子分治：西部以米蘭（後來是拉溫納）為中心，東部以君士坦丁堡為中心。從此再也沒有統一。", _m(west=_W395, east=_E395), 28),
    (u"公元 476", u"西羅馬滅亡", u"日耳曼將領奧多亞塞廢黜了西羅馬的最後一位皇帝。西部分裂成哥德、法蘭克、汪達爾等王國；東羅馬繼續存在。", _m(east=_E395), 33),
    (u"公元 555", u"查士丁尼的收復", u"東羅馬皇帝查士丁尼收復了北非、義大利與西班牙南部，短暫地重現了「羅馬的地中海」，但代價是國力的耗竭與瘟疫。", _m(east=_J555), 36),
    (u"1453", u"君士坦丁堡陷落前夕", u"經過伊斯蘭的擴張、十字軍與鄂圖曼的興起，拜占庭只剩下君士坦丁堡與希臘南部的一小塊土地。1453 年，城市被鄂圖曼攻陷。", _m(east="const morea"), 39),
]

CITIES = [(u"羅馬", 12.5, 41.9), (u"迦太基", 10.3, 36.85), (u"君士坦丁堡", 28.97, 41.0), (u"亞歷山卓", 29.9, 31.2), (u"雅典", 23.7, 37.98), (u"倫底紐姆", -0.1, 51.5), (u"拉溫納", 12.2, 44.4)]


def _path(pts):
    return "M" + "L".join("%d,%d" % tuple(round(v) for v in _xy(*p)) for p in pts) + "Z"


DATA = {
    "vb": ROM_VB, "land": ROM_LAND, "reg": {k: _path(v) for k, v in R.items()},
    "fac": {k: list(v) for k, v in FAC.items()},
    "city": [[n] + [round(v) for v in _xy(lo, la)] for n, lo, la in CITIES],
    "steps": [{"y": y, "t": t, "d": d, "m": m, "L": L} for (y, t, d, m, L) in STEPS],
}

RMLIB = r"""
(function () {
  if (window.__rmLib) return; window.__rmLib = 1;
""" + BASEJS + r"""
  var DATA = """ + json.dumps(DATA, ensure_ascii=False, separators=(",", ":")) + r""", SEQ = 0;
  function initMap(root, cfg) { head(root, cfg.q); var i = cfg.s || 0, id = 'rmclip' + (++SEQ), bar = el('div', 'margin:4px 0'), v = el('div'), lg = el('div', 'margin-top:6px;font-size:0.85em'), inf = el('div', 'margin-top:8px;padding:10px 12px;border-radius:8px;background:var(--accent-soft);line-height:1.7;font-size:0.93em');
    root.appendChild(bar); DATA.steps.forEach(function (s, k) { var b = btn(s.y, k); b.onclick = function () { i = k; draw(); }; bar.appendChild(b); });
    var nav = el('div', 'margin:4px 0'), pv = btn('← 前一個時期'), nx = btn('下一個時期 →'); nav.appendChild(pv); nav.appendChild(nx); root.appendChild(nav);
    pv.onclick = function () { i = Math.max(0, i - 1); draw(); }; nx.onclick = function () { i = Math.min(DATA.steps.length - 1, i + 1); draw(); };
    root.appendChild(v); root.appendChild(lg); root.appendChild(inf);
    function draw() { mark(bar, i); var s = DATA.steps[i], used = {}, g = '<defs><clipPath id="' + id + '"><path d="' + DATA.land + '"/></clipPath></defs>';
      g += '<rect width="' + DATA.vb[0] + '" height="' + DATA.vb[1] + '" fill="#dbe7f3"/><path d="' + DATA.land + '" fill="#e9e4d8" stroke="#c9c2b0" stroke-width="0.4"/><g clip-path="url(#' + id + ')">';
      Object.keys(s.m).forEach(function (r) { var f = s.m[r]; used[f] = 1; g += '<path d="' + DATA.reg[r] + '" fill="' + DATA.fac[f][1] + '" fill-opacity="0.78" stroke="none"/>'; });
      g += '</g>';
      DATA.city.forEach(function (c) { g += '<circle cx="' + c[1] + '" cy="' + c[2] + '" r="3" fill="#1b2631"/><text x="' + (c[1] + 5) + '" y="' + (c[2] - 4) + '" font-size="11" fill="#1b2631" stroke="#fff" stroke-width="2.5" paint-order="stroke">' + c[0] + '</text>'; });
      g += '<text x="14" y="34" font-size="26" font-weight="bold" fill="#1b2631" stroke="#fff" stroke-width="3" paint-order="stroke">' + s.y + ' 年</text><text x="14" y="56" font-size="14" fill="#34495e" stroke="#fff" stroke-width="3" paint-order="stroke">' + s.t + '</text>';
      v.innerHTML = svgw('0 0 ' + DATA.vb[0] + ' ' + DATA.vb[1], g);
      lg.innerHTML = Object.keys(used).map(function (f) { return '<span style="display:inline-block;margin-right:12px"><span style="display:inline-block;width:12px;height:12px;border-radius:2px;vertical-align:-1px;margin-right:4px;background:' + DATA.fac[f][1] + '"></span>' + DATA.fac[f][0] + '</span>'; }).join('');
      inf.innerHTML = '<b>' + s.y + ' 年｜' + s.t + '</b>（第 ' + s.L + ' 課）<br>' + s.d + '<br><span style="color:var(--text-muted);font-size:0.9em">疆域為近似範圍；許多地區（例如附庸國、邊境地帶）的歸屬並不明確。</span>'; }
    draw(); }
  function boot() { document.querySelectorAll('.rm-w').forEach(function (root) { if (root.__done) return; root.__done = 1;
    var cfg = JSON.parse(root.getAttribute('data-cfg')); if (cfg.t === 'map') initMap(root, cfg); }); }
  if (document.readyState === 'complete') boot(); else window.addEventListener('load', boot);
})();
"""


def rmw(t=u"map", q=u"", **cfg):
    cfg.update({"t": t, "q": q})
    return wdg("rm-w", cfg)


def make(icon=u"🏛️", note=RM_NOTE):
    return make_with(icon, note, [("rm-w", RMLIB)])


lesson = make()
