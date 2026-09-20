# -*- coding: utf-8 -*-
"""第 83–86 題。"""
import random
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(83)

# ==================== 83. Remove Duplicates from Sorted List ====================
S["p83_iter"] = '''class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next     # 跳過下一個（不前進，可能還有更多重複）
            else:
                cur = cur.next
        return head'''

S["p83_rec"] = '''class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        head.next = self.deleteDuplicates(head.next)
        # 後面處理好之後，如果新的 next 和自己同值，就把它跳過
        return head.next if head.val == head.next.val else head'''

_p83 = [S.load(k) for k in ("p83_iter", "p83_rec")]


def _p83_ref(vals):
    out = []
    for v in vals:
        if not out or out[-1] != v:
            out.append(v)
    return out


for vals in [[1, 1, 2], [1, 1, 2, 3, 3], [], [1], [1, 1], [1, 1, 1],
             [1, 2, 3], [1, 1, 2, 2, 3, 3]]:
    e = _p83_ref(vals)
    for sol in _p83:
        assert from_list(sol.deleteDuplicates(to_list(vals))) == e, ("P83", vals, sol)
for _ in range(5000):
    vals = sorted(random.randint(0, 4) for _ in range(random.randint(0, 10)))
    e = _p83_ref(vals)
    for sol in _p83:
        assert from_list(sol.deleteDuplicates(to_list(vals))) == e, ("P83", vals, sol)
print("P83 solutions OK")

emit({
 "num": 83, "slug": "remove-duplicates-from-sorted-list",
 "en": [
   "Given the <code>head</code> of a sorted linked list, <em>delete all duplicates such that "
   "each element appears only once</em>. Return <em>the linked list <strong>sorted</strong> "
   "as well</em>.",
 ],
 "zh": [
   "給你一個<strong>已排序</strong>的鏈結串列，刪掉重複的元素，"
   "讓每個值<strong>只出現一次</strong>。回傳處理後的串列（仍然有序）。",
 ],
 "pre": [
   ("note", "和第 82 題的關鍵差異：頭節點永遠保留", [
     ("c", """1 -> 1 -> 2 -> 3 -> 3

第 83 題（本題，每個值留一個）：  1 -> 2 -> 3
第 82 題（有重複的全刪）：        2

因為本題「每組保留第一個」，所以：

    頭節點【永遠】會被保留（它是它那一組的第一個）
    -> 不需要 dummy node
    -> 不需要 prev 指標

    程式碼從第 82 題的 14 行降到 7 行。

這是一個很好的對照：
    「規格上一個小小的差別（留一個 vs 全刪）」
    造成「實作上一整個資料結構（dummy node）的有無」。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [1,1,2]
  輸出：[1,2]

範例 2
  輸入：head = [1,1,2,3,3]
  輸出：[1,2,3]""",
 "constraints": [
   "串列節點數在 <code>[0, 300]</code> 範圍內",
   "−100 ≤ <code>Node.val</code> ≤ 100",
   "串列已依<strong>升序</strong>排好",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>已排序</strong> —— 相同的值連續，所以只要和「下一個」比。",
       "<strong>可以是空串列</strong> → 回傳 <code>None</code>。"
       "<code>while cur and cur.next</code> 自然處理。",
       "<strong>結果永遠非空</strong>（只要輸入非空）—— 和第 82 題不同。",
     ]),
   ]),
 ],
 "idea": [
   "一個指標掃過去，<strong>看到「下一個和我一樣」就把它跳過</strong>。"
   "關鍵是：<strong>跳過之後不能前進</strong>，因為新的「下一個」可能還是一樣。",
 ],
 "approaches": [
   ap("解法一", "單指標掃描（標準解）", [
     ("c", S["p83_iter"]),
     ("h", "為什麼刪掉之後 <code>cur</code> 不能前進？"),
     ("c", """1 -> 1 -> 1

  cur 在第一個 1：
      cur.val == cur.next.val  ->  cur.next = 第三個 1
      現在是 1 -> 1（第一個和第三個）

  如果 cur 前進了：
      cur 會跳到第三個 1，而串列還是 1 -> 1 ✘

  正確做法（cur 不動）：
      cur 還在第一個 1
      cur.val == cur.next.val  ->  cur.next = None
      現在是 1 ✔

一句話：
    刪除一個節點之後，「下一個」變成了新的節點，
    必須重新檢查它。

    這和第 27 題（Remove Element）的「從尾巴填坑」是同一個道理 ——
    只要「搬進來的東西還沒檢查過」，指標就不能前進。"""),
     ("h", "<code>while cur and cur.next</code> 的兩個條件"),
     "<code>cur</code>：處理空串列。"
     "<code>cur.next</code>：處理「走到最後一個節點」（沒有下一個可以比）。"
     "<strong>順序不能換</strong> —— Python 的短路求值保證 <code>cur</code> 是 <code>None</code> 時"
     "不會去讀 <code>cur.next</code>。",
     "<strong>七行、O(1) 空間、一趟掃完。</strong>"
     "這是鏈結串列題裡最乾淨的一題。",
   ], "O(n)", "O(1)", "每個節點最多看兩次", "只用一個指標", optimal=True),

   ap("解法二", "遞迴（三行核心）", [
     ("c", S["p83_rec"]),
     ("c", """語意：「先把後面處理乾淨，再看自己要不要被合併掉」

deleteDuplicates([1,1,2])
    head = 第一個 1
    head.next = deleteDuplicates([1,2])
                    head = 第二個 1
                    head.next = deleteDuplicates([2]) = [2]
                    1 != 2  ->  return 第二個 1（也就是 [1,2]）
    現在 head.next 是第二個 1
    head.val(1) == head.next.val(1)  ->  return head.next
    也就是回傳 [1,2] ✔（第一個 1 被跳過了）

注意這裡「保留的是後面那個」而不是前面那個 ——
但因為值相同，輸出看不出差別。

如果節點帶著其他資料（例如 (值, 標籤)），
「保留哪一個」就有差別了 —— 那時要改成保留 head 並接上 head.next.next。"""),
     "<strong>只有三行核心邏輯。</strong>"
     "但它有 O(n) 的遞迴深度 —— n = 300 沒問題，更大就會爆。",
   ], "O(n)", "O(n)", "每個節點一層遞迴", "遞迴堆疊"),
 ],
 "compare": (["", "第 83 題（留一個）", "第 82 題（全刪）"],
   [["需要 dummy？", "✘", "✔"],
    ["需要 prev？", "✘", "✔"],
    ["頭節點會被刪？", "✘ 永遠保留", "✔ 可能"],
    ["結果可能是空？", "✘（輸入非空的話）", "✔"],
    ["程式碼行數", "7", "14"]]),
 "edges": [
   "<strong>空串列</strong>：<code>[]</code> → <code>[]</code>。",
   "<strong>單一節點</strong>：<code>[1]</code> → <code>[1]</code>。",
   "<strong>全部相同</strong>：<code>[1,1,1]</code> → <code>[1]</code>。"
   "<strong>「刪除後 cur 不前進」在這裡至關重要。</strong>",
   "<strong>沒有重複</strong>：<code>[1,2,3]</code> → 原樣。",
   "<strong>成對重複</strong>：<code>[1,1,2,2,3,3]</code> → <code>[1,2,3]</code>。",
   "<strong>結尾有重複</strong>：<code>[1,2,2]</code> → <code>[1,2]</code>。"
   "最後 <code>cur.next</code> 變成 <code>None</code>，迴圈正確結束。",
 ],
 "follow": [
   ("h", "追問一：如果要「有重複的全部刪掉」呢？"),
   "第 82 題。需要 dummy node 和 prev 指標，程式碼長一倍。"
   "<strong>兩題放在一起寫一次，就能清楚感受到「規格差一句話，實作差一個資料結構」。</strong>",
   ("h", "追問二：如果串列沒有排序呢？"),
   "用一個 <code>set</code> 記錄看過的值，遇到看過的就跳過。"
   "空間從 O(1) 變成 O(不同值的個數)。"
   "<strong>「已排序」在這裡的價值就是那個 set。</strong>",
   ("h", "追問三：Python 的 <code>itertools.groupby</code> 可以用嗎？"),
   "如果先把串列轉成 list，可以 —— 但那就失去「原地操作串列」的意義了，"
   "而且空間變成 O(n)。"
   "<strong>串列題的重點通常是「指標操作」而不是「結果對不對」。</strong>",
   ("h", "追問四：這題為什麼常被當成串列的入門題？"),
   "因為它只需要一個指標、一個 if、一個 while —— "
   "<strong>但它已經包含了串列操作的核心觀念</strong>：",
   ("ul", [
     "「刪除節點」= 讓前一個節點跳過它",
     "刪除之後指標要不要前進（狀態是否改變）",
     "邊界條件（空串列、最後一個節點）",
   ]),
   "<strong>把這三件事想清楚，第 19、82、203、237 題就都會了。</strong>",
 ],
 "related": [
   "<strong>第 82 題 Remove Duplicates from Sorted List II</strong> —— 有重複的全刪",
   "<strong>第 26 題 Remove Duplicates from Sorted Array</strong> —— 陣列版",
   "<strong>第 203 題 Remove Linked List Elements</strong> —— 刪掉特定值",
   "<strong>第 237 題 Delete Node in a Linked List</strong> —— 只給你要刪的那個節點",
 ],
 "check": [
   "刪除之後 <code>cur</code> 為什麼不能前進？請用 <code>[1,1,1]</code> 追一遍。",
   "為什麼這題不需要 dummy node，而第 82 題需要？",
   "<code>while cur and cur.next</code> 的兩個條件各自防什麼？",
   "如果串列沒有排序，要怎麼改？空間會變成多少？",
 ],
})
print("P83 written")

# ==================== 84. Largest Rectangle in Histogram ====================
S["p84_stack"] = '''class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []          # 存索引，對應的高度「嚴格遞增」
        best = 0
        n = len(heights)

        for i in range(n + 1):
            # i == n 時用高度 0 當哨兵，把堆疊裡剩下的全部結算掉
            h = heights[i] if i < n else 0

            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                # 左邊界：堆疊裡的前一個（它一定比 height 矮）
                left = stack[-1] if stack else -1
                width = i - left - 1
                best = max(best, height * width)

            stack.append(i)

        return best'''

S["p84_bounds"] = '''class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # left[i] = 左邊第一個「比 heights[i] 矮」的位置（沒有就是 -1）
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        # right[i] = 右邊第一個「比 heights[i] 矮」的位置（沒有就是 n）
        right = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)

        return max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n else 0'''

S["p84_brute"] = '''class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 暴力：以每根柱子的高度為「矩形的高」，往兩邊擴張
        n = len(heights)
        best = 0
        for i in range(n):
            h = heights[i]
            l = i
            while l - 1 >= 0 and heights[l - 1] >= h:
                l -= 1
            r = i
            while r + 1 < n and heights[r + 1] >= h:
                r += 1
            best = max(best, h * (r - l + 1))
        return best'''

_p84 = [S.load(k) for k in ("p84_stack", "p84_bounds", "p84_brute")]
for c in [[2, 1, 5, 6, 2, 3], [2, 4], [], [1], [0], [1, 1], [5, 4, 3, 2, 1],
          [1, 2, 3, 4, 5], [2, 2, 2], [3, 6, 5, 7, 4, 8, 1, 0]]:
    e = _p84[2].largestRectangleArea(list(c))
    for sol in _p84:
        assert sol.largestRectangleArea(list(c)) == e, ("P84", c, sol,
                                                        sol.largestRectangleArea(list(c)), e)
assert _p84[0].largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
assert _p84[0].largestRectangleArea([2, 4]) == 4
for _ in range(5000):
    c = [random.randint(0, 8) for _ in range(random.randint(0, 12))]
    e = _p84[2].largestRectangleArea(list(c))
    for sol in _p84:
        assert sol.largestRectangleArea(list(c)) == e, ("P84", c, sol)
print("P84 solutions OK")

_P84_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">heights = [2, 1, 5, 6, 2, 3]，最大矩形面積是 10（高 5、寬 2）</text>
            <g>
              <rect x="80" y="172" width="70" height="36" fill="var(--border)" opacity="0.6"/>
              <rect x="150" y="190" width="70" height="18" fill="var(--border)" opacity="0.6"/>
              <rect x="220" y="118" width="70" height="90" fill="var(--border)" opacity="0.6"/>
              <rect x="290" y="100" width="70" height="108" fill="var(--border)" opacity="0.6"/>
              <rect x="360" y="172" width="70" height="36" fill="var(--border)" opacity="0.6"/>
              <rect x="430" y="154" width="70" height="54" fill="var(--border)" opacity="0.6"/>
              <rect x="220" y="118" width="140" height="90" fill="#ff8a65" opacity="0.35"/>
              <rect x="220" y="118" width="140" height="90" fill="none" stroke="#ff8a65" stroke-width="2.5"/>
              <line x1="60" y1="208" x2="540" y2="208" stroke="var(--text-muted)"/>
            </g>
            <g font-size="12" fill="var(--text-muted)" text-anchor="middle">
              <text x="115" y="226">2</text><text x="185" y="226">1</text><text x="255" y="226">5</text>
              <text x="325" y="226">6</text><text x="395" y="226">2</text><text x="465" y="226">3</text>
            </g>
            <text x="290" y="112" fill="#ff8a65" font-size="13" text-anchor="middle">5 × 2 = 10</text>
            <line x1="20" y1="244" x2="620" y2="244" stroke="var(--border)"/>
            <text x="20" y="272" fill="var(--gold)" font-size="12">核心：對每根柱子，問「以它的高度為高，最寬能延伸到哪裡？」</text>
            <text x="20" y="296" fill="var(--text-muted)" font-size="12">左邊界＝左邊第一個比它矮的、右邊界＝右邊第一個比它矮的 → 寬 = right − left − 1</text>
            <text x="20" y="320" fill="var(--text-muted)" font-size="12">「左／右第一個比我小的」正是單調堆疊要回答的問題。</text>'''

emit({
 "num": 84, "slug": "largest-rectangle-in-histogram",
 "en": [
   "Given an array of integers <code>heights</code> representing the histogram's bar height "
   "where the width of each bar is <code>1</code>, return <em>the area of the largest "
   "rectangle in the histogram</em>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>heights</code>，代表柱狀圖裡每根柱子的高度（寬度都是 1）。"
   "求出這張柱狀圖裡<strong>最大的矩形面積</strong>。",
 ],
 "pre": [
   ("note", "換一個角度：對「每個高度」問最大寬度", [
     ("c", """直接枚舉所有矩形是 O(n²) 甚至更多。
換個角度：

    每一個「最大矩形」，它的高度一定等於【某一根柱子的高度】
    （否則還可以再往上長一點）。

    所以只要對每根柱子 i 問：
        「以 heights[i] 為高，這個矩形最寬能到哪裡？」

    答案是：往左右擴張，直到碰到「比 heights[i] 矮」的柱子為止。

        左邊界 L = 左邊第一個「比 heights[i] 矮」的位置
        右邊界 R = 右邊第一個「比 heights[i] 矮」的位置
        寬度 = R - L - 1
        面積 = heights[i] × (R - L - 1)

    取所有 i 的最大值就是答案。

heights = [2, 1, 5, 6, 2, 3]

  i=2（高 5）：左邊第一個比 5 矮的是 index 1（值 1）
               右邊第一個比 5 矮的是 index 4（值 2）
               寬 = 4 - 1 - 1 = 2，面積 = 5 × 2 = 10 ✔

問題轉化成：
    「對每個元素，找出左邊／右邊第一個比它小的元素」

    這正是【單調堆疊】要回答的問題。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：heights = [2,1,5,6,2,3]
  輸出：10
  說明：高 5、寬 2 的矩形（索引 2 到 3，高度取 min(5,6) = 5）。

範例 2
  輸入：heights = [2,4]
  輸出：4""",
 "constraints": [
   "1 ≤ <code>heights.length</code> ≤ 10⁵",
   "0 ≤ <code>heights[i]</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n 到 10⁵</strong>。O(n²) 是 10¹⁰ —— 必定 TLE。"
       "<strong>必須 O(n)。</strong>",
       "<strong>高度可以是 0</strong>。高度 0 的柱子面積永遠是 0，"
       "但它會<strong>切斷</strong>左右兩邊的矩形 —— 這在邏輯上很重要。",
       "<strong>最大面積可能是 10⁵ × 10⁴ = 10⁹</strong>，"
       "在 32 位元整數範圍內（剛好），但在 C/Java 裡值得留意。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P84_FIG, "0 0 640 336"),
 ],
 "approaches": [
   ap("解法一", "暴力擴張（O(n²)，當基準）", [
     ("c", S["p84_brute"]),
     "對每根柱子，往左右擴張直到碰到更矮的。"
     "<strong>直白地實作了上面的公式</strong>，是驗證單調堆疊的標準答案。",
     "<strong>最壞 O(n²)</strong>（全部等高時每根都要掃全長），n = 10⁵ 會 TLE。",
   ], "O(n²)", "O(1)", "每根柱子最多掃全長", "只用幾個變數"),

   ap("解法二", "單調堆疊，一趟解決（標準解）", [
     ("c", S["p84_stack"]),
     ("h", "堆疊的不變量"),
     ("c", """堆疊裡存【索引】，而且對應的高度是「單調不遞減」的。

    stack = [i1, i2, i3, ...]
    heights[i1] < heights[i2] < heights[i3] < ...

為什麼要維持這個性質？
    因為當我們遇到一根「比堆疊頂端矮」的柱子時，
    就表示堆疊頂端那根柱子的【右邊界】找到了！

    而它的【左邊界】就是堆疊裡的前一個
    （因為堆疊是遞增的，前一個一定比它矮）。

    兩個邊界都有了 -> 可以算面積 -> 彈出它。

這就是單調堆疊的核心：
    「用堆疊維持一個單調序列，
      當單調性被破壞時，就是結算的時機。」"""),
     ("h", "逐步追蹤 <code>heights = [2, 1, 5, 6, 2, 3]</code>"),
     ("c", """i=0, h=2: 堆疊空 -> push 0        stack=[0]
i=1, h=1: heights[0]=2 >= 1
            pop 0，height=2
            stack 空 -> left = -1
            width = 1 - (-1) - 1 = 1
            面積 = 2 × 1 = 2          best=2
          push 1                      stack=[1]
i=2, h=5: heights[1]=1 < 5 -> 不彈
          push 2                      stack=[1,2]
i=3, h=6: heights[2]=5 < 6 -> 不彈
          push 3                      stack=[1,2,3]
i=4, h=2: heights[3]=6 >= 2
            pop 3，height=6，left=2
            width = 4 - 2 - 1 = 1，面積 = 6      best=6
          heights[2]=5 >= 2
            pop 2，height=5，left=1
            width = 4 - 1 - 1 = 2，面積 = 10 ✔  best=10
          heights[1]=1 < 2 -> 停
          push 4                      stack=[1,4]
i=5, h=3: heights[4]=2 < 3 -> 不彈
          push 5                      stack=[1,4,5]
i=6, h=0（哨兵）:
          pop 5，height=3，left=4，width=6-4-1=1，面積 3
          pop 4，height=2，left=1，width=6-1-1=4，面積 8
          pop 1，height=1，left=-1，width=6-(-1)-1=6，面積 6
          stack 空

答案 10 ✔"""),
     ("h", "三個關鍵細節"),
     ("c", """① 迴圈跑到 n（不是 n-1），用高度 0 當哨兵

   如果不加哨兵，堆疊裡「一路遞增到底」的柱子永遠不會被結算。
       heights = [1, 2, 3]
       沒有哨兵的話，1、2、3 都留在堆疊裡，best 永遠是 0 ✘

   哨兵 0 比任何高度都矮（題目說高度 >= 0…嚴格說 0 不小於 0，
   但我們用的是 >= 的彈出條件，所以高度 0 的柱子也會被彈出）✔

   另一種寫法是在迴圈後面再加一個「清空堆疊」的迴圈，
   但那要重複寫一次面積計算的邏輯 —— 哨兵的寫法更精簡。

② left = stack[-1] if stack else -1

   彈出之後，堆疊頂端就是「左邊第一個比它矮的」。
   如果堆疊空了，表示左邊沒有更矮的 -> 可以延伸到最左邊 -> left = -1。

③ width = i - left - 1

   開區間 (left, i) 裡的柱子，高度都 >= height。
   個數 = i - left - 1。

   驗算：left=1, i=4 -> width = 2（索引 2 和 3）✔"""),
     ("h", "彈出條件用 <code>&gt;=</code> 還是 <code>&gt;</code>？"),
     ("c", """本文用 >=（相等也彈出）。

用 > 的話，等高的柱子不會互相彈出，
會導致某些柱子算出「偏小的寬度」。

    heights = [2, 2]
    用 >：i=1 時 heights[0]=2 不 > 2，不彈 -> stack=[0,1]
          i=2（哨兵 0）：pop 1，left=0，width=2-0-1=1，面積 2
                        pop 0，left=-1，width=2-(-1)-1=2，面積 4 ✔
          答案 4 ✔ —— 也對！

    為什麼也對？
        因為等高的柱子裡，「最左邊那一根」會算出正確的完整寬度。
        其他的會算出偏小的值，但不影響最大值。

所以 >= 和 > 都會得到正確答案。
>= 會多做幾次彈出（每次都算一個偏小的面積），
> 則是「只讓最左邊那根算完整寬度」。

實務上兩種都常見。用 >= 的好處是
「彈出條件」和「單調不遞減」的定義一致，比較不會搞混。"""),
     ("h", "為什麼是 O(n)？"),
     "<strong>每個索引最多被 push 一次、pop 一次。</strong>"
     "雖然內層有 while，但所有 while 的總執行次數不超過 n。"
     "<strong>這是攤還分析（amortized analysis）的標準例子</strong> —— "
     "和 KMP、以及第 42 題的單調堆疊解法同一個道理。",
   ], "O(n)", "O(n)", "每個索引 push/pop 各一次",
      "堆疊最壞有 n 個元素", optimal=True),

   ap("解法三", "分別求左右邊界（兩趟，最好理解）", [
     "把「找左邊第一個比我矮的」和「找右邊第一個比我矮的」<strong>分開做</strong>，"
     "各用一次單調堆疊，最後再一起算面積。",
     ("c", S["p84_bounds"]),
     ("c", """heights = [2, 1, 5, 6, 2, 3]

left  = [-1, -1,  1,  2,  1,  4]
right = [ 1,  6,  4,  4,  6,  6]

i=0: (1 - (-1) - 1) × 2 = 1 × 2 = 2
i=1: (6 - (-1) - 1) × 1 = 6 × 1 = 6
i=2: (4 - 1 - 1)    × 5 = 2 × 5 = 10 ✔
i=3: (4 - 2 - 1)    × 6 = 1 × 6 = 6
i=4: (6 - 1 - 1)    × 2 = 4 × 2 = 8
i=5: (6 - 4 - 1)    × 3 = 1 × 3 = 3

最大 10 ✔"""),
     "<strong>優點</strong>：把「找邊界」和「算面積」分開，"
     "每一步都很單純，而且 <code>left</code>／<code>right</code> 陣列可以印出來檢查。"
     "<strong>debug 友善得多。</strong>",
     "<strong>缺點</strong>：三趟掃描、兩個額外陣列。複雜度一樣是 O(n)。",
     "<strong>而且「求每個元素左右第一個比它小的」本身就是一個可重用的工具</strong> —— "
     "第 42、85、739、496、503 題都會用到。"
     "<strong>先學會這個版本，再學解法一的「一趟合併」。</strong>",
   ], "O(n)", "O(n)", "三趟掃描", "兩個陣列 + 堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "趟數", "備註"],
   [["一、暴力擴張", "O(n²)", "O(1)", "n", "會 TLE，當基準"],
    ["二、單調堆疊（一趟）", "O(n)", "O(n)", "1", "最精簡，面試預設"],
    ["三、左右邊界（兩趟）", "O(n)", "O(n)", "3", "最好 debug，工具可重用"]]),
 "edges": [
   "<strong>空陣列</strong>：<code>[]</code> → 0。題目保證 n ≥ 1，但別崩潰。",
   "<strong>單一柱子</strong>：<code>[1]</code> → 1；<code>[0]</code> → 0。",
   "<strong>遞增</strong>：<code>[1,2,3,4,5]</code> → 9（高 3 寬 3）。"
   "<strong>沒有哨兵的話會回傳 0。</strong>",
   "<strong>遞減</strong>：<code>[5,4,3,2,1]</code> → 9。每一步都會觸發彈出。",
   "<strong>全部等高</strong>：<code>[2,2,2]</code> → 6。驗證 <code>&gt;=</code> vs <code>&gt;</code>。",
   "<strong>含 0</strong>：<code>[3,6,5,7,4,8,1,0]</code> → 16。0 會把堆疊清空。",
   "<strong>兩根</strong>：<code>[2,4]</code> → 4。",
   "<strong>忘記哨兵</strong>：遞增序列會回傳 0 —— <strong>這是最常見的 bug。</strong>",
 ],
 "follow": [
   ("h", "追問一：二維版（最大全 1 矩形）呢？"),
   "第 85 題（Maximal Rectangle）。"
   "<strong>把二維矩陣「逐列」轉成柱狀圖，對每一列跑一次本題的演算法。</strong>",
   ("c", """matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]

第 0 列的柱狀圖： [1, 0, 1, 0, 0]   -> 最大 1
第 1 列的柱狀圖： [2, 0, 2, 1, 1]   -> 最大 3
第 2 列的柱狀圖： [3, 1, 3, 2, 2]   -> 最大 6 ✔
第 3 列的柱狀圖： [4, 0, 0, 3, 0]   -> 最大 4

「柱子的高度」= 從這一列往上，連續有幾個 1
    如果 matrix[i][j] == '1'：heights[j] += 1
    否則：                     heights[j] = 0

複雜度 O(m × n) —— 每一列 O(n)，共 m 列。

這是「把二維問題降成一維」的漂亮例子。""",),
   ("h", "追問二：單調堆疊能解哪些問題？"),
   ("c", """通用形式：
    「對每個元素，找出左邊／右邊第一個比它大（或小）的元素」

單調遞增堆疊（heights[stack] 遞增）
    -> 彈出時找到的是「第一個比它小的」
單調遞減堆疊
    -> 彈出時找到的是「第一個比它大的」

題目：
    第 42 題   接雨水            （找左右第一個更高的）
    第 84 題   柱狀圖最大矩形     （本題，找左右第一個更矮的）
    第 85 題   最大矩形          （第 84 題的二維版）
    第 496 題  下一個更大元素 I
    第 503 題  下一個更大元素 II（環形）
    第 739 題  每日溫度          （最經典的入門題）
    第 901 題  股票價格跨度
    第 907 題  子陣列的最小值之和

建議的學習順序：
    739（最單純）-> 496/503 -> 84 -> 42 -> 85

單調堆疊的三個要素：
    1. 堆疊裡存【索引】（不是值）—— 因為要算距離
    2. 維持單調性（push 前先彈出破壞單調的）
    3. 彈出的那一刻，就是「找到答案」的時刻""",),
   ("h", "追問三：有沒有不用堆疊的 O(n) 解法？"),
   "有一個用「跳躍指標」的做法：算 <code>left[i]</code> 時，"
   "如果 <code>heights[i-1] &gt;= heights[i]</code>，就直接跳到 <code>left[i-1]</code>，"
   "而不是一格一格退。"
   "<strong>攤還下來也是 O(n)</strong>，而且不用堆疊（O(1) 額外空間，不算輸出陣列）。"
   "但它的正確性論證比堆疊版更難講清楚，實務上很少用。",
   ("h", "追問四：分治法可以嗎？"),
   "可以。找到最矮的柱子，答案是三者的最大值："
   "「整個寬度 × 最矮高度」、「左半的答案」、「右半的答案」。"
   "<strong>但複雜度是 O(n log n)（用線段樹找區間最小值），"
   "而且最壞情況（遞增序列）會退化成 O(n²)</strong>（如果用線性掃描找最小值）。"
   "<strong>比單調堆疊差 —— 但它是一個很好的「換個角度」練習。</strong>",
 ],
 "related": [
   "<strong>第 85 題 Maximal Rectangle</strong> —— 二維版，直接套用本題",
   "<strong>第 42 題 Trapping Rain Water</strong> —— 同一張圖，不同的問題",
   "<strong>第 739 題 Daily Temperatures</strong> —— 單調堆疊的入門題",
   "<strong>第 496／503 題 Next Greater Element</strong> —— 單調堆疊的基本形式",
   "<strong>第 907 題 Sum of Subarray Minimums</strong> —— 同樣求「左右第一個更小的」",
 ],
 "check": [
   "為什麼「最大矩形的高度」一定等於某一根柱子的高度？",
   "哨兵（<code>i == n</code> 時用高度 0）在做什麼？拿掉的話 <code>[1,2,3]</code> 會回傳什麼？",
   "<code>width = i - left - 1</code> 為什麼要減 1？請用 <code>left=1, i=4</code> 驗算。",
   "為什麼每個索引最多被 push 和 pop 各一次？這保證了什麼？",
 ],
})
print("P84 written")
