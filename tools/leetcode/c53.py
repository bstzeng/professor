# -*- coding: utf-8 -*-
"""第 53–55 題。"""
import random
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(53)

# ==================== 53. Maximum Subarray ====================
S["p53_kadane"] = '''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]

        for x in nums[1:]:
            # 關鍵抉擇：是「接上前面那一段」還是「從自己重新開始」？
            cur = max(x, cur + x)
            best = max(best, cur)

        return best'''

S["p53_dp"] = '''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] = 「以 nums[i] 結尾」的最大子陣列和
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)'''

S["p53_prefix"] = '''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 子陣列和 = prefix[j] - prefix[i]
        # 要讓它最大 -> 對每個 j，減掉「目前為止最小的 prefix」
        best = float("-inf")
        prefix = 0
        min_prefix = 0          # prefix[-1] = 0（空前綴）

        for x in nums:
            prefix += x
            best = max(best, prefix - min_prefix)
            min_prefix = min(min_prefix, prefix)

        return best'''

S["p53_divide"] = '''class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def solve(lo: int, hi: int):
            """回傳 (區間總和, 最大前綴和, 最大後綴和, 最大子陣列和)"""
            if lo == hi:
                v = nums[lo]
                return (v, v, v, v)

            mid = (lo + hi) // 2
            ls, lpre, lsuf, lbest = solve(lo, mid)
            rs, rpre, rsuf, rbest = solve(mid + 1, hi)

            total = ls + rs
            pre = max(lpre, ls + rpre)          # 最大前綴：只在左邊，或跨過整個左邊
            suf = max(rsuf, rs + lsuf)          # 最大後綴：只在右邊，或跨過整個右邊
            best = max(lbest, rbest, lsuf + rpre)   # 三種：全左、全右、跨中線

            return (total, pre, suf, best)

        return solve(0, len(nums) - 1)[3]'''

_p53 = [S.load(k) for k in ("p53_kadane", "p53_dp", "p53_prefix", "p53_divide")]


def _p53_ref(nums):
    n = len(nums)
    return max(sum(nums[i:j + 1]) for i in range(n) for j in range(i, n))


for c in [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [1], [5, 4, -1, 7, 8],
          [-1], [-2, -1], [-5, -4, -3], [0], [1, 2, 3]]:
    e = _p53_ref(c)
    for sol in _p53:
        assert sol.maxSubArray(list(c)) == e, ("P53", c, sol, sol.maxSubArray(list(c)), e)
for _ in range(5000):
    c = [random.randint(-8, 8) for _ in range(random.randint(1, 10))]
    e = _p53_ref(c)
    for sol in _p53:
        assert sol.maxSubArray(list(c)) == e, ("P53", c, sol, sol.maxSubArray(list(c)), e)
print("P53 solutions OK")

_P53_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">Kadane：每一步只問一句「前面那段還值得留嗎？」</text>
            <text x="20" y="48" fill="var(--text-muted)" font-size="12">nums = [−2, 1, −3, 4, −1, 2, 1, −5, 4]</text>
            <g font-family="monospace" font-size="12">
              <text x="40" y="80" fill="var(--text-muted)">x</text>
              <text x="130" y="80" fill="var(--text-muted)">cur + x</text>
              <text x="240" y="80" fill="var(--text-muted)">x</text>
              <text x="330" y="80" fill="var(--text-muted)">新的 cur</text>
              <text x="470" y="80" fill="var(--text-muted)">best</text>
            </g>
            <line x1="30" y1="90" x2="600" y2="90" stroke="var(--border)"/>
            <g font-family="monospace" font-size="12">
              <text x="40" y="112" fill="var(--accent)">−2</text><text x="130" y="112" fill="var(--text-muted)">—</text>
              <text x="240" y="112" fill="var(--text-muted)">—</text><text x="330" y="112" fill="var(--gold)">−2</text><text x="470" y="112" fill="#ff8a65">−2</text>

              <text x="40" y="134" fill="var(--accent)">1</text><text x="130" y="134" fill="var(--text-muted)">−1</text>
              <text x="240" y="134" fill="var(--gold)">1 ✔</text><text x="330" y="134" fill="var(--gold)">1</text><text x="470" y="134" fill="#ff8a65">1</text>

              <text x="40" y="156" fill="var(--accent)">−3</text><text x="130" y="156" fill="var(--gold)">−2 ✔</text>
              <text x="240" y="156" fill="var(--text-muted)">−3</text><text x="330" y="156" fill="var(--gold)">−2</text><text x="470" y="156" fill="#ff8a65">1</text>

              <text x="40" y="178" fill="var(--accent)">4</text><text x="130" y="178" fill="var(--text-muted)">2</text>
              <text x="240" y="178" fill="var(--gold)">4 ✔</text><text x="330" y="178" fill="var(--gold)">4</text><text x="470" y="178" fill="#ff8a65">4</text>

              <text x="40" y="200" fill="var(--accent)">−1</text><text x="130" y="200" fill="var(--gold)">3 ✔</text>
              <text x="240" y="200" fill="var(--text-muted)">−1</text><text x="330" y="200" fill="var(--gold)">3</text><text x="470" y="200" fill="#ff8a65">4</text>

              <text x="40" y="222" fill="var(--accent)">2</text><text x="130" y="222" fill="var(--gold)">5 ✔</text>
              <text x="240" y="222" fill="var(--text-muted)">2</text><text x="330" y="222" fill="var(--gold)">5</text><text x="470" y="222" fill="#ff8a65">5</text>

              <text x="40" y="244" fill="var(--accent)">1</text><text x="130" y="244" fill="var(--gold)">6 ✔</text>
              <text x="240" y="244" fill="var(--text-muted)">1</text><text x="330" y="244" fill="var(--gold)">6</text><text x="470" y="244" fill="#ff8a65">6</text>

              <text x="40" y="266" fill="var(--accent)">−5</text><text x="130" y="266" fill="var(--gold)">1 ✔</text>
              <text x="240" y="266" fill="var(--text-muted)">−5</text><text x="330" y="266" fill="var(--gold)">1</text><text x="470" y="266" fill="#ff8a65">6</text>

              <text x="40" y="288" fill="var(--accent)">4</text><text x="130" y="288" fill="var(--gold)">5 ✔</text>
              <text x="240" y="288" fill="var(--text-muted)">4</text><text x="330" y="288" fill="var(--gold)">5</text><text x="470" y="288" fill="#ff8a65">6</text>
            </g>
            <text x="20" y="322" fill="var(--gold)" font-size="12">答案 6（子陣列 [4, −1, 2, 1]）。「cur 變負了就重新開始」是這個演算法的靈魂。</text>'''

emit({
 "num": 53, "slug": "maximum-subarray",
 "en": [
   "Given an integer array <code>nums</code>, find the subarray with the largest sum, and "
   "return <em>its sum</em>.",
   "A <strong>subarray</strong> is a contiguous <strong>non-empty</strong> sequence of "
   "elements within an array.",
   "<strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try "
   "coding another solution using the <strong>divide and conquer</strong> approach.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，找出<strong>和最大</strong>的連續子陣列，回傳它的和。",
   "<strong>子陣列</strong>指的是陣列裡<strong>連續</strong>且<strong>非空</strong>的一段。",
   "<strong>進階：</strong>如果你已經想出 <code>O(n)</code> 的解，"
   "試著再用<strong>分治法</strong>寫一個。",
 ],
 "pre": [
   ("note", "「非空」這兩個字很重要", [
     ("c", """如果允許空子陣列，全負的輸入答案就是 0（什麼都不選）。
題目說「非空」，所以：

    nums = [-2, -1]  ->  答案是 -1（選最大的那個），不是 0

這就是為什麼 best 的初值要是 nums[0]，不能是 0。

    best = 0 的寫法在 [-2, -1] 上會回傳 0  ✘
    best = nums[0] 的寫法回傳 -1           ✔

這是本題第一名的 bug，而且「全正數」的測資抓不出來。"""),
     "<strong>核心洞察（Kadane 演算法）</strong>：走到位置 <code>i</code> 時，"
     "「以 <code>i</code> 結尾的最大子陣列」只有兩種可能 —— "
     "<strong>接上前面那一段</strong>，或<strong>從 <code>i</code> 自己重新開始</strong>。"
     "而「什麼時候該重新開始？」的答案是：<strong>當前面那一段的和是負的時候</strong>"
     "（負數只會拖累，不如丟掉）。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [-2,1,-3,4,-1,2,1,-5,4]
  輸出：6
  說明：子陣列 [4,-1,2,1] 的和是 6，最大。

範例 2
  輸入：nums = [1]
  輸出：1

範例 3
  輸入：nums = [5,4,-1,7,8]
  輸出：23
  說明：整個陣列。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n 到 10⁵</strong>。O(n²) 是 10¹⁰ —— 必定 TLE。要 O(n)。",
       "<strong>陣列至少有一個元素</strong>，所以 <code>nums[0]</code> 一定存在，"
       "可以安全地當初值。",
       "<strong>有負數，而且可能全是負數</strong>。"
       "配上「非空」的要求，就是這題最大的陷阱。",
       "<strong>總和最大 10⁵ × 10⁴ = 10⁹</strong>，"
       "在 32 位元整數範圍內（剛好），但在 C/Java 裡值得留意。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P53_FIG, "0 0 640 334"),
 ],
 "approaches": [
   ap("解法一", "Kadane 演算法（標準解）", [
     ("c", S["p53_kadane"]),
     ("h", "一行轉移式的三種讀法"),
     ("c", """cur = max(x, cur + x)

讀法 1（選擇）：
    「以 x 結尾的最大和」= max(只要 x 自己, 接上前面那一段)

讀法 2（丟棄）：
    等價於 cur = x + max(0, cur)
    「前面那段如果是負的，就當它不存在」

讀法 3（重啟）：
    if cur < 0: cur = 0      # 重新開始
    cur += x

三種寫法完全等價，挑一個你覺得最直覺的記。

為什麼「前面那段是負的就丟掉」是對的？
    設前面那段的和是 S。
    - S >= 0：帶著它只會讓總和變大（或不變），留著。
    - S <  0：帶著它一定讓總和變小，不如從 x 重新開始。

    這是一個「局部決定就足夠」的貪婪 ——
    而它之所以正確，是因為子陣列必須「連續」：
    要接上前面，就必須把「整段」都接上，不能挑著接。"""),
     ("h", "為什麼 <code>best</code> 和 <code>cur</code> 要分開？"),
     "<code>cur</code> 是「<strong>以目前這一格結尾</strong>的最大和」，"
     "<code>best</code> 是「<strong>到目前為止看過的所有</strong>子陣列裡最大的和」。"
     "<code>cur</code> 會上上下下，<code>best</code> 只增不減。"
     "<strong>只用一個變數是這題第二名的 bug。</strong>",
     "<strong>Kadane 演算法由 Jay Kadane 在 1984 年提出</strong>，"
     "當時是為了回應 Ulf Grenander 提出的一個影像處理問題"
     "（在二維的圖裡找「最大和的矩形區域」）。"
     "一維的情況被 Kadane 在幾分鐘內解決 —— 這個故事被 Jon Bentley 寫進了《Programming Pearls》。",
   ], "O(n)", "O(1)", "掃一遍", "兩個變數", optimal=True),

   ap("解法二", "明確寫成 DP（同一件事，換個說法）", [
     ("c", S["p53_dp"]),
     "<code>dp[i]</code> 的定義是「<strong>以 <code>nums[i]</code> 結尾</strong>的最大子陣列和」—— "
     "<strong>不是「前 i 個元素裡的最大子陣列和」</strong>。"
     "這個「以 i 結尾」的定義是關鍵：它讓轉移只依賴 <code>dp[i-1]</code>。",
     ("c", """如果定義成「前 i 個元素裡的最大子陣列和」會怎樣？

    那 dp[i] = max(dp[i-1], 某個以 i 結尾的子陣列和)
    但「某個以 i 結尾的子陣列和」本身又要重新算 ——
    轉移式不封閉，DP 做不下去。

「以 i 結尾」這個限制，讓子問題之間產生了遞推關係。

這是設計 DP 狀態時最常見的技巧：
    加一個「必須用到第 i 個元素」的限制，
    讓子問題變得可遞推，最後再對所有 i 取 max。

同樣的手法出現在：
    第 300 題 最長遞增子序列（以 i 結尾的最長遞增子序列）
    第 152 題 乘積最大子陣列
    第 918 題 環形子陣列的最大和"""),
     "<strong>Kadane 就是這個 DP 的滾動陣列版</strong>（只留 <code>dp[i-1]</code>），"
     "所以空間從 O(n) 降到 O(1)。",
   ], "O(n)", "O(n)", "掃一遍", "dp 陣列（可壓到 O(1)）"),

   ap("解法三", "前綴和的視角", [
     "<strong>子陣列 <code>nums[i..j]</code> 的和 = <code>prefix[j] − prefix[i-1]</code>。</strong>"
     "所以「最大子陣列和」= 「對每個 <code>j</code>，找出最小的 <code>prefix[i-1]</code>」。",
     ("c", S["p53_prefix"]),
     ("c", """nums   = [-2,  1, -3,  4, -1,  2,  1, -5,  4]
prefix = [-2, -1, -4,  0, -1,  1,  2, -3,  1]
           （prefix[-1] = 0，代表空前綴）

對每個 j，答案候選 = prefix[j] - min(prefix[-1..j-1])

j=0: -2 - 0  = -2      min_prefix = min(0, -2) = -2
j=1: -1 - (-2) = 1     min_prefix = -2
j=2: -4 - (-2) = -2    min_prefix = -4
j=3:  0 - (-4) = 4     min_prefix = -4
j=4: -1 - (-4) = 3     min_prefix = -4
j=5:  1 - (-4) = 5     min_prefix = -4
j=6:  2 - (-4) = 6  ✔  min_prefix = -4
j=7: -3 - (-4) = 1     min_prefix = -4
j=8:  1 - (-4) = 5     min_prefix = -4

最大 6 ✔"""),
     "<strong>注意 <code>min_prefix</code> 的初值是 0 而不是 <code>inf</code>。</strong>"
     "0 代表「空前綴」，也就是「子陣列從索引 0 開始」的情況。"
     "而且<strong>更新 <code>min_prefix</code> 必須在計算答案之後</strong> —— "
     "否則 <code>prefix[j] - prefix[j] = 0</code> 會變成一個候選答案，"
     "對應「空子陣列」，違反「非空」的要求。",
     "<strong>這個視角的價值</strong>：它能直接推廣到"
     "「和最接近 k 的子陣列」（用有序集合找最接近的 prefix）、"
     "「和為 k 的子陣列個數」（第 560 題，用雜湊表）、"
     "「和至少為 k 的最短子陣列」（第 862 題，用單調佇列）。"
     "<strong>Kadane 推廣不了這些，前綴和可以。</strong>",
   ], "O(n)", "O(1)", "掃一遍", "三個變數"),

   ap("解法四", "分治法（題目的進階要求）", [
     "把陣列從中間切開。最大子陣列只有三種可能："
     "<strong>完全在左半、完全在右半、或跨過中線</strong>。",
     ("c", S["p53_divide"]),
     ("h", "為什麼要回傳四個值？"),
     ("c", """只回傳「最大子陣列和」是不夠的 ——
因為「跨中線」的情況需要「左半的最大後綴」和「右半的最大前綴」。

而「最大前綴／後綴」在合併時又需要「區間總和」。
所以一次回傳四個值：

    total  區間總和         合併：ls + rs
    pre    最大前綴和        合併：max(lpre, ls + rpre)
    suf    最大後綴和        合併：max(rsuf, rs + lsuf)
    best   最大子陣列和       合併：max(lbest, rbest, lsuf + rpre)
                                              ^^^^^^^^^^^^^ 跨中線

「最大前綴」的兩種可能：
    只在左半裡（lpre），
    或者「吃掉整個左半」再加上右半的最大前綴（ls + rpre）。

這種「為了能合併，多回傳幾個輔助值」的技巧，
在線段樹（segment tree）裡非常常見 ——
事實上，這四個值構成的就是一個可以放進線段樹的「幺半群（monoid）」。"""),
     ("h", "複雜度"),
     "<code>T(n) = 2T(n/2) + O(1)</code>，由主定理得 <strong>O(n)</strong>… "
     "等等，其實是 <strong>O(n)</strong> 沒錯 —— "
     "因為合併只花 O(1)（不像 merge sort 要 O(n)）。"
     "但遞迴本身有 O(n) 個節點，所以總共 O(n) 時間、O(log n) 空間（遞迴堆疊）。",
     "<strong>比 Kadane 慢（常數大很多），而且更難寫。為什麼還要學？</strong>",
     ("ul", [
       "<strong>它可以放進線段樹</strong>，支援「查詢任意區間的最大子陣列和」和「單點修改」，"
       "各 O(log n)。Kadane 做不到 —— 它只能算整個陣列，而且不支援修改。",
       "<strong>它可以平行化</strong>：左右兩半完全獨立。",
       "<strong>它是題目明確要求的進階</strong>。",
     ]),
   ], "O(n)", "O(log n)", "合併只要 O(1)", "遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "可推廣到", "備註"],
   [["一、Kadane", "O(n)", "O(1)", "乘積最大、環形", "面試預設"],
    ["二、DP 陣列", "O(n)", "O(n)", "同上", "Kadane 的未壓縮版"],
    ["三、前綴和", "O(n)", "O(1)", "和為 k、最接近 k", "視角最能推廣"],
    ["四、分治", "O(n)", "O(log n)", "線段樹、平行化", "進階要求"]]),
 "edges": [
   "<strong>全是負數</strong>：<code>[-2,-1]</code> → −1；<code>[-5,-4,-3]</code> → −3。"
   "<strong><code>best = 0</code> 的寫法會錯。</strong>",
   "<strong>單一元素</strong>：<code>[1]</code> → 1；<code>[-1]</code> → −1。",
   "<strong>全是正數</strong>：<code>[1,2,3]</code> → 6（整個陣列）。",
   "<strong>含 0</strong>：<code>[0]</code> → 0；<code>[-1,0,-1]</code> → 0。",
   "<strong>答案在中間</strong>：<code>[-2,1,-3,4,-1,2,1,-5,4]</code> → 6。",
   "<strong>答案是整個陣列</strong>：<code>[5,4,-1,7,8]</code> → 23。",
   "<strong>前綴和版更新 <code>min_prefix</code> 的順序</strong>："
   "如果先更新再算答案，<code>[-1]</code> 會回傳 0 而不是 −1。",
 ],
 "follow": [
   ("h", "追問一：如果要回傳那個子陣列的起訖位置呢？"),
   ("c", """在 Kadane 裡多記兩個變數：

    best = cur = nums[0]
    start = end = tmp_start = 0

    for i in range(1, len(nums)):
        if cur + nums[i] < nums[i]:
            cur = nums[i]
            tmp_start = i          # 從這裡重新開始
        else:
            cur += nums[i]
        if cur > best:
            best = cur
            start, end = tmp_start, i

複雜度不變。
但要先問清楚：如果有多組答案，要回哪一組？""",),
   ("h", "追問二：環形陣列呢？"),
   "第 918 題。答案是以下兩者的較大值：",
   ("ul", [
     "<strong>不跨越邊界</strong>：就是本題的 Kadane 結果",
     "<strong>跨越邊界</strong>：<code>總和 − 最小子陣列和</code>"
     "（把中間「不要的那一段」挖掉）",
   ]),
   "<strong>但要小心一個邊界</strong>：如果全是負數，"
   "「總和 − 最小子陣列和」會是 0（挖掉全部），違反「非空」。"
   "這時候直接回傳 Kadane 的結果。",
   ("h", "追問三：乘積最大子陣列呢？"),
   "第 152 題。<strong>Kadane 的直接推廣行不通</strong>，"
   "因為「負數乘負數會變正數」—— 目前最小的乘積可能在下一步變成最大的。"
   "解法是<strong>同時維護最大和最小兩個值</strong>：",
   ("c", """cur_max, cur_min = max(x, cur_max * x, cur_min * x), \\
                   min(x, cur_max * x, cur_min * x)

（要用舊的 cur_max 算新的 cur_min，所以要同時賦值或先存起來。）

這是一個很好的提醒：
「加法」和「乘法」的結構不同，
加法只需要追蹤一個極值，乘法需要兩個。""",),
   ("h", "追問四：二維版（最大和的子矩形）呢？"),
   "第 363 題的變形。標準做法是：<strong>枚舉「上邊界」和「下邊界」（O(m²) 對），"
   "把那幾列壓縮成一維陣列，再對它跑 Kadane</strong>。"
   "總共 O(m² · n)。"
   "<strong>這正是 Grenander 當年提出的原始問題</strong> —— Kadane 的一維解法就是為了它。",
 ],
 "related": [
   "<strong>第 152 題 Maximum Product Subarray</strong> —— 乘法版，要維護兩個極值",
   "<strong>第 918 題 Maximum Sum Circular Subarray</strong> —— 環形版",
   "<strong>第 560 題 Subarray Sum Equals K</strong> —— 前綴和 + 雜湊表",
   "<strong>第 300 題 Longest Increasing Subsequence</strong> —— 同樣是「以 i 結尾」的 DP",
   "<strong>第 121 題 Best Time to Buy and Sell Stock</strong> —— 本質上是同一題",
 ],
 "check": [
   "為什麼 <code>best</code> 的初值不能是 0？哪一筆測資會錯？",
   "<code>cur = max(x, cur + x)</code> 的三種等價寫法是什麼？它們在說同一件事嗎？",
   "DP 的狀態為什麼要定義成「以 i 結尾」而不是「前 i 個裡的最大」？",
   "前綴和版為什麼一定要「先算答案、再更新 <code>min_prefix</code>」？",
 ],
})
print("P53 written")

# ==================== 54. Spiral Matrix ====================
S["p54_bounds"] = '''class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        out = []

        while top <= bottom and left <= right:
            # 往右：走完最上面那一列
            for c in range(left, right + 1):
                out.append(matrix[top][c])
            top += 1

            # 往下：走完最右邊那一行
            for r in range(top, bottom + 1):
                out.append(matrix[r][right])
            right -= 1

            # 往左：走完最下面那一列（要先確認還有列可走）
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    out.append(matrix[bottom][c])
                bottom -= 1

            # 往上：走完最左邊那一行（要先確認還有行可走）
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    out.append(matrix[r][left])
                left += 1

        return out'''

S["p54_dir"] = '''class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        seen = [[False] * n for _ in range(m)]

        # 右、下、左、上，順時針
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        r = c = d = 0
        out = []
        for _ in range(m * n):
            out.append(matrix[r][c])
            seen[r][c] = True

            nr, nc = r + DIRS[d][0], c + DIRS[d][1]
            # 撞牆或撞到走過的地方 -> 轉 90 度
            if not (0 <= nr < m and 0 <= nc < n and not seen[nr][nc]):
                d = (d + 1) % 4
                nr, nc = r + DIRS[d][0], c + DIRS[d][1]
            r, c = nr, nc

        return out'''

S["p54_peel"] = '''class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        m = [row[:] for row in matrix]      # 不要改到呼叫端的資料
        while m:
            out += m.pop(0)                 # 剝掉最上面一列
            m = [list(r) for r in zip(*m)][::-1]   # 逆時針轉 90 度
        return out'''

_p54 = [S.load(k) for k in ("p54_bounds", "p54_dir", "p54_peel")]


def _p54_ref(matrix):
    res = []
    m = [row[:] for row in matrix]
    while m and m[0]:
        res += m.pop(0)
        m = [list(r) for r in zip(*m)][::-1]
    return res


for mat in [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [[1]], [[1, 2]], [[1], [2]], [], [[]],
            [[1, 2, 3], [4, 5, 6]], [[1], [2], [3], [4]]]:
    e = _p54_ref(mat)
    for sol in _p54:
        g = sol.spiralOrder([r[:] for r in mat])
        assert g == e, ("P54", mat, sol, g, e)
for _ in range(2000):
    m_, n_ = random.randint(0, 5), random.randint(0, 5)
    mat = [[random.randint(0, 99) for _ in range(n_)] for _ in range(m_)]
    e = _p54_ref(mat)
    for sol in _p54:
        g = sol.spiralOrder([r[:] for r in mat])
        assert g == e, ("P54", mat, sol, g, e)
    if m_ and n_:
        assert sorted(e) == sorted(v for row in mat for v in row), ("P54 missing", mat)
print("P54 solutions OK")

_P54_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">四個邊界 top / bottom / left / right，每走完一條邊就往內收一格</text>
            <g font-size="14" text-anchor="middle">
              <rect x="180" y="52" width="46" height="40" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="203" y="78" fill="var(--accent)">1</text>
              <rect x="226" y="52" width="46" height="40" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="249" y="78" fill="var(--accent)">2</text>
              <rect x="272" y="52" width="46" height="40" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="295" y="78" fill="var(--accent)">3</text>
              <rect x="318" y="52" width="46" height="40" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="341" y="78" fill="var(--accent)">4</text>
              <rect x="180" y="92" width="46" height="40" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="203" y="118" fill="var(--gold)">12</text>
              <rect x="226" y="92" width="46" height="40" fill="none" stroke="var(--border)"/><text x="249" y="118" fill="var(--text-muted)">13</text>
              <rect x="272" y="92" width="46" height="40" fill="none" stroke="var(--border)"/><text x="295" y="118" fill="var(--text-muted)">14</text>
              <rect x="318" y="92" width="46" height="40" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="341" y="118" fill="#ff8a65">5</text>
              <rect x="180" y="132" width="46" height="40" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="203" y="158" fill="var(--gold)">11</text>
              <rect x="226" y="132" width="46" height="40" fill="none" stroke="var(--border)"/><text x="249" y="158" fill="var(--text-muted)">16</text>
              <rect x="272" y="132" width="46" height="40" fill="none" stroke="var(--border)"/><text x="295" y="158" fill="var(--text-muted)">15</text>
              <rect x="318" y="132" width="46" height="40" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="341" y="158" fill="#ff8a65">6</text>
              <rect x="180" y="172" width="46" height="40" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="203" y="198" fill="var(--gold)">10</text>
              <rect x="226" y="172" width="46" height="40" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="249" y="198" fill="var(--gold)">9</text>
              <rect x="272" y="172" width="46" height="40" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="295" y="198" fill="var(--gold)">8</text>
              <rect x="318" y="172" width="46" height="40" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="341" y="198" fill="#ff8a65">7</text>
            </g>
            <text x="272" y="42" fill="var(--accent)" font-size="11" text-anchor="middle">① 往右（top 那一列）</text>
            <text x="420" y="118" fill="#ff8a65" font-size="11">② 往下（right 那一行）</text>
            <text x="272" y="228" fill="var(--gold)" font-size="11" text-anchor="middle">③ 往左（bottom 那一列）　④ 往上（left 那一行）</text>
            <text x="20" y="262" fill="var(--gold)" font-size="12">走完一圈後 top++、right−−、bottom−−、left++，範圍縮小，繼續下一圈</text>
            <text x="20" y="286" fill="var(--text-muted)" font-size="12">③ 和 ④ 前面的 if 是為了「只剩一列」或「只剩一行」時不要重複走</text>'''

emit({
 "num": 54, "slug": "spiral-matrix",
 "en": [
   "Given an <code>m x n</code> <code>matrix</code>, return <em>all elements of the "
   "<code>matrix</code> in spiral order</em>.",
 ],
 "zh": [
   "給你一個 <code>m × n</code> 的矩陣，按<strong>螺旋順序</strong>（順時針由外往內）"
   "回傳所有元素。",
 ],
 "pre": [
   ("note", "三種思路，難度天差地遠", [
     ("c", """① 四個邊界（最常見）
    維護 top / bottom / left / right，
    每走完一條邊就往內收，直到邊界交錯。
    -> 要小心「只剩一列」或「只剩一行」時的重複走

② 方向陣列 + 走過標記
    像一隻蟲在爬，撞牆或撞到走過的地方就右轉。
    -> 最不容易出錯，但要 O(mn) 額外空間

③ 剝洋蔥（Python 的花招）
    取走第一列，把剩下的逆時針轉 90 度，重複。
    -> 三行，但每次轉置是 O(mn)，總共 O(mn·min(m,n))

面試建議：寫 ①，但先在紙上畫一遍走法再下筆。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
  輸出：[1,2,3,6,9,8,7,4,5]

範例 2
  輸入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
  輸出：[1,2,3,4,8,12,11,10,9,5,6,7]""",
 "constraints": [
   "<code>m == matrix.length</code>，<code>n == matrix[i].length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 10",
   "−100 ≤ <code>matrix[i][j]</code> ≤ 100",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>不一定是正方形</strong>。<code>m × n</code> 可以是 <code>1 × 5</code> 或 <code>5 × 1</code> —— "
       "<strong>這正是最容易出錯的兩種形狀。</strong>",
       "<strong>規模只有 10 × 10</strong>，效率完全不是問題。"
       "這題純粹考<strong>邊界處理</strong>。",
       "<strong>保證 m, n ≥ 1</strong>，所以不會有空矩陣。"
       "但寫上 <code>if not matrix or not matrix[0]</code> 只要一行，建議保留。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P54_FIG, "0 0 640 298"),
 ],
 "approaches": [
   ap("解法一", "四個邊界，一圈一圈往內收（標準解）", [
     ("c", S["p54_bounds"]),
     ("h", "第 3、4 步前面的 <code>if</code> 是關鍵"),
     ("c", """考慮 matrix = [[1, 2, 3]]（只有一列）

不加 if 的話：
    ① 往右：收 1, 2, 3    top 變成 1
    ② 往下：range(1, 1) 是空的，什麼都不收    right 變成 1
    ③ 往左：range(1, -1, -1) = [1, 0]
            收 matrix[0][1] = 2、matrix[0][0] = 1   ✘ 重複了！

加上 if top <= bottom（此時 top=1 > bottom=0）就會跳過 ③ ✔

同理，matrix = [[1],[2],[3]]（只有一行）需要 if left <= right。

為什麼 ① 和 ② 不用 if？
    因為進入 while 迴圈時已經確認 top <= bottom 且 left <= right，
    所以 ① 一定安全。
    ② 的 range(top, bottom+1) 在 top > bottom 時自然是空的，
    不會出錯（只是什麼都不做）。

    嚴格說 ② 也可以加 if，但沒有必要。
    ③ 和 ④ 則是「必須」加 —— 因為它們用的是反向 range，
    在邊界交錯時會產生「反過來的有效範圍」而重複收集。"""),
     ("h", "四個步驟的對稱性"),
     ("t", ["方向", "固定的邊界", "變動的範圍", "走完之後"],
       [["① 往右", "<code>top</code>", "<code>left → right</code>", "<code>top += 1</code>"],
        ["② 往下", "<code>right</code>", "<code>top → bottom</code>", "<code>right -= 1</code>"],
        ["③ 往左", "<code>bottom</code>", "<code>right → left</code>", "<code>bottom -= 1</code>"],
        ["④ 往上", "<code>left</code>", "<code>bottom → top</code>", "<code>left += 1</code>"]]),
     "<strong>注意每一步用的是「更新過的」邊界</strong>："
     "② 的 <code>range(top, ...)</code> 用的是 ① 之後的 <code>top</code>。"
     "這個順序不能亂，否則會重複收集角落。",
   ], "O(m·n)", "O(1)", "每個元素收集一次", "不算輸出的話只有四個變數", optimal=True),

   ap("解法二", "方向陣列 + 走過標記（最不容易錯）", [
     "換個思路：<strong>不去想「邊界在哪」，而是像一隻蟲在爬 —— "
     "能直走就直走，撞牆或撞到走過的地方就右轉 90 度。</strong>",
     ("c", S["p54_dir"]),
     ("c", """DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
        右      下      左       上

d = (d + 1) % 4 就是「順時針轉 90 度」。

這個「方向陣列 + 模 4」的寫法是網格題的標準工具：
    順時針：DIRS = [右, 下, 左, 上]，d = (d+1) % 4
    逆時針：同一個陣列，d = (d-1) % 4  （Python 的負數取模是正的）
    四方向 BFS：直接對所有 4 個方向展開

用 (0,1) 這種 tuple 而不是一堆 if，
可以讓「換方向」變成純粹的算術，不用改控制流程。"""),
     "<strong>優點</strong>：完全不用推導邊界，"
     "「只剩一列」「只剩一行」這些情況<strong>自動正確</strong>"
     "（因為 <code>seen</code> 會擋住）。",
     "<strong>缺點</strong>：需要 O(mn) 的 <code>seen</code> 陣列。",
     "<strong>省掉 <code>seen</code> 的技巧</strong>：如果允許修改輸入，"
     "可以把走過的格子設成一個「不可能的值」（例如 101，因為題目說值域是 −100 到 100）。"
     "但那會破壞輸入，而且依賴「有一個保留值可用」—— <strong>不是好設計</strong>，"
     "面試時提出來要同時說明它的代價。",
     "<strong>迴圈跑 <code>m * n</code> 次</strong>（剛好每個元素一次），"
     "所以不需要任何終止條件的判斷 —— 這也是它不容易出錯的原因。",
   ], "O(m·n)", "O(m·n)", "每個元素一次", "seen 陣列"),

   ap("解法三", "剝洋蔥（Python 三行）", [
     ("c", S["p54_peel"]),
     ("c", """每一輪做兩件事：
    1. 取走最上面一列（那就是螺旋的下一段）
    2. 把剩下的「逆時針轉 90 度」，讓下一段又跑到最上面

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

  取走 [1,2,3]，剩下 [[4,5,6],[7,8,9]]
  逆時針轉 -> [[6,9],[5,8],[4,7]]
  取走 [6,9]，剩下 [[5,8],[4,7]]
  逆時針轉 -> [[8,7],[5,4]]
  取走 [8,7]，剩下 [[5,4]]
  逆時針轉 -> [[4],[5]]
  取走 [4]，剩下 [[5]]
  逆時針轉 -> [[5]]
  取走 [5]，剩下 []

  結果 [1,2,3,6,9,8,7,4,5] ✔

「逆時針轉 90 度」= zip(*m) 之後把列的順序反轉
    [list(r) for r in zip(*m)][::-1]"""),
     "<strong>極短，而且完全沒有邊界判斷</strong> —— 這是它最迷人的地方。",
     "<strong>但複雜度較差</strong>：每次轉置是 O(mn)，一共轉 <code>min(m,n)</code> 次左右，"
     "總共 <strong>O(mn · min(m,n))</strong>。"
     "在 10×10 完全無所謂，但在 1000×1000 就會很慢。",
     "<strong>而且它會消耗記憶體</strong>（每次轉置都建新矩陣）。"
     "面試時可以當作「Python 的花招」提一下，但別當主答案。",
   ], "O(m·n·min(m,n))", "O(m·n)", "每輪轉置一次", "中間矩陣"),
 ],
 "compare": (["解法", "時間", "空間", "邊界難度", "面試推薦"],
   [["一、四邊界", "O(mn)", "O(1)", "★★★☆☆ 要小心 if", "★★★★★"],
    ["二、方向 + seen", "O(mn)", "O(mn)", "★☆☆☆☆ 幾乎沒有", "★★★★☆"],
    ["三、剝洋蔥", "O(mn·min)", "O(mn)", "★☆☆☆☆", "★★☆☆☆"]]),
 "edges": [
   "<strong>單一元素</strong>：<code>[[1]]</code> → <code>[1]</code>。",
   "<strong>只有一列</strong>：<code>[[1,2,3]]</code> → <code>[1,2,3]</code>。"
   "<strong>沒有 <code>if top &lt;= bottom</code> 會變成 <code>[1,2,3,2,1]</code>。</strong>",
   "<strong>只有一行</strong>：<code>[[1],[2],[3]]</code> → <code>[1,2,3]</code>。"
   "<strong>沒有 <code>if left &lt;= right</code> 會重複。</strong>",
   "<strong>2 × 2</strong>：<code>[[1,2],[3,4]]</code> → <code>[1,2,4,3]</code>。",
   "<strong>寬扁矩陣</strong>：<code>[[1,2,3],[4,5,6]]</code> → <code>[1,2,3,6,5,4]</code>。",
   "<strong>正中間剩一格</strong>：<code>3 × 3</code> 的最後一個元素 5。",
   "<strong>輸出長度</strong>：永遠應該是 <code>m × n</code>。"
   "<strong>寫完之後先檢查長度，是最快的除錯方法。</strong>",
 ],
 "follow": [
   ("h", "追問一：反過來，生成一個螺旋矩陣呢？"),
   "第 59 題（Spiral Matrix II）。"
   "把「讀取」換成「寫入」即可，四個邊界的邏輯一模一樣。"
   "<strong>而且第 59 題保證是正方形（n × n），所以連 <code>if</code> 都可以省</strong>"
   "（正方形不會出現「只剩一列」的中途狀態…"
   "其實 n 是奇數時會剩正中間一格，但那是 <code>top == bottom</code> 且 "
   "<code>left == right</code>，① 會收掉它，之後 ③ 的 if 就擋住了 —— 還是建議保留）。",
   ("h", "追問二：從內往外的螺旋呢？"),
   "最簡單的做法：<strong>照本題做，然後把結果反轉</strong>。"
   "（由外往內順時針的反轉，就是由內往外逆時針。）"
   "如果要「由內往外順時針」，就要另外推導起點和走法。",
   ("h", "追問三：螺旋走訪在真實世界的用途？"),
   ("ul", [
     "<strong>JPEG 的 zigzag 掃描</strong>：把 8×8 的 DCT 係數按「之字形」排列，"
     "讓低頻（重要）的係數集中在前面，高頻（可捨棄）的在後面。"
     "雖然是 zigzag 不是螺旋，但都是「用一個走訪順序把二維資料的重要性排序」。",
     "<strong>影像處理的區域成長</strong>：從一點往外螺旋搜尋最近的特徵。",
     "<strong>Ulam 螺旋</strong>：把自然數按螺旋排列，質數會呈現神奇的對角線圖案 —— "
     "這是數論裡一個著名的視覺化。",
   ]),
   ("h", "追問四：為什麼「方向陣列」的寫法在網格題裡這麼常見？"),
   "因為它把「往哪走」從<strong>控制流程</strong>變成了<strong>資料</strong>。",
   ("c", """不用方向陣列：
    if d == 0: c += 1
    elif d == 1: r += 1
    elif d == 2: c -= 1
    else: r -= 1

用方向陣列：
    r += DIRS[d][0]; c += DIRS[d][1]

好處：
    - 加一個方向（例如八方向）只要改陣列，不用改邏輯
    - 「轉向」變成算術（(d+1) % 4），可以被組合和推理
    - 程式碼短，而且四個方向被強制對稱處理（不會漏改一個）

這個技巧在 BFS/DFS 走迷宮、島嶼問題、
西洋棋的騎士走法（八個方向）都是標準寫法。""",),
 ],
 "related": [
   "<strong>第 59 題 Spiral Matrix II</strong> —— 反過來生成",
   "<strong>第 885 題 Spiral Matrix III</strong> —— 從任意點出發，可以走出邊界",
   "<strong>第 48 題 Rotate Image</strong> —— 另一個「一圈一圈」的矩陣題",
   "<strong>第 200 題 Number of Islands</strong> —— 方向陣列的典型應用",
 ],
 "check": [
   "為什麼第 3、4 步前面需要 <code>if</code>，而第 1、2 步不需要？",
   "用 <code>[[1,2,3]]</code>（只有一列）追一遍，說明沒有 <code>if</code> 會輸出什麼。",
   "方向陣列的寫法為什麼不需要處理「只剩一列」的情況？",
   "寫完之後最快的除錯方法是什麼？（提示：和輸出的長度有關）",
 ],
})
print("P54 written")
