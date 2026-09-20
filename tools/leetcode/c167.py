# -*- coding: utf-8 -*-
"""第 167、168、169、171、172 題。"""
import random, bisect
from collections import Counter
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(167)

# ==================== 167. Two Sum II ====================
S["p167_two"] = '''class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        while lo < hi:
            s = numbers[lo] + numbers[hi]
            if s == target:
                return [lo + 1, hi + 1]     # 題目要 1-indexed
            if s < target:
                lo += 1                     # 和太小 -> 左邊往右（變大）
            else:
                hi -= 1                     # 和太大 -> 右邊往左（變小）

        return []                           # 題目保證有解，走不到這裡'''

S["p167_binary"] = '''import bisect

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            need = target - numbers[i]
            # 在 numbers[i+1:] 裡二分搜尋 need
            j = bisect.bisect_left(numbers, need, i + 1, n)
            if j < n and numbers[j] == need:
                return [i + 1, j + 1]
        return []'''

S["p167_hash"] = '''class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 第 1 題的做法：能用，但沒用到「已排序」這個條件
        seen = {}
        for i, x in enumerate(numbers):
            if target - x in seen:
                return [seen[target - x] + 1, i + 1]
            seen[x] = i
        return []'''


def _p167_ref(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i + 1, j + 1]
    return []


_p167 = [S.load(k) for k in ("p167_two", "p167_binary", "p167_hash")]

for nums, t, want in [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
    ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
]:
    assert _p167_ref(nums, t) == want, ("P167 ref", nums, t, _p167_ref(nums, t))
    for sol in _p167:
        assert sol.twoSum(list(nums), t) == want, ("P167", nums, t, want, sol)

for _ in range(6000):
    n = random.randrange(2, 12)
    nums = sorted(random.randint(-20, 20) for _ in range(n))
    i, j = sorted(random.sample(range(n), 2))
    t = nums[i] + nums[j]
    want = _p167_ref(nums, t)
    for sol in _p167:
        got = sol.twoSum(list(nums), t)
        # 題目保證「恰好有一個解」，但隨機測資可能有多組 —— 只驗證它是合法解
        assert len(got) == 2 and got[0] < got[1]
        assert nums[got[0] - 1] + nums[got[1] - 1] == t, ("P167 random", nums, t, got, sol)
print("P167 solutions OK")

_P167_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 對撞雙指標：從兩端往中間夾。和太小就左邊右移，和太大就右邊左移 —— 每一步都排除一整列／一整行。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">numbers = [2, 7, 11, 15]　target = 9</text>
            <g font-size="13" text-anchor="middle">
              <rect x="80" y="70" width="80" height="34" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="120" y="93" fill="var(--gold)">2</text>
              <rect x="180" y="70" width="80" height="34" fill="none" stroke="var(--border)"/><text x="220" y="93" fill="var(--text-muted)">7</text>
              <rect x="280" y="70" width="80" height="34" fill="none" stroke="var(--border)"/><text x="320" y="93" fill="var(--text-muted)">11</text>
              <rect x="380" y="70" width="80" height="34" fill="none" stroke="#ff8a65" stroke-width="3"/><text x="420" y="93" fill="#ff8a65">15</text>
            </g>
            <text x="120" y="124" fill="var(--gold)" font-size="11" text-anchor="middle">lo</text>
            <text x="420" y="124" fill="#ff8a65" font-size="11" text-anchor="middle">hi</text>
            <text x="20" y="158" fill="var(--text-muted)" font-size="12">2 + 15 = 17 &gt; 9　→　太大 →　hi 左移</text>
            <text x="20" y="186" fill="var(--text-muted)" font-size="12">2 + 11 = 13 &gt; 9　→　太大 →　hi 左移</text>
            <text x="20" y="214" fill="var(--gold)" font-size="12">2 + 7 = 9　✔　找到！回傳 [1, 2]（1-indexed）</text>
            <line x1="20" y1="238" x2="620" y2="238" stroke="var(--border)"/>
            <text x="20" y="266" fill="var(--accent)" font-size="13">★ 為什麼「移動指標」不會漏掉答案？</text>
            <text x="40" y="296" fill="var(--text-muted)" font-size="12">假設目前 numbers[lo] + numbers[hi] &gt; target（太大）。</text>
            <text x="40" y="324" fill="var(--gold)" font-size="12">那麼 numbers[hi] 和【任何 lo 右邊的元素】配對都會 ≥ 目前的和 → 也太大。</text>
            <text x="40" y="350" fill="var(--accent)" font-size="12">→ numbers[hi] 不可能是答案的一部分 → 安全地丟掉它（hi 左移）✔</text>
            <text x="40" y="384" fill="var(--text-muted)" font-size="12">太小時對稱：numbers[lo] 和任何 hi 左邊的配對都 ≤ 目前的和 → 丟掉 lo。</text>
            <text x="20" y="418" fill="#ff8a65" font-size="12">★ 每一步都【排除一整行或一整列】的可能組合 —— 所以掃一遍就夠，O(n)。</text>
            <text x="20" y="444" fill="var(--text-muted)" font-size="12">這個論證依賴「陣列已排序」。第 1 題沒有這個條件，所以只能用雜湊表。</text>'''

emit({
 "num": 167, "slug": "two-sum-ii-input-array-is-sorted",
 "en": [
   "Given a <strong>1-indexed</strong> array of integers <code>numbers</code> that is already "
   "<strong>sorted in non-decreasing order</strong>, find two numbers such that they add up to "
   "a specific <code>target</code> number.",
   "Return <em>the indices of the two numbers, </em><code>index1</code><em> and </em>"
   "<code>index2</code><em>, <strong>added by one</strong> as an integer array </em>"
   "<code>[index1, index2]</code><em> of length 2.</em>",
   "The tests are generated such that there is <strong>exactly one solution</strong>. You "
   "<strong>may not</strong> use the same element twice.",
   "Your solution must use only constant extra space.",
 ],
 "zh": [
   "給你一個<strong>已經升序排列</strong>的整數陣列 <code>numbers</code>"
   "（<strong>索引從 1 開始算</strong>）和一個目標值 <code>target</code>。",
   "找出兩個數，使它們的和等於 <code>target</code>，回傳它們的<strong>索引（從 1 開始）</strong>。",
   "測資保證<strong>恰好有一組解</strong>，而且<strong>不能重複使用同一個元素</strong>。",
   "<strong>只能用常數額外空間。</strong>",
 ],
 "pre": [
   ("note", "★ 和第 1 題的差別：這次陣列是排序好的", [
     ("c", """第 1 題（Two Sum）：陣列【沒有排序】
    -> 只能用雜湊表，O(n) 時間、O(n) 空間

第 167 題（本題）：陣列【已經排序】
    -> 可以用【對撞雙指標】，O(n) 時間、O(1) 空間 ✔

【題目明確要求「常數額外空間」】——
    這就排除了雜湊表，逼你利用「已排序」這個條件。

【對撞雙指標的核心】：

    lo 從最左、hi 從最右，往中間夾。

    s = numbers[lo] + numbers[hi]

    s == target -> 找到了 ✔
    s <  target -> 和太小，要變大 -> lo 右移（因為右邊的更大）
    s >  target -> 和太大，要變小 -> hi 左移（因為左邊的更小）

【為什麼這樣不會漏掉答案？】見下方的 idea。

【這個「對撞雙指標」的模式非常常用】：

    第 11 題 盛最多水的容器
    第 15 題 三數之和（排序後固定一個，剩下用雙指標）
    第 16 題 最接近的三數之和
    第 42 題 接雨水
    第 125 題 驗證回文串
    第 977 題 有序陣列的平方"""),
   ]),
 ],
 "examples": """範例 1
  輸入：numbers = [2,7,11,15], target = 9
  輸出：[1,2]
  說明：2 + 7 = 9，索引（1-indexed）分別是 1 和 2。

範例 2
  輸入：numbers = [2,3,4], target = 6
  輸出：[1,3]

範例 3
  輸入：numbers = [-1,0], target = -1
  輸出：[1,2]""",
 "constraints": [
   "2 ≤ <code>numbers.length</code> ≤ 3 × 10⁴",
   "−1000 ≤ <code>numbers[i]</code> ≤ 1000",
   "<code>numbers</code> 依<strong>非遞減</strong>順序排列",
   "−1000 ≤ <code>target</code> ≤ 1000",
   "測資保證<strong>恰好有一組解</strong>",
 ],
 "idea": [
   ("fig", _P167_FIG, "0 0 640 464"),
   ("c", """【對撞雙指標的正確性證明】

    不變量：「如果存在解，它一定在 [lo, hi] 這個範圍內。」

    初始：[0, n-1] 涵蓋全部 ✔

    情況 A：s > target（和太大）

        考慮 numbers[hi] 和【任何】numbers[k]（lo <= k < hi）的配對：

            numbers[k] <= numbers[hi-1] <= ... 
            其實應該說：numbers[k] <= numbers[hi]

            我們要證的是：numbers[k] + numbers[hi] 對所有
            k in [lo, hi-1] 都 > target 嗎？

            不對 —— k 可能比 lo 小的元素... 但 k >= lo。

            關鍵：numbers[lo] 是 [lo, hi] 裡【最小】的。

            所以對任何 k in [lo, hi-1]：
                numbers[k] + numbers[hi] >= numbers[lo] + numbers[hi] = s > target

            -> numbers[hi] 和區間內任何元素配對都太大
            -> hi 不可能是答案的一部分
            -> 安全地 hi -= 1 ✔

    情況 B：s < target（和太小）

        對稱地，numbers[lo] 和區間內任何元素配對都太小
        -> lo 不可能是答案 -> lo += 1 ✔

    每一步都【只排除一個不可能是答案的元素】，
    所以不會漏掉解 ✔

【★ 這個論證的本質】

    想像一個 n×n 的「和矩陣」M[i][j] = numbers[i] + numbers[j]。

    因為陣列有序，M 的每一列和每一行都是遞增的。

    從【右上角】開始（lo=0, hi=n-1）：
        太大 -> 往左（減小）
        太小 -> 往下（增大）

    這就是「在有序矩陣裡搜尋」的走法（第 240 題）✔

    每一步排除一整行或一整列 -> O(n) 步 ✔

【複雜度】：O(n) 時間、O(1) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "對撞雙指標（標準答案）", [
     ("c", S["p167_two"]),
     "<strong>十行，O(n) 時間、O(1) 空間。</strong>"
     "<strong>這是題目要的答案。</strong>",
     ("h", "別忘了 <code>+1</code>（1-indexed）"),
     "<strong>題目說索引從 1 開始</strong> —— "
     "<strong>回傳 <code>[lo, hi]</code> 而不是 <code>[lo+1, hi+1]</code> 是很常見的粗心錯誤。</strong>",
     "<strong>LeetCode 這一系列題目裡，只有這題是 1-indexed</strong>（第 1 題是 0-indexed）—— "
     "<strong>讀題時要特別注意。</strong>",
     ("h", "為什麼迴圈條件是 <code>lo &lt; hi</code> 而不是 <code>&lt;=</code>？"),
     "因為<strong>「不能重複使用同一個元素」</strong> —— "
     "<code>lo == hi</code> 時會把同一個數加兩次 ✘",
     "<strong>而且題目保證有解，所以一定會在 <code>lo &lt; hi</code> 時找到。</strong>",
     ("h", "有重複元素時會怎樣？"),
     ("c", """numbers = [1, 2, 3, 4, 4, 9], target = 8

    lo=0, hi=5: 1+9=10 > 8 -> hi=4
    lo=0, hi=4: 1+4=5  < 8 -> lo=1
    lo=1, hi=4: 2+4=6  < 8 -> lo=2
    lo=2, hi=4: 3+4=7  < 8 -> lo=3
    lo=3, hi=4: 4+4=8  ✔ 回傳 [4, 5]

    【重複元素完全不影響邏輯】——
    雙指標只看「和」，不看「值是否重複」✔

    這比雜湊表版省心（那裡要小心「同一個元素用兩次」）。""",),
   ], "O(n)", "O(1)", "兩個指標各走一遍", "兩個索引", optimal=True),

   ap("解法二", "對每個元素二分搜尋另一半", [
     ("c", S["p167_binary"]),
     ("c", """對每個 i，在 numbers[i+1:] 裡二分搜尋 target - numbers[i]。

    O(n log n) 時間、O(1) 空間。

【比雙指標慢，但它展示了一個有用的技巧】：

    bisect.bisect_left(a, x, lo, hi)

    在 a[lo:hi] 這個範圍內找 x 的插入位置。

    【指定 lo 和 hi 可以避免切片】——
    numbers[i+1:] 會複製 O(n) 的資料，
    而 bisect(..., i+1, n) 是 O(log n) 且不複製 ✔

【Python 的 bisect 模組】：

    bisect_left(a, x)   第一個 >= x 的位置
    bisect_right(a, x)  第一個 > x 的位置
    insort(a, x)        插入並保持有序（O(n)，因為要搬移）

    找「x 存不存在」：
        i = bisect_left(a, x)
        exists = i < len(a) and a[i] == x    ★ 要檢查兩件事

    【只檢查 i < len(a) 是不夠的】——
    bisect 回傳的是「插入位置」，那裡不一定是 x。

【什麼時候二分比雙指標好？】

    當「陣列已排序但只能查詢一次」時
    （例如 numbers 存在資料庫裡，只能一筆一筆查）。

    這題兩個都能用，雙指標更優。""",),
   ], "O(n log n)", "O(1)", "n 次二分", "幾個變數"),

   ap("解法三", "雜湊表（第 1 題的做法，但不滿足空間要求）", [
     ("c", S["p167_hash"]),
     ("c", """O(n) 時間、O(n) 空間。

【它完全沒有用到「已排序」這個條件】——
    所以它對第 1 題（沒排序）也適用。

【但題目明確要求 O(1) 空間】-> 不合格 ✘

【面試時的價值】：

    如果你先寫這個，面試官會說
    「陣列已經排序了，能不能利用這一點？」

    那就是在提示你用雙指標。

【一般原則】：

    【題目給的每一個條件都是為了「讓某個更好的解法成立」。】

    「已排序」-> 雙指標 / 二分搜尋
    「值域受限」-> 計數排序 / 桶
    「互不相同」-> 可以用值當 key
    「保證有解」-> 不用處理找不到的情況

    看到一個條件沒用到，就要問「它是為了什麼？」""",),
   ], "O(n)", "O(n)", "掃一遍", "雜湊表"),
 ],
 "compare": (["解法", "時間", "空間", "用到「已排序」", "符合要求"],
   [["一、對撞雙指標", "O(n)", "O(1)", "✔", "✔"],
    ["二、逐個二分", "O(n log n)", "O(1)", "✔", "✔ 但較慢"],
    ["三、雜湊表", "O(n)", "O(n)", "✘", "✘ 空間超標"]]),
 "edges": [
   "<strong>只有兩個元素</strong> <code>[-1,0]</code>, <code>target=-1</code> → <code>[1,2]</code>。",
   "<strong>答案在兩端</strong> → 第一次就找到。",
   "<strong>答案在中間</strong> → 要夾很多次。",
   "<strong>有重複元素</strong> <code>[1,2,3,4,4,9]</code>, <code>target=8</code> → "
   "<code>[4,5]</code>。<strong>雙指標完全不受影響。</strong>",
   "<strong>有負數</strong> → 邏輯不變（只看和的大小）。",
   "<strong>忘了 <code>+1</code></strong> → <strong>答案全錯（0-indexed vs 1-indexed）。</strong>",
   "<strong>迴圈條件寫成 <code>lo &lt;= hi</code></strong> → 可能把同一個元素用兩次。",
   "<strong>3 × 10⁴ 個元素</strong> → O(n) 輕鬆；O(n²) 暴力法是 9 億，會逾時。",
 ],
 "follow": [
   ("h", "追問一：如果要「三數之和」呢？"),
   "<strong>第 15 題</strong>。<strong>先排序，然後固定第一個數，"
   "剩下的用本題的雙指標。</strong>",
   ("c", """for i in range(n - 2):
    if i > 0 and nums[i] == nums[i-1]: continue     # 跳過重複
    lo, hi = i + 1, n - 1
    while lo < hi:
        s = nums[i] + nums[lo] + nums[hi]
        if s == 0:
            收下答案
            while lo < hi and nums[lo] == nums[lo+1]: lo += 1   # 跳過重複
            while lo < hi and nums[hi] == nums[hi-1]: hi -= 1
            lo += 1; hi -= 1
        elif s < 0: lo += 1
        else: hi -= 1

    O(n²) 時間、O(1) 空間（不算排序）。

【去重是第 15 題的難點】——
    因為它要「所有不重複的三元組」，
    而本題只要「一組」，所以完全不用去重 ✔

【推廣到 k 數之和】：
    固定 k-2 個數，最內層用雙指標 -> O(n^(k-1))""",),
   ("h", "追問二：如果沒有「保證恰好一組解」呢？"),
   "<strong>雙指標會找到「某一組」</strong>（第一個碰到的）。",
   "<strong>如果要「所有組」</strong>，找到之後不要 return，"
   "而是<strong>同時移動兩個指標並跳過重複值</strong>（像第 15 題那樣）。",
   "<strong>如果「可能無解」</strong>，迴圈結束後回傳 <code>[]</code> 或 <code>[-1,-1]</code> —— "
   "<strong>本文的程式碼已經這樣寫了。</strong>",
   ("h", "追問三：「和矩陣」的視角還能用在哪？"),
   ("c", """把 M[i][j] = numbers[i] + numbers[j] 想成一個【有序矩陣】
（每列遞增、每行遞增）。

    本題就是「在有序矩陣裡找一個值」——
    從右上角開始，太大往左、太小往下 -> O(n) ✔

【同樣的走法】：

    第 240 題 搜尋二維矩陣 II：
        真正的有序矩陣，從右上角開始走 -> O(m+n)

    第 378 題 有序矩陣中第 K 小的元素：
        二分答案 + 用這個走法計數

    第 373 題 查找和最小的 K 對數字：
        用堆在「和矩陣」上做 k 路歸併

【「把兩個一維的東西想成二維」
  是一個很有力的視角轉換】——

    它把「兩個指標怎麼移動」
    變成「在矩陣裡怎麼走」，直覺清楚很多。""",),
   ("h", "追問四：為什麼第 1 題不能用雙指標？"),
   ("c", """因為第 1 題的陣列【沒有排序】，
而且要回傳【原本的索引】。

    如果先排序：
        ✔ 就能用雙指標
        ✘ 但索引亂掉了

    解法：排序時連索引一起帶著

        pairs = sorted((v, i) for i, v in enumerate(nums))
        然後對 pairs 做雙指標，回傳原本的 i

    O(n log n) 時間、O(n) 空間 ——
    比雜湊表的 O(n)/O(n) 差 ✘

【所以第 1 題的最佳解是雜湊表，本題是雙指標】——

    【同一個問題，輸入條件不同，最佳解法就不同。】

    這一對題目是展示這件事的最好例子。""",),
 ],
 "related": [
   "<strong>第 1 題 Two Sum</strong> —— 沒排序的版本，用雜湊表",
   "<strong>第 15 題 3Sum</strong> —— 固定一個數 + 雙指標",
   "<strong>第 11 題 盛最多水的容器</strong> —— 另一個對撞雙指標",
   "<strong>第 240 題 搜尋二維矩陣 II</strong> —— 「和矩陣」視角的原型",
   "<strong>第 653 題 兩數之和 IV（BST）</strong> —— 中序 + 雙指標",
 ],
 "check": [
   "為什麼「和太大就移動 <code>hi</code>」不會漏掉答案？請完整論證一次。",
   "這題和第 1 題的差別是什麼？為什麼最佳解法不同？",
   "回傳的索引是 0-indexed 還是 1-indexed？",
   "把它想成「和矩陣」的話，雙指標在做什麼？",
 ],
})
print("P167 written")

# ==================== 168 / 171. Excel Sheet Column Title / Number ====================
S["p168"] = '''class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = []
        n = columnNumber

        while n:
            n -= 1                          # ★ 先減 1，把 1..26 平移成 0..25
            out.append(chr(ord("A") + n % 26))
            n //= 26

        return "".join(reversed(out))'''

S["p168_divmod"] = '''class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = []
        n = columnNumber
        while n:
            n, r = divmod(n - 1, 26)        # 同時處理「減 1」和「取商餘」
            out.append(chr(ord("A") + r))
        return "".join(out[::-1])'''

S["p168_wrong"] = '''class Solution:
    # 【這是錯的，不要抄】：忘了先減 1
    def convertToTitle(self, columnNumber: int) -> str:
        out = []
        n = columnNumber
        while n:
            out.append(chr(ord("A") + n % 26 - 1))
            n //= 26
        return "".join(reversed(out))'''

S["p171"] = '''class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        for c in columnTitle:
            n = n * 26 + (ord(c) - ord("A") + 1)    # ★ +1：A 是 1 不是 0
        return n'''


def _p168_ref(n):
    out = []
    while n:
        n, r = divmod(n - 1, 26)
        out.append(chr(ord("A") + r))
    return "".join(reversed(out))


def _p171_ref(s):
    n = 0
    for c in s:
        n = n * 26 + ord(c) - 64
    return n


_p168 = [S.load(k) for k in ("p168", "p168_divmod")]
_p168_bad = S.load("p168_wrong")
_p171 = S.load("p171")

for n, want in [(1, "A"), (26, "Z"), (27, "AA"), (28, "AB"), (701, "ZY"),
                (702, "ZZ"), (703, "AAA"), (2147483647, "FXSHRXW")]:
    assert _p168_ref(n) == want, ("P168 ref", n, _p168_ref(n))
    for sol in _p168:
        assert sol.convertToTitle(n) == want, ("P168", n, want, sol)
    assert _p171.titleToNumber(want) == n, ("P171", want, n)

# 錯誤寫法確實在 26 的倍數上答錯
assert _p168_bad.convertToTitle(26) != "Z", "P168 wrong-demo"

for _ in range(8000):
    n = random.randint(1, 2 ** 31 - 1)
    want = _p168_ref(n)
    for sol in _p168:
        assert sol.convertToTitle(n) == want, ("P168 random", n, want, sol)
    # 往返驗證：轉成字母再轉回來，必須等於原本的數
    assert _p171.titleToNumber(want) == n, ("P171 round-trip", n, want)
print("P168 / P171 solutions OK")

_P168_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ Excel 的欄位編號是【沒有 0 的 26 進位】—— 這一個差別，就是這題唯一的難點。</text>
            <g font-size="12">
              <text x="40" y="56" fill="var(--gold)">正常的 26 進位（有 0）：</text>
              <text x="60" y="82" fill="var(--text-muted)">每一位是 0..25，和十進位的 0..9 一樣</text>
              <text x="60" y="106" fill="var(--text-muted)">「10」代表 1×26 + 0 = 26</text>
              <text x="40" y="142" fill="#ff8a65">Excel 的編號（沒有 0）：</text>
              <text x="60" y="168" fill="var(--text-muted)">每一位是 A..Z = 1..26　【沒有代表 0 的符號】</text>
              <text x="60" y="192" fill="var(--text-muted)">「AA」代表 1×26 + 1 = 27，不是 26</text>
            </g>
            <line x1="20" y1="214" x2="620" y2="214" stroke="var(--border)"/>
            <text x="20" y="242" fill="var(--accent)" font-size="13">★ 修正方法：每一步先把 n 減 1，把 1..26 平移成 0..25</text>
            <g font-size="12">
              <text x="40" y="272" fill="var(--text-muted)">n = 26：</text>
              <text x="140" y="272" fill="var(--gold)">n -= 1 → 25　　25 % 26 = 25 → &#39;Z&#39;　　25 // 26 = 0 → 結束　✔ &quot;Z&quot;</text>
              <text x="40" y="300" fill="var(--text-muted)">n = 27：</text>
              <text x="140" y="300" fill="var(--gold)">n -= 1 → 26　　26 % 26 = 0  → &#39;A&#39;　　26 // 26 = 1</text>
              <text x="140" y="324" fill="var(--gold)">n = 1 → 0　　　0 % 26 = 0  → &#39;A&#39;　　0 // 26 = 0 → 結束　✔ &quot;AA&quot;</text>
            </g>
            <line x1="20" y1="348" x2="620" y2="348" stroke="var(--border)"/>
            <text x="20" y="376" fill="#ff8a65" font-size="13">忘了減 1 會怎樣？</text>
            <text x="40" y="404" fill="var(--text-muted)" font-size="12">n = 26：26 % 26 = 0 → chr(&#39;A&#39; + 0 - 1) = &#39;@&#39;　✘　而且 26 // 26 = 1 又多跑一輪</text>
            <text x="40" y="430" fill="#ff8a65" font-size="12">所有「26 的倍數」都會壞掉 —— 這是本題第一名的 bug。</text>
            <text x="20" y="464" fill="var(--accent)" font-size="12">★ 第 171 題（反向）就沒有這個問題：n = n × 26 + (c − &#39;A&#39; + 1)，直接加 1 就好。</text>'''

emit({
 "num": 168, "slug": "excel-sheet-column-title",
 "en": [
   "Given an integer <code>columnNumber</code>, return <em>its corresponding column title as it "
   "appears in an Excel sheet</em>.",
   "For example:",
   ("c", """A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
..."""),
 ],
 "zh": [
   "給你一個整數 <code>columnNumber</code>，回傳它在 Excel 裡對應的<strong>欄位名稱</strong>。",
   ("c", """A  -> 1
B  -> 2
...
Z  -> 26
AA -> 27
AB -> 28
..."""),
 ],
 "pre": [
   ("note", "★ 這是「沒有 0」的 26 進位", [
     ("c", """【正常的 26 進位】：每一位是 0 到 25

    "10" = 1×26 + 0 = 26

【Excel 的編號】：每一位是 A 到 Z = 1 到 26

    "AA" = 1×26 + 1 = 27     ← 不是 26！

    【沒有代表 0 的符號。】

【這造成什麼問題？】

    正常的進位制轉換是：
        digit = n % base
        n //= base

    但這裡 digit 的範圍是 1..26 而不是 0..25 ——
    n % 26 會給出 0..25，對不上 ✘

    而且當 n 是 26 的倍數時，n % 26 = 0，
    但 0 不對應任何字母 ✘

【修正：每一步先 n -= 1】

    這把「1..26」平移成「0..25」：

        n = 26 -> n-1 = 25 -> 25 % 26 = 25 -> 'Z' ✔
                             25 // 26 = 0 -> 結束 ✔

        n = 27 -> n-1 = 26 -> 26 % 26 = 0 -> 'A' ✔
                             26 // 26 = 1
                  n = 1 -> 0 -> 0 % 26 = 0 -> 'A' ✔
        -> "AA" ✔

【一行 n -= 1，就是這題的全部。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：columnNumber = 1
  輸出："A"

範例 2
  輸入：columnNumber = 28
  輸出："AB"

範例 3
  輸入：columnNumber = 701
  輸出："ZY"

範例 4
  輸入：columnNumber = 2147483647
  輸出："FXSHRXW"（32 位元整數的上限）""",
 "constraints": [
   "1 ≤ <code>columnNumber</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("fig", _P168_FIG, "0 0 640 486"),
   ("c", """while n:
    n -= 1                              ★ 先減 1
    out.append(chr(ord('A') + n % 26))
    n //= 26

return "".join(reversed(out))

【或者用 divmod 一次搞定】：

    n, r = divmod(n - 1, 26)
    out.append(chr(ord('A') + r))

    divmod(n-1, 26) 同時給出「新的 n」和「這一位」✔

【★ 為什麼要 reversed？】

    我們是從【最低位】開始算的（% 26 給出最低位），
    但輸出要從最高位開始 -> 反轉 ✔

    這和「十進位轉字串」是一樣的：
        123 -> 3, 2, 1（算出的順序）-> "123"（輸出）

【驗算 701】：

    n=701: n-1=700, 700%26=24 -> 'Y', 700//26=26
    n=26:  n-1=25,  25%26=25  -> 'Z', 25//26=0
    out = ['Y', 'Z'] -> 反轉 -> "ZY" ✔

【複雜度】：O(log₂₆ n) 時間（最多 7 位）、O(1) 空間（不算輸出）"""),
 ],
 "approaches": [
   ap("解法一", "每步先減 1（標準答案）", [
     ("c", S["p168"]),
     "<strong>七行。<code>n -= 1</code> 那一行是全部的關鍵。</strong>",
     ("h", "★ 忘了減 1 會怎樣？"),
     ("c", S["p168_wrong"]),
     ("c", """這個版本在 n = 26 時：

    26 % 26 = 0
    chr(ord('A') + 0 - 1) = chr(64) = '@'    ✘
    26 // 26 = 1

    n = 1:
        1 % 26 = 1
        chr(ord('A') + 1 - 1) = 'A'
        1 // 26 = 0

    結果："A@" ✘（正確答案是 "Z"）

【所有「26 的倍數」都會壞掉】：
    26 -> "A@"  應該是 "Z"
    52 -> "A@"?  ...
    702 -> 錯

【為什麼「26 的倍數」特別容易錯？】

    因為那正是「需要借位」的地方 ——
    Z 是「這一位的最大值」，
    而「沒有 0」的進位制在最大值處的行為
    和一般進位制不同。

    【測試進位制轉換時，永遠要測「base 的倍數」和
      「base^k - 1」這兩類邊界。】

    本文的測試包含了 26、702（= 26×27）等等。""",),
   ], "O(log n)", "O(1)", "最多 7 位", "輸出字串", optimal=True),

   ap("解法二", "<code>divmod</code> 版（最精簡）", [
     ("c", S["p168_divmod"]),
     ("c", """n, r = divmod(n - 1, 26)

    一行同時完成：
        「先減 1」
        「取這一位（餘數）」
        「更新 n（商）」

【divmod 的好處】：
    ✔ 底層只做一次除法（比 // 和 % 分開快）
    ✔ 語意清楚：「這是一次帶餘除法」
    ✔ 不會忘記更新 n

【out[::-1] vs reversed(out)】：

    "".join(out[::-1])      建立一個新 list 再 join
    "".join(reversed(out))  用迭代器，不建 list

    後者略省記憶體，但這題只有 7 個字元 —— 沒差。

    【reversed() 回傳的是迭代器，
      而 join 接受任何可迭代物件 ✔】""",),
   ], "O(log n)", "O(1)", "同解法一", "輸出字串"),
 ],
 "compare": (["寫法", "正確嗎", "關鍵", "備註"],
   [["每步先 n -= 1", "✔", "把 1..26 平移成 0..25", "標準答案"],
    ["divmod(n-1, 26)", "✔", "同上，但更緊湊", "最精簡"],
    ["直接 n % 26 - 1", "✘", "26 的倍數會產生 '@'", "本題第一名的 bug"]]),
 "edges": [
   "<strong><code>1</code></strong> → <code>\"A\"</code>。",
   "<strong><code>26</code></strong> → <code>\"Z\"</code>。"
   "<strong>忘了減 1 會得到 <code>\"A@\"</code>。本題第一名的 bug。</strong>",
   "<strong><code>27</code></strong> → <code>\"AA\"</code>（進位）。",
   "<strong><code>52</code></strong> → <code>\"AZ\"</code>。",
   "<strong><code>702</code></strong> → <code>\"ZZ\"</code>（= 26×27，兩位的最大值）。",
   "<strong><code>703</code></strong> → <code>\"AAA\"</code>（進到三位）。",
   "<strong><code>2147483647</code></strong> → <code>\"FXSHRXW\"</code>（七位）。",
   "<strong>忘了反轉</strong> → 字母順序顛倒。",
 ],
 "follow": [
   ("h", "追問一：反過來（字母轉數字）呢？"),
   "<strong>第 171 題</strong>。<strong>反而簡單得多</strong>：",
   ("c", """n = 0
for c in columnTitle:
    n = n * 26 + (ord(c) - ord('A') + 1)
return n

【為什麼反向比較簡單？】

    正向（數字 -> 字母）要「借位」——
    每一步都要處理「沒有 0」造成的偏移。

    反向（字母 -> 數字）只是「累加」——
    每個字母直接對應 1..26，加上去就好 ✔

【這是「解碼比編碼簡單」的典型例子】。

    類似的：
        第 8 題（字串轉整數）比「整數轉字串」簡單
        JSON 解析比 JSON 生成簡單（不用考慮跳脫、縮排）

    因為「解碼」只要「讀懂」，
    而「編碼」還要「做出合法的格式」。""",),
   ("h", "追問二：「沒有 0 的進位制」還有哪些例子？"),
   ("ul", [
     "<strong>Excel 欄位</strong>（本題）：A..Z = 1..26",
     "<strong>羅馬數字</strong>：完全不同的系統，但也沒有 0",
     "<strong>「第 n 個」的序數</strong>：第 1 個、第 2 個…（沒有「第 0 個」）",
     "<strong>bijective base-k</strong>（雙射進位制）：每個正整數有唯一表示，"
     "而且【沒有前導零的問題】",
   ]),
   ("c", """【雙射 k 進位的特點】：

    數字用 1..k 而不是 0..k-1

    好處：每個正整數有【唯一】的表示，
          不會有 "007" 和 "7" 這種歧義 ✔

    壞處：算術運算不方便（要一直處理偏移）

【Excel 選這個設計，是因為它要的是「命名」而不是「計算」】——

    欄位名稱不需要做加減乘除，
    只需要「每個欄位有一個唯一的、好唸的名字」。

    對這個目的來說，雙射進位制是對的選擇 ✔

【教訓】：
    「看起來奇怪的設計」常常是為了某個
    我們沒想到的目的。

    Excel 的欄位編號不是 bug，是 feature。""",),
   ("h", "追問三：怎麼驗證這兩題的實作是對的？"),
   ("c", """【往返測試（round-trip testing）】：

    for n in 隨機的很多個數:
        title = convertToTitle(n)
        assert titleToNumber(title) == n    ✔

    【這比「比對硬寫的期望值」可靠得多】——

    因為：
        ✔ 可以測幾千個隨機值（硬寫只能測幾個）
        ✔ 不會有「期望值自己算錯」的風險
        ✔ 同時驗證了兩個函式

【本文的測試就是這樣做的】。

【往返測試的一般形式】：

    encode/decode、serialize/deserialize、
    compress/decompress、to_string/parse

    只要有一對「互逆」的操作，就能這樣測。

    【它測的是「語意」而不是「格式」——
      而語意才是真正重要的東西。】""",),
   ("h", "追問四：如果欄位編號可以很大（超過 2³¹）呢？"),
   "<strong>Python 完全不受影響</strong>（整數無限大）。",
   "<strong>Excel 實際的上限是 16384 欄（<code>XFD</code>）</strong> —— "
   "<strong>所以這題的 <code>2³¹-1</code> 只是為了測邊界，不是真實的 Excel 限制。</strong>",
   "<strong>在其他語言裡，只要 <code>n</code> 的型別夠大就沒問題</strong> —— "
   "<strong>這個演算法本身不會產生比 <code>n</code> 更大的中間值。</strong>",
 ],
 "related": [
   "<strong>第 171 題 Excel 表欄位序號</strong> —— 反向運算",
   "<strong>第 12/13 題 整數與羅馬數字互轉</strong> —— 另一種「非標準進位制」",
   "<strong>第 8 題 字串轉整數</strong> —— 同樣的 <code>n*base + digit</code>",
   "<strong>第 405 題 數字轉換為十六進位</strong> —— 標準進位制轉換",
 ],
 "check": [
   "Excel 的編號和「正常的 26 進位」差在哪裡？",
   "<code>n -= 1</code> 這一行在做什麼？忘了它會在哪個輸入出錯？",
   "為什麼「反向」（第 171 題）比「正向」簡單得多？",
   "怎麼用「往返測試」驗證這兩題？",
 ],
})
print("P168 written")

emit({
 "num": 171, "slug": "excel-sheet-column-number",
 "en": [
   "Given a string <code>columnTitle</code> that represents the column title as appears in an "
   "Excel sheet, return <em>its corresponding column number</em>.",
   "For example:",
   ("c", """A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
..."""),
 ],
 "zh": [
   "給你一個 Excel 欄位名稱 <code>columnTitle</code>，回傳它對應的<strong>欄位序號</strong>。",
   "這是<strong>第 168 題的反向運算</strong>。",
 ],
 "pre": [
   ("note", "★ 反向比正向簡單得多", [
     ("c", """第 168 題（數字 -> 字母）：
    要處理「沒有 0」造成的借位 -> 每步要 n -= 1

第 171 題（字母 -> 數字）：
    只要累加 -> 一行搞定 ✔

    n = 0
    for c in columnTitle:
        n = n * 26 + (ord(c) - ord('A') + 1)

【為什麼這麼簡單？】

    每個字母直接對應一個值：
        A -> 1, B -> 2, ..., Z -> 26

    然後就是標準的「進位制展開」：

        "AB" = A × 26¹ + B × 26⁰
             = 1 × 26 + 2
             = 28 ✔

    完全不用管「有沒有 0」——
    因為我們是在【讀】，不是在【產生】。

【n = n * 26 + digit 這個模式】

    是所有「字串轉數字」的標準寫法：

        第 8 題   字串轉整數（base 10）
        第 129 題 求根到葉數字之和（base 10）
        第 165 題 比較版本號（base 10）
        第 171 題 本題（base 26）

    【記住這一行，一整類題目就解決了。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：columnTitle = "A"
  輸出：1

範例 2
  輸入：columnTitle = "AB"
  輸出：28

範例 3
  輸入：columnTitle = "ZY"
  輸出：701""",
 "constraints": [
   "1 ≤ <code>columnTitle.length</code> ≤ 7",
   "<code>columnTitle</code> 只包含<strong>大寫英文字母</strong>",
   "<code>columnTitle</code> 的範圍在 <code>[\"A\", \"FXSHRXW\"]</code> 之間",
 ],
 "idea": [
   ("c", """n = 0
for c in columnTitle:
    n = n * 26 + (ord(c) - ord('A') + 1)
return n

【★ 那個 +1】

    ord(c) - ord('A') 給出 0..25（A 是 0）
    但 Excel 的 A 是 1 -> 要 +1 ✔

    忘了 +1 的話：
        "A" -> 0 ✘（應該是 1）
        "AA" -> 0 × 26 + 0 = 0 ✘（應該是 27）

【★ 為什麼是「先乘後加」？】

    n = n * 26 + digit

    每讀一個新字元，之前累積的值就要「進一位」（乘 26），
    然後把新的一位加上去。

    驗算 "ZY"：
        n = 0
        c='Z': n = 0*26 + 26 = 26
        c='Y': n = 26*26 + 25 = 676 + 25 = 701 ✔

【★ 順序：從左到右（高位到低位）】

    因為 "AB" 的 A 是高位。

    如果從右到左讀，就要自己算 26 的冪次 ——
    麻煩得多。

    【「從高位到低位、每步乘 base 再加」
      是進位制解析的標準做法。】

【複雜度】：O(len) 時間、O(1) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "從左到右累加（標準答案）", [
     ("c", S["p171"]),
     "<strong>四行，O(len) 時間、O(1) 空間。</strong>"
     "<strong>不可能更短了。</strong>",
     ("h", "<code>ord(c) - ord(\"A\") + 1</code> 的三種寫法"),
     ("c", """ord(c) - ord("A") + 1       ✔ 最清楚
ord(c) - 64                 ✔ 等價（ord('A') = 65）
ord(c) - ord("A") + 1       ✔ 本文用的

【為什麼不寫 ord(c) - 64？】

    64 是一個「魔術數字」——
    讀的人要自己算出 ord('A') - 1 = 64。

    寫成 ord(c) - ord("A") + 1 的話，
    意圖一目了然：「c 是第幾個字母，從 1 開始算」。

【效能差異？】

    ord("A") 每次迴圈都會算一次，
    但 CPython 會把它當成常數摺疊嗎？

    —— 不會（ord 是函式呼叫）。

    要優化的話：
        A = ord("A") - 1
        for c in s: n = n * 26 + ord(c) - A

    但 len <= 7，完全不用在意 ✔

    【可讀性 > 微優化，除非你測量過。】""",),
     ("h", "一行版"),
     ("c", """from functools import reduce
return reduce(lambda n, c: n * 26 + ord(c) - 64, columnTitle, 0)

    或者用 enumerate 算冪次：

    return sum((ord(c) - 64) * 26 ** i
               for i, c in enumerate(reversed(columnTitle)))

【兩個都能動，但都比四行版難讀】。

    第二個還多了 O(len) 次冪運算 ——
    「先乘後加」的版本只要 O(len) 次乘法。

    【Horner 法則】：
        a·x³ + b·x² + c·x + d
        = ((a·x + b)·x + c)·x + d

    後者只要 3 次乘法，前者要 6 次 ✔

    這就是「先乘後加」比「算冪次再加」好的數學理由。""",),
   ], "O(len)", "O(1)", "每個字元一次", "一個變數", optimal=True),
 ],
 "compare": (["寫法", "乘法次數", "可讀性", "備註"],
   [["先乘後加（Horner）", "len", "★★★", "標準答案"],
    ["算冪次再加總", "2·len", "★★☆", "多一半的運算"],
    ["reduce 一行", "len", "★☆☆", "炫技但難讀"]]),
 "edges": [
   "<strong><code>\"A\"</code></strong> → <code>1</code>。"
   "<strong>忘了 <code>+1</code> 會得到 0。</strong>",
   "<strong><code>\"Z\"</code></strong> → <code>26</code>。",
   "<strong><code>\"AA\"</code></strong> → <code>27</code>（不是 26）。",
   "<strong><code>\"ZY\"</code></strong> → <code>701</code>。",
   "<strong><code>\"FXSHRXW\"</code></strong> → <code>2147483647</code>（上限）。",
   "<strong>從右到左讀而沒算對冪次</strong> → 答案完全錯。",
   "<strong>長度最多 7</strong> → 完全沒有效能問題。",
 ],
 "follow": [
   ("h", "追問一：怎麼驗證這題和第 168 題？"),
   "<strong>往返測試</strong>："
   "<code>titleToNumber(convertToTitle(n)) == n</code>，"
   "<strong>對幾千個隨機的 <code>n</code> 都要成立。</strong>",
   "<strong>本文的測試就是這樣做的</strong> —— "
   "<strong>它同時驗證了兩個函式，而且不依賴任何硬寫的期望值。</strong>",
   ("h", "追問二：Horner 法則還能用在哪？"),
   ("c", """【多項式求值】：

    p(x) = aₙxⁿ + ... + a₁x + a₀
         = (((aₙ·x + aₙ₋₁)·x + aₙ₋₂)·x + ...)·x + a₀

    n 次乘法（而不是 n(n+1)/2 次）✔

【應用】：

    - 字串轉數字（本題）
    - 字串雜湊（Rabin-Karp，第 28、187 題）
        hash = hash * base + char
    - CRC 校驗碼
    - 多項式的模運算（NTT、密碼學）

【Rabin-Karp 的滾動雜湊】就是 Horner 的變形：

    加一個字元： h = h * base + new
    去一個字元： h = h - old * base^(len-1)

    這讓「滑動視窗的雜湊」可以 O(1) 更新 ✔

    第 187 題（重複的 DNA 序列）就會用到。""",),
   ("h", "追問三：如果字串裡有小寫字母或其他字元呢？"),
   "<strong>題目保證只有大寫字母。</strong>"
   "如果要防禦性地處理：",
   ("c", """for c in columnTitle:
    if not ("A" <= c <= "Z"):
        raise ValueError(f"非法字元: {c}")
    n = n * 26 + ord(c) - 64

【或者先正規化】：
    columnTitle = columnTitle.strip().upper()

【真實的 Excel 公式解析器】要處理：
    - 小寫（a1 和 A1 是同一格）
    - 絕對參照（$A$1）
    - 工作表名稱（Sheet1!A1）
    - 範圍（A1:B10）

    那就不是一個迴圈能解決的了 ——
    需要一個真正的 tokenizer + parser。

【但這題的核心邏輯（n*26 + digit）
  在那個 parser 裡仍然是同一行。】""",),
   ("h", "追問四：為什麼「編碼」比「解碼」難？"),
   ("c", """【解碼】：讀懂一個【已經合法】的輸入

    只要「按照規則逐步累積」就好 ——
    輸入的合法性由提供者保證。

【編碼】：產生一個【必須合法】的輸出

    要處理：
        - 邊界（本題的「沒有 0」）
        - 格式（前導零、對齊、跳脫字元）
        - 唯一性（同一個值不能有兩種表示）

【這個不對稱在很多地方出現】：

    JSON：   parse 比 stringify 簡單（不用考慮縮排、跳脫）
    日期：   解析比格式化簡單（不用考慮時區顯示、語言）
    URL：    解析比組裝簡單（不用考慮編碼規則）

【所以「編碼器」的測試永遠要比「解碼器」更仔細】——

    而「往返測試」是最好的工具：
    它用簡單的解碼器來驗證複雜的編碼器 ✔""",),
 ],
 "related": [
   "<strong>第 168 題 Excel 表欄位名稱</strong> —— 反向運算，難得多",
   "<strong>第 8 題 字串轉整數</strong> —— 同樣的 Horner",
   "<strong>第 13 題 羅馬數字轉整數</strong> —— 另一種非標準編碼的解析",
   "<strong>第 187 題 重複的 DNA 序列</strong> —— Horner 的滾動雜湊版",
 ],
 "check": [
   "<code>n = n * 26 + digit</code> 為什麼是「從左到右」而不是「從右到左」？",
   "那個 <code>+1</code> 為什麼必要？",
   "Horner 法則比「算冪次再加總」省了多少次乘法？",
   "為什麼「解碼」通常比「編碼」簡單？",
 ],
})
print("P171 written")

# ==================== 169. Majority Element ====================
S["p169_boyer"] = '''class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand, count = None, 0

        for x in nums:
            if count == 0:
                cand = x                    # 票數歸零 -> 換人當候選
            count += 1 if x == cand else -1 # 同票 +1，不同票 -1

        return cand'''

S["p169_count"] = '''from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]'''

S["p169_sort"] = '''class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 出現次數 > n/2 的元素，排序後一定佔據正中間的位置
        nums.sort()
        return nums[len(nums) // 2]'''

S["p169_bit"] = '''class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 逐位元投票：多數元素的每一位，都是所有數字在那一位的「多數」
        n = len(nums)
        res = 0
        for b in range(32):
            ones = sum((x >> b) & 1 for x in nums)
            if ones > n // 2:
                res |= 1 << b
        return res - (1 << 32) if res >= (1 << 31) else res'''


def _p169_ref(nums):
    c = Counter(nums)
    n = len(nums)
    for k, v in c.items():
        if v > n // 2:
            return k
    return None


_p169 = [S.load(k) for k in ("p169_boyer", "p169_count", "p169_sort", "p169_bit")]

for nums, want in [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([1], 1),
    ([-1, -1, 2], -1),
    ([5, 5, 5, 5, 1, 2, 3], 5),
]:
    assert _p169_ref(nums) == want, ("P169 ref", nums)
    for sol in _p169:
        assert sol.majorityElement(list(nums)) == want, ("P169", nums, want, sol)

for _ in range(6000):
    n = random.randrange(1, 15)
    maj = random.randint(-30, 30)
    k = n // 2 + 1                          # 多數元素至少出現這麼多次
    nums = [maj] * k
    while len(nums) < n:
        v = random.randint(-30, 30)
        if v != maj:
            nums.append(v)
    random.shuffle(nums)
    assert _p169_ref(nums) == maj
    for sol in _p169:
        assert sol.majorityElement(list(nums)) == maj, ("P169 random", nums, maj, sol)
print("P169 solutions OK")

_P169_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ Boyer-Moore 投票法：把「不同的兩票」互相抵銷。多數票超過一半，所以最後一定剩下它。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">nums = [2, 2, 1, 1, 1, 2, 2]　（2 出現 4 次 &gt; 7/2）</text>
            <g font-size="12" text-anchor="middle">
              <text x="70" y="88" fill="var(--text-muted)" text-anchor="start">x</text>
              <text x="250" y="88" fill="var(--accent)">cand</text>
              <text x="420" y="88" fill="#ff8a65">count</text>
            </g>
            <g font-size="12" text-anchor="middle">
              <text x="70" y="116" fill="var(--text-muted)" text-anchor="start">2</text><text x="250" y="116" fill="var(--accent)">2</text><text x="420" y="116" fill="#ff8a65">1</text>
              <text x="70" y="142" fill="var(--text-muted)" text-anchor="start">2</text><text x="250" y="142" fill="var(--accent)">2</text><text x="420" y="142" fill="#ff8a65">2</text>
              <text x="70" y="168" fill="var(--text-muted)" text-anchor="start">1</text><text x="250" y="168" fill="var(--accent)">2</text><text x="420" y="168" fill="#ff8a65">1</text>
              <text x="70" y="194" fill="var(--text-muted)" text-anchor="start">1</text><text x="250" y="194" fill="var(--accent)">2</text><text x="420" y="194" fill="#ff8a65">0　← 歸零</text>
              <text x="70" y="220" fill="var(--text-muted)" text-anchor="start">1</text><text x="250" y="220" fill="#ff8a65">1　← 換人</text><text x="420" y="220" fill="#ff8a65">1</text>
              <text x="70" y="246" fill="var(--text-muted)" text-anchor="start">2</text><text x="250" y="246" fill="#ff8a65">1</text><text x="420" y="246" fill="#ff8a65">0　← 歸零</text>
              <text x="70" y="272" fill="var(--text-muted)" text-anchor="start">2</text><text x="250" y="272" fill="var(--gold)" font-size="14">2　← 換回來</text><text x="420" y="272" fill="var(--gold)">1</text>
            </g>
            <text x="20" y="306" fill="var(--gold)" font-size="12">最後 cand = 2 ✔</text>
            <line x1="20" y1="328" x2="620" y2="328" stroke="var(--border)"/>
            <text x="20" y="356" fill="var(--accent)" font-size="13">★ 為什麼一定對？</text>
            <text x="40" y="386" fill="var(--text-muted)" font-size="12">把這個過程想成「兩兩對決，不同陣營的互相消滅」：</text>
            <text x="60" y="412" fill="var(--text-muted)" font-size="12">每次 count 歸零，就代表「剛剛消滅了同樣多的『候選票』和『反對票』」。</text>
            <text x="60" y="440" fill="var(--gold)" font-size="12">多數元素的票數 &gt; n/2，其他全部加起來 &lt; n/2 ——</text>
            <text x="60" y="466" fill="var(--accent)" font-size="12">就算每一張反對票都用來消滅多數票，多數票也消不完 → 最後一定剩下它 ✔</text>'''

emit({
 "num": 169, "slug": "majority-element",
 "en": [
   "Given an array <code>nums</code> of size <code>n</code>, return <em>the majority element</em>.",
   "The majority element is the element that appears more than <code>⌊n / 2⌋</code> times. You "
   "may assume that the majority element <strong>always exists</strong> in the array.",
   "<strong>Follow up:</strong> Could you solve the problem in linear time and in "
   "<code>O(1)</code> space?",
 ],
 "zh": [
   "給你一個大小為 <code>n</code> 的陣列 <code>nums</code>，找出其中的<strong>多數元素</strong>。",
   "「多數元素」是指<strong>出現次數超過 <code>⌊n/2⌋</code> 次</strong>的元素。",
   "你可以假設<strong>多數元素一定存在</strong>。",
   "<strong>進階：</strong>能不能做到線性時間、<code>O(1)</code> 空間？",
 ],
 "pre": [
   ("note", "★ 「超過一半」這個條件比想像中強", [
     ("c", """出現次數 > n/2 帶來三個很強的性質：

    1. 【最多只有一個】這樣的元素
       （兩個都超過一半 -> 總數超過 n，矛盾）

    2. 【排序後它一定佔據正中間的位置】
       因為它連續佔了超過一半的格子 ->
       不管它在哪裡，都一定蓋住 index n//2 ✔
       -> 解法三只要兩行

    3. 【任何「兩兩抵銷不同元素」的過程，最後一定剩下它】
       因為它的票數比所有其他票加起來還多 ✔
       -> 這就是 Boyer-Moore 投票法（解法一）

【這三個性質都來自同一個事實：
  「超過一半」是一個非常強的優勢。】

    如果題目改成「出現次數 > n/3」（第 229 題），
    那最多有【兩個】這樣的元素，
    投票法就要維護【兩個】候選 ——
    複雜得多。

【讀題時要問：「這個條件讓什麼變得可能？」】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [3,2,3]
  輸出：3

範例 2
  輸入：nums = [2,2,1,1,1,2,2]
  輸出：2
  說明：2 出現 4 次，4 > 7/2 = 3.5 ✔""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 5 × 10⁴",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
   "<strong>多數元素一定存在</strong>",
 ],
 "idea": [
   ("fig", _P169_FIG, "0 0 640 492"),
   ("c", """【Boyer-Moore 投票法】

    cand, count = None, 0
    for x in nums:
        if count == 0:
            cand = x            # 沒有候選了 -> 換這個當候選
        count += 1 if x == cand else -1

    return cand

【直覺：兩兩對決，不同陣營的互相消滅】

    把每個元素想成一張票。

    每當出現「和候選不同」的票，
    就讓它和一張「候選票」同歸於盡（count -= 1）。

    count 歸零 = 「目前的候選已經被消滅光了」
    -> 換下一個元素當候選。

【★ 為什麼最後剩下的一定是多數元素？】

    設多數元素是 M，它出現了 k > n/2 次。
    其他所有元素加起來出現 n - k < n/2 次。

    【關鍵】：每次 count -= 1，都消耗掉
    「一張候選票」和「一張非候選票」。

    如果候選是 M：消耗一張 M 和一張非 M
    如果候選不是 M：消耗兩張非 M（或一張非 M 和一張 M）

    無論如何，【每次抵銷最多消耗一張 M】。

    非 M 的票只有 n - k < k 張 ->
    就算全部拿去抵銷 M，也消不完 ->
    最後一定還有 M 剩下 ✔

    而「剩下的」就是最後的 cand ✔

【更嚴格的論證】：

    把陣列切成若干段，每一段都是
    「count 從 0 升上去又回到 0」的一輪。

    每一輪裡，候選元素和非候選元素【數量相同】。

    最後一段（count 沒有歸零）的候選就是答案。

    因為前面每一段都「平手」，
    而 M 的總票數過半 -> 它一定在最後一段佔優勢 ✔

【複雜度】：O(n) 時間、O(1) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "Boyer-Moore 投票法（進階要求的答案）", [
     ("c", S["p169_boyer"]),
     "<strong>六行，O(n) 時間、O(1) 空間。</strong>"
     "<strong>這是題目要的答案。</strong>",
     ("h", "★ 如果「多數元素不一定存在」呢？"),
     ("c", """這個演算法會回傳【某一個元素】，但不保證是多數。

    nums = [1, 2, 3]（沒有多數元素）

        x=1: count=0 -> cand=1, count=1
        x=2: 不同 -> count=0
        x=3: count=0 -> cand=3, count=1

        回傳 3 ✘（它只出現一次）

【修正：加第二趟驗證】

    cand = <投票法的結果>
    if nums.count(cand) > len(nums) // 2:
        return cand
    return -1       # 沒有多數元素

    多一趟 O(n)，總複雜度不變 ✔

【題目保證存在，所以可以省略】——
    但面試時要主動說「如果不保證存在，我會加一趟驗證」。

    【「投票法只能找出『候選』，不能保證它是答案」
      是這個演算法最重要的注意事項。】""",),
     ("h", "為什麼 <code>count == 0</code> 時才換候選？"),
     ("c", """count 代表「目前的候選還剩幾張淨票」。

    count > 0 -> 候選還「活著」，繼續和新來的對決
    count == 0 -> 候選被消滅光了，換新的上

【常見的錯誤寫法】：

    if x == cand: count += 1
    else:
        count -= 1
        if count < 0:           ✘ 應該是 == 0 時換
            cand = x; count = 1

    這個版本其實也對（只是換人的時機晚一步），
    但本文的寫法更簡潔。

【另一個錯誤】：

    if count == 0:
        cand = x
        count = 1               ✘ 少了後面的 count += 1
    else:
        count += 1 if x == cand else -1

    這樣「換人」那一輪只加 1 次 —— 其實是對的。
    但本文的寫法把兩件事合併了：
        先換人（如果需要），再統一算票 ——
        換人之後 x == cand 必然成立 -> count += 1 ✔

    【合併之後少一個分支，也少一個出錯的機會。】""",),
   ], "O(n)", "O(1)", "掃一遍", "兩個變數", optimal=True),

   ap("解法二", "排序後取中間（兩行）", [
     ("c", S["p169_sort"]),
     ("c", """nums.sort()
return nums[len(nums) // 2]

【為什麼一定對？】

    多數元素出現 k > n/2 次，排序後它們是【連續】的。

    這一段的長度 > n/2，所以不管它從哪裡開始，
    都一定會蓋住索引 n//2：

        最左的情況：佔據 [0, k-1]，而 k-1 >= n//2 ✔
        最右的情況：佔據 [n-k, n-1]，而 n-k <= n//2 ✔

    兩種極端都蓋住中間 -> 任何位置都蓋住 ✔

【O(n log n) 時間，不滿足進階要求】——
    但它【兩行】，而且正確性一句話說得完。

【面試時的用法】：

    「最簡單的做法是排序後取中間，O(n log n)。
      如果要線性時間和常數空間，我用 Boyer-Moore 投票法。」

    然後寫解法一。

【注意它會修改輸入】——
    要保留原陣列的話用 sorted(nums)[n//2]，
    那就變成 O(n) 空間了。""",),
   ], "O(n log n)", "O(1) 或 O(n)", "排序主導", "視是否原地排序"),

   ap("解法三", "<code>Counter</code>（最直白）", [
     ("c", S["p169_count"]),
     "<strong>一行。O(n) 時間、O(n) 空間。</strong>",
     ("c", """Counter(nums).most_common(1)[0][0]

    most_common(k) 回傳「出現次數最多的 k 個」，
    格式是 [(元素, 次數), ...]

    所以 [0][0] 是「最多的那個元素」✔

【因為題目保證有多數元素，
  所以「出現最多的」就是它 ✔】

【空間 O(n)】-> 不滿足進階要求。

【但它是最好的「參考實作」】——
    本文的測試就是用 Counter 驗證其他三個解法。

【Counter 的其他用法】：

    Counter(nums)[x]          x 出現幾次（不存在回 0，不會 KeyError）
    Counter(a) - Counter(b)   多重集合的差
    Counter(a) & Counter(b)   交集（取較小的次數）
    sum(c.values())           總數

    處理「計數」問題時，先想想 Counter。""",),
   ], "O(n)", "O(n)", "數次數", "雜湊表"),

   ap("解法四", "逐位元投票（另一個角度）", [
     ("c", S["p169_bit"]),
     ("c", """對每一個位元 b，數「有幾個數字在那一位是 1」。

    如果 > n/2，那多數元素在那一位就是 1 ✔

【為什麼？】

    多數元素出現 > n/2 次。

    如果它在第 b 位是 1，那至少有 n/2 個數字在那一位是 1
    -> ones > n/2 ✔

    如果它在第 b 位是 0，那至少有 n/2 個數字在那一位是 0
    -> ones < n/2 ✔

    所以「那一位的多數」就是「多數元素的那一位」✔

【O(32n) 時間、O(1) 空間】——
    也滿足進階要求，但比 Boyer-Moore 慢 32 倍。

【最後那行負數處理】

    和第 137 題一樣 ——
    Python 的整數沒有位寬，
    重新組裝出來的數要手動轉回有號 ✔

【這個解法的價值】：

    它展示了「多數」這個性質可以【逐位元獨立】地判斷。

    而且它能推廣到「找出 > n/k 的元素」嗎？
    —— 不行，因為「> n/3 的元素在某位是 1」
       不代表「那位的 1 超過 n/3」（可能有兩個這樣的元素）。

    【所以這個技巧【只對「超過一半」有效】。】""",),
   ], "O(32n)", "O(1)", "32 位 × n", "幾個變數"),
 ],
 "compare": (["解法", "時間", "空間", "滿足進階", "行數"],
   [["一、Boyer-Moore", "O(n)", "O(1)", "✔", "6"],
    ["二、排序取中間", "O(n log n)", "O(1)", "✘", "2"],
    ["三、Counter", "O(n)", "O(n)", "✘", "1"],
    ["四、逐位元投票", "O(32n)", "O(1)", "✔", "8"]]),
 "edges": [
   "<strong>單一元素</strong> <code>[1]</code> → <code>1</code>。",
   "<strong>多數元素在開頭</strong> <code>[5,5,5,5,1,2,3]</code> → <code>5</code>。",
   "<strong>多數元素在結尾</strong> <code>[1,2,3,5,5,5,5]</code> → <code>5</code>。",
   "<strong>剛好過半</strong>（<code>n=3</code>，出現 2 次）→ 正確。",
   "<strong>有負數</strong> <code>[-1,-1,2]</code> → <code>-1</code>。"
   "<strong>解法四要處理負數的位元表示。</strong>",
   "<strong>多數元素不存在</strong>（題目保證不會）→ "
   "<strong>Boyer-Moore 會回傳某個元素，但那不是答案 —— 需要第二趟驗證。</strong>",
   "<strong>5 × 10⁴ 個元素</strong> → 四種解法都夠快。",
 ],
 "follow": [
   ("h", "追問一：如果要找「出現超過 n/3 次」的元素呢？"),
   "<strong>第 229 題</strong>。<strong>最多有兩個</strong>這樣的元素"
   "（三個的話總數會超過 n）。",
   ("c", """Boyer-Moore 要維護【兩個】候選：

    c1 = c2 = None
    n1 = n2 = 0
    for x in nums:
        if x == c1:   n1 += 1
        elif x == c2: n2 += 1
        elif n1 == 0: c1, n1 = x, 1
        elif n2 == 0: c2, n2 = x, 1
        else:         n1 -= 1; n2 -= 1     ★ 兩個一起減

    然後【必須第二趟驗證】——
    因為「超過 n/3」的元素可能一個都沒有。

【★ 分支的順序很重要】：

    必須先檢查「x 是不是已有的候選」，
    再檢查「有沒有空位」。

    順序反了的話，同一個值可能佔據兩個候選位 ✘

【推廣到 > n/k】：
    維護 k-1 個候選，每次抵銷時 k 個一起減。

    這叫做 Misra-Gries 演算法 ——
    它是「串流資料的頻繁項目」（heavy hitters）
    這個經典問題的基礎。""",),
   ("h", "追問二：Boyer-Moore 在真實世界有什麼用？"),
   ("c", """【串流處理（streaming）】：

    資料一筆一筆來，記憶體放不下全部，
    但要知道「最頻繁的項目」。

    例如：
        - 網路流量裡的「重度使用者」
        - 搜尋引擎的熱門查詢
        - 分散式系統的「熱點」偵測

    Boyer-Moore（和它的推廣 Misra-Gries）
    只要 O(k) 空間就能找出「候選」——
    然後用第二趟（或抽樣）驗證。

【Count-Min Sketch】是另一個方向：
    用雜湊 + 計數陣列做「近似頻率估計」，
    空間 O(1/ε · log(1/δ))。

    Redis、Apache Spark、資料庫的查詢優化器
    都用這類演算法。

【所以這題不是「面試花招」】——
    它是一個真實系統會用到的演算法。""",),
   ("h", "追問三：能不能用分治法？"),
   ("c", """可以：

    def majority(lo, hi):
        if lo == hi: return nums[lo]
        mid = (lo + hi) // 2
        left = majority(lo, mid)
        right = majority(mid+1, hi)
        if left == right: return left
        # 不同 -> 數哪個在整段裡比較多
        lc = count(left, lo, hi)
        rc = count(right, lo, hi)
        return left if lc > rc else right

    T(n) = 2T(n/2) + O(n) -> O(n log n)

【為什麼這樣對？】

    如果 M 是整段的多數，
    那它至少在【左半或右半】的其中一邊也是多數 ——

    （反證：如果兩邊都不是多數，
      那 M 在左半 <= mid-lo+1 的一半，
      在右半 <= hi-mid 的一半，
      加起來 <= 整段的一半 -> 不是多數 ✘）

    所以答案一定在 {left, right} 之中 ✔

【它比 Boyer-Moore 慢，但展示了一個有用的論證】：

    「全域的多數，一定是某個子區間的多數」。

    這類「性質可以往下傳遞」的結構，
    正是分治法能用的前提。""",),
   ("h", "追問四：為什麼「排序後取中間」這麼簡單卻常被忽略？"),
   "<strong>因為大家一看到「找多數」就想「數次數」</strong> —— "
   "<strong>而忘了「超過一半」這個條件本身就決定了它的位置。</strong>",
   "<strong>這是一個很好的提醒</strong>："
   "<strong>先想清楚「題目的條件保證了什麼」，再想演算法。</strong>",
   "<strong>很多時候，一個強的條件會讓問題退化成一行。</strong>",
 ],
 "related": [
   "<strong>第 229 題 求眾數 II</strong> —— 超過 n/3，要兩個候選",
   "<strong>第 1150 題 檢查一個數是否在陣列中佔絕大多數</strong> —— 有序版",
   "<strong>第 136 題 只出現一次的數字</strong> —— 另一個「抵銷」的思路",
   "<strong>第 215 題 陣列中的第 K 個最大元素</strong> —— 另一個「不用完整排序」",
 ],
 "check": [
   "「超過一半」這個條件保證了哪三件事？",
   "Boyer-Moore 為什麼一定會剩下多數元素？請說出那個「抵銷」的論證。",
   "如果多數元素不保證存在，這個演算法要怎麼修？",
   "為什麼「排序後取中間」一定對？",
 ],
})
print("P169 written")

# ==================== 172. Factorial Trailing Zeroes ====================
S["p172"] = '''class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 末尾的 0 = 因數 10 的個數 = min(2 的個數, 5 的個數) = 5 的個數
        cnt = 0
        while n:
            n //= 5
            cnt += n            # 每次除 5，累加「還剩幾個數是這一層 5 的倍數」
        return cnt'''

S["p172_loop"] = '''class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Legendre 公式：n/5 + n/25 + n/125 + ...
        cnt = 0
        p = 5
        while p <= n:
            cnt += n // p
            p *= 5
        return cnt'''

S["p172_brute"] = '''class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 對每個數字數它含有幾個因數 5（能過但慢，而且沒抓到重點）
        cnt = 0
        for i in range(5, n + 1, 5):
            x = i
            while x % 5 == 0:
                cnt += 1
                x //= 5
        return cnt'''


def _p172_ref(n):
    """獨立參考解：真的算階乘，然後數尾巴的 0（只對小 n 用）。"""
    f = math_factorial(n)
    s = str(f)
    return len(s) - len(s.rstrip("0"))


def math_factorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


_p172 = [S.load(k) for k in ("p172", "p172_loop", "p172_brute")]

for n, want in [(3, 0), (5, 1), (0, 0), (25, 6), (30, 7), (100, 24), (125, 31)]:
    assert _p172_ref(n) == want, ("P172 ref", n, _p172_ref(n))
    for sol in _p172:
        assert sol.trailingZeroes(n) == want, ("P172", n, want, sol)

for n in range(0, 300):
    want = _p172_ref(n)
    for sol in _p172:
        assert sol.trailingZeroes(n) == want, ("P172 small", n, want, sol)
# 大的 n：三種解法互相對照
for _ in range(2000):
    n = random.randint(0, 10 ** 4)
    vals = [sol.trailingZeroes(n) for sol in _p172]
    assert len(set(vals)) == 1, ("P172 disagree", n, vals)
print("P172 solutions OK")

_P172_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 末尾的 0 從哪裡來？每一個 10 = 2 × 5。而 2 的因數遠多於 5 —— 所以「數 5 就好」。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">n = 25 時，1×2×…×25 裡有幾個因數 5？</text>
            <g font-size="12">
              <text x="40" y="86" fill="var(--text-muted)">5 的倍數：　5, 10, 15, 20, 25　　→　25 // 5 = 5 個</text>
              <text x="40" y="114" fill="var(--accent)">25 的倍數：25　　　　　　　　　→　25 // 25 = 1 個（它多貢獻一個 5）</text>
              <text x="40" y="142" fill="var(--text-muted)">125 的倍數：無　　　　　　　　　→　25 // 125 = 0</text>
              <text x="40" y="176" fill="var(--gold)" font-size="14">總共 5 + 1 = 6 個因數 5　→　25! 末尾有 6 個 0 ✔</text>
            </g>
            <line x1="20" y1="202" x2="620" y2="202" stroke="var(--border)"/>
            <text x="20" y="230" fill="var(--accent)" font-size="13">★ 為什麼「25 要算兩次」？</text>
            <text x="40" y="258" fill="var(--text-muted)" font-size="12">25 = 5 × 5，它含有【兩個】因數 5。</text>
            <text x="40" y="284" fill="var(--text-muted)" font-size="12">「5 的倍數」那一輪已經算了它一次，「25 的倍數」那一輪再補算一次 ✔</text>
            <text x="40" y="312" fill="var(--gold)" font-size="12">同理 125 = 5³ 要算三次（會在前三輪各被算到一次）。</text>
            <line x1="20" y1="336" x2="620" y2="336" stroke="var(--border)"/>
            <text x="20" y="364" fill="#ff8a65" font-size="13">★ 為什麼 2 的個數一定夠？</text>
            <text x="40" y="392" fill="var(--text-muted)" font-size="12">每 2 個數就有一個 2 的倍數，每 5 個數才有一個 5 的倍數 ——</text>
            <text x="40" y="418" fill="var(--gold)" font-size="12">2 的因數個數 ≈ n/2 + n/4 + … ≈ n　　5 的因數個數 ≈ n/5 + n/25 + … ≈ n/4</text>
            <text x="40" y="446" fill="var(--accent)" font-size="12">2 的數量遠遠超過 5 → 能配成幾個 10，完全由 5 的數量決定 ✔</text>'''

emit({
 "num": 172, "slug": "factorial-trailing-zeroes",
 "en": [
   "Given an integer <code>n</code>, return <em>the number of trailing zeroes in </em>"
   "<code>n!</code>.",
   "Note that <code>n! = n × (n - 1) × (n - 2) × ... × 3 × 2 × 1</code>.",
   "<strong>Follow up:</strong> Could you write a solution that works in logarithmic time "
   "complexity?",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，回傳 <code>n!</code>（<code>n</code> 的階乘）"
   "<strong>末尾有幾個 0</strong>。",
   "<strong>進階：</strong>你能寫出對數時間的解法嗎？",
 ],
 "pre": [
   ("note", "★ 第一步：末尾的 0 從哪裡來？", [
     ("c", """每一個末尾的 0，代表一個因數 10。

    而 10 = 2 × 5

    所以：
        末尾 0 的個數 = 「能湊出幾個 (2, 5) 的配對」
                      = min(因數 2 的個數, 因數 5 的個數)

【★ 而 2 的個數【永遠】比 5 多】

    在 1..n 裡：
        2 的倍數有 n/2 個
        5 的倍數只有 n/5 個

    更精確地：
        因數 2 的總數 ≈ n/2 + n/4 + n/8 + ... ≈ n
        因數 5 的總數 ≈ n/5 + n/25 + ...      ≈ n/4

    2 的數量大約是 5 的四倍 ->
    【5 永遠是瓶頸】✔

    所以：
        答案 = 「1..n 的乘積裡，因數 5 的總個數」

【第二步：怎麼數因數 5？】

    5 的倍數（5, 10, 15, ...）各貢獻【至少】一個 5
        -> n // 5 個

    但 25 = 5² 貢獻【兩個】5 ——
    上面只算了一次，要再補一次
        -> n // 25 個

    125 = 5³ 貢獻三個，再補一次
        -> n // 125 個

    ...

    總共：n//5 + n//25 + n//125 + ...

【這就是 Legendre 公式】（勒讓德公式）。

    項數是 O(log₅ n) -> 滿足進階要求 ✔"""),
   ]),
 ],
 "examples": """範例 1
  輸入：n = 3
  輸出：0
  說明：3! = 6，末尾沒有 0。

範例 2
  輸入：n = 5
  輸出：1
  說明：5! = 120，末尾有一個 0。

範例 3
  輸入：n = 0
  輸出：0
  說明：0! = 1。""",
 "constraints": [
   "0 ≤ <code>n</code> ≤ 10⁴",
 ],
 "idea": [
   ("fig", _P172_FIG, "0 0 640 470"),
   ("c", """【Legendre 公式】

    n! 裡質因數 p 的個數 = Σ_{i>=1} ⌊n / p^i⌋

    對 p = 5：
        n//5 + n//25 + n//125 + ...

【兩種等價的寫法】

    寫法 A（除到 0）：
        cnt = 0
        while n:
            n //= 5
            cnt += n

        第一輪：n 變成 n//5，累加 n//5
        第二輪：n 變成 n//25，累加 n//25
        ...
        n 變成 0 -> 結束 ✔

        【最精簡，而且不會溢位】。

    寫法 B（乘冪）：
        p = 5
        while p <= n:
            cnt += n // p
            p *= 5

        直接算 n//5, n//25, ...

        【更貼近公式，但 p 可能溢位】
        （在 C++/Java 裡 p *= 5 可能超過 int，
          要寫成 while p <= n / 5 之類的）✘

    寫法 A 沒有這個問題 -> 推薦 ✔

【★ 為什麼「除到 0」等價於「加冪次」？】

    ⌊⌊n/5⌋/5⌋ = ⌊n/25⌋

    這是「巢狀向下取整」的性質：
        ⌊⌊n/a⌋/b⌋ = ⌊n/(ab)⌋   （a, b 是正整數）

    所以連續除 5，就等於依序得到
        n//5, n//25, n//125, ... ✔

    【這個恆等式很有用，值得記住。】

【複雜度】：O(log₅ n) 時間、O(1) 空間 ✔

    n = 10^4 時只要 6 輪。"""),
 ],
 "approaches": [
   ap("解法一", "連續除 5（最精簡，也最安全）", [
     ("c", S["p172"]),
     "<strong>六行，O(log n) 時間、O(1) 空間。</strong>",
     ("h", "手動走一遍 <code>n = 100</code>"),
     ("c", """n=100: n //= 5 -> 20, cnt = 20
n=20:  n //= 5 -> 4,  cnt = 24
n=4:   n //= 5 -> 0,  cnt = 24
n=0:   結束

答案 24 ✔

驗證：100! 末尾確實有 24 個 0。

    100//5 = 20      （5,10,...,100 共 20 個）
    100//25 = 4      （25,50,75,100 各多一個 5）
    100//125 = 0
    20 + 4 = 24 ✔""",),
     ("h", "為什麼這個寫法不會溢位？"),
     ("c", """n 一路變小（每次除 5），永遠不會變大 ✔

【對照寫法 B】：

    p = 5
    while p <= n:
        cnt += n // p
        p *= 5

    p 一路變大 —— 最後一次 p *= 5 可能超過 int 範圍。

    n = 10^9 時：
        p 會到 5^13 = 1220703125（還在 int 內）
        再乘一次 -> 6103515625 > 2^31 ✘ 溢位

    在 C++/Java 裡要改成：
        while (n / p >= 1) { cnt += n / p; if (p > n / 5) break; p *= 5; }

    很醜。

【寫法 A 從根本上避免了這個問題】——
    因為它只做除法，不做乘法。

    【「讓變數一路變小」比「一路變大」安全 ——
      這是避免溢位的一個通用原則。】""",),
   ], "O(log n)", "O(1)", "每次除 5", "一個變數", optimal=True),

   ap("解法二", "直接照公式算冪次", [
     ("c", S["p172_loop"]),
     "<strong>更貼近 Legendre 公式的形式，讀起來更「像數學」。</strong>",
     "<strong>但 <code>p *= 5</code> 在其他語言裡有溢位風險</strong>（見解法一的說明）。",
     "<strong>Python 沒有這個問題，所以兩種寫法都可以。</strong>",
   ], "O(log n)", "O(1)", "同解法一", "兩個變數"),

   ap("解法三", "對每個數字數因數 5（能過但沒抓到重點）", [
     ("c", S["p172_brute"]),
     ("c", """for i in range(5, n+1, 5):
    x = i
    while x % 5 == 0:
        cnt += 1
        x //= 5

    對每個 5 的倍數，數它含有幾個因數 5。

    O(n/5 × log₅ n) ≈ O(n) 時間。

【n <= 10^4 時完全夠快】，但：

    ✘ 不滿足「對數時間」的進階要求
    ✘ 而且它【沒有抓到這題的重點】——

       重點是「Legendre 公式把逐個計數
       壓縮成 log 項的求和」。

【什麼時候這個差別會致命？】

    如果 n 可以到 10^9：
        解法一：6 輪 ✔
        解法三：2 億次迴圈 ✘

    LeetCode 這題的 n <= 10^4，
    所以解法三能過 ——
    但那只是題目手下留情。

【放在這裡是為了對照】：

    「能通過」和「解決了問題」是兩件事。
    面試官問「進階」的時候，就是在問這個差別。""",),
   ], "O(n)", "O(1)", "逐個數字數因數", "一個變數"),
 ],
 "compare": (["解法", "時間", "溢位風險", "符合進階", "備註"],
   [["一、連續除 5", "O(log n)", "✘", "✔", "最安全"],
    ["二、算冪次", "O(log n)", "✔ 其他語言", "✔", "最像公式"],
    ["三、逐個數", "O(n)", "✘", "✘", "n 大時會爆"]]),
 "edges": [
   "<strong><code>n = 0</code></strong> → <code>0</code>（<code>0! = 1</code>）。"
   "<strong><code>while n</code> 一次都不跑 ✔</strong>",
   "<strong><code>n = 3</code></strong> → <code>0</code>（<code>3! = 6</code>）。",
   "<strong><code>n = 5</code></strong> → <code>1</code>。",
   "<strong><code>n = 25</code></strong> → <code>6</code>（不是 5）。"
   "<strong>25 貢獻兩個 5 —— 只算 <code>n//5</code> 會答 5。本題第一名的 bug。</strong>",
   "<strong><code>n = 125</code></strong> → <code>31</code>（<code>25 + 5 + 1</code>）。",
   "<strong><code>n = 100</code></strong> → <code>24</code>。",
   "<strong>只算 <code>n // 5</code></strong> → <strong>所有 25 的倍數都會少算。</strong>",
   "<strong>真的去算階乘</strong> → <code>10⁴!</code> 有 35660 位數，"
   "<strong>Python 算得出來但很慢；其他語言直接溢位。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果要問「末尾有幾個某個數字」呢？"),
   ("c", """【末尾的 0 個數】= min(2 的個數, 5 的個數) = 5 的個數 ✔（本題）

【末尾在 base-b 下有幾個 0】？

    把 b 質因數分解：b = p₁^e₁ · p₂^e₂ · ...

    答案 = min over i of ⌊(n! 裡 pᵢ 的個數) / eᵢ⌋

    例如 base 12 = 2² · 3：
        答案 = min(⌊(2 的個數)/2⌋, (3 的個數))

        2 的個數 ≈ n，3 的個數 ≈ n/2
        -> min(n/2, n/2) —— 兩者接近，要真的算

【所以「數 5 就好」只對 base 10 成立】——

    因為 10 = 2 × 5 而且 5 明顯是瓶頸。

    換一個底數，就要兩個都算 ✔

【這個一般化很值得想一遍】——
    它能檢驗你是不是真的懂「為什麼數 5 就好」。""",),
   ("h", "追問二：反過來，「末尾有 k 個 0 的最小 n」呢？"),
   ("c", """第 793 題（階乘函數後 K 個零）。

    f(n) = n 的階乘末尾 0 的個數，是【單調不減】的
    -> 可以【二分搜尋】✔

    def smallest_n_with_k_zeros(k):
        lo, hi = 0, 5 * (k + 1)     # 上界：5k 附近一定夠
        while lo < hi:
            mid = (lo + hi) // 2
            if trailingZeroes(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo if trailingZeroes(lo) == k else -1

【★ 有趣的地方：f(n) 會「跳過」某些值】

    f(24) = 4
    f(25) = 6      ← 跳過了 5！

    因為 25 一口氣貢獻兩個 5。

    所以「末尾剛好 5 個 0」的 n 【不存在】——

    第 793 題問的是「有幾個 n 滿足 f(n) = k」，
    答案永遠是 0 或 5
    （因為 f 每 5 個數才增加一次）。

【這是一個很漂亮的觀察】：
    「單調但會跳號」的函數，
    二分搜尋仍然能用，但要額外檢查「找到的值對不對」。""",),
   ("h", "追問三：Legendre 公式還有什麼用？"),
   ("ul", [
     "<strong>算組合數 C(n,k) 的質因數分解</strong>：<code>(n! 裡 p 的個數) − (k! 裡的) − ((n−k)! 裡的)</code>",
     "<strong>判斷 C(n,k) 能不能被某個質數整除</strong>（Kummer 定理）",
     "<strong>算 n! mod p^k</strong>（Wilson 定理的推廣、Lucas 定理）",
     "<strong>競賽裡「大組合數取模」的標準工具</strong>",
   ]),
   ("c", """【Kummer 定理】（和 Legendre 公式密切相關）：

    C(n, k) 裡質因數 p 的次數
      = 「在 p 進位下，k + (n-k) 做加法時的【進位次數】」

    例如 C(5,2) = 10：
        p = 5：2 + 3 = 5 在 5 進位下是 "2" + "3" = "10" -> 進位 1 次
        -> 10 裡有 5^1 ✔

【這類「質因數計數」的技巧，
  是數論類題目的基本功】——

    而本題（數 5 的個數）是它最簡單的入口。""",),
   ("h", "追問四：為什麼不能直接算 <code>n!</code> 再數 0？"),
   ("c", """n = 10^4 時，10000! 有【35660 位數】。

    Python 算得出來（大整數），
    但要花很久（大整數乘法不是 O(1)）。

    而且轉成字串、再數尾巴的 0，
    又是 O(位數) 的操作。

    總共大約 O(n² log n) —— 慢了好幾個數量級。

【在 C++/Java 裡根本算不出來】（早就溢位）。

【這是「不要算出整個東西，只算你要的部分」的典型例子】：

    要「末尾 0 的個數」-> 只要數因數 5
    不需要知道 n! 到底是多少 ✔

    同樣的思路：
        第 96 題：用卡塔蘭數公式，不用真的生成所有 BST
        第 62 題：用組合數，不用真的走過所有路徑
        第 233 題：數 1 出現的次數，不用真的寫出所有數字

    【「只算需要的」常常能把指數／多項式降到對數。】""",),
 ],
 "related": [
   "<strong>第 793 題 階乘函數後 K 個零</strong> —— 反向問題，用二分",
   "<strong>第 62 題 不同路徑</strong> —— 另一個「用公式取代枚舉」",
   "<strong>第 96 題 不同的二元搜尋樹</strong> —— 同上",
   "<strong>第 233 題 數字 1 的個數</strong> —— 另一個「數位計數」問題",
 ],
 "check": [
   "為什麼「末尾 0 的個數」等於「因數 5 的個數」，而不用管 2？",
   "為什麼 25 要被算兩次？125 呢？",
   "「連續除 5」和「n//5 + n//25 + ...」為什麼等價？",
   "如果改成「base 12 下末尾有幾個 0」，答案要怎麼算？",
 ],
})
print("P172 written")
