# -*- coding: utf-8 -*-
"""電吉他原理與彈奏主題的規格：把 eg_p1…eg_p5 的模組串起來。"""
import eg_p1, eg_p2, eg_p3, eg_p4, eg_p5

TOPIC = {
    "id": "electric-guitar",
    "category": "music",
    "title": "電吉他原理與彈奏：從拾音器到推弦揉弦的完整拆解",
    "short": "電吉他原理",
    "crumb": "電吉他原理",
    "icon": "🎸",
    "description": "從拾音器怎麼靠電磁感應把弦震動變成電訊號講起，"
                   "一路拆解吉他機身結構、音箱前後級、效果器五大分類與排列邏輯，"
                   "最後進入推弦、揉弦、點弦、掃弦、泛音等彈奏技巧，"
                   "技巧課程額外附上 YouTube 搜尋連結輔助觀察真人示範動作。",
}

MODULES = (eg_p1.MODULES + eg_p2.MODULES + eg_p3.MODULES + eg_p4.MODULES
           + eg_p5.MODULES)
