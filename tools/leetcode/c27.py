# -*- coding: utf-8 -*-
"""第 27–30 題。"""
import random, collections
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(27)

# ==================== 27. Remove Element ====================
S["p27_write"] = '''class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0                       # 下一個要寫入的位置
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k'''

S["p27_swap_end"] = '''class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]   # 把最後一個搬過來填坑
                n -= 1                  # 縮小有效範圍；i 不動，要重新檢查搬過來的值
            else:
                i += 1
        return n'''

_p27 = [S.load(k) for k in ("p27_write", "p27_swap_end")]
for c, v in [([3, 2, 2, 3], 3), ([0, 1, 2, 2, 3, 0, 4, 2], 2), ([], 0),
             ([1], 1), ([1], 2), ([4, 4, 4, 4], 4)]:
    e = sorted(x for x in c if x != v)
    for sol in _p27:
        a = list(c)
        k = sol.removeElement(a, v)
        assert k == len(e) and sorted(a[:k]) == e, ("P27", c, v, sol, k, a[:k], e)
for _ in range(4000):
    c = [random.randint(0, 4) for _ in range(random.randint(0, 10))]
    v = random.randint(0, 4)
    e = sorted(x for x in c if x != v)
    for sol in _p27:
        a = list(c)
        k = sol.removeElement(a, v)
        assert k == len(e) and sorted(a[:k]) == e, ("P27", c, v, sol)
print("P27 solutions OK")

emit({
 "num": 27, "slug": "remove-element",
 "en": [
   "Given an integer array <code>nums</code> and an integer <code>val</code>, remove all "
   "occurrences of <code>val</code> in <code>nums</code> <strong>in-place</strong>. "
   "The order of the elements may be changed.",
   "Return the number of elements in <code>nums</code> which are not equal to <code>val</code>. "
   "The first <code>k</code> elements of <code>nums</code> should hold the final result.",
 ],
 "zh": [
   "給你一個陣列 <code>nums</code> 和一個值 <code>val</code>，請<strong>原地</strong>移除所有等於 "
   "<code>val</code> 的元素。<strong>元素的順序可以改變</strong>。",
   "回傳移除後剩下的元素個數 <code>k</code>，而且 <code>nums</code> 的前 <code>k</code> 格要存放結果。",
 ],
 "pre": [
   ("note", "和第 26 題差一個字：「順序可以改變」", [
     ("c", """第 26 題：要保持相對順序  ->  只能用「讀寫指標」往前搬
第 27 題：順序可以改變    ->  多了一個「拿最後一個來填坑」的選項

為什麼這個差別重要？

    nums = [1, 2, 3, 3, 3, 3, 3, 4]，val = 3

    讀寫指標：要走完 8 格，寫 3 次
    填坑法：  遇到 3 就從尾巴搬一個過來，只搬 2 次就結束
              （因為 4 被搬到前面之後，後面的 3 直接被「縮掉」）

當「要刪的元素很多」時，填坑法的寫入次數明顯少很多。
當「要刪的元素很少」時，兩者差不多。

這是一個很典型的「放寬一個條件，換來一個更快的演算法」的例子。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [3,2,2,3], val = 3
  輸出：k = 2，nums 的前 2 格是 [2,2]

範例 2
  輸入：nums = [0,1,2,2,3,0,4,2], val = 2
  輸出：k = 5，nums 的前 5 格包含 [0,0,1,3,4]（順序不拘）""",
 "constraints": [
   "0 ≤ <code>nums.length</code> ≤ 100",
   "0 ≤ <code>nums[i]</code> ≤ 50",
   "0 ≤ <code>val</code> ≤ 100",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>陣列可以是空的</strong>（長度 0）。兩種解法都自然處理（迴圈跑 0 次）。",
       "<strong><code>val</code> 的範圍（0–100）比 <code>nums[i]</code> 的範圍（0–50）大。</strong>"
       "所以 <code>val</code> 可能根本不在陣列裡 —— 這時什麼都不用刪，回傳原長度。",
       "<strong>「順序可以改變」</strong>是這題和第 26 題最大的差別，也是評分的重點："
       "面試官會想看你有沒有注意到這句話、並且利用它。",
     ]),
   ]),
 ],
 "idea": [
   "兩種解法，都是 O(n) 時間、O(1) 空間，差別在<strong>寫入次數</strong>。",
 ],
 "approaches": [
   ap("解法一", "讀寫指標（保持順序，最通用）", [
     ("c", S["p27_write"]),
     "和第 26 題完全一樣的模板：一個指標讀、一個指標寫，"
     "只有「該保留」的元素才寫下去。",
     ("c", """nums = [0,1,2,2,3,0,4,2]，val = 2

x=0  != 2 -> nums[0]=0  k=1
x=1  != 2 -> nums[1]=1  k=2
x=2  == 2 -> 跳過        k=2
x=2  == 2 -> 跳過        k=2
x=3  != 2 -> nums[2]=3  k=3
x=0  != 2 -> nums[3]=0  k=4
x=4  != 2 -> nums[4]=4  k=5
x=2  == 2 -> 跳過        k=5

nums = [0,1,3,0,4,0,4,2]，前 5 格 [0,1,3,0,4] ✔ 回傳 5"""),
     "<strong>順序被保留了</strong>（雖然題目不要求）。"
     "這是它的優點 —— 同一份程式碼可以直接用在「要求保持順序」的題目上。",
     "<strong>寫入次數 = 保留的元素個數</strong>。"
     "如果幾乎沒東西要刪，那就是幾乎每一格都寫一次（寫到自己身上）。",
   ], "O(n)", "O(1)", "掃一遍", "一個下標", optimal=True),

   ap("解法二", "從尾巴搬過來填坑（寫入次數最少）", [
     "既然順序無所謂，遇到要刪的元素時，就<strong>把最後一個有效元素搬過來蓋掉它</strong>，"
     "然後把有效範圍縮小一格。",
     ("c", S["p27_swap_end"]),
     ("c", """nums = [3,2,2,3]，val = 3，n = 4

i=0: nums[0]=3 == 3
     nums[0] = nums[3] = 3，n=3
     i 不動（搬過來的 3 還沒檢查！）
     nums = [3,2,2,|3]

i=0: nums[0]=3 == 3
     nums[0] = nums[2] = 2，n=2
     i 不動
     nums = [2,2,|2,3]

i=0: nums[0]=2 != 3 -> i=1
i=1: nums[1]=2 != 3 -> i=2
i=2 == n=2 -> 結束

回傳 2，前 2 格是 [2,2] ✔"""),
     ("h", "為什麼搬完之後 <code>i</code> 不能前進？"),
     "因為<strong>從尾巴搬過來的那個值還沒被檢查</strong> —— 它自己也可能等於 <code>val</code>。"
     "如果搬完就 <code>i += 1</code>，那個值會被漏掉。",
     ("c", """錯誤寫法：
    if nums[i] == val:
        nums[i] = nums[n-1]
        n -= 1
        i += 1              # ✘ 漏檢查搬過來的值

    nums = [3, 3]，val = 3
    i=0: nums[0]=3 -> nums[0]=nums[1]=3, n=1, i=1
    i=1 == n=1 -> 結束，回傳 1

    錯了！應該回傳 0。前 1 格是 [3]，但 3 應該被刪掉。

這是這個解法唯一的陷阱，也是面試時最常被抓到的 bug。"""),
     ("h", "什麼時候該用這個？"),
     "當<strong>要刪的元素很多</strong>而且<strong>順序真的無所謂</strong>時。"
     "極端例子：<code>[1] + [2]*100000</code>、<code>val = 2</code> —— "
     "解法一要寫 1 次但走 100001 格；解法二只要 1 次搬移就把 i 推到界外。"
     "（實際上兩者都是 O(n)，差的是寫入次數而不是總步數。"
     "在「寫入很貴」的場景，例如寫到 SSD 或需要同步到遠端，這個差別才真的重要。）",
   ], "O(n)", "O(1)", "掃一遍", "兩個變數"),
 ],
 "compare": (["解法", "時間", "寫入次數", "保持順序？", "陷阱"],
   [["一、讀寫指標", "O(n)", "= 保留的個數", "✔", "無"],
    ["二、尾部填坑", "O(n)", "= 刪除的個數", "✘", "搬完後 i 不能前進"]]),
 "edges": [
   "<strong>空陣列</strong>：<code>([], 0)</code> → 0。",
   "<strong>全部都要刪</strong>：<code>([4,4,4,4], 4)</code> → 0。解法二的「i 不前進」在這裡至關重要。",
   "<strong>一個都不用刪</strong>：<code>([1], 2)</code> → 1。",
   "<strong>只有一個且要刪</strong>：<code>([1], 1)</code> → 0。",
   "<strong>要刪的在最後</strong>：<code>([1,2,3], 3)</code> → 2。解法二會把 <code>nums[2]</code> 搬到自己身上，無害。",
   "<strong><code>val</code> 不在陣列裡</strong>：<code>([1,2,3], 99)</code> → 3。",
 ],
 "follow": [
   ("h", "追問一：如果要刪的是「滿足某個條件」的元素呢？"),
   "把 <code>x != val</code> 換成 <code>not predicate(x)</code> 即可，模板完全一樣。"
   "<strong>這個模板的本質是「原地過濾（in-place filter）」</strong>，"
   "和 Python 的 <code>[x for x in nums if ...]</code> 做同一件事，但不配置新記憶體。",
   ("h", "追問二：這個模板還能用在哪？"),
   ("ul", [
     "<strong>第 26／80 題</strong>：條件變成「和前面保留的不重複」",
     "<strong>第 283 題 Move Zeroes</strong>：先把非零的往前搬，再把後面補 0",
     "<strong>第 75 題 Sort Colors</strong>：三個指標的版本（荷蘭國旗）",
     "<strong>C++ 的 <code>std::remove</code></strong>：標準庫就是這個演算法，"
     "而且它也只回傳新的結尾迭代器、不真的縮短容器 —— "
     "所以標準用法是 <code>v.erase(std::remove(v.begin(), v.end(), val), v.end())</code>，"
     "俗稱 erase-remove idiom。<strong>LeetCode 這題其實就是在考 <code>std::remove</code> 的實作。</strong>",
   ]),
   ("h", "追問三：為什麼題目不要求把後面清空？"),
   "因為那會是額外的 O(n) 寫入，而且對「回傳長度 + 前 k 格」這個介面來說沒有意義。"
   "<strong>在真實的容器實作裡，「邏輯長度」和「實體容量」本來就是分開的</strong> —— "
   "<code>vector::erase</code> 也只是改 size，不會去清理後面的記憶體。",
 ],
 "related": [
   "<strong>第 26 題 Remove Duplicates from Sorted Array</strong> —— 同一個模板",
   "<strong>第 283 題 Move Zeroes</strong> —— 過濾 + 補零",
   "<strong>第 75 題 Sort Colors</strong> —— 三指標版",
 ],
 "check": [
   "解法二搬完元素後為什麼不能 <code>i += 1</code>？請用 <code>([3,3], 3)</code> 追一遍。",
   "兩種解法的寫入次數分別是多少？什麼情況下差別最大？",
   "如果題目改成「必須保持順序」，哪個解法失效？",
   "C++ 的 erase-remove idiom 為什麼要寫成兩個函式？和這題有什麼關係？",
 ],
})
print("P27 written")

# ==================== 28. Find the Index of the First Occurrence in a String ====================
S["p28_builtin"] = '''class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)      # 找不到會回傳 -1，剛好符合題目'''

S["p28_naive"] = '''class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        # 起點最多只能到 n - m（再後面就放不下 needle 了）
        for i in range(n - m + 1):
            j = 0
            while j < m and haystack[i + j] == needle[j]:
                j += 1
            if j == m:
                return i
        return -1'''

S["p28_kmp"] = '''class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m == 0:
            return 0

        # --- 第 1 步：建 next 表（也叫 failure function / LPS 表）---
        # nxt[i] = needle[0..i] 這個前綴裡，
        #          「同時是真前綴又是真後綴」的最長長度
        nxt = [0] * m
        k = 0
        for i in range(1, m):
            while k > 0 and needle[i] != needle[k]:
                k = nxt[k - 1]          # 配不上就退回更短的邊界
            if needle[i] == needle[k]:
                k += 1
            nxt[i] = k

        # --- 第 2 步：用 next 表掃描 haystack，指標永不回頭 ---
        k = 0                            # 目前已經配對到 needle 的第幾個字元
        for i in range(n):
            while k > 0 and haystack[i] != needle[k]:
                k = nxt[k - 1]           # 部分失配，滑到下一個可能的對齊
            if haystack[i] == needle[k]:
                k += 1
            if k == m:
                return i - m + 1

        return -1'''

_p28 = [S.load(k) for k in ("p28_builtin", "p28_naive", "p28_kmp")]
for h, nd in [("sadbutsad", "sad"), ("leetcode", "leeto"), ("", ""), ("a", ""),
              ("", "a"), ("aaaaa", "bba"), ("mississippi", "issip"),
              ("aabaaabaaac", "aabaaac"), ("abab", "abab")]:
    e = h.find(nd)
    for sol in _p28:
        assert sol.strStr(h, nd) == e, ("P28", h, nd, sol, sol.strStr(h, nd), e)
for _ in range(4000):
    h = "".join(random.choice("ab") for _ in range(random.randint(0, 14)))
    nd = "".join(random.choice("ab") for _ in range(random.randint(0, 5)))
    e = h.find(nd)
    for sol in _p28:
        assert sol.strStr(h, nd) == e, ("P28", repr(h), repr(nd), sol)
print("P28 solutions OK")

_P28_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">KMP 的核心：配到一半失敗時，不要把指標退回去重來，而是「滑到下一個可能的對齊」</text>
            <text x="20" y="52" fill="var(--text-muted)" font-size="12">暴力法：失敗就回到起點 + 1，haystack 的指標往回走</text>
            <g font-family="monospace" font-size="14">
              <text x="40" y="84" fill="var(--text-muted)">a a b a a a b a a a c</text>
              <text x="40" y="108" fill="var(--accent)">a a b a a a c</text>
              <text x="360" y="108" fill="#ff8a65" font-size="12">第 7 個字配不上</text>
              <text x="58" y="132" fill="var(--text-muted)" opacity="0.5">a a b a a a c</text>
              <text x="360" y="132" fill="var(--text-muted)" font-size="12">整組右移 1 格，從頭比</text>
            </g>
            <line x1="20" y1="150" x2="620" y2="150" stroke="var(--border)"/>
            <text x="20" y="178" fill="var(--text-muted)" font-size="12">KMP：利用「aabaa」的前綴後綴重疊，一口氣滑到正確位置</text>
            <g font-family="monospace" font-size="14">
              <text x="40" y="210" fill="var(--text-muted)">a a b a a a b a a a c</text>
              <text x="40" y="234" fill="var(--accent)">a a b a a</text>
              <text x="152" y="234" fill="#ff8a65">a c</text>
              <text x="40" y="262" fill="var(--gold)" font-size="11">已配對的 &quot;aabaa&quot; 的最長「前綴＝後綴」是 &quot;aa&quot;（長度 2）</text>
              <text x="130" y="288" fill="var(--accent)">a a b a a a c</text>
              <text x="360" y="288" fill="var(--gold)" font-size="12">直接滑 3 格，k 退到 2 繼續</text>
            </g>
            <text x="20" y="318" fill="var(--gold)" font-size="12">haystack 的指標 i 從頭到尾只往前走 —— 這就是 O(n + m) 的來源。</text>'''

emit({
 "num": 28, "slug": "find-the-index-of-the-first-occurrence-in-a-string",
 "en": [
   "Given two strings <code>needle</code> and <code>haystack</code>, return the index of the "
   "first occurrence of <code>needle</code> in <code>haystack</code>, or <code>-1</code> if "
   "<code>needle</code> is not part of <code>haystack</code>.",
 ],
 "zh": [
   "給你兩個字串 <code>haystack</code>（大海）和 <code>needle</code>（針），"
   "回傳 <code>needle</code> 在 <code>haystack</code> 中<strong>第一次出現</strong>的索引；"
   "如果沒出現過，回傳 <code>-1</code>。",
 ],
 "pre": [
   ("note", "這題就是 C 的 strstr / Python 的 str.find", [
     "字串搜尋是計算機科學裡研究得最徹底的問題之一。"
     "這題表面上是 Easy（因為 <code>haystack.find(needle)</code> 一行就過），"
     "但它背後是 <strong>KMP 演算法</strong> —— 面試時真正被問的東西。",
     ("c", """規模與演算法的對應：

    n = len(haystack), m = len(needle)

    暴力法：      O(n · m)    最壞情況
    KMP：         O(n + m)    最壞情況也是線性
    Rabin-Karp：  O(n + m)    平均；最壞 O(n·m)（雜湊碰撞）
    Boyer-Moore： O(n/m)      最好情況；實務上最快，grep 就在用

本題 n, m ≤ 10⁴，所以暴力法 10⁸ 次比較 ——
在 LeetCode 上「大概」會過，但不保證。
而且面試官問這題八成是想聽 KMP。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：haystack = "sadbutsad", needle = "sad"
  輸出：0
  說明："sad" 在索引 0 和 6 都出現，回傳第一個。

範例 2
  輸入：haystack = "leetcode", needle = "leeto"
  輸出：-1""",
 "constraints": [
   "1 ≤ <code>haystack.length</code>, <code>needle.length</code> ≤ 10⁴",
   "<code>haystack</code> 和 <code>needle</code> 只含小寫英文字母",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>長度至少 1</strong>，所以題目保證不會出現空的 <code>needle</code>。"
       "但<strong>依照 C 的慣例，空 needle 應該回傳 0</strong>（空字串在任何位置都「出現」），"
       "我們的程式碼還是會處理它 —— 這是好習慣。",
       "<strong>n, m ≤ 10⁴</strong>：暴力法最壞 10⁸ 次字元比較。"
       "在 Python 裡可能 TLE，在 C++ 裡會過。KMP 的 2 × 10⁴ 則是瞬間。",
       "<strong>只有小寫字母（26 種）</strong>，所以 Boyer-Moore 的壞字元表只要 26 格。"
       "但真正會讓暴力法變慢的是「重複性高的字串」，例如 "
       "<code>haystack = \"aaa...a\"</code>、<code>needle = \"aaa...ab\"</code>。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P28_FIG, "0 0 640 332"),
 ],
 "approaches": [
   ap("解法一", "直接用內建函式（能過，但答不到重點）", [
     ("c", S["p28_builtin"]),
     "<code>str.find</code> 找不到時回傳 −1，剛好就是題目要的。"
     "（注意 <code>str.index</code> 找不到會拋 <code>ValueError</code>，不能用。）",
     "<strong>CPython 的 <code>find</code> 用的是一個混合演算法</strong>"
     "（Crochemore-Perrin 的 Two-Way algorithm 加上 Bloom filter 式的壞字元跳躍），"
     "最壞情況是 O(n + m)。所以效能完全沒問題。",
     "但面試時寫這一行就結束，等於什麼都沒展示。<strong>至少要能寫出解法二，最好能寫解法三。</strong>",
   ], "O(n + m)", "O(1)", "CPython 的 Two-Way 演算法", "—"),

   ap("解法二", "暴力比對（先確保會寫）", [
     ("c", S["p28_naive"]),
     ("h", "為什麼外層是 <code>range(n - m + 1)</code>？"),
     ("c", """起點 i 必須滿足 i + m <= n，也就是 i <= n - m。
所以 range 的上界是 n - m + 1。

  n = 5, m = 3  ->  i 可以是 0, 1, 2  ->  range(3) = range(5-3+1) ✔

如果寫 range(n)，i = 3 時會存取 haystack[3+2] = haystack[5] -> IndexError。
（在 Python 裡用切片 haystack[i:i+m] 不會錯，
  但會安靜地比較一個長度不足的字串，結果還是對，只是多做白工。）"""),
     ("h", "最壞情況長什麼樣？"),
     ("c", """haystack = "aaaaaaaaaa...a"   （n 個 a）
needle   = "aaaa...ab"           （m-1 個 a 加一個 b）

每一個起點都會比對到最後一個字元才失敗：
    n - m + 1 個起點 × m 次比較 = O(n·m)

n = m = 10⁴ 的話是 10⁸ 次 —— 這就是 KMP 要解決的問題。

注意：一般的英文文字不會觸發這個最壞情況，
      暴力法在真實資料上通常很快。
      但「通常很快」和「保證很快」是兩回事。"""),
   ], "O(n·m) 最壞", "O(1)", "每個起點最多比 m 次", "只用兩個下標"),

   ap("解法三", "KMP（線性時間的標準答案）", [
     "暴力法的浪費在於：配對失敗時，<strong>把已經比對過的資訊全部丟掉</strong>，"
     "haystack 的指標退回去重來。KMP 的洞察是：<strong>那些資訊可以用來決定「該滑多遠」。</strong>",
     ("h", "第 1 步：next 表（failure function）"),
     ("c", """nxt[i] 定義：
    needle[0..i] 這個前綴裡，
    「既是真前綴、又是真後綴」的最長字串的長度。

    （「真」= proper = 不能是整個字串自己）

needle = "aabaaac"

  i  前綴        最長的「前綴=後綴」        nxt[i]
  0  "a"         （沒有真前綴）              0
  1  "aa"        "a"                        1
  2  "aab"       （無）                      0
  3  "aaba"      "a"                        1
  4  "aabaa"     "aa"                       2
  5  "aabaaa"    "aa"                       2
  6  "aabaaac"   （無）                      0

  nxt = [0, 1, 0, 1, 2, 2, 0]

為什麼這個表有用？

  假設我們配到 needle[0..4] = "aabaa" 都成功，
  第 5 個字元失敗了。

  已配對的 "aabaa" 的後綴 "aa" 同時也是前綴，
  所以我們可以直接假設「needle 的前 2 個字元已經配好了」，
  從 k = 2 繼續比 —— 不必回頭重比。

  這就是 nxt[4] = 2 的意義。"""),
     ("h", "第 2 步：用 next 表掃描"),
     ("c", S["p28_kmp"]),
     ("h", "為什麼 while 而不是 if？"),
     ("c", """while k > 0 and haystack[i] != needle[k]:
    k = nxt[k - 1]

退一次可能還是配不上，要繼續退，直到配上或退到 0。

例子：needle = "aabaaac"，nxt = [0,1,0,1,2,2,0]
      配到 k = 5（"aabaaa" 都對），第 6 個字元 haystack[i] = 'b'
      needle[5] = 'a' != 'b'
        -> k = nxt[4] = 2，needle[2] = 'b' == 'b' ✔ 配上了，k = 3

如果 haystack[i] 是 'x'：
        -> k = nxt[4] = 2，needle[2] = 'b' != 'x'
        -> k = nxt[1] = 1，needle[1] = 'a' != 'x'
        -> k = nxt[0] = 0，跳出 while（k == 0）
        -> needle[0] = 'a' != 'x'，k 保持 0

每次退都讓 k 變小，而 k 每輪最多 +1 ——
所以「退」的總次數不會超過「加」的總次數，也就是 O(n)。
這又是一次攤還分析。"""),
     ("h", "建表的迴圈和掃描的迴圈幾乎一模一樣"),
     "這不是巧合。<strong>建 next 表 = 拿 needle 去比對它自己</strong>"
     "（從第 1 個字元開始，用同一套「失配就退」的邏輯）。"
     "認出這一點之後，KMP 就只剩一個要記的迴圈，而不是兩個。",
     ("h", "複雜度"),
     "建表 O(m)、掃描 O(n)，總共 <strong>O(n + m)</strong>，"
     "而且 <strong>haystack 的指標 <code>i</code> 從頭到尾只往前走，絕不回頭</strong>。"
     "這個性質讓 KMP 可以用在<strong>串流</strong>上 —— 資料一個字元一個字元進來，"
     "不能倒帶也沒關係。",
   ], "O(n + m)", "O(m)", "建表 O(m) + 掃描 O(n)", "next 表", optimal=True),
 ],
 "compare": (["解法", "最壞時間", "空間", "指標會回頭？", "備註"],
   [["一、內建 find", "O(n+m)", "O(1)", "—", "能過，但沒展示能力"],
    ["二、暴力", "O(n·m)", "O(1)", "會", "先寫它確保正確"],
    ["三、KMP", "O(n+m)", "O(m)", "不會", "面試想聽的答案；可用於串流"]]),
 "edges": [
   "<strong>needle 比 haystack 長</strong>：<code>(\"a\", \"ab\")</code> → −1。"
   "<code>range(n-m+1)</code> 會是空的（<code>range(0)</code>），自然回 −1。",
   "<strong>needle 是空字串</strong>：→ 0。題目保證不會，但依慣例要處理。",
   "<strong>完全相等</strong>：<code>(\"abab\", \"abab\")</code> → 0。",
   "<strong>出現在最後</strong>：<code>(\"aaab\", \"ab\")</code> → 2。",
   "<strong>多次出現</strong>：<code>(\"sadbutsad\", \"sad\")</code> → 0（回第一個）。",
   "<strong>KMP 的經典測資</strong>：<code>(\"aabaaabaaac\", \"aabaaac\")</code> → 4。"
   "這筆會把 next 表的每一種退回都走一遍。",
   "<strong>暴力法的最壞情況</strong>：<code>\"a\"×10000</code> 配 <code>\"a\"×9999+\"b\"</code>。",
 ],
 "follow": [
   ("h", "追問一：如果要找「所有」出現位置呢？"),
   "KMP 只要改一行：找到之後不要 return，而是記錄位置並把 <code>k = nxt[k-1]</code>"
   "（退到最長的邊界，繼續往下找）。這樣可以找出所有位置，包含<strong>重疊</strong>的，"
   "而且總複雜度還是 O(n + m)。",
   ("h", "追問二：如果要在同一個 haystack 裡搜很多不同的 needle 呢？"),
   "KMP 是為「一個 pattern」設計的。多個 pattern 要用 <strong>Aho-Corasick</strong>"
   "（把所有 pattern 建成一棵 Trie，再在 Trie 上建 failure link —— "
   "本質上就是「Trie 版的 KMP」）。"
   "複雜度是 O(所有 pattern 總長 + n + 匹配數)。防毒軟體和 grep 的多模式搜尋都用它。",
   ("h", "追問三：如果 pattern 固定但 haystack 有無限多個呢？"),
   "那就<strong>預先建好 next 表</strong>，之後每個 haystack 只要 O(n)。"
   "或者更進一步，把 next 表編譯成一個 <strong>DFA</strong>（每個狀態對每個字元都有明確的轉移），"
   "這樣連 while 迴圈都不用，每個字元恰好一次查表。"
   "代價是 O(m × 字元集大小) 的表 —— 對 26 個小寫字母是 26m，很划算。",
   ("h", "追問四：實務上真的會用 KMP 嗎？"),
   "<strong>其實不太會。</strong>"
   "grep、Python 的 <code>str.find</code>、C++ 的 <code>std::search</code> "
   "大多用 Boyer-Moore 系列或 Two-Way algorithm。"
   "原因是：Boyer-Moore <strong>從 pattern 的尾巴往前比</strong>，失配時可以一口氣跳過 m 格，"
   "平均複雜度是 <strong>次線性</strong>的 O(n/m) —— 比 KMP 的 O(n) 還快。"
   "KMP 的價值在於<strong>最壞情況的保證</strong>和<strong>不需要回頭</strong>（串流友善），"
   "以及它是 Aho-Corasick、Z-algorithm、後綴自動機這一整條路線的起點。",
 ],
 "related": [
   "<strong>第 214 題 Shortest Palindrome</strong> —— KMP 的 next 表的巧妙應用",
   "<strong>第 459 題 Repeated Substring Pattern</strong> —— 一行 KMP 就解決",
   "<strong>第 686 題 Repeated String Match</strong> —— 字串搜尋的變形",
   "<strong>第 30 題 Substring with Concatenation of All Words</strong> —— 另一種子串搜尋",
 ],
 "check": [
   "<code>needle = \"aabaaac\"</code> 的 next 表是什麼？請自己算一遍。",
   "為什麼 KMP 的掃描迴圈裡用 <code>while</code> 而不是 <code>if</code>？",
   "KMP 的總複雜度為什麼是 O(n+m) 而不是 O(n·m)？請用攤還分析說明。",
   "為什麼「建 next 表」和「掃描」的程式碼長得幾乎一樣？",
 ],
})
print("P28 written")
