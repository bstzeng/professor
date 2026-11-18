# -*- coding: utf-8 -*-
"""事故案例課的共用版型：一起事故＝一課（基本資料、背景、經過、原因、後續改進、一句話教訓）。"""
import re

DEFAULT_Q = [u"這起事故的直接原因是什麼？", u"有哪些因素讓情況惡化，或讓人得以生還？", u"事故之後，做了哪些改進？"]


def F(date, name, vehicle, place, toll, vlabel=u"車輛"):
    return [[u"日期", date], [u"事故", name], [vlabel, vehicle], [u"地點", place], [u"死傷", toll]]


def _plain(s):
    return re.sub(u"<[^>]+>", u"", s).replace(u"<", u"&lt;")


def make_case(lesson):
    def case(title, sub, facts, bg, steps, causes, fixes, moral, q=None, extra=None, status=None):
        body = [("t", [u"項目", u"內容"], facts)]
        if status:
            body.append(("note", u"調查進度", [("p", status)]))
        body += [("h", u"背景"), ("p", bg), ("h", u"經過"), ("ol", steps), ("h", u"原因"), ("ul", causes)]
        if extra:
            body += extra
        body += [("h", u"後續改進"), ("ul", fixes), ("note", u"一句話教訓", [("p", moral)])]
        point = _plain(u"%s（%s）。背景：%s 原因：%s。改進：%s。教訓：%s" % (title, sub, bg, u"；".join(causes), u"；".join(fixes), moral))
        goals = [u"了解%s的背景與經過" % title, u"理解調查認定的原因", u"認識事故之後的改進"]
        return lesson(title, sub, goals, body, point, q or DEFAULT_Q)
    return case
