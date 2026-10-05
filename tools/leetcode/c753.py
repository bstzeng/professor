# -*- coding: utf-8 -*-
"""第 753、754、756、757、761、762、763、764 題。"""
import random
from collections import defaultdict
from functools import lru_cache
from itertools import product
from authoring import ap
from lcauto import em
from runner import Src

S = Src()
random.seed(753)


# ==================== 753. Cracking the Safe ====================
S["p753"] = '''class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        if n == 1:
            return "".join(map(str, range(k)))
        seen, res = set(), []

        def dfs(node):                          # node：長度 n-1 的字串（De Bruijn 圖的節點）
            for d in map(str, range(k)):
                edge = node + d                 # 每條邊對應一個長度 n 的密碼
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    res.append(d)               # ★ Hierholzer：走完再記錄（後序），反過來就是歐拉迴路

        start = "0" * (n - 1)
        dfs(start)
        return start + "".join(reversed(res))'''

_p753 = S.load("p753")
import sys
sys.setrecursionlimit(10000)
for n in range(1, 5):
    for k in range(1, 5):
        if k ** n > 300: continue
        s = _p753.crackSafe(n, k)
        assert len(s) == k ** n + n - 1 and len({s[i:i + n] for i in range(len(s) - n + 1)}) == k ** n, (n, k)
print("P753 OK")

em({
 "num": 753, "title": "破解保險箱",
 "desc": "De Bruijn 序列：把長度 n−1 的字串當節點、每個密碼當邊，找一條走過所有邊的歐拉迴路（Hierholzer 演算法）。",
 "zh": [
   "保險箱的密碼是 <code>n</code> 位數，每位是 <code>0</code>～<code>k−1</code>。保險箱會檢查你<strong>最近輸入的 n 位</strong>，只要等於密碼就打開。",
   "回傳一個<strong>最短</strong>的字串，保證在輸入過程中某個時刻能打開保險箱（也就是說，它包含所有 kⁿ 種密碼作為子字串）。",
 ],
 "idea": [
   ("c", """【下界】
    要包含 kⁿ 個不同的長度 n 子字串，
    字串長度至少 kⁿ + n - 1（每多一個字元最多多一個新的子字串）。
    能做到恰好這個長度的序列叫 De Bruijn 序列。

【轉成歐拉迴路】
    節點：所有長度 n-1 的字串（kⁿ⁻¹ 個）。
    邊：從節點 u 加上一個字元 d，得到長度 n 的密碼 u+d，
        走到新節點 (u+d)[1:]。
    每個密碼恰好對應一條邊。
    每個節點出度 = 入度 = k -> 一定存在歐拉迴路。
    沿著迴路寫下每條邊新增的字元，就得到 De Bruijn 序列。

【Hierholzer 演算法】
    DFS 走未用過的邊，回溯時（後序）才把邊記下來，
    最後反轉就是歐拉迴路。"""),
 ],
 "approaches": [
   ap("解法", "De Bruijn 圖 + Hierholzer", [
     ("c", S["p753"]),
     "驗證方式：小範圍的所有 (n, k)，檢查長度恰為 kⁿ + n − 1，且包含全部 kⁿ 種密碼。",
   ], "O(n · kⁿ)", "O(n · kⁿ)", optimal=True),
 ],
 "edges": ["<strong>n = 1</strong> → \"01…(k−1)\"。", "<strong>k = 1</strong> → n 個 0。"],
 "follow": [("h", "歐拉路徑的另一題"), ("c", "第 332 題（重新安排行程）也是 Hierholzer：機票是邊，要找字典序最小的歐拉路徑。De Bruijn 序列在密碼學、DNA 定序、魔術（猜牌）中都有應用。")],
 "related": ["<strong>第 332 題 重新安排行程</strong>", "<strong>第 2097 題 合法重新排列數對</strong>"],
 "check": ["De Bruijn 圖的節點和邊分別是什麼？", "為什麼一定存在歐拉迴路？", "Hierholzer 為什麼要在回溯時才記錄？"],
})


# ==================== 754. Reach a Number ====================
S["p754"] = '''class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)                # 對稱：負的目標和正的一樣
        k = s = 0
        # ★ 走到總和 >= target，而且「多出來的量」是偶數（把其中某些步反向，每反一步少 2 × 步長）
        while s < target or (s - target) % 2:
            k += 1
            s += k
        return k'''

_p754 = S.load("p754")
for t in range(-60, 61):
    k = 0; reach = {0}
    while t not in reach:
        k += 1; reach = {x + d for x in reach for d in (k, -k)}
    assert _p754.reachNumber(t) == k, t
print("P754 OK")

em({
 "num": 754, "title": "到達終點數字",
 "desc": "先一直往右走到總和 ≥ target，多出來的量 d 若是偶數，就把第 d/2 步改成往左；奇數就再多走一兩步。",
 "zh": ["你站在數線的 0。第 i 步（從 1 開始）可以往左或往右走恰好 i 格。回傳到達 <code>target</code> 的<strong>最少步數</strong>。"],
 "idea": [
   ("c", """【對稱】target 取絕對值。

【先全部往右】
    走 k 步，總和 S = 1 + 2 + ... + k。
    需要 S >= target。

【把某些步反向】
    把第 i 步改成往左，總和減少 2i。
    多出來的量 d = S - target：
        d 是偶數 -> 可以挑一些步，讓它們的和恰好是 d/2，反向即可
                   （1..k 可以湊出 0..S 之間的任何整數）
        d 是奇數 -> 反向只能改變偶數量，不行，再多走一步
    多走 1 或 2 步之內，d 一定會變成偶數。

【答案】
    最小的 k 使 S >= target 且 (S - target) 為偶數。"""),
 ],
 "approaches": [
   ap("解法", "數學", [("c", S["p754"]), "驗證方式：−60～60 所有目標和「枚舉每一步左右」的 BFS 比對。"], "O(√target)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>負的 target</strong> → 取絕對值。", "<strong>target = 2</strong> → 3 步（+1 −2 +3）。"],
 "follow": [("h", "為什麼 1..k 能湊出任何 0..S 的數？"), ("c", "歸納：1..k−1 能湊出 0..S(k−1)，加入 k 後能湊出 k..S(k)；兩段重疊（k ≤ S(k−1)+1），所以覆蓋 0..S(k)。")],
 "related": ["<strong>第 70 題 爬樓梯</strong>", "<strong>第 991 題 壞了的計算器</strong>"],
 "check": ["把一步反向會讓總和改變多少？", "多出來的量為什麼必須是偶數？"],
})


# ==================== 756. Pyramid Transition Matrix ====================
S["p756"] = '''class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        tops = defaultdict(list)
        for a in allowed:
            tops[a[:2]].append(a[2])            # 底部兩個方塊 -> 可以放在上面的方塊

        @cache
        def can(row):                           # 從這一列開始能否堆到頂
            if len(row) == 1:
                return True
            # ★ 上一列的每個位置都有幾種選擇：枚舉所有組合（笛卡兒積）
            for nxt in product(*(tops[row[i:i + 2]] for i in range(len(row) - 1))):
                if can("".join(nxt)):
                    return True
            return False
        return can(bottom)'''

_p756 = S.load("p756")
assert _p756.pyramidTransition("BCD", ["BCC", "CDE", "CEA", "FFF"]) and not _p756.pyramidTransition("AAAA", ["AAB", "AAC", "BCD", "BBE", "DEF"])
def _bf756(bottom, allowed):
    al = set(allowed)
    def go(row):
        if len(row) == 1: return True
        for cand in product("ABCDEF", repeat=len(row) - 1):
            if all(row[i] + row[i + 1] + cand[i] in al for i in range(len(row) - 1)) and go("".join(cand)): return True
        return False
    return go(bottom)
for _ in range(300):
    al = list({"".join(random.choice("ABC") for _ in range(3)) for _ in range(random.randint(1, 12))})
    b = "".join(random.choice("ABC") for _ in range(random.randint(2, 4)))
    _p756 = S.load("p756")
    assert _p756.pyramidTransition(b, al) == _bf756(b, al)
print("P756 OK")

em({
 "num": 756, "title": "金字塔轉換矩陣",
 "desc": "一列一列往上堆：每個位置的候選由下方兩個方塊決定，枚舉整列的組合並對「列」記憶化。",
 "zh": [
   "你要用彩色方塊（以字母 A～F 表示）堆一座金字塔，每往上一列少一個方塊。",
   "每個三角形圖案必須是允許的：<code>allowed</code> 中的字串 <code>\"ABC\"</code> 代表左下是 A、右下是 B 時，上面可以放 C。",
   "給你最底層 <code>bottom</code>，判斷能否堆到只剩一個方塊的頂端。",
 ],
 "idea": [
   ("c", """【一列一列往上】
    目前這一列 row，上一列的第 i 個方塊必須是
    tops[row[i] + row[i+1]] 中的一個。
    枚舉上一列所有可能的組合，遞迴往上。

【記憶化】
    同一列字串可能透過不同路徑產生 -> 用 cache 記住某列「堆不上去」。
    最底層長度 <= 6，列的種類有限。

【剪枝】
    某個位置沒有任何候選 -> product 是空的，直接失敗。"""),
 ],
 "approaches": [
   ap("解法", "回溯 + 記憶化", [("c", S["p756"]), "驗證方式：和枚舉每一列所有字母組合的暴力法比對 300 組。"], "O(Aᴺ)", "O(Aᴺ)", "A 為字母種類、N 為底層長度（最壞情況）", "", optimal=True),
 ],
 "edges": ["<strong>底層長度 2</strong> → 只要 allowed 中有對應的三角形。", "<strong>某對方塊沒有任何允許的頂端</strong> → 立即失敗。"],
 "follow": [("h", "逐格生成的寫法"), ("c", "也可以一格一格填上一列：dfs(row, 已填的上一列前綴)，填滿就遞迴到上一列。比先產生整列的笛卡兒積更早剪枝。")],
 "related": ["<strong>第 118 題 楊輝三角</strong>", "<strong>第 37 題 解數獨</strong>"],
 "check": ["上一列每個位置的候選由什麼決定？", "為什麼可以對「列」做記憶化？"],
})


# ==================== 757. Set Intersection Size At Least Two ====================
S["p757"] = '''class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # 依右端點遞增排序；右端相同時左端大的（較短的）先處理
        intervals.sort(key=lambda x: (x[1], -x[0]))
        a, b = -1, -1                   # 目前集合中最大的兩個數（a < b）
        res = 0
        for l, r in intervals:
            if l > b:                   # 一個都沒有：放入最右邊的兩個 r-1、r
                a, b = r - 1, r
                res += 2
            elif l > a:                 # 只有 b：再放入 r
                a, b = b, r             # ★ 貪心：選得越右邊，越可能同時落在後面的區間裡
                res += 1
            # 已經有兩個：不用動
        return res'''

_p757 = S.load("p757")
assert _p757.intersectionSizeTwo([[1, 3], [3, 7], [8, 9]]) == 5
assert _p757.intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]) == 3
assert _p757.intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]) == 5
for _ in range(600):
    iv = []
    for _ in range(random.randint(1, 5)):
        l = random.randint(0, 6); iv.append([l, l + random.randint(1, 3)])
    pts = sorted({x for l, r in iv for x in range(l, r + 1)})
    best = None
    for k in range(len(pts) + 1):
        from itertools import combinations
        for S_ in combinations(pts, k):
            if all(sum(l <= x <= r for x in S_) >= 2 for l, r in iv):
                best = k; break
        if best is not None: break
    assert _p757.intersectionSizeTwo([x[:] for x in iv]) == best
print("P757 OK")

em({
 "num": 757, "title": "設置交集大小至少為 2",
 "desc": "依右端點排序後貪心：每個區間不夠兩個點時，補上最靠右的點（r 或 r−1、r），讓它們盡量也落在後面的區間。",
 "zh": [
   "給你一組閉區間 <code>intervals</code>。找出一個<strong>最小</strong>的整數集合 <code>nums</code>，使得每個區間都至少包含 nums 中的<strong>兩個</strong>整數。",
   "回傳這個集合的大小。",
 ],
 "idea": [
   ("c", """【「至少一個」的版本：區間刺穿】
    依右端排序，每個區間沒被刺到就在它的右端放一個點。

【至少兩個】
    依右端遞增排序，維護集合中最大的兩個數 a < b。
    處理區間 [l, r]：
        l > b：一個都沒有 -> 放 r-1 和 r（最右邊的兩個）
        a < l <= b：只有 b -> 再放 r
        l <= a：已經有兩個
    選最右邊的點：後面的區間右端更大，越右的點越可能也落在裡面。

【平手時的排序】
    右端相同時，左端大（較短）的先處理。
    反例：先處理較長的區間，它若只缺一個點就只補 r；
    接著較短的區間可能只包含 r，又要補一個點 —— 但 r 已經用掉，
    貪心會想再放一次 r，變成重複。
    先處理短的就會直接放 r-1、r，長的區間自然也包含這兩點。"""),
 ],
 "approaches": [
   ap("解法", "排序 + 貪心", [("c", S["p757"]), "驗證方式：和枚舉所有點集合（由小到大）的暴力法比對 600 組。"], "O(n log n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>區間長度 1</strong>（如 [3,4]）→ 必須取 3 和 4。", "<strong>右端相同</strong> → 左端大的先處理。", "<strong>只有 b 在區間內</strong> → 補 r，並更新 a = b。"],
 "follow": [("h", "一般化"), ("c", "每個區間至少 k 個點：同樣依右端排序，不足時從右端往左補上缺少的數量（避開已選的點）。")],
 "related": ["<strong>第 452 題 用最少數量的箭引爆氣球</strong>", "<strong>第 435 題 無重疊區間</strong>", "<strong>第 646 題 最長數對鏈</strong>"],
 "check": ["為什麼補點時要選最右邊的？", "右端相同時為什麼左端大的先處理？"],
})


# ==================== 761. Special Binary String ====================
S["p761"] = '''class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts, bal, start = [], 0, 0
        for i, c in enumerate(s):
            bal += 1 if c == "1" else -1
            if bal == 0:                    # 找到一個「不可再分」的特殊子字串 1 X 0
                inner = self.makeLargestSpecial(s[start + 1:i])   # 遞迴把內部變成最大
                parts.append("1" + inner + "0")
                start = i + 1
        # ★ 相鄰的特殊子字串可以任意交換 -> 由大到小排序就是字典序最大
        return "".join(sorted(parts, reverse=True))'''

_p761 = S.load("p761")
assert _p761.makeLargestSpecial("11011000") == "11100100"
def _special(s):
    b = 0
    for c in s:
        b += 1 if c == "1" else -1
        if b < 0: return False
    return b == 0
def _bf761(s):
    from collections import deque
    best = s; seen = {s}; q = deque([s]); n = len(s)
    while q:
        t = q.popleft(); best = max(best, t)
        for i in range(n):
            for j in range(i + 2, n + 1, 2):
                if not _special(t[i:j]): continue
                for k in range(j + 2, n + 1, 2):
                    if _special(t[j:k]):
                        u = t[:i] + t[j:k] + t[i:j] + t[k:]
                        if u not in seen: seen.add(u); q.append(u)
    return best
def _rand_special(n):
    if n == 0: return ""
    k = random.randint(1, n)
    return "1" + _rand_special(k - 1) + "0" + _rand_special(n - k)
for _ in range(300):
    s = _rand_special(random.randint(1, 5))
    assert _p761.makeLargestSpecial(s) == _bf761(s), s
print("P761 OK")

em({
 "num": 761, "title": "特殊的二進位序列",
 "desc": "特殊字串就是合法的括號序列（1 = 左括號、0 = 右括號）：拆成頂層的不可分段落，各自遞迴最大化內部，再由大到小排序。",
 "zh": [
   "<strong>特殊的二進位字串</strong>滿足：0 和 1 的數量相同，而且每個前綴中 1 的數量都不少於 0 的數量。",
   "每次操作可以選兩個<strong>相鄰</strong>且都是特殊字串的非空子字串，交換它們。給你一個特殊字串 <code>s</code>，回傳經過任意次操作後能得到的<strong>字典序最大</strong>的字串。",
 ],
 "idea": [
   ("c", """【特殊字串 = 合法的括號序列】
    1 看成 '('，0 看成 ')'。

【結構】
    每個特殊字串可以唯一拆成若干個「不可再分」的段落：
        s = A₁ A₂ ... Aₖ，每個 Aᵢ = 1 Xᵢ 0，Xᵢ 也是特殊字串。
    （掃描時平衡值回到 0 的位置就是段落的結尾。）

【可以做的事】
    交換相鄰的特殊子字串 -> 頂層的段落可以任意重排；
    段落內部的 Xᵢ 也可以遞迴地重排。

【怎麼最大】
    1. 遞迴：把每個 Xᵢ 變成它能達到的最大值。
    2. 把所有段落由大到小排序接起來。
    （段落都以 1 開頭、以 0 結尾，直接比字串大小即可。）"""),
 ],
 "approaches": [
   ap("解法", "遞迴分解 + 排序", [
     ("c", S["p761"]),
     "驗證方式：在長度 ≤ 10 的隨機特殊字串上，和 BFS 窮舉所有可達字串取最大值比對 300 組。",
   ], "O(n²)", "O(n)", "", "", optimal=True),
 ],
 "edges": ["<strong>\"10\"</strong> → 不變。", "<strong>只有一個頂層段落</strong> → 只能改內部。"],
 "follow": [("h", "排序為什麼正確？"), ("c", "每個段落都是「1…0」形式的完整括號，兩個段落 A、B 比較時，A > B 就代表 AB > BA（不會出現一個是另一個前綴而影響比較的情況，因為段落是完整閉合的）。")],
 "related": ["<strong>第 20 題 有效的括號</strong>", "<strong>第 22 題 括號生成</strong>", "<strong>第 856 題 括號的分數</strong>"],
 "check": ["特殊字串和括號序列有什麼關係？", "為什麼頂層段落可以任意重排？"],
})


# ==================== 762. Prime Number of Set Bits in Binary Representation ====================
S["p762"] = '''class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}       # ★ right <= 10⁶ < 2²⁰，1 的個數最多 20
        return sum(bin(x).count("1") in primes for x in range(left, right + 1))'''

_p762 = S.load("p762")
assert _p762.countPrimeSetBits(6, 10) == 4 and _p762.countPrimeSetBits(10, 15) == 5
print("P762 OK")

em({
 "num": 762, "title": "二進位表示中質數個計算置位",
 "desc": "1 的個數最多 20，質數只有 8 個：預先列好，逐一計算 popcount 判斷即可。",
 "zh": ["給你兩個整數 <code>left</code> 和 <code>right</code>，回傳範圍內（含兩端）二進位表示中<strong>1 的個數是質數</strong>的整數個數。"],
 "idea": [
   ("c", """【1 的個數最多 20】
    right <= 10⁶ < 2²⁰ -> popcount <= 20。
    20 以內的質數：2, 3, 5, 7, 11, 13, 17, 19。

【位元遮罩的寫法】
    把這些質數存成一個 int 的位元：
        mask = 0b10100010100010101100（第 p 位為 1 代表 p 是質數）
    判斷 (mask >> popcount) & 1。"""),
 ],
 "approaches": [
   ap("解法", "逐一計算 popcount", [("c", S["p762"])], "O((right − left) · log right)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>1 個 1</strong>（2 的次方）→ 1 不是質數。"],
 "follow": [("h", "更快的計算"), ("c", "Python 3.10+ 有 int.bit_count()；其他語言有內建 popcount 指令。若範圍很大，可以用數位 DP 數「1 的個數為 k」的數有幾個。")],
 "related": ["<strong>第 191 題 位元 1 的個數</strong>", "<strong>第 338 題 位元計數</strong>"],
 "check": ["為什麼只需要考慮 20 以內的質數？"],
})


# ==================== 763. Partition Labels ====================
S["p763"] = '''class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}      # 每個字母最後出現的位置
        res, start, end = [], 0, 0
        for i, c in enumerate(s):
            end = max(end, last[c])                 # 目前這段至少要延伸到這裡
            if i == end:                            # ★ 段內所有字母的最後位置都到齊了：可以切
                res.append(end - start + 1)
                start = i + 1
        return res'''

_p763 = S.load("p763")
assert _p763.partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
for _ in range(2000):
    s = "".join(random.choice("abcde") for _ in range(random.randint(1, 12)))
    cuts = [i for i in range(1, len(s)) if not set(s[:i]) & set(s[i:])]
    b = [0] + cuts + [len(s)]
    assert _p763.partitionLabels(s) == [b[i + 1] - b[i] for i in range(len(b) - 1)]
print("P763 OK")

em({
 "num": 763, "title": "劃分字母區間",
 "desc": "記錄每個字母最後出現的位置；掃描時不斷延伸目前段落的終點，走到終點就切一刀。",
 "zh": [
   "給你字串 <code>s</code>，把它劃分成<strong>盡可能多</strong>的段落，使每個字母最多只出現在一個段落中。",
   "依序回傳每個段落的長度。",
 ],
 "idea": [
   ("c", """【一個字母出現的位置必須全在同一段】
    段落一旦包含字母 c，就必須延伸到 c 最後出現的位置。

【貪心掃描】
    end = 目前段落至少要到的位置。
    每讀到一個字母，end = max(end, last[c])。
    i == end：段落中所有字母的最後位置都已經包含了，
              在這裡切最早，能切出最多段。"""),
 ],
 "approaches": [
   ap("解法", "最後位置 + 貪心", [("c", S["p763"]), "驗證方式：和「所有能切的位置（左右兩邊沒有共同字母）都切」的方法比對 2000 組。"], "O(n)", "O(1)", "字母表大小固定", "", optimal=True),
 ],
 "edges": ["<strong>所有字母都不同</strong> → 每段長度 1。", "<strong>首尾字母相同</strong> → 整個字串一段。"],
 "follow": [("h", "區間合併的角度"), ("c", "每個字母對應一個區間 [第一次, 最後一次]，問題變成合併重疊的區間（第 56 題），合併後每段的長度就是答案。")],
 "related": ["<strong>第 56 題 合併區間</strong>", "<strong>第 769 題 最多能完成排序的區塊</strong>"],
 "check": ["什麼時候可以切一刀？", "為什麼在最早能切的地方切，能得到最多段？"],
})


# ==================== 764. Largest Plus Sign ====================
S["p764"] = '''class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        bad = {(r, c) for r, c in mines}
        # dp[i][j]：以 (i, j) 為中心，四個方向連續 1 的長度的最小值
        dp = [[n] * n for _ in range(n)]
        for i in range(n):
            # ★ 每一列、每一欄各從兩個方向掃一次，記錄連續 1 的長度
            for order in (range(n), range(n - 1, -1, -1)):
                run = 0
                for j in order:
                    run = 0 if (i, j) in bad else run + 1
                    dp[i][j] = min(dp[i][j], run)
                run = 0
                for j in order:
                    run = 0 if (j, i) in bad else run + 1
                    dp[j][i] = min(dp[j][i], run)
        return max(map(max, dp))'''

_p764 = S.load("p764")
assert _p764.orderOfLargestPlusSign(5, [[4, 2]]) == 2 and _p764.orderOfLargestPlusSign(1, [[0, 0]]) == 0
for _ in range(500):
    n = random.randint(1, 7)
    mines = [[random.randrange(n), random.randrange(n)] for _ in range(random.randint(0, n * n // 2))]
    bad = {tuple(m) for m in mines}
    g = [[0 if (i, j) in bad else 1 for j in range(n)] for i in range(n)]
    best = 0
    for i in range(n):
        for j in range(n):
            k = 0
            while all(0 <= x < n and 0 <= y < n and g[x][y] for x, y in ((i - k, j), (i + k, j), (i, j - k), (i, j + k))):
                k += 1
            best = max(best, k)
    assert _p764.orderOfLargestPlusSign(n, mines) == best
print("P764 OK")

em({
 "num": 764, "title": "最大加號標誌",
 "desc": "每個格子往四個方向的連續 1 長度取最小值，就是以它為中心的加號階數；四次方向掃描各 O(n²)。",
 "zh": [
   "在 <code>n x n</code> 的格子中，除了 <code>mines</code> 列出的位置是 0，其他都是 1。",
   "<strong>k 階加號</strong>以某個 1 為中心，往上下左右各延伸 k−1 格，全部都是 1。回傳格子中最大加號的階數；若沒有任何 1，回傳 0。",
 ],
 "idea": [
   ("c", """【以 (i, j) 為中心的最大階數】
    = min(往上、往下、往左、往右的連續 1 個數，含自己)。

【四個方向各掃一次】
    往右的連續長度：由左往右掃，遇 0 歸零、遇 1 加一。
    其他三個方向同理。
    每個格子取四個值的最小值。

【實作技巧】
    用同一個 dp 陣列直接取 min，不必存四份。
    每一列從左右兩邊掃、每一欄從上下兩邊掃。"""),
 ],
 "approaches": [
   ap("解法", "四方向連續長度 DP", [("c", S["p764"]), "驗證方式：和「從每個中心往外逐層檢查」的暴力法比對 500 組。"], "O(n²)", "O(n²)", optimal=True),
 ],
 "edges": ["<strong>全部是 0</strong> → 0。", "<strong>沒有地雷</strong> → (n + 1) // 2。"],
 "follow": [("h", "四方向掃描"), ("c", "「每個位置往四個方向能延伸多遠」：第 85 題（最大矩形）、第 221 題（最大正方形）、第 1139 題（最大的以 1 為邊界的正方形）都用類似的預處理。")],
 "related": ["<strong>第 221 題 最大正方形</strong>", "<strong>第 85 題 最大矩形</strong>", "<strong>第 1139 題 最大的以 1 為邊界的正方形</strong>"],
 "check": ["以某格為中心的加號階數怎麼由四個方向決定？", "為什麼掃描時遇到 0 要歸零？"],
})
