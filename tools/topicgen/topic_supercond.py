# -*- coding: utf-8 -*-
"""超導機制主題的規格。"""
import sp_a, sp_e, sp_ref

TOPIC = {
    "id": "superconductivity",
    "category": "science",
    "title": "超導機制：電阻消失之謎",
    "short": "超導機制",
    "crumb": "超導機制",
    "icon": "🧲",
    "description": "1911 年電阻消失、邁斯納效應與三道臨界邊界；倫敦方程式、金茲堡—朗道理論、第一類與第二類超導、磁通渦旋；"
                   "同位素效應、電子—聲子吸引、庫柏對、BCS 理論與能隙；磁通量子化、約瑟夫森效應、SQUID、2025 年諾貝爾獎的巨觀量子穿隧與量子位元；"
                   "銅氧化物、鐵基、鎳基與高壓氫化物，室溫超導的爭議；MRI、LHC、磁浮、核融合與電力應用。附八個互動實驗。",
}

MODULES = sp_a.MODULES + sp_e.MODULES

REFERENCES = sp_ref.REFERENCES
