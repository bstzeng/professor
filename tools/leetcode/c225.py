# -*- coding: utf-8 -*-
"""第 225–230 題。"""
import random
from collections import deque, Counter
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(225)
_DQ = {"deque": deque}


def _lv(vals):
    """LeetCode 的層序表示 -> 樹。"""
    if not vals or vals[0] is None:
        return None
    it = iter(vals)
    root = TreeNode(next(it))
    q = deque([root])
    while q:
        nd = q.popleft()
        for side in ("left", "right"):
            v = next(it, None)
            if v is not None:
                setattr(nd, side, TreeNode(v))
                q.append(getattr(nd, side))
    return root


def _ser(root):
    out, q = [], deque([root])
    while q:
        nd = q.popleft()
        if nd is None:
            out.append(None)
            continue
        out.append(nd.val)
        q.append(nd.left)
        q.append(nd.right)
    while out and out[-1] is None:
        out.pop()
    return out


def _rand_tree(n, lo=0, hi=9):
    if n == 0:
        return None
    k = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi), _rand_tree(k, lo, hi), _rand_tree(n - 1 - k, lo, hi))


# ==================== 225. Implement Stack using Queues ====================
S["p225_one"] = '''class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):   # ★ 把前面的元素全部轉到後面
            self.q.append(self.q.popleft())  #   新元素就跑到隊頭了

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q'''

S["p225_two"] = '''class MyStack:
    def __init__(self):
        self.q1 = deque()                     # 主佇列：隊頭就是堆疊頂端
        self.q2 = deque()                     # 輔助佇列

    def push(self, x: int) -> None:
        self.q2.append(x)                     # 新元素先進空的 q2
        while self.q1:                        # 舊元素依序排到它後面
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1   # 交換角色

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1'''

S["p225_lazy"] = '''class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:           # O(1)
        self.q.append(x)

    def pop(self) -> int:                     # O(n)：前 n-1 個轉到後面，剩下的就是最後進來的
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        x = self.pop()
        self.q.append(x)                      # 看完要放回去（放在隊尾，正好維持順序）
        return x

    def empty(self) -> bool:
        return not self.q'''

for key in ("p225_one", "p225_two", "p225_lazy"):
    for _ in range(300):
        st, ref = S.load(key, "MyStack", _DQ), []
        for _ in range(random.randrange(1, 40)):
            op = random.random()
            if ref and op < 0.3:
                assert st.pop() == ref.pop(), key
            elif ref and op < 0.5:
                assert st.top() == ref[-1], key
            elif op < 0.6:
                assert st.empty() == (not ref), key
            else:
                x = random.randrange(10)
                st.push(x)
                ref.append(x)
print("P225 OK")

emit({
 "num": 225, "slug": "implement-stack-using-queues",
 "en": [
   "Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions "
   "of a normal stack (<code>push</code>, <code>top</code>, <code>pop</code>, and <code>empty</code>).",
   "You must use <strong>only</strong> standard operations of a queue: push to back, peek/pop from front, size, and is empty.",
   "<strong>Follow-up:</strong> Can you implement the stack using only one queue?",
 ],
 "zh": [
   "只用兩個佇列實作一個後進先出（LIFO）的堆疊，支援 <code>push</code>、<code>top</code>、<code>pop</code>、<code>empty</code>。",
   "只能使用佇列的標準操作：從隊尾加入、從隊頭查看／取出、取得大小、判斷是否為空。",
   "<strong>進階：</strong>能只用<strong>一個</strong>佇列完成嗎？",
 ],
 "examples": """範例
  輸入：["MyStack","push","push","top","pop","empty"]
        [[],[1],[2],[],[],[]]
  輸出：[null,null,null,2,2,false]""",
 "constraints": [
   "1 ≤ <code>x</code> ≤ 9",
   "最多呼叫 100 次",
   "<code>pop</code> 和 <code>top</code> 呼叫時，堆疊一定不是空的",
 ],
 "idea": [
   ("c", """【佇列是先進先出，堆疊是後進先出 —— 順序剛好相反】
    要讓佇列的隊頭永遠是「最後放進來的」元素。

【一個佇列的旋轉技巧】
    push(x)：x 先排到隊尾，
             再把 x 前面的 n-1 個元素，一個一個從隊頭拿出來、放回隊尾。
             轉完一圈，x 就到了隊頭。

    原本 q = [2, 1]（隊頭 2 = 頂端，代表依序 push 了 1、2）
    push(3)：先放到隊尾 -> [2, 1, 3]
    旋轉 2 次：[1, 3, 2] -> [3, 2, 1] ✔  隊頭 3 = 最新

【取捨】
    push 花 O(n)，pop/top O(1)；
    或反過來：push O(1)，pop 時才旋轉 O(n)。
    取決於哪個操作比較頻繁。"""),
 ],
 "approaches": [
   ap("解法一", "兩個佇列（push 時整理）", [
     ("c", S["p225_two"]),
   ], "push O(n)，其他 O(1)", "O(n)", "", ""),

   ap("解法二", "一個佇列（push 時旋轉）", [
     ("c", S["p225_one"]),
   ], "push O(n)，其他 O(1)", "O(n)", "", "", optimal=True),

   ap("解法三", "一個佇列（pop 時才旋轉）", [
     ("c", S["p225_lazy"]),
     "適合 push 遠多於 pop 的情境。注意 <code>top</code> 取出之後要放回隊尾——放回去的位置剛好又是「最新」的位置。",
   ], "push O(1)，pop/top O(n)", "O(n)", "", ""),
 ],
 "compare": (["解法", "push", "pop / top", "佇列數"],
   [["一、兩個佇列", "O(n)", "O(1)", "2"],
    ["二、一個佇列 push 旋轉", "O(n)", "O(1)", "1 ✔"],
    ["三、一個佇列 pop 旋轉", "O(1)", "O(n)", "1"]]),
 "edges": [
   "<strong>只有一個元素</strong> → 旋轉 0 次。",
   "<strong>連續 pop 到空</strong> → <code>empty</code> 要回傳 true。",
   "<strong>Python 的 list 當佇列</strong> → <code>pop(0)</code> 是 O(n)；要用 <code>deque</code>。",
 ],
 "follow": [
   ("h", "反過來：用堆疊實作佇列？"),
   ("c", "第 232 題：兩個堆疊，一個負責進、一個負責出，出的空了才整批倒過來——攤銷 O(1)。比這一題更實用。"),
 ],
 "related": [
   "<strong>第 232 題 用堆疊實作佇列</strong>",
   "<strong>第 155 題 最小堆疊</strong>",
 ],
 "check": [
   "一個佇列時，push 之後要旋轉幾次？為什麼？",
   "什麼情況下應該選擇「pop 時才旋轉」的版本？",
 ],
})


# ==================== 226. Invert Binary Tree ====================
S["p226_rec"] = '''class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        # ★ 左右交換，並且各自再翻轉（先翻後換、先換後翻都可以）
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root'''

S["p226_bfs"] = '''class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root] if root else [])
        while q:                                  # 每個節點都交換自己的左右孩子
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root'''

_p226 = [S.load("p226_rec"), S.load("p226_bfs", extra=_DQ)]


def _mirror_ser(root):
    if root is None:
        return None
    return (root.val, _mirror_ser(root.right), _mirror_ser(root.left))


def _tup(root):
    return None if root is None else (root.val, _tup(root.left), _tup(root.right))


for vals, want in [([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]), ([2, 1, 3], [2, 3, 1]), ([], [])]:
    for sol in _p226:
        assert _ser(sol.invertTree(_lv(vals))) == want, ("P226", vals)
for _ in range(1000):
    n = random.randrange(0, 20)
    random.seed(10000 + _)
    a = _rand_tree(n)
    random.seed(10000 + _)
    b = _rand_tree(n)
    want = _mirror_ser(a)
    assert _tup(_p226[0].invertTree(a)) == want and _tup(_p226[1].invertTree(b)) == want
random.seed(2260)
print("P226 OK")

emit({
 "num": 226, "slug": "invert-binary-tree",
 "en": [
   "Given the <code>root</code> of a binary tree, invert the tree, and return its root.",
 ],
 "zh": [
   "給你一棵二元樹的根節點 <code>root</code>，把它<strong>左右翻轉</strong>（鏡像），回傳翻轉後的根節點。",
 ],
 "examples": """範例 1
  輸入：root = [4,2,7,1,3,6,9]
  輸出：[4,7,2,9,6,3,1]

         4                4
       /   \\            /   \\
      2     7    ->    7     2
     / \\   / \\        / \\   / \\
    1   3 6   9      9   6 3   1

範例 2
  輸入：root = [2,1,3]
  輸出：[2,3,1]

範例 3
  輸入：root = []
  輸出：[]""",
 "constraints": [
   "節點數在 <code>[0, 100]</code> 之間",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "idea": [
   ("c", """【鏡像 = 每一個節點都把左右孩子交換】
    只交換根的左右孩子是不夠的 ——
    子樹內部也要翻轉。

【遞迴定義】
    invert(空) = 空
    invert(node)：
        新的左子樹 = invert(原本的右子樹)
        新的右子樹 = invert(原本的左子樹)

【順序不重要】
    每個節點都交換一次，不管是前序、後序、層序都可以。
    唯一的陷阱：中序（先處理左、交換、再處理「右」）——
    交換之後原本的左子樹跑到右邊，會被翻兩次 ✘

【一行寫法的注意】
    root.left, root.right = invert(root.right), invert(root.left)
    右邊兩個呼叫先全部算完，才同時賦值 ✔
    分兩行寫的話要先暫存，否則 root.left 被覆蓋後就找不到了。"""),
 ],
 "approaches": [
   ap("解法一", "遞迴", [
     ("c", S["p226_rec"]),
   ], "O(n)", "O(h)", "", "遞迴深度 = 樹高", optimal=True),

   ap("解法二", "BFS（迭代）", [
     ("c", S["p226_bfs"]),
     "每個節點出佇列時交換它的兩個孩子。沒有遞迴深度的限制。",
   ], "O(n)", "O(w)", "", "w = 最寬一層"),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、遞迴", "O(n)", "O(h) ✔"],
    ["二、BFS", "O(n)", "O(w)"]]),
 "edges": [
   "<strong>空樹</strong> → 回傳 None。",
   "<strong>只有一邊的孩子</strong> → 交換後變成另一邊。",
   "<strong>非常偏斜的樹</strong> → 遞迴深度 = n；n ≤ 100 沒問題。",
 ],
 "follow": [
   ("h", "這題為什麼有名？"),
   ("c", """Homebrew 的作者 Max Howell 2015 年發推文：
「Google：我們 90% 的工程師都在用你寫的軟體（Homebrew），
但你不會在白板上翻轉二元樹，所以滾吧。」
這題因此成為「白板面試是否合理」爭論的象徵。"""),
 ],
 "related": [
   "<strong>第 101 題 對稱二元樹</strong> —— 判斷樹是否等於自己的鏡像",
   "<strong>第 100 題 相同的樹</strong>",
   "<strong>第 951 題 翻轉等價二元樹</strong>",
 ],
 "check": [
   "為什麼只交換根的左右孩子不夠？",
   "用中序遍歷交換會發生什麼問題？",
 ],
})


# ==================== 227. Basic Calculator II ====================
S["p227_stack"] = '''class Solution:
    def calculate(self, s: str) -> int:
        stack = []            # 存放「要相加的項」
        num = 0
        op = "+"              # ★ num 前面的運算子（第一個數字視為 +）
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and ch != " ") or i == len(s) - 1:
                # 讀完一個數字：依照它「前面」的運算子處理
                if op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                elif op == "*":
                    stack.append(stack.pop() * num)
                else:                                   # "/"：向零取整
                    stack.append(int(stack.pop() / num))
                op, num = ch, 0
        return sum(stack)'''

S["p227_o1"] = '''class Solution:
    def calculate(self, s: str) -> int:
        total = 0             # 已經確定的項的總和
        last = 0              # 最後一項（可能還會被乘除）
        num, op = 0, "+"
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and ch != " ") or i == len(s) - 1:
                if op in "+-":
                    total += last                       # 上一項確定了
                    last = num if op == "+" else -num
                elif op == "*":
                    last *= num
                else:
                    last = int(last / num)
                op, num = ch, 0
        return total + last'''

_p227 = [S.load(x) for x in ("p227_stack", "p227_o1")]
for s, want in [("3+2*2", 7), (" 3/2 ", 1), (" 3+5 / 2 ", 5), ("14-3/2", 13), ("1-5/2", -1),
                ("2*3*4", 24), ("100", 100), ("0-7/2*3", -9)]:
    for sol in _p227:
        assert sol.calculate(s) == want, ("P227", s)


def _ev(e):
    toks = e.replace(" ", "")
    import re as _re
    parts = _re.findall(r"\d+|[-+*/]", toks)
    terms, op = [], "+"
    for p in parts:
        if p in "+-*/":
            op = p
            continue
        n = int(p)
        if op == "+":
            terms.append(n)
        elif op == "-":
            terms.append(-n)
        elif op == "*":
            terms.append(terms.pop() * n)
        else:
            a = terms.pop()
            q = abs(a) // n
            terms.append(q if a >= 0 else -q)
    return sum(terms)


for _ in range(4000):
    k = random.randrange(1, 7)
    e = str(random.randrange(0, 50))
    for _ in range(k - 1):
        op = random.choice("+-*/")
        e += (" " if random.random() < 0.3 else "") + op + (" " if random.random() < 0.3 else "")
        e += str(random.randrange(1 if op == "/" else 0, 50))
    want = _ev(e)
    for sol in _p227:
        assert sol.calculate(e) == want, ("P227 rand", e)
print("P227 OK")

emit({
 "num": 227, "slug": "basic-calculator-ii",
 "en": [
   "Given a string <code>s</code> which represents an expression, evaluate this expression and return its value.",
   "The expression consists of non-negative integers, <code>'+'</code>, <code>'-'</code>, <code>'*'</code>, <code>'/'</code> operators and spaces. "
   "The integer division should <strong>truncate toward zero</strong>. The given expression is always valid.",
   "You are not allowed to use any built-in function which evaluates strings as expressions, such as <code>eval()</code>.",
 ],
 "zh": [
   "給你一個代表算式的字串 <code>s</code>，計算並回傳它的值。",
   "算式由非負整數、<code>'+'</code>、<code>'-'</code>、<code>'*'</code>、<code>'/'</code> 和空白組成（<strong>沒有括號</strong>）。"
   "整數除法<strong>向零取整</strong>。算式一定合法。",
   "不能使用 <code>eval()</code> 之類的內建函式。",
 ],
 "examples": """範例 1
  輸入：s = "3+2*2"
  輸出：7

範例 2
  輸入：s = " 3/2 "
  輸出：1

範例 3
  輸入：s = " 3+5 / 2 "
  輸出：5""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 3 × 10⁵",
   "<code>s</code> 只包含整數與 <code>'+'</code>、<code>'-'</code>、<code>'*'</code>、<code>'/'</code>、空白",
   "所有整數都是非負的，而且在 [0, 2³¹ − 1] 之間",
   "答案保證在 32 位元有號整數範圍內",
 ],
 "idea": [
   ("c", """【把算式看成「若干項相加」】
    3 + 5 / 2 - 4 * 2
    = (+3) + (+5/2) + (-4*2)
    每一項由乘除組成；項與項之間用加減連接。

【堆疊存「項」】
    讀完一個數字 num，看它【前面】的運算子 op：
        +  -> 新的一項 +num，推進堆疊
        -  -> 新的一項 -num，推進堆疊
        *  -> 和上一項合併：堆疊頂端 × num
        /  -> 和上一項合併：堆疊頂端 ÷ num（向零取整）
    最後把堆疊全部加總。

【為什麼看「前面」的運算子？】
    讀到數字的當下還不知道後面是什麼，
    但前面的運算子已經讀過了 -> 用變數 op 記住。

【向零取整的陷阱】
    Python 的 // 是向下取整：-3 // 2 = -2 ✘（題目要 -1）
    用 int(a / b) ✔（數值在 2³¹ 內，浮點數精度足夠）

【最後一個數字】
    字串結尾沒有運算子觸發結算 ->
    判斷 i == len(s) - 1 時也要處理。"""),
 ],
 "approaches": [
   ap("解法一", "堆疊存每一項", [
     ("c", S["p227_stack"]),
     ("c", """【模擬】s = "3+5/2"

    讀 3，遇到 '+'   op='+' -> push 3          stack=[3]      op='+'
    讀 5，遇到 '/'   op='+' -> push 5          stack=[3,5]    op='/'
    讀 2（結尾）     op='/' -> pop 5, 5/2=2    stack=[3,2]
    sum = 5 ✔"""),
   ], "O(n)", "O(n)", "", "", optimal=True),

   ap("解法二", "只保留最後一項（O(1) 空間）", [
     ("c", S["p227_o1"]),
     ("c", """【觀察】乘除只會影響「最後一項」
    更早的項已經不會再變了 -> 直接加進 total。
    所以不需要整個堆疊，一個變數 last 就夠。"""),
   ], "O(n)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、堆疊", "O(n)", "O(n) ✔（最好擴充）"],
    ["二、只存最後一項", "O(n)", "O(1)"]]),
 "edges": [
   "<strong>負數除法</strong>（<code>\"1-5/2\"</code>）→ 項是 −5/2，向零取整 = −2，答案 −1。",
   "<strong>結尾有空白</strong> → 最後一個字元是空白時，要確保最後一個數字仍被結算。本解法中 <code>i == len(s)-1</code> 也涵蓋空白字元，此時 op 是前一個運算子、num 是剛讀完的數字 ✔",
   "<strong>連續乘除</strong>（<code>\"2*3*4\"</code>）→ 同一項一直被更新。",
   "<strong>只有一個數字</strong> → 直接回傳。",
 ],
 "follow": [
   ("h", "追問：加上括號呢？"),
   ("c", "第 772 題（付費）：把本題的做法放進第 224 題的遞迴——遇到 '(' 就遞迴算出一個數字。"),
 ],
 "related": [
   "<strong>第 224 題 基本計算器</strong> —— 加減與括號",
   "<strong>第 150 題 逆波蘭表示法求值</strong>",
   "<strong>第 282 題 給表達式添加運算子</strong> —— 同樣用「最後一項」處理乘法優先順序",
 ],
 "check": [
   "為什麼處理一個數字時，要看的是「前面」的運算子？",
   "Python 中負數的整數除法要怎麼寫才會向零取整？",
   "解法二為什麼只需要保留最後一項？",
 ],
})


# ==================== 228. Summary Ranges ====================
S["p228"] = '''class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i, n = 0, len(nums)
        while i < n:
            j = i
            while j + 1 < n and nums[j + 1] == nums[j] + 1:   # ★ 一路延伸連續的段
                j += 1
            res.append(str(nums[i]) if i == j else f"{nums[i]}->{nums[j]}")
            i = j + 1                                         # 下一段從 j+1 開始
        return res'''

_p228 = S.load("p228")
for nums, want in [([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]), ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
                   ([], []), ([-1], ["-1"]), ([-2147483648, 2147483647], ["-2147483648", "2147483647"])]:
    assert _p228.summaryRanges(nums) == want, nums
for _ in range(2000):
    nums = sorted(random.sample(range(-10, 20), random.randrange(0, 15)))
    got = _p228.summaryRanges(nums)
    back = []
    for g in got:
        k = g.find("->", 1)
        a, b = (g, g) if k < 0 else (g[:k], g[k + 2:])
        back += list(range(int(a), int(b) + 1))
    assert back == nums, (nums, got)
    assert len(got) == (1 + sum(y != x + 1 for x, y in zip(nums, nums[1:])) if nums else 0), (nums, got)
print("P228 OK")

emit({
 "num": 228, "slug": "summary-ranges",
 "en": [
   "You are given a <strong>sorted unique</strong> integer array <code>nums</code>.",
   "Return the <strong>smallest sorted</strong> list of ranges that cover all the numbers in the array exactly. "
   "Each range <code>[a,b]</code> should be output as <code>\"a->b\"</code> if <code>a != b</code>, and <code>\"a\"</code> if <code>a == b</code>.",
 ],
 "zh": [
   "給你一個<strong>已排序、元素不重複</strong>的整數陣列 <code>nums</code>。",
   "回傳<strong>數量最少</strong>、依序排列的區間列表，剛好涵蓋陣列中所有數字。"
   "區間 <code>[a,b]</code> 若 <code>a != b</code> 寫成 <code>\"a->b\"</code>，若 <code>a == b</code> 寫成 <code>\"a\"</code>。",
 ],
 "examples": """範例 1
  輸入：nums = [0,1,2,4,5,7]
  輸出：["0->2","4->5","7"]

範例 2
  輸入：nums = [0,2,3,4,6,8,9]
  輸出：["0","2->4","6","8->9"]""",
 "constraints": [
   "0 ≤ <code>nums.length</code> ≤ 20",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
   "<code>nums</code> 中的值互不相同，且遞增排列",
 ],
 "idea": [
   ("c", """【把陣列切成「連續遞增 1」的段落】
    [0, 1, 2 | 4, 5 | 7]
    斷點出現在 nums[j+1] != nums[j] + 1 的地方。

【雙指標】
    i = 一段的起點
    j 從 i 開始往後延伸，直到下一個不連續
    輸出這一段，然後 i = j + 1

【輸出格式】
    i == j -> "a"
    否則   -> "a->b"

【溢位（其他語言）】
    nums[j] + 1 在 nums[j] = 2³¹ - 1 時會溢位。
    Java/C++ 可以改寫成 nums[j+1] - nums[j] == 1（用 long）。Python 不必擔心。"""),
 ],
 "approaches": [
   ap("解法", "雙指標切段", [
     ("c", S["p228"]),
   ], "O(n)", "O(1)", "", "不計輸出", optimal=True),
 ],
 "edges": [
   "<strong>空陣列</strong> → <code>[]</code>。",
   "<strong>只有一個數</strong> → <code>[\"a\"]</code>。",
   "<strong>負數</strong> → 例如 <code>\"-3->-1\"</code>，格式照樣。",
   "<strong>極值</strong> → 2³¹−1 加 1 在其他語言會溢位。",
 ],
 "follow": [
   ("h", "追問：如果陣列沒有排序、可能重複？"),
   ("c", "先排序去重 O(n log n)；或用雜湊集合，只從「x−1 不在集合裡」的 x 開始往上延伸——這就是第 128 題的做法。"),
 ],
 "related": [
   "<strong>第 163 題 缺失的區間</strong>（付費）",
   "<strong>第 128 題 最長連續序列</strong>",
   "<strong>第 352 題 將資料流變為多個不相交區間</strong>",
 ],
 "check": [
   "一段連續區間在什麼條件下結束？",
   "處理完一段之後，下一段從哪裡開始？",
 ],
})


# ==================== 229. Majority Element II ====================
S["p229_bm"] = '''class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # ★ 超過 n/3 的元素最多 2 個 -> 保留 2 個候選人
        c1, c2, n1, n2 = None, None, 0, 0
        for x in nums:
            if x == c1:
                n1 += 1
            elif x == c2:
                n2 += 1
            elif n1 == 0:
                c1, n1 = x, 1
            elif n2 == 0:
                c2, n2 = x, 1
            else:                     # 三個不同的值互相抵銷
                n1 -= 1
                n2 -= 1
        # 第二趟：候選人不一定真的超過 n/3，要重新計數確認
        return [c for c in (c1, c2) if c is not None and nums.count(c) > len(nums) // 3]'''

S["p229_count"] = '''class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt = collections.Counter(nums)
        return [x for x, c in cnt.items() if c > len(nums) // 3]'''

_p229 = [S.load(x) for x in ("p229_bm", "p229_count")]
for nums, want in [([3, 2, 3], [3]), ([1], [1]), ([1, 2], [1, 2]), ([2, 2], [2]), ([1, 2, 3], [])]:
    for sol in _p229:
        assert sorted(sol.majorityElement(nums)) == sorted(want), ("P229", nums)
for _ in range(5000):
    nums = [random.choice([1, 1, 2, 2, 3, 4, 5][:random.randrange(2, 8)]) for _ in range(random.randrange(1, 13))]
    assert sorted(_p229[0].majorityElement(nums)) == sorted(_p229[1].majorityElement(nums)), nums
print("P229 OK")

_P229_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">摩爾投票推廣：每次拿掉「三個互不相同」的數</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="40" width="36" height="30" fill="none" stroke="var(--accent)"/><text x="58" y="60" fill="var(--accent)">A</text>
              <rect x="80" y="40" width="36" height="30" fill="none" stroke="var(--gold)"/><text x="98" y="60" fill="var(--gold)">B</text>
              <rect x="120" y="40" width="36" height="30" fill="none" stroke="#ff8a65"/><text x="138" y="60" fill="#ff8a65">C</text>
            </g>
            <text x="170" y="60" fill="var(--text)" font-size="12">一次抵銷 3 個數，其中每一種值最多只少 1 個</text>
            <text x="40" y="100" fill="var(--text)" font-size="12">若 x 出現 &gt; n/3 次：抵銷最多 n/3 輪（每輪用掉 3 個），x 最多被扣 n/3 次</text>
            <text x="40" y="122" fill="var(--text)" font-size="12">→ x 一定會留到最後，成為兩個候選人之一。</text>
            <text x="40" y="154" fill="var(--gold)" font-size="12">★ 但留下來的候選人不一定超過 n/3（例如 [1,2,3]），所以要再數一次確認。</text>'''

emit({
 "num": 229, "slug": "majority-element-ii",
 "en": [
   "Given an integer array of size <code>n</code>, find all elements that appear more than <code>⌊ n/3 ⌋</code> times.",
   "<strong>Follow up:</strong> Could you solve the problem in linear time and in <code>O(1)</code> space?",
 ],
 "zh": [
   "給你一個長度為 <code>n</code> 的整數陣列，找出所有出現次數<strong>超過 <code>⌊ n/3 ⌋</code></strong> 的元素。",
   "<strong>進階：</strong>能用線性時間、<code>O(1)</code> 額外空間解決嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [3,2,3]
  輸出：[3]

範例 2
  輸入：nums = [1]
  輸出：[1]

範例 3
  輸入：nums = [1,2]
  輸出：[1,2]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 5 × 10⁴",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
 ],
 "idea": [
   ("fig", _P229_FIG, "0 0 640 170"),
   ("c", """【答案最多幾個？】
    超過 n/3 的元素如果有 3 個，總數就 > n ✘
    -> 最多 2 個。

【第 169 題的摩爾投票：1 個候選人】
    不同的兩個數互相抵銷，超過一半的那個一定留下來。

【推廣：2 個候選人】
    每遇到一個數 x：
        x 等於某個候選人    -> 那個候選人的票 +1
        某個候選人票數為 0  -> x 取代它，票數 1
        否則                -> 兩個候選人的票都 -1
                               （x、c1、c2 三個不同的值互相抵銷）

【為什麼一定要第二趟？】
    保證：真正超過 n/3 的元素一定是候選人。
    不保證：候選人一定超過 n/3。
    [1, 2, 3] -> 候選人可能是 3 和 2，但都只出現一次。

【判斷順序很重要】
    先檢查「等於 c1 / c2」，再檢查「票數為 0」。
    反過來的話，c1 票數 0 時遇到 c2 的值，
    會讓 c1 和 c2 變成同一個值 ✘"""),
 ],
 "approaches": [
   ap("解法一", "雜湊計數", [
     ("c", S["p229_count"]),
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "摩爾投票（兩個候選人）", [
     ("c", S["p229_bm"]),
   ], "O(n)", "O(1)", "兩趟掃描", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、雜湊計數", "O(n)", "O(n)"],
    ["二、摩爾投票", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>n = 1 或 2</strong> → 每個不同的元素都超過 ⌊n/3⌋ = 0。",
   "<strong>沒有任何答案</strong>（<code>[1,2,3]</code>）→ 第二趟全部篩掉。",
   "<strong>候選人初始值</strong> → 用 None，避免和陣列中的值（例如 0）混淆。",
   "<strong>兩個候選人相同</strong> → 判斷順序正確就不會發生。",
 ],
 "follow": [
   ("h", "推廣：超過 n/k 的元素？"),
   ("c", "保留 k−1 個候選人，遇到新值且沒有空位時全部 −1。時間 O(nk)、空間 O(k)。這個演算法叫 Misra–Gries，是串流資料中找「熱門項目」的經典方法。"),
 ],
 "related": [
   "<strong>第 169 題 多數元素</strong> —— 超過 n/2",
   "<strong>第 1150 題 檢查一個數是否在陣列中佔絕大多數</strong>（付費）",
 ],
 "check": [
   "超過 n/3 的元素最多有幾個？為什麼？",
   "三個不同的數互相抵銷，為什麼不會把真正的答案消掉？",
   "為什麼需要第二趟重新計數？",
   "候選人判斷中，為什麼要先檢查「等於候選人」再檢查「票數為 0」？",
 ],
})


# ==================== 230. Kth Smallest Element in a BST ====================
S["p230_it"] = '''class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while True:
            while node:                  # 一路往左，沿途推進堆疊
                stack.append(node)
                node = node.left
            node = stack.pop()           # ★ 中序的下一個（由小到大）
            k -= 1
            if k == 0:
                return node.val          # 第 k 個就停，不必走完整棵樹
            node = node.right'''

S["p230_rec"] = '''class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        for i, v in enumerate(inorder(root), 1):   # 產生器：拿到第 k 個就停
            if i == k:
                return v'''

S["p230_size"] = '''class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        size = {}                        # 節點 -> 子樹大小（樹常常變動時，存在節點上維護）

        def count(node):
            if node is None:
                return 0
            size[node] = 1 + count(node.left) + count(node.right)
            return size[node]

        count(root)
        node = root
        while node:
            left = size.get(node.left, 0)
            if k <= left:                # 在左子樹
                node = node.left
            elif k == left + 1:          # 就是自己
                return node.val
            else:                        # 在右子樹：扣掉左子樹和自己
                k -= left + 1
                node = node.right'''

_p230 = [S.load(x) for x in ("p230_it", "p230_rec", "p230_size")]


def _bst(vals):
    root = None

    def ins(nd, v):
        if nd is None:
            return TreeNode(v)
        if v < nd.val:
            nd.left = ins(nd.left, v)
        else:
            nd.right = ins(nd.right, v)
        return nd

    for v in vals:
        root = ins(root, v)
    return root


for vals, k, want in [([3, 1, 4, None, 2], 1, 1), ([5, 3, 6, 2, 4, None, None, 1], 3, 3)]:
    for sol in _p230:
        assert sol.kthSmallest(_lv(vals), k) == want
for _ in range(1500):
    vals = random.sample(range(100), random.randrange(1, 25))
    t = _bst(vals)
    k = random.randrange(1, len(vals) + 1)
    want = sorted(vals)[k - 1]
    for sol in _p230:
        assert sol.kthSmallest(t, k) == want
print("P230 OK")

emit({
 "num": 230, "slug": "kth-smallest-element-in-a-bst",
 "en": [
   "Given the <code>root</code> of a binary search tree, and an integer <code>k</code>, return the <code>k<sup>th</sup></code> "
   "smallest value (<strong>1-indexed</strong>) of all the values of the nodes in the tree.",
   "<strong>Follow up:</strong> If the BST is modified often (i.e., we can do insert and delete operations) and you need to find "
   "the kth smallest frequently, how would you optimize?",
 ],
 "zh": [
   "給你一棵<strong>二元搜尋樹</strong>的根節點 <code>root</code> 和整數 <code>k</code>，回傳樹中第 <code>k</code> 小的值（<strong>從 1 開始</strong>數）。",
   "<strong>進階：</strong>如果這棵樹經常被修改（插入、刪除），而且需要頻繁查詢第 k 小，要怎麼優化？",
 ],
 "examples": """範例 1
  輸入：root = [3,1,4,null,2], k = 1
  輸出：1

範例 2
  輸入：root = [5,3,6,2,4,null,null,1], k = 3
  輸出：3""",
 "constraints": [
   "節點數為 <code>n</code>",
   "1 ≤ <code>k</code> ≤ <code>n</code> ≤ 10⁴",
   "0 ≤ <code>Node.val</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【BST 的中序遍歷 = 由小到大排序】
    左子樹 < 根 < 右子樹
    中序（左 -> 根 -> 右）走出來就是遞增序列。
    第 k 個拜訪到的節點 = 第 k 小 ✔

【提早停止】
    不用走完整棵樹，數到 k 就回傳。
    用迭代的中序（手動堆疊），時間 O(h + k)：
        先往左走到底花 O(h)，之後每 pop 一次就前進一個。

【進階：樹常常變動】
    每個節點多存一個「子樹大小」size。
    在節點 node：
        left = 左子樹大小
        k <= left      -> 答案在左子樹
        k == left + 1  -> 就是 node
        否則           -> 去右子樹找第 (k - left - 1) 小
    每次查詢 O(h)；插入、刪除時沿路更新 size，也是 O(h)。
    搭配平衡樹（紅黑樹、AVL）h = O(log n)。
    這種樹叫「順序統計樹」(order statistic tree)。"""),
 ],
 "approaches": [
   ap("解法一", "中序遍歷（產生器，提早停止）", [
     ("c", S["p230_rec"]),
   ], "O(h + k)", "O(h)", "", ""),

   ap("解法二", "迭代中序（手動堆疊）", [
     ("c", S["p230_it"]),
     ("c", """【迭代中序的模板】
    1. 一路往左，沿途推進堆疊
    2. pop 出來 = 下一個最小的
    3. 轉到它的右子樹，回到步驟 1"""),
   ], "O(h + k)", "O(h)", "", "", optimal=True),

   ap("解法三", "子樹大小（進階問題）", [
     ("c", S["p230_size"]),
     "這裡為了示範，先 O(n) 算出所有子樹大小；實際應用中 size 存在節點上，隨插入刪除維護，每次查詢只要 O(h)。",
   ], "查詢 O(h)", "O(n)", "預處理 O(n)", ""),
 ],
 "compare": (["解法", "時間", "空間", "適合"],
   [["一、遞迴中序", "O(h + k)", "O(h)", "單次查詢"],
    ["二、迭代中序", "O(h + k)", "O(h)", "單次查詢 ✔"],
    ["三、子樹大小", "O(h) / 次", "O(n)", "樹常變動、查詢頻繁"]]),
 "edges": [
   "<strong>k = 1</strong> → 最左邊的節點。",
   "<strong>k = n</strong> → 最右邊的節點，要走完整棵樹。",
   "<strong>樹是一條鏈</strong> → h = n，堆疊深度 n。",
 ],
 "follow": [
   ("h", "追問：第 k 大？"),
   ("c", "反向中序（右 → 根 → 左），或找第 n − k + 1 小。"),
 ],
 "related": [
   "<strong>第 94 題 二元樹的中序遍歷</strong>",
   "<strong>第 173 題 二元搜尋樹迭代器</strong> —— 同一個迭代中序模板",
   "<strong>第 671 題 二元樹中第二小的節點</strong>",
 ],
 "check": [
   "為什麼 BST 的中序遍歷是遞增的？",
   "迭代中序的時間為什麼是 O(h + k) 而不是 O(n)？",
   "子樹大小的方法中，走到右子樹時 k 要怎麼調整？",
 ],
})
