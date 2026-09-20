# -*- coding: utf-8 -*-
"""第 131–135 題。"""
import random, itertools
from collections import deque
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(131)

# ==================== 131. Palindrome Partitioning ====================
S["p131"] = '''class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # 先預處理：pal[i][j] = s[i..j] 是不是回文
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):          # i 由大到小，才能用到 pal[i+1][j-1]
            for j in range(i, n):
                pal[i][j] = s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1])

        res, path = [], []

        def back(start: int):
            if start == n:
                res.append(path[:])             # 切完了，收下這一組
                return
            for end in range(start, n):
                if pal[start][end]:             # s[start..end] 是回文才切
                    path.append(s[start:end + 1])
                    back(end + 1)
                    path.pop()

        back(0)
        return res'''

S["p131_nopre"] = '''class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res, path = [], []

        def back(start: int):
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                piece = s[start:end + 1]
                if piece == piece[::-1]:        # 每次現場檢查，O(k)
                    path.append(piece)
                    back(end + 1)
                    path.pop()

        back(0)
        return res'''

S["p131_memo"] = '''from functools import lru_cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        @lru_cache(maxsize=None)
        def go(start: int):
            """s[start:] 的所有回文分割方式"""
            if start == n:
                return [[]]                     # 空字串：恰好一種分法（什麼都不切）
            out = []
            for end in range(start, n):
                piece = s[start:end + 1]
                if piece == piece[::-1]:
                    for rest in go(end + 1):
                        out.append([piece] + rest)
            return out

        ans = [list(x) for x in go(0)]
        go.cache_clear()
        return ans'''


def _p131_ref(s):
    """獨立參考解：枚舉所有「在哪些位置切一刀」的組合。"""
    n = len(s)
    out = []
    for mask in range(1 << max(0, n - 1)):
        parts, prev = [], 0
        for i in range(n - 1):
            if mask >> i & 1:
                parts.append(s[prev:i + 1]); prev = i + 1
        parts.append(s[prev:])
        if all(p == p[::-1] for p in parts):
            out.append(parts)
    return out


def _norm(x):
    return sorted(tuple(p) for p in x)


_p131 = [S.load(k) for k in ("p131", "p131_nopre", "p131_memo")]

for s, want in [
    ("aab", [["a", "a", "b"], ["aa", "b"]]),
    ("a", [["a"]]),
    ("ab", [["a", "b"]]),
]:
    assert _norm(_p131_ref(s)) == _norm(want), ("P131 ref", s)
    for sol in _p131:
        assert _norm(sol.partition(s)) == _norm(want), ("P131", s, sol)

for _ in range(2500):
    s = "".join(random.choice("ab") for _ in range(random.randrange(1, 11)))
    want = _norm(_p131_ref(s))
    for sol in _p131:
        assert _norm(sol.partition(s)) == want, ("P131 random", s, sol)
print("P131 solutions OK")

_P131_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">回溯樹：在每個位置問「從這裡開始，切多長的一段？」只有切出回文才往下走。</text>
            <text x="20" y="48" fill="var(--gold)" font-size="13">s = &quot;aab&quot;</text>
            <g font-size="12" text-anchor="middle">
              <rect x="256" y="66" width="128" height="26" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="320" y="84" fill="var(--gold)">start = 0，path = []</text>
              <rect x="86" y="146" width="150" height="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="161" y="164" fill="var(--accent)">切 &quot;a&quot; → path=[a]</text>
              <rect x="278" y="146" width="160" height="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="358" y="164" fill="var(--accent)">切 &quot;aa&quot; → path=[aa]</text>
              <rect x="470" y="146" width="150" height="26" fill="none" stroke="var(--border)"/><text x="545" y="164" fill="var(--text-muted)">切 &quot;aab&quot; ✘ 不是回文</text>
              <rect x="40" y="224" width="160" height="26" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="120" y="242" fill="var(--accent)">切 &quot;a&quot; → [a, a]</text>
              <rect x="212" y="224" width="150" height="26" fill="none" stroke="var(--border)"/><text x="287" y="242" fill="var(--text-muted)">切 &quot;ab&quot; ✘</text>
              <rect x="386" y="224" width="170" height="26" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="471" y="242" fill="var(--gold)">切 &quot;b&quot; → [aa, b] ✔ 收</text>
              <rect x="20" y="302" width="200" height="26" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="120" y="320" fill="var(--gold)">切 &quot;b&quot; → [a, a, b] ✔ 收</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="290" y1="92" x2="180" y2="140"/><line x1="320" y1="92" x2="350" y2="140"/><line x1="350" y1="92" x2="530" y2="140"/>
              <line x1="140" y1="172" x2="115" y2="218"/><line x1="180" y1="172" x2="280" y2="218"/>
              <line x1="358" y1="172" x2="440" y2="218"/>
              <line x1="115" y1="250" x2="115" y2="296"/>
            </g>
            <line x1="20" y1="346" x2="620" y2="346" stroke="var(--border)"/>
            <text x="20" y="374" fill="var(--accent)" font-size="12">回溯三部曲：path.append(piece) → back(end+1) → path.pop()。</text>
            <text x="20" y="400" fill="#ff8a65" font-size="12">收集時一定要 path[:]（複製快照）—— 和第 113 題完全同一個坑。</text>
            <text x="20" y="430" fill="var(--gold)" font-size="12">預處理 pal[i][j] 把「檢查是不是回文」從 O(k) 降到 O(1)：</text>
            <text x="40" y="456" fill="var(--text-muted)" font-size="12">pal[i][j] = (s[i] == s[j]) and (長度 &lt; 3 或 pal[i+1][j-1])　—— i 要【由大到小】算。</text>'''

emit({
 "num": 131, "slug": "palindrome-partitioning",
 "en": [
   "Given a string <code>s</code>, partition <code>s</code> such that every "
   "substring of the partition is a <strong>palindrome</strong>. Return <em>all possible "
   "palindrome partitioning of </em><code>s</code>.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，把它切成若干段，"
   "使得<strong>每一段都是回文</strong>。",
   "回傳<strong>所有可能的切法</strong>。",
 ],
 "pre": [
   ("note", "又是回溯：這次「選擇」是「切多長」", [
     ("c", """回溯的骨架（第 113 題那個）：

    def back(狀態):
        if 完成: 收下答案的【複製】; return
        for 每個選擇:
            做選擇
            back(新狀態)
            撤銷選擇

【這題的「選擇」是什麼？】

    站在位置 start，決定「第一段要切到哪裡」：

        end = start, start+1, ..., n-1

    但只有「s[start..end] 是回文」時才是合法的選擇。

    切完之後，剩下的 s[end+1:] 是同一個子問題 -> 遞迴。

【終止條件】：start == n（整個字串都切完了）

【複雜度】：

    最壞情況 s = "aaaa...a"（n 個 a）：
        每個位置都可以切或不切 -> 2^(n-1) 種分法

        n = 16 -> 32768 種

    每種分法要複製一條長度最多 n 的路徑
    -> O(n · 2^n)

    【這是「輸出敏感」的下界 —— 答案本身就這麼多，
      不可能更快。】

    題目限制 n <= 16 就是為了讓 2^16 可以接受。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "aab"
  輸出：[["a","a","b"],["aa","b"]]
  說明：切法 "a|a|b" 和 "aa|b" 的每一段都是回文。
        "aab" 整個不是回文，"a|ab" 的 "ab" 也不是。

範例 2
  輸入：s = "a"
  輸出：[["a"]]""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 16",
   "<code>s</code> 只包含小寫英文字母",
 ],
 "mid": [
   ("note", "n ≤ 16 這個上限在說什麼", [
     "<strong>2¹⁶ = 65536</strong> —— 這正好是「全部切法」的數量上界。",
     "<strong>所以題目在告訴你：「就是要你枚舉全部，不用想更聰明的辦法」。</strong>",
     "<strong>看到很小的上限（n ≤ 16、20、25），"
     "通常就是「指數級演算法是預期解」的訊號。</strong>",
   ]),
 ],
 "idea": [
   ("fig", _P131_FIG, "0 0 640 474"),
   ("c", """回溯 + 回文檢查。

【核心迴圈】：

    for end in range(start, n):
        if s[start..end] 是回文:
            path.append(s[start:end+1])
            back(end + 1)
            path.pop()

【★ 優化：預處理回文表】

    每次現場檢查 piece == piece[::-1] 是 O(k)。
    在回溯樹上會被重複檢查很多次。

    改成預處理一張 pal[i][j]：

        pal[i][j] = (s[i] == s[j]) and (j - i < 2 or pal[i+1][j-1])

        意思是：頭尾相同，而且【去掉頭尾之後】還是回文。
        長度 1 或 2 時（j - i < 2）不用看內部。

    【★ i 必須由大到小算】

        因為 pal[i][j] 依賴 pal[i+1][j-1] ——
        那是「更下面一列」的值。

        i 由大到小 -> 算 pal[i][*] 時 pal[i+1][*] 已經算好了 ✔

        寫成 i 由小到大會用到還沒算的值（全是 False）-> 答案錯。

    預處理 O(n²)，之後每次檢查 O(1)。

【這個「先建回文表、再做別的事」的兩階段結構，
  在第 132 題（最少切幾刀）也會用到。】"""),
 ],
 "approaches": [
   ap("解法一", "回溯 + 預處理回文表（標準答案）", [
     ("c", S["p131"]),
     ("h", "回文表的建法要看清楚"),
     ("c", """for i in range(n - 1, -1, -1):      ★ i 由大到小
    for j in range(i, n):           j 從 i 開始（只填上三角）
        pal[i][j] = s[i] == s[j] and (j - i < 2 or pal[i+1][j-1])

驗算 s = "aab"：

    i=2: pal[2][2] = (b==b) and (0 < 2) = True
    i=1: pal[1][1] = True
         pal[1][2] = (a==b) = False
    i=0: pal[0][0] = True
         pal[0][1] = (a==a) and (1 < 2) = True     ← "aa" ✔
         pal[0][2] = (a==b) = False                 ← "aab" ✘

    所以從位置 0 可以切 "a"（pal[0][0]）或 "aa"（pal[0][1]）✔

【j - i < 2 這個條件在說什麼？】

    j - i == 0 -> 長度 1，一定是回文
    j - i == 1 -> 長度 2，只要兩個字一樣就是回文
    j - i >= 2 -> 要看去掉頭尾之後 pal[i+1][j-1]

    寫成 j - i < 2 把前兩種情況合併了 ——
    也可以寫成 j <= i + 1，一樣的意思。""",),
     ("h", "回溯的兩個必做動作"),
     "<strong>① <code>res.append(path[:])</code></strong> —— "
     "<strong>忘了 <code>[:]</code> 會得到一堆空 list（和第 113 題同一個坑）。</strong>",
     "<strong>② <code>path.pop()</code></strong> —— "
     "<strong>忘了會讓路徑越積越長。</strong>",
     "<strong>時間 O(n · 2ⁿ)、空間 O(n²)（回文表）+ O(n)（路徑）。</strong>",
   ], "O(n · 2ⁿ)", "O(n²)", "答案本身就這麼多", "回文表 + 路徑", optimal=True),

   ap("解法二", "回溯 + 現場檢查（不預處理）", [
     ("c", S["p131_nopre"]),
     ("c", """少了預處理，程式碼短了六行。

【複雜度差多少？】

    現場檢查一段長度 k 的子字串是 O(k)。

    回溯樹上總共檢查 O(2^n) 次，每次平均 O(n)
    -> O(n · 2^n) 的檢查成本

    加上複製路徑的 O(n · 2^n)
    -> 總共還是 O(n · 2^n)

    【漸進複雜度【沒有變】！】

    因為「複製答案」那一項本來就是 O(n · 2^n)，
    檢查回文的成本被它吸收了。

【所以預處理值得嗎？】

    ✔ 常數會小一些（特別是 s 裡回文很少時，
       預處理能讓大量分支被立刻剪掉）
    ✘ 多了 O(n²) 空間和六行程式碼

    n = 16 時差異不大。

    【但預處理的真正價值在第 132 題】——
    那題只要「最少切幾刀」，沒有指數級的輸出，
    回文檢查就成了瓶頸，預處理是必要的。

【面試時】：
    先寫這個版本（短、清楚），
    然後說「可以預處理回文表把檢查降到 O(1)，
    在下一題（132）那會是關鍵」。"""),
   ], "O(n · 2ⁿ)", "O(n)", "漸進上和解法一相同", "只有路徑"),

   ap("解法三", "記憶化遞迴（回傳「所有分法」）", [
     ("c", S["p131_memo"]),
     ("h", "和回溯的差別：這個版本「回傳答案」而不是「累積答案」"),
     ("c", """go(start) 回傳「s[start:] 的所有分法」。

    base case：go(n) = [[]]
        —— 空字串有【一種】分法（什麼都不切），
           而不是【零種】。

        寫成 [] 的話，所有答案都會是空的 ✘
        （和第 95 題 base case 要回 [None] 是同一個道理。）

【記憶化有用嗎？】

    有，但效果有限：

        go(start) 只有 n 個不同的參數 -> 最多算 n 次 ✔

    但它回傳的 list 大小本身就是指數級的，
    而且外層還要做 [piece] + rest（複製）。

    所以【總時間還是 O(n · 2^n)】——
    記憶化省下的是「重複的遞迴」，
    不是「重複的複製」。

【什麼時候記憶化真的有用？】

    當「子問題的答案很小」而「重複次數很多」時。

    這題的子問題答案是指數級的 -> 記憶化的收益被淹沒。
    第 132 題（只要一個數字）-> 記憶化效果顯著 ✔

    【這是一個很好的對照：
      同樣的子問題結構，「要全部解」和「要最優解」
      的最佳策略完全不同。】"""),
     "<strong>注意回傳時要 <code>[list(x) for x in go(0)]</code></strong> —— "
     "<strong>因為 <code>lru_cache</code> 存的是同一份 list，"
     "直接回傳的話呼叫者改動它會污染快取。</strong>",
   ], "O(n · 2ⁿ)", "O(n · 2ⁿ)", "記憶化省不了複製", "快取所有分法"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、回溯 + 回文表", "O(n·2ⁿ)", "O(n²)", "20", "標準答案"],
    ["二、回溯 + 現場檢查", "O(n·2ⁿ)", "O(n)", "14", "最短，漸進相同"],
    ["三、記憶化遞迴", "O(n·2ⁿ)", "O(n·2ⁿ)", "18", "記憶化收益有限"]]),
 "edges": [
   "<strong>單一字元</strong> <code>\"a\"</code> → <code>[[\"a\"]]</code>。",
   "<strong>沒有任何多字元回文</strong> <code>\"ab\"</code> → <code>[[\"a\",\"b\"]]</code>"
   "（每個字元自己切一段，永遠是合法答案）。",
   "<strong>全部相同</strong> <code>\"aaaa\"</code> → <strong>8 種分法（2³）</strong>。"
   "<strong>這是最壞情況。</strong>",
   "<strong>整個就是回文</strong> <code>\"aba\"</code> → "
   "<code>[[\"a\",\"b\",\"a\"], [\"aba\"]]</code>。",
   "<strong>忘了 <code>path[:]</code></strong> → 全是空 list。",
   "<strong>忘了 <code>path.pop()</code></strong> → 路徑越積越長。",
   "<strong>回文表的 <code>i</code> 由小到大算</strong> → "
   "<strong>用到還沒算的 <code>pal[i+1][j-1]</code>（全 False），長度 ≥ 3 的回文全都漏掉。</strong>",
   "<strong>記憶化版 base case 寫成 <code>[]</code></strong> → 答案全空。",
   "<strong>n = 16 全是相同字元</strong> → 32768 種分法，每種最多 16 段。",
 ],
 "follow": [
   ("h", "追問一：如果只要「最少切幾刀」呢？"),
   "<strong>第 132 題</strong>。那題<strong>不需要枚舉所有分法</strong> —— "
   "<strong>用 DP，<code>O(n²)</code> 就能解，而且 <code>n</code> 可以到 2000。</strong>",
   ("c", """dp[i] = s[0..i] 最少要切幾刀

    dp[i] = min over j: pal[j][i] 時的 dp[j-1] + 1

【「要全部解」vs「要最優解」的複雜度差距】：

    131（全部分法）：O(n · 2^n)，n <= 16
    132（最少刀數）：O(n²)，     n <= 2000

    差了天文數字。

    【這個對比在第 95/96 題（生成 BST vs 數 BST）
      也出現過，是很重要的一課：

      「列出來」和「算出最優的那一個」
      往往是完全不同難度的問題。】""",),
   ("h", "追問二：預處理回文表還有別的做法嗎？"),
   ("c", """(a) 區間 DP（本文用的）：O(n²) 時間、O(n²) 空間

(b) 中心擴展：對每個「中心」往兩邊擴
    for center in range(2n - 1):
        l = center // 2; r = l + center % 2
        while l >= 0 and r < n and s[l] == s[r]:
            pal[l][r] = True; l -= 1; r += 1

    同樣 O(n²) 時間，但常數更小，
    而且【不需要按特定順序算】—— 比較不容易寫錯。

(c) Manacher 演算法：O(n) 找出所有回文半徑

    但它只給「以每個中心的最長回文半徑」，
    要轉成 pal[i][j] 還是 O(n²)。

    對這題沒有幫助（因為輸出本來就是指數級的）。

【第 5 題（最長回文子字串）會把 (b) 和 (c) 講透。】""",),
   ("h", "追問三：如果要求「每段長度都至少 2」呢？"),
   "<strong>把 <code>for end in range(start, n)</code> 改成 "
   "<code>range(start + 1, n)</code></strong>。",
   "<strong>但要注意：這樣可能一種分法都沒有</strong>"
   "（例如 <code>\"ab\"</code>），答案就是 <code>[]</code>。"
   "<strong>原本「每個字元自己一段」這個保底答案消失了 —— "
   "加限制時要想想「還有沒有解」。</strong>",
   ("h", "追問四：如果 <code>s</code> 很長（例如 10⁵）但只要「有沒有一種分法」呢？"),
   "<strong>那答案永遠是「有」</strong> —— <strong>每個字元自己切一段即可。</strong>",
   "<strong>這個「保底答案」的存在，正是為什麼第 132 題的答案上界是 <code>n-1</code> 刀。</strong>"
   "<strong>先找出「一定存在的那個解」，常常能幫你確定答案的範圍。</strong>",
 ],
 "related": [
   "<strong>第 132 題 Palindrome Partitioning II</strong> —— 只要最少刀數，DP",
   "<strong>第 5 題 Longest Palindromic Substring</strong> —— 回文表 / 中心擴展",
   "<strong>第 113 題 Path Sum II</strong> —— 同一個回溯骨架",
   "<strong>第 93 題 Restore IP Addresses</strong> —— 同樣是「切成幾段」的回溯",
   "<strong>第 139/140 題 Word Break I/II</strong> —— 同樣的「切字串」結構",
 ],
 "check": [
   "回溯的「選擇」在這題是什麼？終止條件是什麼？",
   "回文表的 <code>i</code> 為什麼要由大到小算？由小到大會漏掉什麼？",
   "預處理回文表有沒有改變漸進複雜度？為什麼？",
   "為什麼「要全部分法」是 O(n·2ⁿ) 而「要最少刀數」只要 O(n²)？",
 ],
})
print("P131 written")

# ==================== 132. Palindrome Partitioning II ====================
S["p132_dp"] = '''class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # pal[i][j] = s[i..j] 是不是回文
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                pal[i][j] = s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1])

        # dp[i] = s[0..i] 最少要切幾刀
        dp = [0] * n
        for i in range(n):
            if pal[0][i]:
                dp[i] = 0                   # 整段就是回文，不用切
            else:
                dp[i] = min(dp[j - 1] + 1 for j in range(1, i + 1) if pal[j][i])

        return dp[n - 1]'''

S["p132_center"] = '''class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # dp[i] = s[0..i-1] 最少切幾刀（用 1-indexed 比較好寫）
        dp = list(range(-1, n))             # dp[0] = -1，dp[i] 上界是 i-1 刀

        for center in range(n):
            # 奇數長度的回文：以 s[center] 為中心
            l = r = center
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1
            # 偶數長度的回文：以 s[center], s[center+1] 之間為中心
            l, r = center, center + 1
            while l >= 0 and r < n and s[l] == s[r]:
                dp[r + 1] = min(dp[r + 1], dp[l] + 1)
                l -= 1
                r += 1

        return dp[n]'''


def _p132_ref(s):
    """獨立參考解：最樸素的 O(n³) DP，回文每次現場檢查。"""
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = -1
    for i in range(1, n + 1):
        best = i - 1
        for j in range(i):
            t = s[j:i]
            if t == t[::-1]:
                best = min(best, dp[j] + 1)
        dp[i] = best
    return dp[n]


_p132 = [S.load(k) for k in ("p132_dp", "p132_center")]

for s, want in [
    ("aab", 1),
    ("a", 0),
    ("ab", 1),
    ("abccba", 0),
    ("aabbc", 2),
    ("cdd", 1),
]:
    assert _p132_ref(s) == want, ("P132 ref", s, _p132_ref(s))
    for sol in _p132:
        assert sol.minCut(s) == want, ("P132", s, sol)

for _ in range(4000):
    s = "".join(random.choice("abc") for _ in range(random.randrange(1, 15)))
    want = _p132_ref(s)
    for sol in _p132:
        assert sol.minCut(s) == want, ("P132 random", s, want, sol)
# 和第 131 題交叉驗證：最少刀數 = 最短分法的段數 - 1
_p131sol = S.load("p131")
for _ in range(400):
    s = "".join(random.choice("ab") for _ in range(random.randrange(1, 10)))
    want = min(len(p) for p in _p131sol.partition(s)) - 1
    for sol in _p132:
        assert sol.minCut(s) == want, ("P132 vs P131", s, want, sol)
print("P132 solutions OK")

_P132_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">只要「最少刀數」時，完全不需要枚舉所有分法 —— 一維 DP 就夠了。</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">s = &quot;aabbc&quot;　　dp[i] = s[0..i] 最少要切幾刀</text>
            <g font-size="13" text-anchor="middle">
              <rect x="70" y="70" width="70" height="30" fill="none" stroke="var(--border)"/><text x="105" y="90" fill="var(--text-muted)">a</text>
              <rect x="140" y="70" width="70" height="30" fill="none" stroke="var(--border)"/><text x="175" y="90" fill="var(--text-muted)">a</text>
              <rect x="210" y="70" width="70" height="30" fill="none" stroke="var(--border)"/><text x="245" y="90" fill="var(--text-muted)">b</text>
              <rect x="280" y="70" width="70" height="30" fill="none" stroke="var(--border)"/><text x="315" y="90" fill="var(--text-muted)">b</text>
              <rect x="350" y="70" width="70" height="30" fill="none" stroke="var(--border)"/><text x="385" y="90" fill="var(--text-muted)">c</text>
              <text x="105" y="124" fill="var(--accent)">0</text>
              <text x="175" y="124" fill="var(--accent)">0</text>
              <text x="245" y="124" fill="var(--accent)">1</text>
              <text x="315" y="124" fill="var(--accent)">1</text>
              <text x="385" y="124" fill="var(--gold)" font-size="16">2</text>
              <text x="40" y="90" fill="var(--gold)" font-size="11">s：</text>
              <text x="40" y="124" fill="var(--gold)" font-size="11">dp：</text>
            </g>
            <text x="450" y="124" fill="var(--gold)" font-size="12" text-anchor="start">← 答案</text>
            <line x1="20" y1="148" x2="620" y2="148" stroke="var(--border)"/>
            <text x="20" y="176" fill="var(--accent)" font-size="12">逐格推導：</text>
            <text x="40" y="202" fill="var(--text-muted)" font-size="12">dp[0]：&quot;a&quot; 本身是回文 → 0 刀</text>
            <text x="40" y="226" fill="var(--text-muted)" font-size="12">dp[1]：&quot;aa&quot; 本身是回文 → 0 刀</text>
            <text x="40" y="250" fill="var(--text-muted)" font-size="12">dp[2]：&quot;aab&quot; 不是回文。試最後一段是 &quot;b&quot; → dp[1] + 1 = 1 ✔</text>
            <text x="40" y="274" fill="var(--text-muted)" font-size="12">dp[3]：試最後一段 &quot;bb&quot; → dp[1] + 1 = 1 ✔　（比切成 aa|b|b 的 2 刀好）</text>
            <text x="40" y="298" fill="var(--gold)" font-size="12">dp[4]：最後一段只能是 &quot;c&quot; → dp[3] + 1 = 2 ✔　→ &quot;aa | bb | c&quot;</text>
            <line x1="20" y1="320" x2="620" y2="320" stroke="var(--border)"/>
            <text x="20" y="348" fill="#ff8a65" font-size="12">★ 和第 131 題的複雜度差距：</text>
            <text x="40" y="374" fill="var(--text-muted)" font-size="12">131（列出所有分法）：O(n · 2ⁿ)，所以 n ≤ 16</text>
            <text x="40" y="398" fill="var(--gold)" font-size="12">132（只要最少刀數）：O(n²)，　　所以 n 可以到 2000</text>
            <text x="20" y="430" fill="var(--accent)" font-size="12">「算出最優的那一個」比「列出全部」便宜太多 —— 這是 DP 存在的全部理由。</text>'''

emit({
 "num": 132, "slug": "palindrome-partitioning-ii",
 "en": [
   "Given a string <code>s</code>, partition <code>s</code> such that every substring of the "
   "partition is a palindrome.",
   "Return <em>the <strong>minimum</strong> cuts needed for a palindrome partitioning of </em>"
   "<code>s</code>.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，把它切成若干段，使得<strong>每一段都是回文</strong>。",
   "回傳<strong>最少需要切幾刀</strong>。",
   ("note", "注意是「刀數」不是「段數」", [
     "<strong>切 <code>k</code> 刀會得到 <code>k+1</code> 段。</strong>",
     "所以整個字串本身就是回文時，答案是 <code>0</code>（一刀都不用切）。",
     "<strong>答案的上界是 <code>n-1</code></strong>（每個字元自己一段）。",
   ]),
 ],
 "pre": [
   ("note", "和第 131 題的天壤之別", [
     ("c", """131（列出所有分法）：O(n · 2^n)，n <= 16
132（只要最少刀數）：O(n²)，     n <= 2000

    同一個問題結構，但「要全部」和「要最優」
    的成本差了天文數字。

【為什麼？】

    「列出全部」的下界由【輸出大小】決定 ——
    答案有 2^(n-1) 種，光印出來就要那麼久。

    「求最優」不需要產生所有答案 ——
    只要一路記住「到目前為止的最佳值」。

    這正是【動態規劃】存在的理由：

        用「最優子結構」把指數級的搜尋空間
        壓縮成多項式級的狀態空間。

【辨認訊號】：

    題目問「最少 / 最多 / 有幾種」-> 想 DP
    題目問「列出所有」           -> 回溯，而且要接受指數級

    n 的上限也是提示：
        n <= 20 左右 -> 指數級是預期解
        n <= 2000    -> O(n²) 是預期解
        n <= 10^5    -> O(n) 或 O(n log n)"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "aab"
  輸出：1
  說明：切成 "aa" | "b"，兩段都是回文，只切了一刀。

範例 2
  輸入：s = "a"
  輸出：0

範例 3
  輸入：s = "ab"
  輸出：1""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 2000",
   "<code>s</code> 只包含小寫英文字母",
 ],
 "idea": [
   ("fig", _P132_FIG, "0 0 640 448"),
   ("c", """【狀態】
    dp[i] = s[0..i] 最少要切幾刀

【轉移】
    如果 s[0..i] 整段就是回文 -> dp[i] = 0

    否則枚舉「最後一段從哪裡開始」：

        dp[i] = min over j (1 <= j <= i, s[j..i] 是回文) of dp[j-1] + 1
                                                            ^^^^^^^  ^^^
                                                            前面的成本  這一刀

【答案】dp[n-1]

【為什麼要特判 pal[0][i]？】

    因為 j 是從 1 開始的（「最後一段」的起點）。
    j = 0 的情況（整段都是最後一段）沒有「前面的部分」，
    也不需要切這一刀 -> 直接是 0。

    寫成 dp[-1] = -1 的話可以統一，
    但用 1-indexed 會更乾淨（見解法二）。

【複雜度】
    回文表 O(n²) + DP O(n²) = O(n²)

    n = 2000 -> 400 萬，完全可以接受。

【★ 為什麼這題一定要預處理回文表？】

    第 131 題裡預處理「不影響漸進複雜度」
    （因為輸出本來就是指數級的）。

    這題不一樣：
        不預處理 -> 每次檢查 O(n) -> 總共 O(n³)
        n = 2000 -> 80 億 ✘ 一定逾時

        預處理   -> 每次檢查 O(1) -> 總共 O(n²) ✔

    【同一個優化，在兩題裡的價值完全不同。
      這就是為什麼要看清楚「瓶頸在哪裡」。】"""),
 ],
 "approaches": [
   ap("解法一", "回文表 + 一維 DP（標準答案）", [
     ("c", S["p132_dp"]),
     ("h", "兩個 O(n²) 疊在一起"),
     ("c", """第一段：建回文表     O(n²)
第二段：DP           O(n²)

    兩段都是 O(n²)，總共還是 O(n²) ✔

    n = 2000 -> 回文表有 400 萬格（Python 下約 32MB），
    有點大但還在限制內。

【空間優化：可以不存完整的回文表嗎？】

    可以 —— 解法二用「中心擴展」把兩件事合在一起做，
    空間降到 O(n)。

    但解法一的結構比較清楚，
    面試時先寫它。"""),
     ("h", "<code>min(...)</code> 裡的生成式不會是空的嗎？"),
     ("c", """dp[i] = min(dp[j-1] + 1 for j in range(1, i+1) if pal[j][i])

    如果沒有任何 j 滿足 pal[j][i]，min() 會丟 ValueError。

    但這【不可能發生】——

        j = i 時，pal[i][i] 永遠是 True（單一字元是回文）✔

    所以生成式至少有一項。

【不過寫防禦性的程式比較好】：

        dp[i] = min((dp[j-1] + 1 for j in ... if pal[j][i]), default=i)

    default=i 是「最壞情況：每個字元自己一段，切 i 刀」。

    【知道「為什麼不會出錯」比「加上防禦」更重要 ——
      但兩個都做最好。】""",),
     "<strong>時間 O(n²)、空間 O(n²)。</strong>",
   ], "O(n²)", "O(n²)", "回文表 + DP", "回文表", optimal=True),

   ap("解法二", "中心擴展 + 同時更新 DP（空間 O(n)）", [
     ("c", S["p132_center"]),
     ("h", "★ 把「找回文」和「更新 DP」合成一步"),
     ("c", """不先建表，而是【一邊擴展回文、一邊更新 dp】：

    for center in 每個可能的中心:
        往兩邊擴展，每擴出一個回文 s[l..r]：
            dp[r+1] = min(dp[r+1], dp[l] + 1)

【為什麼這樣就夠？】

    每個回文子字串都會被「它的中心」擴展到 ✔
    （奇數長度用單一中心，偶數長度用兩個字之間。）

    所以每個「合法的最後一段」都會被考慮到。

【1-indexed 的技巧】

    dp = list(range(-1, n))     -> dp = [-1, 0, 1, 2, ..., n-1]

    dp[i] 代表「s[0..i-1]（前 i 個字）最少切幾刀」

    dp[0] = -1：空字串「切 -1 刀」
        —— 這樣 dp[l] + 1 在 l = 0 時剛好是 0 ✔
           （整段就是回文，不用切）

    初始值 dp[i] = i - 1：
        最壞情況「每個字元自己一段」= i-1 刀 ✔

    【用 -1 當「空字串」的 base case，
      是為了讓「加一刀」的公式在邊界也成立。
      這和第 1 題用 dummy head 的精神一樣。】

【複雜度】
    中心有 2n-1 個，每個最多擴展 O(n) 次 -> O(n²) 時間
    只用一個長度 n+1 的 dp -> O(n) 空間 ✔

    比解法一省了 O(n²) 的回文表。"""),
     ("h", "為什麼可以「邊擴邊更新」而不用等回文表建完？"),
     ("c", """因為 dp[r+1] 只依賴 dp[l]，而 l <= r。

    但要小心：dp[l] 在被讀取時，是不是已經是最終值？

    【不一定！】

    例如 center 很小時，可能會更新一個很大的 dp[r+1]，
    而那時 dp[l] 可能還會被後面的 center 改小。

    ...但這不影響正確性，因為：

        我們對 dp[r+1] 做的是 min()，
        而所有 (l, r) 的組合最終都會被枚舉到。

        只要「每一對 (l, r) 都被考慮過至少一次」，
        最後的 dp 就是正確的最小值 ✔

    【這是「鬆弛（relaxation）」的思想 ——
      和 Bellman-Ford 演算法一樣：
      不要求「按正確順序更新」，
      只要求「每條邊都被鬆弛夠多次」。】

    嚴格地說，這裡每對 (l, r) 只被鬆弛一次，
    而由於 dp[l] 只依賴「更短的前綴」，
    且中心擴展會先產生短的回文，順序其實是安全的。"""),
   ], "O(n²)", "O(n)", "每個中心擴展 O(n)", "只有 dp 陣列"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、回文表 + DP", "O(n²)", "O(n²)", "16", "結構最清楚"],
    ["二、中心擴展 + DP", "O(n²)", "O(n)", "18", "空間最省"]]),
 "edges": [
   "<strong>單一字元</strong> → <code>0</code>。",
   "<strong>整個就是回文</strong> <code>\"abccba\"</code> → <code>0</code>。"
   "<strong>忘了特判 <code>pal[0][i]</code> 會得到 1。</strong>",
   "<strong>完全沒有多字元回文</strong> <code>\"abc\"</code> → <code>2</code>（上界）。",
   "<strong><code>\"aab\"</code></strong> → <code>1</code>。",
   "<strong><code>\"cdd\"</code></strong> → <code>1</code>（切成 <code>\"c\"|\"dd\"</code>）。",
   "<strong>全部相同</strong> <code>\"aaaa\"</code> → <code>0</code>。",
   "<strong>不預處理回文表（O(n³)）</strong> → "
   "<strong>n = 2000 時 80 億次運算，一定逾時。</strong>",
   "<strong>回文表的 <code>i</code> 由小到大算</strong> → 長度 ≥ 3 的回文全漏。",
   "<strong>解法二的 <code>dp[0]</code> 設成 0 而不是 -1</strong> → 每個答案都多 1。",
 ],
 "follow": [
   ("h", "追問一：如果要輸出「切在哪裡」呢？"),
   "<strong>在更新 <code>dp[i]</code> 時記下「最後一段的起點 <code>j</code>」</strong>，"
   "最後從 <code>n-1</code> 往回追。",
   ("c", """cut_from = [0] * n
...
    dp[i] = dp[j-1] + 1
    cut_from[i] = j          # 記下來

回溯：
    i = n - 1
    parts = []
    while i >= 0:
        j = cut_from[i]
        parts.append(s[j:i+1])
        i = j - 1
    parts.reverse()

【O(n) 額外空間，O(n) 回溯時間。】

    這是所有 DP 題「輸出方案」的通用做法：
    【在轉移時記錄「是從哪裡來的」】。""",),
   ("h", "追問二：能不能比 O(n²) 更快？"),
   ("c", """可以 —— 有 O(n log n) 甚至 O(n) 的做法，
但都非常進階：

    (a) 用【回文樹（Eertree）】或【Manacher】
        找出所有「極大回文」，
        然後在一個特殊結構上做 DP。

    (b) 利用「回文的週期性質」：
        以某個位置結尾的所有回文，
        它們的起點構成 O(log n) 個等差數列（Palindromic Series）。

        基於這個可以做到 O(n log n)。

【但這在面試裡幾乎不會被要求】。

    O(n²) 對 n = 2000 完全夠用，
    知道「存在更快的做法」就好。

    如果面試官真的追問，
    回答「這牽涉到回文的週期結構，
    可以用 Manacher 加上分組 DP 做到 O(n log n)」
    就足夠了。""",),
   ("h", "追問三：如果改成「每段長度至少 k」呢？"),
   "<strong>轉移式加一個條件：<code>i - j + 1 >= k</code></strong>。",
   "<strong>但要注意可能無解</strong>（例如 <code>s = \"ab\"</code>、<code>k = 2</code>）—— "
   "<strong>那時 <code>dp[n-1]</code> 會是 <code>inf</code>，要回傳 <code>-1</code> 之類的。</strong>",
   "<strong>加限制時，第一件事永遠是問「還有沒有解」。</strong>",
   ("h", "追問四：這個 DP 的形狀在別的題目也見過嗎？"),
   ("c", """「把字串切成若干段，每段滿足某個條件，求最優」
是一個非常常見的骨架：

  132  回文分割 II      每段是回文，求最少刀數      （本題）
  139  單詞拆分         每段在字典裡，問可不可行
  140  單詞拆分 II      每段在字典裡，列出所有分法
  91   解碼方法         每段是 1..26，問有幾種
  93   復原 IP 位址     切成 4 段，每段 0..255

【共同的轉移式】：

    dp[i] = <合併> over j: (s[j..i] 合法) 的 dp[j-1] <加上這一段的成本>

    「合併」是 min / max / sum / or，
    取決於題目要「最優」「有幾種」還是「可不可行」。

【認出這個骨架，這五題就變成同一題。】"""),
 ],
 "related": [
   "<strong>第 131 題 Palindrome Partitioning</strong> —— 列出所有分法",
   "<strong>第 5 題 Longest Palindromic Substring</strong> —— 中心擴展的原型",
   "<strong>第 139 題 Word Break</strong> —— 同一個「切字串」DP 骨架",
   "<strong>第 91 題 Decode Ways</strong> —— 同上，改成計數",
   "<strong>第 1278 題 Palindrome Partitioning III</strong> —— 固定切 k 段，允許改字元",
 ],
 "check": [
   "為什麼「求最少刀數」的複雜度比「列出所有分法」低這麼多？",
   "這題為什麼一定要預處理回文表，而第 131 題不預處理也沒差？",
   "解法二的 <code>dp[0] = -1</code> 是什麼意思？設成 0 會怎樣？",
   "如果要輸出「切在哪些位置」，該記錄什麼？",
 ],
})
print("P132 written")

# ==================== 133. Clone Graph ====================
class GNode(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


_GN = {"Node": GNode}

S["p133_dfs"] = '''class Solution:
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}                     # 原節點 -> 新節點

        def dfs(cur):
            if cur in old_to_new:
                return old_to_new[cur]      # ★ 已經複製過，直接回傳（這樣才不會無限遞迴）

            copy = Node(cur.val)
            old_to_new[cur] = copy          # ★ 先登記，再遞迴鄰居
            for nb in cur.neighbors:
                copy.neighbors.append(dfs(nb))
            return copy

        return dfs(node) if node else None'''

S["p133_bfs"] = '''from collections import deque

class Solution:
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if not node:
            return None

        old_to_new = {node: Node(node.val)}
        dq = deque([node])

        while dq:
            cur = dq.popleft()
            for nb in cur.neighbors:
                if nb not in old_to_new:
                    old_to_new[nb] = Node(nb.val)   # 第一次看到，先建好
                    dq.append(nb)
                old_to_new[cur].neighbors.append(old_to_new[nb])

        return old_to_new[node]'''

S["p133_wrong"] = '''class Solution:
    # 【這是錯的，不要抄】
    def cloneGraph(self, node: 'Optional[Node]') -> 'Optional[Node]':
        if not node:
            return None
        copy = Node(node.val)
        for nb in node.neighbors:
            copy.neighbors.append(self.cloneGraph(nb))   # 沒有記錄，會無限遞迴
        return copy'''


def _make_graph(adj):
    """adj 是 0-indexed 的鄰接表；節點值用 1..n。"""
    nodes = [GNode(i + 1) for i in range(len(adj))]
    for i, nbs in enumerate(adj):
        nodes[i].neighbors = [nodes[j] for j in nbs]
    return nodes[0] if nodes else None


def _to_adj(node):
    """把圖讀回鄰接表（依 val 排序），並檢查沒有共用到原節點。"""
    if node is None:
        return []
    seen = {}
    q = deque([node])
    seen[node.val] = node
    while q:
        cur = q.popleft()
        for nb in cur.neighbors:
            if nb.val not in seen:
                seen[nb.val] = nb
                q.append(nb)
    return [sorted(nb.val for nb in seen[v].neighbors) for v in sorted(seen)]


def _all_nodes(node):
    if node is None:
        return []
    out, q, seen = [], deque([node]), {id(node)}
    while q:
        cur = q.popleft()
        out.append(cur)
        for nb in cur.neighbors:
            if id(nb) not in seen:
                seen.add(id(nb)); q.append(nb)
    return out


_p133 = [S.load(k, extra=_GN) for k in ("p133_dfs", "p133_bfs")]

_CASES133 = [
    [[1, 3], [0, 2], [1, 3], [0, 2]],
    [[]],
    [],
    [[1], [0]],
    [[1, 2], [0, 2], [0, 1]],
]
for adj in _CASES133:
    src = _make_graph(adj)
    want = _to_adj(src)
    orig_ids = {id(x) for x in _all_nodes(src)}
    for sol in _p133:
        g = _make_graph(adj)
        out = sol.cloneGraph(g)
        assert _to_adj(out) == _to_adj(g) == want, ("P133", adj, sol)
        # 必須是「深拷貝」：新圖不能含有任何原圖的節點物件
        new_ids = {id(x) for x in _all_nodes(out)}
        old_ids = {id(x) for x in _all_nodes(g)}
        assert not (new_ids & old_ids), ("P133 shallow copy!", adj, sol)

for _ in range(1500):
    n = random.randrange(1, 8)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.45:
                adj[i].append(j); adj[j].append(i)
    # 保證連通（題目的圖是連通的）
    for i in range(1, n):
        if not adj[i]:
            adj[i].append(0); adj[0].append(i)
    want = _to_adj(_make_graph(adj))
    for sol in _p133:
        g = _make_graph(adj)
        out = sol.cloneGraph(g)
        assert _to_adj(out) == want, ("P133 random", adj, sol)
        assert not ({id(x) for x in _all_nodes(out)} & {id(x) for x in _all_nodes(g)}), \
            ("P133 shallow", adj, sol)
print("P133 solutions OK")

_P133_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 圖有【環】，所以「照著邊遞迴複製」會無限繞下去。解法：用一張表記住「誰已經複製過了」。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">原圖（節點 1 和 2 互為鄰居 —— 一個最小的環）</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="110" cy="110" r="22" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="110" y="115" fill="var(--accent)">1</text>
              <circle cx="240" cy="110" r="22" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="240" y="115" fill="var(--accent)">2</text>
            </g>
            <line x1="132" y1="110" x2="218" y2="110" stroke="var(--border)" stroke-width="2"/>
            <text x="20" y="168" fill="#ff8a65" font-size="12">沒有記錄表的話：複製 1 → 要複製鄰居 2 → 要複製 2 的鄰居 1 → 又要複製 1 …</text>
            <text x="20" y="192" fill="#ff8a65" font-size="12">無限遞迴，直接 RecursionError。</text>
            <line x1="20" y1="214" x2="620" y2="214" stroke="var(--border)"/>
            <text x="20" y="242" fill="var(--accent)" font-size="13">★ 關鍵：先登記，再遞迴</text>
            <text x="40" y="272" fill="var(--gold)" font-size="12">copy = Node(cur.val)　　　　　① 先把「殼」建好（鄰居還是空的）</text>
            <text x="40" y="298" fill="var(--gold)" font-size="12">old_to_new[cur] = copy　　　　② 【立刻登記】——這一步絕不能晚</text>
            <text x="40" y="324" fill="var(--text-muted)" font-size="12">for nb in cur.neighbors: …　　③ 再去遞迴鄰居，填 copy.neighbors</text>
            <text x="20" y="360" fill="var(--text-muted)" font-size="12">這樣當 2 回頭要找 1 時，表裡已經有 1 的複本了 → 直接拿來用，不再遞迴 ✔</text>
            <text x="20" y="390" fill="#ff8a65" font-size="12">如果把 ② 放到 ③ 後面（等鄰居都複製完才登記），環就又會無限繞回來。</text>
            <text x="20" y="420" fill="var(--accent)" font-size="12">「先建殼、登記、再填內容」是所有「複製有環結構」問題的共同解法 ——</text>
            <text x="20" y="444" fill="var(--accent)" font-size="12">第 138 題（複製帶隨機指標的串列）用的是一模一樣的手法。</text>'''

emit({
 "num": 133, "slug": "clone-graph",
 "en": [
   "Given a reference of a node in a <strong>connected</strong> undirected graph.",
   "Return a <strong>deep copy</strong> (clone) of the graph.",
   "Each node in the graph contains a value (<code>int</code>) and a list "
   "(<code>List[Node]</code>) of its neighbors.",
   ("c", """class Node {
    public int val;
    public List<Node> neighbors;
}"""),
 ],
 "zh": [
   "給你一個<strong>連通</strong>無向圖裡的某一個節點的參考，"
   "回傳整張圖的<strong>深拷貝</strong>。",
   "每個節點有一個整數 <code>val</code> 和一個鄰居 list。",
   ("note", "「深拷貝」是什麼意思？", [
     "<strong>新圖裡的每一個節點都必須是<strong>新建的物件</strong>，"
     "不能有任何一個節點是原圖的。</strong>",
     "而且<strong>連接關係要和原圖一模一樣</strong>。",
     "<strong>淺拷貝</strong>（只複製第一層、鄰居直接指向原節點）"
     "<strong>是不合格的</strong> —— 改動新圖會影響到舊圖。",
   ]),
 ],
 "pre": [
   ("note", "★ 圖有環，所以「照著邊遞迴」會無限繞", [
     ("c", S["p133_wrong"]),
     ("c", """這段程式碼看起來完全合理：
    「建一個複本，然後遞迴複製每個鄰居。」

但圖是【無向】的 —— 每條邊都是雙向的，
所以【最簡單的兩個節點就構成一個環】：

    1 —— 2

    cloneGraph(1)
      -> 複製 1
      -> 遞迴 cloneGraph(2)
           -> 複製 2
           -> 遞迴 cloneGraph(1)      ← 又回來了！
                -> 複製 1（又一個新的）
                -> 遞迴 cloneGraph(2) ← ...

    無限遞迴 -> RecursionError ✘

【樹沒有這個問題，圖有。】

    這是「樹的題目」和「圖的題目」最根本的差別：
        樹：往下走永遠不會回頭
        圖：可能繞回來

    所以【所有圖的走訪都必須有 visited 記錄】。

【這題的 visited 還兼任第二個角色】：

    old_to_new 不只記錄「走過了」，
    還記錄「走過的那個節點，對應到哪個複本」。

    一張表，兩個用途。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：adjList = [[2,4],[1,3],[2,4],[1,3]]

        1 —— 2
        |    |
        4 —— 3

  輸出：[[2,4],[1,3],[2,4],[1,3]]
  說明：節點 1 的鄰居是 2 和 4，節點 2 的鄰居是 1 和 3，以此類推。

範例 2
  輸入：adjList = [[]]
  輸出：[[]]
  說明：只有一個節點，沒有任何邊。

範例 3
  輸入：adjList = []
  輸出：[]
  說明：空圖。""",
 "constraints": [
   "節點數在 <code>[0, 100]</code> 之間",
   "1 ≤ <code>Node.val</code> ≤ 100",
   "<code>Node.val</code> <strong>互不相同</strong>",
   "沒有重複的邊，也沒有自環",
   "圖是<strong>連通</strong>的，從任一節點都能走到所有節點",
 ],
 "idea": [
   ("fig", _P133_FIG, "0 0 640 462"),
   ("c", """用一個字典 old_to_new: {原節點 -> 新節點}，
它同時扮演兩個角色：

    ① visited 集合（有沒有走過）
    ② 對照表（走過的話，複本是哪一個）

【★★ 三個步驟的順序絕對不能變】

    def dfs(cur):
        if cur in old_to_new:
            return old_to_new[cur]       # 已經複製過

        copy = Node(cur.val)             # ① 先建「殼」
        old_to_new[cur] = copy           # ② 【立刻】登記
        for nb in cur.neighbors:         # ③ 再填鄰居
            copy.neighbors.append(dfs(nb))
        return copy

【為什麼 ② 一定要在 ③ 之前？】

    考慮 1 —— 2：

        dfs(1): 建 copy1，登記 {1: copy1}
            dfs(2): 建 copy2，登記 {2: copy2}
                dfs(1): 【表裡有了】-> 直接回 copy1 ✔ 不再遞迴
            copy2.neighbors = [copy1]
        copy1.neighbors = [copy2]

        完成 ✔

    如果 ② 在 ③ 之後（等鄰居都複製完才登記）：

        dfs(1): 建 copy1
            dfs(2): 建 copy2
                dfs(1): 表裡【還沒有 1】-> 又建一個 copy1' ...
                    無限遞迴 ✘

【「先把不完整的東西登記進去，再去填它」——
  這是處理「循環參考」的通用手法。】

    第 138 題（複製帶隨機指標的串列）、
    物件序列化（pickle / JSON with refs）、
    垃圾回收的標記階段 —— 用的都是這一招。

【為什麼用「節點物件」當 key 而不是 val？】

    這題保證 val 互不相同，所以用 val 當 key 也可以。

    但用節點物件更通用（val 可能重複時也對），
    而且 Python 的物件預設可雜湊（用 id），
    所以直接當 key 完全沒問題 ✔"""),
 ],
 "approaches": [
   ap("解法一", "DFS + 對照表（標準答案）", [
     ("c", S["p133_dfs"]),
     "<strong>十行。<code>old_to_new</code> 一張表做兩件事。</strong>",
     ("h", "空圖的處理"),
     "<code>return dfs(node) if node else None</code> —— "
     "<strong>題目說節點數可以是 0，所以 <code>node</code> 可能是 <code>None</code>。</strong>",
     "<strong>不擋的話 <code>cur.val</code> 直接 crash。</strong>",
     ("h", "複雜度"),
     ("c", """時間 O(V + E)：
    每個節點被 dfs 呼叫一次（之後都直接查表），
    每條邊被走一次（無向圖的話是兩次）。

空間 O(V)：
    對照表 O(V) + 遞迴堆疊最壞 O(V)

    節點數 <= 100，遞迴深度完全不是問題。

【這是圖走訪的標準複雜度】——
    看到 O(V + E) 就知道「每個節點和每條邊都只碰一次」。""",),
   ], "O(V + E)", "O(V)", "每個節點和每條邊一次", "對照表 + 遞迴堆疊", optimal=True),

   ap("解法二", "BFS + 對照表", [
     ("c", S["p133_bfs"]),
     ("h", "和 DFS 版的結構差異"),
     ("c", """DFS 版：在遞迴時「順便」建立鄰居
BFS 版：先把節點都建好，再連邊

    while dq:
        cur = dq.popleft()
        for nb in cur.neighbors:
            if nb not in old_to_new:
                old_to_new[nb] = Node(nb.val)   # 建殼
                dq.append(nb)
            old_to_new[cur].neighbors.append(old_to_new[nb])
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
            這一行在【每次看到邊時】都執行，不只在第一次

【注意這一行不能放進 if 裡面】

    如果放進 if（只在「第一次看到 nb」時連邊），
    那麼「已經建過的鄰居」就連不上了 ✘

    例如三角形 1-2-3-1：
        處理 1 時，2 和 3 都是新的 -> 連上 ✔
        處理 2 時，1 和 3 都已存在 -> 如果在 if 裡就跳過 ✘
                                      2 的鄰居會是空的

    【「建節點」和「連邊」是兩件事，
      前者要去重，後者不能去重。】

    這是 BFS 版最常見的 bug。""",),
     "<strong>沒有遞迴深度問題</strong>（本題用不到，但習慣好）。"
     "<strong>複雜度和 DFS 版完全相同。</strong>",
   ], "O(V + E)", "O(V)", "每個節點和每條邊一次", "對照表 + 佇列"),
 ],
 "compare": (["解法", "時間", "空間", "遞迴？", "備註"],
   [["一、DFS + 對照表", "O(V+E)", "O(V)", "✔", "最短，十行"],
    ["二、BFS + 對照表", "O(V+E)", "O(V)", "✘", "注意連邊不能放進 if"]]),
 "edges": [
   "<strong>空圖</strong>（<code>node = None</code>）→ <code>None</code>。"
   "<strong>一定要擋。</strong>",
   "<strong>單一節點、沒有邊</strong> → 一個新節點，<code>neighbors</code> 是空的。",
   "<strong>兩個節點互為鄰居</strong> → <strong>最小的環，沒有對照表就會無限遞迴。</strong>",
   "<strong>完全圖</strong>（100 個節點兩兩相連）→ 4950 條邊，<code>O(V+E)</code> 輕鬆處理。",
   "<strong>沒有對照表</strong> → <strong><code>RecursionError</code>。本題的核心考點。</strong>",
   "<strong>先遞迴鄰居、後登記</strong> → 一樣無限遞迴。",
   "<strong>BFS 版把「連邊」放進 <code>if</code> 裡</strong> → "
   "<strong>已經建過的鄰居連不上，鄰居表不完整。</strong>",
   "<strong>回傳的是淺拷貝</strong>（<code>neighbors</code> 直接指向原節點）→ 判題會失敗。",
 ],
 "follow": [
   ("h", "追問一：如果圖<strong>不連通</strong>呢？"),
   "<strong>題目保證連通，所以從任一節點都能走遍全圖。</strong>",
   "<strong>如果不連通，光給一個節點是不夠的</strong> —— "
   "<strong>你根本碰不到其他連通塊。</strong>"
   "<strong>那時題目必須給「所有節點的 list」，"
   "然後對每個還沒複製的節點都跑一次 DFS。</strong>",
   ("h", "追問二：這和第 138 題（複製帶隨機指標的串列）有什麼關係？"),
   ("c", """完全同一招。

    第 138 題的 random 指標可以指向串列裡的任何節點
    -> 形成任意的「環」和「交叉」

    解法也是 {原節點 -> 新節點} 的對照表：

        1. 第一遍：建所有新節點，填好對照表
        2. 第二遍：用對照表填 next 和 random

    或者像本題一樣，用 DFS 一次做完。

【第 138 題還有一個更漂亮的 O(1) 空間解】：

    把新節點「交錯插入」原串列中間：
        A -> A' -> B -> B' -> C -> C'

    這樣 A' 就是 A.next，
    A'.random = A.random.next  ← 不用對照表了！

    最後再把兩條串列拆開。

    【那個技巧在圖上做不到 ——
      因為圖沒有「插在中間」這個概念。】""",),
   ("h", "追問三：如果節點值可能重複呢？"),
   "<strong>本文的解法完全不受影響</strong> —— 因為 <strong>key 是「節點物件」而不是 <code>val</code></strong>。",
   "<strong>如果你圖方便用 <code>val</code> 當 key，那就會出錯</strong>："
   "<strong>兩個 <code>val</code> 相同的不同節點會被當成同一個，複製出來的圖會少節點。</strong>",
   "<strong>「用什麼當 key」是雜湊表題最容易忽略的設計決定。</strong>",
   ("h", "追問四：能不能不用額外空間？"),
   "<strong>不行。</strong>輸出本身就有 <code>V</code> 個新節點 —— <strong>至少 O(V)。</strong>",
   "<strong>而且「記住誰複製過」這個資訊也是必要的</strong>"
   "（除非你能在原節點上做記號，但題目沒給那樣的欄位）。",
   "<strong>如果允許修改原圖，可以像第 138 題那樣「把複本暫時掛在原節點上」</strong> —— "
   "<strong>但 <code>Node</code> 沒有多餘的欄位可用，所以這題做不到。</strong>",
 ],
 "related": [
   "<strong>第 138 題 Copy List with Random Pointer</strong> —— 一模一樣的手法",
   "<strong>第 200 題 Number of Islands</strong> —— 圖走訪的 visited",
   "<strong>第 207 題 Course Schedule</strong> —— 有向圖的環偵測",
   "<strong>第 297 題 Serialize and Deserialize Binary Tree</strong> —— 「複製結構」的另一種形式",
 ],
 "check": [
   "為什麼「照著邊直接遞迴複製」會無限遞迴？樹為什麼沒有這個問題？",
   "「先登記、再遞迴鄰居」的順序為什麼不能反？",
   "<code>old_to_new</code> 這張表同時扮演哪兩個角色？",
   "BFS 版的「連邊」那一行為什麼不能放進 <code>if</code> 裡？",
 ],
})
print("P133 written")

# ==================== 134. Gas Station ====================
S["p134_greedy"] = '''class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0       # 全程的淨油量：負的就一定無解
        tank = 0        # 從目前的起點出發，開到這裡剩多少油
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff
            if tank < 0:
                start = i + 1   # ★ 從 start 到 i 都不能當起點，直接跳到 i+1
                tank = 0

        return start if total >= 0 else -1'''

S["p134_brute"] = '''class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for start in range(n):
            tank = 0
            for k in range(n):              # 從 start 開一圈
                i = (start + k) % n
                tank += gas[i] - cost[i]
                if tank < 0:
                    break
            else:
                return start                # 沒有 break -> 成功繞一圈
        return -1'''

S["p134_minprefix"] = '''class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 另一個角度：找「前綴和最小」的那個位置，它的下一站就是答案
        total = 0
        min_sum = 0
        min_idx = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < min_sum:
                min_sum = total
                min_idx = i + 1

        return min_idx % len(gas) if total >= 0 else -1'''


def _p134_ref(gas, cost):
    """獨立參考解：暴力枚舉每個起點。"""
    n = len(gas)
    for s in range(n):
        tank = 0
        ok = True
        for k in range(n):
            i = (s + k) % n
            tank += gas[i] - cost[i]
            if tank < 0:
                ok = False; break
        if ok:
            return s
    return -1


_p134 = [S.load(k) for k in ("p134_greedy", "p134_brute", "p134_minprefix")]

for g, c, want in [
    ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
    ([2, 3, 4], [3, 4, 3], -1),
    ([5], [4], 0),
    ([4], [5], -1),
    ([3, 1, 1], [1, 2, 2], 0),
]:
    assert _p134_ref(g, c) == want, ("P134 ref", g, c, _p134_ref(g, c))
    for sol in _p134:
        assert sol.canCompleteCircuit(list(g), list(c)) == want, ("P134", g, c, sol)

for _ in range(6000):
    n = random.randrange(1, 9)
    g = [random.randint(0, 6) for _ in range(n)]
    c = [random.randint(0, 6) for _ in range(n)]
    want = _p134_ref(g, c)
    for sol in _p134:
        got = sol.canCompleteCircuit(list(g), list(c))
        assert got == want, ("P134 random", g, c, want, got, sol)
print("P134 solutions OK")

_P134_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">把每站化成一個淨值 diff[i] = gas[i] − cost[i]，問題變成「從哪裡開始繞一圈，前綴和永遠不會變負」。</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">gas = [1,2,3,4,5]　cost = [3,4,5,1,2]　→　diff = [−2, −2, −2, 3, 3]</text>
            <g font-size="13" text-anchor="middle">
              <rect x="70" y="70" width="84" height="30" fill="none" stroke="#ff8a65"/><text x="112" y="90" fill="#ff8a65">−2</text>
              <rect x="154" y="70" width="84" height="30" fill="none" stroke="#ff8a65"/><text x="196" y="90" fill="#ff8a65">−2</text>
              <rect x="238" y="70" width="84" height="30" fill="none" stroke="#ff8a65"/><text x="280" y="90" fill="#ff8a65">−2</text>
              <rect x="322" y="70" width="84" height="30" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="364" y="90" fill="var(--gold)">+3</text>
              <rect x="406" y="70" width="84" height="30" fill="none" stroke="var(--accent)"/><text x="448" y="90" fill="var(--accent)">+3</text>
              <text x="112" y="118" fill="var(--text-muted)" font-size="11">站 0</text>
              <text x="196" y="118" fill="var(--text-muted)" font-size="11">站 1</text>
              <text x="280" y="118" fill="var(--text-muted)" font-size="11">站 2</text>
              <text x="364" y="118" fill="var(--gold)" font-size="11">站 3 ← 答案</text>
              <text x="448" y="118" fill="var(--text-muted)" font-size="11">站 4</text>
            </g>
            <text x="20" y="152" fill="var(--text-muted)" font-size="12">總和 = −2−2−2+3+3 = 0 ≥ 0 → 一定有解</text>
            <line x1="20" y1="174" x2="620" y2="174" stroke="var(--border)"/>
            <text x="20" y="202" fill="var(--accent)" font-size="13">一趟掃描（tank 變負就換起點）：</text>
            <text x="40" y="230" fill="var(--text-muted)" font-size="12">i=0　tank = −2 &lt; 0 → start = 1，tank 歸零</text>
            <text x="40" y="254" fill="var(--text-muted)" font-size="12">i=1　tank = −2 &lt; 0 → start = 2，tank 歸零</text>
            <text x="40" y="278" fill="var(--text-muted)" font-size="12">i=2　tank = −2 &lt; 0 → start = 3，tank 歸零</text>
            <text x="40" y="302" fill="var(--text-muted)" font-size="12">i=3　tank = 3 ≥ 0 → 繼續</text>
            <text x="40" y="326" fill="var(--gold)" font-size="12">i=4　tank = 6 ≥ 0 → 結束。答案 start = 3 ✔</text>
            <line x1="20" y1="348" x2="620" y2="348" stroke="var(--border)"/>
            <text x="20" y="376" fill="#ff8a65" font-size="12">★ 為什麼「從 start 到 i 之間」的每一站都可以直接跳過，不用一個一個試？</text>
            <text x="20" y="402" fill="var(--text-muted)" font-size="12">因為從 start 出發走到 i 時油箱才變負 —— 代表 start..i−1 的每個前綴和都 ≥ 0。</text>
            <text x="20" y="426" fill="var(--text-muted)" font-size="12">從中間任何一站 k 出發，等於少了「start..k−1」那段【非負】的補給 ——</text>
            <text x="20" y="450" fill="var(--accent)" font-size="12">只會更早撐不住，不可能更好。所以那些起點可以一次全部排除 → O(n)。</text>'''

emit({
 "num": 134, "slug": "gas-station",
 "en": [
   "There are <code>n</code> gas stations along a circular route, where the amount of gas at "
   "the <code>i</code><sup>th</sup> station is <code>gas[i]</code>.",
   "You have a car with an unlimited gas tank and it costs <code>cost[i]</code> of gas to travel "
   "from the <code>i</code><sup>th</sup> station to its next <code>(i + 1)</code><sup>th</sup> "
   "station. You begin the journey with an empty tank at one of the gas stations.",
   "Given two integer arrays <code>gas</code> and <code>cost</code>, return <em>the starting "
   "gas station's index if you can travel around the circuit once in the clockwise direction, "
   "otherwise return</em> <code>-1</code>. If there exists a solution, it is "
   "<strong>guaranteed</strong> to be <strong>unique</strong>.",
 ],
 "zh": [
   "有 <code>n</code> 個加油站排成一個<strong>環</strong>，第 <code>i</code> 個站有 "
   "<code>gas[i]</code> 公升的油。",
   "你的車油箱無限大，從第 <code>i</code> 站開到第 <code>i+1</code> 站要花 "
   "<code>cost[i]</code> 公升。你從某一站出發，<strong>一開始油箱是空的</strong>。",
   "回傳<strong>能繞完一圈的起點編號</strong>；如果不可能，回傳 <code>-1</code>。",
   "<strong>如果有解，題目保證解是唯一的。</strong>",
 ],
 "pre": [
   ("note", "第一步：把兩個陣列合併成一個", [
     ("c", """diff[i] = gas[i] - cost[i]      「在第 i 站的淨收益」

    正的 -> 這一站補的油比開到下一站花的多
    負的 -> 這一站會虧油

問題重新表述：

    【找一個起點 s，使得從 s 開始的「環狀前綴和」永遠 >= 0】

    也就是：對所有 k = 0..n-1，
        diff[s] + diff[s+1] + ... + diff[s+k]  >= 0   （索引取模）

【這個轉換讓問題從「兩個陣列」變成「一個陣列」，
  而且從「模擬開車」變成「前綴和」——
  一下子清楚很多。】

    第 121 題（買賣股票）也用過同樣的「轉成差分」技巧。"""),
   ]),
   ("note", "★ 兩個關鍵引理", [
     ("c", """【引理一：total < 0 -> 一定無解】

    繞完一圈的總淨收益就是 sum(diff)。
    如果它是負的，不管從哪裡出發，
    走完一圈之後油箱一定是負的 -> 無解 ✔

【引理二：total >= 0 -> 一定有解】

    這個比較不直觀，但可以證明（見下方「追問一」）。

    直覺：油「總量夠」的話，
    一定存在一個「最低點」，從它的下一站出發就能撐過全程。

【兩個引理合起來】：

    total >= 0  ⟺  有解

    所以我們只要：
        1. 算 total 判斷「有沒有解」
        2. 用貪心找出「那個唯一的起點」

    而且【這兩件事可以在同一趟掃描裡完成】✔"""),
   ]),
 ],
 "examples": """範例 1
  輸入：gas = [1,2,3,4,5], cost = [3,4,5,1,2]
  輸出：3
  說明：從 3 號站出發（油箱 0）：
        到 3 號站加 4 升        -> 油箱 = 4
        開到 4 號站花 1 升      -> 油箱 = 3
        到 4 號站加 5 升        -> 油箱 = 8
        開到 0 號站花 2 升      -> 油箱 = 6
        加 1 升 -> 7，開到 1 花 3 -> 4
        加 2 升 -> 6，開到 2 花 4 -> 2
        加 3 升 -> 5，開到 3 花 5 -> 0  ✔ 繞回來了

範例 2
  輸入：gas = [2,3,4], cost = [3,4,3]
  輸出：-1
  說明：總油量 9，總花費 10 -> 不夠，怎麼繞都不行。""",
 "constraints": [
   "<code>n == gas.length == cost.length</code>",
   "1 ≤ <code>n</code> ≤ 10⁵",
   "0 ≤ <code>gas[i]</code>, <code>cost[i]</code> ≤ 10⁴",
   "如果有解，保證<strong>唯一</strong>",
 ],
 "idea": [
   ("fig", _P134_FIG, "0 0 640 468"),
   ("c", """一趟掃描同時做兩件事：

    total = 0       # 全程淨值 -> 判斷有沒有解
    tank = 0        # 從目前候選起點出發，開到這裡剩多少
    start = 0

    for i in 0..n-1:
        d = gas[i] - cost[i]
        total += d
        tank += d
        if tank < 0:
            start = i + 1      ★ 換起點
            tank = 0           ★ 重新開始累積

    return start if total >= 0 else -1

【★★ 核心：為什麼 tank < 0 時可以「跳過中間所有站」？】

    假設從 start 出發，走到 i 時 tank 第一次變負。

    這代表：對所有 k 在 [start, i-1]，
        diff[start..k] >= 0            （不然更早就負了）

    現在考慮從中間某一站 m（start < m <= i）出發：

        從 m 走到 i 的和
            = diff[start..i] - diff[start..m-1]
              ^^^^^^^^^^^^^^   ^^^^^^^^^^^^^^^^^
              < 0（已知）        >= 0（上面推出來的）

            <= diff[start..i]  <  0

        所以【從 m 出發，走到 i 也一定會變負】✔

    -> start..i 這些起點【全部可以排除】
    -> 直接跳到 i+1

    【這就是為什麼一趟 O(n) 就夠，
      而不用對每個起點都試一遍 O(n²)。】

【這個論證叫做「交換論證」或「排除論證」，
  是證明貪心正確性的標準手法。】"""),
 ],
 "approaches": [
   ap("解法一", "一趟貪心（標準答案）", [
     ("c", S["p134_greedy"]),
     "<strong>九行，O(n) 時間、O(1) 空間。</strong>",
     ("h", "為什麼最後可以直接 <code>return start</code>，不用再驗證一次？"),
     ("c", """因為：

    (a) total >= 0 保證【有解】（引理二）
    (b) 題目保證解【唯一】
    (c) 我們的貪心把「所有不可能的起點」都排除了

    所以剩下的 start 就是那個唯一解 ✔

【嚴格一點的論證】：

    最後一次「換起點」之後，tank 一路都 >= 0，
    代表從 start 走到 n-1 都沒問題。

    而從 n-1 繞回 start 的那一段，
    它的和 = total - (start 到 n-1 的和) = total - tank

    因為 total >= 0 而 tank >= 0... 
    這裡需要更仔細的論證，
    但關鍵是「被排除掉的那些前綴，它們的和都是負的」，
    所以繞回來的那一段補得回來。

    完整的證明在「追問一」。

【面試時的說法】：
    「total >= 0 保證有解，貪心排除了所有不可能的起點，
      題目又保證唯一，所以剩下的就是答案。」

    這樣講就夠了。""",),
     ("h", "為什麼 <code>tank</code> 要歸零而不是繼續累積？"),
     "因為 <code>tank</code> 的語意是<strong>「從【目前的候選起點】出發到這裡剩多少」</strong>。",
     "<strong>換了起點就要重新開始算</strong> —— 不歸零的話，"
     "<strong>前面那段（已經被排除的）的虧損會被錯誤地帶進來。</strong>",
   ], "O(n)", "O(1)", "掃一遍", "三個變數", optimal=True),

   ap("解法二", "暴力枚舉每個起點（先講這個）", [
     ("c", S["p134_brute"]),
     "<strong>O(n²) 時間。<code>n = 10⁵</code> 時是 10¹⁰ —— 一定逾時。</strong>",
     ("c", """【但它有兩個價值】：

    1. 面試時三十秒就能寫完，先確保「有一個對的答案」

    2. 它是驗證貪心解的最好工具 ——
       這個網站的每一題都是這樣測的：
       用暴力解當「參考實作」，隨機跑幾千次比對。

【for-else 這個 Python 語法】：

    for k in range(n):
        ...
        if tank < 0:
            break
    else:
        return start        # 【沒有 break】才會執行

    for-else 的 else 是「迴圈正常跑完（沒被 break）時執行」。

    這個語法很少見，但在「搜尋失敗才做某事」的場合很好用。

    （很多人覺得這個 else 的命名很糟 ——
      叫 nobreak 會清楚得多。）""",),
   ], "O(n²)", "O(1)", "每個起點試一圈", "幾個變數"),

   ap("解法三", "找「前綴和最小」的位置（另一個角度）", [
     ("c", S["p134_minprefix"]),
     ("h", "★ 這個視角更直觀"),
     ("c", """把 diff 的前綴和畫成一條折線：

        prefix[i] = diff[0] + diff[1] + ... + diff[i]

    從起點 s 出發能繞完一圈
        ⟺ 從 s 開始的所有環狀前綴和都 >= 0
        ⟺ 【prefix[s-1] 是整條折線的最小值】

    為什麼？

        從 s 出發、走到 j 的油量
          = prefix[j] - prefix[s-1]

        要它 >= 0 對所有 j 成立
          ⟺ prefix[s-1] <= prefix[j] 對所有 j
          ⟺ prefix[s-1] 是最小值 ✔

    所以：【找到前綴和的最低點，它的下一站就是答案】。

    程式碼：
        追蹤 min_sum 和 min_idx（= 最低點的下一個位置）

【這個「最低點的下一站」的說法，
  和解法一的「tank 變負就換起點」其實是同一件事】——

    tank 變負的那一刻，正是「前綴和創新低」的時候。

    兩個解法是同一個演算法的兩種說法。

【為什麼要 min_idx % n？】

    如果最低點是最後一站（i = n-1），
    min_idx 會是 n -> 取模變回 0 ✔"""),
     "<strong>O(n) 時間、O(1) 空間，和解法一相同。</strong>"
     "<strong>挑一個你覺得比較好解釋的講。</strong>",
   ], "O(n)", "O(1)", "掃一遍", "三個變數"),
 ],
 "compare": (["解法", "時間", "空間", "好證明嗎", "備註"],
   [["一、一趟貪心", "O(n)", "O(1)", "要交換論證", "標準答案"],
    ["二、暴力枚舉", "O(n²)", "O(1)", "不用證", "驗證用"],
    ["三、找前綴和最低點", "O(n)", "O(1)", "★ 最直觀", "同一個演算法的另一種說法"]]),
 "edges": [
   "<strong>只有一站</strong> <code>gas=[5], cost=[4]</code> → <code>0</code>。",
   "<strong>只有一站但油不夠</strong> <code>gas=[4], cost=[5]</code> → <code>-1</code>。",
   "<strong>總油量剛好等於總花費</strong> → 有解（<code>total == 0</code> 也算 <code>>= 0</code>）。"
   "<strong>寫成 <code>total > 0</code> 會漏掉這種情況 —— 範例 1 就是。</strong>",
   "<strong>第 0 站就是答案</strong> <code>gas=[3,1,1], cost=[1,2,2]</code> → <code>0</code>。",
   "<strong>最後一站是答案</strong> → <code>start = n-1</code>，解法三要記得取模。",
   "<strong><code>tank</code> 變負時忘了歸零</strong> → 前面的虧損被帶進來，答案錯。",
   "<strong>用 <code>total > 0</code> 而不是 <code>>= 0</code></strong> → "
   "<strong>剛好打平的情況會誤判成 -1。</strong>",
   "<strong>10⁵ 站</strong> → 暴力法 10¹⁰ 次，必定逾時。",
 ],
 "follow": [
   ("h", "追問一：怎麼證明「total ≥ 0 就一定有解」？"),
   ("c", """用「前綴和最低點」的視角最好證（解法三）：

    設 prefix[i] = diff[0] + ... + diff[i]，prefix[-1] = 0

    令 m 是使 prefix[m] 最小的索引（有並列就取最後一個）。

    宣稱：從 s = m + 1 出發可以繞完一圈。

    證明：從 s 出發走到 j 的油量是

        (a) j >= s 時：prefix[j] - prefix[m]  >= 0
            （因為 prefix[m] 是最小值）✔

        (b) j < s 時（已經繞過頭了）：
            油量 = (prefix[n-1] - prefix[m]) + prefix[j]
                 = total - prefix[m] + prefix[j]

            因為 total >= 0 而 prefix[j] >= prefix[m]，
            所以 = total + (prefix[j] - prefix[m]) >= 0 ✔

    兩種情況都 >= 0 -> 可以繞完一圈 ✔

【這個證明的核心是「找到那個最低點」——
  它把「環狀」的困難轉化成「線性」的最小值問題。】""",),
   ("h", "追問二：如果解不唯一呢？"),
   "<strong>題目保證唯一，但如果不唯一（例如所有 <code>diff</code> 都是 0），"
   "貪心會回傳 <code>0</code></strong>（因為 <code>tank</code> 從來沒變負）。",
   "<strong>解法三會回傳「最後一個最低點的下一站」</strong> —— "
   "<strong>兩者可能不同，但都是合法答案。</strong>"
   "<strong>「保證唯一」這個條件讓我們不用煩惱要回傳哪一個。</strong>",
   ("h", "追問三：如果要找「所有可行的起點」呢？"),
   "<strong>算出所有前綴和，找出「等於最小值」的那些位置，它們的下一站都是可行起點。</strong>",
   "<strong>O(n) 時間</strong>（前提是 <code>total >= 0</code>）。"
   "<strong>如果 <code>total < 0</code>，一個可行起點都沒有。</strong>",
   ("h", "追問四：這個貪心和第 53 題（最大子陣列）有什麼關係？"),
   ("c", """非常像！

    第 53 題（Kadane）：
        cur = max(x, cur + x)
        —— 「cur 變負就從頭開始」

    第 134 題：
        if tank < 0: tank = 0; start = i + 1
        —— 「tank 變負就從頭開始」

    【兩者都是「累積值變負就重置」】。

    差別：
        53 題要的是「最大的那一段和」
        134 題要的是「重置後最後一個起點」

【共同的直覺】：

    「一段【負】的前綴，對後面只有害處 ——
      把它丟掉永遠不會更差。」

    這個直覺在第 121、53、134 題都成立。

    它成立的條件是：
        「起點可以自由選擇」+「累積是可加的」""",),
 ],
 "related": [
   "<strong>第 53 題 Maximum Subarray</strong> —— 同樣的「變負就重置」",
   "<strong>第 121 題 Best Time to Buy and Sell Stock</strong> —— 同樣的差分轉換",
   "<strong>第 135 題 Candy</strong> —— 另一個需要證明的貪心",
   "<strong>第 55 題 Jump Game</strong> —— 另一個一趟掃描的貪心",
 ],
 "check": [
   "<code>diff[i] = gas[i] - cost[i]</code> 這個轉換讓問題變成什麼？",
   "<code>tank &lt; 0</code> 時，為什麼「從 <code>start</code> 到 <code>i</code>」的所有起點都可以一次排除？",
   "怎麼證明 <code>total >= 0</code> 就一定有解？",
   "<code>total > 0</code> 和 <code>total >= 0</code> 差在哪個測資？",
 ],
})
print("P134 written")

# ==================== 135. Candy ====================
S["p135_two"] = '''class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n                     # 每個人至少一顆

        # 由左往右：只管「比左邊高就要比左邊多」
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1

        # 由右往左：只管「比右邊高就要比右邊多」，取 max 才不會破壞第一輪的結果
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)

        return sum(candy)'''

S["p135_slope"] = '''class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1

        total = 1
        up = down = peak = 0                # 目前上坡長度、下坡長度、上坡的頂點高度

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:         # 上坡
                up += 1
                down = 0
                peak = up
                total += 1 + up
            elif ratings[i] == ratings[i - 1]:      # 平地：重新開始
                up = down = peak = 0
                total += 1
            else:                                    # 下坡
                up = 0
                down += 1
                # 下坡每多一階，前面整段下坡都要 +1；
                # 如果下坡比峰還長，峰也要跟著被墊高
                total += 1 + down - (1 if peak >= down else 0)

        return total'''

S["p135_brute"] = '''class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1] * n
        changed = True
        while changed:                      # 反覆鬆弛到穩定為止
            changed = False
            for i in range(n):
                if i > 0 and ratings[i] > ratings[i - 1] and candy[i] <= candy[i - 1]:
                    candy[i] = candy[i - 1] + 1
                    changed = True
                if i + 1 < n and ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:
                    candy[i] = candy[i + 1] + 1
                    changed = True
        return sum(candy)'''


def _p135_ref(r):
    """獨立參考解：反覆鬆弛直到穩定（一定收斂到最小解）。"""
    n = len(r)
    c = [1] * n
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if i > 0 and r[i] > r[i - 1] and c[i] <= c[i - 1]:
                c[i] = c[i - 1] + 1; changed = True
            if i + 1 < n and r[i] > r[i + 1] and c[i] <= c[i + 1]:
                c[i] = c[i + 1] + 1; changed = True
    return sum(c)


_p135 = [S.load(k) for k in ("p135_two", "p135_slope", "p135_brute")]

for r, want in [
    ([1, 0, 2], 5),
    ([1, 2, 2], 4),
    ([1], 1),
    ([1, 2, 3, 4, 5], 15),
    ([5, 4, 3, 2, 1], 15),
    ([1, 3, 2, 2, 1], 7),
    ([1, 2, 87, 87, 87, 2, 1], 13),
]:
    assert _p135_ref(r) == want, ("P135 ref", r, _p135_ref(r))
    for sol in _p135:
        assert sol.candy(list(r)) == want, ("P135", r, sol)

for _ in range(6000):
    n = random.randrange(1, 12)
    r = [random.randint(0, 4) for _ in range(n)]
    want = _p135_ref(r)
    for sol in _p135:
        got = sol.candy(list(r))
        assert got == want, ("P135 random", r, want, got, sol)
print("P135 solutions OK")

_P135_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">兩個限制（比左邊高要更多、比右邊高也要更多）分開處理，最後取 max —— 這是本題的全部。</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">ratings = [1, 3, 2, 2, 1]</text>
            <g font-size="13" text-anchor="middle">
              <text x="60" y="80" fill="var(--text-muted)" font-size="11" text-anchor="start">評分：</text>
              <text x="160" y="80" fill="var(--text-muted)">1</text><text x="240" y="80" fill="var(--text-muted)">3</text><text x="320" y="80" fill="var(--text-muted)">2</text><text x="400" y="80" fill="var(--text-muted)">2</text><text x="480" y="80" fill="var(--text-muted)">1</text>
              <text x="60" y="118" fill="var(--accent)" font-size="11" text-anchor="start">左→右：</text>
              <text x="160" y="118" fill="var(--accent)">1</text><text x="240" y="118" fill="var(--accent)">2</text><text x="320" y="118" fill="var(--accent)">1</text><text x="400" y="118" fill="var(--accent)">1</text><text x="480" y="118" fill="var(--accent)">1</text>
              <text x="60" y="156" fill="#ff8a65" font-size="11" text-anchor="start">右→左：</text>
              <text x="160" y="156" fill="#ff8a65">1</text><text x="240" y="156" fill="#ff8a65">1</text><text x="320" y="156" fill="#ff8a65">2</text><text x="400" y="156" fill="#ff8a65">2</text><text x="480" y="156" fill="#ff8a65">1</text>
              <text x="60" y="196" fill="var(--gold)" font-size="11" text-anchor="start">取 max：</text>
              <text x="160" y="196" fill="var(--gold)" font-size="15">1</text><text x="240" y="196" fill="var(--gold)" font-size="15">2</text><text x="320" y="196" fill="var(--gold)" font-size="15">2</text><text x="400" y="196" fill="var(--gold)" font-size="15">2</text><text x="480" y="196" fill="var(--gold)" font-size="15">1</text>
            </g>
            <text x="540" y="196" fill="var(--gold)" font-size="12" text-anchor="start">總和 = 8？</text>
            <text x="20" y="230" fill="#ff8a65" font-size="12">等等 —— 正確答案是 7。上面的 max 算出 1+2+2+2+1 = 8，哪裡不對？</text>
            <text x="20" y="256" fill="var(--text-muted)" font-size="12">重算「右→左」：i=3 時 ratings[3]=2 不大於 ratings[4]=1？ 2 &gt; 1 ✔ 所以 candy[3] = candy[4]+1 = 2</text>
            <text x="20" y="280" fill="var(--text-muted)" font-size="12">i=2：ratings[2]=2，ratings[3]=2 —— 【相等，不大於】→ candy[2] 保持 1</text>
            <text x="20" y="306" fill="var(--gold)" font-size="12">修正後：右→左 = [1, 1, 1, 2, 1]　→　取 max = [1, 2, 1, 2, 1]　→　總和 7 ✔</text>
            <line x1="20" y1="330" x2="620" y2="330" stroke="var(--border)"/>
            <text x="20" y="358" fill="var(--accent)" font-size="12">★ 相等的評分【沒有任何限制】—— 兩個人分數一樣時，糖果數可以隨便，各給 1 顆最省。</text>
            <text x="20" y="384" fill="#ff8a65" font-size="12">這是本題最容易錯的地方：把「≥」寫成「&gt;」或反過來，答案就差很多。</text>
            <text x="20" y="414" fill="var(--accent)" font-size="12">★ 第二輪為什麼要 max 而不是直接賦值？因為直接賦值會把第一輪的結果蓋掉 ——</text>
            <text x="20" y="438" fill="var(--text-muted)" font-size="12">一個人可能同時比左邊和右邊都高（山峰），兩個限制都要滿足，所以取較大的那個。</text>'''

emit({
 "num": 135, "slug": "candy",
 "en": [
   "There are <code>n</code> children standing in a line. Each child is assigned a rating value "
   "given in the integer array <code>ratings</code>.",
   "You are giving candies to these children subjected to the following requirements:",
   ("raw", "<ul><li>Each child must have <strong>at least one</strong> candy.</li>"
           "<li>Children with a higher rating get <strong>more</strong> candies than their "
           "<strong>neighbors</strong>.</li></ul>"),
   "Return <em>the <strong>minimum</strong> number of candies you need to have to distribute "
   "the candies to the children</em>.",
 ],
 "zh": [
   "有 <code>n</code> 個小孩站成一排，第 <code>i</code> 個小孩的評分是 <code>ratings[i]</code>。",
   "分糖果的規則：",
   ("ul", [
     "每個小孩<strong>至少要有一顆</strong>糖。",
     "<strong>評分比相鄰小孩高的，糖果也要比他多。</strong>",
   ]),
   "回傳<strong>最少</strong>需要準備幾顆糖。",
   ("note", "★ 注意：評分「相等」時沒有任何限制", [
     "規則說的是「<strong>比</strong>相鄰的<strong>高</strong>」——"
     "<strong>相等的話，兩邊誰多誰少都可以。</strong>",
     "所以 <code>ratings = [1, 2, 2]</code> 的答案是 "
     "<code>1 + 2 + 1 = 4</code>，<strong>不是 <code>1 + 2 + 2</code></strong>。",
     "<strong>這是本題第一名的陷阱。</strong>",
   ]),
 ],
 "pre": [
   ("note", "★ 為什麼「一趟掃描」不夠？", [
     ("c", """限制其實有【兩個方向】：

    (a) ratings[i] > ratings[i-1]  ->  candy[i] > candy[i-1]
    (b) ratings[i] > ratings[i+1]  ->  candy[i] > candy[i+1]

    一趟由左往右只能處理 (a)。

    反例：ratings = [1, 0]

        由左往右：candy = [1, 1]
            0 不大於 1，所以不用調 -> [1, 1]

        但 ratings[0] = 1 > ratings[1] = 0，
        所以 candy[0] 必須 > candy[1] ✘

        正確答案是 [2, 1]，總和 3。

【所以要掃兩趟】：
    第一趟由左往右，處理「比左邊高」
    第二趟由右往左，處理「比右邊高」
    每個位置取兩者的 max

【★ 為什麼「取 max」就同時滿足兩個限制？】

    第一趟保證了 candy_L 滿足限制 (a)
    第二趟保證了 candy_R 滿足限制 (b)

    取 max(candy_L[i], candy_R[i]) 之後：

        限制 (a)：如果 ratings[i] > ratings[i-1]，
            則 candy_L[i] = candy_L[i-1] + 1
            而 max[i] >= candy_L[i] = candy_L[i-1] + 1

            但我們要的是 max[i] > max[i-1]，
            而 max[i-1] 可能來自 candy_R[i-1]（比 candy_L[i-1] 大）...

        —— 這裡需要更仔細的論證，見「追問一」。

    結論是【確實成立】，而且取 max 給出的是【最小解】。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：ratings = [1,0,2]
  輸出：5
  說明：分配 [2,1,2]。
        第 0 個比第 1 個高 -> 2 > 1 ✔
        第 2 個比第 1 個高 -> 2 > 1 ✔

範例 2
  輸入：ratings = [1,2,2]
  輸出：4
  說明：分配 [1,2,1]。
        【第 2 個和第 1 個評分【相等】，所以沒有限制 ——
          給 1 顆就好，不用給 2 顆。】
        這是本題最容易錯的測資。""",
 "constraints": [
   "<code>n == ratings.length</code>",
   "1 ≤ <code>n</code> ≤ 2 × 10⁴",
   "0 ≤ <code>ratings[i]</code> ≤ 2 × 10⁴",
 ],
 "idea": [
   ("fig", _P135_FIG, "0 0 640 456"),
   ("c", """【兩趟掃描】

    candy = [1] * n                         每個人至少一顆

    # 第一趟：由左往右
    for i in 1..n-1:
        if ratings[i] > ratings[i-1]:
            candy[i] = candy[i-1] + 1

    # 第二趟：由右往左
    for i in n-2..0:
        if ratings[i] > ratings[i+1]:
            candy[i] = max(candy[i], candy[i+1] + 1)
                       ^^^^^^^^^^^^
                       ★ 一定要 max，不能直接賦值

    return sum(candy)

【★ 第二趟為什麼要 max？】

    考慮 ratings = [1, 3, 2]：

        第一趟：[1, 2, 1]
            （3 > 1 所以 candy[1] = 2；2 不大於 3 所以 candy[2] = 1）

        第二趟（i = 1）：ratings[1]=3 > ratings[2]=2
            直接賦值：candy[1] = candy[2] + 1 = 2
            取 max：  candy[1] = max(2, 2) = 2

            這個例子看不出差別。

    考慮 ratings = [1, 2, 3, 2]：

        第一趟：[1, 2, 3, 1]

        第二趟（i = 2）：3 > 2 -> candy[2] = max(3, 1+1) = 3 ✔
            直接賦值的話會變成 2 -> 破壞了 candy[2] > candy[1] ✘

    【max 的意思是「兩個限制都要滿足，取比較嚴格的那個」。】

【第二趟為什麼要由右往左？】

    因為 candy[i] 依賴 candy[i+1]（右邊的），
    所以要先算好右邊的。

    第一趟依賴左邊 -> 由左往右
    第二趟依賴右邊 -> 由右往左

    【方向永遠由「依賴誰」決定。】"""),
 ],
 "approaches": [
   ap("解法一", "兩趟掃描 + 取 max（標準答案）", [
     ("c", S["p135_two"]),
     "<strong>八行，O(n) 時間、O(n) 空間。</strong>"
     "<strong>這是絕大多數人會寫、也應該寫的答案。</strong>",
     ("h", "為什麼用 <code>&gt;</code> 而不是 <code>&gt;=</code>？"),
     ("c", """規則是「評分【比】鄰居【高】，糖果就要【更多】」。

    評分相等時 -> 沒有任何限制 -> 各給 1 顆最省 ✔

    寫成 >= 的話：

        ratings = [1, 2, 2]
        第一趟（用 >=）：candy = [1, 2, 3]  ✘
        正確應該是 [1, 2, 1]，總和 4 而不是 6。

【這是本題第一名的 bug】——

    因為「相等時該怎麼辦」在題目裡是【隱含】的：
    規則只說了「比較高」的情況，沒說相等。

    【題目沒說的情況 = 沒有限制 = 用最省的做法。】

    讀題時要特別注意這種「規則只涵蓋部分情況」的敘述。""",),
     ("h", "空間能不能降到 O(1)？"),
     "<strong>可以（解法二），但程式碼複雜很多。</strong>"
     "<strong>n = 2×10⁴ 時 O(n) 空間完全沒問題，所以實務上不需要。</strong>",
     "<strong>面試時寫這個版本，如果被追問「能不能 O(1) 空間」再說解法二的想法。</strong>",
   ], "O(n)", "O(n)", "兩趟掃描", "candy 陣列", optimal=True),

   ap("解法二", "一趟掃描 + 坡度計數（O(1) 空間）", [
     ("c", S["p135_slope"]),
     ("h", "把序列看成一連串的「上坡 / 下坡 / 平地」"),
     ("c", """     /\\      /
    /  \\    /
   /    \\  /
  up   down up

    上坡長度 up：連續上升了幾階
    下坡長度 down：連續下降了幾階
    peak：這一段上坡的頂點高度（= 上坡結束時的 up）

【上坡時】：
    total += 1 + up

    第 up 階要拿 up + 1 顆（因為每一階都要比前一階多）。

【下坡時】：
    total += 1 + down - (1 if peak >= down else 0)

    下坡的第 down 階要拿 1 顆，
    但前面已經發出去的整段下坡都要各 +1 顆
    -> 所以這一步實際增加 down 顆。

    【但如果下坡比峰還長】，峰本身也要被墊高
    -> 再多 1 顆

    peak >= down 時峰還夠高，不用墊 -> 減掉那個 1
    peak <  down 時峰不夠高，要墊  -> 不減

【平地時】：
    up = down = peak = 0        全部重置（相等沒有限制）
    total += 1

【這個解法很難第一次就寫對】——

    它的價值在於展示「把序列拆成單調段」這個視角，
    以及 O(1) 空間是可能的。

    但實務上和面試裡，解法一永遠是更好的選擇：
    八行 vs 二十行，而且不容易錯。

    【能寫出短而正確的程式碼，比能寫出最省空間的更重要。】"""),
   ], "O(n)", "O(1)", "一趟掃描", "幾個計數器"),

   ap("解法三", "反覆鬆弛到穩定（最笨，但一定對）", [
     ("c", S["p135_brute"]),
     ("c", """反覆掃描，只要有任何一個位置違反限制就修正，
直到一輪掃描下來都沒有改變為止。

【為什麼一定會停？】

    每次修正都讓某個 candy[i] 【嚴格變大】，
    而 candy[i] 有上界（最多 n）。

    所以總修正次數 <= n²，一定會收斂 ✔

【為什麼收斂到的是【最小】解？】

    因為我們從「全部是 1」（絕對的下界）開始，
    而且【只在必要時】才增加。

    每一步都保持「candy[i] <= 最優解的 candy[i]」這個不變量：
        初始時成立（1 是下界）
        修正時：candy[i] = candy[i-1] + 1
                而最優解也必須 > 它的 candy[i-1] >= 我們的 candy[i-1]
                所以最優解的 candy[i] >= 我們的新值 ✔

    收斂時既滿足所有限制、又不超過最優解 -> 它就是最優解 ✔

【這是「鬆弛法」（relaxation）的標準論證】——

    和 Bellman-Ford 求最短路的正確性證明一模一樣。

【複雜度 O(n²) 最壞】（例如嚴格遞減的序列），
    n = 2×10^4 時會逾時。

    但它是驗證解法一、二的最好工具 ——
    這個網站就是用它當參考實作，
    隨機跑幾千次比對。""",),
   ], "O(n²) 最壞", "O(n)", "反覆鬆弛", "candy 陣列"),
 ],
 "compare": (["解法", "時間", "空間", "好寫嗎", "備註"],
   [["一、兩趟掃描", "O(n)", "O(n)", "★★★", "標準答案，八行"],
    ["二、坡度計數", "O(n)", "O(1)", "★☆☆", "空間最省，但難寫對"],
    ["三、反覆鬆弛", "O(n²) 最壞", "O(n)", "★★★", "驗證用"]]),
 "edges": [
   "<strong>只有一個人</strong> → <code>1</code>。",
   "<strong><code>[1,0,2]</code></strong> → <code>5</code>（分配 <code>[2,1,2]</code>）。",
   "<strong><code>[1,2,2]</code></strong> → <code>4</code>，<strong>不是 5</strong>。"
   "<strong>相等沒有限制 —— 本題第一名的陷阱。</strong>",
   "<strong>嚴格遞增</strong> <code>[1,2,3,4,5]</code> → <code>15</code>（<code>1+2+3+4+5</code>）。",
   "<strong>嚴格遞減</strong> <code>[5,4,3,2,1]</code> → <code>15</code>。"
   "<strong>只有一趟由左往右的話會得到 5 —— 這是「必須掃兩趟」的證據。</strong>",
   "<strong>全部相同</strong> <code>[2,2,2]</code> → <code>3</code>（各一顆）。",
   "<strong>山峰</strong> <code>[1,3,2]</code> → <code>4</code>（<code>[1,2,1]</code>）。",
   "<strong>用 <code>&gt;=</code> 而不是 <code>&gt;</code></strong> → 相等時多給糖，答案偏大。",
   "<strong>第二趟直接賦值而不是 <code>max</code></strong> → "
   "<strong>破壞第一趟的結果，答案偏小（而且不合法）。</strong>",
   "<strong>2 × 10⁴ 個嚴格遞減</strong> → 解法三要跑 4 億次，逾時。",
 ],
 "follow": [
   ("h", "追問一：怎麼證明「取 max」給出的是合法且最小的解？"),
   ("c", """【合法性】

    設 L[i] 是第一趟的結果、R[i] 是第二趟（單獨跑）的結果，
    答案 A[i] = max(L[i], R[i])。

    要證：ratings[i] > ratings[i-1] -> A[i] > A[i-1]

        L[i] = L[i-1] + 1
        A[i] >= L[i] = L[i-1] + 1

        而 A[i-1] = max(L[i-1], R[i-1])

        情況一：A[i-1] = L[i-1]
            -> A[i] >= L[i-1] + 1 = A[i-1] + 1 > A[i-1] ✔

        情況二：A[i-1] = R[i-1] > L[i-1]
            R[i-1] > L[i-1] 代表「右邊的限制比較嚴格」，
            也就是 ratings[i-1] > ratings[i]。

            但我們假設 ratings[i] > ratings[i-1] —— 矛盾 ✘
            所以情況二不會發生。

    對稱地，右邊的限制也成立 ✔

【最小性】

    A[i] = max(L[i], R[i])，而 L[i] 和 R[i] 各自都是
    「只考慮單邊限制」時的最小值 ——
    它們都是任何合法解的下界。

    所以 max 也是下界。
    而我們證明了 A 是合法解 -> A 就是最小解 ✔

【「分別算出各個限制的下界，再取 max」
  這個模式，在很多「多重限制求最小」的問題裡都成立。】""",),
   ("h", "追問二：如果改成「環形」排列呢？"),
   "<strong>那就難很多了</strong> —— <strong>兩趟掃描不再夠用，因為沒有「起點」。</strong>",
   ("c", """而且【可能無解】：

    ratings = [1, 2, 3]（環形）

        1 < 2 -> candy[1] > candy[0]
        2 < 3 -> candy[2] > candy[1]
        3 > 1 -> candy[2] > candy[0]     ← 這個沒問題

    這個有解。但如果 ratings = [1, 2, 3] 而且環形相鄰是
    3 和 1 -> 3 > 1 -> candy[2] > candy[0] ✔ 也沒問題。

    真正無解的情況需要「循環的嚴格不等式」，
    而因為 ratings 是固定的數值，
    環上不可能有「一路嚴格遞增又繞回來」——
    所以其實【環形版一定有解】。

    做法：把限制看成有向圖（i -> j 表示 candy[j] > candy[i]），
    答案就是「每個節點的最長路徑長度 + 1」。

    因為圖無環（由數值大小決定方向），
    可以用拓撲排序 + DP，O(n)。

【一般化】：任意的「比較限制圖」都可以這樣解 ——
    這其實就是「DAG 上的最長路徑」。""",),
   ("h", "追問三：如果限制改成「相等的人糖果也要相等」呢？"),
   "<strong>那 <code>[1,2,2]</code> 的答案就會變成 "
   "<code>1 + 2 + 2 = 5</code></strong>。",
   "<strong>做法：先把「相等的相鄰位置」用並查集合併成一個群組，"
   "再對群組做兩趟掃描。</strong>"
   "<strong>但要小心 —— 合併之後可能產生矛盾（無解）。</strong>",
   ("h", "追問四：這個「兩趟掃描」的模式還有哪些題目？"),
   ("ul", [
     "<strong>第 42 題 接雨水</strong> —— 左右各掃一遍求「左邊最高」和「右邊最高」，取 min",
     "<strong>第 238 題 除自身以外的乘積</strong> —— 左前綴積 × 右後綴積",
     "<strong>第 123 題 買賣股票 III</strong> —— 左邊一筆 + 右邊一筆",
     "<strong>第 845 題 陣列中的最長山脈</strong> —— 左邊上坡 + 右邊下坡",
   ]),
   "<strong>共同模式：「答案同時受左右兩側影響」時，分兩趟各處理一側，最後合併。</strong>"
   "<strong>合併的方式（max / min / 乘 / 加）由題目決定。</strong>",
 ],
 "related": [
   "<strong>第 42 題 Trapping Rain Water</strong> —— 同樣的「左右各掃一遍」",
   "<strong>第 238 題 Product of Array Except Self</strong> —— 同上",
   "<strong>第 134 題 Gas Station</strong> —— 另一個需要證明的貪心",
   "<strong>第 845 題 Longest Mountain in Array</strong> —— 上坡下坡的分析",
 ],
 "check": [
   "為什麼「一趟由左往右」不夠？請舉出反例。",
   "評分相等時該怎麼辦？<code>[1,2,2]</code> 的答案是多少？",
   "第二趟為什麼要 <code>max</code> 而不是直接賦值？",
   "怎麼證明「取 max」給出的是最小解？",
 ],
})
print("P135 written")
