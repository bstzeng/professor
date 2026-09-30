# -*- coding: utf-8 -*-
"""第 301、303、304、306、307、309 題。"""
import random
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(301)


# ==================== 301. Remove Invalid Parentheses ====================
S["p301_bfs"] = '''class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def valid(t: str) -> bool:
            bal = 0
            for ch in t:
                if ch == "(":
                    bal += 1
                elif ch == ")":
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        level = {s}
        while level:
            ok = [t for t in level if valid(t)]
            if ok:                               # ★ BFS：第一層出現合法字串 = 刪除最少
                return ok
            nxt = set()                          # 每個字串再多刪一個括號
            for t in level:
                for i, ch in enumerate(t):
                    if ch in "()":
                        nxt.add(t[:i] + t[i + 1:])
            level = nxt
        return [""]'''

S["p301_dfs"] = '''class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # 先算出「至少要刪幾個左括號、幾個右括號」
        rm_l = rm_r = 0
        for ch in s:
            if ch == "(":
                rm_l += 1
            elif ch == ")":
                if rm_l:
                    rm_l -= 1           # 和前面的 ( 配對
                else:
                    rm_r += 1           # 多出來的 )，一定要刪

        res = set()

        def dfs(i: int, bal: int, rl: int, rr: int, path: List[str]):
            if bal < 0 or rl < 0 or rr < 0:          # 剪枝
                return
            if i == len(s):
                if bal == 0 and rl == 0 and rr == 0:
                    res.add("".join(path))
                return
            ch = s[i]
            if ch == "(":
                dfs(i + 1, bal, rl - 1, rr, path)    # 刪掉這個 (
                path.append(ch)
                dfs(i + 1, bal + 1, rl, rr, path)    # 保留
                path.pop()
            elif ch == ")":
                dfs(i + 1, bal, rl, rr - 1, path)    # 刪掉這個 )
                path.append(ch)
                dfs(i + 1, bal - 1, rl, rr, path)    # 保留
                path.pop()
            else:                                    # 字母一定保留
                path.append(ch)
                dfs(i + 1, bal, rl, rr, path)
                path.pop()

        dfs(0, 0, rm_l, rm_r, [])
        return list(res)'''

_p301 = [S.load(x) for x in ("p301_bfs", "p301_dfs")]
for s, want in [("()())()", ["(())()", "()()()"]), ("(a)())()", ["(a())()", "(a)()()"]), (")(", [""]), ("x(", ["x"]), ("", [""])]:
    for sol in _p301:
        assert sorted(sol.removeInvalidParentheses(s)) == sorted(want), (s, sol)
for _ in range(1500):
    s = "".join(random.choice("(()a)") for _ in range(random.randrange(0, 11)))
    a, b = (sorted(sol.removeInvalidParentheses(s)) for sol in _p301)
    assert a == b, s
print("P301 OK")

emit({
 "num": 301, "slug": "remove-invalid-parentheses",
 "en": [
   "Given a string <code>s</code> that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.",
   "Return <em>a list of <strong>unique strings</strong> that are valid with the minimum number of removals</em>. You may return the answer in <strong>any order</strong>.",
 ],
 "zh": [
   "給你一個包含括號和字母的字串 <code>s</code>，刪除<strong>最少數量</strong>的無效括號，使字串變成合法的。",
   "回傳所有可能的結果（<strong>不重複</strong>），順序不限。",
 ],
 "examples": """範例 1
  輸入：s = "()())()"
  輸出：["(())()","()()()"]

範例 2
  輸入：s = "(a)())()"
  輸出：["(a())()","(a)()()"]

範例 3
  輸入：s = ")("
  輸出：[""]""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 25",
   "<code>s</code> 由小寫英文字母和 <code>'('</code>、<code>')'</code> 組成",
   "<code>s</code> 中最多有 20 個括號",
 ],
 "idea": [
   ("c", """【合法括號的判斷】
    從左到右維護 bal（未配對的左括號數）：
        ( -> +1，) -> -1
        途中 bal < 0 -> 不合法（右括號多了）
        結尾 bal != 0 -> 不合法（左括號多了）

【方法一：BFS 按「刪除個數」分層】
    第 0 層：原字串
    第 k 層：刪掉 k 個括號的所有字串（用集合去重）
    第一次在某一層找到合法字串 -> 這一層所有合法的就是答案。
    BFS 天然保證「最少」。

【方法二：先算出要刪幾個，再 DFS】
    掃一遍：
        遇到 ( -> 待配對 +1
        遇到 ) -> 有待配對的就配對；沒有就是「多餘的 )」，必須刪
    最後剩下沒配對的 ( 也必須刪。
    -> 知道恰好要刪 rm_l 個 (、rm_r 個 )。
    DFS 時每個括號選「刪」或「留」，
    刪的額度用完、或 bal < 0 就剪枝。"""),
   ("c", """  "()())()"
   bal: 1 0 1 0 -1  ← 第 5 個字元的 ) 多餘
  rm_l = 0，rm_r = 1：恰好刪一個 )
  刪第 2 個 ) -> "(())()"
  刪第 4 個 ) -> "()()()"
  刪第 5 個 ) -> "()()()"（重複，集合去掉）"""),
 ],
 "approaches": [
   ap("解法一", "BFS 分層", [
     ("c", S["p301_bfs"]),
     "最壞情況下每一層的字串數是組合數 C(n, k)，但因為答案層很淺，而且有集合去重，實際上很快。",
   ], "O(n · 2ⁿ)", "O(n · 2ⁿ)", "最壞情況", ""),

   ap("解法二", "計算刪除數 + 回溯剪枝", [
     ("c", S["p301_dfs"]),
   ], "O(n · 2ⁿ)", "O(n)", "剪枝後實際快很多", "遞迴深度", optimal=True),
 ],
 "compare": (["解法", "時間（最壞）", "備註"],
   [["一、BFS", "O(n·2ⁿ)", "最直觀，保證最少"],
    ["二、DFS + 剪枝", "O(n·2ⁿ)", "剪枝效果好 ✔"]]),
 "edges": [
   "<strong>已經合法</strong> → 回傳原字串。",
   "<strong>全部都得刪</strong>（<code>\")(\"</code>）→ <code>[\"\"]</code>。",
   "<strong>字母</strong> → 永遠保留，不影響 bal。",
   "<strong>重複結果</strong> → 刪相鄰的相同括號會得到相同字串，要去重。",
 ],
 "follow": [
   ("h", "DFS 避免重複的技巧"),
   ("c", "連續相同的括號（例如 \"))\"）中刪哪一個結果都一樣；可以規定「只刪連續段的第一個」來避免產生重複，就不需要集合去重。"),
 ],
 "related": [
   "<strong>第 20 題 有效的括號</strong>",
   "<strong>第 22 題 括號生成</strong>",
   "<strong>第 921 題 使括號有效的最少添加</strong>",
   "<strong>第 1249 題 移除無效的括號</strong> —— 只要一個答案",
 ],
 "check": [
   "怎麼判斷一個字串的括號是否合法？",
   "BFS 為什麼能保證刪除數最少？",
   "怎麼事先算出至少要刪幾個左括號、幾個右括號？",
 ],
})


# ==================== 303. Range Sum Query - Immutable ====================
S["p303"] = '''class NumArray:
    def __init__(self, nums: List[int]):
        # ★ prefix[i] = nums[0] + ... + nums[i-1]（prefix[0] = 0）
        self.prefix = [0]
        for x in nums:
            self.prefix.append(self.prefix[-1] + x)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]'''

_cls = S.loadns("p303")["NumArray"]
for _ in range(500):
    nums = [random.randint(-9, 9) for _ in range(random.randrange(1, 15))]
    na = _cls(nums)
    for _ in range(20):
        l = random.randrange(len(nums))
        r = random.randrange(l, len(nums))
        assert na.sumRange(l, r) == sum(nums[l:r + 1])
print("P303 OK")

emit({
 "num": 303, "slug": "range-sum-query-immutable",
 "en": [
   "Given an integer array <code>nums</code>, handle multiple queries of the following type: calculate the <strong>sum</strong> of the elements of <code>nums</code> between indices "
   "<code>left</code> and <code>right</code> <strong>inclusive</strong> where <code>left &lt;= right</code>.",
   "Implement the <code>NumArray</code> class:",
   ("ul", ["<code>NumArray(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.",
           "<code>int sumRange(int left, int right)</code> Returns the sum of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> inclusive."]),
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，要處理<strong>多次</strong>查詢：計算索引 <code>left</code> 到 <code>right</code>（<strong>包含兩端</strong>）之間元素的總和。",
   ("ul", ["<code>NumArray(nums)</code>：用陣列初始化。",
           "<code>sumRange(left, right)</code>：回傳 <code>nums[left] + ... + nums[right]</code>。"]),
 ],
 "examples": """範例
  輸入：["NumArray", "sumRange", "sumRange", "sumRange"]
        [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
  輸出：[null, 1, -1, -3]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁴",
   "−10⁵ ≤ <code>nums[i]</code> ≤ 10⁵",
   "0 ≤ <code>left ≤ right</code> &lt; <code>nums.length</code>",
   "最多呼叫 10⁴ 次 <code>sumRange</code>",
 ],
 "idea": [
   ("c", """【陣列不會變、查詢很多次 -> 預處理】
    每次查詢都加一遍是 O(n)，10⁴ × 10⁴ = 10⁸ 太慢。

【前綴和】
    prefix[i] = 前 i 個元素的和（nums[0..i-1]）
    prefix[0] = 0

    sum(left..right) = prefix[right + 1] - prefix[left]
                       └ 前 right+1 個 ┘   └ 前 left 個 ┘

【為什麼 prefix 多一格？】
    讓 left = 0 不用特判：prefix[0] = 0。

    nums   =    [-2,  0,  3, -5,  2, -1]
    prefix = [0, -2, -2,  1, -4, -2, -3]
    sumRange(2, 5) = prefix[6] - prefix[2] = -3 - (-2) = -1 ✔"""),
 ],
 "approaches": [
   ap("解法", "前綴和", [
     ("c", S["p303"]),
     "Python 也可以直接寫 <code>self.prefix = [0, *itertools.accumulate(nums)]</code>。",
   ], "建構 O(n)，查詢 O(1)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>left = 0</strong> → 用 prefix[0] = 0，不用特判。",
   "<strong>left = right</strong> → 單一元素。",
   "<strong>負數</strong> → 前綴和照常。",
 ],
 "follow": [
   ("h", "如果陣列會被修改？"),
   ("c", "第 307 題：前綴和每次修改要 O(n) 更新。改用樹狀陣列或線段樹，修改和查詢都是 O(log n)。"),
 ],
 "related": [
   "<strong>第 304 題 二維區域和檢索 - 矩陣不可變</strong>",
   "<strong>第 307 題 區域和檢索 - 陣列可修改</strong>",
   "<strong>第 560 題 和為 K 的子陣列</strong> —— 前綴和 + 雜湊表",
 ],
 "check": [
   "prefix[i] 的定義是什麼？",
   "sumRange(left, right) 怎麼用前綴和算？",
   "為什麼 prefix 要多一格？",
 ],
})


# ==================== 304. Range Sum Query 2D - Immutable ====================
S["p304"] = '''class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        # P[i][j] = 左上角 (0,0) 到 (i-1, j-1) 的矩形總和（多一圈 0）
        self.P = P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                # ★ 上 + 左 - 左上（重複算了一次）+ 自己
                P[i + 1][j + 1] = P[i][j + 1] + P[i + 1][j] - P[i][j] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        P = self.P
        # 大矩形 - 上面一條 - 左邊一條 + 被扣兩次的左上角
        return P[row2 + 1][col2 + 1] - P[row1][col2 + 1] - P[row2 + 1][col1] + P[row1][col1]'''

_cls = S.loadns("p304")["NumMatrix"]
for _ in range(300):
    m, n = random.randrange(1, 7), random.randrange(1, 7)
    M = [[random.randint(-9, 9) for _ in range(n)] for _ in range(m)]
    nm = _cls(M)
    for _ in range(20):
        r1 = random.randrange(m); r2 = random.randrange(r1, m)
        c1 = random.randrange(n); c2 = random.randrange(c1, n)
        assert nm.sumRegion(r1, c1, r2, c2) == sum(M[i][j] for i in range(r1, r2 + 1) for j in range(c1, c2 + 1))
print("P304 OK")

_P304_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">二維前綴和：用四個「從左上角開始的矩形」拼出任意矩形</text>
            <rect x="40" y="40" width="240" height="180" fill="var(--text-muted)" opacity="0.10" stroke="var(--border)"/>
            <rect x="40" y="40" width="240" height="70" fill="#ff8a65" opacity="0.18"/>
            <rect x="40" y="40" width="90" height="180" fill="var(--accent)" opacity="0.18"/>
            <rect x="130" y="110" width="150" height="110" fill="none" stroke="var(--gold)" stroke-width="2.5"/>
            <text x="205" y="170" text-anchor="middle" fill="var(--gold)" font-size="13">要求的區域</text>
            <text x="200" y="80" text-anchor="middle" fill="#ff8a65" font-size="12">上方一條</text>
            <text x="85" y="170" text-anchor="middle" fill="var(--accent)" font-size="12">左邊一條</text>
            <text x="85" y="80" text-anchor="middle" fill="var(--text)" font-size="11">重疊</text>
            <text x="310" y="60" fill="var(--text)" font-size="12">答案 = P(整個大矩形)</text>
            <text x="310" y="84" fill="#ff8a65" font-size="12">　　　− P(上方一條)</text>
            <text x="310" y="108" fill="var(--accent)" font-size="12">　　　− P(左邊一條)</text>
            <text x="310" y="132" fill="var(--text)" font-size="12">　　　+ P(左上角重疊)  ← 被扣了兩次</text>
            <text x="310" y="176" fill="var(--text-muted)" font-size="12">建表也是同一個排容原理：</text>
            <text x="310" y="198" fill="var(--text-muted)" font-size="12">P = 上 + 左 − 左上 + 自己</text>'''

emit({
 "num": 304, "slug": "range-sum-query-2d-immutable",
 "en": [
   "Given a 2D matrix <code>matrix</code>, handle multiple queries of the following type: calculate the <strong>sum</strong> of the elements of <code>matrix</code> inside the rectangle "
   "defined by its <strong>upper left corner</strong> <code>(row1, col1)</code> and <strong>lower right corner</strong> <code>(row2, col2)</code>.",
   "Implement the <code>NumMatrix</code> class:",
   ("ul", ["<code>NumMatrix(int[][] matrix)</code> Initializes the object with the integer matrix <code>matrix</code>.",
           "<code>int sumRegion(int row1, int col1, int row2, int col2)</code> Returns the sum of the elements of <code>matrix</code> inside the rectangle defined by its upper left corner "
           "<code>(row1, col1)</code> and lower right corner <code>(row2, col2)</code>."]),
   "You must design an algorithm where <code>sumRegion</code> works on <code>O(1)</code> time complexity.",
 ],
 "zh": [
   "給你一個二維矩陣 <code>matrix</code>，要處理多次查詢：計算左上角 <code>(row1, col1)</code>、右下角 <code>(row2, col2)</code> 的矩形內所有元素的總和。",
   "<code>sumRegion</code> 必須是 <code>O(1)</code>。",
 ],
 "examples": """範例
  輸入：["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
        [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]],
         [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
  輸出：[null, 8, 11, 12]""",
 "constraints": [
   "1 ≤ <code>m, n</code> ≤ 200",
   "−10⁴ ≤ <code>matrix[i][j]</code> ≤ 10⁴",
   "0 ≤ <code>row1 ≤ row2</code> &lt; m，0 ≤ <code>col1 ≤ col2</code> &lt; n",
   "最多呼叫 10⁴ 次 <code>sumRegion</code>",
 ],
 "idea": [
   ("fig", _P304_FIG, "0 0 640 234"),
   ("c", """【第 303 題的二維版】
    P[i][j] = 左上角 (0,0) 到 (i-1, j-1) 的矩形總和
    （和一維一樣多開一圈 0，省掉邊界判斷）

【建表：排容原理】
    P[i+1][j+1] = P[i][j+1]        上方的矩形
                + P[i+1][j]        左方的矩形
                - P[i][j]          左上角被加了兩次
                + matrix[i][j]     自己

【查詢：也是排容原理】
    sum = P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]"""),
 ],
 "approaches": [
   ap("解法", "二維前綴和", [
     ("c", S["p304"]),
   ], "建構 O(mn)，查詢 O(1)", "O(mn)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>row1 = 0 或 col1 = 0</strong> → 多開的一圈 0 讓公式不用特判。",
   "<strong>單一格子</strong> → 公式照樣成立。",
   "<strong>負數</strong> → 沒問題。",
 ],
 "follow": [
   ("h", "二維差分"),
   ("c", "反過來：「對一個矩形區域全部加上 v」很多次，最後求整個矩陣——在四個角落做 +v、−v、−v、+v，最後做一次二維前綴和。第 2536 題就是這個。"),
 ],
 "related": [
   "<strong>第 303 題 區域和檢索 - 陣列不可變</strong>",
   "<strong>第 1314 題 矩陣區域和</strong>",
   "<strong>第 221 題 最大正方形</strong>",
   "<strong>第 308 題 二維區域和檢索 - 可變</strong>（付費）—— 二維樹狀陣列",
 ],
 "check": [
   "P[i][j] 代表哪個矩形？",
   "建表時為什麼要減掉 P[i][j]？",
   "查詢公式中為什麼要加回 P[r1][c1]？",
 ],
})


# ==================== 306. Additive Number ====================
S["p306"] = '''class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        # ★ 只要決定前兩個數，後面整個序列就被唯一確定了
        for i in range(1, n):                        # 第一個數 = num[:i]
            if num[0] == "0" and i > 1:              # 前導零
                break
            for j in range(i + 1, n):                # 第二個數 = num[i:j]
                if num[i] == "0" and j > i + 1:
                    break
                a, b, k = int(num[:i]), int(num[i:j]), j
                while k < n:                          # 一路驗證下去
                    c = str(a + b)
                    if not num.startswith(c, k):
                        break
                    k += len(c)
                    a, b = b, a + b
                if k == n and k > j:                  # 走到結尾，而且至少有第三個數
                    return True
        return False'''

_p306 = S.load("p306")


def _add_ref(num):
    n = len(num)

    def ok(t):
        return t == "0" or t[0] != "0"

    def go(k, seq):
        if k == n:
            return len(seq) >= 3
        for e in range(k + 1, n + 1):
            t = num[k:e]
            if not ok(t):
                break
            v = int(t)
            if len(seq) >= 2 and v != seq[-1] + seq[-2]:
                continue
            if go(e, seq + [v]):
                return True
        return False
    return go(0, [])


for s, want in [("112358", True), ("199100199", True), ("1023", False), ("101", True), ("000", True), ("0235813", False), ("123", True), ("12", False)]:
    assert _p306.isAdditiveNumber(s) == want, s
for _ in range(1500):
    if random.random() < 0.5:
        a, b = random.randrange(0, 30), random.randrange(0, 30)
        s = str(a) + str(b)
        for _ in range(random.randrange(1, 4)):
            a, b = b, a + b
            s += str(b)
        if random.random() < 0.3:
            s += str(random.randrange(10))
    else:
        s = "".join(random.choice("0112358") for _ in range(random.randrange(1, 10)))
    assert _p306.isAdditiveNumber(s) == _add_ref(s), s
print("P306 OK")

emit({
 "num": 306, "slug": "additive-number",
 "en": [
   "An <strong>additive number</strong> is a string whose digits can form an <strong>additive sequence</strong>.",
   "A valid <strong>additive sequence</strong> should contain <strong>at least</strong> three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.",
   "Given a string containing only digits, return <code>true</code> if it is an <strong>additive number</strong> or <code>false</code> otherwise.",
   "<strong>Note:</strong> Numbers in the additive sequence <strong>cannot</strong> have leading zeros, so sequence <code>1, 2, 03</code> or <code>1, 02, 3</code> is invalid.",
   "<strong>Follow up:</strong> How would you handle overflow for very large input integers?",
 ],
 "zh": [
   "<strong>累加數</strong>：字串的數字可以切成一個<strong>累加序列</strong>——至少三個數，而且從第三個數開始，每個數都等於前兩個數的和。",
   "給你一個只含數字的字串，判斷它是不是累加數。",
   "<strong>注意：</strong>序列中的數<strong>不能有前導零</strong>，例如 <code>1, 2, 03</code> 或 <code>1, 02, 3</code> 都不合法（但單獨的 <code>0</code> 可以）。",
   "<strong>進階：</strong>輸入的整數非常大時，如何處理溢位？",
 ],
 "examples": """範例 1
  輸入："112358"
  輸出：true
  說明：1, 1, 2, 3, 5, 8

範例 2
  輸入："199100199"
  輸出：true
  說明：1, 99, 100, 199""",
 "constraints": [
   "1 ≤ <code>num.length</code> ≤ 35",
   "<code>num</code> 只包含數字",
 ],
 "idea": [
   ("c", """【前兩個數決定一切】
    一旦選定第一個數 a、第二個數 b，
    第三個數一定是 a + b，第四個是 b + (a+b) ……
    整個序列唯一確定，只要檢查字串是否剛好是這個序列。

【所以只要枚舉前兩個數的切點】
    第一個數：num[:i]
    第二個數：num[i:j]
    O(n²) 種組合，每種驗證 O(n) -> O(n³)，n ≤ 35 很快。

【前導零】
    "0" 可以，"03" 不行：
    num[0] == '0' 時，第一個數只能是 "0"；第二個數同理。

【至少三個數】
    驗證時要確定真的有第三個數（k > j）。

【溢位】
    35 位數超過 64 位元整數。Python 的 int 沒有上限；
    其他語言要用字串模擬大數加法。"""),
 ],
 "approaches": [
   ap("解法", "枚舉前兩個數 + 驗證", [
     ("c", S["p306"]),
     "<code>num.startswith(c, k)</code>：從位置 k 開始是否以字串 c 開頭，不用切片。",
   ], "O(n³)", "O(n)", "", "數字的字串", optimal=True),
 ],
 "edges": [
   "<strong>\"000\"</strong> → 0, 0, 0 合法，true。",
   "<strong>\"1023\"</strong> → 1, 02, 3 有前導零，false。",
   "<strong>\"101\"</strong> → 1, 0, 1，true。",
   "<strong>長度 &lt; 3</strong> → 不可能有三個數，false。",
 ],
 "follow": [
   ("h", "相關題"),
   ("c", "第 842 題「將陣列拆分成費氏序列」：同一個想法，但要回傳切出來的序列，而且每個數都要在 32 位元範圍內——超過就剪枝。"),
 ],
 "related": [
   "<strong>第 842 題 將陣列拆分成費氏序列</strong>",
   "<strong>第 93 題 復原 IP 位址</strong> —— 另一題切字串",
 ],
 "check": [
   "為什麼只要枚舉前兩個數？",
   "前導零的規則要怎麼實作？",
   "大數要怎麼處理？",
 ],
})


# ==================== 307. Range Sum Query - Mutable ====================
S["p307_bit"] = '''class NumArray:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)            # 樹狀陣列（1-indexed）
        for i, x in enumerate(nums):
            self._add(i + 1, x)

    def _add(self, i: int, delta: int) -> None:
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i                            # ★ 往上：加上 lowbit

    def _prefix(self, i: int) -> int:              # nums[0..i-1] 的和
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i                            # ★ 往下：減去 lowbit
        return s

    def update(self, index: int, val: int) -> None:
        self._add(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self._prefix(right + 1) - self._prefix(left)'''

S["p307_seg"] = '''class NumArray:
    def __init__(self, nums: List[int]):
        self.n = n = len(nums)
        self.t = [0] * (2 * n)                    # 迭代式線段樹：葉子在 t[n..2n-1]
        self.t[n:] = nums
        for i in range(n - 1, 0, -1):
            self.t[i] = self.t[2 * i] + self.t[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        i = index + self.n
        self.t[i] = val
        while i > 1:                               # 一路更新到根
            i //= 2
            self.t[i] = self.t[2 * i] + self.t[2 * i + 1]

    def sumRange(self, left: int, right: int) -> int:
        l, r = left + self.n, right + self.n + 1   # 半開區間 [l, r)
        s = 0
        while l < r:
            if l & 1:                              # l 是右孩子：自己算進去，往右移
                s += self.t[l]
                l += 1
            if r & 1:                              # r 是右孩子：左邊的兄弟算進去
                r -= 1
                s += self.t[r]
            l //= 2
            r //= 2
        return s'''

S["p307_sqrt"] = '''class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums[:]
        self.B = max(1, int(len(nums) ** 0.5))     # 每塊大小約 √n
        self.block = [0] * ((len(nums) + self.B - 1) // self.B)
        for i, x in enumerate(nums):
            self.block[i // self.B] += x

    def update(self, index: int, val: int) -> None:
        self.block[index // self.B] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        bl, br = left // self.B, right // self.B
        if bl == br:
            return sum(self.nums[left:right + 1])
        return (sum(self.nums[left:(bl + 1) * self.B])      # 左邊零頭
                + sum(self.block[bl + 1:br])                  # 中間整塊
                + sum(self.nums[br * self.B:right + 1]))      # 右邊零頭'''

for key in ("p307_bit", "p307_seg", "p307_sqrt"):
    cls = S.loadns(key)["NumArray"]
    for _ in range(300):
        nums = [random.randint(-9, 9) for _ in range(random.randrange(1, 20))]
        na, ref = cls(nums), nums[:]
        for _ in range(30):
            if random.random() < 0.4:
                i, v = random.randrange(len(ref)), random.randint(-9, 9)
                na.update(i, v)
                ref[i] = v
            else:
                l = random.randrange(len(ref)); r = random.randrange(l, len(ref))
                assert na.sumRange(l, r) == sum(ref[l:r + 1]), key
print("P307 OK")

_P307_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">樹狀陣列：tree[i] 管理「以 i 結尾、長度為 lowbit(i)」的一段</text>
            <g font-size="11" text-anchor="middle">
              <text x="30" y="210" fill="var(--text-muted)">i</text>
              <text x="70" y="210" fill="var(--text)">1</text><text x="120" y="210" fill="var(--text)">2</text><text x="170" y="210" fill="var(--text)">3</text><text x="220" y="210" fill="var(--text)">4</text>
              <text x="270" y="210" fill="var(--text)">5</text><text x="320" y="210" fill="var(--text)">6</text><text x="370" y="210" fill="var(--text)">7</text><text x="420" y="210" fill="var(--text)">8</text>
            </g>
            <g fill="none" stroke-width="2">
              <line x1="52" y1="186" x2="88" y2="186" stroke="var(--accent)"/>
              <line x1="152" y1="186" x2="188" y2="186" stroke="var(--accent)"/>
              <line x1="252" y1="186" x2="288" y2="186" stroke="var(--accent)"/>
              <line x1="352" y1="186" x2="388" y2="186" stroke="var(--accent)"/>
              <line x1="52" y1="156" x2="138" y2="156" stroke="var(--gold)"/>
              <line x1="252" y1="156" x2="338" y2="156" stroke="var(--gold)"/>
              <line x1="52" y1="126" x2="238" y2="126" stroke="#ff8a65"/>
              <line x1="52" y1="96" x2="438" y2="96" stroke="#8e7cc3"/>
            </g>
            <g font-size="11">
              <text x="92" y="182" fill="var(--accent)">t1</text><text x="192" y="182" fill="var(--accent)">t3</text><text x="292" y="182" fill="var(--accent)">t5</text><text x="392" y="182" fill="var(--accent)">t7</text>
              <text x="142" y="152" fill="var(--gold)">t2</text><text x="342" y="152" fill="var(--gold)">t6</text>
              <text x="242" y="122" fill="#ff8a65">t4</text><text x="442" y="92" fill="#8e7cc3">t8</text>
            </g>
            <text x="480" y="120" fill="var(--text)" font-size="12">前綴和(7)</text>
            <text x="480" y="140" fill="var(--text-muted)" font-size="12">= t7 + t6 + t4</text>
            <text x="480" y="160" fill="var(--text-muted)" font-size="12">7 → 6 → 4 → 0</text>
            <text x="480" y="180" fill="var(--text-muted)" font-size="12">（每次減 lowbit）</text>
            <text x="20" y="244" fill="var(--text)" font-size="12">更新位置 3：3 → 4 → 8（每次加 lowbit），只動到涵蓋位置 3 的 t3、t4、t8。都是 O(log n) 步。</text>'''

emit({
 "num": 307, "slug": "range-sum-query-mutable",
 "en": [
   "Given an integer array <code>nums</code>, handle multiple queries of the following types:",
   ("ol", ["<strong>Update</strong> the value of an element in <code>nums</code>.",
           "Calculate the <strong>sum</strong> of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> <strong>inclusive</strong> where <code>left &lt;= right</code>."]),
   "Implement the <code>NumArray</code> class:",
   ("ul", ["<code>NumArray(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.",
           "<code>void update(int index, int val)</code> <strong>Updates</strong> the value of <code>nums[index]</code> to be <code>val</code>.",
           "<code>int sumRange(int left, int right)</code> Returns the <strong>sum</strong> of the elements of <code>nums</code> between indices <code>left</code> and <code>right</code> <strong>inclusive</strong>."]),
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，要處理兩種操作：",
   ("ol", ["<code>update(index, val)</code>：把 <code>nums[index]</code> 改成 <code>val</code>。",
           "<code>sumRange(left, right)</code>：回傳索引 <code>left</code> 到 <code>right</code>（包含）的總和。"]),
 ],
 "examples": """範例
  輸入：["NumArray", "sumRange", "update", "sumRange"]
        [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
  輸出：[null, 9, null, 8]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 3 × 10⁴",
   "−100 ≤ <code>nums[i]</code> ≤ 100",
   "0 ≤ <code>index</code> &lt; <code>nums.length</code>，−100 ≤ <code>val</code> ≤ 100",
   "0 ≤ <code>left ≤ right</code> &lt; <code>nums.length</code>",
   "<code>update</code> 與 <code>sumRange</code> 最多共呼叫 3 × 10⁴ 次",
 ],
 "idea": [
   ("c", """【兩種極端】
    直接存陣列：update O(1)，sumRange O(n)
    前綴和：    update O(n)，sumRange O(1)
    都可能被卡成 O(n) × 3·10⁴ 次。

【要兩種操作都快 -> O(log n) 的資料結構】

【樹狀陣列（Binary Indexed Tree / Fenwick Tree）】
    tree[i] 存「以 i 結尾、長度為 lowbit(i)」的區段和。
    lowbit(i) = i & -i（i 最低位的 1）
        查前綴和：i 一直減 lowbit，把沿路的 tree[i] 加起來
        單點更新：i 一直加 lowbit，把沿路的 tree[i] 都更新
    兩者都是 O(log n)，程式只有幾行。

【線段樹】
    每個節點存一個區間的和，
    區間查詢拆成 O(log n) 個節點，更新沿路到根 O(log n)。
    比樹狀陣列通用（可以求 max、min、做區間修改）。

【分塊（√n 分解）】
    切成 √n 塊，每塊存總和。
    更新 O(1)，查詢 O(√n)。概念最簡單。"""),
   ("fig", _P307_FIG, "0 0 640 258"),
 ],
 "approaches": [
   ap("解法一", "分塊", [
     ("c", S["p307_sqrt"]),
   ], "update O(1)，sumRange O(√n)", "O(n)", "", ""),

   ap("解法二", "線段樹（迭代版）", [
     ("c", S["p307_seg"]),
     ("c", """【陣列表示】
    節點 i 的孩子是 2i、2i+1；葉子放在 t[n .. 2n-1]。
    這個「由下往上」的寫法不需要遞迴，
    而且 n 不是 2 的冪次也成立。"""),
   ], "O(log n)", "O(n)", "", ""),

   ap("解法三", "樹狀陣列", [
     ("c", S["p307_bit"]),
     ("c", """【為什麼加減 lowbit 就能走到正確的位置？】
    查詢：i 減掉最低位的 1 -> 跳到「上一段的結尾」
          例如 7 (111) -> 6 (110) -> 4 (100) -> 0
          t7 管 [7]，t6 管 [5,6]，t4 管 [1..4]，剛好拼成 [1..7]
    更新：i 加上最低位的 1 -> 跳到「下一個涵蓋 i 的區段」
          例如 3 (011) -> 4 (100) -> 8 (1000)"""),
   ], "O(log n)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "update", "sumRange", "備註"],
   [["前綴和", "O(n)", "O(1)", "修改太慢"],
    ["一、分塊", "O(1)", "O(√n)", "概念簡單"],
    ["二、線段樹", "O(log n)", "O(log n)", "最通用"],
    ["三、樹狀陣列", "O(log n)", "O(log n)", "最短 ✔"]]),
 "edges": [
   "<strong>更新成相同的值</strong> → delta = 0，沒有影響。",
   "<strong>樹狀陣列是 1-indexed</strong> → 題目的 index 要 +1。",
   "<strong>只有一個元素</strong> → 所有結構都要能處理 n = 1。",
 ],
 "follow": [
   ("h", "樹狀陣列的其他用途"),
   ("c", "計算逆序數（第 315、493 題）：由右往左掃，把值當索引加 1，查詢「比我小的有幾個」。這時樹狀陣列的索引是「值」而不是「位置」，常常需要先做座標壓縮。"),
 ],
 "related": [
   "<strong>第 303 題 區域和檢索 - 陣列不可變</strong>",
   "<strong>第 315 題 計算右側小於當前元素的個數</strong> —— 樹狀陣列",
   "<strong>第 327 題 區間和的個數</strong>",
   "<strong>第 699 題 掉落的方塊</strong> —— 線段樹",
 ],
 "check": [
   "為什麼前綴和不適合這一題？",
   "lowbit(i) 是什麼？樹狀陣列的 tree[i] 管理哪一段？",
   "查詢和更新時，i 分別怎麼移動？",
   "線段樹比樹狀陣列多了什麼能力？",
 ],
})


# ==================== 309. Best Time to Buy and Sell Stock with Cooldown ====================
S["p309"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -float("inf")    # 今天結束時「持有股票」的最大收益
        sold = 0                # 今天剛賣出（明天是冷凍期）
        rest = 0                # 今天結束時「不持有、也不在冷凍期」
        for p in prices:
            # ★ 三個狀態同時轉移（右邊都用昨天的值）
            hold, sold, rest = (
                max(hold, rest - p),     # 繼續持有，或從「可以買」的狀態買入
                hold + p,                # 賣出
                max(rest, sold),         # 繼續休息，或昨天賣的今天解凍
            )
        return max(sold, rest)'''

S["p309_dp"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # buy[i]：第 i 天結束時持有；sell[i]：第 i 天結束時不持有
        buy, sell = [0] * n, [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            # 買入前一天不能是「賣出日」-> 從 sell[i-2] 買
            buy[i] = max(buy[i - 1], (sell[i - 2] if i >= 2 else 0) - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
        return sell[-1]'''

_p309 = [S.load(x) for x in ("p309", "p309_dp")]


def _cd_ref(pr):
    import functools

    @functools.lru_cache(None)
    def f(i, holding):
        if i >= len(pr):
            return 0
        best = f(i + 1, holding)
        if holding:
            best = max(best, pr[i] + f(i + 2, False))
        else:
            best = max(best, -pr[i] + f(i + 1, True))
        return best
    return f(0, False)


for pr, want in [([1, 2, 3, 0, 2], 3), ([1], 0), ([2, 1], 0), ([1, 2, 4], 3)]:
    for sol in _p309:
        assert sol.maxProfit(pr) == want
for _ in range(3000):
    pr = [random.randrange(0, 10) for _ in range(random.randrange(1, 12))]
    want = _cd_ref(pr)
    for sol in _p309:
        assert sol.maxProfit(pr) == want, pr
print("P309 OK")

_P309_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">三個狀態的狀態機（每天結束時處於哪個狀態）</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="120" cy="120" r="38" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="120" y="118" fill="var(--accent)">hold</text><text x="120" y="136" fill="var(--text-muted)" font-size="10">持有</text>
              <circle cx="330" cy="70" r="38" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="330" y="68" fill="#ff8a65">sold</text><text x="330" y="86" fill="var(--text-muted)" font-size="10">剛賣出</text>
              <circle cx="330" cy="190" r="38" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="330" y="188" fill="var(--gold)">rest</text><text x="330" y="206" fill="var(--text-muted)" font-size="10">空手可買</text>
            </g>
            <g stroke="var(--text-muted)" fill="none">
              <path d="M156 106 L292 78"/><path d="M330 108 L330 152"/><path d="M292 180 L158 132"/>
              <path d="M90 96 C 60 60, 110 50, 112 82"/>
              <path d="M360 214 C 400 250, 400 170, 366 180"/>
            </g>
            <g fill="var(--text-muted)">
              <polygon points="292,78 282,76 285,85"/><polygon points="330,152 325,142 335,142"/><polygon points="158,132 166,127 163,138"/>
              <polygon points="112,82 107,74 117,74"/><polygon points="366,180 376,176 373,186"/>
            </g>
            <g font-size="12">
              <text x="200" y="80" fill="var(--text)">賣出 +p</text>
              <text x="340" y="134" fill="var(--text)">冷凍一天</text>
              <text x="190" y="176" fill="var(--text)">買入 −p</text>
              <text x="40" y="54" fill="var(--text-muted)">繼續持有</text>
              <text x="400" y="220" fill="var(--text-muted)">繼續休息</text>
            </g>
            <text x="440" y="70" fill="#ff8a65" font-size="12">sold 不能直接買</text>
            <text x="440" y="90" fill="#ff8a65" font-size="12">→ 這就是冷凍期</text>'''

emit({
 "num": 309, "slug": "best-time-to-buy-and-sell-stock-with-cooldown",
 "en": [
   "You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.",
   "Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:",
   ("ul", ["After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day)."]),
   "<strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).",
 ],
 "zh": [
   "給你陣列 <code>prices</code>，<code>prices[i]</code> 是股票第 <code>i</code> 天的價格。",
   "可以進行任意多次交易，但有限制：",
   ("ul", ["賣出股票之後，<strong>隔天不能買入</strong>（冷凍期一天）。"]),
   "同一時間最多只能持有一股（必須先賣再買）。",
 ],
 "examples": """範例 1
  輸入：prices = [1,2,3,0,2]
  輸出：3
  說明：買、賣、冷凍、買、賣 -> (2-1) + (2-0) = 3

範例 2
  輸入：prices = [1]
  輸出：0""",
 "constraints": [
   "1 ≤ <code>prices.length</code> ≤ 5000",
   "0 ≤ <code>prices[i]</code> ≤ 1000",
 ],
 "idea": [
   ("fig", _P309_FIG, "0 0 640 250"),
   ("c", """【股票系列的通用方法：狀態機 DP】
    每天結束時處於某個「狀態」，列出狀態之間怎麼轉移。

【三個狀態】
    hold：手上有股票
    sold：今天剛賣掉（明天冷凍，不能買）
    rest：手上沒股票，而且明天可以買

【轉移】
    hold 今天 = max(昨天 hold 繼續持有, 昨天 rest 今天買入 − p)
    sold 今天 = 昨天 hold 今天賣出 + p
    rest 今天 = max(昨天 rest 繼續休息, 昨天 sold 今天解凍)

    注意：買入只能從 rest 來，不能從 sold 來 —— 這就是冷凍期。

【答案】
    最後一天不能持有股票：max(sold, rest)

【初始】
    第 0 天之前：hold = −∞（不可能持有），sold = rest = 0"""),
 ],
 "approaches": [
   ap("解法一", "兩個陣列：buy / sell", [
     ("c", S["p309_dp"]),
     "冷凍期的效果：買入時要從「前天就不持有」的狀態 sell[i−2] 轉移，而不是 sell[i−1]。",
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "三狀態機（O(1) 空間）", [
     ("c", S["p309"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、兩個陣列", "O(n)", "O(n)"],
    ["二、狀態機", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>只有一天</strong> → 0。",
   "<strong>價格一直下跌</strong> → 0，不交易。",
   "<strong>三個狀態同時更新</strong> → 右邊都要用「昨天」的值；Python 的多重賦值自然做到。",
 ],
 "follow": [
   ("h", "股票系列整理"),
   ("c", """第 121 題：只能交易一次。
第 122 題：無限次。
第 123 題：最多兩次（四個狀態）。
第 188 題：最多 k 次（2k 個狀態）。
第 309 題：無限次 + 冷凍期（本題，三個狀態）。
第 714 題：無限次 + 手續費（兩個狀態，賣出時扣費）。
全部都是同一個狀態機框架。"""),
 ],
 "related": [
   "<strong>第 122 題 買賣股票的最佳時機 II</strong>",
   "<strong>第 714 題 買賣股票的最佳時機含手續費</strong>",
   "<strong>第 188 題 買賣股票的最佳時機 IV</strong>",
 ],
 "check": [
   "三個狀態分別代表什麼？",
   "冷凍期在轉移式中怎麼體現？",
   "為什麼答案是 max(sold, rest)？",
 ],
})
