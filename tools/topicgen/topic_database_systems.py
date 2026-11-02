# -*- coding: utf-8 -*-
"""資料庫系統原理（dbs_）。"""
import dbs_a, dbs_c, dbs_e, dbs_g, dbs_ref

TOPIC = {
    "id": "database-systems",
    "category": "tech",
    "title": u"資料庫系統原理：從 SQL、索引、交易到分散式與向量資料庫",
    "short": u"資料庫系統原理",
    "crumb": u"資料庫系統原理",
    "icon": u"🗄️",
    "description": u"關聯模型、SQL、正規化；頁與緩衝池、列式與欄式、B+ 樹、LSM 樹、雜湊與倒排索引；查詢執行、連接演算法、最佳化器與 EXPLAIN；ACID、隔離等級、鎖、MVCC、死結、WAL 與復原；"
                   u"複製、分片、CAP、Raft、2PC、Spanner 與 Aurora；Redis、MongoDB、Cassandra、Neo4j、時序、向量資料庫與資料倉儲；資安與選型。以 Python 實作核心結構，附 10 個瀏覽器內互動工具。",
}

MODULES = dbs_a.MODULES + dbs_c.MODULES + dbs_e.MODULES + dbs_g.MODULES
REFERENCES = dbs_ref.REFERENCES
