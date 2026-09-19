# -*- coding: utf-8 -*-
"""第 35–38 題。"""
import random, collections, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(35)

# ==================== 35. Search Insert Position ====================
S["p35"] = '''class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)        # hi = len，答案範圍是 [0, n]

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1         # mid 確定不是答案
            else:
                hi = mid             # mid 可能就是答案，不能排除

        return lo                    # lo == hi，就是答案'''

S["p35_classic"] = '''class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        # 迴圈結束時 lo == hi + 1，而 lo 剛好就是插入位置
        return lo'''

_p35 = [S.load(k) for k in ("p35", "p35_classic")]
import bisect as _bis
for c, t in [([1, 3, 5, 6], 5), ([1, 3, 5, 6], 2), ([1, 3, 5, 6], 7),
             ([1, 3, 5, 6], 0), ([], 1), ([1], 1)]:
    e = _bis.bisect_left(c, t)
    for sol in _p35:
        assert sol.searchInsert(list(c), t) == e, ("P35", c, t, sol)
for _ in range(5000):
    c = sorted(set(random.randint(-8, 8) for _ in range(random.randint(0, 10))))
    t = random.randint(-9, 9)
    e = _bis.bisect_left(c, t)
    for sol in _p35:
        assert sol.searchInsert(list(c), t) == e, ("P35", c, t, sol)
print("P35 solutions OK")

emit({
 "num": 35, "slug": "search-insert-position",
 "en": [
   "Given a sorted array of <strong>distinct</strong> integers and a target value, return the "
   "index if the target is found. If not, return the index where it would be if it were "
   "inserted in order.",
   "You must write an algorithm with <code>O(log n)</code> runtime complexity.",
 ],
 "zh": [
   "給你一個<strong>元素互不相同</strong>的升序陣列和一個目標值 <code>target</code>。"
   "如果 <code>target</code> 存在就回傳它的索引；"
   "不存在的話，回傳<strong>它應該被插入的位置</strong>（插入後陣列仍然有序）。",
   "演算法必須是 <code>O(log n)</code>。",
 ],
 "pre": [
   ("note", "這題就是 lower_bound，沒別的", [
     ("c", """「第一個 >= target 的位置」同時回答了兩件事：

  target 存在  ->  那個位置就是 target 的索引
  target 不存在 ->  那個位置就是該插進去的地方

nums = [1, 3, 5, 6]

  target=5 -> 第一個 >= 5 的是索引 2  ->  回 2（存在）
  target=2 -> 第一個 >= 2 的是索引 1  ->  回 1（插在 1 和 3 之間）
  target=7 -> 沒有 >= 7 的           ->  回 4（插在最後）
  target=0 -> 第一個 >= 0 的是索引 0  ->  回 0（插在最前）

所以答案的範圍是 [0, n]，一共 n+1 種可能。
這就是為什麼 hi 要初始化成 n 而不是 n-1。"""),
     "<strong>這題是整個二分搜尋家族的入口。</strong>"
     "把 <code>lower_bound</code> 的骨架在這裡寫熟，"
     "第 34、69、74、278、875、1011 題都會受益。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,3,5,6], target = 5
  輸出：2

範例 2
  輸入：nums = [1,3,5,6], target = 2
  輸出：1

範例 3
  輸入：nums = [1,3,5,6], target = 7
  輸出：4""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁴",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
   "<code>nums</code> 是<strong>嚴格遞增</strong>的（沒有重複值）",
   "−10⁴ ≤ <code>target</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>沒有重複值</strong>，所以 lower_bound 和 upper_bound 的差別在這題看不出來。"
       "（有重複值時就是第 34 題。）",
       "<strong>要求 O(log n)</strong> —— 排除線性掃描（雖然 n = 10⁴ 線性也會過，"
       "但這題的重點就是二分）。",
       "<strong>答案可能是 <code>n</code></strong>（插在最後面）。"
       "這是最常被漏掉的邊界。",
     ]),
   ]),
 ],
 "idea": [
   "兩種骨架都能寫，但它們的「結束狀態」意義不同，值得一起看清楚。",
 ],
 "approaches": [
   ap("解法一", "lower_bound 骨架（推薦）", [
     ("c", S["p35"]),
     ("h", "三個要點（和第 34 題一模一樣）"),
     ("c", """1. hi = len(nums)     答案範圍是 [0, n]，n 表示「插在最後」
2. while lo < hi      收斂到一點，不是「找到就 return」
3. hi = mid           mid 可能是答案，不能寫 mid - 1

為什麼不會死循環？
    mid = (lo + hi) // 2 向下取整，所以當 lo < hi 時一定有 mid < hi。
    因此 hi = mid 一定讓 hi 嚴格變小。
    而 lo = mid + 1 一定讓 lo 嚴格變大。
    區間每輪都真的縮小 -> 保證終止。

不變量（loop invariant）：
    答案永遠落在 [lo, hi] 裡面。
    - nums[mid] < target  -> mid 及其左邊都不可能是答案 -> lo = mid + 1 ✔
    - nums[mid] >= target -> mid 可能是答案，右邊都不可能更好 -> hi = mid ✔
    結束時 lo == hi，區間只剩一點，那就是答案。"""),
     "<strong>追一遍 <code>nums = [1,3,5,6], target = 2</code></strong>：",
     ("c", """lo=0, hi=4
mid=2: nums[2]=5 >= 2  -> hi=2
lo=0, hi=2
mid=1: nums[1]=3 >= 2  -> hi=1
lo=0, hi=1
mid=0: nums[0]=1 <  2  -> lo=1
lo=1, hi=1  -> 結束，回傳 1 ✔"""),
   ], "O(log n)", "O(1)", "每輪砍一半", "只用兩個下標", optimal=True),

   ap("解法二", "經典骨架（找到就 return）", [
     "如果你比較習慣「<code>while lo &lt;= hi</code>、找到就 return」的寫法，"
     "這題也能用 —— 關鍵是<strong>知道迴圈結束時 <code>lo</code> 是什麼</strong>。",
     ("c", S["p35_classic"]),
     ("h", "為什麼結束時 <code>lo</code> 就是插入位置？"),
     ("c", """迴圈結束的條件是 lo > hi，而且一定是 lo == hi + 1。

此時的不變量：
    所有 index < lo 的元素都 < target
    所有 index > hi 的元素都 > target
    （而 lo == hi + 1，所以這兩個範圍剛好覆蓋全部）

所以 lo 就是「第一個 >= target 的位置」= 插入位置。

追一遍 nums = [1,3,5,6], target = 2：
    lo=0, hi=3, mid=1: nums[1]=3 > 2 -> hi=0
    lo=0, hi=0, mid=0: nums[0]=1 < 2 -> lo=1
    lo=1 > hi=0 -> 結束，回傳 lo=1 ✔

追一遍 target = 7：
    lo=0, hi=3, mid=1: 3 < 7 -> lo=2
    lo=2, hi=3, mid=2: 5 < 7 -> lo=3
    lo=3, hi=3, mid=3: 6 < 7 -> lo=4
    lo=4 > hi=3 -> 回傳 4 ✔"""),
     "<strong>「結束時 <code>lo</code> 是插入位置」這個性質很有用</strong>，"
     "很多人寫二分只記得「找到就 return」，卻不知道找不到時 <code>lo</code> 和 <code>hi</code> "
     "落在哪裡。這題剛好逼你搞清楚。",
     "<strong>兩種骨架的取捨</strong>：解法一比較短、意圖更明確（「我要找邊界」）；"
     "解法二在「剛好命中」時可以提早 return（常數上稍快）。"
     "實務上建議<strong>只記一種並記熟</strong> —— 混用是所有二分 bug 的來源。",
   ], "O(log n)", "O(1)", "每輪砍一半", "只用兩個下標"),
 ],
 "compare": (["骨架", "迴圈條件", "結束狀態", "適合的問題"],
   [["lower_bound", "<code>lo &lt; hi</code>", "<code>lo == hi</code>，就是答案", "找邊界、找插入點"],
    ["經典", "<code>lo &lt;= hi</code>", "<code>lo == hi + 1</code>", "找特定元素"]]),
 "edges": [
   "<strong>target 比全部都大</strong>：<code>([1,3,5,6], 7)</code> → 4。"
   "<strong><code>hi</code> 寫成 <code>len-1</code> 會回傳 3，錯。</strong>",
   "<strong>target 比全部都小</strong>：<code>([1,3,5,6], 0)</code> → 0。",
   "<strong>剛好命中</strong>：<code>([1,3,5,6], 5)</code> → 2。",
   "<strong>插在中間</strong>：<code>([1,3,5,6], 2)</code> → 1。",
   "<strong>單一元素</strong>：<code>([1], 1)</code> → 0；<code>([1], 0)</code> → 0；<code>([1], 2)</code> → 1。",
   "<strong>空陣列</strong>：<code>([], 1)</code> → 0。題目保證不會，但 lower_bound 自然就對。",
 ],
 "follow": [
   ("h", "追問一：如果有重複值呢？"),
   "<code>lower_bound</code> 會回傳「第一個等於 target 的位置」，"
   "也就是插在<strong>所有相同元素的最左邊</strong>。"
   "如果要插在最右邊，就用 <code>upper_bound</code>（把 <code>&lt;</code> 改成 <code>&lt;=</code>）。"
   "一個字元的差別。",
   ("h", "追問二：這個骨架還能用在哪？"),
   "只要能定義一個<strong>單調的述詞</strong> <code>P(i)</code>"
   "（i 小的時候是 False，超過某一點之後一直是 True），就能用同一個骨架找那個交界點：",
   ("c", """本題：       P(i) = nums[i] >= target
第 278 題：  P(v) = isBadVersion(v)
第 875 題：  P(speed) = 「這個速度吃得完嗎」
第 1011 題： P(cap) = 「這個載重量運得完嗎」
第 410 題：  P(x) = 「最大子陣列和 <= x 時分得出 k 段嗎」

這叫「二分答案」：不是在陣列上二分，而是在「答案的值域」上二分。
一旦認出這個模式，一大票看起來很難的最佳化問題都會變成
「寫一個 check 函式 + 套這個骨架」。"""),
   ("h", "追問三：<code>mid = (lo + hi) // 2</code> 有什麼隱患？"),
   "在 Python 裡沒有。但在 C/Java 裡，"
   "<code>lo + hi</code> <strong>可能溢位</strong>（兩個都接近 INT_MAX 時）。"
   "這是 Java 的 <code>Arrays.binarySearch</code> 存在了九年的著名 bug"
   "（2006 年由 Joshua Bloch 公開）。"
   "安全的寫法是 <code>mid = lo + (hi - lo) // 2</code>。"
   "<strong>這是二分搜尋最有名的歷史教訓，面試時提到會加分。</strong>",
 ],
 "related": [
   "<strong>第 34 題 Find First and Last Position</strong> —— 有重複值的版本",
   "<strong>第 278 題 First Bad Version</strong> —— 最單純的 partition point",
   "<strong>第 875／1011／410 題</strong> —— 二分答案",
   "<strong>第 704 題 Binary Search</strong> —— 最基本的版本",
 ],
 "check": [
   "為什麼 <code>hi</code> 要初始化成 <code>len(nums)</code>？哪一筆測資會抓出 <code>len-1</code> 的錯？",
   "解法二的迴圈結束時，<code>lo</code> 和 <code>hi</code> 的關係是什麼？為什麼 <code>lo</code> 就是答案？",
   "為什麼 <code>hi = mid</code>（不減一）不會造成死循環？",
   "<code>mid = (lo + hi) // 2</code> 在 Java 裡有什麼問題？該怎麼寫？",
 ],
})
print("P35 written")

# ==================== 36. Valid Sudoku ====================
S["p36_three"] = '''class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]      # 3x3 宮格，編號 0..8

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue

                b = (r // 3) * 3 + c // 3      # 宮格編號

                if v in rows[r] or v in cols[c] or v in boxes[b]:
                    return False

                rows[r].add(v)
                cols[c].add(v)
                boxes[b].add(v)

        return True'''

S["p36_oneset"] = '''class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue

                # 把三個約束編碼成三個「不可能撞在一起」的字串
                keys = ((v, "row", r),
                        (v, "col", c),
                        (v, "box", r // 3, c // 3))

                for k in keys:
                    if k in seen:
                        return False
                    seen.add(k)

        return True'''

S["p36_bitmask"] = '''class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 每一列/行/宮用一個 9 位元的整數記錄「哪些數字用過了」
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    continue

                bit = 1 << (int(v) - 1)        # '1' -> 第 0 位，'9' -> 第 8 位
                b = (r // 3) * 3 + c // 3

                if rows[r] & bit or cols[c] & bit or boxes[b] & bit:
                    return False

                rows[r] |= bit
                cols[c] |= bit
                boxes[b] |= bit

        return True'''

_p36 = [S.load(k) for k in ("p36_three", "p36_oneset", "p36_bitmask")]
_B1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
       [".", "9", "8", ".", ".", ".", ".", "6", "."],
       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
       [".", "6", ".", ".", ".", ".", "2", "8", "."],
       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
_B2 = [r[:] for r in _B1]
_B2[0][0] = "8"           # 和左上宮格裡的 8 衝突


def _p36_ref(board):
    for r in range(9):
        vals = [board[r][c] for c in range(9) if board[r][c] != "."]
        if len(vals) != len(set(vals)):
            return False
    for c in range(9):
        vals = [board[r][c] for r in range(9) if board[r][c] != "."]
        if len(vals) != len(set(vals)):
            return False
    for br in range(3):
        for bc in range(3):
            vals = [board[br * 3 + i][bc * 3 + j]
                    for i in range(3) for j in range(3)
                    if board[br * 3 + i][bc * 3 + j] != "."]
            if len(vals) != len(set(vals)):
                return False
    return True


for b in (_B1, _B2):
    e = _p36_ref(b)
    for sol in _p36:
        assert sol.isValidSudoku([r[:] for r in b]) is e, ("P36", sol, e)
assert _p36[0].isValidSudoku([r[:] for r in _B1]) is True
assert _p36[0].isValidSudoku([r[:] for r in _B2]) is False
for _ in range(2000):
    b = [["." for _ in range(9)] for _ in range(9)]
    for _ in range(random.randint(0, 20)):
        b[random.randrange(9)][random.randrange(9)] = str(random.randint(1, 9))
    e = _p36_ref(b)
    for sol in _p36:
        assert sol.isValidSudoku([r[:] for r in b]) is e, ("P36", b, sol, e)
print("P36 solutions OK")

_P36_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">宮格編號 = (r // 3) * 3 + c // 3</text>
            <g>
              <rect x="150" y="40" width="240" height="240" fill="none" stroke="var(--text-muted)" stroke-width="2"/>
              <line x1="230" y1="40" x2="230" y2="280" stroke="var(--text-muted)" stroke-width="2"/>
              <line x1="310" y1="40" x2="310" y2="280" stroke="var(--text-muted)" stroke-width="2"/>
              <line x1="150" y1="120" x2="390" y2="120" stroke="var(--text-muted)" stroke-width="2"/>
              <line x1="150" y1="200" x2="390" y2="200" stroke="var(--text-muted)" stroke-width="2"/>
            </g>
            <g font-size="26" text-anchor="middle" fill="var(--accent)">
              <text x="190" y="90">0</text><text x="270" y="90">1</text><text x="350" y="90">2</text>
              <text x="190" y="170">3</text><text x="270" y="170">4</text><text x="350" y="170">5</text>
              <text x="190" y="250">6</text><text x="270" y="250">7</text><text x="350" y="250">8</text>
            </g>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="190" y="106">r//3=0, c//3=0</text>
              <text x="350" y="266">r//3=2, c//3=2</text>
            </g>
            <text x="420" y="80" fill="var(--gold)" font-size="12">例：r=4, c=7</text>
            <text x="420" y="102" fill="var(--text-muted)" font-size="12">r // 3 = 1</text>
            <text x="420" y="122" fill="var(--text-muted)" font-size="12">c // 3 = 2</text>
            <text x="420" y="142" fill="var(--text-muted)" font-size="12">1 × 3 + 2 = 5</text>
            <text x="420" y="166" fill="var(--accent)" font-size="12">→ 宮格 5 ✔</text>
            <text x="20" y="310" fill="var(--gold)" font-size="12">整除 3 把 0~8 壓成 0~2，乘 3 再加就得到 0~8 的唯一編號 —— 就是二維展平成一維。</text>'''

emit({
 "num": 36, "slug": "valid-sudoku",
 "en": [
   "Determine if a <code>9 x 9</code> Sudoku board is <strong>valid</strong>. "
   "Only the filled cells need to be validated according to the following rules:",
   "(1) Each row must contain the digits <code>1-9</code> without repetition. "
   "(2) Each column must contain the digits <code>1-9</code> without repetition. "
   "(3) Each of the nine <code>3 x 3</code> sub-boxes must contain the digits <code>1-9</code> "
   "without repetition.",
   "<strong>Note:</strong> A Sudoku board (partially filled) could be valid but is not "
   "necessarily solvable.",
 ],
 "zh": [
   "判斷一個 <code>9 × 9</code> 的數獨盤面是否<strong>有效</strong>。"
   "<strong>只需要檢查已經填上的格子</strong>，規則如下：",
   "（1）每一<strong>列</strong>的數字 1–9 不能重複；"
   "（2）每一<strong>行</strong>的數字 1–9 不能重複；"
   "（3）每個 <code>3 × 3</code> <strong>宮格</strong>裡的數字 1–9 不能重複。",
   "<strong>注意：</strong>一個部分填寫的盤面可以是「有效」的，但不一定<strong>有解</strong>。",
 ],
 "pre": [
   ("note", "「有效」不等於「有解」", [
     ("c", """這題只問：目前填的這些數字，有沒有違反三條規則？

它「不」問：這個盤面能不能填完？

例子：
    第一列填了 1 2 3 4 5 6 7 8，第九格是空的
    第一行填了 1（在 (0,0)）
    ...

    可能出現「某個空格所有數字都不能填」的死局，
    但只要目前填的沒有重複，這題就算「有效」。

「能不能填完」是第 37 題（Sudoku Solver），難度高很多。

這個區分很重要：本題是 O(81) 的檢查，第 37 題是回溯搜尋。"""),
   ]),
 ],
 "examples": """範例 1（有效）
  5 3 . | . 7 . | . . .
  6 . . | 1 9 5 | . . .
  . 9 8 | . . . | . 6 .
  ------+-------+------
  8 . . | . 6 . | . . 3
  4 . . | 8 . 3 | . . 1
  7 . . | . 2 . | . . 6
  ------+-------+------
  . 6 . | . . . | 2 8 .
  . . . | 4 1 9 | . . 5
  . . . | . 8 . | . 7 9
  輸出：true

範例 2（無效）
  把左上角的 5 改成 8
  -> 左上 3x3 宮格裡有兩個 8（(0,0) 和 (3,0) 不同宮…
     實際衝突在 (0,0)=8 與同一宮的另一個 8）
  輸出：false""",
 "constraints": [
   "<code>board.length == 9</code>，<code>board[i].length == 9</code>",
   "<code>board[i][j]</code> 是 <code>'1'</code>–<code>'9'</code> 的<strong>字元</strong>，或 <code>'.'</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>盤面固定是 9×9</strong>，所以所有解法都是 O(81) = O(1)。"
       "<strong>這題不考效率，考的是「你怎麼組織這三個約束」。</strong>",
       "<strong>格子裡是「字元」不是「整數」</strong>。"
       "<code>board[r][c]</code> 是 <code>'5'</code> 而不是 <code>5</code>。"
       "用位元法時要記得 <code>int(v)</code>。",
       "<strong>空格是 <code>'.'</code></strong>，要跳過，不能當成一個值。",
     ]),
   ]),
 ],
 "idea": [
   "三條規則的形狀不一樣（列、行、宮），但檢查的邏輯完全一樣：<strong>有沒有重複</strong>。"
   "所以關鍵是<strong>把「這一格屬於哪一列 / 哪一行 / 哪一宮」統一成三個索引</strong>。",
   ("fig", _P36_FIG, "0 0 640 320"),
 ],
 "approaches": [
   ap("解法一", "三組集合，一次掃完（最推薦）", [
     ("c", S["p36_three"]),
     ("h", "宮格編號公式 <code>(r // 3) * 3 + c // 3</code>"),
     ("c", """r // 3 把列號 0..8 壓成宮列 0..2
c // 3 把行號 0..8 壓成宮行 0..2

然後用「二維展平成一維」的標準公式：
    index = 宮列 * 每列的宮數 + 宮行
          = (r // 3) * 3 + (c // 3)

驗算：
    (0,0) -> 0*3 + 0 = 0   左上
    (0,8) -> 0*3 + 2 = 2   右上
    (4,4) -> 1*3 + 1 = 4   正中
    (8,8) -> 2*3 + 2 = 8   右下  ✔

這個「整除壓縮 + 展平」的技巧在所有網格分塊的題目都會用到。
另一個等價寫法是用 tuple (r//3, c//3) 當 key，
不用算公式，但要用 dict 而不是 list。"""),
     "<strong>只掃一遍就同時檢查三條規則</strong>，因為每一格同時屬於一列、一行、一宮，"
     "三個都可以在看到它的當下就更新。",
     "<strong>為什麼用 <code>set</code> 而不是先收集再比長度？</strong>"
     "因為 <code>set</code> 可以<strong>提早退出</strong> —— 一發現重複立刻 return False，"
     "不用把整個盤面掃完。",
   ], "O(81) = O(1)", "O(81) = O(1)", "每格處理一次", "27 個集合，合計最多 81 個元素", optimal=True),

   ap("解法二", "一個集合，把約束編碼進 key", [
     "另一種組織方式：<strong>只用一個集合</strong>，"
     "但把「哪一種約束」也編進 key 裡，讓三種約束不會互相撞到。",
     ("c", S["p36_oneset"]),
     ("c", """(v, "row", r)       表示「第 r 列有 v」
(v, "col", c)       表示「第 c 行有 v」
(v, "box", i, j)    表示「第 (i,j) 宮有 v」

這三種 tuple 的形狀不同、內容也不同，
所以絕不可能互相碰撞。

很多題解會寫成字串：
    f"{v} in row {r}"
    f"{v} in col {c}"
    f"{v} in box {r//3}-{c//3}"

效果一樣，但 tuple 比字串快（不用格式化），
而且不會有「分隔符號選錯導致碰撞」的風險。
例如用 f"{v}-{r}" 當 row key、f"{r}-{v}" 當 col key，
在 v == r 時就會撞在一起。"""),
     "<strong>優點</strong>：概念上最統一 —— 「所有約束都是『這個東西不能出現兩次』」。"
     "<strong>缺點</strong>：key 比較大，常數稍慢，而且要小心不要設計出會碰撞的編碼。",
     "這個「把多個維度編碼進一個 key」的技巧在<strong>約束檢查</strong>類的問題裡很常見"
     "（例如 N 皇后的行／對角線衝突檢查）。",
   ], "O(81) = O(1)", "O(243) = O(1)", "每格產生三個 key", "一個集合，最多 243 個 key"),

   ap("解法三", "位元遮罩（最省記憶體）", [
     "9 個數字剛好可以用一個 9 位元的整數表示「哪些用過了」。",
     ("c", S["p36_bitmask"]),
     ("c", """bit = 1 << (int(v) - 1)

    '1' -> 1 << 0 = 0b000000001
    '5' -> 1 << 4 = 0b000010000
    '9' -> 1 << 8 = 0b100000000

檢查：rows[r] & bit    非 0 表示這一列已經有 v 了
標記：rows[r] |= bit   把那一位設成 1

例：第 0 列填了 5, 3, 7
    rows[0] = 0b001010100
                 ^  ^ ^
                 7  5 3   （第 6、4、2 位）"""),
     "<strong>27 個整數取代 27 個集合</strong>，記憶體從幾 KB 降到 216 位元組。"
     "而且位元運算比雜湊快得多。",
     "在這題（固定 9×9）差別可以忽略，"
     "但<strong>第 37 題（解數獨）會做上百萬次這種檢查</strong>，"
     "位元遮罩帶來的加速是實質的 —— <strong>所以這個版本值得先在這裡練熟。</strong>",
     ("h", "常用的位元技巧"),
     ("c", """檢查第 k 位：      mask & (1 << k)
設定第 k 位：      mask |= (1 << k)
清除第 k 位：      mask &= ~(1 << k)
翻轉第 k 位：      mask ^= (1 << k)
數有幾個 1：       bin(mask).count("1")  或  mask.bit_count()（3.10+）
取最低位的 1：     mask & -mask
清除最低位的 1：   mask & (mask - 1)
全部候選（1~9）：  0b111111111 = 0x1FF = 511
可填的數字：       ~(rows[r] | cols[c] | boxes[b]) & 0x1FF"""),
   ], "O(81) = O(1)", "O(27) = O(1)", "每格三次位元運算", "27 個整數"),
 ],
 "compare": (["解法", "資料結構", "記憶體", "速度", "適合"],
   [["一、三組集合", "27 個 set", "中", "快", "面試預設，最好讀"],
    ["二、單一集合", "1 個 set", "大", "中", "概念統一"],
    ["三、位元遮罩", "27 個 int", "小", "最快", "第 37 題的前置練習"]]),
 "edges": [
   "<strong>全空盤面</strong>：全是 <code>'.'</code> → true。",
   "<strong>同一列重複</strong>：<code>board[0][0] == board[0][5] == '5'</code> → false。",
   "<strong>同一行重複</strong>：<code>board[0][0] == board[5][0] == '5'</code> → false。",
   "<strong>同一宮重複但不同列不同行</strong>：<code>board[0][0] == board[1][1] == '5'</code> → false。"
   "<strong>這是最容易漏掉的一種</strong> —— 只檢查列和行的話會誤判成 true。",
   "<strong>有效但無解</strong>：題目明說這算 true。不要試著去判斷可解性。",
   "<strong>只有一個數字</strong>：一定 true。",
   "<strong>81 格全滿且合法</strong>：true。",
 ],
 "follow": [
   ("h", "追問一：如果要驗證任意 n²×n² 的數獨呢？"),
   "把所有的 9 換成 <code>n*n</code>、3 換成 <code>n</code> 即可："
   "<code>box = (r // n) * n + c // n</code>。"
   "位元遮罩在 n² &gt; 64 時要改用大整數或多個字組 —— Python 沒問題，C++ 要用 bitset。",
   ("h", "追問二：如果要「一邊填一邊驗證」呢？"),
   "那就是第 37 題。此時三組遮罩要能<strong>增量更新和回退</strong>：",
   ("c", """填入：  rows[r] |= bit;  cols[c] |= bit;  boxes[b] |= bit
回退：  rows[r] ^= bit;  cols[c] ^= bit;  boxes[b] ^= bit
        （XOR 可以當「切換」用，因為我們確定那一位現在是 1）

有了遮罩，「這一格可以填哪些數字」是一次運算：
    candidates = ~(rows[r] | cols[c] | boxes[b]) & 0x1FF

這正是第 37 題能在毫秒內解完的關鍵。"""),
   ("h", "追問三：為什麼數獨的三條規則可以用同一套程式碼檢查？"),
   "因為它們在抽象上是同一件事：<strong>「這 9 個格子構成一個群組，群組內不能有重複」</strong>。"
   "列、行、宮只是三種不同的分組方式。"
   "如果把數獨看成一個<strong>圖著色問題</strong>（81 個節點，同群組的節點之間連邊，"
   "用 9 種顏色著色），那麼「有效」就是「目前的部分著色沒有衝突」。"
   "<strong>從這個角度看，數獨、N 皇后、地圖著色、課表排程其實是同一類問題。</strong>",
 ],
 "related": [
   "<strong>第 37 題 Sudoku Solver</strong> —— 這題的延伸，回溯 + 同一套遮罩",
   "<strong>第 51 題 N-Queens</strong> —— 另一個「約束檢查 + 回溯」的經典",
   "<strong>第 289 題 Game of Life</strong> —— 另一個網格題",
 ],
 "check": [
   "宮格編號公式 <code>(r//3)*3 + c//3</code> 是怎麼來的？(4,7) 屬於第幾宮？",
   "只檢查列和行、不檢查宮，哪一種輸入會被誤判成有效？",
   "解法二如果把 row key 寫成 <code>f\"{v}-{r}\"</code>、col key 寫成 <code>f\"{r}-{v}\"</code>，"
   "什麼情況會誤判？",
   "位元遮罩要怎麼算出「這一格可以填哪些數字」？",
 ],
})
print("P36 written")
