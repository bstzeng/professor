# -*- coding: utf-8 -*-
"""第 685、686、687、688、689、690、691、692 題。"""
import random, heapq
from collections import Counter, deque
from functools import lru_cache
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, nodes

S = Src()
random.seed(685)


# ==================== 685. Redundant Connection II ====================
S["p685"] = '''class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = {}
        cand1 = cand2 = None
        for a, b in edges:                      # 找有沒有節點有兩個父節點
            if b in par:
                cand1, cand2 = [par[b], b], [a, b]   # 先出現的、後出現的
            else:
                par[b] = a

        root = list(range(n + 1))
        def find(x):
            while root[x] != x:
                root[x] = root[root[x]]
                x = root[x]
            return x

        for a, b in edges:
            if [a, b] == cand2:
                continue                        # ★ 先假設刪掉後出現的那條，看剩下的是否無環
            ra, rb = find(a), find(b)
            if ra == rb:
                # 有環：若有兩個父節點的情況，刪的應該是 cand1；否則刪形成環的這條
                return cand1 if cand1 else [a, b]
            root[rb] = ra
        return cand2'''

_p685 = S.load("p685")
assert _p685.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
assert _p685.findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]) == [4, 1]
def _is_rooted_tree(n, es):
    indeg = Counter(b for _, b in es)
    if any(indeg[v] > 1 for v in range(1, n + 1)): return False
    roots = [v for v in range(1, n + 1) if indeg[v] == 0]
    if len(roots) != 1: return False
    ch = {v: [] for v in range(1, n + 1)}
    for a, b in es: ch[a].append(b)
    seen = {roots[0]}; st = [roots[0]]
    while st:
        u = st.pop()
        for v in ch[u]:
            if v in seen: return False
            seen.add(v); st.append(v)
    return len(seen) == n
for _ in range(2000):
    n = random.randint(3, 8); perm = list(range(1, n + 1)); random.shuffle(perm)
    es = [[perm[random.randrange(i)], perm[i]] for i in range(1, n)]
    while True:
        a, b = random.randint(1, n), random.randint(1, n)
        if a != b and [a, b] not in es: break
    es.append([a, b]); random.shuffle(es)
    want = next(e for e in reversed(es) if _is_rooted_tree(n, [x for x in es if x is not e]))
    assert _p685.findRedundantDirectedConnection([e[:] for e in es]) == want, es
print("P685 OK")

em({
 "num": 685, "title": "冗餘連接 II",
 "desc": "有向版本分三種情況：有節點入度為 2（兩條候選邊）、有環、或兩者同時；先暫時刪掉後出現的候選邊再用聯合查找判斷。",
 "zh": [
   "<strong>有根樹</strong>是一個有向圖：恰好一個根節點（沒有父節點），其他每個節點恰好有一個父節點，且所有節點都是根的後代。",
   "給你一棵有 n 個節點的有根樹，被多加了一條有向邊（不重複）。回傳一條可以刪除的邊，使剩下的圖成為有根樹；有多個答案時回傳<strong>最後出現</strong>的那條。",
 ],
 "idea": [
   ("c", """【多出的那條邊 u -> v 會造成什麼？】
    情況 1：v 不是根 -> v 有兩個父節點（入度 2），但沒有環
    情況 2：v 是根 -> 沒有入度 2 的節點，但形成一個環
    情況 3：v 不是根，而且 u 是 v 的後代 -> 入度 2 + 環

【做法】
    1. 先找入度為 2 的節點，記下兩條指向它的邊 cand1（先）、cand2（後）。
    2. 暫時跳過 cand2，用聯合查找把其他邊加進來：
       - 若仍形成環：
           有候選 -> 刪錯了，應該刪 cand1（情況 3）
           沒候選 -> 純粹是環，刪形成環的這條（情況 2，和第 684 題相同）
       - 若沒有環：刪 cand2 就對了（情況 1，題目要最後出現的）"""),
 ],
 "approaches": [
   ap("解法", "入度檢查 + 聯合查找", [
     ("c", S["p685"]),
     "驗證方式：隨機有根樹加一條有向邊，和「從後往前試刪，檢查是否為有根樹」的暴力法比對 2000 組。",
   ], "O(n α(n))", "O(n)", optimal=True),
 ],
 "edges": ["<strong>入度 2 但無環</strong> → 刪後出現的那條。", "<strong>入度 2 且有環</strong> → 刪環上那條候選邊（cand1）。", "<strong>只有環、沒有入度 2</strong> → 多的邊指向根，和第 684 題相同。"],
 "follow": [("h", "無向 vs 有向"), ("c", "無向圖（第 684 題）只要找環；有向的有根樹還要求每個節點恰好一個父節點，所以多了入度的檢查。")],
 "related": ["<strong>第 684 題 冗餘連接</strong>", "<strong>第 1361 題 驗證二元樹</strong>"],
 "check": ["多加的邊會造成哪三種情況？", "跳過 cand2 後仍有環，為什麼答案是 cand1？"],
})


# ==================== 686. Repeated String Match ====================
S["p686"] = '''class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        k = -(-len(b) // len(a))            # 至少要重複 ceil(|b| / |a|) 次，長度才夠
        for t in (k, k + 1):                # ★ 最多再多一次（b 可能從 a 的中間開始）
            if b in a * t:
                return t
        return -1'''

_p686 = S.load("p686")
for _ in range(3000):
    a = "".join(random.choice("ab") for _ in range(random.randint(1, 4)))
    b = "".join(random.choice("ab") for _ in range(random.randint(1, 8)))
    want = next((t for t in range(1, 20) if b in a * t), -1)
    assert _p686.repeatedStringMatch(a, b) == want
print("P686 OK")

em({
 "num": 686, "title": "重複疊加字串匹配",
 "desc": "b 要成為 a 重複 k 次的子字串，k 只可能是 ⌈|b|/|a|⌉ 或再加 1，各檢查一次即可。",
 "zh": ["給你兩個字串 <code>a</code>、<code>b</code>，回傳把 <code>a</code> <strong>重複疊加</strong>的最少次數，使 <code>b</code> 成為疊加後字串的子字串；做不到則回傳 <code>-1</code>。"],
 "idea": [
   ("c", """【下界】
    長度至少要 >= |b| -> k >= ceil(|b| / |a|)。

【上界】
    b 在疊加字串中的起點，一定可以落在第一份 a 之內（起點 < |a|）。
    從那裡開始，長度 |b| 最多跨越 ceil(|b|/|a|) + 1 份 a。
    所以只要檢查 k 和 k+1。
    兩個都不行 -> 再多重複也沒用（只是重複同樣的模式）。

【子字串檢查】
    Python 的 in 平均很快；最壞情況可用 KMP 或 Rabin-Karp 保證 O(|a| + |b|)。"""),
 ],
 "approaches": [
   ap("解法", "只檢查 k 與 k+1", [("c", S["p686"]), "驗證方式：和從 1 開始逐一嘗試的暴力法比對 3000 組。"], "O(|a| + |b|)", "O(|a| + |b|)", "使用線性的字串匹配時", "", optimal=True),
 ],
 "edges": ["<strong>b 中有 a 沒有的字元</strong> → −1。", "<strong>b 從 a 中間開始</strong> → 需要 k+1。", "<strong>b 比 a 短</strong> → k = 1 或 2。"],
 "follow": [("h", "字串匹配演算法"), ("c", "KMP（第 28 題）、Rabin-Karp（滾動雜湊）、Z 演算法都是 O(n + m) 的子字串搜尋。")],
 "related": ["<strong>第 28 題 找出字串中第一個匹配項的下標</strong>", "<strong>第 459 題 重複的子字串</strong>"],
 "check": ["為什麼最多只需要檢查 k + 1 次？"],
})


# ==================== 687. Longest Univalue Path ====================
S["p687"] = '''class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = 0
        def arm(nd):                        # 從 nd 往下、值都和 nd 相同的最長鏈（邊數）
            nonlocal res
            if not nd:
                return 0
            L, R = arm(nd.left), arm(nd.right)
            L = L + 1 if nd.left and nd.left.val == nd.val else 0     # ★ 孩子值不同就接不上
            R = R + 1 if nd.right and nd.right.val == nd.val else 0
            res = max(res, L + R)           # 以 nd 為轉折點的路徑
            return max(L, R)
        arm(root)
        return res'''

_p687 = S.load("p687")
def _bf687(t):
    best = 0
    for s in nodes(t):
        # 從 s 出發，只走同值節點，找最遠距離（樹上 BFS，需要父指標）
        pass
    par = {}
    for nd in nodes(t):
        for c in (nd.left, nd.right):
            if c: par[id(c)] = nd
    for s in nodes(t):
        d = {id(s): 0}; q = deque([s])
        while q:
            u = q.popleft()
            for v in (u.left, u.right, par.get(id(u))):
                if v is not None and id(v) not in d and v.val == s.val:
                    d[id(v)] = d[id(u)] + 1; q.append(v)
        best = max(best, max(d.values()))
    return best
for _ in range(1500):
    t = rand_tree(random.randint(1, 12), 0, 1)
    assert _p687.longestUnivaluePath(t) == _bf687(t)
print("P687 OK")

em({
 "num": 687, "title": "最長同值路徑",
 "desc": "第 543 題（直徑）的變形：往下延伸的鏈只能接值相同的孩子；在每個節點用左臂 + 右臂更新答案。",
 "zh": ["給你二元樹的根節點，回傳最長路徑的<strong>邊數</strong>，這條路徑上所有節點的值都相同。路徑不一定經過根。"],
 "idea": [
   ("c", """【和第 543 題相同的骨架】
    arm(nd) = 從 nd 往下、全部同值的最長鏈（邊數）。
    以 nd 為最高點的路徑 = 左臂 + 右臂。

【多一個條件】
    孩子的值和 nd 不同 -> 那一側的臂長為 0（接不上）。
    但仍要遞迴進去，因為孩子的子樹裡可能有其他同值路徑。"""),
 ],
 "approaches": [
   ap("解法", "後序走訪", [("c", S["p687"]), "驗證方式：從每個節點出發只走同值鄰居做 BFS，取最遠距離，比對 1500 棵隨機樹。"], "O(n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>空樹或單一節點</strong> → 0。", "<strong>孩子值不同</strong> → 臂長歸零，但仍要遞迴。"],
 "follow": [("h", "樹上路徑題的模板"), ("c", "「函式回傳往下的單臂，在節點上組合兩臂更新答案」：第 543 題（直徑）、第 124 題（最大路徑和）、第 2246 題（相鄰字元不同的最長路徑）。")],
 "related": ["<strong>第 543 題 二元樹的直徑</strong>", "<strong>第 124 題 二元樹中的最大路徑和</strong>"],
 "check": ["arm 為什麼只能回傳一邊的臂長？", "孩子值不同時為什麼還要遞迴？"],
})


# ==================== 688. Knight Probability in Chessboard ====================
S["p688"] = '''class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
        dp = [[0.0] * n for _ in range(n)]      # dp[i][j]：走了 t 步後在 (i, j) 的機率
        dp[row][column] = 1.0
        for _ in range(k):
            nd = [[0.0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    if dp[i][j]:
                        for di, dj in moves:
                            x, y = i + di, j + dj
                            if 0 <= x < n and 0 <= y < n:
                                nd[x][y] += dp[i][j] / 8    # ★ 每個方向機率 1/8；出界的就消失了
            dp = nd
        return sum(map(sum, dp))'''

_p688 = S.load("p688")
assert abs(_p688.knightProbability(3, 2, 0, 0) - 0.0625) < 1e-9 and _p688.knightProbability(1, 0, 0, 0) == 1.0
@lru_cache(None)
def _bf688(n, k, i, j):
    if not (0 <= i < n and 0 <= j < n): return 0.0
    if k == 0: return 1.0
    return sum(_bf688(n, k - 1, i + a, j + b) for a, b in [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]) / 8
for _ in range(300):
    n = random.randint(1, 6); k = random.randint(0, 6); r, c = random.randrange(n), random.randrange(n)
    assert abs(_p688.knightProbability(n, k, r, c) - _bf688(n, k, r, c)) < 1e-9
print("P688 OK")

em({
 "num": 688, "title": "騎士在棋盤上的機率",
 "desc": "按步數的機率 DP：每格的機率平均分給八個馬步，出界的部分就消失；最後加總留在棋盤上的機率。",
 "zh": [
   "在 <code>n x n</code> 的西洋棋盤上，騎士（馬）從 <code>(row, column)</code> 出發，要走恰好 <code>k</code> 步。每一步從 8 個馬步方向中<strong>等機率</strong>隨機選一個（即使會走出棋盤）。",
   "騎士一旦走出棋盤就停止。回傳走完 k 步後騎士<strong>仍在棋盤上</strong>的機率。",
 ],
 "idea": [
   ("c", """【按步數 DP】
    dp[i][j] = 走了 t 步後在 (i, j) 的機率。
    下一步：每格的機率分成 8 份，分給 8 個目標格；
    目標在棋盤外 -> 那 1/8 的機率就消失了（騎士已離開）。

【答案】
    走完 k 步後所有格子的機率總和。

【反向的寫法】
    f(k, i, j) = 從 (i, j) 出發走 k 步仍在棋盤上的機率
              = 平均( f(k-1, 八個鄰居) )，出界為 0。
    和第 576 題（出界的路徑數）是同一類。"""),
 ],
 "approaches": [
   ap("解法", "按步數的機率 DP", [("c", S["p688"]), "驗證方式：和記憶化遞迴比對 300 組。"], "O(k · n² · 8)", "O(n²)", optimal=True),
 ],
 "edges": ["<strong>k = 0</strong> → 1。", "<strong>n ≤ 2</strong> → 任何馬步都出界，k ≥ 1 時機率 0。"],
 "follow": [("h", "馬可夫鏈"), ("c", "這是一個有吸收態（出界）的馬可夫鏈；k 步後的分布 = 轉移矩陣的 k 次方乘初始分布。k 很大時可用矩陣快速冪。")],
 "related": ["<strong>第 576 題 出界的路徑數</strong>", "<strong>第 935 題 騎士撥號器</strong>", "<strong>第 808 題 分湯</strong>"],
 "check": ["每一步的機率怎麼分配？", "出界的機率到哪裡去了？"],
})


# ==================== 689. Maximum Sum of 3 Non-Overlapping Subarrays ====================
S["p689"] = '''class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        w = [0] * (n - k + 1)                   # w[i]：從 i 開始、長度 k 的視窗和
        s = sum(nums[:k])
        w[0] = s
        for i in range(1, n - k + 1):
            s += nums[i + k - 1] - nums[i - 1]
            w[i] = s

        left = [0] * len(w)                     # left[i]：w[0..i] 中最大值的位置（相同取最左）
        for i in range(1, len(w)):
            left[i] = i if w[i] > w[left[i - 1]] else left[i - 1]
        right = [len(w) - 1] * len(w)           # right[i]：w[i..] 中最大值的位置（相同取最左）
        for i in range(len(w) - 2, -1, -1):
            right[i] = i if w[i] >= w[right[i + 1]] else right[i + 1]

        best = None
        for j in range(k, len(w) - k):          # ★ 枚舉中間的視窗 j，左右各取最好的
            a, c = left[j - k], right[j + k]
            cand = (w[a] + w[j] + w[c], a, j, c)
            if best is None or cand[0] > best[0]:
                best = cand
        return list(best[1:])'''

_p689 = S.load("p689")
assert _p689.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2) == [0, 3, 5]
assert _p689.maxSumOfThreeSubarrays([1, 2, 1, 2, 1, 2, 1, 2, 1], 2) == [0, 2, 4]
for _ in range(1000):
    k = random.randint(1, 3); n = random.randint(3 * k, 3 * k + 6)
    a = [random.randint(1, 5) for _ in range(n)]
    best = None
    for i in range(n - k + 1):
        for j in range(i + k, n - k + 1):
            for l in range(j + k, n - k + 1):
                c = (sum(a[i:i + k]) + sum(a[j:j + k]) + sum(a[l:l + k]), -i, -j, -l)
                if best is None or c > best: best = c
    assert _p689.maxSumOfThreeSubarrays(a, k) == [-best[1], -best[2], -best[3]]
print("P689 OK")

em({
 "num": 689, "title": "三個無重疊子陣列的最大和",
 "desc": "先算所有長度 k 的視窗和，再預處理「左邊最大」與「右邊最大」的位置，枚舉中間視窗 O(n)；注意字典序最小的平手規則。",
 "zh": [
   "給你整數陣列 <code>nums</code> 和整數 <code>k</code>，找出三個長度為 <code>k</code>、<strong>互不重疊</strong>的子陣列，使它們的總和最大。",
   "回傳三個子陣列的起始索引；有多個答案時回傳<strong>字典序最小</strong>的。",
 ],
 "idea": [
   ("c", """【視窗和】
    w[i] = nums[i..i+k-1] 的和，用滑動視窗 O(n) 算出。
    問題變成：選 i < j < l，j >= i + k、l >= j + k，使 w[i] + w[j] + w[l] 最大。

【枚舉中間的 j】
    左邊：w[0 .. j-k] 中最大的 -> 預處理 left[]
    右邊：w[j+k ..] 中最大的   -> 預處理 right[]
    每個 j O(1)。

【字典序最小】
    left：遇到相同值保留較左的（嚴格 > 才更新）。
    right：從右往左掃，遇到相同值更新成較左的（>= 就更新）。
    枚舉 j 由小到大，總和嚴格更大才更新。"""),
 ],
 "approaches": [
   ap("解法", "視窗和 + 左右最大值預處理", [("c", S["p689"]), "驗證方式：和枚舉所有三元組的暴力法（含字典序平手規則）比對 1000 組。"], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>多個相同總和</strong> → 字典序最小，left 與 right 的比較符號要小心。", "<strong>n = 3k</strong> → 唯一解 [0, k, 2k]。"],
 "follow": [("h", "一般化成 m 個子陣列"), ("c", "dp[t][i] = 在前 i 個位置中選 t 個不重疊視窗的最大和；dp[t][i] = max(dp[t][i−1], dp[t−1][i−k] + w[i−k])，O(m·n)，再回溯取字典序最小的答案。")],
 "related": ["<strong>第 123 題 買賣股票的最佳時機 III</strong>", "<strong>第 1031 題 兩個非重疊子陣列的最大和</strong>"],
 "check": ["為什麼枚舉中間的視窗最方便？", "left 與 right 在遇到相同值時分別怎麼處理？為什麼？"],
})


# ==================== 690. Employee Importance ====================
class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id; self.importance = importance; self.subordinates = subordinates

S["p690"] = '''class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp = {e.id: e for e in employees}          # id -> 員工，O(1) 查詢
        def total(i):
            e = emp[i]
            return e.importance + sum(total(s) for s in e.subordinates)   # ★ 自己 + 所有下屬（遞迴）
        return total(id)'''

_p690 = S.load("p690", extra={"Employee": Employee})
assert _p690.getImportance([Employee(1, 5, [2, 3]), Employee(2, 3, []), Employee(3, 3, [])], 1) == 11
assert _p690.getImportance([Employee(1, 2, [5]), Employee(5, -3, [])], 5) == -3
print("P690 OK")

em({
 "num": 690, "title": "員工的重要性",
 "desc": "先用雜湊表建立 id → 員工的索引，再從指定員工 DFS 加總自己與所有直接、間接下屬。",
 "zh": [
   "每位員工有唯一的 <code>id</code>、重要性 <code>importance</code>，以及<strong>直接下屬</strong>的 id 清單 <code>subordinates</code>。",
   "給你所有員工資料和一個 id，回傳這位員工與他<strong>所有直接和間接下屬</strong>的重要性總和。",
 ],
 "idea": [
   ("c", """【組織圖是一棵樹（森林）】
    從指定員工出發，DFS 或 BFS 走過整棵子樹，加總重要性。

【先建索引】
    員工資料是清單，按 id 查詢要 O(n)；
    先建雜湊表 id -> 員工，每次查詢 O(1)。"""),
 ],
 "approaches": [
   ap("解法", "雜湊表 + DFS", [("c", S["p690"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>沒有下屬</strong> → 只有自己的重要性。", "<strong>負的重要性</strong> → 照樣加總。"],
 "follow": [("h", "很深的組織？"), ("c", "遞迴深度可能很深時改用 BFS 或顯式堆疊。")],
 "related": ["<strong>第 1376 題 通知所有員工所需的時間</strong>", "<strong>第 559 題 N 叉樹的最大深度</strong>"],
 "check": ["為什麼要先建立 id → 員工的雜湊表？"],
})


# ==================== 691. Stickers to Spell Word ====================
S["p691"] = '''class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        n = len(target)
        full = (1 << n) - 1
        dp = [-1] * (1 << n)                    # dp[mask]：拼出 mask 中這些位置所需的最少貼紙數
        dp[0] = 0
        for mask in range(1 << n):
            if dp[mask] < 0:
                continue
            for s in stickers:
                cur = mask
                cnt = Counter(s)
                for i, ch in enumerate(target):
                    if not cur >> i & 1 and cnt[ch] > 0:
                        cnt[ch] -= 1            # ★ 用這張貼紙的字母填補還沒拼好的位置
                        cur |= 1 << i
                if cur != mask and (dp[cur] < 0 or dp[cur] > dp[mask] + 1):
                    dp[cur] = dp[mask] + 1
        return dp[full]'''

_p691 = S.load("p691")
assert _p691.minStickers(["with", "example", "science"], "thehat") == 3
assert _p691.minStickers(["notice", "possible"], "basicbasic") == -1
def _bf691(st, target):
    need = Counter(target); best = [10 ** 9]
    def go(need, used):
        if used >= best[0]: return
        if not +need: best[0] = used; return
        c = min(k for k in need if need[k] > 0)
        for s in st:
            if c in s:
                go(need - Counter(s), used + 1)
    go(need, 0)
    return best[0] if best[0] < 10 ** 9 else -1
for _ in range(400):
    st = ["".join(random.choice("abcd") for _ in range(random.randint(1, 4))) for _ in range(random.randint(1, 4))]
    t = "".join(random.choice("abcde") for _ in range(random.randint(1, 6)))
    assert _p691.minStickers(st, t) == _bf691(st, t), (st, t)
print("P691 OK")

em({
 "num": 691, "title": "貼紙拼詞",
 "desc": "target 最多 15 個字元：用位元遮罩表示「哪些位置已拼好」，對每個狀態嘗試每張貼紙，做最短步數的 DP。",
 "zh": [
   "給你 <code>n</code> 種貼紙（每種是一個單字，數量無限），你可以把貼紙上的字母一個個剪下來重新排列。",
   "回傳拼出字串 <code>target</code> 所需的<strong>最少貼紙張數</strong>；拼不出來則回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【狀態：target 的哪些位置已經填好】
    target 長度 <= 15 -> 用 15 位元的遮罩，最多 32768 種狀態。

【轉移】
    從狀態 mask 貼上一張貼紙 s：
        用 s 的字母去填 mask 中還沒填的位置（貪心地從左填起即可，
        因為同樣的字母填哪個位置都等價）。
    得到新狀態 cur，dp[cur] = min(dp[cur], dp[mask] + 1)。

【順序】
    新狀態的位元只會變多 -> cur > mask，
    依 mask 由小到大處理就是合法的 DP 順序。

【其他做法】
    記憶化搜尋「剩下需要的字母計數」，
    每次只嘗試包含「剩下需求中第一個字母」的貼紙來剪枝。"""),
 ],
 "approaches": [
   ap("解法", "位元遮罩 DP", [("c", S["p691"]), "驗證方式：和回溯搜尋（每次只試包含某個缺少字母的貼紙）比對 400 組。"], "O(2ⁿ · m · n)", "O(2ⁿ)", "n = |target|，m = 貼紙數", "", optimal=True),
 ],
 "edges": ["<strong>target 有任何貼紙都沒有的字母</strong> → −1。", "<strong>重複字母</strong> → 遮罩以位置為單位，自然處理。"],
 "follow": [("h", "集合覆蓋"), ("c", "本質是加權的集合覆蓋問題（NP 困難），只因為 target 很短才能用位元遮罩窮舉。")],
 "related": ["<strong>第 322 題 零錢兌換</strong>", "<strong>第 1125 題 最小的必要團隊</strong>", "<strong>第 943 題 最短超級串</strong>"],
 "check": ["遮罩的每一位代表什麼？", "為什麼依 mask 由小到大處理是正確的？"],
})


# ==================== 692. Top K Frequent Words ====================
S["p692"] = '''class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        # ★ 排序鍵：次數由大到小（取負），次數相同時字典序由小到大
        return heapq.nsmallest(k, cnt, key=lambda w: (-cnt[w], w))'''

_p692 = S.load("p692")
assert _p692.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
for _ in range(1500):
    ws = [random.choice(["a", "b", "c", "d", "e", "ab"]) for _ in range(random.randint(1, 10))]
    c = Counter(ws); k = random.randint(1, len(c))
    assert _p692.topKFrequent(ws, k) == sorted(c, key=lambda w: (-c[w], w))[:k]
print("P692 OK")

em({
 "num": 692, "title": "前 K 個高頻單字",
 "desc": "計數後依 (−次數, 單字) 排序取前 k 個；用大小為 k 的堆積可以做到 O(n log k)。",
 "zh": [
   "給你字串陣列 <code>words</code> 和整數 <code>k</code>，回傳出現次數最多的 <code>k</code> 個單字。",
   "結果依<strong>出現次數由高到低</strong>排列；次數相同時依<strong>字典序由小到大</strong>排列。",
   "<strong>進階：</strong>能做到 <code>O(n log k)</code> 時間、<code>O(n)</code> 額外空間嗎？",
 ],
 "idea": [
   ("c", """【計數 + 排序】
    排序鍵 (-次數, 單字)：次數大的在前，同次數字典序小的在前。
    O(n log n)。

【O(n log k)：大小為 k 的堆積】
    heapq.nsmallest(k, ..., key=...) 內部就是維護大小 k 的堆積。
    手寫的話：維護一個「最差的在頂端」的最小堆積，
    但比較規則要反過來（次數小的、或次數相同但字典序大的算比較差），
    需要自訂比較物件。

【桶排序】
    次數最多 n，可以依次數分桶，每桶內排序。"""),
 ],
 "approaches": [
   ap("解法", "計數 + 部分排序", [("c", S["p692"])], "O(n log k)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>次數相同</strong> → 字典序小的在前。", "<strong>k 等於不同單字數</strong> → 全部排序後回傳。"],
 "follow": [("h", "手寫堆積的比較"), ("c", "Python 的 heapq 是最小堆積。要淘汰「最差」的元素，堆頂必須是最差的：次數最小，次數相同時字典序最大。字串無法直接取負，所以要包一個自訂 __lt__ 的類別。")],
 "related": ["<strong>第 347 題 前 K 個高頻元素</strong>", "<strong>第 451 題 根據字元出現頻率排序</strong>", "<strong>第 973 題 最接近原點的 K 個點</strong>"],
 "check": ["排序鍵為什麼是 (−次數, 單字)？", "手寫堆積時，為什麼字串的比較方向不好處理？"],
})
