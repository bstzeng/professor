# -*- coding: utf-8 -*-
"""第 67–70 題。"""
import random, math
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(67)

# ==================== 67. Add Binary ====================
S["p67_manual"] = '''class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        out = []

        # 三個條件的 or：只要還有位數或還有進位就繼續
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i]); i -= 1
            if j >= 0:
                total += int(b[j]); j -= 1

            out.append(str(total % 2))     # 這一位
            carry = total // 2             # 進位

        return "".join(reversed(out))'''

S["p67_bits"] = '''class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 只用位元運算做加法（不用 + 號）
        x, y = int(a, 2), int(b, 2)
        while y:
            carry = (x & y) << 1     # 兩邊都是 1 的位置 -> 進位
            x = x ^ y                # 不進位的加法 = XOR
            y = carry
        return bin(x)[2:]'''

S["p67_builtin"] = '''class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]'''

_p67 = [S.load(k) for k in ("p67_manual", "p67_bits", "p67_builtin")]
for a, b in [("11", "1"), ("1010", "1011"), ("0", "0"), ("1", "1"),
             ("0", "1"), ("1111", "1"), ("100", "110010")]:
    e = bin(int(a, 2) + int(b, 2))[2:]
    for sol in _p67:
        assert sol.addBinary(a, b) == e, ("P67", a, b, sol, sol.addBinary(a, b), e)
for _ in range(5000):
    a = bin(random.randint(0, 2**random.randint(1, 20)))[2:]
    b = bin(random.randint(0, 2**random.randint(1, 20)))[2:]
    e = bin(int(a, 2) + int(b, 2))[2:]
    for sol in _p67:
        assert sol.addBinary(a, b) == e, ("P67", a, b, sol)
print("P67 solutions OK")

_P67_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">二進位直式加法：1010 + 1011 = 10101</text>
            <g font-family="monospace" font-size="18" text-anchor="middle">
              <text x="300" y="58" fill="var(--gold)" font-size="13">進位</text>
              <text x="360" y="58" fill="var(--gold)">1</text>
              <text x="400" y="58" fill="var(--gold)">0</text>
              <text x="440" y="58" fill="var(--gold)">1</text>
              <text x="480" y="58" fill="var(--gold)">0</text>

              <text x="360" y="94" fill="var(--accent)">1</text>
              <text x="400" y="94" fill="var(--accent)">0</text>
              <text x="440" y="94" fill="var(--accent)">1</text>
              <text x="480" y="94" fill="var(--accent)">0</text>

              <text x="322" y="126" fill="var(--text-muted)">+</text>
              <text x="360" y="126" fill="var(--accent)">1</text>
              <text x="400" y="126" fill="var(--accent)">0</text>
              <text x="440" y="126" fill="var(--accent)">1</text>
              <text x="480" y="126" fill="var(--accent)">1</text>
            </g>
            <line x1="310" y1="140" x2="500" y2="140" stroke="var(--text-muted)" stroke-width="1.5"/>
            <g font-family="monospace" font-size="18" text-anchor="middle">
              <text x="320" y="170" fill="#ff8a65">1</text>
              <text x="360" y="170" fill="#ff8a65">0</text>
              <text x="400" y="170" fill="#ff8a65">1</text>
              <text x="440" y="170" fill="#ff8a65">0</text>
              <text x="480" y="170" fill="#ff8a65">1</text>
            </g>
            <g font-family="monospace" font-size="12" fill="var(--text-muted)">
              <text x="40" y="94">第 0 位（最右）： 0 + 1 + 0 = 1　→ 寫 1，進位 0</text>
              <text x="40" y="118">第 1 位：　　　　 1 + 1 + 0 = 2　→ 寫 0，進位 1</text>
              <text x="40" y="142">第 2 位：　　　　 0 + 0 + 1 = 1　→ 寫 1，進位 0</text>
              <text x="40" y="166">第 3 位：　　　　 1 + 1 + 0 = 2　→ 寫 0，進位 1</text>
              <text x="40" y="190">收尾：　　　　　 進位還是 1　　→ 寫 1</text>
            </g>
            <text x="20" y="226" fill="var(--gold)" font-size="12">和十進位完全一樣，只是「滿 2 進 1」而不是「滿 10 進 1」。</text>
            <text x="20" y="250" fill="var(--text-muted)" font-size="12">所以同一份程式碼，把 % 2 和 // 2 換成 % 10 和 // 10 就是十進位版（第 415 題）。</text>'''

emit({
 "num": 67, "slug": "add-binary",
 "en": [
   "Given two binary strings <code>a</code> and <code>b</code>, return <em>their sum as a "
   "binary string</em>.",
 ],
 "zh": [
   "給你兩個<strong>二進位</strong>字串 <code>a</code> 和 <code>b</code>，"
   "回傳它們的和（同樣用二進位字串表示）。",
 ],
 "pre": [
   ("note", "就是直式加法，只是進位變成「滿 2」", [
     ("c", """十進位：  滿 10 進 1    digit = total % 10,  carry = total // 10
二進位：  滿 2  進 1    digit = total % 2,   carry = total // 2

每一位的三種可能：
    0 + 0 = 0           寫 0，不進位
    0 + 1 = 1           寫 1，不進位
    1 + 1 = 10 (二進位)  寫 0，進位 1

    加上上一位的進位之後，total 最大是 1 + 1 + 1 = 3
        3 % 2 = 1，3 // 2 = 1    寫 1，進位 1

所以 total 永遠在 0..3 之間，只有四種情況。

和第 66 題（Plus One）、第 415 題（Add Strings）、
第 2 題（Add Two Numbers）是同一個骨架 ——
只是資料的載體（陣列、字串、鏈結串列）和基底（2 或 10）不同。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：a = "11", b = "1"
  輸出："100"
  說明：3 + 1 = 4

範例 2
  輸入：a = "1010", b = "1011"
  輸出："10101"
  說明：10 + 11 = 21""",
 "constraints": [
   "1 ≤ <code>a.length</code>, <code>b.length</code> ≤ 10⁴",
   "<code>a</code> 和 <code>b</code> 只含 <code>'0'</code> 和 <code>'1'</code>",
   "每個字串<strong>不含前導零</strong>，除非它本身就是 <code>\"0\"</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>長度到 10⁴</strong> —— 一萬位二進位數，大約是 10³⁰¹⁰。"
       "<strong>遠超任何整數型別</strong>（在 C/Java 裡）。"
       "Python 可以硬轉（<code>int(a, 2)</code>），但那繞過了題目的用意。",
       "<strong>兩個字串長度可以不同</strong> —— 所以迴圈條件要用 "
       "<code>i &gt;= 0 or j &gt;= 0</code>（<strong>or</strong> 不是 and）。",
       "<strong>沒有前導零</strong>，所以輸出也不該有。"
       "手動版天然不會產生（只在 carry 還在時才多寫一位）。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P67_FIG, "0 0 640 262"),
 ],
 "approaches": [
   ap("解法一", "手寫直式加法（面試該寫的）", [
     ("c", S["p67_manual"]),
     ("h", "<code>while i &gt;= 0 or j &gt;= 0 or carry</code> —— 三個條件的 or"),
     ("c", """這一行同時處理了三件事：

  i >= 0     a 還有位數沒處理
  j >= 0     b 還有位數沒處理
  carry      還有進位要寫出來

三者只要有一個成立就繼續。

為什麼 carry 也要放在條件裡？
    "1" + "1" = "10"
    處理完第 0 位之後 i = j = -1，但 carry = 1
    如果條件只有 i >= 0 or j >= 0，迴圈會停，
    最高位的 1 就掉了 -> 答案變成 "0" ✘

而寫成 and 的話，短的那個字串用完就會停 ——
"1010" + "1" 會只算一位。

這個「三條件 or」的寫法，是所有大數加法的標準骨架。
第 2、415、989 題都一樣。"""),
     ("h", "為什麼用 list + reverse 而不是字串前綴相加？"),
     "因為我們是<strong>從低位算到高位</strong>，但輸出要<strong>高位在前</strong>。",
     ("c", """錯誤（但直覺）的寫法：
    result = str(total % 2) + result

    每次都在字串前面插入，而 Python 的字串不可變 ——
    每次都要複製整條字串。
    n 位數就是 O(n²)。
    在 n = 10⁴ 時是 10⁸ 次字元複製，會 TLE。

正確寫法：
    out.append(...)         O(1) 攤還
    ...
    "".join(reversed(out))  最後一次 O(n)

    總共 O(n) ✔

「先 append 再反轉」是所有「從低位算到高位」的題目的標準做法。""",),
     "<strong>複雜度 O(max(m, n))</strong>，而且是原地思考，不建中間的大整數。"
     "<strong>這個版本可以逐字翻譯成 C 或 Java。</strong>",
   ], "O(max(m,n))", "O(max(m,n))", "每一位處理一次", "輸出的 list", optimal=True),

   ap("解法二", "位元運算（不用 + 號）", [
     "如果面試官追問「不准用加號呢？」——"
     "<strong>加法可以完全用 XOR 和 AND 實作。</strong>",
     ("c", S["p67_bits"]),
     ("h", "為什麼 XOR 是「不進位的加法」？"),
     ("c", """逐位看：
    0 + 0 = 0    0 XOR 0 = 0  ✔
    0 + 1 = 1    0 XOR 1 = 1  ✔
    1 + 0 = 1    1 XOR 0 = 1  ✔
    1 + 1 = 10   1 XOR 1 = 0  ✔（低位是 0，進位另外處理）

所以 x ^ y 就是「每一位各自相加，但不處理進位」。

而進位發生在「兩邊都是 1」的位置：
    (x & y) 標出所有「兩邊都是 1」的位
    << 1 把它們往左移一位（進位是往高位傳的）

然後把「不進位的和」和「進位」再加一次 ——
遞迴下去，直到沒有進位為止。

    x = 1010, y = 1011
    輪 1: carry = (1010 & 1011) << 1 = 1010 << 1 = 10100
          x = 1010 ^ 1011 = 0001
          y = 10100
    輪 2: carry = (00001 & 10100) << 1 = 0
          x = 00001 ^ 10100 = 10101
          y = 0
    結束，x = 10101 ✔

為什麼一定會終止？
    每一輪 carry 至少往左移一位，
    所以最多 O(位數) 輪之後 carry 一定變成 0。"""),
     "<strong>這就是 CPU 的加法器（ripple-carry adder）的邏輯</strong> —— "
     "只是硬體是平行做的，而我們這裡是迭代。",
     "<strong>但這個版本在這題有點作弊</strong>："
     "它用了 <code>int(a, 2)</code> 把字串轉成整數，"
     "而 Python 的大整數本來就處理了任意長度。"
     "在 C 裡這個技巧只能用在固定寬度的整數上。"
     "<strong>它的價值是回答「不准用 +」這個追問（第 371 題），而不是解本題。</strong>",
   ], "O(位數)", "O(1)", "每輪 carry 往左移一位", "Python 大整數"),

   ap("解法三", "內建函式（一行，但學不到東西）", [
     ("c", S["p67_builtin"]),
     ("c", """int(a, 2)    把二進位字串轉成整數（第二個參數是基底）
bin(n)       把整數轉成二進位字串，但會帶 "0b" 前綴
[2:]         去掉那個前綴

    bin(21) -> "0b10101"
    [2:]    -> "10101" ✔

其他好用的轉換：
    int("ff", 16) -> 255       十六進位
    int("777", 8) -> 511       八進位
    oct(511)      -> "0o777"
    hex(255)      -> "0xff"
    f"{21:b}"     -> "10101"   格式化，不帶前綴（比 bin()[2:] 乾淨）"""),
     "<strong>在 LeetCode 上會過</strong>（Python 的大整數撐得住 10⁴ 位），"
     "<strong>但在面試時等於沒答</strong>。"
     "<strong>而且在 C/Java 裡根本不可能</strong>。",
     "正確的做法：<strong>先寫解法一，再說「Python 其實一行就好，但那用到了任意精度整數」</strong>。",
   ], "O(n)", "O(n)", "轉換 + 大整數加法", "大整數"),
 ],
 "compare": (["解法", "時間", "可翻譯成 C？", "行數", "備註"],
   [["一、手寫直式", "O(max(m,n))", "✔", "14", "面試預設"],
    ["二、位元運算", "O(位數)", "△ 固定寬度才行", "7", "回答「不准用 +」"],
    ["三、內建函式", "O(n)", "✘", "1", "會過但沒展示"]]),
 "edges": [
   "<strong>長度不同</strong>：<code>(\"1010\", \"1\")</code> → <code>\"1011\"</code>。"
   "<strong>迴圈條件用 <code>and</code> 會錯。</strong>",
   "<strong>最後還有進位</strong>：<code>(\"1\", \"1\")</code> → <code>\"10\"</code>；"
   "<code>(\"1111\", \"1\")</code> → <code>\"10000\"</code>。"
   "<strong>條件裡沒有 <code>or carry</code> 會錯。</strong>",
   "<strong>兩個都是 0</strong>：<code>(\"0\", \"0\")</code> → <code>\"0\"</code>。"
   "迴圈跑一次（total = 0），輸出 <code>\"0\"</code> ✔",
   "<strong>其中一個是 0</strong>：<code>(\"0\", \"1\")</code> → <code>\"1\"</code>。",
   "<strong>長度差很多</strong>：<code>(\"100\", \"110010\")</code> → <code>\"110110\"</code>。",
   "<strong>用字串前綴相加</strong>：在 n = 10⁴ 時會 O(n²) 而 TLE。",
 ],
 "follow": [
   ("h", "追問一：如果是任意基底呢？"),
   "把 <code>% 2</code> 和 <code>// 2</code> 換成 <code>% base</code> 和 <code>// base</code>，"
   "並且處理「數字字元」和「數值」的轉換（例如十六進位的 <code>'a'</code> 對應 10）。"
   "<strong>骨架完全不變。</strong>",
   ("h", "追問二：如果不准用 <code>+</code> 呢？"),
   "第 371 題（Sum of Two Integers）。就是解法二的 XOR / AND 技巧。"
   "<strong>但在 Java 或 C++ 裡要小心負數</strong> —— "
   "有號整數的右移和溢位是 undefined behavior 或實作定義的，"
   "標準做法是全程用無號型別運算，最後再轉回來。"
   "<strong>在 Python 裡更麻煩</strong>，因為整數是任意精度的，"
   "負數的二補數表示是「無限長」的，要手動遮罩到 32 位。",
   ("h", "追問三：這一家題目的共同骨架是什麼？"),
   ("c", """第 2 題   Add Two Numbers     鏈結串列，低位在前，基底 10
第 43 題  Multiply Strings    字串，高位在前，乘法
第 66 題  Plus One            陣列，高位在前，加 1
第 67 題  Add Binary          字串，高位在前，基底 2
第 415 題 Add Strings         字串，高位在前，基底 10
第 989 題 Add to Array-Form   陣列 + 整數

共同骨架：
    carry = 0
    while 還有位數 or carry:
        total = carry + (這一位的兩個數)
        寫下 total % base
        carry = total // base

差別只在：
    - 資料結構（陣列／字串／鏈結串列）
    - 方向（低位在前還是高位在前）
    - 基底

    只要把這個骨架記熟，這六題就都是同一題。""",),
 ],
 "related": [
   "<strong>第 2 題 Add Two Numbers</strong> —— 鏈結串列版",
   "<strong>第 415 題 Add Strings</strong> —— 十進位字串版",
   "<strong>第 66 題 Plus One</strong> —— 陣列版",
   "<strong>第 371 題 Sum of Two Integers</strong> —— 只用位元運算",
   "<strong>第 43 題 Multiply Strings</strong> —— 大數乘法",
 ],
 "check": [
   "<code>while i &gt;= 0 or j &gt;= 0 or carry</code> 的三個條件各自防什麼？"
   "把 <code>or carry</code> 拿掉，哪一筆測資會錯？",
   "為什麼要「先 append 再 reverse」而不是「每次在字串前面插入」？在 n = 10⁴ 時差多少？",
   "為什麼 XOR 是「不進位的加法」？進位為什麼是 <code>(x &amp; y) &lt;&lt; 1</code>？",
   "把 <code>% 2</code> 換成 <code>% 10</code> 之後，這份程式碼變成哪一題的解？",
 ],
})
print("P67 written")

# ==================== 68. Text Justification ====================
S["p68"] = '''class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []          # 目前這一行放了哪些單字
        length = 0         # 目前這一行「單字本身」的總字元數（不含空格）

        for w in words:
            # 放進來的話，最少需要 length + len(w) + len(line) 個字元
            # （len(line) 是「至少每個單字之間一個空格」的數量）
            if length + len(w) + len(line) > maxWidth:
                res.append(self._justify(line, length, maxWidth))
                line, length = [], 0
            line.append(w)
            length += len(w)

        # 最後一行：左對齊，右邊補空格
        last = " ".join(line)
        res.append(last + " " * (maxWidth - len(last)))
        return res

    def _justify(self, line: List[str], length: int, maxWidth: int) -> str:
        """把一整行做「左右對齊」（不是最後一行）"""
        if len(line) == 1:
            # 只有一個單字 -> 左對齊
            return line[0] + " " * (maxWidth - length)

        total_spaces = maxWidth - length
        gaps = len(line) - 1
        base, extra = divmod(total_spaces, gaps)   # 每個縫隙的基本量 + 餘數

        out = []
        for i, w in enumerate(line[:-1]):
            # 左邊的 extra 個縫隙各多放一個空格
            out.append(w)
            out.append(" " * (base + (1 if i < extra else 0)))
        out.append(line[-1])
        return "".join(out)'''

_p68 = S.load("p68")


def _p68_check(words, width, res):
    """獨立驗證：每一行都必須符合規格。"""
    # 1. 每一行長度都剛好是 width
    for ln in res:
        assert len(ln) == width, ("長度不對", repr(ln), width)
    # 2. 把所有行的單字接起來，必須剛好是原本的 words
    got = []
    for ln in res:
        got += ln.split()
    assert got == words, ("單字對不上", got, words)
    # 3. 貪婪：每一行都必須「再多放一個單字就會超過」
    idx = 0
    for k, ln in enumerate(res):
        cnt = len(ln.split())
        idx += cnt
        if idx < len(words):
            cur = sum(len(w) for w in words[idx - cnt:idx])
            nxt = words[idx]
            assert cur + cnt + len(nxt) > width, ("不夠貪婪", k, ln)
    # 4. 非最後一行：若有多個單字，必須左右對齊（左邊的縫隙 >= 右邊的）
    for ln in res[:-1]:
        parts = ln.split()
        if len(parts) <= 1:
            assert ln == parts[0] + " " * (width - len(parts[0])), ("單字行", repr(ln))
            continue
        assert not ln.endswith(" "), ("非最後一行不該有尾隨空格", repr(ln))
        gaps = []
        i = 0
        while i < len(ln):
            if ln[i] == " ":
                j = i
                while j < len(ln) and ln[j] == " ":
                    j += 1
                gaps.append(j - i)
                i = j
            else:
                i += 1
        assert gaps == sorted(gaps, reverse=True), ("空格沒有左多右少", repr(ln), gaps)
        assert max(gaps) - min(gaps) <= 1, ("空格分配不均", repr(ln), gaps)
    # 5. 最後一行：左對齊，單字間剛好一個空格
    last = res[-1]
    assert last.rstrip() == " ".join(last.split()), ("最後一行沒有左對齊", repr(last))


_EX1 = _p68.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
assert _EX1 == ["This    is    an", "example  of text", "justification.  "], _EX1
_EX2 = _p68.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
assert _EX2 == ["What   must   be", "acknowledgment  ", "shall be        "], _EX2
_EX3 = _p68.fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
     "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20)
assert _EX3 == ["Science  is  what we", "understand      well",
                "enough to explain to", "a  computer.  Art is",
                "everything  else  we", "do                  "], _EX3

_WORDPOOL = ["a", "bb", "ccc", "dddd", "eeeee", "ffffff", "ggg", "hh"]
for _ in range(3000):
    width = random.randint(6, 14)
    ws = [random.choice([w for w in _WORDPOOL if len(w) <= width])
          for _ in range(random.randint(1, 8))]
    r = _p68.fullJustify(list(ws), width)
    _p68_check(ws, width, r)
print("P68 solutions OK")

_P68_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">maxWidth = 16，這一行有 3 個單字：This(4) is(2) an(2)，共 8 個字元</text>
            <text x="20" y="48" fill="var(--text-muted)" font-size="12">要補的空格總數 = 16 − 8 = 8，縫隙數 = 3 − 1 = 2</text>
            <g font-family="monospace" font-size="16">
              <text x="40" y="86" fill="var(--gold)">divmod(8, 2) = (4, 0)　→ 每個縫隙 4 格，沒有餘數</text>
              <text x="40" y="120" fill="var(--accent)">&quot;This&quot;</text>
              <text x="130" y="120" fill="#ff8a65">&quot;    &quot;</text>
              <text x="230" y="120" fill="var(--accent)">&quot;is&quot;</text>
              <text x="290" y="120" fill="#ff8a65">&quot;    &quot;</text>
              <text x="390" y="120" fill="var(--accent)">&quot;an&quot;</text>
              <text x="470" y="120" fill="var(--text-muted)" font-size="12">= &quot;This    is    an&quot;</text>
            </g>
            <line x1="20" y1="142" x2="620" y2="142" stroke="var(--border)"/>
            <text x="20" y="170" fill="var(--text-muted)" font-size="12">如果除不盡：What(4) must(4) be(2)，共 10 個字元，要補 6 格，2 個縫隙</text>
            <g font-family="monospace" font-size="16">
              <text x="40" y="206" fill="var(--gold)">divmod(6, 2) = (3, 0)　→ 剛好，各 3 格</text>
            </g>
            <text x="20" y="238" fill="var(--text-muted)" font-size="12">再看一個除不盡的：a(1) computer.(9) Art(3) is(2)，共 15 個字元，maxWidth = 20</text>
            <g font-family="monospace" font-size="16">
              <text x="40" y="274" fill="var(--gold)">divmod(5, 3) = (1, 2)　→ 前 2 個縫隙放 1+1 = 2 格，最後 1 個放 1 格</text>
              <text x="40" y="304" fill="var(--accent)">&quot;a  computer.  Art is&quot;</text>
              <text x="380" y="304" fill="#ff8a65" font-size="12">← 左邊的縫隙比較寬</text>
            </g>
            <text x="20" y="336" fill="var(--gold)" font-size="12">規則：空格不能平均分配時，「左邊的縫隙要放比較多」—— divmod 的餘數從左邊開始分。</text>'''

emit({
 "num": 68, "slug": "text-justification",
 "en": [
   "Given an array of strings <code>words</code> and a width <code>maxWidth</code>, format "
   "the text such that each line has exactly <code>maxWidth</code> characters and is fully "
   "(left and right) justified.",
   "You should pack your words in a <strong>greedy approach</strong>; that is, pack as many "
   "words as you can in each line. Pad extra spaces <code>' '</code> when necessary.",
   "Extra spaces between words should be distributed as evenly as possible. If the number of "
   "spaces on a line does not divide evenly between words, the empty slots on the "
   "<strong>left</strong> will be assigned more spaces than the slots on the right.",
   "For the <strong>last line</strong> of text, it should be left-justified, and no extra "
   "space is inserted between words.",
 ],
 "zh": [
   "給你一個字串陣列 <code>words</code> 和一個寬度 <code>maxWidth</code>，"
   "把文字排版成每一行<strong>剛好 <code>maxWidth</code> 個字元</strong>、"
   "而且<strong>左右對齊</strong>的樣子。",
   "排版方式要<strong>貪婪</strong>：每一行盡量塞進最多的單字。",
   "單字之間的空格要<strong>盡量平均分配</strong>。"
   "如果除不盡，<strong>左邊的縫隙要比右邊多</strong>。",
   "<strong>最後一行</strong>要<strong>左對齊</strong>，單字之間只放一個空格，右邊補滿空格。",
 ],
 "pre": [
   ("note", "這題不難，但規則多到一定會漏掉一條", [
     ("c", """五條規則，缺一不可：

  1. 貪婪分行
     每一行盡量塞，直到「再多一個單字就超過 maxWidth」。

  2. 判斷「塞不塞得下」的公式
     現有單字總長 + 新單字長度 + 現有單字數 > maxWidth  ->  塞不下

     為什麼是「+ 現有單字數」而不是「+ 現有單字數 - 1」？
     因為新單字進來之後，縫隙數會變成「現有單字數」。
         已有 2 個單字，再加 1 個 -> 3 個單字 -> 2 個縫隙
         而「現有單字數」= 2 ✔

  3. 一般行：左右對齊，空格盡量平均，左邊多
     空格總數 = maxWidth - 單字總長
     縫隙數   = 單字數 - 1
     base, extra = divmod(空格總數, 縫隙數)
     左邊 extra 個縫隙各放 base + 1，其餘放 base

  4. 只有一個單字的行：左對齊（右邊補空格）
     因為沒有「縫隙」可以放空格，divmod 會除以零。

  5. 最後一行：左對齊，單字間一個空格，右邊補滿

規則 4 和 5 是兩個「例外」，也是最常被漏掉的。"""),
     "<strong>這題在 LeetCode 上被標成 Hard，但它不是演算法難</strong> —— "
     "<strong>它是「規格實作題」</strong>。"
     "真實世界的很多工作就長這樣：規則本身不難，但要一條不漏地實作出來。",
   ]),
 ],
 "examples": """範例 1
  輸入：words = ["This","is","an","example","of","text","justification."]
        maxWidth = 16
  輸出：
    "This    is    an"
    "example  of text"
    "justification.  "

範例 2
  輸入：words = ["What","must","be","acknowledgment","shall","be"]
        maxWidth = 16
  輸出：
    "What   must   be"
    "acknowledgment  "     <- 只有一個單字，左對齊
    "shall be        "     <- 最後一行，左對齊
  說明：注意第二行不是 "acknowledgment" 置中或右對齊。

範例 3
  輸入：words = ["Science","is","what","we","understand","well","enough",
                "to","explain","to","a","computer.","Art","is",
                "everything","else","we","do"]
        maxWidth = 20
  輸出：
    "Science  is  what we"
    "understand      well"
    "enough to explain to"
    "a  computer.  Art is"     <- 5 格分給 3 個縫隙：2, 2, 1
    "everything  else  we"
    "do                  \"""",
 "constraints": [
   "1 ≤ <code>words.length</code> ≤ 300",
   "1 ≤ <code>words[i].length</code> ≤ 20",
   "<code>words[i]</code> 只含英文字母和符號",
   "1 ≤ <code>maxWidth</code> ≤ 100",
   "<code>words[i].length ≤ maxWidth</code>（<strong>保證每個單字都塞得下一行</strong>）",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>保證每個單字都不超過 maxWidth</strong> —— "
       "所以不用處理「一個單字本身就太長」（不用斷字）。"
       "<strong>真實的排版引擎必須處理，那複雜得多。</strong>",
       "<strong>規模很小</strong>（300 個單字、寬度 100），效率完全不是問題。"
       "這題百分之百考<strong>規格的完整實作</strong>。",
       "<strong>單字可以含符號</strong>（例如 <code>\"justification.\"</code>），"
       "但那不影響邏輯 —— 我們只看長度。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P68_FIG, "0 0 640 350"),
 ],
 "approaches": [
   ap("解法", "貪婪分行 + 分開處理三種行（唯一解）", [
     ("c", S["p68"]),
     ("h", "① 分行的判斷式"),
     ("c", """if length + len(w) + len(line) > maxWidth:

    length      目前這一行「單字本身」的總長（不含任何空格）
    len(w)      新單字的長度
    len(line)   目前有幾個單字 = 加入新單字後的「縫隙數」

    所以這個式子算的是：
        「如果把 w 加進來，這一行至少需要幾個字元」
        （每個縫隙至少一個空格）

    超過 maxWidth 就表示塞不下，要先把現有的輸出。

驗算：line = ["This", "is"]，length = 6，w = "an"，maxWidth = 16
    6 + 2 + 2 = 10 <= 16  ->  塞得下 ✔
    加入後 line = ["This","is","an"]，length = 8

    下一個 w = "example"（長度 7）
    8 + 7 + 3 = 18 > 16  ->  塞不下，這一行到此為止 ✔

    注意 len(line) 此時是 3（加入 example 後會有 3 個縫隙）。"""),
     ("h", "② 空格的分配：<code>divmod</code>"),
     ("c", """total_spaces = maxWidth - length      要補的空格總數
gaps = len(line) - 1                  縫隙數
base, extra = divmod(total_spaces, gaps)

    base   每個縫隙至少放幾個
    extra  還剩幾個要分出去 -> 給「最左邊的 extra 個縫隙」各多一個

例：total_spaces = 5, gaps = 3
    divmod(5, 3) = (1, 2)
    縫隙 0： 1 + 1 = 2
    縫隙 1： 1 + 1 = 2
    縫隙 2： 1 + 0 = 1
    總共 2 + 2 + 1 = 5 ✔ 而且左邊比較多 ✔

程式碼裡的 (1 if i < extra else 0) 就是在做這件事。"""),
     ("h", "③ 兩個例外"),
     ("c", """例外 1：這一行只有一個單字
    gaps = 0 -> divmod 會 ZeroDivisionError！
    而且規格說要「左對齊」。

    if len(line) == 1:
        return line[0] + " " * (maxWidth - length)

例外 2：最後一行
    規格明確說「左對齊，單字間一個空格」。

    last = " ".join(line)
    res.append(last + " " * (maxWidth - len(last)))

    注意最後一行「不呼叫 _justify」——
    它走的是完全不同的邏輯。

這兩個例外是本題最常見的失分點。
範例 2 的第二行（"acknowledgment  "）就是專門用來抓例外 1 的。"""),
     ("h", "為什麼分行要用「貪婪」？"),
     "因為題目明確要求。"
     "<strong>但值得知道：貪婪分行不是「最美」的排版。</strong>"
     "TeX 的 Knuth-Plass 演算法用 DP 對「整個段落」做最佳化，"
     "讓每一行的「鬆緊度（badness）」的總和最小 —— "
     "結果是空格分布更均勻、更少的難看行。",
     "<strong>代價是 O(n²) 的 DP 而不是 O(n) 的貪婪</strong>，"
     "而且必須看完整段才能決定第一行 —— "
     "這對「邊打字邊排版」的即時場景不適用。"
     "<strong>瀏覽器的 CSS 文字排版用的就是貪婪（所以有時候會看到很鬆的行）。</strong>",
     ("h", "複雜度"),
     "每個單字被處理一次，每一行的組裝和它的長度成正比。"
     "總共 <strong>O(總字元數)</strong> = O(n × maxWidth) 最壞。",
   ], "O(總字元數)", "O(maxWidth)", "每個單字處理一次",
      "一行的緩衝；不算輸出", optimal=True),
 ],
 "compare": (["行的種類", "對齊方式", "空格分配", "為什麼特殊"],
   [["一般行（多個單字）", "左右對齊", "divmod 平均分，左邊多", "—"],
    ["一般行（一個單字）", "左對齊", "全部補在右邊", "gaps = 0，不能除"],
    ["最後一行", "左對齊", "單字間一格，其餘補右邊", "規格明確要求"]]),
 "edges": [
   "<strong>只有一個單字</strong>：<code>([\"a\"], 5)</code> → <code>[\"a    \"]</code>（最後一行規則）。",
   "<strong>一行只放得下一個單字</strong>：範例 2 的 <code>\"acknowledgment  \"</code>。"
   "<strong>沒有特判會 ZeroDivisionError。</strong>",
   "<strong>剛好填滿</strong>：單字總長 + 縫隙數 剛好等於 maxWidth，"
   "此時 <code>base = 1, extra = 0</code>。",
   "<strong>除不盡</strong>：範例 3 的 <code>\"a  computer.  Art is\"</code>（2, 2, 1）。"
   "<strong>左邊必須比較多。</strong>",
   "<strong>最後一行剛好滿</strong>：不用補空格，但公式 "
   "<code>\" \" * (maxWidth - len(last))</code> 會是 <code>\" \" * 0</code>，自然正確。",
   "<strong>最後一行只有一個單字</strong>：走最後一行的規則（左對齊），不是 <code>_justify</code>。",
   "<strong>每一行的長度</strong>：<strong>永遠必須剛好是 maxWidth</strong>。"
   "<strong>寫完之後先檢查這一點，是最快的除錯方法。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果單字可能比 maxWidth 還長呢？"),
   "就要<strong>斷字（hyphenation）</strong>。"
   "真實的排版引擎用 Liang 的斷字演算法（TeX 用的那個）—— "
   "它用一套「模式（pattern）」字典來判斷一個單字可以在哪裡斷。"
   "簡化的做法是「硬斷」：填滿一行就換行，不管語意。",
   ("h", "追問二：怎麼做出「更美」的排版？"),
   ("c", """Knuth-Plass（TeX 的段落排版演算法）：

  1. 定義每一行的「badness」
     badness = (空格被拉伸或壓縮的程度)³
     完全不用拉伸 -> badness 0
     拉得越開，懲罰越重（三次方讓極端情況被強烈避免）

  2. 用 DP 找「整個段落的 badness 總和最小」的斷行方式
     dp[i] = 到第 i 個單字為止的最小總 badness
     dp[i] = min over j (dp[j] + badness(j..i))

  3. 加上額外的懲罰項：
     連續兩行的鬆緊度差太多、
     連續多行都在同一個地方斷字、
     段落最後一行太短（寡行）…

複雜度 O(n²)，但可以用「只考慮合理的斷點」剪到接近 O(n)。

貪婪 vs DP 的差別在實際排版上非常明顯 ——
這是「局部最優 ≠ 全域最優」最貼近日常的例子。
（把 Word 和 LaTeX 排出來的同一段文字放在一起看就知道了。）""",),
   ("h", "追問三：為什麼「左邊的縫隙要放比較多」？"),
   "這是西文排版的傳統慣例 —— 讓行首看起來比較穩定。"
   "<strong>但這是規格規定的，不是數學必然</strong>。"
   "有些排版系統會反過來，有些會隨機分配以避免「空格河流」"
   "（連續幾行的空格剛好對齊，在版面上形成一條難看的白色通道）。",
   "<strong>面試時遇到這種「看起來任意」的規則，照做就好，不要自己發明。</strong>"
   "但如果能說出「這是排版慣例，不同系統可能不同」，會顯示你有更廣的視野。",
 ],
 "related": [
   "<strong>第 6 題 Zigzag Conversion</strong> —— 另一個排版／索引計算題",
   "<strong>第 1592 題 Rearrange Spaces Between Words</strong> —— 簡化版的空格分配",
   "<strong>第 418 題 Sentence Screen Fitting</strong> —— 反過來問「螢幕能放幾遍」",
 ],
 "check": [
   "分行的判斷式為什麼是 <code>length + len(w) + len(line)</code>？"
   "最後那一項為什麼不用減 1？",
   "「只有一個單字的行」為什麼要特判？不特判會發生什麼錯誤？",
   "<code>divmod(5, 3)</code> 的結果怎麼轉成「2, 2, 1」這樣的空格分配？",
   "寫完之後最快的自我檢查是什麼？",
 ],
})
print("P68 written")
