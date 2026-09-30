# -*- coding: utf-8 -*-
"""第 257、258、260、263、264、268 題。"""
import random
from authoring import emit, ap
from runner import Src
from lchelp import lv, rand_tree

S = Src()
random.seed(257)


# ==================== 257. Binary Tree Paths ====================
S["p257"] = '''class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        path = []                                  # 目前路徑上的值

        def dfs(node):
            path.append(str(node.val))
            if not node.left and not node.right:   # ★ 葉節點：一條完整的路徑
                res.append("->".join(path))
            else:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
            path.pop()                             # 回溯

        dfs(root)
        return res'''

S["p257_it"] = '''class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = [(root, str(root.val))]            # (節點, 從根到它的路徑字串)
        while stack:
            node, s = stack.pop()
            if not node.left and not node.right:
                res.append(s)
            # 先推右再推左，讓左邊先出來，順序和遞迴版相同
            if node.right:
                stack.append((node.right, s + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, s + "->" + str(node.left.val)))
        return res'''

_p257 = [S.load(x) for x in ("p257", "p257_it")]
for vals, want in [([1, 2, 3, None, 5], ["1->2->5", "1->3"]), ([1], ["1"]), ([-1, -2], ["-1->-2"])]:
    for sol in _p257:
        assert sol.binaryTreePaths(lv(vals)) == want


def _paths_ref(nd):
    if not nd.left and not nd.right:
        return [[nd.val]]
    out = []
    for c in (nd.left, nd.right):
        if c:
            out += [[nd.val] + p for p in _paths_ref(c)]
    return out


for _ in range(1500):
    t = rand_tree(random.randrange(1, 20), -9, 9)
    want = ["->".join(map(str, p)) for p in _paths_ref(t)]
    for sol in _p257:
        assert sol.binaryTreePaths(t) == want
print("P257 OK")

emit({
 "num": 257, "slug": "binary-tree-paths",
 "en": [
   "Given the <code>root</code> of a binary tree, return <em>all root-to-leaf paths in <strong>any order</strong></em>.",
   "A <strong>leaf</strong> is a node with no children.",
 ],
 "zh": [
   "給你一棵二元樹的根節點 <code>root</code>，以<strong>任意順序</strong>回傳所有「從根到葉」的路徑。",
   "<strong>葉節點</strong>是沒有任何孩子的節點。",
 ],
 "examples": """範例 1
  輸入：root = [1,2,3,null,5]
  輸出：["1->2->5","1->3"]

       1
     /   \\
    2     3
     \\
      5

範例 2
  輸入：root = [1]
  輸出：["1"]""",
 "constraints": [
   "節點數在 <code>[1, 100]</code> 之間",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "idea": [
   ("c", """【DFS + 回溯的標準題】
    從根往下走，沿路把值放進 path。
    走到葉節點 -> path 就是一條完整路徑，存起來。
    離開節點時把它從 path 移除（回溯），
    讓兄弟節點能繼續使用同一個 path。

【判斷葉節點】
    左右孩子都是 None。
    只有一個孩子的節點不是葉 -> 不能在那裡結束。
    （如果改成「走到 None 就存」，範例 1 的節點 2 會多產生一條 "1->2" ✘）

【字串 vs 串列】
    每層都 path + "->" + val 產生新字串：寫法簡單，
    但每次複製 O(路徑長) -> 總共 O(n · h)。
    用串列 append / pop，只在葉節點 join 一次：比較省。"""),
 ],
 "approaches": [
   ap("解法一", "遞迴 DFS + 回溯", [
     ("c", S["p257"]),
   ], "O(n · h)", "O(h)", "每條路徑 join 一次", "不計輸出", optimal=True),

   ap("解法二", "迭代 DFS（堆疊存路徑字串）", [
     ("c", S["p257_it"]),
     "每個堆疊元素自帶一份到目前為止的路徑字串，不需要回溯。",
   ], "O(n · h)", "O(n · h)", "", "堆疊裡的字串"),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、遞迴 + 回溯", "O(n·h)", "O(h) ✔"],
    ["二、迭代", "O(n·h)", "O(n·h)"]]),
 "edges": [
   "<strong>只有根</strong> → <code>[\"1\"]</code>，沒有箭頭。",
   "<strong>負數</strong> → <code>\"-1->-2\"</code>，照樣轉字串。",
   "<strong>只有一個孩子的節點</strong> → 不是葉節點，不能在那裡產生路徑。",
 ],
 "follow": [
   ("h", "同一個骨架的變化"),
   ("c", "第 112 題（有沒有和為 target 的路徑）、第 113 題（列出所有和為 target 的路徑）、第 129 題（每條路徑組成一個數字再加總），都是「DFS 到葉節點」的同一個模板。"),
 ],
 "related": [
   "<strong>第 113 題 路徑總和 II</strong>",
   "<strong>第 129 題 求根節點到葉節點數字之和</strong>",
   "<strong>第 988 題 從葉結點開始的最小字串</strong>",
 ],
 "check": [
   "什麼時候把 path 存進答案？",
   "為什麼離開節點時要 pop？",
   "只有一個孩子的節點要怎麼處理？",
 ],
})


# ==================== 258. Add Digits ====================
S["p258"] = '''class Solution:
    def addDigits(self, num: int) -> int:
        # ★ 數根：10 ≡ 1 (mod 9)，所以「數字和」和原數 mod 9 相同
        if num == 0:
            return 0
        return 1 + (num - 1) % 9'''

S["p258_loop"] = '''class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(d) for d in str(num))   # 反覆加總各位數
        return num'''

_p258 = [S.load(x) for x in ("p258", "p258_loop")]
for n in list(range(0, 5000)) + [2 ** 31 - 1, 38, 999999999]:
    assert _p258[0].addDigits(n) == _p258[1].addDigits(n), n
assert _p258[0].addDigits(38) == 2
print("P258 OK")

emit({
 "num": 258, "slug": "add-digits",
 "en": [
   "Given an integer <code>num</code>, repeatedly add all its digits until the result has only one digit, and return it.",
   "<strong>Follow up:</strong> Could you do it without any loop/recursion in <code>O(1)</code> runtime?",
 ],
 "zh": [
   "給你一個非負整數 <code>num</code>，反覆把它的各位數字相加，直到結果只剩一位數，回傳這個結果。",
   "<strong>進階：</strong>能不用迴圈或遞迴，在 <code>O(1)</code> 時間內完成嗎？",
 ],
 "examples": """範例 1
  輸入：num = 38
  輸出：2
  說明：3 + 8 = 11，1 + 1 = 2

範例 2
  輸入：num = 0
  輸出：0""",
 "constraints": [
   "0 ≤ <code>num</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【為什麼數字和和 mod 9 有關？】
    10 = 9 + 1 ≡ 1 (mod 9)
    100 = 99 + 1 ≡ 1 (mod 9)
    所以 abc = 100a + 10b + c ≡ a + b + c (mod 9)

    「加總各位數」不會改變 mod 9 的值！
    反覆做下去，最後剩一位數 d（1..9），而 d ≡ num (mod 9)。

【對應關係】
    num mod 9 = 1..8 -> 答案就是 1..8
    num mod 9 = 0    -> 答案是 9（num > 0 時）
    num = 0          -> 答案 0

    合併寫法：1 + (num - 1) % 9（num > 0）

【這叫做「數根」(digital root)】
    小學的「棄九法」驗算乘法也是這個原理：
    a × b = c  =>  數根(a) × 數根(b) 的數根 = 數根(c)"""),
   ("t", ["num", "38", "18", "9", "10", "0"],
    [["num mod 9", "2", "0", "0", "1", "0"],
     ["數根", "2", "9", "9", "1", "0"]]),
 ],
 "approaches": [
   ap("解法一", "模擬", [
     ("c", S["p258_loop"]),
   ], "O(log n)", "O(1)", "數字和很快就變小", ""),

   ap("解法二", "數根公式", [
     ("c", S["p258"]),
   ], "O(1)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、模擬", "O(log n)", "O(1)"],
    ["二、公式", "O(1)", "O(1) ✔"]]),
 "edges": [
   "<strong>num = 0</strong> → 0（公式要特判）。",
   "<strong>9 的倍數</strong> → 9，不是 0。",
   "<strong>個位數</strong> → 本身。",
 ],
 "follow": [
   ("h", "推廣到其他進位"),
   ("c", "b 進位的數根：1 + (num − 1) % (b − 1)。因為 b ≡ 1 (mod b−1)。"),
 ],
 "related": [
   "<strong>第 202 題 快樂數</strong> —— 反覆做「各位數平方和」",
   "<strong>第 1945 題 字串轉換後的各位數字之和</strong>",
 ],
 "check": [
   "為什麼加總各位數不會改變 mod 9 的值？",
   "num 是 9 的倍數時答案是多少？",
 ],
})


# ==================== 260. Single Number III ====================
S["p260"] = '''class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x                    # 出現兩次的都抵銷 -> xor = a ^ b（a != b，所以不為 0）
        low = xor & -xor                # ★ a、b 在這一位不同：一個是 1、一個是 0
        a = 0
        for x in nums:
            if x & low:                 # 依這一位分成兩組，a、b 各在一組
                a ^= x                  # 同一組內其他數字都成對 -> 剩下 a
        return [a, xor ^ a]'''

S["p260_hash"] = '''class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        return [x for x, c in cnt.items() if c == 1]'''

_p260 = [S.load(x) for x in ("p260", "p260_hash")]
for _ in range(3000):
    pool = random.sample(range(-2 ** 31, 2 ** 31) if random.random() < 0.3 else range(-10, 10), random.randrange(2, 8))
    a, b = pool[0], pool[1]
    nums = [a, b] + pool[2:] * 2
    random.shuffle(nums)
    for sol in _p260:
        assert sorted(sol.singleNumber(nums)) == sorted([a, b]), (nums, sol)
print("P260 OK")

_P260_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">nums = [1, 2, 1, 3, 2, 5]，答案 a = 3、b = 5</text>
            <g font-family="monospace" font-size="14">
              <text x="40" y="56" fill="var(--text-muted)">a = 3 =</text><text x="150" y="56" fill="var(--accent)">0 1 1</text>
              <text x="40" y="80" fill="var(--text-muted)">b = 5 =</text><text x="150" y="80" fill="var(--gold)">1 0 1</text>
              <line x1="150" y1="88" x2="200" y2="88" stroke="var(--border)"/>
              <text x="40" y="106" fill="var(--text-muted)">a ^ b =</text><text x="150" y="106" fill="var(--text)">1 1 0</text>
              <text x="40" y="132" fill="var(--text-muted)">lowbit =</text><text x="150" y="132" fill="#ff8a65">0 1 0</text>
            </g>
            <text x="240" y="106" fill="var(--text)" font-size="12">全部 XOR 起來：成對的抵銷，只剩 a ^ b</text>
            <text x="240" y="132" fill="#ff8a65" font-size="12">取最低位的 1：a、b 在這一位一定不同</text>
            <text x="40" y="170" fill="var(--text)" font-size="12">依這一位（第 1 位）分組：</text>
            <text x="60" y="194" fill="var(--accent)" font-size="12">是 1：2, 3, 2 → XOR = 3 = a</text>
            <text x="60" y="216" fill="var(--gold)" font-size="12">是 0：1, 1, 5 → XOR = 5 = b</text>
            <text x="330" y="194" fill="var(--text-muted)" font-size="12">成對的數字一定分在同一組，</text>
            <text x="330" y="216" fill="var(--text-muted)" font-size="12">所以每一組又變回第 136 題。</text>'''

emit({
 "num": 260, "slug": "single-number-iii",
 "en": [
   "Given an integer array <code>nums</code>, in which exactly two elements appear only once and all the other elements appear exactly twice. "
   "Find the two elements that appear only once. You can return the answer in <strong>any order</strong>.",
   "You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，其中<strong>恰好有兩個</strong>元素只出現一次，其他元素都恰好出現兩次。找出這兩個只出現一次的元素，順序不限。",
   "必須在線性時間內完成，而且只能使用常數額外空間。",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,1,3,2,5]
  輸出：[3,5]

範例 2
  輸入：nums = [-1,0]
  輸出：[-1,0]

範例 3
  輸入：nums = [0,1]
  輸出：[1,0]""",
 "constraints": [
   "2 ≤ <code>nums.length</code> ≤ 3 × 10⁴",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
   "恰好有兩個整數只出現一次，其餘都出現兩次",
 ],
 "idea": [
   ("fig", _P260_FIG, "0 0 640 230"),
   ("c", """【第 136 題：只有一個出現一次】
    全部 XOR：x ^ x = 0，剩下的就是答案。

【兩個出現一次：全部 XOR 只能得到 a ^ b】
    怎麼把 a、b 分開？

【關鍵：a != b，所以 a ^ b 至少有一個位元是 1】
    那一位上，a 和 b 一個是 1、一個是 0。
    用這一位把所有數字分成兩組：
        - a、b 一定在不同組
        - 相同的數字這一位也相同 -> 一定在同一組，照樣抵銷
    每一組各自 XOR -> 分別得到 a 和 b ✔

【取哪一位？任何一個 1 都可以，最方便的是最低位】
    low = xor & -xor

【Python 的負數】
    Python 整數沒有位數限制，-x 的「二補數」是無限長的，
    xor & -xor 對負數 xor 依然只留下最低位的 1 ✔
    （C++ 要注意 xor = INT_MIN 時 -xor 會溢位。）"""),
 ],
 "approaches": [
   ap("解法一", "雜湊計數", [
     ("c", S["p260_hash"]),
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "XOR 分組", [
     ("c", S["p260"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、雜湊", "O(n)", "O(n)"],
    ["二、XOR 分組", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>其中一個是 0</strong> → 沒問題，0 在分組位元上是 0。",
   "<strong>負數</strong> → Python 的 <code>&amp;</code> 對負數照常運作。",
   "<strong>長度 2</strong> → 兩個數本身就是答案。",
 ],
 "follow": [
   ("h", "Single Number 系列"),
   ("c", """第 136 題：其他出現 2 次，找 1 個 → XOR。
第 137 題：其他出現 3 次，找 1 個 → 每一位的 1 的個數 mod 3。
第 260 題：其他出現 2 次，找 2 個 → XOR 後用一個不同的位元分組。"""),
 ],
 "related": [
   "<strong>第 136 題 只出現一次的數字</strong>",
   "<strong>第 137 題 只出現一次的數字 II</strong>",
   "<strong>第 268 題 遺失的數字</strong> —— 同樣可以用 XOR",
 ],
 "check": [
   "全部 XOR 之後得到什麼？",
   "為什麼 a ^ b 一定有某一位是 1？",
   "依照那一位分組後，為什麼成對的數字不會被拆開？",
 ],
})


# ==================== 263. Ugly Number ====================
S["p263"] = '''class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:                       # 醜數必須是正整數
            return False
        for p in (2, 3, 5):
            while n % p == 0:            # ★ 把 2、3、5 的因數全部除掉
                n //= p
        return n == 1                    # 剩下 1 = 沒有其他質因數'''

_p263 = S.load("p263")


def _ugly_ref(n):
    if n <= 0:
        return False
    d, m = 2, n
    while d * d <= m:
        while m % d == 0:
            if d not in (2, 3, 5):
                return False
            m //= d
        d += 1
    return m in (1, 2, 3, 5)


for n in list(range(-50, 20000)) + [2 ** 31 - 1, -2 ** 31, 2 ** 30, 3 ** 19]:
    assert _p263.isUgly(n) == _ugly_ref(n), n
print("P263 OK")

emit({
 "num": 263, "slug": "ugly-number",
 "en": [
   "An <strong>ugly number</strong> is a <em>positive</em> integer which does not have a prime factor other than 2, 3, and 5.",
   "Given an integer <code>n</code>, return <code>true</code> if <code>n</code> is an <strong>ugly number</strong>.",
 ],
 "zh": [
   "<strong>醜數</strong>是指質因數只包含 2、3、5 的<em>正</em>整數。",
   "給你一個整數 <code>n</code>，判斷它是不是醜數。",
 ],
 "examples": """範例 1
  輸入：n = 6
  輸出：true
  說明：6 = 2 × 3

範例 2
  輸入：n = 1
  輸出：true
  說明：1 沒有任何質因數，所以符合「只有 2、3、5」。

範例 3
  輸入：n = 14
  輸出：false
  說明：14 有質因數 7。""",
 "constraints": [
   "−2³¹ ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【把允許的質因數除乾淨】
    n = 2^a × 3^b × 5^c × (其他)
    把 2、3、5 全部除掉之後，
        剩下 1   -> 沒有其他質因數 -> 醜數 ✔
        剩下 > 1 -> 有 7、11、... 之類的因數 ✘

【邊界】
    n <= 0 -> 不是（醜數必須是正整數）
            而且 n = 0 會讓 while n % 2 == 0 無窮迴圈！
    n = 1  -> 是（空的質因數分解）"""),
 ],
 "approaches": [
   ap("解法", "反覆除以 2、3、5", [
     ("c", S["p263"]),
   ], "O(log n)", "O(1)", "每次除法 n 至少減半", "", optimal=True),
 ],
 "edges": [
   "<strong>n = 0</strong> → false；沒有先判斷會陷入無窮迴圈。",
   "<strong>負數</strong> → false。",
   "<strong>n = 1</strong> → true。",
   "<strong>大質數</strong>（例如 2³¹ − 1）→ 一次都除不掉，剩下自己，false。",
 ],
 "follow": [
   ("h", "追問：第 n 個醜數？"),
   ("c", "第 264 題：不要一個一個判斷（醜數越來越稀疏），改成用三個指標直接「產生」醜數。"),
 ],
 "related": [
   "<strong>第 264 題 醜數 II</strong>",
   "<strong>第 313 題 超級醜數</strong>",
   "<strong>第 1201 題 醜數 III</strong>",
 ],
 "check": [
   "為什麼除完 2、3、5 之後剩下 1 就是醜數？",
   "n = 0 時如果沒有先判斷，會發生什麼事？",
 ],
})


# ==================== 264. Ugly Number II ====================
S["p264"] = '''class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1]
        i2 = i3 = i5 = 0                   # 三個指標：下一個要乘 2 / 3 / 5 的醜數位置
        while len(ugly) < n:
            a, b, c = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            nxt = min(a, b, c)
            ugly.append(nxt)
            # ★ 所有產生出 nxt 的指標都要前進（例如 6 = 2×3 = 3×2），才不會重複
            if nxt == a:
                i2 += 1
            if nxt == b:
                i3 += 1
            if nxt == c:
                i5 += 1
        return ugly[-1]'''

S["p264_heap"] = '''class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap, seen = [1], {1}
        for _ in range(n - 1):
            x = heapq.heappop(heap)           # 目前最小的醜數
            for p in (2, 3, 5):
                if x * p not in seen:          # 去重
                    seen.add(x * p)
                    heapq.heappush(heap, x * p)
        return heap[0]'''

_p264 = [S.load(x) for x in ("p264", "p264_heap")]
_ug = [x for x in range(1, 5000) if _p263.isUgly(x)]
for n in range(1, len(_ug) + 1):
    for sol in _p264:
        assert sol.nthUglyNumber(n) == _ug[n - 1], n
assert _p264[0].nthUglyNumber(1690) == _p264[1].nthUglyNumber(1690) == 2123366400
print("P264 OK")

_P264_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">三個指標合併三條「醜數 × 2 / × 3 / × 5」的有序序列</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="40" width="40" height="30" fill="none" stroke="var(--text-muted)"/><text x="60" y="60" fill="var(--text)">1</text>
              <rect x="80" y="40" width="40" height="30" fill="none" stroke="var(--text-muted)"/><text x="100" y="60" fill="var(--text)">2</text>
              <rect x="120" y="40" width="40" height="30" fill="none" stroke="var(--text-muted)"/><text x="140" y="60" fill="var(--text)">3</text>
              <rect x="160" y="40" width="40" height="30" fill="none" stroke="var(--text-muted)"/><text x="180" y="60" fill="var(--text)">4</text>
              <rect x="200" y="40" width="40" height="30" fill="none" stroke="var(--text-muted)"/><text x="220" y="60" fill="var(--text)">5</text>
              <rect x="240" y="40" width="40" height="30" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="260" y="60" fill="#ff8a65">?</text>
            </g>
            <g font-size="11" text-anchor="middle">
              <text x="140" y="88" fill="var(--accent)">↑ i2</text>
              <text x="100" y="88" fill="var(--gold)">↑ i3</text>
              <text x="100" y="104" fill="#8e7cc3">i5</text>
            </g>
            <text x="320" y="50" fill="var(--accent)" font-size="12">ugly[i2] × 2 = 3 × 2 = 6</text>
            <text x="320" y="72" fill="var(--gold)" font-size="12">ugly[i3] × 3 = 2 × 3 = 6</text>
            <text x="320" y="94" fill="#8e7cc3" font-size="12">ugly[i5] × 5 = 2 × 5 = 10</text>
            <text x="20" y="136" fill="var(--text)" font-size="12">（i2 已經用過 1、2 產生 2、4；i3 用過 1 產生 3；i5 用過 1 產生 5。）</text>
            <text x="20" y="160" fill="var(--text)" font-size="12">下一個 = min(6, 6, 10) = 6，而且 6 同時由 i2、i3 產生 → 兩個指標都要前進，避免 6 重複。</text>
            <text x="20" y="190" fill="var(--gold)" font-size="12">★ 每個醜數的 ×2、×3、×5 都會被考慮到；每次取最小，就能依序產生所有醜數。</text>'''

emit({
 "num": 264, "slug": "ugly-number-ii",
 "en": [
   "An <strong>ugly number</strong> is a positive integer whose prime factors are limited to <code>2</code>, <code>3</code>, and <code>5</code>.",
   "Given an integer <code>n</code>, return <em>the</em> <code>n<sup>th</sup></code> <em><strong>ugly number</strong></em>.",
 ],
 "zh": [
   "<strong>醜數</strong>是質因數只包含 <code>2</code>、<code>3</code>、<code>5</code> 的正整數。",
   "給你整數 <code>n</code>，回傳第 <code>n</code> 個醜數。",
 ],
 "examples": """範例 1
  輸入：n = 10
  輸出：12
  說明：前 10 個醜數是 [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]

範例 2
  輸入：n = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 1690",
 ],
 "idea": [
   ("c", """【不要逐一檢查每個整數】
    第 1690 個醜數是 2,123,366,400 ——
    逐一判斷要檢查二十多億個數 ✘

【直接「產生」醜數】
    除了 1 以外，每個醜數都是某個更小的醜數 × 2、× 3 或 × 5。
    所以醜數序列 = 1 + 三條序列的合併：
        ugly × 2：2, 4, 6, 8, 10, ...
        ugly × 3：3, 6, 9, 12, 15, ...
        ugly × 5：5, 10, 15, 20, 25, ...
    這三條本身都是遞增的 -> 用三個指標做多路合併（像合併 k 個有序串列）。

【去重】
    6 = 2 × 3 = 3 × 2，會同時出現在兩條序列中。
    取出最小值後，所有「等於它」的指標都要前進 ->
    用三個獨立的 if，不能用 elif ✘"""),
   ("fig", _P264_FIG, "0 0 640 208"),
 ],
 "approaches": [
   ap("解法一", "最小堆積 + 集合去重", [
     ("c", S["p264_heap"]),
     "每次取出最小的醜數 x，把 2x、3x、5x 放進堆積。用集合避免重複放入。",
   ], "O(n log n)", "O(n)", "", ""),

   ap("解法二", "三指標 DP", [
     ("c", S["p264"]),
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、堆積", "O(n log n)", "O(n)"],
    ["二、三指標", "O(n)", "O(n) ✔"]]),
 "edges": [
   "<strong>n = 1</strong> → 1。",
   "<strong>重複值</strong>（6、10、15、30…）→ 所有相等的指標都要前進。",
   "<strong>n = 1690</strong> → 2,123,366,400，超過 32 位元有號整數上限（其他語言用 long）。",
 ],
 "follow": [
   ("h", "推廣：質因數集合是任意給定的 k 個質數？"),
   ("c", "第 313 題「超級醜數」：k 個指標，每一步取 k 個候選的最小值，O(nk)；或用堆積 O(n log k)。"),
 ],
 "related": [
   "<strong>第 263 題 醜數</strong>",
   "<strong>第 313 題 超級醜數</strong>",
   "<strong>第 23 題 合併 K 個排序鏈結串列</strong> —— 多路合併",
 ],
 "check": [
   "為什麼每個醜數（除了 1）都是更小的醜數乘以 2、3 或 5？",
   "三個指標各自代表什麼？",
   "為什麼要用三個獨立的 if，而不是 if / elif？",
 ],
})


# ==================== 268. Missing Number ====================
S["p268_sum"] = '''class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)     # ★ 0+1+...+n 減掉實際總和'''

S["p268_xor"] = '''class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)                          # 先放 n（索引只到 n-1）
        for i, x in enumerate(nums):
            res ^= i ^ x                         # 索引 0..n-1 和值配對抵銷
        return res'''

S["p268_set"] = '''class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set(nums)
        for x in range(len(nums) + 1):
            if x not in s:
                return x'''

S["p268_sort"] = '''class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        lo, hi = 0, len(nums)                    # 找第一個 nums[i] != i 的位置
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == mid:
                lo = mid + 1
            else:
                hi = mid
        return lo'''

_p268 = [S.load(x) for x in ("p268_sum", "p268_xor", "p268_set", "p268_sort")]
for _ in range(3000):
    n = random.randrange(1, 30)
    miss = random.randrange(0, n + 1)
    nums = [x for x in range(n + 1) if x != miss]
    random.shuffle(nums)
    for sol in _p268:
        assert sol.missingNumber(list(nums)) == miss
print("P268 OK")

emit({
 "num": 268, "slug": "missing-number",
 "en": [
   "Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return <em>the only number in the range that is missing from the array.</em>",
   "<strong>Follow up:</strong> Could you implement a solution using only <code>O(1)</code> extra space complexity and <code>O(n)</code> runtime complexity?",
 ],
 "zh": [
   "給你一個陣列 <code>nums</code>，包含 <code>[0, n]</code> 範圍內 <code>n</code> 個<strong>互不相同</strong>的數字，找出範圍內唯一缺少的那個數。",
   "<strong>進階：</strong>能用 <code>O(1)</code> 額外空間、<code>O(n)</code> 時間完成嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [3,0,1]
  輸出：2
  說明：n = 3，範圍 [0, 3]，缺少 2。

範例 2
  輸入：nums = [0,1]
  輸出：2
  說明：n = 2，範圍 [0, 2]，缺少 2。

範例 3
  輸入：nums = [9,6,4,2,3,5,7,0,1]
  輸出：8""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 10⁴",
   "0 ≤ <code>nums[i]</code> ≤ <code>n</code>",
   "<code>nums</code> 中的數字互不相同",
 ],
 "idea": [
   ("c", """【n+1 個候選，只拿到 n 個】

【方法一：高斯求和】
    0 + 1 + ... + n = n(n+1)/2
    減掉陣列實際總和 = 缺的那個數。
    （其他語言要注意溢位；n ≤ 10⁴ 時沒問題。）

【方法二：XOR】
    把 0..n 全部 XOR，再和陣列所有元素 XOR：
    出現兩次的都抵銷，只剩缺的那個。
    技巧：索引 i 剛好是 0..n-1，再補一個 n -> 一次迴圈完成。

【方法三：排序後二分】
    排序後，缺的數之前 nums[i] == i，之後 nums[i] == i + 1。
    找第一個 nums[i] != i 的位置。
    如果陣列本來就排好序，這是 O(log n)。"""),
 ],
 "approaches": [
   ap("解法一", "雜湊集合", [
     ("c", S["p268_set"]),
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "排序 + 二分", [
     ("c", S["p268_sort"]),
   ], "O(n log n)", "O(1)", "已排序時 O(log n)", "原地排序"),

   ap("解法三", "高斯求和", [
     ("c", S["p268_sum"]),
   ], "O(n)", "O(1)", "", "", optimal=True),

   ap("解法四", "XOR", [
     ("c", S["p268_xor"]),
     "和求和法的想法一樣（成對抵銷），但不會溢位。",
   ], "O(n)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、集合", "O(n)", "O(n)", ""],
    ["二、排序 + 二分", "O(n log n)", "O(1)", "會修改輸入"],
    ["三、求和", "O(n)", "O(1)", "最簡潔 ✔"],
    ["四、XOR", "O(n)", "O(1)", "不怕溢位"]]),
 "edges": [
   "<strong>缺的是 0</strong> → 求和法照樣成立。",
   "<strong>缺的是 n</strong>（<code>[0,1]</code>）→ 二分法的 hi 要從 n 開始。",
   "<strong>n = 1</strong> → <code>[0]</code> 缺 1，<code>[1]</code> 缺 0。",
 ],
 "follow": [
   ("h", "延伸：陣列很大、可能有重複，找第一個缺少的正整數？"),
   ("c", "第 41 題（Hard）：把每個數放到「它的值 − 1」的索引上（原地雜湊），再找第一個位置不對的。"),
 ],
 "related": [
   "<strong>第 41 題 缺失的第一個正數</strong>",
   "<strong>第 287 題 尋找重複數</strong>",
   "<strong>第 448 題 找到所有陣列中消失的數字</strong>",
   "<strong>第 136 題 只出現一次的數字</strong> —— XOR 抵銷",
 ],
 "check": [
   "求和法怎麼找出缺的數？",
   "XOR 法中，為什麼要先放一個 n？",
   "二分法要找的是什麼位置？",
 ],
})
