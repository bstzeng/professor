# -*- coding: utf-8 -*-
"""第 99–100 題。"""
import random
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(99)


def _vals_inorder(node):
    return [] if not node else _vals_inorder(node.left) + [node.val] + _vals_inorder(node.right)


def _nodes_inorder(node):
    return [] if not node else _nodes_inorder(node.left) + [node] + _nodes_inorder(node.right)


def _shape(node):
    return "#" if not node else "(%s|%s)" % (_shape(node.left), _shape(node.right))


def _build(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _build(l), _build(r))


def _rand_bst(vals):
    if not vals:
        return None
    k = random.randrange(len(vals))
    return TreeNode(vals[k], _rand_bst(vals[:k]), _rand_bst(vals[k + 1:]))


# ==================== 99. Recover Binary Search Tree ====================
S["p99_sort"] = '''class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # 先把中序走訪的「節點」收集起來
        nodes = []

        def go(node):
            if not node:
                return
            go(node.left)
            nodes.append(node)
            go(node.right)

        go(root)

        # 正確的中序應該是值排序後的結果，直接填回去
        for node, v in zip(nodes, sorted(n.val for n in nodes)):
            node.val = v'''

S["p99_inorder"] = '''class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.first = self.second = self.prev = None

        def go(node):
            if not node:
                return
            go(node.left)

            # 中序走訪裡，prev 應該永遠 < node。違反了就是逆序點
            if self.prev and self.prev.val > node.val:
                if self.first is None:
                    self.first = self.prev      # 第一次：記「大的那個」
                self.second = node              # 每次都更新「小的那個」
            self.prev = node

            go(node.right)

        go(root)
        self.first.val, self.second.val = self.second.val, self.first.val'''

S["p99_iter"] = '''class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack, prev = [], None
        first = second = None
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            if prev and prev.val > node.val:
                if first is None:
                    first = prev
                second = node
            prev = node

            node = node.right

        first.val, second.val = second.val, first.val'''

S["p99_morris"] = '''class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first = second = prev = None
        node = root

        while node:
            if not node.left:
                if prev and prev.val > node.val:
                    if first is None:
                        first = prev
                    second = node
                prev = node
                node = node.right
            else:
                pre = node.left                      # 找中序前驅
                while pre.right and pre.right is not node:
                    pre = pre.right

                if not pre.right:                    # 第一次：架線，往左
                    pre.right = node
                    node = node.left
                else:                                # 第二次：拆線，輸出
                    pre.right = None
                    if prev and prev.val > node.val:
                        if first is None:
                            first = prev
                        second = node
                    prev = node
                    node = node.right

        first.val, second.val = second.val, first.val'''


def _p99_ref(root):
    """獨立參考解：把中序節點的值整個重新排序填回去（一定正確，但 O(n log n) 空間）。"""
    nodes = _nodes_inorder(root)
    for node, v in zip(nodes, sorted(n.val for n in nodes)):
        node.val = v


_p99 = [S.load(k) for k in ("p99_sort", "p99_inorder", "p99_iter", "p99_morris")]

# 官方範例
for spec in [
    [1, [3, None, [2, None, None]], None],           # 範例 1：[1,3,null,null,2]
    [3, [1, None, None], [4, [2, None, None], None]],  # 範例 2：[3,1,4,null,null,2]
    [2, [3, None, None], [1, None, None]],           # 根與兩邊：相鄰交換
]:
    want = sorted(_vals_inorder(_build(spec)))
    for sol in _p99:
        t = _build(spec)
        shape = _shape(t)
        sol.recoverTree(t)
        assert _vals_inorder(t) == want, ("P99", spec, sol, _vals_inorder(t))
        assert _shape(t) == shape, ("P99 shape changed", spec, sol)

# 隨機壓力測試：蓋一棵合法 BST，隨機交換兩個節點的值，再要求還原
for _ in range(4000):
    n = random.randrange(2, 12)
    vals = sorted(random.sample(range(-40, 40), n))
    base = _rand_bst(vals)
    nodes = _nodes_inorder(base)
    i, j = random.sample(range(n), 2)
    nodes[i].val, nodes[j].val = nodes[j].val, nodes[i].val
    broken = [nd.val for nd in _nodes_inorder(base)]

    def clone(nd):
        return None if nd is None else TreeNode(nd.val, clone(nd.left), clone(nd.right))

    for sol in _p99:
        t = clone(base)          # 每個解法都從同一棵壞掉的樹開始
        shape = _shape(t)
        sol.recoverTree(t)
        assert _vals_inorder(t) == vals, ("P99 random", broken, vals, _vals_inorder(t), sol)
        assert _shape(t) == shape, ("P99 shape changed", broken, sol)
print("P99 solutions OK")

_P99_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">中序走訪一遍，把 BST 攤平成一條「本該遞增」的序列。被交換的兩個值，就藏在逆序點裡。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">情況 A：兩個被換的節點【不相鄰】 → 出現兩個逆序點</text>
            <g font-size="14" text-anchor="middle">
              <rect x="40" y="70" width="62" height="30" fill="none" stroke="var(--border)"/><text x="71" y="91" fill="var(--text-muted)">1</text>
              <rect x="112" y="70" width="62" height="30" fill="none" stroke="#ff8a65" stroke-width="3"/><text x="143" y="91" fill="#ff8a65">6</text>
              <rect x="184" y="70" width="62" height="30" fill="none" stroke="var(--border)"/><text x="215" y="91" fill="var(--text-muted)">3</text>
              <rect x="256" y="70" width="62" height="30" fill="none" stroke="var(--border)"/><text x="287" y="91" fill="var(--text-muted)">4</text>
              <rect x="328" y="70" width="62" height="30" fill="none" stroke="var(--border)"/><text x="359" y="91" fill="var(--text-muted)">5</text>
              <rect x="400" y="70" width="62" height="30" fill="none" stroke="#ff8a65" stroke-width="3"/><text x="431" y="91" fill="#ff8a65">2</text>
              <rect x="472" y="70" width="62" height="30" fill="none" stroke="var(--border)"/><text x="503" y="91" fill="var(--text-muted)">7</text>
            </g>
            <text x="143" y="122" fill="#ff8a65" font-size="11">↑ 6 &gt; 3</text>
            <text x="431" y="122" fill="#ff8a65" font-size="11">↑ 5 &gt; 2</text>
            <text x="40" y="148" fill="var(--accent)" font-size="12">第一個逆序點取【前者 6】，第二個逆序點取【後者 2】 → 交換 6 和 2 ✔</text>
            <line x1="20" y1="168" x2="620" y2="168" stroke="var(--border)"/>
            <text x="20" y="196" fill="var(--gold)" font-size="13">情況 B：兩個被換的節點【相鄰】 → 只出現一個逆序點</text>
            <g font-size="14" text-anchor="middle">
              <rect x="40" y="214" width="62" height="30" fill="none" stroke="var(--border)"/><text x="71" y="235" fill="var(--text-muted)">1</text>
              <rect x="112" y="214" width="62" height="30" fill="none" stroke="var(--border)"/><text x="143" y="235" fill="var(--text-muted)">2</text>
              <rect x="184" y="214" width="62" height="30" fill="none" stroke="#ff8a65" stroke-width="3"/><text x="215" y="235" fill="#ff8a65">4</text>
              <rect x="256" y="214" width="62" height="30" fill="none" stroke="#ff8a65" stroke-width="3"/><text x="287" y="235" fill="#ff8a65">3</text>
              <rect x="328" y="214" width="62" height="30" fill="none" stroke="var(--border)"/><text x="359" y="235" fill="var(--text-muted)">5</text>
              <rect x="400" y="214" width="62" height="30" fill="none" stroke="var(--border)"/><text x="431" y="235" fill="var(--text-muted)">6</text>
            </g>
            <text x="251" y="266" fill="#ff8a65" font-size="11">↑ 只有這一個：4 &gt; 3</text>
            <text x="40" y="292" fill="var(--accent)" font-size="12">first = 4（前者），second = 3（後者） → 交換 4 和 3 ✔</text>
            <line x1="20" y1="312" x2="620" y2="312" stroke="var(--border)"/>
            <text x="20" y="340" fill="var(--gold)" font-size="12">一段程式碼同時處理兩種情況的訣竅：</text>
            <text x="20" y="364" fill="var(--text-muted)" font-size="12">first 只在【第一次】遇到逆序時設定（永遠取前者）；second 在【每一次】逆序都覆蓋（永遠取後者）。</text>
            <text x="20" y="388" fill="var(--accent)" font-size="12">情況 B 只逆序一次 → first 和 second 在同一次設定，剛好就是那兩個相鄰的節點 ✔</text>'''

emit({
 "num": 99, "slug": "recover-binary-search-tree",
 "en": [
   "You are given the <code>root</code> of a binary search tree (BST), where the values of "
   "<strong>exactly two</strong> nodes of the tree were swapped by mistake. "
   "<em>Recover the tree without changing its structure</em>.",
   "<strong>Follow up:</strong> A solution using <code>O(n)</code> space is pretty "
   "straight-forward. Could you devise a constant <code>O(1)</code> space solution?",
 ],
 "zh": [
   "給你一棵二元搜尋樹（BST）的根節點 <code>root</code>，"
   "其中<strong>剛好有兩個</strong>節點的值被不小心<strong>交換</strong>了。",
   "請<strong>在不改變樹的結構</strong>的前提下，把它復原。",
   "<strong>進階：</strong>用 <code>O(n)</code> 空間很直接，你能做到 <code>O(1)</code> 嗎？",
 ],
 "pre": [
   ("note", "先確認題目到底在說什麼", [
     ("c", """「兩個節點的值被交換」的意思是：

    原本是一棵合法的 BST，
    然後有人把【其中兩個節點裡存的數字】對調了。

    樹的【形狀完全沒變】，只有兩個位置的數字換了位子。

你要做的是：把那兩個數字換回來。

【注意：是改 val，不是搬節點。】

    題目明確說「不改變結構」——
    所以不能重建樹、不能改 left/right 指標，
    只能修改節點裡的 val。

    （實務上兩者等價，但面試官會看你有沒有讀清楚題目。）

前一題（98）教你「怎麼判斷是不是 BST」，
這一題教你「壞掉了要怎麼修」——
兩題用的是【同一把鑰匙】。"""),
   ]),
   ("note", "這把鑰匙：BST ⟺ 中序走訪嚴格遞增", [
     ("c", """把 BST 中序走訪一遍，會得到一條【嚴格遞增】的序列。

    現在有兩個值被交換了，
    那條序列上就會出現【逆序】。

    原本：  1  2  3  4  5  6  7
    交換 2 和 6：
            1  6  3  4  5  2  7
               ^           ^

    【問題從「樹」變成了「一條幾乎排好序的陣列裡，
      找出被交換的那兩個元素」。】

    這是一個非常標準的化簡：
        樹的問題  --中序-->  陣列的問題"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,3,null,null,2]

          1
         /
        3
         \\
          2

  中序走訪：3, 2, 1   （應該要是 1, 2, 3）
  輸出：[3,1,null,null,2]

          3
         /
        1
         \\
          2

  說明：1 和 3 被交換了，換回來即可。

範例 2
  輸入：root = [3,1,4,null,null,2]

          3
         / \\
        1   4
           /
          2

  中序走訪：1, 3, 2, 4   （應該要是 1, 2, 3, 4）
  輸出：[2,1,4,null,null,3]

  說明：2 和 3 被交換了。""",
 "constraints": [
   "樹的節點數在 <code>[2, 1000]</code> 之間",
   "−2³¹ ≤ <code>Node.val</code> ≤ 2³¹ − 1",
 ],
 "mid": [
   ("note", "注意：節點數至少是 2", [
     "所以<strong>一定存在兩個被交換的節點</strong>，"
     "不需要處理「樹本來就是對的」這種情況。",
     "<strong>但寫防呆比較安全</strong>："
     "如果 <code>first is None</code>（沒找到逆序），就直接 <code>return</code>。"
     "<strong>面試時主動加上這行會加分。</strong>",
   ]),
 ],
 "idea": [
   ("fig", _P99_FIG, "0 0 640 406"),
   ("c", """在中序序列上找「逆序點」（相鄰兩項 prev > cur 的位置）。

【情況 A：被交換的兩個位置不相鄰】

    1  6  3  4  5  2  7
       ^逆序1        ^逆序2

    逆序1：6 > 3   -> 要換的「大值」是 6（前者）
    逆序2：5 > 2   -> 要換的「小值」是 2（後者）

    出現【兩個】逆序點。

【情況 B：被交換的兩個位置相鄰】

    1  2  4  3  5  6
          ^逆序

    只有【一個】逆序點：4 > 3
    要換的就是 4（前者）和 3（後者）。

【怎麼用一段程式碼同時處理兩種情況？】

    每遇到一次逆序 (prev, cur)：
        if first is None: first = prev      # 只記第一次的前者
        second = cur                         # 每次都更新成後者

    情況 A：
        第一次逆序 -> first = 6, second = 3
        第二次逆序 -> first 不動,  second = 2   ✔ 最終 (6, 2)

    情況 B：
        唯一一次逆序 -> first = 4, second = 3   ✔

    【first 只設一次、second 每次都覆蓋】——
    這六個字就是本題的全部技巧。

最後 swap(first.val, second.val) 即可。"""),
   ("h", "為什麼「最多只會有兩個逆序點」？"),
   ("c", """把中序序列想成一個排序好的陣列，然後交換位置 i < j 的兩個元素。

    ... a[i-1]  a[j]  a[i+1] ... a[j-1]  a[i]  a[j+1] ...
                 ^                        ^
              變大了                    變小了

    a[j] 原本比 a[i] 大，現在被放到前面 -> 和右鄰居產生逆序
    a[i] 原本比 a[j] 小，現在被放到後面 -> 和左鄰居產生逆序

    中間那一段 a[i+1] ... a[j-1] 內部仍然遞增（沒被動到）。

    所以【恰好兩個逆序點】——

    除非 j = i + 1（相鄰），此時兩個逆序點重疊成一個。

【這個推理是本題的正確性證明，面試時值得講一遍。】"""),
 ],
 "approaches": [
   ap("解法一", "中序收集 + 排序（最笨但最保險）", [
     ("c", S["p99_sort"]),
     "<strong>先把中序的節點收集起來，再把「排序後的值」依序填回去。</strong>"
     "完全不用思考逆序點，<strong>絕對不會錯</strong>。",
     ("c", """為什麼這樣一定對？

    中序的第 k 個節點，就該放「第 k 小的值」——
    這是 BST 的定義。

    所以把所有值排序後依序填回中序位置，
    結果必然是合法的 BST，而且形狀沒變 ✔

    而且它甚至比題目要求的更強：
    【就算被交換的不只兩個節點，它也能修好。】

代價：
    時間 O(n log n)（排序）
    空間 O(n)（存節點）

    題目 n <= 1000，這個成本完全可以接受。""",),
     "<strong>面試時可以先講這個當「保底解」</strong>，"
     "說「這一定對，但我可以做得更好」，然後再講解法二。"
     "<strong>先給出一個正確解、再優化，是很好的節奏。</strong>",
   ], "O(n log n)", "O(n)", "排序主導", "存所有節點"),

   ap("解法二", "中序找逆序點（面試預設答案）", [
     ("c", S["p99_inorder"]),
     ("h", "三個變數的分工"),
     ("c", """prev    中序走訪裡「上一個節點」（注意存的是節點，不是值）
first   要交換的兩個節點中，【比較大】的那個（先出現）
second  要交換的兩個節點中，【比較小】的那個（後出現）

    if prev and prev.val > node.val:
        if first is None:
            first = prev      # 只在第一次逆序時設定
        second = node         # 每次逆序都更新

    最後 swap(first.val, second.val)

【為什麼 first 只設一次？】
    因為在情況 A 裡，第一個逆序點的「前者」才是被錯放的大值；
    第二個逆序點的前者只是個無辜的路人。

【為什麼 second 每次都更新？】
    因為在情況 A 裡，被錯放的小值出現在【第二個】逆序點的後者。
    在情況 B 裡只有一次逆序，所以「每次都更新」也等於「設一次」。

    兩種情況共用同一段程式碼 ✔"""),
     ("h", "為什麼 <code>prev</code> 存節點而不是值？"),
     "因為<strong>最後要交換的是節點裡的 <code>val</code></strong>，"
     "所以必須抓得到那個節點物件。",
     "<strong>只存值的話，你知道「要換 6 和 2」，卻不知道它們在哪兩個節點上</strong> —— "
     "而且樹裡可能有同值節點（雖然 BST 不該有，但壞掉的樹什麼都可能）。",
     ("h", "<code>if self.prev</code> 這裡為什麼可以不用 <code>is not None</code>？"),
     "<strong>因為 <code>prev</code> 是 <code>TreeNode</code> 物件</strong>，"
     "而自訂類別的實例<strong>永遠是 truthy</strong>（除非定義了 "
     "<code>__bool__</code> 或 <code>__len__</code>）。",
     "<strong>對照第 98 題</strong>：那裡的 <code>prev</code> 存的是<strong>整數值</strong>，"
     "值可能是 <code>0</code>，"
     "<strong>所以那裡非得寫 <code>is not None</code> 不可</strong>。"
     "<strong>同一個符號、不同的型別，安全性完全不同 —— 這是很好的對照練習。</strong>",
     "<strong>空間 O(h)</strong>（遞迴堆疊）。"
     "<strong>還不是 O(1)</strong>，所以進階要求還沒滿足。",
   ], "O(n)", "O(h)", "每個節點看一次", "遞迴堆疊", optimal=True),

   ap("解法三", "中序迭代版（把遞迴堆疊變成顯式堆疊）", [
     ("c", S["p99_iter"]),
     "<strong>和解法二完全等價</strong>，只是把遞迴改成 <code>while</code> + <code>stack</code>。",
     "<strong>好處</strong>：沒有遞迴深度限制（本題 n ≤ 1000 其實不會爆，"
     "但養成習慣總是好的），而且可以用<strong>區域變數</strong>，"
     "不用 <code>self.</code> 或 <code>nonlocal</code>。",
     ("c", """這個骨架（第 94、98、99、173、230 題共用）：

    stack, node = [], root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        # ★★★ 中序輸出的時機，你的邏輯寫在這裡 ★★★
        node = node.right

【把它背起來。】
只要換掉星號那一行，就能解一整排 BST 題目。""",),
     "<strong>空間仍然是 O(h)</strong> —— 堆疊沒消失，只是換了地方住。",
   ], "O(n)", "O(h)", "每個節點進出堆疊一次", "顯式堆疊"),

   ap("解法四", "Morris 中序走訪（真正的 O(1) 空間，滿足進階）", [
     ("c", S["p99_morris"]),
     ("h", "Morris 的核心：借用空指標當「回家的線」"),
     ("c", """一棵 n 個節點的二元樹有 n+1 個空指標，
Morris 把它們臨時借來記錄「走完左子樹之後要回到誰身上」。

對每個有左子樹的 node：

    pre = node.left
    while pre.right and pre.right is not node:
        pre = pre.right            # pre 走到左子樹的最右邊 = node 的中序前驅

    if not pre.right:              # 【第一次】造訪 node
        pre.right = node           #   架線：走完左子樹會自動回到 node
        node = node.left           #   往左下去

    else:                          # 【第二次】造訪 node（沿著線回來的）
        pre.right = None           #   拆線，把樹恢復原狀
        <輸出 node>                #   左子樹已經走完了，現在輪到自己
        node = node.right          #   往右子樹

    如果 node 沒有左子樹，直接輸出自己然後往右走。

【pre.right is not node 這個判斷，就是在區分「第一次」和「第二次」。】""",),
     ("h", "為什麼總時間還是 O(n)？"),
     ("c", """看起來「找前驅」是個內層迴圈，會不會變成 O(n²)？

    不會。

    關鍵：每一條「右邊緣」（right spine）最多被走過【兩次】——
    一次是架線時，一次是拆線時。

    而所有右邊緣的總長度是 O(n)（每條邊只屬於一條右邊緣）。

    所以總成本是 O(n) ✔

    這個分析叫做【攤還分析（amortized analysis）】——
    單次操作可能很貴，但總量有上界。"""),
     ("h", "本題用 Morris 的注意事項"),
     "<strong>和第 98 題不同，這裡沒有「提早結束」的誘惑</strong> —— "
     "本來就要走完整棵樹才能確定 <code>second</code>，"
     "<strong>所以 Morris 在這題用起來反而比第 98 題順</strong>。",
     "<strong>但仍然要注意</strong>：中途絕對不能 <code>return</code>，"
     "否則樹上會留下沒拆的線，變成有環的結構。",
     "<strong>空間真的是 O(1)</strong>（只有 <code>first</code>、<code>second</code>、"
     "<code>prev</code>、<code>node</code>、<code>pre</code> 五個指標）—— "
     "<strong>這才是進階要求的答案。</strong>",
     "<strong>代價</strong>：程式碼長了三倍、暫時修改樹（不可用於唯讀樹或多執行緒）、"
     "實際執行常常比解法三慢（找前驅的常數不小）。",
   ], "O(n)", "O(1)", "攤還每條邊常數次", "只用五個指標"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、收集 + 排序", "O(n log n)", "O(n)", "短", "最保險，連「換三個」都能修"],
    ["二、中序遞迴找逆序", "O(n)", "O(h)", "短", "面試預設答案"],
    ["三、中序迭代找逆序", "O(n)", "O(h)", "中", "沒有遞迴深度問題"],
    ["四、Morris", "O(n)", "O(1)", "長", "唯一滿足進階的解"]]),
 "post": [
   ("note", "面試時的講法建議", [
     ("c", """1. 先說出那把鑰匙：
   「BST 的中序走訪是嚴格遞增的，
     所以交換兩個值，就會在中序序列上留下逆序點。」

2. 給保底解（收集 + 排序），說「這一定對，O(n log n)」。

3. 升級到「找逆序點」，講清楚【兩個逆序點 vs 一個逆序點】
   這兩種情況，以及 first / second 的更新規則。
   ★ 這一步是本題的核心，講不清楚就等於沒解出來。

4. 被問到 O(1) 空間，再端出 Morris。

【第 3 步的「兩種情況」是面試官真正在看的東西。】
很多人寫出程式碼卻說不出「為什麼 second 要每次覆蓋」——
那代表是背來的，不是想出來的。"""),
   ]),
 ],
 "edges": [
   "<strong><code>[1,3,null,null,2]</code></strong> → 換 1 和 3（官方範例 1）。",
   "<strong><code>[3,1,4,null,null,2]</code></strong> → 換 2 和 3（官方範例 2）。",
   "<strong>被交換的兩個節點在中序裡相鄰</strong>（情況 B）→ "
   "<strong>只有一個逆序點</strong>。"
   "<strong>沒處理這個情況的話，<code>second</code> 會是 <code>None</code>，"
   "直接 crash —— 這是本題第一名的 bug。</strong>",
   "<strong>被交換的是根節點和某個葉子</strong> → 一樣用同一套邏輯處理。",
   "<strong>只有兩個節點</strong> <code>[2,3]</code>（3 是左孩子）→ "
   "中序是 <code>3, 2</code>，一個逆序點，換回來變 <code>[3,2]</code>。",
   "<strong><code>first</code> 寫成「每次都更新」</strong> → "
   "情況 A 會抓到錯的節點（抓到第二個逆序點的前者）。",
   "<strong><code>second</code> 寫成「只設一次」</strong> → "
   "情況 A 會抓到錯的節點（抓到第一個逆序點的後者）。",
   "<strong><code>prev</code> 存值而不是節點</strong> → 最後不知道要改哪個節點的 "
   "<code>val</code>。",
   "<strong>Morris 版中途 <code>return</code></strong> → 樹上留下沒拆的線，變成有環。",
 ],
 "follow": [
   ("h", "追問一：如果有 k 個節點被交換（k > 2）呢？"),
   "<strong>「找逆序點」的邏輯就不夠用了</strong> —— "
   "k 個錯位可能產生任意數量的逆序點，而且對應關係不再單純。",
   "<strong>解法一（收集 + 排序）卻完全不受影響</strong>，"
   "因為它根本不管「錯了幾個」，直接把正確的值填回正確的位置。"
   "<strong>這就是「笨解法」的價值 —— 它的正確性不依賴題目的特殊假設。</strong>",
   "如果只想<strong>找出「哪些節點被動過」</strong>："
   "把中序序列和它的排序版逐項比對，不相等的位置就是被動過的節點。"
   "<strong>O(n log n) 時間、O(n) 空間。</strong>",
   ("h", "追問二：如果是「兩個節點的位置被交換」（連同子樹一起搬）呢？"),
   "<strong>那就是完全不同的題目了</strong> —— 樹的形狀變了，"
   "中序序列不再只是「兩個元素互換」，而是「兩段子序列互換」。",
   "<strong>本題明確說「不改變結構」，所以只有 <code>val</code> 被動過。</strong>"
   "<strong>讀題時要抓住這個關鍵字。</strong>",
   ("h", "追問三：Morris 走訪還能做什麼？"),
   ("ul", [
     "<strong>第 94 題</strong>：中序走訪，O(1) 空間",
     "<strong>第 98 題</strong>：驗證 BST，O(1) 空間",
     "<strong>本題</strong>：復原 BST，O(1) 空間",
     "<strong>第 114 題</strong>：把二元樹攤平成鏈結串列（Morris 的變形）",
     "<strong>前序版</strong>：只要把「輸出的時機」從「拆線時」改成「架線時」",
   ]),
   "<strong>後序版也存在但複雜很多</strong>（需要「反轉右邊緣」的技巧），"
   "面試幾乎不會考。",
   ("h", "追問四：能不能一趟就知道「有沒有被交換」？"),
   "<strong>可以 —— 那就是第 98 題</strong>。"
   "本題和第 98 題的差別只在：<strong>第 98 題發現逆序就回 <code>False</code>，"
   "本題發現逆序要記下來繼續走</strong>。",
   ("c", """98 題：  if prev.val > node.val: return False
99 題：  if prev.val > node.val:
             if first is None: first = prev
             second = node

【同一個骨架，不同的動作。】

這種「一個模板解一整類題」的感覺，
正是刷題的真正收穫 ——
不是記住 100 個解法，而是記住 10 個骨架。"""),
 ],
 "related": [
   "<strong>第 98 題 Validate Binary Search Tree</strong> —— 同一把鑰匙，只是判斷不修復",
   "<strong>第 94 題 Binary Tree Inorder Traversal</strong> —— 中序走訪的三種寫法",
   "<strong>第 173 題 Binary Search Tree Iterator</strong> —— 把中序拆成迭代器",
   "<strong>第 114 題 Flatten Binary Tree to Linked List</strong> —— Morris 的變形",
   "<strong>第 230 題 Kth Smallest Element in a BST</strong> —— 同一個中序骨架",
 ],
 "check": [
   "為什麼「交換兩個值」在中序序列上最多只會產生兩個逆序點？請證明一遍。",
   "<code>first</code> 為什麼只在第一次逆序時設定，<code>second</code> 為什麼每次都覆蓋？",
   "被交換的兩個節點在中序裡相鄰時會發生什麼？沒處理會怎麼壞？",
   "為什麼這題的 <code>if prev</code> 可以不寫 <code>is not None</code>，第 98 題卻非寫不可？",
   "Morris 走訪的時間複雜度為什麼還是 O(n)，而不是 O(n²)？",
 ],
})
print("P99 written")

# ==================== 100. Same Tree ====================
S["p100_rec"] = '''class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True                    # 兩邊都空 -> 相同
        if not p or not q:
            return False                   # 只有一邊空 -> 不同
        if p.val != q.val:
            return False                   # 值不同 -> 不同
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))'''

S["p100_oneline"] = '''class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p is q                  # 至少一邊是 None：只有都是 None 才相同
        return (p.val == q.val
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right))'''

S["p100_bfs"] = '''from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        dq = deque([(p, q)])               # 一次比一「對」節點

        while dq:
            a, b = dq.popleft()
            if not a and not b:
                continue                   # 兩邊都空，這一對沒問題
            if not a or not b or a.val != b.val:
                return False
            dq.append((a.left, b.left))    # 左對左
            dq.append((a.right, b.right))  # 右對右

        return True'''

S["p100_stack"] = '''class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            a, b = stack.pop()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            stack.append((a.left, b.left))
            stack.append((a.right, b.right))

        return True'''

S["p100_serial"] = '''class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def ser(node) -> str:
            if not node:
                return "#"                 # 空節點一定要留下記號
            return "(%s,%d,%s)" % (ser(node.left), node.val, ser(node.right))

        return ser(p) == ser(q)'''


def _p100_ref(p, q):
    """獨立參考解：把兩棵樹各自序列化成巢狀 tuple 再比較。"""
    def enc(node):
        return None if node is None else (enc(node.left), node.val, enc(node.right))
    return enc(p) == enc(q)


def _rand_tree100(n, lo, hi):
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi),
                    _rand_tree100(left, lo, hi),
                    _rand_tree100(n - 1 - left, lo, hi))


def _clone100(nd):
    return None if nd is None else TreeNode(nd.val, _clone100(nd.left), _clone100(nd.right))


_p100 = [S.load(k) for k in
         ("p100_rec", "p100_oneline", "p100_bfs", "p100_stack", "p100_serial")]

for sp, sq, want in [
    ([1, [2, None, None], [3, None, None]], [1, [2, None, None], [3, None, None]], True),
    ([1, [2, None, None], None], [1, None, [2, None, None]], False),
    ([1, [2, None, None], [1, None, None]], [1, [1, None, None], [2, None, None]], False),
    (None, None, True),
    (None, [1, None, None], False),
    ([1, None, None], None, False),
    ([1, None, None], [1, None, None], True),
    ([0, None, None], [0, None, None], True),
]:
    a, b = _build(sp), _build(sq)
    assert _p100_ref(a, b) is want, ("P100 ref", sp, sq)
    for sol in _p100:
        assert sol.isSameTree(_build(sp), _build(sq)) is want, ("P100", sp, sq, sol)

# 隨機壓力測試
for _ in range(6000):
    n = random.randrange(0, 8)
    a = _rand_tree100(n, 0, 3)
    r = random.random()
    if r < 0.35:
        b = _clone100(a)                       # 保證相同
    elif r < 0.7 and n > 0:
        b = _clone100(a)                       # 改一個值
        nds = _nodes_inorder(b)
        t = random.choice(nds)
        t.val = t.val + random.choice([-1, 1])
    else:
        b = _rand_tree100(random.randrange(0, 8), 0, 3)   # 完全隨機
    want = _p100_ref(a, b)
    for sol in _p100:
        got = sol.isSameTree(a, b)
        assert got is want, ("P100 random", want, got, sol)

# 序列化版的分隔符必須夠嚴謹：兩棵結構不同但「值序列相同」的樹
_t1 = _build([1, [2, None, None], None])       # 1 的左孩子是 2
_t2 = _build([1, None, [2, None, None]])       # 1 的右孩子是 2
assert _p100_ref(_t1, _t2) is False
for sol in _p100:
    assert sol.isSameTree(_t1, _t2) is False, ("P100 structure", sol)
print("P100 solutions OK")

_P100_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">「相同」= 結構一樣 而且 對應位置的值也一樣。少了任何一個條件都不算。</text>
            <text x="20" y="52" fill="var(--accent)" font-size="13">✔ 相同</text>
            <g font-size="14" text-anchor="middle">
              <circle cx="90" cy="92" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="90" y="97" fill="var(--accent)">1</text>
              <circle cx="50" cy="150" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="50" y="155" fill="var(--accent)">2</text>
              <circle cx="130" cy="150" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="130" y="155" fill="var(--accent)">3</text>
              <circle cx="230" cy="92" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="230" y="97" fill="var(--accent)">1</text>
              <circle cx="190" cy="150" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="190" y="155" fill="var(--accent)">2</text>
              <circle cx="270" cy="150" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="270" y="155" fill="var(--accent)">3</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="77" y1="105" x2="63" y2="137"/><line x1="103" y1="105" x2="117" y2="137"/>
              <line x1="217" y1="105" x2="203" y2="137"/><line x1="243" y1="105" x2="257" y2="137"/>
            </g>
            <text x="340" y="52" fill="#ff8a65" font-size="13">✘ 不同（結構不一樣）</text>
            <g font-size="14" text-anchor="middle">
              <circle cx="410" cy="92" r="18" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="410" y="97" fill="#ff8a65">1</text>
              <circle cx="370" cy="150" r="18" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="370" y="155" fill="#ff8a65">2</text>
              <circle cx="530" cy="92" r="18" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="530" y="97" fill="#ff8a65">1</text>
              <circle cx="570" cy="150" r="18" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="570" y="155" fill="#ff8a65">2</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="397" y1="105" x2="383" y2="137"/>
              <line x1="543" y1="105" x2="557" y2="137"/>
            </g>
            <text x="340" y="186" fill="var(--text-muted)" font-size="11">值的集合都是 {1, 2}，但一個掛左邊、一個掛右邊。</text>
            <line x1="20" y1="208" x2="620" y2="208" stroke="var(--border)"/>
            <text x="20" y="236" fill="var(--gold)" font-size="12">遞迴的三個 base case（順序不能亂）：</text>
            <text x="20" y="262" fill="var(--text-muted)" font-size="12">1. 兩邊都是 None → True　　2. 只有一邊是 None → False　　3. 值不同 → False</text>
            <text x="20" y="288" fill="var(--accent)" font-size="12">然後才遞迴：左對左、右對右。【注意：不能左對右 —— 那是第 101 題「對稱樹」。】</text>
            <text x="20" y="318" fill="var(--text-muted)" font-size="12">把 1 和 2 寫反（先檢查「只有一邊空」）會怎樣？兩邊都空時會誤判成 False —— 空樹和空樹其實相同。</text>'''

emit({
 "num": 100, "slug": "same-tree",
 "en": [
   "Given the roots of two binary trees <code>p</code> and <code>q</code>, write a function "
   "to check if they are the same or not.",
   "Two binary trees are considered the same if they are structurally identical, and the "
   "nodes have the same value.",
 ],
 "zh": [
   "給你兩棵二元樹的根節點 <code>p</code> 和 <code>q</code>，判斷它們是否<strong>相同</strong>。",
   "兩棵二元樹<strong>相同</strong>的條件是："
   "<strong>結構完全一致</strong>，而且<strong>對應位置的節點值也相同</strong>。",
   ("note", "第 100 題，一個里程碑", [
     "<strong>恭喜你走到第 100 題。</strong>"
     "這題是<strong>樹的遞迴</strong>最乾淨的起點 —— "
     "五行程式碼，卻包含了所有樹題目的共同骨架。",
     "<strong>如果你能把這題的三個 base case 說清楚，"
     "後面幾百道樹的題目都只是它的變形。</strong>",
   ]),
 ],
 "pre": [
   ("note", "「相同」的兩個條件，缺一不可", [
     ("c", """1. 結構一致（每個位置有沒有節點，完全一樣）
2. 對應位置的值一樣

    只滿足 2 不算 ——

        1              1
       /                \\
      2                  2

    兩棵樹的「值」都是 {1, 2}，但一個掛左邊、一個掛右邊。
    【不同。】

    只滿足 1 也不算 ——

        1              1
       / \\            / \\
      2   3          2   4

    結構一模一樣，但 3 != 4。
    【不同。】

【這兩個條件在遞迴裡剛好對應到「檢查 None」和「檢查 val」。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：p = [1,2,3], q = [1,2,3]

        1            1
       / \\          / \\
      2   3        2   3

  輸出：true

範例 2
  輸入：p = [1,2], q = [1,null,2]

        1            1
       /              \\
      2                2

  輸出：false   （結構不同）

範例 3
  輸入：p = [1,2,1], q = [1,1,2]

        1            1
       / \\          / \\
      2   1        1   2

  輸出：false   （對應位置的值不同）""",
 "constraints": [
   "兩棵樹的節點數都在 <code>[0, 100]</code> 之間",
   "−10⁴ ≤ <code>Node.val</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "注意：節點數可以是 0", [
     "<strong>所以 <code>p</code> 和 <code>q</code> 都可能是 <code>None</code></strong>。",
     "<strong><code>isSameTree(None, None)</code> 必須回 <code>True</code></strong>"
     "（兩棵空樹是相同的）。<strong>這是最容易被漏掉的測資。</strong>",
   ]),
 ],
 "idea": [
   ("fig", _P100_FIG, "0 0 640 336"),
   ("c", """把定義直接翻成遞迴：

    「p 和 q 相同」
        ⟺ 根節點相同 且 左子樹相同 且 右子樹相同

三個 base case，【順序很重要】：

    1. not p and not q  -> True      兩邊都空，相同
    2. not p or not q   -> False     只有一邊空，結構就不一樣了
    3. p.val != q.val   -> False     都存在但值不同

    然後遞迴：
        isSame(p.left, q.left) and isSame(p.right, q.right)

【為什麼 1 一定要在 2 前面？】

    如果先寫 2（not p or not q -> False），
    那麼 p 和 q 都是 None 時也會進到這一條 -> 回 False ✘

    但兩棵空樹明明是相同的。

    正確的順序是：
        先排除「都空」（True），再排除「只有一邊空」（False）。

    【這是本題唯一的陷阱，也是它值得被當成第 100 題的原因 ——
      它逼你把 base case 的順序想清楚。】

【為什麼 3 要在遞迴之前？】

    這只是效率問題（提早發現不同就不用往下走），
    不影響正確性。但寫在前面更自然。""",),
   "<strong>遞迴、BFS、DFS 迭代、序列化 —— 四種寫法都很短</strong>，"
   "差別只在「用什麼方式同步走訪兩棵樹」。",
 ],
 "approaches": [
   ap("解法一", "遞迴（標準答案，五行）", [
     ("c", S["p100_rec"]),
     "<strong>三個 <code>if</code> 加一行遞迴，就是全部。</strong>"
     "這是樹題目最標準的形狀，值得背下來當模板。",
     ("h", "手動走一遍範例 2"),
     ("c", """p = [1,2]      q = [1,null,2]

        1            1
       /              \\
      2                2

isSame(p=1, q=1)
    兩個都不是 None ✔
    1 == 1 ✔
    -> isSame(p.left=2, q.left=None) and isSame(p.right=None, q.right=2)

    isSame(2, None)
        not p and not q ？ p 存在 -> 否
        not p or not q  ？ q 是 None -> 【是】 -> return False ✔

    短路，右邊不用算了 -> False ✔"""),
     ("h", "複雜度"),
     ("c", """時間 O(min(m, n))

    注意【不是 O(m + n)】——
    因為只要有一邊走完（或發現不同）就會停，
    最多只會訪問「兩棵樹的共同部分」。

    實務上常寫成 O(n)，但說得出 min(m, n) 會加分。

空間 O(min(m, n)) 最壞情況

    遞迴堆疊的深度 = min(兩棵樹的高度)。
    平衡樹是 O(log n)，退化成鏈時是 O(n)。

    本題 n <= 100，完全不用擔心。"""),
   ], "O(min(m, n))", "O(min(h₁, h₂))", "只走共同部分", "遞迴堆疊", optimal=True),

   ap("解法二", "遞迴（更精簡的寫法）", [
     ("c", S["p100_oneline"]),
     ("h", "<code>return p is q</code> 這一手"),
     ("c", """if not p or not q:
    return p is q

    走到這一行時，代表【至少有一邊是 None】。

    如果兩邊都是 None  -> p is q 為 True  ✔
    如果只有一邊是 None -> 一個是 None、一個是節點物件
                        -> p is q 為 False ✔

    一行取代了原本的兩個 if。

【為什麼用 is 而不是 ==？】

    is 比較的是「同一個物件」，
    而 None 在 Python 裡是單例（只有一個 None 物件）。

    用 == 在這裡也會對，但 == 可能觸發 __eq__，
    語意上不夠精確。
    【比較 None 一律用 is，這是 Python 的慣例（PEP 8）。】"""),
     "<strong>精簡不等於比較好</strong> —— "
     "面試時<strong>解法一更容易讓面試官跟上你的思路</strong>。"
     "這個版本適合在寫完解法一之後說「也可以壓成這樣」。",
   ], "O(min(m, n))", "O(min(h₁, h₂))", "同解法一", "遞迴堆疊"),

   ap("解法三", "BFS 迭代（用佇列同步走訪）", [
     ("c", S["p100_bfs"]),
     ("h", "核心：佇列裡放的是「一對節點」"),
     ("c", """dq = deque([(p, q)])

    每次取出一「對」要比較的節點，
    然後把它們的 (左, 左) 和 (右, 右) 再放進去。

    【關鍵是「成對」地走 ——
      兩棵樹用同一個節奏往下推進。】

    如果一對都是 None -> continue（這一對沒問題，不用往下）
    如果只有一邊 None 或值不同 -> 立刻 return False

這個「成對推進」的想法，在下面這些題目裡會一再出現：

    101  Symmetric Tree      -> 放 (左.left, 右.right) 和 (左.right, 右.left)
    572  Subtree of Another  -> 對每個節點呼叫一次 isSameTree
    951  Flip Equivalent BT  -> 兩種配對方式都試
    1367 Linked List in BT   -> 樹和鏈結串列成對推進"""),
     "<strong>沒有遞迴深度限制</strong>。"
     "本題 n ≤ 100 用不到，但<strong>面試官問「能不能不用遞迴」時就是它</strong>。",
     "<strong>空間 O(w)</strong>（w 是樹的最大寬度）—— "
     "<strong>完全二元樹時是 O(n/2) = O(n)，其實比遞迴版差</strong>。"
     "<strong>BFS 換掉的是「深度風險」，不是空間。</strong>",
   ], "O(min(m, n))", "O(w)", "每對節點一次", "佇列最大寬度"),

   ap("解法四", "DFS 迭代（把 deque 換成 stack）", [
     ("c", S["p100_stack"]),
     "<strong>和解法三只差一個字</strong>："
     "<code>popleft()</code>（佇列，BFS）改成 <code>pop()</code>（堆疊，DFS）。",
     ("c", """【這是一個很值得注意的現象】：

    BFS 和 DFS 的迭代版，程式碼結構完全一樣，
    差別只在「從哪一端取出元素」。

        popleft()  -> 先進先出 -> BFS（一層一層）
        pop()      -> 後進先出 -> DFS（一路走到底）

    對「判斷是否相同」這件事來說，
    【走訪順序完全不影響答案】——
    因為我們要檢查「每一對」，順序無所謂。

    所以兩個版本都對，挑順手的寫。

    （但如果題目問「最先發現的不同在哪裡」，
      那順序就有意義了。）""",),
     "<strong>空間 O(h)</strong> —— 對深而窄的樹，這比 BFS 省。",
   ], "O(min(m, n))", "O(h)", "每對節點一次", "堆疊深度"),

   ap("解法五", "序列化後比較字串（有陷阱，但概念重要）", [
     ("c", S["p100_serial"]),
     ("h", "空節點的記號 <code>#</code> 絕對不能省"),
     ("c", """如果序列化時忽略空節點：

        1              1
       /                \\
      2                  2

    前序（跳過空節點）： "1,2"  和  "1,2"   -> 誤判成相同 ✘

加上空節點的記號之後：

        "(( #,2,# ),1,#)"   和   "(#,1,( #,2,# ))"   -> 不同 ✔

【一個序列化方式要能「唯一決定」一棵樹，
  就必須記錄空節點的位置。】

    這在第 297 題（序列化與反序列化二元樹）是核心考點。

    另一個等價的做法是「前序 + 中序」兩條序列 ——
    但那需要值互不重複才成立，限制更多。""",),
     ("h", "為什麼這個解法「不推薦」？"),
     ("ul", [
       "<strong>時間和空間都是 O(n)</strong>，而且常數大（字串拼接）。",
       "<strong>沒有提早結束</strong> —— 就算第一個節點就不同，"
       "也得把兩棵樹整個序列化完。",
       "<strong>字串比較本身是 O(n)</strong>，等於多走了一遍。",
     ]),
     "<strong>但它的概念很有用</strong>："
     "當你要<strong>「把一棵樹當成雜湊表的鍵」</strong>"
     "或<strong>「找出所有重複的子樹」</strong>（第 652 題）時，"
     "<strong>序列化就是標準做法</strong>。",
   ], "O(m + n)", "O(m + n)", "一定走完整棵樹", "兩條字串"),
 ],
 "compare": (["解法", "時間", "空間", "提早結束", "備註"],
   [["一、遞迴", "O(min(m,n))", "O(min(h₁,h₂))", "✔", "標準答案"],
    ["二、遞迴精簡版", "O(min(m,n))", "O(min(h₁,h₂))", "✔", "p is q 的小技巧"],
    ["三、BFS 迭代", "O(min(m,n))", "O(w)", "✔", "沒有遞迴深度問題"],
    ["四、DFS 迭代", "O(min(m,n))", "O(h)", "✔", "和三只差一個字"],
    ["五、序列化比較", "O(m+n)", "O(m+n)", "✘", "概念重要，效率差"]]),
 "post": [
   ("note", "這題是「樹的遞迴模板」的最小範例", [
     ("c", """幾乎所有樹的遞迴題目都長這樣：

    def go(node):
        if <base case>:        # 1. 空節點怎麼辦
            return <base 值>
        <對 node 本身做檢查>     # 2. 當前節點的邏輯
        left  = go(node.left)  # 3. 交給子問題
        right = go(node.right)
        return <合併 left 和 right>   # 4. 把子答案合起來

本題只是把它從「一棵樹」擴展成「兩棵樹同步走」。

    def go(a, b):
        if not a and not b: return True
        if not a or not b:  return False
        if a.val != b.val:  return False
        return go(a.left, b.left) and go(a.right, b.right)

【一旦你掌握這個形狀，下面這些題目都是同一招換皮】：

    101  Symmetric Tree            go(a.left, b.right) and go(a.right, b.left)
    226  Invert Binary Tree        交換左右再遞迴
    104  Maximum Depth             1 + max(左, 右)
    110  Balanced Binary Tree      回傳 (高度, 是否平衡)
    543  Diameter of Binary Tree   在遞迴中順便更新全域最大值
    124  Max Path Sum              同上，但值可能是負的

    【第 100 題是這一整片森林的入口。】"""),
   ]),
 ],
 "edges": [
   "<strong><code>p = None, q = None</code></strong> → <code>True</code>。"
   "<strong>把 base case 順序寫反就會錯，這是本題第一名的 bug。</strong>",
   "<strong><code>p = None, q = [1]</code></strong> → <code>False</code>。",
   "<strong><code>p = [1], q = [1]</code></strong> → <code>True</code>。",
   "<strong><code>p = [1,2], q = [1,null,2]</code></strong> → <code>False</code>（結構不同）。",
   "<strong><code>p = [1,2,1], q = [1,1,2]</code></strong> → <code>False</code>（值不對位）。",
   "<strong>節點值是 <code>0</code></strong> → "
   "如果你用 <code>if not node.val</code> 之類的寫法會爆炸。"
   "<strong>檢查節點存在請用 <code>if not node</code>，不要碰 <code>val</code> 的真假值。</strong>",
   "<strong>把遞迴寫成 <code>go(p.left, q.right)</code></strong> → "
   "那是第 101 題（對稱樹），不是這題。",
   "<strong>序列化版忘了寫空節點記號</strong> → <code>[1,2]</code> 和 "
   "<code>[1,null,2]</code> 會誤判成相同。",
 ],
 "follow": [
   ("h", "追問一：如果要判斷「兩棵樹是否對稱」呢？"),
   "<strong>第 101 題</strong>。只要把遞迴的配對方式改掉：",
   ("c", """相同（第 100 題）：
    go(a.left,  b.left)  and go(a.right, b.right)

對稱（第 101 題）：
    go(a.left,  b.right) and go(a.right, b.left)
        ^^^^^^^^^^^^^^^        ^^^^^^^^^^^^^^^
        左對右                  右對左

    然後對單棵樹呼叫 go(root.left, root.right)。

【一模一樣的骨架，只改了兩個字。】""",),
   ("h", "追問二：如果要判斷「q 是不是 p 的子樹」呢？"),
   "<strong>第 572 題</strong>。最直接的做法："
   "<strong>對 <code>p</code> 的每個節點呼叫一次 <code>isSameTree(節點, q)</code></strong>。"
   "時間 <code>O(m × n)</code>。",
   "<strong>更快的做法</strong>：把兩棵樹都序列化（含空節點記號），"
   "然後用 <strong>KMP</strong> 檢查 <code>q</code> 的序列是不是 <code>p</code> 的"
   "<strong>子字串</strong> —— <code>O(m + n)</code>。",
   "<strong>但要小心</strong>：序列化時<strong>每個值前面要加分隔符</strong>"
   "（例如 <code>,12</code>），否則 <code>12</code> 會錯誤地匹配到 <code>112</code> 的一部分。"
   "<strong>這是「把樹題轉成字串題」最經典的坑。</strong>",
   ("h", "追問三：如果節點可以有任意多個孩子（N 元樹）呢？"),
   ("c", """def isSame(p, q):
    if not p and not q: return True
    if not p or not q:  return False
    if p.val != q.val:  return False
    if len(p.children) != len(q.children): return False     # 新增的檢查
    return all(isSame(a, b) for a, b in zip(p.children, q.children))

【多了一個「孩子數量要相同」的檢查。】

如果孩子的【順序不重要】（無序樹），問題就難很多 ——
要做「樹的同構判定」，
標準做法是 AHU 演算法（把每棵子樹的簽章排序後往上合併），
時間仍是 O(n)，但實作複雜得多。""",),
   ("h", "追問四：如果兩棵樹超大，放不進單一台機器呢？"),
   "<strong>用「樹的雜湊（Merkle tree）」</strong>："
   "每個節點的雜湊值 = <code>hash(值, 左子樹雜湊, 右子樹雜湊)</code>。",
   "<strong>比較兩棵樹只要比較根的雜湊值</strong> —— "
   "<strong>而且可以只傳 32 bytes 就判斷完</strong>。",
   "<strong>如果不同，還能沿著雜湊不同的路徑往下找，快速定位差異在哪</strong> —— "
   "<strong>Git、IPFS、區塊鏈用的就是這一招</strong>。",
   "<strong>代價</strong>：雜湊碰撞的機率（理論上可能誤判成相同），"
   "以及<strong>要先把整棵樹算過一遍</strong>。",
 ],
 "related": [
   "<strong>第 101 題 Symmetric Tree</strong> —— 同一個骨架，改配對方式",
   "<strong>第 572 題 Subtree of Another Tree</strong> —— 反覆呼叫本題",
   "<strong>第 104 題 Maximum Depth of Binary Tree</strong> —— 樹遞迴模板的另一個最小範例",
   "<strong>第 226 題 Invert Binary Tree</strong> —— 樹遞迴的經典入門",
   "<strong>第 297 題 Serialize and Deserialize Binary Tree</strong> —— 序列化為什麼要記空節點",
 ],
 "check": [
   "三個 base case 的順序為什麼不能調換？把前兩個寫反會在哪個測資掛掉？",
   "時間複雜度為什麼是 <code>O(min(m, n))</code> 而不是 <code>O(m + n)</code>？",
   "序列化解法裡，空節點的記號 <code>#</code> 為什麼不能省？",
   "要改成「判斷對稱」（第 101 題），遞迴那一行要怎麼改？",
 ],
})
print("P100 written")
