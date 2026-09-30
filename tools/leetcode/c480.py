# -*- coding: utf-8 -*-
"""第 480、481、482、483、485、486 題。"""
import random
import functools
import statistics
from collections import defaultdict
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(480)


# ==================== 480. Sliding Window Median ====================
S["p480"] = '''class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        lo, hi = [], []                 # lo：最大堆積（存負數），hi：最小堆積
        delayed = collections.Counter() # ★ 延遲刪除：等它跑到堆頂才真正丟掉
        lo_size = hi_size = 0           # 兩邊「有效」元素的個數

        def prune(heap, sign):
            while heap and delayed[sign * heap[0]]:
                delayed[sign * heap[0]] -= 1
                heapq.heappop(heap)

        def rebalance():
            nonlocal lo_size, hi_size
            if lo_size > hi_size + 1:                  # lo 多太多：搬一個到 hi
                heapq.heappush(hi, -heapq.heappop(lo))
                lo_size -= 1; hi_size += 1
                prune(lo, -1)
            elif lo_size < hi_size:                    # hi 比較多：搬一個到 lo
                heapq.heappush(lo, -heapq.heappop(hi))
                lo_size += 1; hi_size -= 1
                prune(hi, 1)

        def add(x):
            nonlocal lo_size, hi_size
            if not lo or x <= -lo[0]:
                heapq.heappush(lo, -x); lo_size += 1
            else:
                heapq.heappush(hi, x); hi_size += 1
            rebalance()

        def remove(x):
            nonlocal lo_size, hi_size
            delayed[x] += 1
            if x <= -lo[0]:                            # x 屬於 lo 那一半
                lo_size -= 1
                if x == -lo[0]:
                    prune(lo, -1)
            else:
                hi_size -= 1
                if hi and x == hi[0]:
                    prune(hi, 1)
            rebalance()

        def median():
            return float(-lo[0]) if k % 2 else (-lo[0] + hi[0]) / 2

        res = []
        for i, x in enumerate(nums):
            add(x)
            if i >= k:
                remove(nums[i - k])
            if i >= k - 1:
                res.append(median())
        return res'''

S["p480_sorted"] = '''class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])               # 視窗保持排序
        res = []
        for i in range(k, len(nums) + 1):
            m = window[k // 2]
            res.append(float(m) if k % 2 else (window[k // 2 - 1] + m) / 2)
            if i == len(nums):
                break
            window.pop(bisect.bisect_left(window, nums[i - k]))   # 移除離開的
            bisect.insort(window, nums[i])                          # 加入新的
        return res'''

_p480 = [S.load(x) for x in ("p480", "p480_sorted")]
for nums, k, want in [([1, 3, -1, -3, 5, 3, 6, 7], 3, [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]), ([1, 2, 3, 4, 2, 3, 1, 4, 2], 3, [2, 3, 3, 3, 2, 3, 2])]:
    for sol in _p480:
        assert sol.medianSlidingWindow(nums, k) == want
for _ in range(2000):
    nums = [random.randint(-5, 5) for _ in range(random.randrange(1, 14))]
    k = random.randint(1, len(nums))
    want = [float(statistics.median(nums[i:i + k])) for i in range(len(nums) - k + 1)]
    for sol in _p480:
        assert sol.medianSlidingWindow(nums, k) == want, (nums, k, sol)
print("P480 OK")

emit({
 "num": 480, "slug": "sliding-window-median",
 "en": [
   "The <strong>median</strong> is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.",
   "You are given an integer array <code>nums</code> and an integer <code>k</code>. There is a sliding window of size <code>k</code> which is moving from the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.",
   "Return <em>the median array for each window in the original array</em>. Answers within <code>10<sup>-5</sup></code> of the actual value will be accepted.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code> 和整數 <code>k</code>，大小為 <code>k</code> 的滑動視窗從左移到右，每次移一格。",
   "回傳每個視窗的<strong>中位數</strong>（個數為偶數時取中間兩個的平均）。",
 ],
 "examples": """範例 1
  輸入：nums = [1,3,-1,-3,5,3,6,7], k = 3
  輸出：[1.0,-1.0,-1.0,3.0,5.0,6.0]

範例 2
  輸入：nums = [1,2,3,4,2,3,1,4,2], k = 3
  輸出：[2.0,3.0,3.0,3.0,2.0,3.0,2.0]""",
 "constraints": [
   "1 ≤ <code>k ≤ nums.length</code> ≤ 10⁵",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【第 295 題（資料流中位數）+ 刪除】
    兩個堆積：lo 存較小的一半（最大堆積）、hi 存較大的一半（最小堆積）。
    但視窗滑動時要「刪除」離開的元素 —— 堆積不支援刪除任意元素。

【延遲刪除】
    要刪的元素先記在 delayed 裡，不真的刪；
    等它跑到堆頂時，才把它彈出丟掉。
    另外用 lo_size、hi_size 記錄「有效」元素的個數，
    平衡時看的是有效個數，而不是堆積的實際長度。

【每次操作】
    加入：放進對應的一半，再平衡
    刪除：記進 delayed、有效個數 -1，如果它剛好在堆頂就清理，再平衡
    平衡後要清理堆頂（搬過去的可能露出被延遲刪除的元素）

【更簡單的做法：排序陣列】
    視窗保持排序，bisect 找位置插入、刪除，O(k) 搬移。
    n = 10⁵、k 很大時較慢，但 Python 的 list 搬移很快，實務上常常夠用。"""),
 ],
 "approaches": [
   ap("解法一", "排序視窗 + bisect", [
     ("c", S["p480_sorted"]),
   ], "O(n · k)", "O(k)", "list 插入刪除的搬移", ""),

   ap("解法二", "雙堆積 + 延遲刪除", [
     ("c", S["p480"]),
     "驗證方式：和 <code>statistics.median</code> 對每個視窗直接計算的結果比對兩千組。",
   ], "O(n log n)", "O(n)", "", "延遲刪除的元素可能暫時留在堆積中", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、排序視窗", "O(n·k)", "程式短"],
    ["二、雙堆積 + 延遲刪除", "O(n log n)", "最快 ✔"],
    ["有序集合（SortedList）", "O(n log k)", "需要第三方套件"]]),
 "edges": [
   "<strong>k = 1</strong> → 每個元素自己就是中位數。",
   "<strong>重複值</strong> → delayed 用計數，不能用集合。",
   "<strong>大數相加</strong>（兩個 2³¹−1 取平均）→ Python 沒有溢位；其他語言要先轉 double 或 long。",
 ],
 "follow": [
   ("h", "延遲刪除"),
   ("c", "堆積刪除任意元素很貴，但「等它浮到頂端再處理」幾乎沒有額外成本。第 218 題（天際線）、第 239 題（滑動視窗最大值的堆積解）都用到。"),
 ],
 "related": [
   "<strong>第 295 題 資料流的中位數</strong>",
   "<strong>第 239 題 滑動視窗最大值</strong>",
   "<strong>第 218 題 天際線問題</strong> —— 延遲刪除",
 ],
 "check": [
   "為什麼需要延遲刪除？",
   "平衡時為什麼要看「有效元素個數」而不是堆積長度？",
   "什麼時候要清理堆頂？",
 ],
})


# ==================== 481. Magical String ====================
S["p481"] = '''class Solution:
    def magicalString(self, n: int) -> int:
        s = [1, 2, 2]
        i = 2                              # ★ s[i] 告訴我們「下一組」要放幾個
        while len(s) < n:
            nxt = 3 - s[-1]                # 下一組的數字：1 和 2 交替
            s.extend([nxt] * s[i])
            i += 1
        return s[:n].count(1)'''

_p481 = S.load("p481")
_ms = "1221121221221121122"
for n in range(1, len(_ms) + 1):
    assert _p481.magicalString(n) == _ms[:n].count("1")
# 自我描述性質：前 10⁴ 個字元的連續段長度，就是字串本身
s = [1, 2, 2]
i = 2
while len(s) < 20000:
    s.extend([3 - s[-1]] * s[i]); i += 1
runs = []
j = 0
while j < 10000:
    k = j
    while k < len(s) and s[k] == s[j]:
        k += 1
    runs.append(k - j)
    j = k
assert runs[:3000] == s[:3000]
print("P481 OK")

emit({
 "num": 481, "slug": "magical-string",
 "en": [
   "A magical string <code>s</code> consists of only <code>'1'</code> and <code>'2'</code> and obeys the following rules:",
   ("ul", ["The string s is magical because concatenating the number of contiguous occurrences of characters <code>'1'</code> and <code>'2'</code> generates the string <code>s</code> itself."]),
   "The first few elements of <code>s</code> is <code>s = \"1221121221221121122……\"</code>. If we group the consecutive <code>1</code>'s and <code>2</code>'s in <code>s</code>, it will be <code>\"1 22 11 2 1 22 1 22 11 2 11 22 ......\"</code> and the occurrences of <code>1</code>'s or <code>2</code>'s in each group are <code>\"1 2 2 1 1 2 1 2 2 1 2 2 ......\"</code>. You can see that the occurrence sequence is <code>s</code> itself.",
   "Given an integer <code>n</code>, return the number of <code>1</code>'s in the first <code>n</code> number in the magical string <code>s</code>.",
 ],
 "zh": [
   "<strong>神奇字串</strong> <code>s</code> 只由 1 和 2 組成，而且「把連續相同的字元分組，每組的長度依序排出來」剛好就是 <code>s</code> 本身。",
   "<code>s = \"1221121221221121122……\"</code>，分組是 <code>1 22 11 2 1 22 1 22 11 2 11 22……</code>，各組長度 <code>1 2 2 1 1 2 1 2 2 1 2 2……</code> 正是 <code>s</code>。",
   "回傳 <code>s</code> 前 <code>n</code> 個字元中有幾個 1。",
 ],
 "examples": """範例 1
  輸入：n = 6
  輸出：3
  說明：前 6 個是 "122112"，有 3 個 1。

範例 2
  輸入：n = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【字串自己描述自己 -> 一邊讀一邊產生】
    s[i] 告訴我們「第 i 組」有幾個字元；
    組與組之間 1、2 交替。

    從 s = [1, 2, 2] 開始，i = 2（第 2 組還沒生成）：
        s[2] = 2 -> 下一組是兩個「1」（和上一個 2 相反）-> [1,2,2,1,1]
        s[3] = 1 -> 下一組是一個「2」                     -> [1,2,2,1,1,2]
        s[4] = 1 -> 下一組是一個「1」                     -> ...

【為什麼讀取指標不會追上寫入？】
    每一組至少 1 個字元，寫入的速度 >= 讀取的速度。"""),
 ],
 "approaches": [
   ap("解法", "雙指標：讀取組長、寫入新組", [
     ("c", S["p481"]),
     "驗證方式：產生前兩萬個字元，確認它的「連續段長度序列」就是它自己。",
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>n ≤ 3</strong> → 直接從前三個字元算。",
   "<strong>產生的長度可能超過 n</strong> → 最後只取前 n 個。",
 ],
 "follow": [
   ("h", "Kolakoski 數列"),
   ("c", "這個數列叫 Kolakoski 數列（1965）。一個未解的數學問題：1 的比例是否趨近 1/2？目前數值上看起來是，但還沒有證明。"),
 ],
 "related": [
   "<strong>第 38 題 外觀數列</strong> —— 另一個「描述自己」的數列",
 ],
 "check": [
   "產生字串時，s[i] 代表什麼？",
   "下一組的數字怎麼決定？",
 ],
})


# ==================== 482. License Key Formatting ====================
S["p482"] = '''class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace("-", "").upper()
        first = len(chars) % k or k                # ★ 第一組可以比較短，其餘都剛好 k 個
        groups = [chars[:first]] + [chars[i:i + k] for i in range(first, len(chars), k)]
        return "-".join(g for g in groups if g)'''

_p482 = S.load("p482")
for s, k, want in [("5F3Z-2e-9-w", 4, "5F3Z-2E9W"), ("2-5g-3-J", 2, "2-5G-3J"), ("---", 3, ""), ("a", 2, "A")]:
    assert _p482.licenseKeyFormatting(s, k) == want
for _ in range(3000):
    s = "".join(random.choice("ab1C--") for _ in range(random.randrange(1, 15)))
    k = random.randint(1, 5)
    c = s.replace("-", "").upper()
    rev = c[::-1]
    want = "-".join(rev[i:i + k] for i in range(0, len(rev), k))[::-1]
    assert _p482.licenseKeyFormatting(s, k) == want
print("P482 OK")

emit({
 "num": 482, "slug": "license-key-formatting",
 "en": [
   "You are given a license key represented as a string <code>s</code> that consists of only alphanumeric characters and dashes. The string is separated into <code>n + 1</code> groups by <code>n</code> dashes. You are also given an integer <code>k</code>.",
   "We want to reformat the string <code>s</code> such that each group contains exactly <code>k</code> characters, except for the first group, which could be shorter than <code>k</code> but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.",
   "Return <em>the reformatted license key</em>.",
 ],
 "zh": [
   "給你一個授權碼字串 <code>s</code>（英數字和破折號）以及整數 <code>k</code>。",
   "重新格式化：每組恰好 <code>k</code> 個字元（第一組可以比較短，但至少一個），組與組之間用破折號分隔，小寫字母轉成大寫。回傳結果。",
 ],
 "examples": """範例 1
  輸入：s = "5F3Z-2e-9-w", k = 4
  輸出："5F3Z-2E9W"

範例 2
  輸入：s = "2-5g-3-J", k = 2
  輸出："2-5G-3J\"""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁵",
   "1 ≤ <code>k</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【先去掉所有破折號、轉大寫】
    剩下 L 個字元。

【分組是從「右邊」數的】
    除了第一組，每組都是 k 個 ->
    第一組的長度 = L % k（如果剛好整除，第一組就是 k 個）。
    之後每 k 個一組。

【另一種寫法】
    反轉字串，每 k 個一組，再反轉回來。

【邊界】
    全部都是破折號 -> 空字串。"""),
 ],
 "approaches": [
   ap("解法", "先算第一組長度，再每 k 個一組", [
     ("c", S["p482"]),
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>只有破折號</strong> → 空字串。",
   "<strong>L 剛好是 k 的倍數</strong> → 第一組也是 k 個。",
   "<strong>小寫字母</strong> → 轉大寫。",
 ],
 "follow": [
   ("h", "從右邊分組"),
   ("c", "千分位逗號（1,234,567）也是從右邊每 3 位一組，同樣的技巧。"),
 ],
 "related": [
   "<strong>第 1556 題 千位分隔數</strong>",
 ],
 "check": [
   "第一組的長度怎麼算？",
   "為什麼 L % k == 0 時第一組是 k 個？",
 ],
})


# ==================== 483. Smallest Good Base ====================
S["p483"] = '''class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        # ★ 位數 m 越多，進位制 k 越小 -> 從最多的位數開始試
        for m in range(num.bit_length(), 1, -1):          # m 個 1：1 + k + k² + ... + k^(m-1)
            k = int(num ** (1 / (m - 1)))                  # k 的候選（k^(m-1) < num < (k+1)^(m-1)）
            for cand in (k, k + 1):                        # 浮點誤差：試 k 和 k+1
                if cand < 2:
                    continue
                total, p = 0, 1
                for _ in range(m):
                    total += p
                    p *= cand
                if total == num:
                    return str(cand)
        return str(num - 1)                                # 兩位 "11"：k = num - 1 一定成立'''


def _good_ref(num):
    for k in range(2, num):
        x = num
        while x % k == 1:
            x //= k
        if x == 0:
            return str(k)
    return str(num - 1)


_p483 = S.load("p483")
for n, want in [("13", "3"), ("4681", "8"), ("1000000000000000000", "999999999999999999"), ("3", "2")]:
    assert _p483.smallestGoodBase(n) == want
for num in range(3, 3000):
    assert _p483.smallestGoodBase(str(num)) == _good_ref(num), num
for _ in range(300):                       # 刻意構造「全 1」的大數
    k, m = random.randint(2, 1000), random.randint(2, 6)
    num = sum(k ** i for i in range(m))
    if num <= 10 ** 18:
        assert int(_p483.smallestGoodBase(str(num))) <= k
print("P483 OK")

emit({
 "num": 483, "slug": "smallest-good-base",
 "en": [
   "Given an integer <code>n</code> represented as a string, return <em>the smallest <strong>good base</strong> of</em> <code>n</code>.",
   "We call <code>k &gt;= 2</code> a <strong>good base</strong> of <code>n</code>, if all digits of <code>n</code> base <code>k</code> are <code>1</code>'s.",
 ],
 "zh": [
   "給你一個以字串表示的整數 <code>n</code>，回傳它的<strong>最小好進位</strong>。",
   "如果 <code>n</code> 在 <code>k</code> 進位（<code>k ≥ 2</code>）下每一位都是 1，就說 <code>k</code> 是 <code>n</code> 的<strong>好進位</strong>。",
 ],
 "examples": """範例 1
  輸入：n = "13"
  輸出："3"
  說明：13 在 3 進位是 111。

範例 2
  輸入：n = "4681"
  輸出："8"
  說明：4681 在 8 進位是 11111。

範例 3
  輸入：n = "1000000000000000000"
  輸出："999999999999999999"
  說明：在 999999999999999999 進位是 11。""",
 "constraints": [
   "<code>n</code> 是 [3, 10¹⁸] 之間的整數",
   "沒有前導零",
 ],
 "idea": [
   ("c", """【n = 1 + k + k² + ... + k^(m-1)】（m 個 1）

【進位越小，位數越多】
    k = 2 時位數最多：m 最多約 log₂ n ≈ 60。
    從最大的 m 往下試，第一個找得到整數 k 的就是最小的 k。

【給定 m，k 是多少？】
    k^(m-1) < n < (k+1)^(m-1)（二項式展開可以證明）
    -> k = ⌊n^(1/(m-1))⌋
    只要驗證這個 k 的 1 + k + ... + k^(m-1) 是否剛好等於 n。
    （浮點數可能差 1，保險起見也試 k + 1；或對 k 二分搜尋。）

【一定有解】
    m = 2："11" = 1 + k -> k = n - 1 永遠成立。"""),
 ],
 "approaches": [
   ap("解法", "枚舉位數 m，直接算出 k", [
     ("c", S["p483"]),
     "驗證方式：3 到 3000 全部和「逐一試 k」的暴力法比對；再刻意構造「全 1」的大數。",
   ], "O(log² n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>n = 3</strong> → 2（3 = 11₂）。",
   "<strong>只有兩位的解</strong> → n − 1。",
   "<strong>浮點誤差</strong> → n 接近 10¹⁸ 時 n^(1/(m−1)) 可能差 1，要驗證相鄰值。",
 ],
 "follow": [
   ("h", "枚舉比較小的那個維度"),
   ("c", "k 的範圍到 10¹⁸，m 的範圍只有 60 —— 枚舉小的那一個，再用數學或二分求另一個。"),
 ],
 "related": [
   "<strong>第 69 題 x 的平方根</strong>",
   "<strong>第 50 題 Pow(x, n)</strong>",
 ],
 "check": [
   "為什麼要從最多的位數開始試？",
   "給定位數 m，k 大約是多少？為什麼？",
   "為什麼一定有解？",
 ],
})


# ==================== 485. Max Consecutive Ones ====================
S["p485"] = '''class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = cur = 0
        for x in nums:
            cur = cur + 1 if x == 1 else 0     # ★ 遇到 0 就歸零
            best = max(best, cur)
        return best'''

_p485 = S.load("p485")
for _ in range(3000):
    a = [random.randint(0, 1) for _ in range(random.randrange(1, 15))]
    want = max(len(s) for s in "".join(map(str, a)).split("0"))
    assert _p485.findMaxConsecutiveOnes(a) == want
print("P485 OK")

emit({
 "num": 485, "slug": "max-consecutive-ones",
 "en": [
   "Given a binary array <code>nums</code>, return <em>the maximum number of consecutive</em> <code>1</code><em>'s in the array</em>.",
 ],
 "zh": [
   "給你一個二進位陣列 <code>nums</code>，回傳其中連續 1 的最大個數。",
 ],
 "examples": """範例 1
  輸入：nums = [1,1,0,1,1,1]
  輸出：3

範例 2
  輸入：nums = [1,0,1,1,0,1]
  輸出：2""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "<code>nums[i]</code> 是 0 或 1",
 ],
 "idea": [
   ("c", """【一趟掃描】
    cur = 目前這一段連續 1 的長度
    遇到 1：cur + 1
    遇到 0：cur 歸零
    隨時更新最大值。"""),
 ],
 "approaches": [
   ap("解法", "一趟計數", [
     ("c", S["p485"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>全部是 0</strong> → 0。",
   "<strong>全部是 1</strong> → n。",
 ],
 "follow": [
   ("h", "進階版本"),
   ("c", "第 487 題（付費，最多翻轉一個 0）、第 1004 題（最多翻轉 k 個 0）：都變成「視窗內 0 的個數 ≤ k」的滑動視窗。"),
 ],
 "related": [
   "<strong>第 1004 題 最大連續 1 的個數 III</strong>",
   "<strong>第 487 題 最大連續 1 的個數 II</strong>（付費）",
 ],
 "check": [
   "cur 在什麼時候歸零？",
 ],
})


# ==================== 486. Predict the Winner ====================
S["p486"] = '''class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # dp[i][j]：只剩 nums[i..j] 時，「目前輪到的玩家」最多能比對手多拿多少分
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # ★ 拿左邊：得 nums[i]，接下來對手在 [i+1, j] 領先 dp[i+1][j]
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        return dp[0][n - 1] >= 0               # 平手也算玩家 1 贏'''

_p486 = S.load("p486")


def _pw_ref(a):
    @functools.lru_cache(None)
    def best(i, j, turn):          # 回傳 (玩家1總分, 玩家2總分)，目前輪到 turn
        if i > j:
            return (0, 0)
        opts = []
        for take, ni, nj in ((a[i], i + 1, j), (a[j], i, j - 1)):
            p1, p2 = best(ni, nj, 1 - turn)
            opts.append((p1 + take, p2) if turn == 0 else (p1, p2 + take))
        return max(opts, key=lambda t: t[0] - t[1]) if turn == 0 else max(opts, key=lambda t: t[1] - t[0])
    p1, p2 = best(0, len(a) - 1, 0)
    return p1 >= p2


for nums, want in [([1, 5, 2], False), ([1, 5, 233, 7], True)]:
    assert _p486.predictTheWinner(nums) == want
for _ in range(2000):
    a = tuple(random.randint(0, 9) for _ in range(random.randrange(1, 9)))
    assert _p486.predictTheWinner(list(a)) == _pw_ref(a), a
print("P486 OK")

emit({
 "num": 486, "slug": "predict-the-winner",
 "en": [
   "You are given an integer array <code>nums</code>. Two players are playing a game with this array: player 1 and player 2.",
   "Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of <code>0</code>. At each turn, the player takes one of the numbers from either end of the array (i.e., <code>nums[0]</code> or <code>nums[nums.length - 1]</code>) which reduces the size of the array by <code>1</code>. The player adds the chosen number to their score. The game ends when there are no more elements in the array.",
   "Return <code>true</code> if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return <code>true</code>. You may assume that both players are playing optimally.",
 ],
 "zh": [
   "兩個玩家輪流從陣列的<strong>頭或尾</strong>拿一個數加到自己的分數，玩家 1 先手，拿完為止。",
   "雙方都採取最佳策略，判斷玩家 1 能不能贏（<strong>平手也算玩家 1 贏</strong>）。",
 ],
 "examples": """範例 1
  輸入：nums = [1,5,2]
  輸出：false
  說明：玩家 1 拿 1 或 2，玩家 2 都會拿 5。

範例 2
  輸入：nums = [1,5,233,7]
  輸出：true
  說明：玩家 1 先拿 1，不管玩家 2 拿 5 還是 7，玩家 1 都能拿到 233。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 20",
   "0 ≤ <code>nums[i]</code> ≤ 10⁷",
 ],
 "idea": [
   ("c", """【把兩個人的分數合併成一個「差值」】
    dp[i][j] = 只剩 nums[i..j]、輪到某個玩家時，
               他最多能「比對手多」拿多少分。

    輪到我時有兩種選擇：
        拿左邊 nums[i]：接下來對手面對 [i+1, j]，他會領先 dp[i+1][j]
            -> 我的淨領先 = nums[i] - dp[i+1][j]
        拿右邊 nums[j]：淨領先 = nums[j] - dp[i][j-1]
    dp[i][j] = 兩者取大

    這個「用差值、對手的最佳就是我的損失」的寫法叫 negamax，
    不用分別記錄兩個人的分數。

【答案】dp[0][n-1] >= 0

【小知識】
    n 是偶數時，先手一定不會輸（第 877 題）：
    先手可以決定「拿走所有奇數位置」或「所有偶數位置」，挑總和大的那組。"""),
 ],
 "approaches": [
   ap("解法", "區間 DP（差值 / negamax）", [
     ("c", S["p486"]),
     "驗證方式：和「分別記錄兩人分數、窮舉雙方選擇」的 minimax 參考實作比對兩千組。",
   ], "O(n²)", "O(n²)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>只有一個數</strong> → 玩家 1 拿走，true。",
   "<strong>平手</strong> → 算玩家 1 贏。",
   "<strong>偶數長度</strong> → 先手一定不輸。",
 ],
 "follow": [
   ("h", "negamax"),
   ("c", "雙人零和遊戲中，「我的分數 − 對手的分數」可以統一用 max 表示：輪到誰都是最大化自己的領先。第 877、1140、1406 題都用這個技巧。"),
 ],
 "related": [
   "<strong>第 877 題 石子遊戲</strong>",
   "<strong>第 464 題 我能贏嗎</strong>",
   "<strong>第 1690 題 石子遊戲 VII</strong>",
 ],
 "check": [
   "dp[i][j] 為什麼存「差值」而不是分數？",
   "拿左邊時，我的淨領先為什麼是 nums[i] − dp[i+1][j]？",
   "為什麼偶數長度時先手一定不會輸？",
 ],
})
