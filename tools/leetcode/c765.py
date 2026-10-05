# -*- coding: utf-8 -*-
"""第 765、766、767、768、769、770、771、773 題。"""
import random, re, heapq
from collections import Counter, deque
from itertools import permutations
from authoring import ap
from lcauto import em
from runner import Src

S = Src()
random.seed(765)


# ==================== 765. Couples Holding Hands ====================
S["p765"] = '''class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {p: i for i, p in enumerate(row)}
        res = 0
        for i in range(0, len(row), 2):
            partner = row[i] ^ 1                # 情侶編號 2k 與 2k+1：互為 x ^ 1
            if row[i + 1] != partner:
                j = pos[partner]
                # ★ 把伴侶換到 i+1：每次交換至少讓一對坐好，這是最優的
                row[i + 1], row[j] = row[j], row[i + 1]
                pos[row[j]] = j
                pos[row[i + 1]] = i + 1
                res += 1
        return res'''

_p765 = S.load("p765")
def _bf765(row):
    start = tuple(row); n = len(row)
    ok = lambda t: all(t[i] ^ 1 == t[i + 1] for i in range(0, n, 2))
    seen = {start}; q = deque([(start, 0)])
    while q:
        t, d = q.popleft()
        if ok(t): return d
        for i in range(n):
            for j in range(i + 1, n):
                u = list(t); u[i], u[j] = u[j], u[i]; u = tuple(u)
                if u not in seen: seen.add(u); q.append((u, d + 1))
for _ in range(300):
    n = 2 * random.randint(1, 4); row = list(range(n)); random.shuffle(row)
    assert _p765.minSwapsCouples(row[:]) == _bf765(row)
print("P765 OK")

em({
 "num": 765, "title": "情侶牽手",
 "desc": "貪心：每個沙發的第一個人固定不動，把他的伴侶換過來；等價於「沙發圖」的環分解，答案 = 沙發數 − 環數。",
 "zh": [
   "有 <code>n</code> 對情侶坐在連續排列的 <code>2n</code> 個座位上，想要牽手（坐在同一張沙發 <code>(2i, 2i+1)</code>）。人以 0～2n−1 編號，情侶是 <code>(0, 1)</code>、<code>(2, 3)</code>、…。",
   "每次交換可以讓任意兩個人交換座位。回傳讓每對情侶都並肩而坐的<strong>最少交換次數</strong>。",
 ],
 "idea": [
   ("c", """【伴侶編號】
    x 的伴侶是 x ^ 1（0↔1、2↔3……）。

【貪心】
    依序看每張沙發 (i, i+1)：
        若 row[i+1] 不是 row[i] 的伴侶，
        就把伴侶從它現在的位置換過來。
    每次交換都讓一對坐好、不會破壞已坐好的沙發。

【為什麼是最少？環分解】
    把每張沙發當成節點，沙發上的兩個人各自所屬的「情侶編號」連一條邊。
    每個節點度數為 2 -> 圖由若干個環組成。
    一個長度 L 的環需要 L-1 次交換才能拆成 L 個自環（每對坐好），
    而每次交換最多讓環數加一。
    答案 = 沙發數 - 環數，貪心正好達到這個下界。"""),
 ],
 "approaches": [
   ap("解法", "貪心交換", [("c", S["p765"]), "驗證方式：n ≤ 8 時和 BFS 窮舉所有交換序列比對 300 組。"], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>已經全部坐好</strong> → 0。", "<strong>伴侶判斷</strong> → x ^ 1，不是 x + 1。"],
 "follow": [("h", "聯合查找的寫法"), ("c", "對每張沙發，把兩個人的情侶編號（x // 2）合併；答案 = n − 連通分量數。和環分解是同一件事。")],
 "related": ["<strong>第 565 題 陣列巢狀</strong>", "<strong>第 854 題 相似度為 K 的字串</strong>", "<strong>第 41 題 缺失的第一個正數</strong>"],
 "check": ["怎麼用位元運算找到伴侶？", "為什麼答案是沙發數減環數？"],
})


# ==================== 766. Toeplitz Matrix ====================
S["p766"] = '''class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # ★ 每個元素都等於左上角的元素 <=> 每條對角線都相同
        return all(matrix[i][j] == matrix[i - 1][j - 1]
                   for i in range(1, len(matrix)) for j in range(1, len(matrix[0])))'''

_p766 = S.load("p766")
assert _p766.isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]) and not _p766.isToeplitzMatrix([[1, 2], [2, 2]])
print("P766 OK")

em({
 "num": 766, "title": "托普利茲矩陣",
 "desc": "每條左上到右下的對角線元素都相同 ⇔ 每個元素都等於它左上角的元素；只需比較相鄰兩列。",
 "zh": [
   "如果矩陣中每一條<strong>從左上到右下</strong>的對角線上的元素都相同，就稱它為托普利茲矩陣。判斷給定的 <code>m x n</code> 矩陣是否為托普利茲矩陣。",
   "<strong>進階：</strong>如果矩陣存在磁碟上、記憶體每次只能讀入一列呢？如果一次連一整列都讀不進來呢？",
 ],
 "idea": [
   ("c", """【局部條件】
    每條對角線都相同
    <=> 每個元素都等於它左上角的元素 matrix[i-1][j-1]。

【進階一：每次只能讀一列】
    只需要比較「這一列」和「上一列」：
    row[1:] == prev[:-1]。
    保留上一列即可。

【進階二：連一列都讀不進來】
    把每一列切成幾段讀，比較時多讀一個重疊的元素；
    或依對角線方向分塊處理。"""),
 ],
 "approaches": [
   ap("解法", "和左上角比較", [("c", S["p766"])], "O(mn)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>只有一列或一欄</strong> → True。"],
 "follow": [("h", "托普利茲矩陣的應用"), ("c", "在訊號處理中，卷積可以寫成托普利茲矩陣乘法；托普利茲系統有專門的快速解法（Levinson 演算法，O(n²)）。")],
 "related": ["<strong>第 498 題 對角線遍歷</strong>", "<strong>第 1329 題 將矩陣按對角線排序</strong>"],
 "check": ["「每條對角線相同」怎麼化成局部的條件？", "只能讀一列時要怎麼做？"],
})


# ==================== 767. Reorganize String ====================
S["p767"] = '''class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        cnt = Counter(s)
        if max(cnt.values()) > (n + 1) // 2:
            return ""                           # 最多的字母太多：一定會有兩個相鄰
        res = [""] * n
        i = 0
        for ch, c in sorted(cnt.items(), key=lambda x: -x[1]):   # 由多到少
            for _ in range(c):
                res[i] = ch
                i += 2                          # ★ 先填偶數位置，填滿再填奇數位置
                if i >= n:
                    i = 1
        return "".join(res)'''

_p767 = S.load("p767")
for _ in range(3000):
    s = "".join(random.choice("aabbc") for _ in range(random.randint(1, 9)))
    r = _p767.reorganizeString(s)
    possible = max(Counter(s).values()) <= (len(s) + 1) // 2
    if possible:
        assert sorted(r) == sorted(s) and all(r[i] != r[i + 1] for i in range(len(r) - 1))
    else:
        assert r == ""
print("P767 OK")

em({
 "num": 767, "title": "重構字串",
 "desc": "最多的字母不超過 ⌈n/2⌉ 就一定可行：由多到少，先填所有偶數位置，再填奇數位置。",
 "zh": ["給你字串 <code>s</code>，重新排列它的字元，使任意兩個<strong>相鄰的字元都不相同</strong>。回傳任何一種可行的結果；不可能則回傳空字串。"],
 "idea": [
   ("c", """【什麼時候不可能？】
    最多的字母出現 m 次，若 m > ⌈n/2⌉，
    就算隔一個放一個也放不下 -> 一定有相鄰。
    反之一定可行。

【構造：隔位填】
    依次數由多到少，把字母依序填進 0, 2, 4, ...，
    偶數位置填滿後接著填 1, 3, 5, ...。
    最多的字母先填，保證它只佔偶數位置（不會自己相鄰）；
    其他字母的次數 <= ⌈n/2⌉，跨越奇偶時也不會和自己相鄰。

【堆積做法】
    每次從最大堆積取出次數最多、且和上一個字元不同的字母。"""),
 ],
 "approaches": [
   ap("解法", "計數 + 隔位填", [("c", S["p767"]), "驗證方式：檢查輸出是原字串的排列且相鄰不同；不可能時回傳空字串（3000 組）。"], "O(n)", "O(n)", "字母只有 26 種，排序是常數", "", optimal=True),
 ],
 "edges": ["<strong>\"aaab\"</strong> → \"\"。", "<strong>單一字元</strong> → 自己。", "<strong>m 剛好等於 ⌈n/2⌉</strong>（n 為奇數）→ 可行，最多的字母佔滿所有偶數位置。"],
 "follow": [("h", "一般化：相同字元至少間隔 k"), ("c", "第 358 題（付費）、第 621 題（任務排程器）：用最大堆積每輪取 k 個不同的字元。")],
 "related": ["<strong>第 621 題 任務排程器</strong>", "<strong>第 1054 題 距離相等的條形碼</strong>", "<strong>第 358 題 K 距離間隔重排字串</strong>（付費）"],
 "check": ["什麼情況下不可能？", "為什麼要從次數最多的字母開始填？"],
})


# ==================== 768. Max Chunks To Make Sorted II ====================
S["p768"] = '''class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        st = []                         # 每個區塊的最大值（由下往上遞增）
        for x in arr:
            if st and st[-1] > x:
                mx = st.pop()
                while st and st[-1] > x:
                    st.pop()            # ★ x 比前面的區塊小：那些區塊都必須和 x 合併
                st.append(mx)           # 合併後的區塊最大值不變
            else:
                st.append(x)            # x 不小於前面所有區塊：自己成為新區塊
        return len(st)'''

_p768 = S.load("p768")
def _bf768(a):
    n = len(a); best = 0
    for mask in range(1 << (n - 1)):
        cuts = [0] + [i + 1 for i in range(n - 1) if mask >> i & 1] + [n]
        if sum((sorted(a[cuts[i]:cuts[i + 1]]) for i in range(len(cuts) - 1)), []) == sorted(a):
            best = max(best, len(cuts) - 1)
    return best
for _ in range(2000):
    a = [random.randint(0, 5) for _ in range(random.randint(1, 8))]
    assert _p768.maxChunksToSorted(a) == _bf768(a)
print("P768 OK")

em({
 "num": 768, "title": "最多能完成排序的區塊 II",
 "desc": "單調堆疊存每個區塊的最大值：新元素比前面區塊的最大值小，就要把那些區塊合併；可以有重複值。",
 "zh": [
   "給你一個整數陣列 <code>arr</code>（<strong>可能有重複值</strong>）。把它切成若干個區塊，各區塊分別排序後再接起來，結果要和整個陣列排序後相同。",
   "回傳最多能切成幾個區塊。",
 ],
 "idea": [
   ("c", """【什麼時候可以在 i 後面切？】
    左邊所有元素的最大值 <= 右邊所有元素的最小值。

【做法一：前綴最大 + 後綴最小】
    maxL[i] <= minR[i+1] 的位置都可以切，數一數即可。O(n)。

【做法二：單調堆疊（每個區塊存最大值）】
    新元素 x：
        x >= 堆疊頂端（前一個區塊的最大值）-> 自己成為新區塊
        x <  頂端 -> x 必須和前面的區塊合併；
                    所有最大值 > x 的區塊都要被吞進來，
                    合併後的最大值是原本頂端的最大值。
    最後堆疊的大小就是區塊數。"""),
 ],
 "approaches": [
   ap("解法一", "前綴最大 + 後綴最小", [("c", "可以在 i 之後切 <=> max(arr[:i+1]) <= min(arr[i+1:])")], "O(n)", "O(n)"),
   ap("解法二", "單調堆疊", [("c", S["p768"]), "驗證方式：和枚舉所有切法的暴力法比對 2000 組。"], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>重複值</strong> → 用 <= 判斷（相等可以切開）。", "<strong>已經排序</strong> → n 塊。", "<strong>完全逆序</strong> → 1 塊。"],
 "follow": [("h", "排列的特例"), ("c", "第 769 題：陣列是 0..n−1 的排列，只要前 i+1 個元素的最大值等於 i 就能切，更簡單。")],
 "related": ["<strong>第 769 題 最多能完成排序的區塊</strong>", "<strong>第 581 題 最短無序連續子陣列</strong>"],
 "check": ["在某個位置可以切的條件是什麼？", "新元素比堆疊頂端小時，為什麼合併後要把原本的最大值放回去？"],
})


# ==================== 769. Max Chunks To Make Sorted ====================
S["p769"] = '''class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = mx = 0
        for i, x in enumerate(arr):
            mx = max(mx, x)
            if mx == i:             # ★ 前 i+1 個數的最大值是 i：它們恰好是 0..i，可以切
                res += 1
        return res'''

_p769 = S.load("p769")
for _ in range(2000):
    n = random.randint(1, 8); a = list(range(n)); random.shuffle(a)
    assert _p769.maxChunksToSorted(a) == _bf768(a)
print("P769 OK")

em({
 "num": 769, "title": "最多能完成排序的區塊",
 "desc": "陣列是 0..n−1 的排列：前 i+1 個數的最大值等於 i，就代表它們恰好是 0..i，可以在這裡切。",
 "zh": ["給你一個長度為 <code>n</code> 的陣列 <code>arr</code>，它是 <code>[0, n−1]</code> 的一個排列。把它切成若干區塊，各自排序後接起來要等於排序後的陣列。回傳最多能切成幾塊。"],
 "idea": [
   ("c", """【排列的特性】
    前 i+1 個數是 0..i 的排列 <=> 它們排序後恰好放在正確位置
    <=> 可以在 i 後面切。

【怎麼判斷前 i+1 個數恰好是 0..i？】
    它們是 i+1 個不同的非負整數，
    最大值 == i <=> 剛好是 0..i（不可能有更小的缺口）。

    一趟掃描維護前綴最大值。"""),
 ],
 "approaches": [
   ap("解法", "前綴最大值", [("c", S["p769"]), "驗證方式：和枚舉所有切法的暴力法比對 2000 組。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>已經排序</strong> → n。", "<strong>[1, 0, ...]</strong> → 前兩個必須在同一塊。"],
 "follow": [("h", "一般情況"), ("c", "有重複值或任意值時（第 768 題），改用前綴最大 ≤ 後綴最小，或單調堆疊。")],
 "related": ["<strong>第 768 題 最多能完成排序的區塊 II</strong>", "<strong>第 763 題 劃分字母區間</strong>"],
 "check": ["為什麼前綴最大值等於 i 就可以切？"],
})


# ==================== 770. Basic Calculator IV ====================
S["p770"] = '''class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        env = dict(zip(evalvars, evalints))
        # 多項式：{(變數1, 變數2, ...)（排序後的 tuple）: 係數}，常數項的鍵是 ()
        def add(p, q, sign=1):
            r = Counter(p)
            for k, v in q.items():
                r[k] += sign * v
            return r
        def mul(p, q):
            r = Counter()
            for k1, v1 in p.items():
                for k2, v2 in q.items():
                    r[tuple(sorted(k1 + k2))] += v1 * v2
            return r

        tokens = re.findall(r"\\d+|[a-z]+|[()+\\-*]", expression)
        pos = 0
        def atom():
            nonlocal pos
            t = tokens[pos]
            pos += 1
            if t == "(":
                p = expr()
                pos += 1                        # 跳過 ')'
                return p
            if t.isdigit():
                return Counter({(): int(t)})
            if t in env:
                return Counter({(): env[t]})    # 已知的變數直接代入數值
            return Counter({(t,): 1})
        def term():                             # ★ 乘法優先：term 處理連乘
            nonlocal pos
            p = atom()
            while pos < len(tokens) and tokens[pos] == "*":
                pos += 1
                p = mul(p, atom())
            return p
        def expr():                             # expr 處理加減
            nonlocal pos
            p = term()
            while pos < len(tokens) and tokens[pos] in "+-":
                sign = 1 if tokens[pos] == "+" else -1
                pos += 1
                p = add(p, term(), sign)
            return p

        poly = expr()
        # 輸出排序：次數高的在前，同次數依變數的字典序；係數為 0 的不輸出
        items = sorted(((k, v) for k, v in poly.items() if v), key=lambda kv: (-len(kv[0]), kv[0]))
        return ["*".join([str(v)] + list(k)) for k, v in items]'''

_p770 = S.load("p770")
cases = [
    ("e + 8 - a + 5", ["e"], [1], ["-1*a", "14"]),
    ("e - 8 + temperature - pressure", ["e", "temperature"], [1, 12], ["-1*pressure", "5"]),
    ("(e + 8) * (e - 8)", [], [], ["1*e*e", "-64"]),
    ("a * b * c + b * a * c * 4", [], [], ["5*a*b*c"]),
    ("((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", [], [],
     ["-1*a*a*b*b", "2*a*a*b*c", "-1*a*a*c*c", "1*a*b*b*b", "-1*a*b*b*c", "-1*a*b*c*c", "1*a*c*c*c", "-1*b*b*b*c", "2*b*b*c*c", "-1*b*c*c*c", "2*a*a*b", "-2*a*a*c", "-2*a*b*b", "2*a*c*c", "1*b*b*b", "-1*b*b*c", "1*b*c*c", "-1*c*c*c", "-1*a*a", "1*a*b", "1*a*c", "-1*b*c"]),
    ("a - a", [], [], []),
]
for e, vs, ints, want in cases:
    assert _p770.basicCalculatorIV(e, vs, ints) == want, (e, _p770.basicCalculatorIV(e, vs, ints))
print("P770 OK")

em({
 "num": 770, "title": "基本計算機 IV",
 "desc": "遞迴下降解析 + 多項式運算：每個子運算式算成「單項式 → 係數」的字典，加減合併同類項、乘法兩兩相乘；最後依次數與字典序輸出。",
 "zh": [
   "給你一個運算式（含 <code>+</code>、<code>-</code>、<code>*</code>、括號、非負整數與小寫變數），以及一部分變數的值 <code>evalvars</code>、<code>evalints</code>。代入已知的變數後，把運算式<strong>化簡</strong>成多項式。",
   "輸出格式：每一項寫成 <code>\"係數*變數*變數...\"</code>（變數依字典序排列，係數 1 也要寫），項的順序是<strong>次數高的在前</strong>，同次數依變數序列的字典序；常數項放最後，係數為 0 的項不輸出。",
 ],
 "idea": [
   ("c", """【多項式的表示】
    {單項式: 係數}，單項式用排序後的變數 tuple 表示：
        3·a·b·b -> {("a","b","b"): 3}
        常數 5   -> {(): 5}

【運算】
    加減：同一個鍵的係數相加減（合併同類項）。
    乘法：兩邊每一項兩兩相乘，變數 tuple 串接後排序，係數相乘。

【解析：運算子優先順序】
    expr := term (('+'|'-') term)*
    term := atom ('*' atom)*
    atom := 數字 | 變數 | '(' expr ')'
    已知的變數在 atom 就直接換成常數。

【輸出排序】
    (-次數, 變數 tuple)；過濾係數為 0 的項。"""),
 ],
 "approaches": [
   ap("解法", "遞迴下降 + 多項式字典", [("c", S["p770"]), "驗證方式：題目所有範例（含展開後 22 項的長多項式），以及完全相消的 a − a。"], "O(T²)", "O(T)", "T 為多項式的項數；乘法是兩兩相乘", "", optimal=True),
 ],
 "edges": ["<strong>係數為 0</strong> → 不輸出（可能全部消掉，回傳空陣列）。", "<strong>係數 1</strong> → 仍要寫出 \"1*a\"。", "<strong>變數順序</strong> → b*a 和 a*b 是同一項。"],
 "follow": [("h", "計算機系列"), ("c", "第 224 題（加減與括號）、第 227 題（加減乘除）、第 772 題（四則加括號，付費）、本題（符號運算）——一路從數值計算走到電腦代數系統（CAS）的雛形。")],
 "related": ["<strong>第 224 題 基本計算機</strong>", "<strong>第 227 題 基本計算機 II</strong>", "<strong>第 736 題 Lisp 語法解析</strong>"],
 "check": ["單項式為什麼要用排序後的 tuple 表示？", "解析時怎麼處理乘法優先於加減？", "輸出的排序規則是什麼？"],
})


# ==================== 771. Jewels and Stones ====================
S["p771"] = '''class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        J = set(jewels)                     # ★ 用集合查詢 O(1)
        return sum(c in J for c in stones)'''

_p771 = S.load("p771")
assert _p771.numJewelsInStones("aA", "aAAbbbb") == 3 and _p771.numJewelsInStones("z", "ZZ") == 0
print("P771 OK")

em({
 "num": 771, "title": "寶石與石頭",
 "desc": "把寶石種類放進集合，數一數石頭中有幾顆在集合裡。",
 "zh": ["字串 <code>jewels</code> 代表哪些種類的石頭是寶石（字母互不相同），<code>stones</code> 代表你擁有的石頭。回傳你擁有的石頭中有幾顆是寶石（區分大小寫）。"],
 "idea": [
   ("c", """【集合查詢】
    逐一檢查每顆石頭是否在寶石集合中。
    用 list 查詢是 O(|J|)，用 set 是 O(1)。"""),
 ],
 "approaches": [
   ap("解法", "雜湊集合", [("c", S["p771"])], "O(|J| + |S|)", "O(|J|)", optimal=True),
 ],
 "edges": ["<strong>大小寫不同</strong> → 視為不同種類。"],
 "follow": [("h", "位元遮罩"), ("c", "字母只有 52 種，可以用一個 64 位元整數當集合：第 (ord(c) − 65) 位代表該字母是寶石。")],
 "related": ["<strong>第 383 題 贖金信</strong>", "<strong>第 349 題 兩個陣列的交集</strong>"],
 "check": ["為什麼要把寶石轉成集合？"],
})


# ==================== 773. Sliding Puzzle ====================
S["p773"] = '''class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # 2×3 的盤面攤平成字串；每個位置的 0 可以和哪些位置交換
        nbr = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        start = "".join(str(x) for row in board for x in row)
        goal = "123450"
        seen = {start}
        q = deque([(start, 0)])
        while q:
            s, d = q.popleft()
            if s == goal:
                return d
            z = s.index("0")
            for j in nbr[z]:                    # ★ 把空格和相鄰的數字交換：一步
                t = list(s)
                t[z], t[j] = t[j], t[z]
                t = "".join(t)
                if t not in seen:
                    seen.add(t)
                    q.append((t, d + 1))
        return -1'''

_p773 = S.load("p773")
assert _p773.slidingPuzzle([[1, 2, 3], [4, 0, 5]]) == 1 and _p773.slidingPuzzle([[1, 2, 3], [5, 4, 0]]) == -1
assert _p773.slidingPuzzle([[4, 1, 2], [5, 0, 3]]) == 5
# 可解性：2×3 盤面中，不含 0 的排列的逆序數奇偶要和目標相同
for _ in range(200):
    p = list(range(6)); random.shuffle(p)
    r = _p773.slidingPuzzle([p[:3], p[3:]])
    seq = [x for x in p if x]; inv = sum(seq[i] > seq[j] for i in range(5) for j in range(i + 1, 5))
    assert (r == -1) == (inv % 2 == 1)
print("P773 OK")

em({
 "num": 773, "title": "滑動謎題",
 "desc": "盤面只有 6! = 720 種狀態：把盤面攤平成字串當節點，空格與相鄰數字交換當邊，從起點 BFS 找最少步數。",
 "zh": [
   "在 2×3 的盤面上有數字 1～5 和一個空格 0。每一步可以把 0 和<strong>上下左右</strong>相鄰的數字交換。",
   "當盤面變成 <code>[[1,2,3],[4,5,0]]</code> 時謎題就解開了。回傳解開所需的<strong>最少步數</strong>；無解則回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【狀態空間很小】
    6 個位置放 0～5 的排列：6! = 720 種。

【BFS】
    狀態：盤面攤平成字串，例如 "123405"。
    鄰居：找到 '0' 的位置 z，和 nbr[z] 中的位置交換。
        位置編號    鄰居
        0 1 2      0:(1,3) 1:(0,2,4) 2:(1,5)
        3 4 5      3:(0,4) 4:(1,3,5) 5:(2,4)
    BFS 第一次到達 "123450" 的層數就是答案；
    走完都沒到就是無解。

【可解性】
    只有一半的盤面（逆序數為偶數的）可解，
    這是 15 數字推盤遊戲同樣的奇偶性論證。"""),
 ],
 "approaches": [
   ap("解法", "狀態圖上的 BFS", [("c", S["p773"]), "驗證方式：題目範例；並對 200 個隨機盤面檢查「無解 ⇔ 不含 0 的序列逆序數為奇數」。"], "O(6! · 6)", "O(6!)", optimal=True),
 ],
 "edges": ["<strong>已經解開</strong> → 0。", "<strong>無解的盤面</strong>（如交換 4、5）→ −1。"],
 "follow": [("h", "更大的盤面"), ("c", "3×3 的八數字推盤有 9!/2 ≈ 18 萬個可解狀態，BFS 仍可行；4×4 的十五數字推盤約 10¹³ 個狀態，就需要 A*（曼哈頓距離啟發式）或 IDA*。")],
 "related": ["<strong>第 752 題 打開轉盤鎖</strong>", "<strong>第 127 題 單字接龍</strong>", "<strong>第 864 題 獲取所有鑰匙的最短路徑</strong>"],
 "check": ["為什麼狀態只有 720 種？", "鄰居表 nbr 是怎麼來的？", "為什麼有些盤面無解？"],
})
