# -*- coding: utf-8 -*-
"""賽局理論主題的規格。"""
import gt_a, gt_e, gt_ref

TOPIC = {
    "id": "game-theory",
    "category": "math",
    "title": u"賽局理論：從囚犯困境到拍賣與 AI",
    "short": u"賽局理論",
    "crumb": u"賽局理論",
    "icon": u"♟️",
    "description": u"當你的結果取決於別人怎麼做：報酬矩陣、優勢策略、囚犯困境、納許均衡、協調與膽小鬼賽局；混合策略、足球 PK 與極小極大；賽局樹、逆向歸納、"
                   u"可信威脅與承諾；重複賽局、以牙還牙、演化與鷹鴿；訊號、檸檬市場、篩選與道德風險；公共財、公地悲劇、寡占、談判、拍賣、投票、大學分發與核威懾；"
                   u"行為賽局、機制設計、AI 與區塊鏈。附報酬矩陣求解器、囚犯困境對戰、錦標賽、拍賣與配對等十個互動工具。",
}

MODULES = gt_a.MODULES + gt_e.MODULES

REFERENCES = gt_ref.REFERENCES
