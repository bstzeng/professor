# -*- coding: utf-8 -*-
"""第 775、777、778、779、780、781、782、783 題。"""
import random, heapq
from collections import Counter, deque
from itertools import permutations
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import bst

S = Src()
random.seed(775)


# ==================== 775. Global and Local Inversions ====================
S["p775"] = '''class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        # 局部倒置一定是全域倒置；兩者相等 <=> 沒有「距離 >= 2」的倒置
        # ★ 對排列來說，等價於每個數離它排序後的位置不超過 1
        return all(abs(x - i) <= 1 for i, x in enumerate(nums))'''

_p775 = S.load("p775")
for n in range(1, 8):
    for p in permutations(range(n)):
        g = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        l = sum(p[i] > p[i + 1] for i in range(n - 1))
        assert _p775.isIdealPermutation(list(p)) == (g == l)
print("P775 OK")

em({
 "num": 775, "title": "全域倒置與局部倒置",
 "desc": "局部倒置一定是全域倒置，所以兩者相等 ⇔ 沒有距離 ≥ 2 的倒置 ⇔ 每個數離它的正確位置不超過 1。",
 "zh": [
   "給你 <code>[0, n−1]</code> 的一個排列 <code>nums</code>。",
   ("ul", ["<strong>全域倒置</strong>：<code>i &lt; j</code> 且 <code>nums[i] &gt; nums[j]</code> 的數對個數。",
           "<strong>局部倒置</strong>：<code>nums[i] &gt; nums[i+1]</code> 的位置個數。"]),
   "判斷全域倒置的數量是否等於局部倒置的數量。",
 ],
 "idea": [
   ("c", """【局部 ⊆ 全域】
    每個局部倒置都是全域倒置（j = i+1 的特例）。
    所以兩者相等 <=> 不存在 j >= i+2 的倒置。

【轉成局部條件】
    做法一：對每個 i，檢查 nums[i] > min(nums[i+2:])，
            從右往左維護後綴最小值，O(n)。
    做法二（排列專用）：
        若某個數 x 離正確位置 x 超過 1，
        例如 x 在位置 i <= x - 2：右邊有至少 2 個比 x 小的數……
        其中至少一個距離 >= 2 -> 有非局部倒置。
        反之每個數最多偏離 1，只可能和鄰居交換 -> 只有局部倒置。
        所以：|nums[i] - i| <= 1 對所有 i 成立。"""),
 ],
 "approaches": [
   ap("解法", "檢查偏離量", [("c", S["p775"]), "驗證方式：n ≤ 7 的所有排列都和直接計算兩種倒置數比對。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>已排序</strong> → 兩者都是 0。", "<strong>[1, 2, 0]</strong> → 0 偏離 2，False。"],
 "follow": [("h", "計算全域倒置數"), ("c", "一般情況下數逆序對需要合併排序或樹狀陣列，O(n log n)（第 493 題、劍指 Offer 51）。本題只問相等與否，所以有 O(n) 的捷徑。")],
 "related": ["<strong>第 493 題 翻轉對</strong>", "<strong>第 629 題 K 個逆序對陣列</strong>"],
 "check": ["為什麼局部倒置一定是全域倒置？", "為什麼偏離量不超過 1 就保證相等？"],
})


# ==================== 777. Swap Adjacent in LR String ====================
S["p777"] = '''class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        # 去掉 X 後，L 和 R 的相對順序必須相同（L、R 不能互相穿越）
        if start.replace("X", "") != result.replace("X", ""):
            return False
        j = 0
        for i, c in enumerate(start):
            if c == "X":
                continue
            while result[j] == "X":
                j += 1
            # ★ L 只能往左移（目標位置 <= 原位置），R 只能往右移
            if c == "L" and j > i or c == "R" and j < i:
                return False
            j += 1
        return True'''

_p777 = S.load("p777")
def _bf777(s, t):
    seen = {s}; q = deque([s])
    while q:
        u = q.popleft()
        if u == t: return True
        for i in range(len(u) - 1):
            pair = u[i:i + 2]
            if pair == "XL": v = u[:i] + "LX" + u[i + 2:]
            elif pair == "RX": v = u[:i] + "XR" + u[i + 2:]
            else: continue
            if v not in seen: seen.add(v); q.append(v)
    return False
for _ in range(2000):
    n = random.randint(1, 7)
    s = "".join(random.choice("LRX") for _ in range(n)); t = "".join(random.choice("LRX") for _ in range(n))
    if random.random() < 0.5:
        t = list(s); random.shuffle(t); t = "".join(t)
    assert _p777.canTransform(s, t) == _bf777(s, t), (s, t)
print("P777 OK")

em({
 "num": 777, "title": "在 LR 字串中交換相鄰字元",
 "desc": "\"XL→LX\" 讓 L 往左移、\"RX→XR\" 讓 R 往右移，而且 L、R 不能互相穿越：去掉 X 後順序相同，且每個 L 不往右、每個 R 不往左。",
 "zh": [
   "給你只含 <code>'L'</code>、<code>'R'</code>、<code>'X'</code> 的字串 <code>start</code> 和 <code>result</code>。每一步可以把一個 <code>\"XL\"</code> 換成 <code>\"LX\"</code>，或把一個 <code>\"RX\"</code> 換成 <code>\"XR\"</code>。",
   "判斷能否把 <code>start</code> 變成 <code>result</code>。",
 ],
 "idea": [
   ("c", """【把 X 看成空格】
    XL -> LX：L 往左移一格（穿過空格）
    RX -> XR：R 往右移一格

【不變量】
    1. L 和 R 不能互相穿越 -> 去掉 X 後的序列必須相同。
    2. L 只能往左：每個 L 在 result 中的位置 <= 在 start 中的位置。
    3. R 只能往右：每個 R 在 result 中的位置 >= 在 start 中的位置。

【充分性】
    這三個條件滿足時，總是能找到移動順序（例如先移動需要往左的 L，
    由左而右處理；R 由右而左處理），不會被卡住。

【雙指標】
    兩個字串各自跳過 X，依序配對非 X 的字元，檢查位置關係。"""),
 ],
 "approaches": [
   ap("解法", "雙指標 + 不變量", [("c", S["p777"]), "驗證方式：和 BFS 窮舉所有可達字串的方法比對 2000 組。"], "O(n)", "O(n)", "", "replace 產生的副本", optimal=True),
 ],
 "edges": ["<strong>L 需要往右</strong> → 不可能。", "<strong>L、R 順序不同</strong>（如 \"RL\" → \"LR\"）→ 不可能。", "<strong>X 的數量</strong> → 由第一個條件自動保證相同。"],
 "follow": [("h", "找不變量"), ("c", "「某種操作能不能把 A 變成 B」的題目，關鍵常常是找出操作不會改變的量（不變量），再證明不變量相同就一定可達。第 2337 題（移動片段得到字串）幾乎是同一題。")],
 "related": ["<strong>第 2337 題 移動片段得到字串</strong>", "<strong>第 838 題 推骨牌</strong>"],
 "check": ["為什麼 L 和 R 不能互相穿越？", "L 和 R 各自只能往哪個方向移動？"],
})


# ==================== 778. Swim in Rising Water ====================
S["p778"] = '''class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]               # (到達這格所需的最低水位, 列, 欄)
        while pq:
            t, i, j = heapq.heappop(pq)
            if (i, j) == (n - 1, n - 1):
                return t
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                    seen.add((x, y))
                    # ★ 路徑的成本是「途中最高的格子」，不是總和
                    heapq.heappush(pq, (max(t, grid[x][y]), x, y))'''

_p778 = S.load("p778")
assert _p778.swimInWater([[0, 2], [1, 3]]) == 3
assert _p778.swimInWater([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]]) == 16
for _ in range(500):
    n = random.randint(1, 5); vals = list(range(n * n)); random.shuffle(vals)
    g = [vals[i * n:(i + 1) * n] for i in range(n)]
    t = 0
    while True:
        if g[0][0] <= t:
            seen = {(0, 0)}; st = [(0, 0)]
            while st:
                i, j = st.pop()
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen and g[x][y] <= t:
                        seen.add((x, y)); st.append((x, y))
            if (n - 1, n - 1) in seen: break
        t += 1
    assert _p778.swimInWater(g) == t
print("P778 OK")

em({
 "num": 778, "title": "水位上升的泳池中游泳",
 "desc": "找一條路徑使「途中最高的格子」最小——瓶頸最短路：把 Dijkstra 的加法換成 max；也可以二分水位或用聯合查找。",
 "zh": [
   "給你一個 <code>n x n</code> 的格子，<code>grid[i][j]</code> 是該格的海拔（0～n²−1 各出現一次）。下雨後，時間 t 時所有地方的水深都是 t。",
   "你可以從一格游到上下左右相鄰的格子，前提是兩格的海拔都不超過 t（游泳本身不花時間）。從 <code>(0, 0)</code> 出發，回傳能到達 <code>(n−1, n−1)</code> 的<strong>最早時間</strong>。",
 ],
 "idea": [
   ("c", """【答案是什麼？】
    一條路徑能在時間 t 走完 <=> 路徑上每一格的海拔 <= t。
    -> 要找一條「最高點」最低的路徑，答案就是那個最高點。

【做法一：修改版 Dijkstra】
    路徑成本 = max(經過的格子)，仍然滿足「延長路徑成本不會變小」，
    所以 Dijkstra 適用：把 d + w 換成 max(d, w)。

【做法二：二分答案】
    給定 t，用 BFS 檢查只走 <= t 的格子能否到達終點。
    t 在 [0, n²-1] 二分，O(n² log n)。

【做法三：聯合查找】
    依海拔由低到高逐一「打開」格子，和已打開的鄰居合併；
    起點和終點第一次連通時的海拔就是答案。"""),
 ],
 "approaches": [
   ap("解法", "Dijkstra（成本取最大值）", [("c", S["p778"]), "驗證方式：和「水位從 0 往上逐一嘗試，每次 DFS 檢查是否連通」的暴力法比對 500 組。"], "O(n² log n)", "O(n²)", optimal=True),
 ],
 "edges": ["<strong>n = 1</strong> → grid[0][0]。", "<strong>起點海拔很高</strong> → 至少要等到起點的海拔。"],
 "follow": [("h", "瓶頸路徑"), ("c", "「最小化路徑上的最大值」也叫 minimax 路徑：第 1631 題（最小體力消耗路徑）、第 1102 題（得分最高的路徑，付費）。它恰好是最小生成樹上兩點之間的路徑。")],
 "related": ["<strong>第 1631 題 最小體力消耗路徑</strong>", "<strong>第 743 題 網路延遲時間</strong>", "<strong>第 1102 題 得分最高的路徑</strong>（付費）"],
 "check": ["為什麼答案是路徑上最高的格子？", "Dijkstra 要改哪裡？為什麼仍然正確？"],
})


# ==================== 779. K-th Symbol in Grammar ====================
S["p779"] = '''class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # ★ 第 k 個（從 1 開始）的值 = (k-1) 的二進位中 1 的個數的奇偶
        return bin(k - 1).count("1") % 2'''

_p779 = S.load("p779")
rows = ["0"]
for _ in range(14):
    rows.append("".join("01" if c == "0" else "10" for c in rows[-1]))
for n in range(1, 15):
    for k in range(1, len(rows[n - 1]) + 1):
        assert _p779.kthGrammar(n, k) == int(rows[n - 1][k - 1])
print("P779 OK")

em({
 "num": 779, "title": "第 K 個語法符號",
 "desc": "第 k 個符號由它的父節點決定：右孩子會翻轉；一路追到根，翻轉次數就是 k−1 的二進位中 1 的個數（Thue–Morse 數列）。",
 "zh": [
   "第一列是 <code>\"0\"</code>。之後每一列由上一列產生：把每個 <code>0</code> 換成 <code>01</code>、每個 <code>1</code> 換成 <code>10</code>。",
   "給你 <code>n</code> 和 <code>k</code>，回傳第 <code>n</code> 列的第 <code>k</code> 個符號（索引從 1 開始）。",
 ],
 "idea": [
   ("c", """【看成一棵完全二元樹】
    第 n 列的第 k 個，是第 n-1 列第 ⌈k/2⌉ 個的孩子：
        左孩子（k 奇數）= 和父節點相同
        右孩子（k 偶數）= 和父節點相反
    遞迴往上，根是 0。

【翻轉幾次？】
    用 0 起算的索引 k-1，它的二進位從高到低就是「從根往下走的路線」，
    每個 1 代表走右孩子 = 翻轉一次。
    答案 = popcount(k-1) % 2。

    與 n 無關！（只要 k 在範圍內）
    這就是 Thue–Morse 數列：0 1 1 0 1 0 0 1 ..."""),
 ],
 "approaches": [
   ap("解法", "位元計數", [("c", S["p779"]), "驗證方式：直接生成前 14 列，檢查每一個位置。"], "O(log k)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>k = 1</strong> → 0。", "<strong>n 很大</strong> → 不能真的生成（第 30 列有 2²⁹ 個字元）。"],
 "follow": [("h", "Thue–Morse 數列"), ("c", "這個數列有許多有趣的性質：它不包含任何三次重複（XXX）的片段；用它決定兩人輪流挑選的順序（ABBABAAB…）比單純輪流更公平。")],
 "related": ["<strong>第 1545 題 找出第 N 個二進位字串中的第 K 位</strong>", "<strong>第 191 題 位元 1 的個數</strong>"],
 "check": ["右孩子與父節點的關係是什麼？", "為什麼答案和 n 無關？"],
})


# ==================== 780. Reaching Points ====================
S["p780"] = '''class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # ★ 倒著走：(tx, ty) 的前一步唯一確定 —— 較大的那個減去較小的
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            if tx > ty:
                if ty > sy:
                    tx %= ty                # 連續減很多次 = 取餘數（像輾轉相除法）
                else:
                    return (tx - sx) % ty == 0      # ty 已經到底：只能一直減 ty
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0
        return tx == sx and ty == sy'''

_p780 = S.load("p780")
assert _p780.reachingPoints(1, 1, 3, 5) and not _p780.reachingPoints(1, 1, 2, 2) and _p780.reachingPoints(1, 1, 1, 1)
for _ in range(3000):
    sx, sy = random.randint(1, 6), random.randint(1, 6); tx, ty = random.randint(1, 30), random.randint(1, 30)
    reach = set(); st = [(sx, sy)]
    while st:
        x, y = st.pop()
        if (x, y) in reach or x > tx or y > ty: continue
        reach.add((x, y)); st += [(x + y, y), (x, x + y)]
    assert _p780.reachingPoints(sx, sy, tx, ty) == ((tx, ty) in reach)
assert _p780.reachingPoints(1, 1, 10 ** 9, 1)
print("P780 OK")

em({
 "num": 780, "title": "到達終點",
 "desc": "正著走有兩種選擇，倒著走卻是唯一的：較大的座標減去較小的；連續減用取餘數加速，就像輾轉相除法，O(log max)。",
 "zh": [
   "從點 <code>(sx, sy)</code> 出發，每一步可以變成 <code>(x, x + y)</code> 或 <code>(x + y, y)</code>。給你終點 <code>(tx, ty)</code>，判斷能否到達。",
   "所有座標都是 1～10⁹ 的正整數。",
 ],
 "idea": [
   ("c", """【正著走會分岔，倒著走不會】
    (tx, ty) 的前一步：
        若 tx > ty，上一步一定是 (tx - ty, ty)（另一種會讓 ty 變小的不可能，因為座標都是正的）
        若 ty > tx，上一步是 (tx, ty - tx)
        若相等，只有起點本身才可能（不能再往回）
    -> 倒推的路徑唯一。

【連續減太慢】
    (10⁹, 1) 要減 10⁹ 次。
    tx 一直大於 ty 時，會連續減 ty -> 直接 tx %= ty。
    這就是輾轉相除法，O(log max)。

【停在起點附近】
    取餘數可能「減過頭」跳過 sx：
    當 ty 已經等於 sy（不能再變），
    只要檢查 tx 能否從 sx 連加若干個 ty 得到：(tx - sx) % ty == 0。"""),
 ],
 "approaches": [
   ap("解法", "倒推 + 取餘數", [("c", S["p780"]), "驗證方式：和從起點 DFS 所有可達點（限制在終點範圍內）比對 3000 組；(1, 1) 到 (10⁹, 1) 也能瞬間算出。"], "O(log max(tx, ty))", "O(1)", optimal=True),
 ],
 "edges": ["<strong>起點等於終點</strong> → True。", "<strong>tx == ty 但不是起點</strong> → False。", "<strong>一個座標已經對齊</strong> → 改用整除判斷，不能繼續取餘數。"],
 "follow": [("h", "倒推的威力"), ("c", "當正向有多種選擇、反向卻唯一時，倒著想就能避免指數級的搜尋。第 991 題（壞了的計算器）也是倒推：從目標往回除以 2 或加 1。")],
 "related": ["<strong>第 991 題 壞了的計算器</strong>", "<strong>第 365 題 水壺問題</strong>"],
 "check": ["為什麼倒推的路徑是唯一的？", "為什麼可以用取餘數代替連續相減？", "什麼時候要改用整除判斷？"],
})


# ==================== 781. Rabbits in Forest ====================
S["p781"] = '''class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        for x, c in Counter(answers).items():
            g = x + 1                       # 回答 x 的兔子，同色的一群恰好 x+1 隻
            res += -(-c // g) * g           # ★ c 隻回答 x 的兔子至少需要 ⌈c / g⌉ 群
        return res'''

_p781 = S.load("p781")
assert _p781.numRabbits([1, 1, 2]) == 5 and _p781.numRabbits([10, 10, 10]) == 11
def _bf781(ans):
    # 窮舉把回答分組：同一組必須回答相同、而且組大小 <= x+1；總數 = Σ 每組的 (x+1)
    c = Counter(ans); tot = 0
    for x, k in c.items():
        best = None
        for groups in range(1, k + 1):
            if groups * (x + 1) >= k:
                best = groups * (x + 1); break
        tot += best
    return tot
for _ in range(2000):
    a = [random.randint(0, 4) for _ in range(random.randint(1, 10))]
    assert _p781.numRabbits(a) == _bf781(a)
print("P781 OK")

em({
 "num": 781, "title": "森林中的兔子",
 "desc": "回答 x 的兔子所屬的顏色恰好有 x+1 隻；c 隻都回答 x 時，至少分成 ⌈c/(x+1)⌉ 群，每群 x+1 隻。",
 "zh": [
   "森林裡有一些兔子，每隻兔子有一種顏色。你問了其中一些兔子：「還有多少隻兔子跟你同色？」答案記在 <code>answers</code> 中。",
   "回傳森林中兔子的<strong>最少</strong>數量。",
 ],
 "idea": [
   ("c", """【回答 x 的意思】
    牠的顏色共有 x + 1 隻（包含自己）。

【同樣回答 x 的兔子】
    可能是同一種顏色，但一種顏色最多只能容納 x+1 隻回答者。
    c 隻回答 x -> 至少 ⌈c / (x+1)⌉ 種顏色，
    每種顏色都有 x+1 隻（沒被問到的也算）。
    貢獻 ⌈c / (x+1)⌉ × (x+1)。

【回答不同的兔子】
    一定是不同顏色（同色的回答必須相同），各自獨立計算。"""),
 ],
 "approaches": [
   ap("解法", "分組計數", [("c", S["p781"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>回答 0</strong> → 每隻都是獨一無二的顏色。", "<strong>[10, 10, 10]</strong> → 同一群就夠，11 隻。", "<strong>[1, 1, 1]</strong> → 一群最多 2 隻，需要兩群，4 隻。"],
 "follow": [("h", "向上取整"), ("c", "Python 中 ⌈a / b⌉ 可以寫成 −(−a // b)，避免浮點數；其他語言常寫成 (a + b − 1) / b。")],
 "related": ["<strong>第 621 題 任務排程器</strong>"],
 "check": ["回答 x 的兔子，同色的有幾隻？", "為什麼回答不同的兔子一定不同色？"],
})


# ==================== 782. Transform to Chessboard ====================
S["p782"] = '''class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # 條件一：只能有兩種列（互為反相），欄同理 —— 用「每一格 = 第一列 ^ 第一欄 ^ 左上角」檢查
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]:
                    return -1
        row, col = board[0], [board[i][0] for i in range(n)]
        # 條件二：第一列與第一欄中 1 的個數必須是 n//2 或 (n+1)//2
        if not (n // 2 <= sum(row) <= (n + 1) // 2 and n // 2 <= sum(col) <= (n + 1) // 2):
            return -1

        def moves(line):
            # 和 0101... 不同的位置數；每次交換修正兩個位置
            diff = sum(x != i % 2 for i, x in enumerate(line))
            if n % 2:
                # ★ 奇數長度：開頭必須是較多的那個數字，只有一種目標；diff 必須是偶數
                return (diff if diff % 2 == 0 else n - diff) // 2
            return min(diff, n - diff) // 2      # 偶數長度：兩種目標取較少的

        return moves(row) + moves(col)'''

_p782 = S.load("p782")
assert _p782.movesToChessboard([[0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1]]) == 2
assert _p782.movesToChessboard([[0, 1], [1, 0]]) == 0 and _p782.movesToChessboard([[1, 0], [1, 0]]) == -1
def _bf782(b):
    n = len(b)
    def ok(m): return all(m[i][j] != m[i][j + 1] for i in range(n) for j in range(n - 1)) and all(m[i][j] != m[i + 1][j] for i in range(n - 1) for j in range(n))
    start = tuple(map(tuple, b)); seen = {start}; q = deque([(start, 0)])
    while q:
        m, d = q.popleft()
        if ok(m): return d
        for i in range(n):
            for j in range(i + 1, n):
                r = list(m); r[i], r[j] = r[j], r[i]; r = tuple(r)
                c = tuple(tuple(row[k] if k not in (i, j) else row[j if k == i else i] for k in range(n)) for row in m)
                for u in (r, c):
                    if u not in seen: seen.add(u); q.append((u, d + 1))
    return -1
for _ in range(300):
    n = random.randint(2, 4)
    if random.random() < 0.6:
        base = [[(i + j) % 2 for j in range(n)] for i in range(n)]
        rp = list(range(n)); cp = list(range(n)); random.shuffle(rp); random.shuffle(cp)
        b = [[base[rp[i]][cp[j]] for j in range(n)] for i in range(n)]
        if random.random() < 0.3: b[random.randrange(n)][random.randrange(n)] ^= 1
    else:
        b = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
    assert _p782.movesToChessboard(b) == _bf782(b), b
print("P782 OK")

em({
 "num": 782, "title": "變為棋盤",
 "desc": "交換列不改變任何一列的內容：合法的盤面只能有兩種互補的列（欄亦同），1 的個數要平衡；列與欄可以分開計算，各是一維的「變成 0101…」問題。",
 "zh": [
   "給你一個 <code>n x n</code> 的 0/1 矩陣。每一步可以交換任意兩<strong>列</strong>，或交換任意兩<strong>欄</strong>。",
   "回傳把它變成<strong>棋盤</strong>（任意兩個上下左右相鄰的格子都不同）的最少步數；不可能則回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【什麼樣的矩陣有可能？】
    交換欄只會重排每一列的內容；交換列不改變任何一列。
    棋盤只有兩種列：0101… 和 1010…，互為反相。
    所以原矩陣也必須只有兩種列，而且互為反相、數量各半（差不超過 1）；
    欄也一樣。
    「每一格 = 第一列 ^ 第一欄 ^ 左上角」這個檢查一次涵蓋了「只有兩種互補的列和欄」。

【列和欄可以分開算】
    換列只影響第一欄的順序，換欄只影響第一列的順序。
    -> 答案 = 把第一列排成交錯 + 把第一欄排成交錯。

【一維：把 line 交換成 0101… 或 1010…】
    diff = 和 0101… 不同的位置數；每次交換修正兩個位置 -> diff / 2。
    偶數長度：兩種目標都可以，取 min(diff, n - diff) / 2。
    奇數長度：只有一種目標（開頭必須是較多的那個數字），
              diff 是偶數的那個才是合法目標。"""),
 ],
 "approaches": [
   ap("解法", "條件檢查 + 列欄分開計算", [
     ("c", S["p782"]),
     "驗證方式：n ≤ 4 時和 BFS 窮舉所有列／欄交換序列比對 300 組（其中多數由棋盤隨機打亂產生）。",
   ], "O(n²)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>出現第三種列</strong> → −1。", "<strong>1 的個數不平衡</strong> → −1。", "<strong>奇數 n</strong> → 只有一種合法目標。"],
 "follow": [("h", "拆解成獨立的子問題"), ("c", "看似二維的交換問題，因為「換列」與「換欄」互不影響，可以拆成兩個一維問題分別求解再相加。")],
 "related": ["<strong>第 765 題 情侶牽手</strong>", "<strong>第 1529 題 最少的後綴翻轉次數</strong>"],
 "check": ["為什麼合法的矩陣只能有兩種互補的列？", "為什麼列和欄可以分開計算？", "奇數長度時怎麼決定目標？"],
})


# ==================== 783. Minimum Distance Between BST Nodes ====================
S["p783"] = '''class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        res, prev = float("inf"), None
        stack, nd = [], root
        while stack or nd:                  # 迭代中序走訪
            while nd:
                stack.append(nd)
                nd = nd.left
            nd = stack.pop()
            if prev is not None:
                res = min(res, nd.val - prev)   # ★ 有序序列的最小差在相鄰元素之間
            prev = nd.val
            nd = nd.right
        return res'''

_p783 = S.load("p783")
for _ in range(1500):
    vals = random.sample(range(100), random.randint(2, 12)); s = sorted(vals)
    assert _p783.minDiffInBST(bst(vals)) == min(b - a for a, b in zip(s, s[1:]))
print("P783 OK")

em({
 "num": 783, "title": "二元搜尋樹節點最小距離",
 "desc": "與第 530 題相同：中序走訪得到有序序列，最小差一定在相鄰元素之間；這裡示範迭代版的中序走訪。",
 "zh": ["給你一棵二元搜尋樹的根節點，回傳樹中任意兩個不同節點值之差的<strong>最小值</strong>。（本題與第 530 題相同。）"],
 "idea": [
   ("c", """【和第 530 題完全一樣】
    中序走訪 = 由小到大，最小差在相鄰元素之間。

【迭代版中序走訪】
    用堆疊模擬遞迴：
        一路往左走並推入堆疊
        彈出一個節點 -> 處理它
        轉向它的右子樹
    不需要遞迴，避免很深的樹造成堆疊溢位。"""),
 ],
 "approaches": [
   ap("解法", "迭代中序走訪", [("c", S["p783"])], "O(n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>只有兩個節點</strong> → 它們的差。", "<strong>樹很深</strong> → 迭代版不受遞迴深度限制。"],
 "follow": [("h", "中序走訪的三種寫法"), ("c", "遞迴（最直觀）、堆疊迭代（本題）、Morris（O(1) 空間，暫時修改樹的指標）。")],
 "related": ["<strong>第 530 題 二元搜尋樹的最小絕對差</strong>", "<strong>第 94 題 二元樹的中序走訪</strong>", "<strong>第 173 題 二元搜尋樹迭代器</strong>"],
 "check": ["迭代中序走訪的三個步驟是什麼？"],
})
