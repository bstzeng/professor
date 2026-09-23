# -*- coding: utf-8 -*-
"""迪士尼動畫正典主題的規格：把 dis_p1…dis_p7 的模組串起來。"""
import dis_p1, dis_p2, dis_p3, dis_p4, dis_p5, dis_p6, dis_p7

TOPIC = {
    "id": "disney-animation",
    "category": "fantasy",
    "title": "迪士尼動畫正典：從白雪公主到星願的劇情全紀錄",
    "short": "迪士尼動畫",
    "crumb": "迪士尼動畫",
    "icon": "🏰",
    "description": "一部電影一堂課，依official「動畫正典」順序完整走過迪士尼動畫工作室"
                   "從 1937《白雪公主》到最新作品的劇情、角色與幕後故事，"
                   "依黃金時代、白銀時代、文藝復興、復興時代等歷史分期分組，"
                   "戰時六部選集片合併一課概述，每一課都有完整劇情、主要角色表"
                   "與一則幕後花絮或爭議說明。",
}

def _merge_same_titled(modules):
    """把標題相同的相鄰模組（例如跨檔案拆寫的模組 G）合併成一個。"""
    merged = []
    for title, lessons in modules:
        if merged and merged[-1][0] == title:
            merged[-1] = (title, merged[-1][1] + lessons)
        else:
            merged.append((title, list(lessons)))
    return merged


MODULES = _merge_same_titled(
    dis_p1.MODULES + dis_p2.MODULES + dis_p3.MODULES + dis_p4.MODULES
    + dis_p5.MODULES + dis_p6.MODULES + dis_p7.MODULES
)
