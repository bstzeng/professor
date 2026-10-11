# -*- coding: utf-8 -*-
"""星海爭霸二代戰略與運營主題的規格。"""
import sc2_a, sc2_e, sc2_ref

TOPIC = {
    "id": "starcraft2-strategy",
    "category": "gameguide",
    "title": u"星海爭霸二代：戰略與運營秘笈",
    "short": u"星海二戰略與運營",
    "crumb": u"星海二戰略與運營",
    "icon": u"🚀",
    "description": u"以《星海爭霸 II：虛空之遺》5.0.17 版為準，從經濟數字、快捷鍵、回放與天梯，到農民不停、基準時間點、后蟲注卵、礦騾與時空加速、開礦節奏的運營秘笈；三族的建築、兵種與開局，九種對戰的要點、防守 all-in、後期決策與職業選手。附經濟模擬器、注卵訓練、開局表、兵種相剋與對戰決策樹。",
}

MODULES = sc2_a.MODULES + sc2_e.MODULES

REFERENCES = sc2_ref.REFERENCES
