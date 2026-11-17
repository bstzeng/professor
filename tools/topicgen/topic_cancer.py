# -*- coding: utf-8 -*-
"""癌症主題的規格。"""
import cnc_a, cnc_f, cnc_ref

TOPIC = {
    "id": "cancer",
    "category": "biomed",
    "title": u"癌症：從細胞到免疫療法",
    "short": u"癌症",
    "crumb": u"癌症",
    "icon": u"🎗️",
    "description": u"癌症的定義、歷史與十大特徵；細胞週期、DNA 修復、致癌基因與 RAS、抑癌基因與 p53、端粒與海拉細胞、腫瘤的演化；吸菸、病毒（B 肝、HPV、幽門桿菌）、檳榔與砷、BRCA、運氣；"
                   u"影像與切片、TNM 分期、篩檢的偽陽性與過度診斷、液態切片；手術、放療與質子、化療、標靶治療與基利克、抗藥性、免疫檢查點、CAR-T 與 mRNA 疫苗；"
                   u"存活率的陷阱、安寧緩和醫療、飲食迷思、藥價與健保、台灣的癌症地圖。附五個互動模擬。",
}

MODULES = cnc_a.MODULES + cnc_f.MODULES
REFERENCES = cnc_ref.REFERENCES
