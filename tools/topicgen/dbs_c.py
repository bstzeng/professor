# -*- coding: utf-8 -*-
"""資料庫系統原理：模組 C 儲存與索引（15～22）、D 查詢處理與最佳化（23～28）。"""
from dbs_common import *

MODULES = [
(u"模組 C｜儲存與索引", [

lesson(u"硬碟、SSD 與記憶體：為什麼 I/O 是一切的關鍵",
  u"資料庫設計的核心，就是減少讀磁碟的次數",
  [u"認識儲存階層的速度差距", u"理解循序讀取與隨機讀取的差別", u"體會索引與全表掃描的取捨"],
  [("h", u"儲存階層"),
   ("t", [u"層級", u"一次存取的時間（約）", u"如果 CPU 快取是 1 秒"],
    [[u"CPU 快取", u"約 1 奈秒", u"1 秒"], [u"記憶體（DRAM）", u"約 100 奈秒", u"約 1.5 分鐘"], [u"NVMe SSD 隨機讀", u"約 50～100 微秒", u"約 1 天"],
     [u"傳統硬碟隨機讀", u"約 5～10 毫秒", u"約 3 個月"], [u"跨資料中心網路往返", u"約 50～150 毫秒", u"數年"]]),
   ("p", u"從記憶體到磁碟，速度差了上千倍。資料庫幾乎所有的設計——頁、緩衝池、B+ 樹、日誌——都是為了<strong>減少磁碟 I/O</strong>，或把隨機 I/O 變成循序 I/O。"),
   ("h", u"循序 vs. 隨機"),
   ("ul", [u"傳統硬碟有讀寫頭與旋轉的碟片，隨機讀取要等讀寫頭移動與碟片轉到位置，循序讀取則可以連續讀。兩者速度可以差上百倍。", u"SSD 沒有機械零件，隨機讀取快得多，但循序讀取仍然比較快，而且寫入有特殊的限制（必須整塊抹除再寫）。", u"所以：讀一整個表（循序）有時反而比用索引一筆一筆跳著讀（隨機）快。"]),
   bw("scan", u"調整資料量、每筆大小與查詢回傳的比例，比較全表掃描與索引查詢："),
   ("note", u"記憶體越來越大", [("p", u"今天一台伺服器可以有數 TB 的記憶體，許多資料庫的「熱資料」可以整個放在記憶體裡。但磁碟仍然決定了持久性（資料不會因斷電消失）與成本，I/O 思維依然重要。")]),
  ],
  u"儲存階層速度差距巨大：CPU 快取約 1 奈秒、記憶體約 100 奈秒、NVMe SSD 隨機讀約 50～100 微秒、硬碟隨機讀約 5～10 毫秒、跨資料中心往返約 50～150 毫秒，若快取是 1 秒則硬碟約 3 個月。資料庫的頁、緩衝池、B+ 樹、日誌等設計都為了減少磁碟 I/O 或化隨機為循序。硬碟循序與隨機讀取可差百倍，SSD 隨機讀快得多但仍有寫入限制，因此回傳比例高時全表掃描可能比索引快。記憶體雖大，磁碟仍決定持久性與成本。",
  [u"為什麼資料庫的設計核心是減少磁碟 I/O？", u"循序讀取和隨機讀取的差別是什麼？", u"在互動工具中，查詢回傳超過多少比例時，全表掃描會比索引快？"]),

lesson(u"頁、緩衝池與資料的實際排列",
  u"資料在磁碟上長什麼樣子",
  [u"理解頁的結構", u"理解緩衝池與替換策略", u"用 Python 實作簡化的緩衝池"],
  [("h", u"頁：讀寫的基本單位"),
   ("p", u"資料庫不會一次只讀一筆資料，而是以<strong>頁</strong>為單位（PostgreSQL 8 KB、MySQL InnoDB 16 KB、SQLite 預設 4 KB）。一頁裡放了許多資料列。"),
   ("t", [u"頁的組成（簡化）", u"說明"],
    [[u"頁標頭", u"頁的編號、剩餘空間、校驗碼、最後修改的日誌位置"], [u"槽目錄（slot directory）", u"每一筆資料在頁內的位置；從前面往後長"], [u"資料列", u"從後面往前長；中間是空白空間"]]),
   ("p", u"這種「槽頁」設計讓資料列可以是不同長度，刪除與更新時只要改槽目錄。資料列的實體位置用（頁號, 槽號）表示，PostgreSQL 稱為 ctid。"),
   ("h", u"緩衝池"),
   ("p", u"緩衝池是記憶體中的一大塊區域，快取磁碟上的頁。資料庫要讀一頁時，先看緩衝池裡有沒有（命中），沒有才去讀磁碟。"),
   ("ul", [u"<strong>命中率</strong>：線上交易系統通常希望 99% 以上。", u"<strong>髒頁</strong>：在記憶體中被修改過、還沒寫回磁碟的頁。由背景程序定期寫回（安全性靠日誌保證，第 34 課）。", u"<strong>替換策略</strong>：緩衝池滿時要踢掉哪一頁？最常見的是 LRU（最久沒用的）及其變形——因為一次全表掃描就可能把所有熱資料擠出去，InnoDB 把 LRU 分成新、舊兩段，PostgreSQL 使用 clock-sweep 演算法。"]),
   PY(u"""
from collections import OrderedDict

class BufferPool:
    \"\"\"簡化的 LRU 緩衝池\"\"\"
    def __init__(self, capacity, disk):
        self.cap, self.disk, self.pages = capacity, disk, OrderedDict()
        self.hits = self.misses = 0

    def get(self, page_no):
        if page_no in self.pages:
            self.hits += 1
            self.pages.move_to_end(page_no)           # 最近用過的移到最後
        else:
            self.misses += 1
            if len(self.pages) >= self.cap:
                self.pages.popitem(last=False)          # 踢掉最久沒用的（髒頁要先寫回）
            self.pages[page_no] = self.disk[page_no]    # 從「磁碟」讀入
        return self.pages[page_no]

disk = {i: f"page-{i}" for i in range(1000)}
bp = BufferPool(100, disk)
for p in [1, 2, 3, 1, 2, 999, 1]: bp.get(p)
print(bp.hits, bp.misses)     # 3 4
"""),
  ],
  u"資料庫以頁為讀寫單位（PostgreSQL 8 KB、InnoDB 16 KB、SQLite 預設 4 KB），槽頁設計包含頁標頭、從前往後長的槽目錄與從後往前長的資料列，支援變長資料，資料位置以頁號與槽號表示。緩衝池在記憶體快取磁碟頁，線上系統希望命中率 99% 以上，髒頁由背景程序寫回、安全性靠日誌保證。替換策略以 LRU 及其變形為主，InnoDB 分新舊兩段、PostgreSQL 用 clock-sweep，以免全表掃描擠出熱資料。",
  [u"為什麼資料庫以「頁」而不是「列」為讀寫單位？", u"什麼是髒頁？它什麼時候被寫回磁碟？", u"為什麼單純的 LRU 會被全表掃描破壞？"]),

lesson(u"列式儲存 vs. 欄式儲存",
  u"同樣的資料，兩種排法，速度差百倍",
  [u"理解列式與欄式儲存的差別", u"理解欄式儲存為何適合分析", u"理解壓縮與向量化執行"],
  [("p", u"一張有 100 個欄位、十億筆資料的銷售表，資料在磁碟上可以怎麼排？"),
   ("t", [u"", u"列式（row store）", u"欄式（column store）"],
    [[u"排法", u"一筆資料的所有欄位放在一起", u"同一個欄位的所有值放在一起"], [u"讀一筆完整的訂單", u"一次讀到", u"要從 100 個地方各讀一點"],
     [u"「每個月的營收總和」", u"要讀全部 100 個欄位", u"只讀「日期」與「金額」兩個欄位"], [u"適合", u"OLTP：常常讀寫整筆資料", u"OLAP：掃描大量資料的少數欄位"],
     [u"代表", u"PostgreSQL、MySQL", u"Snowflake、BigQuery、ClickHouse、DuckDB、Parquet 檔案"]]),
   ("h", u"欄式儲存的三個優勢"),
   ("ol", [u"<strong>只讀需要的欄位</strong>：分析查詢通常只用幾個欄位，I/O 可以少一到兩個數量級。", u"<strong>壓縮效果極好</strong>：同一欄的值型別相同、常常重複。例如「國家」欄只有幾十種值，可以用字典編碼；排序後的日期可以用差值編碼；連續相同的值可以用連續長度編碼。壓縮率常有 5～10 倍以上。", u"<strong>向量化執行</strong>：一次處理一整批（例如 1,024 個）同型別的值，充分利用 CPU 的 SIMD 指令與快取。"]),
   PY(u"""
# 連續長度編碼（RLE）：欄式儲存中排序後的欄位非常適合
def rle(values):
    out, prev, n = [], None, 0
    for v in values:
        if v == prev: n += 1
        else:
            if prev is not None: out.append((prev, n))
            prev, n = v, 1
    out.append((prev, n))
    return out

country = ["台灣"] * 50000 + ["日本"] * 30000 + ["美國"] * 20000
print(rle(country))     # [('台灣', 50000), ('日本', 30000), ('美國', 20000)]：十萬個值只剩三組
"""),
   ("note", u"混合式", [("p", u"有些資料庫同時支援兩種（HTAP），例如 TiDB 的 TiFlash、SQL Server 的欄式索引：交易寫進列式儲存，再非同步複製一份欄式副本給分析用。")]),
  ],
  u"列式儲存把一筆資料的所有欄位放在一起，適合常讀寫整筆資料的 OLTP（PostgreSQL、MySQL）；欄式儲存把同一欄位的值放在一起，適合掃描大量資料少數欄位的 OLAP（Snowflake、BigQuery、ClickHouse、DuckDB、Parquet）。欄式三大優勢是只讀需要的欄位、壓縮效果極好（字典、差值、連續長度編碼，常 5～10 倍以上）與向量化執行充分利用 SIMD 與快取。HTAP 混合式如 TiFlash 與 SQL Server 欄式索引同時支援兩種。",
  [u"為什麼「每個月營收總和」這種查詢在欄式儲存中特別快？", u"為什麼欄式儲存的壓縮效果比列式好？", u"什麼是向量化執行？"]),

lesson(u"B+ 樹索引：為什麼幾乎每個資料庫都用它",
  u"又矮又胖的樹，三四次 I/O 找到十億筆中的任何一筆",
  [u"理解 B+ 樹的結構", u"理解插入與分裂", u"用 Python 實作簡化的 B+ 樹"],
  [("p", u"1970 年，拜爾與麥奎特發明了 <strong>B 樹</strong>。它的變形 <strong>B+ 樹</strong>成為幾乎所有關聯式資料庫索引的標準結構。"),
   ("h", u"結構"),
   ("ul", [u"<strong>內部節點</strong>：只放「路標」鍵與指向子節點的指標。", u"<strong>葉節點</strong>：放所有的鍵與對應的資料位置（或資料本身），並用指標串成有序的鏈結。", u"<strong>每個節點就是一頁</strong>：一頁 8～16 KB 可以放數百個鍵，所以樹非常「胖」，也非常「矮」。"]),
   F(r"\text{height} \approx \lceil \log_{f} N \rceil"),
   ("p", u"每個節點的分支數 f 約 400 時，三層可以容納約 6,400 萬筆、四層約 256 億筆。而上面幾層通常都在緩衝池裡，實際查一筆資料往往只需要 1～2 次磁碟 I/O。"),
   bw("bptree", u"一個一個插入鍵，觀察節點怎麼分裂、樹怎麼長高："),
   ("h", u"為什麼是 B+ 樹，而不是二元樹或雜湊"),
   ("ul", [u"<strong>二元搜尋樹</strong>：每個節點只有 2 個分支，十億筆要 30 層，30 次 I/O。", u"<strong>雜湊</strong>：只能找「等於」，不能做範圍查詢與排序。", u"<strong>B+ 樹</strong>：葉節點有序且串在一起，範圍查詢（<code>BETWEEN</code>、<code>ORDER BY</code>）只要找到起點，再沿著葉節點往後讀。"]),
   PY(u"""
import bisect

class BPlusTree:
    \"\"\"簡化版：只支援插入與查找，每個節點最多 m 個鍵\"\"\"
    def __init__(self, m=4):
        self.m, self.root = m, {"leaf": True, "keys": [], "vals": []}

    def search(self, k, node=None):
        node = node or self.root
        while not node["leaf"]:
            node = node["kids"][bisect.bisect_right(node["keys"], k)]
        i = bisect.bisect_left(node["keys"], k)
        return node["vals"][i] if i < len(node["keys"]) and node["keys"][i] == k else None

    def insert(self, k, v):
        split = self._insert(self.root, k, v)
        if split:                                            # 根分裂：樹長高一層
            sep, right = split
            self.root = {"leaf": False, "keys": [sep], "kids": [self.root, right]}

    def _insert(self, n, k, v):
        if n["leaf"]:
            i = bisect.bisect_left(n["keys"], k)
            n["keys"].insert(i, k); n["vals"].insert(i, v)
            if len(n["keys"]) <= self.m: return None
            h = (len(n["keys"]) + 1) // 2                     # 葉節點分裂：右半第一個鍵「複製」上去
            right = {"leaf": True, "keys": n["keys"][h:], "vals": n["vals"][h:]}
            n["keys"], n["vals"] = n["keys"][:h], n["vals"][:h]
            return right["keys"][0], right
        i = bisect.bisect_right(n["keys"], k)
        split = self._insert(n["kids"][i], k, v)
        if not split: return None
        sep, right = split
        n["keys"].insert(i, sep); n["kids"].insert(i + 1, right)
        if len(n["keys"]) <= self.m: return None
        mid = len(n["keys"]) // 2                             # 內部節點分裂：中間鍵「推」上去
        r = {"leaf": False, "keys": n["keys"][mid + 1:], "kids": n["kids"][mid + 1:]}
        up = n["keys"][mid]
        n["keys"], n["kids"] = n["keys"][:mid], n["kids"][:mid + 1]
        return up, r

t = BPlusTree(m=3)
for k in [10, 20, 5, 6, 12, 30, 7, 17]: t.insert(k, f"row-{k}")
print(t.search(12), t.search(99))       # row-12 None
"""),
  ],
  u"1970 年拜爾與麥奎特發明 B 樹，其變形 B+ 樹成為關聯式資料庫索引的標準：內部節點只放路標，葉節點放所有鍵與資料位置並串成有序鏈結，每個節點即一頁、可放數百個鍵，樹高約為 log_f N，分支數約 400 時三層約 6,400 萬筆、四層約 256 億筆，上層常駐緩衝池，查一筆常只需 1～2 次 I/O。節點滿時從中間分裂，樹從根部長高。相較二元樹太高、雜湊不能做範圍查詢，B+ 樹的有序葉節點利於範圍查詢與排序。",
  [u"為什麼 B+ 樹「又矮又胖」？這對 I/O 有什麼好處？", u"葉節點用指標串起來有什麼用途？", u"為什麼雜湊索引不能取代 B+ 樹？"]),

lesson(u"雜湊索引",
  u"最快的等值查找，以及它做不到的事",
  [u"理解雜湊索引的原理", u"理解擴充雜湊與線性雜湊", u"知道雜湊索引的適用場景"],
  [("p", u"雜湊索引用雜湊函數把鍵直接對應到「桶」（bucket），等值查找平均只需要一次存取："),
   F(r"\text{bucket} = h(\text{key}) \bmod B"),
   ("h", u"問題：桶滿了怎麼辦"),
   ("ul", [u"<strong>靜態雜湊</strong>：桶的數量固定，資料增加後溢出鏈越來越長，效能下降；要擴大就得全部重新雜湊。", u"<strong>擴充雜湊</strong>（extendible hashing）：用一個目錄指向桶，桶滿了只分裂那一個桶，目錄需要時倍增。", u"<strong>線性雜湊</strong>（linear hashing）：依序逐一分裂桶，不需要目錄，擴充過程平滑。"]),
   ("h", u"雜湊 vs. B+ 樹"),
   ("t", [u"", u"雜湊索引", u"B+ 樹"],
    [[u"等值查找（WHERE id = 5）", u"非常快", u"快"], [u"範圍查詢（BETWEEN、>、<）", u"<strong>不支援</strong>", u"支援"], [u"排序（ORDER BY）", u"不支援", u"支援"], [u"前綴查詢（LIKE 'abc%'）", u"不支援", u"支援"]]),
   ("p", u"所以 B+ 樹是預設的索引。雜湊索引用在：記憶體中的資料結構（例如 Redis 的雜湊表、資料庫內部的雜湊連接與雜湊聚合）、只需要等值查找的場合。PostgreSQL 提供雜湊索引，MySQL InnoDB 有「自適應雜湊索引」——自動為常被查詢的 B+ 樹頁建立雜湊捷徑。"),
   PY(u"""
class ExtendibleHash:
    \"\"\"簡化的擴充雜湊：桶容量 cap；目錄大小 2^global_depth\"\"\"
    def __init__(self, cap=2):
        self.cap, self.gd = cap, 1
        b0, b1 = {"ld": 1, "items": {}}, {"ld": 1, "items": {}}
        self.dir = [b0, b1]

    def _bucket(self, k): return self.dir[hash(k) & ((1 << self.gd) - 1)]

    def put(self, k, v):
        b = self._bucket(k)
        if k in b["items"] or len(b["items"]) < self.cap:
            b["items"][k] = v; return
        if b["ld"] == self.gd:                         # 目錄倍增
            self.dir += self.dir; self.gd += 1
        b["ld"] += 1                                    # 只分裂這一個桶
        nb = {"ld": b["ld"], "items": {}}
        for i, x in enumerate(self.dir):
            if x is b and (i >> (b["ld"] - 1)) & 1: self.dir[i] = nb
        old, b["items"] = b["items"], {}
        for kk, vv in old.items(): self._bucket(kk)["items"][kk] = vv
        self.put(k, v)

    def get(self, k): return self._bucket(k)["items"].get(k)
"""),
  ],
  u"雜湊索引以 bucket = h(key) mod B 把鍵對應到桶，等值查找平均一次存取。靜態雜湊溢出鏈會變長且擴大須全部重新雜湊；擴充雜湊以目錄指向桶，只分裂滿的桶並在需要時倍增目錄；線性雜湊依序逐一分裂、不需目錄。雜湊索引等值查找極快，但不支援範圍查詢、排序與前綴查詢，因此 B+ 樹是預設索引；雜湊用於記憶體結構、雜湊連接與聚合，以及只需等值查找的場合，InnoDB 另有自適應雜湊索引。",
  [u"為什麼雜湊索引不能做範圍查詢？", u"擴充雜湊相比靜態雜湊解決了什麼問題？", u"什麼情況下適合使用雜湊索引？"]),

lesson(u"LSM 樹：為寫入而生的設計",
  u"把隨機寫入變成循序寫入",
  [u"理解 LSM 樹的結構", u"理解合併與寫入放大", u"比較 LSM 樹與 B+ 樹"],
  [("p", u"B+ 樹每次寫入都要找到對應的葉節點、就地修改，是隨機寫入。如果寫入量極大（例如監控資料、訊息、物聯網），隨機寫入會成為瓶頸。1996 年歐尼爾等人提出 <strong>LSM 樹</strong>（Log-Structured Merge-tree）：不就地修改，而是不斷「附加」。"),
   ("h", u"運作方式"),
   ("ol", [u"寫入先記到 WAL（防當機），再放進記憶體中的有序結構 <strong>memtable</strong>。", u"memtable 滿了，整批依序寫成一個磁碟上的<strong>不可修改</strong>的有序檔案：<strong>SSTable</strong>。", u"SSTable 越來越多，背景程序定期把它們<strong>合併</strong>（compaction）成更大的檔案，同時丟掉被覆蓋或刪除的舊版本。", u"刪除是寫入一個「墓碑」標記，合併時才真正移除。"]),
   bw("lsm", u"寫入資料，觀察 memtable 如何寫成 SSTable，以及合併如何發生："),
   ("h", u"三種放大"),
   ("t", [u"", u"B+ 樹", u"LSM 樹"],
    [[u"寫入放大（實際寫入／使用者寫入）", u"中（寫整頁）", u"視合併策略，可能 10 倍以上"], [u"讀取放大（一次查詢讀幾個地方）", u"低（樹高）", u"較高（多個 SSTable，靠布隆過濾器緩解）"], [u"空間放大", u"低～中（頁有空白）", u"視合併策略（舊版本暫存）"], [u"寫入速度", u"中", u"非常快（循序寫）"]]),
   ("p", u"使用者：LevelDB、RocksDB（被大量資料庫當作底層引擎，例如 TiDB 的 TiKV、CockroachDB 早期版本）、Cassandra、HBase、ScyllaDB。"),
   PY(u"""
class TinyLSM:
    def __init__(self, memtable_size=4):
        self.mem, self.size, self.sstables = {}, memtable_size, []   # sstables: 新的在前

    def put(self, k, v):
        self.mem[k] = v
        if len(self.mem) >= self.size:
            self.sstables.insert(0, sorted(self.mem.items()))          # 寫成不可修改的有序檔
            self.mem = {}
            if len(self.sstables) >= 3: self.compact()

    def get(self, k):
        if k in self.mem: return self.mem[k]
        for table in self.sstables:                                    # 由新到舊找
            for kk, vv in table:                                       # 實務上用二分搜尋＋布隆過濾器
                if kk == k: return vv
        return None

    def compact(self):
        merged = {}
        for table in reversed(self.sstables): merged.update(table)     # 新的覆蓋舊的
        self.sstables = [sorted(merged.items())]
"""),
  ],
  u"B+ 樹就地修改是隨機寫入，1996 年歐尼爾等人提出的 LSM 樹改為附加：寫入先記 WAL 再放進記憶體有序 memtable，滿了整批寫成不可修改的有序 SSTable，背景合併多個 SSTable 並丟棄舊版本，刪除以墓碑標記。相較 B+ 樹，LSM 寫入非常快（循序寫），但寫入放大可能 10 倍以上、讀取需查多個 SSTable（以布隆過濾器緩解），空間放大視合併策略而定。LevelDB、RocksDB、Cassandra、HBase、ScyllaDB 採用此結構。",
  [u"LSM 樹為什麼寫入特別快？", u"什麼是合併（compaction）？為什麼需要它？", u"什麼情況下應該選擇 LSM 樹而不是 B+ 樹？"]),

lesson(u"複合索引、覆蓋索引與最左前綴",
  u"建對索引，比任何調校都有效",
  [u"理解複合索引的排序方式", u"掌握最左前綴原則", u"理解覆蓋索引與索引的代價"],
  [("h", u"複合索引"),
   SQL(u"CREATE INDEX idx_訂單 ON 訂單 (客戶編號, 下單日期, 金額);"),
   ("p", u"複合索引像電話簿：先依「客戶編號」排序，同一位客戶再依「下單日期」排序，再依「金額」排序。"),
   ("h", u"最左前綴原則"),
   ("t", [u"查詢條件", u"能用到這個索引嗎"],
    [[u"客戶編號 = 42", u"可以"], [u"客戶編號 = 42 AND 下單日期 >= '2026-01-01'", u"可以，而且非常有效"], [u"下單日期 >= '2026-01-01'（沒有客戶編號）", u"<strong>通常不行</strong>：就像只知道名字、不知道姓氏，電話簿幫不上忙"],
     [u"客戶編號 = 42 AND 金額 > 1000（跳過下單日期）", u"只能用到客戶編號的部分"], [u"客戶編號 > 10 AND 下單日期 = '2026-01-01'", u"只有客戶編號能有效縮小範圍（範圍條件之後的欄位幫助有限）"]]),
   ("p", u"設計原則：<strong>等值條件的欄位放前面，範圍條件的欄位放後面</strong>；常一起出現的查詢條件，依選擇性與使用頻率排序。"),
   ("h", u"覆蓋索引"),
   ("p", u"如果查詢需要的所有欄位都在索引裡，資料庫只讀索引就能回答，不用再回到資料表（「回表」）："),
   SQL(u"SELECT 下單日期, 金額 FROM 訂單 WHERE 客戶編號 = 42;   -- 三個欄位都在索引中：Index Only Scan"),
   ("h", u"索引不是越多越好"),
   ("ul", [u"每一次 INSERT、UPDATE、DELETE，都要同步更新所有相關的索引，寫入變慢。", u"索引佔用空間，也佔用緩衝池。", u"最佳化器選擇變多，也可能選錯。", u"原則：根據實際的查詢模式建索引，定期檢查沒被用到的索引並移除。"]),
   ("note", u"讓索引失效的常見寫法", [("ul", [u"在索引欄位上套函數：<code>WHERE YEAR(下單日期) = 2026</code>（改成範圍條件，或建立函數索引）。", u"隱含型別轉換：欄位是文字，條件卻寫成數字。", u"<code>LIKE '%關鍵字'</code>（開頭是萬用字元）。"])]),
  ],
  u"複合索引如電話簿依序排序多個欄位，遵守最左前綴原則：有第一欄條件才能有效使用，跳過中間欄位或範圍條件後的欄位幫助有限，因此等值條件欄位放前、範圍條件欄位放後。覆蓋索引包含查詢需要的所有欄位，可只讀索引不回表（Index Only Scan）。索引會拖慢寫入、佔空間與緩衝池並增加最佳化器誤判機會，應依查詢模式建立並移除未使用者。在索引欄位套函數、隱含型別轉換與開頭萬用字元的 LIKE 會讓索引失效。",
  [u"索引 (A, B, C)，查詢只有 B = 1 的條件，能用到索引嗎？為什麼？", u"什麼是覆蓋索引？它為什麼快？", u"為什麼 <code>WHERE YEAR(日期) = 2026</code> 會讓索引失效？怎麼改寫？"]),

lesson(u"全文索引與倒排索引",
  u"搜尋引擎的核心資料結構",
  [u"理解倒排索引的結構", u"理解中文斷詞的挑戰", u"認識相關性排序"],
  [("p", u"B+ 樹適合「整個值」或「前綴」的查詢。但要找「內容包含『資料庫』這個詞的所有文章」，就需要<strong>倒排索引</strong>。"),
   ("h", u"結構"),
   ("p", u"正排：文章 → 包含哪些詞。倒排：<strong>詞 → 出現在哪些文章</strong>（以及位置）。"),
   PY(u"""
import re
from collections import defaultdict

docs = {1: "資料庫 索引 原理", 2: "倒排 索引 是 搜尋引擎 的 核心", 3: "資料庫 交易 與 日誌"}
index = defaultdict(set)
for doc_id, text in docs.items():
    for term in text.split():              # 實務上需要斷詞、正規化、去除停用字
        index[term].add(doc_id)

def search(*terms):                        # AND 查詢 = 取交集
    sets = [index.get(t, set()) for t in terms]
    return set.intersection(*sets) if sets else set()

print(search("索引"))              # {1, 2}
print(search("資料庫", "索引"))    # {1}
"""),
   ("h", u"中文的挑戰：斷詞"),
   ("ul", [u"英文用空白分隔單字，中文沒有。「台北市長」可以是「台北／市長」或「台北市／長」。", u"做法：用斷詞工具（例如 jieba、CKIP）依詞典與統計模型切詞；或用 <strong>n-gram</strong>（把文字切成每 2 個字一組：台北、北市、市長），不需要詞典但索引較大。", u"PostgreSQL 的全文檢索需要搭配中文斷詞擴充；Elasticsearch 也有對應的中文分析器。"]),
   ("h", u"相關性排序"),
   ("p", u"找到所有包含關鍵字的文件後，要決定哪些排前面。經典的方法是 <strong>TF-IDF</strong> 與其改良 <strong>BM25</strong>："),
   F(r"\text{tfidf}(t,d) = \text{tf}(t,d) \times \log\frac{N}{\text{df}(t)}"),
   ("ul", [u"詞在這篇文章出現越多次（tf），越相關。", u"詞在越少文章出現（df 小），越有鑑別力——「的」出現在每篇文章，幾乎沒有價值。"]),
   ("note", u"從關鍵字到語意", [("p", u"倒排索引只能比對「相同的詞」。搜尋「汽車」找不到只寫「轎車」的文章——這是向量搜尋要解決的問題（第 48 課）。現代搜尋系統常把兩者結合，稱為混合搜尋。")]),
  ],
  u"倒排索引把詞對應到出現的文件與位置，AND 查詢即取交集，是搜尋引擎的核心。中文沒有空白分隔，需要以 jieba、CKIP 等工具依詞典與統計模型斷詞，或用 n-gram 切分（不需詞典但索引較大），PostgreSQL 與 Elasticsearch 都需中文分析擴充。相關性排序以 TF-IDF 與其改良 BM25 為經典：詞在文中出現越多越相關、出現的文件越少越有鑑別力。倒排索引只能比對相同詞，語意比對需要向量搜尋，現代系統常用混合搜尋。",
  [u"倒排索引和 B+ 樹索引各適合什麼查詢？", u"中文全文檢索為什麼需要斷詞？n-gram 有什麼優缺點？", u"TF-IDF 中的 IDF 代表什麼意義？"]),
]),

(u"模組 D｜查詢處理與最佳化", [

lesson(u"一條 SQL 的旅程：解析、改寫、計畫、執行",
  u"從文字到結果，資料庫內部經過哪些步驟",
  [u"理解查詢處理的各個階段", u"理解迭代器（火山）執行模型", u"逐步觀察查詢的執行過程"],
  [("h", u"四個階段"),
   ("ol", [u"<strong>解析</strong>：檢查語法，產生語法樹；確認表與欄位存在、權限是否足夠。", u"<strong>改寫</strong>：展開檢視、把子查詢改寫成連接、化簡條件（例如 <code>WHERE 1 = 1 AND x > 5</code>）。", u"<strong>最佳化</strong>：列舉可能的執行計畫，估計每一個的成本，選出最便宜的（第 25～27 課）。", u"<strong>執行</strong>：依照計畫，由一組運算子合作產生結果。"]),
   bw("qexec", u"選一個查詢，一步一步看每個運算子的輸出："),
   ("h", u"迭代器模型（火山模型）"),
   ("p", u"每個運算子（掃描、過濾、連接、排序……）都實作同一個介面：<code>next()</code>——「給我下一筆」。上層的運算子向下層要資料，資料一筆一筆往上流。"),
   PY(u"""
class Scan:
    def __init__(self, rows): self.it = iter(rows)
    def next(self): return next(self.it, None)

class Filter:
    def __init__(self, child, pred): self.child, self.pred = child, pred
    def next(self):
        while (r := self.child.next()) is not None:
            if self.pred(r): return r
        return None

class Project:
    def __init__(self, child, cols): self.child, self.cols = child, cols
    def next(self):
        r = self.child.next()
        return None if r is None else {c: r[c] for c in self.cols}

rows = [{"name": "王小明", "dept": "資工"}, {"name": "林小華", "dept": "電機"}]
plan = Project(Filter(Scan(rows), lambda r: r["dept"] == "資工"), ["name"])
while (r := plan.next()) is not None: print(r)
"""),
   ("p", u"這個模型的好處是簡單、可以任意組合、而且是<strong>管線化</strong>的：不需要把中間結果全部存下來。缺點是每一筆資料都要經過很多次函數呼叫，對分析查詢不夠快——所以欄式資料庫改用<strong>向量化</strong>（一次傳一批）或<strong>編譯執行</strong>（把整個計畫編譯成機器碼）。"),
  ],
  u"查詢處理分為四階段：解析檢查語法、產生語法樹並確認表欄與權限；改寫展開檢視、子查詢轉連接並化簡條件；最佳化列舉計畫並選成本最低者；執行由運算子合作產生結果。迭代器（火山）模型中每個運算子實作 next()，上層向下層逐筆要資料，簡單、可組合且管線化，但每筆經過多次函數呼叫，分析查詢較慢，因此欄式資料庫改用向量化或編譯執行。",
  [u"查詢處理的四個階段各在做什麼？", u"什麼是迭代器（火山）模型？它有什麼優點？", u"為什麼分析型資料庫要改用向量化執行？"]),

lesson(u"Join 演算法：巢狀迴圈、雜湊、排序合併",
  u"資料庫最重要的三種演算法",
  [u"理解三種 Join 演算法", u"估算各演算法的 I/O 成本", u"知道最佳化器何時選哪一種"],
  [("t", [u"演算法", u"做法", u"I/O 成本（M、N 為兩表頁數，B 為記憶體頁數）", u"適合"],
    [[u"<strong>巢狀迴圈</strong>", u"對外表的每一筆，掃描內表找配對", u"區塊版：約 M + ⌈M/(B−2)⌉ × N", u"外表很小，或內表有索引（索引巢狀迴圈）"],
     [u"<strong>雜湊連接</strong>", u"用較小的表在記憶體建雜湊表，再掃描大表探測", u"放得下記憶體：M + N；放不下（分割）：約 3(M + N)", u"大表等值連接，沒有合適的索引"],
     [u"<strong>排序合併</strong>", u"兩表都依連接鍵排序，再像拉拉鍊一樣合併", u"排序成本＋M + N", u"資料已經有序（例如有索引），或非等值連接"]]),
   bw("join", u"調整兩個表的大小與可用記憶體，比較各演算法的成本："),
   PY(u"""
def hash_join(R, S, key):
    \"\"\"建立階段用較小的 R；探測階段掃描 S\"\"\"
    table = {}
    for r in R: table.setdefault(r[key], []).append(r)
    for s in S:
        for r in table.get(s[key], []):
            yield {**r, **s}

def sort_merge_join(R, S, key):
    R, S = sorted(R, key=lambda x: x[key]), sorted(S, key=lambda x: x[key])
    i = j = 0
    while i < len(R) and j < len(S):
        a, b = R[i][key], S[j][key]
        if a < b: i += 1
        elif a > b: j += 1
        else:                                        # 找出兩邊相同鍵的區段，兩兩配對
            i2 = i
            while i2 < len(R) and R[i2][key] == a: i2 += 1
            j2 = j
            while j2 < len(S) and S[j2][key] == a: j2 += 1
            for r in R[i:i2]:
                for s in S[j:j2]: yield {**r, **s}
            i, j = i2, j2
"""),
   ("h", u"分割雜湊連接（Grace Hash Join）"),
   ("p", u"兩個表都太大、記憶體放不下時：先用同一個雜湊函數把兩個表各切成 k 份寫回磁碟（相同鍵一定落在同一份），再一份一份地載入記憶體做雜湊連接。每個表讀兩次、寫一次，所以約是 3(M + N)。"),
  ],
  u"三種 Join 演算法：巢狀迴圈對外表每筆掃描內表，區塊版成本約 M + ⌈M/(B−2)⌉ × N，適合外表小或內表有索引；雜湊連接以較小表建雜湊表再掃大表探測，放得下記憶體成本 M + N、否則分割約 3(M + N)，適合無索引的大表等值連接；排序合併將兩表排序後像拉鍊合併，適合已有序或非等值連接。分割雜湊連接先以同一雜湊函數把兩表切成 k 份寫回磁碟，再逐份載入連接，每表讀兩次寫一次。",
  [u"什麼情況下巢狀迴圈連接反而是最好的選擇？", u"雜湊連接的兩個階段是什麼？", u"分割雜湊連接的成本為什麼約是 3(M + N)？"]),

lesson(u"統計資訊與成本估計",
  u"最佳化器怎麼「猜」一個條件會篩出多少筆",
  [u"理解選擇性與基數估計", u"認識直方圖與常見值", u"理解估計錯誤的後果"],
  [("p", u"最佳化器要選計畫，必須先估計每一步會產生多少資料列（<strong>基數</strong>）。它依賴資料庫定期收集的<strong>統計資訊</strong>（PostgreSQL 的 ANALYZE、MySQL 的 ANALYZE TABLE）。"),
   ("h", u"統計資訊包括"),
   ("ul", [u"表的總筆數、總頁數。", u"每個欄位的相異值數量、NULL 的比例。", u"<strong>最常見值</strong>（MCV）與它們的頻率。", u"<strong>直方圖</strong>：把值的範圍切成多個桶，每桶的筆數大致相同。"]),
   ("h", u"選擇性估計"),
   F(r"\text{sel}(A = c) \approx \frac{1}{\text{ndistinct}(A)} \qquad \text{sel}(A \lt c) \approx \frac{c - \min}{\max - \min}"),
   F(r"\text{sel}(p_1 \wedge p_2) \approx \text{sel}(p_1) \times \text{sel}(p_2) \quad \text{(independence)}"),
   ("h", u"獨立性假設的陷阱"),
   ("p", u"「縣市 = 台北市」選擇性 10%，「郵遞區號 = 100」選擇性 0.5%。最佳化器假設兩者獨立，估計同時成立的比例是 0.05%；但實際上郵遞區號 100 一定在台北市，真實比例是 0.5%——低估了 10 倍。"),
   ("ul", [u"低估 → 以為結果很少 → 選了巢狀迴圈 → 實際上要跑幾百萬次，查詢慢了上千倍。", u"解法：PostgreSQL 的「延伸統計」（CREATE STATISTICS）可以記錄欄位之間的相依；或改寫查詢、使用提示。"]),
   PY(u"""
# 用等深直方圖估計範圍條件的選擇性
import bisect, random
values = sorted(random.gauss(50, 15) for _ in range(100_000))
buckets = 20
bounds = [values[i * len(values) // buckets] for i in range(buckets)] + [values[-1]]

def est_less_than(c):
    i = bisect.bisect_right(bounds, c) - 1                       # 落在第 i 個桶
    if i < 0: return 0.0
    if i >= buckets: return 1.0
    lo, hi = bounds[i], bounds[i + 1]
    frac = (c - lo) / (hi - lo) if hi > lo else 0                # 桶內假設均勻分布
    return (i + frac) / buckets

real = sum(v < 30 for v in values) / len(values)
print(f"估計 {est_less_than(30):.3f}，實際 {real:.3f}")
"""),
  ],
  u"最佳化器依 ANALYZE 收集的統計資訊估計每步產生的資料列數（基數），統計包括總筆數與頁數、欄位相異值數與 NULL 比例、最常見值 MCV 與頻率，以及每桶筆數相近的直方圖。等值選擇性約為 1/相異值數，範圍條件依值域比例估計，多條件假設獨立而相乘。獨立性假設在相關欄位（如縣市與郵遞區號）會低估 10 倍，導致錯選巢狀迴圈而慢上千倍，可用 PostgreSQL 延伸統計 CREATE STATISTICS、改寫查詢或提示解決。",
  [u"資料庫收集哪些統計資訊？", u"為什麼「獨立性假設」會讓估計出錯？舉一個例子。", u"基數低估可能造成什麼樣的效能問題？"]),

lesson(u"看懂 EXPLAIN：查詢計畫實戰",
  u"資料庫到底打算怎麼做，以及實際做了什麼",
  [u"讀懂查詢計畫的樹狀結構", u"比較估計值與實際值", u"找出計畫中的效能問題"],
  [SQL(u"""
EXPLAIN ANALYZE
SELECT c.姓名, SUM(o.金額)
FROM 客戶 c JOIN 訂單 o ON o.客戶編號 = c.客戶編號
WHERE o.下單日期 >= '2026-10-01'
GROUP BY c.姓名;
"""),
   ("p", u"PostgreSQL 的輸出（簡化）："),
   ("code", u"""HashAggregate  (rows=1200) (actual rows=1187 time=85.2 ms)
  ->  Hash Join  (rows=48000) (actual rows=51320)
        Hash Cond: (o.客戶編號 = c.客戶編號)
        ->  Index Scan using idx_下單日期 on 訂單 o  (rows=48000) (actual rows=51320)
              Index Cond: (下單日期 >= '2026-10-01')
        ->  Hash  (rows=20000)
              ->  Seq Scan on 客戶 c  (rows=20000) (actual rows=20000)"""),
   ("h", u"怎麼讀"),
   ("ul", [u"<strong>由內往外、由下往上</strong>讀：最深層的運算子先執行。", u"這個計畫：用索引找出十月以後的訂單 → 把客戶表整個讀進雜湊表 → 雜湊連接 → 雜湊聚合。", u"<code>rows=</code> 是<strong>估計</strong>值，<code>actual rows=</code> 是<strong>實際</strong>值（只有 EXPLAIN ANALYZE 才有，而且會真的執行查詢）。"]),
   ("h", u"常見的問題訊號"),
   ("t", [u"訊號", u"可能的原因與對策"],
    [[u"估計與實際差 10 倍以上", u"統計資訊過時或欄位相關：執行 ANALYZE、建立延伸統計"], [u"大表上的 Seq Scan，但只回傳少量資料", u"缺少索引，或索引因函數、型別轉換而失效"],
     [u"Nested Loop 的外層實際筆數很大", u"基數低估：應該用 Hash Join"], [u"Sort 或 Hash 使用磁碟（external merge、Batches > 1）", u"工作記憶體不足：調大 work_mem 或減少資料量"], [u"Index Scan 後大量「回表」", u"考慮覆蓋索引"]]),
   ("note", u"MySQL", [("p", u"MySQL 的 EXPLAIN 以表格呈現：注意 <code>type</code> 欄（ALL 代表全表掃描、ref／range 代表用到索引）、<code>key</code>（實際使用的索引）、<code>rows</code>（估計掃描筆數）與 <code>Extra</code>（Using filesort、Using temporary 常是效能警訊）。MySQL 8 也支援 EXPLAIN ANALYZE。")]),
  ],
  u"EXPLAIN ANALYZE 顯示查詢計畫與實際執行結果，由內往外、由下往上閱讀，rows 為估計值、actual rows 為實際值（會真的執行查詢）。問題訊號包括估計與實際差 10 倍以上（執行 ANALYZE 或延伸統計）、大表 Seq Scan 只回傳少量資料（缺索引或索引失效）、外層筆數大的 Nested Loop（基數低估）、Sort 或 Hash 使用磁碟（調大 work_mem）與大量回表（考慮覆蓋索引）。MySQL 的 EXPLAIN 應注意 type、key、rows 與 Extra 欄位。",
  [u"EXPLAIN 和 EXPLAIN ANALYZE 有什麼不同？", u"計畫中估計筆數與實際筆數差很多，代表什麼？", u"看到「Using filesort」或排序使用磁碟時，可以怎麼處理？"]),

lesson(u"查詢最佳化器：Join 順序與常見誤判",
  u"在天文數字般的計畫中，找出夠好的那一個",
  [u"理解 Join 順序的搜尋空間", u"認識動態規劃與啟發式搜尋", u"理解最佳化器的限制"],
  [("h", u"搜尋空間爆炸"),
   ("p", u"三個表的連接有 12 種順序（含左右）；十個表的連接，可能的樹狀結構超過一百億種。每一種再搭配不同的 Join 演算法與存取方法——最佳化器不可能全部算一遍。"),
   ("h", u"System R 的動態規劃"),
   ("p", u"1979 年 IBM System R 的論文（塞林格等人）奠定了現代最佳化器的基礎："),
   ("ol", [u"先找出每個單一表最便宜的存取方式（全表掃描或哪個索引）。", u"再找每一對表最便宜的連接方式。", u"再用兩表的最佳結果，擴展到三表……（動態規劃）。", u"只考慮「左深樹」，並保留「有趣的排序」（例如已經依連接鍵排好序的結果，後面可以省下排序）。"]),
   ("p", u"表的數量太多時（PostgreSQL 預設 12 個以上），改用基因演算法等啟發式方法。"),
   ("h", u"最佳化器為什麼會選錯"),
   ("ul", [u"<strong>基數估計錯誤</strong>：最常見的原因（第 25 課），誤差在多層 Join 中會被乘上去。", u"<strong>成本模型不準</strong>：不知道哪些資料已經在快取裡、SSD 與硬碟的差異。", u"<strong>參數化查詢</strong>：同一個查詢對不同參數值，最佳計畫可能完全不同（例如熱門客戶有十萬筆訂單，一般客戶只有十筆）。"]),
   ("h", u"實務上的對策"),
   ("ul", [u"保持統計資訊更新。", u"用 EXPLAIN ANALYZE 找出估計錯誤的地方。", u"改寫查詢（例如把複雜查詢拆成幾步、用 CTE 或暫存表）。", u"必要時使用提示（MySQL、Oracle 支援；PostgreSQL 需要擴充）或固定計畫——但要知道這是「繞過」問題。"]),
  ],
  u"三表連接有 12 種順序，十表可能的樹狀結構超過一百億種，再搭配演算法與存取方法，最佳化器無法窮舉。1979 年 IBM System R 塞林格等人以動態規劃奠定基礎：先找單表最佳存取方式，再逐步擴展到兩表、三表，只考慮左深樹並保留有趣的排序；表太多時（PostgreSQL 預設 12 個以上）改用基因演算法。選錯的原因包括基數估計錯誤在多層 Join 中相乘、成本模型不準，以及參數化查詢對不同參數的最佳計畫不同。對策是更新統計、EXPLAIN ANALYZE、改寫查詢與必要時使用提示。",
  [u"為什麼最佳化器不能把所有計畫都算一遍？", u"System R 的動態規劃是怎麼運作的？", u"參數化查詢為什麼可能讓最佳化器選錯計畫？"]),

lesson(u"慢查詢調校案例",
  u"從症狀到解法：五個常見情境",
  [u"建立系統化的調校流程", u"認識常見的慢查詢模式", u"知道何時該改架構而不是改查詢"],
  [("h", u"調校流程"),
   ("ol", [u"<strong>找出慢查詢</strong>：開啟慢查詢日誌，或使用 pg_stat_statements 找出「總耗時」最高的查詢（不只是單次最慢的）。", u"<strong>看計畫</strong>：EXPLAIN ANALYZE。", u"<strong>找出瓶頸</strong>：估計錯誤？缺索引？排序溢出到磁碟？", u"<strong>修改並驗證</strong>：一次只改一件事，比較前後的實際執行時間。"]),
   ("h", u"五個常見案例"),
   ("t", [u"症狀", u"原因", u"解法"],
    [[u"<strong>N+1 查詢</strong>：列出 100 位客戶，每位再各查一次訂單，共 101 次查詢", u"ORM 的延遲載入", u"一次 JOIN，或用 IN 一次取回所有訂單"],
     [u"<strong>深分頁</strong>：<code>LIMIT 20 OFFSET 1000000</code> 越後面越慢", u"資料庫要先讀過並丟掉前一百萬筆", u"改用「鍵集分頁」：<code>WHERE id > 上一頁最後的 id ORDER BY id LIMIT 20</code>"],
     [u"<strong>函數讓索引失效</strong>", u"<code>WHERE LOWER(email) = …</code>", u"建立函數索引，或存正規化後的欄位"],
     [u"<strong>大量 COUNT(*)</strong>：首頁顯示「共 3,281,442 筆」", u"每次都要掃描", u"使用近似值、快取計數，或改設計"],
     [u"<strong>OR 條件</strong>：<code>WHERE a = 1 OR b = 2</code>", u"單一索引無法同時處理", u"拆成兩個查詢 UNION，或依賴資料庫的位元圖索引合併"]]),
   PY(u"""
import sqlite3, time
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE 訂單 (id INTEGER PRIMARY KEY, 客戶 INTEGER, 金額 INTEGER)")
db.executemany("INSERT INTO 訂單 (客戶, 金額) VALUES (?, ?)", [(i % 5000, i % 997) for i in range(500_000)])

t = time.time(); db.execute("SELECT * FROM 訂單 LIMIT 20 OFFSET 490000").fetchall(); print("OFFSET", time.time() - t)
t = time.time(); db.execute("SELECT * FROM 訂單 WHERE id > 490000 ORDER BY id LIMIT 20").fetchall(); print("鍵集", time.time() - t)

t = time.time(); db.execute("SELECT SUM(金額) FROM 訂單 WHERE 客戶 = 42").fetchall(); print("無索引", time.time() - t)
db.execute("CREATE INDEX idx_客戶 ON 訂單(客戶)")
t = time.time(); db.execute("SELECT SUM(金額) FROM 訂單 WHERE 客戶 = 42").fetchall(); print("有索引", time.time() - t)
"""),
   ("note", u"何時該改架構", [("p", u"如果最佳化之後，查詢仍然需要掃描數億筆資料（例如即時的多維度報表），問題可能不在 SQL，而在架構：該用讀取副本、快取、實體化檢視，或把分析工作移到資料倉儲（第 49 課）。")]),
  ],
  u"調校流程為：以慢查詢日誌或 pg_stat_statements 找出總耗時最高的查詢、EXPLAIN ANALYZE 看計畫、找出瓶頸、一次改一件事並驗證。常見案例有 ORM 延遲載入造成的 N+1 查詢（改 JOIN 或 IN）、深分頁 OFFSET 越後越慢（改鍵集分頁）、函數使索引失效（函數索引）、大量 COUNT(*)（近似值或快取）與 OR 條件（拆 UNION 或位元圖合併）。若最佳化後仍需掃描數億筆，應考慮讀取副本、快取、實體化檢視或資料倉儲等架構改變。",
  [u"什麼是 N+1 查詢問題？怎麼解決？", u"為什麼 OFFSET 很大的分頁會很慢？鍵集分頁怎麼做？", u"什麼時候應該改架構，而不是繼續調整 SQL？"]),
]),
]
