# -*- coding: utf-8 -*-
"""仙劍奇俠傳歷代故事主題的規格。"""
import pj_a, pj_e, pj_ref

TOPIC = {
    "id": "chinese-paladin",
    "category": "games",
    "title": u"仙劍奇俠傳歷代故事：從餘杭鎮到神樹",
    "short": u"仙劍奇俠傳歷代故事",
    "crumb": u"仙劍歷代故事",
    "icon": u"⚔️",
    "description": u"仙劍奇俠傳單機正傳與外傳的完整劇情（含結局暴雷）：一代李逍遙、趙靈兒、林月如與鎖妖塔、拜月教主；二代王小虎與蘇媚的寬恕；三代景天、雪見、龍葵、紫萱與徐長卿的輪迴；"
                   u"問情篇南宮煌；四代雲天河、韓菱紗與瓊華派的尋仙；五前傳夏侯瑾軒與姜承；五代姜雲凡；六代越今朝與越祈；七代修吾與月清疏。附發行年表、故事時間線、血脈與前世今生、地圖、全系列結局對照等互動工具。",
}

MODULES = pj_a.MODULES + pj_e.MODULES

REFERENCES = pj_ref.REFERENCES
