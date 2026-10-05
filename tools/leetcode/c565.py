# -*- coding: utf-8 -*-
"""第 565、566、567、572、575、576、581、583 題。"""
import random
from collections import Counter
from functools import lru_cache
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, nodes, ser

S = Src()
random.seed(565)


# ==================== 565. Array Nesting ====================
S["p565"] = '''class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            length = 0
            while nums[i] != -1:            # ★ 排列拆成若干個環；走過的標成 -1，不再重走
                nums[i], i = -1, nums[i]
                length += 1
            res = max(res, length)
        return res'''

_p565 = S.load("p565")
for _ in range(2000):
    n = random.randint(1, 10); a = list(range(n)); random.shuffle(a)
    best = 0
    for k in range(n):
        seen = set(); x = k
        while x not in seen:
            seen.add(x); x = a[x]
        best = max(best, len(seen))
    assert _p565.arrayNesting(a[:]) == best
print("P565 OK")

em({
 "num": 565, "title": "陣列巢狀",
 "desc": "排列一定由若干個不相交的環組成：每個環走一次並標記，答案是最大環的長度，O(n)。",
 "zh": [
   "給你一個長度為 <code>n</code> 的陣列 <code>nums</code>，它是 <code>[0, n − 1]</code> 的一個排列。",
   "從索引 k 出發建立集合 <code>s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ...}</code>，直到出現重複元素為止。回傳最大的 <code>s[k]</code> 的大小。",
 ],
 "idea": [
   ("c", """【排列 = 若干個不相交的環】
    每個值恰好被一個索引指到、也恰好指向一個索引，
    所以從任何點出發一直走，一定會繞回起點，形成一個環。
    不同的環互不相交。

【同一個環上的點，答案都一樣】
    從環上任一點出發走到的集合，就是整個環。
    所以每個環只需要走一次：走過的點標記起來，之後跳過。
    總共走 n 步。

【原地標記】
    把走過的 nums[i] 設成 -1，不需要額外的 visited 陣列。"""),
 ],
 "approaches": [
   ap("解法", "環分解 + 原地標記", [("c", S["p565"])], "O(n)", "O(1)", "每個元素只被走過一次", "", optimal=True),
 ],
 "edges": ["<strong>自環</strong>（nums[i] = i）→ 長度 1。", "<strong>整個排列是一個環</strong> → n。"],
 "follow": [("h", "排列的環分解"), ("c", "排列的環結構常出現在：最少交換次數排序（n − 環數）、第 765 題（情侶牽手）、第 41 題（缺失的第一個正數的原地交換）。")],
 "related": ["<strong>第 765 題 情侶牽手</strong>", "<strong>第 41 題 缺失的第一個正數</strong>", "<strong>第 287 題 尋找重複數</strong>"],
 "check": ["為什麼排列一定由環組成？", "為什麼每個環只需要走一次？"],
})


# ==================== 566. Reshape the Matrix ====================
S["p566"] = '''class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat                      # 元素個數不同，無法重塑
        res = [[0] * c for _ in range(r)]
        for k in range(m * n):              # ★ 依列優先的順序編號 k，兩邊用同一個 k 定位
            res[k // c][k % c] = mat[k // n][k % n]
        return res'''

_p566 = S.load("p566")
for _ in range(1000):
    m, n = random.randint(1, 4), random.randint(1, 4); M = [[random.randint(0, 9) for _ in range(n)] for _ in range(m)]
    r, c = random.randint(1, 6), random.randint(1, 6)
    flat = [x for row in M for x in row]
    want = [flat[i * c:(i + 1) * c] for i in range(r)] if r * c == m * n else M
    assert _p566.matrixReshape(M, r, c) == want
print("P566 OK")

em({
 "num": 566, "title": "重塑矩陣",
 "desc": "依列優先的順序給每個元素一個編號 k，原矩陣與新矩陣都用 k 的商與餘數定位。",
 "zh": [
   "實作 MATLAB 的 <code>reshape</code>：把 <code>m x n</code> 的矩陣 <code>mat</code> 依<strong>列優先</strong>的順序重新排成 <code>r x c</code> 的矩陣。",
   "若無法重塑（元素數量不同），回傳原矩陣。",
 ],
 "idea": [
   ("c", """【攤平成一維編號】
    列優先的第 k 個元素：
        在 m×n 矩陣中位於 (k // n, k % n)
        在 r×c 矩陣中位於 (k // c, k % c)
    一個迴圈搞定，不需要真的建一維陣列。"""),
 ],
 "approaches": [
   ap("解法", "一維編號換算", [("c", S["p566"])], "O(mn)", "O(1)", "", "不計輸出", optimal=True),
 ],
 "edges": ["<strong>元素個數不符</strong> → 回傳原矩陣。", "<strong>r, c 與原本相同</strong> → 內容不變。"],
 "follow": [("h", "二維 ↔ 一維"), ("c", "「k → (k // 寬, k % 寬)」是把二維格子攤平的標準換算，第 74 題（搜尋二維矩陣）的二分也用它。")],
 "related": ["<strong>第 74 題 搜尋二維矩陣</strong>", "<strong>第 2022 題 將一維陣列轉換成二維陣列</strong>"],
 "check": ["編號 k 在 r×c 矩陣中的座標是什麼？"],
})


# ==================== 567. Permutation in String ====================
S["p567"] = '''class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False
        need = Counter(s1)
        win = Counter(s2[:k])
        if win == need:
            return True
        for i in range(k, len(s2)):         # ★ 固定長度 k 的視窗往右滑
            win[s2[i]] += 1
            win[s2[i - k]] -= 1
            if win[s2[i - k]] == 0:
                del win[s2[i - k]]          # 刪掉計數為 0 的鍵，Counter 才能直接比較
            if win == need:
                return True
        return False'''

_p567 = S.load("p567", extra={"Counter": Counter})
for _ in range(3000):
    s1 = "".join(random.choice("abc") for _ in range(random.randint(1, 4)))
    s2 = "".join(random.choice("abc") for _ in range(random.randint(1, 9)))
    want = any(sorted(s2[i:i + len(s1)]) == sorted(s1) for i in range(len(s2) - len(s1) + 1))
    assert _p567.checkInclusion(s1, s2) == want
print("P567 OK")

em({
 "num": 567, "title": "字串的排列",
 "desc": "s1 的排列 = 長度相同、字元計數相同的子字串：固定長度的滑動視窗維護計數。",
 "zh": ["給你兩個字串 <code>s1</code>、<code>s2</code>，判斷 <code>s2</code> 是否包含 <code>s1</code> 的某個<strong>排列</strong>作為子字串。"],
 "idea": [
   ("c", """【排列 <=> 字元計數相同】
    要找 s2 中長度為 len(s1)、字元計數和 s1 相同的子字串。

【固定長度的滑動視窗】
    視窗每次右移一格：加入新進來的字元、移除離開的字元。
    每次比較兩個計數表（26 個字母，O(1)）。

【更細的最佳化】
    維護「有幾個字母的計數已經相等」diff，
    每次只更新進出的兩個字母，比較變成 O(1) 的整數檢查。"""),
 ],
 "approaches": [
   ap("解法", "固定長度滑動視窗 + 計數", [("c", S["p567"])], "O(n · 26)", "O(26)", optimal=True),
 ],
 "edges": ["<strong>s1 比 s2 長</strong> → False。", "<strong>計數為 0 的鍵</strong> → Counter 比較時要刪掉（或改用長度 26 的陣列）。"],
 "follow": [("h", "同一個模板"), ("c", "第 438 題（找出所有字母異位詞的起點）和本題幾乎一樣，只是把「找到一個就回傳」改成「全部收集」。")],
 "related": ["<strong>第 438 題 找到字串中所有字母異位詞</strong>", "<strong>第 76 題 最小覆蓋子字串</strong>"],
 "check": ["為什麼「是某個排列」等於「計數相同」？", "視窗移動時要更新哪兩個字元？"],
})


# ==================== 572. Subtree of Another Tree ====================
S["p572"] = '''class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(a, b):
            if not a or not b:
                return a is b
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

        def dfs(nd):                        # 以每個節點為根，檢查是否和 subRoot 完全相同
            return nd is not None and (same(nd, subRoot) or dfs(nd.left) or dfs(nd.right))
        return dfs(root)'''

_p572 = S.load("p572")
def _sig(t): return None if t is None else (t.val, _sig(t.left), _sig(t.right))
for _ in range(2000):
    t = rand_tree(random.randint(1, 10), 0, 2)
    sub = random.choice(nodes(t)) if random.random() < 0.5 else rand_tree(random.randint(1, 4), 0, 2)
    want = any(_sig(n) == _sig(sub) for n in nodes(t))
    assert _p572.isSubtree(t, sub) == want
print("P572 OK")

em({
 "num": 572, "title": "另一棵樹的子樹",
 "desc": "對每個節點做「兩棵樹是否相同」的比對；進階可以序列化後做字串匹配，達到線性時間。",
 "zh": [
   "給你兩棵二元樹的根節點 <code>root</code> 和 <code>subRoot</code>，判斷 <code>root</code> 中是否存在一個子樹和 <code>subRoot</code> <strong>結構與節點值完全相同</strong>。",
   "子樹指某個節點及它的<strong>所有</strong>後代。",
 ],
 "idea": [
   ("c", """【暴力但足夠：O(m · n)】
    對 root 的每個節點 nd，檢查 same(nd, subRoot)（第 100 題）。

【注意：子樹要包含所有後代】
    不能只比對到 subRoot 的葉子就停，
    nd 對應位置也必須沒有多餘的孩子 —— same() 自然處理。

【線性做法】
    把兩棵樹序列化（空孩子也要標記，例如 '#'，值前後加分隔符避免 12 和 2 混淆），
    問題變成「字串 B 是否是字串 A 的子字串」，用 KMP 做到 O(m + n)。"""),
 ],
 "approaches": [
   ap("解法", "每個節點比對兩樹相同", [("c", S["p572"])], "O(m · n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>值相同但多了孩子</strong> → 不算子樹。", "<strong>重複的值</strong> → 要繼續搜尋其他節點，不能找到第一個值相同的就停。"],
 "follow": [("h", "序列化 + 雜湊"), ("c", "也可以把每個子樹算一個雜湊值（Merkle 雜湊），比較 subRoot 的雜湊是否出現在 root 的子樹雜湊中。第 652 題（尋找重複的子樹）用的就是這個想法。")],
 "related": ["<strong>第 100 題 相同的樹</strong>", "<strong>第 652 題 尋找重複的子樹</strong>", "<strong>第 1367 題 二元樹中的鏈結串列</strong>"],
 "check": ["為什麼不能找到第一個值相同的節點就停？", "序列化時為什麼要標記空孩子？"],
})


# ==================== 575. Distribute Candies ====================
S["p575"] = '''class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) // 2)   # ★ 種類數和可吃數量的較小者'''

_p575 = S.load("p575")
assert _p575.distributeCandies([1, 1, 2, 2, 3, 3]) == 3 and _p575.distributeCandies([6, 6, 6, 6]) == 1
print("P575 OK")

em({
 "num": 575, "title": "分糖果",
 "desc": "答案受兩個上限限制：最多只能吃 n/2 顆、最多只有這麼多種，取較小者。",
 "zh": ["Alice 有 <code>n</code> 顆糖果（n 是偶數），<code>candyType[i]</code> 是第 i 顆的種類。醫生說她只能吃 <code>n / 2</code> 顆。她想吃到<strong>最多種類</strong>，回傳最多能吃到幾種。"],
 "idea": [
   ("c", """【兩個上限】
    最多吃 n/2 顆 -> 最多 n/2 種。
    糖果只有 k 種 -> 最多 k 種。
    答案 <= min(k, n/2)。

【一定達得到】
    每種先挑一顆：若 k <= n/2，就能吃到全部 k 種；
    若 k > n/2，挑 n/2 種各一顆即可。"""),
 ],
 "approaches": [
   ap("解法", "取兩個上限的最小值", [("c", S["p575"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>全部同一種</strong> → 1。", "<strong>全部不同</strong> → n/2。"],
 "follow": [("h", "上界 + 構造"), ("c", "先找出答案的上界，再構造一個方案證明上界可以達到——這是很多貪心題的證明方式。")],
 "related": ["<strong>第 1103 題 分糖果 II</strong>"],
 "check": ["答案的兩個上限是什麼？"],
})


# ==================== 576. Out of Boundary Paths ====================
S["p576"] = '''class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * n for _ in range(m)]        # dp[i][j]：走了 t 步後停在 (i, j) 的路徑數
        dp[startRow][startColumn] = 1
        res = 0
        for _ in range(maxMove):
            nd = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    v = dp[i][j]
                    if not v:
                        continue
                    for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                        if 0 <= x < m and 0 <= y < n:
                            nd[x][y] = (nd[x][y] + v) % MOD
                        else:
                            res = (res + v) % MOD   # ★ 這一步走出邊界：這些路徑在此結束並計入答案
            dp = nd
        return res'''

_p576 = S.load("p576")
assert _p576.findPaths(2, 2, 2, 0, 0) == 6 and _p576.findPaths(1, 3, 3, 0, 1) == 12
@lru_cache(None)
def _bf576(m, n, k, i, j):
    if not (0 <= i < m and 0 <= j < n): return 1
    if k == 0: return 0
    return sum(_bf576(m, n, k - 1, x, y) for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)))
for _ in range(300):
    m, n, k = random.randint(1, 4), random.randint(1, 4), random.randint(0, 6)
    i, j = random.randrange(m), random.randrange(n)
    assert _p576.findPaths(m, n, k, i, j) == _bf576(m, n, k, i, j) % (10 ** 9 + 7)
print("P576 OK")

em({
 "num": 576, "title": "出界的路徑數",
 "desc": "按步數 DP：dp[t][i][j] 是 t 步後停在格子內的路徑數，往外走的那一步就計入答案。",
 "zh": [
   "在 <code>m x n</code> 的網格中，球一開始在 <code>[startRow, startColumn]</code>。每一步可以往上下左右移動一格（可以走出網格）。最多走 <code>maxMove</code> 步。",
   "回傳把球移出網格邊界的路徑數，對 <code>10⁹ + 7</code> 取模。",
 ],
 "idea": [
   ("c", """【一出界路徑就結束】
    所以「還在格子內」的狀態才需要繼續走。

【按步數 DP】
    dp[i][j] = 走了 t 步、目前在 (i, j) 的路徑數。
    每一步：從 (i, j) 往四個方向，
        還在格內 -> 加到下一步的 dp
        出界     -> 這些路徑完成，加進答案

【記憶化寫法】
    f(k, i, j) = 從 (i, j) 出發、最多走 k 步能出界的路徑數；
    出界時回傳 1，k = 0 回傳 0。"""),
 ],
 "approaches": [
   ap("解法", "按步數的網格 DP", [("c", S["p576"]), "驗證方式：和記憶化遞迴比對 300 組。"], "O(maxMove · m · n)", "O(m · n)", optimal=True),
 ],
 "edges": ["<strong>maxMove = 0</strong> → 0。", "<strong>角落的格子</strong> → 一步就有兩個方向能出界。"],
 "follow": [("h", "類似的機率版"), ("c", "第 688 題（騎士在棋盤上的機率）：同樣按步數 DP，只是把計數換成機率、八個方向換成馬步。")],
 "related": ["<strong>第 688 題 騎士在棋盤上的機率</strong>", "<strong>第 62 題 不同路徑</strong>", "<strong>第 935 題 騎士撥號器</strong>"],
 "check": ["出界的路徑為什麼不再繼續走？", "dp 的維度為什麼可以只保留兩層？"],
})


# ==================== 581. Shortest Unsorted Continuous Subarray ====================
S["p581"] = '''class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        right, mx = -1, float("-inf")
        for i in range(n):                  # 由左往右：比左邊最大值還小的，一定在要排序的區間裡
            if nums[i] < mx:
                right = i                   # ★ 最後一個「不在正確位置」的位置
            else:
                mx = nums[i]
        left, mn = n, float("inf")
        for i in range(n - 1, -1, -1):      # 由右往左：比右邊最小值還大的，也在區間裡
            if nums[i] > mn:
                left = i
            else:
                mn = nums[i]
        return right - left + 1 if right > left else 0'''

_p581 = S.load("p581")
for _ in range(3000):
    a = [random.randint(0, 5) for _ in range(random.randint(1, 9))]
    s = sorted(a); d = [i for i in range(len(a)) if a[i] != s[i]]
    assert _p581.findUnsortedSubarray(a) == (d[-1] - d[0] + 1 if d else 0)
print("P581 OK")

em({
 "num": 581, "title": "最短無序連續子陣列",
 "desc": "右邊界是最後一個「比左側最大值小」的位置，左邊界是最後一個「比右側最小值大」的位置，兩趟 O(n)。",
 "zh": ["給你一個整數陣列 <code>nums</code>，找出一個<strong>最短的連續子陣列</strong>，只要把它遞增排序，整個陣列就會變成遞增排序。回傳它的長度。"],
 "idea": [
   ("c", """【排序後比對：O(n log n)】
    排序後和原陣列比較，第一個與最後一個不同的位置就是邊界。

【O(n)：什麼樣的位置一定要被排序？】
    由左往右掃，維護目前最大值 mx：
        nums[i] < mx -> 它左邊有比它大的，i 不在正確位置，
                       必須包含在區間內 -> right = i
    最後一次更新的 right 就是右邊界。

    對稱地，由右往左掃維護最小值 mn：
        nums[i] > mn -> left = i
    最後一次更新的 left 就是左邊界。"""),
 ],
 "approaches": [
   ap("解法一", "排序後比對", [("c", "s = sorted(nums)\n第一個 nums[i] != s[i] 的 i 是左邊界，最後一個是右邊界")], "O(n log n)", "O(n)"),
   ap("解法二", "兩趟掃描", [("c", S["p581"]), "驗證方式：和排序比對法對照 3000 組。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>已經有序</strong> → 0。", "<strong>重複值</strong> → 用嚴格的 < 和 >，相等不算錯位。", "<strong>完全逆序</strong> → n。"],
 "follow": [("h", "為什麼「最後一次」更新就是邊界？"), ("c", "right 右邊的每個元素都 >= 它左邊所有元素的最大值，代表它們已經在正確位置，不需要動。")],
 "related": ["<strong>第 769 題 最多能完成排序的區塊</strong>", "<strong>第 1574 題 刪除最短的子陣列使剩餘陣列有序</strong>"],
 "check": ["由左往右掃時，什麼條件代表 i 必須被包含？", "為什麼取最後一次更新的位置？"],
})


# ==================== 583. Delete Operation for Two Strings ====================
S["p583"] = '''class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]      # dp[i][j]：前 i 個與前 j 個字元的 LCS 長度
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # ★ 保留最長共同子序列，其餘全部刪掉
        return m + n - 2 * dp[m][n]'''

_p583 = S.load("p583")
@lru_cache(None)
def _bf583(a, b):
    if not a: return len(b)
    if not b: return len(a)
    if a[0] == b[0]: return _bf583(a[1:], b[1:])
    return 1 + min(_bf583(a[1:], b), _bf583(a, b[1:]))
for _ in range(2000):
    a = "".join(random.choice("abc") for _ in range(random.randint(1, 7)))
    b = "".join(random.choice("abc") for _ in range(random.randint(1, 7)))
    assert _p583.minDistance(a, b) == _bf583(a, b)
print("P583 OK")

em({
 "num": 583, "title": "兩個字串的刪除操作",
 "desc": "兩邊刪到剩下的字串相同，剩下的最多就是最長共同子序列：答案 = m + n − 2·LCS。",
 "zh": ["給你兩個單字 <code>word1</code>、<code>word2</code>，每一步可以從<strong>任一個</strong>字串刪除一個字元。回傳讓兩個字串相同所需的<strong>最少步數</strong>。"],
 "idea": [
   ("c", """【刪完之後剩下的是什麼？】
    兩邊剩下的字串相同 -> 它是兩者的共同子序列。
    要刪最少 = 剩最多 -> 保留最長共同子序列（LCS）。
    答案 = (m - LCS) + (n - LCS)。

【LCS 的 DP（第 1143 題）】
    dp[i][j]：word1 前 i 個、word2 前 j 個字元的 LCS。
    字元相同 -> dp[i-1][j-1] + 1
    不同     -> max(dp[i-1][j], dp[i][j-1])

【也可以直接 DP 刪除次數】
    相同 -> dp[i-1][j-1]；不同 -> 1 + min(dp[i-1][j], dp[i][j-1])。"""),
 ],
 "approaches": [
   ap("解法", "轉成 LCS", [("c", S["p583"]), "驗證方式：和直接遞迴刪除次數的記憶化版本比對 2000 組。"], "O(mn)", "O(mn)", "", "可壓成一維 O(n)", optimal=True),
 ],
 "edges": ["<strong>完全沒有共同字元</strong> → m + n。", "<strong>兩字串相同</strong> → 0。"],
 "follow": [("h", "編輯距離家族"), ("c", "只能刪除：本題；可以插入、刪除、替換：第 72 題（編輯距離）；刪除的成本是 ASCII 值：第 712 題。")],
 "related": ["<strong>第 1143 題 最長共同子序列</strong>", "<strong>第 72 題 編輯距離</strong>", "<strong>第 712 題 兩個字串的最小 ASCII 刪除和</strong>"],
 "check": ["為什麼刪完剩下的一定是共同子序列？", "答案公式 m + n − 2·LCS 怎麼來的？"],
})
