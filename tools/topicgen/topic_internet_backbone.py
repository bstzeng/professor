# -*- coding: utf-8 -*-
"""網際網路的骨幹 的規格。"""
import ibb_a, ibb_b, ibb_ref

TOPIC = {
    "id": "internet-backbone", "category": "tech",
    "title": u"網際網路的骨幹：DNS、BGP、海底電纜與大斷線",
    "short": u"網際網路骨幹", "crumb": u"網際網路骨幹", "icon": u"🌐",
    "description": u"自治系統、付費轉送與對等互連、網路交換中心、IP 位址的分配；DNS 的階層、根伺服器與任播、一次查詢的旅程、TTL 與快取、快取下毒與 DNSSEC、Dyn 與 AWS 的 DNS 事故；BGP 的宣告與 AS 路徑、路徑選擇與商業政策、巴基斯坦與 YouTube 的劫持、2019 年路由洩漏、Facebook 斷線六小時、RPKI；"
                   u"海底電纜的構造、鋪設與維修、波長多工與光速極限、恆春地震斷纜、東加與紅海、馬祖斷纜與 2025 年宏泰 58 案；CDN 與任播、資料中心、Fastly 與 AWS 大斷線、IPv4 耗盡與 IPv6；ICANN 與網路治理、國家斷網、低軌衛星。附 DNS 查詢動畫、BGP 劫持模擬與延遲計算。",
}
MODULES = ibb_a.MODULES + ibb_b.MODULES
REFERENCES = ibb_ref.REFERENCES
