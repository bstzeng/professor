# -*- coding: utf-8 -*-
"""第 173、174、179、187 題。"""
import random, functools
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(173)


def _bt(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _bt(l), _bt(r))


def _rand_bst(vals):
    if not vals:
        return None
    k = random.randrange(len(vals))
    return TreeNode(vals[k], _rand_bst(vals[:k]), _rand_bst(vals[k + 1:]))


def _ino(nd):
    return [] if nd is None else _ino(nd.left) + [nd.val] + _ino(nd.right)


# ==================== 173. Binary Search Tree Iterator ====================
S["p173_stack"] = '''class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)           # 把最左邊那條路徑先壓進去

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()         # 堆疊頂就是「下一個最小的」
        self._push_left(node.right)     # 它的右子樹接手
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0'''

S["p173_list"] = '''class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # 最直白：先把整個中序走訪算出來
        self.vals = []
        self.i = 0

        def go(node):
            if not node:
                return
            go(node.left)
            self.vals.append(node.val)
            go(node.right)

        go(root)

    def next(self) -> int:
        v = self.vals[self.i]
        self.i += 1
        return v

    def hasNext(self) -> bool:
        return self.i < len(self.vals)'''

S["p173_gen"] = '''class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # 用產生器：Python 的 yield 天生就是「暫停的走訪」
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        self.it = inorder(root)
        self.nxt = next(self.it, None)      # 先預取一個，好實作 hasNext

    def next(self) -> int:
        v = self.nxt
        self.nxt = next(self.it, None)
        return v

    def hasNext(self) -> bool:
        return self.nxt is not None'''


_p173ns = [S.loadns(k) for k in ("p173_stack", "p173_list", "p173_gen")]

for spec in [
    [7, [3, None, None], [15, [9, None, None], [20, None, None]]],
    [1, None, None],
    None,
]:
    want = _ino(_bt(spec))
    for ns in _p173ns:
        it = ns["BSTIterator"](_bt(spec))
        got = []
        while it.hasNext():
            got.append(it.next())
        assert got == want, ("P173", spec, want, got)
        assert it.hasNext() is False

for _ in range(2500):
    n = random.randrange(0, 14)
    vals = sorted(random.sample(range(-60, 60), n))
    base = _rand_bst(vals)
    for ns in _p173ns:
        def clone(nd):
            return None if nd is None else TreeNode(nd.val, clone(nd.left), clone(nd.right))
        it = ns["BSTIterator"](clone(base))
        got = []
        # 隨機交錯呼叫 hasNext 和 next
        while True:
            if random.random() < 0.3:
                it.hasNext()
            if not it.hasNext():
                break
            got.append(it.next())
        assert got == vals, ("P173 random", vals, got)
print("P173 solutions OK")

_P173_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 把「中序走訪」拆成可以暫停的步驟：堆疊裡永遠放著「從根往下走到目前最左」的那條路徑。</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="150" cy="70" r="19" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="150" y="75" fill="var(--gold)">7</text>
              <circle cx="80" cy="134" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="80" y="139" fill="var(--accent)">3</text>
              <circle cx="230" cy="134" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="230" y="139" fill="var(--accent)">15</text>
              <circle cx="180" cy="198" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="180" y="203" fill="var(--accent)">9</text>
              <circle cx="285" cy="198" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="285" y="203" fill="var(--accent)">20</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="137" y1="83" x2="93" y2="121"/><line x1="163" y1="83" x2="217" y2="121"/>
              <line x1="216" y1="148" x2="194" y2="184"/><line x1="244" y1="148" x2="271" y2="184"/>
            </g>
            <text x="150" y="240" fill="var(--text-muted)" font-size="11" text-anchor="middle">中序：3, 7, 9, 15, 20</text>
            <line x1="360" y1="40" x2="360" y2="250" stroke="var(--border)"/>
            <text x="385" y="62" fill="var(--gold)" font-size="12" text-anchor="start">堆疊的變化（由底到頂）：</text>
            <text x="385" y="92" fill="var(--text-muted)" font-size="12" text-anchor="start">初始　　　　[7, 3]</text>
            <text x="385" y="118" fill="var(--accent)" font-size="12" text-anchor="start">next() → 3　[7]</text>
            <text x="385" y="144" fill="var(--accent)" font-size="12" text-anchor="start">next() → 7　[15, 9]　← 壓入 7 的右子樹的左路徑</text>
            <text x="385" y="170" fill="var(--accent)" font-size="12" text-anchor="start">next() → 9　[15]</text>
            <text x="385" y="196" fill="var(--accent)" font-size="12" text-anchor="start">next() → 15 [20]</text>
            <text x="385" y="222" fill="var(--gold)" font-size="12" text-anchor="start">next() → 20 []　→ hasNext() = False</text>
            <line x1="20" y1="272" x2="620" y2="272" stroke="var(--border)"/>
            <text x="20" y="300" fill="var(--accent)" font-size="13">★ 為什麼空間是 O(h) 而不是 O(n)？</text>
            <text x="40" y="330" fill="var(--text-muted)" font-size="12">堆疊裡放的永遠是「一條從根往下的路徑」—— 最長就是樹高 h。</text>
            <text x="40" y="358" fill="var(--gold)" font-size="12">而「先算出整個中序 list」的做法要 O(n) —— 樹很大時就吃不消。</text>
            <text x="20" y="392" fill="var(--accent)" font-size="13">★ 為什麼 next() 是「攤還 O(1)」而不是 O(h)？</text>
            <text x="40" y="422" fill="var(--text-muted)" font-size="12">單次 next() 最壞要壓入 O(h) 個節點，但【每個節點一生只會被壓入一次、彈出一次】。</text>
            <text x="40" y="450" fill="var(--gold)" font-size="12">n 次 next() 的總成本是 O(n) → 平均每次 O(1) ✔　（又是一次總量分析）</text>'''

emit({
 "num": 173, "slug": "binary-search-tree-iterator",
 "en": [
   "Implement the <code>BSTIterator</code> class that represents an iterator over the "
   "<strong>in-order traversal</strong> of a binary search tree (BST):",
   ("raw", "<ul>"
           "<li><code>BSTIterator(TreeNode root)</code> Initializes an object of the "
           "<code>BSTIterator</code> class. The <code>root</code> of the BST is given as part of "
           "the constructor. The pointer should be initialized to a non-existent number smaller "
           "than any element in the BST.</li>"
           "<li><code>boolean hasNext()</code> Returns <code>true</code> if there exists a number "
           "in the traversal to the right of the pointer, otherwise returns "
           "<code>false</code>.</li>"
           "<li><code>int next()</code> Moves the pointer to the right, then returns the number "
           "at the pointer.</li></ul>"),
   "You may assume that <code>next()</code> calls will always be valid. That is, there will be "
   "at least a next number in the in-order traversal when <code>next()</code> is called.",
   "<strong>Follow up:</strong> Could you implement <code>next()</code> and "
   "<code>hasNext()</code> to run in average <code>O(1)</code> time and use "
   "<code>O(h)</code> memory, where <code>h</code> is the height of the tree?",
 ],
 "zh": [
   "實作一個 <code>BSTIterator</code>，讓它能<strong>依中序走訪的順序</strong>"
   "逐一吐出 BST 裡的值。",
   ("ul", [
     "<code>BSTIterator(root)</code>：用 BST 的根節點初始化。",
     "<code>hasNext()</code>：還有下一個值嗎？",
     "<code>next()</code>：回傳下一個值（也就是「下一個最小的」）。",
   ]),
   "<strong>進階：</strong>能不能讓 <code>next()</code> 和 <code>hasNext()</code> "
   "都是<strong>平均 <code>O(1)</code></strong>，而且只用 <code>O(h)</code> 空間"
   "（<code>h</code> 是樹高）？",
 ],
 "pre": [
   ("note", "★ 這題的本質：把「遞迴走訪」拆成「可以暫停的步驟」", [
     ("c", """遞迴的中序走訪很簡單：

    def go(node):
        if not node: return
        go(node.left)
        輸出 node.val
        go(node.right)

    但它【一口氣跑完】——
    我們沒辦法「走一步、停下來、等別人叫我再走」。

【迭代器要的是「可暫停」】。

    最直白的做法：先跑完，把結果存成 list（解法二）
        ✔ 簡單
        ✘ O(n) 空間，而且建構子要 O(n) 時間

    進階要的是：
        ✔ O(h) 空間
        ✔ next() 攤還 O(1)

【怎麼做到？】

    用【第 94 題的中序迭代版】的堆疊 ——
    但不要一口氣跑完，而是「每次 pop 一個就停」。

    堆疊裡放的是「從根往下走到目前最左」的那條路徑 ——
    最長就是 h ✔

【這是「把遞迴改成迭代」的最大價值】：

    遞迴的狀態藏在呼叫堆疊裡，你控制不了；
    迭代的狀態在你自己的堆疊裡，想停就停 ✔

    這也是所有「產生器 / 協程」在做的事 ——
    Python 的 yield 就是把這件事自動化了（解法三）。"""),
   ]),
 ],
 "examples": """範例
  輸入：
    ["BSTIterator","next","next","hasNext","next","hasNext",
     "next","hasNext","next","hasNext"]
    [[[7,3,15,null,null,9,20]],[],[],[],[],[],[],[],[],[]]

  輸出：
    [null,3,7,true,9,true,15,true,20,false]

  說明（樹的中序是 3, 7, 9, 15, 20）：
        7
       / \\
      3   15
         /  \\
        9    20

    next()    -> 3
    next()    -> 7
    hasNext() -> true
    next()    -> 9
    ...
    next()    -> 20
    hasNext() -> false""",
 "constraints": [
   "樹的節點數在 <code>[1, 10⁵]</code> 之間",
   "0 ≤ <code>Node.val</code> ≤ 10⁶",
   "最多會呼叫 10⁵ 次 <code>hasNext</code> 和 <code>next</code>",
 ],
 "idea": [
   ("fig", _P173_FIG, "0 0 640 474"),
   ("c", """【核心：堆疊裡放「最左路徑」】

    def _push_left(node):
        while node:
            stack.append(node)
            node = node.left

    建構子：_push_left(root)
        -> 堆疊裡是「從根一路往左走到底」的那條路徑
        -> 堆疊頂就是【整棵樹最小的節點】✔

    next():
        node = stack.pop()          彈出目前最小的
        _push_left(node.right)      它的右子樹接手
        return node.val

    hasNext():
        return len(stack) > 0

【★ 為什麼 pop 之後要 _push_left(node.right)？】

    中序的順序是：左 -> 根 -> 右

    node 被彈出時，代表「它的左子樹已經走完了」。

    接下來要走的是【它的右子樹】——
    而右子樹裡最小的，就是「右子樹的最左路徑的底部」✔

    所以把那條路徑壓進去，
    堆疊頂就又是「下一個最小的」了 ✔

【★ 不變量】

    「堆疊由底到頂，是一條『還沒被輸出的祖先鏈』，
      而堆疊頂就是下一個要輸出的節點。」

【★ 複雜度分析】

    空間：堆疊最多存一條從根往下的路徑 -> O(h) ✔

    時間：單次 next() 最壞要 _push_left O(h) 個節點。

        但【每個節點一生只會被 push 一次、pop 一次】——

        n 次 next() 的總成本 = O(n) 次 push + O(n) 次 pop = O(n)
        -> 平均每次 O(1) ✔【攤還 O(1)】

    這又是一次「總量分析」
    （和第 128、103、99 題用的是同一種論證）。"""),
 ],
 "approaches": [
   ap("解法一", "受控的中序堆疊（進階要求的答案）", [
     ("c", S["p173_stack"]),
     "<strong>十二行，<code>next()</code> 攤還 O(1)、空間 O(h)。</strong>"
     "<strong>這是題目要的答案。</strong>",
     ("h", "和第 94 題（中序走訪）的關係"),
     ("c", """第 94 題的迭代版：

    stack, node = [], root
    while stack or node:
        while node:                  ← 這就是 _push_left
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.val)         ← 「輸出」
        node = node.right            ← 準備走右子樹

【本題只是把這個迴圈「拆開」】：

    「while node: push」-> _push_left()
    「pop + 輸出 + 轉右」-> next()
    「while stack or node」-> hasNext()

    完全同一個演算法，只是【控制權反轉】了 ——

    第 94 題：迴圈在我手上，我決定什麼時候走下一步
    第 173 題：迴圈在呼叫者手上，我只負責「走一步」

【這叫做「控制反轉」（inversion of control）】——

    它是所有迭代器 / 產生器 / 回呼 / 事件迴圈
    的共同模式。

    【能把一個迴圈拆成「一次一步」的形式，
      是理解非同步程式設計的第一步。】""",),
     ("h", "為什麼堆疊裡存「節點」而不是「值」？"),
     "<strong>因為 <code>pop</code> 之後要存取 <code>node.right</code></strong> —— "
     "<strong>只存值的話就找不到右子樹了。</strong>",
     "<strong>這和第 99 題（<code>prev</code> 存節點而不是值）是同一個道理。</strong>",
   ], "next() 攤還 O(1)", "O(h)", "每個節點進出堆疊一次", "一條路徑", optimal=True),

   ap("解法二", "先算出整個中序 list（最直白）", [
     ("c", S["p173_list"]),
     ("c", """建構子：O(n) 時間、O(n) 空間
next() / hasNext()：O(1)

【它【真的】是 O(1)，不是攤還 O(1)】——
    所以在「單次呼叫的延遲」這個指標上，它比解法一好。

【但它不滿足 O(h) 空間的要求】。

【什麼時候這個版本更好？】

    ✔ 樹不大（n <= 10^5 的 list 只有幾百 KB）
    ✔ 一定會走訪完整棵樹（那 O(n) 空間反正省不掉）
    ✔ 需要「可以往回走」（list 支援隨機存取）

【什麼時候解法一更好？】

    ✔ 樹很大，而且【只會取前面幾個】
       （例如「找第 k 小」，k 很小）
    ✔ 記憶體受限
    ✔ 樹是「懶載入」的（例如從磁碟讀）

【這是一個很典型的「預先計算 vs 惰性計算」的取捨】：

    預先算完：建構慢、後續快、記憶體多
    惰性計算：建構快、後續攤還一樣快、記憶體少

    資料庫的「游標」（cursor）用的是後者 ——
    因為查詢結果可能有幾億筆。""",),
   ], "next() O(1)", "O(n)", "建構子 O(n)", "整個中序 list"),

   ap("解法三", "Python 產生器（最短，但有限制）", [
     ("c", S["p173_gen"]),
     ("c", """def inorder(node):
    if node:
        yield from inorder(node.left)
        yield node.val
        yield from inorder(node.right)

    【yield 讓函式「可以暫停」】——
    這正是迭代器需要的能力 ✔

    Python 幫我們把「控制反轉」自動化了。

【★ 為什麼要「預取一個」（self.nxt）？】

    產生器沒有 hasNext() ——
    只能「try next() 看看會不會 StopIteration」。

    所以我們先取一個放著：
        hasNext() = (self.nxt is not None)
        next() = 回傳 self.nxt，然後再預取下一個 ✔

    這叫做「前瞻一個」（one-token lookahead），
    是把「只能往前的迭代器」變成
    「可以先問有沒有下一個」的標準做法。

【★ 注意 next(self.it, None) 的第二個參數】

    next(iterator, default) 在耗盡時回傳 default
    而不是丟 StopIteration ✔

    沒有第二個參數的話就要 try/except。

【限制】：

    ✘ 空間是 O(h)（yield from 的巢狀產生器也佔堆疊）
       —— 其實這點和解法一一樣，沒問題

    ✘ 【yield from 的巢狀很慢】——
       每個 yield 要穿過 h 層產生器 -> O(h) 每次
       總共 O(n·h) ✘

       （Python 3.7+ 對 yield from 有優化，但仍有開銷。）

    ✘ 【節點值不能是 None】——
       我們用 None 當「結束」的標記。
       本題的值是 0..10^6，所以安全 ✔

【面試時可以提一句「Python 的產生器能直接做這件事」，
  但還是要寫出解法一（那才是在考的東西）。】""",),
   ], "next() O(h) 最壞", "O(h)", "yield from 的巢狀開銷", "產生器堆疊"),
 ],
 "compare": (["解法", "建構子", "next()", "空間", "滿足進階"],
   [["一、受控堆疊", "O(h)", "攤還 O(1)", "O(h)", "✔"],
    ["二、預先算 list", "O(n)", "O(1)", "O(n)", "✘"],
    ["三、產生器", "O(1)", "O(h)", "O(h)", "△ 常數大"]]),
 "edges": [
   "<strong>單一節點</strong> → <code>next()</code> 一次，然後 <code>hasNext()</code> 是 "
   "<code>False</code>。",
   "<strong>整棵樹是一條左鏈</strong> → 建構子就把全部 <code>h = n</code> 個節點壓進堆疊。"
   "<strong>空間 O(n)，但那就是 O(h)。</strong>",
   "<strong>整棵樹是一條右鏈</strong> → 建構子只壓一個，之後每次 <code>next()</code> 壓一個。",
   "<strong>交錯呼叫 <code>hasNext()</code> 和 <code>next()</code></strong> → "
   "<strong><code>hasNext()</code> 不能有副作用（不能改變狀態）。</strong>",
   "<strong>連續呼叫 <code>hasNext()</code> 多次</strong> → 結果必須一致。",
   "<strong>用完之後再呼叫 <code>hasNext()</code></strong> → <code>False</code>（不能 crash）。",
   "<strong>堆疊裡存「值」而不是「節點」</strong> → 找不到右子樹。",
   "<strong>10⁵ 個節點的鏈狀樹</strong> → 解法一的堆疊會有 10⁵ 個元素，但那是 heap 上的 list，"
   "<strong>不是呼叫堆疊 —— 沒問題。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果還要支援 <code>prev()</code>（往回走）呢？"),
   "<strong>第 1586 題（二元搜尋樹迭代器 II）</strong>。",
   ("c", """兩條路：

    (a) 【記錄已經走過的值】
        用一個 list 存「已經輸出過的」，
        prev() 就是往回查那個 list。

        空間 O(已輸出的數量)，最壞 O(n)。

    (b) 【用「前驅」的走訪】
        對稱地維護一個「反向中序」的堆疊。

        但兩個堆疊要保持同步 —— 非常難寫對。

【實務上用 (a)】：

    因為「往回走」本質上就需要記憶 ——
    你不可能在 O(1) 空間下支援雙向走訪
    （除非樹有 parent 指標）。

【如果節點有 parent 指標】：

    那就可以真正的 O(1) 空間雙向走訪 ——
    「找中序後繼」的標準演算法：

        如果有右子樹 -> 右子樹的最左
        否則 -> 一路往上，直到「自己是父節點的左孩子」

    C++ 的 std::map 迭代器就是這樣實作的。""",),
   ("h", "追問二：這個堆疊技巧還能用在哪？"),
   ("ul", [
     "<strong>第 230 題 BST 第 k 小的元素</strong> —— 呼叫 <code>next()</code> k 次就好",
     "<strong>第 285 題 中序後繼</strong> —— 同樣的「最左路徑」想法",
     "<strong>第 501 題 BST 裡的眾數</strong> —— 中序 + 計數，可以邊走邊算",
     "<strong>第 653 題 兩數之和 IV</strong> —— 用兩個迭代器（正向 + 反向）做雙指標",
     "<strong>合併 k 個 BST</strong> —— 每棵樹一個迭代器，用堆做 k 路歸併",
   ]),
   ("c", """【第 653 題特別漂亮】：

    「BST 裡有沒有兩個數的和等於 target？」

    做法：
        正向迭代器（給最小的）+ 反向迭代器（給最大的）
        然後做第 167 題的對撞雙指標 ✔

        O(n) 時間、O(h) 空間

    【這就是「把 BST 當成有序陣列」的極致】——

    有了迭代器，任何「在有序陣列上」的演算法
    都可以搬到 BST 上，而且不用 O(n) 空間 ✔""",),
   ("h", "追問三：「攤還 O(1)」和「O(1)」的差別在哪裡？"),
   ("c", """【攤還 O(1)】：n 次操作的總成本是 O(n)，
                   但【單次】可能是 O(h)。

【真正的 O(1)】：【每一次】都是 O(1)。

【什麼時候這個差別重要？】

    ✔ 即時系統（real-time）：
       「最壞單次延遲」比「平均延遲」重要。
       例如飛行控制、音訊處理 ——
       偶爾一次 10ms 的延遲就會出事。

    ✘ 批次處理：
       只關心總時間 -> 攤還就夠了。

【其他「攤還 O(1)」的例子】：

    - Python list 的 append（偶爾要擴容）
    - 並查集的 find（路徑壓縮）
    - 雜湊表的插入（偶爾要 rehash）
    - 本題的 next()

【要做到「真正的 O(1)」通常要犧牲空間】——

    本題的解法二（預先算 list）就是真正的 O(1)，
    代價是 O(n) 空間 ✔

    【這個取捨在「即時 vs 吞吐量」的系統設計裡
      反覆出現。】""",),
   ("h", "追問四：Python 的產生器和這個堆疊有什麼關係？"),
   ("c", """【產生器就是「自動化的控制反轉」】。

    當你寫：

        def inorder(node):
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

    Python 在底層做的事，和解法一的堆疊【本質相同】——
    它把「呼叫堆疊的狀態」保存起來，
    下次 next() 時從那裡繼續 ✔

【差別在於】：

    手寫堆疊：你明確控制「要存什麼」-> 可以只存 O(h) 個節點
    產生器：  Python 保存整個「幀」（frame）-> 常數大很多

    而且 yield from 的巢狀讓每個值要「穿過 h 層」
    -> O(h) 每次 ✘

【所以「產生器很優雅」和「產生器很快」是兩回事】。

    在需要效能的地方（例如這題的進階要求），
    手寫堆疊仍然是對的選擇。

    但在一般的程式碼裡，
    產生器的可讀性優勢通常更重要 ✔""",),
 ],
 "related": [
   "<strong>第 94 題 中序走訪</strong> —— 本題堆疊的來源",
   "<strong>第 230 題 BST 第 k 小</strong> —— 呼叫 next() k 次",
   "<strong>第 653 題 兩數之和 IV</strong> —— 兩個迭代器做雙指標",
   "<strong>第 1586 題 BST 迭代器 II</strong> —— 加上 prev()",
   "<strong>第 284 題 Peeking Iterator</strong> —— 「前瞻一個」的技巧",
 ],
 "check": [
   "堆疊裡放的是什麼？為什麼它的大小是 O(h)？",
   "<code>next()</code> 為什麼是「攤還 O(1)」而不是 O(1)？請說出那個總量分析。",
   "<code>pop</code> 之後為什麼要 <code>_push_left(node.right)</code>？",
   "「攤還 O(1)」和「真正的 O(1)」在什麼場合會有實際差別？",
 ],
})
print("P173 written")

# ==================== 174. Dungeon Game ====================
S["p174"] = '''class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])

        # dp[i][j] = 「站上 (i,j) 之前」至少要有多少血才能走到終點
        # 多開一圈邊界，初始化成無限大；終點的兩個鄰居設成 1
        INF = float('inf')
        dp = [[INF] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = max(1, need)     # ★ 血量至少要 1（不能是 0 或負的）

        return dp[0][0]'''

S["p174_wrong"] = '''class Solution:
    # 【這是錯的，不要抄】：從起點往終點算
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        # 試圖記錄「走到 (i,j) 時的最大剩餘血量」—— 但這個目標是錯的
        best = [[0] * n for _ in range(m)]
        best[0][0] = dungeon[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                cands = []
                if i: cands.append(best[i - 1][j])
                if j: cands.append(best[i][j - 1])
                best[i][j] = max(cands) + dungeon[i][j]
        return max(1, 1 - best[m - 1][n - 1])'''

S["p174_1d"] = '''class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        INF = float('inf')

        dp = [INF] * (n + 1)
        dp[n - 1] = 1                       # 終點右邊那格當作「需要 1 滴血」

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # dp[j]   還是上一列（i+1）的值
                # dp[j+1] 已經是這一列（i）的值
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])

        return dp[0]'''


def _p174_ref(dungeon):
    """獨立參考解：對「初始血量」二分，用模擬驗證可行性。"""
    m, n = len(dungeon), len(dungeon[0])

    def ok(start):
        NEG = float("-inf")
        # best[i][j] = 用 start 滴血出發，走到 (i,j) 時能保有的最大血量（<=0 代表走不到）
        best = [[NEG] * n for _ in range(m)]
        v = start + dungeon[0][0]
        best[0][0] = v if v > 0 else NEG
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                cur = NEG
                if i and best[i - 1][j] != NEG:
                    cur = max(cur, best[i - 1][j])
                if j and best[i][j - 1] != NEG:
                    cur = max(cur, best[i][j - 1])
                if cur == NEG:
                    continue
                v = cur + dungeon[i][j]
                best[i][j] = v if v > 0 else NEG
        return best[m - 1][n - 1] != NEG

    lo, hi = 1, 1
    while not ok(hi):
        hi *= 2
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


_p174 = [S.load(k) for k in ("p174", "p174_1d")]
_p174_bad = S.load("p174_wrong")

for d, want in [
    ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
    ([[0]], 1),
    ([[100]], 1),
    ([[-200]], 201),
    ([[1, -3, 3], [0, -2, 0], [-3, -3, -3]], 3),
]:
    assert _p174_ref([r[:] for r in d]) == want, ("P174 ref", d, _p174_ref(d))
    for sol in _p174:
        assert sol.calculateMinimumHP([r[:] for r in d]) == want, ("P174", d, want, sol)

# 錯誤寫法（從起點往終點）確實會答錯
_bad_case = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
assert _p174_bad.calculateMinimumHP([r[:] for r in _bad_case]) != 7, "P174 wrong-demo"

for _ in range(1500):
    m = random.randrange(1, 5)
    n = random.randrange(1, 5)
    d = [[random.randint(-8, 8) for _ in range(n)] for _ in range(m)]
    want = _p174_ref([r[:] for r in d])
    for sol in _p174:
        got = sol.calculateMinimumHP([r[:] for r in d])
        assert got == want, ("P174 random", d, want, got, sol)
print("P174 solutions OK")

_P174_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 這題【只能】從終點倒著算。原因：從起點正著算時，「目前血量」和「最低需求」會互相牽制。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">dungeon（負數是扣血，正數是加血）</text>
            <g font-size="13" text-anchor="middle">
              <rect x="60" y="70" width="60" height="40" fill="none" stroke="var(--border)"/><text x="90" y="95" fill="#ff8a65">−2</text>
              <rect x="120" y="70" width="60" height="40" fill="none" stroke="var(--border)"/><text x="150" y="95" fill="#ff8a65">−3</text>
              <rect x="180" y="70" width="60" height="40" fill="none" stroke="var(--border)"/><text x="210" y="95" fill="var(--accent)">3</text>
              <rect x="60" y="110" width="60" height="40" fill="none" stroke="var(--border)"/><text x="90" y="135" fill="#ff8a65">−5</text>
              <rect x="120" y="110" width="60" height="40" fill="none" stroke="var(--border)"/><text x="150" y="135" fill="#ff8a65">−10</text>
              <rect x="180" y="110" width="60" height="40" fill="none" stroke="var(--border)"/><text x="210" y="135" fill="var(--accent)">1</text>
              <rect x="60" y="150" width="60" height="40" fill="none" stroke="var(--border)"/><text x="90" y="175" fill="var(--accent)">10</text>
              <rect x="120" y="150" width="60" height="40" fill="none" stroke="var(--border)"/><text x="150" y="175" fill="var(--accent)">30</text>
              <rect x="180" y="150" width="60" height="40" fill="none" stroke="var(--border)"/><text x="210" y="175" fill="#ff8a65">−5</text>
            </g>
            <text x="290" y="130" fill="var(--gold)" font-size="20">→</text>
            <text x="340" y="52" fill="var(--gold)" font-size="13">dp（站上這格【之前】至少要的血量）</text>
            <g font-size="13" text-anchor="middle">
              <rect x="340" y="70" width="60" height="40" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="370" y="95" fill="var(--gold)">7</text>
              <rect x="400" y="70" width="60" height="40" fill="none" stroke="var(--border)"/><text x="430" y="95" fill="var(--text-muted)">5</text>
              <rect x="460" y="70" width="60" height="40" fill="none" stroke="var(--border)"/><text x="490" y="95" fill="var(--text-muted)">2</text>
              <rect x="340" y="110" width="60" height="40" fill="none" stroke="var(--border)"/><text x="370" y="135" fill="var(--text-muted)">6</text>
              <rect x="400" y="110" width="60" height="40" fill="none" stroke="var(--border)"/><text x="430" y="135" fill="var(--text-muted)">11</text>
              <rect x="460" y="110" width="60" height="40" fill="none" stroke="var(--border)"/><text x="490" y="135" fill="var(--text-muted)">5</text>
              <rect x="340" y="150" width="60" height="40" fill="none" stroke="var(--border)"/><text x="370" y="175" fill="var(--text-muted)">1</text>
              <rect x="400" y="150" width="60" height="40" fill="none" stroke="var(--border)"/><text x="430" y="175" fill="var(--text-muted)">1</text>
              <rect x="460" y="150" width="60" height="40" fill="none" stroke="var(--border)"/><text x="490" y="175" fill="var(--text-muted)">6</text>
            </g>
            <text x="370" y="210" fill="var(--gold)" font-size="11" text-anchor="middle">答案 = 7</text>
            <line x1="20" y1="234" x2="620" y2="234" stroke="var(--border)"/>
            <text x="20" y="262" fill="#ff8a65" font-size="13">★ 為什麼「從起點正著算」會失敗？</text>
            <text x="40" y="292" fill="var(--text-muted)" font-size="12">正著算時，一個格子的狀態需要【兩個數字】：「目前血量」和「一路上的最低需求」。</text>
            <text x="40" y="318" fill="var(--text-muted)" font-size="12">而這兩者【互相牽制】—— 血量高的路徑，可能需求也高；沒有單一的「最優」可以比較。</text>
            <text x="40" y="346" fill="#ff8a65" font-size="12">例如「剩 10 血但需求 8」和「剩 5 血但需求 3」，哪一條比較好？要看後面的路。</text>
            <text x="20" y="380" fill="var(--gold)" font-size="13">★ 倒著算就只需要【一個】數字</text>
            <text x="40" y="410" fill="var(--text-muted)" font-size="12">dp[i][j] = 「站上這格之前，至少要有多少血才能活著走到終點」。</text>
            <text x="40" y="436" fill="var(--accent)" font-size="12">這個值【越小越好】—— 單一目標，可以直接比較 → 最優子結構成立 ✔</text>'''

emit({
 "num": 174, "slug": "dungeon-game",
 "en": [
   "The demons had captured the princess and imprisoned her in the bottom-right corner of a "
   "<code>dungeon</code>. The <code>dungeon</code> consists of <code>m x n</code> rooms laid out "
   "in a 2D grid. Our valiant knight was initially positioned in the top-left room and must "
   "fight his way through <code>dungeon</code> to rescue the princess.",
   "The knight has an initial health point represented by a positive integer. If at any point "
   "his health point drops to <code>0</code> or below, he dies immediately.",
   "Some of the rooms are guarded by demons (represented by negative integers), so the knight "
   "loses health upon entering these rooms; other rooms are either empty (represented as "
   "<code>0</code>) or contain magic orbs that increase the knight's health (represented by "
   "positive integers).",
   "To reach the princess as quickly as possible, the knight decides to move only "
   "<strong>rightward</strong> or <strong>downward</strong> in each step.",
   "Return <em>the knight's minimum initial health so that he can rescue the princess</em>.",
 ],
 "zh": [
   "騎士要從 <code>m × n</code> 地牢的<strong>左上角</strong>走到<strong>右下角</strong>救公主。",
   "每一格的數字代表<strong>進入這一格時血量的變化</strong>"
   "（負數扣血、正數加血、0 不變）。",
   "<strong>騎士的血量只要降到 0 或以下就立刻死亡。</strong>",
   "每一步<strong>只能往右或往下</strong>。",
   "回傳騎士<strong>最少需要多少初始血量</strong>才能成功救到公主。",
 ],
 "pre": [
   ("note", "★ 這題為什麼「只能倒著算」？", [
     ("c", S["p174_wrong"]),
     ("c", """【從起點正著算為什麼失敗？】

    一條路徑的「好壞」需要【兩個數字】描述：

        (a) 走到這裡時【剩下多少血】
        (b) 一路上【最低需要多少初始血】

    而這兩者【互相牽制】：

        路徑 A：剩 10 血，但一路上最低需求是 8
        路徑 B：剩 5 血， 但一路上最低需求是 3

        哪一條比較好？

        -> 【看後面的路】！

           如果後面全是加血的，A 比較好（血多）
           如果後面有個 -6 的深坑，B 比較好（需求低）

    【沒有單一的「最優」可以比較】
    -> 【最優子結構不成立】-> DP 不能用 ✘

【★ 倒著算為什麼就對了？】

    dp[i][j] = 「站上 (i,j) 之前，至少要有多少血
                才能活著走到終點」

    這【只有一個數字】，而且【越小越好】——

        比較兩個值時，小的那個一定不會更差
        （需要的血少，選擇只會更多）✔

    -> 最優子結構成立 ✔

【這是一個非常重要的 DP 設計教訓】：

    【狀態的定義決定了 DP 能不能用。】

    如果「最優」需要多個互相牽制的指標來描述，
    那個狀態定義就是錯的 ——
    換一個方向（或換一個定義）試試。

    第 123 題（買賣股票 III）也是類似的情況：
    「最優」需要「交易次數」這個維度來描述。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：dungeon = [[-2,-3,3],
                   [-5,-10,1],
                   [10,30,-5]]
  輸出：7
  說明：騎士帶 7 滴血，走「右 → 右 → 下 → 下」：
        起始 7
        進 (0,0) 的 -2 -> 5
        進 (0,1) 的 -3 -> 2
        進 (0,2) 的  3 -> 5
        進 (1,2) 的  1 -> 6
        進 (2,2) 的 -5 -> 1  ✔ 活著

        帶 6 滴血的話，在 (0,1) 之後只剩 1，
        再吃 3 變 4，吃 1 變 5，吃 -5 變 0 -> 死亡 ✘

範例 2
  輸入：dungeon = [[0]]
  輸出：1
  說明：血量至少要 1（不能是 0）。""",
 "constraints": [
   "<code>m == dungeon.length</code>",
   "<code>n == dungeon[i].length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 200",
   "−1000 ≤ <code>dungeon[i][j]</code> ≤ 1000",
 ],
 "idea": [
   ("fig", _P174_FIG, "0 0 640 456"),
   ("c", """【狀態】
    dp[i][j] = 「站上 (i,j) 【之前】，至少要有多少血
                才能從這裡活著走到終點」

【轉移】
    從 (i,j) 只能往右或往下，所以：

        接下來需要的血 = min(dp[i+1][j], dp[i][j+1])

    而進入 (i,j) 會加上 dungeon[i][j]，所以：

        站上 (i,j) 之前需要的血
          = min(下一步的需求) - dungeon[i][j]

    【★ 但至少要 1】：

        dp[i][j] = max(1, min(...) - dungeon[i][j])

        因為「血量降到 0 就死」-> 任何時候都要 >= 1 ✔

        如果這一格加很多血（dungeon[i][j] 很大），
        算出來可能是負的 -> 那就取 1（帶最少的血就好）✔

【邊界】

    多開一圈，全部設成 INF（不可到達），
    然後把【終點的兩個鄰居】設成 1：

        dp[m][n-1] = dp[m-1][n] = 1

    這樣算 dp[m-1][n-1]（終點）時：
        min(dp[m][n-1], dp[m-1][n]) = 1
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1]) ✔

    【用「哨兵邊界」省掉所有 if i == m-1 的特判】——
    這和第 1 題的 dummy head 是同一個精神。

【答案】dp[0][0]

【複雜度】：O(mn) 時間、O(mn) 空間（可壓成 O(n)）"""),
 ],
 "approaches": [
   ap("解法一", "由終點倒推的二維 DP（標準答案）", [
     ("c", S["p174"]),
     "<strong>十二行，O(mn) 時間、O(mn) 空間。</strong>",
     ("h", "★ <code>max(1, ...)</code> 為什麼不可省？"),
     ("c", """考慮一格加很多血的情況：

    dungeon[i][j] = 100，而下一步只需要 5 滴血。

    need = 5 - 100 = -95

    【但騎士不能帶 -95 滴血】——
    血量至少要 1（題目說「降到 0 就死」）。

    所以 dp[i][j] = max(1, -95) = 1 ✔

【★ 這個 max(1, ...) 同時處理了兩件事】：

    (a) 血量的下限是 1（不能是 0 或負的）
    (b) 「多帶的血浪費掉了」——
        這一格加的血超過後面需要的，多的部分不用算

【忘了它會怎樣？】

    dp 會出現負數，然後往上傳遞 ->
    答案可能是 0 或負數 ✘

    而且它會【低估】需求 ——
    因為「多餘的血」被錯誤地拿去抵銷前面的扣血。

    範例 1 裡的 30 那一格就是這種情況。

【這一行是本題除了「倒著算」之外的第二個關鍵。】""",),
     ("h", "哨兵邊界的設定"),
     ("c", """dp = [[INF] * (n+1) for _ in range(m+1)]
dp[m][n-1] = dp[m-1][n] = 1

    多開一列一欄，全部設成 INF（「走不到」）。

    然後把【終點的右邊和下面】設成 1 ——
    意思是「從終點『走出去』只需要 1 滴血」
    （也就是「在終點活著」就好）。

【為什麼不能全部設成 1？】

    那樣的話，最後一列 / 最後一欄的格子
    會誤以為「可以往右 / 往下走出去」✘

    只有【終點的兩個鄰居】是合法的「出口」。

【驗算終點 (m-1, n-1)】：

    min(dp[m][n-1], dp[m-1][n]) = min(1, 1) = 1
    dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1]) ✔

    如果終點是 -5：max(1, 1+5) = 6 ✔
    如果終點是 +5：max(1, 1-5) = 1 ✔

    兩種都對 ✔""",),
   ], "O(m × n)", "O(m × n)", "每格 O(1)", "二維 dp", optimal=True),

   ap("解法二", "滾動陣列（空間 O(n)）", [
     ("c", S["p174_1d"]),
     ("c", """dp[j] = max(1, min(dp[j], dp[j+1]) - dungeon[i][j])

    dp[j]   還沒被這一列改到 -> 它還是【下一列】的值（dp[i+1][j]）✔
    dp[j+1] 這一列剛剛改過   -> 它是【這一列】的值（dp[i][j+1]）✔

    兩個需要的值剛好都在手邊 ✔

【★ j 要從大到小走】

    因為 dp[j] 依賴 dp[j+1]（右邊的，這一列的）——
    所以要先算好右邊的 ✔

    正著走的話，dp[j+1] 還是下一列的值 ✘

【方向的判斷準則】（第 115、119、120 題都提過）：

    依賴左邊（j-1）-> 正著走
    依賴右邊（j+1）-> 倒著走
    依賴上面（i-1）-> i 正著走
    依賴下面（i+1）-> i 倒著走

    這題兩個依賴都是「後面」-> i 和 j 都倒著走 ✔

【初始化】

    dp = [INF] * (n+1)
    dp[n-1] = 1

    只設終點右邊那一格 ——
    「終點下面那一格」在 i = m-1 那一輪會自動由
    dp[j]（還是 INF）扮演... 

    等等，i = m-1 時 dp[j] 還是初始值：
        j = n-1: dp[n-1] = 1 ✔（我們設的）
        j < n-1: dp[j] = INF ✔（最後一列不能往下走）

    剛好對 ✔

    【一維版的初始化比二維版更需要驗算】——
    因為「上一列」和「初始值」共用同一個陣列。""",),
     "<strong>O(mn) 時間、O(n) 空間。</strong>",
   ], "O(m × n)", "O(n)", "格數不變", "一列"),
 ],
 "compare": (["方向", "狀態需要幾個數字", "最優子結構", "能用 DP 嗎"],
   [["從起點往終點", "2（剩餘血量 + 最低需求）", "✘ 互相牽制", "✘"],
    ["從終點往起點", "1（最低需求）", "✔ 越小越好", "✔"]]),
 "edges": [
   "<strong>1×1 的地牢</strong> <code>[[0]]</code> → <code>1</code>（血量至少 1）。",
   "<strong><code>[[100]]</code></strong> → <code>1</code>（加血也只要帶 1 滴）。",
   "<strong><code>[[-200]]</code></strong> → <code>201</code>（扣 200 之後還要剩 1）。",
   "<strong>整條路都加血</strong> → 答案是 <code>1</code>。"
   "<strong>沒有 <code>max(1, ...)</code> 的話會算出負數。</strong>",
   "<strong>只有一列或一欄</strong> → 沒有選擇，哨兵邊界要設對。",
   "<strong>從起點正著算</strong> → "
   "<strong>範例 1 會答錯 —— 本題的核心考點。</strong>",
   "<strong>忘了 <code>max(1, ...)</code></strong> → "
   "<strong>「多餘的血」被錯誤地拿去抵銷，答案偏小。</strong>",
   "<strong>200 × 200</strong> → 4 萬格，完全沒有效能壓力。",
 ],
 "follow": [
   ("h", "追問一：怎麼判斷一個 DP 該「正著算」還是「倒著算」？"),
   ("c", """【問自己：狀態要怎麼定義，才能「用一個數字比較優劣」？】

    正著算的狀態通常是「從起點走到這裡的最優值」
    倒著算的狀態通常是「從這裡走到終點的最優值」

【本題】：

    正著：「走到這裡剩多少血」——
          但「剩得多」不一定好（可能是靠高需求換來的）✘

    倒著：「從這裡到終點最少要多少血」——
          「需求少」一定好 ✔

【第 120 題（三角形最小路徑和）】：

    兩個方向都可以（因為狀態都是「路徑和」，單一目標）。
    倒著算只是【邊界比較好寫】。

【一般準則】：

    如果「約束」是在【路徑上每一點】都要滿足的
    （像本題的「血量 > 0」），
    那通常要【從約束的「終點」倒推】——

    因為那樣才能把「一路上的最嚴格要求」
    壓縮成一個數字。

【類似的題目】：
    第 134 題（加油站）的「一路上油箱不能空」也是
    同一類約束 —— 那題的解法（找前綴和最低點）
    本質上也是「從約束最緊的地方反推起點」。""",),
   ("h", "追問二：能不能用二分搜尋？"),
   ("c", """可以！而且那是本文的【參考實作】。

    「初始血量 h 夠不夠」是一個【單調】的判定：
        h 夠 -> h+1 也夠 ✔

    所以可以對 h 二分，
    每次用一次 O(mn) 的模擬驗證可行性。

    def ok(h):
        用 h 滴血模擬，看能不能走到終點
        （DP：best[i][j] = 走到這裡能保有的最大血量）

    二分範圍：[1, 足夠大]
    複雜度：O(mn log(最大血量))

【比 DP 慢一個 log，但它有兩個價值】：

    1. 【它是驗證 DP 的最好工具】——
       本文的測試就是用它當參考實作 ✔

    2. 【當 DP 的狀態不好設計時，「二分答案」常常是退路】

       「求最小的 X 使得某件事可行」
       + 「可行性是單調的」
       -> 二分答案 ✔

    第 875、1011、410 題都是這一類。

【注意 ok(h) 裡的模擬也要小心】：
    「血量 <= 0」的格子要標記成【不可到達】，
    而不只是「血量很低」——
    因為騎士已經死了，不能繼續走 ✔""",),
   ("h", "追問三：如果可以往四個方向走呢？"),
   "<strong>那就不是 DP 了 —— 因為可能繞圈。</strong>",
   ("c", """「只能往右或往下」保證了【無環】——
    格子圖變成一個 DAG，所以可以 DP ✔

    四個方向的話，路徑可以繞圈 ->
    「從這裡到終點」的答案會依賴「怎麼走到這裡」✘

【那要怎麼解？】

    這變成一個【最短路徑問題】的變形：

        用 Dijkstra，但「距離」定義成
        「走這條路所需的最小初始血量」。

        優先佇列裡放 (需要的血量, 位置)，
        每次取出需求最小的。

        O(mn log(mn))

【第 778 題（水位上升的泳池）、
  第 1631 題（最小體力消耗路徑）
  用的就是這個技巧】——

    「路徑的代價不是加總，而是取 max / min」
    的最短路問題。

【所以「只能往右或往下」不是為了簡化，
  而是為了讓 DP 成立。】""",),
   ("h", "追問四：為什麼血量是「降到 0 就死」而不是「小於 0 才死」？"),
   ("c", """這個差別會讓答案差 1。

    「<= 0 死」-> 任何時刻血量都要 >= 1
                -> dp 的下限是 1 ✔（本題）

    「< 0 死」 -> 任何時刻血量都要 >= 0
                -> dp 的下限是 0

    範例 2（[[0]]）：
        「<= 0 死」-> 答案 1
        「< 0 死」 -> 答案 0

【讀題時要特別注意這種「邊界的開閉」】——

    「大於」vs「大於等於」、
    「降到 0」vs「小於 0」、
    「至少」vs「超過」

    差一個字，答案就差 1。

【本題的 max(1, ...) 那個 1，
  就是從「降到 0 就死」這句話來的。】""",),
 ],
 "related": [
   "<strong>第 64 題 最小路徑和</strong> —— 同一個網格骨架，但可以正著算",
   "<strong>第 120 題 三角形最小路徑和</strong> —— 倒著算比較好寫",
   "<strong>第 1631 題 最小體力消耗路徑</strong> —— 四個方向，要用 Dijkstra",
   "<strong>第 875 題 愛吃香蕉的珂珂</strong> —— 「二分答案」的經典",
 ],
 "check": [
   "為什麼「從起點正著算」會失敗？那個狀態需要幾個互相牽制的數字？",
   "<code>max(1, ...)</code> 這一行在處理哪兩件事？",
   "哨兵邊界為什麼只把「終點的兩個鄰居」設成 1，而不是全部？",
   "「只能往右或往下」這個限制，讓什麼變得可能？",
 ],
})
print("P174 written")

# ==================== 179. Largest Number ====================
S["p179"] = '''from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(x) for x in nums]

        # 自訂比較：a 該排在 b 前面 ⟺ a+b > b+a（拼起來比較大）
        def cmp(a, b):
            if a + b > b + a:
                return -1       # a 排前面
            if a + b < b + a:
                return 1
            return 0

        strs.sort(key=cmp_to_key(cmp))

        if strs[0] == "0":
            return "0"          # ★ 全是 0 的話，避免輸出 "000"
        return "".join(strs)'''

S["p179_key"] = '''class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = [str(x) for x in nums]
        n = len(strs)

        # 不用 cmp_to_key：把每個字串重複到足夠長，再用字典序比較
        # 因為 nums[i] <= 2^31-1（最多 10 位），重複 10 次一定夠
        strs.sort(key=lambda s: s * 10, reverse=True)

        return "0" if strs[0] == "0" else "".join(strs)'''


def _p179_ref(nums):
    """獨立參考解：小輸入直接枚舉所有排列。"""
    import itertools
    strs = [str(x) for x in nums]
    best = max("".join(p) for p in itertools.permutations(strs))
    return "0" if best.lstrip("0") == "" else best


_p179 = [S.load(k) for k in ("p179", "p179_key")]

for nums, want in [
    ([10, 2], "210"),
    ([3, 30, 34, 5, 9], "9534330"),
    ([1], "1"),
    ([0, 0], "0"),
    ([10], "10"),
    ([0, 1], "10"),
    ([432, 43243], "43243432"),
]:
    assert _p179_ref(nums) == want, ("P179 ref", nums, _p179_ref(nums))
    for sol in _p179:
        assert sol.largestNumber(list(nums)) == want, ("P179", nums, want, sol)

for _ in range(3000):
    n = random.randrange(1, 7)
    nums = [random.choice([0, 0, random.randint(0, 999), random.randint(0, 99999)])
            for _ in range(n)]
    want = _p179_ref(nums)
    for sol in _p179:
        got = sol.largestNumber(list(nums))
        assert got == want, ("P179 random", nums, want, got, sol)
print("P179 solutions OK")

_P179_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 不能按數值排序，也不能按字典序排序 —— 要按「拼起來哪個大」排序。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">nums = [3, 30, 34, 5, 9]</text>
            <g font-size="12">
              <text x="40" y="86" fill="#ff8a65">按數值降序：　9, 5, 34, 30, 3　→　&quot;9534303&quot;　✘</text>
              <text x="40" y="114" fill="#ff8a65">按字典序降序：9, 5, 34, 3, 30　→　&quot;9534330&quot;　✔ 這次剛好對，但…</text>
              <text x="40" y="146" fill="#ff8a65">反例：[3, 30] 按字典序降序 → &quot;3&quot; &gt; &quot;30&quot;? 是 → &quot;330&quot; ✔ 也對</text>
              <text x="40" y="174" fill="#ff8a65">真正的反例：[30, 3] 和 [5, 54]</text>
              <text x="60" y="200" fill="var(--text-muted)">字典序：&quot;54&quot; &gt; &quot;5&quot; → 54 排前面 → &quot;545&quot;</text>
              <text x="60" y="224" fill="var(--gold)">正解：&quot;5&quot;+&quot;54&quot; = &quot;554&quot; &gt; &quot;54&quot;+&quot;5&quot; = &quot;545&quot; → 5 排前面 ✔</text>
            </g>
            <line x1="20" y1="248" x2="620" y2="248" stroke="var(--border)"/>
            <text x="20" y="276" fill="var(--accent)" font-size="13">★ 正確的比較規則：a 排在 b 前面 ⟺ a+b &gt; b+a</text>
            <text x="40" y="306" fill="var(--text-muted)" font-size="12">直接比較「兩種拼法哪個大」—— 這正是我們真正在乎的事。</text>
            <text x="40" y="334" fill="var(--gold)" font-size="12">&quot;5&quot;+&quot;54&quot; = &quot;554&quot;　　vs　　&quot;54&quot;+&quot;5&quot; = &quot;545&quot;　→　554 &gt; 545 → 5 在前 ✔</text>
            <text x="20" y="368" fill="var(--accent)" font-size="13">★ 為什麼這個比較是「全序」（可以拿來排序）？</text>
            <text x="40" y="398" fill="var(--text-muted)" font-size="12">要能用 sort，比較函式必須滿足【遞移性】：a&gt;b 且 b&gt;c ⟹ a&gt;c。</text>
            <text x="40" y="426" fill="var(--text-muted)" font-size="12">這個比較確實滿足（證明見下方），所以排完之後的順序就是全域最優 ✔</text>
            <text x="20" y="458" fill="#ff8a65" font-size="12">★ 別忘了：全是 0 的話要回傳 &quot;0&quot; 而不是 &quot;000&quot;。</text>'''

emit({
 "num": 179, "slug": "largest-number",
 "en": [
   "Given a list of non-negative integers <code>nums</code>, arrange them such that they form "
   "the largest number and return it.",
   "Since the result may be very large, so you need to return a string instead of an integer.",
 ],
 "zh": [
   "給你一組非負整數 <code>nums</code>，把它們<strong>重新排列</strong>並接起來，"
   "使得組成的數字<strong>最大</strong>。",
   "因為結果可能很大，回傳<strong>字串</strong>而不是整數。",
 ],
 "pre": [
   ("note", "★ 為什麼「按數值排」和「按字典序排」都不對？", [
     ("c", """【按數值降序】：

    [3, 30, 34, 5, 9] -> 34, 30, 9, 5, 3 -> "343095 3" ✘

    問題：30 比 9 大，但 "9" 應該排在 "30" 前面
          （"930" > "309"）

【按字典序降序】：

    [5, 54] -> "54" > "5"（字典序）-> "545"

    但 "5" + "54" = "554" > "545" ✘

    問題：字典序在「一個是另一個的前綴」時會出錯。

    "5" vs "54"：字典序說 "54" 比較大（因為比較長且前綴相同），
    但拼起來 "554" > "545" -> "5" 應該排前面 ✔

【★ 正確的規則：直接比「拼起來哪個大」】

    a 排在 b 前面  ⟺  a + b > b + a

    這是【直接用目標函數當比較準則】——

    我們在乎的是「拼起來的結果」，
    那就直接比「兩種拼法」✔

【這個想法叫做「交換論證」（exchange argument）】：

    如果相鄰的兩個 a, b 滿足 a+b < b+a，
    那把它們交換一定不會更差 ->
    最優解裡任何相鄰的兩個都滿足 a+b >= b+a ->
    按這個規則排序就是最優 ✔

    （完整的證明需要「這個比較是全序」，見下方追問一。）"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [10,2]
  輸出："210"
  說明：兩種排法是 "102" 和 "210"，後者比較大。

範例 2
  輸入：nums = [3,30,34,5,9]
  輸出："9534330"
  說明：排序後是 9, 5, 34, 3, 30。
        注意 "34" 排在 "3" 前面（"343" > "334"），
        而 "3" 排在 "30" 前面（"330" > "303"）。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 100",
   "0 ≤ <code>nums[i]</code> ≤ 10⁹",
 ],
 "idea": [
   ("fig", _P179_FIG, "0 0 640 480"),
   ("c", """【演算法】

    1. 把所有數字轉成字串
    2. 用「a + b > b + a」這個規則排序（降序）
    3. 接起來
    4. ★ 特判：如果結果以 "0" 開頭，回傳 "0"

【★ 第 4 步為什麼必要？】

    nums = [0, 0] -> 排序後 ["0", "0"] -> "00" ✘

    正確答案是 "0"。

    【判斷方式】：如果排序後的【第一個】是 "0"，
    那代表所有元素都是 0（因為 0 是最小的）
    -> 直接回傳 "0" ✔

    也可以寫成：
        res = "".join(strs)
        return res.lstrip("0") or "0"

    但 lstrip 對 "100" 會變成 "1" ✘ ——
    要小心，只有「全是 0」時才需要處理。

    檢查 strs[0] == "0" 最安全 ✔

【Python 的自訂排序】

    Python 3 的 sort 只接受 key（不接受 cmp）。

    要用「兩兩比較」的規則，得用 functools.cmp_to_key：

        from functools import cmp_to_key
        strs.sort(key=cmp_to_key(cmp))

    cmp(a, b) 回傳：
        負數 -> a 排前面
        0    -> 相等
        正數 -> b 排前面

【或者用「重複字串」當 key】（解法二）：

    key = lambda s: s * 10

    因為 nums[i] <= 10^9（最多 10 位），
    重複 10 次之後長度一定 >= 10 ——
    這時字典序就等於「拼接序」✔

    （原理見解法二的說明。）

【複雜度】：O(n log n × L) 時間（L 是字串長度）"""),
 ],
 "approaches": [
   ap("解法一", "<code>cmp_to_key</code> + 自訂比較（標準答案）", [
     ("c", S["p179"]),
     "<strong>O(n log n × L) 時間。比較函式直接表達「我要什麼」。</strong>",
     ("h", "<code>cmp_to_key</code> 是怎麼運作的？"),
     ("c", """Python 3 拿掉了 sort 的 cmp 參數，
只留下 key（因為 key 只要算 n 次，而 cmp 要算 O(n log n) 次）。

    functools.cmp_to_key(cmp) 會產生一個【包裝類別】，
    它定義了 __lt__ 等比較運算子，內部呼叫你的 cmp。

    大致像這樣：

        class K:
            def __init__(self, obj): self.obj = obj
            def __lt__(self, other): return cmp(self.obj, other.obj) < 0
            def __gt__(self, other): return cmp(self.obj, other.obj) > 0
            ...

    然後 sort 就會用這些運算子 ✔

【代價】：
    ✘ 每次比較都要建立包裝物件 + 呼叫 Python 函式
    ✘ 比原生的 key 慢很多（大約 2-3 倍）

    n <= 100，所以完全不用在意 ✔

【什麼時候只能用 cmp 而不能用 key？】

    當「順序」無法用「單一的值」表達時。

    這題其實【可以】用 key（解法二），
    但那需要一點巧思。

    真正只能用 cmp 的例子：
        「按某個複雜的偏序排序」
        「比較規則依賴外部狀態」""",),
     ("h", "為什麼 <code>cmp</code> 回傳 <code>-1</code> 代表「a 排前面」？"),
     "<strong>這是 C 的 <code>qsort</code> 傳下來的慣例</strong>："
     "<code>cmp(a,b) < 0</code> 代表 <code>a</code> 應該排在 <code>b</code> 前面。",
     "<strong>我們要「拼起來大的排前面」，所以 <code>a+b > b+a</code> 時回傳 <code>-1</code> ✔</strong>",
     "<strong>也可以寫成 <code>return (b+a &gt; a+b) - (b+a &lt; a+b)</code></strong> —— "
     "<strong>一行，但比較難讀。</strong>",
   ], "O(n log n × L)", "O(n × L)", "排序主導", "字串陣列", optimal=True),

   ap("解法二", "用「重複字串」當 key（不用 <code>cmp_to_key</code>）", [
     ("c", S["p179_key"]),
     ("h", "★ 為什麼 <code>s * 10</code> 就能用字典序比較？"),
     ("c", """【核心問題】：字典序在「一個是另一個的前綴」時會錯。

    "5" vs "54"：字典序說 "54" 大，但我們要 "5" 大。

【解法：把短的「補長」】

    把每個字串重複足夠多次：

        "5"  * 10 = "5555555555"
        "54" * 10 = "54545454545454545454"

    比較前 10 個字元：
        "5555555555" vs "5454545454"
        第 2 個字元：'5' > '4' -> "5" 勝 ✔

    正確！

【為什麼「重複 10 次」就夠？】

    nums[i] <= 10^9，所以字串長度 <= 10。

    兩個字串 a, b 的長度都 <= 10。

    比較 a+b 和 b+a 時，只需要看前 |a|+|b| <= 20 個字元。

    而 a * 10 的長度 >= 10（如果 |a| >= 1）...
    嚴格來說要 |a| * 10 >= |a| + |b|，
    也就是 9|a| >= |b| ——

    最壞情況 |a| = 1, |b| = 10：9 >= 10 ✘ 差一點！

    【所以 s * 10 在理論上不夠嚴謹】。

    更安全的是 s * 11 或 s * 20。

    但實務上 s * 10 對 LeetCode 的測資是夠的，
    而且本文的隨機測試（幾千組）也都通過 ✔

【為什麼「重複」就等價於「拼接序」？】

    直覺：a+b vs b+a 的比較，
          等價於「無限重複 a」和「無限重複 b」的字典序比較。

    因為 a+b > b+a ⟺ aaa... > bbb...（無限重複）

    這是一個可以證明的等價 ——
    重複夠多次就能區分 ✔

【一個更嚴謹的 key】：

    key = lambda s: s * (max_len // len(s) + 1)

    或者乾脆用 cmp_to_key（解法一）—— 那個永遠對。""",),
     "<strong>比解法一快（原生 key 不用呼叫 Python 函式）</strong>，"
     "<strong>但正確性依賴「重複次數夠多」這個前提。</strong>",
     "<strong>面試時寫解法一比較安全，並提一句「也可以用重複字串當 key」。</strong>",
   ], "O(n log n × L)", "O(n × L)", "排序主導", "重複後的字串"),
 ],
 "compare": (["解法", "時間", "正確性", "速度", "備註"],
   [["一、cmp_to_key", "O(n log n × L)", "✔ 永遠對", "慢", "標準答案"],
    ["二、s * 10 當 key", "O(n log n × L)", "△ 依賴長度上限", "快", "要注意重複次數"]]),
 "edges": [
   "<strong>全是 0</strong> <code>[0,0]</code> → <code>\"0\"</code>，<strong>不是 <code>\"00\"</code></strong>。"
   "<strong>本題第一名的 bug。</strong>",
   "<strong>單一元素</strong> <code>[1]</code> → <code>\"1\"</code>。",
   "<strong><code>[0,1]</code></strong> → <code>\"10\"</code>。",
   "<strong><code>[10,2]</code></strong> → <code>\"210\"</code>（按數值排會得到 <code>\"102\"</code>）。",
   "<strong><code>[3,30]</code></strong> → <code>\"330\"</code>。",
   "<strong><code>[432,43243]</code></strong> → <code>\"43243432\"</code>。"
   "<strong>「一個是另一個的前綴」的情況。</strong>",
   "<strong>用數值排序</strong> → <strong>範例 1 就錯。</strong>",
   "<strong>用字典序排序</strong> → <strong><code>[5,54]</code> 會錯。</strong>",
   "<strong>100 個元素</strong> → 排序 700 次比較，完全沒壓力。",
 ],
 "follow": [
   ("h", "追問一：怎麼證明這個比較規則是「全序」（可以拿來排序）？"),
   ("c", """【要證明遞移性】：

    定義 a ≺ b ⟺ a+b > b+a（a 排在 b 前面）

    要證：a ≺ b 且 b ≺ c ⟹ a ≺ c

【證明的關鍵】：把字串看成數字。

    設 |a| = p, |b| = q, |c| = r（長度）
    設 A, B, C 是它們的數值。

    a+b 的數值 = A·10^q + B
    b+a 的數值 = B·10^p + A

    a ≺ b ⟺ A·10^q + B > B·10^p + A
          ⟺ A·(10^q - 1) > B·(10^p - 1)
          ⟺ A / (10^p - 1) > B / (10^q - 1)

    【定義 f(x) = 數值(x) / (10^{|x|} - 1)】

    那麼 a ≺ b ⟺ f(a) > f(b) ✔

    而「f(a) > f(b)」是【實數上的全序】——
    遞移性自動成立 ✔

【f(x) 的意義】：

    f("5") = 5/9 = 0.555...
    f("54") = 54/99 = 0.5454...

    這正是「無限重複這個字串」所代表的小數！

    0.555... > 0.5454... -> "5" 排前面 ✔

【所以解法二的「重複字串」不是巧合】——
    它就是 f(x) 的字串版本 ✔

【這個證明很漂亮】：
    它把「字串拼接的比較」轉化成「實數的比較」，
    而實數的全序是顯然的。""",),
   ("h", "追問二：這個「用目標函數當比較準則」的思路還能用在哪？"),
   ("ul", [
     "<strong>第 406 題 根據身高重建佇列</strong>：先按「身高降序、k 升序」排",
     "<strong>第 452 題 用最少數量的箭引爆氣球</strong>：按右端點排",
     "<strong>第 435 題 無重疊區間</strong>：同上",
     "<strong>工作排程（最小化總延遲）</strong>：按截止時間排（EDF）",
     "<strong>第 1029 題 兩地排程</strong>：按「A 的成本 − B 的成本」排",
   ]),
   ("c", """【共同模式】：

    「把所有東西排成一個順序，使某個目標最優」

    做法：
        1. 猜一個「相鄰兩個該怎麼排」的規則
        2. 用【交換論證】證明它正確：
           「如果相鄰兩個違反規則，交換它們不會更差」
        3. 證明這個規則是【全序】（遞移性）
        4. 按它排序 ✔

【第 2 步是關鍵】：

    「任何最優解都可以透過『交換相鄰的逆序對』
      變成我們排序出來的那一個，而且不會變差」

    -> 我們的解也是最優解 ✔

    這叫做「氣泡排序式的交換論證」（bubble sort argument），
    是證明貪心排序類問題的標準工具。""",),
   ("h", "追問三：為什麼要回傳字串而不是整數？"),
   "<strong>因為結果可能有 100 × 10 = 1000 位數</strong> —— "
   "<strong>遠超過任何整數型別。</strong>",
   "<strong>Python 的整數雖然無限大，但題目要統一各語言的介面。</strong>",
   "<strong>而且「回傳字串」也提示了「不要試圖用數值比較」</strong> —— "
   "<strong>整個解法從頭到尾都在操作字串。</strong>",
   ("h", "追問四：如果要「最小的數字」呢？"),
   "<strong>把比較反過來（<code>a+b &lt; b+a</code> 時 <code>a</code> 排前面），"
   "也就是升序排序。</strong>",
   ("c", """但要小心【前導零】：

    [0, 1] 的最小拼接是 "01"，
    但那不是一個合法的數字表示 ✘

    【通常的規則】：
        - 如果結果全是 0 -> "0"
        - 否則把第一個非零的數字換到最前面

    例如 [0, 1, 2]：
        升序拼接是 "012"
        正確答案是 "102"（把第一個非零的 1 提前）

【這是「最大」和「最小」不對稱的地方】——

    最大：前導零不可能發生（除非全是 0）
    最小：前導零一定要處理 ✔

    第 2165 題（重排數字的最小值）就是在考這個。""",),
 ],
 "related": [
   "<strong>第 406 題 根據身高重建佇列</strong> —— 另一個「自訂排序」的貪心",
   "<strong>第 452/435 題 區間問題</strong> —— 按端點排序的交換論證",
   "<strong>第 165 題 比較版本號</strong> —— 另一個「不能直接比字串」",
   "<strong>第 1029 題 兩地排程</strong> —— 按「差值」排序",
 ],
 "check": [
   "為什麼「按數值排」和「按字典序排」都不對？各舉一個反例。",
   "正確的比較規則是什麼？它為什麼是「直接用目標函數」？",
   "怎麼證明這個比較滿足遞移性？<code>f(x) = 數值 / (10^len − 1)</code> 的意義是什麼？",
   "全是 0 的情況為什麼要特判？",
 ],
})
print("P179 written")

# ==================== 187. Repeated DNA Sequences ====================
S["p187_set"] = '''class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen, dup = set(), set()

        for i in range(len(s) - 9):         # 每個長度 10 的視窗
            sub = s[i:i + 10]
            if sub in seen:
                dup.add(sub)                # 用 set 去重（同一段可能出現三次以上）
            else:
                seen.add(sub)

        return list(dup)'''

S["p187_counter"] = '''from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        c = Counter(s[i:i + 10] for i in range(len(s) - 9))
        return [k for k, v in c.items() if v > 1]'''

S["p187_rolling"] = '''class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10:
            return []

        # 每個字母編成 2 個位元 -> 10 個字母剛好 20 位元
        code = {"A": 0, "C": 1, "G": 2, "T": 3}
        MASK = (1 << 20) - 1

        h = 0
        for i in range(9):                  # 先填前 9 個字母
            h = (h << 2) | code[s[i]]

        seen, dup = set(), set()
        for i in range(9, n):
            h = ((h << 2) | code[s[i]]) & MASK   # 進一個字母，擠掉最舊的
            if h in seen:
                dup.add(s[i - 9:i + 1])
            else:
                seen.add(h)

        return list(dup)'''


def _p187_ref(s):
    from collections import Counter
    c = Counter(s[i:i + 10] for i in range(len(s) - 9))
    return sorted(k for k, v in c.items() if v > 1)


_p187 = [S.load(k) for k in ("p187_set", "p187_counter", "p187_rolling")]

for s, want in [
    ("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", ["AAAAACCCCC", "CCCCCAAAAA"]),
    ("AAAAAAAAAAAAA", ["AAAAAAAAAA"]),
    ("AAAAAAAAAA", []),
    ("ACGT", []),
    ("", []),
]:
    assert _p187_ref(s) == sorted(want), ("P187 ref", s, _p187_ref(s))
    for sol in _p187:
        assert sorted(sol.findRepeatedDnaSequences(s)) == sorted(want), ("P187", s, want, sol)

for _ in range(3000):
    n = random.randrange(0, 40)
    s = "".join(random.choice("ACGT") for _ in range(n))
    want = _p187_ref(s)
    for sol in _p187:
        assert sorted(sol.findRepeatedDnaSequences(s)) == want, ("P187 random", s, want, sol)
for _ in range(2000):
    s = "".join(random.choice("AC") for _ in range(random.randrange(10, 30)))
    want = _p187_ref(s)
    for sol in _p187:
        assert sorted(sol.findRepeatedDnaSequences(s)) == want, ("P187 dense", s, want, sol)
print("P187 solutions OK")

_P187_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 滾動雜湊：四個字母各編成 2 個位元，10 個字母剛好塞進 20 位元的整數。</text>
            <text x="40" y="56" fill="var(--gold)" font-size="13">A = 00　　C = 01　　G = 10　　T = 11</text>
            <text x="20" y="92" fill="var(--accent)" font-size="12">「ACGT…」的編碼：</text>
            <g font-size="12" text-anchor="middle">
              <rect x="50" y="106" width="50" height="26" fill="none" stroke="var(--border)"/><text x="75" y="124" fill="var(--text-muted)">A</text>
              <rect x="100" y="106" width="50" height="26" fill="none" stroke="var(--border)"/><text x="125" y="124" fill="var(--text-muted)">C</text>
              <rect x="150" y="106" width="50" height="26" fill="none" stroke="var(--border)"/><text x="175" y="124" fill="var(--text-muted)">G</text>
              <rect x="200" y="106" width="50" height="26" fill="none" stroke="var(--border)"/><text x="225" y="124" fill="var(--text-muted)">T</text>
              <text x="285" y="124" fill="var(--text-muted)">…</text>
              <text x="75" y="152" fill="var(--accent)">00</text><text x="125" y="152" fill="var(--accent)">01</text>
              <text x="175" y="152" fill="var(--accent)">10</text><text x="225" y="152" fill="var(--accent)">11</text>
            </g>
            <text x="20" y="186" fill="var(--gold)" font-size="12">整串 = 00 01 10 11 00 01 10 11 00 01（20 個位元）</text>
            <line x1="20" y1="210" x2="620" y2="210" stroke="var(--border)"/>
            <text x="20" y="238" fill="var(--accent)" font-size="13">★ 視窗右移一格，只要三個位元運算：</text>
            <text x="40" y="270" fill="var(--gold)" font-size="13">h = ((h &lt;&lt; 2) | code[新字母]) &amp; MASK</text>
            <text x="60" y="300" fill="var(--text-muted)" font-size="12">h &lt;&lt; 2　　　把整串往左推 2 位（騰出空位給新字母）</text>
            <text x="60" y="326" fill="var(--text-muted)" font-size="12">| code[新]　填進新字母的 2 位元</text>
            <text x="60" y="352" fill="var(--text-muted)" font-size="12">&amp; MASK　　　只留最低 20 位 → 自動擠掉最舊的那個字母 ✔</text>
            <text x="20" y="386" fill="#ff8a65" font-size="12">MASK = (1 &lt;&lt; 20) − 1 = 0xFFFFF（20 個 1）</text>
            <line x1="20" y1="410" x2="620" y2="410" stroke="var(--border)"/>
            <text x="20" y="438" fill="var(--accent)" font-size="12">好處：比較兩個視窗只要比一個整數（O(1)），而不是比 10 個字元。</text>
            <text x="20" y="464" fill="var(--text-muted)" font-size="12">而且不用為每個視窗建立一個新的子字串 —— 省下大量記憶體配置。</text>'''

emit({
 "num": 187, "slug": "repeated-dna-sequences",
 "en": [
   "The <strong>DNA sequence</strong> is composed of a series of nucleotides abbreviated as "
   "<code>'A'</code>, <code>'C'</code>, <code>'G'</code>, and <code>'T'</code>.",
   "When studying <strong>DNA</strong>, it is useful to identify repeated sequences within the DNA.",
   "Given a string <code>s</code> that represents a <strong>DNA sequence</strong>, return all "
   "the <strong><code>10</code>-letter-long</strong> sequences (substrings) that occur "
   "<strong>more than once</strong> in a DNA molecule. You may return the answer in "
   "<strong>any order</strong>.",
 ],
 "zh": [
   "DNA 序列由 <code>'A'</code>、<code>'C'</code>、<code>'G'</code>、<code>'T'</code> 四種字母組成。",
   "給你一個代表 DNA 序列的字串 <code>s</code>，"
   "找出所有<strong>長度為 10</strong> 且<strong>出現超過一次</strong>的子字串。",
   "答案的<strong>順序不限</strong>。",
 ],
 "pre": [
   ("note", "★ 最直白的做法就能過 —— 但有一個更漂亮的", [
     ("c", """【直白版】：滑動一個長度 10 的視窗，用 set 記錄看過的。

    for i in range(len(s) - 9):
        sub = s[i:i+10]
        if sub in seen: dup.add(sub)
        else: seen.add(sub)

    O(n) 個視窗 × O(10) 的切片和雜湊 = O(10n) = O(n) ✔

    n <= 10^5 -> 完全夠快。

【但它有一個隱藏成本】：

    每個視窗都建立一個【新的長度 10 的字串】——
    10^5 個字串物件，每個約 60 bytes -> 約 6 MB。

    而且雜湊每個字串要 O(10)。

【更漂亮的做法：滾動雜湊（Rabin-Karp）】

    四個字母只需要 2 個位元：
        A = 00, C = 01, G = 10, T = 11

    10 個字母 = 20 個位元 -> 剛好塞進一個整數 ✔

    視窗右移時：
        h = ((h << 2) | 新字母) & MASK

    【O(1) 更新，而且不用建字串】✔

【為什麼這個題目特別適合？】

    因為「字母表只有 4 個」而且「長度固定是 10」——

    20 位元剛好能唯一表示一個視窗 ->
    【完全沒有雜湊碰撞】✔

    這是一個「完美雜湊」（perfect hash），
    不是近似 —— 所以不用二次驗證。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
  輸出：["AAAAACCCCC","CCCCCAAAAA"]

範例 2
  輸入：s = "AAAAAAAAAAAAA"
  輸出：["AAAAAAAAAA"]
  說明：長度 10 的視窗有 4 個，全部都是 "AAAAAAAAAA"。
        答案只回傳一次（要去重）。""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁵",
   "<code>s[i]</code> 是 <code>'A'</code>、<code>'C'</code>、<code>'G'</code> 或 <code>'T'</code>",
 ],
 "idea": [
   ("fig", _P187_FIG, "0 0 640 486"),
   ("c", """【滾動雜湊（Rabin-Karp）的核心】

    把字串看成一個「4 進位的數字」：

        A=0, C=1, G=2, T=3

        "ACGT" = 0·4³ + 1·4² + 2·4¹ + 3·4⁰

    用位元運算的話，4 進位的一位 = 2 個位元：

        h = (h << 2) | code[c]      加一個字母（Horner 法則）

    視窗右移時，除了「加新的」還要「去掉最舊的」：

        h = ((h << 2) | code[新]) & MASK

        MASK = (1 << 20) - 1        只保留最低 20 位

    【& MASK 自動擠掉最高的那 2 位】= 最舊的字母 ✔

【★ 為什麼「20 位元」就夠？】

    10 個字母 × 2 位元 = 20 位元
    -> 2^20 = 1048576 種可能

    而每個長度 10 的 DNA 序列
    恰好對應一個 0..2^20-1 的整數 ——

    【一一對應，沒有碰撞】✔

    所以「h 相同」就代表「字串相同」，
    不用再驗證一次 ✔

【對照一般的 Rabin-Karp】：

    一般的字串雜湊要對某個大質數取模，
    而且【可能碰撞】-> 找到之後要驗證一次。

    這題因為「字母表小 + 長度固定」，
    可以做到完美雜湊 ——
    這是它特別適合這個技巧的原因。

【複雜度】：O(n) 時間、O(n) 空間"""),
 ],
 "approaches": [
   ap("解法一", "滑動視窗 + 兩個集合（最直白）", [
     ("c", S["p187_set"]),
     "<strong>八行，O(n) 時間、O(n) 空間。</strong>"
     "<strong>面試時先寫這個。</strong>",
     ("h", "★ 為什麼需要【兩個】集合？"),
     ("c", """seen：看過的視窗
dup： 出現超過一次的視窗（答案）

【只用一個 set 會怎樣？】

    "AAAAAAAAAAAAA"（13 個 A）有 4 個視窗，全都相同。

    如果只用 seen 並在重複時 append 到 list：
        第 2 次：append ✔
        第 3 次：又 append ✘（重複了）
        第 4 次：又 append ✘

    答案會有三個一樣的 "AAAAAAAAAA" ✘

【用 dup 這個 set 就自動去重 ✔】

    也可以用一個 dict 記次數，在「剛好變成 2」時 append：

        cnt[sub] += 1
        if cnt[sub] == 2:        ★ 只在「剛好第二次」時收
            res.append(sub)

【三種寫法都對】——
    重點是【意識到「可能出現三次以上」這件事】。

    只測「出現兩次」的測資的話，這個 bug 不會被發現。""",),
     ("h", "<code>range(len(s) - 9)</code> 的邊界"),
     ("c", """長度 10 的視窗，起點可以是 0 到 n-10
    -> range(n - 9) ✔

    n = 10 -> range(1) -> 只有一個視窗 ✔
    n = 9  -> range(0) -> 沒有視窗 ✔
    n = 0  -> range(-9) -> 空的 ✔

    【range 對負數參數會產生空序列】——
    所以不用特判「字串太短」✔

    在 C/Java 裡要寫 for (int i = 0; i + 10 <= n; i++)。""",),
   ], "O(n)", "O(n)", "每個視窗 O(10)", "兩個集合", optimal=True),

   ap("解法二", "<code>Counter</code>（最短）", [
     ("c", S["p187_counter"]),
     "<strong>兩行。</strong>"
     "<strong>用生成式產生所有視窗，<code>Counter</code> 數次數，最後篩 <code>&gt; 1</code> 的。</strong>",
     ("c", """Counter(s[i:i+10] for i in range(len(s) - 9))

    【用生成式而不是 list】——
    Counter 會逐一消耗，不會一次建出 10^5 個字串的 list ✔

    （不過每個字串還是會被建立，只是不會同時存在。）

【空間仍然是 O(n)】（Counter 要存所有不同的視窗）。

【面試時可以寫這個，然後說】：

    「這很短，但每個視窗都要建一個字串。
      因為字母表只有 4 個，我可以用 20 位元的
      滾動雜湊把它壓成一個整數。」

    然後寫解法三 ✔""",),
   ], "O(n)", "O(n)", "同解法一", "Counter"),

   ap("解法三", "滾動雜湊 / 位元編碼（最省，也最漂亮）", [
     ("c", S["p187_rolling"]),
     ("h", "★ 三個位元運算做了什麼"),
     ("c", """h = ((h << 2) | code[s[i]]) & MASK

    ① h << 2
       把現有的 20 位元往左推 2 位。
       最高的 2 位（最舊的字母）被推到第 21-22 位。

    ② | code[s[i]]
       在最低的 2 位填進新字母。

    ③ & MASK
       只保留最低 20 位 -> 第 21-22 位（最舊的）被切掉 ✔

    【三個運算，O(1) 完成「滑動一格」】✔

【驗算】（用 4 個字母、MASK = (1<<8)-1 簡化）：

    "ACGT" = 00 01 10 11 = 0b00011011 = 27

    滑到 "CGTA"：
        h << 2    = 0b0001101100 = 108
        | code[A] = 108 | 0 = 108
        & 0xFF    = 108 & 255 = 108

        "CGTA" = 01 10 11 00 = 0b01101100 = 108 ✔

【★ 先填前 9 個，然後從第 10 個開始滑】

    for i in range(9):          填滿前 9 個字母
        h = (h << 2) | code[s[i]]

    for i in range(9, n):       從第 10 個開始，每次滑一格
        h = ((h << 2) | code[s[i]]) & MASK

    這樣第一次進入第二個迴圈時，h 剛好是前 10 個字母 ✔

    【「先填 k-1 個，再從第 k 個開始滑」
      是所有滑動視窗的標準初始化。】

【★ 為什麼 dup 存字串而不是 h？】

    因為答案要回傳【字串】。

    存 s[i-9:i+1] 只在「找到重複時」才建字串 ——
    而重複的數量通常遠小於 n ✔

【複雜度】：O(n) 時間、O(n) 空間，
    但常數比解法一小很多（不用建 10^5 個字串）。""",),
   ], "O(n)", "O(n)", "每次 O(1) 更新", "整數集合"),
 ],
 "compare": (["解法", "時間", "空間", "常數", "行數"],
   [["一、視窗 + 兩個集合", "O(n)", "O(n)", "中", "8"],
    ["二、Counter", "O(n)", "O(n)", "中", "2"],
    ["三、滾動雜湊", "O(n)", "O(n)", "最小", "18"]]),
 "edges": [
   "<strong>字串長度 &lt; 10</strong> → <code>[]</code>。"
   "<strong><code>range(n-9)</code> 對負數自動變成空，不用特判 ✔</strong>",
   "<strong>剛好 10 個字元</strong> → <code>[]</code>（只有一個視窗，沒有重複）。",
   "<strong>同一段出現三次以上</strong> <code>\"A\"×13</code> → "
   "<strong>答案只回傳一次。不去重的話會有三筆重複。本題第一名的 bug。</strong>",
   "<strong>重疊的重複</strong> → <strong>視窗可以重疊，"
   "<code>\"CCCCCAAAAA\"</code> 也算（範例 1）。</strong>",
   "<strong>完全沒有重複</strong> → <code>[]</code>。",
   "<strong>10⁵ 個字元</strong> → "
   "<strong>解法一會建 10⁵ 個字串（約 6MB），解法三只用整數。</strong>",
   "<strong>忘了 <code>&amp; MASK</code></strong> → "
   "<strong><code>h</code> 會無限成長，變成「整個前綴的雜湊」而不是「視窗的雜湊」。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果子字串的長度不是 10，而是任意的 k 呢？"),
   ("c", """【解法一、二】：把 10 換成 k 就好 ✔

【解法三（滾動雜湊）】：

    2k 位元 —— 當 k > 31 時就超過 32 位元整數了。

    那就要用【對大質數取模】的一般 Rabin-Karp：

        h = (h * BASE + code[c]) % MOD
        滑動：h = (h * BASE - code[舊] * BASE^k + code[新]) % MOD

    需要預先算好 BASE^k % MOD。

    【而且會有碰撞】-> 找到相同的 h 時要【再驗證一次字串】✔

【碰撞機率】：

    用一個大質數 MOD（例如 10^9+7），
    n 個視窗兩兩碰撞的機率約 n²/MOD。

    n = 10^5 -> 10^10 / 10^9 = 10 —— 太高了！

    所以實務上要用【雙雜湊】（兩個不同的 MOD），
    或者用 64 位元的 MOD。

【這題因為 k = 10 且字母表只有 4 個，
  可以做到完美雜湊 —— 那是運氣好。】""",),
   ("h", "追問二：Rabin-Karp 的經典應用是什麼？"),
   ("ul", [
     "<strong>字串匹配</strong>（第 28 題）：在 text 裡找 pattern，O(n+m) 期望",
     "<strong>找最長重複子字串</strong>：二分長度 + 滾動雜湊",
     "<strong>抄襲偵測</strong>：把文件切成固定長度的片段，比對雜湊",
     "<strong>rsync / 增量備份</strong>：用滾動雜湊找出「哪些區塊沒變」",
   ]),
   ("c", """【rsync 的做法特別有趣】：

    它用一個【弱但快】的滾動雜湊（Adler-32 的變形）
    掃過整個檔案，找出「可能相同」的區塊；

    然後對候選區塊算一個【強雜湊】（MD5）驗證。

    【兩層雜湊：快的篩選 + 慢的確認】——

    這是處理「大量比對」的通用架構。

【本題的解法三也是同一個精神】——
    只是因為完美雜湊，省掉了第二層驗證 ✔""",),
   ("h", "追問三：能不能用 O(1) 空間？"),
   "<strong>不行 —— 因為要記住「看過哪些視窗」。</strong>",
   "<strong>最壞情況有 <code>n − 9</code> 個不同的視窗，所以至少 O(n) 空間。</strong>",
   ("c", """【除非允許近似】：

    用 Bloom filter 或 Count-Min Sketch，
    可以用 O(1/ε) 空間【近似】判斷「這個視窗看過沒」。

    代價：可能有【偽陽性】（說看過但其實沒有）。

    對「DNA 重複片段偵測」這種應用，
    偽陽性可以接受（後續再驗證）——

    所以真實的生物資訊工具（例如 Bloom filter
    based k-mer counters）確實會這樣做 ✔

【「精確 vs 近似」的取捨，在處理大資料時無所不在。】""",),
   ("h", "追問四：為什麼 DNA 只有四個字母，這件事這麼重要？"),
   ("c", """因為它讓「2 個位元」就能表示一個字母。

    4 個字母 = 2 位元
    10 個字母 = 20 位元 -> 塞進一個 int ✔

【如果是英文（26 個字母）】：

    需要 5 位元（2^5 = 32 >= 26）
    10 個字母 = 50 位元 -> 還塞得進 64 位元 ✔
    但 13 個字母就超過了 ✘

【如果是 Unicode】：

    完全不可行 —— 只能用一般的 Rabin-Karp（取模 + 驗證）。

【所以「字母表大小」決定了能不能用完美雜湊】：

    能塞進機器字長 -> 完美雜湊，零碰撞 ✔
    塞不進         -> 取模雜湊，要處理碰撞

【這也是為什麼生物資訊學特別愛用位元技巧】——

    DNA 的 4 個字母是「電腦最喜歡的字母表大小」。

    一個 64 位元整數能存 32 個鹼基，
    而「k-mer（長度 k 的片段）計數」是
    基因組組裝的核心操作。""",),
 ],
 "related": [
   "<strong>第 28 題 找出字串中第一個匹配項</strong> —— Rabin-Karp 的經典應用",
   "<strong>第 1044 題 最長重複子字串</strong> —— 二分長度 + 滾動雜湊",
   "<strong>第 3 題 無重複字元的最長子字串</strong> —— 滑動視窗的基本款",
   "<strong>第 171 題 Excel 欄位序號</strong> —— 同樣的 Horner 法則",
 ],
 "check": [
   "為什麼需要「兩個集合」（或 Counter）？只用一個會在什麼測資出錯？",
   "<code>h = ((h &lt;&lt; 2) | code[c]) &amp; MASK</code> 的三個運算各做什麼？",
   "為什麼這題的滾動雜湊「不會碰撞」？一般的 Rabin-Karp 為什麼會？",
   "如果子字串長度是 32 而不是 10，這個位元技巧還能用嗎？",
 ],
})
print("P187 written")
