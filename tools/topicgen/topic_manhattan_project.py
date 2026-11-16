# -*- coding: utf-8 -*-
"""曼哈頓計畫主題的規格。"""
import mhp_a, mhp_f, mhp_ref

TOPIC = {
    "id": "manhattan-project",
    "category": "history",
    "title": u"曼哈頓計畫：從核分裂的發現到原子彈與冷戰",
    "short": u"曼哈頓計畫",
    "crumb": u"曼哈頓計畫",
    "icon": u"☢️",
    "description": u"放射性、中子、費米、核分裂的發現與邁特納；西拉德、愛因斯坦的信、MAUD 報告、德國與日本與蘇聯的核計畫；"
                   u"臨界質量、鈾濃縮、芝加哥一號堆、鈽；格羅夫斯與歐本海默、橡樹嶺、漢福德、洛斯阿拉莫斯；小男孩、鈽的危機、內爆、三位一體試爆；"
                   u"投彈決策、廣島、長崎、輻射效應、日本投降的史學爭論；福克斯與羅森堡、蘇聯原子彈；氫彈、沙皇炸彈、第五福龍丸、古巴飛彈危機；"
                   u"歐本海默聽證會、大科學、核電與核醫、核不擴散。附三個互動模擬。",
}

MODULES = mhp_a.MODULES + mhp_f.MODULES
REFERENCES = mhp_ref.REFERENCES
