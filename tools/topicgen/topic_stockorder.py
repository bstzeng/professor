# -*- coding: utf-8 -*-
"""股票下單的幕後主題的規格。"""
import so_a, so_e, so_ref

TOPIC = {
    "id": "stock-order-flow",
    "category": "tech",
    "title": u"股票下單的幕後：一張委託單的千分之一秒旅程",
    "short": u"股票下單的幕後",
    "crumb": u"股票下單的幕後",
    "icon": u"📈",
    "description": u"按下「買進」之後發生了什麼？從手機、行動網路、券商前台與風控、專線，到證交所的委託簿與撮合引擎；"
                   u"價格時間優先、逐筆交易與集合競價、漲跌停與價格穩定措施、熔斷、市場監視與 T+2 交割；"
                   u"光速極限、共置機房、核心旁路、FPGA、時間同步、芝加哥到紐約的微波競賽與高頻交易；"
                   u"交易所與券商的機房規模（和 YouTube 比一比）、備援設計，以及閃電崩盤、騎士資本、胖手指與交易所當機等事故。附六個互動工具。",
}

MODULES = so_a.MODULES + so_e.MODULES

REFERENCES = so_ref.REFERENCES
