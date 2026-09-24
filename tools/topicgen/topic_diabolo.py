# -*- coding: utf-8 -*-
"""扯鈴招式大全主題的規格：把 db_p1…db_p8 的模組串起來。"""
import db_p1, db_p2, db_p3, db_p4, db_p5, db_p6, db_p7, db_p8

TOPIC = {
    "id": "diabolo",
    "category": "life",
    "title": "扯鈴招式大全：從基本功到雙鈴三鈴的招式收藏",
    "short": "扯鈴招式",
    "crumb": "扯鈴招式",
    "icon": "🪀",
    "description": "不講原理，直接收藏招式：從蓄力甩鈴等基本功，"
                   "到金雞上架、螞蟻上樹等傳統基礎花式，"
                   "再到軸類停控、繞繩甩鞭、過肢體、Suicide 類，"
                   "最後進入雙鈴、三鈴與 Vertax、Cradle 等競技花式，"
                   "每一招都附 YouTube 搜尋連結輔助觀察真人示範動作。",
}


def _merge_same_titled(modules):
    """把標題相同的相鄰模組（例如跨檔案拆寫的模組 B）合併成一個。"""
    merged = []
    for title, lessons in modules:
        if merged and merged[-1][0] == title:
            merged[-1] = (title, merged[-1][1] + lessons)
        else:
            merged.append((title, list(lessons)))
    return merged


MODULES = _merge_same_titled(
    db_p1.MODULES + db_p2.MODULES + db_p3.MODULES + db_p4.MODULES
    + db_p5.MODULES + db_p6.MODULES + db_p7.MODULES + db_p8.MODULES
)
