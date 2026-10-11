# -*- coding: utf-8 -*-
"""世紀帝國一代與二代戰略與運營主題的規格。"""
import aoe_a, aoe_e, aoe_ref

TOPIC = {
    "id": "aoe-strategy",
    "category": "gameguide",
    "title": u"世紀帝國一代與二代：戰略與運營秘笈",
    "short": u"世紀帝國戰略與運營",
    "crumb": u"世紀帝國戰略與運營",
    "icon": u"🏰",
    "description": u"以《世紀帝國 II：決定版》為主，從四種資源、四個時代、村民與城鎮中心的基本功，到開局分配、城鎮中心不閒置、農田、經濟科技與無金部隊的運營秘笈；兵種相剋、黑暗與封建的進攻、快速城堡、攻城與海戰；不列顛、法蘭克、蒙古等文明與 2025、2026 年的新文明；一代決定版與羅馬再起模式，團戰、職業選手與練習方法。附經濟模擬器、城鎮中心訓練、開局表、兵種相剋與文明速查。",
}

MODULES = aoe_a.MODULES + aoe_e.MODULES

REFERENCES = aoe_ref.REFERENCES
