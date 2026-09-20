# -*- coding: utf-8 -*-
"""第 59–61 題。"""
import random, math
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(59)

# ==================== 59. Spiral Matrix II ====================
S["p59"] = '''class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]
        top, bottom, left, right = 0, n - 1, 0, n - 1
        v = 1

        while top <= bottom and left <= right:
            for c in range(left, right + 1):
                m[top][c] = v; v += 1
            top += 1

            for r in range(top, bottom + 1):
                m[r][right] = v; v += 1
            right -= 1

            if top <= bottom:
                for c in range(right, left - 1, -1):
                    m[bottom][c] = v; v += 1
                bottom -= 1

            if left <= right:
                for r in range(bottom, top - 1, -1):
                    m[r][left] = v; v += 1
                left += 1

        return m'''

S["p59_dir"] = '''class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        m = [[0] * n for _ in range(n)]
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # 右下左上

        r = c = d = 0
        for v in range(1, n * n + 1):
            m[r][c] = v
            nr, nc = r + DIRS[d][0], c + DIRS[d][1]
            # 撞牆或撞到已填的格子 -> 右轉
            if not (0 <= nr < n and 0 <= nc < n and m[nr][nc] == 0):
                d = (d + 1) % 4
                nr, nc = r + DIRS[d][0], c + DIRS[d][1]
            r, c = nr, nc

        return m'''

_p59 = [S.load(k) for k in ("p59", "p59_dir")]


def _p59_ref(n):
    """用第 54 題的螺旋讀取來反推：把 1..n² 依螺旋順序填進去。"""
    m = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    v = 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            m[top][c] = v; v += 1
        top += 1
        for r in range(top, bottom + 1):
            m[r][right] = v; v += 1
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                m[bottom][c] = v; v += 1
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                m[r][left] = v; v += 1
            left += 1
    return m


# 獨立驗證：用第 54 題的螺旋走訪讀回來，必須得到 1..n²
def _spiral_read(m):
    res = []
    g = [row[:] for row in m]
    while g and g[0]:
        res += g.pop(0)
        g = [list(r) for r in zip(*g)][::-1]
    return res


for n in range(1, 12):
    for sol in _p59:
        g = sol.generateMatrix(n)
        assert len(g) == n and all(len(r) == n for r in g), ("P59 shape", n)
        assert _spiral_read(g) == list(range(1, n * n + 1)), ("P59", n, sol, g)
assert _p59[0].generateMatrix(3) == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
assert _p59[0].generateMatrix(1) == [[1]]
print("P59 solutions OK")

_P59_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">n = 4：把 1 到 16 依螺旋順序填進去</text>
            <g font-size="15" text-anchor="middle">
              <rect x="200" y="46" width="52" height="46" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="226" y="76" fill="var(--accent)">1</text>
              <rect x="252" y="46" width="52" height="46" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="278" y="76" fill="var(--accent)">2</text>
              <rect x="304" y="46" width="52" height="46" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="330" y="76" fill="var(--accent)">3</text>
              <rect x="356" y="46" width="52" height="46" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="382" y="76" fill="var(--accent)">4</text>
              <rect x="200" y="92" width="52" height="46" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="226" y="122" fill="var(--gold)">12</text>
              <rect x="252" y="92" width="52" height="46" fill="none" stroke="var(--text-muted)"/><text x="278" y="122" fill="var(--text-muted)">13</text>
              <rect x="304" y="92" width="52" height="46" fill="none" stroke="var(--text-muted)"/><text x="330" y="122" fill="var(--text-muted)">14</text>
              <rect x="356" y="92" width="52" height="46" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="382" y="122" fill="#ff8a65">5</text>
              <rect x="200" y="138" width="52" height="46" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="226" y="168" fill="var(--gold)">11</text>
              <rect x="252" y="138" width="52" height="46" fill="none" stroke="var(--text-muted)"/><text x="278" y="168" fill="var(--text-muted)">16</text>
              <rect x="304" y="138" width="52" height="46" fill="none" stroke="var(--text-muted)"/><text x="330" y="168" fill="var(--text-muted)">15</text>
              <rect x="356" y="138" width="52" height="46" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="382" y="168" fill="#ff8a65">6</text>
              <rect x="200" y="184" width="52" height="46" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="226" y="214" fill="var(--gold)">10</text>
              <rect x="252" y="184" width="52" height="46" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="278" y="214" fill="var(--gold)">9</text>
              <rect x="304" y="184" width="52" height="46" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="330" y="214" fill="var(--gold)">8</text>
              <rect x="356" y="184" width="52" height="46" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="382" y="214" fill="#ff8a65">7</text>
            </g>
            <text x="304" y="36" fill="var(--accent)" font-size="11" text-anchor="middle">① 往右 1–4</text>
            <text x="440" y="122" fill="#ff8a65" font-size="11">② 往下 5–7</text>
            <text x="304" y="248" fill="var(--gold)" font-size="11" text-anchor="middle">③ 往左 8–10　④ 往上 11–12　然後內圈 13–16</text>
            <text x="20" y="282" fill="var(--gold)" font-size="12">和第 54 題完全一樣的邊界邏輯，只是把「讀 matrix[r][c]」換成「寫 matrix[r][c] = v」。</text>'''

emit({
 "num": 59, "slug": "spiral-matrix-ii",
 "en": [
   "Given a positive integer <code>n</code>, generate an <code>n x n</code> "
   "<code>matrix</code> filled with elements from <code>1</code> to <code>n²</code> in spiral "
   "order.",
 ],
 "zh": [
   "給你一個正整數 <code>n</code>，產生一個 <code>n × n</code> 的矩陣，"
   "把 <code>1</code> 到 <code>n²</code> 依<strong>螺旋順序</strong>（順時針由外往內）填進去。",
 ],
 "pre": [
   ("note", "和第 54 題是同一題，只是反過來", [
     ("c", """第 54 題：給你矩陣，依螺旋順序「讀」出來
第 59 題：給你 n，依螺旋順序「寫」進去

邊界邏輯一模一樣：
    top / bottom / left / right 四個邊界
    往右 -> 往下 -> 往左 -> 往上，每走完一條邊就往內收

唯一的差別：
    第 54 題： out.append(matrix[top][c])
    第 59 題： matrix[top][c] = v; v += 1

所以如果第 54 題寫熟了，這題就是把一行換掉。

一個額外的好處：
    本題保證是「正方形」，而且「一定填滿」，
    所以不會出現第 54 題那種「1 × n 的扁矩陣」邊界。
    （n 是奇數時中間會剩一格，但那是 top == bottom 的正常情況。）"""),
   ]),
 ],
 "examples": """範例 1
  輸入：n = 3
  輸出：[[1,2,3],[8,9,4],[7,6,5]]

  1 2 3
  8 9 4
  7 6 5

範例 2
  輸入：n = 1
  輸出：[[1]]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 20",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>保證是正方形</strong>，而且 <code>n ≥ 1</code>。"
       "比第 54 題單純很多。",
       "<strong>n ≤ 20</strong>，最多 400 個格子。效率完全不是問題。",
       "<strong>驗證方法</strong>：填完之後，用第 54 題的螺旋走訪讀回來，"
       "應該剛好得到 <code>1, 2, ..., n²</code>。"
       "<strong>這是最可靠的自我檢查，本篇的測試就是這樣做的。</strong>",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P59_FIG, "0 0 640 294"),
 ],
 "approaches": [
   ap("解法一", "四個邊界（和第 54 題同構）", [
     ("c", S["p59"]),
     ("h", "那兩個 <code>if</code> 還需要嗎？"),
     ("c", """本題是正方形，所以不會出現「1 × n」那種扁矩陣。

但 n 是奇數時，最後會剩下正中間一格：
    此時 top == bottom 且 left == right

    ① 往右：填掉那一格，top 變成 bottom + 1
    ② 往下：range(top, bottom+1) 空的，不做事，right 變成 left - 1
    ③ 如果沒有 if top <= bottom：
         range(right, left-1, -1) = range(left-1, left-1, -1) 是空的
         剛好也不做事 —— 所以其實不加 if 也不會錯

    但這是「碰巧」而不是「設計」。
    n 是偶數時，最後一圈是 2×2，四步都會執行，也沒問題。

保留那兩個 if 的理由：
    1. 和第 54 題保持一致（同一套模板）
    2. 意圖明確，不依賴「range 剛好是空的」這種巧合
    3. 如果之後推廣到非正方形，它們就變成必要的

「不依賴巧合」是寫邊界程式碼的好習慣。"""),
     ("h", "驗證的技巧"),
     "填完之後最快的檢查：<strong>矩陣裡的數字排序後應該剛好是 1..n²，一個不多一個不少。</strong>"
     "如果有重複或缺漏，表示邊界收縮的邏輯錯了。"
     "<code>sorted(v for row in m for v in row) == list(range(1, n*n+1))</code> 一行就能檢查。",
   ], "O(n²)", "O(1)（不算輸出）", "每格填一次", "只有四個邊界變數", optimal=True),

   ap("解法二", "方向陣列 + 已填標記", [
     "和第 54 題的解法二一樣：<strong>像蟲一樣爬，撞牆或撞到已填的格子就右轉。</strong>"
     "這題更方便 —— <strong>矩陣本身就是「已填標記」</strong>（0 表示還沒填）。",
     ("c", S["p59_dir"]),
     "<strong>不需要額外的 <code>seen</code> 陣列</strong>，"
     "因為 <code>m[nr][nc] == 0</code> 就代表「還沒填」。"
     "（這依賴「要填的值都 ≥ 1」—— 剛好成立。）",
     "<strong>迴圈跑 <code>n * n</code> 次</strong>，剛好每格一次，"
     "所以完全不需要終止條件的判斷。",
     "<strong>優點</strong>：沒有任何邊界推導，幾乎不可能寫錯。"
     "<strong>缺點</strong>：每一步都要做一次「越界 + 已填」的檢查（常數稍大），"
     "而且依賴「0 是保留值」這個假設。",
   ], "O(n²)", "O(1)（不算輸出）", "每格一次", "沒有額外空間"),
 ],
 "compare": (["解法", "時間", "額外空間", "邊界難度", "備註"],
   [["一、四邊界", "O(n²)", "O(1)", "★★☆☆☆", "和第 54 題同一套模板"],
    ["二、方向 + 0 標記", "O(n²)", "O(1)", "★☆☆☆☆", "最不容易錯"]]),
 "edges": [
   "<strong>n = 1</strong> → <code>[[1]]</code>。",
   "<strong>n = 2</strong> → <code>[[1,2],[4,3]]</code>。最小的完整一圈。",
   "<strong>n = 3</strong> → 正中間是 9（最後一個填的）。",
   "<strong>n 是偶數</strong>：最後一圈剛好是 2×2，四步都會執行。",
   "<strong>n 是奇數</strong>：最後剩正中間一格，只有第 ① 步會填到它。",
   "<strong>驗證</strong>：排序後必須是 1..n²，而且螺旋讀回來要是遞增的。",
 ],
 "follow": [
   ("h", "追問一：如果要從內往外填呢？"),
   "最簡單的做法：<strong>照本題填，然後把每個值 <code>v</code> 換成 <code>n² + 1 − v</code></strong>。"
   "（由外往內填 1..n²，反轉數值就變成由內往外。）"
   "如果要「由內往外順時針」而不是「由內往外逆時針」，方向也要調整。",
   ("h", "追問二：如果不是正方形（m × n）呢？"),
   "四邊界的邏輯完全不用改，只要把 <code>bottom</code> 初始化成 <code>m - 1</code>、"
   "<code>right</code> 初始化成 <code>n - 1</code>。"
   "<strong>但那兩個 <code>if</code> 就變成必要的了</strong>（會出現「只剩一列」的情況）。",
   ("h", "追問三：這題和第 54 題為什麼值得一起練？"),
   "因為它們展示了一個重要的對稱性：<strong>「走訪」和「生成」是同一個演算法的兩面。</strong>",
   ("c", """走訪：  for 每個位置（依某個順序）:  讀出 data[位置]
生成：  for 每個位置（依某個順序）:  data[位置] = 下一個值

只要「順序」的邏輯寫對了，兩者共用同一份程式碼骨架。

同樣的對稱出現在：
    第 6 題 Z 字形變換（走訪）vs 還原（生成）
    序列化 vs 反序列化（第 297 題）
    編碼 vs 解碼

    寫完一個，另一個通常只要改一行。""",),
 ],
 "related": [
   "<strong>第 54 題 Spiral Matrix</strong> —— 反過來，走訪版",
   "<strong>第 885 題 Spiral Matrix III</strong> —— 從任意點出發，可以走出邊界",
   "<strong>第 48 題 Rotate Image</strong> —— 另一個矩陣的「一圈一圈」",
 ],
 "check": [
   "本題保證是正方形，那兩個 <code>if</code> 還需要嗎？為什麼還是建議保留？",
   "解法二為什麼不需要額外的 <code>seen</code> 陣列？它依賴什麼假設？",
   "填完之後，最快的自我檢查是什麼？",
   "如果要「由內往外」填，最省事的做法是什麼？",
 ],
})
print("P59 written")

# ==================== 60. Permutation Sequence ====================
S["p60"] = '''class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 預先算好階乘：fact[i] = i!
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        nums = [str(i) for i in range(1, n + 1)]   # 還沒用掉的數字（遞增）
        k -= 1                                     # 轉成 0-indexed
        out = []

        for i in range(n, 0, -1):
            block = fact[i - 1]        # 固定第一位之後，後面有 (i-1)! 種排法
            idx = k // block           # 第一位該取「剩餘數字」裡的第幾個
            k %= block

            out.append(nums.pop(idx))  # 取走並從候選裡移除

        return "".join(out)'''

S["p60_next"] = '''class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 對照組：從最小的排列開始，呼叫 k-1 次「下一個排列」
        # 正確但 O(k·n)，k 可以到 9! = 362880，會慢很多
        nums = list(range(1, n + 1))

        def next_perm(a):
            i = len(a) - 2
            while i >= 0 and a[i] >= a[i + 1]:
                i -= 1
            if i >= 0:
                j = len(a) - 1
                while a[j] <= a[i]:
                    j -= 1
                a[i], a[j] = a[j], a[i]
            a[i + 1:] = reversed(a[i + 1:])

        for _ in range(k - 1):
            next_perm(nums)
        return "".join(map(str, nums))'''

_p60 = [S.load(k) for k in ("p60", "p60_next")]
import itertools as _it
for n in range(1, 8):
    perms = ["".join(map(str, p)) for p in _it.permutations(range(1, n + 1))]
    for k in range(1, len(perms) + 1):
        for sol in _p60:
            g = sol.getPermutation(n, k)
            assert g == perms[k - 1], ("P60", n, k, sol, g, perms[k - 1])
assert _p60[0].getPermutation(3, 3) == "213"
assert _p60[0].getPermutation(4, 9) == "2314"
assert _p60[0].getPermutation(9, 362880) == "987654321"
print("P60 solutions OK")

_P60_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">n = 4，k = 9（1-indexed）→ 先轉成 k = 8（0-indexed）</text>
            <text x="20" y="48" fill="var(--text-muted)" font-size="12">4 個數字的排列共 24 個，依第一位分成 4 組，每組 3! = 6 個</text>
            <g font-size="12" font-family="monospace">
              <text x="40" y="82" fill="var(--text-muted)">索引 0–5  ：第一位是 1</text>
              <text x="330" y="82" fill="var(--text-muted)">1234 1243 1324 1342 1423 1432</text>
              <text x="40" y="106" fill="var(--gold)">索引 6–11 ：第一位是 2  ← k = 8 落在這</text>
              <text x="330" y="106" fill="var(--gold)">2134 2143 2314 2341 2413 2431</text>
              <text x="40" y="130" fill="var(--text-muted)">索引 12–17：第一位是 3</text>
              <text x="40" y="154" fill="var(--text-muted)">索引 18–23：第一位是 4</text>
            </g>
            <line x1="20" y1="172" x2="620" y2="172" stroke="var(--border)"/>
            <g font-size="12" font-family="monospace">
              <text x="40" y="200" fill="var(--gold)">第 1 位：block = 3! = 6　idx = 8 // 6 = 1　→ 取候選[1] = &apos;2&apos;　k = 8 % 6 = 2</text>
              <text x="40" y="226" fill="var(--gold)">第 2 位：block = 2! = 2　idx = 2 // 2 = 1　→ 取候選[1] = &apos;3&apos;　k = 2 % 2 = 0</text>
              <text x="40" y="252" fill="var(--gold)">第 3 位：block = 1! = 1　idx = 0 // 1 = 0　→ 取候選[0] = &apos;1&apos;　k = 0</text>
              <text x="40" y="278" fill="var(--gold)">第 4 位：block = 0! = 1　idx = 0　　　　　→ 取候選[0] = &apos;4&apos;</text>
            </g>
            <text x="20" y="312" fill="#ff8a65" font-size="13">答案：&quot;2314&quot;　（候選清單每次都會移除已用的數字，所以永遠取得到）</text>'''

emit({
 "num": 60, "slug": "permutation-sequence",
 "en": [
   "The set <code>[1, 2, 3, ..., n]</code> contains a total of <code>n!</code> unique "
   "permutations. By listing and labeling all of the permutations in order, we get the "
   "sequence for <code>n = 3</code>: <code>\"123\", \"132\", \"213\", \"231\", \"312\", \"321\"</code>.",
   "Given <code>n</code> and <code>k</code>, return the <code>k</code>-th permutation sequence.",
 ],
 "zh": [
   "集合 <code>[1, 2, 3, ..., n]</code> 共有 <code>n!</code> 種不同的排列。"
   "把它們<strong>按字典序</strong>列出來並編號（從 1 開始），"
   "例如 <code>n = 3</code> 時依序是："
   "<code>\"123\", \"132\", \"213\", \"231\", \"312\", \"321\"</code>。",
   "給你 <code>n</code> 和 <code>k</code>，回傳<strong>第 <code>k</code> 個</strong>排列。",
 ],
 "pre": [
   ("note", "核心：排列的字典序有「分組」結構", [
     ("c", """n = 4 的 24 個排列，依「第一位是誰」分成 4 組：

    第一位是 1 -> 索引 0..5    （後面 3 個數字的 3! = 6 種排列）
    第一位是 2 -> 索引 6..11
    第一位是 3 -> 索引 12..17
    第一位是 4 -> 索引 18..23

所以「第 k 個排列的第一位是誰」可以直接算：
    idx = k // 3!        （k 用 0-indexed）

算完之後，k 減掉前面那些組，繼續決定第二位：
    k = k % 3!
    第二位的分組大小是 2!

這就是【階乘進位制（factorial number system / factoradic）】：

    8 (十進位)  =  1 × 3! + 1 × 2! + 0 × 1! + 0 × 0!
                =  (1, 1, 0, 0) 階乘進位

    而 (1, 1, 0, 0) 的意思是：
      第 1 位取「剩餘候選」的第 1 個
      第 2 位取「剩餘候選」的第 1 個
      第 3 位取「剩餘候選」的第 0 個
      第 4 位取「剩餘候選」的第 0 個

    這叫做 Lehmer code —— 排列和階乘進位數之間的一一對應。"""),
     "<strong>關鍵是「取剩餘候選的第幾個」而不是「取數字幾」</strong> —— "
     "因為用過的數字要從候選裡移除，索引會跟著變。",
   ]),
 ],
 "examples": """範例 1
  輸入：n = 3, k = 3
  輸出："213"

範例 2
  輸入：n = 4, k = 9
  輸出："2314"

範例 3
  輸入：n = 3, k = 1
  輸出："123\"""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 9",
   "1 ≤ <code>k</code> ≤ <code>n!</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 9</strong>，所以 <code>n!</code> 最大是 <code>9! = 362880</code>。"
       "這個數字剛好落在「生成所有排列會慢但不會爆」的邊緣 —— "
       "所以樸素做法（呼叫 k−1 次 next_permutation）能過，但慢很多。",
       "<strong>k 從 1 開始</strong>（1-indexed）。"
       "<strong>程式裡第一件事就是 <code>k -= 1</code></strong>，"
       "轉成 0-indexed 之後所有的除法和取模才會對。"
       "<strong>忘記減 1 是本題第一名的 bug。</strong>",
       "<strong>保證 <code>k ≤ n!</code></strong>，所以不用處理「k 太大」。",
       "<strong>數字是 1..9，剛好是一位數</strong>，所以答案可以直接字串串接，"
       "不用擔心多位數的問題。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P60_FIG, "0 0 640 326"),
 ],
 "approaches": [
   ap("解法一", "階乘進位制直接構造（標準解）", [
     ("c", S["p60"]),
     ("h", "三個關鍵"),
     ("c", """① k -= 1    轉成 0-indexed

   為什麼？因為除法的分組是從 0 開始的：
       k=0..5   -> 第一組（0 // 6 = 0）
       k=6..11  -> 第二組（6 // 6 = 1）

   如果不減 1，k=6 會算成 6//6 = 1（第二組），
   但 1-indexed 的第 6 個其實還在第一組（"1432"）。

② nums.pop(idx)    取走並移除

   候選清單必須「動態縮短」。
   n=4、第一位取了 '2' 之後，
   剩下的候選是 ['1','3','4']，
   第二位的 idx=1 對應的是 '3' 而不是 '2'。

   如果不移除，第二位的 idx=1 會取到 '2' —— 重複了。

③ block = fact[i-1]

   i 是「還剩幾個數字沒放」。
   固定第一位之後，剩下 i-1 個數字有 (i-1)! 種排法。
   所以每一組的大小是 (i-1)!。"""),
     ("h", "為什麼 <code>nums</code> 必須保持遞增？"),
     "因為「字典序」要求：<strong>索引小的候選，對應字典序小的排列。</strong>"
     "<code>nums</code> 一開始是 <code>['1','2',...,'n']</code>（遞增），"
     "而 <code>pop(idx)</code> 不會破壞剩下元素的相對順序 —— 所以它永遠保持遞增。",
     ("h", "複雜度"),
     "外層迴圈 n 次，每次 <code>nums.pop(idx)</code> 是 O(n)（list 要往前搬）。"
     "所以是 <strong>O(n²)</strong>。n ≤ 9 時完全無所謂。",
     "如果 n 很大，可以把 <code>nums</code> 換成<strong>樹狀陣列（Fenwick tree）</strong>"
     "或平衡樹來支援「找第 idx 個還沒用的數字」，做到 O(n log n)。"
     "但那是競賽等級的優化，面試不需要。",
   ], "O(n²)", "O(n)", "n 次迴圈 × pop 的 O(n)", "候選清單 + 階乘表", optimal=True),

   ap("解法二", "反覆呼叫「下一個排列」（對照組）", [
     ("c", S["p60_next"]),
     "正確，而且重複利用了第 31 題的演算法。"
     "<strong>但複雜度是 O(k · n)</strong> —— "
     "<code>k</code> 最大 362880，<code>n</code> 最大 9，約 300 萬次操作。"
     "LeetCode 上大概能過，但比解法一慢好幾百倍。",
     "<strong>什麼時候這個做法比較好？</strong>"
     "當 <code>k</code> 很小的時候（例如 k ≤ 10），"
     "或者當你「已經有一個排列，想要它後面的幾個」時。"
     "<strong>「直接跳到第 k 個」和「一步一步往前走」各有適用場合。</strong>",
   ], "O(k·n)", "O(n)", "呼叫 k−1 次", "只有排列本身"),
 ],
 "compare": (["解法", "時間", "k=9! 時", "適合", "備註"],
   [["一、階乘進位制", "O(n²)", "瞬間", "k 很大", "標準解"],
    ["二、next_permutation ×(k−1)", "O(k·n)", "約 300 萬次操作", "k 很小", "重用第 31 題"]]),
 "edges": [
   "<strong>k = 1</strong>：<code>(3, 1)</code> → <code>\"123\"</code>（最小的排列）。"
   "<code>k -= 1</code> 之後 <code>k = 0</code>，每一位都取候選的第 0 個。",
   "<strong>k = n!</strong>：<code>(3, 6)</code> → <code>\"321\"</code>（最大的排列）。"
   "<code>(9, 362880)</code> → <code>\"987654321\"</code>。",
   "<strong>n = 1</strong>：<code>(1, 1)</code> → <code>\"1\"</code>。",
   "<strong>忘記 <code>k -= 1</code></strong>：<code>(3, 3)</code> 會回傳 <code>\"231\"</code> "
   "而不是 <code>\"213\"</code>。",
   "<strong>忘記 <code>pop</code>（只用索引不移除）</strong>："
   "會產生重複的數字，例如 <code>\"2214\"</code>。",
   "<strong>階乘表的邊界</strong>：<code>fact[0] = 1</code>（0! = 1）。"
   "最後一位的 <code>block = fact[0] = 1</code>，<code>idx = k // 1 = k</code>，"
   "而此時 <code>k</code> 必然是 0，所以取候選的第 0 個（唯一剩下的那個）✔",
 ],
 "follow": [
   ("h", "追問一：反過來，給一個排列求它是第幾個？"),
   "這叫做<strong>求 Lehmer code</strong>（排列的排名，ranking）。",
   ("c", """對每一位 i，數出「它右邊有幾個比它小的數字」，設為 c_i。
然後排名 = Σ c_i × (n-1-i)!  （0-indexed），最後 +1 轉回 1-indexed。

"2314" 的排名：
    '2' 右邊比它小的：只有 '1'      -> c_0 = 1
    '3' 右邊比它小的：只有 '1'      -> c_1 = 1
    '1' 右邊比它小的：沒有          -> c_2 = 0
    '4' 右邊比它小的：沒有          -> c_3 = 0

    排名（0-indexed）= 1×3! + 1×2! + 0×1! + 0×0!
                     = 6 + 2 = 8
    1-indexed = 9 ✔

樸素做法是 O(n²)（每一位都往右數）。
用樹狀陣列可以做到 O(n log n)。

「排名（rank）」和「反排名（unrank）」是一對 ——
本題是 unrank，這個追問是 rank。""",),
   ("h", "追問二：如果集合裡有重複元素呢？"),
   "分組的大小就不再是 <code>(i-1)!</code>，而是「多重集合的排列數」"
   "<code>(i-1)! / ∏(cⱼ!)</code>。"
   "程式的骨架一樣，但每取走一個數字之後，要重新計算下一組的大小。"
   "<strong>比原題麻煩得多，但思路完全相同。</strong>",
   ("h", "追問三：這個「直接跳到第 k 個」的技巧還能用在哪？"),
   ("ul", [
     "<strong>第 22 題 Generate Parentheses</strong>：用卡塔蘭數算「走左分支有幾個答案」，"
     "就能直接定位第 k 個合法括號序列",
     "<strong>組合的第 k 個</strong>：用組合數 C(n,k) 分組",
     "<strong>子集合的第 k 個</strong>：直接用 k 的二進位表示",
     "<strong>格雷碼的第 k 個</strong>（第 89 題）：<code>k ^ (k &gt;&gt; 1)</code>",
   ]),
   "<strong>共同的模式：把「第 k 個」的問題，轉成「k 在某個進位制下的表示」。</strong>"
   "只要枚舉的結構有清楚的分組，就能跳過前面所有的答案直接算出目標。",
 ],
 "related": [
   "<strong>第 31 題 Next Permutation</strong> —— 一步一步往前走",
   "<strong>第 46／47 題 Permutations</strong> —— 生成全部",
   "<strong>第 89 題 Gray Code</strong> —— 另一個「第 k 個」有公式的枚舉",
   "<strong>第 22 題 Generate Parentheses</strong> —— 可以用同樣的技巧定位第 k 個",
 ],
 "check": [
   "為什麼第一件事就是 <code>k -= 1</code>？不減的話 <code>(3, 3)</code> 會回傳什麼？",
   "為什麼 <code>nums</code> 必須用 <code>pop</code> 移除，而不是只記錄「用過了」？",
   "<code>block = fact[i-1]</code> 在語意上代表什麼？",
   "反過來要算「<code>\"2314\"</code> 是第幾個」，該怎麼做？",
 ],
})
print("P60 written")
