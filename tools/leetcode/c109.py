# -*- coding: utf-8 -*-
"""第 109–112 題。"""
import random, math
from authoring import emit, ap
from runner import Src, TreeNode, ListNode, to_list, from_list

S = Src()
random.seed(109)


def _build(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _build(l), _build(r))


def _rand_tree(n, lo=-5, hi=5):
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi), _rand_tree(left, lo, hi), _rand_tree(n - 1 - left, lo, hi))


def _ino(nd):
    return [] if nd is None else _ino(nd.left) + [nd.val] + _ino(nd.right)


def _height(nd):
    return 0 if nd is None else 1 + max(_height(nd.left), _height(nd.right))


def _balanced(nd):
    if nd is None:
        return True
    return (abs(_height(nd.left) - _height(nd.right)) <= 1
            and _balanced(nd.left) and _balanced(nd.right))


def _is_bst(nd, lo=float("-inf"), hi=float("inf")):
    if nd is None:
        return True
    return (lo < nd.val < hi and _is_bst(nd.left, lo, nd.val) and _is_bst(nd.right, nd.val, hi))


# ==================== 109. Convert Sorted List to BST ====================
S["p109_array"] = '''class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 先把串列倒進陣列，就退化成第 108 題
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            return TreeNode(nums[mid], build(lo, mid - 1), build(mid + 1, hi))

        return build(0, len(nums) - 1)'''

S["p109_slow_fast"] = '''class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)       # 只剩一個節點

        # 快慢指標找中點，prev 用來把串列從中點「剪斷」
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None                    # 剪斷：左半變成獨立的一條串列

        node = TreeNode(slow.val)
        node.left = self.sortedListToBST(head)       # 左半
        node.right = self.sortedListToBST(slow.next) # 右半
        return node'''

S["p109_inorder"] = '''class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 先數長度
        n, p = 0, head
        while p:
            n += 1
            p = p.next

        self.cur = head                     # 串列游標，只會往前走

        def build(size: int) -> Optional[TreeNode]:
            """建一棵有 size 個節點的子樹，並順便消耗掉串列的前 size 個"""
            if size == 0:
                return None

            left = build(size // 2)         # 1) 先把左子樹建完
            node = TreeNode(self.cur.val)   # 2) 此時游標剛好指到這棵子樹的根
            self.cur = self.cur.next
            node.left = left
            node.right = build(size - size // 2 - 1)  # 3) 剩下的給右子樹
            return node

        return build(n)'''


_p109 = [S.load(k) for k in ("p109_array", "p109_slow_fast", "p109_inorder")]

for _ in range(2000):
    n = random.randrange(0, 30)
    nums = sorted(random.sample(range(-200, 200), n))
    for sol in _p109:
        t = sol.sortedListToBST(to_list(nums))
        assert _ino(t) == nums, ("P109 inorder", nums, sol)
        assert _is_bst(t), ("P109 not bst", nums, sol)
        assert _balanced(t), ("P109 not balanced", nums, sol)
for n in range(0, 130):
    nums = list(range(n))
    for sol in _p109:
        h = _height(sol.sortedListToBST(to_list(nums)))
        assert h == (0 if n == 0 else math.ceil(math.log2(n + 1))), ("P109 height", n, h, sol)
print("P109 solutions OK")

emit({
 "num": 109, "slug": "convert-sorted-list-to-binary-search-tree",
 "en": [
   "Given the <code>head</code> of a singly linked list where elements are "
   "<strong>sorted in ascending order</strong>, convert <em>it to a "
   "<strong>height-balanced</strong> binary search tree</em>.",
 ],
 "zh": [
   "給你一條<strong>升序排列</strong>的單向鏈結串列的頭節點 <code>head</code>，"
   "把它轉換成一棵<strong>高度平衡</strong>的二元搜尋樹。",
 ],
 "pre": [
   ("note", "和第 108 題只差一個字，但難度差很多", [
     ("c", """第 108 題：輸入是【陣列】 -> nums[mid] 是 O(1)
第 109 題：輸入是【串列】 -> 找中點是 O(n)

    整個難度差距就在這裡。

    如果照第 108 題的做法，每層都要 O(n) 找中點：
        T(n) = 2T(n/2) + O(n)  ->  O(n log n)

    能過，但不是最優。

【真正漂亮的解法（解法三）完全不找中點】——
    它反過來利用「中序走訪剛好是升序」這個性質，
    按中序的順序建節點，游標一路往前推進。

    O(n) 時間、O(log n) 空間 ——
    而且完全不用複製資料。

    這是本題真正想教你的東西。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [-10,-3,0,5,9]
  輸出：[0,-3,9,-10,null,5]

            0
           / \\
         -3   9
         /   /
      -10   5

  說明：和第 108 題一樣，答案不唯一。

範例 2
  輸入：head = []
  輸出：[]""",
 "constraints": [
   "串列的節點數在 <code>[0, 2 × 10⁴]</code> 之間",
   "−10⁵ ≤ <code>Node.val</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """三條路，由笨到巧：

【A. 倒進陣列】
    先把串列讀成 list，然後完全照第 108 題做。
    O(n) 時間、O(n) 額外空間。

    面試時先講這個 —— 它一定對，而且三十秒就能寫完。
    然後說：「但這用了 O(n) 額外空間，我可以做得更好。」

【B. 每次用快慢指標找中點】
    T(n) = 2T(n/2) + O(n) -> O(n log n) 時間、O(log n) 空間。

    比 A 省空間，但慢了 log n 倍。
    而且要小心「把串列剪斷」的細節。

【C. 中序建樹（最優）】
    先數長度 n（O(n)）。

    然後【按中序的順序建節點】：
        先建左子樹 -> 取當前節點當根 -> 再建右子樹

    因為中序走訪 BST 剛好是升序，
    而串列也剛好是升序 ——
    所以只要讓游標「依中序的節奏往前走」，
    每一步拿到的就是正確的值 ✔

    O(n) 時間、O(log n) 空間，完全不複製資料。

    【這是「把兩個升序序列對齊」的漂亮應用。】"""),
 ],
 "approaches": [
   ap("解法一", "倒進陣列 + 第 108 題（最實際）", [
     ("c", S["p109_array"]),
     "<strong>O(n) 時間、O(n) 空間。</strong>"
     "<strong>在真實工程裡這通常就是正確答案</strong> —— "
     "n = 2×10⁴ 的陣列只佔幾百 KB，換來的是「完全不會寫錯」。",
     "<strong>面試時先寫這個</strong>，然後主動說"
     "「這用了 O(n) 額外空間，如果不允許我可以改成…」。"
     "<strong>先給出一個正確解、再談優化，永遠是對的節奏。</strong>",
   ], "O(n)", "O(n)", "讀一遍 + 建一遍", "陣列副本"),

   ap("解法二", "快慢指標找中點", [
     ("c", S["p109_slow_fast"]),
     ("h", "三個容易錯的地方"),
     ("c", """1. 【必須記住 prev，用來剪斷】

   prev.next = None

   不剪斷的話，左半的遞迴會一路走到串列尾巴，
   把右半的節點也吃進左子樹 -> 無窮遞迴或結構錯亂。

2. 【必須特判 head.next is None】

   只剩一個節點時，prev 會是 None，
   prev.next = None 直接 AttributeError。

   （因為 while fast and fast.next 一次都沒跑。）

3. 【slow 停在哪裡？】

   prev, slow, fast = None, head, head
   while fast and fast.next:
       prev = slow; slow = slow.next; fast = fast.next.next

   n = 2： fast=head, fast.next 存在 -> 跑一輪
           slow 走到第 2 個，prev 是第 1 個
           -> 根是第 2 個，左子樹是第 1 個 ✔

   n = 3： 跑一輪後 fast 指到第 3 個，fast.next 是 None -> 停
           slow 在第 2 個（正中間）✔

   【快慢指標的「停在哪」有好幾種變體，
     一定要用 n = 1, 2, 3 手動驗一遍。】"""),
     ("h", "複雜度"),
     ("c", """T(n) = 2 T(n/2) + O(n)
           ^^^^^^^^   ^^^^
           兩個子問題  找中點

    由主定理（Master Theorem）-> O(n log n)

    這和歸併排序是同一個遞迴式 ——
    可以想成「這題在做一次隱形的歸併排序」。

空間 O(log n)：遞迴深度（樹是平衡的，所以是 log n）。

【比解法一省空間，但慢 log n 倍。
  n = 2×10⁴ 時 log n ≈ 15 —— 實測通常比解法一慢。】"""),
     "<strong>注意這個解法會破壞輸入的串列</strong>（剪斷了）。"
     "<strong>面試時要說出來。</strong>",
   ], "O(n log n)", "O(log n)", "每層找中點 O(n)", "遞迴堆疊"),

   ap("解法三", "中序建樹（最優，O(n) 時間 + O(log n) 空間）", [
     ("c", S["p109_inorder"]),
     ("h", "★ 這個解法的核心：反過來想"),
     ("c", """一般的建樹是「先決定根是誰，再分左右」。
這裡反過來：【先決定樹的形狀，再照中序填值】。

    因為：
        BST 的中序走訪 = 升序
        輸入的串列     = 升序

    所以只要「按中序的順序」建節點，
    每次拿串列的下一個值就一定是對的 ✔

    完全不需要知道「中點在哪裡」！

程式的三步（順序絕對不能變）：

    left = build(size // 2)          1) 先把左子樹整個建完
                                        （這會消耗掉前 size//2 個節點）
    node = TreeNode(self.cur.val)    2) 游標【此刻】剛好指到根
    self.cur = self.cur.next
    node.right = build(...)          3) 剩下的給右子樹

【為什麼第 2 步時游標剛好指到根？】

    因為第 1 步剛好消耗了「左子樹的所有節點」，
    而中序裡根就緊接在左子樹之後 ✔

    這正是中序走訪的定義：左 → 根 → 右。"""),
     ("h", "為什麼 <code>size // 2</code> 和 <code>size - size//2 - 1</code>？"),
     ("c", """size 個節點要分成：左子樹 + 根(1個) + 右子樹

    左：size // 2
    根：1
    右：size - size//2 - 1

    驗算 size = 5：
        左 = 2, 根 = 1, 右 = 5 - 2 - 1 = 2  ✔ （2+1+2 = 5）

    驗算 size = 4：
        左 = 2, 根 = 1, 右 = 4 - 2 - 1 = 1  ✔ （2+1+1 = 4）

    左右最多差 1 -> 保證平衡 ✔

【換成 (size-1)//2 也可以】，
    只是樹會偏向另一邊（一樣平衡）。""",),
     "<strong>時間 O(n)</strong>（數長度 O(n) + 建樹 O(n)，游標只走一遍）。"
     "<strong>空間 O(log n)</strong>（遞迴堆疊）。"
     "<strong>不複製資料、不破壞輸入。</strong>",
     "<strong>這個「先建結構、再按順序填值」的技巧，"
     "在任何「兩個序列順序一致」的場合都適用</strong> —— "
     "例如「把排序好的資料裝進 B 樹」「把已排序的檔案載入索引」。",
   ], "O(n)", "O(log n)", "游標只走一遍", "遞迴堆疊", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "破壞輸入？", "備註"],
   [["一、倒進陣列", "O(n)", "O(n)", "✘", "最實際，不會寫錯"],
    ["二、快慢指標", "O(n log n)", "O(log n)", "✔ 會剪斷", "省空間但慢"],
    ["三、中序建樹", "O(n)", "O(log n)", "✘", "最優，也最漂亮"]]),
 "edges": [
   "<strong>空串列</strong> → <code>None</code>。",
   "<strong>單一節點</strong> → 一個節點的樹。"
   "<strong>解法二必須特判這個，否則 <code>prev</code> 是 <code>None</code> 會 crash。</strong>",
   "<strong>兩個節點</strong> → 考驗快慢指標停在哪裡。",
   "<strong>解法二忘了 <code>prev.next = None</code></strong> → 左子樹會吃掉整條串列。",
   "<strong>解法三三個步驟順序寫錯</strong>（先取根再建左子樹）→ "
   "<strong>值會全部錯位，但樹的形狀是對的 —— 很難 debug。</strong>",
   "<strong>2×10⁴ 個節點</strong> → 樹高只有 15，遞迴安全。",
   "<strong>解法二對輸入的破壞</strong> → 呼叫端如果還要用原串列就出事。",
 ],
 "follow": [
   ("h", "追問一：解法三的正確性要怎麼證明？"),
   ("c", """要證明兩件事：

【1. 中序走訪等於原串列】

    對 build(size) 做歸納：
        size = 0 -> 空樹，消耗 0 個節點 ✔
        size > 0 -> 由歸納假設，build(size//2) 產生的子樹
                    中序等於串列的前 size//2 個，
                    並把游標推進 size//2 格。

                    接著取的那個值就是第 (size//2 + 1) 個 ✔

                    右子樹同理。

        串起來就是「串列的前 size 個，順序不變」✔

【2. 樹是平衡的】

    左子樹 size//2 個、右子樹 size - size//2 - 1 個，
    兩者最多差 1（見上面的驗算）。

    設 H(k) = build(k) 的高度，H 單調遞增，
    則 |H(左) - H(右)| <= 1 ✔

    對每一層都成立 -> 整棵樹平衡 ✔

【能把這兩件事講清楚，這題就滿分了。】""",),
   ("h", "追問二：如果串列是降序呢？"),
   "<strong>三種做法都只要「反過來」</strong>：解法一把陣列 <code>[::-1]</code>；"
   "解法三把「先建左子樹」改成「先建右子樹」。",
   "<strong>或者更簡單：先把串列反轉（第 206 題）再照常做</strong> —— "
   "<strong>「化簡成已解決的問題」通常比重寫一份鏡像邏輯安全。</strong>",
   ("h", "追問三：如果不要求平衡，只要是 BST 呢？"),
   "<strong>那就太簡單了 —— 直接把串列當成一條「全部往右」的鏈</strong>："
   "<code>root = 第一個，root.right = 第二個, ...</code>",
   "<strong>它是合法的 BST（中序就是升序），但高度 n</strong>。"
   "<strong>「平衡」這個要求，才是這題真正的內容。</strong>",
   ("h", "追問四：能不能 O(1) 額外空間？"),
   "<strong>不行</strong> —— 輸出本身就是一棵有 n 個節點的樹，<strong>至少要 O(n) 空間存它</strong>。",
   "<strong>如果指的是「除了輸出以外」的額外空間</strong>，"
   "<strong>O(log n) 的遞迴堆疊已經是下界</strong>："
   "要建一棵高 <code>log n</code> 的樹，總得記住「現在在哪一條路徑上」。",
 ],
 "related": [
   "<strong>第 108 題 有序陣列轉 BST</strong> —— 本題的陣列版",
   "<strong>第 876 題 Middle of the Linked List</strong> —— 快慢指標找中點",
   "<strong>第 148 題 Sort List</strong> —— 同樣用快慢指標切一半",
   "<strong>第 110 題 Balanced Binary Tree</strong> —— 驗證輸出是否平衡",
 ],
 "check": [
   "為什麼「中序建樹」不需要找中點？它利用了什麼性質？",
   "解法三的三個步驟順序寫錯會怎樣？樹的形狀會錯嗎？",
   "快慢指標版為什麼一定要記住 <code>prev</code>？為什麼要特判單一節點？",
   "解法二的遞迴式是什麼？為什麼解出來是 O(n log n)？",
 ],
})
print("P109 written")

# ==================== 110. Balanced Binary Tree ====================
S["p110_naive"] = '''class Solution:
    # 【O(n²) 版，先講它為什麼慢】
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True
        return (abs(height(root.left) - height(root.right)) <= 1
                and self.isBalanced(root.left)
                and self.isBalanced(root.right))'''

S["p110_pair"] = '''class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def go(node):
            """回傳 (是否平衡, 高度)"""
            if not node:
                return True, 0
            lb, lh = go(node.left)
            if not lb:
                return False, 0             # 左邊就不平衡了，不用再算
            rb, rh = go(node.right)
            if not rb:
                return False, 0
            return abs(lh - rh) <= 1, 1 + max(lh, rh)

        return go(root)[0]'''

S["p110_sentinel"] = '''class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node) -> int:
            """回傳高度；若子樹不平衡，回傳 -1 當作「失敗」的哨兵值"""
            if not node:
                return 0

            lh = height(node.left)
            if lh == -1:
                return -1                   # 失敗一路往上傳

            rh = height(node.right)
            if rh == -1:
                return -1

            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)

        return height(root) != -1'''


def _p110_ref(nd):
    return _balanced(nd)


_p110 = [S.load(k) for k in ("p110_naive", "p110_pair", "p110_sentinel")]

for spec, want in [
    ([3, [9, None, None], [20, [15, None, None], [7, None, None]]], True),
    ([1, [2, [3, [4, None, None], [4, None, None]], [3, None, None]], [2, None, None]], False),
    (None, True),
    ([1, None, None], True),
    ([1, [2, None, [3, None, None]], None], False),
]:
    t = _build(spec)
    assert _p110_ref(t) is want, ("P110 ref", spec)
    for sol in _p110:
        assert sol.isBalanced(_build(spec)) is want, ("P110", spec, sol)

for _ in range(5000):
    t = _rand_tree(random.randrange(0, 13))
    want = _p110_ref(t)
    for sol in _p110:
        assert sol.isBalanced(t) is want, ("P110 random", want, sol)
# 第 108 題建出來的樹一定平衡
_p108build = S.load("p109_inorder")
for n in range(0, 60):
    t = _p108build.sortedListToBST(to_list(list(range(n))))
    for sol in _p110:
        assert sol.isBalanced(t) is True, ("P110 vs P109", n, sol)
print("P110 solutions OK")

_P110_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">「高度平衡」= 每一個節點的左右子樹高度差都 ≤ 1。只檢查根節點是不夠的。</text>
            <text x="20" y="50" fill="#ff8a65" font-size="13">反例：root = [1,2,2,3,3,null,null,4,4]　根看起來還好，但下面壞了</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="300" cy="90" r="18" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="300" y="95" fill="var(--gold)">1</text>
              <circle cx="210" cy="148" r="18" fill="none" stroke="#ff8a65" stroke-width="3"/><text x="210" y="153" fill="#ff8a65">2</text>
              <circle cx="390" cy="148" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="390" y="153" fill="var(--accent)">2</text>
              <circle cx="140" cy="206" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="140" y="211" fill="var(--accent)">3</text>
              <circle cx="272" cy="206" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="272" y="211" fill="var(--accent)">3</text>
              <circle cx="100" cy="264" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="100" y="269" fill="var(--accent)">4</text>
              <circle cx="180" cy="264" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="180" y="269" fill="var(--accent)">4</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="287" y1="103" x2="223" y2="135"/><line x1="313" y1="103" x2="377" y2="135"/>
              <line x1="197" y1="161" x2="153" y2="193"/><line x1="223" y1="161" x2="259" y2="193"/>
              <line x1="127" y1="219" x2="113" y2="251"/><line x1="153" y1="219" x2="167" y2="251"/>
            </g>
            <text x="340" y="196" fill="var(--text-muted)" font-size="11" text-anchor="start">根：左高 3、右高 1 → 差 2 ✘</text>
            <text x="340" y="220" fill="#ff8a65" font-size="11" text-anchor="start">左邊那個 2：左高 2、右高 1 → 差 1 ✔</text>
            <text x="340" y="244" fill="var(--text-muted)" font-size="11" text-anchor="start">所以問題出在【根】這一層</text>
            <line x1="20" y1="292" x2="620" y2="292" stroke="var(--border)"/>
            <text x="20" y="318" fill="var(--gold)" font-size="12">O(n²) 版為什麼慢：isBalanced 對每個節點呼叫 height，而 height 又要走整棵子樹。</text>
            <text x="20" y="342" fill="var(--text-muted)" font-size="12">深度 d 的節點被 height 走過 d 次 → 鏈狀樹上總共 1+2+…+n = O(n²)。</text>
            <text x="20" y="370" fill="var(--accent)" font-size="12">修法：讓遞迴【一次回傳兩件事】——「高度」和「是否平衡」。每個節點只走一次 → O(n)。</text>
            <text x="20" y="396" fill="var(--accent)" font-size="12">或者更精簡：只回傳高度，用 -1 這個不可能的值當作「這裡不平衡」的哨兵。</text>'''

emit({
 "num": 110, "slug": "balanced-binary-tree",
 "en": [
   "Given a binary tree, determine if it is <strong>height-balanced</strong>.",
   "A <strong>height-balanced</strong> binary tree is a binary tree in which the depth of the "
   "two subtrees of <em>every</em> node never differs by more than one.",
 ],
 "zh": [
   "給你一個二元樹，判斷它是不是<strong>高度平衡</strong>的。",
   "<strong>高度平衡</strong>的定義是：<strong>每一個</strong>節點的"
   "左右兩棵子樹，高度差<strong>都不超過 1</strong>。",
 ],
 "pre": [
   ("note", "關鍵字是「每一個」", [
     ("c", """不是「根節點的左右高度差 <= 1」，
而是【樹上的每一個節點都要滿足】。

    只檢查根的話：

            1
           / \\
          2   2
         / \\
        3   3
       / \\
      4   4

        根：左高 3、右高 1 -> 差 2 ✘

    這個例子根就壞了，看得出來。

    但反過來的情況也存在 ——
    根很平衡，某個深處的節點卻歪掉了。

    所以【一定要檢查所有節點】。

【這題真正的考點不是「怎麼判斷」，
  而是「怎麼在一趟走訪裡判斷完」。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [3,9,20,null,null,15,7]

            3
           / \\
          9   20
             /  \\
            15   7

  輸出：true

範例 2
  輸入：root = [1,2,2,3,3,null,null,4,4]

            1
           / \\
          2   2
         / \\
        3   3
       / \\
      4   4

  輸出：false
  說明：根的左子樹高 3、右子樹高 1，差了 2。

範例 3
  輸入：root = []
  輸出：true""",
 "constraints": [
   "樹的節點數在 <code>[0, 5000]</code> 之間",
   "−10⁴ ≤ <code>Node.val</code> ≤ 10⁴",
 ],
 "idea": [
   ("fig", _P110_FIG, "0 0 640 414"),
   ("c", """直覺的寫法（解法一）：

    對每個節點，算出左右高度，比較一下，然後遞迴檢查左右子樹。

    問題：算高度本身就要走整棵子樹！

    -> 每個節點被「算高度」這件事重複訪問很多次
    -> 最壞 O(n²)

【怎麼修？】

    觀察：算高度的過程，其實【已經走過所有節點了】。

    那為什麼不在算高度的【同時】順便檢查平衡？

    答案：讓遞迴函式【一次回傳兩件事】。

        go(node) -> (是否平衡, 高度)

    這樣每個節點只被訪問一次 -> O(n) ✔

【這個「後序走訪 + 回傳一包資訊」的手法，
  是樹題最重要的優化範式。】

    第 124 題（最大路徑和）、第 543 題（直徑）、
    第 236 題（最近公共祖先）、第 337 題（打家劫舍 III）
    全部都是這一招。

    共同結構：
        1. 遞迴到底
        2. 拿到左右子樹的「一包資訊」
        3. 用它們算出「自己的一包資訊」往上傳
        4. 順便更新全域答案（如果需要）"""),
 ],
 "approaches": [
   ap("解法一", "先算高度再比較（O(n²)，講清楚它為什麼慢）", [
     ("c", S["p110_naive"]),
     ("h", "為什麼是 O(n²)？"),
     ("c", """height(node) 要走遍 node 的整棵子樹 -> O(子樹大小)

    isBalanced 對每個節點都呼叫一次 height。

    【所以每個節點會被 height 訪問「它的深度」那麼多次】：
        深度 0 的節點被訪問 1 次
        深度 1 的節點被訪問 2 次
        ...
        深度 d 的節點被訪問 d+1 次

    退化成一條鏈時：
        1 + 2 + 3 + ... + n = O(n²)

        n = 5000 -> 1250 萬次 —— 勉強能過，但很慢。

    平衡樹時：
        每一層總共 O(n) 的工作，共 log n 層 -> O(n log n)

【所以它「能過」，但面試官一定會問「能不能一趟走完」。】"""),
     "<strong>優點：最好想、最好寫。</strong>"
     "<strong>面試時可以先寫它把思路講清楚，再優化。</strong>",
   ], "O(n²) 最壞", "O(h)", "高度被重複計算", "遞迴堆疊"),

   ap("解法二", "後序回傳 (平衡, 高度) 一包（標準答案）", [
     ("c", S["p110_pair"]),
     ("h", "為什麼這樣就 O(n) 了？"),
     ("c", """每個節點只被 go() 呼叫【一次】。

    它從左右孩子拿到已經算好的 (平衡, 高度)，
    用 O(1) 的工作合成自己的答案。

    n 個節點 × O(1) = O(n) ✔

【和解法一的差別，本質上是「記憶化」的思想】：

    解法一：每次要高度就重算一遍
    解法二：算過的高度順著遞迴往上傳，不重算

    這和「費氏數列用遞迴 vs 用 DP」是同一個道理。""",),
     ("h", "提早結束的小優化"),
     ("c", """if not lb:
    return False, 0        # 左邊不平衡，右邊根本不用算

    這個「短路」在最壞情況下幫不上忙（整棵樹都平衡時要全走完），
    但在「問題出現得早」的測資上能省下大量時間。

    注意回傳的高度隨便填 0 就好 ——
    因為 lb 是 False，上層看到就直接往上傳 False，
    高度不會被用到。

    【但如果你之後要改這段程式碼，
      「隨便填的值」會變成隱患。
      解法三用哨兵值就沒有這個問題。】"""),
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊", optimal=True),

   ap("解法三", "用 −1 當哨兵（最精簡）", [
     ("c", S["p110_sentinel"]),
     ("h", "核心：用一個「不可能的高度」表示失敗"),
     ("c", """高度永遠 >= 0，所以 -1 是一個「不可能出現」的值。

    用它來表示「這棵子樹不平衡」，
    就不需要回傳 tuple 了。

    height(node) 的語意變成：
        >= 0  -> 這棵子樹平衡，而且高度是這個數
        == -1 -> 這棵子樹不平衡

【好處】：
    ✔ 不用打包 / 拆包 tuple，常數比較小
    ✔ 程式碼更短
    ✔ 不會有「隨便填的高度」這種隱患

【壞處】：
    ✘ 語意藏在一個魔術數字裡，可讀性略差
    ✘ 如果之後需要「不平衡時也回傳真實高度」就得重寫

【哨兵值（sentinel）是很常見的技巧】：
    -1 表示「找不到」（str.find）
    None 表示「沒有值」
    float('inf') 表示「還沒找到更小的」
    虛擬頭節點（dummy head）表示「串列開始之前」

    共同點：用一個「正常情況不會出現的值」
    來省掉額外的旗標變數。"""),
     "<strong>兩個版本複雜度完全相同</strong>，"
     "<strong>挑一個順手的就好</strong>。"
     "<strong>面試時寫解法二（語意清楚）並提一句「也可以用 -1 當哨兵」最好。</strong>",
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "可讀性", "備註"],
   [["一、算高度再比較", "O(n²) 最壞", "O(h)", "★★★", "先講思路用"],
    ["二、回傳 (平衡, 高度)", "O(n)", "O(h)", "★★★", "標準答案"],
    ["三、−1 哨兵", "O(n)", "O(h)", "★★☆", "最短，常數最小"]]),
 "post": [
   ("note", "「後序回傳一包資訊」能解的題目", [
     ("c", """共同骨架：

    def go(node):
        if not node:
            return <base 的那一包>
        L = go(node.left)
        R = go(node.right)
        <可能順便更新全域答案>
        return <用 L, R 組出自己的那一包>

  110  是否平衡        回傳 (平衡, 高度)              （本題）
  543  直徑            回傳 高度，答案 = max(左高+右高)
  124  最大路徑和      回傳 單邊最大，答案 = max(左+根+右)
  236  最近公共祖先    回傳 「子樹裡有沒有 p / q」
  337  打家劫舍 III    回傳 (偷這個節點的最大值, 不偷的最大值)
  968  監控二元樹      回傳 節點的三種狀態
  1245 樹的直徑        同 543，推廣到一般圖

【辨認訊號】：
    「每個節點都要一個答案，而且答案依賴子樹的某種統計量」
    -> 八成就是這一招。

【最容易錯的地方】：
    搞混「回傳給父節點的值」和「答案」。
    第 124 題會把這個講透。"""),
   ]),
 ],
 "edges": [
   "<strong><code>root = None</code></strong> → <code>True</code>（空樹是平衡的）。",
   "<strong>單一節點</strong> → <code>True</code>。",
   "<strong><code>[1,2,null,3,null]</code></strong>（一條左鏈，3 個節點）→ <code>False</code>。"
   "<strong>根的左高 2、右高 0，差 2。</strong>",
   "<strong><code>[1,2,null]</code></strong> → <code>True</code>（左高 1、右高 0，差 1）。",
   "<strong>範例 2 的樹</strong> → <code>False</code>，"
   "<strong>但要注意問題出在「根」而不是更深的節點</strong>。",
   "<strong>完全二元樹</strong>（5000 個節點）→ <code>True</code>，樹高只有 13。",
   "<strong>退化成一條鏈</strong>（5000 個節點）→ "
   "<code>False</code>，但<strong>解法一要跑 1250 萬次</strong>，"
   "<strong>而且遞迴深度 5000 可能 <code>RecursionError</code></strong>。",
   "<strong>只檢查根節點</strong> → 漏掉「深處歪掉」的情況。",
 ],
 "follow": [
   ("h", "追問一：如果要回報「哪個節點不平衡」呢？"),
   "<strong>把哨兵改成回傳 <code>(高度, 第一個壞掉的節點)</code></strong>，"
   "或是<strong>在發現不平衡時記錄到一個成員變數</strong>。",
   "<strong>注意「第一個」的定義</strong>：後序走訪會<strong>先發現最深的那個</strong>。"
   "如果要「最靠近根的那個」，就要改成前序或走完之後再挑。",
   ("h", "追問二：這和 AVL 樹是什麼關係？"),
   ("c", """AVL 樹就是【始終維持這個平衡條件】的 BST。

    它在每次插入 / 刪除之後，
    用「旋轉」（rotation）把違反條件的地方修好。

    本題只是【檢查】，AVL 是【維護】——
    檢查 O(n)，維護則是每次操作 O(log n)。

【為什麼要維持平衡？】
    BST 的所有操作（查找、插入、刪除）都是 O(h)。
    平衡時 h = O(log n)，退化時 h = O(n)。

    所以平衡把最壞情況從 O(n) 拉回 O(log n)。

【其他平衡樹】：
    紅黑樹（Red-Black）：條件較鬆，旋轉次數較少
                        -> C++ 的 std::map、Java 的 TreeMap
    Treap / Skip List：  用隨機性達到「期望平衡」
    B 樹 / B+ 樹：       多路平衡，為磁碟 I/O 優化
                        -> 幾乎所有資料庫的索引

    AVL 比紅黑樹「更平衡」（查找略快），
    但插入刪除的旋轉較多（寫入略慢）。"""),
   ("h", "追問三：「高度平衡」和「重量平衡」有什麼不同？"),
   ("c", """高度平衡（本題）：|左子樹高度 - 右子樹高度| <= 1
重量平衡：          左右子樹的【節點數】比例在某個範圍內

    兩者不互相包含：

        高度平衡但不重量平衡：
            左子樹是滿的（2^k - 1 個節點）
            右子樹是一條鏈（k 個節點）
            高度都是 k -> 高度平衡 ✔
            但節點數差很多 -> 不重量平衡 ✘

    實務上：
        高度平衡 -> 保證查找是 O(log n)
        重量平衡 -> 保證「隨機查找的平均成本」低

    Scapegoat Tree 用的是重量平衡，
    AVL / 紅黑樹用的是高度平衡（或其變體）。""",),
   ("h", "追問四：能不能不用遞迴？"),
   "<strong>可以，用後序的迭代走訪</strong>（第 145 題），"
   "配一個 <code>dict</code> 記錄每個節點的高度。",
   "<strong>但會比遞迴版長很多</strong>，"
   "而且<strong>本題 n ≤ 5000、樹高最多 5000</strong> —— "
   "<strong>真正的風險是「鏈狀樹時遞迴太深」</strong>，"
   "那時迭代版才有價值。",
 ],
 "related": [
   "<strong>第 104 題 Maximum Depth</strong> —— 本題用到的 <code>height</code>",
   "<strong>第 543 題 Diameter of Binary Tree</strong> —— 同一個「回傳一包」的骨架",
   "<strong>第 124 題 Maximum Path Sum</strong> —— 同上，但「回傳值 ≠ 答案」更明顯",
   "<strong>第 108/109 題 轉成平衡 BST</strong> —— 產生本題的合格輸入",
 ],
 "check": [
   "為什麼只檢查根節點是不夠的？",
   "解法一為什麼是 O(n²)？在什麼形狀的樹上最糟？",
   "「後序回傳一包資訊」為什麼能把 O(n²) 降到 O(n)？",
   "用 −1 當哨兵的前提是什麼？什麼情況下這個技巧會失效？",
 ],
})
print("P110 written")

# ==================== 111. Minimum Depth of Binary Tree ====================
S["p111_rec"] = '''class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # 【關鍵】只有一邊有孩子時，不能取 min（空的那邊不算路徑）
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))'''

S["p111_bfs"] = '''from collections import deque

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth, dq = 1, deque([root])
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if not node.left and not node.right:
                    return depth            # 【第一個遇到的葉節點就是答案】
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            depth += 1

        return depth'''

S["p111_wrong"] = '''class Solution:
    # 【這是錯的，不要抄】
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))'''


def _p111_ref(nd):
    """獨立參考解：列出所有葉節點的深度取最小。"""
    if nd is None:
        return 0
    out = []
    def go(x, d):
        if not x.left and not x.right:
            out.append(d)
            return
        if x.left:
            go(x.left, d + 1)
        if x.right:
            go(x.right, d + 1)
    go(nd, 1)
    return min(out)


_p111 = [S.load(k) for k in ("p111_rec", "p111_bfs")]
_p111_bad = S.load("p111_wrong")

for spec, want in [
    ([3, [9, None, None], [20, [15, None, None], [7, None, None]]], 2),
    ([2, None, [3, None, [4, None, [5, None, [6, None, None]]]]], 5),
    (None, 0),
    ([1, None, None], 1),
    ([1, [2, None, None], None], 2),
]:
    t = _build(spec)
    assert _p111_ref(t) == want, ("P111 ref", spec)
    for sol in _p111:
        assert sol.minDepth(_build(spec)) == want, ("P111", spec, sol)

# 錯誤寫法確實在「單邊為空」時答錯
_bad = _build([1, [2, None, None], None])
assert _p111_bad.minDepth(_bad) == 1 and _p111_ref(_bad) == 2, "P111 wrong-demo"

for _ in range(5000):
    t = _rand_tree(random.randrange(0, 13))
    want = _p111_ref(t)
    for sol in _p111:
        assert sol.minDepth(t) == want, ("P111 random", want, sol)
print("P111 solutions OK")

emit({
 "num": 111, "slug": "minimum-depth-of-binary-tree",
 "en": [
   "Given a binary tree, find its minimum depth.",
   "The minimum depth is the number of nodes along the shortest path from the root node down "
   "to the nearest <strong>leaf</strong> node.",
   "<strong>Note:</strong> A leaf is a node with no children.",
 ],
 "zh": [
   "給你一個二元樹，求它的<strong>最小深度</strong>。",
   "<strong>最小深度</strong>是從根節點到<strong>最近的葉節點</strong>"
   "那條路徑上的<strong>節點個數</strong>。",
   "<strong>注意：</strong>「葉節點」是指<strong>沒有任何孩子</strong>的節點。",
 ],
 "pre": [
   ("note", "★ 這題唯一的考點：不能把第 104 題的 max 換成 min", [
     ("c", S["p111_wrong"]),
     ("c", """這段看起來完全合理，但它是【錯的】。

反例：

        1
       /
      2

    minDepth(1)
      = 1 + min(minDepth(2), minDepth(None))
      = 1 + min(1, 0)
      = 1 + 0
      = 1    ✘

    但根節點【不是葉節點】（它有一個孩子），
    所以最短路徑必須走到節點 2 -> 答案是 2。

【問題出在哪裡？】

    空子樹回傳 0。

    對 max 來說，0 是無害的 ——
    取最大時它會被忽略，「另一邊的真實深度」勝出。

    對 min 來說，0 是災難 ——
    它會把答案直接拉到 0，吃掉正確答案。

【0 對 max 是單位元素，對 min 不是。】

    這個不對稱就是第 104 題和第 111 題的全部差別，
    也是這題被單獨列出來的唯一理由。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [3,9,20,null,null,15,7]

            3
           / \\
          9   20
             /  \\
            15   7

  輸出：2
  說明：9 是葉節點，路徑 3 -> 9 有 2 個節點。

範例 2
  輸入：root = [2,null,3,null,4,null,5,null,6]

      2
       \\
        3
         \\
          4
           \\
            5
             \\
              6

  輸出：5
  說明：唯一的葉節點是 6，路徑有 5 個節點。
        【注意這裡答案不是 2 ——
          雖然節點 2 只有一個孩子，但它不是葉節點。】""",
 "constraints": [
   "樹的節點數在 <code>[0, 10⁵]</code> 之間",
   "−1000 ≤ <code>Node.val</code> ≤ 1000",
 ],
 "mid": [
   ("note", "節點數可以到 10⁵ —— 這是個明確的提示", [
     "<strong>如果樹退化成一條鏈，遞迴深度會是 10⁵</strong>，"
     "<strong>Python 一定會 <code>RecursionError</code></strong>。",
     "<strong>而且鏈狀樹正是這題最糟的情況</strong>（要走到最底才找到唯一的葉節點）。",
     "<strong>所以這題的「正確答案」其實是 BFS（解法二）</strong> —— "
     "它<strong>不但沒有深度問題，還能提早結束</strong>。",
   ]),
 ],
 "idea": [
   ("c", """正確的遞迴要分三種情況：

    if not root:        return 0              空樹

    if not root.left:   return 1 + f(right)   只有右孩子 -> 必須往右
    if not root.right:  return 1 + f(left)    只有左孩子 -> 必須往左

    return 1 + min(f(left), f(right))         兩邊都有 -> 才能取 min

【換個角度理解】：
    min 只在「兩條路都是真的路」時才有意義。

    空子樹不是一條「通往葉節點的路」，
    它是「此路不通」——
    所以應該當作 +∞ 而不是 0。

    寫成這樣也對（而且更統一）：

        def f(node):
            if not node:
                return float('inf')          # 此路不通
            if not node.left and not node.right:
                return 1                     # 是葉節點
            return 1 + min(f(node.left), f(node.right))

        # 外層要處理空樹
        return 0 if not root else f(root)

    【用 inf 當「不可能」的哨兵，
      比三個 if 更能表達意圖。】

但【最好的解法是 BFS】：
    層序走訪時，【第一個遇到的葉節點】就是最淺的葉節點。
    找到就立刻回傳，完全不用走完整棵樹。"""),
 ],
 "approaches": [
   ap("解法一", "遞迴（要分三種情況）", [
     ("c", S["p111_rec"]),
     "<strong>三個 <code>if</code>，一個都不能少。</strong>",
     ("h", "為什麼不能只寫「是葉節點就回 1」？"),
     ("c", """有人會寫：

    if not root.left and not root.right:
        return 1
    return 1 + min(f(root.left), f(root.right))

    這【還是錯的】——

        1
       /
      2

    節點 1 不是葉節點 -> 走到第二行
    -> 1 + min(f(2), f(None)) = 1 + min(1, 0) = 1 ✘

    「是不是葉節點」和「某一邊是不是空」是兩個不同的檢查，
    兩個都要做。

    正確的寫法要嘛是本文的三個 if，
    要嘛是上面 idea 裡用 inf 的版本。""",),
     "<strong>時間 O(n)</strong>（最壞要走完整棵樹）、"
     "<strong>空間 O(h)</strong>。",
     "<strong>對 n = 10⁵ 的鏈狀樹，這個版本會 <code>RecursionError</code>。</strong>",
   ], "O(n)", "O(h)", "最壞走完整棵樹", "遞迴堆疊"),

   ap("解法二", "BFS —— 第一個葉節點就是答案（本題最佳）", [
     ("c", S["p111_bfs"]),
     ("h", "★ 為什麼 BFS 在這題完勝遞迴？"),
     ("c", """BFS 是【一層一層】往外擴散的，
所以【先遇到的葉節點一定比較淺】。

    找到第一個葉節點 -> 立刻回傳 -> 【完全不用走完整棵樹】

    對照第 104 題（最大深度）：
        那題必須走完整棵樹才知道最深在哪 ——
        BFS 沒有任何優勢，遞迴的三行版反而更好。

    這題則相反：
        【提早結束】是巨大的優勢。

    極端例子：

        根的左孩子是葉節點，
        右子樹有 10⁵ 個節點。

        遞迴版：走完 10⁵ 個節點
        BFS：   第二層就回傳 -> 只看了 3 個節點 ✔

【這是「BFS 找最短、DFS 找最長」這條通則的完美示範。】

    最短路徑 -> BFS（第一次到達就是最短）
    最長路徑 / 全部路徑 -> DFS（反正都要走完）"""),
     ("h", "為什麼不用擔心遞迴深度？"),
     "<strong>BFS 完全沒有遞迴</strong>，佇列的大小是 <code>O(w)</code>（最大寬度）。",
     "<strong>而且對這題最糟的情況（鏈狀樹），寬度只有 1</strong> —— "
     "<strong>BFS 的空間反而是 O(1)。</strong>"
     "<strong>遞迴版在那裡爆掉，BFS 卻毫髮無傷。</strong>",
     "<strong>唯一的弱點是「又寬又淺」的樹</strong>（例如完全二元樹），"
     "那時佇列會到 <code>O(n/2)</code>。"
     "<strong>但那種樹的最小深度很淺，BFS 一樣很快就結束了。</strong>",
   ], "O(n) 最壞", "O(w)", "通常提早結束", "佇列寬度", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "能提早結束", "鏈狀樹會爆嗎"],
   [["一、遞迴", "O(n)", "O(h)", "✘", "✔ 會 RecursionError"],
    ["二、BFS", "O(n) 最壞", "O(w)", "✔", "✘ 安全"]]),
 "edges": [
   "<strong><code>root = None</code></strong> → <code>0</code>。",
   "<strong>單一節點</strong> → <code>1</code>。",
   "<strong><code>[1,2]</code></strong>（只有左孩子）→ <code>2</code>，<strong>不是 1</strong>。"
   "<strong>這是本題的核心測資 —— 直接把 <code>max</code> 換 <code>min</code> 會答 1。</strong>",
   "<strong><code>[1,null,2]</code></strong>（只有右孩子）→ <code>2</code>。同上。",
   "<strong>範例 2 的一條右鏈</strong> → <code>5</code>，不是 2。",
   "<strong>完全二元樹</strong> → 所有葉節點同深度，答案 = 最大深度。",
   "<strong>10⁵ 個節點的鏈狀樹</strong> → "
   "<strong>遞迴版 <code>RecursionError</code>，BFS 版完全沒事。</strong>",
   "<strong>只寫「是葉節點回 1」而沒處理「單邊為空」</strong> → 仍然錯。",
 ],
 "follow": [
   ("h", "追問一：為什麼第 104 題（max）不用特判？"),
   ("c", """因為【0 是 max 的單位元素，不是 min 的】。

    max(真實深度, 0) = 真實深度 ✔   （0 被忽略）
    min(真實深度, 0) = 0          ✘   （0 吃掉答案）

【更一般的說法】：
    空子樹的回傳值，應該是「該運算的單位元素」。

        求 max  -> 單位元素是 -∞（或 0，如果值都非負）
        求 min  -> 單位元素是 +∞
        求 sum  -> 單位元素是 0
        求 product -> 單位元素是 1
        求 and  -> 單位元素是 True
        求 or   -> 單位元素是 False

    【base case 填錯單位元素，是遞迴題最常見的 bug 來源。】

    這題填了 0（sum 的單位元素）給 min 用 —— 所以錯了。
    正確的應該是 float('inf')。""",),
   ("h", "追問二：如果要「最淺的葉節點的值」而不是深度呢？"),
   "<strong>BFS 版只要把 <code>return depth</code> 改成 <code>return node.val</code></strong>。",
   "<strong>如果有多個同深度的葉節點</strong>，BFS 會回傳<strong>最左邊</strong>的那個"
   "（因為佇列是從左到右填的）—— <strong>這正是第 513 題（找樹左下角的值）的變形。</strong>",
   ("h", "追問三：如果要「根到最近葉節點的路徑」呢？"),
   "<strong>BFS 時在佇列裡存 <code>(節點, 路徑)</code></strong>，"
   "或是<strong>存一個 <code>parent</code> 字典，找到葉節點後往回追。</strong>",
   "<strong>存 <code>parent</code> 比較省空間</strong> —— "
   "存完整路徑的話每個節點都要複製一份 list，"
   "<strong>最壞 <code>O(n·h)</code></strong>。"
   "<strong>「記父節點、事後回溯」是 BFS 求路徑的標準做法</strong>，"
   "第 126 題（單詞接龍 II）會把這招用到極致。",
   ("h", "追問四：什麼時候該用 BFS、什麼時候該用 DFS？"),
   ("c", """【用 BFS】
    ✔ 求「最短 / 最少步數」——第一次到達就是最優
    ✔ 只需要前幾層
    ✔ 樹很深、怕遞迴爆掉
    ✔ 要「逐層」處理（第 102、103、107、199 題）

【用 DFS】
    ✔ 求「最長 / 全部路徑」——反正都要走完
    ✔ 要回溯（第 113 題：路徑總和 II）
    ✔ 樹很寬（DFS 的 O(h) 比 BFS 的 O(w) 省）
    ✔ 需要「後序合併子樹資訊」（第 110、124 題）

【這一題（最小深度）是 BFS，
  第 104 題（最大深度）是 DFS ——
  兩題放在一起看，這條界線就很清楚了。】"""),
 ],
 "related": [
   "<strong>第 104 題 Maximum Depth</strong> —— 對照組，為什麼那題不用特判",
   "<strong>第 102 題 Level Order Traversal</strong> —— BFS 的骨架",
   "<strong>第 112 題 Path Sum</strong> —— 同樣要小心「葉節點」的定義",
   "<strong>第 513 題 Find Bottom Left Tree Value</strong> —— BFS 的另一個變形",
 ],
 "check": [
   "為什麼直接把第 104 題的 <code>max</code> 換成 <code>min</code> 是錯的？請舉出反例。",
   "空子樹的 base case 應該回傳什麼才「統一」？為什麼？",
   "為什麼 BFS 在這題完勝遞迴，在第 104 題卻沒有優勢？",
   "「只寫是葉節點就回 1」為什麼還是不夠？",
 ],
})
print("P111 written")

# ==================== 112. Path Sum ====================
S["p112_rec"] = '''class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False                    # 空樹沒有任何「根到葉」的路徑

        # 走到葉節點：看剩下的目標是不是剛好等於它的值
        if not root.left and not root.right:
            return targetSum == root.val

        rest = targetSum - root.val
        return (self.hasPathSum(root.left, rest) or
                self.hasPathSum(root.right, rest))'''

S["p112_iter"] = '''class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        stack = [(root, targetSum - root.val)]   # (節點, 走到這裡還差多少)
        while stack:
            node, rest = stack.pop()
            if not node.left and not node.right and rest == 0:
                return True
            if node.left:
                stack.append((node.left, rest - node.left.val))
            if node.right:
                stack.append((node.right, rest - node.right.val))

        return False'''

S["p112_wrong"] = '''class Solution:
    # 【這是錯的，不要抄】
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return targetSum == 0           # ← 問題就在這一行
        rest = targetSum - root.val
        return (self.hasPathSum(root.left, rest) or
                self.hasPathSum(root.right, rest))'''


def _p112_ref(root, target):
    """獨立參考解：列出所有根到葉的路徑和。"""
    if root is None:
        return False
    sums = []
    def go(nd, acc):
        acc += nd.val
        if not nd.left and not nd.right:
            sums.append(acc)
            return
        if nd.left:
            go(nd.left, acc)
        if nd.right:
            go(nd.right, acc)
    go(root, 0)
    return target in sums


_p112 = [S.load(k) for k in ("p112_rec", "p112_iter")]
_p112_bad = S.load("p112_wrong")

for spec, tgt, want in [
    ([5, [4, [11, [7, None, None], [2, None, None]], None],
         [8, [13, None, None], [4, None, [1, None, None]]]], 22, True),
    ([1, [2, None, None], [3, None, None]], 5, False),
    (None, 0, False),
    ([1, None, None], 1, True),
    ([1, [2, None, None], None], 1, False),
    ([-2, None, [-3, None, None]], -5, True),
]:
    t = _build(spec)
    assert _p112_ref(t, tgt) is want, ("P112 ref", spec, tgt)
    for sol in _p112:
        assert sol.hasPathSum(_build(spec), tgt) is want, ("P112", spec, tgt, sol)

# 錯誤寫法在「單邊為空」時答錯
_bad = _build([1, [2, None, None], None])
assert _p112_bad.hasPathSum(_bad, 1) is True and _p112_ref(_bad, 1) is False, "P112 wrong-demo"

for _ in range(5000):
    t = _rand_tree(random.randrange(0, 11), -4, 4)
    for tgt in range(-8, 9):
        want = _p112_ref(t, tgt)
        for sol in _p112:
            assert sol.hasPathSum(t, tgt) is want, ("P112 random", tgt, want, sol)
    if random.random() < 0.02:
        pass
print("P112 solutions OK")

emit({
 "num": 112, "slug": "path-sum",
 "en": [
   "Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return "
   "<code>true</code> <em>if the tree has a <strong>root-to-leaf</strong> path such that adding "
   "up all the values along the path equals</em> <code>targetSum</code>.",
   "A <strong>leaf</strong> is a node with no children.",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code> 和一個整數 <code>targetSum</code>。",
   "判斷樹裡有沒有一條<strong>從根到葉</strong>的路徑，"
   "使得路徑上所有節點的值<strong>加起來剛好等於</strong> <code>targetSum</code>。",
   "<strong>葉節點</strong>是指沒有任何孩子的節點。",
 ],
 "pre": [
   ("note", "★ 兩個關鍵字：「根到葉」和「葉」", [
     ("c", """【必須從根開始、必須在葉結束。】

    不是「任意一段路徑」（那是第 437 題）。
    不是「走到一半就停」。

【最常見的錯誤寫法】：

    if not root:
        return targetSum == 0

    看起來很自然：「走到底了，看剩下的是不是 0」。

    但「走到 None」不等於「走到葉節點」！

    反例：

        1          targetSum = 1
       /
      2

        f(1, 1)
          rest = 1 - 1 = 0
          -> f(2, 0)  or  f(None, 0)
                          ^^^^^^^^^^
                          這個回傳 True ✘

        因為 root.right 是 None，
        而 targetSum 剛好是 0 -> 誤判成找到了。

    但根節點 1 【不是葉節點】，
    所以「只走到 1」不是一條合法的路徑 -> 應該是 False。

【正確的 base case 是「走到葉節點」，不是「走到 None」。】

    if not root.left and not root.right:
        return targetSum == root.val

    這和第 111 題的「不能直接取 min」是同一類錯誤 ——
    都源自「把 None 當成合法的終點」。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22

              5
             / \\
            4   8
           /   / \\
          11  13  4
         /  \\      \\
        7    2      1

  輸出：true
  說明：5 -> 4 -> 11 -> 2 = 22 ✔

範例 2
  輸入：root = [1,2,3], targetSum = 5
  輸出：false
  說明：兩條路徑分別是 1+2=3 和 1+3=4，都不是 5。

範例 3
  輸入：root = [], targetSum = 0
  輸出：false
  說明：空樹【沒有任何路徑】，所以連 0 都湊不出來。""",
 "constraints": [
   "樹的節點數在 <code>[0, 5000]</code> 之間",
   "−1000 ≤ <code>Node.val</code> ≤ 1000",
   "−1000 ≤ <code>targetSum</code> ≤ 1000",
 ],
 "mid": [
   ("note", "注意：節點值可以是負數", [
     "<strong>所以「目前的和已經超過 <code>targetSum</code> 就剪枝」是錯的</strong> —— "
     "後面可能有負數把它拉回來。",
     "<strong>只有在「保證所有值都是正數」時，剪枝才安全。</strong>"
     "<strong>面試時一定要先問這個。</strong>",
     "範例：<code>[-2,null,-3]</code>、<code>targetSum = -5</code> → <code>True</code>。",
   ]),
 ],
 "idea": [
   ("c", """遞迴時「把目標往下減」，比「把和往下累加」乾淨：

    f(node, remaining)：
        「從 node 出發，有沒有一條到葉的路徑，和剛好是 remaining？」

    if not node:
        return False                          空樹沒有路徑

    if 是葉節點:
        return remaining == node.val          剛好用完 ✔

    rest = remaining - node.val
    return f(node.left, rest) or f(node.right, rest)

【為什麼「減目標」比「加總和」好？】

    加總和的話，遞迴要多帶一個參數：
        f(node, acc, target)

    減目標只要一個：
        f(node, remaining)

    而且 base case 更自然（remaining == node.val 就是剛好）。

    【「把目標往下傳遞並遞減」是回溯 / DFS 的常見手法】——
    第 39 題（組合總和）、第 494 題（目標和）用的都是它。

【三個 base case 的順序】：
    1. not node          -> False      （空子樹不是路徑）
    2. 是葉節點           -> 比對
    3. 其他               -> 遞迴

    順序不能換：先檢查 None，才能安全地存取 node.left。"""),
 ],
 "approaches": [
   ap("解法一", "遞迴（標準答案）", [
     ("c", S["p112_rec"]),
     "<strong>六行。<code>or</code> 會短路，所以找到一條就不會再找了。</strong>",
     ("h", "為什麼空樹要回 <code>False</code> 而不是 <code>targetSum == 0</code>？"),
     ("c", """「空樹」和「走到 None」是兩個不同的狀況，
但在這個遞迴裡它們共用同一行程式碼。

    空樹（最外層呼叫）：沒有任何根到葉的路徑 -> False ✔
    走到 None（某個孩子不存在）：此路不通    -> False ✔

    兩者都應該是 False，所以可以共用 ✔

    而寫成 targetSum == 0 的話：
        空樹 + targetSum = 0 -> 誤判 True ✘
        單邊為空 -> 誤判 True ✘

【「此路不通」的正確回傳值，
  在「求存在性」的問題裡永遠是 False（or 的單位元素）。】

    對照第 111 題：那裡「此路不通」應該回 +∞（min 的單位元素）。

    又是同一個「base case 要填對單位元素」的原則。""",),
     ("h", "為什麼葉節點的判斷是 <code>targetSum == root.val</code>？"),
     "因為 <code>targetSum</code> 是「<strong>走到這個節點之前</strong>還差多少」，"
     "而葉節點是最後一個 —— 所以它的值必須<strong>剛好把差額補完</strong>。",
     "<strong>寫成 <code>targetSum - root.val == 0</code> 完全一樣</strong>，"
     "只是前者少一次運算。",
   ], "O(n)", "O(h)", "最壞走完整棵樹", "遞迴堆疊", optimal=True),

   ap("解法二", "迭代 + 堆疊（把剩餘量打包進去）", [
     ("c", S["p112_iter"]),
     ("h", "和遞迴版的對應關係"),
     ("c", """遞迴： f(node.left, rest)
迭代： stack.append((node.left, rest - node.left.val))

    注意迭代版的 rest 語意稍有不同：
        遞迴版：「走到這個節點【之前】還差多少」
        迭代版：「走過這個節點【之後】還差多少」

    所以迭代版的葉節點判斷是 rest == 0，
    而遞迴版是 rest == node.val。

    兩種寫法都對，但【不要混用】——
    混用就會差一個 node.val，答案全錯。

【這是「遞迴改迭代」時最容易出錯的地方】：
    狀態的「時間點」要定義清楚，並且全程一致。

    建議在註解裡寫明白：
        # (節點, 走到這裡【之後】還差多少)"""),
     "<strong>沒有遞迴深度問題</strong>（5000 個節點的鏈狀樹會讓遞迴版爆掉）。",
     "<strong>用 <code>pop()</code>（DFS）還是 <code>popleft()</code>（BFS）都可以</strong> —— "
     "<strong>我們只要「存不存在」，順序不影響答案。</strong>"
     "但<strong>如果答案通常在淺處，BFS 會比較快找到。</strong>",
   ], "O(n)", "O(h)", "每個節點一次", "顯式堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、遞迴", "O(n)", "O(h)", "6", "標準答案"],
    ["二、堆疊迭代", "O(n)", "O(h)", "12", "避免遞迴深度問題"]]),
 "edges": [
   "<strong><code>root = None</code>, <code>targetSum = 0</code></strong> → "
   "<strong><code>False</code></strong>（空樹沒有任何路徑）。"
   "<strong>這是最容易錯的測資。</strong>",
   "<strong><code>[1]</code>, <code>targetSum = 1</code></strong> → <code>True</code>。",
   "<strong><code>[1,2]</code>, <code>targetSum = 1</code></strong> → "
   "<strong><code>False</code></strong>。"
   "<strong>根不是葉節點 —— 寫錯 base case 會答 True。</strong>",
   "<strong><code>[-2,null,-3]</code>, <code>targetSum = -5</code></strong> → <code>True</code>。"
   "<strong>負數：不能用「超過就剪枝」。</strong>",
   "<strong>所有值都是 0，<code>targetSum = 0</code></strong> → <code>True</code>（任何路徑都行）。",
   "<strong>把 base case 寫成 <code>if not root: return targetSum == 0</code></strong> → "
   "<strong>本題第一名的 bug。</strong>",
   "<strong>5000 個節點的鏈狀樹</strong> → 遞迴版可能 <code>RecursionError</code>。",
 ],
 "follow": [
   ("h", "追問一：如果要回傳「所有」符合的路徑呢？"),
   "<strong>第 113 題</strong>。要改用<strong>回溯</strong>：一路把節點 <code>append</code> 進 "
   "<code>path</code>，到葉節點時<strong>複製一份</strong>存起來，回溯時 <code>pop()</code>。",
   "<strong>「複製一份」是關鍵</strong>（<code>res.append(path[:])</code>）—— "
   "<strong>直接 <code>res.append(path)</code> 的話，"
   "所有答案都會指向同一個 list，最後全變成空的。</strong>",
   ("h", "追問二：如果路徑不必從根開始、也不必在葉結束呢？"),
   "<strong>第 437 題（Path Sum III）</strong>。"
   "那題要用<strong>「前綴和 + 雜湊表」</strong>，"
   "和第 560 題（和為 k 的子陣列）是同一招，只是搬到樹上。",
   ("c", """核心：走訪時維護「從根到目前節點」的前綴和 acc，
並用一個 counter 記錄「路上出現過哪些前綴和」。

    acc - target 在 counter 裡出現幾次，
    就代表有幾條「以目前節點結尾」的路徑符合。

    【重點：回溯時要把自己的前綴和從 counter 拿掉】——
    否則會算到「不在同一條路徑上」的節點。

    這是本題往上一個難度級距的版本。""",),
   ("h", "追問三：什麼時候可以剪枝？"),
   ("c", """【所有值都是正數】時可以：

    if remaining < 0:
        return False          # 已經超過了，後面只會更大

    這能省下大量搜尋。

【有負數時絕對不行】：

        10
       /
     -20
       \\
        12

    targetSum = 2：
        走到 10 時 remaining = -8（已經「超過」）
        但繼續走 -20 -> remaining = 12
        再走 12 -> remaining = 0 ✔ 找到了

    提早剪枝就會漏掉這條路徑。

【面試時一定要問：「節點值可以是負數嗎？」】
    這個問題本身就會加分 ——
    它顯示你在思考演算法的前提，而不只是套模板。"""),
   ("h", "追問四：如果要「路徑積」等於某個值呢？"),
   "<strong>把減法換成除法，但要小心 <code>0</code></strong> —— "
   "<strong>路徑上有 0 的話，積永遠是 0，而且不能做除法。</strong>",
   "<strong>更安全的做法是「往下累乘」而不是「往下累除」</strong>："
   "傳 <code>acc * node.val</code>，到葉節點時比對 <code>acc == target</code>。",
   "<strong>「累加 / 累乘」比「遞減 / 遞除」通用</strong> —— "
   "<strong>當運算沒有反元素（除法遇到 0、位元 AND 等）時，只能用前者。</strong>",
 ],
 "related": [
   "<strong>第 113 題 Path Sum II</strong> —— 回傳所有路徑（回溯）",
   "<strong>第 437 題 Path Sum III</strong> —— 任意起訖點（前綴和 + 雜湊表）",
   "<strong>第 129 題 Sum Root to Leaf Numbers</strong> —— 把路徑當成數字",
   "<strong>第 111 題 Minimum Depth</strong> —— 同樣要小心「葉節點 ≠ None」",
   "<strong>第 124 題 Maximum Path Sum</strong> —— 路徑可以拐彎的版本",
 ],
 "check": [
   "為什麼 base case 不能寫成 <code>if not root: return targetSum == 0</code>？請舉出反例。",
   "「走到 None」和「走到葉節點」有什麼不同？為什麼這個區別這麼重要？",
   "節點值有負數時，為什麼不能用「和已經超過就剪枝」？",
   "迭代版裡 <code>rest</code> 的語意和遞迴版差在哪裡？混用會怎樣？",
 ],
})
print("P112 written")
