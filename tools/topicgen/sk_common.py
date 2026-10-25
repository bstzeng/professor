# -*- coding: utf-8 -*-
"""〈史蒂芬・金〉（sk_）共用：沿用 nv_common 的互動元件，另加基本資料與改編作品表格。"""
from nv_common import *

SK_NOTE = (u"本課程包含完整劇情（有暴雷）。書名以台灣通行譯名為主並附英文原名；尚無繁體中譯或譯名查不到的，標示「暫譯」。"
           u"劇情為作者自行整理的摘要，非原文引用。")

lesson = make_lesson(u"📕", SK_NOTE, NVLIB, "nv-w")


def info(*rows):
    """基本資料表：info(("出版", "1974"), ("中文譯名", "…"), …)"""
    return ("t", [u"項目", u"內容"], [[a, b] for a, b in rows])


def adapt(*rows):
    """改編作品表：adapt(("1976", "電影", "布萊恩・狄帕瑪", "說明"), …)"""
    return ("t", [u"年份", u"形式", u"主創", u"和原著的差異與評價"], [list(r) for r in rows])
