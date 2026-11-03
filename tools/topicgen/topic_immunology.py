# -*- coding: utf-8 -*-
"""免疫系統與疫苗主題的規格。"""
import imm_a, imm_c, imm_e, imm_ref

TOPIC = {
    "id": "immunology-vaccines",
    "category": "biomed",
    "title": u"免疫系統與疫苗",
    "short": u"免疫系統與疫苗",
    "crumb": u"免疫與疫苗",
    "icon": u"🦠",
    "description": u"病原體、免疫器官與細胞、自我與非我、發炎；屏障、吞噬細胞、補體、NK 細胞與干擾素、發燒、模式識別受體；抗體、T 細胞、MHC、V(D)J 與克隆選擇、免疫耐受與記憶；"
                   u"天花與琴納、巴斯德、疫苗種類、mRNA 疫苗、群體免疫與 R₀、疫苗安全、反疫苗運動與台灣的 B 肝疫苗；過敏、自體免疫、免疫缺陷、HIV、移植、癌症免疫療法、細胞激素風暴；睡眠、壓力、運動營養、腸道菌與老化。含 SIR 模型、抗體反應與群體免疫互動模擬。",
}

MODULES = imm_a.MODULES + imm_c.MODULES + imm_e.MODULES
REFERENCES = imm_ref.REFERENCES
