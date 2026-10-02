# -*- coding: utf-8 -*-
"""蒙地卡羅方法主題的規格。"""
import mc_a, mc_e, mc_ref

TOPIC = {
    "id": "monte-carlo",
    "category": "math",
    "title": "蒙地卡羅方法：用隨機算出確定的答案",
    "short": "蒙地卡羅方法",
    "crumb": "蒙地卡羅",
    "icon": "🎯",
    "description": "蒲豐投針與丟點估 π、大數法則與中央極限定理；偽隨機數、RANDU、梅森旋轉、反函數法、接受—拒絕；蒙地卡羅積分、1/√N、維度詛咒、"
                   "重要性抽樣、變異數縮減、準蒙地卡羅；梅特羅波利斯、吉布斯、HMC、貝氏推論；模擬退火、MCTS 與 AlphaGo、SGD；"
                   "粒子輸運、路徑追蹤、量子蒙地卡羅、系集預報；選擇權定價、VaR、退休規劃。附十個互動模擬。",
}

MODULES = mc_a.MODULES + mc_e.MODULES

REFERENCES = mc_ref.REFERENCES
