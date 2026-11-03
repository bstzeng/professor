# -*- coding: utf-8 -*-
"""攻殼機動隊主題的規格。"""
import gis_a, gis_c, gis_e, gis_ref

TOPIC = {
    "id": "ghost-in-the-shell",
    "category": "anime",
    "title": u"攻殼機動隊：Ghost 與 Shell 的哲學",
    "short": u"攻殼機動隊",
    "crumb": u"攻殼機動隊",
    "icon": u"🧠",
    "description": u"士郎正宗的原作漫畫、押井守的 1995 年電影與《Innocence》、神山健治的 S.A.C.、2nd GIG、Solid State Society、ARISE、SAC_2045 與好萊塢真人版（完整劇透）；"
                   u"電子腦、義體、網路潛入、思考戰車與公安九課；傀儡師、笑面男、Stand Alone Complex、個別十一人與塔奇克馬；素子、巴特、陀古沙與荒卷；記憶與身分、忒修斯之船、AI 能否擁有 Ghost、監控社會、賽博龐克、對《駭客任務》的影響與現實中的腦機介面。",
}

MODULES = gis_a.MODULES + gis_c.MODULES + gis_e.MODULES
REFERENCES = gis_ref.REFERENCES
