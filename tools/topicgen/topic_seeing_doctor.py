# -*- coding: utf-8 -*-
"""看病指南主題的規格：把 sd_a、sd_c、sd_e、sd_g 的模組與速查表串起來。"""
import sd_a, sd_c, sd_e, sd_g, sd_ref

TOPIC = {
    "id": "seeing-a-doctor",
    "category": "biomed",
    "title": "看病指南：從描述症狀到看懂報告",
    "short": "看病指南",
    "crumb": "看病指南",
    "icon": "🏥",
    "description": "不舒服了，接下來怎麼做：怎麼用一句話說出主訴、用八個面向描述症狀、準備病史與看診小抄；"
                   "聽懂醫生的說明、問對問題、一起做決定；知道該看哪一科、什麼時候去急診；"
                   "看懂檢查報告與藥袋，了解健保、自費、住院與病人權利，以及帶孩子、陪長輩看病的重點。",
}

MODULES = sd_a.MODULES + sd_c.MODULES + sd_e.MODULES + sd_g.MODULES

REFERENCES = sd_ref.REFERENCES
