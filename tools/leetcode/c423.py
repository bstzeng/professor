# -*- coding: utf-8 -*-
"""第 423、424、427、429、430、432 題。"""
import random
from collections import Counter, deque
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(423)


# ==================== 423. Reconstruct Original Digits from English ====================
S["p423"] = '''class Solution:
    def originalDigits(self, s: str) -> str:
        c = collections.Counter(s)
        d = [0] * 10
        # ★ 有些字母只出現在一個數字的英文裡，先數這些
        d[0] = c["z"]            # zero
        d[2] = c["w"]            # two
        d[4] = c["u"]            # four
        d[6] = c["x"]            # six
        d[8] = c["g"]            # eight
        # 再來是「扣掉上面之後」只剩一個數字有的字母
        d[1] = c["o"] - d[0] - d[2] - d[4]      # o：zero two four one
        d[3] = c["h"] - d[8]                    # h：three eight
        d[5] = c["f"] - d[4]                    # f：four five
        d[7] = c["s"] - d[6]                    # s：six seven
        d[9] = c["i"] - d[5] - d[6] - d[8]      # i：five six eight nine
        return "".join(str(k) * d[k] for k in range(10))'''

_p423 = S.load("p423")
_W = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for _ in range(3000):
    digs = [random.randrange(10) for _ in range(random.randrange(1, 12))]
    s = list("".join(_W[d] for d in digs))
    random.shuffle(s)
    assert _p423.originalDigits("".join(s)) == "".join(map(str, sorted(digs)))
print("P423 OK")

emit({
 "num": 423, "slug": "reconstruct-original-digits-from-english",
 "en": [
   "Given a string <code>s</code> containing an out-of-order English representation of digits <code>0-9</code>, return <em>the digits in <strong>ascending</strong> order</em>.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，是一些數字（0–9）的英文單字打散後混在一起的結果，請還原這些數字，並<strong>由小到大</strong>回傳。",
 ],
 "examples": """範例 1
  輸入：s = "owoztneoer"
  輸出："012"
  說明：zero, one, two

範例 2
  輸入：s = "fviefuro"
  輸出："45"
  說明：four, five""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁵",
   "<code>s[i]</code> 是 <code>[\"e\",\"g\",\"f\",\"i\",\"h\",\"o\",\"n\",\"s\",\"r\",\"u\",\"t\",\"w\",\"v\",\"x\",\"z\"]</code> 之一",
   "保證 <code>s</code> 是合法的",
 ],
 "idea": [
   ("c", """【找「獨一無二」的字母】
    z 只出現在 zero        -> zero 的個數 = z 的個數
    w 只出現在 two
    u 只出現在 four
    x 只出現在 six
    g 只出現在 eight

【扣掉之後又有新的獨特字母】
    o：zero、one、two、four -> one = o - zero - two - four
    h：three、eight         -> three = h - eight
    f：four、five           -> five = f - four
    s：six、seven           -> seven = s - six
    i：five、six、eight、nine -> nine = i - five - six - eight

    像解方程組一樣，一層一層把未知數解出來。"""),
   ("t", ["數字", "英文", "用來計數的字母", "要扣掉"],
    [["0", "zero", "z", ""], ["2", "two", "w", ""], ["4", "four", "u", ""], ["6", "six", "x", ""], ["8", "eight", "g", ""],
     ["1", "one", "o", "0, 2, 4"], ["3", "three", "h", "8"], ["5", "five", "f", "4"], ["7", "seven", "s", "6"], ["9", "nine", "i", "5, 6, 8"]]),
 ],
 "approaches": [
   ap("解法", "獨特字母 + 逐層扣除", [
     ("c", S["p423"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>同一個數字出現很多次</strong> → 計數自然處理。",
   "<strong>計算順序</strong> → 第二層必須在第一層之後。",
 ],
 "follow": [
   ("h", "一般化"),
   ("c", "這其實是一個 10 元一次方程組（每個字母一條方程式）。這組單字剛好可以用「逐步消去」解出；一般情況需要高斯消去法。"),
 ],
 "related": [
   "<strong>第 383 題 贖金信</strong> —— 字母計數",
   "<strong>第 1189 題 「氣球」的最大數量</strong>",
 ],
 "check": [
   "哪些字母只出現在一個數字的英文裡？",
   "數字 1 的個數要怎麼算？為什麼要扣掉 0、2、4？",
 ],
})


# ==================== 424. Longest Repeating Character Replacement ====================
S["p424"] = '''class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = collections.Counter()
        left = best_freq = 0
        for right, ch in enumerate(s):
            cnt[ch] += 1
            best_freq = max(best_freq, cnt[ch])     # 視窗中出現最多的字元次數（只增不減）
            # ★ 需要替換的數量 = 視窗長度 - 最多的那種字元
            if right - left + 1 - best_freq > k:
                cnt[s[left]] -= 1                   # 超過 k：視窗整體右移一格（長度不變）
                left += 1
        return len(s) - left                        # 視窗長度只增不減，最後的長度就是答案'''

S["p424_strict"] = '''class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        for target in set(s):                       # 假設最後全部變成 target
            left = other = 0
            for right, ch in enumerate(s):
                other += ch != target               # 視窗中不是 target 的個數
                while other > k:
                    other -= s[left] != target
                    left += 1
                best = max(best, right - left + 1)
        return best'''

_p424 = [S.load(x) for x in ("p424", "p424_strict")]
for s, k, want in [("ABAB", 2, 4), ("AABABBA", 1, 4), ("A", 0, 1)]:
    for sol in _p424:
        assert sol.characterReplacement(s, k) == want
for _ in range(3000):
    s = "".join(random.choice("ABC") for _ in range(random.randrange(1, 12)))
    k = random.randint(0, 4)
    want = max(j - i for i in range(len(s)) for j in range(i + 1, len(s) + 1)
               if (j - i) - max(Counter(s[i:j]).values()) <= k)
    for sol in _p424:
        assert sol.characterReplacement(s, k) == want, (s, k, sol)
print("P424 OK")

emit({
 "num": 424, "slug": "longest-repeating-character-replacement",
 "en": [
   "You are given a string <code>s</code> and an integer <code>k</code>. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most <code>k</code> times.",
   "Return <em>the length of the longest substring containing the same letter you can get after performing the above operations</em>.",
 ],
 "zh": [
   "給你一個由大寫字母組成的字串 <code>s</code> 和整數 <code>k</code>。你最多可以把 <code>k</code> 個字元換成任意大寫字母。",
   "回傳操作之後，由<strong>同一種字母</strong>組成的最長子字串長度。",
 ],
 "examples": """範例 1
  輸入：s = "ABAB", k = 2
  輸出：4
  說明：把兩個 A 換成 B（或反過來）。

範例 2
  輸入：s = "AABABBA", k = 1
  輸出：4
  說明：把中間的 A 換成 B，得到 "AABBBBA"。""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁵",
   "<code>s</code> 只包含大寫英文字母",
   "0 ≤ <code>k</code> ≤ <code>s.length</code>",
 ],
 "idea": [
   ("c", """【一個視窗能不能變成同一種字母？】
    需要替換的數量 = 視窗長度 - 出現最多的那種字母的次數
    <= k 就可以。

【方法一：枚舉目標字母 + 標準滑動視窗】
    假設最後全部變成 A：
    視窗內「不是 A」的個數 <= k，標準的可變視窗。
    26 種字母各做一次 -> O(26n)。

【方法二：一次滑動視窗（不縮小的技巧）】
    我們只在乎「最長」的視窗。
    - 視窗長度只增不減：不合法時，左右各移一格（整體平移）
    - best_freq 記錄「歷史上」視窗中出現最多的次數，只增不減

    為什麼 best_freq 不需要在左邊移出時減少？
    視窗長度 = 目前找到的最佳答案。
    要讓答案變大，視窗必須在「不平移」的情況下長大一格，
    這只有在 best_freq 真的變大時才會發生：
        長度 L+1 合法  <=>  某種字元出現至少 L+1-k 次
    而 best_freq 每次增加，都是某個真實視窗裡的真實次數。
    所以偏大的舊 best_freq 只會讓視窗「多平移幾次」，不會讓答案算錯。"""),
 ],
 "approaches": [
   ap("解法一", "枚舉目標字母 + 滑動視窗", [
     ("c", S["p424_strict"]),
   ], "O(26 · n)", "O(1)", "", ""),

   ap("解法二", "只增不減的滑動視窗", [
     ("c", S["p424"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、枚舉字母", "O(26n)", "邏輯最清楚"],
    ["二、不縮小視窗", "O(n)", "技巧性 ✔"]]),
 "edges": [
   "<strong>k = 0</strong> → 最長的連續相同字母段。",
   "<strong>k ≥ 長度</strong> → 整個字串。",
   "<strong>只有一種字母</strong> → 整個字串。",
 ],
 "follow": [
   ("h", "同類題"),
   ("c", "第 1004 題「最大連續 1 的個數 III」：只有 0 和 1，最多把 k 個 0 變 1——就是本題方法一的特例。"),
 ],
 "related": [
   "<strong>第 1004 題 最大連續 1 的個數 III</strong>",
   "<strong>第 3 題 無重複字元的最長子字串</strong>",
   "<strong>第 2024 題 考試的最大困擾度</strong>",
 ],
 "check": [
   "一個視窗需要替換幾個字元？",
   "方法二中，為什麼視窗長度可以只增不減？",
   "best_freq 為什麼不需要在左邊移出時更新？",
 ],
})


# ==================== 427. Construct Quad Tree ====================
class _QNode:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val, self.isLeaf = val, isLeaf
        self.topLeft, self.topRight, self.bottomLeft, self.bottomRight = topLeft, topRight, bottomLeft, bottomRight


S["p427"] = '''"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight): ...
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        # 二維前綴和：O(1) 算出任一區塊的總和
        P = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(n):
                P[i + 1][j + 1] = P[i][j + 1] + P[i + 1][j] - P[i][j] + grid[i][j]

        def build(r: int, c: int, size: int) -> 'Node':
            total = P[r + size][c + size] - P[r][c + size] - P[r + size][c] + P[r][c]
            if total == 0 or total == size * size:          # ★ 全 0 或全 1：葉節點
                return Node(total > 0, True, None, None, None, None)
            h = size // 2
            return Node(True, False,
                        build(r, c, h), build(r, c + h, h),
                        build(r + h, c, h), build(r + h, c + h, h))

        return build(0, 0, n)'''

_p427 = S.load("p427", extra={"Node": _QNode})


def _render(node, size, out, r=0, c=0):
    if node.isLeaf:
        for i in range(r, r + size):
            for j in range(c, c + size):
                out[i][j] = int(node.val)
        return
    h = size // 2
    _render(node.topLeft, h, out, r, c)
    _render(node.topRight, h, out, r, c + h)
    _render(node.bottomLeft, h, out, r + h, c)
    _render(node.bottomRight, h, out, r + h, c + h)


def _minimal(node):
    if node.isLeaf:
        return True
    kids = [node.topLeft, node.topRight, node.bottomLeft, node.bottomRight]
    if all(k.isLeaf for k in kids) and len({k.val for k in kids}) == 1:
        return False                     # 四個一樣的葉子應該合併
    return all(_minimal(k) for k in kids)


for _ in range(1000):
    n = 1 << random.randint(0, 3)
    base = random.random()
    grid = [[int(random.random() < base) for _ in range(n)] for _ in range(n)]
    t = _p427.construct(grid)
    out = [[-1] * n for _ in range(n)]
    _render(t, n, out)
    assert out == grid and _minimal(t)
print("P427 OK")

emit({
 "num": 427, "slug": "construct-quad-tree",
 "en": [
   "Given a <code>n * n</code> matrix <code>grid</code> of <code>0's</code> and <code>1's</code> only. We want to represent <code>grid</code> with a Quad-Tree.",
   "Return <em>the root of the Quad-Tree representing</em> <code>grid</code>.",
   "A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:",
   ("ul", ["<code>val</code>: True if the node represents a grid of 1's or False if the node represents a grid of 0's. Notice that you can assign the <code>val</code> to True or False when <code>isLeaf</code> is False, and both are accepted in the answer.",
           "<code>isLeaf</code>: True if the node is a leaf node on the tree or False if the node has four children."]),
   "We can construct a Quad-Tree from a two-dimensional area using the following steps:",
   ("ol", ["If the current grid has the same value (i.e all <code>1's</code> or all <code>0's</code>) set <code>isLeaf</code> True and set <code>val</code> to the value of the grid and set the four children to Null and stop.",
           "If the current grid has different values, set <code>isLeaf</code> to False and set <code>val</code> to any value and divide the current grid into four sub-grids.",
           "Recurse for each of the children with the proper sub-grid."]),
 ],
 "zh": [
   "給你一個只含 0 和 1 的 <code>n x n</code> 矩陣（n 是 2 的冪），用<strong>四元樹</strong>表示它，回傳根節點。",
   "四元樹的每個內部節點恰好有四個孩子（左上、右上、左下、右下），節點有兩個屬性：<code>val</code>（這塊全是 1 則 True，全是 0 則 False）、<code>isLeaf</code>（是否為葉子）。",
   "建構規則：",
   ("ol", ["目前的區塊如果全部相同 → 葉節點，<code>val</code> 設為該值。",
           "否則 → 內部節點（<code>val</code> 任意），把區塊切成四等份，分別遞迴。"]),
 ],
 "examples": """範例 1
  輸入：grid = [[0,1],[1,0]]
  輸出：根不是葉子，四個孩子分別是 0、1、1、0 的葉子。

範例 2
  輸入：8 × 8 的格子，左半全 1、右上 4×4 全 0、右下有混合
  輸出：只有混合的區塊會繼續分割。""",
 "constraints": [
   "<code>n == grid.length == grid[i].length</code>",
   "<code>n == 2<sup>x</sup></code>，0 ≤ x ≤ 6",
 ],
 "idea": [
   ("c", """【分治】
    build(區塊)：
        全部相同 -> 葉子
        否則     -> 切四塊，分別 build

【怎麼快速判斷一塊是否全部相同？】
    直接掃描：每一層都要掃一次整塊 -> O(n² log n)
    二維前綴和（第 304 題）：O(1) 算出區塊總和
        總和 = 0         -> 全 0
        總和 = size²     -> 全 1
        其他             -> 混合
    -> 總時間 O(n²)（前綴和）+ 節點數

【另一種 O(n²)：由下往上】
    先遞迴建四個孩子，
    如果四個孩子都是葉子而且值相同 -> 合併成一個葉子。"""),
 ],
 "approaches": [
   ap("解法", "分治 + 二維前綴和", [
     ("c", S["p427"]),
     "驗證方式：把建好的四元樹「畫回」矩陣，確認和原矩陣相同，而且沒有四個相同的葉子沒被合併。",
   ], "O(n²)", "O(n²)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>1 × 1</strong> → 一個葉子。",
   "<strong>整塊相同</strong> → 根就是葉子。",
   "<strong>非葉節點的 val</strong> → 任意值都可以。",
 ],
 "follow": [
   ("h", "四元樹的應用"),
   ("c", "影像壓縮（大片相同顏色只存一個節點）、2D 碰撞偵測、地圖的空間索引。第 558 題是兩棵四元樹的 OR 運算。"),
 ],
 "related": [
   "<strong>第 558 題 四元樹交集</strong>",
   "<strong>第 304 題 二維區域和檢索</strong>",
 ],
 "check": [
   "怎麼用前綴和判斷一塊是否全部相同？",
   "分治的遞迴終止條件是什麼？",
 ],
})


# ==================== 429. N-ary Tree Level Order Traversal ====================
class _NNode:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


S["p429"] = '''"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            # ★ 下一層 = 這一層所有節點的孩子，依序串起來
            level = [child for node in level for child in node.children]
        return res'''

_p429 = S.load("p429", extra={"Node": _NNode})


def _rand_nary(n):
    nodes = [_NNode(i) for i in range(n)]
    for i in range(1, n):
        nodes[random.randrange(i)].children.append(nodes[i])
    return nodes[0] if n else None


def _levels(root):
    out, q = [], deque([(root, 0)]) if root else deque()
    while q:
        nd, d = q.popleft()
        if d == len(out):
            out.append([])
        out[d].append(nd.val)
        for c in nd.children:
            q.append((c, d + 1))
    return out


for _ in range(1500):
    t = _rand_nary(random.randrange(0, 20))
    assert _p429.levelOrder(t) == _levels(t)
print("P429 OK")

emit({
 "num": 429, "slug": "n-ary-tree-level-order-traversal",
 "en": [
   "Given an n-ary tree, return the <em>level order</em> traversal of its nodes' values.",
   "<em>Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.</em>",
 ],
 "zh": [
   "給你一棵 <strong>N 元樹</strong>（每個節點可以有任意多個孩子），回傳它的<strong>層序遍歷</strong>結果：每一層的節點值放在一個串列裡。",
 ],
 "examples": """範例 1
  輸入：root = [1,null,3,2,4,null,5,6]
        1
      / | \\
     3  2  4
    / \\
   5   6
  輸出：[[1],[3,2,4],[5,6]]""",
 "constraints": [
   "樹的高度不超過 1000",
   "節點總數在 <code>[0, 10⁴]</code> 之間",
 ],
 "idea": [
   ("c", """【和二元樹的層序遍歷（第 102 題）一樣】
    只是「左孩子、右孩子」換成「children 串列」。

【一層一層處理】
    level = 目前這一層的所有節點
    記下它們的值，
    下一層 = 所有節點的 children 依序接起來。
    重複直到沒有節點。

    這種寫法不需要記錄每層的大小，比「一個佇列 + 計數」更直觀。"""),
 ],
 "approaches": [
   ap("解法", "逐層展開", [
     ("c", S["p429"]),
   ], "O(n)", "O(w)", "", "w = 最寬一層", optimal=True),
 ],
 "edges": [
   "<strong>空樹</strong> → <code>[]</code>。",
   "<strong>只有根</strong> → <code>[[val]]</code>。",
   "<strong>葉子的 children</strong> → 空串列（不是 None，但寫法也要能處理）。",
 ],
 "follow": [
   ("h", "N 元樹系列"),
   ("c", "第 559 題（最大深度）、第 589 題（前序）、第 590 題（後序）——和二元樹相同，只是把兩個孩子換成迴圈。"),
 ],
 "related": [
   "<strong>第 102 題 二元樹的層序遍歷</strong>",
   "<strong>第 559 題 N 叉樹的最大深度</strong>",
   "<strong>第 589 題 N 叉樹的前序遍歷</strong>",
 ],
 "check": [
   "下一層的節點怎麼由這一層得到？",
   "和二元樹的層序遍歷有什麼不同？",
 ],
})


# ==================== 430. Flatten a Multilevel Doubly Linked List ====================
class _MNode:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val, self.prev, self.next, self.child = val, prev, next, child


S["p430"] = '''"""
class Node:
    def __init__(self, val, prev, next, child): ...
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        stack = []                            # 暫存「被子串列打斷的後半段」
        cur = head
        while cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)    # ★ 後半段先存起來，等子串列走完再接
                cur.next = cur.child          # 子串列接到 cur 後面
                cur.child.prev = cur
                cur.child = None
            elif cur.next is None and stack:  # 走到某一層的結尾：接回之前存的後半段
                nxt = stack.pop()
                cur.next = nxt
                nxt.prev = cur
            cur = cur.next
        return head'''

_p430 = S.load("p430", extra={"Node": _MNode})


def _build_ml(d=0, counter=[0]):
    L = random.randint(1, 4)
    nodes = []
    for _ in range(L):
        counter[0] += 1
        nodes.append(_MNode(counter[0]))
    for a, b in zip(nodes, nodes[1:]):
        a.next, b.prev = b, a
    for nd in nodes:
        if d < 3 and random.random() < 0.3:
            nd.child = _build_ml(d + 1, counter)
    return nodes[0]


def _pre(nd):
    out = []
    while nd:
        out.append(nd.val)
        if nd.child:
            out += _pre(nd.child)
        nd = nd.next
    return out


for _ in range(1500):
    h = _build_ml()
    want = _pre(h)
    got = _p430.flatten(h)
    vals, prev, x = [], None, got
    while x:
        assert x.child is None and x.prev is prev
        vals.append(x.val)
        prev, x = x, x.next
    assert vals == want
print("P430 OK")

emit({
 "num": 430, "slug": "flatten-a-multilevel-doubly-linked-list",
 "en": [
   "You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional <strong>child pointer</strong>. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. "
   "These child lists may have one or more children of their own, and so on, to produce a <strong>multilevel data structure</strong>.",
   "Given the <code>head</code> of the first level of the list, <strong>flatten</strong> the list so that all the nodes appear in a single-level, doubly linked list. Let <code>curr</code> be a node with a child list. "
   "The nodes in the child list should appear <strong>after</strong> <code>curr</code> and <strong>before</strong> <code>curr.next</code> in the flattened list.",
   "Return <em>the</em> <code>head</code> <em>of the flattened list. The nodes in the list must have <strong>all</strong> of their child pointers set to</em> <code>null</code>.",
 ],
 "zh": [
   "給你一個雙向鏈結串列，節點除了 <code>next</code>、<code>prev</code> 之外還有一個 <code>child</code> 指標，可能指向另一條雙向串列（它的節點也可能有 child……形成多層結構）。",
   "請把它<strong>攤平</strong>成單層的雙向串列：節點 <code>curr</code> 的子串列要放在 <code>curr</code> 之後、<code>curr.next</code> 之前。",
   "回傳攤平後的頭節點，所有節點的 <code>child</code> 都要設成 <code>null</code>。",
 ],
 "examples": """範例
  輸入：
    1---2---3---4---5---6--NULL
            |
            7---8---9---10--NULL
                |
                11--12--NULL
  輸出：1-2-3-7-8-11-12-9-10-4-5-6""",
 "constraints": [
   "節點數不超過 1000",
   "1 ≤ <code>Node.val</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【攤平的順序 = 前序遍歷】
    把 child 看成「左孩子」、next 看成「右孩子」，
    攤平後的順序就是這棵二元樹的前序遍歷（第 114 題的雙向串列版）。

【用堆疊暫存「後半段」】
    沿著串列走，遇到有 child 的節點 cur：
        cur.next 那一段先推進堆疊（等一下再接）
        把 child 串列接到 cur 後面（記得設 prev、清空 child）
    走到某一層的結尾（next 為 None）而堆疊不空：
        彈出一段，接在後面繼續走

【雙向串列的細節】
    每次接上都要同時設 next 和 prev。
    child 必須設為 None。"""),
 ],
 "approaches": [
   ap("解法", "迭代 + 堆疊存後半段", [
     ("c", S["p430"]),
   ], "O(n)", "O(d)", "", "d = 層數", optimal=True),
 ],
 "edges": [
   "<strong>空串列</strong> → None。",
   "<strong>有 child 的節點沒有 next</strong> → 不用推堆疊。",
   "<strong>多層巢狀</strong> → 堆疊依序接回。",
 ],
 "follow": [
   ("h", "遞迴版本"),
   ("c", "寫一個 flatten_tail(node) 回傳攤平後的尾巴：遇到 child 就遞迴攤平它，拿到子串列的尾巴，接上原本的 next。"),
 ],
 "related": [
   "<strong>第 114 題 二元樹展開為鏈結串列</strong>",
   "<strong>第 341 題 扁平化巢狀串列迭代器</strong>",
 ],
 "check": [
   "攤平的順序和哪種樹的遍歷相同？",
   "遇到有 child 的節點時，原本的 next 要怎麼處理？",
   "雙向串列接上時要設定哪些指標？",
 ],
})


# ==================== 432. All O`one Data Structure ====================
S["p432"] = '''class Bucket:                                # 雙向鏈結串列的一個節點：同一個次數的所有 key
    def __init__(self, count: int):
        self.count = count
        self.keys = set()
        self.prev = self.next = None


class AllOne:
    def __init__(self):
        self.head, self.tail = Bucket(0), Bucket(0)   # 哨兵：head 最小端、tail 最大端
        self.head.next, self.tail.prev = self.tail, self.head
        self.where = {}                                # key -> 它所在的 Bucket

    def _insert_after(self, node: Bucket, count: int) -> Bucket:
        b = Bucket(count)
        b.prev, b.next = node, node.next
        node.next.prev = b
        node.next = b
        return b

    def _remove_if_empty(self, b: Bucket) -> None:
        if not b.keys and b is not self.head:
            b.prev.next, b.next.prev = b.next, b.prev

    def inc(self, key: str) -> None:
        cur = self.where.get(key, self.head)           # 新 key 視為在「次數 0」的 head
        nxt = cur.next
        if nxt is self.tail or nxt.count != cur.count + 1:
            nxt = self._insert_after(cur, cur.count + 1)   # ★ 次數 +1 的桶不存在就建立
        nxt.keys.add(key)
        self.where[key] = nxt
        if cur is not self.head:
            cur.keys.discard(key)
            self._remove_if_empty(cur)

    def dec(self, key: str) -> None:
        cur = self.where[key]
        cur.keys.discard(key)
        if cur.count == 1:
            del self.where[key]                        # 次數變 0：移除 key
        else:
            prv = cur.prev
            if prv is self.head or prv.count != cur.count - 1:
                prv = self._insert_after(cur.prev, cur.count - 1)
            prv.keys.add(key)
            self.where[key] = prv
        self._remove_if_empty(cur)

    def getMaxKey(self) -> str:
        b = self.tail.prev
        return next(iter(b.keys)) if b is not self.head else ""

    def getMinKey(self) -> str:
        b = self.head.next
        return next(iter(b.keys)) if b is not self.tail else ""'''

_cls = S.loadns("p432")["AllOne"]
for _ in range(500):
    ao, ref = _cls(), Counter()
    for _ in range(80):
        r = random.random()
        k = random.choice("abcde")
        if r < 0.5:
            ao.inc(k); ref[k] += 1
        elif r < 0.75:
            live = [x for x in ref if ref[x] > 0]
            if live:
                k = random.choice(live)
                ao.dec(k); ref[k] -= 1
                if ref[k] == 0:
                    del ref[k]
        else:
            if ref:
                mx, mn = max(ref.values()), min(ref.values())
                assert ref[ao.getMaxKey()] == mx and ref[ao.getMinKey()] == mn
            else:
                assert ao.getMaxKey() == "" and ao.getMinKey() == ""
print("P432 OK")

_P432_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">雙向鏈結串列：每個節點是一個「次數桶」，次數由小到大排列</text>
            <g font-size="12" text-anchor="middle">
              <rect x="30" y="50" width="70" height="50" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/><text x="65" y="80" fill="var(--text-muted)">head</text>
              <rect x="140" y="50" width="100" height="50" rx="6" fill="none" stroke="var(--accent)"/><text x="190" y="70" fill="var(--accent)">次數 1</text><text x="190" y="90" fill="var(--text)">{b, c}</text>
              <rect x="280" y="50" width="100" height="50" rx="6" fill="none" stroke="var(--accent)"/><text x="330" y="70" fill="var(--accent)">次數 3</text><text x="330" y="90" fill="var(--text)">{a}</text>
              <rect x="420" y="50" width="100" height="50" rx="6" fill="none" stroke="var(--accent)"/><text x="470" y="70" fill="var(--accent)">次數 4</text><text x="470" y="90" fill="var(--text)">{d}</text>
              <rect x="560" y="50" width="60" height="50" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/><text x="590" y="80" fill="var(--text-muted)">tail</text>
            </g>
            <g stroke="var(--text-muted)"><line x1="100" y1="75" x2="140" y2="75"/><line x1="240" y1="75" x2="280" y2="75"/><line x1="380" y1="75" x2="420" y2="75"/><line x1="520" y1="75" x2="560" y2="75"/></g>
            <text x="190" y="128" text-anchor="middle" fill="var(--gold)" font-size="12">getMinKey → head.next</text>
            <text x="470" y="128" text-anchor="middle" fill="var(--gold)" font-size="12">getMaxKey → tail.prev</text>
            <text x="30" y="166" fill="var(--text)" font-size="12">inc("a")：a 從「次數 3」搬到「次數 4」（隔壁的桶剛好是 4，直接放進去）</text>
            <text x="30" y="188" fill="var(--text)" font-size="12">inc("b")：b 從「次數 1」搬到「次數 2」（隔壁是 3，要在中間新建一個「次數 2」的桶）</text>
            <text x="30" y="214" fill="var(--gold)" font-size="12">★ 次數每次只變 ±1，所以 key 只會搬到相鄰的桶 —— 全部 O(1)。</text>'''

emit({
 "num": 432, "slug": "all-oone-data-structure",
 "en": [
   "Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.",
   "Implement the <code>AllOne</code> class:",
   ("ul", ["<code>AllOne()</code> Initializes the object of the data structure.",
           "<code>inc(String key)</code> Increments the count of the string <code>key</code> by <code>1</code>. If <code>key</code> does not exist in the data structure, insert it with count <code>1</code>.",
           "<code>dec(String key)</code> Decrements the count of the string <code>key</code> by <code>1</code>. If the count of <code>key</code> is <code>0</code> after the decrement, remove it from the data structure. It is guaranteed that <code>key</code> exists in the data structure before the decrement.",
           "<code>getMaxKey()</code> Returns one of the keys with the maximal count. If no element exists, return an empty string <code>\"\"</code>.",
           "<code>getMinKey()</code> Returns one of the keys with the minimum count. If no element exists, return an empty string <code>\"\"</code>."]),
   "<strong>Note</strong> that each function must run in <code>O(1)</code> average time complexity.",
 ],
 "zh": [
   "設計一個資料結構，記錄每個字串的次數，並能快速取得次數最多、最少的字串：",
   ("ul", ["<code>inc(key)</code>：key 的次數 +1（不存在就以 1 加入）。",
           "<code>dec(key)</code>：key 的次數 −1，變成 0 就移除（保證 key 存在）。",
           "<code>getMaxKey()</code>：回傳任一個次數最多的 key；沒有就回傳 <code>\"\"</code>。",
           "<code>getMinKey()</code>：回傳任一個次數最少的 key；沒有就回傳 <code>\"\"</code>。"]),
   "每個操作的平均時間都必須是 <code>O(1)</code>。",
 ],
 "examples": """範例
  inc("hello"), inc("hello")
  getMaxKey() -> "hello"
  getMinKey() -> "hello"
  inc("leet")
  getMaxKey() -> "hello"
  getMinKey() -> "leet\"""",
 "constraints": [
   "1 ≤ <code>key.length</code> ≤ 10",
   "<code>key</code> 只包含小寫英文字母",
   "呼叫 <code>dec</code> 時 key 一定存在",
   "最多呼叫 5 × 10⁴ 次",
 ],
 "idea": [
   ("fig", _P432_FIG, "0 0 640 228"),
   ("c", """【困難點】
    雜湊表 key -> 次數：inc / dec O(1)，但找最大最小要 O(n)。
    堆積：找最大最小 O(1)，但更新某個 key 的次數要 O(log n)。

【關鍵：每次只 ±1】
    次數的變化是「相鄰」的 ->
    用一條依次數排序的雙向鏈結串列，每個節點是一個「次數桶」，
    桶裡放所有這個次數的 key。
    key 次數 +1 -> 搬到下一個桶（不存在就在旁邊新建）
    key 次數 -1 -> 搬到上一個桶
    都只動到相鄰的節點 -> O(1)。

    最小值：head.next 的桶；最大值：tail.prev 的桶。

【另外需要】
    where[key] = key 目前所在的桶（雜湊表）
    桶空了要從串列移除。

【這和 LFU 快取（第 460 題）是同一種結構】"""),
 ],
 "approaches": [
   ap("解法", "次數桶的雙向鏈結串列 + 雜湊表", [
     ("c", S["p432"]),
   ], "每個操作 O(1)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>新的 key</strong> → 從「次數 0」（head）往上搬到次數 1。",
   "<strong>次數降到 0</strong> → 從 where 中移除。",
   "<strong>桶空了</strong> → 從串列移除（head、tail 哨兵不能刪）。",
   "<strong>沒有任何 key</strong> → 回傳空字串。",
 ],
 "follow": [
   ("h", "O(1) 資料結構設計的套路"),
   ("c", "雜湊表負責「找到它」，鏈結串列負責「維持順序、O(1) 搬移」。第 146 題（LRU）、第 460 題（LFU）、本題都是這個組合。"),
 ],
 "related": [
   "<strong>第 460 題 LFU 快取</strong>",
   "<strong>第 146 題 LRU 快取</strong>",
   "<strong>第 380 題 O(1) 插入、刪除和取得隨機元素</strong>",
 ],
 "check": [
   "為什麼用堆積做不到 O(1)？",
   "「每次只 ±1」這個性質為什麼重要？",
   "inc 時如果次數 +1 的桶不存在，要怎麼辦？",
 ],
})
