# -*- coding: utf-8 -*-
"""Ontology：參考頁——互動實驗室、語法與邏輯速查、名詞中英對照。"""
from ont_common import ONTLIB, LS, ow, KATEX, M

LAB = {
    "file": "lab.html", "title": u"Ontology 互動實驗室", "h1": u"Ontology 互動實驗室", "icon": u"🧪",
    "description": u"分類法對照、波菲利之樹、三元組建構器、規則推理、描述邏輯分類器、開放與封閉世界、迷你 SPARQL、序列化格式、Palantir 式 Ontology 模擬與時間軸",
    "body": [
        ("raw", u"<script>%s</script>" % ONTLIB),
        ("p", u"把課程中的互動工具集中在這裡，方便隨時回來練習。每一個都附上對應的課。"),
        ("h", u"1. 分類法與 Ontology 對照（第 3 課）"), ow("taxo"),
        ("h", u"2. 波菲利之樹：屬加種差（第 7、39 課）"), ow("porphyry"),
        ("h", u"3. 圖書館資源的定義（第 4 課）"), ow("porphyry", set="lib"),
        ("h", u"4. 三元組圖譜建構器（第 4、32 課）"), ow("triples"),
        ("h", u"5. 規則推理（第 15、20、22、23、34 課）"), ow("reason"),
        ("h", u"6. 描述邏輯分類器（第 24、27 課）"), ow("classify"),
        ("h", u"7. 開放世界與封閉世界（第 29 課）"), ow("owa"),
        ("h", u"8. 迷你 SPARQL 練習場（第 36 課）"), ow("sparql"),
        ("h", u"9. 序列化格式（第 33 課）"), ow("serial"),
        ("h", u"10. Palantir 式 Ontology 模擬：航空公司（第 60、62 課）"), ow("palantir"),
        ("h", u"11. Palantir 時間軸（第 55 課）"), ow("timeline"),
    ],
}

SYNTAX = {
    "file": "syntax.html", "title": u"語法與邏輯速查", "h1": u"語法與邏輯速查", "icon": u"📋",
    "description": u"描述邏輯符號與 OWL 對照、RDFS 推論規則、Turtle、SPARQL、SHACL 與 Python 套件速查",
    "body": [
        ("raw", KATEX),
        ("h", u"描述邏輯與 OWL 對照"),
        ("t", [u"描述邏輯", u"OWL（Manchester 語法）", u"意思", u"課"], [
            [M(r"C \sqcap D"), u"C and D", u"交集", LS(27)],
            [M(r"C \sqcup D"), u"C or D", u"聯集", LS(27)],
            [M(r"\neg C"), u"not C", u"補集", LS(27)],
            [M(r"\exists R.C"), u"R some C", u"至少有一個 R 指向 C", LS(23)],
            [M(r"\forall R.C"), u"R only C", u"所有 R 都指向 C", LS(23)],
            [M(r"\geq n\, R.C"), u"R min n C", u"至少 n 個", LS(23)],
            [M(r"\leq n\, R.C"), u"R max n C", u"至多 n 個", LS(23)],
            [M(r"\{a, b\}"), u"{a, b}", u"列舉", LS(35)],
            [M(r"C \sqsubseteq D"), u"C SubClassOf: D", u"子類別", LS(20)],
            [M(r"C \equiv D"), u"C EquivalentTo: D", u"等價（定義）", LS(24)],
            [M(r"C \sqcap D \sqsubseteq \bot"), u"DisjointClasses: C, D", u"互斥", LS(25)],
            [M(r"R \circ S \sqsubseteq T"), u"T SubPropertyChain: R o S", u"角色鏈", LS(35)],
            [M(r"R \equiv S^-"), u"R InverseOf: S", u"反向屬性", LS(22)],
            [M(r"\mathrm{Trans}(R)"), u"Characteristics: Transitive", u"傳遞", LS(22)],
        ]),
        ("h", u"描述邏輯家族命名"),
        ("t", [u"字母", u"增加的構造", u"課"], [
            [u"AL", u"交集、原子否定、存在（受限）、全稱", LS(27)], [u"C", u"任意補集（AL + C = ALC）", LS(27)], [u"S", u"ALC + 傳遞角色", LS(27)],
            [u"H", u"角色階層", LS(27)], [u"R", u"角色鏈等複雜角色公理", LS(27)], [u"O", u"列舉（名義個體）", LS(27)],
            [u"I", u"反向角色", LS(27)], [u"N／Q", u"基數／限定基數", LS(27)], [u"(D)", u"資料型別", LS(27)],
        ]),
        ("p", u"OWL 2 DL 對應 SROIQ(D)；OWL 2 EL、QL、RL 是三種較輕量、推理較快的子語言（第 30 課）。"),
        ("h", u"RDFS 推論規則"),
        ("t", [u"規則", u"前提", u"結論"], [
            [u"rdfs2", u"P domain C；x P y", u"x type C"], [u"rdfs3", u"P range C；x P y", u"y type C"],
            [u"rdfs5", u"P subPropertyOf Q；Q subPropertyOf R", u"P subPropertyOf R"], [u"rdfs7", u"P subPropertyOf Q；x P y", u"x Q y"],
            [u"rdfs9", u"A subClassOf B；x type A", u"x type B"], [u"rdfs11", u"A subClassOf B；B subClassOf C", u"A subClassOf C"],
        ]),
        ("h", u"Turtle 速查"),
        ("t", [u"寫法", u"意思"], [
            [u"<code>@prefix ex: &lt;http://example.org/&gt; .</code>", u"宣告前綴"], [u"<code>ex:a ex:p ex:b .</code>", u"一個三元組"],
            [u"<code>ex:a ex:p ex:b ; ex:q ex:c .</code>", u"分號：同主詞，下一個述詞"], [u"<code>ex:a ex:p ex:b , ex:c .</code>", u"逗號：同主詞與述詞，下一個受詞"],
            [u"<code>ex:a a ex:C .</code>", u"a = rdf:type"], [u"<code>[ ex:p ex:b ]</code>", u"空白節點"],
            [u"<code>\"魔戒\"@zh-TW</code>", u"帶語言標籤的字串"], [u"<code>\"1954\"^^xsd:gYear</code>", u"帶資料型別的常值"],
        ]),
        ("h", u"SPARQL 速查"),
        ("t", [u"寫法", u"意思", u"課"], [
            [u"<code>SELECT ?x ?y WHERE { … }</code>", u"回傳綁定表格", LS(36)], [u"<code>ASK { … }</code>", u"是或否", LS(36)],
            [u"<code>CONSTRUCT { … } WHERE { … }</code>", u"產生新圖", LS(36)], [u"<code>OPTIONAL { … }</code>", u"左外連接", LS(36)],
            [u"<code>FILTER(?y &gt; 1950)</code>", u"條件過濾", LS(36)], [u"<code>FILTER NOT EXISTS { … }</code>", u"不存在（封閉世界否定）", LS(29)],
            [u"<code>?c rdfs:subClassOf* ?d</code>", u"屬性路徑：零次以上", LS(36)], [u"<code>?a :p/:q ?b</code>", u"屬性路徑：串接", LS(36)],
            [u"<code>COUNT(?x) … GROUP BY ?y</code>", u"聚合", LS(36)], [u"<code>SERVICE &lt;端點&gt; { … }</code>", u"聯邦查詢", LS(36)],
        ]),
        ("h", u"SHACL 速查"),
        ("t", [u"寫法", u"意思"], [
            [u"<code>sh:targetClass ex:Book</code>", u"檢查所有 Book 的實例"], [u"<code>sh:path ex:title</code>", u"針對哪個屬性"],
            [u"<code>sh:minCount 1</code>／<code>sh:maxCount 1</code>", u"個數"], [u"<code>sh:datatype xsd:integer</code>", u"資料型別"],
            [u"<code>sh:class ex:Person</code>", u"值必須是某類別的實例"], [u"<code>sh:pattern \"^\\\\d{13}$\"</code>", u"正規表示式"],
            [u"<code>sh:minInclusive 0</code>", u"數值範圍"], [u"<code>sh:in ( ex:A ex:B )</code>", u"值必須在清單中"],
        ]),
        ("h", u"Python 套件"),
        ("t", [u"套件", u"用途", u"常用"], [
            [u"rdflib", u"RDF 讀寫與 SPARQL", u"<code>Graph().parse()</code>、<code>g.query()</code>、<code>g.serialize()</code>"],
            [u"owlready2", u"OWL 物件化與推理", u"<code>get_ontology()</code>、<code>sync_reasoner()</code>"],
            [u"owlrl", u"RDFS／OWL RL 規則推理", u"<code>DeductiveClosure(OWLRL_Semantics).expand(g)</code>"],
            [u"pyshacl", u"SHACL 驗證", u"<code>validate(data, shacl_graph=shapes)</code>"],
            [u"pronto", u"OBO 本體", u"<code>Ontology(url)</code>、<code>term.superclasses()</code>"],
            [u"SPARQLWrapper", u"遠端端點", u"<code>SPARQLWrapper(url).query().convert()</code>"],
            [u"networkx", u"圖分析", u"<code>shortest_path()</code>、<code>descendants()</code>"],
        ]),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"名詞中英對照", "h1": u"名詞中英對照", "icon": u"📖",
    "description": u"Ontology、語意網、描述邏輯、知識圖譜與 Palantir 相關名詞",
    "body": [
        ("t", [u"中文", u"英文", u"課"], [
            [u"本體論／本體", u"ontology", LS(1)], [u"範疇", u"category", LS(6)], [u"屬加種差", u"genus and differentia", LS(7)],
            [u"共相", u"universal", LS(8)], [u"實在論／唯名論", u"realism / nominalism", LS(8)], [u"分面分類", u"faceted classification", LS(14)],
            [u"語意網路", u"semantic network", LS(15)], [u"框架", u"frame", LS(15)], [u"專家系統", u"expert system", LS(16)],
            [u"類別", u"class", LS(19)], [u"個體／實例", u"individual / instance", LS(19)], [u"子類別", u"subclass", LS(20)],
            [u"部分–整體", u"part-whole / mereology", LS(20)], [u"物件屬性／資料屬性", u"object property / data property", LS(21)], [u"傳遞性", u"transitivity", LS(22)],
            [u"定義域／值域", u"domain / range", LS(23)], [u"公理", u"axiom", LS(24)], [u"包含關係推理", u"subsumption", LS(24)],
            [u"互斥", u"disjointness", LS(25)], [u"一階邏輯", u"first-order logic", LS(26)], [u"描述邏輯", u"description logic", LS(27)],
            [u"術語盒／斷言盒", u"TBox / ABox", LS(27)], [u"推理機", u"reasoner", LS(28)], [u"一致性／可滿足性", u"consistency / satisfiability", LS(28)],
            [u"開放世界假設", u"open world assumption", LS(29)], [u"唯一名稱假設", u"unique name assumption", LS(29)], [u"可判定性", u"decidability", LS(30)],
            [u"語意網", u"Semantic Web", LS(31)], [u"資源描述框架", u"RDF", LS(32)], [u"三元組", u"triple", LS(32)],
            [u"國際化資源識別碼", u"IRI", LS(32)], [u"空白節點", u"blank node", LS(32)], [u"序列化", u"serialization", LS(33)],
            [u"網路本體語言", u"OWL", LS(35)], [u"屬性路徑", u"property path", LS(36)], [u"形狀", u"shape (SHACL)", LS(37)],
            [u"鏈結資料", u"Linked Data", LS(38)], [u"上層本體", u"upper / top-level ontology", LS(39)], [u"持續者／發生者", u"continuant / occurrent", LS(39)],
            [u"知識圖譜", u"knowledge graph", LS(41)], [u"限定詞", u"qualifier (Wikidata)", LS(42)], [u"法人識別碼", u"LEI", LS(43)],
            [u"資產管理殼", u"Asset Administration Shell", LS(44)], [u"資料目錄詞彙", u"DCAT", LS(45)], [u"能力問題", u"competency question", LS(46)],
            [u"本體設計模式", u"ontology design pattern", LS(48)], [u"本體對齊", u"ontology alignment / matching", LS(49)], [u"棄用", u"deprecation", LS(49)],
            [u"實體解析", u"entity resolution", LS(51)], [u"屬性圖", u"property graph", LS(51)], [u"檢索增強生成", u"RAG", LS(52)],
            [u"語意層", u"semantic layer", LS(54)], [u"資料網格", u"data mesh", LS(54)], [u"數位孿生", u"digital twin", LS(54)],
            [u"前線部署工程師", u"forward deployed engineer", LS(57)], [u"直接上市", u"direct listing", LS(58)], [u"物件類型", u"object type", LS(59)],
            [u"連結類型", u"link type", LS(59)], [u"語意元素／動能元素", u"semantic / kinetic elements", LS(59)], [u"動作類型", u"action type", LS(60)],
            [u"寫回", u"writeback", LS(60)], [u"人在迴圈中", u"human-in-the-loop", LS(62)], [u"神經符號 AI", u"neuro-symbolic AI", LS(65)],
        ]),
    ],
}

REFERENCES = [LAB, SYNTAX, GLOSSARY]
