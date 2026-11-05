# -*- coding: utf-8 -*-
"""藥是怎麼作用的主題的規格。"""
import phm_a, phm_c, phm_e, phm_ref

TOPIC = {
    "id": "pharmacology",
    "category": "biomed",
    "title": u"藥是怎麼作用的：生活中的藥理學",
    "short": u"藥是怎麼作用的",
    "crumb": u"藥理學",
    "icon": u"💊",
    "description": u"劑量與毒性、受體、致效劑與拮抗劑、吸收分布代謝排除、肝腎、半衰期、治療窗、給藥途徑；止痛藥、鴉片類、抗生素與抗藥性、抗病毒藥、感冒藥、過敏藥、胃藥、降血壓、降血脂、降血糖與 GLP-1、抗凝血、安眠藥、抗憂鬱藥、生物製劑；"
                   u"副作用、交互作用、葡萄柚與酒精、嚴重藥物過敏與 HLA-B*1502、年長者多重用藥、孕婦與兒童、藥袋與仿單、保健食品與中藥；天然物與青蒿素、臨床試驗、安慰劑、學名藥與生物相似藥、台灣藥價；成癮的大腦與尼古丁、酒精、咖啡因。含血中濃度與劑量—反應模擬器。",
}

_A, _B = phm_a.MODULES
_C = phm_c.MODULES[0]
MODULES = [_A, (_B[0], _B[1] + phm_c.B2), (_C[0], _C[1] + phm_e.C2)] + phm_e.MODULES
REFERENCES = phm_ref.REFERENCES
