# -*- coding: utf-8 -*-
"""第 474–479 題。"""
import random
import itertools
import math
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(474)


# ==================== 474. Ones and Zeroes ====================
S["p474"] = '''class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # dp[i][j]：最多用 i 個 0、j 個 1 時，最多能選幾個字串
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            zeros, ones = s.count("0"), s.count("1")
            # ★ 二維容量的 0/1 背包：兩個容量都要由大到小
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)
        return dp[m][n]'''

_p474 = S.load("p474")
for strs, m, n, want in [(["10", "0001", "111001", "1", "0"], 5, 3, 4), (["10", "0", "1"], 1, 1, 2)]:
    assert _p474.findMaxForm(strs, m, n) == want
for _ in range(600):
    strs = ["".join(random.choice("01") for _ in range(random.randint(1, 4))) for _ in range(random.randrange(1, 8))]
    m, n = random.randint(0, 6), random.randint(0, 6)
    want = max(r for r in range(len(strs) + 1) for c in itertools.combinations(strs, r)
               if sum(s.count("0") for s in c) <= m and sum(s.count("1") for s in c) <= n)
    assert _p474.findMaxForm(strs, m, n) == want
print("P474 OK")

emit({
 "num": 474, "slug": "ones-and-zeroes",
 "en": [
   "You are given an array of binary strings <code>strs</code> and two integers <code>m</code> and <code>n</code>.",
   "Return <em>the size of the largest subset of <code>strs</code> such that there are <strong>at most</strong></em> <code>m</code> <code>0</code><em>'s and</em> <code>n</code> <code>1</code><em>'s in the subset</em>.",
   "A set <code>x</code> is a <strong>subset</strong> of a set <code>y</code> if all elements of <code>x</code> are also elements of <code>y</code>.",
 ],
 "zh": [
   "給你一組二進位字串 <code>strs</code> 和兩個整數 <code>m</code>、<code>n</code>。",
   "找出最大的子集，使子集中所有字串合起來<strong>最多</strong>有 <code>m</code> 個 0 和 <code>n</code> 個 1，回傳子集的大小。",
 ],
 "examples": """範例 1
  輸入：strs = ["10","0001","111001","1","0"], m = 5, n = 3
  輸出：4
  說明：{"10", "0001", "1", "0"}：5 個 0、3 個 1。

範例 2
  輸入：strs = ["10","0","1"], m = 1, n = 1
  輸出：2""",
 "constraints": [
   "1 ≤ <code>strs.length</code> ≤ 600",
   "1 ≤ <code>strs[i].length</code> ≤ 100",
   "1 ≤ <code>m, n</code> ≤ 100",
 ],
 "idea": [
   ("c", """【0/1 背包，但有「兩個容量」】
    物品：每個字串，重量是 (0 的個數, 1 的個數)，價值 1
    背包：最多 m 個 0、n 個 1
    目標：價值最大

【dp[i][j] = 用最多 i 個 0、j 個 1 時，最多能選幾個字串】
    加入一個字串 (z, o)：
        dp[i][j] = max(dp[i][j], dp[i-z][j-o] + 1)

【兩個維度都要由大到小掃】
    和一維 0/1 背包一樣，避免同一個字串被用兩次。

【複雜度】
    O(字串數 × m × n) = 600 × 100 × 100 = 6×10⁶。"""),
 ],
 "approaches": [
   ap("解法", "二維容量的 0/1 背包", [
     ("c", S["p474"]),
   ], "O(L · m · n)", "O(m · n)", "L = 字串數", "", optimal=True),
 ],
 "edges": [
   "<strong>某個字串的 0 或 1 超過容量</strong> → 迴圈範圍自動略過。",
   "<strong>全部都能選</strong> → 答案是字串數。",
 ],
 "follow": [
   ("h", "多維背包"),
   ("c", "限制條件有幾個，dp 就有幾個容量維度。第 879 題（盈利計劃）也是二維：人數和利潤。"),
 ],
 "related": [
   "<strong>第 416 題 分割等和子集</strong> —— 一維 0/1 背包",
   "<strong>第 879 題 盈利計劃</strong>",
 ],
 "check": [
   "這題的「物品」、「重量」、「價值」分別是什麼？",
   "為什麼兩個維度都要由大到小掃？",
 ],
})


# ==================== 475. Heaters ====================
S["p475"] = '''class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        radius = 0
        for h in houses:
            i = bisect.bisect_left(heaters, h)          # 第一個 >= h 的暖爐
            right = heaters[i] - h if i < len(heaters) else float("inf")
            left = h - heaters[i - 1] if i > 0 else float("inf")
            # ★ 每間房子只需要最近的暖爐；半徑要照顧到「最遠的那間房子」
            radius = max(radius, min(left, right))
        return radius'''

_p475 = S.load("p475")
for houses, heaters, want in [([1, 2, 3], [2], 1), ([1, 2, 3, 4], [1, 4], 1), ([1, 5], [2], 3)]:
    assert _p475.findRadius(houses, heaters) == want
for _ in range(3000):
    houses = [random.randint(1, 30) for _ in range(random.randrange(1, 8))]
    heaters = [random.randint(1, 30) for _ in range(random.randrange(1, 5))]
    want = max(min(abs(h - t) for t in heaters) for h in houses)
    assert _p475.findRadius(houses, list(heaters)) == want
print("P475 OK")

emit({
 "num": 475, "slug": "heaters",
 "en": [
   "Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.",
   "Every house can be warmed, as long as the house is within the heater's warm radius range.",
   "Given the positions of <code>houses</code> and <code>heaters</code> on a horizontal line, return <em>the minimum radius standard of heaters so that those heaters could cover all houses.</em>",
   "<strong>Notice</strong> that all the <code>heaters</code> follow your radius standard, and the warm radius will be the same.",
 ],
 "zh": [
   "冬天來了！所有暖爐的供暖半徑都相同，房子只要在某個暖爐的半徑範圍內就能取暖。",
   "給你房子和暖爐在直線上的位置，回傳能讓所有房子都取暖的<strong>最小半徑</strong>。",
 ],
 "examples": """範例 1
  輸入：houses = [1,2,3], heaters = [2]
  輸出：1

範例 2
  輸入：houses = [1,2,3,4], heaters = [1,4]
  輸出：1

範例 3
  輸入：houses = [1,5], heaters = [2]
  輸出：3""",
 "constraints": [
   "1 ≤ <code>houses.length, heaters.length</code> ≤ 3 × 10⁴",
   "1 ≤ <code>houses[i], heaters[i]</code> ≤ 10⁹",
 ],
 "idea": [
   ("c", """【每間房子：需要的半徑 = 到最近暖爐的距離】
    所有房子都要照顧到 -> 答案 = 所有房子「到最近暖爐距離」的最大值。

【找最近的暖爐】
    暖爐排序後，二分找第一個 >= 房子位置的暖爐，
    最近的暖爐是它或它左邊那一個。

【另一種：雙指標】
    房子和暖爐都排序，指標一起往右走。O(n log n + m log m)。"""),
 ],
 "approaches": [
   ap("解法", "暖爐排序 + 二分找最近", [
     ("c", S["p475"]),
   ], "O((n + m) log m)", "O(1)", "", "不計排序", optimal=True),
 ],
 "edges": [
   "<strong>房子在所有暖爐左邊或右邊</strong> → 只有一側有暖爐。",
   "<strong>房子和暖爐同位置</strong> → 距離 0。",
 ],
 "follow": [
   ("h", "二分答案的做法"),
   ("c", "也可以對半徑二分，檢查給定半徑能否覆蓋所有房子——但直接算「每間房子到最近暖爐的距離」更簡單。"),
 ],
 "related": [
   "<strong>第 35 題 搜尋插入位置</strong>",
   "<strong>第 1631 題 最小體力消耗路徑</strong>",
 ],
 "check": [
   "答案為什麼是「到最近暖爐距離」的最大值？",
   "怎麼找到離一間房子最近的暖爐？",
 ],
})


# ==================== 476. Number Complement ====================
S["p476"] = '''class Solution:
    def findComplement(self, num: int) -> int:
        mask = (1 << num.bit_length()) - 1     # ★ 和 num 等長、全部是 1 的遮罩
        return num ^ mask                      # 只翻轉有效的位元'''

_p476 = S.load("p476")
for n in range(1, 50000):
    b = bin(n)[2:]
    assert _p476.findComplement(n) == int("".join("1" if c == "0" else "0" for c in b), 2)
print("P476 OK")

emit({
 "num": 476, "slug": "number-complement",
 "en": [
   "The <strong>complement</strong> of an integer is the integer you get when you flip all the <code>0</code>'s to <code>1</code>'s and all the <code>1</code>'s to <code>0</code>'s in its binary representation.",
   ("ul", ["For example, The integer <code>5</code> is <code>\"101\"</code> in binary and its <strong>complement</strong> is <code>\"010\"</code> which is the integer <code>2</code>."]),
   "Given an integer <code>num</code>, return <em>its complement</em>.",
 ],
 "zh": [
   "一個整數的<strong>補數</strong>：把它二進位表示中的 0 變 1、1 變 0（只翻轉<strong>有效位元</strong>，不含前導零）。",
   "例如 5 = <code>101</code>，補數是 <code>010</code> = 2。給你 <code>num</code>，回傳它的補數。",
 ],
 "examples": """範例 1
  輸入：num = 5
  輸出：2

範例 2
  輸入：num = 1
  輸出：0""",
 "constraints": [
   "1 ≤ <code>num</code> &lt; 2³¹",
 ],
 "idea": [
   ("c", """【XOR 1 就是翻轉】
    x ^ 1 = 翻轉 x 的那一位。

【只翻轉有效位元】
    ~num 會把前面無限多個 0 也翻成 1（在 Python 變成負數）✘
    用一個「和 num 等長、全是 1」的遮罩：
        num = 101，bit_length = 3
        mask = (1 << 3) - 1 = 111
        101 ^ 111 = 010 ✔"""),
 ],
 "approaches": [
   ap("解法", "等長遮罩 XOR", [
     ("c", S["p476"]),
   ], "O(1)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>num = 1</strong> → 0。",
   "<strong>num 全是 1</strong>（7 = 111）→ 0。",
   "<strong>不能直接用 ~</strong> → 會翻轉前導零。",
 ],
 "follow": [
   ("h", "同一題"),
   ("c", "第 1009 題「十進位整數的反碼」幾乎相同，只是 num 可以是 0（0 的補數定義成 1）。"),
 ],
 "related": [
   "<strong>第 1009 題 十進位整數的反碼</strong>",
   "<strong>第 190 題 顛倒二進位位</strong>",
 ],
 "check": [
   "為什麼不能直接用 ~num？",
   "遮罩怎麼算？",
 ],
})


# ==================== 477. Total Hamming Distance ====================
S["p477"] = '''class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for b in range(30):                          # 值 <= 10⁹ < 2³⁰
            ones = sum(x >> b & 1 for x in nums)     # 這一位是 1 的有幾個
            # ★ 這一位上，每一對「一個 1、一個 0」貢獻 1
            total += ones * (n - ones)
        return total'''

_p477 = S.load("p477")
for _ in range(1000):
    a = [random.randint(0, 10 ** 9) for _ in range(random.randrange(1, 10))]
    want = sum(bin(a[i] ^ a[j]).count("1") for i in range(len(a)) for j in range(i + 1, len(a)))
    assert _p477.totalHammingDistance(a) == want
print("P477 OK")

emit({
 "num": 477, "slug": "total-hamming-distance",
 "en": [
   "The <a href=\"https://en.wikipedia.org/wiki/Hamming_distance\">Hamming distance</a> between two integers is the number of positions at which the corresponding bits are different.",
   "Given an integer array <code>nums</code>, return <em>the sum of <strong>Hamming distances</strong> between all the pairs of the integers in</em> <code>nums</code>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，回傳所有數對之間的<strong>漢明距離總和</strong>（第 461 題）。",
 ],
 "examples": """範例 1
  輸入：nums = [4,14,2]
  輸出：6
  說明：4 = 0100、14 = 1110、2 = 0010
    HD(4,14) + HD(4,2) + HD(14,2) = 2 + 2 + 2 = 6

範例 2
  輸入：nums = [4,14,4]
  輸出：4""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁴",
   "0 ≤ <code>nums[i]</code> ≤ 10⁹",
 ],
 "idea": [
   ("c", """【兩兩計算：O(n²)，n = 10⁴ 時 5×10⁷ 對，偏慢】

【換個方向：一個位元一個位元看】
    固定第 b 位：
        k 個數這一位是 1，n - k 個是 0
        每一對「一個 1、一個 0」在這一位不同 -> 貢獻 1
        共 k × (n - k) 對
    把 30 個位元的貢獻加起來。

【複雜度】O(30 n)。"""),
 ],
 "approaches": [
   ap("解法", "逐位元計數", [
     ("c", S["p477"]),
   ], "O(30 · n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>只有一個數</strong> → 0。",
   "<strong>全部相同</strong> → 0。",
 ],
 "follow": [
   ("h", "「逐位貢獻」的技巧"),
   ("c", "和位元運算有關的「所有數對」問題，常常可以拆成每一位各自計算。例如所有數對 XOR 的總和、所有子陣列 AND 的總和。"),
 ],
 "related": [
   "<strong>第 461 題 漢明距離</strong>",
   "<strong>第 2425 題 所有數對的異或和</strong>",
 ],
 "check": [
   "固定一個位元，它對總和的貢獻是多少？",
   "為什麼這樣比兩兩計算快？",
 ],
})


# ==================== 478. Generate Random Point in a Circle ====================
S["p478"] = '''class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r, self.x, self.y = radius, x_center, y_center

    def randPoint(self) -> List[float]:
        while True:                                  # ★ 拒絕抽樣：在外接正方形取點
            dx = random.uniform(-self.r, self.r)
            dy = random.uniform(-self.r, self.r)
            if dx * dx + dy * dy <= self.r * self.r: # 落在圓內才接受（機率 π/4）
                return [self.x + dx, self.y + dy]'''

S["p478_polar"] = '''class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r, self.x, self.y = radius, x_center, y_center

    def randPoint(self) -> List[float]:
        theta = random.uniform(0, 2 * math.pi)
        # ★ 距離要取 sqrt：半徑 r 以內的面積和 r² 成正比
        d = self.r * math.sqrt(random.random())
        return [self.x + d * math.cos(theta), self.y + d * math.sin(theta)]'''

S["p478_wrong"] = '''class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r, self.x, self.y = radius, x_center, y_center

    def randPoint(self) -> List[float]:
        theta = random.uniform(0, 2 * math.pi)
        d = self.r * random.random()                 # ✘ 沒有開根號：點會擠在圓心附近
        return [self.x + d * math.cos(theta), self.y + d * math.sin(theta)]'''


def _inner_frac(key, N=40000):
    cls = S.loadns(key)["Solution"]
    obj = cls(2.0, 1.0, -1.0)
    inner = 0
    for _ in range(N):
        px, py = obj.randPoint()
        d2 = (px - 1) ** 2 + (py + 1) ** 2
        assert d2 <= 4 + 1e-9
        inner += d2 <= 1.0                           # 半徑 1 的內圈，面積佔 1/4
    return inner / N


assert abs(_inner_frac("p478") - 0.25) < 0.015
assert abs(_inner_frac("p478_polar") - 0.25) < 0.015
assert _inner_frac("p478_wrong") > 0.45              # 錯誤版本：約一半的點落在內圈
print("P478 OK")

emit({
 "num": 478, "slug": "generate-random-point-in-a-circle",
 "en": [
   "Given the radius and the position of the center of a circle, implement the function <code>randPoint</code> which generates a uniform random point inside the circle.",
   "Implement the <code>Solution</code> class:",
   ("ul", ["<code>Solution(double radius, double x_center, double y_center)</code> initializes the object with the radius of the circle <code>radius</code> and the position of the center <code>(x_center, y_center)</code>.",
           "<code>randPoint()</code> returns a random point inside the circle. A point on the circumference of the circle is considered to be in the circle. The answer is returned as an array <code>[x, y]</code>."]),
 ],
 "zh": [
   "給你圓的半徑和圓心，實作 <code>randPoint()</code>：在圓內（含圓周）<strong>均勻</strong>地隨機產生一個點。",
 ],
 "examples": """範例
  Solution(1.0, 0.0, 0.0)
  randPoint() -> 例如 [-0.02493, -0.38077]
  randPoint() -> 例如 [0.82314, 0.38945]""",
 "constraints": [
   "0 &lt; <code>radius</code> ≤ 10⁸",
   "−10⁷ ≤ <code>x_center, y_center</code> ≤ 10⁷",
   "最多呼叫 3 × 10⁴ 次",
 ],
 "idea": [
   ("c", """【方法一：拒絕抽樣】
    在外接正方形 [-r, r] × [-r, r] 均勻取點，
    落在圓外就丟掉重來。
    接受的機率 = 圓面積 / 正方形面積 = π/4 ≈ 78.5%，
    期望取樣 4/π ≈ 1.27 次。

【方法二：極座標 —— 陷阱在距離】
    角度 θ 均勻取 [0, 2π) ✔
    距離 d 均勻取 [0, r] ✘
        外圈的周長比內圈大，但分到的點一樣多 -> 點擠在圓心附近。

    正確：半徑 d 以內的面積 ∝ d²，
    要讓面積均勻，d² 要均勻 -> d = r × √U（U 均勻在 [0,1)）。
    這叫「逆變換抽樣」。

【驗證均勻性】
    半徑 r/2 的內圈面積是 1/4 ->
    均勻的話約 25% 的點落在內圈；
    錯誤版本會有約 50% 落在內圈。"""),
 ],
 "approaches": [
   ap("錯誤示範", "距離直接均勻取", [
     ("c", S["p478_wrong"]),
     "四萬個點中約一半落在半徑 r/2 的內圈，而正確答案應該是四分之一。",
   ]),

   ap("解法一", "拒絕抽樣", [
     ("c", S["p478"]),
   ], "期望 O(1)", "O(1)", "期望取樣 4/π 次", "", optimal=True),

   ap("解法二", "極座標 + 開根號", [
     ("c", S["p478_polar"]),
   ], "O(1)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["距離直接均勻", "O(1)", "不均勻 ✘"],
    ["一、拒絕抽樣", "期望 O(1)", "最直觀 ✔"],
    ["二、極座標 + √", "O(1)", "要懂逆變換"]]),
 "edges": [
   "<strong>圓周上的點</strong> → 也算在圓內（≤）。",
   "<strong>圓心不在原點</strong> → 最後加上圓心座標。",
 ],
 "follow": [
   ("h", "逆變換抽樣"),
   ("c", "想要某個分布 F，就用 F⁻¹(U)。圓的半徑分布 F(d) = (d/r)²，F⁻¹(u) = r√u。同樣的方法可以產生指數分布（−ln U / λ）等。"),
 ],
 "related": [
   "<strong>第 470 題 用 Rand7() 實作 Rand10()</strong> —— 拒絕抽樣",
   "<strong>第 497 題 非重疊矩形中的隨機點</strong>",
   "<strong>第 519 題 隨機翻轉矩陣</strong>",
 ],
 "check": [
   "拒絕抽樣的接受機率是多少？",
   "極座標取點時，為什麼距離要開根號？",
   "怎麼驗證產生的點是均勻的？",
 ],
})


# ==================== 479. Largest Palindrome Product ====================
S["p479"] = '''class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        hi = 10 ** n - 1                   # 最大的 n 位數
        lo = 10 ** (n - 1)
        for left in range(hi, lo - 1, -1):
            # ★ 由大到小枚舉「回文的左半邊」，組出 2n 位的回文數
            p = int(str(left) + str(left)[::-1])
            # 找一個 n 位數的因數 f，使 p / f 也是 n 位數
            f = hi
            while f * f >= p:              # f 從大往小試，只需要試到 √p
                if p % f == 0:
                    return p % 1337
                f -= 1
        return -1'''

_p479 = S.load("p479")
_known = {1: 9, 2: 987, 3: 123, 4: 597, 5: 677, 6: 1218}
for n, want in _known.items():
    assert _p479.largestPalindrome(n) == want, n


def _lp_ref(n):
    best = 0
    lo, hi = 10 ** (n - 1), 10 ** n
    for a in range(lo, hi):
        for b in range(a, hi):
            p = a * b
            if p > best and str(p) == str(p)[::-1]:
                best = p
    return best % 1337


for n in (1, 2, 3):
    assert _lp_ref(n) == _known[n]
print("P479 OK")

emit({
 "num": 479, "slug": "largest-palindrome-product",
 "en": [
   "Given an integer n, return <em>the <strong>largest palindromic integer</strong> that can be represented as the product of two <code>n</code>-digits integers</em>. Since the answer can be very large, return it <strong>modulo</strong> <code>1337</code>.",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，找出能表示成<strong>兩個 n 位數乘積</strong>的最大回文數，回傳它 mod 1337 的結果。",
 ],
 "examples": """範例 1
  輸入：n = 2
  輸出：987
  說明：99 × 91 = 9009，9009 % 1337 = 987

範例 2
  輸入：n = 1
  輸出：9""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 8",
 ],
 "idea": [
   ("c", """【暴力枚舉兩個因數：O(10²ⁿ)，n = 8 不可能】

【改成由大到小枚舉「回文數」】
    兩個 n 位數的乘積最多 2n 位。
    2n 位的回文數由左半邊（n 位）唯一決定：
        左半 9889 -> 回文 98899889
    從最大的左半邊往下試，第一個「能拆成兩個 n 位數相乘」的就是答案。

【怎麼檢查能不能拆？】
    從最大的 n 位數 f = 10ⁿ - 1 往下試，
    p % f == 0 且 p / f 也是 n 位數就成立。
    只需要試到 f² >= p（f 再小，另一個因數就會超過 n 位）。

【為什麼很快？】
    答案通常很接近上界，只要試少數幾個左半邊就找到了。
    （n >= 2 時，答案都是 2n 位的回文數。）"""),
 ],
 "approaches": [
   ap("解法", "由大到小枚舉回文數 + 檢查因數", [
     ("c", S["p479"]),
     "驗證方式：n = 1、2、3 和暴力枚舉所有因數對比對；n = 4、5、6 和已知答案比對。",
   ], "實際上很快", "O(1)", "理論上界難以精確分析", "", optimal=True),
 ],
 "edges": [
   "<strong>n = 1</strong> → 9（= 9 × 1 或 3 × 3），是 1 位數的回文，特判。",
   "<strong>答案要 mod 1337</strong> → 最後才取模。",
 ],
 "follow": [
   ("h", "「枚舉答案」而不是「枚舉輸入」"),
   ("c", "當答案空間比輸入組合小很多、而且可以由大到小嘗試時，直接枚舉答案往往更快——第一個成立的就是最大值。第 906 題（超級回文數）也是枚舉回文的一半。"),
 ],
 "related": [
   "<strong>第 9 題 回文數</strong>",
   "<strong>第 906 題 超級回文數</strong>",
   "<strong>第 866 題 回文質數</strong>",
 ],
 "check": [
   "2n 位的回文數怎麼由左半邊產生？",
   "檢查因數時為什麼只需要試到 f² ≥ p？",
   "為什麼由大到小試，第一個找到的就是答案？",
 ],
})
