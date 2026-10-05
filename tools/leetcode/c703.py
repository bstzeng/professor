# -*- coding: utf-8 -*-
"""第 703、704、705、706、707、709、710、712 題。"""
import random, heapq
from collections import Counter
from functools import lru_cache
from authoring import ap
from lcauto import em
from runner import Src

S = Src()
random.seed(703)


# ==================== 703. Kth Largest Element in a Stream ====================
S["p703"] = '''class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []                      # ★ 大小為 k 的最小堆積：堆頂就是第 k 大
        for x in nums:
            self.add(x)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)   # 比第 k 大還大：踢掉堆頂
        return self.heap[0]'''

_K = S.loadns("p703")["KthLargest"]
for _ in range(500):
    k = random.randint(1, 4); nums = [random.randint(-5, 5) for _ in range(random.randint(k - 1, 6))]
    o = _K(k, nums); allv = nums[:]
    for _ in range(10):
        v = random.randint(-5, 5); allv.append(v)
        assert o.add(v) == sorted(allv, reverse=True)[k - 1]
print("P703 OK")

em({
 "num": 703, "title": "資料流中的第 K 大元素",
 "desc": "維護大小為 k 的最小堆積：裡面是目前最大的 k 個數，堆頂就是第 k 大。",
 "zh": [
   "設計一個類別，找出資料流中<strong>第 k 大</strong>的元素（排序後的第 k 大，不是第 k 個不同的值）。",
   "<code>KthLargest(k, nums)</code> 用初始資料建立；<code>add(val)</code> 加入一個數並回傳目前的第 k 大。保證每次呼叫 add 時至少有 k 個數。",
 ],
 "idea": [
   ("c", """【只需要保留最大的 k 個】
    比第 k 大還小的數，永遠不可能再成為答案（之後只會加入更多數）。

【大小為 k 的最小堆積】
    堆積裡是目前最大的 k 個數，堆頂是其中最小的 = 第 k 大。
    新數 val：
        堆積還不滿 k 個 -> 直接放入
        val > 堆頂 -> 取代堆頂
        否則 -> 丟掉
    每次 O(log k)。"""),
 ],
 "approaches": [
   ap("解法", "大小為 k 的最小堆積", [("c", S["p703"])], "add：O(log k)", "O(k)", optimal=True),
 ],
 "edges": ["<strong>初始資料少於 k 個</strong> → 先放滿。", "<strong>重複值</strong> → 分別計算。"],
 "follow": [("h", "為什麼是最小堆積？"), ("c", "要快速知道「保留的 k 個裡最小的是誰」以決定是否淘汰，所以用最小堆積。找第 k 小則反過來用最大堆積。")],
 "related": ["<strong>第 215 題 陣列中的第 K 個最大元素</strong>", "<strong>第 295 題 資料流的中位數</strong>", "<strong>第 347 題 前 K 個高頻元素</strong>"],
 "check": ["為什麼比第 k 大還小的數可以直接丟掉？", "為什麼用最小堆積找第 k 大？"],
})


# ==================== 704. Binary Search ====================
S["p704"] = '''class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1           # 搜尋範圍 [lo, hi]（閉區間）
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1                # ★ target 在右半邊，mid 本身已經排除
            else:
                hi = mid - 1
        return -1'''

_p704 = S.load("p704")
for _ in range(3000):
    a = sorted(random.sample(range(-20, 20), random.randint(1, 10))); t = random.randint(-22, 22)
    assert _p704.search(a, t) == (a.index(t) if t in a else -1)
print("P704 OK")

em({
 "num": 704, "title": "二分搜尋",
 "desc": "二分搜尋的標準模板：閉區間 [lo, hi]、迴圈條件 lo ≤ hi、每次把 mid 排除在外。",
 "zh": ["給你一個<strong>遞增排序</strong>、元素互不相同的整數陣列 <code>nums</code> 和 <code>target</code>，找到 target 的索引，不存在則回傳 <code>-1</code>。要求 <code>O(log n)</code>。"],
 "idea": [
   ("c", """【閉區間模板】
    搜尋範圍 [lo, hi]，兩端都可能是答案。
    lo <= hi 時範圍非空，繼續：
        nums[mid] == target -> 找到
        nums[mid] <  target -> 答案在 [mid+1, hi]
        nums[mid] >  target -> 答案在 [lo, mid-1]
    mid 已經檢查過，下一輪不包含它 -> 範圍一定縮小，不會無窮迴圈。

【常見錯誤】
    區間定義和迴圈條件、更新方式不一致：
    例如用 [lo, hi) 半開區間卻寫 lo <= hi，或寫 hi = mid 卻用閉區間。"""),
 ],
 "approaches": [
   ap("解法", "閉區間二分", [("c", S["p704"])], "O(log n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>只有一個元素</strong> → lo == hi 時仍要檢查。", "<strong>target 比全部都小或都大</strong> → −1。"],
 "follow": [("h", "整數溢位"), ("c", "其他語言中 (lo + hi) / 2 可能溢位，改寫成 lo + (hi − lo) / 2。Java 的 Arrays.binarySearch 曾經就有這個 bug（2006 年才修正）。")],
 "related": ["<strong>第 35 題 搜尋插入位置</strong>", "<strong>第 34 題 在排序陣列中查找元素的第一個和最後一個位置</strong>", "<strong>第 744 題 尋找比目標字母大的最小字母</strong>"],
 "check": ["為什麼迴圈條件是 lo <= hi？", "更新時為什麼是 mid + 1 和 mid − 1？"],
})


# ==================== 705. Design HashSet ====================
S["p705"] = '''class MyHashSet:
    def __init__(self):
        self.size = 1009                        # 質數個桶，讓餘數分布比較均勻
        self.buckets = [[] for _ in range(self.size)]

    def _bucket(self, key):
        return self.buckets[key % self.size]    # ★ 雜湊函數：取餘數決定放哪個桶

    def add(self, key: int) -> None:
        b = self._bucket(key)
        if key not in b:
            b.append(key)                       # 碰撞：同一個桶裡用串列存放（鏈結法）

    def remove(self, key: int) -> None:
        b = self._bucket(key)
        if key in b:
            b.remove(key)

    def contains(self, key: int) -> bool:
        return key in self._bucket(key)'''

_HS = S.loadns("p705")["MyHashSet"]
o = _HS(); ref = set()
for _ in range(20000):
    k = random.randint(0, 5000); op = random.randint(0, 2)
    if op == 0: o.add(k); ref.add(k)
    elif op == 1: o.remove(k); ref.discard(k)
    else: assert o.contains(k) == (k in ref)
print("P705 OK")

em({
 "num": 705, "title": "設計雜湊集合",
 "desc": "雜湊函數（取餘數）把鍵分到固定數量的桶，桶內用串列處理碰撞（鏈結法）。",
 "zh": ["不使用任何內建的雜湊表函式庫，設計一個雜湊集合，支援 <code>add(key)</code>、<code>remove(key)</code>、<code>contains(key)</code>。鍵的範圍是 [0, 10⁶]。"],
 "idea": [
   ("c", """【最簡單：布林陣列】
    鍵範圍只有 10⁶ -> 開 10⁶+1 的陣列，O(1) 但浪費空間。

【真正的雜湊表】
    1. 雜湊函數：key % 桶數，決定放在哪個桶。
    2. 碰撞處理：不同的鍵可能落在同一個桶，
       鏈結法 —— 每個桶是一個串列。
    3. 桶數選質數：讓餘數分布更均勻。

【效能】
    鍵數 / 桶數 = 負載因子 α，每個操作平均 O(1 + α)。
    實際的雜湊表會在 α 太大時擴容（重新雜湊）。"""),
 ],
 "approaches": [
   ap("解法", "鏈結法雜湊表", [("c", S["p705"]), "驗證方式：和內建 set 對照執行兩萬次隨機操作。"], "平均 O(1 + α)", "O(桶數 + 鍵數)", optimal=True),
 ],
 "edges": ["<strong>重複 add</strong> → 不重複放。", "<strong>remove 不存在的鍵</strong> → 不做事。"],
 "follow": [("h", "另一種碰撞處理：開放定址"), ("c", "所有鍵都放在同一個陣列裡，碰撞時往後找下一個空位（線性探測）。Python 的 dict 就是開放定址（用擾動過的探測序列）。刪除時要留「墓碑」標記，否則會切斷探測鏈。")],
 "related": ["<strong>第 706 題 設計雜湊映射</strong>", "<strong>第 380 題 O(1) 時間插入、刪除和取得隨機元素</strong>"],
 "check": ["什麼是碰撞？鏈結法怎麼處理？", "為什麼桶數常選質數？"],
})


# ==================== 706. Design HashMap ====================
S["p706"] = '''class MyHashMap:
    def __init__(self):
        self.size = 1009
        self.buckets = [[] for _ in range(self.size)]   # 每個桶存 [key, value] 對

    def put(self, key: int, value: int) -> None:
        b = self.buckets[key % self.size]
        for pair in b:
            if pair[0] == key:
                pair[1] = value         # ★ 鍵已存在：更新值
                return
        b.append([key, value])

    def get(self, key: int) -> int:
        for k, v in self.buckets[key % self.size]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        b = self.buckets[key % self.size]
        for i, (k, _) in enumerate(b):
            if k == key:
                b.pop(i)
                return'''

_HM = S.loadns("p706")["MyHashMap"]
o = _HM(); ref = {}
for _ in range(20000):
    k = random.randint(0, 5000); op = random.randint(0, 2)
    if op == 0:
        v = random.randint(0, 9); o.put(k, v); ref[k] = v
    elif op == 1: o.remove(k); ref.pop(k, None)
    else: assert o.get(k) == ref.get(k, -1)
print("P706 OK")

em({
 "num": 706, "title": "設計雜湊映射",
 "desc": "和第 705 題相同的鏈結法，桶裡存鍵值對；put 時鍵已存在就更新值。",
 "zh": ["不使用任何內建的雜湊表函式庫，設計一個雜湊映射，支援 <code>put(key, value)</code>（鍵已存在則更新）、<code>get(key)</code>（不存在回傳 −1）、<code>remove(key)</code>。"],
 "idea": [
   ("c", """【第 705 題 + 值】
    桶裡存 [key, value]。
    put：在桶中找 key，有就更新、沒有就新增。
    get：在桶中找 key。
    remove：在桶中找到後刪除。

    和集合唯一的差別是要記住值，並處理「更新」。"""),
 ],
 "approaches": [
   ap("解法", "鏈結法雜湊映射", [("c", S["p706"]), "驗證方式：和內建 dict 對照執行兩萬次隨機操作。"], "平均 O(1 + α)", "O(桶數 + 鍵數)", optimal=True),
 ],
 "edges": ["<strong>put 已存在的鍵</strong> → 更新，不是新增。", "<strong>get 不存在的鍵</strong> → −1。"],
 "follow": [("h", "動態擴容"), ("c", "當鍵數 / 桶數超過某個門檻（例如 0.75），把桶數加倍並重新分配所有鍵。單次擴容 O(n)，但均攤到每次插入仍是 O(1)。")],
 "related": ["<strong>第 705 題 設計雜湊集合</strong>", "<strong>第 146 題 LRU 快取</strong>"],
 "check": ["put 一個已存在的鍵時要做什麼？"],
})


# ==================== 707. Design Linked List ====================
S["p707"] = '''class MyLinkedList:
    class Node:
        __slots__ = ("val", "next")
        def __init__(self, val, nxt=None):
            self.val, self.next = val, nxt

    def __init__(self):
        self.dummy = self.Node(0)       # ★ 虛擬頭節點：插入或刪除第 0 個元素時不用特判
        self.size = 0

    def _prev(self, index):             # 回傳第 index 個節點的前一個節點
        nd = self.dummy
        for _ in range(index):
            nd = nd.next
        return nd

    def get(self, index: int) -> int:
        if not 0 <= index < self.size:
            return -1
        return self._prev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if not 0 <= index <= self.size:
            return
        p = self._prev(index)
        p.next = self.Node(val, p.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if not 0 <= index < self.size:
            return
        p = self._prev(index)
        p.next = p.next.next
        self.size -= 1'''

_LL = S.loadns("p707")["MyLinkedList"]
for _ in range(300):
    o = _LL(); ref = []
    for _ in range(40):
        op = random.randint(0, 4); i = random.randint(-1, len(ref) + 1); v = random.randint(0, 9)
        if op == 0: assert o.get(i) == (ref[i] if 0 <= i < len(ref) else -1)
        elif op == 1: o.addAtHead(v); ref.insert(0, v)
        elif op == 2: o.addAtTail(v); ref.append(v)
        elif op == 3:
            o.addAtIndex(i, v)
            if 0 <= i <= len(ref): ref.insert(i, v)
        else:
            o.deleteAtIndex(i)
            if 0 <= i < len(ref): ref.pop(i)
print("P707 OK")

em({
 "num": 707, "title": "設計鏈結串列",
 "desc": "虛擬頭節點 + 長度計數：所有操作都化成「找到第 index 個節點的前一個」，不需要對頭節點特判。",
 "zh": [
   "設計一個鏈結串列（單向或雙向皆可），支援：",
   ("ul", ["<code>get(index)</code>：取得第 index 個節點的值，無效則回傳 −1。",
           "<code>addAtHead(val)</code>、<code>addAtTail(val)</code>：加在頭、尾。",
           "<code>addAtIndex(index, val)</code>：插在第 index 個節點之前；index 等於長度時加在尾端；大於長度時不插入。",
           "<code>deleteAtIndex(index)</code>：刪除第 index 個節點（index 有效時）。"]),
 ],
 "idea": [
   ("c", """【虛擬頭節點（dummy）】
    在真正的第一個節點前面放一個假節點。
    「在第 0 個位置插入」= 在 dummy 後面插入，
    和在中間插入的程式碼完全一樣，不用特判 head。

【所有操作都找「前一個節點」】
    _prev(index)：從 dummy 往後走 index 步。
    插入：p.next = 新節點(val, p.next)
    刪除：p.next = p.next.next

【記錄長度】
    方便檢查 index 是否有效，addAtTail 也只是 addAtIndex(size)。"""),
 ],
 "approaches": [
   ap("解法", "虛擬頭節點的單向串列", [("c", S["p707"]), "驗證方式：和 Python list 對照，隨機執行 300 組操作序列（含無效索引）。"], "get / add / delete：O(index)", "O(n)", "addAtHead O(1)", "", optimal=True),
 ],
 "edges": ["<strong>index == size</strong> → addAtIndex 加在尾端；deleteAtIndex 無效。", "<strong>負的 index</strong> → 無效。"],
 "follow": [("h", "雙向串列"), ("c", "加上 prev 指標與尾端虛擬節點：可以從比較近的一端開始走（最多走 n/2），addAtTail 變成 O(1)。第 146 題（LRU 快取）就用雙向串列。")],
 "related": ["<strong>第 146 題 LRU 快取</strong>", "<strong>第 203 題 移除鏈結串列元素</strong>", "<strong>第 641 題 設計循環雙端佇列</strong>"],
 "check": ["虛擬頭節點解決了什麼問題？", "插入與刪除都需要找到哪個節點？"],
})


# ==================== 709. To Lower Case ====================
S["p709"] = '''class Solution:
    def toLowerCase(self, s: str) -> str:
        # ★ ASCII 中大寫 A-Z 是 65-90，小寫是 97-122，相差 32（恰好是第 5 個位元）
        return "".join(chr(ord(c) | 32) if "A" <= c <= "Z" else c for c in s)'''

_p709 = S.load("p709")
for _ in range(2000):
    s = "".join(random.choice("aZbY09 ,.!Qq") for _ in range(random.randint(1, 10)))
    assert _p709.toLowerCase(s) == s.lower()
print("P709 OK")

em({
 "num": 709, "title": "轉換成小寫字母",
 "desc": "大寫與小寫字母的 ASCII 碼相差 32，也就是第 5 個位元：大寫字母 OR 32 就變成小寫。",
 "zh": ["給你字串 <code>s</code>，把其中所有大寫字母轉成小寫後回傳。"],
 "idea": [
   ("c", """【內建】s.lower()

【自己做：ASCII 的設計】
    'A' = 65 = 0b1000001
    'a' = 97 = 0b1100001
    差 32 = 0b0100000 —— 只差第 5 個位元。
    所以：
        轉小寫：c | 32
        轉大寫：c & ~32
        大小寫互換：c ^ 32
    只對字母做，其他字元保持不變。"""),
 ],
 "approaches": [
   ap("解法", "ASCII 位元運算", [("c", S["p709"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>非字母字元</strong> → 不能做位元運算（例如 '@' | 32 會變成 '`'）。"],
 "follow": [("h", "Unicode"), ("c", "ASCII 的技巧只適用於英文字母。Unicode 的大小寫轉換很複雜：德文 ß 的大寫是 SS（長度改變）、土耳其語的 i 有帶點與不帶點兩種——實務上一定要用語言內建的函式。")],
 "related": ["<strong>第 520 題 檢測大寫字母</strong>", "<strong>第 1832 題 判斷句子是否為全字母句</strong>"],
 "check": ["大寫和小寫字母的 ASCII 碼差多少？為什麼可以用 OR？"],
})


# ==================== 710. Random Pick with Blacklist ====================
S["p710"] = '''class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.bound = n - len(blacklist)         # 只在 [0, bound) 中隨機
        black = set(blacklist)
        self.remap = {}
        w = self.bound                          # 從 [bound, n) 中找白名單的數
        for b in blacklist:
            if b < self.bound:                  # ★ 落在隨機範圍內的黑名單，映射到範圍外的白名單數
                while w in black:
                    w += 1
                self.remap[b] = w
                w += 1

    def pick(self) -> int:
        x = random.randrange(self.bound)
        return self.remap.get(x, x)'''

_cls710 = S.loadns("p710")["Solution"]
for _ in range(300):
    n = random.randint(1, 12); bl = random.sample(range(n), random.randint(0, n - 1))
    o = _cls710(n, bl); white = set(range(n)) - set(bl)
    got = Counter(o.pick() for _ in range(300 * len(white)))
    assert set(got) == white
o = _cls710(10, [1, 3, 5, 7]); c = Counter(o.pick() for _ in range(60000))
assert all(abs(v - 10000) < 800 for v in c.values())
print("P710 OK")

em({
 "num": 710, "title": "黑名單中的隨機數",
 "desc": "只在 [0, n−|B|) 中隨機；落在這個範圍內的黑名單數，預先映射到範圍外的白名單數。每次 pick 只呼叫一次亂數。",
 "zh": [
   "給你整數 <code>n</code> 和不重複的黑名單 <code>blacklist</code>。設計 <code>pick()</code>：在 <code>[0, n − 1]</code> 中<strong>不在黑名單</strong>的整數裡均勻隨機選一個。",
   "請盡量減少呼叫內建亂數函式的次數。（n 可達 10⁹。）",
 ],
 "idea": [
   ("c", """【白名單有 W = n - |B| 個】
    想要在 [0, W) 中均勻選一個「編號」，再對應到白名單的某個數。

【映射】
    [0, W) 中的數若不在黑名單 -> 對應自己。
    [0, W) 中的黑名單數有 t 個，
    而 [W, n) 中恰好有 t 個白名單數（數量剛好互補）。
    把它們一一配對：黑名單 b -> 範圍外的白名單 w。

【pick】
    x = 隨機 [0, W)，回傳 remap.get(x, x)。
    一次亂數、O(1)。

【空間】
    只為黑名單建映射，O(|B|)，不受 n = 10⁹ 影響。"""),
 ],
 "approaches": [
   ap("解法", "範圍縮減 + 黑名單重映射", [("c", S["p710"]), "驗證方式：小規模時檢查每個白名單數都會被選到、黑名單數不會出現；六萬次抽樣檢查分布均勻。"], "建構 O(|B|)，pick O(1)", "O(|B|)", optimal=True),
 ],
 "edges": ["<strong>黑名單全在 [W, n)</strong> → 不需要映射。", "<strong>黑名單為空</strong> → 直接在 [0, n) 隨機。"],
 "follow": [("h", "為什麼不用拒絕抽樣？"), ("c", "隨機到黑名單就重抽：黑名單佔大部分時期望要抽很多次。本題要求減少亂數呼叫，映射法保證每次只抽一次。")],
 "related": ["<strong>第 519 題 隨機翻轉矩陣</strong>", "<strong>第 380 題 O(1) 時間插入、刪除和取得隨機元素</strong>", "<strong>第 528 題 按權重隨機選擇</strong>"],
 "check": ["[0, W) 中的黑名單數和 [W, n) 中的白名單數為什麼一樣多？", "pick 為什麼只需要一次亂數？"],
})


# ==================== 712. Minimum ASCII Delete Sum for Two Strings ====================
S["p712"] = '''class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]      # dp[i][j]：s1 前 i 個、s2 前 j 個的最小刪除成本
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])    # s2 是空的：s1 全刪
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]          # ★ 相同字元保留，不花成本
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]),   # 刪 s1 的
                                   dp[i][j - 1] + ord(s2[j - 1]))   # 刪 s2 的
        return dp[m][n]'''

_p712 = S.load("p712")
assert _p712.minimumDeleteSum("sea", "eat") == 231 and _p712.minimumDeleteSum("delete", "leet") == 403
@lru_cache(None)
def _bf712(a, b):
    if not a: return sum(map(ord, b))
    if not b: return sum(map(ord, a))
    r = min(ord(a[0]) + _bf712(a[1:], b), ord(b[0]) + _bf712(a, b[1:]))
    if a[0] == b[0]: r = min(r, _bf712(a[1:], b[1:]))
    return r
for _ in range(1500):
    a = "".join(random.choice("abc") for _ in range(random.randint(1, 6)))
    b = "".join(random.choice("abc") for _ in range(random.randint(1, 6)))
    assert _p712.minimumDeleteSum(a, b) == _bf712(a, b)
print("P712 OK")

em({
 "num": 712, "title": "兩個字串的最小 ASCII 刪除和",
 "desc": "第 583 題的加權版：刪除字元的成本是它的 ASCII 值，DP 結構相同，只是把 +1 換成 +ord(c)。",
 "zh": ["給你兩個字串 <code>s1</code>、<code>s2</code>，刪除一些字元使兩者相同，回傳被刪除字元的 <strong>ASCII 值總和</strong>的最小值。"],
 "idea": [
   ("c", """【和第 583 題相同的 DP】
    dp[i][j] = 讓 s1[:i] 與 s2[:j] 相同的最小刪除成本。
        s1[i-1] == s2[j-1] -> 保留，dp[i-1][j-1]
        否則 -> 刪 s1[i-1] 或刪 s2[j-1]，取較小：
               min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

【邊界】
    一邊是空字串 -> 另一邊全刪，成本是 ASCII 總和。

【另一個角度】
    總成本 - 2 × （保留下來的共同子序列的 ASCII 和的最大值）——
    最大權重的共同子序列。"""),
 ],
 "approaches": [
   ap("解法", "二維 DP", [("c", S["p712"]), "驗證方式：和記憶化遞迴比對 1500 組。"], "O(mn)", "O(mn)", "", "可壓成一維", optimal=True),
 ],
 "edges": ["<strong>完全沒有共同字元</strong> → 兩字串的 ASCII 總和。", "<strong>相同字元</strong> → 保留一定不比刪除差。"],
 "follow": [("h", "為什麼相同時一定保留？"), ("c", "若 s1[i−1] == s2[j−1] 但最優解刪了其中一個，把它們改成「一起保留」不會增加成本——所以直接取 dp[i−1][j−1] 是安全的。")],
 "related": ["<strong>第 583 題 兩個字串的刪除操作</strong>", "<strong>第 1143 題 最長共同子序列</strong>", "<strong>第 72 題 編輯距離</strong>"],
 "check": ["和第 583 題相比，DP 改了哪裡？", "邊界條件是什麼？"],
})
