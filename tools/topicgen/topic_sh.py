# -*- coding: utf-8 -*-
"""沈默之丘主題的規格：把 sh_p1…sh_p5 的模組串起來。"""
import sh_p1, sh_p2, sh_p3, sh_p4, sh_p5

TOPIC = {
    "id": "silent-hill",
    "category": "games",
    "title": "沈默之丘全解析：霧、罪與那座會回應你的小鎮",
    "short": "沈默之丘",
    "crumb": "沈默之丘",
    "icon": "🌫️",
    "description": "從 Team Silent 與 1999 年講起，先建立小鎮的三層世界、教團的信仰與"
                   "「怪物是症狀不是敵人」這套設計語法，再一代一代講完 1 到 4 代、"
                   "西方工作室時期、P.T. 與 Silent Hill f 的劇情，"
                   "另有三部電影的故事，最後以結局全表與心理恐怖的技藝收束。",
}

MODULES = (sh_p1.MODULES + sh_p2.MODULES + sh_p3.MODULES + sh_p4.MODULES + sh_p5.MODULES)
