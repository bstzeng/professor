# -*- coding: utf-8 -*-
"""統計物理與相變主題的規格。"""
import ss_a, ss_e, ss_ref

TOPIC = {
    "id": "statistical-physics",
    "category": "science",
    "title": "統計物理與相變：從原子的亂到宏觀的序",
    "short": "統計物理與相變",
    "crumb": "統計物理與相變",
    "icon": "🎲",
    "description": "大數法則、隨機漫步與布朗運動；熵 S = k ln W、時間之箭、馬克士威妖與蘭道爾原理、自由能；統計系綜、波茲曼因子、"
                   "配分函數、負溫度、速度分布與漲落；費米—狄拉克、玻色—愛因斯坦、BEC、超流；相圖、序參量與對稱性破缺、伊辛模型、"
                   "昂薩格解、臨界現象與普適性；重整化群；滲流、玻璃、AI 與湧現。附八個互動模擬。",
}

MODULES = ss_a.MODULES + ss_e.MODULES

REFERENCES = ss_ref.REFERENCES
