# -*- coding: utf-8 -*-
"""第 113–116 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(113)


def _build(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _build(l), _build(r))


def _rand_tree(n, lo=-4, hi=4):
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi), _rand_tree(left, lo, hi), _rand_tree(n - 1 - left, lo, hi))


# ==================== 113. Path Sum II ====================
S["p113"] = '''class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res, path = [], []

        def go(node, rest):
            if not node:
                return

            path.append(node.val)                 # 選擇
            rest -= node.val

            if not node.left and not node.right and rest == 0:
                res.append(path[:])               # ★ 一定要複製一份
            else:
                go(node.left, rest)
                go(node.right, rest)

            path.pop()                            # 撤銷選擇（回溯）

        go(root, targetSum)
        return res'''

S["p113_immutable"] = '''class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def go(node, rest, path):
            if not node:
                return
            path = path + [node.val]              # 每次造一條新的 path -> 不用撤銷
            rest -= node.val
            if not node.left and not node.right:
                if rest == 0:
                    res.append(path)
                return
            go(node.left, rest, path)
            go(node.right, rest, path)

        go(root, targetSum, [])
        return res'''

S["p113_iter"] = '''class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        stack = [(root, targetSum - root.val, [root.val])]
        while stack:
            node, rest, path = stack.pop()
            if not node.left and not node.right and rest == 0:
                res.append(path)
            if node.right:
                stack.append((node.right, rest - node.right.val, path + [node.right.val]))
            if node.left:
                stack.append((node.left, rest - node.left.val, path + [node.left.val]))

        return res'''


def _p113_ref(root, target):
    """獨立參考解：列出所有根到葉的路徑，再篩出和等於 target 的。"""
    out = []
    def go(nd, path):
        if nd is None:
            return
        path = path + [nd.val]
        if not nd.left and not nd.right:
            if sum(path) == target:
                out.append(path)
            return
        go(nd.left, path)
        go(nd.right, path)
    go(root, [])
    return out


_p113 = [S.load(k) for k in ("p113", "p113_immutable", "p113_iter")]

for spec, tgt, want in [
    ([5, [4, [11, [7, None, None], [2, None, None]], None],
         [8, [13, None, None], [4, [5, None, None], [1, None, None]]]], 22,
     [[5, 4, 11, 2], [5, 8, 4, 5]]),
    ([1, [2, None, None], [3, None, None]], 5, []),
    ([1, [2, None, None], None], 0, []),
    (None, 0, []),
]:
    t = _build(spec)
    assert _p113_ref(t, tgt) == want, ("P113 ref", spec, tgt, _p113_ref(t, tgt))
    for sol in _p113:
        assert sol.pathSum(_build(spec), tgt) == want, ("P113", spec, tgt, sol)

for _ in range(3000):
    t = _rand_tree(random.randrange(0, 11))
    for tgt in range(-6, 7):
        want = _p113_ref(t, tgt)
        for sol in _p113:
            got = sol.pathSum(t, tgt)
            assert got == want, ("P113 random", tgt, want, got, sol)
print("P113 solutions OK")

_P113_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">回溯（backtracking）的三個動作：選擇 → 遞迴 → 撤銷。path 這條 list 全程只有一份。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">走到 5 → 4 → 11 → 7 的過程中，path 的變化：</text>
            <g font-size="13">
              <text x="40" y="84" fill="var(--text-muted)">進入 5　　append(5)　　path = [5]</text>
              <text x="60" y="110" fill="var(--text-muted)">進入 4　　append(4)　　path = [5, 4]</text>
              <text x="80" y="136" fill="var(--text-muted)">進入 11　 append(11)　 path = [5, 4, 11]</text>
              <text x="100" y="162" fill="var(--accent)">進入 7　　append(7)　　path = [5, 4, 11, 7]　rest = 0？ 否 → 不收</text>
              <text x="100" y="188" fill="#ff8a65">離開 7　　pop()　　　　path = [5, 4, 11]　　★ 撤銷，換下一條路</text>
              <text x="100" y="214" fill="var(--gold)">進入 2　　append(2)　　path = [5, 4, 11, 2]　rest = 0 ✔ → 收！</text>
              <text x="100" y="240" fill="#ff8a65">離開 2　　pop()　　　　path = [5, 4, 11]</text>
              <text x="80" y="266" fill="#ff8a65">離開 11　 pop()　　　　path = [5, 4]</text>
            </g>
            <line x1="20" y1="288" x2="620" y2="288" stroke="var(--border)"/>
            <text x="20" y="316" fill="#ff8a65" font-size="13">★ 為什麼收集時一定要寫 path[:] 而不是 path？</text>
            <text x="20" y="342" fill="var(--text-muted)" font-size="12">因為 path 是【同一個 list 物件】，後面還會被 pop 和 append 改來改去。</text>
            <text x="20" y="366" fill="var(--text-muted)" font-size="12">res.append(path) 存進去的只是一個【參考】——走完之後 path 會變回 []，</text>
            <text x="20" y="390" fill="var(--text-muted)" font-size="12">於是 res 裡每一筆都指向那個空 list，答案變成 [[], [], ...]。</text>
            <text x="20" y="418" fill="var(--accent)" font-size="12">path[:]（或 list(path)、copy.copy(path)）會造出一份快照，才是正確的做法。</text>'''

emit({
 "num": 113, "slug": "path-sum-ii",
 "en": [
   "Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return "
   "<em>all <strong>root-to-leaf</strong> paths where the sum of the node values in the path "
   "equals</em> <code>targetSum</code>. Each path should be returned as a list of the node "
   "<strong>values</strong>, not node references.",
   "A <strong>root-to-leaf</strong> path is a path starting from the root and ending at any "
   "leaf node. A <strong>leaf</strong> is a node with no children.",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code> 和一個整數 <code>targetSum</code>。",
   "找出<strong>所有</strong>從根到葉、且路徑上節點值總和等於 <code>targetSum</code> 的路徑。",
   "每條路徑請回傳<strong>節點值的 list</strong>（不是節點物件）。",
 ],
 "pre": [
   ("note", "從「有沒有」到「有哪些」——回溯登場", [
     ("c", """第 112 題問「存不存在」-> 找到一條就可以 return True。
第 113 題問「有哪些」  -> 必須【走完整棵樹】，而且要記住走過的路。

【這個差別帶來三個新東西】：

  1. 要維護一條 path（目前走到哪裡）
  2. 走完一個分支要【撤銷】（回溯），才能走另一個分支
  3. 收集答案時要【複製一份】

    第 3 點是本題第一名的 bug，
    而且它不會報錯 —— 你會得到 [[], [], []] 這種結果。

【回溯（backtracking）的骨架，背起來】：

    def go(狀態):
        if 找到答案:
            res.append(目前狀態的【複製】)
            return
        for 每個選擇:
            做選擇           # append
            go(新狀態)
            撤銷選擇         # pop

    第 39、46、78、79、93、131 題用的都是它。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22

              5
             / \\
            4   8
           /   / \\
          11  13  4
         /  \\    / \\
        7    2  5   1

  輸出：[[5,4,11,2],[5,8,4,5]]

範例 2
  輸入：root = [1,2,3], targetSum = 5
  輸出：[]

範例 3
  輸入：root = [1,2], targetSum = 0
  輸出：[]""",
 "constraints": [
   "樹的節點數在 <code>[0, 5000]</code> 之間",
   "−1000 ≤ <code>Node.val</code> ≤ 1000",
   "−1000 ≤ <code>targetSum</code> ≤ 1000",
 ],
 "idea": [
   ("fig", _P113_FIG, "0 0 640 436"),
   ("c", """回溯三部曲，一個都不能少：

    path.append(node.val)        # 1. 選擇：把自己加進路徑
    ...遞迴左右子樹...
    path.pop()                   # 3. 撤銷：離開時把自己拿掉

    # 2. 在葉節點檢查
    if 是葉節點 and rest == 0:
        res.append(path[:])      # ★ 複製快照

【為什麼要撤銷？】

    因為 path 是【全域共用的一條 list】。

    走完左子樹之後，path 裡還留著左子樹的節點；
    如果不清掉就去走右子樹，
    path 會變成「左子樹 + 右子樹」的大雜燴 ✘

    pop() 把「進入這個節點時 append 的那一個」拿掉，
    讓 path 回到「進來之前的樣子」——
    這就是「回溯」這個名字的來源。

【不變量（invariant）】：
    go(node) 開始執行時，path = 從根到 node.parent 的路徑
    go(node) 結束執行時，path 必須【完全相同】

    每個 append 都要有對應的 pop，
    就像每個開括號都要有閉括號。"""),
 ],
 "approaches": [
   ap("解法一", "回溯 + 共用 path（標準答案）", [
     ("c", S["p113"]),
     ("h", "★ <code>path[:]</code> 為什麼不能省"),
     ("c", """res.append(path)      ✘ 只存了一個【參考】
res.append(path[:])   ✔ 存了一份【快照】

    Python 的 list 是可變物件，
    res.append(path) 存進去的是「那個 list 的地址」。

    之後 path.pop() 會改到【同一個物件】——
    res 裡那一筆也跟著變了。

    走完整棵樹之後 path 會回到 []，
    於是 res = [[], [], []]  ✘

【四種複製寫法，都可以】：
    path[:]           最短，最常用
    list(path)        最明確
    path.copy()       Python 3.3+
    copy.copy(path)   最囉唆

    【注意這些都是「淺複製」】——
    對 list of int 來說完全夠用。
    但如果 path 裡裝的是 list（例如二維路徑），
    就要用 copy.deepcopy()。

【這個 bug 的可怕之處在於它不會報錯】。
    你只會拿到一個「長度對、內容全空」的答案，
    然後盯著程式碼看半小時。

    養成反射：【把可變物件存進結果時，先問自己「要不要複製」。】""",),
     ("h", "為什麼葉節點那裡用 <code>else</code>？"),
     ("c", """if 是葉節點 and rest == 0:
    res.append(path[:])
else:
    go(node.left, rest)
    go(node.right, rest)

    其實不用 else 也對 ——
    因為葉節點的 left 和 right 都是 None，
    go(None, ...) 會立刻 return。

    寫 else 只是省下兩次無謂的函式呼叫。

    但要小心【不要寫成這樣】：

        if 是葉節點:
            if rest == 0:
                res.append(path[:])
            return          # ← 忘了 path.pop()！

    提早 return 會跳過撤銷 ->
    path 越積越長，後面全錯。

    【回溯裡的「提早 return」是很常見的陷阱。】
    要嘛不要提早 return，
    要嘛用 try/finally，
    要嘛改用解法二（不可變 path）。"""),
     "<strong>時間 O(n·h)</strong> 最壞 —— "
     "<strong>走訪是 O(n)，但每次複製路徑是 O(h)</strong>，"
     "而最多可能有 <code>O(n)</code> 條答案路徑。"
     "<strong>空間 O(h)</strong>（不算輸出）。",
   ], "O(n·h)", "O(h)", "複製路徑的成本", "path + 遞迴堆疊", optimal=True),

   ap("解法二", "不可變 path（不用撤銷，最不容易錯）", [
     ("c", S["p113_immutable"]),
     ("h", "用「造新的」取代「改舊的」"),
     ("c", """path = path + [node.val]

    這一行【建立一條新的 list】，
    原本那條完全沒被改到。

    所以：
        ✔ 不需要 pop()（沒東西要撤銷）
        ✔ 不需要 path[:]（每條本來就是獨立的）
        ✔ 提早 return 完全安全

    代價：
        ✘ 每一層都複製整條 path -> 每個節點 O(h)
        ✘ 總共 O(n·h) 的複製成本（解法一只在收集時複製）

【注意不能寫成 path += [node.val]】

    += 對 list 是【原地修改】（等同 extend），
    會改到呼叫者的那條 path ✘

    path = path + [...]  造新的 ✔
    path += [...]        改舊的 ✘

    【這兩者在 list 上行為完全不同，
      是 Python 很經典的一個坑。】
    （對 tuple、str 等不可變型別則沒有差別。）

【什麼時候該用這個版本？】
    ✔ 路徑很短、樹很小 -> 差異可以忽略，換來「不會寫錯」
    ✔ 需要在多執行緒 / 非同步環境共用
    ✔ 你剛被回溯的 pop() 坑過

    大部分面試場合，這個版本是完全可以接受的答案，
    而且更難寫錯。"""),
   ], "O(n·h)", "O(n·h)", "每層都複製", "所有中間路徑"),

   ap("解法三", "迭代 + 堆疊", [
     ("c", S["p113_iter"]),
     "<strong>把 <code>(節點, 剩餘量, 路徑)</code> 一起打包進堆疊</strong> —— "
     "<strong>和解法二一樣用不可變的 path，所以不用撤銷。</strong>",
     ("h", "為什麼先 push <code>right</code> 再 push <code>left</code>？"),
     ("c", """堆疊是後進先出，所以【後 push 的先被處理】。

    要讓輸出順序和遞迴版一致（左子樹的路徑排前面），
    就得【先 push right、後 push left】。

    如果順序反了，答案的內容一樣但【排列順序不同】——
    LeetCode 這題不在意順序，但有些題目在意。

【養成習慣：用堆疊模擬 DFS 時，
  push 的順序要和想要的走訪順序【相反】。】

    這在第 144 題（前序走訪的迭代版）也是同一回事。""",),
     "<strong>沒有遞迴深度問題</strong> —— 5000 個節點的鏈狀樹上這是唯一安全的解法。",
   ], "O(n·h)", "O(n·h)", "每個節點一次", "堆疊裡的所有路徑"),
 ],
 "compare": (["解法", "時間", "空間", "要撤銷嗎", "備註"],
   [["一、共用 path + 回溯", "O(n·h)", "O(h)", "✔", "標準答案，空間最省"],
    ["二、不可變 path", "O(n·h)", "O(n·h)", "✘", "最不容易寫錯"],
    ["三、堆疊迭代", "O(n·h)", "O(n·h)", "✘", "避免遞迴深度問題"]]),
 "edges": [
   "<strong><code>root = None</code></strong> → <code>[]</code>。",
   "<strong>沒有任何符合的路徑</strong> → <code>[]</code>（不是 <code>None</code>）。",
   "<strong><code>[1,2]</code>, <code>targetSum = 1</code></strong> → <code>[]</code>。"
   "<strong>根不是葉節點。</strong>",
   "<strong>多條路徑符合</strong> → 全部都要回傳。",
   "<strong><code>res.append(path)</code> 忘了 <code>[:]</code></strong> → "
   "<strong>結果是 <code>[[], [], ...]</code>，不會報錯 —— 本題第一名的 bug。</strong>",
   "<strong>忘了 <code>path.pop()</code></strong> → 路徑會越積越長，後面的答案全錯。",
   "<strong>在葉節點提早 <code>return</code> 而沒有 <code>pop()</code></strong> → 同上。",
   "<strong>寫成 <code>path += [node.val]</code>（解法二裡）</strong> → "
   "<strong>變成原地修改，破壞了「不可變」的前提。</strong>",
   "<strong>負數節點值</strong> → 不能用「超過就剪枝」（同第 112 題）。",
 ],
 "follow": [
   ("h", "追問一：最多可能有幾條答案？時間複雜度真的是 O(n·h) 嗎？"),
   ("c", """最壞情況：一棵完美二元樹，所有值都是 0，targetSum = 0。

    葉節點有 n/2 個 -> 有 n/2 條路徑全部符合
    每條路徑長度 h = log n

    光是【輸出】就要 O(n/2 × log n) = O(n log n)

    所以 O(n·h) 這個上界是【緊的】——
    不可能更快，因為輸出本身就這麼大。

【這叫做「輸出敏感」（output-sensitive）的複雜度】：

    當答案的規模本身就很大時，
    演算法的複雜度下界由輸出決定。

    第 46 題（全排列，n! 個答案）、
    第 78 題（所有子集，2^n 個答案）
    都是這一類 —— 不要試圖「優化」它們的漸進複雜度。""",),
   ("h", "追問二：如果只要「最長的那條」符合路徑呢？"),
   "<strong>不用存所有路徑，只要記住「目前最長的那一條」</strong>。",
   "<strong>空間從 <code>O(n·h)</code> 降到 <code>O(h)</code></strong> —— "
   "<strong>「只要一個最佳解」時，永遠不要先全部收集再挑。</strong>",
   ("h", "追問三：如果節點值都是正數，能怎麼剪枝？"),
   ("c", """if rest < 0:
    path.pop()          # ★ 別忘了撤銷！
    return

    正數保證「和只會越加越大」，
    所以超過目標就不可能再回來。

【剪枝時最容易忘記撤銷】——

    正確的寫法是把剪枝放在 append 之前：

        def go(node, rest):
            if not node or rest < node.val:   # 先判斷再 append
                return
            path.append(node.val)
            ...
            path.pop()

    【「所有的 return 路徑都要維持不變量」
      是回溯程式碼正確性的核心。】""",),
   ("h", "追問四：如果要回傳節點物件而不是值呢？"),
   "<strong>把 <code>path.append(node.val)</code> 改成 <code>path.append(node)</code> 即可</strong>。",
   "<strong>題目特別強調「不是節點物件」</strong>，"
   "是因為<strong>回傳節點會讓呼叫者能改到樹的內容</strong> —— "
   "<strong>在 API 設計上，回傳內部物件的參考通常是壞事</strong>"
   "（呼叫者可以繞過你的介面直接改狀態）。"
   "<strong>這是題目在偷偷教一個工程觀念。</strong>",
 ],
 "related": [
   "<strong>第 112 題 Path Sum</strong> —— 只問「有沒有」",
   "<strong>第 437 題 Path Sum III</strong> —— 任意起訖點",
   "<strong>第 257 題 Binary Tree Paths</strong> —— 所有根到葉路徑（不看和）",
   "<strong>第 39 題 Combination Sum</strong> —— 同一個回溯骨架",
   "<strong>第 46 題 Permutations</strong> —— 回溯的另一個經典",
 ],
 "check": [
   "<code>res.append(path)</code> 和 <code>res.append(path[:])</code> 差在哪裡？前者會得到什麼？",
   "回溯的「不變量」是什麼？為什麼每個 <code>append</code> 都要配一個 <code>pop</code>？",
   "<code>path = path + [x]</code> 和 <code>path += [x]</code> 在 list 上有什麼不同？",
   "最壞情況下答案有多大？為什麼這題的複雜度不可能低於 O(n·h)？",
 ],
})
print("P113 written")

# ==================== 114. Flatten Binary Tree to Linked List ====================
S["p114_morris"] = '''class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        cur = root
        while cur:
            if cur.left:
                # 找左子樹的【最右節點】——它是前序裡「左子樹的最後一個」
                pre = cur.left
                while pre.right:
                    pre = pre.right

                # 把原本的右子樹接到它後面，再把左子樹整個搬到右邊
                pre.right = cur.right
                cur.right = cur.left
                cur.left = None

            cur = cur.right'''

S["p114_rev"] = '''class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.prev = None                    # 已經串好的那一段的頭

        def go(node):
            if not node:
                return
            go(node.right)                  # 反向後序：右 → 左 → 根
            go(node.left)
            node.right = self.prev          # 把自己接到已串好的那段前面
            node.left = None
            self.prev = node

        go(root)'''

S["p114_stack"] = '''class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return

        stack = [root]
        prev = None
        while stack:
            node = stack.pop()              # 前序：根 → 左 → 右
            if prev:
                prev.left = None
                prev.right = node
            if node.right:
                stack.append(node.right)    # 先 push 右，左才會先被 pop
            if node.left:
                stack.append(node.left)
            prev = node

        prev.left = prev.right = None'''

S["p114_list"] = '''class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        # 最直白：先收集前序，再重新串起來
        order = []

        def pre(node):
            if not node:
                return
            order.append(node)
            pre(node.left)
            pre(node.right)

        pre(root)
        for a, b in zip(order, order[1:]):
            a.left = None
            a.right = b
        if order:
            order[-1].left = order[-1].right = None'''


def _preorder(nd):
    return [] if nd is None else [nd.val] + _preorder(nd.left) + _preorder(nd.right)


def _chain(nd):
    """把展開後的樹讀成一條 list，並檢查每個 left 都是 None。"""
    out = []
    while nd:
        assert nd.left is None, "left not cleared"
        out.append(nd.val)
        nd = nd.right
        assert len(out) <= 5000, "cycle!"
    return out


_p114 = [S.load(k) for k in ("p114_morris", "p114_rev", "p114_stack", "p114_list")]

for spec in [
    [1, [2, [3, None, None], [4, None, None]], [5, None, [6, None, None]]],
    None,
    [0, None, None],
    [1, [2, None, None], None],
    [1, None, [2, None, None]],
]:
    want = _preorder(_build(spec))
    for sol in _p114:
        t = _build(spec)
        sol.flatten(t)
        assert _chain(t) == want, ("P114", spec, sol)

for _ in range(4000):
    n = random.randrange(0, 12)
    base = _rand_tree(n)
    want = _preorder(base)
    def clone(nd):
        return None if nd is None else TreeNode(nd.val, clone(nd.left), clone(nd.right))
    for sol in _p114:
        t = clone(base)
        sol.flatten(t)
        assert _chain(t) == want, ("P114 random", want, sol)
print("P114 solutions OK")

_P114_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">「展開成鏈結串列」= 全部掛在 right 上、left 全設 None，順序要等於【前序走訪】。</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="120" cy="70" r="17" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="120" y="75" fill="var(--gold)">1</text>
              <circle cx="70" cy="126" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="70" y="131" fill="var(--accent)">2</text>
              <circle cx="180" cy="126" r="17" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="180" y="131" fill="#ff8a65">5</text>
              <circle cx="34" cy="182" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="34" y="187" fill="var(--accent)">3</text>
              <circle cx="106" cy="182" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="106" y="187" fill="var(--accent)">4</text>
              <circle cx="216" cy="182" r="17" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="216" y="187" fill="#ff8a65">6</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="108" y1="82" x2="82" y2="114"/><line x1="132" y1="82" x2="168" y2="114"/>
              <line x1="58" y1="139" x2="46" y2="170"/><line x1="82" y1="139" x2="94" y2="170"/>
              <line x1="192" y1="139" x2="204" y2="170"/>
            </g>
            <text x="120" y="222" fill="var(--text-muted)" font-size="11" text-anchor="middle">前序 = 1, 2, 3, 4, 5, 6</text>
            <text x="290" y="130" fill="var(--gold)" font-size="24">→</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="360" cy="70" r="16" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="360" y="75" fill="var(--gold)">1</text>
              <circle cx="400" cy="112" r="16" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="400" y="117" fill="var(--gold)">2</text>
              <circle cx="440" cy="154" r="16" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="440" y="159" fill="var(--gold)">3</text>
              <circle cx="480" cy="196" r="16" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="480" y="201" fill="var(--gold)">4</text>
              <circle cx="520" cy="238" r="16" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="520" y="243" fill="var(--gold)">5</text>
              <circle cx="560" cy="280" r="16" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="560" y="285" fill="var(--gold)">6</text>
            </g>
            <g stroke="var(--gold)" stroke-width="1.5">
              <line x1="371" y1="81" x2="389" y2="101"/><line x1="411" y1="123" x2="429" y2="143"/>
              <line x1="451" y1="165" x2="469" y2="185"/><line x1="491" y1="207" x2="509" y2="227"/>
              <line x1="531" y1="249" x2="549" y2="269"/>
            </g>
            <text x="360" y="316" fill="var(--text-muted)" font-size="11" text-anchor="start">全部靠 right 串起來，left 都是 None</text>
            <line x1="20" y1="338" x2="620" y2="338" stroke="var(--border)"/>
            <text x="20" y="364" fill="var(--accent)" font-size="12">Morris 版的關鍵一步：把 cur 的右子樹，接到【左子樹的最右節點】後面。</text>
            <text x="20" y="388" fill="var(--text-muted)" font-size="12">因為在前序裡，「左子樹的最後一個節點」的下一個，剛好就是「原本的右子樹」。</text>
            <text x="20" y="414" fill="var(--text-muted)" font-size="12">接好之後把整個左子樹搬到 right、left 清空，然後 cur 往右走一步，重複。</text>'''

emit({
 "num": 114, "slug": "flatten-binary-tree-to-linked-list",
 "en": [
   "Given the <code>root</code> of a binary tree, flatten the tree into a \"linked list\":",
   ("raw", "<ul><li>The \"linked list\" should use the same <code>TreeNode</code> class where "
           "the <code>right</code> child pointer points to the next node in the list and the "
           "<code>left</code> child pointer is always <code>null</code>.</li>"
           "<li>The \"linked list\" should be in the same order as a "
           "<strong>pre-order traversal</strong> of the binary tree.</li></ul>"),
   "<strong>Follow up:</strong> Can you flatten the tree in-place (with <code>O(1)</code> "
   "extra space)?",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，把它<strong>原地展開成一條「鏈結串列」</strong>：",
   ("ul", [
     "串列仍然用 <code>TreeNode</code>，但<strong><code>right</code> 指向下一個節點</strong>，"
     "<strong><code>left</code> 一律是 <code>None</code></strong>。",
     "串列的順序必須和這棵樹的<strong>前序走訪</strong>一致。",
   ]),
   "<strong>進階：</strong>你能用 <code>O(1)</code> 額外空間<strong>原地</strong>完成嗎？",
 ],
 "pre": [
   ("note", "為什麼不能「一邊前序走訪一邊改指標」？", [
     ("c", """最直覺的想法：

    def go(node):
        if not node: return
        接到串列尾端(node)
        go(node.left)       ← 危險！
        go(node.right)

    問題：【你在走訪的同時，正在破壞要走的路。】

        把 node 接到串列上時，會改掉 node.right。
        但 node.right 正是你等一下要遞迴的地方 ——
        它已經被覆蓋掉了。

    所以要嘛：
        (a) 先把 left / right 存到區域變數再改（可行）
        (b) 【反過來走】（解法二：右 → 左 → 根）
        (c) 先收集好順序，再一次改完（解法四）
        (d) 完全不遞迴，用 Morris 的方式原地重接（解法一）

【「邊走邊改」是所有指標題的共同陷阱】——
    第 206 題（反轉串列）、第 143 題（重排串列）、
    第 61 題（旋轉串列）都要小心同一件事。

    反射動作：【動指標之前，先把要用的存起來。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,2,5,3,4,null,6]

            1
           / \\
          2   5
         / \\    \\
        3   4    6

  輸出：[1,null,2,null,3,null,4,null,5,null,6]

        1
         \\
          2
           \\
            3
             \\
              4
               \\
                5
                 \\
                  6

  說明：前序走訪是 1, 2, 3, 4, 5, 6。

範例 2
  輸入：root = []
  輸出：[]

範例 3
  輸入：root = [0]
  輸出：[0]""",
 "constraints": [
   "樹的節點數在 <code>[0, 2000]</code> 之間",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "idea": [
   ("fig", _P114_FIG, "0 0 640 432"),
   ("c", """【Morris 式原地重接（解法一）的核心觀察】

    前序走訪的順序是：  根 → 左子樹全部 → 右子樹全部

    所以「左子樹的【最後一個】節點」的下一個，
    就是「原本的右子樹的第一個」。

    而在前序裡，左子樹的最後一個節點
    = 左子樹一路往右走到底的那個節點（最右節點）。

    於是每一步只要做三件事：

        pre = cur.left 一路往右走到底
        pre.right = cur.right       把原本的右子樹接在後面
        cur.right = cur.left        左子樹搬到右邊
        cur.left  = None            清掉左指標

        cur = cur.right             往右走一步，重複

【為什麼這樣就對了？】

    每一步都把「cur 的左子樹」整個插進
    「cur」和「cur 原本的右子樹」之間 ——
    這正是前序的順序 ✔

    而且每一步之後，cur 以上的部分已經是正確的串列，
    cur 以下的部分還是原本的樹（只是結構變了）。

    走到底時整棵樹就被拉成一條線。

【另一條路：反向後序（解法二）】

    既然「邊走邊改」會破壞前序的路，
    那就【倒過來走】：右 → 左 → 根

    這正好是「前序的反序」。

    倒著走的話，每次處理到 node 時，
    node 之後的所有節點【都已經串好了】——
    所以只要把 node 接到那一段前面即可 ✔

    這和「反轉鏈結串列時用 prev 往前接」是同一個思路。"""),
 ],
 "approaches": [
   ap("解法一", "Morris 式原地重接（O(1) 空間，滿足進階）", [
     ("c", S["p114_morris"]),
     "<strong>八行，<code>O(1)</code> 額外空間，沒有遞迴也沒有堆疊。</strong>"
     "<strong>這是本題的最佳解。</strong>",
     ("h", "手動走一遍範例 1"),
     ("c", """            1
           / \\
          2   5
         / \\    \\
        3   4    6

cur = 1：
    左子樹是 2，它的最右節點是 4
    4.right = 5      （把 5 接到 4 後面）
    1.right = 2      （左子樹搬到右邊）
    1.left  = None

        1
         \\
          2
         / \\
        3   4
             \\
              5
               \\
                6

    cur = 2

cur = 2：
    左子樹是 3，它的最右節點就是 3 自己
    3.right = 4
    2.right = 3
    2.left  = None

        1 → 2 → 3 → 4 → 5 → 6  ✔

    cur = 3, 4, 5, 6 都沒有左子樹 -> 直接往右走

完成。"""),
     ("h", "時間複雜度真的是 O(n) 嗎？"),
     ("c", """看起來有內層迴圈（找最右節點），會不會是 O(n²)？

    不會。

    關鍵：每一條「右邊緣」（right spine）
    最多被「找最右節點」這個迴圈走過【一次】。

    因為走過之後，那條右邊緣就被接到別的地方去了，
    不會再被同一個 cur 重複掃描。

    所有右邊緣的總長度是 O(n) -> 總時間 O(n) ✔

    【這和第 94、98、99 題的 Morris 走訪是同一個攤還分析。】

    嚴格來說這題的「最右節點搜尋」總成本
    等於「每條邊被走過的次數」，而每條邊最多被走 2 次。"""),
     "<strong>注意：這個解法會邊改邊走，所以絕對不能中途 return</strong> —— "
     "<strong>不過這題本來就沒有提早結束的需求。</strong>",
   ], "O(n)", "O(1)", "攤還每條邊常數次", "只有兩個指標", optimal=True),

   ap("解法二", "反向後序遞迴（最短，八行）", [
     ("c", S["p114_rev"]),
     ("h", "為什麼是「右 → 左 → 根」？"),
     ("c", """前序是      根 → 左 → 右
它的反序是  右 → 左 → 根

    倒著建串列，就像「反轉鏈結串列」時往前接一樣：

        self.prev 永遠是「已經串好的那一段的頭」

        處理 node 時：
            node.right = self.prev      把自己接到那段前面
            node.left  = None
            self.prev  = node           自己變成新的頭

    走訪順序是前序的【反序】，
    所以串出來的結果剛好是【正序】✔

【為什麼這樣就不會「破壞要走的路」？】

    因為改 node.right 的時候，
    go(node.right) 和 go(node.left) 都【已經執行完了】。

    順序是：先遞迴，後修改 ——
    這就是「後序」的本質。

【三行程式碼，三個觀念】：
    反向走訪、prev 指標、後序修改。
    值得反覆看到熟。""",),
     "<strong>空間 <code>O(h)</code></strong>（遞迴堆疊）—— "
     "<strong>嚴格來說不滿足「O(1) 空間」的進階要求</strong>，"
     "但<strong>它是最好記、最不容易寫錯的版本</strong>。",
     "<strong>用 <code>nonlocal prev</code> 取代 <code>self.prev</code> 也可以</strong>，"
     "效果完全相同。",
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊"),

   ap("解法三", "前序 + 堆疊迭代", [
     ("c", S["p114_stack"]),
     "<strong>用堆疊模擬前序走訪，一邊走一邊把上一個節點接過來。</strong>",
     ("h", "為什麼要「先 push right 再 push left」？"),
     "<strong>堆疊是後進先出</strong>，所以<strong>後 push 的會先被 pop</strong>。"
     "要讓 <code>left</code> 先被處理（前序是根→左→右），就得<strong>後 push 它</strong>。",
     ("h", "為什麼可以安全地邊走邊改？"),
     ("c", """因為在改 node 的指標之前，
    它的 left 和 right 【已經被 push 進堆疊了】。

    堆疊裡存的是「節點的參考」，
    就算之後 node.left 被設成 None，
    堆疊裡那個節點物件仍然好好的 ✔

    【這就是「先把要用的存起來」這個反射動作的具體實現。】

    注意 prev.left = None 要在 prev.right = node 之前或之後都行，
    但【不能忘記】—— 題目要求 left 一律是 None。

    最後一行 prev.left = prev.right = None 是在處理最後一個節點
    （它沒有下一個，但 left/right 可能還留著舊值）。

    ...其實迴圈裡每次都做了 prev.left = None，
    只有最後一個節點沒被當成 prev 處理過，所以要補這一行。"""),
     "<strong>空間 O(h)</strong>（堆疊）。<strong>沒有遞迴深度問題。</strong>",
   ], "O(n)", "O(h)", "每個節點進出堆疊一次", "顯式堆疊"),

   ap("解法四", "先收集前序再重接（最直白）", [
     ("c", S["p114_list"]),
     "<strong>完全不用擔心「邊走邊改」—— 因為走訪和修改是兩個獨立的階段。</strong>",
     "<strong>面試時可以先講這個</strong>（三十秒寫完、一定對），"
     "<strong>再說「這用了 O(n) 空間，我可以做到 O(1)」然後寫解法一。</strong>",
     ("c", """for a, b in zip(order, order[1:]):
    a.left = None
    a.right = b

    zip(order, order[1:]) 產生相鄰的配對：
        (order[0], order[1]), (order[1], order[2]), ...

    【這是「處理相鄰元素」的 Python 慣用寫法】，
    比 for i in range(len(order)-1) 好讀很多。

    最後一個節點沒有 b，所以要另外清掉它的 left/right。""",),
     "<strong>O(n) 時間、O(n) 空間。</strong>",
   ], "O(n)", "O(n)", "走一遍 + 接一遍", "存所有節點"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、Morris 原地重接", "O(n)", "O(1)", "8", "唯一滿足進階要求"],
    ["二、反向後序遞迴", "O(n)", "O(h)", "8", "最好記"],
    ["三、堆疊迭代", "O(n)", "O(h)", "14", "沒有遞迴深度問題"],
    ["四、收集後重接", "O(n)", "O(n)", "12", "最直白，先講這個"]]),
 "edges": [
   "<strong><code>root = None</code></strong> → 什麼都不做（不能 crash）。",
   "<strong>單一節點</strong> → <code>left</code> 和 <code>right</code> 都要是 <code>None</code>。",
   "<strong>只有左子樹</strong> <code>[1,2]</code> → 變成 <code>1 → 2</code>。",
   "<strong>只有右子樹</strong> <code>[1,null,2]</code> → 已經是對的，不能改壞。",
   "<strong>忘了把 <code>left</code> 設成 <code>None</code></strong> → "
   "<strong>判題器會判錯（題目明確要求 <code>left</code> 一律是 <code>null</code>）。</strong>",
   "<strong>沒有先存起 <code>cur.right</code> 就覆蓋它</strong> → 右子樹整個遺失。",
   "<strong>接出一個環</strong>（例如 <code>pre.right = cur</code> 寫錯）→ "
   "<strong>後續任何走訪都會無窮迴圈。</strong>",
   "<strong>解法三忘了處理最後一個節點的 <code>left</code></strong> → 最後一個節點的 <code>left</code> 沒清掉。",
   "<strong>2000 個節點的鏈狀樹</strong> → 解法二、三的遞迴／堆疊深度 2000。",
 ],
 "follow": [
   ("h", "追問一：如果要展開成「中序」或「後序」的順序呢？"),
   "<strong>中序</strong>：這其實比較簡單 —— <strong>就是第 897 題（遞增順序搜尋樹）</strong>，"
   "用中序走訪 + <code>prev</code> 指標即可。",
   "<strong>後序</strong>：用「反向前序」（根 → 右 → 左）倒著串，"
   "<strong>和解法二的技巧對稱</strong>。",
   ("c", """規律：要串出走訪順序 X，就用 X 的【反序】走訪 + 往前接。

    要前序 (根左右)  -> 走 右左根，往前接   （解法二）
    要中序 (左根右)  -> 走 右根左，往前接
    要後序 (左右根)  -> 走 根右左，往前接

【「反著走 + 往前接」可以串出任何走訪順序，
  而且都是 O(n) 時間、O(h) 空間。】""",),
   ("h", "追問二：能不能展開之後再「還原」成原來的樹？"),
   "<strong>不行 —— 資訊已經遺失了。</strong>"
   "<strong>只有一條前序序列，無法唯一決定一棵樹</strong>（第 105 題講過）。",
   "<strong>如果要可逆，就必須在展開時額外記錄結構</strong>"
   "（例如每棵子樹的大小，或帶空節點記號的序列化）。"
   "<strong>這正是第 297 題（序列化與反序列化）在做的事。</strong>",
   ("h", "追問三：Morris 版的攤還分析要怎麼講？"),
   ("c", """「找左子樹的最右節點」這個內層迴圈，
每次都在走一條【右邊緣】。

    關鍵：走過之後，那條右邊緣就被接到 cur.right 上，
    變成主鏈的一部分 —— 【不會再被當成「某個左子樹的右邊緣」掃描】。

    所以每條邊最多被內層迴圈走過一次。
    總邊數是 n - 1 -> 內層迴圈的總成本是 O(n) ✔

    加上外層迴圈的 O(n) -> 總共 O(n)

【這種「單次昂貴、總量有界」的分析，
  在 Morris 走訪、單調堆疊（第 84 題）、
  並查集的路徑壓縮裡反覆出現。】

    學會它，你就能正確評估一大類看起來像 O(n²) 的演算法。"""),
   ("h", "追問四：為什麼題目要求「原地」？"),
   "<strong>因為「先收集再重接」（解法四）太簡單了</strong> —— "
   "<strong>加上 O(1) 空間的限制，才逼出 Morris 那個真正有內容的想法。</strong>",
   "<strong>在真實工程裡，原地操作的價值在於</strong>："
   "<strong>（1）節點數極多時記憶體吃不消；（2）避免配置／回收的成本；</strong>"
   "<strong>（3）保持指標穩定（外部可能還持有這些節點的參考）。</strong>",
 ],
 "related": [
   "<strong>第 94/144 題 中序／前序走訪</strong> —— Morris 技巧的來源",
   "<strong>第 99 題 Recover BST</strong> —— 另一個 Morris 的應用",
   "<strong>第 897 題 Increasing Order Search Tree</strong> —— 中序版的展開",
   "<strong>第 206 題 Reverse Linked List</strong> —— 「prev 往前接」的原型",
   "<strong>第 297 題 Serialize and Deserialize</strong> —— 為什麼展開後不可逆",
 ],
 "check": [
   "為什麼「一邊前序走訪一邊改 <code>right</code>」會出錯？有哪幾種修法？",
   "Morris 版為什麼要找「左子樹的最右節點」？它在前序裡是什麼位置？",
   "反向後序版的走訪順序是什麼？為什麼那樣串出來剛好是正序？",
   "Morris 版的時間為什麼是 O(n) 而不是 O(n²)？",
 ],
})
print("P114 written")

# ==================== 115. Distinct Subsequences ====================
S["p115_2d"] = '''class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        # dp[i][j] = s 的前 i 個字裡，有幾種方式湊出 t 的前 j 個字
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1            # 湊出空字串永遠有 1 種（什麼都不選）

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 不用 s[i-1]：答案就是前 i-1 個字的結果
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    # 也可以用 s[i-1] 去對上 t[j-1]
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[m][n]'''

S["p115_1d"] = '''class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for ch in s:
            # 【一定要倒著走】：dp[j] 依賴 dp[j-1] 的「上一列」的值
            for j in range(n, 0, -1):
                if ch == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]'''

S["p115_memo"] = '''from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(maxsize=None)
        def go(i: int, j: int) -> int:
            """用 s[i:] 湊出 t[j:] 有幾種方式"""
            if j == len(t):
                return 1                    # t 已經湊完了
            if i == len(s):
                return 0                    # s 用完了但 t 還沒湊完

            res = go(i + 1, j)              # 不用 s[i]
            if s[i] == t[j]:
                res += go(i + 1, j + 1)     # 用 s[i] 對上 t[j]
            return res

        ans = go(0, 0)
        go.cache_clear()
        return ans'''


def _p115_ref(s, t):
    """獨立參考解：直接枚舉 s 的所有「選哪些位置」的子集。"""
    m = len(s)
    if len(t) > m:
        return 0
    cnt = 0
    for idx in itertools.combinations(range(m), len(t)):
        if "".join(s[i] for i in idx) == t:
            cnt += 1
    return cnt


_p115 = [S.load(k) for k in ("p115_2d", "p115_1d", "p115_memo")]

for s, t, want in [
    ("rabbbit", "rabbit", 3),
    ("babgbag", "bag", 5),
    ("", "", 1),
    ("a", "", 1),
    ("", "a", 0),
    ("abc", "abcd", 0),
    ("aaa", "aa", 3),
]:
    assert _p115_ref(s, t) == want, ("P115 ref", s, t, _p115_ref(s, t))
    for sol in _p115:
        assert sol.numDistinct(s, t) == want, ("P115", s, t, sol)

for _ in range(2500):
    m = random.randrange(0, 11)
    n = random.randrange(0, 5)
    s = "".join(random.choice("abc") for _ in range(m))
    t = "".join(random.choice("abc") for _ in range(n))
    want = _p115_ref(s, t)
    for sol in _p115:
        assert sol.numDistinct(s, t) == want, ("P115 random", s, t, want, sol)
print("P115 solutions OK")

_P115_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">dp[i][j] = 用 s 的前 i 個字，能湊出 t 的前 j 個字的【方法數】。s = &quot;babgbag&quot;, t = &quot;bag&quot;</text>
            <g font-size="12" text-anchor="middle">
              <text x="60" y="56" fill="var(--text-muted)">s \\ t</text>
              <text x="120" y="56" fill="var(--gold)">&quot;&quot;</text>
              <text x="180" y="56" fill="var(--gold)">b</text>
              <text x="240" y="56" fill="var(--gold)">ba</text>
              <text x="300" y="56" fill="var(--gold)">bag</text>
            </g>
            <g font-size="12" text-anchor="middle">
              <text x="60" y="82" fill="var(--gold)">&quot;&quot;</text><text x="120" y="82" fill="var(--accent)">1</text><text x="180" y="82" fill="var(--text-muted)">0</text><text x="240" y="82" fill="var(--text-muted)">0</text><text x="300" y="82" fill="var(--text-muted)">0</text>
              <text x="60" y="108" fill="var(--gold)">b</text><text x="120" y="108" fill="var(--accent)">1</text><text x="180" y="108" fill="var(--accent)">1</text><text x="240" y="108" fill="var(--text-muted)">0</text><text x="300" y="108" fill="var(--text-muted)">0</text>
              <text x="60" y="134" fill="var(--gold)">ba</text><text x="120" y="134" fill="var(--accent)">1</text><text x="180" y="134" fill="var(--accent)">1</text><text x="240" y="134" fill="var(--accent)">1</text><text x="300" y="134" fill="var(--text-muted)">0</text>
              <text x="60" y="160" fill="var(--gold)">bab</text><text x="120" y="160" fill="var(--accent)">1</text><text x="180" y="160" fill="var(--accent)">2</text><text x="240" y="160" fill="var(--accent)">1</text><text x="300" y="160" fill="var(--text-muted)">0</text>
              <text x="60" y="186" fill="var(--gold)">babg</text><text x="120" y="186" fill="var(--accent)">1</text><text x="180" y="186" fill="var(--accent)">2</text><text x="240" y="186" fill="var(--accent)">1</text><text x="300" y="186" fill="var(--accent)">1</text>
              <text x="60" y="212" fill="var(--gold)">babgb</text><text x="120" y="212" fill="var(--accent)">1</text><text x="180" y="212" fill="var(--accent)">3</text><text x="240" y="212" fill="var(--accent)">1</text><text x="300" y="212" fill="var(--accent)">1</text>
              <text x="60" y="238" fill="var(--gold)">babgba</text><text x="120" y="238" fill="var(--accent)">1</text><text x="180" y="238" fill="var(--accent)">3</text><text x="240" y="238" fill="var(--accent)">4</text><text x="300" y="238" fill="var(--accent)">1</text>
              <text x="60" y="264" fill="var(--gold)">babgbag</text><text x="120" y="264" fill="var(--accent)">1</text><text x="180" y="264" fill="var(--accent)">3</text><text x="240" y="264" fill="var(--accent)">4</text><text x="300" y="264" fill="var(--gold)">5</text>
            </g>
            <rect x="276" y="248" width="48" height="22" fill="none" stroke="var(--gold)" stroke-width="2"/>
            <text x="350" y="264" fill="var(--gold)" font-size="12" text-anchor="start">← 答案 = 5</text>
            <line x1="20" y1="288" x2="620" y2="288" stroke="var(--border)"/>
            <text x="20" y="314" fill="var(--accent)" font-size="12">每一格的兩個來源：</text>
            <text x="40" y="340" fill="var(--text-muted)" font-size="12">不用 s[i-1]　　→　dp[i-1][j]　　　（正上方，永遠要加）</text>
            <text x="40" y="364" fill="var(--text-muted)" font-size="12">用 s[i-1] 對上 t[j-1]　→　dp[i-1][j-1]　（左上方，只有字元相同時才加）</text>
            <text x="20" y="394" fill="#ff8a65" font-size="12">注意第一欄全是 1（湊出空字串只有「什麼都不選」一種），第一列除了 [0][0] 全是 0。</text>
            <text x="20" y="418" fill="var(--gold)" font-size="12">滾動成一維時【必須倒著走 j】，否則 dp[j-1] 會先被這一列改掉，變成「同一個字用兩次」。</text>'''

emit({
 "num": 115, "slug": "distinct-subsequences",
 "en": [
   "Given two strings <code>s</code> and <code>t</code>, return <em>the number of distinct "
   "subsequences of </em><code>s</code><em> which equals </em><code>t</code>.",
   "The test cases are generated so that the answer fits on a 32-bit signed integer.",
 ],
 "zh": [
   "給你兩個字串 <code>s</code> 和 <code>t</code>，"
   "回傳 <code>s</code> 的<strong>子序列</strong>中，"
   "等於 <code>t</code> 的<strong>有幾種</strong>。",
   "測資保證答案能裝進 32 位元有號整數。",
   ("note", "「子序列」的定義", [
     "<strong>刪掉 <code>s</code> 裡任意個字元（可以不刪），剩下的字元<strong>保持原本順序</strong>。</strong>",
     "所以 <code>\"ace\"</code> 是 <code>\"abcde\"</code> 的子序列，"
     "但 <code>\"aec\"</code> 不是（順序變了）。",
     "<strong>「不同的子序列」數的是「刪除方式」而不是「結果字串」</strong> —— "
     "這是本題最容易誤解的地方，下面會講。",
   ]),
 ],
 "pre": [
   ("note", "★ 「不同」到底在數什麼？", [
     ("c", """s = "rabbbit", t = "rabbit"  -> 答案是 3

    s 裡有三個 b：  r a b b b i t
                        1 2 3

    要湊出 "rabbit"（兩個 b），就要從三個 b 裡【選兩個】：
        選 b1, b2  ✔
        選 b1, b3  ✔
        選 b2, b3  ✔

    三種選法，結果字串都是 "rabbit" —— 但算【三種】。

【所以「不同的子序列」數的是「不同的【位置組合】」，
  不是「不同的結果字串」。】

    如果數的是「不同的結果字串」，
    那答案永遠只有 0 或 1（因為 t 是固定的），題目就沒意義了。

    英文原題 "number of distinct subsequences of s which equals t"
    這個 distinct 指的是「s 的不同子序列（按位置區分）」。

    【讀題時卡在這裡是正常的 ——
      先看範例，再回頭理解定義。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "rabbbit", t = "rabbit"
  輸出：3
  說明：（^ 標出選中的位置）
        r a b b b i t
        ^ ^ ^ ^     ^ ^     -> 選 b1, b2
        ^ ^ ^   ^   ^ ^     -> 選 b1, b3
        ^ ^   ^ ^   ^ ^     -> 選 b2, b3

範例 2
  輸入：s = "babgbag", t = "bag"
  輸出：5
  說明：b a b g b a g
        ^ ^     ^           (b1, a1, g1)... 共五種位置組合""",
 "constraints": [
   "1 ≤ <code>s.length</code>, <code>t.length</code> ≤ 1000",
   "<code>s</code> 和 <code>t</code> 只包含英文字母",
 ],
 "idea": [
   ("fig", _P115_FIG, "0 0 640 436"),
   ("c", """狀態：
    dp[i][j] = 用 s 的前 i 個字，湊出 t 的前 j 個字，有幾種方式

轉移（對每個 s[i-1] 只有兩個選擇）：

    【選擇一：不用 s[i-1]】
        那就只能靠前 i-1 個字湊出 t 的前 j 個
        -> dp[i-1][j]

        這一項【永遠存在】（不管字元相不相同）。

    【選擇二：用 s[i-1] 去對上 t[j-1]】
        前提：s[i-1] == t[j-1]
        剩下的 t 前 j-1 個，要靠 s 的前 i-1 個湊
        -> dp[i-1][j-1]

    dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] if s[i-1]==t[j-1] else 0)

邊界：
    dp[i][0] = 1      湊出空字串：什麼都不選，恰好一種 ✔
    dp[0][j] = 0 (j>0)  空的 s 湊不出非空的 t ✔

    【dp[0][0] = 1 這一格是整個 DP 的種子，
      設成 0 的話全表都是 0。】

答案：dp[m][n]

【和第 72 題（編輯距離）、第 1143 題（最長公共子序列）
  是同一個「雙字串二維 DP」家族】——

    差別只在轉移式：
        LCS：     取 max
        編輯距離： 取 min + 1
        本題：     取 sum（計數）

    【求極值用 max/min，求方案數用 +。
      這是布林／極值／計數三種 DP 的萬用轉換。】"""),
 ],
 "approaches": [
   ap("解法一", "二維 DP（標準答案）", [
     ("c", S["p115_2d"]),
     ("h", "為什麼 <code>dp[i][0] = 1</code>？"),
     ("c", """「用 s 的前 i 個字湊出空字串，有幾種方式？」

    答案是 1 —— 【什麼都不選】。

    不是 0！

    這和「空集合的子集有 1 個（就是空集合自己）」、
    「0! = 1」、「空乘積 = 1」是同一類約定 ——
    它們都是為了讓遞迴式在邊界處自洽。

    驗證：如果設成 0，
        dp[1][1] = dp[0][1] + dp[0][0] = 0 + 0 = 0
        整張表全是 0 ✘

    【base case 設錯，是 DP 題最常見的 bug。
      設完之後一定要手動驗算最小的幾格。】"""),
     ("h", "為什麼 <code>dp[i-1][j]</code> 那一項永遠要加？"),
     ("c", """因為「不用 s[i-1]」永遠是一個合法的選擇。

    就算 s[i-1] == t[j-1]，你也可以選擇【不用它】，
    改用前面的某個相同字元。

    這正是範例 1 裡「三個 b 選兩個」會產生 3 種的原因 ——
    每個 b 都有「用」和「不用」兩條路。

【常見錯誤】：寫成 if/else

    if s[i-1] == t[j-1]:
        dp[i][j] = dp[i-1][j-1]      ✘ 漏掉「不用」那條路
    else:
        dp[i][j] = dp[i-1][j]

    這樣 "rabbbit" / "rabbit" 會算出 1 而不是 3。

    【正確的是「永遠加 dp[i-1][j]，字元相同時【再多加】dp[i-1][j-1]」。】""",),
     "<strong>時間 O(mn) = 10⁶，空間 O(mn)</strong>。"
     "<strong>對 1000×1000 來說，二維表是 100 萬個整數 —— Python 下約 40MB，有點吃緊。</strong>"
     "<strong>所以滾動陣列（解法二）在這題是有實際價值的。</strong>",
   ], "O(m × n)", "O(m × n)", "每格 O(1)", "二維表", optimal=True),

   ap("解法二", "滾動陣列（一維，★ 必須倒著走）", [
     ("c", S["p115_1d"]),
     ("h", "★★ 為什麼 <code>j</code> 一定要從大到小？"),
     ("c", """轉移式：dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    兩個來源【都在上一列】。

    壓成一維之後，dp[j] 一開始還是上一列的值。

    【正著走（j 從小到大）】：

        更新 dp[1] 時用到 dp[0]     -> dp[0] 是上一列的 ✔（dp[0] 不會變）
        更新 dp[2] 時用到 dp[1]     -> dp[1] 【已經被這一列改掉了】✘

        就會變成「同一個 s[i] 被用了兩次」——
        答案會偏大。

    【倒著走（j 從大到小）】：

        更新 dp[n] 時用到 dp[n-1]   -> 還沒改，是上一列的 ✔
        更新 dp[n-1] 時用到 dp[n-2] -> 還沒改 ✔
        ...

        所有用到的都還是上一列的值 ✔

【這是 01 背包的經典技巧，一字不差】：

    01 背包（每個物品只能用一次）-> 倒著走
    完全背包（每個物品可以用多次）-> 正著走

    本題「每個 s[i] 只能用一次」-> 01 背包 -> 倒著走 ✔

    【記住這個對照，你就解決了一整類 DP 題的方向問題。】"""),
     ("h", "為什麼沒有 <code>dp[j] = dp[j]</code> 這一行？"),
     ("c", """二維版是：
    dp[i][j] = dp[i-1][j]              # 先繼承
    if 相同: dp[i][j] += dp[i-1][j-1]  # 再加

一維版裡「繼承」這件事是【自動發生的】——
dp[j] 如果不被修改，它本來就還是上一列的值 ✔

    所以只剩下：
        if ch == t[j-1]:
            dp[j] += dp[j-1]

    【滾動陣列常常會讓程式碼「看起來少了一半」，
      那是因為「不變」的部分變成了「不做事」。】""",),
     "<strong>空間從 O(mn) 降到 O(n) = 1000 個整數。</strong>"
     "<strong>時間不變。</strong>",
   ], "O(m × n)", "O(n)", "格數不變", "只留一列"),

   ap("解法三", "記憶化遞迴（最好想）", [
     ("c", S["p115_memo"]),
     ("h", "兩個 base case 的順序很重要"),
     ("c", """if j == len(t): return 1      # t 湊完了 -> 成功一種
if i == len(s): return 0      # s 用完了但 t 沒湊完 -> 失敗

    【順序不能反！】

    如果先檢查 i == len(s)：
        當 s 和 t 同時用完時（i == m 且 j == n），
        會回傳 0 ✘ —— 但那其實是「成功湊完」的情況。

    先檢查 j == len(t)：
        同時用完時回傳 1 ✔

    驗證：s = "a", t = "a"
        go(0,0): s[0]==t[0] -> go(1,0) + go(1,1)
            go(1,0): j=0 != 1, i=1 == 1 -> 0
            go(1,1): j=1 == 1 -> 1 ✔
        答案 1 ✔

【「兩個終止條件同時滿足時該回哪一個」
  是遞迴題最容易踩的邊界。】

    第 97 題（交錯字串）的 base case 也有同樣的考量。"""),
     "<strong>複雜度和迭代版相同</strong>（<code>O(mn)</code> 個狀態，每個算一次）。",
     "<strong>但遞迴深度是 <code>m + n = 2000</code></strong> —— "
     "<strong>Python 預設上限 1000，這題會 <code>RecursionError</code>！</strong>",
     ("c", """實際上 go(i, j) 的遞迴鏈是 i 一路加到 m，
所以深度是 O(m) = 1000 —— 【剛好卡在上限】。

    LeetCode 的 Python 環境通常把上限調高了，
    所以這題實測會過。

    但【不能依賴這件事】——
    面試時要主動說：「這裡深度 1000，
    正式環境我會改用迭代版（解法二）。」

    這比寫出哪個版本更能展示工程判斷。""",),
   ], "O(m × n)", "O(m × n)", "每個狀態算一次", "快取 + 遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "遞迴深度", "備註"],
   [["一、二維 DP", "O(mn)", "O(mn)", "—", "標準答案，最好講"],
    ["二、滾動一維", "O(mn)", "O(n)", "—", "空間最省，注意倒著走"],
    ["三、記憶化遞迴", "O(mn)", "O(mn)", "O(m)", "最好想，但深度有風險"]]),
 "edges": [
   "<strong><code>s = \"\", t = \"\"</code></strong>（題目保證不會）→ <code>1</code>。",
   "<strong><code>t</code> 比 <code>s</code> 長</strong> → <code>0</code>。三種解法都自然正確。",
   "<strong><code>s = \"aaa\", t = \"aa\"</code></strong> → <code>3</code>（C(3,2)）。"
   "<strong>「全部字元相同」是檢驗「有沒有漏掉不用那條路」的最快測資。</strong>",
   "<strong><code>s = \"rabbbit\", t = \"rabbit\"</code></strong> → <code>3</code>。",
   "<strong><code>dp[i][0]</code> 設成 0</strong> → <strong>整張表全是 0。</strong>",
   "<strong>轉移寫成 <code>if/else</code> 而不是「永遠加 + 條件再加」</strong> → "
   "<strong>答案偏小，本題第一名的 bug。</strong>",
   "<strong>一維版正著走 <code>j</code></strong> → <strong>答案偏大（同一個字被用兩次）。</strong>",
   "<strong>記憶化版兩個 base case 順序寫反</strong> → <code>s</code> 和 <code>t</code> 同時用完時答錯。",
   "<strong>1000 × 1000</strong> → 二維表約 40MB（Python），可能觸發記憶體限制。",
 ],
 "follow": [
   ("h", "追問一：為什麼答案保證能裝進 32 位元整數？"),
   ("c", """最壞情況：s 和 t 都是同一個字元重複。

    s = "a" × 1000, t = "a" × k

    答案 = C(1000, k)

    C(1000, 500) 是一個 300 位數的天文數字 ——
    遠遠超過 2^31。

【所以「測資保證答案裝得下」是一個很強的限制】：
    它排除了上面那種極端輸入。

    在 C++ / Java 裡要小心中間值也不能溢位；
    Python 的整數無限大，所以「不小心就過了」——
    但這正是要警覺的地方：
    【題目在考「你知不知道會溢位」，而不是「你會不會算」。】

    面試時主動說「在 C++ 我會用 long long，
    或者題目保證了答案範圍」會加分。""",),
   ("h", "追問二：如果改問「s 有幾個不同的子序列」（不指定 t）呢？"),
   "<strong>那是第 940 題（Distinct Subsequences II），而且那題數的是"
   "「不同的【字串】」而不是「不同的位置組合」</strong> —— 定義正好相反。",
   ("c", """dp[i] = s 的前 i 個字，有幾個【不同的】子序列字串

    dp[i] = 2 × dp[i-1]                     每個舊的都有「加 / 不加 s[i]」兩種
          - dp[last[s[i]] - 1]              扣掉重複算的

    last[c] 是字元 c 上一次出現的位置。

【扣掉的那一項就是「去重」】——
    因為 s[i] 和它上一次出現時，
    會產生一模一樣的字串集合。

    這題（115）不用去重（按位置算），
    第 940 題要去重（按字串算）——
    兩題放在一起看，「distinct」這個字的歧義就很清楚了。""",),
   ("h", "追問三：如果要輸出「是哪些位置組合」呢？"),
   "<strong>從 <code>dp[m][n]</code> 往回走，每一格看是從「上面」還是「左上」來的</strong>。",
   "<strong>但答案的數量可能是指數級的</strong>（<code>C(1000,500)</code>），"
   "<strong>所以「輸出全部」在最壞情況下不可行</strong>。"
   "<strong>實務上只會要求「輸出其中一組」或「輸出前 k 組」。</strong>",
   ("h", "追問四：空間能不能低於 O(n)？"),
   "<strong>不行。</strong><code>dp</code> 這一列的每一格都可能被後面用到，"
   "<strong>而且它們互不相同 —— 資訊量本身就是 Θ(n)。</strong>",
   "<strong>不過如果只要「答案是不是 0」（也就是「t 是不是 s 的子序列」），"
   "那就只要 O(1)</strong> —— 貪心的雙指標掃一遍即可（第 392 題）。"
   "<strong>「要計數」比「要判斷存在」貴得多，這個對比很有代表性。</strong>",
 ],
 "related": [
   "<strong>第 72 題 Edit Distance</strong> —— 同一個雙字串二維 DP 家族",
   "<strong>第 1143 題 Longest Common Subsequence</strong> —— 取 max 的版本",
   "<strong>第 97 題 Interleaving String</strong> —— 布林版的雙字串 DP",
   "<strong>第 392 題 Is Subsequence</strong> —— 只問存在性，貪心 O(n)",
   "<strong>第 940 題 Distinct Subsequences II</strong> —— 數「不同字串」而非「位置組合」",
 ],
 "check": [
   "「不同的子序列」數的是不同的字串還是不同的位置組合？請用 <code>\"rabbbit\"</code> 說明。",
   "為什麼 <code>dp[i-1][j]</code> 那一項永遠要加，而不是寫成 <code>if/else</code>？",
   "一維版為什麼一定要倒著走 <code>j</code>？正著走會多算什麼？",
   "<code>dp[i][0] = 1</code> 的意義是什麼？設成 0 會怎樣？",
 ],
})
print("P115 written")

# ==================== 116 / 117. Populating Next Right Pointers ====================
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


_NODE = {"Node": Node}


def _perfect(depth, counter=None):
    """蓋一棵完美二元樹，值依前序編號。"""
    if counter is None:
        counter = [1]
    if depth == 0:
        return None
    v = counter[0]; counter[0] += 1
    return Node(v, _perfect(depth - 1, counter), _perfect(depth - 1, counter))


def _rand_node_tree(n, counter=None):
    if counter is None:
        counter = [1]
    if n == 0:
        return None
    v = counter[0]; counter[0] += 1
    left = random.randrange(0, n)
    return Node(v, _rand_node_tree(left, counter), _rand_node_tree(n - 1 - left, counter))


def _levels(root):
    """用 left/right 算出每一層的節點（不看 next）。"""
    out, cur = [], [root] if root else []
    while cur:
        out.append(cur)
        cur = [k for nd in cur for k in (nd.left, nd.right) if k]
    return out


def _check_next(root):
    """驗證 next 指標：每層串成一條、最後一個指向 None。回傳每層的值。"""
    got = []
    for lv in _levels(root):
        # 從這一層最左邊的節點沿著 next 走
        chain, nd, seen = [], lv[0], set()
        while nd:
            assert id(nd) not in seen, "cycle in next chain"
            seen.add(id(nd))
            chain.append(nd)
            nd = nd.next
        assert chain[-1].next is None
        assert [x.val for x in chain] == [x.val for x in lv], (
            "next chain mismatch", [x.val for x in chain], [x.val for x in lv])
        got.append([x.val for x in lv])
    return got


S["p116_bfs"] = '''from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        dq = deque([root])
        while dq:
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                if i < n - 1:                  # 不是這一層的最後一個
                    node.next = dq[0]          # 就指向佇列裡的下一個
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return root'''

S["p116_o1"] = '''class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        leftmost = root
        while leftmost and leftmost.left:      # 只要還有下一層
            node = leftmost
            while node:                        # 沿著這一層的 next 走
                node.left.next = node.right    # 1) 同一個父節點的兩個孩子
                if node.next:
                    node.right.next = node.next.left   # 2) 跨父節點
                node = node.next
            leftmost = leftmost.left           # 往下一層

        return root'''

S["p116_rec"] = '''class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def go(a, b):
            """把 a 和 b 這兩棵子樹「縫」起來（a 在左、b 在右）"""
            if not a or not b:
                return
            a.next = b
            go(a.left, a.right)     # a 內部
            go(a.right, b.left)     # 跨過 a 和 b 的接縫
            go(b.left, b.right)     # b 內部

        if root:
            go(root.left, root.right)
        return root'''

_p116 = [S.load(k, extra=_NODE) for k in ("p116_bfs", "p116_o1", "p116_rec")]

for d in range(0, 9):
    want = [[x.val for x in lv] for lv in _levels(_perfect(d))]
    for sol in _p116:
        t = _perfect(d)
        out = sol.connect(t)
        assert (out is None) == (t is None)
        if t:
            assert _check_next(t) == want, ("P116", d, sol)
print("P116 solutions OK")

S["p117_bfs"] = '''from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        dq = deque([root])
        while dq:
            n = len(dq)
            for i in range(n):
                node = dq.popleft()
                if i < n - 1:
                    node.next = dq[0]
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

        return root'''

S["p117_o1"] = '''class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        cur = root                             # 目前這一層（next 已經接好了）
        while cur:
            dummy = Node(0)                    # 下一層的虛擬頭
            tail = dummy                       # 下一層目前串到哪裡

            while cur:                         # 沿著這一層的 next 走一遍
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next

            cur = dummy.next                   # 下一層的第一個節點

        return root'''

_p117 = [S.load(k, extra=_NODE) for k in ("p117_bfs", "p117_o1")]

for _ in range(3000):
    n = random.randrange(0, 14)
    base = _rand_node_tree(n)
    want = [[x.val for x in lv] for lv in _levels(base)]
    def clone_node(nd):
        return None if nd is None else Node(nd.val, clone_node(nd.left), clone_node(nd.right))
    for sol in _p117 + [_p116[0]]:
        t = clone_node(base)
        sol.connect(t)
        if t:
            assert _check_next(t) == want, ("P117 random", want, sol)
print("P117 solutions OK")

_P116_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">O(1) 空間的關鍵：站在【上一層】（next 已經接好），用它當佇列去接【下一層】。</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="320" cy="62" r="17" fill="none" stroke="var(--text-muted)" stroke-width="2"/><text x="320" y="67" fill="var(--text-muted)">1</text>
              <circle cx="200" cy="130" r="17" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="200" y="135" fill="var(--gold)">2</text>
              <circle cx="440" cy="130" r="17" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="440" y="135" fill="var(--gold)">3</text>
              <circle cx="140" cy="198" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="140" y="203" fill="var(--accent)">4</text>
              <circle cx="260" cy="198" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="260" y="203" fill="var(--accent)">5</text>
              <circle cx="380" cy="198" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="380" y="203" fill="var(--accent)">6</text>
              <circle cx="500" cy="198" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="500" y="203" fill="var(--accent)">7</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="307" y1="75" x2="213" y2="117"/><line x1="333" y1="75" x2="427" y2="117"/>
              <line x1="188" y1="143" x2="152" y2="185"/><line x1="212" y1="143" x2="248" y2="185"/>
              <line x1="428" y1="143" x2="392" y2="185"/><line x1="452" y1="143" x2="488" y2="185"/>
            </g>
            <line x1="217" y1="130" x2="423" y2="130" stroke="var(--gold)" stroke-width="2" stroke-dasharray="5 3"/>
            <polygon points="423,130 415,126 415,134" fill="var(--gold)"/>
            <text x="320" y="122" fill="var(--gold)" font-size="11" text-anchor="middle">next（上一層已接好）</text>
            <line x1="157" y1="198" x2="243" y2="198" stroke="var(--accent)" stroke-width="2"/>
            <polygon points="243,198 235,194 235,202" fill="var(--accent)"/>
            <line x1="277" y1="198" x2="363" y2="198" stroke="#ff8a65" stroke-width="2.5"/>
            <polygon points="363,198 355,194 355,202" fill="#ff8a65"/>
            <line x1="397" y1="198" x2="483" y2="198" stroke="var(--accent)" stroke-width="2"/>
            <polygon points="483,198 475,194 475,202" fill="var(--accent)"/>
            <text x="200" y="230" fill="var(--accent)" font-size="11" text-anchor="middle">① node.left.next = node.right</text>
            <text x="320" y="252" fill="#ff8a65" font-size="11" text-anchor="middle">② node.right.next = node.next.left　（跨過父節點的接縫）</text>
            <line x1="20" y1="276" x2="620" y2="276" stroke="var(--border)"/>
            <text x="20" y="302" fill="var(--gold)" font-size="12">第 116 題（完美二元樹）：孩子一定成對出現，所以兩行就接完了。</text>
            <text x="20" y="328" fill="var(--text-muted)" font-size="12">leftmost = leftmost.left 就能往下一層——因為最左邊的節點一定有左孩子。</text>
            <text x="20" y="358" fill="#ff8a65" font-size="12">第 117 題（任意二元樹）：孩子可能缺一邊、甚至整層都不在同一個父節點下，</text>
            <text x="20" y="382" fill="#ff8a65" font-size="12">上面那兩行就不夠了。改用【虛擬頭 + tail 指標】把下一層的節點一個一個串上去，</text>
            <text x="20" y="406" fill="var(--accent)" font-size="12">走完這一層後，dummy.next 就是下一層的第一個節點——完全不需要知道它在哪裡。</text>'''

emit({
 "num": 116, "slug": "populating-next-right-pointers-in-each-node",
 "en": [
   "You are given a <strong>perfect binary tree</strong> where all leaves are on the same "
   "level, and every parent has two children. The binary tree has the following definition:",
   ("c", """struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}"""),
   "Populate each <code>next</code> pointer to point to its next right node. If there is no "
   "next right node, the <code>next</code> pointer should be set to <code>NULL</code>.",
   "Initially, all <code>next</code> pointers are set to <code>NULL</code>.",
   "<strong>Follow up:</strong> You may only use constant extra space. The recursive approach "
   "is fine — implicit stack space does not count as extra space for this problem.",
 ],
 "zh": [
   "給你一棵<strong>完美二元樹</strong>（所有葉節點都在同一層，"
   "而且每個父節點都剛好有兩個孩子），節點的定義多了一個 <code>next</code> 指標。",
   "請把每個節點的 <code>next</code> 指向<strong>同一層裡它右邊的那個節點</strong>；"
   "如果右邊沒有節點，<code>next</code> 就設成 <code>None</code>。",
   "一開始所有 <code>next</code> 都是 <code>None</code>。",
   "<strong>進階：</strong>只能用<strong>常數額外空間</strong>"
   "（遞迴的隱式堆疊不算）。",
 ],
 "pre": [
   ("note", "「完美二元樹」這個前提，就是這題比第 117 題簡單的全部原因", [
     ("c", """完美（perfect）二元樹：
    每一層都是滿的，節點數 = 2^h - 1

    帶來兩個保證：
        (a) 每個非葉節點都【剛好有兩個孩子】
        (b) 最左邊的節點一定有左孩子（除非已經是最後一層）

    有了 (a)，接 next 只要兩行：
        node.left.next  = node.right              同一個父節點
        node.right.next = node.next.left          跨父節點

        因為「node.next 一定存在左孩子」是保證的。

    有了 (b)，往下一層只要：
        leftmost = leftmost.left

【第 117 題把這個前提拿掉，兩行就全都不成立了】——
    孩子可能缺一邊，
    「下一層的第一個節點」也不一定是 leftmost.left。

    那題要改用「虛擬頭 + tail」的通用寫法（見下面）。

    兩題放在一起看，「前提條件如何簡化演算法」
    這件事會非常清楚。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,2,3,4,5,6,7]

            1
           / \\
          2   3
         / \\ / \\
        4  5 6  7

  輸出：[1,#,2,3,#,4,5,6,7,#]

        1 -> None
        2 -> 3 -> None
        4 -> 5 -> 6 -> 7 -> None

  說明：# 代表每一層的結尾。
        注意 5 -> 6 這一條【跨越了不同的父節點】。

範例 2
  輸入：root = []
  輸出：[]""",
 "constraints": [
   "樹的節點數在 <code>[0, 2¹² − 1]</code> 之間",
   "−1000 ≤ <code>Node.val</code> ≤ 1000",
 ],
 "idea": [
   ("fig", _P116_FIG, "0 0 640 424"),
   ("c", """【最直覺的做法】：BFS 層序走訪，每層把相鄰的接起來。
    O(n) 時間、O(w) 空間 —— 但不滿足進階要求。

【O(1) 空間的關鍵想法】：

    當我們要接【第 k+1 層】時，
    【第 k 層的 next 已經接好了】——

    那第 k 層本身就是一個現成的「佇列」！

    沿著第 k 層的 next 走一遍，就能碰到第 k+1 層的所有節點，
    完全不需要額外的資料結構。

    這就是「用已建好的結構當作走訪工具」——
    和 Morris 走訪「借用空指標」是同一種思維。

具體兩步（完美二元樹才成立）：

    for node in 第 k 層（沿著 next 走）:
        node.left.next  = node.right           ① 同父
        node.right.next = node.next.left       ② 跨父（node.next 存在時）

    然後 leftmost = leftmost.left 往下一層。

【驗證 ② 為什麼對】：
    node.right 在這一層的右邊鄰居，
    就是「node 右邊那個節點的左孩子」✔
    （因為每個父節點都有兩個孩子，中間不會有空隙。）"""),
 ],
 "approaches": [
   ap("解法一", "BFS 層序（最直覺，但不滿足進階）", [
     ("c", S["p116_bfs"]),
     "<strong>第 102 題的骨架 + <code>node.next = dq[0]</code>。</strong>",
     ("h", "<code>dq[0]</code> 這個小技巧"),
     ("c", """在 for 迴圈裡，dq 的前面【還沒被取出的】就是同一層的下一個節點。

    if i < n - 1:
        node.next = dq[0]

    i < n - 1 代表「不是這一層的最後一個」。
    是最後一個的話，dq[0] 會是【下一層】的節點 —— 不能接 ✘

【注意 deque 的隨機存取 dq[0] 是 O(1)】
    （兩端的存取都是 O(1)，中間才慢）。

    如果用 dq[i+1] 之類的就會是 O(n) —— 不要那樣寫。""",),
     "<strong>O(n) 時間、O(w) 空間</strong>（最後一層有 n/2 個節點）。"
     "<strong>能過，但題目明確要求 O(1)。</strong>",
   ], "O(n)", "O(w)", "每個節點一次", "佇列最大寬度"),

   ap("解法二", "利用上一層的 next 當佇列（O(1) 空間，標準答案）", [
     ("c", S["p116_o1"]),
     "<strong>九行，<code>O(1)</code> 額外空間。</strong>"
     "<strong>只有 <code>leftmost</code> 和 <code>node</code> 兩個指標。</strong>",
     ("h", "兩層迴圈各在做什麼"),
     ("c", """外層： while leftmost and leftmost.left
    「還有下一層嗎？」

    leftmost.left 存在 -> 代表 leftmost 不是葉節點
                       -> 因為是完美二元樹，整層都不是葉節點
                       -> 下一層存在 ✔

內層： while node
    沿著【這一層已經接好的 next 鏈】走，
    幫下一層接線。

【走完內層之後，第 k+1 層的 next 全部接好了】——
    於是下一輪外層就可以拿它當佇列用。

    這是一個歸納法：
        第 0 層（只有 root）的 next 天生就是 None ✔（base）
        假設第 k 層接好了 -> 可以接好第 k+1 層 ✔（step）"""),
     ("h", "為什麼這樣真的是 O(1) 空間？"),
     "<strong>因為我們沒有建立任何新的資料結構</strong> —— "
     "<strong>「佇列」的角色是由樹自己的 <code>next</code> 指標扮演的。</strong>",
     "<strong>這是本題最漂亮的地方：把「要建的東西」同時當成「建它的工具」。</strong>"
     "<strong>Morris 走訪（第 94、99、114 題）借用的是空的 <code>right</code> 指標，"
     "這裡借用的是「已經接好的 <code>next</code>」—— 同一種思路的兩個變體。</strong>",
   ], "O(n)", "O(1)", "每個節點一次", "只有兩個指標", optimal=True),

   ap("解法三", "遞迴「縫合」兩棵子樹", [
     ("c", S["p116_rec"]),
     ("h", "三個遞迴呼叫，對應三種「接縫」"),
     ("c", """go(a, b) 的意思是「a 和 b 是同一層相鄰的兩個節點」。

    a.next = b                  先把這一對接起來

    go(a.left, a.right)         a 內部的接縫
    go(a.right, b.left)         ★ a 和 b 之間的接縫（最關鍵的一條）
    go(b.left, b.right)         b 內部的接縫

【第二條 go(a.right, b.left) 就是「跨父節點」那一條】——
    沒有它的話，每個父節點底下的兩個孩子會各自成對，
    但「5 -> 6」這種跨越就接不起來了。

    這也是這題最容易漏掉的一行。

【為什麼不用處理更遠的跨越（例如 a.left 和 b.right）？】

    因為它們之間隔著 a.right 和 b.left ——
    只要相鄰的都接好了，整條鏈就自動串起來了 ✔

    「只處理相鄰」是鏈結結構的共同性質。""",),
     "<strong>題目明說「遞迴的隱式堆疊不算額外空間」</strong>，"
     "<strong>所以這個版本也算滿足進階要求。</strong>",
     "<strong>空間實際上是 O(h) = O(log n)</strong>（完美二元樹）。",
   ], "O(n)", "O(log n) 隱式", "每個節點一次", "遞迴堆疊（題目不計）"),
 ],
 "compare": (["解法", "時間", "空間", "滿足進階", "備註"],
   [["一、BFS", "O(n)", "O(w)", "✘", "最直覺"],
    ["二、上一層當佇列", "O(n)", "O(1)", "✔", "標準答案，最漂亮"],
    ["三、遞迴縫合", "O(n)", "O(log n) 隱式", "✔ 題目允許", "好想，但要記得跨父那一行"]]),
 "edges": [
   "<strong><code>root = None</code></strong> → 回傳 <code>None</code>。",
   "<strong>單一節點</strong> → <code>next</code> 保持 <code>None</code>。"
   "<strong>解法二的 <code>leftmost.left</code> 是 <code>None</code>，外層迴圈一次都不跑 ✔</strong>",
   "<strong>兩層</strong> <code>[1,2,3]</code> → <code>2.next = 3</code>，<code>3.next = None</code>。",
   "<strong>每層的最後一個節點</strong> → <code>next</code> 必須是 <code>None</code>，"
   "<strong>不能指到下一層的第一個</strong>。",
   "<strong>解法一忘了 <code>if i &lt; n - 1</code></strong> → "
   "<strong>每層的最後一個會指到下一層 —— 整條鏈串成一條，答案全錯。</strong>",
   "<strong>解法三漏掉 <code>go(a.right, b.left)</code></strong> → 跨父節點的接縫斷掉。",
   "<strong>接出一個環</strong> → 後續走訪無窮迴圈。",
   "<strong>2¹² − 1 = 4095 個節點</strong> → 樹高 12，遞迴完全安全。",
 ],
 "follow": [
   ("h", "追問一：如果不是完美二元樹呢？"),
   "<strong>第 117 題</strong>。解法二的兩行會直接爆炸（<code>node.left</code> 可能是 <code>None</code>），"
   "<strong><code>leftmost = leftmost.left</code> 也不再成立</strong>。",
   "<strong>通用的寫法是「虛擬頭 + tail 指標」</strong> —— 見第 117 題。"
   "<strong>好消息是：那個寫法對第 116 題也完全適用</strong>，"
   "所以<strong>只要記一個版本就夠了</strong>。",
   ("h", "追問二：接好 <code>next</code> 之後能做什麼？"),
   ("c", """next 指標把二元樹「橫向」也串了起來，
於是它同時是一棵樹和一組鏈結串列。

    好處：
        ✔ 層序走訪不再需要佇列 -> O(1) 空間
        ✔ 可以 O(1) 找到「右邊的鄰居」
        ✔ 可以從任一節點橫向掃描整層

    這在【B+ 樹】裡是標準設計 ——
    葉節點之間用類似的指標串起來，
    讓「範圍查詢」（scan）可以沿著葉子一路掃過去，
    不用每次都從根往下找。

    幾乎所有關聯式資料庫的索引都靠這個做 range scan。

【所以這題不是純粹的練習題，
  它是一個真實資料結構的簡化版。】""",),
   ("h", "追問三：解法二的「O(1) 空間」有沒有作弊？"),
   "<strong>沒有。</strong>它<strong>沒有配置任何新的記憶體</strong> —— "
   "用的是題目本來就要求你填的 <code>next</code> 欄位。",
   "<strong>如果題目沒有 <code>next</code> 欄位（只要你「輸出」層序），那就做不到 O(1)</strong> —— "
   "<strong>因為那時你沒有地方可以「借」。</strong>"
   "<strong>「輸出結構本身可以當作中間結構」是這類題目的共同前提。</strong>",
   ("h", "追問四：能不能用 DFS 做到 O(1)？"),
   "<strong>解法三就是 DFS</strong>，但它的空間是 <code>O(h)</code> 的遞迴堆疊 —— "
   "<strong>只是題目特別聲明不計。</strong>",
   "<strong>真正的 O(1) 必須是迭代的</strong>（解法二），"
   "<strong>因為遞迴無論如何都要記住「回到哪裡」。</strong>",
 ],
 "related": [
   "<strong>第 117 題 Populating Next Right Pointers II</strong> —— 拿掉「完美」的前提",
   "<strong>第 102 題 Level Order Traversal</strong> —— 解法一的骨架",
   "<strong>第 114 題 Flatten Binary Tree</strong> —— 另一個「原地重接指標」",
   "<strong>第 199 題 Right Side View</strong> —— 接好 next 後可以 O(1) 空間解",
 ],
 "check": [
   "「完美二元樹」這個前提讓哪兩件事變得成立？",
   "解法二為什麼是 O(1) 空間？它「借用」了什麼？",
   "<code>node.right.next = node.next.left</code> 這一行在接什麼？沒有它會漏掉什麼？",
   "解法一如果忘了 <code>if i &lt; n - 1</code> 會發生什麼？",
 ],
})
print("P116 written")

emit({
 "num": 117, "slug": "populating-next-right-pointers-in-each-node-ii",
 "en": [
   "Given a binary tree, populate each <code>next</code> pointer to point to its next right "
   "node. If there is no next right node, the <code>next</code> pointer should be set to "
   "<code>NULL</code>.",
   "Initially, all <code>next</code> pointers are set to <code>NULL</code>.",
   "<strong>Follow up:</strong> You may only use constant extra space. The recursive approach "
   "is fine — implicit stack space does not count as extra space for this problem.",
 ],
 "zh": [
   "給你一棵<strong>任意的</strong>二元樹（<strong>不保證完美、也不保證完全</strong>），"
   "把每個節點的 <code>next</code> 指向同一層裡它右邊的那個節點；沒有的話設成 <code>None</code>。",
   "一開始所有 <code>next</code> 都是 <code>None</code>。",
   "<strong>進階：</strong>只能用<strong>常數額外空間</strong>（遞迴的隱式堆疊不算）。",
 ],
 "pre": [
   ("note", "★ 第 116 題的兩行為什麼在這裡全部失效", [
     ("c", """第 116 題的核心兩行：

    node.left.next  = node.right
    node.right.next = node.next.left

【失效原因一】：node.left 可能是 None
    -> AttributeError

【失效原因二】：node.next.left 可能是 None
    -> 那 node.right 的右鄰居其實是 node.next.right，
       甚至是「更右邊某個節點」的孩子。

    反例：

            1
           / \\
          2   3
         /     \\
        4       5

        4 的右鄰居是 5 ——
        但它們的父節點（2 和 3）之間隔著「2 沒有右孩子」
        和「3 沒有左孩子」兩個洞。

        「往右找，直到找到第一個存在的孩子」——
        這個搜尋在第 116 題不需要，在這裡卻是必要的。

【失效原因三】：leftmost = leftmost.left 不成立
    -> 下一層的第一個節點，不一定是這一層第一個節點的左孩子。

    上面的例子裡，第 2 層的第一個是 2，
    但第 3 層的第一個是 4（= 2.left，剛好對）；
    如果 2 沒有孩子而 3 有，第 3 層的第一個就會是 3 的孩子。

【三個問題，一個解法全部解決：虛擬頭 + tail 指標。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,2,3,4,5,null,7]

            1
           / \\
          2   3
         / \\    \\
        4   5    7

  輸出：[1,#,2,3,#,4,5,7,#]

        1 -> None
        2 -> 3 -> None
        4 -> 5 -> 7 -> None

  說明：注意 5 -> 7 這一條 ——
        5 的父節點是 2，7 的父節點是 3，
        而且 3 【沒有左孩子】。
        第 116 題的 node.next.left 在這裡會拿到 None。

範例 2
  輸入：root = []
  輸出：[]""",
 "constraints": [
   "樹的節點數在 <code>[0, 6000]</code> 之間",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "idea": [
   ("c", """【虛擬頭（dummy head）+ tail 指標】

    cur = root                  # 目前這一層（next 已接好）
    while cur:
        dummy = Node(0)         # 下一層的「假頭」
        tail = dummy            # 下一層目前串到哪裡

        while cur:              # 沿著這一層的 next 走一遍
            if cur.left:  tail.next = cur.left;  tail = tail.next
            if cur.right: tail.next = cur.right; tail = tail.next
            cur = cur.next

        cur = dummy.next        # 下一層的第一個節點

【為什麼這樣就解決了全部三個問題？】

    問題一（孩子可能是 None）：
        用 if 判斷，不存在就跳過 ✔

    問題二（右鄰居可能隔很遠）：
        我們不「找」右鄰居，而是【按順序串起來】——
        tail 永遠指向「目前串好的最後一個」，
        下一個出現的孩子自然就是它的右鄰居 ✔

    問題三（下一層的第一個在哪）：
        不用知道！dummy.next 會自動是它 ✔
        這正是虛擬頭存在的理由。

【虛擬頭是鏈結串列題的萬用技巧】：

    它把「第一個節點」這個特例，
    變成和其他節點一模一樣的普通情況。

    第 2 題（兩數相加）、第 21 題（合併串列）、
    第 24 題（兩兩交換）、第 82/83 題（刪除重複）、
    第 148 題（排序串列）—— 全都用它。

    【看到「可能要改動頭節點」就先開一個 dummy。】"""),
 ],
 "approaches": [
   ap("解法一", "BFS 層序（最直覺，和第 116 題完全一樣）", [
     ("c", S["p117_bfs"]),
     "<strong>和第 116 題的解法一一字不差</strong> —— "
     "<strong>因為 BFS 根本不在乎樹的形狀。</strong>",
     "<strong>這就是「通用解法」的價值</strong>："
     "<strong>第 116 題的 O(1) 解法在這裡會爆炸，BFS 卻原封不動。</strong>",
     "<strong>O(n) 時間、O(w) 空間</strong> —— 不滿足進階要求，但一定對。",
     "<strong>面試時先寫這個</strong>，再說「我可以用虛擬頭做到 O(1) 空間」。",
   ], "O(n)", "O(w)", "每個節點一次", "佇列最大寬度"),

   ap("解法二", "虛擬頭 + tail（O(1) 空間，標準答案）", [
     ("c", S["p117_o1"]),
     ("h", "三個變數的分工"),
     ("c", """cur    目前正在「掃描」的那一層的游標
dummy  下一層的虛擬頭（每層重開一個）
tail   下一層「已經串好的最後一個」

    外層 while cur：處理一層
    內層 while cur：沿著這一層的 next 掃過去，
                    把看到的孩子一個一個接到 tail 後面

    內層結束時 cur 是 None（走到這一層的尾巴），
    然後 cur = dummy.next 跳到下一層的第一個 ✔

【注意 cur 這個變數被兩層迴圈共用】——
    內層把它走到 None，外層再用 dummy.next 重新賦值。

    這個寫法很精簡，但第一次看會有點繞。
    如果覺得不清楚，可以用兩個變數：

        level_head = root
        while level_head:
            dummy = Node(0); tail = dummy
            cur = level_head
            while cur:
                ...
                cur = cur.next
            level_head = dummy.next

    兩者等價，後者比較好讀。"""),
     ("h", "為什麼每層都要重開一個 <code>dummy</code>？"),
     ("c", """因為 dummy.next 要指向「這一層的第一個節點」。

    如果沿用上一層的 dummy，
    dummy.next 還指著上一層的第一個 —— 拿到錯的東西 ✘

    也可以只開一個 dummy，但每層開始時要 dummy.next = None：

        dummy = Node(0)
        while cur:
            dummy.next = None      # 重置
            tail = dummy
            ...

    兩種寫法都對。每層 new 一個比較不容易忘記重置，
    而且 n 層只多配置 n 個小物件 —— 仍然是 O(1) 的「額外空間」
    （嚴格說是 O(1) at a time，舊的會被回收）。

【如果面試官很嚴格地追問「你配置了 h 個 Node」】，
    就改用「一個 dummy + 每層重置」的寫法，
    那樣真的只配置一個物件。""",),
     "<strong>O(n) 時間、O(1) 額外空間。</strong>"
     "<strong>而且這個寫法對第 116 題也完全適用</strong> —— "
     "<strong>只要記這一個版本就夠了。</strong>",
   ], "O(n)", "O(1)", "每個節點一次", "一個 dummy + 兩個指標", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "對第 116 題也適用", "備註"],
   [["一、BFS", "O(n)", "O(w)", "✔", "最直覺"],
    ["二、虛擬頭 + tail", "O(n)", "O(1)", "✔", "標準答案，通用"]]),
 "post": [
   ("note", "第 116 題 vs 第 117 題：前提條件的價值", [
     ("c", """            第 116 題（完美）        第 117 題（任意）
    接 next   兩行搞定                要處理 None、要用 tail
    找下一層   leftmost.left           需要 dummy.next
    程式行數   9                       14
    通用性     只對完美樹              【對任何二元樹都對】

【教訓】：
    第 116 題的解法「更短」，但那是【買來的】——
    代價是它依賴一個很強的前提。

    第 117 題的解法長一點，但它【沒有前提】。

    在真實工程裡，
    「短但依賴強前提」的程式碼是技術債 ——
    因為前提遲早會被打破（資料變了、需求變了），
    而那時 bug 會出現在離修改點很遠的地方。

【如果只想記一個版本，記第 117 題的。】

    這也是為什麼很多面試官會直接問第 117 題：
    它能同時檢驗你會不會第 116 題。"""),
   ]),
 ],
 "edges": [
   "<strong><code>root = None</code></strong> → <code>None</code>。",
   "<strong>單一節點</strong> → <code>next</code> 保持 <code>None</code>。",
   "<strong><code>[1,2,3,4,5,null,7]</code></strong> → "
   "<strong><code>5.next = 7</code>（跨越了一個「洞」）。這是本題的核心測資。</strong>",
   "<strong>某一層只有一個節點</strong> → 它的 <code>next</code> 是 <code>None</code>。",
   "<strong>整棵樹是一條左鏈</strong> → 每層都只有一個節點，所有 <code>next</code> 都是 <code>None</code>。",
   "<strong>直接套用第 116 題的解法</strong> → "
   "<strong><code>node.left</code> 是 <code>None</code> 時 <code>AttributeError</code>。</strong>",
   "<strong>忘了每層重置 <code>dummy.next</code></strong> → 跳到上一層去，無窮迴圈。",
   "<strong>6000 個節點的鏈狀樹</strong> → 解法二完全沒問題（沒有遞迴）。",
 ],
 "follow": [
   ("h", "追問一：能不能用遞迴做這題？"),
   "<strong>可以，但比第 116 題麻煩得多。</strong>",
   ("c", """問題在於【遞迴的順序】：

    要接第 k+1 層時，必須先確定第 k 層【整層】都接好了。

    但一般的 DFS 是「深度優先」——
    走到左子樹很深的地方時，右子樹連碰都還沒碰到。

    所以要嘛：
        (a) 先接好右子樹再接左子樹（反序 DFS），
            並維護一個「每層目前最右節點」的陣列 -> O(h) 空間
        (b) 每次都從根往右找「第一個存在的孩子」-> 最壞 O(n²)

    兩個都不如迭代版乾淨。

【這是少數「迭代明顯優於遞迴」的樹題】——
    因為它的自然順序是【橫向】的，而遞迴天生是縱向的。""",),
   ("h", "追問二：<code>tail</code> 指標的技巧還能用在哪裡？"),
   ("ul", [
     "<strong>第 2 題 兩數相加</strong> —— 邊算邊往 <code>tail</code> 後面接",
     "<strong>第 21 題 合併兩個有序串列</strong> —— 同上",
     "<strong>第 86 題 分隔串列</strong> —— 開兩個 <code>dummy</code>，最後接起來",
     "<strong>第 328 題 奇偶串列</strong> —— 同上",
     "<strong>任何「一邊走一邊建一條新串列」的題目</strong>",
   ]),
   "<strong>共同模式</strong>：<code>dummy = Node(); tail = dummy; ... tail.next = x; tail = tail.next; ... return dummy.next</code>。"
   "<strong>把這六個字背下來，一整類題目就解決了。</strong>",
   ("h", "追問三：如果樹非常寬（例如 10⁶ 個葉節點）呢？"),
   "<strong>解法二完全不受影響</strong> —— 它的空間是 <code>O(1)</code>，和寬度無關。",
   "<strong>解法一（BFS）的佇列會吃掉 <code>O(w)</code>，可能撐不住。</strong>"
   "<strong>這就是「O(1) 空間」在實務上的價值 —— 它不只是面試題的花招。</strong>",
   ("h", "追問四：接好 <code>next</code> 之後，怎麼做 O(1) 空間的層序走訪？"),
   ("c", """leftmost = root
while leftmost:
    node = leftmost
    while node:
        print(node.val)
        node = node.next
    # 找下一層的第一個：沿著這一層往右找第一個有孩子的
    nxt = None
    node = leftmost
    while node and not nxt:
        nxt = node.left or node.right
        node = node.next
    leftmost = nxt

【完全不用佇列】——
    這正是第 117 題把 next 接好之後的直接紅利。

    B+ 樹的範圍掃描用的就是這個。"""),
 ],
 "related": [
   "<strong>第 116 題 Populating Next Right Pointers</strong> —— 有「完美」前提的版本",
   "<strong>第 102 題 Level Order Traversal</strong> —— 解法一的骨架",
   "<strong>第 21 題 Merge Two Sorted Lists</strong> —— 虛擬頭 + tail 的原型",
   "<strong>第 86 題 Partition List</strong> —— 兩個 dummy 的應用",
 ],
 "check": [
   "第 116 題的兩行在這裡為什麼全部失效？請各舉一個反例。",
   "虛擬頭 <code>dummy</code> 解決了「找下一層第一個節點」這個問題 —— 它是怎麼做到的？",
   "為什麼每一層都要重開（或重置）<code>dummy</code>？",
   "為什麼這題用遞迴反而比迭代麻煩？",
 ],
})
print("P117 written")
