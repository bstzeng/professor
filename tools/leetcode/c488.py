# -*- coding: utf-8 -*-
"""第 488、491、492、493、494、495 題。"""
import random
import itertools
import math
from collections import deque, Counter
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(488)
_DQ = {"deque": deque}


# ==================== 488. Zuma Game ====================
S["p488"] = '''class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def shrink(s: str) -> str:                 # 反覆消除連續 3 個以上的同色球
            changed = True
            while changed:
                changed = False
                i = 0
                while i < len(s):
                    j = i
                    while j < len(s) and s[j] == s[i]:
                        j += 1
                    if j - i >= 3:
                        s = s[:i] + s[j:]
                        changed = True
                        break
                    i = j
            return s

        start = (board, "".join(sorted(hand)))
        q = deque([(board, start[1], 0)])
        seen = {start}
        while q:                                   # ★ BFS：第一次清空就是最少步數
            b, h, step = q.popleft()
            for i in range(len(b) + 1):
                for j, ball in enumerate(h):
                    if j and h[j - 1] == ball:     # 手上相同顏色的球只試一次
                        continue
                    if i and b[i - 1] == ball:     # 插在同色球的左邊或右邊結果一樣：只試左邊
                        continue
                    # 剪枝：只有兩種插法有意義
                    #   1. 和右邊的球同色（湊成一組）
                    #   2. 插在兩個同色球中間把它們隔開（為了之後的連鎖）
                    if not (i < len(b) and (b[i] == ball or (i and b[i - 1] == b[i]))):
                        continue
                    nb = shrink(b[:i] + ball + b[i:])
                    if not nb:
                        return step + 1
                    nh = h[:j] + h[j + 1:]
                    if (nb, nh) not in seen:
                        seen.add((nb, nh))
                        q.append((nb, nh, step + 1))
        return -1'''

_p488 = S.load("p488", extra=_DQ)


def _zuma_ref(board, hand):
    def shrink(s):
        while True:
            m = None
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    m = (i, j)
                    break
                i = j
            if m is None:
                return s
            s = s[:m[0]] + s[m[1]:]

    start = (board, "".join(sorted(hand)))
    q = deque([(board, start[1], 0)])
    seen = {start}
    while q:
        b, h, d = q.popleft()
        for i in range(len(b) + 1):
            for j in range(len(h)):
                nb = shrink(b[:i] + h[j] + b[i:])
                if not nb:
                    return d + 1
                nh = h[:j] + h[j + 1:]
                if (nb, nh) not in seen:
                    seen.add((nb, nh))
                    q.append((nb, nh, d + 1))
    return -1


for b, h, want in [("WRRBBW", "RB", -1), ("WWRRBBWW", "WRBRW", 2), ("G", "GGGGG", 2), ("RRWWRRBBRR", "WB", 2)]:
    assert _p488.findMinStep(b, h) == want, (b, h)
for _ in range(400):
    b = "".join(random.choice("RGB") for _ in range(random.randint(1, 6)))
    # 題目保證初始盤面沒有連續三顆同色
    if any(b[i] == b[i + 1] == b[i + 2] for i in range(len(b) - 2)):
        continue
    h = "".join(random.choice("RGB") for _ in range(random.randint(1, 3)))
    assert _p488.findMinStep(b, h) == _zuma_ref(b, h), (b, h)
print("P488 OK")

emit({
 "num": 488, "slug": "zuma-game",
 "en": [
   "You are playing a variation of the game Zuma.",
   "In this variation of Zuma, there is a <strong>single row</strong> of colored balls on a board, where each ball can be colored red <code>'R'</code>, yellow <code>'Y'</code>, blue <code>'B'</code>, green <code>'G'</code>, or white <code>'W'</code>. You also have several colored balls in your hand.",
   "Your goal is to <strong>clear all</strong> of the balls from the board. On each turn:",
   ("ul", ["Pick <strong>any</strong> ball from your hand and insert it in between two balls in the row or on either end of the row.",
           "If there is a group of <strong>three or more consecutive balls</strong> of the <strong>same color</strong>, remove the group of balls from the board.",
           "If this removal causes more groups of three or more of the same color to form, then continue removing each group until there are none left.",
           "If there are no more balls on the board, then you win the game.",
           "Repeat this process until you either win or do not have any more balls in your hand."]),
   "Given a string <code>board</code>, representing the row of balls on the board, and a string <code>hand</code>, representing the balls in your hand, return <em>the <strong>minimum</strong> number of balls you have to insert to clear all the balls from the board. If you cannot clear all the balls from the board using the balls in your hand, return </em><code>-1</code>.",
 ],
 "zh": [
   "祖瑪遊戲的變形：板子上有一排彩色球（R、Y、B、G、W），你手上也有一些球。",
   "每一回合：從手上挑一顆球插到任意位置；如果出現<strong>連續三顆以上同色</strong>就消除，消除後產生的新組合也會<strong>連鎖</strong>消除。",
   "回傳清空板子<strong>最少</strong>要插幾顆球；做不到回傳 <code>-1</code>。",
 ],
 "examples": """範例 1
  輸入：board = "WRRBBW", hand = "RB"
  輸出：-1

範例 2
  輸入：board = "WWRRBBWW", hand = "WRBRW"
  輸出：2
  說明：插 R → WWRRRBBWW → WWBBWW；插 B → WWBBBWW → WWWW → 清空。

範例 3
  輸入：board = "G", hand = "GGGGG"
  輸出：2""",
 "constraints": [
   "1 ≤ <code>board.length</code> ≤ 16",
   "1 ≤ <code>hand.length</code> ≤ 5",
   "初始盤面沒有連續三顆同色的球",
 ],
 "idea": [
   ("c", """【最少步數 -> BFS】
    狀態 = (板子, 手上的球)，手上的球排序後當成多重集合。
    每一步：選一顆手上的球、選一個位置插入、做連鎖消除。

【狀態太多 -> 剪枝】
    1. 手上相同顏色的球只試一次
    2. 插在同色球的左邊或右邊，結果一樣 -> 只試其中一邊
    3. 只有兩種插法可能有用：
        a. 和旁邊的球同色（湊成一組）
        b. 插在兩顆同色球中間，把它們「隔開」
           —— 看起來沒用，但可能讓之後的連鎖消除成真。
           例：board = "RRWWRRBBRR"、hand = "WB"，答案是 2；
           如果只保留 (a)，BFS 會找不到解而回傳 -1（本頁實際測過）。

    注意：早期很多題解只保留 (a)，後來被證明是錯的（題目更新了測資）。

【連鎖消除】
    反覆找連續 >= 3 的同色段刪掉，直到找不到為止。"""),
 ],
 "approaches": [
   ap("解法", "BFS + 剪枝 + 連鎖消除", [
     ("c", S["p488"]),
     "驗證方式：和「不做任何剪枝、嘗試所有位置和所有球」的 BFS 暴力版本比對四百組隨機盤面。",
   ], "指數級（實際很快）", "指數級", "板長 ≤ 16、手上 ≤ 5 顆", "", optimal=True),
 ],
 "edges": [
   "<strong>手上的球不夠</strong> → −1。",
   "<strong>連鎖消除</strong> → 一次插入可能消掉很多組。",
   "<strong>需要先隔開同色球</strong> → 剪枝不能只保留「湊同色」的插法。",
 ],
 "follow": [
   ("h", "剪枝的正確性"),
   ("c", "設計剪枝時最容易犯的錯，是把「看起來沒用」的選擇剪掉。安全的做法：先寫不剪枝的暴力版本，每加一條剪枝就用隨機測試比對。"),
 ],
 "related": [
   "<strong>第 546 題 移除盒子</strong>",
   "<strong>第 1209 題 刪除字串中的所有相鄰重複項 II</strong> —— 連鎖消除",
 ],
 "check": [
   "BFS 的狀態是什麼？",
   "有哪些剪枝？為什麼「隔開同色球」的插法不能剪掉？",
   "連鎖消除要怎麼實作？",
 ],
})


# ==================== 491. Non-decreasing Subsequences ====================
S["p491"] = '''class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(start: int) -> None:
            if len(path) >= 2:
                res.append(path[:])
            used = set()                         # ★ 同一層（同一個位置）不選重複的值
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if path and nums[i] < path[-1]:  # 必須非遞減
                    continue
                used.add(nums[i])
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res'''

_p491 = S.load("p491")
for _ in range(1000):
    a = [random.randint(-2, 2) for _ in range(random.randrange(1, 9))]
    want = set()
    for r in range(2, len(a) + 1):
        for idx in itertools.combinations(range(len(a)), r):
            v = tuple(a[i] for i in idx)
            if all(v[t] <= v[t + 1] for t in range(r - 1)):
                want.add(v)
    got = _p491.findSubsequences(a)
    assert len(got) == len(want) and set(map(tuple, got)) == want, a
print("P491 OK")

emit({
 "num": 491, "slug": "non-decreasing-subsequences",
 "en": [
   "Given an integer array <code>nums</code>, return <em>all the different possible non-decreasing subsequences of the given array with at least two elements</em>. You may return the answer in <strong>any order</strong>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，回傳所有<strong>不同的</strong>、長度至少 2 的<strong>非遞減子序列</strong>，順序不限。",
 ],
 "examples": """範例 1
  輸入：nums = [4,6,7,7]
  輸出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

範例 2
  輸入：nums = [4,4,3,2,1]
  輸出：[[4,4]]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 15",
   "−100 ≤ <code>nums[i]</code> ≤ 100",
 ],
 "idea": [
   ("c", """【回溯產生子序列】
    每次從 start 往後挑下一個元素，必須 >= 目前路徑的最後一個。
    路徑長度 >= 2 就收進答案。

【去重的難點：不能排序】
    子序列要保持原本的順序 -> 不能像第 90 題那樣排序後跳過相鄰重複。

【同一層用集合去重】
    在同一個 dfs 呼叫（同一層）裡，
    如果某個值已經被選過當「下一個元素」，就不要再選 ——
    後面那個相同的值能產生的子序列，前面那個都已經產生過了。
    [4, 6, 7, 7]：
        在 [4, 6] 之後，第一個 7 和第二個 7 當下一個元素，
        會產生重複的 [4, 6, 7] -> 第二個跳過。
    但 [4, 6, 7] 之後再接第二個 7 是可以的（不同層）。"""),
 ],
 "approaches": [
   ap("解法", "回溯 + 同一層集合去重", [
     ("c", S["p491"]),
   ], "O(2ⁿ · n)", "O(n)", "", "遞迴深度，不計輸出", optimal=True),
 ],
 "edges": [
   "<strong>全部遞減</strong> → 只有相等的值能組成答案。",
   "<strong>重複值</strong> → 同一層只選一次。",
   "<strong>負數</strong> → 集合去重仍然有效。",
 ],
 "follow": [
   ("h", "「同一層去重」 vs 「排序後跳過」"),
   ("c", "能排序時（第 40、90 題），排序後跳過相鄰重複最簡單；不能排序時（本題），每一層開一個集合。"),
 ],
 "related": [
   "<strong>第 90 題 子集 II</strong>",
   "<strong>第 40 題 組合總和 II</strong>",
   "<strong>第 300 題 最長遞增子序列</strong>",
 ],
 "check": [
   "為什麼這題不能排序後去重？",
   "「同一層」用集合去重的原理是什麼？",
 ],
})


# ==================== 492. Construct the Rectangle ====================
S["p492"] = '''class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = math.isqrt(area)                 # ★ 從 √area 往下找第一個因數：長寬最接近
        while area % w:
            w -= 1
        return [area // w, w]'''

_p492 = S.load("p492")
for a in range(1, 5000):
    best = min(([a // w, w] for w in range(1, a + 1) if a % w == 0 and a // w >= w), key=lambda t: t[0] - t[1])
    assert _p492.constructRectangle(a) == best
print("P492 OK")

emit({
 "num": 492, "slug": "construct-the-rectangle",
 "en": [
   "A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area, your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:",
   ("ol", ["The area of the rectangular web page you designed must equal to the given target area.",
           "The width <code>W</code> should not be larger than the length <code>L</code>, which means <code>L &gt;= W</code>.",
           "The difference between length <code>L</code> and width <code>W</code> should be as small as possible."]),
   "Return <em>an array <code>[L, W]</code> where <code>L</code> and <code>W</code> are the length and width of the web page you designed in sequence.</em>",
 ],
 "zh": [
   "給你一個面積 <code>area</code>，設計一個長 <code>L</code>、寬 <code>W</code> 的長方形：面積剛好是 <code>area</code>，<code>L ≥ W</code>，而且 <code>L − W</code> 盡量小。回傳 <code>[L, W]</code>。",
 ],
 "examples": """範例 1
  輸入：area = 4
  輸出：[2,2]

範例 2
  輸入：area = 37
  輸出：[37,1]

範例 3
  輸入：area = 122122
  輸出：[427,286]""",
 "constraints": [
   "1 ≤ <code>area</code> ≤ 10⁷",
 ],
 "idea": [
   ("c", """【長寬越接近 √area，差距越小】
    W <= √area <= L。
    從 W = ⌊√area⌋ 往下找，第一個能整除 area 的 W，
    就是最接近 √area 的寬 -> L = area / W。

【最壞情況】
    area 是質數：一路找到 W = 1，O(√area)。"""),
 ],
 "approaches": [
   ap("解法", "從 √area 往下找因數", [
     ("c", S["p492"]),
   ], "O(√area)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>完全平方數</strong> → L = W。",
   "<strong>質數</strong> → [area, 1]。",
 ],
 "follow": [
   ("h", "因數成對出現"),
   ("c", "因數 d 和 area/d 分別落在 √area 的兩側——列舉因數只需要到 √area（第 204、319、1492 題也用到這個性質）。"),
 ],
 "related": [
   "<strong>第 1492 題 n 的第 k 個因數</strong>",
   "<strong>第 367 題 有效的完全平方數</strong>",
 ],
 "check": [
   "為什麼從 √area 往下找？",
   "最壞情況是什麼？",
 ],
})


# ==================== 493. Reverse Pairs ====================
S["p493"] = '''class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort(lo: int, hi: int) -> int:          # 排序 nums[lo:hi]，回傳其中的翻轉對數
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)
            # ★ 左右各自已排序：雙指標數「左邊 > 2 × 右邊」的對數
            j = mid
            for i in range(lo, mid):
                while j < hi and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - mid
            nums[lo:hi] = sorted(nums[lo:hi])       # 合併（用 sorted 簡化）
            return count

        return sort(0, len(nums))'''

S["p493_bit"] = '''class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        vals = sorted(set(nums))                    # 座標壓縮
        m = len(vals)
        tree = [0] * (m + 1)
        count = 0
        for i, x in enumerate(nums):
            # 前面有幾個數 > 2x：總數 - (<= 2x 的個數)
            r = bisect.bisect_right(vals, 2 * x)    # 名次 1..r 的值 <= 2x
            s, k = 0, r
            while k:
                s += tree[k]
                k -= k & -k
            count += i - s
            k = bisect.bisect_left(vals, x) + 1
            while k <= m:
                tree[k] += 1
                k += k & -k
        return count'''

_p493 = [S.load(x) for x in ("p493", "p493_bit")]
for nums, want in [([1, 3, 2, 3, 1], 2), ([2, 4, 3, 5, 1], 3)]:
    for sol in _p493:
        assert sol.reversePairs(list(nums)) == want
for _ in range(2000):
    a = [random.randint(-10, 10) for _ in range(random.randrange(1, 12))]
    want = sum(1 for i in range(len(a)) for j in range(i + 1, len(a)) if a[i] > 2 * a[j])
    for sol in _p493:
        assert sol.reversePairs(list(a)) == want, (a, sol)
print("P493 OK")

emit({
 "num": 493, "slug": "reverse-pairs",
 "en": [
   "Given an integer array <code>nums</code>, return <em>the number of <strong>reverse pairs</strong> in the array</em>.",
   "A <strong>reverse pair</strong> is a pair <code>(i, j)</code> where:",
   ("ul", ["<code>0 &lt;= i &lt; j &lt; nums.length</code> and",
           "<code>nums[i] &gt; 2 * nums[j]</code>."]),
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，回傳<strong>翻轉對</strong>的數量：<code>i &lt; j</code> 而且 <code>nums[i] &gt; 2 × nums[j]</code>。",
 ],
 "examples": """範例 1
  輸入：nums = [1,3,2,3,1]
  輸出：2
  說明：(1, 4)：3 > 2 × 1；(3, 4)：3 > 2 × 1

範例 2
  輸入：nums = [2,4,3,5,1]
  輸出：3""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 5 × 10⁴",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【逆序數（第 315 題）的變形】
    條件從 nums[i] > nums[j] 變成 nums[i] > 2 × nums[j]。

【合併排序】
    合併左右兩半之前，兩半各自已排序：
    對左邊每個 nums[i]，右邊滿足 nums[i] > 2 × nums[j] 的是一段前綴，
    而且 nums[i] 越大，這段前綴越長 -> 雙指標 O(n)。

    注意：計數和合併要分開做 ——
    合併的比較條件是 <=，計數的條件是 > 2×，兩者不同。

【樹狀陣列】
    從左往右，查詢「前面有幾個數 > 2x」，
    座標壓縮後用樹狀陣列。

【溢位（其他語言）】
    2 × nums[j] 可能超過 int 範圍，要用 long。"""),
 ],
 "approaches": [
   ap("解法一", "合併排序 + 雙指標計數", [
     ("c", S["p493"]),
   ], "O(n log n)", "O(n)", "", "", optimal=True),

   ap("解法二", "座標壓縮 + 樹狀陣列", [
     ("c", S["p493_bit"]),
   ], "O(n log n)", "O(n)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["暴力", "O(n²)", "超時"],
    ["一、合併排序", "O(n log n)", "✔"],
    ["二、樹狀陣列", "O(n log n)", "邊掃邊查"]]),
 "edges": [
   "<strong>負數</strong> → −3 &gt; 2 × (−2) = −4，成立；比較時不要用除法。",
   "<strong>2 × nums[j] 溢位</strong> → Python 沒問題，其他語言用 long。",
 ],
 "follow": [
   ("h", "逆序數家族"),
   ("c", "第 315 題（每個元素右邊比它小的）、第 327 題（區間和的個數）、第 493 題（本題）——合併排序和樹狀陣列兩種工具都通用。"),
 ],
 "related": [
   "<strong>第 315 題 計算右側小於當前元素的個數</strong>",
   "<strong>第 327 題 區間和的個數</strong>",
 ],
 "check": [
   "合併排序時，為什麼計數和合併要分開做？",
   "左邊的數越大，右邊合格的範圍怎麼變化？",
 ],
})


# ==================== 494. Target Sum ====================
S["p494"] = '''class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        # ★ 正號的集合 P、負號的集合 N：P - N = target，P + N = total
        #   -> P = (total + target) / 2，變成「湊出 P 有幾種方法」的 0/1 背包
        if abs(target) > total or (total + target) % 2:
            return 0
        P = (total + target) // 2
        dp = [1] + [0] * P                   # dp[s]：湊出 s 的方法數
        for x in nums:
            for s in range(P, x - 1, -1):    # 0/1 背包：由大到小
                dp[s] += dp[s - x]
        return dp[P]'''

S["p494_memo"] = '''class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.lru_cache(None)
        def ways(i: int, cur: int) -> int:   # 處理完前 i 個數、目前總和 cur
            if i == len(nums):
                return int(cur == target)
            return ways(i + 1, cur + nums[i]) + ways(i + 1, cur - nums[i])
        return ways(0, 0)'''

_p494 = [S.load(x) for x in ("p494", "p494_memo")]
for nums, t, want in [([1, 1, 1, 1, 1], 3, 5), ([1], 1, 1), ([0, 0, 1], 1, 4)]:
    for sol in _p494:
        assert sol.findTargetSumWays(nums, t) == want
for _ in range(1500):
    a = [random.randint(0, 4) for _ in range(random.randrange(1, 9))]
    t = random.randint(-8, 8)
    want = sum(1 for signs in itertools.product((1, -1), repeat=len(a)) if sum(s * x for s, x in zip(signs, a)) == t)
    for sol in _p494:
        assert sol.findTargetSumWays(a, t) == want, (a, t, sol)
print("P494 OK")

emit({
 "num": 494, "slug": "target-sum",
 "en": [
   "You are given an integer array <code>nums</code> and an integer <code>target</code>.",
   "You want to build an <strong>expression</strong> out of nums by adding one of the symbols <code>'+'</code> and <code>'-'</code> before each integer in nums and then concatenate all the integers.",
   ("ul", ["For example, if <code>nums = [2, 1]</code>, you can add a <code>'+'</code> before <code>2</code> and a <code>'-'</code> before <code>1</code> and concatenate them to build the expression <code>\"+2-1\"</code>."]),
   "Return the number of different <strong>expressions</strong> that you can build, which evaluates to <code>target</code>.",
 ],
 "zh": [
   "給你一個非負整數陣列 <code>nums</code> 和整數 <code>target</code>。在每個數前面加上 <code>+</code> 或 <code>-</code>，組成一個算式。",
   "回傳結果等於 <code>target</code> 的算式有幾種。",
 ],
 "examples": """範例 1
  輸入：nums = [1,1,1,1,1], target = 3
  輸出：5
  說明：-1+1+1+1+1、+1-1+1+1+1、+1+1-1+1+1、+1+1+1-1+1、+1+1+1+1-1

範例 2
  輸入：nums = [1], target = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 20",
   "0 ≤ <code>nums[i]</code> ≤ 1000",
   "0 ≤ <code>sum(nums)</code> ≤ 1000",
   "−1000 ≤ <code>target</code> ≤ 1000",
 ],
 "idea": [
   ("c", """【方法一：記憶化搜尋】
    狀態 (處理到第幾個數, 目前總和)，
    總和的範圍是 [-sum, sum] -> 最多 20 × 2001 個狀態。

【方法二：轉換成子集和（背包）】
    把加正號的數集合叫 P、負號的叫 N：
        P - N = target
        P + N = total
    相加：2P = total + target -> P = (total + target) / 2
    問題變成：挑一些數，總和剛好是 P，有幾種挑法？
    —— 0/1 背包計數。

    先判斷：total + target 必須是偶數，而且 |target| <= total。

【0 的處理】
    0 前面加 + 或 - 結果一樣，但算兩種算式。
    背包的 dp[s] += dp[s - 0] 會讓方法數自動加倍 ✔"""),
 ],
 "approaches": [
   ap("解法一", "記憶化搜尋", [
     ("c", S["p494_memo"]),
   ], "O(n · sum)", "O(n · sum)", "", ""),

   ap("解法二", "轉成子集和的 0/1 背包", [
     ("c", S["p494"]),
   ], "O(n · sum)", "O(sum)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["暴力 2ⁿ", "O(2ⁿ)", "O(n)"],
    ["一、記憶化", "O(n·sum)", "O(n·sum)"],
    ["二、背包", "O(n·sum)", "O(sum) ✔"]]),
 "edges": [
   "<strong>total + target 是奇數</strong> → 0。",
   "<strong>|target| &gt; total</strong> → 0。",
   "<strong>有 0</strong> → 每個 0 讓方法數加倍。",
 ],
 "follow": [
   ("h", "代數轉換"),
   ("c", "「給每個數選正負號」看起來是搜尋，但用 P − N、P + N 兩條方程式就能變成背包。第 1049 題（最後一塊石頭的重量 II）也是同一個轉換。"),
 ],
 "related": [
   "<strong>第 416 題 分割等和子集</strong>",
   "<strong>第 1049 題 最後一塊石頭的重量 II</strong>",
   "<strong>第 518 題 零錢兌換 II</strong>",
 ],
 "check": [
   "P 和 N 的關係式是什麼？怎麼推出 P？",
   "為什麼 total + target 必須是偶數？",
   "陣列中的 0 怎麼影響答案？",
 ],
})


# ==================== 495. Teemo Attacking ====================
S["p495"] = '''class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for a, b in zip(timeSeries, timeSeries[1:]):
            total += min(duration, b - a)      # ★ 下一次攻擊會「重置」中毒時間
        return total + duration                # 最後一次攻擊完整持續'''

_p495 = S.load("p495")
for _ in range(3000):
    ts = sorted(random.sample(range(0, 30), random.randrange(1, 8)))
    d = random.randint(0, 6)
    poisoned = set()
    for t in ts:
        poisoned.update(range(t, t + d))
    assert _p495.findPoisonedDuration(ts, d) == len(poisoned)
print("P495 OK")

emit({
 "num": 495, "slug": "teemo-attacking",
 "en": [
   "Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly <code>duration</code> seconds. More formally, an attack at second <code>t</code> will mean Ashe is poisoned during the <strong>inclusive</strong> time interval <code>[t, t + duration - 1]</code>. If Teemo attacks again <strong>before</strong> the poison effect ends, the timer for it is <strong>reset</strong>, and the poison effect will end <code>duration</code> seconds after the new attack.",
   "You are given a <strong>non-decreasing</strong> integer array <code>timeSeries</code>, where <code>timeSeries[i]</code> denotes that Teemo attacks Ashe at second <code>timeSeries[i]</code>, and an integer <code>duration</code>.",
   "Return <em>the <strong>total</strong> number of seconds that Ashe is poisoned</em>.",
 ],
 "zh": [
   "提摩用毒攻擊艾希：在第 <code>t</code> 秒攻擊，艾希會在 <code>[t, t + duration − 1]</code> 這段時間中毒。中毒還沒結束又被攻擊的話，計時會<strong>重置</strong>。",
   "給你非遞減的攻擊時間 <code>timeSeries</code> 和 <code>duration</code>，回傳艾希中毒的總秒數。",
 ],
 "examples": """範例 1
  輸入：timeSeries = [1,4], duration = 2
  輸出：4
  說明：[1,2] 和 [4,5]，共 4 秒。

範例 2
  輸入：timeSeries = [1,2], duration = 2
  輸出：3
  說明：[1,2] 被第 2 秒的攻擊重置成 [2,3]，合起來是 [1,3]，共 3 秒。""",
 "constraints": [
   "1 ≤ <code>timeSeries.length</code> ≤ 10⁴",
   "0 ≤ <code>timeSeries[i], duration</code> ≤ 10⁷",
   "<code>timeSeries</code> 非遞減",
 ],
 "idea": [
   ("c", """【每次攻擊實際貢獻多少秒？】
    下一次攻擊在 b，這次在 a：
        b - a >= duration -> 這次完整持續 duration 秒
        b - a <  duration -> 被下一次重置，只貢獻 b - a 秒
    所以每次貢獻 min(duration, b - a)。
    最後一次攻擊沒有人重置它 -> 完整 duration 秒。

【其實就是區間聯集的長度】
    每次攻擊是區間 [t, t + duration)，
    求這些區間聯集的總長度（第 56 題合併區間的簡化版）。"""),
 ],
 "approaches": [
   ap("解法", "相鄰攻擊的間隔", [
     ("c", S["p495"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>只攻擊一次</strong> → duration。",
   "<strong>同一秒攻擊兩次</strong> → 間隔 0，不重複計算。",
   "<strong>duration = 0</strong> → 0。",
 ],
 "follow": [
   ("h", "區間聯集"),
   ("c", "排序過的區間求聯集長度：只看相鄰兩個的重疊。區間沒排序時要先排序（第 56 題）。"),
 ],
 "related": [
   "<strong>第 56 題 合併區間</strong>",
   "<strong>第 605 題 種花問題</strong>",
 ],
 "check": [
   "每次攻擊實際貢獻的秒數怎麼算？",
   "為什麼最後一次攻擊要另外加 duration？",
 ],
})
