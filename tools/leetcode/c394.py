# -*- coding: utf-8 -*-
"""第 394–400 題。"""
import random
import functools
from collections import Counter, defaultdict, deque
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(394)


# ==================== 394. Decode String ====================
S["p394"] = '''class Solution:
    def decodeString(self, s: str) -> str:
        stack = []                    # 進入括號前的 (目前字串, 重複次數)
        cur, num = "", 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)          # 次數可能是多位數
            elif ch == "[":
                stack.append((cur, num))          # ★ 暫存外層，括號內從空字串開始
                cur, num = "", 0
            elif ch == "]":
                prev, k = stack.pop()
                cur = prev + cur * k              # 括號內重複 k 次，接回外層
            else:
                cur += ch
        return cur'''

S["p394_rec"] = '''class Solution:
    def decodeString(self, s: str) -> str:
        i = 0

        def parse() -> str:                       # 讀到 "]" 或結尾為止
            nonlocal i
            out = []
            while i < len(s) and s[i] != "]":
                if s[i].isdigit():
                    k = 0
                    while s[i].isdigit():
                        k = k * 10 + int(s[i])
                        i += 1
                    i += 1                        # 跳過 "["
                    inner = parse()
                    i += 1                        # 跳過 "]"
                    out.append(inner * k)
                else:
                    out.append(s[i])
                    i += 1
            return "".join(out)

        return parse()'''

_p394 = [S.load(x) for x in ("p394", "p394_rec")]


def _enc(d=0):
    parts = []
    plain = []
    for _ in range(random.randrange(1, 4)):
        if d < 3 and random.random() < 0.4:
            k = random.randint(1, 12)
            e, p = _enc(d + 1)
            parts.append(f"{k}[{e}]")
            plain.append(p * k)
        else:
            c = random.choice("abc")
            parts.append(c)
            plain.append(c)
    return "".join(parts), "".join(plain)


for s, want in [("3[a]2[bc]", "aaabcbc"), ("3[a2[c]]", "accaccacc"), ("2[abc]3[cd]ef", "abcabccdcdcdef"), ("10[a]", "a" * 10)]:
    for sol in _p394:
        assert sol.decodeString(s) == want
for _ in range(2000):
    e, p = _enc()
    for sol in _p394:
        assert sol.decodeString(e) == p, e
print("P394 OK")

emit({
 "num": 394, "slug": "decode-string",
 "en": [
   "Given an encoded string, return its decoded string.",
   "The encoding rule is: <code>k[encoded_string]</code>, where the <code>encoded_string</code> inside the square brackets is being repeated exactly <code>k</code> times. Note that <code>k</code> is guaranteed to be a positive integer.",
   "You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. "
   "Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, <code>k</code>. For example, there will not be input like <code>3a</code> or <code>2[4]</code>.",
 ],
 "zh": [
   "給你一個編碼過的字串，回傳解碼後的結果。",
   "編碼規則：<code>k[encoded_string]</code> 代表方括號內的字串重複 <code>k</code> 次（<code>k</code> 是正整數）。括號可以巢狀。",
   "輸入保證合法：沒有多餘空白、括號配對正確；原始資料中不含數字，數字只用來表示重複次數。",
 ],
 "examples": """範例 1
  輸入：s = "3[a]2[bc]"
  輸出："aaabcbc"

範例 2
  輸入：s = "3[a2[c]]"
  輸出："accaccacc"

範例 3
  輸入：s = "2[abc]3[cd]ef"
  輸出："abcabccdcdcdef\"""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 30",
   "<code>s</code> 由小寫英文字母、數字、<code>'['</code>、<code>']'</code> 組成",
   "所有整數都在 <code>[1, 300]</code> 之間",
   "輸出長度不超過 10⁵",
 ],
 "idea": [
   ("c", """【巢狀括號 -> 堆疊（第 224 題的同一個套路）】
    cur = 目前這一層正在組的字串
    num = 正在讀的重複次數

    '['：把 (cur, num) 推進堆疊，括號內從空字串重新開始
    ']'：彈出 (prev, k)，cur = prev + cur × k
    字母：cur += ch
    數字：num = num × 10 + d（次數可能是多位數，例如 10[a]）

【模擬】s = "3[a2[c]]"
    讀 3         num=3
    讀 [         push ("", 3)        cur=""
    讀 a         cur="a"
    讀 2         num=2
    讀 [         push ("a", 2)       cur=""
    讀 c         cur="c"
    讀 ]         pop ("a", 2)        cur = "a" + "c"×2 = "acc"
    讀 ]         pop ("", 3)         cur = "" + "acc"×3 = "accaccacc" ✔"""),
 ],
 "approaches": [
   ap("解法一", "堆疊", [
     ("c", S["p394"]),
   ], "O(輸出長度)", "O(輸出長度)", "", "", optimal=True),

   ap("解法二", "遞迴下降", [
     ("c", S["p394_rec"]),
   ], "O(輸出長度)", "O(輸出長度)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、堆疊", "O(輸出)", "迭代 ✔"],
    ["二、遞迴", "O(輸出)", "結構最直觀"]]),
 "edges": [
   "<strong>多位數次數</strong>（<code>10[a]</code>）→ 數字要累積。",
   "<strong>括號外的字母</strong>（<code>2[a]bc</code>）→ 直接接在 cur 後面。",
   "<strong>巢狀</strong> → 堆疊處理。",
 ],
 "follow": [
   ("h", "效率"),
   ("c", "Python 字串串接每次都建立新字串；深層巢狀時用串列收集再 join 會更快。輸出最多 10⁵ 個字元，本題兩種寫法都夠快。"),
 ],
 "related": [
   "<strong>第 224 題 基本計算器</strong>",
   "<strong>第 385 題 迷你語法分析器</strong>",
   "<strong>第 726 題 原子的數量</strong>",
 ],
 "check": [
   "遇到 '[' 時要把什麼推進堆疊？",
   "遇到 ']' 時怎麼組合出新的字串？",
   "重複次數是多位數時怎麼處理？",
 ],
})


# ==================== 395. Longest Substring with At Least K Repeating Characters ====================
S["p395"] = '''class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        cnt = collections.Counter(s)
        for ch, c in cnt.items():
            if c < k:
                # ★ 出現次數不到 k 的字元，不可能在任何答案裡 -> 用它把字串切開，分別求解
                return max(self.longestSubstring(part, k) for part in s.split(ch))
        return len(s)                          # 每個字元都 >= k 次：整段都合格'''

S["p395_window"] = '''class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        best = 0
        # 枚舉「子字串中恰好有 t 種不同字元」，t = 1..26，每種做一次滑動視窗
        for t in range(1, len(set(s)) + 1):
            cnt = collections.Counter()
            left = kinds = enough = 0          # 種類數、次數 >= k 的種類數
            for right, ch in enumerate(s):
                if cnt[ch] == 0:
                    kinds += 1
                cnt[ch] += 1
                if cnt[ch] == k:
                    enough += 1
                while kinds > t:               # 種類太多：縮左邊
                    c = s[left]
                    if cnt[c] == k:
                        enough -= 1
                    cnt[c] -= 1
                    if cnt[c] == 0:
                        kinds -= 1
                    left += 1
                if kinds == t == enough:       # 每種字元都至少 k 次
                    best = max(best, right - left + 1)
        return best'''

_p395 = [S.load(x) for x in ("p395", "p395_window")]


def _lsk_ref(s, k):
    best = 0
    for i in range(len(s)):
        c = Counter()
        for j in range(i, len(s)):
            c[s[j]] += 1
            if min(c.values()) >= k:
                best = max(best, j - i + 1)
    return best


for s, k, want in [("aaabb", 3, 3), ("ababbc", 2, 5), ("a", 2, 0)]:
    for sol in _p395:
        assert sol.longestSubstring(s, k) == want
for _ in range(2000):
    s = "".join(random.choice("abc") for _ in range(random.randrange(1, 12)))
    k = random.randint(1, 4)
    want = _lsk_ref(s, k)
    for sol in _p395:
        assert sol.longestSubstring(s, k) == want, (s, k, sol)
print("P395 OK")

emit({
 "num": 395, "slug": "longest-substring-with-at-least-k-repeating-characters",
 "en": [
   "Given a string <code>s</code> and an integer <code>k</code>, return <em>the length of the longest substring of</em> <code>s</code> <em>such that the frequency of each character in this substring is greater than or equal to</em> <code>k</code>.",
   "If no such substring exists, return 0.",
 ],
 "zh": [
   "給你一個字串 <code>s</code> 和整數 <code>k</code>，找出最長的子字串，使得其中<strong>每一種字元</strong>都出現<strong>至少 <code>k</code> 次</strong>。回傳它的長度；不存在時回傳 0。",
 ],
 "examples": """範例 1
  輸入：s = "aaabb", k = 3
  輸出：3
  說明："aaa"

範例 2
  輸入：s = "ababbc", k = 2
  輸出：5
  說明："ababb"，a 出現 2 次、b 出現 3 次。""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁴",
   "<code>s</code> 只包含小寫英文字母",
   "1 ≤ <code>k</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【一般的滑動視窗為什麼不行？】
    視窗擴大時，新字元可能讓條件從「滿足」變「不滿足」，
    再擴大又可能變回「滿足」——沒有單調性，無法決定何時縮左邊。

【方法一：分治】
    如果某個字元在整個字串中出現次數 < k，
    它不可能出現在任何答案裡 ->
    用它把字串切開，答案一定在某一段裡面，分別遞迴。
    如果所有字元都 >= k 次，整個字串就是答案。

    每一層至少排除一種字元 -> 遞迴深度最多 26 -> O(26n)。

【方法二：枚舉種類數 + 滑動視窗】
    加一個限制來創造單調性：
    「子字串恰好有 t 種不同字元」，t = 1..26。
    固定 t 之後：種類數 > t 就縮左邊 —— 有單調性了！
    視窗內種類數 == t 且每種都 >= k 次 -> 更新答案。
    26 次滑動視窗 -> O(26n)。"""),
 ],
 "approaches": [
   ap("解法一", "分治（用不合格的字元切開）", [
     ("c", S["p395"]),
   ], "O(26 · n)", "O(26 · n)", "遞迴深度 ≤ 26", "", optimal=True),

   ap("解法二", "枚舉種類數 + 滑動視窗", [
     ("c", S["p395_window"]),
   ], "O(26 · n)", "O(26)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["暴力", "O(26 · n²)", "O(26)", "超時"],
    ["一、分治", "O(26n)", "O(26n)", "最短 ✔"],
    ["二、枚舉種類數", "O(26n)", "O(26)", "創造單調性的技巧"]]),
 "edges": [
   "<strong>k = 1</strong> → 整個字串。",
   "<strong>k &gt; 字串長度</strong> → 0。",
   "<strong>每個字元都不夠 k 次</strong> → 0。",
 ],
 "follow": [
   ("h", "「枚舉一個額外參數來創造單調性」"),
   ("c", "當滑動視窗缺少單調性時，固定一個小範圍的參數（這裡是種類數 1..26）往往能讓它恢復單調。第 1100、第 2062 題也用類似技巧。"),
 ],
 "related": [
   "<strong>第 3 題 無重複字元的最長子字串</strong>",
   "<strong>第 340 題 至多包含 K 個不同字元的最長子字串</strong>（付費）",
   "<strong>第 1763 題 最長的美好子字串</strong> —— 同樣的分治",
 ],
 "check": [
   "為什麼這題不能直接用滑動視窗？",
   "分治時為什麼可以用出現次數不到 k 的字元切開字串？",
   "枚舉種類數 t 之後，為什麼滑動視窗就有單調性了？",
 ],
})


# ==================== 396. Rotate Function ====================
S["p396"] = '''class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        f = sum(i * x for i, x in enumerate(nums))      # F(0)
        best = f
        for k in range(1, n):
            # ★ 每旋轉一次：所有係數 +1（多加 total），最後一個元素的係數從 n-1 變 0
            f = f + total - n * nums[n - k]
            best = max(best, f)
        return best'''

_p396 = S.load("p396")
for nums, want in [([4, 3, 2, 6], 26), ([100], 0)]:
    assert _p396.maxRotateFunction(nums) == want
for _ in range(2000):
    a = [random.randint(-9, 9) for _ in range(random.randrange(1, 10))]
    n = len(a)
    want = max(sum(i * a[(i - k) % n] for i in range(n)) for k in range(n))
    assert _p396.maxRotateFunction(a) == want
print("P396 OK")

emit({
 "num": 396, "slug": "rotate-function",
 "en": [
   "You are given an integer array <code>nums</code> of length <code>n</code>.",
   "Assume <code>arr<sub>k</sub></code> to be an array obtained by rotating <code>nums</code> by <code>k</code> positions clock-wise. We define the <strong>rotation function</strong> <code>F</code> on <code>nums</code> as follow:",
   ("ul", ["<code>F(k) = 0 * arr<sub>k</sub>[0] + 1 * arr<sub>k</sub>[1] + ... + (n - 1) * arr<sub>k</sub>[n - 1].</code>"]),
   "Return <em>the maximum value of</em> <code>F(0), F(1), ..., F(n-1)</code>.",
 ],
 "zh": [
   "給你一個長度為 <code>n</code> 的整數陣列 <code>nums</code>。",
   "<code>arr<sub>k</sub></code> 是把 <code>nums</code> 順時針旋轉 <code>k</code> 個位置得到的陣列（往右轉，最後一個移到最前面）。定義",
   ("ul", ["<code>F(k) = 0 × arr<sub>k</sub>[0] + 1 × arr<sub>k</sub>[1] + ... + (n − 1) × arr<sub>k</sub>[n − 1]</code>"]),
   "回傳 <code>F(0), F(1), ..., F(n−1)</code> 中的最大值。",
 ],
 "examples": """範例 1
  輸入：nums = [4,3,2,6]
  輸出：26
  說明：
    F(0) = 0×4 + 1×3 + 2×2 + 3×6 = 25
    F(1) = 0×6 + 1×4 + 2×3 + 3×2 = 16
    F(2) = 0×2 + 1×6 + 2×4 + 3×3 = 23
    F(3) = 0×3 + 1×2 + 2×6 + 3×4 = 26

範例 2
  輸入：nums = [100]
  輸出：0""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 10⁵",
   "−100 ≤ <code>nums[i]</code> ≤ 100",
 ],
 "idea": [
   ("c", """【暴力：每個 F(k) 都 O(n) 算 -> O(n²)，太慢】

【找 F(k) 和 F(k-1) 的關係】
    旋轉一次（往右）：
        大部分元素往右移一格 -> 係數 +1
        最後一個元素移到最前面 -> 係數從 n-1 變成 0

    F(k) = F(k-1) + (所有元素各加一次) - n × (被移到最前面的那個)
         = F(k-1) + total - n × nums[n - k]

    為什麼是 - n × x 而不是 - (n-1) × x？
    「所有元素各加一次」也幫它加了 1，
    它原本係數 n-1，加 1 變 n，再變成 0 -> 要減 n。

【範例】nums = [4, 3, 2, 6]，total = 15
    F(0) = 25
    F(1) = 25 + 15 - 4×6 = 16
    F(2) = 16 + 15 - 4×2 = 23
    F(3) = 23 + 15 - 4×3 = 26 ✔"""),
 ],
 "approaches": [
   ap("解法", "遞推公式", [
     ("c", S["p396"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>n = 1</strong> → 0。",
   "<strong>負數</strong> → 最大值可能是負的，初始值要用 F(0) 而不是 0。",
   "<strong>其他語言的溢位</strong> → n × 100 × n 可達 10¹²，要用 64 位元。",
 ],
 "follow": [
   ("h", "「相鄰狀態的差」技巧"),
   ("c", "不重算整個值，只算變化量——第 1423 題（可獲得的最大點數）、第 2121 題（相同元素的間隔之和）、換根 DP 都是這個思路。"),
 ],
 "related": [
   "<strong>第 189 題 輪轉陣列</strong>",
   "<strong>第 834 題 樹中距離之和</strong> —— 換根 DP，同樣的「遞推變化量」",
 ],
 "check": [
   "F(k) 和 F(k−1) 差多少？",
   "為什麼被移到最前面的元素要減 n 倍而不是 n−1 倍？",
 ],
})


# ==================== 397. Integer Replacement ====================
S["p397"] = '''class Solution:
    def integerReplacement(self, n: int) -> int:
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            elif n == 3 or n % 4 == 1:   # ★ 二進位結尾是 01（或 n = 3）：減 1
                n -= 1
            else:                        # 結尾是 11：加 1，可以一次消掉一串 1
                n += 1
            steps += 1
        return steps'''

S["p397_memo"] = '''class Solution:
    def integerReplacement(self, n: int) -> int:
        @functools.lru_cache(None)
        def f(x: int) -> int:
            if x == 1:
                return 0
            if x % 2 == 0:
                return 1 + f(x // 2)
            # 奇數：+1 或 -1 之後一定是偶數，直接合併成兩步
            return 2 + min(f((x + 1) // 2), f((x - 1) // 2))
        return f(n)'''

_p397 = [S.load(x) for x in ("p397", "p397_memo")]
for n, want in [(8, 3), (7, 4), (4, 2), (1, 0), (3, 2), (2 ** 31 - 1, 32)]:
    for sol in _p397:
        assert sol.integerReplacement(n) == want, (n, sol)


def _ir_bfs(n):
    dist = {n: 0}
    dq = deque([n])
    while dq:
        x = dq.popleft()
        if x == 1:
            return dist[x]
        nxt = [x // 2] if x % 2 == 0 else [x + 1, x - 1]
        for y in nxt:
            if y not in dist:
                dist[y] = dist[x] + 1
                dq.append(y)


for n in range(1, 3000):
    want = _ir_bfs(n)
    for sol in _p397:
        assert sol.integerReplacement(n) == want, n
print("P397 OK")

emit({
 "num": 397, "slug": "integer-replacement",
 "en": [
   "Given a positive integer <code>n</code>, you can apply one of the following operations:",
   ("ol", ["If <code>n</code> is even, replace <code>n</code> with <code>n / 2</code>.",
           "If <code>n</code> is odd, replace <code>n</code> with either <code>n + 1</code> or <code>n - 1</code>."]),
   "Return <em>the minimum number of operations needed for</em> <code>n</code> <em>to become</em> <code>1</code>.",
 ],
 "zh": [
   "給你一個正整數 <code>n</code>，每一步可以：",
   ("ol", ["<code>n</code> 是偶數：變成 <code>n / 2</code>。",
           "<code>n</code> 是奇數：變成 <code>n + 1</code> 或 <code>n − 1</code>。"]),
   "回傳讓 <code>n</code> 變成 <code>1</code> 的最少步數。",
 ],
 "examples": """範例 1
  輸入：n = 8
  輸出：3
  說明：8 -> 4 -> 2 -> 1

範例 2
  輸入：n = 7
  輸出：4
  說明：7 -> 8 -> 4 -> 2 -> 1（或 7 -> 6 -> 3 -> 2 -> 1）

範例 3
  輸入：n = 4
  輸出：2""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【偶數沒得選：除以 2】
    只有奇數要決定 +1 還是 -1。

【方法一：記憶化遞迴】
    奇數 x：+1 或 -1 之後一定是偶數，下一步一定除以 2，
    所以可以直接跳兩步：2 + min(f((x+1)/2), f((x-1)/2))。
    每一層規模減半 -> 狀態數 O(log n)。

【方法二：看二進位的貪心】
    除以 2 = 去掉最低位的 0。目標是盡快把 1 消掉。
    奇數的結尾是 ...01 或 ...11：
        ...01：減 1 -> ...00，接下來可以連除兩次 ✔
        ...11：加 1 -> 進位會把一串 1 變成 0（例如 0111 + 1 = 1000）✔
    唯一的例外：n = 3（11）
        3 -> 4 -> 2 -> 1 要 3 步
        3 -> 2 -> 1 只要 2 步 -> 應該減 1。

【Python 不用擔心溢位】
    n = 2³¹ - 1 加 1 在其他語言會溢位，要用 long。"""),
   ("t", ["n", "二進位", "選擇", "理由"],
    [["5", "101", "−1", "結尾 01"],
     ["7", "111", "+1", "結尾 11 → 1000"],
     ["3", "11", "−1", "特例"],
     ["15", "1111", "+1", "→ 10000，再除 4 次"]]),
 ],
 "approaches": [
   ap("解法一", "記憶化遞迴", [
     ("c", S["p397_memo"]),
   ], "O(log n)", "O(log n)", "", ""),

   ap("解法二", "二進位貪心", [
     ("c", S["p397"]),
     "驗證方式：和 BFS 求出的真正最短步數，對 1 到 3000 全部比對。",
   ], "O(log n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、記憶化", "O(log n)", "O(log n)"],
    ["二、貪心", "O(log n)", "O(1) ✔"]]),
 "edges": [
   "<strong>n = 1</strong> → 0。",
   "<strong>n = 3</strong> → 特例，減 1。",
   "<strong>n = 2³¹ − 1</strong> → 加 1 會超過 32 位元（Python 沒問題），答案 32。",
 ],
 "follow": [
   ("h", "位元貪心"),
   ("c", "第 1404 題「將二進位表示減到 1 的步驟數」是同一個問題的簡化版（奇數只能加 1）。"),
 ],
 "related": [
   "<strong>第 1404 題 將二進位表示減到 1 的步驟數</strong>",
   "<strong>第 991 題 壞了的計算器</strong> —— 反向思考",
 ],
 "check": [
   "奇數時為什麼可以一次跳兩步？",
   "二進位結尾是 01 和 11 時分別該怎麼選？為什麼？",
   "n = 3 為什麼是例外？",
 ],
})


# ==================== 398. Random Pick Index ====================
S["p398"] = '''class Solution:
    def __init__(self, nums: List[int]):
        self.pos = collections.defaultdict(list)   # 值 -> 所有出現的索引
        for i, x in enumerate(nums):
            self.pos[x].append(i)

    def pick(self, target: int) -> int:
        return random.choice(self.pos[target])'''

S["p398_reservoir"] = '''class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums                          # 不做預處理

    def pick(self, target: int) -> int:
        count, chosen = 0, -1
        for i, x in enumerate(self.nums):
            if x == target:
                count += 1
                if random.randrange(count) == 0:  # ★ 蓄水池抽樣：第 count 個以 1/count 的機率取代
                    chosen = i
        return chosen'''

for key in ("p398", "p398_reservoir"):
    cls = S.loadns(key)["Solution"]
    obj = cls([1, 2, 3, 3, 3])
    cnt = Counter(obj.pick(3) for _ in range(30000))
    assert set(cnt) == {2, 3, 4} and all(9000 < c < 11000 for c in cnt.values()), (key, cnt)
    assert obj.pick(1) == 0
print("P398 OK")

emit({
 "num": 398, "slug": "random-pick-index",
 "en": [
   "Given an integer array <code>nums</code> with possible <strong>duplicates</strong>, randomly output the index of a given <code>target</code> number. You can assume that the given target number must exist in the array.",
   "Implement the <code>Solution</code> class:",
   ("ul", ["<code>Solution(int[] nums)</code> Initializes the object with the array <code>nums</code>.",
           "<code>int pick(int target)</code> Picks a random index <code>i</code> from <code>nums</code> where <code>nums[i] == target</code>. If there are multiple valid i's, then each index should have an equal probability of returning."]),
 ],
 "zh": [
   "給你一個可能有<strong>重複</strong>元素的整數陣列 <code>nums</code>。",
   "<code>pick(target)</code>：在所有 <code>nums[i] == target</code> 的索引中，<strong>等機率</strong>隨機回傳一個。保證 target 一定存在。",
 ],
 "examples": """範例
  Solution([1, 2, 3, 3, 3])
  pick(3) -> 2、3、4 各 1/3 機率
  pick(1) -> 0""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 2 × 10⁴",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
   "<code>target</code> 一定在 <code>nums</code> 中",
   "最多呼叫 10⁴ 次 <code>pick</code>",
 ],
 "idea": [
   ("c", """【方法一：預處理雜湊表】
    值 -> 所有出現的索引。
    pick 時直接 random.choice，O(1)。
    需要 O(n) 額外空間。

【方法二：蓄水池抽樣（第 382 題）】
    不做預處理，每次 pick 掃一遍陣列：
    遇到第 c 個等於 target 的索引，以 1/c 的機率選它。
    O(1) 額外空間，但每次 pick 要 O(n)。

【怎麼選？】
    這題原本的設計意圖是蓄水池抽樣（陣列很大、記憶體有限）。
    但以題目的數據範圍，雜湊表版本實際上快很多。"""),
 ],
 "approaches": [
   ap("解法一", "雜湊表存索引", [
     ("c", S["p398"]),
   ], "建構 O(n)，pick O(1)", "O(n)", "", "", optimal=True),

   ap("解法二", "蓄水池抽樣", [
     ("c", S["p398_reservoir"]),
   ], "pick O(n)", "O(1)", "", ""),
 ],
 "compare": (["解法", "pick", "額外空間", "適用"],
   [["一、雜湊表", "O(1)", "O(n)", "查詢多 ✔"],
    ["二、蓄水池", "O(n)", "O(1)", "記憶體有限、資料流"]]),
 "edges": [
   "<strong>target 只出現一次</strong> → 永遠回傳那個索引。",
   "<strong>所有元素都相同</strong> → 每個索引各 1/n。",
 ],
 "follow": [
   ("h", "隨機演算法家族"),
   ("c", "第 382 題（串列隨機節點）、第 384 題（洗牌）、第 398 題（本題）、第 528 題（依權重抽樣：前綴和 + 二分）、第 470 題（用 rand7 做 rand10：拒絕抽樣）。"),
 ],
 "related": [
   "<strong>第 382 題 鏈結串列隨機節點</strong>",
   "<strong>第 528 題 按權重隨機選擇</strong>",
   "<strong>第 710 題 黑名單中的隨機數</strong>",
 ],
 "check": [
   "兩種方法在時間和空間上各有什麼取捨？",
   "蓄水池抽樣中，第 c 個符合條件的索引被選中的機率是多少？",
 ],
})


# ==================== 399. Evaluate Division ====================
S["p399"] = '''class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        parent, weight = {}, {}          # ★ weight[x] = x / parent[x]

        def find(x: str) -> str:
            if parent[x] != x:
                root = find(parent[x])
                weight[x] *= weight[parent[x]]   # 路徑壓縮時，比值沿路相乘
                parent[x] = root
            return parent[x]

        def union(a: str, b: str, v: float) -> None:    # a / b = v
            for x in (a, b):
                if x not in parent:
                    parent[x], weight[x] = x, 1.0
            ra, rb = find(a), find(b)
            if ra != rb:
                # 讓 ra 掛到 rb 下：ra / rb = (b / rb) × (a / b) / (a / ra)
                parent[ra] = rb
                weight[ra] = weight[b] * v / weight[a]

        for (a, b), v in zip(equations, values):
            union(a, b, v)

        res = []
        for a, b in queries:
            if a not in parent or b not in parent or find(a) != find(b):
                res.append(-1.0)
            else:
                res.append(weight[a] / weight[b])        # (a / root) / (b / root)
        return res'''

S["p399_bfs"] = '''class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)    # graph[a][b] = a / b
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1 / v

        def bfs(src: str, dst: str) -> float:
            if src not in graph or dst not in graph:
                return -1.0
            q = collections.deque([(src, 1.0)])     # (節點, src / 節點)
            seen = {src}
            while q:
                x, ratio = q.popleft()
                if x == dst:
                    return ratio
                for y, v in graph[x].items():         # x / y = v -> src / y = ratio × v
                    if y not in seen:
                        seen.add(y)
                        q.append((y, ratio * v))
            return -1.0

        return [bfs(a, b) for a, b in queries]'''

_p399 = [S.load(x) for x in ("p399", "p399_bfs")]
E = [["a", "b"], ["b", "c"]]
V = [2.0, 3.0]
Q = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
for sol in _p399:
    got = sol.calcEquation(E, V, Q)
    assert all(abs(g - w) < 1e-9 for g, w in zip(got, [6.0, 0.5, -1.0, 1.0, -1.0])), (got, sol)
for _ in range(1000):
    names = [chr(97 + i) for i in range(random.randrange(2, 7))]
    val = {x: random.choice([1, 2, 3, 5, 0.5, 4]) * random.choice([1, 10]) for x in names}
    eqs, vs = [], []
    for _ in range(random.randrange(1, 6)):
        a, b = random.sample(names, 2)
        eqs.append([a, b]); vs.append(val[a] / val[b])
    qs = [[random.choice(names + ["z"]), random.choice(names + ["z"])] for _ in range(6)]
    r1, r2 = (sol.calcEquation(eqs, vs, qs) for sol in _p399)
    for x, y in zip(r1, r2):
        assert abs(x - y) < 1e-6 * max(1, abs(x)), (eqs, qs, r1, r2)
print("P399 OK")

_P399_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">a / b = 2、b / c = 3：把變數當節點、除法當帶權重的邊</text>
            <g font-size="14" text-anchor="middle">
              <circle cx="90" cy="100" r="22" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="90" y="105" fill="var(--accent)">a</text>
              <circle cx="260" cy="100" r="22" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="260" y="105" fill="var(--accent)">b</text>
              <circle cx="430" cy="100" r="22" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="430" y="105" fill="var(--accent)">c</text>
            </g>
            <g stroke="var(--text-muted)" fill="none">
              <path d="M112 92 L238 92"/><path d="M238 108 L112 108"/>
              <path d="M282 92 L408 92"/><path d="M408 108 L282 108"/>
            </g>
            <g fill="var(--text-muted)">
              <polygon points="238,92 229,88 229,96"/><polygon points="112,108 121,104 121,112"/>
              <polygon points="408,92 399,88 399,96"/><polygon points="282,108 291,104 291,112"/>
            </g>
            <g font-size="12" text-anchor="middle">
              <text x="175" y="84" fill="var(--text)">× 2</text><text x="175" y="126" fill="var(--text-muted)">× 1/2</text>
              <text x="345" y="84" fill="var(--text)">× 3</text><text x="345" y="126" fill="var(--text-muted)">× 1/3</text>
            </g>
            <path d="M90 124 C 150 190, 370 190, 430 124" fill="none" stroke="var(--gold)" stroke-dasharray="5 4"/>
            <text x="260" y="194" text-anchor="middle" fill="var(--gold)" font-size="13">a / c = 2 × 3 = 6（沿路徑相乘）</text>
            <text x="480" y="80" fill="var(--text-muted)" font-size="12">邊 x → y 的權重</text>
            <text x="480" y="100" fill="var(--text-muted)" font-size="12">= x / y</text>
            <text x="480" y="130" fill="var(--text-muted)" font-size="12">不連通 → −1</text>'''

emit({
 "num": 399, "slug": "evaluate-division",
 "en": [
   "You are given an array of variable pairs <code>equations</code> and an array of real numbers <code>values</code>, where <code>equations[i] = [A<sub>i</sub>, B<sub>i</sub>]</code> and <code>values[i]</code> represent the equation <code>A<sub>i</sub> / B<sub>i</sub> = values[i]</code>. Each <code>A<sub>i</sub></code> or <code>B<sub>i</sub></code> is a string that represents a single variable.",
   "You are also given some <code>queries</code>, where <code>queries[j] = [C<sub>j</sub>, D<sub>j</sub>]</code> represents the <code>j<sup>th</sup></code> query where you must find the answer for <code>C<sub>j</sub> / D<sub>j</sub> = ?</code>.",
   "Return <em>the answers to all queries</em>. If a single answer cannot be determined, return <code>-1.0</code>.",
   "<strong>Note:</strong> The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.",
   "<strong>Note:</strong> The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.",
 ],
 "zh": [
   "給你一組等式 <code>equations[i] = [A, B]</code> 和對應的值 <code>values[i]</code>，代表 <code>A / B = values[i]</code>。每個 A、B 是一個變數名稱（字串）。",
   "再給你一些查詢 <code>queries[j] = [C, D]</code>，問 <code>C / D = ?</code>。",
   "回傳所有查詢的答案；無法確定的回傳 <code>-1.0</code>。沒出現在等式中的變數視為未定義（即使查詢 <code>x / x</code> 也回傳 −1）。",
   "輸入保證沒有矛盾、不會除以零。",
 ],
 "examples": """範例 1
  輸入：equations = [["a","b"],["b","c"]], values = [2.0,3.0],
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
  輸出：[6.0,0.5,-1.0,1.0,-1.0]
  說明：a/c = (a/b)(b/c) = 6；b/a = 1/2；e、x 沒有定義。""",
 "constraints": [
   "1 ≤ <code>equations.length</code> ≤ 20",
   "1 ≤ <code>queries.length</code> ≤ 20",
   "0.0 &lt; <code>values[i]</code> ≤ 20.0",
   "變數名稱由小寫字母和數字組成，長度 1 到 5",
 ],
 "idea": [
   ("fig", _P399_FIG, "0 0 640 210"),
   ("c", """【建圖】
    a / b = 2 -> 邊 a → b 權重 2、邊 b → a 權重 1/2
    查詢 x / y = 從 x 走到 y 的路徑上，權重的乘積。
        a / c = (a / b) × (b / c) = 2 × 3 = 6

【方法一：每次查詢做 BFS / DFS】
    沒有路徑（不在同一個連通分量）-> -1

【方法二：帶權重的並查集】
    weight[x] = x / parent[x]
    find 時做路徑壓縮，比值沿路相乘：x / root = (x / p) × (p / root)
    同一個連通分量裡，x / y = (x / root) / (y / root)

    合併 a / b = v 時（ra = find(a)、rb = find(b)）：
        要設定 weight[ra] = ra / rb
        ra / rb = (a / rb) / (a / ra) = (a / b) × (b / rb) / (a / ra)
                = v × weight[b] / weight[a]

【未定義的變數】
    即使是 x / x，只要 x 沒出現過就回傳 -1。"""),
 ],
 "approaches": [
   ap("解法一", "圖 + BFS", [
     ("c", S["p399_bfs"]),
   ], "O(Q · (V + E))", "O(V + E)", "", ""),

   ap("解法二", "帶權重的並查集", [
     ("c", S["p399"]),
   ], "O((E + Q) · α(V))", "O(V)", "近似 O(1) 的 find", "", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、BFS", "O(Q·(V+E))", "直觀"],
    ["二、帶權並查集", "O((E+Q)·α)", "查詢多時更快 ✔"]]),
 "edges": [
   "<strong>未定義的變數</strong>（即使 x / x）→ −1。",
   "<strong>a / a（有定義）</strong> → 1。",
   "<strong>不同的連通分量</strong> → −1。",
   "<strong>浮點誤差</strong> → 題目接受誤差。",
 ],
 "follow": [
   ("h", "帶權並查集的其他應用"),
   ("c", "第 990 題（等式方程的可滿足性，不帶權）、食物鏈問題（權重是「關係類型」mod 3）、第 2307 題（檢查方程中的矛盾）。"),
 ],
 "related": [
   "<strong>第 990 題 等式方程的可滿足性</strong>",
   "<strong>第 2307 題 檢查方程中的矛盾之處</strong>（付費）",
   "<strong>第 547 題 省份數量</strong> —— 並查集",
 ],
 "check": [
   "怎麼把等式轉成圖？邊的權重是什麼？",
   "帶權並查集中 weight[x] 代表什麼？路徑壓縮時怎麼更新？",
   "查詢一個沒出現過的變數除以它自己，答案是什麼？",
 ],
})


# ==================== 400. Nth Digit ====================
S["p400"] = '''class Solution:
    def findNthDigit(self, n: int) -> int:
        digits, count, start = 1, 9, 1       # 目前處理 digits 位數：共 count 個數，從 start 開始
        # ★ 第一步：找出第 n 個數字落在幾位數的區段
        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10
        # 第二步：找出是哪一個數
        num = start + (n - 1) // digits
        # 第三步：是那個數的第幾位
        return int(str(num)[(n - 1) % digits])'''

_p400 = S.load("p400")
_seq = "".join(str(i) for i in range(1, 30000))
for n in range(1, 100000):
    assert _p400.findNthDigit(n) == int(_seq[n - 1]), n
assert _p400.findNthDigit(2 ** 31 - 1) == 2
print("P400 OK")

emit({
 "num": 400, "slug": "nth-digit",
 "en": [
   "Given an integer <code>n</code>, return the <code>n<sup>th</sup></code> digit of the infinite integer sequence <code>[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]</code>.",
 ],
 "zh": [
   "把正整數依序寫成一串：<code>123456789101112...</code>，回傳這串數字中的第 <code>n</code> 個數字。",
 ],
 "examples": """範例 1
  輸入：n = 3
  輸出：3

範例 2
  輸入：n = 11
  輸出：0
  說明：1 2 3 4 5 6 7 8 9 1 0 1 1 ...
        第 11 個數字是 10 的「0」。""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【按位數分區段】
    1 位數：1–9，共 9 個數，佔 9 × 1 = 9 個數字
    2 位數：10–99，共 90 個數，佔 90 × 2 = 180 個數字
    3 位數：100–999，共 900 個數，佔 900 × 3 = 2700 個數字
    k 位數：共 9 × 10^(k-1) 個數，佔 k × 9 × 10^(k-1) 個數字

【三步驟】
    1. 一個區段一個區段扣掉，找出第 n 個數字落在「幾位數」的區段
    2. 在這個區段裡，它屬於第 (n-1) // digits 個數
       -> num = start + (n-1) // digits
    3. 是 num 的第 (n-1) % digits 位

【範例 n = 11】
    扣掉 1 位數的 9 個 -> n = 2，落在 2 位數區段
    num = 10 + (2-1) // 2 = 10
    第 (2-1) % 2 = 1 位 -> "10"[1] = '0' ✔

【用 n - 1 是為了轉成從 0 開始的索引】"""),
   ("t", ["位數", "範圍", "個數", "佔用的數字數", "累計"],
    [["1", "1–9", "9", "9", "9"],
     ["2", "10–99", "90", "180", "189"],
     ["3", "100–999", "900", "2700", "2889"],
     ["4", "1000–9999", "9000", "36000", "38889"]]),
 ],
 "approaches": [
   ap("解法", "區段定位", [
     ("c", S["p400"]),
   ], "O(log n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>n ≤ 9</strong> → 答案就是 n。",
   "<strong>剛好是區段的最後一個</strong>（n = 9、189、2889）→ 條件用 <code>&gt;</code> 而不是 <code>&gt;=</code>。",
   "<strong>n = 2³¹ − 1</strong> → digits × count 在其他語言會溢位。",
 ],
 "follow": [
   ("h", "同一類題"),
   ("c", "「劍指 Offer 44：數字序列中某一位的數字」是同一題。這種「按長度分組、逐組扣除」的定位法，也用在第 440 題（字典序第 K 小）、第 60 題（第 k 個排列）。"),
 ],
 "related": [
   "<strong>第 60 題 排列序列</strong>",
   "<strong>第 440 題 字典序的第 K 小數字</strong>",
   "<strong>第 233 題 數字 1 的個數</strong>",
 ],
 "check": [
   "k 位數的區段總共佔幾個數字？",
   "找到區段後，怎麼算出是哪一個數、哪一位？",
   "為什麼要用 n − 1？",
 ],
})
