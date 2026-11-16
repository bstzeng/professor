# -*- coding: utf-8 -*-
"""新海誠作品全紀錄主題的規格。"""
import shk_a, shk_f, shk_ref

TOPIC = {
    "id": "makoto-shinkai",
    "category": "anime",
    "title": u"新海誠作品全紀錄：從《星之聲》到《鈴芽之旅》",
    "short": u"新海誠",
    "crumb": u"新海誠",
    "icon": u"🌠",
    "description": u"長野、Falcom 與一個人的動畫革命；天空、光與距離的風格；她與她的貓、星之聲、雲之彼端約定的地方、秒速5公分、追逐繁星的孩子、言葉之庭；"
                   u"災難三部曲你的名字、天氣之子、鈴芽之旅與 311；少年少女與大人、擦身而過與重逢；背景美術、CoMix Wave Films、影像分鏡、RADWIMPS、聖地巡禮；"
                   u"天空與天氣、日常的美、神話與信仰、災難的記憶；與宮崎駿的比較、小說與改編。含完整劇情（有暴雷）。",
}

MODULES = shk_a.MODULES + shk_f.MODULES
REFERENCES = shk_ref.REFERENCES
