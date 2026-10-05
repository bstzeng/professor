# -*- coding: utf-8 -*-
"""第 667、668、669、670、671、672、673、674 題。"""
import random
from itertools import permutations, product
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, nodes, bst

S = Src()
random.seed(667)


# ==================== 667. Beautiful Arrangement II ====================
S["p667"] = '''class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, n - k))             # 前面 1..n-k-1 遞增排列，相鄰差都是 1
        lo, hi = n - k, n
        while lo <= hi:                         # ★ 剩下的 k+1 個數「一小一大」交錯：差為 k, k-1, ..., 1
            res.append(lo)
            lo += 1
            if lo <= hi:
                res.append(hi)
                hi -= 1
        return res'''

_p667 = S.load("p667")
for n in range(2, 40):
    for k in range(1, n):
        a = _p667.constructArray(n, k)
        assert sorted(a) == list(range(1, n + 1)) and len({abs(a[i] - a[i + 1]) for i in range(n - 1)}) == k
print("P667 OK")

em({
 "num": 667, "title": "優美的排列 II",
 "desc": "構造：前面遞增貢獻差值 1，最後 k+1 個數「一小一大」交錯排列，產生差 k, k−1, …, 1。",
 "zh": ["給你兩個整數 <code>n</code> 和 <code>k</code>，構造一個由 1 到 <code>n</code> 組成的排列，使得相鄰兩數之差的絕對值<strong>恰好有 k 種不同的值</strong>。有多種答案時回傳任意一種。"],
 "idea": [
   ("c", """【怎麼得到 k 種差值？】
    1, k+1, 2, k, 3, k-1, ...
    差依序是 k, k-1, k-2, ..., 1 —— 恰好 k 種。
    這需要 k+1 個數。

【其他數怎麼放？】
    剩下的數放在前面，遞增排列：差都是 1，
    1 已經在上面的 k 種裡，不會增加新的差值。

【具體】
    前面：1, 2, ..., n-k-1
    後面：n-k, n, n-k+1, n-1, ...（一小一大交錯）
    銜接處 n-k-1 -> n-k 的差也是 1。"""),
 ],
 "approaches": [
   ap("解法", "構造", [("c", S["p667"]), "驗證方式：n < 40 的所有 (n, k) 都檢查排列合法且差值種數恰為 k。"], "O(n)", "O(1)", "", "不計輸出", optimal=True),
 ],
 "edges": ["<strong>k = 1</strong> → 1, 2, ..., n。", "<strong>k = n − 1</strong> → 全部一小一大交錯。"],
 "follow": [("h", "構造題的思路"), ("c", "先找一個「恰好產生所需數量」的小結構（這裡是交錯排列），再把剩下的東西用「不增加新東西」的方式放進去。")],
 "related": ["<strong>第 526 題 優美的排列</strong>", "<strong>第 932 題 漂亮陣列</strong>"],
 "check": ["交錯排列 1, k+1, 2, k, ... 的相鄰差是什麼？", "前面遞增的部分為什麼不會增加新的差值？"],
})


# ==================== 668. Kth Smallest Number in Multiplication Table ====================
S["p668"] = '''class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        lo, hi = 1, m * n
        while lo < hi:                          # 二分答案：找最小的 x，使得「<= x 的個數」>= k
            x = (lo + hi) // 2
            # ★ 第 i 列是 i, 2i, ..., ni：其中 <= x 的有 min(x // i, n) 個
            cnt = sum(min(x // i, n) for i in range(1, m + 1))
            if cnt >= k:
                hi = x
            else:
                lo = x + 1
        return lo'''

_p668 = S.load("p668")
for _ in range(1500):
    m, n = random.randint(1, 8), random.randint(1, 8); k = random.randint(1, m * n)
    assert _p668.findKthNumber(m, n, k) == sorted(i * j for i in range(1, m + 1) for j in range(1, n + 1))[k - 1]
print("P668 OK")

em({
 "num": 668, "title": "乘法表中第 k 小的數",
 "desc": "對答案二分：「≤ x 的數有幾個」可以逐列 O(1) 計算，找最小的 x 使個數 ≥ k。",
 "zh": ["乘法表是一個 <code>m x n</code> 的矩陣，<code>mat[i][j] = i × j</code>（索引從 1 開始）。給你 <code>m</code>、<code>n</code>、<code>k</code>，回傳乘法表中<strong>第 k 小</strong>的數。"],
 "idea": [
   ("c", """【表太大，不能列出來】
    m, n 可達 3×10⁴，共 9×10⁸ 個數。

【二分答案】
    f(x) = 乘法表中 <= x 的數有幾個，隨 x 單調不減。
    第 k 小的數 = 最小的 x 使 f(x) >= k。

【f(x) 怎麼算？】
    第 i 列是 i, 2i, 3i, ..., ni。
    其中 <= x 的有 min(x // i, n) 個。
    加總 m 列 -> O(m)。

【為什麼二分結果一定在表中？】
    最小的滿足 f(x) >= k 的 x，若不在表中，
    則 f(x-1) = f(x) >= k，和「最小」矛盾。"""),
 ],
 "approaches": [
   ap("解法", "二分答案 + 逐列計數", [("c", S["p668"]), "驗證方式：和列出整張表排序比對 1500 組。"], "O(m log(mn))", "O(1)", optimal=True),
 ],
 "edges": ["<strong>k = 1</strong> → 1。", "<strong>k = mn</strong> → mn。", "<strong>重複的數</strong>（如 2×3 和 3×2）→ 分別計數。"],
 "follow": [("h", "二分答案家族"), ("c", "「第 k 小」+「計算 ≤ x 的個數很容易」：第 378 題（有序矩陣中第 K 小）、第 719 題（第 K 小的數對距離）、第 786 題（第 K 個最小的質數分數）。")],
 "related": ["<strong>第 378 題 有序矩陣中第 K 小的元素</strong>", "<strong>第 719 題 找出第 K 小的數對距離</strong>"],
 "check": ["第 i 列中 ≤ x 的數有幾個？", "為什麼二分得到的 x 一定出現在乘法表中？"],
})


# ==================== 669. Trim a Binary Search Tree ====================
S["p669"] = '''class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)      # ★ 根太小：它和整個左子樹都不要
        if root.val > high:
            return self.trimBST(root.left, low, high)       # 根太大：它和整個右子樹都不要
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root'''

_p669 = S.load("p669")
def _ino(t): return [] if t is None else _ino(t.left) + [t.val] + _ino(t.right)
def _isbst(t, lo=-10 ** 9, hi=10 ** 9):
    return t is None or (lo < t.val < hi and _isbst(t.left, lo, t.val) and _isbst(t.right, t.val, hi))
for _ in range(2000):
    vals = random.sample(range(20), random.randint(1, 10)); lo = random.randint(0, 19); hi = random.randint(lo, 19)
    r = _p669.trimBST(bst(vals), lo, hi)
    assert _ino(r) == sorted(v for v in vals if lo <= v <= hi) and _isbst(r)
print("P669 OK")

em({
 "num": 669, "title": "修剪二元搜尋樹",
 "desc": "根小於 low 時連同左子樹整個丟掉、只看右子樹；大於 high 時同理；否則遞迴修剪兩邊。",
 "zh": [
   "給你一棵二元搜尋樹和邊界 <code>low</code>、<code>high</code>，修剪這棵樹，使所有節點值都落在 <code>[low, high]</code> 內。",
   "修剪不能改變留下來節點的相對結構（原本是父子關係的仍是祖先後代關係）。回傳修剪後的根（可能會改變）。",
 ],
 "idea": [
   ("c", """【利用 BST 性質】
    root.val < low：
        root 的左子樹都比 root 小 -> 也都 < low，全部丟掉。
        答案只可能在右子樹 -> 回傳 trim(root.right)。
    root.val > high：對稱，回傳 trim(root.left)。
    否則 root 保留，左右各自遞迴修剪。

    被丟掉的節點的「合法後代」會被接到它原本的父節點上，
    相對結構不變。"""),
 ],
 "approaches": [
   ap("解法", "遞迴", [("c", S["p669"]), "驗證方式：檢查結果的中序走訪等於原值中落在範圍內的排序結果，而且仍是 BST。"], "O(n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>根被剪掉</strong> → 回傳的新根是某個後代。", "<strong>全部被剪掉</strong> → None。"],
 "follow": [("h", "迭代寫法"), ("c", "先往下找到第一個在範圍內的節點當新根；再分別沿著左邊與右邊的鏈修剪：左邊遇到 < low 的就用它的右孩子取代它。O(1) 額外空間。")],
 "related": ["<strong>第 450 題 刪除二元搜尋樹中的節點</strong>", "<strong>第 938 題 二元搜尋樹的範圍和</strong>"],
 "check": ["root.val < low 時，為什麼整個左子樹都可以丟掉？"],
})


# ==================== 670. Maximum Swap ====================
S["p670"] = '''class Solution:
    def maximumSwap(self, num: int) -> int:
        d = list(str(num))
        last = {int(c): i for i, c in enumerate(d)}         # 每個數字最後出現的位置
        for i, c in enumerate(d):
            for big in range(9, int(c), -1):                # ★ 從 9 往下找比 d[i] 大、而且在後面的數字
                if last.get(big, -1) > i:
                    j = last[big]                           # 選最後一個，換過來後較小的數字放在最右邊
                    d[i], d[j] = d[j], d[i]
                    return int("".join(d))
        return num'''

_p670 = S.load("p670")
for _ in range(3000):
    x = random.randint(0, 10 ** random.randint(1, 7)); s = list(str(x)); best = x
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            t = s[:]; t[i], t[j] = t[j], t[i]; best = max(best, int("".join(t)))
    assert _p670.maximumSwap(x) == best
print("P670 OK")

em({
 "num": 670, "title": "最大交換",
 "desc": "從左往右找第一個「後面有更大數字」的位置，和後面最大數字的最後一次出現交換。",
 "zh": ["給你一個非負整數 <code>num</code>，最多交換其中兩位數字一次，回傳能得到的<strong>最大值</strong>。"],
 "idea": [
   ("c", """【貪心】
    越高位越重要：從左往右找第一個「可以變大」的位置 i。
    可以變大 <=> 後面有比 d[i] 大的數字。

【換成誰？】
    後面最大的數字 big。
    若 big 出現多次，選「最後一次」出現的位置：
    被換到後面的 d[i] 比較小，放在越低位越好。
    例：1993 -> 換第一個 1 和最後一個 9 -> 9913（而不是 9193）。

【實作】
    last[數字] = 最後出現的位置。
    對每個 i，從 9 往下試到 d[i]+1，找到在 i 後面的就換。"""),
 ],
 "approaches": [
   ap("解法", "貪心 + 最後出現位置", [("c", S["p670"]), "驗證方式：和枚舉所有交換的暴力法比對 3000 個數。"], "O(位數 · 10)", "O(10)", optimal=True),
 ],
 "edges": ["<strong>已經是非遞增</strong>（如 9973）→ 不交換。", "<strong>重複的最大數字</strong> → 換最後一個。", "<strong>單一位數</strong> → 不變。"],
 "follow": [("h", "相關"), ("c", "第 556 題（下一個更大元素 III）是「比 n 大的最小排列」；本題限制只能交換一次，求最大。")],
 "related": ["<strong>第 556 題 下一個更大元素 III</strong>", "<strong>第 31 題 下一個排列</strong>", "<strong>第 738 題 單調遞增的數字</strong>"],
 "check": ["為什麼要找最左邊可以變大的位置？", "最大數字重複時為什麼選最後一個？"],
})


# ==================== 671. Second Minimum Node In a Binary Tree ====================
S["p671"] = '''class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        first = root.val                        # ★ 根一定是最小值（每個節點 = 兩個孩子的較小者）
        def dfs(nd):
            if not nd:
                return -1
            if nd.val > first:
                return nd.val                   # 比最小值大：這棵子樹裡它就是最小的，不用再往下
            l, r = dfs(nd.left), dfs(nd.right)
            if l == -1 or r == -1:
                return max(l, r)
            return min(l, r)
        return dfs(root)'''

_p671 = S.load("p671")
from runner import TreeNode
def _special(depth):
    if depth == 0 or random.random() < 0.3:
        return TreeNode(random.randint(1, 5))
    l, r = _special(depth - 1), _special(depth - 1)
    return TreeNode(min(l.val, r.val), l, r)
for _ in range(2000):
    t = _special(random.randint(0, 4))
    vals = sorted({n.val for n in nodes(t)})
    assert _p671.findSecondMinimumValue(t) == (vals[1] if len(vals) > 1 else -1)
print("P671 OK")

em({
 "num": 671, "title": "二元樹中第二小的節點",
 "desc": "根一定是最小值；DFS 時遇到比根大的節點就不必往下（它是那棵子樹中最小的），取這些候選的最小值。",
 "zh": [
   "給你一棵特殊的二元樹：每個節點的孩子數是 0 或 2；若有兩個孩子，節點值等於兩個孩子值中的<strong>較小者</strong>。",
   "回傳樹中所有<strong>不同</strong>值中第二小的值；不存在則回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【性質：每個節點都是子樹中的最小值】
    所以根是全樹最小值 first。

【找比 first 大的最小值】
    DFS：
        nd.val > first -> 它是這棵子樹中最小的值，
                         也就是這棵子樹中「比 first 大」的最小候選，直接回傳。
        nd.val == first -> 答案可能在兩邊，兩邊都找，取存在的較小值。

    剪枝讓很多子樹不用走到底。"""),
 ],
 "approaches": [
   ap("解法", "DFS + 剪枝", [("c", S["p671"]), "驗證方式：隨機產生符合題目性質的樹，和「收集所有不同值排序取第二個」比對。"], "O(n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>所有值都相同</strong> → −1。", "<strong>只有根</strong> → −1。"],
 "follow": [("h", "這種樹是什麼？"), ("c", "每個節點是孩子的最小值——這是「錦標賽樹」（tournament tree）：葉子是參賽者，每個內部節點是那場比賽的勝者，根是冠軍。找第二名只需要看和冠軍比過的對手。")],
 "related": ["<strong>第 230 題 二元搜尋樹中第 K 小的元素</strong>"],
 "check": ["為什麼根一定是最小值？", "遇到比根大的節點為什麼可以不往下走？"],
})


# ==================== 672. Bulb Switcher II ====================
S["p672"] = '''class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        n = min(n, 3)                           # ★ 燈的狀態以 6 為週期，而且前 3 盞就能決定全部
        if presses == 0:
            return 1
        if presses == 1:
            return [2, 3, 4][n - 1]
        if presses == 2:
            return [2, 4, 7][n - 1]
        return [2, 4, 8][n - 1]'''

_p672 = S.load("p672")
def _bf672(n, p):
    res = set()
    for combo in product(range(2), repeat=4):           # 每個按鈕按奇數或偶數次
        k = sum(combo)
        if k > p or (p - k) % 2: continue
        st = []
        for i in range(1, n + 1):
            on = 1
            if combo[0]: on ^= 1
            if combo[1] and i % 2 == 0: on ^= 1
            if combo[2] and i % 2 == 1: on ^= 1
            if combo[3] and i % 3 == 1: on ^= 1
            st.append(on)
        res.add(tuple(st))
    return len(res)
for n in range(1, 13):
    for p in range(0, 7):
        assert _p672.flipLights(n, p) == _bf672(n, p), (n, p)
print("P672 OK")

em({
 "num": 672, "title": "燈泡開關 II",
 "desc": "每個按鈕只看按奇數或偶數次（共 16 種），且前 3 盞燈就決定所有燈的狀態——答案只有少數幾種，可以列表。",
 "zh": [
   "房間裡有 <code>n</code> 盞燈（編號 1～n），一開始全亮。有四個按鈕：",
   ("ol", ["翻轉<strong>所有</strong>燈。", "翻轉編號為<strong>偶數</strong>的燈。", "翻轉編號為<strong>奇數</strong>的燈。", "翻轉編號為 <code>3k + 1</code> 的燈（1, 4, 7, …）。"]),
   "恰好按 <code>presses</code> 次按鈕（每次任選一個）後，回傳燈的狀態可能有<strong>幾種不同情形</strong>。",
 ],
 "idea": [
   ("c", """【每個按鈕只在乎按了奇數次還是偶數次】
    翻兩次等於沒翻。所以只有 2⁴ = 16 種組合。
    組合的按鈕數 k 要滿足 k <= presses 且 (presses - k) 是偶數
    （多出來的次數可以兩兩抵消）。

【燈的狀態有週期】
    四個按鈕的週期是 1、2、2、3 -> 整體週期 6。
    再細看：燈 4 = 燈 1 ⊕ 燈 2 ⊕ 燈 3（可以驗證），
    燈 5、6 也能由前 3 盞推出 ->
    只看前 min(n, 3) 盞就夠了。

【結果只有幾種】
    n=1：presses>=1 時 2 種
    n=2：presses=1 時 3 種，>=2 時 4 種
    n>=3：presses=1：4 種；presses=2：7 種；>=3：8 種"""),
 ],
 "approaches": [
   ap("解法", "分析後列表", [("c", S["p672"]), "驗證方式：n ≤ 12、presses ≤ 6 的所有組合，和「枚舉 16 種奇偶組合實際模擬」比對。"], "O(1)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>presses = 0</strong> → 1。", "<strong>n = 1</strong> → 最多 2 種。", "<strong>presses = 2、n ≥ 3</strong> → 7（缺了某一種需要三個按鈕才能做到的狀態）。"],
 "follow": [("h", "如果不想背表？"), ("c", "直接用暴力法：枚舉 16 種奇偶組合，模擬前 min(n, 6) 盞燈的狀態，用集合去重。仍然是 O(1)，而且不容易出錯。")],
 "related": ["<strong>第 319 題 燈泡開關</strong>", "<strong>第 1375 題 二進位字串前綴一致的次數</strong>"],
 "check": ["為什麼每個按鈕只要考慮奇偶？", "為什麼前 3 盞燈就能決定所有燈？"],
})


# ==================== 673. Number of Longest Increasing Subsequence ====================
S["p673"] = '''class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n            # length[i]：以 i 結尾的 LIS 長度
        count = [1] * n             # count[i]：達到這個長度的方法數
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]             # ★ 找到更長的：方法數重新計算
                    elif length[j] + 1 == length[i]:
                        count[i] += count[j]            # 一樣長：方法數累加
        best = max(length)
        return sum(c for l, c in zip(length, count) if l == best)'''

_p673 = S.load("p673")
from itertools import combinations
for _ in range(1500):
    a = [random.randint(0, 5) for _ in range(random.randint(1, 9))]
    best = 0; cnt = 0
    for r in range(1, len(a) + 1):
        for idx in combinations(range(len(a)), r):
            if all(a[idx[i]] < a[idx[i + 1]] for i in range(r - 1)):
                if r > best: best, cnt = r, 1
                elif r == best: cnt += 1
    assert _p673.findNumberOfLIS(a) == cnt
print("P673 OK")

em({
 "num": 673, "title": "最長遞增子序列的個數",
 "desc": "LIS 的 O(n²) DP 再多記一個「方法數」：更長時重設、一樣長時累加。",
 "zh": ["給你整數陣列 <code>nums</code>，回傳<strong>最長嚴格遞增子序列</strong>的個數（不同位置的子序列分開計算）。"],
 "idea": [
   ("c", """【第 300 題的 DP】
    length[i] = 以 nums[i] 結尾的 LIS 長度
             = 1 + max(length[j])，j < i 且 nums[j] < nums[i]

【多記一個 count[i]】
    count[i] = 以 nums[i] 結尾、長度為 length[i] 的子序列個數。
    對每個 j：
        length[j] + 1 > length[i]  -> 找到更長的，count[i] = count[j]
        length[j] + 1 == length[i] -> 又一種方法，count[i] += count[j]

【答案】
    所有 length[i] == 最大長度 的 count[i] 加總。"""),
 ],
 "approaches": [
   ap("解法", "LIS DP + 方法數", [("c", S["p673"]), "驗證方式：和枚舉所有子序列的暴力法比對 1500 組。"], "O(n²)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>全部相同</strong> → n（每個單獨的元素都是長度 1 的 LIS）。", "<strong>嚴格遞增</strong> → 相等不能接。"],
 "follow": [("h", "O(n log n)"), ("c", "對每個長度維護「結尾值 → 累積方法數」的有序結構，用二分加前綴和查詢可以做到 O(n log n)，或用樹狀陣列/線段樹（以值為索引，存 (最長長度, 方法數)）。")],
 "related": ["<strong>第 300 題 最長遞增子序列</strong>", "<strong>第 674 題 最長連續遞增序列</strong>", "<strong>第 354 題 俄羅斯套娃信封問題</strong>"],
 "check": ["找到更長的子序列時 count 要怎麼更新？", "最後答案為什麼要加總多個位置？"],
})


# ==================== 674. Longest Continuous Increasing Subsequence ====================
S["p674"] = '''class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = cur = 1
        for i in range(1, len(nums)):
            cur = cur + 1 if nums[i] > nums[i - 1] else 1   # ★ 遞增就延長，否則重新開始
            res = max(res, cur)
        return res'''

_p674 = S.load("p674")
for _ in range(2000):
    a = [random.randint(0, 5) for _ in range(random.randint(1, 10))]
    want = max(j - i for i in range(len(a)) for j in range(i + 1, len(a) + 1) if all(a[k] < a[k + 1] for k in range(i, j - 1)))
    assert _p674.findLengthOfLCIS(a) == want
print("P674 OK")

em({
 "num": 674, "title": "最長連續遞增序列",
 "desc": "要求連續：一趟掃描，遞增就延長目前長度，否則重設為 1。",
 "zh": ["給你一個未排序的整數陣列，找出<strong>最長且連續</strong>的嚴格遞增子陣列，回傳它的長度。"],
 "idea": [
   ("c", """【連續 -> 不需要 DP】
    cur = 以目前位置結尾的連續遞增長度。
    nums[i] > nums[i-1] -> cur + 1
    否則 -> 從 1 重新開始

    對照第 300 題：不要求連續（子序列）就需要 DP 或二分。"""),
 ],
 "approaches": [
   ap("解法", "一趟掃描", [("c", S["p674"])], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>相等</strong> → 不算遞增，重設。", "<strong>單一元素</strong> → 1。"],
 "follow": [("h", "子陣列 vs 子序列"), ("c", "連續（子陣列）：通常一趟掃描或滑動視窗；不連續（子序列）：通常需要 DP。")],
 "related": ["<strong>第 300 題 最長遞增子序列</strong>", "<strong>第 673 題 最長遞增子序列的個數</strong>"],
 "check": ["相等的相鄰元素要怎麼處理？"],
})
