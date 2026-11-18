# -*- coding: utf-8 -*-
"""網際網路的骨幹：參考頁。"""
from nv_common import LS, NVLIB
import ibb_common as C

TERMS = {"file": "terms.html", "title": u"網路名詞", "h1": u"網際網路骨幹名詞對照", "icon": u"📚", "description": u"本課程常見的名詞",
  "body": [("t", [u"中文", u"英文", u"說明", u"課"], [
    [u"自治系統", u"AS", u"單一組織管理、有一致路由政策的網路", LS(1)], [u"付費轉送", u"Transit", u"向上游購買通往全世界的連線", LS(2)], [u"對等互連", u"Peering", u"互惠交換彼此客戶的流量", LS(2)],
    [u"網路交換中心", u"IXP", u"多家業者互連的中立地點", LS(3)], [u"區域網際網路註冊機構", u"RIR", u"各大洲的位址分配機構", LS(4)], [u"遞迴解析器", u"Recursive resolver", u"替你查詢 DNS 的伺服器", LS(8)],
    [u"權威伺服器", u"Authoritative server", u"回答自己負責網域的伺服器", LS(8)], [u"存活時間", u"TTL", u"答案可以快取多久", LS(9)], [u"DNS 安全擴充", u"DNSSEC", u"以數位簽章驗證 DNS 紀錄", LS(10)],
    [u"邊界閘道協定", u"BGP", u"AS 之間交換路由的協定", LS(12)], [u"最長前綴優先", u"Longest prefix match", u"更細的網段優先", LS(13)], [u"路由劫持", u"Route hijack", u"宣告不屬於自己的網段", LS(14)],
    [u"路由洩漏", u"Route leak", u"把路由傳給不該傳的對象", LS(15)], [u"資源公鑰基礎設施", u"RPKI", u"驗證路由來源的機制", LS(17)], [u"密集波長多工", u"DWDM", u"一根光纖傳送多個波長", LS(20)],
    [u"內容傳遞網路", u"CDN", u"把內容快取在用戶附近", LS(24)], [u"任播", u"Anycast", u"多地宣告同一個 IP", LS(24)], [u"網路位址轉換", u"NAT", u"多個裝置共用公開 IP", LS(27)]])]}
GUIDE = {"file": "guide.html", "title": u"互動圖鑑", "h1": u"網際網路骨幹互動圖鑑", "icon": u"🗺️", "description": u"年表、事件圖鑑、DNS 查詢、BGP 模擬與延遲計算",
  "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 歷史（第 1 課）"), C.HISTORY, ("h", u"2. 重大事件"), C.OUTAGES, ("h", u"3. DNS 查詢（第 8 課）"), C.SEQ_DNS,
           ("h", u"4. BGP 路由模擬（第 13 課）"), C.BGP, ("h", u"5. 距離與延遲（第 20 課）"), C.LAT]}
REFERENCES = [TERMS, GUIDE]
