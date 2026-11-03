# -*- coding: utf-8 -*-
"""法國大革命與拿破崙主題的規格。"""
import fr_a, fr_c, fr_e, fr_ref

TOPIC = {
    "id": "french-revolution",
    "category": "history",
    "title": u"法國大革命與拿破崙：從巴士底獄到滑鐵盧",
    "short": u"法國大革命與拿破崙",
    "crumb": u"法國大革命",
    "icon": u"🇫🇷",
    "description": u"舊制度、啟蒙思想、財政危機與三級會議；網球場誓言、巴士底獄、8 月 4 日之夜、人權宣言與教士公民組織法；瓦倫出逃、革命戰爭、8 月 10 日、九月屠殺、處決國王；吉倫特與山嶽派、羅伯斯比與恐怖統治、旺代、共和曆、熱月與督政府；"
                   u"拿破崙的崛起、霧月政變、民法典與宗教協定；加冕、奧斯特利茨、大陸封鎖、半島戰爭、遠征俄國、萊比錫、滑鐵盧與聖赫勒拿；維也納會議、革命的遺產與史學爭論。含歐洲勢力變化地圖、派系圖與年表。",
}

MODULES = fr_a.MODULES + fr_c.MODULES + fr_e.MODULES
REFERENCES = fr_ref.REFERENCES
