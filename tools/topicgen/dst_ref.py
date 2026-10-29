# -*- coding: utf-8 -*-
"""資料結構：參考頁——互動實驗室、複雜度速查、名詞中英對照。"""
from dst_common import DSTLIB, LS, sw

LAB = {
    "file": "lab.html", "title": u"資料結構互動實驗室", "h1": u"資料結構互動實驗室", "icon": u"🧪",
    "description": u"動態陣列、鏈結串列、堆疊、環狀佇列、雜湊表、BST 與 AVL、堆積、字典樹、線段樹、聯集—尋找、跳躍串列、圖搜尋、拓撲排序、排序、二分搜尋、LRU、布隆過濾器",
    "body": [
        ("raw", u"<script>%s</script>" % DSTLIB),
        ("p", u"把課程中的互動元件集中在這裡，方便隨時回來玩。每一個都附上對應的課。"),
        ("h", u"1. 動態陣列與攤銷成本（第 4、7 課）"), sw("dynarr"),
        ("h", u"2. 鏈結串列（第 8、9 課）"), sw("linked"),
        ("h", u"3. 堆疊：括號配對（第 10 課）"), sw("stack"),
        ("h", u"4. 堆疊：後序運算式（第 10 課）"), sw("stack", mode="rpn"),
        ("h", u"5. 環狀緩衝區（第 11 課）"), sw("ring"),
        ("h", u"6. 雜湊表（第 13～16 課）"), sw("hash"),
        ("h", u"7. 二元搜尋樹與 AVL 樹（第 20～22 課）"), sw("bst"),
        ("h", u"8. 二元堆積（第 24、25 課）"), sw("heap"),
        ("h", u"9. 字典樹（第 29 課）"), sw("trie"),
        ("h", u"10. 線段樹（第 30 課）"), sw("seg"),
        ("h", u"11. 聯集—尋找（第 32 課）"), sw("uf"),
        ("h", u"12. 跳躍串列（第 33 課）"), sw("skip"),
        ("h", u"13. 圖搜尋：BFS、DFS、戴克斯特拉、A*（第 35、37 課）"), sw("grid"),
        ("h", u"14. 拓撲排序（第 36 課）"), sw("topo"),
        ("h", u"15. 排序演算法（第 40～42 課）"), sw("sort"),
        ("h", u"16. 二分搜尋（第 39 課）"), sw("bsearch"),
        ("h", u"17. LRU 快取（第 44 課）"), sw("lru"),
        ("h", u"18. 布隆過濾器（第 45 課）"), sw("bloom"),
    ],
}

CHEAT = {
    "file": "complexity.html", "title": u"資料結構複雜度速查", "h1": u"資料結構複雜度速查", "icon": u"📋",
    "description": u"各種資料結構與演算法的時間、空間複雜度一覽，以及 Python 對應的內建工具",
    "body": [
        ("h", u"資料結構"),
        ("t", [u"結構", u"存取", u"搜尋", u"插入", u"刪除", u"空間", u"課"], [
            [u"陣列", u"O(1)", u"O(n)", u"O(n)", u"O(n)", u"O(n)", LS(6)],
            [u"動態陣列（尾端）", u"O(1)", u"O(n)", u"攤銷 O(1)", u"O(1)", u"O(n)", LS(7)],
            [u"鏈結串列", u"O(n)", u"O(n)", u"O(1)*", u"O(1)*", u"O(n)", LS(8)],
            [u"堆疊／佇列", u"—", u"—", u"O(1)", u"O(1)", u"O(n)", LS(10)],
            [u"雜湊表", u"—", u"平均 O(1)", u"平均 O(1)", u"平均 O(1)", u"O(n)", LS(13)],
            [u"二元搜尋樹", u"—", u"O(h)", u"O(h)", u"O(h)", u"O(n)", LS(20)],
            [u"AVL／紅黑樹", u"—", u"O(log n)", u"O(log n)", u"O(log n)", u"O(n)", LS(22)],
            [u"二元堆積", u"最小值 O(1)", u"O(n)", u"O(log n)", u"取出 O(log n)", u"O(n)", LS(24)],
            [u"B 樹", u"—", u"O(log n)", u"O(log n)", u"O(log n)", u"O(n)", LS(28)],
            [u"字典樹", u"—", u"O(L)", u"O(L)", u"O(L)", u"O(總字元數)", LS(29)],
            [u"線段樹", u"—", u"區間 O(log n)", u"更新 O(log n)", u"—", u"O(n)", LS(30)],
            [u"樹狀陣列", u"—", u"前綴 O(log n)", u"更新 O(log n)", u"—", u"O(n)", LS(31)],
            [u"聯集—尋找", u"—", u"O(α(n))", u"O(α(n))", u"—", u"O(n)", LS(32)],
            [u"跳躍串列", u"—", u"期望 O(log n)", u"期望 O(log n)", u"期望 O(log n)", u"期望 O(n)", LS(33)],
            [u"布隆過濾器", u"—", u"O(k)", u"O(k)", u"不支援", u"O(m) 位元", LS(45)],
        ]),
        ("p", u"* 在已知節點位置時。L 是字串長度，h 是樹高，α 是反阿克曼函數，k 是雜湊函數個數。"),
        ("h", u"演算法"),
        ("t", [u"演算法", u"時間", u"額外空間", u"備註", u"課"], [
            [u"二分搜尋", u"O(log n)", u"O(1)", u"需要排序", LS(39)],
            [u"氣泡／選擇／插入排序", u"O(n²)", u"O(1)", u"插入排序對幾乎排好的資料接近 O(n)", LS(40)],
            [u"合併排序", u"O(n log n)", u"O(n)", u"穩定", LS(41)],
            [u"快速排序", u"平均 O(n log n)，最壞 O(n²)", u"O(log n)", u"實務上通常最快", LS(41)],
            [u"堆積排序", u"O(n log n)", u"O(1)", u"不穩定", LS(25)],
            [u"計數排序", u"O(n + k)", u"O(k)", u"小範圍整數", LS(42)],
            [u"基數排序", u"O(d(n + b))", u"O(n + b)", u"固定長度鍵", LS(42)],
            [u"建堆", u"O(n)", u"O(1)", u"弗洛伊德法", LS(25)],
            [u"BFS／DFS", u"O(V + E)", u"O(V)", u"", LS(35)],
            [u"拓撲排序", u"O(V + E)", u"O(V)", u"卡恩演算法", LS(36)],
            [u"戴克斯特拉", u"O((V + E) log V)", u"O(V)", u"不可有負權重", LS(37)],
            [u"克魯斯克爾", u"O(E log E)", u"O(V)", u"聯集—尋找", LS(38)],
            [u"普林", u"O(E log V)", u"O(V)", u"優先佇列", LS(38)],
        ]),
        ("h", u"Python 工具對照"),
        ("t", [u"需求", u"Python", u"課"], [
            [u"動態陣列、堆疊", u"list", LS(7)], [u"佇列、雙端佇列", u"collections.deque", LS(12)], [u"雜湊表、集合", u"dict、set", LS(17)],
            [u"計數、分組", u"collections.Counter、defaultdict", LS(17)], [u"優先佇列", u"heapq", LS(24)], [u"有序串列的二分搜尋", u"bisect", LS(39)],
            [u"LRU 快取", u"functools.lru_cache、OrderedDict", LS(44)], [u"排序", u"list.sort、sorted（Timsort）", LS(43)],
        ]),
    ],
}

GLOSSARY = {
    "file": "glossary.html", "title": u"資料結構名詞中英對照", "h1": u"資料結構名詞中英對照", "icon": u"📖",
    "description": u"資料結構與演算法常用名詞的中英對照",
    "body": [
        ("t", [u"中文", u"英文", u"課"], [
            [u"資料結構", u"Data Structure", LS(1)], [u"位址", u"Address", LS(2)], [u"指標／參考", u"Pointer / Reference", LS(2)], [u"時間複雜度", u"Time Complexity", LS(3)],
            [u"攤銷分析", u"Amortized Analysis", LS(4)], [u"抽象資料型別", u"Abstract Data Type (ADT)", LS(5)], [u"陣列", u"Array", LS(6)], [u"隨機存取", u"Random Access", LS(6)],
            [u"動態陣列", u"Dynamic Array", LS(7)], [u"容量", u"Capacity", LS(7)], [u"鏈結串列", u"Linked List", LS(8)], [u"哨兵節點", u"Sentinel / Dummy Node", LS(8)],
            [u"雙向鏈結串列", u"Doubly Linked List", LS(9)], [u"快慢指標", u"Fast and Slow Pointers", LS(9)], [u"堆疊", u"Stack", LS(10)], [u"後進先出", u"LIFO", LS(10)],
            [u"佇列", u"Queue", LS(11)], [u"先進先出", u"FIFO", LS(11)], [u"環狀緩衝區", u"Ring Buffer / Circular Buffer", LS(11)], [u"雙端佇列", u"Deque", LS(12)],
            [u"單調堆疊", u"Monotonic Stack", LS(12)], [u"雜湊表", u"Hash Table", LS(13)], [u"碰撞", u"Collision", LS(13)], [u"雜湊函數", u"Hash Function", LS(14)],
            [u"鏈結法", u"Separate Chaining", LS(15)], [u"開放定址", u"Open Addressing", LS(15)], [u"線性探測", u"Linear Probing", LS(15)], [u"墓碑", u"Tombstone", LS(15)],
            [u"負載因子", u"Load Factor", LS(16)], [u"重雜湊", u"Rehashing", LS(16)], [u"樹", u"Tree", LS(18)], [u"根／葉", u"Root / Leaf", LS(18)],
            [u"完全二元樹", u"Complete Binary Tree", LS(18)], [u"前序／中序／後序走訪", u"Preorder / Inorder / Postorder Traversal", LS(19)], [u"層序走訪", u"Level-order Traversal", LS(19)],
            [u"二元搜尋樹", u"Binary Search Tree (BST)", LS(20)], [u"中序後繼者", u"Inorder Successor", LS(21)], [u"AVL 樹", u"AVL Tree", LS(22)], [u"旋轉", u"Rotation", LS(22)],
            [u"平衡因子", u"Balance Factor", LS(22)], [u"紅黑樹", u"Red-Black Tree", LS(23)], [u"優先佇列", u"Priority Queue", LS(24)], [u"二元堆積", u"Binary Heap", LS(24)],
            [u"上浮／下沉", u"Sift Up / Sift Down", LS(24)], [u"建堆", u"Heapify", LS(25)], [u"B 樹／B+ 樹", u"B-tree / B+ tree", LS(28)], [u"字典樹", u"Trie / Prefix Tree", LS(29)],
            [u"線段樹", u"Segment Tree", LS(30)], [u"懶惰標記", u"Lazy Propagation", LS(30)], [u"樹狀陣列", u"Fenwick Tree / Binary Indexed Tree", LS(31)], [u"聯集—尋找", u"Union–Find / Disjoint Set Union", LS(32)],
            [u"路徑壓縮", u"Path Compression", LS(32)], [u"按秩合併", u"Union by Rank", LS(32)], [u"跳躍串列", u"Skip List", LS(33)], [u"鄰接矩陣／串列", u"Adjacency Matrix / List", LS(34)],
            [u"廣度／深度優先搜尋", u"BFS / DFS", LS(35)], [u"拓撲排序", u"Topological Sort", LS(36)], [u"有向無環圖", u"Directed Acyclic Graph (DAG)", LS(36)], [u"最短路徑", u"Shortest Path", LS(37)],
            [u"最小生成樹", u"Minimum Spanning Tree", LS(38)], [u"二分搜尋", u"Binary Search", LS(39)], [u"穩定排序", u"Stable Sort", LS(40)], [u"合併排序", u"Merge Sort", LS(41)],
            [u"快速排序", u"Quicksort", LS(41)], [u"樞紐", u"Pivot", LS(41)], [u"計數排序", u"Counting Sort", LS(42)], [u"基數排序", u"Radix Sort", LS(42)],
            [u"內省排序", u"Introsort", LS(43)], [u"LRU 快取", u"Least Recently Used Cache", LS(44)], [u"布隆過濾器", u"Bloom Filter", LS(45)], [u"偽陽性", u"False Positive", LS(45)],
            [u"持久化資料結構", u"Persistent Data Structure", LS(46)], [u"結構共享", u"Structural Sharing", LS(46)], [u"快取行", u"Cache Line", LS(47)], [u"局部性", u"Locality", LS(47)],
        ]),
    ],
}

REFERENCES = [LAB, CHEAT, GLOSSARY]
