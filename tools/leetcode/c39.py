# -*- coding: utf-8 -*-
"""第 39–41 題。"""
import random, collections, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(39)

# ==================== 39. Combination Sum ====================
S["p39"] = '''class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()          # 排序讓剪枝成立（也讓輸出比較整齊）
        out = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                out.append(path[:])        # 一定要複製！path 之後還會被改
                return

            for i in range(start, len(candidates)):
                if candidates[i] > remain:
                    break                  # 排序後，後面只會更大 -> 整層剪掉

                path.append(candidates[i])
                # 傳 i 而不是 i+1：同一個數字可以重複使用
                backtrack(i, remain - candidates[i])
                path.pop()

        backtrack(0, target)
        return out'''

S["p39_dp"] = '''class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # dp[t] = 湊出金額 t 的所有組合
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]               # 湊出 0 只有一種方法：什麼都不拿

        # 外層跑「候選」、內層跑「金額」-> 每個組合只會被「非遞減」地生成一次
        for c in sorted(candidates):
            for t in range(c, target + 1):
                for combo in dp[t - c]:
                    dp[t].append(combo + [c])

        return dp[target]'''

_p39 = [S.load(k) for k in ("p39", "p39_dp")]


def _norm(res):
    return sorted(tuple(sorted(x)) for x in res)


def _p39_ref(cands, target):
    """用完全背包式的暴力枚舉當基準。"""
    res = []
    cands = sorted(set(cands))

    def go(i, remain, cur):
        if remain == 0:
            res.append(list(cur))
            return
        if i == len(cands):
            return
        k = 0
        while k * cands[i] <= remain:
            go(i + 1, remain - k * cands[i], cur + [cands[i]] * k)
            k += 1
    go(0, target, [])
    return res


for c, t in [([2, 3, 6, 7], 7), ([2, 3, 5], 8), ([2], 1), ([7, 3, 2], 18),
             ([8, 7, 4, 3], 11)]:
    e = _norm(_p39_ref(c, t))
    for sol in _p39:
        g = _norm(sol.combinationSum(list(c), t))
        assert g == e, ("P39", c, t, sol, g, e)
        assert len(g) == len(set(g)), ("P39 dup", c, t, sol)
for _ in range(600):
    c = random.sample(range(2, 9), random.randint(1, 4))
    t = random.randint(1, 14)
    e = _norm(_p39_ref(c, t))
    for sol in _p39:
        g = _norm(sol.combinationSum(list(c), t))
        assert g == e, ("P39", c, t, sol, g, e)
print("P39 solutions OK")

_P39_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">candidates = [2, 3, 6, 7]，target = 7。虛線是被剪掉的分支。</text>
            <g font-size="12" text-anchor="middle" font-family="monospace">
              <text x="320" y="44" fill="var(--gold)">[] remain=7</text>
              <text x="120" y="96" fill="var(--accent)">[2] r=5</text>
              <text x="300" y="96" fill="var(--accent)">[3] r=4</text>
              <text x="440" y="96" fill="var(--text-muted)" opacity="0.5">[6] r=1</text>
              <text x="560" y="96" fill="#ff8a65">[7] r=0 ✔</text>
              <text x="70" y="148" fill="var(--accent)">[2,2] r=3</text>
              <text x="190" y="148" fill="var(--accent)">[2,3] r=2</text>
              <text x="300" y="148" fill="var(--text-muted)" opacity="0.5">[3,3] r=1</text>
              <text x="70" y="200" fill="var(--accent)">[2,2,2] r=1</text>
              <text x="200" y="200" fill="#ff8a65">[2,2,3] r=0 ✔</text>
              <text x="330" y="200" fill="var(--text-muted)" opacity="0.5">[2,3,3] r=-1</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.3">
              <line x1="300" y1="52" x2="140" y2="84"/>
              <line x1="316" y1="52" x2="304" y2="84"/>
              <line x1="120" y1="104" x2="80" y2="136"/>
              <line x1="134" y1="104" x2="184" y2="136"/>
              <line x1="70" y1="156" x2="70" y2="188"/>
              <line x1="86" y1="156" x2="180" y2="188"/>
            </g>
            <g stroke="var(--border)" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.5">
              <line x1="336" y1="52" x2="428" y2="84"/>
              <line x1="344" y1="52" x2="544" y2="84"/>
              <line x1="304" y1="104" x2="300" y2="136"/>
              <line x1="200" y1="156" x2="320" y2="188"/>
            </g>
            <text x="20" y="240" fill="var(--text-muted)" font-size="12">關鍵一：遞迴傳 <tspan fill="var(--gold)">i</tspan>（不是 i+1）→ 同一個數字可以再選一次</text>
            <text x="20" y="262" fill="var(--text-muted)" font-size="12">關鍵二：從 <tspan fill="var(--gold)">start</tspan> 開始而不是 0 → 保證組合是「非遞減」的，天然去重</text>
            <text x="20" y="288" fill="var(--gold)" font-size="12">答案：[[2,2,3], [7]]　注意沒有 [3,2,2] —— 因為 start 限制住了順序。</text>'''

emit({
 "num": 39, "slug": "combination-sum",
 "en": [
   "Given an array of <strong>distinct</strong> integers <code>candidates</code> and a target "
   "integer <code>target</code>, return a list of all <strong>unique combinations</strong> of "
   "<code>candidates</code> where the chosen numbers sum to <code>target</code>.",
   "The <strong>same</strong> number may be chosen from <code>candidates</code> an "
   "<strong>unlimited number of times</strong>. Two combinations are unique if the frequency "
   "of at least one of the chosen numbers is different.",
 ],
 "zh": [
   "給你一個<strong>元素互不相同</strong>的整數陣列 <code>candidates</code> 和一個目標值 "
   "<code>target</code>，找出所有能讓總和等於 <code>target</code> 的<strong>不重複組合</strong>。",
   "<strong>同一個數字可以無限次重複使用</strong>。"
   "兩個組合只要有任何一個數字的<strong>使用次數</strong>不同，就算不同的組合。",
 ],
 "pre": [
   ("note", "三句話決定整題的寫法", [
     ("c", """1. 「元素互不相同」   ->  不用處理候選陣列裡的重複
2. 「可以無限重複用」  ->  遞迴時傳 i 而不是 i+1
3. 「組合不能重複」    ->  用 start 限制「只能往後選」

第 3 點最重要，值得展開：

    如果每一層都從 0 開始選，target=4、candidates=[2]：
        [2,2] 會被生成一次（沒問題）
    但 candidates=[2,3]、target=5：
        [2,3] 和 [3,2] 都會被生成 -> 重複！

    用 start 限制之後，每一層只能選「>= 上一次選的」，
    所以產生的組合永遠是「非遞減」的：
        [2,3] ✔   [3,2] ✘（不會被生成）

    「強制一個固定的順序」是組合類問題去重的標準手法 ——
    它讓每個「多重集合」只有唯一一種生成路徑。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：candidates = [2,3,6,7], target = 7
  輸出：[[2,2,3],[7]]
  說明：2+2+3 = 7，7 = 7。

範例 2
  輸入：candidates = [2,3,5], target = 8
  輸出：[[2,2,2,2],[2,3,3],[3,5]]

範例 3
  輸入：candidates = [2], target = 1
  輸出：[]""",
 "constraints": [
   "1 ≤ <code>candidates.length</code> ≤ 30",
   "2 ≤ <code>candidates[i]</code> ≤ 40",
   "<code>candidates</code> 的所有元素<strong>互不相同</strong>",
   "1 ≤ <code>target</code> ≤ 40",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong><code>candidates[i] ≥ 2</code></strong> —— 沒有 0 也沒有 1。"
       "<strong>如果允許 0，遞迴會無限深</strong>（一直選 0，remain 永遠不變）。"
       "這一條保證每選一個數 <code>remain</code> 至少減 2，遞迴深度最多 <code>target/2 = 20</code>。",
       "<strong>target ≤ 40</strong>，所以答案的數量有限（題目說「不超過 150 個組合」）。"
       "這是在告訴你：<strong>直接枚舉就好，不需要擔心爆炸</strong>。",
       "<strong>元素互不相同</strong> —— 這是和第 40 題最大的差別。"
       "那題候選可以重複，去重會麻煩很多。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P39_FIG, "0 0 640 300"),
 ],
 "approaches": [
   ap("解法一", "回溯（標準解）", [
     ("c", S["p39"]),
     ("h", "三個關鍵，缺一不可"),
     ("c", """① backtrack(i, ...) 而不是 backtrack(i + 1, ...)
      -> 允許同一個數字再選一次
      -> 這是「無限重複」的實作方式

② for i in range(start, len(...)) 而不是 range(len(...))
      -> 只能往後選，保證組合非遞減
      -> 這是「去重」的實作方式

③ out.append(path[:]) 而不是 out.append(path)
      -> path 是共用的 list，之後還會被 pop 和 append
      -> 不複製的話，out 裡全部都會變成同一個（而且最後是空的）
      -> 這是 Python 回溯題第一名的 bug"""),
     ("h", "剪枝：<code>if candidates[i] &gt; remain: break</code>"),
     ("c", """因為 candidates 已經排序，
如果 candidates[i] 已經超過 remain，
那 candidates[i+1], candidates[i+2], ... 只會更大 ——
整個 for 迴圈剩下的部分都不可能有答案。

所以是 break（跳出整層），不是 continue（只跳過這一個）。

沒有排序的話只能寫 continue，效率差很多：
    candidates = [7, 2, 3]，remain = 1
    不排序：檢查 7 ✘、2 ✘、3 ✘   三次
    有排序：檢查 2 ✘ -> break     一次"""),
     ("h", "為什麼不用檢查 <code>remain &lt; 0</code>？"),
     "因為剪枝已經保證了 <code>candidates[i] &lt;= remain</code>，"
     "所以 <code>remain - candidates[i] &gt;= 0</code>，永遠不會變成負數。"
     "<strong>剪枝同時扮演了「邊界檢查」的角色</strong> —— 這是好設計的副產品。",
     ("h", "複雜度"),
     "回溯類問題的複雜度很難給出緊的上界。"
     "粗略地說，搜尋樹的深度是 O(target / min(candidates))，"
     "每個節點的分支數最多 <code>len(candidates)</code>，"
     "所以最壞是 O(n^(target/min))。"
     "但實際上剪枝讓它遠低於這個數字 —— "
     "<strong>而且輸出本身就有 O(答案數 × 平均長度) 那麼大，這是無法避免的下界。</strong>",
   ], "O(n^(T/m))", "O(T/m)", "T = target，m = 最小候選；剪枝後遠低於上界",
      "遞迴深度；不算輸出", optimal=True),

   ap("解法二", "動態規劃（完全背包的組合列舉版）", [
     "這題本質上是<strong>完全背包問題</strong>（每種物品可以拿無限個）。"
     "如果只問「有幾種組合」，DP 是標準答案；"
     "要「列出所有組合」，DP 也能做，只是要存下所有組合。",
     ("c", S["p39_dp"]),
     ("h", "迴圈順序決定了「組合」還是「排列」"),
     ("c", """外層跑候選、內層跑金額  ->  組合（本題要的）
    for c in candidates:
        for t in range(c, target+1):
            dp[t] += dp[t-c] 加上 c

    因為每個候選只被「處理一次」，
    生成的組合裡的數字順序一定是「候選被處理的順序」——
    也就是排序後的非遞減順序。
    [2,3] 會出現，[3,2] 不會。

外層跑金額、內層跑候選  ->  排列（第 377 題要的）
    for t in range(1, target+1):
        for c in candidates:
            dp[t] += dp[t-c] 加上 c

    每個金額都把所有候選試一遍，
    [2,3] 和 [3,2] 都會被生成。

這兩個迴圈只是交換順序，語意卻完全不同。
這是背包問題裡最容易搞混、也最值得記住的一點。"""),
     "<strong>優點</strong>：沒有遞迴，而且 <code>dp</code> 陣列裡有「湊出每個金額」的所有答案 —— "
     "如果題目要問多個 target，這個解法只要算一次。",
     "<strong>缺點</strong>：<strong>記憶體大很多</strong>。"
     "它把所有中間金額的組合都存起來，而回溯只需要當前路徑。"
     "在這題（target ≤ 40）沒問題，但 target 大一點就會爆。",
     "<strong>所以：只問「有幾種」用 DP（只存數量，O(target) 空間）；"
     "要「列出來」用回溯。</strong>",
   ], "O(target × n × 答案數)", "O(target × 答案總大小)",
      "每個金額存所有組合", "所有中間結果"),
 ],
 "compare": (["解法", "時間", "空間", "適合", "備註"],
   [["一、回溯", "O(n^(T/m))", "O(T/m)", "列出所有組合", "面試標準解"],
    ["二、DP", "較大", "大", "多次查詢、只問數量", "完全背包"]]),
 "edges": [
   "<strong>湊不出來</strong>：<code>([2], 1)</code> → <code>[]</code>。",
   "<strong>剛好一個數字就是答案</strong>：<code>([2,3,6,7], 7)</code> 裡的 <code>[7]</code>。",
   "<strong>需要重複很多次</strong>：<code>([2], 40)</code> → <code>[[2]×20]</code>。遞迴深度 20。",
   "<strong>候選沒排序</strong>：<code>([7,3,2], 18)</code>。"
   "不先排序的話 <code>break</code> 剪枝會錯剪。",
   "<strong>忘記 <code>path[:]</code></strong>：輸出會是一堆空 list（或全部相同）。"
   "<strong>先寫 <code>path[:]</code> 再想別的。</strong>",
   "<strong>傳 <code>i+1</code> 而不是 <code>i</code></strong>："
   "<code>([2,3,6,7], 7)</code> 會少掉 <code>[2,2,3]</code>，只剩 <code>[7]</code>。",
   "<strong>從 0 而不是 <code>start</code> 開始</strong>："
   "會產生 <code>[2,2,3]</code>、<code>[2,3,2]</code>、<code>[3,2,2]</code> 三份重複。",
 ],
 "follow": [
   ("h", "追問一：如果候選裡有重複、而且每個只能用一次呢？"),
   "那就是第 40 題（Combination Sum II）。兩個改動：",
   ("ul", [
     "遞迴傳 <code>i + 1</code>（每個只能用一次）",
     "加上「同一層跳過重複值」：<code>if i &gt; start and candidates[i] == candidates[i-1]: continue</code>",
   ]),
   "<strong>注意是 <code>i &gt; start</code> 不是 <code>i &gt; 0</code></strong> —— "
   "同一層不能重複選同一個值，但<strong>不同層可以</strong>（那是「用了兩個相同的數」，是合法的）。",
   ("h", "追問二：如果只問「有幾種組合」呢？"),
   "完全背包的標準 DP，O(target) 空間：",
   ("c", """dp = [0] * (target + 1)
dp[0] = 1
for c in candidates:          # 外層候選 -> 算「組合」
    for t in range(c, target + 1):
        dp[t] += dp[t - c]
return dp[target]

如果把兩層迴圈交換，算出來的是「排列」數（第 377 題）。
這是背包問題最經典的一組對照。"""),
   ("h", "追問三：如果 target 很大（例如 10⁹）呢？"),
   "列出所有組合是不可能的（答案數量爆炸）。"
   "如果只問「有沒有解」，那是<strong>硬幣問題（Frobenius 問題）</strong>："
   "當所有候選的最大公因數是 1 時，"
   "存在一個「Frobenius 數」，超過它的所有金額都湊得出來。"
   "兩個數 a、b 互質時，這個數是 <code>ab − a − b</code>（Chicken McNugget 定理）。"
   "三個以上就沒有簡單公式了。",
   ("h", "追問四：這個回溯模板還能用在哪？"),
   ("c", """start 參數控制「能選哪些」，是組合類回溯的核心：

    傳 i    + start  ->  可重複、組合         （第 39 題）
    傳 i+1  + start  ->  不可重複、組合       （第 40、77、78、90 題）
    不用 start，用 used[] 標記  ->  排列      （第 46、47 題）

三種變化涵蓋了 LeetCode 上絕大多數的枚舉題。"""),
 ],
 "related": [
   "<strong>第 40 題 Combination Sum II</strong> —— 每個只能用一次 + 候選有重複",
   "<strong>第 216 題 Combination Sum III</strong> —— 限定用 k 個數字",
   "<strong>第 377 題 Combination Sum IV</strong> —— 其實是「排列」，只問數量",
   "<strong>第 77／78／90 題</strong> —— 同一個回溯模板",
   "<strong>第 322 題 Coin Change</strong> —— 完全背包的最少硬幣數",
 ],
 "check": [
   "遞迴為什麼傳 <code>i</code> 而不是 <code>i+1</code>？改成 <code>i+1</code> 會少掉哪些答案？",
   "<code>start</code> 參數是怎麼達成去重的？如果每層都從 0 開始，<code>([2,3], 5)</code> 會輸出什麼？",
   "<code>out.append(path[:])</code> 的 <code>[:]</code> 為什麼不能省？不寫會得到什麼？",
   "DP 版本的兩層迴圈如果交換順序，算出來的是什麼？和本題的差別在哪？",
 ],
})
print("P39 written")

# ==================== 40. Combination Sum II ====================
S["p40"] = '''class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()          # 排序：讓相同的值相鄰，去重才做得到
        out = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                out.append(path[:])
                return

            for i in range(start, len(candidates)):
                # 剪枝：排序後，後面只會更大
                if candidates[i] > remain:
                    break

                # 去重：同一層裡，相同的值只取「第一次出現」
                # 注意是 i > start 不是 i > 0
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1, remain - candidates[i])   # i+1：每個只用一次
                path.pop()

        backtrack(0, target)
        return out'''

S["p40_counter"] = '''from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 另一種去重方式：把「相同的值」合併成 (值, 可用次數)
        items = sorted(Counter(candidates).items())
        out = []

        def backtrack(idx: int, remain: int, path: List[int]) -> None:
            if remain == 0:
                out.append(path)          # path 每層都是新的 list，不會被改到
                return
            if idx == len(items):
                return

            value, avail = items[idx]

            # 這個值可以用 0 次、1 次、…、avail 次，各是一條分支
            k = 0
            while k <= avail and value * k <= remain:
                backtrack(idx + 1, remain - value * k, path + [value] * k)
                k += 1

        backtrack(0, target, [])
        return out'''

_p40 = [S.load(k) for k in ("p40", "p40_counter")]


def _p40_ref(cands, target):
    found = set()
    n = len(cands)
    for r in range(1, n + 1):
        for combo in itertools.combinations(sorted(cands), r):
            if sum(combo) == target:
                found.add(combo)
    return sorted(found)


for c, t in [([10, 1, 2, 7, 6, 1, 5], 8), ([2, 5, 2, 1, 2], 5), ([1], 1),
             ([1], 2), ([2, 2, 2], 4), ([1, 1, 1, 1], 2)]:
    e = _p40_ref(c, t)
    for sol in _p40:
        g = sorted(tuple(sorted(x)) for x in sol.combinationSum2(list(c), t))
        assert g == e, ("P40", c, t, sol, g, e)
        assert len(g) == len(set(g)), ("P40 dup", c, t, sol)
for _ in range(1500):
    c = [random.randint(1, 5) for _ in range(random.randint(1, 8))]
    t = random.randint(1, 12)
    e = _p40_ref(c, t)
    for sol in _p40:
        g = sorted(tuple(sorted(x)) for x in sol.combinationSum2(list(c), t))
        assert g == e, ("P40", c, t, sol, g, e)
print("P40 solutions OK")

_P40_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">去重的關鍵：同一層不能重複選「同樣的值」，但不同層可以</text>
            <text x="20" y="50" fill="var(--text-muted)" font-size="12">candidates 排序後 = [1, 1, 2, 5, 6, 7, 10]，target = 8</text>
            <g font-size="12" font-family="monospace">
              <text x="40" y="84" fill="var(--gold)">第 0 層（start = 0）：i 可以是 0..6</text>
              <text x="70" y="108" fill="var(--accent)">i = 0 → 選 candidates[0] = 1 ✔（第一次出現）</text>
              <text x="70" y="130" fill="#ff8a65">i = 1 → candidates[1] = 1 == candidates[0]，而且 i &gt; start</text>
              <text x="110" y="150" fill="#ff8a65">→ continue（跳過，否則會產生重複的組合）</text>
              <text x="70" y="172" fill="var(--accent)">i = 2 → 選 2 ✔</text>
              <text x="70" y="194" fill="var(--text-muted)">…</text>
            </g>
            <line x1="20" y1="212" x2="620" y2="212" stroke="var(--border)"/>
            <g font-size="12" font-family="monospace">
              <text x="40" y="242" fill="var(--gold)">第 1 層（start = 1，因為上一層選了 i = 0）：i 可以是 1..6</text>
              <text x="70" y="266" fill="var(--accent)">i = 1 → candidates[1] = 1，但 i == start，不跳過 ✔</text>
              <text x="110" y="286" fill="var(--accent)">→ 得到 [1, 1]，這是合法的（用了兩個「不同位置」的 1）</text>
            </g>
            <text x="20" y="322" fill="var(--gold)" font-size="12">所以條件是 i &gt; start，不是 i &gt; 0。寫成 i &gt; 0 會漏掉 [1,1,6] 這類答案。</text>'''

emit({
 "num": 40, "slug": "combination-sum-ii",
 "en": [
   "Given a collection of candidate numbers (<code>candidates</code>) and a target number "
   "(<code>target</code>), find all unique combinations in <code>candidates</code> where the "
   "candidate numbers sum to <code>target</code>.",
   "Each number in <code>candidates</code> may only be used <strong>once</strong> in the "
   "combination. Note: the solution set must not contain duplicate combinations.",
 ],
 "zh": [
   "給你一個候選數字陣列 <code>candidates</code>（<strong>可能含有重複的值</strong>）"
   "和一個目標值 <code>target</code>，找出所有能讓總和等於 <code>target</code> 的組合。",
   "<code>candidates</code> 裡的<strong>每個數字在每個組合中只能用一次</strong>。"
   "答案裡<strong>不能有重複的組合</strong>。",
 ],
 "pre": [
   ("note", "和第 39 題的兩個差異", [
     ("c", """第 39 題                      第 40 題（本題）
--------------------          --------------------
候選互不相同                    候選「可能重複」
每個可以用無限次                 每個只能用一次

程式碼的差異只有兩處：

    ① 遞迴傳 i + 1（不是 i）
       -> 每個位置只能用一次

    ② 多一行去重
       if i > start and candidates[i] == candidates[i-1]: continue
       -> 同一層裡，相同的值只選第一次出現的那個

第 ② 點是全題的重點，而且那個 i > start 非常容易寫錯成 i > 0。"""),
     "<strong>「值重複」和「位置重複」要分清楚。</strong>"
     "<code>[1, 1, 6]</code> 是合法答案（用了兩個<strong>不同位置</strong>的 1），"
     "但同一個位置的 1 不能用兩次。"
     "而 <code>[1, 1, 6]</code> 只能出現一次，不能因為「有兩種選法」就輸出兩份。",
   ]),
 ],
 "examples": """範例 1
  輸入：candidates = [10,1,2,7,6,1,5], target = 8
  輸出：[[1,1,6],[1,2,5],[1,7],[2,6]]
  說明：注意 [1,1,6] 用了兩個不同位置的 1，是合法的。
        而 [1,7] 只出現一次，雖然有兩個 1 可以選。

範例 2
  輸入：candidates = [2,5,2,1,2], target = 5
  輸出：[[1,2,2],[5]]""",
 "constraints": [
   "1 ≤ <code>candidates.length</code> ≤ 100",
   "1 ≤ <code>candidates[i]</code> ≤ 50",
   "1 ≤ <code>target</code> ≤ 30",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong><code>candidates[i]</code> 最小是 1</strong>（第 39 題最小是 2）。"
       "但因為每個只能用一次，所以不會有無限遞迴的問題 —— "
       "遞迴深度最多是 <code>len(candidates) = 100</code>。",
       "<strong>target ≤ 30，但 candidates[i] 可以到 50</strong>。"
       "所以會有很多候選一開始就超過 target —— 剪枝很有效。",
       "<strong>候選長度可以到 100</strong>，"
       "不剪枝的話最壞是 2¹⁰⁰ 個子集合 —— 完全不可行。"
       "<strong>排序 + break 剪枝 + 去重</strong>三者缺一不可。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P40_FIG, "0 0 640 334"),
 ],
 "approaches": [
   ap("解法一", "回溯 + 同層去重（標準解）", [
     ("c", S["p40"]),
     ("h", "為什麼是 <code>i &gt; start</code> 而不是 <code>i &gt; 0</code>？"),
     ("c", """candidates 排序後 = [1, 1, 2, 5, 6, 7, 10]，target = 8

寫 i > start（正確）：
    第 0 層 start=0：
        i=0 選 1  ->  進入第 1 層，start=1
            第 1 層 i=1：i == start，不跳過
                         選第二個 1  ->  [1,1]  ✔
                         繼續下去找到 [1,1,6] ✔
        i=1：i > start(0) 且值相同  ->  跳過 ✔
             （避免產生和 i=0 完全一樣的子樹）

寫 i > 0（錯誤）：
    第 1 層 i=1：i > 0 且 candidates[1] == candidates[0]
                 -> 跳過！
    結果 [1,1,6] 永遠生不出來 ✘

一句話總結：
    「同一層」不能選重複的值（會產生一模一樣的子樹）
    「不同層」可以選重複的值（那是用了兩個不同的位置）

    start 剛好就是「這一層的起點」，
    所以 i > start 精確地表達了「這一層裡，不是第一個」。"""),
     ("h", "為什麼這樣就能完全去重？"),
     ("c", """排序之後，相同的值連續排在一起。

考慮值 v 在陣列裡出現在位置 p, p+1, ..., p+k-1（共 k 個）。

去重規則保證：
    如果要用 j 個 v（j <= k），
    程式只會選「最前面的 j 個」：p, p+1, ..., p+j-1

    因為：
    - 第一次選 v 時，只允許 i == start 或「i 是這段的第一個」
    - 選了之後 start 變成 i+1，下一層可以選 p+1
    - 所以生成的一定是連續的前綴

    而 [v(p), v(p+2)] 這種「跳著選」的組合會被跳過 ——
    但它和 [v(p), v(p+1)] 的「值」完全一樣，所以沒有損失。

每個「值的多重集合」都恰好對應唯一一條生成路徑 -> 不重不漏 ✔"""),
     ("h", "三個要素的分工"),
     ("t", ["程式碼", "負責什麼"],
       [["<code>candidates.sort()</code>", "讓相同的值相鄰，去重和剪枝才成立"],
        ["<code>if candidates[i] &gt; remain: break</code>", "剪枝：後面只會更大"],
        ["<code>if i &gt; start and 值相同: continue</code>", "去重：同層不選重複值"],
        ["<code>backtrack(i + 1, ...)</code>", "每個位置只用一次"]]),
   ], "O(2ⁿ)", "O(n)", "最壞列舉所有子集；剪枝後遠低於此",
      "遞迴深度；不算輸出", optimal=True),

   ap("解法二", "先合併成 (值, 次數)，再枚舉次數", [
     "另一種去重的思路：<strong>與其在搜尋時跳過重複，不如一開始就把重複合併掉。</strong>"
     "把 <code>[1,1,2,5,...]</code> 變成 <code>[(1,2), (2,1), (5,1), ...]</code>，"
     "然後對每個「值」枚舉「要用幾個」。",
     ("c", S["p40_counter"]),
     ("c", """items = [(1,2), (2,1), (5,1), (6,1), (7,1), (10,1)]

對 (1, 2)：可以用 0 個、1 個、或 2 個 1
    -> 三條分支，各自往下遞迴
對 (2, 1)：可以用 0 個或 1 個 2
    -> 兩條分支
...

這樣天然就不會產生重複，
因為「這個值要用幾個」這個決定，對每個值只做一次。

path 的寫法：
    這裡把 path 當成「不可變的參數」傳下去（path + [value] * k），
    每層都建一個新 list，所以完全不需要手動撤銷。
    代價是每層複製一次 —— 在這題（target <= 30）完全無所謂，
    而且它換來的是「絕對不會忘記 pop」。

    如果要省那個複製，就得改回 append/pop 的寫法，
    但這裡一次 append 了 k 個，撤銷時也要一次 pop 掉 k 個，
    比第 39 題的「一次一個」容易寫錯。"""),
     "<strong>優點</strong>：去重的邏輯變成「資料的預處理」而不是「搜尋時的判斷」，"
     "概念上更乾淨，也不會寫錯 <code>i &gt; start</code>。",
     "<strong>缺點</strong>：<code>path</code> 的維護比較繞，而且分支數變成"
     "「每個值有 avail+1 種選擇」而不是「每個位置選或不選」—— "
     "在重複值很多的時候反而更快，重複值少的時候差不多。",
     "<strong>這個「合併相同物品」的想法就是「多重背包」的標準處理方式</strong>，"
     "值得記起來。",
   ], "O(∏(cnt+1))", "O(n)", "每個不同的值有 cnt+1 種選擇", "遞迴深度"),
 ],
 "compare": (["解法", "去重方式", "好寫程度", "重複值多時", "備註"],
   [["一、同層跳過", "搜尋時判斷", "★★★★☆", "普通", "面試標準；小心 i &gt; start"],
    ["二、合併計數", "資料預處理", "★★★☆☆", "較快", "多重背包的思路"]]),
 "edges": [
   "<strong>候選有重複，答案要用到多個</strong>：<code>([10,1,2,7,6,1,5], 8)</code> "
   "→ 含 <code>[1,1,6]</code>。<code>i &gt; 0</code> 的寫法會漏掉它。",
   "<strong>候選有重複，答案只用一個</strong>：同上輸入的 <code>[1,7]</code> 只能出現一次。"
   "<strong>沒有去重的話會出現兩次。</strong>",
   "<strong>全部相同</strong>：<code>([2,2,2], 4)</code> → <code>[[2,2]]</code>（只有一組）。",
   "<strong>全部相同且湊不出來</strong>：<code>([1,1,1,1], 2)</code> → <code>[[1,1]]</code>。",
   "<strong>單一元素</strong>：<code>([1], 1)</code> → <code>[[1]]</code>；<code>([1], 2)</code> → <code>[]</code>。",
   "<strong>候選比 target 大</strong>：全部被 <code>break</code> 剪掉，回 <code>[]</code>。",
 ],
 "follow": [
   ("h", "追問一：這個「同層去重」的模板還能用在哪？"),
   ("c", """完全一樣的一行，出現在：

    第 40 題  Combination Sum II    （本題）
    第 47 題  Permutations II        （排列，條件稍有不同）
    第 90 題  Subsets II             （子集）

第 47 題的去重條件是：
    if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue

差別在多了 not used[i-1]，因為排列題用的是 used[] 而不是 start。
語意一樣：「同一層裡，相同的值只選第一次」。

背這三題的去重條件不如理解一句話：
    「讓每個答案只有唯一一條生成路徑」"""),
   ("h", "追問二：如果不排序，改成用 set 去重可以嗎？"),
   "可以（把每個答案排序後放進 set），但有兩個代價：",
   ("ul", [
     "<strong>做了白工</strong>：重複的子樹還是被完整搜過一遍，只是結果被丟掉。"
     "在候選有大量重複時，這個浪費是指數級的。",
     "<strong>失去 <code>break</code> 剪枝</strong>：不排序就不能靠「後面只會更大」提早結束。",
   ]),
   "<strong>「在生成時避免重複」永遠優於「生成後再去重」</strong> —— "
   "這是所有枚舉類問題的通則。",
   ("h", "追問三：如果 target 很大、候選很多呢？"),
   "如果只問「有沒有解」或「有幾種」，那是 <strong>0/1 背包</strong>，"
   "用 DP 在 O(n × target) 解決。"
   "但「列出所有組合」本質上是指數的 —— 答案數量可能就有指數多個，"
   "任何演算法都無法避免。",
 ],
 "related": [
   "<strong>第 39 題 Combination Sum</strong> —— 可重複使用的版本",
   "<strong>第 47 題 Permutations II</strong> —— 排列的去重",
   "<strong>第 90 題 Subsets II</strong> —— 子集的去重",
   "<strong>第 216 題 Combination Sum III</strong> —— 固定個數",
 ],
 "check": [
   "去重條件為什麼是 <code>i &gt; start</code> 而不是 <code>i &gt; 0</code>？"
   "請用 <code>([1,1,6], 8)</code> 說明後者會漏掉什麼。",
   "為什麼「同一層不能選重複值」但「不同層可以」？兩者的語意差別是什麼？",
   "為什麼一定要先排序？它同時讓哪兩件事成立？",
   "第 47 題（排列）的去重條件多了 <code>not used[i-1]</code>，它在扮演 <code>start</code> 的什麼角色？",
 ],
})
print("P40 written")
