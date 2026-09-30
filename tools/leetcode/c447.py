# -*- coding: utf-8 -*-
"""第 447–452 題。"""
import random
import itertools
from collections import Counter, deque
from authoring import emit, ap
from runner import Src, TreeNode
from lchelp import lv, ser, bst, nodes

S = Src()
random.seed(447)


# ==================== 447. Number of Boomerangs ====================
S["p447"] = '''class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total = 0
        for x1, y1 in points:                       # ★ 把每個點當作中心 i
            dist = collections.Counter()
            for x2, y2 in points:
                dist[(x1 - x2) ** 2 + (y1 - y2) ** 2] += 1   # 用距離平方，避免浮點數
            for c in dist.values():
                total += c * (c - 1)                # 同距離的 c 個點中選有序的 (j, k)
        return total'''

_p447 = S.load("p447")
for pts, want in [([[0, 0], [1, 0], [2, 0]], 2), ([[1, 1], [2, 2], [3, 3]], 2), ([[1, 1]], 0)]:
    assert _p447.numberOfBoomerangs(pts) == want
for _ in range(1000):
    pts = [list(p) for p in {(random.randint(0, 4), random.randint(0, 4)) for _ in range(random.randrange(1, 9))}]
    d = lambda a, b: (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
    want = sum(1 for i, j, k in itertools.permutations(range(len(pts)), 3) if d(pts[i], pts[j]) == d(pts[i], pts[k]))
    assert _p447.numberOfBoomerangs(pts) == want
print("P447 OK")

emit({
 "num": 447, "slug": "number-of-boomerangs",
 "en": [
   "You are given <code>n</code> <code>points</code> in the plane that are all <strong>distinct</strong>, where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>. A <strong>boomerang</strong> is a tuple of points <code>(i, j, k)</code> such that the distance between <code>i</code> and <code>j</code> equals the distance between <code>i</code> and <code>k</code> <strong>(the order of the tuple matters)</strong>.",
   "Return <em>the number of boomerangs</em>.",
 ],
 "zh": [
   "平面上有 <code>n</code> 個<strong>互不相同</strong>的點。<strong>迴旋鏢</strong>是一組 <code>(i, j, k)</code>，其中 <code>i</code> 到 <code>j</code> 的距離等於 <code>i</code> 到 <code>k</code> 的距離（<strong>順序有差</strong>）。",
   "回傳迴旋鏢的數量。",
 ],
 "examples": """範例 1
  輸入：points = [[0,0],[1,0],[2,0]]
  輸出：2
  說明：[[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

範例 2
  輸入：points = [[1,1]]
  輸出：0""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 500",
   "−10⁴ ≤ <code>x<sub>i</sub>, y<sub>i</sub></code> ≤ 10⁴",
   "所有點互不相同",
 ],
 "idea": [
   ("c", """【固定中心點 i】
    算出 i 到其他所有點的距離，依距離分組。
    某個距離有 c 個點 -> 從中選「有序的」兩個 (j, k)：c × (c - 1) 種。

【為什麼用距離的平方？】
    開根號會產生浮點數，相等比較不可靠；
    比較距離相等，只要比較平方相等就夠了（而且都是整數）。

【複雜度】
    n 個中心 × n 個點 -> O(n²)。"""),
 ],
 "approaches": [
   ap("解法", "枚舉中心 + 距離計數", [
     ("c", S["p447"]),
   ], "O(n²)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>少於 3 個點</strong> → 0。",
   "<strong>中心點和自己的距離 0</strong> → 只有 1 個（自己），c(c−1) = 0，不影響。",
 ],
 "follow": [
   ("h", "固定一點、分組計數"),
   ("c", "第 149 題（直線上最多的點）：固定一點，依斜率分組。同一個套路。"),
 ],
 "related": [
   "<strong>第 149 題 直線上最多的點數</strong>",
   "<strong>第 356 題 直線鏡像</strong>（付費）",
 ],
 "check": [
   "固定中心後，距離相同的 c 個點能組成幾個迴旋鏢？",
   "為什麼用距離的平方？",
 ],
})


# ==================== 448. Find All Numbers Disappeared in an Array ====================
S["p448"] = '''class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for x in nums:
            i = abs(x) - 1
            if nums[i] > 0:
                nums[i] = -nums[i]            # ★ 標記「值 i+1 出現過」
        # 仍然是正數的位置 i，代表值 i+1 從來沒出現
        return [i + 1 for i, v in enumerate(nums) if v > 0]'''

S["p448_set"] = '''class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        return [x for x in range(1, len(nums) + 1) if x not in seen]'''

_p448 = [S.load(x) for x in ("p448", "p448_set")]
for _ in range(3000):
    n = random.randrange(1, 12)
    nums = [random.randint(1, n) for _ in range(n)]
    want = [x for x in range(1, n + 1) if x not in nums]
    for sol in _p448:
        assert sol.findDisappearedNumbers(list(nums)) == want
print("P448 OK")

emit({
 "num": 448, "slug": "find-all-numbers-disappeared-in-an-array",
 "en": [
   "Given an array <code>nums</code> of <code>n</code> integers where <code>nums[i]</code> is in the range <code>[1, n]</code>, return <em>an array of all the integers in the range</em> <code>[1, n]</code> <em>that do not appear in</em> <code>nums</code>.",
   "<strong>Follow up:</strong> Could you do it without extra space and in <code>O(n)</code> runtime? You may assume the returned list does not count as extra space.",
 ],
 "zh": [
   "給你一個長度為 <code>n</code> 的陣列，每個數都在 <code>[1, n]</code> 之間，回傳 <code>[1, n]</code> 中所有<strong>沒出現</strong>在陣列裡的數。",
   "<strong>進階：</strong>能不用額外空間、<code>O(n)</code> 時間嗎？（輸出不算）",
 ],
 "examples": """範例 1
  輸入：nums = [4,3,2,7,8,2,3,1]
  輸出：[5,6]

範例 2
  輸入：nums = [1,1]
  輸出：[2]""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 10⁵",
   "1 ≤ <code>nums[i]</code> ≤ n",
 ],
 "idea": [
   ("c", """【和第 442 題同一招：陣列當雜湊表】
    讀到 x，把位置 x-1 的值變成負數，代表「x 出現過」。
    最後還是正數的位置 i -> i+1 沒出現過。

【細節】
    - 讀值時要用 abs（可能已經被標成負的）
    - 已經是負的就不要再翻轉（否則會翻回正的）"""),
 ],
 "approaches": [
   ap("解法一", "集合", [
     ("c", S["p448_set"]),
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "原地正負號標記", [
     ("c", S["p448"]),
   ], "O(n)", "O(1)", "", "不計輸出", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、集合", "O(n)", "O(n)"],
    ["二、原地標記", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>沒有消失的數</strong> → 空陣列。",
   "<strong>重複很多次</strong> → 只要標記一次。",
 ],
 "follow": [
   ("h", "另一種原地做法"),
   ("c", "把每個數加 n：nums[(x−1) % n] += n。最後 ≤ n 的位置就是沒出現的。好處是不用處理正負號。"),
 ],
 "related": [
   "<strong>第 442 題 陣列中重複的資料</strong>",
   "<strong>第 41 題 缺失的第一個正數</strong>",
   "<strong>第 268 題 遺失的數字</strong>",
 ],
 "check": [
   "標記的方式是什麼？",
   "為什麼已經是負的就不要再翻轉？",
 ],
})


# ==================== 449. Serialize and Deserialize BST ====================
S["p449"] = '''class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        out = []

        def pre(node):                          # 前序，不需要空節點標記
            if node:
                out.append(str(node.val))
                pre(node.left)
                pre(node.right)

        pre(root)
        return ",".join(out)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = deque(int(x) for x in data.split(",")) if data else deque()

        def build(lo: float, hi: float):
            # ★ BST 的性質：下一個值不在 (lo, hi) 範圍內，就不屬於這棵子樹
            if not vals or not (lo < vals[0] < hi):
                return None
            v = vals.popleft()
            node = TreeNode(v)
            node.left = build(lo, v)
            node.right = build(v, hi)
            return node

        return build(float("-inf"), float("inf"))'''

_cls = S.loadns("p449", {"deque": deque})["Codec"]
for _ in range(1500):
    vals = random.sample(range(0, 60), random.randrange(0, 20))
    t = bst(vals)
    c = _cls()
    s = c.serialize(t)
    assert "#" not in s and "null" not in s
    assert ser(c.deserialize(s)) == ser(t)
print("P449 OK")

emit({
 "num": 449, "slug": "serialize-and-deserialize-bst",
 "en": [
   "Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.",
   "Design an algorithm to serialize and deserialize a <strong>binary search tree</strong>. There is no restriction on how your serialization/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and this string can be deserialized to the original tree structure.",
   "<strong>The encoded string should be as compact as possible.</strong>",
 ],
 "zh": [
   "設計一套演算法，把<strong>二元搜尋樹</strong>序列化成字串、再還原成原本的樹。",
   "<strong>編碼後的字串要盡量精簡。</strong>",
 ],
 "examples": """範例 1
  輸入：root = [2,1,3]
  輸出：[2,1,3]

範例 2
  輸入：root = []
  輸出：[]""",
 "constraints": [
   "節點數在 <code>[0, 10⁴]</code> 之間",
   "0 ≤ <code>Node.val</code> ≤ 10⁴",
   "保證是二元搜尋樹",
 ],
 "idea": [
   ("c", """【和第 297 題的差別：BST 可以不存空節點】
    一般二元樹：前序 + 空標記 "#"，才能唯一確定結構。
    BST：只存前序的值就夠了 —— 值的大小本身就決定了左右。

【為什麼只靠前序就能還原？】
    前序的第一個值是根 r。
    接下來比 r 小的連續一段是左子樹，比 r 大的是右子樹。

【O(n) 還原：帶著上下界遞迴】
    build(lo, hi)：從序列頭拿值，只要它落在 (lo, hi) 就屬於這棵子樹
        根 v = 拿出來
        左子樹 = build(lo, v)
        右子樹 = build(v, hi)
    每個值只被看一次 -> O(n)。

【比第 297 題精簡多少？】
    n 個節點的樹有 n+1 個空指標，
    第 297 題的格式大約要 2n+1 個 token，這裡只要 n 個。"""),
 ],
 "approaches": [
   ap("解法", "前序 + 上下界還原", [
     ("c", S["p449"]),
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>空樹</strong> → 空字串。",
   "<strong>一條鏈</strong> → 遞迴深度 n；很深時改成迭代。",
   "<strong>值不重複</strong> → BST 保證了這一點，上下界用嚴格不等式。",
 ],
 "follow": [
   ("h", "更精簡"),
   ("c", "把數字用固定 2 位元組的二進位編碼（值 ≤ 10⁴ < 2¹⁶），不需要逗號分隔——每個節點剛好 2 個位元組。"),
 ],
 "related": [
   "<strong>第 297 題 二元樹的序列化與反序列化</strong>",
   "<strong>第 1008 題 前序遍歷構造二元搜尋樹</strong>",
   "<strong>第 255 題 驗證前序遍歷序列二元搜尋樹</strong>（付費）",
 ],
 "check": [
   "為什麼 BST 不需要空節點標記？",
   "還原時上下界的作用是什麼？",
   "這個還原為什麼是 O(n)？",
 ],
})


# ==================== 450. Delete Node in a BST ====================
S["p450"] = '''class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:                                     # 找到要刪的節點
            if root.left is None:                 # 只有右孩子（或沒有孩子）
                return root.right
            if root.right is None:                # 只有左孩子
                return root.left
            # ★ 兩個孩子：用右子樹的最小值（後繼）取代自己，再把後繼刪掉
            succ = root.right
            while succ.left:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)
        return root'''

_p450 = S.load("p450")


def _inorder(t):
    out, st, cur = [], [], t
    while st or cur:
        while cur:
            st.append(cur)
            cur = cur.left
        cur = st.pop()
        out.append(cur.val)
        cur = cur.right
    return out


def _is_bst(t, lo=-1e18, hi=1e18):
    return t is None or (lo < t.val < hi and _is_bst(t.left, lo, t.val) and _is_bst(t.right, t.val, hi))


for _ in range(2000):
    vals = random.sample(range(0, 50), random.randrange(0, 15))
    t = bst(vals)
    key = random.choice(vals + [99]) if vals else 3
    t2 = _p450.deleteNode(t, key)
    assert _is_bst(t2) and _inorder(t2) == sorted(v for v in vals if v != key)
print("P450 OK")

_P450_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">刪除有兩個孩子的節點 5：用右子樹最小的 6（中序後繼）取代它</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="160" cy="60" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="160" y="65" fill="#ff8a65">5</text>
              <circle cx="90" cy="120" r="16" fill="none" stroke="var(--text-muted)"/><text x="90" y="125" fill="var(--text)">3</text>
              <circle cx="230" cy="120" r="16" fill="none" stroke="var(--text-muted)"/><text x="230" y="125" fill="var(--text)">8</text>
              <circle cx="190" cy="180" r="16" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="190" y="185" fill="var(--gold)">6</text>
              <circle cx="270" cy="180" r="16" fill="none" stroke="var(--text-muted)"/><text x="270" y="185" fill="var(--text)">9</text>
              <circle cx="220" cy="236" r="16" fill="none" stroke="var(--text-muted)"/><text x="220" y="241" fill="var(--text)">7</text>
            </g>
            <g stroke="var(--text-muted)"><line x1="148" y1="72" x2="102" y2="108"/><line x1="172" y1="72" x2="218" y2="108"/><line x1="222" y1="134" x2="198" y2="166"/><line x1="238" y1="134" x2="262" y2="166"/><line x1="198" y1="194" x2="212" y2="222"/></g>
            <text x="330" y="70" fill="var(--text)" font-size="12">① 找右子樹的最小值：從 8 一路往左 → 6</text>
            <text x="330" y="96" fill="var(--text)" font-size="12">② 把 5 的值換成 6</text>
            <text x="330" y="122" fill="var(--text)" font-size="12">③ 在右子樹中刪掉原本的 6</text>
            <text x="330" y="148" fill="var(--text-muted)" font-size="12">　 6 沒有左孩子 → 用右孩子 7 頂替</text>
            <text x="330" y="190" fill="var(--gold)" font-size="12">★ 6 比左子樹全部大、比右子樹剩下的全部小，</text>
            <text x="330" y="210" fill="var(--gold)" font-size="12">　 放在 5 的位置 BST 性質不變。</text>'''

emit({
 "num": 450, "slug": "delete-node-in-a-bst",
 "en": [
   "Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return <em>the <strong>root node reference</strong> (possibly updated) of the BST</em>.",
   "Basically, the deletion can be divided into two stages:",
   ("ol", ["Search for a node to remove.", "If the node is found, delete the node."]),
   "<strong>Follow up:</strong> Could you solve it with time complexity <code>O(height of tree)</code>?",
 ],
 "zh": [
   "給你二元搜尋樹的根節點和一個 <code>key</code>，刪除值為 <code>key</code> 的節點，回傳（可能改變的）根節點。",
   "分兩步：先找到節點，再刪除它。刪除後仍然必須是二元搜尋樹。",
   "<strong>進階：</strong>能做到 <code>O(樹高)</code> 嗎？",
 ],
 "examples": """範例 1
  輸入：root = [5,3,6,2,4,null,7], key = 3
  輸出：[5,4,6,2,null,null,7]（[5,2,6,null,4,null,7] 也對）

範例 2
  輸入：root = [5,3,6,2,4,null,7], key = 0
  輸出：[5,3,6,2,4,null,7]
  說明：樹中沒有 0。""",
 "constraints": [
   "節點數在 <code>[0, 10⁴]</code> 之間",
   "−10⁵ ≤ <code>Node.val</code> ≤ 10⁵",
   "每個節點的值都不同",
 ],
 "idea": [
   ("fig", _P450_FIG, "0 0 640 256"),
   ("c", """【找到節點：依 BST 性質往左或往右】

【刪除：三種情況】
    1. 沒有孩子 -> 直接刪掉（回傳 None）
    2. 只有一個孩子 -> 讓孩子頂替自己
    3. 兩個孩子 -> 最麻煩：
        找「中序後繼」：右子樹中最小的節點（一路往左走）
        它比左子樹的全部大、比右子樹其他節點都小 ->
        把它的值搬到目前位置，再從右子樹中刪掉它。
        後繼一定沒有左孩子，所以刪它時是情況 1 或 2。

【遞迴寫法的好處】
    每一層回傳「刪除後的子樹根」，父節點接上即可，
    不需要另外記錄父節點。

【也可以用前驅】
    左子樹的最大值，對稱的做法。"""),
 ],
 "approaches": [
   ap("解法", "遞迴 + 中序後繼取代", [
     ("c", S["p450"]),
     "驗證方式：隨機建 BST、刪除任意值，檢查結果仍是 BST，而且中序遍歷剛好少了那個值。",
   ], "O(h)", "O(h)", "", "遞迴深度", optimal=True),
 ],
 "edges": [
   "<strong>key 不存在</strong> → 樹不變。",
   "<strong>刪除根節點</strong> → 回傳新的根。",
   "<strong>刪除葉子</strong> → 直接移除。",
 ],
 "follow": [
   ("h", "平衡樹的刪除"),
   ("c", "紅黑樹、AVL 樹刪除後還要旋轉恢復平衡；Python 標準函式庫沒有平衡樹，sortedcontainers 則用分塊串列代替。"),
 ],
 "related": [
   "<strong>第 701 題 二元搜尋樹中的插入操作</strong>",
   "<strong>第 700 題 二元搜尋樹中的搜尋</strong>",
   "<strong>第 98 題 驗證二元搜尋樹</strong>",
 ],
 "check": [
   "要刪除的節點有兩個孩子時，為什麼要用中序後繼取代？",
   "中序後繼為什麼一定沒有左孩子？",
   "遞迴回傳子樹根的寫法有什麼好處？",
 ],
})


# ==================== 451. Sort Characters By Frequency ====================
S["p451"] = '''class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = collections.Counter(s)
        # ★ 桶排序：次數最多是 len(s)
        bucket = [[] for _ in range(len(s) + 1)]
        for ch, f in cnt.items():
            bucket[f].append(ch)
        out = []
        for f in range(len(s), 0, -1):
            for ch in bucket[f]:
                out.append(ch * f)
        return "".join(out)'''

S["p451_sort"] = '''class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(ch * f for ch, f in collections.Counter(s).most_common())'''

_p451 = [S.load(x) for x in ("p451", "p451_sort")]


def _fs_ok(s, out):
    if sorted(s) != sorted(out):
        return False
    groups = [(k, len(list(g))) for k, g in itertools.groupby(out)]
    c = Counter(s)
    return len(groups) == len(c) and all(n == c[k] for k, n in groups) and all(groups[i][1] >= groups[i + 1][1] for i in range(len(groups) - 1))


for _ in range(3000):
    s = "".join(random.choice("aabbcA1") for _ in range(random.randrange(1, 15)))
    for sol in _p451:
        assert _fs_ok(s, sol.frequencySort(s)), s
print("P451 OK")

emit({
 "num": 451, "slug": "sort-characters-by-frequency",
 "en": [
   "Given a string <code>s</code>, sort it in <strong>decreasing order</strong> based on the <strong>frequency</strong> of the characters. The <strong>frequency</strong> of a character is the number of times it appears in the string.",
   "Return <em>the sorted string</em>. If there are multiple answers, return <em>any of them</em>.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，依字元<strong>出現次數由多到少</strong>重新排列，相同的字元要排在一起。有多種答案時回傳任意一個。",
 ],
 "examples": """範例 1
  輸入：s = "tree"
  輸出："eert"（"eetr" 也可以）

範例 2
  輸入：s = "cccaaa"
  輸出："aaaccc"（"cccaaa" 也可以；"cacaca" 不行，同字元要連在一起）

範例 3
  輸入：s = "Aabb"
  輸出："bbAa"（大小寫不同）""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 5 × 10⁵",
   "<code>s</code> 由大小寫英文字母和數字組成",
 ],
 "idea": [
   ("c", """【計數 -> 依次數排序 -> 每個字元重複次數次】

【排序的方式】
    直接排序不同字元：最多 62 種，O(62 log 62) 可忽略。
    桶排序：次數範圍 1..n，bucket[f] 放出現 f 次的字元，
    從大到小輸出。和第 347 題相同。"""),
 ],
 "approaches": [
   ap("解法一", "Counter.most_common", [
     ("c", S["p451_sort"]),
   ], "O(n + k log k)", "O(n)", "k = 不同字元數", ""),

   ap("解法二", "桶排序", [
     ("c", S["p451"]),
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、most_common", "O(n + k log k)", "一行"],
    ["二、桶排序", "O(n)", "✔"]]),
 "edges": [
   "<strong>大小寫</strong> → 視為不同字元。",
   "<strong>次數相同</strong> → 順序任意，但同一字元必須連續。",
 ],
 "follow": [
   ("h", "同一套路"),
   ("c", "第 347 題（前 K 個高頻元素）、第 692 題（前 K 個高頻單字，同頻時依字典序）。"),
 ],
 "related": [
   "<strong>第 347 題 前 K 個高頻元素</strong>",
   "<strong>第 692 題 前 K 個高頻單字</strong>",
 ],
 "check": [
   "桶的索引代表什麼？",
   "為什麼 \"cacaca\" 不是合法答案？",
 ],
})


# ==================== 452. Minimum Number of Arrows to Burst Balloons ====================
S["p452"] = '''class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])        # ★ 依右端點排序
        arrows = 0
        pos = -float("inf")                    # 上一支箭射在哪裡
        for s, e in points:
            if s > pos:                        # 這顆氣球沒被上一支箭射到
                arrows += 1
                pos = e                        # 射在它的右端點：能順便射到最多後面的氣球
        return arrows'''

_p452 = S.load("p452")


def _arrows_ref(pts):
    cand = sorted({p[1] for p in pts} | {p[0] for p in pts})
    for k in range(1, len(pts) + 1):
        for shots in itertools.combinations(cand, k):
            if all(any(s <= x <= e for x in shots) for s, e in pts):
                return k


for pts, want in [([[10, 16], [2, 8], [1, 6], [7, 12]], 2), ([[1, 2], [3, 4], [5, 6], [7, 8]], 4), ([[1, 2], [2, 3], [3, 4], [4, 5]], 2)]:
    assert _p452.findMinArrowShots([p[:] for p in pts]) == want
for _ in range(600):
    pts = []
    for _ in range(random.randrange(1, 7)):
        a = random.randint(0, 8)
        pts.append([a, a + random.randint(0, 4)])
    assert _p452.findMinArrowShots([p[:] for p in pts]) == _arrows_ref(pts), pts
print("P452 OK")

emit({
 "num": 452, "slug": "minimum-number-of-arrows-to-burst-balloons",
 "en": [
   "There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array <code>points</code> where <code>points[i] = [x<sub>start</sub>, x<sub>end</sub>]</code> denotes a balloon whose <strong>horizontal diameter</strong> stretches between <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code>. You do not know the exact y-coordinates of the balloons.",
   "Arrows can be shot up <strong>directly vertically</strong> (in the positive y-direction) from different points along the x-axis. A balloon with <code>x<sub>start</sub></code> and <code>x<sub>end</sub></code> is <strong>burst</strong> by an arrow shot at <code>x</code> if <code>x<sub>start</sub> &lt;= x &lt;= x<sub>end</sub></code>. There is <strong>no limit</strong> to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.",
   "Given the array <code>points</code>, return <em>the <strong>minimum</strong> number of arrows that must be shot to burst all balloons</em>.",
 ],
 "zh": [
   "牆上貼了一些氣球，每顆氣球用 <code>[x<sub>start</sub>, x<sub>end</sub>]</code> 表示它在 x 軸上的範圍。",
   "從 x 軸上某個位置 <code>x</code> 垂直往上射一支箭，所有 <code>x<sub>start</sub> ≤ x ≤ x<sub>end</sub></code> 的氣球都會被射爆（箭會一直往上飛）。",
   "回傳射爆所有氣球需要的<strong>最少</strong>箭數。",
 ],
 "examples": """範例 1
  輸入：points = [[10,16],[2,8],[1,6],[7,12]]
  輸出：2
  說明：在 x = 6 射一支（爆 [2,8]、[1,6]），在 x = 11 射一支（爆 [10,16]、[7,12]）。

範例 2
  輸入：points = [[1,2],[3,4],[5,6],[7,8]]
  輸出：4

範例 3
  輸入：points = [[1,2],[2,3],[3,4],[4,5]]
  輸出：2
  說明：x = 2 和 x = 4（端點相接的氣球可以一起射）。""",
 "constraints": [
   "1 ≤ <code>points.length</code> ≤ 10⁵",
   "−2³¹ ≤ <code>x<sub>start</sub> &lt; x<sub>end</sub></code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【和第 435 題是同一個貪心】
    依右端點排序。
    第一顆氣球（右端點最小）一定要有一支箭射它 ——
    射在它的右端點最划算：這是能射到它的最右位置，
    可以順便射到最多後面的氣球。

    之後的氣球：
        開始位置 <= 上一支箭的位置 -> 已經被射爆
        否則 -> 需要新的一支箭，射在它的右端點

【和第 435 題的關係】
    最少箭數 = 最多能選出幾個「兩兩不重疊」的氣球。
    差別只在端點相接：這題 [1,2]、[2,3] 算重疊（一支箭射在 2 都爆）。

【溢位（其他語言）】
    座標到 ±2³¹，比較時不要用減法（a - b 可能溢位）。"""),
 ],
 "approaches": [
   ap("解法", "依右端點排序的貪心", [
     ("c", S["p452"]),
   ], "O(n log n)", "O(1)", "", "不計排序", optimal=True),
 ],
 "edges": [
   "<strong>端點相接</strong> → 一支箭可以射兩顆。",
   "<strong>全部互不重疊</strong> → n 支箭。",
   "<strong>一顆大氣球包住很多小的</strong> → 依右端點排序自然處理。",
 ],
 "follow": [
   ("h", "區間貪心整理"),
   ("c", "依右端點排序：選最多不重疊區間（435、452）。依左端點排序：合併區間（56）、插入區間（57）。"),
 ],
 "related": [
   "<strong>第 435 題 無重疊區間</strong>",
   "<strong>第 56 題 合併區間</strong>",
 ],
 "check": [
   "為什麼要射在右端點？",
   "這題和第 435 題有什麼關係？端點相接的處理有什麼不同？",
 ],
})
