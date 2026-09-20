# -*- coding: utf-8 -*-
"""第 105–108 題。"""
import random
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(105)


def _build(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _build(l), _build(r))


def _rand_tree_distinct(vals):
    """用互不相同的值蓋一棵隨機形狀的樹。"""
    if not vals:
        return None
    k = random.randrange(len(vals))
    rest = vals[:k] + vals[k + 1:]
    m = random.randrange(len(rest) + 1)
    return TreeNode(vals[k], _rand_tree_distinct(rest[:m]), _rand_tree_distinct(rest[m:]))


def _pre(nd):
    return [] if nd is None else [nd.val] + _pre(nd.left) + _pre(nd.right)


def _ino(nd):
    return [] if nd is None else _ino(nd.left) + [nd.val] + _ino(nd.right)


def _post(nd):
    return [] if nd is None else _post(nd.left) + _post(nd.right) + [nd.val]


def _enc(nd):
    return None if nd is None else (_enc(nd.left), nd.val, _enc(nd.right))


# ==================== 105. Construct from Preorder and Inorder ====================
S["p105_hash"] = '''class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 中序裡「值 -> 索引」，用來 O(1) 找到根的位置
        pos = {v: i for i, v in enumerate(inorder)}
        self.i = 0                          # 前序目前讀到哪裡

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            """用 inorder[lo..hi] 這一段建子樹"""
            if lo > hi:
                return None

            root_val = preorder[self.i]     # 前序的下一個就是這棵子樹的根
            self.i += 1
            mid = pos[root_val]             # 它在中序裡的位置

            node = TreeNode(root_val)
            node.left = build(lo, mid - 1)  # 【一定要先建左】：前序是 根→左→右
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(inorder) - 1)'''

S["p105_slice"] = '''class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]              # 前序第一個就是根
        k = inorder.index(root_val)         # 它在中序裡的位置 -> 左子樹有 k 個節點

        return TreeNode(
            root_val,
            self.buildTree(preorder[1:k + 1], inorder[:k]),      # 左
            self.buildTree(preorder[k + 1:], inorder[k + 1:]),   # 右
        )'''

S["p105_stack"] = '''class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        j = 0                               # 中序目前要對上的位置

        for val in preorder[1:]:
            node = stack[-1]
            if node.val != inorder[j]:
                # 還沒走完左邊 -> 新節點是堆疊頂的左孩子
                node.left = TreeNode(val)
                stack.append(node.left)
            else:
                # 堆疊頂的左子樹走完了，一路往上彈到該轉右的節點
                while stack and stack[-1].val == inorder[j]:
                    node = stack.pop()
                    j += 1
                node.right = TreeNode(val)
                stack.append(node.right)

        return root'''


_p105 = [S.load(k) for k in ("p105_hash", "p105_slice", "p105_stack")]

for _ in range(2500):
    n = random.randrange(0, 11)
    vals = random.sample(range(-50, 50), n)
    t = _rand_tree_distinct(vals)
    pre, ino = _pre(t), _ino(t)
    for sol in _p105:
        got = sol.buildTree(list(pre), list(ino))
        assert _enc(got) == _enc(t), ("P105", pre, ino, sol)
# 官方範例
_t = _p105[0].buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
assert _pre(_t) == [3, 9, 20, 15, 7] and _ino(_t) == [9, 3, 15, 20, 7]
print("P105 solutions OK")

_P105_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">前序負責「找根」，中序負責「分邊」。兩條序列各出一半力，才能唯一決定一棵樹。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">preorder = [3, 9, 20, 15, 7]　　inorder = [9, 3, 15, 20, 7]</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="70" width="46" height="28" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="63" y="89" fill="var(--gold)">3</text>
              <rect x="94" y="70" width="46" height="28" fill="none" stroke="var(--accent)"/><text x="117" y="89" fill="var(--accent)">9</text>
              <rect x="148" y="70" width="46" height="28" fill="none" stroke="#ff8a65"/><text x="171" y="89" fill="#ff8a65">20</text>
              <rect x="202" y="70" width="46" height="28" fill="none" stroke="#ff8a65"/><text x="225" y="89" fill="#ff8a65">15</text>
              <rect x="256" y="70" width="46" height="28" fill="none" stroke="#ff8a65"/><text x="279" y="89" fill="#ff8a65">7</text>
              <text x="330" y="89" fill="var(--text-muted)" text-anchor="start" font-size="11">前序：第一個一定是根</text>
            </g>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="116" width="46" height="28" fill="none" stroke="var(--accent)"/><text x="63" y="135" fill="var(--accent)">9</text>
              <rect x="94" y="116" width="46" height="28" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="117" y="135" fill="var(--gold)">3</text>
              <rect x="148" y="116" width="46" height="28" fill="none" stroke="#ff8a65"/><text x="171" y="135" fill="#ff8a65">15</text>
              <rect x="202" y="116" width="46" height="28" fill="none" stroke="#ff8a65"/><text x="225" y="135" fill="#ff8a65">20</text>
              <rect x="256" y="116" width="46" height="28" fill="none" stroke="#ff8a65"/><text x="279" y="135" fill="#ff8a65">7</text>
              <text x="330" y="135" fill="var(--text-muted)" text-anchor="start" font-size="11">中序：根把左右切開</text>
            </g>
            <text x="63" y="164" fill="var(--accent)" font-size="11" text-anchor="middle">左子樹</text>
            <text x="225" y="164" fill="#ff8a65" font-size="11" text-anchor="middle">右子樹</text>
            <text x="20" y="194" fill="var(--gold)" font-size="12">根是 3 → 中序裡 3 的左邊有 1 個 → 左子樹 1 個節點，右子樹 3 個節點</text>
            <text x="20" y="218" fill="var(--text-muted)" font-size="12">前序切成： [3] [9] [20, 15, 7]　　中序切成： [9] [3] [15, 20, 7]　　然後各自遞迴</text>
            <line x1="20" y1="240" x2="620" y2="240" stroke="var(--border)"/>
            <g font-size="13" text-anchor="middle">
              <circle cx="320" cy="278" r="18" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="320" y="283" fill="var(--gold)">3</text>
              <circle cx="240" cy="336" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="240" y="341" fill="var(--accent)">9</text>
              <circle cx="400" cy="336" r="18" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="400" y="341" fill="#ff8a65">20</text>
              <circle cx="352" cy="394" r="18" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="352" y="399" fill="#ff8a65">15</text>
              <circle cx="448" cy="394" r="18" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="448" y="399" fill="#ff8a65">7</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="307" y1="291" x2="253" y2="323"/><line x1="333" y1="291" x2="387" y2="323"/>
              <line x1="388" y1="349" x2="364" y2="381"/><line x1="412" y1="349" x2="436" y2="381"/>
            </g>
            <text x="20" y="428" fill="#ff8a65" font-size="12">為什麼一定要兩條序列？只給前序 [3,9,20,15,7]，9 可以掛左邊也可以掛右邊 —— 不唯一。</text>'''

emit({
 "num": 105, "slug": "construct-binary-tree-from-preorder-and-inorder-traversal",
 "en": [
   "Given two integer arrays <code>preorder</code> and <code>inorder</code> where "
   "<code>preorder</code> is the preorder traversal of a binary tree and <code>inorder</code> "
   "is the inorder traversal of the same tree, <em>construct and return the binary tree</em>.",
 ],
 "zh": [
   "給你兩個整數陣列 <code>preorder</code> 和 <code>inorder</code>，"
   "分別是同一棵二元樹的<strong>前序走訪</strong>和<strong>中序走訪</strong>結果。",
   "請把這棵樹<strong>還原出來</strong>。",
 ],
 "pre": [
   ("note", "為什麼需要「兩條」序列？", [
     ("c", """單獨一條走訪序列【無法唯一決定一棵樹】。

    只給前序 [1, 2]：

        1          1
       /            \\
      2              2

    兩棵都符合，分不出來。

【前序告訴你「誰是根」，但沒告訴你「左右怎麼分」。】
【中序告訴你「左右怎麼分」，但沒告訴你「誰是根」。】

    兩個湊起來，資訊就夠了 ✔

    這也是為什麼「前序 + 後序」【不能】唯一決定一棵樹：
        兩者都不提供「左右分界」的資訊。

        前序 [1,2]、後序 [2,1]
        -> 2 可以是左孩子也可以是右孩子

        （除非保證每個節點都有 0 或 2 個孩子 ——
          那就是第 889 題。）

【重要前提：本題保證所有值互不相同。】
    有重複值的話，「在中序裡找根的位置」就會有歧義。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
  輸出：[3,9,20,null,null,15,7]

            3
           / \\
          9   20
             /  \\
            15   7

範例 2
  輸入：preorder = [-1], inorder = [-1]
  輸出：[-1]""",
 "constraints": [
   "1 ≤ <code>preorder.length</code> ≤ 3000",
   "<code>inorder.length == preorder.length</code>",
   "−3000 ≤ <code>preorder[i]</code>, <code>inorder[i]</code> ≤ 3000",
   "<code>preorder</code> 和 <code>inorder</code> 都<strong>沒有重複值</strong>",
   "<code>inorder</code> 是 <code>preorder</code> 的一個排列",
   "<code>preorder</code> 保證是某棵二元樹的前序走訪",
   "<code>inorder</code> 保證是<strong>同一棵樹</strong>的中序走訪",
 ],
 "idea": [
   ("fig", _P105_FIG, "0 0 640 446"),
   ("c", """核心分工：

    前序（根 → 左 → 右）：【第一個元素一定是根】
    中序（左 → 根 → 右）：【根把序列切成左右兩半】

演算法：
    1. 取 preorder[0] 當根
    2. 在 inorder 裡找到它的位置 k
    3. inorder[:k]   是左子樹的中序      -> 左子樹有 k 個節點
       inorder[k+1:] 是右子樹的中序
    4. 既然知道左子樹有 k 個節點，
       preorder[1:k+1] 就是左子樹的前序，
       preorder[k+1:]  是右子樹的前序
    5. 遞迴

【第 4 步是關鍵】：
    前序裡「左子樹的那一段」和「右子樹的那一段」
    是靠【中序算出來的節點個數】切開的。

    這就是兩條序列「互相幫忙」的地方。"""),
 ],
 "approaches": [
   ap("解法一", "遞迴 + 切片（最好懂，但慢）", [
     ("c", S["p105_slice"]),
     "<strong>七行，幾乎就是上面那段文字的直譯。</strong>"
     "<strong>面試時先寫這個版本，說清楚思路，再優化。</strong>",
     ("h", "為什麼是 <code>preorder[1:k+1]</code>？"),
     ("c", """k = 左子樹的節點個數（從中序算出來的）

    preorder = [根] [左子樹的前序(k 個)] [右子樹的前序]
                0    1 .. k               k+1 ..

    所以左子樹的前序是 preorder[1 : 1+k] = preorder[1 : k+1] ✔

    【最容易寫錯的地方就是這個切片邊界。】
    寫錯的話會得到一棵結構怪異但不會 crash 的樹 ——
    很難 debug。

    驗證方法：
        len(preorder[1:k+1]) 應該等於 len(inorder[:k]) = k ✔
        兩邊長度對不上就是切錯了。"""),
     ("h", "為什麼這個版本慢？"),
     ("c", """兩個 O(n) 的操作藏在每一層遞迴裡：

    1. inorder.index(root_val)   -> O(n) 線性搜尋
    2. preorder[1:k+1] 等切片     -> O(k) 複製

    最壞情況（樹退化成一條鏈）：
        T(n) = T(n-1) + O(n)  ->  O(n²)

        n = 3000 -> 900 萬次操作，勉強能過。

    最好情況（平衡樹）：
        T(n) = 2T(n/2) + O(n)  ->  O(n log n)

【所以它「能過」，但不是好答案。】
    面試官一定會問「能不能更快」——
    答案是解法二。"""),
   ], "O(n²) 最壞", "O(n²) 最壞", "index + 切片都是 O(n)", "切片的副本"),

   ap("解法二", "雜湊表 + 索引區間（標準答案，O(n)）", [
     ("c", S["p105_hash"]),
     ("h", "兩個優化，各解決一個 O(n)"),
     ("c", """【優化一：用雜湊表取代 index()】

    pos = {v: i for i, v in enumerate(inorder)}

    一次 O(n) 建表，之後每次查根的位置都是 O(1)。
    （這裡用到「值互不相同」這個前提 ✔）

【優化二：用索引區間取代切片】

    不要真的去切 list，而是傳「這段的左右邊界」。

        build(lo, hi)  代表 inorder[lo..hi]

    完全不複製資料 -> 每層 O(1)。

兩個優化加起來：
    每個節點只做 O(1) 的工作 -> 總共 O(n) ✔

【這組合（雜湊表查位置 + 索引區間代替切片）
  是「把分治從 O(n²) 降到 O(n)」的標準套路。】

    第 106、108、109、889 題用的都是它。""",),
     ("h", "為什麼 <code>self.i</code> 不用傳、也不用回溯？"),
     ("c", """self.i 是「前序讀到哪裡」的全域游標。

    它【只會往前走，永遠不回頭】——
    因為前序走訪的順序（根→左→右）
    和我們建樹的順序完全一致。

    所以不需要為每棵子樹計算「你的前序是從哪裡開始」，
    只要「照順序拿下一個」就好。

【這是本題最漂亮的觀察，也是最容易被忽略的一點。】

    很多人會寫成 build(pre_lo, pre_hi, in_lo, in_hi) 四個參數 ——
    那也對，但其實 pre_lo 完全可以用一個游標取代。"""),
     ("h", "★ <code>node.left</code> 一定要在 <code>node.right</code> 之前"),
     ("c", """node.left  = build(lo, mid - 1)
node.right = build(mid + 1, hi)

    【兩行對調就會得到完全錯誤的樹。】

    因為 self.i 是共用的游標：
        前序的順序是 根 → 左子樹全部 → 右子樹全部

        必須先把左子樹「消耗完」，
        游標才會指到右子樹的第一個元素。

    如果先建右子樹，就會拿左子樹的資料去建右子樹 ✘

    【在 Python 裡尤其危險】：

        return TreeNode(v, build(lo, mid-1), build(mid+1, hi))

        參數求值順序是由左到右，所以這樣寫【是對的】。
        但在某些語言（例如舊版 C++）參數求值順序未定義 ——
        分成兩行寫最安全。

    這個「共用游標 + 求值順序」的坑，
    在第 106 題（後序版）會以鏡像的形式再出現一次。"""),
   ], "O(n)", "O(n)", "每個節點 O(1)", "雜湊表 + 遞迴堆疊", optimal=True),

   ap("解法三", "迭代 + 堆疊（不用遞迴，但很難想）", [
     ("c", S["p105_stack"]),
     ("h", "這個解法在做什麼"),
     ("c", """核心想法：模擬「前序走訪的過程」。

    堆疊裡放的是「目前這條從根往下的路徑」。

    對前序的每一個新元素 val：

    情況 A： stack[-1].val != inorder[j]
        代表堆疊頂的節點【還沒把左子樹走完】
        -> val 是它的左孩子

    情況 B： stack[-1].val == inorder[j]
        代表堆疊頂就是中序裡「下一個該輸出的節點」
        -> 它的左子樹走完了
        -> 一路往上彈，直到找到「該轉右」的那個節點
        -> val 是那個節點的右孩子

【為什麼 inorder[j] 能判斷「左子樹走完了」？】

    中序的順序是 左 → 根 → 右。
    所以當中序游標指到某個節點時，
    就代表它的左子樹已經全部輸出完畢。

    這其實就是【第 94 題中序迭代走訪的逆運算】——
    那裡是「走樹產生序列」，這裡是「讀序列還原樹」。"""),
     "<strong>O(n) 時間、O(h) 空間，而且沒有遞迴深度問題。</strong>",
     "<strong>但它非常難在面試現場推出來</strong> —— "
     "<strong>寫解法二就好</strong>，這個版本知道「存在」即可。",
   ], "O(n)", "O(h)", "每個節點進出堆疊一次", "顯式堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "好想嗎", "備註"],
   [["一、切片遞迴", "O(n²) 最壞", "O(n²)", "★★★", "先講思路用"],
    ["二、雜湊表 + 索引", "O(n)", "O(n)", "★★☆", "標準答案"],
    ["三、堆疊迭代", "O(n)", "O(h)", "★☆☆", "很難想，知道就好"]]),
 "edges": [
   "<strong>單一節點</strong> <code>preorder=[-1], inorder=[-1]</code> → 一個節點的樹。",
   "<strong>退化成一條左鏈</strong>（<code>pre=[1,2,3]</code>、<code>in=[3,2,1]</code>）→ "
   "切片版變 O(n²)，遞迴深度 3000 會 <code>RecursionError</code>。",
   "<strong>退化成一條右鏈</strong>（<code>pre=[1,2,3]</code>、<code>in=[1,2,3]</code>）→ 同上。",
   "<strong><code>node.left</code> 和 <code>node.right</code> 對調</strong> → "
   "<strong>樹整個錯掉，而且不會報錯 —— 本題最難 debug 的 bug。</strong>",
   "<strong>切片寫成 <code>preorder[1:k]</code></strong>（少了 <code>+1</code>）→ "
   "左子樹少一個節點，後面全亂。",
   "<strong>用 <code>inorder.index()</code> 而不建雜湊表</strong> → "
   "鏈狀樹上退化成 O(n²)。",
   "<strong>值有重複</strong>（題目保證不會）→ "
   "<code>pos</code> 只會留下最後一個位置，建出來的樹是錯的。",
 ],
 "follow": [
   ("h", "追問一：如果是「中序 + 後序」呢？"),
   "<strong>第 106 題</strong>。<strong>後序的最後一個是根</strong>，"
   "而且<strong>倒著讀後序就是「根 → 右 → 左」</strong>，"
   "所以<strong>把游標從尾端往前走、並且先建右子樹</strong>即可。",
   ("h", "追問二：「前序 + 後序」可以嗎？"),
   "<strong>一般情況不行</strong>（前面說過原因）。",
   "<strong>但如果保證「每個節點有 0 或 2 個孩子」</strong>（完滿二元樹），"
   "就可以 —— <strong>那是第 889 題</strong>。"
   "此時前序的第二個元素一定是左子樹的根，"
   "在後序裡找到它就知道左子樹有多大。",
   "<strong>更一般地說</strong>：只要能確定「左子樹有幾個節點」，"
   "任意兩條序列就能建樹。<strong>中序之所以萬用，是因為它天然把左右切開。</strong>",
   ("h", "追問三：如果有重複值呢？"),
   "<strong>答案就不唯一了。</strong>",
   ("c", """preorder = [1, 1]
inorder  = [1, 1]

        1          1
       /            \\
      1              1

    兩棵都符合 ——【無法區分】。

    要處理重複值，必須改變輸入格式，例如：
        (a) 額外給「每棵子樹的大小」
        (b) 用帶空節點記號的序列化（第 297 題）
        (c) 給「前序 + 每個節點的深度」

【這也說明了為什麼第 297 題（序列化）
  要用帶 # 的前序，而不是「前序 + 中序」——
  前者對重複值也成立，後者不行。】""",),
   ("h", "追問四：能不能不用遞迴也不用堆疊？"),
   "<strong>可以，但要先把「每棵子樹的區間」算出來</strong>，"
   "本質上還是在手動維護堆疊。",
   "<strong>樹的結構天生是遞迴的</strong>，"
   "<strong>「完全不用任何形式的堆疊」通常意味著 Morris 那種「借用指標」的技巧</strong> —— "
   "但這題是在<strong>建</strong>樹，沒有現成的指標可借，所以做不到。",
 ],
 "related": [
   "<strong>第 106 題 從中序與後序建樹</strong> —— 本題的鏡像版",
   "<strong>第 889 題 從前序與後序建樹</strong> —— 需要「完滿二元樹」的前提",
   "<strong>第 108 題 有序陣列轉 BST</strong> —— 另一種「分治建樹」",
   "<strong>第 297 題 序列化與反序列化</strong> —— 為什麼帶空節點的前序更通用",
   "<strong>第 94 題 中序走訪</strong> —— 解法三是它的逆運算",
 ],
 "check": [
   "為什麼單獨一條前序序列無法唯一決定一棵樹？請舉例。",
   "解法二裡 <code>self.i</code> 為什麼不需要回溯？",
   "<code>node.left</code> 和 <code>node.right</code> 兩行對調會發生什麼？為什麼？",
   "切片版在什麼形狀的樹上會退化成 O(n²)？",
   "如果值有重複，這題還有唯一解嗎？",
 ],
})
print("P105 written")

# ==================== 106. Construct from Inorder and Postorder ====================
S["p106_hash"] = '''class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}
        self.i = len(postorder) - 1         # 後序【從尾端】往回讀

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None

            root_val = postorder[self.i]    # 後序倒著讀，下一個就是根
            self.i -= 1
            mid = pos[root_val]

            node = TreeNode(root_val)
            node.right = build(mid + 1, hi) # 【一定要先建右】：倒讀後序是 根→右→左
            node.left = build(lo, mid - 1)
            return node

        return build(0, len(inorder) - 1)'''

S["p106_slice"] = '''class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root_val = postorder[-1]            # 後序最後一個是根
        k = inorder.index(root_val)

        return TreeNode(
            root_val,
            self.buildTree(inorder[:k], postorder[:k]),          # 左子樹有 k 個
            self.buildTree(inorder[k + 1:], postorder[k:-1]),    # 右子樹（去掉最後的根）
        )'''

S["p106_pop"] = '''class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}

        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            root_val = postorder.pop()      # 直接從尾端 pop，等同倒著讀
            mid = pos[root_val]
            node = TreeNode(root_val)
            node.right = build(mid + 1, hi) # 先右後左
            node.left = build(lo, mid - 1)
            return node

        return build(0, len(inorder) - 1)'''


_p106 = [S.load(k) for k in ("p106_hash", "p106_slice", "p106_pop")]

for _ in range(2500):
    n = random.randrange(0, 11)
    vals = random.sample(range(-50, 50), n)
    t = _rand_tree_distinct(vals)
    ino, post = _ino(t), _post(t)
    for sol in _p106:
        got = sol.buildTree(list(ino), list(post))
        assert _enc(got) == _enc(t), ("P106", ino, post, sol)
_t = _p106[0].buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
assert _pre(_t) == [3, 9, 20, 15, 7], _pre(_t)
print("P106 solutions OK")

emit({
 "num": 106, "slug": "construct-binary-tree-from-inorder-and-postorder-traversal",
 "en": [
   "Given two integer arrays <code>inorder</code> and <code>postorder</code> where "
   "<code>inorder</code> is the inorder traversal of a binary tree and <code>postorder</code> "
   "is the postorder traversal of the same tree, <em>construct and return the binary tree</em>.",
 ],
 "zh": [
   "給你兩個整數陣列 <code>inorder</code> 和 <code>postorder</code>，"
   "分別是同一棵二元樹的<strong>中序走訪</strong>和<strong>後序走訪</strong>結果。",
   "請把這棵樹<strong>還原出來</strong>。",
 ],
 "pre": [
   ("note", "第 105 題的鏡像版：兩個地方要反過來", [
     ("c", """前序： 根 → 左 → 右     -> 【第一個】是根，游標【往前】走
後序： 左 → 右 → 根     -> 【最後一個】是根，游標【往後】走

把後序【倒過來讀】：

    reversed(後序) = 根 → 右 → 左

    對照 前序 = 根 → 左 → 右

    【完全對稱！只是左右對調。】

所以第 105 題的程式碼只要改兩個地方：

    1. self.i 從 len - 1 開始，每次 -= 1（而不是 0 開始 += 1）
    2. 先建 right 再建 left（而不是先 left 後 right）

    其餘一模一樣。

【如果你已經懂第 105 題，這題只要五秒鐘。
  如果你覺得這題很難，代表第 105 題還沒真的懂。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
  輸出：[3,9,20,null,null,15,7]

            3
           / \\
          9   20
             /  \\
            15   7

  驗算：後序（左右根）= 9, 15, 7, 20, 3 ✔
        最後一個 3 就是根。

範例 2
  輸入：inorder = [-1], postorder = [-1]
  輸出：[-1]""",
 "constraints": [
   "1 ≤ <code>inorder.length</code> ≤ 3000",
   "<code>postorder.length == inorder.length</code>",
   "−3000 ≤ <code>inorder[i]</code>, <code>postorder[i]</code> ≤ 3000",
   "<code>inorder</code> 和 <code>postorder</code> 都<strong>沒有重複值</strong>",
   "<code>postorder</code> 保證是某棵二元樹的後序走訪",
   "<code>inorder</code> 保證是<strong>同一棵樹</strong>的中序走訪",
 ],
 "idea": [
   ("c", """對照表（把第 105 題放在旁邊看）：

                     第 105 題（前序+中序）      第 106 題（中序+後序）
    根在哪            preorder[0]                postorder[-1]
    游標起點          0                          len - 1
    游標方向          += 1                       -= 1
    先建哪一邊        left                       right
    中序的用途        找根的位置、分左右          完全相同

【為什麼一定要先建右子樹？】

    倒著讀後序，順序是 根 → 右 → 左。

    游標從尾端往前走時：
        第一個拿到的是根
        接下來一整段是【右子樹】（倒序的）
        再接下來是【左子樹】

    所以必須先把右子樹消耗完，
    游標才會指到左子樹 ✔

    寫反的話（先 left 後 right），
    會拿右子樹的資料去建左子樹 ——
    【樹整個錯掉，而且不會報錯。】"""),
 ],
 "approaches": [
   ap("解法一", "遞迴 + 切片（先講思路）", [
     ("c", S["p106_slice"]),
     ("h", "切片邊界比第 105 題更容易寫錯"),
     ("c", """postorder = [左子樹的後序(k 個)] [右子樹的後序] [根]
             0 .. k-1            k .. n-2      n-1

    左子樹： postorder[:k]        ✔
    右子樹： postorder[k:-1]      ✔  （注意 -1 是要去掉最後那個根）

【最常見的錯誤】：寫成 postorder[k:]
    那樣右子樹會多吃到根，長度對不上。

    驗證方法（養成習慣）：
        len(postorder[:k])   應該 == len(inorder[:k])   = k     ✔
        len(postorder[k:-1]) 應該 == len(inorder[k+1:]) = n-k-1 ✔

    兩邊長度對不上，就是切錯了。"""),
     "<strong>最壞 O(n²)</strong>（<code>index()</code> 和切片）。"
     "<strong>思路清楚，但要準備好被問「怎麼變快」。</strong>",
   ], "O(n²) 最壞", "O(n²) 最壞", "index + 切片", "切片的副本"),

   ap("解法二", "雜湊表 + 索引區間（標準答案）", [
     ("c", S["p106_hash"]),
     "<strong>和第 105 題的解法二逐行對照，只有兩處不同</strong>"
     "（游標方向、左右順序）—— <strong>上面的對照表就是全部。</strong>",
     ("h", "為什麼 <code>pos</code> 建在 <code>inorder</code> 上而不是 <code>postorder</code>？"),
     "因為<strong>我們要找的是「根在中序裡的位置」</strong> —— "
     "那才是能把左右切開的資訊。"
     "<strong>後序只負責「按順序吐出根」，不需要查位置。</strong>",
     "<strong>O(n) 時間、O(n) 空間。</strong>"
     "<strong>每個節點只做 O(1) 的工作。</strong>",
   ], "O(n)", "O(n)", "每個節點 O(1)", "雜湊表 + 遞迴堆疊", optimal=True),

   ap("解法三", "直接 <code>postorder.pop()</code>（最短）", [
     ("c", S["p106_pop"]),
     ("h", "用 <code>pop()</code> 取代手動游標"),
     ("c", """postorder.pop()  從尾端拿掉並回傳最後一個元素 —— O(1)

    這正好就是「倒著讀後序」的意思，
    連 self.i 都不用維護。

    比較：
        第 105 題（前序）：不能用 pop(0) —— 那是 O(n)！
                           所以必須用游標。
        第 106 題（後序）：可以用 pop() —— O(1) ✔

    【list 的尾端操作快、頭端操作慢，
      這個不對稱在這裡剛好幫了後序版一把。】

【代價：它會破壞輸入的 postorder。】

    LeetCode 上無所謂，
    但在真實程式裡【修改呼叫者傳進來的參數是壞習慣】——
    面試時要主動說明這一點，或先 copy 一份。

    這種「函式偷偷改掉輸入」的 bug
    在大型程式裡極難追查。"""),
   ], "O(n)", "O(n)", "pop 是 O(1)", "雜湊表 + 遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "會改輸入嗎", "備註"],
   [["一、切片遞迴", "O(n²) 最壞", "O(n²)", "✘", "思路清楚"],
    ["二、雜湊表 + 游標", "O(n)", "O(n)", "✘", "標準答案"],
    ["三、pop()", "O(n)", "O(n)", "✔", "最短，但會破壞輸入"]]),
 "post": [
   ("note", "三種走訪能組出的所有建樹題", [
     ("c", """前序 + 中序   -> 第 105 題   ✔ 一般二元樹都可以
中序 + 後序   -> 第 106 題   ✔ 一般二元樹都可以
前序 + 後序   -> 第 889 題   ✘ 一般情況不唯一，需要「完滿二元樹」

【規律】：只要其中一條是【中序】，就一定可以。

    因為中序是唯一能「把左右分開」的走訪 ——
    根在中間，左邊全是左子樹，右邊全是右子樹。

    前序和後序都只告訴你「根在哪一端」，
    對「左右怎麼分」完全沒有貢獻。

    兩個都只能定根 -> 資訊不足。

【延伸】：層序 + 中序也可以嗎？
    可以 ✔ —— 層序的第一個是根（和前序一樣），
    但要從層序裡篩出「屬於左子樹的那些」比較麻煩，
    實作上不如前序方便。"""),
   ]),
 ],
 "edges": [
   "<strong>單一節點</strong> → 一個節點的樹。",
   "<strong>退化成一條鏈</strong>（3000 個節點）→ <code>RecursionError</code> 的風險。",
   "<strong>先建 <code>left</code> 後建 <code>right</code></strong> → "
   "<strong>樹整個錯掉，不會報錯 —— 本題第一名的 bug。</strong>",
   "<strong>切片寫成 <code>postorder[k:]</code></strong>（忘了去掉根）→ 長度對不上，結構錯亂。",
   "<strong>游標從 0 開始往前走</strong> → 拿到的是最左下的葉節點當根。",
   "<strong>用 <code>postorder.pop(0)</code></strong> → 那是 O(n)，而且順序也錯。",
   "<strong>解法三會修改輸入</strong> → 呼叫端如果還要用 <code>postorder</code> 就出事了。",
 ],
 "follow": [
   ("h", "追問一：能不能寫成「和第 105 題共用一份程式碼」？"),
   ("c", """可以 —— 把後序反轉，再交換「左右」的角色：

    def buildTree(self, inorder, postorder):
        # reversed(postorder) 的結構是 根 → 右 → 左
        # 相當於「前序」，只是左右對調
        rev = postorder[::-1]
        mirrored = self.build_from_preorder(rev, inorder[::-1])
        return mirror(mirrored)     # 最後再鏡像回來

【能動，但不推薦】：
    多了兩次反轉和一次鏡像，常數變大、也更難讀。

    直接改兩行（游標方向 + 左右順序）比較好。

    不過這個「化簡成已解決的問題」的思路本身很有價值 ——
    在真的想不出來時，它是可靠的退路。""",),
   ("h", "追問二：如何驗證建出來的樹是對的？"),
   "<strong>把它的中序和後序再走一遍，和輸入比對</strong> —— "
   "<strong>這是最可靠的自我檢查，也是這個網站每一題都在做的事。</strong>",
   ("c", """assert inorder_of(tree)   == inorder
assert postorder_of(tree) == postorder

【注意：光比對一條是不夠的。】

    只比中序的話，任何「中序相同」的樹都會通過 ——
    而中序相同的樹有 C(n) 種（卡塔蘭數，第 96 題）。

    兩條都對，才能確定樹是唯一正確的那一棵。"""),
   ("h", "追問三：如果輸入是不合法的（不是同一棵樹的走訪）呢？"),
   "<strong>題目保證合法，所以不用檢查。</strong>"
   "但如果要寫防禦性的程式：",
   ("ul", [
     "<strong>長度不同</strong> → 直接無效。",
     "<strong>多重集合不同</strong> → 無效（用 <code>Counter</code> 比較）。",
     "<strong>結構矛盾</strong> → 最可靠的檢查是「先照常建樹，再驗證走訪結果」。"
     "<strong>先建再驗，比想辦法「邊建邊檢查」簡單得多。</strong>",
   ]),
   ("h", "追問四：時間能不能低於 O(n)？"),
   "<strong>不可能。</strong>輸出本身就有 <code>n</code> 個節點，"
   "<strong>光是把它們建出來就要 O(n)</strong>。"
   "<strong>這叫做「輸出規模下界」（output-sensitive lower bound）</strong> —— "
   "任何「要產生 n 個東西」的問題都至少要 Ω(n)。",
 ],
 "related": [
   "<strong>第 105 題 從前序與中序建樹</strong> —— 本題的鏡像版",
   "<strong>第 889 題 從前序與後序建樹</strong> —— 為什麼需要額外前提",
   "<strong>第 108 題 有序陣列轉 BST</strong> —— 另一種分治建樹",
   "<strong>第 145 題 後序走訪</strong> —— 本題的逆運算",
 ],
 "check": [
   "後序倒著讀是什麼順序？為什麼這讓它和前序「對稱」？",
   "為什麼一定要先建 <code>right</code> 再建 <code>left</code>？",
   "切片版裡右子樹為什麼是 <code>postorder[k:-1]</code> 而不是 <code>postorder[k:]</code>？",
   "為什麼「只要有中序」就一定能建樹，而「前序 + 後序」不行？",
 ],
})
print("P106 written")

# ==================== 107. Level Order Traversal II ====================
S["p107_rev"] = '''from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res, dq = [], deque([root])
        while dq:
            level = []
            for _ in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(level)

        return res[::-1]        # 唯一的差別：最後整個反轉'''

S["p107_insert"] = '''from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res, dq = [], deque([root])
        while dq:
            level = []
            for _ in range(len(dq)):
                node = dq.popleft()
                level.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.insert(0, level)    # 每次插到最前面 —— 能動，但是 O(h) 每次

        return res'''

S["p107_dfs"] = '''class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def go(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append([])
            res[depth].append(node.val)
            go(node.left, depth + 1)
            go(node.right, depth + 1)

        go(root, 0)
        return res[::-1]'''


def _lvl(root):
    out = {}
    def go(nd, d):
        if not nd:
            return
        out.setdefault(d, []).append(nd.val)
        go(nd.left, d + 1)
        go(nd.right, d + 1)
    go(root, 0)
    return [out[d] for d in sorted(out)]


def _p107_ref(root):
    return _lvl(root)[::-1]


def _rand_tree(n, lo=-5, hi=5):
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi), _rand_tree(left, lo, hi), _rand_tree(n - 1 - left, lo, hi))


_p107 = [S.load(k) for k in ("p107_rev", "p107_insert", "p107_dfs")]

for spec, want in [
    ([3, [9, None, None], [20, [15, None, None], [7, None, None]]], [[15, 7], [9, 20], [3]]),
    ([1, None, None], [[1]]),
    (None, []),
]:
    assert _p107_ref(_build(spec)) == want, ("P107 ref", spec)
    for sol in _p107:
        assert sol.levelOrderBottom(_build(spec)) == want, ("P107", spec, sol)

for _ in range(4000):
    t = _rand_tree(random.randrange(0, 12))
    want = _p107_ref(t)
    for sol in _p107:
        assert sol.levelOrderBottom(t) == want, ("P107 random", want, sol)
print("P107 solutions OK")

emit({
 "num": 107, "slug": "binary-tree-level-order-traversal-ii",
 "en": [
   "Given the <code>root</code> of a binary tree, return <em>the bottom-up level order "
   "traversal of its nodes' values</em>. (i.e., from left to right, level by level from leaf "
   "to root).",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，回傳<strong>由下而上</strong>的層序走訪結果。",
   "也就是<strong>從最深的一層開始往上</strong>，每一層內部仍然是<strong>由左到右</strong>。",
 ],
 "pre": [
   ("note", "第 102 題 + 一個 [::-1]", [
     ("c", """這題本身很簡單 —— 照常做層序走訪，最後把結果反轉。

【但它有一個真正的考點：不要用 insert(0, ...)。】

    很多人會想：「既然要倒過來，那我每次就插到最前面。」

        res.insert(0, level)

    能動，但是：
        list.insert(0, x) 要把已有的元素【全部往後搬一格】-> O(len(res))

        做 h 次（h = 層數）-> O(h²)

    對這題來說 h 最多 2000，h² = 400 萬 —— 過得了。
    但這是「碰巧過關」。

【正確的反射】：
    需要「反過來的順序」時，
    永遠是【先照正常順序收集，最後反轉一次】。

    反轉一次是 O(h)，比 O(h²) 好太多。

    這個原則在 list、字串、鏈結串列上都適用，
    是很值得內化的習慣。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [3,9,20,null,null,15,7]

            3
           / \\
          9   20
             /  \\
            15   7

  輸出：[[15,7],[9,20],[3]]

  說明：最深的一層（15, 7）排最前面，根（3）排最後。
        注意【每一層內部仍然是由左到右】——
        只有「層與層之間」的順序倒過來。

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
 "idea": [
   ("c", """把第 102 題的答案照抄，最後加一個 [::-1]。

    res = <第 102 題的結果>
    return res[::-1]

【只反轉「外層」，不反轉「內層」。】

    res       = [[3], [9, 20], [15, 7]]
    res[::-1] = [[15, 7], [9, 20], [3]]   ✔

    每個 level 裡面的順序【完全沒動】。

    如果你不小心寫成：
        return [lv[::-1] for lv in res[::-1]]

    會得到 [[7, 15], [20, 9], [3]] ✘ —— 內層也反了。

【這題的價值，是讓你練習
  「走訪邏輯」和「輸出順序」分離這個習慣。】

    第 103 題（鋸齒）也是同一個原則：
        BFS 照常跑，只在輸出時調整。"""),
 ],
 "approaches": [
   ap("解法一", "BFS + 最後反轉（標準答案）", [
     ("c", S["p107_rev"]),
     "<strong>和第 102 題唯一的差別是最後一行的 <code>[::-1]</code>。</strong>",
     ("h", "<code>[::-1]</code>、<code>reversed()</code>、<code>reverse()</code> 怎麼選？"),
     ("c", """res[::-1]          回傳新 list         O(h) 時間、O(h) 空間
list(reversed(res)) 回傳新 list         O(h) 時間、O(h) 空間
res.reverse()       原地反轉，回傳 None  O(h) 時間、O(1) 額外空間

    這題三個都可以（反正 res 就是要回傳的東西）。

    但要記得：
        return res.reverse()    ✘ 回傳 None！
        res.reverse(); return res   ✔

    【原地修改的方法回傳 None，是 Python 的一貫設計】：
        sort()、reverse()、append()、extend() 都是。

        對應的「回傳新東西」版本是：
        sorted()、reversed()、+ 運算子、list 生成式。

    這個區分踩過一次就會記住 ——
    但最好是現在就記住。"""),
     "<strong>總複雜度和第 102 題完全相同</strong>（多的那次反轉是 O(h)，被 O(n) 吸收）。",
   ], "O(n)", "O(w)", "反轉是 O(h)", "佇列最大寬度", optimal=True),

   ap("解法二", "每次 insert(0, ...)（示範效能陷阱）", [
     ("c", S["p107_insert"]),
     ("h", "為什麼 <code>insert(0, x)</code> 這麼慢"),
     ("c", """Python 的 list 是【連續記憶體的動態陣列】。

    在【尾端】append：直接寫進下一格 -> 攤還 O(1) ✔
    在【頭端】insert：所有元素都要往後搬一格 -> O(n) ✘

        insert(0, x) 之前： [a, b, c]
        搬移：              [_, a, b, c]
        寫入：              [x, a, b, c]

    做 h 次，總成本 = 1 + 2 + ... + h = O(h²)

【什麼時候真的需要頭端插入？】

    改用 collections.deque —— 它的 appendleft() 是 O(1)。

        dq = deque()
        dq.appendleft(level)
        return list(dq)

    這樣是 O(h) ✔

    但對這題來說，「最後反轉一次」更簡單也一樣快。

【記住這組對照】：
    list   -> 尾端快、頭端慢
    deque  -> 兩端都快，但隨機存取慢（O(n)）

    需要兩端操作就用 deque，
    需要隨機存取就用 list。"""),
     "<strong>本題 h ≤ 2000，所以還是會過</strong> —— "
     "<strong>但面試時寫這個，面試官一定會問「這裡的複雜度是多少」。</strong>",
   ], "O(n + h²)", "O(w)", "insert(0) 是 O(h)", "佇列最大寬度"),

   ap("解法三", "DFS + 最後反轉", [
     ("c", S["p107_dfs"]),
     "<strong>和第 102 題的 DFS 版一樣，只是最後反轉。</strong>",
     "<strong>優點</strong>：空間是 <code>O(h)</code> 而不是 <code>O(w)</code> —— "
     "<strong>對「深而窄」的樹比較省</strong>。",
     "<strong>缺點</strong>：遞迴深度 2000 在 Python 下有 <code>RecursionError</code> 的風險"
     "（預設上限 1000）。",
     ("c", """如果真的擔心遞迴深度，可以在開頭加：

    import sys
    sys.setrecursionlimit(10000)

【但這在面試裡是下策】——
    它只是把問題往後推（真正的 C 堆疊還是可能爆），
    而且看起來像在逃避。

    正確的回答是：
        「如果樹可能很深，我會改用迭代版。」

    然後寫解法一。""",),
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、BFS + 最後反轉", "O(n)", "O(w)", "標準答案"],
    ["二、每次 insert(0)", "O(n + h²)", "O(w)", "示範陷阱，不要用"],
    ["三、DFS + 最後反轉", "O(n)", "O(h)", "深而窄的樹比較省"]]),
 "edges": [
   "<strong><code>root = None</code></strong> → <code>[]</code>。",
   "<strong>單一節點</strong> → <code>[[1]]</code>（反轉單元素 list 還是自己）。",
   "<strong>兩層</strong> <code>[1,2,3]</code> → <code>[[2,3],[1]]</code>。"
   "<strong>注意內層的 <code>[2,3]</code> 沒有變成 <code>[3,2]</code>。</strong>",
   "<strong>連內層也反轉了</strong> → 那是錯的，題目只要求層與層之間倒過來。",
   "<strong><code>return res.reverse()</code></strong> → 回傳 <code>None</code>。",
   "<strong>退化成一條鏈</strong>（2000 層）→ "
   "<code>insert(0)</code> 版要做 200 萬次搬移；DFS 版可能 <code>RecursionError</code>。",
 ],
 "follow": [
   ("h", "追問一：如果不准用額外空間存結果，能不能邊算邊輸出？"),
   "<strong>不行 —— 因為「最後一層」要最先輸出，而你必須走完整棵樹才知道最後一層是什麼。</strong>",
   "<strong>除非先做一次「求最大深度」（第 104 題）</strong>，"
   "然後對每個深度 <code>d = h-1, h-2, ..., 0</code> 各做一次「只輸出深度 d」的 DFS。",
   "<strong>空間降到 O(h)，時間變成 O(n·h)</strong> —— "
   "<strong>這就是迭代加深的思路，用時間換空間。</strong>",
   ("h", "追問二：<code>deque.appendleft</code> 為什麼是 O(1)？"),
   ("c", """collections.deque 內部是【雙向鏈結的固定大小區塊串】
（doubly-linked list of fixed-size blocks），
不是連續陣列。

    頭端插入：找到頭的那個區塊，寫進去 -> O(1) ✔
    尾端插入：同理 -> O(1) ✔
    隨機存取 dq[k]：要一塊一塊走過去 -> O(n) ✘

【所以 deque 和 list 的取捨很明確】：

    需要兩端 O(1) 操作（佇列、雙端佇列） -> deque
    需要 O(1) 隨機存取（一般陣列）        -> list

    這題（和第 102 題）用 deque 當 BFS 佇列，
    就是因為 popleft 必須是 O(1)。"""),
   ("h", "追問三：如果要「每層由右到左，而且層也倒過來」呢？"),
   "<strong>內外都反轉</strong>：<code>[lv[::-1] for lv in res[::-1]]</code>。",
   "<strong>這等價於「把整個層序序列完全反轉」</strong> —— "
   "也等價於「先把樹鏡像（第 226 題），再做本題」。"
   "<strong>兩種做法的答案完全相同，可以互相驗證。</strong>",
   ("h", "追問四：為什麼這題會被單獨出一題？"),
   "<strong>因為它考的不是演算法，是「習慣」。</strong>"
   "<strong>「先收集再反轉」vs「每次插到前面」</strong>這個選擇，"
   "在<strong>鏈結串列反轉、字串建構、堆疊輸出</strong>等地方會反覆出現。",
   "<strong>面試官想看的是：你會不會不假思索地寫出 <code>insert(0, ...)</code>。</strong>",
 ],
 "related": [
   "<strong>第 102 題 Level Order Traversal</strong> —— 本題的基礎",
   "<strong>第 103 題 Zigzag Level Order</strong> —— 另一種「輸出時調整」",
   "<strong>第 104 題 Maximum Depth</strong> —— 追問一需要用到",
   "<strong>第 226 題 Invert Binary Tree</strong> —— 追問三的另一種做法",
 ],
 "check": [
   "為什麼「先收集再反轉」比「每次 <code>insert(0, ...)</code>」好？各是什麼複雜度？",
   "<code>list.reverse()</code> 和 <code>list[::-1]</code> 有什麼差別？",
   "只反轉外層和內外都反轉，結果差在哪裡？",
   "<code>deque.appendleft</code> 為什麼能做到 O(1)，而 <code>list.insert(0, x)</code> 不行？",
 ],
})
print("P107 written")

# ==================== 108. Convert Sorted Array to BST ====================
S["p108_mid"] = '''class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2            # 取中點當根
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(nums) - 1)'''

S["p108_slice"] = '''class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        return TreeNode(nums[mid],
                        self.sortedArrayToBST(nums[:mid]),
                        self.sortedArrayToBST(nums[mid + 1:]))'''

S["p108_iter"] = '''class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        root = TreeNode(0)                  # 先放一個佔位的根
        stack = [(root, 0, len(nums) - 1)]  # (要填的節點, 這段的左界, 右界)

        while stack:
            node, lo, hi = stack.pop()
            mid = (lo + hi) // 2
            node.val = nums[mid]

            if lo <= mid - 1:               # 左邊還有東西 -> 開一個左孩子
                node.left = TreeNode(0)
                stack.append((node.left, lo, mid - 1))
            if mid + 1 <= hi:
                node.right = TreeNode(0)
                stack.append((node.right, mid + 1, hi))

        return root'''


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
    return (lo < nd.val < hi and _is_bst(nd.left, lo, nd.val)
            and _is_bst(nd.right, nd.val, hi))


_p108 = [S.load(k) for k in ("p108_mid", "p108_slice", "p108_iter")]

for _ in range(3000):
    n = random.randrange(0, 40)
    nums = sorted(random.sample(range(-200, 200), n))
    for sol in _p108:
        t = sol.sortedArrayToBST(list(nums))
        assert _ino(t) == nums, ("P108 inorder", nums, sol)
        assert _is_bst(t), ("P108 not bst", nums, sol)
        assert _balanced(t), ("P108 not balanced", nums, sol)
# 高度必須剛好是 ceil(log2(n+1))
import math
for n in range(0, 200):
    nums = list(range(n))
    for sol in _p108:
        h = _height(sol.sortedArrayToBST(list(nums)))
        assert h == (0 if n == 0 else math.ceil(math.log2(n + 1))), ("P108 height", n, h, sol)
print("P108 solutions OK")

_P108_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">取中點當根，左右各半遞迴。每次把問題砍半 → 樹高必然是 O(log n)，而且自動平衡。</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">nums = [-10, -3, 0, 5, 9]　　（已排序）</text>
            <g font-size="13" text-anchor="middle">
              <rect x="60" y="66" width="70" height="28" fill="none" stroke="var(--accent)"/><text x="95" y="85" fill="var(--accent)">-10</text>
              <rect x="138" y="66" width="70" height="28" fill="none" stroke="var(--accent)"/><text x="173" y="85" fill="var(--accent)">-3</text>
              <rect x="216" y="66" width="70" height="28" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="251" y="85" fill="var(--gold)">0</text>
              <rect x="294" y="66" width="70" height="28" fill="none" stroke="#ff8a65"/><text x="329" y="85" fill="#ff8a65">5</text>
              <rect x="372" y="66" width="70" height="28" fill="none" stroke="#ff8a65"/><text x="407" y="85" fill="#ff8a65">9</text>
              <text x="470" y="85" fill="var(--text-muted)" text-anchor="start" font-size="11">mid = 2 → 根是 0</text>
            </g>
            <text x="134" y="114" fill="var(--accent)" font-size="11" text-anchor="middle">左半 [-10, -3]</text>
            <text x="368" y="114" fill="#ff8a65" font-size="11" text-anchor="middle">右半 [5, 9]</text>
            <line x1="20" y1="134" x2="620" y2="134" stroke="var(--border)"/>
            <g font-size="13" text-anchor="middle">
              <circle cx="320" cy="174" r="19" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="320" y="179" fill="var(--gold)">0</text>
              <circle cx="220" cy="240" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="220" y="245" fill="var(--accent)">-3</text>
              <circle cx="420" cy="240" r="19" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="420" y="245" fill="#ff8a65">9</text>
              <circle cx="150" cy="306" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="150" y="311" fill="var(--accent)">-10</text>
              <circle cx="350" cy="306" r="19" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="350" y="311" fill="#ff8a65">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="306" y1="188" x2="234" y2="226"/><line x1="334" y1="188" x2="406" y2="226"/>
              <line x1="206" y1="254" x2="164" y2="292"/><line x1="406" y1="254" x2="364" y2="292"/>
            </g>
            <text x="20" y="348" fill="var(--accent)" font-size="12">中序走訪 = -10, -3, 0, 5, 9 = 原陣列 ✔　（所以它一定是合法的 BST）</text>
            <text x="20" y="374" fill="var(--gold)" font-size="12">高度 = 3 = ⌈log₂(5+1)⌉ ✔　（所以它一定是平衡的）</text>
            <line x1="20" y1="394" x2="620" y2="394" stroke="var(--border)"/>
            <text x="20" y="420" fill="#ff8a65" font-size="12">答案不唯一：mid 取 (lo+hi)//2 或 (lo+hi+1)//2 會得到不同但同樣合法的樹。</text>'''

emit({
 "num": 108, "slug": "convert-sorted-array-to-binary-search-tree",
 "en": [
   "Given an integer array <code>nums</code> where the elements are sorted in "
   "<strong>ascending order</strong>, convert <em>it to a "
   "<strong>height-balanced</strong> binary search tree</em>.",
 ],
 "zh": [
   "給你一個<strong>升序排列</strong>的整數陣列 <code>nums</code>，"
   "把它轉換成一棵<strong>高度平衡</strong>的二元搜尋樹。",
   ("note", "「高度平衡」的定義", [
     "<strong>每個節點的左右子樹高度差不超過 1</strong>。",
     "這是 <strong>AVL 樹</strong>的平衡條件，也是第 110 題要判斷的性質。",
     "<strong>注意：答案不唯一</strong> —— 只要滿足「是 BST」和「高度平衡」就算對，"
     "LeetCode 會用特殊的判題器。",
   ]),
 ],
 "pre": [
   ("note", "兩個條件，各由一件事保證", [
     ("c", """要求一：是【二元搜尋樹】
    -> 由「中序走訪必須是原陣列」保證。
       （BST ⟺ 中序遞增，第 98 題的那把鑰匙。）

要求二：【高度平衡】
    -> 由「每次取中點」保證。

【關鍵洞察】：
    這兩個要求剛好都指向同一個做法 ——

        取中點當根，左半建左子樹，右半建右子樹

    因為：
        中點左邊的都比它小 -> 放左子樹 ✔ （滿足 BST）
        中點右邊的都比它大 -> 放右子樹 ✔
        左右兩半的大小最多差 1 -> 高度最多差 1 ✔ （滿足平衡）

    【一個做法同時滿足兩個要求，
      這就是為什麼這題是 Easy。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [-10,-3,0,5,9]
  輸出：[0,-3,9,-10,null,5]

            0
           / \\
         -3   9
         /   /
      -10   5

  說明：[0,-10,5,null,-3,null,9] 也是合法答案。

範例 2
  輸入：nums = [1,3]
  輸出：[3,1]  （或 [1,null,3]）

  說明：兩個元素時，誰當根都可以 ——
        [3,1]      是 mid = (0+1+1)//2 = 1 的結果
        [1,null,3] 是 mid = (0+1)//2   = 0 的結果""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁴",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
   "<code>nums</code> 依<strong>嚴格遞增</strong>排序",
 ],
 "idea": [
   ("fig", _P108_FIG, "0 0 640 438"),
   ("c", """build(lo, hi)：用 nums[lo..hi] 建一棵平衡 BST

    if lo > hi: return None
    mid = (lo + hi) // 2
    node = TreeNode(nums[mid])
    node.left  = build(lo, mid - 1)
    node.right = build(mid + 1, hi)

【為什麼一定平衡？】

    左半有 mid - lo   個元素
    右半有 hi - mid   個元素

    因為 mid 是中點，這兩個數最多差 1。

    設 H(k) = 用 k 個元素建出的樹高，
    則 H(k) = 1 + max(H(⌊(k-1)/2⌋), H(⌈(k-1)/2⌉))

    解出來 H(k) = ⌈log₂(k+1)⌉

    而左右子樹的元素數最多差 1
    -> 它們的高度最多差 1 ✔ （因為 H 是單調的）

    對每個節點都成立 -> 整棵樹高度平衡 ✔

【這也順便證明了樹高是 O(log n)】——
    n = 10⁴ 時樹高只有 14，遞迴完全不會爆。"""),
 ],
 "approaches": [
   ap("解法一", "索引區間遞迴（標準答案）", [
     ("c", S["p108_mid"]),
     "<strong>七行，O(n) 時間。</strong>"
     "<strong>每個元素恰好被用來建一個節點。</strong>",
     ("h", "為什麼這裡不會退化成 O(n²)？"),
     ("c", """對照第 105 題：那裡的切片版會退化，這裡不會。

    差別在於【這裡用的是索引區間，沒有複製資料】。

    每一層遞迴只做 O(1) 的工作（算 mid、建節點），
    節點總數是 n -> 總共 O(n) ✔

    如果改用切片版（解法二），
    每層要複製 O(k) 的資料 -> 變成 O(n log n)。

    （注意：是 O(n log n) 不是 O(n²) ——
      因為這題一定是平衡的，遞迴樹只有 log n 層，
      每層總共複製 O(n)。）"""),
     ("h", "<code>mid</code> 取法的兩個變體"),
     ("c", """mid = (lo + hi) // 2        偏左的中點
mid = (lo + hi + 1) // 2    偏右的中點

    兩個都對，只是建出來的樹不同（但都平衡）。

    nums = [1, 3]：
        偏左： mid = 0 -> 根是 1，右孩子 3    [1, null, 3]
        偏右： mid = 1 -> 根是 3，左孩子 1    [3, 1]

    LeetCode 的判題器會接受任何一個。

【還有一個隨機版本】：
    mid = random.randint(lo, hi) 也能建出 BST，
    但【不保證平衡】—— 所以這題不能這樣寫。

    （不過「隨機選 pivot」正是快速排序避免最壞情況的手法，
      在那裡它是好主意。）

【溢位提醒】：
    在 Java / C++ 裡 (lo + hi) 可能溢位，
    要寫成 lo + (hi - lo) // 2。
    Python 沒這個問題，但面試時提一下會加分。"""),
   ], "O(n)", "O(log n)", "每個元素一次", "遞迴堆疊（樹高）", optimal=True),

   ap("解法二", "切片遞迴（最短，但有隱藏成本）", [
     ("c", S["p108_slice"]),
     "<strong>五行，讀起來最像「題目的直譯」。</strong>",
     ("c", """時間 O(n log n)：

    遞迴樹有 log n 層，
    每一層的切片加起來會複製 O(n) 個元素
    -> O(n log n)

空間 O(n log n)：
    同時存在的切片副本。

    對 n = 10⁴ 來說：
        10⁴ × 14 = 14 萬 —— 完全沒問題。

【所以這個版本在 LeetCode 上跑起來甚至可能更快】——
    因為 Python 的切片是 C 層實作，
    比多一個函式參數的開銷還小。

【但面試時要能說出它的複雜度】。
    「我知道這裡有 O(n log n) 的切片成本，
      如果 n 很大我會改用索引版」——
    這句話比寫出哪個版本更重要。"""),
   ], "O(n log n)", "O(n log n)", "切片複製", "切片副本"),

   ap("解法三", "迭代 + 堆疊（避免遞迴）", [
     ("c", S["p108_iter"]),
     ("h", "技巧：先建空節點佔位，再填值"),
     ("c", """遞迴版是「算出值 -> 建節點 -> 掛上去」，
迭代版沒辦法「先建孩子再掛」，
所以反過來：

    【先建一個空節點掛好，再把 (節點, 區間) 放進堆疊，
      之後再回來填它的值。】

    這是「遞迴改迭代」在【建構型】問題上的通用手法：
        先分配好結構，再填內容。

    對照「查詢型」問題（例如第 104 題）
    只要把參數打包進堆疊就好，不用先分配。

【樹高只有 O(log n) = 14，所以其實完全不需要這個版本。】

    放在這裡是因為這個「佔位再填」的技巧
    在其他建構型題目（例如第 109 題的中序建樹）
    會再出現。"""),
     "<strong>O(n) 時間、O(log n) 空間（堆疊最多存樹高那麼多筆）。</strong>",
   ], "O(n)", "O(log n)", "每個節點一次", "顯式堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、索引區間遞迴", "O(n)", "O(log n)", "9", "標準答案"],
    ["二、切片遞迴", "O(n log n)", "O(n log n)", "5", "最短，實測也快"],
    ["三、迭代 + 堆疊", "O(n)", "O(log n)", "15", "示範「佔位再填」"]]),
 "edges": [
   "<strong>單一元素</strong> <code>[1]</code> → 一個節點。",
   "<strong>兩個元素</strong> <code>[1,3]</code> → <code>mid</code> 取法不同會得到不同的樹，"
   "<strong>但兩個都對</strong>。",
   "<strong>空陣列</strong>（題目保證不會）→ 應回 <code>None</code>。三種解法都自然正確。",
   "<strong><code>lo > hi</code> 寫成 <code>lo >= hi</code></strong> → "
   "會漏掉單一元素的區間，樹少一半節點。",
   "<strong><code>build(lo, mid)</code> 忘了 <code>-1</code></strong> → 無窮遞迴（<code>mid</code> 會一直是自己）。",
   "<strong>用隨機的 <code>mid</code></strong> → 仍是合法 BST，但<strong>不保證平衡</strong>，"
   "判題器會判錯。",
   "<strong>10⁴ 個元素</strong> → 樹高只有 14，<strong>遞迴絕對不會爆</strong>。",
 ],
 "follow": [
   ("h", "追問一：如果輸入是鏈結串列而不是陣列呢？"),
   "<strong>第 109 題。</strong>問題在於<strong>鏈結串列無法 O(1) 取中點</strong>。",
   ("ul", [
     "<strong>做法 A</strong>：先轉成陣列，然後照這題做。"
     "<code>O(n)</code> 時間、<code>O(n)</code> 額外空間 —— <strong>最實際。</strong>",
     "<strong>做法 B</strong>：每次用快慢指標找中點。"
     "<code>O(n log n)</code> 時間、<code>O(log n)</code> 空間。",
     "<strong>做法 C</strong>：<strong>「中序建樹」</strong> —— "
     "先算出長度，然後<strong>按中序的順序建節點</strong>，"
     "一邊建一邊往前推進串列指標。<code>O(n)</code> 時間、<code>O(log n)</code> 空間 —— "
     "<strong>三者中最優，也最漂亮。</strong>",
   ]),
   ("h", "追問二：為什麼答案不唯一？有幾種？"),
   ("c", """n 個元素能建出的【平衡】BST 有幾棵？

    這不是卡塔蘭數（那是【所有】BST 的數量）——
    平衡的限制會砍掉絕大多數。

    n = 1： 1 棵
    n = 2： 2 棵（誰當根都行）
    n = 3： 1 棵（必須是完美二元樹）
    n = 4： 4 棵
    n = 5： 6 棵

    沒有簡單的封閉公式，但可以用 DP 算：
        f(n) = Σ  f(k) × f(n-1-k)
               k
        其中 k 跑過所有「讓左右高度差 ≤ 1」的分割

【LeetCode 用特殊判題器（special judge）就是因為這個】——
    它不比對輸出，而是【驗證你的輸出滿足兩個性質】。""",),
   ("h", "追問三：建出來的樹一定是「完全二元樹」嗎？"),
   "<strong>不一定。</strong>「高度平衡」比「完全」寬鬆得多。",
   ("c", """n = 5, mid = (lo+hi)//2：

        0
       / \\
     -3   9
     /   /
   -10  5

    最後一層的節點沒有「靠左對齊」-> 不是完全二元樹 ✘
    但左右高度差都 ≤ 1 -> 是高度平衡的 ✔

【三個容易混淆的名詞】：
    完全（complete）：除最後一層外都滿，最後一層靠左對齊
    完美（perfect）： 每一層都滿（節點數 = 2^h - 1）
    平衡（balanced）：每個節點的左右高度差 ≤ 1

    完美 ⟹ 完全 ⟹ 平衡，反過來都不成立。

    第 116 題要求「完美」，第 222 題處理「完全」，
    本題和第 110 題講「平衡」。""",),
   ("h", "追問四：如果陣列有重複值呢？"),
   "<strong>題目保證嚴格遞增，所以不會。</strong>"
   "如果有重複，就要先決定「相等的值放哪一側」（見第 98 題的追問），"
   "<strong>建樹的邏輯不變，但 BST 的定義要先講清楚</strong>。",
 ],
 "related": [
   "<strong>第 109 題 有序鏈結串列轉 BST</strong> —— 同一題，但輸入是串列",
   "<strong>第 110 題 Balanced Binary Tree</strong> —— 判斷這題的輸出是否合格",
   "<strong>第 98 題 Validate BST</strong> —— 另一個驗證條件",
   "<strong>第 95 題 Unique Binary Search Trees II</strong> —— 列出所有（不要求平衡的）BST",
 ],
 "check": [
   "「取中點當根」為什麼同時保證了「是 BST」和「高度平衡」？",
   "索引版是 O(n)，切片版是 O(n log n) —— 差別在哪裡？",
   "<code>mid</code> 取 <code>(lo+hi)//2</code> 和 <code>(lo+hi+1)//2</code> 會得到一樣的樹嗎？兩個都對嗎？",
   "「高度平衡」「完全」「完美」三個名詞有什麼不同？",
 ],
})
print("P108 written")
