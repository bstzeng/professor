# -*- coding: utf-8 -*-
"""最終幻想歷代故事主題的規格。"""
import ff_a, ff_e, ff_ref

TOPIC = {
    "id": "final-fantasy",
    "category": "games",
    "title": u"最終幻想歷代故事：十六個世界，一個名字",
    "short": u"最終幻想歷代故事",
    "crumb": u"FF 歷代故事",
    "icon": u"💎",
    "description": u"最終幻想 FF1～FF16 正傳、續作與主要外傳的完整劇情（含結局暴雷）：水晶與光之戰士、塞西爾、凱夫卡、FF7 與其衍生宇宙、FF8 的魔女、FF9、FF10 的斯匹拉、"
                   u"伊瓦利斯與戰略版、FF13 三部曲、FF15、FF16；FF11 與 FF14 簡介。附發行年表、FF7 年表、召喚獸與席德圖鑑、人物關係與全系列結局對照等互動工具。",
}

MODULES = ff_a.MODULES + ff_e.MODULES

REFERENCES = ff_ref.REFERENCES
