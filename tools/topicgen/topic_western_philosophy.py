# -*- coding: utf-8 -*-
"""西方哲學史主題的規格。"""
import phl_a, phl_c, phl_e, phl_ref

TOPIC = {
    "id": "western-philosophy",
    "category": "history",
    "title": u"西方哲學史：從蘇格拉底到現代",
    "short": u"西方哲學史",
    "crumb": u"西方哲學",
    "icon": u"🏛️",
    "description": u"哲學的三大問題與思想實驗；米利都學派、赫拉克利特與巴門尼德、畢達哥拉斯、原子論與詭辯家、蘇格拉底、柏拉圖、亞里斯多德、斯多噶、伊比鳩魯、懷疑論；奧古斯丁、經院哲學、阿奎那、奧坎；"
                   u"馬基維利、培根、笛卡兒、史賓諾莎、萊布尼茲、洛克、柏克萊、休謨、康德；霍布斯、洛克、盧梭、彌爾、黑格爾、馬克思；叔本華、齊克果、尼采、現象學、存在主義、分析哲學、科學哲學、後現代；羅爾斯與諾齊克、三大倫理學派、心靈哲學與 AI。每課附「東方怎麼說」對照，含哲學家時間軸、影響關係圖與思想實驗圖鑑。",
}

MODULES = phl_a.MODULES + phl_c.MODULES + phl_e.MODULES
REFERENCES = phl_ref.REFERENCES
