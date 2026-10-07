# -*- coding: utf-8 -*-
"""勇者鬥惡龍歷代故事主題的規格。"""
import dq_a, dq_e, dq_ref

TOPIC = {
    "id": "dragon-quest",
    "category": "games",
    "title": u"勇者鬥惡龍歷代故事：從洛特的傳說到尋覓逝去的時光",
    "short": u"勇者鬥惡龍歷代故事",
    "crumb": u"DQ 歷代故事",
    "icon": u"🐉",
    "description": u"勇者鬥惡龍正傳與主要外傳的完整劇情（含結局暴雷）：洛特三部曲（DQ3→DQ1→DQ2）、天空三部曲（DQ4 比薩羅、DQ5 三代人的一生、DQ6 夢與現實）、DQ7 的島嶼、DQ8 的詛咒、"
                   u"DQ9 的天使、DQ11 與洛特傳說的連結，以及創世小玩家、怪物仙境等外傳；DQ10 簡介、DQ12 近況。附發行年表、洛特血脈、人物關係、怪物圖鑑與全系列結局對照等互動工具。",
}

MODULES = dq_a.MODULES + dq_e.MODULES

REFERENCES = dq_ref.REFERENCES
