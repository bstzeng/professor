# -*- coding: utf-8 -*-
"""第 453–458 題。"""
import random
import itertools
import math
from collections import Counter
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(453)


# ==================== 453. Minimum Moves to Equal Array Elements ====================
S["p453"] = '''class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # ★ 「n-1 個數各加 1」等價於「1 個數減 1」（相對大小的變化一樣）
        #   所以問題變成：把所有數減到和最小值一樣，要減幾次
        m = min(nums)
        return sum(x - m for x in nums)'''

_p453 = S.load("p453")


def _mm_sim(nums):
    a = sorted(nums)
    moves = 0
    while a[0] != a[-1]:                       # 模擬：除了最大值以外全部 +1
        i = a.index(max(a))
        a = [x + 1 if j != i else x for j, x in enumerate(a)]
        a.sort()
        moves += 1
    return moves


for _ in range(1500):
    a = [random.randint(-3, 5) for _ in range(random.randrange(1, 6))]
    assert _p453.minMoves(a) == _mm_sim(a), a
print("P453 OK")

emit({
 "num": 453, "slug": "minimum-moves-to-equal-array-elements",
 "en": [
   "Given an integer array <code>nums</code> of size <code>n</code>, return <em>the minimum number of moves required to make all array elements equal</em>.",
   "In one move, you can increment <code>n - 1</code> elements of the array by <code>1</code>.",
 ],
 "zh": [
   "給你一個長度為 <code>n</code> 的整數陣列，每一步可以把其中 <code>n − 1</code> 個元素各加 1。回傳讓所有元素相等的最少步數。",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3]
  輸出：3
  說明：[1,2,3] => [2,3,3] => [3,4,3] => [4,4,4]

範例 2
  輸入：nums = [1,1,1]
  輸出：0""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
   "答案保證在 32 位元整數範圍內",
 ],
 "idea": [
   ("c", """【換個角度：相對差距】
    我們只在乎「所有數相等」，也就是它們之間的差距都是 0。
    「n-1 個數各加 1」對差距的影響，
    和「剩下那 1 個數減 1」完全一樣。

【所以問題變成：每一步把一個數減 1】
    所有數都要減到最小值 ->
    步數 = Σ (x - min)

【為什麼是減到最小值而不是更小？】
    減到比最小值更小，每個數都要多減一樣多次，只會更多。"""),
 ],
 "approaches": [
   ap("解法", "轉換成「一個數減 1」", [
     ("c", S["p453"]),
     "驗證方式：和「每次把最大值以外的數加 1」的直接模擬比對。",
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>已經全部相等</strong> → 0。",
   "<strong>只有一個數</strong> → 0。",
   "<strong>負數</strong> → 公式照樣成立。",
 ],
 "follow": [
   ("h", "變化題"),
   ("c", "第 462 題：每步可以把任一個數 +1 或 −1 —— 答案是讓所有數都變成「中位數」。"),
 ],
 "related": [
   "<strong>第 462 題 最小操作次數使陣列元素相等 II</strong>",
   "<strong>第 2033 題 獲取單值網格的最小操作數</strong>",
 ],
 "check": [
   "為什麼「n−1 個數加 1」等價於「1 個數減 1」？",
   "為什麼目標是最小值？",
 ],
})


# ==================== 454. 4Sum II ====================
S["p454"] = '''class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # ★ 兩兩分組：先記下 nums1 + nums2 所有和的出現次數
        ab = collections.Counter(a + b for a in nums1 for b in nums2)
        # 再找 nums3 + nums4 的和 c + d，需要 a + b = -(c + d)
        return sum(ab[-(c + d)] for c in nums3 for d in nums4)'''

_p454 = S.load("p454")
for _ in range(800):
    n = random.randrange(1, 6)
    A = [[random.randint(-3, 3) for _ in range(n)] for _ in range(4)]
    want = sum(1 for a, b, c, d in itertools.product(*A) if a + b + c + d == 0)
    assert _p454.fourSumCount(*A) == want
print("P454 OK")

emit({
 "num": 454, "slug": "4sum-ii",
 "en": [
   "Given four integer arrays <code>nums1</code>, <code>nums2</code>, <code>nums3</code>, and <code>nums4</code> all of length <code>n</code>, return the number of tuples <code>(i, j, k, l)</code> such that:",
   ("ul", ["<code>0 &lt;= i, j, k, l &lt; n</code>",
           "<code>nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0</code>"]),
 ],
 "zh": [
   "給你四個長度都是 <code>n</code> 的整數陣列，回傳有幾組 <code>(i, j, k, l)</code> 使得 <code>nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0</code>。",
 ],
 "examples": """範例 1
  輸入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
  輸出：2

範例 2
  輸入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
  輸出：1""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 200",
   "−2²⁸ ≤ <code>nums[i]</code> ≤ 2²⁸",
 ],
 "idea": [
   ("c", """【暴力 O(n⁴)：200⁴ = 1.6×10⁹，太慢】

【折半（meet in the middle）】
    a + b + c + d = 0  <=>  a + b = -(c + d)
    先把所有 a + b 的和計數（n² 種），
    再對每個 c + d，查 -(c + d) 出現幾次。
    兩邊都是 O(n²) -> 總共 O(n²)。

【和第 15 題 3Sum 不同】
    這題是四個「不同的陣列」，只數組合個數，不用去重，
    所以雜湊表計數就好。"""),
 ],
 "approaches": [
   ap("解法", "兩兩分組 + 雜湊表", [
     ("c", S["p454"]),
   ], "O(n²)", "O(n²)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>n = 1</strong> → 檢查四個數的和是否為 0。",
   "<strong>重複值</strong> → 雜湊表計數自然處理。",
 ],
 "follow": [
   ("h", "折半搜尋"),
   ("c", "「把問題拆成兩半，各自列舉後再配對」可以把 O(n^k) 變成 O(n^(k/2))。第 1755 題（最接近目標值的子序列和）把 2⁴⁰ 拆成兩個 2²⁰。"),
 ],
 "related": [
   "<strong>第 1 題 兩數之和</strong>",
   "<strong>第 18 題 四數之和</strong> —— 同一個陣列，要去重",
   "<strong>第 1755 題 最接近目標值的子序列和</strong>",
 ],
 "check": [
   "為什麼要把四個陣列分成兩組？",
   "複雜度從 O(n⁴) 降到多少？",
 ],
})


# ==================== 455. Assign Cookies ====================
S["p455"] = '''class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()                          # 孩子的胃口
        s.sort()                          # 餅乾的大小
        child = 0
        for cookie in s:                  # ★ 從小餅乾開始，給目前胃口最小、還沒滿足的孩子
            if child < len(g) and cookie >= g[child]:
                child += 1
        return child'''

_p455 = S.load("p455")


def _cookie_ref(g, s):
    best = 0
    for r in range(min(len(g), len(s)), 0, -1):
        for kids in itertools.combinations(sorted(g), r):
            for ck in itertools.combinations(sorted(s), r):
                if all(c >= k for c, k in zip(ck, kids)):
                    return r
    return 0


for g, s, want in [([1, 2, 3], [1, 1], 1), ([1, 2], [1, 2, 3], 2)]:
    assert _p455.findContentChildren(g, s) == want
for _ in range(1000):
    g = [random.randint(1, 6) for _ in range(random.randrange(1, 6))]
    s = [random.randint(1, 6) for _ in range(random.randrange(0, 6))]
    assert _p455.findContentChildren(list(g), list(s)) == _cookie_ref(g, s)
print("P455 OK")

emit({
 "num": 455, "slug": "assign-cookies",
 "en": [
   "Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.",
   "Each child <code>i</code> has a greed factor <code>g[i]</code>, which is the minimum size of a cookie that the child will be content with; and each cookie <code>j</code> has a size <code>s[j]</code>. If <code>s[j] &gt;= g[i]</code>, we can assign the cookie <code>j</code> to the child <code>i</code>, and the child <code>i</code> will be content. Your goal is to maximize the number of your content children and output the maximum number.",
 ],
 "zh": [
   "你要分餅乾給孩子，每個孩子最多一塊。",
   "孩子 <code>i</code> 的胃口是 <code>g[i]</code>（能讓他滿足的最小餅乾大小），餅乾 <code>j</code> 的大小是 <code>s[j]</code>。<code>s[j] ≥ g[i]</code> 時孩子就會滿足。回傳最多能讓幾個孩子滿足。",
 ],
 "examples": """範例 1
  輸入：g = [1,2,3], s = [1,1]
  輸出：1

範例 2
  輸入：g = [1,2], s = [1,2,3]
  輸出：2""",
 "constraints": [
   "1 ≤ <code>g.length</code> ≤ 3 × 10⁴",
   "0 ≤ <code>s.length</code> ≤ 3 × 10⁴",
   "1 ≤ <code>g[i], s[j]</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【貪心：小餅乾給小胃口】
    兩邊都排序。
    從最小的餅乾開始：
        能滿足目前胃口最小的孩子 -> 給他
        不能 -> 這塊餅乾誰都滿足不了（其他孩子胃口更大），丟掉

【為什麼不會吃虧？】
    交換論證：如果最佳解把一塊大餅乾給了小胃口的孩子，
    把它換成「剛好夠用」的小餅乾，大餅乾留給別人 ——
    滿足的人數不會變少。"""),
 ],
 "approaches": [
   ap("解法", "排序 + 雙指標貪心", [
     ("c", S["p455"]),
   ], "O(n log n + m log m)", "O(1)", "", "不計排序", optimal=True),
 ],
 "edges": [
   "<strong>沒有餅乾</strong> → 0。",
   "<strong>所有餅乾都太小</strong> → 0。",
   "<strong>餅乾比孩子多</strong> → 最多滿足全部孩子。",
 ],
 "follow": [
   ("h", "貪心的交換論證"),
   ("c", "證明貪心正確最常用的方法：假設最佳解和貪心選擇不同，證明可以把最佳解「換成」貪心的選擇而不變差。第 435、452、406 題都可以這樣證明。"),
 ],
 "related": [
   "<strong>第 881 題 救生艇</strong> —— 另一題排序 + 雙指標貪心",
   "<strong>第 2410 題 運動員和訓練師的最大匹配數</strong> —— 幾乎相同",
 ],
 "check": [
   "為什麼從最小的餅乾開始分？",
   "一塊餅乾滿足不了目前胃口最小的孩子時，為什麼可以直接丟掉？",
 ],
})


# ==================== 456. 132 Pattern ====================
S["p456"] = '''class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []                     # 單調遞減堆疊（從右往左掃），存「3」的候選
        two = -float("inf")            # 目前找到的最大的「2」（某個被彈出的數）
        for x in reversed(nums):
            if x < two:                # ★ 找到「1」：x < 2 < 3
                return True
            while stack and stack[-1] < x:
                two = stack.pop()      # x 當「3」，被彈出的比 x 小 -> 可以當「2」
            stack.append(x)
        return False'''

S["p456_min"] = '''class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        for j in range(n):                    # 枚舉「3」的位置
            one = min(nums[:j], default=None) # 左邊最小的當「1」
            if one is None or one >= nums[j]:
                continue
            if any(one < nums[k] < nums[j] for k in range(j + 1, n)):
                return True
        return False'''

_p456 = [S.load(x) for x in ("p456", "p456_min")]
for nums, want in [([1, 2, 3, 4], False), ([3, 1, 4, 2], True), ([-1, 3, 2, 0], True), ([1, 0, 1, -4, -3], False)]:
    for sol in _p456:
        assert sol.find132pattern(nums) == want
for _ in range(3000):
    a = [random.randint(0, 5) for _ in range(random.randrange(1, 9))]
    want = any(a[i] < a[k] < a[j] for i, j, k in itertools.combinations(range(len(a)), 3))
    for sol in _p456:
        assert sol.find132pattern(a) == want, (a, sol)
print("P456 OK")

_P456_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">nums = [3, 1, 4, 2]：從右往左掃，堆疊遞減</text>
            <g font-size="12">
              <text x="30" y="52" fill="var(--text-muted)">讀入</text><text x="100" y="52" fill="var(--text-muted)">堆疊</text><text x="200" y="52" fill="var(--text-muted)">two</text><text x="270" y="52" fill="var(--text-muted)">說明</text>
              <text x="30" y="78" fill="var(--text)">2</text><text x="100" y="78" fill="var(--text)">[2]</text><text x="200" y="78" fill="var(--text)">−∞</text>
              <text x="30" y="102" fill="var(--text)">4</text><text x="100" y="102" fill="var(--text)">[4]</text><text x="200" y="102" fill="var(--accent)">2</text><text x="270" y="102" fill="var(--accent)">4 當「3」，彈出的 2 當「2」</text>
              <text x="30" y="126" fill="var(--text)">1</text><text x="100" y="126" fill="var(--text)"></text><text x="200" y="126" fill="var(--text)">2</text><text x="270" y="126" fill="var(--gold)">1 &lt; two = 2 → 找到 1, 4, 2 ✔</text>
            </g>
            <text x="20" y="166" fill="var(--text)" font-size="12">為什麼 two 一定有一個比它大的「3」在它左邊？</text>
            <text x="20" y="188" fill="var(--text-muted)" font-size="12">two 是被某個 x 彈出來的 —— 那個 x 比 two 大，而且位置在 two 的左邊（從右往左掃）。</text>
            <text x="20" y="210" fill="var(--text-muted)" font-size="12">所以只要再遇到一個比 two 小的數，就湊齊了 1 &lt; 2 &lt; 3（位置 i &lt; j &lt; k）。</text>'''

emit({
 "num": 456, "slug": "132-pattern",
 "en": [
   "Given an array of <code>n</code> integers <code>nums</code>, a <strong>132 pattern</strong> is a subsequence of three integers <code>nums[i]</code>, <code>nums[j]</code> and <code>nums[k]</code> such that <code>i &lt; j &lt; k</code> and <code>nums[i] &lt; nums[k] &lt; nums[j]</code>.",
   "Return <code>true</code> <em>if there is a <strong>132 pattern</strong> in</em> <code>nums</code><em>, otherwise, return</em> <code>false</code>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，<strong>132 模式</strong>是指三個位置 <code>i &lt; j &lt; k</code>，滿足 <code>nums[i] &lt; nums[k] &lt; nums[j]</code>（小、大、中）。",
   "判斷陣列中是否存在 132 模式。",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,4]
  輸出：false

範例 2
  輸入：nums = [3,1,4,2]
  輸出：true
  說明：[1, 4, 2]

範例 3
  輸入：nums = [-1,3,2,0]
  輸出：true
  說明：[-1, 3, 2]、[-1, 3, 0]、[-1, 2, 0]""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 2 × 10⁵",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
 ],
 "idea": [
   ("fig", _P456_FIG, "0 0 640 224"),
   ("c", """【三個角色：1（最小，最左）、3（最大，中間）、2（中等，最右）】

【O(n²)：枚舉「3」】
    左邊最小的數當「1」最好（前綴最小值），
    再看右邊有沒有落在 (1, 3) 之間的數。

【O(n)：從右往左 + 單調堆疊】
    從右往左掃，維護：
        stack：遞減的單調堆疊（「3」的候選）
        two：目前能當「2」的最大值（左邊一定有比它大的「3」）
    讀到 x：
        x < two -> x 可以當「1」，找到了！
        否則，x 當「3」：把堆疊中比 x 小的都彈出，
            它們都在 x 右邊、比 x 小 -> 都可以當「2」，保留最大的
        x 推進堆疊

【為什麼 two 要保留「最大」的？】
    two 越大，越容易找到比它小的「1」。
    而堆疊是遞減的，最後被彈出的就是最大的。"""),
 ],
 "approaches": [
   ap("解法一", "枚舉「3」+ 前綴最小值", [
     ("c", S["p456_min"]),
   ], "O(n²)", "O(1)", "", ""),

   ap("解法二", "從右往左的單調堆疊", [
     ("c", S["p456"]),
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["暴力三重迴圈", "O(n³)", "O(1)"],
    ["一、枚舉 3", "O(n²)", "O(1)"],
    ["二、單調堆疊", "O(n)", "O(n) ✔"]]),
 "edges": [
   "<strong>長度 &lt; 3</strong> → false。",
   "<strong>嚴格遞增或遞減</strong> → false。",
   "<strong>相等的值</strong> → 條件是嚴格不等，彈出時用 &lt; 而不是 ≤。",
 ],
 "follow": [
   ("h", "單調堆疊的「被彈出的元素」"),
   ("c", "這題的巧妙之處在於利用「被彈出的元素」本身的資訊：它被彈出，就代表左邊有比它大的數。第 907、2104 題也利用被彈出元素來計算貢獻。"),
 ],
 "related": [
   "<strong>第 334 題 遞增的三元子序列</strong>",
   "<strong>第 496 題 下一個更大元素 I</strong>",
 ],
 "check": [
   "三個角色的位置和大小關係是什麼？",
   "two 代表什麼？為什麼它左邊一定有更大的數？",
   "為什麼 two 要保留最大的？",
 ],
})


# ==================== 457. Circular Array Loop ====================
S["p457"] = '''class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        def nxt(i: int) -> int:
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:                   # 已經確認過不在合法的環上
                continue
            forward = nums[i] > 0
            slow, fast = i, i
            # ★ 快慢指標，而且整條路徑的方向都必須相同
            while True:
                s1 = nxt(slow)
                f1 = nxt(fast)
                if nums[s1] * nums[i] <= 0 or nums[f1] * nums[i] <= 0:
                    break
                f2 = nxt(f1)
                if nums[f2] * nums[i] <= 0:
                    break
                slow, fast = s1, f2
                if slow == fast:
                    if slow == nxt(slow):      # 環長為 1（自己指向自己）不算
                        break
                    return True
            # 這條路徑上的點都不可能在合法環上：標成 0，之後跳過
            j = i
            while nums[j] != 0 and (nums[j] > 0) == forward:
                k = nxt(j)
                nums[j] = 0
                j = k
        return False'''

_p457 = S.load("p457")


def _cal_ref(nums):
    n = len(nums)
    for s in range(n):
        seen = []
        i = s
        for _ in range(n + 1):
            seen.append(i)
            i = (i + nums[i]) % n
        # 走 n+1 步後一定在環上；檢查這個環
        start = i
        cyc = [start]
        j = (start + nums[start]) % n
        while j != start:
            cyc.append(j)
            j = (j + nums[j]) % n
        if len(cyc) > 1 and (all(nums[c] > 0 for c in cyc) or all(nums[c] < 0 for c in cyc)):
            return True
    return False


for nums, want in [([2, -1, 1, 2, 2], True), ([-1, -2, -3, -4, -5, 6], False), ([1, -1, 5, 1, 4], True)]:
    assert _p457.circularArrayLoop(list(nums)) == want
for _ in range(3000):
    n = random.randrange(1, 8)
    nums = [random.choice([-1, 1]) * random.randint(1, 6) for _ in range(n)]
    assert _p457.circularArrayLoop(list(nums)) == _cal_ref(nums), nums
print("P457 OK")

emit({
 "num": 457, "slug": "circular-array-loop",
 "en": [
   "You are playing a game involving a <strong>circular</strong> array of non-zero integers <code>nums</code>. Each <code>nums[i]</code> denotes the number of indices forward/backward you must move if you are located at index <code>i</code>:",
   ("ul", ["If <code>nums[i]</code> is positive, move <code>nums[i]</code> steps <strong>forward</strong>, and",
           "If <code>nums[i]</code> is negative, move <code>nums[i]</code> steps <strong>backward</strong>."]),
   "Since the array is <strong>circular</strong>, you may assume that moving forward from the last element puts you on the first element, and moving backwards from the first element puts you on the last element.",
   "A <strong>cycle</strong> in the array consists of a sequence of indices <code>seq</code> of length <code>k</code> where:",
   ("ul", ["Following the movement rules above results in the repeating index sequence <code>seq[0] -&gt; seq[1] -&gt; ... -&gt; seq[k - 1] -&gt; seq[0] -&gt; ...</code>",
           "Every <code>nums[seq[j]]</code> is either <strong>all positive</strong> or <strong>all negative</strong>.",
           "<code>k &gt; 1</code>"]),
   "Return <code>true</code> <em>if there is a <strong>cycle</strong> in</em> <code>nums</code><em>, or</em> <code>false</code> <em>otherwise</em>.",
   "<strong>Follow up:</strong> Could you solve it in <code>O(n)</code> time complexity and <code>O(1)</code> extra space complexity?",
 ],
 "zh": [
   "給你一個由非零整數組成的<strong>環形</strong>陣列 <code>nums</code>。站在索引 <code>i</code> 時，正數往前走 <code>nums[i]</code> 步，負數往後走 <code>|nums[i]|</code> 步（頭尾相接）。",
   "陣列中的<strong>環</strong>要滿足：",
   ("ul", ["依規則移動會不斷重複同一串索引；",
           "環上所有的數<strong>同號</strong>（全正或全負）；",
           "環的長度 <code>k &gt; 1</code>（自己指向自己不算）。"]),
   "判斷陣列中是否存在這樣的環。",
   "<strong>進階：</strong>能 <code>O(n)</code> 時間、<code>O(1)</code> 空間嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [2,-1,1,2,2]
  輸出：true
  說明：0 → 2 → 3 → 0，全部往前。

範例 2
  輸入：nums = [-1,-2,-3,-4,-5,6]
  輸出：false
  說明：唯一的環是 5 → 5，長度 1 不算。

範例 3
  輸入：nums = [1,-1,5,1,4]
  輸出：true
  說明：3 → 4 → 3（0 → 1 → 0 的方向不同，不算）。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 5000",
   "−1000 ≤ <code>nums[i]</code> ≤ 1000，<code>nums[i] != 0</code>",
 ],
 "idea": [
   ("c", """【每個索引恰好有一條出邊 -> 函數圖】
    從任何點出發一直走，最後一定會進入一個環。
    問題是：有沒有一個環同時滿足「同號」和「長度 > 1」。

【快慢指標（Floyd 判圈，第 141 題）】
    從 i 出發，slow 一次一步、fast 一次兩步，
    途中只要遇到「和 i 方向不同」的點就放棄（不可能是合法的同向環）。
    相遇 -> 找到環；再檢查環長不是 1。

【O(n)：把失敗的路徑標成 0】
    從 i 出發失敗的話，這條路徑上（同方向的那一段）的所有點，
    從它們出發也只會走進同一個失敗的結局 ->
    標成 0，之後直接跳過。每個點最多被處理常數次。

【環長為 1】
    nxt(x) == x，例如 nums[x] 是 n 的倍數。"""),
 ],
 "approaches": [
   ap("解法", "快慢指標 + 標記失敗路徑", [
     ("c", S["p457"]),
     "驗證方式：和「從每個點走 n+1 步進入環，再逐一檢查那個環」的暴力版本比對三千組。",
   ], "O(n)", "O(1)", "", "會修改輸入", optimal=True),
 ],
 "edges": [
   "<strong>自己指向自己</strong>（nums[i] 是 n 的倍數）→ 長度 1，不算。",
   "<strong>環上方向混合</strong> → 不算。",
   "<strong>負數取模</strong> → Python 的 % 永遠是非負，其他語言要 ((i + x) % n + n) % n。",
 ],
 "follow": [
   ("h", "函數圖"),
   ("c", "每個節點只有一條出邊的圖叫函數圖：每個連通分量恰好一個環，其他節點是指向環的樹。第 2127 題（參加會議的最多員工數）、第 2360 題（圖中的最長環）都在處理函數圖。"),
 ],
 "related": [
   "<strong>第 141 題 環狀鏈結串列</strong>",
   "<strong>第 287 題 尋找重複數</strong>",
   "<strong>第 2360 題 圖中的最長環</strong>",
 ],
 "check": [
   "為什麼從任何點出發最後一定會進入環？",
   "怎麼排除「方向混合」和「長度 1」的環？",
   "為什麼可以把失敗路徑上的點標成 0？",
 ],
})


# ==================== 458. Poor Pigs ====================
S["p458"] = '''class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        states = minutesToTest // minutesToDie + 1    # ★ 每隻豬的結局有幾種：第 1 輪死、第 2 輪死……或活到最後
        pigs = 0
        while states ** pigs < buckets:               # pigs 隻豬能區分 states^pigs 種情況
            pigs += 1
        return pigs'''

_p458 = S.load("p458")
for b, d, t, want in [(4, 15, 15, 2), (4, 15, 30, 2), (1000, 15, 60, 5), (1, 1, 1, 0), (1000, 12, 60, 4)]:
    assert _p458.poorPigs(b, d, t) == want
for _ in range(3000):
    b = random.randint(1, 1000)
    d = random.randint(1, 100)
    t = random.randint(d, 100)
    s = t // d + 1
    want = math.ceil(math.log(b) / math.log(s) - 1e-12) if b > 1 else 0
    got = _p458.poorPigs(b, d, t)
    assert s ** got >= b and (got == 0 or s ** (got - 1) < b)
print("P458 OK")

emit({
 "num": 458, "slug": "poor-pigs",
 "en": [
   "There are <code>buckets</code> buckets of liquid, where <strong>exactly one</strong> of the buckets is poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs the liquid to see whether they will die or not. Unfortunately, you only have <code>minutesToTest</code> minutes to determine which bucket is poisonous.",
   "You can feed the pigs according to these steps:",
   ("ol", ["Choose some live pigs to feed.",
           "For each pig, choose which buckets to feed it. The pig will consume all the chosen buckets simultaneously and will take no time. Each pig can feed from any number of buckets, and each bucket can be fed from by any number of pigs.",
           "Wait for <code>minutesToDie</code> minutes. You may <strong>not</strong> feed any other pigs during this time.",
           "After <code>minutesToDie</code> minutes have passed, any pigs that have been fed the poisonous bucket will die, and all others will survive.",
           "Repeat this process until you run out of time."]),
   "Given <code>buckets</code>, <code>minutesToDie</code>, and <code>minutesToTest</code>, return <em>the <strong>minimum</strong> number of pigs needed to figure out which bucket is poisonous within the allotted time</em>.",
 ],
 "zh": [
   "有 <code>buckets</code> 桶液體，其中<strong>恰好一桶</strong>有毒。你可以讓豬喝液體，看牠會不會死，來找出毒桶。總共只有 <code>minutesToTest</code> 分鐘。",
   "每一輪：選一些活著的豬，讓每隻豬同時喝任意幾桶（每桶也可以給任意多隻豬喝），然後等 <code>minutesToDie</code> 分鐘，喝到毒的豬會死。時間夠就可以再進行下一輪。",
   "回傳能保證找出毒桶的<strong>最少</strong>豬數。",
 ],
 "examples": """範例 1
  輸入：buckets = 4, minutesToDie = 15, minutesToTest = 15
  輸出：2
  說明：只有一輪。豬 A 喝 1、2 桶，豬 B 喝 2、3 桶：
    都活著 → 第 4 桶；只有 A 死 → 第 1 桶；
    只有 B 死 → 第 3 桶；都死 → 第 2 桶。

範例 2
  輸入：buckets = 1000, minutesToDie = 15, minutesToTest = 60
  輸出：5""",
 "constraints": [
   "1 ≤ <code>buckets</code> ≤ 1000",
   "1 ≤ <code>minutesToDie ≤ minutesToTest</code> ≤ 100",
 ],
 "idea": [
   ("c", """【資訊量的角度】
    可以進行 T = minutesToTest / minutesToDie 輪。
    一隻豬的「結局」有 T + 1 種：
        第 1 輪死、第 2 輪死、……、第 T 輪死、活到最後。
    p 隻豬的結局組合有 (T + 1)^p 種，
    每一種組合要對應到一個桶 ->
    需要 (T + 1)^p >= buckets。

【真的做得到嗎？—— 用 (T+1) 進位編號】
    把桶編號寫成 p 位的 (T+1) 進位數。
    第 k 隻豬負責第 k 位：
        第 r 輪，喝「第 k 位是 r-1」的所有桶。
    豬在第 r 輪死 -> 毒桶的第 k 位是 r-1；
    活到最後 -> 第 k 位是 T。
    p 隻豬的結果剛好拼出毒桶的完整編號。

【範例 1：T = 1，2 種結局】
    2 隻豬 -> 2² = 4 >= 4 桶 ✔（就是二進位編號）"""),
   ("t", ["桶編號（二進位）", "豬 A 喝？（第 1 位）", "豬 B 喝？（第 0 位）"],
    [["0 = 00", "", ""], ["1 = 01", "", "✔"], ["2 = 10", "✔", ""], ["3 = 11", "✔", "✔"]]),
 ],
 "approaches": [
   ap("解法", "資訊量：(T+1)^p ≥ buckets", [
     ("c", S["p458"]),
   ], "O(log buckets)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>只有 1 桶</strong> → 0 隻豬（不用測就知道）。",
   "<strong>T = 0</strong>（minutesToTest &lt; minutesToDie）→ 題目限制保證至少一輪。",
   "<strong>用浮點 log 計算</strong> → 邊界可能差 1，用整數次方比較最安全。",
 ],
 "follow": [
   ("h", "資訊論下界"),
   ("c", "這題是「用最少的測試分辨 N 種可能」的經典模型：每次測試有 k 種結果，需要 log_k N 次。二分搜尋（k = 2）、秤重找假幣（k = 3，天平有三種結果）都是它的特例。"),
 ],
 "related": [
   "<strong>第 887 題 雞蛋掉落</strong> —— 另一個「最少測試次數」問題",
 ],
 "check": [
   "一隻豬在 T 輪中有幾種結局？",
   "p 隻豬能分辨幾個桶？為什麼？",
   "實際上要怎麼安排豬喝哪些桶？",
 ],
})
