# -*- coding: utf-8 -*-
"""星艦迷航記全紀錄的規格。"""
import stk_a, stk_f, stk_ref

TOPIC = {
    "id": "star-trek",
    "category": "fantasy",
    "title": u"星艦迷航記全紀錄",
    "short": u"星艦迷航記",
    "crumb": u"星艦迷航記",
    "icon": u"🖖",
    "description": u"羅登貝瑞與「太空中的篷車隊」、星際聯邦與後稀缺社會；原初系列、可汗之怒、銀河飛龍、深太空九號、重返地球、企業號、凱爾文時間線、串流時代的奇異新世界與星艦學院；瓦肯、克林貢、羅慕倫、博格、卡達西與自治領、Q；"
                   u"曲速引擎與阿庫別瑞、傳送器與人格同一性、複製機與全像甲板、星艦設計；最高指導原則、烏乎拉與民權、DS9 的戰爭與道德、Data 與人工智慧；通訊器與手機、粉絲文化。附年表、艦橋人物、種族圖鑑、銀河地圖與曲速計算器。",
}

MODULES = stk_a.MODULES + stk_f.MODULES
REFERENCES = stk_ref.REFERENCES
