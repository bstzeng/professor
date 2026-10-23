# -*- coding: utf-8 -*-
"""魔術方塊主題的規格。"""
import rb_a, rb_c, rb_ref

TOPIC = {
    "id": "rubiks-cube",
    "category": "life",
    "title": u"魔術方塊：從看懂記號到相機自動求解",
    "short": u"魔術方塊",
    "crumb": u"魔術方塊",
    "icon": u"🧊",
    "description": u"用可拖曳的 3D 動畫學會解魔術方塊：構造與記號；層先法七步（白十字、角塊、第二層、黃十字、黃邊、黃角歸位與翻轉）；"
                   u"CFOP 速解（F2L、兩步 OLL 十個公式、兩步 PLL 六個公式）；狀態數、上帝之數 20 與科先巴兩階段演算法。"
                   u"附相機解方塊工具：拍照六面、校正顏色、自動辨識，算出約 20 步的解並用 3D 與逐步示意圖帶你轉。",
}

MODULES = rb_a.MODULES + rb_c.MODULES

REFERENCES = rb_ref.REFERENCES
