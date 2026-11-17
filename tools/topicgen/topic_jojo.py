# -*- coding: utf-8 -*-
"""JoJo 的奇妙冒險主題的規格。"""
import jjo_a, jjo_f, jjo_ref

TOPIC = {
    "id": "jojo",
    "category": "anime",
    "title": u"JoJo 的奇妙冒險：從幻影之血到 The JOJOLands",
    "short": u"JoJo",
    "crumb": u"JoJo",
    "icon": u"⭐",
    "description": u"荒木飛呂彥、JoJo 立與喬斯達家族；幻影之血、戰鬥潮流的波紋與柱之男；星塵鬥士的替身與五十天旅程、迪奧與世界；不滅鑽石的杜王町與吉良吉影；"
                   u"黃金之風的布加拉提小隊與緋紅之王；石之海的普奇神父與宇宙一巡；飆馬野郎、JOJOLion、The JOJOLands；替身的規則、名字的音樂、時間能力、波紋與旋轉、改編；"
                   u"人類讚歌與影響。含完整劇情（有暴雷）。",
}

MODULES = jjo_a.MODULES + jjo_f.MODULES
REFERENCES = jjo_ref.REFERENCES
