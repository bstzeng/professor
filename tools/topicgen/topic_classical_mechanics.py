# -*- coding: utf-8 -*-
"""古典力學主題的規格。"""
import cmc_a, cmc_c, cmc_e, cmc_g, cmc_ref

TOPIC = {
    "id": "classical-mechanics",
    "category": "science",
    "title": u"古典力學：從牛頓到拉格朗日與哈密頓",
    "short": u"古典力學",
    "crumb": u"古典力學",
    "icon": u"🪐",
    "description": u"亞里斯多德、伽利略的斜面、克卜勒三大定律、牛頓的《原理》；運動學、拋體與空氣阻力、自由體圖、非慣性系的離心力與科氏力、颱風與傅科擺；"
                   u"功與能量、保守力與位能、動量與碰撞、火箭方程式、角動量；簡諧、阻尼與受迫振動、共振與塔科馬大橋、耦合振子、波動方程式；"
                   u"殼層定理、有效位能、完整推導克卜勒軌道、逃逸速度與霍曼轉移、潮汐、三體問題與拉格朗日點、海王星與水星；質心、轉動慣量、慣量張量、網球拍定理、陀螺與歲差；"
                   u"變分法與最速降線、最小作用量原理、諾特定理、哈密頓方程式與相空間、劉維爾定理、泊松括號與量子化、哈密頓—雅可比方程式；雙擺混沌、KAM 定理與古典力學的邊界。附五個互動模擬。",
}

MODULES = cmc_a.MODULES + cmc_c.MODULES + cmc_e.MODULES + cmc_g.MODULES
REFERENCES = cmc_ref.REFERENCES
