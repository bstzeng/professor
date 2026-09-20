# -*- coding: utf-8 -*-
"""第 69–72 題。"""
import random, math, collections
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(69)

# ==================== 69. Sqrt(x) ====================
S["p69_bin"] = '''class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        # 找「最大的 m 使得 m*m <= x」
        lo, hi = 1, x // 2       # x >= 2 時，答案不會超過 x//2
        while lo <= hi:
            mid = (lo + hi) // 2
            sq = mid * mid
            if sq == x:
                return mid
            if sq < x:
                lo = mid + 1     # mid 可行，但也許還能更大
            else:
                hi = mid - 1

        return hi                # 迴圈結束時 hi 就是「最大的可行值」'''

S["p69_lower"] = '''class Solution:
    def mySqrt(self, x: int) -> int:
        # partition_point 骨架：找「第一個 m 使得 m*m > x」，再減 1
        lo, hi = 0, x + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * mid > x:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1'''

S["p69_newton"] = '''class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        # 牛頓法：求 f(r) = r² - x = 0 的根
        # 迭代式 r' = r - f(r)/f'(r) = r - (r² - x)/(2r) = (r + x/r) / 2
        r = x
        while r * r > x:
            r = (r + x // r) // 2      # 整數版，會單調遞減收斂到 floor(sqrt(x))
        return r'''

_p69 = [S.load(k) for k in ("p69_bin", "p69_lower", "p69_newton")]
for x in [0, 1, 2, 3, 4, 8, 9, 15, 16, 17, 99, 100, 101, 2147395599, 2147483647]:
    e = math.isqrt(x)
    for sol in _p69:
        assert sol.mySqrt(x) == e, ("P69", x, sol, sol.mySqrt(x), e)
for _ in range(5000):
    x = random.choice([random.randint(0, 200), random.randint(0, 2**31 - 1)])
    e = math.isqrt(x)
    for sol in _p69:
        assert sol.mySqrt(x) == e, ("P69", x, sol, sol.mySqrt(x), e)
print("P69 solutions OK")

_P69_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">牛頓法：用切線逼近，每一次迭代「正確位數大約加倍」</text>
            <g>
              <line x1="60" y1="230" x2="600" y2="230" stroke="var(--text-muted)"/>
              <line x1="80" y1="40" x2="80" y2="244" stroke="var(--text-muted)"/>
              <path d="M80 230 Q200 226 300 180 Q420 110 540 46" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="556" y="52" fill="var(--accent)" font-size="12">f(r) = r² − x</text>
              <line x1="140" y1="230" x2="140" y2="222" stroke="var(--text-muted)"/>
              <text x="140" y="248" fill="var(--text-muted)" font-size="11" text-anchor="middle">√x</text>
            </g>
            <g>
              <circle cx="520" cy="58" r="4" fill="#ff8a65"/>
              <text x="520" y="42" fill="#ff8a65" font-size="11" text-anchor="middle">r₀ = x</text>
              <line x1="520" y1="58" x2="330" y2="230" stroke="#ff8a65" stroke-width="1.4" stroke-dasharray="5 4"/>
              <circle cx="330" cy="230" r="4" fill="#ff8a65"/>
              <text x="330" y="262" fill="#ff8a65" font-size="11" text-anchor="middle">r₁</text>

              <line x1="330" y1="230" x2="330" y2="168" stroke="var(--border)" stroke-dasharray="3 3"/>
              <circle cx="330" cy="168" r="4" fill="var(--gold)"/>
              <line x1="330" y1="168" x2="212" y2="230" stroke="var(--gold)" stroke-width="1.4" stroke-dasharray="5 4"/>
              <circle cx="212" cy="230" r="4" fill="var(--gold)"/>
              <text x="212" y="262" fill="var(--gold)" font-size="11" text-anchor="middle">r₂</text>

              <line x1="212" y1="230" x2="212" y2="216" stroke="var(--border)" stroke-dasharray="3 3"/>
              <circle cx="212" cy="216" r="4" fill="var(--accent)"/>
              <line x1="212" y1="216" x2="156" y2="230" stroke="var(--accent)" stroke-width="1.4" stroke-dasharray="5 4"/>
              <circle cx="156" cy="230" r="4" fill="var(--accent)"/>
              <text x="156" y="262" fill="var(--accent)" font-size="11" text-anchor="middle">r₃</text>
            </g>
            <text x="20" y="292" fill="var(--gold)" font-size="12">r&apos; = (r + x/r) / 2　每一步都是「目前猜測」和「x 除以猜測」的平均</text>
            <text x="20" y="316" fill="var(--text-muted)" font-size="12">x = 2147483647 時，牛頓法只要約 20 次迭代；二分搜尋要 31 次。</text>'''

emit({
 "num": 69, "slug": "sqrtx",
 "en": [
   "Given a non-negative integer <code>x</code>, return <em>the square root of "
   "<code>x</code> rounded down to the nearest integer</em>. The returned integer should be "
   "<strong>non-negative</strong> as well.",
   "You <strong>must not use</strong> any built-in exponent function or operator.",
 ],
 "zh": [
   "給你一個非負整數 <code>x</code>，回傳它的<strong>算術平方根，向下取整</strong>。",
   "<strong>不能使用</strong>任何內建的次方函式或運算子"
   "（例如 <code>pow(x, 0.5)</code> 或 <code>x ** 0.5</code>）。",
 ],
 "pre": [
   ("note", "這題就是「找邊界」型的二分搜尋", [
     ("c", """要找的是：「最大的整數 m，使得 m² <= x」

    x = 8  ->  2² = 4 <= 8，3² = 9 > 8  ->  答案 2
    x = 16 ->  4² = 16 <= 16            ->  答案 4

關鍵性質：述詞 P(m) = (m² <= x) 是【單調】的

    m:      0  1  2  3  4  5 ...
    m² <= 8: ✔  ✔  ✔  ✘  ✘  ✘

    一旦變成 ✘ 就永遠是 ✘ —— 這正是二分搜尋的前提。

所以這題和第 35 題（Search Insert Position）是同一個骨架，
只是述詞從「nums[i] >= target」換成「m² > x」。

「二分答案」的通用模式：
    1. 答案的範圍是什麼？        [0, x]
    2. 述詞是什麼？              m² <= x
    3. 它單調嗎？                ✔
    4. 套 partition_point 骨架"""),
     "<strong>為什麼不能用 <code>x ** 0.5</code>？</strong>"
     "除了題目禁止之外，浮點數在大數時會有精度問題 —— "
     "<code>int(2147395600 ** 0.5)</code> 在某些平台上會得到 46339 而不是 46340。"
     "<strong>整數平方根必須用整數運算算，才能保證精確。</strong>",
   ]),
 ],
 "examples": """範例 1
  輸入：x = 4
  輸出：2

範例 2
  輸入：x = 8
  輸出：2
  說明：8 的平方根是 2.828...，向下取整是 2。""",
 "constraints": [
   "0 ≤ <code>x</code> ≤ 2³¹ − 1",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>x 可以到 2³¹ − 1 = 2147483647</strong>，答案最大是 46340"
       "（因為 46340² = 2147395600 ≤ x，而 46341² = 2147488281 > x）。",
       "<strong>在 C/Java 裡 <code>mid * mid</code> 會溢位！</strong>"
       "<code>mid</code> 可能到 10⁹，平方是 10¹⁸ —— 超過 <code>int</code>。"
       "標準做法是改成 <code>mid &gt; x / mid</code>（除法比較，不會溢位）"
       "或用 <code>long</code>。"
       "<strong>Python 沒這個問題，但面試時一定要提。</strong>",
       "<strong>x 可以是 0 或 1</strong> → 答案就是它自己。"
       "<strong>牛頓法要特判這兩個</strong>（<code>x // r</code> 在 <code>r = 0</code> 時會除以零）。",
     ]),
   ]),
 ],
 "idea": [
   ("t", ["解法", "想法", "迭代次數（x ≈ 2³¹）"],
     [["一、二分搜尋", "在 [0, x] 上找邊界", "約 31 次"],
      ["二、partition_point", "同上，換一個骨架", "約 31 次"],
      ["三、牛頓法", "用切線逼近，二次收斂", "約 20 次"]]),
 ],
 "approaches": [
   ap("解法一", "二分搜尋（經典骨架）", [
     ("c", S["p69_bin"]),
     ("h", "為什麼結束時回傳 <code>hi</code>？"),
     ("c", """迴圈用的是「while lo <= hi」的經典骨架。
結束時 lo == hi + 1，而且：

    所有 <= hi 的 m 都滿足 m² <= x
    所有 >= lo 的 m 都滿足 m² > x

所以 hi 就是「最大的可行值」= 答案 ✔

追一遍 x = 8：
    lo=1, hi=4
    mid=2: 4 < 8  -> lo=3
    lo=3, hi=4
    mid=3: 9 > 8  -> hi=2
    lo=3 > hi=2   -> 結束
    return hi = 2 ✔"""),
     ("h", "為什麼上界可以取 <code>x // 2</code>？"),
     ("c", """對 x >= 4，sqrt(x) <= x/2：
    等價於 4x <= x²，也就是 x >= 4 ✔

x = 2, 3 時 x//2 = 1，而答案也是 1 ✔
x = 0, 1 已經被提前 return 擋掉。

所以 hi = x // 2 對所有 x >= 2 都是安全的上界。

這只是常數優化（少一兩次迭代），
寫 hi = x 也完全正確。"""),
     ("h", "C/Java 的溢位陷阱"),
     ("c", """if (mid * mid <= x)      // ✘ mid 到 10⁹ 時 mid*mid 會溢位

三種修法：
  1. 用 long：  if ((long)mid * mid <= x)
  2. 改成除法： if (mid <= x / mid)
  3. 縮小上界： hi = 46340（sqrt(INT_MAX) 的上界）

第 2 種最優雅，而且不依賴更大的型別。
    mid <= x / mid   <=>   mid² <= x（整數除法會捨去，但不影響比較的方向）

    嚴格說：x / mid 是 floor(x/mid)，
    而 mid <= floor(x/mid)  <=>  mid * mid <= x
    （因為 mid 是整數）✔""",),
   ], "O(log x)", "O(1)", "約 31 次迭代", "幾個變數"),

   ap("解法二", "partition_point 骨架（更統一）", [
     ("c", S["p69_lower"]),
     "用第 35 題的 <code>lower_bound</code> 骨架："
     "<strong>找「第一個讓 <code>m² &gt; x</code> 成立的 m」，然後減 1。</strong>",
     ("c", """述詞 P(m) = (m² > x)

    m:      0  1  2  3  4
    P(m):   ✘  ✘  ✘  ✔  ✔    （x = 8）

    第一個 ✔ 是 m = 3
    答案 = 3 - 1 = 2 ✔

上界設 x + 1：
    因為答案最大是 x（當 x = 0 或 1 時），
    所以「第一個 P 成立的位置」最大是 x + 1。

    x = 1: lo 會收斂到 2，答案 2 - 1 = 1 ✔
    x = 0: lo 會收斂到 1，答案 1 - 1 = 0 ✔

這個版本不用任何特判（x = 0 和 1 自動處理），
而且和第 34、35、278、875 題共用同一個骨架。

我個人偏好這個版本 ——
「只記一種二分骨架」比「記三種」不容易出錯。"""),
   ], "O(log x)", "O(1)", "同上", "幾個變數", optimal=True),

   ap("解法三", "牛頓法（收斂最快）", [
     "把「求 √x」變成「求方程式 <code>f(r) = r² − x = 0</code> 的根」，"
     "然後用<strong>牛頓-拉弗森法（Newton-Raphson）</strong>迭代。",
     ("c", S["p69_newton"]),
     ("fig", _P69_FIG, "0 0 640 330"),
     ("h", "迭代式的推導"),
     ("c", """牛頓法的通式：從點 (r, f(r)) 畫切線，切線和 x 軸的交點就是下一個 r。

    r' = r - f(r) / f'(r)

    f(r)  = r² - x
    f'(r) = 2r

    r' = r - (r² - x) / (2r)
       = r - r/2 + x/(2r)
       = (r + x/r) / 2

最後這個形式有一個很直覺的解讀：
    「目前的猜測 r」和「x 除以猜測 x/r」的【平均】

    如果 r 太大，x/r 就會太小；反之亦然。
    取平均就會往中間靠 —— 而正確答案 √x 剛好滿足 r == x/r。

這個公式在古代就被發現了，叫做【巴比倫方法】或【希羅方法】——
比牛頓早了三千多年。"""),
     ("h", "為什麼整數版的 <code>while r * r &gt; x</code> 會停在正確答案？"),
     ("c", """整數版： r = (r + x // r) // 2

關鍵性質：
  1. 從 r = x 開始，序列是【單調遞減】的（在 r > sqrt(x) 的範圍內）
  2. 而且永遠 >= floor(sqrt(x))（不會衝過頭太多）
  3. 所以當 r*r <= x 第一次成立時，r 就是 floor(sqrt(x))

     直覺：r > sqrt(x) 時，AM-GM 不等式保證
           (r + x/r)/2 >= sqrt(x)
           所以新的 r 不會掉到 sqrt(x) 以下。
           而整數除法的捨去，剛好讓它停在 floor(sqrt(x))。

x = 8 的迭代：
    r = 8:  8*8 = 64 > 8  -> r = (8 + 8//8)//2 = (8+1)//2 = 4
    r = 4:  16 > 8        -> r = (4 + 8//4)//2 = (4+2)//2 = 3
    r = 3:  9 > 8         -> r = (3 + 8//3)//2 = (3+2)//2 = 2
    r = 2:  4 <= 8        -> 停，回傳 2 ✔

x = 0 會在 x // r 那裡除以零 —— 所以要提前 return。"""),
     ("h", "為什麼牛頓法比二分快？"),
     "<strong>二分是「線性收斂」</strong>：每次把誤差減半，正確的<strong>位元數</strong>每次加 1。",
     "<strong>牛頓法是「二次收斂」</strong>：每次把誤差平方，"
     "正確的<strong>位元數大約加倍</strong>。",
     ("c", """x ≈ 2³¹ 時：
    二分：  約 31 次迭代（每次砍一半）
    牛頓：  約 5-6 次就收斂到很接近，
            但整數版從 r = x 開始，前幾步是「除以 2」，
            所以實際約 20 次。

    如果初始猜測選得好（例如用位元長度估一個接近的起點），
    牛頓法可以壓到 5-6 次。

實務上：
    現代 CPU 有 sqrt 指令（硬體實作，幾個週期）。
    而軟體實作（例如嵌入式系統、大數函式庫）
    幾乎都用牛頓法 —— 因為二次收斂太划算了。

    著名的「快速反平方根」（Quake III 的 0x5f3759df）
    也是牛頓法，只是用一個位元技巧產生了極好的初始猜測。""",),
   ], "O(log log x) 迭代", "O(1)", "二次收斂", "一個變數"),
 ],
 "compare": (["解法", "迭代次數", "空間", "會溢位？", "備註"],
   [["一、二分（經典骨架）", "約 31", "O(1)", "C/Java 會", "最常見"],
    ["二、partition_point", "約 31", "O(1)", "同上", "骨架統一，不用特判"],
    ["三、牛頓法", "約 20", "O(1)", "同上", "二次收斂，實務用它"]]),
 "edges": [
   "<strong>x = 0</strong> → 0；<strong>x = 1</strong> → 1。"
   "<strong>牛頓法必須特判（<code>x // r</code> 會除以零）。</strong>",
   "<strong>完全平方數</strong>：<code>4 → 2</code>、<code>16 → 4</code>、<code>100 → 10</code>。",
   "<strong>剛好差一</strong>：<code>15 → 3</code>、<code>17 → 4</code>。驗證邊界沒有差一。",
   "<strong>最大值</strong>：<code>2147483647 → 46340</code>。",
   "<strong>臨界點</strong>：<code>2147395599 → 46339</code>（因為 46340² = 2147395600 &gt; 它）。"
   "<strong>這是 LeetCode 專門用來抓浮點精度錯誤的測資</strong> —— "
   "<code>int(2147395599 ** 0.5)</code> 在某些平台會得到 46340（錯）。",
   "<strong>C/Java 的 <code>mid * mid</code></strong>：<code>mid</code> 到 10⁹ 時會溢位。",
 ],
 "follow": [
   ("h", "追問一：如果要精確到小數點後 k 位呢？"),
   "兩種做法：",
   ("ul", [
     "<strong>放大再開根號</strong>：算 <code>isqrt(x × 10^(2k))</code>，"
     "然後在結果的小數點後 k 位插入小數點。這樣完全用整數運算，沒有浮點誤差。",
     "<strong>浮點二分</strong>：在 <code>[0, x]</code> 上二分，直到 "
     "<code>hi - lo &lt; 10^(-k)</code>。簡單但有浮點誤差累積。",
   ]),
   "<strong>第一種在金融和密碼學裡是標準做法</strong> —— 整數運算才能保證可重現。",
   ("h", "追問二：Python 有內建的整數平方根嗎？"),
   "<strong>有：<code>math.isqrt(x)</code>（Python 3.8+）。</strong>"
   "它保證回傳 <code>floor(sqrt(x))</code>，而且對任意大的整數都精確。"
   "內部用的是一個基於牛頓法的「自適應精度」演算法。"
   "<strong>本篇的測試就是拿它當基準。</strong>",
   ("h", "追問三：「快速反平方根」是什麼？"),
   ("c", """Quake III Arena 的著名程式碼（1999 年公開）：

    float Q_rsqrt(float number) {
        long i = *(long*)&number;
        i = 0x5f3759df - (i >> 1);      // 什麼鬼？
        float y = *(float*)&i;
        y = y * (1.5f - 0.5f * number * y * y);   // 一次牛頓迭代
        return y;
    }

它在算 1/sqrt(x)（3D 圖學裡用來正規化向量）。

那一行魔術數字在做什麼？
    IEEE 754 浮點數的位元表示，本身就「近似」是 log₂(x) 的線性函數。
    所以對位元做「減半再取負」，近似就是對數值做「開根號再取倒數」。
    0x5f3759df 是那個近似的最佳偏移常數。

這給出約 1 位有效數字的初始猜測，
然後一次牛頓迭代就把它提升到約 6 位 ——
夠 3D 遊戲用了，而且比呼叫 sqrt() 快好幾倍。

現代 CPU 有 rsqrtss 指令，所以這個技巧已經過時，
但它是「理解浮點數位元表示」的經典教材。""",),
   ("h", "追問四：為什麼「二分答案」是一個這麼通用的模式？"),
   "因為很多最佳化問題都可以改寫成「找最大／最小的可行值」，"
   "而「可行性」往往是單調的。",
   ("c", """本題：      P(m) = (m² <= x)                     找最大可行
第 278 題： P(v) = isBadVersion(v)                找最小成立
第 875 題： P(speed) = 能在 h 小時內吃完           找最小可行
第 1011 題：P(cap) = 能在 d 天內運完               找最小可行
第 410 題： P(x) = 能分成 k 段且每段和 <= x        找最小可行
第 4 題：   二分「切割點」而不是值

判斷能不能用：
    1. 答案在一個有界的範圍裡
    2. 有一個「檢查可行性」的函式 check(m)
    3. check 是單調的（一旦可行就一直可行，或反之）

三個條件都滿足 -> 套 partition_point 骨架，
複雜度 O(log(值域) × check 的複雜度)。""",),
 ],
 "related": [
   "<strong>第 35 題 Search Insert Position</strong> —— 同一個二分骨架",
   "<strong>第 367 題 Valid Perfect Square</strong> —— 判斷是不是完全平方數",
   "<strong>第 50 題 Pow(x, n)</strong> —— 另一個數值計算題",
   "<strong>第 875／1011／410 題</strong> —— 二分答案家族",
 ],
 "check": [
   "在 Java 裡 <code>mid * mid &lt;= x</code> 有什麼問題？三種修法各是什麼？",
   "為什麼 <code>x = 2147395599</code> 是一個重要的測資？",
   "牛頓法的迭代式 <code>(r + x/r) / 2</code> 有什麼直覺上的解讀？",
   "「二分答案」需要滿足哪三個條件？",
 ],
})
print("P69 written")

# ==================== 70. Climbing Stairs ====================
S["p70_iter"] = '''class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = 爬到第 i 階有幾種方法 = dp[i-1] + dp[i-2]（費氏數列）
        a, b = 1, 1        # a = dp[0] = 1（站著不動也算一種），b = dp[1] = 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b'''

S["p70_memo"] = '''from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def f(k: int) -> int:
            if k <= 2:
                return k        # f(1) = 1, f(2) = 2
            return f(k - 1) + f(k - 2)
        return f(n)'''

S["p70_matrix"] = '''class Solution:
    def climbStairs(self, n: int) -> int:
        # 矩陣快速冪：[[1,1],[1,0]]^n 的左上角就是 F(n+1)
        def mul(A, B):
            return [[A[0][0]*B[0][0] + A[0][1]*B[1][0],
                     A[0][0]*B[0][1] + A[0][1]*B[1][1]],
                    [A[1][0]*B[0][0] + A[1][1]*B[1][0],
                     A[1][0]*B[0][1] + A[1][1]*B[1][1]]]

        result = [[1, 0], [0, 1]]        # 單位矩陣
        base = [[1, 1], [1, 0]]
        e = n
        while e:
            if e & 1:
                result = mul(result, base)
            base = mul(base, base)
            e >>= 1

        return result[0][0]'''

_p70 = [S.load(k) for k in ("p70_iter", "p70_memo", "p70_matrix")]


def _fib_ref(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


for n in range(1, 60):
    e = _fib_ref(n)
    for sol in _p70:
        assert sol.climbStairs(n) == e, ("P70", n, sol, sol.climbStairs(n), e)
assert _p70[0].climbStairs(2) == 2
assert _p70[0].climbStairs(3) == 3
assert _p70[0].climbStairs(45) == 1836311903
print("P70 solutions OK")

emit({
 "num": 70, "slug": "climbing-stairs",
 "en": [
   "You are climbing a staircase. It takes <code>n</code> steps to reach the top.",
   "Each time you can either climb <code>1</code> or <code>2</code> steps. In how many "
   "distinct ways can you climb to the top?",
 ],
 "zh": [
   "你正在爬樓梯，需要爬 <code>n</code> 階才能到頂。",
   "每次你可以爬 <strong>1 階</strong>或 <strong>2 階</strong>。"
   "請問有幾種不同的方法可以爬到頂？",
 ],
 "pre": [
   ("note", "一句話推導出遞迴式", [
     ("c", """要到第 n 階，最後一步只有兩種可能：
    從第 n-1 階跨 1 步上來
    從第 n-2 階跨 2 步上來

而這兩種情況不會重疊（最後一步的大小不同），
也涵蓋了所有可能。

所以：  f(n) = f(n-1) + f(n-2)

邊界：
    f(1) = 1     只有「1」
    f(2) = 2     「1+1」或「2」

    n:     1  2  3  4  5  6   7   8
    f(n):  1  2  3  5  8  13  21  34

這正是【費氏數列】（只是起點偏移了一位）：
    Fib: 1, 1, 2, 3, 5, 8, 13, 21, ...
    f:      1, 2, 3, 5, 8, 13, 21, 34

    f(n) = Fib(n+1)

「最後一步從哪來」是所有計數型 DP 的標準切入點 ——
它把問題分解成互斥且窮盡的幾種情況。"""),
     "<strong>這題是動態規劃的「Hello World」。</strong>"
     "值得花時間把它的每一種寫法都弄懂 —— "
     "因為第 62、63、64、91、198、746 題都是同一個骨架的變形。",
   ]),
 ],
 "examples": """範例 1
  輸入：n = 2
  輸出：2
  說明：1 + 1，或 2

範例 2
  輸入：n = 3
  輸出：3
  說明：1 + 1 + 1，1 + 2，2 + 1""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 45",
 ],
 "mid": [
   ("note", "為什麼上限是 45？", [
     ("c", """f(45) = 1836311903

而 INT_MAX = 2147483647

f(46) = 2971215073 > INT_MAX  ->  在 Java/C 裡會溢位

所以題目把 n 限制在 45，讓答案剛好裝得進 32 位元整數。

這是一個很典型的「限制反映了實作細節」的例子 ——
看到 45 這個奇怪的數字，就該想到「應該是為了不溢位」。

（Python 沒有這個問題，但題目要對所有語言公平。）"""),
     "<strong>n ≤ 45 也表示「純遞迴會 TLE」</strong>："
     "沒有記憶化的話 <code>f(45)</code> 要算約 <code>2 × 1.8 × 10⁹</code> 次遞迴呼叫。",
   ]),
 ],
 "idea": [
   ("t", ["解法", "時間", "空間", "適合"],
     [["純遞迴", "O(φⁿ)", "O(n)", "只當反例"],
      ["記憶化遞迴", "O(n)", "O(n)", "從遞迴式直接翻譯"],
      ["迭代（滾動）", "O(n)", "O(1)", "面試預設"],
      ["矩陣快速冪", "O(log n)", "O(1)", "n 極大時"],
      ["通項公式", "O(1)", "O(1)", "有浮點誤差，不推薦"]]),
 ],
 "approaches": [
   ap("解法一", "迭代 + 兩個變數（標準解）", [
     ("c", S["p70_iter"]),
     ("h", "為什麼初值是 <code>a, b = 1, 1</code>？"),
     ("c", """這裡的 a, b 代表 (f(k-1), f(k))，從 k = 1 開始：
    a = f(0) = 1     「爬 0 階」有 1 種方法：站著不動
    b = f(1) = 1     「爬 1 階」有 1 種方法

每一輪 a, b = b, a + b 讓 k 往前一步。
跑 n-1 輪之後，b = f(n) ✔

驗算 n = 3：
    初始 a=1, b=1        (f(0), f(1))
    輪 1: a=1, b=2       (f(1), f(2))
    輪 2: a=2, b=3       (f(2), f(3))
    回傳 3 ✔

為什麼 f(0) = 1（而不是 0）？
    「爬 0 階」= 已經在頂端 = 什麼都不做 = 1 種方法（空的方法）。

    這和「0! = 1」、「空集合的子集有 1 個」是同一種慣例：
    「什麼都不做」本身就是一種做法。

    如果設成 0，f(2) 會算成 1 而不是 2 ✘"""),
     "<strong><code>a, b = b, a + b</code> 是 Python 的同時賦值</strong> —— "
     "右邊會先全部算完再賦值給左邊，所以不需要暫存變數。"
     "在 C/Java 裡要寫成 <code>int tmp = a + b; a = b; b = tmp;</code>。",
     "<strong>O(1) 空間</strong>。這就是「滾動陣列」的極致 —— 只留兩個變數。",
   ], "O(n)", "O(1)", "n 次迴圈", "兩個變數", optimal=True),

   ap("解法二", "記憶化遞迴（從遞迴式直接翻譯）", [
     ("c", S["p70_memo"]),
     "<strong>優點</strong>：程式碼<strong>就是遞迴式本身</strong>，"
     "不需要思考「迴圈該從哪裡開始」。"
     "在面試時，如果你能寫出遞迴式但一時想不清楚迭代的順序，"
     "<strong>加一個 <code>@lru_cache</code> 就能立刻達到同樣的複雜度</strong>。",
     ("h", "沒有記憶化會有多慢？"),
     ("c", """純遞迴的呼叫次數大約是 2 × f(n)：

    n = 10:  約 177 次        瞬間
    n = 30:  約 270 萬次      約 1 秒
    n = 45:  約 37 億次       約 20 分鐘 ✘

為什麼這麼慢？
    因為 f(n-2) 被算了兩次（一次從 f(n-1)、一次直接），
    f(n-3) 被算了三次…

    呼叫樹的大小是 O(φⁿ)，φ = 1.618（黃金比例）。

加上 @lru_cache 之後，每個 f(k) 只算一次 -> O(n) ✔

「重複子問題」是判斷「該不該用 DP」的第一個訊號。""",),
     "<strong>缺點</strong>：O(n) 的遞迴深度。"
     "n = 45 沒問題，但如果 n 到 10⁵，Python 會 <code>RecursionError</code>。",
   ], "O(n)", "O(n)", "每個 k 算一次", "快取 + 遞迴堆疊"),

   ap("解法三", "矩陣快速冪（O(log n)）", [
     "費氏數列可以寫成矩陣的冪：",
     ("c", """[F(n+1)]   [1 1]   [F(n)  ]
[F(n)  ] = [1 0] · [F(n-1)]

所以：
[F(n+1)]   [1 1]^n   [F(1)]
[F(n)  ] = [1 0]   · [F(0)]

而 [1 1]^n 的左上角就是 F(n+1)
   [1 0]

本題的 f(n) = F(n+1)，所以答案就是那個矩陣 n 次方的左上角。

用第 50 題的快速冪算矩陣的 n 次方 -> O(log n) 次矩陣乘法
每次 2×2 矩陣乘法是 O(1)（8 次乘法）
總共 O(log n) ✔"""),
     ("c", S["p70_matrix"]),
     "<strong>在 n ≤ 45 時完全沒必要</strong>（迭代版只要 45 次加法）。"
     "<strong>但如果 n 到 10¹⁸，這是唯一可行的做法。</strong>",
     "<strong>而且這個技巧能推廣到任何線性遞迴</strong>："
     "<code>f(n) = a·f(n-1) + b·f(n-2) + c·f(n-3)</code> 就用 3×3 矩陣，"
     "複雜度 O(k³ log n)。"
     "在競賽和「求第 n 項模某個數」的題目裡非常常用。",
   ], "O(log n)", "O(1)", "log n 次 2×2 矩陣乘法", "幾個 2×2 矩陣"),
 ],
 "compare": (["解法", "時間", "空間", "n = 10¹⁸ 可行？", "備註"],
   [["純遞迴", "O(φⁿ)", "O(n)", "✘", "只當反例"],
    ["記憶化", "O(n)", "O(n)", "✘", "遞迴式直翻"],
    ["迭代", "O(n)", "O(1)", "✘", "面試預設"],
    ["矩陣快速冪", "O(log n)", "O(1)", "✔", "線性遞迴通用"]]),
 "post": [
   ("note", "通項公式（Binet 公式）為什麼不推薦", [
     ("c", """F(n) = (φⁿ - ψⁿ) / √5

    φ = (1 + √5) / 2 ≈ 1.6180339887   （黃金比例）
    ψ = (1 - √5) / 2 ≈ -0.6180339887

看起來 O(1) 就能算出來，但有兩個問題：

  1. 浮點誤差
     √5 是無理數，浮點數只能近似。
     n 大到一定程度（大約 n > 70），
     算出來的值會偏離正確的整數。

  2. 「O(1)」是假的
     計算 φⁿ 本身就需要 O(log n) 次乘法（快速冪），
     而且要維持足夠的精度，位數會隨 n 增長。

     真正的「大 n」情境下，Binet 公式並不比矩陣快速冪快。

所以：Binet 公式是漂亮的數學結果，
      但在工程上，矩陣快速冪（純整數運算）更可靠。

      這是一個很好的提醒：
      「有封閉形式」不等於「計算上更好」。"""),
   ]),
 ],
 "edges": [
   "<strong>n = 1</strong> → 1。迴圈跑 0 次，直接回傳 <code>b = 1</code>。",
   "<strong>n = 2</strong> → 2。迴圈跑 1 次。",
   "<strong>n = 3</strong> → 3。",
   "<strong>n = 45</strong> → 1836311903。剛好在 <code>INT_MAX</code> 之內。",
   "<strong>初值設錯</strong>：如果設 <code>a, b = 0, 1</code>（標準費氏數列），"
   "會算出 <code>f(3) = 2</code> 而不是 3。"
   "<strong>「f(0) = 1」這個慣例是關鍵。</strong>",
   "<strong>純遞迴</strong>：n = 45 時大約 37 億次呼叫，會 TLE。",
 ],
 "follow": [
   ("h", "追問一：如果每次可以爬 1、2 或 3 階呢？"),
   "<code>f(n) = f(n-1) + f(n-2) + f(n-3)</code>（Tribonacci 數列）。"
   "初值 <code>f(0)=1, f(1)=1, f(2)=2</code>。"
   "<strong>迭代版只要多留一個變數。</strong>",
   ("h", "追問二：如果可以爬「集合 S 裡的任意步數」呢？"),
   "<code>f(n) = Σ f(n - s)，s ∈ S 且 n - s &gt;= 0</code>。"
   "這其實就是<strong>完全背包的「排列數」版本</strong>（第 377 題）—— "
   "外層跑金額、內層跑步數。"
   "（如果外層跑步數、內層跑金額，算出來的是「組合數」，"
   "也就是「不在乎爬的順序」—— 完全不同的問題。）",
   ("h", "追問三：如果某些階梯壞了不能踩呢？"),
   "把壞掉的那一階的 <code>f(i)</code> 設成 0。"
   "<strong>和第 63 題（有障礙物的路徑）完全一樣的處理方式。</strong>",
   ("h", "追問四：如果每一階有「成本」，要求最小成本呢？"),
   "第 746 題（Min Cost Climbing Stairs）。"
   "把「相加」換成「取 min 再加上自己的成本」："
   "<code>dp[i] = min(dp[i-1], dp[i-2]) + cost[i]</code>。"
   "<strong>同一個骨架，換一個聚合運算 —— 和第 62 → 64 題的關係一模一樣。</strong>",
   ("h", "追問五：為什麼這題是 DP 的入門題？"),
   "因為它同時展示了 DP 的三個核心要素，而且每一個都極度單純：",
   ("ul", [
     "<strong>最優子結構</strong>：f(n) 可以從 f(n-1) 和 f(n-2) 算出來",
     "<strong>重複子問題</strong>：純遞迴會重複算 f(n-2) 很多次",
     "<strong>狀態的定義</strong>：「爬到第 i 階的方法數」",
   ]),
   "<strong>把這題的五種寫法（純遞迴 → 記憶化 → 迭代 → 滾動 → 矩陣冪）都寫過一遍，"
   "就等於走過了一次完整的 DP 優化流程。</strong>",
 ],
 "related": [
   "<strong>第 746 題 Min Cost Climbing Stairs</strong> —— 加上成本",
   "<strong>第 509 題 Fibonacci Number</strong> —— 純粹的費氏數列",
   "<strong>第 62 題 Unique Paths</strong> —— 二維版的同一種計數 DP",
   "<strong>第 91 題 Decode Ways</strong> —— 加上「哪些步合法」的限制",
   "<strong>第 198 題 House Robber</strong> —— f(n) = max(f(n-1), f(n-2) + v)",
 ],
 "check": [
   "為什麼 <code>f(0) = 1</code> 而不是 0？設成 0 的話 <code>f(2)</code> 會算出什麼？",
   "純遞迴在 n = 45 時大約要跑幾次？為什麼是指數級？",
   "矩陣 <code>[[1,1],[1,0]]</code> 的 n 次方為什麼會給出費氏數？",
   "為什麼 Binet 通項公式在工程上不如矩陣快速冪可靠？",
 ],
})
print("P70 written")
