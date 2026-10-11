# -*- coding: utf-8 -*-
"""魔獸爭霸三戰略與運營主題的規格。"""
import wc3_a, wc3_e, wc3_ref

TOPIC = {
    "id": "warcraft3-strategy",
    "category": "gameguide",
    "title": u"魔獸爭霸三：戰略與運營秘笈",
    "short": u"魔獸三戰略與運營",
    "crumb": u"魔獸三戰略與運營",
    "icon": u"⚔️",
    "description": u"以《魔獸爭霸 III：淬鍊重生》2.0 版本為準，從英雄、物品、維修費與日夜的基本功，到打野、英雄等級節奏、開分礦與騷擾的運營秘笈；人類、獸人、不死族、暗夜精靈四族的英雄、兵種與開局，攻擊與護甲類型、中立英雄、對戰要點、職業選手與經典地圖。附維修費計算器、四族開局表、兵種相剋與攻擊護甲表。",
}

MODULES = wc3_a.MODULES + wc3_e.MODULES

REFERENCES = wc3_ref.REFERENCES
