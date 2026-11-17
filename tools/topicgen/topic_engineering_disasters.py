# -*- coding: utf-8 -*-
"""工程災難與事故調查主題的規格。"""
import eda_a, eda_f, eda_ref

TOPIC = {
    "id": "engineering-disasters",
    "category": "tech",
    "title": u"工程災難與事故調查",
    "short": u"工程災難",
    "crumb": u"工程災難",
    "icon": u"⚠️",
    "description": u"安全規則是用血寫成的：瑞士乳酪模型與正常事故；塔科馬海峽吊橋的顫振、凱悅天橋、三豐百貨、921 東星大樓、莫蘭迪橋；自由輪、彗星客機、阿囉哈 243、華航 611 的疲勞；"
                   u"阿波羅 1 號、挑戰者號與費曼的冰水、哥倫比亞號、火星氣候探測者號、亞利安 5 號；三哩島、車諾比、福島、深水地平線；特內里費、法航 447、737 MAX；"
                   u"Therac-25、北美大停電、Knight Capital、CrowdStrike；博帕爾、高雄氣爆、泰坦號；偏差常態化、共同原因、人因工程。附四個互動模擬。",
}

MODULES = eda_a.MODULES + eda_f.MODULES
REFERENCES = eda_ref.REFERENCES
