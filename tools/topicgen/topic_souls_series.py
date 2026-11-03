# -*- coding: utf-8 -*-
"""魂系列主題的規格。"""
import sls_a, sls_c, sls_e, sls_ref

TOPIC = {
    "id": "souls-series",
    "category": "games",
    "title": u"魂系列的故事與設計：從惡魔靈魂到艾爾登法環",
    "short": u"魂系列的故事與設計",
    "crumb": u"魂系列",
    "icon": u"🗡️",
    "description": u"FromSoftware 與宮崎英高、魂系的機制與隱晦敘事；惡魔靈魂的波雷塔利亞；黑暗靈魂三部曲的初火、傳火、薪王與循環（含 DLC）；血源詛咒的血療、上位者與獵人夢境；隻狼的龍胤與四個結局；"
                   u"艾爾登法環的黃金律法、碎片戰爭、半神、瑪莉卡與拉達岡、六種結局、黃金樹幽影與黑夜君臨；難度哲學、關卡設計、戰鬥系統、非同步多人與類魂遊戲。主流玩家推論另行標註；含全系列劇透。",
}

_C = sls_a.MODULES[-1]
MODULES = sls_a.MODULES[:-1] + [(_C[0], _C[1] + sls_c.MODULES_C2)] + sls_c.MODULES[1:] + sls_e.MODULES
REFERENCES = sls_ref.REFERENCES
