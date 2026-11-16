# -*- coding: utf-8 -*-
"""黑洞主題的規格。"""
import bhl_a, bhl_f, bhl_ref

TOPIC = {
    "id": "black-holes",
    "category": "science",
    "title": u"黑洞：從史瓦西解到事件視界望遠鏡",
    "short": u"黑洞",
    "crumb": u"黑洞",
    "icon": u"🕳️",
    "description": u"米歇爾的暗星、史瓦西解、事件視界與奇異點、時間膨脹、光子球與 ISCO；錢德拉塞卡極限、中子星與脈衝星、超新星、歐本海默—史奈德塌縮；"
                   u"克爾解、能層與彭羅斯過程、無毛定理；天鵝座 X-1、吸積盤、類星體、噴流、人馬座 A*；事件視界望遠鏡的 VLBI、資料、影像重建、M87* 與人馬座 A*；"
                   u"重力波中的黑洞、質量間隙、中等質量黑洞；霍金輻射、黑洞熱力學、貝肯斯坦熵、資訊悖論、全像原理；原始黑洞、蟲洞、《星際效應》、早期宇宙的巨型黑洞。附四個互動模擬。",
}

MODULES = bhl_a.MODULES + bhl_f.MODULES
REFERENCES = bhl_ref.REFERENCES
