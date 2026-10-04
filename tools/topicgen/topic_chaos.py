# -*- coding: utf-8 -*-
"""混沌理論主題的規格。"""
import ch_a, ch_e, ch_h, ch_ref

TOPIC = {
    "id": "chaos-theory",
    "category": "math",
    "title": "混沌理論：決定論中的不可預測",
    "short": "混沌理論",
    "crumb": "混沌理論",
    "icon": "🦋",
    "description": "混沌理論完整導讀：拉普拉斯妖、龐加萊、勞倫茲與蝴蝶效應；邏輯斯諦映射、蛛網圖、週期倍增、分岔圖、費根鮑姆常數與週期三；"
                   "李亞普諾夫指數、可預測時間、相空間與吸引子；勞倫茲方程、拉伸與摺疊、Hénon 映射、龐加萊截面與通往混沌的路；"
                   "碎形維度、曼德博與朱利亞集合、牛頓碎形；雙擺、三體、天氣與系集預報、亂流、生物節律與同步；族群、經濟、混沌控制、加密與常見誤用。"
                   "附十三個即時互動實驗。",
}

MODULES = ch_a.MODULES + ch_e.MODULES + ch_h.MODULES

REFERENCES = ch_ref.REFERENCES
