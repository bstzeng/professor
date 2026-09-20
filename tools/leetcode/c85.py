# -*- coding: utf-8 -*-
"""第 85–88 題。"""
import random, functools
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(85)

# ==================== 85. Maximal Rectangle ====================
S["p85_hist"] = '''class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix[0])
        heights = [0] * n
        best = 0

        for row in matrix:
            # 把「到這一列為止」的連續 1 的高度更新出來
            for j in range(n):
                heights[j] = heights[j] + 1 if row[j] == "1" else 0
            best = max(best, self._largest_rectangle(heights))

        return best

    def _largest_rectangle(self, heights: List[int]) -> int:
        """第 84 題：柱狀圖中最大的矩形"""
        stack = []
        best = 0
        n = len(heights)
        for i in range(n + 1):
            h = heights[i] if i < n else 0
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                best = max(best, height * (i - left - 1))
            stack.append(i)
        return best'''

S["p85_dp"] = '''class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        heights = [0] * n          # 到這一列為止，這一欄連續有幾個 1
        left = [0] * n             # 以這一欄為底的矩形，左邊界最遠能到哪
        right = [n] * n            # 右邊界（開區間）
        best = 0

        for i in range(m):
            cur_left, cur_right = 0, n

            # 高度：由上往下累加
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0

            # 左邊界：由左往右
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            # 右邊界：由右往左
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j

            for j in range(n):
                best = max(best, (right[j] - left[j]) * heights[j])

        return best'''

_p85 = [S.load(k) for k in ("p85_hist", "p85_dp")]


def _p85_ref(matrix):
    """暴力：枚舉所有子矩形。"""
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    best = 0
    for r1 in range(m):
        for r2 in range(r1, m):
            for c1 in range(n):
                for c2 in range(c1, n):
                    if all(matrix[r][c] == "1"
                           for r in range(r1, r2 + 1) for c in range(c1, c2 + 1)):
                        best = max(best, (r2 - r1 + 1) * (c2 - c1 + 1))
    return best


_M = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
      ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
for mat in [_M, [["0"]], [["1"]], [], [[]], [["1", "1"], ["1", "1"]],
            [["0", "1"], ["1", "0"]]]:
    e = _p85_ref(mat)
    for sol in _p85:
        assert sol.maximalRectangle([r[:] for r in mat]) == e, ("P85", mat, sol)
assert _p85[0].maximalRectangle([r[:] for r in _M]) == 6
for _ in range(1500):
    m_, n_ = random.randint(1, 4), random.randint(1, 4)
    mat = [["1" if random.random() < 0.6 else "0" for _ in range(n_)]
           for _ in range(m_)]
    e = _p85_ref(mat)
    for sol in _p85:
        assert sol.maximalRectangle([r[:] for r in mat]) == e, ("P85", mat, sol)
print("P85 solutions OK")

_P85_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">把二維問題「逐列」降成一維：每一列都當成一張柱狀圖，套用第 84 題</text>
            <g font-size="14" text-anchor="middle">
              <text x="110" y="52" fill="var(--text-muted)" font-size="12">matrix</text>
              <rect x="40" y="62" width="34" height="30" fill="var(--accent)" opacity="0.25" stroke="var(--border)"/><text x="57" y="83" fill="var(--text-muted)">1</text>
              <rect x="74" y="62" width="34" height="30" fill="none" stroke="var(--border)"/><text x="91" y="83" fill="var(--text-muted)">0</text>
              <rect x="108" y="62" width="34" height="30" fill="var(--accent)" opacity="0.25" stroke="var(--border)"/><text x="125" y="83" fill="var(--text-muted)">1</text>
              <rect x="142" y="62" width="34" height="30" fill="none" stroke="var(--border)"/><text x="159" y="83" fill="var(--text-muted)">0</text>
              <rect x="176" y="62" width="34" height="30" fill="none" stroke="var(--border)"/><text x="193" y="83" fill="var(--text-muted)">0</text>

              <rect x="40" y="92" width="34" height="30" fill="var(--accent)" opacity="0.25" stroke="var(--border)"/><text x="57" y="113" fill="var(--text-muted)">1</text>
              <rect x="74" y="92" width="34" height="30" fill="none" stroke="var(--border)"/><text x="91" y="113" fill="var(--text-muted)">0</text>
              <rect x="108" y="92" width="34" height="30" fill="var(--accent)" opacity="0.25" stroke="var(--border)"/><text x="125" y="113" fill="var(--text-muted)">1</text>
              <rect x="142" y="92" width="34" height="30" fill="var(--accent)" opacity="0.25" stroke="var(--border)"/><text x="159" y="113" fill="var(--text-muted)">1</text>
              <rect x="176" y="92" width="34" height="30" fill="var(--accent)" opacity="0.25" stroke="var(--border)"/><text x="193" y="113" fill="var(--text-muted)">1</text>

              <rect x="40" y="122" width="34" height="30" fill="#ff8a65" opacity="0.35" stroke="var(--border)"/><text x="57" y="143" fill="var(--text-muted)">1</text>
              <rect x="74" y="122" width="34" height="30" fill="var(--accent)" opacity="0.25" stroke="var(--border)"/><text x="91" y="143" fill="var(--text-muted)">1</text>
              <rect x="108" y="122" width="34" height="30" fill="#ff8a65" opacity="0.35" stroke="var(--border)"/><text x="125" y="143" fill="var(--text-muted)">1</text>
              <rect x="142" y="122" width="34" height="30" fill="#ff8a65" opacity="0.35" stroke="var(--border)"/><text x="159" y="143" fill="var(--text-muted)">1</text>
              <rect x="176" y="122" width="34" height="30" fill="#ff8a65" opacity="0.35" stroke="var(--border)"/><text x="193" y="143" fill="var(--text-muted)">1</text>

              <rect x="40" y="152" width="34" height="30" fill="var(--accent)" opacity="0.25" stroke="var(--border)"/><text x="57" y="173" fill="var(--text-muted)">1</text>
              <rect x="74" y="152" width="34" height="30" fill="none" stroke="var(--border)"/><text x="91" y="173" fill="var(--text-muted)">0</text>
              <rect x="108" y="152" width="34" height="30" fill="none" stroke="var(--border)"/><text x="125" y="173" fill="var(--text-muted)">0</text>
              <rect x="142" y="152" width="34" height="30" fill="var(--accent)" opacity="0.25" stroke="var(--border)"/><text x="159" y="173" fill="var(--text-muted)">1</text>
              <rect x="176" y="152" width="34" height="30" fill="none" stroke="var(--border)"/><text x="193" y="173" fill="var(--text-muted)">0</text>
            </g>
            <g font-family="monospace" font-size="13">
              <text x="250" y="83" fill="var(--text-muted)">heights = [1, 0, 1, 0, 0]</text>
              <text x="470" y="83" fill="var(--text-muted)">最大 1</text>
              <text x="250" y="113" fill="var(--text-muted)">heights = [2, 0, 2, 1, 1]</text>
              <text x="470" y="113" fill="var(--text-muted)">最大 3</text>
              <text x="250" y="143" fill="#ff8a65">heights = [3, 1, 3, 2, 2]</text>
              <text x="470" y="143" fill="#ff8a65">最大 6 ✔</text>
              <text x="250" y="173" fill="var(--text-muted)">heights = [4, 0, 0, 3, 0]</text>
              <text x="470" y="173" fill="var(--text-muted)">最大 4</text>
            </g>
            <line x1="20" y1="198" x2="620" y2="198" stroke="var(--border)"/>
            <text x="20" y="226" fill="var(--gold)" font-size="12">heights[j] 的更新規則：是 &apos;1&apos; 就 +1，是 &apos;0&apos; 就歸零（被切斷了）</text>
            <text x="20" y="250" fill="var(--text-muted)" font-size="12">第 2 列的 [3, 1, 3, 2, 2] 裡，以高度 2 為高、寬度 3（索引 2~4）→ 面積 6</text>
            <text x="20" y="278" fill="var(--text-muted)" font-size="12">總複雜度 O(m × n)：m 列，每列跑一次 O(n) 的單調堆疊</text>'''

emit({
 "num": 85, "slug": "maximal-rectangle",
 "en": [
   "Given a <code>rows x cols</code> binary <code>matrix</code> filled with <code>0</code>'s "
   "and <code>1</code>'s, find the largest rectangle containing only <code>1</code>'s and "
   "<em>return its area</em>.",
 ],
 "zh": [
   "給你一個只含 <code>'0'</code> 和 <code>'1'</code> 的二維矩陣，"
   "找出<strong>只包含 1 的最大矩形</strong>，回傳它的面積。",
 ],
 "pre": [
   ("note", "把二維問題降成一維", [
     ("c", """直接枚舉所有子矩形是 O(m²n²) 甚至更糟。

核心洞察：
    【把每一列都當成一張柱狀圖的「地面」】

    heights[j] = 從這一列往上數，第 j 欄連續有幾個 1

    matrix = 1 0 1 0 0
             1 0 1 1 1
             1 1 1 1 1
             1 0 0 1 0

    第 0 列： heights = [1, 0, 1, 0, 0]
    第 1 列： heights = [2, 0, 2, 1, 1]
    第 2 列： heights = [3, 1, 3, 2, 2]     <- 這一列的柱狀圖最大矩形是 6
    第 3 列： heights = [4, 0, 0, 3, 0]

    更新規則：
        matrix[i][j] == '1'  ->  heights[j] += 1
        matrix[i][j] == '0'  ->  heights[j] = 0     （被切斷了）

    然後對每一列的 heights 跑一次【第 84 題】的演算法。

為什麼這樣不會漏掉答案？
    任何「全是 1 的矩形」，它一定有一個「最下面的那一列」。
    當我們處理到那一列時，那個矩形就會被當成柱狀圖裡的一個矩形算到 ✔

複雜度：m 列 × 每列 O(n) = O(m × n)"""),
     "<strong>這是「降維」最漂亮的例子之一。</strong>"
     "第 84 題是這題的必要前置 —— 沒有先弄懂單調堆疊，這題無從下手。",
   ]),
 ],
 "examples": """範例 1
  輸入：matrix = [["1","0","1","0","0"],
                 ["1","0","1","1","1"],
                 ["1","1","1","1","1"],
                 ["1","0","0","1","0"]]
  輸出：6
  說明：第 1~2 列、第 2~4 欄構成一個 2 × 3 的全 1 矩形。

範例 2
  輸入：matrix = [["0"]]
  輸出：0

範例 3
  輸入：matrix = [["1"]]
  輸出：1""",
 "constraints": [
   "<code>rows == matrix.length</code>，<code>cols == matrix[i].length</code>",
   "1 ≤ <code>row</code>, <code>cols</code> ≤ 200",
   "<code>matrix[i][j]</code> 是 <code>'0'</code> 或 <code>'1'</code>（<strong>字元，不是數字</strong>）",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>格子裡是「字元」不是「整數」</strong>。"
       "要寫 <code>row[j] == \"1\"</code> 而不是 <code>row[j] == 1</code>。"
       "<strong>這個型別錯誤在 Python 裡不會報錯，只會安靜地全部算成 0。</strong>",
       "<strong>200 × 200 = 4 萬格</strong>。O(mn) = 4 萬 —— 瞬間完成。"
       "但 O(m²n²) = 16 億 —— 太慢。",
       "<strong>答案可能是 0</strong>（整個矩陣都是 0）。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P85_FIG, "0 0 640 292"),
 ],
 "approaches": [
   ap("解法一", "逐列轉成柱狀圖 + 第 84 題（最推薦）", [
     ("c", S["p85_hist"]),
     ("h", "為什麼這樣涵蓋了所有可能的矩形？"),
     ("c", """任何一個「全是 1 的矩形」R：
    設它的最下面那一列是第 i 列，左右邊界是 [c1, c2]。

    當我們處理第 i 列時：
        對於 j ∈ [c1, c2]，heights[j] >= R 的高度
        （因為 R 裡那些格子都是 1，往上連續）

    所以在第 i 列的柱狀圖裡，
    存在一個「高 = R 的高度、寬 = c2 - c1 + 1」的矩形。

    第 84 題的演算法會找到它（或更大的）✔

    每個矩形都會在「它的最後一列」被算到，所以不會漏。

（也不會多算 —— 算出來的每個面積都對應一個真實的全 1 矩形。）"""),
     ("h", "<code>heights</code> 的更新是關鍵的一行"),
     ("c", """heights[j] = heights[j] + 1 if row[j] == "1" else 0

    是 '1'：往上的連續 1 又多一個  ->  +1
    是 '0'：這一欄被切斷了        ->  歸零

    「歸零」很重要 —— 它表示「以這一列為底，這一欄一個 1 都沒有」。

    如果寫成 heights[j] += 1 而不歸零，
    就會把被 0 隔開的 1 錯誤地連起來。"""),
     ("h", "為什麼把第 84 題的解法抽成一個方法？"),
     "<strong>因為它就是第 84 題。</strong>"
     "把它獨立出來，這題的主邏輯就只剩 8 行 —— "
     "而且如果第 84 題已經寫過、測過，這裡直接複用，"
     "<strong>出錯的機會大幅降低</strong>。",
     "<strong>「認出這題是另一題的包裝」是面試時最有價值的能力之一</strong> —— "
     "主動說出「這是第 84 題逐列跑一次」會比從頭推導更有說服力。",
   ], "O(m·n)", "O(n)", "m 列 × 每列 O(n)",
      "heights + 堆疊", optimal=True),

   ap("解法二", "純 DP：同時維護高度、左邊界、右邊界", [
     "不用堆疊，改成<strong>對每一欄維護三個量</strong>，逐列遞推。",
     ("c", S["p85_dp"]),
     ("h", "三個陣列的意義"),
     ("c", """對第 i 列的每一欄 j：

  heights[j]  以第 i 列為底，這一欄往上連續有幾個 1
  left[j]     「高度為 heights[j] 的矩形」左邊界最遠能到哪（閉區間）
  right[j]    右邊界（開區間）

  面積 = (right[j] - left[j]) × heights[j]

left 的更新（由左往右掃）：
    cur_left 記錄「這一列上，最近一個 0 的右邊一格」

    matrix[i][j] == '1'：
        left[j] = max(left[j], cur_left)
                  ^上一列的     ^這一列的限制
        取 max 因為「矩形要同時滿足所有列的限制」

    matrix[i][j] == '0'：
        left[j] = 0        重置
        cur_left = j + 1   下一段從 j+1 開始

right 對稱（由右往左掃，取 min）。

為什麼 left 要取 max、right 要取 min？
    因為矩形要「跨越多列」，
    它的左邊界必須 >= 每一列的限制（取最緊的，也就是最大的）
    右邊界必須 <= 每一列的限制（取最小的）

    這是「區間交集」的概念。"""),
     ("h", "為什麼 <code>'0'</code> 時要把 <code>left[j]</code> 設成 0、<code>right[j]</code> 設成 n？"),
     "因為此時 <code>heights[j] = 0</code>，面積一定是 0 —— "
     "<strong>所以 left 和 right 的值不影響答案</strong>。"
     "設成最寬（0 和 n）是為了「重置」，讓下一列從乾淨的狀態開始累積限制。",
     "<strong>優點</strong>：不用堆疊，三個線性掃描，常數小。"
     "<strong>缺點</strong>：三個陣列的語意和更新規則要想很清楚，"
     "而且 <code>cur_left</code>／<code>cur_right</code> 的邊界很容易寫錯。",
     "<strong>面試時寫解法一。</strong>這個版本當作「知道還有另一條路」。",
   ], "O(m·n)", "O(n)", "每列三趟線性掃描", "三個長度 n 的陣列"),
 ],
 "compare": (["解法", "時間", "空間", "依賴第 84 題？", "備註"],
   [["一、逐列 + 單調堆疊", "O(mn)", "O(n)", "✔", "最推薦，複用已知正確的程式碼"],
    ["二、三陣列 DP", "O(mn)", "O(n)", "✘", "不用堆疊，但邊界難推"],
    ["暴力枚舉", "O(m²n²)", "O(1)", "✘", "當基準，會 TLE"]]),
 "edges": [
   "<strong>全是 0</strong>：<code>[[\"0\"]]</code> → 0。",
   "<strong>全是 1</strong>：<code>[[\"1\",\"1\"],[\"1\",\"1\"]]</code> → 4。",
   "<strong>單一格子</strong>：<code>[[\"1\"]]</code> → 1。",
   "<strong>對角線</strong>：<code>[[\"0\",\"1\"],[\"1\",\"0\"]]</code> → 1。"
   "沒有 2×1 或 1×2 的全 1 區塊。",
   "<strong>只有一列</strong>：退化成一維的「最長連續 1」。",
   "<strong>字元 vs 整數</strong>：寫成 <code>row[j] == 1</code> 的話，"
   "<code>heights</code> 永遠是 0，答案永遠是 0。"
   "<strong>這是本題最常見的低級錯誤。</strong>",
   "<strong>空矩陣</strong>：<code>[]</code> 或 <code>[[]]</code> → 0。題目保證不會，但別崩潰。",
 ],
 "follow": [
   ("h", "追問一：如果只要找「最大正方形」呢？"),
   "第 221 題（Maximal Square）。<strong>有一個更簡單的 O(mn) DP</strong>：",
   ("c", """dp[i][j] = 以 (i,j) 為【右下角】的最大正方形邊長

    if matrix[i][j] == '1':
        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    else:
        dp[i][j] = 0

    答案 = max(dp)²

為什麼是三者取 min 加一？
    要讓 (i,j) 當右下角、邊長為 k 的正方形成立，
    必須「上」「左」「左上」三個方向都能支撐 k-1 的正方形。
    取最小的那個 + 1 就是能達成的最大邊長。

「正方形」比「矩形」簡單得多，
因為正方形只有一個自由度（邊長），
而矩形有兩個（長和寬）——
所以矩形需要單調堆疊，正方形只要一個二維 DP。

這是一個很好的對照：
    「多一個自由度」往往讓問題的難度跳一級。""",),
   ("h", "追問二：如果矩陣很大（例如 10⁴ × 10⁴）呢？"),
   "O(mn) = 10⁸ —— 在 C++ 裡勉強，在 Python 裡會 TLE。"
   "<strong>但 O(mn) 已經是下界了</strong>（至少要讀過每一格）。"
   "這時候只能靠常數優化（例如用 numpy 向量化、或用位元運算一次處理 64 欄）。",
   ("h", "追問三：這個「降維」的技巧還能用在哪？"),
   ("c", """「把二維問題固定一個維度，降成一維」是很通用的策略：

  第 85 題  最大矩形        固定「底邊在哪一列」-> 一維柱狀圖
  第 363 題 矩形區域不超過 K 的最大數值和
            固定「上下邊界」-> 一維的「和不超過 K 的最大子陣列」
  最大子矩陣和
            固定「上下邊界」-> 一維的 Kadane（第 53 題）
  第 1074 題 元素和為目標值的子矩陣數目
            固定「上下邊界」-> 一維的「和為 K 的子陣列數」（第 560 題）

共同模式：
    for 上邊界 in ...:
        for 下邊界 in ...:
            把這幾列「壓縮」成一維陣列
            對它跑一維的演算法

    複雜度 O(m² × 一維演算法)

第 85 題比較特別 —— 它只要 O(m)（不是 O(m²)），
因為「柱狀圖」的表示本身就編碼了「上邊界可以往上到哪」的資訊。""",),
 ],
 "related": [
   "<strong>第 84 題 Largest Rectangle in Histogram</strong> —— 本題的必要前置",
   "<strong>第 221 題 Maximal Square</strong> —— 只找正方形，簡單得多",
   "<strong>第 1277 題 Count Square Submatrices</strong> —— 數所有正方形",
   "<strong>第 363／1074 題</strong> —— 同樣是「固定上下邊界降維」",
 ],
 "check": [
   "<code>heights[j]</code> 的更新規則是什麼？為什麼遇到 <code>'0'</code> 要歸零而不是不變？",
   "為什麼「逐列跑第 84 題」不會漏掉任何矩形？",
   "如果把 <code>row[j] == \"1\"</code> 寫成 <code>row[j] == 1</code>，答案會是什麼？",
   "「最大正方形」為什麼比「最大矩形」簡單？",
 ],
})
print("P85 written")

# ==================== 86. Partition List ====================
S["p86"] = '''class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 開兩條新串列：小的放一邊、大的放一邊，最後接起來
        small_head = small = ListNode()
        large_head = large = ListNode()

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large = large.next
            head = head.next

        large.next = None              # 切斷！否則可能留下環
        small.next = large_head.next   # 把「大的那條」接到「小的那條」後面

        return small_head.next'''

S["p86_inplace"] = '''class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 不開新串列的版本：把「小的」一個一個搬到前面
        # （比較難寫，而且不穩定，這裡只當對照）
        dummy = ListNode(0, head)
        prev_small = dummy      # 「小的區段」的最後一個
        prev = dummy

        while prev.next:
            cur = prev.next
            if cur.val < x and prev is not prev_small:
                # 把 cur 從目前的位置摘下來，插到 prev_small 後面
                prev.next = cur.next
                cur.next = prev_small.next
                prev_small.next = cur
                prev_small = cur
                # prev 不動（因為 cur 被摘走了，prev.next 換人了）
            else:
                if cur.val < x:
                    prev_small = cur
                prev = cur

        return dummy.next'''

_p86 = [S.load(k) for k in ("p86", "p86_inplace")]


def _p86_ref(vals, x):
    return [v for v in vals if v < x] + [v for v in vals if v >= x]


for vals, x in [([1, 4, 3, 2, 5, 2], 3), ([2, 1], 2), ([], 1), ([1], 0),
                ([1], 2), ([3, 1], 2), ([1, 2, 3], 0), ([1, 2, 3], 10)]:
    e = _p86_ref(vals, x)
    for sol in _p86:
        g = from_list(sol.partition(to_list(vals), x))
        assert g == e, ("P86", vals, x, sol, g, e)
for _ in range(4000):
    vals = [random.randint(0, 6) for _ in range(random.randint(0, 9))]
    x = random.randint(0, 7)
    e = _p86_ref(vals, x)
    for sol in _p86:
        g = from_list(sol.partition(to_list(vals), x))
        assert g == e, ("P86", vals, x, sol, g, e)
print("P86 solutions OK")

_P86_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">1→4→3→2→5→2，x = 3：分成「小於 3」和「大於等於 3」兩條，再接起來</text>
            <g font-size="14" text-anchor="middle">
              <rect x="60" y="52" width="52" height="34" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="86" y="75" fill="var(--accent)">1</text>
              <rect x="136" y="52" width="52" height="34" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="162" y="75" fill="#ff8a65">4</text>
              <rect x="212" y="52" width="52" height="34" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="238" y="75" fill="#ff8a65">3</text>
              <rect x="288" y="52" width="52" height="34" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="314" y="75" fill="var(--accent)">2</text>
              <rect x="364" y="52" width="52" height="34" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="390" y="75" fill="#ff8a65">5</text>
              <rect x="440" y="52" width="52" height="34" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="466" y="75" fill="var(--accent)">2</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="112" y1="69" x2="132" y2="69"/><line x1="188" y1="69" x2="208" y2="69"/>
              <line x1="264" y1="69" x2="284" y2="69"/><line x1="340" y1="69" x2="360" y2="69"/>
              <line x1="416" y1="69" x2="436" y2="69"/>
            </g>
            <text x="540" y="75" fill="var(--accent)" font-size="11">藍 &lt; 3</text>
            <text x="540" y="95" fill="#ff8a65" font-size="11">橘 ≥ 3</text>
            <line x1="20" y1="110" x2="620" y2="110" stroke="var(--border)"/>
            <g font-size="14" text-anchor="middle">
              <text x="70" y="152" fill="var(--accent)" font-size="12">small</text>
              <rect x="120" y="132" width="52" height="34" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="146" y="155" fill="var(--accent)">1</text>
              <rect x="196" y="132" width="52" height="34" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="222" y="155" fill="var(--accent)">2</text>
              <rect x="272" y="132" width="52" height="34" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="298" y="155" fill="var(--accent)">2</text>
              <text x="70" y="206" fill="#ff8a65" font-size="12">large</text>
              <rect x="120" y="186" width="52" height="34" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="146" y="209" fill="#ff8a65">4</text>
              <rect x="196" y="186" width="52" height="34" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="222" y="209" fill="#ff8a65">3</text>
              <rect x="272" y="186" width="52" height="34" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="298" y="209" fill="#ff8a65">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="172" y1="149" x2="192" y2="149"/><line x1="248" y1="149" x2="268" y2="149"/>
              <line x1="172" y1="203" x2="192" y2="203"/><line x1="248" y1="203" x2="268" y2="203"/>
            </g>
            <path d="M324 149 Q400 149 400 176 Q400 203 324 203" stroke="var(--gold)" stroke-width="2" fill="none" stroke-dasharray="5 4"/>
            <text x="440" y="180" fill="var(--gold)" font-size="12">small.next = large_head.next</text>
            <text x="20" y="252" fill="#ff8a65" font-size="13">結果：1 → 2 → 2 → 4 → 3 → 5　（兩段內部的相對順序都保留了）</text>
            <text x="20" y="280" fill="var(--gold)" font-size="12">最容易漏的一行：large.next = None　—— 不切斷的話會形成環！</text>'''

emit({
 "num": 86, "slug": "partition-list",
 "en": [
   "Given the <code>head</code> of a linked list and a value <code>x</code>, partition it "
   "such that all nodes <strong>less than</strong> <code>x</code> come before nodes "
   "<strong>greater than or equal to</strong> <code>x</code>.",
   "You should <strong>preserve</strong> the original relative order of the nodes in each of "
   "the two partitions.",
 ],
 "zh": [
   "給你一個鏈結串列的頭節點 <code>head</code> 和一個值 <code>x</code>，"
   "請重新排列，讓所有<strong>小於 <code>x</code></strong> 的節點，"
   "都排在<strong>大於或等於 <code>x</code></strong> 的節點前面。",
   "而且要<strong>保留</strong>兩個部分各自原本的相對順序（也就是「穩定」）。",
 ],
 "pre": [
   ("note", "「保留相對順序」= 這是一個穩定的分割", [
     ("c", """1 -> 4 -> 3 -> 2 -> 5 -> 2，x = 3

  小於 3 的（依原順序）： 1, 2, 2
  大於等於 3 的（依原順序）： 4, 3, 5

  答案： 1 -> 2 -> 2 -> 4 -> 3 -> 5

注意：不是排序！4 還是排在 3 前面（原本的順序）。

「穩定」這個要求排除了很多解法：
    - 快速排序的分割（不穩定）
    - 從尾巴往前搬（會反轉順序）

最乾淨的做法：
    【開兩條新串列，掃一遍，各自 append，最後接起來】

    因為 append 天然保持順序，所以穩定性是免費的。"""),
     "<strong>這個「分成兩堆再接起來」的模式，在鏈結串列上特別漂亮</strong> —— "
     "因為串列的「接起來」是 O(1)（改一個指標），"
     "而陣列要 O(n) 的複製。",
   ]),
 ],
 "examples": """範例 1
  輸入：head = [1,4,3,2,5,2], x = 3
  輸出：[1,2,2,4,3,5]

範例 2
  輸入：head = [2,1], x = 2
  輸出：[1,2]""",
 "constraints": [
   "串列節點數在 <code>[0, 200]</code> 範圍內（<strong>可以是空的</strong>）",
   "−100 ≤ <code>Node.val</code> ≤ 100",
   "−200 ≤ <code>x</code> ≤ 200",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong><code>x</code> 的範圍比節點值大</strong>（−200 到 200 vs −100 到 100）—— "
       "所以可能出現「全部都小於 x」或「全部都大於等於 x」的情況。"
       "<strong>那時候其中一條串列會是空的。</strong>",
       "<strong>串列可以是空的</strong> → 回傳 <code>None</code>。",
       "<strong>是「小於」而不是「小於等於」</strong>："
       "等於 <code>x</code> 的節點要放在<strong>後半段</strong>。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P86_FIG, "0 0 640 296"),
 ],
 "approaches": [
   ap("解法一", "兩條串列 + 兩個 dummy（標準解）", [
     ("c", S["p86"]),
     ("h", "為什麼需要兩個 dummy？"),
     ("c", """small_head 和 large_head 是兩個虛擬頭節點。

它們的作用和第 21、19 題一樣：
    「讓第一個節點不再是特例」。

    沒有 dummy 的話，每次 append 都要判斷
    「這是這條串列的第一個嗎？如果是就設 head，否則接在尾巴後面」。

有了 dummy，兩種情況變成同一行：
    small.next = head
    small = small.next

最後回傳 small_head.next（跳過虛擬節點）。

而且 dummy 順便處理了「其中一條是空的」：
    如果沒有任何節點 < x，small_head.next 就是 None，
    small 還是 small_head，
    small.next = large_head.next 直接把大的接上 ✔"""),
     ("h", "<code>large.next = None</code> —— 最容易漏的一行"),
     ("c", """如果不寫這一行，會發生什麼？

    1 -> 4 -> 3 -> 2 -> 5 -> 2，x = 3

    掃完之後：
        small 這條：dummy -> 1 -> 2 -> 2
        large 這條：dummy -> 4 -> 3 -> 5

    但注意！這些是【原本的節點】，指標還沒被完全重設。

    最後一個被放進 small 的節點是 2（原本的最後一個），
    它的 next 本來就是 None ✔

    但最後一個被放進 large 的節點是 5，
    而 5.next 原本指向 2（最後那個節點）——
    而 2 現在在 small 這條裡！

    接起來之後：
        1 -> 2 -> 2 -> 4 -> 3 -> 5 -> 2 -> ...
                  ^                    ^
                  └────────────────────┘  環！

    from_list 會無限迴圈，或 LeetCode 會回報
    「Found cycle in the ListNode」。

所以 large.next = None 是【必須】的。

為什麼 small 那條不用？
    因為 small 的尾巴接下來就會被 small.next = large_head.next 覆寫掉。
    寫了也不會錯，但沒必要。"""),
     ("h", "為什麼是「穩定」的？"),
     "因為我們<strong>按照原本的順序掃過一遍</strong>，"
     "每個節點都 <code>append</code> 到對應的串列尾端。"
     "<code>append</code> 保持插入順序，所以兩段內部的相對順序都不變 ✔",
     "<strong>複雜度 O(n) 時間、O(1) 額外空間</strong>"
     "（兩個 dummy 是常數，節點本身是重用的，沒有建新節點）。",
   ], "O(n)", "O(1)", "掃一遍", "兩個 dummy + 幾個指標", optimal=True),

   ap("解法二", "原地搬移（不開新串列，但難寫很多）", [
     "有些人會想「能不能不開兩條串列？」—— 可以，"
     "<strong>把每個小於 x 的節點摘下來，插到「小的區段」的尾端。</strong>",
     ("c", S["p86_inplace"]),
     "<strong>但它明顯更難寫</strong>：",
     ("ul", [
       "要同時維護 <code>prev</code>（目前掃到哪）和 <code>prev_small</code>（小段的尾巴）",
       "摘除節點之後 <code>prev</code> 不能前進（因為 <code>prev.next</code> 換人了）",
       "要小心「節點已經在正確位置」的情況（<code>prev is prev_small</code>），"
       "否則會把它摘下來再插回原位，造成無窮迴圈",
     ]),
     "<strong>而且空間複雜度完全一樣（都是 O(1)）</strong> —— "
     "解法一的兩個 dummy 只是兩個節點，不是 O(n)。",
     "<strong>所以這個版本沒有任何優勢，只是為了展示「另一條路存在」。</strong>"
     "<strong>面試時寫解法一。</strong>",
   ], "O(n)", "O(1)", "掃一遍", "幾個指標"),
 ],
 "compare": (["解法", "時間", "空間", "好寫程度", "穩定？"],
   [["一、兩條串列", "O(n)", "O(1)", "★★★★★", "✔"],
    ["二、原地搬移", "O(n)", "O(1)", "★★☆☆☆", "✔"]]),
 "edges": [
   "<strong>空串列</strong>：<code>([], 1)</code> → <code>[]</code>。",
   "<strong>全部小於 x</strong>：<code>([1,2,3], 10)</code> → 原樣。"
   "<code>large_head.next</code> 是 <code>None</code>，接上去剛好。",
   "<strong>全部大於等於 x</strong>：<code>([1,2,3], 0)</code> → 原樣。"
   "<code>small_head.next</code> 是 <code>None</code>，"
   "<code>small</code> 還是 <code>small_head</code>，接上大的那條 ✔",
   "<strong>剛好等於 x</strong>：<code>([1], 1)</code> → <code>[1]</code>"
   "（1 不小於 1，所以歸在後半段）。",
   "<strong>只需要交換兩個</strong>：<code>([2,1], 2)</code> → <code>[1,2]</code>。",
   "<strong>忘記 <code>large.next = None</code></strong>："
   "<code>([1,4,3,2,5,2], 3)</code> 會產生一個<strong>環</strong>。"
   "<strong>這是本題唯一真正的陷阱。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果要分成三段（&lt; x、== x、&gt; x）呢？"),
   "開三條串列，最後接起來。"
   "<strong>這就是荷蘭國旗問題（第 75 題）的串列版</strong> —— "
   "但串列版反而更簡單，因為不需要交換，只要 append。",
   ("c", """small = mid = large = 三個 dummy
while head:
    if head.val < x:   接到 small
    elif head.val == x: 接到 mid
    else:              接到 large
    head = head.next

large.next = None
mid_tail.next = large_head.next
small_tail.next = mid_head.next
return small_head.next

陣列版（第 75 題）需要三個指標和小心的交換邏輯，
串列版只要三條串列 —— 這是串列的優勢。""",),
   ("h", "追問二：這和快速排序有什麼關係？"),
   "<strong>這就是 quicksort 的 partition 步驟</strong>（在串列上）。"
   "把它和遞迴組合起來，就是<strong>串列的快速排序</strong>：",
   ("c", """def quicksort_list(head):
    if not head or not head.next:
        return head
    pivot = head.val
    分成 < pivot、== pivot、> pivot 三條
    return concat(quicksort_list(小的), 等於的, quicksort_list(大的))

但實務上串列排序幾乎都用【merge sort】而不是 quicksort，
因為：
    - merge sort 在串列上是 O(1) 額外空間（陣列版要 O(n)）
    - merge sort 穩定
    - quicksort 需要隨機存取來選 pivot（串列做不到），
      而「取第一個當 pivot」在已排序的輸入上會退化成 O(n²)

這就是為什麼 Python 的 sort、Java 的 Collections.sort，
以及第 148 題的標準解，都是 merge sort。""",),
   ("h", "追問三：陣列版呢？"),
   "陣列版的「穩定分割」需要 O(n) 額外空間"
   "（或一個 O(n log n) 的就地穩定分割演算法 —— 相當複雜）。"
   "<strong>串列版的 O(1) 空間是免費的，因為「接起來」不用搬資料。</strong>",
   "<strong>這是鏈結串列相對於陣列最明顯的優勢場景之一。</strong>",
 ],
 "related": [
   "<strong>第 75 題 Sort Colors</strong> —— 陣列版的三路分割",
   "<strong>第 148 題 Sort List</strong> —— 串列的 merge sort",
   "<strong>第 21 題 Merge Two Sorted Lists</strong> —— 同樣用 dummy 組裝串列",
   "<strong>第 328 題 Odd Even Linked List</strong> —— 幾乎一模一樣的「分兩條再接」",
 ],
 "check": [
   "<code>large.next = None</code> 如果漏掉，<code>[1,4,3,2,5,2]</code>、<code>x=3</code> 會發生什麼？",
   "為什麼這個解法天然是「穩定」的？",
   "如果所有節點都小於 <code>x</code>，程式的哪幾行讓它自然正確？",
   "為什麼串列版可以 O(1) 空間，陣列版不行？",
 ],
})
print("P86 written")
