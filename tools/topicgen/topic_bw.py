# -*- coding: utf-8 -*-
"""星海爭霸一代戰略與運營主題的規格。"""
import bw_a, bw_e, bw_ref

TOPIC = {
    "id": "starcraft-bw-strategy",
    "category": "gameguide",
    "title": u"星海爭霸一代：戰略與運營秘笈",
    "short": u"星海一戰略與運營",
    "crumb": u"星海一戰略與運營",
    "icon": u"🛸",
    "description": u"以《星海爭霸：重製版》對戰為準，從資源、人口、快捷鍵與 APM 的基本功，到農民不停、補給不卡、不囤資源、按時開礦的運營秘笈；人族生化與機械化、蟲族飛龍與污染者、神族金甲蟲與仲裁者，三族開局與六種對戰，經典戰術、韓國職業傳奇與地圖。附經濟模擬器、運營訓練、開局表、兵種相剋與對戰決策樹。",
}

MODULES = bw_a.MODULES + bw_e.MODULES

REFERENCES = bw_ref.REFERENCES
