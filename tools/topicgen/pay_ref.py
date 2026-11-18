# -*- coding: utf-8 -*-
"""刷卡與轉帳：參考頁。"""
from nv_common import LS, NVLIB
import pay_common as C

TERMS = {"file": "terms.html", "title": u"支付名詞", "h1": u"支付名詞對照", "icon": u"📚", "description": u"本課程常見的支付名詞",
  "body": [("t", [u"中文", u"英文", u"說明", u"課"], [
    [u"授權", u"Authorization", u"發卡行核准並保留額度", LS(7)], [u"清算", u"Clearing", u"計算誰欠誰多少", LS(8)], [u"結算", u"Settlement", u"資金真正移動", LS(8)],
    [u"即時總額結算", u"RTGS", u"每筆即時全額結清", LS(2)], [u"發卡行", u"Issuer", u"發卡給持卡人的銀行", LS(4)], [u"收單行", u"Acquirer", u"與商店簽約的銀行或機構", LS(4)],
    [u"發卡機構識別碼", u"BIN / IIN", u"卡號前 6～8 位", LS(5)], [u"交換費", u"Interchange fee", u"收單端付給發卡行的費用", LS(9)], [u"3D 驗證", u"3-D Secure", u"網路刷卡的身分驗證", LS(10)],
    [u"代碼化", u"Tokenization", u"以代碼取代真實卡號", LS(11)], [u"預授權", u"Pre-authorization", u"先保留金額，後依實際金額請款", LS(12)], [u"爭議款（退單）", u"Chargeback", u"持卡人透過發卡行提出爭議", LS(13)],
    [u"往來帳戶", u"Nostro / Vostro", u"銀行在他行開設的帳戶", LS(18)], [u"電子票證", u"Stored-value card", u"餘額記在卡片中的儲值卡", LS(20)], [u"警示帳戶", u"—", u"涉及詐騙而被暫停的帳戶", LS(26)],
    [u"央行數位貨幣", u"CBDC", u"央行發行的數位貨幣", LS(28)], [u"穩定幣", u"Stablecoin", u"與法幣掛鉤的代幣", LS(29)]])]}
FLOWS = {"file": "flows.html", "title": u"流程總覽", "h1": u"六種支付流程", "icon": u"🔁", "description": u"刷卡、清算、網路刷卡、ATM、轉帳與國際匯款的逐步流程",
  "body": [("raw", u"<script>%s</script>" % NVLIB), C.SEQ_ALL]}
GUIDE = {"file": "guide.html", "title": u"互動圖鑑", "h1": u"支付互動圖鑑", "icon": u"🗺️", "description": u"年表、卡號檢查碼與手續費拆分",
  "body": [("raw", u"<script>%s</script>" % NVLIB), ("h", u"1. 支付的演進（第 1 課）"), C.HISTORY, ("h", u"2. 卡號檢查碼（第 5 課）"), C.LUHN, ("h", u"3. 手續費拆分（第 9 課）"), C.FEE]}
REFERENCES = [TERMS, FLOWS, GUIDE]
