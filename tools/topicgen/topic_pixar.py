# -*- coding: utf-8 -*-
"""皮克斯動畫主題的規格：把 pix_p1…pix_p4 的模組串起來。"""
import pix_p1, pix_p2, pix_p3, pix_p4

TOPIC = {
    "id": "pixar-animation",
    "category": "fantasy",
    "title": "皮克斯動畫全紀錄：從玩具總動員到最新作品",
    "short": "皮克斯動畫",
    "crumb": "皮克斯動畫",
    "icon": "💡",
    "description": "一部電影一堂課，依上映順序完整走過皮克斯動畫工作室"
                   "從 1995《玩具總動員》到最新作品的劇情、角色與幕後故事，"
                   "依草創期、黃金期、近十年三個階段分組，"
                   "每一課都有完整劇情、主要角色表與一則幕後花絮或主題解析，"
                   "與姊妹主題《迪士尼動畫正典》各自獨立收錄，方便日後分頭擴充。",
}

MODULES = pix_p1.MODULES + pix_p2.MODULES + pix_p3.MODULES + pix_p4.MODULES
