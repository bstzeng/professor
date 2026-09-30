# -*- coding: utf-8 -*-
"""第 201–206 題。"""
import random
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(201)


# ==================== 201. Bitwise AND of Numbers Range ====================
S["p201_shift"] = '''class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:          # ★ 兩者不同，代表最低位一定會出現 0
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift         # 共同前綴補回右邊的 0'''

S["p201_bk"] = '''class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while left < right:
            right &= right - 1       # ★ 拿掉 right 最低位的 1
        return right'''

S["p201_brute"] = '''class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = left
        for x in range(left + 1, right + 1):
            ans &= x
            if ans == 0:             # 小優化：已經是 0 就不會再變
                break
        return ans'''

_p201 = [S.load(k) for k in ("p201_shift", "p201_bk", "p201_brute")]


def _p201_ref(a, b):
    r = a
    for x in range(a, b + 1):
        r &= x
    return r


for a, b, want in [(5, 7, 4), (0, 0, 0), (1, 2147483647, 0), (12, 15, 12), (26, 30, 24),
                   (6, 6, 6), (2147483646, 2147483647, 2147483646)]:
    for sol in _p201:
        got = sol.rangeBitwiseAnd(a, b)
        assert got == want, ("P201", a, b, want, got, sol)
for _ in range(3000):
    a = random.randrange(0, 600)
    b = a + random.randrange(0, 300)
    want = _p201_ref(a, b)
    for sol in _p201:
        assert sol.rangeBitwiseAnd(a, b) == want, ("P201 rand", a, b)
print("P201 OK")

_P201_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">left = 26、right = 30：把區間內所有數字的二進位疊起來看</text>
            <g font-family="ui-monospace,Menlo,Consolas,monospace" font-size="15">
              <text x="40" y="58" fill="var(--text)">26 = </text><text x="110" y="58"><tspan fill="var(--accent)">11</tspan><tspan fill="var(--text)">010</tspan></text>
              <text x="40" y="84" fill="var(--text)">27 = </text><text x="110" y="84"><tspan fill="var(--accent)">11</tspan><tspan fill="var(--text)">011</tspan></text>
              <text x="40" y="110" fill="var(--text)">28 = </text><text x="110" y="110"><tspan fill="var(--accent)">11</tspan><tspan fill="var(--text)">100</tspan></text>
              <text x="40" y="136" fill="var(--text)">29 = </text><text x="110" y="136"><tspan fill="var(--accent)">11</tspan><tspan fill="var(--text)">101</tspan></text>
              <text x="40" y="162" fill="var(--text)">30 = </text><text x="110" y="162"><tspan fill="var(--accent)">11</tspan><tspan fill="var(--text)">110</tspan></text>
              <text x="40" y="198" fill="var(--gold)">AND = </text><text x="110" y="198"><tspan fill="var(--accent)">11</tspan><tspan fill="var(--gold)">000</tspan><tspan fill="var(--text-muted)" font-size="12">  = 24</tspan></text>
            </g>
            <line x1="30" y1="176" x2="260" y2="176" stroke="var(--border)"/>
            <text x="300" y="70" fill="var(--accent)" font-size="12">★ 共同前綴「11」：區間內每個數都一樣 → 保留</text>
            <text x="300" y="100" fill="var(--text)" font-size="12">共同前綴之後的第一個位元，</text>
            <text x="300" y="122" fill="var(--text)" font-size="12">left 是 0、right 是 1 —— 從 0 爬到 1 的途中，</text>
            <text x="300" y="144" fill="var(--text)" font-size="12">一定經過「那一位是 1、後面全是 0」的數，</text>
            <text x="300" y="166" fill="var(--text)" font-size="12">和它前一個數 AND 起來，後面的位全部歸零。</text>
            <text x="300" y="198" fill="var(--gold)" font-size="12">答案 = 共同前綴，後面補 0</text>'''

emit({
 "num": 201, "slug": "bitwise-and-of-numbers-range",
 "en": [
   "You are given two integers <code>left</code> and <code>right</code> that describe the "
   "inclusive range <code>[left, right]</code>. Return the result of applying bitwise AND to "
   "every integer in that range.",
 ],
 "zh": [
   "給你兩個整數 <code>left</code> 和 <code>right</code>，代表閉區間 <code>[left, right]</code>。"
   "請回傳把區間內<strong>所有整數做位元 AND</strong> 之後的結果。",
 ],
 "pre": [
   ("note", "★ 這題的陷阱：直接迴圈會超時", [
     ("c", """區間最長可以是 [0, 2^31 - 1]，大約 21 億個數字。

    一個一個 AND 下去 -> 最多 21 億次運算 ✘

【真正要問的是】：
    AND 一路做下去，哪些位元能活下來？

【答案】：
    只有 left 和 right 的「共同二進位前綴」能活下來，
    其餘位元一定都變成 0。

所以這題不是迴圈題，是【找共同前綴】的題目。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：left = 5, right = 7
  輸出：4
  說明：5 = 101、6 = 110、7 = 111，全部 AND 起來是 100 = 4。

範例 2
  輸入：left = 0, right = 0
  輸出：0

範例 3
  輸入：left = 1, right = 2147483647
  輸出：0""",
 "constraints": [
   "0 ≤ <code>left</code> ≤ <code>right</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("fig", _P201_FIG, "0 0 640 220"),
   ("c", """【為什麼共同前綴之後的位元全部會變 0？】

    假設 left 和 right 的共同前綴是 P，
    在 P 之後的第一個位置上：
        left  的那一位是 0
        right 的那一位是 1
    （因為 left ≤ right，而且這是第一個不同的位）

    從 left 數到 right 的途中，一定會經過這個數：
        M = P 1 000...0     （那一位是 1，後面全 0）
    以及它的前一個數：
        M - 1 = P 0 111...1

    這兩個數 AND 起來：
        P 1 000...0
      & P 0 111...1
      = P 0 000...0

    【從那一位開始到最右邊，全部都被清成 0 了】
    而共同前綴 P 在區間內每個數都一樣，所以保留。

【結論】：
    答案 = left 和 right 的共同前綴，後面補 0 ✔

【怎麼找共同前綴？】兩種常見寫法：
    1. 兩者一起右移，直到相等；再左移回去。
    2. 不斷把 right 最低位的 1 拿掉，直到 right ≤ left。"""),
 ],
 "approaches": [
   ap("解法一", "暴力 AND（會超時，但有助理解）", [
     ("c", S["p201_brute"]),
     "<strong>最壞情況 21 億次迴圈</strong>——即使加了「變成 0 就提早結束」的優化，"
     "像 <code>left = 2³⁰, right = 2³¹ − 1</code> 這種區間，答案是 <code>2³⁰</code> 從不變 0，"
     "還是要跑完十億次。",
   ], "O(right − left)", "O(1)", "區間長度", ""),

   ap("解法二", "同步右移找共同前綴", [
     ("c", S["p201_shift"]),
     ("c", """【模擬】left = 26 (11010)、right = 30 (11110)

    shift = 0：11010 vs 11110  不同
    shift = 1： 1101 vs  1111  不同
    shift = 2：  110 vs   111  不同
    shift = 3：   11 vs    11  相同 -> 停

    答案 = 11 << 3 = 11000 = 24 ✔

【迴圈最多跑幾次？】
    每次右移一位，最多 31 位 -> O(log right) ✔"""),
   ], "O(log right)", "O(1)", "最多 31 次右移", "", optimal=True),

   ap("解法三", "Brian Kernighan：一直拿掉最低位的 1", [
     ("c", S["p201_bk"]),
     ("c", """【right & (right - 1) 做了什麼？】

    right     = 1 1 1 1 0
    right - 1 = 1 1 1 0 1
    AND       = 1 1 1 0 0   <- 最低位的 1 被拿掉了

【為什麼可以這樣做？】
    只要 right > left，right 的最低位的 1
    一定不在共同前綴裡（否則 right 就會 ≤ left），
    所以它在答案裡一定是 0，可以直接拿掉。

    一直拿到 right ≤ left 為止，剩下的就是共同前綴 ✔

【模擬】left = 26、right = 30
    30 = 11110 -> 11100 = 28   仍 > 26
    28 = 11100 -> 11000 = 24   ≤ 26，停
    答案 24 ✔

【注意回傳 right 而不是 left】
    迴圈結束時 right ≤ left，right 才是被清乾淨的共同前綴。"""),
   ], "O(log right)", "O(1)", "迴圈次數 = 要拿掉的 1 的個數", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、暴力", "O(right − left)", "O(1)", "區間大時超時 ✘"],
    ["二、同步右移", "O(log right)", "O(1)", "最直觀 ✔"],
    ["三、Brian Kernighan", "O(log right)", "O(1)", "通常迴圈次數更少"]]),
 "edges": [
   "<strong><code>left == right</code></strong> → 答案就是它本身。",
   "<strong><code>left = 0</code></strong> → 任何數 AND 0 都是 0。",
   "<strong>區間跨過 2 的冪次</strong>（例如 <code>[3, 4]</code>）→ 最高位不同，答案是 0。",
   "<strong>最大值 <code>2³¹ − 1</code></strong> → Python 沒有溢位問題；其他語言要注意 <code>right - 1</code> 不會溢位，但別寫成 <code>right + 1</code>。",
   "<strong>解法三回傳 <code>left</code></strong> → 錯，要回傳 <code>right</code>。",
 ],
 "follow": [
   ("h", "追問一：如果改成 OR 呢？"),
   ("c", """【區間 OR】剛好反過來：

    共同前綴保留，
    共同前綴之後的位元，全部變成 1。

    理由相同：區間內一定有 P 0 111...1 這個數，
    它把後面所有位都填成 1。

    def rangeBitwiseOr(left, right):
        shift = 0
        while left < right:
            left >>= 1; right >>= 1; shift += 1
        return (left << shift) | ((1 << shift) - 1) if shift else left"""),
   ("h", "追問二：同樣的「最低位的 1」技巧還能做什麼？"),
   ("ul", [
     "<strong>第 191 題 位元 1 的個數</strong>：<code>n &amp;= n - 1</code> 每次拿掉一個 1，計數即可。",
     "<strong>第 231 題 2 的冪</strong>：<code>n &gt; 0 and n &amp; (n - 1) == 0</code>。",
     "<strong>第 338 題 位元計數</strong>：<code>bits[i] = bits[i &amp; (i - 1)] + 1</code>。",
   ]),
 ],
 "related": [
   "<strong>第 191 題 位元 1 的個數</strong> —— Brian Kernighan 技巧",
   "<strong>第 231 題 2 的冪</strong> —— <code>n &amp; (n - 1)</code>",
   "<strong>第 338 題 位元計數</strong> —— 同樣的技巧用在 DP",
 ],
 "check": [
   "為什麼答案只由 <code>left</code> 和 <code>right</code> 的共同前綴決定？",
   "共同前綴之後的位元，為什麼一定會被某一對相鄰數字清成 0？",
   "<code>n &amp; (n - 1)</code> 做了什麼事？",
   "解法三為什麼要回傳 <code>right</code>？",
 ],
})


# ==================== 202. Happy Number ====================
S["p202_set"] = '''class Solution:
    def isHappy(self, n: int) -> bool:
        def nxt(x: int) -> int:
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s

        seen = set()
        while n != 1 and n not in seen:   # ★ 重複出現 = 進入循環
            seen.add(n)
            n = nxt(n)
        return n == 1'''

S["p202_floyd"] = '''class Solution:
    def isHappy(self, n: int) -> bool:
        def nxt(x: int) -> int:
            s = 0
            while x:
                x, d = divmod(x, 10)
                s += d * d
            return s

        slow, fast = n, nxt(n)
        while fast != 1 and slow != fast:
            slow = nxt(slow)              # 走一步
            fast = nxt(nxt(fast))         # 走兩步
        return fast == 1'''

S["p202_math"] = '''class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = {4, 16, 37, 58, 89, 145, 42, 20}   # ★ 唯一的非 1 循環
        while n != 1 and n not in cycle:
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1'''

_p202 = [S.load(k) for k in ("p202_set", "p202_floyd", "p202_math")]


def _p202_ref(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1


for n, want in [(19, True), (2, False), (1, True), (7, True), (4, False), (100, True), (2147483647, False)]:
    for sol in _p202:
        assert sol.isHappy(n) == want, ("P202", n, sol)
for n in list(range(1, 3000)) + [random.randrange(1, 2 ** 31) for _ in range(2000)]:
    want = _p202_ref(n)
    for sol in _p202:
        assert sol.isHappy(n) == want, ("P202 rand", n)
print("P202 OK")

_P202_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">n = 2 的軌跡：掉進一個不含 1 的循環，永遠出不來</text>
            <g font-size="14" text-anchor="middle">
              <text x="50" y="70" fill="var(--text)">2</text>
              <text x="85" y="70" fill="var(--text-muted)">→</text>
              <circle cx="130" cy="65" r="20" fill="none" stroke="#ff8a65"/><text x="130" y="70" fill="#ff8a65">4</text>
              <circle cx="220" cy="65" r="20" fill="none" stroke="#ff8a65"/><text x="220" y="70" fill="#ff8a65">16</text>
              <circle cx="310" cy="65" r="20" fill="none" stroke="#ff8a65"/><text x="310" y="70" fill="#ff8a65">37</text>
              <circle cx="400" cy="65" r="20" fill="none" stroke="#ff8a65"/><text x="400" y="70" fill="#ff8a65">58</text>
              <circle cx="400" cy="150" r="20" fill="none" stroke="#ff8a65"/><text x="400" y="155" fill="#ff8a65">89</text>
              <circle cx="310" cy="150" r="20" fill="none" stroke="#ff8a65"/><text x="310" y="155" fill="#ff8a65">145</text>
              <circle cx="220" cy="150" r="20" fill="none" stroke="#ff8a65"/><text x="220" y="155" fill="#ff8a65">42</text>
              <circle cx="130" cy="150" r="20" fill="none" stroke="#ff8a65"/><text x="130" y="155" fill="#ff8a65">20</text>
            </g>
            <g stroke="var(--text-muted)" stroke-width="1.2">
              <line x1="150" y1="65" x2="198" y2="65"/><line x1="240" y1="65" x2="288" y2="65"/>
              <line x1="330" y1="65" x2="378" y2="65"/><line x1="400" y1="85" x2="400" y2="128"/>
              <line x1="380" y1="150" x2="332" y2="150"/><line x1="290" y1="150" x2="242" y2="150"/>
              <line x1="200" y1="150" x2="152" y2="150"/><line x1="130" y1="130" x2="130" y2="87"/>
            </g>
            <text x="460" y="80" fill="var(--text)" font-size="12">4² = 16</text>
            <text x="460" y="102" fill="var(--text)" font-size="12">1² + 6² = 37</text>
            <text x="460" y="124" fill="var(--text)" font-size="12">3² + 7² = 58 …</text>
            <text x="460" y="146" fill="var(--text)" font-size="12">2² + 0² = 4 ↺</text>
            <text x="20" y="200" fill="var(--accent)" font-size="12">★ 數學事實：任何不快樂的數，最後都會掉進這個 8 個數的循環。</text>
            <text x="20" y="222" fill="var(--text-muted)" font-size="12">所以「判斷快樂數」＝「判斷一條序列會走到 1，還是走進循環」＝ 鏈結串列找環（第 141 題）。</text>'''

emit({
 "num": 202, "slug": "happy-number",
 "en": [
   "Decide whether a positive integer <code>n</code> is <em>happy</em>.",
   "Starting from <code>n</code>, repeatedly replace the number with the sum of the squares of its "
   "decimal digits. If this process eventually reaches <code>1</code>, the number is happy. "
   "If it instead falls into a loop that never contains <code>1</code>, it is not happy.",
   "Return <code>true</code> if <code>n</code> is happy, otherwise <code>false</code>.",
 ],
 "zh": [
   "判斷正整數 <code>n</code> 是不是<strong>快樂數</strong>。",
   "從 <code>n</code> 開始，反覆把數字換成「<strong>它每一位數字的平方和</strong>」。"
   "如果最後能變成 <code>1</code>，它就是快樂數；如果掉進一個不含 <code>1</code> 的無限循環，就不是。",
   "是快樂數就回傳 <code>true</code>，否則回傳 <code>false</code>。",
 ],
 "examples": """範例 1
  輸入：n = 19
  輸出：true
  說明：1² + 9² = 82
        8² + 2² = 68
        6² + 8² = 100
        1² + 0² + 0² = 1

範例 2
  輸入：n = 2
  輸出：false
  說明：2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → …（循環）""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("fig", _P202_FIG, "0 0 640 236"),
   ("c", """【這個過程只有兩種結局】

    1. 走到 1（1 → 1 → 1 …，也是一種「循環」，但它是好的）
    2. 走進一個不含 1 的循環

【會不會無限變大、永遠不重複？】不會。

    一個 d 位數，它的「位數平方和」最多是 81 × d。
        10 位數 最多 81 × 10 = 810
    所以不管 n 多大，一步之後就掉到 810 以下，
    之後永遠在 [1, 810] 裡打轉。

    有限的範圍 + 確定性的規則 -> 一定會重複 -> 一定有循環 ✔

【所以問題變成】：
    「這條序列最後會停在 1，還是停在別的循環？」
    = 鏈結串列找環（第 141 題）的換皮版本。"""),
 ],
 "approaches": [
   ap("解法一", "雜湊集合記錄走過的數", [
     ("c", S["p202_set"]),
     ("c", """【為什麼用 divmod 而不是 str(n)？】

    兩者都可以。divmod 避免建立字串，
    在其他語言裡也是標準寫法。

【集合最多會存多少個數？】
    第一步之後就 ≤ 810，所以集合大小是常數等級。"""),
   ], "O(log n)", "O(log n)", "第一步處理 log n 位數，之後在常數範圍內", "集合大小有上界"),

   ap("解法二", "Floyd 快慢指標（O(1) 空間）", [
     ("c", S["p202_floyd"]),
     ("c", """【把 nxt() 想成鏈結串列的 .next】

    slow 每次走一步，fast 每次走兩步。
    - 如果會走到 1：fast 先到 1，而 1 的下一個還是 1。
    - 如果有環：fast 一定會在環裡追上 slow。

【結束條件】
    fast == 1          -> 快樂 ✔
    slow == fast != 1  -> 在不含 1 的環裡相遇 ✘

【為什麼 fast 初始是 nxt(n) 而不是 n？】
    如果兩者都從 n 開始，while 條件 slow != fast
    一開始就不成立，迴圈根本不會執行。"""),
   ], "O(log n)", "O(1)", "同解法一", "只有兩個變數", optimal=True),

   ap("解法三", "數學：唯一的不快樂循環", [
     ("c", S["p202_math"]),
     "數學上可以證明，所有不快樂數最後都會掉進 "
     "<code>4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4</code> 這個循環。"
     "所以只要看到其中任何一個數，就可以判定不快樂。",
     "<strong>這個解法最快，但它依賴一個「背下來的事實」</strong>——面試時可以提，但要說明它的根據"
     "（範圍有限，可以暴力驗證 1–810 的所有數）。",
   ], "O(log n)", "O(1)", "", "集合是常數大小"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、集合", "O(log n)", "O(log n)", "最直觀"],
    ["二、快慢指標", "O(log n)", "O(1)", "面試推薦 ✔"],
    ["三、已知循環", "O(log n)", "O(1)", "要背數學事實"]]),
 "edges": [
   "<strong><code>n = 1</code></strong> → 直接是快樂數。",
   "<strong><code>n = 7</code></strong> → 7 → 49 → 97 → 130 → 10 → 1，是快樂數（個位數裡只有 1 和 7）。",
   "<strong>很大的 n</strong> → 一步之後就 ≤ 810，不需要擔心。",
   "<strong>快慢指標兩者都從 <code>n</code> 開始</strong> → 迴圈不會執行，永遠回傳 <code>false</code>（除非 n = 1）。",
 ],
 "follow": [
   ("h", "追問一：怎麼證明序列一定會進入循環？"),
   ("c", """1. d 位數的位數平方和 ≤ 81d。
2. 當 d ≥ 4 時，81d < 10^(d-1)，也就是「下一個數的位數會變少」。
3. 所以序列最後一定落在 ≤ 3 位數（≤ 243）的範圍內。
4. 有限狀態 + 確定性的轉移 -> 鴿籠原理：一定會重複。"""),
   ("h", "追問二：這個「函數迭代找環」的模式還出現在哪？"),
   ("ul", [
     "<strong>第 141 / 142 題 環狀鏈結串列</strong>：最原始的版本。",
     "<strong>第 287 題 尋找重複數</strong>：把陣列看成 <code>i → nums[i]</code> 的函數，用 Floyd 找環的入口。",
     "<strong>偽隨機數產生器的週期偵測</strong>：同樣是 Floyd 或 Brent 演算法。",
   ]),
 ],
 "related": [
   "<strong>第 141 題 環狀鏈結串列</strong> —— 快慢指標找環",
   "<strong>第 142 題 環狀鏈結串列 II</strong> —— 找環的入口",
   "<strong>第 258 題 各位相加</strong> —— 另一個「反覆對位數做運算」的題目",
   "<strong>第 287 題 尋找重複數</strong> —— 陣列版的 Floyd",
 ],
 "check": [
   "為什麼這個過程不會無限變大？",
   "怎麼把這題轉換成鏈結串列找環？",
   "快慢指標的 <code>fast</code> 為什麼要從 <code>nxt(n)</code> 開始？",
   "不快樂數最後會掉進哪個循環？",
 ],
})


# ==================== 203. Remove Linked List Elements ====================
S["p203_dummy"] = '''class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)        # ★ 虛擬頭節點：頭也能被刪
        prev = dummy
        while prev.next:
            if prev.next.val == val:
                prev.next = prev.next.next   # 刪掉，prev 不動
            else:
                prev = prev.next             # 保留，prev 前進
        return dummy.next'''

S["p203_rec"] = '''class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)   # 先處理後面
        return head.next if head.val == val else head'''

S["p203_nodummy"] = '''class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:  # 先把開頭連續要刪的去掉
            head = head.next
        cur = head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head'''

_p203 = [S.load(k) for k in ("p203_dummy", "p203_rec", "p203_nodummy")]
for vals, v, want in [([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]), ([], 1, []), ([7, 7, 7, 7], 7, []),
                      ([1], 1, []), ([1, 2], 1, [2]), ([1, 2, 2, 1], 2, [1, 1])]:
    for sol in _p203:
        assert from_list(sol.removeElements(to_list(vals), v)) == want, ("P203", vals, v, sol)
for _ in range(3000):
    vals = [random.randint(1, 4) for _ in range(random.randrange(0, 12))]
    v = random.randint(0, 5)
    want = [x for x in vals if x != v]
    for sol in _p203:
        assert from_list(sol.removeElements(to_list(vals), v)) == want, ("P203 rand", vals, v)
print("P203 OK")

emit({
 "num": 203, "slug": "remove-linked-list-elements",
 "en": [
   "You are given the <code>head</code> of a singly linked list and an integer <code>val</code>. "
   "Delete every node whose value equals <code>val</code>, and return the head of the resulting list.",
 ],
 "zh": [
   "給你一個單向鏈結串列的頭節點 <code>head</code> 和一個整數 <code>val</code>，"
   "請<strong>刪除所有值等於 <code>val</code> 的節點</strong>，並回傳新的頭節點。",
 ],
 "examples": """範例 1
  輸入：head = [1,2,6,3,4,5,6], val = 6
  輸出：[1,2,3,4,5]

範例 2
  輸入：head = [], val = 1
  輸出：[]

範例 3
  輸入：head = [7,7,7,7], val = 7
  輸出：[]""",
 "constraints": [
   "串列的節點數在 <code>[0, 10⁴]</code> 之間",
   "1 ≤ <code>Node.val</code> ≤ 50",
   "0 ≤ <code>val</code> ≤ 50",
 ],
 "idea": [
   ("c", """【刪除一個節點，需要的是它的「前一個」節點】

    prev -> target -> after
    prev.next = after      # target 就被跳過了

【麻煩在頭節點】：頭節點沒有前一個節點。

    範例 3 [7,7,7,7] 的每一個節點都要刪，
    包括頭 —— 如果把「刪頭」和「刪中間」分開寫，
    很容易漏掉「連續好幾個頭都要刪」的情況。

【解法：虛擬頭節點（dummy node）】

    dummy -> 7 -> 7 -> 7 -> 7

    現在每個真正的節點都有「前一個」了，
    刪頭和刪中間變成同一件事 ✔
    最後回傳 dummy.next。

【一個容易錯的細節】

    刪掉 prev.next 之後，prev 【不要】前進 ——
    新的 prev.next 還沒檢查過，它可能也要刪。

    [1, 6, 6, 2]，val = 6：
        prev=1，刪第一個 6 -> prev 還是 1
        prev=1，刪第二個 6 -> prev 還是 1
        prev=1，下一個是 2，保留，前進 ✔"""),
 ],
 "approaches": [
   ap("解法一", "虛擬頭節點 + 一次走訪", [
     ("c", S["p203_dummy"]),
     "<strong>虛擬頭節點是鏈結串列題最常用的技巧</strong>，只要「頭節點可能會變」就可以考慮它。",
   ], "O(n)", "O(1)", "每個節點看一次", "只有一個 dummy", optimal=True),

   ap("解法二", "遞迴", [
     ("c", S["p203_rec"]),
     ("c", """【遞迴的想法】

    removeElements(head) =
        先把 head 後面的串列處理好（遞迴），接回 head.next，
        再決定 head 自己要不要留。

【為什麼不推薦在實務上用？】
    串列最長 10^4，遞迴深度也是 10^4，
    超過 Python 預設的遞迴上限（約 1000）-> RecursionError ✘

    LeetCode 的 Python 環境有調高上限，所以能過，
    但這是一個值得在面試中主動點出的風險。"""),
   ], "O(n)", "O(n)", "", "遞迴堆疊深度 n"),

   ap("解法三", "不用虛擬頭節點", [
     ("c", S["p203_nodummy"]),
     "先用一個 <code>while</code> 把開頭連續要刪的節點去掉，剩下的頭就一定要保留，"
     "再用一般的方式處理後面。<strong>能做，但要多寫一個迴圈，也多一個出錯的地方。</strong>",
   ], "O(n)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、虛擬頭節點", "O(n)", "O(1)", "推薦 ✔"],
    ["二、遞迴", "O(n)", "O(n)", "簡潔，但長串列有遞迴深度風險"],
    ["三、先處理頭", "O(n)", "O(1)", "多一段特殊處理"]]),
 "edges": [
   "<strong>空串列</strong> → 回傳 <code>None</code>。",
   "<strong>全部都要刪</strong> → 回傳 <code>None</code>。",
   "<strong>開頭連續好幾個要刪</strong> → 虛擬頭節點自然處理。",
   "<strong>連續好幾個要刪</strong> → 刪完之後 <code>prev</code> 不能前進。",
   "<strong><code>val</code> 不在串列裡</strong> → 原樣回傳。",
 ],
 "follow": [
   ("h", "追問一：如果是雙向鏈結串列呢？"),
   ("c", """刪除節點 x 時要改兩個指標：

    x.prev.next = x.next
    if x.next: x.next.prev = x.prev

同樣可以用虛擬頭（甚至虛擬尾）避免邊界判斷。"""),
   ("h", "追問二：虛擬頭節點還能用在哪些題？"),
   ("ul", [
     "<strong>第 19 題 刪除倒數第 N 個節點</strong>：刪的可能是頭。",
     "<strong>第 21 題 合併兩個有序串列</strong>：從 dummy 開始接。",
     "<strong>第 82 題 刪除排序串列中的重複元素 II</strong>：頭可能整段被刪。",
   ]),
 ],
 "related": [
   "<strong>第 27 題 移除元素</strong> —— 陣列版",
   "<strong>第 83 題 刪除排序串列中的重複元素</strong>",
   "<strong>第 237 題 刪除鏈結串列中的節點</strong> —— 只給要刪的節點",
 ],
 "check": [
   "刪除一個節點為什麼需要它的前一個節點？",
   "虛擬頭節點解決了什麼問題？",
   "刪除之後 <code>prev</code> 為什麼不能前進？",
   "遞迴解法在長串列上有什麼風險？",
 ],
})


# ==================== 204. Count Primes ====================
S["p204_sieve"] = '''class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0                          # 小於 2 的沒有質數；n = 2 也是 0
        is_p = bytearray([1]) * n             # is_p[i]：i 是不是質數
        is_p[0] = is_p[1] = 0
        i = 2
        while i * i < n:                      # ★ 只需要篩到 √n
            if is_p[i]:
                # ★ 從 i*i 開始劃掉，步長 i（用切片一次寫完）
                is_p[i * i::i] = bytes(len(range(i * i, n, i)))
            i += 1
        return sum(is_p)'''

S["p204_trial"] = '''class Solution:
    def countPrimes(self, n: int) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            d = 2
            while d * d <= x:                 # 試除到 √x
                if x % d == 0:
                    return False
                d += 1
            return True

        return sum(is_prime(x) for x in range(n))'''

S["p204_loop"] = '''class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        is_p = [True] * n
        is_p[0] = is_p[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_p[i]:
                for j in range(i * i, n, i):  # 一般迴圈版，比較慢但好懂
                    is_p[j] = False
        return sum(is_p)'''

_p204 = [S.load(k) for k in ("p204_sieve", "p204_trial", "p204_loop")]


def _p204_ref(n):
    return sum(1 for x in range(2, n) if all(x % d for d in range(2, int(x ** 0.5) + 1)))


for n, want in [(10, 4), (0, 0), (1, 0), (2, 0), (3, 1), (4, 2), (5, 2), (100, 25), (1000, 168)]:
    for sol in _p204:
        assert sol.countPrimes(n) == want, ("P204", n, sol)
for n in range(0, 600):
    want = _p204_ref(n)
    for sol in _p204:
        assert sol.countPrimes(n) == want, ("P204 rand", n)
assert _p204[0].countPrimes(5 * 10 ** 6) == 348513
print("P204 OK")

_P204_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">埃拉托斯特尼篩法（n = 30）：每找到一個質數 p，就從 p² 開始劃掉它的倍數</text>
            <g font-size="12" text-anchor="middle">
              <text x="50" y="62" fill="var(--text-muted)">0</text><text x="100" y="62" fill="var(--text-muted)">1</text>
              <text x="150" y="62" fill="var(--accent)" font-weight="bold">2</text><text x="200" y="62" fill="var(--accent)" font-weight="bold">3</text>
              <text x="250" y="62" fill="var(--text-muted)">4</text><text x="300" y="62" fill="var(--accent)" font-weight="bold">5</text>
              <text x="350" y="62" fill="var(--text-muted)">6</text><text x="400" y="62" fill="var(--accent)" font-weight="bold">7</text>
              <text x="450" y="62" fill="var(--text-muted)">8</text><text x="500" y="62" fill="var(--text-muted)">9</text>
              <text x="50" y="102" fill="var(--text-muted)">10</text><text x="100" y="102" fill="var(--accent)" font-weight="bold">11</text>
              <text x="150" y="102" fill="var(--text-muted)">12</text><text x="200" y="102" fill="var(--accent)" font-weight="bold">13</text>
              <text x="250" y="102" fill="var(--text-muted)">14</text><text x="300" y="102" fill="var(--text-muted)">15</text>
              <text x="350" y="102" fill="var(--text-muted)">16</text><text x="400" y="102" fill="var(--accent)" font-weight="bold">17</text>
              <text x="450" y="102" fill="var(--text-muted)">18</text><text x="500" y="102" fill="var(--accent)" font-weight="bold">19</text>
              <text x="50" y="142" fill="var(--text-muted)">20</text><text x="100" y="142" fill="var(--text-muted)">21</text>
              <text x="150" y="142" fill="var(--text-muted)">22</text><text x="200" y="142" fill="var(--accent)" font-weight="bold">23</text>
              <text x="250" y="142" fill="var(--text-muted)">24</text><text x="300" y="142" fill="var(--text-muted)">25</text>
              <text x="350" y="142" fill="var(--text-muted)">26</text><text x="400" y="142" fill="var(--text-muted)">27</text>
              <text x="450" y="142" fill="var(--text-muted)">28</text><text x="500" y="142" fill="var(--accent)" font-weight="bold">29</text>
            </g>
            <text x="20" y="180" fill="var(--text)" font-size="12">p = 2：劃掉 4, 6, 8, …　p = 3：從 9 開始劃掉 9, 12, 15, …　p = 5：從 25 開始劃掉 25</text>
            <text x="20" y="204" fill="var(--text)" font-size="12">p = 7：7² = 49 ≥ 30，停止。剩下沒被劃掉的就是質數：共 10 個。</text>
            <text x="20" y="228" fill="var(--gold)" font-size="12">★ 為什麼從 p² 開始？比 p² 小的倍數 k·p（k &lt; p）早就被更小的質數 k 劃掉了。</text>'''

emit({
 "num": 204, "slug": "count-primes",
 "en": [
   "Given an integer <code>n</code>, return how many prime numbers are <strong>strictly less than</strong> <code>n</code>.",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，回傳<strong>嚴格小於 <code>n</code></strong> 的質數有幾個。",
 ],
 "examples": """範例 1
  輸入：n = 10
  輸出：4
  說明：小於 10 的質數有 2、3、5、7。

範例 2
  輸入：n = 0
  輸出：0

範例 3
  輸入：n = 1
  輸出：0""",
 "constraints": [
   "0 ≤ <code>n</code> ≤ 5 × 10⁶",
 ],
 "idea": [
   ("fig", _P204_FIG, "0 0 640 244"),
   ("c", """【逐一判斷每個數是不是質數】
    每個數試除到 √x -> 總共 O(n √n)
    n = 5×10^6 時大約 10^10 次 ✘

【換個方向：不要「檢查」，改成「劃掉」】
    與其問「x 是不是質數」，
    不如從每個質數出發，把它的倍數全部劃掉。
    最後沒被劃掉的，就是質數。
    這就是【埃拉托斯特尼篩法（Sieve of Eratosthenes）】。

【兩個關鍵優化】
    1. 外層只需要到 √n：
       大於 √n 的合數 x = a·b，一定有一個因數 ≤ √n，
       早就被那個小因數劃掉了。
    2. 內層從 p² 開始：
       p 的倍數 2p, 3p, …, (p-1)p 都有一個比 p 小的因數，
       早就被劃掉了。

【複雜度】
    劃掉的總次數 ≈ n/2 + n/3 + n/5 + n/7 + …
                ≈ n · Σ(1/p) ≈ n · ln ln n
    -> O(n log log n)，幾乎是線性 ✔"""),
 ],
 "approaches": [
   ap("解法一", "逐一試除（會超時）", [
     ("c", S["p204_trial"]),
     "每個數最多試除 √x 次，總共大約 <code>n√n</code>。<strong>n = 5×10⁶ 時太慢。</strong>",
   ], "O(n√n)", "O(1)", "", ""),

   ap("解法二", "埃氏篩（一般迴圈）", [
     ("c", S["p204_loop"]),
     "邏輯完全正確，但在 Python 裡<strong>內層的 for 迴圈是瓶頸</strong>，"
     "n = 5×10⁶ 時可能要好幾秒。",
   ], "O(n log log n)", "O(n)", "", "一個長度 n 的陣列"),

   ap("解法三", "埃氏篩 + 切片賦值（Python 最佳寫法）", [
     ("c", S["p204_sieve"]),
     ("c", """【is_p[i*i::i] = bytes(k) 做了什麼？】

    把 is_p 從 i*i 開始、每隔 i 個的位置，全部設成 0。
    bytes(k) 是 k 個 0 組成的位元組串。

    這一行由 C 實作，一次處理整段 ->
    比 Python 迴圈快好幾十倍 ✔

【為什麼用 bytearray 而不是 list？】
    bytearray 每個元素 1 byte，
    list 每個元素是一個指標（8 bytes）+ 物件。
    n = 5×10^6 時，list 大約 40 MB，bytearray 只要 5 MB。

【len(range(i*i, n, i)) 是在算什麼？】
    切片 is_p[i*i::i] 的長度，
    右邊要給「一樣長」的 bytes，否則會報錯。"""),
   ], "O(n log log n)", "O(n)", "", "n bytes", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "n = 5×10⁶ 實測"],
   [["一、逐一試除", "O(n√n)", "O(1)", "超時 ✘"],
    ["二、篩法（迴圈）", "O(n log log n)", "O(n)", "數秒，邊緣"],
    ["三、篩法（切片）", "O(n log log n)", "O(n)", "約 0.1 秒 ✔"]]),
 "edges": [
   "<strong><code>n = 0, 1, 2</code></strong> → 答案都是 0（「嚴格小於」2 的質數不存在）。",
   "<strong><code>n = 3</code></strong> → 只有 2，答案 1。",
   "<strong>「小於 n」而不是「小於等於 n」</strong> → <code>n</code> 本身是質數也不算。",
   "<strong>外層條件寫成 <code>i * i &lt;= n</code></strong> → 也對，只是多跑一輪；寫成 <code>i &lt; n</code> 會慢很多。",
 ],
 "follow": [
   ("h", "追問一：有沒有 O(n) 的篩法？"),
   ("c", """【線性篩（歐拉篩）】：讓每個合數只被它的「最小質因數」劃掉一次。

    primes = []
    is_p = [True] * n
    for i in range(2, n):
        if is_p[i]:
            primes.append(i)
        for p in primes:
            if i * p >= n: break
            is_p[i * p] = False
            if i % p == 0: break    # ★ p 是 i 的最小質因數，停

理論上是 O(n)，但在 Python 裡因為沒辦法用切片，
實際上比「埃氏篩 + 切片」慢。"""),
   ("h", "追問二：如果要回答很多次「小於 n 的質數個數」？"),
   ("c", """先篩一次到最大的 n，再做前綴和：

    cnt[i] = 小於等於 i 的質數個數

每次查詢 O(1)。"""),
 ],
 "related": [
   "<strong>第 263 題 醜數</strong> —— 質因數分解",
   "<strong>第 264 題 醜數 II</strong> —— 用「倍數」產生序列",
   "<strong>第 2523 題 範圍內最接近的兩個質數</strong> —— 篩法 + 掃描",
 ],
 "check": [
   "篩法為什麼外層只需要到 √n？",
   "為什麼內層從 <code>p²</code> 開始劃？",
   "篩法的時間複雜度為什麼是 <code>O(n log log n)</code>？",
   "Python 裡怎麼讓篩法快幾十倍？",
 ],
})


# ==================== 205. Isomorphic Strings ====================
S["p205_two"] = '''class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            if s2t.get(a, b) != b or t2s.get(b, a) != a:   # ★ 兩個方向都要一致
                return False
            s2t[a] = b
            t2s[b] = a
        return True'''

S["p205_pattern"] = '''class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def pattern(x: str) -> List[int]:
            first = {}
            return [first.setdefault(c, len(first)) for c in x]   # 第幾個出現的字元
        return pattern(s) == pattern(t)'''

S["p205_set"] = '''class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))'''

S["p205_one"] = '''class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        for a, b in zip(s, t):
            if a in s2t and s2t[a] != b:
                return False
            s2t[a] = b
        return True          # ✘ 只檢查了一個方向'''

_p205 = [S.load(k) for k in ("p205_two", "p205_pattern", "p205_set")]
_p205_bad = S.load("p205_one")


def _p205_ref(s, t):
    m1, m2 = {}, {}
    for a, b in zip(s, t):
        if m1.setdefault(a, b) != b or m2.setdefault(b, a) != a:
            return False
    return True


for s, t, want in [("egg", "add", True), ("foo", "bar", False), ("paper", "title", True),
                   ("badc", "baba", False), ("a", "a", True), ("ab", "aa", False), ("13", "42", True)]:
    for sol in _p205:
        assert sol.isIsomorphic(s, t) == want, ("P205", s, t, sol)
assert _p205_bad.isIsomorphic("badc", "baba") is True   # 單向版本在這個例子會錯
for _ in range(5000):
    n = random.randrange(1, 8)
    s = "".join(random.choice("abc") for _ in range(n))
    t = "".join(random.choice("xyz") for _ in range(n))
    want = _p205_ref(s, t)
    for sol in _p205:
        assert sol.isIsomorphic(s, t) == want, ("P205 rand", s, t)
print("P205 OK")

emit({
 "num": 205, "slug": "isomorphic-strings",
 "en": [
   "Two strings <code>s</code> and <code>t</code> of equal length are called <em>isomorphic</em> if the "
   "characters of <code>s</code> can be replaced to produce <code>t</code>.",
   "Every occurrence of a character must be replaced by the same character, keeping the order of "
   "characters unchanged. Two different characters may not map to the same character, but a "
   "character is allowed to map to itself.",
   "Return <code>true</code> if <code>s</code> and <code>t</code> are isomorphic.",
 ],
 "zh": [
   "兩個等長字串 <code>s</code> 和 <code>t</code>，如果可以把 <code>s</code> 的字元替換成別的字元而得到 <code>t</code>，"
   "就稱它們<strong>同構</strong>。",
   "規則：同一個字元的每次出現都必須換成同一個字元，字元的順序不能改變；"
   "<strong>兩個不同的字元不能對應到同一個字元</strong>，但一個字元可以對應到它自己。",
   "如果 <code>s</code> 和 <code>t</code> 同構，回傳 <code>true</code>。",
 ],
 "examples": """範例 1
  輸入：s = "egg", t = "add"
  輸出：true
  說明：e -> a、g -> d。

範例 2
  輸入：s = "foo", t = "bar"
  輸出：false
  說明：o 要同時對應 a 和 r，不行。

範例 3
  輸入：s = "paper", t = "title"
  輸出：true

範例 4
  輸入：s = "badc", t = "baba"
  輸出：false
  說明：b -> b、d -> b，兩個不同的字元對應到同一個 b，不行。""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 5 × 10⁴",
   "<code>t.length == s.length</code>",
   "<code>s</code> 和 <code>t</code> 由任意有效的 ASCII 字元組成",
 ],
 "idea": [
   ("c", """【同構 = 字元之間存在一個「一對一」的對應（雙射）】

    兩個條件缺一不可：
    1. s 的同一個字元，永遠對到 t 的同一個字元（是函數）
    2. s 的不同字元，不能對到 t 的同一個字元（是單射）

【最常見的錯誤：只檢查第一個條件】

    s = "badc", t = "baba"
        b -> b, a -> a, d -> b, c -> a
    只看 s -> t 的方向，每個 s 字元都只對一個 t 字元 ✔
    但 b 和 d 都對到 b ✘

    所以要同時維護 s -> t 和 t -> s 兩張表。

【另一個角度：比較「形狀」】

    "paper" -> 第幾個新字元：[0, 1, 0, 2, 3]
    "title" -> 第幾個新字元：[0, 1, 0, 2, 3]
    形狀一樣 -> 同構 ✔"""),
 ],
 "approaches": [
   ap("解法一", "雙向雜湊表", [
     ("c", S["p205_two"]),
     ("c", """【s2t.get(a, b) != b 的意思】

    如果 a 還沒有對應 -> get 回傳 b -> 相等，不衝突
    如果 a 已經對應 x  -> 看 x 是不是 b

    一行同時處理「第一次出現」和「已經出現」兩種情況。"""),
     ("h", "只檢查單向為什麼會錯"),
     ("c", S["p205_one"]),
     "上面這個版本在 <code>s = \"badc\", t = \"baba\"</code> 會回傳 <code>true</code>——錯。",
   ], "O(n)", "O(k)", "", "k 是字元種類數（ASCII 最多 128）", optimal=True),

   ap("解法二", "比較首次出現的「形狀」", [
     ("c", S["p205_pattern"]),
     "把每個字元換成「它是第幾種出現的字元」，兩個字串的形狀相同就同構。"
     "<strong>這個想法可以直接推廣到第 290 題單詞規律。</strong>",
   ], "O(n)", "O(n)", "", "形狀陣列"),

   ap("解法三", "集合計數（一行）", [
     ("c", S["p205_set"]),
     ("c", """【為什麼三個集合大小相等就代表同構？】

    set(zip(s, t)) 是所有出現過的「配對」。
    - 如果某個 s 字元對到兩種 t 字元，
      配對數 > s 的字元種類數。
    - 如果兩個 s 字元對到同一個 t 字元，
      配對數 > t 的字元種類數。

    三者相等 -> 既是函數又是單射 ✔"""),
   ], "O(n)", "O(n)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、雙向雜湊表", "O(n)", "O(k)", "可以提早結束 ✔"],
    ["二、形狀比較", "O(n)", "O(n)", "好推廣"],
    ["三、集合計數", "O(n)", "O(n)", "一行，但要解釋為什麼對"]]),
 "edges": [
   "<strong>長度 1</strong> → 一定同構。",
   "<strong>字元對應到自己</strong>（<code>\"ab\", \"ab\"</code>）→ 允許。",
   "<strong>兩個不同字元對應同一個</strong>（<code>\"ab\", \"aa\"</code>）→ 不同構。",
   "<strong>只檢查單向</strong> → <code>\"badc\", \"baba\"</code> 會誤判。",
   "<strong>字元不只英文字母</strong> → 題目說是任意 ASCII，別用長度 26 的陣列。",
 ],
 "follow": [
   ("h", "追問：怎麼把一堆字串依「同構」分組？"),
   ("c", """把每個字串轉成它的「形狀」當作 key：

    groups = defaultdict(list)
    for w in words:
        groups[tuple(pattern(w))].append(w)

形狀相同的字串就在同一組 —— 和第 49 題字母異位詞分組是同一個套路。"""),
 ],
 "related": [
   "<strong>第 290 題 單詞規律</strong> —— 字元對單詞的同構",
   "<strong>第 890 題 查找和替換模式</strong> —— 形狀比較",
   "<strong>第 49 題 字母異位詞分組</strong> —— 「找 key」的分組套路",
 ],
 "check": [
   "同構需要滿足哪兩個條件？",
   "為什麼只維護 <code>s → t</code> 一張表會錯？舉一個反例。",
   "「形狀」的想法是什麼？",
   "三個集合大小相等為什麼就代表同構？",
 ],
})


# ==================== 206. Reverse Linked List ====================
S["p206_iter"] = '''class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            nxt = cur.next      # 1. 先記住下一個
            cur.next = prev     # 2. 反轉指標
            prev = cur          # 3. prev 前進
            cur = nxt           # 4. cur 前進
        return prev             # ★ cur 走到 None 時，prev 是新的頭'''

S["p206_rec"] = '''class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)   # 先把後面反轉好
        head.next.next = head                    # ★ 讓後一個節點指回自己
        head.next = None                         # 斷開舊的指標
        return new_head'''

S["p206_stack"] = '''class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        dummy = tail = ListNode()
        while stack:
            tail.next = stack.pop()
            tail = tail.next
        tail.next = None        # ★ 原本的頭現在是尾，要斷開，否則成環
        return dummy.next'''

_p206 = [S.load(k) for k in ("p206_iter", "p206_rec", "p206_stack")]
for vals in [[1, 2, 3, 4, 5], [1, 2], [], [7]]:
    for sol in _p206:
        assert from_list(sol.reverseList(to_list(vals))) == vals[::-1], ("P206", vals, sol)
for _ in range(2000):
    vals = [random.randint(-5000, 5000) for _ in range(random.randrange(0, 30))]
    for sol in _p206:
        assert from_list(sol.reverseList(to_list(vals))) == vals[::-1], ("P206 rand", vals)
print("P206 OK")

_P206_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">迭代反轉的一步：cur 的箭頭改指向 prev，然後三個指標一起往右走</text>
            <g font-size="13" text-anchor="middle">
              <text x="60" y="70" fill="var(--text-muted)">None</text>
              <rect x="120" y="50" width="50" height="30" rx="5" fill="none" stroke="var(--accent)"/><text x="145" y="70" fill="var(--accent)">1</text>
              <rect x="230" y="50" width="50" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="255" y="70" fill="#ff8a65">2</text>
              <rect x="340" y="50" width="50" height="30" rx="5" fill="none" stroke="var(--text-muted)"/><text x="365" y="70" fill="var(--text)">3</text>
              <rect x="450" y="50" width="50" height="30" rx="5" fill="none" stroke="var(--text-muted)"/><text x="475" y="70" fill="var(--text)">4</text>
              <text x="145" y="102" fill="var(--accent)" font-size="11">prev</text>
              <text x="255" y="102" fill="#ff8a65" font-size="11">cur</text>
              <text x="365" y="102" fill="var(--text-muted)" font-size="11">nxt</text>
            </g>
            <g stroke="var(--text-muted)" stroke-width="1.3" fill="none">
              <path d="M120 65 L85 65"/><path d="M85 65 l7 -4 M85 65 l7 4"/>
              <path d="M280 65 L335 65"/><path d="M335 65 l-7 -4 M335 65 l-7 4"/>
              <path d="M390 65 L445 65"/><path d="M445 65 l-7 -4 M445 65 l-7 4"/>
            </g>
            <path d="M230 58 C205 40 190 40 172 58" stroke="#ff8a65" stroke-width="1.8" fill="none" stroke-dasharray="4 3"/>
            <path d="M172 58 l9 -1 M172 58 l3 -8" stroke="#ff8a65" stroke-width="1.8"/>
            <text x="200" y="36" fill="#ff8a65" font-size="11">cur.next = prev</text>
            <text x="20" y="140" fill="var(--text)" font-size="12">1. nxt = cur.next　先記住 3，不然改完箭頭就找不到了</text>
            <text x="20" y="164" fill="var(--text)" font-size="12">2. cur.next = prev　2 的箭頭改成指向 1（虛線）</text>
            <text x="20" y="188" fill="var(--text)" font-size="12">3. prev = cur　　　 prev 移到 2</text>
            <text x="20" y="212" fill="var(--text)" font-size="12">4. cur = nxt　　　　cur 移到 3，進入下一輪</text>
            <text x="20" y="240" fill="var(--gold)" font-size="12">★ 順序不能換：一定要先存 nxt，再改 cur.next。</text>'''

emit({
 "num": 206, "slug": "reverse-linked-list",
 "en": [
   "Given the <code>head</code> of a singly linked list, reverse the list and return the head of the reversed list.",
 ],
 "zh": [
   "給你一個單向鏈結串列的頭節點 <code>head</code>，請把串列<strong>反轉</strong>，並回傳反轉後的頭節點。",
 ],
 "examples": """範例 1
  輸入：head = [1,2,3,4,5]
  輸出：[5,4,3,2,1]

範例 2
  輸入：head = [1,2]
  輸出：[2,1]

範例 3
  輸入：head = []
  輸出：[]""",
 "constraints": [
   "串列的節點數在 <code>[0, 5000]</code> 之間",
   "−5000 ≤ <code>Node.val</code> ≤ 5000",
 ],
 "mid": [
   ("note", "題目的追問", [
     "<strong>「A linked list can be reversed either iteratively or recursively. Could you implement both?」</strong>",
     "這題是鏈結串列的<strong>基本功</strong>：第 25、92、234、143 等題都會用到「反轉一段串列」。",
   ]),
 ],
 "idea": [
   ("fig", _P206_FIG, "0 0 640 256"),
   ("c", """【反轉 = 把每一個箭頭的方向顛倒】

    1 -> 2 -> 3 -> None
    變成
    None <- 1 <- 2 <- 3

【難點】
    改掉 cur.next 的那一刻，就失去了通往後面的路。
    所以要先用 nxt 記住後面，再改。

【三個指標的角色】
    prev：已經反轉好的那一段的頭
    cur ：正在處理的節點
    nxt ：還沒處理的那一段的頭（暫存）

【迴圈不變量】
    每一輪開始時：
        prev 之前（含 prev）是反轉好的串列
        cur 之後（含 cur）是原本的串列
    cur 走到 None -> prev 就是整條反轉好的串列的頭 ✔"""),
 ],
 "approaches": [
   ap("解法一", "迭代（三指標）", [
     ("c", S["p206_iter"]),
     "<strong>一定要背熟的模板</strong>，四行的順序固定：存下一個、改箭頭、prev 前進、cur 前進。",
   ], "O(n)", "O(1)", "每個節點一次", "三個指標", optimal=True),

   ap("解法二", "遞迴", [
     ("c", S["p206_rec"]),
     ("c", """【遞迴的想法】
    假設 head.next 之後的部分已經反轉好了：

        1 -> 2 <- 3 <- 4 <- 5
             ^ head.next（現在是反轉後的尾巴）

    只要讓 2 指回 1：head.next.next = head
    再把 1 的 next 清掉：head.next = None

【最容易漏的一行】
    head.next = None
    漏掉的話，1 和 2 互相指著 -> 環 ✘

【new_head 一路往上傳】
    最深一層回傳原本的尾巴（5），
    每一層都原封不動地回傳它 -> 最後就是新的頭 ✔

【缺點】
    遞迴深度 n = 5000，超過 Python 預設上限 1000。
    LeetCode 有調高，但實務上要小心。"""),
   ], "O(n)", "O(n)", "", "遞迴堆疊"),

   ap("解法三", "堆疊", [
     ("c", S["p206_stack"]),
     "把節點依序推進堆疊，再依序彈出接起來。<strong>最後一定要把尾巴的 <code>next</code> 設成 <code>None</code></strong>，"
     "否則原本的頭（現在的尾）還指著第二個節點，形成環。",
   ], "O(n)", "O(n)", "", "堆疊存 n 個節點"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、迭代", "O(n)", "O(1)", "標準答案 ✔"],
    ["二、遞迴", "O(n)", "O(n)", "要會寫，理解遞迴很好的練習"],
    ["三、堆疊", "O(n)", "O(n)", "直觀，但要記得斷開尾巴"]]),
 "edges": [
   "<strong>空串列</strong> → 回傳 <code>None</code>。",
   "<strong>只有一個節點</strong> → 回傳它自己。",
   "<strong>遞迴漏了 <code>head.next = None</code></strong> → 形成環。",
   "<strong>堆疊法漏了斷開尾巴</strong> → 形成環。",
   "<strong>迭代時先改 <code>cur.next</code> 再存 <code>nxt</code></strong> → 後面的節點全部遺失。",
 ],
 "follow": [
   ("h", "追問一：只反轉第 left 到 right 個節點？"),
   ("c", """這是第 92 題。做法：
    1. 用虛擬頭走到第 left-1 個節點 pre。
    2. 對接下來的 right-left+1 個節點做「頭插法」：
       每次把 cur.next 拿出來，插到 pre 後面。
    3. 一次走訪就完成，O(n) 時間、O(1) 空間。"""),
   ("h", "追問二：每 k 個一組反轉？"),
   ("c", """這是第 25 題（Hard）。
    每次先檢查後面是否還有 k 個節點，
    有的話用本題的迭代法反轉這 k 個，再接回前後。"""),
 ],
 "related": [
   "<strong>第 92 題 反轉鏈結串列 II</strong> —— 反轉一段",
   "<strong>第 25 題 K 個一組反轉鏈結串列</strong>",
   "<strong>第 234 題 回文鏈結串列</strong> —— 反轉後半段再比較",
   "<strong>第 143 題 重排鏈結串列</strong> —— 找中點 + 反轉 + 合併",
 ],
 "check": [
   "迭代法的四行，為什麼順序不能換？",
   "迴圈結束時為什麼回傳 <code>prev</code>？",
   "遞迴法中 <code>head.next.next = head</code> 做了什麼？漏了 <code>head.next = None</code> 會怎樣？",
   "堆疊法最後為什麼要把尾巴斷開？",
 ],
})
