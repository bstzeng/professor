# -*- coding: utf-8 -*-
"""第 33–35 題。"""
import random, bisect
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(33)

# ==================== 33. Search in Rotated Sorted Array ====================
S["p33_one"] = '''class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid

            # 關鍵：mid 一定會落在「左半有序段」或「右半有序段」其中之一
            if nums[lo] <= nums[mid]:
                # 左半段 [lo, mid] 是有序的
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1        # target 在這個有序段裡
                else:
                    lo = mid + 1
            else:
                # 右半段 [mid, hi] 是有序的
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return -1'''

S["p33_pivot"] = '''class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        # 第 1 步：找旋轉點（最小值的索引）
        lo, hi = 0, n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1        # 最小值在右半
            else:
                hi = mid            # 最小值在左半（含 mid）
        pivot = lo

        # 第 2 步：在「旋轉過的座標系」上做標準二分搜尋
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            real = (mid + pivot) % n      # 映射回實際的索引
            if nums[real] == target:
                return real
            if nums[real] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1'''

_p33 = [S.load(k) for k in ("p33_one", "p33_pivot")]
for c, t in [([4, 5, 6, 7, 0, 1, 2], 0), ([4, 5, 6, 7, 0, 1, 2], 3),
             ([1], 0), ([1], 1), ([3, 1], 1), ([5, 1, 3], 3), ([1, 3], 3)]:
    e = c.index(t) if t in c else -1
    for sol in _p33:
        g = sol.search(list(c), t)
        assert (g == -1 and e == -1) or c[g] == t, ("P33", c, t, sol, g, e)
for _ in range(5000):
    k = random.randint(1, 9)
    base = sorted(random.sample(range(-15, 15), k))
    r = random.randint(0, k - 1)
    c = base[r:] + base[:r]
    t = random.randint(-16, 15)
    e = c.index(t) if t in c else -1
    for sol in _p33:
        g = sol.search(list(c), t)
        assert g == e, ("P33", c, t, sol, g, e)
print("P33 solutions OK")

_P33_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">旋轉後的陣列 = 兩段各自遞增的序列。不管 mid 落在哪，一定有一半是完整有序的。</text>
            <g>
              <polyline points="50,178 110,158 170,138 230,118" fill="none" stroke="var(--accent)" stroke-width="2.5"/>
              <polyline points="290,196 350,176 410,156 470,136 530,116" fill="none" stroke="#ff8a65" stroke-width="2.5"/>
              <line x1="40" y1="206" x2="600" y2="206" stroke="var(--text-muted)"/>
              <circle cx="50" cy="178" r="4" fill="var(--accent)"/><circle cx="110" cy="158" r="4" fill="var(--accent)"/>
              <circle cx="170" cy="138" r="4" fill="var(--accent)"/><circle cx="230" cy="118" r="4" fill="var(--accent)"/>
              <circle cx="290" cy="196" r="4" fill="#ff8a65"/><circle cx="350" cy="176" r="4" fill="#ff8a65"/>
              <circle cx="410" cy="156" r="4" fill="#ff8a65"/><circle cx="470" cy="136" r="4" fill="#ff8a65"/>
              <circle cx="530" cy="116" r="4" fill="#ff8a65"/>
            </g>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="50" y="224">0</text><text x="110" y="224">1</text><text x="170" y="224">2</text>
              <text x="230" y="224">3</text><text x="290" y="224">4</text><text x="350" y="224">5</text>
              <text x="410" y="224">6</text><text x="470" y="224">7</text><text x="530" y="224">8</text>
            </g>
            <g font-size="12" text-anchor="middle">
              <text x="50" y="168" fill="var(--accent)">4</text><text x="110" y="148" fill="var(--accent)">5</text>
              <text x="170" y="128" fill="var(--accent)">6</text><text x="230" y="108" fill="var(--accent)">7</text>
              <text x="290" y="212" fill="#ff8a65" opacity="0">.</text>
              <text x="290" y="186" fill="#ff8a65">0</text><text x="350" y="166" fill="#ff8a65">1</text>
              <text x="410" y="146" fill="#ff8a65">2</text><text x="470" y="126" fill="#ff8a65">3</text>
              <text x="530" y="106" fill="#ff8a65">4</text>
            </g>
            <line x1="260" y1="90" x2="260" y2="214" stroke="var(--gold)" stroke-width="2" stroke-dasharray="5 4"/>
            <text x="260" y="82" fill="var(--gold)" font-size="11" text-anchor="middle">旋轉點</text>
            <text x="20" y="252" fill="var(--text-muted)" font-size="12">mid 在左段（藍）→ nums[lo] ≤ nums[mid]，左半 [lo, mid] 有序</text>
            <text x="20" y="274" fill="var(--text-muted)" font-size="12">mid 在右段（橘）→ nums[lo] &gt; nums[mid]，右半 [mid, hi] 有序</text>
            <text x="20" y="300" fill="var(--gold)" font-size="12">判斷 target 在不在「那個有序的一半」裡，就知道要往哪邊縮。</text>'''

emit({
 "num": 33, "slug": "search-in-rotated-sorted-array",
 "en": [
   "There is an integer array <code>nums</code> sorted in ascending order (with "
   "<strong>distinct</strong> values). Prior to being passed to your function, "
   "<code>nums</code> is possibly <strong>rotated</strong> at an unknown pivot index.",
   "Given the array <code>nums</code> <strong>after</strong> the possible rotation and an "
   "integer <code>target</code>, return the index of <code>target</code> if it is in "
   "<code>nums</code>, or <code>-1</code> if it is not.",
   "You must write an algorithm with <code>O(log n)</code> runtime complexity.",
 ],
 "zh": [
   "有一個<strong>元素互不相同</strong>的升序整數陣列 <code>nums</code>，"
   "在傳給你之前，它可能在某個未知的位置被<strong>旋轉</strong>過"
   "（例如 <code>[0,1,2,4,5,6,7]</code> 旋轉成 <code>[4,5,6,7,0,1,2]</code>）。",
   "給你旋轉<strong>之後</strong>的陣列和一個 <code>target</code>，"
   "回傳 <code>target</code> 的索引；不存在就回 <code>-1</code>。",
   "你的演算法必須是 <code>O(log n)</code>。",
 ],
 "pre": [
   ("note", "旋轉陣列的結構：兩段遞增", [
     ("c", """原本：      [0, 1, 2, 4, 5, 6, 7]
旋轉 4 格： [4, 5, 6, 7, 0, 1, 2]
             └─ 段 A ─┘  └段 B┘

性質：
  1. 段 A 和段 B 各自都是嚴格遞增的
  2. 段 A 的「所有」元素都 > 段 B 的「所有」元素
  3. 只有一個「斷點」（從 7 掉到 0 的地方）

關鍵洞察：
  不管 mid 落在哪裡，
  [lo, mid] 和 [mid, hi] 這兩半「至少有一半是完整有序的」。

  因為斷點只有一個，它不可能同時在兩半裡。

而「有序的那一半」可以用一般的範圍判斷確認 target 在不在裡面 ——
在裡面就往那邊縮，不在就往另一邊縮。
每次砍一半 -> O(log n)。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [4,5,6,7,0,1,2], target = 0
  輸出：4

範例 2
  輸入：nums = [4,5,6,7,0,1,2], target = 3
  輸出：-1

範例 3
  輸入：nums = [1], target = 0
  輸出：-1""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 5000",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
   "<code>nums</code> 的<strong>所有值互不相同</strong>",
   "<code>nums</code> 是一個升序陣列旋轉某個位置後的結果（<strong>也可能沒旋轉</strong>）",
   "−10⁴ ≤ <code>target</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>「所有值互不相同」是關鍵。</strong>"
       "有重複值的話（第 81 題），<code>nums[lo] == nums[mid]</code> 時無法判斷哪一半有序，"
       "最壞會退化成 O(n)。這一條讓我們能穩穩地 O(log n)。",
       "<strong>「也可能沒旋轉」</strong>：<code>[1,2,3]</code> 是合法輸入。"
       "此時整個陣列就是「段 A」，判斷式要能處理（<code>nums[lo] &lt;= nums[mid]</code> 永遠成立，"
       "退化成普通二分搜尋）。",
       "<strong>要求 O(log n)</strong> —— 明確排除線性掃描。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P33_FIG, "0 0 640 312"),
 ],
 "approaches": [
   ap("解法一", "一次二分（最推薦）", [
     ("c", S["p33_one"]),
     ("h", "為什麼 <code>nums[lo] &lt;= nums[mid]</code> 就表示左半有序？"),
     ("c", """如果 [lo, mid] 裡有斷點，那麼 nums[lo] 在斷點前（較大的那段），
nums[mid] 在斷點後（較小的那段），所以 nums[lo] > nums[mid]。

反過來說，nums[lo] <= nums[mid] 就表示 [lo, mid] 裡沒有斷點
-> 這一段是完整遞增的。

為什麼用 <= 而不是 < ？
    當 lo == mid 時（區間只有一兩個元素），兩者相等。
    這時「只有一個元素」的區間當然是有序的，所以要算成 True。
    寫 < 的話 [3, 1] 找 1 會出錯：
        lo=0, hi=1, mid=0
        nums[0]=3 < nums[0]=3 ? 否 -> 走 else，判斷右半 [0,1] 有序
        nums[0]=3 < 1 <= nums[1]=1 ? 3 < 1 不成立 -> hi = -1
        回傳 -1  ✘ 錯了，答案是 1

    用 <= 就正確：
        nums[0] <= nums[0] ✔ -> 左半 [0,0] 有序
        nums[0]=3 <= 1 < nums[0]=3 ? 否 -> lo = 1
        下一輪 mid=1，nums[1]==1 ✔ 回傳 1"""),
     ("h", "四個判斷式的邊界，逐一確認"),
     ("c", """左半有序時：  if nums[lo] <= target < nums[mid]
    左邊用 <=  ：target 可能剛好等於 nums[lo]
    右邊用 <   ：target == nums[mid] 已經在最上面 return 了

右半有序時：  if nums[mid] < target <= nums[hi]
    左邊用 <   ：同上
    右邊用 <=  ：target 可能剛好等於 nums[hi]

這四個等號如果擺錯，會在「target 剛好在邊界」的測資上失敗。
建議記法：「開區間的那一端是 mid（因為 mid 已經檢查過了）」。"""),
     "<strong>這是最推薦的寫法</strong>：只掃一遍、13 行、沒有額外的座標映射。"
     "但它的判斷式密度很高，寫的時候要一個一個確認。",
   ], "O(log n)", "O(1)", "每輪砍一半", "只用三個下標", optimal=True),

   ap("解法二", "先找旋轉點，再標準二分（思路最清楚）", [
     "把問題拆成兩個獨立的、各自簡單的子問題。",
     ("c", S["p33_pivot"]),
     ("h", "第 1 步：找旋轉點（最小值的位置）"),
     ("c", """判斷式是 nums[mid] > nums[hi]，不是 nums[mid] > nums[lo]！

為什麼？
    nums[mid] > nums[hi]
        -> mid 在「大的那段」(段 A)，最小值一定在 mid 右邊
        -> lo = mid + 1

    nums[mid] <= nums[hi]
        -> mid 在「小的那段」(段 B)，最小值在 mid 或它左邊
        -> hi = mid       （注意不是 mid - 1，mid 本身可能就是答案）

為什麼不能跟 nums[lo] 比？
    [3, 4, 5, 1, 2]，lo=0, hi=4, mid=2
        nums[2]=5 > nums[0]=3  -> 看似「mid 在大段」，對
    但 [1, 2, 3, 4, 5]（沒旋轉），lo=0, hi=4, mid=2
        nums[2]=3 > nums[0]=1  -> 判斷成「最小值在右邊」  ✘ 錯了

    跟 hi 比就不會有這個問題：
        nums[2]=3 <= nums[4]=5  -> hi = 2，繼續往左收 ✔

「和右端點比」是找旋轉點的標準寫法，值得背下來。

迴圈用 while lo < hi（不是 <=），
結束時 lo == hi 就是答案 —— 這是「找邊界」型二分的標準骨架。"""),
     ("h", "第 2 步：在旋轉座標系上二分"),
     ("c", """找到 pivot 之後，「邏輯上的第 i 個元素」是 nums[(i + pivot) % n]。

    nums = [4,5,6,7,0,1,2]，pivot = 4
    邏輯索引 0 -> 實際索引 (0+4)%7 = 4 -> 值 0
    邏輯索引 1 -> (1+4)%7 = 5 -> 值 1
    邏輯索引 2 -> (2+4)%7 = 6 -> 值 2
    邏輯索引 3 -> (3+4)%7 = 0 -> 值 4
    ...
    邏輯上就是排好的 [0,1,2,4,5,6,7] ✔

所以在邏輯索引上做標準二分，
只要每次存取時做一次 (mid + pivot) % n 的映射即可。

好處：第 2 步的二分是「教科書版」的，沒有任何特殊判斷。"""),
     "<strong>優點</strong>：每一步都是標準工具，不容易寫錯，也容易解釋。",
     "<strong>缺點</strong>：兩次二分（常數大兩倍）、多一個模運算。"
     "但複雜度還是 O(log n)。",
     "<strong>而且找旋轉點這個子程序本身就是第 153 題</strong>，"
     "學會之後可以直接用在那題上。",
   ], "O(log n)", "O(1)", "兩次二分", "只用幾個下標"),
 ],
 "compare": (["解法", "時間", "二分次數", "好寫程度", "備註"],
   [["一、一次二分", "O(log n)", "1", "★★★☆☆", "最短，判斷式要小心"],
    ["二、找旋轉點 + 標準二分", "O(log n)", "2", "★★★★☆", "拆成兩個已知問題"]]),
 "edges": [
   "<strong>沒有旋轉</strong>：<code>([1,2,3], 3)</code> → 2。退化成普通二分。",
   "<strong>單一元素</strong>：<code>([1], 1)</code> → 0；<code>([1], 0)</code> → −1。",
   "<strong>兩個元素</strong>：<code>([3,1], 1)</code> → 1。"
   "<strong>這是最能抓出 <code>&lt;=</code> vs <code>&lt;</code> 錯誤的測資。</strong>",
   "<strong>target 是旋轉點</strong>：<code>([4,5,6,7,0,1,2], 0)</code> → 4。",
   "<strong>target 在頭或尾</strong>：<code>([4,5,6,7,0,1,2], 4)</code> → 0；"
   "<code>([4,5,6,7,0,1,2], 2)</code> → 6。考驗四個等號的位置。",
   "<strong>target 不存在</strong>：<code>([4,5,6,7,0,1,2], 3)</code> → −1。"
   "3 落在兩段「之間」，最容易誤判。",
   "<strong>旋轉一格</strong>：<code>([5,1,3], 3)</code> → 2。",
 ],
 "follow": [
   ("h", "追問一：如果有重複值呢？"),
   "那是第 81 題。問題出在 <code>nums[lo] == nums[mid]</code> 時無法判斷哪一半有序：",
   ("c", """[1, 1, 1, 0, 1]，lo=0, hi=4, mid=2
    nums[0]=1, nums[2]=1, nums[4]=1  全都一樣
    完全看不出斷點在左邊還是右邊。

標準的處理是：遇到 nums[lo] == nums[mid] 時就 lo += 1
（放棄這一格，只損失一個元素，不影響正確性）。

代價：最壞情況（全部相同）退化成 O(n)。
而且這是不可避免的 —— 可以證明有重複值時，
任何演算法在最壞情況下都需要 O(n)。"""),
   ("h", "追問二：如果要找最小值呢？"),
   "就是解法二的第 1 步，也就是第 153 題。核心是「和右端點比」。",
   ("h", "追問三：為什麼二分搜尋在旋轉陣列上還能用？"),
   "二分搜尋的本質<strong>不是「陣列有序」，而是「能在 O(1) 內判斷答案在哪一半」</strong>。"
   "旋轉陣列雖然整體無序，但它有足夠的結構讓我們做出這個判斷。",
   "<strong>這個觀點很重要</strong>，它能幫你認出很多「看起來不能二分但其實可以」的題目：",
   ("ul", [
     "<strong>第 162 題 Find Peak Element</strong>：無序陣列，但「往高處走」一定能找到峰",
     "<strong>第 4 題 Median of Two Sorted Arrays</strong>：二分「切割點」而不是值",
     "<strong>二分答案</strong>：對答案本身二分，用一個 check 函式判斷方向",
   ]),
 ],
 "related": [
   "<strong>第 81 題 Search in Rotated Sorted Array II</strong> —— 有重複值的版本",
   "<strong>第 153／154 題 Find Minimum in Rotated Sorted Array</strong> —— 只找旋轉點",
   "<strong>第 162 題 Find Peak Element</strong> —— 「無序也能二分」的另一例",
   "<strong>第 35 題 Search Insert Position</strong> —— 二分的基本功",
 ],
 "check": [
   "為什麼判斷左半有序要用 <code>nums[lo] &lt;= nums[mid]</code> 而不是 <code>&lt;</code>？"
   "請用 <code>([3,1], 1)</code> 追一遍。",
   "找旋轉點時為什麼要和 <code>nums[hi]</code> 比而不是 <code>nums[lo]</code>？舉一個會出錯的輸入。",
   "四個判斷式的等號位置（<code>&lt;=</code> vs <code>&lt;</code>）各自對應什麼？",
   "二分搜尋真正需要的條件是什麼？為什麼「有序」不是必要的？",
 ],
})
print("P33 written")

# ==================== 34. Find First and Last Position ====================
S["p34_manual"] = '''class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(t: int) -> int:
            """第一個 >= t 的位置（找不到就回 len(nums)）"""
            lo, hi = 0, len(nums)        # 注意 hi 是 len，不是 len-1
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < t:
                    lo = mid + 1
                else:
                    hi = mid             # mid 可能就是答案，不能跳過
            return lo

        left = lower_bound(target)
        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        # 第一個 > target 的位置 = 第一個 >= target+1 的位置
        right = lower_bound(target + 1) - 1
        return [left, right]'''

S["p34_bisect"] = '''import bisect

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)    # 第一個 >= target
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        right = bisect.bisect_right(nums, target) - 1   # 最後一個 == target
        return [left, right]'''

S["p34_twobin"] = '''class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find(first: bool) -> int:
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] == target:
                    ans = mid                 # 先記下來
                    if first:
                        hi = mid - 1          # 繼續往左找更早的
                    else:
                        lo = mid + 1          # 繼續往右找更晚的
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            return ans

        return [find(True), find(False)]'''

_p34 = [S.load(k) for k in ("p34_manual", "p34_bisect", "p34_twobin")]


def _p34_ref(nums, t):
    idx = [i for i, v in enumerate(nums) if v == t]
    return [idx[0], idx[-1]] if idx else [-1, -1]


for c, t in [([5, 7, 7, 8, 8, 10], 8), ([5, 7, 7, 8, 8, 10], 6), ([], 0),
             ([1], 1), ([1], 2), ([2, 2], 2), ([1, 2, 3], 1), ([1, 2, 3], 3)]:
    e = _p34_ref(c, t)
    for sol in _p34:
        assert sol.searchRange(list(c), t) == e, ("P34", c, t, sol)
for _ in range(5000):
    c = sorted(random.randint(-5, 5) for _ in range(random.randint(0, 10)))
    t = random.randint(-6, 6)
    e = _p34_ref(c, t)
    for sol in _p34:
        assert sol.searchRange(list(c), t) == e, ("P34", c, t, sol)
print("P34 solutions OK")

emit({
 "num": 34, "slug": "find-first-and-last-position-of-element-in-sorted-array",
 "en": [
   "Given an array of integers <code>nums</code> sorted in non-decreasing order, find the "
   "starting and ending position of a given <code>target</code> value.",
   "If <code>target</code> is not found in the array, return <code>[-1, -1]</code>.",
   "You must write an algorithm with <code>O(log n)</code> runtime complexity.",
 ],
 "zh": [
   "給你一個<strong>非遞減排序</strong>的整數陣列 <code>nums</code> 和一個目標值 <code>target</code>，"
   "找出 <code>target</code> 出現的<strong>第一個位置和最後一個位置</strong>。",
   "如果 <code>target</code> 不在陣列裡，回傳 <code>[-1, -1]</code>。",
   "演算法必須是 <code>O(log n)</code>。",
 ],
 "pre": [
   ("note", "這題就是在考 lower_bound / upper_bound", [
     ("c", """兩個最重要的二分搜尋變體：

  lower_bound(t) = 第一個 >= t 的位置
  upper_bound(t) = 第一個 >  t 的位置

有了它們，這題就是兩行：

  first = lower_bound(target)
  last  = upper_bound(target) - 1

nums = [5, 7, 7, 8, 8, 10]，target = 8
       索引 0  1  2  3  4  5

  lower_bound(8) = 3    （第一個 >= 8）
  upper_bound(8) = 5    （第一個 > 8，也就是 10 的位置）
  答案 = [3, 5 - 1] = [3, 4] ✔

有用的恆等式：
  upper_bound(t) == lower_bound(t + 1)      （整數才成立）
  出現次數 = upper_bound(t) - lower_bound(t)

Python 的 bisect 模組：
  bisect.bisect_left  == lower_bound
  bisect.bisect_right == upper_bound（也叫 bisect）"""),
     "<strong>「找到某個值」和「找到某個邊界」是兩種不同的二分搜尋。</strong>"
     "前者用 <code>while lo &lt;= hi</code> + 找到就 return；"
     "後者用 <code>while lo &lt; hi</code> + 收斂到唯一一點。"
     "把這兩個骨架分清楚，二分搜尋就不會再寫錯。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [5,7,7,8,8,10], target = 8
  輸出：[3,4]

範例 2
  輸入：nums = [5,7,7,8,8,10], target = 6
  輸出：[-1,-1]

範例 3
  輸入：nums = [], target = 0
  輸出：[-1,-1]""",
 "constraints": [
   "0 ≤ <code>nums.length</code> ≤ 10⁵（<strong>可以是空陣列</strong>）",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
   "<code>nums</code> 是<strong>非遞減</strong>排序的",
   "−10⁹ ≤ <code>target</code> ≤ 10⁹",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>陣列可以是空的</strong>。<code>lower_bound</code> 會回傳 0，"
       "然後 <code>left == len(nums)</code> 這個檢查擋下來。",
       "<strong>要求 O(log n)</strong> —— 所以「先二分找到一個，再往兩邊線性掃」是不行的。"
       "全部相同的陣列（<code>[8,8,8,...,8]</code>，10⁵ 個）會讓那種寫法變成 O(n)。"
       "<strong>這是本題最常見的陷阱。</strong>",
       "<strong>值域到 ±10⁹</strong>，所以 <code>lower_bound(target + 1)</code> "
       "在 <code>target == 10⁹</code> 時會是 <code>10⁹ + 1</code> —— "
       "Python 沒問題，但在 C/Java 裡要注意不要溢位（用 long 或改用 upper_bound）。",
     ]),
   ]),
 ],
 "idea": [
   "三種寫法，本質都是「找邊界」而不是「找元素」。",
 ],
 "approaches": [
   ap("解法一", "自己寫 lower_bound（最該掌握的版本）", [
     ("c", S["p34_manual"]),
     ("h", "lower_bound 的三個關鍵，一個都不能改"),
     ("c", """1. hi 初始是 len(nums)，不是 len(nums) - 1

   因為答案的範圍是 [0, n]，n 表示「全部都 < t，插在最後面」。
   寫 len-1 的話永遠回不了 n，空陣列也會出錯。

2. while lo < hi（不是 <=）

   這是「收斂到一點」的骨架。
   結束時 lo == hi，那一點就是答案。
   寫 <= 會死循環（因為 hi = mid 可能讓區間不縮小）。

3. else 分支是 hi = mid（不是 mid - 1）

   當 nums[mid] >= t 時，mid「本身可能就是答案」，
   不能把它排除掉。

   而 if 分支是 lo = mid + 1，因為 nums[mid] < t
   表示 mid 確定不是答案，可以排除。

這三點是配套的：hi = mid 不縮小上界，
所以必須用 lo < hi 而不是 <=；
而 mid = (lo+hi)//2 向下取整保證了 mid < hi，
所以 hi = mid 一定會讓區間變小，不會死循環。"""),
     ("h", "為什麼可以用 <code>lower_bound(target + 1) - 1</code> 找最後一個？"),
     ("c", """lower_bound(target + 1) = 第一個 >= target+1 的位置
                        = 第一個 > target 的位置（整數）
                        = upper_bound(target)

減 1 就是「最後一個 == target」的位置。

nums = [5,7,7,8,8,10]，target = 8
    lower_bound(9) = 5（值 10 的位置）
    5 - 1 = 4 ✔

好處：只要寫一個 lower_bound 就夠了，不用再寫一個 upper_bound。
（兩個函式長得很像，寫兩次容易抄錯一個等號。）"""),
     "<strong>找不到的判斷</strong>：<code>left == len(nums)</code>（全部都比 target 小）"
     "<strong>或</strong> <code>nums[left] != target</code>（插入位置上不是 target）。"
     "兩個條件缺一不可，而且順序不能換（Python 的短路求值避免了 IndexError）。",
   ], "O(log n)", "O(1)", "兩次二分", "只用幾個下標", optimal=True),

   ap("解法二", "用 bisect 模組（Python 的正解）", [
     ("c", S["p34_bisect"]),
     ("c", """bisect.bisect_left(a, x)   第一個 >= x 的位置（lower_bound）
bisect.bisect_right(a, x)  第一個 >  x 的位置（upper_bound）
bisect.bisect              就是 bisect_right 的別名

記法：
    bisect_left  = 把 x 插在「所有等於 x 的元素的左邊」
    bisect_right = 把 x 插在「所有等於 x 的元素的右邊」

    a = [5,7,7,8,8,10]
    bisect_left(a, 8)  = 3   [5,7,7,|8,8,10]
    bisect_right(a, 8) = 5   [5,7,7,8,8,|10]

出現次數 = bisect_right(a,x) - bisect_left(a,x) = 5 - 3 = 2 ✔"""),
     "<strong>實務上就該這樣寫。</strong>"
     "但面試時建議先寫解法一，證明你知道它在做什麼，再說「Python 有 bisect 可以直接用」。",
     "<strong>bisect 的常見誤用</strong>：忘了檢查 <code>nums[left] != target</code>。"
     "<code>bisect_left</code> 回傳的是「插入位置」，不保證那裡真的有 target。",
   ], "O(log n)", "O(1)", "兩次二分（C 實作，常數很小）", "—"),

   ap("解法三", "找到之後繼續往一邊逼（不用 lower_bound）", [
     "如果一時想不起 <code>lower_bound</code> 的骨架，這個寫法用的是熟悉的"
     "「<code>while lo &lt;= hi</code> + 找到就 return」骨架，只是<strong>找到之後不 return，"
     "先記下來再繼續往一邊找</strong>。",
     ("c", S["p34_twobin"]),
     ("c", """找第一個（first = True）：
    nums = [5,7,7,8,8,10]，target = 8

    lo=0, hi=5, mid=2: nums[2]=7 < 8 -> lo=3
    lo=3, hi=5, mid=4: nums[4]=8 == 8 -> ans=4，往左找 hi=3
    lo=3, hi=3, mid=3: nums[3]=8 == 8 -> ans=3，往左找 hi=2
    lo=3 > hi=2 -> 結束

    回傳 3 ✔

「先記下來再繼續找」這個模式很好記，
而且不需要管 hi 該是 len 還是 len-1。

缺點：比 lower_bound 多跑幾輪
（找到之後還要繼續二分完），但複雜度一樣。"""),
     "<strong>推薦給「二分搜尋還不夠熟」的人</strong>：它的骨架和最基本的二分搜尋一模一樣，"
     "只改了「找到時做什麼」。等到 <code>lower_bound</code> 的三個要點記熟了，再換解法一。",
   ], "O(log n)", "O(1)", "兩次二分，每次都跑完", "只用幾個下標"),
 ],
 "compare": (["解法", "時間", "要記的東西", "適合", "備註"],
   [["一、lower_bound", "O(log n)", "三個要點", "面試", "最標準；一個函式解決兩件事"],
    ["二、bisect", "O(log n)", "兩個函式名", "實務", "最短，但要記得檢查值"],
    ["三、記下來再逼", "O(log n)", "基本骨架", "剛學二分", "最不容易寫錯"]]),
 "edges": [
   "<strong>空陣列</strong>：<code>([], 0)</code> → <code>[-1,-1]</code>。<code>left == len(nums) == 0</code> 擋下。",
   "<strong>target 不在裡面</strong>：<code>([5,7,7,8,8,10], 6)</code> → <code>[-1,-1]</code>。"
   "<code>lower_bound(6) = 1</code>，但 <code>nums[1] = 7 != 6</code>。",
   "<strong>target 比全部都大</strong>：<code>([1,2,3], 5)</code> → <code>[-1,-1]</code>。"
   "<code>lower_bound = 3 == len</code>。<strong>hi 初始寫成 len−1 會在這裡出錯。</strong>",
   "<strong>target 比全部都小</strong>：<code>([1,2,3], 0)</code> → <code>[-1,-1]</code>。",
   "<strong>只出現一次</strong>：<code>([1,2,3], 2)</code> → <code>[1,1]</code>。",
   "<strong>全部都是 target</strong>：<code>([2,2], 2)</code> → <code>[0,1]</code>。"
   "<strong>10⁵ 個相同元素是「二分後線性掃」會 TLE 的測資。</strong>",
   "<strong>target 在頭或尾</strong>：<code>([1,2,3], 1)</code> → <code>[0,0]</code>；"
   "<code>([1,2,3], 3)</code> → <code>[2,2]</code>。",
 ],
 "follow": [
   ("h", "追問一：如果要算「出現幾次」呢？"),
   "<code>upper_bound(t) - lower_bound(t)</code>，一行。"
   "<strong>這比「找到範圍再相減再加一」乾淨</strong>，而且在「不存在」時自動回 0，不用特判。",
   ("h", "追問二：這兩個函式在標準庫裡叫什麼？"),
   ("c", """C++ ：  std::lower_bound / std::upper_bound
        還有 std::equal_range 一次回傳兩個

Python：bisect.bisect_left / bisect.bisect_right

Java：  沒有內建的 lower_bound！
        Arrays.binarySearch 在有重複值時回傳「任意一個」，
        不保證是第一個 —— 所以 Java 要自己寫。

Rust：  slice::partition_point（更一般化的版本）

「有重複值時回傳哪一個」是這些 API 最大的差異，
用之前一定要查清楚。"""),
   ("h", "追問三：lower_bound 可以推廣成什麼？"),
   "<strong>「找出第一個讓述詞 P 為真的位置」</strong>，其中 P 必須是<strong>單調</strong>的"
   "（一旦為真就一直為真）。",
   ("c", """def partition_point(lo, hi, P):
    while lo < hi:
        mid = (lo + hi) // 2
        if P(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

lower_bound 就是 P(i) = (nums[i] >= target)

這個骨架可以直接用在：
  - 二分答案（P = 「這個答案可行嗎」）
  - 第 278 題 First Bad Version（P = isBadVersion）
  - 第 875 題 Koko Eating Bananas（P = 「這個速度吃得完嗎」）
  - 第 1011 題 船的運載能力

把 lower_bound 理解成 partition_point，
你就同時學會了一大類「二分答案」的題目。"""),
 ],
 "related": [
   "<strong>第 35 題 Search Insert Position</strong> —— 就是 lower_bound 本身",
   "<strong>第 278 題 First Bad Version</strong> —— partition_point 的最單純形式",
   "<strong>第 875／1011 題</strong> —— 二分答案",
   "<strong>第 33 題 Search in Rotated Sorted Array</strong> —— 二分的另一種變形",
 ],
 "check": [
   "<code>lower_bound</code> 的 <code>hi</code> 為什麼初始化成 <code>len(nums)</code> 而不是 <code>len(nums)-1</code>？",
   "為什麼 <code>else</code> 分支是 <code>hi = mid</code> 而不是 <code>hi = mid - 1</code>？改了會怎樣？",
   "「先二分找到一個，再往兩邊線性掃」在哪一種輸入上會退化成 O(n)？",
   "把 <code>lower_bound</code> 改寫成 <code>partition_point</code> 的形式，述詞 P 是什麼？",
 ],
})
print("P34 written")
