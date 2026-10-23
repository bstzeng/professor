# -*- coding: utf-8 -*-
"""〈魔術方塊〉共用工具。方塊模型 rb_core.js、3D 介面 rb_ui.js、兩階段求解器 rb_solver.js、相機工具 rb_scan.js
（公式與求解器都以 Node 驗證過：每個示範公式都會把起始狀態轉回復原）。"""
import json
import os
from cc_common import *

_DIR = os.path.dirname(os.path.abspath(__file__))


def _js(name):
    return open(os.path.join(_DIR, name), encoding="utf-8").read()


RB_NOTE = u"方塊配色以「白色在下、黃色在上、綠色朝前」為準（大部分市售方塊的標準配色）。每個 3D 示範都可以拖曳旋轉視角。"

_SOLVER = _js("rb_solver.js")
RBLIB = _js("rb_core.js") + "\n" + _js("rb_ui.js")
RBSOLVE = (_SOLVER + "\nwindow.__rbSolverSrc = " + json.dumps(_SOLVER).replace("</", "<\\/") + ";\n" + _js("rb_scan.js"))


def rbw(cfg, maxw=720):
    """3D 方塊元件：t = player（公式播放）/ notation（記號）/ free（自由轉＋電腦求解）/ net（展開圖）。"""
    return wdg("rb-w", cfg, maxw)


def play(alg, q=None, **k):
    cfg = {"t": "player", "alg": alg}
    if q:
        cfg["q"] = q
    cfg.update(k)
    return rbw(cfg)


SCAN = ("raw", u'<div class="rb-scan content-figure" style="text-align:left;max-width:720px;margin-left:auto;margin-right:auto"></div>')

_base = make_lesson(u"🧊", RB_NOTE, RBLIB, "rb-")


def rblesson(*a, **k):
    L = _base(*a, **k)
    # 方塊的 JS 裡有 \[ 之類的正規表示式，會被誤判成公式；只有正文真的有公式才載入 KaTeX
    text = repr([b for b in L.body if not (isinstance(b, tuple) and b[0] == "raw" and (b[1].startswith("<script>") or b[1] == KATEX))])
    if "\\\\(" not in text and "\\\\[" not in text:
        L.body = [b for b in L.body if b != ("raw", KATEX)]
    raws = [b[1] for b in L.body if isinstance(b, tuple) and b[0] == "raw"]
    if any('class="rb-scan' in r or "&quot;free&quot;" in r for r in raws):
        # 求解器與相機工具要放在 RBLIB 之後
        L.body.insert(1, ("raw", u"<script>%s</script>" % RBSOLVE))
    return L


def alg(s):
    return u'<code style="font-weight:700;white-space:nowrap">%s</code>' % s


def inv(s):
    """簡單公式的反公式（不含括號重複）。"""
    out = []
    for m in s.split():
        if m.endswith("2"):
            out.append(m)
        elif m.endswith("'"):
            out.append(m[:-1])
        else:
            out.append(m + "'")
    return " ".join(reversed(out))
