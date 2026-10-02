# -*- coding: utf-8 -*-
"""冰與火之歌主題的規格。"""
import ia_a, ia_e, ia_ref

TOPIC = {
    "id": "song-of-ice-and-fire",
    "category": "fantasy",
    "title": "冰與火之歌：權力遊戲、凜冬與龍",
    "short": "冰與火之歌",
    "crumb": "冰與火之歌",
    "icon": "🐺",
    "description": "喬治·R·R·馬汀的史詩奇幻完整導讀：POV 寫法與出版史；先民、長夜、瓦雷利亞、伊耿征服、血龍狂舞與篡奪者戰爭；"
                   "九大家族與陰謀家；長城、異鬼、厄斯索斯、宗教與魔法；五部劇情逐課解析（奈德之死、五王之戰、血色婚禮、紫色婚禮、瓊恩之死）；"
                   "灰色人物、權力、戰爭、預言、玫瑰戰爭原型與讀者理論；《血與火》、鄧克與蛋、HBO 影集與爭議結局。附互動地圖、家族圖與人物卡。",
}

MODULES = ia_a.MODULES + ia_e.MODULES

REFERENCES = ia_ref.REFERENCES
