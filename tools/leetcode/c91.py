# -*- coding: utf-8 -*-
"""第 91–93 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(91)

# ==================== 91. Decode Ways ====================
S["p91_dp"] = '''class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0

        # dp[i] = s 的前 i 個字元有幾種解碼方式
        dp = [0] * (n + 1)
        dp[0] = 1          # 空字串：一種（什麼都不解）
        dp[1] = 1          # 上面已經確認 s[0] != '0'

        for i in range(2, n + 1):
            # 單獨解 s[i-1]（必須是 1..9）
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            # 和前一位合起來解（必須是 10..26）
            two = int(s[i - 2:i])
            if 10 <= two <= 26:
                dp[i] += dp[i - 2]

        return dp[n]'''

S["p91_rolling"] = '''class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        # 只需要前兩個狀態，用兩個變數滾動
        prev2, prev1 = 1, 1        # dp[0], dp[1]

        for i in range(2, len(s) + 1):
            cur = 0
            if s[i - 1] != "0":
                cur += prev1
            if 10 <= int(s[i - 2:i]) <= 26:
                cur += prev2
            if cur == 0:
                return 0           # 這一位既不能單獨解、也不能合併 -> 整串無解
            prev2, prev1 = prev1, cur

        return prev1'''

S["p91_memo"] = '''from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @lru_cache(maxsize=None)
        def go(i: int) -> int:
            """從位置 i 開始，有幾種解碼方式"""
            if i == n:
                return 1           # 剛好解完 -> 一種
            if s[i] == "0":
                return 0           # '0' 不能當一個字母的開頭

            total = go(i + 1)                        # 單獨解 s[i]
            if i + 1 < n and int(s[i:i + 2]) <= 26:  # 合起來解 s[i:i+2]
                total += go(i + 2)
            return total

        result = go(0)
        go.cache_clear()
        return result'''

_p91 = [S.load(k) for k in ("p91_dp", "p91_rolling", "p91_memo")]


def _p91_ref(s):
    """暴力遞迴當基準。"""
    n = len(s)

    def go(i):
        if i == n:
            return 1
        if s[i] == "0":
            return 0
        t = go(i + 1)
        if i + 1 < n and int(s[i:i + 2]) <= 26:
            t += go(i + 2)
        return t
    return go(0) if n else 0


for s_ in ["12", "226", "06", "0", "10", "27", "100", "101", "1010",
           "2101", "11106", "1", "999", "123123"]:
    e = _p91_ref(s_)
    for sol in _p91:
        assert sol.numDecodings(s_) == e, ("P91", s_, sol, sol.numDecodings(s_), e)
for _ in range(5000):
    s_ = "".join(random.choice("0123") for _ in range(random.randint(1, 10)))
    e = _p91_ref(s_)
    for sol in _p91:
        assert sol.numDecodings(s_) == e, ("P91", s_, sol, sol.numDecodings(s_), e)
print("P91 solutions OK")

_P91_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">s = &quot;226&quot; 的解碼樹：每一步可以吃 1 個或 2 個數字</text>
            <g font-size="13" text-anchor="middle" font-family="monospace">
              <text x="320" y="48" fill="var(--gold)">&quot;226&quot;</text>
              <text x="180" y="100" fill="var(--accent)">2 | &quot;26&quot;</text>
              <text x="470" y="100" fill="var(--accent)">22 | &quot;6&quot;</text>
              <text x="100" y="152" fill="var(--accent)">2, 2 | &quot;6&quot;</text>
              <text x="270" y="152" fill="#ff8a65">2, 26 ✔</text>
              <text x="470" y="152" fill="#ff8a65">22, 6 ✔</text>
              <text x="100" y="204" fill="#ff8a65">2, 2, 6 ✔</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.3">
              <line x1="300" y1="56" x2="204" y2="88"/>
              <line x1="342" y1="56" x2="446" y2="88"/>
              <line x1="160" y1="108" x2="118" y2="140"/>
              <line x1="198" y1="108" x2="250" y2="140"/>
              <line x1="470" y1="108" x2="470" y2="140"/>
              <line x1="100" y1="160" x2="100" y2="192"/>
            </g>
            <text x="20" y="240" fill="#ff8a65" font-size="13">三種解碼：BBF(2,2,6)、BZ(2,26)、VF(22,6) → 答案 3</text>
            <line x1="20" y1="258" x2="620" y2="258" stroke="var(--border)"/>
            <text x="20" y="286" fill="var(--gold)" font-size="12">這棵樹的形狀和費氏數列一模一樣（每個節點最多兩個分支）——</text>
            <text x="20" y="310" fill="var(--text-muted)" font-size="12">所以 dp[i] = dp[i−1] + dp[i−2]，只是兩項各自有「合不合法」的條件。</text>
            <text x="20" y="338" fill="var(--text-muted)" font-size="12">如果沒有任何 &apos;0&apos; 也沒有 &gt; 26 的兩位數，答案就剛好是費氏數。</text>'''

emit({
 "num": 91, "slug": "decode-ways",
 "en": [
   "A message containing letters from <code>A-Z</code> can be <strong>encoded</strong> into "
   "numbers using the mapping <code>'A' -&gt; \"1\"</code>, <code>'B' -&gt; \"2\"</code>, "
   "..., <code>'Z' -&gt; \"26\"</code>.",
   "To <strong>decode</strong> an encoded message, all the digits must be grouped then mapped "
   "back into letters using the reverse of the mapping above (there may be multiple ways). "
   "Note that the grouping <code>\"06\"</code> is invalid because <code>\"6\"</code> is "
   "different from <code>\"06\"</code>.",
   "Given a string <code>s</code> containing only digits, return <em>the <strong>number</strong> "
   "of ways to <strong>decode</strong> it</em>.",
 ],
 "zh": [
   "一段由 <code>A</code>–<code>Z</code> 組成的訊息，可以用下面的對應<strong>編碼</strong>成數字："
   "<code>'A' → \"1\"</code>、<code>'B' → \"2\"</code>、…、<code>'Z' → \"26\"</code>。",
   "<strong>解碼</strong>時要把數字切成若干段，每一段對應一個字母。"
   "<strong>注意 <code>\"06\"</code> 是無效的</strong>（因為 <code>\"6\"</code> 和 "
   "<code>\"06\"</code> 不同，編碼時不會產生前導零）。",
   "給你一個只含數字的字串 <code>s</code>，回傳<strong>有幾種解碼方式</strong>。",
 ],
 "pre": [
   ("note", "'0' 是這題唯一的難點", [
     ("c", """如果沒有 '0'，這題就是純粹的費氏數列。

    "123"  ->  1|2|3, 1|23, 12|3   = 3 種（費氏）

'0' 的兩條規則：

  1. '0' 【不能單獨解碼】
     因為沒有字母對應到 0。

  2. '0' 只能【跟在 1 或 2 後面】組成 "10" 或 "20"
     "30" 無效（沒有第 30 個字母）
     "00" 無效

所以：
    "06"  ->  0 種（'0' 開頭就死了）
    "10"  ->  1 種（只能是 "10" = J）
    "100" ->  0 種（"10" 之後剩一個 '0'，無解）
    "101" ->  1 種（"10" + "1"）
    "110" ->  1 種（"1" + "10"）
    "1010" -> 1 種（"10" + "10"）

轉移式：
    dp[i] = （若 s[i-1] != '0'）    dp[i-1]
          + （若 10 <= s[i-2:i] <= 26） dp[i-2]

    兩項都不成立 -> dp[i] = 0 -> 整串無解"""),
     "<strong>「兩位數必須在 10 到 26 之間」</strong>這個條件同時擋掉了兩件事："
     "<strong>前導零</strong>（<code>\"06\"</code> 的 6 &lt; 10）和"
     "<strong>超過 Z</strong>（<code>\"27\"</code> &gt; 26）。",
   ]),
 ],
 "examples": """範例 1
  輸入：s = "12"
  輸出：2
  說明："AB"（1 2）或 "L"（12）

範例 2
  輸入：s = "226"
  輸出：3
  說明："BBF"（2 2 6）、"BZ"（2 26）、"VF"（22 6）

範例 3
  輸入：s = "06"
  輸出：0
  說明："06" 不能解碼（'0' 不對應任何字母，
        而且不能寫成 "6" 的前導零形式）。""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 100",
   "<code>s</code> 只含數字，<strong>可能包含前導零</strong>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>可能包含前導零</strong> —— 所以 <code>s[0] == '0'</code> 要特別擋，"
       "答案是 0。",
       "<strong>長度到 100</strong>。答案最大是費氏數 <code>F(101)</code>，"
       "大約 <code>5.7 × 10²⁰</code> —— <strong>超過 64 位元整數</strong>！"
       "但題目說「保證答案在 32 位元整數範圍內」（LeetCode 的實際測資會遵守），"
       "所以測資不會給出那麼長的全合法字串。"
       "<strong>Python 沒有這個問題。</strong>",
       "<strong>只有數字</strong>，沒有其他字元要處理。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P91_FIG, "0 0 640 352"),
 ],
 "approaches": [
   ap("解法一", "DP 陣列（最好講解）", [
     ("c", S["p91_dp"]),
     ("h", "為什麼 <code>dp[0] = 1</code>？"),
     ("c", """dp[0] 代表「空字串有幾種解碼方式」。

答案是 1 —— 「什麼都不解」本身就是一種方式。

如果設成 0，那 dp[2] 就算不出「整個兩位數合起來」的那一種：
    dp[2] = dp[1] + dp[0]
    "12" 的答案應該是 2（"1|2" 和 "12"）
    dp[0] = 1 才能貢獻出「12」這一種 ✔
    dp[0] = 0 的話 dp[2] = 1，錯 ✘

這和第 70 題（爬樓梯）的 f(0) = 1 是同一個慣例：
    「什麼都不做」是一種做法。

    也和「0! = 1」「空集合的子集有 1 個」同源。"""),
     ("h", "兩個轉移項的條件"),
     ("c", """項 1：dp[i] += dp[i-1]    當 s[i-1] != '0'

    「s[i-1] 自己當一個字母」
    只要它不是 '0'（1..9 都對應到 A..I）✔

項 2：dp[i] += dp[i-2]    當 10 <= int(s[i-2:i]) <= 26

    「s[i-2] 和 s[i-1] 合起來當一個字母」

    下界 10：排除 "01"..."09"（前導零，編碼時不會產生）
    上界 26：排除 "27"..."99"（沒有那麼多字母）

    注意 int("06") == 6 < 10 -> 被擋掉 ✔
        這一個條件同時處理了「前導零」和「超過 Z」。

兩項都不成立時 dp[i] = 0，而且之後的 dp 也都會是 0 ——
所以「無解」會自動往後傳播。"""),
     ("h", "為什麼 <code>dp[1] = 1</code> 不用檢查？"),
     "因為函式一開始就擋掉了 <code>s[0] == \"0\"</code>。"
     "走到這裡表示 <code>s[0]</code> 是 1–9，只有一種解法 ✔",
   ], "O(n)", "O(n)", "掃一遍", "dp 陣列"),

   ap("解法二", "滾動變數（O(1) 空間）", [
     ("c", S["p91_rolling"]),
     "<code>dp[i]</code> 只依賴 <code>dp[i-1]</code> 和 <code>dp[i-2]</code>，"
     "所以兩個變數就夠 —— <strong>和第 70 題（爬樓梯）完全一樣的滾動</strong>。",
     ("h", "<code>if cur == 0: return 0</code> 這個提前退出"),
     ("c", """如果某一位既不能單獨解、也不能和前一位合併，
那整個字串就無解了 —— 後面算什麼都是 0。

    "100"：
        i=2: s[1]='0' 不能單獨；"10" 在範圍內 -> cur = prev2 = 1
        i=3: s[2]='0' 不能單獨；"00" 不在 [10,26] -> cur = 0
             -> 直接 return 0 ✔

不加這一行也會得到正確答案（0 會一路傳下去），
只是多跑幾輪。

但它也是一個【好的除錯點】——
如果你的程式在某個測資上回傳了非 0 的錯誤答案，
在這裡加一個 print 就能看出是哪一位出問題。"""),
     "<strong>O(1) 空間，這是本題的最佳解。</strong>",
   ], "O(n)", "O(1)", "掃一遍", "兩個變數", optimal=True),

   ap("解法三", "記憶化遞迴（從定義直翻）", [
     ("c", S["p91_memo"]),
     "<code>go(i)</code> = 「從位置 <code>i</code> 開始有幾種解碼方式」。"
     "<strong>這是「從前往後」的視角，和 DP 版的「前 i 個字元」剛好相反</strong> —— "
     "兩種定義都對，挑一個你覺得自然的。",
     ("c", """終止條件 go(n) = 1
    「剛好解完整個字串」-> 這是一條成功的路徑 -> 算一種 ✔

    注意不是 0！如果設成 0，所有路徑都會變成 0。

    這和 dp[0] = 1 是同一個道理（只是方向相反）。

s[i] == '0' -> return 0
    '0' 不能當一個字母的開頭，這條路死了。

兩個分支：
    go(i+1)                          單獨解 s[i]
    go(i+2)  若 int(s[i:i+2]) <= 26  合起來解

    第二個分支不用檢查「>= 10」——
    因為如果 s[i] == '0' 上面已經 return 0 了，
    所以走到這裡 s[i] 一定是 1..9，
    int(s[i:i+2]) 一定 >= 10 ✔

    這是一個很細的簡化，值得注意。"""),
     "<strong>優點</strong>：最接近「問題的定義」，寫起來不用想邊界。"
     "<strong>缺點</strong>：O(n) 的遞迴深度和快取空間。",
   ], "O(n)", "O(n)", "每個位置算一次", "快取 + 遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "方向", "備註"],
   [["一、DP 陣列", "O(n)", "O(n)", "前 i 個字元", "最好講解"],
    ["二、滾動變數", "O(n)", "O(1)", "同上", "最佳解"],
    ["三、記憶化遞迴", "O(n)", "O(n)", "從 i 開始", "最接近定義"]]),
 "edges": [
   "<strong>開頭是 '0'</strong>：<code>\"0\"</code>、<code>\"06\"</code> → 0。<strong>必須特別擋。</strong>",
   "<strong>結尾是 '0'</strong>：<code>\"10\"</code> → 1；<code>\"30\"</code> → 0。",
   "<strong>連續兩個 '0'</strong>：<code>\"100\"</code> → 0。",
   "<strong>'0' 在中間</strong>：<code>\"101\"</code> → 1；<code>\"1010\"</code> → 1。",
   "<strong>兩位數剛好 26 / 27</strong>：<code>\"26\"</code> → 2；<code>\"27\"</code> → 1。",
   "<strong>沒有 '0' 也沒有大於 26 的組合</strong>：<code>\"123123\"</code> → 費氏數。",
   "<strong>全是大數字</strong>：<code>\"999\"</code> → 1（只能一個一個解）。",
   "<strong>單一字元</strong>：<code>\"1\"</code> → 1；<code>\"0\"</code> → 0。",
 ],
 "follow": [
   ("h", "追問一：如果字串裡有 <code>'*'</code>（代表 1–9 的任一個）呢？"),
   "第 639 題（Decode Ways II）。"
   "轉移式的每一項都要<strong>乘上「有幾種可能」</strong>：",
   ("c", """s[i-1] == '*'：
    單獨解 -> 9 種（1..9）-> dp[i] += 9 * dp[i-1]

s[i-2:i] 含 '*'：
    "1*" -> 11..19，9 種
    "2*" -> 21..26，6 種
    "*1" -> 11 或 21，2 種
    "*7" -> 17（27 太大），1 種
    "**" -> 11..19 和 21..26，共 15 種

    每一種要分開處理，程式碼會長很多。

複雜度還是 O(n)，但常數大很多，而且要對 10^9+7 取模。""",),
   ("h", "追問二：如果要「列出所有解碼結果」而不是「數幾種」呢？"),
   "改成回溯，而且複雜度會變成 O(答案數 × n) —— "
   "而答案數是指數級的（費氏數）。",
   "<strong>「數有幾種」和「列出所有」的難度差距，在計數問題裡是普遍現象</strong> —— "
   "前者往往有多項式的 DP，後者一定是指數級的。"
   "（同樣的對照見第 22 題、第 78 題。）",
   ("h", "追問三：這題和爬樓梯（第 70 題）的關係？"),
   ("c", """第 70 題： f(n) = f(n-1) + f(n-2)          無條件
第 91 題： f(n) = [條件1] f(n-1) + [條件2] f(n-2)

完全相同的遞迴結構，只是兩項各自帶了一個「合不合法」的守衛。

這一類「帶條件的費氏」在很多題目都會出現：
    第 91 題   解碼方法
    第 198 題  打家劫舍（f(n) = max(f(n-1), f(n-2) + v)，改成取 max）
    第 746 題  最小花費爬樓梯
    第 1137 題 第 N 個泰波那契數（三項）

先把第 70 題的五種寫法弄熟，
這一整類題就只是「換一個轉移條件」。""",),
   ("h", "追問四：為什麼這個編碼方式本身是有問題的？"),
   "因為它<strong>不是唯一可解碼的（uniquely decodable）</strong> —— "
   "同一串數字可以有多種解讀，這正是本題要數的東西。",
   "<strong>真實的編碼系統會避免這個問題</strong>：",
   ("ul", [
     "<strong>固定長度</strong>：每個字母都用兩位數（<code>\"01\"</code> 到 <code>\"26\"</code>），"
     "那就唯一了",
     "<strong>前綴碼（prefix-free code）</strong>：沒有任何碼字是另一個的前綴 —— "
     "<strong>哈夫曼編碼</strong>就是這樣設計的",
     "<strong>加分隔符</strong>",
   ]),
   "<strong>「唯一可解碼」是編碼理論的基本要求</strong>，"
   "而 Kraft 不等式給出了「什麼樣的碼長分配可以構成前綴碼」的充要條件。"
   "<strong>這題某種意義上是在展示「不好的編碼會發生什麼事」。</strong>",
 ],
 "related": [
   "<strong>第 70 題 Climbing Stairs</strong> —— 無條件版的同一個遞迴",
   "<strong>第 639 題 Decode Ways II</strong> —— 加上萬用字元 <code>'*'</code>",
   "<strong>第 198 題 House Robber</strong> —— 同樣的兩項遞迴，改成取 max",
   "<strong>第 62 題 Unique Paths</strong> —— 另一個計數 DP",
 ],
 "check": [
   "為什麼 <code>dp[0] = 1</code>？設成 0 的話 <code>\"12\"</code> 會算出什麼？",
   "<code>10 &lt;= two &lt;= 26</code> 這個條件同時擋掉了哪兩種情況？",
   "<code>\"100\"</code> 的答案是什麼？請一步一步追出來。",
   "記憶化版本的第二個分支為什麼不用檢查「&gt;= 10」？",
 ],
})
print("P91 written")

# ==================== 92. Reverse Linked List II ====================
S["p92_onepass"] = '''class Solution:
    def reverseBetween(self, head: Optional[ListNode],
                       left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)

        # 走到「要反轉的那一段」的前一個節點
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # 頭插法：把 cur 後面的節點一個一個「摘下來、插到 prev 後面」
        cur = prev.next
        for _ in range(right - left):
            nxt = cur.next            # 要被搬走的節點
            cur.next = nxt.next       # 把它從原位摘掉
            nxt.next = prev.next      # 插到 prev 後面
            prev.next = nxt

        return dummy.next'''

S["p92_cut"] = '''class Solution:
    def reverseBetween(self, head: Optional[ListNode],
                       left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)

        # 1. 找到那一段的「前一個」和「第一個」
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        start = prev.next            # 反轉後會變成這一段的「尾巴」

        # 2. 標準的串列反轉，做 (right - left + 1) 次
        p, cur = None, start
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = p
            p = cur
            cur = nxt
        # 此時 p 是反轉後的「新頭」，cur 是這一段後面的第一個節點

        # 3. 把三段接回去
        prev.next = p
        start.next = cur

        return dummy.next'''

_p92 = [S.load(k) for k in ("p92_onepass", "p92_cut")]


def _p92_ref(vals, left, right):
    a = list(vals)
    a[left - 1:right] = a[left - 1:right][::-1]
    return a


for vals, l, r in [([1, 2, 3, 4, 5], 2, 4), ([5], 1, 1), ([1, 2], 1, 2),
                   ([1, 2, 3], 1, 3), ([1, 2, 3], 2, 3), ([1, 2, 3], 1, 1),
                   ([3, 5], 1, 2)]:
    e = _p92_ref(vals, l, r)
    for sol in _p92:
        g = from_list(sol.reverseBetween(to_list(vals), l, r))
        assert g == e, ("P92", vals, l, r, sol, g, e)
for _ in range(5000):
    n = random.randint(1, 8)
    vals = list(range(n))
    l = random.randint(1, n)
    r = random.randint(l, n)
    e = _p92_ref(vals, l, r)
    for sol in _p92:
        g = from_list(sol.reverseBetween(to_list(vals), l, r))
        assert g == e, ("P92", vals, l, r, sol, g, e)
print("P92 solutions OK")

_P92_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">1→2→3→4→5，left=2, right=4：反轉中間那一段</text>
            <text x="20" y="48" fill="var(--text-muted)" font-size="12">頭插法：把 cur 後面的節點一個一個摘下來，插到 prev 後面</text>
            <g font-size="14" text-anchor="middle">
              <rect x="30" y="64" width="50" height="34" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/>
              <text x="55" y="86" fill="var(--text-muted)" font-size="10">dummy</text>
              <rect x="104" y="64" width="50" height="34" rx="6" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="129" y="87" fill="var(--gold)">1</text>
              <rect x="178" y="64" width="50" height="34" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="203" y="87" fill="var(--accent)">2</text>
              <rect x="252" y="64" width="50" height="34" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="277" y="87" fill="#ff8a65">3</text>
              <rect x="326" y="64" width="50" height="34" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="351" y="87" fill="#ff8a65">4</text>
              <rect x="400" y="64" width="50" height="34" rx="6" fill="none" stroke="var(--border)"/><text x="425" y="87" fill="var(--text-muted)">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="80" y1="81" x2="100" y2="81"/><line x1="154" y1="81" x2="174" y2="81"/>
              <line x1="228" y1="81" x2="248" y2="81"/><line x1="302" y1="81" x2="322" y2="81"/>
              <line x1="376" y1="81" x2="396" y2="81"/>
            </g>
            <text x="129" y="118" fill="var(--gold)" font-size="11" text-anchor="middle">prev</text>
            <text x="203" y="118" fill="var(--accent)" font-size="11" text-anchor="middle">cur（永遠不動）</text>
            <text x="470" y="87" fill="#ff8a65" font-size="11">要搬的</text>
            <line x1="20" y1="136" x2="620" y2="136" stroke="var(--border)"/>
            <g font-family="monospace" font-size="12">
              <text x="40" y="164" fill="var(--gold)">第 1 輪：摘下 3，插到 prev(1) 後面</text>
              <text x="90" y="186" fill="var(--text-muted)">1 → 3 → 2 → 4 → 5</text>
              <text x="40" y="216" fill="var(--gold)">第 2 輪：摘下 4（cur=2 的下一個），插到 prev(1) 後面</text>
              <text x="90" y="238" fill="var(--text-muted)">1 → 4 → 3 → 2 → 5</text>
              <text x="40" y="268" fill="#ff8a65">共 right − left = 2 輪，完成 ✔</text>
            </g>
            <text x="20" y="302" fill="var(--gold)" font-size="12">關鍵：cur 從頭到尾都指著原本的第一個節點（2），它會一路被擠到這一段的尾巴。</text>'''

emit({
 "num": 92, "slug": "reverse-linked-list-ii",
 "en": [
   "Given the <code>head</code> of a singly linked list and two integers <code>left</code> "
   "and <code>right</code> where <code>left &lt;= right</code>, reverse the nodes of the list "
   "from position <code>left</code> to position <code>right</code>, and return "
   "<em>the reversed list</em>.",
   "<strong>Follow up:</strong> Could you do it in one pass?",
 ],
 "zh": [
   "給你一個單向鏈結串列的頭節點 <code>head</code>，以及兩個整數 <code>left</code> 和 "
   "<code>right</code>（<code>left ≤ right</code>），"
   "請把<strong>第 <code>left</code> 到第 <code>right</code> 個節點</strong>反轉，"
   "回傳處理後的串列。（位置從 1 開始算。）",
   "<strong>進階：</strong>能不能只走<strong>一趟</strong>？",
 ],
 "pre": [
   ("note", "三段式：前、中（要反轉）、後", [
     ("c", """1 -> 2 -> 3 -> 4 -> 5，left = 2, right = 4

    [1]  [2 -> 3 -> 4]  [5]
     前       中          後

    反轉中段： 4 -> 3 -> 2

    接回去：   1 -> 4 -> 3 -> 2 -> 5

需要記住四個位置：
    prev  = 前段的最後一個（節點 1）
    start = 中段的第一個（節點 2）—— 反轉後會變成中段的尾巴
    中段反轉後的新頭（節點 4）
    cur   = 後段的第一個（節點 5）

三個接點：
    prev.next = 新頭     (1 -> 4)
    start.next = 後段    (2 -> 5)

為什麼要 dummy node？
    因為 left 可以是 1 —— 那時候「前段」是空的，
    prev 就是 dummy。

    沒有 dummy 的話，「反轉包含頭節點」要另外寫一套 ✘"""),
     "<strong>兩種實作方式</strong>："
     "<strong>頭插法</strong>（一趟，邊走邊反轉）或"
     "<strong>切開 → 反轉 → 接回</strong>（概念最清楚）。",
   ]),
 ],
 "examples": """範例 1
  輸入：head = [1,2,3,4,5], left = 2, right = 4
  輸出：[1,4,3,2,5]

範例 2
  輸入：head = [5], left = 1, right = 1
  輸出：[5]""",
 "constraints": [
   "串列節點數是 <code>n</code>，1 ≤ <code>n</code> ≤ 500",
   "−500 ≤ <code>Node.val</code> ≤ 500",
   "1 ≤ <code>left</code> ≤ <code>right</code> ≤ <code>n</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>位置從 1 開始</strong>（不是 0）。"
       "所以要走到「第 <code>left</code> 個的前一個」，"
       "從 <code>dummy</code> 出發要走 <code>left - 1</code> 步。",
       "<strong><code>left</code> 可以等於 1</strong> —— 反轉包含頭節點。"
       "<strong>這是必須用 dummy 的理由。</strong>",
       "<strong><code>left</code> 可以等於 <code>right</code></strong> —— 什麼都不用做。"
       "兩種解法都自然處理（迴圈跑 0 次），但提前 return 更清楚。",
       "<strong>保證 <code>right ≤ n</code></strong>，所以不用檢查越界。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P92_FIG, "0 0 640 316"),
 ],
 "approaches": [
   ap("解法一", "頭插法（一趟，符合進階要求）", [
     ("c", S["p92_onepass"]),
     ("h", "三行重接，順序絕對不能亂"),
     ("c", """nxt = cur.next            # 記住要搬的那個節點
cur.next = nxt.next       # 把 nxt 從原位摘掉（cur 直接連到 nxt 的下一個）
nxt.next = prev.next      # nxt 接到「目前 prev 後面的那個」
prev.next = nxt           # prev 指向 nxt

為什麼是這個順序？
    每一步都只依賴「還沒被改掉」的指標。

    如果先做 prev.next = nxt，
    那 nxt.next = prev.next 就會變成 nxt.next = nxt（自環）✘

驗證（1 -> 2 -> 3 -> 4 -> 5，prev=1, cur=2）：
    第 1 輪：
        nxt = 3
        cur.next = nxt.next -> 2 -> 4      （3 被摘掉）
        nxt.next = prev.next -> 3 -> 2
        prev.next = nxt      -> 1 -> 3
        結果：1 -> 3 -> 2 -> 4 -> 5 ✔

    第 2 輪：
        nxt = cur.next = 4   （cur 還是 2！）
        cur.next = nxt.next -> 2 -> 5
        nxt.next = prev.next -> 4 -> 3
        prev.next = nxt      -> 1 -> 4
        結果：1 -> 4 -> 3 -> 2 -> 5 ✔"""),
     ("h", "<code>cur</code> 為什麼從頭到尾都不動？"),
     "因為 <code>cur</code> 指的是「中段原本的第一個節點」，"
     "而它<strong>反轉後會變成中段的最後一個</strong> —— 它的位置在邏輯上是固定的（尾巴）。"
     "<strong>我們一直在把它「後面」的節點搬到前面去，所以它會一路被擠到最後。</strong>",
     "<strong>迴圈跑 <code>right - left</code> 次</strong>（不是 <code>+1</code>）—— "
     "因為有 <code>right - left + 1</code> 個節點，但第一個（<code>cur</code>）不用搬。",
     "<strong>一趟、O(1) 空間，符合進階要求。</strong>"
     "<strong>但三行重接的順序很容易寫錯 —— 建議在紙上畫一遍再下筆。</strong>",
   ], "O(n)", "O(1)", "一趟", "只用幾個指標", optimal=True),

   ap("解法二", "切開 → 反轉 → 接回（概念最清楚）", [
     ("c", S["p92_cut"]),
     ("h", "三個步驟，各自對應一個已知的技巧"),
     ("c", """1. 定位
       從 dummy 走 left-1 步 -> prev
       start = prev.next

2. 反轉（就是第 206 題的標準寫法）
       p, cur = None, start
       重複 (right - left + 1) 次：
           nxt = cur.next; cur.next = p; p = cur; cur = nxt

       跑完之後：
           p   = 反轉後的新頭（原本的第 right 個）
           cur = 後段的第一個（原本的第 right+1 個，或 None）
           start = 反轉後的尾巴（它的 next 現在指向 p 的前一個，是錯的）

3. 接回
       prev.next = p        前段接到新頭
       start.next = cur     反轉後的尾巴接到後段

為什麼 start 一定是「反轉後的尾巴」？
    反轉會把順序整個顛倒，
    原本的第一個自然變成最後一個 ✔"""),
     "<strong>優點</strong>：每一步都是「已知正確的元件」—— "
     "定位、第 206 題的反轉、接回。"
     "<strong>如果第 206 題已經寫熟，這個版本幾乎不可能寫錯。</strong>",
     "<strong>「一趟」嗎？</strong>"
     "嚴格說它走了 <code>left-1 + (right-left+1) = right</code> 步，"
     "只碰到每個節點一次 —— <strong>也算一趟</strong>。"
     "兩種解法的實際步數是一樣的。",
     "<strong>面試建議：先寫這個版本（好解釋），"
     "如果面試官特別問「有沒有更精簡的」，再提頭插法。</strong>",
   ], "O(n)", "O(1)", "一趟", "只用幾個指標"),
 ],
 "compare": (["解法", "步驟", "好寫程度", "依賴", "備註"],
   [["一、頭插法", "定位 + 逐個頭插", "★★☆☆☆", "三行重接的順序", "最精簡"],
    ["二、切開反轉接回", "定位 + 反轉 + 接回", "★★★★☆", "第 206 題", "最好解釋"]]),
 "edges": [
   "<strong><code>left == right</code></strong>：<code>([5], 1, 1)</code> → 原樣。"
   "迴圈跑 0 次，自然正確。",
   "<strong>反轉整條</strong>：<code>([1,2,3], 1, 3)</code> → <code>[3,2,1]</code>。",
   "<strong><code>left == 1</code></strong>：<code>([1,2], 1, 2)</code> → <code>[2,1]</code>。"
   "<strong>沒有 dummy 會在這裡出錯。</strong>",
   "<strong><code>right == n</code></strong>：<code>([1,2,3], 2, 3)</code> → <code>[1,3,2]</code>。"
   "後段是空的，<code>start.next = None</code>。",
   "<strong>單一節點</strong>：<code>([5], 1, 1)</code> → <code>[5]</code>。",
   "<strong>兩個節點</strong>：<code>([3,5], 1, 2)</code> → <code>[5,3]</code>。",
   "<strong>重接順序寫錯</strong>：會產生自環，走訪時無限迴圈。"
   "<strong>測試時一定要檢查回傳的串列會不會停。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果要「每 k 個一組反轉」呢？"),
   "第 25 題（Reverse Nodes in k-Group）。"
   "<strong>本質上是「重複做這一題」</strong> —— "
   "每一組都是一次區間反轉，只是要先數夠 k 個。",
   "<strong>三題的關係</strong>：",
   ("c", """第 206 題  反轉整條串列              最基本
第 92 題   反轉中間一段 [left, right]  本題
第 25 題   每 k 個一組反轉             重複做第 92 題

建議的學習順序：206 -> 92 -> 25
每一題都建立在前一題之上。""",),
   ("h", "追問二：頭插法還能用在哪？"),
   "<strong>「頭插法」的本質是「把後面的元素一個一個搬到前面」</strong> —— "
   "它天然產生「反轉」的效果。",
   ("ul", [
     "<strong>建立一個反序的串列</strong>：讀入時每個都插在頭部",
     "<strong>LRU 快取</strong>（第 146 題）：把剛使用的節點移到最前面",
     "<strong>第 25 題</strong>：每一組都用頭插法",
   ]),
   ("h", "追問三：如果是雙向串列呢？"),
   "反轉一段雙向串列時，<strong>每個節點的 <code>prev</code> 和 <code>next</code> 都要交換</strong>，"
   "而且接回去時要處理四個指標（前段的 next、新頭的 prev、"
   "新尾的 next、後段的 prev）。"
   "<strong>更容易寫錯，但邏輯上是一樣的三段式。</strong>",
   ("h", "追問四：這類題目的除錯建議？"),
   ("ul", [
     "<strong>在紙上畫出「改動前」和「改動後」的圖</strong>，標出每個指標",
     "<strong>用最小的例子驗證</strong>（<code>[1,2]</code>、<code>left=1, right=2</code>）",
     "<strong>檢查有沒有自環</strong>：走訪回傳的串列，如果不會停就是有環",
     "<strong>檢查節點總數</strong>：反轉前後的節點數必須相同",
   ]),
   "<strong>本篇的 <code>from_list</code> 就內建了環偵測</strong> —— "
   "這是測試串列題最有價值的一行程式碼。",
 ],
 "related": [
   "<strong>第 206 題 Reverse Linked List</strong> —— 反轉整條，本題的基礎",
   "<strong>第 25 題 Reverse Nodes in k-Group</strong> —— 重複做本題",
   "<strong>第 24 題 Swap Nodes in Pairs</strong> —— k = 2 的特例",
   "<strong>第 61 題 Rotate List</strong> —— 另一種整段重接",
 ],
 "check": [
   "頭插法的三行重接，順序為什麼不能顛倒？先做 <code>prev.next = nxt</code> 會怎樣？",
   "頭插法的 <code>cur</code> 為什麼從頭到尾都不動？它最後會在哪個位置？",
   "迴圈為什麼跑 <code>right - left</code> 次而不是 <code>right - left + 1</code> 次？",
   "為什麼 <code>left</code> 可能等於 1 這件事，決定了必須用 dummy node？",
 ],
})
print("P92 written")
