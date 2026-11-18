# -*- coding: utf-8 -*-
"""人體實驗與醫學倫理的規格。"""
import hxe_a, hxe_b, hxe_ref

TOPIC = {
    "id": "human-experiments", "category": "biomed",
    "title": u"人體實驗與醫學倫理：從暴行到受試者保護",
    "short": u"人體實驗與醫學倫理", "crumb": u"醫學倫理", "icon": u"⚕️",
    "description": u"醫學為什麼需要人體試驗、受試者與病人；天花與黃熱病、納粹醫師的實驗、醫師審判與紐倫堡守則、731 部隊與戰後的交易、塔斯基吉梅毒研究、瓜地馬拉梅毒實驗、輻射人體實驗、MKUltra、威洛布魯克、海拉細胞、沙利竇邁；"
                   u"赫爾辛基宣言、比徹的揭露、貝爾蒙報告三原則、知情同意、倫理審查委員會、弱勢受試者、安慰劑倫理、台灣人體研究法與健保資料庫案；TGN1412、跨國臨床試驗、賀建奎基因編輯嬰兒、新冠人體挑戰試驗、資料與 AI 的研究倫理。附年表、案例圖鑑、規範關係圖與臨床試驗流程動畫。",
}
MODULES = hxe_a.MODULES + hxe_b.MODULES
REFERENCES = hxe_ref.REFERENCES
