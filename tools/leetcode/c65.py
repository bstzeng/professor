# -*- coding: utf-8 -*-
"""第 65–68 題。"""
import random, re
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(65)

# ==================== 65. Valid Number ====================
S["p65_manual"] = '''class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = False      # 看過數字了嗎
        seen_dot = False        # 看過小數點了嗎
        seen_exp = False        # 看過 e/E 了嗎

        for i, ch in enumerate(s):
            if ch.isdigit():
                seen_digit = True

            elif ch in "+-":
                # 正負號只能出現在「最開頭」或「e/E 的正後面」
                if i > 0 and s[i - 1] not in "eE":
                    return False

            elif ch == ".":
                # 小數點不能重複，也不能出現在 e/E 之後（指數必須是整數）
                if seen_dot or seen_exp:
                    return False
                seen_dot = True

            elif ch in "eE":
                # e/E 不能重複，而且前面「必須」已經有數字
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False     # 重設：e 後面也「必須」有數字

            else:
                return False           # 其他字元一律不合法

        return seen_digit              # 結尾必須以數字收場'''

S["p65_regex"] = '''import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # 整數或小數，後面可接一個「e/E + 整數」
        pattern = r"[+-]?(\\d+\\.?\\d*|\\.\\d+)([eE][+-]?\\d+)?"
        return re.fullmatch(pattern, s) is not None'''

S["p65_fsm"] = '''class Solution:
    def isNumber(self, s: str) -> bool:
        # 明確的有限狀態機：state -> {字元類別: 下一個 state}
        # 字元類別：d=數字, s=正負號, .=小數點, e=指數符號
        TRANSITIONS = [
            {"s": 1, "d": 2, ".": 3},          # 0 起始
            {"d": 2, ".": 3},                  # 1 吃過正負號
            {"d": 2, ".": 4, "e": 5},          # 2 整數部分（可接受狀態）
            {"d": 4},                          # 3 「.」開頭，還沒有數字
            {"d": 4, "e": 5},                  # 4 小數部分（可接受狀態）
            {"s": 6, "d": 7},                  # 5 剛吃過 e/E
            {"d": 7},                          # 6 指數的正負號
            {"d": 7},                          # 7 指數數字（可接受狀態）
        ]
        ACCEPT = {2, 4, 7}

        def kind(ch: str) -> str:
            if ch.isdigit():
                return "d"
            if ch in "+-":
                return "s"
            if ch == ".":
                return "."
            if ch in "eE":
                return "e"
            return "?"

        state = 0
        for ch in s:
            k = kind(ch)
            if k not in TRANSITIONS[state]:
                return False
            state = TRANSITIONS[state][k]

        return state in ACCEPT'''

_p65 = [S.load(k) for k in ("p65_manual", "p65_regex", "p65_fsm")]
_CASES65 = [
    ("2", True), ("0089", True), ("-0.1", True), ("+3.14", True), ("4.", True),
    ("-.9", True), ("2e10", True), ("-90E3", True), ("3e+7", True),
    ("+6e-1", True), ("53.5e93", True), ("-123.456e789", True),
    ("abc", False), ("1a", False), ("1e", False), ("e3", False),
    ("99e2.5", False), ("--6", False), ("-+3", False), ("95a54e53", False),
    (".", False), ("+", False), ("", False), ("e", False), (".e1", False),
    ("4e+", False), ("+.8", True), ("46.e3", True), ("6e6.5", False),
    (".1", True), ("1.", True), ("1.2.3", False), ("+-3", False),
]
for s_, e in _CASES65:
    for sol in _p65:
        assert sol.isNumber(s_) is e, ("P65", repr(s_), sol, sol.isNumber(s_), e)
_alpha65 = "0123456789+-.eE a"
for _ in range(20000):
    s_ = "".join(random.choice(_alpha65) for _ in range(random.randint(0, 6)))
    vals = [sol.isNumber(s_) for sol in _p65]
    assert len(set(vals)) == 1, ("P65 mismatch", repr(s_), vals)
print("P65 solutions OK")

_P65_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">有限狀態機：8 個狀態，雙圈的是「可接受」狀態</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="60" cy="70" r="20" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="60" y="75" fill="var(--accent)">0</text>
              <text x="60" y="104" fill="var(--text-muted)" font-size="10">起始</text>

              <circle cx="160" cy="70" r="20" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="160" y="75" fill="var(--accent)">1</text>
              <text x="160" y="104" fill="var(--text-muted)" font-size="10">正負號</text>

              <circle cx="280" cy="70" r="20" fill="none" stroke="var(--gold)" stroke-width="2"/>
              <circle cx="280" cy="70" r="24" fill="none" stroke="var(--gold)" stroke-width="1.5"/>
              <text x="280" y="75" fill="var(--gold)">2</text>
              <text x="280" y="108" fill="var(--text-muted)" font-size="10">整數</text>

              <circle cx="160" cy="180" r="20" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="160" y="185" fill="var(--accent)">3</text>
              <text x="160" y="214" fill="var(--text-muted)" font-size="10">只有小數點</text>

              <circle cx="280" cy="180" r="20" fill="none" stroke="var(--gold)" stroke-width="2"/>
              <circle cx="280" cy="180" r="24" fill="none" stroke="var(--gold)" stroke-width="1.5"/>
              <text x="280" y="185" fill="var(--gold)">4</text>
              <text x="280" y="218" fill="var(--text-muted)" font-size="10">小數</text>

              <circle cx="400" cy="70" r="20" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="400" y="75" fill="var(--accent)">5</text>
              <text x="400" y="104" fill="var(--text-muted)" font-size="10">剛吃 e</text>

              <circle cx="500" cy="70" r="20" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="500" y="75" fill="var(--accent)">6</text>
              <text x="500" y="104" fill="var(--text-muted)" font-size="10">指數符號</text>

              <circle cx="590" cy="150" r="20" fill="none" stroke="var(--gold)" stroke-width="2"/>
              <circle cx="590" cy="150" r="24" fill="none" stroke="var(--gold)" stroke-width="1.5"/>
              <text x="590" y="155" fill="var(--gold)">7</text>
              <text x="590" y="188" fill="var(--text-muted)" font-size="10">指數數字</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.4" fill="none">
              <path d="M80 70 L138 70"/>
              <path d="M180 70 L256 70"/>
              <path d="M78 82 L146 166"/>
              <path d="M74 56 Q170 20 258 58"/>
              <path d="M178 172 L258 172"/>
              <path d="M290 92 L172 162"/>
              <path d="M304 70 L378 70"/>
              <path d="M300 168 Q380 130 396 92"/>
              <path d="M420 70 L478 70"/>
              <path d="M414 86 Q520 120 570 138"/>
              <path d="M518 84 Q568 108 582 128"/>
            </g>
            <g font-size="10" fill="var(--text-muted)" text-anchor="middle">
              <text x="109" y="62">+ −</text>
              <text x="218" y="62">數字</text>
              <text x="96" y="132">.</text>
              <text x="166" y="30">數字</text>
              <text x="218" y="164">數字</text>
              <text x="236" y="138">.</text>
              <text x="341" y="62">e E</text>
              <text x="364" y="146">e E</text>
              <text x="449" y="62">+ −</text>
              <text x="490" y="126">數字</text>
              <text x="566" y="96">數字</text>
            </g>
            <path d="M262 56 Q280 36 298 56" stroke="var(--border)" stroke-width="1.4" fill="none"/>
            <text x="280" y="34" fill="var(--text-muted)" font-size="10" text-anchor="middle">數字</text>
            <path d="M262 166 Q280 146 298 166" stroke="var(--border)" stroke-width="1.4" fill="none"/>
            <text x="280" y="144" fill="var(--text-muted)" font-size="10" text-anchor="middle">數字</text>
            <path d="M572 136 Q590 116 608 136" stroke="var(--border)" stroke-width="1.4" fill="none"/>
            <text x="590" y="114" fill="var(--text-muted)" font-size="10" text-anchor="middle">數字</text>
            <text x="20" y="256" fill="var(--gold)" font-size="12">走完整個字串後，停在 2、4、7 才算合法 —— 這三個狀態的共同點是「剛吃完數字」。</text>'''

emit({
 "num": 65, "slug": "valid-number",
 "en": [
   "A <strong>valid number</strong> can be split up into these components (in order):",
   "(1) A <strong>decimal number</strong> or an <strong>integer</strong>. "
   "(2) (Optional) An <code>'e'</code> or <code>'E'</code>, followed by an "
   "<strong>integer</strong>.",
   "A <strong>decimal number</strong> can be split up into: (optional) sign, then one of: "
   "digits followed by a dot; digits followed by a dot followed by digits; or a dot followed "
   "by digits. An <strong>integer</strong> is: (optional) sign, then digits.",
   "Given a string <code>s</code>, return <code>true</code> if <code>s</code> is a "
   "<strong>valid number</strong>.",
 ],
 "zh": [
   "一個<strong>有效數字</strong>由以下兩部分組成（依序）：",
   "（1）一個<strong>小數</strong>或<strong>整數</strong>；"
   "（2）（可選）一個 <code>'e'</code> 或 <code>'E'</code>，後面接一個<strong>整數</strong>。",
   "<strong>小數</strong>＝（可選的）正負號 + 下列之一："
   "<code>數字.</code>、<code>數字.數字</code>、<code>.數字</code>。"
   "<strong>整數</strong>＝（可選的）正負號 + 數字。",
   "給你一個字串 <code>s</code>，判斷它是不是有效數字。",
 ],
 "pre": [
   ("note", "先把規則攤平成一張表", [
     ("c", """合法的例子：
    "2"           整數
    "0089"        前導零沒關係
    "-0.1"        小數
    "+3.14"
    "4."          小數點後面可以沒有數字 ✔
    "-.9"         小數點前面可以沒有數字 ✔
    "2e10"        科學記號
    "-90E3"       大寫 E 也可以
    "3e+7"        指數可以有正負號
    "53.5e93"
    "46.e3"       "46." 是合法小數，後面接 e3 ✔

不合法的例子：
    "abc"         不是數字
    "1a"          有雜訊
    "1e"          e 後面必須有數字
    "e3"          e 前面必須有數字
    "99e2.5"      指數必須是「整數」，不能有小數點
    "--6"         正負號最多一個
    "-+3"
    "95a54e53"
    "."           光一個小數點不算數字
    "+"           光一個正負號不算
    ""            空字串不算
    "4e+"         e 和正負號之後還是要有數字

四條核心規則：
    1. 正負號只能在「開頭」或「e/E 的正後面」
    2. 小數點最多一個，而且不能在 e/E 之後
    3. e/E 最多一個，而且「前面」和「後面」都必須有數字
    4. 整個字串必須以數字收場（不能停在 . + - e 上）
       —— 但 "4." 是合法的！所以規則 4 要小心。"""),
     "<strong>「4.」合法但「.」不合法</strong> —— "
     "這一組對照抓出了大部分錯誤的實作。"
     "關鍵在於：<strong>小數點兩邊至少要有一邊有數字</strong>。",
   ]),
 ],
 "examples": """範例 1
  輸入：s = "0"
  輸出：true

範例 2
  輸入：s = "e"
  輸出：false

範例 3
  輸入：s = "."
  輸出：false

範例 4
  輸入：s = "4."
  輸出：true""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 20",
   "<code>s</code> 由英文字母（大小寫）、數字、<code>'+'</code>、<code>'-'</code>、"
   "<code>'.'</code> 組成",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>字元集包含所有英文字母</strong>，不只是 <code>e</code> 和 <code>E</code>。"
       "所以 <code>\"1a\"</code>、<code>\"abc\"</code>、<code>\"Infinity\"</code> 都是測資，"
       "要有一個 <code>else: return False</code> 兜底。",
       "<strong>長度只有 20</strong>，效率完全不是問題。"
       "這題百分之百考<strong>規格的精確翻譯</strong>。",
       "<strong>不需要處理 <code>\"Infinity\"</code>、<code>\"NaN\"</code>、"
       "十六進位、底線分隔符</strong>（Python 的 <code>float()</code> 接受其中幾種）—— "
       "<strong>所以不能用 <code>try: float(s)</code> 作弊</strong>，"
       "<code>float(\"inf\")</code> 和 <code>float(\"nan\")</code> 都會成功但答案應該是 false。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P65_FIG, "0 0 640 268"),
   "三種寫法：<strong>逐字元 + 三個旗標</strong>（最好寫）、"
   "<strong>正規表示式</strong>（最短）、"
   "<strong>明確的狀態機</strong>（最能擴充）。",
 ],
 "approaches": [
   ap("解法一", "逐字元掃描 + 三個旗標（最推薦）", [
     ("c", S["p65_manual"]),
     ("h", "四個分支，逐一對照規則"),
     ("c", """數字： seen_digit = True
    沒有任何限制，數字永遠可以出現。

正負號： 只能在 i == 0 或 s[i-1] in "eE"
    "-1.5"   i=0      ✔
    "1e-5"   s[1]='e' ✔
    "1-5"    s[0]='1' ✘
    "--6"    i=1，s[0]='-' ✘

小數點： 不能重複，也不能在 e 之後
    "1.2.3"   第二個點 -> seen_dot 已經是 True ✘
    "1e2.5"   seen_exp 已經是 True ✘（指數必須是整數）

e/E： 不能重複，而且前面必須有數字
    "e3"      seen_digit 還是 False ✘
    "1e2e3"   seen_exp 已經是 True ✘
    "1e5"     ✔"""),
     ("h", "最精妙的一行：<code>seen_digit = False</code>"),
     ("c", """elif ch in "eE":
    if seen_exp or not seen_digit:
        return False
    seen_exp = True
    seen_digit = False      <- 這一行

為什麼要把 seen_digit 重設成 False？

因為 e 之後「也必須」有數字。
把旗標歸零，等於說「從現在開始重新要求至少一個數字」。

然後最後一行 return seen_digit 就同時檢查了兩件事：
    - 沒有 e 的情況：整個字串至少有一個數字
    - 有 e 的情況：  e 之後至少有一個數字

    "1e"   -> e 之後沒數字 -> seen_digit 是 False -> False ✔
    "1e5"  -> e 之後有 5   -> seen_digit 是 True  -> True  ✔
    "4."   -> 有數字 4     -> True ✔
    "."    -> 從來沒有數字 -> False ✔

一個變數的重複利用，同時處理了兩個「必須有數字」的要求。
這是這個解法最漂亮的地方。"""),
     "<strong>只有 20 行，而且每一行都直接對應規格的一條規則</strong> —— "
     "這讓它很容易驗證，也很容易在面試時逐條講解。",
   ], "O(n)", "O(1)", "掃一遍", "三個 bool", optimal=True),

   ap("解法二", "正規表示式（最短）", [
     ("c", S["p65_regex"]),
     ("h", "pattern 逐段拆解"),
     ("c", """r"[+-]?(\\d+\\.?\\d*|\\.\\d+)([eE][+-]?\\d+)?"

[+-]?              可選的正負號

(                  小數或整數，兩種形式擇一
  \\d+\\.?\\d*         一個以上的數字，然後可選的小數點，然後 0 個以上的數字
                   -> 涵蓋 "123"、"123."、"123.456"
  |
  \\.\\d+             小數點 + 一個以上的數字
                   -> 涵蓋 ".456"
)

(                  可選的指數部分
  [eE]
  [+-]?            指數的可選正負號
  \\d+              指數必須是「一個以上的數字」（不能有小數點）
)?

必須用 re.fullmatch（不是 match 或 search）——
否則 "1a" 會匹配前面的 "1" 而回傳 True ✘"""),
     ("h", "為什麼要拆成兩個分支？"),
     ("c", """如果寫成 \\d*\\.?\\d*（兩邊都用 *），
那 "." 和 "" 都會匹配成功 ✘

必須保證「小數點的至少一邊有數字」：
    \\d+\\.?\\d*   左邊一定有數字
    \\.\\d+        右邊一定有數字

兩者的聯集剛好涵蓋所有合法的小數和整數，
而且排除了 "." 和 ""。

這一行就是整個 pattern 最需要想清楚的地方。"""),
     "<strong>面試時可以寫，但要能逐段解釋。</strong>"
     "而且要主動說「如果不准用 regex，我會用逐字元掃描」—— "
     "因為 regex 版本無法展示你對規格的拆解能力。",
   ], "O(n)", "O(n)", "regex 引擎掃一遍", "編譯後的 pattern"),

   ap("解法三", "明確的有限狀態機（最能擴充）", [
     "把狀態機畫出來，寫成一張轉移表。",
     ("c", S["p65_fsm"]),
     ("h", "八個狀態的意義"),
     ("t", ["狀態", "意義", "可接受？"],
       [["0", "起始，什麼都還沒讀", "✘"],
        ["1", "讀過正負號，等數字或小數點", "✘"],
        ["2", "整數部分（至少一個數字）", "✔"],
        ["3", "只讀到小數點（前面沒數字），等數字", "✘"],
        ["4", "小數部分（小數點兩側至少一邊有數字）", "✔"],
        ["5", "剛讀過 e/E，等指數", "✘"],
        ["6", "指數的正負號，等數字", "✘"],
        ["7", "指數數字", "✔"]]),
     ("h", "為什麼狀態 2 和 4 都可接受，3 不行？"),
     ("c", """狀態 2：讀完整數，例如 "123"          -> 合法 ✔
狀態 3：只讀到 "."（前面沒數字）       -> 還不是數字 ✘
        再讀一個數字就變成狀態 4        -> ".5" ✔
狀態 4：小數，例如 "123." 或 ".5"      -> 合法 ✔

注意狀態 2 讀到 "." 會去狀態 4（不是 3）：
    "123." -> 狀態 2 讀 "." -> 狀態 4（可接受）✔

而狀態 0 或 1 讀到 "." 會去狀態 3：
    "." -> 狀態 3（不可接受）✘
    ".5" -> 狀態 3 讀 "5" -> 狀態 4 ✔

3 和 4 的差別，精確地編碼了
「小數點至少要有一邊有數字」這條規則。"""),
     ("h", "狀態機的價值"),
     ("ul", [
       "<strong>加規則 = 加狀態和轉移</strong>，不用在一堆 if 裡找地方插。"
       "例如要支援 <code>\"0x1F\"</code>，只要加幾個狀態。",
       "<strong>可以被機器產生和驗證</strong>。"
       "真正的編譯器的詞法分析器（lexer）就是這樣做的 —— "
       "工具（lex、flex、ANTLR）從正規表示式自動產生狀態轉移表。",
       "<strong>O(1) 空間，一次掃過，不回頭</strong> —— 串流友善。",
     ]),
     "<strong>缺點</strong>：這張表要手動推導，而且推錯很難查。"
     "在面試的時間壓力下，解法一通常比較保險。",
   ], "O(n)", "O(1)", "掃一遍，每個字元一次查表", "固定大小的轉移表"),
 ],
 "compare": (["解法", "行數", "可擴充性", "好驗證？", "面試推薦"],
   [["一、旗標掃描", "20", "★★☆☆☆", "★★★★★", "★★★★★"],
    ["二、regex", "3", "★★★☆☆", "★★☆☆☆", "★★★☆☆"],
    ["三、狀態機", "30", "★★★★★", "★★★★☆", "★★★☆☆"]]),
 "edges": [
   "<strong><code>\"4.\"</code></strong> → true；<strong><code>\".\"</code></strong> → false。"
   "<strong>最關鍵的一組對照。</strong>",
   "<strong><code>\".1\"</code>、<code>\"+.8\"</code></strong> → true。小數點可以開頭。",
   "<strong><code>\"46.e3\"</code></strong> → true。<code>\"46.\"</code> 是合法小數，後面接 <code>e3</code>。",
   "<strong><code>\"e\"</code>、<code>\"e3\"</code>、<code>\"1e\"</code>、<code>\"4e+\"</code></strong> → false。"
   "e 的前後都必須有數字。",
   "<strong><code>\"99e2.5\"</code>、<code>\"6e6.5\"</code></strong> → false。指數必須是整數。",
   "<strong><code>\"--6\"</code>、<code>\"-+3\"</code>、<code>\"+\"</code></strong> → false。",
   "<strong><code>\"1.2.3\"</code></strong> → false。小數點只能一個。",
   "<strong><code>\"0089\"</code></strong> → true。前導零是合法的。",
   "<strong><code>\"abc\"</code>、<code>\"95a54e53\"</code></strong> → false。要有 else 兜底。",
   "<strong>不要用 <code>float(s)</code></strong>："
   "<code>float(\"inf\")</code>、<code>float(\"nan\")</code>、<code>float(\"1_0\")</code> "
   "都會成功，但這題應該回 false。",
 ],
 "follow": [
   ("h", "追問一：為什麼不能用 <code>try: float(s); return True</code>？"),
   ("c", """Python 的 float() 接受一些這題不允許的東西：

    float("inf")     -> inf      但題目要 false
    float("nan")     -> nan      但題目要 false
    float("  1.5  ") -> 1.5      有空白，題目要 false
    float("1_000")   -> 1000     底線分隔符（3.6+），題目要 false

所以這個「作弊法」會 WA。

更重要的是：這題的用意就是「實作一個 parser」，
用內建函式等於什麼都沒展示。

而且在真實工作裡，你很可能是在寫一個
「和某個規格完全一致」的 parser（例如 JSON、CSV、設定檔），
那時候內建函式的語意和你的規格幾乎不會完全吻合。""",),
   ("h", "追問二：這題和第 8 題（atoi）的關係？"),
   ("c", """第 8 題：解析出一個整數，遇到非法就停（不報錯）
第 65 題：判斷整個字串是否合法（要全對）

第 8 題的狀態機只有 4 個狀態，
第 65 題有 8 個 —— 因為多了小數點和指數。

兩題一起看，就能感受到「規格變複雜時，
狀態機的擴充性為什麼比 if-else 好」。

再往上就是 JSON parser、正規表示式引擎、
以及真正的程式語言 lexer —— 狀態數會到數十個。""",),
   ("h", "追問三：真正的浮點數規格有多複雜？"),
   "IEEE 754 的十進位字串表示還包括："
   "<code>Infinity</code>、<code>NaN</code>（還分 quiet 和 signaling）、"
   "十六進位浮點數（<code>0x1.8p3</code>）、"
   "以及各種語言自己加的糖（Python 的底線、C++ 的 <code>'</code> 分隔符）。"
   "<strong>「正確地解析一個浮點數」是一個出名地難的問題</strong> —— "
   "要做到「解析出的值是最接近的可表示浮點數」需要任意精度運算"
   "（著名的 Ryū 和 Grisu 演算法，以及 David Gay 的 <code>strtod</code>）。"
   "這題只是判斷語法，已經比那簡單太多了。",
 ],
 "related": [
   "<strong>第 8 題 String to Integer (atoi)</strong> —— 簡化版的狀態機",
   "<strong>第 7 題 Reverse Integer</strong> —— 同一家族的數字處理",
   "<strong>第 468 題 Validate IP Address</strong> —— 另一個規格驗證題",
 ],
 "check": [
   "<code>\"4.\"</code> 合法而 <code>\".\"</code> 不合法。你的程式碼裡哪一行造成這個差別？",
   "解法一裡 <code>seen_digit = False</code> 那一行在做什麼？拿掉的話哪一筆測資會錯？",
   "regex 為什麼要拆成 <code>\\d+\\.?\\d*</code> 和 <code>\\.\\d+</code> 兩個分支？",
   "為什麼 <code>try: float(s)</code> 會 WA？舉三個會出錯的輸入。",
 ],
})
print("P65 written")

# ==================== 66. Plus One ====================
S["p66_scan"] = '''class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 從個位往前掃：不是 9 就加一收工，是 9 就變 0 繼續進位
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # 走到這裡表示全部都是 9（例如 999 -> 000）
        return [1] + digits'''

S["p66_carry"] = '''class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 標準的「進位」寫法，比較容易推廣到「加上任意數」
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            total = digits[i] + carry
            digits[i] = total % 10
            carry = total // 10
            if carry == 0:
                break

        if carry:
            digits.insert(0, carry)
        return digits'''

_p66 = [S.load(k) for k in ("p66_scan", "p66_carry")]
for d in [[1, 2, 3], [4, 3, 2, 1], [9], [9, 9], [1, 9], [0], [9, 8, 9]]:
    e = [int(c) for c in str(int("".join(map(str, d))) + 1)]
    for sol in _p66:
        assert sol.plusOne(list(d)) == e, ("P66", d, sol, sol.plusOne(list(d)), e)
for _ in range(5000):
    k = random.randint(1, 8)
    d = [random.randint(1, 9)] + [random.randint(0, 9) for _ in range(k - 1)]
    e = [int(c) for c in str(int("".join(map(str, d))) + 1)]
    for sol in _p66:
        assert sol.plusOne(list(d)) == e, ("P66", d, sol)
print("P66 solutions OK")

emit({
 "num": 66, "slug": "plus-one",
 "en": [
   "You are given a <strong>large integer</strong> represented as an integer array "
   "<code>digits</code>, where each <code>digits[i]</code> is the <code>i</code>-th digit of "
   "the integer. The digits are ordered from most significant to least significant in "
   "left-to-right order.",
   "Increment the large integer by one and return <em>the resulting array of digits</em>.",
 ],
 "zh": [
   "給你一個用整數陣列表示的<strong>大整數</strong> <code>digits</code>，"
   "陣列由<strong>高位到低位</strong>排列（最左邊是最高位）。",
   "把這個大整數<strong>加一</strong>，回傳加完之後的陣列。",
 ],
 "pre": [
   ("note", "唯一的難點：進位", [
     ("c", """加一的三種情況：

  ① 個位不是 9         [1,2,3] -> [1,2,4]
     直接加，收工。

  ② 尾巴有一串 9        [1,9,9] -> [2,0,0]
     把那串 9 變成 0，然後前面那一位加一。

  ③ 全部都是 9         [9,9,9] -> [1,0,0,0]
     全部變 0，而且要在最前面補一個 1 —— 陣列變長了！

情況 ③ 是唯一會改變陣列長度的情況，
也是這題最常被漏掉的地方。

而且它只會發生一次（加一最多讓位數增加 1 位），
所以不需要迴圈處理。"""),
     "<strong>為什麼不直接轉成整數再加一？</strong>"
     "因為題目說「大整數」—— 在 C/Java 裡，100 位數遠超任何整數型別。"
     "<strong>Python 可以（<code>int(\"\".join(...)) + 1</code>），但那完全繞過了題目的用意。</strong>",
   ]),
 ],
 "examples": """範例 1
  輸入：digits = [1,2,3]
  輸出：[1,2,4]
  說明：123 + 1 = 124

範例 2
  輸入：digits = [4,3,2,1]
  輸出：[4,3,2,2]

範例 3
  輸入：digits = [9]
  輸出：[1,0]
  說明：9 + 1 = 10，陣列變長了。""",
 "constraints": [
   "1 ≤ <code>digits.length</code> ≤ 100",
   "0 ≤ <code>digits[i]</code> ≤ 9",
   "<code>digits</code> <strong>不含前導零</strong>，除了數字本身就是 <code>0</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>長度到 100</strong> —— 100 位數，遠超 64 位元整數（約 19 位）。"
       "<strong>這就是「不能轉成整數」的理由。</strong>",
       "<strong>沒有前導零</strong>（除了 <code>[0]</code> 本身）。"
       "所以輸出也不該有前導零 —— 只有情況 ③ 會在最前面加 1，那不是前導零。",
       "<strong><code>[0]</code> 是合法輸入</strong> → 輸出 <code>[1]</code>。",
     ]),
   ]),
 ],
 "idea": [
   "從<strong>最低位</strong>往前掃，遇到 9 就變 0 繼續，遇到非 9 就加一收工。"
   "如果掃完了還在進位，表示全是 9，在最前面補 1。",
 ],
 "approaches": [
   ap("解法一", "從後往前掃，提早退出（最短）", [
     ("c", S["p66_scan"]),
     ("h", "為什麼「不是 9 就可以直接 return」？"),
     ("c", """因為加一最多只產生一個進位。

如果 digits[i] < 9，那 digits[i] + 1 <= 9，
不會產生新的進位 —— 所以前面的位數完全不受影響，直接收工。

這讓大部分情況只跑一次迴圈：
    [1,2,3]  -> i = 2，3 < 9，加一，return  （只跑 1 次）
    [1,9,9]  -> i=2 是 9、i=1 是 9、i=0 是 1 < 9  （跑 3 次）

平均來說，有 90% 的機率個位不是 9，
所以這個解法的期望執行次數大約是 1.11 次 ——
非常接近 O(1)。"""),
     ("h", "最後那一行 <code>return [1] + digits</code>"),
     "走到這裡表示迴圈跑完了都沒有 return，"
     "也就是<strong>每一位都是 9</strong>，而且都已經被設成 0。"
     "此時只要在最前面補一個 1 就對了。",
     ("c", """[9,9,9]
    i=2: 9 -> 0
    i=1: 9 -> 0
    i=0: 9 -> 0
    迴圈結束，digits = [0,0,0]
    return [1] + [0,0,0] = [1,0,0,0] ✔

注意 [1] + digits 會建一個新 list（O(n)）。
如果要「原地」做，可以用 digits.insert(0, 1)，
但那在 Python 裡也是 O(n)（要搬移所有元素）。

C++ 的 vector 也一樣 —— 在前面插入是 O(n)。
如果這個操作很頻繁，應該考慮用 deque 或「反著存」。"""),
   ], "O(n) 最壞，平均 O(1)", "O(1)", "90% 的情況只跑一次",
      "原地修改；只有全 9 時才建新陣列", optimal=True),

   ap("解法二", "標準進位寫法（更容易推廣）", [
     ("c", S["p66_carry"]),
     "這是<strong>大數加法的標準骨架</strong>："
     "<code>total = 這一位 + 進位</code>、<code>這一位 = total % 10</code>、"
     "<code>進位 = total // 10</code>。",
     "<strong>優點</strong>：把 <code>carry = 1</code> 換成任意值，"
     "就變成「加上任意數」；再加一個迴圈變數就變成「兩個大數相加」（第 415 題）。"
     "<strong>可重用性遠高於解法一。</strong>",
     "<strong><code>if carry == 0: break</code></strong> 是效能優化 —— "
     "沒有它也對，只是會白跑完剩下的位數。",
     "<strong>缺點</strong>：比解法一長。在只做「加一」的場合是過度設計。",
   ], "O(n)", "O(1)", "同上", "原地修改"),
 ],
 "compare": (["解法", "行數", "可推廣到大數加法？", "備註"],
   [["一、掃描 + 提早退出", "7", "✘", "最短，面試預設"],
    ["二、標準進位", "12", "✔", "第 2、43、67、415 題的共同骨架"]]),
 "edges": [
   "<strong>不進位</strong>：<code>[1,2,3]</code> → <code>[1,2,4]</code>。",
   "<strong>單一個 9</strong>：<code>[9]</code> → <code>[1,0]</code>。",
   "<strong>全是 9</strong>：<code>[9,9]</code> → <code>[1,0,0]</code>。<strong>陣列變長。</strong>",
   "<strong>尾巴有 9</strong>：<code>[1,9]</code> → <code>[2,0]</code>。",
   "<strong>中間有 9</strong>：<code>[9,8,9]</code> → <code>[9,9,0]</code>。只進一位。",
   "<strong>零</strong>：<code>[0]</code> → <code>[1]</code>。",
   "<strong>最長</strong>：100 個 9 → 101 位。",
 ],
 "follow": [
   ("h", "追問一：如果要加上任意一個數 k 呢？"),
   "把 <code>carry = 1</code> 換成 <code>carry = k</code>。"
   "<strong>其餘完全不用改</strong> —— 因為 <code>total // 10</code> 會自動處理多位數的進位。",
   ("c", """[9, 9] 加上 123：
    carry = 123
    i=1: total = 9 + 123 = 132 -> digits[1] = 2, carry = 13
    i=0: total = 9 + 13  = 22  -> digits[0] = 2, carry = 2
    迴圈結束，carry = 2 -> insert(0, 2)
    結果 [2, 2, 2] = 222 ✔（99 + 123 = 222）

但如果 carry 是多位數，insert(0, carry) 就不對了 ——
要把 carry 拆成多位再插入。
所以「加上任意數」的完整版還要多幾行。""",),
   ("h", "追問二：如果是「減一」呢？"),
   "對稱的邏輯：<strong>從後往前掃，不是 0 就減一收工，是 0 就變 9 繼續借位</strong>。"
   "但多一個麻煩：<strong>結果可能有前導零</strong>"
   "（<code>[1,0,0] - 1 = [0,9,9]</code>，應該輸出 <code>[9,9]</code>），"
   "所以最後要去掉前導零。"
   "<strong>減法通常比加法麻煩，因為它會「縮短」而加法只會「變長」。</strong>",
   ("h", "追問三：為什麼陣列要「高位在前」？"),
   "因為那是<strong>人類閱讀的順序</strong>（123 就是 <code>[1,2,3]</code>）。"
   "但對<strong>運算</strong>來說，「低位在前」比較方便 —— "
   "進位是往高位傳的，如果低位在前，進位就是往陣列的後面傳，"
   "而且「變長」變成 <code>append</code>（O(1)）而不是 <code>insert(0, ...)</code>（O(n)）。",
   "<strong>所以真正的大數函式庫（GMP、Python 的 int）內部都是「低位在前」存的</strong>，"
   "只在輸出時才反轉。"
   "<strong>「內部表示」和「外部表示」可以不同 —— 這是一個很重要的設計觀念。</strong>",
 ],
 "related": [
   "<strong>第 2 題 Add Two Numbers</strong> —— 鏈結串列版（而且是低位在前！）",
   "<strong>第 43 題 Multiply Strings</strong> —— 大數乘法",
   "<strong>第 67 題 Add Binary</strong> —— 二進位版",
   "<strong>第 415 題 Add Strings</strong> —— 字串版的大數加法",
   "<strong>第 989 題 Add to Array-Form of Integer</strong> —— 本題「加上任意數」的版本",
 ],
 "check": [
   "為什麼「個位不是 9 就可以直接 return」？加一最多產生幾個進位？",
   "走到迴圈結束都沒 return，代表什麼？該怎麼處理？",
   "<code>[9,8,9]</code> 的答案是什麼？迴圈跑幾次？",
   "為什麼真正的大數函式庫用「低位在前」而不是「高位在前」？",
 ],
})
print("P66 written")
