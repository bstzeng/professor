# -*- coding: utf-8 -*-
"""從材料力學到建築承重主題的規格。"""
import sm_a, sm_c, sm_e, sm_g, sm_ref

TOPIC = {
    "id": "materials-to-structures",
    "category": "tech",
    "title": u"從材料力學到建築承重：接得起來嗎？",
    "short": u"材料力學到建築承重",
    "crumb": u"材料到建築承重",
    "icon": u"🏗️",
    "description": u"從原子鍵的位能曲線估出彈性模數，看理論強度為什麼比真實強度高一百倍（Griffith 裂紋、差排）；"
                   u"再走過應力應變、莫爾圓、降伏準則、彎曲 σ = My/I、剪應力、撓度、靜不定、歐拉挫屈與規範柱曲線；"
                   u"接著是桁架、剛架、勁度矩陣、有限元素、基礎與雙向板；載重從靜載重、活載重、風、地震到載重組合與可靠度；"
                   u"最後完整手算一棟虛構四層 RC 透天，並談平方立方定律、摩天大樓、吊橋與 921 等案例。附 13 種計算工具。",
}

MODULES = sm_a.MODULES + sm_c.MODULES + sm_e.MODULES + sm_g.MODULES

REFERENCES = sm_ref.REFERENCES
