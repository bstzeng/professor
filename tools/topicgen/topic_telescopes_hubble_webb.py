# -*- coding: utf-8 -*-
"""從哈伯到韋伯主題的規格。"""
import tel_a, tel_f, tel_ref

TOPIC = {
    "id": "telescopes-hubble-webb",
    "category": "science",
    "title": u"從哈伯到韋伯：太空望遠鏡的故事",
    "short": u"從哈伯到韋伯",
    "crumb": u"從哈伯到韋伯",
    "icon": u"🔭",
    "description": u"口徑與解析度、大氣擾動與自適應光學、電磁波譜；史匹哲的夢想、哈伯的發射、磨錯的鏡子、五次維修任務；"
                   u"哈伯常數與距離階梯、哈伯深空、加速膨脹、創生之柱、彗星撞木星、星系中心黑洞；康普頓、錢德拉、史匹哲、普朗克、蓋亞；"
                   u"韋伯的紅外線、摺疊鈹鏡、遮陽板與 L2、四台儀器、預算與延期；344 個單點故障與鏡面對準；第一批影像、紅移 14 的星系、系外行星大氣、哈伯張力、小紅點；"
                   u"歐幾里得、羅曼、宜居世界天文台與極大望遠鏡。附四個互動模擬。",
}

MODULES = tel_a.MODULES + tel_f.MODULES
REFERENCES = tel_ref.REFERENCES
