# -*- coding: utf-8 -*-
"""資安事件全紀錄的規格。"""
import cyb_a, cyb_b, cyb_ref

TOPIC = {
    "id": "cyber-incidents", "category": "tech",
    "title": u"資安事件全紀錄：29 起事件的背景、經過與改進",
    "short": u"資安事件", "crumb": u"資安事件", "icon": u"🛡️",
    "description": u"攻擊鏈與事件調查；蠕蟲與病毒（莫里斯、ILOVEYOU、Slammer、Conficker）、國家級攻擊（震網、烏克蘭電網、NotPetya、SolarWinds、美國電信業者遭入侵）、勒索軟體（WannaCry、中油台塑、美國燃油管線、Kaseya、愛爾蘭衛生署、MOVEit、馬偕與彰基）、"
                   u"資料外洩（Yahoo、Equifax、萬豪、Capital One）、漏洞與供應鏈（心臟出血、Log4Shell、xz 後門、CrowdStrike 當機）、社交工程與金融（孟加拉央行、第一銀行 ATM、Twitter、Uber、Bybit），每一起整理背景、經過、原因與改進；附勒索軟體攻擊鏈動畫、改進關係圖與台灣的資安制度。",
}
MODULES = cyb_a.MODULES + cyb_b.MODULES
REFERENCES = cyb_ref.REFERENCES
