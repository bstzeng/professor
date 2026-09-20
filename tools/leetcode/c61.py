# -*- coding: utf-8 -*-
"""第 61–64 題。"""
import random, math
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(61)

# ==================== 61. Rotate List ====================
S["p61"] = '''class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # 第 1 步：數出長度，並找到尾節點
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n                  # 轉 n 次等於沒轉
        if k == 0:
            return head

        # 第 2 步：接成環
        tail.next = head

        # 第 3 步：走到新的尾節點（原本的第 n-k 個），在那裡斷開
        new_tail = head
        for _ in range(n - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None
        return new_head'''

S["p61_nocycle"] = '''class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head

        # 不接環的版本：用快慢指標找出「倒數第 k+1 個」節點
        slow = head
        for _ in range(n - k - 1):
            slow = slow.next

        new_head = slow.next
        slow.next = None        # 先斷開
        tail.next = head        # 再把原本的尾巴接到原本的頭
        return new_head'''

_p61 = [S.load(k) for k in ("p61", "p61_nocycle")]


def _p61_ref(vals, k):
    if not vals:
        return []
    k %= len(vals)
    return vals[-k:] + vals[:-k] if k else list(vals)


for vals, k in [([1, 2, 3, 4, 5], 2), ([0, 1, 2], 4), ([], 0), ([], 5),
                ([1], 0), ([1], 99), ([1, 2], 1), ([1, 2], 2), ([1, 2, 3], 3)]:
    e = _p61_ref(vals, k)
    for sol in _p61:
        assert from_list(sol.rotateRight(to_list(vals), k)) == e, ("P61", vals, k, sol)
for _ in range(4000):
    vals = list(range(random.randint(0, 8)))
    k = random.randint(0, 20)
    e = _p61_ref(vals, k)
    for sol in _p61:
        assert from_list(sol.rotateRight(to_list(vals), k)) == e, ("P61", vals, k, sol)
print("P61 solutions OK")

_P61_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">list = 1→2→3→4→5，k = 2：把最後 2 個搬到前面</text>
            <text x="20" y="50" fill="var(--text-muted)" font-size="12">第 1 步：接成環，並記下長度 n = 5</text>
            <g font-size="14" text-anchor="middle">
              <rect x="70" y="66" width="56" height="36" rx="6" fill="none" stroke="var(--border)"/><text x="98" y="90" fill="var(--text-muted)">1</text>
              <rect x="164" y="66" width="56" height="36" rx="6" fill="none" stroke="var(--border)"/><text x="192" y="90" fill="var(--text-muted)">2</text>
              <rect x="258" y="66" width="56" height="36" rx="6" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="286" y="90" fill="var(--gold)">3</text>
              <rect x="352" y="66" width="56" height="36" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="380" y="90" fill="#ff8a65">4</text>
              <rect x="446" y="66" width="56" height="36" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="474" y="90" fill="#ff8a65">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="126" y1="84" x2="160" y2="84"/><line x1="220" y1="84" x2="254" y2="84"/>
              <line x1="314" y1="84" x2="348" y2="84"/><line x1="408" y1="84" x2="442" y2="84"/>
            </g>
            <path d="M502 84 Q560 84 560 122 Q560 140 286 140 Q98 140 98 108" stroke="var(--accent)" stroke-width="1.8" fill="none" stroke-dasharray="5 4"/>
            <text x="300" y="158" fill="var(--accent)" font-size="11" text-anchor="middle">tail.next = head（接成環）</text>
            <text x="286" y="120" fill="var(--gold)" font-size="11" text-anchor="middle">新的尾巴</text>
            <text x="20" y="188" fill="var(--text-muted)" font-size="12">第 2 步：從 head 走 n − k − 1 = 5 − 2 − 1 = 2 步，停在節點 3，在那裡斷開</text>
            <g font-size="14" text-anchor="middle">
              <rect x="70" y="206" width="56" height="36" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="98" y="230" fill="#ff8a65">4</text>
              <rect x="164" y="206" width="56" height="36" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="192" y="230" fill="#ff8a65">5</text>
              <rect x="258" y="206" width="56" height="36" rx="6" fill="none" stroke="var(--border)"/><text x="286" y="230" fill="var(--text-muted)">1</text>
              <rect x="352" y="206" width="56" height="36" rx="6" fill="none" stroke="var(--border)"/><text x="380" y="230" fill="var(--text-muted)">2</text>
              <rect x="446" y="206" width="56" height="36" rx="6" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="474" y="230" fill="var(--gold)">3</text>
            </g>
            <g stroke="var(--gold)" stroke-width="1.5">
              <line x1="126" y1="224" x2="160" y2="224"/><line x1="220" y1="224" x2="254" y2="224"/>
              <line x1="314" y1="224" x2="348" y2="224"/><line x1="408" y1="224" x2="442" y2="224"/>
            </g>
            <text x="20" y="272" fill="var(--gold)" font-size="12">新頭 = 原本的第 n − k = 3 個節點（0-indexed 第 3 個，值是 4）</text>'''

emit({
 "num": 61, "slug": "rotate-list",
 "en": [
   "Given the <code>head</code> of a linked list, rotate the list to the right by "
   "<code>k</code> places.",
 ],
 "zh": [
   "給你一個鏈結串列的頭節點 <code>head</code>，把串列<strong>向右旋轉 <code>k</code> 格</strong>。",
   "「向右旋轉 1 格」的意思是：把最後一個節點搬到最前面。",
 ],
 "pre": [
   ("note", "兩個關鍵：取模，以及接成環", [
     ("c", """關鍵 1：k 要先對 n 取模

    轉 n 次等於沒轉（繞了一圈回到原點）。
    題目說 k 可以到 2×10⁹，而串列最多 500 個節點 ——
    不取模的話會做幾十億次無謂的旋轉。

        k %= n

    取模之後 k 一定在 [0, n-1]，最多只轉不到一圈。

關鍵 2：把串列接成環，再在正確的位置剪開

    向右轉 k 格
        <=> 新的頭是「原本的倒數第 k 個」
        <=> 新的尾是「原本的倒數第 k+1 個」
        <=> 新的尾是「原本的第 n-k 個」（1-indexed）

    1 -> 2 -> 3 -> 4 -> 5，k = 2，n = 5
        新頭 = 倒數第 2 個 = 4
        新尾 = 倒數第 3 個 = 3
        結果 4 -> 5 -> 1 -> 2 -> 3 ✔

    做法：先 tail.next = head 接成環，
          再從 head 走 n-k-1 步到新尾，
          記下 new_head = new_tail.next，
          然後 new_tail.next = None 剪開。"""),
     "<strong>「接成環再剪開」比「找到兩段再拼起來」乾淨</strong> —— "
     "因為接環之後，所有節點的相對位置都還在，只要決定「從哪裡剪」就好。",
   ]),
 ],
 "examples": """範例 1
  輸入：head = [1,2,3,4,5], k = 2
  輸出：[4,5,1,2,3]
  說明：
    轉 1 次：[5,1,2,3,4]
    轉 2 次：[4,5,1,2,3]

範例 2
  輸入：head = [0,1,2], k = 4
  輸出：[2,0,1]
  說明：4 % 3 = 1，等於只轉 1 次。""",
 "constraints": [
   "串列節點數在 <code>[0, 500]</code> 範圍內（<strong>可以是空的</strong>）",
   "−100 ≤ <code>Node.val</code> ≤ 100",
   "0 ≤ <code>k</code> ≤ 2 × 10⁹",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>串列可以是空的</strong> → 直接回傳 <code>None</code>。"
       "<strong>而且不能對空串列取模</strong>（<code>k % 0</code> 會 <code>ZeroDivisionError</code>）—— "
       "所以 <code>if not head</code> 一定要在取模之前。",
       "<strong>k 可以到 2 × 10⁹</strong>，而節點最多 500 個。"
       "<strong>不取模的話會 TLE。</strong>這就是題目給這麼大的 k 的理由。",
       "<strong>k 可以是 0</strong> → 原樣回傳。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P61_FIG, "0 0 640 288"),
 ],
 "approaches": [
   ap("解法一", "接成環，再剪開（最推薦）", [
     ("c", S["p61"]),
     ("h", "為什麼走 <code>n - k - 1</code> 步？"),
     ("c", """從 head 出發（head 是第 0 個）：
    走 0 步 -> 第 0 個
    走 m 步 -> 第 m 個

我們要停在「新的尾巴」= 原本的第 (n-k-1) 個（0-indexed）。

驗算 n=5, k=2：
    n-k-1 = 2
    走 2 步 -> 第 2 個節點（值 3）✔
    它的 next（值 4）就是新的頭 ✔

換個角度：
    新頭是「倒數第 k 個」= 第 (n-k) 個（0-indexed）
    新尾是它的前一個 = 第 (n-k-1) 個 ✔"""),
     ("h", "三個提前 return，缺一不可"),
     ("c", """if not head:          空串列 -> 不能取模（除以零），也不能走
if not head.next:     只有一個節點 -> 怎麼轉都一樣
if k == 0:            不用轉

第三個（k % n == 0）在取模之後還要再檢查一次：
    k = 5, n = 5  ->  k %= n  ->  k = 0
    這時候如果繼續走，n-k-1 = 4，
    會走到最後一個節點，new_head = tail.next = head（環！）
    然後 new_tail.next = None 剛好切回原樣 ——
    其實結果是對的，但多做了一圈無謂的操作。

    而且更重要的是：語意上「不用轉」就該直接回傳，
    讓讀程式的人一眼看懂。"""),
     ("h", "為什麼「接成環」是安全的？"),
     "因為我們<strong>立刻就會把它剪開</strong>。"
     "環只存在於函式內部的幾行之間，回傳前一定會有 <code>new_tail.next = None</code>。",
     "<strong>但這是一個要小心的操作</strong>：如果中間的邏輯出錯（例如 <code>n - k - 1</code> 算錯），"
     "就會回傳一個有環的串列，導致呼叫端無窮迴圈。"
     "<strong>測試時一定要檢查「走訪回傳的串列會不會停」</strong> —— "
     "本篇的 <code>from_list</code> 就內建了環偵測。",
   ], "O(n)", "O(1)", "走兩趟（數長度 + 找新尾）", "只用幾個指標", optimal=True),

   ap("解法二", "不接環，直接斷開再拼接", [
     "有些人不喜歡「製造環」這個中間狀態（因為出錯時很難 debug）。"
     "那就<strong>先斷開，再把原本的尾巴接到原本的頭</strong>。",
     ("c", S["p61_nocycle"]),
     ("c", """1 -> 2 -> 3 -> 4 -> 5，k = 2

  slow 走到節點 3（n-k-1 = 2 步）
  new_head = slow.next = 節點 4
  slow.next = None       ->  1 -> 2 -> 3 | 4 -> 5
  tail.next = head       ->  4 -> 5 -> 1 -> 2 -> 3 ✔

順序很重要：
    要先 slow.next = None（斷開），再 tail.next = head（接起來）。
    反過來的話，串列在中間會有一瞬間是環，
    而 slow.next = None 剛好把它剪對 —— 結果也對，
    但「先斷再接」的中間狀態比較安全（永遠不是環）。"""),
     "<strong>兩個版本完全等價</strong>，選你覺得比較不容易出錯的那個。"
     "我個人偏好這個 —— <strong>因為它在任何時刻都不會產生環</strong>，"
     "即使中途出錯，也只會得到「斷掉的串列」而不是「無窮迴圈」。",
   ], "O(n)", "O(1)", "走兩趟", "只用幾個指標"),
 ],
 "compare": (["解法", "中間狀態", "順序要求", "備註"],
   [["一、接環再剪", "會有環", "先接環，再找新尾", "最常見的寫法"],
    ["二、先斷再接", "永遠不是環", "先斷開，再接尾巴", "出錯時比較安全"]]),
 "edges": [
   "<strong>空串列</strong>：<code>([], 5)</code> → <code>[]</code>。"
   "<strong><code>k % 0</code> 會 ZeroDivisionError，所以 <code>if not head</code> 必須在取模之前。</strong>",
   "<strong>單一節點</strong>：<code>([1], 99)</code> → <code>[1]</code>。",
   "<strong>k = 0</strong>：原樣。",
   "<strong>k = n</strong>：<code>([1,2,3], 3)</code> → 原樣（取模後 k = 0）。",
   "<strong>k &gt; n</strong>：<code>([0,1,2], 4)</code> → <code>[2,0,1]</code>（4 % 3 = 1）。",
   "<strong>k = n − 1</strong>：<code>([1,2], 1)</code> → <code>[2,1]</code>。",
   "<strong>k 極大</strong>：<code>k = 2×10⁹</code>。不取模的話會跑幾十億次迴圈。",
 ],
 "follow": [
   ("h", "追問一：向「左」旋轉呢？"),
   "<strong>向左轉 k 格 = 向右轉 (n − k) 格。</strong>"
   "所以只要 <code>k = (n - k) % n</code>，其餘完全一樣。",
   ("h", "追問二：陣列版呢？"),
   "第 189 題（Rotate Array）。有一個很漂亮的 O(1) 空間解法：<strong>反轉三次</strong>。",
   ("c", """nums = [1,2,3,4,5]，k = 2

  1. 整個反轉：      [5,4,3,2,1]
  2. 反轉前 k 個：    [4,5,3,2,1]
  3. 反轉後 n-k 個：  [4,5,1,2,3] ✔

為什麼對？
    設原陣列是 A + B（A 是前 n-k 個，B 是後 k 個）
    目標是 B + A

    整個反轉      -> reverse(A+B) = reverse(B) + reverse(A)
    反轉前 k 個   -> B + reverse(A)
    反轉後 n-k 個 -> B + A  ✔

這個「三次反轉」的技巧在字串旋轉、
以及 C++ 的 std::rotate 實作裡都會用到。

串列版不適合這個做法（反轉串列要改一堆指標），
所以串列用「接環再剪」，陣列用「反轉三次」。""",),
   ("h", "追問三：如果要旋轉很多次（不同的 k）呢？"),
   "每次都 O(n) 的話總共 O(qn)。"
   "更好的做法是<strong>用循環串列（circular linked list）</strong>："
   "只維護一個「當前頭」的指標，旋轉就是移動那個指標，O(k mod n)。"
   "<strong>如果再配上雙向循環串列，還能選擇往左或往右走比較近的方向，變成 O(min(k, n-k))。</strong>"
   "這正是 Python 的 <code>collections.deque</code> 的 <code>rotate()</code> 的做法。",
 ],
 "related": [
   "<strong>第 189 題 Rotate Array</strong> —— 陣列版，「反轉三次」",
   "<strong>第 19 題 Remove Nth Node From End</strong> —— 同樣要找「倒數第 k 個」",
   "<strong>第 141／142 題 Linked List Cycle</strong> —— 環的偵測（本題會短暫製造環）",
   "<strong>第 25 題 Reverse Nodes in k-Group</strong> —— 另一個串列重接",
 ],
 "check": [
   "為什麼 <code>if not head</code> 一定要在 <code>k %= n</code> 之前？",
   "為什麼從 head 走 <code>n - k - 1</code> 步？請用 <code>n=5, k=2</code> 驗證。",
   "「先斷再接」和「先接環再剪」哪個中間狀態比較安全？為什麼？",
   "陣列版的「反轉三次」為什麼是對的？請用 A + B 的記法推導一遍。",
 ],
})
print("P61 written")

# ==================== 62. Unique Paths ====================
S["p62_dp2d"] = '''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j] = 從左上角走到 (i, j) 有幾種走法
        dp = [[1] * n for _ in range(m)]     # 第一列和第一行都只有一種走法

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]'''

S["p62_dp1d"] = '''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 只需要「上一列」的資料，所以一條陣列滾動就夠
        dp = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]     # 右邊 = 上面(舊的 dp[j]) + 左邊(新的 dp[j-1])
        return dp[n - 1]'''

S["p62_math"] = '''import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 總共要走 (m-1) 次下 + (n-1) 次右，共 m+n-2 步
        # 從這 m+n-2 步裡選 m-1 步當「下」-> C(m+n-2, m-1)
        return math.comb(m + n - 2, m - 1)'''

S["p62_manual"] = '''class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 手算 C(m+n-2, m-1)，邊乘邊除避免中間數字太大
        total = m + n - 2
        k = min(m - 1, n - 1)          # 取小的那個，乘法次數較少

        result = 1
        for i in range(1, k + 1):
            # 每一步都整除：result 累積的是 C(total-k+i, i)，一定是整數
            result = result * (total - k + i) // i
        return result'''

_p62 = [S.load(k) for k in ("p62_dp2d", "p62_dp1d", "p62_math", "p62_manual")]
for m_ in range(1, 12):
    for n_ in range(1, 12):
        e = math.comb(m_ + n_ - 2, m_ - 1)
        for sol in _p62:
            assert sol.uniquePaths(m_, n_) == e, ("P62", m_, n_, sol)
assert _p62[0].uniquePaths(3, 7) == 28
assert _p62[0].uniquePaths(3, 2) == 3
for _ in range(400):
    m_, n_ = random.randint(1, 100), random.randint(1, 100)
    e = math.comb(m_ + n_ - 2, m_ - 1)
    for sol in _p62[1:]:
        assert sol.uniquePaths(m_, n_) == e, ("P62", m_, n_, sol)
print("P62 solutions OK")

_P62_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">m = 3, n = 7 的 dp 表：每一格 = 上面 + 左邊</text>
            <g font-size="13" text-anchor="middle">
              <rect x="60" y="46" width="72" height="40" fill="none" stroke="var(--accent)"/><text x="96" y="72" fill="var(--accent)">1</text>
              <rect x="132" y="46" width="72" height="40" fill="none" stroke="var(--accent)"/><text x="168" y="72" fill="var(--accent)">1</text>
              <rect x="204" y="46" width="72" height="40" fill="none" stroke="var(--accent)"/><text x="240" y="72" fill="var(--accent)">1</text>
              <rect x="276" y="46" width="72" height="40" fill="none" stroke="var(--accent)"/><text x="312" y="72" fill="var(--accent)">1</text>
              <rect x="348" y="46" width="72" height="40" fill="none" stroke="var(--accent)"/><text x="384" y="72" fill="var(--accent)">1</text>
              <rect x="420" y="46" width="72" height="40" fill="none" stroke="var(--accent)"/><text x="456" y="72" fill="var(--accent)">1</text>
              <rect x="492" y="46" width="72" height="40" fill="none" stroke="var(--accent)"/><text x="528" y="72" fill="var(--accent)">1</text>

              <rect x="60" y="86" width="72" height="40" fill="none" stroke="var(--accent)"/><text x="96" y="112" fill="var(--accent)">1</text>
              <rect x="132" y="86" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="168" y="112" fill="var(--text-muted)">2</text>
              <rect x="204" y="86" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="240" y="112" fill="var(--text-muted)">3</text>
              <rect x="276" y="86" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="312" y="112" fill="var(--text-muted)">4</text>
              <rect x="348" y="86" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="384" y="112" fill="var(--text-muted)">5</text>
              <rect x="420" y="86" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="456" y="112" fill="var(--text-muted)">6</text>
              <rect x="492" y="86" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="528" y="112" fill="var(--text-muted)">7</text>

              <rect x="60" y="126" width="72" height="40" fill="none" stroke="var(--accent)"/><text x="96" y="152" fill="var(--accent)">1</text>
              <rect x="132" y="126" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="168" y="152" fill="var(--text-muted)">3</text>
              <rect x="204" y="126" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="240" y="152" fill="var(--text-muted)">6</text>
              <rect x="276" y="126" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="312" y="152" fill="var(--text-muted)">10</text>
              <rect x="348" y="126" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="384" y="152" fill="var(--text-muted)">15</text>
              <rect x="420" y="126" width="72" height="40" fill="none" stroke="var(--text-muted)"/><text x="456" y="152" fill="var(--text-muted)">21</text>
              <rect x="492" y="126" width="72" height="40" fill="none" stroke="#ff8a65" stroke-width="2.5"/><text x="528" y="152" fill="#ff8a65">28</text>
            </g>
            <text x="20" y="196" fill="var(--accent)" font-size="12">第一列和第一行都是 1：只能一直往右（或一直往下），只有一種走法</text>
            <text x="20" y="222" fill="var(--text-muted)" font-size="12">其他格子：要到 (i,j)，最後一步只可能從上面或左邊來 → dp[i][j] = dp[i−1][j] + dp[i][j−1]</text>
            <text x="20" y="250" fill="var(--gold)" font-size="12">注意這張表就是「斜著擺的巴斯卡三角形」——  dp[i][j] = C(i+j, i)</text>
            <text x="20" y="274" fill="#ff8a65" font-size="12">答案 28 = C(8, 2) = 8! / (2! · 6!) = 28 ✔</text>'''

emit({
 "num": 62, "slug": "unique-paths",
 "en": [
   "There is a robot on an <code>m x n</code> grid. The robot is initially located at the "
   "<strong>top-left corner</strong>. The robot tries to move to the "
   "<strong>bottom-right corner</strong>. The robot can only move either "
   "<strong>down</strong> or <strong>right</strong> at any point in time.",
   "Given the two integers <code>m</code> and <code>n</code>, return <em>the number of "
   "possible unique paths that the robot can take to reach the bottom-right corner</em>.",
 ],
 "zh": [
   "一個機器人位於 <code>m × n</code> 網格的<strong>左上角</strong>，"
   "想要走到<strong>右下角</strong>。"
   "它<strong>每一步只能往下或往右</strong>。",
   "給你 <code>m</code> 和 <code>n</code>，回傳總共有幾種不同的走法。",
 ],
 "pre": [
   ("note", "兩種完全不同的思路，答案一樣", [
     ("c", """思路 A：動態規劃

    要到達 (i, j)，最後一步只可能是
        從 (i-1, j) 往下走，或
        從 (i, j-1) 往右走

    所以 dp[i][j] = dp[i-1][j] + dp[i][j-1]

    邊界：第一列和第一行都是 1（只有一條路）

思路 B：組合數學

    從左上走到右下，總共要走
        (m-1) 次「下」 + (n-1) 次「右」 = m+n-2 步

    這 m+n-2 步的順序決定了路徑。
    所以問題等價於：
        「在 m+n-2 個位置裡，選 m-1 個放『下』，有幾種選法？」

        答案 = C(m+n-2, m-1)

    m=3, n=7：C(8, 2) = 28 ✔

思路 B 是 O(min(m,n)) 的，比 DP 的 O(mn) 快得多。
但思路 A 能推廣到「有障礙物」（第 63 題）和「有權重」（第 64 題），
思路 B 不行。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：m = 3, n = 7
  輸出：28

範例 2
  輸入：m = 3, n = 2
  輸出：3
  說明：
    1. 下 → 下 → 右
    2. 下 → 右 → 下
    3. 右 → 下 → 下""",
 "constraints": [
   "1 ≤ <code>m</code>, <code>n</code> ≤ 100",
   "題目保證答案不超過 2 × 10⁹",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>m, n ≤ 100</strong>，所以 DP 的 O(mn) = 10⁴ —— 瞬間完成。"
       "這題不考效率，考的是<strong>你能不能看出它是 DP，以及能不能看出它其實是組合數</strong>。",
       "<strong>答案不超過 2 × 10⁹</strong> —— 剛好超過 32 位元有號整數（2¹⁵ ≈ 2.1 × 10⁹）。"
       "在 Java 裡用 <code>int</code> 剛好夠（因為題目保證了上界），但很危險。"
       "<strong>而組合數的中間計算很容易溢位</strong> —— 見解法四。",
       "<strong>m 或 n 可以是 1</strong> → 答案是 1（只能一直走）。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P62_FIG, "0 0 640 288"),
 ],
 "approaches": [
   ap("解法一", "二維 DP（最直白）", [
     ("c", S["p62_dp2d"]),
     "初始化的 <code>[[1] * n for _ in range(m)]</code> 一次搞定了第一列和第一行 —— "
     "它們都只有一種走法。",
     "<strong>注意不能寫 <code>[[1] * n] * m</code></strong>！"
     "那樣 m 個列會是<strong>同一個 list 物件</strong>，改一個就全部都改。"
     "<strong>這是 Python 建二維陣列最經典的陷阱。</strong>",
     "O(mn) 時間、O(mn) 空間。清楚，而且可以直接推廣到第 63、64 題。",
   ], "O(m·n)", "O(m·n)", "填滿整張表", "dp 表"),

   ap("解法二", "一維 DP（滾動陣列）", [
     "<code>dp[i][j]</code> 只依賴<strong>上一列同欄</strong>和<strong>同一列左邊一欄</strong>，"
     "所以一條長度 <code>n</code> 的陣列就夠。",
     ("c", S["p62_dp1d"]),
     ("h", "<code>dp[j] += dp[j-1]</code> 這一行為什麼是對的？"),
     ("c", """在處理第 i 列、第 j 欄的時候：

    dp[j]     還沒更新 -> 它是「上一列」的值 = dp[i-1][j]
    dp[j-1]   已經更新 -> 它是「這一列」的值 = dp[i][j-1]

    dp[j] = dp[j] + dp[j-1]
          = dp[i-1][j] + dp[i][j-1]  ✔ 正是轉移式

關鍵：j 必須「從左往右」跑。
      這樣 dp[j-1] 才會是「已經更新的新值」，
      而 dp[j] 還是「還沒更新的舊值」。

如果從右往左跑，dp[j-1] 會是舊值（上一列的），就錯了。

「滾動陣列的迴圈方向」是所有 DP 空間優化的核心問題：
    需要「上一列」的舊值 -> 某些方向
    需要「這一列」的新值 -> 另一些方向
    有時候還得倒著跑（例如 0/1 背包）。

判斷方法：把轉移式攤開，看每一項需要新的還是舊的。"""),
     "<strong>O(n) 空間</strong>。在 m, n ≤ 100 時沒差，"
     "但如果 n 到 10⁵，這個優化就是必要的。",
   ], "O(m·n)", "O(n)", "同上", "一條長度 n 的陣列", optimal=True),

   ap("解法三", "直接算組合數（最快）", [
     ("c", S["p62_math"]),
     "<strong>一行</strong>。Python 3.8+ 有 <code>math.comb</code>，"
     "它的實作是高度優化的 C 程式碼。",
     ("c", """為什麼是 C(m+n-2, m-1)？

    任何一條路徑，都可以寫成一串「下」和「右」：
        m=3, n=7 -> "下下右右右右右右"（2 個下、6 個右）

    不同的路徑 <=> 不同的排列
    而這種「只有兩種符號」的排列數，就是組合數：
        C(總步數, 下的次數) = C(8, 2) = 28

    也可以寫成 C(m+n-2, n-1)，兩者相等
    （C(8,2) == C(8,6)）。

驗證小例子 m=3, n=2：
    C(3+2-2, 3-1) = C(3, 2) = 3 ✔"""),
     "<strong>複雜度是 O(min(m,n))</strong>（<code>math.comb</code> 的實作），"
     "遠優於 DP 的 O(mn)。",
     "<strong>但它完全無法推廣</strong> —— 一旦有障礙物或權重，組合公式就失效了。"
     "<strong>面試時建議：先講 DP（展示你會建模），再說「其實這是組合數，可以 O(min(m,n))」。</strong>",
   ], "O(min(m,n))", "O(1)", "組合數的計算", "幾個變數"),

   ap("解法四", "手算組合數（不用內建函式，避免溢位）", [
     "如果不能用 <code>math.comb</code>（或在 C/Java 裡），"
     "就要自己算 —— 而且要小心<strong>不要先算階乘再相除</strong>。",
     ("c", S["p62_manual"]),
     ("h", "為什麼要「邊乘邊除」？"),
     ("c", """錯誤寫法：
    return factorial(m+n-2) // (factorial(m-1) * factorial(n-1))

    m = n = 100 時，(m+n-2)! = 198! ≈ 10^372
    在 Python 裡算得出來（但很慢），
    在 C/Java 裡早就溢位了。

正確寫法：
    C(N, k) = (N-k+1)/1 × (N-k+2)/2 × ... × N/k

    for i in 1..k:
        result = result * (N-k+i) // i

    每一步的 result 都是 C(N-k+i, i)，
    是一個組合數，所以「一定是整數」——
    整數除法不會有誤差。

    而中間值最大就是答案本身（2×10⁹），不會溢位。

為什麼每一步都整除？
    result_i = C(N-k+i, i)
    result_{i} = result_{i-1} × (N-k+i) / i
               = C(N-k+i-1, i-1) × (N-k+i) / i

    由組合數的遞推恆等式，這確實等於 C(N-k+i, i)，
    而組合數一定是整數 ✔

    但注意：「result × (N-k+i)」這一步之後才除以 i，
    順序不能顛倒（先除會有餘數損失）。"""),
     "<strong><code>k = min(m-1, n-1)</code></strong>：利用 "
     "<code>C(N,k) == C(N,N-k)</code>，取小的那個可以少跑一半的迴圈，"
     "中間值也更小。",
   ], "O(min(m,n))", "O(1)", "min(m,n) 次乘除", "一個變數"),
 ],
 "compare": (["解法", "時間", "空間", "可推廣到第 63／64 題？", "備註"],
   [["一、二維 DP", "O(mn)", "O(mn)", "✔", "最直白"],
    ["二、一維 DP", "O(mn)", "O(n)", "✔", "滾動陣列"],
    ["三、math.comb", "O(min)", "O(1)", "✘", "最快，一行"],
    ["四、手算組合", "O(min)", "O(1)", "✘", "避免溢位的標準寫法"]]),
 "edges": [
   "<strong>m = 1 或 n = 1</strong>：答案是 1。DP 的初始化直接回傳 1；組合數是 <code>C(k, 0) = 1</code>。",
   "<strong>m = n = 1</strong>：答案 1（起點就是終點，走 0 步）。",
   "<strong>m = 3, n = 2</strong>：3。最小的非平凡例子。",
   "<strong>m = n = 100</strong>：答案是 <code>C(198, 99)</code>，"
   "約 2.25 × 10⁵⁸ —— <strong>遠超題目說的 2 × 10⁹</strong>！"
   "所以題目的「保證不超過 2 × 10⁹」暗示測資不會給到 100 × 100。"
   "（實際上 LeetCode 的測資最大大約是 <code>m = 3, n = 28</code> 這種等級。）",
   "<strong>Python 建二維陣列</strong>：<code>[[1] * n] * m</code> 是錯的，"
   "要用 <code>[[1] * n for _ in range(m)]</code>。",
   "<strong>先算階乘再除</strong>：在 C/Java 裡會溢位。",
 ],
 "follow": [
   ("h", "追問一：如果有障礙物呢？"),
   "第 63 題。DP 幾乎不用改：<strong>障礙物那一格的 <code>dp</code> 設成 0</strong>。"
   "但組合公式完全失效 —— <strong>這就是為什麼 DP 值得先學。</strong>",
   ("h", "追問二：如果每一格有「成本」，要求最小成本路徑呢？"),
   "第 64 題。轉移式從「相加」變成「取 min 再加上自己」："
   "<code>dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]</code>。"
   "<strong>同一張 DP 表，換一個運算，答案完全不同。</strong>",
   ("h", "追問三：這張 DP 表和巴斯卡三角形是什麼關係？"),
   ("c", """dp[i][j] = dp[i-1][j] + dp[i][j-1]

這和巴斯卡三角形的遞推式
    C(n, k) = C(n-1, k-1) + C(n-1, k)
是同一個式子，只是座標系旋轉了 45 度。

事實上 dp[i][j] = C(i+j, i)。

    dp[2][6] = C(8, 2) = 28 ✔

所以這張表「就是」巴斯卡三角形，斜著擺而已。

這也解釋了為什麼組合公式會出現 ——
不是巧合，是同一個遞推結構的兩種計算方式：
    DP 是「自底向上填表」，
    組合公式是「直接套封閉形式」。""",),
   ("h", "追問四：如果可以往上下左右四個方向走呢？"),
   "<strong>路徑數會變成無限大</strong>（可以繞圈）。"
   "所以題目必須限制方向（或限制「不能重複經過同一格」，"
   "那就變成計算自迴避路徑（self-avoiding walk）—— 一個著名的難題，"
   "連 n × n 網格的路徑數都沒有封閉公式）。",
   "<strong>「只能往下或往右」這個限制，正是讓這題有優雅解答的原因。</strong>",
 ],
 "related": [
   "<strong>第 63 題 Unique Paths II</strong> —— 有障礙物",
   "<strong>第 64 題 Minimum Path Sum</strong> —— 有權重，求最小",
   "<strong>第 120 題 Triangle</strong> —— 三角形上的同一種 DP",
   "<strong>第 931 題 Minimum Falling Path Sum</strong> —— 三個方向的版本",
 ],
 "check": [
   "為什麼 <code>dp[i][j] = dp[i-1][j] + dp[i][j-1]</code>？「最後一步」的視角是什麼？",
   "一維 DP 的內層迴圈為什麼必須「從左往右」？從右往左會錯在哪？",
   "組合公式 <code>C(m+n-2, m-1)</code> 是怎麼來的？請用「下下右右右」的排列說明。",
   "<code>[[1] * n] * m</code> 為什麼是錯的？",
 ],
})
print("P62 written")
