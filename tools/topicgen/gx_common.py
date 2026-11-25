# -*- coding: utf-8 -*-
"""中國古典文學七門課（詩經、元曲戲曲、世說新語、孟子、孫子兵法、諸子百家、志怪與明清小說）共用的工具。"""
from cc_common import LS, make_lesson
from nv_common import NVLIB, nvw, node, ev, card, CR, CB, CG, CO, CP, CT, CY, CK  # noqa: F401

GX_NOTE = (u"原文以通行本為準，不同版本偶有異文；白話翻譯為意譯，力求貼近原意，"
           u"學界有不同解讀時會在課中註明。")


def X(tid, name, text=None):
    return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)


def mk(icon, note=None):
    return make_lesson(icon, note or GX_NOTE, NVLIB, "nv-w")


def Q(orig, trans=None, src=None):
    """原文引文：原文（襯線字）＋白話＋出處。"""
    h = (u'<blockquote style="margin:0 0 16px;padding:10px 14px;border-left:4px solid var(--accent);'
         u'background:var(--accent-soft);border-radius:var(--radius,6px)">'
         u'<div style="font-family:var(--font-serif,serif);font-size:1.08em;line-height:1.95">%s</div>' % orig)
    if trans:
        h += u'<div style="margin-top:6px;color:var(--text-muted);font-size:0.92em;line-height:1.7">白話：%s</div>' % trans
    if src:
        h += u'<div style="text-align:right;margin-top:4px;font-size:0.85em;color:var(--text-muted)">——%s</div>' % src
    return ("raw", h + u"</blockquote>")


def W(rows):
    """字詞注釋表。"""
    return ("t", [u"字詞", u"解釋"], rows)


def table(title, h1, desc, sections, file_="table.html", icon=u"📋"):
    body = []
    for h, head_, rows in sections:
        body += [("h", h), ("t", head_, rows)]
    return {"file": file_, "title": title, "h1": h1, "icon": icon, "description": desc, "body": body}
