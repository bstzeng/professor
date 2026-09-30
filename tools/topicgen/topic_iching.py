# -*- coding: utf-8 -*-
"""易經占卜主題的規格：把 ic_p1…ic_p4 的模組與兩個參考頁串起來。"""
import ic_p1, ic_p2, ic_p3, ic_p4, ic_ref

TOPIC = {
    "id": "i-ching",
    "category": "divination",
    "title": "易經占卜：卦是怎麼起、怎麼解的",
    "short": "易經占卜",
    "crumb": "易經占卜",
    "icon": "☯️",
    "description": "從陰陽、八卦到六十四卦，學會讀懂卦辭爻辭；親手用蓍草、銅錢與梅花易數起卦，"
                   "依朱熹規則解卦，再認識六爻納甲的推算方式；"
                   "最後看易經對文化的影響，以及從心理學角度理解它為什麼「感覺很準」。",
}

MODULES = ic_p1.MODULES + ic_p2.MODULES + ic_p3.MODULES + ic_p4.MODULES

REFERENCES = ic_ref.REFERENCES
