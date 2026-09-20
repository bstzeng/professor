# -*- coding: utf-8 -*-
"""第 97–98 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(97)


# ==================== 97. Interleaving String ====================
S["p97_dp2d"] = '''class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False                  # 長度對不上，直接 False

        # dp[i][j] = s1 的前 i 個字 + s2 的前 j 個字，
        #            能不能交錯出 s3 的前 i+j 個字
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True                   # 兩邊都不取，交錯出空字串

        # 第一列：完全不用 s1，只用 s2
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

        # 第一欄：完全不用 s2，只用 s1
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j - 1             # s3 目前要對上的位置
                dp[i][j] = ((dp[i - 1][j] and s1[i - 1] == s3[k]) or
                            (dp[i][j - 1] and s2[j - 1] == s3[k]))

        return dp[m][n]'''

S["p97_dp1d"] = '''class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        if m < n:                         # 讓 s2 是比較短的那個，省空間
            s1, s2, m, n = s2, s1, n, m

        dp = [False] * (n + 1)
        dp[0] = True
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # dp[0] 這一格代表「完全不用 s2」，要自己先更新
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]
            for j in range(1, n + 1):
                k = i + j - 1
                # 此刻 dp[j] 還是上一列的值（= dp[i-1][j]）
                # dp[j-1] 已經是這一列的值（= dp[i][j-1]）
                dp[j] = ((dp[j] and s1[i - 1] == s3[k]) or
                         (dp[j - 1] and s2[j - 1] == s3[k]))

        return dp[n]'''

S["p97_memo"] = '''from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @lru_cache(maxsize=None)
        def go(i: int, j: int) -> bool:
            """s1[i:] 和 s2[j:] 能不能交錯出 s3[i+j:]"""
            if i == len(s1) and j == len(s2):
                return True
            k = i + j
            if i < len(s1) and s1[i] == s3[k] and go(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[k] and go(i, j + 1):
                return True
            return False

        ans = go(0, 0)
        go.cache_clear()
        return ans'''

S["p97_brute"] = '''class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        def go(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            k = i + j
            if i < len(s1) and s1[i] == s3[k] and go(i + 1, j):
                return True
            if j < len(s2) and s2[j] == s3[k] and go(i, j + 1):
                return True
            return False

        return go(0, 0)'''


def _p97_ref(s1, s2, s3):
    """獨立參考解：直接枚舉「s3 的哪些位置來自 s1」。"""
    if len(s1) + len(s2) != len(s3):
        return False
    n = len(s3)
    for idx in itertools.combinations(range(n), len(s1)):
        pick = set(idx)
        if "".join(s3[i] for i in idx) != s1:
            continue
        if "".join(s3[i] for i in range(n) if i not in pick) == s2:
            return True
    return False


_p97 = [S.load(k) for k in ("p97_dp2d", "p97_dp1d", "p97_memo", "p97_brute")]

# 官方範例
for a, b, c, want in [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True),
    ("", "a", "a", True),
    ("a", "", "a", True),
    ("a", "b", "ab", True),
    ("a", "b", "ba", True),
    ("a", "b", "ab c", False),
    ("abc", "def", "abcdef", True),
    ("abc", "def", "adbecf", True),
    ("abc", "def", "abcdefg", False),
]:
    assert _p97_ref(a, b, c) is want, ("P97 ref", a, b, c)
    for sol in _p97:
        assert sol.isInterleave(a, b, c) is want, ("P97", a, b, c, sol)

# 隨機壓力測試：小字母表才容易撞出 True
for _ in range(3000):
    m = random.randrange(0, 6)
    n = random.randrange(0, 6)
    s1 = "".join(random.choice("ab") for _ in range(m))
    s2 = "".join(random.choice("ab") for _ in range(n))
    if random.random() < 0.6:
        # 一半機率造出「真的是交錯」的 s3
        pool = list(s1), list(s2)
        i = j = 0
        buf = []
        while i < m or j < n:
            if i < m and (j >= n or random.random() < 0.5):
                buf.append(s1[i]); i += 1
            else:
                buf.append(s2[j]); j += 1
        s3 = "".join(buf)
    else:
        L = random.randrange(0, 11)
        s3 = "".join(random.choice("ab") for _ in range(L))
    want = _p97_ref(s1, s2, s3)
    for sol in _p97:
        got = sol.isInterleave(s1, s2, s3)
        assert got is want, ("P97 random", s1, s2, s3, want, got, sol)
print("P97 solutions OK")

_P97_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">s1 = &quot;aab&quot;, s2 = &quot;dbc&quot;, s3 = &quot;aadbbc&quot; 的 DP 表。每一格問：s1 前 i 個 + s2 前 j 個，能否交錯出 s3 前 i+j 個？</text>
            <g font-size="13" text-anchor="middle">
              <text x="70" y="58" fill="var(--text-muted)">i \\ j</text>
              <text x="140" y="58" fill="var(--gold)">0</text>
              <text x="210" y="58" fill="var(--gold)">1 d</text>
              <text x="280" y="58" fill="var(--gold)">2 b</text>
              <text x="350" y="58" fill="var(--gold)">3 c</text>
              <text x="70" y="96" fill="var(--gold)">0</text>
              <text x="70" y="134" fill="var(--gold)">1 a</text>
              <text x="70" y="172" fill="var(--gold)">2 a</text>
              <text x="70" y="210" fill="var(--gold)">3 b</text>
            </g>
            <g font-size="14" text-anchor="middle">
              <rect x="112" y="78" width="56" height="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="140" y="96" fill="var(--accent)">T</text>
              <rect x="182" y="78" width="56" height="26" fill="none" stroke="var(--border)"/><text x="210" y="96" fill="var(--text-muted)">F</text>
              <rect x="252" y="78" width="56" height="26" fill="none" stroke="var(--border)"/><text x="280" y="96" fill="var(--text-muted)">F</text>
              <rect x="322" y="78" width="56" height="26" fill="none" stroke="var(--border)"/><text x="350" y="96" fill="var(--text-muted)">F</text>
              <rect x="112" y="116" width="56" height="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="140" y="134" fill="var(--accent)">T</text>
              <rect x="182" y="116" width="56" height="26" fill="none" stroke="var(--border)"/><text x="210" y="134" fill="var(--text-muted)">F</text>
              <rect x="252" y="116" width="56" height="26" fill="none" stroke="var(--border)"/><text x="280" y="134" fill="var(--text-muted)">F</text>
              <rect x="322" y="116" width="56" height="26" fill="none" stroke="var(--border)"/><text x="350" y="134" fill="var(--text-muted)">F</text>
              <rect x="112" y="154" width="56" height="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="140" y="172" fill="var(--accent)">T</text>
              <rect x="182" y="154" width="56" height="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="210" y="172" fill="var(--accent)">T</text>
              <rect x="252" y="154" width="56" height="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="280" y="172" fill="var(--accent)">T</text>
              <rect x="322" y="154" width="56" height="26" fill="none" stroke="var(--border)"/><text x="350" y="172" fill="var(--text-muted)">F</text>
              <rect x="112" y="192" width="56" height="26" fill="none" stroke="var(--border)"/><text x="140" y="210" fill="var(--text-muted)">F</text>
              <rect x="182" y="192" width="56" height="26" fill="none" stroke="var(--border)"/><text x="210" y="210" fill="var(--text-muted)">F</text>
              <rect x="252" y="192" width="56" height="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="280" y="210" fill="var(--accent)">T</text>
              <rect x="322" y="192" width="56" height="26" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="350" y="210" fill="var(--gold)">T</text>
            </g>
            <text x="404" y="212" fill="var(--gold)" font-size="12">← dp[3][3] 就是答案</text>
            <line x1="20" y1="236" x2="620" y2="236" stroke="var(--border)"/>
            <text x="20" y="262" fill="var(--accent)" font-size="12">每一格只看兩個來源：上面（這個字取自 s1）和左邊（這個字取自 s2）。</text>
            <text x="20" y="286" fill="var(--text-muted)" font-size="12">dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])</text>
            <text x="20" y="314" fill="#ff8a65" font-size="12">注意：從 (0,0) 走到 (m,n) 的每一條「只往下或往右」的 T 路徑，都是一種合法的交錯方式。</text>
            <text x="20" y="338" fill="var(--text-muted)" font-size="12">所以這題本質上是「在網格上找一條可行路徑」——和第 62/63/64 題是同一個骨架。</text>'''

emit({
 "num": 97, "slug": "interleaving-string",
 "en": [
   "Given strings <code>s1</code>, <code>s2</code>, and <code>s3</code>, find whether "
   "<code>s3</code> is formed by an <strong>interleaving</strong> of <code>s1</code> and "
   "<code>s2</code>.",
   "An <strong>interleaving</strong> of two strings <code>s</code> and <code>t</code> is a "
   "configuration where <code>s</code> and <code>t</code> are divided into "
   "<code>n</code> and <code>m</code> substrings respectively, such that:",
   ("raw", "<ul><li><code>s = s₁ + s₂ + ... + sₙ</code></li>"
           "<li><code>t = t₁ + t₂ + ... + tₘ</code></li>"
           "<li><code>|n - m| &lt;= 1</code></li>"
           "<li>The <strong>interleaving</strong> is "
           "<code>s₁ + t₁ + s₂ + t₂ + ...</code> or "
           "<code>t₁ + s₁ + t₂ + s₂ + ...</code></li></ul>"),
   "<strong>Note:</strong> <code>a + b</code> is the concatenation of strings "
   "<code>a</code> and <code>b</code>.",
 ],
 "zh": [
   "給你三個字串 <code>s1</code>、<code>s2</code>、<code>s3</code>，"
   "判斷 <code>s3</code> 是不是由 <code>s1</code> 和 <code>s2</code>"
   "<strong>交錯</strong>而成。",
   "所謂<strong>交錯</strong>，就是把 <code>s1</code> 和 <code>s2</code> 各自切成若干段，"
   "然後兩邊<strong>輪流</strong>接起來。",
   ("note", "題目的定義寫得很拗口，其實意思很簡單", [
     ("c", """題目用「切成 n 段和 m 段、|n - m| <= 1、輪流接」來定義，
看起來很複雜，但它等價於一個非常簡單的說法：

【s3 是由 s1 和 s2 的字元合併而成，
  且各自的相對順序都保持不變。】

    s1 = "abc"
    s2 = "xyz"

    "axbycz" ✔   a,b,c 順序對，x,y,z 順序對
    "abxyzc" ✔   同上（段可以很長）
    "axbzcy" ✘   s2 變成 x,z,y，順序壞了

為什麼兩種說法等價？
    「|n - m| <= 1 且輪流」只是在描述「交替出現」，
    但因為【每一段的長度可以是任意的（包含 0）】，
    所以任何「保持相對順序的合併」都能被切成這種形式。

    面試時直接用「合併且保持相對順序」來理解就好。"""),
   ]),
 ],
 "pre": [
   ("note", "第一眼會想到的兩種做法，都是錯的", [
     ("c", """【錯誤一：貪心 / 雙指標】

    i, j, k = 0, 0, 0
    while k < len(s3):
        if s1[i] == s3[k]: i += 1
        elif s2[j] == s3[k]: j += 1
        else: return False
        k += 1

    反例：s1 = "a", s2 = "ab", s3 = "aab"

        k=0: s3[0]='a'，s1[0]='a' 相同 -> 拿 s1（i=1，s1 用完了）
        k=1: s3[1]='a'，s2[0]='a' 相同 -> 拿 s2（j=1）
        k=2: s3[2]='b'，s2[1]='b' 相同 -> 拿 s2（j=2）
        結果：True（碰巧對了）

    換一個：s1 = "ab", s2 = "a", s3 = "aab"

        k=0: s3[0]='a'，s1[0]='a' -> 拿 s1（i=1）
        k=1: s3[1]='a'，s1[1]='b' 不符，s2[0]='a' 符 -> 拿 s2（j=1）
        k=2: s3[2]='b'，s1[1]='b' 符 -> 拿 s1
        True ✔

    真正的反例：s1 = "aa", s2 = "ab", s3 = "aaba"

        貪心先拿 s1 的 'a'、再拿 s1 的 'a'（i=2 用完）
        k=2: 'b'，只剩 s2 = "ab" 的 'a' -> 不符 -> False ✘

        但正解存在：s2 的 'a' + s1 的 'a' + s2 的 'b' + s1 的 'a' = "aaba" ✔

    【當兩邊的字元相同時，貪心無從選擇——這就是 DP 存在的理由。】

【錯誤二：排序後比較字元個數】

    只檢查「s1 + s2 的字元多重集合 == s3 的」是不夠的，
    因為它完全沒有檢查【順序】。

    s1 = "ab", s2 = "cd", s3 = "badc"
        字元完全一樣，但 s3 裡 b 在 a 前面 -> False

    這個檢查可以當作 O(n) 的快速否決，但不能當答案。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
  輸出：true
  說明：切法之一 ->
        s1 = "aa" + "bc" + "c"
        s2 = "dbbc" + "a"
        交錯：  "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac" ✔

範例 2
  輸入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
  輸出：false
  說明：s3 裡有連續三個 b，但 s1 只有一個 b、s2 只有兩個 b，
        而 s2 的兩個 b 之後是 c 不是 a，怎麼排都湊不出來。

範例 3
  輸入：s1 = "", s2 = "", s3 = ""
  輸出：true""",
 "constraints": [
   "0 ≤ <code>s1.length</code>, <code>s2.length</code> ≤ 100",
   "0 ≤ <code>s3.length</code> ≤ 200",
   "<code>s1</code>、<code>s2</code>、<code>s3</code> 只包含小寫英文字母",
 ],
 "mid": [
   ("note", "進階要求：你能只用 O(s2.length) 的額外空間嗎？", [
     "二維 DP 是 O(mn)，用<strong>滾動陣列</strong>可以降到 O(min(m, n))。"
     "見<strong>解法三</strong>。",
   ]),
 ],
 "idea": [
   "把它想成<strong>在網格上走路</strong>："
   "從 <code>(0, 0)</code> 出發，每一步<strong>往下</strong>（拿 <code>s1</code> 的下一個字）"
   "或<strong>往右</strong>（拿 <code>s2</code> 的下一個字），"
   "問能不能走到 <code>(m, n)</code>。",
   ("c", """關鍵觀察：【走到 (i, j) 時，已經用掉的字元數一定是 i + j】

    所以「目前要對上 s3 的哪一個字」不需要另外記，
    它就是 s3[i + j - 1]。

    這是本題最重要的一句話。
    很多人一開始會想寫 dp[i][j][k]（三維），
    但 k 完全由 i + j 決定 -> 維度直接砍掉一維。

狀態：
    dp[i][j] = s1 的前 i 個字 + s2 的前 j 個字，
               能不能交錯出 s3 的前 i+j 個字

轉移（這一格的字 s3[i+j-1] 是從哪裡來的？只有兩種可能）：

    從 s1 來：s1[i-1] == s3[i+j-1] 且 dp[i-1][j] 為真   （從上面下來）
    從 s2 來：s2[j-1] == s3[i+j-1] 且 dp[i][j-1] 為真   （從左邊過來）

    dp[i][j] = 上面那個 or 左邊那個

邊界：
    dp[0][0] = True                （什麼都不拿，湊出空字串）
    dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]   （完全不用 s1）
    dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]   （完全不用 s2）

答案：dp[m][n]

前置檢查：m + n != len(s3) -> 直接 False
    【一定要寫】，否則 dp[m][n] 的語意根本不對（長度都湊不齊）。"""),
   ("fig", _P97_FIG, "0 0 640 356"),
   "<strong>和第 62、63、64 題完全是同一個骨架</strong> —— "
   "「在網格上只能往下或往右走」。"
   "差別只在那三題算「有幾條路 / 最小成本」，這題算「有沒有路」。",
 ],
 "approaches": [
   ap("解法一", "暴力遞迴（先講，說明為什麼會爆）", [
     ("c", S["p97_brute"]),
     ("c", """時間複雜度：O(2^(m+n))

    每一步有兩個選擇（拿 s1 或拿 s2），共 m+n 步。

    m = n = 100 時是 2^200 —— 宇宙熱寂都算不完。

為什麼會這麼慢？【因為同一個 (i, j) 被重複計算無數次】：

    要走到 (2, 2)，可以是「下下右右」「下右下右」「下右右下」
    「右下下右」「右下右下」「右右下下」—— 六條不同的路徑，
    但它們到達後面對的子問題【一模一樣】。

    到達 (i, j) 的路徑數 = C(i+j, i) —— 這就是重複的倍數。

【狀態只有 (m+1)(n+1) = 10201 個，卻算了 2^200 次
  -> 這個落差就是記憶化 / DP 的全部價值。】""",),
   ], "O(2^(m+n))", "O(m+n)", "每步兩個分支", "遞迴深度"),

   ap("解法二", "二維 DP（最推薦，面試預設答案）", [
     ("c", S["p97_dp2d"]),
     ("h", "三個必須寫對的地方"),
     ("c", """1. 【長度檢查】m + n != len(s3) -> return False

   不寫的話，s1="a", s2="b", s3="ab c" 這種會讀到錯的位置，
   或是 dp[m][n] 為真但 s3 其實還有剩。
   【這是本題最常見的漏寫。】

2. 【k = i + j - 1】不是 k = i - 1 或 j - 1

   s3 的索引是「兩邊已用字元數的總和」。
   寫錯這個，範例 1 就會過不了。

3. 【第一列和第一欄要用連乘（and 前一格），不是各自獨立判斷】

   dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
                ^^^^^^^^^ 這個 and 不能少

   少了它，"ba" vs "ab" 這種「單一字元都對得上但順序錯」
   的情況會誤判成 True。"""),
     ("h", "手動走一遍範例 1 的前幾步"),
     ("c", """s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"

dp[0][0] = True

第一欄（只用 s1）：
    dp[1][0]: s1[0]='a' == s3[0]='a' ✔ -> True
    dp[2][0]: s1[1]='a' == s3[1]='a' ✔ -> True
    dp[3][0]: s1[2]='b' vs s3[2]='d' ✘ -> False
    dp[4][0], dp[5][0]: 前一格已是 False -> 都是 False

第一列（只用 s2）：
    dp[0][1]: s2[0]='d' vs s3[0]='a' ✘ -> False
    後面全部 False

dp[2][1]: k = 2, s3[2] = 'd'
    從上（s1[1]='a'）：'a' != 'd' ✘
    從左（s2[0]='d'）：'d' == 'd' ✔ 且 dp[2][0] = True ✔
    -> True

一路推下去，dp[5][5] = True ✔"""),
     "<strong>時間 O(mn) = 10000 次，空間 O(mn)。</strong>"
     "對 <code>m, n ≤ 100</code> 綽綽有餘。",
   ], "O(m × n)", "O(m × n)", "每格 O(1)", "二維表", optimal=True),

   ap("解法三", "滾動陣列（滿足進階的 O(min(m,n)) 空間）", [
     ("c", S["p97_dp1d"]),
     ("h", "為什麼可以壓成一維？"),
     ("c", """dp[i][j] 只依賴 dp[i-1][j]（上面）和 dp[i][j-1]（左邊）。

用一維陣列、由左往右更新時：

    dp[j]     還沒被這一輪改到  -> 它還是 dp[i-1][j]  （上面）✔
    dp[j-1]   這一輪剛剛改過     -> 它已是 dp[i][j-1]  （左邊）✔

    兩個需要的值【剛好都在手邊】，所以不用開二維表。

    （對照第 64 題、第 72 題 —— 同一個滾動技巧。）""",),
     ("h", "<code>dp[0]</code> 這一格最容易忘"),
     ("c", """每進入新的一列 i，dp[0] 代表「完全不用 s2，只用 s1 的前 i 個字」。

    它【也要更新】：
        dp[0] = dp[0] and s1[i-1] == s3[i-1]

    忘了這一行，dp[0] 會一直是上一列的值，
    整條第一欄的資訊就錯了。

    【這是滾動陣列版最經典的 bug。】

    如果你在紙上算，會發現 s1="ab", s2="", s3="ab"
    這種「s2 是空字串」的案例馬上就掛。"""),
     ("h", "為什麼要 <code>if m &lt; n: swap</code>？"),
     "進階要求是 <strong>O(s2.length)</strong>，但把短的那個當成 <code>s2</code> "
     "可以做到 <strong>O(min(m, n))</strong>，更好。",
     "<strong>交換是安全的</strong> —— 「交錯」這個關係對 <code>s1</code>、<code>s2</code> "
     "是<strong>對稱的</strong>（誰在前誰在後不影響答案）。",
   ], "O(m × n)", "O(min(m, n))", "格數不變", "只留一列"),

   ap("解法四", "記憶化遞迴（自頂向下，最好想）", [
     ("c", S["p97_memo"]),
     "<strong>和解法一的差別只有一行 <code>@lru_cache</code></strong> —— "
     "但複雜度從 <code>O(2^(m+n))</code> 掉到 <code>O(mn)</code>。",
     ("c", """自頂向下 vs 自底向上，怎麼選？

  記憶化遞迴（自頂向下）
    ✔ 從暴力解改過來只要一行，最不容易寫錯
    ✔ 只會算「真正需要的狀態」
    ✘ 遞迴深度 m + n = 200（本題安全；更大就要小心 RecursionError）
    ✘ 函式呼叫的常數開銷較大

  迭代 DP（自底向上）
    ✔ 沒有遞迴深度問題，常數小
    ✔ 可以做滾動陣列優化（遞迴版做不到）
    ✘ 邊界（第一列、第一欄）要自己想清楚

【面試建議：先口頭說暴力解 -> 指出重複子問題 -> 加記憶化
  -> 再改寫成迭代 DP -> 最後提滾動陣列。
  這四步是 DP 題的標準敘事，比直接寫出最終解更能展示思路。】"""),
     "<strong><code>cache_clear()</code></strong>：LeetCode 的 "
     "<code>Solution</code> 物件在多筆測資間可能被重用，"
     "而 <code>lru_cache</code> 掛在內層函式上其實每次呼叫都是新的，"
     "這行主要是<strong>釋放記憶體</strong>的好習慣。",
   ], "O(m × n)", "O(m × n)", "每個狀態算一次", "快取 + 遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "好寫嗎", "備註"],
   [["一、暴力遞迴", "O(2^(m+n))", "O(m+n)", "★★★", "會 TLE，只用來講動機"],
    ["二、二維 DP", "O(mn)", "O(mn)", "★★☆", "面試預設答案"],
    ["三、滾動陣列", "O(mn)", "O(min(m,n))", "★☆☆", "滿足進階要求"],
    ["四、記憶化遞迴", "O(mn)", "O(mn)", "★★★", "從暴力解最快改到"]]),
 "post": [
   ("note", "一個 O(1) 空間的常見誤解", [
     "有人會說「用兩個指標加回溯就能 O(1) 空間」——"
     "<strong>那只是把 DP 表換成遞迴堆疊，而且沒有記憶化就會指數爆炸。</strong>",
     "<strong>真正的下界</strong>：這題的狀態空間是 <code>Θ(mn)</code>，"
     "而每個狀態都可能被需要，所以<strong>要 O(mn) 時間是跑不掉的</strong>；"
     "空間則可以靠滾動壓到 <code>O(min(m, n))</code>，"
     "但<strong>壓到 O(1) 沒有已知做法</strong>。",
   ]),
 ],
 "edges": [
   "<strong><code>s1 = \"\", s2 = \"\", s3 = \"\"</code></strong> → <code>True</code>。"
   "<code>dp[0][0] = True</code> 直接回答。",
   "<strong><code>s1 = \"\", s2 = \"a\", s3 = \"a\"</code></strong> → <code>True</code>。"
   "考驗第一列的邊界。",
   "<strong><code>s1 = \"a\", s2 = \"\", s3 = \"a\"</code></strong> → <code>True</code>。"
   "考驗第一欄的邊界（滾動陣列版的 <code>dp[0]</code> 沒更新就會死在這）。",
   "<strong>長度對不上</strong>（<code>m + n != len(s3)</code>）→ 必須先擋掉，"
   "<strong>這是最常見的漏寫</strong>。",
   "<strong><code>s1 = \"a\", s2 = \"b\", s3 = \"ba\"</code></strong> → <code>True</code>。"
   "誰先誰後都可以。",
   "<strong><code>s1 = \"aa\", s2 = \"ab\", s3 = \"aaba\"</code></strong> → <code>True</code>，"
   "但<strong>貪心雙指標會答 False</strong>。這是打臉貪心的標準反例。",
   "<strong><code>k</code> 寫成 <code>i - 1</code> 或 <code>j - 1</code></strong>："
   "範例 1 就會錯。",
   "<strong>第一列/第一欄忘了 <code>and</code> 前一格</strong>："
   "順序錯的字串會被誤判成 True。",
 ],
 "follow": [
   ("h", "追問一：如果要輸出「是怎麼交錯的」呢？"),
   "<strong>從 <code>dp[m][n]</code> 往回走</strong>："
   "在 <code>(i, j)</code> 看是「上面」還是「左邊」讓它變成 <code>True</code>，"
   "往那個方向退，同時記下這個字來自 <code>s1</code> 還是 <code>s2</code>，"
   "最後把記錄反轉。",
   "<strong>需要保留完整的二維表</strong>（滾動陣列版做不到回溯）—— "
   "<strong>這是「壓空間」的代價</strong>，第 72 題（編輯距離）要輸出操作序列時也一樣。",
   ("h", "追問二：如果是三個字串交錯成一個呢？"),
   "<strong>狀態變成 <code>dp[i][j][k]</code></strong>，"
   "<code>s4</code> 的位置是 <code>i + j + k - 1</code>，"
   "每格看三個來源。時間 <code>O(n³)</code>。",
   "<strong>推廣到 <code>t</code> 個字串就是 <code>O(n^t)</code></strong> —— "
   "指數爆炸在字串數量上。",
   "<strong>事實上「t 個字串的交錯判定」在 t 不固定時是 NP-complete 的</strong>（Mansfield, 1983），"
   "所以別期待有多項式的通解。",
   ("h", "追問三：如果問「有幾種交錯方式」呢？"),
   "<strong>把 <code>or</code> 換成 <code>+</code>、<code>True/False</code> 換成計數</strong>：",
   ("c", """dp[i][j] = (dp[i-1][j] if s1[i-1] == s3[i+j-1] else 0) \\
         + (dp[i][j-1] if s2[j-1] == s3[i+j-1] else 0)

dp[0][0] = 1

【布林 DP -> 計數 DP 的萬用轉換：or 變 +，and 變 ×。】

注意：如果 s1 和 s2 有相同的字元，同一個 s3
可能對應到多條不同的路徑 —— 這題數的是「路徑數」，
不是「不同的 s3 數」。"""),
   "<strong>當 <code>s1</code>、<code>s2</code> 的字元完全不重複時，"
   "答案就是 <code>C(m+n, m)</code></strong> —— 和第 62 題（不同路徑）一模一樣。",
   ("h", "追問四：為什麼這題不能用 KMP 之類的字串演算法？"),
   "因為<strong>它不是「找子字串」而是「找一個二維的分割」</strong>。"
   "KMP / Z-function 解決的是「一維的模式匹配」，"
   "而這裡每個位置都有「來自哪一邊」的二元選擇，"
   "<strong>本質上就是二維的狀態空間</strong>。",
 ],
 "related": [
   "<strong>第 62 題 Unique Paths</strong> —— 同一個網格骨架（數路徑）",
   "<strong>第 63 題 Unique Paths II</strong> —— 網格 + 障礙",
   "<strong>第 72 題 Edit Distance</strong> —— 另一個經典的雙字串二維 DP",
   "<strong>第 1143 題 Longest Common Subsequence</strong> —— 雙字串 DP 的基本款",
   "<strong>第 44 題 Wildcard Matching</strong> —— 雙字串 DP + 通配符",
 ],
 "check": [
   "為什麼 <code>s3</code> 的索引可以直接用 <code>i + j - 1</code>，不需要第三個維度？",
   "貪心雙指標為什麼會錯？請說出一個反例。",
   "滾動陣列版裡，<code>dp[0]</code> 為什麼每一列都要更新？不更新會在哪個測資掛掉？",
   "如果改問「有幾種交錯方式」，轉移式要怎麼改？",
 ],
})
print("P97 written")

# ==================== 98. Validate Binary Search Tree ====================
S["p98_bounds"] = '''class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def go(node, lo, hi):
            """node 這棵子樹的所有值，是不是都嚴格落在 (lo, hi) 之間"""
            if not node:
                return True                  # 空樹是合法的 BST
            if not (lo < node.val < hi):
                return False
            # 往左：上界收緊成 node.val；往右：下界收緊成 node.val
            return (go(node.left, lo, node.val) and
                    go(node.right, node.val, hi))

        return go(root, float("-inf"), float("inf"))'''

S["p98_inorder_rec"] = '''class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None                     # 中序走訪的前一個值

        def go(node):
            if not node:
                return True
            if not go(node.left):            # 先走左子樹
                return False
            if self.prev is not None and self.prev >= node.val:
                return False                 # 不是嚴格遞增 -> 不合法
            self.prev = node.val
            return go(node.right)            # 再走右子樹

        return go(root)'''

S["p98_inorder_iter"] = '''class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack, prev, node = [], None, root

        while stack or node:
            while node:                      # 一路往左走到底
                stack.append(node)
                node = node.left
            node = stack.pop()               # 這裡就是「中序輸出」的時機
            if prev is not None and prev >= node.val:
                return False                 # 提早結束，不用走完整棵樹
            prev = node.val
            node = node.right                # 轉向右子樹

        return True'''

S["p98_morris"] = '''class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev, node, ok = None, root, True

        while node:
            if not node.left:
                if prev is not None and prev >= node.val:
                    ok = False               # 【不能直接 return】，要先把樹修回來
                prev = node.val
                node = node.right
            else:
                # 找左子樹的最右節點（中序的前驅）
                pre = node.left
                while pre.right and pre.right is not node:
                    pre = pre.right

                if not pre.right:            # 第一次來：架一條回家的線
                    pre.right = node
                    node = node.left
                else:                        # 第二次來：拆線，並輸出自己
                    pre.right = None
                    if prev is not None and prev >= node.val:
                        ok = False
                    prev = node.val
                    node = node.right

        return ok'''

S["p98_wrong"] = '''class Solution:
    # 【這是錯的，不要抄】
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and root.left.val >= root.val:
            return False
        if root.right and root.right.val <= root.val:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)'''


def _p98_ref(root):
    """獨立參考解：對每個節點，檢查整個左子樹都比它小、整個右子樹都比它大。"""
    def vals(node):
        return [] if not node else vals(node.left) + [node.val] + vals(node.right)

    def ok(node):
        if not node:
            return True
        if any(v >= node.val for v in vals(node.left)):
            return False
        if any(v <= node.val for v in vals(node.right)):
            return False
        return ok(node.left) and ok(node.right)

    return ok(root)


def _build(spec):
    """用 [根, 左, 右] 的巢狀 list 蓋一棵樹；None 代表空。"""
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _build(l), _build(r))


def _rand_tree(n, lo, hi):
    """隨機形狀、隨機值的二元樹。"""
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi),
                    _rand_tree(left, lo, hi),
                    _rand_tree(n - 1 - left, lo, hi))


def _rand_bst(vals):
    """用排序好的值蓋一棵隨機形狀的合法 BST。"""
    if not vals:
        return None
    k = random.randrange(len(vals))
    return TreeNode(vals[k], _rand_bst(vals[:k]), _rand_bst(vals[k + 1:]))


_p98 = [S.load(k) for k in
        ("p98_bounds", "p98_inorder_rec", "p98_inorder_iter", "p98_morris")]
_p98_bad = S.load("p98_wrong")


def _shape98(node):
    return "#" if not node else "(%s %s %s)" % (_shape98(node.left), node.val,
                                                _shape98(node.right))


# 官方範例與經典反例
_CASES98 = [
    ([2, [1, None, None], [3, None, None]], True),
    ([5, [1, None, None], [4, [3, None, None], [6, None, None]]], False),
    ([1, None, None], True),
    ([5, [4, None, None], [6, [3, None, None], [7, None, None]]], False),
    ([2, [2, None, None], None], False),
    ([2, None, [2, None, None]], False),
    ([10, [5, None, [12, None, None]], [15, None, None]], False),
]
for spec, want in _CASES98:
    t = _build(spec)
    assert _p98_ref(t) is want, ("P98 ref", spec)
    for sol in _p98:
        assert sol.isValidBST(_build(spec)) is want, ("P98", spec, sol)

# 錯誤寫法確實在「隔代違規」的案例上答錯
_bad_case = _build([10, [5, None, None], [15, [6, None, None], [20, None, None]]])
assert _p98_bad.isValidBST(_bad_case) is True and _p98_ref(_bad_case) is False, "P98 wrong-demo"

# 隨機壓力測試（亂樹）
for _ in range(4000):
    n = random.randrange(0, 9)
    t = _rand_tree(n, -6, 6)
    want = _p98_ref(t)
    before = _shape98(t)
    for sol in _p98:
        got = sol.isValidBST(t)
        assert got is want, ("P98 random", before, want, got, sol)
        # Morris 版必須把樹修回原狀
        assert _shape98(t) == before, ("P98 tree mutated", before, _shape98(t), sol)

# 隨機壓力測試（保證合法的 BST，確保不會誤判成 False）
for _ in range(1500):
    n = random.randrange(0, 10)
    vals = sorted(random.sample(range(-50, 50), n))
    t = _rand_bst(vals)
    assert _p98_ref(t) is True
    for sol in _p98:
        assert sol.isValidBST(t) is True, ("P98 valid-bst", vals, sol)

# 極端值：節點值可以是 2^31 - 1 或 -2^31
_edge = _build([2147483647, None, None])
for sol in _p98:
    assert sol.isValidBST(_edge) is True, ("P98 INT_MAX", sol)
_edge2 = _build([-2147483648, None, None])
for sol in _p98:
    assert sol.isValidBST(_edge2) is True, ("P98 INT_MIN", sol)
print("P98 solutions OK")

_P98_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">最經典的錯誤：只比較「父子」是不夠的，必須比較「整個子樹」。</text>
            <text x="20" y="48" fill="#ff8a65" font-size="13">反例：root = [10, 5, 15, null, null, 6, 20]</text>
            <g font-size="14" text-anchor="middle">
              <circle cx="200" cy="96" r="21" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="200" y="101" fill="var(--gold)">10</text>
              <circle cx="120" cy="164" r="21" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="120" y="169" fill="var(--accent)">5</text>
              <circle cx="280" cy="164" r="21" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="280" y="169" fill="var(--accent)">15</text>
              <circle cx="230" cy="232" r="21" fill="none" stroke="#ff8a65" stroke-width="3"/><text x="230" y="237" fill="#ff8a65">6</text>
              <circle cx="340" cy="232" r="21" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="340" y="237" fill="var(--accent)">20</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="185" y1="111" x2="135" y2="149"/>
              <line x1="215" y1="111" x2="265" y2="149"/>
              <line x1="266" y1="179" x2="244" y2="217"/>
              <line x1="294" y1="179" x2="326" y2="217"/>
            </g>
            <text x="376" y="100" fill="var(--text-muted)" font-size="12">10 &lt; 15 ✔（父子合法）</text>
            <text x="376" y="124" fill="var(--text-muted)" font-size="12">6 &lt; 15 ✔（父子合法）</text>
            <text x="376" y="156" fill="#ff8a65" font-size="12">但 6 在 10 的右子樹裡，</text>
            <text x="376" y="180" fill="#ff8a65" font-size="12">卻 6 &lt; 10 ✘ —— 隔代違規！</text>
            <line x1="20" y1="270" x2="620" y2="270" stroke="var(--border)"/>
            <text x="20" y="296" fill="var(--accent)" font-size="12">解法一（上下界）怎麼抓到它：走到 15 時區間收成 (10, +∞)，再往左走到 6 時區間是 (10, 15)。</text>
            <text x="20" y="320" fill="var(--accent)" font-size="12">6 不在 (10, 15) 裡 → False ✔　【上界會沿著左邊的路徑一路傳下去。】</text>
            <text x="20" y="348" fill="var(--gold)" font-size="12">解法二（中序）怎麼抓到它：中序輸出 5, 10, 6, 15, 20 —— 10 之後接 6，不是遞增 → False ✔</text>
            <text x="20" y="376" fill="var(--text-muted)" font-size="12">記住這句話：「BST ⟺ 中序走訪嚴格遞增」。這是 BST 所有題目的共同鑰匙。</text>'''

emit({
 "num": 98, "slug": "validate-binary-search-tree",
 "en": [
   "Given the <code>root</code> of a binary tree, <em>determine if it is a valid binary "
   "search tree (BST)</em>.",
   "A <strong>valid BST</strong> is defined as follows:",
   ("raw", "<ul><li>The left subtree of a node contains only nodes with keys "
           "<strong>less than</strong> the node's key.</li>"
           "<li>The right subtree of a node contains only nodes with keys "
           "<strong>greater than</strong> the node's key.</li>"
           "<li>Both the left and right subtrees must also be binary search trees.</li></ul>"),
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，判斷它是不是一棵合法的"
   "<strong>二元搜尋樹（BST）</strong>。",
   "<strong>合法的 BST</strong> 定義如下：",
   ("ul", [
     "一個節點的<strong>左子樹</strong>裡，<strong>所有</strong>節點的值都"
     "<strong>小於</strong>它。",
     "一個節點的<strong>右子樹</strong>裡，<strong>所有</strong>節點的值都"
     "<strong>大於</strong>它。",
     "左右子樹<strong>本身也必須</strong>是合法的 BST。",
   ]),
 ],
 "pre": [
   ("note", "定義裡藏了兩個關鍵字，錯過就會寫出錯的解", [
     ("c", """【關鍵字一：「所有」】

    不是「左孩子比我小」，而是【整個左子樹都比我小】。

    這是本題唯一的難點，也是 90% 的人第一次寫會錯的地方。

【關鍵字二：「小於 / 大於」是嚴格的】

    不能有相等的值。

    所以 [2, 2] 和 [2, null, 2] 都是【不合法】的。

    （注意：有些教科書允許重複值放在某一側，
      但 LeetCode 這題採用「嚴格」的定義。）"""),
   ]),
   ("note", "先看看錯在哪裡：最常見的錯誤寫法", [
     ("c", S["p98_wrong"]),
     ("c", """這段程式碼看起來完全合理：
    「檢查左孩子比我小、右孩子比我大，然後遞迴檢查左右子樹。」

但它只檢查了【父子】關係，沒有檢查【祖孫】關係。

反例：

            10
           /  \\
          5    15
              /  \\
             6    20

    10 的左孩子 5  < 10 ✔
    10 的右孩子 15 > 10 ✔
    15 的左孩子 6  < 15 ✔
    15 的右孩子 20 > 15 ✔

    每一組父子都合法 -> 錯誤解法回答 True

    但 6 在【10 的右子樹】裡，卻 6 < 10 ✘
    -> 正確答案是 False

【限制必須沿著路徑一路往下傳遞，而不是只看一層。】
這就是解法一「上下界」存在的理由。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [2,1,3]

          2
         / \\
        1   3

  輸出：true

範例 2
  輸入：root = [5,1,4,null,null,3,6]

          5
         / \\
        1   4
           / \\
          3   6

  輸出：false
  說明：根是 5，但右子樹裡有 4 和 3，都比 5 小。""",
 "constraints": [
   "樹的節點數在 <code>[1, 10⁴]</code> 之間",
   "−2³¹ ≤ <code>Node.val</code> ≤ 2³¹ − 1",
 ],
 "mid": [
   ("note", "注意這個限制：節點值可以剛好是 2³¹ − 1 或 −2³¹", [
     ("c", """這是題目故意設的陷阱。

如果你在 Java / C++ 裡寫：

    boolean go(TreeNode node, int lo, int hi)   // 用 int 當邊界

    然後一開始傳 go(root, INT_MIN, INT_MAX)，
    那麼單一節點 [INT_MIN] 會被判成 False（因為要求嚴格大於 lo）✘

解法：
    (a) 用 long（Java）/ long long（C++），邊界設成 LONG_MIN / LONG_MAX
    (b) 用 null / Integer 物件表示「沒有限制」，並在比較前先判空
    (c) 改用【中序走訪】—— 它根本不需要邊界值，自然免疫

Python 有 float('-inf') / float('inf')，而且整數不會溢位，
所以沒有這個問題 ——
【但面試時要主動講出來，這是很加分的細節。】"""),
   ]),
 ],
 "idea": [
   ("fig", _P98_FIG, "0 0 640 394"),
   ("c", """兩條主線，兩種都要會：

【思路 A：由上往下傳「合法區間」】

    每個節點都帶著一個開區間 (lo, hi)，意思是
    「你的值必須嚴格落在這個範圍裡」。

    根節點：       (-∞, +∞)
    往左走：       上界收緊成父節點的值 -> (lo, node.val)
    往右走：       下界收緊成父節點的值 -> (node.val, hi)

    這樣「祖先的限制」就自動沿著路徑傳下去了 ✔

【思路 B：BST ⟺ 中序走訪嚴格遞增】

    這是 BST 最重要的一個等價命題。

    因為中序是「左 -> 根 -> 右」，而 BST 保證
    「左子樹全部 < 根 < 右子樹全部」，
    所以輸出必然是由小到大。

    反過來也成立：中序嚴格遞增的二元樹，一定是 BST。

    所以只要中序走一遍，檢查每個值都比前一個大即可。
    【連陣列都不用存，記住前一個值就好。】

兩條路都是 O(n) 時間，選哪個都對；
面試時能同時講出來最好。"""),
 ],
 "approaches": [
   ap("解法一", "上下界遞迴（最直觀、最好講）", [
     ("c", S["p98_bounds"]),
     ("h", "為什麼這樣就抓得到「隔代違規」？"),
     ("c", """回到那個反例：

            10
           /  \\
          5    15
              /  \\
             6    20

    go(10, -∞, +∞)    -∞ < 10 < +∞ ✔
      go(5,  -∞, 10)  -∞ < 5  < 10 ✔
      go(15, 10, +∞)  10 < 15 < +∞ ✔
        go(6,  10, 15)  【10 < 6 ？ 不成立】 ✘ -> False

    關鍵在【往右走時，下界 10 被保留下來了】，
    然後【再往左走時，那個 10 仍然在】。

    「往左走只改上界、往右走只改下界」——
    另一邊的限制原封不動地往下傳，
    這正是「整個子樹」這個要求的程式化表達。"""),
     ("h", "為什麼用 <code>float('-inf')</code> / <code>float('inf')</code>？"),
     "這樣就<strong>不用為根節點寫特例</strong>，"
     "而且和「節點值可能是 <code>±2³¹</code>」的邊界完全無關。",
     "<strong>在 Java / C++ 裡</strong>請用 <code>long</code>，"
     "或用 <code>null</code> 表示「沒有限制」。",
     ("h", "一個更嚴謹的寫法（值可能是任意大整數時）"),
     ("c", """def go(node, lo, hi):        # lo, hi 用 None 表示「沒有限制」
    if not node:
        return True
    if lo is not None and node.val <= lo:
        return False
    if hi is not None and node.val >= hi:
        return False
    return go(node.left, lo, node.val) and go(node.right, node.val, hi)

這個版本對任何型別的值都成立（只要能比大小），
不依賴「有一個比所有值都大/小的哨兵」。

【面試時如果面試官追問「如果值是任意精度的呢」，
  就端出這個版本。】"""),
     "<strong>空間 O(h)</strong>（h 是樹高）。"
     "<strong>最壞情況（退化成一條鏈）是 O(n) = 10⁴</strong> —— "
     "Python 預設遞迴上限是 1000，"
     "<strong>極端測資下真的會 <code>RecursionError</code></strong>，"
     "這時要改用解法三。",
   ], "O(n)", "O(h)", "每個節點看一次", "遞迴堆疊", optimal=True),

   ap("解法二", "中序走訪（遞迴版）", [
     ("c", S["p98_inorder_rec"]),
     ("h", "為什麼只要記「前一個值」就夠？"),
     ("c", """「嚴格遞增」這個性質是【只看相鄰兩項】就能驗證的：

    a1 < a2 < a3 < ... < an
    ⟺ 對每個 i，a_i < a_{i+1}

所以不需要把中序結果存成陣列（那要 O(n) 額外空間），
只要一個變數記住「剛剛輸出的值」就好。

【而且可以提早結束】——
一旦發現逆序就立刻回 False，不必走完整棵樹。

這在「大樹但錯誤出現得早」的測資上快非常多。""",),
     ("h", "為什麼用 <code>self.prev</code> 而不是區域變數？"),
     ("c", """Python 的閉包不能直接「寫入」外層函式的區域變數
（讀可以，寫會被當成新的區域變數）。

三種解法：
    (a) self.prev = None          <- 本文用這個，最直白
    (b) nonlocal prev             <- Python 3 的關鍵字
    (c) prev = [None]             <- 用 list 當可變盒子

    def isValidBST(self, root):
        prev = None
        def go(node):
            nonlocal prev         # (b) 的寫法
            ...

三種都對，挑一個順手的。
【面試時寫 nonlocal 最乾淨。】"""),
     ("h", "<code>self.prev is not None</code> 為什麼不能寫成 <code>self.prev</code>？"),
     "<strong>因為節點值可能是 <code>0</code></strong>，"
     "而 <code>0</code> 在 Python 裡是 falsy。"
     "<strong>寫成 <code>if self.prev and ...</code> 就會漏掉「前一個值是 0」的檢查</strong>，"
     "例如 <code>[0, null, -1]</code> 會被誤判成 True。",
     "<strong>這是「用真假值代替 <code>is not None</code>」的經典 bug</strong>，"
     "在有 <code>0</code>、空字串、空 list 的地方都要小心。",
   ], "O(n)", "O(h)", "每個節點看一次", "遞迴堆疊"),

   ap("解法三", "中序走訪（迭代版，避開遞迴深度限制）", [
     ("c", S["p98_inorder_iter"]),
     ("h", "和第 94 題一模一樣的骨架"),
     ("c", """while stack or node:
    while node:            # 一路往左沉到底，沿路把節點壓進 stack
        stack.append(node)
        node = node.left
    node = stack.pop()     # 【彈出的瞬間就是中序輸出的時機】
    ...檢查...
    node = node.right      # 轉向右子樹，回到外層迴圈

這個 pattern 請背下來 ——
第 94（中序走訪）、98（本題）、173（BST 迭代器）、
230（BST 第 k 小）用的都是它。

【只要在「pop 之後」插入你要做的事，就能解一整類 BST 題目。】""",),
     "<strong>沒有遞迴深度限制</strong> —— "
     "節點數 10⁴ 且樹退化成鏈時，這是唯一安全的一般解法。",
     "<strong>一樣可以提早結束</strong>（發現逆序就 <code>return False</code>），"
     "而且<strong>不用擔心「還有沒拆的線」</strong>（解法四就要擔心）。",
   ], "O(n)", "O(h)", "每個節點進出堆疊一次", "顯式堆疊"),

   ap("解法四", "Morris 中序走訪（O(1) 額外空間）", [
     ("c", S["p98_morris"]),
     ("h", "核心技巧：借用空的 <code>right</code> 指標當「回家的線」"),
     ("c", """一棵有 n 個節點的二元樹，有 n+1 個空指標。
Morris 的想法就是【把它們臨時借來當作返回路徑】。

對每個有左子樹的節點 node：

    1. 找到左子樹的最右節點 pre（= node 在中序裡的前驅）
    2. 如果 pre.right 是空的：
           架線 pre.right = node，然後往左走
           （之後走完左子樹，自然會沿著這條線回到 node）
    3. 如果 pre.right 已經指向 node：
           表示左子樹走完了 -> 拆線、輸出 node、往右走

    【每條線最多架一次、拆一次 -> 總時間仍是 O(n)。】

    （準確地說是 O(n)，因為「找前驅」的總成本
      等於每條右邊緣被走過常數次。）"""),
     ("h", "本題用 Morris 的一個大坑"),
     ("c", """【發現不合法時，不能直接 return False！】

    因為此時樹上還掛著沒拆掉的線 ——
    直接返回會把【原本的樹結構破壞掉】，
    後續任何操作（甚至只是印出來）都會無窮迴圈。

    所以要：
        ok = False        # 只做記號
        ...繼續把走訪跑完，讓所有線都被拆掉...
        return ok

    代價：【失去了提早結束的能力】。

    這也是為什麼實務上 Morris 不一定比解法三快 ——
    它省的是空間，不是時間。""",),
     "<strong>什麼時候真的需要 Morris？</strong>"
     "當面試官明確問「能不能 O(1) 空間」，"
     "或是在<strong>記憶體極度受限的嵌入式環境</strong>。"
     "<strong>一般情況請寫解法一或解法三</strong> —— 更短、更不容易錯、還能提早結束。",
     "<strong>另一個限制</strong>：Morris 會<strong>暫時修改樹</strong>，"
     "所以在<strong>多執行緒環境</strong>或<strong>樹是唯讀的</strong>情況下不能用。",
   ], "O(n)", "O(1)", "每條線架一次拆一次", "只用幾個指標"),
 ],
 "compare": (["解法", "時間", "空間", "能提早結束", "備註"],
   [["一、上下界遞迴", "O(n)", "O(h)", "✔", "最直觀，面試預設"],
    ["二、中序遞迴", "O(n)", "O(h)", "✔", "展示「BST ⟺ 中序遞增」"],
    ["三、中序迭代", "O(n)", "O(h)", "✔", "沒有遞迴深度問題"],
    ["四、Morris", "O(n)", "O(1)", "✘ 要拆線", "唯一的 O(1) 空間解"]]),
 "post": [
   ("note", "把「中序遞增」背下來，你就解開了一整類題目", [
     ("c", """BST ⟺ 中序走訪嚴格遞增

這一句話直接或間接解決了：

    98   Validate BST          -> 檢查中序是否遞增（本題）
    99   Recover BST           -> 中序裡找出逆序對（下一題）
    230  Kth Smallest in BST   -> 中序的第 k 個
    173  BST Iterator          -> 把中序走訪拆成 next() 逐步執行
    501  Find Mode in BST      -> 中序裡相同的值一定連續
    530  Minimum Absolute Diff -> 最小差一定發生在中序的相鄰兩項
    1038 Greater Sum Tree      -> 反向中序（右 -> 根 -> 左）累加

    【看到 BST，先問自己：「中序走一遍能不能解？」
      一半以上的 BST 題答案是「可以」。】"""),
   ]),
 ],
 "edges": [
   "<strong>單一節點</strong> <code>[1]</code> → <code>True</code>。",
   "<strong><code>[5,1,4,null,null,3,6]</code></strong> → <code>False</code>（官方範例 2）。",
   "<strong><code>[10,5,15,null,null,6,20]</code></strong> → <code>False</code>。"
   "<strong>這是打臉「只比父子」的標準反例</strong>。",
   "<strong><code>[2,2]</code> 和 <code>[2,null,2]</code></strong> → 都是 <code>False</code>。"
   "<strong>必須是嚴格不等</strong>，寫成 <code>&lt;=</code> 就錯。",
   "<strong><code>[2147483647]</code></strong> → <code>True</code>。"
   "用 <code>int</code> 當邊界的語言會在這裡掛掉。",
   "<strong><code>[-2147483648]</code></strong> → <code>True</code>。同上。",
   "<strong><code>[0,null,-1]</code></strong> → <code>False</code>。"
   "<strong><code>if prev</code> 寫法（而非 <code>if prev is not None</code>）"
   "會在這裡誤判成 True</strong>。",
   "<strong>退化成一條鏈</strong>（10⁴ 個節點）→ "
   "遞迴版可能 <code>RecursionError</code>，要用解法三或四。",
   "<strong>Morris 版提早 return</strong> → 樹被破壞，後續操作可能無窮迴圈。",
 ],
 "follow": [
   ("h", "追問一：如果允許重複值呢？"),
   "<strong>先問清楚重複值放哪一側</strong>（這是設計決定，沒有標準答案）。",
   ("ul", [
     "<strong>重複值放左邊</strong>：條件變成 <code>左子樹 ≤ 根 &lt; 右子樹</code>，"
     "中序是<strong>非遞減</strong>（<code>prev &gt; node.val</code> 才算錯）。",
     "<strong>重複值放右邊</strong>：條件變成 <code>左子樹 &lt; 根 ≤ 右子樹</code>。",
     "<strong>在節點上存計數</strong>（<code>count</code> 欄位）：樹裡仍然沒有重複的鍵，"
     "<strong>實務上最常見的做法</strong>（C++ 的 <code>std::multiset</code> 就是這樣）。",
   ]),
   ("h", "追問二：如果要回報「哪個節點違規」呢？"),
   "<strong>上下界版</strong>：在 <code>return False</code> 的地方把 "
   "<code>node</code> 記下來，就是第一個（前序順序）違規的節點。",
   "<strong>中序版</strong>：記下 <code>prev</code> 和 <code>node</code>，"
   "就是第一個逆序對 —— <strong>這正是第 99 題的起手式</strong>。",
   ("h", "追問三：如果樹非常大，放不進記憶體呢？"),
   "<strong>中序走訪是「串流友善」的</strong>：它只需要 <code>O(h)</code> 的堆疊，"
   "而且<strong>一次只碰一個節點</strong>。",
   "所以可以<strong>邊從磁碟讀邊驗證</strong>，"
   "只要維護「上一個值」和一個 <code>O(h)</code> 的路徑堆疊。"
   "<strong>上下界版也可以，但它需要同時持有父節點的資訊。</strong>",
   ("h", "追問四：怎麼驗證一棵樹是「平衡的」BST？"),
   "<strong>兩件事要分開檢查</strong>："
   "（1）BST 性質（本題）；（2）平衡性（第 110 題：每個節點的左右高度差 ≤ 1）。",
   "<strong>可以合併成一趟後序走訪</strong>："
   "每個節點同時回傳 <code>(是否合法, 最小值, 最大值, 高度)</code>，"
   "父節點用子節點的結果 <code>O(1)</code> 合成。"
   "<strong>這種「後序回傳一包資訊」的手法是樹題的另一個萬用範式</strong>。",
   ("h", "追問五：為什麼「中序遞增 ⟹ 是 BST」也成立？"),
   ("c", """（⟸ 方向）BST -> 中序遞增，前面說過了。

（⟹ 方向）中序遞增 -> BST，證明如下：

    對任一節點 x，考慮它的左子樹 L 和右子樹 R。

    中序走訪的順序是：  [L 的全部] x [R 的全部]

    既然整個序列嚴格遞增，
    那麼 L 裡的每個值都排在 x 前面 -> 都 < x ✔
    R 裡的每個值都排在 x 後面 -> 都 > x ✔

    這對每個節點都成立 -> 符合 BST 的定義 ✔

【所以「中序嚴格遞增」和「是 BST」是完全等價的，
  不只是必要條件。】

    這個等價性是解法二、三、四全部成立的基礎，
    也值得在面試時主動說出來。"""),
 ],
 "related": [
   "<strong>第 94 題 Binary Tree Inorder Traversal</strong> —— 中序走訪的三種寫法",
   "<strong>第 99 題 Recover Binary Search Tree</strong> —— 中序裡找逆序對",
   "<strong>第 230 題 Kth Smallest Element in a BST</strong> —— 中序的第 k 個",
   "<strong>第 173 題 Binary Search Tree Iterator</strong> —— 把中序拆成迭代器",
   "<strong>第 110 題 Balanced Binary Tree</strong> —— 後序回傳一包資訊",
 ],
 "check": [
   "為什麼「只檢查左孩子 &lt; 根 &lt; 右孩子」是錯的？請畫出一個反例。",
   "上下界遞迴往左走和往右走時，各自改的是哪一個邊界？另一個為什麼不動？",
   "「BST ⟺ 中序走訪嚴格遞增」的兩個方向各要怎麼證？",
   "中序版為什麼要寫 <code>prev is not None</code> 而不是 <code>if prev</code>？",
   "Morris 版為什麼發現不合法時不能直接 <code>return False</code>？",
 ],
})
print("P98 written")
