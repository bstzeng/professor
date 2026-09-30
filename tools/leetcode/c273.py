# -*- coding: utf-8 -*-
"""第 273、274、275、278、279、282 題。"""
import random
import itertools
from collections import deque
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(273)


# ==================== 273. Integer to English Words ====================
S["p273"] = '''class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        below20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                   "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen",
                   "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        def three(n: int) -> List[str]:          # 0..999 -> 單字串列
            words = []
            if n >= 100:
                words += [below20[n // 100], "Hundred"]
                n %= 100
            if n >= 20:
                words.append(tens[n // 10])
                n %= 10
            if n:
                words.append(below20[n])
            return words

        words = []
        # ★ 英文每三位一組：Billion, Million, Thousand, (個)
        for value, name in ((10 ** 9, "Billion"), (10 ** 6, "Million"), (1000, "Thousand"), (1, "")):
            chunk = num // value % 1000
            if chunk:                             # 這一組是 0 就整組略過
                words += three(chunk)
                if name:
                    words.append(name)
        return " ".join(words)'''

_p273 = S.load("p273")
for n, want in [(123, "One Hundred Twenty Three"), (12345, "Twelve Thousand Three Hundred Forty Five"),
                (1234567, "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"),
                (0, "Zero"), (1000000, "One Million"), (1000010, "One Million Ten"), (20, "Twenty"),
                (100, "One Hundred"), (2147483647, "Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"),
                (1000000001, "One Billion One"), (19, "Nineteen"), (110, "One Hundred Ten"), (50868, "Fifty Thousand Eight Hundred Sixty Eight")]:
    assert _p273.numberToWords(n) == want, (n, _p273.numberToWords(n))
for _ in range(3000):
    n = random.randrange(0, 2 ** 31)
    w = _p273.numberToWords(n)
    assert "  " not in w and w == w.strip()
print("P273 OK")

emit({
 "num": 273, "slug": "integer-to-english-words",
 "en": [
   "Convert a non-negative integer <code>num</code> to its English words representation.",
 ],
 "zh": [
   "把非負整數 <code>num</code> 轉換成英文的讀法。",
 ],
 "examples": """範例 1
  輸入：num = 123
  輸出："One Hundred Twenty Three"

範例 2
  輸入：num = 12345
  輸出："Twelve Thousand Three Hundred Forty Five"

範例 3
  輸入：num = 1234567
  輸出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven\"""",
 "constraints": [
   "0 ≤ <code>num</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【英文是「三位一組」的】
    2,147,483,647
    = 2 Billion  147 Million  483 Thousand  647
    每一組都是 0..999 的讀法，後面加上單位。
    （中文是四位一組：萬、億。）

【0..999 怎麼讀】
    百位：   n // 100 + "Hundred"
    剩下 0..99：
        >= 20：十位用 tens（Twenty, Thirty, ...），個位用 below20
        1..19：直接查表（Eleven..Nineteen 是不規則的）
        0：什麼都不加

【細節】
    - 某一組是 0 就整組略過：1,000,010 -> "One Million Ten"
      （不能出現 "Zero Thousand"）
    - 只有 num = 0 時輸出 "Zero"
    - 單字之間恰好一個空白：先收集成串列，最後 join

【拼字陷阱】
    Forty（不是 Fourty）、Fifteen、Eighteen（只有一個 t）、Ninety"""),
   ("t", ["組", "數值", "讀法"],
    [["Billion", "2", "Two Billion"],
     ["Million", "147", "One Hundred Forty Seven Million"],
     ["Thousand", "483", "Four Hundred Eighty Three Thousand"],
     ["（個）", "647", "Six Hundred Forty Seven"]]),
 ],
 "approaches": [
   ap("解法", "三位一組 + 查表", [
     ("c", S["p273"]),
   ], "O(1)", "O(1)", "最多 4 組、每組常數個字", "", optimal=True),
 ],
 "edges": [
   "<strong>0</strong> → \"Zero\"。",
   "<strong>整組為 0</strong>（1,000,000）→ \"One Million\"，後面不接任何東西。",
   "<strong>10..19</strong> → 不規則，查表。",
   "<strong>整十</strong>（20、100）→ 不能有多餘的空白。",
   "<strong>最大值</strong> 2,147,483,647 → 四組都有。",
 ],
 "follow": [
   ("h", "中文怎麼讀？"),
   ("c", "四位一組（萬、億），而且有「零」的規則：組內或組間有 0 要讀一個「零」（一萬零一），連續的 0 只讀一次。規則比英文複雜。"),
 ],
 "related": [
   "<strong>第 12 題 整數轉羅馬數字</strong>",
   "<strong>第 13 題 羅馬數字轉整數</strong>",
 ],
 "check": [
   "為什麼英文要三位一組處理？",
   "某一組是 0 時要怎麼處理？",
   "怎麼避免多餘的空白？",
 ],
})


# ==================== 274. H-Index ====================
S["p274_sort"] = '''class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)            # 由多到少
        h = 0
        # ★ 第 i 篇（0 起算）的引用數 >= i+1 -> 至少有 i+1 篇引用 >= i+1
        while h < len(citations) and citations[h] >= h + 1:
            h += 1
        return h'''

S["p274_count"] = '''class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        cnt = [0] * (n + 1)                     # cnt[k]：引用數恰為 k 的篇數（>= n 的都算在 n）
        for c in citations:
            cnt[min(c, n)] += 1
        total = 0                               # 引用數 >= h 的篇數
        for h in range(n, -1, -1):              # 從大到小試
            total += cnt[h]
            if total >= h:
                return h'''

_p274 = [S.load(x) for x in ("p274_sort", "p274_count")]


def _h_ref(c):
    return max(h for h in range(len(c) + 1) if sum(x >= h for x in c) >= h)


for c, want in [([3, 0, 6, 1, 5], 3), ([1, 3, 1], 1), ([0], 0), ([100], 1), ([0, 0], 0), ([11, 15], 2)]:
    for sol in _p274:
        assert sol.hIndex(list(c)) == want
for _ in range(3000):
    c = [random.randrange(0, 12) for _ in range(random.randrange(1, 12))]
    want = _h_ref(c)
    for sol in _p274:
        assert sol.hIndex(list(c)) == want
print("P274 OK")

_P274_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">引用數由大到小排序：[6, 5, 3, 1, 0]</text>
            <line x1="40" y1="200" x2="360" y2="200" stroke="var(--text-muted)"/>
            <g>
              <rect x="60" y="80" width="40" height="120" fill="var(--accent)" opacity="0.8"/>
              <rect x="120" y="100" width="40" height="100" fill="var(--accent)" opacity="0.8"/>
              <rect x="180" y="140" width="40" height="60" fill="var(--accent)" opacity="0.8"/>
              <rect x="240" y="180" width="40" height="20" fill="var(--text-muted)" opacity="0.6"/>
              <rect x="300" y="198" width="40" height="2" fill="var(--text-muted)"/>
            </g>
            <path d="M40 200 L360 93" stroke="#ff8a65" stroke-dasharray="5 4" fill="none"/>
            <text x="330" y="88" fill="#ff8a65" font-size="12">高度 = 篇數</text>
            <g font-size="12" fill="var(--text-muted)" text-anchor="middle">
              <text x="80" y="218">第1篇</text><text x="140" y="218">第2篇</text><text x="200" y="218">第3篇</text><text x="260" y="218">第4篇</text><text x="320" y="218">第5篇</text>
              <text x="80" y="74">6</text><text x="140" y="94">5</text><text x="200" y="134">3</text><text x="260" y="174">1</text><text x="320" y="192">0</text>
            </g>
            <rect x="40" y="140" width="180" height="60" fill="none" stroke="var(--gold)" stroke-width="2"/>
            <text x="400" y="100" fill="var(--gold)" font-size="12">h = 3：最大的正方形</text>
            <text x="400" y="122" fill="var(--text)" font-size="12">前 3 篇的引用數都 ≥ 3 ✔</text>
            <text x="400" y="144" fill="var(--text)" font-size="12">前 4 篇？第 4 篇只有 1 ✘</text>
            <text x="400" y="176" fill="var(--text-muted)" font-size="12">第 i 篇的高度 ≥ i 的最後一個 i</text>
            <text x="400" y="196" fill="var(--text-muted)" font-size="12">就是 h。</text>'''

emit({
 "num": 274, "slug": "h-index",
 "en": [
   "Given an array of integers <code>citations</code> where <code>citations[i]</code> is the number of citations a researcher received for their "
   "<code>i<sup>th</sup></code> paper, return <em>the researcher's h-index</em>.",
   "According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of <code>h</code> such that the given researcher "
   "has published at least <code>h</code> papers that have each been cited at least <code>h</code> times.",
 ],
 "zh": [
   "給你一個整數陣列 <code>citations</code>，<code>citations[i]</code> 是某位研究者第 <code>i</code> 篇論文被引用的次數。回傳這位研究者的 <strong>h 指數</strong>。",
   "h 指數的定義：最大的 <code>h</code>，使得這位研究者<strong>至少有 <code>h</code> 篇</strong>論文、每篇<strong>至少被引用 <code>h</code> 次</strong>。",
 ],
 "examples": """範例 1
  輸入：citations = [3,0,6,1,5]
  輸出：3
  說明：有 3 篇論文（3、6、5）被引用至少 3 次；
        要 h = 4 需要 4 篇至少被引用 4 次，但只有 2 篇。

範例 2
  輸入：citations = [1,3,1]
  輸出：1""",
 "constraints": [
   "<code>n == citations.length</code>",
   "1 ≤ <code>n</code> ≤ 5000",
   "0 ≤ <code>citations[i]</code> ≤ 1000",
 ],
 "idea": [
   ("fig", _P274_FIG, "0 0 640 232"),
   ("c", """【排序之後很直觀】
    由大到小排序：c[0] >= c[1] >= ...
    如果 c[h-1] >= h，代表前 h 篇都至少 h 次 -> h 可行。
    從 h = 1 往上試，找到最後一個可行的。

【圖形意義】
    把排序後的引用數畫成長條圖，
    h 是「能塞進長條圖左下角的最大正方形」的邊長。

【計數排序：O(n)】
    h 最多是 n（論文總數）。
    引用數 >= n 的論文，對 h 的判斷來說都一樣 -> 全部歸到 n 這一格。
    從 h = n 往下，累加「引用數 >= h 的篇數」，
    第一個滿足 total >= h 的 h 就是答案。"""),
 ],
 "approaches": [
   ap("解法一", "排序", [
     ("c", S["p274_sort"]),
   ], "O(n log n)", "O(1)", "", "原地排序"),

   ap("解法二", "計數排序", [
     ("c", S["p274_count"]),
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、排序", "O(n log n)", "O(1)"],
    ["二、計數", "O(n)", "O(n) ✔"]]),
 "edges": [
   "<strong>全部是 0</strong> → h = 0。",
   "<strong>只有一篇、引用很多</strong>（<code>[100]</code>）→ h = 1（受論文數限制）。",
   "<strong>每篇引用數都很大</strong> → h = n。",
 ],
 "follow": [
   ("h", "如果陣列已經排好序？"),
   ("c", "第 275 題：遞增排序的陣列上可以二分搜尋，O(log n)。"),
 ],
 "related": [
   "<strong>第 275 題 H 指數 II</strong>",
   "<strong>第 1608 題 特殊陣列的特徵值</strong> —— 幾乎相同的定義",
 ],
 "check": [
   "排序後怎麼判斷某個 h 是否可行？",
   "為什麼計數時可以把引用數 ≥ n 的都歸到 n？",
   "h 指數在長條圖上代表什麼？",
 ],
})


# ==================== 275. H-Index II ====================
S["p275"] = '''class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)                       # citations 遞增
        lo, hi = 0, n
        # 找第一個 i 使得 citations[i] >= n - i（從 i 到結尾共 n - i 篇）
        while lo < hi:
            mid = (lo + hi) // 2
            if citations[mid] >= n - mid:        # ★ 從 mid 開始的 n-mid 篇都 >= n-mid
                hi = mid
            else:
                lo = mid + 1
        return n - lo'''

_p275 = S.load("p275")
for c, want in [([0, 1, 3, 5, 6], 3), ([1, 2, 100], 2), ([0], 0), ([100], 1), ([0, 0, 0], 0)]:
    assert _p275.hIndex(c) == want
for _ in range(3000):
    c = sorted(random.randrange(0, 12) for _ in range(random.randrange(1, 12)))
    assert _p275.hIndex(c) == _h_ref(c), c
print("P275 OK")

emit({
 "num": 275, "slug": "h-index-ii",
 "en": [
   "Given an array of integers <code>citations</code> where <code>citations[i]</code> is the number of citations a researcher received for their "
   "<code>i<sup>th</sup></code> paper and <code>citations</code> is sorted in <strong>ascending order</strong>, return <em>the researcher's h-index</em>.",
   "You must write an algorithm that runs in logarithmic time.",
 ],
 "zh": [
   "和第 274 題相同，但 <code>citations</code> 已經<strong>遞增排序</strong>。",
   "必須在<strong>對數時間</strong>內完成。",
 ],
 "examples": """範例 1
  輸入：citations = [0,1,3,5,6]
  輸出：3

範例 2
  輸入：citations = [1,2,100]
  輸出：2""",
 "constraints": [
   "<code>n == citations.length</code>",
   "1 ≤ <code>n</code> ≤ 10⁵",
   "0 ≤ <code>citations[i]</code> ≤ 1000",
   "<code>citations</code> 遞增排序",
 ],
 "idea": [
   ("c", """【遞增排序時，從 i 到結尾有 n - i 篇】
    這 n - i 篇中最少的引用數就是 citations[i]。
    如果 citations[i] >= n - i -> h = n - i 可行。

【單調性】
    i 越大：citations[i] 越大、n - i 越小
    -> 條件 citations[i] >= n - i 一旦成立，之後都成立。
    FFFF...TTTT -> 二分找第一個 T。

    答案 h = n - (第一個 T 的位置)
    都不成立（lo = n）-> h = 0。

【範例】[0, 1, 3, 5, 6]，n = 5
    i:        0  1  2  3  4
    c[i]:     0  1  3  5  6
    n - i:    5  4  3  2  1
    c >= n-i: F  F  T  T  T
    第一個 T 在 i = 2 -> h = 5 - 2 = 3 ✔"""),
 ],
 "approaches": [
   ap("解法", "二分搜尋", [
     ("c", S["p275"]),
   ], "O(log n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>全部是 0</strong> → lo 停在 n，h = 0。",
   "<strong>全部都很大</strong> → lo = 0，h = n。",
   "<strong>重複值</strong> → 單調性不受影響。",
 ],
 "follow": [
   ("h", "二分搜尋的模板"),
   ("c", "「找第一個滿足條件的位置」：<code>lo, hi = 0, n</code>，條件成立時 <code>hi = mid</code>，否則 <code>lo = mid + 1</code>。區間 [lo, hi) 半開，結束時 lo == hi 就是答案（可能是 n，代表都不滿足）。"),
 ],
 "related": [
   "<strong>第 274 題 H 指數</strong>",
   "<strong>第 278 題 第一個錯誤的版本</strong> —— 同一個二分模板",
 ],
 "check": [
   "從 i 到結尾有幾篇論文？這些論文最少被引用幾次？",
   "條件為什麼有單調性？",
   "都不滿足時答案是多少？",
 ],
})


# ==================== 278. First Bad Version ====================
S["p278"] = '''# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n                        # 答案一定在 [lo, hi] 之間
        while lo < hi:
            mid = lo + (hi - lo) // 2        # ★ 其他語言避免 lo + hi 溢位
            if isBadVersion(mid):
                hi = mid                     # mid 可能就是第一個壞的，保留
            else:
                lo = mid + 1                 # mid 是好的，答案在右邊
        return lo'''

_calls = [0]
for n in list(range(1, 60)) + [2 ** 31 - 1]:
    bads = range(1, n + 1) if n < 60 else [1, 2 ** 30, n, 12345]
    for bad in bads:
        _calls[0] = 0

        def isBadVersion(v, bad=bad):
            _calls[0] += 1
            return v >= bad

        sol = S.load("p278", extra={"isBadVersion": isBadVersion})
        assert sol.firstBadVersion(n) == bad
        assert _calls[0] <= 32
print("P278 OK")

emit({
 "num": 278, "slug": "first-bad-version",
 "en": [
   "You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. "
   "Since each version is developed based on the previous version, all the versions after a bad version are also bad.",
   "Suppose you have <code>n</code> versions <code>[1, 2, ..., n]</code> and you want to find out the first bad one, which causes all the following ones to be bad.",
   "You are given an API <code>bool isBadVersion(version)</code> which returns whether <code>version</code> is bad. Implement a function to find the first bad version. "
   "You should minimize the number of calls to the API.",
 ],
 "zh": [
   "你是產品經理，最新版本沒有通過品質檢查。因為每個版本都基於前一個版本開發，<strong>某個壞掉的版本之後的所有版本也都是壞的</strong>。",
   "有 <code>n</code> 個版本 <code>[1, 2, ..., n]</code>，請找出<strong>第一個</strong>壞掉的版本。",
   "你可以呼叫 API <code>isBadVersion(version)</code> 判斷某個版本是否壞掉。請盡量<strong>減少 API 呼叫次數</strong>。",
 ],
 "examples": """範例 1
  輸入：n = 5, bad = 4
  輸出：4
  說明：
    isBadVersion(3) -> false
    isBadVersion(5) -> true
    isBadVersion(4) -> true
    所以 4 是第一個壞掉的版本。

範例 2
  輸入：n = 1, bad = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>bad</code> ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【版本狀態是單調的】
    好 好 好 ... 好 壞 壞 ... 壞
                    ^ 要找這個
    -> 二分搜尋「第一個壞的」。

【兩種更新】
    mid 是壞的 -> 第一個壞的在 mid 或更左邊 -> hi = mid（不能 mid - 1，mid 可能就是答案）
    mid 是好的 -> 第一個壞的在 mid 右邊     -> lo = mid + 1
    lo == hi 時就是答案。

【為什麼不會無窮迴圈？】
    mid = (lo + hi) // 2 偏左，所以 mid < hi：
        hi = mid 讓 hi 變小
        lo = mid + 1 讓 lo 變大
    區間每次都縮小 ✔

【溢位（其他語言）】
    n 可以到 2³¹ - 1，lo + hi 會超過 int 上限。
    寫成 lo + (hi - lo) / 2 ✔

【呼叫次數】
    ⌈log₂ n⌉ ≤ 31 次。"""),
 ],
 "approaches": [
   ap("解法", "二分搜尋", [
     ("c", S["p278"]),
   ], "O(log n)", "O(1)", "最多 31 次 API 呼叫", "", optimal=True),
 ],
 "edges": [
   "<strong>n = 1</strong> → 迴圈不執行，直接回傳 1。",
   "<strong>第一個版本就壞了</strong> → hi 一路縮到 1。",
   "<strong>只有最後一個壞</strong> → lo 一路推到 n。",
   "<strong>n = 2³¹ − 1</strong> → 其他語言注意 lo + hi 溢位。",
 ],
 "follow": [
   ("h", "真實世界：git bisect"),
   ("c", "git bisect 就是這一題：標記一個好的 commit、一個壞的 commit，它會自動二分挑出中間的 commit 讓你測試，幾次就能找出引入 bug 的那一個。"),
 ],
 "related": [
   "<strong>第 35 題 搜尋插入位置</strong>",
   "<strong>第 374 題 猜數字大小</strong>",
   "<strong>第 275 題 H 指數 II</strong>",
 ],
 "check": [
   "為什麼 mid 是壞的時候寫 <code>hi = mid</code> 而不是 <code>mid − 1</code>？",
   "為什麼不會無窮迴圈？",
   "其他語言中計算 mid 要注意什麼？",
 ],
})


# ==================== 279. Perfect Squares ====================
S["p279_dp"] = '''class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, math.isqrt(n) + 1)]
        dp = [0] + [n] * n                  # dp[x]：組成 x 最少要幾個平方數
        for x in range(1, n + 1):
            for s in squares:
                if s > x:
                    break
                dp[x] = min(dp[x], dp[x - s] + 1)   # ★ 最後一個平方數是 s
        return dp[n]'''

S["p279_bfs"] = '''class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, math.isqrt(n) + 1)]
        level, frontier, seen = 0, {n}, {n}
        while frontier:
            level += 1                      # 再用一個平方數
            nxt = set()
            for x in frontier:
                for s in squares:
                    if s > x:
                        break
                    if s == x:
                        return level        # ★ 剛好減到 0：BFS 第一次到達就是最少
                    if x - s not in seen:
                        seen.add(x - s)
                        nxt.add(x - s)
            frontier = nxt
        return level'''

S["p279_math"] = '''class Solution:
    def numSquares(self, n: int) -> int:
        def is_square(x: int) -> bool:
            r = math.isqrt(x)
            return r * r == x

        if is_square(n):                    # 1 個
            return 1
        m = n
        while m % 4 == 0:                   # 去掉 4 的因數
            m //= 4
        if m % 8 == 7:                      # ★ 勒讓德三平方定理：4^a(8b+7) 需要 4 個
            return 4
        for i in range(1, math.isqrt(n) + 1):
            if is_square(n - i * i):        # 2 個
                return 2
        return 3                            # 其他都是 3 個'''

_p279 = [S.load(x) for x in ("p279_dp", "p279_bfs", "p279_math")]
_ref = [0] * 3001
for x in range(1, 3001):
    _ref[x] = min(_ref[x - i * i] + 1 for i in range(1, int(x ** 0.5) + 1))
for n in range(1, 3001):
    assert _p279[2].numSquares(n) == _ref[n], n
    if n % 11 == 0 or n < 200:
        assert _p279[0].numSquares(n) == _ref[n] and _p279[1].numSquares(n) == _ref[n], n
print("P279 OK")

emit({
 "num": 279, "slug": "perfect-squares",
 "en": [
   "Given an integer <code>n</code>, return <em>the least number of perfect square numbers that sum to</em> <code>n</code>.",
   "A <strong>perfect square</strong> is an integer that is the square of an integer; in other words, it is the product of some integer with itself. "
   "For example, <code>1</code>, <code>4</code>, <code>9</code>, and <code>16</code> are perfect squares while <code>3</code> and <code>11</code> are not.",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，回傳<strong>和為 <code>n</code> 的完全平方數的最少個數</strong>。",
   "<strong>完全平方數</strong>是某個整數的平方，例如 <code>1</code>、<code>4</code>、<code>9</code>、<code>16</code>；<code>3</code> 和 <code>11</code> 則不是。",
 ],
 "examples": """範例 1
  輸入：n = 12
  輸出：3
  說明：12 = 4 + 4 + 4

範例 2
  輸入：n = 13
  輸出：2
  說明：13 = 4 + 9""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【完全背包】
    物品：1, 4, 9, 16, ...（每個可以用無限次）
    目標：湊出 n，物品個數最少。
    和第 322 題「零錢兌換」一模一樣。

    dp[x] = min(dp[x - s] + 1)  對所有平方數 s <= x

【貪心不行】
    12：先拿最大的 9，剩 3 = 1+1+1 -> 4 個
    但 4 + 4 + 4 只要 3 個 ✘

【BFS：最少步數】
    從 n 出發，每一步減掉一個平方數，
    第一次走到 0 的層數就是答案。

【數學：答案只可能是 1、2、3、4】
    拉格朗日四平方定理：每個正整數都能寫成 4 個平方數的和。
    勒讓德三平方定理：n 需要 4 個 <=> n = 4^a × (8b + 7)。
    所以：
        n 是平方數              -> 1
        n = 4^a(8b+7)           -> 4
        n = i² + j² 有解        -> 2
        其他                    -> 3"""),
 ],
 "approaches": [
   ap("解法一", "動態規劃（完全背包）", [
     ("c", S["p279_dp"]),
   ], "O(n√n)", "O(n)", "", ""),

   ap("解法二", "BFS", [
     ("c", S["p279_bfs"]),
     "每一層代表多用一個平方數。答案最多 4，所以最多 4 層；但每層節點可能很多，實際速度和 DP 差不多。",
   ], "O(n√n)", "O(n)", "", ""),

   ap("解法三", "數論（四平方定理 + 三平方定理）", [
     ("c", S["p279_math"]),
   ], "O(√n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、DP", "O(n√n)", "O(n)", "通用"],
    ["二、BFS", "O(n√n)", "O(n)", "最少步數"],
    ["三、數論", "O(√n)", "O(1)", "最快 ✔"]]),
 "edges": [
   "<strong>n 本身是平方數</strong> → 1。",
   "<strong>n = 7</strong> → 4 + 1 + 1 + 1 = 4 個（8b+7 型）。",
   "<strong>n = 12</strong> → 貪心會錯。",
 ],
 "follow": [
   ("h", "Python 的效能"),
   ("c", "解法一在 Python 中 n = 10⁴ 約 10⁶ 次運算，可以過但偏慢；常見的加速是把 dp 寫成類別層級的靜態陣列，多個測資共用。"),
 ],
 "related": [
   "<strong>第 322 題 零錢兌換</strong> —— 同一個完全背包",
   "<strong>第 518 題 零錢兌換 II</strong> —— 計算方法數",
   "<strong>第 204 題 計數質數</strong> —— 另一題數論",
 ],
 "check": [
   "這題為什麼是完全背包？",
   "為什麼貪心（每次拿最大的平方數）會錯？舉例。",
   "為什麼答案最多是 4？什麼樣的數需要 4 個？",
 ],
})


# ==================== 282. Expression Add Operators ====================
S["p282"] = '''class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        n = len(num)

        def dfs(i: int, expr: str, value: int, last: int):
            # value：目前算式的值；last：最後一「項」（乘法會改到它）
            if i == n:
                if value == target:
                    res.append(expr)
                return
            for j in range(i, n):
                if j > i and num[i] == "0":            # ★ 不能有前導零（"05" 不是合法數字）
                    break
                s = num[i:j + 1]
                x = int(s)
                if i == 0:                             # 第一個數字前面不能放運算子
                    dfs(j + 1, s, x, x)
                else:
                    dfs(j + 1, expr + "+" + s, value + x, x)
                    dfs(j + 1, expr + "-" + s, value - x, -x)
                    # ★ 乘法：撤銷上一項，改成 上一項 × x
                    dfs(j + 1, expr + "*" + s, value - last + last * x, last * x)

        dfs(0, "", 0, 0)
        return res'''

_p282 = S.load("p282")


def _eval282(e):
    import re as _re
    terms, op = [], "+"
    for tok in _re.findall(r"\d+|[-+*]", e):
        if tok in "+-*":
            op = tok
            continue
        v = int(tok)
        if op == "*":
            terms.append(terms.pop() * v)
        else:
            terms.append(v if op == "+" else -v)
    return sum(terms)


def _ref282(num, target):
    out = []
    for ops in itertools.product(["", "+", "-", "*"], repeat=len(num) - 1):
        e = num[0] + "".join(o + d for o, d in zip(ops, num[1:]))
        import re as _re
        if any(len(t) > 1 and t[0] == "0" for t in _re.findall(r"\d+", e)):
            continue
        if _eval282(e) == target:
            out.append(e)
    return sorted(out)


for num, t, want in [("123", 6, ["1*2*3", "1+2+3"]), ("232", 8, ["2*3+2", "2+3*2"]), ("3456237490", 9191, []),
                     ("105", 5, ["1*0+5", "10-5"]), ("00", 0, ["0*0", "0+0", "0-0"])]:
    assert sorted(_p282.addOperators(num, t)) == sorted(want), (num, t)
for _ in range(300):
    num = "".join(random.choice("0123456789") for _ in range(random.randrange(1, 7)))
    t = random.randrange(-30, 60)
    assert sorted(_p282.addOperators(num, t)) == _ref282(num, t), (num, t)
print("P282 OK")

emit({
 "num": 282, "slug": "expression-add-operators",
 "en": [
   "Given a string <code>num</code> that contains only digits and an integer <code>target</code>, return <em><strong>all possibilities</strong> to insert the binary operators "
   "</em><code>'+'</code><em>, </em><code>'-'</code><em>, and/or </em><code>'*'</code><em> between the digits of </em><code>num</code><em> so that the resultant expression evaluates to the </em><code>target</code><em> value</em>.",
   "Note that operands in the returned expressions <strong>should not</strong> contain leading zeros.",
 ],
 "zh": [
   "給你一個只包含數字的字串 <code>num</code> 和整數 <code>target</code>。在數字之間插入 <code>'+'</code>、<code>'-'</code>、<code>'*'</code>（也可以不插，讓相鄰數字合成多位數），"
   "回傳<strong>所有</strong>計算結果等於 <code>target</code> 的算式。",
   "運算元<strong>不能有前導零</strong>（例如 <code>\"05\"</code> 不合法，但單獨的 <code>\"0\"</code> 可以）。",
 ],
 "examples": """範例 1
  輸入：num = "123", target = 6
  輸出：["1*2*3","1+2+3"]

範例 2
  輸入：num = "232", target = 8
  輸出：["2*3+2","2+3*2"]

範例 3
  輸入：num = "3456237490", target = 9191
  輸出：[]""",
 "constraints": [
   "1 ≤ <code>num.length</code> ≤ 10",
   "<code>num</code> 只包含數字",
   "−2³¹ ≤ <code>target</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【回溯：每一步決定「下一個運算元有多長」和「前面放什麼運算子」】
    num = "123"：
        1 | 2 | 3、12 | 3、1 | 23、123
    每個切點之間可以放 + - *。

【難點：乘法的優先順序】
    邊走邊算 value 時，遇到乘法不能直接 value * x：
        1 + 2 * 3 ≠ (1 + 2) * 3
    解法：多記一個 last = 最後一「項」的值（含正負號）。
        1 + 2       value = 3, last = 2
        1 + 2 * 3   撤銷 last：value - last = 1
                    新的 last = 2 * 3 = 6
                    value = 1 + 6 = 7 ✔

    減法：last = -x，所以 1 - 2 * 3 也正確：
        value = -1, last = -2 -> value = -1 - (-2) + (-6) = -5 ✔

【前導零】
    從 num[i] 開始切，如果 num[i] == '0'，只能切出單獨的 "0"。

【複雜度】
    n-1 個切點，每個有 4 種選擇（不切、+、-、*）-> O(4ⁿ)，
    再乘上每次組字串 O(n)。n ≤ 10 -> 4¹⁰ ≈ 10⁶，可以接受。"""),
 ],
 "approaches": [
   ap("解法", "回溯 + 記錄最後一項", [
     ("c", S["p282"]),
     ("c", """【模擬】num = "232", target = 8

    2                      value=2,  last=2
    2+3                    value=5,  last=3
    2+3*2                  value=5-3+6=8 ✔
    2*3                    value=2-2+6=6, last=6
    2*3+2                  value=8 ✔
    23                     value=23, last=23
    ..."""),
   ], "O(n · 4ⁿ)", "O(n)", "", "遞迴深度，不計輸出", optimal=True),
 ],
 "edges": [
   "<strong>前導零</strong>（<code>\"105\"</code>）→ \"1*05\" 不合法，但 \"1*0+5\" 可以。",
   "<strong>全是 0</strong>（<code>\"00\"</code>, 0）→ \"0+0\"、\"0-0\"、\"0*0\"；\"00\" 不合法。",
   "<strong>大數</strong>（\"9999999999\"）→ Python 沒有溢位問題；其他語言用 long。",
   "<strong>只有一位數</strong> → 只有它本身。",
 ],
 "follow": [
   ("h", "為什麼只需要記「最後一項」？"),
   ("c", "乘法只會和緊鄰在它左邊的那一項結合；更早的項已經被 + 或 − 隔開，不會再改變。這和第 227 題「只保留最後一項」的想法相同。"),
 ],
 "related": [
   "<strong>第 227 題 基本計算器 II</strong> —— 同樣的「最後一項」技巧",
   "<strong>第 241 題 為運算式設計優先順序</strong>",
   "<strong>第 494 題 目標和</strong> —— 只有 + 和 −",
 ],
 "check": [
   "為什麼遇到乘法不能直接 value × x？",
   "<code>last</code> 代表什麼？做乘法時怎麼更新？",
   "前導零要怎麼處理？",
 ],
})
