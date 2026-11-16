# -*- coding: utf-8 -*-
"""重力波主題的規格。"""
import gwv_a, gwv_f, gwv_ref

TOPIC = {
    "id": "gravitational-waves",
    "category": "science",
    "title": u"重力波：LIGO 怎麼量到比質子還小數百倍的位移",
    "short": u"重力波",
    "crumb": u"重力波",
    "icon": u"🌊",
    "description": u"時空的漣漪、愛因斯坦的預言與懷疑、教堂山與黏珠子；線性化重力、兩種偏振、四極公式、啾聲質量；赫爾斯—泰勒脈衝雙星；韋伯棒與錯誤的發現；"
                   u"邁克生干涉儀、共振腔、功率回收、隔振、熱雜訊、量子極限與壓縮光、超高真空；應變資料、匹配濾波、範本庫、偽警報率、時間平移、定位、貝氏參數估計、雜訊瞬變；"
                   u"GW150914、盲注入、2017 年諾貝爾獎、GW170817 與多信使天文學；黑洞族群、重力波速度、標準汽笛、脈衝星計時陣列；愛因斯坦望遠鏡與 LISA。附三個互動模擬。",
}

MODULES = gwv_a.MODULES + gwv_f.MODULES
REFERENCES = gwv_ref.REFERENCES
