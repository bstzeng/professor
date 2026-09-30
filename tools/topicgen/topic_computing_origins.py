# -*- coding: utf-8 -*-
"""電腦是怎麼從零開始的:從開機、DOS 到視窗 3.1。"""
import co_a, co_b, co_c, co_d, co_e, co_f, co_g, co_h, co_ref

TOPIC = {
    "id": "computing-origins",
    "category": "tech",
    "title": "電腦是怎麼從零開始的:從開機、DOS 到視窗 3.1",
    "short": "電腦從零開始",
    "crumb": "電腦從零開始",
    "icon": "💾",
    "description": "在還沒有作業系統、沒有視窗、連寫程式的介面都沒有的年代,電腦是怎麼啟動的?"
                   "從一個開關、邏輯閘、CPU 的心跳講起,一路走過開機的雞生蛋問題(BIOS、POST、開機磁區)、"
                   "DOS 怎麼做出來與怎麼運作(命令列、FAT、INT 21h、640K),再到圖形介面的觀念、"
                   "以及 Windows 3.1 如何在 DOS 之上蓋出視窗(GDI、訊息迴圈、保護模式、多工)。"
                   "重機制、講原理,附名詞年表速查與互動開機流程。",
}

MODULES = (co_a.MODULES + co_b.MODULES + co_c.MODULES + co_d.MODULES + co_e.MODULES
           + co_f.MODULES + co_g.MODULES + co_h.MODULES)

REFERENCES = co_ref.REFERENCES
