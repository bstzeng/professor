# -*- coding: utf-8 -*-
"""船難全紀錄的規格。"""
import swk_a, swk_b, swk_ref

TOPIC = {
    "id": "shipwrecks", "category": "tech",
    "title": u"船難全紀錄：25 起船難的背景、經過與改進",
    "short": u"船難", "crumb": u"船難", "icon": u"🚢",
    "description": u"浮力、重心、穩心與自由液面；SOLAS、MARPOL、ISM 等海上安全公約；25 起船難依主題分類——救生與公約（鐵達尼號、愛爾蘭皇后號）、穩定性與翻覆（東方號、世越號、東方之星）、滾裝船艙門（自由企業先驅號、愛沙尼亞號）、超載與渡輪（太平輪、多尼亞帕茲號、喬拉號、薩拉姆 98、地中海移民船）、"
                   u"戰爭（盧西塔尼亞號、威廉古斯特洛夫號）、天氣（洞爺丸、埃爾法羅號）、碰撞（安德里亞多利亞號、歌詩達協和號）、油汙（托利峽谷號、艾克森瓦德茲號、威望號）、港口與其他（長賜號、大達利號、庫斯克號、貝葉斯號），每一起整理背景、經過、原因與改進；附穩定性模擬與改進關係圖。",
}
MODULES = swk_a.MODULES + swk_b.MODULES
REFERENCES = swk_ref.REFERENCES
