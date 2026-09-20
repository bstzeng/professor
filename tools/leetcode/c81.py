# -*- coding: utf-8 -*-
"""第 81–83 題。"""
import random
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(81)

# ==================== 81. Search in Rotated Sorted Array II ====================
S["p81"] = '''class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True

            if nums[lo] == nums[mid] == nums[hi]:
                # 三個都一樣 -> 看不出哪一半有序，只好兩端各縮一格
                lo += 1
                hi -= 1
            elif nums[lo] <= nums[mid]:
                # 左半段 [lo, mid] 有序
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                # 右半段 [mid, hi] 有序
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False'''

S["p81_shrink"] = '''class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            # 先把左右兩端「和端點相同」的重複值剝掉，再做二分
            while lo < hi and nums[lo] == nums[lo + 1]:
                lo += 1
            while lo < hi and nums[hi] == nums[hi - 1]:
                hi -= 1

            mid = (lo + hi) // 2
            if nums[mid] == target:
                return True

            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        return False'''

_p81 = [S.load(k) for k in ("p81", "p81_shrink")]
for c, t in [([2, 5, 6, 0, 0, 1, 2], 0), ([2, 5, 6, 0, 0, 1, 2], 3),
             ([1, 0, 1, 1, 1], 0), ([1, 1, 1, 0, 1], 0), ([1], 1), ([1], 0),
             ([1, 1], 1), ([3, 1], 1), ([1, 1, 1, 1], 1), ([1, 1, 1, 1], 2)]:
    e = t in c
    for sol in _p81:
        assert sol.search(list(c), t) is e, ("P81", c, t, sol, sol.search(list(c), t), e)
for _ in range(6000):
    k = random.randint(1, 9)
    base = sorted(random.randint(0, 4) for _ in range(k))
    r = random.randint(0, k - 1)
    c = base[r:] + base[:r]
    t = random.randint(-1, 5)
    e = t in c
    for sol in _p81:
        assert sol.search(list(c), t) is e, ("P81", c, t, sol, sol.search(list(c), t), e)
print("P81 solutions OK")

_P81_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">重複值讓「哪一半有序」變得無法判斷</text>
            <text x="20" y="50" fill="var(--text-muted)" font-size="12">nums = [1, 1, 1, 0, 1]，target = 0，lo = 0, mid = 2, hi = 4</text>
            <g font-size="16" text-anchor="middle">
              <rect x="80" y="66" width="80" height="44" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="120" y="95" fill="var(--accent)">1</text>
              <rect x="170" y="66" width="80" height="44" rx="6" fill="none" stroke="var(--border)"/><text x="210" y="95" fill="var(--text-muted)">1</text>
              <rect x="260" y="66" width="80" height="44" rx="6" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="300" y="95" fill="var(--gold)">1</text>
              <rect x="350" y="66" width="80" height="44" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="390" y="95" fill="#ff8a65">0</text>
              <rect x="440" y="66" width="80" height="44" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="480" y="95" fill="var(--accent)">1</text>
            </g>
            <g font-size="12" text-anchor="middle">
              <text x="120" y="130" fill="var(--accent)">lo</text>
              <text x="300" y="130" fill="var(--gold)">mid</text>
              <text x="480" y="130" fill="var(--accent)">hi</text>
            </g>
            <line x1="20" y1="150" x2="620" y2="150" stroke="var(--border)"/>
            <text x="20" y="178" fill="var(--text-muted)" font-size="12">nums[lo] = nums[mid] = nums[hi] = 1　→ 完全看不出斷點在左邊還是右邊</text>
            <g font-family="monospace" font-size="12">
              <text x="40" y="206" fill="var(--text-muted)">[1, 1, 1, 0, 1]　斷點在 mid 右邊</text>
              <text x="40" y="228" fill="var(--text-muted)">[1, 0, 1, 1, 1]　斷點在 mid 左邊</text>
              <text x="380" y="217" fill="#ff8a65">兩者的 lo／mid／hi 完全一樣！</text>
            </g>
            <text x="20" y="262" fill="var(--gold)" font-size="12">唯一的辦法：lo += 1、hi −= 1，放棄這兩格（它們等於 nums[mid]，不是 target）</text>
            <text x="20" y="286" fill="var(--text-muted)" font-size="12">最壞情況（全部相同）會退化成 O(n) —— 而且這是不可避免的。</text>'''

emit({
 "num": 81, "slug": "search-in-rotated-sorted-array-ii",
 "en": [
   "There is an integer array <code>nums</code> sorted in non-decreasing order (not "
   "necessarily with <strong>distinct</strong> values). Before being passed to your function, "
   "<code>nums</code> is <strong>rotated</strong> at an unknown pivot index.",
   "Given the array <code>nums</code> <strong>after</strong> the rotation and an integer "
   "<code>target</code>, return <code>true</code> <em>if</em> <code>target</code> "
   "<em>is in</em> <code>nums</code>, <em>or</em> <code>false</code> <em>if it is not</em>.",
   "<strong>Follow up:</strong> This problem is similar to Search in Rotated Sorted Array, "
   "but <code>nums</code> may contain <strong>duplicates</strong>. Would this affect the "
   "runtime complexity? How and why?",
 ],
 "zh": [
   "有一個<strong>非遞減排序</strong>的整數陣列 <code>nums</code>"
   "（<strong>可能有重複的值</strong>），它在某個未知的位置被<strong>旋轉</strong>過。",
   "給你旋轉之後的陣列和一個 <code>target</code>，判斷 <code>target</code> 在不在裡面。",
   "<strong>進階：</strong>這題和第 33 題很像，但 <code>nums</code> 可能有重複值。"
   "這會影響複雜度嗎？為什麼？",
 ],
 "pre": [
   ("note", "重複值破壞了什麼？", [
     ("c", """第 33 題的核心判斷：
    nums[lo] <= nums[mid]  ->  左半段 [lo, mid] 有序

在「所有值互不相同」的前提下，這個推論是對的。

但有重複值時它失效了：

    nums = [1, 1, 1, 0, 1]     斷點在 mid 右邊
    nums = [1, 0, 1, 1, 1]     斷點在 mid 左邊

    兩者的 lo=0, mid=2, hi=4 位置上的值【完全一樣】：
        nums[0] = 1, nums[2] = 1, nums[4] = 1

    所以 nums[lo] <= nums[mid] 在兩種情況下都成立，
    但「左半有序」只在第一種情況下為真 ✘

唯一的補救：
    當 nums[lo] == nums[mid] == nums[hi] 時，
    我們無法判斷 —— 只好放棄這兩個端點：
        lo += 1
        hi -= 1

    這是安全的，因為 nums[lo] == nums[mid] != target
    （如果等於 target，上面的 nums[mid] == target 就回傳了）。

    但它只縮小了 2 格而不是一半 ——
    最壞情況（全部相同）退化成 O(n)。"""),
     "<strong>而且 O(n) 是不可避免的。</strong>"
     "考慮 <code>[1,1,1,...,1]</code> 裡藏了一個 <code>0</code> —— "
     "任何演算法都必須在最壞情況下檢查幾乎每一格才能確定。"
     "<strong>「有重複值」這個條件，從根本上摧毀了 O(log n) 的可能性。</strong>",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [2,5,6,0,0,1,2], target = 0
  輸出：true

範例 2
  輸入：nums = [2,5,6,0,0,1,2], target = 3
  輸出：false""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 5000",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
   "<code>nums</code> 是一個非遞減陣列旋轉後的結果（<strong>可能有重複值</strong>）",
   "−10⁴ ≤ <code>target</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>可能有重複值</strong> —— 這是和第 33 題唯一的差別，"
       "但它把複雜度從「保證 O(log n)」降成「平均 O(log n)、最壞 O(n)」。",
       "<strong>只要回傳 true/false</strong>（不用回傳索引）。"
       "這讓題目簡單一點 —— 因為有重複值時，「哪一個索引」本來就不唯一。",
       "<strong>n ≤ 5000</strong>，所以就算退化成 O(n) 也完全跑得動。"
       "<strong>題目的重點是「你知不知道會退化，以及為什麼」。</strong>",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P81_FIG, "0 0 640 300"),
 ],
 "approaches": [
   ap("解法一", "第 33 題 + 一個「無法判斷」的分支（標準解）", [
     ("c", S["p81"]),
     ("h", "三個分支的優先順序"),
     ("c", """1. nums[lo] == nums[mid] == nums[hi]
       -> 無法判斷，兩端各縮一格

2. nums[lo] <= nums[mid]
       -> 左半段有序（此時已經排除了「三個都相同」，所以推論成立）

3. else
       -> 右半段有序

第 1 個分支【必須放在最前面】。
如果放在後面，分支 2 會先被觸發並做出錯誤的判斷。

為什麼「三個都相同」才需要放棄？
    只要 nums[lo] != nums[mid] 或 nums[mid] != nums[hi]，
    至少有一邊能確定是有序的：

    nums[lo] < nums[mid]   -> 左半一定有序（沒有斷點）
    nums[lo] > nums[mid]   -> 左半一定有斷點 -> 右半有序
    nums[lo] == nums[mid] 但 nums[mid] != nums[hi]
        -> 此時 nums[mid] != nums[hi]，右半的資訊是有效的
        -> 走 else 分支判斷右半

    嚴格說，只檢查 nums[lo] == nums[mid] == nums[hi] 是「最保守」的做法，
    有些實作只檢查 nums[lo] == nums[mid]（也對，但剪得少一點）。"""),
     ("h", "為什麼 <code>lo += 1; hi -= 1</code> 是安全的？"),
     ("c", """此時 nums[lo] == nums[mid] == nums[hi]，
而且我們已經確認 nums[mid] != target（不然上面就 return True 了）。

所以：
    nums[lo] == nums[mid] != target  -> lo 這一格不可能是答案，可以丟
    nums[hi] == nums[mid] != target  -> hi 這一格也可以丟

丟掉兩格，區間縮小 2。

注意這裡不能寫成「lo = mid + 1」或「hi = mid - 1」——
因為我們不知道 target 在哪一半，不能丟掉一整半。"""),
     ("h", "複雜度分析"),
     ("t", ["情況", "複雜度", "例子"],
       [["沒有重複值", "O(log n)", "退化成第 33 題"],
        ["少量重複", "接近 O(log n)", "偶爾走「縮 2 格」的分支"],
        ["全部相同（除了一個）", "O(n)", "<code>[1,1,...,1,0,1,...,1]</code>"]]),
     "<strong>平均情況仍然接近 O(log n)</strong>，"
     "因為「三個端點剛好相同」在隨機資料上很罕見。",
   ], "平均 O(log n)，最壞 O(n)", "O(1)", "重複值多時退化",
      "只用三個下標", optimal=True),

   ap("解法二", "先剝掉兩端的重複值，再二分", [
     "另一種組織方式：<strong>在每一輪二分之前，先把左右兩端「和鄰居相同」的值剝掉。</strong>",
     ("c", S["p81_shrink"]),
     "<strong>效果和解法一相同</strong>，但邏輯上「先清理、再判斷」比較分明。",
     "<strong>複雜度也一樣</strong>（最壞 O(n)）—— "
     "因為剝重複值本身就可能要剝 O(n) 次。",
     "<strong>要小心內層 while 的條件是 <code>lo &lt; hi</code></strong>（不是 <code>&lt;=</code>），"
     "否則 <code>lo</code> 可能衝過 <code>hi</code>，"
     "然後 <code>nums[lo + 1]</code> 越界。",
     "<strong>兩種寫法挑一個記熟就好。</strong>"
     "解法一比較常見，而且只多一個分支（相對第 33 題的改動最小）。",
   ], "平均 O(log n)，最壞 O(n)", "O(1)", "同上", "同上"),
 ],
 "compare": (["", "第 33 題（無重複）", "第 81 題（有重複）"],
   [["最壞複雜度", "O(log n)", "<strong>O(n)</strong>"],
    ["能判斷哪一半有序？", "永遠可以", "三端相同時不行"],
    ["回傳", "索引", "只要 true/false"],
    ["程式碼差別", "—", "多一個「縮兩格」的分支"]]),
 "edges": [
   "<strong>全部相同且找得到</strong>：<code>([1,1,1,1], 1)</code> → true。第一次 <code>mid</code> 就命中。",
   "<strong>全部相同且找不到</strong>：<code>([1,1,1,1], 2)</code> → false。"
   "<strong>這是 O(n) 退化的極端情況。</strong>",
   "<strong>重複值藏住斷點</strong>：<code>([1,0,1,1,1], 0)</code> → true；"
   "<code>([1,1,1,0,1], 0)</code> → true。"
   "<strong>沒有「三端相同」分支的話，這兩筆會有一筆失敗。</strong>",
   "<strong>單一元素</strong>：<code>([1], 1)</code> → true；<code>([1], 0)</code> → false。",
   "<strong>兩個元素</strong>：<code>([3,1], 1)</code> → true。"
   "驗證 <code>&lt;=</code> vs <code>&lt;</code>（和第 33 題一樣）。",
   "<strong>沒有旋轉</strong>：<code>([1,2,3], 2)</code> → true。退化成普通二分。",
   "<strong>剝重複值時越界</strong>：內層 while 的條件寫成 <code>lo &lt;= hi</code> 會 IndexError。",
 ],
 "follow": [
   ("h", "追問一：為什麼 O(n) 是不可避免的？"),
   ("c", """對抗性論證（adversary argument）：

考慮 nums = [1, 1, 1, ..., 1]（n 個 1）中，
把其中一個換成 0，然後旋轉。

    target = 0

任何演算法在檢查了 k 個位置之後，
如果那 k 個位置都是 1，它還是不知道
「剩下的 n - k 個位置裡有沒有 0」。

對手（adversary）可以一直宣稱「還沒檢查的某一格是 0」，
直到演算法檢查完所有位置為止。

所以最壞情況需要 Ω(n) 次比較。

這是一個很乾淨的下界證明 ——
它說明「有重複值時 O(log n) 不可能」，
而不只是「我們想不出更好的演算法」。""",),
   ("h", "追問二：那為什麼還要寫二分而不是直接線性掃？"),
   "因為<strong>平均情況快很多</strong>。"
   "只有在「大量重複值」的病態輸入上才會退化 —— "
   "而真實資料通常不是那樣。",
   "<strong>這是一個很常見的工程取捨</strong>：",
   ("ul", [
     "<strong>快速排序</strong>：平均 O(n log n)，最壞 O(n²)，但實務上最快",
     "<strong>雜湊表</strong>：平均 O(1)，最壞 O(n)，但實務上無可取代",
     "<strong>本題</strong>：平均 O(log n)，最壞 O(n)",
   ]),
   "<strong>「最壞情況保證」和「平均效能」是兩個不同的目標</strong> —— "
   "在即時系統或對抗性環境（例如可能被攻擊的伺服器）裡選前者，"
   "在一般應用裡選後者。",
   ("h", "追問三：如果要回傳「所有出現的索引」呢？"),
   "那本質上就是 O(出現次數)，而且要先找到「任一個」再往兩邊擴散。"
   "在全部相同的情況下就是 O(n) —— 無法避免。",
   ("h", "追問四：第 154 題（找旋轉陣列的最小值 II）有同樣的問題嗎？"),
   "<strong>有，而且處理方式類似。</strong>"
   "第 153 題（無重複）可以穩定 O(log n)；"
   "第 154 題（有重複）在 <code>nums[mid] == nums[hi]</code> 時無法判斷，"
   "只能 <code>hi -= 1</code>，最壞退化成 O(n)。",
   "<strong>四題放在一起看，會發現「重複值」對二分搜尋的影響是系統性的</strong>：",
   ("c", """第 33 題  搜尋旋轉陣列（無重複）      O(log n)
第 81 題  搜尋旋轉陣列（有重複）      最壞 O(n)
第 153 題 找最小值（無重複）          O(log n)
第 154 題 找最小值（有重複）          最壞 O(n)

共同的原因：
    二分搜尋依賴「能從 O(1) 的資訊判斷答案在哪一半」。
    重複值讓那個判斷失效。""",),
 ],
 "related": [
   "<strong>第 33 題 Search in Rotated Sorted Array</strong> —— 無重複值的版本",
   "<strong>第 153／154 題 Find Minimum in Rotated Sorted Array</strong> —— 同樣的對照",
   "<strong>第 34 題 Find First and Last Position</strong> —— 有重複值的二分",
 ],
 "check": [
   "「三個端點相同」時為什麼無法判斷哪一半有序？請舉出兩個長得一樣但斷點不同的陣列。",
   "<code>lo += 1; hi -= 1</code> 為什麼是安全的？",
   "為什麼最壞情況的 O(n) 是不可避免的？請說明對抗性論證。",
   "這個分支為什麼必須放在三個分支的最前面？",
 ],
})
print("P81 written")

# ==================== 82. Remove Duplicates from Sorted List II ====================
S["p82_iter"] = '''class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy          # prev 永遠指向「已確定保留」的最後一個節點
        cur = head

        while cur:
            # 如果 cur 和後面重複，就一路跳到這一段的最後一個
            if cur.next and cur.val == cur.next.val:
                dup = cur.val
                while cur and cur.val == dup:
                    cur = cur.next
                prev.next = cur          # 整段跳過（不接任何一個）
            else:
                prev = cur               # 這個節點是獨一無二的，保留
                cur = cur.next

        return dummy.next'''

S["p82_rec"] = '''class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        if head.val == head.next.val:
            # 頭節點有重複 -> 整段都要刪掉
            dup = head.val
            while head and head.val == dup:
                head = head.next
            return self.deleteDuplicates(head)

        # 頭節點獨一無二 -> 保留它，處理後面
        head.next = self.deleteDuplicates(head.next)
        return head'''

_p82 = [S.load(k) for k in ("p82_iter", "p82_rec")]


def _p82_ref(vals):
    out = []
    i = 0
    while i < len(vals):
        j = i
        while j < len(vals) and vals[j] == vals[i]:
            j += 1
        if j - i == 1:
            out.append(vals[i])
        i = j
    return out


for vals in [[1, 2, 3, 3, 4, 4, 5], [1, 1, 1, 2, 3], [], [1], [1, 1],
             [1, 1, 2, 2], [1, 2, 2], [1, 1, 2]]:
    e = _p82_ref(vals)
    for sol in _p82:
        assert from_list(sol.deleteDuplicates(to_list(vals))) == e, ("P82", vals, sol)
for _ in range(5000):
    vals = sorted(random.randint(0, 4) for _ in range(random.randint(0, 9)))
    e = _p82_ref(vals)
    for sol in _p82:
        assert from_list(sol.deleteDuplicates(to_list(vals))) == e, ("P82", vals, sol)
print("P82 solutions OK")

_P82_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">1→2→3→3→4→4→5：重複的節點要「整段刪掉」，一個都不留</text>
            <g font-size="14" text-anchor="middle">
              <rect x="30" y="52" width="52" height="36" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/>
              <text x="56" y="75" fill="var(--text-muted)" font-size="10">dummy</text>
              <rect x="106" y="52" width="52" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="132" y="76" fill="var(--accent)">1</text>
              <rect x="182" y="52" width="52" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="208" y="76" fill="var(--accent)">2</text>
              <rect x="258" y="52" width="52" height="36" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="284" y="76" fill="#ff8a65">3</text>
              <rect x="334" y="52" width="52" height="36" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="360" y="76" fill="#ff8a65">3</text>
              <rect x="410" y="52" width="52" height="36" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="436" y="76" fill="#ff8a65">4</text>
              <rect x="486" y="52" width="52" height="36" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="512" y="76" fill="#ff8a65">4</text>
              <rect x="562" y="52" width="52" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="588" y="76" fill="var(--accent)">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="82" y1="70" x2="102" y2="70"/><line x1="158" y1="70" x2="178" y2="70"/>
              <line x1="234" y1="70" x2="254" y2="70"/><line x1="310" y1="70" x2="330" y2="70"/>
              <line x1="386" y1="70" x2="406" y2="70"/><line x1="462" y1="70" x2="482" y2="70"/>
              <line x1="538" y1="70" x2="558" y2="70"/>
            </g>
            <text x="322" y="108" fill="#ff8a65" font-size="12" text-anchor="middle">兩段重複，整段刪掉</text>
            <path d="M208 92 Q396 150 588 92" stroke="var(--gold)" stroke-width="2" fill="none" stroke-dasharray="5 4"/>
            <text x="396" y="140" fill="var(--gold)" font-size="12" text-anchor="middle">prev.next = cur（直接跨過整段）</text>
            <line x1="20" y1="166" x2="620" y2="166" stroke="var(--border)"/>
            <text x="20" y="194" fill="var(--text-muted)" font-size="12">結果：1 → 2 → 5</text>
            <g font-family="monospace" font-size="12">
              <text x="40" y="226" fill="var(--gold)">和第 83 題的差別：</text>
              <text x="60" y="250" fill="var(--text-muted)">第 83 題（保留一個）： 1→2→3→3→4→4→5  =&gt;  1→2→3→4→5</text>
              <text x="60" y="274" fill="var(--text-muted)">第 82 題（全部刪掉）： 1→2→3→3→4→4→5  =&gt;  1→2→5</text>
            </g>
            <text x="20" y="308" fill="#ff8a65" font-size="12">第 82 題可能刪掉頭節點（例如 1→1→2），所以必須用 dummy node。</text>'''

emit({
 "num": 82, "slug": "remove-duplicates-from-sorted-list-ii",
 "en": [
   "Given the <code>head</code> of a sorted linked list, <em>delete all nodes that have "
   "duplicate numbers, leaving only distinct numbers from the original list</em>. Return "
   "<em>the linked list <strong>sorted</strong> as well</em>.",
 ],
 "zh": [
   "給你一個<strong>已排序</strong>的鏈結串列，"
   "請刪掉<strong>所有</strong>有重複數字的節點（<strong>一個都不留</strong>），"
   "只保留原本就唯一出現的數字。回傳處理後的串列（仍然有序）。",
 ],
 "pre": [
   ("note", "和第 83 題的差別：一個都不留 vs 留一個", [
     ("c", """1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5

第 83 題（Remove Duplicates from Sorted List）：
    每個值保留一個  ->  1 -> 2 -> 3 -> 4 -> 5

第 82 題（本題）：
    有重複的「全部刪掉」 ->  1 -> 2 -> 5
                              （3 和 4 完全消失）

差別造成的三個後果：

  1. 【頭節點可能被刪掉】
     1 -> 1 -> 2  ->  答案是 2
     所以必須用 dummy node。

     第 83 題永遠會保留頭節點，所以不需要 dummy。

  2. 【要「往前看」才能決定】
     看到一個節點時，不知道它後面有沒有相同的。
     必須檢查 cur.val == cur.next.val。

  3. 【prev 的維護要小心】
     刪掉一整段之後，prev 不能前進（它還是「最後一個確定保留的」）。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [1,2,3,3,4,4,5]
  輸出：[1,2,5]

範例 2
  輸入：head = [1,1,1,2,3]
  輸出：[2,3]
  說明：頭節點被刪掉了。""",
 "constraints": [
   "串列節點數在 <code>[0, 300]</code> 範圍內（<strong>可以是空的</strong>）",
   "−100 ≤ <code>Node.val</code> ≤ 100",
   "串列已依<strong>升序</strong>排好",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>已排序</strong> —— 相同的值一定連續，所以只要和「下一個」比較。"
       "沒有這個前提就得用雜湊表先統計。",
       "<strong>串列可以是空的</strong> → 回傳 <code>None</code>。",
       "<strong>結果可能是空串列</strong>：<code>[1,1]</code> → <code>[]</code>。",
       "<strong>頭節點可能被刪掉</strong> —— <strong>這是必須用 dummy 的理由。</strong>",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P82_FIG, "0 0 640 322"),
 ],
 "approaches": [
   ap("解法一", "迴圈 + dummy node（標準解）", [
     ("c", S["p82_iter"]),
     ("h", "<code>prev</code> 的不變量"),
     ("c", """prev 永遠指向「已經確定要保留的最後一個節點」。

    初始 prev = dummy（一個一定會保留的虛擬節點）

    情況 A：cur 和後面重複
        跳過整段，prev.next = 那一段之後的第一個節點
        prev 【不動】—— 因為我們什麼都沒保留

    情況 B：cur 是獨一無二的
        prev = cur   —— 它確定被保留了
        cur = cur.next

最容易寫錯的地方：
    情況 A 裡忘記 prev 不動，寫成 prev = cur。
    那樣會把「重複段的第一個」錯誤地當成保留的節點。

    例：1 -> 1 -> 2
        如果 prev 錯誤地移到第一個 1，
        結果會是 1 -> 2（而不是 2）✘"""),
     ("h", "內層 while 的寫法"),
     ("c", """dup = cur.val
while cur and cur.val == dup:
    cur = cur.next

跑完之後，cur 指向「第一個值不等於 dup 的節點」（或 None）。

為什麼要先把 cur.val 存進 dup？
    因為迴圈裡 cur 會變，cur.val 也跟著變。
    如果直接寫 while cur and cur.val == cur.val，那永遠成立 —— 無限迴圈。

    也不能寫 while cur.next and cur.val == cur.next.val: cur = cur.next
    那樣會停在「重複段的最後一個」而不是「之後的第一個」，
    後面還要多走一步，容易漏掉。

存成區域變數是最清楚的寫法。"""),
     ("h", "為什麼不需要真的「釋放」被刪掉的節點？"),
     "在 Python 和 Java 裡，沒有人指向的節點會被垃圾回收自動處理。"
     "在 C++ 裡就要記得 <code>delete</code> —— "
     "<strong>面試時如果用 C++，主動提到這一點會加分。</strong>",
   ], "O(n)", "O(1)", "每個節點最多看兩次", "只用兩個指標", optimal=True),

   ap("解法二", "遞迴（語意最清楚）", [
     ("c", S["p82_rec"]),
     "遞迴式的語意很直白：",
     ("ul", [
       "<strong>頭節點有重複</strong> → 整段跳過，然後「處理剩下的」（結果直接回傳）",
       "<strong>頭節點唯一</strong> → 保留它，然後「處理剩下的」接到它後面",
     ]),
     ("c", """deleteDuplicates([1,1,1,2,3])
    head.val == head.next.val  ->  跳過所有的 1
    return deleteDuplicates([2,3])
        head.val=2 != 3  ->  保留 2
        2.next = deleteDuplicates([3])
                    只有一個節點 -> return [3]
        return [2,3] ✔

deleteDuplicates([1,2,2])
    1 != 2  ->  保留 1
    1.next = deleteDuplicates([2,2])
                head.val == head.next.val -> 跳過所有 2
                return deleteDuplicates([]) = None
    return [1] ✔"""),
     "<strong>不需要 dummy node</strong> —— 「這一段的新頭是誰」就是回傳值。"
     "<strong>這是遞迴版在所有串列題上的共同優勢。</strong>",
     "<strong>缺點</strong>：O(n) 的遞迴深度。n = 300 沒問題，"
     "但如果串列有 10⁵ 個節點，Python 會 <code>RecursionError</code>。",
   ], "O(n)", "O(n)", "每個節點一層遞迴", "遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "需要 dummy？", "備註"],
   [["一、迴圈", "O(n)", "O(1)", "✔ 必須", "面試預設"],
    ["二、遞迴", "O(n)", "O(n)", "✘", "語意最清楚，但吃堆疊"]]),
 "edges": [
   "<strong>空串列</strong>：<code>[]</code> → <code>[]</code>。",
   "<strong>全部重複</strong>：<code>[1,1]</code> → <code>[]</code>。<strong>結果是空串列。</strong>",
   "<strong>頭節點被刪</strong>：<code>[1,1,2]</code> → <code>[2]</code>。"
   "<strong>沒有 dummy（迴圈版）會出錯。</strong>",
   "<strong>尾節點被刪</strong>：<code>[1,2,2]</code> → <code>[1]</code>。",
   "<strong>沒有重複</strong>：<code>[1,2,3]</code> → 原樣。",
   "<strong>三個以上重複</strong>：<code>[1,1,1,2,3]</code> → <code>[2,3]</code>。",
   "<strong>多段重複</strong>：<code>[1,1,2,2]</code> → <code>[]</code>。",
   "<strong><code>prev</code> 在刪除後錯誤前進</strong>："
   "<code>[1,1,2]</code> 會回傳 <code>[1,2]</code> 而不是 <code>[2]</code>。",
 ],
 "follow": [
   ("h", "追問一：第 83 題（每個值保留一個）怎麼寫？"),
   ("c", """簡單很多 —— 不需要 dummy，也不需要 prev：

class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next    # 跳過下一個
            else:
                cur = cur.next
        return head

只有五行。

為什麼不需要 dummy？
    因為頭節點【永遠會被保留】（它是它那一組的第一個）。
    我們只刪「後面的重複」，不刪自己。

為什麼刪掉之後 cur 不能前進？
    1 -> 1 -> 1
    刪掉第二個之後是 1 -> 1，還要再刪一次。
    所以只有在「不相同」時才前進。""",),
   ("h", "追問二：如果串列沒有排序呢？"),
   "「已排序」讓「相同的值連續」成立，所以只要和鄰居比。"
   "沒排序的話要<strong>先走一遍統計每個值出現幾次</strong>（雜湊表，O(n) 空間），"
   "再走第二遍刪掉「出現次數 &gt; 1」的節點。",
   ("h", "追問三：這題和第 26／80 題（陣列版）的關係？"),
   ("c", """陣列版（第 26、80 題）：
    用「讀寫雙指標」原地覆寫，回傳新長度。
    因為陣列可以隨機存取，而且「後面的垃圾不用管」。

串列版（第 82、83 題）：
    改指標「跳過」不要的節點。
    不能覆寫（沒有「後面的垃圾」這個概念 —— 串列的長度是由連結決定的）。

    但也因此，串列版「真的」把節點移除了，
    而陣列版只是「邏輯上」縮短。

共同點：
    都依賴「已排序」讓相同的值相鄰。
    都是「一趟 O(n)、O(1) 額外空間」。

四題一起練，就把「去重」在兩種資料結構上的差異搞清楚了。""",),
 ],
 "related": [
   "<strong>第 83 題 Remove Duplicates from Sorted List</strong> —— 每個值保留一個",
   "<strong>第 26／80 題</strong> —— 陣列版的去重",
   "<strong>第 203 題 Remove Linked List Elements</strong> —— dummy node 的另一個應用",
   "<strong>第 19 題 Remove Nth Node From End</strong> —— 同樣需要 dummy",
 ],
 "check": [
   "為什麼這題必須用 dummy node，而第 83 題不用？",
   "刪掉一整段之後，<code>prev</code> 為什麼不能前進？請用 <code>[1,1,2]</code> 說明。",
   "內層 while 為什麼要先把 <code>cur.val</code> 存進區域變數？",
   "遞迴版為什麼不需要 dummy？",
 ],
})
print("P82 written")
