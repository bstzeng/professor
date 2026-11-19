# -*- coding: utf-8 -*-
"""控制理論的規格。"""
import ctl_a, ctl_ref

TOPIC = {
    "id": "control-theory", "category": "tech",
    "title": u"控制理論：回授是怎麼讓世界穩定的",
    "short": u"控制理論", "crumb": u"控制理論", "icon": u"🎛️",
    "description": u"控制系統的元素、開迴路與閉迴路、正負回授、恆溫器與身體的恆定性、方塊圖與負回授放大器；一階與二階系統、階躍響應的指標、阻尼、延遲；比例、積分、微分控制、PID 調參與齊格勒—尼科爾斯法、積分飽和與 737 MAX 的教訓；"
                   u"不穩定、增益與相位、極點與根軌跡、調速器塔科馬吊橋與千禧橋；頻率響應、波德圖、相位與增益裕度；狀態空間與可控可觀性、前饋、LQR 與模型預測控制、數位控制；倒單擺平衡車與無人機、電網經濟與生態。附恆溫器、PID 調參、延遲、二階系統、倒單擺五個互動模擬。",
}
MODULES = ctl_a.MODULES
REFERENCES = ctl_ref.REFERENCES
