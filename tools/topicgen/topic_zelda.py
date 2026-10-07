# -*- coding: utf-8 -*-
"""薩爾達傳說歷代故事主題的規格。"""
import zd_a, zd_e, zd_ref

TOPIC = {
    "id": "zelda",
    "category": "games",
    "title": u"薩爾達傳說歷代故事：從天空洛夫特到王國之淚",
    "short": u"薩爾達傳說歷代故事",
    "crumb": u"薩爾達歷代故事",
    "icon": u"🗡️",
    "description": u"薩爾達傳說正傳與主要外傳的完整劇情（含結局暴雷），依官方三分歧時間線講解：天空之劍的起源與終焉者的詛咒、時之笛的分歧、勇者敗北線、少年線（穆修拉的假面、黃昏公主）、"
                   u"成年線（風之律動、大地的汽笛）、曠野之息與王國之淚。附發行年表、時間線樹、海拉魯地圖、轉世輪迴、人物關係與結局對照等互動工具。",
}

MODULES = zd_a.MODULES + zd_e.MODULES

REFERENCES = zd_ref.REFERENCES
