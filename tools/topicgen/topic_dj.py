# -*- coding: utf-8 -*-
"""DJ 器材與轉盤原理主題的規格：把 dj_p1…dj_p7 的模組串起來。"""
import dj_p1, dj_p2, dj_p3, dj_p4, dj_p5, dj_p6, dj_p7

TOPIC = {
    "id": "dj-turntable",
    "category": "music",
    "title": "DJ 器材與轉盤原理：從黑膠物理到現場混音的完整拆解",
    "short": "DJ 轉盤原理",
    "crumb": "DJ 轉盤原理",
    "icon": "🎧",
    "description": "從黑膠溝槽如何刻錄聲音、唱頭怎麼把震動變回電訊號講起，"
                   "一路拆解轉盤馬達、混音台訊號路徑、抓拍與刷碟兩大核心技巧，"
                   "再到 CDJ、Timecode Vinyl、MIDI 控制器的數位化演進，"
                   "最後收在效果器、現場臨場判斷與一套入門器材建議。",
}

MODULES = (dj_p1.MODULES + dj_p2.MODULES + dj_p3.MODULES + dj_p4.MODULES
           + dj_p5.MODULES + dj_p6.MODULES + dj_p7.MODULES)
