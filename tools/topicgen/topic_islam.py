# -*- coding: utf-8 -*-
"""伊斯蘭教主題的規格。"""
import is_a, is_b, is_ref

TOPIC = {
    "id": "islam",
    "category": "religion",
    "title": u"伊斯蘭教：歷史與教義",
    "short": u"伊斯蘭教",
    "crumb": u"伊斯蘭教",
    "icon": u"☪️",
    "description": u"從七世紀的阿拉伯半島講起：先知穆罕默德、遷徙與麥地那社群；《古蘭經》的成書與內容、聖訓與經注；"
                   u"認主獨一、六大信仰與五功；沙里亞、法學派、清真、婚姻家庭與吉哈德的原意；遜尼與什葉、蘇菲主義、神學與哲學；"
                   u"從四大哈里發、阿拔斯黃金時代、安達魯斯、十字軍與蒙古到三大火藥帝國；殖民、改革、伊朗革命與極端主義；"
                   u"中國與台灣的伊斯蘭。以理解為目的，並列不同觀點。附伊斯蘭曆換算、教派關係圖與歷史時間軸。",
}

MODULES = is_a.MODULES + is_b.MODULES

REFERENCES = is_ref.REFERENCES
