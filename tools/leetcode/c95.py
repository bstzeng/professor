# -*- coding: utf-8 -*-
"""第 95–97 題。"""
import random, math, functools
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(95)


def _inorder(node):
    return _inorder(node.left) + [node.val] + _inorder(node.right) if node else []


def _shape(node):
    """把樹的形狀序列化，用來比較兩棵樹是否相同。"""
    if not node:
        return "#"
    return "(%s %d %s)" % (_shape(node.left), node.val, _shape(node.right))


def _is_bst(node, lo=float("-inf"), hi=float("inf")):
    if not node:
        return True
    return (lo < node.val < hi and _is_bst(node.left, lo, node.val)
            and _is_bst(node.right, node.val, hi))


# ==================== 95. Unique Binary Search Trees II ====================
S["p95"] = '''class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        def build(lo: int, hi: int) -> List[Optional[TreeNode]]:
            """用 lo..hi 這些數字，能建出哪些 BST"""
            if lo > hi:
                return [None]          # 空樹也是一種（注意是 [None] 不是 []）

            res = []
            for root_val in range(lo, hi + 1):
                # 左子樹用 lo..root_val-1，右子樹用 root_val+1..hi
                for left in build(lo, root_val - 1):
                    for right in build(root_val + 1, hi):
                        res.append(TreeNode(root_val, left, right))
            return res

        return build(1, n)'''

S["p95_memo"] = '''class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        # 「長度相同的區間」形狀完全一樣，只是數值有偏移
        # 所以只算 1..k 的所有形狀，再整體平移
        memo = {}

        def build(length: int) -> List[Optional[TreeNode]]:
            if length == 0:
                return [None]
            if length in memo:
                return memo[length]

            res = []
            for root_val in range(1, length + 1):
                for left in build(root_val - 1):
                    for right in build(length - root_val):
                        res.append(TreeNode(root_val, left, clone(right, root_val)))
            memo[length] = res
            return res

        def clone(node, offset):
            """把整棵子樹的值都加上 offset（右子樹需要平移）"""
            if not node:
                return None
            return TreeNode(node.val + offset,
                            clone(node.left, offset), clone(node.right, offset))

        return build(n)'''

_p95 = [S.load(k) for k in ("p95", "p95_memo")]
_CAT = [1, 1, 2, 5, 14, 42, 132, 429, 1430]
for n in range(0, 9):
    for sol in _p95:
        trees = sol.generateTrees(n)
        if n == 0:
            assert trees == [], ("P95 n=0", sol, trees)
            continue
        assert len(trees) == _CAT[n], ("P95 count", n, sol, len(trees), _CAT[n])
        shapes = set()
        for t in trees:
            assert _inorder(t) == list(range(1, n + 1)), ("P95 中序不對", n, _inorder(t))
            assert _is_bst(t), ("P95 不是 BST", n)
            shapes.add(_shape(t))
        assert len(shapes) == _CAT[n], ("P95 有重複的樹", n, len(shapes))
print("P95 solutions OK")

_P95_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">n = 3：枚舉「誰當根」，左右子樹各自遞迴生成</text>
            <g font-size="13" text-anchor="middle">
              <text x="90" y="48" fill="var(--gold)" font-size="12">根 = 1</text>
              <circle cx="60" cy="74" r="15" fill="none" stroke="var(--accent)"/><text x="60" y="79" fill="var(--accent)">1</text>
              <circle cx="90" cy="118" r="15" fill="none" stroke="var(--accent)"/><text x="90" y="123" fill="var(--accent)">2</text>
              <circle cx="120" cy="162" r="15" fill="none" stroke="var(--accent)"/><text x="120" y="167" fill="var(--accent)">3</text>
              <line x1="70" y1="86" x2="80" y2="106" stroke="var(--border)"/>
              <line x1="100" y1="130" x2="110" y2="150" stroke="var(--border)"/>

              <circle cx="180" cy="74" r="15" fill="none" stroke="var(--accent)"/><text x="180" y="79" fill="var(--accent)">1</text>
              <circle cx="220" cy="118" r="15" fill="none" stroke="var(--accent)"/><text x="220" y="123" fill="var(--accent)">3</text>
              <circle cx="196" cy="162" r="15" fill="none" stroke="var(--accent)"/><text x="196" y="167" fill="var(--accent)">2</text>
              <line x1="190" y1="86" x2="210" y2="106" stroke="var(--border)"/>
              <line x1="210" y1="130" x2="204" y2="150" stroke="var(--border)"/>
            </g>
            <g font-size="13" text-anchor="middle">
              <text x="300" y="48" fill="var(--gold)" font-size="12">根 = 2</text>
              <circle cx="300" cy="74" r="15" fill="none" stroke="#ff8a65"/><text x="300" y="79" fill="#ff8a65">2</text>
              <circle cx="270" cy="118" r="15" fill="none" stroke="#ff8a65"/><text x="270" y="123" fill="#ff8a65">1</text>
              <circle cx="330" cy="118" r="15" fill="none" stroke="#ff8a65"/><text x="330" y="123" fill="#ff8a65">3</text>
              <line x1="290" y1="86" x2="280" y2="106" stroke="var(--border)"/>
              <line x1="310" y1="86" x2="320" y2="106" stroke="var(--border)"/>
            </g>
            <g font-size="13" text-anchor="middle">
              <text x="470" y="48" fill="var(--gold)" font-size="12">根 = 3</text>
              <circle cx="420" cy="74" r="15" fill="none" stroke="var(--accent)"/><text x="420" y="79" fill="var(--accent)">3</text>
              <circle cx="390" cy="118" r="15" fill="none" stroke="var(--accent)"/><text x="390" y="123" fill="var(--accent)">1</text>
              <circle cx="414" cy="162" r="15" fill="none" stroke="var(--accent)"/><text x="414" y="167" fill="var(--accent)">2</text>
              <line x1="410" y1="86" x2="400" y2="106" stroke="var(--border)"/>
              <line x1="398" y1="130" x2="408" y2="150" stroke="var(--border)"/>

              <circle cx="530" cy="74" r="15" fill="none" stroke="var(--accent)"/><text x="530" y="79" fill="var(--accent)">3</text>
              <circle cx="500" cy="118" r="15" fill="none" stroke="var(--accent)"/><text x="500" y="123" fill="var(--accent)">2</text>
              <circle cx="470" cy="162" r="15" fill="none" stroke="var(--accent)"/><text x="470" y="167" fill="var(--accent)">1</text>
              <line x1="520" y1="86" x2="510" y2="106" stroke="var(--border)"/>
              <line x1="490" y1="130" x2="480" y2="150" stroke="var(--border)"/>
            </g>
            <line x1="20" y1="192" x2="620" y2="192" stroke="var(--border)"/>
            <text x="20" y="220" fill="var(--gold)" font-size="12">根 = 1：左邊空、右邊用 {2,3}（2 種）　根 = 2：左 {1}、右 {3}（1 種）</text>
            <text x="20" y="244" fill="var(--gold)" font-size="12">根 = 3：左邊用 {1,2}（2 種）、右邊空　　　合計 2 + 1 + 2 = 5 種 ✔</text>
            <text x="20" y="272" fill="var(--text-muted)" font-size="12">這正是卡塔蘭數的遞迴式：C(3) = C(0)C(2) + C(1)C(1) + C(2)C(0) = 2 + 1 + 2 = 5</text>'''

emit({
 "num": 95, "slug": "unique-binary-search-trees-ii",
 "en": [
   "Given an integer <code>n</code>, return <em>all the structurally unique <strong>BST's</strong> "
   "(binary search trees), which has exactly </em><code>n</code><em> nodes of unique values from "
   "</em><code>1</code><em> to </em><code>n</code>. Return the answer in <strong>any order</strong>.",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，請生成所有由 <code>1</code> 到 <code>n</code> "
   "這 <code>n</code> 個不同數字組成的<strong>二元搜尋樹（BST）</strong>，"
   "回傳它們的根節點。順序不拘。",
 ],
 "pre": [
   ("note", "核心：枚舉「誰當根」", [
     ("c", """BST 的定義：左子樹的所有值 < 根 < 右子樹的所有值。

所以如果選 k 當根，那麼：
    左子樹只能用 1 .. k-1
    右子樹只能用 k+1 .. n

    而且【左右子樹的選擇是獨立的】——
    左邊有 a 種、右邊有 b 種，組合起來就有 a × b 種。

遞迴式：
    build(lo, hi) = 用 lo..hi 這些數字能建出的所有 BST

    build(lo, hi) = 對每個 k ∈ [lo, hi]：
                        for L in build(lo, k-1):
                            for R in build(k+1, hi):
                                產生 TreeNode(k, L, R)

    base：lo > hi  ->  [None]（空樹，一種）

數量：
    f(n) = Σ_{k=1..n} f(k-1) × f(n-k)

    這正是【卡塔蘭數】的遞迴式！
        f(0)=1, f(1)=1, f(2)=2, f(3)=5, f(4)=14, ...

    和第 22 題（括號生成）是同一個數列 ——
    因為兩者的遞迴結構同構。"""),
     "<strong>base case 是 <code>[None]</code> 而不是 <code>[]</code></strong> —— "
     "這是本題最關鍵的一行。<code>[]</code> 表示「沒有任何方案」，"
     "<code>[None]</code> 表示「有一種方案，就是空樹」。"
     "寫成 <code>[]</code> 的話內層迴圈一次都不跑，答案永遠是空的。",
   ]),
 ],
 "examples": """範例 1
  輸入：n = 3
  輸出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],
         [3,1,null,null,2],[3,2,null,1]]
  說明：共 5 棵，剛好是第 3 個卡塔蘭數。

範例 2
  輸入：n = 1
  輸出：[[1]]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 8",
 ],
 "mid": [
   ("note", "為什麼 n 只到 8？", [
     ("c", """卡塔蘭數：
    n:     1  2  3  4   5   6    7    8     9     10
    C(n):  1  2  5  14  42  132  429  1430  4862  16796

n = 8 時要生成 1430 棵樹 ——
而且每棵樹有 8 個節點，總共約 11440 個節點。

n = 15 時是 9694845 棵 —— 記憶體就爆了。

所以 n ≤ 8 是「輸出大小」的限制，不是演算法的限制。

驗證你的程式最快的方法：
    數數量對不對（1, 1, 2, 5, 14, 42, 132, 429, 1430）"""),
   ]),
 ],
 "idea": [
   ("fig", _P95_FIG, "0 0 640 288"),
 ],
 "approaches": [
   ap("解法一", "遞迴分治（標準解）", [
     ("c", S["p95"]),
     ("h", "三層迴圈的意義"),
     ("c", """for root_val in range(lo, hi + 1):      枚舉「誰當根」
    for left in build(lo, root_val-1):  左子樹的所有可能
        for right in build(root_val+1, hi):  右子樹的所有可能
            res.append(TreeNode(root_val, left, right))

這是一個【笛卡兒積】：
    每一個左子樹，都可以配上每一個右子樹。

    根 = 3，左邊用 {1,2} 有 2 種，右邊空有 1 種
    -> 2 × 1 = 2 種 ✔"""),
     ("h", "<code>[None]</code> vs <code>[]</code>"),
     ("c", """if lo > hi:
    return [None]        <- 一定是 [None]

寫成 [] 的話：
    for left in build(lo, root_val-1):     <- 空清單，迴圈不跑
        ...                                 <- 裡面的程式碼永遠不執行

    結果 res 永遠是空的 -> 答案是 [] ✘

[None] 的語意：
    「用『沒有任何數字』能建出的 BST，有一種 —— 就是空樹」

    這和「0! = 1」「空集合的子集有 1 個」是同一個慣例：
        「什麼都沒有」本身就是一種情況。

    也和第 70 題的 f(0) = 1、第 91 題的 dp[0] = 1 同源。

這是本題第一名的 bug。"""),
     ("h", "節點會被共用嗎？"),
     ("c", """會！而且【題目允許】。

    根 = 1 時，右子樹用 {2,3} 有兩種：
        2 -> 3（2 當根，3 當右子）
        3 -> 2（3 當根，2 當左子）

    這兩棵樹是獨立建出來的（各自 new 了節點），不共用。

    但如果 n 更大，例如根 = 1、右子樹用 {2,3,4}：
        build(2, 4) 回傳 5 棵樹
        每棵都被接到「同一個根節點 1」下面嗎？

        不是 —— 迴圈每次都 TreeNode(root_val, left, right)，
        每次都建一個【新的根節點】。

        但 left 和 right 【是共用的】！
        不同的根節點可能指向同一棵子樹物件。

    LeetCode 接受這樣的答案（它只檢查樹的結構）。

    如果要求「每棵樹完全獨立」，就得深複製 —— 但沒必要。"""),
     ("h", "複雜度"),
     "生成 <code>C(n)</code> 棵樹，每棵有 <code>n</code> 個節點 —— "
     "<strong>O(C(n) × n)</strong>，而 <code>C(n) ≈ 4ⁿ / n^1.5</code>。"
     "<strong>這已經是下界了</strong>（光是輸出就要這麼多）。",
   ], "O(C(n) × n)", "O(C(n) × n)", "C(n) 是第 n 個卡塔蘭數",
      "所有樹的節點", optimal=True),

   ap("解法二", "記憶化 + 平移（利用形狀的重複）", [
     "<strong>關鍵觀察：<code>build(1,3)</code> 和 <code>build(5,7)</code> "
     "產生的樹「形狀完全一樣」，只是每個值都差 4。</strong>"
     "所以只要算「長度為 k 的區間」的所有形狀，再整體平移。",
     ("c", S["p95_memo"]),
     ("c", """memo[length] = 「用 1..length 能建出的所有 BST」

    build(3) 的結果可以重複用在
        build(1,3)、build(2,4)、build(5,7)… 只要長度是 3

    但值要平移 —— 所以右子樹要 clone 並加上 offset。

節省了多少？
    原版：build(lo, hi) 對每一對 (lo, hi) 都算一次
          -> O(n²) 個不同的區間

    記憶化版：只對每個「長度」算一次
          -> O(n) 個不同的長度

    但代價是【每次使用都要 clone】（因為值不同）——
    而 clone 的成本和樹的大小成正比。

所以在這一題（n <= 8）記憶化【不一定更快】——
clone 的開銷可能抵銷掉省下的遞迴。

它的真正價值在於展示一個觀念：
    「不同的子問題，如果結構同構，就可以共用計算」

    這在「只要數量」的第 96 題就非常有用 ——
    那題不用 clone，記憶化的效果是決定性的。"""),
     "<strong>面試時寫解法一就好。</strong>"
     "這個版本當作「知道形狀可以共用」的展示。",
   ], "O(C(n) × n)", "O(C(n) × n)", "省下重複的遞迴，但多了 clone",
      "memo + 所有樹"),
 ],
 "compare": (["解法", "時間", "記憶化", "需要 clone？", "備註"],
   [["一、遞迴分治", "O(C(n)·n)", "✘", "✘", "面試預設，最清楚"],
    ["二、記憶化 + 平移", "O(C(n)·n)", "✔ 依長度", "✔", "展示「形狀同構」的觀念"]]),
 "edges": [
   "<strong>n = 1</strong> → 1 棵。",
   "<strong>n = 3</strong> → 5 棵。<strong>先數數量是最快的驗證。</strong>",
   "<strong>n = 8</strong> → 1430 棵。",
   "<strong>base case 寫成 <code>[]</code></strong>：答案永遠是空的。"
   "<strong>本題第一名的 bug。</strong>",
   "<strong>n = 0</strong>（題目不會給）：應該回 <code>[]</code>（沒有樹）"
   "而不是 <code>[None]</code>。"
   "<strong>注意這和 base case 的 <code>[None]</code> 語意不同</strong> —— "
   "「頂層要求 0 個節點」和「某個子樹是空的」是兩回事。",
   "<strong>驗證每棵樹</strong>：中序走訪必須是 <code>1, 2, ..., n</code>，"
   "而且必須真的滿足 BST 的性質。",
   "<strong>驗證沒有重複</strong>：把樹序列化成字串放進 set，數量要和卡塔蘭數相同。",
 ],
 "follow": [
   ("h", "追問一：如果只要「有幾棵」呢？"),
   "第 96 題。<strong>不用真的建樹，只要算卡塔蘭數</strong> —— O(n²) 的 DP 或 O(n) 的公式。"
   "<strong>「數出來」和「列出來」的複雜度差距是天文數字</strong>："
   "n = 19 時卡塔蘭數是 1767263190，"
   "數出來只要幾微秒，列出來則完全不可能。",
   ("h", "追問二：為什麼答案是卡塔蘭數？"),
   ("c", """f(n) = Σ_{k=1..n} f(k-1) × f(n-k)

    k 當根 -> 左子樹用 k-1 個節點，右子樹用 n-k 個節點

而卡塔蘭數的標準遞迴式是：
    C(n) = Σ_{i=0..n-1} C(i) × C(n-1-i)

    把 i = k-1 代入就一模一樣 ✔

第 22 題（括號生成）的遞迴式：
    「第一對括號裡面有 i 對、後面有 n-1-i 對」
    -> 同一個式子 ✔

所以【括號序列】和【二元樹】之間存在一一對應：
    每個合法的括號序列  <->  一棵二元樹

    "(" = 往下走進左子樹
    ")" = 回到父節點

    這叫做「樹的括號表示法」，
    也是 DFS 走訪的自然編碼。

卡塔蘭數出現在超過 200 種組合結構裡 ——
它們之所以答案相同，都是因為底層有這個相同的遞迴分解。""",),
   ("h", "追問三：如果數字不是 1..n 而是任意的呢？"),
   "只要它們<strong>互不相同</strong>，答案的<strong>數量</strong>就一樣"
   "（形狀由「有幾個節點」決定，和具體的值無關）。"
   "只要先排序，然後把 <code>1..n</code> 換成「排序後的陣列」即可。",
   ("h", "追問四：如果要「所有二元樹」（不要求是 BST）呢？"),
   "<strong>數量會變成 <code>C(n) × n!</code></strong> —— "
   "因為形狀有 <code>C(n)</code> 種，而每種形狀可以填入 <code>n!</code> 種數值排列。",
   "<strong>BST 的限制「消滅」了所有的排列自由度</strong> —— "
   "一旦形狀確定了，每個位置放什麼數字也就唯一確定了（由中序必須遞增決定）。"
   "<strong>這是 BST 一個很優雅的性質。</strong>",
 ],
 "related": [
   "<strong>第 96 題 Unique Binary Search Trees</strong> —— 只要數量",
   "<strong>第 22 題 Generate Parentheses</strong> —— 同樣是卡塔蘭數",
   "<strong>第 98 題 Validate BST</strong> —— 驗證 BST 的性質",
   "<strong>第 241 題 Different Ways to Add Parentheses</strong> —— 同樣的「枚舉分割點」分治",
 ],
 "check": [
   "base case 為什麼是 <code>[None]</code> 而不是 <code>[]</code>？寫成 <code>[]</code> 會回傳什麼？",
   "為什麼「左右子樹的選擇是獨立的」？這造成了什麼運算（加法還是乘法）？",
   "n = 4 應該有幾棵樹？請用遞迴式算一遍。",
   "為什麼「BST 的形狀確定後，每個節點的值也唯一確定」？",
 ],
})
print("P95 written")

# ==================== 96. Unique Binary Search Trees ====================
S["p96_dp"] = '''class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] = 用 i 個節點能建出幾棵不同的 BST（就是卡塔蘭數）
        dp = [0] * (n + 1)
        dp[0] = 1                # 空樹算一種

        for i in range(1, n + 1):
            for k in range(1, i + 1):        # k 當根
                dp[i] += dp[k - 1] * dp[i - k]
                #        ^左子樹     ^右子樹

        return dp[n]'''

S["p96_formula"] = '''import math

class Solution:
    def numTrees(self, n: int) -> int:
        # 卡塔蘭數的封閉形式：C(n) = C(2n, n) / (n + 1)
        return math.comb(2 * n, n) // (n + 1)'''

S["p96_iter"] = '''class Solution:
    def numTrees(self, n: int) -> int:
        # 用遞推式 C(k+1) = C(k) * 2(2k+1) / (k+2) 逐步算，全程整數
        c = 1
        for k in range(n):
            c = c * 2 * (2 * k + 1) // (k + 2)
        return c'''

_p96 = [S.load(k) for k in ("p96_dp", "p96_formula", "p96_iter")]
_CAT96 = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012,
          742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190]
for n in range(0, 20):
    for sol in _p96:
        assert sol.numTrees(n) == _CAT96[n], ("P96", n, sol, sol.numTrees(n), _CAT96[n])
# 和第 95 題的實際生成結果對照
_g95 = S.load("p95")
for n in range(1, 8):
    assert len(_g95.generateTrees(n)) == _p96[0].numTrees(n), ("P96 vs P95", n)
print("P96 solutions OK")

emit({
 "num": 96, "slug": "unique-binary-search-trees",
 "en": [
   "Given an integer <code>n</code>, return <em>the number of structurally unique "
   "<strong>BST's</strong> (binary search trees) which has exactly </em><code>n</code><em> "
   "nodes of unique values from </em><code>1</code><em> to </em><code>n</code>.",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，"
   "回傳由 <code>1</code> 到 <code>n</code> 組成的<strong>結構不同</strong>的"
   "二元搜尋樹<strong>有幾棵</strong>。",
 ],
 "pre": [
   ("note", "和第 95 題的天壤之別", [
     ("c", """第 95 題：列出所有 BST      -> O(C(n) × n)，n <= 8
第 96 題：只要數量          -> O(n²) 或 O(n)，n <= 19

同一個遞迴結構，但「數出來」和「列出來」的成本差了幾個數量級。

    n = 19：
        列出來：1767263190 棵樹 × 19 個節點
                = 336 億個節點 -> 不可能

        數出來：19² = 361 次乘加 -> 幾微秒

【當你只需要「有幾種」時，千萬不要真的去生成它們。】
這是組合計數問題最重要的一課。"""),
     "<strong>答案就是卡塔蘭數 <code>C(n)</code></strong>："
     "1, 1, 2, 5, 14, 42, 132, 429, 1430, …",
   ]),
 ],
 "examples": """範例 1
  輸入：n = 3
  輸出：5

範例 2
  輸入：n = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 19",
 ],
 "mid": [
   ("note", "為什麼 n 只到 19？", [
     ("c", """C(19) = 1767263190  <  2^31 - 1 = 2147483647
C(20) = 6564120420  >  2^31 - 1   溢位！

所以 n <= 19 是為了讓答案裝得進 32 位元有號整數。

（和第 70 題的 n <= 45 是同一種考量。）

看到這種「奇怪的上限」，就該想到「應該是為了不溢位」。

Python 沒有這個問題，但題目要對所有語言公平。"""),
   ]),
 ],
 "idea": [
   ("c", """遞迴式（和第 95 題一模一樣，只是把「生成」換成「計數」）：

    選 k 當根：
        左子樹用 1..k-1     共 k-1 個節點   -> dp[k-1] 種
        右子樹用 k+1..n     共 n-k 個節點   -> dp[n-k] 種
        左右獨立 -> 相乘

    dp[n] = Σ_{k=1..n} dp[k-1] × dp[n-k]

    base：dp[0] = 1（空樹一種）

手算 n = 3：
    dp[0] = 1
    dp[1] = dp[0]×dp[0] = 1
    dp[2] = dp[0]×dp[1] + dp[1]×dp[0] = 1 + 1 = 2
    dp[3] = dp[0]×dp[2] + dp[1]×dp[1] + dp[2]×dp[0]
          = 2 + 1 + 2 = 5 ✔

注意 dp[i] 只和「節點的個數」有關，和「是哪些數字」無關 ——
這就是為什麼不需要二維的 dp[lo][hi]。"""),
 ],
 "approaches": [
   ap("解法一", "DP（最推薦，也最好講）", [
     ("c", S["p96_dp"]),
     "<strong>兩層迴圈、五行、O(n²)。</strong>"
     "n = 19 時只要 190 次乘加。",
     ("h", "為什麼 <code>dp</code> 只需要一維？"),
     ("c", """直覺上狀態應該是「用 lo..hi 這些數字有幾種」——
那是二維的 dp[lo][hi]。

但關鍵觀察：
    【答案只和「有幾個節點」有關，和「是哪些數字」無關】

    用 {1,2,3} 能建 5 棵
    用 {5,6,7} 也能建 5 棵（形狀完全一樣，只是值不同）

    因為 BST 的結構完全由「大小關係」決定，
    而 n 個相異數字的大小關係是固定的。

所以 dp[lo][hi] 可以壓縮成 dp[hi - lo + 1] ——
二維變一維 ✔

【發現「某個維度不影響答案」是壓縮 DP 狀態最常見的手法。】

第 95 題的解法二（記憶化 + 平移）用的是同一個觀察，
只是那裡因為要「真的建樹」，所以還得處理數值的平移。"""),
     ("h", "<code>dp[0] = 1</code>"),
     "「用 0 個節點能建幾棵樹」= 1（空樹）。"
     "<strong>設成 0 的話 <code>dp[1]</code> 就會是 0，整串都垮了。</strong>"
     "（和第 70、91、95 題的 base case 是同一個慣例。）",
   ], "O(n²)", "O(n)", "兩層迴圈", "dp 陣列", optimal=True),

   ap("解法二", "卡塔蘭數的封閉公式", [
     ("c", S["p96_formula"]),
     ("c", """C(n) = C(2n, n) / (n + 1)

驗算：
    C(3) = C(6,3) / 4 = 20 / 4 = 5 ✔
    C(4) = C(8,4) / 5 = 70 / 5 = 14 ✔
    C(5) = C(10,5) / 6 = 252 / 6 = 42 ✔

這個公式的一個漂亮證明是【反射原理（reflection principle）】：

    把「合法的括號序列」想成「從 (0,0) 走到 (2n, 0) 的路徑」，
    「(」是往右上走，「)」是往右下走。

    總路徑數 = C(2n, n)（選 n 步往上）
    不合法的（碰到 y = -1）路徑數 = C(2n, n-1)
        （把第一次碰到 y=-1 之後的部分「反射」，
          會一一對應到「從 (0,-2) 出發」的路徑）

    合法數 = C(2n, n) - C(2n, n-1) = C(2n, n) / (n+1) ✔

【要小心整數除法】：
    必須先算出完整的 C(2n, n) 再除以 n+1。
    先除會有餘數損失。

    math.comb 是精確的整數運算，所以安全 ✔"""),
     "<strong>O(n) 時間（<code>math.comb</code> 的成本），最快。</strong>",
     "<strong>但面試時不建議只寫這個</strong> —— "
     "它需要你「剛好知道」這個公式。"
     "<strong>先寫 DP（展示你能自己推導），再說「這其實是卡塔蘭數，有封閉公式」。</strong>",
   ], "O(n)", "O(1)", "組合數的計算", "幾個變數"),

   ap("解法三", "遞推公式（O(n)，全程整數）", [
     "卡塔蘭數還有一個<strong>相鄰兩項的遞推關係</strong>，可以一路乘除算上去。",
     ("c", S["p96_iter"]),
     ("c", """遞推式： C(k+1) = C(k) × 2(2k+1) / (k+2)

從 C(0) = 1 開始：
    k=0: c = 1 × 2×1 / 2 = 1        -> C(1) = 1 ✔
    k=1: c = 1 × 2×3 / 3 = 2        -> C(2) = 2 ✔
    k=2: c = 2 × 2×5 / 4 = 5        -> C(3) = 5 ✔
    k=3: c = 5 × 2×7 / 5 = 14       -> C(4) = 14 ✔
    k=4: c = 14 × 2×9 / 6 = 42      -> C(5) = 42 ✔

每一步的結果都是整數（因為它是卡塔蘭數），
所以 // 不會有精度損失。

【但乘法必須在除法之前】——
    c * 2 * (2k+1) // (k+2)   ✔
    c // (k+2) * 2 * (2k+1)   ✘ 會有餘數損失

這和第 62 題（手算組合數）的注意事項一樣。"""),
     "<strong>O(n) 時間、O(1) 空間、不需要 <code>math.comb</code></strong> —— "
     "在沒有組合數函式庫的語言裡，這是最好的選擇。",
     "<strong>而且中間值不會爆</strong>（最大就是答案本身），"
     "不像「先算 <code>(2n)!</code> 再除」會產生天文數字。",
   ], "O(n)", "O(1)", "n 次乘除", "一個變數"),
 ],
 "compare": (["解法", "時間", "空間", "要記公式？", "備註"],
   [["一、DP", "O(n²)", "O(n)", "✘ 可自己推導", "面試預設"],
    ["二、封閉公式", "O(n)", "O(1)", "✔", "最快，但要知道"],
    ["三、遞推", "O(n)", "O(1)", "✔", "不需要組合數函式庫"]]),
 "edges": [
   "<strong>n = 1</strong> → 1。",
   "<strong>n = 3</strong> → 5。",
   "<strong>n = 19</strong> → 1767263190（剛好在 <code>INT_MAX</code> 之內）。",
   "<strong>n = 0</strong>（題目不會給）→ 1（空樹）。三種解法都自然正確。",
   "<strong><code>dp[0]</code> 設成 0</strong>：整個 dp 都會是 0。",
   "<strong>公式版先除後乘</strong>：會有餘數損失，答案錯。",
   "<strong>用階乘直接算</strong>：<code>(2n)!</code> 在 n = 19 時是 38 位數 —— "
   "Python 撐得住但很慢，C/Java 早就溢位。",
 ],
 "follow": [
   ("h", "追問一：卡塔蘭數還出現在哪些地方？"),
   ("c", """C(n) 計算的東西（超過 200 種已知的組合結構）：

  n 對括號的合法序列數                    （第 22 題）
  n 個節點的不同二元樹形狀                 （本題）
  n+2 邊形的三角剖分方法數
  n×n 網格中不越過對角線的單調路徑數
  n 個元素用不同方式加括號的方法數          （第 241 題）
  長度 2n 的 Dyck path 數
  n 個元素的堆疊排序（stack-sortable）排列數

它們之所以答案相同，都是因為底層有相同的遞迴分解：
    「選一個『中心』，把問題切成左右兩個獨立的子問題」

    C(n) = Σ C(i) × C(n-1-i)

一旦你在某個問題裡認出這個分解，就知道答案是卡塔蘭數。""",),
   ("h", "追問二：為什麼 <code>dp</code> 可以只用一維？"),
   "因為<strong>答案只和「節點個數」有關，和「是哪些數字」無關</strong>。",
   "<strong>這個「發現某個維度是多餘的」的能力，是 DP 優化最核心的技巧</strong>：",
   ("ul", [
     "<strong>本題</strong>：<code>dp[lo][hi]</code> → <code>dp[hi-lo+1]</code>",
     "<strong>第 87 題</strong>：四維 <code>(i1,j1,i2,j2)</code> → 三維 <code>(length,i,j)</code>",
     "<strong>滾動陣列</strong>：<code>dp[i][j]</code> → <code>dp[j]</code>（因為只依賴上一列）",
   ]),
   ("h", "追問三：如果數字有重複呢？"),
   "「1..n 互不相同」是這題的關鍵前提。"
   "如果允許重複，BST 的定義本身就會有歧義"
   "（相等的值要放左邊還是右邊？），"
   "而且不同的放法會產生不同的結構 —— <strong>問題會複雜很多。</strong>",
   ("h", "追問四：如果要「第 k 棵樹」（字典序）呢？"),
   "用<strong>卡塔蘭數做 unranking</strong>："
   "在每個節點上，算出「選 1 當根有幾棵」、「選 2 當根有幾棵」…，"
   "然後根據 <code>k</code> 落在哪一段決定根是誰，再遞迴下去。",
   "<strong>和第 60 題（第 k 個排列）用階乘進位制是同一個技巧</strong> —— "
   "<strong>「有計數公式」就能「直接跳到第 k 個」，不用生成全部。</strong>",
 ],
 "related": [
   "<strong>第 95 題 Unique Binary Search Trees II</strong> —— 列出所有樹",
   "<strong>第 22 題 Generate Parentheses</strong> —— 同樣是卡塔蘭數",
   "<strong>第 241 題 Different Ways to Add Parentheses</strong> —— 同樣的分治結構",
   "<strong>第 70 題 Climbing Stairs</strong> —— 另一個經典的計數 DP",
 ],
 "check": [
   "為什麼 <code>dp</code> 只需要一維（節點個數）而不是二維（區間的左右端點）？",
   "<code>dp[0] = 1</code> 代表什麼？設成 0 會怎樣？",
   "n = 4 的答案是多少？請用遞迴式手算一遍。",
   "為什麼 n 的上限是 19？（提示：和 32 位元整數有關）",
 ],
})
print("P96 written")
