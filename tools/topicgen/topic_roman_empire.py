# -*- coding: utf-8 -*-
"""羅馬帝國興衰主題的規格。"""
import rom_a, rom_c, rom_e, rom_ref

TOPIC = {
    "id": "roman-empire",
    "category": "history",
    "title": u"羅馬帝國興衰：從共和到拜占庭",
    "short": u"羅馬帝國興衰",
    "crumb": u"羅馬帝國興衰",
    "icon": u"🏛️",
    "description": u"建城神話、共和制度、統一義大利、布匿戰爭與漢尼拔、軍團；格拉古兄弟、馬略與蘇拉、斯巴達克斯、凱撒、安東尼與克麗奧佩脫拉；奧古斯都、羅馬和平、五賢帝、道路水道、城市生活、公民與奴隸、基督教的興起；"
                   u"三世紀危機、戴克里先、君士坦丁、東西分治、蠻族遷徙；阿提拉、汪達爾、476 年與羅馬滅亡的理論；查士丁尼、拜占庭、十字軍與 1453 年；羅馬法、建築、語言曆法與共和的教訓。含前 264 年到 1453 年的疆域互動地圖。",
}

MODULES = rom_a.MODULES + rom_c.MODULES + rom_e.MODULES
REFERENCES = rom_ref.REFERENCES
