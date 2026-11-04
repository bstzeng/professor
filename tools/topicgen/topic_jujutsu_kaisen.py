# -*- coding: utf-8 -*-
"""咒術迴戰主題的規格。"""
import jjk_a, jjk_c, jjk_e, jjk_ref

TOPIC = {
    "id": "jujutsu-kaisen",
    "category": "anime",
    "title": u"咒術迴戰全紀錄：咒力、劇情與人物完整解析",
    "short": u"咒術迴戰",
    "crumb": u"咒術迴戰",
    "icon": u"👁️",
    "description": u"芥見下下的原作與 MAPPA 的動畫；咒力與咒靈、等級、術式、束縛、帳與天元、領域展開、反轉術式與黑閃、咒具與天與咒縛、御三家與上層；從第 0 集、宿儺之指、少年院、交流會、懷玉・玉折、澀谷事變、禪院家、死滅迴游到新宿決戰與第 271 話結局（含完整劇透）；"
                   u"虎杖、伏黑、釘崎、五條、宿儺、夏油與羂索、乙骨、二年級與特級咒靈；正確的死亡、愛與詛咒、致敬與爭議。含故事年表、人物關係圖、術式與人物圖鑑。",
}

MODULES = jjk_a.MODULES + jjk_c.MODULES + jjk_e.MODULES
REFERENCES = jjk_ref.REFERENCES
