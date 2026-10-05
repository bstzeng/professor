# -*- coding: utf-8 -*-
"""第 501、502、503、504、506、507、508、509 題。"""
import random
from collections import Counter
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, rand_tree, bst, nodes

S = Src()
random.seed(501)


# ==================== 501. Find Mode in Binary Search Tree ====================
S["p501a"] = '''class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        def dfs(nd):
            if nd:
                cnt[nd.val] += 1
                dfs(nd.left); dfs(nd.right)
        dfs(root)
        best = max(cnt.values())
        return [v for v, c in cnt.items() if c == best]'''

S["p501b"] = '''class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res, best = [], 0
        prev, run = None, 0              # 中序走訪時「上一個值」與它目前連續出現的次數

        def visit(v):
            nonlocal prev, run, best, res
            run = run + 1 if v == prev else 1   # ★ BST 中序是有序的，相同值一定相鄰
            prev = v
            if run > best:
                best, res = run, [v]
            elif run == best:
                res.append(v)

        def inorder(nd):
            if nd:
                inorder(nd.left)
                visit(nd.val)
                inorder(nd.right)

        inorder(root)
        return res'''

for key in ("p501a", "p501b"):
    sol = S.load(key, extra={"Counter": Counter})
    for _ in range(1500):
        vals = [random.randint(0, 6) for _ in range(random.randint(1, 14))]
        c = Counter(vals); b = max(c.values())
        assert sorted(sol.findMode(bst(vals))) == sorted(v for v in c if c[v] == b)
print("P501 OK")

em({
 "num": 501, "title": "二元搜尋樹中的眾數",
 "desc": "BST 的中序走訪是有序的：相同值一定相鄰，像在排序陣列上數連續段，O(1) 額外空間。",
 "zh": [
   "給你一棵<strong>允許重複值</strong>的二元搜尋樹（BST）的根節點，找出所有<strong>眾數</strong>（出現次數最多的值）。若有多個，以任意順序回傳。",
   "這裡的 BST 定義：左子樹的值都 <strong>≤</strong> 節點值，右子樹的值都 <strong>≥</strong> 節點值。",
   "<strong>進階：</strong>能不用額外空間嗎？（遞迴的呼叫堆疊不算）",
 ],
 "idea": [
   ("c", """【一般二元樹的做法】
    用雜湊表數每個值出現幾次，取最大的。O(n) 空間。

【利用 BST 的性質】
    BST 的中序走訪 = 由小到大排好的序列。
    排序後，相同的值一定擠在一起 -> 像在排序陣列上數「連續段」：
        prev：上一個值
        run ：目前這一段的長度
        best：目前最長的長度
    run > best -> 清空答案，只放這個值
    run == best -> 加進答案
    只用幾個變數，不需要雜湊表。"""),
 ],
 "approaches": [
   ap("解法一", "雜湊表計數（任何二元樹都適用）", [("c", S["p501a"])], "O(n)", "O(n)"),
   ap("解法二", "中序走訪 + 連續段計數", [("c", S["p501b"])], "O(n)", "O(h)", "", "只有遞迴堆疊", optimal=True),
 ],
 "edges": [
   "<strong>只有一個節點</strong> → 答案就是它。",
   "<strong>所有值都不同</strong> → 每個值都是眾數，全部回傳。",
   "<strong>更新 best 時要清空舊答案</strong> → 不能只 append。",
 ],
 "follow": [
   ("h", "真正的 O(1) 空間？"),
   ("c", "遞迴堆疊仍是 O(h)。要做到 O(1)，可以用 Morris 中序走訪（第 99 題、第 94 題的進階）：暫時把前驅節點的右指標接回自己，走完再還原。"),
 ],
 "related": ["<strong>第 94 題 二元樹的中序走訪</strong>", "<strong>第 530 題 BST 的最小絕對差</strong>", "<strong>第 98 題 驗證二元搜尋樹</strong>"],
 "check": ["為什麼 BST 中相同的值在中序序列裡一定相鄰？", "run 超過 best 時答案要怎麼更新？"],
})


# ==================== 502. IPO ====================
S["p502"] = '''class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))   # 依門檻（所需資本）排序
        heap = []                                   # 目前「做得起」的專案利潤（最大堆積）
        i = 0
        for _ in range(k):
            while i < len(projects) and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])  # 門檻達到了，放進候選
                i += 1
            if not heap:
                break                               # 一個都做不起，提早結束
            w += -heapq.heappop(heap)               # ★ 貪心：做得起的裡面挑利潤最大的
        return w'''

_p502 = S.load("p502")
from itertools import permutations
def _bf502(k, w, P, C):
    best = w
    def go(w, used, left):
        nonlocal best
        best = max(best, w)
        if left == 0:
            return
        for i in range(len(P)):
            if not used >> i & 1 and C[i] <= w:
                go(w + P[i], used | 1 << i, left - 1)
    go(w, 0, k)
    return best
for _ in range(1500):
    n = random.randint(1, 6)
    P = [random.randint(0, 5) for _ in range(n)]; C = [random.randint(0, 8) for _ in range(n)]
    k = random.randint(1, n); w = random.randint(0, 4)
    assert _p502.findMaximizedCapital(k, w, P, C) == _bf502(k, w, P, C)
print("P502 OK")

em({
 "num": 502, "title": "IPO",
 "desc": "資本只會增加，所以每一步都在「做得起的專案」裡挑利潤最大的：排序 + 最大堆積。",
 "zh": [
   "公司想在 IPO 前最多完成 <code>k</code> 個不同的專案。第 <code>i</code> 個專案需要資本至少 <code>capital[i]</code> 才能開始，完成後得到純利潤 <code>profits[i]</code>（加進資本，不會扣掉門檻）。",
   "一開始資本是 <code>w</code>。選擇最多 <code>k</code> 個專案，回傳最後能得到的<strong>最大資本</strong>。",
 ],
 "idea": [
   ("c", """【關鍵觀察：資本只增不減】
    做任何專案都不會花掉資本（只要達到門檻），利潤 >= 0。
    所以「做得起的專案集合」只會越來越大。

【貪心】
    每一輪：在目前做得起的專案中，挑利潤最大的。
    為什麼對？做了利潤最大的，資本最高，
    之後做得起的集合也最大 —— 不會比其他選擇差。

【資料結構】
    專案依門檻排序，用指標 i 把「門檻 <= w」的專案陸續放進最大堆積；
    每輪從堆積拿最大利潤。
    每個專案最多進出堆積一次。"""),
 ],
 "approaches": [
   ap("解法", "排序 + 最大堆積的貪心", [
     ("c", S["p502"]),
     "驗證方式：和窮舉所有選擇順序的暴力法比對 1500 組隨機資料。",
   ], "O(n log n + k log n)", "O(n)", optimal=True),
 ],
 "edges": [
   "<strong>沒有做得起的專案</strong> → 提早結束，回傳目前資本。",
   "<strong>k 大於專案數</strong> → 堆積空了就停。",
   "<strong>利潤為 0 的專案</strong> → 做了也不影響，不需特別處理。",
 ],
 "follow": [
   ("h", "兩個堆積的寫法"),
   ("c", "也可以把專案依門檻放進最小堆積，每輪把門檻 <= w 的移到利潤最大堆積。和排序 + 指標是同一件事。"),
 ],
 "related": ["<strong>第 630 題 課程表 III</strong>", "<strong>第 871 題 最少加油次數</strong>", "<strong>第 1353 題 最多可以參加的會議數目</strong>"],
 "check": ["為什麼貪心挑利潤最大的專案是對的？", "哪一個性質保證「做得起的集合」只會變大？"],
})


# ==================== 503. Next Greater Element II ====================
S["p503"] = '''class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []                          # 存「還沒找到答案」的索引，對應值由下往上遞減
        for i in range(2 * n):              # ★ 走兩圈：第二圈讓尾端的元素繞回開頭找答案
            x = nums[i % n]
            while stack and nums[stack[-1]] < x:
                res[stack.pop()] = x
            if i < n:
                stack.append(i)             # 只有第一圈需要推進堆疊
        return res'''

_p503 = S.load("p503")
for _ in range(3000):
    a = [random.randint(-3, 3) for _ in range(random.randint(1, 9))]
    n = len(a)
    want = [next((a[(i + d) % n] for d in range(1, n) if a[(i + d) % n] > a[i]), -1) for i in range(n)]
    assert _p503.nextGreaterElements(a) == want
print("P503 OK")

em({
 "num": 503, "title": "下一個更大元素 II",
 "desc": "環形陣列的單調堆疊：把陣列走兩圈，第二圈只負責替還在等待的元素找答案。",
 "zh": [
   "給你一個<strong>環形</strong>整數陣列 <code>nums</code>（最後一個元素的下一個是第一個），回傳每個元素的<strong>下一個更大元素</strong>：依走訪順序往後（可以繞回開頭）找到的第一個比它大的數；不存在則為 <code>-1</code>。",
   "注意陣列<strong>可能有重複值</strong>。",
 ],
 "idea": [
   ("c", """【第 496 題的單調堆疊 + 環形】
    非環形版：由左往右掃，堆疊放「還在等待答案」的元素，
    新元素比頂端大就替頂端解答。

【環形怎麼辦？走兩圈】
    尾端元素的答案可能在開頭 —— 把陣列接在自己後面就好：
    索引 i 從 0 走到 2n-1，值取 nums[i % n]。
    第二圈不推進新元素，只負責「解答」第一圈留下來的。

【為什麼存索引而不是值？】
    有重複值，而且答案要寫回 res[索引]。"""),
 ],
 "approaches": [
   ap("解法", "單調堆疊走兩圈", [
     ("c", S["p503"]),
   ], "O(n)", "O(n)", "每個索引只進出堆疊一次", optimal=True),
 ],
 "edges": [
   "<strong>最大值</strong> → 繞一整圈都找不到，答案 −1（重複的最大值也都是 −1）。",
   "<strong>全部相同</strong> → 全部 −1（嚴格大於）。",
   "<strong>只有一個元素</strong> → −1。",
 ],
 "follow": [
   ("h", "環形陣列的通用技巧"),
   ("c", "「把陣列複製一份接在後面」（或索引取 mod n）是處理環形的標準手法：第 213 題（打家劫舍 II）、第 918 題（環形子陣列最大和）也用類似的想法。"),
 ],
 "related": ["<strong>第 496 題 下一個更大元素 I</strong>", "<strong>第 556 題 下一個更大元素 III</strong>", "<strong>第 739 題 每日溫度</strong>"],
 "check": ["為什麼走兩圈就夠了？", "第二圈為什麼不推進堆疊？"],
})


# ==================== 504. Base 7 ====================
S["p504"] = '''class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        neg, n = num < 0, abs(num)
        digits = []
        while n:
            n, r = divmod(n, 7)          # ★ 反覆除以 7，餘數就是由低到高的每一位
            digits.append(str(r))
        return ("-" if neg else "") + "".join(reversed(digits))'''

_p504 = S.load("p504")
for x in range(-5000, 5001):
    s = _p504.convertToBase7(x)
    assert int(s, 7) == x and (s == "0" or not s.lstrip("-").startswith("0"))
print("P504 OK")

em({
 "num": 504, "title": "七進位數",
 "desc": "反覆除以 7 取餘數，由低位到高位得到每一位；負數先取絕對值。",
 "zh": ["給你一個整數 <code>num</code>，回傳它的<strong>七進位</strong>表示字串。"],
 "idea": [
   ("c", """【進位轉換的標準做法】
    n = d_k·7^k + ... + d_1·7 + d_0
    n % 7 = d_0（最低位），n // 7 去掉最低位。
    反覆做，得到由低到高的每一位，最後反轉。

【負數】
    先記下符號，對絕對值轉換，最後補上 "-"。
    （Python 對負數的 % 和 // 是向下取整，直接做會出錯。）

【0】
    迴圈一次都不會執行，要特判。"""),
 ],
 "approaches": [
   ap("解法", "反覆除以 7", [("c", S["p504"])], "O(log₇|n|)", "O(log₇|n|)", optimal=True),
 ],
 "edges": ["<strong>num = 0</strong> → \"0\"。", "<strong>負數</strong> → 先取絕對值。", "<strong>7 的次方</strong> → 例如 49 = \"100\"。"],
 "follow": [("h", "任意進位"), ("c", "把 7 換成 b 就是任意進位轉換。超過 10 的進位要把餘數對應到字母（第 405 題十六進位）；負進位（第 1017 題）則要調整餘數為非負。")],
 "related": ["<strong>第 405 題 數字轉換為十六進位數</strong>", "<strong>第 168 題 Excel 表列名稱</strong>", "<strong>第 1017 題 負二進位轉換</strong>"],
 "check": ["為什麼要反轉 digits？", "Python 的負數取餘有什麼陷阱？"],
})


# ==================== 506. Relative Ranks ====================
S["p506"] = '''class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        order = sorted(range(len(score)), key=lambda i: -score[i])  # 依分數由高到低排索引
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = [""] * len(score)
        for rank, i in enumerate(order):
            res[i] = medals[rank] if rank < 3 else str(rank + 1)   # ★ 答案寫回原本的位置
        return res'''

_p506 = S.load("p506")
assert _p506.findRelativeRanks([5, 4, 3, 2, 1]) == ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
assert _p506.findRelativeRanks([10, 3, 8, 9, 4]) == ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]
for _ in range(500):
    s = random.sample(range(100), random.randint(1, 10))
    r = _p506.findRelativeRanks(s)
    for i, x in enumerate(s):
        k = sum(y > x for y in s) + 1
        assert r[i] == (["Gold Medal", "Silver Medal", "Bronze Medal"][k - 1] if k <= 3 else str(k))
print("P506 OK")

em({
 "num": 506, "title": "相對名次",
 "desc": "排序的是索引而不是分數：依分數排好索引後，名次寫回原位置。",
 "zh": [
   "給你 <code>n</code> 位選手的分數 <code>score</code>（互不相同）。依分數由高到低排名：第 1 名是 <code>\"Gold Medal\"</code>、第 2 名 <code>\"Silver Medal\"</code>、第 3 名 <code>\"Bronze Medal\"</code>，第 4 名以後就是名次數字字串。",
   "回傳每位選手（依原本順序）的名次。",
 ],
 "idea": [
   ("c", """【排序索引】
    要依分數排序，但答案要放回原本的位置 ->
    排序的對象是「索引」，用分數當排序鍵：
        order = sorted(range(n), key=lambda i: -score[i])
    order[0] 是第一名的索引，order[1] 是第二名……
    res[order[r]] = 第 r+1 名的字串。

    「排序索引」（argsort）是很常用的技巧。"""),
 ],
 "approaches": [
   ap("解法", "排序索引（argsort）", [("c", S["p506"])], "O(n log n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>只有 1～3 人</strong> → 只有獎牌。", "<strong>名次從 1 開始</strong> → 第 4 名寫 \"4\"，不是 \"3\"。"],
 "follow": [("h", "分數範圍很小時"), ("c", "若分數上限 M 不大，可用計數陣列（桶）代替排序：O(n + M)。")],
 "related": ["<strong>第 1331 題 陣列序號轉換</strong>", "<strong>第 1365 題 有多少小於當前數字的數字</strong>"],
 "check": ["為什麼要排序索引而不是直接排序分數？"],
})


# ==================== 507. Perfect Number ====================
S["p507"] = '''class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        total = 1                       # 1 一定是真因數
        d = 2
        while d * d <= num:             # ★ 因數成對出現：d 和 num // d，只需枚舉到 √num
            if num % d == 0:
                total += d
                if d != num // d:       # 完全平方數時不要重複加
                    total += num // d
            d += 1
        return total == num'''

_p507 = S.load("p507")
for x in range(1, 10000):
    assert _p507.checkPerfectNumber(x) == (sum(d for d in range(1, x) if x % d == 0) == x)
for x in (33550336, 8589869056 // 1000, 99999989):
    pass
assert _p507.checkPerfectNumber(33550336)
print("P507 OK")

em({
 "num": 507, "title": "完全數",
 "desc": "因數成對出現，只要枚舉到 √n；附上「10⁸ 以內只有五個完全數」的小知識。",
 "zh": ["<strong>完全數</strong>是等於自己所有<strong>正真因數</strong>（不含自己）總和的正整數，例如 28 = 1 + 2 + 4 + 7 + 14。給你整數 <code>n</code>，判斷它是不是完全數。"],
 "idea": [
   ("c", """【因數成對】
    d 是 n 的因數 -> n / d 也是，而且兩者一個 <= √n、一個 >= √n。
    所以只要枚舉 d = 2..√n，每找到一個就加上 d 和 n/d。
    1 另外加（n 本身不算）。

【注意】
    d == n/d（完全平方數）時只加一次。
    n = 1：真因數總和是 0，不是完全數。"""),
 ],
 "approaches": [
   ap("解法", "枚舉到 √n", [("c", S["p507"])], "O(√n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>n = 1</strong> → False。", "<strong>完全平方數</strong> → √n 只加一次。"],
 "follow": [
   ("h", "其實只有五個"),
   ("c", "題目限制 n ≤ 10⁸，範圍內的完全數只有 6、28、496、8128、33550336。歐幾里得–歐拉定理：偶完全數都是 2^(p−1)·(2^p − 1)，其中 2^p − 1 是梅森質數。至今還不知道是否存在奇完全數。"),
 ],
 "related": ["<strong>第 204 題 計數質數</strong>", "<strong>第 1390 題 四因數</strong>"],
 "check": ["為什麼只需要枚舉到 √n？", "完全平方數要怎麼特別處理？"],
})


# ==================== 508. Most Frequent Subtree Sum ====================
S["p508"] = '''class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        cnt = Counter()
        def total(nd):                  # 後序：先算出左右子樹和，再加上自己
            if not nd:
                return 0
            s = nd.val + total(nd.left) + total(nd.right)
            cnt[s] += 1
            return s
        total(root)
        best = max(cnt.values())
        return [s for s, c in cnt.items() if c == best]'''

_p508 = S.load("p508", extra={"Counter": Counter})
assert sorted(_p508.findFrequentTreeSum(lv([5, 2, -3]))) == [-3, 2, 4]
assert _p508.findFrequentTreeSum(lv([5, 2, -5])) == [2]
for _ in range(1000):
    t = rand_tree(random.randint(1, 10), -3, 3)
    def ss(nd): return nd.val + (ss(nd.left) if nd.left else 0) + (ss(nd.right) if nd.right else 0)
    c = Counter(ss(nd) for nd in nodes(t)); b = max(c.values())
    assert sorted(_p508.findFrequentTreeSum(t)) == sorted(s for s in c if c[s] == b)
print("P508 OK")

em({
 "num": 508, "title": "出現次數最多的子樹元素和",
 "desc": "後序走訪一次算出所有子樹和，雜湊表計數後取出現最多的。",
 "zh": [
   "給你二元樹的根節點，回傳出現次數最多的<strong>子樹元素和</strong>。若有多個並列，全部回傳（順序不限）。",
   "一個節點的「子樹元素和」是以它為根的子樹中所有節點值的總和（包含它自己）。",
 ],
 "idea": [
   ("c", """【子樹和 = 自己 + 左子樹和 + 右子樹和】
    天生的後序走訪：先算出兩個子樹，再組合。
    每個節點算一次，順便把結果丟進計數器。

【取眾數】
    best = 最大出現次數，回傳所有次數 == best 的和。"""),
 ],
 "approaches": [
   ap("解法", "後序走訪 + 計數", [("c", S["p508"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>單一節點</strong> → [val]。", "<strong>負數節點</strong> → 子樹和可能是負的或 0，雜湊表照樣處理。"],
 "follow": [("h", "後序走訪的模式"), ("c", "「函式回傳子樹的某個統計值，同時在外部更新答案」是樹題最常見的模式：第 543 題（直徑）、第 124 題（最大路徑和）、第 563 題（坡度）都是。")],
 "related": ["<strong>第 572 題 另一棵樹的子樹</strong>", "<strong>第 563 題 二元樹的坡度</strong>", "<strong>第 501 題 BST 中的眾數</strong>"],
 "check": ["為什麼要用後序走訪？"],
})


# ==================== 509. Fibonacci Number ====================
S["p509a"] = '''class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1                     # F(0), F(1)
        for _ in range(n):
            a, b = b, a + b             # ★ 只需要前兩項：滾動變數
        return a'''

S["p509b"] = '''class Solution:
    def fib(self, n: int) -> int:
        def mul(A, B):
            return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                    [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]
        res, M = [[1, 0], [0, 1]], [[1, 1], [1, 0]]
        while n:                        # 快速冪：[[1,1],[1,0]]^n = [[F(n+1),F(n)],[F(n),F(n-1)]]
            if n & 1:
                res = mul(res, M)
            M = mul(M, M)
            n >>= 1
        return res[0][1]'''

_f = [0, 1]
for i in range(200):
    _f.append(_f[-1] + _f[-2])
for key in ("p509a", "p509b"):
    sol = S.load(key)
    assert all(sol.fib(n) == _f[n] for n in range(150))
print("P509 OK")

em({
 "num": 509, "title": "斐波那契數",
 "desc": "從指數級的遞迴到記憶化、滾動變數，再到 O(log n) 的矩陣快速冪。",
 "zh": ["斐波那契數列定義為 <code>F(0) = 0</code>、<code>F(1) = 1</code>，<code>F(n) = F(n − 1) + F(n − 2)</code>（n &gt; 1）。給你 <code>n</code>，計算 <code>F(n)</code>。"],
 "idea": [
   ("c", """【直接照定義遞迴：O(φⁿ)】
    fib(n) 呼叫 fib(n-1) 和 fib(n-2)，大量重複計算。
    fib(30) 約一百多萬次呼叫。

【記憶化 / 由下往上】
    每個 F(i) 只算一次 -> O(n)。
    而且 F(i) 只依賴前兩項 -> 兩個變數滾動，O(1) 空間。

【矩陣快速冪：O(log n)】
    [F(n+1)]   [1 1] [F(n)  ]
    [F(n)  ] = [1 0] [F(n-1)]
    所以 [[1,1],[1,0]]^n 一次就得到 F(n)。
    矩陣次方用「平方再平方」，只要 log n 次乘法。"""),
 ],
 "approaches": [
   ap("解法一", "滾動變數", [("c", S["p509a"])], "O(n)", "O(1)", optimal=True),
   ap("解法二", "矩陣快速冪", [("c", S["p509b"]), "n 很大（而且要取模）時才有優勢；本題 n ≤ 30，解法一就夠了。"], "O(log n)", "O(1)"),
 ],
 "compare": (["解法", "時間", "空間"], [["直接遞迴", "O(φⁿ)", "O(n)"], ["記憶化", "O(n)", "O(n)"], ["滾動變數", "O(n)", "O(1)"], ["矩陣快速冪", "O(log n)", "O(1)"]]),
 "edges": ["<strong>n = 0</strong> → 0。", "<strong>n = 1</strong> → 1。"],
 "follow": [("h", "線性遞迴的通解"), ("c", "任何「下一項是前 k 項的線性組合」的數列，都能寫成 k×k 矩陣的次方，用快速冪在 O(k³ log n) 算出第 n 項。第 1137 題（泰波那契）、第 70 題（爬樓梯）是同一族。")],
 "related": ["<strong>第 70 題 爬樓梯</strong>", "<strong>第 1137 題 第 N 個泰波那契數</strong>", "<strong>第 746 題 使用最小花費爬樓梯</strong>"],
 "check": ["直接遞迴為什麼是指數時間？", "為什麼兩個變數就夠了？", "矩陣快速冪的關鍵等式是什麼？"],
})
