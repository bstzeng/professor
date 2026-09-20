# -*- coding: utf-8 -*-
"""第 101–104 題。"""
import random
from collections import deque
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(101)


def _build(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _build(l), _build(r))


def _rand_tree(n, lo=0, hi=4):
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi), _rand_tree(left, lo, hi), _rand_tree(n - 1 - left, lo, hi))


def _mirror(nd):
    return None if nd is None else TreeNode(nd.val, _mirror(nd.right), _mirror(nd.left))


def _enc(nd):
    return None if nd is None else (_enc(nd.left), nd.val, _enc(nd.right))


def _shape(nd):
    return "#" if nd is None else "(%s|%s)" % (_shape(nd.left), _shape(nd.right))


# ==================== 101. Symmetric Tree ====================
S["p101_rec"] = '''class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(a, b):
            """a 和 b 這兩棵子樹互為鏡像嗎？"""
            if not a and not b:
                return True                  # 兩邊都空 -> 對稱
            if not a or not b:
                return False                 # 只有一邊空 -> 不對稱
            return (a.val == b.val
                    and mirror(a.left, b.right)   # 左的左 對 右的右
                    and mirror(a.right, b.left))  # 左的右 對 右的左

        return mirror(root.left, root.right) if root else True'''

S["p101_iter"] = '''from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        dq = deque([(root.left, root.right)])   # 佇列裡放的是「該互為鏡像的一對」

        while dq:
            a, b = dq.popleft()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            dq.append((a.left, b.right))        # 交叉配對
            dq.append((a.right, b.left))

        return True'''

S["p101_level"] = '''from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        level = [root]
        while any(level):
            # 把這一層攤平成一個「值的列表」，空節點用 None 佔位
            vals = [nd.val if nd else None for nd in level]
            if vals != vals[::-1]:              # 這一層必須是回文
                return False

            nxt = []
            for nd in level:
                if nd:
                    nxt.append(nd.left)
                    nxt.append(nd.right)
            level = nxt

        return True'''


def _p101_ref(root):
    """獨立參考解：把樹整個鏡像一份，再比較是否相同。"""
    return _enc(root) == _enc(_mirror(root))


_p101 = [S.load(k) for k in ("p101_rec", "p101_iter", "p101_level")]

for spec, want in [
    ([1, [2, [3, None, None], [4, None, None]], [2, [4, None, None], [3, None, None]]], True),
    ([1, [2, None, [3, None, None]], [2, None, [3, None, None]]], False),
    ([1, None, None], True),
    ([1, [2, None, None], None], False),
    ([1, [2, None, None], [2, None, None]], True),
    ([1, [2, [3, None, None], None], [2, None, [3, None, None]]], True),
    ([1, [2, [3, None, None], None], [2, [3, None, None], None]], False),
    ([2, [3, [4, None, None], [5, None, None]], [3, [5, None, None], [4, None, None]]], True),
]:
    t = _build(spec)
    assert _p101_ref(t) is want, ("P101 ref", spec)
    for sol in _p101:
        assert sol.isSymmetric(_build(spec)) is want, ("P101", spec, sol)

for _ in range(5000):
    n = random.randrange(0, 9)
    t = _rand_tree(n, 0, 2)
    if random.random() < 0.4 and t:
        # 造一棵保證對稱的樹
        half = _rand_tree(random.randrange(0, 5), 0, 2)
        t = TreeNode(random.randint(0, 2), half, _mirror(half))
    want = _p101_ref(t)
    shape = _shape(t)
    for sol in _p101:
        got = sol.isSymmetric(t)
        assert got is want, ("P101 random", want, got, sol)
        assert _shape(t) == shape, ("P101 mutated", sol)
print("P101 solutions OK")

_P101_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">對稱 = 左右子樹互為【鏡像】。注意配對方式是交叉的：左的左 ↔ 右的右，左的右 ↔ 右的左。</text>
            <g font-size="14" text-anchor="middle">
              <circle cx="320" cy="62" r="19" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="320" y="67" fill="var(--gold)">1</text>
              <circle cx="220" cy="126" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="220" y="131" fill="var(--accent)">2</text>
              <circle cx="420" cy="126" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="420" y="131" fill="var(--accent)">2</text>
              <circle cx="160" cy="190" r="19" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="160" y="195" fill="#ff8a65">3</text>
              <circle cx="280" cy="190" r="19" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="280" y="195" fill="var(--gold)">4</text>
              <circle cx="360" cy="190" r="19" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="360" y="195" fill="var(--gold)">4</text>
              <circle cx="480" cy="190" r="19" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="480" y="195" fill="#ff8a65">3</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="306" y1="75" x2="234" y2="113"/><line x1="334" y1="75" x2="406" y2="113"/>
              <line x1="206" y1="139" x2="174" y2="177"/><line x1="234" y1="139" x2="266" y2="177"/>
              <line x1="406" y1="139" x2="374" y2="177"/><line x1="434" y1="139" x2="466" y2="177"/>
            </g>
            <path d="M 160 214 Q 320 268 480 214" fill="none" stroke="#ff8a65" stroke-width="1.5" stroke-dasharray="4 3"/>
            <path d="M 280 214 Q 320 240 360 214" fill="none" stroke="var(--gold)" stroke-width="1.5" stroke-dasharray="4 3"/>
            <text x="320" y="288" fill="var(--text-muted)" font-size="11" text-anchor="middle">虛線連起來的是「該互相比對」的一對</text>
            <line x1="20" y1="308" x2="620" y2="308" stroke="var(--border)"/>
            <text x="20" y="334" fill="var(--accent)" font-size="12">和第 100 題（Same Tree）的差別只有兩個字：</text>
            <text x="20" y="360" fill="var(--text-muted)" font-size="12">第 100 題：go(a.left, b.left) and go(a.right, b.right)　　　← 左對左、右對右</text>
            <text x="20" y="384" fill="var(--gold)" font-size="12">第 101 題：go(a.left, b.right) and go(a.right, b.left)　　　← 左對右、右對左</text>
            <text x="20" y="412" fill="#ff8a65" font-size="12">一模一樣的骨架，只改了配對方式。這就是「一個模板解一整類題」的意思。</text>'''

emit({
 "num": 101, "slug": "symmetric-tree",
 "en": [
   "Given the <code>root</code> of a binary tree, <em>check whether it is a mirror of itself</em> "
   "(i.e., symmetric around its center).",
   "<strong>Follow up:</strong> Could you solve it both recursively and iteratively?",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，判斷它是不是<strong>軸對稱</strong>的"
   "（也就是「自己和自己的鏡像相同」）。",
   "<strong>進階：</strong>你能同時寫出<strong>遞迴</strong>和<strong>迭代</strong>兩種解法嗎？",
 ],
 "pre": [
   ("note", "上一題的雙胞胎", [
     ("c", """第 100 題（Same Tree）問：「這兩棵樹相同嗎？」
第 101 題（本題）問：「這棵樹和它的鏡像相同嗎？」

    所以本題可以【直接用第 100 題的答案】：
        把樹鏡像一份，然後呼叫 isSameTree。

    但那要額外 O(n) 空間去建鏡像。

    更好的做法是【不要真的建鏡像】，
    而是在遞迴時就用「交叉」的方式配對：

        比較 a.left  和  b.right
        比較 a.right 和  b.left

    一個字都不用多寫，空間省下來了。

【這題真正在考的是：你有沒有看出「鏡像」就是「交叉配對」。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,2,2,3,4,4,3]

            1
           / \\
          2   2
         / \\ / \\
        3  4 4  3

  輸出：true

範例 2
  輸入：root = [1,2,2,null,3,null,3]

            1
           / \\
          2   2
           \\   \\
            3   3

  輸出：false
  說明：左子樹的 3 在右邊，右子樹的 3 也在右邊 ——
        要對稱的話，右子樹的 3 應該在左邊。""",
 "constraints": [
   "樹的節點數在 <code>[1, 1000]</code> 之間",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "idea": [
   ("fig", _P101_FIG, "0 0 640 430"),
   ("c", """定義一個輔助函式 mirror(a, b)：
    「a 和 b 這兩棵子樹，互為鏡像嗎？」

三個 base case（和第 100 題完全一樣）：
    1. not a and not b -> True
    2. not a or not b  -> False
    3. a.val != b.val  -> False

遞迴（【這裡是唯一的差別】）：
    mirror(a.left, b.right) and mirror(a.right, b.left)
              ^^^^^^^^^^^^^           ^^^^^^^^^^^^^^^^
              左的左 對 右的右          左的右 對 右的左

最外層呼叫 mirror(root.left, root.right)。

【為什麼不是 mirror(root, root)？】

    那樣會永遠回 True ——
    因為一棵樹和自己當然「值相同」，
    然後 mirror(root.left, root.right) 和
    mirror(root.right, root.left) 會被檢查兩次（互為對稱，所以結果一樣）。

    咦，那不是也對嗎？

    其實 mirror(root, root) 真的也會得到正確答案，
    只是多做了一倍的工作（每一對都被檢查兩次）。

    【寫 mirror(root.left, root.right) 比較乾淨，
      也比較能表達「根節點自己不用比」的意思。】"""),
 ],
 "approaches": [
   ap("解法一", "遞迴（標準答案）", [
     ("c", S["p101_rec"]),
     "<strong>五行，和第 100 題只差兩個字。</strong>",
     ("h", "手動走一遍範例 2"),
     ("c", """root = [1,2,2,null,3,null,3]

            1
           / \\
          2   2
           \\   \\
            3   3

mirror(左邊的 2, 右邊的 2)
    兩邊都在，2 == 2 ✔
    -> mirror(左2.left=None, 右2.right=3)  and  ...

    mirror(None, 3)
        not a and not b ？ b 在 -> 否
        not a or not b  ？ a 是 None -> 【是】 -> False ✔

    短路，答案 False ✔

【看出來了嗎：問題不在「值」，而在「位置」。
  兩個 3 的值一樣，但都掛在右邊，鏡像之後對不上。】"""),
     "<strong>時間 O(n)</strong>（每個節點最多被比一次）、"
     "<strong>空間 O(h)</strong>（遞迴堆疊）。",
   ], "O(n)", "O(h)", "每個節點看一次", "遞迴堆疊", optimal=True),

   ap("解法二", "迭代（佇列成對推進，滿足進階要求）", [
     ("c", S["p101_iter"]),
     ("h", "關鍵：佇列裡放的是「一對」，而且是交叉配對"),
     ("c", """dq.append((a.left,  b.right))
dq.append((a.right, b.left))

    和第 100 題的迭代版比較：

        第 100 題： (a.left, b.left) 和 (a.right, b.right)
        第 101 題： (a.left, b.right) 和 (a.right, b.left)

    【又是只改配對方式。】

    把 popleft() 換成 pop()（改成 DFS）答案也一樣 ——
    因為我們要檢查「每一對」，順序無所謂。""",),
     "<strong>沒有遞迴深度限制</strong>，"
     "而且<strong>可以提早結束</strong>（發現不對稱就立刻回 <code>False</code>）。",
     "<strong>空間 O(w)</strong>（w 是樹的最大寬度）。"
     "<strong>對完全二元樹來說這比遞迴版差</strong>，"
     "但它換到的是「不會 <code>RecursionError</code>」。",
   ], "O(n)", "O(w)", "每對節點一次", "佇列最大寬度"),

   ap("解法三", "層序走訪 + 檢查每層是否回文（想法很漂亮，但有坑）", [
     ("c", S["p101_level"]),
     ("h", "核心想法"),
     ("c", """如果一棵樹對稱，那麼【每一層從左到右讀，都應該是回文】。

        1
       / \\
      2   2
     / \\ / \\
    3  4 4  3

    第 0 層： [1]           回文 ✔
    第 1 層： [2, 2]        回文 ✔
    第 2 層： [3, 4, 4, 3]  回文 ✔

【但是空節點一定要用 None 佔位！】

    不佔位的話：

        1
       / \\
      2   2
       \\   \\
        3   3

    第 2 層如果只收集實際存在的節點 -> [3, 3] -> 是回文 -> 誤判成 True ✘

    佔位之後 -> [None, 3, None, 3] -> 不是回文 -> False ✔

    【這和第 100 題序列化解法「空節點記號不能省」是同一個道理：
      要唯一決定一棵樹，就必須記錄「洞」在哪裡。】"""),
     ("h", "<code>while any(level)</code> 而不是 <code>while level</code>"),
     "因為 <code>level</code> 裡會有 <code>None</code>。"
     "<strong>如果整層都是 <code>None</code>，代表已經走完了</strong>，"
     "<strong>寫成 <code>while level</code> 會無窮迴圈</strong>"
     "（一層 <code>None</code> 生出更多 <code>None</code>… 不對，"
     "實際上 <code>None</code> 不會產生子節點，所以下一層是空 list，"
     "但仍會多跑一輪無謂的檢查）。",
     "<strong>這個解法比較慢</strong>（每層都要建 list 和反轉），"
     "<strong>而且無法提早結束到很早</strong> —— "
     "<strong>面試時當成「另一種觀點」提一下就好，不要當主解。</strong>",
   ], "O(n)", "O(w)", "每層建一次 list", "一層的寬度"),
 ],
 "compare": (["解法", "時間", "空間", "遞迴？", "備註"],
   [["一、遞迴交叉配對", "O(n)", "O(h)", "✔", "標準答案，五行"],
    ["二、佇列成對推進", "O(n)", "O(w)", "✘", "滿足進階要求"],
    ["三、每層檢查回文", "O(n)", "O(w)", "✘", "想法漂亮，但空節點不能省"]]),
 "edges": [
   "<strong>單一節點</strong> <code>[1]</code> → <code>True</code>。",
   "<strong><code>[1,2,2,3,4,4,3]</code></strong> → <code>True</code>（官方範例 1）。",
   "<strong><code>[1,2,2,null,3,null,3]</code></strong> → <code>False</code>（官方範例 2）。"
   "<strong>結構不對稱，但值看起來很像 —— 這是本題的核心測資。</strong>",
   "<strong><code>[1,2,null]</code></strong> → <code>False</code>（只有左邊有孩子）。",
   "<strong><code>[1,2,2]</code></strong> → <code>True</code>。",
   "<strong>寫成 <code>mirror(a.left, b.left)</code></strong> → "
   "那是第 100 題（判斷相同），會把 <code>[1,2,2,null,3,null,3]</code> 誤判成 True。",
   "<strong>層序法忘了用 <code>None</code> 佔位</strong> → "
   "<code>[1,2,2,null,3,null,3]</code> 會誤判成 True。",
   "<strong>節點值有負數或 0</strong> → 用 <code>if not node.val</code> 判斷會爆炸，"
   "<strong>永遠用 <code>if not node</code></strong>。",
 ],
 "follow": [
   ("h", "追問一：如果只問「左右子樹的形狀對稱」，不管值呢？"),
   "<strong>把 <code>a.val != b.val</code> 那一行拿掉即可。</strong>"
   "剩下的邏輯完全不變。",
   ("h", "追問二：如果要「把樹變成對稱的最少修改次數」呢？"),
   "<strong>遞迴時不要提早回傳，而是累加「需要改幾個位置」</strong>：",
   ("c", """def cost(a, b):
    if not a and not b: return 0
    if not a or not b:  return float('inf')   # 結構不同 -> 改值救不了
    return ((a.val != b.val) + cost(a.left, b.right)
                             + cost(a.right, b.left))

如果允許「新增／刪除節點」，問題會變成樹的編輯距離 ——
那就難很多了（一般情況是 NP-hard，有序樹才有多項式解法）。""",),
   ("h", "追問三：如果是 N 元樹呢？"),
   "<strong>把「左對右」推廣成「第 i 個孩子對第 (k-1-i) 個孩子」</strong>"
   "（k 是孩子數量）：",
   ("c", """def mirror(a, b):
    if not a and not b: return True
    if not a or not b:  return False
    if a.val != b.val:  return False
    if len(a.children) != len(b.children): return False
    return all(mirror(x, y) for x, y in zip(a.children, reversed(b.children)))
                                                        ^^^^^^^^^^^^^^^^^^^^
                                                        關鍵：其中一邊要反過來"""),
   ("h", "追問四：能不能用「中序走訪是回文」來判斷？"),
   "<strong>不行 —— 這是個很有教育意義的錯誤想法。</strong>",
   ("c", """直覺：對稱的樹，中序走訪應該是回文吧？

反例：

        1
       / \\
      2   2

    中序： 2, 1, 2  -> 是回文 ✔ 而且樹確實對稱 ✔

但是：

        1
       / \\
      2   2
     /   /
    3   3

    中序： 3, 2, 1, 3, 2  -> 不是回文，樹也確實不對稱 ✔

看起來還行？再看這個：

        2
       / \\
      1   3
           \\
            1      <- 值故意安排過

    中序： 1, 2, 3, 1   -> 不是回文，也確實不對稱 ✔

真正的反例（中序是回文但樹不對稱）：

        1
       / \\
      1   1
     /     \\
    1       1

    中序： 1, 1, 1, 1, 1 -> 回文 ✔
    但左子樹的 1 掛左邊、右子樹的 1 掛右邊 -> 【確實對稱】✔

    嗯，這個剛好是對的。

【結論】：當所有值都相同時，中序永遠是回文，
    但樹的對稱性完全由【結構】決定 ——
    中序走訪【不記錄空節點】，所以它丟失了結構資訊。

    只要把空節點也輸出（用 # 佔位），
    「中序序列是回文」就真的等價於「樹對稱」了。

    這又回到同一個教訓：
    【要用序列表示樹，就必須記錄空節點。】"""),
 ],
 "related": [
   "<strong>第 100 題 Same Tree</strong> —— 同一個骨架，配對方式不同",
   "<strong>第 226 題 Invert Binary Tree</strong> —— 真的把樹鏡像過來",
   "<strong>第 951 題 Flip Equivalent Binary Trees</strong> —— 允許任意翻轉的版本",
   "<strong>第 102 題 Binary Tree Level Order Traversal</strong> —— 解法三用到的層序走訪",
 ],
 "check": [
   "和第 100 題相比，遞迴那一行改了什麼？為什麼這樣就是「鏡像」？",
   "層序解法為什麼一定要用 <code>None</code> 佔位？不佔位會在哪個測資掛掉？",
   "為什麼「中序走訪是回文」不能拿來判斷對稱？要怎麼補救？",
   "如果只比結構不比值，程式要怎麼改？",
 ],
})
print("P101 written")

# ==================== 102. Binary Tree Level Order Traversal ====================
S["p102_bfs"] = '''from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res, dq = [], deque([root])
        while dq:
            n = len(dq)                     # 【關鍵】先鎖住這一層的節點數
            level = []
            for _ in range(n):              # 只處理這 n 個，之後進來的屬於下一層
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(level)

        return res'''

S["p102_nodeq"] = '''class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            # 直接把整層換成下一層，連佇列都不用
            level = [kid for node in level for kid in (node.left, node.right) if kid]

        return res'''

S["p102_dfs"] = '''class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def go(node, depth):
            if not node:
                return
            if depth == len(res):           # 第一次抵達這個深度 -> 開一個新的桶
                res.append([])
            res[depth].append(node.val)
            go(node.left, depth + 1)        # 先左後右，所以桶裡的順序就是左到右
            go(node.right, depth + 1)

        go(root, 0)
        return res'''


def _p102_ref(root):
    """獨立參考解：先算出每個節點的深度，再依深度分組。"""
    out = {}
    def go(nd, d):
        if not nd:
            return
        out.setdefault(d, []).append(nd.val)
        go(nd.left, d + 1)
        go(nd.right, d + 1)
    go(root, 0)
    return [out[d] for d in sorted(out)]


_p102 = [S.load(k) for k in ("p102_bfs", "p102_nodeq", "p102_dfs")]

for spec, want in [
    ([3, [9, None, None], [20, [15, None, None], [7, None, None]]], [[3], [9, 20], [15, 7]]),
    ([1, None, None], [[1]]),
    (None, []),
    ([1, [2, None, None], None], [[1], [2]]),
]:
    assert _p102_ref(_build(spec)) == want, ("P102 ref", spec)
    for sol in _p102:
        assert sol.levelOrder(_build(spec)) == want, ("P102", spec, sol)

for _ in range(4000):
    t = _rand_tree(random.randrange(0, 12), -5, 5)
    want = _p102_ref(t)
    for sol in _p102:
        assert sol.levelOrder(t) == want, ("P102 random", want, sol)
print("P102 solutions OK")

_P102_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">BFS 的核心技巧：進入迴圈前先記下 len(queue)，那就是「這一層有幾個節點」。</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="320" cy="60" r="18" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="320" y="65" fill="var(--gold)">3</text>
              <circle cx="230" cy="120" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="230" y="125" fill="var(--accent)">9</text>
              <circle cx="410" cy="120" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="410" y="125" fill="var(--accent)">20</text>
              <circle cx="360" cy="180" r="18" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="360" y="185" fill="#ff8a65">15</text>
              <circle cx="460" cy="180" r="18" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="460" y="185" fill="#ff8a65">7</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="307" y1="73" x2="243" y2="107"/><line x1="333" y1="73" x2="397" y2="107"/>
              <line x1="397" y1="133" x2="373" y2="167"/><line x1="423" y1="133" x2="447" y2="167"/>
            </g>
            <line x1="20" y1="212" x2="620" y2="212" stroke="var(--border)"/>
            <text x="20" y="238" fill="var(--gold)" font-size="12">佇列的變化（方框內是佇列內容，n 是這一輪鎖住的數量）：</text>
            <text x="30" y="266" fill="var(--text-muted)" font-size="12">起始　　 [3]　　　　　　　　n = 1 → 取出 3，放入 9, 20　　　　收成 [3]</text>
            <text x="30" y="292" fill="var(--text-muted)" font-size="12">第 2 輪　 [9, 20]　　　　　　n = 2 → 取出 9, 20，放入 15, 7　　收成 [9, 20]</text>
            <text x="30" y="318" fill="var(--text-muted)" font-size="12">第 3 輪　 [15, 7]　　　　　　n = 2 → 取出 15, 7，沒有孩子　　　收成 [15, 7]</text>
            <text x="30" y="344" fill="var(--text-muted)" font-size="12">第 4 輪　 []　　　　　　　　 佇列空了 → 結束</text>
            <line x1="20" y1="366" x2="620" y2="366" stroke="var(--border)"/>
            <text x="20" y="392" fill="#ff8a65" font-size="12">如果沒有先鎖住 n，直接 while dq: node = dq.popleft()，你會拿到一條扁平的序列，</text>
            <text x="20" y="416" fill="#ff8a65" font-size="12">沒辦法知道「哪幾個屬於同一層」。那一行 n = len(dq) 就是全部的魔法。</text>'''

emit({
 "num": 102, "slug": "binary-tree-level-order-traversal",
 "en": [
   "Given the <code>root</code> of a binary tree, return <em>the level order traversal of its "
   "nodes' values</em>. (i.e., from left to right, level by level).",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，回傳它的<strong>層序走訪</strong>結果。",
   "也就是<strong>一層一層</strong>、每層<strong>由左到右</strong>，"
   "而且<strong>每一層各自裝成一個 list</strong>。",
 ],
 "pre": [
   ("note", "這題是 BFS 的「母題」", [
     ("c", """前面學過的走訪（第 94、144、145 題）都是【深度優先】——
一路往下走到底，再回頭。

這題是【廣度優先】——
把第 0 層走完，再走第 1 層，再走第 2 層。

    深度優先（DFS）用【堆疊】：後進先出 -> 一路鑽到底
    廣度優先（BFS）用【佇列】：先進先出 -> 一層一層擴散

【BFS 最重要的應用是「最短路徑」】——
因為它保證「先走到的一定比較近」。

    第 111 題（最小深度）、第 127 題（單詞接龍）、
    第 200 題（島嶼數量）、第 994 題（腐爛的橘子）
    用的都是這題的骨架。

    【這題本身不難，但它是後面幾十題的地基。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [3,9,20,null,null,15,7]

            3
           / \\
          9   20
             /  \\
            15   7

  輸出：[[3],[9,20],[15,7]]

範例 2
  輸入：root = [1]
  輸出：[[1]]

範例 3
  輸入：root = []
  輸出：[]""",
 "constraints": [
   "樹的節點數在 <code>[0, 2000]</code> 之間",
   "−1000 ≤ <code>Node.val</code> ≤ 1000",
 ],
 "mid": [
   ("note", "注意：節點數可以是 0", [
     "<strong>所以 <code>root</code> 可能是 <code>None</code>，答案是 <code>[]</code></strong>。"
     "<strong>忘了擋這個，<code>deque([root])</code> 會放進一個 <code>None</code>，"
     "然後 <code>node.val</code> 直接爆炸。</strong>",
   ]),
 ],
 "idea": [
   ("fig", _P102_FIG, "0 0 640 434"),
   ("c", """BFS 的標準骨架，只有一個技巧：

    dq = deque([root])
    while dq:
        n = len(dq)            ★★★ 這一行是全部的魔法 ★★★
        for _ in range(n):
            node = dq.popleft()
            <處理 node>
            把 node 的孩子放進 dq

【為什麼 n = len(dq) 就等於「這一層的節點數」？】

    因為在進入 for 迴圈之前，
    佇列裡【剛好就是完整的一層】——不多也不少。

    這是一個不變量（invariant）：
        「每次外層 while 開始時，dq 裡正好是某一層的全部節點。」

    證明：
        初始時 dq = [root]，正好是第 0 層 ✔
        處理完第 k 層的 n 個節點後，
        放進去的正好是它們所有的孩子 = 第 k+1 層的全部 ✔

    【能講出這個不變量，就代表你真的懂 BFS 了，
      而不只是背了一個模板。】"""),
 ],
 "approaches": [
   ap("解法一", "BFS + 鎖住層大小（標準答案）", [
     ("c", S["p102_bfs"]),
     ("h", "為什麼一定要用 <code>deque</code> 而不是 <code>list</code>？"),
     ("c", """Python 的 list.pop(0) 是 O(n)！

    因為它要把後面所有元素往前搬一格。

    用 list 當佇列：
        n 個節點 × 每次 O(n) 的搬移 = O(n²)

        n = 2000 時是 400 萬次搬移 —— 還撐得住，
        但在 n = 10⁵ 的題目（例如第 127、200 題）就會直接逾時。

    collections.deque 的 popleft() 是 O(1)（雙向鏈結串列實作）。

【這是 Python 刷題最常見的效能陷阱之一。】

    看到「佇列」就 from collections import deque，
    養成反射動作。

    （另一個常見陷阱：用字串相加拼接大量字串，
      應該用 list + "".join。）"""),
     ("h", "<code>if node.left</code> 而不是無條件 append"),
     "<strong>只把「存在的孩子」放進佇列</strong>。"
     "如果把 <code>None</code> 也放進去，下一輪 <code>node.val</code> 就會爆炸；"
     "而且 <code>n = len(dq)</code> 會算進不存在的節點，層的邊界就亂了。",
     "<strong>時間 O(n)</strong>（每個節點進出佇列各一次）、"
     "<strong>空間 O(w)</strong>（w 是最大寬度，完全二元樹時約 n/2）。",
   ], "O(n)", "O(w)", "每個節點進出佇列一次", "佇列最大寬度", optimal=True),

   ap("解法二", "整層替換（Python 最漂亮的寫法）", [
     ("c", S["p102_nodeq"]),
     ("h", "連佇列都不需要"),
     ("c", """既然每一輪要處理的就是「一整層」，
那乾脆直接用一個 list 存整層，然後【整個換成下一層】：

    level = [kid for node in level
                 for kid in (node.left, node.right) if kid]

    這一行讀作：
        「對 level 裡的每個 node，
          取它的 left 和 right，
          留下不是 None 的，組成新的 level。」

    巢狀生成式的順序和巢狀 for 迴圈一樣：

        for node in level:
            for kid in (node.left, node.right):
                if kid:
                    yield kid

    【左先右後的順序自動保證了「每層由左到右」。】

    完全不需要記 n = len(dq)，
    因為「這一層」本來就被獨立裝在一個 list 裡。"""),
     "<strong>四行解完，而且沒有那個容易忘記的 <code>n = len(dq)</code>。</strong>"
     "<strong>複雜度和解法一完全相同。</strong>",
     "<strong>面試時可以先寫解法一（展示你懂 BFS 的標準結構），"
     "再說「用 Python 的話我會這樣寫」。</strong>",
   ], "O(n)", "O(w)", "每個節點看一次", "一層的大小"),

   ap("解法三", "DFS + 深度當索引（證明「層序不一定要 BFS」）", [
     ("c", S["p102_dfs"]),
     ("h", "核心：用 <code>depth</code> 決定放進哪個桶"),
     ("c", """res[depth].append(node.val)

    每個節點知道自己在第幾層，就直接丟進對應的桶裡。

    if depth == len(res):
        res.append([])

    這一行在說：「第一次走到這個深度，先開一個空桶。」

    為什麼 depth 一定是「剛好等於」len(res) 而不會跳號？
        因為 DFS 是一層一層往下走的，
        要走到深度 d，一定先經過深度 d-1。
        所以桶是依序被開出來的 ✔

【為什麼每個桶裡的順序是「由左到右」？】

    因為我們永遠先遞迴 left 再遞迴 right。

    在同一層裡，比較靠左的節點，
    它的整條祖先路徑在 DFS 中一定比較早被走到 ——
    所以它比較早被 append 進桶裡 ✔

    【換成先 right 後 left，每層就會變成由右到左
      —— 那正是第 199 題（右視圖）的做法。】"""),
     "<strong>空間 O(h)</strong>（遞迴堆疊）—— "
     "<strong>對「深而窄」的樹，這比 BFS 的 O(w) 省</strong>。",
     "<strong>但對「淺而寬」的樹（例如完全二元樹）BFS 比較好。</strong>"
     "<strong>兩者沒有絕對優劣，看樹的形狀。</strong>",
   ], "O(n)", "O(h)", "每個節點看一次", "遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、BFS + 鎖層大小", "O(n)", "O(w)", "中", "標準答案，最通用"],
    ["二、整層替換", "O(n)", "O(w)", "短", "Python 最漂亮"],
    ["三、DFS + 深度索引", "O(n)", "O(h)", "中", "深而窄的樹比較省"]]),
 "post": [
   ("note", "這個 BFS 骨架能解的題目", [
     ("c", """dq = deque([root])
while dq:
    n = len(dq)
    for _ in range(n):
        node = dq.popleft()
        ...
        dq.append(孩子)

只要換掉「...」裡的邏輯：

  102  層序走訪            收集 node.val 成 list          （本題）
  103  鋸齒層序            奇數層把 list 反轉
  107  由下而上的層序      最後把整個結果反轉
  111  最小深度            第一次遇到葉節點就回傳層數
  116  填 next 指標        把同一層的節點串起來
  199  右視圖              每層只收最後一個
  515  每層最大值          每層取 max
  637  每層平均值          每層取平均

【八題共用一個骨架。這就是為什麼 BFS 值得背熟。】"""),
   ]),
 ],
 "edges": [
   "<strong><code>root = None</code></strong> → <code>[]</code>。"
   "<strong>沒擋的話 <code>None.val</code> 直接 crash —— 本題第一名的 bug。</strong>",
   "<strong>單一節點</strong> → <code>[[1]]</code>（注意是巢狀 list）。",
   "<strong>退化成一條鏈</strong>（每層只有一個節點）→ 2000 層，每層一個元素。"
   "<strong>DFS 版可能 <code>RecursionError</code>（Python 預設上限 1000）。</strong>",
   "<strong>完全二元樹</strong> → 最後一層約有 n/2 個節點，BFS 的空間是 O(n)。",
   "<strong>忘了 <code>n = len(dq)</code></strong> → 結果會是一條扁平的序列，分不出層。",
   "<strong>用 <code>list.pop(0)</code> 當佇列</strong> → O(n²)。"
   "本題 n ≤ 2000 還過得了，<strong>但養成這個習慣遲早會在大題目上逾時</strong>。",
   "<strong>把 <code>None</code> 也放進佇列</strong> → "
   "<code>n = len(dq)</code> 算錯，層的邊界全亂。",
 ],
 "follow": [
   ("h", "追問一：如果要「由下而上」呢？"),
   "<strong>第 107 題</strong>。最簡單的做法：<strong>正常做完，最後 <code>res[::-1]</code></strong>。",
   "<strong>不要用 <code>res.insert(0, level)</code></strong> —— "
   "<code>insert(0, ...)</code> 是 <code>O(len(res))</code>，"
   "整體變成 <code>O(h²)</code>。"
   "<strong>「先收集再反轉」永遠比「每次插到最前面」好</strong>，"
   "這在鏈結串列、字串、list 上都適用。",
   ("h", "追問二：如果要「鋸齒狀」（一層左到右、下一層右到左）呢？"),
   "<strong>第 103 題</strong>。<strong>在 <code>res.append(level)</code> 之前，"
   "奇數層先 <code>level.reverse()</code></strong>。",
   "<strong>也可以用 <code>deque</code> 從兩端 append</strong>，"
   "但<strong>「最後反轉」更簡單，而且複雜度相同</strong>"
   "（反轉一層是 O(該層大小)，全部加起來還是 O(n)）。",
   ("h", "追問三：如果是 N 元樹呢？"),
   ("c", """把「放 left 和 right」換成「放 children 裡的每一個」：

    for kid in node.children:
        dq.append(kid)

【N 元樹的 BFS 和二元樹一模一樣】——
BFS 根本不在乎每個節點有幾個孩子。

    這是 BFS 相對於「二元樹專屬遞迴」的一大優勢。

    第 429 題就是這題的 N 元樹版本。"""),
   ("h", "追問四：如果樹非常寬（例如 10⁷ 個葉節點），BFS 的記憶體撐不住怎麼辦？"),
   "<strong>改用 DFS（解法三）</strong> —— 它的空間是 <code>O(h)</code>，"
   "和寬度無關。",
   "<strong>但如果只是要「逐層輸出」而不用全部存起來</strong>，"
   "可以用<strong>迭代加深（IDDFS）</strong>："
   "對每個深度 <code>d = 0, 1, 2, ...</code> 做一次「只輸出深度 d」的 DFS。",
   "<strong>空間降到 O(h)，代價是時間變成 O(n·h)</strong> —— "
   "<strong>這是空間換時間的經典取捨</strong>，在<strong>記憶體受限的搜尋</strong>"
   "（例如西洋棋引擎）裡是標準手法。",
 ],
 "related": [
   "<strong>第 103 題 Zigzag Level Order</strong> —— 奇數層反轉",
   "<strong>第 107 題 Level Order Traversal II</strong> —— 最後整個反轉",
   "<strong>第 111 題 Minimum Depth</strong> —— BFS 找最短，第一個葉節點就是答案",
   "<strong>第 199 題 Right Side View</strong> —— 每層只取最後一個",
   "<strong>第 200 題 Number of Islands</strong> —— 同一個 BFS 骨架，換到格子圖上",
 ],
 "check": [
   "<code>n = len(dq)</code> 為什麼剛好等於「這一層的節點數」？請說出那個不變量。",
   "為什麼要用 <code>deque</code> 而不是 <code>list</code>？<code>list.pop(0)</code> 的複雜度是多少？",
   "DFS 版為什麼每個桶裡的順序自動是「由左到右」？",
   "「由下而上」為什麼要用「最後反轉」而不是 <code>insert(0, ...)</code>？",
 ],
})
print("P102 written")

# ==================== 103. Binary Tree Zigzag Level Order Traversal ====================
S["p103_reverse"] = '''from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res, dq, left_to_right = [], deque([root]), True
        while dq:
            n = len(dq)
            level = []
            for _ in range(n):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            res.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right     # 每層翻一次方向

        return res'''

S["p103_deque"] = '''from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res, dq, left_to_right = [], deque([root]), True
        while dq:
            n = len(dq)
            level = deque()                       # 這一層用雙端佇列收集
            for _ in range(n):
                node = dq.popleft()
                if left_to_right:
                    level.append(node.val)        # 從尾端加
                else:
                    level.appendleft(node.val)    # 從頭端加 -> 自動反轉
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            res.append(list(level))
            left_to_right = not left_to_right

        return res'''

S["p103_dfs"] = '''class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def go(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append([])
            # 奇數層從頭端插入，效果等於反轉
            if depth % 2 == 0:
                res[depth].append(node.val)
            else:
                res[depth].insert(0, node.val)
            go(node.left, depth + 1)
            go(node.right, depth + 1)

        go(root, 0)
        return res'''


def _p103_ref(root):
    lv = _p102_ref(root)
    return [row if i % 2 == 0 else row[::-1] for i, row in enumerate(lv)]


_p103 = [S.load(k) for k in ("p103_reverse", "p103_deque", "p103_dfs")]

for spec, want in [
    ([3, [9, None, None], [20, [15, None, None], [7, None, None]]], [[3], [20, 9], [15, 7]]),
    ([1, None, None], [[1]]),
    (None, []),
]:
    assert _p103_ref(_build(spec)) == want, ("P103 ref", spec)
    for sol in _p103:
        assert sol.zigzagLevelOrder(_build(spec)) == want, ("P103", spec, sol)

for _ in range(4000):
    t = _rand_tree(random.randrange(0, 12), -5, 5)
    want = _p103_ref(t)
    for sol in _p103:
        assert sol.zigzagLevelOrder(t) == want, ("P103 random", want, sol)
print("P103 solutions OK")

emit({
 "num": 103, "slug": "binary-tree-zigzag-level-order-traversal",
 "en": [
   "Given the <code>root</code> of a binary tree, return <em>the zigzag level order traversal "
   "of its nodes' values</em>. (i.e., from left to right, then right to left for the next "
   "level and alternate between).",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，回傳它的<strong>鋸齒層序走訪</strong>結果。",
   "也就是<strong>第一層由左到右、第二層由右到左、第三層又由左到右</strong>，"
   "如此交替。",
 ],
 "pre": [
   ("note", "第 102 題加一個 flag，就這樣", [
     ("c", """這題完全是第 102 題（層序走訪）的延伸。

    唯一的新東西：一個記錄「這一層的方向」的布林變數。

【重要觀念：不要去改變 BFS 的推進方式。】

    很多人第一直覺是「那我這一層從右邊開始放孩子」——
    這會讓 BFS 的邏輯變得很亂，而且容易錯。

    【正確的想法】：
        BFS 永遠用同一個方向推進（左先右後），
        只在【輸出這一層時】決定要不要反轉。

    「走訪的順序」和「輸出的順序」是兩件事 ——
    把它們分開，程式就會非常乾淨。

    這個「先照標準做，最後再調整輸出」的思路，
    在第 107 題（由下而上）也是一樣的。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [3,9,20,null,null,15,7]

            3
           / \\
          9   20
             /  \\
            15   7

  輸出：[[3],[20,9],[15,7]]

  說明：第 0 層（3）      由左到右 -> [3]
        第 1 層（9, 20）  由右到左 -> [20, 9]
        第 2 層（15, 7）  由左到右 -> [15, 7]

範例 2
  輸入：root = [1]
  輸出：[[1]]

範例 3
  輸入：root = []
  輸出：[]""",
 "constraints": [
   "樹的節點數在 <code>[0, 2000]</code> 之間",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "idea": [
   ("c", """把第 102 題的骨架照抄，只加兩行：

    left_to_right = True                       # 1) 宣告方向

    while dq:
        n = len(dq)
        level = []
        for _ in range(n):
            ...完全不變...

        res.append(level if left_to_right else level[::-1])
        left_to_right = not left_to_right      # 2) 每層翻面

【注意 BFS 內部一個字都沒改。】

    孩子還是「先 left 再 right」放進佇列，
    所以 level 收集到的永遠是「由左到右」。

    要輸出「由右到左」時，就把它反轉一下。

複雜度的疑慮：
    「每層都反轉一次，會不會變成 O(n²)？」

    不會。
    反轉一層的成本是 O(該層的大小)，
    所有層加起來 = O(所有節點) = O(n) ✔

    【總量分析（不是單次分析）才是對的思考方式。】"""),
 ],
 "approaches": [
   ap("解法一", "BFS + 奇數層反轉（最推薦）", [
     ("c", S["p103_reverse"]),
     "<strong>第 102 題的程式碼 + 兩行。</strong>"
     "面試時這是最好的答案 —— <strong>因為它一眼就看得出「這是層序走訪的變形」</strong>。",
     ("h", "<code>level[::-1]</code> 還是 <code>level.reverse()</code>？"),
     ("c", """level[::-1]      建立一個新的反轉 list（O(k) 時間、O(k) 空間）
level.reverse()  原地反轉，不回傳值（O(k) 時間、O(1) 額外空間）

    這裡兩個都可以，因為 level 本來就要被放進 res。

    但要注意 reverse() 【回傳 None】：

        res.append(level.reverse())    ✘ 會 append 一個 None！
        level.reverse(); res.append(level)   ✔

    【這是 Python 初學者的經典陷阱】——
    sort()、reverse()、append() 都是「原地修改、回傳 None」，
    而 sorted()、reversed()、list[::-1] 才會回傳新東西。"""),
     "<strong>用 <code>not left_to_right</code> 翻面，不要用 <code>depth % 2</code></strong> —— "
     "<strong>少一個要維護的變數，也少一個算錯的機會。</strong>",
   ], "O(n)", "O(w)", "反轉的總成本也是 O(n)", "佇列最大寬度", optimal=True),

   ap("解法二", "用雙端佇列收集，省掉反轉", [
     ("c", S["p103_deque"]),
     ("h", "想法：與其事後反轉，不如一開始就放對位置"),
     ("c", """level 用 deque，然後：

    由左到右的層： append(val)      從尾端加 -> 順序就是左到右
    由右到左的層： appendleft(val)  從頭端加 -> 自動變成右到左

    deque 的兩端插入都是 O(1)，
    所以完全沒有反轉的成本。

【但這真的比較快嗎？】

    理論上：省下了「反轉」這一步。
    實務上：【通常反而比較慢】——

        deque 的 appendleft 常數比 list 的 append 大，
        而 Python 的 list[::-1] 是用 C 實作的，非常快。

    【這是一個很好的提醒：
      「理論上更優」不等於「實際上更快」，
      尤其是在有大量 C 層優化的語言裡。】

    面試時提到這個對照會很加分 ——
    它展示你知道複雜度分析的極限。"""),
     "<strong>不過 <code>appendleft</code> 這個想法本身很有價值</strong> —— "
     "在<strong>其他語言</strong>（沒有快速切片反轉）或"
     "<strong>需要邊產生邊輸出（串流）</strong>的場景，它是對的選擇。",
   ], "O(n)", "O(w)", "沒有反轉成本", "佇列最大寬度"),

   ap("解法三", "DFS + 奇數層 insert(0)（有效能陷阱）", [
     ("c", S["p103_dfs"]),
     "<strong>能動，但 <code>list.insert(0, x)</code> 是 O(k)。</strong>",
     ("c", """對一層有 k 個節點的情況：

    每次 insert(0, ...) 要把已有的元素往後搬一格 -> O(k)
    做 k 次 -> O(k²)

    最後一層可能有 n/2 個節點 -> O(n²)

    n = 2000 時：(1000)² = 100 萬 —— 還過得了，
    但這是「碰巧過關」，不是好解法。

【怎麼修？】

    改成：一律 append，最後統一把奇數層反轉。

        res[depth].append(node.val)
        ...
        return [row if i % 2 == 0 else row[::-1]
                for i, row in enumerate(res)]

    這樣就是乾淨的 O(n) 了。

【教訓：在 list 的「頭部」做插入或刪除，
  幾乎永遠是效能陷阱。
  正確的反射是「先 append，最後反轉」。】""",),
     "<strong>放在這裡是為了示範這個陷阱</strong> —— "
     "<strong>實際面試請寫解法一。</strong>",
   ], "O(n²) 最壞", "O(h)", "insert(0) 是 O(k)", "遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、BFS + 反轉", "O(n)", "O(w)", "最推薦，第 102 題 + 兩行"],
    ["二、雙端佇列", "O(n)", "O(w)", "想法好，但 Python 下不見得快"],
    ["三、DFS + insert(0)", "O(n²) 最壞", "O(h)", "示範效能陷阱，不要用"]]),
 "edges": [
   "<strong><code>root = None</code></strong> → <code>[]</code>。",
   "<strong>單一節點</strong> → <code>[[1]]</code>（第 0 層不反轉）。",
   "<strong>只有兩層</strong> <code>[1,2,3]</code> → <code>[[1],[3,2]]</code>。"
   "<strong>第 1 層要反轉 —— 忘了從第 0 層開始算會整個反過來。</strong>",
   "<strong>把 <code>res.append(level.reverse())</code> 寫錯</strong> → "
   "<code>reverse()</code> 回傳 <code>None</code>，結果會是 <code>[None, None, ...]</code>。",
   "<strong>方向的起點搞錯</strong>（從第 0 層就反轉）→ 整個答案左右顛倒。",
   "<strong>試圖改變 BFS 放孩子的順序</strong> → 邏輯會非常亂，而且下一層的順序也跟著錯。",
   "<strong>用 <code>insert(0, ...)</code></strong> → 寬樹上退化成 O(n²)。",
 ],
 "follow": [
   ("h", "追問一：如果要「每三層換一次方向」呢？"),
   "<strong>把 <code>not left_to_right</code> 換成 <code>depth // 3 % 2 == 1</code> 的判斷</strong>。"
   "<strong>核心結構完全不用動</strong> —— "
   "<strong>這就是「走訪」和「輸出」分離的好處：改需求只要改一行。</strong>",
   ("h", "追問二：如果要「螺旋輸出」（由外往內繞圈）呢？"),
   "<strong>那是矩陣題（第 54 題 Spiral Matrix），不是樹題。</strong>"
   "樹沒有「外圈」的概念 —— <strong>「鋸齒」和「螺旋」是兩個不同的東西</strong>，"
   "英文題目用 zigzag 而不是 spiral 就是在區分這個。",
   ("h", "追問三：如果不用額外的 flag，能不能判斷方向？"),
   "<strong>可以，用 <code>len(res) % 2</code></strong> —— "
   "<code>res</code> 目前有幾層，就代表正要處理第幾層。",
   "<strong>但額外的 <code>flag</code> 更清楚</strong>，"
   "而且<strong>不依賴「<code>res</code> 一定是逐層 append」這個隱含前提</strong>。"
   "<strong>少用隱含狀態，程式比較不容易在改需求時壞掉。</strong>",
   ("h", "追問四：為什麼「每層反轉」不會讓總複雜度變成 O(n²)？"),
   ("c", """反轉第 k 層的成本 = O(第 k 層的節點數)

    總成本 = Σ_k O(第 k 層的節點數)
           = O(Σ_k 第 k 層的節點數)
           = O(所有節點的總數)
           = O(n) ✔

【這叫做「總量分析」（aggregate analysis），
  是攤還分析最簡單的一種形式。】

    常見的誤判：
        「迴圈裡有一個 O(k) 的操作 -> 一定是 O(n·k)」

    但如果那些 k 加起來剛好是 n，
    總成本就還是 O(n)。

    第 99 題的 Morris 走訪、
    第 84 題的單調堆疊、
    這裡的每層反轉 ——
    都是同一種分析方式。"""),
 ],
 "related": [
   "<strong>第 102 題 Level Order Traversal</strong> —— 本題的基礎",
   "<strong>第 107 題 Level Order Traversal II</strong> —— 另一種「輸出時再調整」",
   "<strong>第 199 題 Right Side View</strong> —— 每層只取一個",
   "<strong>第 54 題 Spiral Matrix</strong> —— 真正的「螺旋」（矩陣版）",
 ],
 "check": [
   "為什麼 BFS 內部不需要改變放孩子的順序？",
   "<code>level.reverse()</code> 和 <code>level[::-1]</code> 有什麼差別？哪一個不能直接 append？",
   "「每層都反轉」為什麼總複雜度還是 O(n)？請用總量分析說明。",
   "DFS 版用 <code>insert(0, ...)</code> 為什麼在寬樹上會退化？要怎麼修？",
 ],
})
print("P103 written")

# ==================== 104. Maximum Depth of Binary Tree ====================
S["p104_rec"] = '''class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0                    # 空樹深度 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        #      ^ 自己這一層'''

S["p104_bfs"] = '''from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth, dq = 0, deque([root])
        while dq:
            depth += 1                  # 每處理完一層就加一
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return depth'''

S["p104_stack"] = '''class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        best, stack = 0, [(root, 1)]    # 堆疊裡放 (節點, 它的深度)
        while stack:
            node, d = stack.pop()
            best = max(best, d)
            if node.left:
                stack.append((node.left, d + 1))
            if node.right:
                stack.append((node.right, d + 1))

        return best'''


def _p104_ref(root):
    return 0 if root is None else 1 + max(_p104_ref(root.left), _p104_ref(root.right))


_p104 = [S.load(k) for k in ("p104_rec", "p104_bfs", "p104_stack")]

for spec, want in [
    ([3, [9, None, None], [20, [15, None, None], [7, None, None]]], 3),
    ([1, None, [2, None, None]], 2),
    (None, 0),
    ([1, None, None], 1),
]:
    assert _p104_ref(_build(spec)) == want, ("P104 ref", spec)
    for sol in _p104:
        assert sol.maxDepth(_build(spec)) == want, ("P104", spec, sol)

for _ in range(5000):
    t = _rand_tree(random.randrange(0, 14), -5, 5)
    want = _p104_ref(t)
    # 用第 102 題的層序結果交叉驗證：層數就是深度
    assert len(_p102_ref(t)) == want, "P104 cross-check"
    for sol in _p104:
        assert sol.maxDepth(t) == want, ("P104 random", want, sol)
print("P104 solutions OK")

emit({
 "num": 104, "slug": "maximum-depth-of-binary-tree",
 "en": [
   "Given the <code>root</code> of a binary tree, return <em>its maximum depth</em>.",
   "A binary tree's <strong>maximum depth</strong> is the number of nodes along the longest "
   "path from the root node down to the farthest leaf node.",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，回傳它的<strong>最大深度</strong>。",
   "二元樹的<strong>最大深度</strong>，是從根節點到<strong>最遠的葉節點</strong>"
   "那條路徑上的<strong>節點個數</strong>。",
   ("note", "注意是「節點數」不是「邊數」", [
     ("c", """        1
       /
      2

    節點數： 2  <- LeetCode 這題要的是這個
    邊數：   1

【空樹的深度是 0，單一節點的深度是 1。】

    這個定義在不同教科書裡不一樣（有些用邊數），
    所以【面試時一定要先確認】。

    本題的定義讓遞迴特別漂亮：
        depth(空) = 0
        depth(節點) = 1 + max(左, 右)

    如果用邊數，base case 就要處理葉節點，麻煩很多。"""),
   ]),
 ],
 "pre": [
   ("note", "樹遞迴模板的最小範例", [
     ("c", """幾乎所有樹的遞迴題都長這樣：

    def go(node):
        if not node:                  # 1. 空節點的答案是什麼？
            return <base 值>
        left  = go(node.left)         # 2. 問左子樹
        right = go(node.right)        # 3. 問右子樹
        return <用 left / right 組出自己的答案>   # 4. 合併

本題填進去：
    1. 空節點 -> 0
    4. 1 + max(left, right)

    就這樣，三行。

【如果你覺得樹的遞迴很難，就從這一題開始。
  它把模板剝到只剩骨頭。】

    第 110 題（平衡二元樹）、第 111 題（最小深度）、
    第 124 題（最大路徑和）、第 543 題（直徑）——
    全部都是在第 4 步「合併」那裡做文章。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [3,9,20,null,null,15,7]

            3           <- 第 1 層
           / \\
          9   20        <- 第 2 層
             /  \\
            15   7      <- 第 3 層

  輸出：3

範例 2
  輸入：root = [1,null,2]
  輸出：2""",
 "constraints": [
   "樹的節點數在 <code>[0, 10⁴]</code> 之間",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "mid": [
   ("note", "節點數上限 10⁴ 是個訊號", [
     "<strong>如果樹退化成一條鏈，遞迴深度會是 10⁴</strong>。",
     "<strong>Python 預設的遞迴上限是 1000</strong>，"
     "所以理論上會 <code>RecursionError</code>。",
     "<strong>實務上 LeetCode 的測資不會給這麼極端的樹</strong>，"
     "但<strong>面試時主動提出「如果樹很深我會改用迭代」會加分</strong>。"
     "解法二和解法三就是為此準備的。",
   ]),
 ],
 "idea": [
   ("c", """遞迴的定義幾乎就是題目的中文翻譯：

    「最大深度」= 1（我自己） + max(左子樹的最大深度, 右子樹的最大深度)

    base case：空樹的深度是 0

驗算範例 1：

            3
           / \\
          9   20
             /  \\
            15   7

    depth(15) = 1 + max(0, 0) = 1
    depth(7)  = 1 + max(0, 0) = 1
    depth(20) = 1 + max(1, 1) = 2
    depth(9)  = 1 + max(0, 0) = 1
    depth(3)  = 1 + max(1, 2) = 3 ✔

【這題的價值不在難度，而在它示範了
  「把遞迴定義直接寫成程式」這件事。】

    很多人寫樹的遞迴會想「我要怎麼走訪」，
    然後就卡住了。

    正確的思路是：
        「假設左右子樹的答案我已經有了，
          我要怎麼用它們算出自己的答案？」

    這叫做【遞迴的信心跳躍】（leap of faith）——
    不要去追蹤遞迴怎麼展開，
    只要相信子問題會給你正確答案就好。"""),
 ],
 "approaches": [
   ap("解法一", "遞迴（三行）", [
     ("c", S["p104_rec"]),
     "<strong>沒有比這更短的了。</strong>",
     ("h", "一行版（能寫但不建議）"),
     ("c", """return 1 + max(self.maxDepth(root.left),
               self.maxDepth(root.right)) if root else 0

    可以壓成一行，但【可讀性變差】。

    面試時寫三行版，
    然後說「可以壓成一行，但我覺得這樣比較清楚」——
    這比直接寫一行版更能展示判斷力。"""),
     ("h", "複雜度"),
     ("c", """時間 O(n)：每個節點恰好被呼叫一次。

空間 O(h)：遞迴堆疊的深度 = 樹高。

    平衡樹：  h = log n     -> O(log n)
    一條鏈：  h = n         -> O(n)

    【「空間 O(h)」是所有樹遞迴的共同答案，
      面試時不要說 O(1)。】"""),
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊", optimal=True),

   ap("解法二", "BFS 數層數", [
     ("c", S["p104_bfs"]),
     "<strong>直接把第 102 題的骨架拿來用</strong> —— "
     "<strong>「最大深度」就是「層序走訪有幾層」</strong>。",
     ("c", """這個等價關係值得記住：

    最大深度 = 層序走訪的層數 = BFS 跑了幾輪

    所以第 102 題的答案 len(res)，就是這題的答案。

【什麼時候 BFS 比遞迴好？】

    ✔ 樹很深（避免 RecursionError）
    ✔ 只想知道「前 k 層」（可以提早停）
    ✔ 要找【最小】深度（第 111 題）——
        BFS 遇到第一個葉節點就能停，
        遞迴版則必須走完整棵樹

    ✘ 樹很寬（佇列吃掉 O(w) 記憶體）

    【第 111 題是 BFS 完勝的例子，
      這一題則是遞迴完勝（三行 vs 十行）。】"""),
     "<strong>空間 O(w)</strong>（最大寬度）。"
     "對完全二元樹是 <code>O(n/2)</code>，<strong>比遞迴版差</strong>。",
   ], "O(n)", "O(w)", "每個節點進出佇列一次", "佇列最大寬度"),

   ap("解法三", "DFS 迭代（堆疊裡存深度）", [
     ("c", S["p104_stack"]),
     ("h", "技巧：把「深度」和節點一起放進堆疊"),
     ("c", """stack.append((node.left, d + 1))

    遞迴版的「深度」是隱含在呼叫堆疊裡的，
    改成迭代時就要【自己把它帶著走】。

    這是「遞迴改迭代」的通用手法：
        【把所有遞迴參數打包成 tuple 放進堆疊。】

    遞迴： go(node.left, d + 1)
    迭代： stack.append((node.left, d + 1))

    一一對應。

【什麼時候需要這樣改？】

    ✔ 遞迴太深會爆堆疊
    ✔ 需要在中途暫停 / 序列化搜尋狀態
    ✔ 語言不支援深遞迴（或沒有尾呼叫優化）

    ✘ 其他時候 —— 遞迴版短很多，也好讀很多。"""),
     "<strong>空間 O(h)</strong>，和遞迴版相同（只是堆疊換了地方住）。",
     "<strong>注意這裡用 <code>pop()</code>（DFS）</strong>，"
     "改成 <code>popleft()</code> 就變成 BFS —— <strong>答案一樣，因為我們只取最大值</strong>。",
   ], "O(n)", "O(h)", "每個節點一次", "顯式堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、遞迴", "O(n)", "O(h)", "3", "標準答案"],
    ["二、BFS 數層", "O(n)", "O(w)", "12", "樹很深時用"],
    ["三、DFS 迭代", "O(n)", "O(h)", "10", "把深度打包進堆疊"]]),
 "post": [
   ("note", "這個模板的六個變形", [
     ("c", """104  最大深度        1 + max(左, 右)                    （本題）
111  最小深度        1 + min(左, 右)，但【單邊為空要特判】
110  是否平衡        回傳高度，同時檢查 |左-右| <= 1
543  直徑            答案 = max(左高 + 右高)，回傳 1 + max(左, 右)
124  最大路徑和      答案 = max(左 + 根 + 右)，回傳 根 + max(左, 右, 0)
226  翻轉二元樹      交換左右，然後遞迴

【注意 543 和 124 的共同結構】：

    「回傳給父節點的值」 ≠ 「答案」

    回傳的是「從我往下延伸的一條路徑」，
    答案則是「在我這裡左右接起來的一條路徑」。

    這兩件事必須分開，是這類題目最核心的觀念 ——
    第 124 題會把它講透。"""),
   ]),
 ],
 "edges": [
   "<strong><code>root = None</code></strong> → <code>0</code>。",
   "<strong>單一節點</strong> → <code>1</code>（不是 0 —— 本題用節點數）。",
   "<strong><code>[1,null,2]</code></strong> → <code>2</code>。"
   "<strong>單邊的樹：<code>max</code> 會自動取到有值的那邊，不用特判。</strong>"
   "<strong>（但第 111 題的 <code>min</code> 就不行，那裡必須特判。）</strong>",
   "<strong>退化成一條鏈</strong>（10⁴ 個節點）→ 遞迴版可能 <code>RecursionError</code>，"
   "改用解法二或三。",
   "<strong>完全二元樹</strong>（10⁴ 個節點）→ 深度只有約 14，但 BFS 的佇列會到 5000。",
   "<strong>把 base case 寫成 <code>return 1</code></strong> → 所有深度都多算一層。",
   "<strong>忘了 <code>1 +</code></strong> → 永遠回 0。",
 ],
 "follow": [
   ("h", "追問一：如果要「最小深度」呢？"),
   "<strong>第 111 題 —— 而且它不是把 <code>max</code> 換成 <code>min</code> 這麼簡單。</strong>",
   ("c", """        1
       /
      2

    如果直接寫 1 + min(左, 右)：
        min(depth(2), depth(None)) = min(1, 0) = 0
        -> 答案是 1  ✘

    但根節點【不是葉節點】，
    所以最小深度應該是 2（走到節點 2）。

【正確寫法必須特判「只有一邊有孩子」】：

    if not root.left:  return 1 + minDepth(root.right)
    if not root.right: return 1 + minDepth(root.left)
    return 1 + min(minDepth(root.left), minDepth(root.right))

【為什麼 max 不用特判而 min 要？】

    因為空子樹回傳 0，而 0 是「深度的最小值」——
    對 max 來說它是無害的單位元素（取最大時會被忽略），
    對 min 來說它會把答案直接拉到 0（吃掉正確答案）。

    【這個「0 對 max 無害、對 min 有害」的不對稱，
      是第 111 題唯一的考點。】"""),
   ("h", "追問二：如果要「所有葉節點的深度」呢？"),
   ("c", """def leaf_depths(node, d=1):
    if not node:
        return []
    if not node.left and not node.right:
        return [d]                      # 是葉節點
    return (leaf_depths(node.left, d + 1)
            + leaf_depths(node.right, d + 1))

    然後 max() 是本題、min() 是第 111 題、
    len() 是葉節點數、set() 大小為 1 代表所有葉節點同深度。

【「先算出完整資訊，再取想要的部分」比較通用，
  但比較慢（要建 list）。
  只要一個數字的話，直接遞迴算比較好。】""",),
   ("h", "追問三：如果是 N 元樹呢？"),
   ("c", """def maxDepth(root):
    if not root:
        return 0
    if not root.children:
        return 1                        # 沒有孩子 -> 就是葉節點
    return 1 + max(maxDepth(c) for c in root.children)

【注意要特判 children 為空】——
max() 對空序列會丟 ValueError。

    也可以寫成：
        return 1 + max((maxDepth(c) for c in root.children), default=0)

    default=0 是 Python 3.4+ 的參數，
    專門處理「空序列」的情況，很好用。

    第 559 題就是這題的 N 元樹版本。"""),
   ("h", "追問四：什麼是「樹的高度」？和深度一樣嗎？"),
   ("c", """【深度（depth）】：從【根】往下數 —— 根的深度是 0（或 1）
【高度（height）】：從【葉】往上數 —— 葉的高度是 0（或 1）

    對【整棵樹】而言，
        樹的高度 = 根節點的高度 = 最大深度

    所以這一題問「最大深度」和問「樹的高度」是同一件事。

    但對【單一節點】而言，深度和高度完全不同：

            A          A: 深度 0, 高度 2
           / \\
          B   C        B: 深度 1, 高度 1
         /             C: 深度 1, 高度 0
        D              D: 深度 2, 高度 0

【面試時如果題目說「高度」，先確認是從哪邊數、
  以及空樹算 0 還是 -1。這些慣例真的不統一。】"""),
 ],
 "related": [
   "<strong>第 111 題 Minimum Depth</strong> —— 不能直接把 max 換成 min",
   "<strong>第 110 題 Balanced Binary Tree</strong> —— 用高度判斷平衡",
   "<strong>第 543 題 Diameter of Binary Tree</strong> —— 「回傳值 ≠ 答案」的入門",
   "<strong>第 124 題 Binary Tree Maximum Path Sum</strong> —— 同上，但更難",
   "<strong>第 559 題 Maximum Depth of N-ary Tree</strong> —— N 元樹版",
 ],
 "check": [
   "空樹的深度為什麼是 0 而不是 1？這個 base case 如果寫錯會怎樣？",
   "為什麼 <code>max</code> 版不用特判「單邊為空」，<code>min</code> 版卻非特判不可？",
   "遞迴的空間複雜度是 O(h) 還是 O(n)？什麼時候兩者相同？",
   "「深度」和「高度」對單一節點來說有什麼不同？對整棵樹呢？",
 ],
})
print("P104 written")
