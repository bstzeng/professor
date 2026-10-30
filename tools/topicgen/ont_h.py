# -*- coding: utf-8 -*-
"""Ontology：模組 H Ontology 工程方法（46～50）、I 現代應用（51～54）。"""
from ont_common import *

MODULES = [
(u"模組 H｜Ontology 工程方法", [

lesson(u"方法論與能力問題",
  u"從需求出發：本體要回答哪些問題？",
  [u"認識主要的本體工程方法論", u"會寫能力問題並轉成 SPARQL 測試", u"理解本體開發的生命週期"],
  [("p", u"建本體和寫軟體一樣，需要方法。最常見的失敗是：一開始就畫一棵大樹，想把「所有東西」都放進去，結果做了兩年沒人用。"),
   ("h", u"主要方法論"),
   ("t", [u"方法論", u"年代", u"特點"],
    [[u"<strong>Ontology 101</strong>（諾伊與麥吉尼斯，史丹佛）", u"2001", u"七步驟入門指南：決定範圍 → 考慮重用 → 列術語 → 定類別階層 → 定屬性 → 定屬性限制 → 建個體"],
     [u"<strong>METHONTOLOGY</strong>（馬德里理工大學）", u"1997", u"借用軟體工程：規格、概念化、形式化、實作、維護，加上評估與文件"],
     [u"<strong>NeOn</strong>", u"2010 前後", u"九種情境，強調重用既有本體、非本體資源（資料庫綱要、詞彙表）"],
     [u"<strong>敏捷方法</strong>（如 XD 極限設計、SAMOD）", u"2010 年代", u"小步快跑：一次處理幾個能力問題，以測試驅動開發"]]),
   ("h", u"能力問題（Competency Questions）"),
   ("p", u"格魯寧格與福克斯在 1995 年提出：本體的需求，就是它<strong>必須能回答的問題</strong>。例如一個圖書館本體："),
   ("ol", [u"某位作者寫過哪些書？", u"目前有哪些書逾期未還？逾期的讀者是誰？", u"某本書屬於哪些主題（含上層主題）？", u"哪些書有中譯本？譯者是誰？"]),
   ("p", u"能力問題決定了範圍（不在任何問題裡的概念可以先不做），也是最好的<strong>驗收測試</strong>：每個問題寫成一個 SPARQL 查詢，本體與測試資料要能給出預期答案。"),
   PY(u"""
# 把能力問題寫成自動化測試（pytest），每次修改本體都跑一次
import pytest
from rdflib import Graph
import owlrl

@pytest.fixture(scope="module")
def kg():
    g = Graph().parse("library.ttl").parse("test_data.ttl")
    owlrl.DeductiveClosure(owlrl.OWLRL_Semantics).expand(g)   # 先物化推論結果
    return g

CQS = {
    "CQ1 托爾金寫過哪些書": ('''SELECT ?b WHERE { ?b :writtenBy :Tolkien }''', {":LOTR", ":Hobbit"}),
    "CQ3 魔戒的所有主題（含上層）": ('''SELECT ?t WHERE { :LOTR :subject/skos:broader* ?t }''',
                                {":Fantasy", ":Fiction", ":Literature"}),
}

@pytest.mark.parametrize("name", CQS)
def test_competency_question(kg, name):
    q, expected = CQS[name]
    ns = {"": "http://example.org/lib#", "skos": "http://www.w3.org/2004/02/skos/core#"}
    got = {kg.qname(r[0]) for r in kg.query(q, initNs=ns)}
    assert got == expected, name
"""),
   ("h", u"生命週期"),
   ("ol", [u"<strong>規格</strong>：目的、範圍、使用者、能力問題。", u"<strong>知識擷取</strong>：訪談領域專家、讀文件、分析既有資料庫。", u"<strong>概念化</strong>：列出術語，區分類別、屬性、個體。", u"<strong>重用</strong>：找可以引用的現有本體（第 48 課）。", u"<strong>形式化與實作</strong>：用 OWL 寫下來（第 47 課的 Protégé）。", u"<strong>評估</strong>：推理機檢查一致性、跑能力問題測試、專家審查（第 50 課）。", u"<strong>部署與維護</strong>：版本控制、變更管理（第 49 課）。"]),
  ],
  u"本體工程需要方法，避免想涵蓋一切卻無人使用。主要方法論有七步驟的 Ontology 101、借用軟體工程的 METHONTOLOGY、強調重用的 NeOn 與測試驅動的敏捷方法。能力問題是本體必須回答的問題，決定範圍，也可寫成 SPARQL 自動化測試作為驗收。生命週期包括規格、知識擷取、概念化、重用、形式化、評估與維護。",
  [u"為一個「醫院排班」本體寫出五個能力問題。", u"為什麼能力問題能幫助控制本體的範圍？", u"把能力問題寫成自動化測試有什麼好處？"]),

lesson(u"Protégé 與 Python 工具鏈",
  u"圖形化編輯、推理、程式化處理",
  [u"認識 Protégé 的主要功能", u"認識 Python 的本體工具", u"建立一套可自動化的工作流程"],
  [("p", u"<strong>Protégé</strong> 是史丹佛大學開發的免費開源本體編輯器（最早可追溯到 1980 年代），是全世界最多人使用的 OWL 工具。"),
   ("h", u"Protégé 的主要畫面"),
   ("t", [u"分頁", u"用途"],
    [[u"Entities → Classes", u"建立類別階層；在右側用 Manchester 語法寫等價類別、上層類別、互斥"], [u"Object / Data Properties", u"建立屬性，勾選傳遞、對稱、函數性，設定定義域與值域"],
     [u"Individuals", u"建立個體與屬性值"], [u"Reasoner 選單", u"選擇 HermiT、Pellet、ELK，執行分類；推論出的階層以黃色顯示"],
     [u"DL Query", u"輸入類別運算式，查詢它的子類別與實例"], [u"Explanation", u"點一個推論結果的問號，看是哪些公理推出來的（除錯不一致時非常重要）"]]),
   ("p", u"另有網頁版 WebProtégé，適合多人協作編輯。"),
   ("h", u"Python 工具"),
   ("t", [u"套件", u"用途"],
    [[u"<strong>rdflib</strong>", u"RDF 圖的讀寫、SPARQL 查詢、序列化"], [u"<strong>owlready2</strong>", u"把 OWL 類別與個體對應成 Python 物件；內建 HermiT 與 Pellet"],
     [u"<strong>owlrl</strong>", u"在 rdflib 圖上做 RDFS 與 OWL 2 RL 的規則推理"], [u"<strong>pySHACL</strong>", u"SHACL 驗證"], [u"<strong>pronto</strong>", u"讀取 OBO 格式（生物醫學本體）"],
     [u"<strong>SPARQLWrapper</strong>", u"查詢遠端 SPARQL 端點"], [u"<strong>morph-kgc</strong>", u"用 RML 對應規則把 CSV、資料庫轉成 RDF"], [u"<strong>py-horned-owl</strong>、<strong>ROBOT</strong>（Java）", u"大型本體的處理與自動化建置"]]),
   PY(u"""
# owlready2：本體像 Python 物件一樣操作
from owlready2 import get_ontology, sync_reasoner, default_world

onto = get_ontology("file://library.owl").load()

print(list(onto.classes()))                   # 所有類別
print(onto.Novel.is_a)                        # 上層類別與限制
print(onto.search(label="*Tolkien*"))         # 依標籤搜尋

with onto:
    sync_reasoner()                           # HermiT：一致性檢查 + 分類
print(list(default_world.inconsistent_classes()))   # 不可滿足的類別（應為空）

# 也可以直接用 SPARQL 查 owlready2 的資料庫
print(list(default_world.sparql("SELECT ?b WHERE { ?b a <http://example.org/lib#Novel> }")))
"""),
   ("h", u"把本體當成程式碼管理"),
   ("ul", [u"本體檔（Turtle 較適合 diff）放進 <strong>Git</strong>。", u"每次提交時，<strong>CI</strong> 自動執行：推理機一致性檢查、SHACL 驗證、能力問題測試、命名規則檢查。", u"用 ROBOT 或腳本自動產生發布版本與文件（例如 Widoco、pyLODE 產生 HTML 說明頁）。", u"OBO 社群的 <strong>ODK</strong>（Ontology Development Kit）把這套流程包成標準範本。"]),
  ],
  u"Protégé 是史丹佛開發的免費 OWL 編輯器，提供類別、屬性、個體編輯，推理機分類、DL Query 與推論解釋，另有網頁版協作。Python 工具包括 rdflib、owlready2、owlrl、pySHACL、pronto、SPARQLWrapper、morph-kgc 等。實務上應將本體當成程式碼管理：Git 版控，CI 自動做一致性檢查、SHACL 驗證與能力問題測試，並自動產生發布版本與文件。",
  [u"Protégé 的 Explanation 功能為什麼對除錯很重要？", u"rdflib 和 owlready2 的定位有什麼不同？", u"設計一條本體專案的 CI 流程，至少包含哪些檢查？"]),

lesson(u"設計模式與重用",
  u"不要從零開始：本體設計模式與常用詞彙",
  [u"認識本體設計模式", u"認識應該優先重用的常用詞彙", u"理解重用的方式與取捨"],
  [("p", u"軟體工程有設計模式；本體工程也有。<strong>本體設計模式</strong>（ODP）是針對反覆出現的建模問題、經過驗證的小型解法。"),
   ("h", u"常見的設計模式"),
   ("t", [u"模式", u"解決的問題", u"做法"],
    [[u"<strong>N 元關係</strong>", u"RDF 只有二元關係，「張三於 2020～2023 年在甲公司擔任經理」怎麼表示？", u"把關係變成一個個體（任職），再連到人、公司、職位、起訖時間"],
     [u"<strong>部分–整體</strong>", u"部件、成員、區域包含各有不同性質", u"分開定義 hasPart、hasMember、containedIn，並各自設定傳遞性"],
     [u"<strong>角色</strong>", u"病人、員工是暫時的", u"角色是依存於人的個體，有起訖時間（第 25、39 課）"],
     [u"<strong>值分割</strong>", u"「尺寸」只能是小中大", u"用列舉類別 owl:oneOf 或 SKOS 概念"],
     [u"<strong>情境</strong>（Situation）", u"一個事件涉及多個參與者與角色", u"把情境當作個體，連到各參與者"],
     [u"<strong>出處</strong>", u"這筆資料從哪來", u"使用 PROV-O：Entity、Activity、Agent"]]),
   PY(u"""
# N 元關係模式：任職（Employment）
from rdflib import Graph, Namespace, Literal, RDF
from rdflib.namespace import XSD
EX = Namespace("http://example.org/hr#")
g = Graph()

job = EX.employment_42                       # 把「關係」變成一個個體
g.add((job, RDF.type, EX.Employment))
g.add((job, EX.employee, EX.ZhangSan))
g.add((job, EX.employer, EX.CompanyA))
g.add((job, EX.role, EX.Manager))
g.add((job, EX.start, Literal("2020-03-01", datatype=XSD.date)))
g.add((job, EX.end,   Literal("2023-06-30", datatype=XSD.date)))

q = '''SELECT ?who ?org WHERE {
  ?j a :Employment ; :employee ?who ; :employer ?org ; :start ?s ; :end ?e .
  FILTER(?s <= "2022-01-01"^^xsd:date && ?e >= "2022-01-01"^^xsd:date) }'''
print(list(g.query(q, initNs={"": EX, "xsd": XSD})))      # 2022 年初誰在哪裡工作
"""),
   ("h", u"應該優先重用的詞彙"),
   ("t", [u"詞彙", u"領域"],
    [[u"Dublin Core（dcterms）", u"標題、作者、日期、主題等詮釋資料"], [u"FOAF", u"人與社群關係"], [u"SKOS", u"分類表、詞彙表、主題詞（broader、narrower、related）"],
     [u"schema.org", u"一般網路實體"], [u"PROV-O", u"資料出處"], [u"OWL-Time", u"時間點、時間區間"], [u"GeoSPARQL", u"地理空間"], [u"QUDT", u"量與單位"], [u"ORG", u"組織結構"]]),
   ("h", u"重用的方式"),
   ("ul", [u"<strong>直接引用 IRI</strong>：最輕量，例如在你的資料中使用 dcterms:title。", u"<strong>owl:imports 整個本體</strong>：完整，但可能帶進大量不需要的東西。", u"<strong>模組抽取</strong>（如 MIREOT、SLME）：只抽出需要的類別及其上層，ROBOT extract 可以自動化。", u"<strong>對齊</strong>：自己定義，再用 subClassOf 或 equivalentClass 對應到標準詞彙（第 49 課）。"]),
  ],
  u"本體設計模式是反覆出現的建模問題的驗證解法，例如 N 元關係（將關係個體化）、部分整體、角色、值分割、情境與出處。應優先重用 Dublin Core、FOAF、SKOS、schema.org、PROV-O、OWL-Time、GeoSPARQL、QUDT、ORG 等詞彙。重用方式包括直接引用 IRI、owl:imports、模組抽取與對齊，各有完整度與複雜度的取捨。",
  [u"用 N 元關係模式表示「病人在某日服用某藥物 500 毫克」。", u"什麼情況下應該用 SKOS 而不是 OWL 類別？", u"直接 import 一個大型本體有什麼缺點？"]),

lesson(u"本體對齊、合併與版本管理",
  u"兩套本體說的是同一件事嗎？",
  [u"理解本體對齊的問題與方法", u"認識 SKOS 對應關係與 SSSOM", u"理解本體版本管理的做法"],
  [("p", u"不同組織各自建立的本體，常常描述重疊的領域。要整合資料，就要找出兩邊概念的對應：這叫<strong>本體對齊</strong>（ontology alignment / matching）。"),
   ("h", u"對齊的困難"),
   ("ul", [u"<strong>名稱不同、意思相同</strong>：Car 與 Automobile、「客戶」與「顧客」。", u"<strong>名稱相同、意思不同</strong>：兩個系統的「客戶」，一個含潛在客戶，一個只算成交客戶。", u"<strong>粒度不同</strong>：一邊有「轎車」「休旅車」，另一邊只有「汽車」。", u"<strong>結構不同</strong>：一邊把地址當屬性，另一邊把地址當類別。"]),
   ("h", u"對齊的方法"),
   ("t", [u"方法", u"依據"],
    [[u"字串比對", u"標籤的編輯距離、同義詞（WordNet、UMLS）"], [u"結構比對", u"上下層類別、屬性是否相似"], [u"實例比對", u"兩個類別的實例重疊多少"],
     [u"邏輯驗證", u"對齊後合併，用推理機檢查是否產生不一致"], [u"嵌入與 LLM", u"把標籤與定義轉成向量比較相似度，再請 LLM 判斷（第 53 課）"]]),
   ("p", u"每年的 OAEI（本體對齊評估倡議）競賽會比較各種對齊系統，在解剖學、疾病、生物多樣性等資料集上的表現。"),
   ("h", u"表達對應關係"),
   ("t", [u"關係", u"意思", u"強度"],
    [[u"owl:equivalentClass", u"邏輯上完全等價", u"最強，會影響推理"], [u"rdfs:subClassOf", u"一邊是另一邊的子類別", u"強"], [u"skos:exactMatch", u"可以互換使用", u"不影響 OWL 推理"],
     [u"skos:closeMatch", u"相近，部分情況可互換", u"弱"], [u"skos:broadMatch／narrowMatch", u"較廣／較窄", u"弱"], [u"skos:relatedMatch", u"相關", u"最弱"]]),
   ("p", u"生物醫學社群提出 <strong>SSSOM</strong>（Simple Standard for Sharing Ontological Mappings）：用一張 TSV 表格記錄對應關係，並註明信心分數、對應方法（人工、詞彙比對、LLM）、作者，讓對應本身也可追溯。"),
   PY(u"""
# 簡單的詞彙對齊：標籤正規化 + 字串相似度，輸出 SSSOM 風格的表格
from difflib import SequenceMatcher
import csv, sys

A = {"a:Car": "Automobile", "a:Truck": "Lorry", "a:Customer": "Customer"}
B = {"b:Auto": "automobile", "b:Truck": "truck", "b:Client": "client", "b:Buyer": "customer"}

def norm(s): return s.lower().replace("_", " ").strip()

rows = []
for ia, la in A.items():
    best = max(B.items(), key=lambda kv: SequenceMatcher(None, norm(la), norm(kv[1])).ratio())
    score = SequenceMatcher(None, norm(la), norm(best[1])).ratio()
    pred = "skos:exactMatch" if score > 0.95 else "skos:closeMatch"
    if score > 0.6:
        rows.append([ia, pred, best[0], "semapv:LexicalMatching", round(score, 2)])

w = csv.writer(sys.stdout, delimiter="\\t")
w.writerow(["subject_id", "predicate_id", "object_id", "mapping_justification", "confidence"])
w.writerows(rows)      # 注意：Truck 與 Lorry 是同義詞，純字串比對找不到——需要同義詞庫或嵌入
"""),
   ("h", u"版本管理"),
   ("ul", [u"<strong>版本 IRI</strong>：owl:versionIRI 讓每個發布版本都有固定的網址，使用者可以釘選特定版本。", u"<strong>不要刪除，要棄用</strong>：不再使用的類別標記 owl:deprecated true，並以 obo:IAO_0100001（term replaced by）指向替代者；直接刪除會讓引用它的資料斷掉。", u"<strong>語意差異</strong>：比較兩個版本時，除了文字 diff，還要比較推論結果的差異（例如某類別的上層類別變了），ROBOT diff 等工具可以做到。", u"<strong>變更紀錄</strong>：每次發布附上新增、修改、棄用的術語清單。"]),
  ],
  u"本體對齊要找出不同本體間概念的對應，困難在於同義異名、同名異義、粒度與結構差異。方法有字串、結構、實例比對、邏輯驗證與嵌入或 LLM，OAEI 競賽評估各系統。對應可用 owl:equivalentClass、subClassOf 或較寬鬆的 SKOS 對應關係表達，SSSOM 以表格記錄信心與方法。版本管理需使用版本 IRI、以 deprecated 棄用而非刪除、比較推論差異並保留變更紀錄。",
  [u"舉一個「名稱相同、意思不同」的企業資料例子。", u"什麼時候該用 skos:closeMatch 而不是 owl:equivalentClass？", u"為什麼不應該直接刪除本體中的類別？"]),

lesson(u"品質評估與常見陷阱",
  u"怎麼知道一個本體好不好？",
  [u"認識本體品質的評估面向", u"認識 OOPS! 等陷阱檢測", u"建立本體的品質檢查清單"],
  [("h", u"評估的面向"),
   ("t", [u"面向", u"問題", u"方法"],
    [[u"<strong>邏輯正確</strong>", u"一致嗎？有沒有不可滿足的類別？", u"推理機"], [u"<strong>需求滿足</strong>", u"能回答能力問題嗎？", u"SPARQL 測試（第 46 課）"],
     [u"<strong>領域正確</strong>", u"專家同意這些定義與關係嗎？", u"專家審查"], [u"<strong>資料符合</strong>", u"實際資料符合本體嗎？", u"SHACL 驗證（第 37 課）"],
     [u"<strong>結構品質</strong>", u"階層深度、每個類別的子類別數、孤兒類別", u"度量工具"], [u"<strong>可用性</strong>", u"有沒有標籤、定義、說明？命名一致嗎？", u"檢查清單"],
     [u"<strong>實際效益</strong>", u"應用有沒有因此變好？", u"任務導向評估：搜尋準確率、整合時間、問答正確率"]]),
   ("h", u"OOPS!：本體陷阱掃描"),
   ("p", u"馬德里理工大學的 OOPS!（OntOlogy Pitfall Scanner!）整理了四十多種常見陷阱，例如："),
   ("ul", [u"P04：建立了沒有連到任何東西的孤立元素。", u"P08：缺少標籤或說明。", u"P10：缺少互斥公理（第 25 課的經典錯誤）。", u"P11：缺少定義域或值域。", u"P13：缺少反向屬性。", u"P19：在定義域或值域中用多個類別，被誤解為「或」（實際是「且」）。", u"P24：遞迴定義。", u"P41：沒有宣告授權。"]),
   PY(u"""
# 自製品質檢查：缺標籤、缺定義、沒有任何互斥公理、定義域多個類別
from rdflib import Graph, RDF, RDFS, OWL
from rdflib.namespace import SKOS

g = Graph().parse("library.ttl")
classes = set(g.subjects(RDF.type, OWL.Class))
props   = set(g.subjects(RDF.type, OWL.ObjectProperty))

no_label = [c for c in classes if (c, RDFS.label, None) not in g]
no_def   = [c for c in classes if (c, SKOS.definition, None) not in g and (c, RDFS.comment, None) not in g]
multi_domain = [p for p in props if len(list(g.objects(p, RDFS.domain))) > 1]
has_disjoint = any(g.triples((None, OWL.disjointWith, None))) or any(g.triples((None, RDF.type, OWL.AllDisjointClasses)))

print(f"{len(classes)} 個類別；缺標籤 {len(no_label)}；缺定義 {len(no_def)}")
print("定義域有多個類別（是交集，不是聯集！）：", multi_domain)
if not has_disjoint:
    print("警告：沒有任何互斥公理，推理機幾乎抓不到錯誤")
"""),
   ("h", u"品質檢查清單"),
   ("ol", [u"推理機：一致，沒有不可滿足的類別。", u"每個類別與屬性都有標籤與文字定義。", u"兄弟類別之間是否該互斥？該宣告的都宣告了。", u"屬性的定義域、值域、特性（傳遞、函數性……）都經過思考。", u"所有能力問題的測試都通過。", u"有版本 IRI、授權、作者、變更紀錄。", u"重用了標準詞彙，而不是重新發明。"]),
  ],
  u"本體品質從邏輯正確、需求滿足、領域正確、資料符合、結構品質、可用性與實際效益評估，方法包括推理機、能力問題測試、專家審查、SHACL 與度量工具。OOPS! 整理四十多種常見陷阱，如孤立元素、缺標籤、缺互斥、缺定義域值域、定義域多類別被誤解為聯集、缺授權。可用 rdflib 撰寫自製檢查，並依清單逐項確認。",
  [u"為什麼「定義域寫多個類別」是常見陷阱？", u"一個沒有任何互斥公理的本體會有什麼問題？", u"如何用「實際效益」評估一個企業本體？"]),
]),

(u"模組 I｜現代應用", [

lesson(u"企業知識圖譜",
  u"把散落在各系統的資料，用本體接起來",
  [u"理解企業知識圖譜的架構", u"比較 RDF 與屬性圖兩種技術路線", u"了解從資料到知識圖譜的建構流程"],
  [("p", u"一家中大型企業可能有數百套系統：ERP、CRM、MES、HR、財務……每套系統對「客戶」「產品」「訂單」都有自己的定義。<strong>企業知識圖譜</strong>用一套共同的本體，把這些資料連成一張圖。"),
   ("h", u"兩條技術路線"),
   ("t", [u"", u"RDF 三元組資料庫", u"屬性圖資料庫"],
    [[u"代表產品", u"GraphDB、Stardog、Amazon Neptune、Apache Jena", u"Neo4j、TigerGraph、Amazon Neptune、Memgraph"], [u"資料模型", u"三元組，IRI 全域識別", u"節點與邊都可帶屬性（鍵值對）"],
     [u"綱要", u"RDFS、OWL、SHACL", u"較鬆散，通常在應用層定義"], [u"查詢語言", u"SPARQL", u"Cypher、GQL（2024 年 ISO 標準）"],
     [u"推理", u"有，標準化", u"通常沒有，或需外掛"], [u"優勢", u"資料整合、標準、互通、推理", u"圖演算法（路徑、社群、中心性）、開發者友善"]]),
   ("p", u"兩者正在接近：RDF 1.2 的 RDF-star 讓邊也能有屬性；屬性圖陣營也開始重視綱要。很多企業的做法是：<strong>用本體定義語意，用最適合的資料庫存放</strong>。"),
   ("h", u"建構流程"),
   ("ol", [u"<strong>本體設計</strong>：從能力問題出發（第 46 課）。", u"<strong>資料對應</strong>：把資料庫表格、CSV、API 對應到本體（R2RML、RML；或寫 Python ETL）。", u"<strong>實體解析</strong>：判斷不同系統的「台積電」「TSMC」「台灣積體電路製造股份有限公司」是同一家公司。", u"<strong>非結構化抽取</strong>：從文件、郵件、合約中用 NLP 或 LLM 抽取實體與關係。", u"<strong>驗證與推理</strong>：SHACL 檢查品質，推理補充隱含關係。", u"<strong>服務</strong>：搜尋、推薦、問答、分析、儀表板。"]),
   PY(u"""
# 把兩個系統的資料（CRM、ERP）對應到同一個本體，並做簡單的實體解析
import pandas as pd
from rdflib import Graph, Namespace, Literal, RDF
EX = Namespace("http://example.org/kg#")

crm = pd.DataFrame({"cust_id": ["C01", "C02"], "name": ["台積電", "鴻海精密"], "tax_id": ["22099131", "04541302"]})
erp = pd.DataFrame({"vendor": ["V9"], "vendor_name": ["台灣積體電路製造股份有限公司"], "vat": ["22099131"]})

g = Graph()
def company(tax_id):                       # 以統一編號作為實體解析的鍵 → 同一個 IRI
    return EX["org/" + tax_id]

for r in crm.itertuples():
    c = company(r.tax_id)
    g.add((c, RDF.type, EX.Organization)); g.add((c, EX.name, Literal(r.name)))
    g.add((c, EX.crmId, Literal(r.cust_id)))
for r in erp.itertuples():
    c = company(r.vat)
    g.add((c, RDF.type, EX.Organization)); g.add((c, EX.legalName, Literal(r.vendor_name)))
    g.add((c, EX.erpVendorId, Literal(r.vendor)))

# 同一家公司既是客戶也是供應商——跨系統才看得到的事實
q = "SELECT ?c ?n WHERE { ?c :crmId ?x ; :erpVendorId ?y ; :name ?n }"
print(list(g.query(q, initNs={"": EX})))
"""),
   ("note", u"實際案例", [("ul", [u"<strong>搜尋與推薦</strong>：電商的產品知識圖譜（屬性、相容性、替代品）。", u"<strong>金融</strong>：反洗錢與詐欺偵測，追蹤人、帳戶、公司之間的關係網。", u"<strong>製藥</strong>：連結基因、疾病、藥物、臨床試驗，找出藥物再利用的機會。", u"<strong>供應鏈</strong>：多層供應商的風險傳遞（第 63 課）。"])]),
  ],
  u"企業知識圖譜以共同本體連結散落在 ERP、CRM、MES 等系統的資料。RDF 三元組資料庫以 SPARQL、標準化推理與互通見長；屬性圖資料庫以 Cypher 或 GQL 與圖演算法見長，兩者正互相靠近。建構流程包括本體設計、資料對應、實體解析、非結構化抽取、驗證推理與服務。應用涵蓋搜尋推薦、反洗錢、藥物再利用與供應鏈風險。",
  [u"RDF 資料庫和屬性圖資料庫各適合什麼情境？", u"為什麼實體解析是企業知識圖譜最困難的步驟之一？", u"舉一個「跨系統才看得到」的企業洞見。"]),

lesson(u"Ontology 與大型語言模型：GraphRAG",
  u"讓 LLM 的回答有結構、有根據",
  [u"理解 LLM 的知識問題與 RAG", u"理解 GraphRAG 與知識圖譜增強的做法", u"了解本體在 AI 代理人中的角色"],
  [("p", u"大型語言模型（LLM）擅長理解與生成語言，但有幾個根本問題："),
   ("ul", [u"<strong>幻覺</strong>：一本正經地說錯。", u"<strong>知識過時</strong>：只知道訓練資料截止前的事。", u"<strong>不知道你的私有資料</strong>：公司內部的產品、客戶、流程。", u"<strong>難以追溯</strong>：答案從哪裡來？"]),
   ("h", u"RAG：檢索增強生成"),
   ("p", u"<strong>RAG</strong> 的做法是：先從資料庫檢索相關內容，再把它放進提示讓 LLM 回答。最常見的是把文件切塊、轉成向量，用語意相似度檢索。但向量 RAG 有弱點：遇到需要<strong>多步推理</strong>或<strong>彙整</strong>的問題（「我們有哪些供應商同時供貨給 A 廠和 B 廠，且位於颱風高風險區？」），文件片段很難拼出答案。"),
   ("h", u"知識圖譜增強的幾種做法"),
   ("t", [u"做法", u"流程", u"適合"],
    [[u"<strong>Text-to-SPARQL／Cypher</strong>", u"LLM 根據本體綱要，把問題翻譯成查詢語言，執行後再把結果寫成回答", u"結構化、精確的問題"],
     [u"<strong>子圖檢索</strong>", u"找出問題中的實體，取出它們周圍的子圖，轉成文字放進提示", u"關於特定實體的問題"],
     [u"<strong>GraphRAG</strong>（微軟，2024）", u"用 LLM 從文件中抽取實體與關係建圖，再用社群偵測分群並為每群寫摘要；回答時用摘要處理「全域」問題", u"「這批文件的主要主題是什麼？」這類彙整問題"],
     [u"<strong>混合</strong>", u"向量檢索找文件、圖譜找關係、兩者合併", u"多數實務場景"]]),
   ("h", u"本體的角色"),
   ("ul", [u"<strong>綱要即提示</strong>：把本體的類別與屬性放進提示，LLM 才知道可以查什麼、怎麼查。", u"<strong>約束輸出</strong>：LLM 產生的查詢或抽取結果，可以用本體與 SHACL 驗證。", u"<strong>消除歧義</strong>：「蘋果」是水果還是公司？實體連結到知識圖譜的 IRI 後就明確了。", u"<strong>可追溯</strong>：答案中的每個事實都能指回圖中的三元組與它的出處。", u"<strong>AI 代理人的工具</strong>：本體中定義的「動作」可以變成代理人能呼叫的工具（第 60、62 課）。"]),
   PY(u"""
# Text-to-SPARQL：把本體綱要放進提示，請 Claude 產生查詢，再用 rdflib 執行並驗證
import anthropic
from rdflib import Graph

g = Graph().parse("supply_chain.ttl")
schema = '''
Classes: :Supplier, :Plant, :Region, :Part
Properties: :supplies (Supplier -> Plant), :locatedIn (Supplier -> Region),
            :typhoonRisk (Region -> xsd:string, values "high"/"medium"/"low")
'''
question = "哪些供應商同時供貨給 A 廠和 B 廠，而且位於颱風高風險區？"

MODEL = "claude-..."            # 填入目前可用的 Claude 模型名稱
client = anthropic.Anthropic()
msg = client.messages.create(
    model=MODEL, max_tokens=1024,
    system="你把問題翻譯成 SPARQL。只能使用下列綱要中的類別與屬性，前綴 : 為 <http://example.org/sc#>。只輸出查詢本身。\\n" + schema,
    messages=[{"role": "user", "content": question}],
)
sparql = msg.content[0].text.strip().removeprefix("```sparql").removesuffix("```")

try:
    rows = list(g.query(sparql))                     # 語法錯誤會在這裡被抓到
    print(rows)
except Exception as e:
    print("查詢無效，可把錯誤訊息回傳給模型修正：", e)
"""),
   ("note", u"注意", [("p", u"把 LLM 產生的查詢直接拿去執行時，要限制成<strong>唯讀</strong>、設定逾時與結果數上限，並檢查只用到綱要中存在的詞彙。這和 SQL 注入的防範道理相同。")]),
  ],
  u"LLM 有幻覺、知識過時、不知私有資料與難以追溯等問題，RAG 先檢索再生成，但向量 RAG 難處理多步推理與彙整。知識圖譜增強的做法包括 Text-to-SPARQL、子圖檢索、微軟 2024 年的 GraphRAG（抽取建圖、社群摘要）與混合方式。本體提供綱要提示、約束輸出、消除歧義、可追溯，並讓動作成為代理人工具。執行 LLM 產生的查詢須限制唯讀、逾時與詞彙。",
  [u"向量 RAG 在哪類問題上表現不好？為什麼？", u"GraphRAG 怎麼回答「這批文件的主要主題是什麼」？", u"為什麼要用本體或 SHACL 驗證 LLM 的輸出？"]),

lesson(u"用 LLM 輔助建構 Ontology",
  u"從文件中抽取概念、關係與公理",
  [u"了解 LLM 在本體工程各階段的用途", u"會設計結構化的抽取流程", u"理解人類審查的必要性"],
  [("p", u"傳統的本體建構最貴的部分是<strong>知識擷取</strong>：訪談專家、讀大量文件、整理術語。LLM 能大幅加速這些工作，但不能取代判斷。"),
   ("h", u"LLM 可以幫忙的地方"),
   ("t", [u"階段", u"LLM 的工作", u"人類的工作"],
    [[u"規格", u"根據使用情境草擬能力問題", u"確認優先順序與範圍"], [u"術語擷取", u"從手冊、法規、規格書中列出候選術語與定義", u"去除重複、確認意思"],
     [u"階層與關係", u"建議上下層關係、屬性、定義域值域", u"檢查是否混淆 is-a 與 part-of 等錯誤"], [u"公理", u"把自然語言規則轉成 OWL 公理（Manchester 語法）", u"用推理機驗證、檢查意外推論"],
     [u"對齊", u"判斷兩個概念是否對應（第 49 課）", u"審查低信心的結果"], [u"資料填充", u"從文件抽取個體與關係", u"以 SHACL 驗證、抽樣檢查"], [u"文件", u"為每個類別撰寫說明與範例", u"校對"]]),
   ("h", u"結構化抽取"),
   ("p", u"讓 LLM 輸出符合固定結構的 JSON（工具呼叫或 JSON Schema），比自由文字可靠得多。再用程式把 JSON 轉成 RDF，交給推理機與 SHACL 檢查。"),
   PY(u"""
# 用 Claude 的工具呼叫，從文件中抽取符合本體的實體與關係（結構化輸出）
import anthropic, json
from rdflib import Graph, Namespace, Literal, RDF, RDFS

doc = "B-101 號機於 6 月 3 日在桃園機場執行 A 檢，技師陳大明發現左側發動機滑油壓力感測器異常，更換零件 P-8841 後放行。"

tool = {"name": "record_maintenance",
        "description": "記錄維修事件，所有欄位都必須出現在原文中",
        "input_schema": {"type": "object", "properties": {
            "aircraft": {"type": "string"}, "date": {"type": "string"}, "station": {"type": "string"},
            "technician": {"type": "string"}, "finding": {"type": "string"},
            "parts_replaced": {"type": "array", "items": {"type": "string"}}},
            "required": ["aircraft", "finding"]}}

MODEL = "claude-..."            # 填入目前可用的 Claude 模型名稱
client = anthropic.Anthropic()
msg = client.messages.create(model=MODEL, max_tokens=1024, tools=[tool],
                             tool_choice={"type": "tool", "name": "record_maintenance"},
                             messages=[{"role": "user", "content": doc}])
data = next(b.input for b in msg.content if b.type == "tool_use")

AV = Namespace("http://example.org/aviation#")
g = Graph(); ev = AV["event/" + data["aircraft"] + "-" + data.get("date", "unknown")]
g.add((ev, RDF.type, AV.MaintenanceEvent))
g.add((ev, AV.onAircraft, AV["aircraft/" + data["aircraft"]]))
g.add((ev, RDFS.comment, Literal(data["finding"], lang="zh-TW")))
for p in data.get("parts_replaced", []):
    g.add((ev, AV.replacedPart, AV["part/" + p]))
print(g.serialize(format="turtle"))     # 接著交給 SHACL 驗證、人工抽樣審查
"""),
   ("h", u"常見問題"),
   ("ul", [u"<strong>表面相似</strong>：LLM 擅長命名，但容易把「部分」當成「子類別」、把角色當成類別。", u"<strong>不一致</strong>：同一份文件問兩次，得到不同的階層；需要固定流程、合併與去重。", u"<strong>過度生成</strong>：產生一大堆沒人需要的類別；用能力問題控制範圍。", u"<strong>來源</strong>：每一筆抽取結果都要記錄來自哪份文件的哪一段（PROV-O）。"]),
   ("note", u"建議的工作方式", [("p", u"把 LLM 當成一位很勤快、讀很快、但需要被審查的助理：它產生候選，推理機與 SHACL 做自動檢查，領域專家做最後判斷。人類審查的負擔從「從零寫起」變成「審核與修正」。")]),
  ],
  u"LLM 可加速本體工程中最昂貴的知識擷取：草擬能力問題、擷取術語、建議階層與關係、把規則轉成 OWL 公理、對齊、資料填充與撰寫文件，人類負責確認、檢查與驗證。以工具呼叫或 JSON Schema 做結構化抽取，再轉成 RDF 交給推理機與 SHACL。常見問題有混淆部分與子類別、結果不一致、過度生成與缺乏出處，應以 LLM 產生候選、自動檢查、專家審核的流程進行。",
  [u"為什麼結構化輸出比自由文字更適合本體抽取？", u"LLM 最容易犯的本體建模錯誤是什麼？", u"設計一個從法規條文建立本體的人機協作流程。"]),

lesson(u"資料網格、語意層與數位孿生",
  u"本體在現代資料架構中的位置",
  [u"理解語意層與指標定義", u"理解資料網格與資料產品", u"理解數位孿生與本體的關係"],
  [("h", u"語意層"),
   ("p", u"同一間公司裡，財務部和業務部算出的「營收」常常不一樣：要不要扣退貨？用訂單日還是出貨日？<strong>語意層</strong>（semantic layer）把商業概念與指標的定義集中管理，所有報表與 AI 工具都透過它查詢。"),
   ("ul", [u"例子：dbt 語意層（MetricFlow）、Cube、LookML 等。", u"它像是一個<strong>輕量的本體</strong>：定義實體（客戶、訂單）、維度、指標及它們的關係。", u"LLM 時代特別重要：讓 AI 透過語意層查詢，就不會自己發明「營收」的算法。"]),
   ("h", u"資料網格"),
   ("p", u"德赫加尼（2019）提出<strong>資料網格</strong>（data mesh）：不再由中央資料團隊包辦所有資料，而是讓各業務領域把自己的資料當成<strong>資料產品</strong>來經營。四個原則："),
   ("ol", [u"領域擁有資料。", u"資料即產品（有負責人、文件、品質保證）。", u"自助式資料平台。", u"<strong>聯邦式運算治理</strong>：全公司共用的標準（例如「客戶」的識別方式）由各領域共同制定，並以程式自動執行。"]),
   ("p", u"第 4 點正是本體的用武之地：共用的本體讓各領域的資料產品能互相連結。"),
   ("h", u"數位孿生"),
   ("p", u"<strong>數位孿生</strong>是實體世界（工廠、城市、供應鏈、組織）在數位世界中的即時對應。它需要三樣東西："),
   ("t", [u"元素", u"內容", u"本體的角色"],
    [[u"結構", u"有哪些東西、它們怎麼連接", u"類別、屬性、關係"], [u"狀態", u"即時感測資料與交易資料", u"把資料串流對應到物件"], [u"行為", u"能做什麼、會發生什麼", u"動作、規則、模擬模型"]]),
   ("p", u"微軟 Azure Digital Twins 用 DTDL（Digital Twins Definition Language，以 JSON-LD 為基礎）定義孿生模型；工業界用資產管理殼（第 44 課）。而 Palantir 把它的 Ontology 稱為<strong>組織的數位孿生</strong>——不只描述機器，也描述訂單、人員、決策（第 61 課）。"),
   PY(u"""
# 一個極簡的「語意層」：指標只定義一次，任何人（或 AI）都透過它查詢
import pandas as pd

orders = pd.DataFrame({"order_id": [1, 2, 3, 4], "amount": [1000, 500, 800, 300],
                       "status": ["shipped", "returned", "shipped", "cancelled"],
                       "region": ["北", "北", "南", "南"]})

METRICS = {   # 指標的唯一定義
    "net_revenue": {"desc": "已出貨訂單金額（不含退貨與取消）",
                    "filter": lambda d: d.status == "shipped", "agg": ("amount", "sum")},
    "order_count": {"desc": "所有成立的訂單數（不含取消）",
                    "filter": lambda d: d.status != "cancelled", "agg": ("order_id", "count")},
}

def query(metric, by=None):
    m = METRICS[metric]; d = orders[m["filter"](orders)]
    col, fn = m["agg"]
    return d.groupby(by)[col].agg(fn) if by else d[col].agg(fn)

print(query("net_revenue"))             # 1800
print(query("net_revenue", by="region"))
"""),
  ],
  u"語意層集中定義商業概念與指標（如 dbt MetricFlow、Cube、LookML），像輕量本體，讓報表與 AI 用同一套算法。資料網格主張領域擁有資料、資料即產品、自助平台與聯邦式運算治理，共用本體讓資料產品互相連結。數位孿生需要結構、狀態與行為，Azure 以 DTDL、工業界以資產管理殼定義，Palantir 則把 Ontology 稱為組織的數位孿生。",
  [u"為什麼不同部門算出的「營收」會不同？語意層怎麼解決？", u"資料網格的「聯邦式運算治理」和本體有什麼關係？", u"一個工廠的數位孿生需要哪三種元素？"]),
]),
]
