# -*- coding: utf-8 -*-
"""材料老化與結構安全檢查主題的規格。"""
import ins_a, ins_d, ins_h, ins_ref

TOPIC = {
    "id": "aging-inspection",
    "category": "tech",
    "title": u"材料老化與結構安全檢查：飛機、橋樑、建築怎麼知道還安不安全",
    "short": u"老化與結構檢查",
    "crumb": u"老化與檢查",
    "icon": u"🔩",
    "description": u"材料為什麼會老化、怎麼研究、怎麼檢查、怎麼補強，每課完整推導：疲勞、腐蝕、應力腐蝕、潛變、混凝土碳化與氯離子；"
                   u"S-N 曲線、破壞力學、Paris 定律、加速老化、斷口分析、Weibull；目視、液滲、磁粉、渦電流、超音波、射線、熱像、聲射與 POD；"
                   u"飛機（彗星、阿囉哈、華航 611、檢查間隔、老舊飛機、複材、引擎）、橋樑（評等、氯離子、鋼橋疲勞、沖刷、倒塌案例、承載力）、"
                   u"建築（耐震評估、海砂屋、強度檢測、裂縫判讀、沉陷、地震案例）、壓力容器、核電壓力容器、管線、儲槽、風機葉片；"
                   u"修復與補強（補片、止裂孔、複材修補、陰極防蝕、外加預力、FRP、耐震補強、隔震）、健康監測、可靠度與檢查最佳化。",
}

MODULES = ins_a.MODULES + ins_d.MODULES + ins_h.MODULES

REFERENCES = ins_ref.REFERENCES
