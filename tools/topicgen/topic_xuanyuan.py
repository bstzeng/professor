# -*- coding: utf-8 -*-
"""軒轅劍歷代故事主題的規格。"""
import xy_a, xy_e, xy_ref

TOPIC = {
    "id": "xuanyuan-sword",
    "category": "games",
    "title": u"軒轅劍歷代故事：一部奇幻的中國史",
    "short": u"軒轅劍歷代故事",
    "crumb": u"軒轅劍歷代故事",
    "icon": u"🗡️",
    "description": u"軒轅劍單機正傳與外傳的完整劇情（含結局暴雷）：楓之舞的墨家與煉妖壺；參代法蘭克騎士賽特從威尼斯到長安的王道之旅；天之痕陳靖仇、于小雪、拓跋玉兒與宇文拓；"
                   u"肆代墨家少女水鏡與張良；蒼之濤改寫淝水之戰；伍代山海界；漢之雲、雲之遙的軒轅劍轉世兄弟；陸代牧野之戰；穹之扉的天門與武丁；柒代王莽新朝的天書與黑火。附發行與故事年表、神州與歐亞地圖、跨代人物、全系列結局對照等互動工具。",
}

MODULES = xy_a.MODULES + xy_e.MODULES

REFERENCES = xy_ref.REFERENCES
