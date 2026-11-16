# -*- coding: utf-8 -*-
"""系外行星主題的規格。"""
import exo_a, exo_f, exo_ref

TOPIC = {
    "id": "exoplanets",
    "category": "science",
    "title": u"系外行星：怎麼找到另一個地球",
    "short": u"系外行星",
    "crumb": u"系外行星",
    "icon": u"🪐",
    "description": u"從布魯諾到 1995；徑向速度法、高精度光譜儀、飛馬座 51 b 與熱木星、m sin i、恆星雜訊；凌日法、克卜勒、TESS、假陽性、凌日時間變分；"
                   u"脈衝星行星、重力微透鏡、直接成像、蓋亞天體測量；行星遷移、超級地球與半徑谷、TRAPPIST-1、比鄰星 b、η⊕；"
                   u"穿透光譜、韋伯與 WASP-39b、K2-18b 爭議、相位曲線；可居住帶、紅矮星、生物跡象；BLS、MCMC、機器學習、公民科學；PLATO、羅曼、宜居世界天文台、費米悖論。附四個互動模擬。",
}

MODULES = exo_a.MODULES + exo_f.MODULES
REFERENCES = exo_ref.REFERENCES
