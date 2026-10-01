# -*- coding: utf-8 -*-
"""套裝應用程式的架構：參考頁。"""
from sa_common import LS, SALIB, widget
from ap_a import _STACK, EVQ

CHEATSHEET = {
    "file": "cheatsheet.html", "title": u"應用程式架構速查表", "h1": u"套裝應用程式的架構：速查表", "icon": u"🗂️",
    "description": u"分層、介面模式、常用設計模式、資料與交付的重點與術語，一頁查完",
    "body": [
        ("h", u"1. 分層"),
        ("fig", _STACK, "0 0 640 232", u"應用程式的分層架構。"),
        ("h", u"2. 介面架構模式"),
        ("t", [u"模式", u"重點", u"課"],
         [[u"事件迴圈", u"逐一處理事件；別卡住主執行緒", LS(5)], [u"MVC", u"模型、視圖、控制器分開", LS(7)],
          [u"MVVM", u"資料繫結，ViewModel 可測試", LS(8)], [u"單向資料流", u"動作 → 狀態 → 畫面", LS(9)]]),
        ("h", u"3. 常用設計模式"),
        ("t", [u"模式", u"用在", u"課"],
         [[u"命令（Command）", u"復原重做、巨集、協同編輯", LS(14)], [u"觀察者", u"模型變更通知視圖", LS(7)],
          [u"外掛／擴充點", u"讓第三方擴充功能", LS(20)], [u"登錄表（Registry）", u"指令、快捷鍵", LS(21)],
          [u"分層設定", u"預設 → 使用者 → 專案", LS(22)], [u"儲存庫（Repository）", u"把資料來源藏在介面後", LS(25)]]),
        ("h", u"4. 術語中英對照"),
        ("t", [u"中文", u"英文", u"課"],
         [[u"主執行緒", u"Main／UI Thread", LS(10)], [u"資料繫結", u"Data Binding", LS(8)], [u"文字緩衝區", u"Text Buffer（Gap Buffer、Piece Table、Rope）", LS(13)],
          [u"虛擬化清單", u"Virtualized List", LS(18)], [u"操作轉換", u"Operational Transformation (OT)", LS(19)],
          [u"無衝突複製資料型別", u"CRDT", LS(19)], [u"設計代幣", u"Design Token", LS(23)], [u"指數退避", u"Exponential Backoff", LS(27)],
          [u"冪等", u"Idempotent", LS(27)], [u"程式碼簽章", u"Code Signing", LS(29)], [u"遙測", u"Telemetry", LS(31)],
          [u"語言伺服器協定", u"Language Server Protocol (LSP)", LS(38)]]),
    ],
}

SIM = {
    "file": "playground.html", "title": u"應用程式架構互動實驗室", "h1": u"應用程式架構互動實驗室", "icon": u"🕹️",
    "description": u"事件迴圈、復原重做、Piece Table 三個互動實驗",
    "body": [
        ("raw", u"<script>%s</script>" % SALIB),
        ("h", u"1. 事件迴圈與主執行緒"), widget(EVQ),
        ("h", u"2. 復原／重做（命令模式）"), widget({"t": "undo"}),
        ("h", u"3. Piece Table 文字緩衝區"), widget({"t": "piece", "text": u"今天天氣很好"}),
    ],
}

REFERENCES = [CHEATSHEET, SIM]
