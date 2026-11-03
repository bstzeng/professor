# -*- coding: utf-8 -*-
"""睡眠的科學（slp_）。"""
import slp_a, slp_c, slp_e, slp_ref

TOPIC = {
    "id": "sleep-science",
    "category": "biomed",
    "title": u"睡眠的科學：從睡眠週期、生理時鐘到失眠與改善",
    "short": u"睡眠的科學",
    "crumb": u"睡眠的科學",
    "icon": u"😴",
    "description": u"睡眠的功能與研究史、睡眠的測量；睡眠週期、兩歷程模型、生理時鐘與褪黑激素、時型、咖啡因、酒精與藥物、夢、一生的睡眠；睡眠與記憶、情緒、免疫、代謝、心血管、類淋巴系統、睡眠負債與疲勞駕駛；"
                   u"失眠與 CBT-I、睡眠呼吸中止、猝睡症、不寧腿、異睡症、時鐘失調、輪班、時差、安眠藥；睡眠衛生、光照、臥室、運動飲食、午睡、穿戴裝置與迷思；嬰幼兒、青少年、長者、女性與台灣人的睡眠。附公式與 5 個互動工具。",
}

MODULES = slp_a.MODULES + slp_c.MODULES + slp_e.MODULES
REFERENCES = slp_ref.REFERENCES
