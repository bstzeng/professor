# -*- coding: utf-8 -*-
"""第 513、514、515、516、517、518、519、520 題。"""
import random
from collections import Counter, deque
from functools import lru_cache
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, nodes

S = Src()
random.seed(513)


# ==================== 513. Find Bottom Left Tree Value ====================
S["p513"] = '''class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            nd = q.popleft()
            # ★ 先右後左：最後一個被取出的節點，就是最底層最左邊的
            if nd.right:
                q.append(nd.right)
            if nd.left:
                q.append(nd.left)
        return nd.val'''

_p513 = S.load("p513", extra={"deque": deque})
assert _p513.findBottomLeftValue(lv([2, 1, 3])) == 1
assert _p513.findBottomLeftValue(lv([1, 2, 3, 4, None, 5, 6, None, None, 7])) == 7
for _ in range(1500):
    t = rand_tree(random.randint(1, 12))
    lvl = [t]
    while True:
        nxt = [c for nd in lvl for c in (nd.left, nd.right) if c]
        if not nxt:
            break
        lvl = nxt
    assert _p513.findBottomLeftValue(t) == lvl[0].val
print("P513 OK")

em({
 "num": 513, "title": "找樹左下角的值",
 "desc": "層序走訪時改成「先右後左」，最後一個出佇列的節點就是最底層最左邊的。",
 "zh": ["給你二元樹的根節點，回傳<strong>最底層</strong>中<strong>最左邊</strong>節點的值。樹至少有一個節點。"],
 "idea": [
   ("c", """【一般想法】
    層序走訪，記錄每一層的第一個節點，最後一層的第一個就是答案。

【更簡潔的技巧：先右後左】
    BFS 時每個節點先放右孩子、再放左孩子。
    這樣同一層裡是「由右到左」出佇列，
    整個走訪的最後一個節點 = 最底層的最左邊。
    不用另外記錄層數。

【DFS 也行】
    前序走訪（先左後右），第一次到達新的深度時記下值；
    最深那一層第一個被記下的就是最左邊。"""),
 ],
 "approaches": [
   ap("解法", "BFS 先右後左", [("c", S["p513"])], "O(n)", "O(w)", "", "w 為最寬一層的節點數", optimal=True),
 ],
 "edges": ["<strong>只有根節點</strong> → 根的值。", "<strong>最底層只有右孩子</strong> → 「最左邊」是那一層最左的節點，不一定是左孩子。"],
 "follow": [("h", "層序走訪的變形"), ("c", "第 199 題（右視圖）取每層最後一個；第 515 題取每層最大值；第 637 題取每層平均。都是同一個 BFS 骨架。")],
 "related": ["<strong>第 199 題 二元樹的右視圖</strong>", "<strong>第 102 題 二元樹的層序走訪</strong>", "<strong>第 515 題 在每個樹行中找最大值</strong>"],
 "check": ["為什麼「先右後左」的最後一個節點就是答案？", "答案一定是某個左孩子嗎？"],
})


# ==================== 514. Freedom Trail ====================
S["p514"] = '''class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        pos = defaultdict(list)                 # 每個字母在 ring 上出現的位置
        for i, c in enumerate(ring):
            pos[c].append(i)

        # dp：目前對準位置 -> 到這裡為止的最少旋轉步數
        dp = {0: 0}
        for c in key:
            nxt = {}
            for j in pos[c]:                    # 下一個字元可以用 ring 上任何一個 c
                best = float("inf")
                for i, cost in dp.items():
                    d = abs(i - j)
                    best = min(best, cost + min(d, n - d))   # ★ 順時針或逆時針，取近的
                nxt[j] = best
            dp = nxt
        return min(dp.values()) + len(key)      # 每個字元還要按一次按鈕'''

_p514 = S.load("p514", extra={"defaultdict": __import__("collections").defaultdict})
assert _p514.findRotateSteps("godding", "gd") == 4
assert _p514.findRotateSteps("godding", "godding") == 13
def _bf514(ring, key):
    n = len(ring)
    @lru_cache(None)
    def go(i, k):
        if k == len(key):
            return 0
        return min(min(abs(i - j), n - abs(i - j)) + 1 + go(j, k + 1) for j in range(n) if ring[j] == key[k])
    return go(0, 0)
for _ in range(800):
    ring = "".join(random.choice("abc") for _ in range(random.randint(1, 7)))
    key = "".join(random.choice(ring) for _ in range(random.randint(1, 5)))
    assert _p514.findRotateSteps(ring, key) == _bf514(ring, key)
print("P514 OK")

em({
 "num": 514, "title": "自由之路",
 "desc": "狀態是「目前對準 ring 的哪個位置」：每打一個字元，就在所有候選位置之間轉移，取環上的最短距離。",
 "zh": [
   "電玩《異塵餘生 4》的任務「自由之路」：有一個刻著字元的圓環 <code>ring</code>，一開始第 0 個字元對準 12 點方向。你要依序拼出字串 <code>key</code>。",
   "每一步可以把圓環順時針或逆時針轉一格（算 1 步）；當 <code>key[i]</code> 對準 12 點時，按一下中央按鈕（也算 1 步）拼出這個字元。",
   "回傳拼出整個 <code>key</code> 的<strong>最少步數</strong>。題目保證 <code>key</code> 一定拼得出來。",
 ],
 "idea": [
   ("c", """【為什麼不能貪心（每次轉到最近的那個字元）？】
    ring 上同一個字元可能出現多次。
    現在轉到近的那一個，可能讓下一個字元變很遠。

【DP 狀態】
    拼完 key 的前 k 個字元後，ring 一定停在某個「key[k-1] 所在的位置」。
    dp[j] = 拼完前 k 個字元、且停在位置 j 的最少旋轉步數。

【轉移】
    拼 key[k]：對每個 c = key[k] 的位置 j，
        dp'[j] = min over i ( dp[i] + 環上距離(i, j) )
    環上距離 = min(|i - j|, n - |i - j|)。

【按鈕】
    每個字元固定按一次，最後加上 len(key) 即可。"""),
 ],
 "approaches": [
   ap("解法", "位置 DP", [
     ("c", S["p514"]),
     "驗證方式：和記憶化窮舉比對 800 組隨機資料。",
   ], "O(m · n²)", "O(n)", "m = len(key)；實際上只在同字母的位置間轉移，通常遠小於 n²", "", optimal=True),
 ],
 "edges": ["<strong>key 中連續相同字元</strong> → 不用轉，只按按鈕。", "<strong>環上距離</strong> → 別忘了反方向可能比較近。", "<strong>按鈕步數</strong> → 每個字元都要加 1。"],
 "follow": [("h", "為什麼狀態只需要「位置」？"), ("c", "拼完前 k 個字元後，未來的花費只取決於現在對準哪裡——這就是 DP 的「無後效性」。之前怎麼轉過來的都不重要。")],
 "related": ["<strong>第 1320 題 二指輸入的最小距離</strong>", "<strong>第 72 題 編輯距離</strong>"],
 "check": ["為什麼貪心不對？舉一個反例的想法。", "dp 的狀態代表什麼？", "環上兩點的距離怎麼算？"],
})


# ==================== 515. Find Largest Value in Each Tree Row ====================
S["p515"] = '''class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        level = [root] if root else []
        while level:
            res.append(max(nd.val for nd in level))       # 這一層的最大值
            level = [c for nd in level for c in (nd.left, nd.right) if c]   # 下一層
        return res'''

_p515 = S.load("p515")
assert _p515.largestValues(lv([1, 3, 2, 5, 3, None, 9])) == [1, 3, 9]
assert _p515.largestValues(None) == []
print("P515 OK")

em({
 "num": 515, "title": "在每個樹行中找最大值",
 "desc": "逐層走訪，每一層取最大值。",
 "zh": ["給你二元樹的根節點，回傳每一層（由上到下）的<strong>最大值</strong>所組成的陣列。"],
 "idea": [
   ("c", """【層序走訪】
    用一個 list 存目前這一層的所有節點：
        取這一層的最大值；
        下一層 = 所有節點的孩子。
    直到某一層是空的。

    這種「整層換整層」的寫法比 deque + 計數更直觀。"""),
 ],
 "approaches": [
   ap("解法", "逐層 BFS", [("c", S["p515"])], "O(n)", "O(w)", optimal=True),
 ],
 "edges": ["<strong>空樹</strong> → []。", "<strong>負數節點</strong> → 不能用 0 當最大值初始值。"],
 "follow": [("h", "DFS 版本"), ("c", "前序走訪帶著深度 d：若 d == len(res) 就 append，否則 res[d] = max(res[d], val)。")],
 "related": ["<strong>第 102 題 二元樹的層序走訪</strong>", "<strong>第 513 題 找樹左下角的值</strong>", "<strong>第 637 題 二元樹的層平均值</strong>"],
 "check": ["為什麼不能用 0 當作每層最大值的初始值？"],
})


# ==================== 516. Longest Palindromic Subsequence ====================
S["p516a"] = '''class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]       # dp[i][j]：s[i..j] 的最長迴文子序列長度
        for i in range(n - 1, -1, -1):         # i 由大到小，才能用到 dp[i+1][...]
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2          # ★ 兩端相同：一起收進來
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])  # 丟掉其中一端
        return dp[0][n - 1]'''

S["p516b"] = '''class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 等價於 s 與 reverse(s) 的最長共同子序列（LCS）
        t = s[::-1]
        n = len(s)
        prev = [0] * (n + 1)
        for i in range(1, n + 1):
            cur = [0] * (n + 1)
            for j in range(1, n + 1):
                cur[j] = prev[j - 1] + 1 if s[i - 1] == t[j - 1] else max(prev[j], cur[j - 1])
            prev = cur
        return prev[n]'''

def _bf516(s):
    from itertools import combinations
    for L in range(len(s), 0, -1):
        for idx in combinations(range(len(s)), L):
            t = "".join(s[i] for i in idx)
            if t == t[::-1]:
                return L
for key in ("p516a", "p516b"):
    sol = S.load(key)
    assert sol.longestPalindromeSubseq("bbbab") == 4 and sol.longestPalindromeSubseq("cbbd") == 2
    for _ in range(400):
        s = "".join(random.choice("abc") for _ in range(random.randint(1, 9)))
        assert sol.longestPalindromeSubseq(s) == _bf516(s)
print("P516 OK")

em({
 "num": 516, "title": "最長迴文子序列",
 "desc": "區間 DP：兩端相同就一起收進來，否則丟掉一端；也等價於 s 和反轉後的 LCS。",
 "zh": [
   "給你字串 <code>s</code>，回傳它的<strong>最長迴文子序列</strong>長度。",
   "子序列是刪除某些（或不刪）字元、但不改變其餘字元順序後得到的序列（不需要連續）。",
 ],
 "idea": [
   ("c", """【區間 DP】
    dp[i][j] = s[i..j] 中最長迴文子序列的長度。

    s[i] == s[j]：
        這兩個字元可以當迴文的頭尾 -> dp[i+1][j-1] + 2
    s[i] != s[j]：
        它們不可能同時當頭尾，至少丟掉一個 ->
        max(dp[i+1][j], dp[i][j-1])

【計算順序】
    dp[i][j] 依賴 i+1 的列 -> i 由大到小；j 由小到大。

【另一個角度】
    迴文正著讀、反著讀一樣，
    所以「最長迴文子序列」= LCS(s, reverse(s))（第 1143 題）。"""),
 ],
 "approaches": [
   ap("解法一", "區間 DP", [("c", S["p516a"])], "O(n²)", "O(n²)", "", "可以壓成一維 O(n)", optimal=True),
   ap("解法二", "轉成 LCS", [("c", S["p516b"])], "O(n²)", "O(n)"),
 ],
 "edges": ["<strong>單一字元</strong> → 1。", "<strong>全部相同</strong> → n。", "<strong>子序列 vs 子字串</strong> → 本題不需要連續（對照第 5 題）。"],
 "follow": [("h", "子字串版"), ("c", "第 5 題（最長迴文子字串）要求連續，用中心擴展；第 647 題數迴文子字串的個數。本題是子序列，必須 DP。")],
 "related": ["<strong>第 5 題 最長迴文子字串</strong>", "<strong>第 1143 題 最長共同子序列</strong>", "<strong>第 1312 題 讓字串成為迴文串的最少插入次數</strong>"],
 "check": ["s[i] == s[j] 時為什麼一定可以兩端都取？", "為什麼 i 要由大到小計算？", "為什麼本題等價於 s 與反轉字串的 LCS？"],
})


# ==================== 517. Super Washing Machines ====================
S["p517"] = '''class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n, total = len(machines), sum(machines)
        if total % n:
            return -1                          # 無法平分
        avg = total // n
        res = flow = 0
        for x in machines:
            d = x - avg                        # 這台多（正）或少（負）幾件
            flow += d                          # ★ 必須從左邊流到右邊的衣服總量（可正可負）
            res = max(res, abs(flow), d)       # 兩種瓶頸：跨過某條邊界的流量、單台要送出的量
        return res'''

_p517 = S.load("p517")
assert _p517.findMinMoves([1, 0, 5]) == 3 and _p517.findMinMoves([0, 3, 0]) == 2 and _p517.findMinMoves([0, 2, 0]) == -1
def _bf517(m):
    n = len(m)
    if sum(m) % n:
        return -1
    avg = sum(m) // n
    start = tuple(m); goal = tuple([avg] * n)
    seen = {start}; q = deque([(start, 0)])
    while q:
        st, d = q.popleft()
        if st == goal:
            return d
        # 每一步：選一部分機器各送一件給左或右鄰居
        from itertools import product
        for ch in product((0, -1, 1), repeat=n):
            if all(c == 0 for c in ch):
                continue
            a = list(st); ok = True
            for i, c in enumerate(ch):
                if c == 0:
                    continue
                j = i + c
                if j < 0 or j >= n or st[i] == 0:
                    ok = False; break
                a[i] -= 1; a[j] += 1
            if ok:
                t = tuple(a)
                if t not in seen:
                    seen.add(t); q.append((t, d + 1))
for _ in range(150):
    n = random.randint(1, 4)
    m = [random.randint(0, 3) for _ in range(n)]
    assert _p517.findMinMoves(m) == _bf517(m), m
print("P517 OK")

em({
 "num": 517, "title": "超級洗衣機",
 "desc": "答案是兩種瓶頸的最大值：跨過某條邊界必須流動的衣服量，以及單台機器必須送出的量。",
 "zh": [
   "有 <code>n</code> 台排成一列的洗衣機，<code>machines[i]</code> 是第 i 台裡的衣服件數。",
   "每一步，你可以選<strong>任意多台</strong>機器，每台各把<strong>一件</strong>衣服同時送給它的左邊或右邊鄰居。",
   "回傳讓所有機器衣服數相同的<strong>最少步數</strong>；做不到則回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【先判斷能不能平分】
    總數不能被 n 整除 -> -1。目標是每台 avg 件。

【瓶頸一：跨過邊界的流量】
    看第 i 台和第 i+1 台之間的邊界。
    左邊 i+1 台一共多出 flow = Σ(x - avg) 件，這些必須越過這條邊界。
    每一步最多只有一件衣服能越過同一條邊界 -> 至少 |flow| 步。

【瓶頸二：單台必須送出的量】
    第 i 台多出 d 件（d > 0），每一步它最多送出一件 -> 至少 d 步。
    （注意：少的機器可以同時從左右兩邊收，所以「缺」的量不構成瓶頸，
      只看「多」的。）

【答案 = 所有這些下界的最大值】
    可以證明這個下界總是能達到。"""),
 ],
 "approaches": [
   ap("解法", "前綴流量 + 單台送出量", [
     ("c", S["p517"]),
     "驗證方式：在小規模資料上和 BFS 窮舉每一步所有可能的送法比對。",
   ], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>無法平分</strong> → −1。", "<strong>一台多很多、其他都 0</strong> → 例如 [0,3,0]：中間那台要送出 2 件，每步每台只能送出一件 → 2。", "<strong>缺的機器</strong> → 可以同時從兩邊收，所以不取 −d。"],
 "follow": [("h", "為什麼只取 d 而不取 |d|？"), ("c", "多出 d 件的機器每步只能送出 1 件；但缺 d 件的機器可以同時從左右鄰居各收 1 件，所以它不是瓶頸。對照第 979 題（在二元樹中分配硬幣），那題是邊上的流量總和。")],
 "related": ["<strong>第 979 題 在二元樹中分配硬幣</strong>", "<strong>第 462 題 最少移動次數使陣列元素相等 II</strong>"],
 "check": ["跨過一條邊界的流量為什麼是答案的下界？", "為什麼多出的機器是瓶頸、缺的不是？"],
})


# ==================== 518. Coin Change II ====================
S["p518"] = '''class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)        # dp[x]：湊出 x 的組合數
        dp[0] = 1                      # 什麼都不選，湊出 0
        for c in coins:                # ★ 外層是硬幣：每種組合只會以固定的硬幣順序被數一次
            for x in range(c, amount + 1):
                dp[x] += dp[x - c]     # 由小到大 -> 同一種硬幣可以重複用
        return dp[amount]'''

_p518 = S.load("p518")
assert _p518.change(5, [1, 2, 5]) == 4 and _p518.change(3, [2]) == 0 and _p518.change(10, [10]) == 1
def _bf518(a, cs):
    @lru_cache(None)
    def go(i, a):
        if a == 0: return 1
        if i == len(cs) or a < 0: return 0
        return go(i, a - cs[i]) + go(i + 1, a)
    return go(0, a)
for _ in range(1000):
    cs = random.sample(range(1, 9), random.randint(1, 4)); a = random.randint(0, 25)
    assert _p518.change(a, cs) == _bf518(a, tuple(cs))
print("P518 OK")

em({
 "num": 518, "title": "零錢兌換 II",
 "desc": "完全背包的「組合數」：硬幣放外層迴圈，每種組合只被數一次；和第 377 題的排列數對照。",
 "zh": [
   "給你不同面額的硬幣 <code>coins</code> 和總金額 <code>amount</code>，每種硬幣數量無限。回傳湊出 <code>amount</code> 的<strong>組合數</strong>；湊不出來則回傳 <code>0</code>。",
   "（1, 2 和 2, 1 算同一種組合。）答案保證在 32 位元有號整數範圍內。",
 ],
 "idea": [
   ("c", """【完全背包】
    dp[x] = 湊出金額 x 的組合數，dp[0] = 1。
    用硬幣 c 更新：dp[x] += dp[x - c]。
    x 由小到大 -> dp[x - c] 可能已經用過 c -> 允許重複使用。

【迴圈順序決定是「組合」還是「排列」】
    外層硬幣、內層金額：
        先處理完所有 1，再處理 2……
        每種組合只會以「1 都在 2 前面」的順序出現一次 -> 組合數（本題）。
    外層金額、內層硬幣：
        每個金額都嘗試「最後一枚是哪個硬幣」
        1+2 和 2+1 會被分別數到 -> 排列數（第 377 題）。"""),
 ],
 "approaches": [
   ap("解法", "完全背包（組合數）", [
     ("c", S["p518"]),
     "驗證方式：和記憶化遞迴（「用第 i 種硬幣」或「跳到下一種」）比對 1000 組。",
   ], "O(amount · len(coins))", "O(amount)", optimal=True),
 ],
 "edges": ["<strong>amount = 0</strong> → 1（空組合）。", "<strong>湊不出來</strong> → 0。", "<strong>迴圈順序寫反</strong> → 會變成排列數。"],
 "follow": [("h", "三個硬幣題"), ("c", "第 322 題：最少硬幣數（min）；本題：組合數（外層硬幣）；第 377 題：排列數（外層金額）。同一個背包骨架，換掉運算與迴圈順序。")],
 "related": ["<strong>第 322 題 零錢兌換</strong>", "<strong>第 377 題 組合總和 IV</strong>", "<strong>第 279 題 完全平方數</strong>"],
 "check": ["為什麼外層是硬幣時算的是組合數？", "內層 x 為什麼要由小到大？", "dp[0] 為什麼是 1？"],
})


# ==================== 519. Random Flip Matrix ====================
S["p519"] = '''class Solution:
    def __init__(self, m: int, n: int):
        self.m, self.n = m, n
        self.total = m * n
        self.swap = {}                  # 虛擬陣列中「被換過」的位置：索引 -> 實際值

    def flip(self) -> List[int]:
        k = random.randrange(self.total)          # 在還沒翻的 total 個裡均勻選一個
        self.total -= 1
        idx = self.swap.get(k, k)                 # 虛擬陣列第 k 格的真正值
        # ★ 把最後一格的值搬到第 k 格（Fisher–Yates 的一步），最後一格就被「刪掉」了
        self.swap[k] = self.swap.get(self.total, self.total)
        return [idx // self.n, idx % self.n]

    def reset(self) -> None:
        self.total = self.m * self.n
        self.swap.clear()'''

_cls519 = S.loadns("p519")["Solution"]
for _ in range(200):
    m, n = random.randint(1, 4), random.randint(1, 4)
    o = _cls519(m, n)
    for _r in range(2):
        got = {tuple(o.flip()) for _ in range(m * n)}
        assert got == {(i, j) for i in range(m) for j in range(n)}
        o.reset()
o = _cls519(2, 3); cnt = Counter()
for _ in range(30000):
    cnt[tuple(o.flip())] += 1; o.reset()
assert all(abs(c - 5000) < 600 for c in cnt.values())
print("P519 OK")

em({
 "num": 519, "title": "隨機翻轉矩陣",
 "desc": "把二維格子攤平成一維，用雜湊表模擬「只記錄被換過的位置」的 Fisher–Yates 洗牌。",
 "zh": [
   "有一個 <code>m x n</code> 的二元矩陣，一開始全是 0。設計一個演算法：",
   ("ul", ["<code>flip()</code>：在所有值為 0 的格子中<strong>均勻隨機</strong>選一個，把它設成 1，並回傳它的座標 <code>[i, j]</code>。",
           "<code>reset()</code>：把矩陣恢復成全 0。"]),
   "盡量減少呼叫內建亂數函式的次數，並最佳化時間與空間。",
 ],
 "idea": [
   ("c", """【攤平成一維】
    格子 (i, j) <-> 編號 i·n + j，總共 m·n 個。

【不能真的建陣列】
    m, n 最多 10⁴，m·n 可達 10⁸，建陣列太大。
    但 flip 最多呼叫 1000 次。

【Fisher–Yates + 雜湊表】
    想像一個虛擬陣列 a = [0, 1, ..., total-1]（還沒翻的編號）。
    flip：
        隨機選 k ∈ [0, total)，答案是 a[k]；
        把 a[total-1] 搬到 a[k]，total 減 1 -> a[k] 就被「刪除」了。
    虛擬陣列大部分格子 a[i] = i，只有被搬過的才不一樣 ->
    用雜湊表只記錄那些格子。

    每次 flip 只呼叫一次亂數，O(1)。"""),
 ],
 "approaches": [
   ap("解法", "虛擬陣列的 Fisher–Yates", [
     ("c", S["p519"]),
     "驗證方式：每次翻完 m·n 次正好得到所有格子各一次；三萬次抽樣檢查分布均勻。",
   ], "flip / reset：O(1) 均攤", "O(呼叫次數)", "", "reset 清空雜湊表的成本由之前的 flip 均攤", optimal=True),
 ],
 "edges": ["<strong>翻到最後一格</strong> → k == total，雜湊表記錄自己，不影響正確性。", "<strong>reset 後</strong> → total 恢復、雜湊表清空。"],
 "follow": [("h", "拒絕抽樣的版本"), ("c", "也可以用集合記錄已翻過的格子，隨機到翻過的就重抽。翻得越多重抽越多次，最壞情況很慢——本題要求減少亂數呼叫，所以 Fisher–Yates 更好。")],
 "related": ["<strong>第 384 題 打亂陣列</strong>", "<strong>第 710 題 黑名單中的隨機數</strong>", "<strong>第 380 題 O(1) 時間插入、刪除和取得隨機元素</strong>"],
 "check": ["為什麼不能真的建一個 m·n 的陣列？", "雜湊表裡存的是什麼？", "每次 flip 為什麼只需要一次亂數？"],
})


# ==================== 520. Detect Capital ====================
S["p520"] = '''class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 三種合法情況：全大寫、全小寫、只有第一個字母大寫
        return word.isupper() or word.islower() or (word[0].isupper() and word[1:].islower())'''

_p520 = S.load("p520")
for _ in range(3000):
    w = "".join(random.choice("aAbB") for _ in range(random.randint(1, 5)))
    ups = [c.isupper() for c in w]
    want = all(ups) or not any(ups) or (ups[0] and not any(ups[1:]))
    assert _p520.detectCapitalUse(w) == want, w
print("P520 OK")

em({
 "num": 520, "title": "檢測大寫字母",
 "desc": "三種合法情況：全大寫、全小寫、首字母大寫其餘小寫；也可以用大寫字母數量判斷。",
 "zh": [
   "以下三種情況，我們說一個單字的大寫用法是正確的：",
   ("ol", ["全部字母都大寫，例如 <code>\"USA\"</code>。", "全部字母都小寫，例如 <code>\"leetcode\"</code>。", "只有第一個字母大寫，例如 <code>\"Google\"</code>。"]),
   "給你字串 <code>word</code>，判斷它的大寫用法是否正確。",
 ],
 "idea": [
   ("c", """【直接檢查三種情況】
    word.isupper() 或 word.islower() 或 (首字大寫且其餘小寫)。

【計數的寫法】
    數大寫字母個數 cap：
        cap == 0                -> 全小寫
        cap == len(word)        -> 全大寫
        cap == 1 且首字是大寫    -> 首字母大寫

【小陷阱】
    "g".isupper() 是 False，但 word[1:] 是空字串時，
    "".islower() 也是 False —— 單一字母的情況要靠前兩個條件涵蓋。"""),
 ],
 "approaches": [
   ap("解法", "三種情況判斷", [("c", S["p520"])], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>單一字母</strong> → 一定合法（被 isupper 或 islower 涵蓋）。", "<strong>\"FlaG\"</strong> → 不合法。"],
 "follow": [("h", "Python 字串方法的細節"), ("c", "isupper()/islower() 要求「至少有一個有大小寫之分的字元」，空字串回傳 False。這在組合條件時要特別注意。")],
 "related": ["<strong>第 709 題 轉換成小寫字母</strong>", "<strong>第 2129 題 將標題首字母大寫</strong>"],
 "check": ["單一字母的單字由哪個條件涵蓋？", "用大寫字母數量判斷要怎麼寫？"],
})
