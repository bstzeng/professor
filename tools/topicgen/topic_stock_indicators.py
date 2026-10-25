# -*- coding: utf-8 -*-
"""股市常見指標與應用的規格。"""
import ti_a, ti_c, ti_f, ti_i, ti_k, ti_ref

TOPIC = {
    "id": "stock-indicators",
    "category": "invest",
    "title": u"股市常見指標與應用：技術、籌碼、基本面、總經與風險",
    "short": u"股市常見指標",
    "crumb": u"股市常見指標",
    "icon": u"📊",
    "description": u"台股與美股常見指標完整解析，每個指標都附公式與計算範例：均線、MACD、DMI、SAR、一目均衡表、RSI、KD、CCI、乖離率、布林通道、ATR、OBV、MFI、VWAP、"
                   u"成交量分布、K 線與價格型態、費波納契；騰落線、VIX、Put/Call、融資維持率；三大法人、期權未平倉、融資融券、集保大戶；EPS、月營收、ROE、本益比、殖利率、現金流、"
                   u"F-Score、Z-Score；景氣燈號、PMI、利率、殖利率曲線、CAPE；夏普值、最大回撤、回測與凱利公式。附模擬 K 線圖、回測器與多種計算機。投資教育，非投資建議。",
}

MODULES = ti_a.MODULES + ti_c.MODULES + ti_f.MODULES + ti_i.MODULES + ti_k.MODULES

REFERENCES = ti_ref.REFERENCES
