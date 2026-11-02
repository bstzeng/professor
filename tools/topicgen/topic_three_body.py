# -*- coding: utf-8 -*-
"""三體主題的規格。"""
import tb_a, tb_c, tb_e, tb_ref

TOPIC = {
    "id": "three-body",
    "category": "fantasy",
    "title": u"三體：黑暗森林、智子與宇宙社會學",
    "short": u"三體",
    "crumb": u"三體",
    "icon": u"🪐",
    "description": u"劉慈欣三部曲完整導讀（完整劇透）：文革與葉文潔、紅岸基地、科學邊界、三體遊戲與人列計算機、地球三體組織、古箏行動與智子；"
                   u"面壁者與破壁人、水滴與末日之戰、黑暗森林法則、猜疑鏈與技術爆炸、章北海與黑暗戰役；程心與雲天明、執劍人、廣播紀元、三個童話、二向箔、647 號小宇宙與回歸運動。"
                   u"再逐一檢驗科學設定：三體問題、智子與量子糾纏、強交互作用力、微波背景輻射、太陽重力透鏡、費米悖論、曲率驅動、維度與真空衰變、相對論與引力波，最後討論賽局理論、程心爭議與中國科幻。",
}

MODULES = tb_a.MODULES + tb_c.MODULES + tb_e.MODULES
REFERENCES = tb_ref.REFERENCES
