# -*- coding: utf-8 -*-
"""肥胖、代謝與 GLP-1 減重藥的規格。"""
import glp_a, glp_f, glp_ref

TOPIC = {
    "id": "obesity-glp1",
    "category": "biomed",
    "title": u"肥胖、代謝與 GLP-1 減重藥",
    "short": u"GLP-1 減重藥",
    "crumb": u"肥胖與 GLP-1",
    "icon": u"⚖️",
    "description": u"BMI 與腰圍、肥胖是不是疾病；能量平衡、代謝適應、瘦體素、飢餓與飽足的荷爾蒙、為什麼會復胖；胰島素的發現、胰島素阻抗、代謝症候群；"
                   u"腸泌素效應、吉拉毒蜥、利拉魯肽、司美格魯肽（Ozempic、Wegovy）、替爾泊肽、心血管試驗與口服新藥；"
                   u"副作用、停藥復胖、缺貨與假藥、價格與健保、社會影響；飲食與運動、減重手術、環境與政策。附四個互動模擬。",
}

MODULES = glp_a.MODULES + glp_f.MODULES
REFERENCES = glp_ref.REFERENCES
