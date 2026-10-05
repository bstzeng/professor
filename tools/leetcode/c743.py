# -*- coding: utf-8 -*-
"""第 743、744、745、746、747、748、749、752 題。"""
import random, heapq, bisect
from collections import Counter, deque
from authoring import ap
from lcauto import em
from runner import Src

S = Src()
random.seed(743)


# ==================== 743. Network Delay Time ====================
S["p743"] = '''class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        dist = {}
        pq = [(0, k)]
        while pq:
            d, u = heapq.heappop(pq)
            if u in dist:
                continue                        # 已經確定過最短距離
            dist[u] = d                         # ★ Dijkstra：第一次從堆積取出時，距離就是最短的
            for v, w in adj[u]:
                if v not in dist:
                    heapq.heappush(pq, (d + w, v))
        return max(dist.values()) if len(dist) == n else -1'''

_p743 = S.load("p743")
for _ in range(1500):
    n = random.randint(1, 6); k = random.randint(1, n)
    times = [[random.randint(1, n), random.randint(1, n), random.randint(0, 5)] for _ in range(random.randint(0, 10))]
    times = [t for t in times if t[0] != t[1]]
    seen = set(); times = [t for t in times if (t[0], t[1]) not in seen and not seen.add((t[0], t[1]))]
    INF = 10 ** 9; D = [INF] * (n + 1); D[k] = 0
    for _ in range(n):
        for u, v, w in times:
            if D[u] + w < D[v]: D[v] = D[u] + w
    want = max(D[1:]) if max(D[1:]) < INF else -1
    assert _p743.networkDelayTime(times, n, k) == want
print("P743 OK")

em({
 "num": 743, "title": "網路延遲時間",
 "desc": "單源最短路徑的標準題：Dijkstra 求出從 k 到每個節點的最短時間，答案是其中最大值；有節點到不了就回傳 −1。",
 "zh": [
   "有 <code>n</code> 個網路節點（編號 1～n）。<code>times[i] = (u, v, w)</code> 表示訊號從 u 傳到 v 需要 w 的時間（有向邊）。",
   "從節點 <code>k</code> 發出訊號，回傳<strong>所有節點都收到訊號</strong>所需的最短時間；若有節點收不到，回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【所有節點都收到 = 最晚收到的那個】
    答案 = max(從 k 到每個節點的最短距離)。

【Dijkstra（邊權非負）】
    最小堆積存 (目前距離, 節點)。
    每次取出距離最小的節點 u：
        若已經確定過，跳過；
        否則它的距離就是最短的（之後不可能有更短的路，因為邊權 >= 0），
        用它更新鄰居。

【為什麼第一次取出就是最短？】
    堆積裡其他候選的距離都 >= d，
    經過它們再走非負的邊，只會更長。"""),
 ],
 "approaches": [
   ap("解法", "Dijkstra（堆積）", [("c", S["p743"]), "驗證方式：和 Bellman-Ford（鬆弛 n 輪）比對 1500 組隨機圖。"], "O(E log E)", "O(V + E)", optimal=True),
 ],
 "edges": ["<strong>有節點到不了</strong> → −1。", "<strong>只有一個節點</strong> → 0。", "<strong>邊權為 0</strong> → Dijkstra 仍然正確（非負即可）。"],
 "follow": [("h", "最短路徑演算法比較"), ("c", "Dijkstra：非負邊權，O(E log V)。Bellman-Ford：可有負邊、能偵測負環，O(VE)。Floyd-Warshall：所有點對，O(V³)。0-1 BFS：邊權只有 0 和 1，O(V + E)。")],
 "related": ["<strong>第 787 題 K 站中轉內最便宜的航班</strong>", "<strong>第 1631 題 最小體力消耗路徑</strong>", "<strong>第 1514 題 機率最大的路徑</strong>"],
 "check": ["答案為什麼是所有最短距離的最大值？", "Dijkstra 為什麼要求邊權非負？"],
})


# ==================== 744. Find Smallest Letter Greater Than Target ====================
S["p744"] = '''class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect.bisect_right(letters, target)    # 第一個 > target 的位置
        return letters[i % len(letters)]            # ★ 找不到就繞回第一個'''

_p744 = S.load("p744")
for _ in range(3000):
    ls = sorted(random.choice("acegxz") for _ in range(random.randint(2, 6)))
    if len(set(ls)) < 2: continue
    t = random.choice("abcdefghxyz")
    want = next((c for c in ls if c > t), ls[0])
    assert _p744.nextGreatestLetter(ls, t) == want
print("P744 OK")

em({
 "num": 744, "title": "尋找比目標字母大的最小字母",
 "desc": "bisect_right 找第一個嚴格大於 target 的位置；超出範圍就繞回第一個字母。",
 "zh": [
   "給你一個<strong>非遞減排序</strong>的字元陣列 <code>letters</code>（至少有兩種不同字元）和字元 <code>target</code>，回傳陣列中<strong>大於 target 的最小字元</strong>。",
   "如果不存在，回傳 <code>letters</code> 的第一個字元。",
 ],
 "idea": [
   ("c", """【「第一個 > target」= upper bound】
    bisect_right(letters, target)。
    target 重複出現時，bisect_right 會跳過所有等於它的。

【找不到】
    索引等於長度 -> 回傳 letters[0]。
    用 i % len 一行處理。"""),
 ],
 "approaches": [
   ap("解法", "二分（upper bound）", [("c", S["p744"])], "O(log n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>target 比所有字元都大</strong> → letters[0]。", "<strong>重複字元</strong> → bisect_right 跳過所有相等的。"],
 "follow": [("h", "lower bound vs upper bound"), ("c", "bisect_left：第一個 ≥ x 的位置；bisect_right：第一個 > x 的位置。兩者相減就是 x 出現的次數。")],
 "related": ["<strong>第 704 題 二分搜尋</strong>", "<strong>第 35 題 搜尋插入位置</strong>"],
 "check": ["為什麼要用 bisect_right 而不是 bisect_left？"],
})


# ==================== 745. Prefix and Suffix Search ====================
S["p745"] = '''class WordFilter:
    def __init__(self, words: List[str]):
        self.lookup = {}
        for idx, w in enumerate(words):
            # ★ 預先把「前綴 # 後綴」的所有組合都存起來；後面的單字覆蓋前面的 -> 留下最大索引
            for i in range(len(w) + 1):
                for j in range(len(w) + 1):
                    self.lookup[w[:i] + "#" + w[j:]] = idx

    def f(self, pref: str, suff: str) -> int:
        return self.lookup.get(pref + "#" + suff, -1)'''

_WF = S.loadns("p745")["WordFilter"]
for _ in range(500):
    words = ["".join(random.choice("ab") for _ in range(random.randint(1, 4))) for _ in range(random.randint(1, 6))]
    o = _WF(words)
    for _ in range(8):
        p = "".join(random.choice("ab") for _ in range(random.randint(1, 3))); s = "".join(random.choice("ab") for _ in range(random.randint(1, 3)))
        want = max((i for i, w in enumerate(words) if w.startswith(p) and w.endswith(s)), default=-1)
        assert o.f(p, s) == want
print("P745 OK")

em({
 "num": 745, "title": "前綴和後綴搜尋",
 "desc": "單字很短（≤ 7）：預先把每個單字所有「前綴#後綴」組合存進雜湊表，查詢 O(1)；或用「後綴#單字」建字典樹。",
 "zh": [
   "設計 <code>WordFilter(words)</code> 與 <code>f(pref, suff)</code>：回傳同時有前綴 <code>pref</code> 與後綴 <code>suff</code> 的單字在 <code>words</code> 中的<strong>索引</strong>；有多個時回傳最大的索引，沒有則回傳 −1。",
   "單字長度 ≤ 7，最多 10⁴ 個單字、10⁴ 次查詢。",
 ],
 "idea": [
   ("c", """【單字很短 -> 預先計算所有組合】
    長度 L 的單字有 (L+1) 個前綴、(L+1) 個後綴，
    組合 (L+1)² <= 64 種。
    全部存成 "前綴#後綴" -> 索引。
    依序處理單字，後面的覆蓋前面的 -> 自然留下最大索引。
    10⁴ × 64 ≈ 64 萬個鍵，查詢 O(1)。

【字典樹做法】
    對每個單字 w，把 "後綴 + '#' + w" 的所有版本插入字典樹，
    每個節點記錄經過它的最大索引。
    查詢 "suff#pref" 走到底即可。"""),
 ],
 "approaches": [
   ap("解法", "預先計算所有前綴#後綴", [("c", S["p745"]), "驗證方式：和逐一檢查 startswith / endswith 的暴力法比對 500 組。"], "建構 O(N · L³)，查詢 O(L)", "O(N · L³)", "N 為單字數；字串切片與雜湊的成本含在 L 中", "", optimal=True),
 ],
 "edges": ["<strong>重複的單字</strong> → 留最大索引。", "<strong>前綴或後綴是整個單字</strong> → 也包含在組合中。"],
 "follow": [("h", "取捨"), ("c", "空間換時間：單字長度小時預先計算最快；單字很長時就要用字典樹或兩棵字典樹（前綴樹、後綴樹）取交集。")],
 "related": ["<strong>第 208 題 實作字典樹</strong>", "<strong>第 211 題 新增與搜尋單字</strong>"],
 "check": ["為什麼依序處理單字就能留下最大索引？", "預先計算的鍵有多少個？"],
})


# ==================== 746. Min Cost Climbing Stairs ====================
S["p746"] = '''class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = b = 0                       # 到達第 i-2、i-1 階的最小花費（起點 0、1 免費）
        for i in range(2, len(cost) + 1):
            # ★ 到達第 i 階：從 i-1 踩上來（付 cost[i-1]）或從 i-2 跨上來（付 cost[i-2]）
            a, b = b, min(b + cost[i - 1], a + cost[i - 2])
        return b'''

_p746 = S.load("p746")
assert _p746.minCostClimbingStairs([10, 15, 20]) == 15 and _p746.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
from functools import lru_cache
for _ in range(1500):
    c = tuple(random.randint(0, 9) for _ in range(random.randint(2, 10)))
    @lru_cache(None)
    def f(i):
        if i >= len(c): return 0
        return c[i] + min(f(i + 1), f(i + 2))
    assert _p746.minCostClimbingStairs(list(c)) == min(f(0), f(1))
print("P746 OK")

em({
 "num": 746, "title": "使用最小花費爬樓梯",
 "desc": "爬樓梯的最小成本版：到達第 i 階 = min(從 i−1 踩上來, 從 i−2 跨上來)，兩個變數滾動。",
 "zh": [
   "給你陣列 <code>cost</code>，<code>cost[i]</code> 是踩在第 i 階要付的費用。付費後可以往上爬 1 階或 2 階。",
   "可以從第 0 階或第 1 階開始。回傳到達<strong>樓頂</strong>（超過最後一階）的最小花費。",
 ],
 "idea": [
   ("c", """【dp[i] = 到達第 i 階（還沒付第 i 階的錢）的最小花費】
    dp[0] = dp[1] = 0（可以直接從這裡開始）
    dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
    樓頂是第 n 階 -> dp[n]。

【只依賴前兩項】
    兩個變數滾動，O(1) 空間。"""),
 ],
 "approaches": [
   ap("解法", "DP（滾動變數）", [("c", S["p746"]), "驗證方式：和「從某階出發、付費後往上 1 或 2 階」的記憶化遞迴比對 1500 組。"], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>只有兩階</strong> → min(cost[0], cost[1])。", "<strong>樓頂</strong>是 n，不是 n−1。"],
 "follow": [("h", "狀態定義的兩種方式"), ("c", "也可以定義 dp[i] = 踩在第 i 階（含付費）的最小花費，答案是 min(dp[n−1], dp[n−2])。兩種都對，重點是定義清楚。")],
 "related": ["<strong>第 70 題 爬樓梯</strong>", "<strong>第 509 題 斐波那契數</strong>", "<strong>第 198 題 打家劫舍</strong>"],
 "check": ["dp[i] 的定義是什麼？", "樓頂是第幾階？"],
})


# ==================== 747. Largest Number At Least Twice of Others ====================
S["p747"] = '''class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        i = max(range(len(nums)), key=nums.__getitem__)         # 最大值的位置
        # ★ 只要比第二大的兩倍還大，就比所有其他數的兩倍都大
        second = max((x for j, x in enumerate(nums) if j != i), default=0)
        return i if nums[i] >= 2 * second else -1'''

_p747 = S.load("p747")
for _ in range(3000):
    a = random.sample(range(0, 30), random.randint(2, 6))
    i = a.index(max(a))
    assert _p747.dominantIndex(a) == (i if all(a[i] >= 2 * x for j, x in enumerate(a) if j != i) else -1)
print("P747 OK")

em({
 "num": 747, "title": "至少是其他數字兩倍的最大數",
 "desc": "只需比較最大值與第二大值：最大值 ≥ 2 × 第二大，就 ≥ 2 × 所有其他數。",
 "zh": ["給你整數陣列 <code>nums</code>，其中最大的數是唯一的。判斷最大的數是否<strong>至少是其他每個數的兩倍</strong>；是則回傳最大數的索引，否則回傳 <code>-1</code>。"],
 "idea": [
   ("c", """【只看第二大】
    最大值 >= 2 × 第二大 -> 第二大以下的數更小，自然也成立。
    一趟掃描同時記錄最大與第二大即可。"""),
 ],
 "approaches": [
   ap("解法", "最大值與第二大值", [("c", S["p747"])], "O(n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>其他數都是 0</strong> → 成立。", "<strong>剛好兩倍</strong> → 成立（至少）。"],
 "follow": [("h", "一趟找前兩名"), ("c", "維護 first、second：新數比 first 大就讓 first 退成 second；只比 second 大就更新 second。")],
 "related": ["<strong>第 414 題 第三大的數</strong>", "<strong>第 628 題 三個數的最大乘積</strong>"],
 "check": ["為什麼只需要和第二大比較？"],
})


# ==================== 748. Shortest Completing Word ====================
S["p748"] = '''class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = Counter(c.lower() for c in licensePlate if c.isalpha())   # 忽略數字與空白，不分大小寫
        best = None
        for w in words:
            if (best is None or len(w) < len(best)) and not need - Counter(w):
                best = w                # ★ need - Counter(w) 為空 <=> w 包含所有需要的字母（含次數）
        return best'''

_p748 = S.load("p748")
assert _p748.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"]) == "steps"
assert _p748.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]) == "pest"
print("P748 OK")

em({
 "num": 748, "title": "最短補全詞",
 "desc": "把車牌中的字母（轉小寫）計數，找第一個「每個字母次數都夠」的最短單字；Counter 相減為空就代表涵蓋。",
 "zh": [
   "給你車牌字串 <code>licensePlate</code> 和單字陣列 <code>words</code>。<strong>補全詞</strong>是包含車牌中所有字母的單字（忽略數字和空白、不分大小寫；同一個字母出現幾次，單字中也要至少出現幾次）。",
   "回傳<strong>最短</strong>的補全詞；有多個時回傳 <code>words</code> 中最先出現的。題目保證答案存在。",
 ],
 "idea": [
   ("c", """【計數比較】
    need = 車牌中每個字母（小寫）的次數。
    w 是補全詞 <=> 對每個字母 c，count_w(c) >= need(c)。

【Counter 的減法】
    need - Counter(w) 只保留正數：
    結果為空 <=> 每個需要的字母都夠。

【最短 + 最先出現】
    只有嚴格更短才更新 -> 同長度保留先出現的。"""),
 ],
 "approaches": [
   ap("解法", "字母計數", [("c", S["p748"])], "O(Σ|w|)", "O(1)", "字母表大小固定", "", optimal=True),
 ],
 "edges": ["<strong>車牌有重複字母</strong> → 單字也要有足夠次數。", "<strong>大小寫</strong> → 統一轉小寫。", "<strong>同長度</strong> → 先出現的。"],
 "follow": [("h", "多重集合包含"), ("c", "「A 的字母多重集合包含 B」：第 383 題（贖金信）、第 691 題（貼紙拼詞）也是同樣的計數比較。")],
 "related": ["<strong>第 383 題 贖金信</strong>", "<strong>第 691 題 貼紙拼詞</strong>"],
 "check": ["怎麼用 Counter 判斷一個單字涵蓋所有需要的字母？", "同長度時為什麼不更新？"],
})


# ==================== 749. Contain Virus ====================
S["p749"] = '''class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        g = isInfected
        m, n = len(g), len(g[0])
        walls = 0
        while True:
            regions, frontiers, wall_counts = [], [], []
            seen = set()
            for i in range(m):
                for j in range(n):
                    if g[i][j] == 1 and (i, j) not in seen:
                        cells, front, w = [], set(), 0
                        stack = [(i, j)]
                        seen.add((i, j))
                        while stack:                        # 找出一個感染區域
                            x, y = stack.pop()
                            cells.append((x, y))
                            for a, b in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                                if 0 <= a < m and 0 <= b < n:
                                    if g[a][b] == 0:
                                        front.add((a, b))   # 下一輪會被感染的格子
                                        w += 1              # 每一個相鄰的「區域-健康格」邊界都要一道牆
                                    elif g[a][b] == 1 and (a, b) not in seen:
                                        seen.add((a, b))
                                        stack.append((a, b))
                        regions.append(cells)
                        frontiers.append(front)
                        wall_counts.append(w)
            if not regions:
                return walls
            k = max(range(len(regions)), key=lambda t: len(frontiers[t]))   # ★ 威脅最大的區域
            if not frontiers[k]:
                return walls
            walls += wall_counts[k]
            for x, y in regions[k]:
                g[x][y] = -1                                # 被隔離，之後不再擴散
            for t, front in enumerate(frontiers):
                if t != k:
                    for x, y in front:
                        g[x][y] = 1                         # 其他區域擴散一格'''

_p749 = S.load("p749")
assert _p749.containVirus([[0, 1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]) == 10
assert _p749.containVirus([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 4
assert _p749.containVirus([[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 0, 0]]) == 13
print("P749 OK")

em({
 "num": 749, "title": "隔離病毒",
 "desc": "照規則模擬：每天找出所有感染區域，替「下一輪威脅最多健康格」的區域築牆，其他區域往外擴散一格。",
 "zh": [
   "<code>isInfected</code> 是一個世界地圖：<code>1</code> 是感染區、<code>0</code> 是健康區。病毒每晚會擴散到所有與感染區四方向相鄰的健康格，除非中間有牆。",
   "每天你只能替<strong>一個</strong>感染區域（連通塊）築牆，把它完全圍起來：選擇下一晚會感染最多健康格的那個區域（題目保證不會平手）。",
   "回傳總共需要的牆數；若整個世界都會被感染，回傳到那時為止用的牆數。",
 ],
 "idea": [
   ("c", """【每一天的流程】
    1. 找出所有感染區域（連通塊，不含已隔離的）。
       對每個區域記錄：
           frontier：它下一晚會感染的健康格（集合，去重）
           walls：它需要的牆數 = 區域格與健康格相鄰的「邊」數
                  （同一個健康格可能被兩條邊碰到，各要一道牆）
    2. 選 frontier 最大的區域，加上它的 walls，把它標記為已隔離（-1）。
    3. 其他區域的 frontier 全部變成感染。
    4. 沒有區域或沒有任何威脅時結束。

【注意兩個量的差別】
    「威脅」看的是健康格的個數（去重），
    「牆」看的是邊的個數（不去重）。"""),
 ],
 "approaches": [
   ap("解法", "逐日模擬", [("c", S["p749"]), "驗證方式：題目三個範例（含區域內部被包住的健康格需要 4 道牆的情況）。"], "O((mn)²)", "O(mn)", "每輪 O(mn)；每輪至少隔離一個區域，輪數不超過 mn（寬鬆上界）", "", optimal=True),
 ],
 "edges": ["<strong>同一健康格被一個區域從兩邊碰到</strong> → 威脅算 1 格，牆算 2 道。", "<strong>已隔離的區域</strong> → 之後完全忽略。", "<strong>全部被感染</strong> → 沒有 frontier，結束。"],
 "follow": [("h", "模擬題的技巧"), ("c", "把每一輪需要的資訊（區域、邊界、牆數）一次收集完，再統一更新地圖——邊收集邊修改很容易互相干擾。")],
 "related": ["<strong>第 200 題 島嶼數量</strong>", "<strong>第 994 題 腐爛的橘子</strong>", "<strong>第 463 題 島嶼的周長</strong>"],
 "check": ["威脅數和牆數為什麼不一樣？", "為什麼要先收集完所有區域資訊再更新地圖？"],
})


# ==================== 752. Open the Lock ====================
S["p752"] = '''class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        seen = {"0000"}
        q = deque([("0000", 0)])
        while q:
            s, d = q.popleft()
            if s == target:
                return d
            for i in range(4):
                c = int(s[i])
                for nc in ((c + 1) % 10, (c - 1) % 10):     # ★ 每個轉盤往上或往下轉一格，共 8 個鄰居
                    t = s[:i] + str(nc) + s[i + 1:]
                    if t not in seen and t not in dead:
                        seen.add(t)
                        q.append((t, d + 1))
        return -1'''

_p752 = S.load("p752")
assert _p752.openLock(["0201", "0101", "0102", "1212", "2002"], "0202") == 6
assert _p752.openLock(["8888"], "0009") == 1
assert _p752.openLock(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888") == -1
assert _p752.openLock(["0000"], "8888") == -1
print("P752 OK")

em({
 "num": 752, "title": "打開轉盤鎖",
 "desc": "10⁴ 個密碼狀態的圖上做 BFS：每個狀態有 8 個鄰居，死亡密碼當成障礙物；也可用雙向 BFS 加速。",
 "zh": [
   "一個有 4 個轉盤的密碼鎖，每個轉盤有 0～9 共 10 個數字，可以循環轉動（9 的下一個是 0）。每一步可以把<strong>一個</strong>轉盤轉一格。一開始是 <code>\"0000\"</code>。",
   "<code>deadends</code> 是一組死亡密碼：一旦轉到其中之一，鎖就永遠卡住。回傳轉到 <code>target</code> 的<strong>最少步數</strong>；做不到則回傳 <code>-1</code>。",
 ],
 "idea": [
   ("c", """【狀態圖】
    節點：0000～9999 共 10⁴ 個密碼。
    邊：轉動一個轉盤一格 -> 每個節點 8 個鄰居。
    死亡密碼 = 不能進入的節點。

【最少步數 = 無權圖的最短路徑 = BFS】
    從 "0000" 開始 BFS，第一次到達 target 的層數就是答案。

【起點本身是死亡密碼】
    直接 -1。

【雙向 BFS】
    從起點與終點同時擴展，每次擴展較小的那一邊，
    兩邊相遇時就找到了。搜尋範圍大幅縮小。"""),
 ],
 "approaches": [
   ap("解法", "BFS", [("c", S["p752"])], "O(10⁴ · 8)", "O(10⁴)", optimal=True),
 ],
 "edges": ["<strong>\"0000\" 是死亡密碼</strong> → −1。", "<strong>target == \"0000\"</strong> → 0。", "<strong>target 被死亡密碼完全包圍</strong> → −1。"],
 "follow": [("h", "把問題看成圖"), ("c", "「狀態 + 一步操作」就是一張隱式圖，不需要真的建出來。第 773 題（滑動謎題）、第 127 題（單字接龍）、第 433 題（最小基因變化）都是同一個模式。")],
 "related": ["<strong>第 773 題 滑動謎題</strong>", "<strong>第 127 題 單字接龍</strong>", "<strong>第 433 題 最小基因變化</strong>"],
 "check": ["圖的節點和邊分別是什麼？", "為什麼用 BFS 而不是 DFS？"],
})
