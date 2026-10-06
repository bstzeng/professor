# -*- coding: utf-8 -*-
"""歐洲各國主題的規格。"""
import eup_a, eup_wc, eup_sn, eup_e, eup_b, eup_ref

TOPIC = {
    "id": "europe-countries",
    "category": "geography",
    "title": u"歐洲各國：從英國、法國到土耳其",
    "short": u"歐洲各國",
    "crumb": u"歐洲各國",
    "icon": u"🇪🇺",
    "description": u"一國一課介紹歐洲 42 國，再用兩課介紹梵蒂岡、聖馬利諾、摩納哥、列支敦斯登、安道爾五個迷你國家。每課有位置地圖、一句話記憶、國旗、"
                   u"基本資料、主要城市、地理歷史、你好與謝謝、美食與伴手禮、世界遺產、節慶，以及旅遊建議與從台灣怎麼去。"
                   u"另有歐盟與申根、地形氣候與語言、國旗家族、世界遺產、美食地圖和歐洲與台灣，附互動地圖、找國家測驗、速查表與國旗一覽。",
}

MODULES = [eup_a.MODULE_A, eup_wc.MODULE_B, eup_wc.MODULE_C, eup_sn.MODULE_D, eup_sn.MODULE_E, eup_e.MODULE_F, eup_b.MODULE_G,
           eup_a.MODULE_H, eup_a.MODULE_I]

REFERENCES = eup_ref.REFERENCES
