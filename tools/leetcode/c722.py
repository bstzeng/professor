# -*- coding: utf-8 -*-
"""第 722、724、725、726、728、729、730、731 題。"""
import random, re, bisect
from collections import Counter
from functools import lru_cache
from itertools import combinations
from authoring import ap
from lcauto import em
from runner import Src, to_list, from_list

S = Src()
random.seed(722)


# ==================== 722. Remove Comments ====================
S["p722"] = '''class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res, buf, in_block = [], [], False
        for line in source:
            i = 0
            while i < len(line):
                if in_block:
                    if line.startswith("*/", i):
                        in_block = False        # 區塊註解結束
                        i += 2
                    else:
                        i += 1
                elif line.startswith("/*", i):
                    in_block = True             # ★ 區塊註解開始：之後的內容（可能跨行）都略過
                    i += 2
                elif line.startswith("//", i):
                    break                       # 行註解：這一行剩下的都略過
                else:
                    buf.append(line[i])
                    i += 1
            if not in_block and buf:            # 區塊註解中間的換行不算：buf 要延續到下一行
                res.append("".join(buf))
                buf = []
        return res'''

_p722 = S.load("p722")
src = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
assert _p722.removeComments(src) == ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"]
assert _p722.removeComments(["a/*comment", "line", "more_comment*/b"]) == ["ab"]
assert _p722.removeComments(["a//*b*/c", "d"]) == ["a", "d"]
assert _p722.removeComments(["a/*/b//*c", "blank", "d/*/e*//f"]) == ["ae*"]
print("P722 OK")

em({
 "num": 722, "title": "刪除註解",
 "desc": "逐字元的小型狀態機：是否在區塊註解中；跨行的區塊註解會把前後兩行接在一起，所以緩衝區要延續到下一行。",
 "zh": [
   "給你一份 C++ 程式碼（以行為單位的字串陣列），刪除其中的註解後回傳。",
   ("ul", ["<code>//</code> 是行註解：它與同一行右邊的所有字元都要刪除。",
           "<code>/* ... */</code> 是區塊註解，可以跨越多行；<code>/*/</code> 不算結束（<code>*/</code> 必須在 <code>/*</code> 之後才算）。",
           "誰先出現誰優先：在區塊註解內的 <code>//</code> 沒有作用，在行註解後面的 <code>/*</code> 也沒有作用。",
           "刪除後若某行變成空字串，就不要輸出這一行。"]),
 ],
 "idea": [
   ("c", """【狀態機】
    狀態：是否在區塊註解中（in_block）。
    逐字元掃描：
        在區塊中：看到 */ -> 離開；否則略過
        不在區塊：
            /* -> 進入區塊（i += 2，避免 /*/ 被誤判為結束）
            // -> 這一行剩下的全部略過
            其他 -> 加進緩衝區

【跨行的區塊註解】
    "a/*comment", "line", "more_comment*/b" -> "ab"
    區塊註解吃掉了換行，所以 a 和 b 在同一行。
    -> 只有「行結束時不在區塊中」才把緩衝區輸出成一行，
       否則緩衝區延續到下一行。"""),
 ],
 "approaches": [
   ap("解法", "逐字元狀態機", [("c", S["p722"]), "驗證方式：題目範例，加上跨行合併（ab）、行註解中的 /*、/*/ 不算結束等邊界案例。"], "O(總字元數)", "O(總字元數)", optimal=True),
 ],
 "edges": ["<strong>/*/</strong> → 不是結束。", "<strong>// 在區塊註解內</strong> → 無效。", "<strong>跨行區塊註解</strong> → 前後兩段接成同一行。", "<strong>刪除後是空行</strong> → 不輸出。"],
 "follow": [("h", "詞法分析"), ("c", "編譯器的第一步「詞法分析」就是這樣的狀態機。真實的 C++ 還要處理字串常數中的 // 或 /*（它們不是註解），題目保證沒有引號簡化了問題。")],
 "related": ["<strong>第 591 題 標籤驗證器</strong>", "<strong>第 736 題 Lisp 語法解析</strong>"],
 "check": ["為什麼看到 /* 時要 i += 2？", "跨行區塊註解為什麼不能在行尾就輸出緩衝區？"],
})


# ==================== 724. Find Pivot Index ====================
S["p724"] = '''class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total, left = sum(nums), 0
        for i, x in enumerate(nums):
            if left == total - left - x:        # ★ 左邊的和 == 右邊的和（總和 - 左邊 - 自己）
                return i
            left += x
        return -1'''

_p724 = S.load("p724")
for _ in range(3000):
    a = [random.randint(-3, 3) for _ in range(random.randint(1, 8))]
    want = next((i for i in range(len(a)) if sum(a[:i]) == sum(a[i + 1:])), -1)
    assert _p724.pivotIndex(a) == want
print("P724 OK")

em({
 "num": 724, "title": "尋找陣列的中心索引",
 "desc": "右邊的和 = 總和 − 左邊的和 − 自己，所以一趟掃描維護左邊的和即可。",
 "zh": [
   "<strong>中心索引</strong>是一個位置 i，使得它左邊所有元素的和等於右邊所有元素的和（不含自己；邊界外的和為 0）。",
   "回傳<strong>最左邊</strong>的中心索引；不存在則回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【前綴和】
    left = nums[0..i-1] 的和
    right = total - left - nums[i]
    left == right 就找到了。

    一趟掃描，邊走邊累加 left。
    由左往右找，第一個符合的就是最左邊的。"""),
 ],
 "approaches": [
   ap("解法", "總和 + 左側前綴和", [("c", S["p724"])], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>索引 0</strong> → 左邊和為 0。", "<strong>負數</strong> → 不能提前結束，要掃完。"],
 "follow": [("h", "相同的題目"), ("c", "第 1991 題（找到陣列的中間位置）與本題完全相同。")],
 "related": ["<strong>第 1991 題 找到陣列的中間位置</strong>", "<strong>第 560 題 和為 K 的子陣列</strong>"],
 "check": ["右邊的和怎麼用總和與左邊的和表示？"],
})


# ==================== 725. Split Linked List in Parts ====================
S["p725"] = '''class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n, nd = 0, head
        while nd:
            n += 1
            nd = nd.next
        base, extra = divmod(n, k)              # ★ 每段 base 個，前 extra 段多 1 個
        res, nd = [], head
        for i in range(k):
            res.append(nd)
            size = base + (1 if i < extra else 0)
            for _ in range(size - 1):
                nd = nd.next
            if nd:
                nd.next, nd = None, nd.next     # 切斷，移到下一段的開頭
        return res'''

_p725 = S.load("p725")
for _ in range(1500):
    n, k = random.randint(0, 12), random.randint(1, 6)
    vals = list(range(n)); parts = [from_list(p) for p in _p725.splitListToParts(to_list(vals), k)]
    b, e = divmod(n, k); want = []; i = 0
    for t in range(k):
        s = b + (t < e); want.append(vals[i:i + s]); i += s
    assert parts == want
print("P725 OK")

em({
 "num": 725, "title": "分隔鏈結串列",
 "desc": "先數長度 n，每段 n // k 個、前 n % k 段多一個；依序走並在每段結尾切斷。",
 "zh": [
   "給你鏈結串列的頭節點和整數 <code>k</code>，把串列分成 <code>k</code> 段連續的部分。",
   "各段長度要<strong>盡可能相等</strong>：任兩段長度差不超過 1，而且前面的段不能比後面的短。段數多於節點數時，多出來的段是 <code>null</code>。",
 ],
 "idea": [
   ("c", """【長度分配】
    n 個節點分成 k 段：
        base = n // k，extra = n % k
        前 extra 段各 base + 1 個，其餘 base 個。

【切斷】
    每段走 size - 1 步到結尾，把 next 設成 None，
    下一段從原本的 next 開始。
    size = 0（節點不夠）時這段就是 None。"""),
 ],
 "approaches": [
   ap("解法", "計算長度後切段", [("c", S["p725"])], "O(n + k)", "O(k)", "", "輸出陣列", optimal=True),
 ],
 "edges": ["<strong>k > n</strong> → 後面的段是 None。", "<strong>空串列</strong> → k 個 None。"],
 "follow": [("h", "均分的通用公式"), ("c", "「n 個東西分成 k 份，盡量平均」：divmod(n, k) 給出每份的基本量與多出來的份數。分頁、負載平衡都用它。")],
 "related": ["<strong>第 61 題 旋轉鏈結串列</strong>", "<strong>第 328 題 奇偶鏈結串列</strong>"],
 "check": ["哪幾段會多一個節點？", "切斷時為什麼要先記住 next？"],
})


# ==================== 726. Number of Atoms ====================
S["p726"] = '''class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        tokens = re.findall(r"([A-Z][a-z]*)(\\d*)|(\\()|(\\))(\\d*)", formula)
        for name, cnt, lp, rp, mult in tokens:
            if name:
                stack[-1][name] += int(cnt or 1)        # 原子：加到目前這一層
            elif lp:
                stack.append(Counter())                 # 左括號：開新的一層
            else:
                top = stack.pop()
                k = int(mult or 1)
                for a, c in top.items():
                    stack[-1][a] += c * k               # ★ 右括號：整層乘上倍數，併回上一層
        cnt = stack[0]
        return "".join(a + (str(cnt[a]) if cnt[a] > 1 else "") for a in sorted(cnt))'''

_p726 = S.load("p726")
for f, want in [("H2O", "H2O"), ("Mg(OH)2", "H2MgO2"), ("K4(ON(SO3)2)2", "K4N2O14S4"), ("Be32", "Be32")]:
    assert _p726.countOfAtoms(f) == want, (f, _p726.countOfAtoms(f))
def _rand_formula(d=0):
    parts = []
    for _ in range(random.randint(1, 3)):
        if d < 2 and random.random() < 0.3:
            parts.append("(" + _rand_formula(d + 1) + ")" + random.choice(["", "2", "3"]))
        else:
            parts.append(random.choice(["H", "He", "O", "Mg"]) + random.choice(["", "2", "3"]))
    return "".join(parts)
def _ref726(f):
    def parse(i):
        c = Counter()
        while i < len(f) and f[i] != ")":
            if f[i] == "(":
                sub, i = parse(i + 1); i += 1; j = i
                while j < len(f) and f[j].isdigit(): j += 1
                m = int(f[i:j] or 1); i = j
                for a, v in sub.items(): c[a] += v * m
            else:
                j = i + 1
                while j < len(f) and f[j].islower(): j += 1
                a = f[i:j]; i = j
                while j < len(f) and f[j].isdigit(): j += 1
                c[a] += int(f[i:j] or 1); i = j
        return c, i
    c, _ = parse(0)
    return "".join(a + (str(c[a]) if c[a] > 1 else "") for a in sorted(c))
for _ in range(1500):
    f = _rand_formula(); assert _p726.countOfAtoms(f) == _ref726(f), f
print("P726 OK")

em({
 "num": 726, "title": "原子的數量",
 "desc": "堆疊裡每一層是一個計數器：左括號開新層、右括號把整層乘上倍數併回上一層；最後依字母序輸出。",
 "zh": [
   "給你一個化學式字串 <code>formula</code>，回傳每種原子的數量。",
   "原子名稱以大寫字母開頭，後面接零或多個小寫字母；數量（大於 1 時才寫）接在後面。化學式可以用括號組合並乘上倍數，例如 <code>\"Mg(OH)2\"</code>。",
   "輸出依原子名稱的<strong>字典序</strong>排列，數量為 1 時不寫數字，例如 <code>\"H2MgO2\"</code>。",
 ],
 "idea": [
   ("c", """【括號巢狀 -> 堆疊】
    堆疊的每一層是一個計數器，代表「目前這層括號裡」的原子數量。
        原子 + 數字 -> 加到頂層
        (            -> 推入新的空計數器
        ) + 數字 k   -> 彈出頂層，全部乘 k 後加到下一層

【斷詞】
    正規表示式一次切出三種 token：
        ([A-Z][a-z]*)(\\d*)   原子與數量
        (\\()                 左括號
        (\\))(\\d*)           右括號與倍數

【遞迴寫法】
    parse() 遇到 '(' 就遞迴解析到對應的 ')'，回傳子計數器。"""),
 ],
 "approaches": [
   ap("解法", "堆疊 + 計數器", [("c", S["p726"]), "驗證方式：題目範例，加上隨機產生的巢狀化學式，和遞迴下降解析器比對 1500 組。"], "O(n²)", "O(n)", "最壞每層括號都要把內容乘一次", "", optimal=True),
 ],
 "edges": ["<strong>數量 1 不寫</strong>（輸入與輸出都是）。", "<strong>多位數</strong>（如 Be32）。", "<strong>多層巢狀括號</strong>。"],
 "follow": [("h", "由右往左掃"), ("c", "從右往左掃描，維護一個「目前的乘數」堆疊：遇到 ) 把乘數乘上它後面的數字並推入，遇到 ( 彈出。每個原子直接乘上目前乘數加到總表，避免重複乘整層，O(n)。")],
 "related": ["<strong>第 394 題 字串解碼</strong>", "<strong>第 224 題 基本計算機</strong>", "<strong>第 736 題 Lisp 語法解析</strong>"],
 "check": ["遇到右括號時要做什麼？", "為什麼堆疊的每一層要是一個計數器？"],
})


# ==================== 728. Self Dividing Numbers ====================
S["p728"] = '''class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def ok(x):
            for d in str(x):
                if d == "0" or x % int(d):      # 含 0 不行（不能除以 0）；任一位數不能整除也不行
                    return False
            return True
        return [x for x in range(left, right + 1) if ok(x)]'''

_p728 = S.load("p728")
assert _p728.selfDividingNumbers(1, 22) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
assert _p728.selfDividingNumbers(47, 85) == [48, 55, 66, 77]
print("P728 OK")

em({
 "num": 728, "title": "自除數",
 "desc": "逐一檢查範圍內每個數的每一位：不能有 0，而且每一位都要整除這個數。",
 "zh": [
   "<strong>自除數</strong>是能被它自己每一位數字整除的數，例如 128（128 % 1 == 0、128 % 2 == 0、128 % 8 == 0）。自除數不允許包含數字 0。",
   "給你 <code>left</code> 和 <code>right</code>，回傳範圍內所有的自除數。",
 ],
 "idea": [
   ("c", """【直接檢查】
    範圍最多 10⁴，每個數最多 5 位，直接檢查即可。
    取每一位：轉字串，或反覆 % 10、// 10。
    遇到 0 或不能整除就淘汰。"""),
 ],
 "approaches": [
   ap("解法", "逐一檢查", [("c", S["p728"])], "O((right − left) · log right)", "O(1)", "", "不計輸出", optimal=True),
 ],
 "edges": ["<strong>含 0 的數</strong>（如 10）→ 不是。", "<strong>個位數</strong> → 都是。"],
 "follow": [("h", "檢查順序"), ("c", "要先判斷數字是不是 0，再做取餘數，否則會除以零。用 or 的短路求值剛好保證這個順序。")],
 "related": ["<strong>第 507 題 完全數</strong>", "<strong>第 2520 題 統計能整除數字的位數</strong>"],
 "check": ["為什麼要先檢查是不是 0？"],
})


# ==================== 729. My Calendar I ====================
S["p729"] = '''class MyCalendar:
    def __init__(self):
        self.starts, self.ends = [], []         # 已預訂的區間，依開始時間排序

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_right(self.starts, start)
        # ★ 只需檢查相鄰的兩個區間：前一個的結束 <= start，後一個的開始 >= end
        if i > 0 and self.ends[i - 1] > start:
            return False
        if i < len(self.starts) and self.starts[i] < end:
            return False
        self.starts.insert(i, start)
        self.ends.insert(i, end)
        return True'''

_C1 = S.loadns("p729")["MyCalendar"]
for _ in range(500):
    o = _C1(); booked = []
    for _ in range(15):
        s = random.randint(0, 30); e = random.randint(s + 1, 35)
        ok = all(e <= a or s >= b for a, b in booked)
        if ok: booked.append((s, e))
        assert o.book(s, e) == ok
print("P729 OK")

em({
 "num": 729, "title": "我的日程安排表 I",
 "desc": "已預訂的區間互不重疊、依開始時間排序：二分找到插入位置，只需和前後兩個相鄰區間比較。",
 "zh": [
   "實作一個行事曆：<code>book(start, end)</code> 嘗試預訂半開區間 <code>[start, end)</code>。若和任何已預訂的事件<strong>重疊</strong>（雙重預訂）就回傳 False 且不預訂；否則預訂並回傳 True。",
 ],
 "idea": [
   ("c", """【暴力】
    和每個已預訂區間檢查重疊：s1 < e2 且 s2 < e1。O(n) 每次。

【有序 + 二分】
    已預訂的區間互不重疊 -> 依開始時間排序後，結束時間也是排序的。
    新區間只可能和「插入位置前一個」或「後一個」重疊：
        前一個的 end > start -> 重疊
        後一個的 start < end -> 重疊
    二分 O(log n)；Python 的 list.insert 是 O(n)，
    若用平衡樹（如 SortedList）則整體 O(log n)。"""),
 ],
 "approaches": [
   ap("解法", "排序區間 + 二分", [("c", S["p729"]), "驗證方式：和逐一檢查所有已預訂區間的暴力法比對 500 組。"], "book：O(n)（插入），查詢 O(log n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>相接的區間</strong>（[10,20) 與 [20,30)）→ 不算重疊。", "<strong>完全包含</strong> → 重疊。"],
 "follow": [("h", "允許兩重、統計最大重疊"), ("c", "第 731 題允許兩重預訂但不能三重；第 732 題回傳目前的最大重疊數——差分 + 有序表，或線段樹。")],
 "related": ["<strong>第 731 題 我的日程安排表 II</strong>", "<strong>第 732 題 我的日程安排表 III</strong>", "<strong>第 715 題 Range 模組</strong>"],
 "check": ["為什麼只需要和相鄰的兩個區間比較？", "兩個半開區間重疊的條件是什麼？"],
})


# ==================== 730. Count Different Palindromic Subsequences ====================
S["p730"] = '''class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]        # dp[i][j]：s[i..j] 中不同的非空迴文子序列個數
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] != s[j]:
                    # 容斥：包含 s[i] 的 + 包含 s[j] 的 - 兩者都不含的（重複算了）
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                else:
                    c = s[i]
                    lo, hi = i + 1, j - 1
                    while lo <= hi and s[lo] != c:
                        lo += 1                 # 內部第一個 c
                    while lo <= hi and s[hi] != c:
                        hi -= 1                 # 內部最後一個 c
                    inner = dp[i + 1][j - 1]
                    if lo > hi:                 # ★ 內部沒有 c：內部每個迴文包上 c..c，再加上 "c"、"cc"
                        dp[i][j] = 2 * inner + 2
                    elif lo == hi:              # 內部恰有一個 c："c" 已經算過，只多 "cc"
                        dp[i][j] = 2 * inner + 1
                    else:                       # 內部有兩個以上 c：c[內部第一與最後 c 之間]c 被重複算了
                        dp[i][j] = 2 * inner - dp[lo + 1][hi - 1]
                dp[i][j] %= MOD
        return dp[0][n - 1]'''

_p730 = S.load("p730")
assert _p730.countPalindromicSubsequences("bccb") == 6
assert _p730.countPalindromicSubsequences("abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba") == 104860361
for _ in range(400):
    s = "".join(random.choice("abcd") for _ in range(random.randint(1, 9)))
    subs = set()
    for r in range(1, len(s) + 1):
        for idx in combinations(range(len(s)), r):
            t = "".join(s[i] for i in idx)
            if t == t[::-1]: subs.add(t)
    assert _p730.countPalindromicSubsequences(s) == len(subs), s
print("P730 OK")

em({
 "num": 730, "title": "統計不同回文子序列",
 "desc": "區間 DP 的難題：兩端相同時，依內部有幾個同樣字元分三種情況扣掉重複；兩端不同時用容斥。",
 "zh": [
   "給你一個只含 <code>'a'</code>、<code>'b'</code>、<code>'c'</code>、<code>'d'</code> 的字串 <code>s</code>，回傳其中<strong>不同的非空迴文子序列</strong>的個數，對 <code>10⁹ + 7</code> 取模。",
   "內容相同的子序列只算一次（即使出現在不同位置）。",
 ],
 "idea": [
   ("c", """【dp[i][j] = s[i..j] 中不同的非空迴文子序列個數】

【s[i] != s[j]】
    迴文不可能同時用到 s[i] 當頭、s[j] 當尾。
    容斥：dp[i+1][j] + dp[i][j-1] - dp[i+1][j-1]。

【s[i] == s[j] = c】
    新的迴文：在內部每個迴文外面包上 c...c（兩倍），
    再加上 "c" 和 "cc" 兩個 —— 但可能已經被算過，看內部有幾個 c：
        內部沒有 c：
            "c"、"cc" 都是新的 -> 2·inner + 2
        內部恰有一個 c：
            "c" 已經在 inner 裡 -> 2·inner + 1
        內部有兩個以上（第一個在 lo、最後一個在 hi）：
            "c"、"cc" 都已算過；
            而且 c[s[lo+1..hi-1] 的迴文]c 在 inner 裡就出現過，
            包上外層 c 後會重複 -> 2·inner - dp[lo+1][hi-1]

    每種情況都在保證「內容相同只算一次」。"""),
 ],
 "approaches": [
   ap("解法", "區間 DP + 分情況去重", [
     ("c", S["p730"]),
     "驗證方式：和枚舉所有子序列放進集合的暴力法比對 400 組；題目的長字串範例答案是 104860361。",
   ], "O(n³)", "O(n²)", "找內部第一個與最後一個 c 需要 O(n)；預處理 next/prev 可降到 O(n²)", "", optimal=True),
 ],
 "edges": ["<strong>單一字元</strong> → 1。", "<strong>\"aaa\"</strong> → 3（a、aa、aaa）。", "<strong>減法後取模</strong> → Python 的 % 自動回到非負值。"],
 "follow": [("h", "依字元分類的寫法"), ("c", "另一種 DP：dp[c][i][j] = s[i..j] 中「以字元 c 開頭結尾」的不同迴文數。字元集只有 4 個，轉移更直觀：找 i 之後第一個 c 與 j 之前最後一個 c，再對 4 個字元加總。")],
 "related": ["<strong>第 516 題 最長迴文子序列</strong>", "<strong>第 647 題 迴文子字串</strong>", "<strong>第 940 題 不同的子序列 II</strong>"],
 "check": ["兩端不同時為什麼要減掉 dp[i+1][j−1]？", "兩端相同時，三種情況分別重複算了什麼？"],
})


# ==================== 731. My Calendar II ====================
S["p731"] = '''class MyCalendarTwo:
    def __init__(self):
        self.booked = []                # 所有已預訂的區間
        self.overlaps = []              # 已經被預訂兩次的區間

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if start < e and s < end:
                return False            # ★ 和「已經兩重」的部分重疊 -> 會變成三重
        for s, e in self.booked:
            if start < e and s < end:
                self.overlaps.append((max(s, start), min(e, end)))   # 新的兩重區段
        self.booked.append((start, end))
        return True'''

_C2 = S.loadns("p731")["MyCalendarTwo"]
for _ in range(500):
    o = _C2(); cnt = [0] * 40
    for _ in range(12):
        s = random.randint(0, 30); e = random.randint(s + 1, 35)
        ok = all(cnt[x] < 2 for x in range(s, e))
        if ok:
            for x in range(s, e): cnt[x] += 1
        assert o.book(s, e) == ok
print("P731 OK")

em({
 "num": 731, "title": "我的日程安排表 II",
 "desc": "另外維護「已經兩重」的區段：新事件若碰到任何兩重區段就會變三重；否則把它和既有事件的交集加入兩重列表。",
 "zh": ["實作一個行事曆：<code>book(start, end)</code> 預訂 <code>[start, end)</code>。允許<strong>兩重預訂</strong>（兩個事件重疊），但若會造成<strong>三重預訂</strong>（三個事件有共同時間）就回傳 False 且不預訂。"],
 "idea": [
   ("c", """【兩個列表】
    booked：所有事件
    overlaps：所有「兩個事件重疊」的區段

【新事件 [start, end)】
    1. 若和 overlaps 中任何區段重疊 -> 會三重，拒絕。
    2. 否則接受：它和每個 booked 事件的交集，都成為新的兩重區段。

【差分做法】
    把 start +1、end -1 存進有序表，
    依序累加檢查最大值是否超過 2；超過就撤銷。
    這個做法可以直接推廣到「最多 k 重」。"""),
 ],
 "approaches": [
   ap("解法", "兩重區段列表", [("c", S["p731"]), "驗證方式：在整數座標上和計數陣列模擬比對 500 組。"], "book：O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>相接不算重疊</strong>。", "<strong>被拒絕的事件</strong> → 不能加入任何列表。"],
 "follow": [("h", "一般化"), ("c", "最多 k 重：差分（掃描線）＋有序表，每次 O(n)；或線段樹支援區間加 1 與區間最大值，O(log C)。第 732 題就是回傳目前的最大重疊數。")],
 "related": ["<strong>第 729 題 我的日程安排表 I</strong>", "<strong>第 732 題 我的日程安排表 III</strong>"],
 "check": ["overlaps 存的是什麼？", "為什麼只要檢查 overlaps 就能判斷三重？"],
})
