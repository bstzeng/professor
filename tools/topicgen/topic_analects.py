# -*- coding: utf-8 -*-
"""論語主題的規格。"""
import ly_a, ly_d, ly_g, ly_more

TOPIC = {
    "id": "analects",
    "category": "classics",
    "title": u"論語：孔子與弟子的對話",
    "short": u"論語",
    "crumb": u"論語",
    "icon": u"📜",
    "description": u"依主題重新編排《論語》：學習、仁、君子與小人、孝悌、交友待人、政治與禮，以及孔子這個人——他的自述、幽默、日常、音樂、挫折與顏淵之死。"
                   u"每課附原文、白話、字詞與不同的解讀，收錄兩百五十多則章句；並談論語在台灣、被誤讀的名句與論語成語。附原文白話切換、二十篇索引、一章多解、名句搜尋與成語測驗。",
}

MODULES = ly_a.MODULES + ly_d.MODULES + ly_g.MODULES
ly_more.attach(MODULES)

import ly_ref  # noqa: E402  必須在延伸章句登記之後才建立搜尋頁
REFERENCES = ly_ref.REFERENCES
