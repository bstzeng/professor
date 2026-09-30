# -*- coding: utf-8 -*-
"""第 295、297、299、300 題。"""
import random
import bisect
from collections import deque, Counter
from authoring import emit, ap
from runner import Src
from lchelp import lv, ser, rand_tree

S = Src()
random.seed(295)
_DQ = {"deque": deque}


# ==================== 295. Find Median from Data Stream ====================
S["p295"] = '''class MedianFinder:
    def __init__(self):
        self.lo = []        # 較小的一半：最大堆積（存負數）
        self.hi = []        # 較大的一半：最小堆積

    def addNum(self, num: int) -> None:
        # ★ 先放進 lo，再把 lo 最大的移到 hi —— 保證 lo 的每個數 <= hi 的每個數
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):          # 維持 len(lo) == len(hi) 或 len(hi) + 1
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):          # 奇數個：中位數是 lo 的最大值
            return float(-self.lo[0])
        return (-self.lo[0] + self.hi[0]) / 2    # 偶數個：兩邊堆頂的平均'''

S["p295_sorted"] = '''class MedianFinder:
    def __init__(self):
        self.a = []                                  # 保持排序

    def addNum(self, num: int) -> None:
        bisect.insort(self.a, num)                   # 二分找位置 O(log n)，插入 O(n)

    def findMedian(self) -> float:
        n = len(self.a)
        if n % 2:
            return float(self.a[n // 2])
        return (self.a[n // 2 - 1] + self.a[n // 2]) / 2'''

for key in ("p295", "p295_sorted"):
    cls = S.loadns(key)["MedianFinder"]
    for _ in range(500):
        mf, ref = cls(), []
        for _ in range(random.randrange(1, 40)):
            x = random.randint(-20, 20)
            mf.addNum(x)
            ref.append(x)
            r = sorted(ref)
            n = len(r)
            want = r[n // 2] if n % 2 else (r[n // 2 - 1] + r[n // 2]) / 2
            assert mf.findMedian() == want, key
print("P295 OK")

_P295_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">兩個堆積把資料切成「較小的一半」和「較大的一半」</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="50" width="220" height="60" rx="6" fill="none" stroke="var(--accent)"/>
              <text x="150" y="44" fill="var(--accent)">lo：最大堆積（較小的一半）</text>
              <text x="75" y="86" fill="var(--text-muted)">1</text><text x="115" y="86" fill="var(--text-muted)">2</text>
              <text x="155" y="86" fill="var(--text-muted)">3</text>
              <rect x="190" y="66" width="56" height="30" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="218" y="86" fill="var(--accent)">5</text>
              <rect x="320" y="50" width="220" height="60" rx="6" fill="none" stroke="var(--gold)"/>
              <text x="430" y="44" fill="var(--gold)">hi：最小堆積（較大的一半）</text>
              <rect x="334" y="66" width="56" height="30" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="362" y="86" fill="var(--gold)">7</text>
              <text x="425" y="86" fill="var(--text-muted)">8</text><text x="465" y="86" fill="var(--text-muted)">9</text>
            </g>
            <text x="290" y="86" text-anchor="middle" fill="var(--text)" font-size="14">≤</text>
            <text x="218" y="132" text-anchor="middle" fill="var(--accent)" font-size="11">堆頂 = lo 的最大值</text>
            <text x="362" y="132" text-anchor="middle" fill="var(--gold)" font-size="11">堆頂 = hi 的最小值</text>
            <text x="40" y="170" fill="var(--text)" font-size="12">4 個 + 3 個（lo 多一個）→ 中位數 = lo 的堆頂 = 5</text>
            <text x="40" y="194" fill="var(--text)" font-size="12">若兩邊一樣多 → 中位數 = (lo 堆頂 + hi 堆頂) / 2</text>
            <text x="40" y="222" fill="var(--gold)" font-size="12">★ 中位數永遠在兩個堆頂上：新增 O(log n)，查詢 O(1)。</text>'''

emit({
 "num": 295, "slug": "find-median-from-data-stream",
 "en": [
   "The <strong>median</strong> is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.",
   ("ul", ["For example, for <code>arr = [2,3,4]</code>, the median is <code>3</code>.",
           "For example, for <code>arr = [2,3]</code>, the median is <code>(2 + 3) / 2 = 2.5</code>."]),
   "Implement the MedianFinder class:",
   ("ul", ["<code>MedianFinder()</code> initializes the <code>MedianFinder</code> object.",
           "<code>void addNum(int num)</code> adds the integer <code>num</code> from the data stream to the data structure.",
           "<code>double findMedian()</code> returns the median of all elements so far. Answers within <code>10<sup>-5</sup></code> of the actual answer will be accepted."]),
   "<strong>Follow up:</strong> If all integer numbers from the stream are in the range <code>[0, 100]</code>, how would you optimize your solution? "
   "If <code>99%</code> of all integer numbers from the stream are in the range <code>[0, 100]</code>, how would you optimize your solution?",
 ],
 "zh": [
   "<strong>中位數</strong>是排序後位於中間的值；個數為偶數時，是中間兩個值的平均。",
   ("ul", ["例如 <code>[2,3,4]</code> 的中位數是 <code>3</code>。",
           "例如 <code>[2,3]</code> 的中位數是 <code>(2 + 3) / 2 = 2.5</code>。"]),
   "實作 <code>MedianFinder</code> 類別：",
   ("ul", ["<code>addNum(num)</code>：從資料流加入一個整數。",
           "<code>findMedian()</code>：回傳目前所有元素的中位數（誤差 <code>10<sup>-5</sup></code> 以內都算對）。"]),
   "<strong>進階：</strong>如果所有數字都在 <code>[0, 100]</code> 之間，要怎麼優化？如果 <code>99%</code> 的數字在 <code>[0, 100]</code> 之間呢？",
 ],
 "examples": """範例
  輸入：["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]
        [[],[1],[2],[],[3],[]]
  輸出：[null,null,null,1.5,null,2.0]""",
 "constraints": [
   "−10⁵ ≤ <code>num</code> ≤ 10⁵",
   "呼叫 <code>findMedian</code> 前至少有一個元素",
   "<code>addNum</code> 與 <code>findMedian</code> 最多共呼叫 5 × 10⁴ 次",
 ],
 "idea": [
   ("fig", _P295_FIG, "0 0 640 236"),
   ("c", """【中位數只和「中間」有關】
    不需要完整排序，只要知道：
        較小一半的最大值
        較大一半的最小值

【兩個堆積】
    lo：最大堆積，存較小的一半（Python 用負數模擬）
    hi：最小堆積，存較大的一半
    維持兩個不變量：
        1. lo 的每個數 <= hi 的每個數
        2. len(lo) == len(hi) 或 len(hi) + 1

【加入一個數】
    先推進 lo，再把 lo 的最大值移到 hi ——
        這一步保證不變量 1（新數字經過「篩選」）
    如果 hi 比 lo 多，把 hi 的最小值移回 lo ——
        保證不變量 2

【查詢】
    奇數個：lo 的堆頂
    偶數個：兩個堆頂的平均"""),
 ],
 "approaches": [
   ap("解法一", "維持排序陣列", [
     ("c", S["p295_sorted"]),
     "<code>insort</code> 二分找位置是 O(log n)，但在 list 中間插入要搬移元素，O(n)。5 × 10⁴ 次操作在 Python 中其實還算快（搬移是 C 層級的記憶體複製）。",
   ], "新增 O(n)，查詢 O(1)", "O(n)", "", ""),

   ap("解法二", "兩個堆積", [
     ("c", S["p295"]),
   ], "新增 O(log n)，查詢 O(1)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "addNum", "findMedian"],
   [["一、排序陣列", "O(n)", "O(1)"],
    ["二、兩個堆積", "O(log n)", "O(1) ✔"]]),
 "edges": [
   "<strong>只有一個元素</strong> → lo 有一個，hi 空的，回傳 lo 堆頂。",
   "<strong>重複值</strong> → 不影響。",
   "<strong>負數</strong> → 最大堆積存負數時要注意正負號，取出時再取負。",
   "<strong>回傳浮點數</strong> → Python 的 <code>/</code> 本來就是浮點除法。",
 ],
 "follow": [
   ("h", "進階一：所有數都在 [0, 100]"),
   ("c", "用 101 格的計數陣列，addNum O(1)；findMedian 從頭累加計數找到中間位置，O(101) = O(1)。"),
   ("h", "進階二：99% 在 [0, 100]"),
   ("c", "計數陣列處理 [0, 100]，另外兩個串列（或堆積）存小於 0 和大於 100 的少數例外。中位數幾乎一定落在計數陣列裡，極少數情況才去看例外。"),
   ("h", "延伸：滑動視窗的中位數？"),
   ("c", "第 480 題：還要支援「刪除」——兩個堆積加上延遲刪除，或用有序集合。"),
 ],
 "related": [
   "<strong>第 480 題 滑動視窗中位數</strong>",
   "<strong>第 4 題 尋找兩個正序陣列的中位數</strong>",
   "<strong>第 502 題 IPO</strong> —— 兩個堆積",
 ],
 "check": [
   "兩個堆積分別存什麼？為什麼一個是最大堆積、一個是最小堆積？",
   "加入新數字時，為什麼要先推進 lo 再移一個到 hi？",
   "兩個堆積的大小要維持什麼關係？",
 ],
})


# ==================== 297. Serialize and Deserialize Binary Tree ====================
S["p297_pre"] = '''class Codec:
    def serialize(self, root):
        out = []

        def dfs(node):                       # 前序：根、左、右；空節點寫 "#"
            if node is None:
                out.append("#")
                return
            out.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(out)

    def deserialize(self, data):
        tokens = iter(data.split(","))

        def build():                         # ★ 用同樣的前序順序讀回來
            tok = next(tokens)
            if tok == "#":
                return None
            node = TreeNode(int(tok))
            node.left = build()              # 左子樹會「剛好」讀完它自己的 token
            node.right = build()
            return node

        return build()'''

S["p297_bfs"] = '''class Codec:
    def serialize(self, root):
        if root is None:
            return ""
        out, q = [], deque([root])
        while q:                                     # 層序；空節點寫 "#"
            node = q.popleft()
            if node is None:
                out.append("#")
                continue
            out.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ",".join(out)

    def deserialize(self, data):
        if not data:
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q, i = deque([root]), 1
        while q:
            node = q.popleft()
            for side in ("left", "right"):          # 依序讀出左、右孩子
                if vals[i] != "#":
                    child = TreeNode(int(vals[i]))
                    setattr(node, side, child)
                    q.append(child)
                i += 1
        return root'''

for key in ("p297_pre", "p297_bfs"):
    cls = S.loadns(key, _DQ)["Codec"]
    for vals in ([1, 2, 3, None, None, 4, 5], [], [1], [-1, None, -2, -3]):
        c = cls()
        assert ser(c.deserialize(c.serialize(lv(vals)))) == vals, (key, vals)
    for _ in range(1500):
        t = rand_tree(random.randrange(0, 30), -1000, 1000)
        c = cls()
        s = c.serialize(t)
        assert isinstance(s, str)
        assert ser(c.deserialize(s)) == ser(t)
print("P297 OK")

emit({
 "num": 297, "slug": "serialize-and-deserialize-binary-tree",
 "en": [
   "Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, "
   "or transmitted across a network connection link to be reconstructed later in the same or another computer environment.",
   "Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. "
   "You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.",
 ],
 "zh": [
   "<strong>序列化</strong>是把資料結構轉成一串字元（或位元），方便存檔或透過網路傳送，之後再<strong>反序列化</strong>還原回來。",
   "請設計一套演算法，把二元樹序列化成字串，並能從字串還原成<strong>完全相同</strong>的樹。格式由你自己決定。",
 ],
 "examples": """範例 1
  輸入：root = [1,2,3,null,null,4,5]
  輸出：[1,2,3,null,null,4,5]

範例 2
  輸入：root = []
  輸出：[]""",
 "constraints": [
   "節點數在 <code>[0, 10⁴]</code> 之間",
   "−1000 ≤ <code>Node.val</code> ≤ 1000",
 ],
 "idea": [
   ("c", """【只存前序或中序不夠 —— 要把「空節點」也寫進去】
    只有前序 [1, 2, 3]：
        1 的左孩子是 2 還是右孩子是 2？無法確定 ✘
    加上空節點標記 "#"：
        1,2,#,#,3,#,#  -> 唯一確定 ✔

【前序 + 空標記】
    serialize：根、左、右，空節點寫 "#"
    deserialize：用同一個順序讀：
        讀一個 token：
            "#" -> 回傳 None
            數字 -> 建節點，遞迴建左子樹，再遞迴建右子樹
    左子樹的遞迴會「剛好」消耗掉屬於它的所有 token，
    接下來讀到的自然就是右子樹的開頭。

【層序（BFS）+ 空標記】
    就是 LeetCode 自己用的格式 [1,2,3,null,null,4,5]。
    反序列化時用佇列，每個節點依序讀出兩個孩子。

【為什麼需要分隔符號？】
    值可能是多位數或負數（-1000）-> 用逗號分隔。"""),
   ("c", """        1
       / \\
      2   3        前序：1,2,#,#,3,4,#,#,5,#,#
         / \\       層序：1,2,3,#,#,4,5,#,#,#,#
        4   5"""),
 ],
 "approaches": [
   ap("解法一", "前序 DFS + 空節點標記", [
     ("c", S["p297_pre"]),
   ], "O(n)", "O(n)", "", "", optimal=True),

   ap("解法二", "層序 BFS + 空節點標記", [
     ("c", S["p297_bfs"]),
     "樹很深（一條鏈，一萬層）時，前序遞迴在 Python 會超過遞迴上限；層序版本沒有這個問題。",
   ], "O(n)", "O(n)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、前序", "O(n)", "O(n)", "程式最短 ✔"],
    ["二、層序", "O(n)", "O(n)", "不怕深樹"]]),
 "edges": [
   "<strong>空樹</strong> → 前序版是 \"#\"；層序版是空字串。",
   "<strong>負數、多位數</strong> → 要有分隔符號。",
   "<strong>深度一萬的鏈</strong> → 遞迴版要調高遞迴上限或改用迭代。",
 ],
 "follow": [
   ("h", "如果是 BST？"),
   ("c", "第 449 題：BST 只存前序就夠了（不用空標記）——因為值的大小就能決定左右。反序列化時帶著上下界遞迴。"),
   ("h", "只有前序 + 中序能不能還原？"),
   ("c", "可以（第 105 題），前提是值不重複。但序列化要存兩份，而且重建比較複雜；加空標記的單一遍歷更簡單。"),
 ],
 "related": [
   "<strong>第 449 題 序列化和反序列化二元搜尋樹</strong>",
   "<strong>第 105 題 從前序與中序遍歷序列構造二元樹</strong>",
   "<strong>第 331 題 驗證二元樹的前序序列化</strong>",
   "<strong>第 428 題 序列化和反序列化 N 元樹</strong>（付費）",
 ],
 "check": [
   "為什麼只存前序遍歷的值無法還原樹？",
   "前序反序列化時，為什麼遞迴建完左子樹後，下一個 token 一定屬於右子樹？",
   "什麼情況下要選層序版本？",
 ],
})


# ==================== 299. Bulls and Cows ====================
S["p299"] = '''class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = sum(a == b for a, b in zip(secret, guess))       # 位置和數字都對
        # ★ 共同的數字總數（不管位置）= 兩邊每個數字次數的最小值加總
        common = sum((Counter(secret) & Counter(guess)).values())
        return f"{bulls}A{common - bulls}B"'''

S["p299_one"] = '''class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        balance = [0] * 10          # >0：secret 多出來還沒配對的；<0：guess 多出來的
        for a, b in zip(secret, guess):
            if a == b:
                bulls += 1
                continue
            a, b = int(a), int(b)
            if balance[a] < 0:      # 之前 guess 有一個 a 在等配對
                cows += 1
            if balance[b] > 0:      # 之前 secret 有一個 b 在等配對
                cows += 1
            balance[a] += 1
            balance[b] -= 1
        return f"{bulls}A{cows}B"'''

_p299 = [S.load("p299", extra={"Counter": Counter}), S.load("p299_one")]
for s, g, want in [("1807", "7810", "1A3B"), ("1123", "0111", "1A1B"), ("1", "0", "0A0B"), ("11", "11", "2A0B")]:
    for sol in _p299:
        assert sol.getHint(s, g) == want


def _hint_ref(s, g):
    b = sum(x == y for x, y in zip(s, g))
    rs = [x for x, y in zip(s, g) if x != y]
    rg = [y for x, y in zip(s, g) if x != y]
    c = 0
    for d in set(rs):
        c += min(rs.count(d), rg.count(d))
    return f"{b}A{c}B"


for _ in range(4000):
    n = random.randrange(1, 9)
    s = "".join(random.choice("0123") for _ in range(n))
    g = "".join(random.choice("0123") for _ in range(n))
    want = _hint_ref(s, g)
    for sol in _p299:
        assert sol.getHint(s, g) == want, (s, g)
print("P299 OK")

emit({
 "num": 299, "slug": "bulls-and-cows",
 "en": [
   "You are playing the <strong>Bulls and Cows</strong> game with your friend. You write down a secret number and ask your friend to guess what the number is. "
   "When your friend makes a guess, you provide a hint with the following info:",
   ("ul", ["The number of \"bulls\", which are digits in the guess that are in the correct position.",
           "The number of \"cows\", which are digits in the guess that are in your secret number but are located in the wrong position. "
           "Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls."]),
   "Given the secret number <code>secret</code> and your friend's guess <code>guess</code>, return <em>the hint for your friend's guess</em>.",
   "The hint should be formatted as <code>\"xAyB\"</code>, where <code>x</code> is the number of bulls and <code>y</code> is the number of cows. "
   "Note that both <code>secret</code> and <code>guess</code> may contain duplicate digits.",
 ],
 "zh": [
   "你和朋友玩<strong>猜數字</strong>（1A2B）遊戲。你寫下一個秘密數字，朋友來猜，你要給出提示：",
   ("ul", ["<strong>A（公牛）</strong>：數字和位置都猜對的個數。",
           "<strong>B（母牛）</strong>：數字有出現、但位置不對的個數——也就是扣掉 A 之後，重新排列可以變成 A 的數字個數。"]),
   "給你 <code>secret</code> 和 <code>guess</code>，回傳 <code>\"xAyB\"</code> 格式的提示。",
   "注意：兩個字串都<strong>可能有重複的數字</strong>。",
 ],
 "examples": """範例 1
  輸入：secret = "1807", guess = "7810"
  輸出："1A3B"
  說明：8 位置正確（A）；1、7、0 有出現但位置不對（B）。

範例 2
  輸入：secret = "1123", guess = "0111"
  輸出："1A1B"
  說明：第二位的 1 位置正確；guess 剩下的兩個 1 中，
        只有一個能和 secret 剩下的 1 配對。""",
 "constraints": [
   "1 ≤ <code>secret.length, guess.length</code> ≤ 1000",
   "<code>secret.length == guess.length</code>",
   "兩者都只包含數字",
 ],
 "idea": [
   ("c", """【A：逐位置比對】

【B：重複數字是陷阱】
    secret = "1123", guess = "0111"
    位置 1 的 1 是 A。
    剩下：secret 有 1 個 1（位置 0），guess 有 2 個 1（位置 2、3）
    -> 只能配對 1 次 -> B = 1（不是 2）

【公式】
    兩個字串「共同的數字」總數（不管位置）：
        對每個數字 d，取 min(secret 裡 d 的個數, guess 裡 d 的個數)，加總
    這個總數包含了 A（位置對的當然也是共同的）
    所以 B = 共同總數 - A

    Python：Counter(a) & Counter(b) 就是逐項取最小值。

【一趟掃描的做法】
    balance[d] > 0：secret 有多出來的 d 在等配對
    balance[d] < 0：guess 有多出來的 d 在等配對
    每次遇到不是 A 的位置，看看能不能和之前「在等」的配對。"""),
 ],
 "approaches": [
   ap("解法一", "計數：共同數字 − A", [
     ("c", S["p299"]),
   ], "O(n)", "O(1)", "", "只有 10 種數字", optimal=True),

   ap("解法二", "一趟掃描", [
     ("c", S["p299_one"]),
   ], "O(n)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、計數", "O(n)", "O(1)", "最直觀 ✔"],
    ["二、一趟", "O(n)", "O(1)", "只掃一次"]]),
 "edges": [
   "<strong>全部猜中</strong> → \"nA0B\"。",
   "<strong>完全不相交</strong> → \"0A0B\"。",
   "<strong>重複數字</strong> → 每個數字只能被配對一次。",
 ],
 "follow": [
   ("h", "延伸：如何「猜」出秘密數字？"),
   ("c", "4 位不重複數字共 5040 種；每次選一個猜測，根據回覆排除不可能的候選。Knuth 證明了猜 Mastermind（類似遊戲）最多 5 次就能猜中——用 minimax 選擇最壞情況下剩最少候選的猜測。"),
 ],
 "related": [
   "<strong>第 242 題 有效的字母異位詞</strong> —— 計數",
   "<strong>第 350 題 兩個陣列的交集 II</strong> —— 次數取最小值",
 ],
 "check": [
   "為什麼 B 不能直接數「guess 中有出現在 secret 的數字」？",
   "共同數字總數怎麼算？為什麼要減掉 A？",
 ],
})


# ==================== 300. Longest Increasing Subsequence ====================
S["p300_dp"] = '''class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n                   # dp[i]：以 nums[i]「結尾」的最長遞增子序列長度
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:  # nums[i] 可以接在 nums[j] 後面
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)'''

S["p300_bs"] = '''class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []    # tails[k]：長度 k+1 的遞增子序列中，最小可能的結尾
        for x in nums:
            i = bisect.bisect_left(tails, x)     # 第一個 >= x 的位置
            if i == len(tails):
                tails.append(x)                   # x 比所有結尾都大：延長
            else:
                tails[i] = x                      # ★ 讓長度 i+1 的結尾變得更小
        return len(tails)'''

S["p300_path"] = '''class Solution:
    def findLIS(self, nums: List[int]) -> List[int]:        # 回傳一個最長遞增子序列本身
        tails, tails_idx = [], []    # 結尾的值、以及它在 nums 中的索引
        prev = [-1] * len(nums)      # prev[i]：以 nums[i] 結尾的序列中，前一個元素的索引
        for i, x in enumerate(nums):
            k = bisect.bisect_left(tails, x)
            if k:
                prev[i] = tails_idx[k - 1]
            if k == len(tails):
                tails.append(x)
                tails_idx.append(i)
            else:
                tails[k], tails_idx[k] = x, i
        seq, i = [], tails_idx[-1]   # 從最長序列的結尾往回追
        while i != -1:
            seq.append(nums[i])
            i = prev[i]
        return seq[::-1]'''

_p300 = [S.load(x) for x in ("p300_dp", "p300_bs")]
_p300p = S.load("p300_path")
for nums, want in [([10, 9, 2, 5, 3, 7, 101, 18], 4), ([0, 1, 0, 3, 2, 3], 4), ([7, 7, 7, 7, 7, 7, 7], 1), ([5], 1)]:
    for sol in _p300:
        assert sol.lengthOfLIS(nums) == want
for _ in range(3000):
    nums = [random.randint(-5, 10) for _ in range(random.randrange(1, 14))]
    a, b = (sol.lengthOfLIS(nums) for sol in _p300)
    assert a == b
    seq = _p300p.findLIS(nums)
    assert len(seq) == a and all(x < y for x, y in zip(seq, seq[1:]))
    it = iter(nums)
    assert all(any(v == w for w in it) for v in seq)        # 是子序列
print("P300 OK")

_P300_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">tails：每個長度「最小的結尾」—— nums = [10, 9, 2, 5, 3, 7, 101, 18]</text>
            <g font-size="12">
              <text x="30" y="52" fill="var(--text-muted)">讀入</text><text x="100" y="52" fill="var(--text-muted)">tails</text><text x="330" y="52" fill="var(--text-muted)">動作</text>
              <text x="30" y="76" fill="var(--text)">10</text><text x="100" y="76" fill="var(--text)">[10]</text><text x="330" y="76" fill="var(--text-muted)">延長</text>
              <text x="30" y="98" fill="var(--text)">9</text><text x="100" y="98" fill="var(--text)">[9]</text><text x="330" y="98" fill="var(--accent)">替換：長度 1 的最小結尾 10 → 9</text>
              <text x="30" y="120" fill="var(--text)">2</text><text x="100" y="120" fill="var(--text)">[2]</text><text x="330" y="120" fill="var(--accent)">替換</text>
              <text x="30" y="142" fill="var(--text)">5</text><text x="100" y="142" fill="var(--text)">[2, 5]</text><text x="330" y="142" fill="var(--text-muted)">延長</text>
              <text x="30" y="164" fill="var(--text)">3</text><text x="100" y="164" fill="var(--text)">[2, 3]</text><text x="330" y="164" fill="var(--accent)">替換：長度 2 的最小結尾 5 → 3</text>
              <text x="30" y="186" fill="var(--text)">7</text><text x="100" y="186" fill="var(--text)">[2, 3, 7]</text><text x="330" y="186" fill="var(--text-muted)">延長</text>
              <text x="30" y="208" fill="var(--text)">101</text><text x="100" y="208" fill="var(--text)">[2, 3, 7, 101]</text><text x="330" y="208" fill="var(--text-muted)">延長</text>
              <text x="30" y="230" fill="var(--text)">18</text><text x="100" y="230" fill="var(--gold)">[2, 3, 7, 18]</text><text x="330" y="230" fill="var(--accent)">替換：101 → 18</text>
            </g>
            <text x="20" y="262" fill="var(--gold)" font-size="12">★ 答案 = tails 的長度 = 4。注意 tails 本身不一定是一個真的子序列，只有長度是對的。</text>'''

emit({
 "num": 300, "slug": "longest-increasing-subsequence",
 "en": [
   "Given an integer array <code>nums</code>, return <em>the length of the longest <strong>strictly increasing subsequence</strong></em>.",
   "A <strong>subsequence</strong> is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.",
   "<strong>Follow up:</strong> Can you come up with an algorithm that runs in <code>O(n log(n))</code> time complexity?",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，回傳<strong>最長嚴格遞增子序列</strong>的長度。",
   "<strong>子序列</strong>是從原陣列刪除一些（或不刪）元素、但不改變剩下元素順序所得到的序列。",
   "<strong>進階：</strong>能設計出 <code>O(n log n)</code> 的演算法嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [10,9,2,5,3,7,101,18]
  輸出：4
  說明：最長遞增子序列之一是 [2,3,7,101]。

範例 2
  輸入：nums = [0,1,0,3,2,3]
  輸出：4

範例 3
  輸入：nums = [7,7,7,7,7,7,7]
  輸出：1""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 2500",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【方法一：DP，O(n²)】
    dp[i] = 以 nums[i] 結尾的 LIS 長度
    dp[i] = 1 + max(dp[j])，對所有 j < i 且 nums[j] < nums[i]
    答案 = max(dp)（不是 dp[n-1]！LIS 不一定以最後一個元素結尾）

【方法二：貪心 + 二分，O(n log n)】
    直覺：同樣長度的遞增子序列，結尾越小越好 ——
    越小的結尾，後面越容易接上新元素。

    tails[k] = 長度 k+1 的遞增子序列中，最小的結尾
    tails 一定是嚴格遞增的（長度更長的，結尾一定更大）

    讀入 x：
        x 比所有 tails 都大 -> 接在最長的後面，tails 延長
        否則找第一個 >= x 的 tails[i]，換成 x
            （長度 i+1 的子序列現在可以用更小的 x 結尾）

    為什麼是 bisect_left（第一個 >= x）？
        嚴格遞增：x 不能接在等於 x 的結尾後面，
        所以要替換掉「等於 x」的那一格，而不是延長。"""),
   ("fig", _P300_FIG, "0 0 640 276"),
 ],
 "approaches": [
   ap("解法一", "動態規劃", [
     ("c", S["p300_dp"]),
   ], "O(n²)", "O(n)", "", ""),

   ap("解法二", "貪心 + 二分搜尋（耐心排序）", [
     ("c", S["p300_bs"]),
     ("c", """【耐心排序（Patience Sorting）】
    把牌依序放成好幾堆：每張牌放在「最左邊、堆頂 >= 它」的那一堆上，
    沒有這樣的堆就開新的一堆。
    最後的堆數 = LIS 長度。tails 就是每一堆的堆頂。"""),
   ], "O(n log n)", "O(n)", "", "", optimal=True),

   ap("延伸", "還原出一個實際的 LIS", [
     ("c", S["p300_path"]),
     "tails 本身不是答案序列。要還原，就記下每個元素在序列中的「前一個元素」，最後從最長序列的結尾往回追。",
   ], "O(n log n)", "O(n)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、DP", "O(n²)", "O(n)", "好理解、好擴充"],
    ["二、貪心 + 二分", "O(n log n)", "O(n)", "最快 ✔"]]),
 "edges": [
   "<strong>全部相同</strong> → 1（嚴格遞增）。",
   "<strong>嚴格遞減</strong> → 1。",
   "<strong>只有一個元素</strong> → 1。",
   "<strong>非嚴格遞增</strong>（允許相等）→ 把 <code>bisect_left</code> 換成 <code>bisect_right</code>。",
 ],
 "follow": [
   ("h", "LIS 的變化題"),
   ("c", """第 673 題：LIS 的個數（DP 多記一個 count）。
第 354 題：俄羅斯套娃信封——先依寬度遞增、同寬度依高度遞減排序，再對高度做 LIS。
第 1964 題：每個位置的最長障礙賽路線——非嚴格 LIS，用 bisect_right。"""),
 ],
 "related": [
   "<strong>第 354 題 俄羅斯套娃信封問題</strong>",
   "<strong>第 673 題 最長遞增子序列的個數</strong>",
   "<strong>第 1143 題 最長公共子序列</strong>",
   "<strong>第 334 題 遞增的三元子序列</strong> —— LIS 長度 ≥ 3 的特例",
 ],
 "check": [
   "DP 解法中，為什麼答案是 max(dp) 而不是 dp[n−1]？",
   "tails[k] 代表什麼？為什麼它一定是遞增的？",
   "為什麼用 bisect_left 而不是 bisect_right？",
   "tails 最後的內容是不是一個真的遞增子序列？",
 ],
})
