# -*- coding: utf-8 -*-
"""遊戲的程式架構主題的規格。"""
import ga_a, ga_e, ga_ref

TOPIC = {
    "id": "game-architecture",
    "category": "tech",
    "title": "遊戲的程式架構：從遊戲迴圈到引擎設計",
    "short": "遊戲的程式架構",
    "crumb": "遊戲架構",
    "icon": "🎮",
    "description": "遊戲是每秒跑 60 次的即時模擬。從引擎分層、遊戲迴圈與固定時間步長，到元件式設計、ECS、資料導向、事件與狀態機；"
                   "再看輸入、繪圖、物理、動畫、音效、AI、UI、資源、腳本等子系統，資料驅動、存檔與工具鏈，連線遊戲的預測與同步，"
                   "最後拆解 Unity、Unreal、Godot 的架構。附時間步長、ECS、碰撞、狀態機、A* 尋路等互動實驗。",
}

MODULES = ga_a.MODULES + ga_e.MODULES

REFERENCES = ga_ref.REFERENCES
