# -*- coding: utf-8 -*-
"""AI 新藥研發與癌症標靶預測的規格。"""
import rx_a, rx_c, rx_e, rx_h, rx_ref

TOPIC = {
    "id": "ai-drug-discovery",
    "category": "biomed",
    "title": u"AI 新藥研發：從預測癌症標靶到臨床試驗的完整流程",
    "short": u"AI 新藥研發",
    "crumb": u"AI 新藥研發",
    "icon": u"💊",
    "description": u"新藥研發十個階段與失敗原因、藥物形式；癌症特徵、致癌與抑癌基因、訊號路徑、免疫檢查點與抗藥性；TCGA、DepMap、GTEx、單細胞與遺傳證據；"
                   u"怎麼預測癌症標靶：驅動突變、依賴性、合成致死、表面抗原、網路與知識圖譜、機器學習排序、可成藥性、LLM 文獻探勘、評分卡與實驗驗證；"
                   u"AlphaFold 與蛋白質語言模型；虛擬篩選、生成式化學、逆合成、主動學習；ADMET、自由能與抗體設計；藥動學、生物標記、數位病理、臨床試驗與法規；"
                   u"基利克、PARP、KRAS G12C、PROTAC、ADC 與 AI 新藥公司案例。附多種互動模擬。教育用途，非醫療建議。",
}

MODULES = rx_a.MODULES + rx_c.MODULES + rx_e.MODULES + rx_h.MODULES

REFERENCES = rx_ref.REFERENCES
