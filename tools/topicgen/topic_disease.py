# -*- coding: utf-8 -*-
"""疾病形成機制主題的規格：把 dm_p1…dm_p8 的模組與速查表串起來。"""
import dm_p1, dm_p2, dm_p3, dm_p4, dm_p5, dm_p6, dm_p7, dm_p8, dm_ref

TOPIC = {
    "id": "disease-mechanisms",
    "category": "biomed",
    "title": "疾病是怎麼形成的：致病機制與各器官常見疾病",
    "short": "疾病形成機制",
    "crumb": "疾病形成機制",
    "icon": "🦠",
    "description": "第一部拆解疾病的共同機制：細胞受傷、發炎、免疫失調、感染、遺傳、癌症、"
                   "血流障礙與代謝退化，並用高血壓、肝病與預防醫學串起來；"
                   "第二部逐一走過各器官的常見疾病，標出它們的致病機制、症狀與需要就醫的警訊。",
}

MODULES = (dm_p1.MODULES + dm_p2.MODULES + dm_p3.MODULES + dm_p4.MODULES
           + dm_p5.MODULES + dm_p6.MODULES + dm_p7.MODULES + dm_p8.MODULES)

REFERENCES = dm_ref.REFERENCES
