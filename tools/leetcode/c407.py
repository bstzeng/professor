# -*- coding: utf-8 -*-
"""第 407、409、410、412、413、414 題。"""
import random
import itertools
from collections import Counter
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(407)


# ==================== 407. Trapping Rain Water II ====================
S["p407"] = '''class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        seen = [[False] * n for _ in range(m)]
        heap = []
        for i in range(m):                     # 最外圈是「牆」，先放進最小堆積
            for j in range(n):
                if i in (0, m - 1) or j in (0, n - 1):
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    seen[i][j] = True
        water = 0
        while heap:
            h, i, j = heapq.heappop(heap)      # ★ 目前牆上「最矮」的一格
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and not seen[x][y]:
                    seen[x][y] = True
                    water += max(0, h - heightMap[x][y])     # 比最矮的牆低 -> 積水
                    # 新的牆高度 = 自己和水面取大
                    heapq.heappush(heap, (max(h, heightMap[x][y]), x, y))
        return water'''

_p407 = S.load("p407")


def _trap2_ref(H):
    # 參考解：每格的水位 = 所有「到邊界的路徑」上最大高度的最小值（Bellman-Ford 式鬆弛）
    m, n = len(H), len(H[0])
    INF = 10 ** 9
    lvl = [[H[i][j] if i in (0, m - 1) or j in (0, n - 1) else INF for j in range(n)] for i in range(m)]
    changed = True
    while changed:
        changed = False
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                best = min(lvl[i + 1][j], lvl[i - 1][j], lvl[i][j + 1], lvl[i][j - 1])
                v = max(H[i][j], best)
                if v < lvl[i][j]:
                    lvl[i][j] = v
                    changed = True
    return sum(lvl[i][j] - H[i][j] for i in range(m) for j in range(n))


for H, want in [([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4),
                ([[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]], 10)]:
    assert _p407.trapRainWater(H) == want
for _ in range(1000):
    m, n = random.randrange(1, 7), random.randrange(1, 7)
    H = [[random.randint(0, 6) for _ in range(n)] for _ in range(m)]
    assert _p407.trapRainWater(H) == _trap2_ref(H), H
print("P407 OK")

_P407_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">從外圈往內「灌水」：每次從最矮的牆往內擴張</text>
            <g font-size="13" text-anchor="middle">
              <g fill="none" stroke="var(--border)">
                <rect x="40" y="40" width="200" height="200"/>
                <line x1="80" y1="40" x2="80" y2="240"/><line x1="120" y1="40" x2="120" y2="240"/><line x1="160" y1="40" x2="160" y2="240"/><line x1="200" y1="40" x2="200" y2="240"/>
                <line x1="40" y1="80" x2="240" y2="80"/><line x1="40" y1="120" x2="240" y2="120"/><line x1="40" y1="160" x2="240" y2="160"/><line x1="40" y1="200" x2="240" y2="200"/>
              </g>
              <rect x="80" y="80" width="120" height="120" fill="var(--accent)" opacity="0.18"/>
              <text x="60" y="65" fill="var(--text-muted)">3</text><text x="100" y="65" fill="var(--text-muted)">3</text><text x="140" y="65" fill="var(--text-muted)">3</text><text x="180" y="65" fill="var(--text-muted)">3</text><text x="220" y="65" fill="var(--text-muted)">3</text>
              <text x="60" y="105" fill="var(--text-muted)">3</text><text x="100" y="105" fill="var(--accent)">2</text><text x="140" y="105" fill="var(--accent)">2</text><text x="180" y="105" fill="var(--accent)">2</text><text x="220" y="105" fill="var(--text-muted)">3</text>
              <text x="60" y="145" fill="var(--text-muted)">3</text><text x="100" y="145" fill="var(--accent)">2</text><text x="140" y="145" fill="var(--accent)">1</text><text x="180" y="145" fill="var(--accent)">2</text><text x="220" y="145" fill="var(--text-muted)">3</text>
              <text x="60" y="185" fill="var(--text-muted)">3</text><text x="100" y="185" fill="var(--accent)">2</text><text x="140" y="185" fill="var(--accent)">2</text><text x="180" y="185" fill="var(--accent)">2</text><text x="220" y="185" fill="var(--text-muted)">3</text>
              <text x="60" y="225" fill="var(--text-muted)">3</text><text x="100" y="225" fill="var(--text-muted)">3</text><text x="140" y="225" fill="var(--text-muted)">3</text><text x="180" y="225" fill="var(--text-muted)">3</text><text x="220" y="225" fill="var(--text-muted)">3</text>
            </g>
            <text x="270" y="70" fill="var(--text)" font-size="12">外圈高度 3 是「牆」。</text>
            <text x="270" y="96" fill="var(--text)" font-size="12">內部 8 格高度 2：水可以積到 3 → 各 1 格水</text>
            <text x="270" y="120" fill="var(--text)" font-size="12">中心高度 1：水可以積到 3 → 2 格水</text>
            <text x="270" y="146" fill="var(--gold)" font-size="12">總共 8 × 1 + 2 = 10</text>
            <text x="270" y="186" fill="var(--text-muted)" font-size="12">★ 一格的水位由「包圍它的牆中最矮的缺口」決定，</text>
            <text x="270" y="206" fill="var(--text-muted)" font-size="12">　 所以從最矮的牆開始往內擴張（最小堆積）。</text>'''

emit({
 "num": 407, "slug": "trapping-rain-water-ii",
 "en": [
   "Given an <code>m x n</code> integer matrix <code>heightMap</code> representing the height of each unit cell in a 2D elevation map, return <em>the volume of water it can trap after raining</em>.",
 ],
 "zh": [
   "給你一個 <code>m x n</code> 的整數矩陣 <code>heightMap</code>，代表二維地形上每一格的高度，回傳下雨之後能積多少水。",
 ],
 "examples": """範例 1
  輸入：heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
  輸出：4

範例 2
  輸入：heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
  輸出：10""",
 "constraints": [
   "<code>m == heightMap.length</code>，<code>n == heightMap[i].length</code>",
   "1 ≤ <code>m, n</code> ≤ 200",
   "0 ≤ <code>heightMap[i][j]</code> ≤ 2 × 10⁴",
 ],
 "idea": [
   ("fig", _P407_FIG, "0 0 640 254"),
   ("c", """【一維版（第 42 題）的想法搬不過來】
    一維：水位 = min(左邊最高, 右邊最高)
    二維：水可以從任何方向繞路流出去，不能只看四個方向的最高點。

【從外往內：最小堆積（類似 Dijkstra）】
    最外圈的格子存不了水，它們是一開始的「牆」。
    每次取出目前牆上【最矮】的格子 h：
        它的未拜訪鄰居，如果比 h 低 -> 積水 h - 鄰居高度
        （水從這個最矮的缺口流出，所以水位就是 h）
        鄰居變成新的牆，高度 = max(h, 鄰居高度)

【為什麼從最矮的開始？】
    一格的水位 = 所有通往邊界的路徑中，「路徑上最高點」的最小值。
    這就是 minimax 路徑，用最小堆積像 Dijkstra 一樣擴張就能算出來。"""),
 ],
 "approaches": [
   ap("解法", "最小堆積從外往內擴張", [
     ("c", S["p407"]),
     "驗證方式：和「反覆鬆弛水位直到不再改變」的暴力版本比對一千組隨機地形。",
   ], "O(mn log(mn))", "O(mn)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>m 或 n 小於 3</strong> → 沒有內部格子，0。",
   "<strong>內部比外圈高</strong> → 不積水。",
   "<strong>有缺口</strong> → 水位被最矮的缺口決定。",
 ],
 "follow": [
   ("h", "minimax 路徑"),
   ("c", "第 778 題「水位上升的泳池中游泳」、第 1631 題「最小體力消耗路徑」都是「路徑上最大值的最小化」，同樣用最小堆積（或二分 + BFS、或並查集）。"),
 ],
 "related": [
   "<strong>第 42 題 接雨水</strong>",
   "<strong>第 778 題 水位上升的泳池中游泳</strong>",
   "<strong>第 1631 題 最小體力消耗路徑</strong>",
 ],
 "check": [
   "為什麼一維的「左最高、右最高」不能直接推廣到二維？",
   "為什麼每次要從最矮的牆開始擴張？",
   "新加入的牆高度為什麼是 max(h, 鄰居高度)？",
 ],
})


# ==================== 409. Longest Palindrome ====================
S["p409"] = '''class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = collections.Counter(s)
        length = sum(c // 2 * 2 for c in cnt.values())    # 每種字元盡量成對放在兩側
        # ★ 有任何字元剩下單一個，可以放在正中間
        return length + 1 if length < len(s) else length'''

_p409 = S.load("p409")
for s, want in [("abccccdd", 7), ("a", 1), ("Aa", 1), ("bb", 2)]:
    assert _p409.longestPalindrome(s) == want
for _ in range(2000):
    s = "".join(random.choice("abAB") for _ in range(random.randrange(1, 10)))
    c = Counter(s)
    want = sum(v // 2 * 2 for v in c.values()) + (1 if any(v % 2 for v in c.values()) else 0)
    assert _p409.longestPalindrome(s) == want
print("P409 OK")

emit({
 "num": 409, "slug": "longest-palindrome",
 "en": [
   "Given a string <code>s</code> which consists of lowercase or uppercase letters, return the length of the <strong>longest palindrome</strong> that can be built with those letters.",
   "Letters are <strong>case sensitive</strong>, for example, <code>\"Aa\"</code> is not considered a palindrome.",
 ],
 "zh": [
   "給你一個由大小寫字母組成的字串 <code>s</code>，用這些字母（可以重新排列）能組出的<strong>最長回文</strong>長度是多少？",
   "大小寫視為不同字元，例如 <code>\"Aa\"</code> 不是回文。",
 ],
 "examples": """範例 1
  輸入：s = "abccccdd"
  輸出：7
  說明："dccaccd"

範例 2
  輸入：s = "a"
  輸出：1""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 2000",
   "<code>s</code> 只包含大小寫英文字母",
 ],
 "idea": [
   ("c", """【回文的結構】
    左右對稱：每種字元成對出現，
    正中間可以多放一個「落單」的字元。

【計算】
    每種字元出現 c 次 -> 可以用 c // 2 * 2 個（成對）
    如果有任何字元還剩一個（出現奇數次）-> 中間再放一個，+1

【快速判斷有沒有剩】
    用掉的總數 < 原字串長度 -> 一定有剩的 -> +1"""),
 ],
 "approaches": [
   ap("解法", "計數：成對 + 中間一個", [
     ("c", S["p409"]),
   ], "O(n)", "O(1)", "", "最多 52 種字元", optimal=True),
 ],
 "edges": [
   "<strong>只有一個字元</strong> → 1。",
   "<strong>全部出現偶數次</strong> → 長度就是 n。",
   "<strong>大小寫不同</strong> → \"Aa\" 答案是 1。",
 ],
 "follow": [
   ("h", "相關題"),
   ("c", "第 266 題（付費，能否重排成回文：最多一種字元出現奇數次）、第 2131 題（兩字母單字組成的最長回文）。"),
 ],
 "related": [
   "<strong>第 5 題 最長回文子串</strong> —— 不能重排",
   "<strong>第 2131 題 連接兩字母單字得到的最長回文串</strong>",
 ],
 "check": [
   "回文中每種字元出現幾次？",
   "為什麼最多只能多放一個落單的字元？",
 ],
})


# ==================== 410. Split Array Largest Sum ====================
S["p410_bs"] = '''class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def pieces(limit: int) -> int:           # 每段和 <= limit 時，最少要切幾段
            count, cur = 1, 0
            for x in nums:
                if cur + x > limit:              # 放不下：開新的一段
                    count += 1
                    cur = 0
                cur += x
            return count

        # ★ 對「答案」二分：答案越大，需要的段數越少（單調）
        lo, hi = max(nums), sum(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if pieces(mid) <= k:
                hi = mid                         # mid 可行，試更小的
            else:
                lo = mid + 1
        return lo'''

S["p410_dp"] = '''class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        P = [0]
        for x in nums:
            P.append(P[-1] + x)
        INF = float("inf")
        # dp[j][i]：前 i 個數切成 j 段時，最大段和的最小值
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0
        for j in range(1, k + 1):
            for i in range(1, n + 1):
                for t in range(j - 1, i):        # 最後一段是 nums[t:i]
                    dp[j][i] = min(dp[j][i], max(dp[j - 1][t], P[i] - P[t]))
        return dp[k][n]'''

_p410 = [S.load(x) for x in ("p410_bs", "p410_dp")]
for nums, k, want in [([7, 2, 5, 10, 8], 2, 18), ([1, 2, 3, 4, 5], 2, 9), ([1, 4, 4], 3, 4)]:
    for sol in _p410:
        assert sol.splitArray(nums, k) == want
for _ in range(1500):
    nums = [random.randint(0, 9) for _ in range(random.randrange(1, 9))]
    k = random.randint(1, len(nums))
    a, b = (sol.splitArray(nums, k) for sol in _p410)
    assert a == b, (nums, k)
print("P410 OK")

emit({
 "num": 410, "slug": "split-array-largest-sum",
 "en": [
   "Given an integer array <code>nums</code> and an integer <code>k</code>, split <code>nums</code> into <code>k</code> non-empty subarrays such that the largest sum of any subarray is <strong>minimized</strong>.",
   "Return <em>the minimized largest sum of the split</em>.",
   "A <strong>subarray</strong> is a contiguous part of the array.",
 ],
 "zh": [
   "給你一個非負整數陣列 <code>nums</code> 和整數 <code>k</code>，把 <code>nums</code> 切成 <code>k</code> 個<strong>連續</strong>、非空的子陣列，使「各段和的最大值」<strong>最小</strong>。",
   "回傳這個最小的最大段和。",
 ],
 "examples": """範例 1
  輸入：nums = [7,2,5,10,8], k = 2
  輸出：18
  說明：[7,2,5] 和 [10,8]，最大段和 18。

範例 2
  輸入：nums = [1,2,3,4,5], k = 2
  輸出：9
  說明：[1,2,3] 和 [4,5]。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 1000",
   "0 ≤ <code>nums[i]</code> ≤ 10⁶",
   "1 ≤ <code>k</code> ≤ min(50, <code>nums.length</code>)",
 ],
 "idea": [
   ("c", """【「最大值最小化」-> 想到對答案二分】
    與其直接求答案，不如問：
    「如果每段和不能超過 limit，最少要切幾段？」

    這個問題用貪心很好回答：
    從左往右裝，裝不下就開新的一段。

【單調性】
    limit 越大 -> 每段能裝越多 -> 需要的段數越少。
    找最小的 limit 使得「需要的段數 <= k」。

【二分範圍】
    下界：max(nums)（最大的那個數自己就是一段）
    上界：sum(nums)（整個陣列一段）

【為什麼「段數 <= k」就夠，不用剛好 k？】
    段數比 k 少的話，可以把某段再切開（非空即可），
    最大段和不會變大。

【DP 做法】
    dp[j][i] = 前 i 個數切成 j 段的最小最大段和
    O(k · n²)，概念直接但比較慢。"""),
 ],
 "approaches": [
   ap("解法一", "動態規劃", [
     ("c", S["p410_dp"]),
   ], "O(k · n²)", "O(k · n)", "", ""),

   ap("解法二", "對答案二分 + 貪心檢查", [
     ("c", S["p410_bs"]),
   ], "O(n log(sum))", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、DP", "O(k·n²)", "O(k·n)"],
    ["二、二分答案", "O(n log S)", "O(1) ✔"]]),
 "edges": [
   "<strong>k = n</strong> → 每個數一段，答案是 max(nums)。",
   "<strong>k = 1</strong> → 答案是 sum(nums)。",
   "<strong>有 0</strong> → 不影響。",
 ],
 "follow": [
   ("h", "「二分答案」模板"),
   ("c", "第 875 題（愛吃香蕉的珂珂）、第 1011 題（在 D 天內送達包裹的能力）、第 1482 題（製作 m 束花所需的最少天數）——都是「給定答案能否達成」可以貪心檢查，而且有單調性。"),
 ],
 "related": [
   "<strong>第 1011 題 在 D 天內送達包裹的能力</strong> —— 幾乎相同",
   "<strong>第 875 題 愛吃香蕉的珂珂</strong>",
   "<strong>第 1231 題 分享巧克力</strong>（付費）—— 最小值最大化",
 ],
 "check": [
   "給定 limit，怎麼算出最少要切幾段？",
   "為什麼可以對答案二分？單調性在哪裡？",
   "二分的上下界是什麼？",
 ],
})


# ==================== 412. Fizz Buzz ====================
S["p412"] = '''class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"                # ★ 15 的倍數兩個都會加上 -> "FizzBuzz"
            res.append(s or str(i))
        return res'''

_p412 = S.load("p412")
out = _p412.fizzBuzz(15)
assert out == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
for n in range(1, 200):
    o = _p412.fizzBuzz(n)
    for i, s in enumerate(o, 1):
        assert s == ("FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i))
print("P412 OK")

emit({
 "num": 412, "slug": "fizz-buzz",
 "en": [
   "Given an integer <code>n</code>, return <em>a string array</em> <code>answer</code> <em>(<strong>1-indexed</strong>) where</em>:",
   ("ul", ["<code>answer[i] == \"FizzBuzz\"</code> if <code>i</code> is divisible by <code>3</code> and <code>5</code>.",
           "<code>answer[i] == \"Fizz\"</code> if <code>i</code> is divisible by <code>3</code>.",
           "<code>answer[i] == \"Buzz\"</code> if <code>i</code> is divisible by <code>5</code>.",
           "<code>answer[i] == i</code> (as a string) if none of the above conditions are true."]),
 ],
 "zh": [
   "給你一個整數 <code>n</code>，回傳字串陣列 <code>answer</code>（從 1 開始）：",
   ("ul", ["<code>i</code> 同時是 3 和 5 的倍數 → <code>\"FizzBuzz\"</code>",
           "只是 3 的倍數 → <code>\"Fizz\"</code>",
           "只是 5 的倍數 → <code>\"Buzz\"</code>",
           "都不是 → <code>i</code> 本身（字串）"]),
 ],
 "examples": """範例
  輸入：n = 15
  輸出：["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【最常見的錯誤：判斷順序】
    if i % 3 == 0: "Fizz"
    elif i % 5 == 0: "Buzz"
    elif i % 15 == 0: "FizzBuzz"   ✘ 永遠到不了（15 已經在第一個條件被抓走）

    必須先判斷 15，或用「字串相加」的寫法。

【字串相加】
    是 3 的倍數就加 "Fizz"，是 5 的倍數就加 "Buzz"，
    兩個都是就自然變成 "FizzBuzz"；
    空字串代表都不是 -> 用數字。
    這個寫法很容易擴充（例如再加「7 的倍數 -> Bazz」）。"""),
 ],
 "approaches": [
   ap("解法", "字串相加", [
     ("c", S["p412"]),
   ], "O(n)", "O(1)", "", "不計輸出", optimal=True),
 ],
 "edges": [
   "<strong>15 的倍數</strong> → 必須是 \"FizzBuzz\"，注意判斷順序。",
   "<strong>n = 1</strong> → <code>[\"1\"]</code>。",
 ],
 "follow": [
   ("h", "為什麼這題有名？"),
   ("c", "2007 年 Imran Ghory 用它篩選面試者，發現很多自稱會寫程式的人寫不出來。它考的不是演算法，而是「能不能正確處理條件的優先順序」。"),
 ],
 "related": [
   "<strong>第 1195 題 交替列印字串</strong> —— 多執行緒版的 FizzBuzz",
 ],
 "check": [
   "為什麼先判斷 3 再判斷 15 會出錯？",
   "字串相加的寫法有什麼好處？",
 ],
})


# ==================== 413. Arithmetic Slices ====================
S["p413"] = '''class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = cur = 0      # cur：以 nums[i] 結尾的等差子陣列個數（長度 >= 3）
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cur += 1     # ★ 之前每一個都能再延長一格，再加上新的長度 3 那一個
            else:
                cur = 0
            total += cur
        return total'''

_p413 = S.load("p413")
for nums, want in [([1, 2, 3, 4], 3), ([1], 0), ([1, 2, 3, 8, 9, 10], 2), ([7, 7, 7, 7], 3)]:
    assert _p413.numberOfArithmeticSlices(nums) == want
for _ in range(2000):
    a = [random.randint(0, 3) for _ in range(random.randrange(1, 10))]
    want = sum(1 for i in range(len(a)) for j in range(i + 2, len(a))
               if len({a[t + 1] - a[t] for t in range(i, j)}) == 1)
    assert _p413.numberOfArithmeticSlices(a) == want
print("P413 OK")

emit({
 "num": 413, "slug": "arithmetic-slices",
 "en": [
   "An integer array is called arithmetic if it consists of <strong>at least three elements</strong> and if the difference between any two consecutive elements is the same.",
   ("ul", ["For example, <code>[1,3,5,7,9]</code>, <code>[7,7,7,7]</code>, and <code>[3,-1,-5,-9]</code> are arithmetic sequences."]),
   "Given an integer array <code>nums</code>, return <em>the number of arithmetic <strong>subarrays</strong> of</em> <code>nums</code>.",
   "A <strong>subarray</strong> is a contiguous subsequence of the array.",
 ],
 "zh": [
   "<strong>等差數列</strong>：至少三個元素，而且相鄰兩數的差都相同。例如 <code>[1,3,5,7,9]</code>、<code>[7,7,7,7]</code>、<code>[3,-1,-5,-9]</code>。",
   "給你一個整數陣列 <code>nums</code>，回傳其中有幾個<strong>子陣列</strong>（連續）是等差數列。",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,4]
  輸出：3
  說明：[1,2,3]、[2,3,4]、[1,2,3,4]

範例 2
  輸入：nums = [1]
  輸出：0""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 5000",
   "−1000 ≤ <code>nums[i]</code> ≤ 1000",
 ],
 "idea": [
   ("c", """【以每個位置「結尾」來數】
    cur[i] = 以 nums[i] 結尾、長度 >= 3 的等差子陣列個數

    如果 nums[i-2], nums[i-1], nums[i] 構成等差：
        所有以 nums[i-1] 結尾的等差子陣列，都能延長一格 -> cur[i-1] 個
        再加上新的 [nums[i-2], nums[i-1], nums[i]] -> 1 個
        cur[i] = cur[i-1] + 1
    否則 cur[i] = 0

    答案 = 所有 cur[i] 的總和。

【範例 [1,2,3,4]】
    i=2：[1,2,3]          cur = 1
    i=3：[2,3,4]、[1,2,3,4] cur = 2
    總和 3 ✔

【數學版】
    一段長度 L 的等差區段，貢獻 (L-1)(L-2)/2 個子陣列。"""),
 ],
 "approaches": [
   ap("解法", "DP：以 i 結尾的個數", [
     ("c", S["p413"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>長度 &lt; 3</strong> → 0。",
   "<strong>全部相同</strong> → 公差 0 也算等差。",
   "<strong>等差被中斷</strong> → cur 歸零重新開始。",
 ],
 "follow": [
   ("h", "子序列版本"),
   ("c", "第 446 題「等差數列劃分 II」：改成子序列（不連續），要用 dp[i][公差] 的雜湊表 DP。"),
 ],
 "related": [
   "<strong>第 446 題 等差數列劃分 II - 子序列</strong>",
   "<strong>第 1027 題 最長等差數列</strong>",
 ],
 "check": [
   "cur[i] 和 cur[i−1] 的關係是什麼？為什麼是 +1？",
   "長度 L 的等差區段包含幾個等差子陣列？",
 ],
})


# ==================== 414. Third Maximum Number ====================
S["p414"] = '''class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None          # 前三大（互不相同）
        for x in nums:
            if x in (first, second, third):    # ★ 重複的值不算
                continue
            if first is None or x > first:
                first, second, third = x, first, second
            elif second is None or x > second:
                second, third = x, second
            elif third is None or x > third:
                third = x
        return first if third is None else third   # 不同的值不足三個 -> 回傳最大'''

S["p414_set"] = '''class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        top = sorted(set(nums), reverse=True)
        return top[2] if len(top) >= 3 else top[0]'''

_p414 = [S.load(x) for x in ("p414", "p414_set")]
for nums, want in [([3, 2, 1], 1), ([1, 2], 2), ([2, 2, 3, 1], 1), ([1, 2, -2 ** 31], -2 ** 31)]:
    for sol in _p414:
        assert sol.thirdMax(nums) == want
for _ in range(3000):
    a = [random.randint(-5, 5) for _ in range(random.randrange(1, 9))]
    assert _p414[0].thirdMax(a) == _p414[1].thirdMax(a), a
print("P414 OK")

emit({
 "num": 414, "slug": "third-maximum-number",
 "en": [
   "Given an integer array <code>nums</code>, return <em>the <strong>third distinct maximum</strong> number in this array. If the third maximum does not exist, return the <strong>maximum</strong> number</em>.",
   "<strong>Follow up:</strong> Can you find an <code>O(n)</code> solution?",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，回傳<strong>第三大的不同數值</strong>；如果不同的數值不足三個，回傳<strong>最大值</strong>。",
   "<strong>進階：</strong>能做到 <code>O(n)</code> 嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [3,2,1]
  輸出：1

範例 2
  輸入：nums = [1,2]
  輸出：2
  說明：不同的值只有兩個，回傳最大值。

範例 3
  輸入：nums = [2,2,3,1]
  輸出：1
  說明：不同的值是 3、2、1。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁴",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【維護前三大（互不相同）】
    first > second > third
    讀到 x：
        已經是三者之一 -> 跳過（「不同的」第三大）
        x > first  -> 全部往下擠一格
        x > second -> second、third 往下擠
        x > third  -> 取代 third

【初始值的陷阱】
    用 -2³¹ 當「還沒有」會出錯：
    [1, 2, -2³¹] 的第三大就是 -2³¹，無法分辨「真的有」還是「還沒有」。
    用 None（或 -∞）當哨兵最安全。"""),
 ],
 "approaches": [
   ap("解法一", "集合 + 排序", [
     ("c", S["p414_set"]),
   ], "O(n log n)", "O(n)", "", ""),

   ap("解法二", "一趟維護前三大", [
     ("c", S["p414"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、排序", "O(n log n)", "O(n)"],
    ["二、前三大", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>重複值</strong> → 只算一次。",
   "<strong>不同的值少於三個</strong> → 回傳最大值。",
   "<strong>值等於 −2³¹</strong> → 不能用它當「不存在」的標記。",
 ],
 "follow": [
   ("h", "推廣到第 k 大"),
   ("c", "第 215 題：大小為 k 的最小堆積，或快速選擇；本題 k = 3 而且要去重。"),
 ],
 "related": [
   "<strong>第 215 題 陣列中的第 K 個最大元素</strong>",
 ],
 "check": [
   "讀到一個比 first 還大的數時，三個變數怎麼更新？",
   "為什麼不能用 −2³¹ 當初始值？",
 ],
})
