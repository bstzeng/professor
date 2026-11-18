# -*- coding: utf-8 -*-
"""電話系統全解析：參考頁——名詞對照、SIP 速查、互動圖鑑。"""
from nv_common import LS, NVLIB
import phn_common as C

TERMS = {
    "file": "terms.html", "title": u"名詞對照", "h1": u"電話系統名詞對照", "icon": u"📚",
    "description": u"本課程常見的電話與網路電話名詞",
    "body": [
        ("t", [u"中文", u"英文", u"說明", u"課"], [
            [u"信令", u"Signaling", u"建立、維持、拆除通話的控制訊息", LS(5)], [u"雙音多頻", u"DTMF", u"按鍵音，每鍵兩個頻率", LS(5)],
            [u"7 號信令", u"SS7", u"電信業者之間獨立的信令網路", LS(5)], [u"分時多工", u"TDM", u"把時間切成時槽，多通電話共用一條線", LS(4)],
            [u"企業總機", u"PBX", u"公司內部的交換機", LS(6)], [u"外線直撥分機", u"DID", u"外面直接撥到分機", LS(7)],
            [u"互動式語音應答", u"IVR", u"語音選單", LS(8)], [u"自動話務分配", u"ACD", u"排隊與分派來電", LS(9)],
            [u"厄朗", u"Erlang", u"話務量的單位", LS(9)], [u"即時傳輸協定", u"RTP", u"傳送語音封包", LS(11)],
            [u"工作階段初始協定", u"SIP", u"網路電話的信令協定", LS(12)], [u"工作階段描述協定", u"SDP", u"描述媒體的位址與編碼", LS(13)],
            [u"網路位址轉換", u"NAT", u"私有位址共用公開位址", LS(14)], [u"背對背使用者代理", u"B2BUA", u"在中間接起兩段通話的伺服器", LS(15)],
            [u"邊界控制器", u"SBC", u"網路邊界的安全與互通設備", LS(15)], [u"平均意見分數", u"MOS", u"通話品質評分（1～5）", LS(16)],
            [u"通話段", u"Call leg", u"一通電話中，端點與交換機之間的一段", LS(18)], [u"橋接", u"Bridge", u"把兩段通話接在一起", LS(18)],
            [u"轉介", u"REFER", u"SIP 中請對方撥給第三人的請求", LS(21)], [u"取代", u"Replaces", u"讓新通話取代既有的通話", LS(21)],
            [u"通話明細紀錄", u"CDR", u"每通電話的計費紀錄", LS(25)], [u"IP 多媒體子系統", u"IMS", u"VoLTE 的核心，電信業者的 SIP 系統", LS(31)],
            [u"國際收益分成詐騙", u"IRSF", u"盜打高費率國際號碼分錢", LS(32)],
        ]),
    ],
}

SIPREF = {
    "file": "sip.html", "title": u"SIP 速查", "h1": u"SIP 訊息與轉接速查", "icon": u"📞",
    "description": u"SIP 請求、回應碼與保留／轉接的訊息流程",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"五種情境的訊息流程"), C.SIP(u"選擇情境，按「下一步」：", [C.SC_BASIC, C.SC_HOLD, C.SC_BLIND, C.SC_ATT, C.SC_B2B]),
        ("h", u"保留與轉接的要點"),
        ("t", [u"功能", u"SIP 做法", u"課"], [
            [u"保留", u"re-INVITE，SDP 改為 a=sendonly／inactive", LS(19)], [u"恢復", u"re-INVITE，SDP 改回 a=sendrecv", LS(19)],
            [u"直接轉接", u"REFER（Refer-To）→ 被轉者 INVITE 第三人 → NOTIFY 回報 → BYE", LS(21)],
            [u"先問再轉", u"REFER 附 Replaces → 被轉者 INVITE（Replaces）→ 舊通話被取代", LS(21)],
            [u"總機改接", u"B2BUA 另建一段並橋接；必要時以 re-INVITE 更新媒體位址", LS(22)],
        ]),
    ],
}

GUIDE = {
    "file": "guide.html", "title": u"互動圖鑑", "h1": u"電話系統互動圖鑑", "icon": u"🗺️",
    "description": u"年表、取樣、按鍵音、通話段、語音選單、人力計算與 0204 計費",
    "body": [
        ("raw", u"<script>%s</script>" % NVLIB),
        ("h", u"1. 電話系統的歷史（第 1 課）"), C.HISTORY,
        ("h", u"2. 取樣與量化（第 3 課）"), C.PCM,
        ("h", u"3. 按鍵音（第 5 課）"), C.DTMF,
        ("h", u"4. 兩段通話與轉接（第 18 課）"), C.LEGS,
        ("h", u"5. 語音選單模擬器（第 8 課）"), C.IVR,
        ("h", u"6. 話務中心人力計算（第 9 課）"), C.ERL,
        ("h", u"7. 0204 計費示意（第 25 課）"), C.PREM,
    ],
}

REFERENCES = [TERMS, SIPREF, GUIDE]
