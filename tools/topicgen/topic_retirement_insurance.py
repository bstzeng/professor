# -*- coding: utf-8 -*-
"""退休與保險規劃主題的規格。"""
import rti_a, rti_c, rti_e, rti_ref

TOPIC = {
    "id": "retirement-insurance",
    "category": "invest",
    "title": u"退休與保險規劃：勞保、勞退、保險怎麼配",
    "short": u"退休與保險規劃",
    "crumb": u"退休與保險",
    "icon": u"🧓",
    "description": u"所得替代率、通膨、平均餘命與長壽風險、三層保障、4% 法則與複利；勞保老年年金的 A／B 式與請領年齡、勞保財務、勞退新制與自提節稅、舊制、國民年金、軍公教與自營業者、轉職時的年資；"
                   u"資產配置與水桶法、存股與 ETF、配息不等於報酬、提領策略、稅與補充保費、以房養老、安養信託與意定監護、理財陷阱與詐騙；健保的缺口、實支實付、重大傷病、失能、壽險、長照、儲蓄險與投資型保單、保單健檢、理賠與話術；25、35、50、65 歲的案例與照顧父母。含勞保、勞退、退休缺口、提領模擬、壽險需求等互動試算。",
}

_D = rti_c.MODULES[-1]
MODULES = rti_a.MODULES + rti_c.MODULES[:-1] + [(_D[0], _D[1] + rti_e.MODULES[0][1])] + rti_e.MODULES[1:]
REFERENCES = rti_ref.REFERENCES
