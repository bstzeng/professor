# -*- coding: utf-8 -*-
"""核融合主題的規格。"""
import fus_a, fus_f, fus_ref

TOPIC = {
    "id": "nuclear-fusion",
    "category": "science",
    "title": u"核融合：從太陽到 ITER 與 NIF",
    "short": u"核融合",
    "crumb": u"核融合",
    "icon": u"☀️",
    "description": u"結合能、庫侖障壁與量子穿隧、伽莫夫峰、D-T 與無中子融合；質子—質子鏈、CNO 循環、太陽的自我調節；勞森判據推導、軔致輻射與反常輸運、Q 值；"
                   u"磁場中的帶電粒子、仿星器與 ZETA、托卡馬克與 T-3、TFTR 與 JET、不穩定性與破裂、ITER、W7-X；雷射內爆、NIF 與黑腔、2022 年點火、8.6 MJ 紀錄；"
                   u"中子與材料、氚增殖、偏濾器、高溫超導磁鐵；民間融合公司、EAST 與 KSTAR、永遠的三十年、冷融合；氫彈、μ 子催化、融合電廠。附三個互動模擬。",
}

MODULES = fus_a.MODULES + fus_f.MODULES
REFERENCES = fus_ref.REFERENCES
