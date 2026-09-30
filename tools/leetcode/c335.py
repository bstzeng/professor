# -*- coding: utf-8 -*-
"""第 335、336、337、338、341、342 題。"""
import random
from authoring import emit, ap
from runner import Src
from lchelp import lv, rand_tree

S = Src()
random.seed(335)


# ==================== 335. Self Crossing ====================
S["p335"] = '''class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        d = distance
        for i in range(3, len(d)):
            # 情況 1：第 i 條線撞上第 i-3 條（四條線圍成的方框）
            if d[i] >= d[i - 2] and d[i - 1] <= d[i - 3]:
                return True
            # 情況 2：第 i 條線和第 i-4 條「接在一起」（五條線）
            if i >= 4 and d[i - 1] == d[i - 3] and d[i] + d[i - 4] >= d[i - 2]:
                return True
            # 情況 3：第 i 條線撞上第 i-5 條（六條線，螺旋縮小時）
            if (i >= 5 and d[i - 2] >= d[i - 4] and d[i - 3] >= d[i - 1]
                    and d[i - 1] + d[i - 5] >= d[i - 3] and d[i] + d[i - 4] >= d[i - 2]):
                return True
        return False'''

_p335 = S.load("p335")


def _cross_ref(d):
    """逐條線段檢查是否和之前（非相鄰）的線段相交或接觸。"""
    x = y = 0
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    segs = []
    for i, L in enumerate(d):
        dx, dy = dirs[i % 4]
        nx, ny = x + dx * L, y + dy * L
        segs.append((x, y, nx, ny))
        x, y = nx, ny

    def inter(a, b):
        ax1, ay1, ax2, ay2 = a
        bx1, by1, bx2, by2 = b
        return (max(min(ax1, ax2), min(bx1, bx2)) <= min(max(ax1, ax2), max(bx1, bx2)) and
                max(min(ay1, ay2), min(by1, by2)) <= min(max(ay1, ay2), max(by1, by2)))

    for i in range(len(segs)):
        for j in range(i - 1):
            if inter(segs[i], segs[j]):
                return True
        # 相鄰的線段只共享一個端點；若方向相反重疊（長度 0 不會發生）不需處理
    return False


for d, want in [([2, 1, 1, 2], True), ([1, 2, 3, 4], False), ([1, 1, 1, 2, 1], True), ([1, 1, 2, 1, 1], True), ([3, 3, 4, 2, 2], False)]:
    assert _p335.isSelfCrossing(d) == want, d
for _ in range(20000):
    d = [random.randint(1, 5) for _ in range(random.randrange(1, 9))]
    assert _p335.isSelfCrossing(d) == _cross_ref(d), d
print("P335 OK")

def _path_svg(d, ox, oy, sc, hit):
    """把 distance 畫成折線；最後一條橘色、被撞的那條藍色。"""
    x = y = 0
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    pts = [(0, 0)]
    for i, L in enumerate(d):
        x, y = x + dirs[i % 4][0] * L, y + dirs[i % 4][1] * L
        pts.append((x, y))
    P = [(ox + px * sc, oy - py * sc) for px, py in pts]
    out = []
    for i in range(len(d)):
        (x1, y1), (x2, y2) = P[i], P[i + 1]
        col = "#ff8a65" if i == len(d) - 1 else ("var(--accent)" if i == hit else "var(--text-muted)")
        w = 2.5 if col != "var(--text-muted)" else 1.5
        out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{col}" stroke-width="{w}"/>')
    out.append(f'<circle cx="{P[0][0]:.0f}" cy="{P[0][1]:.0f}" r="3" fill="var(--text)"/>')
    return "\n            ".join(out)


_P335_FIG = ('''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">最後一條線（橘色）只可能碰到 i−3、i−4、i−5 這三條之一（藍色）；黑點是起點</text>
            ''' + _path_svg([2, 2, 1, 2], 110, 130, 30, 0) + '''
            <text x="40" y="200" fill="var(--text)" font-size="12">① [2,2,1,2]：撞上 i−3</text>
            ''' + _path_svg([1, 1, 2, 1, 1], 320, 110, 30, 0) + '''
            <text x="240" y="200" fill="var(--text)" font-size="12">② [1,1,2,1,1]：接上 i−4</text>
            ''' + _path_svg([2, 2, 4, 4, 3, 3], 530, 110, 15, 0) + '''
            <text x="440" y="200" fill="var(--text)" font-size="12">③ [2,2,4,4,3,3]：撞上 i−5</text>
            <text x="20" y="232" fill="var(--text-muted)" font-size="12">螺旋一旦「縮小」就只能繼續縮小，能碰到的線段永遠在最近的幾條之內。</text>''')

emit({
 "num": 335, "slug": "self-crossing",
 "en": [
   "You are given an array of integers <code>distance</code>.",
   "You start at the point <code>(0, 0)</code> on an <strong>X-Y plane,</strong> and you move <code>distance[0]</code> meters to the north, then <code>distance[1]</code> meters to the west, "
   "<code>distance[2]</code> meters to the south, <code>distance[3]</code> meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.",
   "Return <code>true</code> <em>if your path crosses itself or</em> <code>false</code> <em>if it does not</em>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>distance</code>。",
   "從平面上的 <code>(0, 0)</code> 出發，依序往<strong>北</strong>走 <code>distance[0]</code>、往<strong>西</strong>走 <code>distance[1]</code>、往<strong>南</strong>走 <code>distance[2]</code>、往<strong>東</strong>走 <code>distance[3]</code>……每走一段就逆時針轉 90°。",
   "如果路徑和自己<strong>相交（或碰到）</strong>，回傳 <code>true</code>。",
 ],
 "examples": """範例 1
  輸入：distance = [2,1,1,2]
  輸出：true

範例 2
  輸入：distance = [1,2,3,4]
  輸出：false

範例 3
  輸入：distance = [1,1,1,2,1]
  輸出：true
  說明：回到了起點 (0, 0)。""",
 "constraints": [
   "1 ≤ <code>distance.length</code> ≤ 10⁵",
   "1 ≤ <code>distance[i]</code> ≤ 10⁵",
 ],
 "idea": [
   ("fig", _P335_FIG, "0 0 640 246"),
   ("c", """【暴力：每條新線段和之前所有線段比】
    O(n²)，n = 10⁵ 太慢。

【觀察：路徑是一個螺旋】
    - 一直「擴張」（每段都比兩段前更長）-> 永遠不會相交
    - 一旦「縮小」，就被困在之前的框框裡，只能繼續縮小
    所以第 i 條線只可能碰到最近的幾條：i-3、i-4、i-5。

【三種情況】
    ① 撞上 i-3（四條線圍成的框）
        d[i] >= d[i-2]  且  d[i-1] <= d[i-3]
    ② 剛好接上 i-4（五條線，首尾相連）
        d[i-1] == d[i-3]  且  d[i] + d[i-4] >= d[i-2]
    ③ 撞上 i-5（六條線，從擴張轉為縮小的瞬間）
        d[i-2] >= d[i-4]
        d[i-3] >= d[i-1]
        d[i-1] + d[i-5] >= d[i-3]
        d[i]   + d[i-4] >= d[i-2]

【這題是純幾何分類】
    重點在「為什麼只需要看最近 5 條」，
    推導時畫圖最清楚。"""),
 ],
 "approaches": [
   ap("解法", "只檢查最近三種碰撞情況", [
     ("c", S["p335"]),
     "驗證方式：用逐條線段兩兩求交的暴力版本，對兩萬組隨機輸入比對結果完全一致。",
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>長度 ≤ 3</strong> → 不可能相交。",
   "<strong>回到原點</strong>（<code>[1,1,1,1]</code>）→ 算相交（碰到）。",
   "<strong>一直擴張</strong>（<code>[1,2,3,4,5,…]</code>）→ 永遠 false。",
 ],
 "follow": [
   ("h", "如何避免分類錯誤？"),
   ("c", "這種幾何分類題容易漏情況。最可靠的做法：先寫一個 O(n²) 的線段相交暴力解，用隨機測試比對。本頁的程式碼就是這樣驗證的。"),
 ],
 "related": [
   "<strong>第 54 題 螺旋矩陣</strong>",
   "<strong>第 1496 題 判斷路徑是否相交</strong> —— 每步 1 格，用集合記錄走過的點",
 ],
 "check": [
   "為什麼第 i 條線只需要和 i−3、i−4、i−5 比？",
   "螺旋從「擴張」變「縮小」後，為什麼不能再擴張？",
 ],
})


# ==================== 336. Palindrome Pairs ====================
S["p336"] = '''class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        index = {w: i for i, w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for k in range(len(w) + 1):
                prefix, suffix = w[:k], w[k:]
                # ① w = prefix + suffix，prefix 是回文 -> 找 reverse(suffix) 放在 w 前面
                #    reverse(suffix) + prefix + suffix 就是回文
                if prefix == prefix[::-1]:
                    j = index.get(suffix[::-1])
                    if j is not None and j != i:
                        res.append([j, i])
                # ② suffix 是回文 -> 找 reverse(prefix) 放在 w 後面
                #    k != len(w)：避免空字串的情況和 ① 重複計算
                if k != len(w) and suffix == suffix[::-1]:
                    j = index.get(prefix[::-1])
                    if j is not None and j != i:
                        res.append([i, j])
        return res'''

S["p336_brute"] = '''class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        for i, a in enumerate(words):
            for j, b in enumerate(words):
                if i != j and a + b == (a + b)[::-1]:
                    res.append([i, j])
        return res'''

_p336 = [S.load(x) for x in ("p336", "p336_brute")]
for w, want in [(["abcd", "dcba", "lls", "s", "sssll"], [[0, 1], [1, 0], [3, 2], [2, 4]]), (["bat", "tab", "cat"], [[0, 1], [1, 0]]), (["a", ""], [[0, 1], [1, 0]])]:
    for sol in _p336:
        assert sorted(sol.palindromePairs(w)) == sorted(want)
for _ in range(2000):
    words = list({"".join(random.choice("ab") for _ in range(random.randrange(0, 5))) for _ in range(random.randrange(1, 8))})
    a, b = (sorted(sol.palindromePairs(words)) for sol in _p336)
    assert a == b, words
print("P336 OK")

emit({
 "num": 336, "slug": "palindrome-pairs",
 "en": [
   "You are given a <strong>0-indexed</strong> array of <strong>unique</strong> strings <code>words</code>.",
   "A <strong>palindrome pair</strong> is a pair of integers <code>(i, j)</code> such that:",
   ("ul", ["<code>0 &lt;= i, j &lt; words.length</code>,",
           "<code>i != j</code>, and",
           "<code>words[i] + words[j]</code> (the concatenation of the two strings) is a palindrome."]),
   "Return <em>an array of all the <strong>palindrome pairs</strong> of</em> <code>words</code>.",
   "You must write an algorithm with <code>O(sum of words[i].length)</code> runtime complexity.",
 ],
 "zh": [
   "給你一個字串陣列 <code>words</code>，其中字串<strong>互不相同</strong>。",
   "<strong>回文對</strong>是一對索引 <code>(i, j)</code>，滿足 <code>i != j</code>，而且 <code>words[i] + words[j]</code> 串接起來是回文。",
   "回傳所有回文對。",
 ],
 "examples": """範例 1
  輸入：words = ["abcd","dcba","lls","s","sssll"]
  輸出：[[0,1],[1,0],[3,2],[2,4]]
  說明："dcbaabcd"、"abcddcba"、"slls"、"llssssll"

範例 2
  輸入：words = ["bat","tab","cat"]
  輸出：[[0,1],[1,0]]

範例 3
  輸入：words = ["a",""]
  輸出：[[0,1],[1,0]]""",
 "constraints": [
   "1 ≤ <code>words.length</code> ≤ 5000",
   "0 ≤ <code>words[i].length</code> ≤ 300",
   "<code>words[i]</code> 由小寫英文字母組成",
 ],
 "idea": [
   ("c", """【暴力：兩兩串接判斷，O(n² · L)】
    n = 5000 -> 2500 萬對，每對還要檢查回文，太慢。

【換個角度：對每個單字 w，它的「搭檔」長什麼樣？】
    把 w 切成 prefix + suffix（所有切法，包含空字串）。

    情況 ①：prefix 本身是回文
        搭檔 = reverse(suffix)，放在 w 的【前面】
        reverse(suffix) + [prefix] + suffix
                          └ 回文 ┘
        左右兩邊互為鏡像，中間是回文 -> 整體回文 ✔

    情況 ②：suffix 本身是回文
        搭檔 = reverse(prefix)，放在 w 的【後面】
        prefix + [suffix] + reverse(prefix) ✔

    用雜湊表查搭檔是否存在。

【避免重複】
    當 w 和搭檔等長時（切點在頭或尾），
    ① 的 k = 0 和 ② 的 k = len(w) 會找到同一對。
    ② 跳過 k = len(w) 就好。

【複雜度】
    每個單字 L+1 種切法，每種 O(L) 檢查回文和反轉 -> O(n · L²)。
    比暴力的 O(n² · L) 好很多（L ≤ 300，n ≤ 5000）。
    用 Trie + Manacher 可以做到真正的 O(總長度)，但實作複雜。"""),
 ],
 "approaches": [
   ap("解法一", "暴力兩兩串接", [
     ("c", S["p336_brute"]),
   ], "O(n² · L)", "O(L)", "", ""),

   ap("解法二", "枚舉切點 + 雜湊表查搭檔", [
     ("c", S["p336"]),
   ], "O(n · L²)", "O(n · L)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、暴力", "O(n²·L)", "n 大時超時"],
    ["二、切點 + 雜湊", "O(n·L²)", "實務上最常用 ✔"],
    ["Trie + Manacher", "O(Σ L)", "理論最佳，實作複雜"]]),
 "edges": [
   "<strong>空字串</strong> → 和任何回文字串都能配成兩對（前、後各一）。",
   "<strong>自己和自己</strong> → 題目要求 i != j，必須排除。",
   "<strong>等長的互為反轉</strong>（\"abcd\"、\"dcba\"）→ 兩個方向都要算，但不能重複。",
 ],
 "follow": [
   ("h", "Trie 做法的概念"),
   ("c", "把所有單字「反轉」後插入 Trie。對每個 w 沿 Trie 往下走：途中遇到某個單字結尾，且 w 剩下的部分是回文 → 找到一對；走完 w 之後，Trie 子樹中「剩下部分是回文」的單字也都是搭檔（需要預先記錄）。"),
 ],
 "related": [
   "<strong>第 5 題 最長回文子串</strong>",
   "<strong>第 214 題 最短回文串</strong>",
   "<strong>第 2131 題 連接兩字母單字得到的最長回文串</strong>",
 ],
 "check": [
   "把 w 切成 prefix + suffix 後，兩種情況下的搭檔分別是什麼？",
   "為什麼 prefix 是回文時，reverse(suffix) + w 會是回文？",
   "怎麼避免同一對被算兩次？",
 ],
})


# ==================== 337. House Robber III ====================
S["p337"] = '''class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node) -> Tuple[int, int]:
            # 回傳 (搶這個節點的最大收益, 不搶這個節點的最大收益)
            if node is None:
                return 0, 0
            l_rob, l_skip = dfs(node.left)
            r_rob, r_skip = dfs(node.right)
            rob = node.val + l_skip + r_skip             # ★ 搶自己 -> 孩子都不能搶
            skip = max(l_rob, l_skip) + max(r_rob, r_skip)   # 不搶自己 -> 孩子隨意
            return rob, skip

        return max(dfs(root))'''

S["p337_memo"] = '''class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def best(node) -> int:                   # 以 node 為根的子樹，最多能搶多少
            if node is None:
                return 0
            if node in memo:
                return memo[node]
            # 搶 node：跳過孩子，從孫子開始
            take = node.val
            for child in (node.left, node.right):
                if child:
                    take += best(child.left) + best(child.right)
            # 不搶 node：兩個孩子各自最佳
            skip = best(node.left) + best(node.right)
            memo[node] = max(take, skip)
            return memo[node]

        return best(root)'''

_p337 = [S.load(x) for x in ("p337", "p337_memo")]


def _rob_ref(root):
    nodes, parent = [], {}
    st = [root] if root else []
    while st:
        nd = st.pop()
        nodes.append(nd)
        for c in (nd.left, nd.right):
            if c:
                parent[c] = nd
                st.append(c)
    best = 0
    for mask in range(1 << len(nodes)):
        chosen = {nodes[i] for i in range(len(nodes)) if mask >> i & 1}
        if any(parent.get(nd) in chosen for nd in chosen):
            continue
        best = max(best, sum(nd.val for nd in chosen))
    return best


for vals, want in [([3, 2, 3, None, 3, None, 1], 7), ([3, 4, 5, 1, 3, None, 1], 9)]:
    for sol in _p337:
        assert sol.rob(lv(vals)) == want
for _ in range(800):
    t = rand_tree(random.randrange(1, 11), 0, 9)
    want = _rob_ref(t)
    for sol in _p337:
        assert sol.rob(t) == want
print("P337 OK")

emit({
 "num": 337, "slug": "house-robber-iii",
 "en": [
   "The thief has found himself a new place for his thievery again. There is only one entrance to this area, called <code>root</code>.",
   "Besides the <code>root</code>, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. "
   "It will automatically contact the police if <strong>two directly-linked houses were broken into on the same night</strong>.",
   "Given the <code>root</code> of the binary tree, return <em>the maximum amount of money the thief can rob <strong>without alerting the police</strong></em>.",
 ],
 "zh": [
   "小偷又找到新的地區。這個地區的房子排成一棵<strong>二元樹</strong>，入口是根節點 <code>root</code>。",
   "如果<strong>直接相連</strong>的兩間房子（父子）在同一晚都被偷，就會觸發警報。",
   "回傳在不觸發警報的前提下，最多能偷到多少錢。",
 ],
 "examples": """範例 1
  輸入：root = [3,2,3,null,3,null,1]
  輸出：7
  說明：3 + 3 + 1 = 7

範例 2
  輸入：root = [3,4,5,1,3,null,1]
  輸出：9
  說明：4 + 5 = 9""",
 "constraints": [
   "節點數在 <code>[1, 10⁴]</code> 之間",
   "0 ≤ <code>Node.val</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【第 198 題（一排房子）搬到樹上】
    每個節點只有兩種選擇：搶、不搶。

【樹形 DP：每個節點回傳兩個值】
    rob  = 搶這個節點時，子樹的最大收益
    skip = 不搶這個節點時，子樹的最大收益

    rob  = node.val + 左.skip + 右.skip        （搶自己 -> 孩子都不能搶）
    skip = max(左.rob, 左.skip) + max(右.rob, 右.skip)   （孩子可搶可不搶）

    後序遍歷：先算孩子，再算自己。
    答案 = max(根.rob, 根.skip)

【常見錯誤：「只搶奇數層或偶數層」】
    [2, 1, 3, null, 4]：
           2
          / \
         1   3
          \
           4
    偶數層 2 + 4 = 6，奇數層 1 + 3 = 4
    但最佳是 3 + 4 = 7（3 的父親是 2、4 的父親是 1，互不相連）✔
    最佳解可以跨層混搭。

【記憶化版本】
    best(node) = max(搶 node + 四個孫子的 best, 兩個孩子的 best)
    需要雜湊表存結果；回傳兩個值的版本更乾淨。"""),
 ],
 "approaches": [
   ap("解法一", "記憶化（孩子 vs 孫子）", [
     ("c", S["p337_memo"]),
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "樹形 DP：回傳（搶, 不搶）", [
     ("c", S["p337"]),
   ], "O(n)", "O(h)", "", "遞迴深度", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["暴力遞迴", "指數", "O(h)"],
    ["一、記憶化", "O(n)", "O(n)"],
    ["二、回傳兩個值", "O(n)", "O(h) ✔"]]),
 "edges": [
   "<strong>只有根</strong> → 根的值。",
   "<strong>一條鏈</strong> → 退化成第 198 題。",
   "<strong>值為 0</strong> → 搶不搶都一樣。",
 ],
 "follow": [
   ("h", "打家劫舍系列"),
   ("c", "第 198 題：一排。第 213 題：環形（拆成兩排）。第 337 題：樹（每個節點回傳兩個狀態）。第 2560 題：二分答案 + 貪心。"),
 ],
 "related": [
   "<strong>第 198 題 打家劫舍</strong>",
   "<strong>第 213 題 打家劫舍 II</strong>",
   "<strong>第 968 題 監控二元樹</strong> —— 每個節點回傳三個狀態",
 ],
 "check": [
   "每個節點回傳的兩個值分別代表什麼？",
   "搶自己時，為什麼只能加孩子的 skip？",
   "為什麼「只搶某些整層」是錯的？",
 ],
})


# ==================== 338. Counting Bits ====================
S["p338"] = '''class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # ★ i >> 1 已經算過了；i 比它多的只有最低位
            ans[i] = ans[i >> 1] + (i & 1)
        return ans'''

S["p338_low"] = '''class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1        # 清掉最低位的 1，少一個 1
        return ans'''

S["p338_naive"] = '''class Solution:
    def countBits(self, n: int) -> List[int]:
        return [bin(i).count("1") for i in range(n + 1)]'''

_p338 = [S.load(x) for x in ("p338", "p338_low", "p338_naive")]
for n in range(0, 300):
    want = [bin(i).count("1") for i in range(n + 1)]
    for sol in _p338:
        assert sol.countBits(n) == want
print("P338 OK")

emit({
 "num": 338, "slug": "counting-bits",
 "en": [
   "Given an integer <code>n</code>, return <em>an array</em> <code>ans</code> <em>of length</em> <code>n + 1</code> <em>such that for each</em> <code>i</code> (<code>0 &lt;= i &lt;= n</code>)<em>,</em> <code>ans[i]</code> <em>is the <strong>number of</strong></em> <code>1</code><em><strong>'s</strong> in the binary representation of</em> <code>i</code>.",
   "<strong>Follow up:</strong> It is very easy to come up with a solution with a runtime of <code>O(n log n)</code>. Can you do it in linear time <code>O(n)</code> and possibly in a single pass? "
   "Can you do it without using any built-in function (i.e., like <code>__builtin_popcount</code> in C++)?",
 ],
 "zh": [
   "給你整數 <code>n</code>，回傳長度 <code>n + 1</code> 的陣列 <code>ans</code>，<code>ans[i]</code> 是 <code>i</code> 的二進位表示中 <code>1</code> 的個數（<code>0 ≤ i ≤ n</code>）。",
   "<strong>進階：</strong><code>O(n log n)</code> 很容易，能做到 <code>O(n)</code> 嗎？能不用內建的 popcount 函式嗎？",
 ],
 "examples": """範例 1
  輸入：n = 2
  輸出：[0,1,1]

範例 2
  輸入：n = 5
  輸出：[0,1,1,2,1,2]
  說明：0, 1, 10, 11, 100, 101""",
 "constraints": [
   "0 ≤ <code>n</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【用前面算過的答案 —— DP】

【方法一：右移一位】
    i >> 1 就是把 i 的最低位去掉：
        i = 1011 (11)
        i >> 1 = 101 (5)
    所以 ans[i] = ans[i >> 1] + (i 的最低位)
    i >> 1 < i，一定已經算過了。

【方法二：清掉最低位的 1】
    i & (i - 1) 會把 i 最低位的 1 變成 0（第 231 題用過）：
        i = 1100 (12)
        i & (i-1) = 1000 (8)
    所以 ans[i] = ans[i & (i - 1)] + 1

【規律】
    偶數 2k：和 k 的 1 個數相同（多一個 0 在後面）
    奇數 2k+1：比 k 多一個"""),
   ("t", ["i", "0", "1", "2", "3", "4", "5", "6", "7", "8"],
    [["二進位", "0", "1", "10", "11", "100", "101", "110", "111", "1000"],
     ["ans[i]", "0", "1", "1", "2", "1", "2", "2", "3", "1"]]),
 ],
 "approaches": [
   ap("解法一", "逐一計算", [
     ("c", S["p338_naive"]),
   ], "O(n log n)", "O(1)", "不計輸出", ""),

   ap("解法二", "DP：清掉最低位的 1", [
     ("c", S["p338_low"]),
   ], "O(n)", "O(1)", "", "不計輸出"),

   ap("解法三", "DP：右移一位", [
     ("c", S["p338"]),
   ], "O(n)", "O(1)", "", "不計輸出", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、逐一計算", "O(n log n)", "最直接"],
    ["二、i &amp; (i−1)", "O(n)", ""],
    ["三、i &gt;&gt; 1", "O(n)", "最好記 ✔"]]),
 "edges": [
   "<strong>n = 0</strong> → <code>[0]</code>。",
   "<strong>2 的冪</strong> → 1 個 1。",
 ],
 "follow": [
   ("h", "位元 DP 的其他應用"),
   ("c", "狀態壓縮 DP 中經常要知道一個遮罩有幾個 1，就可以用這個方法預先算好整張表。"),
 ],
 "related": [
   "<strong>第 191 題 位元 1 的個數</strong>",
   "<strong>第 231 題 2 的冪</strong>",
   "<strong>第 461 題 漢明距離</strong>",
 ],
 "check": [
   "i &gt;&gt; 1 和 i 的 1 的個數差多少？",
   "i &amp; (i − 1) 和 i 的 1 的個數差多少？",
 ],
})


# ==================== 341. Flatten Nested List Iterator ====================
class _NI:
    """題目提供的 NestedInteger 介面（測試用）。"""

    def __init__(self, x):
        self._x = x

    def isInteger(self):
        return isinstance(self._x, int)

    def getInteger(self):
        return self._x if isinstance(self._x, int) else None

    def getList(self):
        return [_NI(y) for y in self._x] if not isinstance(self._x, int) else None


S["p341"] = '''# class NestedInteger:
#    def isInteger(self) -> bool: ...
#    def getInteger(self) -> int: ...
#    def getList(self) -> [NestedInteger]: ...

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = nestedList[::-1]          # 反過來放，pop() 拿到的是最前面的

    def _settle(self) -> None:
        # ★ 把頂端的串列展開，直到頂端是整數（或堆疊空了）
        while self.stack and not self.stack[-1].isInteger():
            self.stack.extend(self.stack.pop().getList()[::-1])

    def next(self) -> int:
        self._settle()
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        self._settle()                          # 空串列 [] 要在這裡被跳過
        return bool(self.stack)'''

S["p341_gen"] = '''class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def walk(lst):                          # 產生器：遞迴地逐一吐出整數
            for x in lst:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    yield from walk(x.getList())
        self.gen = walk(nestedList)
        self._advance()

    def _advance(self):
        self.peeked = next(self.gen, None)       # 預先拿一個（整數不會是 None）

    def next(self) -> int:
        val = self.peeked
        self._advance()
        return val

    def hasNext(self) -> bool:
        return self.peeked is not None'''


def _flat(x):
    return [x] if isinstance(x, int) else [z for y in x for z in _flat(y)]


def _rand_nested(d=0):
    out = []
    for _ in range(random.randrange(0, 4)):
        if d < 3 and random.random() < 0.4:
            out.append(_rand_nested(d + 1))
        else:
            out.append(random.randint(-5, 5))
    return out


for key in ("p341", "p341_gen"):
    cls = S.loadns(key, {"NestedInteger": _NI})["NestedIterator"]
    for raw in ([[1, 1], 2, [1, 1]], [1, [4, [6]]], [[]], [[], [[]], 3]):
        it = cls([_NI(x) for x in raw])
        out = []
        while it.hasNext():
            out.append(it.next())
        assert out == _flat(raw), (key, raw)
    for _ in range(1000):
        raw = _rand_nested()
        it = cls([_NI(x) for x in raw])
        out = []
        while it.hasNext():
            if random.random() < 0.3:
                assert it.hasNext()
            out.append(it.next())
        assert out == _flat(raw), (key, raw)
print("P341 OK")

emit({
 "num": 341, "slug": "flatten-nested-list-iterator",
 "en": [
   "You are given a nested list of integers <code>nestedList</code>. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.",
   "Implement the <code>NestedIterator</code> class:",
   ("ul", ["<code>NestedIterator(List&lt;NestedInteger&gt; nestedList)</code> Initializes the iterator with the nested list <code>nestedList</code>.",
           "<code>int next()</code> Returns the next integer in the nested list.",
           "<code>boolean hasNext()</code> Returns <code>true</code> if there are still some integers in the nested list and <code>false</code> otherwise."]),
   "If <code>res</code> matches the expected flattened list, then your code will be judged as correct.",
 ],
 "zh": [
   "給你一個巢狀的整數串列 <code>nestedList</code>：每個元素要嘛是整數，要嘛是另一個串列（裡面又可以是整數或串列）。請實作一個迭代器，把它<strong>攤平</strong>後依序輸出。",
   ("ul", ["<code>next()</code>：回傳下一個整數。",
           "<code>hasNext()</code>：還有沒有整數。"]),
   "元素是透過題目提供的 <code>NestedInteger</code> 介面存取：<code>isInteger()</code>、<code>getInteger()</code>、<code>getList()</code>。",
 ],
 "examples": """範例 1
  輸入：nestedList = [[1,1],2,[1,1]]
  輸出：[1,1,2,1,1]

範例 2
  輸入：nestedList = [1,[4,[6]]]
  輸出：[1,4,6]""",
 "constraints": [
   "1 ≤ <code>nestedList.length</code> ≤ 500",
   "整數的值在 <code>[−10⁶, 10⁶]</code> 之間",
 ],
 "idea": [
   ("c", """【最簡單：建構時整個攤平存進陣列】
    寫起來短，但如果巢狀結構很大、只需要前幾個元素，就浪費了。

【惰性展開：用堆疊】
    堆疊存「還沒處理的元素」，頂端是下一個要處理的。
    需要下一個整數時：
        頂端是串列 -> 彈出來，把它的元素「反過來」推回去
        重複直到頂端是整數
    反過來推，才能讓串列的第一個元素在頂端。

【hasNext 要負責展開】
    陷阱：[[]] 或 [[], [[]]] —— 堆疊不是空的，但其實沒有任何整數。
    所以 hasNext 必須先把頂端展開到整數為止，
    再判斷堆疊是否為空。

【產生器版本】
    Python 的 yield from 可以把遞迴寫成惰性的迭代器，
    再加上「預先拿一個」就能實作 hasNext。"""),
   ("c", """  堆疊（頂端在右）       動作
  [ [1,1]  2  [1,1] ]  -> 反放：[ [1,1]  2  [1,1] ] 的反序
  頂端 [1,1] 是串列     -> 展開：...  2  1  1
  頂端 1 是整數          -> next() 回傳 1"""),
 ],
 "approaches": [
   ap("解法一", "堆疊惰性展開", [
     ("c", S["p341"]),
   ], "攤銷 O(1)", "O(深度 + 寬度)", "每個元素進出堆疊常數次", "", optimal=True),

   ap("解法二", "產生器（yield from）", [
     ("c", S["p341_gen"]),
     "這裡用 None 當作「已經結束」的標記是安全的，因為元素一定是整數。如果元素可能是任意型別，要改用第 284 題的旗標技巧。",
   ], "攤銷 O(1)", "O(深度)", "", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["全部先攤平", "O(N)", "O(N)", "最簡單但不惰性"],
    ["一、堆疊", "攤銷 O(1)", "O(D + W)", "標準 ✔"],
    ["二、產生器", "攤銷 O(1)", "O(D)", "Python 特有的優雅"]]),
 "edges": [
   "<strong>空的巢狀串列</strong>（<code>[[]]</code>、<code>[[], [[]]]</code>）→ hasNext 必須是 false。",
   "<strong>很深的巢狀</strong> → 堆疊版本不受遞迴限制。",
   "<strong>連續呼叫 hasNext</strong> → 展開只做一次，不能消耗元素。",
 ],
 "follow": [
   ("h", "迭代器三部曲"),
   ("c", "第 173 題（BST 迭代器）、第 284 題（窺視迭代器）、第 341 題（本題）都用同一個想法：用堆疊把「遞迴走訪」改寫成「按需前進」。"),
 ],
 "related": [
   "<strong>第 173 題 二元搜尋樹迭代器</strong>",
   "<strong>第 284 題 窺視迭代器</strong>",
   "<strong>第 385 題 迷你語法分析器</strong> —— 建立 NestedInteger",
 ],
 "check": [
   "為什麼串列展開時要反過來推進堆疊？",
   "hasNext 為什麼要先展開？舉一個不展開會出錯的例子。",
 ],
})


# ==================== 342. Power of Four ====================
S["p342"] = '''class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # ★ 2 的冪（只有一個 1），而且那個 1 在偶數位（第 0、2、4… 位）
        return n > 0 and n & (n - 1) == 0 and n & 0x55555555 != 0'''

S["p342_mod"] = '''class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 4^k ≡ 1 (mod 3)，而 2·4^k ≡ 2 (mod 3)
        return n > 0 and n & (n - 1) == 0 and n % 3 == 1'''

_p342 = [S.load(x) for x in ("p342", "p342_mod")]
_pw4 = {4 ** i for i in range(16)}
for n in list(range(-40, 5000)) + [4 ** 15, 2 ** 31 - 1, 2 ** 29, 2 ** 30]:
    for sol in _p342:
        assert sol.isPowerOfFour(n) == (n in _pw4), n
print("P342 OK")

emit({
 "num": 342, "slug": "power-of-four",
 "en": [
   "Given an integer <code>n</code>, return <code>true</code> <em>if it is a power of four. Otherwise, return</em> <code>false</code>.",
   "An integer <code>n</code> is a power of four, if there exists an integer <code>x</code> such that <code>n == 4<sup>x</sup></code>.",
   "<strong>Follow up:</strong> Could you solve it without loops/recursion?",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，判斷它是不是 4 的冪次（存在整數 <code>x</code> 使 <code>n == 4<sup>x</sup></code>）。",
   "<strong>進階：</strong>能不用迴圈或遞迴嗎？",
 ],
 "examples": """範例 1
  輸入：n = 16
  輸出：true

範例 2
  輸入：n = 5
  輸出：false

範例 3
  輸入：n = 1
  輸出：true""",
 "constraints": [
   "−2³¹ ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【4 的冪一定是 2 的冪】
    4^k = 2^(2k) -> 二進位只有一個 1，而且在【偶數位】：
        1 = 1         （第 0 位）
        4 = 100       （第 2 位）
        16 = 10000    （第 4 位）
    2 的冪但不是 4 的冪：2 = 10、8 = 1000 —— 1 在奇數位。

【方法一：遮罩】
    0x55555555 = 0101 0101 ... 0101（所有偶數位都是 1）
    n & 0x55555555 != 0 <=> 那個唯一的 1 在偶數位。

【方法二：mod 3】
    4 ≡ 1 (mod 3) -> 4^k ≡ 1 (mod 3)
    2·4^k ≡ 2 (mod 3)
    所以 2 的冪中，mod 3 == 1 的就是 4 的冪。

【不能用 3 的冪那招】
    4 不是質數：2 也整除 4^15，但 2 不是 4 的冪。"""),
   ("t", ["n", "1", "2", "4", "8", "16", "32", "64"],
    [["二進位", "1", "10", "100", "1000", "10000", "100000", "1000000"],
     ["4 的冪？", "✔", "", "✔", "", "✔", "", "✔"],
     ["n % 3", "1", "2", "1", "2", "1", "2", "1"]]),
 ],
 "approaches": [
   ap("解法一", "2 的冪 + 偶數位遮罩", [
     ("c", S["p342"]),
   ], "O(1)", "O(1)", "", "", optimal=True),

   ap("解法二", "2 的冪 + mod 3", [
     ("c", S["p342_mod"]),
   ], "O(1)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、遮罩", "O(1)", "位元運算 ✔"],
    ["二、mod 3", "O(1)", "數論"]]),
 "edges": [
   "<strong>n = 1</strong> → true（4⁰）。",
   "<strong>2 的奇數次冪</strong>（2、8、32…）→ 是 2 的冪但不是 4 的冪。",
   "<strong>n ≤ 0</strong> → false。",
 ],
 "follow": [
   ("h", "冪次判斷三兄弟"),
   ("c", "2 的冪：一個 1。3 的冪：整除 3¹⁹。4 的冪：一個 1 在偶數位。"),
 ],
 "related": [
   "<strong>第 231 題 2 的冪</strong>",
   "<strong>第 326 題 3 的冪</strong>",
 ],
 "check": [
   "4 的冪在二進位中有什麼特徵？",
   "0x55555555 是什麼？",
   "為什麼不能用「整除最大的 4 的冪」來判斷？",
 ],
})
