# -*- coding: utf-8 -*-
"""人體使用手冊：共用工具。

lesson() 每課結尾自動補上「本週就做這一件事」與一行健康教育聲明。
沿用其他主題的 SVG 小工具（box、flow、bars、line_chart…）。
"""
from gen import Lesson
from fmt_common import (T, R, C, E, P, A, box, flow, svg, title, layout, mono, bars, line_chart,
                        RED, BLUE, GREEN, ORANGE, ACC, GOLD, MUTED, LINE, TXT, PURPLE, TEAL, GRAY)

NOTE = (u"本課是<strong>一般健康教育</strong>，整理自世界衛生組織（WHO）、台灣國民健康署與各大醫學會的公開指引，"
        u"<strong>不能取代個人的醫療建議</strong>。有慢性病、正在服藥、懷孕，或出現文中提到的警訊時，請先和醫師討論；"
        u"各項篩檢與補助的年齡、頻率會調整，以最新公告為準。")


def lesson(title_, desc, goals, body, act, check, nxt=None):
    """act：「本週就做這一件事」的內容（字串）。"""
    blocks = []
    for b in body:
        if isinstance(b, tuple) and b[0] == "FIGX":
            blocks.append(("fig", b[1], b[2], b[3]))
        else:
            blocks.append(b)
    blocks.append(("note", u"✅ 本週就做這一件事", [("p", act)]))
    blocks.append(("raw", u'<p style="color:var(--text-muted);font-size:0.9em">🩺 %s</p>' % NOTE))
    return Lesson(title_, desc, goals, blocks, check, nxt)


def LS(n, text=None):
    return u'<a href="lesson-%02d.html">%s</a>' % (n, text or u"第 %d 課" % n)


_TOPICS = {
    "hr": (u"heart-rate-aerobic", u"心率與有氧運動"),
    "ho": (u"human-organs", u"人體器官運作機制"),
    "dm": (u"disease-mechanisms", u"疾病是怎麼形成的"),
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
