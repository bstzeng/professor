# -*- coding: utf-8 -*-
"""第 343、344、345、347、349、350 題。"""
import random
from collections import Counter
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(343)


# ==================== 343. Integer Break ====================
S["p343_dp"] = '''class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)                   # dp[i]：把 i 拆成至少兩份的最大乘積
        for i in range(2, n + 1):
            for j in range(1, i):
                # 第一份是 j；剩下的 i-j 可以「不再拆」或「繼續拆」
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]'''

S["p343"] = '''class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1                     # 必須拆成至少兩份：2=1+1、3=1+2
        q, r = divmod(n, 3)
        # ★ 盡量拆成 3；餘 1 時把一個 3 + 1 換成 2 + 2（4 > 3）
        if r == 0:
            return 3 ** q
        if r == 1:
            return 3 ** (q - 1) * 4
        return 3 ** q * 2'''

_p343 = [S.load(x) for x in ("p343_dp", "p343")]
for n in range(2, 59):
    assert _p343[0].integerBreak(n) == _p343[1].integerBreak(n), n
assert _p343[1].integerBreak(10) == 36
print("P343 OK")

emit({
 "num": 343, "slug": "integer-break",
 "en": [
   "Given an integer <code>n</code>, break it into the sum of <code>k</code> <strong>positive integers</strong>, where <code>k &gt;= 2</code>, and maximize the product of those integers.",
   "Return <em>the maximum product you can get</em>.",
 ],
 "zh": [
   "給你一個正整數 <code>n</code>，把它拆成<strong>至少兩個</strong>正整數的和，並使這些整數的乘積最大。",
   "回傳最大乘積。",
 ],
 "examples": """範例 1
  輸入：n = 2
  輸出：1
  說明：2 = 1 + 1，1 × 1 = 1

範例 2
  輸入：n = 10
  輸出：36
  說明：10 = 3 + 3 + 4，3 × 3 × 4 = 36""",
 "constraints": [
   "2 ≤ <code>n</code> ≤ 58",
 ],
 "idea": [
   ("c", """【DP】
    dp[i] = 把 i 拆成至少兩份的最大乘積
    枚舉第一份 j：
        剩下的 i - j 不再拆：j × (i - j)
        剩下的 i - j 繼續拆：j × dp[i - j]
    注意 dp[i - j] 要求「至少兩份」，所以「不拆」要另外考慮。

【數學：盡量拆成 3】
    為什麼是 3？
    - 拆出 1 沒有意義：1 × x < 1 + x（把 1 加到別的份更好）
    - 拆出 >= 5 的數不划算：5 < 2 × 3 = 6，x < 2(x-2) 對 x >= 5 成立
    - 所以每一份只會是 2、3、4；而 4 = 2 + 2，乘積一樣
    - 2 + 2 + 2 = 6：2³ = 8 < 3² = 9 -> 三個 2 不如兩個 3
    結論：盡量用 3，剩下的用 2。

【餘數】
    n % 3 == 0 -> 3^q
    n % 3 == 1 -> 3^(q-1) × 4    （3 + 1 不如 2 + 2）
    n % 3 == 2 -> 3^q × 2

【小心 n = 2、3】
    必須至少拆兩份：2 -> 1×1 = 1，3 -> 1×2 = 2
    （如果可以不拆，3 會比較大，但題目不允許。）"""),
   ("t", ["n", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
    [["最大乘積", "1", "2", "4", "6", "9", "12", "18", "27", "36"],
     ["拆法", "1+1", "1+2", "2+2", "2+3", "3+3", "3+4", "3+3+2", "3+3+3", "3+3+4"]]),
 ],
 "approaches": [
   ap("解法一", "動態規劃", [
     ("c", S["p343_dp"]),
   ], "O(n²)", "O(n)", "", ""),

   ap("解法二", "數學：盡量拆成 3", [
     ("c", S["p343"]),
   ], "O(log n)", "O(1)", "計算次方", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、DP", "O(n²)", "O(n)"],
    ["二、拆成 3", "O(log n)", "O(1) ✔"]]),
 "edges": [
   "<strong>n = 2、3</strong> → 必須拆，答案是 n − 1。",
   "<strong>餘 1</strong> → 用 2 + 2 取代 3 + 1。",
 ],
 "follow": [
   ("h", "為什麼 3 最好？（連續版本）"),
   ("c", "把 n 拆成 n/x 份、每份 x，乘積是 x^(n/x)。取對數 (n/x)·ln x，對 x 微分 = 0 得 x = e ≈ 2.718。最接近 e 的整數是 3。"),
   ("h", "大數版本"),
   ("c", "劍指 Offer 14-II：n 到 1000，答案要 mod 10⁹+7——同樣拆成 3，用快速冪取模。"),
 ],
 "related": [
   "<strong>第 279 題 完全平方數</strong>",
   "<strong>第 1808 題 好因子的最大數目</strong> —— 同樣盡量拆成 3",
 ],
 "check": [
   "為什麼每一份不會是 1 或大於等於 5？",
   "為什麼三個 2 不如兩個 3？",
   "n % 3 == 1 時為什麼要特別處理？",
 ],
})


# ==================== 344. Reverse String ====================
S["p344"] = '''class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1
        while i < j:                         # ★ 頭尾交換，往中間靠
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1'''

S["p344_py"] = '''class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]                       # 切片賦值：原地改內容（s = s[::-1] 只是改變區域變數 ✘）'''

_p344 = [S.load(x) for x in ("p344", "p344_py")]
for _ in range(500):
    a = [random.choice("abcXY") for _ in range(random.randrange(1, 12))]
    for sol in _p344:
        b = list(a)
        sol.reverseString(b)
        assert b == a[::-1]
print("P344 OK")

emit({
 "num": 344, "slug": "reverse-string",
 "en": [
   "Write a function that reverses a string. The input string is given as an array of characters <code>s</code>.",
   "You must do this by modifying the input array <strong>in-place</strong> with <code>O(1)</code> extra memory.",
 ],
 "zh": [
   "寫一個函式把字串反轉。輸入是一個字元陣列 <code>s</code>。",
   "必須<strong>原地</strong>修改輸入陣列，只能用 <code>O(1)</code> 額外空間。",
 ],
 "examples": """範例 1
  輸入：s = ["h","e","l","l","o"]
  輸出：["o","l","l","e","h"]

範例 2
  輸入：s = ["H","a","n","n","a","h"]
  輸出：["h","a","n","n","a","H"]""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁵",
   "<code>s[i]</code> 是可列印的 ASCII 字元",
 ],
 "idea": [
   ("c", """【雙指標】
    i 從頭、j 從尾，交換後各往中間走一步，直到相遇。
    只需要 n/2 次交換。

【Python 的陷阱】
    s = s[::-1]    ✘ 只是讓區域變數 s 指向新串列，原本的串列沒變
    s[:] = s[::-1] ✔ 切片賦值，把原串列的內容換掉
    s.reverse()    ✔ 內建的原地反轉

    （嚴格來說 s[::-1] 會先建立一個 O(n) 的新串列。）"""),
 ],
 "approaches": [
   ap("解法一", "雙指標交換", [
     ("c", S["p344"]),
   ], "O(n)", "O(1)", "", "", optimal=True),

   ap("解法二", "Python 切片賦值", [
     ("c", S["p344_py"]),
   ], "O(n)", "O(n)", "", "暫時的反轉副本"),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、雙指標", "O(n)", "O(1) ✔"],
    ["二、切片", "O(n)", "O(n)"]]),
 "edges": [
   "<strong>長度 1</strong> → 不變。",
   "<strong>奇數長度</strong> → 中間的字元不動。",
 ],
 "follow": [
   ("h", "雙指標的基本型"),
   ("c", "第 345 題（只反轉母音）、第 541 題（每 2k 個反轉前 k 個）、第 151 題（反轉單字順序：先整體反轉，再每個單字反轉）都建立在這個操作上。"),
 ],
 "related": [
   "<strong>第 345 題 反轉字串中的母音</strong>",
   "<strong>第 541 題 反轉字串 II</strong>",
   "<strong>第 151 題 反轉字串中的單字</strong>",
 ],
 "check": [
   "為什麼 <code>s = s[::-1]</code> 不能通過？",
   "雙指標需要交換幾次？",
 ],
})


# ==================== 345. Reverse Vowels of a String ====================
S["p345"] = '''class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)                       # 字串不可變，先轉成串列
        i, j = 0, len(chars) - 1
        while i < j:
            if chars[i] not in vowels:        # 左邊不是母音：往右找
                i += 1
            elif chars[j] not in vowels:      # 右邊不是母音：往左找
                j -= 1
            else:                             # ★ 兩邊都是母音：交換
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return "".join(chars)'''

_p345 = S.load("p345")
for s, want in [("IceCreAm", "AceCreIm"), ("leetcode", "leotcede"), ("hello", "holle"), ("bcd", "bcd")]:
    assert _p345.reverseVowels(s) == want
for _ in range(2000):
    s = "".join(random.choice("aEbcUio x") for _ in range(random.randrange(1, 12)))
    vs = [c for c in s if c in "aeiouAEIOU"][::-1]
    it = iter(vs)
    want = "".join(next(it) if c in "aeiouAEIOU" else c for c in s)
    assert _p345.reverseVowels(s) == want
print("P345 OK")

emit({
 "num": 345, "slug": "reverse-vowels-of-a-string",
 "en": [
   "Given a string <code>s</code>, reverse only all the vowels in the string and return it.",
   "The vowels are <code>'a'</code>, <code>'e'</code>, <code>'i'</code>, <code>'o'</code>, and <code>'u'</code>, and they can appear in both lower and upper cases, more than once.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，只把其中的<strong>母音</strong>反轉，其他字元位置不變，回傳結果。",
   "母音是 <code>a</code>、<code>e</code>、<code>i</code>、<code>o</code>、<code>u</code>，大小寫都算，可能出現多次。",
 ],
 "examples": """範例 1
  輸入：s = "IceCreAm"
  輸出："AceCreIm"
  說明：母音依序是 I, e, e, A，反轉成 A, e, e, I。

範例 2
  輸入：s = "leetcode"
  輸出："leotcede\"""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 3 × 10⁵",
   "<code>s</code> 由可列印的 ASCII 字元組成",
 ],
 "idea": [
   ("c", """【第 344 題的雙指標，加上「跳過非母音」】
    i 往右找下一個母音，j 往左找下一個母音，
    兩個都找到了就交換。

【細節】
    - 大小寫都要算：用集合 "aeiouAEIOU"
    - Python 字串不可變：先轉成 list，最後 join
    - 每次迴圈只移動一個指標（或交換後兩個都移），
      寫成 if / elif / else 最不容易出錯"""),
 ],
 "approaches": [
   ap("解法", "雙指標", [
     ("c", S["p345"]),
   ], "O(n)", "O(n)", "", "字串轉成串列", optimal=True),
 ],
 "edges": [
   "<strong>沒有母音</strong> → 原字串。",
   "<strong>只有一個母音</strong> → 原字串。",
   "<strong>大寫母音</strong> → 也要算。",
 ],
 "follow": [
   ("h", "變化"),
   ("c", "第 917 題「僅僅反轉字母」：跳過非字母的字元，其餘一模一樣。"),
 ],
 "related": [
   "<strong>第 344 題 反轉字串</strong>",
   "<strong>第 917 題 僅僅反轉字母</strong>",
 ],
 "check": [
   "兩個指標什麼時候交換？",
   "為什麼要先把字串轉成串列？",
 ],
})


# ==================== 347. Top K Frequent Elements ====================
S["p347_bucket"] = '''class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        # ★ 桶排序：bucket[f] 放「出現 f 次」的數；頻率最多是 n
        bucket = [[] for _ in range(len(nums) + 1)]
        for x, f in cnt.items():
            bucket[f].append(x)
        res = []
        for f in range(len(nums), 0, -1):        # 從高頻往低頻拿
            res.extend(bucket[f])
            if len(res) >= k:
                return res[:k]
        return res'''

S["p347_heap"] = '''class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        heap = []                                 # 大小為 k 的最小堆積（依頻率）
        for x, f in cnt.items():
            heapq.heappush(heap, (f, x))
            if len(heap) > k:
                heapq.heappop(heap)               # 丟掉目前頻率最低的
        return [x for f, x in heap]'''

S["p347_py"] = '''class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x for x, _ in collections.Counter(nums).most_common(k)]'''

_p347 = [S.load(x) for x in ("p347_bucket", "p347_heap", "p347_py")]
for nums, k, want in [([1, 1, 1, 2, 2, 3], 2, [1, 2]), ([1], 1, [1])]:
    for sol in _p347:
        assert sorted(sol.topKFrequent(nums, k)) == want
for _ in range(2000):
    # 保證答案唯一：頻率互不相同
    vals = random.sample(range(-20, 20), random.randrange(1, 7))
    freqs = random.sample(range(1, 10), len(vals))
    nums = [v for v, f in zip(vals, freqs) for _ in range(f)]
    random.shuffle(nums)
    k = random.randrange(1, len(vals) + 1)
    want = sorted(v for v, f in sorted(zip(vals, freqs), key=lambda t: -t[1])[:k])
    for sol in _p347:
        assert sorted(sol.topKFrequent(nums, k)) == want
print("P347 OK")

emit({
 "num": 347, "slug": "top-k-frequent-elements",
 "en": [
   "Given an integer array <code>nums</code> and an integer <code>k</code>, return <em>the</em> <code>k</code> <em>most frequent elements</em>. You may return the answer in <strong>any order</strong>.",
   "It is <strong>guaranteed</strong> that the answer is <strong>unique</strong>.",
   "<strong>Follow up:</strong> Your algorithm's time complexity must be better than <code>O(n log n)</code>, where n is the array's size.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code> 和整數 <code>k</code>，回傳<strong>出現次數最多的 <code>k</code> 個元素</strong>，順序不限。",
   "保證答案唯一。",
   "<strong>進階：</strong>時間複雜度必須優於 <code>O(n log n)</code>。",
 ],
 "examples": """範例 1
  輸入：nums = [1,1,1,2,2,3], k = 2
  輸出：[1,2]

範例 2
  輸入：nums = [1], k = 1
  輸出：[1]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
   "<code>k</code> 介於 1 和不同元素的個數之間",
   "保證答案唯一",
 ],
 "idea": [
   ("c", """【第一步都一樣：計數】
    Counter(nums) -> {值: 次數}，O(n)。

【第二步：取次數最多的 k 個】
    排序：O(m log m)，m = 不同元素個數
    堆積：大小維持 k 的最小堆積，O(m log k)
    桶排序：次數最多是 n ->
        開 n+1 個桶，bucket[f] 放出現 f 次的值，
        從最大的桶往下拿，拿滿 k 個為止。O(n) ✔

【為什麼桶排序在這裡可行？】
    「次數」的範圍是 1..n，有上界而且不大，
    可以直接當索引。"""),
 ],
 "approaches": [
   ap("解法一", "Counter.most_common", [
     ("c", S["p347_py"]),
     "<code>most_common(k)</code> 內部用 <code>heapq.nlargest</code>，O(m log k)。",
   ], "O(n + m log k)", "O(m)", "", ""),

   ap("解法二", "大小為 k 的最小堆積", [
     ("c", S["p347_heap"]),
   ], "O(n + m log k)", "O(m)", "", ""),

   ap("解法三", "桶排序", [
     ("c", S["p347_bucket"]),
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["排序", "O(n + m log m)", ""],
    ["一、most_common", "O(n + m log k)", "一行"],
    ["二、堆積", "O(n + m log k)", "資料流也適用"],
    ["三、桶排序", "O(n)", "最快 ✔"]]),
 "edges": [
   "<strong>k = 不同元素個數</strong> → 全部回傳。",
   "<strong>所有元素都一樣</strong> → 只有一個。",
   "<strong>負數</strong> → 計數時沒影響。",
 ],
 "follow": [
   ("h", "快速選擇"),
   ("c", "對 (次數, 值) 陣列做第 215 題的快速選擇，平均 O(m)，找出第 k 大的次數當分界線。"),
 ],
 "related": [
   "<strong>第 215 題 陣列中的第 K 個最大元素</strong>",
   "<strong>第 692 題 前 K 個高頻單字</strong> —— 次數相同時依字典序",
   "<strong>第 451 題 根據字元出現頻率排序</strong>",
 ],
 "check": [
   "為什麼可以用桶排序？桶的索引代表什麼？",
   "堆積為什麼要用最小堆積而且大小維持 k？",
 ],
})


# ==================== 349. Intersection of Two Arrays ====================
S["p349"] = '''class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))          # 集合交集'''

S["p349_sort"] = '''class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a, b = sorted(nums1), sorted(nums2)
        i = j = 0
        res = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                i += 1
            elif a[i] > b[j]:
                j += 1
            else:
                if not res or res[-1] != a[i]:        # 去重
                    res.append(a[i])
                i += 1
                j += 1
        return res'''

_p349 = [S.load(x) for x in ("p349", "p349_sort")]
for _ in range(2000):
    a = [random.randrange(0, 8) for _ in range(random.randrange(1, 10))]
    b = [random.randrange(0, 8) for _ in range(random.randrange(1, 10))]
    want = sorted(set(a) & set(b))
    for sol in _p349:
        assert sorted(sol.intersection(a, b)) == want
print("P349 OK")

emit({
 "num": 349, "slug": "intersection-of-two-arrays",
 "en": [
   "Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>. Each element in the result must be <strong>unique</strong> and you may return the result in <strong>any order</strong>.",
 ],
 "zh": [
   "給你兩個整數陣列 <code>nums1</code>、<code>nums2</code>，回傳它們的<strong>交集</strong>。結果中每個元素<strong>只出現一次</strong>，順序不限。",
 ],
 "examples": """範例 1
  輸入：nums1 = [1,2,2,1], nums2 = [2,2]
  輸出：[2]

範例 2
  輸入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
  輸出：[9,4]""",
 "constraints": [
   "1 ≤ <code>nums1.length, nums2.length</code> ≤ 1000",
   "0 ≤ <code>nums1[i], nums2[i]</code> ≤ 1000",
 ],
 "idea": [
   ("c", """【結果要去重 -> 集合】
    set(nums1) & set(nums2)，O(n + m)。

【不用雜湊表：排序 + 雙指標】
    兩個陣列都排序，指標各自從頭走：
        小的那邊前進
        相等 -> 加入答案（和上一個不同才加），兩邊都前進"""),
 ],
 "approaches": [
   ap("解法一", "集合交集", [
     ("c", S["p349"]),
   ], "O(n + m)", "O(n + m)", "", "", optimal=True),

   ap("解法二", "排序 + 雙指標", [
     ("c", S["p349_sort"]),
   ], "O(n log n + m log m)", "O(1)", "", "不計排序與輸出"),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、集合", "O(n + m)", "O(n + m) ✔"],
    ["二、排序 + 雙指標", "O(n log n + m log m)", "O(1)"]]),
 "edges": [
   "<strong>沒有交集</strong> → 空陣列。",
   "<strong>重複元素</strong> → 答案中只出現一次。",
 ],
 "follow": [
   ("h", "保留重複次數？"),
   ("c", "第 350 題：每個元素出現的次數 = 在兩個陣列中次數的最小值。"),
 ],
 "related": [
   "<strong>第 350 題 兩個陣列的交集 II</strong>",
   "<strong>第 1213 題 三個有序陣列的交集</strong>（付費）",
 ],
 "check": [
   "為什麼用集合最方便？",
   "雙指標版本怎麼去重？",
 ],
})


# ==================== 350. Intersection of Two Arrays II ====================
S["p350"] = '''class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1           # 對較短的陣列計數，省空間
        cnt = collections.Counter(nums1)
        res = []
        for x in nums2:
            if cnt[x] > 0:                        # ★ 還有「額度」才加入
                res.append(x)
                cnt[x] -= 1
        return res'''

S["p350_counter"] = '''class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Counter 的 & 是「每個鍵取較小的次數」
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())'''

_p350 = [S.load(x) for x in ("p350", "p350_counter")]
for _ in range(2000):
    a = [random.randrange(0, 6) for _ in range(random.randrange(1, 10))]
    b = [random.randrange(0, 6) for _ in range(random.randrange(1, 10))]
    want = sorted((Counter(a) & Counter(b)).elements())
    for sol in _p350:
        assert sorted(sol.intersect(a, b)) == want
print("P350 OK")

emit({
 "num": 350, "slug": "intersection-of-two-arrays-ii",
 "en": [
   "Given two integer arrays <code>nums1</code> and <code>nums2</code>, return <em>an array of their intersection</em>. Each element in the result must appear as many times as it shows in both arrays and you may return the result in <strong>any order</strong>.",
   "<strong>Follow up:</strong>",
   ("ul", ["What if the given array is already sorted? How would you optimize your algorithm?",
           "What if <code>nums1</code>'s size is small compared to <code>nums2</code>'s size? Which algorithm is better?",
           "What if elements of <code>nums2</code> are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?"]),
 ],
 "zh": [
   "給你兩個整數陣列，回傳它們的交集。每個元素在結果中出現的次數，等於它在<strong>兩個陣列中出現次數的較小值</strong>。順序不限。",
   "<strong>進階：</strong>",
   ("ul", ["如果陣列已經排好序，怎麼優化？",
           "如果 <code>nums1</code> 比 <code>nums2</code> 小很多，哪個方法比較好？",
           "如果 <code>nums2</code> 存在磁碟上、記憶體不夠一次讀進來，怎麼辦？"]),
 ],
 "examples": """範例 1
  輸入：nums1 = [1,2,2,1], nums2 = [2,2]
  輸出：[2,2]

範例 2
  輸入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
  輸出：[4,9]""",
 "constraints": [
   "1 ≤ <code>nums1.length, nums2.length</code> ≤ 1000",
   "0 ≤ <code>nums[i]</code> ≤ 1000",
 ],
 "idea": [
   ("c", """【計數】
    對其中一個陣列計數（每個值的「額度」），
    掃另一個陣列，有額度就加入答案並扣一。

【為什麼對「較短」的陣列計數？】
    雜湊表大小 = 較短陣列的不同元素數 -> 省記憶體。

【進階問題】
    已排序：雙指標，O(1) 額外空間，不需要雜湊表。
    nums1 很小：對 nums1 計數，nums2 用串流的方式掃一遍。
    nums2 在磁碟上：
        - nums1 放得進記憶體 -> 對 nums1 計數，nums2 分塊讀進來處理
        - 都放不進 -> 外部排序兩個檔案，再用雙指標串流合併"""),
 ],
 "approaches": [
   ap("解法一", "Counter 的 &amp;", [
     ("c", S["p350_counter"]),
   ], "O(n + m)", "O(n + m)", "", ""),

   ap("解法二", "計數 + 扣額度", [
     ("c", S["p350"]),
   ], "O(n + m)", "O(min(n, m))", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、Counter &amp;", "O(n + m)", "O(n + m)"],
    ["二、扣額度", "O(n + m)", "O(min(n,m)) ✔"],
    ["排序 + 雙指標", "O(n log n + m log m)", "O(1)"]]),
 "edges": [
   "<strong>沒有交集</strong> → 空陣列。",
   "<strong>重複很多次</strong> → 取兩邊次數的較小值。",
 ],
 "follow": [
   ("h", "Counter 的集合運算"),
   ("c", "<code>c1 &amp; c2</code>：每個鍵取最小值；<code>c1 | c2</code>：取最大值；<code>c1 - c2</code>：相減並丟掉 ≤ 0 的；<code>c1 + c2</code>：相加。"),
 ],
 "related": [
   "<strong>第 349 題 兩個陣列的交集</strong>",
   "<strong>第 1002 題 查找共用字元</strong> —— 多個字串的 Counter 交集",
 ],
 "check": [
   "每個元素在答案中應該出現幾次？",
   "為什麼要對較短的陣列計數？",
   "nums2 放不進記憶體時該怎麼做？",
 ],
})
