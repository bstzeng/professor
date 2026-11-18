# -*- coding: utf-8 -*-
"""刷卡與轉帳是怎麼運作的 的規格。"""
import pay_a, pay_b, pay_ref

TOPIC = {
    "id": "payment-systems", "category": "finance",
    "title": u"刷卡與轉帳是怎麼運作的：信用卡、ATM、轉帳與行動支付的底層",
    "short": u"刷卡與轉帳", "crumb": u"支付系統", "icon": u"💳",
    "description": u"錢是帳本上的紀錄；授權、清算、結算與風險；央行同資系統、財金公司與卡組織；信用卡的四方模型、卡號與 Luhn 檢查碼、晶片與感應、授權流程、清算與結算、交換費與刷卡回饋、3D 驗證、代碼化與手機錢包、預授權、盜刷與退單、循環信用；"
                   u"ATM 跨行提款、即時跨行轉帳、約定帳戶與限額、SWIFT 與國際匯款、支票與票據交換；悠遊卡離線扣款、電子支付儲值與信託、TWQR、網路金流；側錄與釣魚、ATM 解除分期詐騙、警示帳戶與人頭帳戶；Pix 與 UPI、央行數位貨幣、穩定幣。附六種流程的逐步動畫、卡號檢查碼與手續費拆分。",
}
MODULES = pay_a.MODULES + pay_b.MODULES
REFERENCES = pay_ref.REFERENCES
