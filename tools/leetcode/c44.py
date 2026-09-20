# -*- coding: utf-8 -*-
"""第 44–46 題。"""
import random, re, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(44)

# ==================== 44. Wildcard Matching ====================
S["p44_dp"] = '''class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        # dp[i][j] = s 的前 i 個字元，能不能被 p 的前 j 個字元匹配
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # 空字串 vs 只由 '*' 組成的前綴
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    # '*' 配空（不用它）   或   '*' 多吃一個 s[i-1]
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
                elif p[j - 1] in (s[i - 1], "?"):
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]'''

S["p44_greedy"] = '''class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0                    # s 和 p 的指標
        star = -1                    # p 裡「最後一個 *」的位置
        match = 0                    # 那個 * 目前吃掉了 s 的哪個位置

        while i < len(s):
            if j < len(p) and p[j] in (s[i], "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                star = j             # 記住這個 *
                match = i            # 先讓它吃 0 個
                j += 1
            elif star != -1:
                # 卡住了，但前面有 * -> 讓它多吃一個字元，從 * 之後重來
                j = star + 1
                match += 1
                i = match
            else:
                return False         # 卡住而且沒有 * 可以回溯

        # s 用完了，p 剩下的必須全是 '*'
        while j < len(p) and p[j] == "*":
            j += 1
        return j == len(p)'''

_p44 = [S.load(k) for k in ("p44_dp", "p44_greedy")]


def _p44_ref(s, p):
    """把 wildcard 轉成正規表示式當基準。"""
    rx = "".join({"*": ".*", "?": "."}.get(c, re.escape(c)) for c in p)
    return re.fullmatch(rx, s) is not None


for s_, p_ in [("aa", "a"), ("aa", "*"), ("cb", "?a"), ("adceb", "*a*b"),
               ("acdcb", "a*c?b"), ("", ""), ("", "*"), ("", "***"),
               ("a", ""), ("abc", "a*c"), ("aaaa", "*a*a*a*a*")]:
    e = _p44_ref(s_, p_)
    for sol in _p44:
        assert sol.isMatch(s_, p_) is e, ("P44", s_, p_, sol, sol.isMatch(s_, p_), e)
for _ in range(4000):
    s_ = "".join(random.choice("ab") for _ in range(random.randint(0, 7)))
    p_ = "".join(random.choice("ab?*") for _ in range(random.randint(0, 6)))
    e = _p44_ref(s_, p_)
    for sol in _p44:
        assert sol.isMatch(s_, p_) is e, ("P44", repr(s_), repr(p_), sol)
print("P44 solutions OK")

_P44_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">貪婪 + 回溯：* 先吃 0 個，卡住了才讓它多吃一個</text>
            <text x="20" y="50" fill="var(--text-muted)" font-size="12">s = &quot;adceb&quot;，p = &quot;*a*b&quot;</text>
            <g font-family="monospace" font-size="13">
              <text x="40" y="82" fill="var(--gold)">① p[0] = &apos;*&apos;  →  記下 star=0, match=0，先吃 0 個，j=1</text>
              <text x="40" y="106" fill="var(--accent)">② p[1]=&apos;a&apos; vs s[0]=&apos;a&apos;  ✔  i=1, j=2</text>
              <text x="40" y="130" fill="var(--gold)">③ p[2] = &apos;*&apos;  →  star=2, match=1，j=3</text>
              <text x="40" y="154" fill="#ff8a65">④ p[3]=&apos;b&apos; vs s[1]=&apos;d&apos;  ✘  但有 star</text>
              <text x="76" y="176" fill="#ff8a65">→ 回到 j=star+1=3，match=2，i=2</text>
              <text x="40" y="200" fill="#ff8a65">⑤ p[3]=&apos;b&apos; vs s[2]=&apos;c&apos;  ✘  → match=3, i=3</text>
              <text x="40" y="224" fill="#ff8a65">⑥ p[3]=&apos;b&apos; vs s[3]=&apos;e&apos;  ✘  → match=4, i=4</text>
              <text x="40" y="248" fill="var(--accent)">⑦ p[3]=&apos;b&apos; vs s[4]=&apos;b&apos;  ✔  i=5, j=4</text>
              <text x="40" y="272" fill="var(--accent)">⑧ i == len(s)，j == len(p)  →  匹配成功 ✔</text>
            </g>
            <text x="20" y="306" fill="var(--gold)" font-size="12">只回溯到「最後一個 *」就夠了 —— 這是本題能用貪婪的關鍵，第 10 題做不到。</text>'''

emit({
 "num": 44, "slug": "wildcard-matching",
 "en": [
   "Given an input string <code>s</code> and a pattern <code>p</code>, implement wildcard "
   "pattern matching with support for <code>'?'</code> and <code>'*'</code> where:",
   "<code>'?'</code> matches any <strong>single</strong> character; "
   "<code>'*'</code> matches any <strong>sequence</strong> of characters "
   "(including the empty sequence).",
   "The matching should cover the <strong>entire</strong> input string.",
 ],
 "zh": [
   "給你一個字串 <code>s</code> 和一個模式 <code>p</code>，"
   "實作支援 <code>'?'</code> 和 <code>'*'</code> 的<strong>萬用字元匹配</strong>：",
   "<code>'?'</code> 匹配<strong>任意單一字元</strong>；"
   "<code>'*'</code> 匹配<strong>任意一段字元序列</strong>（可以是空的）。",
   "匹配必須覆蓋<strong>整個</strong> <code>s</code>。",
 ],
 "pre": [
   ("note", "和第 10 題（正規表示式匹配）的關鍵差異", [
     ("c", """第 10 題 Regular Expression        第 44 題 Wildcard（本題）
--------------------------        --------------------------
'.'  配任意「一個」字元             '?'  配任意「一個」字元
'*'  「前一個元素」重複 0+ 次        '*'  自己就配任意「一段」

差異的後果非常大：

    第 10 題的 '*' 和前一個字元「綁在一起」，
    "a*" 是一個不可分割的單位，只能配 a 的重複。
    -> 貪婪行不通，必須 DP。

    第 44 題的 '*' 是「獨立」的，
    它可以配任何東西，和前後完全無關。
    -> 可以用「先吃 0 個，卡住再多吃一個」的貪婪 + 回溯。

這就是為什麼第 44 題有 O(1) 空間的解，而第 10 題沒有。

這也是 shell 萬用字元（ls *.txt）和 regex 的差別：
    shell 的 *.txt  =  任意字元 + ".txt"
    regex 的 *.txt  =  「任意多個任意字元」+ 任意一個字元 + "txt"
                       （因為 regex 的 * 要有前綴，這裡是 .）"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "aa", p = "a"
  輸出：false

範例 2
  輸入：s = "aa", p = "*"
  輸出：true
  說明：'*' 可以配任意長度的序列。

範例 3
  輸入：s = "cb", p = "?a"
  輸出：false
  說明：'?' 配掉 'c'，但 'a' 配不上 'b'。

範例 4
  輸入：s = "adceb", p = "*a*b"
  輸出：true
  說明：第一個 '*' 配空，第二個 '*' 配 "dce"。""",
 "constraints": [
   "0 ≤ <code>s.length</code>, <code>p.length</code> ≤ 2000",
   "<code>s</code> 只含小寫英文字母",
   "<code>p</code> 只含小寫英文字母、<code>'?'</code>、<code>'*'</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>長度到 2000</strong>（第 10 題只有 20）。"
       "O(m × n) = 4 × 10⁶ 沒問題，但如果寫成指數級的純遞迴就會 TLE。",
       "<strong>兩邊都可以是空字串</strong>。"
       "<code>(\"\", \"\")</code> → true；<code>(\"\", \"*\")</code> → true；"
       "<code>(\"a\", \"\")</code> → false。三種都要測。",
       "<strong>沒有「保證 * 前面有字元」這種限制</strong>（第 10 題有）。"
       "因為這題的 <code>'*'</code> 是獨立的，"
       "<code>\"*\"</code>、<code>\"**\"</code>、<code>\"*a*\"</code> 都是合法的 pattern。",
     ]),
   ]),
 ],
 "idea": [
   "兩條路：<strong>DP</strong>（穩、好推導、O(m·n) 空間）"
   "或<strong>貪婪 + 回溯</strong>（O(1) 空間，但要想清楚為什麼對）。",
 ],
 "approaches": [
   ap("解法一", "動態規劃（先確保會寫）", [
     ("c", S["p44_dp"]),
     ("h", "轉移式只有兩條"),
     ("c", """情況 A： p[j-1] == '*'

    dp[i][j] = dp[i][j-1]     '*' 配空字串（等於不用它）
             or dp[i-1][j]     '*' 再多吃一個 s[i-1]

    第二項的 j 不變 —— 因為 '*' 可以繼續吃，它還在。

情況 B： p[j-1] 是普通字元或 '?'

    dp[i][j] = dp[i-1][j-1]  且  p[j-1] 配得上 s[i-1]

    只有一條路，沒有分岔。

初始化：
    dp[0][0] = True
    dp[0][j] = dp[0][j-1]  若 p[j-1] == '*'
               False       否則

    「空字串只能被全是 * 的 pattern 匹配」

    p = "*a*"
      dp[0][0] = True
      dp[0][1] = dp[0][0] = True    （'*' 配空）
      dp[0][2] = False              （'a' 配不上空）
      dp[0][3] = False              （前面已經斷了）"""),
     ("h", "和第 10 題的 DP 比較"),
     ("c", """第 10 題（'*' 綁前一個字元）：
    dp[i][j] = dp[i][j-2]                        （'x*' 用 0 次）
             or (dp[i-1][j] and p[j-2] 配 s[i-1]) （'x*' 多吃一個）
    注意是 j-2（跳過 'x*' 兩格）

第 44 題（'*' 獨立）：
    dp[i][j] = dp[i][j-1]     （'*' 配空）
             or dp[i-1][j]     （'*' 多吃一個）
    是 j-1（只跳過 '*' 一格），而且沒有「配得上」的前提

少了那個前提，就是本題能用貪婪的根本原因。"""),
     "<strong>空間可以壓到 O(n)</strong>："
     "<code>dp[i][j]</code> 只依賴 <code>dp[i][j-1]</code>（同列）和 <code>dp[i-1][j]</code>（上一列），"
     "用一條長度 n+1 的陣列滾動即可。但既然有 O(1) 的解法（解法二），這個優化意義不大。",
   ], "O(m·n)", "O(m·n)（可壓到 O(n)）", "填滿 (m+1)×(n+1) 的表", "dp 表"),

   ap("解法二", "貪婪 + 回溯（O(1) 空間，最佳解）", [
     "核心策略：<strong>遇到 <code>'*'</code> 先讓它吃 0 個字元，繼續往下配；"
     "如果之後卡住了，就回到最後一個 <code>'*'</code>，讓它多吃一個，重來。</strong>",
     ("c", S["p44_greedy"]),
     ("fig", _P44_FIG, "0 0 640 318"),
     ("h", "為什麼「只回溯到最後一個 <code>*</code>」就夠了？"),
     ("c", """這是本題最需要想清楚的一點。

假設 p = "*a*b"，我們已經用第一個 * 配了某一段、
並且成功配上了 'a'，現在卡在 'b' 上。

問：需不需要回去讓「第一個 *」多吃一點？

答：不需要。

理由：
    設第一個 * 目前吃到 s[0..k]，然後 'a' 配上 s[k+1]。
    如果讓第一個 * 多吃一點，'a' 就要配 s[k+2] 之後的某個 'a'。

    但！第二個 * 可以配「任意一段」——
    它能吃掉的範圍，完全涵蓋了「第一個 * 多吃」所能達成的效果。

    換句話說：
        "* a * b" 中，第二個 * 的彈性已經包含了
        「a 出現在更後面」這種可能性嗎？

    不完全是 —— 但關鍵在於：
    我們是在「第二個 * 之後」卡住的，
    而第二個 * 可以無限往後吃，
    所以只要 s 的後面還有 'b'，第二個 * 一定能配上。

    如果 s 的後面完全沒有 'b'，那不管第一個 * 怎麼調整都沒用。

    所以：卡住時，只需要調整「離卡住位置最近的那個 *」。

嚴格的證明要用「交換論證」：
    如果存在一組成功的匹配，
    那麼一定存在一組「每個 * 都盡量少吃」的成功匹配，
    而貪婪演算法找到的就是那一組。"""),
     ("h", "四個分支，逐一對照"),
     ("c", """① p[j] 配得上 s[i]（字元相同或 '?'）
       -> 兩邊都前進

② p[j] 是 '*'
       -> 記下 star = j、match = i（先吃 0 個），只有 j 前進

③ 配不上，但前面有 * （star != -1）
       -> j 回到 star + 1，match += 1（* 多吃一個），i = match

④ 配不上，而且沒有 *
       -> 直接失敗

結束後的收尾：
    s 用完了，但 p 可能還剩東西。
    只有「剩下的全是 *」才算成功（* 可以配空）。
    p = "a*", s = "a"  ->  j 停在 1，剩下 '*'  ->  True ✔
    p = "ab", s = "a"  ->  j 停在 1，剩下 'b'  ->  False ✔"""),
     ("h", "複雜度"),
     "最壞情況是 O(m × n)（例如 <code>s = \"aaaa...a\"</code>、"
     "<code>p = \"*a*a*a*a\"</code>，每個 <code>*</code> 都要反覆回溯）。"
     "<strong>但實務上幾乎總是接近 O(m + n)</strong>，"
     "而且<strong>空間是 O(1)</strong> —— 這是它勝過 DP 的地方。",
     "<strong>這正是 shell 的 <code>fnmatch</code> 和 <code>glob</code> 用的演算法。</strong>",
   ], "O(m·n) 最壞，實務接近 O(m+n)", "O(1)",
      "只有病態 pattern 才會退化", "四個整數變數", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "好證明？", "備註"],
   [["一、DP", "O(m·n)", "O(m·n)→O(n)", "✔ 容易", "穩；面試先寫它"],
    ["二、貪婪 + 回溯", "O(m·n) 最壞", "O(1)", "✘ 要交換論證", "最優；shell 就用它"]]),
 "edges": [
   "<strong>兩邊都空</strong>：<code>(\"\", \"\")</code> → true。",
   "<strong>pattern 只有 <code>*</code></strong>：<code>(\"\", \"*\")</code>、<code>(\"\", \"***\")</code> → true。",
   "<strong>s 非空、p 空</strong>：<code>(\"a\", \"\")</code> → false。",
   "<strong>結尾的 <code>*</code></strong>：<code>(\"a\", \"a*\")</code> → true。收尾的 while 迴圈就是為它。",
   "<strong>連續多個 <code>*</code></strong>：<code>(\"abc\", \"*****a*****c\")</code> → true。"
   "貪婪版會反覆更新 <code>star</code>，但不影響正確性。",
   "<strong>需要回溯的情況</strong>：<code>(\"adceb\", \"*a*b\")</code> → true。",
   "<strong>貪婪的最壞情況</strong>：<code>(\"aaaa\", \"*a*a*a*a*\")</code> → true。"
   "會觸發大量回溯。",
   "<strong>只有 <code>?</code></strong>：<code>(\"abc\", \"???\")</code> → true；"
   "<code>(\"ab\", \"???\")</code> → false（<code>?</code> 不能配空）。",
 ],
 "follow": [
   ("h", "追問一：為什麼第 10 題不能用同樣的貪婪？"),
   "因為第 10 題的 <code>'*'</code> <strong>不能配任意字元</strong>，"
   "它只能配「前面那個字元」的重複。",
   ("c", """s = "aaa", p = "a*b*a"

第 44 題的貪婪思路（讓 * 盡量少吃，卡住再多吃）在這裡完全不成立，
因為 "a*" 只能吃 a，"b*" 只能吃 b。

而且「卡住時該調整哪個 *」也不明確 ——
可能要同時調整好幾個，那就是指數級的搜尋。

所以第 10 題只能 DP。""",),
   ("h", "追問二：這個演算法在真實世界的哪裡？"),
   ("ul", [
     "<strong>shell 的檔名展開</strong>：<code>ls *.txt</code>、<code>rm test_?.log</code>",
     "<strong>POSIX 的 <code>fnmatch(3)</code></strong>：本題的演算法就是它的簡化版",
     "<strong>.gitignore</strong>：也是萬用字元（加上 <code>**</code> 表示跨目錄）",
     "<strong>SQL 的 LIKE</strong>：<code>%</code> 對應 <code>*</code>，<code>_</code> 對應 <code>?</code>",
   ]),
   "<strong>萬用字元之所以在 shell 裡勝過 regex，就是因為它簡單、直覺、而且可以 O(1) 空間匹配。</strong>",
   ("h", "追問三：如果要支援 <code>[abc]</code> 這種字元集呢？"),
   "DP 版只要改「配不配得上」那一行的判斷即可，結構完全不變。"
   "貪婪版也一樣 —— <strong>因為 <code>[abc]</code> 和 <code>?</code> 一樣是「配一個」</strong>，"
   "不會影響 <code>*</code> 的回溯邏輯。"
   "這正是 <code>fnmatch</code> 實際支援的功能。",
   ("h", "追問四：如果 pattern 要重複用在很多字串上？"),
   "可以把 pattern <strong>預先正規化</strong>："
   "把連續的 <code>\"***\"</code> 壓成 <code>\"*\"</code>（語意完全相同），"
   "並且預先切成「被 <code>*</code> 分隔的片段」。"
   "之後每次匹配就變成「依序在 s 裡找這些片段」，"
   "第一段要在開頭、最後一段要在結尾、中間的貪婪往後找。"
   "<strong>這是 <code>fnmatch</code> 的實際實作方式，也能天然避開貪婪版的最壞情況。</strong>",
 ],
 "related": [
   "<strong>第 10 題 Regular Expression Matching</strong> —— <code>*</code> 語意不同的姊妹題",
   "<strong>第 72 題 Edit Distance</strong> —— 兩字串的二維 DP",
   "<strong>第 97 題 Interleaving String</strong> —— 同樣的 DP 骨架",
 ],
 "check": [
   "第 44 題的 <code>'*'</code> 和第 10 題的 <code>'*'</code> 差在哪？為什麼這個差別讓貪婪變得可行？",
   "貪婪版為什麼「只回溯到最後一個 <code>*</code>」就夠了？",
   "DP 的初始化 <code>dp[0][j] = dp[0][j-1]</code> 為什麼是 <code>j-1</code>（第 10 題是 <code>j-2</code>）？",
   "貪婪版最後那個 while 迴圈在處理什麼？拿掉的話哪一筆測資會錯？",
 ],
})
print("P44 written")

# ==================== 45. Jump Game II ====================
S["p45_dp"] = '''class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        INF = float("inf")
        dp = [INF] * n          # dp[i] = 跳到位置 i 最少要幾步
        dp[0] = 0

        for i in range(n):
            for j in range(i + 1, min(i + nums[i], n - 1) + 1):
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[n - 1]'''

S["p45_greedy"] = '''class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        cur_end = 0        # 目前這一步能到的最遠邊界
        farthest = 0       # 在目前這一步的範圍內，下一步最遠能到哪

        # 不看最後一格：走到那裡就結束了，不需要再跳
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == cur_end:          # 走到這一層的邊界了，必須再跳一步
                jumps += 1
                cur_end = farthest

        return jumps'''

S["p45_bfs"] = '''class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # 把它看成 BFS：第 k 層 = 「剛好 k 步能到的所有位置」
        level = 0
        left = right = 0          # 目前這一層的範圍 [left, right]

        while right < n - 1:
            level += 1
            nxt = max(i + nums[i] for i in range(left, right + 1))
            left, right = right + 1, nxt

        return level'''

_p45 = [S.load(k) for k in ("p45_dp", "p45_greedy", "p45_bfs")]


def _p45_ref(nums):
    n = len(nums)
    INF = float("inf")
    d = [INF] * n
    d[0] = 0
    for i in range(n):
        if d[i] == INF:
            continue
        for j in range(i + 1, min(i + nums[i], n - 1) + 1):
            d[j] = min(d[j], d[i] + 1)
    return d[n - 1]


for c in [[2, 3, 1, 1, 4], [2, 3, 0, 1, 4], [1], [1, 2], [2, 1], [1, 1, 1, 1],
          [5, 1, 1, 1, 1], [3, 2, 1, 0, 4][:1]]:
    e = _p45_ref(c)
    for sol in _p45:
        assert sol.jump(list(c)) == e, ("P45", c, sol, sol.jump(list(c)), e)
for _ in range(4000):
    n = random.randint(1, 9)
    # 保證一定跳得到終點
    c = [random.randint(1, 4) for _ in range(n)]
    e = _p45_ref(c)
    for sol in _p45:
        assert sol.jump(list(c)) == e, ("P45", c, sol, sol.jump(list(c)), e)
print("P45 solutions OK")

_P45_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">nums = [2, 3, 1, 1, 4]，把它看成一層一層的 BFS</text>
            <g font-size="14" text-anchor="middle">
              <rect x="60" y="48" width="64" height="38" rx="6" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="92" y="73" fill="var(--gold)">2</text>
              <rect x="152" y="48" width="64" height="38" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="184" y="73" fill="var(--accent)">3</text>
              <rect x="244" y="48" width="64" height="38" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="276" y="73" fill="var(--accent)">1</text>
              <rect x="336" y="48" width="64" height="38" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="368" y="73" fill="#ff8a65">1</text>
              <rect x="428" y="48" width="64" height="38" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="460" y="73" fill="#ff8a65">4</text>
            </g>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="92" y="102">0</text><text x="184" y="102">1</text><text x="276" y="102">2</text>
              <text x="368" y="102">3</text><text x="460" y="102">4</text>
            </g>
            <text x="540" y="73" fill="var(--text-muted)" font-size="12">← 終點</text>
            <line x1="20" y1="122" x2="620" y2="122" stroke="var(--border)"/>
            <g font-size="12">
              <text x="40" y="150" fill="var(--gold)">第 0 層（0 步可達）：{0}</text>
              <text x="340" y="150" fill="var(--text-muted)">從 0 最遠能到 0 + 2 = 2</text>
              <text x="40" y="180" fill="var(--accent)">第 1 層（1 步可達）：{1, 2}</text>
              <text x="340" y="180" fill="var(--text-muted)">最遠 max(1+3, 2+1) = 4</text>
              <text x="40" y="210" fill="#ff8a65">第 2 層（2 步可達）：{3, 4}</text>
              <text x="340" y="210" fill="#ff8a65">4 就是終點 → 答案 2</text>
            </g>
            <text x="20" y="250" fill="var(--gold)" font-size="12">貪婪版的 cur_end 就是「這一層的右邊界」，farthest 就是「下一層的右邊界」。</text>
            <text x="20" y="274" fill="var(--text-muted)" font-size="12">走到 cur_end 時就代表這一層走完了，jumps += 1，進入下一層 —— 這就是 BFS 的層數。</text>'''

emit({
 "num": 45, "slug": "jump-game-ii",
 "en": [
   "You are given a <code>0</code>-indexed array of integers <code>nums</code> of length "
   "<code>n</code>. You are initially positioned at <code>nums[0]</code>.",
   "Each element <code>nums[i]</code> represents the maximum length of a forward jump from "
   "index <code>i</code>.",
   "Return the <strong>minimum</strong> number of jumps to reach <code>nums[n - 1]</code>. "
   "The test cases are generated such that you can reach <code>nums[n - 1]</code>.",
 ],
 "zh": [
   "給你一個長度為 <code>n</code> 的整數陣列 <code>nums</code>，你一開始站在索引 0。",
   "<code>nums[i]</code> 表示從索引 <code>i</code> 出發<strong>最多</strong>能往前跳幾格"
   "（也就是可以跳 1 到 <code>nums[i]</code> 格）。",
   "回傳到達最後一格所需的<strong>最少跳躍次數</strong>。"
   "題目保證<strong>一定到得了</strong>。",
 ],
 "pre": [
   ("note", "把它看成 BFS，一切就清楚了", [
     ("c", """把每個位置當成一個節點，「一步能跳到」當成一條邊。
求「最少幾步」= 求無權圖的最短路徑 = BFS。

而 BFS 的「層」在這題有一個特別漂亮的性質：

    第 k 層 = 「剛好 k 步能到達的所有位置」
            = 一段「連續的區間」！

為什麼是連續的？
    因為從位置 i 可以跳 1..nums[i] 格（不是只能跳 nums[i] 格），
    所以第 k 層能到的位置是 [上一層的右邊界+1, 這一層能到的最遠處]。

    既然每一層都是一個區間，
    我們就不需要真的維護一個佇列 ——
    只要記住「這一層的右邊界」和「下一層的右邊界」就夠了。

    O(n) 空間的 BFS 變成 O(1) 空間的雙變數掃描。

nums = [2, 3, 1, 1, 4]
    第 0 層： [0, 0]        最遠能到 0+2 = 2
    第 1 層： [1, 2]        最遠 max(1+3, 2+1) = 4
    第 2 層： [3, 4]        含終點 4  ->  答案 2"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [2,3,1,1,4]
  輸出：2
  說明：從索引 0 跳 1 步到索引 1，再從索引 1 跳 3 步到索引 4。

範例 2
  輸入：nums = [2,3,0,1,4]
  輸出：2""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁴",
   "0 ≤ <code>nums[i]</code> ≤ 1000",
   "<strong>保證一定能到達 <code>nums[n-1]</code></strong>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>保證一定到得了</strong> —— 所以不用回傳 −1，也不用處理「卡住」的情況。"
       "（「會不會卡住」是第 55 題 Jump Game。）",
       "<strong>n 到 10⁴</strong>。O(n²) 是 10⁸ —— 在 Python 裡會 TLE。"
       "所以要 O(n)。",
       "<strong><code>nums[i]</code> 可以是 0</strong>，"
       "但因為保證到得了，0 只會出現在「不需要經過」的位置，或最後一格。",
       "<strong>n 可以是 1</strong>：起點就是終點，答案 0。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P45_FIG, "0 0 640 286"),
 ],
 "approaches": [
   ap("解法一", "動態規劃（會 TLE 的基準線）", [
     ("c", S["p45_dp"]),
     "<code>dp[j] = min(dp[j], dp[i] + 1)</code> —— 標準的最短路徑 DP。",
     "<strong>但它是 O(n²)</strong>：最壞情況（每個 <code>nums[i]</code> 都很大）"
     "內層迴圈要跑 O(n) 次。n = 10⁴ 時是 10⁸ —— TLE。",
     "它的價值是<strong>絕對正確</strong>，可以拿來驗證後面的貪婪解。"
     "（本篇的壓力測試就是拿它當基準。）",
   ], "O(n²)", "O(n)", "每個位置往後更新 O(n) 格", "dp 陣列"),

   ap("解法二", "貪婪 / 隱式 BFS（標準解）", [
     ("c", S["p45_greedy"]),
     ("h", "三個變數的意義"),
     ("c", """jumps     已經跳了幾步（= BFS 的層數）
cur_end   「目前這一層」能到的最右邊界
farthest  「掃過目前這一層的所有位置後」，下一層能到的最右邊界

演算法：
    一路往右走，沿途更新 farthest。
    一旦走到 cur_end（這一層的邊界），
    就表示「這一層走完了」，必須再跳一步進入下一層。

nums = [2, 3, 1, 1, 4]

  i=0: farthest = max(0, 0+2) = 2
       i == cur_end(0)  ->  jumps=1, cur_end=2
  i=1: farthest = max(2, 1+3) = 4
       i(1) != cur_end(2)
  i=2: farthest = max(4, 2+1) = 4
       i == cur_end(2)  ->  jumps=2, cur_end=4
  i=3: 迴圈到 n-1=4 就停（range(4) = 0,1,2,3）

  回傳 2 ✔"""),
     ("h", "為什麼迴圈是 <code>range(n - 1)</code> 而不是 <code>range(n)</code>？"),
     ("c", """因為走到最後一格就結束了，不需要「從最後一格再跳」。

如果寫成 range(n)：
    nums = [1, 1]
    i=0: farthest=1, i==cur_end(0) -> jumps=1, cur_end=1
    i=1: farthest=2, i==cur_end(1) -> jumps=2  ✘ 多算一步

    正確答案是 1（從 0 跳到 1）。

一句話：最後一格是「終點」不是「跳板」。

同理，n == 1 時 range(0) 是空的，直接回 0 ✔"""),
     ("h", "為什麼貪婪是對的？"),
     ("c", """貪婪的策略是：「在這一層的範圍內，選能跳最遠的那個位置」。

為什麼不會錯過更好的解？

    設第 k 層能到的範圍是 [L_k, R_k]。
    這是「恰好 k 步能到的所有位置」（而且是連續的）。

    第 k+1 層能到的最遠處 = max(i + nums[i])，i 在 [L_k, R_k] 裡。

    關鍵：任何「k+1 步能到的位置」，
          都必須先在 k 步內到達某個 i，再從 i 跳過去。
          所以 R_{k+1} 就是上面那個 max —— 沒有更好的了。

    而因為每一層都是連續區間，
    「到達第 j 格的最少步數」就是「j 落在第幾層」。

這其實不是「貪婪的啟發式」，而是「BFS 的正確性」——
BFS 保證第一次訪問到某個節點時，走的就是最短路徑。

所以這個解法既可以說是貪婪，也可以說是 BFS。
兩種說法都對，只是視角不同。"""),
   ], "O(n)", "O(1)", "掃一遍", "三個變數", optimal=True),

   ap("解法三", "顯式寫出 BFS 的層（最能看出結構）", [
     "把「層」明確地寫出來，讓 BFS 的結構一目了然。",
     ("c", S["p45_bfs"]),
     ("c", """nums = [2, 3, 1, 1, 4]，n = 5

  初始： left=0, right=0, level=0
  right(0) < 4  ->
      level=1
      nxt = max(i + nums[i] for i in [0,0]) = 0+2 = 2
      left, right = 1, 2
  right(2) < 4  ->
      level=2
      nxt = max(1+3, 2+1) = 4
      left, right = 3, 4
  right(4) == 4  ->  迴圈結束

  回傳 2 ✔"""),
     "<strong>和解法二完全等價</strong>，只是把「層」寫成明確的 <code>[left, right]</code>，"
     "而不是隱含在 <code>cur_end</code> 裡。",
     "<strong>優點</strong>：結構最清楚，一眼就看得出這是 BFS。"
     "<strong>缺點</strong>：每一層要重新掃一次 <code>range(left, right+1)</code>，"
     "雖然總和還是 O(n)（每個位置只屬於一層），但常數稍大。",
     "<strong>面試時的建議</strong>：先用這個版本講清楚「為什麼是 BFS」，"
     "再說「可以壓成兩個變數」，然後寫解法二。",
   ], "O(n)", "O(1)", "每個位置恰好屬於一層", "幾個變數"),
 ],
 "compare": (["解法", "時間", "空間", "n=10⁴ 能過？", "視角"],
   [["一、DP", "O(n²)", "O(n)", "✘", "最短路徑 DP"],
    ["二、貪婪掃描", "O(n)", "O(1)", "✔", "貪婪 / 隱式 BFS"],
    ["三、顯式分層", "O(n)", "O(1)", "✔", "BFS，結構最清楚"]]),
 "edges": [
   "<strong>只有一格</strong>：<code>[1]</code> → 0。起點就是終點。<code>range(0)</code> 是空的。",
   "<strong>兩格</strong>：<code>[1,2]</code> → 1；<code>[2,1]</code> → 1。",
   "<strong>一步到底</strong>：<code>[5,1,1,1,1]</code> → 1。",
   "<strong>每次只能跳一格</strong>：<code>[1,1,1,1]</code> → 3。",
   "<strong>中間有 0 但可以跨過</strong>：<code>[2,3,0,1,4]</code> → 2。",
   "<strong>迴圈寫成 <code>range(n)</code></strong>："
   "<code>[1,1]</code> 會回傳 2 而不是 1。<strong>這是本題第一名的 off-by-one。</strong>",
   "<strong>nums[i] 超出陣列</strong>：<code>[100, 1]</code> → 1。"
   "<code>farthest</code> 可能超過 <code>n-1</code>，不影響正確性。",
 ],
 "follow": [
   ("h", "追問一：如果不保證到得了呢？"),
   "那是第 55 題（Jump Game），問「能不能到」。"
   "同樣的貪婪，只是條件變成：<strong>如果 <code>i &gt; farthest</code> 就表示卡住了</strong>。",
   ("c", """class Solution:
    def canJump(self, nums):
        farthest = 0
        for i, v in enumerate(nums):
            if i > farthest:      # 連這一格都到不了
                return False
            farthest = max(farthest, i + v)
        return True

如果本題也要處理「到不了」，
就在解法二的迴圈裡加上 if i > cur_end: return -1。""",),
   ("h", "追問二：如果每一步的成本不同（不是都算 1 步）呢？"),
   "那就不能用 BFS 了（BFS 只對無權圖有效），"
   "要改用 <strong>Dijkstra</strong>（O(n log n)）或 DP。"
   "<strong>「所有邊的權重都一樣」正是 BFS 能用的前提</strong>，"
   "也是這題能做到 O(n) 的根本原因。",
   ("h", "追問三：如果可以往回跳呢？"),
   "第 1345 題（Jump Game IV）是這類問題的一般化 —— "
   "可以往前一格、往後一格、或跳到任何「數值相同」的格子。"
   "那題就必須寫真正的 BFS（用佇列），"
   "因為「可達範圍」不再是連續區間了。"
   "<strong>「層是連續區間」這個性質，是本題能省掉佇列的關鍵。</strong>",
   ("h", "追問四：如果要回傳「實際的跳躍路徑」呢？"),
   "在更新 <code>farthest</code> 時一併記下「是從哪個位置達成的」，"
   "然後每次 <code>jumps += 1</code> 時把那個位置記進路徑。"
   "複雜度不變，空間變 O(答案長度)。",
 ],
 "related": [
   "<strong>第 55 題 Jump Game</strong> —— 只問「能不能到」",
   "<strong>第 1306 題 Jump Game III</strong> —— 可以往回跳，要真的 BFS",
   "<strong>第 1345 題 Jump Game IV</strong> —— 加上「跳到相同值」的邊",
   "<strong>第 134 題 Gas Station</strong> —— 另一個「貪婪 + 掃一遍」的經典",
 ],
 "check": [
   "為什麼迴圈是 <code>range(n-1)</code>？用 <code>[1,1]</code> 說明寫成 <code>range(n)</code> 會錯在哪。",
   "<code>cur_end</code> 和 <code>farthest</code> 分別對應 BFS 的什麼？",
   "為什麼「k 步能到的位置」一定是一段連續區間？這個性質依賴題目的哪一句話？",
   "如果每一步的成本不同，為什麼就不能用這個解法了？",
 ],
})
print("P45 written")
