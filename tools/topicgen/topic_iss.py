# -*- coding: utf-8 -*-
"""國際太空站 ISS 的規格。"""
import iss_a, iss_c, iss_e, iss_g, iss_ref

TOPIC = {
    "id": "iss",
    "category": "tech",
    "title": u"國際太空站 ISS：艙段、生活、科學任務與未來",
    "short": u"國際太空站",
    "crumb": u"國際太空站",
    "icon": u"🛰️",
    "description": u"國際太空站完整導覽：禮炮號、天空實驗室、和平號到 ISS 的歷史與國際合作；俄羅斯段、節點艙、命運號、哥倫布號、希望號、穹頂、桁架與機械手臂；"
                   u"電力、散熱、空氣、水回收、姿態與軌道維持；太空人的作息、飲食、睡眠、衛生、運動、身體與心理變化、太空漫步與緊急狀況；聯盟號、太空梭、貨運船、龍飛船與星際客機；"
                   u"人體、生物、植物、物理、阿爾法磁譜儀與地球觀測等科學任務；重大事件、紀錄與私人太空人；延壽、離軌、商業太空站與天宮。附可點選的太空站圖與互動模擬。",
}

MODULES = iss_a.MODULES + iss_c.MODULES + iss_e.MODULES + iss_g.MODULES

REFERENCES = iss_ref.REFERENCES
