# -*- coding: utf-8 -*-
"""時間的意義主題的規格：把 tm_p1…tm_p4 的模組串起來。"""
import tm_p1, tm_p2, tm_p3, tm_p4

TOPIC = {
    "id": "meaning-of-time",
    "category": "life",
    "title": "時間的意義：從滑手機的空虛感，到有意識地選擇時間",
    "short": "時間的意義",
    "crumb": "時間的意義",
    "icon": "⏳",
    "description": "從「滑完短影音為什麼特別空虛」講起，拆解手遊與短影音的留人設計，"
                   "再借塞內卡、斯多葛、佛學無常觀與心流、時間觀等心理學研究，"
                   "重新理解時間為什麼珍貴、休息為什麼不是浪費，"
                   "最後用時間審計、環境設計與每週回顧，找回屬於自己的時間意義。",
}

MODULES = tm_p1.MODULES + tm_p2.MODULES + tm_p3.MODULES + tm_p4.MODULES
