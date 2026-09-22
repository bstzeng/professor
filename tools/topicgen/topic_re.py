# -*- coding: utf-8 -*-
"""惡靈古堡主題的規格：把 re_p1…re_p9 的模組串起來。"""
import re_p1, re_p2, re_p3, re_p4, re_p5, re_p6, re_p7, re_p8, re_p9

TOPIC = {
    "id": "resident-evil",
    "category": "games",
    "title": "惡靈古堡全紀錄：病毒、保護傘與三十年的生存恐怖",
    "short": "惡靈古堡",
    "crumb": "惡靈古堡",
    "icon": "🧟",
    "description": "從 1966 年非洲那朵始祖之花講起，完整拆解病毒族譜、保護傘公司與它的後繼組織，"
                   "再一代一代講完 0 代到 8 代、代號維若妮卡與啟示錄的劇情（含各重製版的改動）；"
                   "另有安德森真人電影六部曲、2021 重啟、Netflix 影集與 CG 動畫的故事，"
                   "最後以完整時間線與「恐怖與動作的鐘擺」收束。",
}

MODULES = (re_p1.MODULES + re_p2.MODULES + re_p3.MODULES + re_p4.MODULES
           + re_p5.MODULES + re_p6.MODULES + re_p7.MODULES + re_p8.MODULES
           + re_p9.MODULES)
