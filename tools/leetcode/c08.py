# -*- coding: utf-8 -*-
"""第 8–9 題。"""
import random, re
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(8)
INT_MIN, INT_MAX = -2**31, 2**31 - 1

# ==================== 8. String to Integer (atoi) ====================
S["p8_step"] = '''class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        i, n = 0, len(s)

        # 第 1 步：跳過開頭的空白（只有 ' '，不含 \\t \\n）
        while i < n and s[i] == " ":
            i += 1
        if i == n:
            return 0

        # 第 2 步：讀符號，最多一個
        sign = 1
        if s[i] in "+-":
            if s[i] == "-":
                sign = -1
            i += 1

        # 第 3 步：讀連續的數字，遇到非數字立刻停
        num = 0
        while i < n and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
            # 第 4 步：邊讀邊夾住範圍（讀完才判斷也行，但這樣不會累積大數）
            if sign == 1 and num > INT_MAX:
                return INT_MAX
            if sign == -1 and -num < INT_MIN:
                return INT_MIN

        return sign * num'''

S["p8_regex"] = '''import re

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        m = re.match(r"[ ]*([+-]?\\d+)", s)
        if not m:
            return 0

        return max(INT_MIN, min(INT_MAX, int(m.group(1))))'''

_p8a = S.load("p8_step")
_p8b = S.load("p8_regex")
for s in ["42", "   -42", "4193 with words", "words and 987", "-91283472332",
          "+1", "+-12", "  +0 123", "00000-42a1234", "   ", "-2147483649",
          "2147483648", ".1", "3.14", "", "0032", "  0000000000012345678",
          "-000000000000001", "+", "-", "21474836460"]:
    assert _p8a.myAtoi(s) == _p8b.myAtoi(s), ("P8", repr(s), _p8a.myAtoi(s), _p8b.myAtoi(s))
assert _p8a.myAtoi("42") == 42
assert _p8a.myAtoi("   -42") == -42
assert _p8a.myAtoi("4193 with words") == 4193
assert _p8a.myAtoi("words and 987") == 0
assert _p8a.myAtoi("-91283472332") == -2147483648
_alpha = " +-0123456789abc."
for _ in range(6000):
    s = "".join(random.choice(_alpha) for _ in range(random.randint(0, 12)))
    assert _p8a.myAtoi(s) == _p8b.myAtoi(s), ("P8", repr(s), _p8a.myAtoi(s), _p8b.myAtoi(s))
print("P8 solutions OK")

_P8_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">把 atoi 想成一台只有四個狀態的自動機</text>
            <g font-size="12" text-anchor="middle">
              <rect x="34" y="52" width="106" height="46" rx="8" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="87" y="72" fill="var(--accent)" font-size="13">start</text>
              <text x="87" y="90" fill="var(--text-muted)" font-size="10">吃空白</text>

              <rect x="192" y="52" width="106" height="46" rx="8" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="245" y="72" fill="var(--accent)" font-size="13">signed</text>
              <text x="245" y="90" fill="var(--text-muted)" font-size="10">剛吃完 + 或 −</text>

              <rect x="350" y="52" width="106" height="46" rx="8" fill="none" stroke="var(--gold)" stroke-width="2.5"/>
              <text x="403" y="72" fill="var(--gold)" font-size="13">number</text>
              <text x="403" y="90" fill="var(--text-muted)" font-size="10">正在累加</text>

              <rect x="508" y="52" width="106" height="46" rx="8" fill="none" stroke="#ff8a65" stroke-width="2"/>
              <text x="561" y="72" fill="#ff8a65" font-size="13">end</text>
              <text x="561" y="90" fill="var(--text-muted)" font-size="10">停，不再改變</text>
            </g>
            <path d="M140 75 L188 75" stroke="var(--accent)" stroke-width="1.5"/>
            <text x="164" y="68" fill="var(--text-muted)" font-size="10" text-anchor="middle">+ −</text>
            <path d="M298 75 L346 75" stroke="var(--accent)" stroke-width="1.5"/>
            <text x="322" y="68" fill="var(--text-muted)" font-size="10" text-anchor="middle">0-9</text>
            <path d="M456 75 L504 75" stroke="#ff8a65" stroke-width="1.5"/>
            <text x="480" y="68" fill="var(--text-muted)" font-size="10" text-anchor="middle">其他</text>
            <path d="M87 52 Q87 20 155 24 Q230 28 245 48" stroke="var(--border)" stroke-width="1.5" fill="none"/>
            <path d="M87 98 Q160 140 350 110" stroke="var(--accent)" stroke-width="1.5" fill="none" stroke-dasharray="4 3"/>
            <text x="220" y="136" fill="var(--text-muted)" font-size="10">直接是數字（沒有符號）</text>
            <path d="M87 98 Q60 130 110 134 Q140 136 140 110" stroke="var(--border)" stroke-width="1.5" fill="none"/>
            <text x="60" y="120" fill="var(--text-muted)" font-size="10">空白</text>
            <path d="M403 98 Q403 128 440 128 Q470 128 456 100" stroke="var(--gold)" stroke-width="1.5" fill="none"/>
            <text x="470" y="128" fill="var(--text-muted)" font-size="10">0-9</text>
            <text x="20" y="176" fill="var(--gold)" font-size="12">關鍵：一旦離開 number 進到 end，就再也回不去了 —— 這就是 &quot;4193 with words&quot; 只讀到 4193 的原因。</text>
            <text x="20" y="200" fill="var(--text-muted)" font-size="12">&quot;+-12&quot;：start →(+) signed →(−) 不是數字 → end，num 還是 0 → 答案 0</text>'''

emit({
 "num": 8, "slug": "string-to-integer-atoi",
 "en": [
   "Implement the <code>myAtoi(string s)</code> function, which converts a string to a "
   "32-bit signed integer.",
   "The algorithm is as follows: (1) skip any leading whitespace; (2) read an optional "
   "<code>'+'</code> or <code>'-'</code> sign; (3) read digits until a non-digit character "
   "or the end of input; (4) if no digits were read, the result is 0; (5) clamp the result "
   "to the range <code>[-2³¹, 2³¹ - 1]</code>.",
 ],
 "zh": [
   "實作 <code>myAtoi(string s)</code>，把字串轉換成 32 位元有號整數（類似 C/C++ 的 <code>atoi</code>）。",
   "規則依序是："
   "（1）跳過開頭的空白；"
   "（2）讀一個可有可無的 <code>'+'</code> 或 <code>'-'</code>；"
   "（3）一直讀數字，直到遇到非數字或字串結束；"
   "（4）如果一個數字都沒讀到，結果是 0；"
   "（5）超出 <code>[-2³¹, 2³¹ − 1]</code> 就夾（clamp）到邊界值，<strong>不是回傳 0</strong>。",
 ],
 "pre": [
   ("note", "這題不難，但規則多到一定會漏掉一條", [
     "第 7 題溢位回 <code>0</code>，這題溢位回 <strong>邊界值</strong>。"
     "光這一條就淘汰掉一半的人。把五條規則抄下來、一條一條對照著寫，是最有效率的做法。",
     ("c", """五條規則，缺一不可：

  1. 只跳「開頭」的空白，而且只跳半形空格 ' '
     → "  42"    ->  42
     → " 4 2"    ->  4     （中間的空白就是終止符）

  2. 符號最多一個
     → "+-12"    ->  0     （第二個符號不是數字，直接結束）
     → "--1"     ->  0

  3. 遇到非數字立刻停，不報錯
     → "4193 with words"  ->  4193
     → "words and 987"    ->  0     （開頭就不是數字）

  4. 一個數字都沒讀到 -> 0
     → "", "   ", "+", "abc"   都是 0

  5. 溢位要 clamp，不是回 0
     → "-91283472332"  ->  -2147483648   （不是 0！）
     → "21474836460"   ->   2147483647"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "42"
  輸出：42

範例 2
  輸入：s = "   -42"
  輸出：-42
  說明：跳過三個空白，讀到 '-'，然後讀 42。

範例 3
  輸入：s = "4193 with words"
  輸出：4193
  說明：讀到空白就停了。

範例 4
  輸入：s = "words and 987"
  輸出：0
  說明：第一個非空白字元是 'w'，不是數字也不是符號，直接結束。

範例 5
  輸入：s = "-91283472332"
  輸出：-2147483648
  說明：超出下界，夾到 INT_MIN（不是回傳 0）。""",
 "constraints": [
   "0 ≤ <code>s.length</code> ≤ 200（<strong>可以是空字串</strong>）",
   "<code>s</code> 由英文字母、數字、<code>' '</code>、<code>'+'</code>、<code>'-'</code>、<code>'.'</code> 組成",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>字串可以是空的</strong>，所以每個 <code>s[i]</code> 之前都要先確認 <code>i &lt; n</code>。",
       "<strong>字元集裡有 <code>'.'</code></strong> —— 這是在提醒你 <code>\"3.14\"</code> 的答案是 <strong>3</strong>，"
       "不是 3.14，也不是 0。小數點就只是一個普通的終止符。",
       "<strong>只有半形空格 <code>' '</code>，沒有 <code>\\t</code> 或 <code>\\n</code>。</strong>"
       "所以千萬不要用 <code>s.strip()</code> 或 <code>str.isspace()</code> —— "
       "它們會把 tab、換行、甚至全形空白都吃掉，在某些測資上會與規格不符。",
       "n ≤ 200，效率完全不是問題。這題考的是<strong>把規格翻譯成程式碼的精準度</strong>。",
     ]),
   ]),
 ],
 "idea": [
   "把它當成一台<strong>有限狀態機</strong>來看，五條規則就變成四個狀態之間的轉移，一條都不會漏。",
   ("fig", _P8_FIG, "0 0 640 216"),
 ],
 "approaches": [
   ap("解法一", "照著規則一步一步走（面試標準答案）", [
     "四個步驟對應四段程式碼，順序不能換：<strong>吃空白 → 吃符號 → 吃數字 → 夾範圍</strong>。",
     ("c", S["p8_step"]),
     ("h", "為什麼溢位檢查要放在迴圈裡面？"),
     "放在迴圈外面（讀完整個數字再夾）在 Python 裡也會對，但有兩個問題：",
     ("ul", [
       "字串長度 200 時，累積出來的整數會有 200 位數 —— Python 撐得住，C/Java 早就爆了。"
       "把檢查放在迴圈裡，<strong>同一份邏輯可以直接翻譯成 C</strong>。",
       "提前 return 也比較快，雖然在這個規模下無所謂。",
     ]),
     ("h", "為什麼負數要寫 <code>-num &lt; INT_MIN</code> 而不是 <code>num &gt; 2**31</code>？"),
     "兩者等價（<code>-num &lt; -2**31</code> ⟺ <code>num &gt; 2**31</code>），"
     "但寫成前者的好處是：<strong>判斷式直接對應題目的規格文字</strong>「結果小於 INT_MIN」，"
     "讀程式碼的人不用自己在心裡做一次移項。規格題寫得越像規格越好。",
     ("h", "那個常見的錯誤：用 <code>strip()</code>"),
     ("c", """錯誤寫法：
    s = s.strip()          # ✘ 會把結尾的空白也吃掉，還會吃掉 \\t \\n
    s = s.lstrip()         # ✘ 同樣會吃 \\t \\n

規格只說「跳過開頭的『空白字元』」，而測資裡只會出現半形空格。
用 while s[i] == " " 才是精確對應規格的寫法。

實務上這個差別很重要：如果你在寫一個真的 parser，
「哪些字元算 whitespace」必須由規格決定，不能由語言的預設值決定。"""),
   ], "O(n)", "O(1)", "每個字元最多看一次", "只用幾個變數", optimal=True),

   ap("解法二", "正規表示式（簡潔但要小心）", [
     ("c", S["p8_regex"]),
     ("h", "這個 pattern 逐字拆解"),
     ("c", """r"[ ]*([+-]?\\d+)"

  [ ]*      開頭 0 個以上的半形空格
            （寫 [ ] 而不是 \\s 是故意的：\\s 會吃 \\t \\n \\r \\f \\v）
  (         開始擷取
    [+-]?     可有可無的一個符號
    \\d+       一個以上的數字（+ 而不是 * ，沒數字就整個不匹配）
  )         結束擷取

re.match 只從字串開頭比對（不是 re.search），
所以 "words and 987" 匹配失敗 → 回傳 0 ✔"""),
     ("h", "三個容易出錯的地方"),
     ("ul", [
       "<strong>必須用 <code>re.match</code> 而不是 <code>re.search</code>。</strong>"
       "<code>search</code> 會在整個字串裡找，<code>\"words and 987\"</code> 就會錯誤地回傳 987。",
       "<strong>必須用 <code>\\d+</code> 而不是 <code>\\d*</code>。</strong>"
       "用 <code>*</code> 的話 <code>\"+\"</code> 會匹配成功但 group 是 <code>\"+\"</code>，<code>int(\"+\")</code> 會拋例外。",
       "<strong>不要用 <code>\\s*</code>。</strong>理由同上：規格只允許半形空格。",
     ]),
     "<strong>面試時該不該用？</strong>可以寫，但要主動說明每個部分在做什麼 —— "
     "面試官想確認你是<strong>理解規格後寫出 regex</strong>，而不是從網路上背了一條。"
     "被追問「如果不准用 regex 呢」的機率很高，所以解法一還是要會。",
   ], "O(n)", "O(n)", "regex 引擎掃一遍", "編譯後的 pattern 與擷取到的子字串"),
 ],
 "compare": (["解法", "時間", "空間", "可翻譯成 C？", "備註"],
   [["一、逐步解析", "O(n)", "O(1)", "✔", "面試預設；規格對應最清楚"],
    ["二、正規表示式", "O(n)", "O(n)", "✘", "最短，但細節陷阱多"]]),
 "edges": [
   "<strong>空字串 / 全空白</strong>：<code>\"\"</code>、<code>\"   \"</code> → 0。不能對空字串取 <code>s[0]</code>。",
   "<strong>只有符號</strong>：<code>\"+\"</code>、<code>\"-\"</code>、<code>\"+-12\"</code>、<code>\"--1\"</code> → 都是 0。",
   "<strong>開頭不是數字也不是符號</strong>：<code>\"words and 987\"</code>、<code>\".1\"</code> → 0。",
   "<strong>數字後面接垃圾</strong>：<code>\"4193 with words\"</code> → 4193；<code>\"3.14\"</code> → 3；<code>\"00000-42a1234\"</code> → 0。",
   "<strong>前導零</strong>：<code>\"0032\"</code> → 32；<code>\"-000000000000001\"</code> → −1。",
   "<strong>正溢位</strong>：<code>\"2147483648\"</code> → 2147483647（<strong>不是 0</strong>）。",
   "<strong>負溢位</strong>：<code>\"-2147483649\"</code> → −2147483648（<strong>不是 0</strong>）。",
   "<strong>剛好在邊界</strong>：<code>\"2147483647\"</code>、<code>\"-2147483648\"</code> → 原值，不能被誤夾。",
   "<strong>空白在中間</strong>：<code>\"  +0 123\"</code> → 0（讀完 0 之後遇到空白就停）。",
 ],
 "follow": [
   ("h", "追問一：要支援小數或科學記號呢？"),
   "那就變成第 65 題（Valid Number），狀態機會從 4 個狀態擴張到 9 個左右。"
   "<strong>這正是為什麼一開始就用狀態機的角度思考很划算</strong> —— 加規則等於加狀態和轉移，"
   "而不是在一堆 if 裡面到處補洞。",
   ("h", "追問二：要支援不同進位（像 <code>strtol</code> 的 base 參數）呢？"),
   "把 <code>s[i].isdigit()</code> 換成「這個字元在 base 進位下的值」，"
   "把 <code>num * 10</code> 換成 <code>num * base</code>，再處理 <code>0x</code>／<code>0b</code> 前綴即可。"
   "溢位檢查的移項技巧完全一樣，只是把 10 換成 base。",
   ("h", "追問三：為什麼真實世界的 <code>atoi</code> 被認為是壞 API？"),
   "因為它<strong>無法區分「解析失敗」和「答案真的是 0」</strong> —— "
   "<code>atoi(\"abc\")</code> 和 <code>atoi(\"0\")</code> 都回 0，呼叫端無從得知發生了什麼。"
   "這也是 C 標準後來推薦 <code>strtol</code>（會回傳「停在哪裡」和設定 <code>errno</code>）的原因，"
   "而 Rust 的 <code>str::parse</code> 直接回傳 <code>Result</code>。"
   "這是一個很好的 API 設計話題，面試時提到會加分。",
 ],
 "related": [
   "<strong>第 7 題 Reverse Integer</strong> —— 同一套溢位處理",
   "<strong>第 65 題 Valid Number</strong> —— 狀態機的完整版",
   "<strong>第 12／13 題 羅馬數字互轉</strong> —— 另一類解析題",
 ],
 "check": [
   "<code>\"  +0 123\"</code> 的答案是什麼？請一個字元一個字元說明狀態怎麼轉移。",
   "為什麼溢位要 clamp 而不是回 0？請找出題目敘述裡明確講這件事的那一句。",
   "如果把 <code>while s[i] == \" \"</code> 改成 <code>s = s.lstrip()</code>，哪一種輸入會與規格不符？",
   "regex 版本如果改用 <code>re.search</code>，<code>\"words and 987\"</code> 會回傳什麼？為什麼是錯的？",
 ],
})
print("P8 written")

# ==================== 9. Palindrome Number ====================
S["p9_str"] = '''class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]'''

S["p9_full"] = '''class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False          # 負數一定不是：'-' 只出現在左邊

        original, rev = x, 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10

        return rev == original'''

S["p9_half"] = '''class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 負數不是回文；結尾是 0 的也不是（除了 0 本身）
        # 因為那表示開頭必須是 0，而正整數不會有前導零
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:            # 只反轉一半就停
            rev = rev * 10 + x % 10
            x //= 10

        # 偶數位：x 和 rev 剛好一樣長      -> x == rev
        # 奇數位：rev 多吃了正中間那一位   -> 砍掉它再比
        return x == rev or x == rev // 10'''

_p9 = [S.load(k) for k in ("p9_str", "p9_full", "p9_half")]
for x in [121, -121, 10, 0, 1, 11, 1221, 12321, 100, 1000021, 1410110141, -101, 2147483647]:
    e = _p9[0].isPalindrome(x)
    for sol in _p9:
        assert sol.isPalindrome(x) == e, ("P9", x, sol)
assert _p9[0].isPalindrome(121) is True and _p9[0].isPalindrome(-121) is False
assert _p9[0].isPalindrome(10) is False
for _ in range(8000):
    x = random.choice([random.randint(-1000, 1000), random.randint(-10**9, 10**9)])
    e = _p9[0].isPalindrome(x)
    for sol in _p9:
        assert sol.isPalindrome(x) == e, ("P9", x, sol)
print("P9 solutions OK")

_P9_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">只反轉一半：每一輪 x 少一位、rev 多一位，交會的時候就停</text>
            <g font-family="monospace" font-size="14">
              <text x="30" y="52" fill="var(--text-muted)" font-size="12">x = 1221（偶數位）</text>
              <text x="40" y="80" fill="var(--text-muted)">輪 0：</text>
              <text x="120" y="80" fill="var(--accent)">x = 1221</text>
              <text x="280" y="80" fill="var(--gold)">rev = 0</text>
              <text x="420" y="80" fill="var(--text-muted)" font-size="12">1221 &gt; 0 → 繼續</text>
              <text x="40" y="104" fill="var(--text-muted)">輪 1：</text>
              <text x="120" y="104" fill="var(--accent)">x = 122</text>
              <text x="280" y="104" fill="var(--gold)">rev = 1</text>
              <text x="420" y="104" fill="var(--text-muted)" font-size="12">122 &gt; 1 → 繼續</text>
              <text x="40" y="128" fill="var(--text-muted)">輪 2：</text>
              <text x="120" y="128" fill="var(--accent)">x = 12</text>
              <text x="280" y="128" fill="var(--gold)">rev = 12</text>
              <text x="420" y="128" fill="#ff8a65" font-size="12">12 &gt; 12 不成立 → 停</text>
              <text x="120" y="156" fill="var(--gold)" font-size="13">x == rev → 12 == 12 ✔ 是回文</text>
            </g>
            <line x1="20" y1="176" x2="620" y2="176" stroke="var(--border)"/>
            <g font-family="monospace" font-size="14">
              <text x="30" y="204" fill="var(--text-muted)" font-size="12">x = 12321（奇數位）</text>
              <text x="40" y="232" fill="var(--text-muted)">輪 0：</text>
              <text x="120" y="232" fill="var(--accent)">x = 12321</text>
              <text x="280" y="232" fill="var(--gold)">rev = 0</text>
              <text x="40" y="256" fill="var(--text-muted)">輪 1：</text>
              <text x="120" y="256" fill="var(--accent)">x = 1232</text>
              <text x="280" y="256" fill="var(--gold)">rev = 1</text>
              <text x="40" y="280" fill="var(--text-muted)">輪 2：</text>
              <text x="120" y="280" fill="var(--accent)">x = 123</text>
              <text x="280" y="280" fill="var(--gold)">rev = 12</text>
              <text x="40" y="304" fill="var(--text-muted)">輪 3：</text>
              <text x="120" y="304" fill="var(--accent)">x = 12</text>
              <text x="280" y="304" fill="var(--gold)">rev = 123</text>
              <text x="420" y="304" fill="#ff8a65" font-size="12">12 &gt; 123 不成立 → 停</text>
              <text x="120" y="332" fill="var(--gold)" font-size="13">rev 多吃了中間的 3 → 比 x == rev // 10 → 12 == 12 ✔</text>
            </g>'''

emit({
 "num": 9, "slug": "palindrome-number",
 "en": [
   "Given an integer <code>x</code>, return <code>true</code> <em>if</em> <code>x</code> "
   "<em>is a palindrome, and</em> <code>false</code> <em>otherwise</em>.",
   "<strong>Follow up:</strong> Could you solve it without converting the integer to a string?",
 ],
 "zh": [
   "給你一個整數 <code>x</code>，如果它是<strong>回文數</strong>就回傳 <code>true</code>，否則回傳 <code>false</code>。",
   "回文數的意思是：正著讀和倒著讀都一樣。例如 121 是，−121 不是（倒過來是 121−）。",
   "<strong>進階：</strong>能不能<strong>不把整數轉成字串</strong>就解出來？",
 ],
 "pre": [
   ("note", "三個一秒判定的特例", [
     ("c", """1. 負數  ->  永遠 False
      -121 倒過來是 "121-"，'-' 只能在左邊，不可能對稱。

2. 結尾是 0 且不是 0 本身  ->  永遠 False
      10  倒過來是 01 = 1 ≠ 10
      100 倒過來是 001 = 1 ≠ 100
      因為正整數沒有前導零，結尾是 0 就表示開頭該是 0 —— 矛盾。

3. 0 本身  ->  True
      唯一結尾是 0 卻成立的數，所以第 2 條一定要寫 "and x != 0"。"""),
     "這三條寫在最前面，剩下的邏輯會乾淨很多。特別是第 2 條，"
     "它是「只反轉一半」那個解法能夠終止得漂亮的關鍵。",
   ]),
 ],
 "examples": """範例 1
  輸入：x = 121
  輸出：true

範例 2
  輸入：x = -121
  輸出：false
  說明：從左讀是 -121，從右讀是 121-，不一樣。

範例 3
  輸入：x = 10
  輸出：false
  說明：從右讀是 01，不等於 10。""",
 "constraints": [
   "−2³¹ ≤ <code>x</code> ≤ 2³¹ − 1",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "範圍就是 32 位元有號整數，最多 10 位數 —— 所以任何 O(位數) 的解法都是 O(1) 等級，快得不得了。",
       "<strong>但「不轉字串」這個 follow-up 才是真正的考點。</strong>"
       "如果只寫 <code>str(x) == str(x)[::-1]</code>，面試通常到此為止，不會加分。",
       "注意：<strong>反轉整個數字可能溢位</strong>（第 7 題的問題）。"
       "所以「只反轉一半」不只是優化，在 32 位元環境裡是<strong>正確性的需求</strong>。",
     ]),
   ]),
 ],
 "idea": [
   ("t", ["解法", "想法", "轉字串？", "會溢位？"],
     [["一、字串反轉", "<code>s == s[::-1]</code>", "會", "不會"],
      ["二、整數全反轉", "反轉後和原值比", "不會", "<strong>在 C/Java 會</strong>"],
      ["三、只反轉一半", "反轉到中點就停，兩半相比", "不會", "不會"]]),
 ],
 "approaches": [
   ap("解法一", "轉成字串比對（最短，但答不到 follow-up）", [
     ("c", S["p9_str"]),
     "<code>str(-121)</code> 是 <code>\"-121\"</code>，反轉後 <code>\"121-\"</code>，"
     "不相等 —— 所以<strong>連負數都不用特別擋</strong>，這個解法自動就對了。",
     "兩行、絕對正確、LeetCode 上 0 ms。但題目白紙黑字寫了 follow-up，"
     "所以面試時這只能當開場，不能當結尾。",
   ], "O(log x)", "O(log x)", "位數 = log₁₀x", "字串本身"),

   ap("解法二", "反轉整個整數再比（會有溢位隱憂）", [
     ("c", S["p9_full"]),
     "邏輯很直白，Python 裡完全正確。",
     ("h", "但在 C 或 Java 裡它是錯的"),
     ("c", """x = 1999999999  （不是回文）
反轉後 = 9999999991  >  INT_MAX = 2147483647

在 32 位元環境裡，rev 會環繞成一個垃圾值。
碰巧的話它甚至可能等於某個 x，讓你得到錯誤的 true。

要修就得加上第 7 題那套溢位檢查 —— 但那樣就比解法三還長了。"""),
     "<strong>這就是解法三存在的理由</strong>：只反轉一半，rev 的位數永遠不會超過 x 原本的一半，"
     "溢位問題從根本上消失。",
   ], "O(log x)", "O(1)", "位數次迴圈", "幾個整數變數"),

   ap("解法三", "只反轉後半段（進階解答）", [
     "回文的定義是「前半段 == 後半段反過來」。"
     "既然如此，<strong>根本不需要反轉整個數字</strong> —— "
     "把後半段反轉出來，跟剩下的前半段比就行了。",
     ("c", S["p9_half"]),
     ("fig", _P9_FIG, "0 0 640 352"),
     ("h", "終止條件 <code>while x &gt; rev</code> 為什麼對？"),
     "每跑一輪，<code>x</code> 少一位、<code>rev</code> 多一位。"
     "所以 <code>x</code> 單調變小、<code>rev</code> 單調變大，一定會交會，迴圈保證終止。"
     "交會點就是中點：",
     ("c", """位數為偶數（1221，4 位）：
    跑 2 輪後 x = 12（前半）、rev = 12（後半反轉）
    兩者位數相同 → 直接比 x == rev

位數為奇數（12321，5 位）：
    跑 3 輪後 x = 12、rev = 123
    rev 多吃了正中間的 '3'
    但正中間那一位在回文裡「跟自己對稱」，怎樣都成立 → 砍掉它
    比 x == rev // 10  →  12 == 12 ✔

所以最後一行要寫成：
    return x == rev or x == rev // 10
兩種情況各對應一個條件，用 or 一次涵蓋。"""),
     ("h", "為什麼一定要先擋「結尾是 0」？"),
     ("c", """假設不擋，看 x = 10：
    輪 0： x = 10, rev = 0    10 > 0  → 跑
    輪 1： x = 1,  rev = 0    1 > 0   → 跑   （rev = 0*10 + 0 = 0，還是 0！）
    輪 2： x = 0,  rev = 1    0 > 1 不成立 → 停
    檢查：x == rev ? 0 == 1 ✘
          x == rev // 10 ? 0 == 0 ✔   →  回傳 True

    錯了！10 不是回文。

根本原因：後半段的前導零在反轉時「消失」了，
導致 rev 的位數比預期少，中點判斷跟著失準。
先擋掉 x % 10 == 0（且 x != 0）就完全避開這個坑。"""),
     "<strong>這個坑是這題最值得記的地方。</strong>它不是隨便的邊界檢查，"
     "而是「數字反轉會吃掉前導零」這個性質造成的必然結果。",
   ], "O(log x)", "O(1)", "只跑一半的位數", "兩個整數變數", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "答到 follow-up？", "32 位元安全？"],
   [["一、字串", "O(log x)", "O(log x)", "✘", "✔"],
    ["二、全反轉", "O(log x)", "O(1)", "✔", "✘ 需額外加溢位檢查"],
    ["三、半反轉", "O(log x)", "O(1)", "✔", "✔"]]),
 "edges": [
   "<strong>負數</strong>：<code>-121</code>、<code>-1</code> → false。<code>-0</code> 在整數裡就是 0，不用擔心。",
   "<strong>0</strong> → true。第 2 條特例的 <code>and x != 0</code> 就是為了它。",
   "<strong>結尾是 0</strong>：<code>10</code>、<code>100</code>、<code>1000021</code> → false。解法三沒擋會錯。",
   "<strong>單一位數</strong>：<code>0</code>～<code>9</code> → 全部 true。",
   "<strong>偶數位回文</strong>：<code>1221</code>、<code>11</code> → true。走 <code>x == rev</code> 分支。",
   "<strong>奇數位回文</strong>：<code>121</code>、<code>12321</code> → true。走 <code>x == rev // 10</code> 分支。",
   "<strong>接近上界</strong>：<code>2147483647</code> → false；<code>1410110141</code> → true。",
 ],
 "follow": [
   ("h", "追問一：如果是十六進位或任意 base 的回文呢？"),
   "把所有的 <code>10</code> 換成 <code>base</code> 就好，邏輯完全不變。"
   "有趣的是：一個數可能在 base 10 是回文、在 base 2 不是（例如 121₁₀ = 1111001₂，不是回文），"
   "而 585 在兩種進位下都是回文（585₁₀ = 1001001001₂）。",
   ("h", "追問二：要找「最接近 x 的回文數」呢？"),
   "第 564 題（Find the Closest Palindrome），難度陡增。"
   "核心想法是：<strong>拿前半段去鏡射出後半段</strong>，"
   "再考慮「前半段 ±1 後鏡射」以及 <code>99...9</code> 和 <code>10...01</code> 這兩個跨位數的候選，"
   "最後在這幾個候選裡挑最近的。",
   ("h", "追問三：為什麼「只反轉一半」在系統程式裡是個有用的模式？"),
   "因為它體現了一個通則：<strong>不要算出你不需要的東西</strong>。"
   "反轉整個數字會製造一個可能溢位的中間值，而我們根本不需要那個值。"
   "同樣的想法出現在：檢查兩個大數是否相等時先比長度、"
   "比較浮點數時避免相減、判斷連結串列有沒有環時用快慢指標而不是全部存起來。",
 ],
 "related": [
   "<strong>第 7 題 Reverse Integer</strong> —— 反轉整數與溢位的完整處理",
   "<strong>第 125 題 Valid Palindrome</strong> —— 字串版，要忽略大小寫與非字母數字",
   "<strong>第 234 題 Palindrome Linked List</strong> —— 一樣是「只處理一半」的技巧",
   "<strong>第 564 題 Find the Closest Palindrome</strong> —— 這題的困難版",
 ],
 "check": [
   "如果把 <code>(x % 10 == 0 and x != 0)</code> 這個檢查拿掉，<code>x = 10</code> 會回傳什麼？請一輪一輪追出來。",
   "最後為什麼要寫 <code>x == rev or x == rev // 10</code>？各自對應哪一種位數？",
   "<code>while x &gt; rev</code> 為什麼保證會停？如果改成 <code>while x &gt;= rev</code> 會發生什麼事？",
   "在 Java 裡用解法二，<code>x = 1999999999</code> 會發生什麼？為什麼解法三沒有這個問題？",
 ],
})
print("P9 written")
