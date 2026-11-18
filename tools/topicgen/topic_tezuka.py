# -*- coding: utf-8 -*-
"""手塚治虫全紀錄的規格。"""
import tzk_a, tzk_f, tzk_ref

TOPIC = {
    "id": "tezuka",
    "category": "anime",
    "title": u"手塚治虫全紀錄：漫畫之神的作品與影響",
    "short": u"手塚治虫",
    "crumb": u"手塚治虫",
    "icon": u"🦾",
    "description": u"寶塚的童年與昆蟲、戰爭與醫學、《新寶島》的電影式分鏡；原子小金剛、森林大帝與緞帶騎士、火之鳥、怪醫黑傑克、佛陀、三眼神童與多羅羅、阿道夫之謎、奇子與 MW；"
                   u"蟲製作與第一部電視動畫、有限動畫與低價承包、實驗動畫、倒閉與再起；生命的尊嚴、科技與人性、戰爭、明星系統；常盤莊、宮崎駿的批評、台灣的「怪醫秦博士」、手塚治虫文化賞與 PLUTO。",
}

MODULES = tzk_a.MODULES + tzk_f.MODULES
REFERENCES = tzk_ref.REFERENCES
