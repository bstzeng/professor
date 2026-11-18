# -*- coding: utf-8 -*-
"""微積分：直覺與應用的規格。"""
import clc_a, clc_f, clc_ref

TOPIC = {
    "id": "calculus",
    "category": "math",
    "title": u"微積分：直覺與應用",
    "short": u"微積分",
    "crumb": u"微積分",
    "icon": u"📈",
    "description": u"重直覺與應用的微積分：函數、芝諾悖論與極限、瞬間變化率；導數與切線、規則、連鎖律與反向傳播、e 與複利、三角函數；最佳化、相關變化率、牛頓法、線性近似與誤差傳遞、經濟學的邊際；"
                   u"黎曼和、微積分基本定理、換元與分部、體積與平均值、常態分布；斜率場、指數成長與半衰期、冷卻與藥物濃度、邏輯斯諦、簡諧振動與共振；泰勒展開與尤拉公式、梯度下降與 AI、牛頓與萊布尼茲。附割線切線、黎曼和、圍籬最佳化與斜率場四個互動工具。",
}

MODULES = clc_a.MODULES + clc_f.MODULES
REFERENCES = clc_ref.REFERENCES
