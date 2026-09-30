# -*- coding: utf-8 -*-
"""第 433–438 題。"""
import random
import itertools
from collections import Counter, deque
from authoring import emit, ap
from runner import Src
from lchelp import lv, rand_tree

S = Src()
random.seed(433)
_DQ = {"deque": deque}


# ==================== 433. Minimum Genetic Mutation ====================
S["p433"] = '''class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        valid = set(bank)
        if endGene not in valid:
            return -1
        q = deque([(startGene, 0)])
        seen = {startGene}
        while q:                                   # ★ BFS：第一次到達就是最少步數
            gene, d = q.popleft()
            if gene == endGene:
                return d
            for i in range(8):
                for c in "ACGT":                   # 改一個字元
                    nxt = gene[:i] + c + gene[i + 1:]
                    if nxt in valid and nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, d + 1))
        return -1'''

_p433 = S.load("p433", extra=_DQ)
for s, e, bank, want in [("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1), ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
                         ("AAAAAAAA", "CCCCCCCC", [], -1), ("AACCGGTT", "AACCGGTT", ["AACCGGTT"], 0)]:
    assert _p433.minMutation(s, e, bank) == want


def _mm_ref(s, e, bank):
    nodes = list({s} | set(bank))
    if e not in bank:
        return -1
    dist = {s: 0}
    changed = True
    while changed:
        changed = False
        for a in list(dist):
            for b in nodes:
                if b in bank and sum(x != y for x, y in zip(a, b)) == 1 and dist[a] + 1 < dist.get(b, 99):
                    dist[b] = dist[a] + 1
                    changed = True
    return dist.get(e, -1)


for _ in range(800):
    mk = lambda: "".join(random.choice("AC") for _ in range(8))
    s, e = mk(), mk()
    bank = list({mk() for _ in range(random.randrange(0, 30))})
    if random.random() < 0.5:
        bank.append(e)
    assert _p433.minMutation(s, e, bank) == _mm_ref(s, e, bank), (s, e, bank)
print("P433 OK")

emit({
 "num": 433, "slug": "minimum-genetic-mutation",
 "en": [
   "A gene string can be represented by an 8-character long string, with choices from <code>'A'</code>, <code>'C'</code>, <code>'G'</code>, and <code>'T'</code>.",
   "Suppose we need to investigate a mutation from a gene string <code>startGene</code> to a gene string <code>endGene</code> where one mutation is defined as one single character changed in the gene string. For example, <code>\"AACCGGTT\" --&gt; \"AACCGGTA\"</code> is one mutation.",
   "There is also a gene bank <code>bank</code> that records all the valid gene mutations. A gene must be in <code>bank</code> to make it a valid gene string.",
   "Given the two gene strings <code>startGene</code> and <code>endGene</code> and the gene bank <code>bank</code>, return <em>the minimum number of mutations needed to mutate from</em> <code>startGene</code> <em>to</em> <code>endGene</code>. If there is no such a mutation, return <code>-1</code>.",
   "Note that the starting point is assumed to be valid, so it might not be included in the bank.",
 ],
 "zh": [
   "基因字串長度 8，由 <code>A</code>、<code>C</code>、<code>G</code>、<code>T</code> 組成。一次<strong>突變</strong>是改變其中一個字元。",
   "基因庫 <code>bank</code> 記錄所有合法的基因；突變後的基因必須在基因庫裡。",
   "回傳從 <code>startGene</code> 突變到 <code>endGene</code> 的最少次數；做不到回傳 <code>-1</code>。起點不一定在基因庫裡。",
 ],
 "examples": """範例 1
  輸入：startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
  輸出：1

範例 2
  輸入：startGene = "AACCGGTT", endGene = "AAACGGTA",
        bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
  輸出：2""",
 "constraints": [
   "0 ≤ <code>bank.length</code> ≤ 10",
   "所有基因字串長度都是 8，只包含 <code>A、C、G、T</code>",
 ],
 "idea": [
   ("c", """【最少步數 -> BFS】
    每個基因是一個節點，差一個字元（而且在基因庫中）的基因之間有邊。
    從起點 BFS，第一次到達終點的層數就是答案。

【怎麼找鄰居？】
    對 8 個位置 × 4 種字元，產生 32 個候選，
    在基因庫的集合裡查。

【和第 127 題「單字接龍」一模一樣】
    只是字母表從 26 個縮成 4 個。"""),
 ],
 "approaches": [
   ap("解法", "BFS", [
     ("c", S["p433"]),
   ], "O(B · 8 · 4)", "O(B)", "B = 基因庫大小", "", optimal=True),
 ],
 "edges": [
   "<strong>終點不在基因庫</strong> → −1。",
   "<strong>起點等於終點</strong> → 0。",
   "<strong>起點不在基因庫</strong> → 沒關係，起點預設合法。",
 ],
 "follow": [
   ("h", "雙向 BFS"),
   ("c", "狀態空間大時（例如第 127 題有 5000 個單字），從起點和終點同時 BFS，每次擴展較小的那一邊，可以大幅減少拜訪的節點。"),
 ],
 "related": [
   "<strong>第 127 題 單字接龍</strong>",
   "<strong>第 752 題 開啟轉盤鎖</strong>",
 ],
 "check": [
   "為什麼用 BFS？",
   "怎麼產生一個基因的所有鄰居？",
 ],
})


# ==================== 434. Number of Segments in a String ====================
S["p434"] = '''class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        for i, ch in enumerate(s):
            # ★ 一個段落的開頭：自己不是空白，而且前一個是空白（或是字串開頭）
            if ch != " " and (i == 0 or s[i - 1] == " "):
                count += 1
        return count'''

S["p434_py"] = '''class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())          # 不帶參數的 split 會自動處理連續空白'''

_p434 = [S.load(x) for x in ("p434", "p434_py")]
for _ in range(3000):
    s = "".join(random.choice("ab  ,") for _ in range(random.randrange(0, 12)))
    want = len([w for w in s.split(" ") if w])
    for sol in _p434:
        assert sol.countSegments(s) == want
print("P434 OK")

emit({
 "num": 434, "slug": "number-of-segments-in-a-string",
 "en": [
   "Given a string <code>s</code>, return <em>the number of segments in the string</em>.",
   "A <strong>segment</strong> is defined to be a contiguous sequence of <strong>non-space characters</strong>.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，回傳其中的<strong>段落數</strong>。段落是連續的非空白字元。",
 ],
 "examples": """範例 1
  輸入：s = "Hello, my name is John"
  輸出：5

範例 2
  輸入：s = "Hello"
  輸出：1""",
 "constraints": [
   "0 ≤ <code>s.length</code> ≤ 300",
   "<code>s</code> 由英文字母、數字、標點符號和空白 <code>' '</code> 組成",
 ],
 "idea": [
   ("c", """【數「段落的開頭」】
    一個段落的第一個字元：自己不是空白，而且前一個字元是空白（或它在最前面）。
    每個段落恰好有一個開頭 -> 開頭的個數 = 段落數。

【Python 的 split()】
    不帶參數時，會把連續空白當作一個分隔符，並忽略頭尾空白。
    s.split(" ")（帶參數）則會產生空字串 ✘。"""),
 ],
 "approaches": [
   ap("解法一", "split()", [
     ("c", S["p434_py"]),
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "數段落開頭", [
     ("c", S["p434"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、split", "O(n)", "O(n)"],
    ["二、數開頭", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>空字串</strong> → 0。",
   "<strong>全是空白</strong> → 0。",
   "<strong>連續空白、頭尾空白</strong> → 不能產生空段落。",
 ],
 "follow": [
   ("h", "相關題"),
   ("c", "第 58 題（最後一個單字的長度）、第 151 題（反轉單字順序）都要正確處理多餘的空白。"),
 ],
 "related": [
   "<strong>第 58 題 最後一個單字的長度</strong>",
   "<strong>第 151 題 反轉字串中的單字</strong>",
 ],
 "check": [
   "怎麼判斷一個字元是段落的開頭？",
   "<code>split()</code> 和 <code>split(\" \")</code> 有什麼不同？",
 ],
})


# ==================== 435. Non-overlapping Intervals ====================
S["p435"] = '''class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])      # ★ 依「結束時間」排序
        keep = 0
        end = -float("inf")
        for s, e in intervals:
            if s >= end:                        # 和上一個保留的不重疊：保留
                keep += 1
                end = e
        return len(intervals) - keep            # 刪掉的 = 總數 - 最多能保留的'''

_p435 = S.load("p435")


def _eo_ref(iv):
    best = 0
    for r in range(len(iv) + 1):
        for c in itertools.combinations(sorted(iv), r):
            if all(c[i][1] <= c[i + 1][0] for i in range(len(c) - 1)):
                best = max(best, r)
    return len(iv) - best


for iv, want in [([[1, 2], [2, 3], [3, 4], [1, 3]], 1), ([[1, 2], [1, 2], [1, 2]], 2), ([[1, 2], [2, 3]], 0)]:
    assert _p435.eraseOverlapIntervals([x[:] for x in iv]) == want
for _ in range(800):
    iv = []
    for _ in range(random.randrange(1, 8)):
        a = random.randint(0, 8)
        iv.append([a, a + random.randint(1, 4)])
    assert _p435.eraseOverlapIntervals([x[:] for x in iv]) == _eo_ref(iv), iv
print("P435 OK")

_P435_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">依結束時間排序，每次挑「最早結束」而且不衝突的區間</text>
            <line x1="60" y1="190" x2="580" y2="190" stroke="var(--text-muted)"/>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="100" y="206">1</text><text x="200" y="206">2</text><text x="300" y="206">3</text><text x="400" y="206">4</text><text x="500" y="206">5</text>
            </g>
            <g stroke-width="6" stroke-linecap="round">
              <line x1="100" y1="50" x2="200" y2="50" stroke="var(--accent)"/>
              <line x1="100" y1="80" x2="300" y2="80" stroke="#ff8a65"/>
              <line x1="200" y1="110" x2="300" y2="110" stroke="var(--accent)"/>
              <line x1="300" y1="140" x2="400" y2="140" stroke="var(--accent)"/>
            </g>
            <g font-size="12">
              <text x="210" y="54" fill="var(--accent)">[1,2] 最早結束 → 保留</text>
              <text x="310" y="84" fill="#ff8a65">[1,3] 開始 1 &lt; 2 → 衝突，刪掉</text>
              <text x="310" y="114" fill="var(--accent)">[2,3] 保留</text>
              <text x="410" y="144" fill="var(--accent)">[3,4] 保留</text>
            </g>
            <text x="20" y="234" fill="var(--gold)" font-size="12">★ 最早結束的區間，留給後面的空間最多 —— 選它絕不會比選別的差。</text>'''

emit({
 "num": 435, "slug": "non-overlapping-intervals",
 "en": [
   "Given an array of intervals <code>intervals</code> where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code>, return <em>the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping</em>.",
   "<strong>Note</strong> that intervals which only touch at a point are <strong>non-overlapping</strong>. For example, <code>[1, 2]</code> and <code>[2, 3]</code> are non-overlapping.",
 ],
 "zh": [
   "給你一組區間 <code>intervals</code>，回傳<strong>最少</strong>要刪掉幾個區間，才能讓剩下的區間互不重疊。",
   "只在端點接觸的區間不算重疊，例如 <code>[1, 2]</code> 和 <code>[2, 3]</code>。",
 ],
 "examples": """範例 1
  輸入：intervals = [[1,2],[2,3],[3,4],[1,3]]
  輸出：1
  說明：刪掉 [1,3]。

範例 2
  輸入：intervals = [[1,2],[1,2],[1,2]]
  輸出：2

範例 3
  輸入：intervals = [[1,2],[2,3]]
  輸出：0""",
 "constraints": [
   "1 ≤ <code>intervals.length</code> ≤ 10⁵",
   "−5 × 10⁴ ≤ <code>start<sub>i</sub> &lt; end<sub>i</sub></code> ≤ 5 × 10⁴",
 ],
 "idea": [
   ("fig", _P435_FIG, "0 0 640 248"),
   ("c", """【轉換：最少刪幾個 = 總數 - 最多能保留幾個互不重疊的】
    這是經典的「活動選擇問題」。

【貪心：依結束時間排序，能選就選】
    為什麼選「最早結束」的？
    假設最佳解的第一個區間不是最早結束的那個 X，
    把它換成 X：X 結束得更早，不會和後面的衝突 ->
    換完一樣是合法的最佳解。
    所以選最早結束的永遠不吃虧。

【依開始時間排序行不行？】
    可以，但遇到重疊時要保留「結束較早」的那個（刪掉結束晚的），
    邏輯比較繞。依結束時間排序最直接。

【端點相接不算重疊】
    判斷用 s >= end（不是 s > end）。"""),
 ],
 "approaches": [
   ap("解法", "依結束時間排序的貪心", [
     ("c", S["p435"]),
   ], "O(n log n)", "O(1)", "", "不計排序", optimal=True),
 ],
 "edges": [
   "<strong>端點相接</strong>（[1,2]、[2,3]）→ 不算重疊。",
   "<strong>完全相同的區間</strong> → 只能留一個。",
   "<strong>一個區間包住很多小區間</strong> → 貪心會刪掉大的。",
 ],
 "follow": [
   ("h", "同一個貪心"),
   ("c", "第 452 題（用最少的箭射爆氣球）：本質上是「最多能選幾個互不重疊的區間」，只是端點相接也算重疊。"),
 ],
 "related": [
   "<strong>第 452 題 用最少數量的箭引爆氣球</strong>",
   "<strong>第 56 題 合併區間</strong>",
   "<strong>第 646 題 最長數對鏈</strong>",
 ],
 "check": [
   "為什麼要依結束時間排序？",
   "證明選最早結束的區間不會吃虧。",
   "判斷不重疊時為什麼用 ≥？",
 ],
})


# ==================== 436. Find Right Interval ====================
S["p436"] = '''class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        starts = sorted((s, i) for i, (s, _) in enumerate(intervals))   # (起點, 原索引)
        keys = [s for s, _ in starts]
        res = []
        for _, e in intervals:
            j = bisect.bisect_left(keys, e)          # ★ 第一個起點 >= e 的區間
            res.append(starts[j][1] if j < len(starts) else -1)
        return res'''

_p436 = S.load("p436")
for _ in range(2000):
    starts = random.sample(range(-10, 20), random.randrange(1, 8))
    iv = [[s, s + random.randint(0, 6)] for s in starts]
    want = []
    for s, e in iv:
        cand = [(iv[j][0], j) for j in range(len(iv)) if iv[j][0] >= e]
        want.append(min(cand)[1] if cand else -1)
    assert _p436.findRightInterval(iv) == want
print("P436 OK")

emit({
 "num": 436, "slug": "find-right-interval",
 "en": [
   "You are given an array of <code>intervals</code>, where <code>intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]</code> and each <code>start<sub>i</sub></code> is <strong>unique</strong>.",
   "The <strong>right interval</strong> for an interval <code>i</code> is an interval <code>j</code> such that <code>start<sub>j</sub> &gt;= end<sub>i</sub></code> and <code>start<sub>j</sub></code> is <strong>minimized</strong>. Note that <code>i</code> may equal <code>j</code>.",
   "Return <em>an array of <strong>right interval</strong> indices for each interval <code>i</code></em>. If no <strong>right interval</strong> exists for interval <code>i</code>, then put <code>-1</code> at index <code>i</code>.",
 ],
 "zh": [
   "給你一組區間 <code>intervals</code>，每個區間的起點都<strong>不相同</strong>。",
   "區間 <code>i</code> 的<strong>右側區間</strong>是滿足 <code>start<sub>j</sub> ≥ end<sub>i</sub></code> 的區間中，起點<strong>最小</strong>的那個（<code>j</code> 可以等於 <code>i</code>）。",
   "回傳每個區間的右側區間索引；不存在的話填 <code>-1</code>。",
 ],
 "examples": """範例 1
  輸入：intervals = [[1,2]]
  輸出：[-1]

範例 2
  輸入：intervals = [[3,4],[2,3],[1,2]]
  輸出：[-1,0,1]

範例 3
  輸入：intervals = [[1,4],[2,3],[3,4]]
  輸出：[-1,2,-1]""",
 "constraints": [
   "1 ≤ <code>intervals.length</code> ≤ 2 × 10⁴",
   "−10⁶ ≤ <code>start<sub>i</sub> ≤ end<sub>i</sub></code> ≤ 10⁶",
   "每個起點都不相同",
 ],
 "idea": [
   ("c", """【對每個區間 i：找第一個起點 >= end_i 的區間】
    把所有起點排序（記住原本的索引），
    對每個 end_i 二分搜尋 bisect_left(起點, end_i)。

【為什麼 i 可以等於 j？】
    start_i = end_i 的區間（長度 0），自己就是自己的右側區間。"""),
 ],
 "approaches": [
   ap("解法", "起點排序 + 二分", [
     ("c", S["p436"]),
   ], "O(n log n)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>沒有更右邊的區間</strong> → −1。",
   "<strong>起點等於終點</strong> → 自己可能是答案。",
 ],
 "follow": [
   ("h", "雙指標版本"),
   ("c", "把區間分別依起點、依終點排序，兩個指標同時往前走，也可以 O(n log n)（排序主導）完成，查詢部分 O(n)。"),
 ],
 "related": [
   "<strong>第 35 題 搜尋插入位置</strong>",
   "<strong>第 2070 題 每一個查詢的最大美麗值</strong>",
 ],
 "check": [
   "為什麼排序時要記住原本的索引？",
   "二分搜尋要找的是什麼？",
 ],
})


# ==================== 437. Path Sum III ====================
S["p437"] = '''class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        seen = collections.Counter({0: 1})      # 從根到「目前路徑上的祖先」的前綴和出現次數

        def dfs(node, prefix: int) -> int:
            if node is None:
                return 0
            prefix += node.val
            # ★ 以 node 結尾、和為 target 的路徑數 = 之前有幾個前綴和 = prefix - target
            count = seen[prefix - targetSum]
            seen[prefix] += 1
            count += dfs(node.left, prefix) + dfs(node.right, prefix)
            seen[prefix] -= 1                    # 回溯：離開這條路徑
            return count

        return dfs(root, 0)'''

S["p437_brute"] = '''class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def from_node(node, remain: int) -> int:      # 以 node 為起點往下的路徑數
            if node is None:
                return 0
            return ((node.val == remain)
                    + from_node(node.left, remain - node.val)
                    + from_node(node.right, remain - node.val))

        def total(node) -> int:                        # 每個節點都當一次起點
            if node is None:
                return 0
            return from_node(node, targetSum) + total(node.left) + total(node.right)

        return total(root)'''

_p437 = [S.load(x) for x in ("p437", "p437_brute")]
for vals, t, want in [([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1], 8, 3), ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22, 3)]:
    for sol in _p437:
        assert sol.pathSum(lv(vals), t) == want
for _ in range(1500):
    tr = rand_tree(random.randrange(0, 18), -3, 3)
    t = random.randint(-4, 4)
    assert _p437[0].pathSum(tr, t) == _p437[1].pathSum(tr, t)
print("P437 OK")

emit({
 "num": 437, "slug": "path-sum-iii",
 "en": [
   "Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <em>the number of paths where the sum of the values along the path equals</em> <code>targetSum</code>.",
   "The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).",
 ],
 "zh": [
   "給你二元樹的根節點 <code>root</code> 和整數 <code>targetSum</code>，回傳<strong>節點值總和等於 targetSum</strong> 的路徑數量。",
   "路徑不必從根開始、也不必在葉子結束，但必須<strong>往下走</strong>（只能從父節點走到子節點）。",
 ],
 "examples": """範例 1
  輸入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
  輸出：3
  說明：5→3、5→2→1、-3→11

範例 2
  輸入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
  輸出：3""",
 "constraints": [
   "節點數在 <code>[0, 1000]</code> 之間",
   "−10⁹ ≤ <code>Node.val</code> ≤ 10⁹",
   "−1000 ≤ <code>targetSum</code> ≤ 1000",
 ],
 "idea": [
   ("c", """【暴力：每個節點都當起點往下找】
    O(n · h)，最壞 O(n²)。

【前綴和 + 雜湊表（第 560 題搬到樹上）】
    一條從根往下的路徑可以看成一個陣列。
    prefix = 根到目前節點的總和
    路徑 (祖先 a 的下一個, ..., 目前節點) 的和 = prefix - prefix(a)
    要它等於 target <=> prefix(a) = prefix - target

    所以：在「目前這條從根往下的路徑」上，
    有幾個祖先的前綴和等於 prefix - target，
    就有幾條以目前節點結尾的合格路徑。

【回溯】
    雜湊表只能記錄「目前路徑上」的前綴和 ——
    離開一個節點（回到父節點）時，要把它的前綴和減掉，
    否則兄弟子樹會誤用到不在同一條路徑上的前綴和。

【初始 {0: 1}】
    代表「從根開始」的路徑（前面什麼都沒有，前綴和是 0）。"""),
 ],
 "approaches": [
   ap("解法一", "每個節點當起點", [
     ("c", S["p437_brute"]),
   ], "O(n · h)", "O(h)", "最壞 O(n²)", ""),

   ap("解法二", "前綴和 + 雜湊表 + 回溯", [
     ("c", S["p437"]),
   ], "O(n)", "O(h)", "", "雜湊表只存目前路徑", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、暴力", "O(n·h)", "O(h)"],
    ["二、前綴和", "O(n)", "O(h) ✔"]]),
 "edges": [
   "<strong>空樹</strong> → 0。",
   "<strong>負數節點</strong> → 前綴和可以重複出現，所以要計數（不能用集合）。",
   "<strong>路徑只有一個節點</strong> → 也算。",
 ],
 "follow": [
   ("h", "前綴和家族"),
   ("c", "第 560 題（陣列版）、第 1248 題（奇數個數）、第 930 題（二元子陣列）——「子陣列和 = target」⟹ 前綴和 + 雜湊表計數。"),
 ],
 "related": [
   "<strong>第 560 題 和為 K 的子陣列</strong>",
   "<strong>第 112 題 路徑總和</strong>",
   "<strong>第 113 題 路徑總和 II</strong>",
 ],
 "check": [
   "路徑和怎麼用前綴和表示？",
   "為什麼離開節點時要把它的前綴和從雜湊表減掉？",
   "雜湊表為什麼一開始要放 {0: 1}？",
 ],
})


# ==================== 438. Find All Anagrams in a String ====================
S["p438"] = '''class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        if k > len(s):
            return []
        need = [0] * 26
        window = [0] * 26
        for ch in p:
            need[ord(ch) - 97] += 1
        res = []
        for i, ch in enumerate(s):
            window[ord(ch) - 97] += 1            # 右邊進一個
            if i >= k:
                window[ord(s[i - k]) - 97] -= 1  # 左邊出一個（視窗固定長度 k）
            if i >= k - 1 and window == need:    # ★ 字母計數相同 = 異位詞
                res.append(i - k + 1)
        return res'''

S["p438_diff"] = '''class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        cnt = [0] * 26                   # cnt = 視窗計數 - p 的計數
        for ch in p:
            cnt[ord(ch) - 97] -= 1
        diff = sum(1 for c in cnt if c)  # 有幾個字母的計數不一致
        res = []

        def change(ch, d):
            nonlocal diff
            i = ord(ch) - 97
            if cnt[i] == 0:
                diff += 1
            cnt[i] += d
            if cnt[i] == 0:
                diff -= 1

        for i, ch in enumerate(s):
            change(ch, 1)
            if i >= k:
                change(s[i - k], -1)
            if i >= k - 1 and diff == 0:  # 每一步 O(1) 判斷
                res.append(i - k + 1)
        return res'''

_p438 = [S.load(x) for x in ("p438", "p438_diff")]
for s, p, want in [("cbaebabacd", "abc", [0, 6]), ("abab", "ab", [0, 1, 2]), ("a", "ab", [])]:
    for sol in _p438:
        assert sol.findAnagrams(s, p) == want
for _ in range(3000):
    s = "".join(random.choice("abc") for _ in range(random.randrange(1, 12)))
    p = "".join(random.choice("abc") for _ in range(random.randrange(1, 5)))
    want = [i for i in range(len(s) - len(p) + 1) if sorted(s[i:i + len(p)]) == sorted(p)]
    for sol in _p438:
        assert sol.findAnagrams(s, p) == want
print("P438 OK")

emit({
 "num": 438, "slug": "find-all-anagrams-in-a-string",
 "en": [
   "Given two strings <code>s</code> and <code>p</code>, return <em>an array of all the start indices of</em> <code>p</code><em>'s anagrams in</em> <code>s</code>. You may return the answer in <strong>any order</strong>.",
 ],
 "zh": [
   "給你兩個字串 <code>s</code> 和 <code>p</code>，找出 <code>s</code> 中所有是 <code>p</code> 的<strong>異位詞</strong>的子字串，回傳它們的起始索引。",
 ],
 "examples": """範例 1
  輸入：s = "cbaebabacd", p = "abc"
  輸出：[0,6]
  說明："cba"、"bac"

範例 2
  輸入：s = "abab", p = "ab"
  輸出：[0,1,2]""",
 "constraints": [
   "1 ≤ <code>s.length, p.length</code> ≤ 3 × 10⁴",
   "只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【固定長度的滑動視窗】
    異位詞長度一定等於 len(p) -> 視窗長度固定為 k。
    每次右邊進一個字元、左邊出一個字元，
    比較視窗的字母計數和 p 的計數。

【比較的成本】
    直接比較兩個 26 格陣列：每步 O(26)，總共 O(26n)。
    更快：維護「有幾種字母的計數不一致」（diff），
    每次只有兩個字母的計數改變 -> O(1) 更新 diff，
    diff == 0 就是異位詞。"""),
 ],
 "approaches": [
   ap("解法一", "滑動視窗 + 比較計數陣列", [
     ("c", S["p438"]),
   ], "O(26 · n)", "O(1)", "", "", optimal=True),

   ap("解法二", "滑動視窗 + 維護不一致的數量", [
     ("c", S["p438_diff"]),
   ], "O(n)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、比較陣列", "O(26n)", "最直觀 ✔"],
    ["二、維護 diff", "O(n)", "字母表大時更好"]]),
 "edges": [
   "<strong>p 比 s 長</strong> → 空陣列。",
   "<strong>重疊的答案</strong>（\"abab\"）→ 都要列出。",
 ],
 "follow": [
   ("h", "同一個視窗"),
   ("c", "第 567 題「字串的排列」：只問「有沒有」，找到一個就回傳 true。第 76 題「最小覆蓋子串」：視窗長度不固定，要找最短的。"),
 ],
 "related": [
   "<strong>第 567 題 字串的排列</strong>",
   "<strong>第 242 題 有效的字母異位詞</strong>",
   "<strong>第 76 題 最小覆蓋子串</strong>",
 ],
 "check": [
   "為什麼視窗長度是固定的？",
   "怎麼讓每一步的比較從 O(26) 降到 O(1)？",
 ],
})
