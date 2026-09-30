# -*- coding: utf-8 -*-
"""人體器官運作機制主題的規格：把 ho_p1…ho_p6 的模組與速查表串起來。"""
import ho_p1, ho_p2, ho_p3, ho_p4, ho_p5, ho_p6, ho_ref

TOPIC = {
    "id": "human-organs",
    "category": "biomed",
    "title": "人體器官運作機制：從細胞到全身系統",
    "short": "人體器官運作機制",
    "crumb": "人體器官運作機制",
    "icon": "🫀",
    "description": "從細胞膜、ATP 與恆定性打地基，逐一拆解循環、呼吸、消化、泌尿、神經、感覺、"
                   "內分泌、免疫、運動與生殖系統——每個器官不只講它做什麼，更講它怎麼做到，"
                   "最後用運動、一頓飯與老化，把各系統串回一個會合作的身體。",
}

MODULES = (ho_p1.MODULES + ho_p2.MODULES + ho_p3.MODULES
           + ho_p4.MODULES + ho_p5.MODULES + ho_p6.MODULES)

REFERENCES = ho_ref.REFERENCES
