# -*- coding: utf-8 -*-
"""美國五十州主題的規格。"""
import ust_a, ust_ne, ust_mw, ust_s, ust_w, ust_ref

TOPIC = {
    "id": "us-states",
    "category": "geography",
    "title": u"美國五十州：位置、州旗與特色",
    "short": u"美國五十州",
    "crumb": u"美國五十州",
    "icon": u"🗽",
    "description": u"一州一課，依東北、中西部、南部、西部四大區域介紹五十州：每課有位置地圖、一句話記憶、基本資料、州旗、"
                   u"地理與歷史、大企業、代表食物、華人社群、景點與冷知識。另有華盛頓特區、波多黎各與關島等屬地、五十州大比較，"
                   u"以及華人在美國的歷史；附可點選的互動地圖、找州測驗、加入順序動畫與州旗一覽。",
}

MODULES = [ust_a.MODULE_A] + ust_ne.MODULES + ust_mw.MODULES + ust_s.MODULES + ust_w.MODULES + [ust_a.MODULE_F]

REFERENCES = ust_ref.REFERENCES
