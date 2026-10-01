# -*- coding: utf-8 -*-
"""遊戲的程式架構：參考頁。"""
from sa_common import LS, SALIB, widget
from ga_a import _LAYERS, FSM_PLAYER

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"遊戲架構速查表", "h1": u"遊戲的程式架構：速查表", "icon": u"🗂️",
    "description": u"引擎分層、常用設計模式、子系統與術語中英對照，一頁查完",
    "body": [
        ("h", u"1. 引擎分層"),
        ("fig", _LAYERS, "0 0 640 312", u"遊戲引擎的典型分層。"),
        ("h", u"2. 常用設計模式"),
        ("t", [u"模式", u"用途", u"課"],
         [[u"遊戲迴圈", u"輸入 → 更新 → 繪製", LS(5)], [u"固定時間步長＋累加器", u"穩定的物理", LS(6)],
          [u"元件（Component）", u"用組合代替繼承", LS(11)], [u"ECS", u"資料與邏輯分離、快取友善", LS(12)],
          [u"觀察者／事件", u"系統之間低耦合", LS(15)], [u"狀態機", u"角色、AI、遊戲流程", LS(16)],
          [u"行為樹", u"AI 決策", LS(25)], [u"命令（Command）", u"輸入、重播、連線同步", LS(36)],
          [u"物件池", u"避免頻繁配置記憶體", LS(7)], [u"控制代碼（Handle）", u"安全地參考資源", LS(27)]]),
        ("h", u"3. 術語中英對照"),
        ("t", [u"中文", u"英文", u"課"],
         [[u"畫格／每秒畫格數", u"Frame／FPS", LS(7)], [u"垂直同步", u"VSync", LS(7)], [u"繪製呼叫", u"Draw Call", LS(18)],
          [u"精靈／圖集", u"Sprite／Atlas", LS(19)], [u"細節層次", u"Level of Detail (LOD)", LS(20)], [u"包圍盒", u"AABB", LS(21)],
          [u"寬階段／窄階段", u"Broad／Narrow Phase", LS(22)], [u"骨架動畫", u"Skeletal Animation", LS(23)],
          [u"序列化", u"Serialization", LS(30)], [u"反射", u"Reflection", LS(32)], [u"客戶端預測", u"Client-side Prediction", LS(36)],
          [u"鎖步", u"Lockstep", LS(37)]]),
    ],
}

SIM = {
    "file": "playground.html", "title": u"遊戲架構互動實驗室", "h1": u"遊戲架構互動實驗室", "icon": u"🕹️",
    "description": u"時間步長、ECS、碰撞、狀態機、A* 尋路，五個互動實驗",
    "body": [
        ("raw", u"<script>%s</script>" % SALIB),
        ("h", u"1. 固定 vs 可變時間步長"), widget({"t": "loop"}),
        ("h", u"2. ECS 視覺化"), widget({"t": "ecs"}),
        ("h", u"3. 碰撞偵測"), widget({"t": "coll"}),
        ("h", u"4. 角色狀態機"), widget(FSM_PLAYER),
        ("h", u"5. A* 尋路"), widget({"t": "astar"}),
    ],
}

REFERENCES = [CHEATSHEET, SIM]
