# -*- coding: utf-8 -*-
"""第 71–73 題。"""
import random, posixpath
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(71)

# ==================== 71. Simplify Path ====================
S["p71"] = '''class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # split("/") 會自動把 "a//b" 切成 ['a', '', 'b']，空字串代表連續斜線
        for part in path.split("/"):
            if part == "" or part == ".":
                continue            # 空的或「當前目錄」-> 忽略
            if part == "..":
                if stack:
                    stack.pop()     # 回上一層；已經在根目錄就什麼都不做
            else:
                stack.append(part)  # 一般的目錄名（含 "..." 這種）

        return "/" + "/".join(stack)'''

S["p71_manual"] = '''class Solution:
    def simplifyPath(self, path: str) -> str:
        # 不用 split，手動掃描（在沒有 split 的語言裡就得這樣寫）
        stack = []
        i, n = 0, len(path)

        while i < n:
            while i < n and path[i] == "/":
                i += 1                      # 跳過連續的斜線
            j = i
            while j < n and path[j] != "/":
                j += 1                      # 取出一段名稱
            part = path[i:j]
            i = j

            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)'''

_p71 = [S.load(k) for k in ("p71", "p71_manual")]


def _p71_ref(path):
    out = []
    for part in path.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if out:
                out.pop()
        else:
            out.append(part)
    return "/" + "/".join(out)


for p in ["/home/", "/../", "/home//foo/", "/a/./b/../../c/", "/", "/...",
          "/a//b////c/d//././/..", "/../../../", "/a/../../b/../c//.//",
          "/abc/...", "/..hidden"]:
    e = _p71_ref(p)
    for sol in _p71:
        assert sol.simplifyPath(p) == e, ("P71", repr(p), sol, sol.simplifyPath(p), e)
_seg = ["a", "bb", ".", "..", "", "...", "c"]
for _ in range(5000):
    p = "/" + "/".join(random.choice(_seg) for _ in range(random.randint(0, 7)))
    if random.random() < 0.3:
        p += "/"
    e = _p71_ref(p)
    for sol in _p71:
        assert sol.simplifyPath(p) == e, ("P71", repr(p), sol)
print("P71 solutions OK")

_P71_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">path = &quot;/a/./b/../../c/&quot;　用堆疊模擬「進入目錄」和「回上一層」</text>
            <g font-family="monospace" font-size="13">
              <text x="40" y="56" fill="var(--text-muted)">切開後</text>
              <text x="140" y="56" fill="var(--accent)">&apos;&apos;</text>
              <text x="200" y="56" fill="var(--gold)">&apos;a&apos;</text>
              <text x="260" y="56" fill="var(--accent)">&apos;.&apos;</text>
              <text x="320" y="56" fill="var(--gold)">&apos;b&apos;</text>
              <text x="380" y="56" fill="#ff8a65">&apos;..&apos;</text>
              <text x="450" y="56" fill="#ff8a65">&apos;..&apos;</text>
              <text x="520" y="56" fill="var(--gold)">&apos;c&apos;</text>
              <text x="570" y="56" fill="var(--accent)">&apos;&apos;</text>
            </g>
            <line x1="20" y1="72" x2="620" y2="72" stroke="var(--border)"/>
            <g font-family="monospace" font-size="13">
              <text x="40" y="100" fill="var(--accent)">&apos;&apos;　 空字串（連續斜線或開頭）→ 忽略</text>
              <text x="380" y="100" fill="var(--text-muted)">堆疊：[]</text>
              <text x="40" y="126" fill="var(--gold)">&apos;a&apos;　一般目錄名 → push</text>
              <text x="380" y="126" fill="var(--text-muted)">堆疊：[a]</text>
              <text x="40" y="152" fill="var(--accent)">&apos;.&apos;　當前目錄 → 忽略</text>
              <text x="380" y="152" fill="var(--text-muted)">堆疊：[a]</text>
              <text x="40" y="178" fill="var(--gold)">&apos;b&apos;　→ push</text>
              <text x="380" y="178" fill="var(--text-muted)">堆疊：[a, b]</text>
              <text x="40" y="204" fill="#ff8a65">&apos;..&apos;  上一層 → pop</text>
              <text x="380" y="204" fill="var(--text-muted)">堆疊：[a]</text>
              <text x="40" y="230" fill="#ff8a65">&apos;..&apos;  上一層 → pop</text>
              <text x="380" y="230" fill="var(--text-muted)">堆疊：[]</text>
              <text x="40" y="256" fill="var(--gold)">&apos;c&apos;　→ push</text>
              <text x="380" y="256" fill="var(--text-muted)">堆疊：[c]</text>
              <text x="40" y="282" fill="var(--accent)">&apos;&apos;　 → 忽略（結尾的斜線）</text>
              <text x="380" y="282" fill="var(--text-muted)">堆疊：[c]</text>
            </g>
            <text x="20" y="318" fill="var(--gold)" font-size="13">結果 = &quot;/&quot; + &quot;/&quot;.join([&quot;c&quot;]) = &quot;/c&quot;　（堆疊為空時剛好是 &quot;/&quot;）</text>'''

emit({
 "num": 71, "slug": "simplify-path",
 "en": [
   "Given an <strong>absolute path</strong> for a Unix-style file system, which begins with a "
   "slash <code>'/'</code>, transform this path into its <strong>simplified canonical "
   "path</strong>.",
   "The rules are: a single period <code>'.'</code> represents the current directory; a "
   "double period <code>'..'</code> represents the previous directory (going one level up); "
   "multiple consecutive slashes are treated as a single slash. Any sequence of periods that "
   "is not <code>'.'</code> or <code>'..'</code> (e.g. <code>'...'</code>) is treated as a "
   "<strong>valid directory name</strong>.",
   "The canonical path must start with <code>'/'</code>, have directories separated by a "
   "single <code>'/'</code>, and must not end with <code>'/'</code> (unless it is the root).",
 ],
 "zh": [
   "給你一個 Unix 風格的<strong>絕對路徑</strong>（以 <code>'/'</code> 開頭），"
   "把它化簡成<strong>標準路徑（canonical path）</strong>。",
   "規則："
   "<code>'.'</code> 表示<strong>當前目錄</strong>；"
   "<code>'..'</code> 表示<strong>回上一層</strong>；"
   "連續的多個 <code>'/'</code> 視為一個；"
   "任何「不是 <code>.</code> 也不是 <code>..</code>」的點序列"
   "（例如 <code>'...'</code>）都是<strong>合法的目錄名</strong>。",
   "標準路徑必須以 <code>'/'</code> 開頭、目錄之間只用一個 <code>'/'</code> 分隔、"
   "而且<strong>結尾不能有 <code>'/'</code></strong>（除非它就是根目錄）。",
 ],
 "pre": [
   ("note", "為什麼是堆疊？", [
     ("c", """路徑是一個「進入／退出」的巢狀結構：

    進入一個目錄  ->  push
    回到上一層    ->  pop

這正是堆疊的定義。

四種路徑片段的處理：
    ""    連續斜線或開頭／結尾的斜線   -> 忽略
    "."   當前目錄                    -> 忽略
    ".."  上一層                      -> pop（堆疊空了就什麼都不做）
    其他  目錄名                       -> push

第四種要特別注意：
    "..."   是合法的目錄名！（不是 ".." 也不是 "."）
    "...."  也是
    "..a"   也是

    只有「剛好兩個點」才是「上一層」。
    很多人用 startswith("..") 判斷，那會把 "..." 誤判 ✘"""),
     "<strong>「根目錄的 <code>..</code> 停在根目錄」</strong>是 Unix 的實際行為 —— "
     "<code>cd /..</code> 之後你還在 <code>/</code>。"
     "所以 <code>pop</code> 之前要檢查堆疊是不是空的。",
   ]),
 ],
 "examples": """範例 1
  輸入：path = "/home/"
  輸出："/home"
  說明：結尾的斜線要去掉。

範例 2
  輸入：path = "/../"
  輸出："/"
  說明：根目錄的上一層還是根目錄。

範例 3
  輸入：path = "/home//foo/"
  輸出："/home/foo"
  說明：連續的斜線視為一個。

範例 4
  輸入：path = "/a/./b/../../c/"
  輸出："/c"

範例 5
  輸入：path = "/..."
  輸出："/..."
  說明："..." 是合法的目錄名，不是「上兩層」。""",
 "constraints": [
   "1 ≤ <code>path.length</code> ≤ 3000",
   "<code>path</code> 只含英文字母、數字、<code>'.'</code>、<code>'/'</code>、<code>'_'</code>",
   "<code>path</code> 是一個<strong>有效的絕對 Unix 路徑</strong>（一定以 <code>'/'</code> 開頭）",
 ],
 "mid": [
   ("note", "五個容易踩的坑", [
     ("ul", [
       "<strong><code>\"...\"</code> 是目錄名</strong>，不是「上兩層」。"
       "只有<strong>剛好兩個點</strong>才是 <code>..</code>。",
       "<strong>根目錄的 <code>..</code> 要停住</strong>："
       "<code>\"/../../../\"</code> → <code>\"/\"</code>，不能 pop 空堆疊。",
       "<strong>結果為空時要輸出 <code>\"/\"</code></strong>。"
       "<code>\"/\" + \"/\".join([])</code> = <code>\"/\" + \"\"</code> = <code>\"/\"</code> ✔ "
       "—— 這個公式自然就對了，不用特判。",
       "<strong>結尾不能有斜線</strong>：<code>\"/home/\"</code> → <code>\"/home\"</code>。"
       "用 <code>\"/\".join</code> 天然不會產生尾隨斜線。",
       "<strong>連續斜線</strong>：<code>split(\"/\")</code> 會產生空字串，要過濾掉。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P71_FIG, "0 0 640 336"),
 ],
 "approaches": [
   ap("解法一", "split + 堆疊（最推薦）", [
     ("c", S["p71"]),
     ("h", "<code>path.split(\"/\")</code> 的行為"),
     ("c", """"/a/./b/../../c/".split("/")
    -> ['', 'a', '.', 'b', '..', '..', 'c', '']

注意：
  - 開頭的 "/" 產生一個空字串
  - 結尾的 "/" 也產生一個空字串
  - 連續的 "//" 會產生中間的空字串

    "/home//foo/".split("/")
    -> ['', 'home', '', 'foo', '']

所以「忽略空字串」這一條，同時處理了
「開頭斜線」「結尾斜線」「連續斜線」三件事。

（注意這裡用的是 split("/")，帶參數版本。
  和第 58 題不同 —— 那題要用不帶參數的 split() 來忽略連續空白。
  兩種 split 的語意不同，要看清楚需求。）"""),
     ("h", "最後一行的巧妙之處"),
     ("c", """return "/" + "/".join(stack)

  stack = ["home", "foo"]  ->  "/" + "home/foo" = "/home/foo" ✔
  stack = ["c"]            ->  "/" + "c"        = "/c"        ✔
  stack = []               ->  "/" + ""         = "/"         ✔

三種情況（多層、單層、根目錄）都被同一個公式涵蓋，
而且天然不會產生尾隨斜線。

不用任何 if —— 這是「讓邊界自然落在公式裡」的好例子。"""),
     "<strong>複雜度 O(n)</strong>：split 是 O(n)，迴圈是 O(片段數)，join 是 O(n)。",
   ], "O(n)", "O(n)", "掃一遍", "堆疊 + 切出來的片段", optimal=True),

   ap("解法二", "手動掃描（不用 split）", [
     "如果語言沒有好用的 <code>split</code>（例如 C），或者想避免建那個中間 list，"
     "就手動掃描。",
     ("c", S["p71_manual"]),
     ("h", "雙指標分段的骨架"),
     ("c", """while i < n:
    while i < n and path[i] == "/":   # 跳過所有斜線
        i += 1
    j = i
    while j < n and path[j] != "/":   # 取出一段名稱
        j += 1
    part = path[i:j]
    i = j
    ...處理 part...

這個「跳過分隔符 + 取出一段」的骨架，
就是手寫 tokenizer 的最基本形式。

它自然處理了連續斜線（第一個 while 會一路跳過），
所以 part 永遠不會是空字串
（除非 i == n，此時 part 是空的，被 continue 擋掉）。

好處：不建中間的 list，空間只有堆疊。
壞處：長很多，而且兩個 while 的邊界要小心。"""),
     "<strong>在 Python 裡沒有理由用這個版本</strong>，"
     "但如果面試官問「不用內建函式呢」，這就是答案。",
   ], "O(n)", "O(n)", "掃一遍", "只有堆疊"),
 ],
 "compare": (["解法", "行數", "額外空間", "適合", "備註"],
   [["一、split + 堆疊", "12", "O(n)（含 split 的 list）", "Python", "面試預設"],
    ["二、手動掃描", "22", "O(n)（只有堆疊）", "C / 不准用 split", "tokenizer 的基本骨架"]]),
 "edges": [
   "<strong>根目錄</strong>：<code>\"/\"</code> → <code>\"/\"</code>。",
   "<strong>結尾斜線</strong>：<code>\"/home/\"</code> → <code>\"/home\"</code>。",
   "<strong>根目錄的上一層</strong>：<code>\"/../\"</code>、<code>\"/../../../\"</code> → <code>\"/\"</code>。",
   "<strong>連續斜線</strong>：<code>\"/home//foo/\"</code> → <code>\"/home/foo\"</code>。",
   "<strong>三個點</strong>：<code>\"/...\"</code> → <code>\"/...\"</code>。"
   "<strong>用 <code>startswith(\"..\")</code> 判斷會錯。</strong>",
   "<strong>以點開頭的隱藏檔</strong>：<code>\"/..hidden\"</code> → <code>\"/..hidden\"</code>。同上。",
   "<strong>全部被抵銷</strong>：<code>\"/a/../../b/../c//.//\"</code> → <code>\"/c\"</code>。",
   "<strong>複雜的混合</strong>：<code>\"/a//b////c/d//././/..\"</code> → <code>\"/a/b/c\"</code>。",
 ],
 "follow": [
   ("h", "追問一：如果是相對路徑（不以 <code>/</code> 開頭）呢？"),
   "麻煩得多。<strong>相對路徑開頭的 <code>..</code> 不能被丟掉</strong> —— "
   "<code>\"../a\"</code> 化簡後還是 <code>\"../a\"</code>。",
   ("c", """做法：用一個計數器記「有幾個還沒被抵銷的 ..」

    for part in path.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            if stack and stack[-1] != "..":
                stack.pop()
            else:
                stack.append("..")     # 相對路徑才需要這一行
        else:
            stack.append(part)

    return "/".join(stack) or "."

    "a/../../b"  ->  ["..", "b"]  ->  "../b" ✔
    "a/.."       ->  []           ->  "."    ✔（空路徑要輸出 "."）

Python 的 os.path.normpath 就是這樣做的。""",),
   ("h", "追問二：真實的 <code>realpath</code> 和這題有什麼不同？"),
   ("c", """本題（以及 Python 的 os.path.normpath）是【純字串操作】——
它不碰檔案系統。

真實的 realpath(3) 會：
  1. 解析【符號連結（symlink）】
     這是關鍵差異！如果 /a/b 是一個指向 /x/y 的 symlink，
     那 /a/b/.. 的答案是 /x（不是 /a）。

     所以純字串的化簡「在有 symlink 時是錯的」。

  2. 檢查每一層是否真的存在、是否有權限

  3. 處理掛載點、/proc 這類特殊檔案系統

這就是為什麼 shell 裡 cd .. 的行為
和 pwd -P（物理路徑）可能不一樣：
    cd 預設用「邏輯路徑」（純字串化簡），
    pwd -P 會真的去解析 symlink。

本題考的是「邏輯路徑」的化簡。""",),
   ("h", "追問三：這題的安全意義是什麼？"),
   "<strong>路徑穿越（path traversal）攻擊</strong>。"
   "如果一個網站讓使用者指定檔名，而沒有做路徑化簡，"
   "攻擊者就能用 <code>../../../etc/passwd</code> 讀到不該讀的檔案。",
   "<strong>正確的防禦</strong>：",
   ("ul", [
     "<strong>先化簡，再檢查</strong>是否還在允許的目錄底下"
     "（而不是「先檢查有沒有 <code>..</code>」—— 那會被 URL 編碼、"
     "Unicode 正規化、或 <code>....//</code> 這類技巧繞過）",
     "<strong>用作業系統提供的 <code>realpath</code></strong>（會解析 symlink），"
     "而不是純字串化簡",
     "<strong>最後再確認一次結果的前綴</strong>是允許的根目錄",
   ]),
   "<strong>「先正規化，再驗證」是所有輸入驗證的通則</strong> —— "
   "反過來（先驗證再正規化）幾乎總是可以被繞過。",
 ],
 "related": [
   "<strong>第 20 題 Valid Parentheses</strong> —— 堆疊的最基本應用",
   "<strong>第 388 題 Longest Absolute File Path</strong> —— 另一個路徑 + 堆疊題",
   "<strong>第 1472 題 Design Browser History</strong> —— 「上一頁／下一頁」也是堆疊",
 ],
 "check": [
   "<code>\"/...\"</code> 的答案是什麼？用 <code>startswith(\"..\")</code> 判斷會錯在哪？",
   "<code>\"/\" + \"/\".join(stack)</code> 在 <code>stack</code> 為空時會得到什麼？",
   "<code>split(\"/\")</code> 產生的空字串，同時處理了哪三種情況？",
   "為什麼「純字串化簡」在有符號連結時是錯的？",
 ],
})
print("P71 written")

# ==================== 72. Edit Distance ====================
S["p72_2d"] = '''class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # dp[i][j] = 把 word1 的前 i 個字元，變成 word2 的前 j 個字元，最少幾步
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 邊界：一邊是空字串時，只能全刪或全插
        for i in range(m + 1):
            dp[i][0] = i        # 刪掉 i 個
        for j in range(n + 1):
            dp[0][j] = j        # 插入 j 個

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]        # 字元相同，不用動
                else:
                    dp[i][j] = 1 + min(
                        dp[i - 1][j],      # 刪除 word1[i-1]
                        dp[i][j - 1],      # 插入 word2[j-1]
                        dp[i - 1][j - 1],  # 替換
                    )

        return dp[m][n]'''

S["p72_1d"] = '''class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n:
            word1, word2, m, n = word2, word1, n, m   # 讓 n 是較小的那個

        prev = list(range(n + 1))          # dp[0][*]

        for i in range(1, m + 1):
            cur = [i] + [0] * n            # dp[i][0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    cur[j] = prev[j - 1]
                else:
                    cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
            prev = cur

        return prev[n]'''

_p72 = [S.load(k) for k in ("p72_2d", "p72_1d")]


def _p72_ref(a, b):
    m, n = len(a), len(b)
    d = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            d[i][j] = (d[i - 1][j - 1] if a[i - 1] == b[j - 1]
                       else 1 + min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]))
    return d[m][n]


for a, b in [("horse", "ros"), ("intention", "execution"), ("", ""), ("", "a"),
             ("a", ""), ("abc", "abc"), ("abc", "xyz"), ("sunday", "saturday"),
             ("kitten", "sitting")]:
    e = _p72_ref(a, b)
    for sol in _p72:
        assert sol.minDistance(a, b) == e, ("P72", a, b, sol, sol.minDistance(a, b), e)
for _ in range(3000):
    a = "".join(random.choice("abc") for _ in range(random.randint(0, 7)))
    b = "".join(random.choice("abc") for _ in range(random.randint(0, 7)))
    e = _p72_ref(a, b)
    for sol in _p72:
        assert sol.minDistance(a, b) == e, ("P72", a, b, sol)
print("P72 solutions OK")

_P72_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">word1 = &quot;horse&quot;，word2 = &quot;ros&quot;　dp 表（答案在右下角）</text>
            <g font-family="monospace" font-size="14" text-anchor="middle">
              <text x="100" y="52" fill="var(--text-muted)" font-size="12">&quot;&quot;</text>
              <text x="160" y="52" fill="var(--accent)">r</text>
              <text x="220" y="52" fill="var(--accent)">o</text>
              <text x="280" y="52" fill="var(--accent)">s</text>

              <text x="50" y="80" fill="var(--text-muted)" font-size="12">&quot;&quot;</text>
              <text x="100" y="80" fill="var(--gold)">0</text>
              <text x="160" y="80" fill="var(--gold)">1</text>
              <text x="220" y="80" fill="var(--gold)">2</text>
              <text x="280" y="80" fill="var(--gold)">3</text>

              <text x="50" y="110" fill="var(--accent)">h</text>
              <text x="100" y="110" fill="var(--gold)">1</text>
              <text x="160" y="110" fill="var(--text-muted)">1</text>
              <text x="220" y="110" fill="var(--text-muted)">2</text>
              <text x="280" y="110" fill="var(--text-muted)">3</text>

              <text x="50" y="140" fill="var(--accent)">o</text>
              <text x="100" y="140" fill="var(--gold)">2</text>
              <text x="160" y="140" fill="var(--text-muted)">2</text>
              <text x="220" y="140" fill="#ff8a65">1</text>
              <text x="280" y="140" fill="var(--text-muted)">2</text>

              <text x="50" y="170" fill="var(--accent)">r</text>
              <text x="100" y="170" fill="var(--gold)">3</text>
              <text x="160" y="170" fill="#ff8a65">2</text>
              <text x="220" y="170" fill="var(--text-muted)">2</text>
              <text x="280" y="170" fill="var(--text-muted)">2</text>

              <text x="50" y="200" fill="var(--accent)">s</text>
              <text x="100" y="200" fill="var(--gold)">4</text>
              <text x="160" y="200" fill="var(--text-muted)">3</text>
              <text x="220" y="200" fill="var(--text-muted)">3</text>
              <text x="280" y="200" fill="#ff8a65">2</text>

              <text x="50" y="230" fill="var(--accent)">e</text>
              <text x="100" y="230" fill="var(--gold)">5</text>
              <text x="160" y="230" fill="var(--text-muted)">4</text>
              <text x="220" y="230" fill="var(--text-muted)">4</text>
              <text x="280" y="230" fill="#ff8a65">3</text>
            </g>
            <rect x="256" y="212" width="48" height="26" fill="none" stroke="#ff8a65" stroke-width="2"/>
            <g font-size="12">
              <text x="350" y="80" fill="var(--gold)">第 0 列／第 0 行：一邊是空字串</text>
              <text x="350" y="100" fill="var(--text-muted)">只能全刪（i 步）或全插（j 步）</text>
              <text x="350" y="140" fill="var(--text-muted)">字元相同 → 直接抄左上角</text>
              <text x="350" y="160" fill="var(--text-muted)">（o == o，dp[2][2] = dp[1][1] = 1）</text>
              <text x="350" y="196" fill="var(--text-muted)">字元不同 → 1 + min(上, 左, 左上)</text>
              <text x="350" y="216" fill="#ff8a65">答案 dp[5][3] = 3</text>
            </g>
            <text x="20" y="266" fill="var(--gold)" font-size="12">horse → rorse（替換 h→r）→ rose（刪 r）→ ros（刪 e）　共 3 步</text>'''

emit({
 "num": 72, "slug": "edit-distance",
 "en": [
   "Given two strings <code>word1</code> and <code>word2</code>, return <em>the minimum "
   "number of operations required to convert <code>word1</code> to <code>word2</code></em>.",
   "You have the following three operations permitted on a word: "
   "<strong>Insert</strong> a character, <strong>Delete</strong> a character, "
   "<strong>Replace</strong> a character.",
 ],
 "zh": [
   "給你兩個字串 <code>word1</code> 和 <code>word2</code>，"
   "回傳把 <code>word1</code> 轉換成 <code>word2</code> 所需的<strong>最少操作次數</strong>。",
   "你可以使用三種操作："
   "<strong>插入</strong>一個字元、<strong>刪除</strong>一個字元、<strong>替換</strong>一個字元。",
 ],
 "pre": [
   ("note", "這就是 Levenshtein 距離", [
     ("c", """「編輯距離」正式的名字是【Levenshtein 距離】
（1965 年由蘇聯數學家 Vladimir Levenshtein 提出）。

它是「兩個字串有多不一樣」最常用的度量，
而且它是一個真正的【度量（metric）】：
    d(a, a) = 0
    d(a, b) = d(b, a)         對稱（因為插入和刪除互為反操作）
    d(a, c) <= d(a, b) + d(b, c)   三角不等式

實際應用：
    拼字檢查、自動更正
    DNA 序列比對（生物資訊學）
    版本控制的 diff
    模糊搜尋（fuzzy search）
    OCR 的錯誤率評估

    "kitten" -> "sitting" 的距離是 3：
        kitten -> sitten  （k 換成 s）
        sitten -> sittin  （e 換成 i）
        sittin -> sitting （插入 g）"""),
   ]),
 ],
 "examples": """範例 1
  輸入：word1 = "horse", word2 = "ros"
  輸出：3
  說明：
    horse -> rorse （把 'h' 換成 'r'）
    rorse -> rose  （刪掉 'r'）
    rose  -> ros   （刪掉 'e'）

範例 2
  輸入：word1 = "intention", word2 = "execution"
  輸出：5""",
 "constraints": [
   "0 ≤ <code>word1.length</code>, <code>word2.length</code> ≤ 500",
   "<code>word1</code> 和 <code>word2</code> 只含小寫英文字母",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>兩個字串都可以是空的</strong>。"
       "<code>(\"\", \"\")</code> → 0；<code>(\"\", \"abc\")</code> → 3。"
       "<strong>邊界初始化就是為了這個。</strong>",
       "<strong>長度到 500</strong>，所以 O(mn) = 25 萬 —— 瞬間完成。"
       "而 O(m × n) 的 dp 表也只有 25 萬個整數，記憶體沒問題。",
       "<strong>三種操作的成本都是 1</strong>。"
       "如果成本不同（例如插入比刪除貴），轉移式要加上對應的權重 —— 見文末追問。",
     ]),
   ]),
 ],
 "idea": [
   ("c", """狀態定義（最關鍵的一步）：

    dp[i][j] = 把 word1 的【前 i 個字元】變成 word2 的【前 j 個字元】，最少幾步

轉移：看 word1[i-1] 和 word2[j-1]（注意索引偏移 1）

  情況 A：兩個字元相同
      不需要任何操作，直接看更小的子問題
          dp[i][j] = dp[i-1][j-1]

  情況 B：兩個字元不同，三種操作各試一次，取最小

      刪除 word1[i-1]：
          先把 word1 前 i-1 個變成 word2 前 j 個，再刪掉這一個
          dp[i][j] = dp[i-1][j] + 1

      插入 word2[j-1]：
          先把 word1 前 i 個變成 word2 前 j-1 個，再插入這一個
          dp[i][j] = dp[i][j-1] + 1

      替換 word1[i-1] 成 word2[j-1]：
          先把前 i-1 對上前 j-1，再換掉這一個
          dp[i][j] = dp[i-1][j-1] + 1

      取三者的 min。

邊界：
    dp[i][0] = i     word2 是空的 -> 全部刪掉，i 步
    dp[0][j] = j     word1 是空的 -> 全部插入，j 步"""),
   ("fig", _P72_FIG, "0 0 640 280"),
 ],
 "approaches": [
   ap("解法一", "二維 DP（標準解）", [
     ("c", S["p72_2d"]),
     ("h", "三個方向，各自對應一種操作"),
     ("c", """dp[i][j] 的三個來源（在 dp 表上的方向）：

        dp[i-1][j-1]  ←左上→  替換
             ↑
        dp[i-1][j]    ←上→    刪除 word1 的一個字元
             
        dp[i][j-1]    ←左→    插入 word2 的一個字元

記法：
    「上」表示 i 變小 -> word1 少一個字元 -> 刪除
    「左」表示 j 變小 -> word2 少一個字元 -> 對應「插入」
                        （我們在 word1 裡插入一個字元來配上 word2[j-1]）
    「左上」表示兩邊都少一個 -> 一對一，替換（或不用動）

很多人會把「上」和「左」搞混 ——
記住「i 對應 word1，j 對應 word2」就不會錯。"""),
     ("h", "為什麼「字元相同」時不用考慮其他三種？"),
     ("c", """直覺上會擔心：字元相同的時候，
會不會「刪掉它再插入別的」反而更省？

不會。可以證明：
    dp[i][j] = dp[i-1][j-1]  當 word1[i-1] == word2[j-1] 時
    永遠是最優的。

證明的直覺（交換論證）：
    設有一個最優解，它沒有把 word1[i-1] 對應到 word2[j-1]。
    那麼這兩個字元各自被「刪除」或「替換」了。
    我們總可以把方案改成「讓它們互相對應、不動」，
    而操作次數不會增加。

    （嚴格的證明要處理幾種情況，但結論是對的。）

實務上：如果不確定，就四個都取 min ——
    dp[i][j] = min(dp[i-1][j-1] + (0 if 相同 else 1),
                   dp[i-1][j] + 1,
                   dp[i][j-1] + 1)

    這樣寫也對，而且不用依賴上面那個定理。
    複雜度一樣。"""),
     ("h", "索引偏移 1 的陷阱"),
     "<code>dp[i][j]</code> 對應的是 <code>word1[i-1]</code> 和 <code>word2[j-1]</code>，"
     "<strong>不是 <code>word1[i]</code></strong>。"
     "因為 <code>dp</code> 的第 0 列／第 0 行代表「空字串」。"
     "<strong>這個 off-by-one 是 DP 題最常見的 bug 之一。</strong>",
   ], "O(m·n)", "O(m·n)", "填滿 (m+1)×(n+1) 的表", "dp 表"),

   ap("解法二", "一維滾動（O(min(m,n)) 空間）", [
     "<code>dp[i][j]</code> 只依賴<strong>上一列</strong>（<code>dp[i-1][*]</code>）"
     "和<strong>這一列的左邊</strong>（<code>dp[i][j-1]</code>），"
     "所以兩條陣列就夠。",
     ("c", S["p72_1d"]),
     ("h", "為什麼要先交換讓 n 變小？"),
     "空間是 O(n)，所以讓 <code>n = min(m, n)</code> 可以省一半。"
     "<strong>而且編輯距離是對稱的</strong>（<code>d(a,b) == d(b,a)</code>），"
     "所以交換不影響答案。",
     ("h", "為什麼這裡用兩條陣列而不是一條？"),
     ("c", """轉移式需要三個值：
    prev[j]      上一列同欄     （dp[i-1][j]）
    cur[j-1]     這一列左邊     （dp[i][j-1]）
    prev[j-1]    上一列左邊     （dp[i-1][j-1]）  ← 關鍵

如果只用一條陣列 dp：
    當我們要寫 dp[j] 時，dp[j] 還是舊值（上一列）✔
    dp[j-1] 已經是新值（這一列）✔
    但 dp[i-1][j-1] 呢？它在上一輪就被 dp[j-1] 的新值蓋掉了 ✘

所以單陣列版必須「先把 dp[j-1] 的舊值存起來」：

    prev_diag = dp[0]
    dp[0] = i
    for j in 1..n:
        tmp = dp[j]                    # 先存 dp[i-1][j]
        dp[j] = ... 用 prev_diag ...
        prev_diag = tmp                # 它就是下一輪的「左上」

    這樣可以做到真正的 O(n) 單陣列，但容易寫錯。

    用兩條陣列（prev 和 cur）比較不容易錯，
    空間一樣是 O(n)，只是常數 2 倍 —— 完全值得。

這和第 62、63、64 題的差別：
    那幾題的轉移只需要「上」和「左」，不需要「左上」，
    所以單陣列就夠。
    多一個「左上」，就多一層麻煩。"""),
   ], "O(m·n)", "O(min(m,n))", "同上", "兩條陣列", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "能回溯出操作序列？", "備註"],
   [["一、二維 DP", "O(mn)", "O(mn)", "✔", "面試預設"],
    ["二、一維滾動", "O(mn)", "O(min(m,n))", "✘（表被丟掉了）", "空間最省"]]),
 "edges": [
   "<strong>兩個都空</strong>：<code>(\"\", \"\")</code> → 0。",
   "<strong>一個空</strong>：<code>(\"\", \"abc\")</code> → 3；<code>(\"abc\", \"\")</code> → 3。",
   "<strong>完全相同</strong>：<code>(\"abc\", \"abc\")</code> → 0。走的是「字元相同」那條路。",
   "<strong>完全不同</strong>：<code>(\"abc\", \"xyz\")</code> → 3（三次替換）。",
   "<strong>長度不同</strong>：<code>(\"a\", \"ab\")</code> → 1（插入一個）。",
   "<strong>經典測資</strong>：<code>(\"kitten\", \"sitting\")</code> → 3；"
   "<code>(\"sunday\", \"saturday\")</code> → 3。",
   "<strong>索引偏移</strong>：<code>word1[i-1]</code> 寫成 <code>word1[i]</code> 會 IndexError 或答案錯。",
 ],
 "follow": [
   ("h", "追問一：如果要回傳「具體的操作序列」呢？"),
   "需要完整的二維 dp 表（不能用滾動陣列）。"
   "從 <code>dp[m][n]</code> 開始往回走，"
   "每一步比較「當前值是從哪個方向來的」，"
   "就能重建出插入／刪除／替換的序列。O(m+n) 的回溯。",
   "<strong>這正是 <code>diff</code> 工具的原理</strong> —— "
   "它算的是「最少的插入和刪除」（沒有替換），"
   "也就是 LCS（最長公共子序列）的對偶問題。",
   ("h", "追問二：如果三種操作的成本不同呢？"),
   ("c", """dp[i][j] = min(
    dp[i-1][j]   + cost_delete,
    dp[i][j-1]   + cost_insert,
    dp[i-1][j-1] + (0 if 相同 else cost_replace),
)

骨架完全一樣，只是把 1 換成對應的成本。

有趣的特例：
    如果 cost_replace >= cost_delete + cost_insert，
    那「替換」永遠不划算（不如刪了再插），
    這時候編輯距離退化成「LCS 距離」：
        d(a,b) = m + n - 2 × LCS(a,b)

    這就是 diff 的模型（只有插入和刪除）。""",),
   ("h", "追問三：如果還能「交換相鄰兩個字元」呢？"),
   "那叫做 <strong>Damerau-Levenshtein 距離</strong>，"
   "多一個轉移項：<code>dp[i-2][j-2] + 1</code>（當 "
   "<code>word1[i-1] == word2[j-2]</code> 且 <code>word1[i-2] == word2[j-1]</code> 時）。",
   "<strong>這對拼字檢查很重要</strong> —— "
   "打字時「相鄰字母打反」（<code>teh</code> → <code>the</code>）是最常見的錯誤之一，"
   "在 Levenshtein 裡它是 2 步，在 Damerau-Levenshtein 裡只有 1 步。",
   ("h", "追問四：有沒有比 O(mn) 更快的做法？"),
   ("c", """有幾個方向：

  1. 如果只要知道「距離是不是 <= k」
     只需要算 dp 表中「離對角線 k 格以內」的部分
     -> O(k × min(m,n))
     這在拼字檢查裡非常實用（通常只關心距離 1 或 2）。

  2. 位元平行（Myers 1999）
     用位元運算一次處理 64 個格子
     -> O(mn / w)，w 是字組寬度
     實測快 10-30 倍，是 agrep、TRE 等工具的核心。

  3. 理論下界
     2015 年 Backurs 和 Indyk 證明：
     如果存在 O(n^(2-ε)) 的演算法，
     那麼 SETH（強指數時間假說）就不成立。

     換句話說：在合理的複雜度假設下，
     O(n²) 已經是最優的。

     這是「細緻複雜度（fine-grained complexity）」的
     一個著名結果 —— 它為「看起來可以更快但一直沒人做到」
     的問題提供了理論解釋。""",),
 ],
 "related": [
   "<strong>第 1143 題 Longest Common Subsequence</strong> —— 只有插入和刪除的版本",
   "<strong>第 583 題 Delete Operation for Two Strings</strong> —— 同上",
   "<strong>第 10／44 題 正規表示式／通配符匹配</strong> —— 同樣的二維 DP 骨架",
   "<strong>第 97 題 Interleaving String</strong> —— 兩字串的另一種二維 DP",
   "<strong>第 712 題 Minimum ASCII Delete Sum</strong> —— 成本不是 1 的版本",
 ],
 "check": [
   "<code>dp[i][j]</code> 的三個來源（上、左、左上）分別對應哪一種操作？",
   "為什麼「字元相同」時可以直接抄左上角，不用考慮其他三種？",
   "一維滾動為什麼需要兩條陣列（或一個額外的 <code>prev_diag</code> 變數）？"
   "和第 62 題的差別在哪？",
   "如果 <code>cost_replace</code> 很貴，編輯距離會退化成什麼？",
 ],
})
print("P72 written")
