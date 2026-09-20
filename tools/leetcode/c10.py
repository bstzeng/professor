# -*- coding: utf-8 -*-
"""第 10–12 題。"""
import random, re, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(10)

# ==================== 10. Regular Expression Matching ====================
S["p10_rec"] = '''class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def go(i: int, j: int) -> bool:
            """s[i:] 能不能被 p[j:] 完整匹配"""
            if j == len(p):
                return i == len(s)      # pattern 用完了，s 也要剛好用完

            # 第一個字元配不配得上（要先確認 s 還有字元可配）
            first = i < len(s) and p[j] in (s[i], ".")

            # 往後看一格是不是 '*'
            if j + 1 < len(p) and p[j + 1] == "*":
                # 兩條路：'x*' 整組不用（跳 2 格），或用掉一個 s 的字元（i 前進）
                return go(i, j + 2) or (first and go(i + 1, j))

            return first and go(i + 1, j + 1)

        return go(0, 0)'''

S["p10_memo"] = '''from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def go(i: int, j: int) -> bool:
            if j == len(p):
                return i == len(s)

            first = i < len(s) and p[j] in (s[i], ".")

            if j + 1 < len(p) and p[j + 1] == "*":
                return go(i, j + 2) or (first and go(i + 1, j))

            return first and go(i + 1, j + 1)

        result = go(0, 0)
        go.cache_clear()        # 避免不同測資之間互相污染
        return result'''

S["p10_dp"] = '''class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = s 的前 i 個字元，能不能被 p 的前 j 個字元匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True                       # 空 vs 空

        # 空字串 vs 只由 "x*" 組成的 pattern，例如 "a*b*c*"
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    # 情況 A：'x*' 當作出現 0 次 -> 直接看 p 少兩格的結果
                    dp[i][j] = dp[i][j - 2]
                    # 情況 B：'x*' 多吃一個 s[i-1]（前提是 x 配得上 s[i-1]）
                    if p[j - 2] in (s[i - 1], "."):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and p[j - 1] in (s[i - 1], ".")

        return dp[m][n]'''

_p10 = [S.load(k) for k in ("p10_rec", "p10_memo", "p10_dp")]
_cases10 = [("aa", "a"), ("aa", "a*"), ("ab", ".*"), ("aab", "c*a*b"),
            ("mississippi", "mis*is*p*."), ("", ""), ("", "a*"), ("", ".*"),
            ("a", ""), ("ab", ".*c"), ("aaa", "a*a"), ("aaa", "ab*a*c*a")]
for s_, p_ in _cases10:
    e = re.fullmatch(p_, s_) is not None
    for sol in _p10:
        assert sol.isMatch(s_, p_) == e, ("P10", s_, p_, sol, e)
for _ in range(1500):
    s_ = "".join(random.choice("ab") for _ in range(random.randint(0, 6)))
    toks = []
    for _ in range(random.randint(0, 4)):
        c = random.choice("ab.")
        toks.append(c + "*" if random.random() < 0.45 else c)
    p_ = "".join(toks)
    e = re.fullmatch(p_, s_) is not None
    for sol in _p10:
        assert sol.isMatch(s_, p_) == e, ("P10", repr(s_), repr(p_), sol, e)
print("P10 solutions OK")

_P10_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">dp 表：s = &quot;aab&quot;，p = &quot;c*a*b&quot;　（✔ = True）</text>
            <g font-family="monospace" font-size="13" text-anchor="middle">
              <text x="120" y="52" fill="var(--text-muted)">&quot;&quot;</text>
              <text x="180" y="52" fill="var(--accent)">c</text>
              <text x="240" y="52" fill="var(--accent)">*</text>
              <text x="300" y="52" fill="var(--accent)">a</text>
              <text x="360" y="52" fill="var(--accent)">*</text>
              <text x="420" y="52" fill="var(--accent)">b</text>
              <text x="70" y="52" fill="var(--text-muted)" font-size="11">p →</text>
              <text x="70" y="84" fill="var(--text-muted)">&quot;&quot;</text>
              <text x="70" y="116" fill="var(--gold)">a</text>
              <text x="70" y="148" fill="var(--gold)">a</text>
              <text x="70" y="180" fill="var(--gold)">b</text>
              <text x="30" y="116" fill="var(--text-muted)" font-size="11">s</text>
              <text x="30" y="136" fill="var(--text-muted)" font-size="11">↓</text>

              <text x="120" y="84" fill="var(--gold)">✔</text>
              <text x="180" y="84" fill="var(--text-muted)">·</text>
              <text x="240" y="84" fill="var(--gold)">✔</text>
              <text x="300" y="84" fill="var(--text-muted)">·</text>
              <text x="360" y="84" fill="var(--gold)">✔</text>
              <text x="420" y="84" fill="var(--text-muted)">·</text>

              <text x="120" y="116" fill="var(--text-muted)">·</text>
              <text x="180" y="116" fill="var(--text-muted)">·</text>
              <text x="240" y="116" fill="var(--text-muted)">·</text>
              <text x="300" y="116" fill="var(--gold)">✔</text>
              <text x="360" y="116" fill="var(--gold)">✔</text>
              <text x="420" y="116" fill="var(--text-muted)">·</text>

              <text x="120" y="148" fill="var(--text-muted)">·</text>
              <text x="180" y="148" fill="var(--text-muted)">·</text>
              <text x="240" y="148" fill="var(--text-muted)">·</text>
              <text x="300" y="148" fill="var(--text-muted)">·</text>
              <text x="360" y="148" fill="var(--gold)">✔</text>
              <text x="420" y="148" fill="var(--text-muted)">·</text>

              <text x="120" y="180" fill="var(--text-muted)">·</text>
              <text x="180" y="180" fill="var(--text-muted)">·</text>
              <text x="240" y="180" fill="var(--text-muted)">·</text>
              <text x="300" y="180" fill="var(--text-muted)">·</text>
              <text x="360" y="180" fill="var(--text-muted)">·</text>
              <text x="420" y="180" fill="#ff8a65">✔</text>
            </g>
            <rect x="400" y="164" width="40" height="24" rx="4" fill="none" stroke="#ff8a65" stroke-width="2"/>
            <text x="470" y="180" fill="#ff8a65" font-size="12">答案</text>
            <text x="20" y="216" fill="var(--text-muted)" font-size="12">第一列全靠 &quot;x*&quot; 當 0 次：dp[0][2] = dp[0][0]，dp[0][4] = dp[0][2]</text>
            <text x="20" y="238" fill="var(--gold)" font-size="12">dp[2][4]（&quot;aa&quot; vs &quot;c*a*&quot;）＝ a* 吃掉第二個 a → 看 dp[1][4] ✔</text>'''

emit({
 "num": 10, "slug": "regular-expression-matching",
 "en": [
   "Given an input string <code>s</code> and a pattern <code>p</code>, implement regular "
   "expression matching with support for <code>'.'</code> and <code>'*'</code> where:",
   "<code>'.'</code> matches any single character; <code>'*'</code> matches zero or more of "
   "the <strong>preceding</strong> element.",
   "The matching should cover the <strong>entire</strong> input string (not partial).",
 ],
 "zh": [
   "給你一個字串 <code>s</code> 和一個模式 <code>p</code>，實作支援 <code>'.'</code> 和 "
   "<code>'*'</code> 的正規表示式匹配：",
   "<code>'.'</code> 匹配<strong>任意單一字元</strong>；"
   "<code>'*'</code> 匹配<strong>它前面那個元素</strong>的零次或多次。",
   "匹配必須覆蓋<strong>整個</strong> <code>s</code>，不是部分匹配。",
 ],
 "pre": [
   ("note", "先把 '*' 的語意講死，這是全題的關鍵", [
     ("c", """'*' 不是獨立的萬用字元，它是「前一個元素的量詞」。
必須把 'x*' 當成一個不可分割的單位來看。

  "a*"   =  可以是 ""、"a"、"aa"、"aaa"…
  ".*"   =  可以是 ""、任意 1 個字元、任意 2 個字元…（等於萬用的一切）
  "a*b"  =  0 個以上的 a，然後一個 b  ->  "b"、"ab"、"aaab" ✔

常見誤解 1：以為 '*' 像 shell 的萬用字元（那是第 44 題 Wildcard Matching）
  shell:      "a*"  =  以 a 開頭的任何字串
  regex:      "a*"  =  只由 a 組成的字串（含空字串）
  完全不同！

常見誤解 2：忘了 '*' 可以吃 0 次
  s = "aab", p = "c*a*b"
  c* 吃 0 次、a* 吃 2 次、b 吃 1 次  ->  匹配成功 ✔
  漏掉「吃 0 次」這條路，這題就一定錯。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "aa", p = "a"
  輸出：false
  說明："a" 只能匹配一個 a，但 s 有兩個，不是「整個」匹配。

範例 2
  輸入：s = "aa", p = "a*"
  輸出：true
  說明：a* 可以匹配零個或多個 a，這裡吃兩個。

範例 3
  輸入：s = "ab", p = ".*"
  輸出：true
  說明：".*" 表示「零個或多個任意字元」。

範例 4
  輸入：s = "aab", p = "c*a*b"
  輸出：true
  說明：c* 吃 0 個 c，a* 吃 2 個 a，b 吃 1 個 b。

範例 5
  輸入：s = "mississippi", p = "mis*is*p*."
  輸出：false""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 20，1 ≤ <code>p.length</code> ≤ 20",
   "<code>s</code> 只含小寫英文字母",
   "<code>p</code> 只含小寫英文字母、<code>'.'</code>、<code>'*'</code>",
   "<strong>保證每個 <code>'*'</code> 前面都有一個有效的字元</strong>（不會出現 <code>\"*a\"</code> 或 <code>\"**\"</code>）",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>長度只有 20</strong>。這是在說：連純遞迴（指數級）都可能過得了 —— "
       "但別賭，加個記憶化只要多一行。",
       "<strong>「保證 * 前面有有效字元」是一個大禮。</strong>"
       "你完全不用檢查 <code>p[j-1]</code> 存不存在，"
       "也不用處理 <code>\"**\"</code> 這種病態輸入。沒有這條保證，這題會難上一倍。",
       "<strong>要「整個」匹配</strong>，所以終止條件是 <code>i == len(s) and j == len(p)</code>，"
       "對應 Python 的 <code>re.fullmatch</code> 而不是 <code>re.match</code>。",
     ]),
   ]),
 ],
 "idea": [
   "所有解法的骨架都一樣，差別只在「有沒有把算過的結果存起來」。"
   "先想清楚遞迴，DP 只是把同一個遞迴式從上往下改成從下往上。",
   ("h", "核心的分岔：看 p[j+1] 是不是 '*'"),
   ("c", """定義 go(i, j) = 「s[i:] 能不能被 p[j:] 完整匹配」

情況 1：p[j+1] 不是 '*'（或 j 已經是最後一格）
    只有一條路：s[i] 要配得上 p[j]，然後兩邊都前進一格。
        go(i, j) = first and go(i+1, j+1)

情況 2：p[j+1] 是 '*'    ← 這是唯一會分岔的地方
    兩條路，任一條通就算通：
      (A) 'x*' 用 0 次  ->  跳過這兩格：      go(i, j+2)
      (B) 'x*' 再吃一個  ->  s 前進、p 不動：  first and go(i+1, j)

        go(i, j) = go(i, j+2) or (first and go(i+1, j))

其中 first = (i < len(s)) and p[j] in (s[i], '.')

注意 (B) 為什麼 j 不動：
    因為 'x*' 可以吃任意多次，吃完一個之後它還在，下一輪還能再吃。""",),
 ],
 "approaches": [
   ap("解法一", "純遞迴（先把遞迴式寫對）", [
     ("c", S["p10_rec"]),
     ("h", "三個必須想清楚的細節"),
     ("ul", [
       "<strong><code>j == len(p)</code> 時要回 <code>i == len(s)</code>，不是 <code>True</code>。</strong>"
       "pattern 用完但 s 還有剩，那是匹配失敗。",
       "<strong><code>first</code> 一定要先檢查 <code>i &lt; len(s)</code>。</strong>"
       "s 已經用完時沒有 <code>s[i]</code> 可以配，但 pattern 可能還有一堆 <code>\"a*b*\"</code> "
       "要靠「吃 0 次」消化掉 —— 所以不能直接 return False。",
       "<strong>情況 2 的 <code>or</code> 順序有影響（效能上）。</strong>"
       "先試「吃 0 次」通常比較快收斂，因為它讓 j 前進了兩格，而「再吃一個」讓 j 原地不動。",
     ]),
     ("h", "為什麼會變成指數級？"),
     ("c", """s = "aaaaaaaaaaaaaaaaaaaa"  (20 個 a)
p = "a*a*a*a*a*a*a*a*a*a*"

每個 a* 都可以吃 0~20 個，組合數爆炸，
而且大量不同的路徑會走到同一個 (i, j) —— 重複計算。

這正是「加記憶化」的訊號：
狀態只有 (i, j)，最多 21 × 21 = 441 種，
但沒有快取的話同一個狀態會被重算幾十萬次。"""),
   ], "最壞 O(2^(m+n))", "O(m+n)", "大量重複子問題", "遞迴堆疊"),

   ap("解法二", "記憶化遞迴（加一行就好）", [
     "遞迴式一個字都不用改，只要在函式上掛一個 <code>@lru_cache</code>。"
     "狀態總數是 <code>(m+1) × (n+1)</code>，每個狀態算一次 O(1)，立刻變成多項式時間。",
     ("c", S["p10_memo"]),
     "<code>cache_clear()</code> 在 LeetCode 上其實不必要（每次呼叫都是新的 Solution 實例，"
     "但 <code>lru_cache</code> 掛在內層函式上，本來就會隨著外層函式結束而釋放）。"
     "寫上去是好習慣：如果把 <code>go</code> 提到類別層級，忘了清快取就會在跨測資時拿到錯的答案。",
     "<strong>面試時這是最推薦的寫法</strong>：遞迴式直接對應你剛剛在白板上推導的邏輯，"
     "不需要再花腦力去想「迴圈該從哪裡開始、邊界要怎麼初始化」。",
   ], "O(m·n)", "O(m·n)", "(m+1)(n+1) 個狀態 × O(1)", "快取表 + 遞迴堆疊"),

   ap("解法三", "自底向上 DP（把遞迴翻成表格）", [
     "定義改成<strong>前綴</strong>形式比較好寫邊界：<code>dp[i][j]</code> = "
     "「<code>s</code> 的前 <code>i</code> 個字元」能不能被「<code>p</code> 的前 <code>j</code> 個字元」匹配。"
     "注意此時 <code>s[i-1]</code> 才是第 i 個字元。",
     ("c", S["p10_dp"]),
     ("fig", _P10_FIG, "0 0 640 252"),
     ("h", "第一列（空字串）的初始化最容易漏"),
     ("c", """dp[0][j]：s 是空的，p 的前 j 個字元能不能匹配空字串？

只有一種可能：p 的前 j 個字元全部是 "x*" 的形式，每組都吃 0 次。

  p = "a*b*c*"
  dp[0][0] = True                （空 vs 空）
  dp[0][1] = False               （"a" 配不上空字串）
  dp[0][2] = dp[0][0] = True     （"a*" 吃 0 次）
  dp[0][3] = False               （"a*b" 裡的 b 配不上）
  dp[0][4] = dp[0][2] = True     （"a*b*" 都吃 0 次）
  dp[0][5] = False
  dp[0][6] = dp[0][4] = True

規律：只有 p[j-1] == '*' 時 dp[0][j] = dp[0][j-2]，其餘一律 False。

漏掉這一段的話，s = "aab"、p = "c*a*b" 會算成 False。"""),
     ("h", "為什麼 '*' 那一格要寫成兩行而不是一個 or？"),
     "因為情況 B 有前置條件：只有當 <code>p[j-2]</code>（也就是 <code>'*'</code> 前面那個字元）"
     "配得上 <code>s[i-1]</code> 時，才輪得到「多吃一個」這條路。"
     "寫成兩行（先給 A，再視情況 or 上 B）比塞進一個長運算式好讀，也比較不會把條件擺錯位置。",
     ("h", "空間可以壓到 O(n)"),
     "<code>dp[i][j]</code> 只依賴 <code>dp[i][*]</code>（同一列）和 <code>dp[i-1][j]</code>（上一列同欄），"
     "所以用兩條長度 n+1 的陣列滾動就夠。"
     "但 m, n ≤ 20，這個優化在這題沒有意義，講出來即可。",
   ], "O(m·n)", "O(m·n)", "填滿 (m+1)×(n+1) 的表", "可滾動壓到 O(n)", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "好寫程度", "備註"],
   [["一、純遞迴", "最壞 O(2^(m+n))", "O(m+n)", "★★★★☆", "先寫它來確認遞迴式"],
    ["二、記憶化", "O(m·n)", "O(m·n)", "★★★★☆", "面試首選：加一行就達標"],
    ["三、自底向上 DP", "O(m·n)", "O(m·n)→O(n)", "★★☆☆☆", "邊界最多，但不吃遞迴深度"]]),
 "post": [
   ("note", "和第 44 題 Wildcard Matching 的差別", [
     ("c", """第 10 題（本題）              第 44 題 Wildcard Matching
------------------------      ------------------------
'.'  配任意「一個」字元        '?'  配任意「一個」字元
'*'  前一個元素重複 0+ 次      '*'  自己就配任意「一段」（含空）

關鍵差異：
  第 10 題的 '*' 要往前看一格（p[j-1] 是誰）；
  第 44 題的 '*' 是獨立的，不依賴前面。

所以第 44 題可以用貪婪 + 回溯做到 O(1) 空間，
第 10 題不行 —— 'x*' 的耦合讓貪婪失效。

兩題常被搞混，面試前建議放在一起讀。"""),
   ]),
 ],
 "edges": [
   "<strong><code>p</code> 裡的 <code>\"x*\"</code> 要吃 0 次</strong>：<code>(\"aab\", \"c*a*b\")</code> → true。漏掉這條路是第一名錯誤。",
   "<strong><code>s</code> 空、<code>p</code> 非空</strong>：<code>(\"\", \"a*\")</code> → true；<code>(\"\", \"a\")</code> → false。",
   "<strong><code>s</code> 非空、<code>p</code> 空</strong>：<code>(\"a\", \"\")</code> → false。",
   "<strong>連續多個 <code>\"x*\"</code></strong>：<code>(\"\", \"a*b*c*\")</code> → true。考驗第一列的初始化。",
   "<strong><code>\".*\"</code></strong>：<code>(\"ab\", \".*\")</code> → true。<code>'.'</code> 和 <code>'*'</code> 疊在一起。",
   "<strong>貪婪會出錯的例子</strong>：<code>(\"aaa\", \"a*a\")</code> → true。"
   "若讓 <code>a*</code> 貪婪吃光三個 a，後面的 <code>a</code> 就沒東西配了 —— "
   "必須能「退回來」少吃一個。這正是 DP 兩條路都要試的原因。",
   "<strong>長度到上限</strong>：20 個 a 配 <code>\"a*\"×10</code>，純遞迴會明顯變慢。",
 ],
 "follow": [
   ("h", "追問一：要支援 <code>'+'</code>（一次以上）呢？"),
   "最省事的做法是<strong>改寫 pattern</strong>：把 <code>\"x+\"</code> 換成 <code>\"xx*\"</code>，"
   "然後完全沿用現有的程式碼。"
   "這也是很多 regex 引擎內部的做法 —— 先正規化（desugar），再交給核心引擎。",
   ("h", "追問二：真正的 regex 引擎是怎麼做的？"),
   "兩大流派：<strong>回溯式</strong>（Perl、Python 的 <code>re</code>、Java）"
   "和 <strong>自動機式</strong>（NFA/DFA，如 RE2、Go 的 <code>regexp</code>）。"
   "回溯式支援 backreference 這類強大但無法用自動機表達的功能，代價是最壞情況會指數爆炸"
   "（著名的 ReDoS 攻擊，例如 <code>(a+)+$</code> 配上一串 a）。"
   "自動機式保證線性時間，但功能受限。"
   "<strong>本題的 DP 解本質上就是自動機式的做法</strong> —— 這是很好的延伸話題。",
   ("h", "追問三：如果 pattern 要重複用在很多字串上？"),
   "那就把 pattern <strong>預編譯</strong>成自動機（狀態轉移表），"
   "之後每個字串只要 O(len(s)) 掃一遍即可，不必每次重跑 O(m·n) 的 DP。"
   "這正是 <code>re.compile</code> 存在的理由。",
 ],
 "related": [
   "<strong>第 44 題 Wildcard Matching</strong> —— <code>'*'</code> 語意不同的姊妹題",
   "<strong>第 72 題 Edit Distance</strong> —— 同樣是兩個字串的二維 DP",
   "<strong>第 97 題 Interleaving String</strong> —— 兩指標 DP 的另一個變形",
 ],
 "check": [
   "<code>(\"aaa\", \"a*a\")</code> 為什麼是 true？如果用「<code>a*</code> 貪婪吃到底」的寫法會得到什麼？",
   "DP 第一列的初始化 <code>dp[0][j] = dp[0][j-2]</code>，為什麼是減 2 而不是減 1？",
   "把遞迴裡 <code>first</code> 的 <code>i &lt; len(s)</code> 拿掉，哪一筆測資會 IndexError？",
   "狀態總共有幾個？為什麼加了 <code>lru_cache</code> 之後複雜度就從指數變成 O(m·n)？",
 ],
})
print("P10 written")

# ==================== 11. Container With Most Water ====================
S["p11_brute"] = '''class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                best = max(best, (j - i) * min(height[i], height[j]))
        return best'''

S["p11_two"] = '''class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        best = 0

        while lo < hi:
            h = min(height[lo], height[hi])
            best = max(best, (hi - lo) * h)

            # 移動「比較矮」的那一邊。矮的那邊是瓶頸，
            # 留著它只會讓寬度變小而高度不變 -> 不可能更好
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1

        return best'''

S["p11_skip"] = '''class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        best = 0

        while lo < hi:
            h = min(height[lo], height[hi])
            best = max(best, (hi - lo) * h)

            # 小優化：一路跳過所有不比 h 高的柱子
            # （它們當瓶頸時高度不會變好，寬度又更小）
            if height[lo] < height[hi]:
                while lo < hi and height[lo] <= h:
                    lo += 1
            else:
                while lo < hi and height[hi] <= h:
                    hi -= 1

        return best'''

_p11 = [S.load(k) for k in ("p11_brute", "p11_two", "p11_skip")]
assert _p11[0].maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert _p11[0].maxArea([1, 1]) == 1
for _ in range(4000):
    a = [random.randint(0, 12) for _ in range(random.randint(2, 10))]
    e = _p11[0].maxArea(a)
    for sol in _p11:
        assert sol.maxArea(a) == e, ("P11", a, sol, e)
print("P11 solutions OK")

_P11_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">height = [1, 8, 6, 2, 5, 4, 8, 3, 7]，答案是 49（索引 1 與 8，寬 7 × 高 7）</text>
            <g>
              <rect x="60" y="192" width="14" height="16" fill="var(--border)"/>
              <rect x="120" y="80" width="14" height="128" fill="var(--gold)"/>
              <rect x="180" y="112" width="14" height="96" fill="var(--border)"/>
              <rect x="240" y="176" width="14" height="32" fill="var(--border)"/>
              <rect x="300" y="128" width="14" height="80" fill="var(--border)"/>
              <rect x="360" y="144" width="14" height="64" fill="var(--border)"/>
              <rect x="420" y="80" width="14" height="128" fill="var(--border)"/>
              <rect x="480" y="160" width="14" height="48" fill="var(--border)"/>
              <rect x="540" y="96" width="14" height="112" fill="var(--gold)"/>
              <rect x="134" y="96" width="406" height="112" fill="var(--accent)" opacity="0.16"/>
              <line x1="60" y1="208" x2="580" y2="208" stroke="var(--text-muted)" stroke-width="1"/>
            </g>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="67" y="224">0</text><text x="127" y="224">1</text><text x="187" y="224">2</text>
              <text x="247" y="224">3</text><text x="307" y="224">4</text><text x="367" y="224">5</text>
              <text x="427" y="224">6</text><text x="487" y="224">7</text><text x="547" y="224">8</text>
            </g>
            <g font-size="11" text-anchor="middle">
              <text x="67" y="186" fill="var(--text-muted)">1</text>
              <text x="127" y="74" fill="var(--gold)">8</text>
              <text x="187" y="106" fill="var(--text-muted)">6</text>
              <text x="247" y="170" fill="var(--text-muted)">2</text>
              <text x="307" y="122" fill="var(--text-muted)">5</text>
              <text x="367" y="138" fill="var(--text-muted)">4</text>
              <text x="427" y="74" fill="var(--text-muted)">8</text>
              <text x="487" y="154" fill="var(--text-muted)">3</text>
              <text x="547" y="90" fill="var(--gold)">7</text>
            </g>
            <text x="337" y="156" fill="var(--accent)" font-size="13" text-anchor="middle">面積 = 7 × 7 = 49</text>
            <text x="20" y="252" fill="var(--text-muted)" font-size="12">水位由「比較矮的那根」決定 —— 中間的柱子完全不影響（這點和第 42 題接雨水不同）</text>'''

emit({
 "num": 11, "slug": "container-with-most-water",
 "en": [
   "You are given an integer array <code>height</code> of length <code>n</code>. There are "
   "<code>n</code> vertical lines drawn such that the two endpoints of the "
   "<code>i</code>-th line are <code>(i, 0)</code> and <code>(i, height[i])</code>.",
   "Find two lines that together with the x-axis form a container, such that the container "
   "contains the most water. Return <em>the maximum amount of water a container can store</em>.",
   "Notice that you may not slant the container.",
 ],
 "zh": [
   "給你一個長度為 <code>n</code> 的整數陣列 <code>height</code>。"
   "第 <code>i</code> 根垂直線的兩端點是 <code>(i, 0)</code> 和 <code>(i, height[i])</code>。",
   "找出兩根線，讓它們和 x 軸圍成的容器能裝<strong>最多的水</strong>，回傳這個最大容量。",
   "注意：容器不能傾斜。",
 ],
 "pre": [
   ("note", "面積公式與一個關鍵觀察", [
     ("c", """選第 i 根和第 j 根（i < j）：

    面積 = 寬 × 高
         = (j - i) × min(height[i], height[j])

「高」取 min 是因為水會從比較矮的那一邊溢出來。

關鍵觀察：中間的柱子完全不影響答案。
  容器就是兩片牆加底部，中間有什麼都無所謂。
  （這點和第 42 題「接雨水」剛好相反 —— 那題中間的柱子會佔掉體積。）"""),
   ]),
 ],
 "examples": """範例 1
  輸入：height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
  輸出：49
  說明：選索引 1（高 8）和索引 8（高 7），
        面積 = (8 - 1) × min(8, 7) = 7 × 7 = 49。

範例 2
  輸入：height = [1, 1]
  輸出：1
  說明：唯一的選擇，面積 = 1 × 1 = 1。""",
 "constraints": [
   "<code>n == height.length</code>",
   "2 ≤ <code>n</code> ≤ 10⁵",
   "0 ≤ <code>height[i]</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n 可以到 10⁵</strong>。O(n²) 是 10¹⁰ —— 絕對 TLE。"
       "這個數字就是在告訴你：<strong>必須找到 O(n) 或 O(n log n) 的解</strong>。",
       "<strong><code>height[i]</code> 可以是 0</strong>。高度 0 的柱子當牆時面積是 0，"
       "不會是答案，但也不會讓程式出錯 —— 不用特別處理。",
       "<strong>n 至少是 2</strong>，所以一定存在至少一組答案，不必處理「找不到」。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P11_FIG, "0 0 640 266"),
   "暴力法要試 C(n,2) ≈ n²/2 組。要降到 O(n)，得找到一個理由，"
   "能讓我們<strong>一口氣排除掉大量組合</strong>而不用一一驗算 —— 這就是雙指標的價值。",
 ],
 "approaches": [
   ap("解法一", "暴力列舉所有配對", [
     ("c", S["p11_brute"]),
     "正確但 O(n²)，在 n = 10⁵ 時穩定 TLE。"
     "還是值得寫出來 —— 它是驗證雙指標的標準答案（本篇的壓力測試就是拿它當基準）。",
   ], "O(n²)", "O(1)", "所有 C(n,2) 對", "只有一個 best"),

   ap("解法二", "雙指標從兩端夾（關鍵在證明）", [
     "從<strong>最寬</strong>的一組開始：<code>lo = 0</code>、<code>hi = n-1</code>。"
     "然後每一步<strong>丟掉比較矮的那一根</strong>，往中間收縮。",
     ("h", "為什麼可以放心丟掉矮的那一根？（這是整題唯一需要證明的地方）"),
     ("c", """假設現在 height[lo] < height[hi]，也就是 lo 這根比較矮。

考慮所有「還包含 lo 這根」的組合：(lo, k)，其中 lo < k < hi。

  寬度：k - lo  <  hi - lo        （k 在 hi 左邊，一定更窄）
  高度：min(height[lo], height[k])  ≤  height[lo]
                                    =  min(height[lo], height[hi])
        （因為 height[lo] 本來就是兩者中較小的，
          不管 height[k] 多高，min 都不會超過 height[lo]）

  所以：面積(lo, k)  <  面積(lo, hi)     嚴格更小

結論：(lo, hi) 已經是「所有包含 lo 的組合」裡最好的那個。
      既然它已經被記錄下來了，lo 就再也沒有用處 —— 安全丟棄。

同理，如果 hi 比較矮，就丟 hi。

每一步丟掉一根柱子，n 根柱子最多丟 n 次 -> O(n)。"""),
     ("c", S["p11_two"]),
     ("h", "兩根一樣高的時候丟哪一根？"),
     "都可以。上面的程式碼寫 <code>if height[lo] &lt; height[hi]</code>，"
     "相等時走 else 丟 <code>hi</code>。"
     "證明同樣成立（相等時兩邊的論證對稱），所以不會漏掉答案。",
     ("h", "常見的錯誤直覺"),
     ("c", """錯誤想法：「應該移動比較高的那一邊，才能找到更高的牆」

反例： height = [2, 3, 10, 5, 7, 8, 9]
       lo = 0 (高 2)，hi = 6 (高 9)，面積 = 6 × 2 = 12

       若移動比較高的 hi：hi = 5 (高 8)，面積 = 5 × 2 = 10  變小了
       而且 lo 這根高度 2 還在，它永遠是瓶頸，
       不管右邊怎麼換，高度都被鎖死在 2，寬度卻一直縮 -> 只會越來越差。

正確的做法是丟掉瓶頸（矮的那根），才有機會讓高度上升。"""),
   ], "O(n)", "O(1)", "兩個指標合計走 n 步", "只用幾個變數", optimal=True),

   ap("解法三", "雙指標 + 跳過無用柱子（同複雜度的常數優化）", [
     "在移動指標時，可以一口氣跳過所有「不比目前水位高」的柱子 —— "
     "它們當瓶頸時高度不會更好，寬度又更小，一定不是答案。",
     ("c", S["p11_skip"]),
     "最壞情況（遞增序列）還是 O(n)，"
     "但在高度分布隨機時實測能少跑不少輪。<strong>複雜度沒變，只是常數更小。</strong>",
     "面試時提一句就好，不必為了它把主解法寫複雜。",
   ], "O(n)", "O(1)", "最壞仍是 n 步，平均更少", "只用幾個變數"),
 ],
 "compare": (["解法", "時間", "空間", "n = 10⁵ 能過？", "備註"],
   [["一、暴力", "O(n²)", "O(1)", "✘", "當測試基準"],
    ["二、雙指標", "O(n)", "O(1)", "✔", "標準解，重點是講清楚證明"],
    ["三、雙指標 + 跳過", "O(n)", "O(1)", "✔", "常數優化，加分項"]]),
 "edges": [
   "<strong>只有兩根</strong>：<code>[1,1]</code> → 1。while 迴圈只跑一輪。",
   "<strong>全部一樣高</strong>：<code>[5,5,5,5]</code> → 15（最寬的那組）。相等時的分支要能正確前進，否則死循環。",
   "<strong>遞增序列</strong>：<code>[1,2,3,4,5]</code> → 6（索引 1 與 4）。答案不在最寬的那組。",
   "<strong>遞減序列</strong>：<code>[5,4,3,2,1]</code> → 6。對稱的情況。",
   "<strong>含 0</strong>：<code>[0,2,0]</code> → 0。高度 0 不會讓程式出錯。",
   "<strong>最高的兩根不是答案</strong>：<code>[2,100,3,4,5,100,2]</code> 的答案確實是那兩根 100；"
   "但 <code>[100,1,1,1,1,99]</code> 的答案是 <code>5 × 99 = 495</code>，"
   "不是「相鄰的兩根最高」。<strong>寬度和高度要一起看。</strong>",
 ],
 "follow": [
   ("h", "追問一：這題和第 42 題「接雨水」差在哪？"),
   ("c", """第 11 題（本題）                 第 42 題 Trapping Rain Water
------------------------        ------------------------
只選「兩根」當牆                 每一格都要算能積多少水
中間的柱子被忽略                 中間的柱子會佔掉體積
答案是一個矩形面積                答案是所有格子的總和
雙指標從兩端夾                   雙指標 / 單調堆疊 / 前後綴最大值

雖然都用雙指標、都在柱狀圖上，但問的東西完全不同。
第 11 題「水會漫過中間的柱子」，第 42 題不會。
這兩題常被放在一起考，建議連著練。"""),
   ("h", "追問二：如果容器可以由三片牆組成呢？"),
   "問題會變得複雜很多，雙指標的證明不再成立（丟掉一根柱子可能同時破壞好幾組候選）。"
   "通常要退回 DP 或分治。<strong>雙指標之所以能用，完全依賴「答案只由兩個端點決定」這個結構。</strong>",
   ("h", "追問三：如果要回傳那兩根柱子的索引，而不只是面積？"),
   "在更新 <code>best</code> 的時候一併記下 <code>(lo, hi)</code> 即可，複雜度不變。"
   "唯一要注意的是：答案可能不唯一，要先問清楚「任一組」還是「字典序最小的那組」。",
 ],
 "related": [
   "<strong>第 42 題 Trapping Rain Water</strong> —— 同一張柱狀圖，完全不同的問題",
   "<strong>第 84 題 Largest Rectangle in Histogram</strong> —— 柱狀圖 + 單調堆疊",
   "<strong>第 15 題 3Sum</strong> —— 雙指標的另一個經典應用",
 ],
 "check": [
   "請完整說出「為什麼可以丟掉矮的那一根」的證明，包含寬度和高度兩個部分。",
   "如果改成「移動比較高的那一根」，在 <code>[2,3,10,5,7,8,9]</code> 上會得到什麼答案？正確答案是多少？",
   "兩根一樣高時，丟左邊和丟右邊會得到一樣的答案嗎？為什麼？",
   "雙指標為什麼是 O(n) 而不是 O(n²)？每一輪確切減少了什麼？",
 ],
})
print("P11 written")

# ==================== 12. Integer to Roman ====================
S["p12_greedy"] = '''class Solution:
    def intToRoman(self, num: int) -> str:
        # 由大到小，並且把 6 個「減法形式」當成獨立的符號插進去
        VALUES = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100,  "C"), (90,  "XC"), (50,  "L"), (40,  "XL"),
            (10,   "X"), (9,   "IX"), (5,   "V"), (4,   "IV"),
            (1,    "I"),
        ]

        out = []
        for value, symbol in VALUES:
            if num == 0:
                break
            count, num = divmod(num, value)
            out.append(symbol * count)

        return "".join(out)'''

S["p12_table"] = '''class Solution:
    def intToRoman(self, num: int) -> str:
        # 每一位數（千、百、十、個）的寫法直接查表，完全不用算
        THOUSANDS = ["", "M", "MM", "MMM"]
        HUNDREDS  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        TENS      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ONES      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (THOUSANDS[num // 1000]
                + HUNDREDS[num % 1000 // 100]
                + TENS[num % 100 // 10]
                + ONES[num % 10])'''

_p12a, _p12b = S.load("p12_greedy"), S.load("p12_table")


def _roman_ref(n):
    # 獨立寫的參考實作：直接照羅馬數字規則展開
    digits = [int(c) for c in "%04d" % n]
    sym = [("M", "", ""), ("C", "D", "M"), ("X", "L", "C"), ("I", "V", "X")]
    out = []
    for d, (one, five, ten) in zip(digits, sym):
        if d <= 3:
            out.append(one * d)
        elif d == 4:
            out.append(one + five)
        elif d <= 8:
            out.append(five + one * (d - 5))
        else:
            out.append(one + ten)
    return "".join(out)


assert _p12a.intToRoman(3749) == "MMMDCCXLIX"
assert _p12a.intToRoman(58) == "LVIII"
assert _p12a.intToRoman(1994) == "MCMXCIV"
for n in range(1, 4000):
    e = _roman_ref(n)
    assert _p12a.intToRoman(n) == e, ("P12 greedy", n, _p12a.intToRoman(n), e)
    assert _p12b.intToRoman(n) == e, ("P12 table", n, _p12b.intToRoman(n), e)
print("P12 solutions OK")

emit({
 "num": 12, "slug": "integer-to-roman",
 "en": [
   "Seven different symbols represent Roman numerals with the following values: "
   "<code>I=1, V=5, X=10, L=50, C=100, D=500, M=1000</code>.",
   "Roman numerals are formed by appending the conversions of decimal place values from "
   "highest to lowest. If the value starts with 4 or 9, use the "
   "<strong>subtractive form</strong> (<code>IV, IX, XL, XC, CD, CM</code>).",
   "Given an integer, convert it to a Roman numeral.",
 ],
 "zh": [
   "羅馬數字用七個符號表示：<code>I=1, V=5, X=10, L=50, C=100, D=500, M=1000</code>。",
   "寫法是<strong>由高位到低位</strong>依序寫出每一個位數的表示。"
   "如果某一位是 4 或 9，要用<strong>減法形式</strong>"
   "（<code>IV=4, IX=9, XL=40, XC=90, CD=400, CM=900</code>）。",
   "給你一個整數，把它轉成羅馬數字。",
 ],
 "pre": [
   ("note", "六個減法形式，就是這題的全部規則", [
     ("c", """基本符號：
    I = 1     V = 5     X = 10    L = 50
    C = 100   D = 500   M = 1000

減法形式（只有這六個，沒有別的）：
    IV = 4     IX = 9
    XL = 40    XC = 90
    CD = 400   CM = 900

規律：只有 I、X、C 可以放在別人左邊做減法，
      而且只能放在「它的 5 倍」和「它的 10 倍」左邊。
      V、L、D、M 永遠不做減數。

所以 IL（49）、IC（99）、VX 都是「不合法」的寫法。
正確的 49 是 XLIX（40 + 9），99 是 XCIX（90 + 9）。"""),
     "<strong>把這六個減法形式當成「額外的六個符號」</strong>，"
     "整個問題就退化成最單純的貪婪找零錢 —— 這是解法一的全部洞察。",
   ]),
 ],
 "examples": """範例 1
  輸入：num = 3749
  輸出："MMMDCCXLIX"
  說明：3000 = MMM
        700  = DCC
        40   = XL
        9    = IX

範例 2
  輸入：num = 58
  輸出："LVIII"
  說明：50 = L，8 = VIII

範例 3
  輸入：num = 1994
  輸出："MCMXCIV"
  說明：1000 = M，900 = CM，90 = XC，4 = IV""",
 "constraints": [
   "1 ≤ <code>num</code> ≤ 3999",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>上限是 3999</strong>，因為標準羅馬數字最大的符號是 M（1000），"
       "而規則不允許連寫四個 M。4000 要寫成 <code>M̄V</code>（上加橫線表示 ×1000），"
       "這個延伸規則題目不考。",
       "<strong>下限是 1</strong>，<strong>羅馬數字沒有 0</strong>，也沒有負數。"
       "這讓所有邊界處理都省掉了。",
       "範圍固定又小，所以<strong>查表法（解法二）是完全合理的</strong> —— "
       "四張表加起來只有 34 個字串。",
     ]),
   ]),
 ],
 "idea": [
   "兩種思路，都是 O(1)：",
   ("t", ["解法", "想法", "表格大小"],
     [["一、貪婪找零", "由大到小，能減就減；把 6 個減法形式當成獨立符號", "13 筆"],
      ["二、位數查表", "千百十個各查一張表，接起來就好", "34 筆"]]),
 ],
 "approaches": [
   ap("解法一", "貪婪：把減法形式當成獨立符號", [
     "直覺上會擔心「貪婪會不會出錯」（像找零錢問題裡某些幣值組合會讓貪婪失效）。"
     "但羅馬數字的符號值刻意設計成 <strong>1, 4, 5, 9, 10, 40, 50, 90, …</strong> 這樣的序列，"
     "每一個都能被更小的組合精確補齊，貪婪保證最優。",
     ("c", S["p12_greedy"]),
     ("h", "追一遍 num = 1994"),
     ("c", """num = 1994

1000 "M"  : divmod(1994, 1000) = (1, 994)   -> "M"      num = 994
 900 "CM" : divmod(994, 900)   = (1, 94)    -> "CM"     num = 94
 500 "D"  : divmod(94, 500)    = (0, 94)    -> ""       num = 94
 400 "CD" : (0, 94)                          -> ""
 100 "C"  : (0, 94)                          -> ""
  90 "XC" : divmod(94, 90)     = (1, 4)     -> "XC"     num = 4
  50 "L"  : (0, 4)                           -> ""
  40 "XL" : (0, 4)                           -> ""
  10 "X"  : (0, 4)                           -> ""
   9 "IX" : (0, 4)                           -> ""
   5 "V"  : (0, 4)                           -> ""
   4 "IV" : divmod(4, 4)       = (1, 0)     -> "IV"     num = 0
                                                break

結果："M" + "CM" + "XC" + "IV" = "MCMXCIV" ✔"""),
     ("h", "為什麼 VALUES 的順序絕對不能亂？"),
     "必須嚴格<strong>由大到小</strong>。特別是 <code>900 \"CM\"</code> 一定要排在 "
     "<code>500 \"D\"</code> 前面 —— 否則 900 會先被拆成 <code>D</code>(500) + "
     "<code>CCCC</code>(400)，得到 <code>\"DCCCC\"</code>，那不是合法的羅馬數字。",
     "<strong><code>count</code> 最多是 3。</strong>"
     "因為相鄰兩個符號值的比例最多是 4（例如 1000/900、100/90），"
     "而減法形式把 4 和 9 都攔截掉了，所以 <code>symbol * count</code> "
     "最多重複三次 —— 剛好符合羅馬數字「同一符號不連寫四次」的規則。"
     "<strong>這不是巧合，是那個 VALUES 表刻意設計的結果。</strong>",
   ], "O(1)", "O(1)", "固定 13 次迴圈", "輸出最多 15 個字元（3888 = MMMDCCCLXXXVIII）", optimal=True),

   ap("解法二", "位數查表（最快，也最好讀）", [
     "既然只有四個十進位位數，而每一位只有 0–9 十種可能，"
     "那就<strong>把 4 × 10 = 40 種情況全部列出來</strong>（實際只要 34 筆，千位只到 3）。",
     ("c", S["p12_table"]),
     ("h", "四張表的規律"),
     ("c", """每一張表的結構都一樣，只是換符號：

  位數   1 的符號  5 的符號  10 的符號
  ----   --------  --------  ---------
  個位     I         V         X
  十位     X         L         C
  百位     C         D         M
  千位     M         -         -      （沒有 5000、10000 的符號，所以只到 MMM）

  d = 0 : ""
  d = 1~3 : one * d          (I, II, III)
  d = 4 : one + five         (IV)
  d = 5 : five               (V)
  d = 6~8 : five + one*(d-5) (VI, VII, VIII)
  d = 9 : one + ten          (IX)

如果覺得手寫四張表很醜，也可以用上面這個規律在程式裡生出來 ——
但既然只有 34 筆，寫死反而更清楚、更不容易錯。"""),
     "<strong>這是本題最快的解法</strong>：沒有迴圈，就四次除法取模加四次陣列索引。"
     "也最不容易寫錯 —— 因為所有規則都變成了資料，而資料可以一眼看完、一眼檢查。",
     "<strong>這體現一個很實用的原則：能用資料表達的，就不要用控制流程表達。</strong>"
     "表格可以被檢查、被測試、被生成；散落在 if-else 裡的規則不行。",
   ], "O(1)", "O(1)", "四次查表", "34 個常數字串"),
 ],
 "compare": (["解法", "時間", "好讀程度", "容易寫錯的地方"],
   [["一、貪婪", "O(1)（13 輪）", "★★★★☆", "VALUES 的順序排錯"],
    ["二、位數查表", "O(1)（4 次）", "★★★★★", "表本身打錯字"]]),
 "edges": [
   "<strong>最小值 1</strong> → <code>\"I\"</code>。",
   "<strong>最大值 3999</strong> → <code>\"MMMCMXCIX\"</code>。",
   "<strong>每個減法形式都要單獨測</strong>：4 → IV，9 → IX，40 → XL，90 → XC，400 → CD，900 → CM。",
   "<strong>輸出最長的情況</strong>：3888 → <code>\"MMMDCCCLXXXVIII\"</code>（15 個字元）。",
   "<strong>某些位數是 0</strong>：1000 → <code>\"M\"</code>，2020 → <code>\"MMXX\"</code>。查表法自動回空字串。",
   "<strong>49 和 99</strong>：<code>\"XLIX\"</code> 和 <code>\"XCIX\"</code>，"
   "不是 <code>\"IL\"</code> 和 <code>\"IC\"</code>。最能驗證你有沒有搞錯減法規則。",
 ],
 "follow": [
   ("h", "追問一：如果要支援大於 3999 呢？"),
   "標準做法是用上劃線（vinculum）表示乘以 1000：<code>V̄</code> = 5000、<code>X̄</code> = 10000。"
   "程式上就是在 VALUES 表前面補上這些符號。"
   "但這已經不是「標準羅馬數字」的範圍，實作前要先跟出題者確認規格。",
   ("h", "追問二：貪婪為什麼在這裡一定對？找零錢問題不是常常會失敗嗎？"),
   "找零錢的貪婪確實會失敗 —— 經典反例是幣值 <code>{1, 3, 4}</code> 湊 6："
   "貪婪拿 4+1+1 三枚，最優是 3+3 兩枚。"
   "羅馬數字之所以安全，是因為它的值序列 <code>1,4,5,9,10,40,50,90,100,400,500,900,1000</code> "
   "具有一個特殊性質：<strong>每個值都整除或被下一個大值「幾乎整除」，"
   "而餘數永遠能被更小的符號在 3 個以內補完</strong>。"
   "能講出這個差別，比只說「貪婪就是對的」有說服力得多。",
   ("h", "追問三：反過來，羅馬數字轉整數呢？"),
   "就是下一題（第 13 題）。核心技巧是：<strong>由左往右掃，如果當前符號比右邊的小就減、否則就加</strong>。"
   "反向轉換反而比正向簡單，因為不用煩惱「該用哪種寫法」。",
 ],
 "related": [
   "<strong>第 13 題 Roman to Integer</strong> —— 反方向",
   "<strong>第 273 題 Integer to English Words</strong> —— 同樣是「數字轉表示法」，但規則多很多",
 ],
 "check": [
   "如果把 VALUES 裡的 <code>(900, \"CM\")</code> 移到 <code>(500, \"D\")</code> 後面，1994 會變成什麼？",
   "為什麼 <code>symbol * count</code> 裡的 <code>count</code> 不可能是 4？",
   "49 的正確寫法是什麼？為什麼不是 <code>\"IL\"</code>？",
   "查表法的四張表為什麼千位只有 4 筆而其他是 10 筆？",
 ],
})
print("P12 written")
