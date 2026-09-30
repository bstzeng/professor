# -*- coding: utf-8 -*-
"""第 219–224 題。"""
import random
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(219)


# ==================== 219. Contains Duplicate II ====================
S["p219_last"] = '''class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}                               # 值 -> 最近一次出現的索引
        for i, x in enumerate(nums):
            if x in last and i - last[x] <= k:  # ★ 只要和「最近一次」比就夠了
                return True
            last[x] = i
        return False'''

S["p219_window"] = '''class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()                          # 最近 k 個元素
        for i, x in enumerate(nums):
            if x in window:
                return True
            window.add(x)
            if len(window) > k:                 # 視窗超過 k 個：移除最舊的
                window.remove(nums[i - k])
        return False'''

S["p219_brute"] = '''class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if nums[i] == nums[j]:
                    return True
        return False'''

_p219 = [S.load(x) for x in ("p219_last", "p219_window", "p219_brute")]
for nums, k, want in [([1, 2, 3, 1], 3, True), ([1, 0, 1, 1], 1, True), ([1, 2, 3, 1, 2, 3], 2, False),
                      ([1], 0, False), ([1, 1], 0, False), ([99, 99], 2, True)]:
    for sol in _p219:
        assert sol.containsNearbyDuplicate(nums, k) == want, ("P219", nums, k, sol)
for _ in range(4000):
    nums = [random.randint(0, 5) for _ in range(random.randrange(1, 14))]
    k = random.randrange(0, 6)
    want = _p219[2].containsNearbyDuplicate(nums, k)
    for sol in _p219[:2]:
        assert sol.containsNearbyDuplicate(nums, k) == want, ("P219 rand", nums, k, sol)
print("P219 OK")

emit({
 "num": 219, "slug": "contains-duplicate-ii",
 "en": [
   "Given an integer array <code>nums</code> and an integer <code>k</code>, return <code>true</code> if there exist two "
   "<strong>different</strong> indices <code>i</code> and <code>j</code> such that <code>nums[i] == nums[j]</code> and "
   "<code>abs(i - j) &lt;= k</code>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code> 和整數 <code>k</code>。如果存在兩個<strong>不同</strong>的索引 <code>i</code>、<code>j</code>，"
   "使得 <code>nums[i] == nums[j]</code> 而且 <code>abs(i - j) &lt;= k</code>，回傳 <code>true</code>。",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,1], k = 3
  輸出：true
  說明：索引 0 和 3 的值都是 1，距離 3 ≤ 3。

範例 2
  輸入：nums = [1,0,1,1], k = 1
  輸出：true

範例 3
  輸入：nums = [1,2,3,1,2,3], k = 2
  輸出：false
  說明：相同值之間的距離都是 3。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
   "0 ≤ <code>k</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【第 217 題 + 距離限制】

【想法一：只記每個值「最近一次」出現的位置】
    走到索引 i、值 x 時，
    要找的是「之前某個 x 的位置 j，使 i - j <= k」。
    距離最小的 j，一定是【最近一次】出現的那個。
    所以只要記住最近一次就夠了 ✔

【想法二：維護一個長度最多 k 的滑動視窗】
    視窗裡只放「最近 k 個元素」。
    新元素如果已經在視窗裡 -> 距離一定 <= k ✔
    視窗超過 k 個 -> 移除最舊的那個（索引 i - k）。

【k = 0 的情況】
    兩個不同的索引距離至少是 1，一定是 false。
    想法二中，視窗大小為 0：每次加入後立刻移除 ✔"""),
 ],
 "approaches": [
   ap("解法一", "雜湊表記最近一次的位置", [
     ("c", S["p219_last"]),
   ], "O(n)", "O(n)", "", "不同值的個數", optimal=True),

   ap("解法二", "大小為 k 的滑動視窗集合", [
     ("c", S["p219_window"]),
     ("c", """【為什麼移除 nums[i - k]？】
    加入 nums[i] 之後，視窗裡是 nums[i-k .. i]，共 k+1 個。
    最舊的 nums[i-k] 和之後的元素距離會超過 k，移除它。

【視窗裡不會有重複值嗎？】
    不會 —— 一旦要加入重複的值，就已經回傳 true 了。
    所以 len(window) 就是元素個數。"""),
   ], "O(n)", "O(min(n, k))", "", "視窗最多 k 個"),

   ap("解法三", "暴力（只往後看 k 個）", [
     ("c", S["p219_brute"]),
     "O(n·k)，n、k 都是 10⁵ 時超時。",
   ], "O(n·k)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、最近位置", "O(n)", "O(n)", "最簡潔 ✔"],
    ["二、滑動視窗", "O(n)", "O(min(n,k))", "k 小時省空間"],
    ["三、暴力", "O(n·k)", "O(1)", "超時"]]),
 "edges": [
   "<strong><code>k = 0</code></strong> → 一定是 <code>false</code>。",
   "<strong><code>k ≥ n</code></strong> → 退化成第 217 題。",
   "<strong>同一個值出現很多次</strong> → 只需要和最近一次比。",
 ],
 "follow": [
   ("h", "追問：如果值不需要相等，只要相差不超過 t？"),
   ("c", "這是第 220 題：滑動視窗裡要能查「有沒有落在 [x−t, x+t] 的值」——用分桶或有序結構。"),
 ],
 "related": [
   "<strong>第 217 題 存在重複元素</strong>",
   "<strong>第 220 題 存在重複元素 III</strong>",
   "<strong>第 643 題 子陣列最大平均數 I</strong> —— 固定大小的滑動視窗",
 ],
 "check": [
   "為什麼只需要和「最近一次」出現的位置比較？",
   "滑動視窗解法中，為什麼移除的是 <code>nums[i - k]</code>？",
   "<code>k = 0</code> 時答案是什麼？",
 ],
})


# ==================== 220. Contains Duplicate III ====================
S["p220_bucket"] = '''class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        w = valueDiff + 1                    # ★ 桶寬 t+1：同一桶內任兩數相差 <= t
        buckets = {}                         # 桶編號 -> 桶內唯一的值
        for i, x in enumerate(nums):
            b = x // w                       # Python 的 // 向下取整，負數也正確
            if b in buckets:
                return True
            if b - 1 in buckets and x - buckets[b - 1] <= valueDiff:
                return True
            if b + 1 in buckets and buckets[b + 1] - x <= valueDiff:
                return True
            buckets[b] = x
            if i >= indexDiff:               # 維持視窗大小：移除太舊的
                del buckets[nums[i - indexDiff] // w]
        return False'''

S["p220_sorted"] = '''class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        window = []                          # 視窗內的值，保持排序
        for i, x in enumerate(nums):
            j = bisect.bisect_left(window, x - valueDiff)   # 第一個 >= x - t 的值
            if j < len(window) and window[j] <= x + valueDiff:
                return True
            bisect.insort(window, x)
            if i >= indexDiff:
                window.pop(bisect.bisect_left(window, nums[i - indexDiff]))
        return False'''

S["p220_brute"] = '''class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, min(i + indexDiff + 1, len(nums))):
                if abs(nums[i] - nums[j]) <= valueDiff:
                    return True
        return False'''

_p220 = [S.load(x) for x in ("p220_bucket", "p220_sorted", "p220_brute")]
for nums, a, b, want in [([1, 2, 3, 1], 3, 0, True), ([1, 5, 9, 1, 5, 9], 2, 3, False),
                         ([-3, 3], 2, 4, False), ([-3, 3], 2, 6, True), ([1, 2], 1, 0, False), ([4, 1, 6, 3], 1, 1, False)]:
    for sol in _p220:
        assert sol.containsNearbyAlmostDuplicate(nums, a, b) == want, ("P220", nums, a, b, sol)
for _ in range(5000):
    n = random.randrange(2, 14)
    nums = [random.randint(-15, 15) for _ in range(n)]
    a = random.randrange(1, n + 1)
    b = random.randrange(0, 6)
    want = _p220[2].containsNearbyAlmostDuplicate(nums, a, b)
    for sol in _p220[:2]:
        assert sol.containsNearbyAlmostDuplicate(nums, a, b) == want, ("P220 rand", nums, a, b, sol)
print("P220 OK")

_P220_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">分桶：valueDiff = t = 3，桶寬 w = t + 1 = 4</text>
            <line x1="40" y1="90" x2="600" y2="90" stroke="var(--text-muted)"/>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="60" y="108">-4</text><text x="140" y="108">0</text><text x="220" y="108">4</text>
              <text x="300" y="108">8</text><text x="380" y="108">12</text><text x="460" y="108">16</text><text x="540" y="108">20</text>
            </g>
            <g stroke="var(--border)"><line x1="60" y1="50" x2="60" y2="94"/><line x1="140" y1="50" x2="140" y2="94"/>
              <line x1="220" y1="50" x2="220" y2="94"/><line x1="300" y1="50" x2="300" y2="94"/><line x1="380" y1="50" x2="380" y2="94"/>
              <line x1="460" y1="50" x2="460" y2="94"/><line x1="540" y1="50" x2="540" y2="94"/></g>
            <g font-size="12" text-anchor="middle" fill="var(--text)">
              <text x="100" y="60">桶 -1</text><text x="180" y="60">桶 0</text><text x="260" y="60">桶 1</text>
              <text x="340" y="60">桶 2</text><text x="420" y="60">桶 3</text><text x="500" y="60">桶 4</text>
            </g>
            <circle cx="320" cy="82" r="5" fill="var(--accent)"/><text x="320" y="130" text-anchor="middle" fill="var(--accent)" font-size="12">9</text>
            <circle cx="380" cy="82" r="5" fill="#ff8a65"/><text x="380" y="130" text-anchor="middle" fill="#ff8a65" font-size="12">12</text>
            <text x="20" y="162" fill="var(--text)" font-size="12">① 同一個桶：兩數相差一定 ≤ 3 → 直接成立（所以每個桶最多只會放一個數）。</text>
            <text x="20" y="186" fill="var(--text)" font-size="12">② 相鄰的桶：有可能 ≤ 3（例如 9 在桶 2、12 在桶 3，相差 3），要實際相減檢查。</text>
            <text x="20" y="210" fill="var(--text)" font-size="12">③ 隔兩個以上的桶：相差一定 &gt; 3 → 不用看。</text>
            <text x="20" y="236" fill="var(--gold)" font-size="12">★ 每個新數字只要看 3 個桶，O(1)；視窗外的數字從桶裡刪掉。</text>'''

emit({
 "num": 220, "slug": "contains-duplicate-iii",
 "en": [
   "You are given an integer array <code>nums</code> and two integers <code>indexDiff</code> and <code>valueDiff</code>.",
   "Return <code>true</code> if there is a pair of indices <code>(i, j)</code> with <code>i != j</code>, "
   "<code>abs(i - j) &lt;= indexDiff</code> and <code>abs(nums[i] - nums[j]) &lt;= valueDiff</code>. Otherwise return <code>false</code>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，以及兩個整數 <code>indexDiff</code>、<code>valueDiff</code>。",
   "如果存在一對索引 <code>(i, j)</code>，滿足 <code>i != j</code>、<code>abs(i - j) &lt;= indexDiff</code>、"
   "而且 <code>abs(nums[i] - nums[j]) &lt;= valueDiff</code>，回傳 <code>true</code>；否則回傳 <code>false</code>。",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
  輸出：true
  說明：(0, 3)：距離 3，值相差 0。

範例 2
  輸入：nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
  輸出：false""",
 "constraints": [
   "2 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
   "1 ≤ <code>indexDiff</code> ≤ <code>nums.length</code>",
   "0 ≤ <code>valueDiff</code> ≤ 10⁹",
 ],
 "idea": [
   ("fig", _P220_FIG, "0 0 640 250"),
   ("c", """【第 219 題的滑動視窗，但查詢條件變了】
    視窗（最近 indexDiff 個元素）裡，
    有沒有某個值 y 落在 [x - t, x + t]？

【方法一：有序結構】
    視窗內的值保持排序，二分找「第一個 >= x - t 的值」，
    再看它是否 <= x + t。
    需要能在 O(log k) 插入和刪除的有序集合。
    Python 標準函式庫沒有平衡樹，用 list + insort 的插入是 O(k)。

【方法二：分桶】
    把數線切成寬度 w = t + 1 的桶：
        桶編號 = x // w
    - 同一桶內任兩數相差 <= t ✔
    - 所以每個桶在視窗裡最多只會有一個數
      （有第二個的話早就回傳 true 了）
    - 相差 <= t 的兩個數，只可能在同一桶或相鄰桶
    每個新數字只看 3 個桶 -> O(1) ✔

【負數】
    Python 的 // 是向下取整：-1 // 4 = -1、-4 // 4 = -1、-5 // 4 = -2 ✔
    其他語言（C++/Java 向零取整）要自己處理，
    否則 -3 和 3 會被放進同一個桶 0 ✘

【為什麼桶寬是 t + 1 而不是 t？】
    同一桶內最大相差 = 桶寬 − 1，要讓它剛好等於 t -> 桶寬 t + 1。
    另外 t = 0 時，桶寬 t 會除以零 ✘"""),
 ],
 "approaches": [
   ap("解法一", "暴力", [
     ("c", S["p220_brute"]),
   ], "O(n·k)", "O(1)", "k = indexDiff", ""),

   ap("解法二", "滑動視窗 + 排序陣列（bisect）", [
     ("c", S["p220_sorted"]),
     "查詢是 O(log k)，但 <code>insort</code> 和 <code>pop</code> 在 list 中間插入刪除是 O(k)。"
     "在其他語言用 <code>TreeSet</code> / <code>std::set</code> 可以做到 O(n log k)；"
     "Python 可以用第三方的 <code>sortedcontainers.SortedList</code>。",
   ], "O(n·k)（list）", "O(k)", "用平衡樹可降為 O(n log k)", ""),

   ap("解法三", "滑動視窗 + 分桶", [
     ("c", S["p220_bucket"]),
     ("c", """【為什麼刪除時可以直接 del buckets[編號]？】
    每個桶最多一個數，而且視窗裡的數互不在同一桶，
    所以那個桶裡放的一定就是要移除的 nums[i - indexDiff] ✔"""),
   ], "O(n)", "O(min(n, k))", "每個數只看 3 個桶", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、暴力", "O(n·k)", "O(1)", "超時"],
    ["二、有序結構", "O(n log k)*", "O(k)", "*需要平衡樹"],
    ["三、分桶", "O(n)", "O(k)", "最佳 ✔"]]),
 "edges": [
   "<strong><code>valueDiff = 0</code></strong> → 退化成第 219 題；桶寬 1。",
   "<strong>負數</strong> → 必須向下取整分桶（Python 的 <code>//</code> 正確）。",
   "<strong>值很大</strong>（±10⁹）→ 相減不會溢位（Python）；其他語言要用 64 位元。",
   "<strong>同一個桶已經有數</strong> → 直接 <code>true</code>，不需要相減。",
 ],
 "follow": [
   ("h", "追問：分桶的想法還能用在哪？"),
   ("c", """第 164 題「最大間距」：n 個數放進 n+1 個桶，最大間距一定出現在「桶與桶之間」，
不用排序就能 O(n) 求出。分桶是「用值域換時間」的經典技巧。"""),
 ],
 "related": [
   "<strong>第 219 題 存在重複元素 II</strong>",
   "<strong>第 164 題 最大間距</strong> —— 分桶",
   "<strong>第 2817 題 限制條件下元素之間的最小絕對差</strong> —— 有序集合",
 ],
 "check": [
   "桶寬為什麼取 <code>valueDiff + 1</code>？",
   "為什麼每個桶最多只會有一個數？",
   "為什麼只需要檢查相鄰的兩個桶？",
   "負數分桶時要注意什麼？",
 ],
})


# ==================== 221. Maximal Square ====================
S["p221"] = '''class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # dp[i][j]：以 (i-1, j-1) 為「右下角」的最大正方形邊長（多一圈 0 當邊界）
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        best = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    # ★ 上、左、左上三個方向的最小值 + 1
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    best = max(best, dp[i][j])
        return best * best                       # ★ 回傳面積'''

S["p221_1d"] = '''class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        dp = [0] * (n + 1)                       # 上一列的結果，原地更新成這一列
        best = 0
        for row in matrix:
            diag = 0                             # dp[i-1][j-1]
            for j in range(1, n + 1):
                up = dp[j]                       # 還沒被覆蓋：上一列的 dp[j]
                if row[j - 1] == "1":
                    dp[j] = min(up, dp[j - 1], diag) + 1
                    best = max(best, dp[j])
                else:
                    dp[j] = 0
                diag = up                        # 下一格的左上角 = 這一格的上面
        return best * best'''

S["p221_brute"] = '''class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        best = 0
        for i in range(m):
            for j in range(n):
                k = 0                            # 以 (i, j) 為左上角，邊長一直加大
                while i + k < m and j + k < n and all(
                        matrix[i + k][c] == "1" for c in range(j, j + k + 1)) and all(
                        matrix[r][j + k] == "1" for r in range(i, i + k + 1)):
                    k += 1
                best = max(best, k)
        return best * best'''

_p221 = [S.load(x) for x in ("p221", "p221_1d", "p221_brute")]
M1 = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
for mat, want in [(M1, 4), ([["0", "1"], ["1", "0"]], 1), ([["0"]], 0), ([["1"]], 1), ([["1", "1"], ["1", "1"]], 4)]:
    for sol in _p221:
        assert sol.maximalSquare(mat) == want, ("P221", mat, sol)
for _ in range(2000):
    m, n = random.randrange(1, 7), random.randrange(1, 7)
    mat = [[random.choice("0111") for _ in range(n)] for _ in range(m)]
    want = _p221[2].maximalSquare(mat)
    for sol in _p221[:2]:
        assert sol.maximalSquare(mat) == want, ("P221 rand", mat, sol)
print("P221 OK")

_P221_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">dp[i][j] = min(上, 左, 左上) + 1：以 (i, j) 為右下角的最大正方形邊長</text>
            <g font-size="14" text-anchor="middle">
              <rect x="60" y="45" width="50" height="50" fill="none" stroke="var(--accent)"/><text x="85" y="75" fill="var(--accent)">2</text>
              <rect x="110" y="45" width="50" height="50" fill="none" stroke="var(--accent)"/><text x="135" y="75" fill="var(--accent)">2</text>
              <rect x="60" y="95" width="50" height="50" fill="none" stroke="var(--accent)"/><text x="85" y="125" fill="var(--accent)">3</text>
              <rect x="110" y="95" width="50" height="50" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="135" y="125" fill="#ff8a65">?</text>
            </g>
            <text x="70" y="40" fill="var(--text-muted)" font-size="11">左上</text><text x="124" y="40" fill="var(--text-muted)" font-size="11">上</text>
            <text x="36" y="125" fill="var(--text-muted)" font-size="11">左</text>
            <text x="200" y="70" fill="var(--text)" font-size="12">? = min(2, 2, 3) + 1 = 3</text>
            <text x="200" y="100" fill="var(--text)" font-size="12">★ 為什麼是「最小值」？</text>
            <text x="200" y="124" fill="var(--text-muted)" font-size="12">要以 ? 為右下角擴成 k×k，上、左、左上三個方向</text>
            <text x="200" y="146" fill="var(--text-muted)" font-size="12">都必須至少能撐出 (k−1)×(k−1)。</text>
            <text x="200" y="168" fill="var(--text-muted)" font-size="12">三者中最弱的那個決定了能擴多大 —— 木桶原理。</text>
            <text x="20" y="200" fill="var(--gold)" font-size="12">★ 最後回傳的是「面積」= 最大邊長的平方，不是邊長。</text>'''

emit({
 "num": 221, "slug": "maximal-square",
 "en": [
   "Given an <code>m x n</code> binary matrix filled with <code>'0'</code> and <code>'1'</code>, find the largest square "
   "that contains only <code>'1'</code>s and return its <strong>area</strong>.",
 ],
 "zh": [
   "給你一個由 <code>'0'</code> 和 <code>'1'</code> 組成的 <code>m x n</code> 矩陣，找出<strong>只包含 <code>'1'</code> 的最大正方形</strong>，回傳它的<strong>面積</strong>。",
 ],
 "examples": """範例 1
  輸入：matrix = [["1","0","1","0","0"],
                  ["1","0","1","1","1"],
                  ["1","1","1","1","1"],
                  ["1","0","0","1","0"]]
  輸出：4

範例 2
  輸入：matrix = [["0","1"],["1","0"]]
  輸出：1

範例 3
  輸入：matrix = [["0"]]
  輸出：0""",
 "constraints": [
   "<code>m == matrix.length</code>，<code>n == matrix[i].length</code>",
   "1 ≤ <code>m, n</code> ≤ 300",
   "<code>matrix[i][j]</code> 是 <code>'0'</code> 或 <code>'1'</code>",
 ],
 "idea": [
   ("fig", _P221_FIG, "0 0 640 214"),
   ("c", """【狀態】
    dp[i][j] = 以 (i, j) 為「右下角」的全 1 正方形，最大邊長。

【轉移】
    matrix[i][j] == '0' -> dp = 0
    matrix[i][j] == '1' -> dp = min(上, 左, 左上) + 1

【為什麼是 min？】
    要以 (i, j) 為右下角擴成 k×k 的正方形，需要：
        上方那格能撐出 (k-1)×(k-1)
        左方那格能撐出 (k-1)×(k-1)
        左上那格能撐出 (k-1)×(k-1)
    三個條件同時成立 -> k - 1 <= 三者的最小值。
    反過來，三者都 >= k-1 時，四塊拼起來剛好覆蓋 k×k 的每一格 ✔

【邊界】多開一列一行的 0，就不用特別判斷 i = 0 或 j = 0。

【常見錯誤】
    - 回傳邊長而不是面積 ✘
    - 矩陣元素是字串 '1'，寫成 == 1 永遠不成立 ✘"""),
 ],
 "approaches": [
   ap("解法一", "暴力擴張", [
     ("c", S["p221_brute"]),
     "每個格子當左上角，邊長一格一格加大，每次檢查新增的一列一行。最壞 O((mn)·min(m,n)²)。",
   ], "O(mn · min(m,n)²)", "O(1)", "", ""),

   ap("解法二", "二維 DP", [
     ("c", S["p221"]),
   ], "O(mn)", "O(mn)", "", "", optimal=True),

   ap("解法三", "一維 DP（滾動陣列）", [
     ("c", S["p221_1d"]),
     ("c", """【dp[j] 在更新前後代表什麼？】
    更新前：上一列的 dp[j]（= 「上」）
    dp[j-1] 已經更新過：這一列的左邊（= 「左」）
    「左上」是上一列的 dp[j-1]，已經被覆蓋了 ->
    所以要在覆蓋之前用 diag 暫存。

【每一格結束時 diag = up】
    下一格 (j+1) 的左上，就是這一格 (j) 的上 ✔"""),
   ], "O(mn)", "O(n)", "", "只保留一列"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、暴力擴張", "O(mn·min(m,n)²)", "O(1)", "慢"],
    ["二、二維 DP", "O(mn)", "O(mn)", "最直觀 ✔"],
    ["三、一維 DP", "O(mn)", "O(n)", "要小心左上角"]]),
 "edges": [
   "<strong>全部是 '0'</strong> → 0。",
   "<strong>只有一個 '1'</strong> → 面積 1。",
   "<strong>元素是字串</strong> → 要和 <code>'1'</code> 比，不是 <code>1</code>。",
   "<strong>回傳面積</strong> → 邊長要平方。",
 ],
 "follow": [
   ("h", "追問：如果要「最大矩形」而不是正方形？"),
   ("c", """第 85 題（Hard）：對每一列計算「往上連續 1 的高度」，
把問題轉成每一列上的第 84 題「直方圖中最大的矩形」，用單調堆疊 O(n) 解。"""),
   ("h", "追問：要數「所有」全 1 正方形的個數？"),
   ("c", "第 1277 題：同一個 DP，把所有 dp[i][j] 加總即可——以 (i,j) 為右下角的正方形共有 dp[i][j] 個。"),
 ],
 "related": [
   "<strong>第 85 題 最大矩形</strong>",
   "<strong>第 1277 題 統計全為 1 的正方形子矩陣</strong>",
   "<strong>第 84 題 柱狀圖中最大的矩形</strong>",
 ],
 "check": [
   "<code>dp[i][j]</code> 的定義是什麼？",
   "轉移為什麼取三者的最小值？",
   "一維 DP 中為什麼需要 <code>diag</code> 變數？",
   "最後為什麼要平方？",
 ],
})


# ==================== 222. Count Complete Tree Nodes ====================
S["p222"] = '''class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def height(node, go_left: bool) -> int:  # 一路往左（或右）走的深度
            h = 0
            while node:
                h += 1
                node = node.left if go_left else node.right
            return h

        if root is None:
            return 0
        hl, hr = height(root, True), height(root, False)
        if hl == hr:                             # ★ 最左與最右一樣深：這是「滿」二元樹
            return (1 << hl) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)'''

S["p222_bs"] = '''class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        h = 0                                    # 最後一層的層號（根是第 0 層）
        node = root
        while node.left:
            node = node.left
            h += 1

        def exists(idx: int) -> bool:            # 最後一層第 idx 個位置（0 起算）有沒有節點
            node = root
            lo, hi = 0, (1 << h) - 1
            for _ in range(h):                   # 從根往下，每層二分決定往左或往右
                mid = (lo + hi) // 2
                if idx <= mid:
                    node, hi = node.left, mid
                else:
                    node, lo = node.right, mid + 1
            return node is not None

        lo, hi = 0, (1 << h) - 1                 # 二分找最後一層最右邊存在的位置
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if exists(mid):
                lo = mid
            else:
                hi = mid - 1
        return (1 << h) - 1 + lo + 1             # 上面 h 層是滿的 + 最後一層的個數'''

S["p222_dfs"] = '''class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)'''

_p222 = [S.load(x) for x in ("p222", "p222_bs", "p222_dfs")]


def _complete(n):
    if n == 0:
        return None
    nodes = [TreeNode(i + 1) for i in range(n)]
    for i in range(n):
        if 2 * i + 1 < n:
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < n:
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]


for n in list(range(0, 300)) + [50000]:
    t = _complete(n)
    for sol in _p222:
        assert sol.countNodes(t) == n, ("P222", n, sol)
print("P222 OK")

_P222_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">完全二元樹：左右子樹至少有一棵是「滿」的</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="300" cy="55" r="14" fill="none" stroke="var(--text-muted)"/><text x="300" y="59" fill="var(--text)">1</text>
              <circle cx="190" cy="105" r="14" fill="none" stroke="var(--accent)"/><text x="190" y="109" fill="var(--accent)">2</text>
              <circle cx="410" cy="105" r="14" fill="none" stroke="var(--gold)"/><text x="410" y="109" fill="var(--gold)">3</text>
              <circle cx="135" cy="155" r="14" fill="none" stroke="var(--accent)"/><text x="135" y="159" fill="var(--accent)">4</text>
              <circle cx="245" cy="155" r="14" fill="none" stroke="var(--accent)"/><text x="245" y="159" fill="var(--accent)">5</text>
              <circle cx="355" cy="155" r="14" fill="none" stroke="var(--gold)"/><text x="355" y="159" fill="var(--gold)">6</text>
              <circle cx="465" cy="155" r="14" fill="none" stroke="var(--gold)"/><text x="465" y="159" fill="var(--gold)">7</text>
              <circle cx="110" cy="205" r="14" fill="none" stroke="var(--accent)"/><text x="110" y="209" fill="var(--accent)">8</text>
              <circle cx="160" cy="205" r="14" fill="none" stroke="var(--accent)"/><text x="160" y="209" fill="var(--accent)">9</text>
              <circle cx="220" cy="205" r="14" fill="none" stroke="var(--accent)"/><text x="220" y="209" fill="var(--accent)">10</text>
              <circle cx="270" cy="205" r="14" fill="none" stroke="var(--accent)"/><text x="270" y="209" fill="var(--accent)">11</text>
              <circle cx="330" cy="205" r="14" fill="none" stroke="var(--gold)"/><text x="330" y="209" fill="var(--gold)">12</text>
            </g>
            <g stroke="var(--text-muted)" stroke-width="1.1">
              <line x1="289" y1="64" x2="201" y2="96"/><line x1="311" y1="64" x2="399" y2="96"/>
              <line x1="181" y1="116" x2="144" y2="144"/><line x1="199" y1="116" x2="236" y2="144"/>
              <line x1="401" y1="116" x2="364" y2="144"/><line x1="419" y1="116" x2="456" y2="144"/>
              <line x1="130" y1="168" x2="115" y2="192"/><line x1="140" y1="168" x2="155" y2="192"/>
              <line x1="240" y1="168" x2="225" y2="192"/><line x1="250" y1="168" x2="265" y2="192"/>
              <line x1="350" y1="168" x2="335" y2="192"/>
            </g>
            <text x="500" y="60" fill="var(--accent)" font-size="12">左子樹（藍）：</text>
            <text x="500" y="78" fill="var(--accent)" font-size="12">最左、最右都深 3 層</text>
            <text x="500" y="96" fill="var(--accent)" font-size="12">→ 滿 → 2³−1 = 7 個</text>
            <text x="500" y="200" fill="var(--gold)" font-size="12">右子樹（金）：</text>
            <text x="500" y="218" fill="var(--gold)" font-size="12">最左 3 層、最右 2 層 → 遞迴</text>
            <text x="20" y="246" fill="var(--text)" font-size="12">★ 每一層只會往「不滿」的那一邊遞迴一次，每次花 O(log n) 算高度 → O(log² n)。</text>'''

emit({
 "num": 222, "slug": "count-complete-tree-nodes",
 "en": [
   "Given the <code>root</code> of a <strong>complete</strong> binary tree, return the number of nodes in the tree.",
   "In a complete binary tree, every level except possibly the last is completely filled, and the nodes of the last level "
   "are as far left as possible. The last level <code>h</code> may contain between <code>1</code> and <code>2<sup>h</sup></code> nodes.",
   "Design an algorithm that runs in less than <code>O(n)</code> time.",
 ],
 "zh": [
   "給你一棵<strong>完全二元樹</strong>的根節點 <code>root</code>，回傳樹中的節點總數。",
   "完全二元樹：除了最後一層之外，每一層都是滿的；最後一層的節點都<strong>盡量靠左</strong>排列。"
   "若最後一層是第 <code>h</code> 層，它有 <code>1</code> 到 <code>2<sup>h</sup></code> 個節點。",
   "請設計一個<strong>比 <code>O(n)</code> 更快</strong>的演算法。",
 ],
 "examples": """範例 1
  輸入：root = [1,2,3,4,5,6]
  輸出：6

範例 2
  輸入：root = []
  輸出：0

範例 3
  輸入：root = [1]
  輸出：1""",
 "constraints": [
   "樹的節點數在 <code>[0, 5 × 10⁴]</code> 之間",
   "0 ≤ <code>Node.val</code> ≤ 5 × 10⁴",
   "題目保證這是一棵完全二元樹",
 ],
 "idea": [
   ("fig", _P222_FIG, "0 0 700 260"),
   ("c", """【一般遍歷 O(n) 一定可以，但題目要求更快】
    要利用「完全」這個性質。

【關鍵觀察】
    一棵樹如果「一路往左走」和「一路往右走」深度相同，
    它就是【滿】二元樹 -> 節點數 = 2^h - 1，O(log n) 就算完。

    完全二元樹的左右子樹，至少有一棵是滿的：
        最後一層的節點停在左子樹裡 -> 右子樹是滿的（少一層）
        最後一層延伸到右子樹       -> 左子樹是滿的

【所以遞迴時】
    每一層，滿的那一邊 O(log n) 算完，
    只需要往「不滿」的那一邊繼續遞迴 ->
    遞迴深度 O(log n)，每層算高度 O(log n) -> O(log² n) ✔"""),
 ],
 "approaches": [
   ap("解法一", "一般遍歷（O(n)，不符要求）", [
     ("c", S["p222_dfs"]),
     "對任何二元樹都成立，但沒有用到「完全」的性質。",
   ], "O(n)", "O(log n)", "", "遞迴深度 = 樹高"),

   ap("解法二", "比較最左、最右的深度", [
     ("c", S["p222"]),
     ("c", """【為什麼 hl == hr 就是滿的？】
    完全二元樹中，最左路徑一定是最深的。
    最右路徑也一樣深 -> 最後一層從最左到最右都填滿了 ✔

【hl != hr 時】
    根本身算 1 個，左右子樹各自遞迴。
    兩次遞迴中至少有一次會在下一層直接命中「滿」的情況。"""),
   ], "O(log² n)", "O(log n)", "", "遞迴深度", optimal=True),

   ap("解法三", "二分搜尋最後一層", [
     ("c", S["p222_bs"]),
     ("c", """【把最後一層想成一個長度 2^h 的陣列】
    前面一段有節點、後面一段沒有 ——
    「存在 / 不存在」是單調的 -> 可以二分找分界點。

【exists(idx) 怎麼判斷？】
    從根往下 h 步：每一步看 idx 落在左半還是右半，
    就知道往左還是往右 —— 就像在二分搜尋的過程中走樹。
    O(h) = O(log n)。

【總共】二分 O(log n) 次 × 每次 O(log n) -> O(log² n)"""),
   ], "O(log² n)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、一般遍歷", "O(n)", "O(log n)", "不符要求"],
    ["二、比較左右深度", "O(log² n)", "O(log n)", "最簡潔 ✔"],
    ["三、二分最後一層", "O(log² n)", "O(1)", "思路很漂亮"]]),
 "edges": [
   "<strong>空樹</strong> → 0。",
   "<strong>只有根</strong> → 1。",
   "<strong>剛好是滿二元樹</strong> → 解法二一步就算完。",
   "<strong>最後一層只有一個節點</strong> → 二分搜尋的範圍要正確涵蓋位置 0。",
 ],
 "follow": [
   ("h", "追問：如果不保證是完全二元樹？"),
   ("c", "那就只能 O(n) 遍歷——沒有任何結構可以利用。"),
 ],
 "related": [
   "<strong>第 958 題 二元樹的完全性檢驗</strong>",
   "<strong>第 104 題 二元樹的最大深度</strong>",
   "<strong>第 919 題 完全二元樹插入器</strong>",
 ],
 "check": [
   "怎麼在 O(log n) 內判斷一棵完全二元樹是不是「滿」的？",
   "為什麼完全二元樹的左右子樹至少有一棵是滿的？",
   "解法二的複雜度為什麼是 O(log² n)？",
   "解法三中，怎麼判斷最後一層的某個位置有沒有節點？",
 ],
})


# ==================== 223. Rectangle Area ====================
S["p223"] = '''class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        # ★ 重疊部分：x 方向與 y 方向的重疊長度相乘（不重疊時長度取 0）
        w = max(0, min(ax2, bx2) - max(ax1, bx1))
        h = max(0, min(ay2, by2) - max(ay1, by1))
        return area_a + area_b - w * h'''

S["p223_grid"] = '''class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:
        cells = set()                            # 逐格標記（只適合小座標，用來驗證）
        for x1, y1, x2, y2 in ((ax1, ay1, ax2, ay2), (bx1, by1, bx2, by2)):
            for x in range(x1, x2):
                for y in range(y1, y2):
                    cells.add((x, y))
        return len(cells)'''

_p223 = [S.load(x) for x in ("p223", "p223_grid")]
for args, want in [((-3, 0, 3, 4, 0, -1, 9, 2), 45), ((-2, -2, 2, 2, -2, -2, 2, 2), 16),
                   ((0, 0, 0, 0, -1, -1, 1, 1), 4), ((0, 0, 1, 1, 2, 2, 3, 3), 2)]:
    for sol in _p223:
        assert sol.computeArea(*args) == want, ("P223", args, sol)
for _ in range(3000):
    def rect():
        x1, x2 = sorted(random.sample(range(-6, 7), 2))
        y1, y2 = sorted(random.sample(range(-6, 7), 2))
        return [x1, y1, x2, y2]
    args = rect() + rect()
    assert _p223[0].computeArea(*args) == _p223[1].computeArea(*args), ("P223 rand", args)
print("P223 OK")

emit({
 "num": 223, "slug": "rectangle-area",
 "en": [
   "Two axis-aligned rectangles are given in the plane. Rectangle A has bottom-left corner <code>(ax1, ay1)</code> and "
   "top-right corner <code>(ax2, ay2)</code>; rectangle B has bottom-left corner <code>(bx1, by1)</code> and top-right corner "
   "<code>(bx2, by2)</code>.",
   "Return the total area covered by the two rectangles together.",
 ],
 "zh": [
   "平面上有兩個<strong>邊與座標軸平行</strong>的矩形。矩形 A 的左下角是 <code>(ax1, ay1)</code>、右上角是 <code>(ax2, ay2)</code>；"
   "矩形 B 的左下角是 <code>(bx1, by1)</code>、右上角是 <code>(bx2, by2)</code>。",
   "請回傳兩個矩形<strong>合起來覆蓋的總面積</strong>。",
 ],
 "examples": """範例 1
  輸入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
  輸出：45
  說明：A 面積 24、B 面積 27，重疊部分 3 × 2 = 6，24 + 27 − 6 = 45。

範例 2
  輸入：ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
  輸出：16
  說明：兩個矩形完全重合。""",
 "constraints": [
   "−10⁴ ≤ <code>ax1 ≤ ax2</code> ≤ 10⁴",
   "−10⁴ ≤ <code>ay1 ≤ ay2</code> ≤ 10⁴",
   "−10⁴ ≤ <code>bx1 ≤ bx2</code> ≤ 10⁴",
   "−10⁴ ≤ <code>by1 ≤ by2</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【排容原理】
    總面積 = A + B − 重疊

【重疊區域怎麼算？】
    兩個軸對齊矩形的交集，還是一個軸對齊矩形（或空的）。
    x 方向的重疊區間：[max(ax1, bx1), min(ax2, bx2)]
    y 方向的重疊區間：[max(ay1, by1), min(ay2, by2)]
    長度 = 右端 − 左端；如果是負數，代表不重疊 -> 取 0。

    重疊面積 = x 重疊長度 × y 重疊長度

【最常見的錯誤】
    只寫 min(ax2, bx2) - max(ax1, bx1)，沒有和 0 取 max ->
    兩個方向都不重疊時，兩個負數相乘變成正數 ✘
    （例如兩個矩形在對角線方向完全分開）"""),
 ],
 "approaches": [
   ap("解法一", "逐格標記（只適合小座標）", [
     ("c", S["p223_grid"]),
     "座標到 ±10⁴ 時最多要標記 4×10⁸ 格，太慢。只用來驗證公式。",
   ], "O(面積)", "O(面積)", "", ""),

   ap("解法二", "排容原理", [
     ("c", S["p223"]),
   ], "O(1)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、逐格標記", "O(面積)", "O(面積)"],
    ["二、排容原理", "O(1)", "O(1) ✔"]]),
 "edges": [
   "<strong>完全不重疊</strong> → 重疊寬或高至少一個取 0。",
   "<strong>對角分開</strong>（兩個方向都不重疊）→ 一定要和 0 取 max，否則負負得正。",
   "<strong>只有邊或角接觸</strong> → 重疊長度 0，面積 0。",
   "<strong>一個包住另一個</strong> → 重疊就是小的那個。",
   "<strong>退化成一條線或一個點</strong>（面積 0）→ 公式照樣成立。",
 ],
 "follow": [
   ("h", "追問：如果有 n 個矩形，要算聯集面積？"),
   ("c", """這是第 850 題：排容原理的項數會爆炸（2^n），
改用「掃描線 + 座標壓縮」：沿 x 方向掃描，每一段計算被覆蓋的 y 長度總和。"""),
 ],
 "related": [
   "<strong>第 836 題 矩形重疊</strong> —— 只判斷有沒有重疊",
   "<strong>第 850 題 矩形面積 II</strong> —— n 個矩形",
   "<strong>第 986 題 區間列表的交集</strong> —— 一維版本",
 ],
 "check": [
   "兩個矩形的重疊部分怎麼算？",
   "為什麼要和 0 取 max？舉一個不取會出錯的例子。",
 ],
})


# ==================== 224. Basic Calculator ====================
S["p224_stack"] = '''class Solution:
    def calculate(self, s: str) -> int:
        result = 0          # 目前這一層括號內的累計結果
        num = 0             # 正在讀的數字
        sign = 1            # 這個數字前面的正負號
        stack = []          # 進入括號時，存下外層的 (result, sign)
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch in "+-":
                result += sign * num         # 前一個數字結算
                num = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stack.append((result, sign)) # ★ 暫存外層，括號內從 0 重新開始
                result, sign = 0, 1
            elif ch == ")":
                result += sign * num         # 括號內最後一個數字
                num = 0
                prev_result, prev_sign = stack.pop()
                result = prev_result + prev_sign * result   # ★ 括號整體帶著前面的符號
            # 空白直接略過
        return result + sign * num'''

S["p224_rec"] = '''class Solution:
    def calculate(self, s: str) -> int:
        i = 0

        def expr() -> int:                  # 讀到 ')' 或字串結尾為止
            nonlocal i
            total, sign, num = 0, 1, 0
            while i < len(s):
                ch = s[i]
                i += 1
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch in "+-":
                    total += sign * num
                    num, sign = 0, (1 if ch == "+" else -1)
                elif ch == "(":
                    num = expr()            # ★ 遞迴算出括號的值，當成一個數字
                elif ch == ")":
                    break
            return total + sign * num

        return expr()'''

_p224 = [S.load(x) for x in ("p224_stack", "p224_rec")]
for s, want in [("1 + 1", 2), (" 2-1 + 2 ", 3), ("(1+(4+5+2)-3)+(6+8)", 23), ("-(2+3)", -5),
                ("1-(     -2)", 3), ("2147483647", 2147483647), ("- (3 + (4 + 5))", -12), ("(12)-(-(3))", 15)]:
    for sol in _p224:
        assert sol.calculate(s) == want, ("P224", s, sol)


def _gen(depth=0):
    parts = []
    for i in range(random.randrange(1, 4)):
        if i:
            parts.append(random.choice("+-"))
        elif random.random() < 0.3:
            parts.append("-")
        if depth < 3 and random.random() < 0.35:
            parts.append("(" + _gen(depth + 1) + ")")
        else:
            parts.append(str(random.randrange(0, 60)))
    return (" " if random.random() < 0.3 else "").join(parts)


for _ in range(5000):
    e = _gen()
    want = eval(e)
    for sol in _p224:
        assert sol.calculate(e) == want, ("P224 rand", e)
print("P224 OK")

emit({
 "num": 224, "slug": "basic-calculator",
 "en": [
   "Given a string <code>s</code> representing a valid arithmetic expression, evaluate it and return the result.",
   "The expression contains non-negative integers, <code>'+'</code>, <code>'-'</code>, <code>'('</code>, <code>')'</code>, and spaces. "
   "<code>'-'</code> may be used as a unary minus (for example <code>\"-1\"</code> or <code>\"-(2 + 3)\"</code>), but <code>'+'</code> is never unary.",
   "You may not use any built-in function that evaluates strings as expressions, such as <code>eval()</code>.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，代表一個<strong>合法的</strong>算式，請計算並回傳結果。",
   "算式只包含非負整數、<code>'+'</code>、<code>'-'</code>、<code>'('</code>、<code>')'</code> 和空白。"
   "<code>'-'</code> 可以當作<strong>一元負號</strong>（例如 <code>\"-1\"</code>、<code>\"-(2 + 3)\"</code>），但 <code>'+'</code> 不會是一元的。",
   "<strong>不能使用 <code>eval()</code></strong> 這類直接計算字串的內建函式。",
 ],
 "examples": """範例 1
  輸入：s = "1 + 1"
  輸出：2

範例 2
  輸入：s = " 2-1 + 2 "
  輸出：3

範例 3
  輸入：s = "(1+(4+5+2)-3)+(6+8)"
  輸出：23""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 3 × 10⁵",
   "<code>s</code> 由數字、<code>'+'</code>、<code>'-'</code>、<code>'('</code>、<code>')'</code>、<code>' '</code> 組成",
   "<code>s</code> 是合法的算式",
   "不會出現連續兩個運算子",
   "所有數字與運算過程的結果都在 32 位元有號整數範圍內",
 ],
 "idea": [
   ("c", """【沒有括號時】
    只有加減，由左到右：每個數字帶著它前面的正負號加總。
        "2 - 1 + 2" = (+2) + (-1) + (+2) = 3

    一元負號自然成立："-1" 就是 (sign = -1) × 1。

【有括號時】
    一對括號 = 一個小算式，它的值要整體帶著前面的正負號：
        "3 - (4 - 5)" = 3 + (-1) × (4 - 5) = 4

【用堆疊暫存外層的狀態】
    遇到 '(' ：
        把目前的 result 和括號前的 sign 推進堆疊，
        括號內從 result = 0、sign = +1 重新開始。
    遇到 ')' ：
        結算括號內的值 inner，
        彈出外層的 (prev_result, prev_sign)：
            result = prev_result + prev_sign × inner

【最容易漏的】
    ')' 之前的最後一個數字、字串結尾的最後一個數字，
    都要記得 result += sign × num。"""),
 ],
 "approaches": [
   ap("解法一", "一次掃描 + 堆疊", [
     ("c", S["p224_stack"]),
     ("c", """【模擬】s = "1 - (2 + 3)"

    讀 1          num = 1
    讀 '-'        result = 1, sign = -1
    讀 '('        push (1, -1)；result = 0, sign = 1
    讀 2, '+'     result = 2, sign = 1
    讀 3, ')'     result = 2 + 3 = 5；pop (1, -1)
                  result = 1 + (-1) × 5 = -4
    結尾          -4 + 1 × 0 = -4 ✔"""),
   ], "O(n)", "O(n)", "", "堆疊深度 = 括號層數", optimal=True),

   ap("解法二", "遞迴下降", [
     ("c", S["p224_rec"]),
     ("c", """【遇到 '(' 就遞迴呼叫 expr()】
    它會讀到對應的 ')' 為止，回傳括號內的值，
    這個值被當成一個普通數字 num，接著由外層的 sign 處理。

【nonlocal i】
    所有層級共用同一個讀取位置，
    內層讀過的字元，外層不會再讀一次。

【遞迴深度】
    = 括號巢狀層數。極端情況（上萬層括號）會超過遞迴上限。"""),
   ], "O(n)", "O(n)", "", "遞迴深度"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、堆疊", "O(n)", "O(n)", "不怕深層括號 ✔"],
    ["二、遞迴下降", "O(n)", "O(n)", "容易擴充到乘除"]]),
 "edges": [
   "<strong>開頭就是負號</strong>（<code>\"-1\"</code>）→ sign 一開始變成 −1，自然處理。",
   "<strong>括號前的負號</strong>（<code>\"-(2+3)\"</code>）→ 整個括號取負。",
   "<strong>括號內開頭是負號</strong>（<code>\"1-(-2)\"</code>）→ 括號內 sign 重新從 +1 開始，才能正確處理。",
   "<strong>多位數</strong> → <code>num = num * 10 + d</code>。",
   "<strong>大量空白</strong> → 直接略過。",
   "<strong>忘了結算最後一個數字</strong> → 答案少一項。",
 ],
 "follow": [
   ("h", "追問：如果加上乘除（第 227 題）？"),
   ("c", """乘除優先順序比加減高 ——
遇到加減時把數字（帶正負號）推進堆疊；
遇到乘除時彈出堆疊頂端，算完再推回去；
最後把堆疊全部加總。"""),
   ("h", "追問：加減乘除再加括號（第 772 題，付費）？"),
   ("c", "把第 227 題的做法放進遞迴下降：每遇到 '(' 就遞迴，括號內用堆疊處理乘除。"),
 ],
 "related": [
   "<strong>第 227 題 基本計算器 II</strong> —— 加減乘除，沒有括號",
   "<strong>第 150 題 逆波蘭表示法求值</strong>",
   "<strong>第 394 題 字串解碼</strong> —— 同樣的「括號 = 堆疊」套路",
 ],
 "check": [
   "遇到 <code>'('</code> 時要把什麼推進堆疊？為什麼？",
   "遇到 <code>')'</code> 時怎麼和外層合併？",
   "一元負號為什麼不需要特別處理？",
   "有哪兩個地方容易忘記結算最後一個數字？",
 ],
})
