# -*- coding: utf-8 -*-
"""微中子主題的規格。"""
import neu_a, neu_f, neu_ref

TOPIC = {
    "id": "neutrinos",
    "category": "science",
    "title": u"微中子：追蹤幽靈粒子的一百年",
    "short": u"微中子",
    "crumb": u"微中子",
    "icon": u"👻",
    "description": u"貝他衰變的能量危機、包立的信、費米的理論；柯溫與萊因斯、緲子與陶子微中子；太陽怎麼發光、戴維斯的氯實驗、三十年的太陽微中子之謎；"
                   u"完整推導振盪、超級神岡的上下不對稱、SNO 的重水、MSW 效應；契忍可夫與閃爍體偵測器、事件重建、地下實驗室、卡方與費爾德曼—卡辛斯；"
                   u"大亞灣與 θ₁₃、T2K 與 NOvA、質量順序、CP 破壞；超新星 1987A、冰立方與耀變體、地球微中子；KATRIN、馬約拉納與翹翹板、惰性微中子、宇宙學；DUNE、Hyper-K 與 JUNO。附三個互動模擬。",
}

MODULES = neu_a.MODULES + neu_f.MODULES
REFERENCES = neu_ref.REFERENCES
