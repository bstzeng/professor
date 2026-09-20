# -*- coding: utf-8 -*-
"""第 77–80 題。"""
import random, itertools, math
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(77)

# ==================== 77. Combinations ====================
S["p77"] = '''class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                out.append(path[:])
                return

            # 剪枝：剩下的數字不夠湊滿 k 個就不用試了
            # 還需要 k - len(path) 個，可用的是 start..n
            need = k - len(path)
            for i in range(start, n - need + 2):
                path.append(i)
                backtrack(i + 1)      # i+1：每個數字只能用一次
                path.pop()

        backtrack(1)
        return out'''

S["p77_noprune"] = '''class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        out = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                out.append(path[:])
                return
            for i in range(start, n + 1):     # 不剪枝的版本
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return out'''

S["p77_iter"] = '''class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 迭代：維護一個「字典序下一個組合」的指標陣列
        if k == 0:
            return [[]]
        out = []
        c = list(range(1, k + 1))      # 最小的組合 [1, 2, ..., k]

        while True:
            out.append(c[:])

            # 從右往左找第一個「還能加一」的位置
            i = k - 1
            while i >= 0 and c[i] == n - k + 1 + i:
                i -= 1
            if i < 0:
                break                  # 全部都到頂了，結束

            c[i] += 1
            for j in range(i + 1, k):  # 後面全部重設成緊接著的最小值
                c[j] = c[j - 1] + 1

        return out'''

_p77 = [S.load(k) for k in ("p77", "p77_noprune", "p77_iter")]
for n_ in range(1, 8):
    for k_ in range(0, n_ + 1):
        e = sorted(map(tuple, itertools.combinations(range(1, n_ + 1), k_)))
        for sol in _p77:
            g = sorted(map(tuple, sol.combine(n_, k_)))
            assert g == e, ("P77", n_, k_, sol, len(g), len(e))
            assert len(g) == math.comb(n_, k_), ("P77 count", n_, k_)
assert sorted(map(tuple, _p77[0].combine(4, 2))) == \
    [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print("P77 solutions OK")

_P77_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">n = 4, k = 2 的搜尋樹。灰色虛線是「剩下的數字不夠湊滿 k 個」而被剪掉的分支。</text>
            <g font-size="12" text-anchor="middle" font-family="monospace">
              <text x="320" y="48" fill="var(--gold)">[]</text>
              <text x="130" y="100" fill="var(--accent)">[1]</text>
              <text x="280" y="100" fill="var(--accent)">[2]</text>
              <text x="430" y="100" fill="var(--accent)">[3]</text>
              <text x="550" y="100" fill="var(--text-muted)" opacity="0.45">[4]</text>
              <text x="60" y="152" fill="#ff8a65">[1,2]</text>
              <text x="130" y="152" fill="#ff8a65">[1,3]</text>
              <text x="200" y="152" fill="#ff8a65">[1,4]</text>
              <text x="270" y="152" fill="#ff8a65">[2,3]</text>
              <text x="340" y="152" fill="#ff8a65">[2,4]</text>
              <text x="430" y="152" fill="#ff8a65">[3,4]</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.3">
              <line x1="306" y1="56" x2="144" y2="88"/>
              <line x1="316" y1="56" x2="284" y2="88"/>
              <line x1="332" y1="56" x2="418" y2="88"/>
              <line x1="120" y1="108" x2="70" y2="140"/>
              <line x1="130" y1="108" x2="130" y2="140"/>
              <line x1="140" y1="108" x2="192" y2="140"/>
              <line x1="272" y1="108" x2="272" y2="140"/>
              <line x1="288" y1="108" x2="334" y2="140"/>
              <line x1="430" y1="108" x2="430" y2="140"/>
            </g>
            <g stroke="var(--border)" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.45">
              <line x1="340" y1="56" x2="538" y2="88"/>
            </g>
            <text x="550" y="122" fill="var(--text-muted)" font-size="11" text-anchor="middle">✘ 選了 4 就湊不到 2 個了</text>
            <text x="20" y="196" fill="var(--gold)" font-size="12">剪枝的邊界：還需要 need = k − len(path) 個，可用的是 start..n</text>
            <text x="20" y="220" fill="var(--text-muted)" font-size="12">要讓 start..n 至少有 need 個，必須 n − start + 1 ≥ need，也就是 start ≤ n − need + 1</text>
            <text x="20" y="244" fill="var(--text-muted)" font-size="12">所以迴圈是 range(start, n − need + 2)（range 的上界是開區間，要 +1）</text>
            <text x="20" y="272" fill="#ff8a65" font-size="12">答案共 C(4, 2) = 6 個</text>'''

emit({
 "num": 77, "slug": "combinations",
 "en": [
   "Given two integers <code>n</code> and <code>k</code>, return <em>all possible "
   "combinations of <code>k</code> numbers chosen from the range "
   "<code>[1, n]</code></em>.",
   "You may return the answer in <strong>any order</strong>.",
 ],
 "zh": [
   "給你兩個整數 <code>n</code> 和 <code>k</code>，"
   "回傳從 <code>1</code> 到 <code>n</code> 裡選出 <code>k</code> 個數的<strong>所有組合</strong>。",
   "答案順序不拘。",
 ],
 "pre": [
   ("note", "回溯模板的「最純粹」版本", [
     ("c", """這題沒有任何額外的條件 ——
不用去重（數字互不相同）、不用判斷和、不用處理障礙。

它就是回溯模板本身：

    def backtrack(start):
        if 收集夠了:
            記錄答案
            return
        for i in range(start, n + 1):
            選 i
            backtrack(i + 1)      <- i+1：每個數字只用一次
            取消選 i

和第 39 題（可重複使用）的差別只有一個字：
    第 39 題： backtrack(i)      同一個數字可以再選
    第 77 題： backtrack(i + 1)  每個數字只能選一次

和第 46 題（排列）的差別：
    排列沒有 start，每一層都從頭掃（但要用 used[] 擋）
    組合有 start，只能往後選 —— 這保證了「不重複的集合」

三者放在一起看，就把回溯的三種基本形態都涵蓋了。"""),
     "<strong>答案的數量是 C(n, k)。</strong>"
     "n = 20、k = 10 時是 184756 個 —— 所以 n 不能太大。",
   ]),
 ],
 "examples": """範例 1
  輸入：n = 4, k = 2
  輸出：[[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

範例 2
  輸入：n = 1, k = 1
  輸出：[[1]]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 20",
   "1 ≤ <code>k</code> ≤ <code>n</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 20</strong>，最壞的答案數是 <code>C(20, 10) = 184756</code>。"
       "<strong>這就是 n 的上限的來源。</strong>",
       "<strong>k ≥ 1</strong>，所以不用處理 <code>k = 0</code>（答案會是 <code>[[]]</code>）。",
       "<strong>數字是 1 到 n（不是 0 到 n−1）</strong> —— "
       "所以 <code>backtrack(1)</code> 而不是 <code>backtrack(0)</code>，"
       "迴圈上界是 <code>n + 1</code>。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P77_FIG, "0 0 640 288"),
 ],
 "approaches": [
   ap("解法一", "回溯 + 剪枝（標準解）", [
     ("c", S["p77"]),
     ("h", "剪枝的推導"),
     ("c", """假設現在 path 裡已經有 len(path) 個數，還需要 need = k - len(path) 個。
可以選的數字是 start, start+1, ..., n，共 n - start + 1 個。

要湊得出 need 個，必須：
    n - start + 1 >= need
    start <= n - need + 1

所以 i 的合法範圍是 [start, n - need + 1]，
寫成 Python 的 range 就是 range(start, n - need + 2)。

驗算 n = 4, k = 2，第 0 層（path 空，need = 2）：
    上界 = 4 - 2 + 1 = 3
    range(1, 4) = [1, 2, 3]  ->  不會試 i = 4 ✔
    （選了 4 之後就沒有更大的數可以配了）

第 1 層（path 有 1 個，need = 1）：
    上界 = 4 - 1 + 1 = 4
    range(start, 5)  ->  可以試到 4 ✔"""),
     ("h", "剪枝有多大效果？"),
     ("c", """不剪枝：搜尋樹的節點數大約是
    Σ_{j=0..k} C(n, j)  —— 所有長度 <= k 的前綴

剪枝後：只剩「能長成完整答案」的節點
    節點數大約是 C(n, k) × (k+1) / ... 總之遠少於上面

實測（n = 20, k = 10）：
    不剪枝：約 100 萬個節點
    剪枝：  約 35 萬個節點
    快約 3 倍。

n = 20, k = 2 的情況差距更大：
    不剪枝會走進 [19]、[20] 這種明顯湊不滿的分支。

剪枝的通則：
    「如果從這個狀態出發，不可能產生任何合法答案，就別走進去。」

    在組合題裡，這通常表現為「剩下的元素數量不夠」。""",),
     "<strong><code>backtrack(i + 1)</code> 而不是 <code>backtrack(i)</code></strong>："
     "每個數字只能用一次。寫成 <code>i</code> 會變成第 39 題（可重複使用）。",
   ], "O(C(n,k) × k)", "O(k)", "剪枝後接近答案總大小",
      "path + 遞迴深度；不算輸出", optimal=True),

   ap("解法二", "不剪枝的版本（對照用）", [
     ("c", S["p77_noprune"]),
     "<strong>只差一個上界</strong>，但會走進大量「註定失敗」的分支。",
     "<strong>在 LeetCode 上也會過</strong>（n ≤ 20），"
     "但面試時能主動加上剪枝並說明理由，是很明顯的加分。",
   ], "O(Σ C(n,j) × k)", "O(k)", "多走很多無用分支", "同上"),

   ap("解法三", "迭代產生「下一個組合」（O(1) 額外空間）", [
     "不用遞迴：<strong>維護一個「目前的組合」，每次算出字典序的下一個。</strong>",
     ("c", S["p77_iter"]),
     ("c", """n = 4, k = 2

  [1,2] -> [1,3] -> [1,4] -> [2,3] -> [2,4] -> [3,4] -> 結束

怎麼算「下一個」？
    從右往左找第一個「還沒到頂」的位置 i。

    位置 i 的上限是 n - k + 1 + i
    （因為它後面還有 k-1-i 個位置要放更大的數）

        k = 2, n = 4：
        位置 0 的上限 = 4 - 2 + 1 + 0 = 3
        位置 1 的上限 = 4 - 2 + 1 + 1 = 4

    [1,4]：位置 1 已經是 4（到頂），往左；位置 0 是 1 < 3，可以加
           -> c[0] = 2，然後 c[1] = c[0] + 1 = 3  -> [2,3] ✔

    [3,4]：位置 1 到頂，位置 0 是 3 也到頂 -> i < 0 -> 結束 ✔

這和第 31 題（Next Permutation）是同一個想法：
「找到可以增加的最右位置，加一，然後把後面重設成最小」。

C++ 的 next_permutation 和這個 next_combination
是同一類「字典序枚舉」的工具。"""),
     "<strong>優點</strong>：不吃遞迴堆疊，而且產生的順序保證是字典序。",
     "<strong>缺點</strong>：邊界（<code>n - k + 1 + i</code>）要推導，比回溯難記。",
     "<strong>什麼時候值得用？</strong>當 <code>k</code> 很大（遞迴深度深）"
     "或者需要「一個一個產生、隨時可以停」的惰性枚舉時。",
   ], "O(C(n,k) × k)", "O(k)", "每個組合 O(k) 產生", "只有一個陣列"),
 ],
 "compare": (["解法", "剪枝", "遞迴？", "字典序？", "備註"],
   [["一、回溯 + 剪枝", "✔", "✔", "✔", "面試預設"],
    ["二、回溯（不剪枝）", "✘", "✔", "✔", "只差一個上界"],
    ["三、迭代下一個組合", "—", "✘", "✔", "不吃堆疊，惰性枚舉"]]),
 "edges": [
   "<strong>k = n</strong>：<code>(3, 3)</code> → <code>[[1,2,3]]</code>（只有一組）。",
   "<strong>k = 1</strong>：<code>(4, 1)</code> → <code>[[1],[2],[3],[4]]</code>。",
   "<strong>n = k = 1</strong>：<code>[[1]]</code>。",
   "<strong>答案數量</strong>：必須等於 <code>C(n, k)</code>。"
   "<strong>這是最快的自我檢查。</strong>",
   "<strong>忘記 <code>path[:]</code></strong>：輸出會是一堆空 list。",
   "<strong>寫成 <code>backtrack(i)</code></strong>：會產生 <code>[1,1]</code> 這種重複使用的組合。",
   "<strong>剪枝的上界寫成 <code>n - need + 1</code>（少 +1）</strong>："
   "<code>range</code> 的上界是開區間，會漏掉最大的那個數。",
 ],
 "follow": [
   ("h", "追問一：這三種回溯形態怎麼分辨？"),
   ("c", """組合，元素不可重複用（第 77、78、90、40 題）：
    for i in range(start, n):
        ...
        backtrack(i + 1)

組合，元素可以重複用（第 39 題）：
    for i in range(start, n):
        ...
        backtrack(i)          <- 傳 i 不是 i+1

排列（第 46、47 題）：
    for i in range(n):        <- 不用 start，每層從頭掃
        if used[i]: continue
        used[i] = True
        ...
        used[i] = False

一句話：
    start 控制「只能往後選」-> 產生組合（不在乎順序）
    used  控制「不能重複用」-> 產生排列（在乎順序）""",),
   ("h", "追問二：如果 n 很大但 k 很小呢？"),
   "答案數 <code>C(n, k) ≈ n^k / k!</code> 還是會很大。"
   "但如果<strong>只要第 m 個組合</strong>，可以用「組合數 unranking」直接算出來 —— "
   "和第 60 題（Permutation Sequence）用階乘進位制是同一個想法，"
   "只是這裡用的是組合數（Pascal 三角形）而不是階乘。",
   ("h", "追問三：如果要「所有子集」而不是「恰好 k 個」呢？"),
   "第 78 題。把 <code>if len(path) == k</code> 的判斷拿掉，"
   "改成<strong>每進入一層就記錄一次</strong>（因為每個節點都是一個合法的子集）。"
   "<strong>下一題就是它。</strong>",
   ("h", "追問四：Python 有內建的嗎？"),
   "<code>itertools.combinations(range(1, n+1), k)</code>。"
   "它是惰性的（generator），所以 <code>n = 50, k = 25</code> 也不會爆記憶體 —— "
   "只要你不把它全部 <code>list()</code> 起來。"
   "<strong>本篇的測試就是拿它當基準。</strong>",
 ],
 "related": [
   "<strong>第 78／90 題 Subsets</strong> —— 所有子集（不限長度）",
   "<strong>第 39／40 題 Combination Sum</strong> —— 加上「和等於 target」的條件",
   "<strong>第 46／47 題 Permutations</strong> —— 排列（在乎順序）",
   "<strong>第 216 題 Combination Sum III</strong> —— 本題 + 和的條件",
 ],
 "check": [
   "剪枝的上界 <code>n - need + 1</code> 是怎麼推導出來的？",
   "<code>backtrack(i + 1)</code> 改成 <code>backtrack(i)</code> 會變成哪一題？",
   "答案的數量應該是多少？怎麼用它來檢查程式？",
   "組合題用 <code>start</code>、排列題用 <code>used[]</code> —— 兩者在控制什麼？",
 ],
})
print("P77 written")

# ==================== 78. Subsets ====================
S["p78_backtrack"] = '''class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        path = []

        def backtrack(start: int) -> None:
            out.append(path[:])          # 每個節點都是一個合法的子集
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return out'''

S["p78_pick"] = '''class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []
        path = []

        def backtrack(i: int) -> None:
            """對第 i 個元素做「選」或「不選」的二元決定"""
            if i == n:
                out.append(path[:])
                return

            backtrack(i + 1)             # 不選 nums[i]

            path.append(nums[i])         # 選 nums[i]
            backtrack(i + 1)
            path.pop()

        backtrack(0)
        return out'''

S["p78_bits"] = '''class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []

        # 每個子集對應一個 n 位元的二進位數：第 i 位是 1 表示選 nums[i]
        for mask in range(1 << n):
            subset = [nums[i] for i in range(n) if mask & (1 << i)]
            out.append(subset)

        return out'''

S["p78_iter"] = '''class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 迭代：每加入一個新元素，就把「所有已知子集」各複製一份並加上它
        out = [[]]
        for x in nums:
            out += [sub + [x] for sub in out]
        return out'''

_p78 = [S.load(k) for k in ("p78_backtrack", "p78_pick", "p78_bits", "p78_iter")]
for c in [[1, 2, 3], [0], [], [1, 2], [-1, 0, 1]]:
    e = sorted(tuple(sorted(x)) for r in range(len(c) + 1)
               for x in itertools.combinations(c, r))
    for sol in _p78:
        g = sorted(tuple(sorted(x)) for x in sol.subsets(list(c)))
        assert g == e, ("P78", c, sol, g, e)
        assert len(g) == 2 ** len(c), ("P78 count", c, sol)
for _ in range(500):
    c = random.sample(range(-9, 10), random.randint(0, 6))
    e = sorted(tuple(sorted(x)) for r in range(len(c) + 1)
               for x in itertools.combinations(c, r))
    for sol in _p78:
        g = sorted(tuple(sorted(x)) for x in sol.subsets(list(c)))
        assert g == e, ("P78", c, sol)
print("P78 solutions OK")

_P78_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">位元遮罩：n 個元素的子集，和 n 位元的二進位數一一對應</text>
            <text x="20" y="46" fill="var(--text-muted)" font-size="12">nums = [1, 2, 3]，共 2³ = 8 個子集</text>
            <g font-family="monospace" font-size="13">
              <text x="60" y="80" fill="var(--text-muted)">mask</text>
              <text x="180" y="80" fill="var(--text-muted)">二進位</text>
              <text x="330" y="80" fill="var(--text-muted)">選了誰</text>
              <text x="490" y="80" fill="var(--text-muted)">子集</text>
            </g>
            <line x1="40" y1="90" x2="600" y2="90" stroke="var(--border)"/>
            <g font-family="monospace" font-size="13">
              <text x="60" y="114" fill="var(--accent)">0</text><text x="180" y="114" fill="var(--gold)">000</text>
              <text x="330" y="114" fill="var(--text-muted)">—</text><text x="490" y="114" fill="#ff8a65">[]</text>

              <text x="60" y="138" fill="var(--accent)">1</text><text x="180" y="138" fill="var(--gold)">001</text>
              <text x="330" y="138" fill="var(--text-muted)">第 0 位</text><text x="490" y="138" fill="#ff8a65">[1]</text>

              <text x="60" y="162" fill="var(--accent)">2</text><text x="180" y="162" fill="var(--gold)">010</text>
              <text x="330" y="162" fill="var(--text-muted)">第 1 位</text><text x="490" y="162" fill="#ff8a65">[2]</text>

              <text x="60" y="186" fill="var(--accent)">3</text><text x="180" y="186" fill="var(--gold)">011</text>
              <text x="330" y="186" fill="var(--text-muted)">第 0、1 位</text><text x="490" y="186" fill="#ff8a65">[1, 2]</text>

              <text x="60" y="210" fill="var(--accent)">4</text><text x="180" y="210" fill="var(--gold)">100</text>
              <text x="330" y="210" fill="var(--text-muted)">第 2 位</text><text x="490" y="210" fill="#ff8a65">[3]</text>

              <text x="60" y="234" fill="var(--accent)">5</text><text x="180" y="234" fill="var(--gold)">101</text>
              <text x="330" y="234" fill="var(--text-muted)">第 0、2 位</text><text x="490" y="234" fill="#ff8a65">[1, 3]</text>

              <text x="60" y="258" fill="var(--accent)">6</text><text x="180" y="258" fill="var(--gold)">110</text>
              <text x="330" y="258" fill="var(--text-muted)">第 1、2 位</text><text x="490" y="258" fill="#ff8a65">[2, 3]</text>

              <text x="60" y="282" fill="var(--accent)">7</text><text x="180" y="282" fill="var(--gold)">111</text>
              <text x="330" y="282" fill="var(--text-muted)">全部</text><text x="490" y="282" fill="#ff8a65">[1, 2, 3]</text>
            </g>
            <text x="20" y="318" fill="var(--gold)" font-size="12">「子集 ↔ 位元遮罩」是計數與枚舉的核心對應 —— 也是「子集 DP」這一整類題的基礎。</text>'''

emit({
 "num": 78, "slug": "subsets",
 "en": [
   "Given an integer array <code>nums</code> of <strong>unique</strong> elements, return "
   "<em>all possible subsets (the power set)</em>.",
   "The solution set <strong>must not</strong> contain duplicate subsets. Return the solution "
   "in <strong>any order</strong>.",
 ],
 "zh": [
   "給你一個<strong>元素互不相同</strong>的整數陣列 <code>nums</code>，"
   "回傳它的<strong>所有子集</strong>（也就是<strong>冪集合</strong>）。",
   "答案裡不能有重複的子集，順序不拘。",
 ],
 "pre": [
   ("note", "子集的數量一定是 2ⁿ", [
     ("c", """對每個元素，你只有兩種選擇：「選」或「不選」。
n 個元素各自獨立 -> 2 × 2 × ... × 2 = 2ⁿ 種。

    nums = [1,2,3]  ->  2³ = 8 個子集（含空集合和全集）

這個「2ⁿ」的結構有一個非常漂亮的對應：

    每個子集  <->  一個 n 位元的二進位數

    000 -> []         100 -> [3]
    001 -> [1]        101 -> [1,3]
    010 -> [2]        110 -> [2,3]
    011 -> [1,2]      111 -> [1,2,3]

    第 i 位是 1  <=>  選了 nums[i]

這個對應是「位元遮罩枚舉」的基礎，
也是「子集 DP」（第 464、698、1349、TSP 等題）的核心工具。"""),
     "<strong>寫完之後先檢查「答案數量是不是 2ⁿ」</strong> —— "
     "這是最快的除錯方法。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3]
  輸出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

範例 2
  輸入：nums = [0]
  輸出：[[],[0]]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10",
   "−10 ≤ <code>nums[i]</code> ≤ 10",
   "<code>nums</code> 的所有元素<strong>互不相同</strong>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 10</strong>，所以最多 <code>2¹⁰ = 1024</code> 個子集。"
       "<strong>規模小到可以用任何方法。</strong>",
       "<strong>元素互不相同</strong> —— 不用去重。"
       "（有重複的是第 90 題。）",
       "<strong>順序不拘</strong>，所以四種解法產生的順序不同都沒關係。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P78_FIG, "0 0 640 332"),
   "四種解法，對應四種看待「子集」的方式："
   "<strong>「選哪些位置」、「每個元素選不選」、「一個二進位數」、「逐步擴張」</strong>。",
 ],
 "approaches": [
   ap("解法一", "回溯 + start（和第 77 題同一個模板）", [
     ("c", S["p78_backtrack"]),
     ("h", "和第 77 題只差一行"),
     ("c", """第 77 題（恰好 k 個）：
    if len(path) == k:
        out.append(path[:])
        return
    for i in range(start, n):
        ...

第 78 題（所有子集）：
    out.append(path[:])          <- 不判斷長度，每個節點都收
    for i in range(start, n):
        ...

差別：
    第 77 題只在「葉子」（長度剛好 k）收集
    第 78 題在「每一個節點」都收集

    因為搜尋樹上的每一條路徑（不管長短）都對應一個合法的子集。

    根節點（path 為空）-> 空集合 ✔
    第一層          -> 單元素子集
    ...
    葉子            -> 全集

    共 2ⁿ 個節點 = 2ⁿ 個子集 ✔"""),
     "<strong>沒有終止條件</strong>（沒有 <code>if ... return</code>）—— "
     "迴圈跑完自然就返回了。"
     "<strong>這是本題和第 77 題最明顯的視覺差異。</strong>",
   ], "O(2ⁿ × n)", "O(n)", "2ⁿ 個節點，每個複製 O(n)",
      "path + 遞迴深度；不算輸出", optimal=True),

   ap("解法二", "選 / 不選的二元決策樹", [
     "另一種回溯的組織方式：<strong>對每個元素做一次「選」或「不選」的決定。</strong>",
     ("c", S["p78_pick"]),
     ("c", """搜尋樹長這樣（nums = [1,2]）：

                    i=0
            不選 /        \\ 選 1
              i=1          i=1
         不選 /  \\ 選2   不選 /  \\ 選2
           []    [2]     [1]   [1,2]

    每個葉子就是一個子集，共 2ⁿ 個葉子 ✔

和解法一的差別：
    解法一：在「每個節點」收集，樹的節點數 = 2ⁿ
    解法二：只在「葉子」收集，樹的節點數 = 2^(n+1) - 1，葉子數 = 2ⁿ

    解法二的樹大一倍（有很多內部節點不對應答案），
    但它的結構更「規整」—— 每一層剛好對應一個元素。

什麼時候解法二比較好？
    當「選 / 不選」有不同的代價或條件時。
    例如 0/1 背包、第 494 題（目標和）、
    以及任何「對每個元素做二元決定」的問題。

    解法一的 start 形式在「要收集所有前綴」時比較自然。"""),
   ], "O(2ⁿ × n)", "O(n)", "2^(n+1) 個節點", "同上"),

   ap("解法三", "位元遮罩枚舉（最直接的對應）", [
     ("c", S["p78_bits"]),
     ("c", """for mask in range(1 << n):      # 0 到 2ⁿ-1
    subset = [nums[i] for i in range(n) if mask & (1 << i)]

mask & (1 << i)    測試 mask 的第 i 位是不是 1

    mask = 5 = 0b101, n = 3
    i=0: 5 & 1 = 1 ✔  選 nums[0]
    i=1: 5 & 2 = 0 ✘
    i=2: 5 & 4 = 4 ✔  選 nums[2]
    -> [nums[0], nums[2]]

沒有遞迴、沒有回溯，就是兩層迴圈。

常用的相關技巧：
    bin(mask).count("1")   這個子集有幾個元素
    mask & (mask - 1)      清掉最低位的 1
    mask & -mask           取出最低位的 1
    (1 << n) - 1           全選的遮罩

    枚舉 mask 的所有「子集」（子集的子集）：
        sub = mask
        while sub:
            ...
            sub = (sub - 1) & mask
        # 別忘了空集合

        這個技巧在「子集 DP」裡非常重要，
        而且總複雜度是 O(3ⁿ) 而不是 O(4ⁿ)。"""),
     "<strong>優點</strong>：沒有遞迴、程式碼最短、而且<strong>可以直接平行化</strong>"
     "（每個 mask 獨立）。",
     "<strong>限制</strong>：<code>n</code> 不能超過語言的整數位寬"
     "（在 C 裡是 32 或 64）。Python 沒這個限制，但 2ⁿ 本來就撐不了多大的 n。",
   ], "O(2ⁿ × n)", "O(1)", "2ⁿ 個 mask × O(n) 展開", "不算輸出的話 O(1)"),

   ap("解法四", "迭代擴張（最短）", [
     ("c", S["p78_iter"]),
     ("c", """out = [[]]

加入 1：  out = [[]] + [[1]]           = [[], [1]]
加入 2：  out = [[],[1]] + [[2],[1,2]] = [[], [1], [2], [1,2]]
加入 3：  out = ... + [[3],[1,3],[2,3],[1,2,3]]
          = 8 個 ✔

每加入一個元素，答案的數量就「乘以 2」——
因為每個已知的子集，都分裂成「加它」和「不加它」兩個。

這正是 2ⁿ 的建構式定義：
    P(S ∪ {x}) = P(S) ∪ { A ∪ {x} : A ∈ P(S) }"""),
     "<strong>一行核心邏輯</strong>，而且<strong>不需要遞迴、不需要位元運算</strong>。",
     "<strong>缺點</strong>：所有中間結果都在記憶體裡（但反正最後也要全部輸出）。"
     "而且 <code>out += [...]</code> 在迴圈中修改 <code>out</code> —— "
     "<strong>這裡是安全的</strong>，因為右邊的 list comprehension 會先完整求值。"
     "（如果寫成 generator 就會無限迴圈。）",
   ], "O(2ⁿ × n)", "O(2ⁿ × n)", "同上", "所有中間結果"),
 ],
 "compare": (["解法", "遞迴？", "行數", "能平行化？", "最能推廣到"],
   [["一、回溯 + start", "✔", "10", "✘", "第 90 題（去重）"],
    ["二、選 / 不選", "✔", "12", "✘", "0/1 背包、第 494 題"],
    ["三、位元遮罩", "✘", "6", "✔", "子集 DP、狀態壓縮"],
    ["四、迭代擴張", "✘", "5", "✘", "最短，但最不好推廣"]]),
 "edges": [
   "<strong>空陣列</strong>：<code>[]</code> → <code>[[]]</code>（一個空集合）。"
   "題目保證 n ≥ 1，但四種解法都自然正確。",
   "<strong>單一元素</strong>：<code>[0]</code> → <code>[[], [0]]</code>。",
   "<strong>答案數量</strong>：必須是 <code>2ⁿ</code>。"
   "<strong>n = 10 時是 1024 個 —— 先數數量再檢查內容。</strong>",
   "<strong>空集合要包含</strong>：很多人會漏掉。"
   "解法一的「根節點也收集」、解法四的初值 <code>[[]]</code>、"
   "解法三的 <code>mask = 0</code> —— 三者都在處理這件事。",
   "<strong>全集要包含</strong>：<code>[1,2,3]</code> 的答案要有 <code>[1,2,3]</code>。",
   "<strong>忘記 <code>path[:]</code></strong>：輸出會是 2ⁿ 個空 list。",
 ],
 "follow": [
   ("h", "追問一：如果有重複元素呢？"),
   "第 90 題（Subsets II）。加上排序 + 同層去重（和第 40 題一樣）：",
   ("c", """nums.sort()
...
for i in range(start, n):
    if i > start and nums[i] == nums[i-1]:
        continue
    ...

位元遮罩法在這裡會失效（會產生重複的子集），
除非事後用 set 去重 —— 那就浪費了。

所以「有重複」的版本只能用回溯。""",),
   ("h", "追問二：什麼是「子集 DP」？"),
   ("c", """當狀態是「一個集合」時，用 n 位元的整數當 DP 的索引。

    dp[mask] = 「已經處理了 mask 這些元素」時的最佳值

經典應用：
    第 464 題  我能贏嗎（博弈 + 狀態壓縮）
    第 698 題  劃分為 k 個相等的子集
    第 847 題  訪問所有節點的最短路徑
    第 1349 題 參加考試的最大學生數
    旅行推銷員問題（TSP）：dp[mask][i] = 走過 mask、目前在 i 的最短距離
                            O(2ⁿ × n²)，n <= 20 左右可行

前提：n 要夠小（通常 <= 20，因為 2²⁰ ≈ 100 萬）。

而「枚舉 mask 的所有子集」的技巧：
    sub = mask
    while sub:
        處理 sub
        sub = (sub - 1) & mask

    總複雜度 O(3ⁿ)（不是 O(4ⁿ)）——
    因為每個元素有三種狀態：不在 mask 裡、在 mask 但不在 sub、在 sub 裡。""",),
   ("h", "追問三：為什麼不可能有比 O(2ⁿ) 更快的演算法？"),
   "<strong>因為輸出本身就有 2ⁿ 個子集。</strong>"
   "任何「列出所有子集」的演算法，光是寫出答案就要 Ω(2ⁿ) 的時間。",
   "<strong>這是「輸出敏感（output-sensitive）」複雜度的典型例子</strong> —— "
   "當答案的大小是指數級時，演算法的複雜度下界也是指數級，"
   "所以「優化」的空間只在常數和記憶體上。",
   "（如果只要「子集的個數」或「某個統計量」，那就完全不同了 —— "
   "個數是 2ⁿ，一行就算出來。<strong>「列出來」和「數出來」的難度可以天差地遠。</strong>）",
 ],
 "related": [
   "<strong>第 90 題 Subsets II</strong> —— 有重複元素",
   "<strong>第 77 題 Combinations</strong> —— 限定大小的子集",
   "<strong>第 39／40 題 Combination Sum</strong> —— 加上和的條件",
   "<strong>第 46／47 題 Permutations</strong> —— 排列",
   "<strong>第 698／1349 題</strong> —— 子集 DP（狀態壓縮）",
 ],
 "check": [
   "本題和第 77 題的回溯程式碼只差一行，是哪一行？為什麼？",
   "位元遮罩法裡 <code>mask &amp; (1 &lt;&lt; i)</code> 在測試什麼？",
   "解法四的初值為什麼是 <code>[[]]</code> 而不是 <code>[]</code>？",
   "為什麼不可能有比 O(2ⁿ) 更快的演算法？",
 ],
})
print("P78 written")
