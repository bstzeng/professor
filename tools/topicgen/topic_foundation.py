# -*- coding: utf-8 -*-
"""基地主題的規格。"""
import fd_a, fd_e, fd_ref

TOPIC = {
    "id": "foundation",
    "category": "fantasy",
    "title": "基地：預測歷史的科學與銀河帝國的衰亡",
    "short": "基地",
    "crumb": "基地",
    "icon": "🌌",
    "description": "以撒·艾西莫夫七部曲完整導讀：作者與出版史、銀河帝國與川陀、心理史學與謝頓危機；《基地》哈定與馬洛、"
                   "里歐思將軍與騾、第二基地與「星際盡頭」；崔維茲、蓋婭、地球與丹尼爾；前傳中的謝頓；機器人三定律、第零法則與大宇宙統合；"
                   "歷史決定論、心理史學能否成真、羅馬帝國原型、Apple TV+ 影集與影響。附心理史學模擬、時間表與人物卡。",
}

MODULES = fd_a.MODULES + fd_e.MODULES

REFERENCES = fd_ref.REFERENCES
