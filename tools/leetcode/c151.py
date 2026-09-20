# -*- coding: utf-8 -*-
"""第 151–155 題。"""
import random, re
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(151)

# ==================== 151. Reverse Words in a String ====================
S["p151_split"] = '''class Solution:
    def reverseWords(self, s: str) -> str:
        # split() 不帶參數時會自動忽略所有連續空白
        return " ".join(reversed(s.split()))'''

S["p151_manual"] = '''class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        i, n = 0, len(s)

        while i < n:
            while i < n and s[i] == " ":
                i += 1                      # 跳過空白
            if i >= n:
                break
            j = i
            while j < n and s[j] != " ":
                j += 1                      # 找到這個單字的結尾
            words.append(s[i:j])
            i = j

        # 反轉單字順序，用單一空格接起來
        out, k = [], len(words) - 1
        while k >= 0:
            out.append(words[k])
            k -= 1
        return " ".join(out)'''

S["p151_inplace"] = '''class Solution:
    def reverseWords(self, s: str) -> str:
        # 「原地」三部曲（Python 字串不可變，所以先轉成 list 模擬）
        a = list(s)

        def rev(lo, hi):
            while lo < hi:
                a[lo], a[hi] = a[hi], a[lo]
                lo += 1
                hi -= 1

        # 第一步：把多餘的空白壓掉（前導、尾隨、連續）
        write = 0
        i, n = 0, len(a)
        while i < n:
            while i < n and a[i] == " ":
                i += 1
            if i >= n:
                break
            if write:                       # 不是第一個單字 -> 先補一個空格
                a[write] = " "
                write += 1
            start = write
            while i < n and a[i] != " ":
                a[write] = a[i]
                write += 1
                i += 1
            rev(start, write - 1)           # 第二步：反轉【每一個單字】
        del a[write:]

        rev(0, len(a) - 1)                  # 第三步：反轉【整個字串】
        return "".join(a)'''


def _p151_ref(s):
    return " ".join(reversed(s.split()))


_p151 = [S.load(k) for k in ("p151_split", "p151_manual", "p151_inplace")]

for s, want in [
    ("the sky is blue", "blue is sky the"),
    ("  hello world  ", "world hello"),
    ("a good   example", "example good a"),
    ("a", "a"),
    ("   ", ""),
    ("  a  ", "a"),
]:
    assert _p151_ref(s) == want, ("P151 ref", repr(s))
    for sol in _p151:
        assert sol.reverseWords(s) == want, ("P151", repr(s), want, sol.reverseWords(s), sol)

for _ in range(6000):
    parts = []
    for _ in range(random.randrange(0, 6)):
        parts.append(" " * random.randrange(0, 3))
        parts.append("".join(random.choice("abc") for _ in range(random.randrange(1, 4))))
    parts.append(" " * random.randrange(0, 3))
    s = "".join(parts)
    want = _p151_ref(s)
    for sol in _p151:
        assert sol.reverseWords(s) == want, ("P151 random", repr(s), want, sol)
print("P151 solutions OK")

_P151_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 原地反轉三部曲：先壓掉多餘空白 → 反轉每一個單字 → 反轉整個字串。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">s = &quot;  the sky  is blue  &quot;</text>
            <g font-size="13">
              <text x="40" y="88" fill="var(--text-muted)">① 壓掉前導、尾隨、連續空白</text>
              <text x="70" y="116" fill="var(--accent)">&quot;the sky is blue&quot;</text>
              <text x="40" y="154" fill="var(--text-muted)">② 反轉【每一個單字】</text>
              <text x="70" y="182" fill="var(--accent)">&quot;eht yks si eulb&quot;</text>
              <text x="40" y="220" fill="var(--text-muted)">③ 反轉【整個字串】</text>
              <text x="70" y="248" fill="var(--gold)" font-size="15">&quot;blue is sky the&quot;　✔</text>
            </g>
            <line x1="20" y1="276" x2="620" y2="276" stroke="var(--border)"/>
            <text x="20" y="304" fill="var(--accent)" font-size="13">為什麼「反轉兩次」剛好等於「把單字順序倒過來」？</text>
            <text x="40" y="332" fill="var(--text-muted)" font-size="12">整串反轉之後，單字的【順序】倒了，但每個單字內部的字母也倒了。</text>
            <text x="40" y="358" fill="var(--gold)" font-size="12">先把每個單字各自倒一次，整串再倒一次 —— 字母被倒了兩次，等於沒倒 ✔</text>
            <text x="40" y="384" fill="var(--text-muted)" font-size="12">而單字的順序只被倒了一次 → 剛好就是我們要的。</text>
            <text x="20" y="418" fill="#ff8a65" font-size="12">★ 兩次反轉的順序可以對調（先整串、再每個單字），結果一樣。</text>
            <text x="20" y="444" fill="var(--text-muted)" font-size="12">這個「局部反轉 + 全域反轉」的技巧，在第 189 題（輪轉陣列）會以三次反轉的形式再出現。</text>'''

emit({
 "num": 151, "slug": "reverse-words-in-a-string",
 "en": [
   "Given an input string <code>s</code>, reverse the order of the <strong>words</strong>.",
   "A <strong>word</strong> is defined as a sequence of non-space characters. The "
   "<strong>words</strong> in <code>s</code> will be separated by at least one space.",
   "Return <em>a string of the words in reverse order concatenated by a single space.</em>",
   "<strong>Note</strong> that <code>s</code> may contain leading or trailing spaces or multiple "
   "spaces between two words. The returned string should only have a single space separating the "
   "words. Do not include any extra spaces.",
   "<strong>Follow up:</strong> If the string data type is mutable in your language, can you "
   "solve it <strong>in-place</strong> with <code>O(1)</code> extra space?",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，把裡面<strong>單字的順序反轉</strong>。",
   "「單字」是指<strong>一串不含空格的字元</strong>，單字之間至少有一個空格隔開。",
   "回傳<strong>反轉後、用單一空格連接</strong>的字串。",
   ("ul", [
     "<code>s</code> 可能有<strong>前導空格、尾隨空格、或單字間的連續空格</strong>。",
     "回傳的字串<strong>不能有任何多餘的空格</strong>。",
   ]),
   "<strong>進階：</strong>如果你的語言裡字串是可變的，"
   "能不能用 <code>O(1)</code> 額外空間<strong>原地</strong>完成？",
 ],
 "pre": [
   ("note", "★ Python 的一行解，以及它為什麼「不算解」", [
     ("c", S["p151_split"]),
     ("c", """return " ".join(reversed(s.split()))

    s.split()【不帶參數】時會：
        ✔ 依【任意長度的空白】切割
        ✔ 自動忽略前導和尾隨的空白
        ✔ 不會產生空字串

    對照 s.split(" ")【帶參數】：
        "  a  b  ".split(" ")
          -> ['', '', 'a', '', 'b', '', '']   ✘ 一堆空字串

    【這兩者的差別是這題最常見的坑。】

【為什麼一行解「不算解」？】

    因為它完全不處理題目真正在考的東西：
        - 怎麼跳過連續空白
        - 怎麼原地做（進階要求）

    面試時寫這一行，面試官會說
    「很好，現在假設你不能用 split 和 join」。

【但也不要覺得一行解「沒價值」】：
    在真實工作裡，它就是最好的程式碼 ——
    短、清楚、不會錯。

    【面試考的是「你會不會做」，
      工作要的是「用最少的程式碼把事做對」。
      兩者的最佳答案常常不同。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "the sky is blue"
  輸出："blue is sky the"

範例 2
  輸入：s = "  hello world  "
  輸出："world hello"
  說明：前導和尾隨的空格都要去掉。

範例 3
  輸入：s = "a good   example"
  輸出："example good a"
  說明：單字之間的多個空格要壓成一個。""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁴",
   "<code>s</code> 包含英文大小寫字母、數字和空格 <code>' '</code>",
   "<code>s</code> 裡<strong>至少有一個單字</strong>",
 ],
 "idea": [
   ("fig", _P151_FIG, "0 0 640 466"),
   ("c", """【方法 A：切割 + 反轉 + 接起來】

    words = 手動或用 split() 切出所有單字
    return " ".join(reversed(words))

    O(n) 時間、O(n) 空間。

【方法 B：原地三部曲（進階要求）】

    ① 壓掉多餘空白
        把字元往前搬，只在單字之間留一個空格。

    ② 反轉【每一個單字】
        "the sky is blue" -> "eht yks si eulb"

    ③ 反轉【整個字串】
        "eht yks si eulb" -> "blue is sky the" ✔

【★ 為什麼「反轉兩次」剛好對？】

    只做 ③（整串反轉）：
        "the sky" -> "yks eht"
        單字順序對了，但字母也倒了 ✘

    先做 ②（每個單字各自反轉）：
        "the sky" -> "eht yks"
        再做 ③ -> "sky the" ✔

    【字母被反轉了兩次 = 沒反轉；
      單字順序只被反轉一次 = 倒過來了。】

    ② 和 ③ 的順序可以對調，結果一樣。

【這個技巧的一般形式】：

    要「把 k 個區塊的順序倒過來，但區塊內容不變」：
        先各自反轉每個區塊，再反轉整體。

    第 189 題（輪轉陣列）用的是同一招的三次反轉版本。

【Python 的字串不可變】，所以「原地」只能用 list 模擬 ——
    嚴格來說還是 O(n) 空間。

    在 C++（std::string）或 Java（char[]）裡才能真的 O(1)。"""),
 ],
 "approaches": [
   ap("解法一", "<code>split</code> + <code>reversed</code> + <code>join</code>（一行）", [
     ("c", S["p151_split"]),
     "<strong>一行，O(n) 時間、O(n) 空間。</strong>"
     "<strong>在真實工作裡這就是正確答案。</strong>",
     ("h", "<code>split()</code> vs <code>split(\" \")</code>"),
     ("c", """s = "  a  b  "

s.split()       -> ['a', 'b']                      ✔
s.split(" ")    -> ['', '', 'a', '', 'b', '', '']  ✘

【split() 不帶參數時的特殊行為】：

    - 分隔符是「任意長度的連續空白」（空格、tab、換行都算）
    - 自動去掉前後的空白
    - 【不會產生空字串】

    這正好是這題要的行為 ✔

【要修掉 split(" ") 的話】：

    [w for w in s.split(" ") if w]

    也可以，只是多一步過濾。

【反轉的三種寫法】：

    reversed(words)     回傳迭代器，最省記憶體
    words[::-1]         回傳新 list
    words.reverse()     原地反轉，回傳 None（別直接 join 它！）

    " ".join(reversed(words)) 最好 ——
    join 接受任何可迭代物件，不用先建一個新 list。""",),
   ], "O(n)", "O(n)", "切割 + 接合", "單字 list", optimal=True),

   ap("解法二", "手動切割（不用 <code>split</code>）", [
     ("c", S["p151_manual"]),
     ("h", "「跳過空白、找單字」的雙迴圈模式"),
     ("c", """while i < n:
    while i < n and s[i] == " ":     跳過空白
        i += 1
    if i >= n: break                 ★ 全是空白時要擋
    j = i
    while j < n and s[j] != " ":     找單字結尾
        j += 1
    words.append(s[i:j])
    i = j

【這個「外層 while + 兩個內層 while」的結構，
  是所有「手動 tokenize」的標準模式。】

    第 8 題（字串轉整數）、
    第 165 題（比較版本號）、
    第 68 題（文字左右對齊）
    都用得上。

【★ if i >= n: break 不能少】

    s = "   "（全是空白）時：
        第一個內層迴圈把 i 推到 n
        沒有 break 的話，s[i:j] 會是空字串 ->
        words 裡多一個 '' ✘

    （實際上 j 也會是 n，所以 s[n:n] = ""，
      words 會變成 ['']，join 之後是 "" ——
      這題剛好還是對的。
      但在其他情況下就會出錯，所以要擋。）

    本題保證「至少有一個單字」，所以不會全是空白。
    但防禦性地寫還是比較好。""",),
     "<strong>複雜度和解法一相同</strong>，"
     "<strong>但它展示了「不依賴函式庫」的能力。</strong>",
   ], "O(n)", "O(n)", "掃一遍", "單字 list"),

   ap("解法三", "原地三部曲（進階要求）", [
     ("c", S["p151_inplace"]),
     ("h", "★ 第一步「壓掉空白」是最難寫的"),
     ("c", """用「讀寫雙指標」：
    i    = 讀取位置
    write = 寫入位置（永遠 <= i）

    while i < n:
        跳過空白
        if 已經寫過東西: 先補一個空格
        複製整個單字過去
        順便反轉這個單字

    del a[write:]       ★ 把後面的垃圾切掉

【★ if write: 這個判斷】

    「不是第一個單字才補空格」——
    這樣就不會在開頭多一個空格 ✔

    寫成「每個單字後面補空格」的話，
    最後會多一個尾隨空格，還要再刪掉。

    【「在前面補分隔符（除了第一個）」
      比「在後面補分隔符（最後要刪）」乾淨。】

    這和 " ".join() 的行為是一樣的。

【讀寫雙指標是「原地壓縮」的標準手法】：

    第 26 題 刪除排序陣列的重複項
    第 27 題 移除元素
    第 80 題 刪除重複項 II
    第 283 題 移動零

    共同結構：
        for read in range(n):
            if 要保留:
                a[write] = a[read]
                write += 1
        （最後 write 就是新長度）

【在 Python 裡這個「原地」是假的】——
    字串不可變，我們是在 list 上做。

    真正的 O(1) 空間要在 C++ / Java 的 char 陣列上。
    但這個技巧本身值得會。""",),
     "<strong>O(n) 時間。在支援可變字串的語言裡是 O(1) 額外空間。</strong>",
   ], "O(n)", "O(1)（可變字串的語言）", "三趟掃描", "讀寫雙指標"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、split + join", "O(n)", "O(n)", "1", "工作用這個"],
    ["二、手動切割", "O(n)", "O(n)", "18", "展示 tokenize 能力"],
    ["三、原地三部曲", "O(n)", "O(1)*", "28", "進階要求的答案"]]),
 "edges": [
   "<strong>只有一個單字</strong> <code>\"a\"</code> → <code>\"a\"</code>。",
   "<strong>前導空格</strong> <code>\"  a\"</code> → <code>\"a\"</code>。",
   "<strong>尾隨空格</strong> <code>\"a  \"</code> → <code>\"a\"</code>。",
   "<strong>單字間多個空格</strong> <code>\"a   b\"</code> → <code>\"a b\"</code>（只留一個）。",
   "<strong>全是空格</strong> <code>\"   \"</code>（題目保證不會）→ <code>\"\"</code>。",
   "<strong>用 <code>s.split(\" \")</code> 而不是 <code>s.split()</code></strong> → "
   "<strong>結果裡會有一堆空字串。本題第一名的 bug。</strong>",
   "<strong>原地版忘了 <code>del a[write:]</code></strong> → 後面留著舊資料的垃圾。",
   "<strong>原地版在每個單字「後面」補空格</strong> → 最後多一個尾隨空格。",
   "<strong>10⁴ 個字元</strong> → 三種解法都是 O(n)，輕鬆。",
 ],
 "follow": [
   ("h", "追問一：如果要「反轉每個單字的字母，但不改變單字順序」呢？"),
   "<strong>第 557 題</strong>。<strong>只要做三部曲的第 ② 步就好</strong>（反轉每個單字）。",
   "<strong>Python 一行：<code>\" \".join(w[::-1] for w in s.split(\" \"))</code></strong>。",
   "<strong>注意這裡要用 <code>split(\" \")</code>（保留空白結構）而不是 <code>split()</code></strong> —— "
   "<strong>因為那題要求保留原本的空格。剛好和這題相反。</strong>",
   ("h", "追問二：「局部反轉 + 全域反轉」還能用在哪？"),
   ("c", """【第 189 題 輪轉陣列】：把陣列向右轉 k 格

    nums = [1,2,3,4,5,6,7], k = 3
    -> [5,6,7,1,2,3,4]

    三次反轉：
        1. 反轉整個：      [7,6,5,4,3,2,1]
        2. 反轉前 k 個：   [5,6,7,4,3,2,1]
        3. 反轉後 n-k 個： [5,6,7,1,2,3,4] ✔

    O(n) 時間、O(1) 空間。

【一般形式】：

    要把 AB 變成 BA（A、B 是兩段）：
        reverse(A), reverse(B), reverse(整體)

    或者： reverse(整體), reverse(B 的新位置), reverse(A 的新位置)

    【證明】：(A^R B^R)^R = B A  ✔
        （反轉的反轉規則：(XY)^R = Y^R X^R）

【這個恆等式是所有「區塊交換」演算法的基礎】——

    字串旋轉、陣列輪轉、
    甚至某些原地矩陣轉置都用它。""",),
   ("h", "追問三：為什麼 Python 做不到真正的 O(1) 空間？"),
   ("c", """因為 Python 的 str 是【不可變】的 ——
    任何「修改」都是建立一個新字串。

    所以我們只能：
        a = list(s)         O(n) 空間
        ...在 a 上操作...
        return "".join(a)   又一個 O(n)

【什麼語言可以真的 O(1)？】

    C：      char* 直接改
    C++：    std::string 可變（s[i] = c）
    Java：   String 不可變，但 char[] 可以
    Go：     string 不可變，[]byte 可以
    Rust：   String 可變（但要小心 UTF-8 邊界）

【為什麼很多語言的字串是不可變的？】

    ✔ 可以安全地共用（多個變數指向同一份資料）
    ✔ 可以當雜湊表的 key（hash 不會變）
    ✔ 執行緒安全
    ✔ 可以做 interning（相同的字串只存一份）

    代價：每次「修改」都要複製。

    【這就是為什麼「迴圈裡用 += 拼字串」在 Python 裡是 O(n²)】——
    應該用 list + join。""",),
   ("h", "追問四：如果分隔符不只是空格呢？"),
   "<strong>用 <code>re.split(r'\\s+', s.strip())</code></strong> —— "
   "<code>\\s</code> 包含空格、tab、換行、回車等所有空白字元。",
   "<strong>注意要先 <code>strip()</code></strong>，"
   "<strong>否則前導空白會產生一個空字串。</strong>",
   "<strong>其實 Python 的 <code>s.split()</code> 已經這樣做了</strong> —— "
   "<strong>它的分隔符就是「任意連續空白」，而且自動處理前後。"
   "所以這題不需要正規表達式。</strong>",
 ],
 "related": [
   "<strong>第 557 題 Reverse Words in a String III</strong> —— 只反轉每個單字",
   "<strong>第 189 題 Rotate Array</strong> —— 三次反轉的經典",
   "<strong>第 186 題 Reverse Words in a String II</strong> —— 付費題，真正的原地版",
   "<strong>第 26/27/283 題</strong> —— 讀寫雙指標的原地壓縮",
   "<strong>第 8 題 String to Integer</strong> —— 手動 tokenize",
 ],
 "check": [
   "<code>s.split()</code> 和 <code>s.split(\" \")</code> 有什麼不同？哪一個適合這題？",
   "「反轉每個單字 + 反轉整串」為什麼剛好等於「反轉單字順序」？",
   "原地版的第一步（壓空白）用了什麼技巧？為什麼「在前面補空格」比「在後面補」好？",
   "為什麼 Python 做不到真正的 O(1) 空間？哪些語言可以？",
 ],
})
print("P151 written")

# ==================== 152. Maximum Product Subarray ====================
S["p152"] = '''class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = cur_max = cur_min = nums[0]

        for x in nums[1:]:
            if x < 0:
                cur_max, cur_min = cur_min, cur_max   # 負數會把大小顛倒過來
            cur_max = max(x, cur_max * x)             # 要嘛從 x 重新開始
            cur_min = min(x, cur_min * x)
            best = max(best, cur_max)

        return best'''

S["p152_nested"] = '''class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        cur_max = cur_min = nums[0]

        for x in nums[1:]:
            # 三個候選：只取 x、接在最大後面、接在最小後面
            cands = (x, cur_max * x, cur_min * x)
            cur_max = max(cands)
            cur_min = min(cands)
            best = max(best, cur_max)

        return best'''

S["p152_twopass"] = '''class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 從左掃一遍、從右掃一遍，各自累乘（碰到 0 就重置）
        def scan(a):
            best = float('-inf')
            prod = 1
            for x in a:
                prod *= x
                best = max(best, prod)
                if x == 0:
                    prod = 1            # 0 把連乘切斷，重新開始
            return best

        return max(scan(nums), scan(nums[::-1]))'''


def _p152_ref(nums):
    """獨立參考解：枚舉所有子陣列。"""
    n = len(nums)
    best = float("-inf")
    for i in range(n):
        p = 1
        for j in range(i, n):
            p *= nums[j]
            best = max(best, p)
    return best


_p152 = [S.load(k) for k in ("p152", "p152_nested", "p152_twopass")]

for nums, want in [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-2], -2),
    ([0], 0),
    ([-2, 3, -4], 24),
    ([2, -5, -2, -4, 3], 24),
    ([1, 0, -1, 2, 3, -5, -2], 60),
]:
    assert _p152_ref(nums) == want, ("P152 ref", nums, _p152_ref(nums))
    for sol in _p152:
        assert sol.maxProduct(list(nums)) == want, ("P152", nums, want, sol)

for _ in range(6000):
    n = random.randrange(1, 11)
    nums = [random.randint(-4, 4) for _ in range(n)]
    want = _p152_ref(nums)
    for sol in _p152:
        got = sol.maxProduct(list(nums))
        assert got == want, ("P152 random", nums, want, got, sol)
print("P152 solutions OK")

_P152_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 和第 53 題（最大子陣列【和】）的關鍵差別：負負得正 —— 所以「目前最小」也可能變成答案。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">nums = [2, −5, −2, −4, 3]</text>
            <g font-size="12" text-anchor="middle">
              <text x="70" y="88" fill="var(--text-muted)" text-anchor="start">x</text>
              <text x="220" y="88" fill="var(--accent)">cur_max</text>
              <text x="360" y="88" fill="#ff8a65">cur_min</text>
              <text x="500" y="88" fill="var(--gold)">best</text>
            </g>
            <g font-size="12" text-anchor="middle">
              <text x="70" y="118" fill="var(--text-muted)" text-anchor="start">2</text>
              <text x="220" y="118" fill="var(--accent)">2</text><text x="360" y="118" fill="#ff8a65">2</text><text x="500" y="118" fill="var(--gold)">2</text>
              <text x="70" y="148" fill="var(--text-muted)" text-anchor="start">−5</text>
              <text x="220" y="148" fill="var(--accent)">−5</text><text x="360" y="148" fill="#ff8a65">−10</text><text x="500" y="148" fill="var(--gold)">2</text>
              <text x="70" y="178" fill="var(--text-muted)" text-anchor="start">−2</text>
              <text x="220" y="178" fill="var(--accent)">20</text><text x="360" y="178" fill="#ff8a65">−2</text><text x="500" y="178" fill="var(--gold)">20</text>
              <text x="70" y="208" fill="var(--text-muted)" text-anchor="start">−4</text>
              <text x="220" y="208" fill="var(--accent)">8</text><text x="360" y="208" fill="#ff8a65">−80</text><text x="500" y="208" fill="var(--gold)">20</text>
              <text x="70" y="238" fill="var(--text-muted)" text-anchor="start">3</text>
              <text x="220" y="238" fill="var(--accent)">24</text><text x="360" y="238" fill="#ff8a65">−240</text><text x="500" y="238" fill="var(--gold)" font-size="15">24</text>
            </g>
            <text x="40" y="272" fill="#ff8a65" font-size="11">↑ 看 x = −2 這一行：cur_min 從 −10 一口氣翻成 cur_max = 20 —— 這就是「負負得正」。</text>
            <line x1="20" y1="296" x2="620" y2="296" stroke="var(--border)"/>
            <text x="20" y="324" fill="var(--accent)" font-size="13">為什麼要同時追蹤「最大」和「最小」？</text>
            <text x="40" y="352" fill="var(--text-muted)" font-size="12">碰到一個【負數】x 時：</text>
            <text x="60" y="378" fill="var(--text-muted)" font-size="12">　（很大的正數）× x　→　很小的負數</text>
            <text x="60" y="402" fill="var(--gold)" font-size="12">　（很小的負數）× x　→　【很大的正數】← 答案可能在這裡</text>
            <text x="40" y="432" fill="var(--accent)" font-size="12">所以「目前最小的乘積」不是沒用的垃圾 —— 它是下一個最大值的候選來源。</text>
            <text x="20" y="464" fill="#ff8a65" font-size="12">★ 0 會把一切歸零，所以每一步都要考慮「從 x 自己重新開始」（那個 max(x, …)）。</text>'''

emit({
 "num": 152, "slug": "maximum-product-subarray",
 "en": [
   "Given an integer array <code>nums</code>, find a subarray that has the largest product, and "
   "return <em>the product</em>.",
   "The test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，找出<strong>乘積最大</strong>的連續子陣列，"
   "回傳那個<strong>乘積</strong>。",
   "測資保證答案能裝進 32 位元整數。",
   ("note", "「子陣列」是連續的", [
     "<strong>必須是原陣列裡一段<strong>連續</strong>的元素</strong>，不能跳著取。",
     "<strong>而且不能是空的</strong>（至少一個元素）——"
     "所以答案可能是負數（全是負數且只有一個元素時）。",
   ]),
 ],
 "pre": [
   ("note", "★ 和第 53 題（最大子陣列和）的關鍵差別", [
     ("c", """第 53 題（求【和】）用 Kadane：

    cur = max(x, cur + x)
    best = max(best, cur)

    直覺：「前面那段如果是負的，不如丟掉重新開始」。

【為什麼這招在「乘積」上會失敗？】

    因為【負負得正】。

    nums = [-2, 3, -4]

    如果只追蹤「目前最大乘積」：
        x=-2: cur = -2, best = -2
        x=3:  cur = max(3, -2*3) = 3, best = 3
        x=-4: cur = max(-4, 3*-4) = -4, best = 3   ✘

    但正解是 (-2) * 3 * (-4) = 24 ！

    問題出在 x=3 那一步：我們丟掉了 -6（因為它比 3 小），
    但 -6 才是下一步的黃金 —— 乘上 -4 之後變成 24。

【★ 解法：同時追蹤「目前最大」和「目前最小」】

    碰到負數 x 時：
        最大 × x -> 變成很小的負數
        最小 × x -> 變成【很大的正數】✔

    所以「目前最小」不是垃圾，
    它是「下一個最大值」的候選來源。

【這個「同時追蹤兩個極值」的模式，
  在任何「有正負號翻轉」的問題裡都會出現】——

    第 152 題（本題）
    第 1014 題 最佳觀光組合
    任何涉及「乘法」或「減法」的最佳化 DP"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [2,3,-2,4]
  輸出：6
  說明：子陣列 [2,3] 的乘積是 6。

範例 2
  輸入：nums = [-2,0,-1]
  輸出：0
  說明：答案是 0（只取中間那個 0）。
        【不能取 [-2,0,-1] 的乘積 0 嗎？也是 0，一樣。】
        但不能取 [-2,-1]，因為它們不連續（中間隔著 0）。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 2 × 10⁴",
   "−10 ≤ <code>nums[i]</code> ≤ 10",
   "<code>nums</code> 的任意前綴或後綴的乘積都保證能裝進 32 位元整數",
 ],
 "idea": [
   ("fig", _P152_FIG, "0 0 640 484"),
   ("c", """【狀態】
    cur_max = 「以目前這個元素結尾」的子陣列的最大乘積
    cur_min = 「以目前這個元素結尾」的子陣列的最小乘積

【轉移】
    三個候選：
        x                   只取 x 自己（前面全部丟掉）
        cur_max * x         接在「之前的最大」後面
        cur_min * x         接在「之前的最小」後面

    cur_max = max(三者)
    cur_min = min(三者)

【為什麼要「只取 x 自己」這個選項？】

    因為前面可能有 0 把一切歸零，
    或者前面的乘積不管正負都比 x 差。

    例如 nums = [0, 5]：
        x=5: cur_max = max(5, 0*5, 0*5) = 5 ✔
        沒有「只取 x」的話會變成 0 ✘

【解法一的等價寫法（先交換）】

    if x < 0:
        cur_max, cur_min = cur_min, cur_max
    cur_max = max(x, cur_max * x)
    cur_min = min(x, cur_min * x)

    「x 是負數時，最大和最小會互換角色」——
    先換過來，後面就可以照正數的方式寫。

    【兩種寫法完全等價】。
    解法二（列出三個候選）比較不容易想錯，
    解法一比較精簡。

【複雜度】：O(n) 時間、O(1) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "同時追蹤最大最小（先交換的寫法）", [
     ("c", S["p152"]),
     "<strong>八行，O(n) 時間、O(1) 空間。</strong>",
     ("h", "★ <code>if x &lt; 0: swap</code> 為什麼在乘法【之前】？"),
     ("c", """因為 x 是負數時，「乘上 x」會把大小關係整個顛倒：

    a > b  且 x < 0  =>  a*x < b*x

    所以「之前的最大」乘上負數會變成「之後的最小」，
    「之前的最小」乘上負數會變成「之後的最大」。

    先交換，就等於「預先把角色對調」——
    後面的 max/min 就可以照正常的方式算 ✔

【驗證 x = -2，cur_max = 3, cur_min = -6】：

    交換後：cur_max = -6, cur_min = 3
    cur_max = max(-2, -6 * -2) = max(-2, 12) = 12 ✔
    cur_min = min(-2, 3 * -2)  = min(-2, -6) = -6 ✔

    正確 ✔

【不交換直接算會怎樣？】

    cur_max = max(-2, 3 * -2) = max(-2, -6) = -2  ✘
    （漏掉了 -6 * -2 = 12 這個候選）

【所以順序很重要。】

    如果覺得容易搞混，就用解法二
    （把三個候選都列出來，不用管順序）。""",),
     ("h", "為什麼 <code>best</code> 只看 <code>cur_max</code>？"),
     "因為答案是<strong>「最大乘積」</strong> —— <code>cur_min</code> 只是中間變數。",
     "<strong>但 <code>cur_min</code> 必須一路維護</strong>，"
     "<strong>因為它可能在下一步變成 <code>cur_max</code>。</strong>",
     ("h", "初始值為什麼是 <code>nums[0]</code> 而不是 1 或 0？"),
     ("c", """因為子陣列【不能是空的】。

    初始成 1 的話：
        nums = [-2]
        cur_max = max(-2, 1 * -2) = -2 ✔ 剛好對

    但 best 初始成 1 就錯了：
        nums = [-2] -> best = max(1, -2) = 1 ✘
        正確答案是 -2

    【初始成 nums[0] 並從索引 1 開始跑，是最安全的】——
    它保證「至少取一個元素」這個約束。

    這和第 53 題（最大子陣列和）的初始化是同一個道理。""",),
   ], "O(n)", "O(1)", "掃一遍", "三個變數", optimal=True),

   ap("解法二", "列出三個候選（最不容易想錯）", [
     ("c", S["p152_nested"]),
     ("c", """cands = (x, cur_max * x, cur_min * x)
cur_max = max(cands)
cur_min = min(cands)

    不用管 x 的正負 ——
    把所有可能性都列出來，取最大和最小 ✔

【★ 一定要先算好 cands 再賦值】

    錯誤寫法：
        cur_max = max(x, cur_max * x, cur_min * x)
        cur_min = min(x, cur_max * x, cur_min * x)
                         ^^^^^^^ 這裡的 cur_max 已經是【新的】了 ✘

    Python 的 tuple 先求值，所以本文的寫法安全 ✔

    也可以寫成同時賦值：
        cur_max, cur_min = (max(x, cur_max*x, cur_min*x),
                            min(x, cur_max*x, cur_min*x))

    Python 的多重賦值會先算完右邊 -> 也安全 ✔

【這個「先算完所有新值再一起賦值」的原則】，
    在任何「狀態互相依賴」的 DP 裡都適用。

    第 122、123 題的股票狀態機也提過同樣的注意事項。

【推薦這個版本】：
    多一個變數，但完全不用思考正負號的交換 ——
    在面試的壓力下比較不會寫錯。""",),
   ], "O(n)", "O(1)", "掃一遍", "幾個變數"),

   ap("解法三", "左右各掃一遍（另一個視角）", [
     ("c", S["p152_twopass"]),
     ("h", "★ 這個解法背後的觀察"),
     ("c", """【觀察】：答案的那個子陣列，
    它的【左端點】要嘛是陣列開頭、要嘛緊接在一個 0 後面。

    為什麼？

    考慮「最大乘積子陣列」被 0 切開的那些段落。
    在每一段裡（沒有 0），乘積的符號只由「負數的個數」決定。

    如果那一段的負數個數是【偶數】：
        整段的乘積是正的 -> 取整段最好 ✔

    如果是【奇數】：
        必須去掉一個負數（從左端或右端去掉）
        -> 要嘛取「從左端到最後一個負數之前」
           要嘛取「從第一個負數之後到右端」

    這兩種情況，剛好被「從左掃」和「從右掃」涵蓋了 ✔

【所以：】

    從左累乘、記錄最大值（碰到 0 就重置成 1）
    從右累乘、記錄最大值
    取兩者的最大 -> 答案 ✔

【為什麼碰到 0 要重置成 1？】

    0 會讓連乘歸零 ——
    後面的元素應該「重新開始算」。

    注意 best 已經包含了那個 0（prod *= x 之後才 max），
    所以「答案是 0」的情況也涵蓋到了 ✔

【這個解法的價值】：
    ✔ 不用思考「同時追蹤最大最小」
    ✔ 只有 max，沒有 min
    ✘ 要掃兩遍
    ✘ 正確性的論證反而比較繞

    但它展示了一個很有用的思路：
    【先分析「答案長什麼樣」，再設計演算法】。""",),
   ], "O(n)", "O(n)", "掃兩遍", "反轉的副本"),
 ],
 "compare": (["解法", "時間", "空間", "好想嗎", "備註"],
   [["一、最大最小 + 交換", "O(n)", "O(1)", "★★☆", "最精簡"],
    ["二、列出三個候選", "O(n)", "O(1)", "★★★", "最不易錯，推薦"],
    ["三、左右各掃一遍", "O(n)", "O(n)", "★☆☆", "視角有趣"]]),
 "edges": [
   "<strong>單一元素</strong> <code>[-2]</code> → <code>-2</code>。"
   "<strong><code>best</code> 初始成 0 或 1 會答錯。</strong>",
   "<strong>有 0</strong> <code>[-2,0,-1]</code> → <code>0</code>。"
   "<strong>0 會把連乘切斷。</strong>",
   "<strong>奇數個負數</strong> <code>[-2,3,-4]</code> → <code>24</code>。"
   "<strong>只追蹤最大值的話會答 3 —— 本題第一名的 bug。</strong>",
   "<strong>偶數個負數</strong> <code>[-2,-3]</code> → <code>6</code>（整段都取）。",
   "<strong>全是負數</strong> <code>[-1,-2,-3]</code> → <code>6</code>（取前兩個或後兩個）。",
   "<strong>全是 0</strong> <code>[0,0]</code> → <code>0</code>。",
   "<strong>先算 <code>cur_max</code> 再用它算 <code>cur_min</code></strong> → "
   "<strong><code>cur_min</code> 用到了新值，答案錯。</strong>",
   "<strong>2 × 10⁴ 個元素</strong> → O(n) 輕鬆；"
   "<strong>但暴力 O(n²) = 4 億，會逾時。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果改成「乘積最小」呢？"),
   "<strong>完全對稱 —— 只要把最後的 <code>best = max(best, cur_max)</code> "
   "改成 <code>best = min(best, cur_min)</code></strong>。",
   "<strong>因為我們本來就同時維護了兩個極值 ✔</strong>"
   "<strong>「同時追蹤最大最小」這個設計，讓兩個問題共用同一份程式碼。</strong>",
   ("h", "追問二：如果要回傳「是哪一段子陣列」呢？"),
   ("c", """在更新 cur_max 時記錄「這一段的起點」：

    if x > cur_max * x:     # 選擇「重新開始」
        start_max = i
    ...
    if cur_max > best:
        best = cur_max
        ans = (start_max, i)

【但要小心】：cur_max 和 cur_min 各自有自己的起點，
    而且交換時起點也要跟著交換 ——

        if x < 0:
            cur_max, cur_min = cur_min, cur_max
            start_max, start_min = start_min, start_max  ★

    【「把互相關聯的變數一起更新」】——
    忘記同步是這類擴充最常見的 bug。

    （第 121 題的「記錄買賣日」也提過同樣的注意事項。）""",),
   ("h", "追問三：這題和第 53 題（最大子陣列和）的差別可以一般化嗎？"),
   ("c", """【可以】。關鍵在於「運算是否保持大小關係」：

    加法：a > b  =>  a + x > b + x       ✔ 永遠保持
          -> 只要追蹤「最大」就夠（Kadane）

    乘法：a > b  =>  a * x > b * x       ✘ x < 0 時反轉
          -> 必須同時追蹤「最大」和「最小」

【一般原則】：

    如果轉移函式是【單調遞增】的，追蹤一個極值就夠。
    如果它可能【反轉大小關係】，就要追蹤兩個。

    其他例子：
        減法（a - x）：單調 -> 一個
        取相反數：     反轉 -> 兩個
        絕對值：       非單調 -> 要分情況

【這個判斷方式比「背住要追蹤兩個」有用得多】——
    遇到新題目時可以自己推導出來。""",),
   ("h", "追問四：為什麼題目要保證「前綴後綴乘積在 32 位元內」？"),
   ("c", """因為連乘會【爆炸性成長】。

    nums[i] 的範圍是 [-10, 10]，
    n 可以到 2 × 10^4。

    如果全部是 10，乘積是 10^20000 ——
    天文數字。

【在 C++/Java 裡會溢位成垃圾值】（未定義行為或繞回）。

【在 Python 裡不會溢位，但會變得很慢】——
    大整數的乘法不是 O(1)。

    如果真的有 10^20000 這種數，
    每次乘法都要 O(位數) 的時間 ->
    整個演算法退化成 O(n × 位數)。

【題目的保證讓我們可以假設「乘法是 O(1)」】。

    這類「保證中間結果不溢位」的條件，
    在涉及乘法、階乘、指數的題目裡很常見 ——
    讀到時要意識到「它在保護什麼」。""",),
 ],
 "related": [
   "<strong>第 53 題 Maximum Subarray</strong> —— 求和的版本，只要追蹤一個極值",
   "<strong>第 238 題 Product of Array Except Self</strong> —— 另一個乘積題",
   "<strong>第 628 題 三個數的最大乘積</strong> —— 同樣要考慮負負得正",
   "<strong>第 713 題 乘積小於 K 的子陣列</strong> —— 滑動視窗版（但要求正數）",
 ],
 "check": [
   "為什麼 Kadane（只追蹤最大值）在乘積上會失敗？請舉出反例。",
   "碰到負數時，「目前最小」為什麼會變成「下一個最大」的來源？",
   "<code>if x &lt; 0: swap</code> 為什麼要在乘法之前？",
   "什麼樣的運算需要「同時追蹤兩個極值」？判斷準則是什麼？",
 ],
})
print("P152 written")

# ==================== 153 / 154. Find Minimum in Rotated Sorted Array ====================
S["p153"] = '''class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1        # mid 在「左半段（大的那半）」-> 最小值在右邊
            else:
                hi = mid            # mid 可能就是最小值 -> 不能寫 mid - 1

        return nums[lo]'''

S["p153_wrong"] = '''class Solution:
    # 【這是錯的，不要抄】：和 nums[lo] 比較
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[lo]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]'''

S["p154"] = '''class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[hi]:
                hi = mid
            else:
                hi -= 1             # ★ 相等：無法判斷，只能保守地縮小一格

        return nums[lo]'''


def _rot(sorted_vals, k):
    return sorted_vals[k:] + sorted_vals[:k]


_p153 = S.load("p153")
_p153_bad = S.load("p153_wrong")
_p154 = S.load("p154")

for nums, want in [
    ([3, 4, 5, 1, 2], 1),
    ([4, 5, 6, 7, 0, 1, 2], 0),
    ([11, 13, 15, 17], 11),
    ([1], 1),
    ([2, 1], 1),
]:
    assert _p153.findMin(list(nums)) == want, ("P153", nums)
    assert _p154.findMin(list(nums)) == want, ("P154 on distinct", nums)

# 第 153 題：所有元素互不相同
for n in range(1, 13):
    base = sorted(random.sample(range(-50, 50), n))
    for k in range(n):
        a = _rot(base, k)
        assert _p153.findMin(list(a)) == base[0], ("P153 rot", a)
        assert _p154.findMin(list(a)) == base[0], ("P154 rot", a)
for _ in range(4000):
    n = random.randrange(1, 13)
    base = sorted(random.sample(range(-50, 50), n))
    a = _rot(base, random.randrange(n))
    assert _p153.findMin(list(a)) == base[0], ("P153 random", a)

# 錯誤寫法（和 nums[lo] 比）確實會答錯
assert _p153_bad.findMin([3, 1, 2]) != 1 or True   # 先確認它在某些輸入上會錯
_bad_found = False
for n in range(1, 10):
    base = sorted(random.sample(range(-50, 50), n))
    for k in range(n):
        a = _rot(base, k)
        if _p153_bad.findMin(list(a)) != base[0]:
            _bad_found = True
assert _bad_found, "P153 wrong-demo：應該要找得到反例"

# 第 154 題：允許重複
for nums, want in [
    ([1, 3, 5], 1),
    ([2, 2, 2, 0, 1], 0),
    ([1, 1], 1),
    ([3, 3, 1, 3], 1),
    ([10, 1, 10, 10, 10], 1),
]:
    assert _p154.findMin(list(nums)) == want, ("P154", nums, want, _p154.findMin(list(nums)))

for _ in range(6000):
    n = random.randrange(1, 13)
    base = sorted(random.randint(0, 4) for _ in range(n))
    a = _rot(base, random.randrange(n))
    assert _p154.findMin(list(a)) == base[0], ("P154 random", a, base[0])
print("P153 / P154 solutions OK")

_P153_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">旋轉排序陣列長得像「兩段各自遞增」的階梯。最小值就是那個「斷崖」的底部。</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">nums = [4, 5, 6, 7, 0, 1, 2]</text>
            <g stroke="var(--border)" stroke-width="1"><line x1="60" y1="230" x2="560" y2="230"/></g>
            <g font-size="12" text-anchor="middle">
              <rect x="70" y="150" width="50" height="80" fill="none" stroke="var(--accent)"/><text x="95" y="250" fill="var(--accent)">4</text>
              <rect x="140" y="130" width="50" height="100" fill="none" stroke="var(--accent)"/><text x="165" y="250" fill="var(--accent)">5</text>
              <rect x="210" y="110" width="50" height="120" fill="none" stroke="var(--accent)"/><text x="235" y="250" fill="var(--accent)">6</text>
              <rect x="280" y="90" width="50" height="140" fill="none" stroke="var(--accent)"/><text x="305" y="250" fill="var(--accent)">7</text>
              <rect x="350" y="222" width="50" height="8" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="375" y="250" fill="var(--gold)">0</text>
              <rect x="420" y="206" width="50" height="24" fill="none" stroke="#ff8a65"/><text x="445" y="250" fill="#ff8a65">1</text>
              <rect x="490" y="190" width="50" height="40" fill="none" stroke="#ff8a65"/><text x="515" y="250" fill="#ff8a65">2</text>
            </g>
            <text x="375" y="278" fill="var(--gold)" font-size="12" text-anchor="middle">↑ 最小值</text>
            <text x="200" y="76" fill="var(--accent)" font-size="11" text-anchor="middle">左段（大的那半）</text>
            <text x="450" y="176" fill="#ff8a65" font-size="11" text-anchor="middle">右段（小的那半）</text>
            <line x1="20" y1="298" x2="620" y2="298" stroke="var(--border)"/>
            <text x="20" y="326" fill="#ff8a65" font-size="13">★ 為什麼要和 nums[hi] 比，不能和 nums[lo] 比？</text>
            <text x="40" y="354" fill="var(--text-muted)" font-size="12">和 nums[hi] 比：</text>
            <text x="60" y="380" fill="var(--accent)" font-size="12">nums[mid] &gt; nums[hi]　→　mid 一定在【左段】，最小值在 mid 右邊 → lo = mid + 1</text>
            <text x="60" y="404" fill="var(--accent)" font-size="12">nums[mid] ≤ nums[hi]　→　mid 在【右段】（或就是最小值）→ hi = mid</text>
            <text x="40" y="436" fill="#ff8a65" font-size="12">和 nums[lo] 比就分不出來 ——「完全沒旋轉」和「旋轉很多」會長得一樣：</text>
            <text x="60" y="462" fill="var(--text-muted)" font-size="12">[1,2,3]（沒旋轉）和 [3,1,2]（旋轉 2 格）的 nums[mid] 都不大於 nums[lo]，</text>
            <text x="60" y="486" fill="var(--text-muted)" font-size="12">但前者的答案在左邊、後者在右邊 —— 同樣的判斷卻要走相反的方向 ✘</text>'''

emit({
 "num": 153, "slug": "find-minimum-in-rotated-sorted-array",
 "en": [
   "Suppose an array of length <code>n</code> sorted in ascending order is "
   "<strong>rotated</strong> between <code>1</code> and <code>n</code> times. For example, the "
   "array <code>nums = [0,1,2,4,5,6,7]</code> might become:",
   ("raw", "<ul><li><code>[4,5,6,7,0,1,2]</code> if it was rotated <code>4</code> times.</li>"
           "<li><code>[0,1,2,4,5,6,7]</code> if it was rotated <code>7</code> times.</li></ul>"),
   "Given the sorted rotated array <code>nums</code> of <strong>unique</strong> elements, return "
   "<em>the minimum element of this array</em>.",
   "You must write an algorithm that runs in <code>O(log n)</code> time.",
 ],
 "zh": [
   "一個升序排列的陣列被<strong>旋轉</strong>了若干次"
   "（把前面幾個元素搬到後面去）。",
   "例如 <code>[0,1,2,4,5,6,7]</code> 旋轉 4 次會變成 <code>[4,5,6,7,0,1,2]</code>。",
   "給你這個旋轉後的陣列（<strong>所有元素互不相同</strong>），找出<strong>最小值</strong>。",
   "<strong>必須是 <code>O(log n)</code> 的演算法。</strong>",
 ],
 "pre": [
   ("note", "★ 二分搜尋不一定要「已排序」", [
     ("c", """一般的二分搜尋需要「整個陣列有序」。

但二分搜尋真正需要的其實只是：

    【能在 O(1) 內判斷「答案在左半還是右半」】

旋轉排序陣列雖然不是整體有序，
但它有非常強的結構：

    【它是「兩段各自遞增」的，而且左段的所有值都 > 右段的所有值】

        [4, 5, 6, 7 | 0, 1, 2]
         \\_左段_/    \\_右段_/

    最小值就是「右段的第一個」= 那個斷崖的底部。

    只要能判斷 mid 落在哪一段，就能砍掉一半 ✔

【這是「二分搜尋的一般化」】：

    只要存在一個【單調的判定函式】
    （前半都是 False、後半都是 True），
    就能用二分搜尋找到那個分界點。

    第 162 題（尋找峰值）更極端 ——
    那個陣列完全沒有排序，但仍然能二分。"""),
   ]),
   ("note", "★ 為什麼是和 <code>nums[hi]</code> 比，不是 <code>nums[lo]</code>？", [
     ("c", S["p153_wrong"]),
     ("c", """和 nums[lo] 比的版本【是錯的】。

【原因：「完全沒旋轉」這個情況無法區分】

    考慮 [1, 2, 3]（沒旋轉，答案是 nums[0] = 1）：
        lo=0, hi=2, mid=1
        nums[1]=2 > nums[0]=1 -> lo = mid+1 = 2
        迴圈結束，回傳 nums[2] = 3 ✘

    考慮 [3, 1, 2]（旋轉了）：
        lo=0, hi=2, mid=1
        nums[1]=1 > nums[0]=3? 否 -> hi = 1
        lo=0, hi=1, mid=0
        nums[0]=3 > nums[0]=3? 否 -> hi = 0
        回傳 nums[0] = 3 ✘

    兩個都錯。

【和 nums[hi] 比就沒有這個問題】：

    nums[mid] > nums[hi]
        -> mid 一定在【左段】（因為左段的值都比右段大）
        -> 最小值在 mid 【右邊】 -> lo = mid + 1 ✔

    nums[mid] < nums[hi]
        -> mid 在【右段】
        -> 最小值在 mid 或它左邊 -> hi = mid ✔

    （互不相同，所以不會相等。）

    【驗證 [1,2,3]】：
        mid=1: nums[1]=2 > nums[2]=3? 否 -> hi=1
        mid=0: nums[0]=1 > nums[1]=2? 否 -> hi=0
        回傳 nums[0] = 1 ✔

【為什麼 hi 比較好用？】

    因為【最小值永遠在「右段」（或就是整個陣列的開頭）】，
    而 nums[hi] 永遠屬於右段（或者陣列沒旋轉時屬於唯一那段）。

    拿它當「參考點」，比較的結果就永遠有意義。

    nums[lo] 則可能屬於左段也可能屬於右段 —— 資訊不足 ✘"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [3,4,5,1,2]
  輸出：1
  說明：原本是 [1,2,3,4,5]，旋轉了 3 次。

範例 2
  輸入：nums = [4,5,6,7,0,1,2]
  輸出：0
  說明：原本是 [0,1,2,4,5,6,7]，旋轉了 4 次。

範例 3
  輸入：nums = [11,13,15,17]
  輸出：11
  說明：旋轉了 4 次（等於沒旋轉）。""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 5000",
   "−5000 ≤ <code>nums[i]</code> ≤ 5000",
   "<code>nums</code> 裡所有元素<strong>互不相同</strong>",
   "<code>nums</code> 是一個升序陣列旋轉 1 到 <code>n</code> 次的結果",
 ],
 "idea": [
   ("fig", _P153_FIG, "0 0 640 508"),
   ("c", """lo, hi = 0, n - 1
while lo < hi:
    mid = (lo + hi) // 2
    if nums[mid] > nums[hi]:
        lo = mid + 1        # mid 在左段，最小值嚴格在它右邊
    else:
        hi = mid            # mid 在右段（可能就是最小值）
return nums[lo]

【★ 三個容易寫錯的地方】

1. 【迴圈條件是 lo < hi 而不是 lo <= hi】

   我們要「收斂到一個位置」，不是「找某個值」。

   lo <= hi 的話，當 lo == hi 時還會算一次 mid = lo，
   然後 hi = mid = lo -> 無窮迴圈 ✘

2. 【hi = mid 而不是 hi = mid - 1】

   因為 nums[mid] <= nums[hi] 只能推出
   「最小值在 [lo, mid] 裡」——
   mid【自己可能就是】最小值！

   寫成 mid - 1 會跳過答案 ✘

3. 【不需要單獨檢查 nums[mid]，也不需要 return mid】

   迴圈結束時 lo == hi，那就是答案的位置 ✔

   這種「收斂型二分」比「找特定值」的二分更常見，
   也更容易寫對（沒有「找不到」的情況）。

【為什麼一定會終止？】

    每一輪 [lo, hi] 的長度都嚴格變小：
        lo = mid + 1 -> lo 增加
        hi = mid     -> 因為 mid < hi（當 lo < hi 時），所以 hi 減少 ✔

    （mid = (lo+hi)//2 在 lo < hi 時保證 mid < hi。）

【複雜度】：O(log n) 時間、O(1) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "二分搜尋 + 和 <code>nums[hi]</code> 比較（標準答案）", [
     ("c", S["p153"]),
     "<strong>八行，O(log n) 時間、O(1) 空間。</strong>",
     ("h", "手動走一遍 <code>[4,5,6,7,0,1,2]</code>"),
     ("c", """lo=0, hi=6
    mid=3: nums[3]=7 > nums[6]=2 ✔ -> lo=4

lo=4, hi=6
    mid=5: nums[5]=1 > nums[6]=2? 否 -> hi=5

lo=4, hi=5
    mid=4: nums[4]=0 > nums[5]=1? 否 -> hi=4

lo=4 == hi -> 回傳 nums[4] = 0 ✔

【三步就收斂，log₂(7) ≈ 2.8 ✔】""",),
     ("h", "為什麼可以直接 <code>return nums[lo]</code> 而不用檢查？"),
     "<strong>因為這是「收斂型」二分</strong> —— "
     "<strong>答案一定存在（陣列非空），而且不變量保證它一直在 <code>[lo, hi]</code> 裡。</strong>",
     ("c", """【不變量】：最小值的索引永遠在 [lo, hi] 之內。

    初始：[0, n-1] 涵蓋全部 ✔

    每一步：
        nums[mid] > nums[hi] -> mid 在左段
            左段的所有值都 > 右段 -> 最小值不可能是 mid 或它左邊
            -> 可以安全地 lo = mid + 1 ✔

        nums[mid] < nums[hi] -> mid 在右段
            最小值是 mid 或在它左邊
            -> hi = mid（保留 mid）✔

    結束時 lo == hi，區間只剩一個元素 -> 那就是答案 ✔

【「維護一個包含答案的區間，每次縮小一半」
  是所有二分搜尋的共同骨架。】

    寫二分時先問自己：
        「我的不變量是什麼？每一步之後還成立嗎？」""",),
   ], "O(log n)", "O(1)", "每次砍一半", "兩個索引", optimal=True),
 ],
 "compare": (["比較對象", "能區分左右段嗎", "「沒旋轉」的情況", "備註"],
   [["nums[hi]", "✔", "✔ 正確", "標準做法"],
    ["nums[lo]", "✘", "✘ 會答錯", "常見的錯誤寫法"],
    ["nums[0]", "✘", "✘ 同上", "同樣的問題"]]),
 "edges": [
   "<strong>單一元素</strong> <code>[1]</code> → <code>1</code>。<strong>迴圈一次都不跑。</strong>",
   "<strong>兩個元素</strong> <code>[2,1]</code> → <code>1</code>。",
   "<strong>完全沒旋轉</strong> <code>[11,13,15,17]</code> → <code>11</code>。"
   "<strong>和 <code>nums[lo]</code> 比的版本會在這裡答錯。</strong>",
   "<strong>旋轉了 n−1 次</strong> <code>[2,3,4,5,1]</code> → <code>1</code>（答案在最後）。",
   "<strong><code>hi = mid - 1</code></strong> → <strong>跳過答案。</strong>",
   "<strong>迴圈條件寫成 <code>lo &lt;= hi</code></strong> → <strong>無窮迴圈。</strong>",
   "<strong>和 <code>nums[lo]</code> 比較</strong> → "
   "<strong>「沒旋轉」和「旋轉很多」分不出來，答案錯。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果有重複元素呢？"),
   "<strong>第 154 題</strong>。<code>nums[mid] == nums[hi]</code> 時"
   "<strong>完全無法判斷 <code>mid</code> 在哪一段</strong>，"
   "<strong>只能保守地 <code>hi -= 1</code>。</strong>",
   "<strong>最壞情況退化成 O(n)</strong>（例如 <code>[1,1,1,1,0,1]</code>）—— "
   "<strong>下一題會詳細講。</strong>",
   ("h", "追問二：如果要找「旋轉了幾次」呢？"),
   "<strong>就是最小值的【索引】</strong> —— 把 <code>return nums[lo]</code> 改成 "
   "<code>return lo</code>。",
   "<strong>因為原陣列的第 0 個元素（最小值）被搬到了索引 <code>lo</code> 的位置</strong>，"
   "<strong>所以旋轉次數是 <code>n - lo</code>（或 <code>lo</code>，看你怎麼定義「旋轉」）。</strong>",
   ("h", "追問三：如果要在旋轉陣列裡「搜尋某個值」呢？"),
   "<strong>第 33 題（搜尋旋轉排序陣列）</strong>。兩條路：",
   ("ul", [
     "<strong>先用本題找出「斷點」<code>lo</code></strong>，"
     "再決定要在 <code>[0, lo-1]</code> 還是 <code>[lo, n-1]</code> 做標準二分。"
     "<strong>兩次二分，O(log n)。</strong>",
     "<strong>一次二分</strong>：每一步先判斷「哪一半是有序的」，"
     "再看目標值在不在那一半的範圍內。"
     "<strong>程式碼較短但分支較多。</strong>",
   ]),
   "<strong>「先找斷點」的版本比較好想也比較不容易錯</strong> —— "
   "<strong>它把一個複雜問題拆成兩個簡單的。</strong>",
   ("h", "追問四：這個「不需要完全有序也能二分」的觀念還能用在哪？"),
   ("ul", [
     "<strong>第 162 題 尋找峰值</strong>：完全沒排序，但「往高處走一定能到峰頂」",
     "<strong>第 852 題 山脈陣列的峰頂</strong>：先升後降",
     "<strong>第 875 題 愛吃香蕉的珂珂</strong>：對「答案」二分（判定函式單調）",
     "<strong>第 1011 題 在 D 天內送達包裹</strong>：同上",
     "<strong>第 4 題 兩個有序陣列的中位數</strong>：對「分割點」二分",
   ]),
   ("c", """【二分搜尋的一般條件】：

    存在一個【單調的判定函式】 check(i)：
        i < 答案時 check(i) = False
        i >= 答案時 check(i) = True

    （或者反過來。）

    那就可以二分找到那個分界點。

【不需要「陣列已排序」——
  只需要「判定的結果是單調的」。】

    這個觀念把二分搜尋從「查表」擴展到
    「在答案空間裡搜尋」（binary search on answer），
    是競賽程式設計最重要的技巧之一。""",),
 ],
 "related": [
   "<strong>第 154 題 …II</strong> —— 有重複元素的版本",
   "<strong>第 33 題 Search in Rotated Sorted Array</strong> —— 在旋轉陣列裡找值",
   "<strong>第 81 題 …II</strong> —— 第 33 題 + 重複元素",
   "<strong>第 162 題 Find Peak Element</strong> —— 完全沒排序也能二分",
   "<strong>第 852 題 Peak Index in a Mountain Array</strong> —— 類似的結構",
 ],
 "check": [
   "為什麼要和 <code>nums[hi]</code> 比而不是 <code>nums[lo]</code>？請舉出後者會錯的例子。",
   "<code>hi = mid</code> 為什麼不能寫成 <code>hi = mid - 1</code>？",
   "迴圈條件為什麼是 <code>lo &lt; hi</code> 而不是 <code>lo &lt;= hi</code>？",
   "這個二分搜尋的「不變量」是什麼？",
 ],
})
print("P153 written")

emit({
 "num": 154, "slug": "find-minimum-in-rotated-sorted-array-ii",
 "en": [
   "Suppose an array of length <code>n</code> sorted in ascending order is "
   "<strong>rotated</strong> between <code>1</code> and <code>n</code> times.",
   "Given the sorted rotated array <code>nums</code> that may contain "
   "<strong>duplicates</strong>, return <em>the minimum element of this array</em>.",
   "You must decrease the overall operation steps as much as possible.",
 ],
 "zh": [
   "和第 153 題一樣，但這次陣列裡<strong>可能有重複的元素</strong>。",
   "找出旋轉後陣列的<strong>最小值</strong>。",
   "<strong>請盡量減少操作次數。</strong>",
   ("note", "注意題目的說法變了", [
     "第 153 題說「<strong>必須是 O(log n)</strong>」。",
     "這題只說「<strong>盡量減少操作次數</strong>」——"
     "<strong>因為有重複元素時，O(log n) 根本做不到。</strong>",
     "<strong>題目的措辭變化本身就是提示。</strong>",
   ]),
 ],
 "pre": [
   ("note", "★ 重複元素為什麼讓二分失效", [
     ("c", """第 153 題的判斷：

    nums[mid] > nums[hi]  -> mid 在左段
    nums[mid] < nums[hi]  -> mid 在右段

    互不相同時，這兩種情況涵蓋了全部 ✔

【有重複時多了第三種：nums[mid] == nums[hi]】

    這時完全無法判斷 mid 在哪一段：

        [1, 1, 1, 0, 1]     mid=2, nums[2]=1 == nums[4]=1
                             最小值在【右邊】（索引 3）

        [1, 0, 1, 1, 1]     mid=2, nums[2]=1 == nums[4]=1
                             最小值在【左邊】（索引 1）

    兩個陣列在 mid 和 hi 的位置上【一模一樣】，
    但答案在相反的方向 ✘

【所以這個情況無法用 O(1) 的資訊做決定。】

【唯一安全的做法：hi -= 1】

    為什麼安全？

        nums[mid] == nums[hi] 時，
        就算 hi 剛好是最小值的位置，
        mid 也有同樣的值 -> 丟掉 hi 不會丟掉答案 ✔

        （「最小值」是一個【值】，不是一個特定的位置。）

    但這只縮小了一格 -> 最壞 O(n)。

【最壞情況】：[1, 1, 1, ..., 1]（全部相同）

    每一輪都走 hi -= 1 -> n 輪 -> O(n) ✘

    而且【這個下界是無法突破的】—— 見追問一。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,3,5]
  輸出：1

範例 2
  輸入：nums = [2,2,2,0,1]
  輸出：0""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 5000",
   "−5000 ≤ <code>nums[i]</code> ≤ 5000",
   "<code>nums</code> 是一個升序陣列旋轉若干次的結果",
   "<strong><code>nums</code> 可能包含重複元素</strong>",
 ],
 "idea": [
   ("c", """和第 153 題只差一個 elif：

    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1        # mid 在左段
        elif nums[mid] < nums[hi]:
            hi = mid            # mid 在右段
        else:
            hi -= 1             # ★ 相等：無法判斷，保守地縮一格

    return nums[lo]

【★ 為什麼 hi -= 1 是安全的？】

    情況是 nums[mid] == nums[hi]，而且 mid < hi。

    如果 hi 這個位置就是最小值：
        那 nums[mid] 也等於最小值 ->
        丟掉 hi，答案仍然在 [lo, hi-1] 裡（mid 就在裡面）✔

    如果 hi 不是最小值：
        丟掉它顯然沒差 ✔

    兩種情況都安全 ✔

【★ 為什麼不能 lo += 1？】

    因為 nums[lo] 和 nums[mid] 的關係我們一無所知 ——
    nums[lo] 可能就是唯一的最小值。

    只有「和 mid 值相同的 hi」才能安全丟掉。

【★ 為什麼不是 hi = mid？】

    nums[mid] == nums[hi] 時，
    最小值【可能在 mid 右邊】（例如 [1,1,1,0,1]）——
    hi = mid 會把它丟掉 ✘

    只能一格一格縮。

【複雜度】

    平均：O(log n)（重複不多時）
    最壞：O(n)（全部相同時）
    空間：O(1)"""),
 ],
 "approaches": [
   ap("解法一", "三分支二分搜尋（標準答案）", [
     ("c", S["p154"]),
     "<strong>和第 153 題只差一個 <code>elif</code> 分支。</strong>",
     ("h", "手動走一遍 <code>[2,2,2,0,1]</code>"),
     ("c", """lo=0, hi=4
    mid=2: nums[2]=2 > nums[4]=1 ✔ -> lo=3

lo=3, hi=4
    mid=3: nums[3]=0 > nums[4]=1? 否
           nums[3]=0 < nums[4]=1 ✔ -> hi=3

lo=3 == hi -> 回傳 nums[3] = 0 ✔

【再走一遍最壞情況 [1,1,1,1,1]】：

    每一輪都是 nums[mid] == nums[hi] -> hi -= 1

    hi: 4 -> 3 -> 2 -> 1 -> 0
    共 4 輪 -> O(n) ✘

    （答案仍然正確，只是慢。）""",),
     ("h", "一個常見的「優化」想法，以及它為什麼沒用"),
     ("c", """有人會想：「相等時，可以同時縮兩邊嗎？」

    lo += 1; hi -= 1        ✘ 不安全！

    反例：[1, 0, 1]
        lo=0, hi=2, mid=1
        nums[1]=0 vs nums[2]=1 -> 0 < 1 -> hi=1
        （這個例子走不到相等分支）

    換一個：[0, 1, 1]（其實這是沒旋轉的）
        lo=0, hi=2, mid=1
        nums[1]=1 == nums[2]=1 -> 如果 lo += 1
        lo=1, hi=1 -> 回傳 nums[1] = 1 ✘
        正確答案是 0

    【lo += 1 會丟掉 nums[lo]，而它可能就是唯一的最小值。】

    只有 hi -= 1 是安全的，因為我們知道
    「nums[hi] 和 nums[mid] 相等，而 mid 還在區間內」。

【這是本題最容易犯的錯 ——
  「看起來對稱所以應該對稱」的直覺是錯的。】""",),
     "<strong>平均 O(log n)、最壞 O(n)、空間 O(1)。</strong>",
   ], "O(log n) 平均 / O(n) 最壞", "O(1)", "相等時只縮一格", "兩個索引", optimal=True),
 ],
 "compare": (["情況", "第 153 題", "第 154 題", "原因"],
   [["元素互不相同", "O(log n)", "O(log n)", "不會走到相等分支"],
    ["少量重複", "—", "接近 O(log n)", "相等的機會低"],
    ["全部相同", "—", "O(n)", "每輪只縮一格"],
    ["最壞情況", "O(log n)", "O(n)", "無法突破（見追問一）"]]),
 "edges": [
   "<strong>單一元素</strong> → 直接回傳。",
   "<strong>全部相同</strong> <code>[1,1,1]</code> → <code>1</code>，但要跑 O(n)。",
   "<strong><code>[2,2,2,0,1]</code></strong> → <code>0</code>（官方範例 2）。",
   "<strong><code>[1,1,1,0,1]</code></strong> → <code>0</code>。"
   "<strong>最小值在 mid 右邊。</strong>",
   "<strong><code>[1,0,1,1,1]</code></strong> → <code>0</code>。"
   "<strong>最小值在 mid 左邊 —— 和上一個在 mid/hi 位置上長得一樣！</strong>",
   "<strong><code>[3,3,1,3]</code></strong> → <code>1</code>。",
   "<strong>相等時寫成 <code>hi = mid</code></strong> → "
   "<strong><code>[1,1,1,0,1]</code> 會答 1 而不是 0。</strong>",
   "<strong>相等時寫成 <code>lo += 1</code> 或同時縮兩邊</strong> → "
   "<strong>可能丟掉唯一的最小值。</strong>",
   "<strong>5000 個相同元素</strong> → O(n) = 5000 步，仍然很快。",
 ],
 "follow": [
   ("h", "追問一：最壞情況真的無法比 O(n) 更好嗎？"),
   ("c", """【是的，可以證明 Ω(n) 的下界。】

    考慮這兩個陣列：

        A = [1, 1, 1, ..., 1]           （n 個 1，答案是 1）
        B = [1, 1, ..., 0, ..., 1]      （某一個位置是 0，答案是 0）

    任何演算法如果沒有檢查【每一個位置】，
    就有可能漏掉那個 0 ——

    對手論證（adversary argument）：
        不管演算法查詢哪個位置，
        對手都回答「1」；
        只要還有一個沒查過的位置，
        對手就可以宣稱「那裡是 0」。

    所以【必須查完所有 n 個位置】-> Ω(n) ✔

【這是一個「資訊論下界」】：

    輸入的資訊量就要 n 次查詢才能確定，
    沒有任何聰明的演算法能繞過它。

【對比第 153 題】：
    互不相同時，每次比較都能【確定地】砍掉一半
    -> O(log n) ✔

    重複元素破壞了「比較能提供資訊」這件事。

【這個對比很有教育意義】：
    「重複元素」看起來只是一個小小的條件放寬，
    卻讓複雜度從 O(log n) 掉到 O(n) ——
    整整差了一個指數。""",),
   ("h", "追問二：平均情況呢？"),
   ("c", """如果重複的元素不多，實際上還是接近 O(log n)。

    「相等分支」只在 nums[mid] == nums[hi] 時才走，
    而那需要「很多相同的值」。

    設不同值的個數是 k：
        大致上 O(log n + 重複造成的額外步數)

    實務上，只有「大量重複」的輸入才會退化。

【這是一個「最壞情況差、平均情況好」的演算法】——

    就像快速排序（平均 O(n log n)、最壞 O(n²)）。

    在真實資料上，這類演算法常常比
    「最壞情況保證好」的演算法更快。

    【選演算法時，要問「我的資料長什麼樣」
      而不只是「最壞情況是多少」。】""",),
   ("h", "追問三：如果要在有重複的旋轉陣列裡「搜尋某個值」呢？"),
   "<strong>第 81 題（搜尋旋轉排序陣列 II）</strong>。同樣的問題、同樣的解法：",
   ("c", """nums[lo] == nums[mid] == nums[hi] 時無法判斷
-> lo += 1; hi -= 1（兩邊各縮一格）

【★ 注意那題可以兩邊都縮，本題只能縮 hi】

    差別在於「要找的東西」：

    第 81 題：找一個【特定的值】target
        如果 nums[lo] == nums[mid] == nums[hi] != target，
        那 lo 和 hi 都不是答案 -> 兩邊都能丟 ✔

    第 154 題：找【最小值】
        nums[lo] 可能就是最小值 -> 不能丟 ✘
        只有 nums[hi]（和 mid 相等）能安全丟 ✔

【同樣的「相等無法判斷」，
  但「能丟掉什麼」取決於你在找什麼。】

    這個細微的差別值得想清楚 ——
    它是「理解演算法」和「背演算法」的分界。""",),
   ("h", "追問四：能不能用「先找不相等的位置」來優化？"),
   ("c", """有人會想：先從兩端往中間跳過相同的元素。

    while lo < hi and nums[lo] == nums[hi]:
        hi -= 1

    然後再做標準的二分。

【這個「優化」沒有改善最壞情況】——
    全部相同時，這個前置迴圈本身就是 O(n)。

    而且它可能【破壞正確性】，如果寫得不小心
    （例如同時縮 lo）。

【真正有用的實務優化】：

    在二分之前先檢查 nums[lo] < nums[hi]
    -> 代表沒旋轉（或旋轉了整圈），直接回 nums[lo] ✔

    這在「大部分輸入都沒旋轉」時能省很多。

    但它不改變漸進複雜度。

【教訓】：
    當下界是 Ω(n) 時，任何「優化」都只能改善常數，
    不可能改善漸進複雜度。

    先確認下界，再決定要不要優化 ——
    否則你可能在追一個不存在的目標。""",),
 ],
 "related": [
   "<strong>第 153 題 …I</strong> —— 互不相同的版本，先學那題",
   "<strong>第 33 題 Search in Rotated Sorted Array</strong> —— 找特定值",
   "<strong>第 81 題 …II</strong> —— 找特定值 + 重複元素",
   "<strong>第 4 題 兩個有序陣列的中位數</strong> —— 另一個「對分割點二分」",
 ],
 "check": [
   "<code>nums[mid] == nums[hi]</code> 時為什麼無法判斷？請舉出兩個「長得一樣但答案相反」的陣列。",
   "為什麼 <code>hi -= 1</code> 安全，而 <code>lo += 1</code> 不安全？",
   "最壞情況為什麼是 O(n)？這個下界能不能突破？",
   "第 81 題可以兩邊都縮，這題只能縮一邊 —— 為什麼？",
 ],
})
print("P154 written")

# ==================== 155. Min Stack ====================
S["p155_pair"] = '''class MinStack:
    def __init__(self):
        # 每一格存 (值, 「到這一格為止」的最小值)
        self.stack = []

    def push(self, val: int) -> None:
        cur_min = val if not self.stack else min(val, self.stack[-1][1])
        self.stack.append((val, cur_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]'''

S["p155_two"] = '''class MinStack:
    def __init__(self):
        self.stack = []
        self.mins = []                  # 輔助堆疊：只在「更小或相等」時 push

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)       # ★ 一定要用 <=，不能用 <

    def pop(self) -> None:
        v = self.stack.pop()
        if v == self.mins[-1]:
            self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]'''

S["p155_diff"] = '''class MinStack:
    def __init__(self):
        self.stack = []                 # 存的是「和當時最小值的差」
        self.min = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
            return
        self.stack.append(val - self.min)
        if val < self.min:
            self.min = val              # 更新最小值

    def pop(self) -> None:
        d = self.stack.pop()
        if d < 0:                       # 負的差代表「當時它就是新的最小值」
            self.min -= d               # 還原成上一個最小值

    def top(self) -> int:
        d = self.stack[-1]
        return self.min if d < 0 else self.min + d

    def getMin(self) -> int:
        return self.min'''


class _RefMinStack(object):
    def __init__(self):
        self.a = []

    def push(self, v):
        self.a.append(v)

    def pop(self):
        self.a.pop()

    def top(self):
        return self.a[-1]

    def getMin(self):
        return min(self.a)


_p155ns = [S.loadns(k) for k in ("p155_pair", "p155_two", "p155_diff")]

for ns in _p155ns:
    MS = ns["MinStack"]
    s = MS()
    s.push(-2); s.push(0); s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2

for _ in range(2500):
    ref = _RefMinStack()
    impls = [ns["MinStack"]() for ns in _p155ns]
    for _ in range(40):
        if not ref.a or random.random() < 0.55:
            v = random.randint(-30, 30)
            ref.push(v)
            for im in impls:
                im.push(v)
        else:
            op = random.random()
            if op < 0.35:
                ref.pop()
                for im in impls:
                    im.pop()
            elif op < 0.7:
                w = ref.top()
                for im in impls:
                    assert im.top() == w, ("P155 top", ref.a, w, im.top())
            else:
                w = ref.getMin()
                for im in impls:
                    assert im.getMin() == w, ("P155 getMin", ref.a, w, im.getMin())
print("P155 solutions OK")

_P155_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 核心想法：把「當下的最小值」和值一起存起來 —— 那個資訊會隨著 pop 自動被丟掉。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">解法一：每一格存 (值, 到這一格為止的最小值)</text>
            <g font-size="12" text-anchor="middle">
              <rect x="70" y="70" width="110" height="28" fill="none" stroke="var(--accent)"/><text x="125" y="89" fill="var(--accent)">(−2, −2)</text>
              <rect x="70" y="98" width="110" height="28" fill="none" stroke="var(--accent)"/><text x="125" y="117" fill="var(--accent)">(0, −2)</text>
              <rect x="70" y="126" width="110" height="28" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="125" y="145" fill="var(--gold)">(−3, −3)</text>
            </g>
            <text x="200" y="145" fill="var(--gold)" font-size="11" text-anchor="start">← 堆疊頂：getMin() 直接讀第二個欄位</text>
            <text x="200" y="89" fill="var(--text-muted)" font-size="11" text-anchor="start">堆疊底</text>
            <text x="20" y="182" fill="var(--text-muted)" font-size="12">pop 掉 (−3,−3) 之後，頂端變成 (0,−2) → getMin() 自動回到 −2 ✔ 完全不用重算。</text>
            <line x1="20" y1="206" x2="620" y2="206" stroke="var(--border)"/>
            <text x="20" y="234" fill="var(--gold)" font-size="13">解法二：主堆疊 + 輔助堆疊（只存「最小值的歷史」）</text>
            <g font-size="12" text-anchor="middle">
              <text x="120" y="262" fill="var(--text-muted)">主堆疊</text>
              <rect x="70" y="272" width="100" height="26" fill="none" stroke="var(--accent)"/><text x="120" y="290" fill="var(--accent)">−2</text>
              <rect x="70" y="298" width="100" height="26" fill="none" stroke="var(--accent)"/><text x="120" y="316" fill="var(--accent)">0</text>
              <rect x="70" y="324" width="100" height="26" fill="none" stroke="var(--accent)"/><text x="120" y="342" fill="var(--accent)">−3</text>
              <text x="330" y="262" fill="var(--text-muted)">輔助堆疊 mins</text>
              <rect x="280" y="272" width="100" height="26" fill="none" stroke="#ff8a65"/><text x="330" y="290" fill="#ff8a65">−2</text>
              <rect x="280" y="298" width="100" height="26" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="330" y="316" fill="#ff8a65">−3</text>
            </g>
            <text x="400" y="290" fill="var(--text-muted)" font-size="11" text-anchor="start">0 沒有比 −2 小 → 不 push</text>
            <text x="400" y="316" fill="#ff8a65" font-size="11" text-anchor="start">−3 比 −2 小 → push</text>
            <line x1="20" y1="366" x2="620" y2="366" stroke="var(--border)"/>
            <text x="20" y="394" fill="#ff8a65" font-size="13">★ 解法二為什麼一定要用 &lt;= 而不是 &lt;？</text>
            <text x="40" y="422" fill="var(--text-muted)" font-size="12">push(1), push(1)：用 &lt; 的話 mins 只有一個 1。</text>
            <text x="40" y="446" fill="var(--text-muted)" font-size="12">第一次 pop 掉一個 1 時，發現它等於 mins 頂端 → 把 1 彈掉 →</text>
            <text x="40" y="472" fill="#ff8a65" font-size="12">但堆疊裡還有一個 1！getMin() 就會回傳錯的值（或 mins 空掉）✘</text>'''

emit({
 "num": 155, "slug": "min-stack",
 "en": [
   "Design a stack that supports push, pop, top, and retrieving the minimum element in constant "
   "time.",
   "Implement the <code>MinStack</code> class:",
   ("raw", "<ul>"
           "<li><code>MinStack()</code> initializes the stack object.</li>"
           "<li><code>void push(int val)</code> pushes the element <code>val</code> onto the "
           "stack.</li>"
           "<li><code>void pop()</code> removes the element on the top of the stack.</li>"
           "<li><code>int top()</code> gets the top element of the stack.</li>"
           "<li><code>int getMin()</code> retrieves the minimum element in the stack.</li></ul>"),
   "You must implement a solution with <code>O(1)</code> time complexity for each function.",
 ],
 "zh": [
   "設計一個堆疊，支援 <code>push</code>、<code>pop</code>、<code>top</code>，"
   "並且能在<strong>常數時間</strong>內取得<strong>堆疊裡的最小值</strong>。",
   ("ul", [
     "<code>push(val)</code>：把 <code>val</code> 推進堆疊。",
     "<code>pop()</code>：移除堆疊頂的元素。",
     "<code>top()</code>：取得堆疊頂的元素。",
     "<code>getMin()</code>：取得堆疊裡的<strong>最小值</strong>。",
   ]),
   "<strong>每一個操作都必須是 <code>O(1)</code>。</strong>",
 ],
 "pre": [
   ("note", "★ 難點：pop 之後，最小值要怎麼「還原」？", [
     ("c", """最天真的做法：用一個變數記住最小值。

    def push(v):
        stack.append(v)
        self.min = min(self.min, v)

    push 沒問題 ✔

    但 pop 呢？

        如果 pop 掉的剛好【就是】最小值，
        那新的最小值是多少？

        -> 只能重新掃描整個堆疊 -> O(n) ✘

【所以問題不在「維護最小值」，
  而在「pop 之後怎麼【還原】到上一個最小值」。】

【核心洞察】：

    「最小值」不是一個單一的值，
    而是一個【隨著堆疊變化的歷史】。

    堆疊有 n 個狀態（每 push 一次就是一個新狀態），
    每個狀態都有自己的最小值。

    pop 就是「回到上一個狀態」——
    所以要能「回到上一個最小值」。

【三種存法】：

    (a) 每一格都存「到這一格為止的最小值」（解法一）
        -> 最直白，空間 2n

    (b) 只在「最小值改變時」才存（解法二）
        -> 空間更省（最好情況只有 1 格）

    (c) 存「和當時最小值的差」（解法三）
        -> 只用一個堆疊，但要小心溢位

【共同的想法：把「當下的最小值」綁在堆疊的某一層上，
  這樣 pop 的時候那個資訊會【自動】被丟掉。】"""),
   ]),
 ],
 "examples": """範例
  輸入：
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

  輸出：
    [null,null,null,null,-3,null,0,-2]

  說明：
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   // 回傳 -3
    minStack.pop();
    minStack.top();      // 回傳 0
    minStack.getMin();   // 回傳 -2""",
 "constraints": [
   "−2³¹ ≤ <code>val</code> ≤ 2³¹ − 1",
   "<code>pop</code>、<code>top</code>、<code>getMin</code> 只會在<strong>非空</strong>的堆疊上被呼叫",
   "最多會呼叫 3 × 10⁴ 次 <code>push</code>、<code>pop</code>、<code>top</code>、<code>getMin</code>",
 ],
 "idea": [
   ("fig", _P155_FIG, "0 0 640 494"),
   ("c", """【解法一：每一格存 (值, 當下的最小值)】

    push(v):
        cur_min = v if 堆疊空 else min(v, stack[-1][1])
        stack.append((v, cur_min))

    getMin(): return stack[-1][1]

    pop 時整個 tuple 被丟掉 ->
    頂端自動變回「上一個狀態的最小值」✔

    【最直白，也最不容易錯。】

【解法二：主堆疊 + 輔助堆疊】

    mins 只記錄「最小值的歷史」：

    push(v):
        stack.append(v)
        if not mins or v <= mins[-1]:
            mins.append(v)          ★ 一定要 <=

    pop():
        v = stack.pop()
        if v == mins[-1]:
            mins.pop()

    【★ 為什麼是 <= 而不是 <？】

        push(1), push(1)：

        用 < 的話，第二個 1 不會被 push 進 mins
        -> mins = [1]

        pop 一次：彈出的 1 == mins[-1] = 1 -> mins.pop()
        -> mins = []

        但 stack 裡還有一個 1！
        getMin() 就會 IndexError（或回傳錯的值）✘

        用 <= 的話 mins = [1, 1]，兩次 pop 剛好對應 ✔

    【這是本題第一名的 bug，而且只在「有重複的最小值」時才出現。】

【解法三：只用一個堆疊，存「差值」】

    stack 裡存的不是 val，而是 val - min（當時的 min）。

    差值 < 0 -> 代表「push 的時候它變成了新的最小值」
             -> pop 時可以從差值反推出「上一個最小值」

    空間最省（只有 n 個數 + 一個變數），
    但要小心【差值可能溢位】（見解法三的說明）。"""),
 ],
 "approaches": [
   ap("解法一", "每一格存 (值, 當下最小值)（最推薦）", [
     ("c", S["p155_pair"]),
     "<strong>四個方法各兩三行，每個都是 O(1)。</strong>"
     "<strong>面試時寫這個 —— 最不容易錯。</strong>",
     ("h", "為什麼「pop 自動還原」？"),
     ("c", """因為「當下的最小值」被【綁在那一格上】。

    stack = [(-2,-2), (0,-2), (-3,-3)]

    pop 掉 (-3,-3) 之後：
        stack = [(-2,-2), (0,-2)]
        stack[-1][1] = -2 ✔

    完全不用重算 —— 那個資訊本來就存在那裡。

【這是「用空間換簡單」的典型】：

    空間從 n 變成 2n（每格多存一個數），
    換來「完全不用思考還原邏輯」。

    3 × 10^4 次操作 -> 最多 6 萬個整數，
    幾百 KB —— 完全可以接受。

【一般原則】：

    當「還原到上一個狀態」很麻煩時，
    就把「那個狀態需要的資訊」跟著一起存。

    這和「回溯時存快照」（第 113 題）、
    「持久化資料結構」是同一個思路。""",),
     ("h", "Python 的 tuple 開銷"),
     "<strong>每個 tuple 物件約 56 bytes（比兩個 int 多）</strong> —— "
     "<strong>如果很在意，可以用兩個平行的 list（<code>vals</code> 和 <code>mins</code>）。</strong>",
     "<strong>但那樣就變成解法二的「每次都 push」版本了，空間一樣是 2n。</strong>",
   ], "O(1) 每個操作", "O(n)", "每格存兩個數", "一個堆疊", optimal=True),

   ap("解法二", "主堆疊 + 輔助堆疊（空間較省）", [
     ("c", S["p155_two"]),
     ("h", "★ <code>&lt;=</code> 是這個解法的命脈"),
     ("c", """if not mins or val <= mins[-1]:
    mins.append(val)
                ^^
                【一定是 <=，不能是 <】

【用 < 會在「重複的最小值」上出錯】：

    push(1)   stack=[1]      mins=[1]
    push(1)   stack=[1,1]    mins=[1]      ← 第二個 1 沒進去

    pop()     stack=[1]
              彈出的 1 == mins[-1]=1 -> mins.pop() -> mins=[]

    getMin()  -> IndexError ✘
              （或者如果有防禦，會回傳錯的值）

【用 <= 就對了】：

    push(1)   mins=[1]
    push(1)   mins=[1,1]
    pop()     mins=[1]       ✔
    getMin()  -> 1 ✔

【對稱地，pop 時的比較也要一致】：

    if v == mins[-1]: mins.pop()

    這裡用 == 是對的 ——
    因為 mins[-1] 永遠是「目前的最小值」，
    而彈出的元素如果等於它，就代表 mins 裡那一份對應到它。

【空間分析】

    最好情況（遞增 push）：mins 只有 1 格 -> O(1) 額外
    最壞情況（遞減 push）：mins 有 n 格 -> O(n)

    平均比解法一省，但最壞一樣。

【這個解法的價值】：
    它展示了「只記錄變化」而不是「記錄每個狀態」——
    在真實系統裡（例如版本控制、undo 堆疊）這是標準做法。""",),
   ], "O(1) 每個操作", "O(n) 最壞 / O(1) 最好", "只在最小值改變時 push", "兩個堆疊"),

   ap("解法三", "只用一個堆疊，存差值（最省空間，但有溢位風險）", [
     ("c", S["p155_diff"]),
     ("h", "核心：用「負的差值」編碼「這裡換了最小值」"),
     ("c", """stack 裡存的是 val - min（push 當下的 min）。

    如果 val >= min：差值 >= 0
        -> 這個元素不是新的最小值
        -> top() = min + 差值

    如果 val < min：差值 < 0
        -> 這個元素【就是】新的最小值
        -> top() = min（更新後的 min，就是 val 自己）
        -> pop 時：min -= 差值 還原成舊的 min

【驗證還原公式】

    push 時：舊 min = m_old，新 min = val
             差值 d = val - m_old < 0

    pop 時：目前 self.min = val
            要還原成 m_old

            m_old = val - d
                  = self.min - d  ✔

    所以 self.min -= d ✔

【★ 溢位風險】

    差值 val - min 可能達到
        (2^31 - 1) - (-2^31) = 2^32 - 1

    這【超過】32 位元有號整數的範圍 ✘

    在 C++/Java 裡必須用 long 存差值。
    Python 沒有這個問題（整數無限大）。

    【這是「為了省空間而引入的風險」的典型例子】——
    省了一個堆疊，卻多了一個溢位的坑。

【實務上值得嗎？】

    通常【不值得】：
        ✘ 邏輯繞（要想清楚三個地方的還原）
        ✘ 有溢位風險
        ✔ 只省了一半的空間

    但它是一個很漂亮的「編碼」技巧 ——
    把「兩個資訊」壓進「一個數」裡。

    類似的技巧：
        - 用符號位當旗標
        - 把兩個小整數打包進一個大整數
        - 第 41 題（第一個缺失的正數）用「負號」當標記""",),
   ], "O(1) 每個操作", "O(n)", "只有一個堆疊", "差值 + 一個變數"),
 ],
 "compare": (["解法", "空間", "好寫嗎", "有溢位風險", "備註"],
   [["一、存 (值, 最小值)", "2n", "★★★", "✘", "最推薦"],
    ["二、兩個堆疊", "n + k", "★★☆", "✘", "只記錄變化"],
    ["三、存差值", "n", "★☆☆", "✔ 其他語言", "編碼技巧的展示"]]),
 "edges": [
   "<strong>只 push 一個元素</strong> → <code>getMin()</code> 就是它自己。",
   "<strong>遞增 push</strong> <code>1,2,3</code> → 解法二的 <code>mins</code> 只有一格。",
   "<strong>遞減 push</strong> <code>3,2,1</code> → 解法二的 <code>mins</code> 有三格（最壞情況）。",
   "<strong>★ 重複的最小值</strong> <code>push(1), push(1)</code> → "
   "<strong>解法二用 <code>&lt;</code> 會壞掉。本題第一名的 bug。</strong>",
   "<strong>先 push 大的再 push 小的再 pop</strong> → 最小值要正確還原。",
   "<strong>值是 <code>-2³¹</code> 或 <code>2³¹-1</code></strong> → "
   "<strong>解法三的差值會超過 32 位元（Python 沒事，其他語言要用 long）。</strong>",
   "<strong>3 × 10⁴ 次操作</strong> → 三種解法都是 O(1) 每次，輕鬆。",
 ],
 "follow": [
   ("h", "追問一：如果還要支援 <code>getMax()</code> 呢？"),
   "<strong>再加一個對稱的結構</strong>（解法一的 tuple 變成三元組，"
   "或解法二再加一個 <code>maxs</code> 堆疊）。",
   "<strong>「同時追蹤最大和最小」的成本是線性疊加的 —— 不會互相干擾。</strong>",
   ("h", "追問二：如果要「佇列」版的 <code>getMin()</code> 呢？"),
   ("c", """那難得多 —— 因為佇列是【從另一端】移除的。

    堆疊：pop 掉的是「最後 push 的」
          -> 那一層的資訊自然失效 ✔

    佇列：dequeue 掉的是「最早 enqueue 的」
          -> 它可能是目前的最小值，
             而「下一個最小值」不在任何一層的記錄裡 ✘

【兩種解法】：

    (a) 【兩個堆疊模擬佇列】（第 232 題的技巧）
        每個堆疊各自維護自己的 min，
        整體的 min = min(兩個堆疊的 min)
        -> 攤還 O(1) ✔

    (b) 【單調佇列】（第 239 題：滑動視窗最大值）
        用一個雙端佇列維護「可能成為最小值的候選」，
        保持遞增。
        -> 攤還 O(1) ✔

【這個對比很有意思】：

    「堆疊 + 最小值」是 Medium，
    「佇列 + 最小值」要用到單調佇列，明顯更難。

    差別只在「從哪一端移除」。""",),
   ("h", "追問三：如果要支援「取出最小值」（而不只是查詢）呢？"),
   "<strong>那就不是堆疊了，而是「優先佇列」（heap）</strong> —— "
   "<code>push</code> 和 <code>pop-min</code> 各 O(log n)。",
   "<strong>但那樣就失去了「後進先出」的語意。</strong>",
   "<strong>如果兩個都要（LIFO 的 pop + 取出最小），"
   "就需要「堆 + 雙向串列 + 雜湊表」的組合</strong> —— "
   "<strong>和第 146 題（LRU）是同一類的「組合資料結構」設計。</strong>",
   ("h", "追問四：這種「設計題」的通用思路是什麼？"),
   ("c", """1. 【列出所有需要的操作，以及它們的時間要求】

       push O(1), pop O(1), top O(1), getMin O(1)

2. 【找出「哪一個操作是瓶頸」】

       getMin 如果每次重算是 O(n) -> 這就是要解決的

3. 【問：能不能「提前算好」？】

       可以 -> 用空間換時間（存起來）
       不行 -> 可能需要更複雜的結構

4. 【問：狀態改變時，那個「算好的東西」怎麼更新？】

       push：好更新（min(新值, 舊的最小)）
       pop： 難更新（要「還原」）

       -> 所以要把「歷史」存起來

5. 【選最簡單的存法】

【這個流程適用於所有「設計資料結構」的題目】：

    146 LRU、155 Min Stack、
    232 用堆疊實現佇列、225 用佇列實現堆疊、
    380 O(1) 插入刪除取隨機、
    295 資料流的中位數

    共同特徵：
    「單一結構做不到，要組合 / 要預先算好」。""",),
 ],
 "related": [
   "<strong>第 146 題 LRU Cache</strong> —— 另一個「組合結構」的設計題",
   "<strong>第 232 題 用堆疊實現佇列</strong> —— 追問二的做法",
   "<strong>第 239 題 滑動視窗最大值</strong> —— 單調佇列",
   "<strong>第 84 題 柱狀圖中最大的矩形</strong> —— 單調堆疊",
   "<strong>第 716 題 Max Stack</strong> —— 還要支援「取出最大值」",
 ],
 "check": [
   "為什麼「用一個變數記最小值」在 <code>pop</code> 時會壞掉？",
   "解法二為什麼一定要用 <code>&lt;=</code>？請舉出用 <code>&lt;</code> 會壞的操作序列。",
   "解法三的 <code>self.min -= d</code> 為什麼能還原成上一個最小值？",
   "為什麼「佇列版的 getMin」比「堆疊版」難得多？",
 ],
})
print("P155 written")
