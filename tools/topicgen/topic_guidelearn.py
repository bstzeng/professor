# -*- coding: utf-8 -*-
"""引導孩子學習主題的規格。"""
import gl_a, gl_e, gl_ref

TOPIC = {
    "id": "guiding-learning",
    "category": "edu",
    "title": u"引導孩子學習：學習科學給家長的實用 Tips",
    "short": u"引導孩子學習",
    "crumb": u"引導孩子學習",
    "icon": u"📚",
    "description": u"從工作記憶、遺忘曲線與必要難度出發，逐一實作學習科學的六大策略（提取、間隔、交錯、精緻化、具體例子、雙重編碼）與費曼學習法；談動機、成長心態、回饋與錯題本；"
                   u"鷹架、提問階梯、等待時間與後設認知；閱讀、寫作、CPA 數學、英語、自然與社會的分科引導；讀書時間、考前準備與考試焦慮、補習、學習困難與資優；"
                   u"以及 AI 時代怎麼把 AI 當家教而不是槍手。附遺忘曲線模擬、間隔複習表、提問階梯、CPA 示範、專注計時器與情境演練。",
}

MODULES = gl_a.MODULES + gl_e.MODULES

REFERENCES = gl_ref.REFERENCES
