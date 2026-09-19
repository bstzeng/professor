# -*- coding: utf-8 -*-
"""第 4–9 題：內容 + 解法測試。所有貼在頁面上的程式碼都先在這裡跑過。"""
import random
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(4)

# ==================== 4. Median of Two Sorted Arrays ====================
S["p4_merge"] = '''class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        if n % 2:
            return float(merged[n // 2])
        return (merged[n // 2 - 1] + merged[n // 2]) / 2'''

S["p4_twopointer"] = '''class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        # 只要走到第 total//2 個位置就夠了，不必合併完整個陣列
        need = total // 2 + 1
        i = j = 0
        prev = cur = 0
        for _ in range(need):
            prev = cur
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                cur = nums1[i]; i += 1
            else:
                cur = nums2[j]; j += 1
        if total % 2:
            return float(cur)
        return (prev + cur) / 2'''

S["p4_kth"] = '''class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def kth(i: int, j: int, k: int) -> int:
            """回傳 nums1[i:] 與 nums2[j:] 合起來第 k 小的數（k 從 1 起算）。"""
            if i >= len(nums1):            # nums1 用完了，直接在 nums2 上數
                return nums2[j + k - 1]
            if j >= len(nums2):
                return nums1[i + k - 1]
            if k == 1:                     # 取兩個開頭較小的
                return min(nums1[i], nums2[j])

            half = k // 2
            # 各往前看 half 個；超出邊界視為 +inf（那一邊絕不會被丟掉）
            va = nums1[i + half - 1] if i + half - 1 < len(nums1) else float("inf")
            vb = nums2[j + half - 1] if j + half - 1 < len(nums2) else float("inf")

            if va <= vb:
                # nums1 的前 half 個都排在第 k 名之前，安全丟棄
                return kth(i + half, j, k - half)
            return kth(i, j + half, k - half)

        total = len(nums1) + len(nums2)
        if total % 2:
            return float(kth(0, 0, total // 2 + 1))
        return (kth(0, 0, total // 2) + kth(0, 0, total // 2 + 1)) / 2'''

S["p4_partition"] = '''class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 永遠對「短的那個」做二分，複雜度才是 O(log min(m, n))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)

        # 左半邊要放的總數。用 (m+n+1)//2 讓奇數時左半邊多一個
        half = (m + n + 1) // 2

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2      # nums1 取前 i 個進左半邊
            j = half - i            # nums2 就必須取前 j 個

            l1 = nums1[i - 1] if i > 0 else float("-inf")
            r1 = nums1[i]     if i < m else float("inf")
            l2 = nums2[j - 1] if j > 0 else float("-inf")
            r2 = nums2[j]     if j < n else float("inf")

            if l1 <= r2 and l2 <= r1:          # 切對了
                if (m + n) % 2:
                    return float(max(l1, l2))  # 奇數：左半邊最大的那個
                return (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2:
                hi = i - 1          # nums1 拿太多了，往左切
            else:
                lo = i + 1          # nums1 拿太少了，往右切

        raise ValueError("輸入不是有序陣列")'''

_p4 = [S.load(k) for k in ("p4_merge", "p4_twopointer", "p4_kth", "p4_partition")]


def _p4_ref(a, b):
    m = sorted(a + b); n = len(m)
    return float(m[n // 2]) if n % 2 else (m[n // 2 - 1] + m[n // 2]) / 2


for a, b in [([1, 3], [2]), ([1, 2], [3, 4]), ([], [1]), ([2], []),
             ([0, 0], [0, 0]), ([1, 1, 1], [1, 1]), ([1, 2, 3, 4, 5], [6])]:
    e = _p4_ref(a, b)
    for s in _p4:
        assert abs(s.findMedianSortedArrays(a, b) - e) < 1e-9, ("P4", a, b)
for _ in range(4000):
    la, lb = random.randint(0, 7), random.randint(0, 7)
    if la + lb == 0:
        continue
    a = sorted(random.randint(-15, 15) for _ in range(la))
    b = sorted(random.randint(-15, 15) for _ in range(lb))
    e = _p4_ref(a, b)
    for s in _p4:
        assert abs(s.findMedianSortedArrays(a, b) - e) < 1e-9, ("P4", a, b, s)
print("P4 solutions OK")

_P4_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">A = [1, 3, 8, 9, 15]（m=5）   B = [7, 11, 18, 19, 21, 25]（n=6）   half = (5+6+1)//2 = 6</text>
            <g font-size="13" text-anchor="middle">
              <text x="34" y="62" fill="var(--text-muted)" font-size="12">A</text>
              <rect x="56" y="44" width="52" height="34" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="82" y="67" fill="var(--accent)">1</text>
              <rect x="112" y="44" width="52" height="34" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="138" y="67" fill="var(--accent)">3</text>
              <rect x="168" y="44" width="52" height="34" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="194" y="67" fill="var(--accent)">8</text>
              <rect x="232" y="44" width="52" height="34" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="258" y="67" fill="#ff8a65">9</text>
              <rect x="288" y="44" width="52" height="34" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="314" y="67" fill="#ff8a65">15</text>
            </g>
            <line x1="226" y1="34" x2="226" y2="88" stroke="var(--gold)" stroke-width="2.5"/>
            <text x="226" y="28" fill="var(--gold)" font-size="11" text-anchor="middle">i = 3</text>
            <g font-size="13" text-anchor="middle">
              <text x="34" y="134" fill="var(--text-muted)" font-size="12">B</text>
              <rect x="56" y="116" width="52" height="34" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="82" y="139" fill="var(--accent)">7</text>
              <rect x="112" y="116" width="52" height="34" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="138" y="139" fill="var(--accent)">11</text>
              <rect x="176" y="116" width="52" height="34" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="202" y="139" fill="#ff8a65">18</text>
              <rect x="232" y="116" width="52" height="34" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="258" y="139" fill="#ff8a65">19</text>
              <rect x="288" y="116" width="52" height="34" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="314" y="139" fill="#ff8a65">21</text>
              <rect x="344" y="116" width="52" height="34" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="370" y="139" fill="#ff8a65">25</text>
            </g>
            <line x1="170" y1="106" x2="170" y2="160" stroke="var(--gold)" stroke-width="2.5"/>
            <text x="170" y="100" fill="var(--gold)" font-size="11" text-anchor="middle">j = 6 − 3 = 2</text>
            <text x="430" y="62" fill="var(--accent)" font-size="12">左半邊 6 個</text>
            <text x="430" y="82" fill="var(--accent)" font-size="11">{1, 3, 8} ∪ {7, 11}… 只有 5 個 ✘</text>
            <text x="430" y="134" fill="#ff8a65" font-size="12">右半邊 5 個</text>
            <text x="20" y="196" fill="var(--text-muted)" font-size="12">檢查條件：l1 = A[i−1] = 8 ≤ r2 = B[j] = 18 ✔　　l2 = B[j−1] = 11 &gt; r1 = A[i] = 9 ✘</text>
            <text x="20" y="216" fill="var(--gold)" font-size="12">→ A 這邊拿太少了，lo = i + 1，往右再切一次</text>'''

emit({
 "num": 4, "slug": "median-of-two-sorted-arrays",
 "en": [
   "Given two sorted arrays <code>nums1</code> and <code>nums2</code> of size "
   "<code>m</code> and <code>n</code> respectively, return <strong>the median</strong> "
   "of the two sorted arrays.",
   "The overall run time complexity should be <code>O(log (m+n))</code>.",
 ],
 "zh": [
   "給定兩個<strong>已排序</strong>的陣列 <code>nums1</code> 與 <code>nums2</code>，"
   "長度分別是 <code>m</code> 和 <code>n</code>，請回傳這兩個陣列合起來之後的<strong>中位數</strong>。",
   "整體時間複雜度必須是 <code>O(log (m+n))</code>。",
 ],
 "pre": [
   ("note", "先把「中位數」的定義講死", [
     "中位數就是「把所有數字排好之後站在正中間的那個數」。總共有奇數個的時候正中間只有一個；"
     "偶數個的時候正中間有兩個，取平均。",
     ("c", """總長 5：  [1, 3, 8, 9, 15]
                    ↑  中位數 = 8

總長 6：  [1, 3, 7, 8, 9, 15]
                 ↑  ↑  中位數 = (7 + 8) / 2 = 7.5"""),
     "這題真正難的不是定義，是那句 <strong>O(log (m+n))</strong>。"
     "它把最自然的「合併起來再取中間」（O(m+n)）直接判出局，"
     "逼你去想一個<strong>根本不看大部分元素</strong>的做法。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums1 = [1, 3], nums2 = [2]
  輸出：2.00000
  說明：合併後是 [1, 2, 3]，中位數是 2。

範例 2
  輸入：nums1 = [1, 2], nums2 = [3, 4]
  輸出：2.50000
  說明：合併後是 [1, 2, 3, 4]，中位數是 (2 + 3) / 2 = 2.5。

範例 3（容易忘記的情況）
  輸入：nums1 = [], nums2 = [1]
  輸出：1.00000
  說明：其中一個陣列可以是空的。""",
 "constraints": [
   "<code>nums1.length == m</code>，<code>nums2.length == n</code>",
   "0 ≤ <code>m</code> ≤ 1000，0 ≤ <code>n</code> ≤ 1000",
   "1 ≤ <code>m + n</code> ≤ 2000（<strong>兩個都空是不會出現的</strong>，但單獨一個空會）",
   "−10⁶ ≤ <code>nums1[i]</code>, <code>nums2[i]</code> ≤ 10⁶",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<code>m + n ≤ 2000</code> 很小 —— 小到 O(m+n) 的解法在 LeetCode 上<strong>一定會過</strong>。"
       "所以這題的難度完全來自題目自己加的那條 O(log) 規定，不是來自資料規模。",
       "<code>m</code> 或 <code>n</code> 可以是 <strong>0</strong>。所有「取 nums1[0]」的寫法都要先問一句：真的有第 0 個嗎？",
       "數值有負數，所以哨兵值不能用 0 或 −1，要用 <code>float(\"-inf\")</code>。",
     ]),
     "本篇會把四種解法都寫出來，因為它們是一條清楚的思考鏈："
     "<strong>合併 → 不用真的合併 → 不用一個一個走 → 連走都不走</strong>。",
   ]),
 ],
 "idea": [
   "四種解法，一層一層往下砍：",
   ("t", ["解法", "核心想法", "時間"],
        [["一、合併排序", "把兩個接起來 sorted()", "O((m+n) log(m+n))"],
         ["二、雙指標合併", "像 merge sort 的 merge，走到中間就停", "O(m+n)"],
         ["三、遞迴找第 k 小", "每次砍掉 k/2 個，遞迴", "O(log(m+n))"],
         ["四、二分切割點", "直接二分「A 要貢獻幾個給左半邊」", "O(log min(m,n))"]]),
 ],
 "approaches": [
   ap("解法一", "直接合併再排序（先確認答案長什麼樣）", [
     "最直觀的寫法。雖然它違反題目的複雜度要求，但它是後面三個解法的<strong>正確性基準</strong> —— "
     "寫任何優化版本之前，先有一份「絕對正確但很慢」的參考實作，是解 Hard 題最划算的投資。",
     ("c", S["p4_merge"]),
     "注意 <code>float(...)</code> 不能省：奇數長度時 <code>merged[n // 2]</code> 是 int，"
     "而題目要的是浮點數。Python 這裡不會報錯，但輸出格式可能不合預期。",
   ], "O((m+n) log(m+n))", "O(m+n)", "排序主導", "合併後的新陣列"),

   ap("解法二", "雙指標合併，走到一半就停", [
     "既然只要中間那一兩個數，就沒必要把整個合併結果生出來。"
     "像 merge sort 的 merge 步驟一樣，兩個指標各指一個陣列的開頭，每次取小的往前走，"
     "數到第 <code>(m+n)//2 + 1</code> 個就可以收工。",
     ("c", """A = [1, 3, 8, 9, 15]      B = [7, 11, 18, 19, 21, 25]
total = 11（奇數），need = 11//2 + 1 = 6

第 1 步：A[0]=1  vs B[0]=7   → 取 1     cur=1
第 2 步：A[1]=3  vs B[0]=7   → 取 3     cur=3
第 3 步：A[2]=8  vs B[0]=7   → 取 7     cur=7
第 4 步：A[2]=8  vs B[1]=11  → 取 8     cur=8
第 5 步：A[3]=9  vs B[1]=11  → 取 9     cur=9
第 6 步：A[4]=15 vs B[1]=11  → 取 11    cur=11  ← 停

奇數 → 答案就是 cur = 11
（B 後面的 18、19、21、25 完全沒被碰到）"""),
     ("c", S["p4_twopointer"]),
     "<code>prev</code> 存的是上一步取到的值，偶數長度時剛好就是中間兩個裡比較小的那個。"
     "這個「多留一個前值」的小技巧，在所有「走到第 k 個」的題目都會用到。",
     "<strong>條件 <code>i &lt; m and (j &gt;= n or nums1[i] &lt;= nums2[j])</code> 的順序不能換。</strong>"
     "先確認 <code>i &lt; m</code>，再看 <code>j &gt;= n</code>（B 空了就只能取 A），"
     "最後才比大小。Python 的 <code>and</code>／<code>or</code> 短路求值讓這一行同時處理了三種情況。",
   ], "O(m+n)", "O(1)", "實際只走 (m+n)/2 步", "只用幾個變數"),

   ap("解法三", "遞迴找第 k 小：每次砍掉 k/2 個", [
     "要突破 O(m+n)，必須做到「<strong>一次丟掉一大塊</strong>」而不是「一次丟掉一個」。",
     "把問題改寫成更一般的形式：<strong>在兩個有序陣列裡找第 k 小的數</strong>。"
     "中位數只是 k = (m+n+1)//2 的特例（偶數時再多問一次 k+1）。",
     ("h", "為什麼可以安全地砍掉 k/2 個？"),
     "假設我們各往前看 <code>half = k//2</code> 個元素，"
     "比較 <code>A[i+half−1]</code> 和 <code>B[j+half−1]</code>。若 <code>A</code> 那個比較小：",
     ("c", """A: [ a1  a2  ...  a_half ] a_half+1 ...
              ↑ 最大的是 A[i+half-1]

B: [ b1  b2  ...  b_half ] b_half+1 ...
              ↑ 最大的是 B[j+half-1]  ≥ A[i+half-1]

問：A 的前 half 個，有沒有可能有人是「第 k 小」？
答：沒有。以 A[i+half-1] 為例，排在它前面的最多有
      A 自己的 half-1 個  +  B 裡比它小的（最多 half-1 個，因為 B[j+half-1] 比它大）
    = 2*half - 2  ≤  k - 2

    所以 A[i+half-1] 的名次 ≤ k-1，它和它前面的全都排在第 k 名之前。
    → 安全丟棄，k 減去 half，繼續找。"""),
     "這段推導是整題的靈魂。<code>2*half − 2 ≤ k − 2</code> 這個不等式，"
     "正是 <code>half = k//2</code>（而不是 <code>k//2 + 1</code>）的原因。",
     ("c", S["p4_kth"]),
     ("h", "兩個容易寫錯的地方"),
     ("ul", [
       "<strong>越界要填 <code>+inf</code> 而不是直接 return。</strong>"
       "若 <code>A</code> 剩下不到 half 個，我們不能丟 A 的東西（可能不夠丟），"
       "填 <code>inf</code> 會讓程式自動去丟 B 那邊 —— 一行就處理完這個邊界。",
       "<strong><code>k == 1</code> 一定要當成終止條件。</strong>"
       "因為 <code>half = 1//2 = 0</code>，不擋下來就會無限遞迴。",
     ]),
     "遞迴深度是 O(log k)，k 最大 2000，所以最多約 11 層，不會爆堆疊。",
   ], "O(log(m+n))", "O(log(m+n))", "每層 k 砍一半", "遞迴堆疊；改成迴圈可以降到 O(1)"),

   ap("解法四", "二分切割點（標準最佳解）", [
     "換一個角度：<strong>不要找第 k 小，直接找那一刀。</strong>",
     "把兩個陣列各切一刀，左邊全部丟進「左半邊」，右邊全部丟進「右半邊」。"
     "如果我們能讓這一刀滿足兩個條件，中位數就在刀口上：",
     ("ol", [
       "<strong>數量對</strong>：左半邊剛好有 <code>(m+n+1)//2</code> 個元素。",
       "<strong>大小對</strong>：左半邊<strong>任何一個</strong>都 ≤ 右半邊<strong>任何一個</strong>。",
     ]),
     "條件 1 讓我們只需要決定一個變數：<code>i</code>（A 貢獻幾個給左半邊）。"
     "因為一旦 <code>i</code> 定了，<code>j = half − i</code> 就被綁死了。",
     "條件 2 看起來要比很多次，其實只要比兩對：因為兩邊各自有序，"
     "左半邊最大的只可能是 <code>A[i−1]</code> 或 <code>B[j−1]</code>，"
     "右半邊最小的只可能是 <code>A[i]</code> 或 <code>B[j]</code>。所以只要檢查："
     "<code>A[i−1] ≤ B[j]</code> 而且 <code>B[j−1] ≤ A[i]</code>。",
     ("fig", _P4_FIG, "0 0 640 236"),
     "而 <code>i</code> 和這兩個條件是<strong>單調</strong>的：<code>i</code> 越大，"
     "<code>A[i−1]</code> 越大、<code>B[j]</code> 越小，所以 <code>A[i−1] ≤ B[j]</code> "
     "從成立變成不成立只會發生一次。單調 → 可以二分。",
     ("c", S["p4_partition"]),
     ("h", "為什麼是 <code>(m+n+1)//2</code> 而不是 <code>(m+n)//2</code>？"),
     ("c", """m+n = 11（奇數），half = (11+1)//2 = 6
  左半邊 6 個，右半邊 5 個 → 左邊比較多 → 答案 = 左半邊最大的 = max(l1, l2)

m+n = 12（偶數），half = (12+1)//2 = 6
  左右各 6 個 → 答案 = (左半邊最大 + 右半邊最小) / 2 = (max(l1,l2) + min(r1,r2)) / 2

用 +1 的好處：奇偶兩種情況共用同一個 half，
奇數時左邊永遠多一個，答案就永遠是 max(l1, l2)，不必分兩套下標公式。"""),
     ("h", "為什麼一定要先確保 nums1 是短的？"),
     "二分的範圍是 <code>[0, m]</code>，所以複雜度是 O(log m)。"
     "交換之後 m 是兩者中較小的，得到 O(log min(m,n))。"
     "更重要的是<strong>正確性</strong>：如果 A 比 B 長，<code>j = half − i</code> 有可能算出負數或超過 n，"
     "所有 <code>nums2[j]</code> 都會炸掉。交換這一步不是優化，是必要條件。",
     ("h", "±inf 哨兵在做什麼"),
     "<code>i == 0</code> 表示 A 完全不貢獻給左半邊，此時「A 在左半邊的最大值」不存在，"
     "設成 <code>−inf</code> 讓 <code>l1 ≤ r2</code> 自動成立。"
     "<code>i == m</code> 同理設 <code>+inf</code>。"
     "有了這四個哨兵，「其中一個陣列是空的」這個邊界就完全不用特別處理了 —— "
     "這是很優雅的一點，值得記下來。",
   ], "O(log min(m, n))", "O(1)", "只在短陣列上二分", "只用常數個變數", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "程式碼行數", "面試評價"],
   [["一、合併排序", "O((m+n)log(m+n))", "O(m+n)", "5", "當作正確性基準可以，當答案不行"],
    ["二、雙指標", "O(m+n)", "O(1)", "15", "能過測資，但沒達到題目要求"],
    ["三、遞迴第 k 小", "O(log(m+n))", "O(log(m+n))", "20", "達標；推導漂亮，遞迴容易寫錯"],
    ["四、二分切割", "O(log min(m,n))", "O(1)", "25", "標準最佳解，但邊界最多"]]),
 "post": [
   ("note", "面試時該寫哪一個？", [
     "誠實的建議：<strong>先講解法二，再寫解法四</strong>。",
     "先用 30 秒說明「合併只要走一半就夠了，O(m+n)、O(1) 空間」，證明你能想到乾淨的解；"
     "然後說「但題目要 O(log)，所以要換成二分切割」，再開始寫解法四。"
     "這樣就算解法四的邊界寫卡住，面試官也已經看到你有一個可用的答案了。",
     "不要一上來就默寫解法四 —— 這題的 ±inf 哨兵和 <code>half</code> 公式太容易背錯，"
     "背錯又講不出為什麼，比寫慢一點還糟。",
   ]),
 ],
 "edges": [
   "<strong>其中一個陣列是空的</strong>：<code>([], [1])</code> → 1.0。解法四靠哨兵自動處理，解法一二靠 Python 的空 list 語意。",
   "<strong>兩個陣列不重疊</strong>：<code>([1,2], [3,4])</code> 和 <code>([3,4], [1,2])</code> 都要對。",
   "<strong>全部相同</strong>：<code>([0,0], [0,0])</code> → 0.0。比較用 <code>≤</code> 而不是 <code>&lt;</code>，否則會死循環。",
   "<strong>長度差很多</strong>：<code>([1,2,3,4,5], [6])</code> → 3.0。這會逼出「短的那邊全進左半邊或全進右半邊」的極端切法。",
   "<strong>奇偶都要測</strong>：m+n 的奇偶走的是完全不同的 return 分支。",
   "<strong>負數</strong>：哨兵必須是 <code>float(\"-inf\")</code>，寫 0 或 −1 會在負數測資上錯。",
 ],
 "follow": [
   ("h", "追問一：如果不是兩個陣列，是 k 個有序陣列的中位數？"),
   "二分切割法推不上去（k 個切點沒辦法只用一個變數綁死）。這時候換一個維度二分："
   "<strong>直接二分答案的數值</strong>。猜一個值 <code>x</code>，用二分搜尋算出所有陣列裡 ≤ x 的元素總共幾個，"
   "再根據這個計數調整 x。複雜度 O(k · log(值域) · log(最長陣列長度))。這也是第 378 題的標準解法。",
   ("h", "追問二：如果陣列在硬碟上，不能隨機存取？"),
   "解法四需要 <code>A[i]</code> 這種隨機存取，硬碟上代價很高；解法二只需要循序讀，反而比較適合。"
   "<strong>複雜度不是唯一標準，存取模式也是。</strong>這是很常見的 follow-up 陷阱。",
   ("h", "追問三：資料會一直更新，要隨時能查中位數？"),
   "那就不是這題了，而是第 295 題（Find Median from Data Stream）："
   "用一個最大堆放小的一半、一個最小堆放大的一半，插入 O(log n)、查詢 O(1)。",
 ],
 "related": [
   "<strong>第 215 題 Kth Largest Element in an Array</strong> —— 「第 k 小」這個抽象化的單陣列版本",
   "<strong>第 295 題 Find Median from Data Stream</strong> —— 雙堆維護動態中位數",
   "<strong>第 378 題 Kth Smallest Element in a Sorted Matrix</strong> —— 二分答案的典型題",
 ],
 "check": [
   "解法四裡 <code>half</code> 為什麼要寫 <code>(m+n+1)//2</code>？改成 <code>(m+n)//2</code> 會在什麼輸入上錯？",
   "如果拿掉「讓 nums1 是較短的那個」那兩行，什麼輸入會讓程式崩潰？崩在哪一行？",
   "解法三裡 <code>half = k//2</code>，如果改成 <code>k//2 + 1</code> 會發生什麼事？請用 k=3 舉一個具體例子。",
   "四個哨兵 <code>±inf</code> 分別對應哪一種邊界？把它們全部改成 0，哪一筆測資會錯？",
 ],
})
print("P4 written")
