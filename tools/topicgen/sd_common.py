# -*- coding: utf-8 -*-
"""看病指南：共用工具。

lesson() 每課結尾自動補上「本週就做這一件事」與一行健康教育聲明。
沿用其他主題的 SVG 小工具（box、flow、bars、line_chart…）。
"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, layout, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)

NOTE = (u"本課是<strong>一般衛教與就醫資訊</strong>，以台灣的醫療與健保制度為背景，<strong>不能取代醫師的診斷</strong>。"
        u"出現胸痛、呼吸困難、意識改變、疑似中風等緊急狀況，請直接撥打 119 或前往急診；"
        u"健保部分負擔、轉診與各項規定會調整，以衛生福利部與健保署最新公告為準。")


def lesson(title_, desc, goals, body, act, check, nxt=None):
    """act：「下次看病就用這一招」的內容（字串）。"""
    blocks = []
    for b in body:
        if isinstance(b, tuple) and b[0] == "FIGX":
            blocks.append(("fig", b[1], b[2], b[3]))
        else:
            blocks.append(b)
    blocks.append(("note", u"✅ 下次看病就用這一招", [("p", act)]))
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🩺 %s</p>' % NOTE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


_TOPICS = {
    "hr": (u"heart-rate-aerobic", u"心率與有氧運動"),
    "ho": (u"human-organs", u"人體器官運作機制"),
    "dm": (u"disease-mechanisms", u"疾病是怎麼形成的"),
    "um": (u"body-manual", u"人體使用手冊"),
}


def XL(key, n=None, text=None):
    """連到其他主題：XL("hr", 15, "談話測試") 或 XL("ho")（主題首頁）。"""
    tid, name = _TOPICS[key]
    if n is None:
        return u'<a href="../%s/index.html">%s</a>' % (tid, text or u"〈%s〉" % name)
    return u'<a href="../%s/lesson-%02d.html">%s</a>' % (tid, n, text or u"〈%s〉第 %d 課" % (name, n))


def fig(svgtext, h, cap):
    return ("FIGX", svgtext, "0 0 640 %d" % h, cap)


def why(text):
    """「為什麼」小框：連回機制。"""
    return ("note", u"🔬 背後的機制", [("p", text)])


def warn(items):
    """警訊清單：出現就該就醫。"""
    return ("note", u"⚠️ 出現這些情況，請就醫", [("ul", items)])
