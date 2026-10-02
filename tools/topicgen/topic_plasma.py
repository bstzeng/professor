# -*- coding: utf-8 -*-
"""電漿物理主題的規格。"""
import pz_a, pz_e, pz_ref

TOPIC = {
    "id": "plasma-physics",
    "category": "science",
    "title": "電漿（等離子體）物理：物質的第四態",
    "short": "電漿物理",
    "crumb": "電漿物理",
    "icon": "⚡",
    "description": "物質的第四態：電離、德拜屏蔽、電漿頻率；迴旋、漂移、磁鏡、輻射帶與極光；磁流體力學、凍結定理、阿爾芬波、磁重聯、發電機；"
                   "朗道阻尼與不穩定性；日冕、太陽風、太空天氣、黑洞吸積盤；核融合：勞森判據、托卡馬克、仿星器、NIF 點火、ITER 與民營公司；"
                   "半導體蝕刻、照明、冷電漿醫療與電漿推進。附六個互動模擬。",
}

MODULES = pz_a.MODULES + pz_e.MODULES

REFERENCES = pz_ref.REFERENCES
