# -*- coding: utf-8 -*-
"""晶片 layout 設計主題的規格：把 cl_p1…cl_p6 的模組與兩個參考頁串起來。"""
import cl_p1, cl_p2, cl_p3, cl_p4, cl_p5, cl_p6, cl_ref

TOPIC = {
    "id": "chip-layout",
    "category": "tech",
    "title": "晶片是怎麼畫出來的：從電路到 Layout 的完整旅程",
    "short": "晶片 Layout 設計",
    "crumb": "晶片 Layout 設計",
    "icon": "🔲",
    "description": "從一顆電晶體的俯視圖畫起，經過標準元件、Verilog、邏輯合成、HLS 與 FPGA，"
                   "走完 floorplan、擺放、時脈樹、繞線與時序／DRC／LVS 簽核，"
                   "再到類比 layout、tape-out、光罩與測試，最後看 EDA、先進封裝、AI 與台灣產業鏈。",
}

MODULES = (cl_p1.MODULES + cl_p2.MODULES + cl_p3.MODULES
           + cl_p4.MODULES + cl_p5.MODULES + cl_p6.MODULES)

REFERENCES = cl_ref.REFERENCES
