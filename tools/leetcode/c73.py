# -*- coding: utf-8 -*-
"""第 73–76 題。"""
import random, collections
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(73)

# ==================== 73. Set Matrix Zeroes ====================
S["p73_sets"] = '''class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()

        # 第 1 遍：記下「哪些列」和「哪些行」有 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # 第 2 遍：照著標記清零
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0'''

S["p73_inplace"] = '''class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        # 用「第 0 列」和「第 0 行」當標記區，但它們自己的狀態要另外存
        first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

        # 第 1 遍：把 (1,1) 以後的 0，記到第 0 列／第 0 行
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 第 2 遍：照著標記清零（同樣只處理 (1,1) 以後）
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 最後才處理第 0 列和第 0 行本身
        if first_row_has_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_has_zero:
            for i in range(m):
                matrix[i][0] = 0'''

_p73 = [S.load(k) for k in ("p73_sets", "p73_inplace")]


def _p73_ref(mat):
    m, n = len(mat), len(mat[0])
    rows = {i for i in range(m) for j in range(n) if mat[i][j] == 0}
    cols = {j for i in range(m) for j in range(n) if mat[i][j] == 0}
    return [[0 if i in rows or j in cols else mat[i][j] for j in range(n)]
            for i in range(m)]


for mat in [[[1, 1, 1], [1, 0, 1], [1, 1, 1]],
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[1]], [[0]], [[1, 0]], [[0], [1]], [[1, 2], [3, 4]]]:
    e = _p73_ref(mat)
    for sol in _p73:
        a = [r[:] for r in mat]
        sol.setZeroes(a)
        assert a == e, ("P73", mat, sol, a, e)
for _ in range(4000):
    m_, n_ = random.randint(1, 5), random.randint(1, 5)
    mat = [[0 if random.random() < 0.2 else random.randint(1, 9)
            for _ in range(n_)] for _ in range(m_)]
    e = _p73_ref(mat)
    for sol in _p73:
        a = [r[:] for r in mat]
        sol.setZeroes(a)
        assert a == e, ("P73", mat, sol, a, e)
print("P73 solutions OK")

_P73_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">O(1) 空間的關鍵：借用第 0 列和第 0 行當「標記區」</text>
            <g font-size="14" text-anchor="middle">
              <text x="160" y="50" fill="var(--text-muted)" font-size="12">原矩陣</text>
              <rect x="60" y="62" width="50" height="38" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="85" y="87" fill="var(--gold)">0</text>
              <rect x="110" y="62" width="50" height="38" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="135" y="87" fill="var(--gold)">1</text>
              <rect x="160" y="62" width="50" height="38" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="185" y="87" fill="var(--gold)">2</text>
              <rect x="210" y="62" width="50" height="38" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="235" y="87" fill="var(--gold)">0</text>
              <rect x="60" y="100" width="50" height="38" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="85" y="125" fill="var(--gold)">3</text>
              <rect x="110" y="100" width="50" height="38" fill="none" stroke="var(--border)"/><text x="135" y="125" fill="var(--text-muted)">4</text>
              <rect x="160" y="100" width="50" height="38" fill="none" stroke="var(--border)"/><text x="185" y="125" fill="var(--text-muted)">5</text>
              <rect x="210" y="100" width="50" height="38" fill="none" stroke="var(--border)"/><text x="235" y="125" fill="var(--text-muted)">2</text>
              <rect x="60" y="138" width="50" height="38" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="85" y="163" fill="var(--gold)">1</text>
              <rect x="110" y="138" width="50" height="38" fill="none" stroke="var(--border)"/><text x="135" y="163" fill="var(--text-muted)">3</text>
              <rect x="160" y="138" width="50" height="38" fill="none" stroke="var(--border)"/><text x="185" y="163" fill="var(--text-muted)">1</text>
              <rect x="210" y="138" width="50" height="38" fill="none" stroke="var(--border)"/><text x="235" y="163" fill="var(--text-muted)">5</text>
            </g>
            <text x="160" y="196" fill="var(--gold)" font-size="11" text-anchor="middle">金色 = 標記區（第 0 列 + 第 0 行）</text>
            <text x="300" y="120" fill="var(--gold)" font-size="20" text-anchor="middle">→</text>
            <g font-size="14" text-anchor="middle">
              <text x="450" y="50" fill="var(--text-muted)" font-size="12">答案</text>
              <rect x="350" y="62" width="50" height="38" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="375" y="87" fill="#ff8a65">0</text>
              <rect x="400" y="62" width="50" height="38" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="425" y="87" fill="#ff8a65">0</text>
              <rect x="450" y="62" width="50" height="38" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="475" y="87" fill="#ff8a65">0</text>
              <rect x="500" y="62" width="50" height="38" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="525" y="87" fill="#ff8a65">0</text>
              <rect x="350" y="100" width="50" height="38" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="375" y="125" fill="#ff8a65">0</text>
              <rect x="400" y="100" width="50" height="38" fill="none" stroke="var(--accent)"/><text x="425" y="125" fill="var(--accent)">4</text>
              <rect x="450" y="100" width="50" height="38" fill="none" stroke="var(--accent)"/><text x="475" y="125" fill="var(--accent)">5</text>
              <rect x="500" y="100" width="50" height="38" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="525" y="125" fill="#ff8a65">0</text>
              <rect x="350" y="138" width="50" height="38" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="375" y="163" fill="#ff8a65">0</text>
              <rect x="400" y="138" width="50" height="38" fill="none" stroke="var(--accent)"/><text x="425" y="163" fill="var(--accent)">3</text>
              <rect x="450" y="138" width="50" height="38" fill="none" stroke="var(--accent)"/><text x="475" y="163" fill="var(--accent)">1</text>
              <rect x="500" y="138" width="50" height="38" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="525" y="163" fill="#ff8a65">0</text>
            </g>
            <text x="20" y="232" fill="var(--gold)" font-size="12">核心矛盾：清零會「製造新的 0」，如果邊掃邊清，會把整個矩陣都清光。</text>
            <text x="20" y="256" fill="var(--text-muted)" font-size="12">所以一定要分兩遍：先「記錄」，再「執行」。</text>'''

emit({
 "num": 73, "slug": "set-matrix-zeroes",
 "en": [
   "Given an <code>m x n</code> integer matrix <code>matrix</code>, if an element is "
   "<code>0</code>, set its entire row and column to <code>0</code>'s.",
   "You must do it <strong>in place</strong>.",
   "<strong>Follow up:</strong> A straightforward solution using <code>O(mn)</code> space is "
   "probably a bad idea. A simple improvement uses <code>O(m + n)</code> space, but still not "
   "the best solution. Could you devise a constant space solution?",
 ],
 "zh": [
   "給你一個 <code>m × n</code> 的整數矩陣，"
   "如果某個元素是 <code>0</code>，就把它所在的<strong>整列和整行</strong>都設成 <code>0</code>。",
   "必須<strong>原地</strong>修改。",
   "<strong>進階：</strong>O(mn) 空間的做法顯然不好；O(m+n) 空間的做法好一些，但還不是最好。"
   "你能想出<strong>常數空間</strong>的解法嗎？",
 ],
 "pre": [
   ("note", "核心矛盾：清零會製造新的 0", [
     ("c", """如果邊掃邊清：

    matrix = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]

    掃到 (1,1) 的 0 -> 把第 1 列和第 1 行清零
        [[1, 0, 1],
         [0, 0, 0],
         [1, 0, 1]]

    繼續掃，掃到 (0,1) 是 0（剛剛才被我們清成 0 的！）
        -> 又把第 0 列和第 1 行清零
        -> 最後整個矩陣都變成 0  ✘

問題出在：我們沒辦法分辨
    「原本就是 0」和「被我們清成 0」。

解法一律是【分兩遍】：
    第 1 遍：只「記錄」哪些列／行要清，不動矩陣
    第 2 遍：照著記錄執行

差別只在「記錄放哪裡」：
    O(mn)：複製一份矩陣          —— 浪費
    O(m+n)：兩個 set 或兩個陣列   —— 合理
    O(1)：借用矩陣的第 0 列和第 0 行 —— 最佳"""),
   ]),
 ],
 "examples": """範例 1
  輸入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
  輸出：[[1,0,1],[0,0,0],[1,0,1]]

範例 2
  輸入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
  輸出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]""",
 "constraints": [
   "<code>m == matrix.length</code>，<code>n == matrix[0].length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 200",
   "−2³¹ ≤ <code>matrix[i][j]</code> ≤ 2³¹ − 1",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>值域是完整的 32 位元整數</strong> —— "
       "<strong>所以不能用「某個特殊值」當標記</strong>"
       "（例如把要清零的格子先設成 <code>-2³¹</code>），"
       "因為那個值可能是真實資料。"
       "<strong>這一條就是在堵「用哨兵值」這條路。</strong>",
       "<strong>規模只有 200 × 200</strong>，"
       "所以 O(m+n) 空間的版本完全跑得動 —— "
       "<strong>題目要 O(1) 純粹是為了考你。</strong>",
       "<strong>m 和 n 都至少是 1</strong>，"
       "所以 <code>matrix[0][0]</code> 一定存在。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P73_FIG, "0 0 640 270"),
 ],
 "approaches": [
   ap("解法一", "兩個集合記錄（O(m+n) 空間，最好懂）", [
     ("c", S["p73_sets"]),
     "第 1 遍收集，第 2 遍執行。"
     "<strong>思路完全直白，而且不容易寫錯。</strong>",
     "空間 O(m + n)（兩個集合最多裝 m 和 n 個索引）。"
     "在 200 × 200 的規模下這是 400 個整數 —— 完全不是問題。",
     "<strong>面試時先寫這個版本</strong>，"
     "確認邏輯正確之後，再說「可以用矩陣的第一列和第一行當標記區，降到 O(1)」。",
   ], "O(m·n)", "O(m+n)", "掃兩遍", "兩個集合"),

   ap("解法二", "借用第 0 列 / 第 0 行（O(1) 空間，進階解）", [
     "既然 O(m+n) 的資訊要存在某個地方，"
     "而<strong>矩陣本身的第 0 列剛好有 n 格、第 0 行剛好有 m 格</strong> —— "
     "那就借用它們。",
     ("c", S["p73_inplace"]),
     ("h", "為什麼第 0 列和第 0 行要「另外」記？"),
     ("c", """因為它們身兼二職：
    既是「標記區」，又是「需要被清零的真實資料」。

考慮 matrix[0][3] == 0（第 0 列本來就有 0）：
    我們會用 matrix[0][j] 來記「第 j 行要清零」，
    但 matrix[0][3] 本身的 0 到底是
        「原本就是 0」還是「被當成標記寫進去的」？
    分不出來。

    更麻煩的是：如果第 0 列本來就有 0，
    那整個第 0 列都要清零 ——
    但我們在第 1、2 遍時還需要用它當標記，不能提早清掉。

所以：
    1. 先用兩個 bool 記住「第 0 列有沒有 0」「第 0 行有沒有 0」
    2. 第 1、2 遍只處理 (1,1) 以後的區域，用第 0 列／行當標記
    3. 最後才根據那兩個 bool 清掉第 0 列／第 0 行

順序絕對不能顛倒 ——
如果先清第 0 列，標記就全毀了。

這兩個 bool 就是「O(1)」裡的那個常數。"""),
     ("h", "為什麼兩個主迴圈都從 1 開始？"),
     ("c", """第 1 遍 for i in range(1, m): for j in range(1, n):
    只掃 (1,1) 以後的區域。
    第 0 列和第 0 行的 0 已經被那兩個 bool 記下來了。

    如果從 0 開始掃：
        matrix[0][j] == 0 會讓我們寫 matrix[0][0] = 0 和 matrix[0][j] = 0
        後者是寫到自己身上（無害），但前者會污染「第 0 行」的標記 ——
        導致整個第 0 行被錯誤地清零。

第 2 遍同理。

    如果第 2 遍從 0 開始：
        matrix[0][0] 可能因為某個標記而被設成 0，
        然後它又會被當成「第 0 列的標記」…
        邏輯混亂。

「把標記區和資料區分開處理」是這個解法的關鍵紀律。"""),
     ("h", "為什麼「值域是完整 32 位元」讓其他技巧失效？"),
     ("c", """常見的「投機」做法：
    把要清零的格子先標記成某個特殊值（例如 float("inf") 或 -2**31），
    第二遍再把它們變成 0。

    在 Python 裡可以用 None 或 float("inf")（不是合法的矩陣值），
    但在 C/Java 裡，int 的每一個值都可能是真實資料 ——
    找不到安全的哨兵。

    而且就算用 None，那也是「用型別系統偷渡了額外的資訊位元」，
    嚴格說不是 O(1) 空間（每個格子多了一個 bit）。

所以「借用第 0 列／行」才是真正的 O(1) 解 ——
它沒有引入任何新的儲存空間，只是「重新解讀」既有的格子。"""),
   ], "O(m·n)", "O(1)", "掃兩遍 + 兩次收尾", "兩個 bool", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "好寫程度", "備註"],
   [["一、兩個集合", "O(mn)", "O(m+n)", "★★★★★", "先寫它"],
    ["二、借用第 0 列／行", "O(mn)", "O(1)", "★★☆☆☆", "進階解；順序是關鍵"]]),
 "edges": [
   "<strong>1 × 1</strong>：<code>[[0]]</code> → <code>[[0]]</code>；<code>[[1]]</code> → <code>[[1]]</code>。",
   "<strong>第 0 列有 0</strong>：<code>[[1,0]]</code> → <code>[[0,0]]</code>。"
   "<strong>沒有 <code>first_row_has_zero</code> 會錯。</strong>",
   "<strong>第 0 行有 0</strong>：<code>[[0],[1]]</code> → <code>[[0],[0]]</code>。",
   "<strong><code>matrix[0][0] == 0</code></strong>："
   "第 0 列和第 0 行都要清。兩個 bool 都會是 True。",
   "<strong>完全沒有 0</strong>：<code>[[1,2],[3,4]]</code> → 原樣。",
   "<strong>全部都是 0</strong>：原樣（都已經是 0）。",
   "<strong>邊掃邊清</strong>：<code>[[1,1,1],[1,0,1],[1,1,1]]</code> 會變成全 0。"
   "<strong>這是本題的核心陷阱。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果不能修改輸入呢？"),
   "那 O(1) 空間是不可能的 —— 你必須把「哪些列／行要清」記在某個地方，"
   "而那至少需要 m + n 個位元。"
   "<strong>「借用輸入當儲存空間」正是 O(1) 解法的全部基礎。</strong>"
   "（和第 41 題「缺失的第一個正數」是同一個道理。）",
   ("h", "追問二：如果矩陣很大，放不進記憶體呢？"),
   "改成兩趟的<strong>串流處理</strong>：",
   ("ul", [
     "<strong>第一趟</strong>：讀過整個矩陣，記錄哪些列／行有 0（需要 O(m+n) 記憶體，通常可接受）",
     "<strong>第二趟</strong>：再讀一次，逐格輸出（該清的輸出 0）",
   ]),
   "<strong>O(1) 空間的技巧在這裡反而不適用</strong> —— "
   "因為它需要「隨機存取第 0 列和第 0 行」，"
   "而串流讀取只能循序。"
   "<strong>「最省空間」和「最適合串流」往往不是同一個解法。</strong>",
   ("h", "追問三：這個「借用輸入當儲存空間」的技巧還能用在哪？"),
   ("c", """第 41 題  缺失的第一個正數    把數字換到自己的位置，或用正負號標記
第 73 題  矩陣置零             借用第 0 列／行
第 442 題 找出所有重複的數字     用正負號標記
第 448 題 找出所有消失的數字     同上
第 289 題 生命遊戲             用「2 位元」編碼新舊兩種狀態
                              （0/1 是舊狀態，額外的位元記新狀態）

共同的條件：
    1. 允許修改輸入
    2. 輸入本身有「沒被用滿」的資訊空間
       （值域比實際需要小、或索引和值域對得上、
         或有結構性的冗餘）

共同的代價：
    程式碼變複雜、破壞輸入、而且常常有微妙的順序要求。

    值不值得？在 LeetCode 上是「題目要求」，
    在真實工程裡通常「不值得」——
    除非記憶體真的是瓶頸（嵌入式、GPU kernel、超大資料）。""",),
 ],
 "related": [
   "<strong>第 41 題 First Missing Positive</strong> —— 同樣是「借用輸入」的 O(1) 技巧",
   "<strong>第 289 題 Game of Life</strong> —— 用位元編碼新舊狀態",
   "<strong>第 48 題 Rotate Image</strong> —— 另一個原地矩陣操作",
   "<strong>第 54 題 Spiral Matrix</strong> —— 矩陣走訪",
 ],
 "check": [
   "為什麼「邊掃邊清」會把整個矩陣清光？請用範例 1 追一遍。",
   "為什麼第 0 列和第 0 行需要用兩個額外的 bool 記錄？",
   "兩個主迴圈為什麼都從 1 開始而不是 0？",
   "為什麼「值域是完整 32 位元整數」這一條，堵死了「用特殊值當標記」的做法？",
 ],
})
print("P73 written")

# ==================== 74. Search a 2D Matrix ====================
S["p74_flat"] = '''class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # 把二維矩陣「看成」一個長度 m*n 的有序一維陣列
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            r, c = divmod(mid, n)          # 一維索引還原成 (列, 行)
            v = matrix[r][c]

            if v == target:
                return True
            if v < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return False'''

S["p74_two"] = '''class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # 第 1 次二分：找出 target 可能在哪一列
        lo, hi = 0, m - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            if matrix[mid][0] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            return False        # while 沒有 break -> 沒有任何一列涵蓋 target

        # 第 2 次二分：在那一列裡找
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False'''

S["p74_staircase"] = '''class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 從「右上角」出發：往左變小、往下變大
        # 這個解法對第 240 題（每列每行遞增，但列之間不連續）也成立
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            v = matrix[r][c]
            if v == target:
                return True
            if v > target:
                c -= 1          # 太大 -> 往左（這一行的下面只會更大）
            else:
                r += 1          # 太小 -> 往下（這一列的左邊只會更小）

        return False'''

_p74 = [S.load(k) for k in ("p74_flat", "p74_two", "p74_staircase")]


def _make_matrix(m, n, lo=0, step=3):
    v = lo
    mat = []
    for _ in range(m):
        row = []
        for _ in range(n):
            v += random.randint(1, step)
            row.append(v)
        mat.append(row)
    return mat


for mat, t in [([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
               ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
               ([[1]], 1), ([[1]], 2), ([[1, 3]], 3), ([[1], [3]], 3)]:
    e = any(t in row for row in mat)
    for sol in _p74:
        assert sol.searchMatrix([r[:] for r in mat], t) is e, ("P74", mat, t, sol)
for _ in range(4000):
    m_, n_ = random.randint(1, 5), random.randint(1, 5)
    mat = _make_matrix(m_, n_)
    t = random.randint(0, mat[-1][-1] + 3)
    e = any(t in row for row in mat)
    for sol in _p74:
        assert sol.searchMatrix([r[:] for r in mat], t) is e, ("P74", mat, t, sol, e)
print("P74 solutions OK")

_P74_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">整個矩陣「攤平」之後就是一個有序陣列 —— 所以可以直接對 [0, m·n−1] 二分</text>
            <g font-size="13" text-anchor="middle">
              <rect x="70" y="48" width="58" height="34" fill="none" stroke="var(--accent)"/><text x="99" y="71" fill="var(--accent)">1</text>
              <rect x="128" y="48" width="58" height="34" fill="none" stroke="var(--accent)"/><text x="157" y="71" fill="var(--accent)">3</text>
              <rect x="186" y="48" width="58" height="34" fill="none" stroke="var(--accent)"/><text x="215" y="71" fill="var(--accent)">5</text>
              <rect x="244" y="48" width="58" height="34" fill="none" stroke="var(--accent)"/><text x="273" y="71" fill="var(--accent)">7</text>
              <rect x="70" y="82" width="58" height="34" fill="none" stroke="var(--gold)"/><text x="99" y="105" fill="var(--gold)">10</text>
              <rect x="128" y="82" width="58" height="34" fill="none" stroke="var(--gold)"/><text x="157" y="105" fill="var(--gold)">11</text>
              <rect x="186" y="82" width="58" height="34" fill="none" stroke="var(--gold)"/><text x="215" y="105" fill="var(--gold)">16</text>
              <rect x="244" y="82" width="58" height="34" fill="none" stroke="var(--gold)"/><text x="273" y="105" fill="var(--gold)">20</text>
              <rect x="70" y="116" width="58" height="34" fill="none" stroke="#ff8a65"/><text x="99" y="139" fill="#ff8a65">23</text>
              <rect x="128" y="116" width="58" height="34" fill="none" stroke="#ff8a65"/><text x="157" y="139" fill="#ff8a65">30</text>
              <rect x="186" y="116" width="58" height="34" fill="none" stroke="#ff8a65"/><text x="215" y="139" fill="#ff8a65">34</text>
              <rect x="244" y="116" width="58" height="34" fill="none" stroke="#ff8a65"/><text x="273" y="139" fill="#ff8a65">60</text>
            </g>
            <text x="340" y="105" fill="var(--gold)" font-size="20" text-anchor="middle">→</text>
            <g font-size="12" text-anchor="middle">
              <rect x="380" y="82" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="397" y="104" fill="var(--accent)">1</text>
              <rect x="414" y="82" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="431" y="104" fill="var(--accent)">3</text>
              <rect x="448" y="82" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="465" y="104" fill="var(--accent)">5</text>
              <rect x="482" y="82" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="499" y="104" fill="var(--accent)">7</text>
              <rect x="516" y="82" width="34" height="34" fill="none" stroke="var(--gold)"/><text x="533" y="104" fill="var(--gold)">10</text>
              <rect x="550" y="82" width="34" height="34" fill="none" stroke="var(--gold)"/><text x="567" y="104" fill="var(--gold)">11</text>
              <rect x="584" y="82" width="34" height="34" fill="none" stroke="var(--gold)"/><text x="601" y="104" fill="var(--gold)">…</text>
            </g>
            <text x="20" y="186" fill="var(--gold)" font-size="12">一維索引 k　↔　(列, 行) = divmod(k, n)</text>
            <text x="20" y="210" fill="var(--text-muted)" font-size="12">k = 5，n = 4 → divmod(5, 4) = (1, 1) → matrix[1][1] = 11 ✔</text>
            <line x1="20" y1="228" x2="620" y2="228" stroke="var(--border)"/>
            <text x="20" y="256" fill="var(--text-muted)" font-size="12">另一種視角（階梯搜尋）：從右上角出發，往左變小、往下變大</text>
            <text x="20" y="280" fill="var(--text-muted)" font-size="12">每一步都能排除「一整列」或「一整行」→ O(m + n)，而且對第 240 題也成立</text>'''

emit({
 "num": 74, "slug": "search-a-2d-matrix",
 "en": [
   "You are given an <code>m x n</code> integer matrix <code>matrix</code> with the following "
   "two properties: each row is sorted in non-decreasing order; the first integer of each row "
   "is greater than the last integer of the previous row.",
   "Given an integer <code>target</code>, return <code>true</code> if <code>target</code> is "
   "in <code>matrix</code> or <code>false</code> otherwise.",
   "You must write a solution in <code>O(log(m * n))</code> time complexity.",
 ],
 "zh": [
   "給你一個 <code>m × n</code> 的整數矩陣，它有兩個性質："
   "（1）<strong>每一列</strong>都是非遞減排序；"
   "（2）<strong>每一列的第一個數，都大於前一列的最後一個數</strong>。",
   "給你一個 <code>target</code>，判斷它在不在矩陣裡。",
   "演算法必須是 <code>O(log(m × n))</code>。",
 ],
 "pre": [
   ("note", "第二個性質是關鍵：整個矩陣「攤平」就是有序的", [
     ("c", """matrix = [[1,  3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]

攤平（逐列接起來）：
    [1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]

    嚴格遞增！

為什麼？
    性質 1 保證「同一列內」遞增
    性質 2 保證「跨列的接縫」也遞增（7 < 10，20 < 23）

所以整個矩陣就是「一個折疊起來的有序陣列」。

一維索引 k  <->  二維座標 (r, c)：
    r, c = divmod(k, n)         一維 -> 二維
    k = r * n + c               二維 -> 一維

    k = 5, n = 4  ->  (1, 1)  ->  matrix[1][1] = 11 ✔

有了這個對應，直接對 [0, m*n-1] 做標準二分搜尋 -> O(log(mn)) ✔"""),
     "<strong>如果沒有性質 2</strong>（每一列的開頭不保證比上一列的結尾大），"
     "那就是第 240 題（Search a 2D Matrix II），"
     "攤平之後<strong>不是有序的</strong>，二分搜尋失效 —— "
     "只能用 O(m+n) 的階梯搜尋。",
   ]),
 ],
 "examples": """範例 1
  輸入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
  輸出：true

範例 2
  輸入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
  輸出：false""",
 "constraints": [
   "<code>m == matrix.length</code>，<code>n == matrix[i].length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 100",
   "−10⁴ ≤ <code>matrix[i][j]</code>, <code>target</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>要求 O(log(mn))</strong> —— "
       "排除了 O(m + n) 的階梯搜尋（雖然在 100 × 100 時也很快）。",
       "<strong>m, n ≥ 1</strong>，所以 <code>matrix[0][0]</code> 一定存在。"
       "但寫上 <code>if not matrix or not matrix[0]</code> 比較安全。",
       "<strong>注意 <code>log(mn) = log m + log n</code></strong> —— "
       "所以「先二分找列，再二分找行」（解法二）也符合要求。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P74_FIG, "0 0 640 294"),
 ],
 "approaches": [
   ap("解法一", "當成一維陣列二分（最推薦）", [
     ("c", S["p74_flat"]),
     ("h", "<code>divmod(mid, n)</code> —— 注意是 <code>n</code> 不是 <code>m</code>"),
     ("c", """一維索引 k 對應 (r, c)：
    r = k // n      （n 是「每一列有幾個元素」= 行數）
    c = k % n

    Python 的 divmod(k, n) 一次給出兩個值。

最常見的錯誤：寫成 divmod(mid, m)。

    matrix 是 3 列 × 4 行（m=3, n=4）
    k = 5 應該對應 (1, 1)

    divmod(5, 4) = (1, 1)  ✔
    divmod(5, 3) = (1, 2)  ✘ 完全錯了

記法：「除以『一列有幾個』得到列號」。
      而「一列有幾個」= 行數 = n。"""),
     "<strong>整個解法就是標準二分搜尋</strong>，只多了一行座標轉換。"
     "<strong>而且它明確地展示了「這個矩陣就是一個有序陣列」這個洞察</strong> —— "
     "面試時這個表達很有力。",
     "<strong>複雜度 O(log(mn))</strong>，剛好符合要求。",
   ], "O(log(m·n))", "O(1)", "一次二分", "幾個變數", optimal=True),

   ap("解法二", "兩次二分（先找列，再找行）", [
     ("c", S["p74_two"]),
     "<strong>複雜度 O(log m + log n) = O(log(mn))</strong>，和解法一相同。",
     ("h", "<code>while ... else</code>"),
     "Python 的 <code>while-else</code>：<code>else</code> 只在「迴圈正常結束（沒 break）」時執行。"
     "這裡用來表達「沒有任何一列涵蓋 target」。"
     "<strong>但這個語法很多人沒看過，面試時建議改成明確的旗標變數。</strong>",
     ("h", "第一次二分的判斷式"),
     ("c", """if matrix[mid][0] <= target <= matrix[mid][n-1]:
    找到了「可能包含 target 的那一列」

if matrix[mid][0] > target:
    這一列的開頭就太大了 -> 往上找

else:
    這一列的結尾還太小 -> 往下找

要小心三個條件是互斥且窮盡的 ——
漏掉一種就會死循環或漏答案。

相較之下，解法一只有「相等／太小／太大」三種，
判斷式更簡單。"""),
     "<strong>優點</strong>：不需要一維／二維的座標轉換，"
     "而且「先定位列，再定位行」的分解很自然。",
     "<strong>缺點</strong>：程式碼長一倍，而且判斷式比較容易寫錯。",
   ], "O(log m + log n)", "O(1)", "兩次二分", "幾個變數"),

   ap("解法三", "從右上角出發的階梯搜尋（對第 240 題也成立）", [
     "完全不同的思路：<strong>從矩陣的「右上角」出發。"
     "往左走數字變小，往下走數字變大 —— "
     "所以每一步都能根據比較結果，排除一整行或一整列。</strong>",
     ("c", S["p74_staircase"]),
     ("c", """matrix = [[1,  3,  5,  7],
          [10, 11, 16, 20],
          [23, 30, 34, 60]]
target = 16

  (0,3) = 7  < 16  ->  這一列（第 0 列）左邊都 <= 7，全部排除 -> r=1
  (1,3) = 20 > 16  ->  這一行（第 3 行）下面都 >= 20，全部排除 -> c=2
  (1,2) = 16 == 16 ->  找到 ✔

每一步排除一整列或一整行，所以最多走 m + n 步。

為什麼一定要從「右上角」（或左下角）？
    右上角是唯一一個「往兩個方向走，值的變化方向相反」的角落：
        往左 -> 變小
        往下 -> 變大

    左上角就不行：往右和往下「都變大」，
    比較結果沒辦法告訴你該走哪邊。
    右下角同理（往左和往上都變小）。

    左下角也可以（往右變大、往上變小），是對稱的選擇。"""),
     ("h", "為什麼這題不該用它（但值得會）"),
     "<strong>複雜度是 O(m + n)，不符合題目要求的 O(log(mn))。</strong>"
     "在 100 × 100 時 O(m+n) = 200 比 O(log(mn)) ≈ 14 慢，但都很快。",
     "<strong>它的價值在於：它不需要「性質 2」。</strong>"
     "<strong>第 240 題</strong>（每列遞增、每行也遞增，但列之間不連續）"
     "沒辦法攤平成有序陣列，二分搜尋完全失效 —— "
     "<strong>而階梯搜尋照樣可以用。</strong>",
     "<strong>所以：本題寫解法一，但要知道解法三，因為它是第 240 題的唯一好解。</strong>",
   ], "O(m + n)", "O(1)", "每步排除一列或一行", "兩個變數"),
 ],
 "compare": (["解法", "時間", "需要「性質 2」？", "第 240 題可用？", "備註"],
   [["一、攤平二分", "O(log(mn))", "✔ 必須", "✘", "本題最佳"],
    ["二、兩次二分", "O(log m + log n)", "✔ 必須", "✘", "同樣達標，較長"],
    ["三、階梯搜尋", "O(m + n)", "✘ 不需要", "✔", "第 240 題的解"]]),
 "edges": [
   "<strong>1 × 1</strong>：<code>([[1]], 1)</code> → true；<code>([[1]], 2)</code> → false。",
   "<strong>只有一列</strong>：<code>([[1,3]], 3)</code> → true。退化成一般的二分搜尋。",
   "<strong>只有一行</strong>：<code>([[1],[3]], 3)</code> → true。",
   "<strong>target 在接縫處</strong>：<code>target = 10</code>（第 1 列的開頭）。"
   "驗證跨列的邏輯。",
   "<strong>target 比全部都小／都大</strong>：<code>target = 0</code> 或 <code>1000</code> → false。",
   "<strong>target 剛好落在兩列之間</strong>：<code>target = 8</code>（7 和 10 之間）→ false。",
   "<strong><code>divmod(mid, m)</code> 的錯誤</strong>："
   "在非正方形矩陣上會完全錯亂。<strong>一定要用 <code>n</code>。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果沒有「每列開頭 &gt; 上一列結尾」這個性質呢？"),
   "那就是<strong>第 240 題</strong>。此時矩陣只保證「每列遞增、每行遞增」，"
   "攤平之後不是有序的：",
   ("c", """[[1, 4, 7],
 [2, 5, 8],
 [3, 6, 9]]

攤平：[1,4,7, 2,5,8, 3,6,9]  -> 不是有序的 ✘

二分搜尋完全失效。

階梯搜尋照樣可用（從右上角 7 開始）：
    7 > 5 -> 往左   4 < 5 -> 往下   5 == 5 ✔

    O(m + n)，而且可以證明這是最優的
    （對抗性論證：任何演算法在最壞情況下都必須看 Ω(m+n) 個元素）。""",),
   ("h", "追問二：如果要找「第 k 小的元素」呢？"),
   "第 378 題（Kth Smallest Element in a Sorted Matrix）。"
   "在本題的條件下（攤平有序）直接取 <code>matrix[k//n][k%n]</code> 就好。"
   "但在第 240 題的條件下，要用<strong>二分答案</strong>："
   "猜一個值 <code>x</code>，用階梯搜尋算出「有幾個元素 ≤ x」，再調整 <code>x</code>。"
   "複雜度 O((m+n) log(值域))。",
   ("h", "追問三：這種「把二維當成一維」的技巧還能用在哪？"),
   ("ul", [
     "<strong>矩陣的線性化儲存</strong>：C 的二維陣列本來就是這樣存的"
     "（row-major order），<code>a[i][j]</code> 編譯後就是 <code>*(a + i*n + j)</code>。",
     "<strong>Union-Find 在網格上</strong>：把 <code>(i,j)</code> 編成 <code>i*n+j</code> 當節點編號。",
     "<strong>位元遮罩表示網格狀態</strong>：第 <code>i*n+j</code> 個位元代表 <code>(i,j)</code>。",
     "<strong>快取友善的走訪順序</strong>：按 row-major 走過陣列，比按 column-major 快好幾倍"
     "（因為記憶體是連續的，而 CPU 一次載入一整條快取行）。",
   ]),
   "<strong>「二維其實是一維的一種看法」是很多效能優化的起點。</strong>",
 ],
 "related": [
   "<strong>第 240 題 Search a 2D Matrix II</strong> —— 沒有性質 2，只能階梯搜尋",
   "<strong>第 378 題 Kth Smallest in a Sorted Matrix</strong> —— 二分答案",
   "<strong>第 35／704 題</strong> —— 一維二分搜尋的基礎",
   "<strong>第 33 題 Search in Rotated Sorted Array</strong> —— 另一種「看起來不能二分但可以」",
 ],
 "check": [
   "<code>divmod(mid, n)</code> 為什麼是除以 <code>n</code> 不是 <code>m</code>？舉一個非正方形的例子。",
   "階梯搜尋為什麼一定要從「右上角」或「左下角」出發？從左上角會怎樣？",
   "如果拿掉「每列開頭 &gt; 上一列結尾」這個性質，三種解法哪些還能用？",
   "本題和第 240 題的最優複雜度分別是多少？為什麼不一樣？",
 ],
})
print("P74 written")
