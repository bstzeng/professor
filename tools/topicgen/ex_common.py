# -*- coding: utf-8 -*-
"""執行檔課程：共用工具（沿用檔案格式課的圖解與 Hex 工具）。"""
import struct
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, hexdump, hexfig, fig,
                        layout, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)
from gen import Lesson

SAFE = (u"本課用最小範例與觀察工具，說明執行檔的<strong>結構與載入原理</strong>，屬於系統知識與資安基礎；"
        u"不含惡意程式技術。手工打造的極小執行檔常被防毒軟體視為可疑，請只在自己的環境、用自己的檔案練習。")


def lesson(title_, desc, goals, body, tryit, check, fig=None, nxt=None):
    blocks = []
    for b in body:
        if b == "FIG":
            blocks.append(("fig", fig[0], fig[1], fig[2]))
        elif isinstance(b, tuple) and b[0] == "FIGX":
            blocks.append(("fig", b[1], b[2], b[3]))
        else:
            blocks.append(b)
    blocks.append(("note", u"動手試試", [("p", tryit)]))
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🔧 %s</p>' % SAFE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


def FMT(n, text):
    """連到姊妹課程《檔案格式解剖學》。"""
    return u'<a href="../file-formats/lesson-%02d.html">%s</a>' % (n, text)


# ---------- 手寫的 184 位元組 ELF（真的能執行） ----------
_MSG = u"你好，我是手寫的程式\n".encode("utf-8")
_CODE = (b"\xB8\x01\x00\x00\x00"
         b"\xBF\x01\x00\x00\x00"
         b"\x48\x8D\x35" + struct.pack("<i", 16) +
         b"\xBA" + struct.pack("<I", len(_MSG)) +
         b"\x0F\x05"
         b"\xB8\x3C\x00\x00\x00"
         b"\x31\xFF"
         b"\x0F\x05")
_BASE = 0x400000
_HDR = 64 + 56
_BODY = _CODE + _MSG
_TOTAL = _HDR + len(_BODY)
_EH = b"\x7fELF" + bytes([2, 1, 1, 0]) + b"\0" * 8 + struct.pack(
    "<HHIQQQIHHHHHH", 2, 0x3E, 1, _BASE + _HDR, 64, 0, 0, 64, 56, 1, 0, 0, 0)
_PH = struct.pack("<IIQQQQQQ", 1, 5, 0, _BASE, _BASE, _TOTAL, _TOTAL, 0x1000)
ELF = _EH + b"MTrk"[:0] + _PH + _BODY   # (no-op slice keeps formatting)
assert len(ELF) == 184 and ELF[:4] == b"\x7fELF"

import base64
ELF_URI = "data:application/octet-stream;base64," + base64.b64encode(ELF).decode("ascii")
