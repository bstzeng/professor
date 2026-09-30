# -*- coding: utf-8 -*-
"""第 283、284、287、289、290、292 題。"""
import random
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(283)


# ==================== 283. Move Zeroes ====================
S["p283"] = '''class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0                                  # 下一個非零元素要放的位置
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # ★ 交換：非零往前、零往後；順序保持不變
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1'''

S["p283_fill"] = '''class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0
        for x in nums:                            # 第一趟：把非零元素依序往前搬
            if x != 0:
                nums[slow] = x
                slow += 1
        for i in range(slow, len(nums)):          # 第二趟：剩下的位置補 0
            nums[i] = 0'''

_p283 = [S.load(x) for x in ("p283", "p283_fill")]
for _ in range(3000):
    a = [random.choice([0, 0, 1, 2, 3, -1]) for _ in range(random.randrange(1, 12))]
    want = [x for x in a if x] + [0] * a.count(0)
    for sol in _p283:
        b = list(a)
        sol.moveZeroes(b)
        assert b == want
print("P283 OK")

emit({
 "num": 283, "slug": "move-zeroes",
 "en": [
   "Given an integer array <code>nums</code>, move all <code>0</code>'s to the end of it while maintaining the relative order of the non-zero elements.",
   "<strong>Note</strong> that you must do this in-place without making a copy of the array.",
   "<strong>Follow up:</strong> Could you minimize the total number of operations done?",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，把所有 <code>0</code> 移到陣列末尾，同時保持非零元素的<strong>相對順序</strong>。",
   "必須<strong>原地</strong>修改，不能複製陣列。",
   "<strong>進階：</strong>能盡量減少操作次數嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [0,1,0,3,12]
  輸出：[1,3,12,0,0]

範例 2
  輸入：nums = [0]
  輸出：[0]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁴",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【快慢指標】
    fast 掃過每一個元素；
    slow 指向「下一個非零元素該放的位置」。
    fast 遇到非零 -> 放到 slow，slow 前進。

【兩種寫法】
    覆蓋 + 補零：先把非零元素往前搬，最後剩下的全部填 0。
    交換：nums[slow] 和 nums[fast] 交換，零自然被換到後面。

【為什麼順序不變？】
    非零元素按照 fast 掃描的順序依序放到 slow，
    slow 只會往前，所以相對順序保持。

【減少寫入次數（進階）】
    陣列裡零很少時，交換版會對每個非零元素都寫一次（即使 slow == fast）。
    可以加上 if slow != fast 才交換，減少不必要的寫入。

【模擬】[0, 1, 0, 3, 12]
    fast=1: 1 和 nums[0] 交換 -> [1, 0, 0, 3, 12], slow=1
    fast=3: 3 和 nums[1] 交換 -> [1, 3, 0, 0, 12], slow=2
    fast=4: 12 和 nums[2] 交換 -> [1, 3, 12, 0, 0] ✔"""),
 ],
 "approaches": [
   ap("解法一", "搬移非零元素，最後補 0", [
     ("c", S["p283_fill"]),
   ], "O(n)", "O(1)", "", ""),

   ap("解法二", "快慢指標交換", [
     ("c", S["p283"]),
   ], "O(n)", "O(1)", "一趟", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "寫入次數"],
   [["一、搬移 + 補 0", "O(n)", "O(1)", "n 次"],
    ["二、交換", "O(n)", "O(1)", "2 × 非零個數 ✔"]]),
 "edges": [
   "<strong>沒有 0</strong> → 陣列不變。",
   "<strong>全部是 0</strong> → 陣列不變。",
   "<strong>0 都已經在最後</strong> → 不變。",
 ],
 "follow": [
   ("h", "同一個模板"),
   ("c", "第 27 題「移除元素」、第 26 題「刪除有序陣列中的重複項」都是「slow 指向下一個要寫入的位置」的快慢指標。"),
 ],
 "related": [
   "<strong>第 27 題 移除元素</strong>",
   "<strong>第 26 題 刪除有序陣列中的重複項</strong>",
   "<strong>第 75 題 顏色分類</strong> —— 三向切分",
 ],
 "check": [
   "slow 指標代表什麼？",
   "為什麼這個做法能保持非零元素的相對順序？",
 ],
})


# ==================== 284. Peeking Iterator ====================
class _Iterator:
    def __init__(self, nums):
        self._a, self._i = nums, 0

    def hasNext(self):
        return self._i < len(self._a)

    def next(self):
        self._i += 1
        return self._a[self._i - 1]


S["p284"] = '''# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums): ...
#     def hasNext(self) -> bool: ...
#     def next(self) -> int: ...

class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self.has = iterator.hasNext()
        self.nxt = iterator.next() if self.has else None   # ★ 永遠預先拿好下一個

    def peek(self):
        return self.nxt

    def next(self):
        val = self.nxt
        self.has = self.it.hasNext()
        self.nxt = self.it.next() if self.has else None     # 補上下一個
        return val

    def hasNext(self):
        return self.has'''

S["p284_flag"] = '''class PeekingIterator:
    def __init__(self, iterator):
        self.it = iterator
        self.cached = False              # 有沒有「偷看過、但還沒被 next 拿走」的元素
        self.value = None

    def peek(self):
        if not self.cached:              # 需要時才偷看
            self.value = self.it.next()
            self.cached = True
        return self.value

    def next(self):
        if self.cached:
            self.cached = False
            return self.value
        return self.it.next()

    def hasNext(self):
        return self.cached or self.it.hasNext()'''

for key in ("p284", "p284_flag"):
    cls = S.loadns(key, {"Iterator": _Iterator})["PeekingIterator"]
    for _ in range(1000):
        arr = [random.randrange(1, 9) for _ in range(random.randrange(1, 10))]
        pi = cls(_Iterator(arr))
        for i in range(len(arr) + 1):
            assert pi.hasNext() == (i < len(arr)), key
            if i == len(arr):
                break
            for _ in range(random.randrange(0, 3)):
                assert pi.peek() == arr[i], key
                assert pi.hasNext(), key
            assert pi.next() == arr[i], key
print("P284 OK")

emit({
 "num": 284, "slug": "peeking-iterator",
 "en": [
   "Design an iterator that supports the <code>peek</code> operation on an existing iterator in addition to the <code>hasNext</code> and the <code>next</code> operations.",
   "Implement the <code>PeekingIterator</code> class:",
   ("ul", ["<code>PeekingIterator(Iterator&lt;int&gt; nums)</code> Initializes the object with the given integer iterator <code>iterator</code>.",
           "<code>int next()</code> Returns the next element in the array and moves the pointer to the next element.",
           "<code>boolean hasNext()</code> Returns <code>true</code> if there are still elements in the array.",
           "<code>int peek()</code> Returns the next element in the array <strong>without</strong> moving the pointer."]),
   "<strong>Follow up:</strong> How would you extend your design to be generic and work with all types, not just integer?",
 ],
 "zh": [
   "給你一個只支援 <code>hasNext</code>、<code>next</code> 的迭代器，請包裝出一個額外支援 <code>peek</code> 的迭代器。",
   ("ul", ["<code>PeekingIterator(iterator)</code>：用給定的迭代器初始化。",
           "<code>next()</code>：回傳下一個元素，並前進。",
           "<code>hasNext()</code>：還有沒有元素。",
           "<code>peek()</code>：回傳下一個元素，但<strong>不前進</strong>。"]),
   "<strong>進階：</strong>怎麼讓設計適用於任何型別，而不只是整數？",
 ],
 "examples": """範例
  輸入：["PeekingIterator","next","peek","next","next","hasNext"]
        [[[1,2,3]],[],[],[],[],[]]
  輸出：[null,1,2,2,3,false]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 1000",
   "1 ≤ <code>nums[i]</code> ≤ 1000",
   "所有 <code>next</code>、<code>peek</code> 呼叫都是合法的",
   "最多呼叫 1000 次",
 ],
 "idea": [
   ("c", """【原本的迭代器只能「拿」不能「看」】
    一旦呼叫 next()，元素就被消耗了，沒辦法放回去。

【解法：自己多存一個元素（快取）】
    偷看的時候其實已經拿出來了，
    存在自己身上；下次 next() 直接給這個存著的值。

【兩種策略】
    預先拿（eager）：建構時就拿好第一個，
        之後每次 next() 都順便補下一個。
        peek 永遠 O(1)，邏輯簡單。
    需要才拿（lazy）：用一個旗標 cached 記錄「是否已偷看」。
        如果底層迭代器很昂貴（讀檔、網路），可以少拿一個。

【hasNext 要把快取算進去】
    快取裡有東西 -> 還有下一個，
    即使底層迭代器已經 hasNext() == False。"""),
 ],
 "approaches": [
   ap("解法一", "預先拿好下一個（eager）", [
     ("c", S["p284"]),
   ], "每個操作 O(1)", "O(1)", "", ""),

   ap("解法二", "需要時才偷看（lazy）", [
     ("c", S["p284_flag"]),
     "用旗標 <code>cached</code> 區分「沒有快取」和「快取的值剛好是 None」，所以這個寫法對任何型別（包含 None）都成立——這就是進階問題的答案。",
   ], "每個操作 O(1)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、eager", "O(1)", "建構時就消耗一個元素"],
    ["二、lazy + 旗標", "O(1)", "泛型安全 ✔"]]),
 "edges": [
   "<strong>連續 peek 多次</strong> → 都回傳同一個值，不前進。",
   "<strong>peek 之後 hasNext</strong> → 快取中還有值，要回傳 true。",
   "<strong>元素可能是 None / null</strong>（泛型）→ 不能用「值是否為 None」判斷有沒有快取，要用旗標。",
 ],
 "follow": [
   ("h", "設計模式"),
   ("c", "這是「裝飾器（Decorator）」模式：包住一個現有物件，介面不變，再加上新功能。Python 的 <code>itertools</code> 沒有內建 peek，常見的做法就是自己包一層；<code>more_itertools.peekable</code> 也是同樣原理。"),
 ],
 "related": [
   "<strong>第 173 題 二元搜尋樹迭代器</strong>",
   "<strong>第 251 題 展開二維向量</strong>（付費）",
   "<strong>第 341 題 扁平化巢狀列表迭代器</strong>",
 ],
 "check": [
   "為什麼需要自己多存一個元素？",
   "hasNext 為什麼要考慮快取？",
   "泛型版本為什麼要用旗標，而不是檢查值是否為 None？",
 ],
})


# ==================== 287. Find the Duplicate Number ====================
S["p287_floyd"] = '''class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 把 i -> nums[i] 看成鏈結串列的 next；重複的值 = 環的入口
        slow = fast = 0
        while True:                            # 第一階段：快慢指標在環內相遇
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0                               # ★ 第二階段：一個從頭、一個從相遇點，同速前進
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow                            # 相遇處就是環的入口'''

S["p287_bs"] = '''class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums) - 1              # 對「值」二分
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = sum(x <= mid for x in nums)  # <= mid 的元素個數
            if cnt > mid:                      # ★ 鴿籠原理：1..mid 裡擠了超過 mid 個 -> 重複在左半
                hi = mid
            else:
                lo = mid + 1
        return lo'''

S["p287_bits"] = '''class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        res = 0
        for b in range(n.bit_length()):
            mask = 1 << b
            # 陣列中這一位是 1 的個數 vs 1..n 中這一位是 1 的個數
            have = sum(1 for x in nums if x & mask)
            expect = sum(1 for x in range(1, n + 1) if x & mask)
            if have > expect:                  # 多出來的，一定來自重複的數
                res |= mask
        return res'''

_p287 = [S.load(x) for x in ("p287_floyd", "p287_bs", "p287_bits")]
for nums, want in [([1, 3, 4, 2, 2], 2), ([3, 1, 3, 4, 2], 3), ([3, 3, 3, 3, 3], 3), ([1, 1], 1), ([2, 2, 2], 2)]:
    for sol in _p287:
        assert sol.findDuplicate(nums) == want
for _ in range(3000):
    n = random.randrange(1, 15)
    d = random.randint(1, n)
    k = random.randrange(2, n + 2)                 # 重複 k 次
    others = random.sample([x for x in range(1, n + 1) if x != d], n + 1 - k) if n + 1 - k <= n - 1 else None
    if others is None:
        continue
    nums = [d] * k + others
    random.shuffle(nums)
    for sol in _p287:
        assert sol.findDuplicate(nums) == d, (nums, sol)
print("P287 OK")

_P287_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">nums = [1, 3, 4, 2, 2]：把 i → nums[i] 當成「下一個節點」</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="60" cy="90" r="17" fill="none" stroke="var(--text-muted)"/><text x="60" y="95" fill="var(--text)">0</text>
              <circle cx="160" cy="90" r="17" fill="none" stroke="var(--text-muted)"/><text x="160" y="95" fill="var(--text)">1</text>
              <circle cx="260" cy="90" r="17" fill="none" stroke="var(--text-muted)"/><text x="260" y="95" fill="var(--text)">3</text>
              <circle cx="360" cy="90" r="17" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="360" y="95" fill="#ff8a65">2</text>
              <circle cx="460" cy="90" r="17" fill="none" stroke="var(--text-muted)"/><text x="460" y="95" fill="var(--text)">4</text>
            </g>
            <g stroke="var(--text-muted)" fill="var(--text-muted)">
              <line x1="77" y1="90" x2="137" y2="90"/><polygon points="143,90 134,85 134,95"/>
              <line x1="177" y1="90" x2="237" y2="90"/><polygon points="243,90 234,85 234,95"/>
              <line x1="277" y1="90" x2="337" y2="90"/><polygon points="343,90 334,85 334,95"/>
              <line x1="377" y1="90" x2="437" y2="90"/><polygon points="443,90 434,85 434,95"/>
            </g>
            <path d="M455 107 C 440 150, 380 150, 365 110" fill="none" stroke="var(--gold)"/>
            <polygon points="363,107 360,118 369,114" fill="var(--gold)"/>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="110" y="78">nums[0]=1</text><text x="210" y="78">nums[1]=3</text><text x="310" y="78">nums[3]=2</text><text x="410" y="78">nums[2]=4</text>
              <text x="410" y="160" fill="var(--gold)">nums[4]=2</text>
            </g>
            <text x="20" y="196" fill="var(--text)" font-size="12">兩個索引（3 和 4）都指向 2 → 2 有兩個「前一個節點」→ 2 就是環的入口。</text>
            <text x="20" y="220" fill="var(--gold)" font-size="12">★ 找重複數 = 找環的入口 = 第 142 題的 Floyd 演算法。</text>'''

emit({
 "num": 287, "slug": "find-the-duplicate-number",
 "en": [
   "Given an array of integers <code>nums</code> containing <code>n + 1</code> integers where each integer is in the range <code>[1, n]</code> inclusive.",
   "There is only <strong>one repeated number</strong> in <code>nums</code>, return <em>this repeated number</em>.",
   "You must solve the problem <strong>without</strong> modifying the array <code>nums</code> and using only constant extra space.",
   "<strong>Follow up:</strong> How can we prove that at least one duplicate number must exist in <code>nums</code>? Can you solve the problem in linear runtime complexity?",
 ],
 "zh": [
   "給你一個包含 <code>n + 1</code> 個整數的陣列 <code>nums</code>，每個整數都在 <code>[1, n]</code> 範圍內。",
   "陣列中<strong>只有一個數字重複</strong>（但可能重複很多次），請找出它。",
   "必須<strong>不修改</strong>陣列，而且只使用<strong>常數</strong>額外空間。",
   "<strong>進階：</strong>如何證明一定存在重複的數？能在線性時間內解決嗎？",
 ],
 "examples": """範例 1
  輸入：nums = [1,3,4,2,2]
  輸出：2

範例 2
  輸入：nums = [3,1,3,4,2]
  輸出：3

範例 3
  輸入：nums = [3,3,3,3,3]
  輸出：3""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 10⁵",
   "<code>nums.length == n + 1</code>",
   "1 ≤ <code>nums[i]</code> ≤ <code>n</code>",
   "只有一個整數重複，但它可能出現兩次以上",
 ],
 "idea": [
   ("c", """【限制很多】
    不能改陣列 -> 不能排序、不能原地標記
    O(1) 空間  -> 不能用雜湊集合
    重複的數可能出現很多次 -> 求和、XOR 都不行

【為什麼一定有重複？】
    鴿籠原理：n + 1 個數放進 n 個值裡 -> 至少一個值出現兩次。

【方法一：對「值」二分（鴿籠原理）】
    數一數 <= mid 的元素有幾個（cnt）。
    如果 1..mid 都沒重複，cnt 最多是 mid。
    cnt > mid -> 重複的數在 [1, mid] ✔
    O(n log n)。"""),
   ("fig", _P287_FIG, "0 0 640 234"),
   ("c", """【方法二：看成鏈結串列找環（Floyd）】
    把索引 i 看成節點，nums[i] 看成它的 next。
    - 值都在 [1, n]，索引 0 不會被任何人指到 -> 從 0 出發是一條「鏈」
    - n+1 個節點，每個都有 next -> 走下去一定會進入環
    - 環的入口 = 有兩個前驅的節點 = 被兩個索引指到的值 = 重複的數

    然後就是第 142 題：
    1. 快慢指標（一次兩步、一次一步）在環內相遇
    2. 一個指標回到起點，兩個同速前進，再次相遇就是環的入口
    O(n) 時間、O(1) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "對值二分 + 計數", [
     ("c", S["p287_bs"]),
   ], "O(n log n)", "O(1)", "", ""),

   ap("解法二", "逐位元比較", [
     ("c", S["p287_bits"]),
     ("c", """【每一個位元分開看】
    陣列 = 1..n 各一個 + 重複的數多出來的幾份（替換掉某些缺少的數）。
    重複的數 d 在某一位是 1 -> 陣列中這一位的 1 會比 1..n 多。
    d 在某一位是 0 -> 陣列中這一位的 1 不會比 1..n 多。
    （嚴謹證明要考慮「d 取代了哪些數」，結論依然成立。）"""),
   ], "O(n log n)", "O(1)", "", ""),

   ap("解法三", "Floyd 判圈（快慢指標）", [
     ("c", S["p287_floyd"]),
     ("c", """【為什麼第二階段一定會在入口相遇？】（第 142 題的證明）
    起點到入口距離 a，入口到相遇點 b，環長 L。
    相遇時：fast 走 2(a+b)，slow 走 a+b，差 a+b 是 L 的整數倍。
    -> 從相遇點再走 a 步 = 總共 a+b+a ≡ a (mod L)，剛好停在入口。
    而從起點走 a 步也剛好到入口 -> 兩者在入口相遇 ✔"""),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、對值二分", "O(n log n)", "O(1)", "最好想"],
    ["二、逐位元", "O(n log n)", "O(1)", ""],
    ["三、Floyd", "O(n)", "O(1)", "最佳 ✔"]]),
 "edges": [
   "<strong>重複很多次</strong>（<code>[3,3,3,3,3]</code>）→ 三種方法都成立；求和、XOR 會失敗。",
   "<strong>n = 1</strong>（<code>[1,1]</code>）→ 1。",
   "<strong>從 0 出發很重要</strong> → 索引 0 不在任何環裡，保證是「鏈 + 環」的形狀。",
 ],
 "follow": [
   ("h", "如果可以修改陣列？"),
   ("c", "原地標記：走到值 x 時把 nums[x] 變成負數，遇到已經是負數的就找到了。O(n) 時間、O(1) 空間，但違反本題限制。"),
 ],
 "related": [
   "<strong>第 142 題 環狀鏈結串列 II</strong>",
   "<strong>第 41 題 缺失的第一個正數</strong>",
   "<strong>第 268 題 遺失的數字</strong>",
   "<strong>第 645 題 錯誤的集合</strong>",
 ],
 "check": [
   "為什麼一定存在重複的數？",
   "為什麼求和或 XOR 在這題不管用？",
   "把陣列看成鏈結串列時，重複的數對應到什麼？",
   "Floyd 演算法第二階段為什麼一定會在環的入口相遇？",
 ],
})


# ==================== 289. Game of Life ====================
S["p289"] = '''class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        # ★ 用第 2 個位元存「下一代」：bit0 = 現在，bit1 = 下一代
        for i in range(m):
            for j in range(n):
                live = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if (di or dj) and 0 <= i + di < m and 0 <= j + dj < n:
                            live += board[i + di][j + dj] & 1    # 只看現在的狀態
                if live == 3 or (live == 2 and board[i][j] & 1):
                    board[i][j] |= 2                              # 下一代活著
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1                                 # 全部換成下一代'''

S["p289_copy"] = '''class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        old = [row[:] for row in board]            # 複製一份舊的
        for i in range(m):
            for j in range(n):
                live = sum(old[x][y] for x in range(max(0, i - 1), min(m, i + 2))
                                      for y in range(max(0, j - 1), min(n, j + 2))) - old[i][j]
                board[i][j] = 1 if live == 3 or (live == 2 and old[i][j]) else 0'''

_p289 = [S.load(x) for x in ("p289", "p289_copy")]
B0 = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
for sol in _p289:
    b = [r[:] for r in B0]
    sol.gameOfLife(b)
    assert b == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    b = [[1, 1], [1, 0]]
    sol.gameOfLife(b)
    assert b == [[1, 1], [1, 1]]
for _ in range(1500):
    m, n = random.randrange(1, 7), random.randrange(1, 7)
    b = [[random.randrange(2) for _ in range(n)] for _ in range(m)]
    b1, b2 = [r[:] for r in b], [r[:] for r in b]
    _p289[0].gameOfLife(b1)
    _p289[1].gameOfLife(b2)
    assert b1 == b2
print("P289 OK")

_P289_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">每個格子用兩個位元：bit0 = 現在，bit1 = 下一代</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="40" width="130" height="30" fill="none" stroke="var(--border)"/><text x="105" y="60" fill="var(--text)">值</text>
              <rect x="170" y="40" width="130" height="30" fill="none" stroke="var(--border)"/><text x="235" y="60" fill="var(--text)">二進位</text>
              <rect x="300" y="40" width="130" height="30" fill="none" stroke="var(--border)"/><text x="365" y="60" fill="var(--text)">現在</text>
              <rect x="430" y="40" width="130" height="30" fill="none" stroke="var(--border)"/><text x="495" y="60" fill="var(--text)">下一代</text>
              <text x="105" y="92" fill="var(--text)">0</text><text x="235" y="92" fill="var(--text-muted)">00</text><text x="365" y="92" fill="var(--text-muted)">死</text><text x="495" y="92" fill="var(--text-muted)">死</text>
              <text x="105" y="116" fill="var(--text)">1</text><text x="235" y="116" fill="var(--text-muted)">01</text><text x="365" y="116" fill="var(--accent)">活</text><text x="495" y="116" fill="var(--text-muted)">死</text>
              <text x="105" y="140" fill="var(--text)">2</text><text x="235" y="140" fill="var(--text-muted)">10</text><text x="365" y="140" fill="var(--text-muted)">死</text><text x="495" y="140" fill="var(--gold)">活</text>
              <text x="105" y="164" fill="var(--text)">3</text><text x="235" y="164" fill="var(--text-muted)">11</text><text x="365" y="164" fill="var(--accent)">活</text><text x="495" y="164" fill="var(--gold)">活</text>
            </g>
            <text x="40" y="196" fill="var(--text)" font-size="12">計算鄰居時用 board[x][y] &amp; 1，只看「現在」—— 不會被已經算好的下一代干擾。</text>
            <text x="40" y="218" fill="var(--gold)" font-size="12">★ 全部算完之後 board[i][j] &gt;&gt;= 1，一次切換到下一代。</text>'''

emit({
 "num": 289, "slug": "game-of-life",
 "en": [
   "According to Wikipedia's article: \"The <strong>Game of Life</strong>, also known simply as <strong>Life</strong>, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.\"",
   "The board is made up of an <code>m x n</code> grid of cells, where each cell has an initial state: <strong>live</strong> (represented by a <code>1</code>) or <strong>dead</strong> "
   "(represented by a <code>0</code>). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules:",
   ("ol", ["Any live cell with fewer than two live neighbors dies as if caused by under-population.",
           "Any live cell with two or three live neighbors lives on to the next generation.",
           "Any live cell with more than three live neighbors dies, as if by over-population.",
           "Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction."]),
   "The next state of the board is determined by applying the above rules simultaneously to every cell in the current state. Given the current state of the board, update the board to reflect its next state.",
   "<strong>Follow up:</strong> Could you solve it in-place? The board is infinite in principle — how would you address the problems when the active area encroaches upon the border of the array?",
 ],
 "zh": [
   "<strong>生命遊戲</strong>是英國數學家康威在 1970 年設計的細胞自動機。",
   "<code>m x n</code> 的格子中，每個細胞是<strong>活</strong>（<code>1</code>）或<strong>死</strong>（<code>0</code>）。每個細胞和周圍八個鄰居（上下左右與斜角）依照四條規則互動：",
   ("ol", ["活細胞的活鄰居少於 2 個 → 死亡（人口太少）。",
           "活細胞的活鄰居有 2 或 3 個 → 繼續存活。",
           "活細胞的活鄰居多於 3 個 → 死亡（人口過剩）。",
           "死細胞的活鄰居<strong>恰好</strong> 3 個 → 復活（繁殖）。"]),
   "所有細胞<strong>同時</strong>依照目前的狀態更新。請把 <code>board</code> 更新成下一代的狀態。",
   "<strong>進階：</strong>能原地完成嗎？理論上棋盤是無限大的，活躍區域碰到邊界時該怎麼辦？",
 ],
 "examples": """範例 1
  輸入：board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
  輸出：[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

範例 2
  輸入：board = [[1,1],[1,0]]
  輸出：[[1,1],[1,1]]""",
 "constraints": [
   "<code>m == board.length</code>，<code>n == board[i].length</code>",
   "1 ≤ <code>m, n</code> ≤ 25",
   "<code>board[i][j]</code> 是 <code>0</code> 或 <code>1</code>",
 ],
 "idea": [
   ("c", """【四條規則可以濃縮成一句】
    下一代活著 <=> 活鄰居 == 3，或（活鄰居 == 2 且自己現在活著）

【難點：「同時」更新】
    如果邊算邊改，後面的格子算鄰居時會看到「已經更新過」的值 ✘

【方法一：複製一份舊棋盤】
    從舊的讀、往新的寫。O(mn) 額外空間。

【方法二：原地，用多餘的位元】
    格子只用 0 / 1，int 還有很多位元沒用到。
    bit0 存現在的狀態，bit1 存下一代的狀態：
        算鄰居時只看 & 1（現在）
        決定下一代活著就 |= 2
    全部算完後，每格 >>= 1，下一代就變成現在。"""),
   ("fig", _P289_FIG, "0 0 640 232"),
 ],
 "approaches": [
   ap("解法一", "複製棋盤", [
     ("c", S["p289_copy"]),
   ], "O(mn)", "O(mn)", "每格看 8 個鄰居", ""),

   ap("解法二", "原地：第二個位元存下一代", [
     ("c", S["p289"]),
   ], "O(mn)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、複製", "O(mn)", "O(mn)"],
    ["二、位元編碼", "O(mn)", "O(1) ✔"]]),
 "edges": [
   "<strong>邊界的格子</strong> → 鄰居少於 8 個，要檢查範圍。",
   "<strong>1 × 1</strong> → 沒有鄰居，活的會死。",
   "<strong>死細胞剛好 2 個活鄰居</strong> → 仍然是死的（只有「3」能復活）。",
 ],
 "follow": [
   ("h", "無限大的棋盤？"),
   ("c", """用雜湊集合只存活細胞的座標（稀疏表示）：
對每個活細胞的 8 個鄰居 +1 計數，再依規則決定下一代的集合。
記憶體只和活細胞數量有關，棋盤可以無限延伸。
著名的「滑翔機」(glider)——範例 1 就是一台——會一直往斜下方移動。"""),
 ],
 "related": [
   "<strong>第 73 題 矩陣置零</strong> —— 原地標記",
   "<strong>第 957 題 N 天後的牢房</strong> —— 一維版本，找週期",
 ],
 "check": [
   "四條規則可以怎麼合併成一個判斷？",
   "為什麼不能邊算邊直接改？",
   "位元編碼中，bit0 和 bit1 各代表什麼？",
 ],
})


# ==================== 290. Word Pattern ====================
S["p290"] = '''class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        p2w, w2p = {}, {}                         # ★ 兩個方向都要一對一
        for ch, w in zip(pattern, words):
            if p2w.setdefault(ch, w) != w or w2p.setdefault(w, ch) != ch:
                return False
        return True'''

S["p290_idx"] = '''class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        # 兩個序列「第一次出現的位置」逐項相同 <=> 結構相同
        return [pattern.index(c) for c in pattern] == [words.index(w) for w in words]'''

S["p290_set"] = '''class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        # 雙射 <=> 字母種類數 = 單字種類數 = 配對種類數
        return len(words) == len(pattern) and \\
            len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))'''

_p290 = [S.load(x) for x in ("p290", "p290_idx", "p290_set")]
for p, s, want in [("abba", "dog cat cat dog", True), ("abba", "dog cat cat fish", False), ("aaaa", "dog cat cat dog", False),
                   ("abba", "dog dog dog dog", False), ("a", "a b", False), ("ab", "x x", False)]:
    for sol in _p290:
        assert sol.wordPattern(p, s) == want, (p, s, sol)
for _ in range(4000):
    p = "".join(random.choice("abc") for _ in range(random.randrange(1, 6)))
    s = " ".join(random.choice(["dog", "cat", "fish"]) for _ in range(random.randrange(1, 6)))
    r = [sol.wordPattern(p, s) for sol in _p290]
    assert r[0] == r[1] == r[2], (p, s)
print("P290 OK")

emit({
 "num": 290, "slug": "word-pattern",
 "en": [
   "Given a <code>pattern</code> and a string <code>s</code>, find if <code>s</code> follows the same pattern.",
   "Here <strong>follow</strong> means a full match, such that there is a bijection between a letter in <code>pattern</code> and a <strong>non-empty</strong> word in <code>s</code>. Specifically:",
   ("ul", ["Each letter in <code>pattern</code> maps to <strong>exactly</strong> one unique word in <code>s</code>.",
           "Each unique word in <code>s</code> maps to <strong>exactly</strong> one letter in <code>pattern</code>.",
           "No two letters map to the same word, and no two words map to the same letter."]),
 ],
 "zh": [
   "給你一個規律 <code>pattern</code> 和字串 <code>s</code>，判斷 <code>s</code> 是否遵循相同的規律。",
   "「遵循」是指 <code>pattern</code> 的字母和 <code>s</code> 的單字之間存在<strong>雙射</strong>（一對一對應）：",
   ("ul", ["每個字母只對應一個單字。",
           "每個單字只對應一個字母。",
           "不同的字母不能對應到同一個單字，反之亦然。"]),
 ],
 "examples": """範例 1
  輸入：pattern = "abba", s = "dog cat cat dog"
  輸出：true

範例 2
  輸入：pattern = "abba", s = "dog cat cat fish"
  輸出：false

範例 3
  輸入：pattern = "aaaa", s = "dog cat cat dog"
  輸出：false""",
 "constraints": [
   "1 ≤ <code>pattern.length</code> ≤ 300",
   "<code>pattern</code> 只包含小寫英文字母",
   "1 ≤ <code>s.length</code> ≤ 3000",
   "<code>s</code> 只包含小寫英文字母和空白",
   "<code>s</code> 沒有前導或結尾空白，單字之間恰好一個空白",
 ],
 "idea": [
   ("c", """【和第 205 題「同構字串」一模一樣】
    只是右邊從「字元」換成了「單字」。

【為什麼要兩個方向？】
    只檢查 字母 -> 單字：
        "ab" 對 "dog dog"：a->dog, b->dog，每個字母都只對應一個單字 ✔
        但兩個字母對到同一個單字，不是雙射 ✘
    所以還要檢查 單字 -> 字母。

【長度不同】
    pattern 的長度和單字數不同 -> 直接 false。
    （zip 會默默截斷，一定要先檢查！）

【其他寫法】
    - 「第一次出現的位置」序列相同 <=> 結構相同
    - 集合大小：字母種類 = 單字種類 = (字母, 單字) 配對種類 <=> 雙射"""),
 ],
 "approaches": [
   ap("解法一", "兩個雜湊表", [
     ("c", S["p290"]),
     "<code>setdefault(k, v)</code>：k 不存在時設成 v 並回傳 v；存在時回傳原本的值。一行同時完成「查」和「設」。",
   ], "O(n + |s|)", "O(n)", "", "", optimal=True),

   ap("解法二", "第一次出現的位置", [
     ("c", S["p290_idx"]),
     "<code>index</code> 是 O(n)，整體 O(n²)。n ≤ 300 可以接受，寫法最短。",
   ], "O(n²)", "O(n)", "", ""),

   ap("解法三", "集合大小", [
     ("c", S["p290_set"]),
     ("c", """【為什麼三個大小相等 <=> 雙射？】
    配對數 >= 字母種類數，等號成立 <=> 每個字母只和一種單字配對。
    配對數 >= 單字種類數，等號成立 <=> 每個單字只和一種字母配對。
    兩個都成立 -> 雙射 ✔"""),
   ], "O(n + |s|)", "O(n)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、兩個雜湊表", "O(n)", "最標準 ✔"],
    ["二、第一次出現位置", "O(n²)", "最短"],
    ["三、集合大小", "O(n)", "巧妙"]]),
 "edges": [
   "<strong>長度不同</strong> → false；zip 會截斷，一定要先檢查。",
   "<strong>不同字母對到同一個單字</strong>（<code>\"ab\"</code>, <code>\"x x\"</code>）→ false。",
   "<strong>同一個字母對到不同單字</strong> → false。",
 ],
 "follow": [
   ("h", "追問：如果 s 沒有空白分隔？"),
   ("c", "第 291 題（付費）：\"abab\" 對 \"redblueredblue\"——不知道每個字母對應多長的子字串，要用回溯嘗試所有切法。"),
 ],
 "related": [
   "<strong>第 205 題 同構字串</strong>",
   "<strong>第 291 題 單字規律 II</strong>（付費）",
   "<strong>第 890 題 查找和替換模式</strong>",
 ],
 "check": [
   "為什麼只檢查「字母 → 單字」不夠？",
   "為什麼要先比較長度？",
   "集合大小法為什麼成立？",
 ],
})


# ==================== 292. Nim Game ====================
S["p292"] = '''class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0            # ★ 4 的倍數是必敗態'''

S["p292_dp"] = '''class Solution:
    def canWinNim(self, n: int) -> bool:
        # win[i]：剩 i 顆、輪到我時，我能不能贏（只用來觀察規律，n 很大時太慢）
        win = [False] * (n + 1)
        for i in range(1, n + 1):
            # 只要有一種拿法讓對手落入必敗態，我就必勝
            win[i] = any(not win[i - k] for k in (1, 2, 3) if k <= i)
        return win[n]'''

_p292 = [S.load(x) for x in ("p292", "p292_dp")]
for n in range(1, 400):
    assert _p292[0].canWinNim(n) == _p292[1].canWinNim(n), n
print("P292 OK")

emit({
 "num": 292, "slug": "nim-game",
 "en": [
   "You are playing the following Nim Game with your friend:",
   ("ul", ["Initially, there is a heap of stones on the table.",
           "You and your friend will alternate taking turns, and <strong>you go first</strong>.",
           "On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.",
           "The one who removes the last stone is the winner."]),
   "Given <code>n</code>, the number of stones in the heap, return <code>true</code> if you can win the game assuming both you and your friend play optimally, otherwise return <code>false</code>.",
 ],
 "zh": [
   "你和朋友玩拿石頭遊戲：",
   ("ul", ["桌上有一堆石頭。",
           "兩人輪流，<strong>你先手</strong>。",
           "每次可以拿 1 到 3 顆。",
           "拿到最後一顆的人獲勝。"]),
   "給你石頭數 <code>n</code>，假設雙方都採取最佳策略，判斷你能不能贏。",
 ],
 "examples": """範例 1
  輸入：n = 4
  輸出：false
  說明：不管你拿 1、2、3 顆，朋友都能拿走剩下的全部。

範例 2
  輸入：n = 1
  輸出：true

範例 3
  輸入：n = 2
  輸出：true""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【從小的情況觀察】
    剩 1、2、3 顆：一次拿完 -> 必勝
    剩 4 顆：拿 1/2/3 之後對手面對 3/2/1 -> 對手必勝 -> 我必敗
    剩 5、6、7 顆：拿 1/2/3 讓對手面對 4 -> 必勝
    剩 8 顆：不管怎麼拿，對手面對 5/6/7 -> 必敗

【規律：4 的倍數是必敗態】
    必勝策略：每次拿到讓剩下的是 4 的倍數。
    對手拿 k 顆（1..3），我就拿 4 - k 顆，
    每一輪兩人合計拿 4 顆，剩下的永遠是 4 的倍數，
    最後一輪剩 4 顆輪到對手 -> 我拿到最後一顆。

    如果一開始就是 4 的倍數，對手可以用同樣的策略對付我。

【博弈的一般方法】
    必敗態：所有走法都通往必勝態
    必勝態：存在一種走法通往必敗態
    從小到大推（DP），找規律。"""),
   ("t", ["剩下的石頭", "1", "2", "3", "4", "5", "6", "7", "8"],
    [["先手", "勝", "勝", "勝", "敗", "勝", "勝", "勝", "敗"]]),
 ],
 "approaches": [
   ap("解法一", "DP 推必勝／必敗態（觀察用）", [
     ("c", S["p292_dp"]),
     "n 可以到 2³¹，DP 會超時也會超記憶體——但用它跑出前幾十項，就能發現規律。",
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "數學：n % 4", [
     ("c", S["p292"]),
   ], "O(1)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、DP", "O(n)", "O(n)"],
    ["二、n % 4", "O(1)", "O(1) ✔"]]),
 "edges": [
   "<strong>n = 1、2、3</strong> → 必勝。",
   "<strong>n = 4</strong> → 必敗。",
   "<strong>n 很大</strong> → 只看 mod 4。",
 ],
 "follow": [
   ("h", "推廣：每次拿 1 到 m 顆？"),
   ("c", "巴什博弈（Bash Game）：n % (m + 1) != 0 先手必勝。本題 m = 3。"),
   ("h", "多堆石頭？"),
   ("c", "真正的 Nim 遊戲：每次從任一堆拿任意顆。先手必勝 ⟺ 各堆石頭數的 XOR 不為 0（Sprague–Grundy 理論的起點）。"),
 ],
 "related": [
   "<strong>第 877 題 石子遊戲</strong>",
   "<strong>第 1025 題 除數博弈</strong>",
   "<strong>第 294 題 翻轉遊戲 II</strong>（付費）",
   "<strong>第 464 題 我能贏嗎</strong>",
 ],
 "check": [
   "為什麼剩 4 顆時先手必敗？",
   "必勝策略是什麼？",
   "怎麼判斷一個狀態是必勝還是必敗？",
 ],
})
