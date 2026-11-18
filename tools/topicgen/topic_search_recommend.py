# -*- coding: utf-8 -*-
"""搜尋引擎與推薦系統的規格。"""
import sch_a, sch_f, sch_ref

TOPIC = {
    "id": "search-recommend",
    "category": "tech",
    "title": u"搜尋引擎與推薦系統：從 PageRank 到 TikTok",
    "short": u"搜尋與推薦",
    "crumb": u"搜尋與推薦",
    "icon": u"🔎",
    "description": u"搜尋的歷史、網路爬蟲與 robots.txt、倒排索引、中文斷詞；TF-IDF 與 BM25、PageRank、SEO 與內容農場、學習排序、NDCG；自動完成與拼字校正、向量搜尋與嵌入、RAG 與 AI 搜尋、搜尋廣告與 GSP 拍賣；"
                   u"協同過濾、Netflix 大獎與矩陣分解、多階段推薦與雙塔模型、YouTube 與 TikTok、冷啟動與探索、A/B 測試；同溫層、隱私與 GDPR、Google 反壟斷案。附倒排索引、PageRank、向量搜尋與協同過濾四個互動工具。",
}

MODULES = sch_a.MODULES + sch_f.MODULES
REFERENCES = sch_ref.REFERENCES
