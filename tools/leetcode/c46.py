# -*- coding: utf-8 -*-
"""第 46–48 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(46)

# ==================== 46. Permutations ====================
S["p46_used"] = '''class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []
        path = []
        used = [False] * n

        def backtrack() -> None:
            if len(path) == n:
                out.append(path[:])
                return
            for i in range(n):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return out'''

S["p46_swap"] = '''class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []

        def backtrack(k: int) -> None:
            """nums[:k] 已經固定好了，決定第 k 個位置放誰"""
            if k == n:
                out.append(nums[:])
                return
            for i in range(k, n):
                nums[k], nums[i] = nums[i], nums[k]   # 把 nums[i] 換到第 k 位
                backtrack(k + 1)
                nums[k], nums[i] = nums[i], nums[k]   # 換回來

        backtrack(0)
        return out'''

S["p46_insert"] = '''class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 迭代法：一個一個把元素插進「所有已知排列」的每一個位置
        out = [[]]
        for x in nums:
            out = [p[:i] + [x] + p[i:] for p in out for i in range(len(p) + 1)]
        return out'''

_p46 = [S.load(k) for k in ("p46_used", "p46_swap", "p46_insert")]
for c in [[1, 2, 3], [0, 1], [1], []]:
    e = sorted(map(tuple, itertools.permutations(c)))
    for sol in _p46:
        g = sorted(map(tuple, sol.permute(list(c))))
        assert g == e, ("P46", c, sol, g, e)
for _ in range(300):
    c = random.sample(range(-5, 6), random.randint(0, 5))
    e = sorted(map(tuple, itertools.permutations(c)))
    for sol in _p46:
        g = sorted(map(tuple, sol.permute(list(c))))
        assert g == e, ("P46", c, sol)
print("P46 solutions OK")

_P46_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">nums = [1,2,3] 的搜尋樹：每一層選一個「還沒用過」的數字</text>
            <g font-size="12" text-anchor="middle" font-family="monospace">
              <text x="320" y="44" fill="var(--gold)">[]</text>
              <text x="140" y="92" fill="var(--accent)">[1]</text>
              <text x="320" y="92" fill="var(--accent)">[2]</text>
              <text x="500" y="92" fill="var(--accent)">[3]</text>
              <text x="90" y="140" fill="var(--accent)">[1,2]</text>
              <text x="200" y="140" fill="var(--accent)">[1,3]</text>
              <text x="268" y="140" fill="var(--accent)">[2,1]</text>
              <text x="378" y="140" fill="var(--accent)">[2,3]</text>
              <text x="446" y="140" fill="var(--accent)">[3,1]</text>
              <text x="556" y="140" fill="var(--accent)">[3,2]</text>
              <text x="90" y="188" fill="#ff8a65">[1,2,3]</text>
              <text x="200" y="188" fill="#ff8a65">[1,3,2]</text>
              <text x="268" y="188" fill="#ff8a65">[2,1,3]</text>
              <text x="378" y="188" fill="#ff8a65">[2,3,1]</text>
              <text x="446" y="188" fill="#ff8a65">[3,1,2]</text>
              <text x="556" y="188" fill="#ff8a65">[3,2,1]</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.3">
              <line x1="306" y1="52" x2="152" y2="80"/>
              <line x1="320" y1="52" x2="320" y2="80"/>
              <line x1="334" y1="52" x2="488" y2="80"/>
              <line x1="130" y1="100" x2="96" y2="128"/>
              <line x1="150" y1="100" x2="194" y2="128"/>
              <line x1="308" y1="100" x2="274" y2="128"/>
              <line x1="332" y1="100" x2="372" y2="128"/>
              <line x1="490" y1="100" x2="452" y2="128"/>
              <line x1="510" y1="100" x2="550" y2="128"/>
              <line x1="90" y1="148" x2="90" y2="176"/>
              <line x1="200" y1="148" x2="200" y2="176"/>
              <line x1="268" y1="148" x2="268" y2="176"/>
              <line x1="378" y1="148" x2="378" y2="176"/>
              <line x1="446" y1="148" x2="446" y2="176"/>
              <line x1="556" y1="148" x2="556" y2="176"/>
            </g>
            <text x="20" y="226" fill="var(--gold)" font-size="12">每一層的分支數：3 → 2 → 1，總共 3! = 6 條路徑</text>
            <text x="20" y="250" fill="var(--text-muted)" font-size="12">和組合題（第 39、40、78 題）最大的差別：<tspan fill="var(--accent)">沒有 start 參數</tspan>，每一層都從頭掃</text>
            <text x="20" y="272" fill="var(--text-muted)" font-size="12">因為排列在乎順序，[1,2] 和 [2,1] 是不同的答案，不能用 start 限制</text>'''

emit({
 "num": 46, "slug": "permutations",
 "en": [
   "Given an array <code>nums</code> of <strong>distinct</strong> integers, return "
   "<em>all the possible permutations</em>. You can return the answer in any order.",
 ],
 "zh": [
   "給你一個<strong>元素互不相同</strong>的整數陣列 <code>nums</code>，"
   "回傳它的<strong>所有排列</strong>。答案順序不拘。",
 ],
 "pre": [
   ("note", "排列 vs 組合：差在「有沒有 start」", [
     ("c", """組合（第 39、40、77、78、90 題）：
    順序不重要，[1,2] 和 [2,1] 是同一個
    -> 用 start 參數限制「只能往後選」
    -> for i in range(start, n)

排列（第 46、47 題）：
    順序很重要，[1,2] 和 [2,1] 是不同的
    -> 不能用 start，每一層都要從頭掃
    -> for i in range(n)，但要用 used[] 記錄「這個已經用過了」

一句話：
    組合用 start 防止「重複的集合」
    排列用 used  防止「重複使用同一個元素」

    兩者都是在控制「哪些還能選」，只是規則不同。"""),
     "<strong>n 個相異元素的排列有 n! 個。</strong>"
     "n = 6 時 720 個，n = 10 時 3,628,800 個 —— "
     "所以這類題目的 n 一定很小（本題 n ≤ 6）。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3]
  輸出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

範例 2
  輸入：nums = [0,1]
  輸出：[[0,1],[1,0]]

範例 3
  輸入：nums = [1]
  輸出：[[1]]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 6",
   "−10 ≤ <code>nums[i]</code> ≤ 10",
   "<code>nums</code> 的所有元素<strong>互不相同</strong>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 6</strong>，所以答案最多 720 個。"
       "這個數字就是在說：<strong>直接枚舉，不用擔心效率。</strong>",
       "<strong>元素互不相同</strong> —— 不用去重。"
       "（有重複的是第 47 題，去重會麻煩很多。）",
       "<strong>答案順序不拘</strong>，所以三種解法產生的順序不同都沒關係。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P46_FIG, "0 0 640 284"),
 ],
 "approaches": [
   ap("解法一", "回溯 + used 陣列（最標準）", [
     ("c", S["p46_used"]),
     ("h", "三個狀態要同步"),
     ("c", """used[i] = True       標記「這個元素被用了」
path.append(...)     記錄選了什麼
backtrack()          往下一層
path.pop()           撤銷選擇
used[i] = False      撤銷標記

「做」和「撤銷」必須完全對稱 ——
少撤銷一個，後面的搜尋就會基於錯的狀態。

建議的寫法習慣：
    做的兩行寫在一起，撤銷的兩行也寫在一起，
    而且撤銷的順序和做的順序相反（像堆疊）。
    這樣視覺上就能檢查有沒有漏。"""),
     "<strong>終止條件是 <code>len(path) == n</code></strong>，"
     "不是 <code>all(used)</code> —— 前者是 O(1)，後者是 O(n)。",
     "<strong>為什麼 <code>path[:]</code> 不能省？</strong>"
     "同第 39 題：<code>path</code> 是共用的 list，之後還會被改。"
     "<strong>這是回溯題第一名的 bug。</strong>",
   ], "O(n! · n)", "O(n)", "n! 條路徑，每條複製 O(n)",
      "used + path + 遞迴深度；不算輸出", optimal=True),

   ap("解法二", "原地交換（不需要 used 陣列）", [
     "另一種思路：<strong>不用額外標記，直接在原陣列上交換。</strong>"
     "把「決定第 k 個位置放誰」想成「從 <code>nums[k:]</code> 裡挑一個換到第 k 位」。",
     ("c", S["p46_swap"]),
     ("c", """nums = [1,2,3]，backtrack(0)

  i=0: 交換 (0,0) -> [1,2,3]，往下
       i=1: 交換 (1,1) -> [1,2,3]，往下
            i=2: 交換 (2,2) -> 收 [1,2,3]
            換回
       i=2: 交換 (1,2) -> [1,3,2]，往下
            收 [1,3,2]
            換回 -> [1,2,3]
  i=1: 交換 (0,1) -> [2,1,3]，往下 ...
  i=2: 交換 (0,2) -> [3,2,1]，往下 ...

不變量：進入 backtrack(k) 時，nums[:k] 是已經決定好的前綴，
        nums[k:] 是「還沒用到的元素」（順序可能被打亂，但集合不變）。"""),
     "<strong>優點</strong>：不需要 <code>used</code> 陣列，也不需要 <code>path</code> —— "
     "<code>nums</code> 本身就是路徑。空間更省。",
     "<strong>缺點</strong>：",
     ("ul", [
       "<strong>產生的順序不是字典序</strong>（解法一是）。題目不要求，但有些題目會要求。",
       "<strong>推廣到第 47 題（有重複值）時會出問題</strong> —— "
       "因為交換會打亂順序，「相同的值相鄰」這個去重前提就不成立了。"
       "要改用 set 記錄「這一層試過哪些值」。",
     ]),
     "<strong>所以：解法一更通用，解法二更省空間。面試建議寫解法一。</strong>",
   ], "O(n! · n)", "O(n)", "同上", "只有遞迴深度和 nums 本身"),

   ap("解法三", "迭代插入（不用遞迴）", [
     "完全不同的角度：<strong>已經有了 k 個元素的所有排列，"
     "要加入第 k+1 個元素時，把它插進每個排列的每一個位置。</strong>",
     ("c", S["p46_insert"]),
     ("c", """nums = [1,2,3]

初始：      [[]]

加入 1：    把 1 插進 [] 的 1 個位置
            -> [[1]]

加入 2：    把 2 插進 [1] 的 2 個位置（前、後）
            -> [[2,1], [1,2]]

加入 3：    把 3 插進 [2,1] 的 3 個位置 -> [3,2,1], [2,3,1], [2,1,3]
            把 3 插進 [1,2] 的 3 個位置 -> [3,1,2], [1,3,2], [1,2,3]
            -> 共 6 個 ✔

數量驗證：1 × 2 × 3 = 6 = 3! ✔
每一輪的數量乘上「目前長度 + 1」，剛好就是階乘的定義。"""),
     "<strong>一行 list comprehension 寫完</strong>，而且完全不用遞迴。",
     "<strong>缺點</strong>：所有中間結果都要留在記憶體裡（O(n!·n) 空間），"
     "而回溯只需要 O(n)。在 n 大的時候差別很大 —— 但這題 n ≤ 6，無所謂。",
     "<strong>這個「插入法」在數學上很漂亮</strong>：它直接對應了 "
     "<code>n! = 1 × 2 × ... × n</code> 的遞迴定義。",
   ], "O(n! · n)", "O(n! · n)", "同上", "所有中間結果"),
 ],
 "compare": (["解法", "時間", "額外空間", "字典序？", "能推廣到第 47 題？"],
   [["一、used 陣列", "O(n!·n)", "O(n)", "✔（若輸入有序）", "✔ 最容易"],
    ["二、原地交換", "O(n!·n)", "O(n)", "✘", "要改成用 set 去重"],
    ["三、迭代插入", "O(n!·n)", "O(n!·n)", "✘", "很難"]]),
 "edges": [
   "<strong>單一元素</strong>：<code>[1]</code> → <code>[[1]]</code>。",
   "<strong>兩個元素</strong>：<code>[0,1]</code> → <code>[[0,1],[1,0]]</code>。",
   "<strong>空陣列</strong>：<code>[]</code> → <code>[[]]</code>（一個空排列）。"
   "題目保證 n ≥ 1，但三種解法都自然正確。",
   "<strong>n = 6</strong>：720 個答案。確認數量對得上 <code>6! = 720</code>。",
   "<strong>忘記 <code>path[:]</code></strong>：輸出會是 n! 個空 list。",
   "<strong>忘記 <code>used[i] = False</code></strong>：只會產生一個排列（之後全部被擋）。",
   "<strong>負數</strong>：<code>[-1, 0, 1]</code>。值域有負數，不要用某個數字當「沒用過」的標記。",
 ],
 "follow": [
   ("h", "追問一：如果有重複元素呢？"),
   "第 47 題。加上排序 + 同層去重：",
   ("c", """nums.sort()
...
for i in range(n):
    if used[i]:
        continue
    if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
        continue          # 同一層裡，相同的值只用第一個
    ...

那個 not used[i-1] 是關鍵：
    used[i-1] == True   表示「前一個相同的值」在「上一層」被用了
                        -> 這是合法的（用兩個相同的值）
    used[i-1] == False  表示「前一個相同的值」在這一層被跳過了
                        -> 那我也該跳過，否則會產生一模一樣的子樹

和第 40 題的 i > start 是同一個道理：
「同一層裡，相同的值只選第一次出現的那個」。""",),
   ("h", "追問二：如果只要第 k 個排列（字典序）呢？"),
   "第 60 題。不需要生成全部 —— 用<strong>階乘進位制</strong>直接算："
   "第一位有 <code>(n-1)!</code> 種後續，所以 <code>第一位的候選索引 = k // (n-1)!</code>，"
   "然後 <code>k %= (n-1)!</code>，遞迴下去。O(n²)。",
   ("h", "追問三：如果要「下一個排列」呢？"),
   "第 31 題。O(n) 的 Narayana Pandita 演算法："
   "找下降點 → 交換 → 反轉尾段。"
   "<strong>如果要依序列出所有排列，反覆呼叫「下一個排列」比回溯更省記憶體</strong>"
   "（O(1) vs O(n)），而且天然是字典序。",
   ("h", "追問四：Python 的 <code>itertools.permutations</code> 用什麼演算法？"),
   "CPython 的實作是<strong>迭代版的「索引 + 迴圈計數器」</strong>，"
   "本質上和解法二（交換法）類似，但寫成了不用遞迴的形式。"
   "<strong>而且它是惰性的（generator）</strong> —— "
   "所以 <code>itertools.permutations(range(20))</code> 不會爆記憶體，"
   "只有真的去迭代它才會一個一個產生。"
   "<strong>在「只需要前幾個」或「邊產生邊過濾」的場景，惰性求值是關鍵。</strong>",
 ],
 "related": [
   "<strong>第 47 題 Permutations II</strong> —— 有重複元素",
   "<strong>第 31 題 Next Permutation</strong> —— 一次產生下一個",
   "<strong>第 60 題 Permutation Sequence</strong> —— 直接算第 k 個",
   "<strong>第 78／90 題 Subsets</strong> —— 組合版的回溯",
   "<strong>第 17／39／40／77 題</strong> —— 回溯家族",
 ],
 "check": [
   "排列和組合的回溯，在程式碼上最大的差別是什麼？為什麼排列不能用 <code>start</code>？",
   "解法二（交換法）為什麼不需要 <code>used</code> 陣列？它的不變量是什麼？",
   "解法三的中間結果數量是 1, 2, 6, 24, ...，這對應什麼公式？",
   "第 47 題的去重條件 <code>not used[i-1]</code> 在表達什麼？",
 ],
})
print("P46 written")

# ==================== 47. Permutations II ====================
S["p47"] = '''class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()             # 讓相同的值相鄰，去重才做得到
        n = len(nums)
        out = []
        path = []
        used = [False] * n

        def backtrack() -> None:
            if len(path) == n:
                out.append(path[:])
                return

            for i in range(n):
                if used[i]:
                    continue
                # 同一層裡，相同的值只用「第一個還沒被用掉的」
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                path.append(nums[i])
                backtrack()
                path.pop()
                used[i] = False

        backtrack()
        return out'''

S["p47_counter"] = '''from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        counter = Counter(nums)       # 把重複的值合併成 值 -> 剩餘數量
        out = []
        path = []

        def backtrack() -> None:
            if len(path) == n:
                out.append(path[:])
                return
            # 每一層只對「不同的值」各試一次 -> 天然不會重複
            for v in counter:
                if counter[v] == 0:
                    continue
                counter[v] -= 1
                path.append(v)
                backtrack()
                path.pop()
                counter[v] += 1

        backtrack()
        return out'''

_p47 = [S.load(k) for k in ("p47", "p47_counter")]
for c in [[1, 1, 2], [1, 2, 3], [1], [2, 2, 1, 1], [0, 0, 0]]:
    e = sorted(set(itertools.permutations(c)))
    for sol in _p47:
        g = sorted(map(tuple, sol.permuteUnique(list(c))))
        assert g == e, ("P47", c, sol, g, e)
        assert len(g) == len(set(g)), ("P47 dup", c, sol)
for _ in range(600):
    c = [random.randint(1, 3) for _ in range(random.randint(0, 5))]
    e = sorted(set(itertools.permutations(c)))
    for sol in _p47:
        g = sorted(map(tuple, sol.permuteUnique(list(c))))
        assert g == e, ("P47", c, sol, g, e)
print("P47 solutions OK")

_P47_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">nums = [1, 1, 2]（排序後）。用下標區分兩個 1：1ₐ（索引 0）、1ᵦ（索引 1）</text>
            <text x="20" y="50" fill="var(--text-muted)" font-size="12">不去重的話，會產生 3! = 6 條路徑，但只有 3 個「不同的值序列」</text>
            <g font-size="12" font-family="monospace">
              <text x="50" y="84" fill="var(--accent)">[1ₐ, 1ᵦ, 2]</text>
              <text x="200" y="84" fill="var(--accent)">→ [1,1,2] ✔ 保留</text>
              <text x="50" y="108" fill="var(--text-muted)" opacity="0.5">[1ᵦ, 1ₐ, 2]</text>
              <text x="200" y="108" fill="#ff8a65">→ [1,1,2] ✘ 重複</text>
              <text x="50" y="132" fill="var(--accent)">[1ₐ, 2, 1ᵦ]</text>
              <text x="200" y="132" fill="var(--accent)">→ [1,2,1] ✔ 保留</text>
              <text x="50" y="156" fill="var(--text-muted)" opacity="0.5">[1ᵦ, 2, 1ₐ]</text>
              <text x="200" y="156" fill="#ff8a65">→ [1,2,1] ✘ 重複</text>
              <text x="50" y="180" fill="var(--accent)">[2, 1ₐ, 1ᵦ]</text>
              <text x="200" y="180" fill="var(--accent)">→ [2,1,1] ✔ 保留</text>
              <text x="50" y="204" fill="var(--text-muted)" opacity="0.5">[2, 1ᵦ, 1ₐ]</text>
              <text x="200" y="204" fill="#ff8a65">→ [2,1,1] ✘ 重複</text>
            </g>
            <line x1="20" y1="224" x2="620" y2="224" stroke="var(--border)"/>
            <text x="20" y="252" fill="var(--gold)" font-size="12">規則：只允許「1ₐ 排在 1ᵦ 前面」的那些路徑 → 每個值序列恰好對應一條路徑</text>
            <text x="20" y="276" fill="var(--text-muted)" font-size="12">實作：選 nums[i] 時，如果前一個相同的值 nums[i−1] 還沒被用，就跳過</text>
            <text x="20" y="300" fill="var(--text-muted)" font-size="12">（那表示我正想在 1ₐ 之前用 1ᵦ —— 正是要禁止的情況）</text>'''

emit({
 "num": 47, "slug": "permutations-ii",
 "en": [
   "Given a collection of numbers, <code>nums</code>, that might contain "
   "<strong>duplicates</strong>, return <em>all possible unique permutations</em> "
   "<strong>in any order</strong>.",
 ],
 "zh": [
   "給你一個<strong>可能含有重複數字</strong>的陣列 <code>nums</code>，"
   "回傳所有<strong>不重複</strong>的排列。答案順序不拘。",
 ],
 "pre": [
   ("note", "問題出在哪：相同的值製造出相同的答案", [
     ("c", """nums = [1, 1, 2]

如果照第 46 題的做法（不去重），會產生 3! = 6 條路徑。
但因為兩個 1 長得一樣，其中有一半是重複的：

    [1,1,2] ×2    [1,2,1] ×2    [2,1,1] ×2

正確答案只有 3 個。

一般公式：有 n 個元素、其中值 v 出現 c_v 次，
          不同的排列數 = n! / ∏(c_v!)

    [1,1,2]：3! / (2! × 1!) = 6 / 2 = 3 ✔"""),
     "<strong>去重的兩種思路</strong>：",
     ("ul", [
       "<strong>排序 + 同層跳過</strong>（解法一）：強制「相同的值必須按固定順序使用」",
       "<strong>用 Counter 把相同的值合併</strong>（解法二）：每一層只對「不同的值」各試一次",
     ]),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,1,2]
  輸出：[[1,1,2],[1,2,1],[2,1,1]]

範例 2
  輸入：nums = [1,2,3]
  輸出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 8",
   "−10 ≤ <code>nums[i]</code> ≤ 10",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 8</strong>，所以最多 8! = 40320 個排列。"
       "就算不去重、事後用 set 過濾也跑得動 —— "
       "<strong>但那不是題目想考的</strong>。",
       "<strong>可能有重複</strong> —— 這是和第 46 題唯一的差別，"
       "但它讓程式碼多了兩行、難度多了一級。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P47_FIG, "0 0 640 312"),
 ],
 "approaches": [
   ap("解法一", "排序 + 同層去重（標準解）", [
     ("c", S["p47"]),
     ("h", "去重條件的三個部分"),
     ("c", """if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
    continue

① i > 0
   不是第一個元素（第一個沒有「前一個」可以比）

② nums[i] == nums[i-1]
   和前一個是相同的值（排序後相同的值相鄰）

③ not used[i-1]
   前一個相同的值「還沒被用掉」

三個同時成立才跳過。

第 ③ 點是全題的精髓，值得仔細看：

    used[i-1] == True
        表示 nums[i-1] 已經在「更上層」被選了。
        現在選 nums[i] 是合法的 ——
        這就是「用了兩個 1」的正常情況。
        例：路徑是 [1ₐ, ...]，現在要選 1ᵦ  ->  允許 ✔

    used[i-1] == False
        表示 nums[i-1] 在「這一層」被跳過了（或還沒輪到）。
        現在選 nums[i] 會產生和「選 nums[i-1]」一模一樣的子樹。
        例：這一層還沒用任何 1，卻想先用 1ᵦ  ->  禁止 ✘

換句話說，這個條件強制了一個規則：
    「相同的值，必須按照它們在陣列裡的順序被使用。」
    1ₐ 一定比 1ᵦ 先用。

    這樣每個「值的序列」就只對應唯一一條「索引的路徑」-> 不重不漏。"""),
     ("h", "為什麼一定要先排序？"),
     "因為去重條件靠的是 <code>nums[i] == nums[i-1]</code> —— "
     "<strong>只有相同的值相鄰時，這個比較才抓得到所有重複。</strong>"
     "<code>[1, 2, 1]</code> 不排序的話，兩個 1 不相鄰，條件永遠不成立，完全沒去重。",
     ("h", "寫成 <code>used[i-1]</code>（不加 not）會怎樣？"),
     ("c", """if i > 0 and nums[i] == nums[i-1] and used[i-1]:
    continue

這個版本「也能」去重，而且答案也是對的！

    差別只在：它強制「1ᵦ 必須比 1ₐ 先用」（反過來的順序）。
    每個值序列還是只對應一條路徑，所以不重不漏。

但它有一個缺點：
    used[i-1] 為 True 時才跳過 ——
    這表示程式會先「選了 1ₐ」再發現要跳過 1ᵦ，
    走進去又退出來，剪枝發生得比較晚。

    not used[i-1] 的版本會在「還沒選任何 1」時就跳過 1ᵦ，
    剪得比較早，效率略好。

兩種寫法在 LeetCode 上都會過，但推薦 not used[i-1]。"""),
   ], "O(n! · n)", "O(n)", "去重後遠低於 n!；最壞（全不同）是 n!",
      "used + path + 遞迴深度", optimal=True),

   ap("解法二", "用 Counter：每一層只試「不同的值」", [
     "換個角度：<strong>與其在搜尋時跳過重複，不如一開始就不要讓重複的東西出現在選項裡。</strong>",
     ("c", S["p47_counter"]),
     ("c", """nums = [1,1,2]  ->  counter = {1: 2, 2: 1}

第 0 層：對「值」1 和 2 各試一次（不是對三個「位置」）
    選 1 -> counter = {1:1, 2:1}
        第 1 層：試 1 和 2
            選 1 -> {1:0, 2:1}，第 2 層只能選 2 -> [1,1,2] ✔
            選 2 -> {1:1, 2:0}，第 2 層只能選 1 -> [1,2,1] ✔
    選 2 -> counter = {1:2, 2:0}
        第 1 層：只能選 1
            -> [2,1,1] ✔

三條路徑，三個答案，完全沒有重複 ——
因為「同一層對同一個值只試一次」是這個寫法的內建性質。"""),
     "<strong>優點</strong>：",
     ("ul", [
       "<strong>不需要排序</strong>（Counter 不在乎順序）",
       "<strong>不需要記住 <code>not used[i-1]</code> 那個容易寫錯的條件</strong>",
       "<strong>剪枝更徹底</strong>：分支數是「不同值的個數」而不是 <code>n</code>。"
       "在重複值很多時（例如 8 個 1），第一層只有 1 個分支而不是 8 個。",
     ]),
     "<strong>缺點</strong>：產生的順序取決於 dict 的迭代順序"
     "（Python 3.7+ 是插入順序，所以是「第一次出現的順序」）。"
     "如果需要字典序，要先排序或用 <code>sorted(counter)</code>。",
     "<strong>這個寫法我更推薦</strong> —— 它把「去重」從「搜尋時的判斷」"
     "變成了「資料結構的性質」，比較不容易出錯。",
   ], "O(n! · n)", "O(n)", "分支數 = 不同值的個數", "Counter + path + 遞迴深度"),
 ],
 "compare": (["解法", "要排序？", "去重方式", "重複值多時", "好記程度"],
   [["一、used + 同層跳過", "✔ 必須", "搜尋時判斷", "分支數仍是 n", "★★★☆☆"],
    ["二、Counter", "✘ 不用", "資料結構保證", "分支數 = 不同值數", "★★★★★"]]),
 "edges": [
   "<strong>全部相同</strong>：<code>[0,0,0]</code> → <code>[[0,0,0]]</code>（只有一個）。"
   "<strong>最能抓出去重 bug 的測資。</strong>",
   "<strong>成對重複</strong>：<code>[1,1,2,2]</code> → 6 個"
   "（<code>4!/(2!·2!) = 6</code>）。",
   "<strong>完全沒有重複</strong>：<code>[1,2,3]</code> → 6 個。退化成第 46 題。",
   "<strong>單一元素</strong>：<code>[1]</code> → <code>[[1]]</code>。",
   "<strong>忘記排序</strong>：<code>[1,2,1]</code> 會輸出 6 個（含重複）而不是 3 個。",
   "<strong>條件寫成 <code>i &gt; 0 and nums[i] == nums[i-1]</code>（漏掉 used）</strong>："
   "<code>[1,1,2]</code> 只會輸出 <code>[[1,2,1],[2,1,1]]</code>，"
   "漏掉 <code>[1,1,2]</code> —— 因為「用兩個 1」被完全禁止了。",
 ],
 "follow": [
   ("h", "追問一：這個「同層去重」的條件，和第 40 題的有什麼關係？"),
   ("c", """第 40 題（組合，用 start）：
    if i > start and candidates[i] == candidates[i-1]: continue

第 47 題（排列，用 used）：
    if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue

兩者在說同一件事：
    「同一層裡，相同的值只選第一次出現的那個」

差別只在「怎麼判斷『同一層』」：
    組合題有 start，i == start 就是「這一層的第一個」
    排列題沒有 start，改用 not used[i-1] 判斷
        （前一個相同的值沒被用 -> 它在這一層還沒被選 -> 我是重複的）

第 90 題（子集）用的是組合的那一套。

背三個條件不如記一句話：
    「讓每個答案只有唯一一條生成路徑」""",),
   ("h", "追問二：事後用 set 去重可以嗎？"),
   ("c", """可以（n <= 8，最多 40320 個），但有兩個問題：

  1. 做了白工：重複的子樹被完整搜過，只是結果被丟掉。
     [0]*8 會搜 8! = 40320 條路徑，而答案只有 1 個。
     浪費 99.998%。

  2. 需要 O(答案數) 的額外記憶體存 set。

Counter 版本在同樣的輸入下只會搜 1 條路徑。
差距是天文數字。

「在生成時避免重複」永遠優於「生成後再去重」。""",),
   ("h", "追問三：不同排列的總數怎麼算？"),
   "<strong>多重集合的排列數</strong>：<code>n! / (c₁! × c₂! × ... × cₖ!)</code>，"
   "其中 <code>cᵢ</code> 是第 i 個不同值出現的次數。"
   "這個公式可以拿來驗證你的程式輸出的數量對不對 —— "
   "<strong>在寫回溯題時，先算出「答案應該有幾個」是非常有效的除錯手段。</strong>",
 ],
 "related": [
   "<strong>第 46 題 Permutations</strong> —— 沒有重複的版本",
   "<strong>第 40 題 Combination Sum II</strong> —— 組合的同層去重",
   "<strong>第 90 題 Subsets II</strong> —— 子集的同層去重",
   "<strong>第 31 題 Next Permutation</strong> —— 它天然就會跳過重複",
 ],
 "check": [
   "去重條件裡的 <code>not used[i-1]</code> 在表達什麼？漏掉它會輸出什麼？",
   "為什麼一定要先排序？<code>[1,2,1]</code> 不排序會怎樣？",
   "Counter 版本為什麼不需要任何去重判斷？它的「同一層」是什麼？",
   "<code>[1,1,2,2]</code> 應該有幾個答案？用公式算一遍。",
 ],
})
print("P47 written")
