# -*- coding: utf-8 -*-
"""第 367、368、371、372、373、374 題。"""
import random
import itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(367)


# ==================== 367. Valid Perfect Square ====================
S["p367_bs"] = '''class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == num:
                return True
            if sq < num:
                lo = mid + 1
            else:
                hi = mid - 1
        return False'''

S["p367_newton"] = '''class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = num
        while x * x > num:
            x = (x + num // x) // 2        # ★ 牛頓法：x 往 √num 快速收斂（從上方逼近）
        return x * x == num'''

S["p367_odd"] = '''class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        odd = 1
        while num > 0:                     # 1 + 3 + 5 + ... + (2k-1) = k²
            num -= odd
            odd += 2
        return num == 0'''

_p367 = [S.load(x) for x in ("p367_bs", "p367_newton", "p367_odd")]
_sq = {i * i for i in range(1, 50000)}
for n in list(range(1, 20000)) + [2 ** 31 - 1, 46340 ** 2, 46341 ** 2 - 1]:
    want = n in _sq
    for sol in _p367[:2]:
        assert sol.isPerfectSquare(n) == want, n
    if n < 20000:
        assert _p367[2].isPerfectSquare(n) == want
print("P367 OK")

emit({
 "num": 367, "slug": "valid-perfect-square",
 "en": [
   "Given a positive integer <code>num</code>, return <code>true</code> <em>if</em> <code>num</code> <em>is a perfect square or</em> <code>false</code> <em>otherwise</em>.",
   "A <strong>perfect square</strong> is an integer that is the square of an integer. In other words, it is the product of some integer with itself.",
   "You must not use any built-in library function, such as <code>sqrt</code>.",
 ],
 "zh": [
   "給你一個正整數 <code>num</code>，判斷它是不是<strong>完全平方數</strong>（某個整數的平方）。",
   "不能使用 <code>sqrt</code> 之類的內建函式。",
 ],
 "examples": """範例 1
  輸入：num = 16
  輸出：true

範例 2
  輸入：num = 14
  輸出：false""",
 "constraints": [
   "1 ≤ <code>num</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【方法一：二分搜尋】
    在 [1, num] 找 x 使 x² == num。
    x² 隨 x 遞增 -> 可以二分。
    （其他語言要注意 mid * mid 溢位，用 long 或比較 mid 和 num / mid。）

【方法二：牛頓法】
    求 f(x) = x² - num 的根：
        x ← x - f(x)/f'(x) = (x + num/x) / 2
    從 x = num 開始，每次迭代正確位數大約翻倍，收斂非常快。
    用整數除法時，x 會從上方單調遞減到 ⌊√num⌋。

【方法三：奇數和】
    1 = 1
    1 + 3 = 4
    1 + 3 + 5 = 9
    前 k 個奇數的和 = k²。
    從 num 依序減掉 1, 3, 5, ...，剛好減到 0 就是完全平方數。
    O(√n)，概念漂亮但比較慢。"""),
 ],
 "approaches": [
   ap("解法一", "奇數和", [
     ("c", S["p367_odd"]),
   ], "O(√n)", "O(1)", "", ""),

   ap("解法二", "二分搜尋", [
     ("c", S["p367_bs"]),
   ], "O(log n)", "O(1)", "", "", optimal=True),

   ap("解法三", "牛頓法", [
     ("c", S["p367_newton"]),
   ], "O(log n)", "O(1)", "實際上收斂得比二分快", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、奇數和", "O(√n)", "數學趣味"],
    ["二、二分", "O(log n)", "最通用 ✔"],
    ["三、牛頓法", "O(log n)", "收斂最快"]]),
 "edges": [
   "<strong>num = 1</strong> → true。",
   "<strong>2³¹ − 1</strong> → false；46340² = 2147395600 是範圍內最大的平方數。",
   "<strong>浮點數 sqrt</strong> → 大數時可能有誤差，而且題目禁止。",
 ],
 "follow": [
   ("h", "整數平方根"),
   ("c", "第 69 題「x 的平方根」回傳 ⌊√x⌋，是同樣的二分或牛頓法。Python 內建的 <code>math.isqrt</code> 就是精確的整數平方根。"),
 ],
 "related": [
   "<strong>第 69 題 x 的平方根</strong>",
   "<strong>第 633 題 平方數之和</strong>",
   "<strong>第 279 題 完全平方數</strong>",
 ],
 "check": [
   "二分搜尋的範圍是什麼？為什麼可以二分？",
   "牛頓法的迭代式是怎麼來的？",
   "為什麼前 k 個奇數的和是 k²？",
 ],
})


# ==================== 368. Largest Divisible Subset ====================
S["p368"] = '''class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n              # dp[i]：以 nums[i] 為「最大元素」的整除子集大小
        prev = [-1] * n           # 用來回溯出子集
        for i in range(n):
            for j in range(i):
                # ★ 排序後，只要 nums[i] 被「目前子集的最大值」nums[j] 整除，
                #    就被子集裡所有數整除（整除有遞移性）
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        i = max(range(n), key=lambda t: dp[t])
        res = []
        while i != -1:
            res.append(nums[i])
            i = prev[i]
        return res[::-1]'''

_p368 = S.load("p368")


def _div_ok(s):
    return all(a % b == 0 or b % a == 0 for a, b in itertools.combinations(s, 2))


for _ in range(1500):
    nums = random.sample(range(1, 40), random.randrange(1, 9))
    got = _p368.largestDivisibleSubset(list(nums))
    assert set(got) <= set(nums) and _div_ok(got)
    best = max(len(c) for r in range(1, len(nums) + 1) for c in itertools.combinations(nums, r) if _div_ok(c))
    assert len(got) == best, (nums, got)
print("P368 OK")

emit({
 "num": 368, "slug": "largest-divisible-subset",
 "en": [
   "Given a set of <strong>distinct</strong> positive integers <code>nums</code>, return the largest subset <code>answer</code> such that every pair <code>(answer[i], answer[j])</code> of elements in this subset satisfies:",
   ("ul", ["<code>answer[i] % answer[j] == 0</code>, or",
           "<code>answer[j] % answer[i] == 0</code>"]),
   "If there are multiple solutions, return any of them.",
 ],
 "zh": [
   "給你一組<strong>互不相同</strong>的正整數 <code>nums</code>，找出最大的子集，使得子集中<strong>任意兩個數</strong>都有整除關係（一個能整除另一個）。",
   "有多個答案時回傳任意一個。",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3]
  輸出：[1,2]
  說明：[1,3] 也可以。

範例 2
  輸入：nums = [1,2,4,8]
  輸出：[1,2,4,8]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 1000",
   "1 ≤ <code>nums[i]</code> ≤ 2 × 10⁹",
   "<code>nums</code> 中的整數互不相同",
 ],
 "idea": [
   ("c", """【排序後，整除子集就是一條「整除鏈」】
    排序後的子集 a₁ < a₂ < ... < aₖ，
    任兩個都有整除關係 <=> a₁ | a₂ | a₃ | ... | aₖ（每個整除下一個）

    為什麼？整除有遞移性：a | b 且 b | c => a | c。
    所以只要相鄰的整除，任兩個都整除。

【這就是最長遞增子序列（第 300 題）的變形】
    「遞增」換成「整除」：
    dp[i] = 以 nums[i] 結尾（最大元素）的最長整除鏈長度
    dp[i] = 1 + max(dp[j])，對所有 j < i 且 nums[i] % nums[j] == 0

【要回傳子集本身】
    多記一個 prev[i]，最後從 dp 最大的位置往回追。"""),
   ("c", """  nums = [1, 2, 3, 4, 6, 8, 12, 24]
  dp   =  1  2  2  3  3  4  4   5
  24 <- 12 <- 4 <- 2 <- 1   （或 24 <- 12 <- 6 <- 2 <- 1）"""),
 ],
 "approaches": [
   ap("解法", "排序 + LIS 式 DP + 回溯", [
     ("c", S["p368"]),
   ], "O(n²)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>只有一個數</strong> → 它本身。",
   "<strong>互質的數</strong> → 答案大小 1（或包含 1 時大小 2）。",
   "<strong>包含 1</strong> → 1 可以放進任何鏈的開頭。",
 ],
 "follow": [
   ("h", "為什麼不能用 O(n log n) 的 LIS？"),
   ("c", "二分 LIS 依賴「結尾越小越好」的全序關係；整除只是偏序（2 和 3 互不整除），無法用 tails 陣列二分。"),
 ],
 "related": [
   "<strong>第 300 題 最長遞增子序列</strong>",
   "<strong>第 1048 題 最長字串鏈</strong> —— 同樣的「鏈」DP",
 ],
 "check": [
   "為什麼排序後只要相鄰元素整除，整個子集就合法？",
   "dp[i] 的定義是什麼？",
   "怎麼把子集本身找出來？",
 ],
})


# ==================== 371. Sum of Two Integers ====================
S["p371"] = '''class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF                     # 模擬 32 位元
        while b & MASK:
            carry = (a & b) << 1              # ★ 兩個都是 1 的位產生進位
            a = a ^ b                         # ★ 不考慮進位的相加
            b = carry
        a &= MASK
        # 32 位元的最高位是 1 -> 負數，轉回 Python 的負整數
        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)'''

_p371 = S.load("p371")
for _ in range(20000):
    a, b = random.randint(-1000, 1000), random.randint(-1000, 1000)
    assert _p371.getSum(a, b) == a + b, (a, b)
for a, b in [(1, 2), (2, 3), (-1, 1), (-1000, -1000), (0, 0), (-1, -1)]:
    assert _p371.getSum(a, b) == a + b
print("P371 OK")

_P371_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">a = 5 (0101)，b = 3 (0011)：XOR 是「不進位的加法」，AND 左移是「進位」</text>
            <g font-family="monospace" font-size="14">
              <text x="40" y="60" fill="var(--text-muted)">第 1 輪</text>
              <text x="140" y="60" fill="var(--text)">a ^ b      = 0110</text>
              <text x="140" y="82" fill="#ff8a65">(a &amp; b)&lt;&lt;1 = 0010</text>
              <text x="40" y="118" fill="var(--text-muted)">第 2 輪</text>
              <text x="140" y="118" fill="var(--text)">a ^ b      = 0100</text>
              <text x="140" y="140" fill="#ff8a65">(a &amp; b)&lt;&lt;1 = 0100</text>
              <text x="40" y="176" fill="var(--text-muted)">第 3 輪</text>
              <text x="140" y="176" fill="var(--text)">a ^ b      = 0000</text>
              <text x="140" y="198" fill="#ff8a65">(a &amp; b)&lt;&lt;1 = 1000</text>
              <text x="40" y="234" fill="var(--text-muted)">第 4 輪</text>
              <text x="140" y="234" fill="var(--gold)">a ^ b      = 1000 = 8</text>
              <text x="140" y="256" fill="var(--text-muted)">進位       = 0000 → 結束</text>
            </g>
            <text x="440" y="100" fill="var(--text)" font-size="12">每一輪：</text>
            <text x="440" y="122" fill="var(--text-muted)" font-size="12">a ← 不進位的和</text>
            <text x="440" y="144" fill="var(--text-muted)" font-size="12">b ← 進位</text>
            <text x="440" y="166" fill="var(--text-muted)" font-size="12">直到沒有進位</text>'''

emit({
 "num": 371, "slug": "sum-of-two-integers",
 "en": [
   "Given two integers <code>a</code> and <code>b</code>, return <em>the sum of the two integers without using the operators</em> <code>+</code> <em>and</em> <code>-</code>.",
 ],
 "zh": [
   "給你兩個整數 <code>a</code> 和 <code>b</code>，<strong>不使用 <code>+</code> 和 <code>-</code> 運算子</strong>，回傳它們的和。",
 ],
 "examples": """範例 1
  輸入：a = 1, b = 2
  輸出：3

範例 2
  輸入：a = 2, b = 3
  輸出：5""",
 "constraints": [
   "−1000 ≤ <code>a, b</code> ≤ 1000",
 ],
 "idea": [
   ("fig", _P371_FIG, "0 0 640 270"),
   ("c", """【二進位加法拆成兩部分】
    每一位：
        0 + 0 = 0
        0 + 1 = 1
        1 + 1 = 0，進位 1
    「不考慮進位的和」= a XOR b
    「進位」           = (a AND b) << 1
    和 = 不進位的和 + 進位 -> 又是一個加法！
    重複直到進位為 0。

【Python 的麻煩：整數沒有位數限制】
    負數在 Python 中是「無限長的 1」，
    負數的進位會一直往左傳，永遠不會變成 0 ✘

    解法：用 MASK = 0xFFFFFFFF 模擬 32 位元：
    - 每次運算都只看低 32 位
    - 最後如果第 31 位是 1（代表負數），
      用 ~(a ^ MASK) 轉回 Python 的負整數
    （C++、Java 的 int 本來就是 32 位元，不需要這些處理。）

【進位最多傳 32 次】
    每一輪進位至少往左移一位，32 輪後一定消失。"""),
 ],
 "approaches": [
   ap("解法", "XOR + AND 進位（32 位元遮罩）", [
     ("c", S["p371"]),
     ("c", """【~(a ^ MASK) 在做什麼？】
    a 是 32 位元的補數表示（0 .. 2³²-1）。
    a ^ MASK：把低 32 位全部反轉
    ~(...)  ：Python 的 ~x = -x - 1，把「無限長」的高位補成 1
    合起來就是把 32 位元的負數，擴展成 Python 的負整數。"""),
   ], "O(1)", "O(1)", "最多 32 輪", "", optimal=True),
 ],
 "edges": [
   "<strong>負數</strong> → Python 需要遮罩處理。",
   "<strong>a + b = 0</strong>（<code>-1, 1</code>）→ 最後結果是 0。",
   "<strong>其中一個是 0</strong> → 第一輪就沒有進位。",
 ],
 "follow": [
   ("h", "硬體裡的加法器"),
   ("c", "CPU 的「全加器」就是這個邏輯：sum = a ⊕ b ⊕ carry_in，carry_out = (a∧b) ∨ (carry_in∧(a⊕b))。把 32 個全加器串起來是「漣波進位加法器」，本解法就是在模擬它。"),
 ],
 "related": [
   "<strong>第 67 題 二進位求和</strong>",
   "<strong>第 29 題 兩數相除</strong> —— 不用乘除",
   "<strong>第 2 題 兩數相加</strong> —— 鏈結串列的進位",
 ],
 "check": [
   "a XOR b 和 (a AND b) &lt;&lt; 1 分別代表什麼？",
   "為什麼 Python 需要 32 位元遮罩？",
   "迴圈最多跑幾次？",
 ],
})


# ==================== 372. Super Pow ====================
S["p372"] = '''class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        res = 1
        for d in b:                           # b 從最高位讀到最低位
            # ★ a^(10x + d) = (a^x)^10 × a^d
            res = pow(res, 10, MOD) * pow(a, d, MOD) % MOD
        return res'''

S["p372_euler"] = '''class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        # 1337 = 7 × 191，φ(1337) = 6 × 190 = 1140
        # 指數可以對 φ(1337) 取模，再加回一個 φ 避免指數變成 0
        e = 0
        for d in b:
            e = (e * 10 + d) % 1140
        return pow(a, e + 1140, 1337)          # + 1140 確保 a 不和 1337 互質時也正確'''

_p372 = [S.load(x) for x in ("p372", "p372_euler")]
for a, b, want in [(2, [3], 8), (2, [1, 0], 1024), (1, [4, 3, 3, 8, 5, 2], 1), (2147483647, [2, 0, 0], 1198)]:
    for sol in _p372:
        assert sol.superPow(a, b) == want
for _ in range(3000):
    a = random.randint(1, 3000)
    b = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(random.randrange(0, 5))]
    e = int("".join(map(str, b)))
    want = pow(a, e, 1337)
    for sol in _p372:
        assert sol.superPow(a, b) == want, (a, b, sol)
print("P372 OK")

emit({
 "num": 372, "slug": "super-pow",
 "en": [
   "Your task is to calculate <code>a<sup>b</sup> mod 1337</code> where <code>a</code> is a positive integer and <code>b</code> is an extremely large positive integer given in the form of an array.",
 ],
 "zh": [
   "計算 <code>a<sup>b</sup> mod 1337</code>，其中 <code>a</code> 是正整數，<code>b</code> 是一個<strong>非常大</strong>的正整數，以陣列的形式給出（每個元素是一位數字）。",
 ],
 "examples": """範例 1
  輸入：a = 2, b = [3]
  輸出：8

範例 2
  輸入：a = 2, b = [1,0]
  輸出：1024

範例 3
  輸入：a = 1, b = [4,3,3,8,5,2]
  輸出：1""",
 "constraints": [
   "1 ≤ <code>a</code> ≤ 2³¹ − 1",
   "1 ≤ <code>b.length</code> ≤ 2000",
   "0 ≤ <code>b[i]</code> ≤ 9",
   "<code>b</code> 沒有前導零",
 ],
 "idea": [
   ("c", """【b 可能有 2000 位數 —— 不能先轉成整數再算】
    （Python 其實可以，但那不是這題想考的。）

【一位一位處理指數】
    假設 b = 10x + d（x 是前面那些位，d 是最後一位）：
        a^b = a^(10x + d) = (a^x)^10 × a^d

    從最高位讀到最低位，維護 res = a^(目前讀到的前綴) mod 1337：
        讀到新的一位 d：
        res ← res^10 × a^d  (mod 1337)

    這就像把十進位字串轉成數字時的 num = num × 10 + d，
    只是「乘 10」變成「10 次方」、「加 d」變成「乘 a^d」。

【每次都取模】
    (x × y) mod m = ((x mod m) × (y mod m)) mod m
    數字永遠不會超過 1337²。

【另一個方法：歐拉定理】
    φ(1337) = 1140，可以把指數 b 對 1140 取模。
    但 a 和 1337 不互質時要小心（加上一個 1140 保險）。"""),
 ],
 "approaches": [
   ap("解法一", "逐位處理指數", [
     ("c", S["p372"]),
     "Python 內建的 <code>pow(x, e, m)</code> 就是快速冪取模，O(log e)。",
   ], "O(len(b))", "O(1)", "每一位做兩次小的快速冪", "", optimal=True),

   ap("解法二", "歐拉定理降冪", [
     ("c", S["p372_euler"]),
     ("c", """【為什麼要 + 1140？】
    1337 = 7 × 191，兩個質因數都只出現一次。
    對每個質因數 p 分開看（指數 k >= 1）：
        p 不整除 a：費馬小定理 a^(p-1) ≡ 1，而 p-1 整除 1140 -> a^k ≡ a^(k+1140)
        p 整除 a  ：兩邊都 ≡ 0 (mod p)
    所以只要指數 >= 1，就可以把指數換成 (b mod 1140) + 1140。
    直接用 b mod 1140 的話，b mod 1140 = 0 且 a 是 7 或 191 的倍數時會算錯（a⁰ = 1）。"""),
   ], "O(len(b))", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、逐位", "O(len(b))", "不需要數論 ✔"],
    ["二、歐拉定理", "O(len(b))", "需要算 φ"]]),
 "edges": [
   "<strong>a 是 1337 的倍數</strong> → 答案 0。",
   "<strong>a 很大</strong> → 先 mod 1337（pow 會自動處理）。",
   "<strong>b 的中間有 0</strong> → a⁰ = 1，照樣成立。",
 ],
 "follow": [
   ("h", "快速冪"),
   ("c", "第 50 題「Pow(x, n)」：把指數拆成二進位，每次平方。本題是把指數拆成十進位，每次 10 次方。"),
 ],
 "related": [
   "<strong>第 50 題 Pow(x, n)</strong>",
   "<strong>第 1922 題 統計好數字的數目</strong> —— 快速冪取模",
 ],
 "check": [
   "a^(10x + d) 怎麼用 a^x 表示？",
   "為什麼每一步都可以取模？",
 ],
})


# ==================== 373. Find K Pairs with Smallest Sums ====================
S["p373"] = '''class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # 把每個 nums1[i] 想成一條有序串列：(i,0), (i,1), (i,2), ...
        # ★ 多路合併：一開始放每條串列的第一個（最多 k 條就夠）
        heap = [(nums1[i] + nums2[0], i, 0) for i in range(min(k, len(nums1)))]
        heapq.heapify(heap)
        res = []
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):              # 同一條串列的下一個
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return res'''

_p373 = S.load("p373")
for _ in range(2000):
    a = sorted(random.randint(-5, 10) for _ in range(random.randrange(1, 7)))
    b = sorted(random.randint(-5, 10) for _ in range(random.randrange(1, 7)))
    k = random.randrange(1, len(a) * len(b) + 1)
    got = _p373.kSmallestPairs(a, b, k)
    allsums = sorted(x + y for x in a for y in b)
    assert len(got) == k and sorted(x + y for x, y in got) == allsums[:k]
    # 每一對都要來自不同的 (i, j)
    from collections import Counter as _C
    assert not (_C(map(tuple, got)) - _C((x, y) for x in a for y in b))
print("P373 OK")

emit({
 "num": 373, "slug": "find-k-pairs-with-smallest-sums",
 "en": [
   "You are given two integer arrays <code>nums1</code> and <code>nums2</code> sorted in <strong>non-decreasing order</strong> and an integer <code>k</code>.",
   "Define a pair <code>(u, v)</code> which consists of one element from the first array and one element from the second array.",
   "Return <em>the</em> <code>k</code> <em>pairs</em> <code>(u<sub>1</sub>, v<sub>1</sub>), (u<sub>2</sub>, v<sub>2</sub>), ..., (u<sub>k</sub>, v<sub>k</sub>)</code> <em>with the smallest sums</em>.",
 ],
 "zh": [
   "給你兩個<strong>非遞減排序</strong>的整數陣列 <code>nums1</code>、<code>nums2</code>，以及整數 <code>k</code>。",
   "一個數對 <code>(u, v)</code> 由第一個陣列的一個元素和第二個陣列的一個元素組成。",
   "回傳和最小的 <code>k</code> 個數對。",
 ],
 "examples": """範例 1
  輸入：nums1 = [1,7,11], nums2 = [2,4,6], k = 3
  輸出：[[1,2],[1,4],[1,6]]

範例 2
  輸入：nums1 = [1,1,2], nums2 = [1,2,3], k = 2
  輸出：[[1,1],[1,1]]""",
 "constraints": [
   "1 ≤ <code>nums1.length, nums2.length</code> ≤ 10⁵",
   "−10⁹ ≤ <code>nums1[i], nums2[i]</code> ≤ 10⁹",
   "兩個陣列都是非遞減排序",
   "1 ≤ <code>k</code> ≤ 10⁴，<code>k ≤ nums1.length × nums2.length</code>",
 ],
 "idea": [
   ("c", """【所有數對排成一張表】
          nums2 ->
    nums1  (0,0) (0,1) (0,2) ...
      |    (1,0) (1,1) (1,2) ...
      v    (2,0) (2,1) ...
    每一列（固定 i）由左到右和遞增；每一欄由上到下也遞增。

【多路合併（第 23 題的套路）】
    把每一列看成一條有序串列。
    堆積裡放每一列「目前最小的那一個」：
        一開始是 (i, 0)，對所有 i
        彈出 (i, j) 後，放入同一列的下一個 (i, j+1)
    彈 k 次就是答案。

【只需要前 k 列】
    第 k 列之後的 (i, 0) 至少比 (0,0)..(k-1,0) 這 k 個都大，
    不可能擠進前 k 名。
    所以堆積大小最多 k -> 每次 O(log k)。

【為什麼不用 visited？】
    有些寫法從 (0,0) 開始，同時往右、往下擴展，需要集合去重。
    「每列一條串列、只往右走」的寫法每個格子只會被放入一次，不需要去重。"""),
 ],
 "approaches": [
   ap("解法", "最小堆積多路合併", [
     ("c", S["p373"]),
   ], "O(k log k)", "O(k)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>重複值</strong> → 不同位置的相同數對要分別算（範例 2）。",
   "<strong>k 大於某一個陣列的長度</strong> → 初始只放 min(k, len(nums1)) 列。",
   "<strong>負數</strong> → 不影響，排序關係照樣成立。",
 ],
 "follow": [
   ("h", "k 很大時"),
   ("c", "對「和」二分搜尋：給定 x，用雙指標 O(m + n) 數出和 ≤ x 的數對有幾個，找到第 k 小的和，再收集答案。和第 378 題（有序矩陣第 K 小）是同一個想法。"),
 ],
 "related": [
   "<strong>第 23 題 合併 K 個排序鏈結串列</strong>",
   "<strong>第 378 題 有序矩陣中第 K 小的元素</strong>",
   "<strong>第 719 題 找出第 K 小的數對距離</strong>",
 ],
 "check": [
   "為什麼可以把數對看成多條有序串列？",
   "為什麼只需要放前 k 列進堆積？",
   "這個寫法為什麼不需要 visited 集合？",
 ],
})


# ==================== 374. Guess Number Higher or Lower ====================
S["p374"] = '''# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while True:
            mid = (lo + hi) // 2
            r = guess(mid)
            if r == 0:
                return mid
            if r < 0:                   # ★ -1 代表「猜的太大」：答案在左邊
                hi = mid - 1
            else:                       # 1 代表「猜的太小」
                lo = mid + 1'''

for n in list(range(1, 80)) + [2 ** 31 - 1]:
    picks = range(1, n + 1) if n < 80 else [1, n, 12345678, 2 ** 30]
    for pick in picks:
        calls = [0]

        def guess(x, pick=pick):
            calls[0] += 1
            return 0 if x == pick else (-1 if x > pick else 1)

        sol = S.load("p374", extra={"guess": guess})
        assert sol.guessNumber(n) == pick and calls[0] <= 32
print("P374 OK")

emit({
 "num": 374, "slug": "guess-number-higher-or-lower",
 "en": [
   "We are playing the Guess Game. The game is as follows: I pick a number from <code>1</code> to <code>n</code>. You have to guess which number I picked. "
   "Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.",
   "You call a pre-defined API <code>int guess(int num)</code>, which returns three possible results:",
   ("ul", ["<code>-1</code>: Your guess is higher than the number I picked (i.e. <code>num &gt; pick</code>).",
           "<code>1</code>: Your guess is lower than the number I picked (i.e. <code>num &lt; pick</code>).",
           "<code>0</code>: your guess is equal to the number I picked (i.e. <code>num == pick</code>)."]),
   "Return <em>the number that I picked</em>.",
 ],
 "zh": [
   "猜數字遊戲：我從 <code>1</code> 到 <code>n</code> 選一個數字，你來猜。每次猜錯，我會告訴你我選的數字比你猜的大還是小。",
   "呼叫 API <code>guess(num)</code>，回傳：",
   ("ul", ["<code>-1</code>：你猜的<strong>太大</strong>了（<code>num &gt; pick</code>）。",
           "<code>1</code>：你猜的<strong>太小</strong>了（<code>num &lt; pick</code>）。",
           "<code>0</code>：猜中了。"]),
   "回傳我選的數字。",
 ],
 "examples": """範例 1
  輸入：n = 10, pick = 6
  輸出：6

範例 2
  輸入：n = 1, pick = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 2³¹ − 1",
   "1 ≤ <code>pick</code> ≤ <code>n</code>",
 ],
 "idea": [
   ("c", """【標準二分搜尋】
    每猜一次，排除一半的範圍。
    最多 ⌈log₂ n⌉ ≤ 31 次。

【唯一的陷阱：回傳值的方向】
    -1 是「你猜的太大」，不是「答案比較小」的意思嗎？
    —— 其實是同一件事，但很容易寫反：
        guess(mid) == -1 -> mid > pick -> hi = mid - 1
        guess(mid) ==  1 -> mid < pick -> lo = mid + 1

【溢位（其他語言）】
    lo + hi 在 n = 2³¹ - 1 時會溢位 -> lo + (hi - lo) / 2。"""),
 ],
 "approaches": [
   ap("解法", "二分搜尋", [
     ("c", S["p374"]),
   ], "O(log n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>n = 1</strong> → 1。",
   "<strong>pick 在兩端</strong> → 二分照樣找到。",
   "<strong>回傳值方向</strong> → −1 代表要往左找。",
 ],
 "follow": [
   ("h", "猜錯要付錢？"),
   ("c", "第 375 題：猜錯 x 要付 x 元，問最壞情況下至少要準備多少錢——這時二分不一定最好，要用區間 DP。"),
 ],
 "related": [
   "<strong>第 278 題 第一個錯誤的版本</strong>",
   "<strong>第 375 題 猜數字大小 II</strong>",
   "<strong>第 704 題 二分搜尋</strong>",
 ],
 "check": [
   "guess 回傳 −1 時要往哪邊找？",
   "最多需要猜幾次？",
 ],
})
