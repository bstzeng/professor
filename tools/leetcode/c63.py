# -*- coding: utf-8 -*-
"""第 63–66 題。"""
import random, math
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(63)

# ==================== 63. Unique Paths II ====================
S["p63_2d"] = '''class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0                      # 起點就被擋住

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0          # 障礙物：走不到，也不能往外傳
                    continue
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]

        return dp[m - 1][n - 1]'''

S["p63_1d"] = '''class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        dp = [0] * n
        dp[0] = 1                         # 起點（若被擋，下面第一輪就會歸零）

        for row in obstacleGrid:
            for j in range(n):
                if row[j] == 1:
                    dp[j] = 0             # 障礙物：這一格歸零
                elif j > 0:
                    dp[j] += dp[j - 1]    # 否則：上面(舊 dp[j]) + 左邊(新 dp[j-1])
        return dp[n - 1]'''

_p63 = [S.load(k) for k in ("p63_2d", "p63_1d")]


def _p63_ref(g):
    m, n = len(g), len(g[0])
    if g[0][0] == 1:
        return 0
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1
    for i in range(m):
        for j in range(n):
            if g[i][j] == 1:
                dp[i][j] = 0
                continue
            if i:
                dp[i][j] += dp[i - 1][j]
            if j:
                dp[i][j] += dp[i][j - 1]
    return dp[m - 1][n - 1]


for g in [[[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 1], [0, 0]], [[1]], [[0]],
          [[1, 0]], [[0, 0], [1, 1], [0, 0]], [[0, 0, 0], [1, 1, 0], [0, 0, 0]]]:
    e = _p63_ref(g)
    for sol in _p63:
        assert sol.uniquePathsWithObstacles([r[:] for r in g]) == e, ("P63", g, sol)
for _ in range(4000):
    m_, n_ = random.randint(1, 5), random.randint(1, 5)
    g = [[1 if random.random() < 0.25 else 0 for _ in range(n_)] for _ in range(m_)]
    e = _p63_ref(g)
    for sol in _p63:
        assert sol.uniquePathsWithObstacles([r[:] for r in g]) == e, ("P63", g, sol)
print("P63 solutions OK")

emit({
 "num": 63, "slug": "unique-paths-ii",
 "en": [
   "You are given an <code>m x n</code> integer array <code>grid</code>. There is a robot "
   "initially located at the <strong>top-left corner</strong>. The robot tries to move to the "
   "<strong>bottom-right corner</strong>. The robot can only move either down or right.",
   "An obstacle and space are marked as <code>1</code> or <code>0</code> respectively in "
   "<code>grid</code>. A path that the robot takes cannot include <strong>any</strong> square "
   "that is an obstacle.",
   "Return <em>the number of possible unique paths</em>.",
 ],
 "zh": [
   "給你一個 <code>m × n</code> 的二維陣列 <code>obstacleGrid</code>，"
   "機器人從<strong>左上角</strong>出發，要走到<strong>右下角</strong>，"
   "每一步只能往下或往右。",
   "格子裡的 <code>1</code> 表示<strong>障礙物</strong>，<code>0</code> 表示空地。"
   "路徑上<strong>不能經過任何障礙物</strong>。",
   "回傳總共有幾種不同的走法。",
 ],
 "pre": [
   ("note", "和第 62 題只差一行", [
     ("c", """第 62 題：dp[i][j] = dp[i-1][j] + dp[i][j-1]

第 63 題：if 是障礙物: dp[i][j] = 0
          else:      dp[i][j] = dp[i-1][j] + dp[i][j-1]

「障礙物 = 0 種走法」這個設定非常漂亮：
    走不到它（0 種），
    而且它也不會把任何走法「傳」給右邊和下面的格子（加 0 等於沒加）。

所以我們不需要特別處理「繞過障礙物」——
只要把它的值設成 0，整張表就會自動正確。

而組合公式（C(m+n-2, m-1)）在這裡完全失效 ——
因為「哪些路徑會被擋住」沒有簡單的封閉形式。
這就是 DP 相對於數學公式的價值：它能吸收任意的局部限制。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
  輸出：2
  說明：3×3 的網格正中間有一個障礙物。
        1. 右 → 右 → 下 → 下
        2. 下 → 下 → 右 → 右

範例 2
  輸入：obstacleGrid = [[0,1],[0,0]]
  輸出：1""",
 "constraints": [
   "<code>m == obstacleGrid.length</code>，<code>n == obstacleGrid[i].length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 100",
   "<code>obstacleGrid[i][j]</code> 是 <code>0</code> 或 <code>1</code>",
 ],
 "mid": [
   ("note", "三個容易踩的邊界", [
     ("ul", [
       "<strong>起點就是障礙物</strong>：<code>[[1]]</code> → 0。"
       "如果直接寫 <code>dp[0][0] = 1</code> 而不檢查，答案會錯。",
       "<strong>終點是障礙物</strong>：答案 0。"
       "這個會被主迴圈自然處理（<code>dp[m-1][n-1]</code> 被設成 0）。",
       "<strong>第一列或第一行中間有障礙物</strong>：<code>[[0,1,0]]</code> → 0。"
       "<strong>障礙物「後面」的格子全部走不到</strong> —— "
       "所以第一列／第一行不能無腦初始化成 1，必須讓 DP 自然算出來。",
     ]),
   ]),
 ],
 "idea": [
   "第 62 題的 DP 骨架完全不變，只加上「障礙物歸零」。"
   "<strong>但初始化要小心</strong>：第 62 題可以把第一列和第一行都設成 1，這題不行。",
 ],
 "approaches": [
   ap("解法一", "二維 DP（把邊界也交給迴圈處理）", [
     ("c", S["p63_2d"]),
     ("h", "為什麼不預先初始化第一列和第一行？"),
     ("c", """第 62 題可以寫 dp = [[1] * n for _ in range(m)]
（第一列和第一行都是 1）。

這題不行，因為障礙物會「切斷」它們：

    grid = [[0, 1, 0]]

    dp[0][0] = 1
    dp[0][1] = 0（障礙物）
    dp[0][2] = dp[0][1] = 0   ← 走不到！

    如果無腦設成 1，dp[0][2] 會是 1 ✘

所以正確的做法是：
    只設 dp[0][0] = 1（起點），
    其餘全部交給主迴圈的 if i > 0 / if j > 0 去累加。

    i == 0 時只會累加 dp[0][j-1]（左邊）
    j == 0 時只會累加 dp[i-1][0]（上面）

    邊界自然就對了，而且障礙物的 0 會正確地往後傳播。

「讓邊界由一般規則自然產生，而不是特別初始化」
是減少 bug 的好習慣。"""),
     ("h", "起點被擋住的特判"),
     "<code>if obstacleGrid[0][0] == 1: return 0</code>。"
     "其實主迴圈也會處理（<code>dp[0][0]</code> 被 <code>continue</code> 前的 "
     "<code>dp[i][j] = 0</code> 蓋掉）—— "
     "但我們在迴圈前就寫了 <code>dp[0][0] = 1</code>，"
     "而迴圈的第一輪 <code>i=0, j=0</code> 會把它改回 0。"
     "<strong>所以其實不特判也對</strong>，但寫出來讓意圖更清楚。",
   ], "O(m·n)", "O(m·n)", "填滿整張表", "dp 表"),

   ap("解法二", "一維 DP（滾動陣列，最推薦）", [
     ("c", S["p63_1d"]),
     ("h", "初始化 <code>dp[0] = 1</code> 的巧妙之處"),
     ("c", """dp = [0] * n
dp[0] = 1

這個 dp 代表「第 -1 列」的狀態 ——
一個虛擬的、在網格上方的列，
只有第 0 欄有 1 條路徑（代表「起點可達」）。

然後第一輪迴圈（處理第 0 列）：
    j=0: row[0] == 0 -> j > 0 不成立 -> dp[0] 保持 1 ✔
         （或 row[0] == 1 -> dp[0] = 0，處理了「起點被擋」）
    j=1: dp[1] += dp[0] = 1
    ...

所以「起點被擋住」這個邊界，被第一輪迴圈自動處理了 ——
不需要任何特判。

這就是為什麼一維版比二維版還短。"""),
     ("h", "三個分支的順序"),
     ("c", """if row[j] == 1:
    dp[j] = 0              障礙物優先，直接歸零
elif j > 0:
    dp[j] += dp[j-1]       非障礙物且不在第一欄：累加左邊
（else: j == 0 且非障礙物 -> dp[0] 保持不變 = 上一列的值）

第三種情況（j == 0）為什麼「保持不變」就對？
    第 0 欄只能從上面來，
    而 dp[0] 此刻正好是「上一列第 0 欄」的值 ✔

    不用寫任何程式碼 —— 這是滾動陣列的自然結果。"""),
     "<strong>O(n) 空間，而且程式碼比二維版還短。</strong>"
     "面試時寫這個版本，並且說明「<code>dp</code> 在迴圈中途同時混合了新舊兩列的值」。",
   ], "O(m·n)", "O(n)", "同上", "一條長度 n 的陣列", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、二維 DP", "O(mn)", "O(mn)", "16", "最直白"],
    ["二、一維 DP", "O(mn)", "O(n)", "11", "更短，邊界自動處理"]]),
 "edges": [
   "<strong>起點是障礙物</strong>：<code>[[1]]</code>、<code>[[1,0]]</code> → 0。",
   "<strong>終點是障礙物</strong>：<code>[[0,0],[0,1]]</code> → 0。",
   "<strong>第一列被切斷</strong>：<code>[[0,1,0]]</code> → 0。"
   "<strong>無腦初始化第一列為 1 會錯。</strong>",
   "<strong>整列被擋住</strong>：<code>[[0,0],[1,1],[0,0]]</code> → 0。",
   "<strong>沒有障礙物</strong>：退化成第 62 題。",
   "<strong>1×1 空網格</strong>：<code>[[0]]</code> → 1。",
   "<strong>繞得過的障礙</strong>：<code>[[0,0,0],[1,1,0],[0,0,0]]</code> → 1（只能從上面繞）。",
 ],
 "follow": [
   ("h", "追問一：為什麼組合公式在這裡失效？"),
   "因為「有幾條路徑被障礙物擋住」沒有簡單的封閉形式。"
   "理論上可以用<strong>容斥原理</strong>（扣掉經過障礙物 A 的、扣掉經過 B 的、加回同時經過 A 和 B 的…），"
   "但障礙物有 k 個時要算 2ᵏ 項 —— 遠不如 DP 的 O(mn)。",
   "<strong>這是一個很好的例子：封閉公式很美，但 DP 更能「吸收」局部的限制。</strong>",
   ("h", "追問二：如果要原地做（不用額外空間）呢？"),
   "可以直接把 <code>obstacleGrid</code> 當成 <code>dp</code> 表用 —— "
   "把障礙物的 1 改成 0，空地填上路徑數。"
   "<strong>但這會破壞輸入</strong>，而且「1 同時代表障礙物和路徑數 1」很容易混淆。"
   "<strong>一維滾動陣列的 O(n) 已經夠好了</strong>，不值得為了 O(1) 犧牲可讀性。",
   ("h", "追問三：如果障礙物很少呢？"),
   "可以用<strong>容斥 + 組合數</strong>：先算總路徑 <code>C(m+n-2, m-1)</code>，"
   "再依序扣掉「第一個碰到的障礙物是第 i 個」的路徑數。"
   "把障礙物排序後，用 <code>f[i] = C(到 i 的路徑) − Σ f[j] × C(從 j 到 i 的路徑)</code> 遞推。"
   "複雜度 O(k²)，k 是障礙物數量。"
   "<strong>當 k ≪ mn 時（例如 10⁹ × 10⁹ 的網格只有 100 個障礙物），這是唯一可行的做法。</strong>",
 ],
 "related": [
   "<strong>第 62 題 Unique Paths</strong> —— 沒有障礙物的版本",
   "<strong>第 64 題 Minimum Path Sum</strong> —— 同一張表，換成求最小值",
   "<strong>第 980 題 Unique Paths III</strong> —— 必須走過所有空格，要用回溯",
 ],
 "check": [
   "為什麼第一列和第一行不能無腦初始化成 1？舉一個會錯的輸入。",
   "一維版的 <code>dp[0] = 1</code> 代表什麼？「起點被擋」是怎麼被自動處理的？",
   "一維版裡 <code>j == 0</code> 且非障礙物時什麼都不做，為什麼是對的？",
   "為什麼組合公式在有障礙物時失效？容斥原理的代價是什麼？",
 ],
})
print("P63 written")

# ==================== 64. Minimum Path Sum ====================
S["p64_1d"] = '''class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [0] * n

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[0][0]
                elif i == 0:
                    dp[j] = dp[j - 1] + grid[i][j]        # 第一列：只能從左邊來
                elif j == 0:
                    dp[j] = dp[j] + grid[i][j]            # 第一行：只能從上面來
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
                    #            ^上面     ^左邊
        return dp[n - 1]'''

S["p64_inplace"] = '''class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # 直接把 grid 當 dp 表用（會破壞輸入，但空間 O(1)）
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[m - 1][n - 1]'''

S["p64_dijkstra"] = '''import heapq

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 對照組：把它當成一般的最短路徑問題（Dijkstra）
        # 正確但沒必要 —— 因為這張圖是 DAG（只能往下往右），DP 就夠了
        m, n = len(grid), len(grid[0])
        dist = [[float("inf")] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        pq = [(grid[0][0], 0, 0)]
        while pq:
            d, r, c = heapq.heappop(pq)
            if (r, c) == (m - 1, n - 1):
                return d
            if d > dist[r][c]:
                continue
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < m and nc < n and d + grid[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = d + grid[nr][nc]
                    heapq.heappush(pq, (dist[nr][nc], nr, nc))

        return dist[m - 1][n - 1]'''

_p64 = [S.load(k) for k in ("p64_1d", "p64_inplace", "p64_dijkstra")]


def _p64_ref(g):
    m, n = len(g), len(g[0])
    d = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                d[i][j] = g[i][j]
            elif i == 0:
                d[i][j] = d[i][j - 1] + g[i][j]
            elif j == 0:
                d[i][j] = d[i - 1][j] + g[i][j]
            else:
                d[i][j] = min(d[i - 1][j], d[i][j - 1]) + g[i][j]
    return d[m - 1][n - 1]


for g in [[[1, 3, 1], [1, 5, 1], [4, 2, 1]], [[1, 2, 3], [4, 5, 6]], [[1]],
          [[1, 2]], [[1], [2]], [[0, 0], [0, 0]]]:
    e = _p64_ref(g)
    for sol in _p64:
        assert sol.minPathSum([r[:] for r in g]) == e, ("P64", g, sol)
for _ in range(3000):
    m_, n_ = random.randint(1, 5), random.randint(1, 5)
    g = [[random.randint(0, 9) for _ in range(n_)] for _ in range(m_)]
    e = _p64_ref(g)
    for sol in _p64:
        assert sol.minPathSum([r[:] for r in g]) == e, ("P64", g, sol)
print("P64 solutions OK")

_P64_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">grid（左）與 dp 表（右）：dp[i][j] = min(上, 左) + grid[i][j]</text>
            <g font-size="15" text-anchor="middle">
              <text x="130" y="52" fill="var(--text-muted)" font-size="12">grid</text>
              <rect x="70" y="64" width="46" height="42" fill="none" stroke="var(--border)"/><text x="93" y="92" fill="var(--text-muted)">1</text>
              <rect x="116" y="64" width="46" height="42" fill="none" stroke="var(--border)"/><text x="139" y="92" fill="var(--text-muted)">3</text>
              <rect x="162" y="64" width="46" height="42" fill="none" stroke="var(--border)"/><text x="185" y="92" fill="var(--text-muted)">1</text>
              <rect x="70" y="106" width="46" height="42" fill="none" stroke="var(--border)"/><text x="93" y="134" fill="var(--text-muted)">1</text>
              <rect x="116" y="106" width="46" height="42" fill="none" stroke="var(--border)"/><text x="139" y="134" fill="var(--text-muted)">5</text>
              <rect x="162" y="106" width="46" height="42" fill="none" stroke="var(--border)"/><text x="185" y="134" fill="var(--text-muted)">1</text>
              <rect x="70" y="148" width="46" height="42" fill="none" stroke="var(--border)"/><text x="93" y="176" fill="var(--text-muted)">4</text>
              <rect x="116" y="148" width="46" height="42" fill="none" stroke="var(--border)"/><text x="139" y="176" fill="var(--text-muted)">2</text>
              <rect x="162" y="148" width="46" height="42" fill="none" stroke="var(--border)"/><text x="185" y="176" fill="var(--text-muted)">1</text>
            </g>
            <text x="250" y="130" fill="var(--gold)" font-size="20" text-anchor="middle">→</text>
            <g font-size="15" text-anchor="middle">
              <text x="380" y="52" fill="var(--text-muted)" font-size="12">dp</text>
              <rect x="320" y="64" width="52" height="42" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="346" y="92" fill="var(--accent)">1</text>
              <rect x="372" y="64" width="52" height="42" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="398" y="92" fill="var(--accent)">4</text>
              <rect x="424" y="64" width="52" height="42" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="450" y="92" fill="var(--accent)">5</text>
              <rect x="320" y="106" width="52" height="42" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="346" y="134" fill="var(--accent)">2</text>
              <rect x="372" y="106" width="52" height="42" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="398" y="134" fill="var(--gold)">7</text>
              <rect x="424" y="106" width="52" height="42" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="450" y="134" fill="var(--gold)">6</text>
              <rect x="320" y="148" width="52" height="42" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="346" y="176" fill="var(--accent)">6</text>
              <rect x="372" y="148" width="52" height="42" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="398" y="176" fill="var(--gold)">8</text>
              <rect x="424" y="148" width="52" height="42" fill="none" stroke="#ff8a65" stroke-width="2.5"/><text x="450" y="176" fill="#ff8a65">7</text>
            </g>
            <text x="20" y="224" fill="var(--text-muted)" font-size="12">dp[1][2] = min(dp[0][2], dp[1][1]) + grid[1][2] = min(5, 7) + 1 = 6</text>
            <text x="20" y="248" fill="var(--text-muted)" font-size="12">dp[2][2] = min(dp[1][2], dp[2][1]) + grid[2][2] = min(6, 8) + 1 = 7</text>
            <text x="20" y="276" fill="#ff8a65" font-size="12">答案 7，對應路徑 1 → 3 → 1 → 1 → 1（往右、右、下、下）</text>'''

emit({
 "num": 64, "slug": "minimum-path-sum",
 "en": [
   "Given a <code>m x n</code> <code>grid</code> filled with non-negative numbers, find a "
   "path from top left to bottom right, which <strong>minimizes</strong> the sum of all "
   "numbers along its path.",
   "<strong>Note:</strong> You can only move either down or right at any point in time.",
 ],
 "zh": [
   "給你一個填滿<strong>非負整數</strong>的 <code>m × n</code> 網格，"
   "找出一條從左上角到右下角的路徑，使路徑上所有數字的<strong>總和最小</strong>，"
   "回傳這個最小總和。",
   "<strong>注意：</strong>每一步只能往下或往右。",
 ],
 "pre": [
   ("note", "和第 62、63 題是同一張表", [
     ("c", """第 62 題： dp[i][j] = dp[i-1][j] + dp[i][j-1]        （數路徑）
第 63 題： 同上，障礙物那格設 0                      （數路徑，有限制）
第 64 題： dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

同一張表、同樣的走訪順序，
只是把「相加」換成「取 min 再加上自己的成本」。

這三題放在一起看，會發現 DP 的本質是：
    1. 定義狀態（dp[i][j] 代表什麼）
    2. 找出轉移（dp[i][j] 怎麼從更小的子問題算出來）
    3. 決定順序（確保算 dp[i][j] 時，它依賴的都已經算好）

「聚合運算」（sum / min / max / count）只是最後一個細節。

同一個骨架還能做：
    最大路徑和      -> 把 min 換成 max
    路徑上的最大值最小化 -> dp = min(max(上, 自己), max(左, 自己))
    有幾條最小路徑   -> 同時維護「最小值」和「達成它的路徑數」"""),
   ]),
 ],
 "examples": """範例 1
  輸入：grid = [[1,3,1],[1,5,1],[4,2,1]]
  輸出：7
  說明：路徑 1 → 3 → 1 → 1 → 1，總和 7。

範例 2
  輸入：grid = [[1,2,3],[4,5,6]]
  輸出：12
  說明：1 → 2 → 3 → 6。""",
 "constraints": [
   "<code>m == grid.length</code>，<code>n == grid[i].length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 200",
   "0 ≤ <code>grid[i][j]</code> ≤ 200",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>值是「非負」的</strong> —— 這一點很重要，"
       "它保證了「走更多格不會變便宜」，所以 DP（甚至 Dijkstra）都適用。"
       "<strong>如果允許負數，而且可以往四個方向走，就可能有負環，最短路徑無定義。</strong>",
       "<strong>m, n ≤ 200</strong>，O(mn) = 4 × 10⁴ —— 瞬間完成。",
       "<strong>值可以是 0</strong>，所以不能用 0 當「還沒算過」的標記。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P64_FIG, "0 0 640 290"),
 ],
 "approaches": [
   ap("解法一", "一維滾動 DP（最推薦）", [
     ("c", S["p64_1d"]),
     ("h", "四個分支，為什麼不能合併？"),
     ("c", """i == 0 and j == 0：起點。沒有「上面」也沒有「左邊」。
i == 0：第一列。只能從左邊來。
j == 0：第一行。只能從上面來。
其他：   兩邊都可以，取 min。

第 62 題可以把第一列和第一行都設成 1 來省掉分支，
但這題的邊界值不是常數（要累加 grid 的值），
所以只能老實分四種情況。

一個常見的簡化技巧：
    把 dp 開成 (m+1) × (n+1)，多一圈「哨兵」，
    值設成 inf（除了 dp[0][1] 或 dp[1][0] 設成 0）。
    這樣 min(上, 左) 在邊界上會自動選到正確的那一邊。

        dp = [[inf] * (n+1) for _ in range(m+1)]
        dp[0][1] = 0        # 讓 dp[1][1] 能算出 grid[0][0]
        for i in 1..m:
            for j in 1..n:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]

    四個分支變成一個。代價是索引要偏移 1，容易搞混。
    兩種寫法各有支持者 —— 挑一個你不會寫錯的。"""),
     ("h", "一維版裡 <code>dp[j]</code> 和 <code>dp[j-1]</code> 分別是什麼？"),
     "處理 <code>(i, j)</code> 時：<code>dp[j]</code> <strong>還沒更新</strong>，"
     "所以是「上一列同欄」= <code>dp[i-1][j]</code>；"
     "<code>dp[j-1]</code> <strong>已經更新</strong>，"
     "所以是「這一列左邊」= <code>dp[i][j-1]</code>。"
     "<strong>和第 62、63 題完全一樣的滾動機制。</strong>",
   ], "O(m·n)", "O(n)", "每格一次", "一條長度 n 的陣列", optimal=True),

   ap("解法二", "原地修改 grid（O(1) 額外空間）", [
     ("c", S["p64_inplace"]),
     "<strong>把輸入的 <code>grid</code> 直接當 <code>dp</code> 表用。</strong>"
     "因為 <code>dp[i][j]</code> 算完之後，<code>grid[i][j]</code> 的原值就不再需要了。",
     "<strong>優點</strong>：完全不用額外空間。",
     "<strong>缺點</strong>：<strong>破壞了輸入</strong>。"
     "在真實的程式裡這通常是不可接受的（呼叫端可能還要用那份資料），"
     "而且會讓函式變得「不可重複呼叫」。",
     "<strong>面試時</strong>：可以提出來，但一定要主動說「這會修改輸入，"
     "如果不允許的話我會用一維滾動陣列，O(n) 空間」。"
     "<strong>主動指出自己解法的副作用，比被面試官抓到好得多。</strong>",
   ], "O(m·n)", "O(1)", "同上", "破壞輸入"),

   ap("解法三", "Dijkstra（對照組：為什麼用不到）", [
     "這題其實是一個「帶權最短路徑」問題，所以 Dijkstra 當然可以解。"
     "但它是<strong>殺雞用牛刀</strong> —— 值得看一眼，理解為什麼不需要。",
     ("c", S["p64_dijkstra"]),
     ("h", "為什麼 DP 就夠了，不需要 Dijkstra？"),
     ("c", """因為這張圖是【有向無環圖（DAG）】，而且有一個「天然的拓撲順序」。

    只能往下或往右
        -> 任何路徑上的 (i+j) 嚴格遞增
        -> 不可能有環
        -> 按 i 由小到大、j 由小到大掃過去，
           就是一個合法的拓撲排序

    在 DAG 上，只要按拓撲順序走一遍，
    每個節點的最短距離在「第一次算到它」時就已經是最終答案了。
    不需要優先佇列去反覆挑「目前最近的節點」。

複雜度比較：
    DP：        O(mn)
    Dijkstra：  O(mn log(mn))   多一個 log，還有堆的常數

什麼時候真的需要 Dijkstra？
    - 可以往四個方向走（有環了）
    - 邊權不同且圖不是 DAG

    例如第 1631 題（Path With Minimum Effort）就必須用 Dijkstra 或二分 + BFS。

結論：
    「DP 是 DAG 上的最短路徑」，
    「Dijkstra 是一般圖上的最短路徑」。
    看到「只能往一個方向走」就該想到 DP。"""),
   ], "O(mn log(mn))", "O(mn)", "優先佇列的額外負擔", "dist 表 + 堆"),
 ],
 "compare": (["解法", "時間", "空間", "破壞輸入？", "備註"],
   [["一、一維滾動 DP", "O(mn)", "O(n)", "✘", "面試預設"],
    ["二、原地 DP", "O(mn)", "O(1)", "✔", "要主動說明副作用"],
    ["三、Dijkstra", "O(mn log mn)", "O(mn)", "✘", "殺雞用牛刀，但理解它的差別很有價值"]]),
 "edges": [
   "<strong>1 × 1</strong>：<code>[[1]]</code> → 1。",
   "<strong>只有一列</strong>：<code>[[1,2]]</code> → 3。只能一直往右。",
   "<strong>只有一行</strong>：<code>[[1],[2]]</code> → 3。",
   "<strong>全是 0</strong>：<code>[[0,0],[0,0]]</code> → 0。不能用 0 當哨兵。",
   "<strong>最小路徑不是「貪婪地每步選小的」</strong>："
   "<code>[[1,3,1],[1,5,1],[4,2,1]]</code> 的第一步，"
   "往右（3）比往下（1）貴，但正確答案走的是往右。"
   "<strong>貪婪在這題行不通 —— 這正是需要 DP 的理由。</strong>",
   "<strong>200 × 200 全是 200</strong>：答案 <code>399 × 200 = 79800</code>。不會溢位。",
 ],
 "follow": [
   ("h", "追問一：如果要回傳「那條路徑」而不只是總和？"),
   "兩種做法：",
   ("ul", [
     "<strong>記 parent</strong>：算 <code>dp[i][j]</code> 時記下它是從上面還是左邊來的，"
     "最後從終點回溯。需要 O(mn) 空間。",
     "<strong>從 dp 表反推</strong>：從 <code>(m-1, n-1)</code> 開始，"
     "比較 <code>dp[i-1][j]</code> 和 <code>dp[i][j-1]</code>，"
     "誰小就往誰走。不用額外空間，但需要完整的二維 dp 表（不能用滾動陣列）。",
   ]),
   ("h", "追問二：如果要求「最大路徑和」呢？"),
   "把 <code>min</code> 換成 <code>max</code>。<strong>一個字的差別。</strong>"
   "（但如果值可以是負的，「最大」和「最小」的難度就不對稱了 —— 見下一個追問。）",
   ("h", "追問三：如果值可以是負的呢？"),
   "<strong>只能往下往右的話，DP 完全不受影響</strong>（還是 DAG，沒有環）。"
   "但如果可以往四個方向走，負權就可能造成<strong>負環</strong>，最短路徑無定義。"
   "此時 Dijkstra 也不能用（它要求非負權），"
   "要改用 <strong>Bellman-Ford</strong>（能偵測負環）。",
   "<strong>「非負」這個條件，正是 Dijkstra 和很多貪婪演算法的前提。</strong>",
   ("h", "追問四：如果要「最小化路徑上的最大值」呢？"),
   "轉移式換成 <code>dp[i][j] = min(max(dp[i-1][j], grid[i][j]), max(dp[i][j-1], grid[i][j]))</code>。"
   "<strong>同一張表，換一個聚合運算。</strong>"
   "這類問題叫做「瓶頸最短路徑（bottleneck shortest path）」，"
   "在網路頻寬、登山路線規劃裡都有應用。"
   "（第 1631 題是它的四方向版本，要用 Dijkstra 或二分搜尋 + BFS。）",
 ],
 "related": [
   "<strong>第 62／63 題 Unique Paths</strong> —— 同一張表，換成計數",
   "<strong>第 120 題 Triangle</strong> —— 三角形上的同一種 DP",
   "<strong>第 931 題 Minimum Falling Path Sum</strong> —— 三個來源方向",
   "<strong>第 1631 題 Path With Minimum Effort</strong> —— 四方向 + 瓶頸，要 Dijkstra",
 ],
 "check": [
   "為什麼「每一步都選比較小的那一格」（貪婪）在這題行不通？舉範例 1 的第一步說明。",
   "一維版裡 <code>dp[j]</code> 和 <code>dp[j-1]</code> 分別對應二維表的哪一格？",
   "為什麼這題用 DP 就夠，不需要 Dijkstra？關鍵性質是什麼？",
   "如果改成「最小化路徑上的最大值」，轉移式要怎麼寫？",
 ],
})
print("P64 written")
