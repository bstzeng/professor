# -*- coding: utf-8 -*-
"""京都動畫作品全紀錄主題的規格。"""
import kya_a, kya_f, kya_ref

TOPIC = {
    "id": "kyoto-animation",
    "category": "anime",
    "title": u"京都動畫作品全紀錄：從宇治到全世界",
    "short": u"京都動畫",
    "crumb": u"京都動畫",
    "icon": u"🎞️",
    "description": u"宇治的上色工作室、承包時代、Key 三部作、涼宮春日現象；幸運☆星、日常、K-ON!、冰菓、中二病與 Free!、吹響吧！上低音號、聲之形、紫羅蘭永恆花園；"
                   u"空氣感、演技作畫、光與色彩、聖地巡禮、音樂；正職員工與內部培養、導演們、京都動畫大賞；2019 年第一工作室事件、哀悼與重建；影響與批評。含部分劇情（有暴雷）。",
}

MODULES = kya_a.MODULES + kya_f.MODULES
REFERENCES = kya_ref.REFERENCES
