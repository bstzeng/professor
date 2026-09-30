# -*- coding: utf-8 -*-
"""第 231–236 題。"""
import random
from authoring import emit, ap
from runner import Src, to_list, from_list
from lchelp import lv, bst, nodes, rand_tree

S = Src()
random.seed(231)


# ==================== 231. Power of Two ====================
S["p231_bit"] = '''class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # ★ 2 的冪次在二進位中只有一個 1；n & (n-1) 會把最低位的 1 清掉
        return n > 0 and n & (n - 1) == 0'''

S["p231_low"] = '''class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & -n == n          # n & -n：只保留最低位的 1'''

S["p231_loop"] = '''class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:                     # 一直除以 2
            n //= 2
        return n == 1'''

S["p231_div"] = '''class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # 範圍內最大的 2 的冪次是 2^30；n 是 2 的冪次 <=> n 整除 2^30
        return n > 0 and (1 << 30) % n == 0'''

_p231 = [S.load(x) for x in ("p231_bit", "p231_low", "p231_loop", "p231_div")]
_pw = {1 << i for i in range(31)}
for n in list(range(-70, 5000)) + [2 ** 30, 2 ** 30 - 1, 2 ** 31 - 1, -2 ** 31, 3 * 2 ** 20]:
    for sol in _p231:
        assert sol.isPowerOfTwo(n) == (n in _pw), ("P231", n, sol)
print("P231 OK")

_P231_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">n &amp; (n − 1)：把最低位的 1 清成 0</text>
            <g font-family="monospace" font-size="15">
              <text x="40" y="58" fill="var(--text-muted)">n     = 8</text><text x="200" y="58" fill="var(--accent)">0 1 0 0 0</text>
              <text x="40" y="82" fill="var(--text-muted)">n − 1 = 7</text><text x="200" y="82" fill="var(--text)">0 0 1 1 1</text>
              <line x1="200" y1="90" x2="300" y2="90" stroke="var(--border)"/>
              <text x="40" y="110" fill="var(--text-muted)">n &amp; (n−1)</text><text x="200" y="110" fill="var(--gold)">0 0 0 0 0</text>
              <text x="330" y="58" fill="var(--text-muted)">n     = 12</text><text x="490" y="58" fill="var(--accent)">0 1 1 0 0</text>
              <text x="330" y="82" fill="var(--text-muted)">n − 1 = 11</text><text x="490" y="82" fill="var(--text)">0 1 0 1 1</text>
              <line x1="490" y1="90" x2="590" y2="90" stroke="var(--border)"/>
              <text x="330" y="110" fill="var(--text-muted)">n &amp; (n−1)</text><text x="490" y="110" fill="#ff8a65">0 1 0 0 0</text>
            </g>
            <text x="40" y="144" fill="var(--gold)" font-size="12">8 只有一個 1 → 清掉就變 0 → 是 2 的冪</text>
            <text x="330" y="144" fill="#ff8a65" font-size="12">12 有兩個 1 → 清掉一個還剩 → 不是</text>
            <text x="20" y="176" fill="var(--text)" font-size="12">減 1 會把「最低位的 1」變 0，並把它右邊的 0 全部變 1；AND 之後這一段全部歸零。</text>'''

emit({
 "num": 231, "slug": "power-of-two",
 "en": [
   "Given an integer <code>n</code>, return <code>true</code> if it is a power of two. Otherwise, return <code>false</code>.",
   "An integer <code>n</code> is a power of two if there exists an integer <code>x</code> such that <code>n == 2<sup>x</sup></code>.",
   "<strong>Follow up:</strong> Could you solve it without loops/recursion?",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，判斷它是不是 2 的冪次。",
   "如果存在整數 <code>x</code> 使得 <code>n == 2<sup>x</sup></code>，<code>n</code> 就是 2 的冪次。",
   "<strong>進階：</strong>能不用迴圈或遞迴嗎？",
 ],
 "examples": """範例 1
  輸入：n = 1
  輸出：true
  說明：2⁰ = 1

範例 2
  輸入：n = 16
  輸出：true

範例 3
  輸入：n = 3
  輸出：false""",
 "constraints": [
   "−2³¹ ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("fig", _P231_FIG, "0 0 640 190"),
   ("c", """【2 的冪次在二進位中長什麼樣子？】
    1 = 1, 2 = 10, 4 = 100, 8 = 1000 ...
    恰好只有【一個】位元是 1。

【n & (n - 1) 清掉最低位的 1】
    n     = ...1000
    n - 1 = ...0111
    AND   = ...0000
    只有一個 1 的數，清掉之後就是 0。

【一定要先檢查 n > 0】
    n = 0：0 & (-1) = 0，會被誤判 ✘
    負數：永遠不是 2 的冪次。

【另一個技巧：n & -n】
    二補數中 -n = ~n + 1，
    n & -n 只保留最低位的 1（這個值叫 lowbit，樹狀陣列會用到）。
    只有一個 1 的數，lowbit 就是它自己。"""),
 ],
 "approaches": [
   ap("解法一", "一直除以 2", [
     ("c", S["p231_loop"]),
   ], "O(log n)", "O(1)", "", ""),

   ap("解法二", "n &amp; (n − 1)", [
     ("c", S["p231_bit"]),
   ], "O(1)", "O(1)", "", "", optimal=True),

   ap("解法三", "n &amp; −n（lowbit）", [
     ("c", S["p231_low"]),
   ], "O(1)", "O(1)", "", ""),

   ap("解法四", "最大的 2 的冪次能否被 n 整除", [
     ("c", S["p231_div"]),
     "2³⁰ 的因數只有 2⁰、2¹、…、2³⁰（質因數分解只有 2）。這個技巧對任何<strong>質數</strong>的冪次都適用（第 326 題的 3 的冪次也能這樣做）。",
   ], "O(1)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、除以 2", "O(log n)", "最直觀"],
    ["二、n &amp; (n−1)", "O(1)", "最常見 ✔"],
    ["三、n &amp; −n", "O(1)", "lowbit"],
    ["四、整除 2³⁰", "O(1)", "適用於質數的冪次"]]),
 "edges": [
   "<strong>n = 0</strong> → false（位元解法一定要先檢查 n &gt; 0）。",
   "<strong>n = 1</strong> → true（2⁰）。",
   "<strong>負數</strong> → false；−2³¹ 在二補數中只有一個 1，但不是 2 的冪次。",
 ],
 "follow": [
   ("h", "延伸：數一個數有幾個 1？"),
   ("c", "第 191 題：不斷做 n &amp;= n − 1，做了幾次就有幾個 1（Brian Kernighan 演算法）。"),
 ],
 "related": [
   "<strong>第 191 題 位元 1 的個數</strong>",
   "<strong>第 326 題 3 的冪</strong>",
   "<strong>第 342 題 4 的冪</strong>",
 ],
 "check": [
   "2 的冪次在二進位中有什麼特徵？",
   "<code>n &amp; (n − 1)</code> 做了什麼？",
   "為什麼要先檢查 <code>n &gt; 0</code>？",
 ],
})


# ==================== 232. Implement Queue using Stacks ====================
S["p232"] = '''class MyQueue:
    def __init__(self):
        self.inbox = []            # 負責 push
        self.outbox = []           # 負責 pop / peek（頂端 = 隊頭）

    def push(self, x: int) -> None:
        self.inbox.append(x)

    def _move(self) -> None:
        if not self.outbox:        # ★ 只有 outbox 空了才倒，否則順序會亂
            while self.inbox:
                self.outbox.append(self.inbox.pop())

    def pop(self) -> int:
        self._move()
        return self.outbox.pop()

    def peek(self) -> int:
        self._move()
        return self.outbox[-1]

    def empty(self) -> bool:
        return not self.inbox and not self.outbox'''

S["p232_naive"] = '''class MyQueue:
    def __init__(self):
        self.s = []                # 頂端永遠是隊頭（最早進來的）
        self.tmp = []

    def push(self, x: int) -> None:          # O(n)：先把全部倒出去，放 x，再倒回來
        while self.s:
            self.tmp.append(self.s.pop())
        self.s.append(x)
        while self.tmp:
            self.s.append(self.tmp.pop())

    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return not self.s'''

for key in ("p232", "p232_naive"):
    for _ in range(300):
        q, ref = S.load(key, "MyQueue"), []
        for _ in range(random.randrange(1, 50)):
            r = random.random()
            if ref and r < 0.3:
                assert q.pop() == ref.pop(0), key
            elif ref and r < 0.45:
                assert q.peek() == ref[0], key
            elif r < 0.55:
                assert q.empty() == (not ref), key
            else:
                x = random.randrange(10)
                q.push(x)
                ref.append(x)
print("P232 OK")

_P232_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">push 1, 2, 3 之後 pop：outbox 空了，才把 inbox 整批倒過去</text>
            <g font-size="13" text-anchor="middle">
              <rect x="60" y="50" width="60" height="96" fill="none" stroke="var(--border)"/>
              <rect x="66" y="116" width="48" height="24" fill="none" stroke="var(--accent)"/><text x="90" y="133" fill="var(--accent)">1</text>
              <rect x="66" y="88" width="48" height="24" fill="none" stroke="var(--accent)"/><text x="90" y="105" fill="var(--accent)">2</text>
              <rect x="66" y="60" width="48" height="24" fill="none" stroke="var(--accent)"/><text x="90" y="77" fill="var(--accent)">3</text>
              <text x="90" y="166" fill="var(--text-muted)">inbox</text>
              <rect x="300" y="50" width="60" height="96" fill="none" stroke="var(--border)"/>
              <rect x="306" y="116" width="48" height="24" fill="none" stroke="var(--gold)"/><text x="330" y="133" fill="var(--gold)">3</text>
              <rect x="306" y="88" width="48" height="24" fill="none" stroke="var(--gold)"/><text x="330" y="105" fill="var(--gold)">2</text>
              <rect x="306" y="60" width="48" height="24" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="330" y="77" fill="#ff8a65">1</text>
              <text x="330" y="166" fill="var(--text-muted)">outbox</text>
            </g>
            <line x1="140" y1="98" x2="274" y2="98" stroke="var(--text-muted)"/><polygon points="282,98 272,93 272,103" fill="var(--text-muted)"/>
            <text x="210" y="88" text-anchor="middle" fill="var(--text-muted)" font-size="12">逐一 pop 再 push</text>
            <text x="210" y="116" text-anchor="middle" fill="var(--text-muted)" font-size="12">順序反轉</text>
            <text x="390" y="78" fill="#ff8a65" font-size="12">← 頂端 = 最早 push 的 1</text>
            <text x="390" y="104" fill="var(--text)" font-size="12">pop / peek 直接拿這裡</text>
            <text x="20" y="196" fill="var(--gold)" font-size="12">★ 每個元素一生只會被搬一次：inbox → outbox。n 次操作總共 O(n) → 攤銷 O(1)。</text>'''

emit({
 "num": 232, "slug": "implement-queue-using-stacks",
 "en": [
   "Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions "
   "of a normal queue (<code>push</code>, <code>peek</code>, <code>pop</code>, and <code>empty</code>).",
   "You must use <strong>only</strong> standard operations of a stack: push to top, peek/pop from top, size, and is empty.",
   "<strong>Follow-up:</strong> Can you implement the queue such that each operation is <strong>amortized</strong> <code>O(1)</code> "
   "time complexity? In other words, performing <code>n</code> operations will take overall <code>O(n)</code> time even if one of those operations may take longer.",
 ],
 "zh": [
   "只用兩個堆疊實作一個先進先出（FIFO）的佇列，支援 <code>push</code>、<code>peek</code>、<code>pop</code>、<code>empty</code>。",
   "只能使用堆疊的標準操作：推到頂端、查看／取出頂端、取得大小、判斷是否為空。",
   "<strong>進階：</strong>能讓每個操作的<strong>攤銷</strong>時間都是 <code>O(1)</code> 嗎？也就是做 <code>n</code> 次操作總共 <code>O(n)</code>，即使其中某一次比較久。",
 ],
 "examples": """範例
  輸入：["MyQueue","push","push","peek","pop","empty"]
        [[],[1],[2],[],[],[]]
  輸出：[null,null,null,1,1,false]""",
 "constraints": [
   "1 ≤ <code>x</code> ≤ 9",
   "最多呼叫 100 次",
   "<code>pop</code> 和 <code>peek</code> 呼叫時，佇列一定不是空的",
 ],
 "idea": [
   ("fig", _P232_FIG, "0 0 640 210"),
   ("c", """【一個堆疊倒進另一個堆疊，順序就反過來】
    inbox：[1, 2, 3]（3 在頂端）
    全部倒到 outbox：[3, 2, 1]（1 在頂端）✔ 最早的在最上面

【兩個堆疊的分工】
    push -> 永遠放進 inbox
    pop / peek -> 從 outbox 拿；outbox 空了才把 inbox 整批倒過去

【為什麼「outbox 空了才倒」？】
    outbox 裡的元素都比 inbox 裡的早進來。
    如果 outbox 還有東西就倒，新的元素會壓在舊元素上面 ✘

【攤銷 O(1)】
    單次 pop 可能要搬 n 個 -> O(n)
    但每個元素一生：push 進 inbox 1 次、搬家 1 次、pop 出 outbox 1 次
    n 次操作總共 O(n) -> 平均每次 O(1)。"""),
 ],
 "approaches": [
   ap("解法一", "每次 push 都整理成佇列順序", [
     ("c", S["p232_naive"]),
     "每次 push 都要把整個堆疊倒出去再倒回來，O(n)。",
   ], "push O(n)，其他 O(1)", "O(n)", "", ""),

   ap("解法二", "inbox / outbox 兩個堆疊（攤銷）", [
     ("c", S["p232"]),
   ], "攤銷 O(1)", "O(n)", "單次 pop 最壞 O(n)", "", optimal=True),
 ],
 "compare": (["解法", "push", "pop / peek"],
   [["一、每次整理", "O(n)", "O(1)"],
    ["二、inbox / outbox", "O(1)", "攤銷 O(1) ✔"]]),
 "edges": [
   "<strong>push、pop 交錯</strong> → outbox 還有東西時不能倒。",
   "<strong>empty</strong> → 兩個堆疊都要是空的。",
   "<strong>peek 之後再 pop</strong> → peek 也會觸發搬家，但搬過一次就不會重複搬。",
 ],
 "follow": [
   ("h", "「攤銷」和「平均」有什麼不同？"),
   ("c", """平均（期望）複雜度是對隨機輸入取平均，可能有運氣差的輸入。
攤銷複雜度是對「任何一串操作」的總成本保證——最壞情況下 n 次操作也只要 O(n)。
Python list 的 append、動態陣列擴容，都是攤銷 O(1) 的例子。"""),
 ],
 "related": [
   "<strong>第 225 題 用佇列實作堆疊</strong>",
   "<strong>第 155 題 最小堆疊</strong>",
   "<strong>第 641 題 設計循環雙端佇列</strong>",
 ],
 "check": [
   "為什麼把一個堆疊倒進另一個，順序就變成佇列順序？",
   "為什麼只有 outbox 空的時候才能倒？",
   "為什麼攤銷時間是 O(1)？",
 ],
})


# ==================== 233. Number of Digit One ====================
S["p233"] = '''class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        p = 1                                   # 目前處理的位數：1, 10, 100, ...
        while p <= n:
            high = n // (p * 10)                # 這一位左邊的數字
            cur = n // p % 10                   # 這一位的數字
            low = n % p                         # 這一位右邊的數字
            if cur == 0:
                count += high * p               # ★ 左邊只能取 0..high-1
            elif cur == 1:
                count += high * p + low + 1     # ★ 左邊取 high 時，右邊只能取 0..low
            else:
                count += (high + 1) * p         # ★ 左邊可以取 0..high，右邊任意
            p *= 10
        return count'''

S["p233_dp"] = '''class Solution:
    def countDigitOne(self, n: int) -> int:
        digits = list(map(int, str(n)))

        @functools.lru_cache(None)
        def dfs(i: int, ones: int, tight: bool) -> int:
            # 從第 i 位開始填，前面已經有 ones 個 1；tight = 前面每一位都貼著 n
            if i == len(digits):
                return ones
            limit = digits[i] if tight else 9
            return sum(dfs(i + 1, ones + (d == 1), tight and d == limit)
                       for d in range(limit + 1))

        return dfs(0, 0, True)'''

S["p233_brute"] = '''class Solution:
    def countDigitOne(self, n: int) -> int:
        return sum(str(x).count("1") for x in range(1, n + 1))'''

_p233 = [S.load(x) for x in ("p233", "p233_dp", "p233_brute")]
_acc, _run = [0], 0
for x in range(1, 30001):
    _run += str(x).count("1")
    _acc.append(_run)
for n in list(range(0, 3000)) + random.sample(range(3000, 30001), 300):
    assert _p233[0].countDigitOne(n) == _acc[n], ("P233", n)
    if n % 7 == 0:
        assert _p233[1].countDigitOne(n) == _acc[n], ("P233 dp", n)
assert _p233[2].countDigitOne(13) == 6
assert _p233[0].countDigitOne(10 ** 9) == _p233[1].countDigitOne(10 ** 9) == 900000001
print("P233 OK")

emit({
 "num": 233, "slug": "number-of-digit-one",
 "en": [
   "Given an integer <code>n</code>, count the total number of digit <code>1</code> appearing in all non-negative integers less than or equal to <code>n</code>.",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，計算 <code>0</code> 到 <code>n</code> 的所有整數中，數字 <code>1</code> 一共出現了幾次。",
 ],
 "examples": """範例 1
  輸入：n = 13
  輸出：6
  說明：1, 10, 11(兩個), 12, 13 -> 1 + 1 + 2 + 1 + 1 = 6

範例 2
  輸入：n = 0
  輸出：0""",
 "constraints": [
   "0 ≤ <code>n</code> ≤ 10⁹",
 ],
 "idea": [
   ("c", """【換個角度：一位一位地數】
    不要數「每個數字有幾個 1」，
    改成數「個位是 1 的數有幾個」+「十位是 1 的數有幾個」+ ...

【以 n = 3141592，看百位（p = 100）】
    把 n 切成三段：high = 3141 | cur = 5 | low = 92

    百位是 1 的數長這樣：[左邊 L] 1 [右邊 R]，R 是 00..99
    - L = 0..3140：右邊隨便填 -> 3141 × 100 個
    - L = 3141：百位 1 比 cur = 5 小，右邊也隨便填 -> 再 100 個
    總共 (high + 1) × p

【cur 的三種情況】
    cur == 0：L 只能取 0..high-1         -> high × p
              （L = high 時，百位 1 > 0，超過 n）
    cur == 1：L 取 0..high-1 -> high × p
              L = high 時，R 只能 0..low  -> low + 1
    cur >= 2：L 可以取 0..high           -> (high + 1) × p

【複雜度】
    n 有 log₁₀ n 位，每一位 O(1) -> O(log n)"""),
   ("t", ["位數 p", "high", "cur", "low", "這一位是 1 的個數"],
    [["1", "1", "3", "0", "(1+1)×1 = 2（1, 11）"],
     ["10", "0", "1", "3", "0×10 + 3+1 = 4（10–13）"],
     ["合計", "", "", "", "6 ✔（n = 13）"]]),
 ],
 "approaches": [
   ap("解法一", "暴力：每個數字轉字串數 1", [
     ("c", S["p233_brute"]),
     "n = 10⁹ 時要跑十億次，超時。",
   ], "O(n log n)", "O(1)", "", ""),

   ap("解法二", "數位 DP", [
     ("c", S["p233_dp"]),
     ("c", """【數位 DP 的通用模板】
    從最高位往低位一位一位填，
    tight 表示「目前為止每一位都和 n 相同」——
    這時下一位最多只能填 n 的那一位；否則 0..9 都可以。

    這個模板能解一大類「1 到 n 之間有多少數滿足某條件」的題目。
    本題狀態數 ≈ 位數 × 1 的個數 × 2，很小。"""),
   ], "O(log² n · 10)", "O(log² n)", "", ""),

   ap("解法三", "逐位計算（數學）", [
     ("c", S["p233"]),
   ], "O(log n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、暴力", "O(n log n)", "O(1)", "超時"],
    ["二、數位 DP", "O(log² n · 10)", "O(log² n)", "模板通用"],
    ["三、逐位計算", "O(log n)", "O(1)", "最快 ✔"]]),
 "edges": [
   "<strong>n = 0</strong> → 0（迴圈一次都不跑）。",
   "<strong>n 的某一位是 0</strong>（例如 n = 105 的十位）→ 用 high × p。",
   "<strong>n = 10⁹</strong> → 答案 900,000,001；其他語言注意溢位。",
 ],
 "follow": [
   ("h", "推廣：數字 d（0–9）出現幾次？"),
   ("c", """把 cur == 1 換成 cur == d 的比較即可；但 d = 0 要特別處理——
不能有前導零，所以 high 要從 1 開始算（high × p 改成 (high − 1) × p 等）。
這正是面試題 17.06 / 第 1067 題（付費）的內容。"""),
 ],
 "related": [
   "<strong>第 902 題 最大為 N 的數字組合</strong> —— 數位 DP",
   "<strong>第 1067 題 範圍內的數字計數</strong>（付費）",
   "<strong>第 2376 題 統計特殊整數</strong> —— 數位 DP",
 ],
 "check": [
   "為什麼改成「每一位分別數」會比較容易？",
   "cur 分別是 0、1、≥2 時，公式為什麼不同？",
   "數位 DP 中 <code>tight</code> 代表什麼？",
 ],
})


# ==================== 234. Palindrome Linked List ====================
S["p234"] = '''class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. 快慢指標找中點
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2. 反轉後半段（奇數長度時，中間節點歸到後半段，不影響比較）
        prev = None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        # 3. 前後兩半同時往中間比
        left, right = head, prev
        ok = True
        while right:
            if left.val != right.val:
                ok = False
                break
            left, right = left.next, right.next
        return ok'''

S["p234_restore"] = '''class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            prev = None
            while node:
                node.next, prev, node = prev, node, node.next
            return prev

        # 找「前半段的最後一個節點」
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = reverse(slow.next)

        p, q, ok = head, second, True
        while ok and q:
            ok = p.val == q.val
            p, q = p.next, q.next

        slow.next = reverse(second)            # ★ 還原串列，呼叫者的資料不被破壞
        return ok'''

S["p234_arr"] = '''class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]'''

_p234 = [S.load(x) for x in ("p234", "p234_restore", "p234_arr")]
for _ in range(3000):
    n = random.randrange(1, 12)
    half = [random.randrange(3) for _ in range(n // 2)]
    vals = half + ([random.randrange(3)] if n % 2 else []) + half[::-1]
    if random.random() < 0.5:
        vals = [random.randrange(3) for _ in range(n)]
    want = vals == vals[::-1]
    for sol in _p234:
        h = to_list(vals)
        assert sol.isPalindrome(h) == want, ("P234", vals, sol)
    h = to_list(vals)
    _p234[1].isPalindrome(h)
    assert from_list(h) == vals, "P234 restore"
print("P234 OK")

emit({
 "num": 234, "slug": "palindrome-linked-list",
 "en": [
   "Given the <code>head</code> of a singly linked list, return <code>true</code> if it is a palindrome or <code>false</code> otherwise.",
   "<strong>Follow up:</strong> Could you do it in <code>O(n)</code> time and <code>O(1)</code> space?",
 ],
 "zh": [
   "給你一個單向鏈結串列的頭節點 <code>head</code>，判斷它是不是<strong>回文</strong>。",
   "<strong>進階：</strong>能用 <code>O(n)</code> 時間、<code>O(1)</code> 空間完成嗎？",
 ],
 "examples": """範例 1
  輸入：head = [1,2,2,1]
  輸出：true

範例 2
  輸入：head = [1,2]
  輸出：false""",
 "constraints": [
   "節點數在 <code>[1, 10⁵]</code> 之間",
   "0 ≤ <code>Node.val</code> ≤ 9",
 ],
 "idea": [
   ("c", """【陣列很簡單：頭尾兩個指標往中間比】
    但單向串列不能往回走。

【O(1) 空間的三步驟】
    1. 快慢指標找中點（第 876 題）
         快指標一次兩步、慢指標一次一步，
         快的走到底時，慢的在中間。
    2. 反轉後半段（第 206 題）
    3. 前半段從 head、後半段從反轉後的頭，同時往中間比

    1 -> 2 -> 3 -> 2 -> 1
    反轉後半：1 -> 2 -> 3 <- 2 <- 1
                        （3 的 next 是 None）
    left 從 1 開始、right 從右邊的 1 開始，逐一比對 ✔

【奇數長度】
    中間的節點和自己比，一定相等，不影響答案。

【副作用】
    這個做法會改動串列。實務上（或面試加分）
    比完之後應該把後半段再反轉回去 -> 解法三。"""),
 ],
 "approaches": [
   ap("解法一", "複製到陣列", [
     ("c", S["p234_arr"]),
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "快慢指標 + 反轉後半段", [
     ("c", S["p234"]),
   ], "O(n)", "O(1)", "", "", optimal=True),

   ap("解法三", "比完之後還原串列", [
     ("c", S["p234_restore"]),
     ("c", """【這裡的快慢指標條件不一樣】
    while fast.next and fast.next.next
    讓 slow 停在「前半段的最後一個」，
    才能透過 slow.next 把反轉後的後半段接回去。

    長度 4：slow 停在第 2 個   [1, 2 | 2, 1]
    長度 5：slow 停在第 3 個   [1, 2, 3 | 2, 1]"""),
   ], "O(n)", "O(1)", "", "不破壞輸入"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、陣列", "O(n)", "O(n)", "最簡單"],
    ["二、反轉後半段", "O(n)", "O(1)", "會改動串列"],
    ["三、反轉後還原", "O(n)", "O(1)", "最完整 ✔"]]),
 "edges": [
   "<strong>只有一個節點</strong> → true。",
   "<strong>兩個節點</strong> → 比較兩個值。",
   "<strong>奇數長度</strong> → 中間節點不影響。",
 ],
 "follow": [
   ("h", "還有其他 O(1) 空間以外的做法嗎？"),
   ("c", "遞迴：用遞迴走到串列尾端，回程時和一個從頭前進的全域指標比較。看起來沒有額外資料結構，但遞迴堆疊仍是 O(n)，而且 n = 10⁵ 會超過 Python 的遞迴上限。"),
 ],
 "related": [
   "<strong>第 206 題 反轉鏈結串列</strong>",
   "<strong>第 876 題 鏈結串列的中間節點</strong>",
   "<strong>第 143 題 重排鏈結串列</strong> —— 同樣的「找中點 + 反轉後半」",
 ],
 "check": [
   "O(1) 空間的做法分哪三步？",
   "奇數長度時，中間節點要怎麼處理？",
   "為什麼要把串列還原？",
 ],
})


# ==================== 235. Lowest Common Ancestor of a BST ====================
S["p235"] = '''class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while node:
            if p.val < node.val and q.val < node.val:     # 兩個都在左邊
                node = node.left
            elif p.val > node.val and q.val > node.val:   # 兩個都在右邊
                node = node.right
            else:                                         # ★ 在這裡分岔（或其中一個就是 node）
                return node'''

S["p235_rec"] = '''class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root'''


def _lca_ref(root, p, q):
    def path(t):
        out, nd = [], root
        stack = [(root, [root])]
        while stack:
            nd, pth = stack.pop()
            if nd is t:
                return pth
            for c in (nd.left, nd.right):
                if c:
                    stack.append((c, pth + [c]))
    a, b = path(p), path(q)
    ans = None
    for x, y in zip(a, b):
        if x is y:
            ans = x
    return ans


_p235 = [S.load(x) for x in ("p235", "p235_rec")]
_t = lv([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
_byv = {nd.val: nd for nd in nodes(_t)}
for a, b, want in [(2, 8, 6), (2, 4, 2), (3, 5, 4), (0, 5, 2), (7, 9, 8)]:
    for sol in _p235:
        assert sol.lowestCommonAncestor(_t, _byv[a], _byv[b]).val == want
for _ in range(2000):
    vals = random.sample(range(60), random.randrange(2, 20))
    t = bst(vals)
    ns = nodes(t)
    p, q = random.sample(ns, 2)
    want = _lca_ref(t, p, q)
    for sol in _p235:
        assert sol.lowestCommonAncestor(t, p, q) is want
print("P235 OK")

emit({
 "num": 235, "slug": "lowest-common-ancestor-of-a-binary-search-tree",
 "en": [
   "Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.",
   "According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes <code>p</code> and "
   "<code>q</code> as the lowest node in <code>T</code> that has both <code>p</code> and <code>q</code> as descendants "
   "(where we allow <strong>a node to be a descendant of itself</strong>).”",
 ],
 "zh": [
   "給你一棵<strong>二元搜尋樹</strong>，找出其中兩個節點 <code>p</code>、<code>q</code> 的<strong>最近公共祖先</strong>（LCA）。",
   "最近公共祖先：在樹 <code>T</code> 中，同時以 <code>p</code> 和 <code>q</code> 為子孫的「最低」（最深）節點——"
   "<strong>一個節點也可以是自己的子孫</strong>。",
 ],
 "examples": """範例 1
  輸入：root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
  輸出：6

範例 2
  輸入：root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
  輸出：2
  說明：節點可以是自己的祖先。

範例 3
  輸入：root = [2,1], p = 2, q = 1
  輸出：2""",
 "constraints": [
   "節點數在 <code>[2, 10⁵]</code> 之間",
   "−10⁹ ≤ <code>Node.val</code> ≤ 10⁹",
   "所有 <code>Node.val</code> 互不相同",
   "<code>p != q</code>，而且 <code>p</code>、<code>q</code> 都在樹中",
 ],
 "idea": [
   ("c", """【BST 讓我們知道 p、q 在哪一邊】
    從根往下走，在每個節點 node：
        p、q 都比 node 小 -> LCA 在左子樹
        p、q 都比 node 大 -> LCA 在右子樹
        否則              -> node 就是 LCA

【為什麼「否則」就是答案？】
    「否則」有兩種情況：
    1. p、q 分別在 node 兩側 -> 往任何一邊走都會失去另一個
    2. p 或 q 就是 node 本身 -> node 是自己的子孫

【範例】p = 3, q = 5
    6：都比 6 小 -> 往左
    2：都比 2 大 -> 往右
    4：3 < 4 < 5 -> 分岔，答案 4 ✔

【複雜度】只走一條從根往下的路徑 -> O(h)"""),
 ],
 "approaches": [
   ap("解法一", "遞迴", [
     ("c", S["p235_rec"]),
   ], "O(h)", "O(h)", "", "遞迴深度"),

   ap("解法二", "迭代", [
     ("c", S["p235"]),
   ], "O(h)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、遞迴", "O(h)", "O(h)"],
    ["二、迭代", "O(h)", "O(1) ✔"]]),
 "edges": [
   "<strong>p 是 q 的祖先</strong> → 答案是 p。",
   "<strong>p 或 q 是根</strong> → 答案是根。",
   "<strong>樹是一條鏈</strong> → h = n，迭代版不怕遞迴上限。",
 ],
 "follow": [
   ("h", "如果不是 BST？"),
   ("c", "無法從值判斷方向，就是第 236 題：後序遍歷，看左右子樹各自有沒有找到 p 或 q。"),
 ],
 "related": [
   "<strong>第 236 題 二元樹的最近公共祖先</strong>",
   "<strong>第 1650 題 二元樹的最近公共祖先 III</strong>（付費，有 parent 指標）",
 ],
 "check": [
   "在每個節點，如何決定往左、往右或停下？",
   "為什麼 p、q 分在兩側時，目前節點就是 LCA？",
 ],
})


# ==================== 236. Lowest Common Ancestor of a Binary Tree ====================
S["p236"] = '''class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root is p or root is q:    # 找到其中一個（或走到底）
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:              # ★ p、q 分別在兩側 -> 這裡就是 LCA
            return root
        return left or right            # 只有一側找到：把它往上傳'''

S["p236_parent"] = '''class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root: None}
        stack = [root]
        while p not in parent or q not in parent:     # 建 parent 表，直到兩個都找到
            node = stack.pop()
            for child in (node.left, node.right):
                if child:
                    parent[child] = node
                    stack.append(child)
        ancestors = set()
        while p:                         # p 的所有祖先（含自己）
            ancestors.add(p)
            p = parent[p]
        while q not in ancestors:        # q 往上走，第一個碰到的就是 LCA
            q = parent[q]
        return q'''

_p236 = [S.load(x) for x in ("p236", "p236_parent")]
_t = lv([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
_byv = {nd.val: nd for nd in nodes(_t)}
for a, b, want in [(5, 1, 3), (5, 4, 5), (7, 8, 3), (6, 4, 5)]:
    for sol in _p236:
        assert sol.lowestCommonAncestor(_t, _byv[a], _byv[b]).val == want
for _ in range(2000):
    t = rand_tree(random.randrange(2, 25))
    ns = nodes(t)
    p, q = random.sample(ns, 2)
    want = _lca_ref(t, p, q)
    for sol in _p236:
        assert sol.lowestCommonAncestor(t, p, q) is want
print("P236 OK")

_P236_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">後序遍歷：每個節點回傳「在我的子樹裡找到了 p 或 q 嗎？」</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="300" cy="55" r="15" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="300" y="59" fill="#ff8a65">3</text>
              <circle cx="190" cy="105" r="15" fill="none" stroke="var(--text-muted)"/><text x="190" y="109" fill="var(--text)">5</text>
              <circle cx="410" cy="105" r="15" fill="none" stroke="var(--text-muted)"/><text x="410" y="109" fill="var(--text)">1</text>
              <circle cx="135" cy="155" r="15" fill="none" stroke="var(--text-muted)"/><text x="135" y="159" fill="var(--text)">6</text>
              <circle cx="245" cy="155" r="15" fill="none" stroke="var(--text-muted)"/><text x="245" y="159" fill="var(--text)">2</text>
              <circle cx="370" cy="155" r="15" fill="none" stroke="var(--text-muted)"/><text x="370" y="159" fill="var(--text)">0</text>
              <circle cx="450" cy="155" r="15" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="450" y="159" fill="var(--accent)">8</text>
              <circle cx="220" cy="205" r="15" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="220" y="209" fill="var(--accent)">7</text>
              <circle cx="270" cy="205" r="15" fill="none" stroke="var(--text-muted)"/><text x="270" y="209" fill="var(--text)">4</text>
            </g>
            <g stroke="var(--text-muted)">
              <line x1="288" y1="65" x2="202" y2="95"/><line x1="312" y1="65" x2="398" y2="95"/>
              <line x1="180" y1="117" x2="145" y2="143"/><line x1="200" y1="117" x2="235" y2="143"/>
              <line x1="400" y1="117" x2="380" y2="143"/><line x1="420" y1="117" x2="440" y2="143"/>
              <line x1="238" y1="168" x2="226" y2="191"/><line x1="252" y1="168" x2="264" y2="191"/>
            </g>
            <g font-size="11" fill="var(--gold)">
              <text x="226" y="140">回傳 7</text><text x="150" y="92">回傳 7</text>
              <text x="458" y="132">回傳 8</text><text x="430" y="90">回傳 8</text>
            </g>
            <text x="500" y="200" fill="var(--text-muted)" font-size="11">其他節點回傳 None</text>
            <text x="330" y="44" fill="#ff8a65" font-size="12">左右都不是 None → 3 就是 LCA</text>
            <text x="20" y="246" fill="var(--text)" font-size="12">p = 7、q = 8：7 一路往上傳到 5，8 往上傳到 1，在 3 這裡會合。</text>'''

emit({
 "num": 236, "slug": "lowest-common-ancestor-of-a-binary-tree",
 "en": [
   "Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.",
   "According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes <code>p</code> and "
   "<code>q</code> as the lowest node in <code>T</code> that has both <code>p</code> and <code>q</code> as descendants "
   "(where we allow <strong>a node to be a descendant of itself</strong>).”",
 ],
 "zh": [
   "給你一棵<strong>一般的二元樹</strong>（不是 BST），找出兩個節點 <code>p</code>、<code>q</code> 的最近公共祖先。",
   "一個節點也可以是自己的子孫。",
 ],
 "examples": """範例 1
  輸入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
  輸出：3

範例 2
  輸入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
  輸出：5

範例 3
  輸入：root = [1,2], p = 1, q = 2
  輸出：1""",
 "constraints": [
   "節點數在 <code>[2, 10⁵]</code> 之間",
   "−10⁹ ≤ <code>Node.val</code> ≤ 10⁹",
   "所有 <code>Node.val</code> 互不相同",
   "<code>p != q</code>，而且 <code>p</code>、<code>q</code> 都在樹中",
 ],
 "idea": [
   ("fig", _P236_FIG, "0 0 640 260"),
   ("c", """【沒有 BST 性質，不知道 p、q 在哪一邊 -> 兩邊都要找】

【遞迴函式的含義】
    lca(node) 回傳：
        如果 node 的子樹同時包含 p 和 q -> 它們的 LCA
        如果只包含其中一個               -> 那一個節點
        都不包含                         -> None

【後序處理】
    先問左右子樹：
        左右都有回傳 -> p、q 分在兩側，node 就是 LCA
        只有一側有   -> 把那一側的結果往上傳
        都沒有       -> None

【遇到 p 或 q 就直接回傳，不往下找】
    如果 q 在 p 的子樹裡呢？
    那麼 p 就是答案 —— 而其他地方都找不到 q，
    p 會一路被往上傳到根 ✔
    （題目保證 p、q 都在樹中，這個捷徑才成立）"""),
 ],
 "approaches": [
   ap("解法一", "後序遞迴", [
     ("c", S["p236"]),
   ], "O(n)", "O(h)", "", "遞迴深度", optimal=True),

   ap("解法二", "記錄父節點", [
     ("c", S["p236_parent"]),
     ("c", """【把樹變成「可以往上走」】
    1. DFS 記錄每個節點的父節點
    2. p 往上走到根，沿途放進集合
    3. q 往上走，第一個出現在集合裡的就是 LCA

    和第 160 題「兩個串列的交點」是同一個問題：
    p、q 往上的路徑是兩條會合的串列。"""),
   ], "O(n)", "O(n)", "", "迭代，不怕深樹"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、後序遞迴", "O(n)", "O(h)", "最簡潔 ✔"],
    ["二、父節點表", "O(n)", "O(n)", "樹很深時不怕遞迴上限"]]),
 "edges": [
   "<strong>p 是 q 的祖先</strong> → 回傳 p（遇到 p 就停）。",
   "<strong>p、q 其中一個是根</strong> → 回傳根。",
   "<strong>樹很深</strong>（一條鏈，10⁵ 層）→ Python 遞迴會爆，用解法二。",
   "<strong>用 <code>is</code> 比較節點</strong>，不要用值（題目保證值不重複，但比身分更保險）。",
 ],
 "follow": [
   ("h", "追問：如果 p 或 q 不一定在樹中？"),
   ("c", "第 1644 題（付費）：不能再「遇到 p 就停」，必須完整遍歷，另外記錄兩個節點是否都真的找到。"),
   ("h", "追問：大量 LCA 查詢？"),
   ("c", "倍增法（binary lifting）：預處理 O(n log n)，每次查詢 O(log n)；或 Tarjan 離線演算法、歐拉序 + RMQ。"),
 ],
 "related": [
   "<strong>第 235 題 二元搜尋樹的最近公共祖先</strong>",
   "<strong>第 1644、1650、1676 題</strong>（付費）—— LCA 的各種變化",
   "<strong>第 1123 題 最深葉節點的最近公共祖先</strong>",
 ],
 "check": [
   "遞迴函式的回傳值代表什麼？",
   "左右子樹都有回傳時，為什麼目前節點就是答案？",
   "為什麼遇到 p 就可以直接回傳，不用再往下找 q？",
 ],
})
