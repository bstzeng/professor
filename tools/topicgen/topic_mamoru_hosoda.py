# -*- coding: utf-8 -*-
"""細田守作品全紀錄主題的規格。"""
import hsd_a, hsd_f, hsd_ref

TOPIC = {
    "id": "mamoru-hosoda",
    "category": "anime",
    "title": u"細田守作品全紀錄：從《數碼寶貝》到《Scarlet》",
    "short": u"細田守",
    "crumb": u"細田守",
    "icon": u"🌻",
    "description": u"東映動畫的演出、數碼寶貝我們的戰爭遊戲、霍爾風波與航海王劇場版；跳躍吧！時空少女、夏日大作戰、狼的孩子雨和雪、怪物的孩子、未來的未來、龍與雀斑公主、Scarlet 永無止境的史嘉蕾；"
                   u"少女、父母與孩子、野獸；OZ 與 U、夏天與入道雲、現實與異界；地圖工作室、無影的角色、CG 與手繪、合作者、音樂、演員配音；與宮崎駿、新海誠的比較與評價。含完整劇情（有暴雷）。",
}

MODULES = hsd_a.MODULES + hsd_f.MODULES
REFERENCES = hsd_ref.REFERENCES
