# -*- coding: utf-8 -*-
"""第 55–58 題。"""
import random
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(55)

# ==================== 55. Jump Game ====================
S["p55_greedy"] = '''class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0            # 目前能到達的最遠位置
        for i, v in enumerate(nums):
            if i > farthest:    # 連這一格都走不到 -> 卡住了
                return False
            farthest = max(farthest, i + v)
            if farthest >= len(nums) - 1:
                return True     # 已經能到終點，提早結束
        return True'''

S["p55_back"] = '''class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 從終點往回推：維護「目前必須到得了的目標」
        target = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i      # 只要到得了 i，就到得了原本的 target
        return target == 0'''

S["p55_dp"] = '''class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reach = [False] * n     # reach[i] = 能不能到達位置 i
        reach[0] = True

        for i in range(n):
            if not reach[i]:
                continue
            for j in range(i + 1, min(i + nums[i], n - 1) + 1):
                reach[j] = True

        return reach[n - 1]'''

_p55 = [S.load(k) for k in ("p55_greedy", "p55_back", "p55_dp")]
for c in [[2, 3, 1, 1, 4], [3, 2, 1, 0, 4], [0], [1], [0, 1], [2, 0, 0],
          [1, 0, 1, 0], [2, 5, 0, 0]]:
    e = _p55[2].canJump(list(c))
    for sol in _p55:
        assert sol.canJump(list(c)) is e, ("P55", c, sol, sol.canJump(list(c)), e)
for _ in range(5000):
    c = [random.randint(0, 4) for _ in range(random.randint(1, 10))]
    e = _p55[2].canJump(list(c))
    for sol in _p55:
        assert sol.canJump(list(c)) is e, ("P55", c, sol)
print("P55 solutions OK")

emit({
 "num": 55, "slug": "jump-game",
 "en": [
   "You are given an integer array <code>nums</code>. You are initially positioned at the "
   "array's <strong>first index</strong>, and each element in the array represents your "
   "maximum jump length at that position.",
   "Return <code>true</code> if you can reach the last index, or <code>false</code> otherwise.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，你一開始站在<strong>第一個位置</strong>。"
   "<code>nums[i]</code> 表示從位置 <code>i</code> <strong>最多</strong>能往前跳幾格。",
   "判斷你能不能到達<strong>最後一個位置</strong>，能就回傳 <code>true</code>，不能就 <code>false</code>。",
 ],
 "pre": [
   ("note", "一個變數就夠了：farthest", [
     ("c", """核心洞察：
    我們不需要知道「怎麼跳」，只需要知道「最遠能到哪」。

    因為從位置 i 可以跳 1..nums[i] 格（不是只能跳 nums[i] 格），
    所以「能到達的位置」永遠是一段【連續的】前綴 [0, farthest]。

    既然是連續的，只要記住右端點 farthest 就夠了。

演算法：
    從左往右掃，沿途更新 farthest = max(farthest, i + nums[i])。
    如果走到某個 i 時發現 i > farthest，表示這一格根本到不了 -> False。

nums = [3, 2, 1, 0, 4]
    i=0: 0 <= 0 ✔   farthest = max(0, 0+3) = 3
    i=1: 1 <= 3 ✔   farthest = max(3, 1+2) = 3
    i=2: 2 <= 3 ✔   farthest = max(3, 2+1) = 3
    i=3: 3 <= 3 ✔   farthest = max(3, 3+0) = 3
    i=4: 4 >  3 ✘   到不了 -> False ✔

    卡在索引 3 的那個 0 上。"""),
     "<strong>「可達集合是連續前綴」是這題能用單一變數解決的根本原因。</strong>"
     "如果可以往回跳（第 1306 題），這個性質就不成立了，必須寫真正的 BFS/DFS。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [2,3,1,1,4]
  輸出：true
  說明：0 → 1 → 4，或 0 → 2 → 3 → 4。

範例 2
  輸入：nums = [3,2,1,0,4]
  輸出：false
  說明：不管怎麼跳都會停在索引 3（值是 0），跳不出去。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁴",
   "0 ≤ <code>nums[i]</code> ≤ 10⁵",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n 到 10⁴</strong>。O(n²) 的 DP 是 10⁸ —— 在 Python 裡會 TLE。要 O(n)。",
       "<strong><code>nums[i]</code> 可以是 0</strong> —— 這就是唯一會「卡住」的原因。"
       "如果全部 ≥ 1，答案永遠是 true。",
       "<strong>n 可以是 1</strong>：起點就是終點，答案 true（<strong>即使 <code>nums = [0]</code></strong>）。"
       "這是最常被漏掉的邊界。",
       "<strong><code>nums[i]</code> 可以到 10⁵</strong>，遠大於陣列長度。"
       "<code>i + nums[i]</code> 可能超出陣列 —— 不影響正確性，但要記得它代表「已經能到終點」。",
     ]),
   ]),
 ],
 "idea": [
   "三種解法，其實是同一個結構的三種視角：<strong>正著推、倒著推、或建整張可達表</strong>。",
 ],
 "approaches": [
   ap("解法一", "從左往右貪婪（最推薦）", [
     ("c", S["p55_greedy"]),
     ("h", "為什麼「發現 <code>i &gt; farthest</code> 就 False」是對的？"),
     ("c", """farthest 是「從 [0, i-1] 這些格子出發，最遠能跳到哪」。

如果 i > farthest，表示沒有任何一個「到得了的格子」能跳到 i。
而 i 之後的格子都在 i 右邊，更到不了。
所以直接 False。

反過來，如果掃完整個陣列都沒觸發這個條件，
表示每一格都到得了 —— 包含最後一格 -> True。

（其實不用掃完：farthest >= n-1 就可以提早回 True。）"""),
     ("h", "為什麼這是「貪婪」而不需要回溯？"),
     "因為我們<strong>不需要決定「在哪一格要跳多遠」</strong>。"
     "從位置 <code>i</code> 出發能到的範圍是 <code>[i+1, i+nums[i]]</code>，"
     "而「可達集合」是所有這些範圍的聯集 —— "
     "<strong>而聯集永遠是一段連續前綴</strong>（因為它們都從 <code>i+1</code> 開始，而 <code>i</code> 本身可達）。"
     "所以只要追蹤右端點，不會漏掉任何可能。",
     "<strong>和第 45 題（Jump Game II）的關係</strong>："
     "那題問「最少幾步」，用的是同一個 <code>farthest</code>，"
     "只是多了一個 <code>cur_end</code> 來分層。"
     "<strong>兩題一起看，會發現它們是同一個掃描的兩種輸出。</strong>",
   ], "O(n)", "O(1)", "掃一遍，可提早結束", "一個變數", optimal=True),

   ap("解法二", "從右往左倒推（另一個漂亮的視角）", [
     "換個方向：<strong>維護一個「目標」，從終點開始往左走。"
     "如果某一格能跳到目標，那它就成為新的目標。</strong>",
     ("c", S["p55_back"]),
     ("c", """nums = [2, 3, 1, 1, 4]，target 初值 = 4

i=3: 3 + 1 = 4 >= 4 ✔  target = 3
i=2: 2 + 1 = 3 >= 3 ✔  target = 2
i=1: 1 + 3 = 4 >= 2 ✔  target = 1
i=0: 0 + 2 = 2 >= 1 ✔  target = 0

target == 0 -> True ✔

nums = [3, 2, 1, 0, 4]，target = 4

i=3: 3 + 0 = 3 >= 4 ✘  target 不變（還是 4）
i=2: 2 + 1 = 3 >= 4 ✘  target = 4
i=1: 1 + 2 = 3 >= 4 ✘  target = 4
i=0: 0 + 3 = 3 >= 4 ✘  target = 4

target == 4 != 0 -> False ✔"""),
     "<strong>語意很漂亮</strong>：「要到終點，就必須先到 target；"
     "而要到 target，就必須先到新的 target…」—— 一路把需求往前推。"
     "最後如果需求推到了索引 0，表示從起點出發就能一路達成。",
     "<strong>和解法一等價，但有時候更好想</strong> —— "
     "尤其當題目變成「從終點反推最少步數」或「必經的關鍵點」時。",
   ], "O(n)", "O(1)", "掃一遍", "一個變數"),

   ap("解法三", "可達表 DP（會 TLE 的基準線）", [
     ("c", S["p55_dp"]),
     "直接建一張「每一格能不能到」的表。正確，但 O(n²) —— "
     "最壞情況（每個 <code>nums[i]</code> 都很大）內層迴圈要跑 O(n) 次。",
     "<strong>它的價值是最直白</strong>，可以拿來驗證貪婪解"
     "（本篇的壓力測試就是拿它當基準）。"
     "而且它清楚地展示了「可達集合」這個概念 —— "
     "貪婪法只是發現了「這張表永遠是 <code>True...True False...False</code> 的形狀」，"
     "所以只要記住分界點就夠了。",
   ], "O(n²)", "O(n)", "每格往後標記 O(n) 個", "reach 陣列"),
 ],
 "compare": (["解法", "時間", "空間", "方向", "備註"],
   [["一、貪婪 farthest", "O(n)", "O(1)", "左 → 右", "面試預設"],
    ["二、倒推 target", "O(n)", "O(1)", "右 → 左", "語意漂亮"],
    ["三、可達表", "O(n²)", "O(n)", "左 → 右", "基準線，會 TLE"]]),
 "edges": [
   "<strong>單一元素</strong>：<code>[0]</code> → <strong>true</strong>（起點就是終點）。"
   "<strong>最常被漏掉的邊界。</strong>",
   "<strong>第一格就是 0</strong>：<code>[0, 1]</code> → false。",
   "<strong>剛好卡住</strong>：<code>[3,2,1,0,4]</code> → false。",
   "<strong>剛好跳過去</strong>：<code>[2,0,0]</code> → true（從 0 直接跳到 2）。",
   "<strong>中間有 0 但跳得過</strong>：<code>[2,5,0,0]</code> → true。",
   "<strong>剛好每步走一格</strong>：<code>[1,1,1,1]</code> → true。",
   "<strong>最後一格是 0</strong>：<code>[1,0]</code> → true（到了就不用再跳）。",
 ],
 "follow": [
   ("h", "追問一：如果要問「最少幾步」呢？"),
   "第 45 題（Jump Game II）。同一個 <code>farthest</code>，"
   "再加一個 <code>cur_end</code> 來記「這一層的邊界」。走到邊界就步數 +1。",
   ("h", "追問二：如果可以往回跳呢？"),
   "第 1306 題（Jump Game III）：從 <code>i</code> 可以跳到 <code>i + nums[i]</code> "
   "或 <code>i - nums[i]</code>，問能不能到達某個值為 0 的位置。"
   "<strong>「可達集合是連續前綴」的性質完全失效</strong>，"
   "必須寫真正的 BFS 或 DFS（O(n) 時間、O(n) 空間）。",
   "<strong>這是一個很好的對照</strong>：多了「往回跳」這一個看似小的改動，"
   "就把一個 O(1) 空間的貪婪題，變成了一個需要顯式圖搜尋的題目。",
   ("h", "追問三：如果每一格有不同的「成本」呢？"),
   "那就是加權最短路徑，要用 Dijkstra（O(n log n)）或 DP。"
   "<strong>貪婪之所以能用，完全依賴「每一步的代價相同」</strong>。",
   ("h", "追問四：如果要回傳「卡在哪一格」呢？"),
   "貪婪版在 <code>return False</code> 之前，"
   "<code>farthest</code> 就是「最遠能到的位置」，"
   "而那一格必然是 <code>nums[farthest] == 0</code>（否則還能再往前）。"
   "一行就能加上。",
 ],
 "related": [
   "<strong>第 45 題 Jump Game II</strong> —— 最少步數",
   "<strong>第 1306 題 Jump Game III</strong> —— 可以往回跳，要 BFS",
   "<strong>第 134 題 Gas Station</strong> —— 另一個「掃一遍 + 一個變數」的貪婪",
   "<strong>第 1024 題 Video Stitching</strong> —— 區間覆蓋版的同一個貪婪",
 ],
 "check": [
   "<code>[0]</code> 的答案是什麼？為什麼？",
   "為什麼「可達集合」一定是一段連續前綴？這依賴題目的哪一句話？",
   "解法二的 <code>target</code> 在語意上代表什麼？",
   "如果改成「可以往回跳」，為什麼貪婪就失效了？",
 ],
})
print("P55 written")

# ==================== 56. Merge Intervals ====================
S["p56"] = '''class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])      # 依「起點」排序

        out = []
        for start, end in intervals:
            # 和上一段沒有重疊（上一段的結束 < 這一段的開始）-> 開新的一段
            if not out or out[-1][1] < start:
                out.append([start, end])
            else:
                # 有重疊 -> 把上一段的結束往右延伸
                out[-1][1] = max(out[-1][1], end)

        return out'''

S["p56_sweep"] = '''class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 掃描線：把每個區間拆成「開始 +1」和「結束 -1」兩個事件
        events = []
        for s, e in intervals:
            events.append((s, 0))       # 0 排在 1 前面，讓 [1,2] 和 [2,3] 能合併
            events.append((e, 1))
        events.sort()

        out = []
        depth = 0
        start = 0
        for pos, kind in events:
            if kind == 0:
                if depth == 0:
                    start = pos         # 從 0 變成 1：一段新的合併區間開始
                depth += 1
            else:
                depth -= 1
                if depth == 0:
                    out.append([start, pos])   # 回到 0：這一段結束

        return out'''

_p56 = [S.load(k) for k in ("p56", "p56_sweep")]


def _p56_ref(intervals):
    if not intervals:
        return []
    xs = sorted(intervals)
    res = [list(xs[0])]
    for s, e in xs[1:]:
        if s <= res[-1][1]:
            res[-1][1] = max(res[-1][1], e)
        else:
            res.append([s, e])
    return res


for c in [[[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 4], [4, 5]], [[1, 4], [2, 3]],
          [[1, 4], [0, 4]], [[1, 4], [0, 0]], [], [[1, 1]], [[1, 2], [3, 4]]]:
    e = _p56_ref(c)
    for sol in _p56:
        g = sol.merge([list(x) for x in c])
        assert g == e, ("P56", c, sol, g, e)
for _ in range(4000):
    c = []
    for _ in range(random.randint(0, 7)):
        a = random.randint(0, 12)
        b = random.randint(a, 12)
        c.append([a, b])
    e = _p56_ref(c)
    for sol in _p56:
        g = sol.merge([list(x) for x in c])
        assert g == e, ("P56", c, sol, g, e)
print("P56 solutions OK")

_P56_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">依起點排序後，只需要和「上一個已合併的區間」比較</text>
            <text x="20" y="48" fill="var(--text-muted)" font-size="12">intervals = [[1,3], [2,6], [8,10], [15,18]]</text>
            <g>
              <line x1="40" y1="180" x2="600" y2="180" stroke="var(--text-muted)"/>
              <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
                <text x="70" y="198">1</text><text x="130" y="198">3</text>
                <text x="100" y="198">2</text><text x="250" y="198">6</text>
                <text x="310" y="198">8</text><text x="370" y="198">10</text>
                <text x="460" y="198">15</text><text x="550" y="198">18</text>
              </g>
              <line x1="70" y1="74" x2="130" y2="74" stroke="var(--accent)" stroke-width="4"/>
              <text x="145" y="78" fill="var(--accent)" font-size="12">[1, 3]</text>
              <line x1="100" y1="100" x2="250" y2="100" stroke="var(--accent)" stroke-width="4"/>
              <text x="265" y="104" fill="var(--accent)" font-size="12">[2, 6]　與上一段重疊（2 ≤ 3）</text>
              <line x1="310" y1="126" x2="370" y2="126" stroke="var(--gold)" stroke-width="4"/>
              <text x="385" y="130" fill="var(--gold)" font-size="12">[8, 10]　不重疊（8 &gt; 6）</text>
              <line x1="460" y1="152" x2="550" y2="152" stroke="var(--gold)" stroke-width="4"/>
              <text x="565" y="156" fill="var(--gold)" font-size="12">[15, 18]</text>
            </g>
            <g>
              <line x1="70" y1="232" x2="250" y2="232" stroke="#ff8a65" stroke-width="5"/>
              <line x1="310" y1="232" x2="370" y2="232" stroke="#ff8a65" stroke-width="5"/>
              <line x1="460" y1="232" x2="550" y2="232" stroke="#ff8a65" stroke-width="5"/>
              <text x="20" y="236" fill="#ff8a65" font-size="12">結果</text>
            </g>
            <text x="20" y="268" fill="var(--gold)" font-size="12">[[1,6], [8,10], [15,18]]</text>
            <text x="20" y="294" fill="var(--text-muted)" font-size="12">排序保證了：新區間的起點 ≥ 所有已處理區間的起點，所以只要看最後一段。</text>'''

emit({
 "num": 56, "slug": "merge-intervals",
 "en": [
   "Given an array of <code>intervals</code> where "
   "<code>intervals[i] = [start_i, end_i]</code>, merge all overlapping intervals, and return "
   "<em>an array of the non-overlapping intervals that cover all the intervals in the "
   "input</em>.",
 ],
 "zh": [
   "給你一個區間陣列 <code>intervals</code>，其中 <code>intervals[i] = [startᵢ, endᵢ]</code>。"
   "請把所有<strong>重疊的區間合併</strong>，回傳一個不重疊的區間陣列，"
   "而且它要剛好覆蓋輸入的所有區間。",
 ],
 "pre": [
   ("note", "排序是這題的全部", [
     ("c", """不排序的話，你必須拿每個區間和「所有其他區間」比較 -> O(n²)，
而且合併之後還要重新檢查（合併可能製造出新的重疊）。

依「起點」排序之後，一個關鍵性質成立：

    處理到第 i 個區間時，它的起點 >= 前面所有區間的起點。
    所以它只可能和「目前結果裡的最後一段」重疊 ——
    不可能和更早的段重疊（那些段的結束更早，或已經被合併進去了）。

    => 只要和 out[-1] 比較就夠了，O(n)。

重疊的判斷：
    上一段 [a, b]，這一段 [c, d]，而且 c >= a（排序保證）

    重疊  <=>  c <= b
    不重疊 <=>  c > b

    合併後變成 [a, max(b, d)]
    （d 不一定比 b 大！[1,10] 和 [2,3] 合併後還是 [1,10]）"""),
     "<strong><code>max(b, d)</code> 的 max 不能省。</strong>"
     "包含關係（<code>[1,10]</code> 完全包住 <code>[2,3]</code>）是最常被漏掉的情況。",
   ]),
 ],
 "examples": """範例 1
  輸入：intervals = [[1,3],[2,6],[8,10],[15,18]]
  輸出：[[1,6],[8,10],[15,18]]
  說明：[1,3] 和 [2,6] 重疊，合併成 [1,6]。

範例 2
  輸入：intervals = [[1,4],[4,5]]
  輸出：[[1,5]]
  說明：端點相碰也算重疊。""",
 "constraints": [
   "1 ≤ <code>intervals.length</code> ≤ 10⁴",
   "<code>intervals[i].length == 2</code>",
   "0 ≤ <code>startᵢ</code> ≤ <code>endᵢ</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong><code>startᵢ ≤ endᵢ</code></strong> —— 保證區間是合法的（不會有 <code>[5,2]</code>）。"
       "而且<strong>可以相等</strong>（<code>[1,1]</code> 是一個「點」區間）。",
       "<strong>端點相碰算重疊</strong>：<code>[1,4]</code> 和 <code>[4,5]</code> → <code>[1,5]</code>。"
       "所以判斷式是 <code>out[-1][1] &lt; start</code>（嚴格小於才不重疊），"
       "<strong>不是 <code>&lt;=</code></strong>。"
       "（有些題目定義成開區間，那就要用 <code>&lt;=</code> —— 一定要先確認規格。）",
       "<strong>沒說輸入已排序</strong>，所以要自己排。"
       "排序 O(n log n) 就是這題的複雜度下界。",
       "<strong>n 到 10⁴</strong>，O(n log n) 完全沒問題。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P56_FIG, "0 0 640 306"),
 ],
 "approaches": [
   ap("解法一", "排序 + 一趟合併（標準解）", [
     ("c", S["p56"]),
     ("h", "三個細節"),
     ("c", """① intervals.sort(key=lambda x: x[0])
   只依「起點」排序就夠了。
   起點相同時，終點的順序不影響正確性
   （因為我們用 max 取聯集）。

   直接寫 intervals.sort() 也行（會依 [start, end] 字典序排），
   效果一樣。

② if not out or out[-1][1] < start
   not out 處理「第一個區間」。
   注意順序：先檢查 not out，Python 的短路求值保證
   不會對空 list 取 out[-1]。

③ out[-1][1] = max(out[-1][1], end)
   max 不能省！
   [[1,10], [2,3]] 排序後還是 [[1,10],[2,3]]，
   如果直接寫 out[-1][1] = end，會變成 [[1,3]] ✘"""),
     ("h", "為什麼不需要「合併後再檢查一次」？"),
     ("c", """直覺會擔心：合併 [1,3] 和 [2,6] 變成 [1,6] 之後，
會不會又和更早的某一段重疊？

不會。因為排序保證了「更早的段」起點更小，
而它們已經是「不重疊的」了 ——
    out 裡的段永遠滿足 out[i][1] < out[i+1][0]

而新來的區間起點 >= 所有已處理的起點，
所以它只可能往右延伸 out[-1]，
不可能「往回」碰到 out[-2]。

嚴格說：
    設 out = [..., A, B]，A[1] < B[0]（不重疊）
    新區間 C，C[0] >= B[0]
    若 C 和 B 合併成 B'，則 B'[0] = B[0] 不變
    所以 A[1] < B[0] = B'[0] 仍然成立 ✔

合併只會改變「右端點」，不會改變「左端點」——
這就是為什麼一趟就夠。"""),
     "<strong>複雜度由排序主導：O(n log n)。</strong>"
     "合併本身只是 O(n) 的一趟掃描。",
   ], "O(n log n)", "O(n) 或 O(log n)", "排序主導",
      "排序的空間；輸出不算", optimal=True),

   ap("解法二", "掃描線（事件排序）", [
     "更一般化的框架：<strong>把每個區間拆成「開始」和「結束」兩個事件，"
     "按位置排序後掃過去，用一個計數器記錄「目前疊了幾層」。"
     "計數器從 0 升起時是一段的開始，回到 0 時是一段的結束。</strong>",
     ("c", S["p56_sweep"]),
     ("c", """intervals = [[1,3], [2,6], [8,10]]

事件（位置, 類型）：
    (1, 開始) (2, 開始) (3, 結束) (6, 結束) (8, 開始) (10, 結束)

掃描：
    pos=1  開始  depth 0->1  記下 start=1
    pos=2  開始  depth 1->2
    pos=3  結束  depth 2->1
    pos=6  結束  depth 1->0  輸出 [1, 6] ✔
    pos=8  開始  depth 0->1  start=8
    pos=10 結束  depth 1->0  輸出 [8, 10] ✔

關鍵：事件的 tuple 是 (位置, 類型)，而「開始」用 0、「結束」用 1。
      這樣同一個位置上，「開始」會排在「結束」前面。

      為什麼重要？
      [1,4] 和 [4,5] 在位置 4 同時有「結束」和「開始」。
      如果「結束」先處理，depth 會歸零 -> 輸出 [1,4]，然後 [4,5] 另起一段 ✘
      如果「開始」先處理，depth 從 2 降到 1 -> 繼續 -> 最後輸出 [1,5] ✔

      這一個排序鍵的細節，決定了「端點相碰算不算重疊」。"""),
     "<strong>掃描線比「排序 + 合併」複雜，但它能回答更多問題</strong>：",
     ("ul", [
       "<strong>最大重疊層數</strong>（第 253 題 Meeting Rooms II：最少需要幾間會議室）"
       "—— 就是 <code>depth</code> 的最大值",
       "<strong>被覆蓋至少 k 次的區域</strong>",
       "<strong>區間的聯集總長度</strong>",
       "<strong>加權區間</strong>（每個區間帶一個值，求每個位置的總和）",
     ]),
     "<strong>「排序 + 合併」是掃描線的一個特例。</strong>"
     "先學會前者，但知道後者的存在，遇到變形題時才不會卡住。",
   ], "O(n log n)", "O(n)", "2n 個事件排序", "事件陣列"),
 ],
 "compare": (["解法", "時間", "空間", "能回答", "備註"],
   [["一、排序 + 合併", "O(n log n)", "O(log n)", "只有合併", "面試預設，最短"],
    ["二、掃描線", "O(n log n)", "O(n)", "重疊層數、覆蓋次數…", "更通用的框架"]]),
 "edges": [
   "<strong>沒有重疊</strong>：<code>[[1,2],[3,4]]</code> → 原樣。",
   "<strong>全部重疊成一段</strong>：<code>[[1,4],[2,3],[0,5]]</code> → <code>[[0,5]]</code>。",
   "<strong>包含關係</strong>：<code>[[1,4],[2,3]]</code> → <code>[[1,4]]</code>。"
   "<strong>沒有 <code>max</code> 會變成 <code>[[1,3]]</code>。</strong>",
   "<strong>端點相碰</strong>：<code>[[1,4],[4,5]]</code> → <code>[[1,5]]</code>。"
   "判斷式用 <code>&lt;=</code> 而不是 <code>&lt;</code> 會分成兩段。",
   "<strong>點區間</strong>：<code>[[1,1]]</code> → <code>[[1,1]]</code>。",
   "<strong>沒排序的輸入</strong>：<code>[[1,4],[0,4]]</code> → <code>[[0,4]]</code>。"
   "<strong>忘記排序會輸出兩段。</strong>",
   "<strong>單一區間</strong>：<code>[[1,3]]</code> → 原樣。",
   "<strong>空輸入</strong>：<code>[]</code> → <code>[]</code>。題目保證不會，但別崩潰。",
 ],
 "follow": [
   ("h", "追問一：如果要插入一個新區間到「已排序且不重疊」的陣列裡呢？"),
   "第 57 題（Insert Interval）。因為已經排序，可以 O(n) 解決 —— "
   "甚至可以用二分搜尋找到插入位置，做到 O(log n + 受影響的區間數)。"
   "詳見下一題。",
   ("h", "追問二：如果要問「最少需要幾間會議室」呢？"),
   "第 253 題。<strong>就是掃描線的 <code>depth</code> 最大值。</strong>",
   ("c", """max_depth = 0
depth = 0
for pos, kind in events:
    depth += 1 if kind == 0 else -1
    max_depth = max(max_depth, depth)

注意：這題的「端點相碰」通常「不算」重疊
（10:00 結束的會議和 10:00 開始的會議可以用同一間房），
所以排序鍵要反過來：結束事件排在開始事件前面。

同一個框架，改一個排序鍵，答案完全不同 ——
所以規格一定要先問清楚。""",),
   ("h", "追問三：如果區間會動態新增和刪除呢？"),
   "排序 + 合併不適用（每次都要重排）。"
   "要用<strong>平衡二元搜尋樹</strong>（Python 可以用 <code>sortedcontainers</code> 的 "
   "<code>SortedList</code>）維護「目前的不重疊區間集合」，"
   "每次插入時用二分搜尋找到影響範圍，合併掉被吞併的區間。"
   "這就是第 715 題（Range Module）和第 352 題（Data Stream as Disjoint Intervals）。",
   ("h", "追問四：區間問題的通用心法？"),
   ("c", """1. 幾乎都要「先排序」
       依起點排：合併、插入
       依終點排：無重疊區間的最大數量（第 435 題）、活動選擇問題

2. 想清楚「重疊」的定義
       閉區間 [a,b] 和 [c,d] 重疊  <=>  a <= d 且 c <= b
       端點相碰算不算？一定要問。

3. 掃描線是更一般的框架
       把區間拆成事件，用計數器追蹤狀態。
       能回答「合併」以外的一大票問題。

4. 依終點排序 + 貪婪 = 活動選擇
       「最多能選幾個互不重疊的區間」的標準解，
       貪婪地選「最早結束」的那一個。""",),
 ],
 "related": [
   "<strong>第 57 題 Insert Interval</strong> —— 插入單一區間",
   "<strong>第 253 題 Meeting Rooms II</strong> —— 掃描線求最大重疊",
   "<strong>第 435 題 Non-overlapping Intervals</strong> —— 依終點排序的貪婪",
   "<strong>第 452 題 Minimum Number of Arrows</strong> —— 同上",
   "<strong>第 986 題 Interval List Intersections</strong> —— 兩組區間的交集",
 ],
 "check": [
   "為什麼「依起點排序後，只要和最後一段比較」就夠了？",
   "<code>max(out[-1][1], end)</code> 的 <code>max</code> 為什麼不能省？舉一個會錯的輸入。",
   "掃描線裡「開始事件排在結束事件前面」這個設計，決定了什麼？",
   "如果題目改成「端點相碰不算重疊」，兩種解法各要改哪裡？",
 ],
})
print("P56 written")
