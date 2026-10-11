# -*- coding: utf-8 -*-
"""霹靂布袋戲主題的規格。"""
import pl_a, pl_e, pl_ref

TOPIC = {
    "id": "pili-puppetry",
    "category": "anime",
    "title": u"霹靂布袋戲：從掌中戲到素還真的四十年",
    "short": u"霹靂布袋戲",
    "crumb": u"霹靂布袋戲",
    "icon": u"🎭",
    "description": u"從黃海岱的五洲園、黃俊雄的《雲州大儒俠》到黃強華、黃文擇創立霹靂；戲偶構造、操偶、八音才子的口白、特效與 AI；苦境、三教與詩號的世界觀；"
                   u"1988 年《霹靂金光》到 2026 年《塗附世界》的劇集大事記；素還真、一頁書、葉小釵、三先天、羅喉、棄天帝等經典角色；聖石傳說、東離劍遊紀、Netflix 與授權周邊，以及新手入門路線。附大事記、劇集年表、角色卡與關係圖、詩號卡、入門選劇。",
}

MODULES = pl_a.MODULES + pl_e.MODULES

REFERENCES = pl_ref.REFERENCES
