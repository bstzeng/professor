# -*- coding: utf-8 -*-
"""台灣電力與能源現況主題的規格。"""
import twe_a, twe_e, twe_ref

TOPIC = {
    "id": "taiwan-energy",
    "category": "tech",
    "title": u"台灣電力與能源現況：電從哪裡來、燃料從哪裡來",
    "short": u"台灣電力與能源",
    "crumb": u"台灣能源",
    "icon": u"⚡",
    "description": u"台灣最新的發電結構（2025 年燃氣 47.8%、燃煤 35.4%、再生能源 13.1%、核能歸零）與十年變化；燃氣、燃煤、燃油、核能、太陽光電、離岸風電、水力抽蓄、地熱生質的原理與現況；"
                   u"負載曲線、備轉容量與停電事件；液化天然氣、煤炭、原油的進口來源與比例、安全存量與 2026 年中東戰事的衝擊；"
                   u"國際燃料歷年價格、每度電成本、電價與台電財務；2050 淨零路徑與電源配比取捨。數據截至 2026 年 10 月，附 9 個互動圖表。",
}

MODULES = twe_a.MODULES + twe_e.MODULES

REFERENCES = twe_ref.REFERENCES
