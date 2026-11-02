# -*- coding: utf-8 -*-
"""資料庫系統原理：參考頁——互動實驗室、名詞對照。"""
from dbs_common import DBSLIB, LS, bw

LAB = {
    "file": "lab.html", "title": u"資料庫互動實驗室", "h1": u"資料庫互動實驗室", "icon": u"🧪",
    "description": u"查詢執行步驟、全表掃描與索引、B+ 樹、LSM 樹、連接演算法、隔離等級、MVCC、死結、WAL 復原、一致性雜湊",
    "body": [
        ("raw", u"<script>%s</script>" % DBSLIB),
        ("p", u"把課程中的互動工具集中在這裡。所有工具都在瀏覽器內以 JavaScript 模擬，不需要安裝或連線任何資料庫。"),
        ("h", u"1. 全表掃描與索引（第 15 課）"), bw("scan"),
        ("h", u"2. B+ 樹插入與分裂（第 18 課）"), bw("bptree"),
        ("h", u"3. LSM 樹寫入與合併（第 20 課）"), bw("lsm"),
        ("h", u"4. 查詢執行步驟（第 23 課）"), bw("qexec"),
        ("h", u"5. 連接演算法比較（第 24 課）"), bw("join"),
        ("h", u"6. 隔離等級與異常（第 30 課）"), bw("iso"),
        ("h", u"7. MVCC 多版本（第 32 課）"), bw("mvcc"),
        ("h", u"8. 死結偵測（第 33 課）"), bw("deadlock"),
        ("h", u"9. WAL 與當機復原（第 34 課）"), bw("wal"),
        ("h", u"10. 一致性雜湊（第 37 課）"), bw("ring"),
    ],
}

G = [
    (u"資料庫管理系統", u"DBMS", u"管理資料儲存、查詢與交易的軟體", 1),
    (u"關聯模型", u"relational model", u"以關係（表）表示資料，由 Codd 於 1970 年提出", 4),
    (u"主鍵／外鍵", u"primary key / foreign key", u"唯一識別一列／參照另一表的主鍵", 5),
    (u"關聯代數", u"relational algebra", u"選擇、投影、連接等運算，SQL 的數學基礎", 14),
    (u"連接", u"JOIN", u"依條件合併兩張表的資料列", 8),
    (u"共通表運算式", u"CTE", u"WITH 子句；遞迴 CTE 可處理階層與圖", 10),
    (u"正規化", u"normalization", u"消除重複與更新異常（1NF、2NF、3NF、BCNF）", 6),
    (u"功能相依", u"functional dependency", u"X 決定 Y：X 相同則 Y 必相同", 6),
    (u"頁", u"page", u"磁碟與記憶體間交換資料的單位（常見 4～16 KB）", 16),
    (u"緩衝池", u"buffer pool", u"把常用的頁快取在記憶體中", 16),
    (u"欄式儲存", u"columnar storage", u"同一欄的值存在一起，利於分析與壓縮", 17),
    (u"B+ 樹", u"B+ tree", u"高扇出的平衡樹，資料庫索引的主流結構", 18),
    (u"覆蓋索引", u"covering index", u"索引已包含查詢需要的所有欄位", 21),
    (u"LSM 樹", u"log-structured merge tree", u"先寫記憶體再批次寫成有序檔案，擅長大量寫入", 20),
    (u"布隆過濾器", u"Bloom filter", u"判斷「一定不存在」或「可能存在」的機率結構", 20),
    (u"倒排索引", u"inverted index", u"詞 → 文件清單，全文檢索的基礎", 22),
    (u"執行計畫", u"execution plan", u"最佳化器選出的運算子樹；以 EXPLAIN 查看", 26),
    (u"雜湊連接", u"hash join", u"以較小的表建雜湊表，再掃描大表比對", 24),
    (u"基數估計", u"cardinality estimation", u"估計每個運算子輸出多少列", 25),
    (u"ACID", u"ACID", u"原子性、一致性、隔離性、持久性", 29),
    (u"隔離等級", u"isolation level", u"讀未提交、讀已提交、可重複讀、可序列化", 30),
    (u"幻讀", u"phantom read", u"同一範圍查詢兩次，多出或少了資料列", 30),
    (u"寫入偏斜", u"write skew", u"兩個交易各自讀後寫不同列，合起來違反約束", 30),
    (u"兩階段鎖定", u"two-phase locking (2PL)", u"先只取得鎖、再只釋放鎖，保證可序列化", 31),
    (u"多版本並行控制", u"MVCC", u"保留多個版本，讀不擋寫、寫不擋讀", 32),
    (u"死結", u"deadlock", u"交易互相等待對方的鎖", 33),
    (u"預寫式日誌", u"write-ahead log (WAL)", u"修改資料頁前先把日誌寫入磁碟", 34),
    (u"檢查點", u"checkpoint", u"把髒頁寫回磁碟，縮短復原時間", 34),
    (u"時間點復原", u"point-in-time recovery (PITR)", u"基礎備份加上重播 WAL 到指定時間", 35),
    (u"複寫延遲", u"replication lag", u"副本落後主節點的時間", 36),
    (u"分片", u"sharding", u"依分片鍵把資料分散到多台機器", 37),
    (u"一致性雜湊", u"consistent hashing", u"增減節點時只需搬動少量資料", 37),
    (u"CAP 定理", u"CAP theorem", u"網路分割時只能在一致性與可用性之間二選一", 38),
    (u"共識演算法", u"consensus (Raft, Paxos)", u"讓多台機器對同一序列的決定達成一致", 39),
    (u"兩階段提交", u"two-phase commit (2PC)", u"協調者先詢問、再決定提交或中止", 40),
    (u"Saga", u"saga", u"以一連串本地交易加補償動作完成長流程", 40),
    (u"快取失效", u"cache invalidation", u"資料更新後讓快取中的舊資料失效", 43),
    (u"反正規化", u"denormalization", u"刻意重複存放資料以加速讀取", 6),
    (u"向量嵌入", u"vector embedding", u"把內容轉成高維向量，意思相近則向量相近", 48),
    (u"近似最近鄰", u"approximate nearest neighbor (ANN)", u"以少許準確度換取大幅加速的相似度搜尋，如 HNSW", 48),
    (u"檢索增強生成", u"RAG", u"先檢索相關資料，再交給語言模型回答", 48),
    (u"星狀綱要", u"star schema", u"事實表加上維度表的分析用綱要", 49),
    (u"湖倉一體", u"lakehouse", u"在資料湖上加入交易與綱要管理（Iceberg、Delta Lake）", 49),
    (u"SQL 注入", u"SQL injection", u"使用者輸入被當成 SQL 執行；以參數化查詢防範", 50),
    (u"變更資料擷取", u"change data capture (CDC)", u"從資料庫日誌擷取變更並同步到其他系統", 51),
]

GLOSSARY = {
    "file": "glossary.html", "title": u"資料庫名詞對照", "h1": u"資料庫名詞對照", "icon": u"📖",
    "description": u"資料庫系統常用名詞的中英對照與簡短說明",
    "body": [
        ("t", [u"中文", u"英文", u"說明", u"課"], [[a, b, c, LS(n)] for a, b, c, n in G]),
    ],
}

REFERENCES = [LAB, GLOSSARY]
