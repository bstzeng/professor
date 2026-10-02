# -*- coding: utf-8 -*-
"""排隊理論主題的規格。"""
import qt_a, qt_e, qt_ref

TOPIC = {
    "id": "queueing-theory",
    "category": "math",
    "title": "排隊理論：為什麼你總是在等？",
    "short": "排隊理論",
    "crumb": "排隊理論",
    "icon": "⏳",
    "description": "從超商、客服到網路封包：排隊系統的組成、卜瓦松到達與指數分布、檢查站悖論；利特爾定律 L = λW；"
                   "M/M/1 推導與「使用率接近 100% 就塞爆」的壅塞曲線；多櫃台、爾朗 B／C 公式與人力規劃；變異、優先權、"
                   "放棄與重試風暴；生產線瓶頸與排隊網路；電腦系統、尾端延遲、交通與排隊心理學。附六個互動模擬。",
}

MODULES = qt_a.MODULES + qt_e.MODULES

REFERENCES = qt_ref.REFERENCES
