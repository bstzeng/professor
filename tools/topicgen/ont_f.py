# -*- coding: utf-8 -*-
"""Ontology：模組 F 語意網技術（31～38）、G 上層本體與領域本體（39～45）。"""
from ont_common import *

MODULES = [
(u"模組 F｜語意網技術", [

lesson(u"柏納斯–李的語意網願景",
  u"讓網路從「給人看的文件」變成「給機器理解的資料」",
  [u"理解語意網的願景與動機", u"認識語意網的技術堆疊", u"評估語意網的成就與挫折"],
  [("p", u"2001 年，全球資訊網的發明者提姆・柏納斯–李與亨德勒、拉西拉在《科學人》發表〈語意網〉一文。他們描繪的場景是：你的軟體代理人能自動讀懂醫院、診所、保險公司網站上的資訊，幫你安排一個時間、地點、保險都符合的看診。"),
   ("p", u"問題在於：當時的網頁是 HTML，只描述「怎麼顯示」，不描述「是什麼」。網頁上寫「營業時間：週一至週五 9:00–17:00」，人看得懂，機器只看到一串字。"),
   ("h", u"語意網的技術堆疊（「千層蛋糕」）"),
   ("t", [u"層", u"技術", u"作用"],
    [[u"識別", u"IRI（URI）", u"給每個東西一個全球唯一的名字"], [u"資料模型", u"RDF", u"用三元組描述任何東西（第 32 課）"], [u"語法", u"Turtle、JSON-LD、RDF/XML", u"把 RDF 寫下來（第 33 課）"],
     [u"簡單綱要", u"RDFS", u"類別、子類別、定義域、值域（第 34 課）"], [u"本體", u"OWL", u"完整的描述邏輯（第 35 課）"], [u"查詢", u"SPARQL", u"查詢 RDF 圖（第 36 課）"],
     [u"規則與驗證", u"SWRL、RIF、SHACL", u"規則推理與資料驗證（第 37 課）"], [u"信任與證明", u"數位簽章、出處（PROV-O）", u"資料從哪裡來、可不可信"]]),
   ("h", u"成就與挫折"),
   ("ul", [u"<strong>挫折</strong>：「整個網路變成機器可讀的知識庫」並沒有發生。大部分網站沒有動機去標註語意；OWL 的學習曲線陡峭；早期工具難用。", u"<strong>成就</strong>：技術在特定領域大放異彩——生物醫學本體、政府開放資料、圖書館與博物館的鏈結資料、Wikidata（第 42 課）。", u"<strong>意外的勝利</strong>：搜尋引擎推動的 schema.org（第 41 課）讓數以億計的網頁嵌入 JSON-LD 結構化資料；Google 在 2012 年推出知識圖譜。語意網以「知識圖譜」之名，悄悄進入了主流。"]),
   PY(u"""
# 網頁中嵌入的 JSON-LD（schema.org），用 rdflib 讀成 RDF 圖
from rdflib import Graph
jsonld = '''
{ "@context": "https://schema.org",
  "@type": "Book",
  "name": "The Lord of the Rings",
  "author": { "@type": "Person", "name": "J. R. R. Tolkien" },
  "datePublished": "1954" }
'''
g = Graph().parse(data=jsonld, format="json-ld")   # 需要能連線取得 schema.org 的 context
for s, p, o in g:
    print(p, o)
"""),
  ],
  u"2001 年柏納斯–李等人提出語意網，讓網路從給人看的文件變成機器可理解的資料。技術堆疊包括 IRI、RDF、序列化語法、RDFS、OWL、SPARQL、規則與 SHACL、信任與出處。全網語意化的願景未實現，但技術在生物醫學、開放資料、文化資產與 Wikidata 大放異彩，並透過 schema.org 的 JSON-LD 與 2012 年 Google 知識圖譜進入主流。",
  [u"為什麼 HTML 網頁對機器來說「看不懂」？", u"語意網的哪些部分成功了，哪些沒有？", u"schema.org 為什麼能讓網站願意標註語意？"]),

lesson(u"RDF：三元組與 IRI",
  u"用最簡單的結構描述任何東西：主詞、述詞、受詞",
  [u"理解 RDF 的三元組資料模型", u"理解 IRI、空白節點與常值", u"用 rdflib 建立與操作 RDF 圖"],
  [("p", u"<strong>RDF</strong>（Resource Description Framework）只有一種結構：<strong>三元組</strong>。"),
   F(r"\langle \text{主詞},\; \text{述詞},\; \text{受詞} \rangle"),
   ("p", u"一組三元組就是一張<strong>有向、帶標籤的圖</strong>：主詞與受詞是節點，述詞是邊。任何資料——表格、樹、網路——都能拆成三元組，這是 RDF 能整合異質資料的原因。"),
   ow("triples", u"加入幾個三元組，看圖怎麼長出來；也注意下方自動產生的 Turtle："),
   ("h", u"三種節點"),
   ("t", [u"類型", u"說明", u"例子"],
    [[u"<strong>IRI</strong>", u"全球唯一的識別碼（URI 的國際化版本，可含中文）", u"http://www.wikidata.org/entity/Q15228（《魔戒》）"], [u"<strong>常值</strong>", u"字串、數字、日期；可帶語言標籤或資料型別", u"\"魔戒\"@zh-TW、\"1954\"^^xsd:gYear"],
     [u"<strong>空白節點</strong>", u"沒有全域名字的節點，只在這張圖裡有意義", u"「某個地址」：_:addr1 :城市 :台北"]]),
   ("p", u"主詞只能是 IRI 或空白節點；述詞只能是 IRI；受詞三者皆可。"),
   ("h", u"為什麼用 IRI"),
   ("ul", [u"<strong>全球唯一</strong>：不同組織的「Book」只要 IRI 不同，就不會撞名。", u"<strong>可以解析</strong>：好的 IRI 用 HTTP 打開，就能取得這個東西的描述（鏈結資料原則，第 38 課）。", u"<strong>可以連結</strong>：你的資料可以直接引用 Wikidata 的 IRI，兩邊的資料就接起來了。"]),
   PY(u"""
from rdflib import Graph, URIRef, Literal, BNode, Namespace
from rdflib.namespace import RDF, XSD

WD  = Namespace("http://www.wikidata.org/entity/")
LIB = Namespace("http://example.org/lib#")
g = Graph()

lotr = WD.Q15228                                   # 直接引用 Wikidata 的 IRI
g.add((lotr, RDF.type, LIB.Novel))
g.add((lotr, LIB.title, Literal("魔戒", lang="zh-TW")))
g.add((lotr, LIB.title, Literal("The Lord of the Rings", lang="en")))
g.add((lotr, LIB.year, Literal("1954", datatype=XSD.gYear)))

addr = BNode()                                     # 空白節點
g.add((LIB.Tolkien, LIB.address, addr))
g.add((addr, LIB.city, Literal("Oxford")))

for s, p, o in g.triples((lotr, None, None)):      # 樣式比對：主詞固定，其他任意
    print(p, o)
"""),
   ("note", u"RDF 的限制", [("ul", [u"只能表達二元關係；多元關係要用具體化或空白節點拆開。", u"三元組本身沒有時間或來源，需要命名圖或 RDF-star（RDF 1.2）補充（第 25 課）。", u"開放世界語意：RDF 不會告訴你資料是否完整。"])]),
  ],
  u"RDF 只有一種結構：主詞、述詞、受詞三元組，組合起來是一張有向標籤圖，任何資料都能拆成三元組，因此擅長整合。節點有 IRI（全球唯一、可解析、可連結）、常值（可帶語言標籤或型別）與空白節點；主詞為 IRI 或空白節點，述詞只能是 IRI。限制包括只有二元關係、三元組沒有時間來源、開放世界語意。",
  [u"為什麼表格資料可以轉成 RDF 三元組？舉例說明。", u"空白節點適合用在什麼情況？", u"直接引用 Wikidata 的 IRI 有什麼好處？"]),

lesson(u"序列化格式：Turtle、JSON-LD 與其他",
  u"同一張圖，五種寫法",
  [u"認識主要的 RDF 序列化格式", u"知道各格式的適用場合", u"用 rdflib 互相轉換"],
  [("p", u"RDF 是抽象的圖，要存進檔案或在網路上傳輸，就要選一種<strong>序列化格式</strong>。"),
   ow("serial", u"切換不同的格式，比較同樣 6 個三元組的寫法："),
   ("t", [u"格式", u"副檔名", u"特點", u"適合"],
    [[u"Turtle", u".ttl", u"簡潔易讀，有前綴、分號、逗號縮寫", u"手寫、閱讀、版本控制"], [u"N-Triples", u".nt", u"一行一個三元組，無縮寫", u"大量資料的串流處理、合併"],
     [u"N-Quads", u".nq", u"N-Triples 加上第四欄（所屬的命名圖）", u"多個圖的資料集"], [u"TriG", u".trig", u"Turtle 加上命名圖", u"多個圖的資料集"],
     [u"JSON-LD", u".jsonld", u"一般 JSON 加上 @context", u"網頁、Web API、與 JavaScript 互通"], [u"RDF/XML", u".rdf / .owl", u"第一個標準格式（2004）", u"舊系統、Protégé 預設輸出"]]),
   ("h", u"Turtle 的縮寫規則"),
   ("ul", [u"<code>@prefix lib: &lt;http://example.org/lib#&gt; .</code> 之後，lib:Book 就代表完整的 IRI。", u"分號 <code>;</code>：同一個主詞，接下一個述詞。", u"逗號 <code>,</code>：同一個主詞與述詞，接下一個受詞。", u"<code>a</code>：rdf:type 的縮寫。", u"<code>[ ... ]</code>：空白節點。"]),
   PY(u"""
from rdflib import Graph

ttl = '''
@prefix lib: <http://example.org/lib#> .
lib:LOTR a lib:Novel ;
    lib:title "The Lord of the Rings" ;
    lib:author lib:Tolkien ;
    lib:subject lib:Fantasy, lib:Adventure ;      # 逗號：多個受詞
    lib:publisher [ lib:name "Allen & Unwin" ] .  # 空白節點
'''
g = Graph().parse(data=ttl, format="turtle")

for fmt in ["nt", "json-ld", "xml"]:
    print(f"--- {fmt} ---")
    print(g.serialize(format=fmt))
"""),
   ("h", u"JSON-LD 的 @context"),
   ("p", u"JSON-LD 的妙處在於：一般的網頁開發者看到的就是普通的 JSON；但 @context 把每個鍵對應到一個 IRI，RDF 工具就能把它讀成三元組。這讓結構化資料能被大量採用（第 41 課的 schema.org）。"),
   ("note", u"選擇建議", [("p", u"手寫與版本控制用 Turtle；給網頁與前端用 JSON-LD；大檔案交換用 N-Triples（可以 gzip，逐行處理）；需要命名圖時用 TriG 或 N-Quads。")]),
  ],
  u"RDF 圖需序列化才能儲存與傳輸。Turtle 簡潔易讀，以前綴、分號、逗號、a 與方括號空白節點縮寫；N-Triples 一行一個三元組適合大量處理；N-Quads 與 TriG 支援命名圖；JSON-LD 是加上 @context 的一般 JSON，適合網頁與 API；RDF/XML 是最早的標準。rdflib 可在各格式間互轉。",
  [u"Turtle 中的分號和逗號各代表什麼？", u"為什麼 JSON-LD 對網頁開發者特別友善？", u"處理十億個三元組的檔案，你會選哪種格式？為什麼？"]),

lesson(u"RDFS：最基本的綱要語言",
  u"類別、子類別、子屬性、定義域、值域，以及它們的推論規則",
  [u"認識 RDFS 的詞彙", u"理解 RDFS 的推論規則", u"知道 RDFS 的表達力限制"],
  [("p", u"RDF 只能描述個體之間的關係。<strong>RDF Schema</strong>（RDFS，1999～2004）增加了一組描述「類別與屬性」的詞彙："),
   ("t", [u"詞彙", u"意思"],
    [[u"rdfs:Class", u"一個類別"], [u"rdfs:subClassOf", u"子類別"], [u"rdfs:subPropertyOf", u"子屬性"], [u"rdfs:domain", u"屬性的定義域"], [u"rdfs:range", u"屬性的值域"],
     [u"rdfs:label、rdfs:comment", u"人類可讀的名稱與說明"], [u"rdfs:seeAlso、rdfs:isDefinedBy", u"相關資源"]]),
   ("h", u"RDFS 的推論規則（節錄）"),
   ("t", [u"規則", u"如果", u"則"],
    [[u"rdfs2（定義域）", u"P rdfs:domain C；x P y", u"x rdf:type C"], [u"rdfs3（值域）", u"P rdfs:range C；x P y", u"y rdf:type C"], [u"rdfs5", u"P ⊑ Q；Q ⊑ R（子屬性）", u"P ⊑ R"],
     [u"rdfs7", u"P rdfs:subPropertyOf Q；x P y", u"x Q y"], [u"rdfs9", u"A ⊑ B；x rdf:type A", u"x rdf:type B"], [u"rdfs11", u"A ⊑ B；B ⊑ C", u"A ⊑ C"]]),
   ow("reason", u"互動裡的「subClassOf 傳遞」「型別繼承」「定義域與值域」就是 RDFS 的規則 rdfs11、rdfs9、rdfs2/3："),
   PY(u"""
from rdflib import Graph
import owlrl

g = Graph().parse(data='''
@prefix :     <http://example.org/lib#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
:Novel rdfs:subClassOf :Book .
:Book  rdfs:subClassOf :Publication .
:writtenBy rdfs:domain :Book ; rdfs:range :Person .
:hasMother rdfs:subPropertyOf :hasParent .
:LOTR a :Novel ; :writtenBy :Tolkien .
:Ann :hasMother :Mary .
''', format="turtle")

owlrl.DeductiveClosure(owlrl.RDFS_Semantics).expand(g)
ns = {"": "http://example.org/lib#"}
print([str(r.t) for r in g.query("SELECT ?t WHERE { :Tolkien a ?t }", initNs=ns)])  # 包含 :Person
print(g.query("ASK { :Ann :hasParent :Mary }", initNs=ns).askAnswer)            # True（rdfs7）
"""),
   ("h", u"RDFS 做不到的事"),
   ("ul", [u"無法說兩個類別<strong>互斥</strong>（貓和狗沒有交集）。", u"無法說屬性是<strong>傳遞</strong>、<strong>對稱</strong>、<strong>函數性</strong>的。", u"無法定義類別（父母 ≡ 人 ⊓ ∃有子女.人）。", u"無法表達基數（恰好兩個父母）。", u"<strong>沒有否定，所以 RDFS 永遠不會矛盾</strong>：任何 RDFS 資料都是一致的。"]),
   ("p", u"需要這些功能時，就要用 OWL（下一課）。但 RDFS 的簡單與高效，使它在大量資料的場景中仍然很常用。"),
  ],
  u"RDFS 增加描述類別與屬性的詞彙：Class、subClassOf、subPropertyOf、domain、range、label、comment 等。其推論規則包括定義域與值域推出型別、子屬性傳遞與繼承、型別沿子類別繼承、子類別傳遞。RDFS 無法表達互斥、屬性特性、類別定義與基數，且沒有否定所以永不矛盾；需要時改用 OWL，但 RDFS 在大量資料中仍常用。",
  [u"根據 rdfs7，由「安 hasMother 瑪麗」可以推出什麼？", u"為什麼 RDFS 資料永遠不會矛盾？", u"列出三件 RDFS 做不到、OWL 做得到的事。"]),

lesson(u"OWL 2：完整的本體語言",
  u"類別運算式、屬性特性、等價、互斥、資料範圍",
  [u"認識 OWL 2 的主要構造", u"區分 OWL 2 DL 與 OWL 2 Full", u"用 Python 建立 OWL 本體"],
  [("p", u"<strong>OWL</strong>（Web Ontology Language）2004 年成為 W3C 標準，2009 年更新為 <strong>OWL 2</strong>。它以描述邏輯 SROIQ(D) 為基礎，提供完整的本體建模能力。"),
   ("h", u"主要構造"),
   ("t", [u"類別", u"OWL 詞彙", u"描述邏輯"],
    [[u"類別運算", u"owl:intersectionOf、unionOf、complementOf", u"⊓、⊔、¬"], [u"屬性限制", u"owl:someValuesFrom、allValuesFrom、hasValue", u"∃、∀、∃R.{a}"],
     [u"基數", u"owl:minQualifiedCardinality 等", u"≥n、≤n、=n"], [u"類別公理", u"owl:equivalentClass、disjointWith、AllDisjointClasses", u"≡、互斥"],
     [u"屬性特性", u"TransitiveProperty、SymmetricProperty、FunctionalProperty、inverseOf", u"S、I、F"], [u"屬性鏈", u"owl:propertyChainAxiom", u"R ∘ S ⊑ T"],
     [u"個體", u"owl:sameAs、differentFrom、AllDifferent", u"a = b、a ≠ b"], [u"列舉", u"owl:oneOf", u"{a, b, c}"], [u"鍵", u"owl:hasKey", u"以屬性值識別個體"]]),
   ("h", u"OWL 2 DL vs. OWL 2 Full"),
   ("ul", [u"<strong>OWL 2 DL</strong>：遵守描述邏輯的限制（例如類別和個體分開、傳遞屬性不能有基數限制），推理<strong>可判定</strong>。實務上說「OWL」幾乎都是指這個。", u"<strong>OWL 2 Full</strong>：允許任何 RDF 圖（類別也可以是個體、可以有屬性），表達力最大，但推理<strong>不可判定</strong>，很少使用。"]),
   PY(u"""
from owlready2 import (get_ontology, Thing, AllDisjoint, TransitiveProperty,
                       PropertyChain, sync_reasoner)

onto = get_ontology("http://example.org/family.owl")
with onto:
    class Person(Thing): pass
    class Man(Person): pass
    class Woman(Person): pass
    AllDisjoint([Man, Woman])                                   # 互斥
    class has_parent(Person >> Person): pass
    class has_brother(Person >> Man): pass
    class has_uncle(Person >> Man): pass
    has_uncle.property_chain.append(PropertyChain([has_parent, has_brother]))  # 角色鏈

    ann, mary, tom = Woman("Ann"), Woman("Mary"), Man("Tom")
    ann.has_parent = [mary]; mary.has_brother = [tom]

sync_reasoner(infer_property_values=True)
print(ann.has_uncle)          # [family.Tom]
onto.save(file="family.owl", format="rdfxml")
"""),
   ("note", u"Manchester 語法", [("p", u"Protégé 介面中常看到更接近英文的 <strong>Manchester 語法</strong>：<code>Parent EquivalentTo: Person and (hasChild some Person)</code>。它和 OWL/XML、函數式語法、Turtle 都是同一個本體的不同寫法。")]),
  ],
  u"OWL 2 以 SROIQ(D) 為基礎，提供類別運算（交聯補）、屬性限制（some、all、hasValue）、限定基數、等價與互斥公理、屬性特性、角色鏈、sameAs 與 differentFrom、列舉與鍵。OWL 2 DL 遵守描述邏輯限制，推理可判定；OWL 2 Full 允許任意 RDF 但不可判定。owlready2 可宣告互斥、角色鏈並以 HermiT 推理；Protégé 常用 Manchester 語法。",
  [u"用 OWL 怎麼表達「叔伯是父母的兄弟」？", u"OWL 2 DL 和 OWL 2 Full 最大的差別是什麼？", u"owl:hasKey 有什麼用途？"]),

lesson(u"SPARQL：查詢知識圖譜",
  u"用圖樣比對問問題",
  [u"理解 SPARQL 的基本結構", u"會寫 SELECT、FILTER、OPTIONAL、聚合與屬性路徑", u"用 Python 查詢本地圖與 Wikidata"],
  [("p", u"<strong>SPARQL</strong>（2008 年成為標準，2013 年更新為 1.1）是 RDF 的查詢語言。它的核心是<strong>圖樣比對</strong>：寫下一些含有變數的三元組樣式，找出資料中所有能讓變數一致的綁定。"),
   ow("sparql", u"選一個範例查詢，或自己修改後執行（這是教學用的迷你引擎）："),
   ("h", u"四種查詢形式"),
   ("t", [u"形式", u"回傳"],
    [[u"SELECT", u"變數綁定的表格"], [u"CONSTRUCT", u"一張新的 RDF 圖（用來轉換資料）"], [u"ASK", u"是或否"], [u"DESCRIBE", u"某個資源的描述"]]),
   ("h", u"常用功能"),
   ("ul", [u"<code>FILTER(?year &gt; 1950 &amp;&amp; lang(?t) = \"zh\")</code>：條件過濾。", u"<code>OPTIONAL { ?b :isbn ?i }</code>：有就填，沒有也不排除（類似 LEFT JOIN）。", u"<code>COUNT、SUM、AVG</code> 搭配 <code>GROUP BY</code>：聚合。", u"<code>?c rdfs:subClassOf+ :Book</code>：<strong>屬性路徑</strong>，+ 表示一次以上、* 表示零次以上——不必推理機也能沿著階層查詢。", u"<code>FILTER NOT EXISTS { … }</code>：資料中不存在（封閉世界的否定）。", u"<code>SERVICE &lt;…&gt; { … }</code>：聯邦查詢，同時查詢遠端的端點。"]),
   PY(u"""
from rdflib import Graph
g = Graph().parse("library.ttl")          # 本地資料

q = '''
PREFIX :     <http://example.org/lib#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?author (COUNT(?b) AS ?n) WHERE {
    ?b a/rdfs:subClassOf* :Book ;          # 屬性路徑：Book 或其任何子類別
       :writtenBy ?author .
    OPTIONAL { ?b :year ?y }
    FILTER(!BOUND(?y) || ?y > 1940)
}
GROUP BY ?author
ORDER BY DESC(?n)
'''
for row in g.query(q):
    print(row.author, row.n)

# 查詢 Wikidata 的公開端點：托爾金（Q892）的作品
from SPARQLWrapper import SPARQLWrapper, JSON
sp = SPARQLWrapper("https://query.wikidata.org/sparql", agent="ontology-course-demo")
sp.setQuery('''
SELECT ?work ?workLabel WHERE {
  ?work wdt:P50 wd:Q892 .                   # P50 = 作者
  SERVICE wikibase:label { bd:serviceParam wikibase:language "zh-tw,zh,en". }
} LIMIT 10''')
sp.setReturnFormat(JSON)
for b in sp.query().convert()["results"]["bindings"]:
    print(b["workLabel"]["value"])
"""),
   ("note", u"SPARQL 與推理", [("p", u"SPARQL 本身只查詢「寫在圖裡」的三元組。要查到推論出來的事實，有兩種做法：先用推理機<strong>物化</strong>結果再查詢（第 30 課），或使用支援推理的三元組資料庫（GraphDB、Stardog、Jena 等）在查詢時推理。")]),
  ],
  u"SPARQL 以圖樣比對查詢 RDF：以含變數的三元組樣式找出一致的綁定。查詢形式有 SELECT、CONSTRUCT、ASK、DESCRIBE；常用 FILTER、OPTIONAL、聚合與 GROUP BY、屬性路徑（+ 與 *）、FILTER NOT EXISTS 與 SERVICE 聯邦查詢。Python 可用 rdflib 查本地圖、用 SPARQLWrapper 查 Wikidata。SPARQL 只查寫在圖中的三元組，推論結果需先物化或使用支援推理的資料庫。",
  [u"OPTIONAL 和一般的三元組樣式有什麼不同？", u"rdfs:subClassOf* 中的星號是什麼意思？", u"為什麼 SPARQL 查不到推論出來的事實？怎麼解決？"]),

lesson(u"SHACL：資料驗證",
  u"開放世界的本體，封閉世界的檢查",
  [u"理解 SHACL 與 OWL 的分工", u"會寫基本的形狀（shape）", u"用 pySHACL 驗證資料"],
  [("p", u"OWL 在開放世界中做推論，無法回答「這份資料是否完整、是否符合規格」（第 29 課）。2017 年 W3C 推出 <strong>SHACL</strong>（Shapes Constraint Language），專門用<strong>封閉世界</strong>的方式驗證 RDF 資料。"),
   ("t", [u"", u"OWL", u"SHACL"],
    [[u"目的", u"描述概念、推論新知識", u"檢查資料是否符合約束"], [u"世界假設", u"開放", u"封閉"], [u"「每本書至少一位作者」遇到沒有作者的書", u"推論：它有某位未知的作者", u"<strong>報錯</strong>：違反約束"],
     [u"「作者的值域是人」遇到作者是一本書", u"推論：那本書也是一個人", u"<strong>報錯</strong>：值不是 Person"]]),
   ("h", u"形狀"),
   ("p", u"SHACL 用<strong>形狀</strong>描述資料應該長什麼樣子："),
   ("ul", [u"<strong>目標</strong>：這個形狀要檢查哪些節點（例如所有 lib:Book 的實例）。", u"<strong>屬性形狀</strong>：某個屬性的值要滿足什麼：個數（sh:minCount、sh:maxCount）、型別（sh:datatype、sh:class）、範圍（sh:minInclusive）、格式（sh:pattern）等。", u"違反時產生一份<strong>驗證報告</strong>，說明哪個節點、哪個屬性、違反了什麼。"]),
   PY(u"""
from rdflib import Graph
from pyshacl import validate

data = Graph().parse(data='''
@prefix lib: <http://example.org/lib#> .
lib:LOTR   a lib:Book ; lib:title "The Lord of the Rings" ; lib:writtenBy lib:Tolkien ; lib:year 1954 .
lib:Silmar a lib:Book ; lib:year "一九七七" .                 # 沒有書名、年份格式錯
lib:Tolkien a lib:Person .
''', format="turtle")

shapes = Graph().parse(data='''
@prefix sh:  <http://www.w3.org/ns/shacl#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix lib: <http://example.org/lib#> .
lib:BookShape a sh:NodeShape ;
    sh:targetClass lib:Book ;
    sh:property [ sh:path lib:title ; sh:minCount 1 ; sh:datatype xsd:string ] ;
    sh:property [ sh:path lib:writtenBy ; sh:minCount 1 ; sh:class lib:Person ] ;
    sh:property [ sh:path lib:year ; sh:datatype xsd:integer ;
                  sh:minInclusive 1450 ; sh:maxInclusive 2100 ] .
''', format="turtle")

conforms, report_graph, report_text = validate(data, shacl_graph=shapes, inference="rdfs")
print(conforms)        # False
print(report_text)     # 列出 Silmar 缺少書名、缺少作者、年份型別錯誤
"""),
   ("h", u"SHACL 的其他功能"),
   ("ul", [u"<strong>SHACL-SPARQL</strong>：用任意 SPARQL 查詢寫自訂約束（例如「借閱日期必須早於到期日」）。", u"<strong>SHACL Rules</strong>：根據形狀產生新三元組。", u"形狀可以拿來<strong>自動產生表單與文件</strong>，因為它精確描述了資料的結構。"]),
   ("note", u"ShEx", [("p", u"另一個類似的語言是 <strong>ShEx</strong>（Shape Expressions），Wikidata 用它來定義各種實體的資料綱要（EntitySchema）。")]),
  ],
  u"SHACL（2017）以封閉世界驗證 RDF 資料，和 OWL 的開放世界推論分工：同樣的約束，OWL 會推論、SHACL 會報錯。形狀由目標與屬性形狀組成，可約束個數、型別、類別、範圍與格式，違反時產生驗證報告。pySHACL 可在 Python 中驗證。SHACL 還支援 SPARQL 自訂約束、規則與自動產生表單；Wikidata 則用類似的 ShEx。",
  [u"同樣是「每本書至少一位作者」，OWL 和 SHACL 的處理方式有什麼不同？", u"寫一個 SHACL 屬性形狀：ISBN 必須恰好一個，且符合 13 位數字格式。", u"為什麼實務上 OWL 和 SHACL 常常一起使用？"]),

lesson(u"鏈結資料與 LOD 雲",
  u"四條原則，把世界的資料連在一起",
  [u"理解鏈結資料四原則", u"認識五星開放資料", u"認識 LOD 雲中的代表資料集"],
  [("p", u"2006 年，柏納斯–李提出比語意網更務實的<strong>鏈結資料</strong>（Linked Data）原則："),
   ("ol", [u"用 IRI 為東西命名。", u"用 HTTP IRI，讓人可以查詢這些名字。", u"有人查詢 IRI 時，用標準格式（RDF、SPARQL）提供有用的資訊。", u"包含連到其他 IRI 的連結，讓人可以發現更多東西。"]),
   ("h", u"五星開放資料"),
   ("t", [u"星等", u"條件", u"例子"],
    [[u"★", u"以開放授權放在網路上（任何格式）", u"掃描的 PDF"], [u"★★", u"結構化資料", u"Excel"], [u"★★★", u"非專有格式", u"CSV"], [u"★★★★", u"用 IRI 標識事物", u"RDF"], [u"★★★★★", u"連結到其他人的資料", u"連到 Wikidata、DBpedia 的 RDF"]]),
   ("h", u"LOD 雲"),
   ("p", u"依照這些原則發布、彼此連結的資料集，形成了 <strong>LOD（Linked Open Data）雲</strong>，涵蓋上千個資料集："),
   ("ul", [u"<strong>DBpedia</strong>：從維基百科資訊框抽取的知識（第 42 課）。", u"<strong>Wikidata</strong>：維基媒體的協作知識庫。", u"<strong>GeoNames</strong>：全球地名。", u"<strong>VIAF</strong>：各國國家圖書館的作者權威檔整合。", u"<strong>UniProt</strong>、<strong>PubChem</strong>：蛋白質與化學物質。", u"各國政府、圖書館、博物館的開放資料。"]),
   ("h", u"owl:sameAs：連結的關鍵"),
   ("p", u"不同資料集對同一個東西有不同的 IRI。用 <code>owl:sameAs</code> 連起來，就能合併它們的描述。但 sameAs 在邏輯上是嚴格的「完全相同」，實務上常被誤用為「大致相同」或「相關」，造成錯誤的推論——這是鏈結資料最常見的品質問題之一。較寬鬆的連結可用 skos:exactMatch、skos:closeMatch。"),
   PY(u"""
import requests
from rdflib import Graph

# 鏈結資料原則 2、3：對 IRI 做 HTTP 請求，透過內容協商取得 RDF
iri = "http://www.wikidata.org/entity/Q892"           # 托爾金
resp = requests.get(iri, headers={"Accept": "text/turtle"}, timeout=30)
g = Graph().parse(data=resp.text, format="turtle")
print(len(g), "triples about Tolkien")

# 原則 4：沿著連結找到其他資料集的 IRI
q = '''SELECT ?o WHERE { ?s <http://www.wikidata.org/prop/direct/P214> ?o }'''   # VIAF ID
print([str(r.o) for r in g.query(q)])
"""),
  ],
  u"鏈結資料四原則：以 IRI 命名、使用可查詢的 HTTP IRI、查詢時提供 RDF 等標準格式、包含指向其他 IRI 的連結。五星開放資料從開放授權逐步提升到連結他人資料。依此發布的資料集形成 LOD 雲，包括 DBpedia、Wikidata、GeoNames、VIAF、UniProt 等。owl:sameAs 是連結的關鍵，但常被誤用，較寬鬆的對應可用 skos:exactMatch 或 closeMatch。",
  [u"一份政府的 CSV 開放資料是幾顆星？要怎麼變成五顆星？", u"為什麼 owl:sameAs 容易被誤用？", u"什麼是內容協商？在鏈結資料中有什麼作用？"]),
]),

(u"模組 G｜上層本體與領域本體", [

lesson(u"上層本體：BFO、DOLCE、SUMO",
  u"所有領域共通的最高層概念",
  [u"理解上層本體的作用", u"比較 BFO、DOLCE 與 SUMO", u"知道何時應該採用上層本體"],
  [("p", u"不同領域的本體如果各自定義「物體」「事件」「性質」，整合時就會對不起來。<strong>上層本體</strong>提供一組所有領域共用的最高層類別，讓各個領域本體掛在同一個骨架上。"),
   ("t", [u"本體", u"開發者", u"特點", u"使用者"],
    [[u"<strong>BFO</strong>（Basic Formal Ontology）", u"巴利・史密斯等", u"實在論立場、極簡（約 35 個類別），2021 年成為 ISO/IEC 21838-2 國際標準", u"OBO Foundry 的數百個生物醫學本體、美國國防部與情報體系"],
     [u"<strong>DOLCE</strong>", u"瓜里諾等（義大利）", u"認知與語言學取向：反映人類的概念化方式", u"語言學、文化資產、部分工程領域"],
     [u"<strong>SUMO</strong>", u"IEEE 工作小組", u"規模大、與 WordNet 對應", u"自然語言處理研究"]]),
   ("h", u"BFO 的最高層"),
   ("t", [u"持續者（continuant）", u"發生者（occurrent）"],
    [[u"<strong>獨立持續者</strong>：物體（人、細胞、汽車）、物體的集合、場所", u"<strong>過程</strong>：手術、心跳、生產流程"], [u"<strong>特化依存持續者</strong>：性質（顏色、質量）、<strong>角色</strong>（病人角色）、<strong>傾向</strong>（易碎性）與<strong>功能</strong>（心臟的泵血功能）", u"<strong>過程邊界</strong>：開始、結束的瞬間"],
     [u"<strong>一般依存持續者</strong>：資訊內容（一份計畫書的內容，可以有很多份拷貝）", u"<strong>時間區域</strong>、<strong>時空區域</strong>"]]),
   ("p", u"注意 BFO 對「角色」的處理：病人角色依存於某個人，可以開始與結束——正好避開了第 25 課的錯誤。"),
   ow("porphyry", u"上層本體可以看成一棵非常抽象的「波菲利之樹」的頂端："),
   PY(u"""
# 載入 BFO（OWL 檔可從 OBO Foundry 取得），把自己的領域類別掛在它下面
from owlready2 import get_ontology, Thing

bfo = get_ontology("http://purl.obolibrary.org/obo/bfo.owl").load()
obo = bfo.get_namespace("http://purl.obolibrary.org/obo/")
MaterialEntity = obo.BFO_0000040          # material entity（物質實體）
Process        = obo.BFO_0000015          # process（過程）

lib = get_ontology("http://example.org/lib.owl")
lib.imported_ontologies.append(bfo)
with lib:
    class PhysicalBook(MaterialEntity): pass        # 實體書是物質實體
    class Borrowing(Process): pass                  # 借閱是一個過程
"""),
   ("note", u"要不要用上層本體？", [("ul", [u"<strong>要</strong>：本體要和其他組織的本體整合、要長期維護、需要嚴謹的語意（生物醫學、國防）。", u"<strong>可以不用</strong>：小型、單一應用、短期的本體；上層本體的哲學區分會增加學習成本。"])]),
  ],
  u"上層本體提供跨領域共用的最高層類別，讓領域本體掛在同一骨架上。BFO 採實在論、約 35 個類別，2021 年成為 ISO/IEC 21838-2，廣用於 OBO Foundry 生物醫學本體與美國國防體系；DOLCE 採認知與語言學取向；SUMO 規模大並對應 WordNet。BFO 最高層分持續者（物體、性質、角色、傾向、功能、資訊內容）與發生者（過程、邊界、時空區域）。整合與長期維護時宜採用。",
  [u"在 BFO 中，「心臟」和「心跳」各屬於哪一類？", u"BFO 怎麼處理「病人」這種角色？", u"什麼情況下可以不用上層本體？"]),

lesson(u"生物醫學：Gene Ontology、SNOMED CT 與 OBO Foundry",
  u"Ontology 最成功的應用領域",
  [u"認識 Gene Ontology 的結構與用途", u"認識 SNOMED CT 與醫療術語", u"理解 OBO Foundry 的原則"],
  [("h", u"Gene Ontology（GO）"),
   ("p", u"1998 年，果蠅、酵母菌、小鼠三個模式生物資料庫的研究者發現，彼此描述基因功能的用詞不一致，無法比較。他們建立了 <strong>Gene Ontology</strong>，用統一的詞彙描述基因產物的功能，分成三個獨立的分支："),
   ("t", [u"分支", u"描述", u"例子"],
    [[u"分子功能（MF）", u"分子層次的活性", u"ATP 結合、激酶活性"], [u"生物過程（BP）", u"多個分子功能組成的生物程序", u"細胞分裂、DNA 修復"], [u"細胞組成（CC）", u"在細胞中的位置", u"細胞核、粒線體膜"]]),
   ("p", u"GO 有數萬個術語，以 is_a、part_of、regulates 等關係連成有向無環圖。研究者最常用它做<strong>富集分析</strong>：一群在實驗中表現量改變的基因，是否特別集中在某些功能上？"),
   ("h", u"SNOMED CT"),
   ("p", u"<strong>SNOMED CT</strong> 是全球最大的臨床醫學術語系統，包含數十萬個概念（疾病、症狀、手術、藥物、身體結構……），以描述邏輯（OWL 2 EL 的子集）定義。例如「細菌性肺炎」被定義為：肺炎 ⊓ ∃致病因子.細菌 ⊓ ∃發現部位.肺結構。推理機據此自動算出它的所有上層類別。"),
   ("p", u"電子病歷系統用 SNOMED CT 編碼，不同醫院的紀錄才能互相理解、做研究與統計。台灣衛福部的電子病歷交換與 FHIR 標準推動也涉及 SNOMED CT、LOINC（檢驗項目）等國際術語。"),
   ("h", u"OBO Foundry"),
   ("p", u"<strong>OBO Foundry</strong> 是一個生物醫學本體的協作社群，制定共同原則：開放授權、共用 BFO 上層本體、每個術語有唯一的 ID 與文字定義、明確的範圍、不重複造輪子（例如解剖用 Uberon、化學用 ChEBI、疾病用 MONDO）。"),
   PY(u"""
# 用 pronto 讀取 Gene Ontology（OBO 格式），找一個術語的所有上層類別
import pronto
go = pronto.Ontology("http://purl.obolibrary.org/obo/go/go-basic.obo")

term = go["GO:0006281"]                       # DNA repair（DNA 修復）
print(term.name, "|", term.definition)
for sup in term.superclasses(distance=None):  # 沿 is_a 往上
    print("  ⊑", sup.id, sup.name)

# 富集分析通常用專門套件（如 goatools），比較某組基因的 GO 註記與背景分布
"""),
   ("note", u"為什麼生物醫學特別成功", [("ul", [u"領域知識龐大、精確，而且有共同的科學基礎。", u"資料整合需求極強：基因、蛋白質、疾病、藥物分散在數千個資料庫。", u"有長期的公共資金與學術社群支持。"])]),
  ],
  u"Gene Ontology 1998 年由多個模式生物資料庫建立，分為分子功能、生物過程、細胞組成三支，以 is_a、part_of、regulates 連成有向無環圖，常用於基因富集分析。SNOMED CT 是最大的臨床術語系統，以 OWL 2 EL 子集定義數十萬概念並自動分類，是電子病歷互通的基礎。OBO Foundry 制定開放、共用 BFO、唯一 ID、不重複造輪子等原則。生物醫學因知識精確、整合需求強與長期支持而最成功。",
  [u"Gene Ontology 的三個分支各描述什麼？", u"SNOMED CT 怎麼用描述邏輯定義「細菌性肺炎」？", u"OBO Foundry 為什麼強調「不重複造輪子」？"]),

lesson(u"schema.org 與 Google 知識圖譜",
  u"搜尋引擎讓語意網走進了每一個網頁",
  [u"認識 schema.org 的起源與用途", u"理解結構化資料如何影響搜尋結果", u"認識 Google 知識圖譜"],
  [("p", u"2011 年，Google、Bing、Yahoo（隨後 Yandex 加入）共同推出 <strong>schema.org</strong>：一套描述網頁內容的共同詞彙。網站在 HTML 中嵌入結構化資料，搜尋引擎就能理解「這是一份食譜、這是一個活動、這是一項產品」。"),
   ("h", u"為什麼成功"),
   ("ul", [u"<strong>有明確的回報</strong>：標註了結構化資料，搜尋結果就可能出現星等評分、價格、活動時間等「複合式搜尋結果」，點擊率更高。", u"<strong>簡單</strong>：不需要懂 OWL，寫一段 JSON-LD 就好。", u"<strong>務實的設計</strong>：類別階層很淺、屬性很寬鬆（例如 author 的值可以是 Person 或 Organization），容忍不完美的資料。"]),
   ("h", u"常見的類型"),
   ("t", [u"類型", u"常見屬性", u"搜尋結果的呈現"],
    [[u"Product", u"name、brand、offers（price、availability）、aggregateRating", u"價格與庫存、評分星等"], [u"Recipe", u"recipeIngredient、cookTime、nutrition", u"食譜卡片"], [u"Event", u"startDate、location、offers", u"活動清單"],
     [u"LocalBusiness", u"address、openingHours、geo", u"地圖與營業時間"], [u"FAQPage、HowTo", u"mainEntity、step", u"展開式問答"], [u"Organization", u"logo、sameAs（連到社群帳號）", u"知識面板"]]),
   PY(u"""
import json
# 產生一段放在網頁 <script type="application/ld+json"> 中的產品結構化資料
product = {
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "手沖咖啡壺 600ml",
    "brand": {"@type": "Brand", "name": "晨光器物"},
    "offers": {"@type": "Offer", "price": "1280", "priceCurrency": "TWD",
               "availability": "https://schema.org/InStock"},
    "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.6", "reviewCount": "87"},
}
print('<script type="application/ld+json">' + json.dumps(product, ensure_ascii=False) + "</script>")
"""),
   ("h", u"Google 知識圖譜"),
   ("p", u"2012 年，Google 推出知識圖譜，口號是「things, not strings」（是事物，不是字串）。搜尋「托爾金」時右側出現的知識面板——生卒年、作品、相關人物——就來自知識圖譜。它整合了 Freebase（Google 2010 年收購的協作知識庫，後來資料移轉到 Wikidata）、維基百科、schema.org 標註與授權資料。"),
   ("note", u"知識圖譜的商業化", [("p", u"之後，「知識圖譜」成為產業界的流行詞：亞馬遜的產品圖譜、LinkedIn 的經濟圖譜、各大銀行的客戶與風險圖譜。它們多半不使用完整的 OWL 推理，但核心概念——用實體與關係組織資料、有一套明確的綱要——和本體一脈相承（第 51 課）。")]),
  ],
  u"2011 年各大搜尋引擎推出 schema.org，網站以 JSON-LD 嵌入結構化資料，即可在搜尋結果中呈現評分、價格、活動等。它因有明確回報、簡單、設計務實而成功，常見類型有 Product、Recipe、Event、LocalBusiness、FAQPage、Organization。Google 2012 年推出知識圖譜，以「是事物不是字串」為口號，整合 Freebase、維基百科與 schema.org，帶動產業界的知識圖譜熱潮。",
  [u"schema.org 成功的原因是什麼？", u"為一家咖啡店寫出 LocalBusiness 結構化資料需要哪些屬性？", u"「things, not strings」是什麼意思？"]),

lesson(u"Wikidata 與 DBpedia",
  u"全世界最大的開放知識圖譜",
  [u"認識 Wikidata 的資料模型", u"理解限定詞與參考來源", u"認識 DBpedia 與兩者的差別"],
  [("h", u"Wikidata"),
   ("p", u"Wikidata 2012 年由維基媒體基金會推出，是一個任何人都能編輯的結構化知識庫，存放了一億個以上的項目。它是維基百科各語言版本的資訊框、各種 AI 助理與搜尋引擎的重要資料來源。"),
   ("h", u"資料模型"),
   ("t", [u"元素", u"識別碼", u"例子"],
    [[u"項目（item）", u"Q 開頭", u"Q892 托爾金、Q15228 魔戒"], [u"屬性（property）", u"P 開頭", u"P50 作者、P569 出生日期、P31 是…的實例"], [u"陳述", u"項目 + 屬性 + 值", u"Q15228 P50 Q892"],
     [u"限定詞", u"附加在陳述上", u"「開始時間」「結束時間」「排名」"], [u"參考來源", u"附加在陳述上", u"「來自哪本書、哪個網站」"], [u"排名", u"首選／一般／不建議", u"同一屬性有多個值時，哪個是目前正確的"]]),
   ("p", u"這個模型比單純的 RDF 三元組豐富：每個陳述都可以有時間、來源與可信度，正好解決了第 25 課提到的時間與出處問題。匯出成 RDF 時，Wikidata 用具體化的方式表示陳述。"),
   ("h", u"P31 與 P279"),
   ("p", u"Wikidata 沒有強制使用 OWL，而是用兩個屬性表示類別結構：<strong>P31</strong>（是…的實例，對應 rdf:type）與 <strong>P279</strong>（是…的子類別，對應 rdfs:subClassOf）。因為是群眾協作，階層中常有不一致之處，研究者會用推理與 SHACL／ShEx 工具找出問題。"),
   PY(u"""
from SPARQLWrapper import SPARQLWrapper, JSON
sp = SPARQLWrapper("https://query.wikidata.org/sparql", agent="ontology-course-demo")

# 出生在台灣、職業是作家的人，依出生日期排序（含限定詞的寫法見 p:/ps:/pq:）
sp.setQuery('''
SELECT ?p ?pLabel ?birth WHERE {
  ?p wdt:P31 wd:Q5 ;              # 是人類
     wdt:P106 wd:Q36180 ;         # 職業：作家
     wdt:P19/wdt:P17 wd:Q865 ;    # 出生地所屬國家：台灣（Q865）
     wdt:P569 ?birth .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "zh-tw,zh,en". }
} ORDER BY ?birth LIMIT 20''')
sp.setReturnFormat(JSON)
for b in sp.query().convert()["results"]["bindings"]:
    print(b["birth"]["value"][:10], b["pLabel"]["value"])
"""),
   ("h", u"DBpedia"),
   ("p", u"<strong>DBpedia</strong>（2007 年起，萊比錫大學與柏林自由大學等）用程式從維基百科的資訊框<strong>自動抽取</strong>結構化資料，並建立 DBpedia 本體。它是 LOD 雲的中心節點之一。"),
   ("t", [u"", u"Wikidata", u"DBpedia"],
    [[u"資料來源", u"人工直接編輯（加上機器人）", u"從維基百科自動抽取"], [u"語言", u"單一知識庫、多語標籤", u"依維基百科語言版本分開抽取"], [u"出處", u"每個陳述可附參考來源", u"來自維基百科頁面"], [u"更新", u"即時", u"定期重新抽取"]]),
  ],
  u"Wikidata 2012 年推出，是可協作編輯的結構化知識庫，項目以 Q、屬性以 P 編號，陳述可附限定詞、參考來源與排名，解決時間與出處問題，類別結構以 P31（實例）與 P279（子類別）表示。可透過 SPARQL 端點查詢。DBpedia 自 2007 年從維基百科資訊框自動抽取資料並建立本體，是 LOD 雲中心節點；兩者在資料來源、多語處理、出處與更新方式上不同。",
  [u"Wikidata 的 P31 和 P279 各對應 RDF 的什麼？", u"限定詞與參考來源解決了 RDF 三元組的什麼問題？", u"Wikidata 和 DBpedia 的資料來源有什麼不同？"]),

lesson(u"金融：FIBO",
  u"讓銀行、監理機關說同一種語言",
  [u"了解 FIBO 的緣起與範圍", u"理解金融本體在監理與風險管理的用途", u"認識金融領域的其他標準"],
  [("p", u"2008 年金融危機時，監理機關發現一個驚人的事實：銀行無法快速回答「我們對雷曼兄弟及其所有子公司的總曝險是多少？」因為交易對手、法人、金融工具散落在數百個系統中，各自用不同的方式定義。"),
   ("p", u"<strong>FIBO</strong>（Financial Industry Business Ontology）由企業資料管理協會（EDM Council）與物件管理組織（OMG）合作開發，用 OWL 定義金融業的概念。"),
   ("h", u"FIBO 的模組"),
   ("t", [u"模組", u"內容"],
    [[u"FND（基礎）", u"協議、契約、當事人、貨幣、日期等"], [u"BE（商業實體）", u"法人、公司、所有權與控制關係"], [u"FBC（金融商業與商務）", u"金融服務、監理機構、產品"],
     [u"SEC（證券）", u"股票、債券、證券識別碼"], [u"DER（衍生性商品）", u"選擇權、期貨、交換"], [u"LOAN（貸款）", u"房貸、消費貸款"], [u"IND（指數與指標）", u"利率、經濟指標"]]),
   ("h", u"關鍵應用：法人與控制關係"),
   ("p", u"要算出對某集團的總曝險，就要知道誰控制誰。在 FIBO 中，「控制」可以沿著所有權鏈推理："),
   F(r"\text{hasMajorityOwner} \sqsubseteq \text{isControlledBy},\qquad \text{isControlledBy} \circ \text{isControlledBy} \sqsubseteq \text{isUltimatelyControlledBy}"),
   ("p", u"全球法人識別碼（<strong>LEI</strong>，20 碼）制度在 2012 年後建立，每個參與金融交易的法人都有唯一的 LEI，並揭露直接與最終母公司。LEI 資料加上本體，就能自動算出集團結構。"),
   PY(u"""
# 用 SPARQL 屬性路徑沿著控制鏈找出最終母公司，並加總曝險
from rdflib import Graph
g = Graph().parse(data='''
@prefix : <http://example.org/fin#> .
:SubA  :isControlledBy :HoldCo .
:SubB  :isControlledBy :SubA .
:HoldCo :isControlledBy :ParentGroup .
:Loan1 :borrower :SubB ; :exposure 120 .
:Loan2 :borrower :SubA ; :exposure 80 .
:Loan3 :borrower :OtherCorp ; :exposure 50 .
''', format="turtle")
q = '''
SELECT (SUM(?e) AS ?total) WHERE {
  ?loan :borrower ?b ; :exposure ?e .
  ?b :isControlledBy* :ParentGroup .          # 零次或多次：集團內任何一家
}'''
print(list(g.query(q, initNs={"": "http://example.org/fin#"})))   # 200
"""),
   ("h", u"其他金融標準"),
   ("ul", [u"<strong>ISO 20022</strong>：金融訊息（跨境支付、證券交易）的資料模型與訊息標準。", u"<strong>BIAN</strong>：銀行業服務架構。", u"監理科技（RegTech）：用本體把法規條文對應到資料，自動產生監理報表。"]),
  ],
  u"2008 年金融危機暴露出銀行無法快速彙總對集團的曝險，因為各系統定義不一。FIBO 由 EDM Council 與 OMG 以 OWL 定義金融概念，分為基礎、商業實體、金融商業、證券、衍生性商品、貸款、指數等模組。控制關係可沿所有權鏈推理，搭配 2012 年後建立的 20 碼 LEI 制度即可自動算出集團結構與曝險。其他標準包括 ISO 20022、BIAN 與監理科技應用。",
  [u"2008 年金融危機暴露了什麼樣的資料問題？", u"LEI 是什麼？和本體怎麼搭配？", u"為什麼「控制」關係適合用角色鏈或屬性路徑表示？"]),

lesson(u"工程與製造：IFC/BIM 與工業 4.0",
  u"建築、工廠與供應鏈中的本體",
  [u"認識 IFC 與 ifcOWL", u"認識工業 4.0 的資產管理殼", u"理解本體在製造業的角色"],
  [("h", u"建築：IFC 與 BIM"),
   ("p", u"建築資訊模型（BIM）需要在建築師、結構技師、機電、營造廠、業主之間交換資料。<strong>IFC</strong>（Industry Foundation Classes，ISO 16739）由 buildingSMART 制定，定義了牆、梁、柱、門、空間、管線等上千個類別及其關係。"),
   ("ul", [u"IFC 原本是以 EXPRESS 語言定義的資料模型。", u"<strong>ifcOWL</strong> 把 IFC 轉成 OWL，讓建築資料能和其他鏈結資料（地理、能源、產品）整合。", u"<strong>BOT</strong>（Building Topology Ontology）是 W3C 社群提出的輕量建築本體：基地、建築、樓層、空間、元件，以及包含、相鄰等關係。", u"<strong>Brick Schema</strong>：描述建築中的設備與感測器（空調、照明、溫度計），讓能源管理軟體能跨大樓使用。"]),
   ("h", u"製造：工業 4.0"),
   ("p", u"德國提出的工業 4.0 中，每一台機器、每一個零件都要有<strong>數位分身</strong>。標準化的方式是<strong>資產管理殼</strong>（Asset Administration Shell, AAS）：用一組標準的「子模型」描述資產（銘牌、技術資料、維護紀錄、碳足跡），並引用 <strong>ECLASS</strong> 或 IEC 61360 的標準化屬性定義。"),
   ("ul", [u"<strong>OPC UA</strong>：工廠設備的通訊標準，其資訊模型本身就是一套物件導向的「本體」。", u"<strong>ISO 15926</strong>：石化與流程工廠的生命週期資料，採用四維主義的上層本體（第 12 課）。", u"<strong>產業本體</strong>：例如工業本體鑄造所（IOF）以 BFO 為基礎，建立製造、維護、供應鏈的共用本體。"]),
   PY(u"""
# 用 Brick Schema 描述一間會議室的空調與感測器（Brick 是 RDF/OWL 本體）
from rdflib import Graph, Namespace, RDF
BRICK = Namespace("https://brickschema.org/schema/Brick#")
BLDG  = Namespace("http://example.org/building#")
g = Graph(); g.bind("brick", BRICK)

g.add((BLDG.Room301, RDF.type, BRICK.Room))
g.add((BLDG.VAV3,    RDF.type, BRICK.Variable_Air_Volume_Box))
g.add((BLDG.VAV3,    BRICK.feeds, BLDG.Room301))
g.add((BLDG.T301,    RDF.type, BRICK.Zone_Air_Temperature_Sensor))
g.add((BLDG.T301,    BRICK.isPointOf, BLDG.Room301))

# 能源管理程式只要查「哪些房間有溫度感測器」，不必知道每棟大樓的點位命名規則
q = '''SELECT ?room ?s WHERE { ?s a brick:Zone_Air_Temperature_Sensor ; brick:isPointOf ?room }'''
print(list(g.query(q, initNs={"brick": BRICK})))
"""),
   ("note", u"為什麼製造業需要本體", [("p", u"一間工廠可能有上千個感測器、數十種設備品牌、多套系統（MES、ERP、維護系統）。每個系統的點位命名都不一樣（「T_301_ZN」「Room301Temp」…）。本體讓分析與 AI 應用寫一次就能在所有工廠使用——這也是 Palantir 在製造業的切入點（第 63 課）。")]),
  ],
  u"建築領域以 buildingSMART 的 IFC（ISO 16739）交換 BIM 資料，ifcOWL 將其轉為 OWL，另有輕量的 BOT 與描述設備感測器的 Brick Schema。製造領域的工業 4.0 以資產管理殼的標準子模型與 ECLASS 屬性描述數位分身，另有 OPC UA 資訊模型、四維主義的 ISO 15926 與以 BFO 為基礎的 IOF。本體讓分析與 AI 應用跨大樓、跨工廠重用。",
  [u"IFC 和 ifcOWL 有什麼不同？", u"什麼是資產管理殼？", u"為什麼點位命名不一致是工廠導入 AI 的障礙？"]),

lesson(u"政府與開放資料",
  u"DCAT、跨機關資料交換，以及台灣的資料標準",
  [u"認識 DCAT 與資料目錄", u"理解政府資料標準化的挑戰", u"認識台灣的政府開放資料與資料標準"],
  [("h", u"DCAT：描述資料集的詞彙"),
   ("p", u"各國政府都有開放資料平台，但每個平台描述資料集的方式不同。W3C 的 <strong>DCAT</strong>（Data Catalog Vocabulary）提供共同的詞彙：資料目錄（Catalog）、資料集（Dataset）、發布形式（Distribution）、資料服務，以及標題、主題、發布機關、授權、更新頻率等屬性。歐盟在此基礎上制定 DCAT-AP，讓會員國的資料目錄可以彙整搜尋。"),
   PY(u"""
from rdflib import Graph, Namespace, Literal, URIRef, RDF
from rdflib.namespace import DCAT, DCTERMS

EX = Namespace("http://example.org/data#")
g = Graph(); g.bind("dcat", DCAT); g.bind("dct", DCTERMS)

ds = EX.AirQuality
g.add((ds, RDF.type, DCAT.Dataset))
g.add((ds, DCTERMS.title, Literal("空氣品質監測小時值", lang="zh-TW")))
g.add((ds, DCTERMS.publisher, EX.EnvironmentAgency))
g.add((ds, DCAT.keyword, Literal("PM2.5", lang="zh-TW")))
g.add((ds, DCTERMS.license, URIRef("https://data.gov.tw/license")))

dist = EX.AirQualityCSV
g.add((ds, DCAT.distribution, dist))
g.add((dist, RDF.type, DCAT.Distribution))
g.add((dist, DCAT.mediaType, URIRef("https://www.iana.org/assignments/media-types/text/csv")))
print(g.serialize(format="turtle"))
"""),
   ("h", u"跨機關的語意互通"),
   ("ul", [u"<strong>核心詞彙</strong>：歐盟的 Core Person、Core Business、Core Location 等，讓各國的「人」「企業」「地址」能對應。", u"<strong>英國</strong>：政府發布統一的資料標準與登記簿（registers）。", u"<strong>美國</strong>：NIEM（國家資訊交換模型）讓聯邦、州、地方機關在司法、國安、急難等領域交換資料。"]),
   ("h", u"台灣"),
   ("ul", [u"<strong>政府資料開放平臺</strong>（data.gov.tw）彙整各機關的開放資料集，並有統一的詮釋資料欄位與政府資料開放授權條款。", u"<strong>資料標準</strong>：國家發展委員會等單位推動各領域的資料標準（例如地址、交通、觀光的共通格式），以減少同一資料各機關各自定義的問題。", u"<strong>地理資訊</strong>：國土資訊系統（NGIS）與 TGOS 地理圖資雲服務提供門牌地址、行政區等共用的參考資料。", u"<strong>醫療</strong>：衛福部推動以 HL7 FHIR 為基礎的醫療資料交換，搭配國際術語標準（第 40 課）。"]),
   ("note", u"開放資料的星等提升", [("p", u"台灣的開放資料多以 CSV、JSON 發布（三顆星）。要提升到五顆星，關鍵是：用穩定的 IRI 標識行政區、機關、門牌等共通實體，並連結到 Wikidata 或國際標準代碼。這正是本體與鏈結資料能貢獻的地方。")]),
  ],
  u"W3C 的 DCAT 以 Catalog、Dataset、Distribution、資料服務等詞彙描述資料集，歐盟延伸為 DCAT-AP 以彙整各國目錄。跨機關互通有歐盟核心詞彙、英國登記簿、美國 NIEM。台灣有政府資料開放平臺與統一授權、各領域資料標準、NGIS 與 TGOS 共用圖資，以及以 FHIR 為基礎的醫療資料交換。提升到五星的關鍵是以穩定 IRI 標識共通實體並連結國際標準。",
  [u"DCAT 中 Dataset 和 Distribution 有什麼不同？", u"為什麼各機關需要共通的「地址」定義？", u"台灣的開放資料要從三顆星提升到五顆星，需要做什麼？"]),
]),
]
