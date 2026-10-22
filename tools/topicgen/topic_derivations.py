# -*- coding: utf-8 -*-
"""數學公式是怎麼推導出來的主題的規格。"""
import md_a, md_d, md_f, md_i, md_ref

TOPIC = {
    "id": "math-derivations",
    "category": "math",
    "title": u"數學公式是怎麼推導出來的",
    "short": u"公式怎麼推導",
    "crumb": u"公式怎麼推導",
    "icon": u"✏️",
    "description": u"從高中到大一微積分，51 條公式逐步推導：每一步標出用了哪一招（代換、拆開重組、對稱、極限、歸納、反證……），可展開「為什麼可以？」，"
                   u"再用拉桿與圖形親手驗證。涵蓋畢氏定理、圓面積、等比級數、一元二次公式、二項式定理、e、和角公式、海龍公式、導數與積分的各條規則、"
                   u"球體積、泰勒展開、尤拉公式、巴塞爾問題、斯特靈公式、高斯積分、常態分布、行列式、最小平方法，以及自由落體、向心加速度、克卜勒第三定律、單擺與因次分析。",
}

MODULES = md_a.MODULES + md_d.MODULES + md_f.MODULES + md_i.MODULES

REFERENCES = md_ref.REFERENCES
