# -*- coding: utf-8 -*-
"""馬斯克的第一性原理：參考頁——互動工具箱、名詞速查與年表。"""
from fp_common import LS, FPLIB, fpw

GUIDE = {
    "file": "guide.html", "title": u"第一性原理工具箱", "h1": u"第一性原理工具箱", "icon": u"🧰",
    "description": u"拆解樹、白痴指數、五步驟、重複使用、發射成本、學習曲線、預測對照、Starship 試飛、檢查清單",
    "body": [
        ("raw", u"<script>%s</script>" % FPLIB),
        ("p", u"工具中的數字多為公開估算或教學示意；近期事件以 2026 年 10 月前的公開資料為準。"),
        ("h", u"1. 拆解樹（第 7 課）"), fpw({"t": "tree"}),
        ("h", u"2. 白痴指數（第 8 課）"), fpw({"t": "idiot"}),
        ("h", u"3. 五步驟演算法（第 10 課）"), fpw({"t": "algo"}),
        ("h", u"4. 重複使用經濟學（第 17 課）"), fpw({"t": "reuse"}),
        ("h", u"5. 發射成本（第 18 課）"), fpw({"t": "launch"}),
        ("h", u"6. 學習曲線與原料地板（第 21 課）"), fpw({"t": "learn"}),
        ("h", u"7. Starship 試飛紀錄（第 34 課）"), fpw({"t": "ship"}),
        ("h", u"8. 預測與實際（第 41 課）"), fpw({"t": "pred"}),
        ("h", u"9. 第一性原理檢查清單（第 51 課）"), fpw({"t": "check"}),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"名詞速查與年表", "h1": u"名詞速查與年表", "icon": u"📖",
    "description": u"方法名詞與馬斯克事業年表",
    "body": [
        ("h", u"1. 名詞"),
        ("t", [u"名詞", u"說明", u"課"],
         [[u"第一性原理", u"拆到確定為真的基本事實，再往上推導", LS(1)], [u"類比推理", u"照著類似事物或既有做法來做", LS(4)],
          [u"白痴指數", u"零件價格 ÷ 原料成本", LS(8)], [u"理論極限", u"物理上最好能做到的程度", LS(9)], [u"五步驟演算法", u"質疑需求、刪除、簡化、加速、自動化", LS(10)],
          [u"垂直整合", u"自己製造上下游零件與服務", LS(15)], [u"萊特定律", u"累積產量每翻倍，單位成本下降固定比例", LS(22)], [u"OTA", u"透過網路更新車輛軟體", LS(24)],
          [u"一體化壓鑄", u"以大型壓鑄機把許多零件鑄成一件", LS(26)], [u"迭代式開發", u"快速試做、試飛、從失敗修正", LS(34)],
          [u"倖存者偏差", u"只看到成功者而忽略失敗者", LS(44)], [u"切斯特頓的柵欄", u"拆除規則前先了解它為何存在", LS(43)]]),
        ("h", u"2. 年表"),
        ("t", [u"年份", u"事件", u"課"],
         [[u"1999～2002", u"X.com、PayPal，eBay 收購", LS(29)], [u"2002", u"創立 SpaceX", LS(13)], [u"2004", u"投資並加入 Tesla 董事會", LS(21)],
          [u"2008", u"Falcon 1 第四次發射成功；Roadster 交車；NASA 貨運合約", LS(16)], [u"2012", u"Model S、超級充電站、OTA；第一性原理訪談", LS(5)],
          [u"2013", u"Hyperloop 白皮書", LS(31)], [u"2015", u"Falcon 9 第一節首次著陸", LS(17)], [u"2016", u"Tesla 收購 SolarCity；創立 Neuralink、Boring Company", LS(30)],
          [u"2017～2018", u"Model 3 生產地獄", LS(27)], [u"2019", u"Starship 改用不鏽鋼；首批 Starlink", LS(19)], [u"2020", u"Crew Dragon 載人；Model Y 一體化壓鑄", LS(26)],
          [u"2022", u"收購推特", LS(33)], [u"2023", u"推特改名 X；創立 xAI；Starship 首次試飛", LS(36)], [u"2024", u"Neuralink 首例人體植入；筷子夾住助推器；Colossus", LS(34)],
          [u"2025", u"DOGE；Robotaxi 奧斯汀試營運；xAI 併 X；BYD 純電車銷量超越 Tesla", LS(39)],
          [u"2026", u"SpaceX 併 xAI 並上市；Cybercab 開始生產；Starship 首次入軌；GAO 審查 DOGE", LS(36)]]),
    ],
}

REFERENCES = [GUIDE, GLOSSARY]
