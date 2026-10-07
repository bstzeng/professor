# -*- coding: utf-8 -*-
"""氣的輸送主題的規格。"""
import qi_a, qi_e, qi_ref

TOPIC = {
    "id": "qi-transport",
    "category": "life",
    "title": u"氣的輸送：中醫理論中的氣如何生成、運行與阻滯",
    "short": u"氣的輸送",
    "crumb": u"氣的輸送",
    "icon": u"🌬️",
    "description": u"用「輸送現象」的眼光整理中醫的氣理論：氣的字源與先秦氣論、氣的種類；元氣、脾胃、肺與宗氣的生成；十二經流注、子午流注、營衛運行、奇經、腧穴與三焦；"
                   u"升降出入、肝升肺降、脾升胃降、心腎相交、氣血耦合與晝夜四季；氣虛、氣滯、氣逆、氣陷與九氣為病；針灸、導引與入門呼吸練習、中藥、推拿；"
                   u"最後中立整理經絡實體、針灸與氣功的研究證據。附子午流注、營衛運行、氣機升降、源—流—匯類比模型與呼吸節拍器。本課程不是診斷或治療建議。",
}

MODULES = qi_a.MODULES + qi_e.MODULES

REFERENCES = qi_ref.REFERENCES
