# -*- coding: utf-8 -*-
"""第 118–121 題。"""
import random, math
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(118)

# ==================== 118. Pascal's Triangle ====================
S["p118"] = '''class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)             # 先全填 1，兩端就不用特判
            for j in range(1, i):           # 中間的才要算（j 從 1 到 i-1）
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res'''

S["p118_shift"] = '''class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res, row = [], [1]
        for _ in range(numRows):
            res.append(row)
            # 把這一列左移一格、右移一格，逐項相加 -> 下一列
            row = [a + b for a, b in zip([0] + row, row + [0])]
        return res'''

S["p118_comb"] = '''import math

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 第 i 列第 j 項就是組合數 C(i, j)
        return [[math.comb(i, j) for j in range(i + 1)] for i in range(numRows)]'''


def _p118_ref(n):
    return [[math.comb(i, j) for j in range(i + 1)] for i in range(n)]


_p118 = [S.load(k) for k in ("p118", "p118_shift", "p118_comb")]
for n in range(0, 40):
    want = _p118_ref(n)
    for sol in _p118:
        assert sol.generate(n) == want, ("P118", n, sol)
assert _p118[0].generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
print("P118 solutions OK")

_P118_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">每一項 = 上一列的「左上」加「右上」。兩端沒有上鄰居，所以永遠是 1。</text>
            <g font-size="14" text-anchor="middle">
              <text x="320" y="58" fill="var(--gold)">1</text>
              <text x="290" y="96" fill="var(--gold)">1</text><text x="350" y="96" fill="var(--gold)">1</text>
              <text x="260" y="134" fill="var(--gold)">1</text><text x="320" y="134" fill="var(--accent)">2</text><text x="380" y="134" fill="var(--gold)">1</text>
              <text x="230" y="172" fill="var(--gold)">1</text><text x="290" y="172" fill="var(--accent)">3</text><text x="350" y="172" fill="var(--accent)">3</text><text x="410" y="172" fill="var(--gold)">1</text>
              <text x="200" y="210" fill="var(--gold)">1</text><text x="260" y="210" fill="var(--accent)">4</text><text x="320" y="210" fill="#ff8a65">6</text><text x="380" y="210" fill="var(--accent)">4</text><text x="440" y="210" fill="var(--gold)">1</text>
            </g>
            <g stroke="#ff8a65" stroke-width="1.5">
              <line x1="285" y1="180" x2="313" y2="200"/><line x1="355" y1="180" x2="327" y2="200"/>
            </g>
            <text x="480" y="210" fill="#ff8a65" font-size="12" text-anchor="start">6 = 3 + 3</text>
            <line x1="20" y1="238" x2="620" y2="238" stroke="var(--border)"/>
            <text x="20" y="264" fill="var(--accent)" font-size="12">第 i 列第 j 項就是組合數 C(i, j)：「從 i 個東西裡選 j 個」有幾種選法。</text>
            <text x="20" y="290" fill="var(--text-muted)" font-size="12">為什麼？從頂端走到 (i, j) 的路徑數 —— 每一步往左下或往右下，走 i 步、其中 j 步往右下。</text>
            <text x="20" y="316" fill="var(--text-muted)" font-size="12">而 C(i, j) = C(i-1, j-1) + C(i-1, j) 正是「最後一步從哪裡來」的分解 —— 就是這個三角形的遞迴式。</text>
            <text x="20" y="346" fill="var(--gold)" font-size="12">「移位相加」的寫法：[0]+row 和 row+[0] 逐項相加，一行就生出下一列。</text>
            <text x="40" y="372" fill="var(--text-muted)" font-size="12">row = [1,3,3,1]　→　[0,1,3,3,1] + [1,3,3,1,0]　→　[1,4,6,4,1] ✔</text>'''

emit({
 "num": 118, "slug": "pascals-triangle",
 "en": [
   "Given an integer <code>numRows</code>, return the first <code>numRows</code> of "
   "<strong>Pascal's triangle</strong>.",
   "In <strong>Pascal's triangle</strong>, each number is the sum of the two numbers directly "
   "above it.",
 ],
 "zh": [
   "給你一個整數 <code>numRows</code>，回傳<strong>楊輝三角</strong>（Pascal's triangle）"
   "的前 <code>numRows</code> 列。",
   "在楊輝三角裡，<strong>每個數字都等於它正上方兩個數字的和</strong>。",
 ],
 "examples": """範例 1
  輸入：numRows = 5
  輸出：[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

              1
             1 1
            1 2 1
           1 3 3 1
          1 4 6 4 1

範例 2
  輸入：numRows = 1
  輸出：[[1]]""",
 "constraints": [
   "1 ≤ <code>numRows</code> ≤ 30",
 ],
 "idea": [
   ("fig", _P118_FIG, "0 0 640 390"),
   ("c", """遞迴式：
    row[i][0] = row[i][i] = 1                     兩端永遠是 1
    row[i][j] = row[i-1][j-1] + row[i-1][j]       中間的是左上 + 右上

實作技巧：【先把整列填成 1，再回頭改中間的】

    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = res[i-1][j-1] + res[i-1][j]

    這樣兩端就完全不用特判 ✔

    注意 range(1, i) 而不是 range(1, i+1) ——
    第 i 列有 i+1 個元素（索引 0..i），
    要改的是索引 1..i-1。

        i = 0: range(1,0) 空 -> [1] ✔
        i = 1: range(1,1) 空 -> [1,1] ✔
        i = 2: range(1,2) -> 改 row[1] -> [1,2,1] ✔

【「先填預設值、再改需要改的」是避免邊界特判的通用技巧。】

複雜度：
    第 i 列有 i+1 個元素，總共 1+2+...+n = O(n²) 個數字。
    【這是輸出的大小，所以 O(n²) 是下界 —— 不可能更快。】"""),
 ],
 "approaches": [
   ap("解法一", "逐列遞推（標準答案）", [
     ("c", S["p118"]),
     "<strong>五行。<code>[1] * (i+1)</code> 這一手省掉了所有邊界判斷。</strong>",
     "<strong>時間 O(n²)、空間 O(n²)</strong>（就是輸出本身）。"
     "<strong>n ≤ 30，所以最多 465 個數字。</strong>",
   ], "O(n²)", "O(n²)", "輸出的大小", "輸出本身", optimal=True),

   ap("解法二", "移位相加（Python 最漂亮的寫法）", [
     ("c", S["p118_shift"]),
     ("h", "一行生出下一列"),
     ("c", """row = [a + b for a, b in zip([0] + row, row + [0])]

    [0] + row  =  把這一列往【右】推一格（左邊補 0）
    row + [0]  =  把這一列往【左】推一格（右邊補 0）

    逐項相加，就是「左上 + 右上」✔

    驗證 row = [1, 3, 3, 1]：
        [0, 1, 3, 3, 1]
      + [1, 3, 3, 1, 0]
      = [1, 4, 6, 4, 1] ✔

    而且長度自動加一 ✔
    兩端也自動是 1（0 加上原本的 1）✔

    【零個特判。】"""),
     ("h", "★ 注意「先 append 再遞推」的順序"),
     ("c", """res, row = [], [1]
for _ in range(numRows):
    res.append(row)                  # 先把目前這一列收下
    row = [a + b for ...]            # 再算出下一列

【順序反過來就錯了】：

    res, row = [], []
    for _ in range(numRows):
        row = [a+b for a,b in zip([0]+row, row+[0])]
        res.append(row)

    第一輪：row = []
        [0] + [] = [0]
        [] + [0] = [0]
        zip([0], [0]) -> [(0, 0)]
        -> row = [0]     ✘ 應該是 [1]

    整個三角形會從 [0] 開始，全部錯掉。

    要讓它對，初始值必須是 row = [1]，
    而且【要先收下再遞推】。

【這是「漂亮的一行式」最典型的風險】：

    邏輯本身沒問題，但邊界（第一輪）要另外想清楚。
    一行式把迴圈的骨架壓縮掉了，
    連帶也把「第一輪長什麼樣」藏了起來。

    【寫完一行式，一定要手算 n = 0, 1, 2 三個情況。】

    這一段不是在勸你別寫一行式 ——
    而是提醒：越短的程式碼，越需要邊界驗算。"""),
     "<strong>複雜度和解法一完全相同</strong>，"
     "<strong>而且不需要回頭去查 <code>res[i-1]</code>。</strong>",
   ], "O(n²)", "O(n²)", "輸出的大小", "輸出本身"),

   ap("解法三", "直接算組合數", [
     ("c", S["p118_comb"]),
     ("c", """第 i 列第 j 項 = C(i, j)

    為什麼？

    從三角形頂端走到位置 (i, j)：
        每一步往左下或往右下，共走 i 步，
        其中恰好 j 步往右下。

        路徑數 = C(i, j) ✔

    而「每個數是上面兩個的和」正是
        C(i, j) = C(i-1, j-1) + C(i-1, j)
    這個遞迴式（帕斯卡法則）。

    證明：從 i 個東西選 j 個，
        分成「有沒有選第 i 個」兩種情況：
            選了 -> 從剩下 i-1 個選 j-1 個 -> C(i-1, j-1)
            沒選 -> 從剩下 i-1 個選 j 個   -> C(i-1, j)

【「選或不選」的分解 —— 和 01 背包、
  第 115 題（不同子序列）是完全一樣的思路。】""",),
     "<strong>一行，但 <code>math.comb</code> 每次呼叫要 O(j) 時間</strong>，"
     "<strong>總共 O(n³)</strong> —— <strong>比遞推慢，但 n ≤ 30 完全無所謂。</strong>",
     "<strong>價值在於它點出了「這個三角形就是組合數表」這件事。</strong>",
   ], "O(n³)", "O(n²)", "每次 comb 是 O(j)", "輸出本身"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、逐列遞推", "O(n²)", "O(n²)", "5", "標準答案"],
    ["二、移位相加", "O(n²)", "O(n²)", "6", "不用回查上一列"],
    ["三、組合數", "O(n³)", "O(n²)", "1", "點出數學意義"]]),
 "edges": [
   "<strong><code>numRows = 1</code></strong> → <code>[[1]]</code>。",
   "<strong><code>numRows = 0</code></strong>（題目保證不會）→ <code>[]</code>。三種解法都自然正確。",
   "<strong><code>range(1, i)</code> 寫成 <code>range(1, i+1)</code></strong> → "
   "<strong><code>res[i-1][i]</code> 索引越界。</strong>",
   "<strong>沒有先填 1 就直接算</strong> → 兩端要特判，容易漏。",
   "<strong><code>numRows = 30</code></strong> → 最大的數是 C(29,14) = 77558760，"
   "<strong>遠小於 2³¹，不會溢位。</strong>",
   "<strong>移位版初始值寫成 <code>row = []</code>、或先遞推再 append</strong> → "
   "<strong>第一列會變成 <code>[0]</code>，整個三角形全錯。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果只要「第 k 列」呢？"),
   "<strong>第 119 題</strong>。可以只用 <code>O(k)</code> 空間 —— "
   "<strong>在一個陣列上倒著更新</strong>，或<strong>直接用乘除算組合數</strong>。",
   ("h", "追問二：楊輝三角還有哪些性質？"),
   ("c", """  第 i 列的和 = 2^i             （二項式定理：(1+1)^i）
  第 i 列的交錯和 = 0 (i>0)     （(1-1)^i = 0）
  沿對角線加 = 費氏數列
  第 i 列所有數的 gcd：i 是質數時，中間各項都被 i 整除
  對 2 取模後畫出來 = 謝爾賓斯基三角形（碎形！）
  第 i 列的最大值在中間，約為 2^i / sqrt(πi/2)

【最後一條是史特林近似的應用】——
    它解釋了為什麼 C(2n,n) 大約是 4^n / sqrt(πn)，
    也就是第 96 題卡塔蘭數的漸進大小。

  「對 2 取模是碎形」這件事特別有趣：
    C(i,j) 是奇數 ⟺ j 的二進位是 i 的二進位的「子集」
    （Kummer 定理 / Lucas 定理）""",),
   ("h", "追問三：如果 <code>numRows</code> 很大（例如 10⁵）呢？"),
   "<strong>輸出本身就有 <code>10¹⁰</code> 個數字 —— 不可能存下來。</strong>",
   "<strong>那時題目一定會改成「只要第 k 列」或「只要某一項」</strong>，"
   "<strong>而且會要求對某個質數取模</strong>（否則數字本身就是天文數字）。"
   "<strong>取模之後就可以用 Lucas 定理在 O(log n) 內算單一項。</strong>",
   ("h", "追問四：「路徑數」的解釋能推廣嗎？"),
   "<strong>能 —— 那就是第 62 題（不同路徑）</strong>："
   "<strong>m×n 網格從左上走到右下的路徑數 = C(m+n-2, m-1)</strong>。",
   "<strong>楊輝三角本質上就是「把網格旋轉 45 度」</strong>。"
   "<strong>第 62、63、118、119 題是同一個東西的四種包裝。</strong>",
 ],
 "related": [
   "<strong>第 119 題 Pascal's Triangle II</strong> —— 只要第 k 列，O(k) 空間",
   "<strong>第 62 題 Unique Paths</strong> —— 同一個組合數，換成網格",
   "<strong>第 96 題 Unique Binary Search Trees</strong> —— 卡塔蘭數也是組合數",
   "<strong>第 115 題 Distinct Subsequences</strong> —— 同樣的「選或不選」分解",
 ],
 "check": [
   "為什麼 <code>range(1, i)</code> 而不是 <code>range(1, i+1)</code>？",
   "「先填 1 再改中間」省掉了什麼特判？",
   "第 i 列第 j 項為什麼等於 C(i, j)？請用「路徑數」解釋。",
   "這題的時間複雜度為什麼不可能低於 O(n²)？",
 ],
})
print("P118 written")

# ==================== 119. Pascal's Triangle II ====================
S["p119_back"] = '''class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            # 【倒著走】：row[j] 要用到 row[j-1] 的「上一列」的值
            for j in range(i - 1, 0, -1):
                row[j] += row[j - 1]
        return row'''

S["p119_shift"] = '''class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [a + b for a, b in zip([0] + row, row + [0])]
        return row'''

S["p119_mul"] = '''class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # C(n, k) = C(n, k-1) * (n - k + 1) / k，一路乘除算過去
        row = [1]
        n = rowIndex
        for k in range(1, n + 1):
            row.append(row[-1] * (n - k + 1) // k)
        return row'''


def _p119_ref(k):
    return [math.comb(k, j) for j in range(k + 1)]


_p119 = [S.load(k) for k in ("p119_back", "p119_shift", "p119_mul")]
for k in range(0, 60):
    want = _p119_ref(k)
    for sol in _p119:
        assert sol.getRow(k) == want, ("P119", k, sol)
assert _p119[0].getRow(3) == [1, 3, 3, 1]
print("P119 solutions OK")

emit({
 "num": 119, "slug": "pascals-triangle-ii",
 "en": [
   "Given an integer <code>rowIndex</code>, return the <code>rowIndex</code><sup>th</sup> "
   "(<strong>0-indexed</strong>) row of the <strong>Pascal's triangle</strong>.",
   "In <strong>Pascal's triangle</strong>, each number is the sum of the two numbers directly "
   "above it.",
   "<strong>Follow up:</strong> Could you optimize your algorithm to use only "
   "<code>O(rowIndex)</code> extra space?",
 ],
 "zh": [
   "給你一個整數 <code>rowIndex</code>，回傳楊輝三角的<strong>第 <code>rowIndex</code> 列</strong>"
   "（<strong>從 0 開始算</strong>）。",
   "<strong>進階：</strong>你能只用 <code>O(rowIndex)</code> 額外空間嗎？",
 ],
 "pre": [
   ("note", "★ 這題的唯一考點：倒著更新", [
     ("c", """如果照第 118 題那樣做，要存整個三角形 -> O(k²) 空間。

    進階要求只用 O(k) —— 也就是【只保留一列，原地更新】。

【但原地更新有陷阱】：

    row[j] = row[j-1] + row[j]
             ^^^^^^^^   ^^^^^^
             需要「上一列」的值

    正著走（j 從小到大）：
        更新 row[1] 時用 row[0]  -> row[0] 永遠是 1，沒問題
        更新 row[2] 時用 row[1]  -> row[1] 【已經被這一輪改掉了】✘

        row = [1,1,1]，要變成 [1,2,1]
        正著走：row[1] += row[0] -> [1,2,1]
                row[2] += row[1] -> [1,2,3]  ✘ 應該是 [1,2,1]

    倒著走（j 從大到小）：
        更新 row[2] 時用 row[1]  -> 還沒改 ✔
        更新 row[1] 時用 row[0]  -> 還沒改 ✔

        row = [1,1,1]
        倒著走：row[2] += row[1] -> [1,1,2]
                row[1] += row[0] -> [1,2,2]

        咦，這也不對？

    ...因為 row 一開始就全填 1 了，
    而第 2 列（i=2）只需要改 row[1]：

        for j in range(i-1, 0, -1)  ->  i=2 時 range(1,0,-1) = [1]
        row[1] += row[0] -> [1,2,1] ✔

    【內層迴圈的上界是 i-1，不是 len(row)-1。】
    因為第 i 列只有前 i+1 個是有效的，
    而其中只有索引 1..i-1 需要更新。

【這個「倒著走」和第 115 題（不同子序列）、
  01 背包是完全同一件事。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：rowIndex = 3
  輸出：[1,3,3,1]

範例 2
  輸入：rowIndex = 0
  輸出：[1]

範例 3
  輸入：rowIndex = 1
  輸出：[1,1]""",
 "constraints": [
   "0 ≤ <code>rowIndex</code> ≤ 33",
 ],
 "mid": [
   ("note", "為什麼上限是 33？", [
     ("c", """第 33 列的最大值是 C(33, 16) = 1166803110

    C(34, 17) = 2333606220  >  2^31 - 1 = 2147483647   溢位！

所以 rowIndex <= 33 是為了讓所有數字都裝得進
32 位元有號整數。

【和第 96 題的 n <= 19、第 70 題的 n <= 45 是同一種考量。】

    看到這種「奇怪的上限」，
    反射動作應該是「這大概是為了不溢位」。

Python 的整數無限大，所以不受影響 ——
但解法三（乘除法）在其他語言裡要特別小心：
    【必須先乘後除】，而且中間值可能接近上限。""",),
   ]),
 ],
 "idea": [
   ("c", """三條路：

【A. 原地倒著更新】（解法一）
    只用一個長度 k+1 的陣列，倒著走避免覆蓋。
    O(k²) 時間、O(k) 空間 ✔ 滿足進階。

【B. 移位相加】（解法二）
    每次造一條新的 list（第 118 題的解法二）。
    O(k²) 時間，但空間嚴格說是 O(k) ——
    因為同時只有兩條 list 存在（舊的會被回收）。

【C. 直接用組合數遞推】（解法三）
    C(n, k) = C(n, k-1) × (n - k + 1) / k

    一路乘除算過去，O(k) 時間、O(k) 空間（就是輸出）。

    【這是唯一一個 O(k) 時間的解法】——
    比要求的 O(k²) 還快一個數量級。"""),
 ],
 "approaches": [
   ap("解法一", "原地倒著更新（滿足進階要求）", [
     ("c", S["p119_back"]),
     ("h", "兩個迴圈的邊界"),
     ("c", """for i in range(2, rowIndex + 1):        # 從第 2 列開始
    for j in range(i - 1, 0, -1):      # j 從 i-1 倒數到 1

    為什麼 i 從 2 開始？
        第 0 列 [1]、第 1 列 [1,1] 都不用改
        （全 1 就是答案）。

    為什麼 j 的上界是 i-1？
        第 i 列有 i+1 個元素（索引 0..i），
        兩端是 1 不用改，所以要改的是 1..i-1。

    為什麼 j 的下界是 1（不含 0）？
        row[0] 永遠是 1。

    驗算 rowIndex = 3：
        初始 row = [1,1,1,1]
        i=2: j=1  -> row[1] += row[0] -> [1,2,1,1]
        i=3: j=2  -> row[2] += row[1] -> [1,2,3,1]
             j=1  -> row[1] += row[0] -> [1,3,3,1] ✔"""),
     "<strong>O(k²) 時間、O(k) 空間（除了輸出之外是 O(1)）。</strong>"
     "<strong>這就是進階要求的答案。</strong>",
   ], "O(k²)", "O(k)", "兩層迴圈", "只有一列"),

   ap("解法二", "移位相加（最短）", [
     ("c", S["p119_shift"]),
     "<strong>四行。和第 118 題的解法二完全一樣，只是不收集中間結果。</strong>",
     "<strong>注意初始值是 <code>row = [1]</code> 而不是 <code>[]</code></strong> —— "
     "<strong>同樣的邊界陷阱。</strong>",
     "<strong>迴圈跑 <code>rowIndex</code> 次</strong>（不是 <code>rowIndex + 1</code>）—— "
     "因為初始的 <code>[1]</code> 就已經是第 0 列了。",
     ("c", """空間嚴格說是多少？

    每一輪都建立一條新的 list，
    但舊的立刻失去參考、會被回收。

    所以【同時存在的記憶體】是 O(k) ✔

    不過它確實比解法一多了「配置 + 回收」的成本，
    在極端在意效能的場合（k 很大）會有差別。

    對 k <= 33 來說完全無所謂。""",),
   ], "O(k²)", "O(k)", "每輪建一條新 list", "同時兩條列"),

   ap("解法三", "組合數遞推（O(k) 時間，最快）", [
     ("c", S["p119_mul"]),
     ("h", "推導 <code>C(n,k) = C(n,k-1) × (n-k+1) / k</code>"),
     ("c", """C(n, k)     = n! / (k! (n-k)!)
C(n, k-1)   = n! / ((k-1)! (n-k+1)!)

    C(n,k) / C(n,k-1)
      = [(k-1)! (n-k+1)!] / [k! (n-k)!]
      = (n-k+1) / k                       ✔

驗算 n = 4：
    C(4,0) = 1
    C(4,1) = 1 × (4-1+1)/1 = 4/1 = 4      ✔
    C(4,2) = 4 × (4-2+1)/2 = 4×3/2 = 6    ✔
    C(4,3) = 6 × (4-3+1)/3 = 6×2/3 = 4    ✔
    C(4,4) = 4 × (4-4+1)/4 = 4×1/4 = 1    ✔

【★ 必須先乘後除】：

    row[-1] * (n - k + 1) // k     ✔
    row[-1] // k * (n - k + 1)     ✘ 餘數會被丟掉

    為什麼先乘後除一定整除？
        因為 C(n,k-1) × (n-k+1) = C(n,k) × k，
        而 C(n,k) 是整數 -> 左邊一定被 k 整除 ✔

    【這和第 96 題（卡塔蘭數遞推）、
      第 62 題（手算組合數）的注意事項一模一樣。】"""),
     "<strong>O(k) 時間 —— 只跑一個迴圈。</strong>"
     "<strong>比進階要求的 O(k²) 還快。</strong>",
     "<strong>但要注意中間值</strong>：<code>row[-1] * (n-k+1)</code> "
     "可能比最終答案大一個因子 <code>k</code>。"
     "<strong>在 C++ / Java 裡 <code>rowIndex = 33</code> 時這個中間值會超過 "
     "<code>int</code>，必須用 <code>long long</code>。</strong>",
   ], "O(k)", "O(k)", "一個迴圈", "輸出本身", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "中間值會溢位嗎", "備註"],
   [["一、原地倒著更新", "O(k²)", "O(k)", "✘", "進階要求的標準答案"],
    ["二、移位相加", "O(k²)", "O(k)", "✘", "最短"],
    ["三、組合數遞推", "O(k)", "O(k)", "✔ 其他語言要注意", "最快"]]),
 "edges": [
   "<strong><code>rowIndex = 0</code></strong> → <code>[1]</code>。"
   "<strong>三種解法的迴圈都一次都不跑。</strong>",
   "<strong><code>rowIndex = 1</code></strong> → <code>[1,1]</code>。",
   "<strong><code>rowIndex = 33</code></strong> → 最大值 1166803110，剛好在 <code>INT_MAX</code> 內。",
   "<strong>解法一正著走 <code>j</code></strong> → "
   "<strong>答案全錯（用到被改過的值）—— 本題第一名的 bug。</strong>",
   "<strong>解法一的 <code>j</code> 上界寫成 <code>rowIndex</code> 而不是 <code>i-1</code></strong> → "
   "會提前把後面的格子加進去。",
   "<strong>解法二初始值寫成 <code>[]</code></strong> → 得到 <code>[0]</code>。",
   "<strong>解法三先除後乘</strong> → 餘數損失，答案錯。",
 ],
 "follow": [
   ("h", "追問一：如果只要「第 n 列的第 k 項」呢？"),
   "<strong>直接 <code>math.comb(n, k)</code></strong>，或用解法三的遞推算 k 步 —— "
   "<strong>O(k) 時間、O(1) 空間。</strong>",
   "<strong>不需要算出整列。</strong>"
   "<strong>「只要一個值」時，永遠先問「能不能跳過中間過程」。</strong>",
   ("h", "追問二：如果 <code>rowIndex</code> 很大（例如 10⁶）且要對質數取模呢？"),
   ("c", """C(n, k) mod p （p 是質數）：

    方法 A：預處理階乘和反元素
        fact[i] = i! mod p
        inv_fact[i] = (i!)^(-1) mod p   用費馬小定理算
        C(n,k) = fact[n] × inv_fact[k] × inv_fact[n-k] mod p

        預處理 O(n)，之後每次查詢 O(1)。

    方法 B：Lucas 定理（n 很大、p 很小時）
        C(n,k) mod p = Π C(n_i, k_i) mod p
        （n_i, k_i 是 n, k 在 p 進位下的每一位）

        O(log_p n) 時間。

【競賽裡幾乎所有組合數題目都長這樣】——
    「對 10^9 + 7 取模」是標準設定，
    因為 10^9+7 是質數，而且 2^31 裝得下它的平方的一半。""",),
   ("h", "追問三：解法三為什麼不會有精度問題？"),
   "<strong>因為全程都是整數運算（<code>//</code> 而不是 <code>/</code>）。</strong>",
   "<strong>如果用浮點數（<code>/</code>），<code>C(33,16)</code> 這種九位數會開始累積誤差</strong>，"
   "<strong>最後可能差個 1。</strong>"
   "<strong>「組合數一律用整數運算」是鐵律。</strong>",
   ("h", "追問四：能不能 O(1) 空間？"),
   "<strong>如果「輸出」不算，那解法三已經是 O(1) 了</strong>"
   "（只需要記住上一項）。",
   "<strong>但輸出本身有 k+1 個數字，所以總空間至少 O(k)</strong> —— "
   "<strong>這是輸出規模的下界，無法突破。</strong>",
 ],
 "related": [
   "<strong>第 118 題 Pascal's Triangle</strong> —— 要整個三角形",
   "<strong>第 115 題 Distinct Subsequences</strong> —— 同樣的「倒著更新」",
   "<strong>第 62 題 Unique Paths</strong> —— 同一個組合數",
   "<strong>第 96 題 Unique Binary Search Trees</strong> —— 同樣的「先乘後除」",
 ],
 "check": [
   "原地更新為什麼一定要倒著走？正著走會算出什麼？",
   "內層迴圈的上界為什麼是 <code>i-1</code> 而不是 <code>rowIndex</code>？",
   "<code>C(n,k) = C(n,k-1) × (n-k+1) / k</code> 怎麼推出來的？為什麼一定整除？",
   "為什麼題目的上限是 33？",
 ],
})
print("P119 written")

# ==================== 120. Triangle ====================
S["p120_bottom"] = '''class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 由下而上：dp[j] = 從第 i 列第 j 格走到底的最小和
        dp = triangle[-1][:]                    # 最後一列就是 base

        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                # 只能往正下方或右下方走
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]'''

S["p120_inplace"] = '''class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 直接把答案寫回 triangle（O(1) 額外空間，但會改到輸入）
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]'''

S["p120_top"] = '''class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 由上而下：dp[j] = 走到第 i 列第 j 格的最小和
        dp = [triangle[0][0]]

        for i in range(1, len(triangle)):
            nxt = [0] * (i + 1)
            for j in range(i + 1):
                if j == 0:
                    best = dp[0]                # 最左邊只能從正上方來
                elif j == i:
                    best = dp[i - 1]            # 最右邊只能從左上方來
                else:
                    best = min(dp[j - 1], dp[j])
                nxt[j] = triangle[i][j] + best
            dp = nxt

        return min(dp)'''


def _p120_ref(tri):
    """獨立參考解：枚舉所有路徑（只對小輸入用）。"""
    n = len(tri)
    best = [float("inf")]
    def go(i, j, acc):
        acc += tri[i][j]
        if i == n - 1:
            best[0] = min(best[0], acc)
            return
        go(i + 1, j, acc)
        go(i + 1, j + 1, acc)
    go(0, 0, 0)
    return best[0]


_p120 = [S.load(k) for k in ("p120_bottom", "p120_inplace", "p120_top")]

for tri, want in [
    ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
    ([[-10]], -10),
    ([[1], [2, 3]], 3),
]:
    assert _p120_ref(tri) == want, ("P120 ref", tri)
    for sol in _p120:
        assert sol.minimumTotal([r[:] for r in tri]) == want, ("P120", tri, sol)

for _ in range(3000):
    n = random.randrange(1, 11)
    tri = [[random.randint(-20, 20) for _ in range(i + 1)] for i in range(n)]
    want = _p120_ref(tri)
    for sol in _p120:
        assert sol.minimumTotal([r[:] for r in tri]) == want, ("P120 random", tri, want, sol)
print("P120 solutions OK")

_P120_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">由下而上的 DP：每一格都問「從我走到底，最少要加多少？」答案最後匯集到頂點。</text>
            <g font-size="14" text-anchor="middle">
              <text x="320" y="58" fill="var(--gold)">2</text>
              <text x="285" y="100" fill="var(--gold)">3</text><text x="355" y="100" fill="var(--gold)">4</text>
              <text x="250" y="142" fill="var(--gold)">6</text><text x="320" y="142" fill="var(--gold)">5</text><text x="390" y="142" fill="var(--gold)">7</text>
              <text x="215" y="184" fill="var(--gold)">4</text><text x="285" y="184" fill="var(--gold)">1</text><text x="355" y="184" fill="var(--gold)">8</text><text x="425" y="184" fill="var(--gold)">3</text>
            </g>
            <text x="480" y="58" fill="var(--text-muted)" font-size="11" text-anchor="start">原始三角形</text>
            <line x1="20" y1="208" x2="620" y2="208" stroke="var(--border)"/>
            <text x="20" y="234" fill="var(--accent)" font-size="12">由下往上算 dp（dp[j] = 從這一格走到底的最小和）：</text>
            <g font-size="14" text-anchor="middle">
              <text x="215" y="268" fill="var(--text-muted)">4</text><text x="285" y="268" fill="var(--text-muted)">1</text><text x="355" y="268" fill="var(--text-muted)">8</text><text x="425" y="268" fill="var(--text-muted)">3</text>
              <text x="250" y="306" fill="var(--accent)">7</text><text x="320" y="306" fill="var(--accent)">6</text><text x="390" y="306" fill="var(--accent)">10</text>
              <text x="285" y="344" fill="var(--accent)">9</text><text x="355" y="344" fill="var(--accent)">10</text>
              <text x="320" y="382" fill="#ff8a65" font-size="17">11</text>
            </g>
            <text x="480" y="268" fill="var(--text-muted)" font-size="11" text-anchor="start">最後一列：照抄</text>
            <text x="480" y="306" fill="var(--text-muted)" font-size="11" text-anchor="start">6 + min(4,1) = 7　5 + min(1,8) = 6</text>
            <text x="480" y="344" fill="var(--text-muted)" font-size="11" text-anchor="start">3 + min(7,6) = 9　4 + min(6,10) = 10</text>
            <text x="480" y="382" fill="#ff8a65" font-size="11" text-anchor="start">2 + min(9,10) = 11 ← 答案</text>
            <line x1="20" y1="404" x2="620" y2="404" stroke="var(--border)"/>
            <text x="20" y="430" fill="var(--gold)" font-size="12">由下而上完全不用特判邊界：每一格的 dp[j] 和 dp[j+1] 一定都存在（下一列比較長）。</text>
            <text x="20" y="454" fill="#ff8a65" font-size="12">由上而下則要處理「最左邊只能從上面來、最右邊只能從左上來」——多兩個 if。</text>'''

emit({
 "num": 120, "slug": "triangle",
 "en": [
   "Given a <code>triangle</code> array, return <em>the minimum path sum from top to bottom</em>.",
   "For each step, you may move to an adjacent number of the row below. More formally, if you "
   "are on index <code>i</code> on the current row, you may move to either index <code>i</code> "
   "or index <code>i + 1</code> on the next row.",
   "<strong>Follow up:</strong> Could you do this using only <code>O(n)</code> extra space, "
   "where <code>n</code> is the total number of rows in the triangle?",
 ],
 "zh": [
   "給你一個三角形陣列 <code>triangle</code>，求<strong>從頂端走到底端的最小路徑和</strong>。",
   "每一步只能走到<strong>下一列相鄰的位置</strong>："
   "如果你在第 <code>i</code> 格，下一步只能到下一列的第 <code>i</code> 格或第 <code>i+1</code> 格。",
   "<strong>進階：</strong>你能只用 <code>O(n)</code> 額外空間嗎（<code>n</code> 是列數）？",
 ],
 "pre": [
   ("note", "★ 為什麼「由下而上」遠比「由上而下」乾淨", [
     ("c", """【由上而下】dp[i][j] = 從頂點走到 (i,j) 的最小和

    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1], dp[i-1][j])

    問題：
        j == 0 時沒有 dp[i-1][-1]  -> 要特判
        j == i 時沒有 dp[i-1][i]   -> 要特判
        最後還要 min(dp[最後一列]) -> 多一步

    三個額外的處理。

【由下而上】dp[j] = 從 (i,j) 走到底的最小和

    dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

    因為【下一列一定比這一列長一格】，
    所以 dp[j] 和 dp[j+1] 【永遠都存在】✔

        零個特判。

    而且答案直接就是 dp[0]（從頂點出發），不用再取 min。

【教訓】：
    當一個方向要處理邊界、另一個方向不用時，
    幾乎一定要選不用的那個。

    「反過來想」在 DP 題裡是很常見的簡化手段 ——
    第 174 題（地下城遊戲）甚至是【只有】倒著算才對。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

            2
           3 4
          6 5 7
         4 1 8 3

  輸出：11
  說明：2 + 3 + 5 + 1 = 11（如上圖粗體的那條路徑）

範例 2
  輸入：triangle = [[-10]]
  輸出：-10""",
 "constraints": [
   "1 ≤ <code>triangle.length</code> ≤ 200",
   "<code>triangle[0].length == 1</code>",
   "<code>triangle[i].length == triangle[i-1].length + 1</code>",
   "−10⁴ ≤ <code>triangle[i][j]</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "注意：數字可以是負數", [
     "<strong>所以不能用「目前的和已經超過最佳解就剪枝」這種貪心式的優化</strong> —— "
     "後面可能有很大的負數。",
     "<strong>而且「每一步都選比較小的鄰居」這種貪心也是錯的</strong>（見下方的邊界清單）。",
   ]),
 ],
 "idea": [
   ("fig", _P120_FIG, "0 0 640 472"),
   ("c", """由下而上的 DP：

    dp = triangle[-1][:]                    最後一列就是答案（走到底了）

    for i from n-2 down to 0:
        for j in 0..i:
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

    return dp[0]

【dp[j] 的語意】：
    「站在第 i 列第 j 格，一路走到最後一列，路徑和最小是多少」

【為什麼可以原地覆蓋 dp？】

    算第 i 列的 dp[j] 時，用的是 dp[j] 和 dp[j+1]（第 i+1 列的值）。

    正著走（j 從 0 到 i）：
        更新 dp[0] 用 dp[0], dp[1]  -> 都還是舊值 ✔
        更新 dp[1] 用 dp[1], dp[2]  -> dp[1] 是舊值（還沒改）、dp[2] 也是 ✔
        ...

    【每次用到的兩格都在「目前位置的右邊或自己」，
      而我們是從左往右改的 —— 所以還沒被覆蓋 ✔】

    這和第 115、119 題「必須倒著走」正好相反 ——
    方向取決於「依賴的格子在左邊還是右邊」。

    【判斷方法】：
        依賴左邊（j-1）-> 倒著走
        依賴右邊（j+1）-> 正著走
        兩邊都依賴     -> 需要額外的暫存變數

複雜度：
    O(n²) 時間（三角形的總格數），O(n) 空間 ✔ 滿足進階要求。"""),
 ],
 "approaches": [
   ap("解法一", "由下而上 + 滾動陣列（標準答案）", [
     ("c", S["p120_bottom"]),
     "<strong>六行，零個邊界特判，O(n) 空間。</strong>"
     "<strong>直接滿足進階要求。</strong>",
     ("h", "手動走一遍範例 1"),
     ("c", """            2
           3 4
          6 5 7
         4 1 8 3

dp = [4, 1, 8, 3]                （最後一列）

i = 2（[6,5,7]）：
    dp[0] = 6 + min(4, 1) = 7
    dp[1] = 5 + min(1, 8) = 6
    dp[2] = 7 + min(8, 3) = 10
    dp = [7, 6, 10, 3]           （後面的 3 是殘留，不會再用到）

i = 1（[3,4]）：
    dp[0] = 3 + min(7, 6) = 9
    dp[1] = 4 + min(6, 10) = 10
    dp = [9, 10, 10, 3]

i = 0（[2]）：
    dp[0] = 2 + min(9, 10) = 11
    dp = [11, 10, 10, 3]

return dp[0] = 11 ✔

【注意 dp 後面的殘留值】：
    它們不會影響答案，因為每一列只用前 i+1 格。
    不需要特地清掉。"""),
     ("h", "<code>triangle[-1][:]</code> 為什麼要複製？"),
     "<strong>不複製的話 <code>dp</code> 就是 <code>triangle[-1]</code> 本身</strong>，"
     "後面的更新會改到輸入 —— <strong>雖然這題改到最後一列其實沒差</strong>"
     "（迴圈從倒數第二列開始），"
     "<strong>但「不要修改呼叫者傳進來的東西」是應該養成的習慣。</strong>",
   ], "O(n²)", "O(n)", "三角形的總格數", "一列", optimal=True),

   ap("解法二", "原地修改（O(1) 額外空間，但會改到輸入）", [
     ("c", S["p120_inplace"]),
     "<strong>四行，連 <code>dp</code> 陣列都不用 —— 直接把答案寫回 <code>triangle</code>。</strong>",
     ("c", """【什麼時候可以這樣做？】

    ✔ 題目明確說可以修改輸入
    ✔ 輸入之後不會再被用到
    ✔ 你在寫競賽程式（只求快）

    ✘ 這是一個函式庫 API
    ✘ 呼叫者還要用原本的資料
    ✘ 多執行緒共用這份資料

【面試時】：
    可以寫，但一定要【主動說明】：
        「這會修改輸入，如果不允許我會複製一份。」

    不說的話，面試官可能會覺得你沒意識到副作用。

    「有沒有意識到副作用」比「有沒有副作用」更重要。""",),
     "<strong>嚴格來說這是 O(1) 額外空間</strong>，"
     "<strong>但「改掉輸入」通常不算真正的勝利。</strong>",
   ], "O(n²)", "O(1)", "三角形的總格數", "不用額外陣列"),

   ap("解法三", "由上而下（示範它為什麼比較麻煩）", [
     ("c", S["p120_top"]),
     ("c", """比解法一多了三件事：

    1. j == 0 的特判（最左邊只能從正上方來）
    2. j == i 的特判（最右邊只能從左上方來）
    3. 最後要 min(dp)（因為終點可能在最後一列的任何位置）

    而且不能原地更新（要另開一個 nxt），
    因為 dp[j] 同時依賴 dp[j-1] 和 dp[j] ——
    正著走會覆蓋掉 dp[j-1] 的舊值。

    （要原地的話得倒著走，但倒著走又會讓 dp[j] 用到新值… 
      實際上倒著走是對的：dp[j] 依賴 dp[j-1] 和 dp[j]，
      倒著走時 dp[j-1] 還沒改 ✔
      但那樣寫更難懂，不如直接開新陣列。）

【放在這裡是為了對照】——
    同一個問題，換個方向就從「六行零特判」變成「十四行三特判」。

    【選對 DP 的方向，常常比想出 DP 本身更省力。】""",),
   ], "O(n²)", "O(n)", "三角形的總格數", "兩列"),
 ],
 "compare": (["解法", "時間", "空間", "特判數", "會改輸入嗎"],
   [["一、由下而上", "O(n²)", "O(n)", "0", "✘"],
    ["二、原地修改", "O(n²)", "O(1)", "0", "✔"],
    ["三、由上而下", "O(n²)", "O(n)", "2", "✘"]]),
 "edges": [
   "<strong>只有一列</strong> <code>[[-10]]</code> → <code>-10</code>。"
   "<strong>迴圈一次都不跑，直接回 <code>dp[0]</code> ✔</strong>",
   "<strong>兩列</strong> <code>[[1],[2,3]]</code> → <code>3</code>。",
   "<strong>全部是負數</strong> → 答案是負的，<strong>不能用「和 ≥ 0 就剪枝」。</strong>",
   "<strong>貪心「每步選較小的鄰居」是錯的</strong>：",
   "<strong>例如 <code>[[1],[2,1],[9,9,1]]</code></strong> → "
   "<strong>貪心從 1 選 1（右邊），再從 1 選 1 → 1+1+1 = 3 ✔ 剛好對。</strong>"
   "<strong>但 <code>[[1],[1,2],[9,100,1]]</code> → 貪心選 1（左），下一步只能 9 或 100 → 11；"
   "正解是走 2 再走 1 = 4。</strong>",
   "<strong>由上而下忘了特判 <code>j == 0</code></strong> → "
   "<code>dp[-1]</code> 在 Python 是最後一個元素 —— <strong>不會報錯，但答案錯，極難 debug。</strong>",
   "<strong>由下而上的 <code>j</code> 上界寫成 <code>i+1</code></strong> → "
   "<code>dp[i+2]</code> 索引越界（最後一輪時）。",
   "<strong>200 列</strong> → 總格數 20100，完全沒有效能壓力。",
 ],
 "follow": [
   ("h", "追問一：如果要輸出「走了哪條路徑」呢？"),
   "<strong>保留完整的二維 <code>dp</code>，然後從 <code>dp[0][0]</code> 往下追</strong>："
   "在每一格看 <code>dp[i+1][j]</code> 和 <code>dp[i+1][j+1]</code> 哪個小就往哪走。",
   "<strong>需要 O(n²) 空間</strong> —— <strong>這是「壓空間」的代價</strong>"
   "（和第 97、72 題的追問一樣）。",
   ("h", "追問二：為什麼貪心會錯？"),
   ("c", """貪心「每一步選較小的鄰居」是【局部最優】，
但這題的【局部最優不等於全域最優】。

    [[1],
     [1, 2],
     [9, 100, 1]]

    貪心：1 -> 選 1（因為 1 < 2）-> 只能選 9 或 100 -> 1+1+9 = 11
    正解：1 -> 選 2 -> 選 1 -> 1+2+1 = 4 ✔

    「現在多付 1，後面省下 8」——
    貪心看不到未來，所以錯。

【什麼時候貪心才對？】
    要能證明「交換論證」或「擬陣結構」。

    第 122 題（買賣股票 II）、第 134 題（加油站）、
    第 135 題（分發糖果）的貪心都是對的，
    而且都有明確的證明。

    【貪心不是「感覺對就用」，是「證明了才能用」。】"""),
   ("h", "追問三：如果改成「最大路徑和」呢？"),
   "<strong>把 <code>min</code> 換成 <code>max</code>，一個字。</strong>"
   "<strong>其他完全不變。</strong>",
   "<strong>如果改成「路徑上數字的乘積最大」，就麻煩了</strong> —— "
   "<strong>負負得正，要同時追蹤最大和最小值</strong>"
   "（和第 152 題「乘積最大子陣列」一樣）。",
   ("h", "追問四：這題和第 64 題（最小路徑和）有什麼不同？"),
   ("c", """第 64 題：m×n 矩形網格，只能往右或往下
第 120 題：三角形，只能往正下或右下

    【本質上是同一個問題】——
    把三角形的每一列「靠左對齊」，
    就變成一個下三角形的網格，
    「正下 / 右下」對應到「下 / 右下」。

    兩題的 DP 式幾乎一樣：
        64：  dp[j] = grid[i][j] + min(dp[j], dp[j-1])
        120： dp[j] = tri[i][j]  + min(dp[j], dp[j+1])

    差別只在「往哪個方向走」和「從哪一端開始算」。

【網格 DP 家族】：
    62 不同路徑、63 有障礙、64 最小路徑和、
    120 三角形、174 地下城遊戲、931 下降路徑最小和

    全部都是「每格只能從固定幾個鄰居來」的骨架。"""),
 ],
 "related": [
   "<strong>第 64 題 Minimum Path Sum</strong> —— 矩形網格版",
   "<strong>第 62/63 題 Unique Paths</strong> —— 同一個網格骨架（數路徑）",
   "<strong>第 174 題 Dungeon Game</strong> —— 只能倒著算的網格 DP",
   "<strong>第 931 題 Minimum Falling Path Sum</strong> —— 三個方向的版本",
   "<strong>第 152 題 Maximum Product Subarray</strong> —— 改成乘積時的陷阱",
 ],
 "check": [
   "「由下而上」為什麼不用特判邊界？「由上而下」要特判哪兩個？",
   "滾動陣列時 <code>j</code> 該正著走還是倒著走？判斷依據是什麼？",
   "為什麼貪心「每步選較小的鄰居」是錯的？請舉出反例。",
   "這題和第 64 題本質上是同一個問題嗎？差在哪裡？",
 ],
})
print("P120 written")

# ==================== 121. Best Time to Buy and Sell Stock ====================
S["p121"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        low = float('inf')              # 到目前為止看過的最低價

        for p in prices:
            low = min(low, p)           # 更新歷史最低點
            best = max(best, p - low)   # 如果今天賣，能賺多少

        return best'''

S["p121_dp"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 兩個狀態：hold = 手上有股票時的最大「現金」；free = 空手時的最大現金
        hold = float('-inf')            # 一開始不可能持股
        free = 0

        for p in prices:
            hold = max(hold, -p)        # 買進（只能買一次，所以是 -p 不是 free - p）
            free = max(free, hold + p)  # 賣出

        return free'''

S["p121_kadane"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 把價格轉成「每日漲跌」，問題就變成「最大子陣列和」（第 53 題）
        cur = best = 0
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            cur = max(diff, cur + diff) # Kadane：要嘛從今天重新開始，要嘛接著昨天
            best = max(best, cur)
        return best'''


def _p121_ref(prices):
    """獨立參考解：暴力枚舉所有買賣日。"""
    best = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            best = max(best, prices[j] - prices[i])
    return best


_p121 = [S.load(k) for k in ("p121", "p121_dp", "p121_kadane")]

for pr, want in [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1], 0),
    ([2, 4, 1], 2),
    ([3, 3, 3], 0),
]:
    assert _p121_ref(pr) == want, ("P121 ref", pr)
    for sol in _p121:
        assert sol.maxProfit(pr) == want, ("P121", pr, sol)

for _ in range(6000):
    n = random.randrange(1, 14)
    pr = [random.randint(0, 20) for _ in range(n)]
    want = _p121_ref(pr)
    for sol in _p121:
        assert sol.maxProfit(pr) == want, ("P121 random", pr, want, sol)
print("P121 solutions OK")

_P121_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">一趟掃描：左手記住「到今天為止的最低價」，右手算「如果今天賣能賺多少」。</text>
            <text x="20" y="48" fill="var(--gold)" font-size="13">prices = [7, 1, 5, 3, 6, 4]</text>
            <g stroke="var(--border)" stroke-width="1">
              <line x1="70" y1="230" x2="560" y2="230"/>
            </g>
            <g font-size="12" text-anchor="middle">
              <circle cx="100" cy="90" r="5" fill="var(--text-muted)"/><text x="100" y="78" fill="var(--text-muted)">7</text><text x="100" y="250" fill="var(--text-muted)">第0天</text>
              <circle cx="190" cy="212" r="6" fill="var(--accent)"/><text x="190" y="200" fill="var(--accent)">1</text><text x="190" y="250" fill="var(--accent)">買</text>
              <circle cx="280" cy="140" r="5" fill="var(--text-muted)"/><text x="280" y="128" fill="var(--text-muted)">5</text><text x="280" y="250" fill="var(--text-muted)">第2天</text>
              <circle cx="370" cy="176" r="5" fill="var(--text-muted)"/><text x="370" y="164" fill="var(--text-muted)">3</text><text x="370" y="250" fill="var(--text-muted)">第3天</text>
              <circle cx="460" cy="122" r="6" fill="#ff8a65"/><text x="460" y="110" fill="#ff8a65">6</text><text x="460" y="250" fill="#ff8a65">賣</text>
              <circle cx="550" cy="158" r="5" fill="var(--text-muted)"/><text x="550" y="146" fill="var(--text-muted)">4</text><text x="550" y="250" fill="var(--text-muted)">第5天</text>
            </g>
            <polyline points="100,90 190,212 280,140 370,176 460,122 550,158" fill="none" stroke="var(--border)" stroke-width="1.5"/>
            <line x1="190" y1="212" x2="460" y2="122" stroke="var(--gold)" stroke-width="2" stroke-dasharray="5 3"/>
            <text x="325" y="160" fill="var(--gold)" font-size="12" text-anchor="middle">利潤 = 6 − 1 = 5</text>
            <line x1="20" y1="272" x2="620" y2="272" stroke="var(--border)"/>
            <text x="20" y="298" fill="var(--accent)" font-size="12">逐日追蹤（low = 歷史最低，best = 目前最佳利潤）：</text>
            <text x="40" y="324" fill="var(--text-muted)" font-size="12">p=7　low=7　best=max(0, 7−7)=0</text>
            <text x="40" y="348" fill="var(--text-muted)" font-size="12">p=1　low=1　best=max(0, 1−1)=0</text>
            <text x="40" y="372" fill="var(--text-muted)" font-size="12">p=5　low=1　best=max(0, 5−1)=4</text>
            <text x="40" y="396" fill="var(--text-muted)" font-size="12">p=3　low=1　best=max(4, 3−1)=4</text>
            <text x="40" y="420" fill="var(--gold)" font-size="12">p=6　low=1　best=max(4, 6−1)=5　←</text>
            <text x="40" y="444" fill="var(--text-muted)" font-size="12">p=4　low=1　best=max(5, 4−1)=5</text>
            <text x="20" y="474" fill="#ff8a65" font-size="12">★ 先更新 low 再算 best，所以「同一天買又賣」會得到 0 —— 剛好符合「不能當天套利」。</text>'''

emit({
 "num": 121, "slug": "best-time-to-buy-and-sell-stock",
 "en": [
   "You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a "
   "given stock on the <code>i</code><sup>th</sup> day.",
   "You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock "
   "and choosing a <strong>different day in the future</strong> to sell that stock.",
   "Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot "
   "achieve any profit, return <code>0</code>.",
 ],
 "zh": [
   "給你一個陣列 <code>prices</code>，<code>prices[i]</code> 是某支股票第 <code>i</code> 天的價格。",
   "你想選<strong>某一天買入</strong>，再選<strong>未來的某一天賣出</strong>，"
   "讓利潤最大化。",
   "回傳你能獲得的<strong>最大利潤</strong>；如果沒辦法獲利，回傳 <code>0</code>。",
 ],
 "pre": [
   ("note", "這是「買賣股票」六題的第一題", [
     ("c", """121  只能買賣【一次】                   （本題）
122  可以買賣【無限次】                 -> 貪心
123  最多買賣【兩次】                   -> 四個狀態變數
188  最多買賣【k 次】                   -> 通用 DP
309  無限次，但賣出後要【冷凍一天】     -> 三個狀態
714  無限次，但每筆要付【手續費】       -> 兩個狀態

    【全部都是同一個狀態機 DP 的變形。】

    本題是最簡單的入口，
    但它有一個「一趟掃描」的特解（解法一）——
    那個特解非常漂亮，也是面試官想聽到的答案。

    不過【解法二（狀態機）才是能推廣到其他五題的那一個】，
    所以兩個都要會。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：prices = [7,1,5,3,6,4]
  輸出：5
  說明：第 2 天（價格 1）買入，第 5 天（價格 6）賣出，利潤 6 - 1 = 5。
        【注意不能在第 2 天買、第 1 天賣 —— 必須先買後賣。】

範例 2
  輸入：prices = [7,6,4,3,1]
  輸出：0
  說明：一路下跌，任何買賣都會虧錢，所以不交易，利潤 0。""",
 "constraints": [
   "1 ≤ <code>prices.length</code> ≤ 10⁵",
   "0 ≤ <code>prices[i]</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "10⁵ 這個上限在說什麼", [
     "<strong>O(n²) 的暴力法是 10¹⁰ 次運算 —— 一定逾時。</strong>",
     "<strong>所以必須是 O(n) 或 O(n log n)。</strong>"
     "<strong>而這題有非常乾淨的 O(n) 一趟解法。</strong>",
   ]),
 ],
 "idea": [
   ("fig", _P121_FIG, "0 0 640 492"),
   ("c", """【核心觀察】：

    如果決定「第 i 天賣出」，那最好的買入日
    一定是「第 0 到 i-1 天裡價格最低的那天」。

    所以只要一邊掃描、一邊記住「到目前為止的最低價」，
    就能在 O(1) 時間內算出「今天賣出的最佳利潤」。

    low  = min(low, prices[i])
    best = max(best, prices[i] - low)

【★ 順序很重要：先更新 low，再算 best】

    這樣當 prices[i] 就是新的最低價時，
    prices[i] - low = 0 -> 不會產生負利潤 ✔

    也順便處理了「不能同一天買又賣」——
    其實同一天買賣的利潤是 0，
    而我們允許「不交易」（答案下界是 0），
    所以這兩件事剛好一致。

【為什麼這樣一定是全域最優？】

    答案一定對應某一組 (買入日 i, 賣出日 j)，i < j。

    我們的迴圈走到 j 時，low 一定 <= prices[i]
    （因為 i < j，prices[i] 已經被納入 min 了）。

    所以 best >= prices[j] - low >= prices[j] - prices[i] ✔

    而 best 又永遠是某組合法交易的利潤（不會高估）。

    兩邊夾擊 -> best 就是最大值 ✔"""),
 ],
 "approaches": [
   ap("解法一", "一趟掃描記錄歷史最低（標準答案）", [
     ("c", S["p121"]),
     "<strong>五行，O(n) 時間、O(1) 空間。</strong>"
     "<strong>這題不可能有更好的解。</strong>",
     ("h", "<code>low</code> 初始化成 <code>inf</code> 還是 <code>prices[0]</code>？"),
     ("c", """兩個都可以：

    low = float('inf')      然後從第 0 天開始掃
    low = prices[0]         然後從第 1 天開始掃

    用 inf 的好處是【不用特判空陣列】
    （雖然題目保證至少一天）。

    用 prices[0] 的好處是【不引入浮點數】——

        注意 float('inf') 和整數比較是安全的，
        但如果你之後對 low 做整數運算（例如取餘數），
        就會出問題。

    這題只有 min 和減法，兩種都沒問題。

【一般原則】：
    需要「比任何輸入都大 / 小」的初始值時，
        Python：float('inf') / float('-inf')
        或者用「題目保證的範圍外的值」（這題可以用 10001）

    後者永遠是整數，比較安全。"""),
     ("h", "為什麼 <code>best</code> 初始化成 0 而不是 <code>-inf</code>？"),
     "因為<strong>題目說「沒辦法獲利就回 0」</strong> —— "
     "也就是<strong>「不交易」永遠是一個合法選項</strong>。",
     "<strong>初始化成 <code>-inf</code> 的話，一路下跌的陣列會回傳負數 ✘</strong>",
   ], "O(n)", "O(1)", "掃一遍", "兩個變數", optimal=True),

   ap("解法二", "狀態機 DP（能推廣到其他五題）", [
     ("c", S["p121_dp"]),
     ("h", "兩個狀態的意義"),
     ("c", """hold = 「今天結束時【手上有股票】」的最大現金
free = 「今天結束時【手上沒股票】」的最大現金

    注意這裡算的是【現金】而不是利潤 ——
    買股票要花錢，所以 hold 通常是負的。

轉移：
    hold = max(hold, -p)
           ^^^^  ^^
           昨天就持股   今天才買（花掉 p 元）

    free = max(free, hold + p)
           ^^^^  ^^^^^^^^
           昨天就空手   今天賣掉（拿回 p 元）

    答案是 free（最後一定要賣掉，手上留股票沒意義）。

【★ 為什麼是 -p 而不是 free - p？】

    因為本題【只能交易一次】——
    買入之前一定是「從來沒交易過」，現金是 0。

    所以買入後的現金是 0 - p = -p。

    第 122 題（無限次）就要寫成 free - p，
    因為可以「賣掉之後再買」。

    【這一個減號，就是 121 和 122 的全部差別。】

    122：hold = max(hold, free - p)
    121：hold = max(hold, 0 - p)"""),
     ("h", "為什麼這個版本比較有價值？"),
     ("c", """因為【它能推廣】：

    123（最多兩次）：四個狀態
        buy1, sell1, buy2, sell2

        buy1  = max(buy1,  -p)
        sell1 = max(sell1, buy1 + p)
        buy2  = max(buy2,  sell1 - p)
        sell2 = max(sell2, buy2 + p)

    188（最多 k 次）：2k 個狀態，用迴圈跑

    309（冷凍期）：三個狀態（持股 / 冷凍 / 可買）

    714（手續費）：hold = max(hold, free - p)
                   free = max(free, hold + p - fee)

【解法一的「記住最低價」只對 121 有效，
  解法二的狀態機對全部六題都有效。】

    面試時先寫解法一（展示你看出了特殊結構），
    再說「如果改成 k 次交易，我會用狀態機」——
    這個回答會非常加分。"""),
   ], "O(n)", "O(1)", "掃一遍", "兩個變數"),

   ap("解法三", "轉成「最大子陣列和」（第 53 題）", [
     ("c", S["p121_kadane"]),
     ("h", "把價格換成「每日漲跌」"),
     ("c", """prices = [7, 1, 5, 3, 6, 4]
diff   =   [-6, 4, -2, 3, -2]

    「第 i 天買、第 j 天賣」的利潤
      = prices[j] - prices[i]
      = diff[i+1] + diff[i+2] + ... + diff[j]      （望遠鏡求和）

    也就是【diff 的一段連續區間和】✔

    所以「最大利潤」= 「diff 的最大子陣列和」
                    = 第 53 題（Kadane 演算法）

    驗證：diff 的最大子陣列是 [4, -2, 3] = 5 ✔

【Kadane 演算法】：
    cur = max(diff, cur + diff)
          ^^^^      ^^^^^^^^^^
          從今天重新開始   接著昨天那一段

    best = max(best, cur)

    一行遞推，O(n)。

【這個「差分轉換」的技巧很通用】：

    「區間和」<-> 「前綴差」
    「最大差值」<-> 「最大子陣列和」

    看到「求兩個位置的最大差」，
    就可以想想要不要轉成差分。"""),
     "<strong>複雜度和解法一相同，但多繞了一圈。</strong>"
     "<strong>價值在於它揭示了「這題和第 53 題是同一題」。</strong>",
   ], "O(n)", "O(1)", "掃一遍", "兩個變數"),
 ],
 "compare": (["解法", "時間", "空間", "能推廣嗎", "備註"],
   [["一、記錄歷史最低", "O(n)", "O(1)", "✘ 只對本題", "標準答案，最短"],
    ["二、狀態機 DP", "O(n)", "O(1)", "✔ 六題通用", "面試最該講的"],
    ["三、Kadane", "O(n)", "O(1)", "△", "揭示和第 53 題的關係"]]),
 "edges": [
   "<strong>只有一天</strong> <code>[1]</code> → <code>0</code>（沒辦法買了又賣）。",
   "<strong>一路下跌</strong> <code>[7,6,4,3,1]</code> → <code>0</code>。"
   "<strong><code>best</code> 初始化成 <code>-inf</code> 會回傳負數。</strong>",
   "<strong>一路上漲</strong> <code>[1,2,3,4]</code> → <code>3</code>（第一天買、最後一天賣）。",
   "<strong>全部相同</strong> <code>[3,3,3]</code> → <code>0</code>。",
   "<strong>最低價在最後一天</strong> <code>[2,4,1]</code> → <code>2</code>。"
   "<strong>不能因為 1 最低就去買它 —— 後面沒有天可以賣了。</strong>"
   "<strong>「先更新 <code>low</code> 再算 <code>best</code>」自動處理了這件事。</strong>",
   "<strong>先算 <code>best</code> 再更新 <code>low</code></strong> → "
   "<strong>其實也對（那樣等於不允許同日買賣），但要確認 <code>low</code> 的初始值。</strong>",
   "<strong>10⁵ 天</strong> → O(n²) 暴力法必定逾時。",
 ],
 "follow": [
   ("h", "追問一：如果可以買賣無限次呢？"),
   "<strong>第 122 題</strong>。答案是<strong>「把所有上漲區間的漲幅加起來」</strong>：",
   ("c", """profit = sum(max(0, prices[i] - prices[i-1]) for i in range(1, n))

【為什麼這樣是對的？】

    任何一段「低點買、高點賣」的交易，
    都可以拆成「每天買、隔天賣」的一串小交易，
    總利潤完全相同（望遠鏡求和）。

        買在 a 賣在 c  =  (b-a) + (c-b)

    而「每天都判斷要不要賺這一天」是最自由的策略 ——
    負的就不做，正的就做。

    所以貪心是最優的 ✔

【這是「交換論證」的典型應用】：
    證明「任何最優解都能被改造成貪心解，而不會變差」。""",),
   ("h", "追問二：如果最多只能買賣兩次呢？"),
   "<strong>第 123 題</strong>。用四個狀態變數（見解法二的說明）。",
   "<strong>也可以用「分割點」的思路</strong>："
   "<strong>枚舉一個分割點 <code>i</code>，答案 = 「<code>[0,i]</code> 的最大利潤」+「<code>[i,n)</code> 的最大利潤」</strong>。"
   "<strong>各自用本題的方法預處理，總共 O(n)。</strong>"
   "<strong>但狀態機版更短也更好推廣。</strong>",
   ("h", "追問三：如果要輸出「哪天買、哪天賣」呢？"),
   "<strong>在更新 <code>best</code> 時順便記下 <code>(買入日, 賣出日)</code></strong>。",
   ("c", """low, low_day = prices[0], 0
best, ans = 0, None
for i, p in enumerate(prices):
    if p < low:
        low, low_day = p, i
    if p - low > best:
        best, ans = p - low, (low_day, i)

【注意 low_day 要和 low 同步更新】——
    只更新 low 而忘了 low_day 是很常見的錯誤。

    把「互相關聯的變數」放在同一行更新，
    可以減少這類 bug。""",),
   ("h", "追問四：如果是「股價會即時進來」的串流呢？"),
   "<strong>解法一天生就是串流演算法</strong> —— "
   "<strong>它只需要 O(1) 空間，而且每來一筆就能立刻更新答案。</strong>",
   "<strong>這叫做「線上演算法」（online algorithm）</strong>："
   "<strong>不需要看到全部資料就能維護答案。</strong>"
   "<strong>相對地，需要先排序或先看完全部的演算法叫「離線」（offline）。</strong>",
   "<strong>面試官問「如果資料是串流進來的」時，先檢查你的解法是不是已經是線上的了。</strong>",
 ],
 "related": [
   "<strong>第 122 題 Best Time to Buy and Sell Stock II</strong> —— 無限次，貪心",
   "<strong>第 123 題 …III</strong> —— 最多兩次，四個狀態",
   "<strong>第 188 題 …IV</strong> —— 最多 k 次，通用 DP",
   "<strong>第 53 題 Maximum Subarray</strong> —— 解法三揭示的等價問題",
   "<strong>第 309/714 題</strong> —— 冷凍期 / 手續費的變形",
 ],
 "check": [
   "為什麼「先更新 <code>low</code> 再算 <code>best</code>」就不會出現負利潤？",
   "狀態機版裡 <code>hold = max(hold, -p)</code> 的 <code>-p</code> 為什麼不是 <code>free - p</code>？",
   "這題和第 53 題（最大子陣列和）的等價關係是什麼？",
   "<code>best</code> 初始化成 <code>-inf</code> 會在哪個測資出錯？",
 ],
})
print("P121 written")
