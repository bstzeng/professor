# -*- coding: utf-8 -*-
"""第 310、312、313、315、316、318 題。"""
import random
import itertools
import functools
from collections import deque
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(310)
_DQ = {"deque": deque}


# ==================== 310. Minimum Height Trees ====================
S["p310"] = '''class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        leaves = [v for v in range(n) if len(adj[v]) == 1]
        remaining = n
        # ★ 一層一層剝掉葉子，最後剩下的 1～2 個點就是中心
        while remaining > 2:
            remaining -= len(leaves)
            nxt = []
            for leaf in leaves:
                parent = adj[leaf].pop()          # 葉子只有一個鄰居
                adj[parent].remove(leaf)
                if len(adj[parent]) == 1:         # 鄰居變成新的葉子
                    nxt.append(parent)
            leaves = nxt
        return leaves'''

S["p310_diam"] = '''class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def bfs(src):                              # 回傳最遠點與 parent 陣列
            parent = [-1] * n
            seen = [False] * n
            seen[src] = True
            q, last = deque([src]), src
            while q:
                last = q.popleft()
                for w in adj[last]:
                    if not seen[w]:
                        seen[w] = True
                        parent[w] = last
                        q.append(w)
            return last, parent

        u, _ = bfs(0)                              # 離 0 最遠的點 u 是直徑的一端
        v, parent = bfs(u)                         # 離 u 最遠的點 v 是另一端
        path = [v]
        while path[-1] != u:
            path.append(parent[path[-1]])
        k = len(path)
        # ★ 直徑的中點（1 個或 2 個）就是最小高度樹的根
        return [path[k // 2]] if k % 2 else [path[k // 2 - 1], path[k // 2]]'''

_p310 = [S.load("p310"), S.load("p310_diam", extra=_DQ)]


def _mht_ref(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)

    def height(r):
        d = {r: 0}
        q = deque([r])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if y not in d:
                    d[y] = d[x] + 1
                    q.append(y)
        return max(d.values())
    hs = [height(r) for r in range(n)]
    m = min(hs)
    return [r for r in range(n) if hs[r] == m]


for n, e, want in [(4, [[1, 0], [1, 2], [1, 3]], [1]), (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]], [3, 4]), (1, [], [0]), (2, [[0, 1]], [0, 1])]:
    for sol in _p310:
        assert sorted(sol.findMinHeightTrees(n, e)) == want
for _ in range(1500):
    n = random.randrange(1, 15)
    edges = [[i, random.randrange(i)] for i in range(1, n)]
    want = _mht_ref(n, edges)
    for sol in _p310:
        assert sorted(sol.findMinHeightTrees(n, [e[:] for e in edges])) == want, (n, edges, sol)
print("P310 OK")

_P310_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">像剝洋蔥：一層一層拿掉葉子（度數為 1 的點）</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="60" cy="70" r="15" fill="none" stroke="#ff8a65"/><text x="60" y="74" fill="#ff8a65">0</text>
              <circle cx="60" cy="130" r="15" fill="none" stroke="#ff8a65"/><text x="60" y="134" fill="#ff8a65">1</text>
              <circle cx="60" cy="190" r="15" fill="none" stroke="#ff8a65"/><text x="60" y="194" fill="#ff8a65">2</text>
              <circle cx="170" cy="130" r="15" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="170" y="134" fill="var(--gold)">3</text>
              <circle cx="280" cy="130" r="15" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="280" y="134" fill="var(--gold)">4</text>
              <circle cx="390" cy="130" r="15" fill="none" stroke="#ff8a65"/><text x="390" y="134" fill="#ff8a65">5</text>
            </g>
            <g stroke="var(--text-muted)">
              <line x1="74" y1="76" x2="156" y2="124"/><line x1="75" y1="130" x2="155" y2="130"/><line x1="74" y1="184" x2="156" y2="136"/>
              <line x1="185" y1="130" x2="265" y2="130"/><line x1="295" y1="130" x2="375" y2="130"/>
            </g>
            <text x="60" y="226" text-anchor="middle" fill="#ff8a65" font-size="11">第 1 輪剝掉</text>
            <text x="390" y="160" text-anchor="middle" fill="#ff8a65" font-size="11">第 1 輪剝掉</text>
            <text x="225" y="100" text-anchor="middle" fill="var(--gold)" font-size="12">剩下 3、4 → 答案</text>
            <text x="440" y="70" fill="var(--text)" font-size="12">★ 最小高度樹的根</text>
            <text x="440" y="90" fill="var(--text)" font-size="12">= 樹的「中心」</text>
            <text x="440" y="110" fill="var(--text)" font-size="12">= 最長路徑（直徑）</text>
            <text x="440" y="130" fill="var(--text)" font-size="12">　的中點</text>
            <text x="440" y="164" fill="var(--text-muted)" font-size="12">直徑 0-3-4-5 長 3 條邊，</text>
            <text x="440" y="184" fill="var(--text-muted)" font-size="12">中點落在 3、4 之間</text>
            <text x="440" y="204" fill="var(--text-muted)" font-size="12">→ 兩個答案</text>'''

emit({
 "num": 310, "slug": "minimum-height-trees",
 "en": [
   "A tree is an undirected graph in which any two vertices are connected by <em>exactly</em> one path. In other words, any connected graph without simple cycles is a tree.",
   "Given a tree of <code>n</code> nodes labelled from <code>0</code> to <code>n - 1</code>, and an array of <code>n - 1</code> <code>edges</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> "
   "indicates that there is an undirected edge between the two nodes, you can choose any node of the tree as the root. When you select a node <code>x</code> as the root, the result tree has height <code>h</code>. "
   "Among all possible rooted trees, those with minimum height (i.e. <code>min(h)</code>) are called <strong>minimum height trees</strong> (MHTs).",
   "Return <em>a list of all <strong>MHTs'</strong> root labels</em>. You can return the answer in <strong>any order</strong>.",
   "The <strong>height</strong> of a rooted tree is the number of edges on the longest downward path between the root and a leaf.",
 ],
 "zh": [
   "樹是任兩點之間恰好有一條路徑的無向圖。給你一棵有 <code>n</code> 個節點（編號 <code>0</code> 到 <code>n - 1</code>）的樹，以及 <code>n - 1</code> 條邊。",
   "你可以選任何一個節點當根。選 <code>x</code> 當根時，樹的高度是 <code>h</code>（根到最遠葉子的邊數）。所有選法中，高度最小的叫做<strong>最小高度樹</strong>。",
   "回傳所有最小高度樹的<strong>根</strong>，順序不限。",
 ],
 "examples": """範例 1
  輸入：n = 4, edges = [[1,0],[1,2],[1,3]]
  輸出：[1]

範例 2
  輸入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
  輸出：[3,4]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 2 × 10⁴",
   "<code>edges.length == n - 1</code>",
   "0 ≤ <code>a<sub>i</sub>, b<sub>i</sub></code> &lt; <code>n</code>，<code>a<sub>i</sub> != b<sub>i</sub></code>",
   "所有 <code>(a<sub>i</sub>, b<sub>i</sub>)</code> 互不相同，而且保證是一棵樹",
 ],
 "idea": [
   ("fig", _P310_FIG, "0 0 640 240"),
   ("c", """【暴力：每個點當根做一次 BFS】
    O(n²)，n = 2×10⁴ 時 4×10⁸，太慢。

【直覺：根應該在樹的「正中間」】
    樹高 = 根到最遠點的距離。
    最遠的點一定是某條最長路徑（直徑）的端點，
    所以根應該選在直徑的中點 —— 離兩端都一樣近。

【方法一：剝葉子（拓樸排序的變形）】
    葉子不可能是答案（除非 n <= 2）——
    把它換成它的鄰居，高度只會更小或相同。
    所以一層一層剝掉所有葉子，
    剩下 1 或 2 個點時停止，它們就是中心。

【為什麼最後剩 1 或 2 個？】
    直徑長度是偶數 -> 中點是一個點
    直徑長度是奇數 -> 中點在一條邊上 -> 兩個端點都是答案

【方法二：直接找直徑】
    從任意點 BFS 到最遠點 u（u 一定是直徑的一端），
    再從 u BFS 到最遠點 v，路徑 u..v 就是直徑，取中點。"""),
 ],
 "approaches": [
   ap("解法一", "剝葉子", [
     ("c", S["p310"]),
   ], "O(n)", "O(n)", "", "", optimal=True),

   ap("解法二", "兩次 BFS 找直徑中點", [
     ("c", S["p310_diam"]),
     ("c", """【為什麼從任意點出發的最遠點，一定是直徑的端點？】
    這是樹的經典性質（反證法）：
    如果最遠點 u 不是任何直徑的端點，
    可以構造出一條比直徑更長的路徑，矛盾。"""),
   ], "O(n)", "O(n)", "", ""),
 ],
 "compare": (["解法", "時間", "空間"],
   [["暴力 BFS", "O(n²)", "O(n)"],
    ["一、剝葉子", "O(n)", "O(n) ✔"],
    ["二、找直徑", "O(n)", "O(n)"]]),
 "edges": [
   "<strong>n = 1</strong> → <code>[0]</code>，沒有邊。",
   "<strong>n = 2</strong> → <code>[0, 1]</code>，兩個都是葉子，也都是答案。",
   "<strong>星狀圖</strong> → 中心點。",
   "<strong>一條鏈</strong> → 中間的 1 或 2 個點。",
 ],
 "follow": [
   ("h", "換根 DP"),
   ("c", "另一種 O(n) 方法：先以 0 為根算出每個點「往下」的最大深度，再第二次 DFS 把「往上」的最大距離傳下去，每個點的高度 = max(往下, 往上)。這個技巧叫換根 DP，第 834 題也用得到。"),
 ],
 "related": [
   "<strong>第 207 題 課程表</strong> —— 同樣是一層一層剝掉入度 0 的點",
   "<strong>第 1245 題 樹的直徑</strong>（付費）",
   "<strong>第 834 題 樹中距離之和</strong> —— 換根 DP",
 ],
 "check": [
   "為什麼最小高度樹的根一定在直徑的中點？",
   "為什麼答案最多只有 2 個？",
   "剝葉子什麼時候停止？",
 ],
})


# ==================== 312. Burst Balloons ====================
S["p312"] = '''class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a = [1] + nums + [1]                   # 兩端補上虛擬氣球 1
        n = len(a)
        # dp[i][j]：開區間 (i, j) 裡的氣球全部戳破，最多拿幾枚硬幣
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):             # 區間長度由小到大
            for i in range(n - length):
                j = i + length
                best = 0
                for k in range(i + 1, j):      # ★ k 是 (i, j) 中「最後」被戳破的
                    best = max(best, dp[i][k] + a[i] * a[k] * a[j] + dp[k][j])
                dp[i][j] = best
        return dp[0][n - 1]'''

S["p312_memo"] = '''class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        a = [1] + nums + [1]

        @functools.lru_cache(None)
        def solve(i: int, j: int) -> int:      # 開區間 (i, j)
            return max((solve(i, k) + a[i] * a[k] * a[j] + solve(k, j)
                        for k in range(i + 1, j)), default=0)

        return solve(0, len(a) - 1)'''

_p312 = [S.load(x) for x in ("p312", "p312_memo")]


def _burst_ref(nums):
    best = 0
    for perm in itertools.permutations(range(len(nums))):
        alive = list(range(len(nums)))
        tot = 0
        for p in perm:
            k = alive.index(p)
            l = nums[alive[k - 1]] if k > 0 else 1
            r = nums[alive[k + 1]] if k + 1 < len(alive) else 1
            tot += l * nums[p] * r
            alive.pop(k)
        best = max(best, tot)
    return best


for nums, want in [([3, 1, 5, 8], 167), ([1, 5], 10), ([7], 7)]:
    for sol in _p312:
        assert sol.maxCoins(nums) == want
for _ in range(300):
    nums = [random.randrange(0, 8) for _ in range(random.randrange(1, 7))]
    want = _burst_ref(nums)
    for sol in _p312:
        assert sol.maxCoins(nums) == want
print("P312 OK")

_P312_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">反過來想：k 是區間 (i, j) 裡「最後」被戳破的氣球</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="60" cy="80" r="20" fill="none" stroke="var(--text-muted)" stroke-width="2"/><text x="60" y="85" fill="var(--text)">i</text>
              <circle cx="140" cy="80" r="16" fill="none" stroke="var(--accent)" stroke-dasharray="3 3"/>
              <circle cx="200" cy="80" r="16" fill="none" stroke="var(--accent)" stroke-dasharray="3 3"/>
              <circle cx="280" cy="80" r="20" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="280" y="85" fill="var(--gold)">k</text>
              <circle cx="360" cy="80" r="16" fill="none" stroke="#ff8a65" stroke-dasharray="3 3"/>
              <circle cx="420" cy="80" r="16" fill="none" stroke="#ff8a65" stroke-dasharray="3 3"/>
              <circle cx="500" cy="80" r="20" fill="none" stroke="var(--text-muted)" stroke-width="2"/><text x="500" y="85" fill="var(--text)">j</text>
            </g>
            <text x="170" y="126" text-anchor="middle" fill="var(--accent)" font-size="12">dp[i][k]</text>
            <text x="170" y="144" text-anchor="middle" fill="var(--text-muted)" font-size="11">先戳完</text>
            <text x="390" y="126" text-anchor="middle" fill="#ff8a65" font-size="12">dp[k][j]</text>
            <text x="390" y="144" text-anchor="middle" fill="var(--text-muted)" font-size="11">先戳完</text>
            <text x="280" y="126" text-anchor="middle" fill="var(--gold)" font-size="12">最後戳 k</text>
            <text x="280" y="144" text-anchor="middle" fill="var(--gold)" font-size="11">得 a[i]·a[k]·a[j]</text>
            <text x="20" y="182" fill="var(--text)" font-size="12">k 還活著的時候，左右兩邊被 k 隔開，互不影響 → 可以分成兩個獨立的子問題。</text>
            <text x="20" y="206" fill="var(--text)" font-size="12">k 最後才戳，那時它的鄰居就是區間的兩個邊界 i、j。</text>
            <text x="20" y="232" fill="var(--gold)" font-size="12">★ 如果改成「k 是第一個戳的」，戳完之後左右兩半會黏在一起，子問題就不獨立了 ✘</text>'''

emit({
 "num": 312, "slug": "burst-balloons",
 "en": [
   "You are given <code>n</code> balloons, indexed from <code>0</code> to <code>n - 1</code>. Each balloon is painted with a number on it represented by an array <code>nums</code>. You are asked to burst all the balloons.",
   "If you burst the <code>i<sup>th</sup></code> balloon, you will get <code>nums[i - 1] * nums[i] * nums[i + 1]</code> coins. If <code>i - 1</code> or <code>i + 1</code> goes out of bounds of the array, then treat it as if there is a balloon with a <code>1</code> painted on it.",
   "Return <em>the maximum coins you can collect by bursting the balloons wisely</em>.",
 ],
 "zh": [
   "有 <code>n</code> 個氣球，編號 <code>0</code> 到 <code>n - 1</code>，每個氣球上寫著一個數字 <code>nums[i]</code>。你要把所有氣球戳破。",
   "戳破第 <code>i</code> 個氣球可以得到 <code>nums[i - 1] * nums[i] * nums[i + 1]</code> 枚硬幣——這裡的左右鄰居是<strong>目前還沒被戳破</strong>的相鄰氣球；超出邊界就當作寫著 <code>1</code>。",
   "回傳最多能拿到幾枚硬幣。",
 ],
 "examples": """範例 1
  輸入：nums = [3,1,5,8]
  輸出：167
  說明：
    nums = [3,1,5,8] -> [3,5,8] -> [3,8] -> [8] -> []
    coins = 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 167

範例 2
  輸入：nums = [1,5]
  輸出：10""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 300",
   "0 ≤ <code>nums[i]</code> ≤ 100",
 ],
 "idea": [
   ("fig", _P312_FIG, "0 0 640 246"),
   ("c", """【困難點】
    戳破一個氣球後，它的左右鄰居會「黏在一起」變成新的鄰居。
    如果先選「第一個戳哪個」，剩下的左右兩半會互相影響 ✘

【逆向思考：選「最後一個」戳哪個】
    在開區間 (i, j) 裡，假設 k 是最後才戳的：
        - k 還在的時候，(i, k) 和 (k, j) 被 k 隔開，互不影響
        - 最後戳 k 時，它的鄰居只剩 i 和 j
    -> dp[i][j] = max over k of  dp[i][k] + a[i]*a[k]*a[j] + dp[k][j]

【技巧】
    兩端補上 1：a = [1] + nums + [1]
    答案 = dp[0][n+1]（整個開區間）

【填表順序】
    dp[i][j] 依賴更短的區間 -> 按區間長度由小到大。
    O(n³)，n = 300 時約 4.5 × 10⁶ 次轉移。"""),
 ],
 "approaches": [
   ap("解法一", "記憶化搜尋", [
     ("c", S["p312_memo"]),
   ], "O(n³)", "O(n²)", "", ""),

   ap("解法二", "區間 DP", [
     ("c", S["p312"]),
   ], "O(n³)", "O(n²)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、記憶化", "O(n³)", "O(n²)"],
    ["二、區間 DP", "O(n³)", "O(n²) ✔"]]),
 "edges": [
   "<strong>只有一個氣球</strong> → 1 × nums[0] × 1。",
   "<strong>有 0</strong> → 乘積為 0，照樣處理；把 0 最先戳最划算。",
   "<strong>開區間</strong> → dp[i][i+1] = 0（中間沒有氣球）。",
 ],
 "follow": [
   ("h", "區間 DP 的標誌"),
   ("c", """「合併／拆解一段連續的東西，操作會影響左右鄰居」→ 想區間 DP。
關鍵往往是選對「分割點」的意義：本題是最後戳的，
第 1000 題合併石頭是最後一次合併，第 1039 題多邊形三角剖分是和底邊組成三角形的那個頂點。"""),
 ],
 "related": [
   "<strong>第 1000 題 合併石頭的最低成本</strong>",
   "<strong>第 1039 題 多邊形三角剖分的最低得分</strong>",
   "<strong>第 546 題 移除盒子</strong>",
   "<strong>第 241 題 為運算式設計優先順序</strong>",
 ],
 "check": [
   "為什麼選「第一個戳」會讓子問題不獨立？",
   "最後戳 k 時，它的左右鄰居是誰？",
   "為什麼要在兩端補上 1？",
   "dp 表要按照什麼順序填？",
 ],
})


# ==================== 313. Super Ugly Number ====================
S["p313"] = '''class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        ugly = [1]
        idx = [0] * k                         # idx[t]：primes[t] 下一個要乘的醜數位置
        nxt = primes[:]                       # nxt[t] = ugly[idx[t]] * primes[t]
        for _ in range(n - 1):
            m = min(nxt)
            ugly.append(m)
            for t in range(k):                # ★ 所有等於 m 的都要前進（去重）
                if nxt[t] == m:
                    idx[t] += 1
                    nxt[t] = ugly[idx[t]] * primes[t]
        return ugly[-1]'''

S["p313_heap"] = '''class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        heap = [(p, p, 0) for p in primes]    # (候選值, 質數, 乘的是 ugly[哪個位置])
        heapq.heapify(heap)
        while len(ugly) < n:
            val, p, i = heapq.heappop(heap)
            if val != ugly[-1]:               # 跳過重複
                ugly.append(val)
            heapq.heappush(heap, (ugly[i + 1] * p, p, i + 1))
        return ugly[-1]'''

_p313 = [S.load(x) for x in ("p313", "p313_heap")]
for n, pr, want in [(12, [2, 7, 13, 19], 32), (1, [2, 3, 5], 1), (10, [2, 3, 5], 12)]:
    for sol in _p313:
        assert sol.nthSuperUglyNumber(n, pr) == want
_PR = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
for _ in range(300):
    pr = sorted(random.sample(_PR, random.randrange(1, 5)))
    n = random.randrange(1, 60)
    got, frontier = {1}, [1]                   # 參考答案：BFS 產生所有 <= 上界的醜數
    lim = max(pr) ** 7
    while frontier:
        nxt = []
        for v in frontier:
            for p in pr:
                if v * p <= lim and v * p not in got:
                    got.add(v * p)
                    nxt.append(v * p)
        frontier = nxt
    seq = sorted(got)[:n]
    if len(seq) < n or seq[-1] * min(pr) > lim:
        continue
    for sol in _p313:
        assert sol.nthSuperUglyNumber(n, pr) == seq[-1], (n, pr)
print("P313 OK")

emit({
 "num": 313, "slug": "super-ugly-number",
 "en": [
   "A <strong>super ugly number</strong> is a positive integer whose prime factors are in the array <code>primes</code>.",
   "Given an integer <code>n</code> and an array of integers <code>primes</code>, return <em>the</em> <code>n<sup>th</sup></code> <em><strong>super ugly number</strong></em>.",
   "The <code>n<sup>th</sup></code> <strong>super ugly number</strong> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> signed integer.",
 ],
 "zh": [
   "<strong>超級醜數</strong>：質因數全部都在陣列 <code>primes</code> 中的正整數。",
   "給你 <code>n</code> 和 <code>primes</code>，回傳第 <code>n</code> 個超級醜數（保證在 32 位元有號整數範圍內）。",
 ],
 "examples": """範例 1
  輸入：n = 12, primes = [2,7,13,19]
  輸出：32
  說明：前 12 個是 [1,2,4,7,8,13,14,16,19,26,28,32]

範例 2
  輸入：n = 1, primes = [2,3,5]
  輸出：1""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 10⁵",
   "1 ≤ <code>primes.length</code> ≤ 100",
   "2 ≤ <code>primes[i]</code> ≤ 1000",
   "<code>primes[i]</code> 保證是質數，而且互不相同、遞增排列",
 ],
 "idea": [
   ("c", """【第 264 題的推廣：3 個質數 -> k 個質數】
    每個超級醜數（除了 1）= 某個更小的超級醜數 × 某個質數。
    k 條有序序列：ugly × primes[0]、ugly × primes[1]、...
    用 k 個指標做多路合併。

【每一步】
    k 個候選 nxt[t] = ugly[idx[t]] × primes[t]
    取最小值 m 加入序列，
    所有 nxt[t] == m 的指標都要前進（去重）。

【複雜度】
    直接掃 k 個候選：O(nk)
    用堆積：O(n log k)（但重複值要跳過）"""),
 ],
 "approaches": [
   ap("解法一", "k 個指標", [
     ("c", S["p313"]),
   ], "O(nk)", "O(n + k)", "", "", optimal=True),

   ap("解法二", "最小堆積", [
     ("c", S["p313_heap"]),
     "堆積裡每個質數各一個候選。取出後，把同一個質數的下一個候選放回去；和前一個相同的值直接跳過。",
   ], "O(n log k)", "O(n + k)", "含重複的彈出，實際次數會多一些", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、k 指標", "O(nk)", "k ≤ 100 時很快 ✔"],
    ["二、堆積", "O(n log k)", "k 很大時更好"]]),
 "edges": [
   "<strong>n = 1</strong> → 1。",
   "<strong>只有一個質數</strong> → 答案是 p^(n−1)。",
   "<strong>重複值</strong>（例如 14 = 2×7 = 7×2）→ 必須去重。",
 ],
 "follow": [
   ("h", "中間值溢位"),
   ("c", "答案保證在 32 位元內，但候選值 ugly[idx]×p 可能超過——其他語言要用 64 位元或先判斷。Python 沒有這個問題。"),
 ],
 "related": [
   "<strong>第 264 題 醜數 II</strong>",
   "<strong>第 23 題 合併 K 個排序鏈結串列</strong>",
 ],
 "check": [
   "為什麼可以把超級醜數看成 k 條有序序列的合併？",
   "為什麼所有等於最小值的指標都要前進？",
 ],
})


# ==================== 315. Count of Smaller Numbers After Self ====================
S["p315_bit"] = '''class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 座標壓縮：把值換成名次 1..m
        rank = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
        m = len(rank)
        tree = [0] * (m + 1)                  # 樹狀陣列：tree 以「名次」為索引

        def add(i):
            while i <= m:
                tree[i] += 1
                i += i & -i

        def query(i):                         # 名次 1..i 已經出現幾次
            s = 0
            while i:
                s += tree[i]
                i -= i & -i
            return s

        res = []
        for x in reversed(nums):              # ★ 由右往左：樹裡放的都是「右邊」的數
            r = rank[x]
            res.append(query(r - 1))          # 比 x 小 = 名次 < r
            add(r)
        return res[::-1]'''

S["p315_merge"] = '''class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        idx = list(range(n))                  # 對「索引」排序，才能知道答案該加到誰身上

        def sort(lo: int, hi: int) -> None:   # 排序 idx[lo:hi]（依 nums 值）
            if hi - lo <= 1:
                return
            mid = (lo + hi) // 2
            sort(lo, mid)
            sort(mid, hi)
            merged = []
            j = mid
            for i in range(lo, mid):
                # ★ 右半中比 nums[idx[i]] 小的，會在 i 之前被放進 merged
                while j < hi and nums[idx[j]] < nums[idx[i]]:
                    merged.append(idx[j])
                    j += 1
                res[idx[i]] += j - mid        # 右半已經放進去的個數
                merged.append(idx[i])
            merged.extend(idx[j:hi])
            idx[lo:hi] = merged

        sort(0, n)
        return res'''

S["p315_bisect"] = '''class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        seen = []                             # 右邊的數，保持排序
        res = []
        for x in reversed(nums):
            i = bisect.bisect_left(seen, x)   # 比 x 小的個數
            res.append(i)
            seen.insert(i, x)                 # list 插入 O(n)
        return res[::-1]'''

_p315 = [S.load(x) for x in ("p315_bit", "p315_merge", "p315_bisect")]
for nums, want in [([5, 2, 6, 1], [2, 1, 1, 0]), ([-1], [0]), ([-1, -1], [0, 0])]:
    for sol in _p315:
        assert sol.countSmaller(nums) == want
for _ in range(3000):
    nums = [random.randint(-6, 6) for _ in range(random.randrange(1, 14))]
    want = [sum(nums[j] < nums[i] for j in range(i + 1, len(nums))) for i in range(len(nums))]
    for sol in _p315:
        assert sol.countSmaller(nums) == want, (nums, sol)
print("P315 OK")

emit({
 "num": 315, "slug": "count-of-smaller-numbers-after-self",
 "en": [
   "Given an integer array <code>nums</code>, return <em>an integer array</em> <code>counts</code> <em>where</em> <code>counts[i]</code> <em>is the number of smaller elements to the right of</em> <code>nums[i]</code>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，回傳陣列 <code>counts</code>，其中 <code>counts[i]</code> 是 <code>nums[i]</code> <strong>右邊</strong>比它<strong>小</strong>的元素個數。",
 ],
 "examples": """範例 1
  輸入：nums = [5,2,6,1]
  輸出：[2,1,1,0]
  說明：
    5 的右邊有 2 個更小的（2 和 1）
    2 的右邊有 1 個更小的（1）
    6 的右邊有 1 個更小的（1）
    1 的右邊有 0 個

範例 2
  輸入：nums = [-1,-1]
  輸出：[0,0]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【暴力 O(n²)：n = 10⁵ 太慢】

【方法一：由右往左 + 樹狀陣列】
    從最右邊開始，把看過的數「登記」起來。
    處理 nums[i] 時，登記簿裡剛好是它右邊的所有數，
    問：登記簿裡比 nums[i] 小的有幾個？

    登記簿用樹狀陣列，以「值」為索引：
        登記 x：tree 在位置 x 加 1
        查詢比 x 小的個數：前綴和 [1, x-1]
    值的範圍可能很大或有負數 -> 先座標壓縮成名次 1..m。

【方法二：合併排序】
    這題本質上是「逆序數」問題的每個元素版本。
    合併左右兩半時：
        左半的元素 a 被放進結果時，
        右半中已經被放進去的元素，都比 a 小、而且在 a 的右邊
        -> counts[a 的原索引] += 右半已放進去的個數
    要排序的是「索引」，才能把答案加回原位置。

【方法三：維持排序陣列 + 二分】
    概念最簡單，但 list.insert 是 O(n)，最壞 O(n²)。"""),
 ],
 "approaches": [
   ap("解法一", "排序陣列 + 二分", [
     ("c", S["p315_bisect"]),
   ], "O(n²)", "O(n)", "insert 的搬移在 C 層級，實務上不算太慢", ""),

   ap("解法二", "座標壓縮 + 樹狀陣列", [
     ("c", S["p315_bit"]),
   ], "O(n log n)", "O(n)", "", "", optimal=True),

   ap("解法三", "合併排序（排索引）", [
     ("c", S["p315_merge"]),
     ("c", """【為什麼是嚴格小於 <？】
    右半中「等於」nums[idx[i]] 的元素不算比它小，
    所以用 < 讓左半的相等元素先放進去（這也保持了穩定排序）。"""),
   ], "O(n log n)", "O(n)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、排序陣列", "O(n²)", "O(n)", "最短"],
    ["二、樹狀陣列", "O(n log n)", "O(n)", "最通用 ✔"],
    ["三、合併排序", "O(n log n)", "O(n)", "逆序數經典"]]),
 "edges": [
   "<strong>重複值</strong> → 「更小」是嚴格小於，相等不算。",
   "<strong>負數</strong> → 座標壓縮解決。",
   "<strong>遞增陣列</strong> → 全部是 0。",
 ],
 "follow": [
   ("h", "逆序數家族"),
   ("c", "把 counts 全部加起來，就是陣列的逆序數。第 493 題「翻轉對」（nums[i] &gt; 2·nums[j]）、第 327 題「區間和的個數」都用同樣的兩種工具：合併排序或樹狀陣列。"),
 ],
 "related": [
   "<strong>第 307 題 區域和檢索 - 陣列可修改</strong> —— 樹狀陣列",
   "<strong>第 327 題 區間和的個數</strong>",
   "<strong>第 493 題 翻轉對</strong>",
   "<strong>第 1649 題 通過指令創建有序陣列</strong>",
 ],
 "check": [
   "為什麼要由右往左處理？",
   "樹狀陣列的索引代表什麼？為什麼需要座標壓縮？",
   "合併排序時，counts 在什麼時候增加？增加多少？",
 ],
})


# ==================== 316. Remove Duplicate Letters ====================
S["p316"] = '''class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {ch: i for i, ch in enumerate(s)}   # 每個字母最後出現的位置
        stack, in_stack = [], set()
        for i, ch in enumerate(s):
            if ch in in_stack:                     # 已經在答案裡了，跳過
                continue
            # ★ 堆疊頂端比 ch 大，而且後面還會再出現 -> 先丟掉，之後再放
            while stack and stack[-1] > ch and last[stack[-1]] > i:
                in_stack.remove(stack.pop())
            stack.append(ch)
            in_stack.add(ch)
        return "".join(stack)'''

S["p316_greedy"] = '''class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        cnt = collections.Counter(s)
        pos = 0                                    # 第一個字母要選的位置
        for i, ch in enumerate(s):
            if ch < s[pos]:
                pos = i                            # 選最小的字母
            cnt[ch] -= 1
            if cnt[ch] == 0:                       # ch 之後不會再出現 -> 不能再往後找了
                break
        c = s[pos]
        # 選定 c，把它之後的部分去掉所有 c，遞迴
        return c + self.removeDuplicateLetters(s[pos + 1:].replace(c, ""))'''

_p316 = [S.load(x) for x in ("p316", "p316_greedy")]


def _rdl_ref(s):
    need = set(s)
    best = None
    for mask in range(1 << len(s)):
        t = "".join(s[i] for i in range(len(s)) if mask >> i & 1)
        if len(t) == len(need) and set(t) == need:
            if best is None or t < best:
                best = t
    return best


for s, want in [("bcabc", "abc"), ("cbacdcbc", "acdb"), ("a", "a")]:
    for sol in _p316:
        assert sol.removeDuplicateLetters(s) == want
for _ in range(1500):
    s = "".join(random.choice("abcd") for _ in range(random.randrange(1, 12)))
    want = _rdl_ref(s)
    for sol in _p316:
        assert sol.removeDuplicateLetters(s) == want, (s, sol)
print("P316 OK")

_P316_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">s = "cbacdcbc"，單調堆疊的變化（堆疊頂端在右邊）</text>
            <g font-size="12">
              <text x="30" y="52" fill="var(--text-muted)">讀入</text><text x="90" y="52" fill="var(--text-muted)">堆疊</text><text x="220" y="52" fill="var(--text-muted)">說明</text>
              <text x="30" y="76" fill="var(--text)">c</text><text x="90" y="76" fill="var(--text)">c</text>
              <text x="30" y="98" fill="var(--text)">b</text><text x="90" y="98" fill="var(--text)">b</text><text x="220" y="98" fill="var(--accent)">c &gt; b，而且 c 後面還有 → 丟掉 c</text>
              <text x="30" y="120" fill="var(--text)">a</text><text x="90" y="120" fill="var(--text)">a</text><text x="220" y="120" fill="var(--accent)">b &gt; a，b 後面還有 → 丟掉 b</text>
              <text x="30" y="142" fill="var(--text)">c</text><text x="90" y="142" fill="var(--text)">a c</text>
              <text x="30" y="164" fill="var(--text)">d</text><text x="90" y="164" fill="var(--text)">a c d</text>
              <text x="30" y="186" fill="var(--text)">c</text><text x="90" y="186" fill="var(--text)">a c d</text><text x="220" y="186" fill="var(--text-muted)">c 已經在堆疊裡 → 跳過</text>
              <text x="30" y="208" fill="var(--text)">b</text><text x="90" y="208" fill="var(--text)">a c d b</text><text x="220" y="208" fill="#ff8a65">d &gt; b，但 d 後面沒有了 → 不能丟</text>
              <text x="30" y="230" fill="var(--text)">c</text><text x="90" y="230" fill="var(--gold)">a c d b</text><text x="220" y="230" fill="var(--text-muted)">c 已經在 → 跳過；答案 "acdb"</text>
            </g>'''

emit({
 "num": 316, "slug": "remove-duplicate-letters",
 "en": [
   "Given a string <code>s</code>, remove duplicate letters so that every letter appears once and only once. You must make sure your result is "
   "<strong>the smallest in lexicographical order</strong> among all possible results.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，刪除重複的字母，使每個字母<strong>恰好出現一次</strong>。在所有可能的結果中，回傳<strong>字典序最小</strong>的那一個。",
   "（結果必須是 <code>s</code> 的子序列——不能改變字母的相對順序。）",
 ],
 "examples": """範例 1
  輸入：s = "bcabc"
  輸出："abc"

範例 2
  輸入：s = "cbacdcbc"
  輸出："acdb\"""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁴",
   "<code>s</code> 只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【字典序最小 -> 越前面的字母越小越好】
    貪心：讓答案的前面盡量放小字母。

【單調堆疊】
    由左到右讀，維護目前的答案（堆疊）。
    讀到 ch：
        - 已經在堆疊裡 -> 跳過（每個字母只要一個）
        - 堆疊頂端 top > ch，而且 top 後面還會出現
              -> 把 top 丟掉（之後再放它，換到比較後面的位置比較好）
          重複直到不能丟為止
        - 放入 ch

【關鍵條件：後面還會出現】
    如果 top 之後不會再出現，丟掉它就再也拿不回來，
    違反「每個字母恰好一次」-> 不能丟。
    用 last[ch] 記錄每個字母最後出現的位置。

【為什麼已在堆疊裡的要跳過？】
    堆疊裡的那個 ch 位置更前面；
    它之所以沒被彈出，代表它前面的字母都比它小（或不能丟），
    用後面的 ch 替換不會讓答案更小。"""),
   ("fig", _P316_FIG, "0 0 640 244"),
 ],
 "approaches": [
   ap("解法一", "逐字母貪心 + 遞迴", [
     ("c", S["p316_greedy"]),
     ("c", """【每次決定答案的第一個字母】
    從左往右找，直到遇到某個字母「最後一次出現」為止——
    再往右的話，那個字母就沒得選了。
    這段範圍內最小的字母（最左邊那個）就是答案的第一個字母。
    然後把它之後的字串去掉這個字母，遞迴。
    最多 26 層，每層 O(n) -> O(26n)。"""),
   ], "O(26 · n)", "O(26 · n)", "", "遞迴產生的字串"),

   ap("解法二", "單調堆疊", [
     ("c", S["p316"]),
   ], "O(n)", "O(1)", "每個字母最多進出堆疊一次", "最多 26 個字母", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、逐字母貪心", "O(26n)", "O(26n)"],
    ["二、單調堆疊", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>沒有重複</strong> → 原字串。",
   "<strong>全部相同</strong> → 單一字母。",
   "<strong>大字母最後才出現</strong> → 不能丟，只能留在前面。",
 ],
 "follow": [
   ("h", "同題"),
   ("c", "第 1081 題「不同字元的最小子序列」和本題完全相同。第 402 題「移掉 K 位數字」是同一種單調堆疊，只是丟的條件換成「還有刪除額度」。"),
 ],
 "related": [
   "<strong>第 1081 題 不同字元的最小子序列</strong>",
   "<strong>第 402 題 移掉 K 位數字</strong>",
   "<strong>第 321 題 拼接最大數</strong>",
 ],
 "check": [
   "什麼情況下可以把堆疊頂端丟掉？",
   "為什麼需要「後面還會出現」這個條件？",
   "已經在堆疊裡的字母為什麼可以直接跳過？",
 ],
})


# ==================== 318. Maximum Product of Word Lengths ====================
S["p318"] = '''class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # ★ 每個單字用 26 位元的遮罩表示「有哪些字母」
        best_len = {}                               # 遮罩 -> 最長的單字長度
        for w in words:
            m = 0
            for ch in w:
                m |= 1 << (ord(ch) - 97)
            best_len[m] = max(best_len.get(m, 0), len(w))
        ans = 0
        items = list(best_len.items())
        for i in range(len(items)):
            m1, l1 = items[i]
            for j in range(i + 1, len(items)):
                m2, l2 = items[j]
                if m1 & m2 == 0:                    # 沒有共同字母
                    ans = max(ans, l1 * l2)
        return ans'''

S["p318_set"] = '''class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = [set(w) for w in words]
        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (sets[i] & sets[j]):         # 集合交集：O(26)
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans'''

_p318 = [S.load(x) for x in ("p318", "p318_set")]
for w, want in [(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"], 16), (["a", "ab", "abc", "d", "cd", "bcd", "abcd"], 4), (["a", "aa", "aaa", "aaaa"], 0)]:
    for sol in _p318:
        assert sol.maxProduct(w) == want
for _ in range(2000):
    words = ["".join(random.choice("abcdef") for _ in range(random.randrange(1, 5))) for _ in range(random.randrange(2, 9))]
    assert _p318[0].maxProduct(words) == _p318[1].maxProduct(words)
print("P318 OK")

emit({
 "num": 318, "slug": "maximum-product-of-word-lengths",
 "en": [
   "Given a string array <code>words</code>, return <em>the maximum value of</em> <code>length(word[i]) * length(word[j])</code> <em>where the two words do not share common letters</em>. If no such two words exist, return <code>0</code>.",
 ],
 "zh": [
   "給你一個字串陣列 <code>words</code>，找出兩個<strong>沒有任何共同字母</strong>的單字，回傳它們長度乘積的最大值。如果不存在這樣的兩個單字，回傳 <code>0</code>。",
 ],
 "examples": """範例 1
  輸入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
  輸出：16
  說明："abcw" 和 "xtfn"，4 × 4 = 16

範例 2
  輸入：words = ["a","ab","abc","d","cd","bcd","abcd"]
  輸出：4
  說明："ab" 和 "cd"

範例 3
  輸入：words = ["a","aa","aaa","aaaa"]
  輸出：0""",
 "constraints": [
   "2 ≤ <code>words.length</code> ≤ 1000",
   "1 ≤ <code>words[i].length</code> ≤ 1000",
   "<code>words[i]</code> 只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【兩兩比較是免不了的：O(n²) 對】
    重點是「判斷兩個單字有沒有共同字母」要多快。

【位元遮罩】
    只有 26 個小寫字母 -> 一個 int 的 26 個位元剛好。
        "abc" -> ...000111
        "bd"  -> ...001010
    有共同字母 <=> 遮罩 AND 不為 0。
    判斷變成 O(1) 的一次位元運算。

【進一步優化】
    字母組成相同的單字（遮罩相同），只需要保留最長的那個。
    "aab"、"ab"、"ba" 遮罩都一樣 -> 只留長度 3。
    遮罩最多 2²⁶ 種，但實際上通常比 n 少很多。"""),
 ],
 "approaches": [
   ap("解法一", "集合交集", [
     ("c", S["p318_set"]),
   ], "O(n² · 26)", "O(n · 26)", "", ""),

   ap("解法二", "位元遮罩", [
     ("c", S["p318"]),
   ], "O(L + n²)", "O(n)", "L = 所有單字的總長", "", optimal=True),
 ],
 "compare": (["解法", "判斷一對", "總時間"],
   [["一、集合", "O(26)", "O(n²·26)"],
    ["二、位元遮罩", "O(1)", "O(L + n²) ✔"]]),
 "edges": [
   "<strong>全部都有共同字母</strong> → 0。",
   "<strong>重複字母</strong>（\"aaaa\"）→ 遮罩只有一個位元。",
   "<strong>相同遮罩</strong> → 只需保留最長的。",
 ],
 "follow": [
   ("h", "位元遮罩表示集合"),
   ("c", "小集合（≤ 64 個元素）用整數表示，交集是 &amp;、聯集是 |、差集是 &amp; ~。第 1178 題「猜字謎」、第 1255 題、第 2002 題都用同樣的技巧。"),
 ],
 "related": [
   "<strong>第 1178 題 猜字謎</strong>",
   "<strong>第 1239 題 串聯字串的最大長度</strong>",
 ],
 "check": [
   "怎麼用一個整數表示一個單字包含哪些字母？",
   "怎麼 O(1) 判斷兩個單字沒有共同字母？",
   "遮罩相同的單字為什麼只保留最長的？",
 ],
})
