# -*- coding: utf-8 -*-
"""第 415、416、417、419、420、421 題。"""
import random
import itertools
from collections import deque
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(415)
_DQ = {"deque": deque}


# ==================== 415. Add Strings ====================
S["p415"] = '''class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        out = []
        while i >= 0 or j >= 0 or carry:        # ★ 最後的進位也要處理
            d = carry
            if i >= 0:
                d += ord(num1[i]) - 48          # 字元轉數字，不用 int()
                i -= 1
            if j >= 0:
                d += ord(num2[j]) - 48
                j -= 1
            out.append(chr(d % 10 + 48))
            carry = d // 10
        return "".join(reversed(out))'''

_p415 = S.load("p415")
for _ in range(5000):
    a, b = random.randint(0, 10 ** random.randint(0, 30)), random.randint(0, 10 ** random.randint(0, 30))
    assert _p415.addStrings(str(a), str(b)) == str(a + b)
assert _p415.addStrings("999", "1") == "1000" and _p415.addStrings("0", "0") == "0"
print("P415 OK")

emit({
 "num": 415, "slug": "add-strings",
 "en": [
   "Given two non-negative integers, <code>num1</code> and <code>num2</code> represented as string, return <em>the sum of</em> <code>num1</code> <em>and</em> <code>num2</code> <em>as a string</em>.",
   "You must solve the problem without using any built-in library for handling large integers (such as <code>BigInteger</code>). You must also not convert the inputs to integers directly.",
 ],
 "zh": [
   "給你兩個以字串表示的非負整數 <code>num1</code>、<code>num2</code>，回傳它們的和（字串）。",
   "不能使用大數函式庫，也不能直接把整個字串轉成整數。",
 ],
 "examples": """範例 1
  輸入：num1 = "11", num2 = "123"
  輸出："134"

範例 2
  輸入：num1 = "456", num2 = "77"
  輸出："533"

範例 3
  輸入：num1 = "0", num2 = "0"
  輸出："0\"""",
 "constraints": [
   "1 ≤ <code>num1.length, num2.length</code> ≤ 10⁴",
   "只包含數字，沒有前導零（除了 0 本身）",
 ],
 "idea": [
   ("c", """【直式加法】
    兩個指標從最低位（字串尾端）往前走，
    每一位：d = 兩個數字 + 進位
        寫下 d % 10，進位 = d // 10
    較短的那個走完了就當 0。

【最後的進位】
    "999" + "1"：三位都處理完還有進位 1 -> 要再寫一個 "1"。
    把 carry 放進迴圈條件就不會漏。

【字元轉數字】
    ord(ch) - ord('0')，或 ord(ch) - 48。"""),
 ],
 "approaches": [
   ap("解法", "雙指標直式加法", [
     ("c", S["p415"]),
   ], "O(max(m, n))", "O(max(m, n))", "", "輸出", optimal=True),
 ],
 "edges": [
   "<strong>長度不同</strong> → 短的那個補 0。",
   "<strong>最後有進位</strong>（999 + 1）→ 多一位。",
   "<strong>0 + 0</strong> → \"0\"。",
 ],
 "follow": [
   ("h", "大數運算家族"),
   ("c", "第 2 題（鏈結串列相加）、第 43 題（字串相乘）、第 67 題（二進位相加）、第 445 題（鏈結串列相加 II，高位在前）。"),
 ],
 "related": [
   "<strong>第 43 題 字串相乘</strong>",
   "<strong>第 67 題 二進位求和</strong>",
   "<strong>第 2 題 兩數相加</strong>",
 ],
 "check": [
   "迴圈條件為什麼要包含 carry？",
   "兩個字串長度不同時怎麼處理？",
 ],
})


# ==================== 416. Partition Equal Subset Sum ====================
S["p416"] = '''class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:                          # 總和是奇數，不可能平分
            return False
        target = total // 2
        dp = [True] + [False] * target         # dp[s]：能不能湊出和 s
        for x in nums:
            for s in range(target, x - 1, -1): # ★ 0/1 背包：容量由大到小，每個數只用一次
                if dp[s - x]:
                    dp[s] = True
            if dp[target]:
                return True
        return dp[target]'''

S["p416_bits"] = '''class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        reach = 1                              # 第 s 個位元是 1 <=> 能湊出 s
        for x in nums:
            reach |= reach << x                # 每個已知的和都可以再加上 x
        return reach >> (total // 2) & 1 == 1'''

_p416 = [S.load(x) for x in ("p416", "p416_bits")]
for nums, want in [([1, 5, 11, 5], True), ([1, 2, 3, 5], False), ([2, 2], True), ([1], False)]:
    for sol in _p416:
        assert sol.canPartition(nums) == want
for _ in range(2000):
    a = [random.randint(1, 12) for _ in range(random.randrange(1, 10))]
    want = sum(a) % 2 == 0 and any(sum(c) * 2 == sum(a) for r in range(len(a) + 1) for c in itertools.combinations(a, r))
    for sol in _p416:
        assert sol.canPartition(a) == want
print("P416 OK")

emit({
 "num": 416, "slug": "partition-equal-subset-sum",
 "en": [
   "Given an integer array <code>nums</code>, return <code>true</code> <em>if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or</em> <code>false</code> <em>otherwise</em>.",
 ],
 "zh": [
   "給你一個正整數陣列 <code>nums</code>，判斷能不能把它分成兩個子集，使兩個子集的總和相等。",
 ],
 "examples": """範例 1
  輸入：nums = [1,5,11,5]
  輸出：true
  說明：[1, 5, 5] 和 [11]。

範例 2
  輸入：nums = [1,2,3,5]
  輸出：false""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 200",
   "1 ≤ <code>nums[i]</code> ≤ 100",
 ],
 "idea": [
   ("c", """【轉換：能不能挑出一些數，和剛好是總和的一半？】
    總和是奇數 -> 直接 false。
    否則 target = total / 2，這就是 0/1 背包：
    「每個數用或不用，能不能湊出 target」。

【dp[s] = 能不能湊出 s】
    加入一個數 x：dp[s] = dp[s] or dp[s - x]

【容量要由大到小掃】
    由小到大的話，dp[s - x] 可能是「這一輪剛被 x 更新的」，
    等於 x 被用了兩次 ✘（那是完全背包）。
    由大到小，dp[s - x] 一定還是上一輪的值 ✔

【位元集合（bitset）】
    用一個大整數的第 s 位表示「能湊出 s」：
        reach |= reach << x
    一行完成所有 s 的更新，Python 的大整數運算很快。"""),
 ],
 "approaches": [
   ap("解法一", "0/1 背包 DP", [
     ("c", S["p416"]),
   ], "O(n · sum)", "O(sum)", "", "", optimal=True),

   ap("解法二", "位元集合", [
     ("c", S["p416_bits"]),
   ], "O(n · sum / w)", "O(sum / w)", "w = 機器字長，實際上非常快", ""),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、背包 DP", "O(n·sum)", "O(sum) ✔"],
    ["二、bitset", "O(n·sum/w)", "O(sum/w)"]]),
 "edges": [
   "<strong>總和是奇數</strong> → false。",
   "<strong>只有一個數</strong> → false。",
   "<strong>某個數大於 target</strong> → 那個數一定不能選（迴圈範圍自動略過）。",
 ],
 "follow": [
   ("h", "背包家族"),
   ("c", "第 494 題（目標和：+/− 號轉成子集和）、第 1049 題（最後一塊石頭的重量 II：盡量接近一半）、第 474 題（二維容量的 0/1 背包）。"),
 ],
 "related": [
   "<strong>第 494 題 目標和</strong>",
   "<strong>第 1049 題 最後一塊石頭的重量 II</strong>",
   "<strong>第 698 題 劃分為 k 個相等的子集</strong>",
 ],
 "check": [
   "這題怎麼轉換成背包問題？",
   "為什麼容量要由大到小掃？",
   "位元集合的 reach |= reach &lt;&lt; x 在做什麼？",
 ],
})


# ==================== 417. Pacific Atlantic Water Flow ====================
S["p417"] = '''class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def reach(starts) -> set:
            # ★ 反過來從海邊往內「逆流而上」：只能走到不比目前低的格子
            seen = set(starts)
            q = deque(starts)
            while q:
                i, j = q.popleft()
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if (0 <= x < m and 0 <= y < n and (x, y) not in seen
                            and heights[x][y] >= heights[i][j]):
                        seen.add((x, y))
                        q.append((x, y))
            return seen

        pacific = reach([(0, j) for j in range(n)] + [(i, 0) for i in range(m)])
        atlantic = reach([(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m)])
        return [list(p) for p in pacific & atlantic]     # 兩邊都到得了'''

_p417 = S.load("p417", extra=_DQ)


def _pa_ref(H):
    m, n = len(H), len(H[0])
    res = []
    for si in range(m):
        for sj in range(n):
            seen = {(si, sj)}
            st = [(si, sj)]
            pac = atl = False
            while st:
                i, j = st.pop()
                if i == 0 or j == 0:
                    pac = True
                if i == m - 1 or j == n - 1:
                    atl = True
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and (x, y) not in seen and H[x][y] <= H[i][j]:
                        seen.add((x, y))
                        st.append((x, y))
            if pac and atl:
                res.append([si, sj])
    return res


for _ in range(800):
    m, n = random.randrange(1, 6), random.randrange(1, 6)
    H = [[random.randint(0, 4) for _ in range(n)] for _ in range(m)]
    assert sorted(_p417.pacificAtlantic(H)) == sorted(_pa_ref(H)), H
print("P417 OK")

emit({
 "num": 417, "slug": "pacific-atlantic-water-flow",
 "en": [
   "There is an <code>m x n</code> rectangular island that borders both the <strong>Pacific Ocean</strong> and <strong>Atlantic Ocean</strong>. The <strong>Pacific Ocean</strong> touches the island's left and top edges, and the <strong>Atlantic Ocean</strong> touches the island's right and bottom edges.",
   "The island is partitioned into a grid of square cells. You are given an <code>m x n</code> integer matrix <code>heights</code> where <code>heights[r][c]</code> represents the <strong>height above sea level</strong> of the cell at coordinate <code>(r, c)</code>.",
   "The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is <strong>less than or equal to</strong> the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.",
   "Return <em>a <strong>2D list</strong> of grid coordinates</em> <code>result</code> <em>where</em> <code>result[i] = [r<sub>i</sub>, c<sub>i</sub>]</code> <em>denotes that rain water can flow from cell</em> <code>(r<sub>i</sub>, c<sub>i</sub>)</code> <em>to <strong>both</strong> the Pacific and Atlantic oceans</em>.",
 ],
 "zh": [
   "一座 <code>m x n</code> 的長方形島嶼，<strong>太平洋</strong>在左邊和上邊，<strong>大西洋</strong>在右邊和下邊。",
   "<code>heights[r][c]</code> 是每一格的海拔。雨水可以從一格流到上下左右<strong>高度小於或等於</strong>它的鄰格；靠海的格子可以直接流進海裡。",
   "回傳所有雨水能<strong>同時</strong>流到太平洋和大西洋的格子座標。",
 ],
 "examples": """範例 1
  輸入：heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
  輸出：[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

範例 2
  輸入：heights = [[1]]
  輸出：[[0,0]]""",
 "constraints": [
   "1 ≤ <code>m, n</code> ≤ 200",
   "0 ≤ <code>heights[r][c]</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【正著做：每一格都搜一次能不能流到兩個海】
    O((mn)²)，40000 格太慢。

【反著做：從海邊往內「逆流而上」】
    水往低處流 <=> 反過來，從海邊出發，只能走到「不比目前低」的格子。
    從太平洋岸（上邊、左邊）的所有格子一起 BFS -> 能流到太平洋的集合
    從大西洋岸（下邊、右邊）一起 BFS -> 能流到大西洋的集合
    兩個集合的交集就是答案。

    每一格在每次 BFS 中最多被拜訪一次 -> O(mn)。

【多源 BFS】
    把所有岸邊的格子當起點一起放進佇列，
    比「每個起點各跑一次」快得多。"""),
 ],
 "approaches": [
   ap("解法", "從兩個海岸分別多源 BFS，取交集", [
     ("c", S["p417"]),
   ], "O(mn)", "O(mn)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>1 × 1</strong> → 同時靠兩個海，答案就是它。",
   "<strong>右上角、左下角</strong> → 一定同時靠兩個海。",
   "<strong>高度相等</strong> → 可以流過去（≤）。",
 ],
 "follow": [
   ("h", "「反向搜尋」的思維"),
   ("c", "問「從哪些起點能到達目標」時，從目標反向搜尋往往更快：第 130 題（被圍繞的區域，從邊界反向找）、第 1020 題（飛地的數量）。"),
 ],
 "related": [
   "<strong>第 130 題 被圍繞的區域</strong>",
   "<strong>第 200 題 島嶼數量</strong>",
   "<strong>第 1020 題 飛地的數量</strong>",
 ],
 "check": [
   "為什麼要從海邊反向搜尋？",
   "反向時，可以往哪些格子走？",
   "什麼是多源 BFS？",
 ],
})


# ==================== 419. Battleships in a Board ====================
S["p419"] = '''class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                # ★ 只數每艘船的「頭」：左邊和上邊都不是 X
                if (c == "X" and (i == 0 or board[i - 1][j] != "X")
                        and (j == 0 or row[j - 1] != "X")):
                    count += 1
        return count'''

_p419 = S.load("p419")


def _rand_board():
    m, n = random.randrange(1, 7), random.randrange(1, 7)
    B = [["."] * n for _ in range(m)]
    ships = 0
    for _ in range(random.randrange(0, 8)):
        i, j = random.randrange(m), random.randrange(n)
        horiz = random.random() < 0.5
        L = random.randint(1, 3)
        cells = [(i, j + t) if horiz else (i + t, j) for t in range(L)]
        if any(not (0 <= x < m and 0 <= y < n) for x, y in cells):
            continue
        # 船與船之間必須隔開（四周不能有 X）
        bad = any(0 <= x + dx < m and 0 <= y + dy < n and B[x + dx][y + dy] == "X"
                  for x, y in cells for dx, dy in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)))
        if bad:
            continue
        for x, y in cells:
            B[x][y] = "X"
        ships += 1
    return B, ships


for _ in range(3000):
    B, ships = _rand_board()
    assert _p419.countBattleships(B) == ships
print("P419 OK")

emit({
 "num": 419, "slug": "battleships-in-a-board",
 "en": [
   "Given an <code>m x n</code> matrix <code>board</code> where each cell is a battleship <code>'X'</code> or empty <code>'.'</code>, return <em>the number of the <strong>battleships</strong> on</em> <code>board</code>.",
   "<strong>Battleships</strong> can only be placed horizontally or vertically on <code>board</code>. In other words, they can only be made of the shape <code>1 x k</code> (<code>1</code> row, <code>k</code> columns) or <code>k x 1</code> (<code>k</code> rows, <code>1</code> column), where <code>k</code> can be of any size. "
   "At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).",
   "<strong>Follow up:</strong> Could you do it in one-pass, using only <code>O(1)</code> extra memory and without modifying the values <code>board</code>?",
 ],
 "zh": [
   "給你一個 <code>m x n</code> 的棋盤，每格是戰艦 <code>'X'</code> 或空格 <code>'.'</code>，回傳戰艦的數量。",
   "戰艦只能橫放或直放（<code>1 x k</code> 或 <code>k x 1</code>），兩艘戰艦之間至少隔一格（不會相鄰）。",
   "<strong>進階：</strong>能只掃一遍、<code>O(1)</code> 額外空間、而且不修改棋盤嗎？",
 ],
 "examples": """範例 1
  輸入：board = [["X",".",".","X"],
                 [".",".",".","X"],
                 [".",".",".","X"]]
  輸出：2

範例 2
  輸入：board = [["."]]
  輸出：0""",
 "constraints": [
   "1 ≤ <code>m, n</code> ≤ 200",
   "<code>board[i][j]</code> 是 <code>'.'</code> 或 <code>'X'</code>",
 ],
 "idea": [
   ("c", """【一般做法：數連通區塊（第 200 題）】
    DFS / BFS，但要修改棋盤或用 visited -> 不符合進階要求。

【只數「船頭」】
    每艘船都是一條直線，有唯一的「最左上角」那一格：
        它的左邊不是 X，上邊也不是 X。
    其他格子至少有一個鄰居（左或上）是同一艘船的 X。
    所以：數滿足「是 X、左邊不是 X、上邊不是 X」的格子數 = 船數。

    因為題目保證船不相鄰，不會有「左邊的 X 屬於另一艘船」的情況。"""),
 ],
 "approaches": [
   ap("解法", "只數每艘船的頭", [
     ("c", S["p419"]),
   ], "O(mn)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>沒有船</strong> → 0。",
   "<strong>長度 1 的船</strong> → 自己就是頭。",
   "<strong>第一列、第一欄</strong> → 沒有上邊或左邊，視為不是 X。",
 ],
 "follow": [
   ("h", "如果船可以相鄰？"),
   ("c", "那就無法只看局部分辨，必須用 DFS／並查集數連通區塊（而且題目會變得不明確——相鄰的兩艘船看起來就像一艘 L 形的船）。"),
 ],
 "related": [
   "<strong>第 200 題 島嶼數量</strong>",
   "<strong>第 695 題 島嶼的最大面積</strong>",
 ],
 "check": [
   "船頭有什麼特徵？",
   "為什麼題目保證「船不相鄰」這件事很重要？",
 ],
})


# ==================== 420. Strong Password Checker ====================
S["p420"] = '''class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        missing = 3 - (any(c.islower() for c in password)
                       + any(c.isupper() for c in password)
                       + any(c.isdigit() for c in password))
        # 找出所有長度 >= 3 的連續相同段
        replace = 0            # 只用替換時，需要的替換次數
        ones = twos = 0        # 長度 % 3 == 0、== 1 的段數
        i = 2
        while i < n:
            if password[i] == password[i - 1] == password[i - 2]:
                length = 2
                while i < n and password[i] == password[i - 1]:
                    length += 1
                    i += 1
                replace += length // 3
                if length % 3 == 0:
                    ones += 1
                elif length % 3 == 1:
                    twos += 1
            else:
                i += 1

        if n < 6:                               # 太短：插入可以順便補類型、打斷連續
            return max(6 - n, missing)
        if n <= 20:                             # 長度合格：替換可以順便補類型
            return max(missing, replace)

        # 太長：必須刪 n - 20 個，★ 用刪除優先減少替換次數
        delete = n - 20
        replace -= min(delete, ones)                    # 長度 %3==0 的段：刪 1 個省 1 次替換
        replace -= min(max(delete - ones, 0), twos * 2) // 2   # %3==1：刪 2 個省 1 次
        replace -= max(delete - ones - 2 * twos, 0) // 3       # 其他：刪 3 個省 1 次
        return delete + max(missing, replace)'''

_p420 = S.load("p420")


def _spc_ref(pw):
    """0-1 BFS：從左到右處理原字元（保留 / 刪除 / 替換），也可以插入新字元。
    新字元一律視為「和任何字元都不同」的全新字元，只記錄它的類型。"""
    n = len(pw)

    def typ(c):
        return 1 if c.islower() else 2 if c.isupper() else 4 if c.isdigit() else 0

    # 狀態：(i, 長度, 最後一個字元（原字元或 None=新字元）, 連續長度, 已有類型)
    start = (0, 0, "#", 0, 0)
    dist = {start: 0}
    dq = deque([start])
    best = None
    while dq:
        st = dq.popleft()
        d = dist[st]
        i, L, last, run, mask = st
        if i == n and 6 <= L <= 20 and mask == 7:
            return d
        moves = []
        if i < n:
            c = pw[i]
            nrun = run + 1 if (last == c) else 1
            if nrun < 3 and L < 20:
                moves.append(((i + 1, L + 1, c, nrun, mask | typ(c)), 0))        # 保留
            moves.append(((i + 1, L, last, run, mask), 1))                      # 刪除
            if L < 20:
                for t in (1, 2, 4):
                    moves.append(((i + 1, L + 1, None, 1, mask | t), 1))        # 替換成新字元
        if L < 20:
            for t in (1, 2, 4):
                moves.append(((i, L + 1, None, 1, mask | t), 1))                # 插入新字元
        for ns, w in moves:
            nd = d + w
            if nd < dist.get(ns, 10 ** 9):
                dist[ns] = nd
                if w == 0:
                    dq.appendleft(ns)
                else:
                    dq.append(ns)
    return best


for pw, want in [("a", 5), ("aA1", 3), ("1337C0d3", 0), ("aaa111", 2), ("bbaaaaaaaaaaaaaaacccccc", 8),
                 ("aaaaaaaaaaaaaaaaaaaaa", 7), ("ABABABABABABABABABAB1", 2), ("...", 3)]:
    assert _p420.strongPasswordChecker(pw) == want, (pw, _p420.strongPasswordChecker(pw))
for _ in range(1500):
    L = random.choice([random.randint(0, 8), random.randint(16, 28)])
    pw = "".join(random.choice("aaaAA11.b") for _ in range(L))
    assert _p420.strongPasswordChecker(pw) == _spc_ref(pw), pw
print("P420 OK")

emit({
 "num": 420, "slug": "strong-password-checker",
 "en": [
   "A password is considered strong if the below conditions are all met:",
   ("ul", ["It has at least <code>6</code> characters and at most <code>20</code> characters.",
           "It contains at least <strong>one lowercase</strong> letter, at least <strong>one uppercase</strong> letter, and at least <strong>one digit</strong>.",
           "It does not contain three repeating characters in a row (i.e., <code>\"B<u><strong>aaa</strong></u>bb0\"</code> is weak, but <code>\"B<strong><u>aa</u></strong>b<u><strong>a</strong></u>0\"</code> is strong)."]),
   "Given a string <code>password</code>, return <em>the minimum number of steps required to make <code>password</code> strong. if <code>password</code> is already strong, return <code>0</code>.</em>",
   "In one step, you can:",
   ("ul", ["Insert one character to <code>password</code>,",
           "Delete one character from <code>password</code>, or",
           "Replace one character of <code>password</code> with another character."]),
 ],
 "zh": [
   "一個密碼要同時滿足以下條件才算「強」：",
   ("ul", ["長度在 <code>6</code> 到 <code>20</code> 之間。",
           "至少有一個<strong>小寫字母</strong>、一個<strong>大寫字母</strong>、一個<strong>數字</strong>。",
           "沒有<strong>連續三個相同</strong>的字元（例如 <code>\"Baaabb0\"</code> 不行）。"]),
   "每一步可以<strong>插入</strong>、<strong>刪除</strong>或<strong>替換</strong>一個字元。回傳讓密碼變強的最少步數。",
 ],
 "examples": """範例 1
  輸入：password = "a"
  輸出：5

範例 2
  輸入：password = "aA1"
  輸出：3

範例 3
  輸入：password = "1337C0d3"
  輸出：0""",
 "constraints": [
   "1 ≤ <code>password.length</code> ≤ 50",
   "<code>password</code> 由字母、數字、<code>'.'</code>、<code>'!'</code> 組成",
 ],
 "idea": [
   ("c", """【三個問題】
    missing：缺幾種字元類型（0~3）
    長度：太短或太長
    連續段：每一段長度 L >= 3 的連續相同字元

【情況一：太短（n < 6）】
    插入可以同時補長度、補類型、打斷連續段。
    答案 = max(6 - n, missing)
    （n < 6 時連續段最長 5，插入兩個就能打斷，不會超過 6 - n。）

【情況二：長度剛好（6 <= n <= 20）】
    替換最划算：換掉一個字元，可以同時打斷連續段、補一種類型。
    長度 L 的段需要 L // 3 次替換（每 3 個換中間那個）。
    答案 = max(missing, 替換次數總和)

【情況三：太長（n > 20）—— 最難】
    必須刪 n - 20 個字元。刪除也能縮短連續段，
    要把刪除用在「最能省下替換次數」的地方：
        L % 3 == 0 的段：刪 1 個就少 1 次替換（6 -> 5：2 次變 1 次）
        L % 3 == 1 的段：刪 2 個才少 1 次（7 -> 5）
        其他：每刪 3 個少 1 次
    依照這個優先順序分配刪除額度。
    答案 = 刪除數 + max(missing, 剩下的替換次數)"""),
   ("t", ["段長 L", "只替換", "刪幾個能少 1 次替換"],
    [["3", "1", "1（3→2）"],
     ["4", "1", "2（4→2）"],
     ["5", "1", "3（5→2）"],
     ["6", "2", "1（6→5）"],
     ["7", "2", "2（7→5）"]]),
 ],
 "approaches": [
   ap("解法", "分三種長度情況的貪心", [
     ("c", S["p420"]),
     ("c", """【驗證方式】
    這題的貪心很容易漏情況。本頁的程式碼和一個獨立的 0-1 BFS 暴力解比對：
    狀態 =（處理到第幾個字元、目前長度、最後一個字元、連續長度、已有的類型），
    每個原字元可以保留（成本 0）、刪除、替換，也可以在任何位置插入新字元（成本 1），
    找出滿足所有條件的最少成本。隨機 1500 組、長度 0–28 的密碼全部一致。"""),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>很短又全部相同</strong>（\"aaa\"）→ 3（插入 3 個就同時解決所有問題）。",
   "<strong>很長又全部相同</strong> → 刪除優先用在 %3 == 0 的段。",
   "<strong>沒有字母也沒有數字</strong>（\"...\"）→ missing = 3。",
 ],
 "follow": [
   ("h", "為什麼這題是出名的難題？"),
   ("c", "三個條件互相影響：插入、刪除、替換都可能同時解決多個問題。關鍵在於分清楚「每種長度情況下，哪個操作最划算」，以及太長時刪除的分配順序。"),
 ],
 "related": [
   "<strong>第 1957 題 刪除字元使字串變好</strong>",
   "<strong>第 2299 題 強密碼檢驗器 II</strong> —— 只需判斷",
 ],
 "check": [
   "長度 6 到 20 時，為什麼替換最划算？",
   "長度 L 的連續段需要幾次替換？",
   "太長時，刪除為什麼要優先用在 L % 3 == 0 的段？",
 ],
})


# ==================== 421. Maximum XOR of Two Numbers in an Array ====================
S["p421"] = '''class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0
        for b in range(max(nums).bit_length() - 1, -1, -1):   # ★ 從最高位開始決定答案
            mask |= 1 << b
            prefixes = {x & mask for x in nums}                 # 所有數的前綴（高位部分）
            want = ans | (1 << b)                               # 希望這一位是 1
            # a ^ b = want  <=>  a ^ want = b：看有沒有兩個前綴能湊出 want
            if any(p ^ want in prefixes for p in prefixes):
                ans = want
        return ans'''

S["p421_trie"] = '''class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        H = max(nums).bit_length()
        trie = {}
        for x in nums:                                  # 建二進位字典樹（高位在上）
            node = trie
            for b in range(H - 1, -1, -1):
                node = node.setdefault(x >> b & 1, {})
        best = 0
        for x in nums:
            node, cur = trie, 0
            for b in range(H - 1, -1, -1):
                bit = x >> b & 1
                if 1 - bit in node:                     # 盡量走相反的位元，讓 XOR 這一位是 1
                    cur |= 1 << b
                    node = node[1 - bit]
                else:
                    node = node[bit]
            best = max(best, cur)
        return best'''

_p421 = [S.load(x) for x in ("p421", "p421_trie")]
for nums, want in [([3, 10, 5, 25, 2, 8], 28), ([14, 70, 53, 83, 49, 91, 36, 80, 92, 51, 66, 70], 127), ([0], 0)]:
    for sol in _p421:
        assert sol.findMaximumXOR(nums) == want
for _ in range(2000):
    a = [random.randint(0, 200) for _ in range(random.randrange(1, 10))]
    want = max(x ^ y for x in a for y in a)
    for sol in _p421:
        assert sol.findMaximumXOR(a) == want
print("P421 OK")

emit({
 "num": 421, "slug": "maximum-xor-of-two-numbers-in-an-array",
 "en": [
   "Given an integer array <code>nums</code>, return <em>the maximum result of</em> <code>nums[i] XOR nums[j]</code>, where <code>0 &lt;= i &lt;= j &lt; n</code>.",
 ],
 "zh": [
   "給你一個非負整數陣列 <code>nums</code>，回傳 <code>nums[i] XOR nums[j]</code> 的最大值（<code>0 ≤ i ≤ j &lt; n</code>）。",
 ],
 "examples": """範例 1
  輸入：nums = [3,10,5,25,2,8]
  輸出：28
  說明：5 XOR 25 = 28。

範例 2
  輸入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
  輸出：127""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 2 × 10⁵",
   "0 ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【XOR 的大小由最高位決定】
    只要能讓較高的位元是 1，後面的位元不管怎樣都比較大。
    -> 從最高位開始，貪心地讓每一位盡量是 1。

【方法一：二進位字典樹（Trie）】
    把每個數的位元（從高到低）插入 Trie。
    對每個 x，從根往下走，每一層盡量走「和 x 這一位相反」的分支
    （相反才能讓 XOR 的這一位是 1）。
    O(n · 31)。

【方法二：逐位確定答案 + 雜湊集合】
    假設答案的高位已經確定為 ans。
    試試看下一位能不能是 1：want = ans | (1 << b)
    把所有數只保留高位（x & mask）放進集合，
    問：有沒有兩個前綴 p、q 使 p ^ q = want？
    <=> 對某個 p，p ^ want 也在集合裡（XOR 的性質：a ^ b = c <=> a ^ c = b）"""),
 ],
 "approaches": [
   ap("解法一", "二進位字典樹", [
     ("c", S["p421_trie"]),
   ], "O(n · L)", "O(n · L)", "L = 位元數", ""),

   ap("解法二", "逐位貪心 + 雜湊集合", [
     ("c", S["p421"]),
   ], "O(n · L)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["暴力", "O(n²)", "O(1)"],
    ["一、Trie", "O(n·L)", "O(n·L)"],
    ["二、逐位 + 集合", "O(n·L)", "O(n) ✔"]]),
 "edges": [
   "<strong>只有一個數</strong> → 0（自己 XOR 自己）。",
   "<strong>全部是 0</strong> → 0。",
   "<strong>位元數</strong> → 只需要看到最大值的最高位。",
 ],
 "follow": [
   ("h", "XOR Trie 的延伸"),
   ("c", "第 1707 題（和陣列中元素的最大異或值，帶上限的離線查詢）、第 1938 題（查詢最大基因差，DFS + 可刪除的 Trie）。"),
 ],
 "related": [
   "<strong>第 1707 題 與陣列中元素的最大異或值</strong>",
   "<strong>第 208 題 實作 Trie</strong>",
   "<strong>第 1803 題 統計異或值在範圍內的數對有多少</strong>",
 ],
 "check": [
   "為什麼可以從最高位開始貪心？",
   "在 Trie 中為什麼要走相反的分支？",
   "a ^ b = c 和 a ^ c = b 為什麼等價？",
 ],
})
