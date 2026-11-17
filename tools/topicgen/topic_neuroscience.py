# -*- coding: utf-8 -*-
"""神經科學主題的規格。"""
import brn_a, brn_f, brn_ref

TOPIC = {
    "id": "neuroscience",
    "category": "biomed",
    "title": u"神經科學：大腦如何運作",
    "short": u"神經科學",
    "crumb": u"神經科學",
    "icon": u"🧠",
    "description": u"大腦的數字與腦區、從顱相學到卡哈爾；神經元、膜電位、動作電位與霍奇金—赫胥黎、髓鞘、突觸與羅威的夢、神經傳導物質、赫布與 LTP；"
                   u"視網膜、休伯爾與威澤爾、視錯覺、耳蝸、感覺小人與幻肢；運動皮質、小腦、基底核與帕金森、多巴胺與獎勵預測誤差、習慣與成癮；"
                   u"H.M.、記憶與間隔效應、位置細胞、杏仁核、蓋吉與前額葉；睡眠、意識的困難問題、裂腦人、阿茲海默症與中風；腦造影、腦機介面、大腦與 AI。附五個互動模擬。",
}

MODULES = brn_a.MODULES + brn_f.MODULES
REFERENCES = brn_ref.REFERENCES
