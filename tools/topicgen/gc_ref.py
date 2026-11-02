# -*- coding: utf-8 -*-
"""全球市值前 20 大：參考頁——互動實驗室、名詞對照。"""
from gc_common import GCLIB, LS, gw

LAB = {
    "file": "lab.html", "title": u"互動實驗室", "h1": u"互動實驗室", "icon": u"🧪",
    "description": u"你的一天、市值排行賽跑、二十大比較總表、營收結構、成長情境模擬、簡易估值、護城河雷達",
    "body": [
        ("raw", u"<script>%s</script>" % GCLIB),
        ("p", u"把課程中的互動工具集中在這裡，方便隨時回來比較與練習。"),
        ("h", u"1. 你的一天：你碰到了哪幾家（第 1、32 課）"), gw("day"),
        ("h", u"2. 市值排行賽跑（第 4 課）"), gw("race"),
        ("h", u"3. 二十大比較總表（第 1、25 課）"), gw("table"),
        ("h", u"4. 營收結構圖（第 5～24 課）"), gw("seg"),
        ("h", u"5. 成長情境模擬器（第 29 課）"), gw("sim"),
        ("h", u"6. 簡易估值計算器（第 27、29 課）"), gw("dcf"),
        ("h", u"7. 護城河雷達圖（第 28 課）"), gw("moat"),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"名詞對照", "h1": u"名詞對照", "icon": u"📖",
    "description": u"財務、產業與科技名詞的中英對照與白話解釋",
    "body": [
        ("t", [u"中文", u"英文", u"白話解釋", u"課"], [
            [u"市值", u"market capitalization", u"股價乘以股數，買下整家公司的價格", LS(1)],
            [u"營收", u"revenue", u"一年賣東西收到的錢", LS(2)],
            [u"毛利率", u"gross margin", u"每 100 元營收扣掉直接成本後剩多少", LS(2)],
            [u"營業利益", u"operating income", u"本業賺的錢", LS(2)],
            [u"淨利率", u"net margin", u"每 100 元營收最後真正賺多少", LS(2)],
            [u"自由現金流", u"free cash flow", u"營業現金扣掉資本支出，真正多出來的錢", LS(2)],
            [u"資本支出", u"capital expenditure (capex)", u"蓋工廠、資料中心、買設備的錢", LS(2)],
            [u"本益比", u"price-to-earnings ratio (P/E)", u"市值除以淨利", LS(2)],
            [u"財年", u"fiscal year", u"公司自訂的會計年度", LS(25)],
            [u"營利模式", u"business model", u"公司怎麼賺錢", LS(3)],
            [u"經常性收入", u"recurring revenue", u"訂閱等每期自動流入的收入", LS(3)],
            [u"網路效應", u"network effect", u"用的人越多越好用", LS(28)],
            [u"轉換成本", u"switching cost", u"換掉一個產品的麻煩與代價", LS(28)],
            [u"護城河", u"economic moat", u"讓對手難以搶走獲利的優勢", LS(28)],
            [u"晶圓代工", u"foundry", u"只替別人製造晶片", LS(11)],
            [u"無晶圓廠", u"fabless", u"只設計晶片、不自己製造", LS(10)],
            [u"先進封裝", u"advanced packaging (CoWoS)", u"把多顆晶片與記憶體封裝在一起", LS(11)],
            [u"高頻寬記憶體", u"HBM", u"疊在 AI 晶片旁的高速記憶體", LS(14)],
            [u"客製晶片", u"ASIC", u"為特定客戶與用途設計的晶片", LS(12)],
            [u"圖形處理器", u"GPU", u"擅長平行運算的晶片，AI 的主力", LS(10)],
            [u"雲端運算", u"cloud computing", u"租用遠端的運算與儲存", LS(6)],
            [u"保險浮存金", u"insurance float", u"收了保費、還沒理賠前可以運用的錢", LS(19)],
            [u"淨利息收入", u"net interest income", u"銀行的存放款利差收入", LS(20)],
            [u"跨境交易", u"cross-border transaction", u"在國外或外國網站刷卡", LS(21)],
            [u"上游／下游", u"upstream / downstream", u"石油業的開採與煉油銷售", LS(23)],
            [u"專利懸崖", u"patent cliff", u"專利到期後營收大幅下滑", LS(18)],
            [u"首次公開發行", u"IPO", u"公司第一次在股市公開賣股票", LS(17)],
            [u"情境分析", u"scenario analysis", u"同時考慮樂觀、基準、悲觀等多種未來", LS(29)],
            [u"年複合成長率", u"CAGR", u"平均每年的成長速度", LS(29)],
            [u"現金流折現", u"discounted cash flow (DCF)", u"把未來的現金折算成今天的價值", LS(29)],
        ]),
    ],
}

REFERENCES = [LAB, GLOSSARY]
