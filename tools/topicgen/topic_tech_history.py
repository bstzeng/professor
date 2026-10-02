# -*- coding: utf-8 -*-
"""人類科技發展史主題的規格。"""
import th_a, th_f, th_ref

TOPIC = {
    "id": "tech-history",
    "category": "tech",
    "title": "人類科技發展史：從用火到 AI",
    "short": "人類科技發展史",
    "crumb": "科技發展史",
    "icon": "🔥",
    "description": "從約 330 萬年前的第一把石器、掌握火、農業革命，到青銅、文字、輪子、鐵器；希臘、羅馬、秦漢的古典技術；"
                   "造紙、印刷、火藥、指南針與伊斯蘭黃金時代；印刷機、大航海與科學革命；蒸汽機與兩次工業革命；原子、太空、電晶體，"
                   "一直到網際網路、智慧型手機與生成式 AI。每課分析「為什麼在這時候、這裡出現」，附可縮放的總時間軸、蒸汽機動畫與前置技術關係圖。",
}

MODULES = th_a.MODULES + th_f.MODULES

REFERENCES = th_ref.REFERENCES
