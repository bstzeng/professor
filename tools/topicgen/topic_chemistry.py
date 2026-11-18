# -*- coding: utf-8 -*-
"""化學：元素與化學鍵的規格。"""
import chm_a, chm_f, chm_ref

TOPIC = {
    "id": "chemistry",
    "category": "science",
    "title": u"化學：元素與化學鍵",
    "short": u"化學",
    "crumb": u"化學",
    "icon": u"⚗️",
    "description": u"元素、化合物與混合物、原子結構與同位素、莫耳；軌域、電子組態、門得列夫與週期表、原子半徑、游離能與電負度、各族元素；"
                   u"離子鍵、共價鍵與路易斯結構、VSEPR 分子形狀、極性與氫鍵、金屬鍵、有機分子與手性；反應式、焓、活化能與催化劑、化學平衡與勒沙特列、熵與自由能；"
                   u"溶解度、酸鹼與 pH、緩衝與血液、氧化還原、電池與電解；塑膠與半導體、藥物、化學工業與環境。附互動週期表、3D 分子形狀、反應速率與滴定曲線。",
}

MODULES = chm_a.MODULES + chm_f.MODULES
REFERENCES = chm_ref.REFERENCES
