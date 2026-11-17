# -*- coding: utf-8 -*-
"""質數與黎曼猜想主題的規格。"""
import rie_a, rie_f, rie_ref

TOPIC = {
    "id": "riemann-hypothesis",
    "category": "math",
    "title": u"質數與黎曼猜想：數學最重要的未解問題",
    "short": u"質數與黎曼猜想",
    "crumb": u"黎曼猜想",
    "icon": u"🔢",
    "description": u"質數無窮多、篩法、質數分布的不規則；高斯與勒讓德、對數積分、切比雪夫、1896 年質數定理；巴塞爾問題、歐拉乘積、解析延拓與 −1/12、函數方程、平凡零點與臨界帶；"
                   u"黎曼 1859 年的論文、顯式公式、黎曼猜想、質數的音樂；十兆個零點、哈代與臨界線上的比例、斯奎斯數、羅賓不等式、失敗的證明；蒙哥馬利與戴森、隨機矩陣、希爾伯特—波利亞與量子混沌；"
                   u"RSA、張益唐與有界間隙、哥德巴赫、L 函數與韋伊猜想、千禧年大獎。附五個互動模擬（ζ 零點即時計算）。",
}

MODULES = rie_a.MODULES + rie_f.MODULES
REFERENCES = rie_ref.REFERENCES
