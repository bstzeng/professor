# -*- coding: utf-8 -*-
"""線性代數：從向量到 SVD、PCA 與 PageRank（la_）。"""
import la_a, la_c, la_e, la_h, la_ref

TOPIC = {
    "id": "linear-algebra",
    "category": "math",
    "title": u"線性代數：從向量、矩陣到特徵值、SVD 與 AI",
    "short": u"線性代數",
    "crumb": u"線性代數",
    "icon": u"🧮",
    "description": u"以幾何直覺與應用為主的線性代數：向量與方程組、矩陣即變換、向量空間與四個基本子空間、行列式、正交與最小平方、特徵值與對角化，一路到 SVD、影像壓縮、PCA、PageRank、電腦圖學與機器學習，附 2D 變換遊樂場等互動元件。",
}

MODULES = la_a.MODULES + la_c.MODULES + la_e.MODULES + la_h.MODULES
REFERENCES = la_ref.REFERENCES
