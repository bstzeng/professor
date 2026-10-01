# -*- coding: utf-8 -*-
"""作業系統是怎麼寫出來的主題的規格。"""
import os_a, os_e, os_ref

TOPIC = {
    "id": "os-dev",
    "category": "tech",
    "title": "作業系統是怎麼寫出來的：從開機到 Shell",
    "short": "作業系統是怎麼寫出來的",
    "crumb": "作業系統開發",
    "icon": "🖥️",
    "description": "跟著一個極簡的教學用 x86-64 核心，從按下電源、BIOS／UEFI、開機程式、進入 64 位元長模式，到中斷與例外、計時器、鍵盤；"
                   "實體記憶體、四層頁表、核心堆積、寫入時複製；行程、情境切換、排程、系統呼叫、ELF 載入、fork／exec、同步與死結；"
                   "驅動程式、PCI、磁碟、VFS、檔案系統與日誌；最後完成終端機、Shell、管線與 libc，並對照 Linux、Windows、macOS。附頁表、排程、競爭條件等互動實驗。",
}

MODULES = os_a.MODULES + os_e.MODULES

REFERENCES = os_ref.REFERENCES
