# -*- coding: utf-8 -*-
"""機場是怎麼運作的：參考頁。"""
from nv_common import LS, NVLIB
import apt_a as C

TERMS = {"file": "terms.html", "title": u"機場名詞", "h1": u"機場名詞對照", "icon": u"📚", "description": u"本課程常見的機場名詞",
  "body": [("t", [u"中文", u"英文", u"說明", u"課"], [
    [u"空側／陸側", u"Airside / Landside", u"安檢線內外的區域", LS(2)], [u"跑道安全區", u"RESA", u"跑道兩端的緩衝區", LS(3)], [u"行李處理系統", u"BHS", u"輸送、檢查與分揀行李", LS(5)],
    [u"自動查驗通關", u"e-Gate", u"以生物辨識自助通關", LS(7)], [u"遠端機位", u"Remote stand", u"不靠空橋的停機位", LS(8)], [u"最短轉機時間", u"MCT", u"轉機所需的最短時間", LS(9)],
    [u"過站作業", u"Turnaround", u"飛機在地面的各項作業", LS(11)], [u"要徑", u"Critical path", u"決定完成時間的最長作業鏈", LS(11)], [u"時刻帶", u"Slot", u"在特定時段使用機場的許可", LS(16)],
    [u"流量管理", u"ATFM", u"以地面等待等方式調節流量", LS(17)], [u"儀器降落系統", u"ILS", u"以無線電引導飛機進場", LS(18)], [u"停止排燈", u"Stop bar", u"進入跑道前的紅燈", LS(15)]])]}
GUIDE = {"file": "guide.html", "title": u"互動圖鑑", "h1": u"機場互動圖鑑", "icon": u"🗺️", "description": u"過站甘特圖、跑道容量、行李流程與世界機場",
  "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 過站作業（第 11 課）"), C.GANTT, ("h", u"2. 跑道容量（第 3 課）"), C.RWY,
           ("h", u"3. 託運行李的旅程（第 5 課）"), C.SEQ_BAG, ("h", u"4. 世界著名機場"), C.AIRPORTS]}
REFERENCES = [TERMS, GUIDE]
