# -*- coding: utf-8 -*-
"""沙丘主題的規格。"""
import dn_a, dn_e, dn_ref

TOPIC = {
    "id": "dune",
    "category": "fantasy",
    "title": "沙丘：香料、沙漠與救世主的警告",
    "short": "沙丘",
    "crumb": "沙丘",
    "icon": "🏜️",
    "description": "法蘭克·赫伯特六部曲完整導讀：作者與出版史、巴特勒聖戰與沒有電腦的封建宇宙、宇航公會、貝尼·傑瑟里特、門塔特與香料經濟；"
                   "沙蟲、弗瑞曼人與水的文化；《沙丘》劇情逐課解析，續集《救世主》《沙丘之子》《神帝》《異端》《聖殿》；"
                   "生態、救世主、宗教、預知與爭議等主題；佐杜洛夫斯基、林區、影集與維勒納夫電影。附互動地圖、年表、勢力圖與人物卡。",
}

MODULES = dn_a.MODULES + dn_e.MODULES

REFERENCES = dn_ref.REFERENCES
