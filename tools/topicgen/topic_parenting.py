# -*- coding: utf-8 -*-
"""家長教養主題的規格。"""
import pa_a, pa_e, pa_ref

TOPIC = {
    "id": "parenting",
    "category": "edu",
    "title": u"家長教養：從出生到 18 歲",
    "short": u"家長教養",
    "crumb": u"家長教養",
    "icon": u"🏡",
    "description": u"以研究為本的教養指南：教養風格、溫暖與設限、修復關係與家長自我照顧；依年齡談安全睡眠與安撫、情緒崩潰與正向管教、讚美與如廁、學習習慣與第一支手機、霸凌與性教育、"
                   u"青少年溝通與監督、菸酒電子煙、升學與打工、迎接 18 歲成年；並涵蓋離婚、多元家庭、特殊需求與台灣法規、求助專線。附教養風格象限與多個情境演練決策樹。",
}

MODULES = pa_a.MODULES + pa_e.MODULES

REFERENCES = pa_ref.REFERENCES
