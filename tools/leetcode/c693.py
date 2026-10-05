# -*- coding: utf-8 -*-
"""第 693、695、696、697、698、699、700、701 題。"""
import random
from collections import Counter
from functools import lru_cache
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, bst, nodes

S = Src()
random.seed(693)


def _ino(t): return [] if t is None else _ino(t.left) + [t.val] + _ino(t.right)


# ==================== 693. Binary Number with Alternating Bits ====================
S["p693"] = '''class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n ^ (n >> 1)            # ★ 位元交替 <=> 每一位都和右邊那位不同 <=> 異或後全是 1
        return x & (x + 1) == 0     # 全是 1（形如 0b111...1）<=> 加 1 後和自己沒有共同的 1'''

_p693 = S.load("p693")
for n in range(1, 20000):
    b = bin(n)[2:]
    assert _p693.hasAlternatingBits(n) == all(b[i] != b[i + 1] for i in range(len(b) - 1))
print("P693 OK")

em({
 "num": 693, "title": "交替位元二進位數",
 "desc": "n 與 n>>1 異或後，位元交替的數會變成全 1；再用 x & (x+1) == 0 判斷全 1。",
 "zh": ["給你一個正整數，判斷它的二進位表示中，相鄰的兩個位元是否<strong>永遠不同</strong>（例如 5 = 101、10 = 1010）。"],
 "idea": [
   ("c", """【逐位檢查】
    反覆比較最低兩位，右移，O(log n)。

【位元技巧】
    n      = 1 0 1 0 1
    n >> 1 = 0 1 0 1 0
    異或   = 1 1 1 1 1   <- 交替時每一位都和右邊那位不同
    所以：交替 <=> x = n ^ (n >> 1) 是全 1。

【怎麼判斷全 1？】
    全 1 的數 x = 2^k - 1，x + 1 = 2^k，
    兩者沒有共同的 1 -> x & (x + 1) == 0。"""),
 ],
 "approaches": [
   ap("解法", "位元運算", [("c", S["p693"]), "驗證方式：1～20000 全部和逐位檢查比對。"], "O(1)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>n = 1</strong> → True。", "<strong>n = 3（11）</strong> → False。"],
 "follow": [("h", "常見位元判斷"), ("c", "x & (x − 1) == 0：x 是 2 的次方（第 231 題）；x & (x + 1) == 0：x 是全 1；x & −x：取出最低位的 1。")],
 "related": ["<strong>第 191 題 位元 1 的個數</strong>", "<strong>第 231 題 2 的冪</strong>", "<strong>第 762 題 二進位表示中質數個計算置位</strong>"],
 "check": ["n ^ (n >> 1) 在位元交替時為什麼是全 1？", "怎麼用一個運算判斷全 1？"],
})


# ==================== 695. Max Area of Island ====================
S["p695"] = '''class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def area(i, j):
            if not (0 <= i < m and 0 <= j < n) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0              # ★ 淹掉，避免重複計算
            return 1 + area(i + 1, j) + area(i - 1, j) + area(i, j + 1) + area(i, j - 1)
        return max((area(i, j) for i in range(m) for j in range(n)), default=0)'''

_p695 = S.load("p695")
for _ in range(1500):
    m, n = random.randint(1, 6), random.randint(1, 6)
    g = [[int(random.random() < 0.5) for _ in range(n)] for _ in range(m)]
    seen = set(); best = 0
    for i in range(m):
        for j in range(n):
            if g[i][j] and (i, j) not in seen:
                st = [(i, j)]; seen.add((i, j)); c = 0
                while st:
                    x, y = st.pop(); c += 1
                    for a, b in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= a < m and 0 <= b < n and g[a][b] and (a, b) not in seen:
                            seen.add((a, b)); st.append((a, b))
                best = max(best, c)
    assert _p695.maxAreaOfIsland([r[:] for r in g]) == best
print("P695 OK")

em({
 "num": 695, "title": "島嶼的最大面積",
 "desc": "第 200 題的變形：DFS 淹沒每個島嶼時順便回傳格子數，取最大。",
 "zh": ["給你一個 0/1 矩陣，1 代表陸地。<strong>島嶼</strong>由上下左右相鄰的陸地組成。回傳面積最大的島嶼面積（格子數）；沒有島嶼則回傳 0。"],
 "idea": [
   ("c", """【和第 200 題相同的 flood fill】
    遇到陸地就 DFS，把整個島嶼淹掉（設成 0）。

【DFS 回傳面積】
    area(i, j) = 1 + 四個方向的 area。
    越界或不是陸地 -> 0。"""),
 ],
 "approaches": [
   ap("解法", "DFS 淹沒並計數", [("c", S["p695"])], "O(mn)", "O(mn)", "", "遞迴深度最壞是整個矩陣", optimal=True),
 ],
 "edges": ["<strong>沒有陸地</strong> → 0。", "<strong>斜對角不算相連</strong>。", "<strong>很大的島嶼</strong> → 遞迴可能很深，可改用顯式堆疊。"],
 "follow": [("h", "島嶼系列"), ("c", "第 200 題（數量）、第 463 題（周長）、第 827 題（最多把一格 0 變 1 後的最大島嶼）、第 1905 題（子島嶼）。")],
 "related": ["<strong>第 200 題 島嶼數量</strong>", "<strong>第 463 題 島嶼的周長</strong>", "<strong>第 827 題 最大人工島</strong>"],
 "check": ["為什麼要把走過的陸地設成 0？"],
})


# ==================== 696. Count Binary Substrings ====================
S["p696"] = '''class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res, prev, cur = 0, 0, 1        # prev：上一段連續相同字元的長度；cur：目前這一段
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cur += 1
            else:
                res += min(prev, cur)   # ★ 相鄰兩段可以組成 min(兩段長度) 個合法子字串
                prev, cur = cur, 1
        return res + min(prev, cur)'''

_p696 = S.load("p696")
for _ in range(3000):
    s = "".join(random.choice("01") for _ in range(random.randint(1, 12)))
    want = 0
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1, 2):
            t = s[i:j]; h = len(t) // 2
            if len(set(t[:h])) == 1 and len(set(t[h:])) == 1 and t[0] != t[-1]: want += 1
    assert _p696.countBinarySubstrings(s) == want
print("P696 OK")

em({
 "num": 696, "title": "計數二進位子字串",
 "desc": "把字串切成連續相同字元的段落，相鄰兩段可以貢獻 min(長度) 個合法子字串。",
 "zh": [
   "給你一個二進位字串 <code>s</code>，計算有多少個非空子字串滿足：0 和 1 的數量相同，而且所有 0 是連在一起的、所有 1 也是連在一起的（例如 <code>\"0011\"</code>、<code>\"10\"</code>）。",
   "重複出現的子字串要依出現次數分別計算。",
 ],
 "idea": [
   ("c", """【合法的子字串長什麼樣？】
    一段 0 後面接一段等長的 1（或反過來），而且一定跨越一個「0/1 交界」。

【依段落思考】
    s = 00111011 -> 段落長度 [2, 3, 1, 2]
    相鄰兩段（長度 a, b）跨越它們之間的交界：
        可以取 01、0011、... 最多 min(a, b) 種。
    答案 = Σ min(相鄰兩段長度)。

【一趟掃描】
    只要記住上一段與目前這一段的長度。"""),
 ],
 "approaches": [
   ap("解法", "相鄰段落長度", [("c", S["p696"]), "驗證方式：和枚舉所有子字串的暴力法比對 3000 組。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>全部相同</strong> → 0。", "<strong>\"10101\"</strong> → 4。"],
 "follow": [("h", "段落壓縮（run-length）"), ("c", "把字串壓成 (字元, 長度) 的段落，很多字串題會變簡單：第 443 題（壓縮字串）、第 1446 題（連續字元）。")],
 "related": ["<strong>第 443 題 壓縮字串</strong>", "<strong>第 647 題 迴文子字串</strong>"],
 "check": ["為什麼相鄰兩段的貢獻是 min(a, b)？"],
})


# ==================== 697. Degree of an Array ====================
S["p697"] = '''class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first, last, cnt = {}, {}, Counter()
        for i, x in enumerate(nums):
            first.setdefault(x, i)
            last[x] = i
            cnt[x] += 1
        deg = max(cnt.values())
        # ★ 包含某個眾數「所有」出現位置的最短子陣列 = 從它第一次到最後一次
        return min(last[x] - first[x] + 1 for x in cnt if cnt[x] == deg)'''

_p697 = S.load("p697")
for _ in range(2000):
    a = [random.randint(0, 4) for _ in range(random.randint(1, 9))]
    deg = max(Counter(a).values())
    want = min(j - i for i in range(len(a)) for j in range(i + 1, len(a) + 1) if max(Counter(a[i:j]).values()) == deg)
    assert _p697.findShortestSubArray(a) == want
print("P697 OK")

em({
 "num": 697, "title": "陣列的度",
 "desc": "陣列的度由眾數決定；子陣列要保持同樣的度，必須包含某個眾數的所有出現位置，所以記第一次與最後一次出現。",
 "zh": [
   "陣列的<strong>度</strong>是其中任一元素出現次數的最大值。",
   "給你非空整數陣列 <code>nums</code>，找出與 <code>nums</code> 有<strong>相同度</strong>的最短連續子陣列，回傳它的長度。",
 ],
 "idea": [
   ("c", """【度 = 眾數的出現次數 deg】

【子陣列的度也要是 deg】
    子陣列中某個元素要出現 deg 次 ->
    它必須是原陣列的眾數，而且子陣列包含它的「全部」出現位置。
    最短的就是從第一次出現到最後一次出現。

【答案】
    所有眾數 x 中，last[x] - first[x] + 1 的最小值。"""),
 ],
 "approaches": [
   ap("解法", "記錄第一次、最後一次與次數", [("c", S["p697"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>多個眾數</strong> → 取跨度最小的。", "<strong>所有元素都不同</strong> → 1。"],
 "follow": [("h", "一趟完成"), ("c", "也可以在掃描時同時更新：次數變大就更新度與答案，次數相同就比較長度。")],
 "related": ["<strong>第 1 題 兩數之和</strong>", "<strong>第 169 題 多數元素</strong>"],
 "check": ["為什麼子陣列必須包含眾數的所有出現位置？"],
})


# ==================== 698. Partition to K Equal Sum Subsets ====================
S["p698"] = '''class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        nums.sort(reverse=True)                 # 大的先放：越早失敗越好剪枝
        if nums[0] > target:
            return False
        n = len(nums)

        @cache
        def dfs(mask, cur):                     # mask：已使用的數；cur：目前這個桶的和
            if mask == (1 << n) - 1:
                return True
            for i in range(n):
                if not mask >> i & 1 and cur + nums[i] <= target:
                    # ★ 桶剛好裝滿時歸零，開始填下一個桶
                    if dfs(mask | 1 << i, (cur + nums[i]) % target):
                        return True
            return False
        return dfs(0, 0)'''

_p698 = S.load("p698")
assert _p698.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4) and not _p698.canPartitionKSubsets([1, 2, 3, 4], 3)
from itertools import product as _prod
for _ in range(500):
    a = [random.randint(1, 6) for _ in range(random.randint(1, 7))]; k = random.randint(1, 4)
    want = any(len(set(sum(x for x, g in zip(a, assign) if g == b) for b in range(k))) == 1 for assign in _prod(range(k), repeat=len(a)))
    _p698 = S.load("p698")
    assert _p698.canPartitionKSubsets(a[:], k) == want, (a, k)
print("P698 OK")

em({
 "num": 698, "title": "劃分為 k 個相等的子集",
 "desc": "一個桶一個桶地填：狀態是「用過哪些數」，目前桶的和可由 mask 推出，所以可以用位元遮罩記憶化。",
 "zh": ["給你整數陣列 <code>nums</code> 和正整數 <code>k</code>，判斷能否把陣列分成 <code>k</code> 個<strong>非空</strong>子集，使每個子集的總和都相等。"],
 "idea": [
   ("c", """【先排除】
    總和不能被 k 整除 -> False。
    最大的數 > target -> False。

【一個桶一個桶地填】
    依序填滿第 1 個桶（和為 target）、第 2 個……
    填滿時 cur 歸零（用 % target）。

【狀態只需要 mask】
    已用的數決定了已用的總和 S，
    目前這個桶的和 = S % target —— 也由 mask 決定。
    所以 dfs(mask) 可以記憶化，2ⁿ 個狀態，n <= 16。

【剪枝】
    由大到小排序：大的數比較難放，早點失敗。"""),
 ],
 "approaches": [
   ap("解法", "位元遮罩記憶化搜尋", [("c", S["p698"]), "驗證方式：和枚舉每個數分到哪一組的暴力法比對 500 組。"], "O(n · 2ⁿ)", "O(2ⁿ)", optimal=True),
 ],
 "edges": ["<strong>k = 1</strong> → True。", "<strong>某個數大於 target</strong> → False。", "<strong>總和不整除</strong> → False。"],
 "follow": [("h", "k = 2 的特例"), ("c", "第 416 題（分割等和子集）：k = 2 時只要找一個和為 total/2 的子集，用 0/1 背包 O(n·sum)。")],
 "related": ["<strong>第 416 題 分割等和子集</strong>", "<strong>第 473 題 火柴拼正方形</strong>", "<strong>第 2305 題 公平分發餅乾</strong>"],
 "check": ["為什麼目前桶的和可以由 mask 推出？", "為什麼要由大到小排序？"],
})


# ==================== 699. Falling Squares ====================
S["p699"] = '''class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        placed = []                             # 已落下的方塊：(左, 右, 頂端高度)
        res, best = [], 0
        for left, size in positions:
            right = left + size                 # 佔據 [left, right)
            base = 0
            for l, r, h in placed:
                if l < right and left < r:      # ★ 區間有重疊（只碰到邊不算）
                    base = max(base, h)
            top = base + size
            placed.append((left, right, top))
            best = max(best, top)
            res.append(best)
        return res'''

_p699 = S.load("p699")
assert _p699.fallingSquares([[1, 2], [2, 3], [6, 1]]) == [2, 5, 5]
assert _p699.fallingSquares([[100, 100], [200, 100]]) == [100, 100]
for _ in range(1000):
    pos = [[random.randint(0, 10), random.randint(1, 4)] for _ in range(random.randint(1, 7))]
    h = [0] * 20; out = []; best = 0
    for l, s in pos:
        b = max(h[l:l + s]);
        for x in range(l, l + s): h[x] = b + s
        best = max(best, b + s); out.append(best)
    assert _p699.fallingSquares(pos) == out
print("P699 OK")

em({
 "num": 699, "title": "掉落的方塊",
 "desc": "每個新方塊落在與它重疊的已落方塊中最高的那個上面；n ≤ 1000 時 O(n²) 即可，進階可用座標壓縮 + 線段樹。",
 "zh": [
   "在數線上依序丟下一些正方形方塊。<code>positions[i] = [left, sideLength]</code>：第 i 個方塊的左邊在 x = left，邊長為 sideLength。",
   "方塊從很高的地方垂直落下，直到碰到地面或另一個方塊的<strong>頂面</strong>（只碰到側邊不算）就停住。每落下一個方塊後，記錄目前所有方塊堆的<strong>最高高度</strong>，回傳這些高度。",
 ],
 "idea": [
   ("c", """【一個方塊會停在哪裡？】
    它佔據 [left, left+size)。
    和它水平重疊的已落方塊中，頂端最高的那個 -> 它的底部高度 base。
    新頂端 = base + size。

【重疊判斷】
    [l1, r1) 和 [l2, r2) 重疊 <=> l1 < r2 且 l2 < r1。
    只碰到邊緣（r1 == l2）不算。

【O(n²)】
    n <= 1000，每個方塊和之前所有方塊比較即可。

【O(n log n)】
    座標壓縮後用線段樹：
        區間查詢最大值（base）、區間賦值（新高度）。"""),
 ],
 "approaches": [
   ap("解法一", "逐一比較", [("c", S["p699"]), "驗證方式：在小座標範圍內和「逐格維護高度陣列」的模擬比對 1000 組。"], "O(n²)", "O(n)"),
   ap("解法二", "座標壓縮 + 線段樹", [("c", "收集所有 left 與 left+size 並排序去重\n線段樹支援：區間最大值查詢、區間賦值（懶標記）\n每個方塊：base = query(l, r-1)；update(l, r-1, base + size)")], "O(n log n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>只碰到邊緣</strong> → 不算疊上去。", "<strong>完全不重疊</strong> → 落在地面。", "<strong>答案是目前的最高高度</strong>，不是這個方塊的高度。"],
 "follow": [("h", "區間賦值線段樹"), ("c", "第 715 題（Range 模組）、第 732 題（我的日程安排表 III）也是座標很大、需要動態開點或座標壓縮的線段樹題。")],
 "related": ["<strong>第 715 題 Range 模組</strong>", "<strong>第 218 題 天際線問題</strong>", "<strong>第 732 題 我的日程安排表 III</strong>"],
 "check": ["兩個左閉右開區間重疊的條件是什麼？", "新方塊的底部高度怎麼決定？"],
})


# ==================== 700. Search in a Binary Search Tree ====================
S["p700"] = '''class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root and root.val != val:
            root = root.left if val < root.val else root.right    # ★ 每一步排除一半的子樹
        return root'''

_p700 = S.load("p700")
for _ in range(2000):
    vals = random.sample(range(30), random.randint(1, 10)); t = bst(vals); v = random.randint(0, 30)
    r = _p700.searchBST(t, v)
    assert (r is not None and r.val == v and _ino(r) == sorted(x for x in _ino(r))) if v in vals else r is None
print("P700 OK")

em({
 "num": 700, "title": "二元搜尋樹中的搜尋",
 "desc": "BST 的基本操作：比節點小往左、大往右，O(h)。",
 "zh": ["給你一棵二元搜尋樹的根節點和整數 <code>val</code>，找到值等於 <code>val</code> 的節點並回傳以它為根的子樹；不存在則回傳 <code>null</code>。"],
 "idea": [
   ("c", """【BST 的性質】
    左子樹全部 < 節點 < 右子樹全部。
    val < 節點 -> 只可能在左子樹
    val > 節點 -> 只可能在右子樹

    迭代寫法不需要遞迴堆疊，O(1) 額外空間。"""),
 ],
 "approaches": [
   ap("解法", "迭代搜尋", [("c", S["p700"])], "O(h)", "O(1)", "h 為樹高；平衡時 O(log n)，退化成鏈時 O(n)", "", optimal=True),
 ],
 "edges": ["<strong>找不到</strong> → None。", "<strong>樹退化成鏈</strong> → O(n)。"],
 "follow": [("h", "BST 的三個基本操作"), ("c", "搜尋（本題）、插入（第 701 題）、刪除（第 450 題）。平衡 BST（AVL、紅黑樹）保證 h = O(log n)。")],
 "related": ["<strong>第 701 題 二元搜尋樹中的插入操作</strong>", "<strong>第 450 題 刪除二元搜尋樹中的節點</strong>"],
 "check": ["為什麼每一步可以排除一整棵子樹？"],
})


# ==================== 701. Insert into a Binary Search Tree ====================
S["p701"] = '''class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        nd = root
        while True:
            if val < nd.val:
                if not nd.left:
                    nd.left = TreeNode(val)     # ★ 找到空位就放進去：新節點一定是葉子
                    return root
                nd = nd.left
            else:
                if not nd.right:
                    nd.right = TreeNode(val)
                    return root
                nd = nd.right'''

_p701 = S.load("p701")
for _ in range(2000):
    vals = random.sample(range(30), random.randint(0, 10)); t = bst(vals)
    v = random.choice([x for x in range(30) if x not in vals])
    r = _p701.insertIntoBST(t, v)
    assert _ino(r) == sorted(vals + [v])
print("P701 OK")

em({
 "num": 701, "title": "二元搜尋樹中的插入操作",
 "desc": "像搜尋一樣往下走，走到空位就放新節點——新節點永遠是葉子，原本的結構完全不動。",
 "zh": [
   "給你一棵二元搜尋樹的根節點和一個值 <code>val</code>（保證不在樹中），把它插入 BST，回傳插入後的根節點。",
   "可能有多種合法的插入方式，回傳任意一種即可。",
 ],
 "idea": [
   ("c", """【最簡單的插入：當成葉子】
    像搜尋 val 一樣往下走：小往左、大往右。
    走到空的位置 -> val 本來應該在這裡 -> 放一個新節點。
    不需要調整任何既有的節點。

【空樹】
    新節點就是根。"""),
 ],
 "approaches": [
   ap("解法", "迭代找到空位", [("c", S["p701"]), "驗證方式：插入後中序走訪必須是排序好的全部值。"], "O(h)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>空樹</strong> → 回傳新節點。", "<strong>插入後樹可能不平衡</strong> → 題目不要求平衡。"],
 "follow": [("h", "保持平衡"), ("c", "一直插入遞增的值會讓樹退化成鏈。AVL 樹、紅黑樹在插入後用旋轉恢復平衡；Python 沒有內建平衡 BST，常用 sortedcontainers.SortedList 代替。")],
 "related": ["<strong>第 700 題 二元搜尋樹中的搜尋</strong>", "<strong>第 450 題 刪除二元搜尋樹中的節點</strong>"],
 "check": ["為什麼新節點一定可以放在葉子的位置？"],
})
