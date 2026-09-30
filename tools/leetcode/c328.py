# -*- coding: utf-8 -*-
"""第 328、329、330、331、332、334 題。"""
import random
import itertools
from collections import defaultdict
from authoring import emit, ap
from runner import Src, to_list, from_list
from lchelp import rand_tree

S = Src()
random.seed(328)


# ==================== 328. Odd Even Linked List ====================
S["p328"] = '''class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        odd, even = head, head.next
        even_head = even                        # 記住偶數串的開頭，最後要接上
        while even and even.next:
            odd.next = even.next                # ★ 奇數跳過一個偶數
            odd = odd.next
            even.next = odd.next                # 偶數跳過一個奇數
            even = even.next
        odd.next = even_head                    # 奇數串的尾巴接上偶數串
        return head'''

_p328 = S.load("p328")
for n in range(0, 12):
    for _ in range(20):
        vals = [random.randrange(-9, 9) for _ in range(n)]
        assert from_list(_p328.oddEvenList(to_list(vals))) == vals[::2] + vals[1::2]
print("P328 OK")

_P328_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">兩條串列交錯前進：odd 跳過偶數，even 跳過奇數</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="56" width="44" height="28" fill="none" stroke="var(--accent)"/><text x="62" y="75" fill="var(--accent)">1</text>
              <rect x="120" y="56" width="44" height="28" fill="none" stroke="var(--gold)"/><text x="142" y="75" fill="var(--gold)">2</text>
              <rect x="200" y="56" width="44" height="28" fill="none" stroke="var(--accent)"/><text x="222" y="75" fill="var(--accent)">3</text>
              <rect x="280" y="56" width="44" height="28" fill="none" stroke="var(--gold)"/><text x="302" y="75" fill="var(--gold)">4</text>
              <rect x="360" y="56" width="44" height="28" fill="none" stroke="var(--accent)"/><text x="382" y="75" fill="var(--accent)">5</text>
            </g>
            <g fill="none" stroke-width="1.5">
              <path d="M62 84 C 90 116, 190 116, 218 86" stroke="var(--accent)"/>
              <path d="M222 84 C 250 116, 350 116, 378 86" stroke="var(--accent)"/>
              <path d="M142 56 C 170 30, 270 30, 298 54" stroke="var(--gold)"/>
            </g>
            <text x="440" y="66" fill="var(--gold)" font-size="12">偶數串：2 → 4</text>
            <text x="440" y="112" fill="var(--accent)" font-size="12">奇數串：1 → 3 → 5</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="140" width="44" height="28" fill="none" stroke="var(--accent)"/><text x="62" y="159" fill="var(--accent)">1</text>
              <rect x="110" y="140" width="44" height="28" fill="none" stroke="var(--accent)"/><text x="132" y="159" fill="var(--accent)">3</text>
              <rect x="180" y="140" width="44" height="28" fill="none" stroke="var(--accent)"/><text x="202" y="159" fill="var(--accent)">5</text>
              <rect x="270" y="140" width="44" height="28" fill="none" stroke="var(--gold)"/><text x="292" y="159" fill="var(--gold)">2</text>
              <rect x="340" y="140" width="44" height="28" fill="none" stroke="var(--gold)"/><text x="362" y="159" fill="var(--gold)">4</text>
            </g>
            <g stroke="var(--text-muted)"><line x1="84" y1="154" x2="110" y2="154"/><line x1="154" y1="154" x2="180" y2="154"/><line x1="314" y1="154" x2="340" y2="154"/></g>
            <line x1="224" y1="154" x2="270" y2="154" stroke="#ff8a65" stroke-width="2"/>
            <text x="247" y="190" text-anchor="middle" fill="#ff8a65" font-size="12">odd.next = even_head</text>
            <text x="20" y="222" fill="var(--text)" font-size="12">只改指標，不建立新節點：O(1) 額外空間。</text>'''

emit({
 "num": 328, "slug": "odd-even-linked-list",
 "en": [
   "Given the <code>head</code> of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return <em>the reordered list</em>.",
   "The <strong>first</strong> node is considered <strong>odd</strong>, and the <strong>second</strong> node is <strong>even</strong>, and so on.",
   "Note that the relative order inside both the even and odd groups should remain as it was in the input.",
   "You must solve the problem in <code>O(1)</code> extra space complexity and <code>O(n)</code> time complexity.",
 ],
 "zh": [
   "給你一個單向鏈結串列的頭節點 <code>head</code>，把所有<strong>奇數位置</strong>的節點排在前面、<strong>偶數位置</strong>的節點排在後面，回傳重排後的串列。",
   "第一個節點算奇數，第二個算偶數，以此類推（看的是<strong>位置</strong>，不是節點的值）。兩組內部都要保持原本的相對順序。",
   "必須 <code>O(1)</code> 額外空間、<code>O(n)</code> 時間。",
 ],
 "examples": """範例 1
  輸入：head = [1,2,3,4,5]
  輸出：[1,3,5,2,4]

範例 2
  輸入：head = [2,1,3,5,6,4,7]
  輸出：[2,3,6,7,1,5,4]""",
 "constraints": [
   "節點數在 <code>[0, 10⁴]</code> 之間",
   "−10⁶ ≤ <code>Node.val</code> ≤ 10⁶",
 ],
 "idea": [
   ("fig", _P328_FIG, "0 0 640 236"),
   ("c", """【把一條串列拆成兩條，再接起來】
    odd 指標負責奇數位置，even 指標負責偶數位置。
    每一步：
        odd.next  = even.next   （odd 跳過一個偶數節點）
        even.next = odd.next    （even 跳過一個奇數節點）
    最後把奇數串的尾巴接到偶數串的開頭。

【迴圈條件：even and even.next】
    even 是 None：長度是奇數，odd 停在最後一個
    even.next 是 None：長度是偶數，even 停在最後一個
    兩種情況下 odd 都停在奇數串的最後一個節點 ✔

【一定要先記住 even_head】
    迴圈過程中 head.next 已經被改掉了，之後找不到偶數串的開頭。"""),
 ],
 "approaches": [
   ap("解法", "奇偶兩條串列交錯前進", [
     ("c", S["p328"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>空串列</strong> → None。",
   "<strong>一個或兩個節點</strong> → 不變。",
   "<strong>看的是位置不是值</strong> → 範例 2 中值 2 排在最前面。",
 ],
 "follow": [
   ("h", "同一個骨架"),
   ("c", "第 86 題「分隔鏈結串列」：依值分成兩條（小於 x、大於等於 x）再接起來；只是分組條件從「位置奇偶」換成「值的大小」。"),
 ],
 "related": [
   "<strong>第 86 題 分隔鏈結串列</strong>",
   "<strong>第 725 題 分隔鏈結串列</strong>（分成 k 段）",
 ],
 "check": [
   "迴圈的結束條件為什麼是 <code>even and even.next</code>？",
   "為什麼要事先記住 <code>even_head</code>？",
 ],
})


# ==================== 329. Longest Increasing Path in a Matrix ====================
S["p329"] = '''class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # ★ 嚴格遞增 -> 不可能繞回原點，不需要 visited，可以直接記憶化
        @functools.lru_cache(None)
        def dfs(i: int, j: int) -> int:           # 從 (i, j) 出發的最長遞增路徑
            best = 1
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    best = max(best, 1 + dfs(x, y))
            return best

        return max(dfs(i, j) for i in range(m) for j in range(n))'''

S["p329_topo"] = '''class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        outdeg = [[0] * n for _ in range(m)]      # 有幾個鄰居比我大
        for i in range(m):
            for j in range(n):
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        outdeg[i][j] += 1
        # 從「局部最大值」（沒有更大的鄰居）開始，一層一層往回剝
        layer = [(i, j) for i in range(m) for j in range(n) if outdeg[i][j] == 0]
        depth = 0
        while layer:
            depth += 1
            nxt = []
            for i, j in layer:
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                        outdeg[x][y] -= 1
                        if outdeg[x][y] == 0:
                            nxt.append((x, y))
            layer = nxt
        return depth                              # 層數 = 最長路徑的長度'''

_p329 = [S.load(x) for x in ("p329", "p329_topo")]
for M, want in [([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4), ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4), ([[1]], 1)]:
    for sol in _p329:
        assert sol.longestIncreasingPath(M) == want
for _ in range(800):
    m, n = random.randrange(1, 6), random.randrange(1, 6)
    M = [[random.randrange(0, 6) for _ in range(n)] for _ in range(m)]
    assert _p329[0].longestIncreasingPath(M) == _p329[1].longestIncreasingPath(M), M
print("P329 OK")

emit({
 "num": 329, "slug": "longest-increasing-path-in-a-matrix",
 "en": [
   "Given an <code>m x n</code> integers <code>matrix</code>, return <em>the length of the longest increasing path in</em> <code>matrix</code>.",
   "From each cell, you can either move in four directions: left, right, up, or down. You <strong>may not</strong> move <strong>diagonally</strong> or move <strong>outside the boundary</strong> (i.e., wrap-around is not allowed).",
 ],
 "zh": [
   "給你一個 <code>m x n</code> 的整數矩陣，回傳其中<strong>最長嚴格遞增路徑</strong>的長度。",
   "每一步可以往上下左右四個方向移動，不能斜走，也不能走出邊界。",
 ],
 "examples": """範例 1
  輸入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
  輸出：4
  說明：1 → 2 → 6 → 9

範例 2
  輸入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
  輸出：4
  說明：3 → 4 → 5 → 6""",
 "constraints": [
   "1 ≤ <code>m, n</code> ≤ 200",
   "0 ≤ <code>matrix[i][j]</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【一般的「最長路徑」是 NP 困難的】
    但這題有一個關鍵：路徑必須【嚴格遞增】。

【嚴格遞增 -> 不會有環】
    沿著路徑值一直變大，不可能回到走過的格子。
    所以：
    - 不需要 visited 集合
    - 「從 (i, j) 出發的最長路徑」只和 (i, j) 有關 -> 可以記憶化！

【記憶化 DFS】
    dfs(i, j) = 1 + max(dfs(鄰居))，只看比自己大的鄰居。
    每個格子只算一次 -> O(mn)。

【拓樸排序觀點】
    把「小 -> 大」當成有向邊，整張圖是 DAG。
    DAG 上的最長路徑 = 拓樸排序的層數。
    從沒有更大鄰居的格子（終點）開始，一層一層往回剝。"""),
 ],
 "approaches": [
   ap("解法一", "記憶化 DFS", [
     ("c", S["p329"]),
     "40000 個格子時遞迴深度可能很深（例如蛇形遞增），Python 需要調高遞迴上限；拓樸排序版本沒有這個問題。",
   ], "O(mn)", "O(mn)", "", "", optimal=True),

   ap("解法二", "拓樸排序（BFS 剝層）", [
     ("c", S["p329_topo"]),
   ], "O(mn)", "O(mn)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["暴力 DFS", "指數", "O(mn)", "沒有記憶化"],
    ["一、記憶化 DFS", "O(mn)", "O(mn)", "最直觀 ✔"],
    ["二、拓樸排序", "O(mn)", "O(mn)", "不用遞迴"]]),
 "edges": [
   "<strong>全部相同</strong> → 1（嚴格遞增，無法移動）。",
   "<strong>1 × 1</strong> → 1。",
   "<strong>蛇形遞增</strong> → 路徑長 mn，遞迴深度也是 mn。",
 ],
 "follow": [
   ("h", "記憶化的前提"),
   ("c", "能記憶化的條件：子問題的答案不依賴「怎麼走到這裡的」。如果允許走相等的值，就可能繞圈，子問題會依賴 visited 狀態，記憶化就不成立了。"),
 ],
 "related": [
   "<strong>第 300 題 最長遞增子序列</strong>",
   "<strong>第 2328 題 網格圖中遞增路徑的數目</strong> —— 同一個記憶化 DFS，改成計數",
   "<strong>第 207 題 課程表</strong> —— 拓樸排序",
 ],
 "check": [
   "為什麼這一題不需要 visited？",
   "為什麼可以記憶化？",
   "拓樸排序版本的層數為什麼等於最長路徑長度？",
 ],
})


# ==================== 330. Patching Array ====================
S["p330"] = '''class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        reach = 0            # ★ 目前可以湊出 [1, reach] 的每一個數
        i = patches = 0
        while reach < n:
            if i < len(nums) and nums[i] <= reach + 1:
                reach += nums[i]         # 用現有的數擴展：[1, reach + nums[i]]
                i += 1
            else:
                reach += reach + 1       # 補上 reach+1：範圍直接翻倍
                patches += 1
        return patches'''

_p330 = S.load("p330")


def _mp_ref(nums, n):
    def cover(arr):
        sums = {0}
        for x in arr:
            sums |= {s + x for s in sums}
        return all(v in sums for v in range(1, n + 1))
    for k in range(0, 8):
        for add in itertools.combinations_with_replacement(range(1, n + 1), k):
            if cover(list(nums) + list(add)):
                return k
    return None


for nums, n, want in [([1, 3], 6, 1), ([1, 5, 10], 20, 2), ([1, 2, 2], 5, 0)]:
    assert _p330.minPatches(nums, n) == want
for _ in range(300):
    nums = sorted(random.randrange(1, 10) for _ in range(random.randrange(0, 4)))
    n = random.randrange(1, 14)
    want = _mp_ref(nums, n)
    assert _p330.minPatches(nums, n) == want, (nums, n)
assert _p330.minPatches([], 2 ** 31 - 1) == 31
print("P330 OK")

emit({
 "num": 330, "slug": "patching-array",
 "en": [
   "Given a sorted integer array <code>nums</code> and an integer <code>n</code>, add/patch elements to the array such that any number in the range <code>[1, n]</code> inclusive can be formed by the sum of some elements in the array.",
   "Return <em>the minimum number of patches required</em>.",
 ],
 "zh": [
   "給你一個已排序的正整數陣列 <code>nums</code> 和整數 <code>n</code>。請補上最少的數字，使得 <code>[1, n]</code> 中的每一個整數，都能表示成陣列中某些元素的和（每個元素最多用一次）。",
   "回傳最少要補幾個數。",
 ],
 "examples": """範例 1
  輸入：nums = [1,3], n = 6
  輸出：1
  說明：補上 2 之後，[1,2,3] 能湊出 1..6。

範例 2
  輸入：nums = [1,5,10], n = 20
  輸出：2
  說明：補上 2 和 4。

範例 3
  輸入：nums = [1,2,2], n = 5
  輸出：0""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 1000",
   "1 ≤ <code>nums[i]</code> ≤ 10⁴",
   "<code>nums</code> 遞增排序",
   "1 ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【關鍵不變量】
    假設目前的數字能湊出 [1, reach] 的每一個數。
    再加入一個數 x：
        x <= reach + 1 -> 新的範圍是 [1, reach + x]（原本的 + x 無縫接上）
        x >  reach + 1 -> reach + 1 永遠湊不出來（其他數都太大）

【貪心】
    下一個 nums[i] <= reach + 1 -> 直接用它擴展
    否則 reach + 1 湊不出來，必須補一個數 ->
        補哪個最好？補 reach + 1 本身！
        範圍變成 [1, 2·reach + 1]，擴展得最多。

【為什麼很快？】
    每次補數，reach 至少翻倍 -> 最多補 O(log n) 個。
    n = 2³¹ - 1、nums 為空：補 1, 2, 4, ..., 2³⁰ 共 31 個。"""),
   ("c", """  nums = [1, 5, 10], n = 20
  reach = 0    用 1        -> reach = 1
  reach = 1    5 > 2，補 2 -> reach = 3
  reach = 3    5 > 4，補 4 -> reach = 7
  reach = 7    用 5        -> reach = 12
  reach = 12   用 10       -> reach = 22 >= 20，結束。補了 2 個 ✔"""),
 ],
 "approaches": [
   ap("解法", "貪心：維護可湊出的範圍", [
     ("c", S["p330"]),
   ], "O(m + log n)", "O(1)", "m = nums 長度", "", optimal=True),
 ],
 "edges": [
   "<strong>nums 為空</strong> → 補 1, 2, 4, …，約 log₂ n 個。",
   "<strong>nums 沒有 1</strong> → 一定要補 1。",
   "<strong>重複的數</strong>（<code>[1,2,2]</code>）→ 每個都可以用一次，照樣擴展。",
   "<strong>n 很大</strong> → 其他語言的 reach 要用 64 位元，否則 2·reach + 1 會溢位。",
 ],
 "follow": [
   ("h", "同一個不變量"),
   ("c", "第 1798 題「你能構造出連續值的最大數目」：幾乎完全相同，只是不能補數，問最多能連續湊到多少。第 2952 題「需要添加的硬幣的最小數量」也是同一題。"),
 ],
 "related": [
   "<strong>第 1798 題 你能構造出連續值的最大數目</strong>",
   "<strong>第 2952 題 需要添加的硬幣的最小數量</strong>",
 ],
 "check": [
   "「可以湊出 [1, reach]」再加入 x，新的範圍是什麼？條件是什麼？",
   "需要補數時，為什麼補 reach + 1 最好？",
   "為什麼補的數最多只有 O(log n) 個？",
 ],
})


# ==================== 331. Verify Preorder Serialization of a Binary Tree ====================
S["p331"] = '''class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1                              # ★ 目前有幾個「空位」可以放節點（一開始留給根）
        for tok in preorder.split(","):
            if slots == 0:                     # 沒有空位了卻還有節點
                return False
            slots -= 1                         # 每個節點（含 #）佔掉一個空位
            if tok != "#":
                slots += 2                     # 非空節點帶來兩個新空位（左、右孩子）
        return slots == 0                      # 所有空位剛好填滿'''

S["p331_stack"] = '''class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for tok in preorder.split(","):
            stack.append(tok)
            # 「數字, #, #」代表一棵完整的葉子子樹 -> 化簡成一個 #
            while len(stack) >= 3 and stack[-1] == stack[-2] == "#" and stack[-3] != "#":
                del stack[-3:]
                stack.append("#")
        return stack == ["#"]'''

_p331 = [S.load(x) for x in ("p331", "p331_stack")]


def _ser_pre(nd, out):
    if nd is None:
        out.append("#")
        return
    out.append(str(nd.val))
    _ser_pre(nd.left, out)
    _ser_pre(nd.right, out)


def _valid_ref(toks):
    def parse(i):              # 回傳解析一棵樹後的位置，失敗回傳 -1
        if i >= len(toks):
            return -1
        if toks[i] == "#":
            return i + 1
        j = parse(i + 1)
        return -1 if j < 0 else parse(j)
    return parse(0) == len(toks)


for s, want in [("9,3,4,#,#,1,#,#,2,#,6,#,#", True), ("1,#", False), ("9,#,#,1", False), ("#", True)]:
    for sol in _p331:
        assert sol.isValidSerialization(s) == want
for _ in range(2000):
    if random.random() < 0.5:
        out = []
        _ser_pre(rand_tree(random.randrange(0, 12)), out)
        toks = out
        if random.random() < 0.5 and len(toks) > 1:
            k = random.randrange(len(toks))
            toks = toks[:k] + toks[k + 1:] if random.random() < 0.5 else toks[:k] + [random.choice(["#", "5"])] + toks[k:]
    else:
        toks = [random.choice(["#", "#", "1"]) for _ in range(random.randrange(1, 10))]
    s = ",".join(toks)
    want = _valid_ref(toks)
    for sol in _p331:
        assert sol.isValidSerialization(s) == want, (s, sol)
print("P331 OK")

emit({
 "num": 331, "slug": "verify-preorder-serialization-of-a-binary-tree",
 "en": [
   "One way to serialize a binary tree is to use <strong>preorder traversal</strong>. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as <code>'#'</code>.",
   "Given a string of comma-separated values <code>preorder</code>, return <code>true</code> if it is a correct preorder traversal serialization of a binary tree.",
   "It is <strong>guaranteed</strong> that each comma-separated value in the string must be either an integer or a character <code>'#'</code> representing null pointer. "
   "You may assume that the input format is always valid.",
   "<strong>Note:</strong> You are not allowed to reconstruct the tree.",
 ],
 "zh": [
   "二元樹的一種序列化方式是<strong>前序遍歷</strong>：遇到非空節點記下它的值，遇到空節點記下 <code>'#'</code>。",
   "給你一個以逗號分隔的字串 <code>preorder</code>，判斷它是不是某棵二元樹<strong>正確的</strong>前序序列化結果。",
   "每個值保證是整數或 <code>'#'</code>，格式一定正確。",
   "<strong>注意：</strong>不能把樹重建出來。",
 ],
 "examples": """範例 1
  輸入：preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
  輸出：true

範例 2
  輸入：preorder = "1,#"
  輸出：false

範例 3
  輸入：preorder = "9,#,#,1"
  輸出：false""",
 "constraints": [
   "1 ≤ <code>preorder.length</code> ≤ 10⁴",
   "<code>preorder</code> 由 [0, 100] 的整數和 <code>'#'</code> 以逗號分隔組成",
 ],
 "idea": [
   ("c", """【數「空位」（slots）】
    想像一棵樹是一個一個「位置」被填上去的：
        一開始只有 1 個空位（根的位置）
        每讀一個 token，佔掉 1 個空位
        如果是非空節點，它又提供 2 個新空位（左孩子、右孩子）
        如果是 #，不提供新空位

    合法 <=>
        途中每次要放節點時都還有空位（slots > 0）
        而且最後空位剛好用完（slots == 0）

【範例 "1,#"】
    slots: 1 -> 讀 1：0 + 2 = 2 -> 讀 #：1
    結束時 slots = 1 != 0 -> 還有一個右孩子的位置沒填 ✘

【範例 "9,#,#,1"】
    slots: 1 -> 9：2 -> #：1 -> #：0 -> 讀 1 時 slots = 0 ✘

【另一個角度：出度 = 入度】
    樹中 非空節點數 + 1 = 空節點數（每個非空節點有 2 條往下的邊）。
    slots 就是在即時追蹤這個差。"""),
 ],
 "approaches": [
   ap("解法一", "堆疊化簡", [
     ("c", S["p331_stack"]),
     "每當堆疊頂端是「數字, #, #」，就代表一棵完整的小子樹，把它化簡成一個 #。合法的序列最後會只剩一個 #。",
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "計算空位", [
     ("c", S["p331"]),
   ], "O(n)", "O(1)", "", "不計 split", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、堆疊化簡", "O(n)", "O(n)"],
    ["二、計算空位", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>\"#\"</strong> → 空樹，true。",
   "<strong>提早用完空位</strong>（\"#,1\"）→ false。",
   "<strong>多位數的值</strong> → 用逗號切開，不能逐字元處理。",
 ],
 "follow": [
   ("h", "相關題"),
   ("c", "第 297 題用同樣的格式真正地序列化與還原；本題只驗證格式，不需要建樹。"),
 ],
 "related": [
   "<strong>第 297 題 二元樹的序列化與反序列化</strong>",
   "<strong>第 449 題 序列化和反序列化二元搜尋樹</strong>",
 ],
 "check": [
   "「空位」一開始有幾個？每種 token 讓它怎麼變化？",
   "合法序列要滿足哪兩個條件？",
 ],
})


# ==================== 332. Reconstruct Itinerary ====================
S["p332"] = '''class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):   # 反向排序：pop() 拿到字典序最小的
            graph[a].append(b)
        route = []

        def visit(airport: str) -> None:
            while graph[airport]:
                visit(graph[airport].pop())          # 每張機票只用一次
            route.append(airport)                    # ★ 無路可走時才加入（後序）

        visit("JFK")
        return route[::-1]                           # 後序的反轉 = 歐拉路徑'''

S["p332_iter"] = '''class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        stack, route = ["JFK"], []
        while stack:
            while graph[stack[-1]]:                  # 一路往下走
                stack.append(graph[stack[-1]].pop())
            route.append(stack.pop())                # 卡住了：加入路線，退回上一站
        return route[::-1]'''

_EX = {"defaultdict": defaultdict}
_p332 = [S.load("p332", extra=_EX), S.load("p332_iter", extra=_EX)]


def _it_ref(tickets):
    best = None
    tickets = sorted(tickets)

    def go(cur, used, path):
        nonlocal best
        if best is not None:
            return
        if len(path) == len(tickets) + 1:
            best = path[:]
            return
        for i, (a, b) in enumerate(tickets):
            if not used[i] and a == cur:
                used[i] = True
                path.append(b)
                go(b, used, path)
                path.pop()
                used[i] = False
    go("JFK", [False] * len(tickets), ["JFK"])
    return best


for t, want in [([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]], ["JFK", "MUC", "LHR", "SFO", "SJC"]),
                ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]], ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]),
                ([["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]], ["JFK", "NRT", "JFK", "KUL"])]:
    for sol in _p332:
        assert sol.findItinerary([x[:] for x in t]) == want
_AP = ["JFK", "AAA", "BBB", "CCC"]
for _ in range(1500):
    path = ["JFK"] + [random.choice(_AP) for _ in range(random.randrange(1, 7))]
    tickets = [[a, b] for a, b in zip(path, path[1:]) if True]
    random.shuffle(tickets)
    want = _it_ref(tickets)
    for sol in _p332:
        assert sol.findItinerary([x[:] for x in tickets]) == want, (tickets, sol)
print("P332 OK")

_P332_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">tickets：JFK→KUL、JFK→NRT、NRT→JFK（先試字典序小的 KUL）</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="100" cy="110" r="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="100" y="115" fill="var(--accent)">JFK</text>
              <circle cx="280" cy="60" r="26" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="280" y="65" fill="#ff8a65">KUL</text>
              <circle cx="280" cy="170" r="26" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="280" y="175" fill="var(--gold)">NRT</text>
            </g>
            <g stroke="var(--text-muted)" fill="none"><path d="M124 100 L254 68"/><path d="M122 124 C 170 170, 220 180, 254 172"/><path d="M256 158 C 220 140, 160 130, 126 118"/></g>
            <g fill="var(--text-muted)"><polygon points="254,68 244,65 246,74"/><polygon points="254,172 244,168 245,177"/><polygon points="126,118 135,116 133,125"/></g>
            <text x="180" y="72" fill="var(--text-muted)" font-size="11">①</text><text x="175" y="175" fill="var(--text-muted)" font-size="11">②</text><text x="190" y="136" fill="var(--text-muted)" font-size="11">③</text>
            <g font-size="12">
              <text x="340" y="56" fill="var(--text)">走 JFK→KUL：KUL 沒有出去的票，卡住</text>
              <text x="340" y="76" fill="#ff8a65">→ KUL 放進 route（它一定是終點）</text>
              <text x="340" y="106" fill="var(--text)">回到 JFK，走 JFK→NRT→JFK</text>
              <text x="340" y="126" fill="var(--text)">JFK 沒票了 → 依序放進 route</text>
              <text x="340" y="160" fill="var(--text-muted)">route（後序）= KUL, JFK, NRT, JFK</text>
              <text x="340" y="182" fill="var(--gold)">反轉 = JFK, NRT, JFK, KUL ✔</text>
            </g>
            <text x="20" y="226" fill="var(--text)" font-size="12">★ 先走進死路也沒關係：死路的終點會先被放進 route，反轉後自然排在最後。</text>'''

emit({
 "num": 332, "slug": "reconstruct-itinerary",
 "en": [
   "You are given a list of airline <code>tickets</code> where <code>tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.",
   "All of the tickets belong to a man who departs from <code>\"JFK\"</code>, thus, the itinerary must begin with <code>\"JFK\"</code>. If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.",
   ("ul", ["For example, the itinerary <code>[\"JFK\", \"LGA\"]</code> has a smaller lexical order than <code>[\"JFK\", \"LGB\"]</code>."]),
   "You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.",
 ],
 "zh": [
   "給你一串機票 <code>tickets</code>，<code>tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]</code> 代表一趟航班的出發與抵達機場。請重建行程。",
   "所有機票都屬於一位從 <code>\"JFK\"</code> 出發的旅客，所以行程必須從 <code>\"JFK\"</code> 開始。如果有多種合法行程，回傳<strong>字典序最小</strong>的那一個。",
   "保證至少有一種合法行程。<strong>每張機票都必須恰好使用一次</strong>。",
 ],
 "examples": """範例 1
  輸入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
  輸出：["JFK","MUC","LHR","SFO","SJC"]

範例 2
  輸入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
  輸出：["JFK","ATL","JFK","SFO","ATL","SFO"]""",
 "constraints": [
   "1 ≤ <code>tickets.length</code> ≤ 300",
   "<code>from<sub>i</sub>.length == 3</code>，<code>to<sub>i</sub>.length == 3</code>，都是大寫英文字母",
   "<code>from<sub>i</sub> != to<sub>i</sub></code>",
 ],
 "idea": [
   ("c", """【每張機票恰好用一次 = 歐拉路徑】
    機場是節點，機票是有向邊。
    要找一條從 JFK 出發、每條邊恰好走一次的路徑 —— 歐拉路徑。

【貪心「每次走字典序最小的」會錯】
    JFK -> KUL、JFK -> NRT、NRT -> JFK
    貪心先走 KUL，結果 KUL 是死路，NRT 那兩張票用不到 ✘

【Hierholzer 演算法】
    DFS，每走一條邊就把它刪掉。
    當某個節點「沒有邊可走」時，才把它加入 route。
    最後把 route 反轉。

    為什麼可以？
    第一個卡住的節點一定是歐拉路徑的終點（死路）。
    之後回溯時再從別的節點繞出去的「環」，
    會在反轉後被插在正確的位置。

【字典序最小】
    每個節點的出邊排序，DFS 時先走小的。
    即使先走進死路，死路也會被放到最後，
    其他部分仍然是字典序最小的選擇。"""),
   ("fig", _P332_FIG, "0 0 640 240"),
 ],
 "approaches": [
   ap("解法一", "Hierholzer（遞迴）", [
     ("c", S["p332"]),
   ], "O(E log E)", "O(E)", "排序主導", "", optimal=True),

   ap("解法二", "Hierholzer（迭代）", [
     ("c", S["p332_iter"]),
   ], "O(E log E)", "O(E)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["回溯窮舉", "指數", "每步嘗試所有票"],
    ["一、Hierholzer 遞迴", "O(E log E)", "最短 ✔"],
    ["二、Hierholzer 迭代", "O(E log E)", "不怕深遞迴"]]),
 "edges": [
   "<strong>重複的機票</strong>（同一條航線兩張）→ 兩條平行邊，都要用。",
   "<strong>先遇到死路</strong> → 死路會被放到行程最後。",
   "<strong>用 list.pop() 取最小</strong> → 所以要反向排序；也可以用堆積。",
 ],
 "follow": [
   ("h", "歐拉路徑存在的條件"),
   ("c", "有向圖：所有節點入度 = 出度（歐拉迴路），或恰好一個節點出度比入度多 1（起點）、一個入度比出度多 1（終點），而且邊都連通。本題保證有解。第 753 題「破解保險箱」和第 2097 題也是 Hierholzer。"),
 ],
 "related": [
   "<strong>第 753 題 破解保險箱</strong> —— de Bruijn 序列 = 歐拉迴路",
   "<strong>第 2097 題 合法重新排列數對</strong>",
 ],
 "check": [
   "這一題為什麼是歐拉路徑問題？",
   "為什麼「每次走字典序最小」的貪心會錯？",
   "Hierholzer 演算法什麼時候把節點加入結果？為什麼最後要反轉？",
 ],
})


# ==================== 334. Increasing Triplet Subsequence ====================
S["p334"] = '''class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float("inf")
        # first：目前看過最小的數；second：某個「前面有更小的數」的數中，最小的
        for x in nums:
            if x <= first:
                first = x              # 更小的開頭
            elif x <= second:
                second = x             # first < x：長度 2 的遞增序列，結尾更小
            else:
                return True            # ★ first < second < x
        return False'''

_p334 = S.load("p334")
for nums, want in [([1, 2, 3, 4, 5], True), ([5, 4, 3, 2, 1], False), ([2, 1, 5, 0, 4, 6], True), ([20, 100, 10, 12, 5, 13], True), ([1, 1, 1], False)]:
    assert _p334.increasingTriplet(nums) == want
for _ in range(5000):
    nums = [random.randint(0, 6) for _ in range(random.randrange(1, 10))]
    want = any(nums[i] < nums[j] < nums[k] for i, j, k in itertools.combinations(range(len(nums)), 3))
    assert _p334.increasingTriplet(nums) == want, nums
print("P334 OK")

emit({
 "num": 334, "slug": "increasing-triplet-subsequence",
 "en": [
   "Given an integer array <code>nums</code>, return <code>true</code> <em>if there exists a triple of indices</em> <code>(i, j, k)</code> <em>such that</em> <code>i &lt; j &lt; k</code> <em>and</em> <code>nums[i] &lt; nums[j] &lt; nums[k]</code>. If no such indices exists, return <code>false</code>.",
   "<strong>Follow up:</strong> Could you implement a solution that runs in <code>O(n)</code> time complexity and <code>O(1)</code> space complexity?",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，判斷是否存在索引 <code>i &lt; j &lt; k</code> 使得 <code>nums[i] &lt; nums[j] &lt; nums[k]</code>。",
   "<strong>進階：</strong>能用 <code>O(n)</code> 時間、<code>O(1)</code> 空間嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,4,5]
  輸出：true

範例 2
  輸入：nums = [5,4,3,2,1]
  輸出：false

範例 3
  輸入：nums = [2,1,5,0,4,6]
  輸出：true
  說明：(3, 4, 5)：0 < 4 < 6""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 5 × 10⁵",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【這是「LIS 長度 >= 3」的特例】
    第 300 題的 tails 陣列只需要前兩格：
        first  = 長度 1 的遞增序列中，最小的結尾
        second = 長度 2 的遞增序列中，最小的結尾
    遇到比 second 還大的數 -> 長度 3 出現了。

【更新規則】
    x <= first          -> first = x
    first < x <= second -> second = x
    x > second          -> 找到了

【常見疑惑：first 被更新到 second 後面，不會錯嗎？】
    nums = [2, 5, 1, 6]
    讀到 1 時 first 變成 1，但 1 在 5 的後面。
    沒關係：second = 5 的意義是「存在一個比 5 小的數在 5 前面」（那個 2）。
    讀到 6 > second -> 2 < 5 < 6 確實存在 ✔
    first 的更新只是為了「未來」有機會找到更小的 second。"""),
 ],
 "approaches": [
   ap("解法", "兩個變數（LIS 的前兩格）", [
     ("c", S["p334"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>重複值</strong>（<code>[1,1,1]</code>）→ 用 <code>&lt;=</code> 讓相等的值不算遞增。",
   "<strong>長度 &lt; 3</strong> → false。",
   "<strong>first 在 second 之後被更新</strong> → 不影響正確性。",
 ],
 "follow": [
   ("h", "另一種 O(n) 做法"),
   ("c", "前綴最小值 + 後綴最大值：存在 j 使得 prefix_min[j−1] &lt; nums[j] &lt; suffix_max[j+1]。O(n) 時間但 O(n) 空間。"),
 ],
 "related": [
   "<strong>第 300 題 最長遞增子序列</strong>",
   "<strong>第 456 題 132 模式</strong>",
 ],
 "check": [
   "first 和 second 分別代表什麼？",
   "為什麼 first 被更新到 second 後面的位置，答案仍然正確？",
   "為什麼比較時要用 &lt;= 而不是 &lt;？",
 ],
})
