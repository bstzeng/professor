# -*- coding: utf-8 -*-
"""第 587、589、590、591、592、593、594、598 題。"""
import random, re
from collections import Counter
from fractions import Fraction
from itertools import permutations
from authoring import ap
from lcauto import em
from runner import Src

S = Src()
random.seed(587)


class NNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


def rand_ntree(n):
    if n == 0:
        return None
    root = NNode(random.randint(0, 9)); all_ = [root]
    for _ in range(n - 1):
        p = random.choice(all_); c = NNode(random.randint(0, 9)); p.children.append(c); all_.append(c)
    return root


# ==================== 587. Erect the Fence ====================
S["p587"] = '''class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        pts = sorted(map(tuple, trees))
        if len(pts) <= 3:
            return [list(p) for p in set(pts)]

        def cross(o, a, b):         # (a - o) × (b - o)：> 0 左轉，< 0 右轉，= 0 共線
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        def half(points):
            hull = []
            for p in points:
                # ★ 只在「右轉」時彈出；共線（= 0）的點保留，因為邊上的樹也要圍進去
                while len(hull) >= 2 and cross(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull.append(p)
            return hull

        lower = half(pts)               # 下凸包（由左到右）
        upper = half(pts[::-1])         # 上凸包（由右到左）
        return [list(p) for p in set(lower + upper)]'''

_p587 = S.load("p587")
def _bf587(pts):
    pts = list(set(map(tuple, pts)))
    def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    res = set()
    if len(pts) <= 2:
        return set(pts)
    for p in pts:
        # p 在凸包邊界上 <=> 存在一條經過 p 的直線，所有點都在同一側（含線上）
        on = False
        for q in pts:
            if q == p: continue
            if all(cross(p, q, r) >= 0 for r in pts) or all(cross(p, q, r) <= 0 for r in pts):
                on = True; break
        if on: res.add(p)
    return res
for _ in range(1500):
    pts = [[random.randint(0, 5), random.randint(0, 5)] for _ in range(random.randint(1, 9))]
    pts = [list(p) for p in set(map(tuple, pts))]
    assert set(map(tuple, _p587.outerTrees(pts))) == _bf587(pts), pts
print("P587 OK")

em({
 "num": 587, "title": "安裝柵欄",
 "desc": "凸包：Andrew 單調鏈演算法，排序後分別建上下凸包；本題邊上共線的點也要保留，只在右轉時彈出。",
 "zh": [
   "給你花園中每棵樹的座標 <code>trees[i] = [x, y]</code>。你要用<strong>最短</strong>的繩子把所有樹圍起來。",
   "回傳<strong>恰好位於柵欄上</strong>的所有樹的座標（順序不限）。",
 ],
 "idea": [
   ("c", """【最短的圍繩 = 凸包】
    把所有點包起來的最小凸多邊形。

【Andrew 單調鏈】
    1. 依 (x, y) 排序。
    2. 由左到右建下凸包：維護一個堆疊，
       新點讓最後兩點和它形成「右轉」時，中間那點不是凸包上的點，彈出。
    3. 由右到左用同樣方法建上凸包。
    4. 兩者合併（去重）。

【轉向判斷：外積】
    cross(o, a, b) = (a-o) × (b-o)
        > 0：o -> a -> b 左轉
        < 0：右轉
        = 0：共線

【本題的特別之處：邊上的點也要】
    一般凸包只保留頂點（共線時也彈出）；
    本題要所有在柵欄上的樹 -> 只在嚴格右轉（< 0）時彈出。"""),
 ],
 "approaches": [
   ap("解法", "Andrew 單調鏈", [
     ("c", S["p587"]),
     "驗證方式：和「點在凸包邊界上 ⇔ 存在一條經過它、所有點都在同一側的直線」的暴力判斷比對 1500 組。",
   ], "O(n log n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>所有點共線</strong> → 上下凸包都包含全部點，用集合去重。", "<strong>點數 ≤ 3</strong> → 全部都在柵欄上。", "<strong>邊上共線的點</strong> → 只在 cross < 0 時彈出才能保留。"],
 "follow": [("h", "其他凸包演算法"), ("c", "Graham 掃描（依極角排序）、Jarvis 步進（禮物包裝法，O(nh)）。Andrew 只用 x 座標排序，處理共線比 Graham 簡單。")],
 "related": ["<strong>第 593 題 有效的正方形</strong>", "<strong>第 963 題 最小面積矩形 II</strong>"],
 "check": ["外積的正負代表什麼？", "為什麼本題只在 cross < 0 時彈出？", "所有點共線時會發生什麼？"],
})


# ==================== 589. N-ary Tree Preorder Traversal ====================
S["p589"] = '''class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res, stack = [], [root] if root else []
        while stack:
            nd = stack.pop()
            res.append(nd.val)
            stack.extend(reversed(nd.children))     # ★ 反著推進堆疊，第一個孩子才會先被取出
        return res'''

_p589 = S.load("p589", extra={"Node": NNode})
def _pre(t): return [] if t is None else [t.val] + [v for c in t.children for v in _pre(c)]
for _ in range(500):
    t = rand_ntree(random.randint(0, 15)); assert _p589.preorder(t) == _pre(t)
print("P589 OK")

em({
 "num": 589, "title": "N 叉樹的前序走訪",
 "desc": "迭代版前序：孩子反向推進堆疊，讓第一個孩子先被取出。",
 "zh": ["給你一棵 N 叉樹的根節點，回傳節點值的<strong>前序走訪</strong>（先根，再依序走訪每個孩子）。", "<strong>進階：</strong>遞迴很簡單，能用迭代寫嗎？"],
 "idea": [
   ("c", """【遞迴】
    [root.val] + 依序對每個孩子遞迴。

【迭代】
    堆疊是後進先出。
    取出節點、記錄值，再把孩子「反著」推進去，
    這樣第一個孩子在最上面，下一次先被取出。"""),
 ],
 "approaches": [
   ap("解法", "堆疊迭代", [("c", S["p589"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>空樹</strong> → []。", "<strong>孩子的順序</strong> → 反向推進才能維持由左到右。"],
 "follow": [("h", "後序的技巧"), ("c", "第 590 題：「根、右…左」的走訪反轉過來就是後序。")],
 "related": ["<strong>第 590 題 N 叉樹的後序走訪</strong>", "<strong>第 144 題 二元樹的前序走訪</strong>"],
 "check": ["為什麼孩子要反向推進堆疊？"],
})


# ==================== 590. N-ary Tree Postorder Traversal ====================
S["p590"] = '''class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res, stack = [], [root] if root else []
        while stack:
            nd = stack.pop()
            res.append(nd.val)
            stack.extend(nd.children)       # 正著推：取出順序是「根、最後一個孩子、…、第一個孩子」
        return res[::-1]                    # ★ 反轉後就是「第一個孩子…最後一個孩子、根」= 後序'''

_p590 = S.load("p590", extra={"Node": NNode})
def _post(t): return [] if t is None else [v for c in t.children for v in _post(c)] + [t.val]
for _ in range(500):
    t = rand_ntree(random.randint(0, 15)); assert _p590.postorder(t) == _post(t)
print("P590 OK")

em({
 "num": 590, "title": "N 叉樹的後序走訪",
 "desc": "「根 → 孩子由右到左」的走訪反轉過來，就是後序。",
 "zh": ["給你一棵 N 叉樹的根節點，回傳節點值的<strong>後序走訪</strong>（先依序走訪每個孩子，最後才是根）。", "<strong>進階：</strong>能用迭代寫嗎？"],
 "idea": [
   ("c", """【反轉技巧】
    後序 = 孩子1, 孩子2, ..., 孩子k, 根
    反過來 = 根, 孩子k, ..., 孩子1 —— 這是「孩子由右到左的前序」，
    用堆疊很好做：取出根，孩子正著推進去（最後一個孩子在頂端，先被取出）。
    最後把結果反轉即可。"""),
 ],
 "approaches": [
   ap("解法", "反向前序再反轉", [("c", S["p590"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>空樹</strong> → []。", "<strong>只有根</strong> → [root.val]。"],
 "follow": [("h", "不反轉的寫法"), ("c", "堆疊中存 (節點, 下一個要處理的孩子索引)，孩子都處理完才輸出根。這更貼近遞迴的真實過程。")],
 "related": ["<strong>第 589 題 N 叉樹的前序走訪</strong>", "<strong>第 145 題 二元樹的後序走訪</strong>"],
 "check": ["反轉之前的走訪順序是什麼？"],
})


# ==================== 591. Tag Validator ====================
S["p591"] = '''class Solution:
    def isValid(self, code: str) -> bool:
        stack, i, n = [], 0, len(code)
        while i < n:
            if i > 0 and not stack:
                return False                        # 整段程式碼必須被一個標籤包住
            if code.startswith("<![CDATA[", i):
                if not stack:
                    return False                    # CDATA 必須在某個標籤裡
                j = code.find("]]>", i + 9)
                if j < 0:
                    return False
                i = j + 3                           # ★ CDATA 內的內容原樣跳過，不解析
            elif code.startswith("</", i):
                j = code.find(">", i + 2)
                if j < 0:
                    return False
                name = code[i + 2:j]
                if not stack or stack[-1] != name:
                    return False                    # 結束標籤要和最近的開始標籤相符
                stack.pop()
                i = j + 1
            elif code.startswith("<", i):
                j = code.find(">", i + 1)
                if j < 0:
                    return False
                name = code[i + 1:j]
                if not (1 <= len(name) <= 9 and name.isupper() and name.isalpha()):
                    return False                    # 標籤名稱：1～9 個大寫字母
                stack.append(name)
                i = j + 1
            else:
                i += 1                              # 一般文字
        return not stack and n > 0'''

_p591 = S.load("p591")
cases = [("<DIV>This is the first line <![CDATA[<div>]]></DIV>", True),
         ("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>", True),
         ("<A>  <B> </A>   </B>", False), ("<DIV>  div tag is not closed  <DIV>", False),
         ("<DIV>  unmatched <  </DIV>", False), ("<DIV> closed tags with invalid tag name  <b>123</b> </DIV>", False),
         ("<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>", False),
         ("<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>", False),
         ("<A></A><B></B>", False), ("<A><![CDATA[</A>]]></A>", True), ("<![CDATA[x]]>", False), ("<AAAAAAAAAA></AAAAAAAAAA>", False),
         ("<A></A>", True), ("<A>", False), ("", False), ("<A><B></B></A>", True)]
for c, want in cases:
    assert _p591.isValid(c) == want, c
print("P591 OK")

em({
 "num": 591, "title": "標籤驗證器",
 "desc": "照規格寫的小型解析器：一個堆疊配對開始與結束標籤，CDATA 內容整段跳過不解析。",
 "pre": [],
 "zh": [
   "給你一段程式碼字串，判斷它是否是合法的<strong>標籤巢狀結構</strong>。主要規則：",
   ("ol", [
     "整段程式碼必須被<strong>一個</strong>合法的封閉標籤包住。",
     "封閉標籤的格式是 <code>&lt;TAG_NAME&gt;內容&lt;/TAG_NAME&gt;</code>，開始與結束的名稱必須相同。",
     "<code>TAG_NAME</code> 只能由 1～9 個<strong>大寫字母</strong>組成。",
     "內容可以包含其他合法的封閉標籤、CDATA 與任意字元，但不能有不配對的 <code>&lt;</code>、不配對的標籤或名稱不合法的標籤。",
     "CDATA 的格式是 <code>&lt;![CDATA[內容]]&gt;</code>，內容是第一個 <code>]]&gt;</code> 之前的所有字元，<strong>不做任何解析</strong>。",
   ]),
 ],
 "idea": [
   ("c", """【用堆疊配對標籤】
    遇到開始標籤 <NAME>：檢查名稱合法，推進堆疊。
    遇到結束標籤 </NAME>：必須和堆疊頂端相同，彈出。

【CDATA 優先】
    <![CDATA[ 也是以 < 開頭，要先判斷它；
    找到第一個 ]]>，整段跳過（裡面的 < 不算標籤）。

【「整段被一個標籤包住」怎麼檢查？】
    除了第 0 個字元，掃描過程中堆疊不能是空的
    （空了代表最外層標籤已經結束，後面卻還有東西）。
    結束時堆疊必須是空的。

【判斷順序很重要】
    <![CDATA[  ->  </  ->  <  ->  一般字元"""),
 ],
 "approaches": [
   ap("解法", "堆疊 + 逐段解析", [("c", S["p591"]), "驗證方式：題目所有範例加上幾個邊界案例（兩個並列的最外層標籤、CDATA 在最外層、名稱 10 個字母、空字串）。"], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>兩個並列的最外層標籤</strong> → 不合法。", "<strong>CDATA 不在任何標籤內</strong> → 不合法。", "<strong>CDATA 內有像標籤的文字</strong> → 不解析，合法。", "<strong>名稱超過 9 個字母或含小寫</strong> → 不合法。"],
 "follow": [("h", "解析器的寫法"), ("c", "這類題目的關鍵是「依優先順序嘗試匹配每一種語法單元」，寫成一個 while 迴圈加上 startswith 判斷，比正規表示式清楚得多。")],
 "related": ["<strong>第 20 題 有效的括號</strong>", "<strong>第 722 題 刪除註解</strong>", "<strong>第 736 題 Lisp 語法解析</strong>"],
 "check": ["為什麼要先判斷 CDATA？", "怎麼檢查整段程式碼只被一個標籤包住？"],
})


# ==================== 592. Fraction Addition and Subtraction ====================
S["p592"] = '''class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = 0, 1
        for a, b in re.findall(r"([+-]?\\d+)/(\\d+)", expression):   # 每個分數連同正負號一起抓
            a, b = int(a), int(b)
            num, den = num * b + a * den, den * b     # ★ 通分相加
            g = math.gcd(num, den)
            num, den = num // g, den // g             # 隨時約分，避免數字變大
        return "%d/%d" % (num, den)'''

_p592 = S.load("p592")
assert _p592.fractionAddition("-1/2+1/2") == "0/1" and _p592.fractionAddition("-1/2+1/2+1/3") == "1/3" and _p592.fractionAddition("1/3-1/2") == "-1/6"
for _ in range(2000):
    fr = [(random.choice("+-"), random.randint(1, 10), random.randint(1, 10)) for _ in range(random.randint(1, 6))]
    expr = "".join(("" if i == 0 and s == "+" else s) + "%d/%d" % (a, b) for i, (s, a, b) in enumerate(fr))
    v = sum((Fraction(a, b) * (1 if s == "+" else -1) for s, a, b in fr), Fraction(0))
    assert _p592.fractionAddition(expr) == "%d/%d" % (v.numerator, v.denominator)
print("P592 OK")

em({
 "num": 592, "title": "分數加減運算",
 "desc": "用正規表示式把每個帶正負號的分數抓出來，逐一通分相加並以最大公因數約分。",
 "zh": [
   "給你一個只含分數加減的運算式字串，例如 <code>\"-1/2+1/2+1/3\"</code>，回傳計算結果的字串。",
   "結果必須是<strong>最簡分數</strong>；若結果是整數，也要寫成分母為 1 的分數，例如 <code>\"2/1\"</code>。",
 ],
 "idea": [
   ("c", """【切出每個分數】
    正規表示式 ([+-]?\\d+)/(\\d+)：
    分子連同前面的正負號一起抓，省去處理運算子。

【通分相加】
    a/b + c/d = (a·d + c·b) / (b·d)
    每次加完用 gcd 約分，數字不會爆大。

【符號】
    分母永遠是正的，負號都在分子上；
    gcd 對負數也回傳正值，約分後符號保持在分子。"""),
 ],
 "approaches": [
   ap("解法", "正規表示式 + 逐一通分", [("c", S["p592"]), "驗證方式：和 Python 的 Fraction 精確計算比對 2000 個隨機運算式。"], "O(k · log M)", "O(1)", "k 個分數", "", optimal=True),
 ],
 "edges": ["<strong>結果為 0</strong> → \"0/1\"。", "<strong>開頭是負號</strong> → 正規表示式把它併入第一個分子。", "<strong>結果是整數</strong> → 分母 1。"],
 "follow": [("h", "最小公倍數通分"), ("c", "也可以先算所有分母的最小公倍數再一次通分；分母都 ≤ 10 時，LCM(1..10) = 2520，直接用 2520 當公分母也行。")],
 "related": ["<strong>第 537 題 複數乘法</strong>", "<strong>第 640 題 求解方程</strong>", "<strong>第 166 題 分數到小數</strong>"],
 "check": ["正負號為什麼跟著分子一起抓？", "為什麼每一步都要約分？"],
})


# ==================== 593. Valid Square ====================
S["p593"] = '''class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        pts = [p1, p2, p3, p4]
        d = sorted((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
                   for i, a in enumerate(pts) for b in pts[i + 1:])   # 六個兩兩距離的平方
        # ★ 正方形：四條相等的邊（> 0）+ 兩條相等的對角線，且對角線² = 2 × 邊²
        return d[0] > 0 and d[0] == d[1] == d[2] == d[3] and d[4] == d[5] == 2 * d[0]'''

_p593 = S.load("p593")
def _bf593(pts):
    for p in permutations(pts):
        a, b, c, d = p
        v1 = (b[0] - a[0], b[1] - a[1])
        if v1 == (0, 0): continue
        v2 = (-v1[1], v1[0])
        if [a[0] + v2[0], a[1] + v2[1]] == d and [b[0] + v2[0], b[1] + v2[1]] == c:
            return True
    return False
for _ in range(5000):
    if random.random() < 0.5:
        x, y, dx, dy = random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3), random.randint(-3, 3)
        pts = [[x, y], [x + dx, y + dy], [x + dx - dy, y + dy + dx], [x - dy, y + dx]]
        if random.random() < 0.3: pts[random.randrange(4)][random.randrange(2)] += random.choice([-1, 1])
        random.shuffle(pts)
    else:
        pts = [[random.randint(-2, 2), random.randint(-2, 2)] for _ in range(4)]
    assert _p593.validSquare(*pts) == _bf593(pts), pts
print("P593 OK")

em({
 "num": 593, "title": "有效的正方形",
 "desc": "六個兩兩距離排序後：前四個相等且大於 0（邊）、後兩個相等且是邊的兩倍（對角線平方）。",
 "zh": ["給你平面上四個點的座標（順序任意），判斷它們能否構成一個<strong>正方形</strong>（邊長必須大於 0、四個角都是直角）。"],
 "idea": [
   ("c", """【點的順序未知 -> 看所有兩兩距離】
    4 個點有 6 個兩兩距離。正方形的 6 個距離是：
        4 條邊（相等）+ 2 條對角線（相等，且對角線² = 2·邊²）

【用距離的平方】
    避免開根號的浮點誤差。

【為什麼這樣就夠？】
    「四邊相等」只能保證菱形；
    再加上「兩條對角線相等」就排除了非正方形的菱形。
    （d² 的關係 2 倍是額外的保險，也排除了邊長 0 的退化情況搭配 d[0] > 0。）"""),
 ],
 "approaches": [
   ap("解法", "排序六個距離", [("c", S["p593"]), "驗證方式：和「嘗試所有點的順序，用向量旋轉 90° 檢查」的暴力法比對 5000 組（含刻意擾動的近似正方形）。"], "O(1)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>重複點</strong> → 距離 0，回傳 False。", "<strong>菱形</strong> → 四邊相等但對角線不等。", "<strong>傾斜的正方形</strong> → 距離判斷不受方向影響。"],
 "follow": [("h", "為什麼不用斜率？"), ("c", "斜率需要除法，遇到垂直線要特判；距離平方只用整數乘法，簡單又精確。")],
 "related": ["<strong>第 587 題 安裝柵欄</strong>", "<strong>第 939 題 最小面積矩形</strong>"],
 "check": ["正方形的六個兩兩距離有什麼特徵？", "只檢查四邊相等為什麼不夠？"],
})


# ==================== 594. Longest Harmonious Subsequence ====================
S["p594"] = '''class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        # ★ 和諧子序列只能由 x 和 x+1 兩種值組成：把兩者的出現次數加起來
        return max((cnt[x] + cnt[x + 1] for x in cnt if x + 1 in cnt), default=0)'''

_p594 = S.load("p594", extra={"Counter": Counter})
for _ in range(2000):
    a = [random.randint(0, 5) for _ in range(random.randint(1, 10))]
    want = 0
    for mask in range(1, 1 << len(a)):
        sub = [a[i] for i in range(len(a)) if mask >> i & 1]
        if max(sub) - min(sub) == 1:
            want = max(want, len(sub))
    assert _p594.findLHS(a) == want
print("P594 OK")

em({
 "num": 594, "title": "最長和諧子序列",
 "desc": "子序列不要求連續，順序無關：只要數每個值 x 和 x+1 的出現次數總和。",
 "zh": ["<strong>和諧陣列</strong>是最大值與最小值的差<strong>恰好為 1</strong> 的陣列。給你整數陣列 <code>nums</code>，回傳它所有子序列中最長的和諧子序列長度。"],
 "idea": [
   ("c", """【子序列 = 挑一些元素，順序不影響最大最小值】
    所以只要決定「挑哪些值」。

【和諧 <=> 只含 x 和 x+1 兩種值（兩種都要有）】
    挑了 x 和 x+1 之後，所有等於它們的元素都挑進來最好。
    長度 = cnt[x] + cnt[x+1]。

【注意】
    x+1 必須存在，否則只有一種值，差是 0 不是 1。"""),
 ],
 "approaches": [
   ap("解法", "雜湊表計數", [("c", S["p594"]), "驗證方式：和枚舉所有子序列的暴力法比對 2000 組。"], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>全部相同</strong> → 0（差是 0）。", "<strong>沒有相差 1 的值</strong> → 0。"],
 "follow": [("h", "子序列 vs 子陣列"), ("c", "如果要求連續（子陣列），就要用滑動視窗維護最大最小值；本題是子序列，順序無關，計數即可。")],
 "related": ["<strong>第 1 題 兩數之和</strong>"],
 "check": ["為什麼順序在這題不重要？", "為什麼 x+1 必須存在？"],
})


# ==================== 598. Range Addition II ====================
S["p598"] = '''class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        # ★ 每次操作都包含左上角；被所有操作覆蓋的區域 = 所有矩形的交集
        a = min((op[0] for op in ops), default=m)
        b = min((op[1] for op in ops), default=n)
        return a * b'''

_p598 = S.load("p598")
for _ in range(1000):
    m, n = random.randint(1, 5), random.randint(1, 5)
    ops = [[random.randint(1, m), random.randint(1, n)] for _ in range(random.randint(0, 4))]
    M = [[0] * n for _ in range(m)]
    for a, b in ops:
        for i in range(a):
            for j in range(b):
                M[i][j] += 1
    mx = max(max(r) for r in M)
    assert _p598.maxCount(m, n, ops) == sum(v == mx for r in M for v in r)
print("P598 OK")

em({
 "num": 598, "title": "範圍求和 II",
 "desc": "每次操作都是從左上角開始的矩形：最大值就是被所有操作覆蓋的區域，即最小寬 × 最小高。",
 "zh": [
   "給你一個 <code>m x n</code> 的全 0 矩陣和一組操作 <code>ops</code>，每個操作 <code>[a, b]</code> 把所有 <code>0 ≤ x &lt; a</code>、<code>0 ≤ y &lt; b</code> 的格子加 1。",
   "做完所有操作後，回傳矩陣中<strong>最大值</strong>的個數。",
 ],
 "idea": [
   ("c", """【每個操作都是從 (0, 0) 開始的矩形】
    最大值 = 被最多操作覆蓋的格子。
    被所有操作都覆蓋的區域 = 所有矩形的交集 = min(a) × min(b)，
    而且它一定非空（每個矩形都包含 (0, 0)）。
    這個區域裡的值 = 操作總數 = 最大值。

【沒有操作】
    整個矩陣都是 0，答案 m × n。"""),
 ],
 "approaches": [
   ap("解法", "取所有矩形的交集", [("c", S["p598"])], "O(k)", "O(1)", "k 為操作數", "", optimal=True),
 ],
 "edges": ["<strong>ops 為空</strong> → m × n。"],
 "follow": [("h", "一般的區間加法"), ("c", "如果矩形不是都從左上角開始，就要用二維差分陣列：每個矩形在四個角做 ±1，最後做二維前綴和還原。")],
 "related": ["<strong>第 370 題 區間加法</strong>（付費）", "<strong>第 304 題 二維區域和檢索</strong>"],
 "check": ["為什麼交集一定非空？", "沒有操作時答案是多少？"],
})
