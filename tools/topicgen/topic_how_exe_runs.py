# -*- coding: utf-8 -*-
"""執行檔是怎麼跑起來的：主題規格。"""
import ex_j, ex_k, ex_l, ex_ref

TOPIC = {
    "id": "how-exe-runs",
    "category": "tech",
    "title": "執行檔是怎麼跑起來的：從雙擊到程式結束",
    "short": "執行檔是怎麼跑起來的",
    "crumb": "執行檔是怎麼跑起來的",
    "icon": "⚙️",
    "description": "從原始碼到 exe 的編譯、組譯、連結，親手拆解一個 184 位元組、真的能執行的手寫程式，"
                   "再一步步追蹤雙擊之後作業系統做的每一件事——安全關卡、建立行程、載入記憶體、"
                   "接上函式、跑到 main、執行到結束，最後對照 Linux／macOS 並介紹觀察工具。",
}

MODULES = ex_j.MODULES + ex_k.MODULES + ex_l.MODULES

REFERENCES = ex_ref.REFERENCES
