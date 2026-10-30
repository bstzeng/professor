# -*- coding: utf-8 -*-
"""Ontology：模組 J Palantir（55～64）、K 總結（65）。"""
from ont_common import *

MODULES = [
(u"模組 J｜Palantir：把 Ontology 變成作業系統", [

lesson(u"Palantir 是誰",
  u"一家把「本體」放在產品核心的軟體公司",
  [u"認識 Palantir 的創辦背景與名稱由來", u"認識四大產品線", u"理解它為什麼出現在一門 Ontology 課程裡"],
  [("p", u"<strong>Palantir Technologies</strong> 2003 年創立於加州帕羅奧圖，創辦人包括 PayPal 共同創辦人彼得・提爾、哲學博士出身的執行長亞歷克斯・卡普，以及喬・朗斯代爾、史蒂芬・柯恩、內森・格廷斯。名稱來自托爾金《魔戒》中的「真知晶球」（palantír）——能看見遠方事物的水晶球。"),
   ("p", u"起點是一個問題：PayPal 用軟體偵測詐欺很有效，能不能把類似的方法用在反恐情報？2001 年九一一事件後，美國情報機構最大的教訓之一，就是各單位的資料沒有連起來。"),
   ow("timeline", u"Palantir 的重要事件（可依類別篩選）："),
   ("h", u"四大產品"),
   ("t", [u"產品", u"推出", u"用途"],
    [[u"<strong>Gotham</strong>", u"2008 前後", u"政府、國防與情報：整合多來源資料，分析人、地、事件的關聯（第 56 課）"],
     [u"<strong>Foundry</strong>", u"2016 前後推向商業", u"企業的資料整合與營運平台，核心就是 <strong>Ontology</strong>（第 57、59 課）"],
     [u"<strong>Apollo</strong>", u"2021 公開", u"持續部署：讓同一套軟體在公有雲、地端、機密網路、戰場邊緣裝置上自動更新"],
     [u"<strong>AIP</strong>", u"2023", u"人工智慧平台：把大型語言模型接上 Ontology，讓 AI 能查詢資料、呼叫動作（第 62 課）"]]),
   ("h", u"為什麼出現在這門課"),
   ("p", u"Palantir 把哲學名詞 Ontology 拿來作為產品的核心概念，但它的 Ontology 和 OWL 本體有相同也有不同："),
   ("t", [u"", u"OWL／語意網的本體", u"Palantir 的 Ontology"],
    [[u"目的", u"精確定義概念、跨組織共享、邏輯推理", u"把企業資料變成可操作的物件，支撐決策與行動"], [u"核心元素", u"類別、屬性、公理", u"物件類型、屬性、連結類型，加上<strong>動作</strong>與<strong>函數</strong>"],
     [u"推理", u"描述邏輯推理機", u"主要是程式邏輯、規則與模型，而非 DL 推理"], [u"標準", u"W3C 開放標準", u"專有平台（提供 API 與 SDK）"],
     [u"讀寫", u"主要用於描述與查詢", u"<strong>可以寫回</strong>：動作會改變資料並同步到原始系統"]]),
   ("p", u"簡單說：語意網的本體回答「世界是什麼」；Palantir 的 Ontology 進一步回答「我們能對它做什麼」。這正是本課程從亞里斯多德走到企業 AI 的最後一段路。"),
  ],
  u"Palantir 2003 年由提爾、卡普、朗斯代爾、柯恩、格廷斯創立，名稱取自《魔戒》的真知晶球，起源於把 PayPal 的反詐欺思路用於九一一後的情報整合。四大產品為情報分析的 Gotham、以 Ontology 為核心的企業平台 Foundry、持續部署的 Apollo 與連接 LLM 的 AIP。其 Ontology 與 OWL 本體同樣以物件與關係為核心，但更強調動作、函數與寫回，回答「能對世界做什麼」。",
  [u"Palantir 的名稱由來是什麼？", u"Palantir 的 Ontology 和 OWL 本體最大的差別是什麼？", u"為什麼九一一事件和 Palantir 的誕生有關？"]),

lesson(u"Gotham：情報分析起家",
  u"把散落的資料連成一張網",
  [u"理解情報分析的資料整合問題", u"認識 Gotham 的核心功能", u"理解存取控制與稽核在其中的地位"],
  [("p", u"情報分析師面對的資料來自四面八方：通聯紀錄、金融交易、出入境、報告文件、衛星影像、線人資料……每一種存放在不同的系統，格式不同，權限不同。分析師的工作是找出其中的<strong>關聯</strong>：這個電話號碼和那個帳戶有關嗎？這兩個人在同一個時間出現在同一個地點嗎？"),
   ("h", u"Gotham 的做法"),
   ("ul", [u"<strong>以實體為中心</strong>：不論資料來自哪裡，都對應到「人」「組織」「地點」「事件」「物品」等物件，同一個實體的資料合併在一起——這就是一個本體。", u"<strong>圖形分析</strong>：以節點和連線呈現物件之間的關係，分析師可以從一個人出發，一步步展開他的關聯網路。", u"<strong>時間與地理</strong>：事件放在時間軸與地圖上，找出時空上的交會。", u"<strong>協作</strong>：分析成果可以分享、標註，形成組織的共同知識。"]),
   ("h", u"安全模型"),
   ("p", u"情報資料的權限極為複雜：同一份報告，不同人能看到的部分不同。Gotham 從一開始就把<strong>細粒度存取控制</strong>和<strong>稽核</strong>放在核心：每一筆資料都帶有標記（例如機密等級、來源限制），每一次查看與操作都留下紀錄。Palantir 一直把這點當作回應隱私疑慮的主要論點（第 64 課）。"),
   PY(u"""
# 以實體為中心的關聯分析：多來源資料 → 同一張圖 → 找出兩人之間的關聯路徑
import networkx as nx

calls  = [("號碼A", "號碼B"), ("號碼B", "號碼C")]                   # 通聯紀錄
owners = [("甲", "號碼A"), ("乙", "號碼C")]                         # 門號登記
money  = [("乙", "帳戶X"), ("丙", "帳戶X")]                         # 金融資料（共用帳戶）
trips  = [("丙", "事件：某日某港口"), ("甲", "事件：某日某港口")]    # 出入境

G = nx.Graph()
for src, edges in [("通聯", calls), ("門號", owners), ("金融", money), ("出入境", trips)]:
    for a, b in edges:
        G.add_edge(a, b, source=src)        # 每條邊記得它來自哪個資料源（出處）

path = nx.shortest_path(G, "甲", "丙")
print(" → ".join(path))
for a, b in zip(path, path[1:]):
    print(f"  {a} — {b}：來源 {G[a][b]['source']}")
"""),
   ("note", u"和 Ontology 的關係", [("p", u"這個程式片段裡其實已經有一個隱含的本體：人、門號、帳戶、事件是不同的物件類型，「撥打」「登記」「持有」「出現於」是不同的連結類型。Gotham 的價值在於把這個本體明確化、規模化，並套上安全控制。")]),
  ],
  u"情報分析的難題是資料散落於格式與權限各異的系統，而分析師需要找出其中的關聯。Gotham 以實體為中心合併多來源資料，提供圖形、時間與地理分析與協作，本質上就是一個本體。它從一開始就以細粒度存取控制與完整稽核為核心，資料帶有機密等級等標記，每次操作皆有紀錄，這也是 Palantir 回應隱私疑慮的主要論點。",
  [u"為什麼「以實體為中心」能解決多來源資料的整合問題？", u"在上面的程式中，隱含的物件類型和連結類型有哪些？", u"為什麼情報系統特別需要細粒度存取控制？"]),

lesson(u"Foundry 與前線部署工程師",
  u"把情報分析的方法帶進企業，以及一種特殊的銷售模式",
  [u"認識 Foundry 平台的組成", u"理解前線部署工程師（FDE）模式", u"評估這種模式的優缺點"],
  [("p", u"2010 年代，Palantir 把同樣的方法帶進企業：製造、能源、醫療、金融、航空。商業平台後來稱為 <strong>Foundry</strong>。"),
   ("h", u"Foundry 的組成（簡化）"),
   ("t", [u"層", u"功能"],
    [[u"資料連接", u"連到 ERP、MES、資料庫、檔案、串流、API 等數百種來源"], [u"資料整合", u"Pipeline Builder（視覺化）、Code Repositories（Python／PySpark、SQL、Java）建立轉換管線；有版本與血緣追蹤"],
     [u"<strong>Ontology</strong>", u"把整合後的資料對應成物件類型、屬性、連結；定義動作與函數"], [u"應用", u"Workshop（低程式碼建應用）、Quiver（分析）、Contour（表格分析）、地圖等"],
     [u"AI", u"模型整合與 AIP（第 62 課）"], [u"治理", u"權限、標記、稽核、資料血緣"]]),
   PY(u"""
# Foundry 的資料轉換通常寫成 Python（PySpark）；以下是其轉換函式的寫法示意
from transforms.api import transform_df, Input, Output     # Foundry 平台提供的套件
from pyspark.sql import functions as F

@transform_df(
    Output("/Company/ontology/aircraft_status"),
    maintenance=Input("/Company/raw/mro_work_orders"),
    fleet=Input("/Company/raw/fleet_master"),
)
def compute(maintenance, fleet):
    open_wo = (maintenance.filter(F.col("status") == "OPEN")
                          .groupBy("tail_number").agg(F.count("*").alias("open_work_orders")))
    return (fleet.join(open_wo, "tail_number", "left")
                 .withColumn("available", F.coalesce(F.col("open_work_orders"), F.lit(0)) == 0))
# 這張輸出表接著被對應為 Ontology 中的「飛機」物件類型（每列一架、tail_number 為主鍵）
"""),
   ("h", u"前線部署工程師（FDE）"),
   ("p", u"Palantir 早期最有特色的做法，是派工程師直接進駐客戶現場，稱為<strong>前線部署工程師</strong>（Forward Deployed Engineer）。他們不只是安裝軟體，而是和客戶一起找出問題、整合資料、建立應用，再把在現場反覆出現的需求帶回產品。"),
   ("t", [u"優點", u"缺點"],
    [[u"真正解決客戶的問題，建立深厚關係", u"成本高、毛利低，被批評「更像顧問公司」"], [u"產品從實戰中長出來（例如 Ontology 就是這樣成形的）", u"擴張速度受限於人力"],
     [u"客戶黏著度高，一旦用上很難離開", u"早期每個導入案都要很長時間才能看到成果"]]),
   ("p", u"Palantir 後來的策略是把 FDE 的經驗不斷產品化，讓平台越來越能自助；2023 年的 AIP 訓練營（第 62 課）更把「幾個月的導入」壓縮成「幾天的實作」。FDE 這個職稱與模式，近年也被許多 AI 公司仿效。"),
  ],
  u"Foundry 把情報分析的方法帶進企業，由資料連接、整合管線（Pipeline Builder 與 Python／PySpark 程式碼庫）、Ontology、應用（Workshop、Quiver 等）、AI 與治理組成。前線部署工程師進駐客戶現場解決問題並把需求帶回產品，優點是深度與黏著度、產品從實戰成形，缺點是成本高、擴張慢。Palantir 持續將其產品化，並以 AIP 訓練營縮短導入時間。",
  [u"在 Foundry 中，資料從原始系統到 Ontology 物件要經過哪些步驟？", u"FDE 模式為什麼被批評「像顧問公司」？", u"為什麼說 Palantir 的 Ontology 是「從現場長出來的」？"]),

lesson(u"上市、商業模式與估值爭論",
  u"怎麼賺錢、靠什麼成長、為什麼看法兩極",
  [u"理解 Palantir 的營收結構與商業模式", u"認識主要的成長動力", u"理解多空雙方對估值的論點"],
  [("p", u"Palantir 在 2020 年 9 月以<strong>直接上市</strong>的方式在紐約證交所掛牌（不發行新股募資，既有股東直接出售），同年總部從帕羅奧圖遷到丹佛。2024 年 9 月納入 S&P 500，11 月將掛牌轉到那斯達克。"),
   ("h", u"營收結構"),
   ("p", u"Palantir 把營收分為<strong>政府</strong>與<strong>商業</strong>兩大部門，再各分美國與國際。它主要以軟體訂閱與平台使用收費，合約常為多年期。"),
   ("t", [u"年度", u"全年營收（約）", u"年增率（約）", u"備註"],
    [[u"2020", u"11 億美元", u"47%", u"上市當年"], [u"2023", u"22 億美元", u"17%", u"首度全年 GAAP 獲利"], [u"2024", u"29 億美元", u"29%", u"AIP 帶動商業成長加速"],
     [u"2025", u"44.75 億美元", u"56%", u"美國商業營收約 14.65 億美元，年增約 109%（2026 年 2 月公布）"]]),
   ("p", u"（數字依公司公開財報整理並四捨五入，僅供理解規模與趨勢。）"),
   ("h", u"商業模式的特點"),
   ("ul", [u"<strong>「取得、擴張、規模化」</strong>：先以小範圍導入取得客戶，證明價值後擴大到更多部門與使用案例，單一客戶的營收逐年成長。", u"<strong>平台而非專案</strong>：每個新應用都建在同一套 Ontology 上，邊際成本越來越低。", u"<strong>高轉換成本</strong>：企業的資料管線、Ontology、應用與工作流程都在平台上，離開的代價很高。", u"<strong>政府的長期合約</strong>：例如 2025 年 7 月美國陸軍宣布的企業協議，整合 75 份既有合約，期限 10 年、<strong>上限</strong> 100 億美元（上限不等於保證支出，每 18～24 個月重新評估）。"]),
   ("h", u"估值爭論"),
   ("t", [u"看多的論點", u"看空的論點"],
    [[u"AI 應用落地的少數贏家：企業要的不是模型，而是能接上自家資料與流程的平台", u"市值相對於營收與獲利的倍數極高，已經反映了多年的高成長預期"],
     [u"美國商業營收高速成長，客戶數與每客戶營收同步上升", u"客戶總數仍相對少，營收集中於少數大型客戶與美國政府"],
     [u"毛利率高、已穩定獲利，營運槓桿逐漸顯現", u"股票酬勞的稀釋效果長期受到批評"],
     [u"國防科技與 AI 軍事化的長期趨勢", u"政府預算與政治風向的不確定性；爭議可能影響國際客戶（第 64 課）"]]),
   ("p", u"Palantir 常引用軟體業的「<strong>40 法則</strong>」：營收成長率加上獲利率（常用調整後營業利益率或自由現金流率）超過 40%，代表成長與獲利兼顧。"),
   check(u"40 法則計算", [["g", u"營收年增率（%）", 56, -50, 200, 1], ["m", u"調整後營業利益率（%）", 45, -100, 100, 1]],
         [[u"40 法則分數", "g+m"], [u"是否超過 40（1 = 是）", "(g+m)>=40?1:0"]], u"數值可自行輸入。這只是衡量成長與獲利平衡的經驗法則，不代表估值是否合理。"),
   ("note", u"本課不談股價", [("p", u"股價與市值變動很快，也不是理解這家公司的重點。重要的是：它的價值主張建立在「Ontology 讓 AI 真正能在企業裡做事」這個論點上——這正是本課程前面五十多課在討論的東西。")]),
  ],
  u"Palantir 2020 年 9 月直接上市、總部遷往丹佛，2024 年納入 S&P 500 並轉往那斯達克。營收分政府與商業部門，以多年期訂閱為主，2025 年全年約 44.75 億美元、年增約 56%，美國商業年增約 109%。商業模式為取得、擴張、規模化，平台邊際成本低、轉換成本高，並有美國陸軍 10 年上限 100 億美元等長期協議。看多者強調 AI 落地、商業成長與獲利，看空者擔心估值倍數、客戶集中、股票酬勞稀釋與政治風險。",
  [u"什麼是直接上市？和傳統 IPO 有什麼不同？", u"為什麼「上限 100 億美元」不等於 Palantir 會收到 100 億美元？", u"列出估值爭論中你認為最重要的一個看多與一個看空論點。"]),

lesson(u"Palantir Ontology 的架構：物件、屬性與連結",
  u"語意元素：把資料變成「名詞」",
  [u"理解物件類型、屬性、連結類型", u"理解資料集與物件的對應", u"比較 Palantir Ontology 與 OWL 的建模方式"],
  [("p", u"Palantir 的官方文件把 Ontology 的元素分為兩類：<strong>語意元素</strong>（semantic elements）——物件、屬性、連結；以及<strong>動能元素</strong>（kinetic elements）——動作、函數等（下一課）。"),
   ("h", u"語意元素"),
   ("t", [u"元素", u"說明", u"OWL 的近似對應"],
    [[u"<strong>物件類型</strong>（object type）", u"一種實體或事件的綱要，例如飛機、航班、工單、客戶。每個物件類型有一個<strong>主鍵</strong>，並由一個或多個資料集提供資料", u"類別（owl:Class）"],
     [u"<strong>物件</strong>（object）", u"物件類型的一個實例，對應資料集中的一列", u"個體"], [u"<strong>屬性</strong>（property）", u"物件的特徵，有型別（字串、數字、日期、地理位置、時間序列等）", u"資料屬性"],
     [u"<strong>連結類型</strong>（link type）", u"兩個物件類型之間的關係，有基數（一對一、一對多、多對多），例如「航班 由…執飛 飛機」", u"物件屬性"],
     [u"<strong>介面</strong>（interface）", u"多個物件類型共有的形狀，例如「可維修的資產」", u"上層類別（但更接近程式語言的介面）"]]),
   ("h", u"和 OWL 的建模差異"),
   ("ul", [u"<strong>封閉世界、資料驅動</strong>：物件就是資料集裡的列，沒有的就是沒有（第 29 課的 CWA）。", u"<strong>主鍵與型別嚴格</strong>：更像資料庫或程式語言的型別系統，而不是邏輯理論。", u"<strong>沒有描述邏輯推理</strong>：不會自動推論「有子女的人是父母」；需要的話用函數或資料管線計算。", u"<strong>面向應用</strong>：物件類型的設計以「使用者要在畫面上看到什麼、要做什麼決定」為準。"]),
   ("p", u"下面用 Python 寫一個<strong>極簡的模擬</strong>，幫助理解這些元素如何組合（這不是 Palantir 的程式碼）："),
   PY(u"""
# 極簡模擬：物件類型、屬性、連結類型、物件集合（概念示意，不是 Palantir 的 API）
from dataclasses import dataclass, field
import pandas as pd

@dataclass
class ObjectType:
    name: str
    primary_key: str
    backing: pd.DataFrame                       # 資料集：每一列 = 一個物件
    def get(self, pk):   return self.backing.set_index(self.primary_key).loc[pk].to_dict()
    def where(self, **kw):
        d = self.backing
        for k, v in kw.items(): d = d[d[k] == v]
        return d

@dataclass
class LinkType:
    name: str; source: ObjectType; target: ObjectType; fk: str     # 一對多：以外鍵實作
    def follow(self, src_pk):
        tgt = self.source.get(src_pk)[self.fk]
        return self.target.get(tgt)

aircraft = ObjectType("Aircraft", "tail", pd.DataFrame(
    {"tail": ["B-101", "B-102"], "type": ["A321", "A321"], "seats": [194, 194], "status": ["可用", "可用"]}))
flight = ObjectType("Flight", "flight_no", pd.DataFrame(
    {"flight_no": ["CI-301", "CI-512"], "dest": ["成田", "新加坡"], "pax": [182, 188], "tail": ["B-101", "B-102"]}))
operated_by = LinkType("operatedBy", flight, aircraft, fk="tail")

print(operated_by.follow("CI-301"))           # 沿著連結：CI-301 由哪架飛機執飛
print(flight.where(dest="成田"))               # 物件集合（object set）的篩選
"""),
   ("note", u"Ontology SDK", [("p", u"Palantir 提供 <strong>Ontology SDK</strong>（OSDK），會根據你的 Ontology 自動產生 TypeScript 或 Python 的型別化客戶端，讓外部應用以「物件」而不是「資料表」的方式存取資料。下一課會看到它的概念性寫法。")]),
  ],
  u"Palantir 官方文件將 Ontology 元素分為語意元素（物件、屬性、連結）與動能元素（動作、函數等）。物件類型有主鍵並由資料集支撐，物件對應資料列，屬性有嚴格型別，連結類型帶基數，介面描述共有形狀。和 OWL 相比，它採封閉世界、資料驅動、型別嚴格、不做描述邏輯推理、以應用為導向。OSDK 會依 Ontology 產生 TypeScript 或 Python 的型別化客戶端。",
  [u"Palantir 的物件類型和 OWL 的類別有什麼相同與不同？", u"為什麼說 Palantir Ontology 比較接近封閉世界？", u"為一間醫院設計三個物件類型與兩個連結類型。"]),

lesson(u"動作、函數與寫回",
  u"動能元素：把資料變成「動詞」",
  [u"理解動作類型的組成：參數、驗證規則、副作用", u"理解函數的用途", u"理解寫回與決策紀錄的意義"],
  [("p", u"傳統的資料平台和 BI 工具是<strong>唯讀</strong>的：你看儀表板、得出結論，然後到另一個系統去執行決策。Palantir Ontology 的關鍵設計，是把「能做的事」也放進 Ontology。"),
   ow("palantir", u"一個航空公司的模擬：回報故障、讓 AI 提出建議、由人核准後執行。也試著手動改派，看看驗證規則如何擋下不合理的操作。"),
   ("h", u"動作類型（action type）"),
   ("t", [u"組成", u"說明", u"模擬中的例子"],
    [[u"<strong>參數</strong>", u"執行動作需要的輸入", u"要改派的航班、目標飛機"], [u"<strong>驗證規則</strong>（提交條件）", u"什麼情況下允許執行；也包括誰有權限執行", u"飛機必須可用、座位數足夠、時段不衝突"],
     [u"<strong>規則／效果</strong>", u"對 Ontology 中的物件做什麼修改（新增、修改、刪除物件或連結）", u"把航班的「執飛飛機」連結改到新飛機"],
     [u"<strong>副作用</strong>", u"通知、呼叫外部系統（webhook）", u"通知機組、更新地勤排班"], [u"<strong>寫回</strong>", u"把修改同步回原始的營運系統", u"航班排程系統、維修系統開立工單"]]),
   ("h", u"函數（function）"),
   ("p", u"函數是寫在 Ontology 上的程式邏輯（Palantir 支援 TypeScript 與 Python），用來<strong>即時計算</strong>衍生的值或做複雜的判斷：受影響的旅客總數、某架飛機的風險分數、某個改派方案的成本。函數可以被應用畫面、動作的驗證規則、AI 代理人呼叫。"),
   PY(u"""
# 概念性寫法（偽程式碼）：用 Ontology SDK 以「物件」方式讀取並執行動作
# 實際的套件名稱與方法由平台依你的 Ontology 自動產生，以下僅示意其風格
from my_airline_sdk import FoundryClient            # 自動產生的客戶端（名稱示意）

client = FoundryClient()
flights = client.ontology.objects.Flight
affected = flights.where(flights.aircraft_tail == "B-101").take(10)

for f in affected:
    print(f.flight_no, f.departure_time, f.passenger_count)

# 呼叫一個「動作類型」：參數經過平台上的驗證規則檢查；通過才會修改物件並寫回
result = client.ontology.actions.reassign_aircraft(flight=affected[0], new_aircraft="B-104")
print(result)                                       # 驗證失敗時會回傳錯誤，而不是靜默修改資料
"""),
   ("h", u"為什麼「寫回」很重要"),
   ("ul", [u"<strong>閉環</strong>：分析與執行在同一個地方，不必在多個系統之間複製貼上。", u"<strong>決策也是資料</strong>：每一次動作都被記錄——誰、何時、根據什麼資料、做了什麼決定。這些紀錄本身成為可以分析的資料，組織可以從過去的決策中學習。", u"<strong>安全的自動化</strong>：AI 不能直接改資料庫，只能呼叫定義好的動作；動作有驗證規則與權限，就像給 AI 一組有護欄的工具（第 62 課）。"]),
   ("note", u"對照 OWL", [("p", u"OWL 本體描述「世界是什麼樣子」，本身沒有「動作」的概念。Palantir 把動作放進本體，讓它從知識表示走向<strong>營運系統</strong>。學術界也有描述服務與流程的本體（如 OWL-S），但沒有成為主流。")]),
  ],
  u"Palantir Ontology 把能做的事也放進本體。動作類型由參數、驗證規則與權限、對物件的修改、副作用與寫回組成；函數以 TypeScript 或 Python 即時計算衍生值，可供應用、驗證規則與 AI 呼叫。OSDK 讓外部程式以物件方式讀取並呼叫動作。寫回形成分析與執行的閉環，讓決策本身成為可分析的資料，並使 AI 只能透過有護欄的動作修改資料。",
  [u"一個動作類型由哪些部分組成？", u"在模擬中，為什麼把 CI-301 改派給 B-102 會失敗？", u"「決策也是資料」對組織有什麼價值？"]),

lesson(u"語意與動能：企業的數位孿生",
  u"名詞加上動詞，就是組織的作業系統",
  [u"整合語意元素與動能元素", u"理解「組織的數位孿生」的含義", u"理解治理與動態安全"],
  [("p", u"把前兩課合起來：<strong>語意元素</strong>（物件、屬性、連結）描述組織中有什麼、彼此怎麼關聯；<strong>動能元素</strong>（動作、函數）描述能做什麼、會發生什麼。兩者合起來，Palantir 稱之為組織的<strong>數位孿生</strong>——不只是機器與設備的孿生，而是訂單、人員、資產、決策的整體模型。"),
   ("t", [u"", u"語言學類比", u"Ontology 元素", u"例子"],
    [[u"語意", u"名詞", u"物件類型", u"飛機、航班、機場、工單、旅客"], [u"語意", u"形容詞", u"屬性", u"座位數、狀態、起飛時間"], [u"語意", u"介系詞與關係", u"連結類型", u"航班由飛機執飛、工單針對飛機"],
     [u"動能", u"動詞", u"動作類型", u"回報故障、改派飛機、核准工單"], [u"動能", u"推理與計算", u"函數", u"受影響旅客數、延誤成本"]]),
   ("h", u"一個完整的決策迴圈"),
   ("ol", [u"<strong>感知</strong>：資料管線把維修系統的新故障紀錄同步進來，B-101 的狀態變成「停飛」。", u"<strong>理解</strong>：函數算出 CI-301、CI-305 受影響，共 342 名旅客。", u"<strong>決策</strong>：調度員（或 AI 代理人）比較幾個改派方案的成本與風險。", u"<strong>行動</strong>：透過動作類型執行改派，驗證規則確保方案可行。", u"<strong>寫回與紀錄</strong>：排程系統更新、通知發出，整個決策過程被記錄下來。", u"<strong>學習</strong>：累積的決策紀錄用來評估與改進未來的決策（包括訓練模型）。"]),
   ("h", u"治理與動態安全"),
   ("p", u"當 Ontology 成為全組織的作業系統，安全就必須做在 Ontology 層，而不是每個應用各自處理："),
   ("ul", [u"<strong>物件與屬性層級的權限</strong>：同一個「員工」物件，人資看得到薪資，主管只看得到職稱。", u"<strong>標記</strong>：資料帶有分類標記（例如個資、機密），標記會沿著資料管線傳遞到衍生的資料與物件。", u"<strong>動作權限</strong>：誰可以執行哪些動作、在什麼條件下。", u"<strong>稽核</strong>：每一次讀取與動作都留下紀錄。"]),
   ("p", u"Palantir 的文件把這類能力稱為動能元素中的「動態安全」（dynamic security）。"),
   PY(u"""
# 概念示意：屬性層級權限 + 標記傳遞（不是 Palantir 的 API）
EMPLOYEE = {"id": "E17", "name": "林小芳", "title": "工程師", "salary": 96000, "national_id": "A2********"}
MARKINGS = {"salary": {"HR"}, "national_id": {"HR", "PII"}}       # 需要的權限標記

def view(obj, user_groups):
    return {k: (v if MARKINGS.get(k, set()) <= user_groups else "▇▇▇") for k, v in obj.items()}

print(view(EMPLOYEE, {"Manager"}))             # 主管：看不到薪資與身分證號
print(view(EMPLOYEE, {"HR", "PII"}))            # 人資：全部可見

# 標記傳遞：由含 PII 的欄位計算出的衍生欄位，也會繼承 PII 標記
def derive(field, sources):
    MARKINGS[field] = set().union(*(MARKINGS.get(s, set()) for s in sources))
derive("salary_band", ["salary"]);  print(MARKINGS["salary_band"])   # {'HR'}
"""),
  ],
  u"語意元素描述組織中有什麼與如何關聯，動能元素描述能做什麼與會發生什麼，合起來即 Palantir 所稱組織的數位孿生，可類比名詞、形容詞、關係與動詞。完整的決策迴圈包括感知、理解、決策、行動、寫回紀錄與學習。安全必須做在 Ontology 層：物件與屬性權限、沿管線傳遞的標記、動作權限與稽核，官方文件稱之為動態安全。",
  [u"用名詞、形容詞、動詞的類比，描述一間便利商店的 Ontology。", u"為什麼安全控制要做在 Ontology 層，而不是每個應用自己處理？", u"什麼是標記傳遞？為什麼重要？"]),

lesson(u"AIP：讓 AI 在 Ontology 上工作",
  u"大型語言模型 + 物件 + 動作 + 人類核准",
  [u"理解 AIP 的架構與設計理念", u"理解 AI 代理人以動作為工具的模式", u"認識 AIP 訓練營的推廣方式"],
  [("p", u"2023 年，Palantir 推出 <strong>AIP</strong>（Artificial Intelligence Platform）。它的核心論點是：大型語言模型本身不知道你的企業，也不應該直接存取你的資料庫；但如果讓它在 <strong>Ontology</strong> 上工作，它就能理解業務概念、查詢正確的資料、並透過受控的動作採取行動。"),
   ("h", u"AIP 的組成（簡化）"),
   ("t", [u"元件", u"作用"],
    [[u"模型接入", u"接入多家廠商的大型語言模型，以及客戶自己的模型"], [u"AIP Logic", u"用低程式碼方式組合 LLM、Ontology 查詢、函數與動作，建立 AI 功能"],
     [u"代理人（AIP Agent Studio 等）", u"建立能多步驟推理、呼叫工具的 AI 代理人"], [u"Ontology 作為工具", u"物件查詢、函數、動作都可以作為 LLM 的工具"],
     [u"安全與稽核", u"AI 只能看到使用者有權限看到的資料；每次呼叫都有紀錄"], [u"評估", u"對 AI 功能建立測試案例並評估表現"]]),
   ("h", u"關鍵設計：AI 提建議，人做決定"),
   ("p", u"在剛才的模擬中，「② AIP 產生建議」只是<strong>建議</strong>；要按「③ 核准」才會真正執行動作。這種「人在迴圈中」（human-in-the-loop）的設計，是在高風險場景（航空、醫療、國防）使用 AI 的關鍵。隨著信心累積，部分低風險動作可以逐步改為自動執行。"),
   PY(u"""
# 以「Ontology 動作」作為 Claude 的工具；AI 只能提出動作，由人核准後才執行
import anthropic, json

def affected_flights(tail):                  # 函數（唯讀）
    return [{"flight": "CI-301", "pax": 182, "time": "08:30"}, {"flight": "CI-305", "pax": 160, "time": "14:10"}]
def available_aircraft(min_seats):           # 函數（唯讀）
    return [{"tail": "B-104", "seats": 194}, {"tail": "B-103", "seats": 307}]

tools = [
  {"name": "affected_flights", "description": "列出由某架飛機執飛的航班",
   "input_schema": {"type": "object", "properties": {"tail": {"type": "string"}}, "required": ["tail"]}},
  {"name": "available_aircraft", "description": "列出可用且座位數不少於 min_seats 的飛機",
   "input_schema": {"type": "object", "properties": {"min_seats": {"type": "integer"}}, "required": ["min_seats"]}},
  {"name": "propose_reassignment", "description": "提出改派方案（不會立即執行，需人工核准）",
   "input_schema": {"type": "object", "properties": {"flight": {"type": "string"}, "tail": {"type": "string"}},
                    "required": ["flight", "tail"]}},
]
READ_ONLY = {"affected_flights": affected_flights, "available_aircraft": available_aircraft}
proposals = []

MODEL = "claude-..."                         # 填入目前可用的 Claude 模型名稱
client = anthropic.Anthropic()
messages = [{"role": "user", "content": "B-101 停飛維修，請為受影響的航班提出改派方案。"}]
while True:
    msg = client.messages.create(model=MODEL, max_tokens=2048, tools=tools, messages=messages)
    messages.append({"role": "assistant", "content": msg.content})
    if msg.stop_reason != "tool_use":
        break
    results = []
    for b in msg.content:
        if b.type != "tool_use":
            continue
        if b.name in READ_ONLY:
            out = READ_ONLY[b.name](**b.input)
        else:                                 # 寫入類動作：只記錄為提案
            proposals.append(b.input); out = {"status": "pending_human_approval"}
        results.append({"type": "tool_result", "tool_use_id": b.id, "content": json.dumps(out, ensure_ascii=False)})
    messages.append({"role": "user", "content": results})

for p in proposals:                           # 人類核准後，才透過有驗證規則的動作真正執行
    if input(f"核准 {p['flight']} 改由 {p['tail']} 執飛？(y/n) ") == "y":
        print("執行動作 reassign_aircraft", p)
"""),
   ("h", u"AIP 訓練營"),
   ("p", u"Palantir 推廣 AIP 的方式也很特別：<strong>訓練營</strong>（bootcamp）。客戶帶著自己的資料與問題，和 Palantir 工程師在一到數天內直接做出可用的 AI 應用。這取代了傳統漫長的試點與銷售流程，也是 2023 年後美國商業客戶快速成長的重要原因之一。"),
   ("note", u"給學習者的啟示", [("p", u"不論是否使用 Palantir，「LLM + 明確的本體 + 受控的動作 + 人類核准 + 完整稽核」這個架構，已經是企業 AI 代理人設計的通用模式。第 52 課的 GraphRAG 與本課的動作工具，分別對應「讓 AI 讀懂」與「讓 AI 安全地做事」。")]),
  ],
  u"AIP 於 2023 年推出，核心論點是讓 LLM 在 Ontology 上工作，以理解業務概念、查詢正確資料並透過受控動作行動。組成包括多模型接入、AIP Logic、代理人、以 Ontology 作為工具、安全稽核與評估。關鍵設計是 AI 提建議、人核准後執行，低風險動作再逐步自動化。AIP 訓練營讓客戶在數天內做出應用，帶動美國商業成長。LLM、本體、受控動作、人類核准與稽核已成企業 AI 代理人的通用模式。",
  [u"為什麼 LLM 不應該直接存取企業的資料庫？", u"在上面的程式中，唯讀函數和寫入動作的處理方式有什麼不同？", u"AIP 訓練營和傳統的軟體銷售流程有什麼不同？"]),

lesson(u"案例：國防、醫療、製造與危機應變",
  u"Ontology 在真實世界中的運作",
  [u"認識 Palantir 在不同領域的代表案例", u"從案例中辨認物件、連結與動作", u"思考這些案例帶來的爭議"],
  [("p", u"以下案例依公開報導整理，重點放在「Ontology 解決了什麼整合問題」。"),
   ("h", u"美國陸軍"),
   ("ul", [u"2016 年 Palantir 控告陸軍的情報系統（DCGS-A）採購程序未考慮商用現成產品並勝訴，之後逐步取得陸軍合約。", u"<strong>Army Vantage</strong>：整合人員、裝備、戰備、財務資料，供陸軍各級指揮官決策。", u"2024 年取得 TITAN（新一代情報地面站）原型合約；同年 Maven Smart System（以 AI 整合多來源情資的系統）合約擴大。", u"2025 年 7 月陸軍宣布企業協議：整合 75 份合約，10 年、上限 100 億美元，目的在減少重複採購、加速取得軟體。"]),
   ("h", u"英國 NHS"),
   ("p", u"2023 年 11 月，英國國民保健署（NHS England）把<strong>聯邦資料平台</strong>（Federated Data Platform）合約授予以 Palantir 為首的團隊。目標是讓各醫院整合病床、手術排程、候診名單、出院流程等資料，縮短候診時間。這個合約在英國引發強烈的隱私與信任討論，NHS 強調資料仍由各醫院控制、Palantir 不擁有資料。"),
   ("h", u"製造與供應鏈"),
   ("ul", [u"<strong>航空</strong>：空中巴士 2017 年推出以 Foundry 為基礎的 Skywise 平台，整合生產與機隊營運資料，並開放給航空公司使用。", u"<strong>供應鏈</strong>：把供應商、零件、工廠、訂單、物流建成 Ontology，當某個供應商出問題時，立即算出受影響的產品與客戶訂單，並以動作調整採購或排程。"]),
   ("h", u"新冠疫情"),
   ("p", u"2020 年，美國衛生及公共服務部（HHS）使用 Palantir 建立 <strong>HHS Protect</strong> 平台，整合醫院容量、檢測、病例等資料；疫苗分配追蹤系統 <strong>Tiberius</strong> 協助規劃疫苗配送。英國 NHS 在疫情期間也使用 Foundry 建立資料平台。"),
   ("h", u"烏克蘭"),
   ("p", u"2022 年俄烏戰爭爆發後，Palantir 的軟體被用於烏克蘭的戰場情資整合；公開報導也提到用於記錄戰爭罪證據、規劃排雷等工作。這讓 Palantir 成為「軟體定義戰爭」討論的焦點。"),
   PY(u"""
# 供應鏈影響分析：沿著 Ontology 的連結找出某供應商出問題時受影響的客戶訂單
import networkx as nx

G = nx.DiGraph()
G.add_edges_from([
    ("供應商：甲電子", "零件：電源模組"), ("供應商：乙化工", "零件：外殼"),
    ("零件：電源模組", "產品：工業電腦 X1"), ("零件：電源模組", "產品：伺服器 S5"),
    ("零件：外殼", "產品：工業電腦 X1"),
    ("產品：工業電腦 X1", "訂單：O-1001"), ("產品：伺服器 S5", "訂單：O-1002"), ("產品：伺服器 S5", "訂單：O-1003"),
])
hit = nx.descendants(G, "供應商：甲電子")
print("受影響訂單：", sorted(n for n in hit if n.startswith("訂單")))
# 下一步：對每張受影響訂單呼叫「調整交期」或「改用替代料」的動作，並由採購主管核准
"""),
   ("note", u"從案例看到的共同模式", [("ol", [u"資料散落在大量既有系統中，沒有人看得到全貌。", u"建立 Ontology，把資料對應到共同的物件與連結。", u"在 Ontology 上建立應用與動作，讓第一線人員能直接做決定。", u"每個案例都伴隨著對隱私、權力與問責的質疑（下一課）。"])]),
  ],
  u"美國陸軍案例包括 2016 年 DCGS-A 訴訟勝訴、Army Vantage、2024 年 TITAN 與 Maven 合約，以及 2025 年 10 年上限 100 億美元的企業協議。英國 NHS 2023 年授予聯邦資料平台合約，以縮短候診，但引發隱私討論。製造業有空中巴士的 Skywise 與供應鏈影響分析；疫情期間有 HHS Protect 與 Tiberius；俄烏戰爭中用於情資整合與排雷。共同模式是整合散落資料、建立 Ontology、以應用與動作支援第一線決策，並伴隨問責爭議。",
  [u"NHS 聯邦資料平台要解決什麼問題？為什麼引起爭議？", u"在供應鏈案例中，物件類型、連結類型和動作各是什麼？", u"這些案例的共同模式是什麼？"]),

lesson(u"爭議與倫理",
  u"誰在使用這些工具？用來做什麼？誰來監督？",
  [u"認識圍繞 Palantir 的主要爭議", u"理解各方的論點", u"思考資料整合技術的倫理問題"],
  [("p", u"Palantir 可能是全世界最具爭議的軟體公司之一。理解這些爭議，有助於思考任何強大的資料整合技術——包括你可能親手建立的知識圖譜——所帶來的責任。"),
   ("h", u"主要爭議"),
   ("t", [u"議題", u"事件", u"批評", u"公司與支持者的回應"],
    [[u"<strong>移民執法</strong>", u"自 2014 年起為美國移民及海關執法局（ICE）提供調查案件管理系統；2025 年媒體報導 ICE 委託開發新系統", u"協助大規模驅逐與家庭分離，員工與人權團體多次抗議", u"服務的是依法運作的政府機關；政策由民選政府決定"],
     [u"<strong>預測性警務</strong>", u"2018 年媒體揭露與紐奧良警方合作多年，市議會等並不知情", u"缺乏透明與民主監督，可能強化對特定社區的偏見", u"合作後來終止；強調工具本身不做「預測」判斷"],
     [u"<strong>隱私與醫療資料</strong>", u"英國 NHS 聯邦資料平台", u"擔心病人資料被商業公司掌握、信任受損", u"資料由 NHS 控制，平台有細粒度權限與稽核"],
     [u"<strong>AI 軍事化</strong>", u"Maven、TITAN、烏克蘭戰場", u"AI 加速殺傷鏈，降低戰爭門檻，問責不清", u"民主國家必須擁有最好的技術，否則讓給對手"],
     [u"<strong>權力集中</strong>", u"同一家公司深入國防、情報、醫療、執法", u"單一私人公司掌握過多關鍵基礎設施", u"軟體可以被稽核，並受合約與法律約束"]]),
   ("h", u"卡普的立場：《科技共和國》"),
   ("p", u"2025 年，卡普與尼古拉斯・札米斯卡出版《科技共和國》（The Technological Republic）。核心主張是：矽谷曾經與國家緊密合作（從二戰到太空計畫），後來卻轉向消費性應用與廣告；西方民主國家需要科技菁英重新投入國防與公共事務，否則將在 AI 時代輸給威權國家。批評者則認為這是在為國防承包商的商業利益包裝意識形態。"),
   ("h", u"從技術角度思考倫理"),
   ("ul", [u"<strong>整合本身就是力量</strong>：分開來無害的資料，連起來就可能識別、追蹤一個人。本體越好，這個力量越大。", u"<strong>設計中的價值</strong>：一個系統把什麼東西建模成物件、哪些關係可以被查詢、哪些動作可以被執行，都是價值選擇。", u"<strong>技術性護欄</strong>：細粒度權限、目的限制、稽核紀錄、資料保存期限、人類核准——這些都可以寫進本體與動作的設計中。", u"<strong>技術性護欄不足以取代制度</strong>：誰能看稽核紀錄？誰決定什麼是合法目的？這些需要法律、監督機關與公眾參與。"]),
   PY(u"""
# 用 Python 檢查一份 Ontology 設計是否內建了基本的倫理護欄（自我檢查清單的示意）
design = {
    "objects": {"Person": {"pii": True, "retention_days": None}, "Case": {"pii": True, "retention_days": 1825}},
    "actions": {"flag_person": {"human_approval": False, "audit": True, "purpose_required": False}},
}
issues = []
for name, o in design["objects"].items():
    if o["pii"] and o["retention_days"] is None:
        issues.append(f"物件 {name} 含個資但沒有保存期限")
for name, a in design["actions"].items():
    if not a["human_approval"]: issues.append(f"動作 {name} 影響個人卻不需要人工核准")
    if not a["purpose_required"]: issues.append(f"動作 {name} 沒有要求填寫使用目的")
    if not a["audit"]: issues.append(f"動作 {name} 沒有稽核紀錄")
print("\\n".join(issues) or "通過基本檢查")
"""),
   ("note", u"開放討論", [("p", u"本課刻意呈現多方論點，而非下結論。值得思考的問題是：如果你是一位知識圖譜工程師，被要求為某個用途建立 Ontology，你會在什麼情況下拒絕？你會要求哪些護欄？")]),
  ],
  u"Palantir 的爭議包括：自 2014 年起支援 ICE 的移民執法、2018 年揭露與紐奧良警方的預測性警務合作、NHS 醫療資料隱私、Maven 與 TITAN 等 AI 軍事化，以及私人公司掌握關鍵基礎設施的權力集中，公司則以合法政府、權限稽核與民主國家需要技術回應。卡普 2025 年的《科技共和國》主張科技菁英重返國防。技術倫理上，整合即力量、設計即價值，權限、目的限制、稽核、保存期限與人類核准等護欄可寫入設計，但仍需制度監督。",
  [u"為什麼「分開來無害的資料，連起來可能有害」？舉一個例子。", u"《科技共和國》的核心主張是什麼？你同意嗎？", u"列出三種可以直接寫進 Ontology 設計中的倫理護欄。"]),
]),

(u"模組 K｜總結", [

lesson(u"哲學的老問題，在 AI 時代的新答案",
  u"從亞里斯多德到 AI 代理人：「存在的是什麼」為什麼仍然重要",
  [u"串起整門課的主線", u"理解本體在 AI 時代的價值", u"規劃下一步的學習與實作"],
  [("p", u"兩千多年前，亞里斯多德問：「存在的東西有哪些種類？」今天，企業在導入 AI 時問的問題驚人地相似：「我們的業務裡有哪些東西？它們之間是什麼關係？我們可以對它們做什麼？」"),
   ("h", u"一條貫穿的主線"),
   ("t", [u"時代", u"問題", u"答案的形式"],
    [[u"古希臘", u"存在的是什麼？如何分類？", u"範疇、屬加種差、波菲利之樹"], [u"中世紀到近代", u"共相存在嗎？概念如何組合？", u"實在論與唯名論、萊布尼茲的通用文字"],
     [u"20 世紀", u"如何讓機器表示知識？", u"一階邏輯、語意網路、框架、專家系統"], [u"1990～2000 年代", u"如何共享與推理？", u"格魯伯的定義、描述邏輯、OWL、語意網"],
     [u"2010 年代", u"如何整合海量資料？", u"知識圖譜、Wikidata、schema.org、企業本體"], [u"2020 年代", u"如何讓 AI 可靠地理解與行動？", u"GraphRAG、語意層、Palantir 式的物件 + 動作 + AI"]]),
   ("h", u"為什麼 LLM 沒有讓本體過時"),
   ("ul", [u"<strong>LLM 懂語言，不懂你的組織</strong>：「客戶」在你的公司裡精確指的是什麼，只有你的本體知道。", u"<strong>可驗證</strong>：本體讓 AI 的輸出可以被檢查（SHACL、型別、驗證規則）。", u"<strong>可追溯</strong>：答案能指回具體的物件與資料來源。", u"<strong>可控制</strong>：AI 透過定義好的動作行事，而不是任意修改系統。", u"<strong>反過來，LLM 讓本體更容易建</strong>：知識擷取、對齊、文件撰寫的成本大幅下降（第 53 課）。"]),
   ("p", u"符號主義與連結主義的長期爭論，在這裡找到了一種分工：<strong>神經網路負責感知與語言，本體負責結構、約束與行動</strong>。這種結合常被稱為神經符號（neuro-symbolic）AI。"),
   ("h", u"下一步：一個實作專案"),
   ("ol", [u"選一個你熟悉的小領域（社團、家庭收支、課程、店鋪）。", u"寫 5～10 個能力問題（第 46 課）。", u"用 rdflib 或 owlready2 建立本體與測試資料，重用 schema.org 或 SKOS。", u"用推理機檢查一致性，用 SHACL 驗證資料，用 SPARQL 回答能力問題。", u"加上「動作」：寫幾個會修改資料、帶有驗證規則的 Python 函式。", u"最後接上 LLM：讓它根據本體回答問題、提出動作建議，由你核准。"]),
   PY(u"""
# 最小的「本體 + 動作 + 驗證」骨架：你的實作專案可以從這裡開始
from rdflib import Graph, Namespace, Literal, RDF
from pyshacl import validate

EX = Namespace("http://example.org/club#")
g = Graph().parse(data='''
@prefix : <http://example.org/club#> .
:Alice a :Member ; :name "Alice" .
:Chess a :Activity ; :capacity 2 .
''', format="turtle")

shapes = Graph().parse(data='''
@prefix sh: <http://www.w3.org/ns/shacl#> . @prefix : <http://example.org/club#> .
:ActivityShape a sh:NodeShape ; sh:targetClass :Activity ;
  sh:property [ sh:path :participant ; sh:class :Member ] .
''', format="turtle")

def action_join(member, activity):
    \"\"\"動作：報名活動。先檢查前提，再修改，再驗證；失敗就回復。\"\"\"
    cap = int(g.value(activity, EX.capacity))
    if len(list(g.objects(activity, EX.participant))) >= cap:
        return "拒絕：名額已滿"
    g.add((activity, EX.participant, member))
    ok, _, report = validate(g, shacl_graph=shapes)
    if not ok:
        g.remove((activity, EX.participant, member)); return "拒絕：" + report
    return "完成"

print(action_join(EX.Alice, EX.Chess))     # 完成
print(action_join(EX.Bob, EX.Chess))       # 拒絕：Bob 不是 Member（SHACL 驗證失敗）
"""),
   ("note", u"結語", [("p", u"Ontology 從來不只是技術。它是一種思考方式：在動手之前，先問清楚「這裡有什麼、它們是什麼關係、我們能做什麼、什麼不該做」。這個問題，亞里斯多德問過，萊布尼茲問過，格魯伯問過，今天的 AI 工程師也必須回答。")]),
  ],
  u"從亞里斯多德的範疇到企業 AI，本體始終在回答「存在什麼、如何關聯、能做什麼」：古希臘的分類、中世紀的共相之爭、20 世紀的知識表示、OWL 與語意網、知識圖譜，到 GraphRAG 與 Palantir 式的物件加動作。LLM 沒有讓本體過時，因為本體提供組織專屬的語意、可驗證、可追溯與可控制，而 LLM 反過來降低建構成本，形成神經符號的分工。下一步可從能力問題出發，建立含推理、SHACL、SPARQL、動作與 LLM 的小專案。",
  [u"用你自己的話說明：為什麼 LLM 時代反而更需要本體？", u"亞里斯多德的「範疇」和 Palantir 的「物件類型」有什麼相似之處？", u"為你的實作專案寫下五個能力問題。"]),
]),
]
