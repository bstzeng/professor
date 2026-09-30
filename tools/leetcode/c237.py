# -*- coding: utf-8 -*-
"""第 237–242 題。"""
import random
from collections import deque
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(237)
_DQ = {"deque": deque}


# ==================== 237. Delete Node in a Linked List ====================
S["p237"] = '''class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # ★ 拿不到前一個節點 -> 把下一個節點的值複製過來，改成刪掉下一個
        node.val = node.next.val
        node.next = node.next.next'''

_p237 = S.load("p237")
for _ in range(2000):
    n = random.randrange(2, 10)
    vals = random.sample(range(-50, 50), n)
    head = to_list(vals)
    k = random.randrange(0, n - 1)          # 不會是最後一個
    nd = head
    for _ in range(k):
        nd = nd.next
    _p237.deleteNode(nd)
    assert from_list(head) == vals[:k] + vals[k + 1:]
print("P237 OK")

_P237_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">只拿到 node（值 5），拿不到前一個節點 4</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="40" width="50" height="30" fill="none" stroke="var(--text-muted)"/><text x="65" y="60" fill="var(--text)">4</text>
              <rect x="150" y="40" width="50" height="30" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="175" y="60" fill="#ff8a65">5</text>
              <rect x="260" y="40" width="50" height="30" fill="none" stroke="var(--text-muted)"/><text x="285" y="60" fill="var(--text)">1</text>
              <rect x="370" y="40" width="50" height="30" fill="none" stroke="var(--text-muted)"/><text x="395" y="60" fill="var(--text)">9</text>
              <text x="175" y="88" fill="#ff8a65" font-size="11">node</text>
            </g>
            <g stroke="var(--text-muted)"><line x1="90" y1="55" x2="146" y2="55"/><line x1="200" y1="55" x2="256" y2="55"/><line x1="310" y1="55" x2="366" y2="55"/></g>
            <text x="440" y="60" fill="var(--text-muted)" font-size="12">① 複製下一個的值</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="120" width="50" height="30" fill="none" stroke="var(--text-muted)"/><text x="65" y="140" fill="var(--text)">4</text>
              <rect x="150" y="120" width="50" height="30" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="175" y="140" fill="var(--gold)">1</text>
              <rect x="260" y="120" width="50" height="30" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/><text x="285" y="140" fill="var(--text-muted)">1</text>
              <rect x="370" y="120" width="50" height="30" fill="none" stroke="var(--text-muted)"/><text x="395" y="140" fill="var(--text)">9</text>
            </g>
            <g stroke="var(--text-muted)"><line x1="90" y1="135" x2="146" y2="135"/></g>
            <path d="M200 128 C 260 96, 330 96, 370 128" fill="none" stroke="var(--gold)"/>
            <text x="440" y="140" fill="var(--text-muted)" font-size="12">② 跳過下一個節點</text>
            <text x="20" y="186" fill="var(--text)" font-size="12">結果：4 → 1 → 9。串列「看起來」刪掉了 5，其實被移除的是原本的第三個節點。</text>'''

emit({
 "num": 237, "slug": "delete-node-in-a-linked-list",
 "en": [
   "There is a singly-linked list <code>head</code> and we want to delete a node <code>node</code> in it.",
   "You are given the node to be deleted <code>node</code>. You will <strong>not be given access</strong> to the first node of <code>head</code>.",
   "All the values of the linked list are <strong>unique</strong>, and it is guaranteed that the given node <code>node</code> is not the last node in the linked list.",
   "Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean: the value of the given node should not exist in the "
   "linked list, the number of nodes should decrease by one, and all the values before and after <code>node</code> should be in the same order.",
 ],
 "zh": [
   "有一個單向鏈結串列，我們要刪除其中的節點 <code>node</code>。",
   "你只會拿到<strong>要刪除的那個節點</strong> <code>node</code>，<strong>拿不到</strong>串列的頭節點。",
   "串列中所有值互不相同，而且保證 <code>node</code> 不是最後一個節點。",
   "「刪除」的意思是：這個值不再出現在串列中、節點數少一個、其他值的前後順序不變（不是真的從記憶體釋放）。",
 ],
 "examples": """範例 1
  輸入：head = [4,5,1,9], node = 5
  輸出：[4,1,9]

範例 2
  輸入：head = [4,5,1,9], node = 1
  輸出：[4,5,9]""",
 "constraints": [
   "節點數在 <code>[2, 1000]</code> 之間",
   "−1000 ≤ <code>Node.val</code> ≤ 1000",
   "每個節點的值互不相同",
   "<code>node</code> 在串列中，而且不是尾節點",
 ],
 "idea": [
   ("fig", _P237_FIG, "0 0 640 200"),
   ("c", """【正常刪除需要前一個節點】
    prev.next = node.next
    但我們拿不到 prev，單向串列也無法往回走。

【換個想法：讓 node「變成」下一個節點】
    1. 把下一個節點的值複製到 node
    2. 刪掉下一個節點（它的前一個就是 node，拿得到！）

【為什麼題目保證 node 不是最後一個？】
    最後一個節點沒有「下一個」可以複製 ->
    這個技巧就失效了。

【這是一個「腦筋急轉彎」】
    嚴格來說節點本身沒被刪除，是「值」被刪除了。
    如果外部有其他指標指向「原本的下一個節點」，它們會出問題。
    這也是題目特別說明「刪除」定義的原因。"""),
 ],
 "approaches": [
   ap("解法", "複製下一個節點的值，再刪除下一個", [
     ("c", S["p237"]),
   ], "O(1)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>node 是倒數第二個</strong> → <code>node.next.next</code> 是 None，照樣成立。",
   "<strong>node 是頭節點</strong> → 也成立。",
   "<strong>node 是尾節點</strong> → 題目保證不會出現。",
 ],
 "follow": [
   ("h", "實務上的問題"),
   ("c", "如果節點帶有其他資料（不只一個 val），要複製全部欄位；如果別處持有「下一個節點」的參考，它會變成懸空的孤兒。所以這個技巧只適合面試題的設定。"),
 ],
 "related": [
   "<strong>第 203 題 移除鏈結串列元素</strong> —— 有 head 的正常刪除",
   "<strong>第 19 題 刪除鏈結串列的倒數第 N 個節點</strong>",
 ],
 "check": [
   "為什麼不能直接刪除 node？",
   "為什麼題目要保證 node 不是最後一個節點？",
 ],
})


# ==================== 238. Product of Array Except Self ====================
S["p238"] = '''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        for i in range(1, n):                  # 第一趟：ans[i] = 左邊所有數的乘積
            ans[i] = ans[i - 1] * nums[i - 1]
        right = 1                              # 右邊所有數的乘積，從右往左累積
        for i in range(n - 1, -1, -1):
            ans[i] *= right                    # ★ 左邊乘積 × 右邊乘積
            right *= nums[i]
        return ans'''

S["p238_two"] = '''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n                         # left[i]  = nums[0..i-1] 的乘積
        right = [1] * n                        # right[i] = nums[i+1..n-1] 的乘積
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        return [left[i] * right[i] for i in range(n)]'''

S["p238_brute"] = '''class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return [math.prod(nums[:i] + nums[i + 1:]) for i in range(len(nums))]'''

_p238 = [S.load(x) for x in ("p238", "p238_two", "p238_brute")]
for nums, want in [([1, 2, 3, 4], [24, 12, 8, 6]), ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]), ([0, 0], [0, 0]), ([2, 3], [3, 2])]:
    for sol in _p238:
        assert sol.productExceptSelf(nums) == want
for _ in range(3000):
    nums = [random.randint(-3, 3) for _ in range(random.randrange(2, 10))]
    want = _p238[2].productExceptSelf(nums)
    for sol in _p238[:2]:
        assert sol.productExceptSelf(nums) == want
print("P238 OK")

_P238_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">ans[i] = （i 左邊全部的乘積）×（i 右邊全部的乘積）</text>
            <g font-size="14" text-anchor="middle">
              <rect x="80" y="45" width="60" height="34" fill="none" stroke="var(--accent)"/><text x="110" y="67" fill="var(--accent)">1</text>
              <rect x="140" y="45" width="60" height="34" fill="none" stroke="var(--accent)"/><text x="170" y="67" fill="var(--accent)">2</text>
              <rect x="200" y="45" width="60" height="34" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="230" y="67" fill="#ff8a65">3</text>
              <rect x="260" y="45" width="60" height="34" fill="none" stroke="var(--gold)"/><text x="290" y="67" fill="var(--gold)">4</text>
            </g>
            <text x="110" y="104" fill="var(--accent)" font-size="12">左邊乘積 = 1 × 2 = 2</text>
            <text x="270" y="104" fill="var(--gold)" font-size="12">右邊乘積 = 4</text>
            <text x="200" y="132" fill="#ff8a65" font-size="12" text-anchor="middle">ans[2] = 2 × 4 = 8</text>
            <text x="20" y="162" fill="var(--text)" font-size="12">第一趟（左 → 右）：先把「左邊乘積」存進 ans。</text>
            <text x="20" y="184" fill="var(--text)" font-size="12">第二趟（右 → 左）：用一個變數累積「右邊乘積」，乘進 ans。</text>
            <text x="20" y="214" fill="var(--gold)" font-size="12">★ 不用除法，除了輸出陣列之外只用 O(1) 空間。</text>'''

emit({
 "num": 238, "slug": "product-of-array-except-self",
 "en": [
   "Given an integer array <code>nums</code>, return an array <code>answer</code> such that <code>answer[i]</code> is equal to "
   "the product of all the elements of <code>nums</code> except <code>nums[i]</code>.",
   "The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.",
   "You must write an algorithm that runs in <code>O(n)</code> time and <strong>without using the division operation</strong>.",
   "<strong>Follow up:</strong> Can you solve the problem in <code>O(1)</code> extra space complexity? (The output array does not count as extra space.)",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，回傳陣列 <code>answer</code>，其中 <code>answer[i]</code> 等於 <code>nums</code> 中<strong>除了 <code>nums[i]</code> 以外</strong>所有元素的乘積。",
   "保證任何前綴或後綴的乘積都在 32 位元整數範圍內。",
   "必須在 <code>O(n)</code> 時間內完成，而且<strong>不能使用除法</strong>。",
   "<strong>進階：</strong>能用 <code>O(1)</code> 額外空間嗎？（輸出陣列不算）",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,4]
  輸出：[24,12,8,6]

範例 2
  輸入：nums = [-1,1,0,-3,3]
  輸出：[0,0,9,0,0]""",
 "constraints": [
   "2 ≤ <code>nums.length</code> ≤ 10⁵",
   "−30 ≤ <code>nums[i]</code> ≤ 30",
   "任何前綴或後綴的乘積都在 32 位元整數範圍內",
 ],
 "idea": [
   ("fig", _P238_FIG, "0 0 640 228"),
   ("c", """【為什麼不能用「總乘積 ÷ nums[i]」？】
    1. 題目禁止除法
    2. 有 0 的時候不能除：
       一個 0 -> 只有那個位置的答案不是 0
       兩個以上的 0 -> 全部是 0
       處理起來很麻煩

【前綴積 × 後綴積】
    answer[i] = (nums[0] × ... × nums[i-1]) × (nums[i+1] × ... × nums[n-1])
              =       prefix[i]            ×          suffix[i]

    prefix 從左往右累乘，suffix 從右往左累乘。

【O(1) 額外空間】
    先把 prefix 直接存在 answer 裡，
    第二趟從右往左，用一個變數 right 累積 suffix，
    邊走邊乘進 answer ✔"""),
 ],
 "approaches": [
   ap("解法一", "暴力", [
     ("c", S["p238_brute"]),
   ], "O(n²)", "O(n)", "", ""),

   ap("解法二", "前綴積陣列 + 後綴積陣列", [
     ("c", S["p238_two"]),
   ], "O(n)", "O(n)", "", "兩個輔助陣列"),

   ap("解法三", "輸出陣列當前綴積 + 一個變數當後綴積", [
     ("c", S["p238"]),
   ], "O(n)", "O(1)", "", "不計輸出陣列", optimal=True),
 ],
 "compare": (["解法", "時間", "額外空間"],
   [["一、暴力", "O(n²)", "O(n)"],
    ["二、前綴 + 後綴陣列", "O(n)", "O(n)"],
    ["三、就地", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>一個 0</strong> → 只有 0 所在的位置有非零答案。",
   "<strong>兩個以上的 0</strong> → 全部是 0。這兩種情況前綴後綴法自然處理，不用特判。",
   "<strong>負數</strong> → 乘法照常。",
   "<strong>長度 2</strong> → 答案是兩個數交換。",
 ],
 "follow": [
   ("h", "「前綴 + 後綴」的套路還能用在哪？"),
   ("c", "第 42 題接雨水（左邊最高 × 右邊最高）、第 135 題分發糖果（左右各掃一次）、第 2256 題最小平均差——只要答案取決於「左邊全部」和「右邊全部」，就可以兩趟掃描。"),
 ],
 "related": [
   "<strong>第 42 題 接雨水</strong>",
   "<strong>第 152 題 乘積最大子陣列</strong>",
   "<strong>第 724 題 尋找陣列的中心索引</strong> —— 前綴和版本",
 ],
 "check": [
   "為什麼不用「總乘積除以 nums[i]」？",
   "answer[i] 可以拆成哪兩部分的乘積？",
   "怎麼做到 O(1) 額外空間？",
 ],
})


# ==================== 239. Sliding Window Maximum ====================
S["p239"] = '''class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()                   # 存索引；對應的值從隊頭到隊尾「遞減」
        ans = []
        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] <= x:     # ★ 比 x 小的舊元素，永遠不可能再當最大值
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:                  # 隊頭已經滑出視窗
                dq.popleft()
            if i >= k - 1:
                ans.append(nums[dq[0]])         # 隊頭 = 視窗最大值
        return ans'''

S["p239_heap"] = '''class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []                      # (-值, 索引)：最大堆積
        ans = []
        for i, x in enumerate(nums):
            heapq.heappush(heap, (-x, i))
            if i >= k - 1:
                while heap[0][1] <= i - k:      # 延遲刪除：堆頂不在視窗內才丟掉
                    heapq.heappop(heap)
                ans.append(-heap[0][0])
        return ans'''

S["p239_block"] = '''class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        left = [0] * n                 # left[i]：i 所在的區塊中，從區塊開頭到 i 的最大值
        right = [0] * n                # right[i]：從 i 到所在區塊結尾的最大值
        for i in range(n):
            left[i] = nums[i] if i % k == 0 else max(left[i - 1], nums[i])
        for i in range(n - 1, -1, -1):
            right[i] = nums[i] if i == n - 1 or (i + 1) % k == 0 else max(right[i + 1], nums[i])
        # 視窗 [i, i+k-1] 最多跨兩個區塊：right[i] 管前半，left[i+k-1] 管後半
        return [max(right[i], left[i + k - 1]) for i in range(n - k + 1)]'''

S["p239_brute"] = '''class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]'''

_p239 = [S.load("p239", extra=_DQ)] + [S.load(x) for x in ("p239_heap", "p239_block", "p239_brute")]
for nums, k, want in [([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]), ([1], 1, [1]), ([9, 8, 7], 3, [9]), ([1, -1], 1, [1, -1])]:
    for sol in _p239:
        assert sol.maxSlidingWindow(nums, k) == want
for _ in range(3000):
    nums = [random.randint(-5, 5) for _ in range(random.randrange(1, 16))]
    k = random.randrange(1, len(nums) + 1)
    want = _p239[3].maxSlidingWindow(nums, k)
    for sol in _p239[:3]:
        assert sol.maxSlidingWindow(nums, k) == want, (nums, k, sol)
print("P239 OK")

_P239_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">單調遞減佇列：nums = [1, 3, −1, −3, 5, 3, 6, 7]，k = 3</text>
            <g font-size="12">
              <text x="30" y="52" fill="var(--text-muted)">i</text><text x="56" y="52" fill="var(--text-muted)">x</text><text x="92" y="52" fill="var(--text-muted)">處理後的佇列（值）</text><text x="330" y="52" fill="var(--text-muted)">視窗最大</text>
              <text x="30" y="72" fill="var(--text)">0</text><text x="56" y="72" fill="var(--text)">1</text><text x="92" y="72" fill="var(--text)">[1]</text>
              <text x="30" y="92" fill="var(--text)">1</text><text x="56" y="92" fill="var(--text)">3</text><text x="92" y="92" fill="var(--text)">[3]</text><text x="200" y="92" fill="var(--text-muted)">← 1 被 3 踢掉</text>
              <text x="30" y="112" fill="var(--text)">2</text><text x="56" y="112" fill="var(--text)">-1</text><text x="92" y="112" fill="var(--text)">[3, -1]</text><text x="330" y="112" fill="var(--gold)">3</text>
              <text x="30" y="132" fill="var(--text)">3</text><text x="56" y="132" fill="var(--text)">-3</text><text x="92" y="132" fill="var(--text)">[3, -1, -3]</text><text x="330" y="132" fill="var(--gold)">3</text>
              <text x="30" y="152" fill="var(--text)">4</text><text x="56" y="152" fill="var(--text)">5</text><text x="92" y="152" fill="var(--text)">[5]</text><text x="200" y="152" fill="var(--text-muted)">← 全部被 5 踢掉</text><text x="330" y="152" fill="var(--gold)">5</text>
              <text x="30" y="172" fill="var(--text)">5</text><text x="56" y="172" fill="var(--text)">3</text><text x="92" y="172" fill="var(--text)">[5, 3]</text><text x="330" y="172" fill="var(--gold)">5</text>
              <text x="30" y="192" fill="var(--text)">6</text><text x="56" y="192" fill="var(--text)">6</text><text x="92" y="192" fill="var(--text)">[6]</text><text x="330" y="192" fill="var(--gold)">6</text>
              <text x="30" y="212" fill="var(--text)">7</text><text x="56" y="212" fill="var(--text)">7</text><text x="92" y="212" fill="var(--text)">[7]</text><text x="330" y="212" fill="var(--gold)">7</text>
            </g>
            <text x="400" y="80" fill="var(--text)" font-size="12">★ 新來的 x 比隊尾大：</text>
            <text x="400" y="100" fill="var(--text-muted)" font-size="12">隊尾比 x 早進、比 x 小，</text>
            <text x="400" y="120" fill="var(--text-muted)" font-size="12">又會比 x 早離開視窗 ——</text>
            <text x="400" y="140" fill="var(--text-muted)" font-size="12">它永遠不會再是最大值。</text>
            <text x="400" y="176" fill="var(--text)" font-size="12">★ 隊頭索引滑出視窗：</text>
            <text x="400" y="196" fill="var(--text-muted)" font-size="12">從隊頭移除。</text>'''

emit({
 "num": 239, "slug": "sliding-window-maximum",
 "en": [
   "You are given an array of integers <code>nums</code>, there is a sliding window of size <code>k</code> which is moving from "
   "the very left of the array to the very right. You can only see the <code>k</code> numbers in the window. Each time the sliding window moves right by one position.",
   "Return <em>the max sliding window</em>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，有一個大小為 <code>k</code> 的滑動視窗從最左邊移動到最右邊，每次向右移動一格。",
   "回傳每個位置上視窗內的<strong>最大值</strong>。",
 ],
 "examples": """範例 1
  輸入：nums = [1,3,-1,-3,5,3,6,7], k = 3
  輸出：[3,3,5,5,6,7]
  說明：
    視窗位置                  最大值
    [1  3  -1] -3  5  3  6  7    3
     1 [3  -1  -3] 5  3  6  7    3
     1  3 [-1  -3  5] 3  6  7    5
     1  3  -1 [-3  5  3] 6  7    5
     1  3  -1  -3 [5  3  6] 7    6
     1  3  -1  -3  5 [3  6  7]   7

範例 2
  輸入：nums = [1], k = 1
  輸出：[1]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
   "1 ≤ <code>k</code> ≤ <code>nums.length</code>",
 ],
 "idea": [
   ("fig", _P239_FIG, "0 0 640 228"),
   ("c", """【暴力 O(nk) 太慢：每個視窗都重新找最大】

【關鍵觀察：有些元素永遠不可能是最大值】
    如果 j < i 而且 nums[j] <= nums[i]：
        j 比 i 早離開視窗、值又不比 i 大
        -> 只要 i 在視窗裡，j 就沒機會當最大值
        -> j 可以直接丟掉

【單調遞減佇列（deque）】
    佇列存索引，對應的值從隊頭到隊尾嚴格遞減。
    新元素 x 進來：
        1. 從隊尾踢掉所有 <= x 的（它們沒用了）
        2. x 從隊尾加入
        3. 隊頭如果已經滑出視窗，從隊頭移除
        4. 隊頭就是目前視窗的最大值

【為什麼是 O(n)？】
    每個索引最多進佇列一次、出佇列一次 -> 總共 O(n)。
    雖然有 while 迴圈，但是攤銷後每個元素 O(1)。

【為什麼存索引而不是值？】
    要判斷隊頭是否已經滑出視窗，需要知道它的位置。"""),
 ],
 "approaches": [
   ap("解法一", "暴力", [
     ("c", S["p239_brute"]),
   ], "O(nk)", "O(1)", "", "不計輸出"),

   ap("解法二", "最大堆積 + 延遲刪除", [
     ("c", S["p239_heap"]),
     "堆積裡可能留著已經滑出視窗的元素，只在它們跑到堆頂時才丟掉。最壞堆積大小 O(n)（例如遞增陣列）。",
   ], "O(n log n)", "O(n)", "", ""),

   ap("解法三", "分塊前後綴最大值", [
     ("c", S["p239_block"]),
     ("c", """【把陣列切成每 k 個一塊】
    任何長度 k 的視窗，最多跨越兩個區塊：
        前半段 = 某區塊的「後綴」-> right[i]
        後半段 = 下一區塊的「前綴」-> left[i+k-1]
    視窗最大值 = max(right[i], left[i+k-1])

    剛好對齊區塊時，right[i] 就是整塊的最大值，
    left[i+k-1] 也是同一塊的最大值，一樣正確。
    這個方法不需要任何資料結構，只要三趟掃描。"""),
   ], "O(n)", "O(n)", "", ""),

   ap("解法四", "單調佇列", [
     ("c", S["p239"]),
   ], "O(n)", "O(k)", "", "佇列最多 k 個", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、暴力", "O(nk)", "O(1)", "超時"],
    ["二、堆積", "O(n log n)", "O(n)", "直觀"],
    ["三、分塊", "O(n)", "O(n)", "巧妙，沒有資料結構"],
    ["四、單調佇列", "O(n)", "O(k)", "經典 ✔"]]),
 "edges": [
   "<strong>k = 1</strong> → 答案就是原陣列。",
   "<strong>k = n</strong> → 只有一個視窗，答案是整個陣列的最大值。",
   "<strong>遞減陣列</strong> → 佇列會長到 k，隊頭不斷滑出。",
   "<strong>重複值</strong> → 用 <code>&lt;=</code> 踢掉相同的舊值（留新的，比較晚離開）。用 <code>&lt;</code> 也對，只是佇列比較長。",
 ],
 "follow": [
   ("h", "單調佇列 vs 單調堆疊"),
   ("c", """單調堆疊（第 739、496 題）：只從一端進出，用來找「下一個更大的元素」。
單調佇列：兩端都要操作——隊尾維持單調、隊頭處理過期——用來求「滑動視窗的極值」。
進階應用：第 1696 題、第 862 題，用單調佇列優化 DP。"""),
 ],
 "related": [
   "<strong>第 155 題 最小堆疊</strong>",
   "<strong>第 1438 題 絕對差不超過限制的最長連續子陣列</strong> —— 兩個單調佇列",
   "<strong>第 862 題 和至少為 K 的最短子陣列</strong>",
   "<strong>第 1696 題 跳躍遊戲 VI</strong> —— 單調佇列優化 DP",
 ],
 "check": [
   "為什麼比新元素小的舊元素可以直接丟掉？",
   "佇列裡為什麼存索引而不是值？",
   "為什麼雖然有 while 迴圈，總時間仍是 O(n)？",
   "分塊法中，為什麼視窗最大值 = max(right[i], left[i+k−1])？",
 ],
})


# ==================== 240. Search a 2D Matrix II ====================
S["p240"] = '''class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        r, c = 0, n - 1                        # ★ 從右上角出發
        while r < m and c >= 0:
            v = matrix[r][c]
            if v == target:
                return True
            if v > target:                     # 這一欄往下都更大 -> 整欄排除
                c -= 1
            else:                              # 這一列往左都更小 -> 整列排除
                r += 1
        return False'''

S["p240_bs"] = '''class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:                     # 每一列各自二分搜尋
            i = bisect.bisect_left(row, target)
            if i < len(row) and row[i] == target:
                return True
        return False'''

_p240 = [S.load(x) for x in ("p240", "p240_bs")]
M = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
for t, want in [(5, True), (20, False), (30, True), (1, True), (0, False)]:
    for sol in _p240:
        assert sol.searchMatrix(M, t) == want
for _ in range(1500):
    m, n = random.randrange(1, 7), random.randrange(1, 7)
    mat = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            mat[i][j] = max(mat[i - 1][j] if i else -5, mat[i][j - 1] if j else -5) + random.randrange(0, 3)
    for t in range(-6, 30):
        want = any(t in row for row in mat)
        for sol in _p240:
            assert sol.searchMatrix(mat, t) == want
print("P240 OK")

_P240_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">從右上角出發，找 target = 5</text>
            <g font-size="13" text-anchor="middle">
              <g fill="none" stroke="var(--border)">
                <rect x="40" y="40" width="200" height="200"/>
                <line x1="80" y1="40" x2="80" y2="240"/><line x1="120" y1="40" x2="120" y2="240"/><line x1="160" y1="40" x2="160" y2="240"/><line x1="200" y1="40" x2="200" y2="240"/>
                <line x1="40" y1="80" x2="240" y2="80"/><line x1="40" y1="120" x2="240" y2="120"/><line x1="40" y1="160" x2="240" y2="160"/><line x1="40" y1="200" x2="240" y2="200"/>
              </g>
              <rect x="120" y="40" width="120" height="200" fill="var(--text-muted)" opacity="0.12"/>
              <text x="60" y="65" fill="var(--text)">1</text><text x="100" y="65" fill="var(--text)">4</text><text x="140" y="65" fill="#ff8a65">7</text><text x="180" y="65" fill="#ff8a65">11</text><text x="220" y="65" fill="#ff8a65">15</text>
              <text x="60" y="105" fill="var(--text)">2</text><text x="100" y="105" fill="var(--gold)">5</text><text x="140" y="105" fill="var(--text-muted)">8</text><text x="180" y="105" fill="var(--text-muted)">12</text><text x="220" y="105" fill="var(--text-muted)">19</text>
              <text x="60" y="145" fill="var(--text)">3</text><text x="100" y="145" fill="var(--text)">6</text><text x="140" y="145" fill="var(--text-muted)">9</text><text x="180" y="145" fill="var(--text-muted)">16</text><text x="220" y="145" fill="var(--text-muted)">22</text>
              <text x="60" y="185" fill="var(--text)">10</text><text x="100" y="185" fill="var(--text)">13</text><text x="140" y="185" fill="var(--text-muted)">14</text><text x="180" y="185" fill="var(--text-muted)">17</text><text x="220" y="185" fill="var(--text-muted)">24</text>
              <text x="60" y="225" fill="var(--text)">18</text><text x="100" y="225" fill="var(--text)">21</text><text x="140" y="225" fill="var(--text-muted)">23</text><text x="180" y="225" fill="var(--text-muted)">26</text><text x="220" y="225" fill="var(--text-muted)">30</text>
            </g>
            <g font-size="12">
              <text x="270" y="60" fill="#ff8a65">15 &gt; 5 → 15 以下整欄都更大，往左</text>
              <text x="270" y="82" fill="#ff8a65">11 &gt; 5 → 往左</text>
              <text x="270" y="104" fill="#ff8a65">7 &gt; 5 → 往左（灰色三欄已排除）</text>
              <text x="270" y="126" fill="var(--text)">4 &lt; 5 → 4 左邊整列都更小，往下</text>
              <text x="270" y="148" fill="var(--gold)">5 == 5 → 找到 ✔</text>
              <text x="270" y="190" fill="var(--text-muted)">每一步排除一整列或一整欄，</text>
              <text x="270" y="210" fill="var(--text-muted)">最多走 m + n 步。</text>
            </g>'''

emit({
 "num": 240, "slug": "search-a-2d-matrix-ii",
 "en": [
   "Write an efficient algorithm that searches for a value <code>target</code> in an <code>m x n</code> integer matrix <code>matrix</code>. This matrix has the following properties:",
   ("ul", ["Integers in each row are sorted in ascending from left to right.",
           "Integers in each column are sorted in ascending from top to bottom."]),
 ],
 "zh": [
   "在 <code>m x n</code> 的整數矩陣 <code>matrix</code> 中搜尋 <code>target</code>。矩陣有以下性質：",
   ("ul", ["每一列由左到右遞增。",
           "每一欄由上到下遞增。"]),
   "注意：和第 74 題不同，下一列的開頭<strong>不一定</strong>比上一列的結尾大。",
 ],
 "examples": """範例 1
  輸入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
  輸出：true

範例 2
  輸入：同上, target = 20
  輸出：false""",
 "constraints": [
   "1 ≤ <code>m, n</code> ≤ 300",
   "−10⁹ ≤ <code>matrix[i][j]</code> ≤ 10⁹",
   "每一列、每一欄都是遞增的",
   "−10⁹ ≤ <code>target</code> ≤ 10⁹",
 ],
 "idea": [
   ("fig", _P240_FIG, "0 0 640 250"),
   ("c", """【為什麼從右上角出發？】
    右上角的值，是「這一列最大」也是「這一欄最小」。
    和 target 比較後，一定能排除一整列或一整欄：
        v > target -> 這一欄往下全部 >= v > target，整欄排除，往左
        v < target -> 這一列往左全部 <= v < target，整列排除，往下

【左上角為什麼不行？】
    左上角是列最小、也是欄最小 ->
    v < target 時，往右、往下都可能 -> 無法決定方向 ✘
    （左下角也可以，對稱的道理。）

【這其實是一棵 BST】
    把右上角當根：往左 = 變小，往下 = 變大。"""),
 ],
 "approaches": [
   ap("解法一", "每一列二分搜尋", [
     ("c", S["p240_bs"]),
   ], "O(m log n)", "O(1)", "", ""),

   ap("解法二", "從右上角走階梯", [
     ("c", S["p240"]),
   ], "O(m + n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、逐列二分", "O(m log n)", "O(1)"],
    ["二、右上角階梯", "O(m + n)", "O(1) ✔"]]),
 "edges": [
   "<strong>target 比全部都小或都大</strong> → 很快走出邊界。",
   "<strong>只有一列或一欄</strong> → 退化成線性掃描（或二分）。",
   "<strong>重複值</strong> → 不影響正確性。",
 ],
 "follow": [
   ("h", "第 74 題 vs 第 240 題"),
   ("c", "第 74 題：整個矩陣「攤平」後是排序的 → 當成一維陣列二分，O(log mn)。本題只有列、欄分別排序 → 階梯走法 O(m + n)。"),
   ("h", "延伸：在這種矩陣中找第 k 小？"),
   ("c", "第 378 題：對「值」二分，每次用同樣的階梯走法 O(m + n) 數出 ≤ mid 的個數。"),
 ],
 "related": [
   "<strong>第 74 題 搜尋二維矩陣</strong>",
   "<strong>第 378 題 有序矩陣中第 K 小的元素</strong>",
   "<strong>第 1351 題 統計有序矩陣中的負數</strong> —— 同一種階梯走法",
 ],
 "check": [
   "為什麼要從右上角（或左下角）出發？",
   "每一步能排除什麼？",
   "時間複雜度為什麼是 O(m + n)？",
 ],
})


# ==================== 241. Different Ways to Add Parentheses ====================
S["p241"] = '''class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @functools.lru_cache(None)
        def solve(expr: str) -> List[int]:
            if expr.isdigit():                        # 純數字：只有一種結果
                return [int(expr)]
            res = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    # ★ 把 ch 當作「最後才算」的運算子，左右兩邊分別遞迴
                    for a in solve(expr[:i]):
                        for b in solve(expr[i + 1:]):
                            res.append(a + b if ch == "+" else a - b if ch == "-" else a * b)
            return res

        return solve(expression)'''

S["p241_dp"] = '''class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums, ops = [], []                        # 先切成數字與運算子
        for tok in re.findall(r"\\d+|[-+*]", expression):
            (ops if tok in "+-*" else nums).append(tok)
        nums = list(map(int, nums))
        n = len(nums)
        # dp[i][j]：第 i 到第 j 個數字之間，所有可能的結果
        dp = [[[] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = [nums[i]]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                for k in range(i, j):              # ops[k] 是最後算的
                    op = ops[k]
                    for a in dp[i][k]:
                        for b in dp[k + 1][j]:
                            dp[i][j].append(a + b if op == "+" else a - b if op == "-" else a * b)
        return dp[0][n - 1]'''

_p241 = [S.load(x) for x in ("p241", "p241_dp")]
for e, want in [("2-1-1", [0, 2]), ("2*3-4*5", [-34, -14, -10, -10, 10]), ("11", [11]), ("1+2", [3])]:
    for sol in _p241:
        assert sorted(sol.diffWaysToCompute(e)) == sorted(want), (e, sol)
for _ in range(400):
    k = random.randrange(1, 7)
    e = str(random.randrange(0, 12))
    for _ in range(k - 1):
        e += random.choice("+-*") + str(random.randrange(0, 12))
    a, b = (sorted(sol.diffWaysToCompute(e)) for sol in _p241)
    assert a == b, e
    cat = [1, 1, 2, 5, 14, 42, 132]
    assert len(a) == cat[k - 1]
print("P241 OK")

emit({
 "num": 241, "slug": "different-ways-to-add-parentheses",
 "en": [
   "Given a string <code>expression</code> of numbers and operators, return all possible results from computing all the different possible ways "
   "to group numbers and operators. You may return the answer in <strong>any order</strong>.",
   "The test cases are generated such that the output values fit in a 32-bit integer and the number of different results does not exceed <code>10<sup>4</sup></code>.",
 ],
 "zh": [
   "給你一個由數字和運算子組成的字串 <code>expression</code>，用所有不同的方式加上括號（決定運算順序），回傳所有可能的計算結果，順序不限。",
   "保證結果在 32 位元整數範圍內，而且結果的個數不超過 <code>10<sup>4</sup></code>。",
 ],
 "examples": """範例 1
  輸入：expression = "2-1-1"
  輸出：[0,2]
  說明：
    ((2-1)-1) = 0
    (2-(1-1)) = 2

範例 2
  輸入：expression = "2*3-4*5"
  輸出：[-34,-14,-10,-10,10]
  說明：
    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10""",
 "constraints": [
   "1 ≤ <code>expression.length</code> ≤ 20",
   "<code>expression</code> 由數字與 <code>'+'</code>、<code>'-'</code>、<code>'*'</code> 組成",
   "所有整數都在 [0, 99] 之間",
   "整數不會有前導的 <code>'-'</code> 或 <code>'+'</code>",
 ],
 "idea": [
   ("c", """【分治：選一個運算子「最後才算」】
    任何一種加括號的方式，總有一個運算子是「最外層」、最後才算的。
    2 * 3 - 4 * 5
          ^ 如果 '-' 最後算：
    (2 * 3 的所有可能結果) - (4 * 5 的所有可能結果)

    左半、右半各自是同樣的子問題 -> 遞迴。
    兩邊的結果兩兩組合。

【結果的個數】
    n 個數字的加括號方式有 Catalan(n-1) 種：
        1, 1, 2, 5, 14, 42, 132, 429, ...
    題目說結果不超過 10⁴，所以可以全部列出來。

【重複的結果要保留】
    範例 2 中 -10 出現兩次（兩種不同的括號方式）。

【記憶化】
    同一個子字串可能被算很多次 ->
    用 lru_cache 或以 (i, j) 為狀態的區間 DP。"""),
 ],
 "approaches": [
   ap("解法一", "分治遞迴 + 記憶化", [
     ("c", S["p241"]),
   ], "O(Catalan 數)", "O(Catalan 數)", "輸出本身就這麼多", "", optimal=True),

   ap("解法二", "區間 DP", [
     ("c", S["p241_dp"]),
     ("c", """【和第 312 題戳氣球、矩陣連乘是同一類】
    dp[i][j] = 第 i..j 個數字能算出的所有結果
    枚舉最後算的運算子 k（介於第 k 和 k+1 個數字之間）：
        dp[i][j] += dp[i][k] ⊗ dp[k+1][j]
    按區間長度由短到長填表。"""),
   ], "O(Catalan 數)", "O(Catalan 數)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、分治 + 記憶化", "O(Catalan)", "最自然 ✔"],
    ["二、區間 DP", "O(Catalan)", "先切 token，避免字串切片"]]),
 "edges": [
   "<strong>只有一個數字</strong>（<code>\"11\"</code>）→ <code>[11]</code>。",
   "<strong>多位數</strong> → 遞迴基底用 <code>isdigit()</code> 判斷整段都是數字。",
   "<strong>重複結果</strong> → 要保留，不能去重。",
 ],
 "follow": [
   ("h", "追問：如果只要最大值？"),
   ("c", "區間 DP 只存每段的最大值與最小值（減法和乘法遇到負數時，最小值可能變最大值）——這就是很多「加括號求最大值」問題的套路。"),
 ],
 "related": [
   "<strong>第 95 題 不同的二元搜尋樹 II</strong> —— 同一種「選根 / 選最後的運算子」分治",
   "<strong>第 282 題 給表達式添加運算子</strong>",
   "<strong>第 312 題 戳氣球</strong> —— 區間 DP",
 ],
 "check": [
   "為什麼要選一個「最後才算」的運算子？",
   "n 個數字共有幾種加括號的方式？",
   "為什麼重複的結果不能去掉？",
 ],
})


# ==================== 242. Valid Anagram ====================
S["p242_count"] = '''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = [0] * 26
        for a, b in zip(s, t):              # s 的字母 +1，t 的字母 -1
            cnt[ord(a) - 97] += 1
            cnt[ord(b) - 97] -= 1
        return all(c == 0 for c in cnt)     # ★ 全部抵銷 = 字母組成相同'''

S["p242_counter"] = '''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)   # 也適用於 Unicode'''

S["p242_sort"] = '''class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)'''

_p242 = [S.load(x) for x in ("p242_count", "p242_counter", "p242_sort")]
for s, t, want in [("anagram", "nagaram", True), ("rat", "car", False), ("a", "ab", False), ("ab", "ba", True)]:
    for sol in _p242:
        assert sol.isAnagram(s, t) == want
for _ in range(3000):
    s = "".join(random.choice("abc") for _ in range(random.randrange(1, 8)))
    t = "".join(random.sample(s, len(s))) if random.random() < 0.5 else "".join(random.choice("abc") for _ in range(random.randrange(1, 8)))
    want = sorted(s) == sorted(t)
    for sol in _p242:
        assert sol.isAnagram(s, t) == want
print("P242 OK")

emit({
 "num": 242, "slug": "valid-anagram",
 "en": [
   "Given two strings <code>s</code> and <code>t</code>, return <code>true</code> if <code>t</code> is an anagram of <code>s</code>, and <code>false</code> otherwise.",
   "An <strong>anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.",
   "<strong>Follow up:</strong> What if the inputs contain Unicode characters? How would you adapt your solution to such a case?",
 ],
 "zh": [
   "給你兩個字串 <code>s</code> 和 <code>t</code>，判斷 <code>t</code> 是不是 <code>s</code> 的<strong>字母異位詞</strong>。",
   "字母異位詞：把一個字串的字母重新排列得到的字串，每個字母恰好用一次。",
   "<strong>進階：</strong>如果輸入包含 Unicode 字元，要怎麼調整？",
 ],
 "examples": """範例 1
  輸入：s = "anagram", t = "nagaram"
  輸出：true

範例 2
  輸入：s = "rat", t = "car"
  輸出：false""",
 "constraints": [
   "1 ≤ <code>s.length, t.length</code> ≤ 5 × 10⁴",
   "<code>s</code> 和 <code>t</code> 只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【異位詞 = 每個字母出現的次數完全相同】
    順序無關，只看「字母組成」。

【方法一：排序】
    兩個字串排序後相同 <=> 互為異位詞。

【方法二：計數】
    只有 26 個小寫字母 -> 長度 26 的陣列。
    s 的字母 +1、t 的字母 -1，
    最後全部為 0 就代表組成相同。

【先比長度】
    長度不同一定不是，直接回傳 false。

【Unicode 進階】
    字元種類太多，不能用固定長度的陣列 ->
    改用雜湊表（Counter / dict）。
    另外要注意：有些字元可以用不同的碼位序列表示
    （例如 é 可以是一個字元，也可以是 e + 組合重音），
    嚴謹的比較要先做 Unicode 正規化（unicodedata.normalize）。"""),
 ],
 "approaches": [
   ap("解法一", "排序比較", [
     ("c", S["p242_sort"]),
   ], "O(n log n)", "O(n)", "", "sorted 產生新串列"),

   ap("解法二", "26 格計數陣列", [
     ("c", S["p242_count"]),
   ], "O(n)", "O(1)", "", "固定 26 格", optimal=True),

   ap("解法三", "雜湊計數（Counter）", [
     ("c", S["p242_counter"]),
   ], "O(n)", "O(k)", "", "k = 字元種類，適用 Unicode"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、排序", "O(n log n)", "O(n)", "最簡單"],
    ["二、26 格陣列", "O(n)", "O(1)", "只限小寫字母 ✔"],
    ["三、Counter", "O(n)", "O(k)", "Unicode 也適用"]]),
 "edges": [
   "<strong>長度不同</strong> → 直接 false。",
   "<strong>相同的字串</strong> → true（自己是自己的異位詞）。",
   "<strong>重複字母</strong>（<code>\"aab\"</code> vs <code>\"abb\"</code>）→ 次數不同，false。",
 ],
 "follow": [
   ("h", "延伸：把一堆字串依異位詞分組？"),
   ("c", "第 49 題：以「排序後的字串」或「26 格計數的 tuple」當雜湊表的鍵。"),
 ],
 "related": [
   "<strong>第 49 題 字母異位詞分組</strong>",
   "<strong>第 438 題 找到字串中所有字母異位詞</strong> —— 滑動視窗 + 計數",
   "<strong>第 383 題 贖金信</strong>",
 ],
 "check": [
   "異位詞的本質是什麼？",
   "計數法中，為什麼 s 加一、t 減一，最後全部為 0 就代表是異位詞？",
   "輸入有 Unicode 時要怎麼改？",
 ],
})
