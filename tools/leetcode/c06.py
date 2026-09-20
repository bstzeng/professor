# -*- coding: utf-8 -*-
"""第 6–9 題。"""
import random, re
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(6)
INT_MIN, INT_MAX = -2**31, 2**31 - 1

# ==================== 6. Zigzag Conversion ====================
S["p6_sim"] = '''class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:            # 沒有這行會除以零／無限迴圈
            return s

        rows = [[] for _ in range(numRows)]
        r, step = 0, 1              # step = +1 往下，-1 往上

        for ch in s:
            rows[r].append(ch)
            if r == 0:
                step = 1            # 撞到頂，轉成往下
            elif r == numRows - 1:
                step = -1           # 撞到底，轉成往上
            r += step

        return "".join("".join(row) for row in rows)'''

S["p6_formula"] = '''class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = len(s)
        cycle = 2 * numRows - 2     # 一個「往下 + 斜上」的完整週期
        out = []

        for r in range(numRows):
            for base in range(r, n, cycle):
                out.append(s[base])                 # 垂直段上的字元

                second = base + cycle - 2 * r       # 同一週期裡斜線上的字元
                if r != 0 and r != numRows - 1 and second < n:
                    out.append(s[second])

        return "".join(out)'''

_p6a, _p6b = S.load("p6_sim"), S.load("p6_formula")
for s, r in [("PAYPALISHIRING", 3), ("PAYPALISHIRING", 4), ("A", 1), ("AB", 1), ("ABC", 5)]:
    assert _p6a.convert(s, r) == _p6b.convert(s, r), ("P6", s, r)
assert _p6a.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert _p6a.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
for _ in range(3000):
    s = "".join(random.choice("ABCDEFG") for _ in range(random.randint(1, 20)))
    r = random.randint(1, 6)
    assert _p6a.convert(s, r) == _p6b.convert(s, r), ("P6", s, r)
print("P6 solutions OK")

_P6_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">s = &quot;PAYPALISHIRING&quot;，numRows = 4</text>
            <g font-size="14" font-family="monospace">
              <text x="30" y="56" fill="var(--text-muted)" font-size="11">row 0</text>
              <text x="90" y="56" fill="var(--accent)">P</text>
              <text x="234" y="56" fill="var(--accent)">I</text>
              <text x="378" y="56" fill="var(--accent)">N</text>
              <text x="30" y="92" fill="var(--text-muted)" font-size="11">row 1</text>
              <text x="90" y="92" fill="var(--gold)">A</text>
              <text x="186" y="92" fill="#ff8a65">L</text>
              <text x="234" y="92" fill="var(--gold)">S</text>
              <text x="330" y="92" fill="#ff8a65">I</text>
              <text x="378" y="92" fill="var(--gold)">G</text>
              <text x="30" y="128" fill="var(--text-muted)" font-size="11">row 2</text>
              <text x="90" y="128" fill="var(--gold)">Y</text>
              <text x="138" y="128" fill="#ff8a65">A</text>
              <text x="234" y="128" fill="var(--gold)">H</text>
              <text x="282" y="128" fill="#ff8a65">R</text>
              <text x="30" y="164" fill="var(--text-muted)" font-size="11">row 3</text>
              <text x="90" y="164" fill="var(--accent)">P</text>
              <text x="234" y="164" fill="var(--accent)">I</text>
            </g>
            <text x="90" y="192" fill="var(--text-muted)" font-size="11" text-anchor="middle">週期 0</text>
            <text x="234" y="192" fill="var(--text-muted)" font-size="11" text-anchor="middle">週期 1</text>
            <text x="378" y="192" fill="var(--text-muted)" font-size="11" text-anchor="middle">週期 2</text>
            <line x1="162" y1="34" x2="162" y2="176" stroke="var(--border)" stroke-dasharray="3 4"/>
            <line x1="306" y1="34" x2="306" y2="176" stroke="var(--border)" stroke-dasharray="3 4"/>
            <text x="440" y="56" fill="var(--accent)" font-size="11">藍：垂直段（每週期 numRows 個）</text>
            <text x="440" y="76" fill="#ff8a65" font-size="11">橘：斜線段（每週期 numRows−2 個）</text>
            <text x="20" y="224" fill="var(--gold)" font-size="12">cycle = 2 × 4 − 2 = 6 → 每 6 個字元重複一次形狀</text>
            <text x="20" y="246" fill="var(--text-muted)" font-size="12">輸出＝逐列讀出：PIN + ALSIG + YAHR + PI = &quot;PINALSIGYAHRPI&quot;</text>'''

emit({
 "num": 6, "slug": "zigzag-conversion",
 "en": [
   "The string <code>\"PAYPALISHIRING\"</code> is written in a zigzag pattern on a given "
   "number of rows like this:",
   "<code>P&nbsp;&nbsp;&nbsp;A&nbsp;&nbsp;&nbsp;H&nbsp;&nbsp;&nbsp;N</code><br>"
   "<code>A&nbsp;P&nbsp;L&nbsp;S&nbsp;I&nbsp;I&nbsp;G</code><br>"
   "<code>Y&nbsp;&nbsp;&nbsp;I&nbsp;&nbsp;&nbsp;R</code>",
   "And then read line by line: <code>\"PAHNAPLSIIGYIR\"</code>.",
   "Write the code that will take a string and make this conversion given a number of rows.",
 ],
 "zh": [
   "把字串 <code>\"PAYPALISHIRING\"</code> 以 Z 字形（之字形）寫在指定的列數上，例如 3 列時長這樣：",
   "<code>P&nbsp;&nbsp;&nbsp;A&nbsp;&nbsp;&nbsp;H&nbsp;&nbsp;&nbsp;N</code><br>"
   "<code>A&nbsp;P&nbsp;L&nbsp;S&nbsp;I&nbsp;I&nbsp;G</code><br>"
   "<code>Y&nbsp;&nbsp;&nbsp;I&nbsp;&nbsp;&nbsp;R</code>",
   "然後<strong>一列一列</strong>讀出來，得到 <code>\"PAHNAPLSIIGYIR\"</code>。",
   "請實作這個轉換：給定字串與列數，回傳轉換後的結果。",
 ],
 "pre": [
   ("note", "這題唯一的難點是「看懂題目」", [
     "Z 字形的走法是：<strong>先由上往下走滿一整列，再斜著往右上走回第 0 列</strong>，如此重複。"
     "不是「橫著寫再折」，也不是矩陣旋轉。",
     ("c", """numRows = 4 時字元的落點（數字是在原字串裡的索引）

row 0 :  0           6            12
row 1 :  1     5     7     11     13
row 2 :  2  4        8  10
row 3 :  3           9

看索引就清楚了：
  0→1→2→3 往下，  3→4→5 斜上（跳過 row 3 和 row 0 本身），
  6→7→8→9 再往下…  每 6 個一循環。"""),
     "<strong>注意：輸出裡完全沒有空白。</strong>上面那張圖的空格只是為了畫出形狀，"
     "實際輸出只是把每一列的字元接起來。很多人第一次寫會真的去建一個二維字元矩陣填空白 —— "
     "那不但沒必要，還會在 <code>numRows</code> 很大時浪費大量記憶體。",
   ]),
 ],
 "examples": """範例 1
  輸入：s = "PAYPALISHIRING", numRows = 3
  輸出："PAHNAPLSIIGYIR"

範例 2
  輸入：s = "PAYPALISHIRING", numRows = 4
  輸出："PINALSIGYAHRPI"
  說明：
      P     I     N
      A   L S   I G
      Y A   H R
      P     I

範例 3
  輸入：s = "A", numRows = 1
  輸出："A\"""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 1000",
   "<code>s</code> 由英文字母（大小寫）、<code>','</code> 和 <code>'.'</code> 組成",
   "1 ≤ <code>numRows</code> ≤ 1000（<strong>可以大於 <code>s.length</code></strong>）",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong><code>numRows == 1</code> 一定要單獨處理。</strong>"
       "此時 <code>cycle = 2·1 − 2 = 0</code>，<code>range(r, n, 0)</code> 會直接丟 "
       "<code>ValueError: range() arg 3 must not be zero</code>；模擬法則會卡在同一列無限迴圈。"
       "這是本題最常見的 runtime error。",
       "<strong><code>numRows</code> 可以大於字串長度。</strong>"
       "例如 <code>s = \"ABC\"</code>、<code>numRows = 5</code>：根本折不回來，"
       "答案就是原字串 <code>\"ABC\"</code>。後面幾列是空的，不能輸出空白。",
       "n ≤ 1000，所以 O(n) 或 O(n · numRows) 都過得了。這題考的不是效率，是<strong>索引推導</strong>。",
     ]),
   ]),
 ],
 "idea": [
   "兩條路：<strong>老實模擬走法</strong>，或是<strong>推出每一列有哪些索引的公式</strong>。"
   "模擬法好寫好debug，公式法省空間又能展示你真的看懂了結構。面試時兩個都值得講。",
   ("fig", _P6_FIG, "0 0 640 262"),
 ],
 "approaches": [
   ap("解法一", "模擬：一個指標在列之間上下彈", [
     "想像有一顆球在第 0 列和第 numRows−1 列之間彈來彈去，每讀一個字元就把它丟進當前那一列的桶子裡。",
     ("c", """s = "PAYPALISHIRING", numRows = 4

字元  P  A  Y  P  A  L  I  S  H  I  R  I  N  G
row   0  1  2  3  2  1  0  1  2  3  2  1  0  1
step  +1 +1 +1 -1 -1 -1 +1 +1 +1 -1 -1 -1 +1 +1
         ↑ 撞到 row 3 → step 翻成 -1
                     ↑ 撞到 row 0 → step 翻成 +1

桶子：
  row 0 = [P, I, N]
  row 1 = [A, L, S, I, G]
  row 2 = [Y, A, H, R]
  row 3 = [P, I]"""),
     ("c", S["p6_sim"]),
     ("h", "為什麼判斷方向要放在 append 之後？"),
     "因為我們要的是「<strong>放好這個字元之後，下一步往哪走</strong>」。"
     "如果先改方向再 append，第一個字元就會被放到 row 1 而不是 row 0。"
     "順序是：<strong>放 → 決定方向 → 移動</strong>。",
     ("h", "為什麼用 <code>if r == 0 / elif r == numRows-1</code> 而不是 <code>if r == numRows-1 / elif r == 0</code>？"),
     "在 <code>numRows &gt;= 2</code> 時兩種寫法都對（0 和 numRows−1 不可能同時成立）。"
     "但如果沒有擋 <code>numRows == 1</code>，此時 <code>0 == numRows-1</code>，"
     "兩種寫法會走不同分支、都會壞掉 —— 所以真正的保險還是最上面那個提前 return。",
     "<strong>為什麼用 list of list 而不是字串相加？</strong>"
     "Python 的字串是不可變的，<code>rows[r] += ch</code> 每次都會複製整條字串，"
     "最壞情況變成 O(n²)。用 list append 再一次 join 是 Python 的標準做法。",
   ], "O(n)", "O(n)", "每個字元剛好被處理一次", "桶子總共存 n 個字元"),

   ap("解法二", "直接算出每一列的索引（不建桶子）", [
     "既然形狀每 <code>cycle = 2·numRows − 2</code> 個字元重複一次，"
     "就可以直接算出「第 r 列有哪些索引」，一列一列直接輸出，連桶子都不用。",
     ("h", "推導"),
     ("c", """設 cycle = 2 * numRows - 2  （往下 numRows 步 + 斜上 numRows-2 步）

第 r 列在第 k 個週期裡，最多有兩個字元：

  (A) 垂直段上的：   base = k * cycle + r
  (B) 斜線段上的：   second = k * cycle + (cycle - r)
                           = base + cycle - 2*r

  驗證 (B)：一個週期的字元索引是 base0 .. base0+cycle-1，
  走法是 row 0,1,...,numRows-1,numRows-2,...,1。
  往下時 row r 對應偏移 r；
  往上時 row r 對應偏移 cycle - r。

首列 (r = 0) 和末列 (r = numRows-1) 只有 (A)：
  r = 0          → second = base + cycle，那已經是下一個週期的 (A) 了
  r = numRows-1  → second = base + cycle - 2*(numRows-1) = base，重複自己"""),
     ("c", """numRows = 4，cycle = 6，s 長度 14

r = 0：base = 0, 6, 12                      → P I N
r = 1：base = 1  second = 1+6-2 = 5         → A L
       base = 7  second = 7+6-2 = 11        → S I
       base = 13 second = 17 ≥ 14，跳過      → G
r = 2：base = 2  second = 2+6-4 = 4         → Y A
       base = 8  second = 10                → H R
r = 3：base = 3, 9                          → P I

接起來：PIN + ALSIG + YAHR + PI = "PINALSIGYAHRPI" ✔"""),
     ("c", S["p6_formula"]),
     "<code>if second &lt; n</code> 這個檢查不能省：最後一個週期通常是不完整的。",
     "<strong>這個解法的空間是 O(1)</strong>（不算輸出）。實務差別不大，"
     "但它證明你真的理解了 Z 字形的週期結構，而不只是會模擬 —— "
     "面試官常會在你寫完模擬法之後追問「有沒有辦法不用額外的桶子？」",
   ], "O(n)", "O(1)", "每個字元剛好輸出一次", "不算輸出的話只有幾個變數", optimal=True),
 ],
 "compare": (["解法", "時間", "額外空間", "好寫程度", "備註"],
   [["一、模擬彈跳", "O(n)", "O(n)", "★★★★★", "面試預設；不容易寫錯"],
    ["二、索引公式", "O(n)", "O(1)", "★★★☆☆", "推導清楚才寫，不然很容易差一"]]),
 "edges": [
   "<strong><code>numRows == 1</code></strong>：必須直接回傳 <code>s</code>。公式法會 <code>ValueError</code>，模擬法會無限迴圈。",
   "<strong><code>numRows &gt;= len(s)</code></strong>：<code>(\"ABC\", 5)</code> → <code>\"ABC\"</code>。折不回來，後面幾列是空的。",
   "<strong><code>numRows == 2</code></strong>：<code>cycle = 2</code>，沒有斜線段，等於奇偶分離。是公式法的邊界。",
   "<strong>長度剛好整除 cycle</strong> 和<strong>剛好差 1</strong>：最後一個週期完不完整，走的是不同分支。",
   "<strong>單一字元</strong>：<code>(\"A\", 1)</code>、<code>(\"A\", 3)</code> 都要回 <code>\"A\"</code>。",
 ],
 "follow": [
   ("h", "追問一：如果要反過來，從 Z 字形結果還原原字串呢？"),
   "先用同一套公式算出「每一列有幾個字元」，就知道結果字串該怎麼切成 numRows 段；"
   "然後再跑一次彈跳模擬，這次是<strong>從各段的開頭依序取字元</strong>填回去。"
   "關鍵洞察：<strong>轉換是一個排列（permutation），排列一定可逆。</strong>",
   ("h", "追問二：字串長到放不進記憶體怎麼辦？"),
   "解法二天生就是串流友善的 —— 它按列輸出，每一列只需要對原字串做隨機存取（例如 mmap 或 seek）。"
   "解法一則必須把所有桶子同時放在記憶體裡。這又是一次「複雜度相同、存取模式不同」的取捨。",
   ("h", "追問三：為什麼 <code>cycle</code> 是 <code>2·numRows − 2</code> 而不是 <code>2·numRows</code>？"),
   "因為轉折點（第 0 列和最後一列）<strong>只會被走到一次，不會走兩次</strong>。"
   "往下 numRows 步，往上只有 numRows − 2 步（頭尾都已經算過了）。"
   "把這句話說清楚，通常就代表你真的懂這題了。",
 ],
 "related": [
   "<strong>第 48 題 Rotate Image</strong> —— 另一類「座標對應」題，同樣是先把索引關係寫對",
   "<strong>第 54／59 題 Spiral Matrix</strong> —— 模擬走法的經典題",
 ],
 "check": [
   "<code>numRows = 5</code> 時 cycle 是多少？第 2 列在第 0 個週期裡有哪兩個索引？",
   "把模擬法的「決定方向」搬到 <code>rows[r].append(ch)</code> 前面，輸出會變成什麼？",
   "為什麼公式法對 <code>r == numRows-1</code> 要排除 <code>second</code>？如果不排除會重複輸出什麼？",
   "如果題目改成「Z 字形之後<strong>逐行</strong>輸出、空格保留」，兩種解法各要改哪裡？",
 ],
})
print("P6 written")

# ==================== 7. Reverse Integer ====================
S["p7_str"] = '''class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        r = sign * int(str(abs(x))[::-1])

        return 0 if r < INT_MIN or r > INT_MAX else r'''

S["p7_digit"] = '''class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        r = 0

        while x:
            d = x % 10
            x //= 10

            # 事前檢查：如果 r*10 + d 會超過 INT_MAX，現在就收手
            # 寫成 r > (INT_MAX - d) // 10 可以完全避免溢位
            if r > (INT_MAX - d) // 10:
                return 0

            r = r * 10 + d

        r *= sign
        return 0 if r < INT_MIN or r > INT_MAX else r'''

_p7a, _p7b = S.load("p7_str"), S.load("p7_digit")
for x in [123, -123, 120, 0, 1534236469, -2147483648, 2147483647, 1463847412, -1463847412, -2147483412]:
    assert _p7a.reverse(x) == _p7b.reverse(x), ("P7", x, _p7a.reverse(x), _p7b.reverse(x))
assert _p7a.reverse(123) == 321 and _p7a.reverse(-123) == -321 and _p7a.reverse(120) == 21
assert _p7a.reverse(1534236469) == 0
for _ in range(6000):
    x = random.randint(INT_MIN, INT_MAX)
    assert _p7a.reverse(x) == _p7b.reverse(x), ("P7", x)
print("P7 solutions OK")

emit({
 "num": 7, "slug": "reverse-integer",
 "en": [
   "Given a signed 32-bit integer <code>x</code>, return <code>x</code> "
   "<em>with its digits reversed</em>. If reversing <code>x</code> causes the value to go "
   "outside the signed 32-bit integer range <code>[-2³¹, 2³¹ - 1]</code>, then return <code>0</code>.",
   "<strong>Assume the environment does not allow you to store 64-bit integers "
   "(signed or unsigned).</strong>",
 ],
 "zh": [
   "給你一個 32 位元的有號整數 <code>x</code>，請把它的<strong>每一位數字反轉</strong>後回傳。"
   "如果反轉後的結果超出 32 位元有號整數的範圍 <code>[-2³¹, 2³¹ − 1]</code>，就回傳 <code>0</code>。",
   "<strong>假設執行環境不允許你存 64 位元整數（不論有號無號）。</strong>",
 ],
 "pre": [
   ("note", "這題的真正考點是溢位，不是反轉", [
     "反轉本身在 Python 裡是一行：<code>int(str(abs(x))[::-1])</code>。"
     "題目真正想考的是那句「<strong>不准用 64 位元整數</strong>」。",
     ("c", """INT_MAX = 2147483647   （2³¹ − 1，10 位數）
INT_MIN = -2147483648  （−2³¹）

x = 1534236469  → 反轉是 9646324351 → 超過 INT_MAX → 回傳 0
x = 1463847412  → 反轉是 2147483641 → 剛好在範圍內 → 回傳 2147483641

注意 INT_MIN 的絕對值比 INT_MAX 大 1：
  -(-2147483648) = 2147483648 > INT_MAX
  在 C / Java 裡 abs(INT_MIN) 本身就會溢位！"""),
     "<strong>Python 的整數是任意精度的，所以你在 Python 裡「感覺不到」這個問題。</strong>"
     "但面試官問的是：如果是 C 或 Java，你會怎麼寫？下面解法二就是那個答案。",
   ]),
 ],
 "examples": """範例 1
  輸入：x = 123
  輸出：321

範例 2
  輸入：x = -123
  輸出：-321
  說明：負號留在原地，只反轉數字部分。

範例 3
  輸入：x = 120
  輸出：21
  說明：反轉後的前導零要去掉（021 → 21）。

範例 4
  輸入：x = 1534236469
  輸出：0
  說明：反轉後是 9646324351，超出 32 位元範圍。""",
 "constraints": [
   "−2³¹ ≤ <code>x</code> ≤ 2³¹ − 1，也就是 −2147483648 ≤ <code>x</code> ≤ 2147483647",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>輸入保證在範圍內，輸出不保證。</strong>要檢查的是結果，不是輸入。",
       "<strong><code>x = -2147483648</code>（INT_MIN）是必考測資。</strong>"
       "在 C/Java 裡 <code>-x</code> 或 <code>abs(x)</code> 都會溢位；"
       "而它反轉後是 8463847412，遠超範圍，答案是 0。",
       "<strong>前導零自動消失。</strong>120 → 021 → 21。"
       "用 <code>int()</code> 轉換會自動處理；用逐位算的方法也會自動處理（開頭的 0 乘進去等於沒乘）。",
       "<strong><code>x = 0</code></strong> → 0。逐位法的 while 迴圈一次都不會跑，剛好回傳初值 0。",
     ]),
   ]),
 ],
 "idea": [
   "兩個層次：<strong>Python 的寫法</strong>（能過、三行）和 <strong>C/Java 的寫法</strong>"
   "（面試官真正想看的溢位處理）。建議兩個都準備。",
 ],
 "approaches": [
   ap("解法一", "字串反轉（Python 的作弊寫法）", [
     ("c", S["p7_str"]),
     ("h", "為什麼要先取 abs 再反轉？"),
     "因為 <code>str(-123)</code> 是 <code>\"-123\"</code>，"
     "直接 <code>[::-1]</code> 會變成 <code>\"321-\"</code>，<code>int()</code> 會拋例外。"
     "先把符號拆出來、只反轉數字部分，最後再乘回去，是最乾淨的做法。",
     "<strong>這個解法在 LeetCode 上會過。</strong>但如果面試官說「假設不能用字串轉換」"
     "或「假設是 32 位元環境」，它就完全不成立了 —— 它靠的正是 Python 的任意精度整數。",
   ], "O(log x)", "O(log x)", "位數是 log₁₀x，最多 10 位", "字串本身"),

   ap("解法二", "逐位取出，並在溢位「之前」就攔下來", [
     "標準做法：不斷 <code>% 10</code> 取最低位、<code>// 10</code> 砍掉它，把取出的位數往結果的左邊推。",
     ("c", """x = 123

輪 1： d = 123 % 10 = 3    x = 12     r = 0*10 + 3 = 3
輪 2： d = 12 % 10  = 2    x = 1      r = 3*10 + 2 = 32
輪 3： d = 1 % 10   = 1    x = 0      r = 32*10 + 1 = 321
x 變成 0，結束 → 321"""),
     ("h", "關鍵：怎麼在「不能用更大的型別」的前提下判斷溢位？"),
     "直覺會想寫 <code>if r * 10 + d &gt; INT_MAX</code> —— "
     "但在 C/Java 裡，<code>r * 10 + d</code> <strong>這個算式本身就已經溢位了</strong>，"
     "算出來的值是環繞後的垃圾，拿它去比較毫無意義。",
     "解法是把不等式<strong>移項</strong>，讓兩邊都不會超過範圍：",
     ("c", """想判斷：      r * 10 + d  >  INT_MAX
移項：        r * 10      >  INT_MAX - d
              r           >  (INT_MAX - d) / 10

因為 r 和 d 都是整數，且 d ∈ [0, 9]：
              r > (INT_MAX - d) // 10        ← 這一行永遠不會溢位

左邊的 r 是現有的合法值，
右邊 (INT_MAX - d) // 10 最大是 214748364，也是合法值。
兩個合法值比大小，安全。"""),
     ("c", S["p7_digit"]),
     ("h", "常見的簡化寫法（以及它為什麼也對）"),
     ("c", """很多題解寫成：
    if r > INT_MAX // 10 or (r == INT_MAX // 10 and d > 7):
        return 0

INT_MAX // 10 = 214748364，INT_MAX % 10 = 7

  r > 214748364            → r*10 一定超過 → 溢位
  r == 214748364 且 d > 7  → 214748364*10 + d = 2147483640 + d > 2147483647 → 溢位
  其他情況                  → 安全

兩種寫法等價。移項版比較短，分case 版比較好讀，
但分case 版要記住那個「7」是哪來的（就是 INT_MAX 的個位數）。"""),
     ("h", "負數怎麼辦？"),
     "這裡先取 <code>abs(x)</code>、全部用正數算、最後乘回符號，所以只要檢查上界。"
     "在 C 裡不能這樣做（<code>abs(INT_MIN)</code> 會溢位），"
     "標準 C 寫法是<strong>全程用負數算</strong>、只檢查下界 <code>INT_MIN</code>，"
     "因為負數那一側的範圍比較大，不會漏掉任何合法值。"
     "如果面試考的是 C，值得把這點講出來。",
   ], "O(log x)", "O(1)", "最多 10 次迴圈", "只有幾個整數變數", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "32 位元環境可用？", "備註"],
   [["一、字串反轉", "O(log x)", "O(log x)", "✘ 靠 Python 大整數", "最短，LeetCode 上能過"],
    ["二、逐位 + 事前檢查", "O(log x)", "O(1)", "✔", "面試標準答案"]]),
 "edges": [
   "<strong><code>x = 0</code></strong> → 0。while 迴圈跑 0 次。",
   "<strong><code>x = -2147483648</code>（INT_MIN）</strong> → 0。C/Java 裡 <code>abs</code> 會溢位，必須小心。",
   "<strong><code>x = 1463847412</code></strong> → 2147483641。<strong>剛好沒溢位</strong>，用來驗證你的判斷式沒有多擋。",
   "<strong><code>x = 1534236469</code></strong> → 0。<strong>剛好溢位</strong>，用來驗證你的判斷式沒有漏擋。",
   "<strong>結尾是 0</strong>：<code>120 → 21</code>、<code>1000 → 1</code>。",
   "<strong>單一位數</strong>：<code>7 → 7</code>、<code>-7 → -7</code>。",
 ],
 "follow": [
   ("h", "追問一：如果不准用取模和除法呢？"),
   "只能走字串／字元陣列的路：把數字一位一位印成字元、反轉、再手動累加回去。"
   "但累加時同樣要做溢位檢查，判斷式完全一樣。",
   ("h", "追問二：反轉 64 位元整數呢？"),
   "邏輯一模一樣，把 <code>INT_MAX</code> 換成 <code>2**63 - 1</code> 即可。"
   "重點是：<strong>「事前檢查」這個模式與位元寬度無關</strong>，這才是這題真正要你帶走的東西。",
   ("h", "追問三：為什麼不能寫 <code>try: ... except OverflowError</code>？"),
   "Python 的整數運算根本不會丟 <code>OverflowError</code>（它會自動變大整數）。"
   "而 C/Java 的有號整數溢位是 undefined behavior 或靜默環繞，也不會有例外可以接。"
   "<strong>溢位必須主動預防，不能被動捕捉</strong> —— 這是系統程式設計的基本功。",
 ],
 "related": [
   "<strong>第 8 題 String to Integer (atoi)</strong> —— 同一套溢位檢查，包在字串解析裡",
   "<strong>第 9 題 Palindrome Number</strong> —— 用一樣的逐位技巧，但只反轉一半",
   "<strong>第 66 題 Plus One</strong> —— 陣列形式的進位處理",
 ],
 "check": [
   "<code>(INT_MAX - d) // 10</code> 的最大可能值是多少？為什麼它保證不會溢位？",
   "如果把檢查寫成 <code>if r * 10 + d &gt; INT_MAX</code>，在 Python 裡會對嗎？在 Java 裡呢？為什麼不一樣？",
   "找出一個「反轉後剛好等於 INT_MAX」的輸入，並確認你的程式回傳它而不是 0。",
   "在 C 裡如果全程用負數累加，判斷式要怎麼寫？為什麼那樣比較安全？",
 ],
})
print("P7 written")
