# -*- coding: utf-8 -*-
"""檔案格式解剖學主題規格。"""
import fmt_a, fmt_b, fmt_c, fmt_d, fmt_e, fmt_f, fmt_g, fmt_h, fmt_i, fmt_m, fmt_ref

TOPIC = {
    "id": "file-formats",
    "category": "tech",
    "title": "檔案格式解剖學：JPG、MP3、ZIP 裡面到底存了什麼",
    "short": "檔案格式解剖學",
    "crumb": "檔案格式解剖學",
    "icon": "🗂️",
    "description": "用十六進位檢視器，一個位元組一個位元組拆開常見檔案：JPG 怎麼壓縮、"
                   "PNG 與 ZIP 的區塊結構、MP3 的心理聲學、字型與 3D 模型、影片的容器與編碼、"
                   "docx 其實是 ZIP、憑證與醫學影像，最後談檔案損壞、偽裝與資安。每課都有可下載的範例檔。",
}

MODULES = (fmt_a.MODULES + fmt_b.MODULES + fmt_c.MODULES + fmt_d.MODULES + fmt_e.MODULES
           + fmt_f.MODULES + fmt_g.MODULES + fmt_h.MODULES + fmt_i.MODULES + fmt_m.MODULES)

REFERENCES = fmt_ref.REFERENCES
