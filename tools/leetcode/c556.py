# -*- coding: utf-8 -*-
"""第 556、557、558、559、560、561、563、564 題。"""
import random
from itertools import permutations
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, nodes

S = Src()
random.seed(556)


class NNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


def rand_ntree(n):
    if n == 0:
        return None
    root = NNode(random.randint(0, 9)); all_ = [root]
    for _ in range(n - 1):
        p = random.choice(all_); c = NNode(random.randint(0, 9)); p.children.append(c); all_.append(c)
    return root


# ==================== 556. Next Greater Element III ====================
S["p556"] = '''class Solution:
    def nextGreaterElement(self, n: int) -> int:
        d = list(str(n))
        i = len(d) - 2
        while i >= 0 and d[i] >= d[i + 1]:
            i -= 1                          # 從右往左找第一個「下降」的位置
        if i < 0:
            return -1                       # 整個是非遞增的：已經是最大排列
        j = len(d) - 1
        while d[j] <= d[i]:
            j -= 1                          # 右邊比 d[i] 大的最小數字（在最右邊）
        d[i], d[j] = d[j], d[i]
        d[i + 1:] = reversed(d[i + 1:])     # ★ 右邊原本遞減，反轉成遞增 = 最小
        res = int("".join(d))
        return res if res < 2 ** 31 else -1'''

_p556 = S.load("p556")
for _ in range(3000):
    n = random.randint(1, 10 ** random.randint(1, 7))
    perms = sorted({int("".join(p)) for p in permutations(str(n))})
    bigger = [x for x in perms if x > n]
    assert _p556.nextGreaterElement(n) == (bigger[0] if bigger and bigger[0] < 2 ** 31 else -1)
assert _p556.nextGreaterElement(2147483486) == -1 and _p556.nextGreaterElement(1999999999) == -1
print("P556 OK")

em({
 "num": 556, "title": "下一個更大元素 III",
 "desc": "就是第 31 題「下一個排列」套在數字的位數上，最後檢查 32 位元溢位。",
 "zh": [
   "給你一個正整數 <code>n</code>，找出由 <code>n</code> 的各位數字<strong>重新排列</strong>而成、且<strong>大於 n 的最小整數</strong>。不存在則回傳 <code>-1</code>。",
   "如果答案超過 32 位元有號整數的範圍，也回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【這就是「下一個排列」（第 31 題）】
    1. 從右往左找第一個 d[i] < d[i+1] 的 i。
       i 右邊是非遞增的 —— 這部分已經是最大排列，必須動 d[i]。
    2. 在右邊找比 d[i] 大的最小數字 d[j]（從右往左第一個 > d[i] 的），交換。
    3. 交換後 i 右邊仍是非遞增，反轉成遞增 -> 讓後綴最小。

【例】
    n = 12443
    i 指向 2（2 < 4），右邊 443 裡比 2 大的最小是 3 -> 13442
    反轉 i 右邊 -> 13244

【溢位】
    2147483486 的下一個排列 2147483648 > 2³¹ - 1 -> -1。"""),
 ],
 "approaches": [
   ap("解法", "下一個排列", [("c", S["p556"]), "驗證方式：和「列出所有排列、取大於 n 的最小值」比對 3000 個數。"], "O(位數)", "O(位數)", optimal=True),
 ],
 "edges": ["<strong>位數非遞增</strong>（如 21、999）→ −1。", "<strong>溢位</strong> → −1。", "<strong>重複數字</strong> → 比較時用 >= 與 <=。"],
 "follow": [("h", "為什麼這樣是「最小的更大」？"), ("c", "要比 n 大，必須在某位變大；變的位置越靠右越好（i 是最右邊能變的位置），變大的幅度越小越好（d[j] 是最小的更大數字），之後的位數越小越好（遞增排列）。")],
 "related": ["<strong>第 31 題 下一個排列</strong>", "<strong>第 503 題 下一個更大元素 II</strong>", "<strong>第 670 題 最大交換</strong>"],
 "check": ["為什麼要找「從右往左第一個下降」的位置？", "交換後為什麼要反轉而不是排序？", "什麼情況下會溢位？"],
})


# ==================== 557. Reverse Words in a String III ====================
S["p557"] = '''class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(w[::-1] for w in s.split(" "))   # 單字順序不變，每個單字各自反轉'''

_p557 = S.load("p557")
assert _p557.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
assert _p557.reverseWords("Mr Ding") == "rM gniD"
print("P557 OK")

em({
 "num": 557, "title": "反轉字串中的單字 III",
 "desc": "以空白切開，每個單字各自反轉再接回；不改變單字順序與空白。",
 "zh": ["給你一個句子 <code>s</code>，反轉每個單字的字元順序，但保留空白與單字的原始順序。"],
 "idea": [
   ("c", """【切開 -> 各自反轉 -> 接回】
    題目保證單字之間只有一個空白、沒有前後空白，
    split(" ") 再 join 就能完整還原空白。

【不用內建函式的寫法】
    雙指標找出每個單字的 [start, end)，原地反轉這一段。"""),
 ],
 "approaches": [
   ap("解法", "切開後各自反轉", [("c", S["p557"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>只有一個單字</strong> → 整個反轉。", "<strong>標點符號</strong> → 視為單字的一部分。"],
 "follow": [("h", "三個反轉題"), ("c", "第 151 題：反轉單字順序（每個單字不反轉）；本題：單字順序不變、每個單字反轉；兩者合起來就是反轉整個字串。")],
 "related": ["<strong>第 151 題 反轉字串中的單字</strong>", "<strong>第 541 題 反轉字串 II</strong>", "<strong>第 344 題 反轉字串</strong>"],
 "check": ["為什麼這裡可以用 split(\" \") 而不是 split()？"],
})


# ==================== 558. Logical OR of Two Binary Grids Represented as Quad-Trees ====================
class QNode:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val; self.isLeaf = isLeaf
        self.topLeft = topLeft; self.topRight = topRight; self.bottomLeft = bottomLeft; self.bottomRight = bottomRight

S["p558"] = '''class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        a, b = quadTree1, quadTree2
        if a.isLeaf:
            return a if a.val else b            # ★ 全 1 OR 任何東西 = 全 1；全 0 OR b = b
        if b.isLeaf:
            return b if b.val else a
        kids = [self.intersect(x, y) for x, y in
                ((a.topLeft, b.topLeft), (a.topRight, b.topRight),
                 (a.bottomLeft, b.bottomLeft), (a.bottomRight, b.bottomRight))]
        # 四個孩子都是同值的葉子 -> 合併成一個葉子
        if all(k.isLeaf for k in kids) and len({k.val for k in kids}) == 1:
            return Node(kids[0].val, True)
        return Node(False, False, *kids)'''

_p558 = S.load("p558", extra={"Node": QNode})
def build(g, r, c, n):
    v = {g[i][j] for i in range(r, r + n) for j in range(c, c + n)}
    if len(v) == 1:
        return QNode(v.pop() == 1, True)
    h = n // 2
    return QNode(True, False, build(g, r, c, h), build(g, r, c + h, h), build(g, r + h, c, h), build(g, r + h, c + h, h))
def grid(t, n):
    g = [[0] * n for _ in range(n)]
    def go(t, r, c, n):
        if t.isLeaf:
            for i in range(r, r + n):
                for j in range(c, c + n):
                    g[i][j] = int(t.val)
            return
        h = n // 2
        go(t.topLeft, r, c, h); go(t.topRight, r, c + h, h); go(t.bottomLeft, r + h, c, h); go(t.bottomRight, r + h, c + h, h)
    go(t, 0, 0, n); return g
def canonical(t):
    if t.isLeaf: return True
    ks = [t.topLeft, t.topRight, t.bottomLeft, t.bottomRight]
    if all(k.isLeaf for k in ks) and len({k.val for k in ks}) == 1: return False
    return all(canonical(k) for k in ks)
for _ in range(800):
    n = random.choice([1, 2, 4, 8])
    g1 = [[int(random.random() < 0.4) for _ in range(n)] for _ in range(n)]
    g2 = [[int(random.random() < 0.4) for _ in range(n)] for _ in range(n)]
    r = _p558.intersect(build(g1, 0, 0, n), build(g2, 0, 0, n))
    assert grid(r, n) == [[a | b for a, b in zip(x, y)] for x, y in zip(g1, g2)] and canonical(r)
print("P558 OK")

em({
 "num": 558, "title": "四叉樹交集",
 "desc": "遞迴 OR：遇到全 1 的葉子直接回傳它，遇到全 0 的葉子回傳另一棵；四個孩子相同時要合併。",
 "zh": [
   "<strong>四叉樹</strong>把一個 n×n 的 0/1 格子遞迴切成四塊：若某塊全是同一個值，就是一個葉子（<code>isLeaf = True</code>，<code>val</code> 是那個值）；否則再切成左上、右上、左下、右下四個子樹。",
   "給你兩棵四叉樹 <code>quadTree1</code>、<code>quadTree2</code>，各代表一個 n×n 的二元矩陣。回傳代表兩個矩陣<strong>逐格 OR</strong> 結果的四叉樹。",
   "（題目名稱是 intersect，但實際做的是邏輯 OR。）",
 ],
 "idea": [
   ("c", """【葉子的捷徑】
    a 是全 1 的葉子：1 OR 任何值 = 1 -> 直接回傳 a。
    a 是全 0 的葉子：0 OR x = x    -> 直接回傳 b。
    b 是葉子時同理。

【兩個都不是葉子】
    四個象限分別遞迴。

【合併】
    遞迴結果可能四個孩子都變成同值的葉子
    （例如兩邊互補，OR 之後全是 1）——
    這時要合併成一個葉子，否則不是合法（最簡）的四叉樹。"""),
 ],
 "approaches": [
   ap("解法", "遞迴 OR + 合併", [
     ("c", S["p558"]),
     "驗證方式：由隨機格子建四叉樹，OR 之後還原成格子比對，並檢查結果是最簡的（沒有可以合併的四個同值葉子）。",
   ], "O(n²)", "O(log n)", "最壞每個格子都是葉子", "遞迴深度", optimal=True),
 ],
 "edges": ["<strong>一棵是全 1 的葉子</strong> → 直接回傳它。", "<strong>OR 之後四塊都是 1</strong> → 必須合併。"],
 "follow": [("h", "四叉樹的用途"), ("c", "影像壓縮（大片同色區域用一個節點表示）、地圖的空間索引、碰撞偵測。第 427 題是由格子建四叉樹。")],
 "related": ["<strong>第 427 題 建立四叉樹</strong>"],
 "check": ["遇到全 0 的葉子為什麼回傳另一棵？", "為什麼遞迴後要檢查是否能合併？"],
})


# ==================== 559. Maximum Depth of N-ary Tree ====================
S["p559"] = '''class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        return 1 + max((self.maxDepth(c) for c in root.children), default=0)   # 沒有孩子時 max 用 default'''

_p559 = S.load("p559", extra={"Node": NNode})
def _d(t): return 0 if t is None else 1 + max([_d(c) for c in t.children] + [0])
for _ in range(500):
    t = rand_ntree(random.randint(0, 15)); assert _p559.maxDepth(t) == _d(t)
print("P559 OK")

em({
 "num": 559, "title": "N 叉樹的最大深度",
 "desc": "和二元樹一樣：1 + 所有孩子深度的最大值；沒有孩子時要處理空的 max。",
 "zh": ["給你一棵 N 叉樹的根節點，回傳它的<strong>最大深度</strong>：從根到最遠葉子節點經過的節點數。"],
 "idea": [
   ("c", """【遞迴】
    depth(nd) = 1 + max(depth(c) for c in nd.children)
    葉子沒有孩子 -> max 的參數是空的，用 default=0。

【BFS】
    一層一層走，數層數。"""),
 ],
 "approaches": [
   ap("解法", "遞迴", [("c", S["p559"])], "O(n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>空樹</strong> → 0。", "<strong>葉子</strong> → max 的空序列要給 default。"],
 "follow": [("h", "N 叉樹系列"), ("c", "第 589、590 題（前序、後序）、第 429 題（層序）。二元樹的寫法把「左、右」換成「所有孩子」即可。")],
 "related": ["<strong>第 104 題 二元樹的最大深度</strong>", "<strong>第 589 題 N 叉樹的前序走訪</strong>"],
 "check": ["葉子節點的 max 為什麼需要 default？"],
})


# ==================== 560. Subarray Sum Equals K ====================
S["p560"] = '''class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = Counter({0: 1})          # 前綴和 -> 出現次數（空前綴的和是 0）
        s = res = 0
        for x in nums:
            s += x
            res += seen[s - k]          # ★ 之前有幾個前綴和等於 s - k，就有幾段以這裡結尾、和為 k
            seen[s] += 1
        return res'''

from collections import Counter
_p560 = S.load("p560", extra={"Counter": Counter})
for _ in range(3000):
    a = [random.randint(-3, 3) for _ in range(random.randint(1, 10))]; k = random.randint(-4, 4)
    want = sum(sum(a[i:j]) == k for i in range(len(a)) for j in range(i + 1, len(a) + 1))
    assert _p560.subarraySum(a, k) == want
print("P560 OK")

em({
 "num": 560, "title": "和為 K 的子陣列",
 "desc": "有負數所以不能用滑動視窗；前綴和 + 雜湊表計數：以每個位置結尾、和為 k 的子陣列有幾個。",
 "zh": ["給你整數陣列 <code>nums</code>（<strong>可能有負數</strong>）和整數 <code>k</code>，回傳和為 <code>k</code> 的連續子陣列的<strong>個數</strong>。"],
 "idea": [
   ("c", """【為什麼不能用滑動視窗？】
    有負數 -> 視窗擴大不一定讓和變大，失去單調性。

【前綴和】
    nums[i+1..j] 的和 = P[j] - P[i]。
    它等於 k <=> P[i] = P[j] - k。

【雜湊表記次數】
    掃到 j 時，以 j 結尾、和為 k 的子陣列個數
    = 之前有幾個前綴和等於 P[j] - k。
    先查、再把 P[j] 加入（避免和自己配對成空陣列）。
    空前綴 P = 0 預先放一次。"""),
 ],
 "approaches": [
   ap("解法", "前綴和 + 雜湊表計數", [("c", S["p560"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>k = 0</strong> → 前綴和重複出現的次數。", "<strong>負數</strong> → 同一個前綴和可能出現多次，所以要記次數。", "<strong>先查後加</strong> → 順序反了會把空子陣列算進去（k = 0 時）。"],
 "follow": [("h", "家族"), ("c", "第 523 題（和為 k 的倍數：記餘數的第一次位置）、第 974 題（記餘數的次數）、第 1074 題（二維版：枚舉上下邊界後變成本題）。")],
 "related": ["<strong>第 523 題 連續的子陣列和</strong>", "<strong>第 974 題 和可被 K 整除的子陣列</strong>", "<strong>第 1074 題 元素和為目標值的子矩陣數量</strong>"],
 "check": ["為什麼滑動視窗不適用？", "seen 的初始值為什麼是 {0: 1}？", "為什麼要先查再加？"],
})


# ==================== 561. Array Partition ====================
S["p561"] = '''class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])           # ★ 排序後相鄰兩兩配對，取每對的較小者（偶數索引）'''

_p561 = S.load("p561")
for _ in range(500):
    a = [random.randint(-5, 5) for _ in range(2 * random.randint(1, 4))]
    best = max(sum(min(p[i], p[i + 1]) for i in range(0, len(p), 2)) for p in permutations(a))
    assert _p561.arrayPairSum(a[:]) == best
print("P561 OK")

em({
 "num": 561, "title": "陣列拆分",
 "desc": "排序後相鄰配對：最小的數一定是某對的較小者，讓它和「次小」配對浪費最少。",
 "zh": ["給你長度為 <code>2n</code> 的整數陣列，把它分成 <code>n</code> 對，使每對較小值的<strong>總和最大</strong>，回傳這個總和。"],
 "idea": [
   ("c", """【貪心】
    最小的數 a₁ 不管和誰配對，它都是那一對的較小者，一定會被算進去。
    它的配對對象「被浪費」了（不計分），
    所以應該浪費最小的那個：讓它和次小的 a₂ 配對。
    遞迴下去 -> 排序後 (a₁,a₂), (a₃,a₄), ... 配對。
    答案 = 排序後偶數索引的和。"""),
 ],
 "approaches": [
   ap("解法", "排序後相鄰配對", [("c", S["p561"]), "驗證方式：和枚舉所有排列的暴力法比對。"], "O(n log n)", "O(1)", "", "", optimal=True),
 ],
 "edges": ["<strong>負數</strong> → 照樣成立。", "<strong>重複值</strong> → 不影響。"],
 "follow": [("h", "計數排序"), ("c", "值域只有 [−10⁴, 10⁴]，可以用計數排序做到 O(n + 值域)。")],
 "related": ["<strong>第 881 題 救生艇</strong>", "<strong>第 1877 題 陣列中最大數對和的最小值</strong>"],
 "check": ["為什麼最小的數要和次小的數配對？"],
})


# ==================== 563. Binary Tree Tilt ====================
S["p563"] = '''class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0
        def total(nd):                  # 回傳子樹和，同時累加坡度
            nonlocal res
            if not nd:
                return 0
            L, R = total(nd.left), total(nd.right)
            res += abs(L - R)           # ★ 這個節點的坡度
            return nd.val + L + R
        total(root)
        return res'''

_p563 = S.load("p563")
def _ss(t): return 0 if t is None else t.val + _ss(t.left) + _ss(t.right)
for _ in range(1000):
    t = rand_tree(random.randint(0, 12), -5, 9)
    want = sum(abs(_ss(n.left) - _ss(n.right)) for n in nodes(t)) if t else 0
    assert _p563.findTilt(t) == want
print("P563 OK")

em({
 "num": 563, "title": "二元樹的坡度",
 "desc": "後序走訪回傳子樹和，同時在每個節點累加 |左子樹和 − 右子樹和|。",
 "zh": [
   "一個節點的<strong>坡度</strong> = |左子樹所有節點值之和 − 右子樹所有節點值之和|（沒有子樹的那邊和為 0）。",
   "回傳整棵樹所有節點坡度的<strong>總和</strong>。",
 ],
 "idea": [
   ("c", """【需要每個節點的左右子樹和】
    後序走訪：total(nd) 回傳子樹和；
    拿到 L、R 後順便把 |L - R| 加進全域答案。
    每個節點只算一次 -> O(n)。

【不要這樣做】
    對每個節點各自重新計算子樹和 -> O(n²)。"""),
 ],
 "approaches": [
   ap("解法", "後序走訪", [("c", S["p563"])], "O(n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>空樹</strong> → 0。", "<strong>葉子</strong> → 坡度 0。"],
 "follow": [("h", "同一個模式"), ("c", "「回傳 A、順便算 B」：第 543 題回傳深度、算直徑；第 508 題回傳子樹和、統計次數；本題回傳子樹和、累加坡度。")],
 "related": ["<strong>第 508 題 出現次數最多的子樹元素和</strong>", "<strong>第 543 題 二元樹的直徑</strong>"],
 "check": ["遞迴函式回傳什麼？坡度在哪裡累加？"],
})


# ==================== 564. Find the Closest Palindrome ====================
S["p564"] = '''class Solution:
    def nearestPalindromic(self, n: str) -> str:
        L, x = len(n), int(n)
        cands = {10 ** L + 1, 10 ** (L - 1) - 1}       # 位數變多（10..01）或變少（9..9）的情況
        prefix = int(n[:(L + 1) // 2])                  # 前半段（奇數長度含中間位）
        for p in (prefix - 1, prefix, prefix + 1):      # ★ 前半段 ±1，再鏡射成迴文
            s = str(p)
            cands.add(int(s + s[::-1][L % 2:]))         # 奇數長度時中間位不重複
        cands.discard(x)                                # 不能是自己
        return str(min(cands, key=lambda c: (abs(c - x), c)))'''

_p564 = S.load("p564")
def _bf564(x):
    d = 1
    while True:
        for c in (x - d, x + d):
            if c >= 0 and str(c) == str(c)[::-1]:
                return c
        d += 1
for x in list(range(1, 3000)) + [random.randint(1, 10 ** 8) for _ in range(300)]:
    assert int(_p564.nearestPalindromic(str(x))) == _bf564(x), x
assert _p564.nearestPalindromic("123") == "121" and _p564.nearestPalindromic("1") == "0"
assert _p564.nearestPalindromic("99") == "101" and _p564.nearestPalindromic("1000") == "999"
print("P564 OK")

em({
 "num": 564, "title": "尋找最近的迴文數",
 "desc": "答案只有五個候選：前半段 −1、不變、+1 再鏡射，以及位數變多的 10…01 和變少的 9…9。",
 "zh": [
   "給你一個用字串表示的整數 <code>n</code>，回傳<strong>最接近</strong>它的迴文整數（不包含它自己）。",
   "若有兩個一樣近，回傳<strong>較小</strong>的那個。「最接近」指兩數之差的絕對值最小。",
 ],
 "idea": [
   ("c", """【迴文由前半段決定】
    長度 L 的迴文，只要知道前 ⌈L/2⌉ 位，後半段就是鏡射。
    要離 n 最近 -> 前半段應該和 n 的前半段差不多：
        prefix - 1、prefix、prefix + 1，各自鏡射成迴文。

【位數改變的情況】
    n = 99    -> 最近的是 101（位數變多）
    n = 1000  -> 最近的是 999（位數變少）
    n = 10    -> 9
    所以再加兩個候選：10^L + 1、10^(L-1) - 1。

【從 5 個候選中挑】
    排除 n 自己，選 |c - n| 最小，平手選較小的。

【注意奇偶長度】
    奇數長度時中間位不能重複：鏡射時跳過反轉後的第一個字元。"""),
 ],
 "approaches": [
   ap("解法", "五個候選", [
     ("c", S["p564"]),
     "驗證方式：1～3000 全部，加上 300 個隨機八位數，和「往兩側逐一找迴文」的暴力法比對。",
   ], "O(L)", "O(L)", optimal=True),
 ],
 "edges": ["<strong>n = \"1\"</strong> → \"0\"。", "<strong>n = \"10\"</strong> → \"9\"。", "<strong>n 本身是迴文</strong>（如 \"121\"）→ 不能回傳自己，答案是 111 或 131 中較近／較小的。", "<strong>平手</strong> → 取較小。"],
 "follow": [("h", "為什麼 5 個候選就夠？"), ("c", "同樣位數的迴文中，最接近 n 的一定由 n 的前半段或它的 ±1 產生（前半段差 2 以上，整數差距至少是 10^(L/2) 等級，比 ±1 的候選更遠）；位數不同的迴文中，最近的就是 9…9 或 10…01。")],
 "related": ["<strong>第 9 題 迴文數</strong>", "<strong>第 479 題 最大回文數乘積</strong>", "<strong>第 906 題 超級回文數</strong>"],
 "check": ["為什麼只看前半段 ±1？", "哪兩種情況會讓位數改變？", "奇數長度的鏡射要注意什麼？"],
})
