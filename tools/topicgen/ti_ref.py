# -*- coding: utf-8 -*-
"""股市常見指標與應用：參考頁——互動工具箱、公式速查、名詞中英對照。"""
from ti_common import TILIB, MDLIB, KATEX, LS, M, K, tw
from ti_i import _FS

GUIDE = {
    "file": "guide.html", "title": u"指標互動工具箱", "h1": u"指標互動工具箱", "icon": u"🧰",
    "description": u"綜合 K 線圖、回測器、本益比河流圖、凱利公式、風險指標、選擇權未平倉、市場寬度、K 線與價格型態、費波納契、背離練習",
    "body": [
        ("raw", u"<script>%s</script>" % TILIB),
        ("p", u"所有圖表都使用程式產生的模擬股價，用來理解指標的計算與行為，不代表任何真實股票。"),
        ("h", u"1. 綜合 K 線圖（趨勢＋擺盪＋量）"), K(u"均線、布林通道搭配 MACD、KD、成交量，可切換日線與週線：", ov=["sma", "boll"], sub=["vol", "macd", "kd"], ctl=["ma1", "ma2", "ma3"], tf=1),
        ("h", u"2. 趨勢跟隨（第 8、16 課）"), K(u"SAR、Supertrend 與 DMI：", ov=["sar", "sup"], sub=["dmi", "atr"], sig="sup"),
        ("h", u"3. 量能（第 18～21 課）"), K(u"成交量分布、VWAP、OBV 與 MFI：", ov=["vp", "vwap"], sub=["vol", "obv", "mfi"]),
        ("h", u"4. 簡易回測器（第 49 課）"), tw("bt", u"選策略、盤勢、成本，並檢驗過度擬合與運氣："),
        ("h", u"5. 本益比河流圖（第 37 課）"), tw("river", u""),
        ("h", u"6. 風險與績效指標（第 46 課）"), tw("risk", u""),
        ("h", u"7. 凱利公式（第 50 課）"), tw("kelly", u""),
        ("h", u"8. 選擇權未平倉（第 31 課）"), tw("oi", u""),
        ("h", u"9. 市場寬度（第 26 課）"), tw("breadth", u""),
        ("h", u"10. K 線型態（第 23 課）"), tw("cdl", u""),
        ("h", u"11. 價格型態（第 24 課）"), tw("pat", u""),
        ("h", u"12. 費波納契（第 25 課）"), tw("fib", u""),
        ("h", u"13. 背離練習（第 14 課）"), tw("div", u""),
        ("h", u"14. 均線權重（第 4 課）"), tw("wts", u""),
        ("h", u"15. F-Score（第 41 課）"), tw("fs", u"", items=_FS),
    ],
}

_H = [u"指標", u"公式", u"常用參數／判讀", u"課"]

FORMULAS = {
    "file": "formulas.html", "title": u"指標公式速查", "h1": u"指標公式速查", "icon": u"🧮",
    "description": u"趨勢、擺盪、波動、量能、基本面、風險績效指標的公式與常用參數一覽",
    "body": [
        ("p", u"C、H、L、O、V 分別是收盤、最高、最低、開盤、成交量；n 是天數。"),
        ("h", u"1. 趨勢"),
        ("t", _H, [
            [u"SMA", M(r"\frac{1}{n}\sum C"), u"台股 5／20／60／240；美股 50／200", LS(4)],
            [u"EMA", M(r"E_t = E_{t-1} + \alpha(C_t - E_{t-1}),\ \alpha = \frac{2}{n+1}"), u"平均落後同 SMA，但轉彎較快", LS(4)],
            [u"扣抵", M(r"\Delta MA = \frac{C_{t+1} - C_{t+1-n}}{n}"), u"收盤高於扣抵值，均線上揚", LS(5)],
            [u"MACD", M(r"DIF = E_{12} - E_{26},\ \text{訊號} = E_9(DIF)"), u"柱狀體 = DIF − 訊號線", LS(6)],
            [u"DMI／ADX", M(r"DX = 100\frac{|{+DI} - ({-DI})|}{{+DI} + ({-DI})}"), u"ADX < 20 盤整、> 25 有趨勢", LS(7)],
            [u"Aroon", M(r"100\frac{n - \text{距高點天數}}{n}"), u"25 日", LS(7)],
            [u"SAR", M(r"S_{t+1} = S_t + AF(EP - S_t)"), u"AF 0.02 起、上限 0.2", LS(8)],
            [u"一目均衡表", M(r"\frac{H_9 + L_9}{2},\ \frac{H_{26} + L_{26}}{2}"), u"先行帶往前平移 26 天", LS(8)],
            [u"KAMA", M(r"ER = \frac{|C_t - C_{t-n}|}{\sum|\Delta C|}"), u"趨勢快、盤整慢", LS(9)]]),
        ("h", u"2. 擺盪與動能"),
        ("t", _H, [
            [u"RSI", M(r"100\frac{\bar U}{\bar U + \bar D}"), u"14 日 70／30；台股 6／12 日 80／20", LS(10)],
            [u"KD", M(r"RSV = 100\frac{C - L_9}{H_9 - L_9},\ K = \tfrac23 K' + \tfrac13 RSV"), u"9,3,3；80／20", LS(11)],
            [u"威廉 %R", M(r"-100\frac{H_n - C}{H_n - L_n}"), u"−20／−80", LS(12)],
            [u"CCI", M(r"\frac{TP - \overline{TP}}{0.015\,MD}"), u"±100", LS(12)],
            [u"UO", M(r"100\frac{4A_7 + 2A_{14} + A_{28}}{7}"), u"30／70，看背離", LS(12)],
            [u"ROC", M(r"100\left(\frac{C_t}{C_{t-n}} - 1\right)"), u"12 日", LS(13)],
            [u"乖離率", M(r"100\frac{C - MA_n}{MA_n}"), u"依個股歷史分布判斷", LS(13)],
            [u"PSY", M(r"100\frac{\text{上漲天數}}{n}"), u"12 日；75／25", LS(14)]]),
        ("h", u"3. 波動"),
        ("t", _H, [
            [u"布林通道", M(r"MA_{20} \pm 2\sigma_{20}"), u"%b、帶寬、擠壓", LS(15)],
            [u"TR／ATR", M(r"TR = \max(H - L, |H - C'|, |L - C'|)"), u"ATR 14 日；停損 2ATR", LS(16)],
            [u"肯特納通道", M(r"EMA_{20} \pm 2ATR_{10}"), u"", LS(16)],
            [u"唐奇安通道", M(r"\max(H, n),\ \min(L, n)"), u"20 日突破、10 日出場", LS(16)],
            [u"歷史波動率", M(r"\sigma(\ln\tfrac{C_t}{C_{t-1}})\sqrt{252}"), u"", LS(17)],
            [u"VIX 換算", M(r"\frac{VIX}{\sqrt{12}}"), u"約一個月一個標準差", LS(17)]]),
        ("h", u"4. 量能與寬度"),
        ("t", _H, [
            [u"OBV", M(r"OBV_t = OBV_{t-1} \pm V_t"), u"看方向與背離", LS(19)],
            [u"CLV／A/D", M(r"\frac{(C - L) - (H - C)}{H - L}"), u"A/D 累加 CLV × V", LS(19)],
            [u"CMF", M(r"\frac{\sum CLV\cdot V}{\sum V}"), u"20 日；±0.25", LS(19)],
            [u"MFI", M(r"100 - \frac{100}{1 + MR}"), u"14 日；80／20", LS(20)],
            [u"VWAP", M(r"\frac{\sum P V}{\sum V}"), u"當日或錨定", LS(20)],
            [u"樞紐點", M(r"P = \frac{H + L + C}{3},\ R_1 = 2P - L"), u"", LS(25)],
            [u"ADL", M(r"ADL_t = ADL_{t-1} + A - D"), u"", LS(26)],
            [u"McClellan", M(r"E_{19}(A - D) - E_{39}(A - D)"), u"", LS(27)],
            [u"TRIN", M(r"\frac{A / D}{AV / DV}"), u"< 1 偏多、> 2 恐慌", LS(27)]]),
        ("h", u"5. 籌碼"),
        ("t", _H, [
            [u"融資維持率", M(r"\frac{\text{現值}}{\text{融資金額}}"), u"整戶 < 130% 追繳", LS(29)],
            [u"券資比", M(r"\frac{\text{融券餘額}}{\text{融資餘額}}"), u"> 30% 偏高", LS(32)],
            [u"PCR", M(r"\frac{\text{賣權}}{\text{買權}}"), u"看歷史極端值", LS(28)],
            [u"Days to Cover", M(r"\frac{\text{放空股數}}{\text{日均量}}"), u"", LS(32)],
            [u"當沖比率", M(r"\frac{\text{當沖量}}{\text{總量}}"), u"", LS(34)]]),
        ("h", u"6. 基本面與大盤估值"),
        ("t", _H, [
            [u"EPS", M(r"\frac{\text{淨利}}{\text{股數}}"), u"看本業、看近四季", LS(35)],
            [u"杜邦分析", M(r"ROE = \frac{NI}{S}\cdot\frac{S}{A}\cdot\frac{A}{E}"), u"", LS(36)],
            [u"PE／PEG", M(r"\frac{P}{EPS},\ \frac{PE}{g}"), u"PEG < 1 偏便宜", LS(37)],
            [u"PB", M(r"\frac{P}{BVPS} = PE \times ROE"), u"資產型產業", LS(38)],
            [u"EV/EBITDA", M(r"\frac{\text{市值} + \text{負債} - \text{現金}}{EBITDA}"), u"", LS(38)],
            [u"殖利率／配息率", M(r"\frac{D}{P},\ \frac{D}{EPS}"), u"", LS(39)],
            [u"自由現金流", M(r"OCF - CapEx"), u"", LS(40)],
            [u"CCC", M(r"DIO + DSO - DPO"), u"", LS(41)],
            [u"Z-Score", M(r"1.2X_1 + 1.4X_2 + 3.3X_3 + 0.6X_4 + X_5"), u"> 2.99 安全、< 1.81 危險", LS(41)],
            [u"高登模型", M(r"P = \frac{D_1}{r - g}"), u"", LS(43)],
            [u"股債利差", M(r"\frac{1}{PE} - y_{10}"), u"", LS(45)]]),
        ("h", u"7. 風險與績效"),
        ("t", _H, [
            [u"CAGR", M(r"\left(\frac{V_1}{V_0}\right)^{1/T} - 1"), u"", LS(46)],
            [u"β", M(r"\frac{\mathrm{Cov}(R_i, R_m)}{\mathrm{Var}(R_m)}"), u"", LS(46)],
            [u"夏普值", M(r"\frac{R - R_f}{\sigma}"), u"長期 > 1 很優秀", LS(47)],
            [u"Calmar", M(r"\frac{CAGR}{|MDD|}"), u"", LS(47)],
            [u"期望值", M(r"pW - (1 - p)L"), u"打平勝率 1/(1+R)", LS(47)],
            [u"凱利", M(r"f^* = p - \frac{1 - p}{R}"), u"實務用半凱利", LS(50)],
            [u"部位", M(r"\frac{\text{資金}\times\text{風險}\%}{\text{進場} - \text{停損}}"), u"每筆 0.5%～2%", LS(50)]]),
        ("raw", KATEX),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"指標名詞中英對照", "h1": u"指標名詞中英對照", "icon": u"📖",
    "description": u"技術、籌碼、基本面與總經指標的中英名稱對照",
    "body": [
        ("t", [u"中文", u"英文", u"課"], [
            [u"移動平均線", u"Moving Average（SMA／EMA／WMA）", LS(4)], [u"黃金交叉／死亡交叉", u"Golden Cross／Death Cross", LS(4)],
            [u"指數平滑異同移動平均線", u"MACD", LS(6)], [u"趨向指標", u"Directional Movement Index（DMI）、ADX", LS(7)],
            [u"拋物線停損轉向", u"Parabolic SAR", LS(8)], [u"一目均衡表", u"Ichimoku Kinko Hyo", LS(8)],
            [u"相對強弱指標", u"Relative Strength Index（RSI）", LS(10)], [u"隨機指標", u"Stochastic Oscillator（KD）", LS(11)],
            [u"順勢指標", u"Commodity Channel Index（CCI）", LS(12)], [u"終極擺盪指標", u"Ultimate Oscillator", LS(12)],
            [u"變動率", u"Rate of Change（ROC）", LS(13)], [u"乖離率", u"BIAS", LS(13)], [u"心理線", u"Psychological Line（PSY）", LS(14)],
            [u"背離", u"Divergence", LS(14)], [u"布林通道", u"Bollinger Bands", LS(15)], [u"平均真實區間", u"Average True Range（ATR）", LS(16)],
            [u"唐奇安通道", u"Donchian Channel", LS(16)], [u"肯特納通道", u"Keltner Channel", LS(16)], [u"歷史／隱含波動率", u"Historical／Implied Volatility", LS(17)],
            [u"能量潮", u"On-Balance Volume（OBV）", LS(19)], [u"累積／派發線", u"Accumulation/Distribution Line", LS(19)], [u"資金流量指標", u"Money Flow Index（MFI）", LS(20)],
            [u"成交量加權平均價", u"VWAP", LS(20)], [u"成交量分布", u"Volume Profile、POC、Value Area", LS(21)],
            [u"支撐／壓力", u"Support／Resistance", LS(22)], [u"缺口", u"Gap", LS(22)], [u"頭肩頂", u"Head and Shoulders", LS(24)],
            [u"費波納契回撤", u"Fibonacci Retracement", LS(25)], [u"樞紐點", u"Pivot Point", LS(25)], [u"騰落線", u"Advance-Decline Line", LS(26)],
            [u"阿姆斯指數", u"TRIN／Arms Index", LS(27)], [u"恐慌指數", u"VIX", LS(28)], [u"賣買權比", u"Put/Call Ratio", LS(28)],
            [u"融資維持率", u"Margin Maintenance Ratio", LS(29)], [u"三大法人", u"Institutional Investors", LS(30)], [u"未平倉量", u"Open Interest", LS(31)],
            [u"最大痛點", u"Max Pain", LS(31)], [u"軋空", u"Short Squeeze", LS(32)], [u"借券", u"Securities Borrowing and Lending（SBL）", LS(32)],
            [u"每股盈餘", u"Earnings Per Share（EPS）", LS(35)], [u"股東權益報酬率", u"Return on Equity（ROE）", LS(36)], [u"本益比", u"Price-to-Earnings（PE）", LS(37)],
            [u"股價淨值比", u"Price-to-Book（PB）", LS(38)], [u"企業價值", u"Enterprise Value（EV）", LS(38)], [u"殖利率", u"Dividend Yield", LS(39)],
            [u"自由現金流", u"Free Cash Flow（FCF）", LS(40)], [u"現金循環週期", u"Cash Conversion Cycle", LS(41)], [u"採購經理人指數", u"PMI", LS(42)],
            [u"殖利率曲線倒掛", u"Yield Curve Inversion", LS(43)], [u"美元指數", u"US Dollar Index（DXY）", LS(44)], [u"席勒本益比", u"CAPE", LS(45)],
            [u"年化報酬", u"CAGR", LS(46)], [u"最大回撤", u"Maximum Drawdown（MDD）", LS(46)], [u"風險值", u"Value at Risk（VaR）", LS(46)],
            [u"夏普值", u"Sharpe Ratio", LS(47)], [u"獲利因子", u"Profit Factor", LS(47)], [u"前視偏差", u"Look-ahead Bias", LS(49)],
            [u"過度擬合", u"Overfitting", LS(49)], [u"凱利公式", u"Kelly Criterion", LS(50)]]),
    ],
}

REFERENCES = [GUIDE, FORMULAS, GLOSSARY]
