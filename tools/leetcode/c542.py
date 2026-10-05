# -*- coding: utf-8 -*-
"""第 542、543、546、547、551、552、553、554 題。"""
import random
from collections import Counter, deque
from functools import lru_cache
from itertools import product
from fractions import Fraction
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, nodes

S = Src()
random.seed(542)


# ==================== 542. 01 Matrix ====================
S["p542"] = '''class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dist = [[-1] * n for _ in range(m)]
        q = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))            # ★ 多源 BFS：所有 0 同時當起點
        while q:
            i, j = q.popleft()
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and dist[x][y] == -1:
                    dist[x][y] = dist[i][j] + 1     # 第一次被抵達時就是最短距離
                    q.append((x, y))
        return dist'''

_p542 = S.load("p542", extra={"deque": deque})
for _ in range(1000):
    m, n = random.randint(1, 5), random.randint(1, 5)
    M = [[random.randint(0, 1) for _ in range(n)] for _ in range(m)]
    if all(v for r in M for v in r):
        M[random.randrange(m)][random.randrange(n)] = 0
    zs = [(i, j) for i in range(m) for j in range(n) if M[i][j] == 0]
    want = [[min(abs(i - a) + abs(j - b) for a, b in zs) for j in range(n)] for i in range(m)]
    assert _p542.updateMatrix(M) == want
print("P542 OK")

em({
 "num": 542, "title": "01 矩陣",
 "desc": "反過來想：從所有 0 同時出發做多源 BFS，每格第一次被抵達的層數就是到最近 0 的距離。",
 "zh": ["給你一個由 0 和 1 組成的矩陣 <code>mat</code>，回傳一個同樣大小的矩陣：每個格子是它到<strong>最近的 0</strong> 的距離（上下左右相鄰的距離為 1）。"],
 "idea": [
   ("c", """【直接做：每個 1 各跑一次 BFS】
    O((mn)²)，太慢。

【反過來：從所有 0 同時出發】
    把所有 0 一起放進佇列當第 0 層（多源 BFS）。
    BFS 一層一層往外擴：第 d 層抵達的格子，到最近 0 的距離就是 d。
    每格只被抵達一次 -> O(mn)。

    想像在每個 0 同時滴下墨水，墨水同速擴散，
    每格最先被哪滴墨水染到，就是離哪個 0 最近。

【另一種解法：兩趟 DP】
    距離來自上/左或下/右：
    先由左上往右下掃（取上、左），再由右下往左上掃（取下、右）。"""),
 ],
 "approaches": [
   ap("解法", "多源 BFS", [("c", S["p542"]), "驗證方式：和「對每格算到所有 0 的曼哈頓距離取最小」比對（沒有障礙物時最短路徑就是曼哈頓距離）。"], "O(mn)", "O(mn)", optimal=True),
 ],
 "edges": ["<strong>本身是 0</strong> → 距離 0。", "<strong>只有一個 0</strong> → 多源退化成單源。"],
 "follow": [("h", "多源 BFS 家族"), ("c", "第 994 題（腐爛的橘子）、第 1162 題（地圖分析：離陸地最遠的海）、第 286 題（牆與門，付費）。共同點：答案是「到最近的某類格子的距離」。")],
 "related": ["<strong>第 994 題 腐爛的橘子</strong>", "<strong>第 1162 題 地圖分析</strong>", "<strong>第 1765 題 地圖中的最高點</strong>"],
 "check": ["為什麼要從 0 出發而不是從 1 出發？", "多源 BFS 中，第一次抵達為什麼就是最短距離？"],
})


# ==================== 543. Diameter of Binary Tree ====================
S["p543"] = '''class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(nd):                      # 回傳：從 nd 往下最長的路徑有幾個節點
            nonlocal res
            if not nd:
                return 0
            L, R = depth(nd.left), depth(nd.right)
            res = max(res, L + R)           # ★ 經過 nd 的最長路徑：左邊往下 + 右邊往下（邊數）
            return 1 + max(L, R)
        depth(root)
        return res'''

_p543 = S.load("p543")
def _bf543(t):
    adj = {}
    for nd in nodes(t):
        adj.setdefault(id(nd), [])
        for c in (nd.left, nd.right):
            if c:
                adj[id(nd)].append(id(c)); adj.setdefault(id(c), []).append(id(nd))
    best = 0
    for s in adj:
        d = {s: 0}; q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in d:
                    d[v] = d[u] + 1; q.append(v)
        best = max(best, max(d.values()))
    return best
for _ in range(1000):
    t = rand_tree(random.randint(1, 15))
    assert _p543.diameterOfBinaryTree(t) == _bf543(t)
print("P543 OK")

em({
 "num": 543, "title": "二元樹的直徑",
 "desc": "每條路徑都有一個「最高點」：在每個節點計算左深度 + 右深度，後序走訪一次完成。",
 "zh": [
   "給你二元樹的根節點，回傳樹的<strong>直徑</strong>：任意兩個節點之間最長路徑的<strong>邊數</strong>。",
   "這條路徑不一定經過根節點。",
 ],
 "idea": [
   ("c", """【每條路徑都有一個最高的節點】
    路徑從某個節點的左子樹往上爬到它，再往下走進右子樹。
    以 nd 為最高點的最長路徑 = 左子樹深度 + 右子樹深度（邊數）。

【一次後序走訪】
    depth(nd) 回傳以 nd 為端點往下的最長鏈（節點數），
    同時在每個節點用 L + R 更新全域答案。

【常見錯誤】
    只算根節點的 L + R —— 最長路徑可能完全在某個子樹裡。"""),
 ],
 "approaches": [
   ap("解法", "後序走訪：深度 + 全域最大", [("c", S["p543"]), "驗證方式：把樹當成無向圖，從每個節點做 BFS 取最遠距離，和這個解法比對 1000 棵隨機樹。"], "O(n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>單一節點</strong> → 0。", "<strong>一條鏈</strong> → n − 1。", "<strong>最長路徑不經過根</strong> → 全域變數處理。"],
 "follow": [("h", "一般樹的直徑"), ("c", "任意樹（不只二元樹）：從任意點 BFS 找最遠點 u，再從 u BFS 找最遠點 v，u–v 就是直徑（第 1245 題，付費）。")],
 "related": ["<strong>第 124 題 二元樹中的最大路徑和</strong>", "<strong>第 687 題 最長同值路徑</strong>", "<strong>第 104 題 二元樹的最大深度</strong>"],
 "check": ["depth 回傳的是節點數還是邊數？答案又是哪一個？", "為什麼要用全域變數記錄答案？"],
})


# ==================== 546. Remove Boxes ====================
S["p546"] = '''class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @cache
        def dp(l, r, k):
            # boxes[l..r]，而且 boxes[r] 的右邊還「黏著」k 個和 boxes[r] 同色的盒子
            if l > r:
                return 0
            while l < r and boxes[r - 1] == boxes[r]:   # 把同色的往左吸進來
                r -= 1
                k += 1
            # 選擇一：現在就把 boxes[r] 和黏著的 k 個一起移除
            res = dp(l, r - 1, 0) + (k + 1) ** 2
            # ★ 選擇二：先清掉中間 (i+1..r-1)，讓 boxes[i] 和 boxes[r] 接在一起
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
            return res
        return dp(0, len(boxes) - 1, 0)'''

_p546 = S.load("p546", extra={"cache": lru_cache(None)})
assert _p546.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
assert _p546.removeBoxes([1, 1, 1]) == 9 and _p546.removeBoxes([1]) == 1
@lru_cache(None)
def _bf546(t):
    if not t:
        return 0
    best = 0; i = 0
    while i < len(t):
        j = i
        while j < len(t) and t[j] == t[i]:
            j += 1
        best = max(best, (j - i) ** 2 + _bf546(t[:i] + t[j:]))
        i = j
    return best
for _ in range(400):
    b = [random.randint(1, 3) for _ in range(random.randint(1, 9))]
    _p546 = S.load("p546", extra={"cache": lru_cache(None)})
    assert _p546.removeBoxes(b) == _bf546(tuple(b))
print("P546 OK")

em({
 "num": 546, "title": "移除盒子",
 "desc": "區間 DP 必須多加一維「右邊黏著幾個同色盒子」：dp(l, r, k)，經典的難題狀態設計。",
 "zh": [
   "給你一排不同顏色的盒子 <code>boxes</code>（正整數代表顏色）。每一輪可以移除<strong>連續且同色</strong>的 <code>k</code> 個盒子（k ≥ 1），得到 <code>k × k</code> 分。",
   "重複直到沒有盒子，回傳可以得到的<strong>最高總分</strong>。",
 ],
 "idea": [
   ("c", """【為什麼一般區間 DP 不夠？】
    dp(l, r) 只看 boxes[l..r] 本身，
    但分數取決於「同色的能不能湊在一起再一起消」——
    這可能和區間外的盒子有關。

【多加一維：右邊黏著幾個同色】
    dp(l, r, k) = 處理 boxes[l..r]，
                  而且 boxes[r] 右邊還黏著 k 個同色盒子（之後一定和它一起消）。

【兩種選擇】
    1. 現在就把 boxes[r] 連同黏著的 k 個一起消：
           (k+1)² + dp(l, r-1, 0)
    2. 在 l..r-1 中找一個同色的 boxes[i]，
       先把中間 i+1..r-1 全部消掉，讓 boxes[i] 和 boxes[r] 接起來：
           dp(i+1, r-1, 0) + dp(l, i, k+1)

【小最佳化】
    先把 r 左邊連續同色的吸進 k，減少重複狀態。"""),
 ],
 "approaches": [
   ap("解法", "三維區間 DP（記憶化）", [
     ("c", S["p546"]),
     "驗證方式：和窮舉所有消除順序的暴力法比對 400 組。",
   ], "O(n⁴)", "O(n³)", "狀態 n³、轉移 O(n)", "", optimal=True),
 ],
 "edges": ["<strong>全同色</strong> → n²。", "<strong>全部不同色</strong> → n。"],
 "follow": [("h", "「區間外的資訊」要放進狀態"), ("c", "這是區間 DP 中最典型的「狀態不夠用就加維度」。類似的還有第 664 題（奇怪的印表機）、第 1000 題（合併石頭的最低成本）。")],
 "related": ["<strong>第 664 題 奇怪的印表機</strong>", "<strong>第 312 題 戳氣球</strong>", "<strong>第 1000 題 合併石頭的最低成本</strong>"],
 "check": ["為什麼 dp(l, r) 兩個參數不夠？", "k 代表什麼？", "選擇二為什麼要先把中間清掉？"],
})


# ==================== 547. Number of Provinces ====================
S["p547"] = '''class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]       # 路徑壓縮（隔代指向）
                x = parent[x]
            return x
        count = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    a, b = find(i), find(j)
                    if a != b:
                        parent[a] = b
                        count -= 1                  # ★ 每次成功合併，連通分量少一個
        return count'''

_p547 = S.load("p547")
for _ in range(1000):
    n = random.randint(1, 8)
    M = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.25:
                M[i][j] = M[j][i] = 1
    seen = set(); comps = 0
    for s in range(n):
        if s not in seen:
            comps += 1; st = [s]; seen.add(s)
            while st:
                u = st.pop()
                for v in range(n):
                    if M[u][v] and v not in seen:
                        seen.add(v); st.append(v)
    assert _p547.findCircleNum(M) == comps
print("P547 OK")

em({
 "num": 547, "title": "省份數量",
 "desc": "求無向圖的連通分量數：DFS/BFS 或聯合查找，每次成功合併分量數減一。",
 "zh": [
   "有 <code>n</code> 個城市。<code>isConnected[i][j] = 1</code> 表示城市 i 和 j 直接相連。相連具有傳遞性：a 連 b、b 連 c，則 a 和 c 間接相連。",
   "<strong>省份</strong>是一組直接或間接相連的城市，組外沒有城市與它們相連。回傳省份的數量。",
 ],
 "idea": [
   ("c", """【就是數連通分量】
    鄰接矩陣表示的無向圖，求連通分量數。

【DFS】
    對每個還沒拜訪的城市，從它出發 DFS 標記整個分量，計數加一。

【聯合查找（Union-Find）】
    一開始 n 個分量。
    每條邊 (i, j)：若 i、j 不在同一個集合就合併，分量數減一。
    路徑壓縮讓 find 接近 O(1)。"""),
 ],
 "approaches": [
   ap("解法", "聯合查找", [("c", S["p547"])], "O(n² α(n))", "O(n)", "", "", optimal=True),
 ],
 "edges": ["<strong>沒有任何邊</strong> → n。", "<strong>全部相連</strong> → 1。", "<strong>矩陣是對稱的</strong> → 只看上三角即可。"],
 "follow": [("h", "聯合查找的兩個最佳化"), ("c", "路徑壓縮（find 時把節點直接接到根附近）和按秩合併（矮的樹接到高的下面）。兩者一起用，均攤複雜度是反阿克曼函數 α(n)，實務上視為常數。")],
 "related": ["<strong>第 200 題 島嶼數量</strong>", "<strong>第 684 題 冗餘連接</strong>", "<strong>第 721 題 帳戶合併</strong>"],
 "check": ["為什麼每次成功合併分量數減一？", "路徑壓縮做了什麼？"],
})


# ==================== 551. Student Attendance Record I ====================
S["p551"] = '''class Solution:
    def checkRecord(self, s: str) -> bool:
        # 缺席少於 2 次，而且沒有連續 3 次（含以上）遲到
        return s.count("A") < 2 and "LLL" not in s'''

_p551 = S.load("p551")
for s in ("".join(p) for L in range(1, 7) for p in product("APL", repeat=L)):
    want = s.count("A") < 2 and all(s[i:i + 3] != "LLL" for i in range(len(s)))
    assert _p551.checkRecord(s) == want
print("P551 OK")

em({
 "num": 551, "title": "學生出勤紀錄 I",
 "desc": "兩個條件直接翻譯：A 少於兩個、不含 \"LLL\" 子字串。",
 "zh": [
   "出勤紀錄字串 <code>s</code> 只含三種字元：<code>'A'</code> 缺席、<code>'L'</code> 遲到、<code>'P'</code> 出席。",
   "學生能得到出勤獎勵，若同時滿足：總缺席<strong>少於 2 天</strong>，而且<strong>沒有連續 3 天以上</strong>遲到。判斷是否能得獎。",
 ],
 "idea": [
   ("c", """【條件直接翻譯】
    s.count('A') < 2
    "LLL" not in s      （連續 3 天以上遲到，一定包含 "LLL"）

【一趟掃描】
    也可以邊掃邊數 A 的個數與目前連續 L 的長度，提早結束。"""),
 ],
 "approaches": [
   ap("解法", "計數 + 子字串判斷", [("c", S["p551"])], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>\"LL\" 不算</strong> → 只有兩天。", "<strong>非連續的 L</strong> → \"LPLPL\" 可以。"],
 "follow": [("h", "反過來：數有多少合法紀錄"), ("c", "第 552 題：長度 n 的紀錄中有幾個能得獎——就要用 DP 或矩陣快速冪了。")],
 "related": ["<strong>第 552 題 學生出勤紀錄 II</strong>"],
 "check": ["為什麼檢查 \"LLL\" 就能涵蓋「3 天以上連續遲到」？"],
})


# ==================== 552. Student Attendance Record II ====================
S["p552"] = '''class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        # dp[a][l]：目前有 a 個 A（0 或 1）、結尾連續 l 個 L（0～2）的紀錄數
        dp = [[1, 0, 0], [0, 0, 0]]             # 長度 0：空紀錄
        for _ in range(n):
            nd = [[0] * 3 for _ in range(2)]
            for a in range(2):
                for l in range(3):
                    v = dp[a][l]
                    if not v:
                        continue
                    nd[a][0] = (nd[a][0] + v) % MOD             # 加 P：連續 L 歸零
                    if a == 0:
                        nd[1][0] = (nd[1][0] + v) % MOD         # 加 A：A 數 +1，連續 L 歸零
                    if l < 2:
                        nd[a][l + 1] = (nd[a][l + 1] + v) % MOD # ★ 加 L：只有連續 L 少於 2 才能加
            dp = nd
        return sum(map(sum, dp)) % MOD'''

_p552 = S.load("p552")
for n in range(1, 9):
    want = sum(1 for p in product("APL", repeat=n) if p.count("A") < 2 and "LLL" not in "".join(p))
    assert _p552.checkRecord(n) == want
assert _p552.checkRecord(10101) == 183236316
print("P552 OK")

em({
 "num": 552, "title": "學生出勤紀錄 II",
 "desc": "狀態 = (A 的數量, 結尾連續 L 的數量)，共 6 種；每加一個字元在狀態間轉移，O(n)。",
 "zh": [
   "沿用第 551 題的規則（缺席少於 2 天、沒有連續 3 天以上遲到）。給你整數 <code>n</code>，回傳長度為 <code>n</code> 的出勤紀錄中，有多少種能得到獎勵。",
   "答案可能很大，回傳對 <code>10⁹ + 7</code> 取模的結果。",
 ],
 "idea": [
   ("c", """【需要記住哪些資訊？】
    往紀錄後面再加一個字元時，要知道：
        目前有幾個 A（0 或 1）—— 決定能不能再加 A
        結尾連續幾個 L（0、1、2）—— 決定能不能再加 L
    共 2 × 3 = 6 種狀態。

【轉移】
    加 P：(a, l) -> (a, 0)
    加 A：(0, l) -> (1, 0)
    加 L：(a, l) -> (a, l+1)，只有 l < 2 時可以

【答案】
    長度 n 時 6 個狀態的總和。

【更快：矩陣快速冪】
    轉移是固定的 6×6 矩陣 -> O(6³ log n)。"""),
 ],
 "approaches": [
   ap("解法", "6 狀態 DP", [
     ("c", S["p552"]),
     "驗證方式：n ≤ 8 時和枚舉所有 3ⁿ 種紀錄比對；n = 10101 的答案是 183236316。",
   ], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>n = 1</strong> → 3。", "<strong>n = 2</strong> → 8（只有 \"AA\" 不行）。", "<strong>取模</strong> → 每次加法後都要取。"],
 "follow": [("h", "從「判斷」到「計數」"), ("c", "第 551 題是判斷一個紀錄；本題數所有紀錄。把「判斷時需要記住的資訊」當成 DP 的狀態，是這類計數題的通用思路（自動機 DP）。")],
 "related": ["<strong>第 551 題 學生出勤紀錄 I</strong>", "<strong>第 935 題 騎士撥號器</strong>", "<strong>第 1220 題 統計母音字母序列的數目</strong>"],
 "check": ["為什麼狀態需要兩個維度？", "加 L 的條件是什麼？"],
})


# ==================== 553. Optimal Division ====================
S["p553"] = '''class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        s = [str(x) for x in nums]
        if len(nums) <= 2:
            return "/".join(s)
        # ★ a / (b / c / d ...) = a · c · d ... / b：除了 b 以外全部變成乘
        return s[0] + "/(" + "/".join(s[1:]) + ")"'''

_p553 = S.load("p553")
def _all553(a):
    if len(a) == 1:
        return {Fraction(a[0])}
    out = set()
    for k in range(1, len(a)):
        for x in _all553(a[:k]):
            for y in _all553(a[k:]):
                out.add(x / y)
    return out
for _ in range(300):
    a = [random.randint(2, 9) for _ in range(random.randint(1, 5))]
    expr = _p553.optimalDivision(a)
    def ev(e):
        return eval(__import__("re").sub(r"(\d+)", r"Fraction(\1)", e))
    assert ev(expr) == max(_all553(a)), (a, expr)
assert _p553.optimalDivision([1000, 100, 10, 2]) == "1000/(100/10/2)"
print("P553 OK")

em({
 "num": 553, "title": "最優除法",
 "desc": "數學觀察：第一個數一定在分子、第二個數一定在分母，最好的情況是其餘全部變成分子。",
 "zh": [
   "給你一個正整數陣列 <code>nums</code>，相鄰的數之間做浮點除法，例如 <code>[2,3,4]</code> 代表 <code>2/3/4</code>。",
   "你可以在任意位置加括號改變運算順序。回傳讓結果<strong>最大</strong>的運算式字串，而且不能包含多餘的括號。",
 ],
 "idea": [
   ("c", """【不管怎麼加括號】
    nums[0] 一定在分子（它是最左邊的被除數）。
    nums[1] 一定在分母（nums[0] 直接或間接除以它）。

【其餘的呢？】
    a / (b / c / d) = a / (b / (c·d)) = a·c·d / b
    把 b 之後的全部包進括號，c、d…全部翻到分子。
    任何加括號的結果都是「某些數相乘 / 另一些數相乘」，
    而 b 一定在分母、a 一定在分子。
    題目的數都 >= 2：分子越多、分母越少，值越大 ->
    「只有 b 在分母、其餘全在分子」就是上界，而且這個構造達到了它。

【特例】
    1 個或 2 個數：不需要括號。"""),
 ],
 "approaches": [
   ap("解法", "數學構造", [
     ("c", S["p553"]),
     "驗證方式：用分數精確計算所有加括號方式的結果，確認構造出來的運算式等於最大值。",
   ], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>n = 1</strong> → \"a\"。", "<strong>n = 2</strong> → \"a/b\"（括號是多餘的）。"],
 "follow": [("h", "一般化：區間 DP"), ("c", "如果數字可以小於 1 或允許其他運算，就要用區間 DP 同時記錄每段的最大值與最小值（最大的 a/b 需要最小的 b）。")],
 "related": ["<strong>第 241 題 為運算式設計優先級</strong>", "<strong>第 282 題 給運算式添加運算子</strong>"],
 "check": ["哪兩個數的位置是固定的？", "為什麼 a/(b/c/d) 等於 a·c·d/b？"],
})


# ==================== 554. Brick Wall ====================
S["p554"] = '''class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = Counter()
        for row in wall:
            pos = 0
            for w in row[:-1]:              # 最右邊的磚縫是牆的邊界，不算
                pos += w
                edges[pos] += 1             # 這個位置有一條磚縫
        # ★ 穿過磚縫最多的位置，切到的磚最少
        return len(wall) - max(edges.values(), default=0)'''

_p554 = S.load("p554", extra={"Counter": Counter})
assert _p554.leastBricks([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]]) == 2
assert _p554.leastBricks([[1], [1], [1]]) == 3
for _ in range(1000):
    W = random.randint(2, 7)
    wall = []
    for _ in range(random.randint(1, 5)):
        row, s = [], 0
        while s < W:
            w = random.randint(1, W - s); row.append(w); s += w
        wall.append(row)
    best = len(wall)
    for x in range(1, W):
        cut = 0
        for row in wall:
            s = 0; edge = False
            for w in row:
                s += w
                if s == x: edge = True
            cut += not edge
        best = min(best, cut)
    assert _p554.leastBricks(wall) == best
print("P554 OK")

em({
 "num": 554, "title": "磚牆",
 "desc": "與其數切到幾塊磚，不如數每個位置有幾條磚縫：磚縫最多的位置切到的磚最少。",
 "zh": [
   "一面磚牆有 <code>n</code> 列，每列的磚塊高度相同、寬度不同，但每列的總寬度相同。<code>wall[i]</code> 是第 i 列由左到右的磚塊寬度。",
   "從牆頂畫一條垂直線到底，若線剛好經過磚縫就不算穿過該磚。回傳這條線<strong>最少</strong>要穿過幾塊磚。不能沿著牆的兩側邊緣畫。",
 ],
 "idea": [
   ("c", """【換個角度數】
    在位置 x 畫線：穿過的磚數 = 列數 - 在 x 有磚縫的列數。
    要最少穿過 -> 找磚縫最多的位置。

【數磚縫】
    每一列做前綴和，每個前綴和（最後一個除外）就是一條磚縫的位置。
    用雜湊表數每個位置的磚縫數。

    牆寬可能高達 2^31，不能枚舉 x；
    但磚縫總數 = 磚塊總數，最多 2×10⁴。"""),
 ],
 "approaches": [
   ap("解法", "前綴和 + 雜湊表數磚縫", [("c", S["p554"])], "O(磚塊總數)", "O(磚塊總數)", optimal=True),
 ],
 "edges": ["<strong>每列只有一塊磚</strong> → 沒有磚縫，答案是列數（max 用 default=0）。", "<strong>最右邊的邊界</strong> → 不能算成磚縫。"],
 "follow": [("h", "補集思維"), ("c", "「最少穿過幾塊」= 總列數 −「最多避開幾塊」。當直接數很難時，數它的補集常常比較容易。")],
 "related": ["<strong>第 560 題 和為 K 的子陣列</strong>"],
 "check": ["為什麼最後一塊磚的右緣不能算？", "為什麼不能直接枚舉每個 x？"],
})
