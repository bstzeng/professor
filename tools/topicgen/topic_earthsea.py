# -*- coding: utf-8 -*-
"""地海主題的規格。"""
import es_a, es_e, es_ref

TOPIC = {
    "id": "earthsea",
    "category": "fantasy",
    "title": "地海：真名、平衡與陰影",
    "short": "地海",
    "crumb": "地海",
    "icon": "🐉",
    "description": "娥蘇拉·勒瑰恩六部曲完整導讀：勒瑰恩生平、地海群島與閱讀順序；真名、平衡、柔克學院九師傅、女人的魔法與龍；"
                   "《地海巫師》的陰影、《地海古墓》的自由、《地海彼岸》的死亡；《地海孤雛》《地海故事集》《地海奇風》的重新看見；"
                   "道家思想、有色人種主角、女性主義的重寫、死亡與不朽、榮格的陰影；迷你劇、吉卜力《地海戰記》與對奇幻文學的影響。",
}

MODULES = es_a.MODULES + es_e.MODULES

REFERENCES = es_ref.REFERENCES
