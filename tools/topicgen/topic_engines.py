# -*- coding: utf-8 -*-
"""引擎原理的規格。"""
import eng_a, eng_f, eng_ref

TOPIC = {
    "id": "engines",
    "category": "tech",
    "title": u"引擎原理：從蒸汽機到噴射引擎",
    "short": u"引擎原理",
    "crumb": u"引擎原理",
    "icon": u"🔥",
    "description": u"熱力學第一定律、P-V 圖與卡諾效率；紐科門與瓦特、高壓蒸汽與火車、蒸汽渦輪與發電廠；四行程與奧圖循環、點火與爆震、柴油引擎與柴油門、渦輪增壓、轉子與二行程、觸媒轉化器、變速箱與差速器；"
                   u"活塞螺旋槳、渦輪噴射、渦輪扇與旁通比、複循環發電、火箭引擎與比衝、衝壓與超燃衝壓；混合動力、氫與合成燃料、內燃機與電動車、排放法規。附 P-V 圖、四行程動畫、旁通比與火箭方程式四個互動模擬。",
}

MODULES = eng_a.MODULES + eng_f.MODULES
REFERENCES = eng_ref.REFERENCES
