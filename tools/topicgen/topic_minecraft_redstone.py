# -*- coding: utf-8 -*-
"""Minecraft 紅石電路主題的規格。"""
import mcr_a, mcr_f, mcr_ref

TOPIC = {
    "id": "minecraft-redstone",
    "category": "tech",
    "title": u"Minecraft 紅石電路：用遊戲學計算機",
    "short": u"紅石電路",
    "crumb": u"紅石電路",
    "icon": u"🟥",
    "description": u"Minecraft 與紅石、訊號強度、紅石火把反相器、中繼器與比較器、活塞觀察者與遊戲刻；布林與夏農、基本邏輯閘與笛摩根、NAND 萬用閘、XOR、卡諾圖；"
                   u"二進位與二補數、半加器全加器、漣波進位加法器、解碼器與七段顯示器、多工器、ALU；回饋與記憶、RS 閂鎖、D 與 T 正反器、時脈、計數器、記憶體；"
                   u"馮紐曼架構、指令集、控制單元、執行程式、玩家的紅石電腦、速度與限制；從紅石到晶片、圖靈完備。附五個互動模擬，含一台可單步執行的迷你 CPU。",
}

MODULES = mcr_a.MODULES + mcr_f.MODULES
REFERENCES = mcr_ref.REFERENCES
