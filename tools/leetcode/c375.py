# -*- coding: utf-8 -*-
"""第 375、376、377、378、380、381 題。"""
import random
import itertools
import functools
from collections import defaultdict, Counter
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(375)


# ==================== 375. Guess Number Higher or Lower II ====================
S["p375"] = '''class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp[i][j]：答案在 [i, j] 之間時，保證能猜中所需的最少金額
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for length in range(2, n + 1):
            for i in range(1, n - length + 2):
                j = i + length - 1
                # ★ 先猜 k：付 k 元，然後對方可能把你逼到較貴的那一半（取 max）
                #   我們選讓「最壞情況」最便宜的 k（取 min）
                dp[i][j] = min(k + max(dp[i][k - 1], dp[k + 1][j]) for k in range(i, j))
        return dp[1][n]'''

S["p375_memo"] = '''class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(None)
        def cost(lo: int, hi: int) -> int:
            if lo >= hi:                       # 只剩 0 或 1 個候選：不用付錢
                return 0
            return min(k + max(cost(lo, k - 1), cost(k + 1, hi)) for k in range(lo, hi + 1))
        return cost(1, n)'''

_p375 = [S.load(x) for x in ("p375", "p375_memo")]
for n, want in [(1, 0), (2, 1), (3, 2), (10, 16)]:
    for sol in _p375:
        assert sol.getMoneyAmount(n) == want, (n, sol)
for n in range(1, 60):
    assert _p375[0].getMoneyAmount(n) == _p375[1].getMoneyAmount(n)
print("P375 OK")

emit({
 "num": 375, "slug": "guess-number-higher-or-lower-ii",
 "en": [
   "We are playing the Guessing Game. The game will work as follows:",
   ("ol", ["I pick a number between <code>1</code> and <code>n</code>.",
           "You guess a number.",
           "If you guess the right number, <strong>you win the game</strong>.",
           "If you guess the wrong number, then I will tell you whether the number I picked is <strong>higher or lower</strong>, and you will continue guessing.",
           "Every time you guess a wrong number <code>x</code>, you will pay <code>x</code> dollars. If you run out of money, <strong>you lose the game</strong>."]),
   "Given a particular <code>n</code>, return <em>the minimum amount of money you need to <strong>guarantee a win regardless of what number I pick</strong></em>.",
 ],
 "zh": [
   "猜數字遊戲的付費版：",
   ("ol", ["我從 <code>1</code> 到 <code>n</code> 選一個數字。",
           "你猜一個數字。猜對就贏。",
           "猜錯了，我會告訴你答案比較大還是比較小，你繼續猜。",
           "每猜錯一次 <code>x</code>，你要付 <code>x</code> 元。錢用完就輸了。"]),
   "給你 <code>n</code>，回傳<strong>不管我選哪個數字，你都保證能贏</strong>所需的最少金額。",
 ],
 "examples": """範例 1
  輸入：n = 10
  輸出：16
  說明：最佳策略：先猜 7
    答案 > 7：猜 9（猜錯最多再付 9）-> 總共 7 + 9 = 16
    答案 < 7：猜 3 -> 再猜 5（或 1）-> 最多 7 + 3 + 5 = 15
    最壞情況 16 元。

範例 2
  輸入：n = 1
  輸出：0

範例 3
  輸入：n = 2
  輸出：1
  說明：先猜 1，錯了就付 1 元，答案一定是 2。""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 200",
 ],
 "idea": [
   ("c", """【二分不是最佳策略】
    第 374 題要「次數最少」-> 二分。
    這題要「錢最少」-> 猜大的數字比較貴，
    應該讓貴的猜測出現在「剩下的範圍比較小」的那一邊。

【極小化極大（minimax）】
    你：選一個 k 來猜（想讓成本最小）
    對手：答案永遠讓你落到比較貴的那一邊（最壞情況）

    cost(i, j) = min over k of  [ k + max(cost(i, k-1), cost(k+1, j)) ]
                 你選 k           付 k    對手選較差的那一半

    cost(i, i) = 0（只剩一個，不用猜錯）
    cost(i, i-1) = 0（空範圍）

【區間 DP】
    依區間長度由小到大填表，O(n³)。
    n = 200 時約 1.3×10⁶ 次，很快。

【小優化】
    k 取在右半邊比較有可能是最佳（左邊的數字便宜），
    可以只枚舉 k >= (i+j)/2，但不影響複雜度等級。"""),
 ],
 "approaches": [
   ap("解法一", "記憶化搜尋", [
     ("c", S["p375_memo"]),
   ], "O(n³)", "O(n²)", "", ""),

   ap("解法二", "區間 DP", [
     ("c", S["p375"]),
     "迴圈只枚舉 k 從 i 到 j−1：猜 j 永遠不會比猜 j−1 更好（猜 j−1 的話，錯了答案就一定是 j）。",
   ], "O(n³)", "O(n²)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、記憶化", "O(n³)", "O(n²)"],
    ["二、區間 DP", "O(n³)", "O(n²) ✔"]]),
 "edges": [
   "<strong>n = 1</strong> → 0。",
   "<strong>n = 2</strong> → 1（猜 1）。",
   "<strong>n = 3</strong> → 2（猜 2，不論大小都知道答案）。",
 ],
 "follow": [
   ("h", "minimax 的其他題"),
   ("c", "第 486 題「預測贏家」、第 877 題「石子遊戲」、第 464 題「我能贏嗎」都是雙方輪流做最佳選擇的遊戲，DP 中一方取 max、另一方取 min（或用差值合併成一個 max）。"),
 ],
 "related": [
   "<strong>第 374 題 猜數字大小</strong>",
   "<strong>第 312 題 戳氣球</strong> —— 區間 DP",
   "<strong>第 486 題 預測贏家</strong> —— minimax",
 ],
 "check": [
   "為什麼二分搜尋在這題不是最佳策略？",
   "轉移式中的 min 和 max 分別代表誰的選擇？",
   "dp 表要按照什麼順序填？",
 ],
})


# ==================== 376. Wiggle Subsequence ====================
S["p376"] = '''class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = down = 1          # up：最後一步是「上升」的最長擺動子序列；down 同理
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1          # ★ 接在「最後是下降」的後面
            elif nums[i] < nums[i - 1]:
                down = up + 1
            # 相等：兩者都不變
        return max(up, down)'''

S["p376_greedy"] = '''class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count = 1
        prev_diff = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i - 1]
            # 只數「轉折點」：方向改變時（忽略相等）
            if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
                count += 1
                prev_diff = diff
        return count'''

_p376 = [S.load(x) for x in ("p376", "p376_greedy")]


def _wig_ref(a):
    best = 1
    for r in range(2, len(a) + 1):
        for c in itertools.combinations(a, r):
            d = [y - x for x, y in zip(c, c[1:])]
            if all(x != 0 for x in d) and all((d[i] > 0) != (d[i + 1] > 0) for i in range(len(d) - 1)):
                best = r
    return best


for nums, want in [([1, 7, 4, 9, 2, 5], 6), ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7), ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2), ([0, 0], 1)]:
    for sol in _p376:
        assert sol.wiggleMaxLength(nums) == want
for _ in range(1000):
    a = [random.randint(0, 4) for _ in range(random.randrange(1, 10))]
    want = _wig_ref(a)
    for sol in _p376:
        assert sol.wiggleMaxLength(a) == want, (a, sol)
print("P376 OK")

emit({
 "num": 376, "slug": "wiggle-subsequence",
 "en": [
   "A <strong>wiggle sequence</strong> is a sequence where the differences between successive numbers strictly alternate between positive and negative. "
   "The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.",
   ("ul", ["For example, <code>[1, 7, 4, 9, 2, 5]</code> is a <strong>wiggle sequence</strong> because the differences <code>(6, -3, 5, -7, 3)</code> alternate between positive and negative.",
           "In contrast, <code>[1, 4, 7, 2, 5]</code> and <code>[1, 7, 4, 5, 5]</code> are not wiggle sequences."]),
   "A <strong>subsequence</strong> is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.",
   "Given an integer array <code>nums</code>, return <em>the length of the longest <strong>wiggle subsequence</strong> of</em> <code>nums</code>.",
   "<strong>Follow up:</strong> Could you solve this in <code>O(n)</code> time?",
 ],
 "zh": [
   "<strong>擺動序列</strong>：相鄰兩數的差<strong>嚴格地正負交替</strong>（第一個差可正可負）。只有一個元素、或兩個不相等的元素，也算擺動序列。",
   ("ul", ["例如 <code>[1, 7, 4, 9, 2, 5]</code> 的差是 <code>(6, -3, 5, -7, 3)</code>，是擺動序列。",
           "<code>[1, 4, 7, 2, 5]</code>（前兩個差都是正的）和 <code>[1, 7, 4, 5, 5]</code>（最後的差是 0）都不是。"]),
   "給你一個整數陣列 <code>nums</code>，回傳其中<strong>最長擺動子序列</strong>的長度。",
   "<strong>進階：</strong>能在 <code>O(n)</code> 時間內完成嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [1,7,4,9,2,5]
  輸出：6

範例 2
  輸入：nums = [1,17,5,10,13,15,10,5,16,8]
  輸出：7
  說明：[1,17,10,13,10,16,8] 是其中一個。

範例 3
  輸入：nums = [1,2,3,4,5,6,7,8,9]
  輸出：2""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 1000",
   "0 ≤ <code>nums[i]</code> ≤ 1000",
 ],
 "idea": [
   ("c", """【貪心：數「山峰」和「山谷」】
    把陣列畫成折線圖。
    連續上升的一段，只需要保留最高點（山峰）；
    連續下降的一段，只需要保留最低點（山谷）。
    答案 = 轉折點的個數 + 1（起點）。

    1  17  5  10  13  15  10  5  16  8
       ↑峰 ↓谷      ↑峰      ↓谷 ↑峰 ↓
    10 → 13 → 15 是連續上升，只算 15 這個峰。

【DP 觀點：兩個狀態】
    up   = 目前為止，最後一步是「上升」的最長擺動子序列長度
    down = 最後一步是「下降」的最長長度
    nums[i] > nums[i-1]：up = down + 1
    nums[i] < nums[i-1]：down = up + 1
    相等：都不變

【為什麼 up = down + 1 不需要取 max？】
    up 和 down 都只會增加，而且 down + 1 >= 舊的 up 一定成立
    （可以用歸納法證明 |up - down| <= 1）。

【相等的元素】
    差為 0 不算擺動，直接跳過。"""),
 ],
 "approaches": [
   ap("解法一", "貪心：數轉折點", [
     ("c", S["p376_greedy"]),
     "<code>prev_diff</code> 只在真正轉折時更新；用 <code>&lt;= 0</code>、<code>&gt;= 0</code> 讓開頭的相等元素也能正確處理。",
   ], "O(n)", "O(1)", "", ""),

   ap("解法二", "DP：up / down 兩個狀態", [
     ("c", S["p376"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["O(n²) DP", "O(n²)", "O(n)"],
    ["一、貪心", "O(n)", "O(1)"],
    ["二、up / down", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>只有一個元素</strong> → 1。",
   "<strong>全部相同</strong> → 1。",
   "<strong>單調遞增</strong> → 2。",
   "<strong>開頭有相等的元素</strong>（<code>[0,0,1]</code>）→ 2。",
 ],
 "follow": [
   ("h", "相關題"),
   ("c", "第 978 題「最長湍流子陣列」：子陣列（連續）版本，同樣用 up / down 兩個狀態，但不連續時要重置。"),
 ],
 "related": [
   "<strong>第 978 題 最長湍流子陣列</strong>",
   "<strong>第 300 題 最長遞增子序列</strong>",
 ],
 "check": [
   "為什麼只需要保留山峰和山谷？",
   "up 和 down 的轉移式是什麼？",
   "相等的相鄰元素怎麼處理？",
 ],
})


# ==================== 377. Combination Sum IV ====================
S["p377"] = '''class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target            # dp[x]：總和為 x 的「排列」數；空序列算 1 種
        for x in range(1, target + 1):     # ★ 外層是總和、內層是數字 -> 算排列（順序不同算不同）
            for num in nums:
                if num <= x:
                    dp[x] += dp[x - num]   # 最後一個數是 num
        return dp[target]'''

_p377 = S.load("p377")


def _perm_ref(nums, t):
    @functools.lru_cache(None)
    def f(x):
        if x == 0:
            return 1
        return sum(f(x - v) for v in nums if v <= x)
    return f(t)


for nums, t, want in [([1, 2, 3], 4, 7), ([9], 3, 0)]:
    assert _p377.combinationSum4(nums, t) == want
for _ in range(1000):
    nums = random.sample(range(1, 15), random.randrange(1, 5))
    t = random.randrange(1, 40)
    assert _p377.combinationSum4(nums, t) == _perm_ref(tuple(nums), t)
print("P377 OK")

emit({
 "num": 377, "slug": "combination-sum-iv",
 "en": [
   "Given an array of <strong>distinct</strong> integers <code>nums</code> and a target integer <code>target</code>, return <em>the number of possible combinations that add up to</em> <code>target</code>.",
   "The test cases are generated so that the answer can fit in a <strong>32-bit</strong> integer.",
   "<strong>Follow up:</strong> What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?",
 ],
 "zh": [
   "給你一個由<strong>互不相同</strong>的正整數組成的陣列 <code>nums</code> 和目標 <code>target</code>，回傳總和為 <code>target</code> 的組合數。",
   "注意：<strong>順序不同的序列視為不同的組合</strong>（所以其實是「排列」數）。每個數字可以重複使用。",
   "<strong>進階：</strong>如果允許負數會怎樣？需要加上什麼限制？",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3], target = 4
  輸出：7
  說明：
    (1,1,1,1) (1,1,2) (1,2,1) (2,1,1) (1,3) (3,1) (2,2)

範例 2
  輸入：nums = [9], target = 3
  輸出：0""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 200",
   "1 ≤ <code>nums[i]</code> ≤ 1000",
   "<code>nums</code> 中的元素互不相同",
   "1 ≤ <code>target</code> ≤ 1000",
 ],
 "idea": [
   ("c", """【題目說「組合」，其實要算「排列」】
    (1,1,2)、(1,2,1)、(2,1,1) 算三種。

【DP：依「最後一個數」分類】
    dp[x] = 總和為 x 的序列數
    最後一個數是 num -> 前面是總和 x - num 的任意序列
    dp[x] = Σ dp[x - num]
    dp[0] = 1（空序列）

【迴圈順序決定是排列還是組合】
    外層 target、內層 nums -> 排列（本題）
        每個總和 x 都考慮「所有數字都可以放最後」
    外層 nums、內層 target -> 組合（第 518 題）
        數字按固定順序加入，(1,2) 和 (2,1) 只會被數一次

【允許負數？】
    [1, -1] 湊 0：可以 1,-1,1,-1,... 無限長 -> 無限多種 ✘
    必須限制序列的長度。"""),
   ("t", ["x", "0", "1", "2", "3", "4"],
    [["dp[x]", "1", "1", "2", "4", "7"],
     ["計算", "", "dp[0]", "dp[1]+dp[0]", "dp[2]+dp[1]+dp[0]", "dp[3]+dp[2]+dp[1]"]]),
 ],
 "approaches": [
   ap("解法", "完全背包（排列數）", [
     ("c", S["p377"]),
     "中間值可能超過 32 位元（題目只保證最終答案在範圍內）；Python 沒有溢位問題，其他語言要用 unsigned 或 long 並注意。",
   ], "O(target · n)", "O(target)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>沒有數字 ≤ target</strong> → 0。",
   "<strong>target 剛好是某個數字</strong> → 至少 1 種。",
   "<strong>中間值溢位</strong>（其他語言）→ 本題已知的陷阱。",
 ],
 "follow": [
   ("h", "背包問題的迴圈順序整理"),
   ("c", """0/1 背包（每個只能用一次）：外層物品，內層容量「由大到小」。
完全背包 + 組合數：外層物品，內層容量「由小到大」（第 518 題）。
完全背包 + 排列數：外層容量，內層物品（本題、第 70 題爬樓梯）。"""),
 ],
 "related": [
   "<strong>第 518 題 零錢兌換 II</strong> —— 組合數",
   "<strong>第 70 題 爬樓梯</strong> —— nums = [1, 2] 的特例",
   "<strong>第 39 題 組合總和</strong> —— 列出所有組合",
 ],
 "check": [
   "這題算的是組合數還是排列數？",
   "兩層迴圈的順序交換會發生什麼？",
   "允許負數時為什麼要限制長度？",
 ],
})


# ==================== 378. Kth Smallest Element in a Sorted Matrix ====================
S["p378_bs"] = '''class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def count_le(x: int) -> int:           # 矩陣中 <= x 的個數：從左下角走階梯
            cnt, r, c = 0, n - 1, 0
            while r >= 0 and c < n:
                if matrix[r][c] <= x:
                    cnt += r + 1                # 這一欄上面的都 <= x
                    c += 1
                else:
                    r -= 1
            return cnt

        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo < hi:                          # ★ 對「值」二分：找最小的 x 使 count_le(x) >= k
            mid = (lo + hi) // 2
            if count_le(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo'''

S["p378_heap"] = '''class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(matrix[i][0], i, 0) for i in range(min(n, k))]   # 每一列的第一個
        heapq.heapify(heap)
        for _ in range(k - 1):                  # 彈出 k-1 次
            _, i, j = heapq.heappop(heap)
            if j + 1 < n:
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return heap[0][0]'''

_p378 = [S.load(x) for x in ("p378_bs", "p378_heap")]
for M, k, want in [([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13), ([[-5]], 1, -5)]:
    for sol in _p378:
        assert sol.kthSmallest(M, k) == want
for _ in range(1000):
    n = random.randrange(1, 7)
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            M[i][j] = max(M[i - 1][j] if i else -10, M[i][j - 1] if j else -10) + random.randrange(0, 4)
    flat = sorted(x for r in M for x in r)
    k = random.randrange(1, n * n + 1)
    for sol in _p378:
        assert sol.kthSmallest(M, k) == flat[k - 1]
print("P378 OK")

emit({
 "num": 378, "slug": "kth-smallest-element-in-a-sorted-matrix",
 "en": [
   "Given an <code>n x n</code> <code>matrix</code> where each of the rows and columns is sorted in ascending order, return <em>the</em> <code>k<sup>th</sup></code> <em>smallest element in the matrix</em>.",
   "Note that it is the <code>k<sup>th</sup></code> smallest element <strong>in the sorted order</strong>, not the <code>k<sup>th</sup></code> <strong>distinct</strong> element.",
   "You must find a solution with a memory complexity better than <code>O(n<sup>2</sup>)</code>.",
 ],
 "zh": [
   "給你一個 <code>n x n</code> 的矩陣，每一列、每一欄都是遞增排序的，回傳矩陣中第 <code>k</code> 小的元素。",
   "注意是排序後的第 <code>k</code> 個（重複的值要分別算），不是第 <code>k</code> 個<strong>不同</strong>的值。",
   "空間複雜度必須優於 <code>O(n²)</code>。",
 ],
 "examples": """範例 1
  輸入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
  輸出：13
  說明：排序後 [1,5,9,10,11,12,13,13,15]，第 8 個是 13。

範例 2
  輸入：matrix = [[-5]], k = 1
  輸出：-5""",
 "constraints": [
   "<code>n == matrix.length == matrix[i].length</code>",
   "1 ≤ <code>n</code> ≤ 300",
   "−10⁹ ≤ <code>matrix[i][j]</code> ≤ 10⁹",
   "每一列、每一欄都遞增",
   "1 ≤ <code>k</code> ≤ n²",
 ],
 "idea": [
   ("c", """【方法一：多路合併（第 373 題的套路）】
    每一列是一條有序串列，
    最小堆積放每一列目前的最小值，彈 k 次。
    O(k log n)。

【方法二：對「值」二分】
    答案一定在 [左上角, 右下角] 之間。
    猜一個值 x，數一數矩陣中 <= x 的有幾個：
        >= k -> 答案 <= x
        <  k -> 答案 > x
    找最小的 x 使 count(x) >= k。

    count 怎麼算？從左下角走階梯（第 240 題的走法）：
        matrix[r][c] <= x -> 這一欄第 0..r 列都 <= x，加 r+1，往右
        否則 -> 往上
    O(n)。

    總共 O(n log(max - min))，空間 O(1)。

【為什麼二分出來的 x 一定在矩陣裡？】
    找的是「最小的」滿足 count(x) >= k 的 x。
    如果 x 不在矩陣裡，那 x - 1 的 count 一樣，也滿足 -> 矛盾。"""),
 ],
 "approaches": [
   ap("解法一", "最小堆積多路合併", [
     ("c", S["p378_heap"]),
   ], "O(k log n)", "O(n)", "", ""),

   ap("解法二", "對值二分 + 階梯計數", [
     ("c", S["p378_bs"]),
   ], "O(n log(max − min))", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["全部排序", "O(n² log n)", "O(n²)"],
    ["一、堆積", "O(k log n)", "O(n)"],
    ["二、值二分", "O(n log V)", "O(1) ✔"]]),
 "edges": [
   "<strong>重複值</strong> → 要分別算（範例 1 的 13）。",
   "<strong>負數</strong> → 二分下界是左上角，可以是負數；<code>(lo + hi) // 2</code> 在 Python 向下取整，照樣收斂。",
   "<strong>k = 1 或 n²</strong> → 左上角或右下角。",
 ],
 "follow": [
   ("h", "對答案二分"),
   ("c", "「第 k 小」的問題，如果「數出 ≤ x 的個數」很容易，就可以對答案二分。第 668 題（乘法表中第 k 小）、第 719 題（第 k 小的數對距離）、第 786 題都是這個套路。"),
 ],
 "related": [
   "<strong>第 240 題 搜尋二維矩陣 II</strong> —— 階梯走法",
   "<strong>第 373 題 查找和最小的 K 對數字</strong>",
   "<strong>第 668 題 乘法表中第 k 小的數</strong>",
 ],
 "check": [
   "怎麼在 O(n) 內數出矩陣中 ≤ x 的個數？",
   "二分搜尋的條件是什麼？",
   "為什麼二分得到的值一定在矩陣裡？",
 ],
})


# ==================== 380. Insert Delete GetRandom O(1) ====================
S["p380"] = '''class RandomizedSet:
    def __init__(self):
        self.vals = []              # 存值：random.choice 需要可以用索引存取
        self.pos = {}               # 值 -> 它在 vals 中的索引

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        i = self.pos[val]
        last = self.vals[-1]
        # ★ 把最後一個元素搬到要刪除的位置，再刪掉尾巴 —— O(1)
        self.vals[i] = last
        self.pos[last] = i
        self.vals.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)'''

_cls = S.loadns("p380")["RandomizedSet"]
for _ in range(300):
    rs, ref = _cls(), set()
    for _ in range(60):
        r, v = random.random(), random.randrange(10)
        if r < 0.4:
            assert rs.insert(v) == (v not in ref); ref.add(v)
        elif r < 0.75:
            assert rs.remove(v) == (v in ref); ref.discard(v)
        elif ref:
            assert rs.getRandom() in ref
        assert sorted(rs.vals) == sorted(ref)
rs = _cls()
for v in range(4):
    rs.insert(v)
cnt = Counter(rs.getRandom() for _ in range(40000))
assert all(9000 < cnt[v] < 11000 for v in range(4))
print("P380 OK")

_P380_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">remove(20)：把最後一個元素 40 搬到 20 的位置，再刪掉尾巴</text>
            <g font-size="13" text-anchor="middle">
              <text x="40" y="62" fill="var(--text-muted)" text-anchor="start">vals</text>
              <rect x="90" y="44" width="50" height="28" fill="none" stroke="var(--border)"/><text x="115" y="63" fill="var(--text)">10</text>
              <rect x="140" y="44" width="50" height="28" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="165" y="63" fill="#ff8a65">20</text>
              <rect x="190" y="44" width="50" height="28" fill="none" stroke="var(--border)"/><text x="215" y="63" fill="var(--text)">30</text>
              <rect x="240" y="44" width="50" height="28" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="265" y="63" fill="var(--gold)">40</text>
              <text x="40" y="142" fill="var(--text-muted)" text-anchor="start">vals</text>
              <rect x="90" y="124" width="50" height="28" fill="none" stroke="var(--border)"/><text x="115" y="143" fill="var(--text)">10</text>
              <rect x="140" y="124" width="50" height="28" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="165" y="143" fill="var(--gold)">40</text>
              <rect x="190" y="124" width="50" height="28" fill="none" stroke="var(--border)"/><text x="215" y="143" fill="var(--text)">30</text>
              <rect x="240" y="124" width="50" height="28" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/>
            </g>
            <path d="M265 76 C 250 100, 180 100, 168 120" fill="none" stroke="var(--gold)"/>
            <polygon points="168,122 164,112 173,114" fill="var(--gold)"/>
            <text x="320" y="62" fill="var(--text-muted)" font-size="12">pos = {10:0, 20:1, 30:2, 40:3}</text>
            <text x="320" y="142" fill="var(--text-muted)" font-size="12">pos = {10:0, 40:1, 30:2}</text>
            <text x="20" y="190" fill="var(--text)" font-size="12">從陣列中間刪除是 O(n)（要搬後面的元素）；但刪除「尾巴」是 O(1)。</text>
            <text x="20" y="212" fill="var(--gold)" font-size="12">★ 順序不重要，所以先和尾巴交換，再刪尾巴。記得更新被搬動元素在 pos 裡的索引。</text>'''

emit({
 "num": 380, "slug": "insert-delete-getrandom-o1",
 "en": [
   "Implement the <code>RandomizedSet</code> class:",
   ("ul", ["<code>RandomizedSet()</code> Initializes the <code>RandomizedSet</code> object.",
           "<code>bool insert(int val)</code> Inserts an item <code>val</code> into the set if not present. Returns <code>true</code> if the item was not present, <code>false</code> otherwise.",
           "<code>bool remove(int val)</code> Removes an item <code>val</code> from the set if present. Returns <code>true</code> if the item was present, <code>false</code> otherwise.",
           "<code>int getRandom()</code> Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the <strong>same probability</strong> of being returned."]),
   "You must implement the functions of the class such that each function works in <strong>average</strong> <code>O(1)</code> time complexity.",
 ],
 "zh": [
   "實作 <code>RandomizedSet</code>：",
   ("ul", ["<code>insert(val)</code>：val 不存在時加入並回傳 true，否則回傳 false。",
           "<code>remove(val)</code>：val 存在時刪除並回傳 true，否則回傳 false。",
           "<code>getRandom()</code>：<strong>等機率</strong>回傳集合中的一個元素（呼叫時保證非空）。"]),
   "每個操作的<strong>平均</strong>時間都必須是 <code>O(1)</code>。",
 ],
 "examples": """範例
  insert(1)   -> true
  remove(2)   -> false
  insert(2)   -> true
  getRandom() -> 1 或 2（機率各半）
  remove(1)   -> true
  insert(2)   -> false
  getRandom() -> 2""",
 "constraints": [
   "−2³¹ ≤ <code>val</code> ≤ 2³¹ − 1",
   "最多呼叫 2 × 10⁵ 次",
   "呼叫 <code>getRandom</code> 時至少有一個元素",
 ],
 "idea": [
   ("fig", _P380_FIG, "0 0 640 226"),
   ("c", """【單獨用一種資料結構都不夠】
    雜湊集合：insert、remove O(1)，但 getRandom 不能用索引隨機取 ✘
    陣列：getRandom O(1)（隨機索引），但 remove 要先找位置 O(n)、刪中間又要搬移 ✘

【陣列 + 雜湊表】
    vals：存所有值（給 getRandom 用）
    pos ：值 -> 它在 vals 裡的索引（給 remove 找位置用）

【O(1) 刪除的技巧】
    集合沒有順序 ->
    把要刪的元素和陣列最後一個交換，然後 pop 尾巴。
    別忘了更新「被搬過來的那個元素」在 pos 裡的索引。

【邊界：刪除的剛好是最後一個】
    last == val，自己和自己交換，
    先更新 pos[last] = i 再 del pos[val] —— 順序很重要，
    否則會把剛刪掉的鍵又加回去 ✘"""),
 ],
 "approaches": [
   ap("解法", "陣列 + 雜湊表（交換到尾巴再刪）", [
     ("c", S["p380"]),
   ], "每個操作平均 O(1)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>刪除最後一個元素</strong> → 和自己交換；要先更新 pos 再刪鍵。",
   "<strong>重複插入</strong> → 回傳 false。",
   "<strong>刪除不存在的值</strong> → 回傳 false。",
 ],
 "follow": [
   ("h", "允許重複值？"),
   ("c", "第 381 題：pos 改成「值 → 索引的集合」，其餘技巧相同。"),
 ],
 "related": [
   "<strong>第 381 題 O(1) 時間插入、刪除和獲取隨機元素 - 允許重複</strong>",
   "<strong>第 146 題 LRU 快取</strong> —— 另一個「兩種資料結構組合」的設計題",
   "<strong>第 710 題 黑名單中的隨機數</strong>",
 ],
 "check": [
   "為什麼需要陣列和雜湊表兩種結構？",
   "怎麼在 O(1) 內從陣列中刪除一個元素？",
   "刪除最後一個元素時要注意什麼？",
 ],
})


# ==================== 381. Insert Delete GetRandom O(1) - Duplicates allowed ====================
S["p381"] = '''class RandomizedCollection:
    def __init__(self):
        self.vals = []
        self.pos = collections.defaultdict(set)   # ★ 值 -> 所有出現位置的集合

    def insert(self, val: int) -> bool:
        self.pos[val].add(len(self.vals))
        self.vals.append(val)
        return len(self.pos[val]) == 1            # 之前沒有才回傳 true

    def remove(self, val: int) -> bool:
        if not self.pos[val]:
            return False
        i = self.pos[val].pop()                   # 任選 val 的一個位置
        last = self.vals[-1]
        self.vals[i] = last                       # 最後一個搬過來
        self.pos[last].add(i)
        self.pos[last].discard(len(self.vals) - 1)   # ★ 先 add 再 discard：i 可能就是最後一個
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)           # 重複的值自然有較高機率'''

_cls = S.loadns("p381")["RandomizedCollection"]
for _ in range(300):
    rc, ref = _cls(), Counter()
    for _ in range(60):
        r, v = random.random(), random.randrange(5)
        if r < 0.45:
            assert rc.insert(v) == (ref[v] == 0); ref[v] += 1
        elif r < 0.8:
            assert rc.remove(v) == (ref[v] > 0)
            if ref[v]:
                ref[v] -= 1
        elif sum(ref.values()):
            assert ref[rc.getRandom()] > 0
        assert Counter(rc.vals) == +ref
        for val, idxs in rc.pos.items():
            assert all(rc.vals[i] == val for i in idxs) and len(idxs) == ref[val]
rc = _cls()
for v in (1, 1, 2):
    rc.insert(v)
cnt = Counter(rc.getRandom() for _ in range(30000))
assert 19000 < cnt[1] < 21000
print("P381 OK")

emit({
 "num": 381, "slug": "insert-delete-getrandom-o1-duplicates-allowed",
 "en": [
   "<code>RandomizedCollection</code> is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.",
   ("ul", ["<code>bool insert(int val)</code> Inserts an item <code>val</code> into the multiset, even if the item is already present. Returns <code>true</code> if the item is not present, <code>false</code> otherwise.",
           "<code>bool remove(int val)</code> Removes an item <code>val</code> from the multiset if present. Returns <code>true</code> if the item is present, <code>false</code> otherwise. Note that if <code>val</code> has multiple occurrences in the multiset, we only remove one of them.",
           "<code>int getRandom()</code> Returns a random element from the current multiset of elements. The probability of each element being returned is <strong>linearly related</strong> to the number of the same values the multiset contains."]),
   "You must implement the functions of the class such that each function works on <strong>average</strong> <code>O(1)</code> time complexity.",
 ],
 "zh": [
   "和第 380 題相同，但允許<strong>重複</strong>的值（多重集合）：",
   ("ul", ["<code>insert(val)</code>：一定加入；如果之前不存在回傳 true，否則回傳 false。",
           "<code>remove(val)</code>：存在的話刪除<strong>其中一個</strong>並回傳 true。",
           "<code>getRandom()</code>：隨機回傳一個元素，機率和它的<strong>出現次數成正比</strong>。"]),
   "每個操作平均 <code>O(1)</code>。",
 ],
 "examples": """範例
  insert(1)   -> true
  insert(1)   -> false
  insert(2)   -> true
  getRandom() -> 1 的機率 2/3，2 的機率 1/3
  remove(1)   -> true
  getRandom() -> 1 或 2，各 1/2""",
 "constraints": [
   "−2³¹ ≤ <code>val</code> ≤ 2³¹ − 1",
   "最多呼叫 2 × 10⁵ 次",
   "呼叫 <code>getRandom</code> 時至少有一個元素",
 ],
 "idea": [
   ("c", """【第 380 題的推廣】
    pos 從「值 -> 一個索引」變成「值 -> 索引的集合」。

【remove(val)】
    1. 從 pos[val] 任取一個索引 i
    2. 把最後一個元素 last 搬到 i
    3. 更新 pos[last]：加入 i、移除原本的最後位置
    4. pop 尾巴

【陷阱：i 就是最後一個位置】
    last == val 且 i == len - 1：
        如果先 discard(len-1) 再 add(i)，會把 i 加回去 ✘
        先 add(i) 再 discard(len-1)：兩個是同一個數，最後被移除 ✔

【getRandom 自動符合機率要求】
    陣列中重複的值就佔多個位置，
    random.choice 均勻選索引 -> 機率和出現次數成正比。"""),
 ],
 "approaches": [
   ap("解法", "陣列 + 值到索引集合的雜湊表", [
     ("c", S["p381"]),
   ], "每個操作平均 O(1)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>刪除的剛好是最後一個位置</strong> → add 與 discard 的順序很重要。",
   "<strong>刪光某個值</strong> → pos[val] 變成空集合，之後 insert 要回傳 true。",
   "<strong>重複值的機率</strong> → 陣列中佔幾格就有幾倍機率。",
 ],
 "follow": [
   ("h", "為什麼用集合而不是串列存索引？"),
   ("c", "remove 時要從 pos[last] 刪掉「原本的最後位置」這個特定索引——串列刪特定值是 O(k)，集合是 O(1)。"),
 ],
 "related": [
   "<strong>第 380 題 O(1) 時間插入、刪除和獲取隨機元素</strong>",
   "<strong>第 398 題 隨機數索引</strong>",
 ],
 "check": [
   "pos 的結構和第 380 題有什麼不同？",
   "刪除時 add 和 discard 的順序為什麼重要？",
   "getRandom 為什麼自然符合「機率和出現次數成正比」？",
 ],
})
