# -*- coding: utf-8 -*-
"""福爾摩斯與推理小說全紀錄的規格。"""
import dtc_a, dtc_f, dtc_ref

TOPIC = {
    "id": "detective-fiction",
    "category": "wuxia",
    "title": u"福爾摩斯與推理小說全紀錄",
    "short": u"推理小說",
    "crumb": u"推理小說",
    "icon": u"🔍",
    "description": u"愛倫坡與杜邦、推理的要素與公平；柯南・道爾與貝爾醫師、華生、溯因推理、經典案件、莫里亞蒂與萊辛巴赫、羅卡交換原理、改編；克莉絲蒂、東方快車與一個都不留、羅傑・艾克洛命案、諾克斯十誡與范達因二十條、昆恩的向讀者挑戰、卡爾的密室講義；"
                   u"漢密特與錢德勒、警察小說、心理懸疑與北歐黑色；江戶川亂步、橫溝正史、松本清張、島田莊司與新本格、宮部美幸、東野圭吾、湊佳苗；詭計圖鑑、華文推理與柯南。重大暴雷會事先提醒。",
}

MODULES = dtc_a.MODULES + dtc_f.MODULES
REFERENCES = dtc_ref.REFERENCES
