# -*- coding: utf-8 -*-
"""皇宮裡的人與官主題的規格。"""
import pg_a, pg_c, pg_e, pg_g, pg_ref

TOPIC = {
    "id": "imperial-palace",
    "category": "history",
    "title": u"皇宮裡的人與官：從三公九卿到紫禁城",
    "short": u"皇宮裡的人與官",
    "crumb": u"皇宮裡的人與官",
    "icon": u"🏯",
    "description": u"皇宮裡到底有多少人？宦官、宮女、后妃、侍衛、工匠與皇族的人數與來源，並把史料記載與學者估計分開說明；"
                   u"從秦漢三公九卿、隋唐三省六部、宋代二府三司、明代內閣與司禮監到清代軍機處，看懂兩千年中央官制各管什麼；"
                   u"監察、三法司與廠衛；明代二十四衙門與清代內務府；九品十八級、補服頂戴、俸祿與科舉入仕；"
                   u"最後走一遍紫禁城：建造、中軸線、三大殿、後三宮、養心殿、建築密碼、防火排水，以及兩岸故宮。附紫禁城互動平面圖、官制組織圖、品級對照器等工具。",
}

MODULES = pg_a.MODULES + pg_c.MODULES + pg_e.MODULES + pg_g.MODULES

REFERENCES = pg_ref.REFERENCES
