# -*- coding: utf-8 -*-
"""選擇權與 Black–Scholes：參考頁——公式表與名詞表。"""
from opt_common import LS, M

FORMULAS = {
    "file": "formulas.html", "title": u"公式表", "h1": u"選擇權定價公式表", "icon": u"🧮",
    "description": u"本課程用到的主要公式",
    "body": [
        ("t", [u"名稱", u"公式", u"課"], [
            [u"到期價值", M(r"C_T=\max(S_T-K,0),\ P_T=\max(K-S_T,0)"), LS(2)],
            [u"買賣權平價", M(r"C+Ke^{-rT}=P+S"), LS(5)],
            [u"風險中性機率", M(r"q=\frac{e^{r\Delta t}-d}{u-d}"), LS(8)],
            [u"二項樹倒推", M(r"V=e^{-r\Delta t}[qV_u+(1-q)V_d]"), LS(9)],
            [u"CRR 參數", M(r"u=e^{\sigma\sqrt{\Delta t}},\ d=1/u"), LS(9)],
            [u"幾何布朗運動", M(r"dS=\mu S\,dt+\sigma S\,dW"), LS(15)],
            [u"GBM 的解", M(r"S_t=S_0e^{(\mu-\sigma^2/2)t+\sigma W_t}"), LS(15)],
            [u"伊藤引理", M(r"df=(f_t+af_x+\tfrac12b^2f_{xx})dt+bf_x\,dW"), LS(17)],
            [u"Black–Scholes 方程式", M(r"V_t+\tfrac12\sigma^2S^2V_{SS}+rSV_S-rV=0"), LS(20)],
            [u"買權公式", M(r"C=SN(d_1)-Ke^{-rT}N(d_2)"), LS(21)],
            [u"賣權公式", M(r"P=Ke^{-rT}N(-d_2)-SN(-d_1)"), LS(21)],
            [u"d₁、d₂", M(r"d_{1,2}=\frac{\ln(S/K)+(r\pm\sigma^2/2)T}{\sigma\sqrt T}"), LS(21)],
            [u"Delta（買權）", M(r"N(d_1)"), LS(26)],
            [u"Gamma", M(r"\frac{N'(d_1)}{S\sigma\sqrt T}"), LS(26)],
            [u"Vega", M(r"SN'(d_1)\sqrt T"), LS(27)],
            [u"Theta 與 Gamma", M(r"\Theta\approx-\tfrac12\sigma^2S^2\Gamma"), LS(27)],
        ]),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"名詞表", "h1": u"選擇權名詞表", "icon": u"📖",
    "description": u"中英對照的選擇權名詞",
    "body": [
        ("t", [u"中文", u"英文", u"說明", u"課"], [
            [u"買權、賣權", u"call, put", u"買進、賣出的權利", LS(2)],
            [u"履約價", u"strike", u"約定的買賣價格", LS(2)],
            [u"權利金", u"premium", u"選擇權的價格", LS(2)],
            [u"歐式、美式", u"European, American", u"只能到期履約／隨時可履約", LS(2)],
            [u"價內、價平、價外", u"ITM, ATM, OTM", u"立刻履約是否有價值", LS(2)],
            [u"跨式、勒式", u"straddle, strangle", u"同時買賣權的策略", LS(4)],
            [u"套利", u"arbitrage", u"無風險的獲利", LS(5)],
            [u"風險中性", u"risk-neutral", u"預期報酬等於無風險利率的計算世界", LS(8)],
            [u"布朗運動", u"Brownian motion", u"連續的隨機漫步", LS(14)],
            [u"幾何布朗運動", u"GBM", u"股價的標準模型", LS(15)],
            [u"隱含波動度", u"implied volatility", u"由市場價格反推的波動度", LS(29)],
            [u"波動度偏斜、微笑", u"skew, smile", u"隱含波動度隨履約價變化", LS(29)],
            [u"希臘字母", u"Greeks", u"Delta、Gamma、Theta、Vega、Rho", LS(26)],
            [u"Delta 避險", u"delta hedging", u"用標的抵銷價格風險", LS(28)],
            [u"肥尾", u"fat tails", u"極端事件比常態分布頻繁", LS(35)],
        ]),
    ],
}

REFERENCES = [FORMULAS, GLOSSARY]
