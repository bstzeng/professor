# -*- coding: utf-8 -*-
"""第 459–464 題。"""
import random
import itertools
import functools
from collections import Counter, defaultdict, OrderedDict
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(459)


# ==================== 459. Repeated Substring Pattern ====================
S["p459"] = '''class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # ★ s 由某個子字串重複組成 <=> s 出現在 (s + s) 去掉頭尾字元之後的字串裡
        return s in (s + s)[1:-1]'''

S["p459_div"] = '''class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for L in range(1, n // 2 + 1):          # 枚舉子字串長度（必須整除 n）
            if n % L == 0 and s[:L] * (n // L) == s:
                return True
        return False'''

S["p459_kmp"] = '''class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        pi = [0] * n                             # KMP 前綴函數：最長相等前後綴
        for i in range(1, n):
            k = pi[i - 1]
            while k and s[i] != s[k]:
                k = pi[k - 1]
            if s[i] == s[k]:
                k += 1
            pi[i] = k
        period = n - pi[-1]                      # 最小週期
        return pi[-1] > 0 and n % period == 0'''

_p459 = [S.load(x) for x in ("p459", "p459_div", "p459_kmp")]
for s, want in [("abab", True), ("aba", False), ("abcabcabcabc", True), ("a", False), ("aaaa", True)]:
    for sol in _p459:
        assert sol.repeatedSubstringPattern(s) == want
for _ in range(3000):
    if random.random() < 0.5:
        s = "".join(random.choice("ab") for _ in range(random.randrange(1, 4))) * random.randint(1, 4)
    else:
        s = "".join(random.choice("ab") for _ in range(random.randrange(1, 10)))
    want = any(len(s) % L == 0 and s[:L] * (len(s) // L) == s for L in range(1, len(s)))
    for sol in _p459:
        assert sol.repeatedSubstringPattern(s) == want, (s, sol)
print("P459 OK")

emit({
 "num": 459, "slug": "repeated-substring-pattern",
 "en": [
   "Given a string <code>s</code>, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，判斷它能不能由它的某個子字串<strong>重複多次</strong>（至少兩次）組成。",
 ],
 "examples": """範例 1
  輸入：s = "abab"
  輸出：true
  說明："ab" 重複兩次。

範例 2
  輸入：s = "aba"
  輸出：false

範例 3
  輸入：s = "abcabcabcabc"
  輸出：true""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁴",
   "<code>s</code> 只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【方法一：枚舉子字串長度】
    子字串長度 L 必須整除 n，檢查 s[:L] 重複 n/L 次是否等於 s。
    O(n × 因數個數)。

【方法二：s + s 的技巧】
    如果 s = t 重複 k 次（k >= 2），
    s + s = t 重複 2k 次，去掉第一個和最後一個字元後，
    中間仍然包含一個完整的 s（從第二個 t 開始）。
    反過來，如果 s 出現在 (s+s)[1:-1] 裡，
    代表 s 旋轉某個非零位移後等於自己 -> s 有週期 -> 由重複組成。

【方法三：KMP 前綴函數】
    pi[n-1] = s 最長的「相等前綴與後綴」長度。
    最小週期 = n - pi[n-1]。
    週期能整除 n（而且 pi > 0）-> 由重複組成。"""),
 ],
 "approaches": [
   ap("解法一", "枚舉子字串長度", [
     ("c", S["p459_div"]),
   ], "O(n · d(n))", "O(n)", "d(n) = n 的因數個數", ""),

   ap("解法二", "s + s 技巧", [
     ("c", S["p459"]),
   ], "O(n)", "O(n)", "Python 的子字串搜尋平均很快", "", optimal=True),

   ap("解法三", "KMP 前綴函數", [
     ("c", S["p459_kmp"]),
   ], "O(n)", "O(n)", "保證線性", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、枚舉長度", "O(n·d(n))", "最直觀"],
    ["二、s + s", "O(n)", "一行 ✔"],
    ["三、KMP", "O(n)", "最壞情況也線性"]]),
 "edges": [
   "<strong>長度 1</strong> → false（至少要重複兩次）。",
   "<strong>全部相同</strong>（\"aaaa\"）→ true。",
   "<strong>週期不整除長度</strong>（\"abaab\"）→ false。",
 ],
 "follow": [
   ("h", "字串週期"),
   ("c", "「最小週期 = n − π[n−1]」是 KMP 前綴函數最重要的應用之一，也用在第 214 題（最短回文串）、第 1392 題（最長快樂前綴）。"),
 ],
 "related": [
   "<strong>第 28 題 找出字串中第一個匹配項的索引</strong> —— KMP",
   "<strong>第 796 題 旋轉字串</strong> —— 同樣的 s + s 技巧",
   "<strong>第 214 題 最短回文串</strong>",
 ],
 "check": [
   "為什麼要去掉 s + s 的頭尾字元？",
   "KMP 前綴函數怎麼算出最小週期？",
 ],
})


# ==================== 460. LFU Cache ====================
S["p460"] = '''class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.val = {}                                   # key -> value
        self.freq = {}                                  # key -> 使用次數
        self.groups = collections.defaultdict(collections.OrderedDict)  # 次數 -> 依使用時間排序的 keys
        self.min_freq = 0

    def _touch(self, key: int) -> None:                 # 使用一次：次數 +1，搬到下一組
        f = self.freq[key]
        del self.groups[f][key]
        if not self.groups[f]:
            del self.groups[f]
            if self.min_freq == f:
                self.min_freq = f + 1
        self.freq[key] = f + 1
        self.groups[f + 1][key] = None                  # 放在這一組的最後（最新）

    def get(self, key: int) -> int:
        if key not in self.val:
            return -1
        self._touch(key)
        return self.val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.val:
            self.val[key] = value
            self._touch(key)
            return
        if len(self.val) == self.cap:
            # ★ 淘汰：次數最少的那一組裡，最久沒用的（OrderedDict 的第一個）
            old, _ = self.groups[self.min_freq].popitem(last=False)
            if not self.groups[self.min_freq]:
                del self.groups[self.min_freq]
            del self.val[old], self.freq[old]
        self.val[key] = value
        self.freq[key] = 1
        self.groups[1][key] = None
        self.min_freq = 1                               # 新 key 的次數一定是最少的'''


class _LFURef:
    def __init__(self, cap):
        self.cap, self.d, self.t = cap, {}, 0

    def get(self, k):
        if k not in self.d:
            return -1
        v, f, _ = self.d[k]
        self.t += 1
        self.d[k] = (v, f + 1, self.t)
        return v

    def put(self, k, v):
        if self.cap == 0:
            return
        self.t += 1
        if k in self.d:
            _, f, _ = self.d[k]
            self.d[k] = (v, f + 1, self.t)
            return
        if len(self.d) == self.cap:
            victim = min(self.d, key=lambda x: (self.d[x][1], self.d[x][2]))
            del self.d[victim]
        self.d[k] = (v, 1, self.t)


_cls = S.loadns("p460")["LFUCache"]
for _ in range(500):
    cap = random.randint(0, 4)
    a, b = _cls(cap), _LFURef(cap)
    for _ in range(60):
        k = random.randrange(6)
        if random.random() < 0.5:
            assert a.get(k) == b.get(k)
        else:
            v = random.randrange(100)
            a.put(k, v)
            b.put(k, v)
print("P460 OK")

_P460_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">依「使用次數」分組；每一組內再依「最近使用時間」排序</text>
            <g font-size="12">
              <text x="30" y="62" fill="var(--accent)">次數 1</text>
              <rect x="100" y="46" width="44" height="26" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="122" y="64" text-anchor="middle" fill="#ff8a65">k3</text>
              <rect x="150" y="46" width="44" height="26" fill="none" stroke="var(--border)"/><text x="172" y="64" text-anchor="middle" fill="var(--text)">k5</text>
              <text x="30" y="106" fill="var(--accent)">次數 2</text>
              <rect x="100" y="90" width="44" height="26" fill="none" stroke="var(--border)"/><text x="122" y="108" text-anchor="middle" fill="var(--text)">k1</text>
              <text x="30" y="150" fill="var(--accent)">次數 4</text>
              <rect x="100" y="134" width="44" height="26" fill="none" stroke="var(--border)"/><text x="122" y="152" text-anchor="middle" fill="var(--text)">k2</text>
              <rect x="150" y="134" width="44" height="26" fill="none" stroke="var(--border)"/><text x="172" y="152" text-anchor="middle" fill="var(--text)">k4</text>
            </g>
            <text x="100" y="186" fill="var(--text-muted)" font-size="11">← 最久沒用　　最近使用 →</text>
            <text x="250" y="62" fill="#ff8a65" font-size="12">滿了要淘汰：min_freq = 1 那一組的第一個 → k3</text>
            <text x="250" y="106" fill="var(--text)" font-size="12">get(k1)：k1 從「次數 2」搬到「次數 3」組的最後面</text>
            <text x="250" y="150" fill="var(--text)" font-size="12">put 新 key：放進「次數 1」組，min_freq 重設為 1</text>
            <text x="20" y="220" fill="var(--gold)" font-size="12">★ 次數每次只 +1，所以只會搬到相鄰的組；min_freq 只會 +1 或重設為 1 —— 全部 O(1)。</text>'''

emit({
 "num": 460, "slug": "lfu-cache",
 "en": [
   "Design and implement a data structure for a <a href=\"https://en.wikipedia.org/wiki/Least_frequently_used\">Least Frequently Used (LFU)</a> cache.",
   "Implement the <code>LFUCache</code> class:",
   ("ul", ["<code>LFUCache(int capacity)</code> Initializes the object with the <code>capacity</code> of the data structure.",
           "<code>int get(int key)</code> Gets the value of the <code>key</code> if the <code>key</code> exists in the cache. Otherwise, returns <code>-1</code>.",
           "<code>void put(int key, int value)</code> Update the value of the <code>key</code> if present, or inserts the <code>key</code> if not already present. When the cache reaches its <code>capacity</code>, it should invalidate and remove the <strong>least frequently used</strong> key before inserting a new item. For this problem, when there is a <strong>tie</strong> (i.e., two or more keys with the same frequency), the <strong>least recently used</strong> <code>key</code> would be invalidated."]),
   "To determine the least frequently used key, a <strong>use counter</strong> is maintained for each key in the cache. The key with the smallest <strong>use counter</strong> is the least frequently used key. When a key is first inserted into the cache, its <strong>use counter</strong> is set to <code>1</code> (due to the <code>put</code> operation). The <strong>use counter</strong> for a key in the cache is incremented either a <code>get</code> or <code>put</code> operation is called on it.",
   "The functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> average time complexity.",
 ],
 "zh": [
   "設計一個 <strong>LFU（最不常使用）快取</strong>：",
   ("ul", ["<code>get(key)</code>：存在就回傳值，否則回傳 −1。",
           "<code>put(key, value)</code>：存在就更新值，否則插入。快取滿了的時候，先淘汰<strong>使用次數最少</strong>的 key；次數相同時，淘汰<strong>最久沒被使用</strong>的那個。"]),
   "每個 key 有一個使用次數：插入時設為 1，之後每次 <code>get</code> 或 <code>put</code> 都 +1。",
   "<code>get</code> 和 <code>put</code> 的平均時間都必須是 <code>O(1)</code>。",
 ],
 "examples": """範例
  LFUCache(2)
  put(1, 1), put(2, 2)
  get(1)    -> 1      （1 的次數 2，2 的次數 1）
  put(3, 3)           （淘汰次數最少的 2）
  get(2)    -> -1
  get(3)    -> 3      （1 和 3 的次數都是 2）
  put(4, 4)           （次數相同，淘汰最久沒用的 1）
  get(1)    -> -1""",
 "constraints": [
   "1 ≤ <code>capacity</code> ≤ 10⁴",
   "0 ≤ <code>key</code> ≤ 10⁵，0 ≤ <code>value</code> ≤ 10⁹",
   "最多呼叫 2 × 10⁵ 次",
 ],
 "idea": [
   ("fig", _P460_FIG, "0 0 640 234"),
   ("c", """【需要同時知道兩件事】
    1. 哪些 key 的次數最少？
    2. 同樣次數中，哪個最久沒用？

【結構：次數 -> 一條「依使用時間排序」的串列】
    groups[f] = 所有次數為 f 的 key，最舊的在前面（就是一個小 LRU）
    min_freq  = 目前最小的次數

    使用一次 key（get 或 put 已存在的 key）：
        從 groups[f] 移除，加到 groups[f+1] 的最後面
        如果 groups[f] 空了而且 f == min_freq -> min_freq += 1
    淘汰：
        groups[min_freq] 的第一個（最舊的）
    插入新 key：
        放進 groups[1]，min_freq = 1

【Python 的 OrderedDict】
    有序字典本身就是「雜湊表 + 雙向鏈結串列」：
    刪除任意 key、在尾端加入、從頭部彈出都是 O(1)。

【和第 432 題（All O`one）的結構一樣】"""),
 ],
 "approaches": [
   ap("解法", "次數分組的 OrderedDict + min_freq", [
     ("c", S["p460"]),
     "驗證方式：和一個「直接用 (次數, 最後使用時間) 找最小值」的 O(n) 參考實作，隨機比對五百組操作序列。",
   ], "get / put O(1)", "O(capacity)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>capacity = 0</strong> → 什麼都不存（原題 capacity ≥ 1，但寫法仍應處理）。",
   "<strong>put 已存在的 key</strong> → 更新值，而且次數 +1。",
   "<strong>次數相同</strong> → 淘汰最久沒用的。",
   "<strong>min_freq 什麼時候更新</strong> → 只有「最小那一組被搬空」或「插入新 key」時。",
 ],
 "follow": [
   ("h", "LRU vs LFU"),
   ("c", "LRU（第 146 題）只看「最近一次什麼時候用」，對突發的大量掃描很敏感；LFU 看「用了幾次」，能保留長期熱門的資料，但新資料很容易被淘汰。實務上常用兩者的混合（例如 Redis 的 LFU 會讓次數隨時間衰減）。"),
 ],
 "related": [
   "<strong>第 146 題 LRU 快取</strong>",
   "<strong>第 432 題 全 O(1) 的資料結構</strong>",
 ],
 "check": [
   "淘汰時要找哪一個 key？",
   "min_freq 在什麼時候改變？",
   "為什麼 OrderedDict 適合用在這裡？",
 ],
})


# ==================== 461. Hamming Distance ====================
S["p461"] = '''class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y                  # ★ 不同的位元在 XOR 後是 1
        count = 0
        while z:
            z &= z - 1             # 每次清掉最低位的 1
            count += 1
        return count'''

_p461 = S.load("p461")
for _ in range(5000):
    x, y = random.randint(0, 2 ** 31 - 1), random.randint(0, 2 ** 31 - 1)
    assert _p461.hammingDistance(x, y) == bin(x ^ y).count("1")
print("P461 OK")

emit({
 "num": 461, "slug": "hamming-distance",
 "en": [
   "The <a href=\"https://en.wikipedia.org/wiki/Hamming_distance\">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.",
   "Given two integers <code>x</code> and <code>y</code>, return <em>the <strong>Hamming distance</strong> between them</em>.",
 ],
 "zh": [
   "兩個整數的<strong>漢明距離</strong>是它們二進位表示中，對應位元<strong>不同</strong>的位置數量。",
   "給你 <code>x</code> 和 <code>y</code>，回傳它們的漢明距離。",
 ],
 "examples": """範例 1
  輸入：x = 1, y = 4
  輸出：2
  說明：
    1   (0 0 0 1)
    4   (0 1 0 0)
           ↑   ↑

範例 2
  輸入：x = 3, y = 1
  輸出：1""",
 "constraints": [
   "0 ≤ <code>x, y</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【XOR：相同為 0、不同為 1】
    x ^ y 的每一個 1，就是一個不同的位元。
    問題變成：數 x ^ y 有幾個 1（第 191 題）。

【Brian Kernighan：z &= z - 1】
    每次清掉最低位的 1，執行幾次就有幾個 1。
    比逐位檢查快：只跑「1 的個數」次。"""),
 ],
 "approaches": [
   ap("解法", "XOR + 數 1 的個數", [
     ("c", S["p461"]),
     "Python 也可以直接寫 <code>bin(x ^ y).count(\"1\")</code>，或 3.10 以上的 <code>(x ^ y).bit_count()</code>。",
   ], "O(1)", "O(1)", "最多 31 次", "", optimal=True),
 ],
 "edges": [
   "<strong>x = y</strong> → 0。",
   "<strong>其中一個是 0</strong> → 另一個的 1 的個數。",
 ],
 "follow": [
   ("h", "漢明距離的應用"),
   ("c", "錯誤更正碼（漢明碼）、DNA 序列比對、相似雜湊（SimHash 用漢明距離判斷兩篇文章是否相似）。"),
 ],
 "related": [
   "<strong>第 191 題 位元 1 的個數</strong>",
   "<strong>第 477 題 漢明距離總和</strong>",
 ],
 "check": [
   "為什麼 x ^ y 的 1 就代表不同的位元？",
   "z &amp;= z − 1 做了什麼？",
 ],
})


# ==================== 462. Minimum Moves to Equal Array Elements II ====================
S["p462"] = '''class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]              # ★ 全部移到中位數，總距離最小
        return sum(abs(x - median) for x in nums)'''

S["p462_pair"] = '''class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        i, j, moves = 0, len(nums) - 1, 0
        while i < j:                               # 最小和最大配對：要移動的距離就是它們的差
            moves += nums[j] - nums[i]
            i += 1
            j -= 1
        return moves'''

_p462 = [S.load(x) for x in ("p462", "p462_pair")]
for _ in range(3000):
    a = [random.randint(-10, 10) for _ in range(random.randrange(1, 9))]
    want = min(sum(abs(x - t) for x in a) for t in range(-10, 11))
    for sol in _p462:
        assert sol.minMoves2(list(a)) == want
print("P462 OK")

emit({
 "num": 462, "slug": "minimum-moves-to-equal-array-elements-ii",
 "en": [
   "Given an integer array <code>nums</code> of size <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.",
   "In one move, you can increment or decrement an element of the array by <code>1</code>.",
   "Test cases are designed so that the answer will fit in a <strong>32-bit</strong> integer.",
 ],
 "zh": [
   "給你一個整數陣列，每一步可以把任一個元素 +1 或 −1。回傳讓所有元素相等的最少步數。",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3]
  輸出：2
  說明：[1,2,3] => [2,2,3] => [2,2,2]

範例 2
  輸入：nums = [1,10,2,9]
  輸出：16""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
 ],
 "idea": [
   ("c", """【選一個目標值 t，總步數 = Σ |x - t|】
    要讓絕對距離和最小 -> t 取中位數。

【為什麼是中位數？】
    把數排序後，最小和最大配成一對：
    不管 t 放在它們之間哪裡，這一對的距離和都是 (max - min)；
    放在外面只會更多。
    第二小和第二大再配一對……
    中位數同時在所有配對的中間 -> 每一對都達到最小。

【配對的寫法】
    答案 = Σ (nums[n-1-i] - nums[i])，i < n/2
    完全不需要算出中位數是多少。

【O(n)】
    用快速選擇（第 215 題）找中位數，平均 O(n)。"""),
 ],
 "approaches": [
   ap("解法一", "排序 + 中位數", [
     ("c", S["p462"]),
   ], "O(n log n)", "O(1)", "", "", optimal=True),

   ap("解法二", "排序 + 頭尾配對", [
     ("c", S["p462_pair"]),
   ], "O(n log n)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、中位數", "O(n log n)", "✔"],
    ["二、頭尾配對", "O(n log n)", "直接顯示為什麼是中位數"],
    ["快速選擇", "平均 O(n)", "不需要完整排序"]]),
 "edges": [
   "<strong>偶數個元素</strong> → 兩個中位數之間的任何值都一樣好。",
   "<strong>只有一個</strong> → 0。",
 ],
 "follow": [
   ("h", "中位數 vs 平均數"),
   ("c", "絕對距離和 Σ|x − t| 的最小值在中位數；平方距離和 Σ(x − t)² 的最小值在平均數。第 296 題（最佳碰頭地點，付費）是二維的中位數問題。"),
 ],
 "related": [
   "<strong>第 453 題 最小操作次數使陣列元素相等</strong>",
   "<strong>第 296 題 最佳碰頭地點</strong>（付費）",
   "<strong>第 2033 題 獲取單值網格的最小操作數</strong>",
 ],
 "check": [
   "為什麼目標值要取中位數？",
   "頭尾配對的寫法為什麼正確？",
 ],
})


# ==================== 463. Island Perimeter ====================
S["p463"] = '''class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        land = shared = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v:
                    land += 1
                    if i and grid[i - 1][j]:       # 和上面的陸地共用一條邊
                        shared += 1
                    if j and row[j - 1]:           # 和左邊的陸地共用一條邊
                        shared += 1
        # ★ 每塊陸地 4 條邊；每條共用邊讓兩塊各少 1
        return 4 * land - 2 * shared'''

_p463 = S.load("p463")
for _ in range(2000):
    m, n = random.randrange(1, 6), random.randrange(1, 6)
    g = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    want = 0
    for i in range(m):
        for j in range(n):
            if g[i][j]:
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if not (0 <= x < m and 0 <= y < n) or not g[x][y]:
                        want += 1
    assert _p463.islandPerimeter(g) == want
print("P463 OK")

emit({
 "num": 463, "slug": "island-perimeter",
 "en": [
   "You are given <code>row x col</code> <code>grid</code> representing a map where <code>grid[i][j] = 1</code> represents land and <code>grid[i][j] = 0</code> represents water.",
   "Grid cells are connected <strong>horizontally/vertically</strong> (not diagonally). The <code>grid</code> is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).",
   "The island doesn't have \"lakes\", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.",
 ],
 "zh": [
   "給你一張地圖 <code>grid</code>，1 是陸地、0 是水。格子只以上下左右相連。地圖外圍都是水，而且恰好有一座島（沒有湖）。",
   "每格邊長 1，回傳島的<strong>周長</strong>。",
 ],
 "examples": """範例 1
  輸入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
  輸出：16

範例 2
  輸入：grid = [[1]]
  輸出：4""",
 "constraints": [
   "1 ≤ <code>row, col</code> ≤ 100",
   "<code>grid[i][j]</code> 是 0 或 1",
   "恰好有一座島",
 ],
 "idea": [
   ("c", """【每塊陸地貢獻 4 條邊】
    但兩塊相鄰的陸地之間那條邊不在周長上 ——
    它被兩塊陸地各算了一次，所以要扣 2。

    周長 = 4 × 陸地數 - 2 × 相鄰的陸地對數

【數相鄰對：只看上和左】
    每一對相鄰只會被數一次（在右邊或下邊那一格數到它）。

【另一種寫法】
    對每塊陸地，數它四個方向中「是水或出界」的邊。"""),
 ],
 "approaches": [
   ap("解法", "計數：4 × 陸地 − 2 × 共用邊", [
     ("c", S["p463"]),
   ], "O(mn)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>單一格子</strong> → 4。",
   "<strong>一排陸地</strong> → 2 × 長度 + 2。",
   "<strong>貼著地圖邊界</strong> → 出界也算周長。",
 ],
 "follow": [
   ("h", "如果有湖？"),
   ("c", "湖的內側邊也算周長的話，公式照樣成立（湖邊也是「陸地旁邊是水」）。題目說沒有湖，是為了定義清楚。"),
 ],
 "related": [
   "<strong>第 200 題 島嶼數量</strong>",
   "<strong>第 695 題 島嶼的最大面積</strong>",
   "<strong>第 827 題 最大人工島</strong>",
 ],
 "check": [
   "為什麼每一條共用邊要扣 2？",
   "為什麼只需要檢查上和左兩個方向？",
 ],
})


# ==================== 464. Can I Win ====================
S["p464"] = '''class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        n = maxChoosableInteger
        if desiredTotal <= 0:
            return True
        if n * (n + 1) // 2 < desiredTotal:      # 全部加起來都不夠：沒有人能贏
            return False

        @functools.lru_cache(None)
        def win(used: int, remain: int) -> bool:
            # used：已經用過的數（位元遮罩）；remain：還差多少。輪到「目前的玩家」
            for x in range(1, n + 1):
                if used >> x & 1:
                    continue
                # ★ 選 x 直接達標，或選 x 之後對手必輸 -> 我必勝
                if x >= remain or not win(used | 1 << x, remain - x):
                    return True
            return False

        return win(0, desiredTotal)'''

_p464 = S.load("p464")


def _ciw_ref(n, t):
    if t <= 0:
        return True
    if n * (n + 1) // 2 < t:
        return False

    def win(avail, remain):
        for x in avail:
            if x >= remain:
                return True
            if not win(avail - {x}, remain - x):
                return True
        return False
    return win(frozenset(range(1, n + 1)), t)


for n, t, want in [(10, 11, False), (10, 0, True), (10, 1, True), (4, 6, True)]:
    assert _p464.canIWin(n, t) == want
for n in range(1, 8):
    for t in range(0, 30):
        assert _p464.canIWin(n, t) == _ciw_ref(n, t), (n, t)
print("P464 OK")

emit({
 "num": 464, "slug": "can-i-win",
 "en": [
   "In the \"100 game\" two players take turns adding, to a running total, any integer from <code>1</code> to <code>10</code>. The player who first causes the running total to <strong>reach or exceed</strong> 100 wins.",
   "What if we change the game so that players <strong>cannot</strong> re-use integers?",
   "For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total &gt;= 100.",
   "Given two integers <code>maxChoosableInteger</code> and <code>desiredTotal</code>, return <code>true</code> if the first player to move can force a win, otherwise, return <code>false</code>. Assume both players play <strong>optimally</strong>.",
 ],
 "zh": [
   "兩個玩家輪流從 <code>1</code> 到 <code>maxChoosableInteger</code> 中挑一個數加到累計總和上，<strong>每個數只能用一次</strong>。先讓總和<strong>達到或超過</strong> <code>desiredTotal</code> 的人獲勝。",
   "假設雙方都採取最佳策略，判斷先手能不能必勝。",
 ],
 "examples": """範例 1
  輸入：maxChoosableInteger = 10, desiredTotal = 11
  輸出：false
  說明：不管先手選什麼 x，後手選 11 − x 就達標。

範例 2
  輸入：maxChoosableInteger = 10, desiredTotal = 0
  輸出：true

範例 3
  輸入：maxChoosableInteger = 10, desiredTotal = 1
  輸出：true""",
 "constraints": [
   "1 ≤ <code>maxChoosableInteger</code> ≤ 20",
   "0 ≤ <code>desiredTotal</code> ≤ 300",
 ],
 "idea": [
   ("c", """【博弈 DP：必勝態 / 必敗態】
    狀態 = 已經用過哪些數（位元遮罩）。
    （剩下多少目標可以由 used 算出，放進參數只是方便。）

    目前的玩家必勝 <=> 存在某個還沒用的 x：
        x >= 剩餘目標（直接贏），或
        選了 x 之後，對手處於必敗態

【狀態數】
    2²⁰ ≈ 10⁶ 種 used，每個狀態試 20 個數 -> 2×10⁷ 次，記憶化後可以接受。

【特判】
    desiredTotal <= 0 -> 先手直接贏
    1 + 2 + ... + n < desiredTotal -> 沒有人能贏，先手不會贏 -> false
    （沒有這個特判，遞迴會把所有數用完都達不到，回傳 false 也對，
      但要走完整個狀態空間，很慢。）"""),
 ],
 "approaches": [
   ap("解法", "位元遮罩 + 記憶化搜尋", [
     ("c", S["p464"]),
     "驗證方式：和「用集合表示剩餘數字、不記憶化」的直接遞迴，對 n ≤ 7、目標 0–29 全部比對。",
   ], "O(2ⁿ · n)", "O(2ⁿ)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>desiredTotal = 0</strong> → true。",
   "<strong>總和不夠</strong> → false。",
   "<strong>最大數 ≥ 目標</strong> → 先手直接選它就贏。",
 ],
 "follow": [
   ("h", "位元遮罩 DP"),
   ("c", "「從 n ≤ 20 個東西中挑子集」的狀態都可以用一個整數表示。第 698 題（劃分為 k 個相等的子集）、第 847 題（訪問所有節點的最短路徑）、第 1349 題（考試的最大學生數）。"),
 ],
 "related": [
   "<strong>第 292 題 Nim 遊戲</strong>",
   "<strong>第 486 題 預測贏家</strong>",
   "<strong>第 375 題 猜數字大小 II</strong>",
 ],
 "check": [
   "狀態是什麼？為什麼用位元遮罩？",
   "什麼時候目前的玩家必勝？",
   "為什麼要先檢查總和夠不夠？",
 ],
})
