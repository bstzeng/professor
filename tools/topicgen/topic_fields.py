# -*- coding: utf-8 -*-
"""菲爾茲獎主題的規格。"""
import fm_a, fm_b, fm_d, fm_f, fm_ref

TOPIC = {
    "id": "fields-medal",
    "category": "nobel",
    "title": u"菲爾茲獎：九十年的數學地圖",
    "short": u"菲爾茲獎",
    "crumb": u"菲爾茲獎",
    "icon": u"📐",
    "description": u"比照諾貝爾獎系列的架構，從 1936 年第一屆讀到 2026 年費城大會：每位得主一課，共 68 位得主加懷爾斯特別獎，說明他們解決了什麼問題、之前難在哪裡、對今天的影響；"
                   u"附各時期總覽、領域與國籍統計、年齡分布，以及年齡限制、代表性、其他數學大獎的橫向分析。附得主時間軸、速查卡與滲流、質數間隔、掛谷針三個互動實驗。",
}

MODULES = fm_a.MODULES_A + fm_b.MODULES + fm_d.MODULES + fm_f.MODULES + fm_a.MODULES_IJ

REFERENCES = fm_ref.REFERENCES
