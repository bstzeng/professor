# -*- coding: utf-8 -*-
"""套裝應用程式的架構主題的規格。"""
import ap_a, ap_d, ap_ref

TOPIC = {
    "id": "app-architecture",
    "category": "tech",
    "title": "套裝應用程式的架構：從事件迴圈到自動更新",
    "short": "套裝應用程式的架構",
    "crumb": "應用程式架構",
    "icon": "🧰",
    "description": "Word、Photoshop、VS Code、聊天軟體這類桌面應用程式是怎麼組織的？從分層架構、事件迴圈、MVC／MVVM／單向資料流、"
                   "主執行緒與非同步，到文件模型、文字緩衝區、復原重做、檔案格式、自動儲存、協同編輯；再看外掛、指令、設定、主題、"
                   "本機資料庫、離線同步、網路、授權、安全與隱私，以及測試、封裝、自動更新、當機回報與效能。附事件迴圈、復原重做、Piece Table 互動實驗。",
}

MODULES = ap_a.MODULES + ap_d.MODULES

REFERENCES = ap_ref.REFERENCES
