# -*- coding: utf-8 -*-
"""電話系統全解析的規格。"""
import phn_a, phn_b, phn_c, phn_ref

TOPIC = {
    "id": "telephone-systems",
    "category": "tech",
    "title": u"電話系統全解析：交換機、總機、語音選單與轉接的底層原理",
    "short": u"電話系統",
    "crumb": u"電話系統",
    "icon": u"☎️",
    "description": u"信令、交換與媒體；接線生與自動交換、64 kbps 與取樣、E1 與時槽、DTMF 與 7 號信令；企業總機、號碼規劃與 0800、語音選單設計、話務中心與 Erlang C、語音信箱與會議；網路電話、RTP、SIP、SDP、NAT 穿越、B2BUA 與 SBC、通話品質；"
                   u"轉接的原理——通話段與橋接、為什麼轉接時電話不會斷、保留的 re-INVITE、拍叉簧與時槽、REFER 與 Replaces、總機改接、轉接失敗；0204 付費語音資訊服務的商業模式、計費、管制與 2023 年終止；客服系統設計、高可用、雲端與 WebRTC、VoLTE 與 IMS、盜打與來電顯示偽造、錄音與緊急電話。",
}

MODULES = phn_a.MODULES + phn_b.MODULES + phn_c.MODULES
REFERENCES = phn_ref.REFERENCES
