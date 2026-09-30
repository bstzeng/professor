# -*- coding: utf-8 -*-
"""第 319、321、322、324、326、327 題。"""
import random
import itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(319)


# ==================== 319. Bulb Switcher ====================
S["p319"] = '''class Solution:
    def bulbSwitch(self, n: int) -> int:
        # ★ 燈泡 k 被切換的次數 = k 的因數個數；只有完全平方數的因數個數是奇數
        return math.isqrt(n)'''

S["p319_sim"] = '''class Solution:
    def bulbSwitch(self, n: int) -> int:
        bulbs = [False] * (n + 1)
        for r in range(1, n + 1):              # 第 r 輪：切換 r 的倍數
            for k in range(r, n + 1, r):
                bulbs[k] = not bulbs[k]
        return sum(bulbs)'''

_p319 = [S.load(x) for x in ("p319", "p319_sim")]
for n in range(0, 400):
    assert _p319[0].bulbSwitch(n) == _p319[1].bulbSwitch(n), n
assert _p319[0].bulbSwitch(10 ** 9) == 31622
print("P319 OK")

emit({
 "num": 319, "slug": "bulb-switcher",
 "en": [
   "There are <code>n</code> bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.",
   "On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the <code>i<sup>th</sup></code> round, you toggle every <code>i</code> bulb. "
   "For the <code>n<sup>th</sup></code> round, you only toggle the last bulb.",
   "Return <em>the number of bulbs that are on after <code>n</code> rounds</em>.",
 ],
 "zh": [
   "有 <code>n</code> 個燈泡，一開始全部關著。第 1 輪把所有燈泡打開，第 2 輪把每第 2 個燈泡關掉，",
   "第 3 輪切換每第 3 個燈泡（開變關、關變開）……第 <code>i</code> 輪切換每第 <code>i</code> 個燈泡。第 <code>n</code> 輪只切換最後一個。",
   "回傳 <code>n</code> 輪之後有幾個燈泡是亮的。",
 ],
 "examples": """範例 1
  輸入：n = 3
  輸出：1
  說明：
    一開始   [關, 關, 關]
    第 1 輪  [開, 開, 開]
    第 2 輪  [開, 關, 開]
    第 3 輪  [開, 關, 關]

範例 2
  輸入：n = 0
  輸出：0

範例 3
  輸入：n = 1
  輸出：1""",
 "constraints": [
   "0 ≤ <code>n</code> ≤ 10⁹",
 ],
 "idea": [
   ("c", """【燈泡 k 在第 r 輪被切換 <=> r 是 k 的因數】
    所以燈泡 k 總共被切換「k 的因數個數」次。
    切換奇數次 -> 最後是亮的。

【什麼數的因數個數是奇數？】
    因數總是成對出現：d 和 k/d。
        12 的因數：(1,12) (2,6) (3,4) -> 6 個，偶數
    只有 d == k/d 時，這一對只算一個 —— 也就是 k 是完全平方數。
        16 的因數：(1,16) (2,8) (4,4) -> 1,2,4,8,16，5 個，奇數

【答案】
    1..n 之間的完全平方數個數 = ⌊√n⌋

【注意浮點數】
    int(n ** 0.5) 在 n 很大時可能因為浮點誤差少 1；
    Python 3.8+ 的 math.isqrt 是精確的整數平方根。"""),
   ("t", ["燈泡", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
    [["因數個數", "1", "2", "2", "3", "2", "4", "2", "4", "3"],
     ["最後", "亮", "暗", "暗", "亮", "暗", "暗", "暗", "暗", "亮"]]),
 ],
 "approaches": [
   ap("解法一", "模擬（觀察規律用）", [
     ("c", S["p319_sim"]),
     "O(n log n)（調和級數），n = 10⁹ 時太慢，但可以用來驗證規律。",
   ], "O(n log n)", "O(n)", "", ""),

   ap("解法二", "數學：⌊√n⌋", [
     ("c", S["p319"]),
   ], "O(1)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、模擬", "O(n log n)", "O(n)"],
    ["二、⌊√n⌋", "O(1)", "O(1) ✔"]]),
 "edges": [
   "<strong>n = 0</strong> → 0。",
   "<strong>n = 10⁹</strong> → 31622；用 <code>math.isqrt</code> 避免浮點誤差。",
 ],
 "follow": [
   ("h", "變化題"),
   ("c", "第 672 題「燈泡開關 II」只有四種按鈕，狀態空間很小；第 1375 題「二進位字串前綴一致的次數」則是另一種開燈問題。"),
 ],
 "related": [
   "<strong>第 672 題 燈泡開關 II</strong>",
   "<strong>第 367 題 有效的完全平方數</strong>",
 ],
 "check": [
   "燈泡 k 總共被切換幾次？",
   "為什麼只有完全平方數的因數個數是奇數？",
   "為什麼建議用 math.isqrt？",
 ],
})


# ==================== 321. Create Maximum Number ====================
S["p321"] = '''class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def pick(nums: List[int], t: int) -> List[int]:
            # 從 nums 中保持順序挑 t 個，使結果最大（單調遞減堆疊）
            drop = len(nums) - t                     # 可以丟掉幾個
            stack = []
            for x in nums:
                while drop and stack and stack[-1] < x:
                    stack.pop()
                    drop -= 1
                stack.append(x)
            return stack[:t]

        def merge(a: List[int], b: List[int]) -> List[int]:
            # ★ 比較「剩下的整段」而不是只比第一位（Python 串列比較就是字典序）
            return [max(a, b).pop(0) for _ in range(len(a) + len(b))]

        best = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            best = max(best, merge(pick(nums1, i), pick(nums2, k - i)))
        return best'''

_p321 = S.load("p321")


def _mn_ref(a, b, k):
    best = []
    for i in range(0, k + 1):
        if i > len(a) or k - i > len(b):
            continue
        for ca in itertools.combinations(range(len(a)), i):
            for cb in itertools.combinations(range(len(b)), k - i):
                xa, xb = [a[t] for t in ca], [b[t] for t in cb]
                # 所有合併方式
                for pos in itertools.combinations(range(k), i):
                    r, ia, ib, ps = [], 0, 0, set(pos)
                    for t in range(k):
                        if t in ps:
                            r.append(xa[ia]); ia += 1
                        else:
                            r.append(xb[ib]); ib += 1
                    best = max(best, r)
    return best


for a, b, k, want in [([3, 4, 6, 5], [9, 1, 2, 5, 8, 3], 5, [9, 8, 6, 5, 3]), ([6, 7], [6, 0, 4], 5, [6, 7, 6, 0, 4]), ([3, 9], [8, 9], 3, [9, 8, 9])]:
    assert _p321.maxNumber(a, b, k) == want
for _ in range(300):
    a = [random.randrange(0, 5) for _ in range(random.randrange(0, 5))]
    b = [random.randrange(0, 5) for _ in range(random.randrange(0, 5))]
    if not a and not b:
        continue
    k = random.randrange(1, len(a) + len(b) + 1)
    assert _p321.maxNumber(a, b, k) == _mn_ref(a, b, k), (a, b, k)
print("P321 OK")

emit({
 "num": 321, "slug": "create-maximum-number",
 "en": [
   "You are given two integer arrays <code>nums1</code> and <code>nums2</code> of lengths <code>m</code> and <code>n</code> respectively. <code>nums1</code> and <code>nums2</code> represent the digits of two numbers. You are also given an integer <code>k</code>.",
   "Create the maximum number of length <code>k &lt;= m + n</code> from digits of the two numbers. The relative order of the digits from the same array must be preserved.",
   "Return an array of the <code>k</code> digits representing the answer.",
 ],
 "zh": [
   "給你兩個整數陣列 <code>nums1</code>、<code>nums2</code>（長度 <code>m</code>、<code>n</code>），各自代表一個數字的各位數，以及整數 <code>k</code>。",
   "從兩個陣列中挑出共 <code>k</code> 位數字（<code>k ≤ m + n</code>），拼成<strong>最大</strong>的數。來自同一個陣列的數字必須保持原本的相對順序。",
   "回傳這 <code>k</code> 位數字組成的陣列。",
 ],
 "examples": """範例 1
  輸入：nums1 = [3,4,6,5], nums2 = [9,1,2,5,8,3], k = 5
  輸出：[9,8,6,5,3]

範例 2
  輸入：nums1 = [6,7], nums2 = [6,0,4], k = 5
  輸出：[6,7,6,0,4]

範例 3
  輸入：nums1 = [3,9], nums2 = [8,9], k = 3
  輸出：[9,8,9]""",
 "constraints": [
   "<code>m == nums1.length</code>，<code>n == nums2.length</code>",
   "1 ≤ <code>m, n</code> ≤ 500",
   "0 ≤ <code>nums1[i], nums2[i]</code> ≤ 9",
   "1 ≤ <code>k</code> ≤ <code>m + n</code>",
 ],
 "idea": [
   ("c", """【拆成三個子問題】
    1. 枚舉從 nums1 拿 i 個、nums2 拿 k - i 個
    2. 從一個陣列中保持順序挑 t 個，使結果最大
    3. 把兩個結果合併成最大的數
    所有 i 的結果取最大。

【子問題 2：單調堆疊（第 402 題的反面）】
    可以丟掉 len - t 個數字。
    從左到右，遇到比堆疊頂端大的數字，
    而且還有丟棄額度 -> 把頂端丟掉（讓大的數字往前）。

【子問題 3：合併 —— 陷阱在相等的時候】
    像合併排序一樣每次取較大的，
    但兩邊開頭相同時要看後面：
        a = [6, 7]，b = [6, 0, 4]
        開頭都是 6。取 a 的 6 -> 下一步能拿到 7 ✔
                    取 b 的 6 -> 下一步是 max(6, 0) = 6 ✘
    正確做法：比較「整段剩下的序列」的字典序，取較大的那邊的開頭。

【複雜度】
    枚舉 i 共 O(k) 種；每種挑選 O(m + n)，合併最壞 O(k²)（逐段比較）
    -> O(k · (m + n + k²))，實際上很快。"""),
 ],
 "approaches": [
   ap("解法", "枚舉分配 + 單調堆疊 + 字典序合併", [
     ("c", S["p321"]),
     ("c", """【merge 那一行在做什麼？】
    max(a, b) 用 Python 串列的字典序比較，選出「剩下的部分比較大」的那個串列，
    pop(0) 取出它的開頭。重複 len(a)+len(b) 次。
    （pop(0) 是 O(n)，要更快可以改用索引，但長度只有幾百，不影響。）"""),
   ], "O(k · (m + n + k²))", "O(m + n + k)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>開頭相同</strong> → 一定要比較後續，不能只看第一位。",
   "<strong>i 的範圍</strong> → 至少 max(0, k − n)，最多 min(k, m)。",
   "<strong>一個陣列全部都要拿</strong> → 單調堆疊不會丟任何東西。",
 ],
 "follow": [
   ("h", "拆解成已知題"),
   ("c", "「挑 t 個使結果最大」= 第 402 題（移掉 K 位數字，最小）的反向；「兩個序列合併成最大」= 第 1754 題（構造字典序最大的合併字串）。"),
 ],
 "related": [
   "<strong>第 402 題 移掉 K 位數字</strong>",
   "<strong>第 316 題 去除重複字母</strong>",
   "<strong>第 1754 題 構造字典序最大的合併字串</strong>",
 ],
 "check": [
   "這題可以拆成哪三個子問題？",
   "單調堆疊什麼時候可以丟掉頂端？",
   "合併時兩邊開頭相同，為什麼要比較後面？",
 ],
})


# ==================== 322. Coin Change ====================
S["p322"] = '''class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = amount + 1                       # 不可能的值（最多用 amount 個 1 元）
        dp = [0] + [INF] * amount              # dp[x]：湊出 x 最少要幾枚
        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    # ★ 最後一枚是 c：剩下的 x - c 用最少的方式湊
                    dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] < INF else -1'''

S["p322_bfs"] = '''class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        seen = {0}
        frontier = [0]
        steps = 0
        while frontier:                       # BFS：第幾層 = 用了幾枚
            steps += 1
            nxt = []
            for s in frontier:
                for c in coins:
                    t = s + c
                    if t == amount:
                        return steps
                    if t < amount and t not in seen:
                        seen.add(t)
                        nxt.append(t)
            frontier = nxt
        return -1'''

S["p322_greedy_wrong"] = '''class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # ✘ 錯誤示範：每次拿最大的面額
        count = 0
        for c in sorted(coins, reverse=True):
            count += amount // c
            amount %= c
        return count if amount == 0 else -1'''

_p322 = [S.load(x) for x in ("p322", "p322_bfs")]
_g = S.load("p322_greedy_wrong")
assert _g.coinChange([1, 3, 4], 6) == 3 and _p322[0].coinChange([1, 3, 4], 6) == 2
for coins, amt, want in [([1, 2, 5], 11, 3), ([2], 3, -1), ([1], 0, 0), ([186, 419, 83, 408], 6249, 20)]:
    for sol in _p322:
        assert sol.coinChange(coins, amt) == want


def _cc_ref(coins, amt):
    import functools

    @functools.lru_cache(None)
    def f(x):                                   # 遞迴窮舉「最後一枚」
        if x == 0:
            return 0
        opts = [f(x - c) for c in coins if c <= x]
        opts = [o for o in opts if o >= 0]
        return min(opts) + 1 if opts else -1
    return f(amt)


for _ in range(800):
    coins = random.sample(range(1, 12), random.randrange(1, 4))
    amt = random.randrange(0, 25)
    want = _cc_ref(coins, amt)
    for sol in _p322:
        assert sol.coinChange(coins, amt) == want, (coins, amt, sol)
print("P322 OK")

emit({
 "num": 322, "slug": "coin-change",
 "en": [
   "You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.",
   "Return <em>the fewest number of coins that you need to make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.",
   "You may assume that you have an infinite number of each kind of coin.",
 ],
 "zh": [
   "給你一個代表不同面額硬幣的陣列 <code>coins</code>，以及總金額 <code>amount</code>。",
   "回傳湊出總金額所需的<strong>最少硬幣數</strong>。如果無法湊出，回傳 <code>-1</code>。",
   "每種硬幣的數量都是無限的。",
 ],
 "examples": """範例 1
  輸入：coins = [1,2,5], amount = 11
  輸出：3
  說明：11 = 5 + 5 + 1

範例 2
  輸入：coins = [2], amount = 3
  輸出：-1

範例 3
  輸入：coins = [1], amount = 0
  輸出：0""",
 "constraints": [
   "1 ≤ <code>coins.length</code> ≤ 12",
   "1 ≤ <code>coins[i]</code> ≤ 2³¹ − 1",
   "0 ≤ <code>amount</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【貪心為什麼不行？】
    coins = [1, 3, 4]，amount = 6
    貪心：4 + 1 + 1 = 3 枚
    最佳：3 + 3     = 2 枚 ✘
    （台幣、美元這種面額設計剛好讓貪心成立，但一般情況不成立。）

【完全背包 DP】
    dp[x] = 湊出 x 的最少硬幣數
    dp[0] = 0
    dp[x] = min(dp[x - c] + 1)  對每個 c <= x
    「最後一枚是 c」-> 剩下 x - c 用最少的方式湊。

【不可能的標記】
    用 amount + 1 當作「無限大」：
    就算全用 1 元也只要 amount 枚，所以 amount + 1 不可能是真的答案。

【BFS 觀點】
    金額是節點，加一枚硬幣是一條邊，
    從 0 走到 amount 的最短路徑 = 最少硬幣數。"""),
   ("t", ["x", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
    [["dp[x]", "0", "1", "1", "2", "2", "1", "2", "2", "3", "3", "2", "3"]]),
 ],
 "approaches": [
   ap("錯誤示範", "貪心（每次拿最大面額）", [
     ("c", S["p322_greedy_wrong"]),
     "coins = [1, 3, 4]、amount = 6 時回傳 3，正確答案是 2。",
   ]),

   ap("解法一", "BFS 最短路徑", [
     ("c", S["p322_bfs"]),
   ], "O(amount · k)", "O(amount)", "k = 硬幣種類數", ""),

   ap("解法二", "完全背包 DP", [
     ("c", S["p322"]),
   ], "O(amount · k)", "O(amount)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["貪心", "O(k log k)", "O(1)", "錯誤"],
    ["一、BFS", "O(amount·k)", "O(amount)", "找到就停"],
    ["二、DP", "O(amount·k)", "O(amount)", "標準 ✔"]]),
 "edges": [
   "<strong>amount = 0</strong> → 0。",
   "<strong>無法湊出</strong> → −1。",
   "<strong>硬幣面額大於 amount</strong> → 直接跳過。",
   "<strong>面額很大</strong>（2³¹ − 1）→ <code>c &lt;= x</code> 的判斷避免負索引。",
 ],
 "follow": [
   ("h", "追問：有幾種湊法？"),
   ("c", """第 518 題「零錢兌換 II」：dp[x] += dp[x − c]。
但要注意迴圈順序：外層硬幣、內層金額 → 算「組合數」（1+2 和 2+1 算同一種）；
外層金額、內層硬幣 → 算「排列數」（第 377 題）。"""),
 ],
 "related": [
   "<strong>第 518 題 零錢兌換 II</strong>",
   "<strong>第 279 題 完全平方數</strong> —— 同一個完全背包",
   "<strong>第 377 題 組合總和 IV</strong> —— 排列數",
 ],
 "check": [
   "舉一個貪心會出錯的例子。",
   "dp[x] 的轉移式是什麼？",
   "為什麼用 amount + 1 表示無法湊出？",
 ],
})


# ==================== 324. Wiggle Sort II ====================
S["p324_sort"] = '''class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = sorted(nums)
        half = (len(nums) + 1) // 2
        # ★ 小的一半、大的一半各自「反轉」後交錯放：避免相等的中位數相鄰
        nums[::2] = s[:half][::-1]         # 偶數位置放較小的一半（由大到小）
        nums[1::2] = s[half:][::-1]        # 奇數位置放較大的一半（由大到小）'''

S["p324_cnt"] = '''class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        cnt = [0] * 5001                   # 值域 0..5000：計數排序
        for x in nums:
            cnt[x] += 1
        v = 5000
        # 先填奇數位置（放大的），再填偶數位置，都從大到小取
        for start in (1, 0):
            for i in range(start, len(nums), 2):
                while cnt[v] == 0:
                    v -= 1
                nums[i] = v
                cnt[v] -= 1'''

_p324 = [S.load(x) for x in ("p324_sort", "p324_cnt")]


def _is_wiggle(a):
    return all((a[i] < a[i + 1]) if i % 2 == 0 else (a[i] > a[i + 1]) for i in range(len(a) - 1))


for _ in range(4000):
    n = random.randrange(1, 12)
    # 產生一定有解的輸入：先造一個 wiggle 再打亂
    base = sorted(random.randint(0, 6) for _ in range(n))
    half = (n + 1) // 2
    w = [0] * n
    w[::2] = base[:half][::-1]
    w[1::2] = base[half:][::-1]
    if not _is_wiggle(w):
        continue
    random.shuffle(base)
    for sol in _p324:
        a = list(base)
        sol.wiggleSort(a)
        assert _is_wiggle(a) and sorted(a) == sorted(base), (base, a, sol)
print("P324 OK")

emit({
 "num": 324, "slug": "wiggle-sort-ii",
 "en": [
   "Given an integer array <code>nums</code>, reorder it such that <code>nums[0] &lt; nums[1] &gt; nums[2] &lt; nums[3]...</code>.",
   "You may assume the input array always has a valid answer.",
   "<strong>Follow Up:</strong> Can you do it in <code>O(n)</code> time and/or <strong>in-place</strong> with <code>O(1)</code> extra space?",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，把它重新排列成 <code>nums[0] &lt; nums[1] &gt; nums[2] &lt; nums[3]...</code>（嚴格的一小一大交錯）。",
   "保證一定有合法的答案。",
   "<strong>進階：</strong>能在 <code>O(n)</code> 時間、<code>O(1)</code> 額外空間內原地完成嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [1,5,1,1,6,4]
  輸出：[1,6,1,5,1,4]
  說明：[1,4,1,5,1,6] 也可以。

範例 2
  輸入：nums = [1,3,2,2,3,1]
  輸出：[2,3,1,3,1,2]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 5 × 10⁴",
   "0 ≤ <code>nums[i]</code> ≤ 5000",
   "保證有合法答案",
 ],
 "idea": [
   ("c", """【直覺：小的放偶數位置、大的放奇數位置】
    排序後切成兩半：小半 S、大半 L，交錯放 S L S L ...
    每個 L 都 >= 兩邊的 S。

【陷阱：中位數重複】
    nums = [4, 5, 5, 6]
    小半 [4, 5]、大半 [5, 6]
    順著放：4 5 5 6 -> 5 和 5 相鄰，5 < 5 不成立 ✘

【解法：兩半都「反轉」再交錯】
    小半反轉 [5, 4]、大半反轉 [6, 5]
    交錯：5 6 4 5 ✔
    反轉後，小半的中位數被放到最前面，大半的中位數被放到最後面，
    相等的中位數在陣列中離得最遠，不會相鄰。

【O(n) 時間】
    值域只有 0..5000 -> 計數排序。
    （更一般的 O(n) + O(1) 空間做法：快速選擇找中位數 + 三向切分 + 虛擬索引映射，
     非常精巧但不好寫。）"""),
   ("c", """  排序後   [1, 1, 1, 4, 5, 6]
  小半反轉 [1, 1, 1]      大半反轉 [6, 5, 4]
  交錯     1  6  1  5  1  4  ✔"""),
 ],
 "approaches": [
   ap("解法一", "排序 + 兩半反轉交錯", [
     ("c", S["p324_sort"]),
   ], "O(n log n)", "O(n)", "", ""),

   ap("解法二", "計數排序（值域小）", [
     ("c", S["p324_cnt"]),
     "從最大值開始，先填滿所有奇數位置，再填偶數位置——和解法一的「反轉交錯」是同一個排列。",
   ], "O(n + V)", "O(V)", "V = 值域大小 5001", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、排序", "O(n log n)", "O(n)"],
    ["二、計數排序", "O(n + V)", "O(V) ✔"]]),
 "edges": [
   "<strong>中位數重複很多次</strong> → 一定要反轉，否則相等元素會相鄰。",
   "<strong>奇數長度</strong> → 小半比大半多一個（偶數位置比較多）。",
   "<strong>n = 1</strong> → 不變。",
 ],
 "follow": [
   ("h", "第 280 題（付費）"),
   ("c", "Wiggle Sort I 允許相等（≤ ≥ ≤），只要一趟掃描：相鄰兩個不符合就交換，O(n)。嚴格版本就難多了。"),
 ],
 "related": [
   "<strong>第 280 題 擺動排序</strong>（付費）",
   "<strong>第 215 題 陣列中的第 K 個最大元素</strong> —— 快速選擇",
   "<strong>第 75 題 顏色分類</strong> —— 三向切分",
 ],
 "check": [
   "為什麼直接把小半、大半交錯放可能失敗？舉例。",
   "兩半反轉後為什麼就不會有相等的元素相鄰？",
 ],
})


# ==================== 326. Power of Three ====================
S["p326_loop"] = '''class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1'''

S["p326"] = '''class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # ★ 3^19 = 1162261467 是 32 位元內最大的 3 的冪；3 是質數，它的因數只有 3 的冪
        return n > 0 and 1162261467 % n == 0'''

_p326 = [S.load(x) for x in ("p326_loop", "p326")]
_pw3 = {3 ** i for i in range(20)}
for n in list(range(-30, 3000)) + [3 ** 19, 3 ** 19 - 1, 2 ** 31 - 1, 3 ** 18 * 2, 3 ** 10]:
    for sol in _p326:
        assert sol.isPowerOfThree(n) == (n in _pw3), n
print("P326 OK")

emit({
 "num": 326, "slug": "power-of-three",
 "en": [
   "Given an integer <code>n</code>, return <code>true</code> <em>if it is a power of three. Otherwise, return</em> <code>false</code>.",
   "An integer <code>n</code> is a power of three, if there exists an integer <code>x</code> such that <code>n == 3<sup>x</sup></code>.",
   "<strong>Follow up:</strong> Could you solve it without loops/recursion?",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，判斷它是不是 3 的冪次（存在整數 <code>x</code> 使 <code>n == 3<sup>x</sup></code>）。",
   "<strong>進階：</strong>能不用迴圈或遞迴嗎？",
 ],
 "examples": """範例 1
  輸入：n = 27
  輸出：true

範例 2
  輸入：n = 0
  輸出：false

範例 3
  輸入：n = -1
  輸出：false""",
 "constraints": [
   "−2³¹ ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【2 的冪有位元技巧，3 的冪沒有】
    二進位中 3 的冪沒有特別的樣子。

【方法一：一直除以 3】
    除到不能整除為止，看是不是剩 1。

【方法二：整除最大的 3 的冪】
    32 位元範圍內最大的 3 的冪是 3¹⁹ = 1162261467。
    3 是質數 -> 3¹⁹ 的因數只有 3⁰, 3¹, ..., 3¹⁹。
    所以 n 是 3 的冪 <=> n > 0 且 n 整除 3¹⁹。

    這個技巧只對【質數】的冪次成立：
    例如 4 的冪不能這樣做 —— 2 也整除 4¹⁵，但 2 不是 4 的冪。

【方法三（不推薦）：對數】
    log₃(n) 是整數？浮點誤差很難處理：
    math.log(243, 3) = 4.999999999999999 ✘"""),
 ],
 "approaches": [
   ap("解法一", "反覆除以 3", [
     ("c", S["p326_loop"]),
   ], "O(log n)", "O(1)", "", ""),

   ap("解法二", "3¹⁹ 能否被 n 整除", [
     ("c", S["p326"]),
   ], "O(1)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、除法", "O(log n)", "通用"],
    ["二、整除 3¹⁹", "O(1)", "只適用於質數的冪 ✔"]]),
 "edges": [
   "<strong>n = 1</strong> → true（3⁰）。",
   "<strong>n ≤ 0</strong> → false；解法一要先檢查，否則 n = 0 會無窮迴圈。",
   "<strong>用 log 判斷</strong> → 浮點誤差，不可靠。",
 ],
 "follow": [
   ("h", "冪次判斷整理"),
   ("c", "2 的冪：n &amp; (n−1) == 0。4 的冪：先是 2 的冪，而且唯一的 1 在偶數位（n &amp; 0x55555555）或 n % 3 == 1。3 的冪：整除 3¹⁹。"),
 ],
 "related": [
   "<strong>第 231 題 2 的冪</strong>",
   "<strong>第 342 題 4 的冪</strong>",
   "<strong>第 1780 題 判斷一個數能否表示成三的冪的和</strong>",
 ],
 "check": [
   "為什麼 n 整除 3¹⁹ 就代表 n 是 3 的冪？",
   "這個技巧為什麼不能用在 4 的冪？",
   "為什麼不建議用對數判斷？",
 ],
})


# ==================== 327. Count of Range Sum ====================
S["p327_merge"] = '''class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # 前綴和：區間和 = P[j] - P[i]；要數有幾對 i < j 使 lower <= P[j] - P[i] <= upper
        P = [0]
        for x in nums:
            P.append(P[-1] + x)

        def sort(lo: int, hi: int) -> int:      # 排序 P[lo:hi] 並回傳跨左右的對數
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)
            # ★ 左右兩半各自已排序：對每個左邊的 P[i]，右邊合格的 P[j] 是一段連續區間
            l = r = mid
            for i in range(lo, mid):
                while l < hi and P[l] - P[i] < lower:
                    l += 1
                while r < hi and P[r] - P[i] <= upper:
                    r += 1
                count += r - l
            P[lo:hi] = sorted(P[lo:hi])         # 合併（這裡用 sorted 簡化，仍是 O(n log n)）
            return count

        return sort(0, len(P))'''

S["p327_bit"] = '''class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        P = [0]
        for x in nums:
            P.append(P[-1] + x)
        vals = sorted(set(P))                   # 座標壓縮
        m = len(vals)
        tree = [0] * (m + 1)

        def add(i):
            while i <= m:
                tree[i] += 1
                i += i & -i

        def query(i):                           # 名次 1..i 的個數
            s = 0
            while i:
                s += tree[i]
                i -= i & -i
            return s

        count = 0
        for p in P:
            # 之前的 P[i] 要落在 [p - upper, p - lower]
            lo = bisect.bisect_left(vals, p - upper)       # 名次 > lo 的
            hi = bisect.bisect_right(vals, p - lower)      # 名次 <= hi 的
            count += query(hi) - query(lo)
            add(bisect.bisect_left(vals, p) + 1)
        return count'''

_p327 = [S.load(x) for x in ("p327_merge", "p327_bit")]
for nums, lo, hi, want in [([-2, 5, -1], -2, 2, 3), ([0], 0, 0, 1)]:
    for sol in _p327:
        assert sol.countRangeSum(nums, lo, hi) == want
for _ in range(3000):
    nums = [random.randint(-5, 5) for _ in range(random.randrange(1, 12))]
    lo = random.randint(-6, 6)
    hi = random.randint(lo, lo + 8)
    want = sum(lo <= sum(nums[i:j]) <= hi for i in range(len(nums)) for j in range(i + 1, len(nums) + 1))
    for sol in _p327:
        assert sol.countRangeSum(nums, lo, hi) == want, (nums, lo, hi, sol)
print("P327 OK")

emit({
 "num": 327, "slug": "count-of-range-sum",
 "en": [
   "Given an integer array <code>nums</code> and two integers <code>lower</code> and <code>upper</code>, return <em>the number of range sums that lie in</em> <code>[lower, upper]</code> <em>inclusive</em>.",
   "Range sum <code>S(i, j)</code> is defined as the sum of the elements in <code>nums</code> between indices <code>i</code> and <code>j</code> inclusive, where <code>i &lt;= j</code>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code> 和兩個整數 <code>lower</code>、<code>upper</code>，回傳有幾個<strong>區間和</strong>落在 <code>[lower, upper]</code> 之間（包含兩端）。",
   "區間和 <code>S(i, j)</code> 是 <code>nums[i] + ... + nums[j]</code>（<code>i ≤ j</code>）。",
 ],
 "examples": """範例 1
  輸入：nums = [-2,5,-1], lower = -2, upper = 2
  輸出：3
  說明：[0,0]、[2,2]、[0,2] 的和分別是 -2、-1、2。

範例 2
  輸入：nums = [0], lower = 0, upper = 0
  輸出：1""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
   "−10⁵ ≤ <code>lower ≤ upper</code> ≤ 10⁵",
   "答案保證在 32 位元整數範圍內",
 ],
 "idea": [
   ("c", """【前綴和轉換】
    P[0] = 0，P[k] = nums[0] + ... + nums[k-1]
    區間和 S(i, j) = P[j+1] - P[i]
    問題變成：有幾對 a < b，使得 lower <= P[b] - P[a] <= upper？

    也就是：對每個 P[b]，
    前面有幾個 P[a] 落在 [P[b] - upper, P[b] - lower]？

【方法一：樹狀陣列（和第 315 題同一個套路）】
    由左到右掃過 P，
    查詢「已經看過的前綴和中，落在某個值域的有幾個」，
    再把 P[b] 加進去。
    值很大（可到 10¹⁴）-> 座標壓縮。

【方法二：合併排序】
    排序 P 的過程中，左半、右半各自已排序。
    所有「a 在左半、b 在右半」的配對：
        對左邊每個 P[a]，右邊合格的 P[b] 是一段連續區間 [l, r)，
        而且 P[a] 變大時，l、r 只會往右 -> 雙指標 O(n)。
    左半內部、右半內部的配對由遞迴處理。"""),
 ],
 "approaches": [
   ap("解法一", "前綴和 + 座標壓縮 + 樹狀陣列", [
     ("c", S["p327_bit"]),
   ], "O(n log n)", "O(n)", "", ""),

   ap("解法二", "前綴和 + 合併排序", [
     ("c", S["p327_merge"]),
     ("c", """【為什麼排序不會破壞「a < b」的關係？】
    計數時只配對「a 在左半、b 在右半」，
    左半的原始索引都小於右半 —— 在各自內部怎麼排序都不影響這個事實。"""),
   ], "O(n log n)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["暴力", "O(n²)", "O(1)"],
    ["一、樹狀陣列", "O(n log n)", "O(n)"],
    ["二、合併排序", "O(n log n)", "O(n) ✔"]]),
 "edges": [
   "<strong>前綴和很大</strong>（10⁵ × 2³¹）→ Python 沒有溢位；其他語言用 64 位元。",
   "<strong>lower = upper</strong> → 數「和剛好等於某值」的區間。",
   "<strong>別忘了 P[0] = 0</strong> → 從索引 0 開始的區間要靠它。",
 ],
 "follow": [
   ("h", "簡化版"),
   ("c", "第 560 題「和為 K 的子陣列」：lower = upper = k，而且可以用雜湊表 O(n)——因為只需要「剛好等於」，不需要值域查詢。"),
 ],
 "related": [
   "<strong>第 315 題 計算右側小於當前元素的個數</strong>",
   "<strong>第 493 題 翻轉對</strong>",
   "<strong>第 560 題 和為 K 的子陣列</strong>",
 ],
 "check": [
   "區間和怎麼用前綴和表示？問題轉換成什麼？",
   "合併排序中，為什麼合格的 P[b] 是連續的一段？",
   "排序為什麼不會影響 a &lt; b 的條件？",
 ],
})
