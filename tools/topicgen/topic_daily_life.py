# -*- coding: utf-8 -*-
"""穿越古代過一天主題的規格。"""
import dl_a, dl_c, dl_e, dl_g, dl_j, dl_ref

TOPIC = {
    "id": "ancient-daily-life",
    "category": "history",
    "title": "穿越古代過一天：中國歷代百姓的生活、新事物與娛樂",
    "short": "穿越古代過一天",
    "crumb": "穿越古代過一天",
    "icon": "🏮",
    "description": "從周代農夫、秦代小吏、唐代長安的賣餅郎，到宋代開封的夜市、明代江南的織戶、晚清上海的職員："
                   "用史料重建各朝百姓從早到晚的一天，看每個朝代多了哪些食物、器物與娛樂，"
                   "再把吃、住、穿、夜晚、錢的三千年演變串起來。附時辰換算器、餐桌時間軸、穿越日程模擬器與「哪朝有」小測驗。",
}

MODULES = dl_a.MODULES + dl_c.MODULES + dl_e.MODULES + dl_g.MODULES + dl_j.MODULES

REFERENCES = dl_ref.REFERENCES
