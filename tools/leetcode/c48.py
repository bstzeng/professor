# -*- coding: utf-8 -*-
"""第 48–50 題。"""
import random, collections
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(48)

# ==================== 48. Rotate Image ====================
S["p48_transpose"] = '''class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 第 1 步：轉置（沿主對角線翻），只處理右上三角
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 第 2 步：每一列左右反轉
        for row in matrix:
            row.reverse()'''

S["p48_ring"] = '''class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # 一圈一圈往內做；n//2 圈就夠（奇數時正中間那格不用動）
        for layer in range(n // 2):
            first, last = layer, n - 1 - layer
            for i in range(first, last):
                offset = i - first

                top = matrix[first][i]                       # 先存上邊

                matrix[first][i] = matrix[last - offset][first]      # 左 -> 上
                matrix[last - offset][first] = matrix[last][last - offset]  # 下 -> 左
                matrix[last][last - offset] = matrix[i][last]        # 右 -> 下
                matrix[i][last] = top                                # 上 -> 右'''

_p48 = [S.load(k) for k in ("p48_transpose", "p48_ring")]


def _p48_ref(m):
    return [list(r) for r in zip(*m[::-1])]


for n in range(0, 7):
    m = [[random.randint(0, 99) for _ in range(n)] for _ in range(n)]
    e = _p48_ref(m)
    for sol in _p48:
        a = [r[:] for r in m]
        sol.rotate(a)
        assert a == e, ("P48", n, m, sol, a, e)
for _ in range(3000):
    n = random.randint(1, 6)
    m = [[random.randint(0, 99) for _ in range(n)] for _ in range(n)]
    e = _p48_ref(m)
    for sol in _p48:
        a = [r[:] for r in m]
        sol.rotate(a)
        assert a == e, ("P48", m, sol, a, e)
print("P48 solutions OK")

_P48_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">轉置 + 每列反轉 = 順時針旋轉 90°</text>
            <g font-size="15" text-anchor="middle">
              <text x="86" y="48" fill="var(--text-muted)" font-size="12">原矩陣</text>
              <rect x="40" y="60" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="57" y="83" fill="var(--accent)">1</text>
              <rect x="76" y="60" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="93" y="83" fill="var(--accent)">2</text>
              <rect x="112" y="60" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="129" y="83" fill="var(--accent)">3</text>
              <rect x="40" y="96" width="34" height="34" fill="none" stroke="var(--border)"/><text x="57" y="119" fill="var(--text-muted)">4</text>
              <rect x="76" y="96" width="34" height="34" fill="none" stroke="var(--border)"/><text x="93" y="119" fill="var(--text-muted)">5</text>
              <rect x="112" y="96" width="34" height="34" fill="none" stroke="var(--border)"/><text x="129" y="119" fill="var(--text-muted)">6</text>
              <rect x="40" y="132" width="34" height="34" fill="none" stroke="var(--border)"/><text x="57" y="155" fill="var(--text-muted)">7</text>
              <rect x="76" y="132" width="34" height="34" fill="none" stroke="var(--border)"/><text x="93" y="155" fill="var(--text-muted)">8</text>
              <rect x="112" y="132" width="34" height="34" fill="none" stroke="var(--border)"/><text x="129" y="155" fill="var(--text-muted)">9</text>
            </g>
            <text x="180" y="118" fill="var(--gold)" font-size="20" text-anchor="middle">→</text>
            <text x="180" y="140" fill="var(--gold)" font-size="11" text-anchor="middle">轉置</text>
            <g font-size="15" text-anchor="middle">
              <text x="286" y="48" fill="var(--text-muted)" font-size="12">轉置後</text>
              <rect x="240" y="60" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="257" y="83" fill="var(--accent)">1</text>
              <rect x="276" y="60" width="34" height="34" fill="none" stroke="var(--border)"/><text x="293" y="83" fill="var(--text-muted)">4</text>
              <rect x="312" y="60" width="34" height="34" fill="none" stroke="var(--border)"/><text x="329" y="83" fill="var(--text-muted)">7</text>
              <rect x="240" y="96" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="257" y="119" fill="var(--accent)">2</text>
              <rect x="276" y="96" width="34" height="34" fill="none" stroke="var(--border)"/><text x="293" y="119" fill="var(--text-muted)">5</text>
              <rect x="312" y="96" width="34" height="34" fill="none" stroke="var(--border)"/><text x="329" y="119" fill="var(--text-muted)">8</text>
              <rect x="240" y="132" width="34" height="34" fill="none" stroke="var(--accent)"/><text x="257" y="155" fill="var(--accent)">3</text>
              <rect x="276" y="132" width="34" height="34" fill="none" stroke="var(--border)"/><text x="293" y="155" fill="var(--text-muted)">6</text>
              <rect x="312" y="132" width="34" height="34" fill="none" stroke="var(--border)"/><text x="329" y="155" fill="var(--text-muted)">9</text>
            </g>
            <text x="380" y="118" fill="var(--gold)" font-size="20" text-anchor="middle">→</text>
            <text x="380" y="140" fill="var(--gold)" font-size="11" text-anchor="middle">每列反轉</text>
            <g font-size="15" text-anchor="middle">
              <text x="486" y="48" fill="var(--text-muted)" font-size="12">答案</text>
              <rect x="440" y="60" width="34" height="34" fill="none" stroke="#ff8a65"/><text x="457" y="83" fill="#ff8a65">7</text>
              <rect x="476" y="60" width="34" height="34" fill="none" stroke="#ff8a65"/><text x="493" y="83" fill="#ff8a65">4</text>
              <rect x="512" y="60" width="34" height="34" fill="none" stroke="#ff8a65"/><text x="529" y="83" fill="#ff8a65">1</text>
              <rect x="440" y="96" width="34" height="34" fill="none" stroke="var(--border)"/><text x="457" y="119" fill="var(--text-muted)">8</text>
              <rect x="476" y="96" width="34" height="34" fill="none" stroke="var(--border)"/><text x="493" y="119" fill="var(--text-muted)">5</text>
              <rect x="512" y="96" width="34" height="34" fill="none" stroke="var(--border)"/><text x="529" y="119" fill="var(--text-muted)">2</text>
              <rect x="440" y="132" width="34" height="34" fill="none" stroke="var(--border)"/><text x="457" y="155" fill="var(--text-muted)">9</text>
              <rect x="476" y="132" width="34" height="34" fill="none" stroke="var(--border)"/><text x="493" y="155" fill="var(--text-muted)">6</text>
              <rect x="512" y="132" width="34" height="34" fill="none" stroke="var(--border)"/><text x="529" y="155" fill="var(--text-muted)">3</text>
            </g>
            <text x="20" y="198" fill="var(--gold)" font-size="12">第一列 [1,2,3] 變成第三行（由上到下 1,2,3）→ 這正是順時針 90° 的定義</text>
            <text x="20" y="222" fill="var(--text-muted)" font-size="12">逆時針 90° = 轉置 + 每「行」反轉（或：每列先反轉再轉置）</text>'''

emit({
 "num": 48, "slug": "rotate-image",
 "en": [
   "You are given an <code>n x n</code> 2D <code>matrix</code> representing an image. "
   "Rotate the image by <strong>90 degrees (clockwise)</strong>.",
   "You have to rotate the image <strong>in-place</strong>, which means you have to modify the "
   "input 2D matrix directly. <strong>DO NOT</strong> allocate another 2D matrix and do the "
   "rotation.",
 ],
 "zh": [
   "給你一個 <code>n × n</code> 的二維矩陣 <code>matrix</code>，代表一張圖片。"
   "請把它<strong>順時針旋轉 90 度</strong>。",
   "必須<strong>原地</strong>旋轉，也就是直接修改輸入的矩陣。"
   "<strong>不能</strong>另外配置一個二維陣列。",
 ],
 "pre": [
   ("note", "先把「旋轉後誰跑到哪」寫清楚", [
     ("c", """順時針 90°：位置 (i, j) 的元素，會跑到 (j, n-1-i)

    1 2 3          7 4 1
    4 5 6    ->    8 5 2
    7 8 9          9 6 3

驗證：
    (0,0)=1 -> (0, 3-1-0) = (0,2)  ✔ 1 在右上角
    (0,2)=3 -> (2, 2)              ✔ 3 在右下角
    (2,0)=7 -> (0, 0)              ✔ 7 在左上角

反過來說（比較好用於「從新位置找舊值」）：
    new[i][j] = old[n-1-j][i]

四種基本變換：
    順時針 90°   ：轉置 + 每「列」反轉
    逆時針 90°   ：轉置 + 每「行」反轉
    180°         ：每列反轉 + 每行反轉（或整個陣列反轉兩次）
    轉置          ：沿主對角線鏡射

記法：「轉置」把矩陣翻到對角線的另一邊，
      再左右翻一次就轉成順時針；再上下翻就是逆時針。"""),
     "<strong>「不能配置另一個二維陣列」是整題的重點。</strong>"
     "沒有這條限制的話，<code>[list(r) for r in zip(*matrix[::-1])]</code> 一行就結束了。",
   ]),
 ],
 "examples": """範例 1
  輸入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
  輸出：[[7,4,1],[8,5,2],[9,6,3]]

範例 2
  輸入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
  輸出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]""",
 "constraints": [
   "<code>n == matrix.length == matrix[i].length</code>",
   "1 ≤ <code>n</code> ≤ 20",
   "−1000 ≤ <code>matrix[i][j]</code> ≤ 1000",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>保證是正方形</strong>（<code>n × n</code>）。"
       "非正方形的矩陣<strong>無法原地旋轉</strong>（形狀會變），只能建新的。",
       "<strong>n ≤ 20</strong>，效率完全不是問題。這題考的是<strong>索引推導</strong>。",
       "<strong>必須原地</strong>。在 Python 裡要小心："
       "<code>matrix = [...]</code> 只改區域變數，"
       "必須用 <code>matrix[i][j] = ...</code> 或 <code>matrix[:] = ...</code>。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P48_FIG, "0 0 640 234"),
 ],
 "approaches": [
   ap("解法一", "轉置 + 每列反轉（最推薦）", [
     ("c", S["p48_transpose"]),
     ("h", "為什麼內層是 <code>range(i + 1, n)</code>？"),
     ("c", """轉置是「交換 (i,j) 和 (j,i)」。

如果內層寫 range(n)，每一對會被交換「兩次」：
    i=0, j=1 時交換 (0,1) 和 (1,0)
    i=1, j=0 時又交換 (1,0) 和 (0,1)  -> 換回去了！

結果是完全沒變。

只處理右上三角（j > i）就每一對只交換一次 ✔
對角線上的元素（i == j）不用動（自己和自己交換）。"""),
     ("h", "為什麼「轉置 + 每列反轉」就是順時針 90°？"),
     ("c", """轉置：      (i, j) -> (j, i)
每列反轉：  (i, j) -> (i, n-1-j)

合起來：    (i, j) -> (j, i) -> (j, n-1-i)

而順時針 90° 的定義就是 (i, j) -> (j, n-1-i)  ✔

換個角度看：
    原矩陣的「第 0 列」是 [1, 2, 3]
    旋轉後它應該變成「最右邊那一行」，由上到下是 1, 2, 3

    轉置後第 0 列變成第 0 行（由上到下 1, 2, 3）—— 位置錯了，在最左邊
    每列反轉把最左邊的那一行翻到最右邊 ✔"""),
     "<strong>兩趟、各 O(n²)，總共還是 O(n²)，而且完全不用推「四格輪換」的索引。</strong>"
     "面試時這是最不容易寫錯的寫法。",
     ("h", "Python 的一行版（但違反題目要求）"),
     ("c", """matrix[:] = [list(r) for r in zip(*matrix[::-1])]

zip(*matrix[::-1]) 做了什麼？
    matrix[::-1]  把列的順序倒過來（上下翻轉）
    zip(*...)     轉置

    上下翻轉 + 轉置 = 順時針 90°（和「轉置 + 左右翻轉」等價）

用 matrix[:] = ... 確實會改到原物件，
但它在過程中建了一個新的二維結構 —— 嚴格說不算 O(1) 空間。
面試時可以提，但要說清楚它不符合「不配置另一個二維陣列」。"""),
   ], "O(n²)", "O(1)", "掃兩遍", "只用幾個變數", optimal=True),

   ap("解法二", "一圈一圈、四格輪換", [
     "更「直接」的做法：<strong>每次同時搬動四個互為旋轉關係的格子</strong>，一圈一圈往內做。",
     ("c", S["p48_ring"]),
     ("c", """n = 4 的兩圈：

    ┌───────────────┐
    │ o o o o       │  layer 0（外圈）：first=0, last=3
    │ o + + o       │  layer 1（內圈）：first=1, last=2
    │ o + + o       │
    │ o o o o       │
    └───────────────┘

每一圈要處理 (last - first) 組四元組。
  layer 0： i 從 0 到 2，共 3 組（4 個邊各 3 格，角落不重複）
  layer 1： i 從 1 到 1，共 1 組

n 是奇數時，正中間那一格不需要動（它旋轉後還在原地），
所以迴圈是 range(n // 2)，剛好跳過它。"""),
     ("h", "四格輪換的順序"),
     ("c", """對外圈的第 i 個位置（offset = i - first）：

    上： matrix[first][i]
    右： matrix[i][last]
    下： matrix[last][last - offset]
    左： matrix[last - offset][first]

順時針旋轉表示：上 -> 右 -> 下 -> 左 -> 上

實作時要「反著搬」（否則會覆蓋掉還沒用到的值）：
    先把「上」存起來
    左 -> 上
    下 -> 左
    右 -> 下
    上（暫存的）-> 右

這就像交換兩個變數要用 temp 一樣，
只是這裡是四個變數的環狀輪換。"""),
     "<strong>優點</strong>：只掃一遍，常數比解法一小一半。"
     "<strong>缺點</strong>：四個索引公式非常容易寫錯，"
     "而且 <code>last - offset</code> 這種寫法要推導才看得懂。",
     "<strong>面試建議</strong>：講出這個做法存在（展示你想過），但寫解法一。"
     "如果面試官特別要求「只掃一遍」再寫這個。",
   ], "O(n²)", "O(1)", "每個元素只搬一次", "一個暫存變數"),
 ],
 "compare": (["解法", "掃幾遍", "空間", "容易寫錯？", "備註"],
   [["一、轉置 + 反轉", "2", "O(1)", "✘ 很好寫", "面試預設"],
    ["二、四格輪換", "1", "O(1)", "✔ 索引難推", "常數較小"]]),
 "edges": [
   "<strong>n = 1</strong>：<code>[[1]]</code> → <code>[[1]]</code>。什麼都不用做。",
   "<strong>n = 2</strong>：<code>[[1,2],[3,4]]</code> → <code>[[3,1],[4,2]]</code>。"
   "解法二只有一圈、一組四元組。",
   "<strong>n 是奇數</strong>：<code>n = 3</code> 時正中間 <code>(1,1)</code> 不動。"
   "<code>range(n // 2) = range(1)</code> 剛好跳過它。",
   "<strong>轉置寫成 <code>range(n)</code></strong>：矩陣完全沒變（每對交換兩次）。"
   "<strong>這是最常見的 bug。</strong>",
   "<strong>Python 的原地陷阱</strong>：<code>matrix = 新矩陣</code> 不會改到呼叫端。",
   "<strong>有負數</strong>：<code>[[-1,0],[1,-2]]</code>。不影響邏輯，但不要用某個數字當哨兵。",
 ],
 "follow": [
   ("h", "追問一：逆時針 90° 呢？"),
   "<strong>轉置 + 每「行」反轉</strong>（或等價地：每列先反轉，再轉置）。",
   ("c", """順時針：  transpose(m); for row in m: row.reverse()
逆時針：  transpose(m); m.reverse()          # 反轉「列的順序」

驗證逆時針：
    (i, j) -> transpose -> (j, i) -> 列順序反轉 -> (n-1-j, i)
    逆時針 90° 的定義就是 (i, j) -> (n-1-j, i)  ✔

180°：     m.reverse(); for row in m: row.reverse()
           等價於 (i,j) -> (n-1-i, n-1-j)""",),
   ("h", "追問二：如果不是正方形呢？"),
   "<strong>無法原地旋轉。</strong>"
   "<code>m × n</code> 的矩陣旋轉後變成 <code>n × m</code>，形狀改變，"
   "而 Python 的 list of list 沒辦法在不重新配置的情況下改變形狀。"
   "只能建一個新的：<code>[list(r) for r in zip(*matrix[::-1])]</code>。",
   "<strong>但如果資料是存在一維陣列裡的</strong>（像真正的影像緩衝區），"
   "就可以用「置換環（permutation cycle）」的方式原地重排 —— "
   "那是一個相當漂亮但複雜的演算法（in-place matrix transposition），"
   "需要走遍每個置換環。",
   ("h", "追問三：真實的影像旋轉是怎麼做的？"),
   ("ul", [
     "<strong>90° 的倍數</strong>：就是本題的做法（純粹的記憶體搬移，無損）。"
     "實務上還要考慮<strong>快取友善性</strong> —— "
     "按「區塊（tile）」旋轉比按整列旋轉快很多，因為它讓讀寫都落在同一個快取行附近。",
     "<strong>任意角度</strong>：完全不同的問題。"
     "旋轉後的像素位置不是整數，需要<strong>插值</strong>"
     "（最近鄰、雙線性、雙三次），而且會有鋸齒和資訊損失。"
     "標準做法是「反向映射」：對每個輸出像素，算出它在原圖的位置，再插值取值。",
   ]),
   ("h", "追問四：為什麼「轉置 + 反轉」比「四格輪換」不容易錯？"),
   "因為它<strong>把一個複雜的置換拆成兩個簡單的置換</strong>。"
   "<code>(i,j) → (j,n-1-i)</code> 很難一眼驗證，"
   "但 <code>(i,j) → (j,i)</code> 和 <code>(i,j) → (i,n-1-j)</code> 都是「一看就對」的。"
   "<strong>把複雜的變換分解成簡單變換的複合，是幾何與線性代數的通用策略</strong> —— "
   "旋轉矩陣本身也常被分解成剪切（shear）的複合。",
 ],
 "related": [
   "<strong>第 54／59 題 Spiral Matrix</strong> —— 另一種「一圈一圈」的走法",
   "<strong>第 73 題 Set Matrix Zeroes</strong> —— 另一個原地矩陣操作",
   "<strong>第 867 題 Transpose Matrix</strong> —— 只做轉置（可以不是正方形）",
   "<strong>第 189 題 Rotate Array</strong> —— 一維版的旋轉，也是「反轉三次」",
 ],
 "check": [
   "轉置的內層迴圈為什麼是 <code>range(i+1, n)</code>？寫成 <code>range(n)</code> 會怎樣？",
   "請驗證「轉置 + 每列反轉」的複合映射確實是 <code>(i,j) → (j, n-1-i)</code>。",
   "逆時針 90° 要怎麼做？和順時針差在哪一步？",
   "為什麼非正方形的矩陣無法原地旋轉？",
 ],
})
print("P48 written")

# ==================== 49. Group Anagrams ====================
S["p49_sort"] = '''from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))     # 字母重排後相同 -> 同一組
            groups[key].append(s)
        return list(groups.values())'''

S["p49_count"] = '''from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            groups[tuple(count)].append(s)   # tuple 才能當 dict 的 key
        return list(groups.values())'''

S["p49_prime"] = '''from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 每個字母配一個質數，字串的 key = 所有字母的質數乘積
        # 由算術基本定理，乘積相同 <=> 字母組成相同
        PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                  43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

        groups = defaultdict(list)
        for s in strs:
            key = 1
            for ch in s:
                key *= PRIMES[ord(ch) - ord("a")]
            groups[key].append(s)
        return list(groups.values())'''

_p49 = [S.load(k) for k in ("p49_sort", "p49_count", "p49_prime")]


def _norm49(res):
    return sorted(tuple(sorted(g)) for g in res)


for c in [["eat", "tea", "tan", "ate", "nat", "bat"], [""], ["a"], [],
          ["abc", "cba", "bac", "xyz"], ["", "", "b"]]:
    e = _norm49(_p49[0].groupAnagrams(list(c)))
    for sol in _p49:
        g = _norm49(sol.groupAnagrams(list(c)))
        assert g == e, ("P49", c, sol, g, e)
for _ in range(2000):
    c = ["".join(random.choice("abc") for _ in range(random.randint(0, 4)))
         for _ in range(random.randint(0, 8))]
    e = _norm49(_p49[0].groupAnagrams(list(c)))
    for sol in _p49:
        g = _norm49(sol.groupAnagrams(list(c)))
        assert g == e, ("P49", c, sol, g, e)
print("P49 solutions OK")

emit({
 "num": 49, "slug": "group-anagrams",
 "en": [
   "Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. "
   "You can return the answer in <strong>any order</strong>.",
   "An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a "
   "different word or phrase, typically using all the original letters exactly once.",
 ],
 "zh": [
   "給你一個字串陣列 <code>strs</code>，把<strong>字母異位詞</strong>分到同一組。"
   "回傳的順序不拘。",
   "<strong>字母異位詞</strong>指的是：用完全相同的字母（含數量）重新排列而成的字串。"
   "例如 <code>\"eat\"</code>、<code>\"tea\"</code>、<code>\"ate\"</code> 互為異位詞。",
 ],
 "pre": [
   ("note", "整題只有一個問題：怎麼設計 key？", [
     ("c", """所有解法的骨架都一樣：

    groups = defaultdict(list)
    for s in strs:
        groups[key(s)].append(s)
    return list(groups.values())

唯一的差別是 key(s) 怎麼算。

key 必須滿足：
    「兩個字串互為異位詞」  <=>  「它們的 key 相同」

三種 key 設計：
    ① 排序後的字串     "eat" -> "aet"
    ② 26 個字母的計數  "eat" -> (1,0,0,0,1,0,...,1,0,...)
    ③ 質數乘積        "eat" -> 5 × 2 × 71 = 710

而 key 必須是「可雜湊的（hashable）」——
所以計數要用 tuple 而不是 list。"""),
     "<strong>「設計一個好的 key」是雜湊表題目的核心技能。</strong>"
     "一旦 key 對了，剩下的就是三行。",
   ]),
 ],
 "examples": """範例 1
  輸入：strs = ["eat","tea","tan","ate","nat","bat"]
  輸出：[["bat"],["nat","tan"],["ate","eat","tea"]]

範例 2
  輸入：strs = [""]
  輸出：[[""]]

範例 3
  輸入：strs = ["a"]
  輸出：[["a"]]""",
 "constraints": [
   "1 ≤ <code>strs.length</code> ≤ 10⁴",
   "0 ≤ <code>strs[i].length</code> ≤ 100（<strong>可以是空字串</strong>）",
   "<code>strs[i]</code> 只含<strong>小寫英文字母</strong>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>只有小寫英文字母（26 種）</strong> —— "
       "這是「用長度 26 的計數陣列當 key」（解法二）能成立的前提。",
       "<strong>字串可以是空的</strong>。空字串和空字串互為異位詞，會被分到同一組。"
       "三種 key 都自然處理（空的排序還是空、計數全 0、乘積是 1）。",
       "<strong>n ≤ 10⁴、每個長度 ≤ 100</strong>。"
       "所以 <code>k</code>（平均字串長度）不大，"
       "<code>O(n · k log k)</code> 的排序法完全夠用。",
     ]),
   ]),
 ],
 "idea": [
   ("t", ["key 設計", "計算成本", "key 大小", "有沒有隱憂"],
     [["排序後的字串", "O(k log k)", "k 個字元", "無"],
      ["26 格計數 tuple", "O(k)", "固定 26", "字元集大時 key 變大"],
      ["質數乘積", "O(k)", "一個大整數", "在定長整數語言會溢位"]]),
 ],
 "approaches": [
   ap("解法一", "排序當 key（最推薦）", [
     ("c", S["p49_sort"]),
     "三行。<code>sorted(\"eat\")</code> 得到 <code>['a','e','t']</code>，"
     "<code>\"\".join(...)</code> 變成 <code>\"aet\"</code>。"
     "<strong>異位詞排序後一定相同</strong> —— 這是定義的直接推論。",
     ("h", "為什麼 <code>defaultdict(list)</code>？"),
     "省掉 <code>if key not in groups: groups[key] = []</code> 這一行。"
     "<code>defaultdict(list)</code> 在存取不存在的 key 時會自動建一個空 list。"
     "<strong>這是 Python 處理「分組」時的標準工具。</strong>",
     ("h", "複雜度"),
     "<code>n</code> 個字串，平均長度 <code>k</code>。"
     "每個字串排序 O(k log k)，總共 <strong>O(n · k log k)</strong>。"
     "k ≤ 100 的話 <code>log k ≈ 7</code>，完全可以接受。",
     "<strong>實務上這是最好的選擇</strong>：最短、最清楚、沒有任何隱憂。"
     "解法二的 O(n·k) 在理論上更好，但常數（建 tuple、雜湊 26 個元素）"
     "往往抵銷掉那個 log k。",
   ], "O(n·k log k)", "O(n·k)", "每個字串排序一次", "所有字串 + key", optimal=True),

   ap("解法二", "26 格計數當 key（理論上最快）", [
     ("c", S["p49_count"]),
     ("c", """"eat" 的計數：
    索引:  0(a) 1(b) 2(c) 3(d) 4(e) ... 19(t) ...
    值:     1    0    0    0    1   ...   1   ...

key = (1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0)

"tea" 和 "ate" 算出來完全一樣 ✔"""),
     "<strong>為什麼要 <code>tuple(count)</code> 而不是直接用 <code>count</code>？</strong>"
     "因為 Python 的 <code>list</code> 是可變的，<strong>不可雜湊</strong>，"
     "不能當 dict 的 key。<code>tuple</code> 是不可變的，可以。"
     "<strong>忘記轉 tuple 會直接 <code>TypeError: unhashable type: 'list'</code>。</strong>",
     ("h", "理論上 O(n·k) 比 O(n·k log k) 好，實務上呢？"),
     ("c", """理論：  O(n·k) < O(n·k log k)

實務（k = 100，26 個字母）：
    排序法：  一次 sorted() 是高度優化的 C 實作（Timsort）
              key 是長度 100 的字串，雜湊很快

    計數法：  建一個 26 元素的 list，逐字元累加（Python 迴圈，慢）
              轉成 tuple，雜湊 26 個整數

    在 CPython 裡，排序法通常「更快」——
    因為 sorted() 和字串雜湊都在 C 層跑，
    而計數法的逐字元迴圈在 Python 層跑。

    如果字串很長（k >> 26），計數法才會贏。
    如果字串很短（k < 26），計數法反而浪費（key 比字串還大）。

結論：漸近複雜度不是唯一標準，常數和實作語言都重要。"""),
     "<strong>但在 C++ / Java 裡，計數法明顯更快</strong>，"
     "因為那些語言的逐字元迴圈沒有 Python 的直譯開銷。",
   ], "O(n·k)", "O(n·k)", "每個字元掃一次", "所有字串 + n 個 26 元組"),

   ap("解法三", "質數乘積當 key（漂亮但危險）", [
     "利用<strong>算術基本定理</strong>：每個正整數的質因數分解是唯一的。"
     "所以「字母的質數乘積」和「字母的組成」是一一對應的。",
     ("c", S["p49_prime"]),
     ("c", """a=2, b=3, c=5, d=7, e=11, ...

"abc" -> 2 × 3 × 5 = 30
"bca" -> 3 × 5 × 2 = 30  ✔ 相同（乘法交換律）
"abb" -> 2 × 3 × 3 = 18  ✘ 和 "abc" 不同

為什麼保證不會碰撞？
    算術基本定理：30 = 2 × 3 × 5 是唯一的分解。
    所以 key = 30 只可能來自「一個 a、一個 b、一個 c」。

漂亮的地方：
    「字母的多重集合」這個抽象概念，
    被編碼成「一個整數」，而且完全無損。"""),
     ("h", "為什麼實務上不該用？"),
     ("c", """字串長度 100、全是 'z'（質數 101）：

    key = 101^100 ≈ 10^200

    Python：沒問題（任意精度整數），但大整數的乘法和雜湊很慢
    C++/Java：早就溢位了

    溢位之後會發生什麼？
        值會環繞成某個「看起來隨機」的數字。
        兩個不同的字母組合可能環繞到同一個值 -> 碰撞 -> 答案錯。
        而且這種錯誤「很難重現」——
        只有特定的長字串才會撞，測資通常測不出來。

    有人會說「模一個大質數就好」——
    但那就不再是「唯一分解」了，只是一個雜湊函式，
    碰撞機率雖低但不是 0，而且你失去了「保證正確」這個唯一的優點。

所以：這個解法值得知道（它很漂亮，而且展示了數論的應用），
      但不該在正式程式碼裡用。"""),
     "<strong>面試時提到它會加分</strong>（顯示你想得夠多），"
     "但一定要主動說明溢位的問題 —— 不然反而像是不知道風險。",
   ], "O(n·k)", "O(n·k)", "每個字元一次乘法", "大整數 key"),
 ],
 "compare": (["解法", "時間", "key 大小", "安全？", "實務推薦"],
   [["一、排序", "O(n·k log k)", "k", "✔", "★★★★★"],
    ["二、26 格計數", "O(n·k)", "26", "✔", "★★★★☆（C++/Java 更好）"],
    ["三、質數乘積", "O(n·k)", "大整數", "✘ 會溢位", "★☆☆☆☆ 只當談資"]]),
 "edges": [
   "<strong>空字串</strong>：<code>[\"\"]</code> → <code>[[\"\"]]</code>。三種 key 都能處理。",
   "<strong>多個空字串</strong>：<code>[\"\", \"\", \"b\"]</code> → 兩組。",
   "<strong>單一字串</strong>：<code>[\"a\"]</code> → <code>[[\"a\"]]</code>。",
   "<strong>完全沒有異位詞</strong>：<code>[\"abc\",\"xyz\"]</code> → 兩組，各一個。",
   "<strong>全部互為異位詞</strong>：<code>[\"abc\",\"cba\",\"bac\"]</code> → 一組三個。",
   "<strong>重複的字串</strong>：<code>[\"a\",\"a\"]</code> → 一組兩個（不去重）。",
   "<strong>忘記 <code>tuple(count)</code></strong>：<code>TypeError: unhashable type: 'list'</code>。",
 ],
 "follow": [
   ("h", "追問一：如果字元集很大（例如 Unicode）呢？"),
   "26 格計數法就不能用了（開 10 萬格的陣列太浪費）。改用：",
   ("ul", [
     "<strong>排序法</strong>：完全不受影響，key 的大小和字串一樣長。",
     "<strong><code>Counter</code> 的 <code>frozenset(items)</code></strong>："
     "<code>frozenset(Counter(s).items())</code>，只存出現過的字元。稀疏但可雜湊。",
   ]),
   "<strong>這是排序法勝出的場景</strong> —— 它對字元集大小完全不敏感。",
   ("h", "追問二：如果要「串流」處理（字串一個一個進來）呢？"),
   "三種解法都天然支援 —— 它們本來就是「逐一處理」。"
   "只要改成「每次進來一個就更新 groups，並回報它屬於哪一組」即可。",
   ("h", "追問三：怎麼判斷「兩個字串是不是異位詞」（單一比對）？"),
   "第 242 題。不需要建 dict，直接比較："
   "<code>sorted(s) == sorted(t)</code>（O(k log k)）"
   "或 <code>Counter(s) == Counter(t)</code>（O(k)）。"
   "<strong>先檢查長度是否相同</strong>可以提早退出，是很值得寫的一行。",
   ("h", "追問四：這題背後的抽象概念是什麼？"),
   "<strong>「等價類（equivalence class）」與「標準形（canonical form）」。</strong>",
   ("c", """「互為異位詞」是一個等價關係：
    自反：s 和自己互為異位詞 ✔
    對稱：s~t 則 t~s ✔
    遞移：s~t 且 t~u 則 s~u ✔

而 key(s) 就是「s 所屬等價類的標準形」——
同一類的所有元素算出同一個 key。

這個模式在很多地方出現：
    分數化簡（1/2 和 2/4 的標準形都是 1/2）
    圖同構的判定（canonical labeling）
    編譯器的常數摺疊與公共子表達式消除
    快取的 key 正規化（URL 的 query 參數排序）

「找一個標準形，然後用雜湊表分組」是這一整類問題的通用解法。"""),
 ],
 "related": [
   "<strong>第 242 題 Valid Anagram</strong> —— 單一比對版",
   "<strong>第 438 題 Find All Anagrams in a String</strong> —— 滑動視窗找異位詞",
   "<strong>第 567 題 Permutation in String</strong> —— 同上",
   "<strong>第 819／1002 題</strong> —— 其他字元計數題",
 ],
 "check": [
   "為什麼計數法一定要 <code>tuple(count)</code>？不轉會怎樣？",
   "質數乘積法在 Java 裡會出什麼問題？為什麼「模一個大質數」不能完全解決？",
   "排序法的 O(n·k log k) 比計數法的 O(n·k) 差，為什麼在 Python 裡反而通常更快？",
   "如果字元集是完整的 Unicode，三種解法各會怎樣？",
 ],
})
print("P49 written")
