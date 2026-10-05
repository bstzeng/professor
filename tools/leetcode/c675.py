# -*- coding: utf-8 -*-
"""第 675、676、677、678、679、680、682、684 題。"""
import random, heapq
from collections import deque
from fractions import Fraction
from itertools import permutations
from authoring import ap
from lcauto import em
from runner import Src

S = Src()
random.seed(675)


# ==================== 675. Cut Off Trees for Golf Event ====================
S["p675"] = '''class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        trees = sorted((h, i, j) for i, row in enumerate(forest) for j, h in enumerate(row) if h > 1)

        def bfs(si, sj, ti, tj):                # 兩點間最短步數（不能走 0）
            if (si, sj) == (ti, tj):
                return 0
            seen = {(si, sj)}
            q = deque([(si, sj, 0)])
            while q:
                i, j, d = q.popleft()
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and forest[x][y] and (x, y) not in seen:
                        if (x, y) == (ti, tj):
                            return d + 1
                        seen.add((x, y))
                        q.append((x, y, d + 1))
            return -1

        res, si, sj = 0, 0, 0
        for _, ti, tj in trees:                 # ★ 砍樹順序固定（由矮到高），只要把每一段最短路加起來
            d = bfs(si, sj, ti, tj)
            if d < 0:
                return -1
            res += d
            si, sj = ti, tj
        return res'''

_p675 = S.load("p675")
assert _p675.cutOffTree([[1, 2, 3], [0, 0, 4], [7, 6, 5]]) == 6
assert _p675.cutOffTree([[1, 2, 3], [0, 0, 0], [7, 6, 5]]) == -1
assert _p675.cutOffTree([[2, 3, 4], [0, 0, 5], [8, 7, 6]]) == 6
print("P675 OK")

em({
 "num": 675, "title": "為高爾夫比賽砍樹",
 "desc": "砍樹順序是固定的（由矮到高），問題拆成一連串「兩點間最短路」：每一段做一次 BFS。",
 "zh": [
   "給你一個 <code>m x n</code> 的森林矩陣：<code>0</code> 是障礙物（不能走）、<code>1</code> 是空地、大於 1 的數是樹（可以走，值是樹的高度，砍掉後變成 1）。",
   "你從 <code>(0, 0)</code> 出發，每步可以往上下左右走一格。必須依<strong>高度由矮到高</strong>砍掉所有樹（高度互不相同），回傳最少步數；無法砍完所有樹則回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【順序是固定的】
    必須由矮到高砍 -> 先把所有樹依高度排序。
    路線 = (0,0) -> 第 1 棵 -> 第 2 棵 -> ... -> 最後一棵。

【每一段獨立】
    砍樹只把格子變成 1，不改變「哪些格子能走」，
    所以每一段的最短路互不影響 -> 各做一次 BFS 加總。
    任何一段走不到 -> -1。

【複雜度】
    最多 mn 棵樹，每段 BFS O(mn) -> O((mn)²)。
    m, n <= 50，約 6×10⁶，可以接受。

【加速】
    把 BFS 換成 A*（曼哈頓距離當啟發式）或 Hadlock 演算法。"""),
 ],
 "approaches": [
   ap("解法", "排序 + 逐段 BFS", [("c", S["p675"])], "O((mn)²)", "O(mn)", optimal=True),
 ],
 "edges": ["<strong>(0,0) 本身是樹</strong> → 第一段距離可能是 0。", "<strong>某棵樹被障礙物隔開</strong> → −1。", "<strong>(0,0) 是障礙物</strong>（題目保證不會）。"],
 "follow": [("h", "A* 搜尋"), ("c", "A* 用 f = 已走距離 + 曼哈頓距離 排序的優先佇列。曼哈頓距離不會高估真實距離（可容許的啟發式），所以找到的仍是最短路，但通常探索的格子少很多。")],
 "related": ["<strong>第 1091 題 二進位矩陣中的最短路徑</strong>", "<strong>第 864 題 獲取所有鑰匙的最短路徑</strong>"],
 "check": ["為什麼可以把每一段分開計算？", "整體時間複雜度是多少？"],
})


# ==================== 676. Implement Magic Dictionary ====================
S["p676"] = '''class MagicDictionary:
    def __init__(self):
        self.patterns = Counter()       # 「挖掉一個字元」的樣式 -> 次數
        self.words = set()

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = set(dictionary)
        for w in dictionary:
            for i in range(len(w)):
                self.patterns[w[:i] + "*" + w[i + 1:]] += 1

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            p = searchWord[:i] + "*" + searchWord[i + 1:]
            # ★ 有字典單字符合這個樣式，而且那個單字不是 searchWord 自己（或還有別的單字也符合）
            c = self.patterns[p]
            if c > 1 or (c == 1 and searchWord not in self.words):
                return True
        return False'''

_M = S.loadns("p676")["MagicDictionary"]
for _ in range(1000):
    d = list({"".join(random.choice("ab") for _ in range(random.randint(1, 3))) for _ in range(random.randint(1, 5))})
    md = _M(); md.buildDict(d)
    for _ in range(5):
        w = "".join(random.choice("abc") for _ in range(random.randint(1, 3)))
        want = any(len(x) == len(w) and sum(a != b for a, b in zip(x, w)) == 1 for x in d)
        assert md.search(w) == want, (d, w)
print("P676 OK")

em({
 "num": 676, "title": "實作一個魔法字典",
 "desc": "把每個單字「挖掉一個字元」的樣式存起來；查詢時產生同樣的樣式，並排除只和自己相符的情況。",
 "zh": [
   "設計一個資料結構：先用一組<strong>互不相同</strong>的單字建立字典，之後給你一個單字 <code>searchWord</code>，判斷能否<strong>恰好改變一個字元</strong>，使它變成字典中的某個單字。",
   "實作 <code>buildDict(dictionary)</code> 與 <code>search(searchWord)</code>。",
 ],
 "idea": [
   ("c", """【直接比對】
    對字典中每個同長度的單字，數有幾個位置不同，恰好 1 個就成立。
    查詢 O(字典大小 × 長度)。

【樣式（廣義鄰居）】
    "hello" -> "*ello", "h*llo", "he*lo", "hel*o", "hell*"
    兩個單字恰好差一個字元 <=> 它們有一個共同的樣式，而且它們不相同。

【排除自己】
    searchWord 本身在字典裡時，它自己也會產生相同的樣式，
    但「改變 0 個字元」不算。
    所以要求：樣式的次數 >= 2，或次數 = 1 且 searchWord 不在字典裡。"""),
 ],
 "approaches": [
   ap("解法一", "逐一比對", [("c", "for w in dictionary:\n    if len(w) == len(s) and sum(a != b for a, b in zip(w, s)) == 1: return True")], "查詢 O(N · L)", "O(N · L)"),
   ap("解法二", "挖空樣式的雜湊表", [("c", S["p676"]), "驗證方式：和逐一比對的方法對照 1000 組隨機字典與查詢。"], "建構 O(N · L²)，查詢 O(L²)", "O(N · L²)", "L 為單字長度（字串切片的成本）", "", optimal=True),
 ],
 "edges": ["<strong>查詢的單字在字典裡</strong> → 不能和自己配對。", "<strong>長度不同</strong> → 不可能。", "<strong>\"hello\" 與 \"hallo\" 都在字典裡，查 \"hello\"</strong> → True（和 hallo 差一個字元）。"],
 "follow": [("h", "廣義鄰居"), ("c", "第 127 題（單字接龍）也用相同的「挖掉一個字元」樣式來快速找鄰居，避免兩兩比對。")],
 "related": ["<strong>第 127 題 單字接龍</strong>", "<strong>第 208 題 實作字典樹</strong>"],
 "check": ["兩個單字恰好差一個字元時，它們有什麼共同的樣式？", "為什麼要特別處理 searchWord 在字典中的情況？"],
})


# ==================== 677. Map Sum Pairs ====================
S["p677"] = '''class MapSum:
    def __init__(self):
        self.vals = {}                  # 鍵 -> 目前的值
        self.trie = {}                  # 每個節點存「經過這個前綴的所有鍵的值總和」

    def insert(self, key: str, val: int) -> None:
        delta = val - self.vals.get(key, 0)     # ★ 覆寫時只加上差值
        self.vals[key] = val
        nd = self.trie
        for ch in key:
            nd = nd.setdefault(ch, {"#": 0})
            nd["#"] += delta

    def sum(self, prefix: str) -> int:
        nd = self.trie
        for ch in prefix:
            if ch not in nd:
                return 0
            nd = nd[ch]
        return nd["#"]'''

_MS = S.loadns("p677")["MapSum"]
for _ in range(500):
    ms = _MS(); ref = {}
    for _ in range(20):
        k = "".join(random.choice("ab") for _ in range(random.randint(1, 3)))
        if random.random() < 0.6:
            v = random.randint(0, 9); ms.insert(k, v); ref[k] = v
        else:
            assert ms.sum(k) == sum(v for x, v in ref.items() if x.startswith(k))
print("P677 OK")

em({
 "num": 677, "title": "鍵值映射",
 "desc": "字典樹的每個節點存「經過這個前綴的鍵的值總和」；覆寫舊鍵時只沿路加上差值。",
 "zh": [
   "設計一個 <code>MapSum</code>：",
   ("ul", ["<code>insert(key, val)</code>：插入鍵值對；若鍵已存在，<strong>覆寫</strong>它的值。",
           "<code>sum(prefix)</code>：回傳所有以 <code>prefix</code> 開頭的鍵的值總和。"]),
 ],
 "idea": [
   ("c", """【字典樹 + 前綴總和】
    每個節點存 total：所有經過這個節點（以這個前綴開頭）的鍵的值總和。
    sum(prefix) 只要走到 prefix 的節點，回傳它的 total，O(|prefix|)。

【覆寫的處理】
    鍵已存在時，不能直接再加 val（會重複計算）。
    記住每個鍵目前的值，沿路加上 delta = 新值 - 舊值。"""),
 ],
 "approaches": [
   ap("解法", "字典樹 + 差值更新", [("c", S["p677"]), "驗證方式：和雜湊表暴力加總對照，隨機執行 500 組操作。"], "insert / sum：O(L)", "O(總字元數)", optimal=True),
 ],
 "edges": ["<strong>覆寫既有的鍵</strong> → 用差值。", "<strong>前綴不存在</strong> → 0。", "<strong>前綴等於某個完整的鍵</strong> → 那個鍵也算。"],
 "follow": [("h", "暴力法"), ("c", "只用雜湊表、sum 時掃過所有鍵檢查 startswith：insert O(1)、sum O(N·L)。操作數少時也能過，但字典樹把查詢降到 O(L)。")],
 "related": ["<strong>第 208 題 實作字典樹</strong>", "<strong>第 648 題 單字替換</strong>"],
 "check": ["字典樹節點存的是什麼？", "覆寫時為什麼要用差值？"],
})


# ==================== 678. Valid Parenthesis String ====================
S["p678"] = '''class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0                     # 未配對的 '(' 數量可能的最小值與最大值
        for c in s:
            if c == "(":
                lo += 1
                hi += 1
            elif c == ")":
                lo -= 1
                hi -= 1
            else:                       # '*' 可以是 ')'、空、或 '('
                lo -= 1
                hi += 1
            if hi < 0:
                return False            # ★ 就算所有 * 都當 '('，右括號還是太多
            lo = max(lo, 0)             # 不能有負數個未配對的左括號
        return lo == 0'''

_p678 = S.load("p678")
from itertools import product
def _valid(s):
    b = 0
    for c in s:
        b += 1 if c == "(" else -1
        if b < 0: return False
    return b == 0
for _ in range(3000):
    s = "".join(random.choice("()*") for _ in range(random.randint(1, 8)))
    stars = [i for i, c in enumerate(s) if c == "*"]
    want = False
    for ch in product(["(", ")", ""], repeat=len(stars)):
        t = list(s)
        for i, c in zip(stars, ch): t[i] = c
        if _valid("".join(t)): want = True; break
    assert _p678.checkValidString(s) == want, s
print("P678 OK")

em({
 "num": 678, "title": "有效的括號字串",
 "desc": "不追蹤每一種可能，只追蹤「未配對左括號數」的可能範圍 [lo, hi]：一趟 O(n)。",
 "zh": [
   "給你一個只含 <code>'('</code>、<code>')'</code>、<code>'*'</code> 的字串。<code>'*'</code> 可以當成 <code>'('</code>、<code>')'</code> 或空字串。",
   "判斷是否存在一種替換方式，使字串成為<strong>有效的括號字串</strong>。",
 ],
 "idea": [
   ("c", """【一般括號：只要一個計數器 bal】
    任何時刻 bal >= 0，結束時 bal == 0。

【有 '*' 時，bal 可能是一個範圍】
    維護 [lo, hi]：未配對左括號數可能的最小與最大值。
        '(' -> 兩者 +1
        ')' -> 兩者 -1
        '*' -> lo - 1（當 ')'），hi + 1（當 '('）
    hi < 0：就算全部往有利方向選，右括號還是太多 -> 失敗。
    lo < 0：把 lo 拉回 0（負數不合法，那些選擇不可能）。
    結束時 lo == 0 代表存在一種選法讓 bal 剛好為 0。

【為什麼範圍內每個值都達得到？】
    每一步範圍都是連續的整數區間（變化量是 ±1 的組合）。

【其他做法】
    兩個堆疊（存 '(' 與 '*' 的索引）、或 O(n²) DP。"""),
 ],
 "approaches": [
   ap("解法", "貪心：維護可能範圍", [("c", S["p678"]), "驗證方式：和枚舉每個 * 的三種替換的暴力法比對 3000 組。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>\"*)\"</strong> → True。", "<strong>\")*\"</strong> → False（開頭就 hi < 0）。", "<strong>\"(*\"</strong> → True。"],
 "follow": [("h", "雙堆疊做法"), ("c", "一個堆疊存 '(' 的索引，一個存 '*' 的索引。遇到 ')' 優先消耗 '('，其次 '*'；最後剩下的 '(' 要和在它右邊的 '*' 配對。")],
 "related": ["<strong>第 20 題 有效的括號</strong>", "<strong>第 32 題 最長有效括號</strong>", "<strong>第 921 題 使括號有效的最少添加</strong>"],
 "check": ["lo 和 hi 分別代表什麼？", "為什麼 lo 要和 0 取最大值？", "什麼時候可以提早判定失敗？"],
})


# ==================== 679. 24 Game ====================
S["p679"] = '''class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def solve(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6         # 浮點數比較要留誤差
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    rest = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    # ★ 任取兩個數做一次運算，結果放回去，問題縮小一個數
                    cands = [a + b, a - b, a * b]
                    if abs(b) > 1e-9:
                        cands.append(a / b)
                    if any(solve(rest + [c]) for c in cands):
                        return True
            return False
        return solve([float(c) for c in cards])'''

_p679 = S.load("p679")
assert _p679.judgePoint24([4, 1, 8, 7]) and not _p679.judgePoint24([1, 2, 1, 2])
assert _p679.judgePoint24([3, 3, 8, 8])      # 8 / (3 - 8/3) = 24：需要分數
assert _p679.judgePoint24([1, 5, 5, 5])      # 5 × (5 - 1/5) = 24
def _exact(nums):
    if len(nums) == 1: return nums[0] == 24
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j: continue
            rest = [nums[k] for k in range(len(nums)) if k not in (i, j)]
            a, b = nums[i], nums[j]
            for c in [a + b, a - b, a * b] + ([a / b] if b else []):
                if _exact(rest + [c]): return True
    return False
for _ in range(150):
    cards = [random.randint(1, 9) for _ in range(4)]
    assert _p679.judgePoint24(cards) == _exact([Fraction(c) for c in cards]), cards
print("P679 OK")

em({
 "num": 679, "title": "24 點遊戲",
 "desc": "回溯：任取兩個數做加減乘除，把結果放回去，四個數變三個、三個變兩個……；除法要用實數並容許誤差。",
 "zh": [
   "給你 4 張牌，每張是 1～9 的數字。判斷能否用 <code>+</code>、<code>-</code>、<code>*</code>、<code>/</code> 與括號，把這 4 個數（每個恰好用一次）組成結果為 <strong>24</strong> 的運算式。",
   "規則：除法是<strong>實數除法</strong>（不是整數除法）；<code>-</code> 不能當成一元負號；不能把數字串接（例如 1 和 2 不能變成 12）。",
 ],
 "idea": [
   ("c", """【括號的本質】
    任何加括號的運算式，都可以看成「每次挑兩個數合併成一個」，
    重複三次。所以不用直接處理括號。

【回溯】
    solve(nums)：
        只剩一個數 -> 檢查是否為 24
        否則任取有序對 (a, b)，嘗試 a+b、a-b、a*b、a/b，
        把結果放回剩下的數中遞迴。
    有序對讓 a-b 與 b-a、a/b 與 b/a 都被嘗試到。

【規模】
    4 個數：12 對 × 4 種運算 × 3 個數：6 對 × 4 × 2 個數：2 × 4 ≈ 9216 種，很小。

【浮點誤差】
    8 / (3 - 8/3) = 24 會得到 23.999999...，要用 |x - 24| < 1e-6。
    （或改用分數 Fraction 精確計算。）"""),
 ],
 "approaches": [
   ap("解法", "回溯（兩兩合併）", [("c", S["p679"]), "驗證方式：經典難題 [3,3,8,8]、[1,5,5,5] 都能找到；並和用 Fraction 精確計算的版本比對 150 組。"], "O(1)", "O(1)", "固定 4 個數，約 9216 種運算組合", "", optimal=True),
 ],
 "edges": ["<strong>除以 0</strong> → 跳過。", "<strong>需要分數中間值</strong>（如 3,3,8,8）→ 不能用整數除法。", "<strong>浮點誤差</strong> → 容許 1e−6。"],
 "follow": [("h", "一般化"), ("c", "n 個數湊目標 t：同樣的兩兩合併回溯，複雜度隨 n 急遽成長。也可以記憶化「剩下的數的多重集合」來去除重複。")],
 "related": ["<strong>第 282 題 給運算式添加運算子</strong>", "<strong>第 241 題 為運算式設計優先級</strong>"],
 "check": ["為什麼「兩兩合併」能涵蓋所有加括號的方式？", "為什麼要用有序對？", "為什麼浮點比較要容許誤差？"],
})


# ==================== 680. Valid Palindrome II ====================
S["p680"] = '''class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(l, r):
            return all(s[l + k] == s[r - k] for k in range((r - l + 1) // 2))
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # ★ 第一個不匹配：刪左邊或刪右邊，剩下的部分必須是迴文
                return is_pal(l + 1, r) or is_pal(l, r - 1)
            l += 1
            r -= 1
        return True'''

_p680 = S.load("p680")
for _ in range(3000):
    s = "".join(random.choice("abc") for _ in range(random.randint(1, 9)))
    want = s == s[::-1] or any((t := s[:i] + s[i + 1:]) == t[::-1] for i in range(len(s)))
    assert _p680.validPalindrome(s) == want
print("P680 OK")

em({
 "num": 680, "title": "驗證迴文串 II",
 "desc": "雙指標遇到第一個不匹配時，只有兩種選擇：刪左邊或刪右邊，各檢查一次剩下的是否迴文。",
 "zh": ["給你字串 <code>s</code>，判斷<strong>最多刪除一個字元</strong>後，它能否成為迴文。"],
 "idea": [
   ("c", """【雙指標從兩端往內】
    相同 -> 繼續。
    第一次不同（s[l] != s[r]）：
        這兩個至少要刪一個，否則不可能是迴文。
        刪 s[l]：檢查 s[l+1..r] 是否迴文
        刪 s[r]：檢查 s[l..r-1] 是否迴文
    任一成立即可。

【為什麼不用往外找其他刪除位置？】
    l 左邊、r 右邊已經兩兩配對好了，
    刪那裡的字元只會破壞已經對好的部分。"""),
 ],
 "approaches": [
   ap("解法", "雙指標 + 兩種刪法", [("c", S["p680"]), "驗證方式：和「嘗試刪除每個位置」的暴力法比對 3000 組。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>本身就是迴文</strong> → True。", "<strong>\"abca\"</strong> → True（刪 b 或 c）。", "<strong>兩種刪法都要試</strong> → \"cupuufuc\" 只能刪特定一邊。"],
 "follow": [("h", "最多刪 k 個？"), ("c", "第 1216 題（付費）：最多刪 k 個字元能否成為迴文 ⇔ n − 最長迴文子序列 ≤ k（第 516 題）。")],
 "related": ["<strong>第 125 題 驗證迴文串</strong>", "<strong>第 516 題 最長迴文子序列</strong>", "<strong>第 1216 題 驗證迴文串 III</strong>（付費）"],
 "check": ["遇到不匹配時有哪兩種選擇？", "為什麼只需要在第一個不匹配處做選擇？"],
})


# ==================== 682. Baseball Game ====================
S["p682"] = '''class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == "+":
                st.append(st[-1] + st[-2])      # 前兩次分數的和
            elif op == "D":
                st.append(st[-1] * 2)           # 前一次分數的兩倍
            elif op == "C":
                st.pop()                        # ★ 作廢前一次分數：堆疊天生支援「撤銷」
            else:
                st.append(int(op))
        return sum(st)'''

_p682 = S.load("p682")
assert _p682.calPoints(["5", "2", "C", "D", "+"]) == 30
assert _p682.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
assert _p682.calPoints(["1", "C"]) == 0
print("P682 OK")

em({
 "num": 682, "title": "棒球比賽",
 "desc": "用堆疊記錄有效分數：C 是彈出（撤銷），+ 與 D 看堆疊頂端。",
 "zh": [
   "你在記錄一場規則奇怪的棒球比賽。給你一組操作字串 <code>operations</code>，依序處理：",
   ("ul", ["整數 <code>x</code>：記錄新分數 x。", "<code>\"+\"</code>：記錄新分數 = 前兩次分數之和。",
           "<code>\"D\"</code>：記錄新分數 = 前一次分數的兩倍。", "<code>\"C\"</code>：讓前一次分數作廢，從紀錄中移除。"]),
   "回傳所有有效分數的總和。",
 ],
 "idea": [
   ("c", """【堆疊】
    每個操作只和「最近的分數」有關，而 C 要撤銷最近的一筆 ->
    堆疊最自然：
        x  -> push x
        +  -> push 頂端兩個的和
        D  -> push 頂端 × 2
        C  -> pop
    最後加總。"""),
 ],
 "approaches": [
   ap("解法", "堆疊模擬", [("c", S["p682"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>負數分數</strong> → int(\"-2\") 照樣解析。", "<strong>全部作廢</strong> → 0。"],
 "follow": [("h", "撤銷操作"), ("c", "編輯器的「復原」功能就是一個操作堆疊；要同時支援「重做」就再加一個堆疊。")],
 "related": ["<strong>第 150 題 逆波蘭表示法求值</strong>", "<strong>第 1047 題 刪除字串中的所有相鄰重複項</strong>"],
 "check": ["為什麼這題適合用堆疊？"],
})


# ==================== 684. Redundant Connection ====================
S["p684"] = '''class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra == rb:
                return [a, b]           # ★ 兩端已經連通：這條邊形成環，就是答案（最後出現的那條）
            parent[ra] = rb'''

_p684 = S.load("p684")
assert _p684.findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
assert _p684.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
for _ in range(1500):
    n = random.randint(3, 9)
    tree = [[random.randint(1, i - 1), i] for i in range(2, n + 1)]
    while True:
        a, b = random.sample(range(1, n + 1), 2)
        if [a, b] not in tree and [b, a] not in tree: break
    edges = tree + [[min(a, b), max(a, b)]]; random.shuffle(edges)
    # 參考：從後往前試，刪掉後剩下的是樹（連通）
    def connected(es):
        adj = {i: [] for i in range(1, n + 1)}
        for x, y in es: adj[x].append(y); adj[y].append(x)
        seen = {1}; st = [1]
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in seen: seen.add(v); st.append(v)
        return len(seen) == n
    want = next(e for e in reversed(edges) if connected([x for x in edges if x is not e]))
    assert _p684.findRedundantConnection(edges) == want
print("P684 OK")

em({
 "num": 684, "title": "冗餘連接",
 "desc": "依序加入邊，用聯合查找判斷兩端是否已連通；第一條連接已連通兩點的邊就是要刪的。",
 "zh": [
   "一棵有 <code>n</code> 個節點（編號 1～n）的樹，被多加了一條邊，變成有 n 條邊的無向圖。",
   "回傳一條可以刪除的邊，使剩下的圖成為一棵有 n 個節點的樹。若有多個答案，回傳在輸入中<strong>最後出現</strong>的那條。",
 ],
 "idea": [
   ("c", """【樹 + 一條邊 = 恰好一個環】
    要刪的邊一定在環上；環上的任何一條都可以刪。

【依序加入，找第一條形成環的邊】
    用聯合查找：加入 (a, b) 時，
        a、b 已經連通 -> 這條邊會形成環
    為什麼它是「環上最後出現的那條」？
    環上的邊中，前面的邊加入時都還沒形成環，
    最後一條加入時才把環閉合 -> 正好是它。"""),
 ],
 "approaches": [
   ap("解法", "聯合查找", [("c", S["p684"]), "驗證方式：隨機樹加一條邊後打亂順序，和「從後往前試刪、看是否仍連通」的方法比對 1500 組。"], "O(n α(n))", "O(n)", optimal=True),
 ],
 "edges": ["<strong>環很長</strong> → 仍然只看第一次 find 相同。", "<strong>多個候選</strong> → 依序處理自然得到最後出現的。"],
 "follow": [("h", "有向圖版本"), ("c", "第 685 題（冗餘連接 II）：有向圖、要變回有根樹，多了「某個節點有兩個父節點」的情況，要分情況討論。")],
 "related": ["<strong>第 685 題 冗餘連接 II</strong>", "<strong>第 547 題 省份數量</strong>", "<strong>第 261 題 以圖判樹</strong>（付費）"],
 "check": ["為什麼第一條形成環的邊就是環上最後出現的邊？"],
})
