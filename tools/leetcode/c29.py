# -*- coding: utf-8 -*-
"""第 29–31 題。"""
import random, collections
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(29)
INT_MIN, INT_MAX = -2**31, 2**31 - 1

# ==================== 29. Divide Two Integers ====================
S["p29_sub"] = '''class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # 唯一會溢位的情況：-2^31 / -1 = 2^31，超過 INT_MAX
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)   # 異號才是負的
        a, b = abs(dividend), abs(divisor)

        quotient = 0
        while a >= b:            # 一次減一個 b —— 正確但會 TLE
            a -= b
            quotient += 1

        return -quotient if negative else quotient'''

S["p29_shift"] = '''class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)

        quotient = 0
        while a >= b:
            # 找出最大的 k，使得 b << k 仍然 <= a
            temp, multiple = b, 1
            while a >= (temp << 1):
                temp <<= 1           # temp 翻倍
                multiple <<= 1       # 對應的商也翻倍
            a -= temp
            quotient += multiple

        return -quotient if negative else quotient'''

S["p29_bits"] = '''class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        negative = (dividend < 0) != (divisor < 0)
        a, b = abs(dividend), abs(divisor)

        # 從高位往低位試：這一位能不能填 1？
        # 就是長除法（直式除法）的二進位版本
        quotient = 0
        for k in range(31, -1, -1):
            if (b << k) <= a:
                a -= b << k
                quotient |= 1 << k

        return -quotient if negative else quotient'''

_p29 = [S.load(k) for k in ("p29_sub", "p29_shift", "p29_bits")]


def _p29_ref(x, y):
    if x == INT_MIN and y == -1:
        return INT_MAX
    q = abs(x) // abs(y)
    if (x < 0) != (y < 0):
        q = -q
    return max(INT_MIN, min(INT_MAX, q))


for x, y in [(10, 3), (7, -3), (-2147483648, -1), (-2147483648, 1), (1, 1),
             (0, 5), (-1, 1), (2147483647, 1), (-2147483648, 2), (1, -1)]:
    e = _p29_ref(x, y)
    for sol in _p29[1:]:
        assert sol.divide(x, y) == e, ("P29", x, y, sol, sol.divide(x, y), e)
for _ in range(3000):
    x = random.randint(INT_MIN, INT_MAX)
    y = random.choice([random.randint(-50, 50), random.randint(INT_MIN, INT_MAX)])
    if y == 0:
        continue
    e = _p29_ref(x, y)
    for sol in _p29[1:]:
        assert sol.divide(x, y) == e, ("P29", x, y, sol, sol.divide(x, y), e)
# 逐次相減版只用小數字測（會很慢）
for _ in range(300):
    x = random.randint(-300, 300)
    y = random.choice([i for i in range(-9, 10) if i != 0])
    assert _p29[0].divide(x, y) == _p29_ref(x, y), ("P29 sub", x, y)
print("P29 solutions OK")

_P29_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">43 ÷ 3：二進位長除法，從高位往低位問「這一位能填 1 嗎？」</text>
            <g font-family="monospace" font-size="13">
              <text x="40" y="54" fill="var(--text-muted)">k = 5:  3 &lt;&lt; 5 = 96  &gt; 43  ✘  這一位填 0</text>
              <text x="40" y="78" fill="var(--text-muted)">k = 4:  3 &lt;&lt; 4 = 48  &gt; 43  ✘  填 0</text>
              <text x="40" y="102" fill="var(--gold)">k = 3:  3 &lt;&lt; 3 = 24  ≤ 43  ✔  填 1，a = 43 − 24 = 19</text>
              <text x="40" y="126" fill="var(--gold)">k = 2:  3 &lt;&lt; 2 = 12  ≤ 19  ✔  填 1，a = 19 − 12 = 7</text>
              <text x="40" y="150" fill="var(--gold)">k = 1:  3 &lt;&lt; 1 = 6   ≤ 7   ✔  填 1，a = 7 − 6 = 1</text>
              <text x="40" y="174" fill="var(--text-muted)">k = 0:  3 &lt;&lt; 0 = 3   &gt; 1   ✘  填 0</text>
            </g>
            <line x1="20" y1="192" x2="620" y2="192" stroke="var(--border)"/>
            <g font-family="monospace" font-size="14">
              <text x="40" y="222" fill="var(--accent)">商 = 0b001110 = 14</text>
              <text x="300" y="222" fill="var(--accent)">餘 = 1</text>
              <text x="40" y="250" fill="var(--text-muted)" font-size="12">驗算：14 × 3 + 1 = 43 ✔</text>
            </g>
            <text x="20" y="284" fill="var(--gold)" font-size="12">最多 32 位 → 最多 32 輪。比「一次減 3」的 14 輪穩定得多（想像 2³¹ ÷ 1）。</text>'''

emit({
 "num": 29, "slug": "divide-two-integers",
 "en": [
   "Given two integers <code>dividend</code> and <code>divisor</code>, divide two integers "
   "<strong>without</strong> using multiplication, division, and mod operator.",
   "The integer division should truncate toward zero, which means losing its fractional part. "
   "For example, <code>8.345</code> would be truncated to <code>8</code>, and "
   "<code>-2.7335</code> would be truncated to <code>-2</code>.",
   "Return the quotient. If the quotient is strictly greater than <code>2³¹ - 1</code>, "
   "return <code>2³¹ - 1</code>; if less than <code>-2³¹</code>, return <code>-2³¹</code>.",
 ],
 "zh": [
   "給你兩個整數 <code>dividend</code>（被除數）和 <code>divisor</code>（除數），"
   "在<strong>不使用乘法、除法和取餘運算子</strong>的前提下做整數除法。",
   "結果要<strong>向零取整</strong>（截斷小數部分）。"
   "例如 <code>8.345</code> 截斷成 <code>8</code>，<code>-2.7335</code> 截斷成 <code>-2</code>（不是 −3）。",
   "回傳商。如果商大於 <code>2³¹ − 1</code> 就回 <code>2³¹ − 1</code>，"
   "小於 <code>−2³¹</code> 就回 <code>−2³¹</code>。",
 ],
 "pre": [
   ("note", "三個陷阱，一個比一個隱蔽", [
     ("c", """陷阱 1：溢位。而且只有「一種」情況會溢位。

    -2³¹ / -1 = 2³¹ = 2147483648 > INT_MAX = 2147483647

    其他所有組合的商都在範圍內：
      任何數除以 |divisor| >= 1 只會變小或不變，
      而 dividend 本身一定在範圍內。
      唯一的例外就是「最負的數 ÷ -1」，因為正負兩側不對稱。

陷阱 2：向零取整，不是向下取整。

    -7 / 3  ->  -2   （不是 -3！）
     7 / -3 ->  -2

    Python 的 // 是「向下取整（floor）」：
        -7 // 3 == -3    ✘ 和題目要的不一樣
    Python 的 int() 對浮點數是向零截斷，但不能用除法。

    正確做法：取絕對值算、最後補上符號。
        abs(-7) // abs(3) = 2，異號 -> -2 ✔

陷阱 3：Python 沒有 32 位元整數。

    在 C/Java 裡，abs(INT_MIN) 本身就會溢位。
    標準做法是「全程用負數算」，因為負數那一側範圍比較大。
    Python 沒這個問題，但面試官可能會問。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：dividend = 10, divisor = 3
  輸出：3
  說明：10 / 3 = 3.333... 截斷成 3。

範例 2
  輸入：dividend = 7, divisor = -3
  輸出：-2
  說明：7 / -3 = -2.333... 向零截斷成 -2（不是 -3）。""",
 "constraints": [
   "−2³¹ ≤ <code>dividend</code>, <code>divisor</code> ≤ 2³¹ − 1",
   "<code>divisor != 0</code>（不用處理除以零）",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>保證 divisor 不是 0</strong>，省掉一個邊界。",
       "<strong>只有 <code>INT_MIN / -1</code> 會溢位</strong>。"
       "所以「clamp 到範圍內」實際上只要寫一個 if。"
       "很多人會寫一大串 min/max，那是沒想清楚。",
       "<strong>不能用 <code>*</code>、<code>/</code>、<code>%</code></strong>。"
       "但<strong>可以用位移 <code>&lt;&lt;</code> <code>&gt;&gt;</code>、加減、比較</strong> —— "
       "而位移就是乘除 2 的冪次。這就是這題的解法方向。",
     ]),
   ]),
 ],
 "idea": [
   "<strong>除法的本質是「減多少次」。</strong>"
   "一次減一個太慢，所以改成<strong>一次減掉「除數的 2 的冪次倍」</strong> —— "
   "這正是我們小學學的直式除法，只是換成二進位。",
   ("fig", _P29_FIG, "0 0 640 296"),
 ],
 "approaches": [
   ap("解法一", "一次減一個（會 TLE 的基準線）", [
     ("c", S["p29_sub"]),
     "邏輯完全正確，但當 <code>dividend = 2³¹ − 1</code>、<code>divisor = 1</code> 時，"
     "要跑 21 億次迴圈 —— 必定 TLE。",
     "<strong>但它的前兩行（溢位檢查、符號處理）在後面兩個解法裡完全一樣</strong>，"
     "所以先把它寫對是有價值的。",
   ], "O(dividend / divisor)", "O(1)", "最壞 2³¹ 次", "幾個變數"),

   ap("解法二", "倍增：每次減掉「盡可能大」的一塊", [
     "既然一次減一個太慢，那就<strong>一次減掉 divisor 的 2 的冪次倍</strong>。"
     "而 <code>b × 2ᵏ</code> 用位移就能算出來，不算乘法。",
     ("c", S["p29_shift"]),
     ("c", """43 ÷ 3

外層第 1 輪（a = 43）：
    temp = 3,  multiple = 1
    43 >= 6?  ✔ -> temp = 6,  multiple = 2
    43 >= 12? ✔ -> temp = 12, multiple = 4
    43 >= 24? ✔ -> temp = 24, multiple = 8
    43 >= 48? ✘ 停
    a = 43 - 24 = 19，quotient = 8

外層第 2 輪（a = 19）：
    temp = 3, multiple = 1
    19 >= 6?  ✔ -> temp = 6,  multiple = 2
    19 >= 12? ✔ -> temp = 12, multiple = 4
    19 >= 24? ✘ 停
    a = 19 - 12 = 7，quotient = 12

外層第 3 輪（a = 7）：
    7 >= 6? ✔ -> temp = 6, multiple = 2
    7 >= 12? ✘ 停
    a = 7 - 6 = 1，quotient = 14

a = 1 < 3，結束。答案 14 ✔"""),
     ("h", "為什麼是 O(log²n)？"),
     "外層每輪至少把 <code>a</code> 砍掉一半（因為減掉的 <code>temp</code> 至少是 "
     "<code>a</code> 的一半），所以外層最多 32 輪；"
     "內層的倍增也最多 32 次。總共 O(log² n) —— 大約 1024 次運算，瞬間完成。",
     "<strong>注意內層條件是 <code>a &gt;= (temp &lt;&lt; 1)</code> 而不是 <code>a &gt;= temp</code>。</strong>"
     "我們要找的是「翻倍之後<strong>還不會超過</strong>」的最大值，"
     "所以要先試探翻倍後的結果。寫錯的話 <code>temp</code> 會超過 <code>a</code>，減出負數。",
   ], "O(log²n)", "O(1)", "外層 log n 輪 × 內層 log n", "幾個變數"),

   ap("解法三", "二進位長除法（最乾淨）", [
     "把解法二的兩層迴圈<strong>攤平成一層</strong>：直接從第 31 位往下問"
     "「這一位的商能不能是 1？」",
     ("c", S["p29_bits"]),
     "<strong>這就是我們小學學的直式除法，只是基底從 10 換成 2。</strong>"
     "十進位的直式除法每一位要試 0–9（十選一），"
     "二進位每一位只要試 0 或 1（能減就是 1，不能就是 0）—— "
     "<strong>這正是為什麼電腦用二進位做除法比較簡單。</strong>",
     ("c", """43 ÷ 3，從 k = 31 開始（前面全是 0，略過）

k=5: 3<<5 = 96 > 43  -> 商的第 5 位 = 0
k=4: 3<<4 = 48 > 43  -> 第 4 位 = 0
k=3: 3<<3 = 24 <= 43 -> 第 3 位 = 1，a = 43-24 = 19
k=2: 3<<2 = 12 <= 19 -> 第 2 位 = 1，a = 19-12 = 7
k=1: 3<<1 = 6  <= 7  -> 第 1 位 = 1，a = 7-6 = 1
k=0: 3<<0 = 3  > 1   -> 第 0 位 = 0

商 = 0b001110 = 14，餘 = 1
驗算：14 × 3 + 1 = 43 ✔"""),
     "<strong>固定 32 輪</strong>，不管數字多大 —— 複雜度是 O(32) = O(1)。"
     "而且沒有巢狀迴圈，最好讀也最好記。",
     ("h", "在 C/Java 裡要注意什麼？"),
     ("c", """b << k 在 32 位元裡可能溢位！

C/Java 的正確寫法是反過來比：
    if ((a >>> k) >= b)        // 無號右移，避免符號位問題
        a -= b << k;

或者全程用 long（64 位元）來算 b << k。

Python 沒有這個問題（整數任意精度），
但如果面試官問「這段翻成 C 會怎樣」，
要能指出這一行。"""),
   ], "O(32) = O(1)", "O(1)", "固定 32 輪", "幾個變數", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "會 TLE？", "備註"],
   [["一、逐次相減", "O(n)", "O(1)", "✔ 會", "邏輯基準"],
    ["二、倍增", "O(log²n)", "O(1)", "✘", "直觀，但有巢狀迴圈"],
    ["三、二進位長除法", "O(32)", "O(1)", "✘", "最乾淨；就是直式除法"]]),
 "edges": [
   "<strong><code>INT_MIN / -1</code></strong> → <code>INT_MAX</code>。"
   "<strong>唯一會溢位的組合</strong>，一定要單獨擋。",
   "<strong><code>INT_MIN / 1</code></strong> → <code>INT_MIN</code>。"
   "不溢位，不能被上面那個 if 誤攔。",
   "<strong>被除數是 0</strong>：<code>(0, 5)</code> → 0。while 一次都不跑。",
   "<strong>除數比被除數大</strong>：<code>(1, 2)</code> → 0。",
   "<strong>剛好整除</strong>：<code>(6, 3)</code> → 2。",
   "<strong>負數的向零取整</strong>：<code>(7, -3)</code> → −2（不是 −3）；"
   "<code>(-7, 3)</code> → −2；<code>(-7, -3)</code> → 2。四種符號組合都要測。",
   "<strong>除以 1 和 −1</strong>：<code>(2147483647, 1)</code> → 2147483647。"
   "這是解法一 TLE 的測資。",
 ],
 "follow": [
   ("h", "追問一：如果還要回傳餘數呢？"),
   "解法三跑完之後，<code>a</code> 裡剩下的就是餘數（絕對值）。"
   "符號依照語言慣例：C99 和 Java 的 <code>%</code> 結果跟<strong>被除數</strong>同號，"
   "Python 的 <code>%</code> 跟<strong>除數</strong>同號。"
   "<code>-7 % 3</code> 在 C 裡是 −1，在 Python 裡是 2。"
   "<strong>這個差別在跨語言移植時害過很多人。</strong>",
   ("h", "追問二：CPU 是怎麼做除法的？"),
   "本質上就是解法三 —— 硬體版的「回復餘數法（restoring division）」"
   "或它的改良版「不回復餘數法（non-restoring division）」，"
   "一個時脈週期算一位。"
   "<strong>這也是為什麼整數除法比乘法慢很多</strong>"
   "（在現代 x86 上，乘法約 3–5 個週期，除法約 20–40 個）。",
   "編譯器知道這一點，所以<strong>看到「除以常數」時會把它改寫成乘法 + 位移</strong>。"
   "例如 <code>x / 3</code> 會被編譯成大約 "
   "<code>(x * 0xAAAAAAAB) &gt;&gt; 33</code> —— "
   "用一個「魔術數字」（1/3 的定點數近似）的乘法取代除法。"
   "這個技巧叫做 <strong>Barrett reduction / magic number division</strong>。",
   ("h", "追問三：如果不准用減法呢？"),
   "那就只剩位元運算了。加法可以用 <code>XOR</code>（不進位加）和 "
   "<code>AND + 左移</code>（進位）遞迴實作；"
   "減法是「加上二補數」。這就是第 371 題（Sum of Two Integers）。"
   "把那題和這題組合起來，就能在<strong>只用位元運算</strong>的前提下做除法。",
 ],
 "related": [
   "<strong>第 7 題 Reverse Integer</strong> —— 同一套 32 位元溢位思維",
   "<strong>第 50 題 Pow(x, n)</strong> —— 同樣的「倍增 / 二進位分解」技巧",
   "<strong>第 371 題 Sum of Two Integers</strong> —— 只用位元做加法",
   "<strong>第 166 題 Fraction to Recurring Decimal</strong> —— 長除法的延伸",
 ],
 "check": [
   "為什麼只有 <code>INT_MIN / -1</code> 會溢位？請說明其他組合為什麼都安全。",
   "Python 的 <code>-7 // 3</code> 是多少？和題目要的答案差在哪？為什麼要先取絕對值？",
   "解法二的內層條件為什麼是 <code>a &gt;= (temp &lt;&lt; 1)</code> 而不是 <code>a &gt;= temp</code>？",
   "解法三翻成 C 的話，<code>b &lt;&lt; k</code> 這一行有什麼問題？該怎麼改？",
 ],
})
print("P29 written")

# ==================== 30. Substring with Concatenation of All Words ====================
S["p30_naive"] = '''from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        m = len(words)            # 單字個數
        w = len(words[0])         # 每個單字的長度（題目保證等長）
        total = m * w
        need = Counter(words)
        out = []

        for i in range(len(s) - total + 1):
            seen = Counter()
            for j in range(m):
                piece = s[i + j * w: i + (j + 1) * w]
                if piece not in need:
                    break             # 根本不是任何一個單字
                seen[piece] += 1
                if seen[piece] > need[piece]:
                    break             # 這個單字用太多次了
            else:
                out.append(i)         # for 沒有 break -> 全部配對成功

        return out'''

S["p30_window"] = '''from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        m = len(words)
        w = len(words[0])
        total = m * w
        n = len(s)
        if n < total:
            return []

        need = Counter(words)
        out = []

        # 依「起點對 w 取餘數」分成 w 組，每組各做一次滑動視窗
        for offset in range(w):
            left = offset
            count = 0                 # 視窗裡目前有幾個單字
            window = Counter()

            for right in range(offset, n - w + 1, w):
                piece = s[right: right + w]

                if piece not in need:
                    # 整個視窗作廢，從下一格重新開始
                    window.clear()
                    count = 0
                    left = right + w
                    continue

                window[piece] += 1
                count += 1

                # 這個單字用太多次 -> 從左邊縮，直到把多出來的那個吐掉
                while window[piece] > need[piece]:
                    window[s[left: left + w]] -= 1
                    left += w
                    count -= 1

                if count == m:
                    out.append(left)
                    # 視窗已經滿了，吐掉最左邊一個再繼續
                    window[s[left: left + w]] -= 1
                    left += w
                    count -= 1

        return out'''

_p30 = [S.load(k) for k in ("p30_naive", "p30_window")]
for s_, ws in [("barfoothefoobarman", ["foo", "bar"]),
               ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
               ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
               ("aaa", ["a", "a"]), ("a", ["a"]), ("ab", ["ba"]),
               ("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]),
               ("aaaaaa", ["aa", "aa", "aa"])]:
    e = sorted(_p30[0].findSubstring(s_, list(ws)))
    g = sorted(_p30[1].findSubstring(s_, list(ws)))
    assert g == e, ("P30", s_, ws, g, e)
for _ in range(1500):
    w = random.randint(1, 3)
    m = random.randint(1, 3)
    ws = ["".join(random.choice("ab") for _ in range(w)) for _ in range(m)]
    s_ = "".join(random.choice("ab") for _ in range(random.randint(0, 12)))
    e = sorted(_p30[0].findSubstring(s_, list(ws)))
    g = sorted(_p30[1].findSubstring(s_, list(ws)))
    assert g == e, ("P30", s_, ws, g, e)
print("P30 solutions OK")

emit({
 "num": 30, "slug": "substring-with-concatenation-of-all-words",
 "en": [
   "You are given a string <code>s</code> and an array of strings <code>words</code>. "
   "All the strings of <code>words</code> are of <strong>the same length</strong>.",
   "A <strong>concatenated substring</strong> in <code>s</code> is a substring that contains "
   "all the strings of <code>words</code> concatenated in <strong>any order</strong>, exactly "
   "once, with no other characters in between.",
   "Return the starting indices of all the concatenated substrings in <code>s</code>. "
   "You can return the answer in any order.",
 ],
 "zh": [
   "給你一個字串 <code>s</code> 和一個字串陣列 <code>words</code>，"
   "<code>words</code> 裡所有字串的<strong>長度都相同</strong>。",
   "所謂<strong>串聯子字串</strong>，是指 <code>s</code> 的一段子字串，"
   "它剛好由 <code>words</code> 裡<strong>所有</strong>單字以<strong>任意順序</strong>串接而成，"
   "每個單字恰好用一次，中間不能有多餘的字元。",
   "回傳所有串聯子字串的<strong>起始索引</strong>，順序不拘。",
 ],
 "pre": [
   ("note", "「所有單字等長」是這題唯一可用的槓桿", [
     ("c", """如果單字長度不一樣，這題會變成一個相當困難的搜尋問題。
題目保證等長，所以：

    1. 串聯子字串的長度是固定的 = m × w
       （m = 單字個數，w = 單字長度）

    2. 可以把 s 按 w 切塊，一次看 w 個字元，
       而不是一個字元一個字元看。

    3. 起點只有 w 種「對齊方式」：
       i % w == 0, 1, 2, ..., w-1
       同一組對齊的起點之間可以共用計算 -> 滑動視窗。

例子：
    s = "barfoothefoobarman"，words = ["foo","bar"]
    m = 2, w = 3, total = 6

    i=0:  "barfoo"  = bar + foo  ✔ 兩個都用到，各一次
    i=9:  "foobar"  = foo + bar  ✔
    答案 [0, 9]

    注意 words 可能有重複：
    words = ["a","a"] 表示需要「兩個 a」，不是「一個 a」。
    所以要用 Counter 而不是 set。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "barfoothefoobarman", words = ["foo","bar"]
  輸出：[0,9]
  說明：索引 0 開始的 "barfoo" 和索引 9 開始的 "foobar"。

範例 2
  輸入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
  輸出：[]
  說明：需要兩個 "word"，但沒有任何一段同時包含兩個 word 和 good、best。

範例 3
  輸入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
  輸出：[6,9,12]""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁴",
   "1 ≤ <code>words.length</code> ≤ 5000",
   "1 ≤ <code>words[i].length</code> ≤ 30",
   "<code>s</code> 和 <code>words[i]</code> 只含小寫英文字母",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong><code>words</code> 可以有重複的單字。</strong>"
       "<code>[\"word\",\"good\",\"best\",\"word\"]</code> 需要<strong>兩個</strong> word。"
       "所以必須用 <code>Counter</code>（多重集合）而不是 <code>set</code>。"
       "<strong>這是本題最常見的錯誤。</strong>",
       "<strong>n ≤ 10⁴、m ≤ 5000、w ≤ 30</strong>。"
       "暴力法是 O(n × m × w)，最壞 10⁴ × 5000 × 30 = 1.5 × 10⁹ —— 太慢。"
       "但注意 <code>m × w ≤ n</code> 才可能有答案，所以實際上 "
       "<strong>O(n × m)</strong> 已經夠好（Python 的切片和 Counter 有常數開銷，"
       "但暴力法在 LeetCode 上通常能過）。"
       "滑動視窗的 O(n × w) 才是真正漂亮的解。",
       "<strong>單字長度可以到 30</strong>，所以「w 組對齊」最多 30 組。",
     ]),
   ]),
 ],
 "idea": [
   ("c", """兩種解法：

暴力法：對每個起點 i，把後面 m 個單字切出來逐一檢查
        O(n × m × w)，但一旦發現不對就提早退出，實測不算慢

滑動視窗：把起點按 i % w 分成 w 組，每組維護一個視窗
          每個字元進出視窗各一次
          O(n × w)   —— w 是單字長度，最多 30

為什麼要分成 w 組？

    s = "barfoothefoobarman"，w = 3

    對齊方式 0： bar|foo|the|foo|bar|man     起點 0, 3, 6, 9, 12, 15
    對齊方式 1： b|arf|oot|hef|oob|arm|an    起點 1, 4, 7, 10, 13, 16
    對齊方式 2： ba|rfo|oth|efo|oba|rma|n    起點 2, 5, 8, 11, 14, 17

    同一組裡的起點，切出來的「單字邊界」是一致的，
    所以可以像一般的滑動視窗那樣「右邊進、左邊出」。
    不同組之間邊界不同，不能混在一起，所以要跑 w 次。"""),
 ],
 "approaches": [
   ap("解法一", "枚舉每個起點，逐塊檢查", [
     ("c", S["p30_naive"]),
     ("h", "Python 的 <code>for ... else</code>"),
     ("c", """for j in range(m):
    ...
    if 有問題:
        break
else:
    out.append(i)      # 只有「沒 break」才會執行

for-else 的 else 是「迴圈正常跑完」才執行，
被 break 中斷就不執行。

這個語法在「搜尋失敗才做某事」的場景很好用，
但很多人沒看過，會誤以為 else 配的是 if。
面試時建議改寫成一個 bool 旗標，比較不會造成誤解。"""),
     ("h", "兩個提早退出的條件"),
     ("ul", [
       "<code>piece not in need</code>：切出來的根本不是清單裡的任何單字 —— 立刻失敗。",
       "<code>seen[piece] &gt; need[piece]</code>：這個單字用超過允許的次數 —— 立刻失敗。"
       "<strong>這就是為什麼用 Counter 而不是 set。</strong>",
     ]),
     "<strong>為什麼不用比較 <code>seen == need</code>？</strong>"
     "因為我們一路檢查「沒有超量」，而且總共放進 <code>m</code> 個，"
     "所以跑完 <code>m</code> 輪就一定剛好相等。提早檢查比最後比較兩個 Counter 快得多。",
     "實測上這個解法在 LeetCode 通常能過，因為提早退出很有效 —— "
     "大部分起點在第一塊就失敗了。",
   ], "O(n·m·w) 最壞", "O(m·w)", "n 個起點 × m 塊 × 切片 O(w)", "兩個 Counter"),

   ap("解法二", "分組滑動視窗（最佳解）", [
     "暴力法的浪費：相鄰的起點 <code>i</code> 和 <code>i+w</code> 共用了 <code>m−1</code> 塊，"
     "卻各自重算一遍。滑動視窗把這些共用的部分留下來。",
     ("c", S["p30_window"]),
     ("h", "三種情況，對應三段程式碼"),
     ("c", """情況 A：切出來的不是任何單字
    整個視窗都作廢（因為任何包含這塊的視窗都不可能成立）
    -> window.clear(), count = 0, left 跳到這塊後面

情況 B：是單字，但用太多次
    不能整個丟掉，只要從左邊吐到「不超量」為止
    -> while window[piece] > need[piece]: 吐最左邊那塊

    例：need = {"a": 1}，視窗是 [a]，現在又進來一個 a
        吐掉最左邊的 a，視窗變成 [a]（新的那個）

情況 C：視窗剛好滿了（count == m）
    記下答案，然後吐掉最左邊一塊，繼續往右找
    （不能停下來，後面可能還有答案）"""),
     ("h", "為什麼是 O(n × w) 而不是 O(n)？"),
     "因為要跑 <code>w</code> 組（<code>w</code> 種對齊方式）。"
     "每一組裡，<code>left</code> 和 <code>right</code> 各自只往右走 "
     "<code>n/w</code> 步，所以每組是 O(n/w) 次「塊操作」，"
     "每次塊操作要做一次長度 <code>w</code> 的切片和雜湊 —— O(w)。"
     "每組 O(n)，共 w 組 —— <strong>O(n × w)</strong>。",
     "相較暴力法的 O(n × m × w)，這裡把 <code>m</code> 換成了 1。"
     "當單字很多（m = 5000）時差距非常大。",
     ("h", "常見的實作錯誤"),
     ("ul", [
       "<strong>忘記在情況 C 之後吐掉最左邊</strong> —— 視窗會永遠滿著，只找到第一個答案。",
       "<strong>情況 A 忘記把 <code>left</code> 跳到 <code>right + w</code></strong> —— "
       "視窗會殘留無效的塊。",
       "<strong><code>range(offset, n - w + 1, w)</code> 的上界寫錯</strong> —— "
       "最後一塊的起點最多是 <code>n − w</code>。",
     ]),
   ], "O(n·w)", "O(m·w)", "w 組 × 每組 O(n)", "兩個 Counter", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "m=5000 時", "好寫程度"],
   [["一、枚舉起點", "O(n·m·w)", "O(m·w)", "慢但通常能過", "★★★★☆"],
    ["二、分組滑動視窗", "O(n·w)", "O(m·w)", "快很多", "★★☆☆☆"]]),
 "edges": [
   "<strong><code>words</code> 有重複</strong>："
   "<code>(\"aaa\", [\"a\",\"a\"])</code> → <code>[0,1]</code>。用 set 會得到錯誤答案。",
   "<strong>整個 s 就是答案</strong>：<code>(\"a\", [\"a\"])</code> → <code>[0]</code>。",
   "<strong>沒有答案</strong>：<code>(\"ab\", [\"ba\"])</code> → <code>[]</code>。",
   "<strong>重疊的答案</strong>：<code>(\"barfoofoobarthefoobarman\", [\"bar\",\"foo\",\"the\"])</code> "
   "→ <code>[6,9,12]</code>。答案可以重疊，不能找到一個就跳過整段。",
   "<strong>s 比 total 短</strong>：<code>(\"a\", [\"ab\"])</code> → <code>[]</code>。"
   "<code>range(n - total + 1)</code> 會是空的。",
   "<strong>全部相同</strong>：<code>(\"aaaaaa\", [\"aa\",\"aa\",\"aa\"])</code> → <code>[0]</code>。",
   "<strong>單字長度 1</strong>：<code>w = 1</code> 時只有一組對齊，退化成一般的滑動視窗（第 438 題）。",
 ],
 "follow": [
   ("h", "追問一：如果單字長度不一樣呢？"),
   "<strong>整個解法都崩潰了。</strong>「按 w 切塊」不成立，滑動視窗也不成立。"
   "這時候要用 Trie + 回溯（每個位置試所有可能的單字長度），"
   "複雜度會變得很差。<strong>「等長」這個條件價值連城。</strong>",
   ("h", "追問二：如果只要求「包含」而不要求「恰好」呢？"),
   "那就退化成第 76 題（Minimum Window Substring）的變形 —— "
   "不需要分組，因為不要求對齊。",
   ("h", "追問三：這題和第 438 題（Find All Anagrams）的關係？"),
   ("c", """第 438 題：s 裡所有「p 的字母重排」的起點
          = 本題在 w = 1 的特例
          （每個「單字」就是一個字元）

所以：
    w = 1  ->  只有一組對齊，就是標準滑動視窗
    w > 1  ->  要分成 w 組

先把第 438 題寫熟，這題就只是「多包一層 offset 迴圈」。
反過來先攻這題會事倍功半。"""),
 ],
 "related": [
   "<strong>第 438 題 Find All Anagrams in a String</strong> —— w = 1 的特例，建議先練",
   "<strong>第 76 題 Minimum Window Substring</strong> —— 滑動視窗 + Counter 的經典",
   "<strong>第 567 題 Permutation in String</strong> —— 固定長度的滑動視窗",
 ],
 "check": [
   "為什麼要用 <code>Counter</code> 而不是 <code>set</code>？舉一個會出錯的輸入。",
   "為什麼滑動視窗要分成 <code>w</code> 組？如果只跑一組會漏掉什麼？",
   "情況 A（切出來不是單字）為什麼可以把整個視窗清空，而不是只吐一塊？",
   "找到答案（<code>count == m</code>）之後為什麼一定要吐掉最左邊一塊？",
 ],
})
print("P30 written")
