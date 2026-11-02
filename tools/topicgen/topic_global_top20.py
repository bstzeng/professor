# -*- coding: utf-8 -*-
"""全球市值前 20 大公司：做什麼、怎麼賺錢、未來 15 年（gc_）。"""
import gc_a, gc_b, gc_c, gc_d, gc_ref

TOPIC = {
    "id": "global-top20",
    "category": "invest",
    "title": u"全球市值前 20 大公司：它們做什麼、怎麼賺錢、未來 15 年會怎樣",
    "short": u"全球市值前 20 大",
    "crumb": u"全球市值前 20 大",
    "icon": u"🏢",
    "description": u"蘋果、輝達、微軟、Google、亞馬遜、台積電、SpaceX、沙烏地阿美、特斯拉、Meta、博通、禮來、波克夏、三星、美光、沃爾瑪、摩根大通、超微、Visa、艾克森美孚：一家一課，從你每天碰到的產品出發，講清楚它的產業位置、營收結構、營利模式、護城河、風險、和台灣的關係，以及 5 年、10 年、15 年的三種情境展望。附二十大比較總表、市值排行賽跑、營收結構、成長情境模擬、簡易估值、護城河雷達與「你的一天」互動工具。",
}

MODULES = gc_a.MODULES + gc_b.MODULES + gc_c.MODULES + gc_d.MODULES
REFERENCES = gc_ref.REFERENCES
