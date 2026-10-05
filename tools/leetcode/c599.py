# -*- coding: utf-8 -*-
"""第 599、600、605、606、609、611、617、621 題。"""
import random
from collections import Counter, defaultdict
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, nodes, ser

S = Src()
random.seed(599)


# ==================== 599. Minimum Index Sum of Two Lists ====================
S["p599"] = '''class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        pos = {s: i for i, s in enumerate(list1)}      # list1 中每個字串的索引
        best, res = float("inf"), []
        for j, s in enumerate(list2):
            if s in pos:
                t = pos[s] + j
                if t < best:
                    best, res = t, [s]                  # ★ 更小：重新開始
                elif t == best:
                    res.append(s)                       # 並列：加進去
        return res'''

_p599 = S.load("p599")
for _ in range(2000):
    pool = list("abcdefg")
    l1 = random.sample(pool, random.randint(1, 5)); l2 = random.sample(pool, random.randint(1, 5))
    if not set(l1) & set(l2):
        l2.append(l1[0])
    sums = {s: l1.index(s) + l2.index(s) for s in set(l1) & set(l2)}
    b = min(sums.values())
    assert sorted(_p599.findRestaurant(l1, l2)) == sorted(s for s in sums if sums[s] == b)
print("P599 OK")

em({
 "num": 599, "title": "兩個列表的最小索引總和",
 "desc": "把第一個列表建成「字串 → 索引」的雜湊表，掃第二個列表時計算索引和並保留最小的。",
 "zh": [
   "給你兩個字串陣列 <code>list1</code>、<code>list2</code>（各自的字串互不重複）。<strong>共同字串</strong>是同時出現在兩個陣列中的字串。",
   "回傳所有「兩邊索引和最小」的共同字串（順序不限）。",
 ],
 "idea": [
   ("c", """【雜湊表查索引】
    list1 建成 {字串: 索引}。
    掃 list2 的每個字串，若在表中，索引和 = i + j。

【維護最小值與答案】
    更小 -> 清空答案，只放這個
    相等 -> 加進答案"""),
 ],
 "approaches": [
   ap("解法", "雜湊表", [("c", S["p599"])], "O(m + n)", "O(m)", "", "", optimal=True),
 ],
 "edges": ["<strong>多個並列</strong> → 全部回傳。", "<strong>只有一個共同字串</strong> → 就是它。"],
 "follow": [("h", "提早結束"), ("c", "掃到 j > best 時就可以停：之後的索引和至少是 j，不可能更小。")],
 "related": ["<strong>第 1 題 兩數之和</strong>", "<strong>第 349 題 兩個陣列的交集</strong>"],
 "check": ["遇到更小的索引和時，答案要怎麼更新？"],
})


# ==================== 600. Non-negative Integers without Consecutive Ones ====================
S["p600"] = '''class Solution:
    def findIntegers(self, n: int) -> int:
        # f[k]：長度為 k、沒有連續 1 的二進位字串個數（就是費氏數列）
        f = [1, 2]
        for _ in range(32):
            f.append(f[-1] + f[-2])
        bits = bin(n)[2:]
        L = len(bits)
        res, prev = 0, "0"
        for i, b in enumerate(bits):
            if b == "1":
                res += f[L - i - 1]             # ★ 這一位填 0，後面 L-i-1 位可以任意（只要不連續 1）
                if prev == "1":
                    return res                  # n 本身有連續 1：之後的前綴都不合法，提早結束
            prev = b
        return res + 1                          # n 本身也合法'''

_p600 = S.load("p600")
_ok = [0] * 5001
for x in range(5001):
    _ok[x] = (1 if "11" not in bin(x) else 0) + (_ok[x - 1] if x else 0)
for x in range(5001):
    assert _p600.findIntegers(x) == _ok[x]
assert _p600.findIntegers(10 ** 9) == 2178309
print("P600 OK")

em({
 "num": 600, "title": "不含連續 1 的非負整數",
 "desc": "數位 DP：長度 k 不含連續 1 的二進位串個數是費氏數；沿著 n 的二進位逐位累加「這位改填 0」的情況。",
 "zh": ["給你正整數 <code>n</code>，回傳 <code>[0, n]</code> 範圍內，二進位表示中<strong>沒有連續兩個 1</strong> 的整數個數。"],
 "idea": [
   ("c", """【長度 k 的合法二進位串有幾個？】
    f[k]：結尾是 0 -> 前面 k-1 位任意合法：f[k-1]
          結尾是 1 -> 倒數第二位必須是 0：f[k-2]
    f[k] = f[k-1] + f[k-2]，f[0] = 1、f[1] = 2 —— 費氏數列。

【數 <= n 的合法數（數位 DP 的標準流程）】
    從最高位往下看 n 的二進位 b。
    當 b[i] = 1：
        若這一位改填 0，後面 L-i-1 位就不受 n 限制，
        任何合法串都行 -> 加上 f[L-i-1]。
        然後「這一位照 n 填 1」，繼續往下。
        但如果前一位也是 1，代表照 n 填已經出現 11，
        之後都不合法 -> 直接結束。
    當 b[i] = 0：只能填 0，繼續。
    走到底沒有中斷，代表 n 本身合法，再加 1。

【例】
    n = 5 = 101：
        第一位 1：改填 0 -> 0??，f[2] = 3（000,001,010）
        第三位 1：改填 0 -> 100，f[0] = 1
        n 本身 101 合法 +1
    答案 5（0,1,2,4,5）。"""),
 ],
 "approaches": [
   ap("解法", "數位 DP（費氏數）", [
     ("c", S["p600"]),
     "驗證方式：0～5000 全部和暴力計數比對；n = 10⁹ 的答案是 2178309。",
   ], "O(log n)", "O(log n)", optimal=True),
 ],
 "edges": ["<strong>n 本身有連續 1</strong> → 提早結束，不加最後的 1。", "<strong>n = 1</strong> → 2（0 和 1）。"],
 "follow": [("h", "數位 DP 的模板"), ("c", "「數 [0, n] 中滿足某條件的數」：逐位走 n，每一位若能填比 n 小的數字，之後就不受限制（free），用預先算好的表；同時檢查 n 自己的前綴是否還合法。第 233 題、第 902 題、第 1012 題都是同一套。")],
 "related": ["<strong>第 233 題 數字 1 的個數</strong>", "<strong>第 902 題 最大為 N 的數字組合</strong>", "<strong>第 1012 題 至少有 1 位重複的數字</strong>"],
 "check": ["長度 k 的合法串個數為什麼滿足費氏遞迴？", "什麼時候可以提早結束？", "最後的 +1 代表什麼？"],
})


# ==================== 605. Can Place Flowers ====================
S["p605"] = '''class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        bed = [0] + flowerbed + [0]             # 頭尾補 0，省去邊界判斷
        for i in range(1, len(bed) - 1):
            if bed[i - 1] == bed[i] == bed[i + 1] == 0:
                bed[i] = 1                      # ★ 貪心：能種就種，越早種越不會浪費空間
                n -= 1
        return n <= 0'''

_p605 = S.load("p605")
def _bf605(bed):
    best = 0
    L = len(bed)
    for mask in range(1 << L):
        b = bed[:]; ok = True; c = 0
        for i in range(L):
            if mask >> i & 1:
                if b[i]: ok = False; break
                b[i] = 1; c += 1
        if ok and all(not (b[i] and b[i + 1]) for i in range(L - 1)):
            best = max(best, c)
    return best
for _ in range(1500):
    L = random.randint(1, 9); bed = [0] * L
    for i in range(L):
        if random.random() < 0.3 and (i == 0 or bed[i - 1] == 0): bed[i] = 1
    n = random.randint(0, 4)
    assert _p605.canPlaceFlowers(bed[:], n) == (_bf605(bed) >= n)
print("P605 OK")

em({
 "num": 605, "title": "種花問題",
 "desc": "貪心：由左到右能種就種；頭尾補 0 讓邊界判斷變得一致。",
 "zh": ["一排花壇 <code>flowerbed</code>，1 代表已種花、0 代表空地，<strong>相鄰的地不能同時種花</strong>。給你整數 <code>n</code>，判斷能否再種下 <code>n</code> 朵花而不違反規則。"],
 "idea": [
   ("c", """【貪心：能種就種】
    由左往右，遇到「自己、左、右都是 0」的位置就種。
    為什麼越早種越好？在 i 種花只影響 i+1；
    如果不在 i 種而改在 i+1 種，會影響 i+2，只會更差。

【邊界處理】
    頭尾各補一個 0，第一格和最後一格就不用特判。"""),
 ],
 "approaches": [
   ap("解法", "貪心", [("c", S["p605"]), "驗證方式：和枚舉所有種法的暴力法比對 1500 組。"], "O(n)", "O(n)", "", "補 0 的副本；直接在原陣列判斷邊界則 O(1)", optimal=True),
 ],
 "edges": ["<strong>n = 0</strong> → True。", "<strong>只有一格且是 0</strong> → 可以種 1 朵。"],
 "follow": [("h", "直接數連續 0 的長度"), ("c", "一段長度為 k、兩邊都是花的空地可以種 (k−1)//2 朵；靠邊的空地少了一側限制，補 0 後就統一成同一個公式。")],
 "related": ["<strong>第 495 題 提莫攻擊</strong>", "<strong>第 849 題 到最近的人的最大距離</strong>"],
 "check": ["為什麼「能種就種」是最好的？", "頭尾補 0 解決了什麼問題？"],
})


# ==================== 606. Construct String from Binary Tree ====================
S["p606"] = '''class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        s = str(root.val)
        if root.left or root.right:
            s += "(" + self.tree2str(root.left) + ")"   # ★ 有右孩子時，空的左孩子也要寫 "()"
        if root.right:
            s += "(" + self.tree2str(root.right) + ")"
        return s'''

_p606 = S.load("p606")
assert _p606.tree2str(lv([1, 2, 3, 4])) == "1(2(4))(3)" and _p606.tree2str(lv([1, 2, 3, None, 4])) == "1(2()(4))(3)"
def _parse(s):
    i = 0
    def node():
        nonlocal i
        j = i
        while i < len(s) and (s[i] == "-" or s[i].isdigit()): i += 1
        from runner import TreeNode
        nd = TreeNode(int(s[j:i]))
        if i < len(s) and s[i] == "(":
            i += 1
            nd.left = node() if s[i] != ")" else None
            i += 1
            if i < len(s) and s[i] == "(":
                i += 1; nd.right = node(); i += 1
        return nd
    return node()
for _ in range(1000):
    t = rand_tree(random.randint(1, 10), -3, 9)
    assert ser(_parse(_p606.tree2str(t))) == ser(t)
print("P606 OK")

em({
 "num": 606, "title": "根據二元樹建立字串",
 "desc": "前序走訪加括號；唯一要保留的空括號是「沒有左孩子但有右孩子」時的 ()。",
 "zh": [
   "給你二元樹的根節點，用<strong>前序走訪</strong>的方式把它轉成由整數和括號組成的字串：每個子樹放在一對括號裡。",
   "省略所有<strong>不影響還原</strong>的空括號：唯一不能省的是「左孩子為空但右孩子存在」時的 <code>()</code>。",
 ],
 "idea": [
   ("c", """【什麼時候需要括號？】
    沒有孩子：只有值。
    只有左孩子：值(左)          —— 右邊的 () 可省
    只有右孩子：值()(右)        —— 左邊的 () 不能省，否則會被誤認成左孩子
    兩個都有：值(左)(右)

【整理成兩條規則】
    有任何孩子 -> 寫左括號組（可能是空的 ()）
    有右孩子   -> 寫右括號組"""),
 ],
 "approaches": [
   ap("解法", "前序遞迴", [("c", S["p606"]), "驗證方式：把輸出字串解析回樹，和原樹比對 1000 棵隨機樹（確保資訊沒有遺失）。"], "O(n)", "O(h)", "", "", optimal=True),
 ],
 "edges": ["<strong>只有右孩子</strong> → 必須保留 \"()\"。", "<strong>負數節點</strong> → 直接轉字串。"],
 "follow": [("h", "反過來：由字串建樹"), ("c", "第 536 題（付費）是本題的反向：解析括號字串還原二元樹。")],
 "related": ["<strong>第 297 題 二元樹的序列化與反序列化</strong>", "<strong>第 652 題 尋找重複的子樹</strong>"],
 "check": ["為什麼只有右孩子時左邊的 () 不能省？"],
})


# ==================== 609. Find Duplicate File in System ====================
S["p609"] = '''class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        groups = defaultdict(list)              # 檔案內容 -> 所有具有這個內容的完整路徑
        for p in paths:
            root, *files = p.split(" ")
            for f in files:
                name, content = f[:-1].split("(")   # "1.txt(abcd)" -> "1.txt", "abcd"
                groups[content].append(root + "/" + name)
        return [g for g in groups.values() if len(g) > 1]   # ★ 只回傳有重複的群組'''

_p609 = S.load("p609", extra={"defaultdict": defaultdict})
r = _p609.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
assert sorted(map(sorted, r)) == sorted(map(sorted, [["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"], ["root/a/1.txt", "root/c/3.txt"]]))
print("P609 OK")

em({
 "num": 609, "title": "在系統中查找重複檔案",
 "desc": "以檔案內容為鍵分組；附上「真實檔案系統」的追問：先比大小、再比雜湊、最後逐位元組確認。",
 "zh": [
   "給你一組目錄資訊字串，每個格式為 <code>\"目錄 檔名1(內容1) 檔名2(內容2) ...\"</code>。",
   "找出所有<strong>內容相同</strong>的檔案群組（至少兩個檔案），以完整路徑 <code>\"目錄/檔名\"</code> 表示，回傳順序不限。",
 ],
 "idea": [
   ("c", """【以內容為鍵分組】
    解析每個字串：第一段是目錄，之後每段是 "檔名(內容)"。
    groups[內容].append(目錄 + "/" + 檔名)
    最後只留下大小 > 1 的群組。"""),
 ],
 "approaches": [
   ap("解法", "雜湊表分組", [("c", S["p609"])], "O(總字元數)", "O(總字元數)", optimal=True),
 ],
 "edges": ["<strong>沒有重複</strong> → []。", "<strong>同一目錄下的兩個檔案內容相同</strong> → 也算。"],
 "follow": [
   ("h", "真實檔案系統（題目的追問）"),
   ("ul", [
     "<strong>怎麼搜尋檔案？</strong>DFS 或 BFS 走訪目錄樹皆可；目錄很深時 BFS 不會爆遞迴堆疊，DFS 的記憶體用量則與深度成正比。",
     "<strong>檔案很大（GB 等級）怎麼辦？</strong>不能把內容當鍵。先依<strong>檔案大小</strong>分組（大小不同一定不同），只對大小相同的檔案計算雜湊（如 SHA-256）。",
     "<strong>每次只能讀 1KB？</strong>串流計算雜湊：分塊讀入、逐塊更新雜湊值。也可以先只比對第一個 1KB 的雜湊，篩掉大部分不同的檔案。",
     "<strong>如何避免誤判？</strong>雜湊相同後，再逐位元組比對確認，排除雜湊碰撞。",
   ]),
 ],
 "related": ["<strong>第 49 題 字母異位詞分組</strong>"],
 "check": ["分組的鍵是什麼？", "處理大檔案時為什麼先比較檔案大小？"],
})


# ==================== 611. Valid Triangle Number ====================
S["p611"] = '''class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for k in range(len(nums) - 1, 1, -1):       # 固定最長邊 nums[k]
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i                    # ★ i..j-1 和 j 配對都成立（它們都 >= nums[i]）
                    j -= 1
                else:
                    i += 1                          # 太小：左邊加大
        return res'''

_p611 = S.load("p611")
from itertools import combinations
for _ in range(2000):
    a = [random.randint(0, 9) for _ in range(random.randint(0, 9))]
    want = sum(1 for x, y, z in combinations(a, 3) if x + y > z and x + z > y and y + z > x)
    assert _p611.triangleNumber(a[:]) == want
print("P611 OK")

em({
 "num": 611, "title": "有效三角形的個數",
 "desc": "排序後固定最長邊，另外兩邊用雙指標：一旦成立，左指標到右指標之間的都成立，O(n²)。",
 "zh": ["給你一個非負整數陣列 <code>nums</code>，回傳從中選出三個數（索引不同）可以構成<strong>三角形</strong>三邊長的組合數。"],
 "idea": [
   ("c", """【三角不等式】
    排序後 a <= b <= c，只需檢查 a + b > c（另外兩個自動成立）。

【固定最長邊 c = nums[k]】
    在 nums[0..k-1] 中找有幾對 (i, j) 使 nums[i] + nums[j] > nums[k]。
    雙指標 i = 0、j = k-1：
        nums[i] + nums[j] > c：
            i 換成 i..j-1 任何一個（都 >= nums[i]）也成立 -> 一次加 j - i 對，j 左移
        否則：nums[i] 太小，i 右移

【0 的處理】
    0 + b > c 不可能（b <= c），自然被排除。"""),
 ],
 "approaches": [
   ap("解法一", "排序 + 二分", [("c", "固定 i、j，用二分找最大的 k 使 nums[k] < nums[i] + nums[j]\n時間 O(n² log n)")], "O(n² log n)", "O(1)"),
   ap("解法二", "排序 + 雙指標", [("c", S["p611"]), "驗證方式：和三重迴圈比對 2000 組。"], "O(n²)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>含 0</strong> → 不可能是邊。", "<strong>少於 3 個數</strong> → 0。", "<strong>重複值</strong> → 不同索引視為不同組合。"],
 "follow": [("h", "三數之和家族"), ("c", "「排序 + 固定一個 + 雙指標」是第 15 題（三數之和）、第 16 題（最接近的三數之和）、第 259 題（較小的三數之和，付費）的共同骨架。")],
 "related": ["<strong>第 15 題 三數之和</strong>", "<strong>第 16 題 最接近的三數之和</strong>", "<strong>第 976 題 三角形的最大周長</strong>"],
 "check": ["排序後為什麼只要檢查一個不等式？", "條件成立時為什麼可以一次加 j − i？"],
})


# ==================== 617. Merge Two Binary Trees ====================
S["p617"] = '''class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            return root1 or root2           # ★ 一邊是空的：直接沿用另一邊的整棵子樹
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1'''

_p617 = S.load("p617")
assert ser(_p617.mergeTrees(lv([1, 3, 2, 5]), lv([2, 1, 3, None, 4, None, 7]))) == [3, 4, 5, 5, 4, None, 7]
def _mg(a, b):
    if a is None: return b
    if b is None: return a
    return (a[0] + b[0], _mg(a[1], b[1]), _mg(a[2], b[2]))
def _sig(t): return None if t is None else (t.val, _sig(t.left), _sig(t.right))
for _ in range(1000):
    a, b = rand_tree(random.randint(0, 8)), rand_tree(random.randint(0, 8))
    want = _mg(_sig(a), _sig(b))
    assert _sig(_p617.mergeTrees(a, b)) == want
print("P617 OK")

em({
 "num": 617, "title": "合併二元樹",
 "desc": "同步走訪兩棵樹：重疊處相加，其中一邊為空就直接接上另一邊的子樹。",
 "zh": [
   "給你兩棵二元樹 <code>root1</code>、<code>root2</code>。把它們疊在一起：重疊位置的節點值相加，不重疊的位置則保留存在的那一個節點。",
   "回傳合併後的樹（從兩棵樹的根開始合併）。",
 ],
 "idea": [
   ("c", """【同步遞迴】
    merge(a, b)：
        有一邊是空的 -> 回傳另一邊（整棵子樹直接接上，不用複製）
        都不空 -> a.val += b.val，左右分別遞迴

    這裡直接修改 root1 並回傳它；
    若不想改動輸入，可以每次建新節點。"""),
 ],
 "approaches": [
   ap("解法", "同步遞迴", [("c", S["p617"])], "O(min(m, n))", "O(min(h₁, h₂))", "只走訪兩棵樹重疊的部分", "", optimal=True),
 ],
 "edges": ["<strong>一棵是空樹</strong> → 回傳另一棵。", "<strong>形狀完全不同</strong> → 非重疊的部分直接接上。"],
 "follow": [("h", "同步走訪兩棵樹"), ("c", "第 100 題（相同的樹）、第 101 題（對稱二元樹）、第 951 題（翻轉等價二元樹）都是「兩棵樹一起走」的模式。")],
 "related": ["<strong>第 100 題 相同的樹</strong>", "<strong>第 101 題 對稱二元樹</strong>"],
 "check": ["為什麼一邊為空時可以直接回傳另一邊？", "時間複雜度為什麼是較小那棵的大小？"],
})


# ==================== 621. Task Scheduler ====================
S["p621"] = '''class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks).values()
        mx = max(cnt)                           # 最多的任務出現幾次
        k = sum(c == mx for c in cnt)           # 有幾種任務都是這個次數
        # ★ 骨架：(mx - 1) 個長度 n+1 的區塊，最後再放 k 個；任務夠多時沒有閒置
        return max(len(tasks), (mx - 1) * (n + 1) + k)'''

_p621 = S.load("p621", extra={"Counter": Counter})
def _sim621(tasks, n):
    cnt = Counter(tasks); last = {}; t = 0; left = len(tasks)
    while left:
        cand = [x for x in cnt if cnt[x] and t - last.get(x, -10 ** 9) > n]
        if cand:
            x = max(cand, key=lambda x: cnt[x]); cnt[x] -= 1; last[x] = t; left -= 1
        t += 1
    return t
for _ in range(2000):
    tasks = [random.choice("ABCD") for _ in range(random.randint(1, 10))]; n = random.randint(0, 4)
    assert _p621.leastInterval(tasks, n) == _sim621(tasks, n)
print("P621 OK")

em({
 "num": 621, "title": "任務排程器",
 "desc": "以出現最多的任務搭骨架：(mx−1)·(n+1) + 並列最多的種數；任務夠多時沒有閒置，答案就是任務總數。",
 "zh": [
   "CPU 要執行一組任務 <code>tasks</code>（每個字母代表一種任務），每個時間單位可以執行一個任務或閒置。",
   "<strong>同一種任務</strong>之間必須間隔至少 <code>n</code> 個時間單位。回傳完成所有任務的<strong>最少時間</strong>。",
 ],
 "idea": [
   ("c", """【最多的任務決定骨架】
    設最多的任務 A 出現 mx 次。A 和 A 之間至少隔 n 格：
        A _ _ | A _ _ | A
    前 mx-1 個 A 各帶一個長度 n+1 的區塊，最後一個 A 單獨放。
    其他任務塞進空格裡。

【並列最多的任務】
    若有 k 種任務都出現 mx 次（例如 A 和 B），
    最後一個區塊要放 k 個：A B _ | A B _ | A B
    長度 = (mx - 1)(n + 1) + k。

【任務很多，空格不夠塞】
    那就根本不需要閒置 —— 把區塊拉長即可，
    答案就是任務總數。

    答案 = max(len(tasks), (mx-1)(n+1) + k)。"""),
 ],
 "approaches": [
   ap("解法", "公式（貪心的骨架分析）", [("c", S["p621"]), "驗證方式：和「每個時間點選剩餘最多、且已冷卻的任務」的貪心模擬比對 2000 組。"], "O(m)", "O(1)", "m 為任務數；字母只有 26 種", "", optimal=True),
 ],
 "edges": ["<strong>n = 0</strong> → 不需間隔，答案 = 任務數。", "<strong>多種任務並列最多</strong> → 公式中的 k。", "<strong>任務種類很多</strong> → 不會有閒置。"],
 "follow": [("h", "模擬的做法"), ("c", "用最大堆積模擬：每一輪取出最多 n+1 個剩餘次數最多的任務各執行一次，再放回去。對要求輸出實際排程的變形更直觀。")],
 "related": ["<strong>第 767 題 重構字串</strong>", "<strong>第 358 題 K 距離間隔重排字串</strong>（付費）", "<strong>第 2365 題 任務排程器 II</strong>"],
 "check": ["骨架的長度公式是怎麼來的？", "為什麼要和任務總數取最大值？", "k 代表什麼？"],
})
