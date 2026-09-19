# -*- coding: utf-8 -*-
"""第 42–44 題。"""
import random, functools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(42)

# ==================== 42. Trapping Rain Water ====================
S["p42_brute"] = '''class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        for i in range(n):
            # 這一格能積多少水 = min(左邊最高, 右邊最高) - 自己的高度
            left_max = max(height[:i + 1])
            right_max = max(height[i:])
            total += min(left_max, right_max) - height[i]
        return total'''

S["p42_prefix"] = '''class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        # 預先算好每一格的「左邊最高」和「右邊最高」
        left = [0] * n
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        right = [0] * n
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        return sum(min(left[i], right[i]) - height[i] for i in range(n))'''

S["p42_two"] = '''class Solution:
    def trap(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        left_max = right_max = 0
        total = 0

        while lo < hi:
            # 處理「比較矮」的那一邊：它的水位由那一邊的 max 決定
            if height[lo] < height[hi]:
                left_max = max(left_max, height[lo])
                total += left_max - height[lo]
                lo += 1
            else:
                right_max = max(right_max, height[hi])
                total += right_max - height[hi]
                hi -= 1

        return total'''

S["p42_stack"] = '''class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []        # 存索引，對應的高度由高到低（單調遞減堆疊）
        total = 0

        for i, h in enumerate(height):
            # 當前柱子比堆疊頂端高 -> 形成一個「凹槽」
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()        # 凹槽的底
                if not stack:
                    break                   # 左邊沒有牆，接不到水
                left = stack[-1]            # 左邊的牆
                width = i - left - 1
                depth = min(height[left], h) - height[bottom]
                total += width * depth
            stack.append(i)

        return total'''

_p42 = [S.load(k) for k in ("p42_brute", "p42_prefix", "p42_two", "p42_stack")]
for c in [[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], [4, 2, 0, 3, 2, 5], [],
          [1], [1, 2], [2, 1], [3, 0, 3], [5, 5, 5], [0, 0, 0]]:
    e = _p42[0].trap(list(c)) if c else 0
    for sol in _p42:
        assert sol.trap(list(c)) == e, ("P42", c, sol, sol.trap(list(c)), e)
assert _p42[1].trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert _p42[1].trap([4, 2, 0, 3, 2, 5]) == 9
for _ in range(5000):
    c = [random.randint(0, 6) for _ in range(random.randint(0, 12))]
    e = _p42[0].trap(list(c)) if c else 0
    for sol in _p42:
        assert sol.trap(list(c)) == e, ("P42", c, sol, sol.trap(list(c)), e)
print("P42 solutions OK")

_P42_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">height = [0,1,0,2,1,0,1,3,2,1,2,1]，總共接 6 單位的水</text>
            <g>
              <rect x="86" y="170" width="38" height="24" fill="var(--text-muted)" opacity="0.65"/>
              <rect x="170" y="146" width="38" height="48" fill="var(--text-muted)" opacity="0.65"/>
              <rect x="212" y="170" width="38" height="24" fill="var(--text-muted)" opacity="0.65"/>
              <rect x="296" y="170" width="38" height="24" fill="var(--text-muted)" opacity="0.65"/>
              <rect x="338" y="122" width="38" height="72" fill="var(--text-muted)" opacity="0.65"/>
              <rect x="380" y="146" width="38" height="48" fill="var(--text-muted)" opacity="0.65"/>
              <rect x="422" y="170" width="38" height="24" fill="var(--text-muted)" opacity="0.65"/>
              <rect x="464" y="146" width="38" height="48" fill="var(--text-muted)" opacity="0.65"/>
              <rect x="506" y="170" width="38" height="24" fill="var(--text-muted)" opacity="0.65"/>
              <rect x="128" y="170" width="38" height="24" fill="var(--accent)" opacity="0.4"/>
              <rect x="212" y="146" width="38" height="24" fill="var(--accent)" opacity="0.4"/>
              <rect x="254" y="146" width="38" height="48" fill="var(--accent)" opacity="0.4"/>
              <rect x="296" y="146" width="38" height="24" fill="var(--accent)" opacity="0.4"/>
              <rect x="422" y="146" width="38" height="24" fill="var(--accent)" opacity="0.4"/>
              <line x1="40" y1="194" x2="600" y2="194" stroke="var(--text-muted)"/>
            </g>
            <g font-size="10" fill="var(--text-muted)" text-anchor="middle">
              <text x="63" y="210">0</text><text x="105" y="210">1</text><text x="147" y="210">0</text>
              <text x="189" y="210">2</text><text x="231" y="210">1</text><text x="273" y="210">0</text>
              <text x="315" y="210">1</text><text x="357" y="210">3</text><text x="399" y="210">2</text>
              <text x="441" y="210">1</text><text x="483" y="210">2</text><text x="525" y="210">1</text>
            </g>
            <text x="270" y="118" fill="var(--accent)" font-size="12" text-anchor="middle">藍色 = 積水</text>
            <text x="20" y="242" fill="var(--gold)" font-size="12">每一格的水位 = min(左邊最高, 右邊最高)　水量 = 水位 − 自己的高度（不能是負的）</text>
            <text x="20" y="266" fill="var(--text-muted)" font-size="12">索引 5（高度 0）：左邊最高 2、右邊最高 3 → 水位 min(2,3) = 2 → 積水 2 − 0 = 2</text>
            <text x="20" y="288" fill="var(--text-muted)" font-size="12">索引 7（高度 3）：水位 3 → 積水 0（它自己就是最高的牆）</text>'''

emit({
 "num": 42, "slug": "trapping-rain-water",
 "en": [
   "Given <code>n</code> non-negative integers representing an elevation map where the width "
   "of each bar is <code>1</code>, compute how much water it can trap after raining.",
 ],
 "zh": [
   "給你 <code>n</code> 個非負整數，代表一張<strong>高度圖</strong>，每根柱子的寬度都是 1。"
   "計算下雨之後這張圖能接住多少水。",
 ],
 "pre": [
   ("note", "唯一需要的公式：逐格計算", [
     ("c", """第 i 格能積多少水？

    水位 = min(左邊最高的柱子, 右邊最高的柱子)
    水量 = max(0, 水位 - height[i])

為什麼是 min？
    水會從「比較矮的那一邊」溢出去。
    左牆 2、右牆 3 -> 水最多只能積到高度 2。

為什麼要 max(0, ...)？
    如果 height[i] 自己就是最高的牆，
    min(左, 右) 會等於 height[i]，差是 0。
    （不會是負的，因為「左邊最高」的定義包含 i 自己。）

    注意這個定義很重要：left_max[i] 是 max(height[0..i])，「含 i」。
    如果定義成「不含 i」，就要真的用 max(0, ...) 夾住。

把每一格的水量加起來就是答案。
四種解法的差別只在「怎麼算出每一格的左右最大值」。"""),
     "<strong>「逐格計算」（column by column）是關鍵的視角切換。</strong>"
     "很多人第一次看到這題會想「找出所有的凹槽」—— 那很難定義，"
     "因為凹槽可以巢狀、可以相連。<strong>但「每一格積多少水」是完全獨立的。</strong>",
   ]),
 ],
 "examples": """範例 1
  輸入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
  輸出：6

範例 2
  輸入：height = [4,2,0,3,2,5]
  輸出：9
  說明：
    索引 1 (高 2)：min(4, 5) - 2 = 2
    索引 2 (高 0)：min(4, 5) - 0 = 4
    索引 3 (高 3)：min(4, 5) - 3 = 1
    索引 4 (高 2)：min(4, 5) - 2 = 2
    合計 9""",
 "constraints": [
   "<code>n == height.length</code>",
   "1 ≤ <code>n</code> ≤ 2 × 10⁴",
   "0 ≤ <code>height[i]</code> ≤ 10⁵",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n 到 2 × 10⁴</strong>。O(n²) 是 4 × 10⁸ —— 在 Python 裡會 TLE。"
       "所以要 O(n)。",
       "<strong>高度可以是 0</strong>，而且很常見（那是積水最深的地方）。",
       "<strong>沒有要求 O(1) 空間</strong>，所以前後綴陣列（解法二）完全合法。"
       "但雙指標（解法三）能做到 O(1)，是加分項。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P42_FIG, "0 0 640 300"),
   ("t", ["解法", "怎麼取得左右最大值", "時間", "空間"],
     [["一、暴力", "每格都重新掃一遍", "O(n²)", "O(1)"],
      ["二、前後綴陣列", "預先算好兩個陣列", "O(n)", "O(n)"],
      ["三、雙指標", "邊走邊維護，只處理矮的那邊", "O(n)", "O(1)"],
      ["四、單調堆疊", "橫著一層一層算", "O(n)", "O(n)"]]),
 ],
 "approaches": [
   ap("解法一", "暴力：每格都重新找左右最大值", [
     ("c", S["p42_brute"]),
     "直接把公式翻成程式碼。正確，但每一格都要掃兩次整個陣列 —— O(n²)。",
     "<strong>它的價值是把公式講清楚</strong>，而且是後面三個解法的正確性基準。",
     "<code>height[:i+1]</code> 包含 i 自己，"
     "<code>height[i:]</code> 也包含 i 自己 —— "
     "這保證了 <code>min(left, right) &gt;= height[i]</code>，差永遠非負。",
   ], "O(n²)", "O(n)", "每格掃兩遍", "切片產生的暫時陣列"),

   ap("解法二", "前後綴最大值陣列（最好懂的 O(n)）", [
     "暴力法的浪費：<code>left_max[i]</code> 和 <code>left_max[i-1]</code> 只差一個元素，"
     "卻重算了一遍。用遞推一次算完。",
     ("c", S["p42_prefix"]),
     ("c", """height = [0,1,0,2,1,0,1,3,2,1,2,1]

left   = [0,1,1,2,2,2,2,3,3,3,3,3]     從左往右取 max
right  = [3,3,3,3,3,3,3,3,2,2,2,1]     從右往左取 max
min    = [0,1,1,2,2,2,2,3,2,2,2,1]
height = [0,1,0,2,1,0,1,3,2,1,2,1]
水量    = [0,0,1,0,1,2,1,0,0,1,0,0]     min - height

總和 = 1 + 1 + 2 + 1 + 1 = 6 ✔"""),
     "<strong>「前綴最大值 / 後綴最大值」是一個極常用的預處理模式</strong>。"
     "任何「每個位置都需要知道左邊（或右邊）某個聚合值」的問題都適用 —— "
     "最大值、最小值、總和、乘積都一樣。",
     "三次掃描、兩個輔助陣列，思路完全直白。<strong>面試時這個解法就夠了。</strong>",
   ], "O(n)", "O(n)", "掃三遍", "兩個長度 n 的陣列"),

   ap("解法三", "雙指標（O(1) 空間）", [
     "核心洞察：<strong>如果我們知道「左邊最高」比「右邊最高」小，"
     "那這一格的水位就由左邊決定 —— 右邊到底多高根本不重要。</strong>",
     ("c", S["p42_two"]),
     ("h", "為什麼這樣是對的？"),
     ("c", """設當前 lo 和 hi，已經掃過的部分讓我們知道：
    left_max  = max(height[0..lo])
    right_max = max(height[hi..n-1])

情況：height[lo] < height[hi]

    我們要算 lo 這一格的水位 = min(真正的左最大, 真正的右最大)

    「真正的左最大」就是 left_max（左邊已經全掃過了）✔

    「真正的右最大」是 max(height[lo+1..n-1])，我們還不知道全部，
    但我們知道它 >= height[hi] > height[lo]

    而 left_max 呢？left_max 是 max(height[0..lo])。
    這裡的關鍵：left_max 也 >= height[lo]。

    要證明 min(左最大, 右最大) == left_max，
    只要證明 left_max <= 右最大。

    分兩種情況：
      - 若 left_max <= height[lo]：那 left_max == height[lo] < height[hi] <= 右最大 ✔
      - 若 left_max > height[lo]：left_max 是某根在 lo 左邊的柱子…

    比較乾淨的論證方式是換個角度：
      我們只在 height[lo] < height[hi] 時處理 lo。
      這保證了「右邊至少有一根高度 height[hi] 的柱子」，
      而水位是 min(left_max, 右最大)。

      若 left_max <= height[hi]，則因為 右最大 >= height[hi] >= left_max，
      得 min = left_max ✔

      若 left_max > height[hi]，那麼 height[lo] < height[hi] < left_max，
      表示 lo 左邊有一根比 height[hi] 還高的柱子。
      此時 min(left_max, 右最大) 可能小於 left_max…

      但這種情況不會發生！因為如果 left_max > height[hi]，
      那在更早的某一輪，我們會走 else 分支去處理 hi 那一邊，
      而不是走到這裡。

      更精確地說，演算法維持一個不變量：
          每一步只處理「兩端中較矮的那一根」，
          而較矮那一根的水位一定由「它自己那一側的 max」決定。

結論：只處理矮的那一邊，永遠不會算錯。"""),
     "<strong>這個「只處理矮的那一邊」的直覺，和第 11 題（盛最多水的容器）一模一樣</strong> —— "
     "雖然兩題問的東西完全不同。<strong>「瓶頸在矮的那邊」是柱狀圖問題的共同結構。</strong>",
     "<strong>優點</strong>：O(1) 空間、一趟掃完。"
     "<strong>缺點</strong>：正確性最不直觀，面試時要能講清楚，不然像在背。",
   ], "O(n)", "O(1)", "兩個指標合計走 n 步", "只用幾個變數", optimal=True),

   ap("解法四", "單調堆疊（橫著算）", [
     "前面三個解法都是「<strong>直著算</strong>」—— 一次算完一整欄的水。"
     "單調堆疊是「<strong>橫著算</strong>」—— 一次算完一整層的水。",
     ("c", S["p42_stack"]),
     ("c", """堆疊裡存索引，對應的高度是「單調遞減」的。

遇到一根「比堆疊頂端高」的柱子時，就形成了一個凹槽：

      左牆        底        右牆
    height[left]  height[bottom]  h
         |                          |
         |____________     _________|
                      |   |
                    凹槽（積水）

    寬 = i - left - 1          （不含兩道牆）
    深 = min(左牆, 右牆) - 底
    水量 = 寬 × 深

height = [4, 2, 0, 3, 2, 5]

  i=0 h=4: 堆疊空 -> push  stack=[0]
  i=1 h=2: 2 < 4，不彈 -> push  stack=[0,1]
  i=2 h=0: 0 < 2 -> push  stack=[0,1,2]
  i=3 h=3: 3 > height[2]=0
      pop bottom=2（高 0），left=1（高 2）
      寬 = 3-1-1 = 1，深 = min(2,3)-0 = 2  -> +2
      3 > height[1]=2
      pop bottom=1（高 2），left=0（高 4）
      寬 = 3-0-1 = 2，深 = min(4,3)-2 = 1  -> +2
      3 < 4，停 -> push  stack=[0,3]   小計 4
  i=4 h=2: 2 < 3 -> push  stack=[0,3,4]
  i=5 h=5: 5 > height[4]=2
      pop bottom=4（高 2），left=3（高 3）
      寬 = 5-3-1 = 1，深 = min(3,5)-2 = 1  -> +1
      5 > height[3]=3
      pop bottom=3（高 3），left=0（高 4）
      寬 = 5-0-1 = 4，深 = min(4,5)-3 = 1  -> +4
      堆疊剩 [0]，5 > 4
      pop bottom=0，堆疊空 -> break（左邊沒牆）
      push  stack=[5]

  總計 4 + 1 + 4 = 9 ✔"""),
     "<strong><code>if not stack: break</code> 不能省</strong>："
     "彈出底之後如果堆疊空了，表示左邊沒有牆，水會流走。",
     "<strong>單調堆疊的通用意義</strong>：它在回答"
     "「<strong>對每個元素，左邊／右邊第一個比它大（或小）的是誰</strong>」。"
     "認出這個模式之後，第 84、85、496、503、739 題都會變簡單。"
     "<strong>但對這一題，它是四個解法裡最複雜的一個 —— 除非面試官指定，否則不建議寫。</strong>",
   ], "O(n)", "O(n)", "每個索引 push/pop 各一次", "堆疊最壞有 n 個元素"),
 ],
 "compare": (["解法", "時間", "空間", "算的方向", "面試推薦度"],
   [["一、暴力", "O(n²)", "O(1)", "直", "只當基準"],
    ["二、前後綴陣列", "O(n)", "O(n)", "直", "★★★★★ 最好講"],
    ["三、雙指標", "O(n)", "O(1)", "直", "★★★★☆ 最優，但要會證明"],
    ["四、單調堆疊", "O(n)", "O(n)", "橫", "★★☆☆☆ 為第 84 題鋪路"]]),
 "edges": [
   "<strong>空陣列或單一元素</strong>：<code>[]</code>、<code>[1]</code> → 0。",
   "<strong>兩根柱子</strong>：<code>[1,2]</code>、<code>[2,1]</code> → 0。中間沒有格子。",
   "<strong>遞增</strong>：<code>[1,2,3,4]</code> → 0。水全部流走。",
   "<strong>遞減</strong>：<code>[4,3,2,1]</code> → 0。",
   "<strong>全部一樣高</strong>：<code>[5,5,5]</code> → 0。",
   "<strong>全部是 0</strong>：<code>[0,0,0]</code> → 0。",
   "<strong>最簡單的凹槽</strong>：<code>[3,0,3]</code> → 3。",
   "<strong>巢狀凹槽</strong>：<code>[4,2,0,3,2,5]</code> → 9。"
   "單調堆疊在這裡會連續彈出多層，最能驗證實作。",
 ],
 "follow": [
   ("h", "追問一：這題和第 11 題（盛最多水的容器）差在哪？"),
   ("c", """第 11 題                       第 42 題（本題）
--------------------          --------------------
只選「兩根」當牆                所有柱子都參與
中間的柱子被忽略                中間的柱子會佔掉體積
求「最大的一個矩形」             求「總積水量」
答案是 max                     答案是 sum

雖然都用雙指標、都在柱狀圖上，問的東西完全不同。

共同點：兩題的雙指標都是「處理矮的那一邊」，
因為兩題的瓶頸都在矮的那一側。""",),
   ("h", "追問二：二維版本呢？"),
   "第 407 題（Trapping Rain Water II）。"
   "二維的「左右最大值」變成「從邊界往內的最小屏障高度」，"
   "沒辦法用簡單的前後綴。"
   "<strong>標準解法是用最小堆從邊界往內做 BFS</strong>："
   "每次從堆裡取出最矮的邊界格，向內擴展，"
   "內部格子的水位 = max(自己的高度, 當前邊界的高度)。"
   "這其實是 Dijkstra 的變形。",
   ("h", "追問三：如果柱子的寬度不是 1 呢？"),
   "水量公式變成 <code>寬度 × (水位 − 高度)</code>，其餘邏輯完全不變。"
   "前後綴陣列和雙指標都能直接推廣。",
   ("h", "追問四：如果要回答「哪幾格積了水」而不只是總量？"),
   "前後綴陣列版最方便 —— 它本來就逐格算出了每一格的水量。"
   "雙指標版也可以（處理每一格時記錄下來）。"
   "<strong>單調堆疊版最不方便</strong>，因為它是橫著算的，"
   "一次的計算跨越多個格子。",
 ],
 "related": [
   "<strong>第 11 題 Container With Most Water</strong> —— 同一張圖，不同的問題",
   "<strong>第 84 題 Largest Rectangle in Histogram</strong> —— 單調堆疊的經典",
   "<strong>第 85 題 Maximal Rectangle</strong> —— 第 84 題的二維版",
   "<strong>第 407 題 Trapping Rain Water II</strong> —— 二維版，要用最小堆",
   "<strong>第 739 題 Daily Temperatures</strong> —— 單調堆疊的入門題",
 ],
 "check": [
   "為什麼水位是 <code>min(左邊最高, 右邊最高)</code> 而不是 <code>max</code>？",
   "雙指標為什麼只處理「比較矮」的那一邊？如果處理比較高的那一邊會算錯什麼？",
   "單調堆疊裡 <code>if not stack: break</code> 是在處理什麼情況？",
   "這題和第 11 題的雙指標寫法很像，但一個求 max 一個求 sum。它們的共同結構是什麼？",
 ],
})
print("P42 written")

# ==================== 43. Multiply Strings ====================
S["p43_grid"] = '''class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        # 關鍵：num1[i] * num2[j] 的結果一定落在 res[i+j] 和 res[i+j+1] 這兩格
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            d1 = int(num1[i])
            for j in range(n - 1, -1, -1):
                d2 = int(num2[j])

                total = d1 * d2 + res[i + j + 1]    # 加上之前留在低位的值
                res[i + j + 1] = total % 10         # 個位留下
                res[i + j] += total // 10           # 進位往前推

        # 去掉開頭的 0（最多只會有一個）
        out = "".join(map(str, res)).lstrip("0")
        return out'''

S["p43_addshift"] = '''class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def add(a: str, b: str) -> str:
            """字串直式加法"""
            i, j = len(a) - 1, len(b) - 1
            carry = 0
            out = []
            while i >= 0 or j >= 0 or carry:
                s = carry
                if i >= 0:
                    s += int(a[i]); i -= 1
                if j >= 0:
                    s += int(b[j]); j -= 1
                out.append(str(s % 10))
                carry = s // 10
            return "".join(reversed(out))

        def mul_digit(a: str, d: int) -> str:
            """字串乘以一位數"""
            if d == 0:
                return "0"
            carry = 0
            out = []
            for ch in reversed(a):
                p = int(ch) * d + carry
                out.append(str(p % 10))
                carry = p // 10
            while carry:
                out.append(str(carry % 10))
                carry //= 10
            return "".join(reversed(out))

        # 就是小學的直式乘法：每一位乘一次、補零、全部加起來
        result = "0"
        for k, ch in enumerate(reversed(num2)):
            partial = mul_digit(num1, int(ch))
            if partial != "0":
                partial += "0" * k          # 補 k 個零（左移 k 位）
            result = add(result, partial)

        return result'''

_p43 = [S.load(k) for k in ("p43_grid", "p43_addshift")]
for a, b in [("2", "3"), ("123", "456"), ("0", "0"), ("0", "123"), ("9", "9"),
             ("999", "999"), ("1", "1"), ("100", "100"), ("123456789", "987654321")]:
    e = str(int(a) * int(b))
    for sol in _p43:
        assert sol.multiply(a, b) == e, ("P43", a, b, sol, sol.multiply(a, b), e)
for _ in range(3000):
    a = str(random.randint(0, 10**random.randint(1, 8)))
    b = str(random.randint(0, 10**random.randint(1, 8)))
    e = str(int(a) * int(b))
    for sol in _p43:
        assert sol.multiply(a, b) == e, ("P43", a, b, sol)
print("P43 solutions OK")

_P43_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">位置對應：num1[i] × num2[j] 的兩位數結果，落在 res[i+j]（十位）和 res[i+j+1]（個位）</text>
            <g font-family="monospace" font-size="14">
              <text x="60" y="60" fill="var(--text-muted)">num1 = &quot;123&quot;   （i = 0,1,2）</text>
              <text x="60" y="84" fill="var(--text-muted)">num2 = &quot;45&quot;    （j = 0,1）</text>
              <text x="60" y="108" fill="var(--accent)">res 長度 = 3 + 2 = 5</text>
            </g>
            <line x1="20" y1="126" x2="620" y2="126" stroke="var(--border)"/>
            <g font-family="monospace" font-size="13">
              <text x="60" y="152" fill="var(--gold)">i=2, j=1:  3 × 5 = 15</text>
              <text x="300" y="152" fill="var(--text-muted)">→ res[3] += 1（十位）, res[4] = 5（個位）</text>
              <text x="60" y="176" fill="var(--gold)">i=2, j=0:  3 × 4 = 12</text>
              <text x="300" y="176" fill="var(--text-muted)">→ res[2] += 1, res[3] = 2</text>
              <text x="60" y="200" fill="var(--gold)">i=1, j=1:  2 × 5 = 10</text>
              <text x="300" y="200" fill="var(--text-muted)">→ res[2] += 1, res[3] = 0</text>
              <text x="60" y="224" fill="var(--text-muted)">…</text>
            </g>
            <line x1="20" y1="242" x2="620" y2="242" stroke="var(--border)"/>
            <g font-size="14" text-anchor="middle">
              <rect x="150" y="262" width="60" height="36" rx="5" fill="none" stroke="var(--border)"/><text x="180" y="286" fill="var(--text-muted)">0</text>
              <rect x="216" y="262" width="60" height="36" rx="5" fill="none" stroke="var(--accent)"/><text x="246" y="286" fill="var(--accent)">5</text>
              <rect x="282" y="262" width="60" height="36" rx="5" fill="none" stroke="var(--accent)"/><text x="312" y="286" fill="var(--accent)">5</text>
              <rect x="348" y="262" width="60" height="36" rx="5" fill="none" stroke="var(--accent)"/><text x="378" y="286" fill="var(--accent)">3</text>
              <rect x="414" y="262" width="60" height="36" rx="5" fill="none" stroke="var(--accent)"/><text x="444" y="286" fill="var(--accent)">5</text>
            </g>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="180" y="314">res[0]</text><text x="246" y="314">res[1]</text>
              <text x="312" y="314">res[2]</text><text x="378" y="314">res[3]</text>
              <text x="444" y="314">res[4]</text>
            </g>
            <text x="20" y="344" fill="var(--gold)" font-size="12">去掉開頭的 0 → &quot;5535&quot;　驗算：123 × 45 = 5535 ✔</text>'''

emit({
 "num": 43, "slug": "multiply-strings",
 "en": [
   "Given two non-negative integers <code>num1</code> and <code>num2</code> represented as "
   "strings, return the product of <code>num1</code> and <code>num2</code>, also represented "
   "as a string.",
   "<strong>Note:</strong> You must not use any built-in BigInteger library or convert the "
   "inputs to integer directly.",
 ],
 "zh": [
   "給你兩個以<strong>字串</strong>表示的非負整數 <code>num1</code> 和 <code>num2</code>，"
   "回傳它們的乘積，同樣以字串表示。",
   "<strong>注意：</strong>不能使用任何大整數函式庫，"
   "也<strong>不能直接把輸入轉成整數</strong>。",
 ],
 "pre": [
   ("note", "核心洞察：結果的位置是可以事先算出來的", [
     ("c", """num1 的第 i 位（從左數，0-indexed）
num2 的第 j 位

它們相乘的結果，會落在結果的哪裡？

    num1[i] 代表的數量級是 10^(m-1-i)
    num2[j] 代表的數量級是 10^(n-1-j)
    乘積的數量級是 10^(m+n-2-i-j)

    如果結果陣列 res 長度是 m+n（同樣是「從左數」），
    那麼數量級 10^k 對應的索引是 (m+n-1) - k
                              = (m+n-1) - (m+n-2-i-j)
                              = i + j + 1

    而 num1[i] * num2[j] 最大是 9×9 = 81，是兩位數，
    所以十位要放在 res[i+j]。

結論：
    res[i+j+1] 放個位
    res[i+j]   放十位

這個公式讓我們可以「先全部乘完再統一處理進位」，
不用管乘法的順序。"""),
     "<strong>為什麼結果的長度是 m + n？</strong>"
     "因為 <code>m</code> 位數乘 <code>n</code> 位數，結果最多是 <code>m + n</code> 位"
     "（例如 99 × 99 = 9801，2 + 2 = 4 位），"
     "最少是 <code>m + n − 1</code> 位（例如 10 × 10 = 100，3 位）。"
     "所以開 <code>m + n</code> 格一定夠，最多前面多一個 0。",
   ]),
 ],
 "examples": """範例 1
  輸入：num1 = "2", num2 = "3"
  輸出："6"

範例 2
  輸入：num1 = "123", num2 = "456"
  輸出："56088\"""",
 "constraints": [
   "1 ≤ <code>num1.length</code>, <code>num2.length</code> ≤ 200",
   "<code>num1</code> 和 <code>num2</code> 只含數字 <code>0</code>–<code>9</code>",
   "兩者都<strong>不含前導零</strong>，除非數字本身就是 <code>\"0\"</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>長度到 200</strong>，所以結果最多 400 位 —— "
       "遠超任何內建整數型別（在 C/Java 裡）。"
       "<strong>Python 的整數是任意精度的，所以 <code>str(int(a)*int(b))</code> 會過</strong>，"
       "但那完全違背題目的用意。",
       "<strong>沒有前導零</strong>（除了 <code>\"0\"</code> 自己）。"
       "所以輸出也不能有前導零 —— <code>lstrip(\"0\")</code> 是必要的。",
       "<strong>其中一個可能是 <code>\"0\"</code></strong>。"
       "這時候結果是 <code>\"0\"</code>，但 <code>lstrip(\"0\")</code> 會把它變成空字串！"
       "<strong>必須先擋掉。</strong>",
       "O(m × n) = 4 × 10⁴ —— 完全不是問題。這題考的是實作，不是效率。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P43_FIG, "0 0 640 356"),
 ],
 "approaches": [
   ap("解法一", "位置對應 + 統一進位（最推薦）", [
     ("c", S["p43_grid"]),
     ("h", "為什麼可以「邊乘邊進位」？"),
     ("c", """total = d1 * d2 + res[i+j+1]

    d1 * d2      最多 81
    res[i+j+1]   最多 9（因為每次都取了 % 10）
    total        最多 90，是兩位數 ✔

res[i+j+1] = total % 10      個位留下
res[i+j]  += total // 10     十位「累加」到前一格（用 += 不是 =）

注意這裡的不對稱：
    res[i+j+1] 用「=」（覆蓋），因為它已經被加進 total 了
    res[i+j]   用「+=」（累加），因為它可能還有別的進位要加

res[i+j] 會不會爆掉（超過 9）？
    會，但沒關係 ——
    因為輪到 (i-1, j) 或 (i, j-1) 時，
    res[i+j] 會被當成「低位」讀進 total，然後處理它的進位。

    迴圈的順序（i 從右往左、j 從右往左）保證了
    「低位一定先被處理完」。

最後一格 res[0] 呢？
    它不會爆，因為結果最多 m+n 位。"""),
     ("h", "迴圈順序為什麼要從右往左？"),
     "因為進位是「從低位往高位傳」的。"
     "從右往左跑，可以保證處理 <code>res[i+j]</code> 時，"
     "所有會影響它的低位進位都已經算完了。",
     ("h", "<code>lstrip(\"0\")</code> 的陷阱"),
     ("c", """res 最多只有一個前導零（因為結果至少 m+n-1 位）。

但 lstrip 是「去掉所有開頭的 0」：
    "0000" -> ""     空字串！

這在 num1 或 num2 是 "0" 時會發生。
所以最上面的 if num1 == "0" or num2 == "0": return "0" 不能省。

更保險的寫法：
    out = "".join(map(str, res)).lstrip("0")
    return out if out else "0\""""),
   ], "O(m·n)", "O(m+n)", "雙層迴圈", "結果陣列", optimal=True),

   ap("解法二", "拆成「乘一位數」+「字串加法」（最像手算）", [
     "把小學的直式乘法照搬過來：<strong>num1 分別乘以 num2 的每一位，"
     "每次結果往左移一位，最後全部加起來。</strong>",
     ("c", S["p43_addshift"]),
     ("c", """    123
  ×  45
  ------
    615        123 × 5，不補零
   4920        123 × 4，補 1 個零
  ------
   5535        兩者相加

程式碼裡：
    k = 0（num2 的個位 '5'）-> mul_digit("123", 5) = "615"，補 0 個零
    k = 1（num2 的十位 '4'）-> mul_digit("123", 4) = "492"，補 1 個零 -> "4920"
    add("615", "4920") = "5535" ✔"""),
     "<strong>優點</strong>：把問題拆成兩個獨立的、各自簡單的子程序"
     "（<code>add</code> 和 <code>mul_digit</code>），"
     "每一個都可以單獨測試。而且 <code>add</code> 本身就是第 415 題、"
     "<code>mul_digit</code> 是第 66 題的變形 —— <strong>都是可以重複使用的元件</strong>。",
     "<strong>缺點</strong>：中間結果要建 <code>n</code> 次字串，常數比解法一大，程式碼也長。",
     "<strong>什麼時候該選它？</strong>"
     "如果你已經有一個寫好的大數加法函式庫，這個做法可以直接組合起來，"
     "不用重新推導位置公式。<strong>在實務上，「組合已知正確的元件」通常比"
     "「寫一個更聰明但更容易錯的東西」划算。</strong>",
   ], "O(m·n)", "O(m+n)", "n 次「乘一位 + 加法」", "中間字串"),
 ],
 "compare": (["解法", "時間", "行數", "可重用性", "備註"],
   [["一、位置對應", "O(m·n)", "18", "低", "面試預設，最短"],
    ["二、拆成 add + mul_digit", "O(m·n)", "38", "高", "元件可重用，好測試"]]),
 "edges": [
   "<strong>任一個是 \"0\"</strong>：<code>(\"0\", \"123\")</code> → <code>\"0\"</code>。"
   "<strong>沒有特判的話 <code>lstrip(\"0\")</code> 會回傳空字串。</strong>",
   "<strong>兩個都是 \"0\"</strong>：<code>(\"0\", \"0\")</code> → <code>\"0\"</code>。",
   "<strong>單一位數</strong>：<code>(\"9\", \"9\")</code> → <code>\"81\"</code>。結果剛好 2 位（m+n）。",
   "<strong>結果少一位</strong>：<code>(\"1\", \"1\")</code> → <code>\"1\"</code>。"
   "<code>res</code> 是 <code>[0,1]</code>，要去掉前導零。",
   "<strong>全是 9</strong>：<code>(\"999\", \"999\")</code> → <code>\"998001\"</code>。進位最密集。",
   "<strong>結尾有 0</strong>：<code>(\"100\", \"100\")</code> → <code>\"10000\"</code>。"
   "<strong>結尾的 0 不能被 strip 掉</strong> —— 用 <code>lstrip</code> 而不是 <code>strip</code>。",
   "<strong>長度到上限</strong>：200 × 200 位，結果 400 位。",
 ],
 "follow": [
   ("h", "追問一：有沒有比 O(m·n) 更快的乘法？"),
   ("c", """有，而且是計算機科學的一個經典主題：

  長乘法（本題）        O(n²)
  Karatsuba（1960）     O(n^1.585)
      把 n 位拆成兩半，用 3 次遞迴乘法而不是 4 次：
      (a·10^k + b)(c·10^k + d)
        = ac·10^2k + (ad + bc)·10^k + bd
        而 ad + bc = (a+b)(c+d) - ac - bd
        所以只要算 ac、bd、(a+b)(c+d) 三次

  Toom-Cook             O(n^1.465) 等（拆成更多份）
  Schönhage-Strassen（1971）  O(n log n log log n)
      用快速傅立葉變換（FFT）
  Harvey-van der Hoeven（2019） O(n log n)
      理論上的最優，但常數大到實務上沒用

實務上的門檻（以 GMP 函式庫為例）：
    < 30 位     長乘法最快（常數最小）
    30~300 位   Karatsuba
    > 幾千位    FFT 系列

本題 200 位，長乘法完全夠用。"""),
   ("h", "追問二：Python 的大整數乘法用什麼演算法？"),
   "CPython 用<strong>長乘法 + Karatsuba</strong>："
   "在 <code>longobject.c</code> 裡，當兩個數都超過 70 個「digit」"
   "（CPython 內部用 30 位元為一個 digit）時切換到 Karatsuba。"
   "<strong>它沒有實作 FFT 乘法</strong> —— 需要超大整數運算時，"
   "Python 使用者通常會轉向 <code>gmpy2</code>（綁定 GMP）。",
   ("h", "追問三：為什麼題目要禁止直接轉整數？"),
   "因為在 C、Java、Go 這些語言裡<strong>根本沒有「直接轉」這個選項</strong> —— "
   "200 位數遠超 64 位元。"
   "這題的本意是「實作大整數乘法」，"
   "而 Python 的任意精度整數讓這個限制變成一句人為的規定。",
   "<strong>面試時的正確態度</strong>：主動說「Python 可以直接算，但我理解題目要的是手寫的直式乘法，"
   "所以我會實作位置對應的版本」。",
 ],
 "related": [
   "<strong>第 415 題 Add Strings</strong> —— 字串加法，這題的元件",
   "<strong>第 67 題 Add Binary</strong> —— 二進位的字串加法",
   "<strong>第 66 題 Plus One</strong> —— 陣列形式的進位",
   "<strong>第 2 題 Add Two Numbers</strong> —— 鏈結串列形式的加法",
 ],
 "check": [
   "<code>num1[i] × num2[j]</code> 為什麼落在 <code>res[i+j]</code> 和 <code>res[i+j+1]</code>？請自己推一遍。",
   "為什麼 <code>res[i+j+1]</code> 用 <code>=</code> 而 <code>res[i+j]</code> 用 <code>+=</code>？",
   "如果不特判 <code>\"0\"</code>，<code>(\"0\", \"5\")</code> 會回傳什麼？",
   "為什麼結果陣列開 <code>m + n</code> 格一定夠？最多會有幾個前導零？",
 ],
})
print("P43 written")
