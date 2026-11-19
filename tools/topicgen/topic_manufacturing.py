# -*- coding: utf-8 -*-
"""製造工法的規格。"""
import mfg_a, mfg_ref

TOPIC = {
    "id": "manufacturing", "category": "tech",
    "title": u"東西是怎麼做出來的：製造工法",
    "short": u"製造工法", "crumb": u"製造工法", "icon": u"🏭",
    "description": u"選擇工法的三個問題、公差與配合、量測；鑄造、射出成型、吹塑押出與熱成型、玻璃與陶瓷；鍛造、軋延與抽線、沖壓與連續模、擠型；車床與銑床、CNC 與 G 碼、刀具與切削液、磨削放電與雷射、一體成形的手機外殼；"
                   u"焊接、螺絲鉚接與黏著、陽極處理電鍍與塗裝；3D 列印的原理與限制；模具、流水線與節拍時間、良率與統計製程管制、豐田生產方式、半導體與台灣的產業聚落。附公差疊加、射出成型、切削參數、3D 列印與開模、管制圖五個互動模擬。",
}
MODULES = mfg_a.MODULES
REFERENCES = mfg_ref.REFERENCES
