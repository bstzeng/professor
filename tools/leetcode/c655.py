# -*- coding: utf-8 -*-
"""第 655、657、658、659、661、662、664、665 題。"""
import random, heapq
from collections import Counter
from functools import lru_cache
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, nodes

S = Src()
random.seed(655)


def _height(t): return 0 if t is None else 1 + max(_height(t.left), _height(t.right))


# ==================== 655. Print Binary Tree ====================
S["p655"] = '''class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(nd):
            return -1 if not nd else 1 + max(height(nd.left), height(nd.right))
        h = height(root)                        # 題目定義的高度：只有根時為 0
        m, n = h + 1, 2 ** (h + 1) - 1
        res = [[""] * n for _ in range(m)]
        def place(nd, r, c):
            if not nd:
                return
            res[r][c] = str(nd.val)
            off = 2 ** (h - r - 1)              # ★ 孩子與父節點的水平距離，每往下一層減半
            place(nd.left, r + 1, c - off)
            place(nd.right, r + 1, c + off)
        place(root, 0, (n - 1) // 2)
        return res'''

_p655 = S.load("p655")
assert _p655.printTree(lv([1, 2])) == [["", "1", ""], ["2", "", ""]]
assert _p655.printTree(lv([1, 2, 3, None, 4])) == [["", "", "", "1", "", "", ""], ["", "1", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]][:0] or True
r = _p655.printTree(lv([1, 2, 3, None, 4]))
assert r == [["", "", "", "1", "", "", ""], ["", "2", "", "", "", "3", ""], ["", "", "4", "", "", "", ""]]
print("P655 OK")

em({
 "num": 655, "title": "輸出二元樹",
 "desc": "先求高度決定矩陣大小 (h+1) × (2^(h+1)−1)，根放正中間，孩子的水平偏移每層減半。",
 "zh": [
   "給你二元樹的根節點，把樹畫進一個 <code>m x n</code> 的字串矩陣 <code>res</code>。設樹的高度為 <code>height</code>（只有根時為 0），規則如下：",
   ("ul", ["列數 <code>m = height + 1</code>，欄數 <code>n = 2^(height+1) − 1</code>。",
           "根放在第一列的正中間 <code>res[0][(n−1)/2]</code>。",
           "若某節點放在 <code>res[r][c]</code>，它的左孩子放在 <code>res[r+1][c − 2^(height−r−1)]</code>，右孩子放在 <code>res[r+1][c + 2^(height−r−1)]</code>。",
           "空的格子放空字串 <code>\"\"</code>。"]),
 ],
 "idea": [
   ("c", """【題目已經把規則寫好了】
    1. 求高度 h，建 (h+1) × (2^(h+1) - 1) 的空矩陣。
    2. 從根開始遞迴放置：
           位置 (r, c)，孩子在下一列，左右偏移 2^(h - r - 1)。

【為什麼偏移是這樣？】
    第 r 列的每個節點「管轄」寬度 2^(h-r+1) - 1 的區塊，
    孩子放在左右兩半的中間 -> 偏移是半寬的一半，每層減半。"""),
 ],
 "approaches": [
   ap("解法", "求高度 + 遞迴放置", [("c", S["p655"])], "O(h · 2ʰ)", "O(h · 2ʰ)", "矩陣本身的大小", "", optimal=True),
 ],
 "edges": ["<strong>只有根</strong> → [[\"1\"]]。", "<strong>高度定義</strong> → 只有根時為 0，要和「節點數深度」區分。"],
 "follow": [("h", "樹的視覺化"), ("c", "這就是在終端機畫出二元樹的方法。偏移每層減半保證不同子樹不會重疊。")],
 "related": ["<strong>第 102 題 二元樹的層序走訪</strong>", "<strong>第 662 題 二元樹最大寬度</strong>"],
 "check": ["矩陣的欄數為什麼是 2^(h+1) − 1？", "第 r 列的孩子偏移量是多少？"],
})


# ==================== 657. Robot Return to Origin ====================
S["p657"] = '''class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # ★ 回到原點 <=> 上下次數相同，而且左右次數相同
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")'''

_p657 = S.load("p657")
for _ in range(2000):
    m = "".join(random.choice("UDLR") for _ in range(random.randint(1, 10)))
    x = sum({"L": -1, "R": 1}.get(c, 0) for c in m); y = sum({"D": -1, "U": 1}.get(c, 0) for c in m)
    assert _p657.judgeCircle(m) == (x == 0 and y == 0)
print("P657 OK")

em({
 "num": 657, "title": "機器人能否返回原點",
 "desc": "上下互相抵消、左右互相抵消：比較四個方向的次數即可。",
 "zh": ["機器人從原點 (0, 0) 出發，依字串 <code>moves</code> 移動（<code>'U'</code> 上、<code>'D'</code> 下、<code>'L'</code> 左、<code>'R'</code> 右，每次一格）。判斷它最後是否回到原點。"],
 "idea": [
   ("c", """【座標分開看】
    y：U +1、D -1 -> 回到 0 <=> U 和 D 一樣多
    x：R +1、L -1 -> 回到 0 <=> R 和 L 一樣多

    移動順序完全不影響終點。"""),
 ],
 "approaches": [
   ap("解法", "計數", [("c", S["p657"])], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>空移動</strong>（題目長度至少 1）。", "<strong>順序不同但次數相同</strong> → 結果相同。"],
 "follow": [("h", "會轉彎的機器人"), ("c", "第 1041 題（困於環中的機器人）：指令改成「前進、左轉、右轉」並無限重複，判斷是否被困在一個圓內——只要模擬一次，若回到原點或方向改變就一定會困住。")],
 "related": ["<strong>第 1041 題 困於環中的機器人</strong>"],
 "check": ["為什麼移動順序不影響終點？"],
})


# ==================== 658. Find K Closest Elements ====================
S["p658"] = '''class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lo, hi = 0, len(arr) - k            # 答案是某個長度 k 的視窗 arr[i : i+k]，二分起點 i
        while lo < hi:
            mid = (lo + hi) // 2
            # ★ 比較視窗兩端「下一個被淘汰的候選」：左端 arr[mid] 與右邊外面的 arr[mid+k]
            if x - arr[mid] > arr[mid + k] - x:
                lo = mid + 1                # 左端比較遠：視窗應該往右
            else:
                hi = mid
        return arr[lo:lo + k]'''

_p658 = S.load("p658")
for _ in range(3000):
    arr = sorted(random.randint(-5, 10) for _ in range(random.randint(1, 10))); k = random.randint(1, len(arr)); x = random.randint(-8, 13)
    want = sorted(sorted(arr, key=lambda a: (abs(a - x), a))[:k])
    assert _p658.findClosestElements(arr, k, x) == want
print("P658 OK")

em({
 "num": 658, "title": "找到 K 個最接近的元素",
 "desc": "答案一定是一個連續的長度 k 視窗；二分視窗的起點，比較 arr[mid] 和 arr[mid+k] 哪個離 x 遠。",
 "zh": [
   "給你一個<strong>已排序</strong>的整數陣列 <code>arr</code>、整數 <code>k</code> 和 <code>x</code>，找出最接近 <code>x</code> 的 <code>k</code> 個數，並依遞增順序回傳。",
   "整數 a 比 b 更接近 x 的條件：<code>|a − x| &lt; |b − x|</code>，或距離相同但 <code>a &lt; b</code>。",
 ],
 "idea": [
   ("c", """【答案是連續的一段】
    陣列有序，最接近 x 的 k 個數一定是某個連續視窗 arr[i : i+k]。

【二分視窗起點 i ∈ [0, n-k]】
    比較 arr[mid]（視窗最左）和 arr[mid+k]（視窗右邊外面第一個）：
        x - arr[mid] > arr[mid+k] - x：
            右邊那個比較近，視窗起點至少要 mid+1
        否則：起點 <= mid
    注意不要加絕對值：arr[mid] 和 arr[mid+k] 可能都在 x 的同一側，
    直接用帶號的差比較才正確。
    距離相同時選左邊（較小的數），所以用 > 而不是 >=。

【其他做法】
    雙指標從兩端往內刪，刪掉 n-k 個，O(n)。"""),
 ],
 "approaches": [
   ap("解法一", "雙指標從兩端刪除", [("c", "l, r = 0, n-1\n當 r - l + 1 > k：刪掉 |arr[l]-x| 和 |arr[r]-x| 中較遠的（相同時刪右邊）")], "O(n)", "O(1)"),
   ap("解法二", "二分視窗起點", [("c", S["p658"]), "驗證方式：和「依 (距離, 值) 排序取前 k 個」比對 3000 組。"], "O(log(n−k) + k)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>x 比所有數都小</strong> → 前 k 個。", "<strong>x 比所有數都大</strong> → 後 k 個。", "<strong>距離相同</strong> → 選較小的。"],
 "follow": [("h", "為什麼不能用絕對值比較？"), ("c", "若 arr[mid] 和 arr[mid+k] 都在 x 右邊且相等（重複值），|差| 相同，但視窗應該往左；帶號的 x − arr[mid] 為負，比較結果會讓 hi = mid，正確。")],
 "related": ["<strong>第 35 題 搜尋插入位置</strong>", "<strong>第 973 題 最接近原點的 K 個點</strong>", "<strong>第 1300 題 轉變陣列後最接近目標值的陣列和</strong>"],
 "check": ["為什麼答案一定是連續的？", "二分時比較的是哪兩個元素？", "為什麼不加絕對值？"],
})


# ==================== 659. Split Array into Consecutive Subsequences ====================
S["p659"] = '''class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        cnt = Counter(nums)                 # 還沒被使用的數
        tail = Counter()                    # tail[x]：以 x 結尾、長度 >= 3 的子序列數
        for x in nums:
            if cnt[x] == 0:
                continue                    # 已經被之前的新序列用掉
            cnt[x] -= 1
            if tail[x - 1]:
                tail[x - 1] -= 1            # ★ 優先接到已有的序列後面
                tail[x] += 1
            elif cnt[x + 1] and cnt[x + 2]:
                cnt[x + 1] -= 1             # 否則以 x 開頭新建一個長度 3 的序列
                cnt[x + 2] -= 1
                tail[x + 2] += 1
            else:
                return False                # 既接不上也開不了新的
        return True'''

_p659 = S.load("p659")
@lru_cache(None)
def _bf659(rest, ends):
    # rest：還沒分配的數（有序 tuple）；ends：每個進行中序列的 (結尾, 長度) 排序 tuple
    if not rest:
        return all(L >= 3 for _, L in ends)
    x = rest[0]; r = rest[1:]; opts = False
    for i, (e, L) in enumerate(ends):
        if e == x - 1:
            ne = ends[:i] + ((x, L + 1),) + ends[i + 1:]
            if _bf659(r, tuple(sorted(ne))): return True
    return _bf659(r, tuple(sorted(ends + ((x, 1),))))
for _ in range(1500):
    a = sorted(random.randint(1, 6) for _ in range(random.randint(1, 9)))
    assert _p659.isPossible(a) == _bf659(tuple(a), ()), a
print("P659 OK")

em({
 "num": 659, "title": "分割陣列為連續子序列",
 "desc": "貪心：每個數優先接到「以 x−1 結尾」的序列後面，接不上才以它開頭新建長度 3 的序列。",
 "zh": [
   "給你一個<strong>非遞減排序</strong>的整數陣列 <code>nums</code>。判斷能否把它分成一個或多個子序列，使得：",
   ("ul", ["每個子序列都由<strong>連續遞增</strong>的整數組成（每個數比前一個大 1）。", "每個子序列的長度<strong>至少為 3</strong>。"]),
 ],
 "idea": [
   ("c", """【由小到大處理每個數 x，兩種選擇】
    A. 接到某個以 x-1 結尾的序列後面
    B. 以 x 開頭建立新序列

【為什麼優先 A？】
    新序列需要 x+1、x+2 也存在才能湊滿 3 個，風險高；
    接到已有序列後面一定不會讓情況變差：
    如果某個解讓 x 開新序列，而存在以 x-1 結尾的序列，
    可以把 x 開頭的那整段接到那個序列後面，仍然合法。

【開新序列時直接預約 x+1、x+2】
    立刻從 cnt 中扣掉，保證新序列長度至少 3；
    扣不到就失敗。

【兩個計數表】
    cnt：還沒用的數
    tail：以某數結尾、已經合法（長度 >= 3）的序列數"""),
 ],
 "approaches": [
   ap("解法", "貪心 + 兩個計數表", [("c", S["p659"]), "驗證方式：和窮舉每個數接到哪個序列或新建序列的搜尋比對 1500 組。"], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>[1,2,3,3,4,5]</strong> → True（123、345）。", "<strong>[1,2,3,4,4,5]</strong> → False。", "<strong>重複的數很多</strong> → 會開出多條平行的序列。"],
 "follow": [("h", "相關"), ("c", "第 846 題（一手順子）：每組長度固定為 W，從最小的數開始貪心組成順子。本題長度不固定，需要「接上舊的」這個選項。")],
 "related": ["<strong>第 846 題 一手順子</strong>", "<strong>第 1296 題 劃分陣列為連續數字的集合</strong>"],
 "check": ["為什麼優先接到已有的序列後面？", "開新序列時為什麼要立刻扣掉 x+1 和 x+2？"],
})


# ==================== 661. Image Smoother ====================
S["p661"] = '''class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = c = 0
                for x in range(max(0, i - 1), min(m, i + 2)):       # ★ 3×3 範圍與邊界取交集
                    for y in range(max(0, j - 1), min(n, j + 2)):
                        s += img[x][y]
                        c += 1
                res[i][j] = s // c                                  # 向下取整的平均
        return res'''

_p661 = S.load("p661")
assert _p661.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
assert _p661.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == [[137, 141, 137], [141, 138, 141], [137, 141, 137]]
print("P661 OK")

em({
 "num": 661, "title": "圖片平滑器",
 "desc": "每個像素取周圍 3×3（與邊界取交集）的平均並向下取整；附上二維前綴和與卷積的延伸。",
 "zh": ["<strong>圖片平滑器</strong>是一個 3×3 的濾波器：每個像素的新值 = 它與周圍 8 個像素（超出邊界的不算）的<strong>平均值，向下取整</strong>。給你灰階圖片 <code>img</code>，回傳平滑後的圖片。"],
 "idea": [
   ("c", """【直接模擬】
    對每個 (i, j)，加總 3×3 範圍中存在的格子，除以格子數。
    範圍與邊界取交集：
        x 在 [max(0, i-1), min(m-1, i+1)]，y 同理。

【要寫到新矩陣】
    不能原地覆蓋，否則後面的格子會用到已平滑的值。
    （或用高位元存新值的原地技巧。）

【窗口很大時】
    用二維前綴和，每格 O(1) 求區域和。"""),
 ],
 "approaches": [
   ap("解法", "直接模擬", [("c", S["p661"])], "O(mn)", "O(mn)", "每格固定看 9 格", "輸出矩陣", optimal=True),
 ],
 "edges": ["<strong>角落</strong> → 只有 4 格。", "<strong>邊</strong> → 6 格。", "<strong>單一像素</strong> → 自己。"],
 "follow": [("h", "影像處理中的卷積"), ("c", "這是「均值濾波」（box blur）。把 3×3 的權重換成高斯分布就是高斯模糊；換成 [[0,−1,0],[−1,5,−1],[0,−1,0]] 就是銳化。")],
 "related": ["<strong>第 304 題 二維區域和檢索</strong>", "<strong>第 1314 題 矩陣區域和</strong>"],
 "check": ["為什麼不能原地更新？", "邊界格子的範圍怎麼算？"],
})


# ==================== 662. Maximum Width of Binary Tree ====================
S["p662"] = '''class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        level = [(root, 0)]                     # (節點, 在完全二元樹中的編號)
        while level:
            res = max(res, level[-1][1] - level[0][1] + 1)   # 這一層最右 - 最左 + 1
            first = level[0][1]
            nxt = []
            for nd, i in level:
                i -= first                      # ★ 每層重新從 0 編號，避免編號隨深度指數成長
                if nd.left:
                    nxt.append((nd.left, 2 * i))
                if nd.right:
                    nxt.append((nd.right, 2 * i + 1))
            level = nxt
        return res'''

_p662 = S.load("p662")
assert _p662.widthOfBinaryTree(lv([1, 3, 2, 5, 3, None, 9])) == 4
assert _p662.widthOfBinaryTree(lv([1, 3, 2, 5, None, None, 9, 6, None, 7])) == 7
for _ in range(1500):
    t = rand_tree(random.randint(1, 12))
    lvl = [(t, 0)]; best = 0
    while lvl:
        best = max(best, lvl[-1][1] - lvl[0][1] + 1)
        lvl = [(c, 2 * i + k) for nd, i in lvl for k, c in enumerate((nd.left, nd.right)) if c]
    assert _p662.widthOfBinaryTree(t) == best
print("P662 OK")

em({
 "num": 662, "title": "二元樹最大寬度",
 "desc": "像堆積一樣給節點編號（左 2i、右 2i+1），每層寬度 = 最右編號 − 最左編號 + 1；每層重新從 0 編號避免數字暴增。",
 "zh": [
   "給你二元樹的根節點，回傳樹的<strong>最大寬度</strong>。",
   "每一層的寬度是該層最左與最右的非空節點之間的長度——<strong>中間的空節點也要算</strong>，就像把這棵樹補成完全二元樹後算出來的寬度。答案保證在 32 位元有號整數範圍內。",
 ],
 "idea": [
   ("c", """【像堆積一樣編號】
    根是 0，節點 i 的左孩子 2i、右孩子 2i+1。
    同一層中，空節點的位置也被編號「佔住」了。
    該層寬度 = 最右編號 - 最左編號 + 1。

【編號會爆炸】
    一條往右的長鏈，深度 3000 的編號是 2^3000。
    Python 不會溢位但會變慢；其他語言會溢位。
    解法：每層都減掉該層最左節點的編號，從 0 重新開始。
    寬度只看差值，不受影響。"""),
 ],
 "approaches": [
   ap("解法", "BFS + 堆積編號", [("c", S["p662"]), "驗證方式：和不做重新編號的版本比對 1500 棵隨機樹。"], "O(n)", "O(w)", optimal=True),
 ],
 "edges": ["<strong>只有根</strong> → 1。", "<strong>很深的單鏈</strong> → 重新編號避免數字變大。", "<strong>中間的空節點</strong> → 要算進寬度。"],
 "follow": [("h", "堆積編號的用途"), ("c", "陣列表示的二元堆積就是用這套編號。第 958 題（判斷完全二元樹）也可以用它：所有編號應該恰好是 0..n−1。")],
 "related": ["<strong>第 958 題 二元樹的完全性檢驗</strong>", "<strong>第 102 題 二元樹的層序走訪</strong>", "<strong>第 655 題 輸出二元樹</strong>"],
 "check": ["節點編號如何反映空節點的位置？", "為什麼每層要重新從 0 編號？"],
})


# ==================== 664. Strange Printer ====================
S["p664"] = '''class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]        # dp[i][j]：印出 s[i..j] 的最少次數
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]     # ★ s[j] 可以在印 s[i] 那一次順便印上（延長那一筆）
                else:
                    dp[i][j] = min(dp[i][k] + dp[k + 1][j] for k in range(i, j))   # 從中間切開
        return dp[0][n - 1]'''

_p664 = S.load("p664")
assert _p664.strangePrinter("aaabbb") == 2 and _p664.strangePrinter("aba") == 2
def _bf664(s):
    # BFS：狀態 = 目前紙上的內容（未印的位置為 '.'），每步把一段連續區間覆蓋成某個字元
    from collections import deque
    n = len(s); start = "." * n; seen = {start}; q = deque([(start, 0)]); chars = set(s)
    while q:
        cur, d = q.popleft()
        if cur == s: return d
        for i in range(n):
            for j in range(i, n):
                for c in chars:
                    nx = cur[:i] + c * (j - i + 1) + cur[j + 1:]
                    if nx not in seen:
                        seen.add(nx); q.append((nx, d + 1))
for _ in range(150):
    s = "".join(random.choice("abc") for _ in range(random.randint(1, 5)))
    assert _p664.strangePrinter(s) == _bf664(s), s
print("P664 OK")

em({
 "num": 664, "title": "奇怪的印表機",
 "desc": "區間 DP：s[i] == s[j] 時，最後一個字元可以「搭便車」在印 s[i] 的那一筆一起印；否則枚舉切點。",
 "zh": [
   "有一台奇怪的印表機：每次只能印出<strong>一段連續、相同字元</strong>的序列，而且可以從任何位置開始、在任何位置結束，新印的字元會<strong>覆蓋</strong>原本的字元。",
   "給你字串 <code>s</code>，回傳印出它所需的<strong>最少列印次數</strong>。",
 ],
 "idea": [
   ("c", """【區間 DP】
    dp[i][j] = 印出 s[i..j] 的最少次數。

【s[i] == s[j]】
    第一筆可以印 s[i] 這個字元，而且一路延伸到 j，
    之後再覆蓋中間的部分 —— s[j] 不需要額外的次數：
        dp[i][j] = dp[i][j-1]

【s[i] != s[j]】
    印 s[i] 和 s[j] 的那兩筆不可能是同一筆，
    所以存在一個切點 k，左右兩段各自獨立印：
        dp[i][j] = min over k ( dp[i][k] + dp[k+1][j] )

【計算順序】
    i 由大到小、j 由小到大。"""),
 ],
 "approaches": [
   ap("解法", "區間 DP", [("c", S["p664"]), "驗證方式：在長度 ≤ 5 的字串上和 BFS（每步把任一區間覆蓋成任一字元）比對 150 組。"], "O(n³)", "O(n²)", optimal=True),
 ],
 "edges": ["<strong>單一字元</strong> → 1。", "<strong>連續相同字元</strong> → 可以先壓縮成一個，不影響答案。", "<strong>\"aba\"</strong> → 2（先印 aaa，再印中間的 b）。"],
 "follow": [("h", "相關的區間 DP"), ("c", "第 546 題（移除盒子）需要再多一維；第 1000 題（合併石頭）、第 312 題（戳氣球）也是「枚舉切點」的區間 DP。")],
 "related": ["<strong>第 546 題 移除盒子</strong>", "<strong>第 312 題 戳氣球</strong>", "<strong>第 516 題 最長迴文子序列</strong>"],
 "check": ["s[i] == s[j] 時為什麼 dp[i][j] = dp[i][j−1]？", "不相等時為什麼一定存在一個切點？"],
})


# ==================== 665. Non-decreasing Array ====================
S["p665"] = '''class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if changed:
                    return False                # 第二次遇到下降
                changed = True
                # ★ 能降低 nums[i-1] 就降低（不影響後面）；否則只好把 nums[i] 拉高
                if i < 2 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
        return True'''

_p665 = S.load("p665")
for _ in range(3000):
    a = [random.randint(0, 5) for _ in range(random.randint(1, 7))]
    nd = lambda b: all(b[i] <= b[i + 1] for i in range(len(b) - 1))
    want = nd(a) or any(nd(a[:i] + [v] + a[i + 1:]) for i in range(len(a)) for v in range(-1, 7))
    assert _p665.checkPossibility(a[:]) == want, a
print("P665 OK")

em({
 "num": 665, "title": "非遞減數列",
 "desc": "遇到下降 nums[i] < nums[i−1] 時，優先把 nums[i−1] 降下來；若會破壞前面才把 nums[i] 拉上去；第二次下降就失敗。",
 "zh": ["給你一個整數陣列 <code>nums</code>，判斷<strong>最多修改一個元素</strong>後，它能否變成非遞減數列（每個元素都 ≤ 下一個元素）。"],
 "idea": [
   ("c", """【下降點】
    nums[i] < nums[i-1] 的位置。
    一次修改最多影響兩個相鄰的比較 (k-1, k) 與 (k, k+1)，
    所以下降點太多一定不行；但有一個下降點也不一定行 ——
    要看修改之後會不會在旁邊製造新的下降。

【遇到下降時怎麼修？】
    兩種選擇：
        降低 nums[i-1] 到 nums[i]：對後面最有利（不讓值變大），
            但前提是 nums[i-2] <= nums[i]，否則會在前面造成新的下降。
        拉高 nums[i] 到 nums[i-1]：一定不破壞前面，但可能影響後面。
    能降就降，不能降才拉高。

【例】
    [3, 4, 2, 3]：在 i=2 下降，nums[0]=3 > 2，只能把 2 拉高成 4，
    然後 4 > 3 又下降 -> False。"""),
 ],
 "approaches": [
   ap("解法", "貪心修正", [("c", S["p665"]), "驗證方式：和「嘗試修改每個位置成每個可能值」的暴力法比對 3000 組。"], "O(n)", "O(1)", "", "會修改輸入", optimal=True),
 ],
 "edges": ["<strong>[4,2,3]</strong> → True（4 改成 1）。", "<strong>[3,4,2,3]</strong> → False。", "<strong>下降在第一個位置</strong> → 直接降低 nums[0]。"],
 "follow": [("h", "最少修改幾個？"), ("c", "一般化：最少修改幾個元素使陣列非遞減 = n − 最長非遞減子序列長度（LIS 的變形，O(n log n)）。")],
 "related": ["<strong>第 300 題 最長遞增子序列</strong>", "<strong>第 1909 題 刪除一個元素使陣列嚴格遞增</strong>"],
 "check": ["遇到下降時有哪兩種修法？", "什麼時候不能降低 nums[i−1]？"],
})
