# -*- coding: utf-8 -*-
"""機動戰士鋼彈（宇宙世紀）主題的規格。"""
import gun_a, gun_c, gun_e, gun_ref

TOPIC = {
    "id": "gundam-uc",
    "category": "anime",
    "title": u"機動戰士鋼彈：宇宙世紀全解析",
    "short": u"機動戰士鋼彈",
    "crumb": u"機動戰士鋼彈",
    "icon": u"🤖",
    "description": u"富野由悠季與 1979 年的《機動戰士鋼彈》、真實系機器人、鋼彈系列全景與觀看順序；太空殖民地與拉格朗日點、地球聯邦與吉翁、米諾夫斯基粒子、機動戰士與新人類；"
                   u"一年戰爭（阿姆羅、夏亞、拉拉、蘭巴・拉爾、08MS 小隊、0080）、0083、Z、ZZ、逆襲的夏亞、UC、閃光的哈薩維、F91、V 鋼彈（完整劇透）；主要人物論；戰爭與正義、新人類與相互理解、重力與特權、少年兵、人形兵器的工程學、鋼普拉，以及對日本與台灣的影響。",
}

MODULES = gun_a.MODULES + gun_c.MODULES + gun_e.MODULES
REFERENCES = gun_ref.REFERENCES
