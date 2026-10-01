# -*- coding: utf-8 -*-
"""圍棋入門主題的規格。"""
import go_a, go_c, go_e, go_h, go_ref

TOPIC = {
    "id": "go-basics",
    "category": "life",
    "title": "圍棋入門：從會規則到會下棋",
    "short": "圍棋入門",
    "crumb": "圍棋入門",
    "icon": "⚫",
    "description": "給已經知道規則、卻不知道怎麼下的人：從吃子技巧（征子、枷、倒撲、接不歸）、連接與切斷、"
                   "死活（真假眼、直三彎三、刀把五、雙活、對殺），到好形、布局、定石、中盤攻防與官子。"
                   "每課都有可以點擊作答的棋盤練習，所有題目的答案都經過程式搜尋驗證；附互動棋盤與速查表。",
}

MODULES = go_a.MODULES + go_c.MODULES + go_e.MODULES + go_h.MODULES

REFERENCES = go_ref.REFERENCES
