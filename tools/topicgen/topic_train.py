# -*- coding: utf-8 -*-
"""駕駛台灣的火車主題的規格。"""
import tr_a, tr_e, tr_ref

TOPIC = {
    "id": "train-driver",
    "category": "tech",
    "title": "駕駛台灣的火車：從出勤點呼到進站停車",
    "short": "駕駛台灣的火車",
    "crumb": "火車駕駛",
    "icon": "🚆",
    "description": "以臺鐵區間車為主線，認識台灣的鐵道系統、火車怎麼加速與煞車、駕駛台的設備、色燈號誌與 ATP，"
                   "再跟著司機員從出勤點呼、出庫檢查、指差確認、出發、運轉到進站停車；也談平交道、異常處置、重大事故的教訓，"
                   "並比較高鐵的車內號誌與捷運的自動駕駛。附駕駛模擬器、號誌測驗、煞車距離計算器、指差確認練習與運行圖。",
}

MODULES = tr_a.MODULES + tr_e.MODULES

REFERENCES = tr_ref.REFERENCES
