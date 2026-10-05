# -*- coding: utf-8 -*-
"""第 713、714、715、717、718、719、720、721 題。"""
import random, bisect
from collections import defaultdict
from functools import lru_cache
from authoring import ap
from lcauto import em
from runner import Src

S = Src()
random.seed(713)


# ==================== 713. Subarray Product Less Than K ====================
S["p713"] = '''class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0                            # 所有數 >= 1，乘積不可能 < 1
        prod, l, res = 1, 0, 0
        for r, x in enumerate(nums):
            prod *= x
            while prod >= k:
                prod //= nums[l]                # 太大：從左邊縮小視窗
                l += 1
            res += r - l + 1                    # ★ 以 r 結尾、乘積 < k 的子陣列：起點可以是 l..r
        return res'''

_p713 = S.load("p713")
for _ in range(3000):
    a = [random.randint(1, 6) for _ in range(random.randint(1, 9))]; k = random.randint(0, 40)
    want = 0
    for i in range(len(a)):
        p = 1
        for j in range(i, len(a)):
            p *= a[j]
            if p < k: want += 1
    assert _p713.numSubarrayProductLessThanK(a, k) == want
print("P713 OK")

em({
 "num": 713, "title": "乘積小於 K 的子陣列",
 "desc": "所有數都是正數，乘積隨視窗擴大單調增加：滑動視窗，每個右端點貢獻 r − l + 1 個子陣列。",
 "zh": ["給你一個<strong>正整數</strong>陣列 <code>nums</code> 和整數 <code>k</code>，回傳乘積<strong>嚴格小於</strong> <code>k</code> 的連續子陣列個數。"],
 "idea": [
   ("c", """【單調性】
    全部是正數 -> 視窗變大乘積不減、變小乘積不增。
    可以用滑動視窗。

【每個右端點 r】
    維持最左的 l，使 nums[l..r] 的乘積 < k。
    那麼 nums[l..r]、nums[l+1..r]、...、nums[r..r] 都 < k
    （它們是 nums[l..r] 的後綴，乘積更小）。
    -> 以 r 結尾的合法子陣列有 r - l + 1 個。

【k <= 1】
    所有正整數乘積 >= 1，一個都沒有。
    （也避免 while 迴圈把 l 推過 r。）"""),
 ],
 "approaches": [
   ap("解法", "滑動視窗", [("c", S["p713"]), "驗證方式：和雙重迴圈比對 3000 組。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>k ≤ 1</strong> → 0。", "<strong>單一元素 ≥ k</strong> → 視窗縮成空的（l = r + 1），貢獻 0。"],
 "follow": [("h", "對數轉換"), ("c", "也可以取 log 把乘積變成和：log(prod) < log k，再對前綴和二分。但有浮點誤差，滑動視窗更好。")],
 "related": ["<strong>第 209 題 長度最小的子陣列</strong>", "<strong>第 560 題 和為 K 的子陣列</strong>", "<strong>第 2302 題 統計得分小於 K 的子陣列數目</strong>"],
 "check": ["為什麼以 r 結尾的合法子陣列有 r − l + 1 個？", "k ≤ 1 為什麼要特判？"],
})


# ==================== 714. Best Time to Buy and Sell Stock with Transaction Fee ====================
S["p714"] = '''class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]              # cash：手上沒股票的最大收益；hold：持有股票
        for p in prices[1:]:
            # ★ 賣出時付手續費；用舊的 hold 算新的 cash
            cash, hold = max(cash, hold + p - fee), max(hold, cash - p)
        return cash'''

_p714 = S.load("p714")
assert _p714.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8 and _p714.maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
@lru_cache(None)
def _bf714(prices, fee, i, holding):
    if i == len(prices): return 0
    best = _bf714(prices, fee, i + 1, holding)
    if holding: best = max(best, prices[i] - fee + _bf714(prices, fee, i + 1, False))
    else: best = max(best, -prices[i] + _bf714(prices, fee, i + 1, True))
    return best
for _ in range(1500):
    p = tuple(random.randint(1, 10) for _ in range(random.randint(1, 9))); f = random.randint(0, 4)
    assert _p714.maxProfit(list(p), f) == _bf714(p, f, 0, False)
print("P714 OK")

em({
 "num": 714, "title": "買賣股票的最佳時機含手續費",
 "desc": "股票系列的兩狀態 DP（持有／不持有），每次賣出扣一次手續費。",
 "zh": [
   "給你每天的股價 <code>prices</code> 與每筆交易的手續費 <code>fee</code>。可以交易任意多次，但同一時間最多持有一股（必須先賣出才能再買），每筆交易（一買一賣）要付一次手續費。",
   "回傳能獲得的最大利潤。",
 ],
 "idea": [
   ("c", """【兩個狀態】
    cash：今天結束時手上沒有股票的最大收益
    hold：今天結束時持有股票的最大收益

【轉移】
    cash = max(昨天就沒有, 昨天持有今天賣出 hold + p - fee)
    hold = max(昨天就持有, 昨天沒有今天買入 cash - p)

【同一天買又賣？】
    用新的 cash 算 hold 等於當天賣了又買，
    手續費讓這種操作只會虧，不影響答案；
    但同時賦值最乾淨。

    和第 122 題（無限次交易）只差一個 fee。"""),
 ],
 "approaches": [
   ap("解法", "持有／不持有兩狀態 DP", [("c", S["p714"]), "驗證方式：和記憶化搜尋比對 1500 組。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>手續費大於任何價差</strong> → 0。", "<strong>單日</strong> → 0。"],
 "follow": [("h", "股票系列"), ("c", "第 121 題（一次）、122 題（無限次）、123 題（兩次）、188 題（k 次）、309 題（冷凍期）、714 題（手續費）——全部可以用「持有／不持有」狀態機統一處理。")],
 "related": ["<strong>第 122 題 買賣股票的最佳時機 II</strong>", "<strong>第 309 題 最佳買賣股票時機含冷凍期</strong>", "<strong>第 188 題 買賣股票的最佳時機 IV</strong>"],
 "check": ["cash 和 hold 分別代表什麼？", "手續費應該在哪個轉移中扣除？"],
})


# ==================== 715. Range Module ====================
S["p715"] = '''class RangeModule:
    def __init__(self):
        self.iv = []                    # 排序、互不重疊、也不相接的區間端點：[l1, r1, l2, r2, ...]

    def addRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.iv, left)
        j = bisect.bisect_right(self.iv, right)
        # ★ 落在 [i, j) 的端點全部被吞掉；偶數索引代表「在區間外」，要補上新的端點
        new = ([left] if i % 2 == 0 else []) + ([right] if j % 2 == 0 else [])
        self.iv[i:j] = new

    def queryRange(self, left: int, right: int) -> bool:
        i = bisect.bisect_right(self.iv, left)
        j = bisect.bisect_left(self.iv, right)
        return i == j and i % 2 == 1    # left 與 right 落在同一個區間內

    def removeRange(self, left: int, right: int) -> None:
        i = bisect.bisect_left(self.iv, left)
        j = bisect.bisect_right(self.iv, right)
        new = ([left] if i % 2 == 1 else []) + ([right] if j % 2 == 1 else [])
        self.iv[i:j] = new'''

_RM = S.loadns("p715")["RangeModule"]
for _ in range(400):
    o = _RM(); cov = [False] * 30
    for _ in range(30):
        l = random.randint(0, 27); r = random.randint(l + 1, 29); op = random.randint(0, 2)
        if op == 0:
            o.addRange(l, r)
            for x in range(l, r): cov[x] = True
        elif op == 1:
            o.removeRange(l, r)
            for x in range(l, r): cov[x] = False
        else:
            assert o.queryRange(l, r) == all(cov[l:r]), (l, r)
print("P715 OK")

em({
 "num": 715, "title": "Range 模組",
 "desc": "把所有區間的端點存成一個排序陣列：索引的奇偶代表「在區間內／外」，加入與刪除都是一次二分加切片替換。",
 "zh": [
   "設計一個追蹤數字範圍的模組，範圍以<strong>半開區間</strong> <code>[left, right)</code> 表示：",
   ("ul", ["<code>addRange(left, right)</code>：開始追蹤 [left, right) 中所有實數（與已追蹤的部分合併）。",
           "<code>queryRange(left, right)</code>：若 [left, right) 中每個實數都正在被追蹤，回傳 True。",
           "<code>removeRange(left, right)</code>：停止追蹤 [left, right) 中的所有實數。"]),
 ],
 "idea": [
   ("c", """【端點陣列】
    把所有不相交的區間攤平：[l1, r1, l2, r2, ...]（排序）。
    對任意位置 x，bisect 得到的索引 i：
        i 是奇數 -> x 在某個區間裡面
        i 是偶數 -> x 在所有區間外面

【addRange(left, right)】
    i = bisect_left(left)、j = bisect_right(right)
    [i, j) 之間的端點都被新區間覆蓋，刪掉。
    若 i 是偶數（left 在區間外）-> left 成為新的左端點；
    若 j 是偶數（right 在區間外）-> right 成為新的右端點。
    bisect_left / right 的選擇讓相接的區間自動合併。

【removeRange】
    對稱：奇數時補端點（原本在區間內，切開後需要新邊界）。

【queryRange】
    left 和 right 落在同一個區間內：
    bisect_right(left) == bisect_left(right) 而且是奇數。

    每個操作 O(log n + 被刪除的端點數)，均攤 O(log n)（切片的搬移成本另計）。"""),
 ],
 "approaches": [
   ap("解法一", "有序區間列表", [("c", "維護排序的 [l, r) 列表\nadd：找出所有與 [left, right) 重疊或相接的區間，合併成一個\nremove：找出重疊的區間，切掉 [left, right) 的部分\nquery：二分找包含 left 的區間，檢查它的右端 >= right")], "O(n)", "O(n)"),
   ap("解法二", "端點陣列 + 奇偶判斷", [("c", S["p715"]), "驗證方式：在整數座標上和布林陣列模擬比對 400 組隨機操作序列。"], "O(log n + 移動量)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>相接的區間</strong>（[1,3) 與 [3,5)）→ 應該合併。", "<strong>刪除區間的中間一段</strong> → 一個區間變成兩個。", "<strong>查詢空集合</strong>（題目保證 left < right）。"],
 "follow": [("h", "線段樹做法"), ("c", "座標達 10⁹，可用動態開點線段樹：區間賦值（設為追蹤/不追蹤）＋區間「是否全部為真」查詢。")],
 "related": ["<strong>第 56 題 合併區間</strong>", "<strong>第 57 題 插入區間</strong>", "<strong>第 352 題 將資料流變為多個不相交區間</strong>"],
 "check": ["端點陣列中索引的奇偶代表什麼？", "addRange 為什麼用 bisect_left 找 left、bisect_right 找 right？"],
})


# ==================== 717. 1-bit and 2-bit Characters ====================
S["p717"] = '''class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:            # 從頭解碼到最後一位之前
            i += bits[i] + 1                # ★ 1 開頭是兩位元字元，0 是一位元字元
        return i == len(bits) - 1           # 剛好停在最後一位：它是單獨的一位元字元'''

_p717 = S.load("p717")
def _gen717():
    chars = [random.choice(["0", "10", "11"]) for _ in range(random.randint(0, 5))] + [random.choice(["0", "10", "11"])]
    return [int(c) for c in "".join(chars)], chars[-1] == "0"
for _ in range(3000):
    bits, _ = _gen717()
    if bits[-1] != 0: continue
    i = 0
    while i < len(bits) - 1: i += 2 if bits[i] else 1
    assert _p717.isOneBitCharacter(bits) == (i == len(bits) - 1)
assert _p717.isOneBitCharacter([1, 0, 0]) and not _p717.isOneBitCharacter([1, 1, 1, 0])
print("P717 OK")

em({
 "num": 717, "title": "1 位元與 2 位元字元",
 "desc": "從頭解碼：遇到 1 跳兩格、遇到 0 跳一格；看最後是否剛好停在最後一位。",
 "zh": [
   "有兩種特殊字元：一位元字元 <code>0</code>，以及兩位元字元 <code>10</code> 或 <code>11</code>。",
   "給你一個以 <code>0</code> 結尾的位元陣列 <code>bits</code>，判斷最後一個字元是否<strong>一定</strong>是一位元字元。",
 ],
 "idea": [
   ("c", """【編碼是唯一可解碼的】
    讀到 0 -> 一定是一位元字元
    讀到 1 -> 一定是兩位元字元的開頭（連同下一位）
    從頭讀就能唯一切開，這是一種前綴碼。

【做法】
    i 從 0 開始，i += bits[i] + 1，直到 i >= n - 1。
    i == n - 1：最後一個 0 是自己一個字元 -> True
    i == n    ：最後一個 0 被前面的 1 吃掉了 -> False

【更快：只看結尾的連續 1】
    倒數第二位往前數連續的 1 的個數：
    偶數 -> True，奇數 -> False。"""),
 ],
 "approaches": [
   ap("解法", "從頭解碼", [("c", S["p717"])], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>[0]</strong> → True。", "<strong>[1, 0]</strong> → False。"],
 "follow": [("h", "前綴碼"), ("c", "沒有任何碼字是另一個碼字的前綴，所以從頭讀就能唯一解碼——霍夫曼編碼、UTF-8 都是前綴碼。")],
 "related": ["<strong>第 393 題 UTF-8 編碼驗證</strong>", "<strong>第 91 題 解碼方法</strong>"],
 "check": ["為什麼從頭讀可以唯一切開？", "只看結尾連續 1 的個數為什麼可以？"],
})


# ==================== 718. Maximum Length of Repeated Subarray ====================
S["p718"] = '''class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)                  # dp[j]：以 nums1[i-1]、nums2[j-1] 結尾的最長公共子陣列
        res = 0
        for i in range(1, m + 1):
            for j in range(n, 0, -1):       # 由右往左：dp[j-1] 還是上一列的值
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1   # ★ 相同就延長斜對角的長度
                    res = max(res, dp[j])
                else:
                    dp[j] = 0               # 不同就斷掉（要求連續）
        return res'''

_p718 = S.load("p718")
for _ in range(2000):
    a = [random.randint(0, 2) for _ in range(random.randint(1, 8))]; b = [random.randint(0, 2) for _ in range(random.randint(1, 8))]
    want = max([L for L in range(1, min(len(a), len(b)) + 1) for i in range(len(a) - L + 1) for j in range(len(b) - L + 1) if a[i:i + L] == b[j:j + L]] + [0])
    assert _p718.findLength(a, b) == want
print("P718 OK")

em({
 "num": 718, "title": "最長重複子陣列",
 "desc": "最長公共「子陣列」（連續）：dp[i][j] 是以兩者各自結尾的公共長度，不同就歸零；和 LCS 的差別只在不相等時的處理。",
 "zh": ["給你兩個整數陣列 <code>nums1</code>、<code>nums2</code>，回傳兩者<strong>公共的、長度最長的連續子陣列</strong>的長度。"],
 "idea": [
   ("c", """【以結尾定義狀態】
    dp[i][j] = 以 nums1[i-1] 和 nums2[j-1] 結尾的最長公共子陣列長度。
        相等   -> dp[i-1][j-1] + 1
        不相等 -> 0（連續性斷掉）
    答案是所有 dp 的最大值。

【和 LCS（子序列）對照】
    LCS 不相等時取 max(dp[i-1][j], dp[i][j-1])；
    子陣列要求連續，不相等就歸零。

【空間壓縮】
    只依賴左上角 -> 一維陣列，j 由右往左更新。

【更快的做法】
    二分長度 + 滾動雜湊：O((m+n) log min(m,n))。"""),
 ],
 "approaches": [
   ap("解法", "DP（一維壓縮）", [("c", S["p718"]), "驗證方式：和枚舉所有子陣列的暴力法比對 2000 組。"], "O(mn)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>沒有共同元素</strong> → 0。", "<strong>一維壓縮時 j 的方向</strong> → 必須由右往左，否則 dp[j−1] 已被覆蓋。"],
 "follow": [("h", "滑動對齊"), ("c", "另一個 O(mn) 時間、O(1) 空間的做法：把兩個陣列錯開各種位移對齊，數每種對齊下最長的連續相等段。")],
 "related": ["<strong>第 1143 題 最長共同子序列</strong>", "<strong>第 1044 題 最長重複子字串</strong>"],
 "check": ["不相等時為什麼 dp 歸零？", "壓縮成一維時 j 為什麼要由右往左？"],
})


# ==================== 719. Find K-th Smallest Pair Distance ====================
S["p719"] = '''class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)

        def count(d):                       # 距離 <= d 的數對有幾個（雙指標）
            c = l = 0
            for r in range(n):
                while nums[r] - nums[l] > d:
                    l += 1
                c += r - l                  # 以 r 為右端、左端在 [l, r) 的數對
            return c

        lo, hi = 0, nums[-1] - nums[0]
        while lo < hi:                      # ★ 二分答案：最小的 d 使得「距離 <= d 的數對」>= k
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo'''

_p719 = S.load("p719")
from itertools import combinations
for _ in range(1500):
    a = [random.randint(0, 20) for _ in range(random.randint(2, 9))]
    ds = sorted(abs(x - y) for x, y in combinations(a, 2)); k = random.randint(1, len(ds))
    assert _p719.smallestDistancePair(a[:], k) == ds[k - 1]
print("P719 OK")

em({
 "num": 719, "title": "找出第 K 小的數對距離",
 "desc": "對答案二分：排序後用雙指標在 O(n) 內數出「距離 ≤ d 的數對」個數，找最小的 d 使個數 ≥ k。",
 "zh": ["兩個數 a、b 的<strong>距離</strong>是 <code>|a − b|</code>。給你整數陣列 <code>nums</code> 和整數 <code>k</code>，回傳所有數對 <code>(nums[i], nums[j])</code>（i &lt; j）的距離中<strong>第 k 小</strong>的。"],
 "idea": [
   ("c", """【數對太多】
    n = 10⁴ -> 約 5×10⁷ 個數對，全部列出來排序太慢。

【二分答案】
    f(d) = 距離 <= d 的數對個數，隨 d 單調不減。
    第 k 小的距離 = 最小的 d 使 f(d) >= k。
    d 的範圍 [0, max - min]。

【f(d)：排序 + 雙指標】
    對每個右端 r，找最小的 l 使 nums[r] - nums[l] <= d，
    那麼 (l, r), (l+1, r), ..., (r-1, r) 都符合 -> r - l 個。
    r 往右時 l 只會往右 -> O(n)。

    總時間 O(n log n + n log W)。"""),
 ],
 "approaches": [
   ap("解法", "排序 + 二分答案 + 雙指標計數", [("c", S["p719"]), "驗證方式：和列出所有距離排序比對 1500 組。"], "O(n log n + n log W)", "O(1)", "W 為最大值與最小值的差", "", optimal=True),
 ],
 "edges": ["<strong>重複值</strong> → 距離 0。", "<strong>k = 1</strong> → 排序後相鄰差的最小值。"],
 "follow": [("h", "二分答案的條件"), ("c", "答案有單調性（d 越大，符合的越多），而且「給定 d 時的計數」容易算。和第 668 題（乘法表中第 k 小）、第 378 題同一類。")],
 "related": ["<strong>第 668 題 乘法表中第 k 小的數</strong>", "<strong>第 378 題 有序矩陣中第 K 小的元素</strong>", "<strong>第 786 題 第 K 個最小的質數分數</strong>"],
 "check": ["為什麼可以對距離二分？", "雙指標計數時，每個 r 貢獻幾個數對？"],
})


# ==================== 720. Longest Word in Dictionary ====================
S["p720"] = '''class Solution:
    def longestWord(self, words: List[str]) -> str:
        ok = {""}                           # 可以「一次加一個字母」逐步建出來的單字
        best = ""
        for w in sorted(words):             # 依字典序排序：前綴一定排在它前面
            if w[:-1] in ok:                # ★ 去掉最後一個字母後也能建出來
                ok.add(w)
                if len(w) > len(best):      # 同長度時，先出現的字典序較小，不更新
                    best = w
        return best'''

_p720 = S.load("p720")
assert _p720.longestWord(["w", "wo", "wor", "worl", "world"]) == "world"
assert _p720.longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"]) == "apple"
for _ in range(2000):
    ws = list({"".join(random.choice("ab") for _ in range(random.randint(1, 4))) for _ in range(random.randint(1, 8))})
    s = set(ws)
    good = [w for w in ws if all(w[:i] in s for i in range(1, len(w) + 1))]
    want = min(good, key=lambda w: (-len(w), w)) if good else ""
    assert _p720.longestWord(ws) == want
print("P720 OK")

em({
 "num": 720, "title": "字典中最長的單字",
 "desc": "排序後依序處理：一個單字能被建出 ⇔ 去掉最後一個字母後的單字已能被建出；也可用字典樹。",
 "zh": [
   "給你一個字串陣列 <code>words</code>，找出最長的單字，使得它能由陣列中的其他單字<strong>每次加一個字母</strong>逐步建出（它的每個前綴都在陣列中）。",
   "若有多個，回傳字典序最小的；沒有則回傳空字串。",
 ],
 "idea": [
   ("c", """【能被建出的條件】
    w 的每個前綴都在 words 中 <=> w[:-1] 能被建出，而且 w 在 words 中。
    （歸納：一路往回推到單一字母。）

【排序後依序處理】
    字典序排序保證 w[:-1] 在 w 之前出現，
    所以處理 w 時已經知道 w[:-1] 能不能建出。

【平手】
    同長度時字典序小的先被處理，只有「更長」才更新答案。

【字典樹】
    把所有單字插入字典樹，從根做 DFS，
    只走「節點本身是某個單字結尾」的路徑，最深的就是答案。"""),
 ],
 "approaches": [
   ap("解法", "排序 + 雜湊集合", [("c", S["p720"]), "驗證方式：和「檢查每個單字的所有前綴是否都在集合中」的暴力法比對 2000 組。"], "O(Σ L log n)", "O(Σ L)", "排序比較字串的成本", "", optimal=True),
 ],
 "edges": ["<strong>沒有單一字母的單字</strong> → \"\"。", "<strong>同長度</strong> → 字典序小的。"],
 "follow": [("h", "相關"), ("c", "第 1858 題（付費）幾乎相同；第 524 題是「刪除字母得到字典單字」，方向相反。")],
 "related": ["<strong>第 208 題 實作字典樹</strong>", "<strong>第 648 題 單字替換</strong>", "<strong>第 524 題 通過刪除字母匹配到字典裡最長單字</strong>"],
 "check": ["為什麼只要檢查 w[:−1] 能否被建出？", "排序在這裡解決了什麼問題？"],
})


# ==================== 721. Accounts Merge ====================
S["p721"] = '''class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        def find(x):
            parent.setdefault(x, x)
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        owner = {}
        for acc in accounts:
            name, first = acc[0], acc[1]
            for e in acc[1:]:
                owner[e] = name
                parent[find(e)] = find(first)       # ★ 同一個帳戶裡的 email 都屬於同一個人

        groups = defaultdict(list)
        for e in owner:
            groups[find(e)].append(e)
        return [[owner[r]] + sorted(es) for r, es in groups.items()]'''

_p721 = S.load("p721")
r = _p721.accountsMerge([["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
assert sorted(r) == sorted([["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]])
for _ in range(1000):
    accs = []
    for _ in range(random.randint(1, 6)):
        nm = random.choice("AB")
        es = random.sample([nm + str(i) for i in range(6)], random.randint(1, 3))
        accs.append([nm] + es)
    # 參考：反覆合併有共同 email 的群組
    groups = [set(a[1:]) for a in accs]; names = [a[0] for a in accs]
    changed = True
    while changed:
        changed = False
        for i in range(len(groups)):
            for j in range(i + 1, len(groups)):
                if groups[i] & groups[j]:
                    groups[i] |= groups.pop(j); names.pop(j); changed = True; break
            if changed: break
    want = sorted([n] + sorted(g) for n, g in zip(names, groups))
    assert sorted(_p721.accountsMerge(accs)) == want
print("P721 OK")

em({
 "num": 721, "title": "帳戶合併",
 "desc": "以 email 為節點，同一帳戶內的 email 互相連通；用聯合查找求連通分量，每個分量就是一個人。",
 "zh": [
   "給你一組帳戶 <code>accounts</code>，<code>accounts[i][0]</code> 是名字，其餘是這個帳戶的 email。",
   "兩個帳戶只要有<strong>任何一個共同的 email</strong>，就一定屬於同一個人（同名不代表同一個人）。合併後回傳每個人的帳戶：名字在前，後面是<strong>排序好</strong>的所有 email。帳戶順序不限。",
 ],
 "idea": [
   ("c", """【圖的連通分量】
    節點：每個 email。
    邊：同一個帳戶內的 email 互相相連
        （只要把每個 email 連到該帳戶的第一個 email 即可）。
    同一個連通分量的 email 屬於同一個人。

【聯合查找】
    每個帳戶：把所有 email 和第一個 email 合併。
    最後依代表元素分組、排序，加上名字。

【名字從哪來？】
    同一個連通分量的帳戶名字一定相同（同一個人），
    記下任一個 email 對應的名字即可。"""),
 ],
 "approaches": [
   ap("解法", "聯合查找", [("c", S["p721"]), "驗證方式：和「反覆合併有交集的 email 集合」的暴力法比對 1000 組。"], "O(N log N)", "O(N)", "N 為 email 總數；排序是主要成本", "", optimal=True),
 ],
 "edges": ["<strong>同名但沒有共同 email</strong> → 不合併。", "<strong>間接相連</strong>（A–B 共用、B–C 共用）→ 三個帳戶都合併。", "<strong>帳戶內重複的 email</strong> → 分組時用 owner 的鍵去重。"],
 "follow": [("h", "DFS 做法"), ("c", "建好 email 的鄰接表後，對每個沒拜訪過的 email 做 DFS 收集整個分量，效果相同。")],
 "related": ["<strong>第 547 題 省份數量</strong>", "<strong>第 684 題 冗餘連接</strong>", "<strong>第 737 題 句子相似性 II</strong>（付費）"],
 "check": ["圖的節點和邊分別是什麼？", "為什麼只要把每個 email 和帳戶的第一個 email 合併？"],
})
