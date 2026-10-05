# -*- coding: utf-8 -*-
"""第 646、647、648、649、650、652、653、654 題。"""
import random
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import combinations
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, nodes, bst, ser

S = Src()
random.seed(646)


# ==================== 646. Maximum Length of Pair Chain ====================
S["p646"] = '''class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda p: p[1])          # ★ 依結尾排序：結尾越早，留給後面的空間越多
        res, end = 0, float("-inf")
        for a, b in pairs:
            if a > end:                         # 能接在目前鏈的後面
                res += 1
                end = b
        return res'''

_p646 = S.load("p646")
def _bf646(ps):
    ps = sorted(ps); n = len(ps); dp = [1] * n
    for i in range(n):
        for j in range(i):
            if ps[j][1] < ps[i][0]: dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
for _ in range(2000):
    ps = []
    for _ in range(random.randint(1, 8)):
        a = random.randint(-5, 5); ps.append([a, a + random.randint(1, 4)])
    assert _p646.findLongestChain([p[:] for p in ps]) == _bf646(ps)
print("P646 OK")

em({
 "num": 646, "title": "最長數對鏈",
 "desc": "就是區間排程：依結尾排序，貪心地挑能接上的；也可以當成 O(n²) 的 LIS 型 DP。",
 "zh": [
   "給你 <code>n</code> 個數對 <code>pairs[i] = [left, right]</code>（left &lt; right）。若 <code>b &lt; c</code>，數對 <code>[c, d]</code> 可以接在 <code>[a, b]</code> 後面形成鏈。",
   "回傳能形成的<strong>最長鏈</strong>長度。數對可以任意順序挑選，不必全部用到。",
 ],
 "idea": [
   ("c", """【這是區間排程問題】
    每個數對是一個區間，鏈 = 一組互不重疊（嚴格分開）的區間。
    要選最多個 -> 經典貪心：依結尾排序，能選就選。

【為什麼依結尾排序？】
    第一個選結尾最早的區間，留給後面的空間最大；
    任何最優解都可以把它的第一個區間換成這個，不會變差（交換論證）。

【DP 寫法】
    依開頭排序後，dp[i] = 以 i 結尾的最長鏈，和 LIS 相同，O(n²)。"""),
 ],
 "approaches": [
   ap("解法一", "排序 + LIS 型 DP", [("c", "依 left 排序\ndp[i] = 1 + max(dp[j])，j < i 且 pairs[j][1] < pairs[i][0]")], "O(n²)", "O(n)"),
   ap("解法二", "依結尾排序的貪心", [("c", S["p646"]), "驗證方式：和 DP 比對 2000 組。"], "O(n log n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>相接的端點</strong>（b == c）→ 不能接，要嚴格小於。", "<strong>只有一個數對</strong> → 1。"],
 "follow": [("h", "區間排程家族"), ("c", "第 435 題（移除最少區間使其不重疊 = n − 本題答案）、第 452 題（最少的箭射爆氣球）都是依結尾排序的貪心。")],
 "related": ["<strong>第 435 題 無重疊區間</strong>", "<strong>第 452 題 用最少數量的箭引爆氣球</strong>", "<strong>第 300 題 最長遞增子序列</strong>"],
 "check": ["為什麼要依結尾而不是開頭排序？", "b == c 能接上嗎？"],
})


# ==================== 647. Palindromic Substrings ====================
S["p647"] = '''class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        for c in range(2 * n - 1):              # ★ 2n-1 個中心：n 個字元 + n-1 個字元間隙
            l, r = c // 2, (c + 1) // 2         # c 偶數 -> 奇數長度；c 奇數 -> 偶數長度
            while l >= 0 and r < n and s[l] == s[r]:
                res += 1                        # 每擴展成功一次，就多一個迴文子字串
                l -= 1
                r += 1
        return res'''

_p647 = S.load("p647")
for _ in range(2000):
    s = "".join(random.choice("ab") for _ in range(random.randint(1, 10)))
    assert _p647.countSubstrings(s) == sum(s[i:j] == s[i:j][::-1] for i in range(len(s)) for j in range(i + 1, len(s) + 1))
print("P647 OK")

em({
 "num": 647, "title": "迴文子字串",
 "desc": "中心擴展：枚舉 2n−1 個中心（字元與字元間隙），每次成功擴展就多一個迴文，O(n²) 時間、O(1) 空間。",
 "zh": ["給你字串 <code>s</code>，回傳其中<strong>迴文子字串</strong>的個數。位置不同的子字串即使內容相同也分開計算。"],
 "idea": [
   ("c", """【每個迴文都有一個中心】
    奇數長度：中心是一個字元。
    偶數長度：中心是兩個字元之間的間隙。
    共 2n - 1 個中心。

【從中心往外擴】
    左右字元相同就繼續擴，每擴一次就是一個新的迴文。
    用 c = 0..2n-2 統一表示：l = c // 2、r = (c+1) // 2。

【DP 做法】
    dp[i][j] = s[i..j] 是否為迴文 = s[i]==s[j] 且 dp[i+1][j-1]。
    O(n²) 時間與空間。

【Manacher】
    利用對稱性可以做到 O(n)。"""),
 ],
 "approaches": [
   ap("解法", "中心擴展", [("c", S["p647"])], "O(n²)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>全部相同</strong> → n(n+1)/2。", "<strong>單一字元</strong> → 1。"],
 "follow": [("h", "Manacher 演算法"), ("c", "記錄目前延伸最右的迴文 [C−R, C+R]，新中心 i 落在裡面時，它的半徑至少是鏡像位置 2C−i 的半徑（但不超過右邊界），再從那裡繼續擴展。每個字元最多被右邊界越過一次，O(n)。")],
 "related": ["<strong>第 5 題 最長迴文子字串</strong>", "<strong>第 516 題 最長迴文子序列</strong>", "<strong>第 131 題 分割迴文串</strong>"],
 "check": ["為什麼有 2n − 1 個中心？", "c 如何換算成 l 和 r？"],
})


# ==================== 648. Replace Words ====================
S["p648"] = '''class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for w in dictionary:
            nd = trie
            for ch in w:
                nd = nd.setdefault(ch, {})
            nd["$"] = w                     # 標記：這裡是一個字根的結尾

        def shortest_root(word):
            nd = trie
            for ch in word:
                if "$" in nd:
                    return nd["$"]          # ★ 沿路第一個遇到的結尾 = 最短字根
                if ch not in nd:
                    return word             # 走不下去：沒有字根是它的前綴
                nd = nd[ch]
            return nd.get("$", word)

        return " ".join(shortest_root(w) for w in sentence.split())'''

_p648 = S.load("p648")
assert _p648.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery") == "the cat was rat by the bat"
assert _p648.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs") == "a a b c"
for _ in range(1500):
    d = ["".join(random.choice("ab") for _ in range(random.randint(1, 3))) for _ in range(random.randint(1, 4))]
    ws = ["".join(random.choice("ab") for _ in range(random.randint(1, 5))) for _ in range(random.randint(1, 5))]
    def rep(w):
        c = [r for r in d if w.startswith(r)]
        return min(c, key=len) if c else w
    assert _p648.replaceWords(d, " ".join(ws)) == " ".join(rep(w) for w in ws)
print("P648 OK")

em({
 "num": 648, "title": "單字替換",
 "desc": "把字根建成字典樹，每個單字沿樹走，遇到的第一個字根結尾就是最短字根。",
 "zh": [
   "英文中，<strong>字根</strong>後面接上其他字可以組成較長的<strong>衍生字</strong>，例如字根 <code>\"help\"</code> 加上 <code>\"ful\"</code> 變成 <code>\"helpful\"</code>。",
   "給你字根字典 <code>dictionary</code> 和句子 <code>sentence</code>，把句子中每個衍生字替換成它的字根；若有多個字根都符合，用<strong>最短</strong>的那個。回傳替換後的句子。",
 ],
 "idea": [
   ("c", """【問題：找單字的最短前綴，且這個前綴在字典中】

【暴力】
    對每個單字，從長度 1 開始試每個前綴是否在雜湊集合裡。
    O(L²) 每個單字（切片成本）。

【字典樹】
    把所有字根插入字典樹，結尾標記。
    每個單字沿著字典樹走：
        遇到結尾標記 -> 這就是最短的字根，停止
        走不下去 -> 沒有字根，保留原字
    每個單字 O(L)。"""),
 ],
 "approaches": [
   ap("解法", "字典樹", [("c", S["p648"]), "驗證方式：和「找所有是前綴的字根取最短」的暴力法比對 1500 組。"], "O(總字元數)", "O(字根總長)", optimal=True),
 ],
 "edges": ["<strong>沒有字根符合</strong> → 保留原單字。", "<strong>單字本身就是字根</strong> → 走完時檢查結尾標記。", "<strong>多個字根</strong> → 第一個遇到的最短。"],
 "follow": [("h", "字典樹的典型用途"), ("c", "前綴查詢：自動完成、最長公共前綴、拼字檢查。第 208 題是字典樹的基本實作，第 720 題、第 677 題也用它。")],
 "related": ["<strong>第 208 題 實作字典樹</strong>", "<strong>第 720 題 字典中最長的單字</strong>", "<strong>第 677 題 鍵值映射</strong>"],
 "check": ["為什麼第一個遇到的結尾就是最短字根？", "字典樹比雜湊集合好在哪裡？"],
})


# ==================== 649. Dota2 Senate ====================
S["p649"] = '''class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R = deque(i for i, c in enumerate(senate) if c == "R")
        D = deque(i for i, c in enumerate(senate) if c == "D")
        while R and D:
            r, d = R.popleft(), D.popleft()
            # ★ 先發言的人禁掉對方下一個人，自己排到下一輪（索引 + n）
            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)
        return "Radiant" if R else "Dire"'''

_p649 = S.load("p649")
def _sim649(s):
    alive = [True] * len(s); ban = {"R": 0, "D": 0}
    while True:
        for i, c in enumerate(s):
            if not alive[i]: continue
            if ban[c]:
                ban[c] -= 1; alive[i] = False; continue
            o = "D" if c == "R" else "R"
            if not any(alive[j] and s[j] == o for j in range(len(s))):
                return "Radiant" if c == "R" else "Dire"
            ban[o] += 1
for _ in range(2000):
    s = "".join(random.choice("RD") for _ in range(random.randint(1, 10)))
    assert _p649.predictPartyVictory(s) == _sim649(s), s
print("P649 OK")

em({
 "num": 649, "title": "Dota2 參議院",
 "desc": "貪心：每個人都禁掉「下一個要發言的對手」；用兩個佇列模擬，發言後索引加 n 排到下一輪。",
 "zh": [
   "Dota2 的參議院由天輝（Radiant，<code>'R'</code>）和夜魘（Dire，<code>'D'</code>）兩黨組成。依字串順序輪流行使權利，每人每輪可以選擇：",
   ("ul", ["<strong>禁止</strong>一位參議員的權利：被禁止的人在這一輪與之後各輪都失去所有權利。",
           "<strong>宣布勝利</strong>：如果還有權利的參議員都屬於同一黨，就宣布該黨勝利。"]),
   "每位參議員都很聰明，會採取對自己黨最有利的策略。給你字串 <code>senate</code>，預測哪一黨會勝利，回傳 <code>\"Radiant\"</code> 或 <code>\"Dire\"</code>。",
 ],
 "idea": [
   ("c", """【最佳策略：禁掉下一個要發言的對手】
    下一個對手如果不被禁，他會馬上禁掉我方的人；
    禁掉更後面的對手效果比較差。

【兩個佇列模擬】
    R、D 各放自己黨員的發言順序（索引）。
    每次比較兩個佇列的隊首：索引小的先發言，
        禁掉對方隊首（對方 popleft 後不放回）
        自己以「索引 + n」放回隊尾 —— 代表下一輪才再發言。
    某個佇列空了，另一黨勝。"""),
 ],
 "approaches": [
   ap("解法", "兩個佇列模擬", [("c", S["p649"]), "驗證方式：和逐輪逐人模擬「禁掉下一個對手」的版本比對 2000 組。"], "O(n)", "O(n)", "每一次比較淘汰一人", "", optimal=True),
 ],
 "edges": ["<strong>全部同一黨</strong> → 直接勝。", "<strong>\"RDD\"</strong> → R 禁第一個 D，第二個 D 禁 R → Dire 勝。"],
 "follow": [("h", "為什麼索引要加 n？"), ("c", "加 n 讓它排在這一輪所有人的後面、但保持在下一輪中的相對順序，等於模擬了環狀的發言順序。")],
 "related": ["<strong>第 735 題 小行星碰撞</strong>", "<strong>第 950 題 按遞增順序顯示卡牌</strong>"],
 "check": ["為什麼要禁掉「下一個」對手？", "發言後為什麼放回時索引要加 n？"],
})


# ==================== 650. 2 Keys Keyboard ====================
S["p650"] = '''class Solution:
    def minSteps(self, n: int) -> int:
        res, d = 0, 2
        while n > 1:
            while n % d == 0:
                res += d            # ★ 把長度乘以 d：複製 1 次 + 貼上 d-1 次 = d 步
                n //= d
            d += 1
        return res                  # 答案 = 質因數的總和'''

_p650 = S.load("p650")
dp = [0, 0] + [10 ** 9] * 1000
for i in range(2, 1001):
    for j in range(1, i):
        if i % j == 0:
            dp[i] = min(dp[i], dp[j] + i // j)
for n in range(1, 1001):
    assert _p650.minSteps(n) == dp[n]
print("P650 OK")

em({
 "num": 650, "title": "只有兩個鍵的鍵盤",
 "desc": "每一段「複製一次、貼上 k−1 次」把長度乘以 k、花 k 步；拆成質因數最划算，答案是質因數總和。",
 "zh": [
   "記事本上一開始只有一個字元 <code>'A'</code>。每一步可以做兩種操作之一：",
   ("ul", ["<strong>Copy All</strong>：複製目前所有字元（不能只複製一部分）。", "<strong>Paste</strong>：貼上上一次複製的內容。"]),
   "給你 <code>n</code>，回傳得到恰好 <code>n</code> 個 <code>'A'</code> 的<strong>最少步數</strong>。",
 ],
 "idea": [
   ("c", """【操作的結構】
    每次 Copy All 後接著貼上若干次：
        複製 1 次 + 貼上 k-1 次 = k 步，長度變成 k 倍。
    所以 n = k₁ × k₂ × ... × kₘ，總步數 = k₁ + k₂ + ... + kₘ。

【怎麼拆最好？】
    若 k = a × b（a, b >= 2），則 a + b <= a × b。
    拆開不會更差 -> 全部拆成質數最好。
    答案 = n 的質因數（含重複）總和。

【DP 角度】
    dp[i] = min(dp[j] + i/j)，j 是 i 的因數 —— O(n²)，結果相同。"""),
 ],
 "approaches": [
   ap("解法一", "DP", [("c", "dp[i] = min(dp[j] + i // j)，j 為 i 的因數")], "O(n²)", "O(n)"),
   ap("解法二", "質因數分解", [("c", S["p650"]), "驗證方式：1～1000 全部和 DP 比對。"], "O(√n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>n = 1</strong> → 0。", "<strong>n 是質數</strong> → n（複製一次、貼上 n−1 次）。"],
 "follow": [("h", "為什麼 a + b ≤ a × b？"), ("c", "a × b − a − b = (a−1)(b−1) − 1 ≥ 0，當 a, b ≥ 2。所以拆成更小的因數只會讓步數變少或不變。")],
 "related": ["<strong>第 651 題 四個鍵的鍵盤</strong>（付費）", "<strong>第 991 題 壞了的計算器</strong>"],
 "check": ["複製一次再貼上 k−1 次，長度和步數分別如何變化？", "為什麼拆成質因數最好？"],
})


# ==================== 652. Find Duplicate Subtrees ====================
S["p652"] = '''class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        ids = {}                    # 子樹結構 (左 id, 值, 右 id) -> 唯一編號
        count = Counter()
        res = []

        def dfs(nd):
            if not nd:
                return 0
            key = (dfs(nd.left), nd.val, dfs(nd.right))   # ★ 用孩子的編號描述子樹，比序列化字串短
            if key not in ids:
                ids[key] = len(ids) + 1
            uid = ids[key]
            count[uid] += 1
            if count[uid] == 2:     # 第二次出現時才加入，避免重複回傳
                res.append(nd)
            return uid

        dfs(root)
        return res'''

_p652 = S.load("p652", extra={"Counter": Counter})
def _sig(t): return None if t is None else (t.val, _sig(t.left), _sig(t.right))
for _ in range(1500):
    t = rand_tree(random.randint(1, 12), 0, 2)
    c = Counter(_sig(n) for n in nodes(t))
    want = sorted(map(str, (k for k, v in c.items() if v >= 2)))
    assert sorted(str(_sig(n)) for n in _p652.findDuplicateSubtrees(t)) == want
print("P652 OK")

em({
 "num": 652, "title": "尋找重複的子樹",
 "desc": "給每種子樹結構一個編號：(左編號, 值, 右編號) 映射到新編號，相同結構得到相同編號，O(n)。",
 "zh": [
   "給你二元樹的根節點，回傳所有<strong>重複的子樹</strong>。每一種重複的子樹只需回傳其中任意一個的根節點。",
   "兩棵樹重複是指它們結構相同且對應節點值相同。",
 ],
 "idea": [
   ("c", """【序列化每個子樹】
    "值,左序列,右序列" 當鍵，雜湊表計數。
    但字串長度可達 O(n)，總共 O(n²)。

【給結構編號】
    子樹的結構完全由 (左子樹編號, 值, 右子樹編號) 決定。
    第一次看到這個三元組 -> 給它新編號。
    相同的子樹一定得到相同的編號（歸納法）。
    每個節點 O(1) -> 總共 O(n)。

【只回傳一次】
    計數變成 2 的時候才加入答案。"""),
 ],
 "approaches": [
   ap("解法", "子樹結構編號", [("c", S["p652"]), "驗證方式：和「把每個子樹轉成巢狀 tuple 計數」的方法比對 1500 棵隨機樹。"], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>值相同但結構不同</strong> → 編號不同。", "<strong>出現三次以上</strong> → 只回傳一次。", "<strong>葉子重複</strong> → 也算。"],
 "follow": [("h", "雜湊合併（hash consing）"), ("c", "把相同結構共用同一個編號（或同一個物件）的技巧叫 hash consing，函數式語言與編譯器常用它節省記憶體並加速相等比較。")],
 "related": ["<strong>第 572 題 另一棵樹的子樹</strong>", "<strong>第 297 題 二元樹的序列化與反序列化</strong>", "<strong>第 49 題 字母異位詞分組</strong>"],
 "check": ["為什麼 (左編號, 值, 右編號) 足以描述一棵子樹？", "為什麼在計數為 2 時加入答案？"],
})


# ==================== 653. Two Sum IV - Input is a BST ====================
S["p653"] = '''class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            nd = stack.pop()
            if not nd:
                continue
            if k - nd.val in seen:
                return True                     # ★ 和兩數之和一樣：找之前出現過的互補值
            seen.add(nd.val)
            stack += [nd.left, nd.right]
        return False'''

_p653 = S.load("p653")
for _ in range(2000):
    vals = random.sample(range(-10, 10), random.randint(1, 8)); k = random.randint(-15, 15)
    want = any(a + b == k for a, b in combinations(vals, 2))
    assert _p653.findTarget(bst(vals), k) == want
print("P653 OK")

em({
 "num": 653, "title": "兩數之和 IV - 輸入二元搜尋樹",
 "desc": "任何走訪 + 雜湊集合即可；也可以利用中序有序性做雙指標。",
 "zh": ["給你一棵二元搜尋樹的根節點和整數 <code>k</code>，判斷樹中是否存在兩個<strong>不同的</strong>節點，它們的值相加等於 <code>k</code>。"],
 "idea": [
   ("c", """【第 1 題的翻版】
    走訪每個節點，查 k - val 是否看過，再把 val 加進集合。
    這對任何二元樹都成立。

【利用 BST】
    中序走訪得到有序陣列，再用雙指標（第 167 題）。
    進階：用兩個迭代器（一個正向中序、一個反向中序）做雙指標，
    只需 O(h) 額外空間。"""),
 ],
 "approaches": [
   ap("解法", "走訪 + 雜湊集合", [("c", S["p653"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>同一個節點用兩次</strong> → 不行；先查再加入就自然避免。", "<strong>只有一個節點</strong> → False。"],
 "follow": [("h", "BST 迭代器"), ("c", "第 173 題的 BST 迭代器可以 O(h) 空間依序產生值；做一個正向、一個反向，就能在樹上直接跑雙指標。")],
 "related": ["<strong>第 1 題 兩數之和</strong>", "<strong>第 167 題 兩數之和 II</strong>", "<strong>第 173 題 二元搜尋樹迭代器</strong>"],
 "check": ["為什麼要先查再加入？", "怎麼利用 BST 的有序性？"],
})


# ==================== 654. Maximum Binary Tree ====================
S["p654"] = '''class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []                              # 單調遞減堆疊：右側鏈（根 -> 最右節點）
        for x in nums:
            nd = TreeNode(x)
            last = None
            while stack and stack[-1].val < x:
                last = stack.pop()              # 比 x 小的都成為 x 的左子樹
            nd.left = last
            if stack:
                stack[-1].right = nd            # ★ x 成為「左邊第一個比它大的」的右孩子
            stack.append(nd)
        return stack[0]'''

from runner import TreeNode
_p654 = S.load("p654")
def _rec(a):
    if not a: return None
    i = a.index(max(a)); return (a[i], _rec(a[:i]), _rec(a[i + 1:]))
def _sig(t): return None if t is None else (t.val, _sig(t.left), _sig(t.right))
for _ in range(2000):
    a = random.sample(range(30), random.randint(1, 10))
    assert _sig(_p654.constructMaximumBinaryTree(a)) == _rec(a)
print("P654 OK")

em({
 "num": 654, "title": "最大二元樹",
 "desc": "遞迴直接照定義建是 O(n²)；單調堆疊一趟 O(n)：每個數的父節點是左右兩側第一個更大值中較小的那個。",
 "zh": [
   "給你一個元素互不相同的整數陣列 <code>nums</code>，用以下方式遞迴建立<strong>最大二元樹</strong>：",
   ("ol", ["根是陣列中的最大值。", "左子樹由最大值<strong>左邊</strong>的子陣列遞迴建立。", "右子樹由最大值<strong>右邊</strong>的子陣列遞迴建立。"]),
   "回傳建好的樹。",
 ],
 "idea": [
   ("c", """【照定義遞迴】
    找最大值、切兩半遞迴。遞增或遞減陣列會退化成 O(n²)。

【單調堆疊：O(n)】
    由左到右讀入 x：
        堆疊（遞減）中比 x 小的全部彈出，
        最後一個彈出的成為 x 的左孩子（它們都在 x 左邊且比 x 小，
            其中最大的那個是 x 左子樹的根）。
        若堆疊還有元素（左邊第一個比 x 大的），x 成為它的右孩子。
        推入 x。
    最後堆疊底部就是整棵樹的根（全域最大值）。

【這是笛卡兒樹】
    依索引是二元搜尋樹、依值是最大堆積的樹。"""),
 ],
 "approaches": [
   ap("解法一", "照定義遞迴", [("c", "i = nums.index(max(nums))\nroot.left = build(nums[:i]); root.right = build(nums[i+1:])")], "O(n²)", "O(n)", "最壞情況（有序陣列）"),
   ap("解法二", "單調堆疊", [("c", S["p654"]), "驗證方式：和遞迴定義的結果比對 2000 組。"], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>遞增陣列</strong> → 一路往左的鏈。", "<strong>遞減陣列</strong> → 一路往右的鏈。"],
 "follow": [("h", "笛卡兒樹的用途"), ("c", "笛卡兒樹可以在 O(n) 建立，配合 LCA 能 O(1) 回答區間最大值查詢（RMQ）。第 998 題（最大二元樹 II）是在尾端插入一個數的版本。")],
 "related": ["<strong>第 998 題 最大二元樹 II</strong>", "<strong>第 84 題 柱狀圖中最大的矩形</strong>", "<strong>第 503 題 下一個更大元素 II</strong>"],
 "check": ["為什麼最後一個被彈出的節點是 x 的左孩子？", "為什麼 x 是堆疊頂端（彈出後）的右孩子？"],
})
