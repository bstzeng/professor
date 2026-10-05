# -*- coding: utf-8 -*-
"""諾貝爾醫學獎／經濟學獎共用工具：沿用物理獎、化學獎課程的版型（總表、逐年精讀六段式）。"""
from gen import Lesson
from cc_common import fig, D, M, LS
from fmt_common import (T, R, C, P, A, box, flow, svg, title, bars,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)

_DIG = u"〇一二三四五六七八九"


def cy(y):
    """2006 → 二〇〇六"""
    return u"".join(_DIG[int(c)] for c in str(y))


TOPICS = {"np": (u"nobel-physics", u"諾貝爾物理獎"), "nc": (u"nobel-chemistry", u"諾貝爾化學獎"),
          "nm": (u"nobel-medicine", u"諾貝爾生理學或醫學獎"), "ne": (u"nobel-economics", u"諾貝爾經濟學獎"),
          "body": (u"body-manual", u"人體使用手冊"), "organs": (u"human-organs", u"人體器官運作機制"),
          "stat": (u"statistics-doe", u"統計學與實驗設計"), "stock": (u"stock-investing", u"股票的本質"),
          "debt": (u"national-debt", u"國債是什麼"), "chaos": (u"chaos-theory", u"混沌理論"),
          "tc": (u"computability", u"計算理論"), "fp": (u"first-principles", u"第一性原理")}


def XT(key, note=u""):
    tid, name = TOPICS[key]
    return u'<a href="../%s/index.html">%s</a>%s' % (tid, name, (u"——" + note) if note else u"")


def _fix(body):
    return [("fig", b[1], b[2], b[3]) if isinstance(b, tuple) and b[0] == "FIGX" else b for b in body]


def lesson(title_, desc, goals, body, check, nxt=None):
    return Lesson(title_, desc, goals, _fix(body), check, nxt)


def Y(year, topic, goals, who, reason, field, what, before, timeline, gapnote, impact, links, check, nxt):
    """逐年精讀的六段式課程。what：段落清單；before：困境清單（最後可附一段 str 結語）；timeline：[(時間, 事件)]。"""
    body = [("h", u"1. 得獎者與官方獎項理由"),
            ("t", [u"項目", u"內容"], [[u"得獎者", who], [u"獎項理由", reason], [u"領域", field]]),
            ("h", u"2. 那到底是什麼")]
    body += [("p", x) if isinstance(x, str) else x for x in what]
    body.append(("h", u"3. 在此之前的困境"))
    items = [b for b in before if not b.startswith(u"§")]
    body.append(("ul", items))
    for b in before:
        if b.startswith(u"§"):
            body.append(("p", b[1:]))
    body += [("h", u"4. 從發現到獲獎的時間差"), ("t", [u"時間", u"事件"], [list(t) for t in timeline]), ("p", gapnote),
             ("h", u"5. 今天的影響"), ("ul", impact)]
    if links:
        body += [("h", u"6. 站上延伸連結"), ("ul", links)]
    return Lesson(u"%s年：%s" % (cy(year), topic), u"%d 年的得獎研究" % year, goals, body, check, nxt)
