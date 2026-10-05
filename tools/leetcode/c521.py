# -*- coding: utf-8 -*-
"""第 521、522、523、524、525、526、528、529 題。"""
import random
from collections import Counter
from functools import lru_cache
from itertools import combinations, permutations
from authoring import ap
from lcauto import em
from runner import Src

S = Src()
random.seed(521)


def _is_sub(a, b):
    it = iter(b)
    return all(c in it for c in a)


# ==================== 521. Longest Uncommon Subsequence I ====================
S["p521"] = '''class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        # ★ 兩字串不同時，較長的那個（或任一個，若等長）本身就不是另一個的子序列
        return -1 if a == b else max(len(a), len(b))'''

_p521 = S.load("p521")
def _bf521(a, b):
    best = -1
    for s in (a, b):
        o = b if s is a else a
        for L in range(1, len(s) + 1):
            for idx in combinations(range(len(s)), L):
                t = "".join(s[i] for i in idx)
                if not _is_sub(t, o):
                    best = max(best, L)
    return best
for _ in range(1500):
    a = "".join(random.choice("ab") for _ in range(random.randint(1, 5)))
    b = "".join(random.choice("ab") for _ in range(random.randint(1, 5)))
    assert _p521.findLUSlength(a, b) == _bf521(a, b)
print("P521 OK")

em({
 "num": 521, "title": "最長特殊序列 I",
 "desc": "腦筋急轉彎：兩字串不同時，較長的那個整個就是答案；相同則 −1。",
 "zh": [
   "給你兩個字串 <code>a</code> 和 <code>b</code>，回傳它們之間<strong>最長特殊序列</strong>的長度；不存在則回傳 <code>-1</code>。",
   "<strong>特殊序列</strong>：是其中一個字串的子序列，但<strong>不是</strong>另一個字串的子序列。",
 ],
 "idea": [
   ("c", """【看起來要枚舉子序列，其實不用】
    a == b：任何 a 的子序列都是 b 的子序列 -> -1。
    a != b：
        若 len(a) > len(b)：a 不可能是較短的 b 的子序列 -> a 本身就是答案。
        若等長但不同：a 不是 b 的子序列（等長的子序列只能是它自己）。
    整個字串是自己最長的子序列 -> 答案 max(len(a), len(b))。"""),
 ],
 "approaches": [
   ap("解法", "比較兩字串", [("c", S["p521"]), "驗證方式：和枚舉所有子序列的暴力法比對 1500 組。"], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": ["<strong>a == b</strong> → −1。", "<strong>等長但不同</strong> → 長度本身。"],
 "follow": [("h", "多個字串？"), ("c", "第 522 題：字串變多時，「最長的那個」可能是別人的子序列，就要真的檢查了。")],
 "related": ["<strong>第 522 題 最長特殊序列 II</strong>", "<strong>第 392 題 判斷子序列</strong>"],
 "check": ["為什麼較長的字串不可能是較短字串的子序列？", "等長但不同的情況為什麼也成立？"],
})


# ==================== 522. Longest Uncommon Subsequence II ====================
S["p522"] = '''class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub(s, t):                       # s 是不是 t 的子序列
            it = iter(t)
            return all(c in it for c in s)      # ★ 每個 c 在迭代器中往後找，找到後迭代器停在那裡

        res = -1
        for i, s in enumerate(strs):
            # 答案一定是某個完整的字串：只要它不是任何其他字串的子序列
            if all(i == j or not is_sub(s, t) for j, t in enumerate(strs)):
                res = max(res, len(s))
        return res'''

_p522 = S.load("p522")
def _bf522(strs):
    best = -1
    for i, s in enumerate(strs):
        for L in range(1, len(s) + 1):
            for idx in combinations(range(len(s)), L):
                t = "".join(s[k] for k in idx)
                if all(j == i or not _is_sub(t, o) for j, o in enumerate(strs)):
                    best = max(best, L)
    return best
for _ in range(800):
    strs = ["".join(random.choice("ab") for _ in range(random.randint(1, 4))) for _ in range(random.randint(2, 4))]
    assert _p522.findLUSlength(strs) == _bf522(strs), strs
print("P522 OK")

em({
 "num": 522, "title": "最長特殊序列 II",
 "desc": "如果某個子序列是特殊的，包含它的完整字串也是特殊的——所以只需要檢查每個完整字串。",
 "zh": [
   "給你字串陣列 <code>strs</code>，回傳<strong>最長特殊序列</strong>的長度；不存在則回傳 <code>-1</code>。",
   "<strong>特殊序列</strong>：是某一個字串的子序列，但不是<strong>其他任何</strong>字串的子序列。",
 ],
 "idea": [
   ("c", """【關鍵：只要看完整的字串】
    若 t 是 strs[i] 的子序列，而且不是其他任何字串的子序列，
    那 strs[i] 本身也不是其他字串的子序列
    （否則 t ⊆ strs[i] ⊆ 某字串，t 也會是它的子序列）。
    而 strs[i] 比 t 更長 -> 只需檢查每個完整字串。

【做法】
    對每個 strs[i]，檢查它是不是其他任何字串的子序列；
    不是的話，len(strs[i]) 是一個候選答案。

【子序列判斷：雙指標 / 迭代器】
    it = iter(t); all(c in it for c in s)
    'c in it' 會消耗迭代器直到找到 c，正好是貪心雙指標。"""),
 ],
 "approaches": [
   ap("解法", "檢查每個完整字串", [("c", S["p522"]), "驗證方式：和枚舉所有子序列的暴力法比對 800 組。"], "O(n² · L)", "O(1)", "n 個字串、長度 L", "", optimal=True),
 ],
 "edges": ["<strong>重複的字串</strong> → 互為子序列，都不能當答案。", "<strong>全部都是某個字串的子序列</strong> → −1。"],
 "follow": [("h", "最佳化"), ("c", "可以依長度由大到小排序，第一個符合的就是答案，提早結束。")],
 "related": ["<strong>第 521 題 最長特殊序列 I</strong>", "<strong>第 392 題 判斷子序列</strong>", "<strong>第 524 題 通過刪除字母匹配到字典裡最長單字</strong>"],
 "check": ["為什麼只需要檢查完整的字串？", "iter + in 的寫法如何實現子序列判斷？"],
})


# ==================== 523. Continuous Subarray Sum ====================
S["p523"] = '''class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        first = {0: -1}                 # 前綴和 mod k -> 第一次出現的位置（空前綴在 -1）
        s = 0
        for i, x in enumerate(nums):
            s = (s + x) % k
            if s in first:
                if i - first[s] >= 2:   # ★ 兩個前綴和同餘 -> 中間那段的和是 k 的倍數；長度至少 2
                    return True
            else:
                first[s] = i            # 只記第一次：讓子陣列盡量長
        return False'''

_p523 = S.load("p523")
for _ in range(3000):
    a = [random.randint(0, 6) for _ in range(random.randint(1, 8))]; k = random.randint(1, 7)
    want = any(sum(a[i:j]) % k == 0 for i in range(len(a)) for j in range(i + 2, len(a) + 1))
    assert _p523.checkSubarraySum(a, k) == want
print("P523 OK")

em({
 "num": 523, "title": "連續的子陣列和",
 "desc": "前綴和同餘定理：兩個前綴和除以 k 的餘數相同，中間那段就是 k 的倍數；記第一次出現的位置保證長度。",
 "zh": [
   "給你整數陣列 <code>nums</code> 和整數 <code>k</code>，判斷是否存在<strong>長度至少為 2</strong> 的連續子陣列，其元素總和是 <code>k</code> 的倍數。",
   "（0 也算是 k 的倍數。）",
 ],
 "idea": [
   ("c", """【前綴和】
    子陣列 nums[i+1..j] 的和 = P[j] - P[i]。
    它是 k 的倍數 <=> P[j] ≡ P[i] (mod k)。

【雜湊表記「餘數第一次出現的位置」】
    掃到 j 時，若 P[j] mod k 之前出現過（在位置 i），
    且 j - i >= 2，就找到了。
    只記第一次出現：讓 i 盡量小，子陣列盡量長。

【空前綴】
    first[0] = -1：讓「從頭開始的子陣列」也能被找到。
    例如 [2, 4], k=6：P = 2, 6 -> 6%6 = 0，和 first[0] = -1 相距 2。"""),
 ],
 "approaches": [
   ap("解法", "前綴和餘數 + 雜湊表", [("c", S["p523"])], "O(n)", "O(min(n, k))", optimal=True),
 ],
 "edges": ["<strong>[0, 0]</strong> → True（0 是任何 k 的倍數）。", "<strong>單一元素是 k 的倍數</strong> → 不算（長度至少 2）。", "<strong>覆蓋 first</strong> → 錯誤：會讓長度變短。"],
 "follow": [("h", "前綴和 + 雜湊表家族"), ("c", "第 560 題（和為 k 的個數：記次數）、第 974 題（和可被 k 整除的個數：記餘數次數）、第 525 題（0 和 1 個數相同：記第一次位置）。")],
 "related": ["<strong>第 560 題 和為 K 的子陣列</strong>", "<strong>第 974 題 和可被 K 整除的子陣列</strong>", "<strong>第 525 題 連續陣列</strong>"],
 "check": ["為什麼兩個同餘的前綴和代表中間是 k 的倍數？", "為什麼只記錄第一次出現的位置？", "first[0] = -1 的作用是什麼？"],
})


# ==================== 524. Longest Word in Dictionary through Deleting ====================
S["p524"] = '''class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        best = ""
        for w in dictionary:
            # 比較條件：更長，或一樣長但字典序更小
            if len(w) > len(best) or (len(w) == len(best) and w < best):
                it = iter(s)
                if all(c in it for c in w):     # ★ w 是 s 的子序列（雙指標）
                    best = w
        return best'''

_p524 = S.load("p524")
assert _p524.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]) == "apple"
assert _p524.findLongestWord("abpcplea", ["a", "b", "c"]) == "a"
for _ in range(1500):
    s = "".join(random.choice("abc") for _ in range(random.randint(1, 8)))
    d = ["".join(random.choice("abc") for _ in range(random.randint(1, 4))) for _ in range(random.randint(1, 5))]
    cand = sorted((w for w in d if _is_sub(w, s)), key=lambda w: (-len(w), w))
    assert _p524.findLongestWord(s, d) == (cand[0] if cand else "")
print("P524 OK")

em({
 "num": 524, "title": "通過刪除字母匹配到字典裡最長單字",
 "desc": "對每個字典單字做子序列判斷，依「長度大、字典序小」挑最好的；先比較再檢查能省時間。",
 "zh": [
   "給你字串 <code>s</code> 和字串陣列 <code>dictionary</code>，找出字典中<strong>最長</strong>、而且可以由 <code>s</code> 刪除一些字元得到的單字。",
   "若有多個，回傳<strong>字典序最小</strong>的；都不行則回傳空字串。",
 ],
 "idea": [
   ("c", """【「刪除一些字元得到」= 子序列】
    逐一檢查每個單字是不是 s 的子序列（雙指標 O(|s|)）。

【挑最好的】
    更長的優先；一樣長時字典序小的優先。

【小最佳化】
    先比較「這個單字有沒有可能比目前答案好」，
    有可能才做子序列檢查，省掉很多無用功。

【另一種寫法】
    先依 (-長度, 字典序) 排序字典，第一個是子序列的就是答案。"""),
 ],
 "approaches": [
   ap("解法", "逐一子序列判斷", [("c", S["p524"])], "O(d · |s|)", "O(1)", "d 為字典大小", "", optimal=True),
 ],
 "edges": ["<strong>沒有任何單字符合</strong> → \"\"。", "<strong>同長度比字典序</strong> → \"a\" 勝過 \"b\"。"],
 "follow": [("h", "字典很大時"), ("c", "預處理 s：next[i][c] = 位置 i 之後第一個字元 c 的位置。之後每個單字的子序列判斷只要 O(|w|)，和第 792 題（匹配子序列的單字數）相同。")],
 "related": ["<strong>第 392 題 判斷子序列</strong>", "<strong>第 792 題 匹配子序列的單字數</strong>", "<strong>第 720 題 字典中最長的單字</strong>"],
 "check": ["「刪除一些字元」等於哪個概念？", "為什麼先比較長度再做子序列檢查？"],
})


# ==================== 525. Contiguous Array ====================
S["p525"] = '''class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        first = {0: -1}                 # 差值 -> 第一次出現的位置
        bal = res = 0
        for i, x in enumerate(nums):
            bal += 1 if x == 1 else -1  # ★ 把 0 看成 -1：0 和 1 一樣多 <=> 總和為 0
            if bal in first:
                res = max(res, i - first[bal])
            else:
                first[bal] = i
        return res'''

_p525 = S.load("p525")
for _ in range(3000):
    a = [random.randint(0, 1) for _ in range(random.randint(1, 10))]
    want = max([j - i for i in range(len(a)) for j in range(i + 1, len(a) + 1) if 2 * sum(a[i:j]) == j - i] + [0])
    assert _p525.findMaxLength(a) == want
print("P525 OK")

em({
 "num": 525, "title": "連續陣列",
 "desc": "把 0 換成 −1，問題變成「和為 0 的最長子陣列」：前綴和第一次出現的位置。",
 "zh": ["給你一個只含 <code>0</code> 和 <code>1</code> 的陣列 <code>nums</code>，回傳 0 和 1 數量相同的<strong>最長連續子陣列</strong>長度。"],
 "idea": [
   ("c", """【轉換】
    把 0 看成 -1。子陣列中 0 和 1 一樣多 <=> 和為 0。

【和為 0 的最長子陣列】
    前綴和 P[j] == P[i] -> nums[i+1..j] 的和為 0，長度 j - i。
    要最長 -> 每個前綴和只記錄第一次出現的位置。
    空前綴：first[0] = -1。

    和第 523 題是同一個模板。"""),
 ],
 "approaches": [
   ap("解法", "前綴和 + 第一次出現位置", [("c", S["p525"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>全是 0 或全是 1</strong> → 0。", "<strong>整個陣列平衡</strong> → 靠 first[0] = -1 抓到長度 n。"],
 "follow": [("h", "陣列代替雜湊表"), ("c", "前綴和的範圍是 [−n, n]，可以用長度 2n+1 的陣列（加上偏移 n）代替雜湊表，常數更小。")],
 "related": ["<strong>第 523 題 連續的子陣列和</strong>", "<strong>第 560 題 和為 K 的子陣列</strong>", "<strong>第 1124 題 表現良好的最長時間段</strong>"],
 "check": ["為什麼把 0 換成 −1？", "為什麼 first[0] = −1？"],
})


# ==================== 526. Beautiful Arrangement ====================
S["p526"] = '''class Solution:
    def countArrangement(self, n: int) -> int:
        @cache
        def dfs(mask):
            i = bin(mask).count("1") + 1        # 已經放了幾個數 -> 現在要填第 i 個位置
            if i > n:
                return 1
            total = 0
            for x in range(1, n + 1):
                # ★ x 還沒用過，而且和位置 i 互相整除
                if not mask >> (x - 1) & 1 and (x % i == 0 or i % x == 0):
                    total += dfs(mask | 1 << (x - 1))
            return total
        return dfs(0)'''

_p526 = S.load("p526", extra={"cache": lru_cache(None)})
for n in range(1, 9):
    want = sum(all(p[i] % (i + 1) == 0 or (i + 1) % p[i] == 0 for i in range(n)) for p in permutations(range(1, n + 1)))
    assert _p526.countArrangement(n) == want
assert _p526.countArrangement(15) == 24679
print("P526 OK")

em({
 "num": 526, "title": "優美的排列",
 "desc": "依位置逐一填數的回溯，用位元遮罩記錄用過的數並記憶化：O(n · 2ⁿ)。",
 "zh": [
   "把 1 到 <code>n</code> 排成一個排列 <code>perm</code>（索引從 1 開始）。如果對每個位置 i 都滿足以下其中一個條件，就稱它為<strong>優美的排列</strong>：",
   ("ul", ["<code>perm[i]</code> 能被 <code>i</code> 整除", "<code>i</code> 能被 <code>perm[i]</code> 整除"]),
   "給你 <code>n</code>，回傳優美排列的數量。",
 ],
 "idea": [
   ("c", """【回溯：一個位置一個位置填】
    填第 i 個位置時，試所有還沒用過、且和 i 互相整除的數。
    整除條件很嚴格，剪枝效果很好。

【狀態壓縮 + 記憶化】
    「已經用了哪些數」用一個 n 位元的遮罩 mask 表示。
    已用的數的個數 = popcount(mask) -> 就知道現在填第幾個位置。
    所以 dfs(mask) 的結果只跟 mask 有關 -> 可以記憶化。
    狀態數 2ⁿ，每個狀態試 n 個數 -> O(n · 2ⁿ)。"""),
 ],
 "approaches": [
   ap("解法", "位元遮罩 DP（記憶化回溯）", [
     ("c", S["p526"]),
     "驗證方式：n ≤ 8 時和枚舉所有排列比對；n = 15 的答案是 24679。",
   ], "O(n · 2ⁿ)", "O(2ⁿ)", optimal=True),
 ],
 "edges": ["<strong>n = 1</strong> → 1。", "<strong>1 可以放任何位置</strong>、<strong>任何數可以放在位置 1</strong>。"],
 "follow": [("h", "從後往前填更快"), ("c", "從位置 n 往 1 填：大位置的候選數很少，越早剪枝。位置 1 最後填，因為任何數都能放。")],
 "related": ["<strong>第 667 題 優美的排列 II</strong>", "<strong>第 46 題 全排列</strong>", "<strong>第 698 題 劃分為 k 個相等的子集</strong>"],
 "check": ["怎麼從 mask 知道現在要填第幾個位置？", "為什麼可以記憶化？"],
})


# ==================== 528. Random Pick with Weight ====================
S["p528"] = '''class Solution:
    def __init__(self, w: List[int]):
        self.prefix = list(accumulate(w))       # 權重前綴和：[w0, w0+w1, ...]

    def pickIndex(self) -> int:
        r = random.randrange(self.prefix[-1])   # 0 <= r < 總權重
        # ★ 第一個前綴和 > r 的位置：r 落在 [prefix[i-1], prefix[i]) 這一段
        return bisect.bisect_right(self.prefix, r)'''

from itertools import accumulate
_cls528 = S.loadns("p528", extra={"accumulate": accumulate})["Solution"]
o = _cls528([1, 3, 6]); cnt = Counter(o.pickIndex() for _ in range(50000))
for i, w in enumerate([1, 3, 6]):
    assert abs(cnt[i] / 50000 - w / 10) < 0.01
assert _cls528([5]).pickIndex() == 0
print("P528 OK")

em({
 "num": 528, "title": "按權重隨機選擇",
 "desc": "把權重排成一條長度為總和的線段，均勻選一點，再用二分找它落在哪一段。",
 "zh": [
   "給你一個正整數陣列 <code>w</code>，<code>w[i]</code> 是索引 i 的權重。實作 <code>pickIndex()</code>：隨機回傳一個索引，選中 i 的機率是 <code>w[i] / sum(w)</code>。",
 ],
 "idea": [
   ("c", """【把權重排成線段】
    w = [1, 3, 6]，總和 10：
        [0,1) -> 0，[1,4) -> 1，[4,10) -> 2
    在 [0, 10) 中均勻選一個整數 r，落在哪一段就回傳哪個索引。
    每段長度 = 權重 -> 機率正好正比於權重。

【找段落：前綴和 + 二分】
    prefix = [1, 4, 10]。
    r 落在第 i 段 <=> prefix[i-1] <= r < prefix[i]
    <=> i = 第一個 prefix > r 的位置 = bisect_right(prefix, r)。"""),
 ],
 "approaches": [
   ap("解法", "前綴和 + 二分搜尋", [("c", S["p528"]), "驗證方式：五萬次抽樣，各索引的頻率和理論機率相差不到 1%。"], "建構 O(n)，pick O(log n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>只有一個權重</strong> → 永遠回傳 0。", "<strong>bisect_left vs bisect_right</strong> → r 等於某個前綴和時屬於下一段，要用 right。"],
 "follow": [("h", "O(1) 抽樣：別名法"), ("c", "Walker 的別名法（alias method）可以 O(n) 預處理、O(1) 抽樣：把每個索引的機率「切塊」補進 n 個等高的桶，每桶最多兩個索引。")],
 "related": ["<strong>第 497 題 非重疊矩形中的隨機點</strong>", "<strong>第 710 題 黑名單中的隨機數</strong>", "<strong>第 398 題 隨機數索引</strong>"],
 "check": ["為什麼要用 bisect_right 而不是 bisect_left？", "每段的長度為什麼等於權重？"],
})


# ==================== 529. Minesweeper ====================
S["p529"] = '''class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click
        if board[r][c] == "M":
            board[r][c] = "X"                       # 踩到地雷，遊戲結束
            return board
        stack = [(r, c)]
        while stack:
            i, j = stack.pop()
            if board[i][j] != "E":
                continue                            # 已經揭開過
            nbrs = [(x, y) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2)
                    if 0 <= x < m and 0 <= y < n and (x, y) != (i, j)]
            mines = sum(board[x][y] in "MX" for x, y in nbrs)
            if mines:
                board[i][j] = str(mines)            # 旁邊有雷：顯示數字，不再擴散
            else:
                board[i][j] = "B"                   # ★ 旁邊沒雷：揭開並往八個方向擴散
                stack += [(x, y) for x, y in nbrs if board[x][y] == "E"]
        return board'''

_p529 = S.load("p529")
B = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"], ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
assert _p529.updateBoard(B, [3, 0]) == [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
B = [["B", "1", "E", "1", "B"], ["B", "1", "M", "1", "B"], ["B", "1", "1", "1", "B"], ["B", "B", "B", "B", "B"]]
assert _p529.updateBoard(B, [1, 2])[1][2] == "X"
def _ref529(board, click):
    import copy; b = copy.deepcopy(board); m, n = len(b), len(b[0])
    r, c = click
    if b[r][c] == "M":
        b[r][c] = "X"; return b
    def rec(i, j):
        if b[i][j] != "E": return
        nb = [(x, y) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2) if 0 <= x < m and 0 <= y < n and (x, y) != (i, j)]
        k = sum(b[x][y] == "M" for x, y in nb)
        if k: b[i][j] = str(k)
        else:
            b[i][j] = "B"
            for x, y in nb: rec(x, y)
    rec(r, c); return b
import copy
for _ in range(1500):
    m, n = random.randint(1, 5), random.randint(1, 5)
    b = [[random.choice("EEEEM") for _ in range(n)] for _ in range(m)]
    cl = [random.randrange(m), random.randrange(n)]
    assert _p529.updateBoard(copy.deepcopy(b), cl) == _ref529(b, cl)
print("P529 OK")

em({
 "num": 529, "title": "踩地雷遊戲",
 "desc": "照規則模擬：點到空白且四周沒雷就往八方向擴散（DFS/BFS），有雷就顯示數字並停止。",
 "zh": [
   "給你一個踩地雷的盤面 <code>board</code>：<code>'M'</code> 是未揭開的地雷、<code>'E'</code> 是未揭開的空格、<code>'B'</code> 是已揭開且四周（八個方向）沒有地雷的空格、<code>'1'</code>～<code>'8'</code> 是已揭開並顯示四周地雷數的格子、<code>'X'</code> 是已揭開的地雷。",
   "給你下一次點擊的位置 <code>click</code>（保證點在未揭開的 <code>'M'</code> 或 <code>'E'</code> 上），依下列規則回傳更新後的盤面：",
   ("ol", ["點到地雷 <code>'M'</code>：改成 <code>'X'</code>，遊戲結束。",
           "點到 <code>'E'</code> 且四周沒有地雷：改成 <code>'B'</code>，並<strong>遞迴</strong>揭開四周所有未揭開的格子。",
           "點到 <code>'E'</code> 且四周至少有一個地雷：改成地雷數 <code>'1'</code>～<code>'8'</code>。",
           "沒有更多格子可以揭開時，回傳盤面。"]),
 ],
 "idea": [
   ("c", """【就是 flood fill（洪水填充）】
    從點擊的格子開始：
        數八個鄰居裡的地雷數 k
        k > 0：寫上數字，停止（數字格是邊界）
        k = 0：寫上 'B'，把八個鄰居中還是 'E' 的推進堆疊繼續

【為什麼不會重複處理？】
    只處理還是 'E' 的格子；處理後就變成 'B' 或數字。

【遞迴 vs 堆疊】
    盤面最大 50×50，遞迴深度可能到 2500，
    用顯式堆疊比較保險。"""),
 ],
 "approaches": [
   ap("解法", "DFS（顯式堆疊）", [("c", S["p529"]), "驗證方式：和照規則直接寫的遞迴版本比對 1500 個隨機盤面。"], "O(mn)", "O(mn)", optimal=True),
 ],
 "edges": ["<strong>點到地雷</strong> → 只改那一格。", "<strong>數字格不擴散</strong> → 它是空白區的邊界。", "<strong>八個方向</strong> → 包含對角線。"],
 "follow": [("h", "Flood fill 家族"), ("c", "第 733 題（圖片填色）、第 200 題（島嶼數量）、第 130 題（被圍繞的區域）都是「從一格出發，往鄰居擴散，遇到邊界停止」。")],
 "related": ["<strong>第 733 題 圖片渲染</strong>", "<strong>第 200 題 島嶼數量</strong>", "<strong>第 130 題 被圍繞的區域</strong>"],
 "check": ["什麼情況下不繼續擴散？", "怎麼保證每格只處理一次？"],
})
