# -*- coding: utf-8 -*-
"""第 636、637、638、639、640、641、643、645 題。"""
import random, re
from collections import deque, Counter
from functools import lru_cache
from fractions import Fraction
from itertools import product
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree

S = Src()
random.seed(636)


# ==================== 636. Exclusive Time of Functions ====================
S["p636"] = '''class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []                          # 呼叫堆疊：正在執行（或被暫停）的函式 id
        prev = 0                            # 上一個事件的「時間點」（時間片段的開頭）
        for log in logs:
            fid, kind, t = log.split(":")
            fid, t = int(fid), int(t)
            if kind == "start":
                if stack:
                    res[stack[-1]] += t - prev      # 目前執行中的函式跑到 t 之前
                stack.append(fid)
                prev = t
            else:
                res[stack.pop()] += t - prev + 1    # ★ end 的時間戳是「該單位的結尾」，所以 +1
                prev = t + 1
        return res'''

_p636 = S.load("p636")
assert _p636.exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]) == [3, 4]
assert _p636.exclusiveTime(1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]) == [8]
assert _p636.exclusiveTime(2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]) == [7, 1]
for _ in range(1000):
    n = random.randint(1, 3); T = 0; logs = []; st = []; owner = []
    for _ in range(random.randint(1, 8)):
        if st and random.random() < 0.5:
            f = st.pop(); logs.append("%d:end:%d" % (f, T)); owner.append(f); T += 1
        else:
            f = random.randrange(n); logs.append("%d:start:%d" % (f, T)); st.append(f)
            if random.random() < 0.6:
                owner.append(f); T += 1
            else:
                pass
    while st:
        f = st.pop(); logs.append("%d:end:%d" % (f, T)); owner.append(f); T += 1
    # 用逐時間單位模擬的參考答案
    ref = [0] * n; stack = []; prev_t = 0
    events = [(int(l.split(":")[2]), l.split(":")[1], int(l.split(":")[0])) for l in logs]
    cur = 0
    for t, kind, f in events:
        while cur < t:
            if stack: ref[stack[-1]] += 1
            cur += 1
        if kind == "start":
            stack.append(f)
        else:
            ref[stack[-1]] += 1; stack.pop(); cur = t + 1
    assert _p636.exclusiveTime(n, logs) == ref, logs
print("P636 OK")

em({
 "num": 636, "title": "函式的獨佔時間",
 "desc": "用堆疊模擬呼叫堆疊，記錄上一個事件的時間點；注意 start 在單位開頭、end 在單位結尾。",
 "zh": [
   "單執行緒 CPU 上執行了 <code>n</code> 個函式（id 為 0～n−1），可能互相呼叫或遞迴。給你依時間排序的日誌，每筆格式為 <code>\"id:start:時間\"</code> 或 <code>\"id:end:時間\"</code>。",
   "<code>\"0:start:3\"</code> 表示函式 0 在第 3 個時間單位的<strong>開頭</strong>開始；<code>\"1:end:2\"</code> 表示函式 1 在第 2 個時間單位的<strong>結尾</strong>結束。",
   "函式的<strong>獨佔時間</strong>是它自己在執行（不含它呼叫的其他函式）的時間總和。回傳每個函式的獨佔時間。",
 ],
 "idea": [
   ("c", """【單執行緒 = 任何時刻只有堆疊頂端在執行】
    用堆疊模擬呼叫堆疊。

【把時間切成片段】
    prev = 目前這個片段的開頭時間點。
    遇到 start t：
        頂端函式從 prev 跑到 t 的開頭 -> 加 t - prev
        新函式入堆疊，prev = t
    遇到 end t：
        頂端函式從 prev 跑到 t 的結尾 -> 加 t - prev + 1
        出堆疊，prev = t + 1（下一個單位的開頭）

【關鍵：start 和 end 的時間語意不同】
    start 在單位開頭、end 在單位結尾，所以 end 要 +1。"""),
 ],
 "approaches": [
   ap("解法", "堆疊模擬", [("c", S["p636"]), "驗證方式：題目範例，加上隨機產生的合法日誌，和「逐時間單位模擬」的參考答案比對。"], "O(m)", "O(m)", "m 為日誌筆數", "", optimal=True),
 ],
 "edges": ["<strong>遞迴呼叫自己</strong> → 堆疊裡會有重複 id，照常處理。", "<strong>同一時間單位內 start 又 end</strong> → 時間 1。"],
 "follow": [("h", "效能分析器"), ("c", "這就是 profiler 計算「self time」（獨佔時間）和「total time」（含子呼叫）的方式。火焰圖（flame graph）中每個框的寬度就是 total time。")],
 "related": ["<strong>第 20 題 有效的括號</strong>", "<strong>第 71 題 簡化路徑</strong>"],
 "check": ["為什麼 end 要加 1？", "prev 在 start 與 end 之後分別設成什麼？"],
})


# ==================== 637. Average of Levels in Binary Tree ====================
S["p637"] = '''class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res, level = [], [root]
        while level:
            res.append(sum(nd.val for nd in level) / len(level))     # 這一層的平均
            level = [c for nd in level for c in (nd.left, nd.right) if c]
        return res'''

_p637 = S.load("p637")
assert _p637.averageOfLevels(lv([3, 9, 20, None, None, 15, 7])) == [3.0, 14.5, 11.0]
print("P637 OK")

em({
 "num": 637, "title": "二元樹的層平均值",
 "desc": "逐層走訪，每層求和除以節點數。",
 "zh": ["給你二元樹的根節點，回傳每一層節點值的<strong>平均值</strong>組成的陣列（與標準答案相差 10⁻⁵ 以內都算正確）。"],
 "idea": [
   ("c", """【層序走訪】
    每一層：sum / len，再換到下一層。

【溢位？】
    其他語言要注意節點值累加可能超過 32 位元整數，
    Python 的整數沒有上限。"""),
 ],
 "approaches": [
   ap("解法", "逐層 BFS", [("c", S["p637"])], "O(n)", "O(w)", optimal=True),
 ],
 "edges": ["<strong>大數值</strong> → 其他語言要用 64 位元累加。"],
 "follow": [("h", "BFS 骨架"), ("c", "和第 102、515、513 題同一個「整層換整層」的骨架。")],
 "related": ["<strong>第 102 題 二元樹的層序走訪</strong>", "<strong>第 515 題 在每個樹行中找最大值</strong>"],
 "check": ["在 C++ 或 Java 中為什麼要注意加總的型別？"],
})


# ==================== 638. Shopping Offers ====================
S["p638"] = '''class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        # 先把「比單買還貴」的大禮包濾掉
        offers = [s for s in special if sum(s[i] * price[i] for i in range(n)) > s[n]]

        @cache
        def dfs(need):
            best = sum(need[i] * price[i] for i in range(n))     # 全部單買
            for s in offers:
                rest = tuple(need[i] - s[i] for i in range(n))
                if min(rest) >= 0:                               # ★ 大禮包不能買超過需要的量
                    best = min(best, s[n] + dfs(rest))
            return best
        return dfs(tuple(needs))'''

_p638 = S.load("p638", extra={"cache": lru_cache(None)})
assert _p638.shoppingOffers([2, 5], [[3, 0, 5], [1, 2, 10]], [3, 2]) == 14
assert _p638.shoppingOffers([2, 3, 4], [[1, 1, 0, 4], [2, 2, 1, 9]], [1, 2, 1]) == 11
def _bf638(price, special, needs):
    n = len(price); best = [10 ** 9]
    def go(need, cost):
        best[0] = min(best[0], cost + sum(a * b for a, b in zip(need, price)))
        for s in special:
            r = [need[i] - s[i] for i in range(n)]
            if min(r) >= 0 and sum(s[:n]) > 0: go(r, cost + s[n])
    go(needs, 0); return best[0]
for _ in range(400):
    n = random.randint(1, 3); price = [random.randint(1, 6) for _ in range(n)]
    special = [[random.randint(0, 2) for _ in range(n)] + [random.randint(1, 15)] for _ in range(random.randint(0, 3))]
    needs = [random.randint(0, 4) for _ in range(n)]
    _p638 = S.load("p638", extra={"cache": lru_cache(None)})
    assert _p638.shoppingOffers(price, special, needs) == _bf638(price, special, needs)
print("P638 OK")

em({
 "num": 638, "title": "大禮包",
 "desc": "狀態是「還需要的數量」：每一步試所有買得起的大禮包，剩下的單買；物品種類少，記憶化很有效。",
 "zh": [
   "商店有 <code>n</code> 種物品，<code>price[i]</code> 是第 i 種的單價。另有一些<strong>大禮包</strong> <code>special[j]</code>：前 n 個數是各物品的數量，最後一個數是禮包價格。",
   "給你需要的數量 <code>needs</code>，回傳<strong>恰好</strong>買到需要數量的最低花費。大禮包可以買任意多次，但<strong>不能買超過需要的數量</strong>（即使更便宜也不行）。",
 ],
 "idea": [
   ("c", """【狀態：還需要多少】
    dfs(need) = 買齊 need 的最低花費。
    選擇：
        全部單買：Σ need[i] · price[i]
        或先買一個大禮包 s（前提：s 的每一項都 <= need），
            再遞迴 dfs(need - s)

【記憶化】
    n <= 6、每項需求 <= 10 -> 狀態最多 11⁶ ≈ 177 萬，實際上遠少於此。
    need 用 tuple 當鍵。

【小最佳化】
    比單買還貴的大禮包永遠不會用，先濾掉。"""),
 ],
 "approaches": [
   ap("解法", "記憶化搜尋", [("c", S["p638"]), "驗證方式：和不記憶化的完整窮舉比對 400 組。"], "O(S · m · n)", "O(S)", "S 為出現的狀態數，m 為禮包數", "", optimal=True),
 ],
 "edges": ["<strong>不能超買</strong> → 禮包某一項超過需要就不能用。", "<strong>沒有禮包</strong> → 全部單買。", "<strong>禮包比單買貴</strong> → 濾掉。"],
 "follow": [("h", "多維完全背包"), ("c", "這其實是一個多維的完全背包：每種「物品」（單買某樣東西、或某個禮包）可以用無限次，要恰好裝滿多維容量 needs。")],
 "related": ["<strong>第 322 題 零錢兌換</strong>", "<strong>第 474 題 一和零</strong>"],
 "check": ["DP 的狀態是什麼？", "為什麼要過濾掉比單買還貴的禮包？"],
})


# ==================== 639. Decode Ways II ====================
S["p639"] = '''class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10 ** 9 + 7

        def one(c):                         # 單一字元能解碼成幾種字母
            if c == "*":
                return 9                    # 1～9
            return 0 if c == "0" else 1

        def two(a, b):                      # 兩個字元合起來（10～26）能解碼成幾種
            if a == "*" and b == "*":
                return 15                   # 11～19（9 種）+ 21～26（6 種）
            if a == "*":
                return 2 if b <= "6" else 1 # 1b 和 2b，或只有 1b
            if b == "*":
                return 9 if a == "1" else 6 if a == "2" else 0
            return 1 if 10 <= int(a + b) <= 26 else 0

        prev2, prev1 = 1, one(s[0])         # dp[i-2], dp[i-1]
        for i in range(1, len(s)):
            # ★ 和第 91 題相同的遞迴，只是每項乘上「有幾種解法」
            cur = (prev1 * one(s[i]) + prev2 * two(s[i - 1], s[i])) % MOD
            prev2, prev1 = prev1, cur
        return prev1'''

_p639 = S.load("p639")
assert _p639.numDecodings("*") == 9 and _p639.numDecodings("1*") == 18 and _p639.numDecodings("2*") == 15
def _dec91(s):
    a, b = 1, (0 if s[0] == "0" else 1)
    for i in range(1, len(s)):
        c = (b if s[i] != "0" else 0) + (a if 10 <= int(s[i - 1:i + 1]) <= 26 else 0)
        a, b = b, c
    return b
for _ in range(400):
    s = "".join(random.choice("012*67*") for _ in range(random.randint(1, 4)))
    stars = [i for i, c in enumerate(s) if c == "*"]
    tot = 0
    for fill in product("123456789", repeat=len(stars)):
        t = list(s)
        for i, d in zip(stars, fill): t[i] = d
        tot += _dec91("".join(t))
    assert _p639.numDecodings(s) == tot % (10 ** 9 + 7), s
print("P639 OK")

em({
 "num": 639, "title": "解碼方法 II",
 "desc": "第 91 題的 DP 加上萬用字元：每個轉移乘上「單字元／雙字元各有幾種合法解碼」，分情況數清楚即可。",
 "zh": [
   "訊息用 <code>'A' → \"1\"</code>、…、<code>'Z' → \"26\"</code> 編碼。現在編碼字串中還可能出現 <code>'*'</code>，代表 <code>'1'</code>～<code>'9'</code> 中的任一個數字（不含 <code>'0'</code>）。",
   "給你字串 <code>s</code>，回傳所有可能的解碼方式總數，對 <code>10⁹ + 7</code> 取模。",
 ],
 "idea": [
   ("c", """【第 91 題的 DP】
    dp[i] = dp[i-1]·(s[i] 單獨解碼的方法數)
          + dp[i-2]·(s[i-1..i] 合起來解碼的方法數)

【單一字元 one(c)】
    '*' -> 9；'0' -> 0；其他 -> 1

【兩個字元 two(a, b)】（合起來要在 10～26）
    "**" -> 11～19、21～26，共 15
    "*b" -> b <= 6：1b、2b 兩種；b >= 7：只有 1b
    "a*" -> a = 1：11～19 九種；a = 2：21～26 六種；其他 0
    "ab" -> 10 <= ab <= 26 則 1，否則 0

    注意 '*' 不能代表 0，所以 "*0"：10、20 兩種（b = '0' <= '6'）。"""),
 ],
 "approaches": [
   ap("解法", "DP + 分情況計數", [
     ("c", S["p639"]),
     "驗證方式：把每個 * 展開成 1～9 的所有組合，用第 91 題的解法逐一計算加總，比對 400 組。",
   ], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>\"*0\"</strong> → 2（10、20）。", "<strong>\"0\" 開頭</strong> → 0。", "<strong>\"**\"</strong> → 9×9 + 15 = 96。"],
 "follow": [("h", "萬用字元的 DP"), ("c", "「把萬用字元的每一種可能都數進轉移係數」：第 10 題、第 44 題（萬用字元匹配）是判斷型；本題是計數型，轉移時乘上可能數。")],
 "related": ["<strong>第 91 題 解碼方法</strong>", "<strong>第 44 題 萬用字元匹配</strong>"],
 "check": ["\"*b\" 在 b ≤ 6 和 b ≥ 7 時各有幾種？", "\"**\" 合起來為什麼是 15 種？"],
})


# ==================== 640. Solve the Equation ====================
S["p640"] = '''class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(side):                    # 回傳 (x 的係數, 常數)
            a = b = 0
            for sign, num, x in re.findall(r"([+-]?)(\\d*)(x?)", side):
                if not num and not x:
                    continue                # findall 會匹配到空字串，略過
                v = int(num) if num else 1  # "x" 的係數是 1，"0x" 的係數是 0
                if sign == "-":
                    v = -v
                if x:
                    a += v
                else:
                    b += v
            return a, b

        l, r = equation.split("=")
        a1, b1 = parse(l)
        a2, b2 = parse(r)
        a, b = a1 - a2, b2 - b1             # ★ 移項：(a1 - a2)x = b2 - b1
        if a == 0:
            return "Infinite solutions" if b == 0 else "No solution"
        return "x=%d" % (b // a)'''

_p640 = S.load("p640")
cases = [("x+5-3+x=6+x-2", "x=2"), ("x=x", "Infinite solutions"), ("2x=x", "x=0"), ("x=x+2", "No solution"),
         ("-x=-1", "x=1"), ("0x=0", "Infinite solutions"), ("2x+3x-6x=x+2", "x=-1")]
for e, want in cases:
    assert _p640.solveEquation(e) == want, e
print("P640 OK")

em({
 "num": 640, "title": "求解方程",
 "desc": "把等號兩邊各解析成 ax + b，移項後判斷無解、無限多解或唯一解。",
 "zh": [
   "解一個只含 <code>'+'</code>、<code>'-'</code>、變數 <code>x</code> 與係數的一元一次方程，回傳 <code>\"x=#value\"</code>。",
   "若無解回傳 <code>\"No solution\"</code>；若有無限多解回傳 <code>\"Infinite solutions\"</code>。題目保證若有唯一解，它一定是整數。",
 ],
 "idea": [
   ("c", """【每一邊都是 ax + b】
    用正規表示式 ([+-]?)(\\d*)(x?) 切出每一項：
        有 x -> 係數（沒寫數字代表 1）加到 a
        沒有 x -> 常數加到 b

【移項】
    a1·x + b1 = a2·x + b2
    (a1 - a2)·x = b2 - b1

【三種情況】
    a ≠ 0 -> 唯一解 b / a
    a = 0、b = 0 -> 無限多解
    a = 0、b ≠ 0 -> 無解

【陷阱】
    "0x" 的係數是 0，不是 1 —— 有寫數字就用數字。"""),
 ],
 "approaches": [
   ap("解法", "解析兩邊 + 移項", [("c", S["p640"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>\"x\" 沒有係數</strong> → 1。", "<strong>\"0x\"</strong> → 係數 0。", "<strong>開頭是負號</strong> → 正規表示式把它當成第一項的符號。"],
 "follow": [("h", "相關的解析題"), ("c", "第 592 題（分數加減）、第 224 題（基本計算機）、第 770 題（基本計算機 IV：多項式化簡）。")],
 "related": ["<strong>第 592 題 分數加減運算</strong>", "<strong>第 224 題 基本計算機</strong>"],
 "check": ["移項後的兩個係數是什麼？", "\"0x\" 為什麼要特別注意？"],
})


# ==================== 641. Design Circular Deque ====================
S["p641"] = '''class MyCircularDeque:
    def __init__(self, k: int):
        self.buf = [0] * k
        self.head = 0                           # 隊首索引
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1) % len(self.buf)     # ★ 隊首往前退一格（取模繞回尾端）
        self.buf[self.head] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.buf[(self.head + self.size) % len(self.buf)] = value
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % len(self.buf)
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.buf[self.head]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.buf[(self.head + self.size - 1) % len(self.buf)]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.buf)'''

_D = S.loadns("p641")["MyCircularDeque"]
for _ in range(500):
    k = random.randint(1, 5); q = _D(k); ref = deque()
    for _ in range(40):
        op = random.choice(["if", "il", "df", "dl", "gf", "gr", "e", "full"]); v = random.randint(0, 9)
        if op == "if":
            ok = len(ref) < k
            if ok: ref.appendleft(v)
            assert q.insertFront(v) == ok
        elif op == "il":
            ok = len(ref) < k
            if ok: ref.append(v)
            assert q.insertLast(v) == ok
        elif op == "df":
            ok = bool(ref)
            if ok: ref.popleft()
            assert q.deleteFront() == ok
        elif op == "dl":
            ok = bool(ref)
            if ok: ref.pop()
            assert q.deleteLast() == ok
        elif op == "gf": assert q.getFront() == (ref[0] if ref else -1)
        elif op == "gr": assert q.getRear() == (ref[-1] if ref else -1)
        elif op == "e": assert q.isEmpty() == (not ref)
        else: assert q.isFull() == (len(ref) == k)
print("P641 OK")

em({
 "num": 641, "title": "設計循環雙端佇列",
 "desc": "第 622 題的環形緩衝區再加兩個操作：隊首插入時 head 往前退一格、隊尾刪除只要減少個數。",
 "zh": ["設計一個容量為 <code>k</code> 的<strong>循環雙端佇列</strong>，支援 <code>insertFront</code>、<code>insertLast</code>、<code>deleteFront</code>、<code>deleteLast</code>（成功回傳 True）、<code>getFront</code>、<code>getRear</code>（空時回傳 −1）、<code>isEmpty</code>、<code>isFull</code>。"],
 "idea": [
   ("c", """【和第 622 題相同的表示法】
    buf、head（隊首索引）、size。

【新增的兩個操作】
    insertFront：head = (head - 1) % k，放進 buf[head]。
                 Python 的 % 對負數回傳非負值，-1 % k = k-1。
    deleteLast ：size -= 1 即可（隊尾位置由 head + size 決定）。

    所有操作都是 O(1)。"""),
 ],
 "approaches": [
   ap("解法", "環形緩衝區", [("c", S["p641"]), "驗證方式：和 collections.deque 對照，隨機執行 500 組操作序列。"], "每個操作 O(1)", "O(k)", optimal=True),
 ],
 "edges": ["<strong>head 往前退到 −1</strong> → 取模繞到 k − 1。", "<strong>滿或空時的操作</strong> → 回傳 False 或 −1。"],
 "follow": [("h", "其他語言的負數取模"), ("c", "C++、Java 中 −1 % k 是 −1，要寫成 (head − 1 + k) % k。")],
 "related": ["<strong>第 622 題 設計循環佇列</strong>", "<strong>第 1670 題 設計前中後佇列</strong>"],
 "check": ["insertFront 時 head 怎麼更新？", "deleteLast 為什麼只要減少 size？"],
})


# ==================== 643. Maximum Average Subarray I ====================
S["p643"] = '''class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = best = sum(nums[:k])
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]      # ★ 視窗右移：加入新的、減去離開的
            best = max(best, s)
        return best / k'''

_p643 = S.load("p643")
for _ in range(2000):
    a = [random.randint(-9, 9) for _ in range(random.randint(1, 10))]; k = random.randint(1, len(a))
    assert abs(_p643.findMaxAverage(a, k) - max(sum(a[i:i + k]) for i in range(len(a) - k + 1)) / k) < 1e-9
print("P643 OK")

em({
 "num": 643, "title": "子陣列最大平均數 I",
 "desc": "固定長度 k 的滑動視窗維護總和；長度固定時，平均最大等於總和最大。",
 "zh": ["給你整數陣列 <code>nums</code> 和整數 <code>k</code>，找出長度<strong>恰好為 k</strong> 的連續子陣列中最大的平均值。"],
 "idea": [
   ("c", """【長度固定 -> 平均最大 <=> 總和最大】
    只要找總和最大的長度 k 子陣列，最後除以 k。

【滑動視窗】
    先算前 k 個的和，之後每次右移：
        加上新進入的 nums[i]，減掉離開的 nums[i-k]。
    O(n)。"""),
 ],
 "approaches": [
   ap("解法", "固定長度滑動視窗", [("c", S["p643"])], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>k = n</strong> → 整個陣列的平均。", "<strong>全是負數</strong> → best 的初始值要用第一個視窗，不能用 0。"],
 "follow": [("h", "長度至少為 k 的版本"), ("c", "第 644 題（付費）：長度至少 k、求最大平均。對答案二分：檢查「是否存在平均 ≥ x 的子陣列」——把每個數減 x 後，問題變成「長度至少 k 的子陣列和是否 ≥ 0」。")],
 "related": ["<strong>第 644 題 子陣列最大平均數 II</strong>（付費）", "<strong>第 1343 題 大小為 K 且平均值大於等於閾值的子陣列數目</strong>"],
 "check": ["為什麼平均最大等於總和最大？", "best 的初始值為什麼不能是 0？"],
})


# ==================== 645. Set Mismatch ====================
S["p645"] = '''class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dup = sum(nums) - sum(set(nums))            # 總和多出來的部分 = 重複的那個數
        missing = n * (n + 1) // 2 - sum(set(nums)) # 1..n 的和 - 實際出現的不同數字和
        return [dup, missing]'''

S["p645b"] = '''class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup = missing = -1
        for x in nums:
            i = abs(x) - 1
            if nums[i] < 0:
                dup = abs(x)                # ★ 這個位置已經被標記過 -> x 出現第二次
            else:
                nums[i] = -nums[i]          # 用負號標記「數字 i+1 出現過」
        for i, x in enumerate(nums):
            if x > 0:
                missing = i + 1             # 沒被標記的位置 -> 這個數字沒出現
        return [dup, missing]'''

for key in ("p645", "p645b"):
    sol = S.load(key)
    for _ in range(2000):
        n = random.randint(2, 10); a = list(range(1, n + 1)); m = random.choice(a); d = random.choice([x for x in a if x != m])
        a[a.index(m)] = d; random.shuffle(a)
        assert sol.findErrorNums(a[:]) == [d, m]
print("P645 OK")

em({
 "num": 645, "title": "錯誤的集合",
 "desc": "數學（總和差）或原地負號標記：O(n) 時間，後者 O(1) 額外空間。",
 "zh": [
   "集合 <code>s</code> 原本包含 1 到 <code>n</code> 的所有整數。不幸的是，其中一個數字被複製成另一個數字的值，導致<strong>一個數字重複</strong>、<strong>一個數字遺失</strong>。",
   "給你這個錯誤後的陣列 <code>nums</code>，回傳 <code>[重複的數, 遺失的數]</code>。",
 ],
 "idea": [
   ("c", """【數學】
    sum(nums) - sum(set(nums)) = 重複的數（它多算了一次）
    n(n+1)/2 - sum(set(nums))   = 遺失的數

【原地標記：O(1) 額外空間】
    數字 x 出現 -> 把 nums[x-1] 變成負數。
    標記時發現已經是負數 -> x 是重複的。
    最後仍是正數的位置 i -> 數字 i+1 沒出現過。
    （和第 448 題、第 442 題相同的技巧。）

【其他做法】
    異或：把 nums 與 1..n 全部異或得到 dup ^ missing，
    再依某一位分組找出兩者。"""),
 ],
 "approaches": [
   ap("解法一", "數學", [("c", S["p645"])], "O(n)", "O(n)", "", "set 需要額外空間"),
   ap("解法二", "原地負號標記", [("c", S["p645b"])], "O(n)", "O(1)", "", "會修改輸入", optimal=True),
 ],
 "edges": ["<strong>n = 2</strong> → [1,1] 答案 [1,2]。", "<strong>標記時用 abs</strong> → 值可能已經被改成負數。"],
 "follow": [("h", "原地標記家族"), ("c", "值域在 [1, n] 的陣列可以把「值」當索引，用負號或加 n 來標記出現過——第 41、442、448 題都用這招。")],
 "related": ["<strong>第 448 題 找到所有陣列中消失的數字</strong>", "<strong>第 442 題 陣列中重複的資料</strong>", "<strong>第 268 題 遺失的數字</strong>"],
 "check": ["sum(nums) − sum(set(nums)) 為什麼是重複的數？", "原地標記時為什麼要取絕對值？"],
})
