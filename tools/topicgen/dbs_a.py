# -*- coding: utf-8 -*-
"""資料庫系統原理：模組 A 導論（1～3）、B 關聯模型與 SQL（4～14）。"""
from dbs_common import *

MODULES = [
(u"模組 A｜導論", [

lesson(u"為什麼需要資料庫",
  u"Excel 和一堆檔案，到底哪裡不夠用",
  [u"理解直接用檔案存資料的問題", u"認識資料庫管理系統提供的能力", u"建立整門課的問題意識"],
  [("p", u"假設你用一個 Excel 檔管理一家網路商店的訂單。一開始很好用；但當公司長大，問題一個一個出現："),
   ("t", [u"問題", u"例子", u"資料庫怎麼解決"],
    [[u"<strong>同時修改</strong>", u"兩位客服同時修改同一筆訂單，後存檔的人覆蓋了前一個人的修改", u"交易與並行控制（模組 E）"], [u"<strong>當機</strong>", u"存檔到一半斷電，檔案損毀", u"日誌與當機復原（第 34 課）"],
     [u"<strong>資料量</strong>", u"一千萬筆訂單，打開檔案就要好幾分鐘；找一筆要從頭看到尾", u"儲存結構與索引（模組 C）"], [u"<strong>資料不一致</strong>", u"客戶地址存在三個檔案裡，改了一個忘了另外兩個", u"正規化與約束（第 6、12 課）"],
     [u"<strong>複雜查詢</strong>", u"「上個月每個縣市、每種商品的營收」要手動寫一堆公式", u"SQL 與查詢最佳化（模組 B、D）"], [u"<strong>權限</strong>", u"工讀生不該看到客戶的信用卡資料", u"權限管理（第 50 課）"]]),
   ("h", u"資料庫管理系統（DBMS）"),
   ("p", u"DBMS 是專門管理資料的軟體，提供四個核心能力："),
   ("ol", [u"<strong>資料獨立性</strong>：你只要說「要什麼」（SQL），不用管資料在磁碟上怎麼放。", u"<strong>有效率的存取</strong>：索引、快取、查詢最佳化，讓十億筆資料也能毫秒級查詢。", u"<strong>交易</strong>：多人同時讀寫不會互相干擾，當機也不會壞掉（ACID）。", u"<strong>完整性與安全</strong>：約束確保資料正確，權限確保資料不外洩。"]),
   ("note", u"本課程的路線", [("p", u"這門課重在<strong>原理</strong>：除了學會用 SQL，更要理解資料庫內部怎麼存資料（B+ 樹、LSM 樹）、怎麼執行查詢（Join 演算法、最佳化器）、怎麼保證交易正確（鎖、MVCC、WAL），以及怎麼擴展到多台機器（複製、分片、共識）。許多核心結構會用 Python 寫一個簡化版。")]),
  ],
  u"用 Excel 或檔案管理資料，會遇到同時修改互相覆蓋、存檔到一半當機損毀、資料量大時開啟與查找緩慢、同一資料存多處而不一致、複雜查詢難寫，以及缺乏權限控制。資料庫管理系統提供資料獨立性（只說要什麼）、有效率的存取（索引、快取、最佳化）、交易（ACID）與完整性安全。本課程重在原理，理解資料如何儲存、查詢如何執行、交易如何保證正確與如何擴展到多台機器，並以 Python 實作簡化版核心結構。",
  [u"用 Excel 管理大量訂單會遇到哪些問題？", u"什麼是資料獨立性？", u"資料庫管理系統提供哪四個核心能力？"]),

lesson(u"資料庫系統的架構",
  u"從一行 SQL 到磁碟上的位元組",
  [u"認識資料庫的分層架構", u"理解各元件的分工", u"知道後續課程對應到哪一層"],
  [("p", u"一個關聯式資料庫（例如 PostgreSQL、MySQL）內部大致分成幾層："),
   ("t", [u"層", u"元件", u"做什麼", u"課程"],
    [[u"<strong>介面</strong>", u"連線管理、SQL 解析", u"接收 SQL，檢查語法，轉成內部的樹狀結構", u"第 23 課"],
     [u"<strong>查詢處理</strong>", u"改寫、最佳化器、執行器", u"決定怎麼執行（用哪個索引、哪種 Join），然後執行", u"模組 D"],
     [u"<strong>存取方法</strong>", u"資料表、索引（B+ 樹、雜湊）", u"找到需要的資料列", u"第 17～22 課"],
     [u"<strong>緩衝管理</strong>", u"緩衝池（buffer pool）", u"把常用的磁碟頁快取在記憶體", u"第 16 課"],
     [u"<strong>交易管理</strong>", u"鎖管理、MVCC、日誌", u"確保並行正確與當機復原", u"模組 E"],
     [u"<strong>儲存</strong>", u"檔案、頁", u"資料在磁碟上的實際格式", u"第 15、16 課"]]),
   ("h", u"一次查詢的旅程"),
   ("ol", [u"應用程式送出 <code>SELECT * FROM 訂單 WHERE 客戶 = 42</code>。", u"解析器檢查語法，轉成語法樹。", u"最佳化器估計：訂單有一千萬筆，客戶 42 大約有 30 筆，用「客戶」索引比較快。", u"執行器用索引找到 30 筆資料的位置。", u"緩衝池檢查這些頁是否已在記憶體；不在就從磁碟讀進來。", u"結果回傳給應用程式。"]),
   ("h", u"三種部署方式"),
   ("ul", [u"<strong>主從式伺服器</strong>：PostgreSQL、MySQL、Oracle、SQL Server——資料庫是一個獨立的程式，應用程式透過網路連線。", u"<strong>嵌入式</strong>：SQLite、DuckDB——資料庫就是應用程式裡的一個函式庫，資料存在一個檔案裡。SQLite 存在於幾乎每一支手機與每一個瀏覽器中，是全世界部署數量最多的資料庫。", u"<strong>雲端託管</strong>：Amazon RDS／Aurora、Google Cloud SQL、Azure SQL——由雲端業者負責維運。"]),
  ],
  u"關聯式資料庫分為介面（連線與 SQL 解析）、查詢處理（改寫、最佳化器、執行器）、存取方法（資料表與 B+ 樹、雜湊索引）、緩衝管理（緩衝池）、交易管理（鎖、MVCC、日誌）與儲存（檔案與頁）。一次查詢經過解析、最佳化器估計並選擇索引、執行器找資料、緩衝池讀頁、回傳結果。部署方式有主從式伺服器（PostgreSQL、MySQL）、嵌入式（SQLite、DuckDB，SQLite 是部署數量最多的資料庫）與雲端託管。",
  [u"最佳化器在查詢中扮演什麼角色？", u"緩衝池的作用是什麼？", u"為什麼 SQLite 是全世界部署數量最多的資料庫？"]),

lesson(u"資料庫全景",
  u"關聯式、NoSQL、圖、時序、向量、資料倉儲：各解決什麼問題",
  [u"認識主要的資料庫類型", u"理解 OLTP 與 OLAP 的差別", u"建立選型的初步框架"],
  [("h", u"兩大工作負載"),
   ("t", [u"", u"OLTP（交易處理）", u"OLAP（分析處理）"],
    [[u"典型操作", u"下訂單、轉帳、更新會員資料", u"「過去三年每個月、每個地區的營收」"], [u"每次存取", u"少量資料列，很多次", u"大量資料列，次數少"], [u"重點", u"低延遲、高並行、正確性", u"掃描速度、壓縮、平行運算"],
     [u"儲存方式", u"列式儲存（第 17 課）", u"欄式儲存"], [u"代表", u"PostgreSQL、MySQL、Oracle", u"Snowflake、BigQuery、ClickHouse、DuckDB"]]),
   ("h", u"資料庫的種類"),
   ("t", [u"類型", u"資料模型", u"擅長", u"代表"],
    [[u"關聯式", u"資料表、SQL", u"一般業務資料、交易", u"PostgreSQL、MySQL、SQLite"], [u"鍵值", u"鍵 → 值", u"快取、工作階段", u"Redis、DynamoDB"],
     [u"文件", u"JSON 文件", u"結構多變的資料", u"MongoDB"], [u"寬欄", u"列鍵＋大量欄位", u"超大量寫入", u"Cassandra、HBase"],
     [u"圖", u"節點與邊", u"關係與路徑", u"Neo4j"], [u"時序", u"時間戳記＋數值", u"監控、物聯網、金融行情", u"InfluxDB、TimescaleDB"],
     [u"向量", u"高維向量", u"語意搜尋、AI 的 RAG", u"pgvector、Milvus、Pinecone"], [u"分散式 SQL", u"資料表、SQL，跨多台機器", u"全球規模的交易", u"Spanner、CockroachDB、TiDB"]]),
   ("p", u"這些類型的界線越來越模糊：PostgreSQL 有 JSON、全文檢索、向量（pgvector）擴充；MongoDB 支援交易；雲端資料倉儲也能處理半結構化資料。"),
   ("note", u"一個常見的建議", [("p", u"如果不確定，先從 PostgreSQL 開始。它功能完整、穩定、開源，能處理絕大多數的需求；等到真的遇到它處理不了的規模或模式，再引入專門的資料庫（第 51 課）。")]),
  ],
  u"工作負載分為 OLTP（下單、轉帳，少量資料多次存取，重低延遲高並行，列式儲存，如 PostgreSQL、MySQL）與 OLAP（大量資料分析，重掃描、壓縮、平行，欄式儲存，如 Snowflake、BigQuery、ClickHouse、DuckDB）。資料庫類型包括關聯式、鍵值（Redis）、文件（MongoDB）、寬欄（Cassandra）、圖（Neo4j）、時序、向量（pgvector、Milvus）與分散式 SQL（Spanner、CockroachDB、TiDB），界線日益模糊。不確定時先從 PostgreSQL 開始。",
  [u"OLTP 和 OLAP 有什麼不同？", u"為什麼向量資料庫在 AI 時代變得重要？", u"為什麼常有人建議「先用 PostgreSQL」？"]),
]),

(u"模組 B｜關聯模型與 SQL", [

lesson(u"關聯模型：資料表、主鍵與外鍵",
  u"柯德在 1970 年提出的想法，至今仍是主流",
  [u"理解關聯模型的基本元素", u"理解主鍵與外鍵", u"理解參照完整性"],
  [("p", u"1970 年，IBM 的柯德（Edgar Codd）發表論文〈大型共享資料庫的關聯模型〉，提出用<strong>數學上的關聯（集合）</strong>來表示資料。他因此在 1981 年獲得圖靈獎。"),
   ("h", u"基本元素"),
   ("t", [u"數學名詞", u"日常名詞", u"例子"],
    [[u"關聯（relation）", u"資料表", u"學生"], [u"值組（tuple）", u"資料列", u"(1, 王小明, 資工)"], [u"屬性（attribute）", u"欄位", u"姓名"], [u"定義域（domain）", u"型別", u"整數、文字、日期"]]),
   ("h", u"鍵"),
   ("ul", [u"<strong>主鍵</strong>：唯一識別每一列的欄位（或欄位組合），不能重複、不能是 NULL。例如學號。", u"<strong>外鍵</strong>：指向另一個表主鍵的欄位，用來表示關係。例如選課表的「學號」指向學生表。", u"<strong>候選鍵</strong>：所有可以當主鍵的選擇（例如學號、身分證字號）。", u"<strong>自然鍵 vs. 代理鍵</strong>：用真實世界的值（身分證字號）還是系統產生的流水號？實務上多用代理鍵，因為真實世界的值可能改變。"]),
   SQL(u"""
CREATE TABLE 學生 (
    學號   INTEGER PRIMARY KEY,
    姓名   TEXT    NOT NULL,
    系所   TEXT
);
CREATE TABLE 選課 (
    學號   INTEGER REFERENCES 學生(學號),   -- 外鍵
    課程   TEXT,
    成績   INTEGER CHECK (成績 BETWEEN 0 AND 100),
    PRIMARY KEY (學號, 課程)                -- 複合主鍵：同一人不能重複選同一門課
);
"""),
   ("h", u"參照完整性"),
   ("p", u"外鍵保證：選課表裡的每一個學號，都必須存在於學生表中。如果要刪除一位學生，資料庫會拒絕（RESTRICT），或連同他的選課紀錄一起刪除（CASCADE），或把外鍵設為 NULL（SET NULL）——由設計者決定。"),
   ("note", u"為什麼關聯模型能勝出", [("p", u"之前的階層式與網狀資料庫，程式必須知道資料怎麼串在一起，結構一改程式就要重寫。關聯模型只描述資料「是什麼」，查詢「要什麼」，至於「怎麼找」交給資料庫——這就是第 1 課說的資料獨立性。")]),
  ],
  u"1970 年 IBM 的柯德提出以數學關聯（集合）表示資料的關聯模型，1981 年獲圖靈獎。關聯即資料表、值組即資料列、屬性即欄位、定義域即型別。主鍵唯一識別每列且不可為 NULL，外鍵指向另一表的主鍵以表示關係，候選鍵是所有可當主鍵者，實務上多用代理鍵。外鍵保證參照完整性，刪除時可設定 RESTRICT、CASCADE 或 SET NULL。關聯模型只描述資料是什麼、查詢要什麼，怎麼找交給資料庫，因而勝過階層式與網狀資料庫。",
  [u"主鍵和外鍵各有什麼作用？", u"為什麼實務上常用代理鍵而不是自然鍵？", u"關聯模型為什麼能取代早期的階層式資料庫？"]),

lesson(u"ER 模型：從需求畫出資料表",
  u"實體、關係與基數",
  [u"理解實體關係模型", u"理解一對一、一對多、多對多", u"把 ER 圖轉換成資料表"],
  [("p", u"設計資料庫的第一步，不是直接寫 CREATE TABLE，而是釐清需求中有哪些「東西」以及它們的關係。1976 年陳品山（Peter Chen）提出的<strong>實體關係模型</strong>（ER 模型）是最常用的工具。"),
   ("h", u"基本元素"),
   ("ul", [u"<strong>實體</strong>：需求中的名詞——客戶、商品、訂單。", u"<strong>屬性</strong>：實體的特徵——客戶的姓名、電話。", u"<strong>關係</strong>：實體之間的動詞——客戶「下」訂單、訂單「包含」商品。"]),
   ("h", u"基數"),
   ("t", [u"類型", u"例子", u"轉成資料表"],
    [[u"<strong>一對一</strong>", u"員工 — 員工證", u"在其中一個表加外鍵（並設 UNIQUE），或合併成一個表"], [u"<strong>一對多</strong>", u"客戶 — 訂單（一位客戶有很多訂單）", u"在「多」的那一邊加外鍵：訂單.客戶編號"],
     [u"<strong>多對多</strong>", u"訂單 — 商品（一張訂單多種商品，一種商品出現在多張訂單）", u"建立<strong>中介表</strong>：訂單明細（訂單編號、商品編號、數量、單價）"]]),
   SQL(u"""
CREATE TABLE 客戶 (客戶編號 INTEGER PRIMARY KEY, 姓名 TEXT, 電話 TEXT);
CREATE TABLE 商品 (商品編號 INTEGER PRIMARY KEY, 品名 TEXT, 定價 NUMERIC);
CREATE TABLE 訂單 (
    訂單編號 INTEGER PRIMARY KEY,
    客戶編號 INTEGER REFERENCES 客戶,          -- 一對多
    下單時間 TIMESTAMP
);
CREATE TABLE 訂單明細 (                         -- 多對多的中介表
    訂單編號 INTEGER REFERENCES 訂單,
    商品編號 INTEGER REFERENCES 商品,
    數量     INTEGER,
    成交單價 NUMERIC,                            -- 下單當時的價格，和商品現在的定價不同
    PRIMARY KEY (訂單編號, 商品編號)
);
"""),
   ("note", u"一個常見的設計細節", [("p", u"訂單明細裡要存「成交單價」，不能只參照商品表的定價：商品明天漲價，昨天的訂單金額不應該跟著變。區分「現在的狀態」與「當時的事實」，是資料模型設計中最常被忽略的問題之一。")]),
  ],
  u"1976 年陳品山提出的實體關係模型以實體（名詞，如客戶、商品、訂單）、屬性與關係（動詞）描述需求。基數分為一對一（加唯一外鍵或合併）、一對多（在多的一方加外鍵，如訂單.客戶編號）與多對多（建立中介表，如訂單明細）。訂單明細應存成交單價而非只參照商品現價，區分現在的狀態與當時的事實是常被忽略的設計問題。",
  [u"一對多與多對多關係各怎麼轉成資料表？", u"為什麼訂單明細要存「成交單價」？", u"為一個圖書館借閱系統畫出實體與關係。"]),

lesson(u"正規化：1NF 到 BCNF",
  u"一件事只記一次",
  [u"理解資料重複帶來的異常", u"理解函數相依", u"掌握 1NF、2NF、3NF、BCNF"],
  [("h", u"為什麼要正規化"),
   ("p", u"看這張表：(學號, 姓名, 系所, 系主任, 課程, 成績)。系主任的名字在每一位該系學生的每一筆選課中都重複一次。這會造成三種<strong>異常</strong>："),
   ("ul", [u"<strong>更新異常</strong>：換系主任時，要改上千筆，漏改一筆就不一致。", u"<strong>插入異常</strong>：新成立的系還沒有學生，就無法記錄它的系主任。", u"<strong>刪除異常</strong>：某系最後一位學生退學，系主任的資訊也跟著消失。"]),
   ("h", u"函數相依"),
   F(r"X \rightarrow Y"),
   ("p", u"「知道 X 就能唯一決定 Y」。例如 學號 → 姓名、系所 → 系主任、(學號, 課程) → 成績。正規化就是根據函數相依，把表拆開。"),
   ("t", [u"正規形式", u"要求", u"違反的例子"],
    [[u"<strong>1NF</strong>", u"每個欄位都是單一值（不可再分）", u"「電話」欄位存「0912…, 0223…」兩支電話"], [u"<strong>2NF</strong>", u"1NF，且非鍵欄位要相依於<strong>整個</strong>主鍵", u"主鍵 (學號, 課程)，但 姓名 只相依於學號"],
     [u"<strong>3NF</strong>", u"2NF，且非鍵欄位不能透過其他非鍵欄位間接相依於主鍵", u"學號 → 系所 → 系主任（遞移相依）"], [u"<strong>BCNF</strong>", u"每一個決定因子都必須是候選鍵", u"3NF 的少數特殊情況"]]),
   ("p", u"拆成：學生(學號, 姓名, 系所)、系所(系所, 系主任)、選課(學號, 課程, 成績)，每一件事都只記一次。"),
   ("h", u"什麼時候反正規化"),
   ("ul", [u"<strong>讀取遠多於寫入</strong>，而且 Join 很昂貴時（例如報表、資料倉儲的星狀綱要）。", u"<strong>需要歷史快照</strong>時（上一課的成交單價）。", u"反正規化是有意識的取捨：用寫入的複雜度與重複，換取讀取的速度。"]),
  ],
  u"未正規化的表會造成更新異常、插入異常與刪除異常。函數相依 X → Y 表示知道 X 即可唯一決定 Y，正規化據此拆表：1NF 要求欄位單一值，2NF 要求非鍵欄位相依於整個主鍵，3NF 不允許透過非鍵欄位的遞移相依，BCNF 要求每個決定因子都是候選鍵。例如拆成學生、系所、選課三表。讀多寫少且 Join 昂貴（報表、星狀綱要）或需要歷史快照時，可有意識地反正規化。",
  [u"舉例說明更新異常、插入異常、刪除異常。", u"2NF 和 3NF 各解決什麼問題？", u"什麼情況下應該反正規化？"]),

lesson(u"SQL 基礎：SELECT、WHERE、ORDER BY",
  u"宣告式語言：說你要什麼，不說怎麼做",
  [u"掌握 SELECT 的基本語法", u"理解 SQL 的邏輯執行順序", u"理解 NULL 的三值邏輯"],
  [("p", u"SQL 起源於 1970 年代 IBM 的 System R 計畫（最初叫 SEQUEL），1979 年 Oracle 推出第一個商業化的 SQL 資料庫。它是<strong>宣告式</strong>語言：你描述想要的結果，資料庫決定怎麼取得。"),
   SQL(u"""
SELECT 姓名, 系所
FROM   學生
WHERE  系所 IN ('資工', '電機') AND 姓名 LIKE '林%'
ORDER BY 系所, 姓名 DESC
LIMIT  10;
"""),
   ("h", u"邏輯執行順序"),
   ("p", u"SQL 的寫法順序和「邏輯上」的執行順序不同。理解這個順序，就能避開很多錯誤（例如為什麼 WHERE 不能用 SELECT 裡取的別名）："),
   ("ol", [u"FROM／JOIN：決定資料來源", u"WHERE：過濾資料列", u"GROUP BY：分組", u"HAVING：過濾分組", u"SELECT：計算輸出欄位", u"ORDER BY：排序", u"LIMIT：取前幾筆"]),
   ("h", u"NULL：三值邏輯"),
   ("p", u"NULL 代表「未知」或「不適用」，不是 0，也不是空字串。任何和 NULL 的比較，結果都是 UNKNOWN（第三種真假值）："),
   ("ul", [u"<code>NULL = NULL</code> 的結果是 UNKNOWN，不是 TRUE。所以要用 <code>IS NULL</code>。", u"WHERE 只保留結果為 TRUE 的列，UNKNOWN 會被濾掉。", u"<code>NOT IN</code> 的陷阱：如果子查詢結果中有 NULL，<code>x NOT IN (…)</code> 永遠不會是 TRUE，整個查詢可能回傳 0 筆。"]),
   PY(u"""
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript('''
CREATE TABLE 學生 (學號 INTEGER PRIMARY KEY, 姓名 TEXT, 系所 TEXT);
INSERT INTO 學生 VALUES (1,'王小明','資工'), (2,'林小華','電機'), (3,'陳大文',NULL);
''')
print(db.execute("SELECT 姓名 FROM 學生 WHERE 系所 = NULL").fetchall())   # []  永遠找不到
print(db.execute("SELECT 姓名 FROM 學生 WHERE 系所 IS NULL").fetchall())  # [('陳大文',)]
"""),
  ],
  u"SQL 起源於 1970 年代 IBM System R（最初稱 SEQUEL），1979 年 Oracle 推出第一個商業 SQL 資料庫，是宣告式語言。SELECT 搭配 WHERE、IN、LIKE、ORDER BY、LIMIT 使用。邏輯執行順序為 FROM／JOIN、WHERE、GROUP BY、HAVING、SELECT、ORDER BY、LIMIT，因此 WHERE 不能用 SELECT 的別名。NULL 代表未知，與之比較結果為 UNKNOWN，須用 IS NULL；WHERE 只保留 TRUE；子查詢含 NULL 時 NOT IN 可能永遠不成立。",
  [u"為什麼 WHERE 子句不能使用 SELECT 中定義的別名？", u"為什麼 <code>WHERE 欄位 = NULL</code> 找不到任何資料？", u"NOT IN 遇到 NULL 會發生什麼事？"]),

lesson(u"JOIN：把資料表接起來",
  u"內連接、外連接、交叉連接，以及常見陷阱",
  [u"掌握各種 JOIN 的語意", u"理解 JOIN 造成的資料列倍增", u"避開常見的 JOIN 錯誤"],
  [("t", [u"類型", u"結果"],
    [[u"<strong>INNER JOIN</strong>", u"只保留兩邊都對得上的列"], [u"<strong>LEFT JOIN</strong>", u"保留左表所有列；右表對不上的填 NULL"], [u"<strong>RIGHT JOIN</strong>", u"保留右表所有列（等於把左右對調的 LEFT JOIN）"],
     [u"<strong>FULL OUTER JOIN</strong>", u"兩邊所有列都保留"], [u"<strong>CROSS JOIN</strong>", u"笛卡兒積：每一列和另一表的每一列配對"], [u"<strong>自我連接</strong>", u"表和自己連接，例如員工表找出每個人的主管"]]),
   SQL(u"""
-- 每位學生和他的選課；沒選課的學生也要列出來
SELECT s.姓名, e.課程, e.成績
FROM 學生 s
LEFT JOIN 選課 e ON s.學號 = e.學號;

-- 找出「沒有選任何課」的學生（反連接）
SELECT s.姓名
FROM 學生 s
LEFT JOIN 選課 e ON s.學號 = e.學號
WHERE e.學號 IS NULL;
"""),
   ("h", u"常見陷阱"),
   ("ul", [u"<strong>資料列倍增</strong>：一位客戶有 3 張訂單、每張訂單有 4 項商品，連接後這位客戶會出現 12 列。此時再 SUM(訂單金額) 會被重複計算——先聚合再 JOIN，或小心使用 DISTINCT。", u"<strong>LEFT JOIN 被 WHERE 變成 INNER JOIN</strong>：<code>LEFT JOIN 選課 e ON … WHERE e.成績 > 80</code>，沒選課的學生 e.成績 是 NULL，被 WHERE 濾掉了。條件要放在 ON 裡。", u"<strong>忘了連接條件</strong>：變成 CROSS JOIN，一萬筆乘一萬筆就是一億筆。"]),
   ("note", u"JOIN 在內部怎麼做", [("p", u"JOIN 是資料庫最昂貴的操作之一。內部有巢狀迴圈、雜湊、排序合併三種主要演算法，最佳化器會依資料量與索引選擇（第 24 課）。")]),
  ],
  u"JOIN 類型包括只保留對得上列的 INNER JOIN、保留左表所有列並以 NULL 補右表的 LEFT JOIN、RIGHT JOIN、保留雙方所有列的 FULL OUTER JOIN、笛卡兒積 CROSS JOIN 與自我連接。LEFT JOIN 加 WHERE 右表欄位 IS NULL 可找出沒有對應的資料（反連接）。常見陷阱有一對多連接造成資料列倍增使 SUM 重複計算、LEFT JOIN 的右表條件放在 WHERE 使其變成 INNER JOIN，以及忘了連接條件造成巨大的 CROSS JOIN。內部以巢狀迴圈、雜湊、排序合併三種演算法實作。",
  [u"INNER JOIN 與 LEFT JOIN 的結果有什麼不同？", u"怎麼用 LEFT JOIN 找出「沒有訂單的客戶」？", u"為什麼把右表條件放在 WHERE 會讓 LEFT JOIN 變成 INNER JOIN？"]),

lesson(u"聚合：GROUP BY 與 HAVING",
  u"把很多列變成一列",
  [u"掌握聚合函數與 GROUP BY", u"區分 WHERE 與 HAVING", u"理解聚合與 NULL 的關係"],
  [SQL(u"""
SELECT 系所,
       COUNT(*)        AS 學生數,
       AVG(成績)       AS 平均成績,
       MAX(成績)       AS 最高分
FROM 學生 s JOIN 選課 e ON s.學號 = e.學號
WHERE e.課程 <> '體育'            -- 先過濾「資料列」
GROUP BY 系所
HAVING AVG(成績) >= 80            -- 再過濾「分組」
ORDER BY 平均成績 DESC;
"""),
   ("h", u"規則"),
   ("ul", [u"SELECT 中的欄位，要嘛出現在 GROUP BY 裡，要嘛被聚合函數包起來。否則資料庫不知道一組裡的多個值要顯示哪一個。", u"<strong>WHERE</strong> 在分組<strong>之前</strong>過濾資料列，不能用聚合函數。", u"<strong>HAVING</strong> 在分組<strong>之後</strong>過濾，可以用聚合函數。"]),
   ("h", u"聚合與 NULL"),
   ("ul", [u"<code>COUNT(*)</code> 計算列數；<code>COUNT(欄位)</code> 只計算該欄位不是 NULL 的列。", u"<code>SUM</code>、<code>AVG</code> 會忽略 NULL：三個人的成績是 80、NULL、100，AVG 是 90 而不是 60。", u"一列都沒有時，<code>COUNT</code> 回傳 0，<code>SUM</code> 回傳 NULL——用 <code>COALESCE(SUM(x), 0)</code> 處理。"]),
   ("h", u"資料庫內部怎麼分組"),
   ("ul", [u"<strong>雜湊聚合</strong>：用雜湊表，以分組鍵為鍵，邊讀邊累計。速度快，但分組很多時需要大量記憶體。", u"<strong>排序聚合</strong>：先依分組鍵排序，相同的鍵就會相鄰，依序累計即可。若資料已經依索引排序，就特別划算。"]),
   bw("qexec", u"選「GROUP BY 分組」，一步一步看資料怎麼被連接、分組與彙總：", k=u"GROUP BY 分組"),
  ],
  u"聚合函數 COUNT、AVG、MAX 等搭配 GROUP BY 把多列變成一列，SELECT 欄位必須在 GROUP BY 中或被聚合。WHERE 在分組前過濾資料列、不能用聚合函數，HAVING 在分組後過濾、可用聚合函數。COUNT(*) 計算列數、COUNT(欄位) 不計 NULL，SUM 與 AVG 忽略 NULL，無資料時 SUM 回傳 NULL 可用 COALESCE 處理。內部以雜湊聚合（快但耗記憶體）或排序聚合（資料已排序時划算）實作。",
  [u"WHERE 和 HAVING 有什麼不同？", u"三個成績 80、NULL、100，AVG 的結果是多少？為什麼？", u"雜湊聚合和排序聚合各適合什麼情況？"]),

lesson(u"子查詢與 CTE",
  u"把複雜的查詢拆成好讀的步驟",
  [u"掌握子查詢的幾種用法", u"理解相關子查詢", u"使用 CTE 與遞迴 CTE"],
  [("h", u"子查詢"),
   SQL(u"""
-- 純量子查詢：成績高於全體平均的選課
SELECT * FROM 選課 WHERE 成績 > (SELECT AVG(成績) FROM 選課);

-- EXISTS：至少選了一門資料庫課的學生
SELECT 姓名 FROM 學生 s
WHERE EXISTS (SELECT 1 FROM 選課 e WHERE e.學號 = s.學號 AND e.課程 = '資料庫');
"""),
   ("p", u"第二個例子是<strong>相關子查詢</strong>：子查詢裡引用了外層的 s.學號。概念上每一位學生都要執行一次子查詢；但現代的最佳化器通常會把它改寫成「半連接」，效率和 JOIN 差不多。"),
   ("h", u"CTE：WITH 子句"),
   SQL(u"""
WITH 系所平均 AS (
    SELECT s.系所, AVG(e.成績) AS 平均
    FROM 學生 s JOIN 選課 e ON s.學號 = e.學號
    GROUP BY s.系所
)
SELECT s.姓名, e.成績, a.平均
FROM 學生 s
JOIN 選課 e   ON s.學號 = e.學號
JOIN 系所平均 a ON s.系所 = a.系所
WHERE e.成績 > a.平均;          -- 成績高於自己系所平均的人
"""),
   ("p", u"CTE 讓複雜的查詢像寫程式一樣，一步一步命名每個中間結果，可讀性大幅提升。"),
   ("h", u"遞迴 CTE：走訪樹與圖"),
   SQL(u"""
-- 員工(編號, 姓名, 主管編號)：找出某位主管底下的所有人（不論幾層）
WITH RECURSIVE 部屬 AS (
    SELECT 編號, 姓名, 1 AS 層級 FROM 員工 WHERE 主管編號 = 1
    UNION ALL
    SELECT e.編號, e.姓名, d.層級 + 1
    FROM 員工 e JOIN 部屬 d ON e.主管編號 = d.編號
)
SELECT * FROM 部屬;
"""),
  ],
  u"子查詢包括純量子查詢（如成績高於平均）與 EXISTS 子查詢；引用外層欄位的相關子查詢概念上逐列執行，但最佳化器常改寫成半連接。CTE 以 WITH 子句命名中間結果，使複雜查詢像程式一樣逐步可讀，例如先算系所平均再找高於平均者。遞迴 CTE（WITH RECURSIVE）以起始查詢加 UNION ALL 遞迴部分，可走訪樹與圖，例如找出某主管底下所有層級的部屬。",
  [u"什麼是相關子查詢？它的效能一定很差嗎？", u"CTE 相比子查詢有什麼好處？", u"用遞迴 CTE 可以解決哪些類型的問題？"]),

lesson(u"視窗函數：排名、移動平均與累計",
  u"不用把資料列合併，也能做跨列的計算",
  [u"理解視窗函數與 GROUP BY 的差別", u"掌握 PARTITION BY、ORDER BY 與視窗範圍", u"應用排名、前後列比較與移動平均"],
  [("p", u"GROUP BY 把一組資料「壓扁」成一列；<strong>視窗函數</strong>則在保留每一列的同時，看見同一組的其他列。"),
   SQL(u"""
SELECT 姓名, 系所, 成績,
       RANK()       OVER (PARTITION BY 系所 ORDER BY 成績 DESC) AS 系內排名,
       AVG(成績)    OVER (PARTITION BY 系所)                    AS 系所平均,
       成績 - AVG(成績) OVER (PARTITION BY 系所)               AS 與平均差距
FROM 成績表;
"""),
   ("h", u"三個組成"),
   ("ul", [u"<strong>PARTITION BY</strong>：把資料分成幾個「視窗」（類似 GROUP BY，但不壓扁）。", u"<strong>ORDER BY</strong>：視窗內的排序。", u"<strong>框架</strong>：視窗內要看哪幾列，例如 <code>ROWS BETWEEN 6 PRECEDING AND CURRENT ROW</code>（包含自己共 7 列）。"]),
   ("h", u"常用函數"),
   ("t", [u"函數", u"用途", u"例子"],
    [[u"ROW_NUMBER、RANK、DENSE_RANK", u"排名（處理同分的方式不同）", u"每個系的前三名"], [u"LAG、LEAD", u"取前一列、後一列的值", u"和昨天比，股價漲跌多少"],
     [u"SUM … OVER (ORDER BY …)", u"累計", u"今年到目前為止的累計營收"], [u"AVG … ROWS BETWEEN n PRECEDING", u"移動平均", u"股價的 5 日、20 日均線"],
     [u"NTILE", u"分成 n 等分", u"把客戶依消費金額分成十等分"]]),
   SQL(u"""
-- 股價的 5 日均線與日報酬率
SELECT 日期, 收盤價,
       AVG(收盤價) OVER (ORDER BY 日期 ROWS BETWEEN 4 PRECEDING AND CURRENT ROW) AS 五日均線,
       收盤價 / LAG(收盤價) OVER (ORDER BY 日期) - 1                              AS 日報酬
FROM 股價 WHERE 代號 = '2330';
"""),
  ],
  u"視窗函數在保留每一列的同時看見同組其他列，不像 GROUP BY 會壓扁資料。組成包括分割視窗的 PARTITION BY、視窗內排序的 ORDER BY 與指定範圍的框架（如 ROWS BETWEEN 6 PRECEDING AND CURRENT ROW）。常用函數有 ROW_NUMBER、RANK、DENSE_RANK 排名，LAG、LEAD 取前後列，SUM OVER 累計，AVG 搭配框架計算移動平均（如股價 5 日均線），NTILE 分等分。",
  [u"視窗函數和 GROUP BY 有什麼不同？", u"RANK 和 DENSE_RANK 在處理同分時有什麼差別？", u"寫出計算 20 日均線的 SQL。"]),

lesson(u"DDL 與約束：讓資料庫幫你守規則",
  u"型別、NOT NULL、UNIQUE、CHECK、外鍵與 ALTER TABLE",
  [u"掌握建立與修改資料表", u"理解各種約束的作用", u"理解線上修改綱要的挑戰"],
  [SQL(u"""
CREATE TABLE 帳戶 (
    帳號     BIGINT PRIMARY KEY,
    戶名     TEXT        NOT NULL,
    身分證   CHAR(10)    UNIQUE,
    餘額     NUMERIC(14,2) NOT NULL DEFAULT 0 CHECK (餘額 >= 0),
    幣別     CHAR(3)     NOT NULL DEFAULT 'TWD',
    開戶時間 TIMESTAMPTZ NOT NULL DEFAULT now()
);
ALTER TABLE 帳戶 ADD COLUMN 狀態 TEXT NOT NULL DEFAULT '正常';
"""),
   ("h", u"選對型別"),
   ("ul", [u"<strong>金額用 NUMERIC（十進位），不要用 FLOAT</strong>：浮點數無法精確表示 0.1，累加後會出現分毫誤差。", u"時間盡量用帶時區的型別，存 UTC。", u"文字長度不確定時用 TEXT（PostgreSQL 中 TEXT 與 VARCHAR 效能相同）。"]),
   ("h", u"約束是最後一道防線"),
   ("t", [u"約束", u"保證"],
    [[u"NOT NULL", u"一定要有值"], [u"UNIQUE", u"不能重複（資料庫會自動建立索引）"], [u"CHECK", u"符合條件，例如餘額不能是負數"], [u"FOREIGN KEY", u"參照的資料一定存在"], [u"EXCLUDE（PostgreSQL）", u"例如同一間會議室的預約時段不能重疊"]]),
   ("p", u"應用程式也會檢查這些規則，但程式有 bug、有多個服務同時寫入、有人直接在資料庫下指令……只有資料庫的約束能保證「無論如何都成立」。"),
   ("h", u"線上修改綱要"),
   ("p", u"在一個一億筆、持續被寫入的大表上 ALTER TABLE，可能會鎖住整個表好幾個小時。實務上的做法："),
   ("ul", [u"新增可為 NULL 或有預設值的欄位，現代資料庫多半能瞬間完成（只改中繼資料）。", u"建索引用 <code>CREATE INDEX CONCURRENTLY</code>（PostgreSQL）。", u"大改動用工具（例如 gh-ost、pt-online-schema-change）建一個新表、背景複製資料、最後切換。"]),
  ],
  u"DDL 以 CREATE TABLE 與 ALTER TABLE 建立與修改資料表。選型時金額應用 NUMERIC 而非無法精確表示 0.1 的 FLOAT，時間用帶時區型別存 UTC。約束包括 NOT NULL、UNIQUE（自動建索引）、CHECK（如餘額不能為負）、FOREIGN KEY 與 PostgreSQL 的 EXCLUDE（如時段不重疊），是無論程式如何都成立的最後防線。在大表上線上修改綱要可能長時間鎖表，可利用只改中繼資料的新增欄位、CREATE INDEX CONCURRENTLY，或 gh-ost 等工具背景複製後切換。",
  [u"為什麼金額不應該用 FLOAT 型別？", u"既然應用程式會檢查資料，為什麼資料庫還需要約束？", u"在大表上修改綱要有什麼風險？怎麼降低？"]),

lesson(u"檢視、預存程序與觸發器",
  u"把邏輯放在資料庫裡：好處與代價",
  [u"理解檢視與實體化檢視", u"認識預存程序與觸發器", u"評估邏輯放在資料庫的取捨"],
  [("h", u"檢視（View）"),
   SQL(u"""
CREATE VIEW 資工系成績 AS
SELECT s.姓名, e.課程, e.成績
FROM 學生 s JOIN 選課 e ON s.學號 = e.學號
WHERE s.系所 = '資工';

SELECT * FROM 資工系成績 WHERE 成績 >= 90;   -- 像查一般的表一樣
"""),
   ("ul", [u"檢視是一個「存起來的查詢」，不存資料；查詢時展開成原本的 SQL。", u"用途：簡化複雜查詢、限制權限（只讓某些人看到部分欄位）。"]),
   ("h", u"實體化檢視"),
   ("p", u"把查詢結果真的存起來，查詢時直接讀取，速度很快；但資料不會自動更新，需要定期 <code>REFRESH</code>。適合計算昂貴、可以接受稍微過時的報表。"),
   ("h", u"預存程序與觸發器"),
   ("t", [u"", u"做什麼", u"例子"],
    [[u"<strong>預存程序／函數</strong>", u"把一段邏輯（包含多個 SQL 與流程控制）存在資料庫裡執行", u"轉帳：檢查餘額、扣款、入帳、寫紀錄"], [u"<strong>觸發器</strong>", u"在 INSERT／UPDATE／DELETE 時自動執行", u"每次修改帳戶都自動寫一筆稽核紀錄"]]),
   ("h", u"取捨"),
   ("t", [u"好處", u"代價"],
    [[u"減少應用程式與資料庫之間的往返，效能好", u"邏輯分散在兩個地方，難以維護、測試與版本控制"], [u"規則集中，所有應用程式都會遵守", u"觸發器的副作用不容易被看見，除錯困難"], [u"適合資料密集、需要強一致的操作", u"綁定特定資料庫產品，難以遷移"]]),
   ("p", u"現代的常見做法是：資料完整性（約束）放在資料庫，業務邏輯放在應用程式，只有效能關鍵或稽核需求才使用預存程序與觸發器。"),
  ],
  u"檢視是存起來的查詢、不存資料，可簡化查詢與限制權限；實體化檢視把結果存起來、查詢快但需定期 REFRESH。預存程序把含流程控制的邏輯存在資料庫執行（如轉帳），觸發器在增刪改時自動執行（如寫稽核紀錄）。好處是減少往返、規則集中、適合資料密集與強一致操作；代價是邏輯分散難維護測試、觸發器副作用不易察覺、綁定特定產品。常見做法是完整性約束放資料庫、業務邏輯放應用程式。",
  [u"檢視和實體化檢視有什麼不同？", u"觸發器有什麼好處與風險？", u"你會把「訂單折扣計算」放在預存程序還是應用程式？為什麼？"]),

lesson(u"關聯代數：SQL 背後的數學",
  u"選擇、投影、連接：最佳化器思考的語言",
  [u"認識關聯代數的基本運算", u"把 SQL 轉成關聯代數", u"理解等價改寫與最佳化的關係"],
  [("p", u"SQL 是給人寫的；資料庫內部會先把它轉成<strong>關聯代數</strong>——一組作用在資料表上、結果仍是資料表的運算。"),
   ("t", [u"運算", u"符號", u"意思"],
    [[u"選擇", M(r"\sigma_{\text{cond}}(R)"), u"保留符合條件的列（WHERE）"], [u"投影", M(r"\pi_{A,B}(R)"), u"只保留某些欄位（SELECT 的欄位）"], [u"連接", M(r"R \bowtie_{\text{cond}} S"), u"JOIN"],
     [u"聯集、差集、交集", M(r"R \cup S,\; R - S,\; R \cap S"), u"UNION、EXCEPT、INTERSECT"], [u"笛卡兒積", M(r"R \times S"), u"CROSS JOIN"], [u"分組聚合", M(r"\gamma_{\text{dept},\,\text{AVG(score)}}(R)"), u"GROUP BY"]]),
   ("h", u"一個查詢的代數形式"),
   SQL(u"SELECT 姓名 FROM 學生 s JOIN 選課 e ON s.學號 = e.學號 WHERE e.成績 >= 90;"),
   F(r"\pi_{\text{name}}\left(\sigma_{\text{score} \ge 90}\left(\text{Student} \bowtie \text{Enroll}\right)\right)"),
   ("h", u"等價改寫：最佳化的基礎"),
   ("p", u"同一個結果有很多種等價的代數式，成本可以差上千倍。最重要的一條規則是<strong>選擇下推</strong>：先過濾、再連接。"),
   F(r"\sigma_{\text{score} \ge 90}(S \bowtie E) \equiv S \bowtie \sigma_{\text{score} \ge 90}(E)"),
   ("p", u"如果選課有一百萬筆、成績 90 分以上只有五萬筆，先過濾再連接，Join 的輸入就少了 95%。"),
   PY(u"""
# 用 Python 實作三個基本運算（資料表 = 字典的串列）
def select(R, pred):  return [r for r in R if pred(r)]
def project(R, cols): return [{c: r[c] for c in cols} for r in R]
def join(R, S, key):
    idx = {}
    for s in S: idx.setdefault(s[key], []).append(s)       # 雜湊連接（第 24 課）
    return [{**r, **s} for r in R for s in idx.get(r[key], [])]

students = [{"sid": 1, "name": "王小明"}, {"sid": 2, "name": "林小華"}]
enroll   = [{"sid": 1, "course": "資料庫", "score": 92}, {"sid": 2, "course": "資料庫", "score": 78}]
print(project(join(students, select(enroll, lambda e: e["score"] >= 90), "sid"), ["name"]))
"""),
  ],
  u"資料庫內部先把 SQL 轉成關聯代數：選擇 σ（WHERE）、投影 π（SELECT 欄位）、連接 ⋈（JOIN）、聯集差集交集（UNION、EXCEPT、INTERSECT）、笛卡兒積 ×（CROSS JOIN）與分組聚合 γ（GROUP BY），運算結果仍是資料表。同一結果有多種等價代數式，成本可差上千倍，最重要的改寫規則是選擇下推：先過濾再連接，可大幅縮小 Join 輸入。三個基本運算可用 Python 簡單實作。",
  [u"把一個含 WHERE 與 JOIN 的 SQL 寫成關聯代數。", u"什麼是選擇下推？為什麼它能大幅提升效能？", u"為什麼資料庫要先把 SQL 轉成關聯代數？"]),
]),
]
