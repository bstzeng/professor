# -*- coding: utf-8 -*-
"""異塵餘生 Fallout 全紀錄的規格。"""
import flo_a, flo_f, flo_ref

TOPIC = {
    "id": "fallout",
    "category": "games",
    "title": u"異塵餘生 Fallout 全紀錄：核子廢土的世界、作品與勢力",
    "short": u"Fallout",
    "crumb": u"Fallout",
    "icon": u"☢️",
    "description": u"永遠的 1950 年代與復古未來主義、資源戰爭與 2077 年的大戰、Vault-Tec 的避難所實驗、屍鬼與 FEV、瓶蓋與嗶嗶小子；從初代、《2》、黑島與 Van Buren、《3》、《新維加斯》、《4》、《76》到 Amazon 影集；"
                   u"鋼鐵兄弟會、英克雷、新加州共和國、凱撒軍團與豪斯先生、學院與合成人；戰爭從未改變、對 1950 年代美國的諷刺、灰色的選擇、真實的冷戰與核恐懼；S.P.E.C.I.A.L. 配點器、V.A.T.S.、多重解法與模組。重大暴雷會事先提醒。",
}

MODULES = flo_a.MODULES + flo_f.MODULES
REFERENCES = flo_ref.REFERENCES
