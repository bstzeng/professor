# -*- coding: utf-8 -*-
"""第 622、623、624、628、629、630、632、633 題。"""
import random, heapq, math
from collections import deque
from functools import lru_cache
from itertools import permutations, combinations
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, ser

S = Src()
random.seed(622)


# ==================== 622. Design Circular Queue ====================
S["p622"] = '''class MyCircularQueue:
    def __init__(self, k: int):
        self.buf = [0] * k
        self.head = 0                   # 隊首的索引
        self.size = 0                   # ★ 另外記元素個數，就不必為了區分「空」和「滿」浪費一格

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buf[(self.head + self.size) % len(self.buf)] = value   # 隊尾 = head + size（取模繞回）
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % len(self.buf)
        self.size -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.buf[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.buf[(self.head + self.size - 1) % len(self.buf)]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.buf)'''

_Q = S.loadns("p622")["MyCircularQueue"]
for _ in range(500):
    k = random.randint(1, 5); q = _Q(k); ref = deque()
    for _ in range(40):
        op = random.choice(["en", "de", "f", "r", "e", "full"])
        if op == "en":
            v = random.randint(0, 9); ok = len(ref) < k
            if ok: ref.append(v)
            assert q.enQueue(v) == ok
        elif op == "de":
            ok = bool(ref)
            if ok: ref.popleft()
            assert q.deQueue() == ok
        elif op == "f": assert q.Front() == (ref[0] if ref else -1)
        elif op == "r": assert q.Rear() == (ref[-1] if ref else -1)
        elif op == "e": assert q.isEmpty() == (not ref)
        else: assert q.isFull() == (len(ref) == k)
print("P622 OK")

em({
 "num": 622, "title": "設計循環佇列",
 "desc": "固定大小的陣列加上「隊首索引 + 元素個數」，隊尾位置取模繞回；記個數可避開空與滿難以區分的問題。",
 "zh": [
   "設計一個<strong>循環佇列</strong>（環形緩衝區）：容量固定為 <code>k</code>，最後一個位置之後接回第一個位置，出隊後騰出的空間可以重複使用。",
   "實作 <code>enQueue</code>、<code>deQueue</code>（成功回傳 True）、<code>Front</code>、<code>Rear</code>（空時回傳 −1）、<code>isEmpty</code>、<code>isFull</code>。不可使用內建的佇列。",
 ],
 "idea": [
   ("c", """【陣列 + 取模】
    buf 長度 k。
    head：隊首索引
    size：目前元素個數
    隊尾的下一個空位 = (head + size) % k
    最後一個元素   = (head + size - 1) % k

【為什麼要記 size？】
    只用 head、tail 兩個指標時，
    「空」和「滿」都是 head == tail，無法區分。
    傳統解法是浪費一格（容量 k+1），
    或像這裡另外記元素個數。"""),
 ],
 "approaches": [
   ap("解法", "陣列 + 隊首索引 + 個數", [("c", S["p622"]), "驗證方式：和 deque 對照，隨機執行 500 組操作序列。"], "每個操作 O(1)", "O(k)", optimal=True),
 ],
 "edges": ["<strong>滿了還 enQueue</strong> → False。", "<strong>空的時候 Front / Rear</strong> → −1。", "<strong>k = 1</strong> → 隊首就是隊尾。"],
 "follow": [("h", "環形緩衝區的應用"), ("c", "音訊串流、網路封包緩衝、日誌只保留最近 N 筆——作業系統與嵌入式系統中到處都是。第 641 題是雙端版本。")],
 "related": ["<strong>第 641 題 設計循環雙端佇列</strong>", "<strong>第 232 題 用堆疊實作佇列</strong>", "<strong>第 346 題 資料流中的移動平均值</strong>（付費）"],
 "check": ["只用兩個指標時，空和滿為什麼難以區分？", "隊尾元素的索引怎麼算？"],
})


# ==================== 623. Add One Row to Tree ====================
S["p623"] = '''class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)          # 新的根，原樹變成它的左子樹
        level = [root]
        for _ in range(depth - 2):              # 走到第 depth-1 層
            level = [c for nd in level for c in (nd.left, nd.right) if c]
        for nd in level:
            # ★ 原本的左子樹接到新節點的左邊，右子樹接到新節點的右邊
            nd.left = TreeNode(val, nd.left, None)
            nd.right = TreeNode(val, None, nd.right)
        return root'''

from runner import TreeNode
_p623 = S.load("p623")
assert ser(_p623.addOneRow(lv([4, 2, 6, 3, 1, 5]), 1, 2)) == [4, 1, 1, 2, None, None, 6, 3, 1, 5]
assert ser(_p623.addOneRow(lv([4, 2, None, 3, 1]), 1, 3)) == [4, 2, None, 1, 1, 3, None, None, 1]
def _sig(t): return None if t is None else (t.val, _sig(t.left), _sig(t.right))
def _ref(s, v, d, cur=1):
    if s is None: return None
    if cur == d - 1:
        return (s[0], (v, s[1], None), (v, None, s[2]))
    return (s[0], _ref(s[1], v, d, cur + 1), _ref(s[2], v, d, cur + 1))
def _height(t): return 0 if t is None else 1 + max(_height(t.left), _height(t.right))
for _ in range(1000):
    t = rand_tree(random.randint(1, 10)); d = random.randint(1, _height(t) + 1)
    s = _sig(t)
    want = (9, s, None) if d == 1 else _ref(s, 9, d)
    assert _sig(_p623.addOneRow(t, 9, d)) == want
print("P623 OK")

em({
 "num": 623, "title": "在二元樹中增加一行",
 "desc": "走到第 depth−1 層，在每個節點下面插入兩個新節點，原本的左右子樹分別接到新節點的同側。",
 "zh": [
   "給你二元樹的根節點和整數 <code>val</code>、<code>depth</code>，在第 <code>depth</code> 層插入一整列值為 <code>val</code> 的節點（根是第 1 層）。",
   "規則：對第 <code>depth − 1</code> 層的每個非空節點，建立兩個新節點作為它新的左、右孩子；原本的左子樹接到新左孩子的<strong>左邊</strong>，原本的右子樹接到新右孩子的<strong>右邊</strong>。",
   "若 <code>depth == 1</code>，建立一個新根，原樹成為它的左子樹。",
 ],
 "idea": [
   ("c", """【找到第 depth-1 層】
    逐層 BFS，走 depth-2 次就到了。

【插入】
    對每個節點 nd：
        nd.left  = 新節點(val, 左 = 原 nd.left)
        nd.right = 新節點(val, 右 = 原 nd.right)
    注意方向：原左子樹接在新節點的「左」，原右子樹接在新節點的「右」。

【depth = 1 特判】
    新根的左孩子是原樹。"""),
 ],
 "approaches": [
   ap("解法", "逐層走到第 depth−1 層", [("c", S["p623"])], "O(n)", "O(w)", optimal=True),
 ],
 "edges": ["<strong>depth = 1</strong> → 新根。", "<strong>depth = 樹高 + 1</strong> → 在所有最底層節點下面加葉子。"],
 "follow": [("h", "DFS 寫法"), ("c", "遞迴帶著目前深度，深度為 depth−1 時插入；其他時候往下遞迴。")],
 "related": ["<strong>第 102 題 二元樹的層序走訪</strong>"],
 "check": ["原本的右子樹要接到新節點的哪一邊？", "depth = 1 怎麼處理？"],
})


# ==================== 624. Maximum Distance in Arrays ====================
S["p624"] = '''class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lo, hi = arrays[0][0], arrays[0][-1]        # 「之前的陣列」中的最小值與最大值
        res = 0
        for a in arrays[1:]:
            # ★ 先和「之前的陣列」比較，保證兩個數來自不同陣列
            res = max(res, a[-1] - lo, hi - a[0])
            lo, hi = min(lo, a[0]), max(hi, a[-1])
        return res'''

_p624 = S.load("p624")
for _ in range(2000):
    arrs = [sorted(random.randint(-9, 9) for _ in range(random.randint(1, 4))) for _ in range(random.randint(2, 5))]
    want = max(abs(x - y) for i, a in enumerate(arrs) for j, b in enumerate(arrs) if i != j for x in a for y in b)
    assert _p624.maxDistance(arrs) == want
print("P624 OK")

em({
 "num": 624, "title": "陣列列表中的最大距離",
 "desc": "每個陣列只有頭尾有用；逐一處理時只和「之前的陣列」的最小最大值比較，自動保證來自不同陣列。",
 "zh": ["給你 <code>m</code> 個各自<strong>遞增排序</strong>的陣列。從兩個<strong>不同</strong>的陣列各挑一個整數，回傳兩數差的絕對值的最大值。"],
 "idea": [
   ("c", """【每個陣列只看頭尾】
    排序過 -> a[0] 最小、a[-1] 最大。

【不能直接取全域最大 - 全域最小】
    它們可能來自同一個陣列。

【一趟掃描】
    維護「前面所有陣列」的最小值 lo 與最大值 hi。
    處理陣列 a 時：
        a[-1] - lo（a 的最大 - 前面的最小）
        hi - a[0]（前面的最大 - a 的最小）
    先更新答案、再把 a 併入 lo / hi —— 保證兩個數來自不同陣列。"""),
 ],
 "approaches": [
   ap("解法", "一趟掃描", [("c", S["p624"])], "O(m)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>全域最大與最小在同一個陣列</strong> → 必須用次佳的組合。", "<strong>陣列只有一個元素</strong> → 頭尾相同，照常處理。"],
 "follow": [("h", "「和之前的比」技巧"), ("c", "「先查詢前面的資訊、再把自己加進去」保證不會和自己配對——兩數之和（第 1 題）的一趟雜湊表也是同一個想法。")],
 "related": ["<strong>第 121 題 買賣股票的最佳時機</strong>", "<strong>第 1 題 兩數之和</strong>"],
 "check": ["為什麼不能直接用全域最大減全域最小？", "為什麼要先更新答案再更新 lo、hi？"],
})


# ==================== 628. Maximum Product of Three Numbers ====================
S["p628"] = '''class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        a = heapq.nlargest(3, nums)
        b = heapq.nsmallest(2, nums)
        # ★ 兩種候選：最大的三個；或兩個最小（可能是兩個大負數，相乘變大正數）× 最大
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])'''

_p628 = S.load("p628")
for _ in range(3000):
    a = [random.randint(-10, 10) for _ in range(random.randint(3, 7))]
    assert _p628.maximumProduct(a) == max(x * y * z for x, y, z in combinations(a, 3))
print("P628 OK")

em({
 "num": 628, "title": "三個數的最大乘積",
 "desc": "只有兩個候選：最大的三個數，或最小的兩個數（兩個負數）乘上最大的數。",
 "zh": ["給你一個整數陣列（可能有負數），找出三個數使它們的<strong>乘積最大</strong>，回傳這個乘積。"],
 "idea": [
   ("c", """【沒有負數】最大的三個相乘。

【有負數】
    兩個負數相乘是正數。如果最小的兩個是很大的負數，
    min1 × min2 × max1 可能更大。

    例：[-10, -10, 1, 2, 3]
        最大三個：1×2×3 = 6
        兩負一正：(-10)×(-10)×3 = 300

【其他組合不可能更好】
    一個負數兩個正數 -> 乘積為負（除非沒得選，那也包含在上面兩種中）。
    三個負數 -> 選絕對值最小的三個 = 最大的三個，已包含。

【只需要 5 個數】
    最大的 3 個、最小的 2 個，一次掃描 O(n) 即可。"""),
 ],
 "approaches": [
   ap("解法", "最大三個與最小兩個", [("c", S["p628"]), "驗證方式：和枚舉所有三元組比對 3000 組。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>全是負數</strong> → 最大的三個（絕對值最小）。", "<strong>含 0</strong> → 照樣被候選涵蓋。", "<strong>剛好 3 個數</strong> → 兩個候選相同。"],
 "follow": [("h", "排序版"), ("c", "排序後答案 = max(a[-1]·a[-2]·a[-3], a[0]·a[1]·a[-1])，寫起來最短，O(n log n)。")],
 "related": ["<strong>第 152 題 乘積最大子陣列</strong>", "<strong>第 1913 題 兩個數對之間的最大乘積差</strong>"],
 "check": ["為什麼最小的兩個數可能是答案的一部分？", "為什麼不用考慮「一負兩正」？"],
})


# ==================== 629. K Inverse Pairs Array ====================
S["p629"] = '''class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] + [0] * k                  # i = 1：只有 [1]，逆序對 0 個
        for i in range(2, n + 1):
            # 新數字 i 是目前最大的，放在倒數第 j 個位置會產生 j 個新逆序對（j = 0..i-1）
            # dp'[x] = dp[x] + dp[x-1] + ... + dp[x-(i-1)]   -> 用前綴和 O(1) 算出
            pre = [0] * (k + 2)
            for x in range(k + 1):
                pre[x + 1] = (pre[x] + dp[x]) % MOD
            dp = [(pre[x + 1] - pre[max(0, x - i + 1)]) % MOD for x in range(k + 1)]   # ★ 滑動視窗和
        return dp[k]'''

_p629 = S.load("p629")
for n in range(1, 7):
    cnt = [0] * 20
    for p in permutations(range(n)):
        cnt[sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))] += 1
    for k in range(16):
        assert _p629.kInversePairs(n, k) == cnt[k]
assert _p629.kInversePairs(1000, 1000) == 663677020
print("P629 OK")

em({
 "num": 629, "title": "K 個逆序對陣列",
 "desc": "把最大的數 i 插入 i−1 的排列，能產生 0～i−1 個新逆序對；轉移是一段連續區間的和，用前綴和降到 O(nk)。",
 "zh": [
   "陣列中滿足 <code>i &lt; j</code> 且 <code>nums[i] &gt; nums[j]</code> 的索引對 <code>[i, j]</code> 稱為<strong>逆序對</strong>。",
   "給你 <code>n</code> 和 <code>k</code>，回傳由 1 到 <code>n</code> 組成、<strong>恰好</strong>有 <code>k</code> 個逆序對的排列數量，對 <code>10⁹ + 7</code> 取模。",
 ],
 "idea": [
   ("c", """【一次加一個最大的數】
    dp[i][x] = 1..i 的排列中，恰好 x 個逆序對的數量。
    在 1..i-1 的排列中插入 i（它比所有數都大）：
        插在最後  -> 新增 0 個逆序對
        插在倒數第 2 個位置 -> 新增 1 個
        ...
        插在最前面 -> 新增 i-1 個
    所以 dp[i][x] = dp[i-1][x] + dp[i-1][x-1] + ... + dp[i-1][x-(i-1)]

【直接算是 O(n · k · n)，太慢】
    右邊是 dp[i-1] 上一段長度為 i 的連續區間和 ->
    先做前綴和，每項 O(1)。
    總時間 O(n · k)。"""),
 ],
 "approaches": [
   ap("解法", "DP + 前綴和", [
     ("c", S["p629"]),
     "驗證方式：n ≤ 6 時和枚舉所有排列的逆序對分布比對；(1000, 1000) 的答案是 663677020。",
   ], "O(n · k)", "O(k)", optimal=True),
 ],
 "edges": ["<strong>k = 0</strong> → 1（只有遞增排列）。", "<strong>k > n(n−1)/2</strong> → 0。", "<strong>前綴和相減可能為負</strong> → 取模時注意（Python 的 % 會回傳非負值）。"],
 "follow": [("h", "另一種轉移"), ("c", "dp[i][x] − dp[i][x−1] = dp[i−1][x] − dp[i−1][x−i]，可以寫成 dp[i][x] = dp[i][x−1] + dp[i−1][x] − dp[i−1][x−i]，不需要另外的前綴和陣列。")],
 "related": ["<strong>第 493 題 翻轉對</strong>", "<strong>第 775 題 全域倒置與局部倒置</strong>"],
 "check": ["插入最大的數 i 時，能產生多少個新的逆序對？", "為什麼轉移可以用前綴和加速？"],
})


# ==================== 630. Course Schedule III ====================
S["p630"] = '''class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])        # 依截止日排序
        heap, t = [], 0                         # heap：已選課程的時長（最大堆積）；t：目前總時間
        for dur, last in courses:
            heapq.heappush(heap, -dur)
            t += dur
            if t > last:
                t += heapq.heappop(heap)        # ★ 超時：丟掉已選課程中最長的那一門
        return len(heap)'''

_p630 = S.load("p630")
def _bf630(cs):
    best = 0
    for r in range(len(cs) + 1):
        for sub in combinations(cs, r):
            t = 0; ok = True
            for d, l in sorted(sub, key=lambda c: c[1]):
                t += d
                if t > l: ok = False; break
            if ok: best = max(best, r)
    return best
for _ in range(1000):
    cs = [[random.randint(1, 5), random.randint(1, 12)] for _ in range(random.randint(1, 7))]
    assert _p630.scheduleCourse([c[:] for c in cs]) == _bf630(cs)
print("P630 OK")

em({
 "num": 630, "title": "課程表 III",
 "desc": "依截止日排序後逐一加入；超時就丟掉目前最長的課——貪心 + 最大堆積的經典「反悔」技巧。",
 "zh": [
   "有 <code>n</code> 門課，<code>courses[i] = [duration, lastDay]</code>：這門課要連續上 <code>duration</code> 天，而且必須在第 <code>lastDay</code> 天（含）之前上完。",
   "從第 1 天開始，一次只能上一門課。回傳最多能修完幾門課。",
 ],
 "idea": [
   ("c", """【選定一組課之後，怎麼排？】
    依截止日由早到晚上（交換論證：截止日早的先上不會更差）。
    所以先依 lastDay 排序，依序決定要不要選。

【貪心 + 反悔】
    依序把每門課加進來，累計時間 t。
    若 t 超過這門課的截止日：
        必須丟掉一門課。丟哪一門？丟「時長最長」的！
        - 課程數不變（加一門、丟一門）
        - 總時間減最多 -> 對之後的課最有利
    用最大堆積隨時取出最長的課。

【為什麼丟掉之後一定合法？】
    丟掉的課時長 >= 剛加入的這門，
    總時間不會超過「加入前」的 t，而之前是合法的。"""),
 ],
 "approaches": [
   ap("解法", "依截止日排序 + 最大堆積反悔", [("c", S["p630"]), "驗證方式：和枚舉所有子集（依截止日排序檢查可行性）的暴力法比對 1000 組。"], "O(n log n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>時長超過截止日的課</strong> → 加入後馬上被自己丟掉。", "<strong>截止日相同</strong> → 排序穩定性不影響結果。"],
 "follow": [("h", "反悔貪心"), ("c", "「先貪心選、不合法時用堆積撤銷最差的選擇」：第 871 題（最少加油次數）、第 1642 題（可以到達的最遠建築）都是同一個模式。")],
 "related": ["<strong>第 871 題 最少加油次數</strong>", "<strong>第 1642 題 可以到達的最遠建築</strong>", "<strong>第 502 題 IPO</strong>"],
 "check": ["為什麼要依截止日排序？", "超時時為什麼丟最長的課？", "丟掉之後為什麼一定合法？"],
})


# ==================== 632. Smallest Range Covering Elements from K Lists ====================
S["p632"] = '''class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(a[0], i, 0) for i, a in enumerate(nums)]   # 每個列表目前指向的元素
        heapq.heapify(heap)
        hi = max(a[0] for a in nums)
        best = [heap[0][0], hi]
        while True:
            lo, i, j = heapq.heappop(heap)          # 目前 k 個指標中的最小值
            if hi - lo < best[1] - best[0]:
                best = [lo, hi]                     # [最小, 最大] 覆蓋每個列表至少一個數
            if j + 1 == len(nums[i]):
                return best                         # ★ 最小值所在的列表用完了，區間無法再往右推
            x = nums[i][j + 1]
            heapq.heappush(heap, (x, i, j + 1))     # 只能推進最小值所在的列表
            hi = max(hi, x)'''

_p632 = S.load("p632")
assert _p632.smallestRange([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]) == [20, 24]
for _ in range(1500):
    k = random.randint(1, 4)
    nums = [sorted(random.randint(0, 15) for _ in range(random.randint(1, 4))) for _ in range(k)]
    vals = sorted({v for a in nums for v in a})
    best = None
    for a in vals:
        for b in vals:
            if a <= b and all(any(a <= v <= b for v in L) for L in nums):
                if best is None or (b - a, a) < (best[1] - best[0], best[0]):
                    best = [a, b]
    assert _p632.smallestRange(nums) == best, (nums, best)
print("P632 OK")

em({
 "num": 632, "title": "最小區間",
 "desc": "k 個指標各指向一個列表，用最小堆積找最小值並推進它——就是 k 路合併上的滑動視窗。",
 "zh": [
   "給你 <code>k</code> 個<strong>非遞減排序</strong>的整數列表，找出一個<strong>最小區間</strong> <code>[a, b]</code>，使得每個列表都至少有一個數落在區間內。",
   "區間 [a, b] 比 [c, d] 小的定義：<code>b − a &lt; d − c</code>，或長度相同但 <code>a &lt; c</code>。",
 ],
 "idea": [
   ("c", """【每個列表挑一個數 -> 區間 = [這 k 個數的最小, 最大]】
    一開始每個列表挑第一個數。

【怎麼縮小區間？】
    區間由最小值和最大值決定。
    要讓它變小，只能把最小值換掉（往右推它所在的列表）——
    推進其他列表只會讓最大值變大或不變，不可能更好。

【用最小堆積】
    堆積裡放 k 個指標，取出最小的、記錄區間、推進那個列表。
    同時維護目前的最大值 hi。
    當最小值所在的列表用完時，再也無法讓所有列表都有代表，結束。

【另一個角度】
    把所有數合併排序並標記來自哪個列表，
    就變成「包含 k 種顏色的最短視窗」（第 76 題的變形）。"""),
 ],
 "approaches": [
   ap("解法", "k 指標 + 最小堆積", [("c", S["p632"]), "驗證方式：和枚舉所有 [a, b]（a、b 取自出現過的值）的暴力法比對 1500 組。"], "O(N log k)", "O(k)", "N 為所有列表的元素總數", "", optimal=True),
 ],
 "edges": ["<strong>只有一個列表</strong> → [最小元素, 最小元素]（長度 0）。", "<strong>長度相同的區間</strong> → 取 a 較小的；嚴格小於時才更新，先找到的 a 較小。"],
 "follow": [("h", "k 路合併"), ("c", "第 23 題（合併 k 個排序鏈結串列）也是 k 個指標 + 最小堆積。本題是在合併過程中同時維護一個視窗。")],
 "related": ["<strong>第 23 題 合併 K 個排序鏈結串列</strong>", "<strong>第 76 題 最小覆蓋子字串</strong>", "<strong>第 373 題 查找和最小的 K 對數字</strong>"],
 "check": ["為什麼只推進最小值所在的列表？", "什麼時候可以結束？"],
})


# ==================== 633. Sum of Square Numbers ====================
S["p633"] = '''class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, math.isqrt(c)
        while a <= b:
            s = a * a + b * b
            if s == c:
                return True
            if s < c:
                a += 1              # ★ 太小：a 變大
            else:
                b -= 1              # 太大：b 變小
        return False'''

_p633 = S.load("p633")
sq = {i * i for i in range(400)}
for c in range(0, 100000, 7):
    assert _p633.judgeSquareSum(c) == any(c - a * a in sq for a in range(int(c ** 0.5) + 1))
assert _p633.judgeSquareSum(2 ** 31 - 1) is False
print("P633 OK")

em({
 "num": 633, "title": "平方數之和",
 "desc": "雙指標從 0 和 √c 往中間夾；附上費馬平方和定理的數論判斷。",
 "zh": ["給你非負整數 <code>c</code>，判斷是否存在整數 <code>a</code>、<code>b</code> 使 <code>a² + b² = c</code>。"],
 "idea": [
   ("c", """【雙指標】
    a 從 0、b 從 ⌊√c⌋ 開始：
        a² + b² == c -> 找到
        太小 -> a += 1
        太大 -> b -= 1
    和「有序陣列的兩數之和」一模一樣，O(√c)。

【數論做法（費馬平方和定理）】
    c 可以寫成兩個平方數之和
    <=> c 的質因數分解中，每個「除以 4 餘 3」的質數都出現偶數次。
    做質因數分解，O(√c)。"""),
 ],
 "approaches": [
   ap("解法", "雙指標", [("c", S["p633"])], "O(√c)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>c = 0</strong> → 0² + 0²，True。", "<strong>a 可以等於 b</strong> → 例如 2 = 1² + 1²。", "<strong>大數</strong> → 用 math.isqrt 避免浮點誤差。"],
 "follow": [("h", "為什麼雙指標不會漏掉答案？"), ("c", "若 a² + b² < c，目前的 a 配上任何 ≤ b 的數都更小，所以 a 不可能是答案，可以丟掉；反之亦然。每一步都安全地排除一個候選。")],
 "related": ["<strong>第 167 題 兩數之和 II（有序陣列）</strong>", "<strong>第 367 題 有效的完全平方數</strong>", "<strong>第 279 題 完全平方數</strong>"],
 "check": ["為什麼雙指標能保證不漏掉答案？", "費馬平方和定理的條件是什麼？"],
})
