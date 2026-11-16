# -*- coding: utf-8 -*-
"""資訊理論主題的規格。"""
import inf_a, inf_f, inf_ref

TOPIC = {
    "id": "information-theory",
    "category": "math",
    "title": u"資訊理論：從夏農的熵到壓縮、通訊與 LLM",
    "short": u"資訊理論",
    "crumb": u"資訊理論",
    "icon": u"📡",
    "description": u"夏農 1948、資訊量與熵的推導、英文與中文的熵；信源編碼定理、霍夫曼、算術編碼、LZ77 與 ZIP、鴿籠原理、率—失真；"
                   u"互資訊、通道容量、夏農—哈特利；漢明碼、里德—所羅門、渦輪碼與 LDPC、極化碼與 5G；交叉熵、KL 散度、最大熵；"
                   u"交叉熵損失、語言模型即壓縮器、困惑度、資訊增益、VAE；馬克士威惡魔、蘭道爾原理、黑洞資訊悖論、量子資訊；一次性密碼本、密碼強度、柯氏複雜度。附四個互動模擬。",
}

MODULES = inf_a.MODULES + inf_f.MODULES
REFERENCES = inf_ref.REFERENCES
