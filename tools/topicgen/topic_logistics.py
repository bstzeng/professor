# -*- coding: utf-8 -*-
"""全球物流系統主題的規格。"""
import lg_a, lg_e, lg_ref

TOPIC = {
    "id": "global-logistics",
    "category": "tech",
    "title": u"全球物流系統：一件商品怎麼跨越半個地球來到你手上",
    "short": u"全球物流系統",
    "crumb": u"全球物流系統",
    "icon": u"🚢",
    "description": u"從一支手機的旅程出發：貨櫃革命、貨櫃船、航線與海運聯盟、世界大港與碼頭、運河與海峽、長榮陽明萬海；航空貨運、快遞樞紐、冷鏈；"
                   u"卡車、中歐班列、多式聯運、管線；配送中心、越庫、自動化倉儲、電商與超商取貨；長鞭效應、經濟訂購量、JIT、韌性、半導體供應鏈；"
                   u"國貿條規、提單報關、保稅與出口管制；疫情塞港、長賜輪、紅海與巴拿馬乾旱；追蹤技術、路線最佳化、自動化與綠色航運。附世界航線地圖、長鞭效應模擬等六個互動工具。",
}

MODULES = lg_a.MODULES + lg_e.MODULES

REFERENCES = lg_ref.REFERENCES
