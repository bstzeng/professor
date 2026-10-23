# -*- coding: utf-8 -*-
"""現代核電廠設計主題的規格。"""
import npp_a, npp_c, npp_e, npp_g, npp_ref

TOPIC = {
    "id": "nuclear-plant-design",
    "category": "tech",
    "title": u"現代核電廠設計：從核分裂到被動安全",
    "short": u"核電廠設計",
    "crumb": u"核電廠設計",
    "icon": u"⚛️",
    "description": u"完整推導的核電廠設計課：反應爐物理（臨界、緩和、反應度、回饋、氙毒、衰變熱）；燃料與爐心（熱限值、DNB、鋯水反應、燃耗）；"
                   u"熱流與一次系統（壓力槽、蒸汽產生器、自然循環、朗肯循環）；縱深防禦、單一失效、PRA；LOCA、全廠斷電、AP1000 被動安全、嚴重事故對策、"
                   u"三哩島車諾比福島；儀控、電力、熱沉、選址、耐震、外部危害；SMR、高溫氣冷、鈉冷、熔鹽與核融合；執照、建造、LCOE、除役與核廢料。附 12 個互動模擬。",
}

MODULES = npp_a.MODULES + npp_c.MODULES + npp_e.MODULES + npp_g.MODULES

REFERENCES = npp_ref.REFERENCES
