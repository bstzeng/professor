# -*- coding: utf-8 -*-
"""第 57–60 題。"""
import random, bisect, math
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(57)

# ==================== 57. Insert Interval ====================
S["p57_scan"] = '''class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        out = []
        s, e = newInterval
        i, n = 0, len(intervals)

        # 第 1 段：完全在新區間「左邊」的，原封不動放進去
        while i < n and intervals[i][1] < s:
            out.append(intervals[i])
            i += 1

        # 第 2 段：所有和新區間重疊的，吞併成一個大區間
        while i < n and intervals[i][0] <= e:
            s = min(s, intervals[i][0])
            e = max(e, intervals[i][1])
            i += 1
        out.append([s, e])

        # 第 3 段：完全在右邊的，原封不動放進去
        while i < n:
            out.append(intervals[i])
            i += 1

        return out'''

S["p57_bisect"] = '''import bisect

class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        starts = [x[0] for x in intervals]
        ends = [x[1] for x in intervals]
        s, e = newInterval

        # 第一個「結束 >= s」的區間 —— 從它開始可能有重疊
        lo = bisect.bisect_left(ends, s)
        # 第一個「開始 > e」的區間 —— 從它開始不可能重疊
        hi = bisect.bisect_right(starts, e)

        if lo < hi:        # 有區間要被吞併
            s = min(s, intervals[lo][0])
            e = max(e, intervals[hi - 1][1])

        return intervals[:lo] + [[s, e]] + intervals[hi:]'''

_p57 = [S.load(k) for k in ("p57_scan", "p57_bisect")]


def _p57_ref(intervals, new):
    xs = sorted([list(x) for x in intervals] + [list(new)])
    res = [xs[0]]
    for a, b in xs[1:]:
        if a <= res[-1][1]:
            res[-1][1] = max(res[-1][1], b)
        else:
            res.append([a, b])
    return res


for c, nv in [([[1, 3], [6, 9]], [2, 5]),
              ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
              ([], [5, 7]), ([[1, 5]], [2, 3]), ([[1, 5]], [6, 8]),
              ([[1, 5]], [0, 0]), ([[1, 5]], [0, 6]), ([[3, 5], [12, 15]], [6, 6])]:
    e = _p57_ref(c, nv)
    for sol in _p57:
        g = sol.insert([list(x) for x in c], list(nv))
        assert g == e, ("P57", c, nv, sol, g, e)
for _ in range(4000):
    # 產生一組「已排序且不重疊」的區間
    cur = 0
    c = []
    for _ in range(random.randint(0, 6)):
        cur += random.randint(1, 3)
        a = cur
        cur += random.randint(0, 3)
        c.append([a, cur])
        cur += random.randint(1, 2)
    a = random.randint(0, 25)
    nv = [a, a + random.randint(0, 6)]
    e = _p57_ref(c, nv)
    for sol in _p57:
        g = sol.insert([list(x) for x in c], list(nv))
        assert g == e, ("P57", c, nv, sol, g, e)
print("P57 solutions OK")

_P57_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">把原本的區間分成三段：左邊、重疊、右邊</text>
            <text x="20" y="48" fill="var(--text-muted)" font-size="12">intervals = [[1,2], [3,5], [6,7], [8,10], [12,16]]，新區間 = [4, 8]</text>
            <g>
              <line x1="40" y1="200" x2="600" y2="200" stroke="var(--text-muted)"/>
              <line x1="60" y1="90" x2="92" y2="90" stroke="var(--accent)" stroke-width="4"/>
              <text x="76" y="80" fill="var(--accent)" font-size="11" text-anchor="middle">[1,2]</text>
              <line x1="124" y1="90" x2="188" y2="90" stroke="var(--gold)" stroke-width="4"/>
              <text x="156" y="80" fill="var(--gold)" font-size="11" text-anchor="middle">[3,5]</text>
              <line x1="220" y1="90" x2="252" y2="90" stroke="var(--gold)" stroke-width="4"/>
              <text x="236" y="80" fill="var(--gold)" font-size="11" text-anchor="middle">[6,7]</text>
              <line x1="284" y1="90" x2="348" y2="90" stroke="var(--gold)" stroke-width="4"/>
              <text x="316" y="80" fill="var(--gold)" font-size="11" text-anchor="middle">[8,10]</text>
              <line x1="412" y1="90" x2="540" y2="90" stroke="var(--accent)" stroke-width="4"/>
              <text x="476" y="80" fill="var(--accent)" font-size="11" text-anchor="middle">[12,16]</text>

              <line x1="156" y1="130" x2="284" y2="130" stroke="#ff8a65" stroke-width="5"/>
              <text x="220" y="150" fill="#ff8a65" font-size="12" text-anchor="middle">新區間 [4, 8]</text>

              <rect x="110" y="70" width="252" height="76" fill="var(--gold)" opacity="0.1"/>
              <text x="236" y="178" fill="var(--gold)" font-size="11" text-anchor="middle">重疊區：[3,5]、[6,7]、[8,10]</text>
            </g>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="60" y="218">1</text><text x="92" y="218">2</text><text x="124" y="218">3</text>
              <text x="156" y="218">4</text><text x="188" y="218">5</text><text x="220" y="218">6</text>
              <text x="252" y="218">7</text><text x="284" y="218">8</text><text x="348" y="218">10</text>
              <text x="412" y="218">12</text><text x="540" y="218">16</text>
            </g>
            <text x="20" y="252" fill="var(--gold)" font-size="12">吞併後：s = min(4, 3) = 3，e = max(8, 10) = 10 → [3, 10]</text>
            <text x="20" y="276" fill="#ff8a65" font-size="12">答案：[[1,2], [3,10], [12,16]]</text>'''

emit({
 "num": 57, "slug": "insert-interval",
 "en": [
   "You are given an array of non-overlapping intervals <code>intervals</code> where "
   "<code>intervals[i] = [start_i, end_i]</code> represent the start and the end of the "
   "<code>i</code>-th interval and <code>intervals</code> is sorted in ascending order by "
   "<code>start_i</code>. You are also given an interval <code>newInterval</code>.",
   "Insert <code>newInterval</code> into <code>intervals</code> such that "
   "<code>intervals</code> is still sorted in ascending order by <code>start_i</code> and "
   "<code>intervals</code> still does not have any overlapping intervals "
   "(merge overlapping intervals if necessary).",
 ],
 "zh": [
   "給你一個<strong>已依起點排序、而且互不重疊</strong>的區間陣列 <code>intervals</code>，"
   "以及一個新區間 <code>newInterval</code>。",
   "把新區間插進去，並且讓結果<strong>仍然是「依起點排序、互不重疊」</strong>"
   "（必要時要合併重疊的區間）。",
 ],
 "pre": [
   ("note", "把原陣列切成三段", [
     ("c", """設新區間是 [s, e]。原本的區間可以分成三類：

  ① 完全在左邊： interval[1] < s
     它的結束比新區間的開始還早 -> 不重疊，原封不動

  ② 有重疊：     interval[0] <= e  且  interval[1] >= s
     要被吞併進新區間

  ③ 完全在右邊： interval[0] > e
     它的開始比新區間的結束還晚 -> 不重疊，原封不動

而因為原陣列「已排序且不重疊」，
這三類在陣列裡剛好是【連續的三段】：
    [①①①][②②②][③③③]

所以只要找出兩個分界點，就能一趟做完。

吞併的規則：
    s = min(s, 所有重疊區間的最小起點)
    e = max(e, 所有重疊區間的最大終點)"""),
     "<strong>「已排序且不重疊」這個前提，讓這題從 O(n log n) 降到 O(n)</strong> —— "
     "如果沒有這個前提，就只能套用第 56 題的做法（先加進去再全部重排合併）。",
   ]),
 ],
 "examples": """範例 1
  輸入：intervals = [[1,3],[6,9]], newInterval = [2,5]
  輸出：[[1,5],[6,9]]
  說明：[2,5] 和 [1,3] 重疊，合併成 [1,5]。

範例 2
  輸入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
  輸出：[[1,2],[3,10],[12,16]]
  說明：[4,8] 和 [3,5]、[6,7]、[8,10] 都重疊，一起合併成 [3,10]。""",
 "constraints": [
   "0 ≤ <code>intervals.length</code> ≤ 10⁴（<strong>可以是空的</strong>）",
   "<code>intervals[i].length == 2</code>",
   "0 ≤ <code>startᵢ</code> ≤ <code>endᵢ</code> ≤ 10⁵",
   "<code>intervals</code> 已依 <code>startᵢ</code> <strong>升序排列</strong>且<strong>互不重疊</strong>",
   "<code>newInterval.length == 2</code>，0 ≤ <code>start</code> ≤ <code>end</code> ≤ 10⁵",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong><code>intervals</code> 可以是空的</strong> → 答案就是 <code>[newInterval]</code>。"
       "三段式寫法自然處理（前兩個 while 都不跑，直接 append）。",
       "<strong>已排序且不重疊</strong> —— 這是 O(n) 解法的全部基礎。"
       "面試時務必確認這個前提（如果沒有，就是第 56 題）。",
       "<strong>端點相碰算重疊</strong>：<code>[[1,5]]</code> 插入 <code>[5,7]</code> → <code>[[1,7]]</code>。"
       "所以判斷式用 <code>&lt;</code> 和 <code>&lt;=</code> 而不是反過來。",
       "<strong>n 到 10⁴</strong>，O(n) 輕鬆過。二分搜尋（O(log n) 定位）是加分項而不是必需。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P57_FIG, "0 0 640 290"),
 ],
 "approaches": [
   ap("解法一", "三段式一趟掃描（標準解）", [
     ("c", S["p57_scan"]),
     ("h", "兩個 while 的條件，一個字都不能錯"),
     ("c", """第 1 段（左邊）：  intervals[i][1] < s
    「這個區間的結束，比新區間的開始還早」
    用嚴格 < ：如果 intervals[i][1] == s，端點相碰，算重疊，不能放進第 1 段。

第 2 段（重疊）：  intervals[i][0] <= e
    「這個區間的開始，不超過新區間的結束」
    用 <= ：端點相碰算重疊。

    為什麼不用同時檢查 intervals[i][1] >= s？
    因為第 1 段的 while 已經把「結束 < s」的全部消化掉了，
    所以走到第 2 段時，剩下的都保證 intervals[i][1] >= s。

    這是「三段式」的優雅之處：
    每一段的條件都靠前一段的結束來簡化。

第 3 段：  剩下全部原封不動。"""),
     ("h", "追一遍範例 2"),
     ("c", """intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]，new = [4,8]
s, e = 4, 8

第 1 段：
    i=0: [1,2] 的 2 < 4 ✔  放進 out，i=1
    i=1: [3,5] 的 5 < 4 ✘  停

第 2 段：
    i=1: [3,5] 的 3 <= 8 ✔  s=min(4,3)=3, e=max(8,5)=8，i=2
    i=2: [6,7] 的 6 <= 8 ✔  s=3, e=max(8,7)=8，i=3
    i=3: [8,10] 的 8 <= 8 ✔ s=3, e=max(8,10)=10，i=4
    i=4: [12,16] 的 12 <= 10 ✘ 停
    out.append([3, 10])

第 3 段：
    i=4: 放進 [12,16]

結果 [[1,2],[3,10],[12,16]] ✔"""),
     "<strong>注意 <code>e</code> 在第 2 段會「一邊擴大一邊被用來判斷」</strong> —— "
     "這是對的，因為吞併之後新區間變大，可能又碰到更右邊的區間。"
     "例子裡 <code>[8,10]</code> 就是靠 <code>e</code> 從 8 沒變（<code>8 &lt;= 8</code>）才被吞進來的。",
   ], "O(n)", "O(n)", "每個區間看一次", "輸出陣列", optimal=True),

   ap("解法二", "二分搜尋定位（在區間很多時更快）", [
     "既然陣列已排序，兩個分界點可以用<strong>二分搜尋</strong>找出來，"
     "而不是線性掃過去。",
     ("c", S["p57_bisect"]),
     ("c", """lo = bisect_left(ends, s)
    ends 是所有區間的「結束」，它也是遞增的（因為不重疊）。
    找「第一個 end >= s」的位置 —— 從它開始才可能重疊。

hi = bisect_right(starts, e)
    starts 是所有區間的「開始」，遞增。
    找「第一個 start > e」的位置 —— 從它開始不可能重疊。

所以 intervals[lo : hi] 就是所有和新區間重疊的區間。

if lo < hi:  表示真的有重疊
    s = min(s, intervals[lo][0])     最左邊那個的起點
    e = max(e, intervals[hi-1][1])   最右邊那個的終點

    （不用掃過中間所有的，因為已排序且不重疊，
      最小起點一定在 lo，最大終點一定在 hi-1。）

最後拼起來：
    intervals[:lo] + [[s, e]] + intervals[hi:]"""),
     ("h", "為什麼 <code>ends</code> 也是遞增的？"),
     "因為題目保證「已排序且<strong>不重疊</strong>」。"
     "不重疊表示 <code>intervals[i][1] &lt; intervals[i+1][0] ≤ intervals[i+1][1]</code>，"
     "所以 <code>ends</code> 必然也遞增 —— 才能對它做二分搜尋。"
     "<strong>如果區間可能重疊（例如 <code>[[1,10],[2,3]]</code>），"
     "<code>ends</code> 就不是遞增的，這個解法會錯。</strong>",
     ("h", "複雜度真的比較好嗎？"),
     ("c", """定位：   O(log n)
切片：   intervals[:lo] 和 intervals[hi:] 是 O(n) 的複製

所以總複雜度還是 O(n)。

真正的差別在「常數」：
    解法一：n 次迴圈（Python 層）
    解法二：兩次 bisect（C 層）+ 兩次切片（C 層的 memcpy）

在 n = 10⁴ 時，解法二通常快 5–10 倍 ——
不是因為複雜度，而是因為工作都在 C 層做。

如果輸出可以用「回傳索引範圍」而不是「新陣列」，
解法二才能真正做到 O(log n)。"""),
     "<strong>面試時：先寫解法一</strong>（它展示了對問題結構的理解），"
     "再提「因為已排序，兩個分界點可以二分搜尋」。",
   ], "O(n)（定位 O(log n)）", "O(n)", "切片主導", "輸出陣列"),
 ],
 "compare": (["解法", "定位", "總時間", "依賴「不重疊」？", "備註"],
   [["一、三段式掃描", "O(n)", "O(n)", "只依賴「已排序」", "面試預設"],
    ["二、二分搜尋", "O(log n)", "O(n)（切片）", "✔ 必須", "常數小很多"]]),
 "edges": [
   "<strong>空陣列</strong>：<code>([], [5,7])</code> → <code>[[5,7]]</code>。",
   "<strong>新區間在最前面</strong>：<code>([[1,5]], [0,0])</code> → <code>[[0,0],[1,5]]</code>。",
   "<strong>新區間在最後面</strong>：<code>([[1,5]], [6,8])</code> → <code>[[1,5],[6,8]]</code>。",
   "<strong>新區間被完全包含</strong>：<code>([[1,5]], [2,3])</code> → <code>[[1,5]]</code>。"
   "<code>min</code> 和 <code>max</code> 都不能省。",
   "<strong>新區間包含所有</strong>：<code>([[1,2],[3,4]], [0,10])</code> → <code>[[0,10]]</code>。",
   "<strong>端點相碰</strong>：<code>([[1,5]], [5,7])</code> → <code>[[1,7]]</code>；"
   "<code>([[3,5],[12,15]], [6,6])</code> → <code>[[3,5],[6,6],[12,15]]</code>。",
   "<strong>點區間插在縫隙</strong>：驗證「不重疊」時不會被誤吞。",
 ],
 "follow": [
   ("h", "追問一：如果要插入很多個區間呢？"),
   "一個一個插是 O(k · n)。"
   "<strong>更好的做法：把 k 個新區間全部加進去，再套第 56 題的「排序 + 合併」</strong>，"
   "O((n+k) log(n+k))。"
   "當 <code>k</code> 接近 <code>n</code> 時後者明顯更好。",
   ("h", "追問二：如果是「刪除一個區間」呢？"),
   "第 1272 題（Remove Interval）。結構很像，也是三段式，"
   "但重疊的部分要「切掉中間」而不是「合併」：",
   ("c", """對每個重疊的區間 [a, b] 和要刪除的 [s, e]：
    左邊殘留： [a, s]  若 a < s
    右邊殘留： [e, b]  若 e < b

一個區間可能被切成兩段（當 [s,e] 完全在 [a,b] 內部時）。

刪除比插入麻煩，因為區間數量可能「變多」。""",),
   ("h", "追問三：如果要支援「動態插入 + 查詢某點是否被覆蓋」呢？"),
   "第 715 題（Range Module）。"
   "用 <strong>平衡二元搜尋樹</strong>（Python 的 <code>sortedcontainers.SortedList</code>）"
   "維護不重疊的區間集合，每次操作 O(log n + 受影響的區間數)。"
   "或者用<strong>線段樹 + 座標壓縮</strong>。",
   ("h", "追問四：這題的「三段式」在哪裡還會出現？"),
   "任何「有序資料 + 一個範圍操作」的問題：",
   ("ul", [
     "<strong>陣列的區間刪除／替換</strong>（<code>list[a:b] = [...]</code> 就是三段式）",
     "<strong>版本控制的 diff / patch</strong>：未變、變更、未變",
     "<strong>資料庫的範圍更新</strong>",
     "<strong>文字編輯器的區塊選取與替換</strong>",
   ]),
   "<strong>「把序列切成『不受影響的前段 + 受影響的中段 + 不受影響的後段』」"
   "是處理有序資料的通用模式。</strong>",
 ],
 "related": [
   "<strong>第 56 題 Merge Intervals</strong> —— 沒有「已排序」前提的版本",
   "<strong>第 1272 題 Remove Interval</strong> —— 刪除版",
   "<strong>第 715 題 Range Module</strong> —— 動態版",
   "<strong>第 986 題 Interval List Intersections</strong> —— 兩組有序區間的交集",
 ],
 "check": [
   "第 1 段的條件為什麼用 <code>&lt;</code> 而第 2 段用 <code>&lt;=</code>？",
   "第 2 段為什麼不需要檢查 <code>intervals[i][1] &gt;= s</code>？",
   "二分搜尋版為什麼需要「不重疊」這個前提？只有「已排序」夠嗎？",
   "<code>([[1,5]], [2,3])</code> 的答案是什麼？哪個 <code>min</code> / <code>max</code> 在這裡起作用？",
 ],
})
print("P57 written")

# ==================== 58. Length of Last Word ====================
S["p58_split"] = '''class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() 不帶參數時，會自動忽略所有連續空白與首尾空白
        return len(s.split()[-1])'''

S["p58_scan"] = '''class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        # 先跳過結尾的空白
        while i >= 0 and s[i] == " ":
            i -= 1

        # 再往左數字母，數到空白或開頭為止
        length = 0
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length'''

S["p58_rstrip"] = '''class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()                  # 去掉結尾空白
        return len(s) - s.rfind(" ") - 1    # 找不到時 rfind 回 -1，剛好是整串長度'''

_p58 = [S.load(k) for k in ("p58_split", "p58_scan", "p58_rstrip")]
for s_ in ["Hello World", "   fly me   to   the moon  ",
           "luffy is still joyboy", "a", "a ", " a", "day"]:
    e = len(s_.split()[-1])
    for sol in _p58:
        assert sol.lengthOfLastWord(s_) == e, ("P58", repr(s_), sol, sol.lengthOfLastWord(s_), e)
for _ in range(5000):
    parts = []
    for _ in range(random.randint(1, 4)):
        parts.append("".join(random.choice("ab") for _ in range(random.randint(1, 4))))
    s_ = (" " * random.randint(0, 3)) + \
         (" " * random.randint(1, 3)).join(parts) + (" " * random.randint(0, 3))
    e = len(s_.split()[-1])
    for sol in _p58:
        assert sol.lengthOfLastWord(s_) == e, ("P58", repr(s_), sol)
print("P58 solutions OK")

emit({
 "num": 58, "slug": "length-of-last-word",
 "en": [
   "Given a string <code>s</code> consisting of words and spaces, return <em>the length of "
   "the <strong>last</strong> word in the string</em>.",
   "A <strong>word</strong> is a maximal substring consisting of non-space characters only.",
 ],
 "zh": [
   "給你一個由<strong>單字</strong>和<strong>空白</strong>組成的字串 <code>s</code>，"
   "回傳<strong>最後一個單字</strong>的長度。",
   "<strong>單字</strong>指的是連續的非空白字元組成的最長子字串。",
 ],
 "pre": [
   ("note", "唯一的陷阱：結尾的空白", [
     ("c", """s = "Hello World  "

  天真的做法：從最後一個字元往前數
      最後一個字元是空白 -> 數出 0  ✘

  正確答案是 5（"World"）

所以流程一定是兩步：
    1. 先跳過「結尾的空白」
    2. 再往左數字母

除此之外，這題沒有別的難度。
它在 LeetCode 上的意義比較像是「確認你會處理邊界」。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "Hello World"
  輸出：5

範例 2
  輸入：s = "   fly me   to   the moon  "
  輸出：4
  說明：最後一個單字是 "moon"。

範例 3
  輸入：s = "luffy is still joyboy"
  輸出：6""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁴",
   "<code>s</code> 只含英文字母和空白 <code>' '</code>",
   "<code>s</code> 裡<strong>至少有一個單字</strong>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>保證至少有一個單字</strong> —— 所以不用處理「全是空白」的情況，"
       "<code>s.split()[-1]</code> 不會 IndexError。"
       "（但寫成能處理比較安全。）",
       "<strong>只有半形空格</strong>，沒有 tab 或換行。"
       "所以 <code>s[i] == \" \"</code> 的判斷是精確的。",
       "<strong>可能有連續空白、開頭空白、結尾空白</strong> —— 三種都要能處理。",
     ]),
   ]),
 ],
 "idea": [
   "三種寫法都是 O(n)，但<strong>從後往前掃的版本實際上是 O(最後一個單字的長度 + 結尾空白數)</strong>，"
   "通常遠小於 n。",
 ],
 "approaches": [
   ap("解法一", "從後往前掃（最推薦）", [
     ("c", S["p58_scan"]),
     "兩個 while 對應兩個步驟，語意非常清楚。",
     "<strong>複雜度其實優於 O(n)</strong>："
     "它只會碰到「結尾的空白 + 最後一個單字」這些字元，"
     "前面的內容完全不看。"
     "對一個 10⁴ 字元、最後一個單字只有 3 個字母的輸入，它只跑幾步。",
     "<strong>而且 O(1) 空間</strong> —— 不建任何新字串。",
     ("h", "兩個 while 的邊界 <code>i &gt;= 0</code>"),
     "第一個 while 的 <code>i &gt;= 0</code> 防的是「全是空白」"
     "（題目保證不會，但別讓程式炸掉）。"
     "第二個 while 的 <code>i &gt;= 0</code> 防的是「整個字串只有一個單字」"
     "（例如 <code>\"day\"</code>，會一路數到索引 −1 之前停下）。",
   ], "O(結尾空白 + 最後單字長)", "O(1)", "通常遠小於 n", "只用兩個變數", optimal=True),

   ap("解法二", "<code>split()</code>（最短）", [
     ("c", S["p58_split"]),
     ("h", "<code>split()</code> 不帶參數 vs 帶參數，差很多"),
     ("c", """s = "  a  b  "

s.split()       -> ['a', 'b']
    不帶參數時：
      - 以「任意連續空白」為分隔
      - 自動忽略首尾的空白
      - 不會產生空字串

s.split(" ")    -> ['', '', 'a', '', 'b', '', '']
    帶參數時：
      - 嚴格以「單一個空格」為分隔
      - 連續空白會產生空字串
      - 首尾空白也會產生空字串

所以這題一定要用 s.split()（不帶參數）。
寫成 s.split(" ")[-1] 會在 "Hello World  " 上回傳 0 ✘

這是 Python 字串處理最常見的一個坑。"""),
     "<strong>缺點</strong>：它把整個字串切成一個 list，"
     "空間是 O(n)，而且一定要掃完整個字串。"
     "對這題（n ≤ 10⁴）完全無所謂，但在「只要最後一個單字」的場景下是浪費。",
     "<strong>實務上就寫這一行</strong>。面試時可以先寫它，再說「如果要 O(1) 空間，可以從後往前掃」。",
   ], "O(n)", "O(n)", "切出整個 list", "list 本身"),

   ap("解法三", "<code>rstrip</code> + <code>rfind</code>", [
     ("c", S["p58_rstrip"]),
     ("c", """s = "Hello World  "

s.rstrip()        -> "Hello World"    長度 11
s.rfind(" ")      -> 5                最後一個空格的位置
11 - 5 - 1 = 5 ✔

s = "day"（沒有空格）

s.rstrip()        -> "day"            長度 3
s.rfind(" ")      -> -1               找不到
3 - (-1) - 1 = 3 ✔

「找不到回 -1」這個慣例，在這裡剛好讓公式統一 ——
不用寫 if。這種「讓邊界自然落在公式裡」的設計很值得學。"""),
     "<strong>介於解法一和二之間</strong>：比 <code>split</code> 省記憶體"
     "（<code>rstrip</code> 還是會建一個新字串，但只有一份），"
     "比手寫掃描短。",
   ], "O(n)", "O(n)", "rstrip 建新字串", "一份字串複本"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、從後往前掃", "O(尾端)", "O(1)", "10", "最優，面試預設"],
    ["二、split()", "O(n)", "O(n)", "1", "最短，實務首選"],
    ["三、rstrip + rfind", "O(n)", "O(n)", "2", "公式統一，不用 if"]]),
 "edges": [
   "<strong>結尾有空白</strong>：<code>\"Hello World  \"</code> → 5。<strong>本題的核心陷阱。</strong>",
   "<strong>開頭有空白</strong>：<code>\" a\"</code> → 1。",
   "<strong>連續空白</strong>：<code>\"   fly me   to   the moon  \"</code> → 4。",
   "<strong>只有一個單字</strong>：<code>\"day\"</code> → 3。掃描版會數到 <code>i == -1</code>。",
   "<strong>只有一個字元</strong>：<code>\"a\"</code> → 1；<code>\"a \"</code> → 1。",
   "<strong>用 <code>split(\" \")</code> 的錯誤</strong>："
   "<code>\"Hello World  \"</code> 會回傳 0（最後一個元素是空字串）。",
 ],
 "follow": [
   ("h", "追問一：如果要回傳「第 k 個單字」的長度呢？"),
   "從後往前掃的優勢就消失了（可能要掃到開頭）。"
   "這時 <code>split()</code> 反而是最好的選擇，或者用一個計數器邊掃邊數單字。",
   ("h", "追問二：如果分隔符不只是空格（tab、換行、全形空白）呢？"),
   "手寫掃描要改成 <code>s[i].isspace()</code>，"
   "或者定義一個明確的分隔字元集合。"
   "<strong><code>split()</code>（不帶參數）已經處理了所有 Unicode 空白</strong>，"
   "這是它的優勢。",
   "<strong>但要注意</strong>：<code>str.isspace()</code> 對全形空白 <code>'\\u3000'</code> "
   "也回傳 True —— 這通常是你要的，但如果規格明確只說「半形空格」，就會不符。"
   "<strong>「哪些字元算空白」永遠應該由規格決定，不是由語言的預設值決定。</strong>",
   ("h", "追問三：為什麼「從後往前」在這題特別划算？"),
   "因為我們只要「最後一個單字」—— "
   "<strong>需要的資訊全部集中在字串的尾端。</strong>"
   "從前往後掃會讀完整個字串，只為了拿到最後那幾個字元。",
   "<strong>這是一個很通用的判斷</strong>：問自己「答案依賴哪一部分的資料？」"
   "然後只去讀那一部分。"
   "同樣的想法出現在：從後往前的字串比對（Boyer-Moore）、"
   "從尾端讀取日誌檔（<code>tail</code>）、"
   "以及本題。",
 ],
 "related": [
   "<strong>第 151 題 Reverse Words in a String</strong> —— 同樣要處理多餘空白",
   "<strong>第 557 題 Reverse Words in a String III</strong> —— 逐字反轉",
   "<strong>第 8 題 String to Integer (atoi)</strong> —— 另一個「空白處理」的規格題",
 ],
 "check": [
   "<code>\"Hello World  \"</code> 用 <code>s.split(\" \")[-1]</code> 會得到什麼？為什麼？",
   "<code>s.split()</code> 和 <code>s.split(\" \")</code> 的三個差別是什麼？",
   "解法三為什麼不需要處理「沒有空格」的情況？<code>rfind</code> 回 −1 剛好帶來什麼？",
   "從後往前掃的實際複雜度是多少？什麼時候它會比 O(n) 好很多？",
 ],
})
print("P58 written")
