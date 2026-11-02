# -*- coding: utf-8 -*-
"""總體經濟：參考頁——互動實驗室、公式總表、名詞對照。"""
from mx_common import MXLIB, LS, xw, KATEX, M

LAB = {
    "file": "lab.html", "title": u"總經互動實驗室", "h1": u"總經互動實驗室", "icon": u"🧪",
    "description": u"通膨與購買力、貨幣創造、殖利率曲線、泰勒法則、房貸、利率與股價、乘數、利差與匯率、景氣燈號、菲利普曲線",
    "body": [
        ("raw", u"<script>%s</script>" % MXLIB),
        ("p", u"把課程中的互動工具集中在這裡。"),
        ("h", u"1. 通膨與購買力（第 7 課）"), xw("infl"),
        ("h", u"2. 台灣景氣對策信號（第 10 課）"), xw("signal"),
        ("h", u"3. 銀行貨幣創造（第 13 課）"), xw("money"),
        ("h", u"4. 殖利率曲線（第 16 課）"), xw("yc"),
        ("h", u"5. 利率與房貸（第 21 課）"), xw("mortgage"),
        ("h", u"6. 泰勒法則（第 24 課）"), xw("taylor"),
        ("h", u"7. 菲利普曲線（第 25 課）"), xw("phillips"),
        ("h", u"8. 乘數效果（第 30 課）"), xw("mult"),
        ("h", u"9. 利差與匯率（第 33 課）"), xw("fx"),
        ("h", u"10. 利率與股價估值（第 46 課）"), xw("pv"),
    ],
}

FORMULAS = {
    "file": "formulas.html", "title": u"總經公式總表", "h1": u"總經公式總表", "icon": u"📋",
    "description": u"GDP、通膨、貨幣、利率、債券、政策法則、財政、匯率與估值的常用公式",
    "body": [
        ("raw", KATEX),
        ("t", [u"主題", u"公式", u"課"], [
            [u"支出面 GDP", M(r"GDP = C + I + G + (X - M)"), LS(5)],
            [u"實質 GDP", M(r"\text{real} = \text{nominal} / \text{deflator} \times 100"), LS(6)],
            [u"季增年率", M(r"(1 + g_q)^4 - 1"), LS(6)],
            [u"通膨率", M(r"\pi = (CPI_t - CPI_{t-12}) / CPI_{t-12}"), LS(7)],
            [u"費雪方程式", M(r"i \approx r + \pi^e"), LS(7)],
            [u"失業率", M(r"u = U / LF"), LS(8)],
            [u"歐肯法則", M(r"\Delta u \approx -\tfrac{1}{2}(g - g^*)"), LS(8)],
            [u"貨幣數量學說", M(r"MV = PY"), LS(12)],
            [u"貨幣乘數", M(r"m = (1 + c) / (r + c)"), LS(13)],
            [u"債券價格", M(r"P = \sum C/(1+y)^t + F/(1+y)^n"), LS(15)],
            [u"殖利率曲線利差", M(r"y_{10} - y_{2}"), LS(16)],
            [u"信用利差", M(r"y_{corp} - y_{tsy}"), LS(17)],
            [u"房貸月付金", M(r"PMT = L\,m(1+m)^n / ((1+m)^n - 1)"), LS(21)],
            [u"泰勒法則", M(r"i = r^* + \pi + 0.5(\pi - \pi^*) + 0.5(y - y^*)"), LS(24)],
            [u"菲利普曲線", M(r"\pi = \pi^e - \beta(u - u_n)"), LS(25)],
            [u"財政赤字", M(r"G + TR - T"), LS(29)],
            [u"乘數", M(r"k = 1 / (1 - MPC(1 - t) + m)"), LS(30)],
            [u"拋補利率平價", M(r"F = S (1 + i_d) / (1 + i_f)"), LS(33)],
            [u"購買力平價", M(r"\Delta S / S \approx \pi_d - \pi_f"), LS(33)],
            [u"經常帳", M(r"CA = S - I"), LS(35)],
            [u"套息報酬", M(r"(i_{high} - i_{low}) - \Delta S / S"), LS(37)],
            [u"高登成長模型", M(r"P = D_1 / (r - g)"), LS(46)],
            [u"外資美元報酬", M(r"R_{USD} \approx R_{TWD} + \Delta FX"), LS(49)],
        ]),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"總經名詞對照", "h1": u"總經名詞對照", "icon": u"📖",
    "description": u"總體經濟與貨幣政策常用名詞的中英對照",
    "body": [
        ("t", [u"中文", u"英文", u"課"], [
            [u"國內生產毛額", u"GDP", LS(5)], [u"消費者物價指數", u"CPI", LS(7)], [u"個人消費支出物價指數", u"PCE price index", LS(7)], [u"核心通膨", u"core inflation", LS(7)],
            [u"非農就業", u"nonfarm payrolls", LS(8)], [u"勞動參與率", u"labor force participation rate", LS(8)], [u"採購經理人指數", u"PMI", LS(9)], [u"景氣對策信號", u"monitoring indicators", LS(10)],
            [u"部分準備制度", u"fractional reserve banking", LS(13)], [u"貨幣供給", u"money supply (M1, M2)", LS(14)], [u"殖利率", u"yield", LS(15)], [u"存續期間", u"duration", LS(15)],
            [u"殖利率曲線倒掛", u"yield curve inversion", LS(16)], [u"信用利差", u"credit spread", LS(17)], [u"聯邦公開市場委員會", u"FOMC", LS(19)], [u"點陣圖", u"dot plot", LS(19)],
            [u"準備金利息", u"interest on reserve balances (IORB)", LS(20)], [u"隔夜逆回購", u"overnight reverse repo (ON RRP)", LS(20)], [u"量化寬鬆／緊縮", u"QE / QT", LS(22)], [u"前瞻指引", u"forward guidance", LS(23)],
            [u"中性利率", u"neutral rate (r*)", LS(24)], [u"通膨目標制", u"inflation targeting", LS(25)], [u"重貼現率", u"discount rate", LS(26)], [u"選擇性信用管制", u"selective credit controls", LS(26)],
            [u"殖利率曲線控制", u"yield curve control (YCC)", LS(27)], [u"自動穩定器", u"automatic stabilizers", LS(29)], [u"排擠效果", u"crowding out", LS(30)], [u"期限溢酬", u"term premium", LS(31)],
            [u"財政主導", u"fiscal dominance", LS(32)], [u"不可能三角", u"impossible trinity", LS(33)], [u"經常帳", u"current account", LS(35)], [u"套息交易", u"carry trade", LS(37)],
            [u"停滯性通膨", u"stagflation", LS(40)], [u"資產負債表衰退", u"balance sheet recession", LS(41)], [u"軟著陸", u"soft landing", LS(39)], [u"股權風險溢酬", u"equity risk premium", LS(46)],
        ]),
    ],
}

REFERENCES = [LAB, FORMULAS, GLOSSARY]
