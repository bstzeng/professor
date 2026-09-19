# -*- coding: utf-8 -*-
"""第 13–15 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(13)

# ==================== 13. Roman to Integer ====================
S["p13_lookahead"] = '''class Solution:
    def romanToInt(self, s: str) -> int:
        VALUE = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

        total = 0
        for i, ch in enumerate(s):
            v = VALUE[ch]
            # 比右邊的小 -> 這是減法形式的前半，要減；否則加
            if i + 1 < len(s) and v < VALUE[s[i + 1]]:
                total -= v
            else:
                total += v
        return total'''

S["p13_pair"] = '''class Solution:
    def romanToInt(self, s: str) -> int:
        VALUE = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        PAIR = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        total, i = 0, 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i + 2] in PAIR:
                total += PAIR[s[i:i + 2]]
                i += 2                      # 兩個字元一起消化掉
            else:
                total += VALUE[s[i]]
                i += 1
        return total'''

S["p13_reverse"] = '''class Solution:
    def romanToInt(self, s: str) -> int:
        VALUE = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}

        total, prev = 0, 0
        for ch in reversed(s):              # 從右往左掃
            v = VALUE[ch]
            # 比「右邊已經處理過的最大值」小 -> 減，否則加
            total += -v if v < prev else v
            prev = max(prev, v)
        return total'''

_p13 = [S.load(k) for k in ("p13_lookahead", "p13_pair", "p13_reverse")]
_i2r = S.load("p12_greedy") if False else None
# 用第 12 題的查表法產生所有 1..3999 的羅馬數字當測資
_TH = ["", "M", "MM", "MMM"]
_HU = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
_TE = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
_ON = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
for n in range(1, 4000):
    r = _TH[n // 1000] + _HU[n % 1000 // 100] + _TE[n % 100 // 10] + _ON[n % 10]
    for sol in _p13:
        assert sol.romanToInt(r) == n, ("P13", n, r, sol, sol.romanToInt(r))
assert _p13[0].romanToInt("III") == 3
assert _p13[0].romanToInt("LVIII") == 58
assert _p13[0].romanToInt("MCMXCIV") == 1994
print("P13 solutions OK")

_P13_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">s = &quot;MCMXCIV&quot;：每個字元只要問一句「我比右邊的小嗎？」</text>
            <g font-family="monospace" font-size="18" text-anchor="middle">
              <text x="80" y="66" fill="var(--accent)">M</text>
              <text x="160" y="66" fill="#ff8a65">C</text>
              <text x="240" y="66" fill="var(--accent)">M</text>
              <text x="320" y="66" fill="#ff8a65">X</text>
              <text x="400" y="66" fill="var(--accent)">C</text>
              <text x="480" y="66" fill="#ff8a65">I</text>
              <text x="560" y="66" fill="var(--accent)">V</text>
            </g>
            <g font-size="12" text-anchor="middle" fill="var(--text-muted)">
              <text x="80" y="92">1000</text>
              <text x="160" y="92">100</text>
              <text x="240" y="92">1000</text>
              <text x="320" y="92">10</text>
              <text x="400" y="92">100</text>
              <text x="480" y="92">1</text>
              <text x="560" y="92">5</text>
            </g>
            <g font-size="13" text-anchor="middle">
              <text x="80" y="122" fill="var(--accent)">+1000</text>
              <text x="160" y="122" fill="#ff8a65">−100</text>
              <text x="240" y="122" fill="var(--accent)">+1000</text>
              <text x="320" y="122" fill="#ff8a65">−10</text>
              <text x="400" y="122" fill="var(--accent)">+100</text>
              <text x="480" y="122" fill="#ff8a65">−1</text>
              <text x="560" y="122" fill="var(--accent)">+5</text>
            </g>
            <g font-size="11" text-anchor="middle" fill="var(--text-muted)">
              <text x="80" y="144">1000 ≥ 100</text>
              <text x="160" y="144">100 &lt; 1000</text>
              <text x="240" y="144">1000 ≥ 10</text>
              <text x="320" y="144">10 &lt; 100</text>
              <text x="400" y="144">100 ≥ 1</text>
              <text x="480" y="144">1 &lt; 5</text>
              <text x="560" y="144">最後一個</text>
            </g>
            <line x1="40" y1="164" x2="600" y2="164" stroke="var(--border)"/>
            <text x="320" y="192" fill="var(--gold)" font-size="14" text-anchor="middle">1000 − 100 + 1000 − 10 + 100 − 1 + 5 = 1994</text>
            <text x="20" y="222" fill="var(--text-muted)" font-size="12">不需要認得 CM、XC、IV 這些組合 —— 只要比大小，減法形式會自動浮現。</text>'''

emit({
 "num": 13, "slug": "roman-to-integer",
 "en": [
   "Roman numerals are represented by seven different symbols: "
   "<code>I, V, X, L, C, D</code> and <code>M</code> "
   "(values <code>1, 5, 10, 50, 100, 500, 1000</code>).",
   "Usually, numerals are written largest to smallest from left to right. However, for "
   "<code>4</code> and <code>9</code>, the smaller numeral is placed before the larger one "
   "and <strong>subtracted</strong>: <code>IV, IX, XL, XC, CD, CM</code>.",
   "Given a Roman numeral, convert it to an integer.",
 ],
 "zh": [
   "羅馬數字由七個符號組成："
   "<code>I=1, V=5, X=10, L=50, C=100, D=500, M=1000</code>。",
   "一般來說是<strong>由大到小、從左寫到右</strong>。但遇到 4 和 9 的時候，"
   "會把小的符號寫在大的<strong>左邊</strong>表示<strong>相減</strong>："
   "<code>IV=4, IX=9, XL=40, XC=90, CD=400, CM=900</code>。",
   "給你一個羅馬數字字串，把它轉成整數。",
 ],
 "pre": [
   ("note", "一句話就解完這題", [
     "<strong>從左往右掃，如果當前符號比右邊那個小，就減它；否則加它。</strong>",
     ("c", """為什麼這一句就夠了？

因為羅馬數字的寫法規定是「由大到小」。
唯一會出現「小的在大的左邊」的情形，就是那六個減法形式。

所以「比右邊小」這個條件，
恰好、而且只會，在減法形式的前半個字元上成立。

  "MCMXCIV"
   M  C  M  X  C  I  V
   ^     ^     ^     ^     這些「≥ 右邊」-> 加
      ^     ^     ^        這些「< 右邊」-> 減

你完全不需要在程式裡列出 IV、IX、XL… 這六個組合。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "III"
  輸出：3

範例 2
  輸入：s = "LVIII"
  輸出：58
  說明：L = 50，V = 5，III = 3

範例 3
  輸入：s = "MCMXCIV"
  輸出：1994
  說明：M = 1000，CM = 900，XC = 90，IV = 4""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 15",
   "<code>s</code> 只含 <code>'I', 'V', 'X', 'L', 'C', 'D', 'M'</code>",
   "<strong>保證 <code>s</code> 是 1 到 3999 範圍內的有效羅馬數字</strong>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>「保證是有效的羅馬數字」是一個非常大的禮物。</strong>"
       "你不用檢查 <code>\"IIII\"</code>、<code>\"IL\"</code>、<code>\"VX\"</code> 這些非法輸入，"
       "也不用回報錯誤。所有解法都可以假設輸入完美。"
       "（如果面試官追問「那要怎麼驗證合法性」，那是另一個難度等級的問題 —— 見文末追問。）",
       "<strong>長度 ≤ 15</strong>：最長的合法羅馬數字是 3888 = "
       "<code>\"MMMDCCCLXXXVIII\"</code>，剛好 15 個字元。",
       "效率完全不是問題，所以這題的評分重點是：<strong>你的解法有多簡潔、多能說明白</strong>。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P13_FIG, "0 0 640 238"),
   "三種寫法，本質都是同一個觀察，只是實作角度不同：往右看、成對吃、往左掃。",
 ],
 "approaches": [
   ap("解法一", "往右看一格，決定加還是減（最推薦）", [
     ("c", S["p13_lookahead"]),
     "只需要一張 7 筆的表，不需要列出六個減法組合。"
     "<strong>最後一個字元一定是加</strong>（<code>i + 1 &lt; len(s)</code> 不成立），"
     "這和羅馬數字「最後一個符號永遠不做減數」的規則一致。",
     ("h", "為什麼這個判斷不會誤判？"),
     "因為合法的羅馬數字裡，「小的在大的左邊」只可能是那六個減法形式之一。"
     "例如 <code>\"XIV\"</code>（14）：<code>X</code>(10) ≥ <code>I</code>(1) → 加；"
     "<code>I</code>(1) &lt; <code>V</code>(5) → 減；<code>V</code> → 加。"
     "得到 10 − 1 + 5 = 14 ✔",
     "<strong>如果輸入不合法就不保證了</strong>："
     "<code>\"IM\"</code> 會被算成 999，但那不是合法的羅馬數字（1000−1 應寫成 <code>\"CMXCIX\"</code>）。"
     "題目保證輸入合法，所以這不是問題 —— 但要知道這個前提在哪裡。",
   ], "O(n)", "O(1)", "掃一遍", "7 筆常數表", optimal=True),

   ap("解法二", "認出兩字元的組合，一次吃兩個", [
     "另一種直覺：既然有六個「雙字元符號」，就把它們也放進表裡，遇到就一次吃兩格。",
     ("c", S["p13_pair"]),
     "邏輯上和第 12 題的貪婪法完全對稱（那題是查值找符號，這題是查符號找值）。",
     "<strong>缺點是表變大了</strong>（7 + 6 = 13 筆），而且要小心 <code>i</code> 的前進步數。"
     "好處是<strong>意圖非常明確</strong>：讀程式碼的人一眼就看得出「CM 是一個符號」。"
     "在需要維護的真實程式裡，這種明確性往往比精簡更值錢。",
   ], "O(n)", "O(1)", "掃一遍，每格最多看兩個字元", "13 筆常數表"),

   ap("解法三", "從右往左掃（面試常見的變體）", [
     "換個方向：從最右邊開始，記住「目前看過的最大值」。"
     "如果當前符號比它小，就是減法形式的前半，減掉；否則加。",
     ("c", S["p13_reverse"]),
     ("h", "為什麼要用 <code>max</code> 而不是直接記上一個？"),
     ("c", """考慮 "XIV"（14），從右往左：

  V (5):  prev = 0，5 ≥ 0  -> +5,   prev = 5
  I (1):  prev = 5，1 < 5  -> -1,   prev = max(5, 1) = 5     ← 這裡是關鍵
  X (10): prev = 5，10 ≥ 5 -> +10,  prev = 10

  總和 = 5 - 1 + 10 = 14 ✔

如果 prev 只記「上一個」而不取 max：
  I 之後 prev 會變成 1，
  然後 X (10) ≥ 1 -> +10，這次剛好也對。

但看 "MCMXCIV"：
  V(5) +5, prev=5
  I(1) -1, prev=1  ← 沒取 max，prev 退化成 1
  C(100) ≥ 1 -> +100, prev=100
  X(10)  < 100 -> -10, prev=10   ← 又退化
  M(1000) ≥ 10 -> +1000, prev=1000
  C(100)  < 1000 -> -100, prev=100
  M(1000) ≥ 100 -> +1000
  總和 = 5-1+100-10+1000-100+1000 = 1994 ✔ 碰巧也對

實際上在「合法羅馬數字」的前提下兩種寫法都對，
因為減法形式的後半永遠比前半大。
但寫 max 的版本語意更穩（「右邊出現過的最大值」），
也比較不需要依賴輸入的合法性 —— 建議保留。"""),
     "這個方向的好處是：如果題目改成「串流輸入、從尾端逐字到達」，它可以邊收邊算。",
   ], "O(n)", "O(1)", "掃一遍", "幾個變數"),
 ],
 "compare": (["解法", "時間", "表格大小", "好讀程度", "備註"],
   [["一、往右看一格", "O(n)", "7 筆", "★★★★★", "面試首選，最短"],
    ["二、成對比對", "O(n)", "13 筆", "★★★★☆", "意圖最明確，好維護"],
    ["三、從右往左", "O(n)", "7 筆", "★★★☆☆", "串流友善；要解釋 max"]]),
 "edges": [
   "<strong>單一字元</strong>：<code>\"I\"</code> → 1，<code>\"M\"</code> → 1000。",
   "<strong>全部是減法形式</strong>：<code>\"MCMXCIV\"</code> → 1994。",
   "<strong>完全沒有減法形式</strong>：<code>\"MMMDCCCLXXXVIII\"</code> → 3888（最長的輸入）。",
   "<strong>六個減法形式各測一次</strong>：IV=4、IX=9、XL=40、XC=90、CD=400、CM=900。",
   "<strong>減法形式在開頭</strong>：<code>\"IX\"</code> → 9。第一個字元就要減。",
   "<strong>減法形式在結尾</strong>：<code>\"XIV\"</code> → 14。倒數第二個字元要減。",
   "<strong>連續三個相同符號</strong>：<code>\"III\"</code> → 3、<code>\"MMM\"</code> → 3000。",
 ],
 "follow": [
   ("h", "追問一：如果不保證輸入合法，要怎麼驗證？"),
   "這比轉換難得多，要檢查的規則包括：",
   ("ul", [
     "同一符號不能連寫超過三次（<code>\"IIII\"</code> 非法）",
     "<code>V</code>、<code>L</code>、<code>D</code> 不能重複出現（<code>\"VV\"</code> 非法）",
     "只有 <code>I</code>、<code>X</code>、<code>C</code> 能當減數，"
     "而且只能減它的 5 倍和 10 倍（<code>\"IL\"</code>、<code>\"IC\"</code> 非法）",
     "減法形式後面不能再接更大或等大的符號（<code>\"IXI\"</code>、<code>\"CMM\"</code> 非法）",
   ]),
   "<strong>最乾淨的做法是「轉回去比對」</strong>：先用本題的解法算出數字 n，"
   "再用第 12 題的解法把 n 轉回羅馬數字，看看是不是和輸入一模一樣。"
   "因為第 12 題產生的是<strong>唯一的標準寫法</strong>，"
   "所以「轉回來一樣」等價於「輸入是合法的標準寫法」。"
   "<strong>用一個已知正確的正向函式來驗證反向輸入 —— 這個技巧在很多解析題上都很好用。</strong>",
   ("h", "追問二：為什麼羅馬數字不適合做算術？"),
   "因為它<strong>沒有位值（positional value）也沒有零</strong>。"
   "<code>MCMXCIV + I</code> 沒辦法像十進位那樣「個位加一、有需要再進位」，"
   "你得先理解整個字串代表什麼數。"
   "這正是十進位位值系統（以及零這個概念）在數學史上如此重要的原因 —— "
   "它讓算術變成可以機械化的符號操作。",
   ("h", "追問三：處理很長的輸入（假設可以超過 3999）時，哪個解法最好？"),
   "三個都是 O(n)、O(1)，沒有差別。"
   "但解法三（從右往左）在串流場景下最有優勢，因為它不需要往後看。",
 ],
 "related": [
   "<strong>第 12 題 Integer to Roman</strong> —— 反方向，也是驗證合法性的工具",
   "<strong>第 8 題 String to Integer (atoi)</strong> —— 另一種字串轉數字的解析題",
 ],
 "check": [
   "為什麼「比右邊小就減」這條規則，不需要另外列出六個減法組合就能正確運作？",
   "這個規則依賴「輸入是合法羅馬數字」嗎？請舉一個非法輸入，說明它會算出什麼。",
   "解法三的 <code>prev = max(prev, v)</code> 如果改成 <code>prev = v</code>，在哪一種輸入上語意會變得不可靠？",
   "要驗證一個字串是不是「合法的標準羅馬數字」，最簡單的做法是什麼？",
 ],
})
print("P13 written")

# ==================== 14. Longest Common Prefix ====================
S["p14_vertical"] = '''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first = strs[0]
        for i, ch in enumerate(first):        # 一欄一欄往下比
            for other in strs[1:]:
                if i >= len(other) or other[i] != ch:
                    return first[:i]          # 這一欄對不上，前 i 個字元就是答案
        return first                          # 第一個字串本身就是共同前綴'''

S["p14_horizontal"] = '''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            # 一直砍 prefix 的尾巴，直到它是 s 的前綴
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix'''

S["p14_sort"] = '''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # 字典序排序後，只有頭尾兩個需要比
        lo, hi = min(strs), max(strs)

        for i, ch in enumerate(lo):
            if i >= len(hi) or hi[i] != ch:
                return lo[:i]
        return lo'''

S["p14_zip"] = '''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        out = []
        for chars in zip(*strs):              # zip 在最短的字串用完時自動停
            if len(set(chars)) > 1:           # 這一欄有人不一樣
                break
            out.append(chars[0])
        return "".join(out)'''

_p14 = [S.load(k) for k in ("p14_vertical", "p14_horizontal", "p14_sort", "p14_zip")]


def _lcp_ref(strs):
    if not strs:
        return ""
    n = min(len(x) for x in strs)
    k = 0
    while k < n and len(set(x[k] for x in strs)) == 1:
        k += 1
    return strs[0][:k]


for c in [["flower", "flow", "flight"], ["dog", "racecar", "car"], ["a"], [""],
          ["", "b"], ["ab", "a"], ["abc", "abc", "abc"], ["c", "acc", "ccc"]]:
    e = _lcp_ref(c)
    for sol in _p14:
        assert sol.longestCommonPrefix(list(c)) == e, ("P14", c, sol, sol.longestCommonPrefix(list(c)), e)
for _ in range(4000):
    c = ["".join(random.choice("ab") for _ in range(random.randint(0, 5)))
         for _ in range(random.randint(1, 5))]
    e = _lcp_ref(c)
    for sol in _p14:
        assert sol.longestCommonPrefix(list(c)) == e, ("P14", c, sol, e)
print("P14 solutions OK")

emit({
 "num": 14, "slug": "longest-common-prefix",
 "en": [
   "Write a function to find the longest common prefix string amongst an array of strings.",
   "If there is no common prefix, return an empty string <code>\"\"</code>.",
 ],
 "zh": [
   "寫一個函式，找出一組字串裡<strong>最長的共同前綴</strong>。",
   "如果沒有共同前綴，回傳空字串 <code>\"\"</code>。",
 ],
 "pre": [
   ("note", "前綴的兩個性質，決定了所有解法", [
     ("c", """性質 1：答案的長度不會超過「最短的那個字串」
    ["abcdef", "ab"] -> 最多只能是 "ab"

性質 2：共同前綴具有「傳遞收斂」的性質
    LCP(a, b, c) = LCP(LCP(a, b), c)
    也就是可以一個一個併進去，不必同時看全部。

性質 3（最漂亮的一個）：
    把所有字串照「字典序」排好之後，
    LCP(全部) == LCP(最小的那個, 最大的那個)

    因為字典序最小和最大的兩個字串「差最多」，
    它們都同意的前綴，中間的字串一定也同意。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：strs = ["flower", "flow", "flight"]
  輸出："fl"

範例 2
  輸入：strs = ["dog", "racecar", "car"]
  輸出：""
  說明：連第一個字元都不一樣。""",
 "constraints": [
   "1 ≤ <code>strs.length</code> ≤ 200",
   "0 ≤ <code>strs[i].length</code> ≤ 200（<strong>字串可以是空的</strong>）",
   "<code>strs[i]</code> 只含小寫英文字母",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>字串可以是空的。</strong><code>[\"\", \"b\"]</code> 的答案是 <code>\"\"</code>。"
       "任何對 <code>s[0]</code> 的存取都要先確認長度 —— 這是本題最常見的 IndexError 來源。",
       "<strong>陣列至少有一個元素</strong>（<code>strs.length ≥ 1</code>），"
       "所以理論上不用檢查空陣列。但寫上 <code>if not strs</code> 只要一行，"
       "而且讓函式在別的情境下也安全 —— 建議保留。",
       "<strong>只有一個字串時</strong>，答案就是它自己。<code>[\"a\"]</code> → <code>\"a\"</code>。",
       "規模很小（200 × 200 = 40000 個字元），任何解法都會過。"
       "這題考的是<strong>邊界處理的乾淨程度</strong>。",
     ]),
   ]),
 ],
 "idea": [
   ("t", ["解法", "怎麼掃", "時間", "特點"],
     [["一、垂直掃描", "一欄一欄往下比", "O(S)", "最早退出，最直覺"],
      ["二、水平掃描", "把 prefix 和下一個字串合併", "O(S)", "體現 LCP 的結合律"],
      ["三、排序取頭尾", "只比 min 和 max", "O(n·m)", "最少的比較次數"],
      ["四、zip", "Python 的一行流", "O(S)", "最短，但要懂 zip 的行為"]]),
   "<code>S</code> 是所有字元的總數。四種都是線性等級，差別在<strong>提早退出的時機</strong>和可讀性。",
 ],
 "approaches": [
   ap("解法一", "垂直掃描：一欄一欄比（最推薦）", [
     "把所有字串上下對齊排好，一次比一「欄」。只要有任何一個字串在這一欄對不上（或已經沒字元了），就結束。",
     ("c", """strs = ["flower", "flow", "flight"]

  欄位:   0  1  2  3  4  5
        f  l  o  w  e  r
        f  l  o  w
        f  l  i  g  h  t
        ─  ─  ✘
        ✔  ✔  第 2 欄：o vs o vs i -> 不一致，停

答案 = first[:2] = "fl\""""),
     ("c", S["p14_vertical"]),
     "<strong>最壞情況只會比到「最短字串的長度」次</strong>，因為 <code>i &gt;= len(other)</code> "
     "會在最短的字串用完時立刻 return。",
     "這是四種解法裡<strong>最早退出</strong>的：只要第一欄就不一致（像範例 2），"
     "只做 <code>n−1</code> 次比較就結束了。",
   ], "O(S)", "O(1)", "S = 所有字元總數；不一致時提早退出", "只回傳切片", optimal=True),

   ap("解法二", "水平掃描：把答案一個一個併進去", [
     "利用 <code>LCP(a,b,c) = LCP(LCP(a,b), c)</code>："
     "先拿第一個當候選前綴，然後每遇到一個新字串就把候選砍短，直到它是新字串的前綴為止。",
     ("c", """prefix = "flower"

  vs "flow":
      "flow".startswith("flower")  ✘  -> prefix = "flowe"
      "flow".startswith("flowe")   ✘  -> prefix = "flow"
      "flow".startswith("flow")    ✔  停

  vs "flight":
      "flight".startswith("flow")  ✘  -> prefix = "flo"
      "flight".startswith("flo")   ✘  -> prefix = "fl"
      "flight".startswith("fl")    ✔  停

答案 = "fl\""""),
     ("c", S["p14_horizontal"]),
     "<code>if not prefix: return \"\"</code> 這行不能省 —— 否則 <code>prefix[:-1]</code> "
     "在空字串上會一直是空字串，<code>\"\".startswith(\"\")</code> 是 True，"
     "所以其實不會死循環，但加上這行可以提早結束，也讓意圖更清楚。",
     "<strong>這個解法的價值在於它體現了「結合律」</strong>，"
     "可以直接推廣成 map-reduce：把字串分成幾組平行算出各組的 LCP，再把結果兩兩合併。",
   ], "O(S)", "O(m)", "m = 最短字串長度", "prefix 的切片"),

   ap("解法三", "排序後只比頭尾（最少的字元比較）", [
     "字典序排序後，只需要比<strong>最小</strong>和<strong>最大</strong>這兩個字串。",
     ("h", "為什麼只比頭尾就夠？"),
     ("c", """設排序後是 s₁ ≤ s₂ ≤ ... ≤ sₙ（字典序）

宣稱：LCP(全部) = LCP(s₁, sₙ)

證明的直覺：
  設 p = LCP(s₁, sₙ)，也就是 s₁ 和 sₙ 的前 |p| 個字元都一樣。
  對於中間任何一個 sₖ，我們有 s₁ ≤ sₖ ≤ sₙ。

  字典序比較是「從左到右逐字元比，第一個不同的決定大小」。
  既然 s₁ 和 sₙ 的前 |p| 個字元完全相同，
  而 sₖ 被夾在它們中間，
  sₖ 的前 |p| 個字元也只能是同一串 —— 否則它會跑到 s₁ 之前或 sₙ 之後。

  所以 p 是所有字串的共同前綴。
  又因為 LCP(全部) ⊆ LCP(s₁, sₙ)（子集的 LCP 一定不比全集短），
  兩邊相等。"""),
     ("c", S["p14_sort"]),
     "用 <code>min()</code> 和 <code>max()</code> 只要 O(n·m) 就能找出頭尾，"
     "不必真的做 O(n·m·log n) 的完整排序。",
     "<strong>字元比較次數最少</strong>（只比兩個字串），"
     "但因為 <code>min</code>／<code>max</code> 本身要掃過所有字串，總複雜度沒有變好。"
     "面試時提出來會是很好的加分點 —— 它展示了你會從「資料的序關係」找結構。",
   ], "O(n·m)", "O(1)", "n 個字串各比較一次求 min/max", "只回傳切片"),

   ap("解法四", "Python 的 zip 一行流", [
     ("c", S["p14_zip"]),
     ("h", "<code>zip(*strs)</code> 在做什麼？"),
     ("c", """strs = ["flower", "flow", "flight"]

zip(*strs) 等於 zip("flower", "flow", "flight")
  -> ('f', 'f', 'f')
     ('l', 'l', 'l')
     ('o', 'o', 'i')      <- set 大小 3 > 1，break
     ...

關鍵：zip 會在「最短的那個」用完時自動停止。
      "flow" 只有 4 個字元，所以最多只會產生 4 組。
      這剛好就是我們要的「答案不超過最短字串」的性質 ——
      連檢查都不用寫。

len(set(chars)) > 1 就是「這一欄有人不一樣」。"""),
     "<strong>如果 <code>strs</code> 裡有空字串會怎樣？</strong>"
     "<code>zip</code> 會立刻停（最短長度是 0），迴圈一次都不跑，回傳 <code>\"\"</code> —— 正確。",
     "很 Pythonic，寫起來很爽。但面試時建議<strong>先寫解法一，再說「Python 可以這樣一行寫」</strong>，"
     "因為面試官想確認你懂演算法，而不是懂語言特性。",
   ], "O(S)", "O(m)", "每一欄建一次 set", "輸出的 list"),
 ],
 "compare": (["解法", "時間", "空間", "最早退出？", "備註"],
   [["一、垂直掃描", "O(S)", "O(1)", "✔ 最好", "面試預設"],
    ["二、水平掃描", "O(S)", "O(m)", "普通", "可平行化（結合律）"],
    ["三、排序頭尾", "O(n·m)", "O(1)", "—", "字元比較最少，思路漂亮"],
    ["四、zip", "O(S)", "O(m)", "✔", "最短，Python 專用"]]),
 "edges": [
   "<strong>完全沒有共同前綴</strong>：<code>[\"dog\",\"racecar\",\"car\"]</code> → <code>\"\"</code>。",
   "<strong>含空字串</strong>：<code>[\"\"]</code>、<code>[\"\",\"b\"]</code>、<code>[\"b\",\"\"]</code> → 全部是 <code>\"\"</code>。",
   "<strong>其中一個是另一個的前綴</strong>：<code>[\"ab\",\"a\"]</code> → <code>\"a\"</code>。"
   "垂直掃描要靠 <code>i &gt;= len(other)</code> 這個檢查擋住。",
   "<strong>全部一樣</strong>：<code>[\"abc\",\"abc\",\"abc\"]</code> → <code>\"abc\"</code>。"
   "第一個字串會被完整走完，迴圈正常結束。",
   "<strong>只有一個字串</strong>：<code>[\"a\"]</code> → <code>\"a\"</code>。",
   "<strong>第一個字串最短</strong>：<code>[\"c\",\"acc\",\"ccc\"]</code> → <code>\"\"</code>。",
 ],
 "follow": [
   ("h", "追問一：如果字串陣列很大，而且會反覆查詢不同的子集合呢？"),
   "建一棵 <strong>Trie（字典樹）</strong>。"
   "所有字串插進去之後，從根節點往下走，"
   "只要當前節點<strong>只有一個子節點</strong>而且<strong>不是某個字串的結尾</strong>，就繼續往下。"
   "建樹 O(S)，之後每次查詢 O(答案長度)。"
   "<strong>但如果只查一次，建 Trie 是浪費</strong> —— 建樹本身就已經 O(S) 了。",
   ("h", "追問二：要找最長共同「後綴」呢？"),
   "把每個字串反轉，套用同一套解法，答案再反轉回來。"
   "一行 <code>[s[::-1] for s in strs]</code> 就解決。",
   ("h", "追問三：這個問題可以平行化嗎？"),
   "可以，而且很漂亮。因為 LCP 滿足<strong>結合律</strong>"
   "（<code>LCP(LCP(a,b), c) = LCP(a, LCP(b,c))</code>）"
   "而且有單位元（任意長字串），它是一個 <strong>monoid</strong>。"
   "所以可以把陣列切成 k 塊，各自算出局部 LCP，再把 k 個結果兩兩合併 —— "
   "這正是 map-reduce 的標準形式。",
 ],
 "related": [
   "<strong>第 208 題 Implement Trie</strong> —— 字典樹的完整實作",
   "<strong>第 720 題 Longest Word in Dictionary</strong> —— Trie 的應用",
 ],
 "check": [
   "為什麼「排序後只比頭尾」是對的？請用 <code>[\"abc\", \"abd\", \"abe\"]</code> 說明。",
   "垂直掃描裡 <code>i &gt;= len(other)</code> 這個檢查是為了哪一種輸入？拿掉會發生什麼？",
   "<code>zip(*strs)</code> 遇到 <code>[\"\", \"abc\"]</code> 會產生幾組？為什麼答案自動就對了？",
   "LCP 是一個 monoid，這件事為什麼讓它可以平行化？",
 ],
})
print("P14 written")
