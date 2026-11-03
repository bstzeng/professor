# -*- coding: utf-8 -*-
"""行為經濟學與投資心理主題的規格。"""
import bhv_a, bhv_c, bhv_e, bhv_ref

TOPIC = {
    "id": "behavioral-finance",
    "category": "invest",
    "title": u"行為經濟學與投資心理",
    "short": u"行為經濟學與投資心理",
    "crumb": u"行為財務",
    "icon": u"🧠",
    "description": u"理性人假設、系統一與系統二、啟發法；錨定、可得性、代表性、過度自信、確認偏誤、後見之明、賭徒謬誤與回歸平均；展望理論、損失趨避、機率加權、框架、稟賦效應、心理帳戶、沉沒成本與現時偏誤；"
                   u"處分效應、追高殺低、羊群、本土偏誤、過度交易、台股散戶的實證研究與 FOMO；鬱金香、南海、網路泡沫與迷因股，動能、反轉與效率市場的爭論；推力、自動化、檢查表與事前驗屍。含展望理論、心理帳戶與處分效應互動測驗。",
}

MODULES = bhv_a.MODULES + bhv_c.MODULES + bhv_e.MODULES
REFERENCES = bhv_ref.REFERENCES
