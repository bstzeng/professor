# -*- coding: utf-8 -*-
"""第 50–52 題。"""
import random
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(50)

# ==================== 50. Pow(x, n) ====================
S["p50_rec"] = '''class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_pow(base: float, exp: int) -> float:
            if exp == 0:
                return 1.0
            half = fast_pow(base, exp // 2)      # 只算一次，重複使用
            if exp % 2 == 0:
                return half * half
            return half * half * base

        if n < 0:
            return 1.0 / fast_pow(x, -n)
        return fast_pow(x, n)'''

S["p50_iter"] = '''class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        result = 1.0
        # 把 n 寫成二進位，逐位處理
        # x^13 = x^(1101₂) = x^8 · x^4 · x^1
        while n:
            if n & 1:            # 這一位是 1 -> 把當前的 x 乘進答案
                result *= x
            x *= x               # x 平方，對應下一個位元
            n >>= 1

        return result'''

S["p50_naive"] = '''class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 樸素做法：乘 n 次。n 到 2^31 時會 TLE，只當對照
        if n < 0:
            x, n = 1 / x, -n
        result = 1.0
        for _ in range(n):
            result *= x
        return result'''

_p50 = [S.load(k) for k in ("p50_rec", "p50_iter")]
_p50_naive = S.load("p50_naive")
for x, n in [(2.0, 10), (2.1, 3), (2.0, -2), (1.0, 2147483647), (2.0, 0),
             (0.0, 5), (-2.0, 3), (-2.0, 2), (0.00001, 2147483647),
             (2.0, -2147483648), (1.0, -2147483648)]:
    e = x ** n if not (x == 0 and n < 0) else None
    for sol in _p50:
        g = sol.myPow(x, n)
        if e is None:
            continue
        assert abs(g - e) <= 1e-9 * max(1.0, abs(e)), ("P50", x, n, sol, g, e)
for _ in range(5000):
    x = round(random.uniform(-3, 3), 4)
    n = random.randint(-30, 30)
    if x == 0 and n < 0:
        continue
    e = x ** n
    for sol in _p50:
        g = sol.myPow(x, n)
        assert abs(g - e) <= 1e-9 * max(1.0, abs(e)), ("P50", x, n, sol, g, e)
# 樸素版只用小指數比對
for _ in range(500):
    x = round(random.uniform(-2, 2), 3)
    n = random.randint(-12, 12)
    if x == 0 and n < 0:
        continue
    e = _p50_naive.myPow(x, n)
    for sol in _p50:
        assert abs(sol.myPow(x, n) - e) <= 1e-9 * max(1.0, abs(e)), ("P50 naive", x, n)
print("P50 solutions OK")

_P50_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">快速冪：把指數寫成二進位，只要 log n 次乘法</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">x¹³ = x^(1101₂) = x⁸ · x⁴ · x¹</text>
            <g font-family="monospace" font-size="13">
              <text x="40" y="86" fill="var(--text-muted)">輪次</text>
              <text x="130" y="86" fill="var(--text-muted)">n</text>
              <text x="230" y="86" fill="var(--text-muted)">n 的最低位</text>
              <text x="380" y="86" fill="var(--text-muted)">當前的 x</text>
              <text x="500" y="86" fill="var(--text-muted)">result</text>
            </g>
            <line x1="30" y1="96" x2="610" y2="96" stroke="var(--border)"/>
            <g font-family="monospace" font-size="13">
              <text x="40" y="120" fill="var(--text-muted)">0</text>
              <text x="130" y="120" fill="var(--text-muted)">1101</text>
              <text x="230" y="120" fill="var(--gold)">1  ✔ 乘</text>
              <text x="380" y="120" fill="var(--accent)">x¹</text>
              <text x="500" y="120" fill="#ff8a65">x¹</text>

              <text x="40" y="146" fill="var(--text-muted)">1</text>
              <text x="130" y="146" fill="var(--text-muted)">110</text>
              <text x="230" y="146" fill="var(--text-muted)">0  ✘</text>
              <text x="380" y="146" fill="var(--accent)">x²</text>
              <text x="500" y="146" fill="#ff8a65">x¹</text>

              <text x="40" y="172" fill="var(--text-muted)">2</text>
              <text x="130" y="172" fill="var(--text-muted)">11</text>
              <text x="230" y="172" fill="var(--gold)">1  ✔ 乘</text>
              <text x="380" y="172" fill="var(--accent)">x⁴</text>
              <text x="500" y="172" fill="#ff8a65">x⁵</text>

              <text x="40" y="198" fill="var(--text-muted)">3</text>
              <text x="130" y="198" fill="var(--text-muted)">1</text>
              <text x="230" y="198" fill="var(--gold)">1  ✔ 乘</text>
              <text x="380" y="198" fill="var(--accent)">x⁸</text>
              <text x="500" y="198" fill="#ff8a65">x¹³</text>

              <text x="40" y="224" fill="var(--text-muted)">4</text>
              <text x="130" y="224" fill="var(--text-muted)">0</text>
              <text x="230" y="224" fill="var(--text-muted)">結束</text>
            </g>
            <line x1="30" y1="240" x2="610" y2="240" stroke="var(--border)"/>
            <text x="20" y="268" fill="var(--gold)" font-size="12">乘法次數：4 次平方 + 3 次累乘 = 7 次（樸素法要 12 次）</text>
            <text x="20" y="292" fill="var(--text-muted)" font-size="12">n = 2³¹ 時：快速冪約 62 次，樸素法要 21 億次。</text>'''

emit({
 "num": 50, "slug": "powx-n",
 "en": [
   "Implement <code>pow(x, n)</code>, which calculates <code>x</code> raised to the power "
   "<code>n</code> (i.e., <code>x^n</code>).",
 ],
 "zh": [
   "實作 <code>pow(x, n)</code>，也就是計算 <code>x</code> 的 <code>n</code> 次方。",
 ],
 "pre": [
   ("note", "核心想法：平方比連乘快得多", [
     ("c", """樸素做法：x^13 = x·x·x·x·x·x·x·x·x·x·x·x·x   （12 次乘法）

快速冪：    x^13 = x^8 · x^4 · x^1

    而 x^2  = x · x          （1 次）
       x^4  = x^2 · x^2      （1 次）
       x^8  = x^4 · x^4      （1 次）
    再乘起來 x^8 · x^4 · x^1  （2 次）

    總共 5 次。

一般來說：
    樸素   O(n)      次乘法
    快速冪 O(log n)  次乘法

n = 2^31 時：21 億次 vs 62 次。

為什麼是 x^8 · x^4 · x^1？
    因為 13 = 1101₂ = 8 + 4 + 1
    指數的二進位表示，直接告訴我們要乘哪幾個「平方項」。"""),
     "<strong>這個技巧叫做「快速冪（binary exponentiation / exponentiation by squaring）」</strong>，"
     "它適用於任何滿足<strong>結合律</strong>的運算 —— 不只是數字乘法，"
     "矩陣乘法、模乘法、字串串接都可以。",
   ]),
 ],
 "examples": """範例 1
  輸入：x = 2.00000, n = 10
  輸出：1024.00000

範例 2
  輸入：x = 2.10000, n = 3
  輸出：9.26100

範例 3
  輸入：x = 2.00000, n = -2
  輸出：0.25000
  說明：2^-2 = 1/2^2 = 1/4 = 0.25""",
 "constraints": [
   "−100.0 &lt; <code>x</code> &lt; 100.0",
   "−2³¹ ≤ <code>n</code> ≤ 2³¹ − 1",
   "<code>n</code> 是整數",
   "要嘛 <code>x</code> 不是 0，要嘛 <code>n</code> &gt; 0",
   "−10⁴ ≤ <code>x^n</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n 可以是 −2³¹</strong>。"
       "在 C/Java 裡 <code>-n</code> 會溢位（因為 <code>2³¹</code> 超過 <code>INT_MAX</code>）—— "
       "標準做法是先轉成 <code>long</code>。"
       "<strong>Python 沒這個問題</strong>，但面試時值得主動提。",
       "<strong>「要嘛 x 不是 0，要嘛 n &gt; 0」</strong> —— "
       "這排除了 <code>0^(-1)</code>（除以零）。所以不用處理那個邊界。",
       "<strong>x^n 保證在 ±10⁴ 之內</strong> —— 不用擔心浮點溢位。"
       "但<strong>中間結果可能很大</strong>（例如 <code>x = 0.00001</code>、<code>n = -2³¹</code>，"
       "中間會算 <code>100000^(2³¹)</code>… 實際上會變成 <code>inf</code>，"
       "但因為保證最終答案在範圍內，這種輸入不會出現在測資裡）。",
       "<strong>n 可以是 0</strong> → 答案是 1.0（包含 <code>0^0 = 1</code>，這是慣例）。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P50_FIG, "0 0 640 304"),
 ],
 "approaches": [
   ap("解法一", "樸素連乘（會 TLE 的基準線）", [
     ("c", S["p50_naive"]),
     "<code>n = 2³¹ − 1</code> 時要跑 21 億次迴圈 —— 必定 TLE。",
     "<strong>而且浮點數連乘 n 次會累積比較多的捨入誤差</strong>，"
     "快速冪的 log n 次乘法在數值上通常也比較穩定。",
   ], "O(n)", "O(1)", "n 次乘法", "一個變數"),

   ap("解法二", "遞迴快速冪（最好理解）", [
     ("c", S["p50_rec"]),
     ("h", "關鍵是 <code>half</code> 只算一次"),
     ("c", """錯誤寫法（看起來很像，但慢得多）：
    return fast_pow(base, exp // 2) * fast_pow(base, exp // 2)

    這樣會遞迴兩次，變成 T(n) = 2T(n/2) + O(1) = O(n)
    —— 和樸素法一樣慢！

正確寫法：
    half = fast_pow(base, exp // 2)      # 只呼叫一次
    return half * half

    T(n) = T(n/2) + O(1) = O(log n) ✔

這是「分治」與「重複計算」最經典的對照：
差一個變數，複雜度差了指數級。"""),
     ("h", "奇偶兩種情況"),
     ("c", """exp 是偶數： x^exp = (x^(exp/2))²
    x^8 = (x^4)²

exp 是奇數： x^exp = (x^(exp//2))² · x
    x^7 = (x^3)² · x = x^6 · x

    因為 7 // 2 = 3（整數除法捨去），
    (x^3)² = x^6，少了一個 x，補回來。"""),
     ("h", "負指數的處理"),
     "<code>x^(-n) = 1 / x^n</code>。"
     "先算正的再取倒數，比在遞迴裡處理負數乾淨得多。",
     "<strong>遞迴深度是 O(log n)</strong>，n = 2³¹ 時約 31 層 —— 完全安全。",
   ], "O(log n)", "O(log n)", "每層砍一半", "遞迴堆疊"),

   ap("解法三", "迭代快速冪（O(1) 空間，標準寫法）", [
     "把遞迴改成迴圈：<strong>從指數的最低位開始，逐位決定「要不要把當前的平方項乘進答案」。</strong>",
     ("c", S["p50_iter"]),
     ("h", "三行迴圈在做什麼"),
     ("c", """while n:
    if n & 1:      # n 的最低位是 1 嗎？
        result *= x
    x *= x         # x 平方，準備下一個位元
    n >>= 1        # n 右移一位

不變量：
    進入第 k 輪時，x 的值是「原本的 x 的 2^k 次方」，
    而 n 是「原本的 n 右移 k 位」。

    如果 n 的第 k 位是 1，就把 x^(2^k) 乘進 result。

    最後 result = ∏ x^(2^k)，其中 k 跑遍 n 的所有 1 位元
                = x^(所有 2^k 之和)
                = x^n  ✔

x^13，13 = 1101₂：
    k=0: 位元 1 -> result = x^1     x 變成 x^2
    k=1: 位元 0 ->                  x 變成 x^4
    k=2: 位元 1 -> result = x^5     x 變成 x^8
    k=3: 位元 1 -> result = x^13    x 變成 x^16（用不到）
    n 變成 0，結束 ✔"""),
     ("h", "為什麼這是最該記的版本？"),
     ("ul", [
       "<strong>O(1) 空間</strong>（沒有遞迴堆疊）",
       "<strong>只有 5 行</strong>，而且結構固定，很難寫錯",
       "<strong>直接推廣到「模冪」</strong>：把 <code>*=</code> 換成 <code>= (... * ...) % m</code>，"
       "就是 RSA 和 Diffie-Hellman 的核心運算",
       "<strong>直接推廣到矩陣快速冪</strong>：把 <code>*</code> 換成矩陣乘法，"
       "就能在 O(log n) 算費氏數列的第 n 項",
     ]),
     ("h", "在 C/Java 裡的溢位陷阱"),
     ("c", """if (n < 0) { x = 1 / x; n = -n; }

n = INT_MIN = -2147483648 時，
-n = 2147483648 > INT_MAX = 2147483647  -> 溢位！
結果 -n 還是 INT_MIN（負數），while (n) 會變成無窮迴圈或直接錯。

標準修法：先轉成 64 位元
    long N = n;
    if (N < 0) { x = 1 / x; N = -N; }

Python 沒有這個問題（任意精度整數），
但這是這題在 C/Java 面試裡最常見的扣分點。"""),
   ], "O(log n)", "O(1)", "log n 輪，每輪 2 次乘法", "三個變數", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "n=2³¹ 能過？", "備註"],
   [["一、樸素連乘", "O(n)", "O(1)", "✘", "基準線"],
    ["二、遞迴快速冪", "O(log n)", "O(log n)", "✔", "最好解釋"],
    ["三、迭代快速冪", "O(log n)", "O(1)", "✔", "最該記的版本"]]),
 "edges": [
   "<strong><code>n = 0</code></strong>：任何 <code>x</code> 都回 1.0（含 <code>0^0 = 1</code>）。",
   "<strong><code>n</code> 是負數</strong>：<code>(2.0, -2)</code> → 0.25。",
   "<strong><code>n = -2³¹</code></strong>：<strong>C/Java 會在 <code>-n</code> 溢位。</strong>",
   "<strong><code>x = 1.0</code>、<code>n</code> 很大</strong>：<code>(1.0, 2147483647)</code> → 1.0。"
   "樸素法會跑 21 億次，快速冪只要 31 次。",
   "<strong><code>x</code> 是負數</strong>：<code>(-2.0, 3)</code> → −8.0；<code>(-2.0, 2)</code> → 4.0。"
   "奇偶次方的符號不同 —— 快速冪自然處理（符號跟著乘法走）。",
   "<strong><code>x = 0</code>、<code>n &gt; 0</code></strong> → 0.0。題目保證不會有 <code>n ≤ 0</code> 的情況。",
   "<strong><code>x</code> 接近 1、<code>n</code> 很大</strong>：浮點誤差會累積。"
   "這也是快速冪的另一個好處：乘法次數少，誤差也少。",
 ],
 "follow": [
   ("h", "追問一：模冪 <code>(x^n) mod m</code> 呢？"),
   ("c", """只要在每次乘法後取模：

class Solution:
    def mod_pow(self, x, n, m):
        result = 1
        x %= m
        while n:
            if n & 1:
                result = result * x % m
            x = x * x % m
            n >>= 1
        return result

這就是 Python 內建的 pow(x, n, m)。

為什麼可以中途取模？
    因為 (a·b) mod m = ((a mod m)·(b mod m)) mod m
    模運算和乘法「相容」，所以可以隨時取模，
    避免中間結果變成天文數字。

這是 RSA 加密、Diffie-Hellman 金鑰交換、
以及所有「大數模運算」的核心。
如果沒有快速冪，RSA 的每次加解密要做 2^2048 次乘法 —— 完全不可行。""",),
   ("h", "追問二：矩陣快速冪能做什麼？"),
   ("c", """費氏數列：
    [F(n+1)]   [1 1]^n   [F(1)]
    [F(n)  ] = [1 0]   · [F(0)]

用快速冪算那個矩陣的 n 次方 -> O(log n) 算出 F(n)。
（樸素的遞推是 O(n)。）

更一般地：任何「線性遞迴關係」都能寫成矩陣冪，
所以都能用快速冪加速到 O(k³ log n)，k 是遞迴的階數。

這在競賽和密碼學裡都很常用。""",),
   ("h", "追問三：真正的 <code>pow()</code>（浮點指數）是怎麼實作的？"),
   "完全不同的演算法。"
   "<code>pow(x, y)</code> 當 <code>y</code> 是浮點數時，用的是 "
   "<code>exp(y · log(x))</code>，而 <code>exp</code> 和 <code>log</code> "
   "用的是多項式逼近（通常是 minimax 多項式或 CORDIC）。",
   "<strong>但那樣會有精度損失</strong> —— 所以 C 的 <code>pow(2.0, 10.0)</code> "
   "在某些平台上可能回傳 <code>1023.9999999</code> 而不是 <code>1024.0</code>。"
   "好的實作會特判「指數是整數」的情況，改用快速冪。"
   "<strong>這也是為什麼這題值得會：整數指數有更快、更精確的算法。</strong>",
   ("h", "追問四：能不能用更少的乘法？"),
   "快速冪不一定是「乘法次數最少」的方案。"
   "例如 <code>x^15</code>，快速冪要 6 次乘法，"
   "但 <code>x^15 = ((x^3)^5)</code> 只要 5 次。"
   "「最少乘法次數」是<strong>加法鏈（addition chain）問題</strong>，"
   "求最優解是 NP-hard。"
   "<strong>快速冪是一個「足夠好而且保證 O(log n)」的近似</strong> —— "
   "這是工程上很常見的取捨。",
 ],
 "related": [
   "<strong>第 29 題 Divide Two Integers</strong> —— 同樣的「倍增」思維",
   "<strong>第 372 題 Super Pow</strong> —— 指數是一個大數（用陣列表示）",
   "<strong>第 69 題 Sqrt(x)</strong> —— 另一個數值計算題",
   "<strong>第 509 題 Fibonacci Number</strong> —— 矩陣快速冪的應用",
 ],
 "check": [
   "為什麼 <code>half = fast_pow(base, exp//2)</code> 要存進變數？"
   "寫成呼叫兩次的複雜度是多少？",
   "迭代版的三行迴圈，每一輪的 <code>x</code> 代表什麼？請寫出不變量。",
   "在 Java 裡 <code>n = -2³¹</code> 會發生什麼？該怎麼修？",
   "把 <code>*=</code> 換成模乘法之後，這個演算法在密碼學裡叫什麼？為什麼它是 RSA 的關鍵？",
 ],
})
print("P50 written")
