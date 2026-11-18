# -*- coding: utf-8 -*-
"""手機是怎麼連上網的：參考頁。"""
from nv_common import LS, NVLIB
import mob_common as C

TERMS = {"file": "terms.html", "title": u"行動通訊名詞", "h1": u"行動通訊名詞對照", "icon": u"📚", "description": u"本課程常見的名詞",
  "body": [("t", [u"中文", u"英文", u"說明", u"課"], [
    [u"細胞", u"Cell", u"一個基地台（扇區）涵蓋的範圍", LS(2)], [u"回傳", u"Backhaul", u"基地台連回核心網路的線路", LS(3)], [u"正交分頻多工", u"OFDM", u"把頻寬切成許多子載波", LS(4)],
    [u"國際行動用戶識別碼", u"IMSI", u"SIM 卡中的用戶身分", LS(5)], [u"嵌入式 SIM", u"eSIM", u"可下載設定檔的內建 SIM", LS(7)], [u"隨機接取", u"Random access", u"手機向基地台打招呼的程序", LS(9)],
    [u"追蹤區域", u"Tracking area", u"網路記錄閒置手機位置的單位", LS(10)], [u"呼叫", u"Paging", u"網路尋找閒置手機的廣播", LS(11)], [u"換手", u"Handover", u"從一個基地台切換到另一個", LS(12)],
    [u"服務化架構", u"SBA", u"5G 核心網路的軟體化架構", LS(13)], [u"IP 多媒體子系統", u"IMS", u"VoLTE 的核心", LS(17)], [u"細胞廣播", u"Cell broadcast", u"向區域內所有手機廣播的技術", LS(18)],
    [u"網路切片", u"Network slicing", u"在同一網路上建立多個虛擬網路", LS(21)], [u"開放式無線接取網路", u"Open RAN", u"以開放介面組成的基地台", LS(22)], [u"SIM 卡挾持", u"SIM swap", u"冒充用戶補發 SIM 卡", LS(27)]])]}
FLOWS = {"file": "flows.html", "title": u"流程總覽", "h1": u"五種行動網路流程", "icon": u"🔁", "description": u"開機註冊、呼叫、換手、簡訊與漫遊",
  "body": [("raw", u"<script>%s</script>" % NVLIB), C.SEQ_ALL]}
GUIDE = {"file": "guide.html", "title": u"互動圖鑑", "h1": u"行動網路互動圖鑑", "icon": u"🗺️", "description": u"年表與換手模擬",
  "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 行動通訊的世代（第 1 課）"), C.HISTORY, ("h", u"2. 換手模擬（第 12 課）"), C.HO]}
REFERENCES = [TERMS, FLOWS, GUIDE]
