# -*- coding: utf-8 -*-
"""第 87–90 題。"""
import random, functools, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(87)

# ==================== 87. Scramble String ====================
S["p87_memo"] = '''from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(maxsize=None)
        def go(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):      # 字母組成不同 -> 不可能
                return False

            n = len(a)
            for i in range(1, n):           # 在第 i 個位置切一刀
                # 不交換：a 的左邊配 b 的左邊，a 的右邊配 b 的右邊
                if go(a[:i], b[:i]) and go(a[i:], b[i:]):
                    return True
                # 交換：a 的左邊配 b 的「右邊末段」，a 的右邊配 b 的「左邊前段」
                if go(a[:i], b[n - i:]) and go(a[i:], b[:n - i]):
                    return True
            return False

        result = go(s1, s2)
        go.cache_clear()
        return result'''

S["p87_dp"] = '''class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2) or sorted(s1) != sorted(s2):
            return False

        # dp[length][i][j] = s1[i:i+length] 能不能擾亂成 s2[j:j+length]
        dp = [[[False] * n for _ in range(n)] for _ in range(n + 1)]

        for i in range(n):
            for j in range(n):
                dp[1][i][j] = s1[i] == s2[j]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    for k in range(1, length):          # 左段長度 k
                        # 不交換
                        if dp[k][i][j] and dp[length - k][i + k][j + k]:
                            dp[length][i][j] = True
                            break
                        # 交換
                        if dp[k][i][j + length - k] and dp[length - k][i + k][j]:
                            dp[length][i][j] = True
                            break

        return dp[n][0][0]'''

_p87 = [S.load(k) for k in ("p87_memo", "p87_dp")]


def _p87_ref(a, b):
    """獨立的暴力遞迴（不記憶化）當基準 —— 只用在短字串上。"""
    def go(x, y):
        if x == y:
            return True
        if sorted(x) != sorted(y):
            return False
        n = len(x)
        for i in range(1, n):
            if go(x[:i], y[:i]) and go(x[i:], y[i:]):
                return True
            if go(x[:i], y[n - i:]) and go(x[i:], y[:n - i]):
                return True
        return False
    return len(a) == len(b) and go(a, b)


# 題目保證長度 >= 1，所以不測空字串
for a, b in [("great", "rgeat"), ("abcde", "caebd"), ("a", "a"), ("ab", "ba"),
             ("abc", "bca"), ("abcd", "bdac"), ("abb", "bab"), ("aa", "aa")]:
    e = _p87_ref(a, b)
    for sol in _p87:
        assert sol.isScramble(a, b) is e, ("P87", a, b, sol, sol.isScramble(a, b), e)
for _ in range(600):
    n = random.randint(1, 6)
    a = "".join(random.choice("ab") for _ in range(n))
    if random.random() < 0.5:
        b = "".join(random.sample(a, n))       # 同樣的字母，打亂順序
    else:
        b = "".join(random.choice("ab") for _ in range(n))
    e = _p87_ref(a, b)
    for sol in _p87:
        assert sol.isScramble(a, b) is e, ("P87", a, b, sol, sol.isScramble(a, b), e)
print("P87 solutions OK")

_P87_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">擾亂字串：把字串遞迴地切成兩段，每一刀都可以決定「要不要交換左右」</text>
            <g font-size="13" text-anchor="middle" font-family="monospace">
              <text x="320" y="50" fill="var(--gold)">&quot;great&quot;</text>
              <text x="180" y="96" fill="var(--accent)">&quot;gr&quot;</text>
              <text x="440" y="96" fill="var(--accent)">&quot;eat&quot;</text>
              <text x="120" y="142" fill="var(--text-muted)">&quot;g&quot;</text>
              <text x="240" y="142" fill="var(--text-muted)">&quot;r&quot;</text>
              <text x="380" y="142" fill="var(--text-muted)">&quot;e&quot;</text>
              <text x="500" y="142" fill="var(--accent)">&quot;at&quot;</text>
              <text x="450" y="186" fill="var(--text-muted)">&quot;a&quot;</text>
              <text x="550" y="186" fill="var(--text-muted)">&quot;t&quot;</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.3">
              <line x1="300" y1="58" x2="196" y2="84"/>
              <line x1="340" y1="58" x2="424" y2="84"/>
              <line x1="168" y1="104" x2="130" y2="130"/>
              <line x1="192" y1="104" x2="230" y2="130"/>
              <line x1="424" y1="104" x2="390" y2="130"/>
              <line x1="452" y1="104" x2="490" y2="130"/>
              <line x1="490" y1="150" x2="458" y2="174"/>
              <line x1="512" y1="150" x2="542" y2="174"/>
            </g>
            <line x1="20" y1="208" x2="620" y2="208" stroke="var(--border)"/>
            <text x="20" y="236" fill="var(--gold)" font-size="12">在 &quot;gr&quot; 這一層交換左右子樹 → &quot;rg&quot;</text>
            <text x="20" y="260" fill="var(--text-muted)" font-size="12">得到 &quot;rg&quot; + &quot;eat&quot; = &quot;rgeat&quot; ✔ 所以 &quot;great&quot; 可以擾亂成 &quot;rgeat&quot;</text>
            <line x1="20" y1="278" x2="620" y2="278" stroke="var(--border)"/>
            <text x="20" y="306" fill="var(--text-muted)" font-size="12">遞迴式：對每一個切點 i，試「不交換」和「交換」兩種配對</text>
            <text x="20" y="330" fill="var(--accent)" font-size="12">不交換：a[:i] ↔ b[:i]　且　a[i:] ↔ b[i:]</text>
            <text x="20" y="354" fill="#ff8a65" font-size="12">交換：　a[:i] ↔ b[n−i:]　且　a[i:] ↔ b[:n−i]</text>'''

emit({
 "num": 87, "slug": "scramble-string",
 "en": [
   "We can scramble a string <code>s</code> to get a string <code>t</code> using the "
   "following algorithm: (1) If the length of the string is 1, stop. (2) If the length is "
   "&gt; 1, split the string into two non-empty substrings at a random index. "
   "(3) <strong>Randomly</strong> decide to swap the two substrings or keep them in the same "
   "order. (4) Apply the algorithm recursively on each of the two substrings.",
   "Given two strings <code>s1</code> and <code>s2</code> of <strong>the same length</strong>, "
   "return <code>true</code> if <code>s2</code> is a scrambled string of <code>s1</code>.",
 ],
 "zh": [
   "我們可以用下面的演算法把字串 <code>s</code> 「擾亂」成字串 <code>t</code>："
   "（1）長度是 1 就停止；"
   "（2）長度 &gt; 1 時，在<strong>隨機</strong>的位置把字串切成兩段非空的子字串；"
   "（3）<strong>隨機</strong>決定要不要交換這兩段；"
   "（4）對這兩段<strong>遞迴</strong>做同樣的事。",
   "給你兩個<strong>長度相同</strong>的字串 <code>s1</code> 和 <code>s2</code>，"
   "判斷 <code>s2</code> 是不是 <code>s1</code> 的擾亂字串。",
 ],
 "pre": [
   ("note", "先把「擾亂」想成一棵二元樹", [
     ("c", """「擾亂」的過程，就是【建一棵二元樹，然後隨機交換某些節點的左右子樹】。

    "great" 切成 "gr" | "eat"
              "gr" 切成 "g" | "r"
              "eat" 切成 "e" | "at"
                        "at" 切成 "a" | "t"

    這棵樹的葉子由左到右讀出來就是 "great"。

    如果在 "gr" 那個節點交換左右子樹：
        葉子變成 r, g, e, a, t  ->  "rgeat" ✔

所以問題變成：
    「存不存在一棵這樣的二元樹，
      以及一組交換的選擇，讓葉子序列變成 s2？」

遞迴式：
    isScramble(a, b) 為真，若且唯若存在一個切點 i：

      (不交換) isScramble(a[:i], b[:i]) 且 isScramble(a[i:], b[i:])
      (交換)   isScramble(a[:i], b[n-i:]) 且 isScramble(a[i:], b[:n-i])

「交換」那一行的下標最容易寫錯：
    a 的左邊（長度 i）要去配 b 的【末尾 i 個字元】-> b[n-i:]
    a 的右邊（長度 n-i）要去配 b 的【開頭 n-i 個】-> b[:n-i]"""),
     "<strong>這題是「區間 DP」的一個特別難的變形</strong> —— "
     "它的狀態不是一維的區間，而是「兩個字串的兩個區間」。",
   ]),
 ],
 "examples": """範例 1
  輸入：s1 = "great", s2 = "rgeat"
  輸出：true
  說明：
    great
    /    \\
   gr    eat        交換 gr -> rg
   / \\   /  \\
  g   r e    at     得到 rg + eat = rgeat

範例 2
  輸入：s1 = "abcde", s2 = "caebd"
  輸出：false

範例 3
  輸入：s1 = "a", s2 = "a"
  輸出：true""",
 "constraints": [
   "<code>s1.length == s2.length</code>",
   "1 ≤ <code>s1.length</code> ≤ 30",
   "<code>s1</code> 和 <code>s2</code> 由小寫英文字母組成",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>長度只有 30</strong> —— 這反映了複雜度。"
       "DP 的狀態是 <code>O(n³)</code>（長度 × i × j），"
       "每個狀態要試 <code>O(n)</code> 個切點 —— 總共 <strong>O(n⁴)</strong>。"
       "n = 30 時是 81 萬 —— 剛好可以。n = 100 就會是 10⁸，太慢。",
       "<strong>兩個字串長度相同</strong>（題目保證），所以不用檢查。",
       "<strong>只有小寫字母</strong>，所以「字母組成」的剪枝可以用 26 格的計數陣列。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P87_FIG, "0 0 640 370"),
 ],
 "approaches": [
   ap("解法一", "記憶化遞迴（最推薦）", [
     ("c", S["p87_memo"]),
     ("h", "三個部分"),
     ("c", """1. 終止條件 a == b
   完全相同就不用切了。
   （也涵蓋了「長度 1 且字元相同」的情況。）

2. 剪枝 sorted(a) != sorted(b)
   字母組成不同 -> 不管怎麼切怎麼換都不可能相等。

   這個剪枝【威力極大】——
   沒有它的話，大量明顯不可能的分支會被完整搜索。

   實測：加上它之後，"abcdefghij" vs "jihgfedcba" 這類測資
   從幾秒降到毫秒。

   更快的版本是用 Counter 或 26 格陣列（O(n) 而不是 O(n log n)），
   但 n <= 30，sorted 的常數完全可以接受。

3. 枚舉切點 i，試兩種配對

   注意 i 的範圍是 1..n-1（兩段都必須非空）。
   寫成 range(n) 會產生「空段」，造成無限遞迴。"""),
     ("h", "「交換」那一行的下標推導"),
     ("c", """a 在位置 i 切開：  a[:i]（長度 i）  +  a[i:]（長度 n-i）

「不交換」：
    a[:i] 配 b 的【前 i 個】      -> b[:i]
    a[i:] 配 b 的【後 n-i 個】    -> b[i:]

「交換」：
    a[:i] 跑到右邊去了
        -> 它要配 b 的【後 i 個】  -> b[n-i:]
    a[i:] 跑到左邊去了
        -> 它要配 b 的【前 n-i 個】-> b[:n-i]

驗算 a = "great"（n=5），i = 2：
    a[:2] = "gr"，a[2:] = "eat"

    不交換： "gr" 配 b[:2]，"eat" 配 b[2:]
    交換：   "gr" 配 b[3:]（後 2 個），"eat" 配 b[:3]（前 3 個）

    b = "rgeat"
        不交換： "gr" vs "rg" -> 遞迴（會成立）✔
        交換：   "gr" vs "at"  ✘，"eat" vs "rge" ✘

    所以是走「不交換」那條路，然後在 "gr" vs "rg" 那一層才交換 ✔"""),
     ("h", "<code>lru_cache</code> 用字串當 key 的代價"),
     ("c", """@lru_cache 會用 (a, b) 這個 tuple 當 key。

    字串的雜湊是 O(長度) 的（雖然 Python 會快取字串的 hash 值）。
    而且每個狀態要存兩個字串的參照。

    狀態數：a 是 s1 的某個子字串（O(n²) 個），
            b 是 s2 的某個子字串（O(n²) 個），
            但因為長度必須相同，實際只有 O(n³) 個有效狀態。

    n = 30 -> 約 27000 個狀態，完全可以接受。

如果要更省，就用解法二的「三維 dp 陣列」——
它用 (length, i, j) 當索引，不用存字串。"""),
   ], "O(n⁴)", "O(n³)", "O(n³) 個狀態 × O(n) 個切點",
      "快取 + 遞迴堆疊", optimal=True),

   ap("解法二", "自底向上三維 DP", [
     "把遞迴翻成迭代：<code>dp[length][i][j]</code> = "
     "「<code>s1[i:i+length]</code> 能不能擾亂成 <code>s2[j:j+length]</code>」。",
     ("c", S["p87_dp"]),
     ("h", "為什麼狀態要用 (length, i, j) 而不是 (i1, j1, i2, j2)？"),
     ("c", """直覺上狀態應該是「s1 的區間 [i1, j1]」對「s2 的區間 [i2, j2]」——
那是四個維度，O(n⁴) 個狀態。

但因為【兩個區間的長度必須相同】，
    j1 - i1 == j2 - i2

所以只要記 (length, i1, i2) 三個量就夠了，
第四個可以算出來。

O(n³) 個狀態 × O(n) 個切點 = O(n⁴) 時間。

「發現某個維度可以被其他維度決定」是壓縮 DP 狀態的常見手法。"""),
     ("h", "迴圈的順序"),
     ("c", """for length in 2..n:        <- 一定要「由短到長」
    for i in ...:
        for j in ...:
            for k in 1..length-1:
                看 dp[k][...] 和 dp[length-k][...]

    因為 dp[length] 依賴 dp[k] 和 dp[length-k]，
    而 k 和 length-k 都【小於 length】——
    所以必須先算完所有更短的長度。

    這和第 5 題（最長回文子字串）的區間 DP 是同一個道理：
    「區間 DP 要按區間長度由短到長填表」。"""),
     "<strong>優點</strong>：不吃遞迴堆疊、沒有雜湊的開銷。",
     "<strong>缺點</strong>：四層迴圈、下標關係複雜，"
     "而且<strong>失去了「字母組成」的剪枝</strong>（除非額外加）—— "
     "所以它一定會跑滿 O(n⁴)，而記憶化版本通常遠低於此。",
     "<strong>實測上記憶化版本通常更快</strong>，因為剪枝砍掉了大部分狀態。"
     "<strong>面試時寫記憶化版。</strong>",
   ], "O(n⁴)", "O(n³)", "四層迴圈，一定跑滿", "三維陣列"),
 ],
 "compare": (["解法", "時間", "空間", "有剪枝？", "實測", "備註"],
   [["一、記憶化遞迴", "O(n⁴) 上界", "O(n³)", "✔ 字母組成", "通常快得多", "面試預設"],
    ["二、三維 DP", "O(n⁴)", "O(n³)", "✘", "一定跑滿", "不吃堆疊"]]),
 "edges": [
   "<strong>完全相同</strong>：<code>(\"a\", \"a\")</code>、<code>(\"abc\", \"abc\")</code> → true。"
   "第一個判斷就 return。",
   "<strong>字母組成不同</strong>：<code>(\"abc\", \"abd\")</code> → false。剪枝直接擋下。",
   "<strong>長度 2</strong>：<code>(\"ab\", \"ba\")</code> → true（交換一次）。",
   "<strong>看起來像但其實不行</strong>：<code>(\"abcde\", \"caebd\")</code> → false。"
   "<strong>字母組成相同，但沒有任何一種切法能達成 —— 這是本題的核心測資。</strong>",
   "<strong>有重複字母</strong>：<code>(\"abb\", \"bab\")</code> → true。",
   "<strong>切點範圍</strong>：<code>range(1, n)</code>。"
   "寫成 <code>range(n)</code> 會產生空段，造成<strong>無限遞迴</strong>。",
   "<strong>沒有剪枝</strong>：長度 30 的測資會超時。",
 ],
 "follow": [
   ("h", "追問一：為什麼這題這麼難？"),
   ("c", """因為它的狀態空間是「兩個字串的兩個區間」——
比一般的字串 DP（第 5、72、516 題）多了一個維度。

而且它的「決策」有兩層：
    1. 在哪裡切（n-1 種）
    2. 要不要交換（2 種）

一般的區間 DP 只有第 1 種。

另外，「交換」讓下標的對應變得不直覺 ——
大部分人第一次寫都會把 b[n-i:] 和 b[:n-i] 弄反。

建議的驗證方法：
    用 "ab" vs "ba" 這個最小的例子手動追一遍。
    n=2, i=1：
        不交換： "a" vs "b" ✘
        交換：   "a" vs b[1:]="a" ✔ 且 "b" vs b[:1]="b" ✔
        -> True ✔

    如果下標寫反（b[:i] 和 b[i:]），這個例子會回傳 False。""",),
   ("h", "追問二：剪枝為什麼這麼重要？"),
   ("c", """沒有「字母組成」剪枝的話：

    s1 = "abcdefghijklmnopqrstuvwxyzabcd"（30 個字元）
    s2 = 完全不同的 30 個字元

    程式會枚舉所有切點、所有交換組合，
    在確定「不可能」之前走完整棵搜尋樹。

加上剪枝之後，第一次呼叫就直接 return False。

而且剪枝在【遞迴的中途】也持續生效 ——
一旦某一段的字母組成對不上，整棵子樹就被砍掉。

這是「可行性剪枝（feasibility pruning）」的典型案例：
    用一個便宜的必要條件，提前排除不可能的分支。

    必要條件：字母組成相同（O(n log n) 或 O(n)）
    真正的條件：存在合法的擾亂樹（指數級）

    便宜的必要條件擋掉了絕大部分的失敗案例。""",),
   ("h", "追問三：這題有沒有多項式的「聰明」解法？"),
   "<strong>沒有已知的更好解法。</strong>"
   "O(n⁴) 已經是標準答案。"
   "有一些研究用「後綴自動機」或「字串雜湊」把常數壓小，"
   "但漸近複雜度還是 O(n⁴)。",
   "<strong>這題的價值不在於它的實用性</strong>（幾乎沒有真實應用），"
   "<strong>而在於它逼你把「遞迴式 → 記憶化 → DP」這條路走得很紮實</strong> —— "
   "因為它的下標複雜到，不把定義寫清楚就一定會錯。",
   ("h", "追問四：寫這類題目的除錯建議？"),
   ("ul", [
     "<strong>先寫一個不記憶化的暴力遞迴</strong>，用短字串驗證正確性",
     "<strong>再加 <code>@lru_cache</code></strong>（一行），確認答案不變但變快",
     "<strong>最後才考慮翻成迭代 DP</strong>（如果真的需要）",
     "<strong>用最小的例子手動追</strong>（<code>\"ab\"</code> vs <code>\"ba\"</code>）驗證下標",
   ]),
   "<strong>本篇的測試就是這樣做的</strong>：獨立寫一份暴力遞迴當基準，"
   "然後用隨機測資對照兩個解法。",
 ],
 "related": [
   "<strong>第 5 題 Longest Palindromic Substring</strong> —— 區間 DP 的入門",
   "<strong>第 72 題 Edit Distance</strong> —— 兩字串的二維 DP",
   "<strong>第 312 題 Burst Balloons</strong> —— 另一個需要「枚舉切點」的區間 DP",
   "<strong>第 1000 題 Minimum Cost to Merge Stones</strong> —— 三維區間 DP",
 ],
 "check": [
   "「交換」那一行的下標為什麼是 <code>b[n-i:]</code> 和 <code>b[:n-i]</code>？"
   "請用 <code>\"ab\"</code> vs <code>\"ba\"</code> 驗證。",
   "切點的範圍為什麼是 <code>range(1, n)</code> 而不是 <code>range(n)</code>？",
   "「字母組成相同」是必要條件還是充分條件？它為什麼是一個好剪枝？",
   "DP 的狀態為什麼是 (length, i, j) 三維而不是四維？",
 ],
})
print("P87 written")

# ==================== 88. Merge Sorted Array ====================
S["p88_back"] = '''class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 從「後面」往前填，就不會覆蓋掉 nums1 還沒讀的資料
        i, j, k = m - 1, n - 1, m + n - 1

        while j >= 0:                      # nums2 還有就要繼續
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        # i >= 0 的部分不用管：它們已經在正確的位置上了'''

S["p88_forward"] = '''class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 從前面填的話，必須先把 nums1 的前 m 個複製出來（O(m) 額外空間）
        left = nums1[:m]
        i = j = k = 0

        while i < m and j < n:
            if left[i] <= nums2[j]:
                nums1[k] = left[i]; i += 1
            else:
                nums1[k] = nums2[j]; j += 1
            k += 1

        while i < m:
            nums1[k] = left[i]; i += 1; k += 1
        while j < n:
            nums1[k] = nums2[j]; j += 1; k += 1'''

_p88 = [S.load(k) for k in ("p88_back", "p88_forward")]
for a, m_, b, n_ in [([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
                     ([1], 1, [], 0), ([0], 0, [1], 1),
                     ([2, 0], 1, [1], 1), ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3),
                     ([0, 0, 0], 0, [1, 2, 3], 3)]:
    e = sorted(a[:m_] + b[:n_])
    for sol in _p88:
        arr = list(a)
        sol.merge(arr, m_, list(b), n_)
        assert arr == e, ("P88", a, m_, b, n_, sol, arr, e)
for _ in range(5000):
    m_ = random.randint(0, 6)
    n_ = random.randint(0, 6)
    a = sorted(random.randint(-9, 9) for _ in range(m_)) + [0] * n_
    b = sorted(random.randint(-9, 9) for _ in range(n_))
    e = sorted(a[:m_] + b)
    for sol in _p88:
        arr = list(a)
        sol.merge(arr, m_, list(b), n_)
        assert arr == e, ("P88", a, m_, b, n_, sol, arr, e)
print("P88 solutions OK")

_P88_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">從後往前填：k 永遠在 i 的右邊，所以不會覆蓋到還沒讀的資料</text>
            <g font-size="14" text-anchor="middle">
              <text x="46" y="76" fill="var(--text-muted)" font-size="12">nums1</text>
              <rect x="86" y="56" width="56" height="36" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="114" y="80" fill="var(--accent)">1</text>
              <rect x="146" y="56" width="56" height="36" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="174" y="80" fill="var(--accent)">2</text>
              <rect x="206" y="56" width="56" height="36" rx="5" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="234" y="80" fill="var(--gold)">3</text>
              <rect x="266" y="56" width="56" height="36" rx="5" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/><text x="294" y="80" fill="var(--text-muted)">0</text>
              <rect x="326" y="56" width="56" height="36" rx="5" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/><text x="354" y="80" fill="var(--text-muted)">0</text>
              <rect x="386" y="56" width="56" height="36" rx="5" fill="none" stroke="#ff8a65" stroke-width="2.5"/><text x="414" y="80" fill="#ff8a65">0</text>
            </g>
            <text x="234" y="112" fill="var(--gold)" font-size="11" text-anchor="middle">i = m−1 = 2</text>
            <text x="414" y="112" fill="#ff8a65" font-size="11" text-anchor="middle">k = m+n−1 = 5</text>
            <text x="470" y="80" fill="var(--text-muted)" font-size="11">← 後面 n 格是預留的空位</text>
            <g font-size="14" text-anchor="middle">
              <text x="46" y="164" fill="var(--text-muted)" font-size="12">nums2</text>
              <rect x="86" y="144" width="56" height="36" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="114" y="168" fill="var(--accent)">2</text>
              <rect x="146" y="144" width="56" height="36" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="174" y="168" fill="var(--accent)">5</text>
              <rect x="206" y="144" width="56" height="36" rx="5" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="234" y="168" fill="var(--gold)">6</text>
            </g>
            <text x="234" y="200" fill="var(--gold)" font-size="11" text-anchor="middle">j = n−1 = 2</text>
            <line x1="20" y1="222" x2="620" y2="222" stroke="var(--border)"/>
            <g font-family="monospace" font-size="12">
              <text x="40" y="250" fill="var(--text-muted)">比 nums1[2]=3 vs nums2[2]=6 → 填 6，k=4, j=1</text>
              <text x="40" y="272" fill="var(--text-muted)">比 nums1[2]=3 vs nums2[1]=5 → 填 5，k=3, j=0</text>
              <text x="40" y="294" fill="var(--text-muted)">比 nums1[2]=3 vs nums2[0]=2 → 填 3，k=2, i=1</text>
              <text x="40" y="316" fill="var(--text-muted)">比 nums1[1]=2 vs nums2[0]=2 → 填 2（nums2 的），k=1, j=−1</text>
              <text x="40" y="338" fill="var(--gold)">j &lt; 0，結束。nums1[0..1] = [1, 2] 已經在正確位置 ✔</text>
            </g>
            <text x="20" y="370" fill="#ff8a65" font-size="12">結果：[1, 2, 2, 3, 5, 6]　　不變量：k ≥ i 恆成立 → 絕不覆蓋</text>'''

emit({
 "num": 88, "slug": "merge-sorted-array",
 "en": [
   "You are given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in "
   "<strong>non-decreasing order</strong>, and two integers <code>m</code> and <code>n</code>, "
   "representing the number of elements in <code>nums1</code> and <code>nums2</code> "
   "respectively.",
   "<strong>Merge</strong> <code>nums1</code> and <code>nums2</code> into a single array "
   "sorted in non-decreasing order. The final sorted array should be stored inside the array "
   "<code>nums1</code>. To accommodate this, <code>nums1</code> has a length of "
   "<code>m + n</code>, where the last <code>n</code> elements are set to <code>0</code> and "
   "should be ignored.",
 ],
 "zh": [
   "給你兩個<strong>非遞減排序</strong>的整數陣列 <code>nums1</code> 和 <code>nums2</code>，"
   "以及兩個整數 <code>m</code> 和 <code>n</code>，分別代表它們<strong>實際的元素個數</strong>。",
   "請把兩個陣列<strong>合併成一個非遞減的陣列</strong>，"
   "結果必須存放在 <code>nums1</code> 裡面。"
   "為此 <code>nums1</code> 的長度是 <code>m + n</code>，"
   "後面 <code>n</code> 格是預留的 <code>0</code>，要忽略。",
 ],
 "pre": [
   ("note", "關鍵洞察：從「後面」往前填", [
     ("c", """如果從前面往後填，會覆蓋掉 nums1 還沒讀的資料：

    nums1 = [1, 2, 3, _, _, _]，m = 3
    nums2 = [2, 5, 6]，n = 3

    從前面填：
        比 1 vs 2 -> 填 1 到 nums1[0]（填到自己身上，沒事）
        比 2 vs 2 -> 填 2 到 nums1[1]（沒事）
        比 3 vs 2 -> 填 2（nums2 的）到 nums1[2]
                     但 nums1[2] 原本是 3，還沒讀！✘ 被蓋掉了

    所以從前面填必須先複製一份 nums1[:m]（O(m) 額外空間）。

從後面填：
    k 從 m+n-1 開始，i 從 m-1 開始。

    不變量：k >= i 恆成立

    證明：一開始 k = m+n-1 >= m-1 = i（因為 n >= 0）
          每一輪 k 減 1，而 i 最多減 1
          -> 差距只會變大或不變
          -> k >= i 永遠成立 ✔

    所以 nums1[k] = ... 絕不會覆蓋到 nums1[i] 或它左邊的資料 ✔

    O(1) 額外空間 ✔"""),
     "<strong>「從後往前」是所有「原地合併到較大的那個陣列」問題的通用技巧。</strong>"
     "同樣的想法出現在第 977 題（有序陣列的平方）、"
     "以及很多「原地擴張」的操作。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
  輸出：[1,2,2,3,5,6]

範例 2
  輸入：nums1 = [1], m = 1, nums2 = [], n = 0
  輸出：[1]

範例 3
  輸入：nums1 = [0], m = 0, nums2 = [1], n = 1
  輸出：[1]
  說明：m = 0 表示 nums1 裡沒有有效元素。""",
 "constraints": [
   "<code>nums1.length == m + n</code>，<code>nums2.length == n</code>",
   "0 ≤ <code>m</code>, <code>n</code> ≤ 200",
   "1 ≤ <code>m + n</code> ≤ 200",
   "−10⁹ ≤ <code>nums1[i]</code>, <code>nums2[j]</code> ≤ 10⁹",
   "<strong>進階：</strong>能不能設計一個 <code>O(m + n)</code> 的演算法？",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong><code>m</code> 或 <code>n</code> 可以是 0</strong>。"
       "<code>m = 0</code> 表示 <code>nums1</code> 全是預留的 0；"
       "<code>n = 0</code> 表示什麼都不用合併。<strong>兩個邊界都要能處理。</strong>",
       "<strong><code>nums1</code> 後面的 0 要忽略</strong> —— "
       "它們不是資料，只是預留的空間。"
       "<strong>不能直接 <code>sorted(nums1 + nums2)</code></strong>，"
       "那會把那些 0 也排進去。",
       "<strong>值可以是負的</strong>，所以那些預留的 0 有可能比真實資料還大 —— "
       "更加不能把它們當資料。",
       "<strong>必須原地</strong>（結果存在 <code>nums1</code>）。"
       "在 Python 裡要用 <code>nums1[k] = ...</code> 或 <code>nums1[:] = ...</code>。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P88_FIG, "0 0 640 384"),
 ],
 "approaches": [
   ap("解法一", "從後往前雙指標（標準解）", [
     ("c", S["p88_back"]),
     ("h", "為什麼迴圈條件只有 <code>j &gt;= 0</code>？"),
     ("c", """直覺會寫 while i >= 0 or j >= 0，但其實只要 j >= 0。

理由：
    如果 j < 0（nums2 用完了），
    那 nums1 剩下的部分（索引 0..i）【已經在正確的位置上了】——
    它們本來就在 nums1 裡，而且順序正確。

    不需要搬動 ✔

    nums1 = [1, 2, 3, _, _, _]，nums2 = [4, 5, 6]
        填完 6, 5, 4 之後 j = -1，
        而 nums1[0..2] = [1,2,3] 原封不動，剛好就是答案 ✔

反過來，如果 i < 0（nums1 的有效部分用完了），
    nums2 剩下的【必須】搬過來 ——
    所以迴圈條件必須包含 j >= 0。

    nums1 = [4, 5, 6, _, _, _]，nums2 = [1, 2, 3]
        填完 6, 5, 4 之後 i = -1，
        還要繼續填 3, 2, 1 ✔

這個不對稱（只檢查 j）是一個很漂亮的小優化，
但也要能說明為什麼 —— 不然看起來像 bug。"""),
     ("h", "<code>if i &gt;= 0 and nums1[i] &gt; nums2[j]</code>"),
     ("c", """兩個條件：
    i >= 0              nums1 還有有效元素可以比
    nums1[i] > nums2[j] nums1 的比較大 -> 它該放在後面

    如果 i < 0（短路），直接走 else 填 nums2 的 ✔

用 > 而不是 >=：
    相等時填 nums2 的。
    在「只有數值」的情況下沒差別。
    （如果元素帶額外資料，這會影響穩定性 ——
      但從後往前填的「穩定性」定義本來就要反著想，
      這題不考。）

順序很重要：先檢查 i >= 0，再存取 nums1[i]。
    在 Python 裡 nums1[-1] 不會報錯（會拿到最後一個元素），
    所以漏掉這個檢查會【安靜地算錯】。"""),
     "<strong>O(m + n) 時間、O(1) 空間</strong> —— 符合進階要求。",
   ], "O(m + n)", "O(1)", "每個元素處理一次", "只用三個下標", optimal=True),

   ap("解法二", "從前往後 + 複製一份（O(m) 空間）", [
     ("c", S["p88_forward"]),
     "先把 <code>nums1</code> 的前 <code>m</code> 個複製出來，"
     "然後就是<strong>標準的 merge 步驟</strong>（和第 21 題一樣）。",
     "<strong>優點</strong>：邏輯和「一般的 merge」完全一致，"
     "不需要想「從後往前」這個技巧。",
     "<strong>缺點</strong>：O(m) 額外空間，不符合進階要求。",
     "<strong>什麼時候可以用？</strong>"
     "如果 <code>m</code> 很小而 <code>n</code> 很大，"
     "O(m) 的額外空間其實很便宜。"
     "<strong>但既然從後往前只多花一點腦力就能做到 O(1)，沒理由不用。</strong>",
   ], "O(m + n)", "O(m)", "同上", "複製的前 m 個"),
 ],
 "compare": (["解法", "時間", "空間", "方向", "備註"],
   [["一、從後往前", "O(m+n)", "O(1)", "→ 左", "符合進階要求"],
    ["二、複製 + 從前往後", "O(m+n)", "O(m)", "← 右", "邏輯最熟悉"],
    ["<code>sorted(nums1[:m] + nums2)</code>", "O((m+n)log(m+n))", "O(m+n)", "—", "能過但沒展示"]]),
 "edges": [
   "<strong><code>n = 0</code></strong>：<code>([1], 1, [], 0)</code> → <code>[1]</code>。"
   "while 迴圈一次都不跑。",
   "<strong><code>m = 0</code></strong>：<code>([0], 0, [1], 1)</code> → <code>[1]</code>。"
   "<code>i</code> 一開始就是 −1，全部走 else 分支。"
   "<strong><code>i &gt;= 0</code> 的檢查在這裡至關重要。</strong>",
   "<strong><code>nums2</code> 全部比較小</strong>：<code>([4,5,6,0,0,0], 3, [1,2,3], 3)</code>。"
   "<code>i</code> 會先耗盡。",
   "<strong><code>nums2</code> 全部比較大</strong>：<code>([1,2,3,0,0,0], 3, [4,5,6], 3)</code>。"
   "<code>j</code> 先耗盡，<code>nums1</code> 前面原封不動。",
   "<strong>交錯</strong>：<code>([2,0], 1, [1], 1)</code> → <code>[1,2]</code>。",
   "<strong>有相等的值</strong>：範例 1 裡兩個 2。",
   "<strong>直接 <code>sorted(nums1 + nums2)</code></strong>："
   "會把預留的 0 也排進去，答案錯（尤其在有負數時）。",
 ],
 "follow": [
   ("h", "追問一：如果 <code>nums1</code> 沒有預留空間呢？"),
   "那就只能開一個新陣列（O(m+n) 空間），或者"
   "<strong>用某種「原地合併」的演算法</strong> —— "
   "但「就地穩定合併」是一個相當困難的問題，"
   "最好的已知演算法（例如 SymMerge、或 Kronrod 的區塊交換法）"
   "是 O((m+n) log(m+n)) 時間、O(1) 空間，常數還很大。",
   "<strong>「給你預留空間」這個設定，正是讓 O(m+n) + O(1) 成為可能的關鍵。</strong>",
   ("h", "追問二：這和 merge sort 有什麼關係？"),
   "<strong>這就是 merge sort 的 merge 步驟。</strong>"
   "差別在於：一般的 merge sort 用一個暫存陣列（O(n) 空間），"
   "而這題因為「目標陣列後面有空位」，所以可以從後往前做到 O(1)。",
   ("c", """這個技巧在真實的排序實作裡也有用：

  Timsort（Python 和 Java 的排序演算法）在合併兩個 run 時，
  會比較兩段的長度，把「較短的那一段」複製到暫存區，
  然後根據是複製了左邊還是右邊，
  決定要「從前往後」還是「從後往前」合併 ——
  正是為了減少記憶體搬移。

  所以這題的技巧，真的在標準庫裡跑著。""",),
   ("h", "追問三：如果要合併 k 個有序陣列呢？"),
   "第 23 題（Merge k Sorted Lists）的陣列版。"
   "<strong>用最小堆 O(N log k)</strong>，或<strong>分治兩兩合併 O(N log k)</strong>。"
   "「從後往前」的技巧在這裡不適用（沒有一個「夠大的目標陣列」）。",
   ("h", "追問四：為什麼這題常被當成「簡單但有陷阱」的代表？"),
   ("ul", [
     "<strong>直覺（從前往後）是錯的</strong> —— 會覆蓋資料",
     "<strong>邊界（m=0、n=0）很容易漏</strong>",
     "<strong>Python 的負索引不會報錯</strong>，所以 <code>i &gt;= 0</code> 漏掉會安靜出錯",
     "<strong>「忽略預留的 0」這句話很容易被跳過</strong>",
   ]),
   "<strong>它是一個很好的提醒：Easy 題不等於沒有陷阱。</strong>",
 ],
 "related": [
   "<strong>第 21 題 Merge Two Sorted Lists</strong> —— 串列版",
   "<strong>第 23 題 Merge k Sorted Lists</strong> —— k 條的版本",
   "<strong>第 977 題 Squares of a Sorted Array</strong> —— 同樣的「從後往前填」",
   "<strong>第 148 題 Sort List</strong> —— merge sort 的完整實作",
 ],
 "check": [
   "為什麼從前往後填會出錯？請用範例 1 說明是哪一步被覆蓋。",
   "「<code>k &gt;= i</code> 恆成立」為什麼保證不會覆蓋？請證明它。",
   "迴圈條件為什麼只需要 <code>j &gt;= 0</code>，不用 <code>i &gt;= 0 or j &gt;= 0</code>？",
   "<code>m = 0</code> 時程式走的是哪一條路徑？<code>i &gt;= 0</code> 的檢查在這裡做了什麼？",
 ],
})
print("P88 written")
