# -*- coding: utf-8 -*-
"""第 496、497、498、500 題。"""
import random
from collections import Counter
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(496)


# ==================== 496. Next Greater Element I ====================
S["p496"] = '''class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nxt = {}                       # nums2 中每個值 -> 它右邊第一個更大的值
        stack = []                     # 單調遞減堆疊：還沒找到「下一個更大」的值
        for x in nums2:
            while stack and stack[-1] < x:
                nxt[stack.pop()] = x   # ★ x 就是它們等待的「下一個更大元素」
            stack.append(x)
        return [nxt.get(x, -1) for x in nums1]'''

_p496 = S.load("p496")
for _ in range(3000):
    nums2 = random.sample(range(0, 20), random.randrange(1, 10))
    nums1 = random.sample(nums2, random.randint(1, len(nums2)))
    want = []
    for x in nums1:
        i = nums2.index(x)
        want.append(next((y for y in nums2[i + 1:] if y > x), -1))
    assert _p496.nextGreaterElement(nums1, nums2) == want
print("P496 OK")

_P496_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">nums2 = [1, 3, 4, 2]：單調遞減堆疊，新的數字「解決」所有比它小的等待者</text>
            <g font-size="12">
              <text x="30" y="52" fill="var(--text-muted)">讀入</text><text x="100" y="52" fill="var(--text-muted)">彈出（找到答案）</text><text x="280" y="52" fill="var(--text-muted)">堆疊</text>
              <text x="30" y="78" fill="var(--text)">1</text><text x="100" y="78" fill="var(--text-muted)">—</text><text x="280" y="78" fill="var(--text)">[1]</text>
              <text x="30" y="102" fill="var(--text)">3</text><text x="100" y="102" fill="var(--accent)">1 → 3</text><text x="280" y="102" fill="var(--text)">[3]</text>
              <text x="30" y="126" fill="var(--text)">4</text><text x="100" y="126" fill="var(--accent)">3 → 4</text><text x="280" y="126" fill="var(--text)">[4]</text>
              <text x="30" y="150" fill="var(--text)">2</text><text x="100" y="150" fill="var(--text-muted)">—（2 &lt; 4）</text><text x="280" y="150" fill="var(--text)">[4, 2]</text>
              <text x="30" y="174" fill="var(--text-muted)">結束</text><text x="100" y="174" fill="#ff8a65">4、2 → −1</text><text x="280" y="174" fill="var(--text-muted)">留在堆疊裡的都沒有答案</text>
            </g>
            <text x="20" y="208" fill="var(--gold)" font-size="12">★ 堆疊從底到頂遞減：新數字比頂端大，頂端就等到了答案；每個數只進出一次，O(n)。</text>'''

emit({
 "num": 496, "slug": "next-greater-element-i",
 "en": [
   "The <strong>next greater element</strong> of some element <code>x</code> in an array is the <strong>first greater</strong> element that is <strong>to the right</strong> of <code>x</code> in the same array.",
   "You are given two <strong>distinct 0-indexed</strong> integer arrays <code>nums1</code> and <code>nums2</code>, where <code>nums1</code> is a subset of <code>nums2</code>.",
   "For each <code>0 &lt;= i &lt; nums1.length</code>, find the index <code>j</code> such that <code>nums1[i] == nums2[j]</code> and determine the <strong>next greater element</strong> of <code>nums2[j]</code> in <code>nums2</code>. If there is no next greater element, then the answer for this query is <code>-1</code>.",
   "Return <em>an array </em><code>ans</code><em> of length </em><code>nums1.length</code><em> such that </em><code>ans[i]</code><em> is the <strong>next greater element</strong> as described above.</em>",
   "<strong>Follow up:</strong> Could you find an <code>O(nums1.length + nums2.length)</code> solution?",
 ],
 "zh": [
   "陣列中某個元素 <code>x</code> 的<strong>下一個更大元素</strong>，是在它<strong>右邊第一個</strong>比它大的元素。",
   "給你兩個元素<strong>互不相同</strong>的陣列 <code>nums1</code>、<code>nums2</code>，<code>nums1</code> 是 <code>nums2</code> 的子集。對 <code>nums1</code> 的每個元素，找出它在 <code>nums2</code> 中的下一個更大元素；沒有則為 <code>-1</code>。",
   "<strong>進階：</strong>能做到 <code>O(nums1.length + nums2.length)</code> 嗎？",
 ],
 "examples": """範例 1
  輸入：nums1 = [4,1,2], nums2 = [1,3,4,2]
  輸出：[-1,3,-1]

範例 2
  輸入：nums1 = [2,4], nums2 = [1,2,3,4]
  輸出：[3,-1]""",
 "constraints": [
   "1 ≤ <code>nums1.length ≤ nums2.length</code> ≤ 1000",
   "0 ≤ <code>nums1[i], nums2[i]</code> ≤ 10⁴",
   "所有整數互不相同，<code>nums1</code> 的元素都在 <code>nums2</code> 中",
 ],
 "idea": [
   ("fig", _P496_FIG, "0 0 640 222"),
   ("c", """【單調堆疊的經典題】
    先對 nums2 的每個值算出「下一個更大元素」，存進雜湊表，
    再依 nums1 查表。

【單調遞減堆疊】
    堆疊裡放「還在等待下一個更大元素」的值。
    讀到 x：
        堆疊頂端比 x 小 -> x 就是它的答案，彈出並記錄
        重複直到頂端 >= x
        x 推進堆疊（它也開始等待）
    結束時還在堆疊裡的，右邊沒有更大的 -> -1。

【為什麼堆疊是遞減的？】
    如果頂端比 x 小，早就被 x 彈出了 ——
    所以留在堆疊裡的，一定由下往上遞減。"""),
 ],
 "approaches": [
   ap("解法", "單調堆疊 + 雜湊表", [
     ("c", S["p496"]),
   ], "O(m + n)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>最右邊的元素</strong> → −1。",
   "<strong>遞減陣列</strong> → 全部 −1。",
   "<strong>元素互不相同</strong> → 才能用值當雜湊表的鍵（否則要用索引）。",
 ],
 "follow": [
   ("h", "單調堆疊系列"),
   ("c", "第 503 題（環形陣列：走兩圈）、第 739 題（每日溫度：記錄索引算距離）、第 84 題（柱狀圖最大矩形）、第 42 題（接雨水）。"),
 ],
 "related": [
   "<strong>第 503 題 下一個更大元素 II</strong>",
   "<strong>第 739 題 每日溫度</strong>",
   "<strong>第 84 題 柱狀圖中最大的矩形</strong>",
 ],
 "check": [
   "堆疊裡存的是什麼？",
   "什麼時候一個元素找到了它的答案？",
   "為什麼總時間是 O(n)？",
 ],
})


# ==================== 497. Random Point in Non-overlapping Rectangles ====================
S["p497"] = '''class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = []                      # 每個矩形「整數點數」的前綴和
        total = 0
        for a, b, x, y in rects:
            total += (x - a + 1) * (y - b + 1)   # ★ 算的是格點數，不是面積
            self.prefix.append(total)

    def pick(self) -> List[int]:
        k = random.randrange(self.prefix[-1])    # 在所有格點中均勻選第 k 個
        i = bisect.bisect_right(self.prefix, k)  # 落在第 i 個矩形
        a, b, x, y = self.rects[i]
        k -= self.prefix[i - 1] if i else 0      # 在這個矩形內的編號
        w = x - a + 1
        return [a + k % w, b + k // w]'''

_cls = S.loadns("p497")["Solution"]
rects = [[-2, -2, 1, 1], [2, 2, 4, 6], [5, 0, 5, 0]]
obj = _cls(rects)
pts = [(x, y) for a, b, c, d in rects for x in range(a, c + 1) for y in range(b, d + 1)]
N = 60000
cnt = Counter(tuple(obj.pick()) for _ in range(N))
assert set(cnt) == set(pts)
exp = N / len(pts)
assert all(abs(c - exp) < exp * 0.25 for c in cnt.values()), cnt
print("P497 OK")

emit({
 "num": 497, "slug": "random-point-in-non-overlapping-rectangles",
 "en": [
   "You are given an array of non-overlapping axis-aligned rectangles <code>rects</code> where <code>rects[i] = [a<sub>i</sub>, b<sub>i</sub>, x<sub>i</sub>, y<sub>i</sub>]</code> indicates that <code>(a<sub>i</sub>, b<sub>i</sub>)</code> is the bottom-left corner point of the <code>i<sup>th</sup></code> rectangle and <code>(x<sub>i</sub>, y<sub>i</sub>)</code> is the top-right corner point of the <code>i<sup>th</sup></code> rectangle. Design an algorithm to pick a random integer point inside the space covered by one of the given rectangles. A point on the perimeter of a rectangle is included in the space covered by the rectangle.",
   "Any integer point inside the space covered by one of the given rectangles should be equally likely to be returned.",
   "<strong>Note</strong> that an integer point is a point that has integer coordinates.",
 ],
 "zh": [
   "給你一組<strong>互不重疊</strong>、邊與座標軸平行的矩形，<code>[a, b, x, y]</code> 代表左下角 <code>(a, b)</code>、右上角 <code>(x, y)</code>。",
   "設計 <code>pick()</code>：在所有矩形覆蓋的範圍內（含邊界），<strong>均勻</strong>地隨機選一個<strong>整數座標點</strong>。",
 ],
 "examples": """範例
  Solution([[-2, -2, 1, 1], [2, 2, 4, 6]])
  pick() -> 例如 [1, -2]
  pick() -> 例如 [3, 4]""",
 "constraints": [
   "1 ≤ <code>rects.length</code> ≤ 100",
   "−10⁹ ≤ <code>a<sub>i</sub> &lt; x<sub>i</sub></code> ≤ 10⁹",
   "<code>x<sub>i</sub> − a<sub>i</sub></code> ≤ 2000，<code>y<sub>i</sub> − b<sub>i</sub></code> ≤ 2000",
   "最多呼叫 10⁴ 次 <code>pick</code>",
 ],
 "idea": [
   ("c", """【每個整數點機率相同 -> 矩形被選中的機率 ∝ 它的點數】
    矩形 [a, b, x, y] 的整數點數 = (x - a + 1) × (y - b + 1)
    注意是「點數」，不是面積 (x-a)(y-b)！
    1×1 的矩形有 4 個整數點，面積卻是 1。

【依點數加權隨機選矩形（第 528 題）】
    點數的前綴和，隨機一個 k ∈ [0, 總點數)，
    二分找到它落在哪個矩形。

【在矩形內定位】
    k 減掉前面矩形的點數後，就是這個矩形內的編號，
    編號 k -> 座標 (a + k % 寬, b + k // 寬)。
    一次隨機數同時決定了「哪個矩形」和「哪個點」。"""),
 ],
 "approaches": [
   ap("解法", "點數前綴和 + 二分 + 編號轉座標", [
     ("c", S["p497"]),
     "驗證方式：六萬次抽樣，每個整數點都被選到，而且次數都在期望值 ±25% 以內。",
   ], "建構 O(n)，pick O(log n)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>退化成一條線或一個點的矩形</strong> → 點數仍然 ≥ 1。",
   "<strong>用面積當權重</strong> → 錯誤：邊界上的點會被低估。",
 ],
 "follow": [
   ("h", "加權隨機選擇"),
   ("c", "「依權重選」= 權重前綴和 + 均勻隨機 + 二分。第 528 題是最純粹的版本。"),
 ],
 "related": [
   "<strong>第 528 題 按權重隨機選擇</strong>",
   "<strong>第 478 題 在圓內隨機生成點</strong>",
 ],
 "check": [
   "為什麼要用整數點數而不是面積當權重？",
   "一個隨機數怎麼同時決定矩形和點？",
 ],
})


# ==================== 498. Diagonal Traverse ====================
S["p498"] = '''class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        for d in range(m + n - 1):                 # ★ 同一條對角線上 i + j = d
            # 這條對角線上 i 的範圍
            lo, hi = max(0, d - n + 1), min(d, m - 1)
            rows = range(hi, lo - 1, -1) if d % 2 == 0 else range(lo, hi + 1)
            # d 偶數：往右上走（i 由大到小）；d 奇數：往左下走（i 由小到大）
            for i in rows:
                res.append(mat[i][d - i])
        return res'''

_p498 = S.load("p498")
for M, want in [([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]), ([[1, 2], [3, 4]], [1, 2, 3, 4])]:
    assert _p498.findDiagonalOrder(M) == want
for _ in range(1000):
    m, n = random.randrange(1, 6), random.randrange(1, 6)
    M = [[i * n + j for j in range(n)] for i in range(m)]
    want = []
    for d in range(m + n - 1):
        cells = [(i, d - i) for i in range(m) if 0 <= d - i < n]
        if d % 2 == 0:
            cells.reverse()
        want += [M[i][j] for i, j in cells]
    assert _p498.findDiagonalOrder(M) == want
print("P498 OK")

emit({
 "num": 498, "slug": "diagonal-traverse",
 "en": [
   "Given an <code>m x n</code> matrix <code>mat</code>, return <em>an array of all the elements of the array in a diagonal order</em>.",
 ],
 "zh": [
   "給你一個 <code>m x n</code> 的矩陣，依照<strong>對角線來回</strong>的順序回傳所有元素：第一條往右上、第二條往左下、第三條往右上……",
 ],
 "examples": """範例 1
  輸入：mat = [[1,2,3],[4,5,6],[7,8,9]]
  輸出：[1,2,4,7,5,3,6,8,9]
  說明：對角線依序是 [1]、[2,4]（往左下）、[7,5,3]（往右上）、[6,8]、[9]。

範例 2
  輸入：mat = [[1,2],[3,4]]
  輸出：[1,2,3,4]""",
 "constraints": [
   "1 ≤ <code>m, n</code> ≤ 10⁴",
   "1 ≤ <code>m × n</code> ≤ 10⁴",
 ],
 "idea": [
   ("c", """【同一條對角線：i + j 相同】
    d = i + j，從 0 到 m + n - 2。

【每條對角線上 i 的範圍】
    j = d - i 必須在 [0, n-1]：i >= d - n + 1
    i 本身在 [0, m-1]
    -> i 從 max(0, d-n+1) 到 min(d, m-1)

【方向交替】
    d 偶數：往右上走 -> i 由大到小
    d 奇數：往左下走 -> i 由小到大

    不需要模擬「撞到邊界要轉彎」的複雜規則。"""),
 ],
 "approaches": [
   ap("解法", "依對角線編號 i + j 分組", [
     ("c", S["p498"]),
   ], "O(mn)", "O(1)", "", "不計輸出", optimal=True),
 ],
 "edges": [
   "<strong>只有一列或一欄</strong> → 每條對角線只有一個元素。",
   "<strong>長方形</strong> → i 的範圍要同時考慮 m 和 n。",
 ],
 "follow": [
   ("h", "對角線分組"),
   ("c", "i + j 相同是「反對角線」，i − j 相同是「主對角線」。第 1424 題（對角線遍歷 II）、第 1329 題（對角線排序）、N 皇后（第 51 題）都用這兩個不變量。"),
 ],
 "related": [
   "<strong>第 1424 題 對角線遍歷 II</strong>",
   "<strong>第 54 題 螺旋矩陣</strong>",
   "<strong>第 51 題 N 皇后</strong>",
 ],
 "check": [
   "同一條對角線上的格子有什麼共同點？",
   "第 d 條對角線上 i 的範圍是什麼？",
 ],
})


# ==================== 500. Keyboard Row ====================
S["p500"] = '''class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        # ★ 單字的字母集合是某一排的子集
        return [w for w in words if any(set(w.lower()) <= r for r in rows)]'''

_p500 = S.load("p500")
for words, want in [(["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]), (["omk"], []), (["adsdf", "sfd"], ["adsdf", "sfd"])]:
    assert _p500.findWords(words) == want
_R = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
for _ in range(2000):
    w = "".join(random.choice("qaZwsXAe") for _ in range(random.randrange(1, 6)))
    want = any(all(c.lower() in r for c in w) for r in _R)
    assert (_p500.findWords([w]) == [w]) == want
print("P500 OK")

emit({
 "num": 500, "slug": "keyboard-row",
 "en": [
   "Given an array of strings <code>words</code>, return <em>the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below</em>.",
   "<strong>Note</strong> that the strings are <strong>case-insensitive</strong>, both lowercased and uppercased of the same letter are treated as if they are at the same row.",
   "In the <strong>American keyboard</strong>:",
   ("ul", ["the first row consists of the characters <code>\"qwertyuiop\"</code>,",
           "the second row consists of the characters <code>\"asdfghjkl\"</code>, and",
           "the third row consists of the characters <code>\"zxcvbnm\"</code>."]),
 ],
 "zh": [
   "給你一組單字 <code>words</code>，回傳只用美式鍵盤<strong>同一排</strong>字母就能打出來的單字（不分大小寫）。",
   ("ul", ["第一排：<code>qwertyuiop</code>", "第二排：<code>asdfghjkl</code>", "第三排：<code>zxcvbnm</code>"]),
 ],
 "examples": """範例 1
  輸入：words = ["Hello","Alaska","Dad","Peace"]
  輸出：["Alaska","Dad"]

範例 2
  輸入：words = ["omk"]
  輸出：[]""",
 "constraints": [
   "1 ≤ <code>words.length</code> ≤ 20",
   "1 ≤ <code>words[i].length</code> ≤ 100",
   "<code>words[i]</code> 由大小寫英文字母組成",
 ],
 "idea": [
   ("c", """【集合的子集關係】
    單字的字母集合（轉小寫）是某一排的子集 <=> 可以只用那一排打出來。
    Python：set(w.lower()) <= row_set

【另一種寫法】
    先建「字母 -> 排號」的對照表，
    檢查單字中所有字母的排號是否都相同。"""),
 ],
 "approaches": [
   ap("解法", "集合子集判斷", [
     ("c", S["p500"]),
   ], "O(總字元數)", "O(1)", "", "三排字母是固定的", optimal=True),
 ],
 "edges": [
   "<strong>大小寫混合</strong> → 先轉小寫。",
   "<strong>單一字母的單字</strong> → 一定可以。",
 ],
 "follow": [
   ("h", "小知識"),
   ("c", "只用第一排能打出的最長常見英文單字之一是 \"typewriter\"（打字機）——據說當年業務員示範 QWERTY 鍵盤時，就用它來展示打字速度。"),
 ],
 "related": [
   "<strong>第 1165 題 單行鍵盤</strong>（付費）",
 ],
 "check": [
   "怎麼用集合判斷一個單字能不能用同一排打出？",
 ],
})
