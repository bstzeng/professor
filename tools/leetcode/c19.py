# -*- coding: utf-8 -*-
"""第 19–22 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(19)

# ==================== 19. Remove Nth Node From End of List ====================
S["p19_two_pass"] = '''class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 第一趟：算出總長度
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        # 倒數第 n 個 = 正數第 (length - n) 個（0-indexed）
        # 我們要停在它「前面」那個節點
        dummy = ListNode(0, head)      # 虛擬頭節點，讓「刪掉第一個」不用特判
        prev = dummy
        for _ in range(length - n):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next'''

S["p19_one_pass"] = '''class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy

        # 先讓 fast 走 n + 1 步，製造出「n 的間距」
        # （多走 1 步是為了讓 slow 最後停在「要刪的那個」前面）
        for _ in range(n + 1):
            fast = fast.next

        # 兩個一起走，fast 到底時 slow 剛好在正確位置
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next'''

S["p19_recursive"] = '''class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(node):
            """回傳 (處理後的子串列, 這個節點是倒數第幾個)"""
            if node is None:
                return None, 0

            node.next, idx = helper(node.next)
            idx += 1                    # 加上自己

            if idx == n:                # 自己就是要刪的那個
                return node.next, idx
            return node, idx

        new_head, _ = helper(head)
        return new_head'''

_p19 = [S.load(k) for k in ("p19_two_pass", "p19_one_pass", "p19_recursive")]
for vals, n in [([1, 2, 3, 4, 5], 2), ([1], 1), ([1, 2], 1), ([1, 2], 2),
                ([1, 2, 3], 3), ([1, 2, 3], 1)]:
    e = vals[:len(vals) - n] + vals[len(vals) - n + 1:]
    for sol in _p19:
        assert from_list(sol.removeNthFromEnd(to_list(vals), n)) == e, ("P19", vals, n, sol)
for _ in range(3000):
    k = random.randint(1, 8)
    vals = list(range(k))
    n = random.randint(1, k)
    e = vals[:k - n] + vals[k - n + 1:]
    for sol in _p19:
        assert from_list(sol.removeNthFromEnd(to_list(vals), n)) == e, ("P19", vals, n, sol)
print("P19 solutions OK")

_P19_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">list = 1→2→3→4→5，n = 2（要刪掉 4）。dummy 讓「刪第一個」不需要特判。</text>
            <g font-size="14" text-anchor="middle">
              <rect x="34" y="52" width="60" height="38" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/>
              <text x="64" y="76" fill="var(--text-muted)" font-size="11">dummy</text>
              <rect x="120" y="52" width="60" height="38" rx="6" fill="none" stroke="var(--border)"/><text x="150" y="77" fill="var(--text-muted)">1</text>
              <rect x="206" y="52" width="60" height="38" rx="6" fill="none" stroke="var(--border)"/><text x="236" y="77" fill="var(--text-muted)">2</text>
              <rect x="292" y="52" width="60" height="38" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="322" y="77" fill="var(--accent)">3</text>
              <rect x="378" y="52" width="60" height="38" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="408" y="77" fill="#ff8a65">4</text>
              <rect x="464" y="52" width="60" height="38" rx="6" fill="none" stroke="var(--border)"/><text x="494" y="77" fill="var(--text-muted)">5</text>
              <rect x="550" y="52" width="60" height="38" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="3 3"/>
              <text x="580" y="76" fill="var(--text-muted)" font-size="11">None</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="94" y1="71" x2="116" y2="71"/><line x1="180" y1="71" x2="202" y2="71"/>
              <line x1="266" y1="71" x2="288" y2="71"/><line x1="352" y1="71" x2="374" y2="71"/>
              <line x1="438" y1="71" x2="460" y2="71"/><line x1="524" y1="71" x2="546" y2="71"/>
            </g>
            <text x="322" y="112" fill="var(--accent)" font-size="12" text-anchor="middle">slow</text>
            <text x="580" y="112" fill="var(--gold)" font-size="12" text-anchor="middle">fast</text>
            <path d="M322 122 Q451 150 580 122" stroke="var(--gold)" stroke-width="1.5" fill="none" stroke-dasharray="5 4"/>
            <text x="451" y="150" fill="var(--gold)" font-size="11" text-anchor="middle">固定間距 n + 1 = 3</text>
            <text x="20" y="184" fill="var(--text-muted)" font-size="12">起手式：fast 從 dummy 先走 3 步到 &quot;3&quot;、slow 留在 dummy，然後兩個一起走。</text>
            <text x="20" y="206" fill="var(--text-muted)" font-size="12">fast 走到 None 時，slow 剛好停在 &quot;3&quot; —— 也就是要刪的 &quot;4&quot; 的前一個。</text>
            <text x="20" y="232" fill="var(--gold)" font-size="12">slow.next = slow.next.next → 3 直接指向 5，節點 4 被摘掉。</text>'''

emit({
 "num": 19, "slug": "remove-nth-node-from-end-of-list",
 "en": [
   "Given the <code>head</code> of a linked list, remove the <code>n</code>-th node from the "
   "end of the list and return its head.",
   "<strong>Follow up:</strong> Could you do this in one pass?",
 ],
 "zh": [
   "給你一個鏈結串列的頭節點 <code>head</code>，刪掉<strong>倒數第 <code>n</code> 個</strong>節點，"
   "然後回傳串列的頭節點。",
   "<strong>進階：</strong>能不能只走<strong>一趟</strong>就做到？",
 ],
 "pre": [
   ("note", "兩個技巧，這題就是在教這兩個", [
     ("c", """技巧 1：虛擬頭節點（dummy node）

    沒有 dummy 時，「刪掉第一個節點」要特別處理：
        if 要刪的是 head:
            return head.next
        else:
            ...正常的刪法...

    有了 dummy 之後：
        dummy -> 1 -> 2 -> 3
        「刪掉 1」和「刪掉 2」變成完全一樣的操作，
        因為 1 也有「前一個節點」了。

    這個技巧在所有「可能會刪／改到頭節點」的串列題都適用。

技巧 2：快慢指標製造固定間距

    要找「倒數第 n 個」，不必先知道總長度。
    讓一個指標先走 n 步，然後兩個一起走 ——
    快的到終點時，慢的就在倒數第 n 個。

    這是「一趟」的關鍵。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [1,2,3,4,5], n = 2
  輸出：[1,2,3,5]
  說明：倒數第 2 個是 4，把它刪掉。

範例 2
  輸入：head = [1], n = 1
  輸出：[]
  說明：刪掉唯一的節點，變成空串列。

範例 3
  輸入：head = [1,2], n = 1
  輸出：[1]""",
 "constraints": [
   "串列節點數是 <code>sz</code>，1 ≤ <code>sz</code> ≤ 30",
   "0 ≤ <code>Node.val</code> ≤ 100",
   "1 ≤ <code>n</code> ≤ <code>sz</code>（<strong>保證 n 不會超出範圍</strong>）",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>保證 1 ≤ n ≤ sz</strong>，所以不用處理「n 太大」或「n 是 0」。"
       "但你的程式在 <code>n == sz</code>（刪頭）和 <code>n == 1</code>（刪尾）"
       "這兩個邊界上都必須正確。",
       "<strong>串列至少有一個節點</strong>，但<strong>刪完之後可能變成空的</strong>，"
       "所以回傳值要能是 <code>None</code>。",
       "規模只有 30，效率完全不是重點。這題考的是<strong>指標操作的乾淨度</strong>，"
       "以及你知不知道 dummy node 這個技巧。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P19_FIG, "0 0 640 246"),
 ],
 "approaches": [
   ap("解法一", "兩趟：先數長度，再走到位置", [
     "最直觀：第一趟數出總長度 <code>L</code>，倒數第 <code>n</code> 個就是正數第 "
     "<code>L − n</code> 個（0-indexed）。第二趟走 <code>L − n</code> 步停在它前面。",
     ("c", S["p19_two_pass"]),
     ("h", "為什麼是走 <code>L − n</code> 步而不是 <code>L − n − 1</code>？"),
     ("c", """L = 5, n = 2，要刪的是值 4（0-indexed 的第 3 個）

從 dummy 出發：
    走 0 步 -> dummy
    走 1 步 -> 節點 1
    走 2 步 -> 節點 2
    走 3 步 -> 節點 3   <- 這就是「要刪的那個」的前一個

L - n = 5 - 2 = 3 ✔

關鍵：因為起點是 dummy（在 head 前面一格），
      走 k 步會停在「第 k 個節點」，
      而不是「第 k+1 個節點」。
      dummy 幫我們自動處理掉這個 off-by-one。"""),
     "這個解法完全正確，只是走了兩趟。"
     "<strong>題目的 follow-up 就是在問：能不能一趟？</strong>",
   ], "O(L)", "O(1)", "走兩趟，共 2L 步", "只有幾個指標"),

   ap("解法二", "一趟：快慢指標固定間距（標準解）", [
     "核心想法：<strong>不需要知道總長度，只需要知道「間距」。</strong>"
     "讓 <code>fast</code> 先走 <code>n + 1</code> 步，然後兩個一起走。"
     "當 <code>fast</code> 走到 <code>None</code> 時，<code>slow</code> 和終點的距離就是 <code>n + 1</code> —— "
     "也就是說它剛好停在「倒數第 n 個」的前一個。",
     ("c", S["p19_one_pass"]),
     ("h", "為什麼是 <code>n + 1</code> 步而不是 <code>n</code> 步？"),
     ("c", """如果只走 n 步：
    fast 到 None 時，slow 停在「倒數第 n 個」本身。
    但要刪除一個節點，你需要它的「前一個」（單向串列沒辦法往回走）。

多走 1 步，slow 就落後一格，剛好停在前一個。

驗算（L = 5, n = 2）：
    dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
      ↑
     both

    fast 走 3 步：fast 在節點 3，slow 在 dummy
    一起走：fast=4, slow=1
    一起走：fast=5, slow=2
    一起走：fast=None, slow=3   <- 停
    slow.next = slow.next.next  ->  3 指向 5，刪掉 4 ✔"""),
     ("h", "<code>n == L</code>（刪頭）為什麼也對？"),
     ("c", """L = 1, n = 1：  dummy -> 1 -> None

    fast 走 n+1 = 2 步：dummy -> 1 -> None，fast = None
    while fast: 不執行
    slow 還在 dummy
    slow.next = slow.next.next  ->  dummy.next = None
    return dummy.next = None  ✔ 空串列

沒有 dummy 的話，這裡 slow 會是 None，
slow.next 直接 AttributeError。
這就是 dummy 最大的價值。"""),
     "<strong>「先讓一個指標走 k 步製造間距」是快慢指標的一種。</strong>"
     "另外兩種常見的是「一步 vs 兩步」（找中點、判斷有沒有環）"
     "和「同速但起點不同」（找兩個串列的交點）。三種都要會。",
   ], "O(L)", "O(1)", "只走一趟", "兩個指標", optimal=True),

   ap("解法三", "遞迴：回傳「倒數第幾個」", [
     "遞迴天生就是「從後往前」的 —— 遞迴回來的時候，正好是從尾巴往頭走。"
     "利用這一點，讓每一層回報「我是倒數第幾個」。",
     ("c", S["p19_recursive"]),
     ("h", "為什麼 <code>node.next, idx = helper(node.next)</code> 這一行同時做兩件事？"),
     "它把「子串列處理完的結果」接回來（可能少了一個節點），"
     "同時拿到「子串列有幾個節點」。"
     "加上自己就是 <code>idx + 1</code>，"
     "如果剛好等於 <code>n</code>，就回傳 <code>node.next</code>（跳過自己）。",
     "<strong>優點</strong>：完全不需要 dummy node —— "
     "「刪掉頭節點」被 <code>return node.next</code> 自然處理掉了。",
     "<strong>缺點</strong>：O(L) 的遞迴堆疊。L = 30 沒問題，"
     "但如果串列有 10⁵ 個節點，Python 預設的遞迴上限（1000）會直接爆掉。",
     "面試時寫這個版本要主動提到堆疊深度的問題 —— 不然會被認為沒想到。",
   ], "O(L)", "O(L)", "走一趟（遞迴下去再回來）", "遞迴堆疊"),
 ],
 "compare": (["解法", "趟數", "空間", "需要 dummy？", "備註"],
   [["一、兩趟", "2", "O(1)", "建議用", "最直觀"],
    ["二、快慢指標", "1", "O(1)", "強烈建議", "標準解，答到 follow-up"],
    ["三、遞迴", "1", "O(L)", "不需要", "優雅但吃堆疊"]]),
 "edges": [
   "<strong>只有一個節點，刪它</strong>：<code>([1], 1)</code> → <code>[]</code>。回傳 <code>None</code>。",
   "<strong>刪頭</strong>：<code>([1,2], 2)</code> → <code>[2]</code>。<strong>沒有 dummy 就會在這裡炸掉。</strong>",
   "<strong>刪尾</strong>：<code>([1,2], 1)</code> → <code>[1]</code>。",
   "<strong>n 等於長度</strong>：<code>([1,2,3], 3)</code> → <code>[2,3]</code>。",
   "<strong>n 等於 1</strong>：<code>([1,2,3], 1)</code> → <code>[1,2]</code>。",
   "<strong>fast 走 n+1 步時可能剛好走到 None</strong>：這是合法的（表示要刪頭），"
   "不能在迴圈裡加 <code>if fast is None: return</code> 之類的早退。",
 ],
 "follow": [
   ("h", "追問一：如果 n 可能超過串列長度呢？"),
   "快慢指標版本會在「先走 n+1 步」的迴圈裡對 <code>None</code> 取 <code>.next</code> 而崩潰。"
   "要加一個檢查：",
   ("c", """for _ in range(n + 1):
    if fast is None:
        return head        # n 太大，什麼都不刪（或依規格拋錯）
    fast = fast.next"""),
   "<strong>題目保證了 n 合法，所以不用寫。但面試官很可能追問這個。</strong>",
   ("h", "追問二：如果是雙向串列呢？"),
   "雙向串列可以從尾巴往前走 n 步，直接找到目標，而且刪除只要改兩個指標"
   "（<code>node.prev.next = node.next</code>、<code>node.next.prev = node.prev</code>）。"
   "但如果沒有存 tail 指標，還是得先走到尾巴 —— 複雜度一樣。",
   ("h", "追問三：這個「固定間距」的技巧還能用在哪？"),
   ("ul", [
     "<strong>找中點</strong>（第 876 題）：一步 vs 兩步，快的到終點時慢的在中間",
     "<strong>判斷有沒有環</strong>（第 141 題）：快慢指標會相遇",
     "<strong>找環的起點</strong>（第 142 題）：相遇後從頭再放一個指標，同速前進",
     "<strong>找兩串列的交點</strong>（第 160 題）：走完自己再走對方，抵銷長度差",
   ]),
   "這四題加上本題，構成了鏈結串列雙指標的完整套路。",
 ],
 "related": [
   "<strong>第 876 題 Middle of the Linked List</strong> —— 快慢指標找中點",
   "<strong>第 141／142 題 Linked List Cycle</strong> —— 快慢指標判環",
   "<strong>第 203 題 Remove Linked List Elements</strong> —— dummy node 的另一個應用",
 ],
 "check": [
   "為什麼 <code>fast</code> 要先走 <code>n + 1</code> 步而不是 <code>n</code> 步？",
   "不用 dummy node 的話，<code>([1], 1)</code> 會在哪一行崩潰？",
   "遞迴解法為什麼不需要 dummy？它用什麼取代了 dummy 的功能？",
   "如果 <code>n</code> 可能大於串列長度，快慢指標版要改哪裡？",
 ],
})
print("P19 written")

# ==================== 20. Valid Parentheses ====================
S["p20_stack"] = '''class Solution:
    def isValid(self, s: str) -> bool:
        PAIR = {")": "(", "]": "[", "}": "{"}    # 右括號 -> 對應的左括號
        stack = []

        for ch in s:
            if ch in PAIR:                        # 是右括號
                # 堆疊空了，或頂端不是配對的左括號 -> 失敗
                if not stack or stack.pop() != PAIR[ch]:
                    return False
            else:                                 # 是左括號
                stack.append(ch)

        return not stack       # 必須剛好清空；還有剩表示有左括號沒關'''

S["p20_replace"] = '''class Solution:
    def isValid(self, s: str) -> bool:
        # 反覆把最內層的一對消掉，直到消不動為止
        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""'''

_p20a, _p20b = S.load("p20_stack"), S.load("p20_replace")
for s_ in ["()", "()[]{}", "(]", "([])", "([)]", "", "(", ")", "{[]}",
           "(((((((((())))))))))", "]", "([{}])", "(()"]:
    assert _p20a.isValid(s_) == _p20b.isValid(s_), ("P20", s_, _p20a.isValid(s_), _p20b.isValid(s_))
assert _p20a.isValid("()[]{}") is True and _p20a.isValid("(]") is False
for _ in range(6000):
    s_ = "".join(random.choice("()[]{}") for _ in range(random.randint(0, 10)))
    assert _p20a.isValid(s_) == _p20b.isValid(s_), ("P20", s_, _p20a.isValid(s_), _p20b.isValid(s_))
print("P20 solutions OK")

_P20_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">s = &quot;{[()]}&quot;：左括號進堆疊，右括號要和堆疊頂端配對</text>
            <g font-family="monospace" font-size="15" text-anchor="middle">
              <text x="70" y="52" fill="var(--text-muted)" font-size="12">讀到</text>
              <text x="140" y="52" fill="var(--accent)">{</text>
              <text x="220" y="52" fill="var(--accent)">[</text>
              <text x="300" y="52" fill="var(--accent)">(</text>
              <text x="380" y="52" fill="#ff8a65">)</text>
              <text x="460" y="52" fill="#ff8a65">]</text>
              <text x="540" y="52" fill="#ff8a65">}</text>
            </g>
            <text x="70" y="90" fill="var(--text-muted)" font-size="12">堆疊</text>
            <g font-size="12" text-anchor="middle" font-family="monospace">
              <rect x="116" y="132" width="48" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="140" y="150" fill="var(--accent)">{</text>

              <rect x="196" y="132" width="48" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="220" y="150" fill="var(--accent)">{</text>
              <rect x="196" y="102" width="48" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="220" y="120" fill="var(--accent)">[</text>

              <rect x="276" y="132" width="48" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="300" y="150" fill="var(--accent)">{</text>
              <rect x="276" y="102" width="48" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="300" y="120" fill="var(--accent)">[</text>
              <rect x="276" y="72" width="48" height="26" rx="4" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="300" y="90" fill="var(--gold)">(</text>

              <rect x="356" y="132" width="48" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="380" y="150" fill="var(--accent)">{</text>
              <rect x="356" y="102" width="48" height="26" rx="4" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="380" y="120" fill="var(--gold)">[</text>

              <rect x="436" y="132" width="48" height="26" rx="4" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="460" y="150" fill="var(--gold)">{</text>

              <rect x="516" y="132" width="48" height="26" rx="4" fill="none" stroke="var(--border)" stroke-dasharray="3 3"/><text x="540" y="150" fill="var(--text-muted)" font-size="10">空</text>
            </g>
            <line x1="100" y1="166" x2="580" y2="166" stroke="var(--border)"/>
            <g font-size="11" text-anchor="middle" fill="var(--text-muted)">
              <text x="140" y="184">push</text>
              <text x="220" y="184">push</text>
              <text x="300" y="184">push</text>
              <text x="380" y="184">pop (</text>
              <text x="460" y="184">pop [</text>
              <text x="540" y="184">pop {</text>
            </g>
            <text x="20" y="216" fill="var(--gold)" font-size="12">結束時堆疊為空 → 合法 ✔　若還有剩（例如 &quot;(()&quot;）→ 不合法</text>
            <text x="20" y="240" fill="#ff8a65" font-size="12">&quot;([)]&quot; 會在讀到 &quot;)&quot; 時發現頂端是 &quot;[&quot; 而不是 &quot;(&quot; → 立刻失敗</text>'''

emit({
 "num": 20, "slug": "valid-parentheses",
 "en": [
   "Given a string <code>s</code> containing just the characters "
   "<code>'('</code>, <code>')'</code>, <code>'{'</code>, <code>'}'</code>, "
   "<code>'['</code> and <code>']'</code>, determine if the input string is valid.",
   "An input string is valid if: open brackets are closed by the same type of brackets, "
   "open brackets are closed in the correct order, and every close bracket has a "
   "corresponding open bracket of the same type.",
 ],
 "zh": [
   "給你一個只含 <code>'('</code>、<code>')'</code>、<code>'{'</code>、<code>'}'</code>、"
   "<code>'['</code>、<code>']'</code> 的字串 <code>s</code>，判斷它是否<strong>有效</strong>。",
   "有效的定義："
   "（1）左括號必須用<strong>相同類型</strong>的右括號關閉；"
   "（2）左括號必須以<strong>正確的順序</strong>關閉；"
   "（3）每個右括號都要有對應的左括號。",
 ],
 "pre": [
   ("note", "為什麼一定是堆疊？", [
     "括號匹配的結構是<strong>後進先出（LIFO）</strong>："
     "最後打開的括號，必須最先關閉。這正是堆疊的定義。",
     ("c", """"{[()]}"  合法    最內層的 () 先關，然後 []，最後 {}
"([)]"    不合法  ( 比 [ 早開，卻比 [ 晚關 —— 交錯了

如果不用堆疊，你必須同時追蹤「所有還沒關的括號以及它們的順序」
—— 那就是在手工實作一個堆疊。

反過來說，如果只有一種括號（例如只有小括號），
那用一個「計數器」就夠了（+1 開、-1 關、不能變負、結束時要是 0）。
是「多種括號」讓計數器失效、逼出堆疊。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "()"
  輸出：true

範例 2
  輸入：s = "()[]{}"
  輸出：true

範例 3
  輸入：s = "(]"
  輸出：false
  說明：類型對不上。

範例 4
  輸入：s = "([)]"
  輸出：false
  說明：順序不對（交錯了）。

範例 5
  輸入：s = "([])"
  輸出：true""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁴",
   "<code>s</code> 只由 <code>'()[]{}'</code> 這六個字元組成",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>只有六種字元</strong>，沒有其他雜訊。"
       "所以「不是右括號的就是左括號」這個判斷是安全的 —— 不用第三個分支。",
       "<strong>長度到 10⁴</strong>。O(n) 的堆疊解法輕鬆過；"
       "但 O(n²) 的「反覆 replace」解法（解法二）在最壞情況下會明顯變慢。",
       "<strong>長度至少 1</strong>，不過空字串在數學上是合法的（堆疊為空），"
       "我們的程式也自然會回 true —— 不用特判。",
       "<strong>奇數長度必定不合法</strong>。可以加一行 <code>if len(s) % 2: return False</code> 提前退出，"
       "但這只是常數優化。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P20_FIG, "0 0 640 254"),
 ],
 "approaches": [
   ap("解法一", "堆疊（唯一正解）", [
     ("c", S["p20_stack"]),
     ("h", "三個必須同時成立的條件"),
     ("c", """1. 遇到右括號時，堆疊不能是空的
       ")" 或 "]" 開頭 -> 沒有對應的左括號 -> False

2. 遇到右括號時，堆疊頂端必須是「同類型」的左括號
       "(]" -> pop 出 "("，但 "]" 需要的是 "[" -> False

3. 全部處理完之後，堆疊必須是空的
       "(()" -> 結束時堆疊還剩一個 "(" -> False

漏掉第 3 條是最常見的 bug：
"(((" 會一路 push 而不觸發任何檢查，
如果最後直接 return True 就錯了。"""),
     ("h", "為什麼用「右括號 → 左括號」的映射，而不是反過來？"),
     ("c", """PAIR = {")": "(", "]": "[", "}": "{"}

這樣寫的好處：判斷「這是不是右括號」只要 ch in PAIR，
一個字典同時當「分類器」和「對照表」用。

如果反過來寫 {"(": ")", ...}，
判斷右括號就要另外寫 ch in ")]}" 或 ch in PAIR.values()，
多一個資料結構，也多一個出錯的地方。

小細節，但它讓程式碼從 8 行變 6 行，而且更不容易錯。"""),
     "<strong><code>stack.pop() != PAIR[ch]</code> 這一行同時做了兩件事</strong>："
     "取出頂端、並且比對。因為 Python 的 <code>and</code> 短路求值，"
     "<code>not stack</code> 為真時就不會執行 <code>pop()</code>，所以不會 IndexError。"
     "<strong>順序不能顛倒</strong>。",
   ], "O(n)", "O(n)", "每個字元處理一次", "最壞情況（全是左括號）堆疊有 n 個元素", optimal=True),

   ap("解法二", "反覆消除（有趣但很慢）", [
     "另一種思路：合法的字串一定能靠「不斷消掉相鄰的一對」化簡成空字串。",
     ("c", S["p20_replace"]),
     ("c", """"{[()]}"
  -> replace("()", "")  ->  "{[]}"
  -> replace("[]", "")  ->  "{}"
  -> replace("{}", "")  ->  ""
  -> 空字串，合法 ✔

"([)]"
  -> 三種 replace 都找不到東西可消
  -> while 條件不成立，跳出
  -> s != ""，不合法 ✔"""),
     "<strong>正確，但複雜度是 O(n²)</strong>："
     "最壞情況（例如 <code>\"((((...))))\"</code>）每輪只能消掉最內層的一對，"
     "要跑 n/2 輪，每輪的 <code>replace</code> 又要掃過整個字串。"
     "n = 10⁴ 時大約 5 × 10⁷ 次字元操作 —— 能過，但比堆疊慢一兩個數量級。",
     "<strong>為什麼還要講它？</strong>"
     "因為它揭示了一件事：<strong>堆疊本質上就是在做同一件事，只是一趟做完。</strong>"
     "堆疊的 push/pop 就是「延後的消除」—— "
     "理解這個對應關係，之後看到單調堆疊、運算式求值這類題目會更有感覺。",
   ], "O(n²)", "O(n)", "最壞 n/2 輪 × 每輪 O(n)", "字串的複本"),
 ],
 "compare": (["解法", "時間", "空間", "n=10⁴ 能過？", "備註"],
   [["一、堆疊", "O(n)", "O(n)", "✔ 瞬間", "唯一該寫的答案"],
    ["二、反覆消除", "O(n²)", "O(n)", "✔ 但慢", "理解「堆疊 = 延後消除」的好例子"]]),
 "edges": [
   "<strong>右括號開頭</strong>：<code>\")\"</code>、<code>\"]\"</code> → false。堆疊是空的就 pop 會炸。",
   "<strong>左括號沒關</strong>：<code>\"(\"</code>、<code>\"(()\"</code> → false。忘記最後檢查堆疊為空的話會錯。",
   "<strong>類型錯配</strong>：<code>\"(]\"</code>、<code>\"{)\"</code> → false。",
   "<strong>順序交錯</strong>：<code>\"([)]\"</code> → false。這是堆疊存在的理由。",
   "<strong>正確巢狀</strong>：<code>\"([{}])\"</code>、<code>\"{[]}\"</code> → true。",
   "<strong>並列</strong>：<code>\"()[]{}\"</code> → true。每一對獨立開關。",
   "<strong>深層巢狀</strong>：<code>\"(((((((((())))))))))\"</code> → true。堆疊會長到 10 層。",
   "<strong>奇數長度</strong>：一定 false，可以提前退出。",
 ],
 "follow": [
   ("h", "追問一：如果還有其他字元（例如 <code>\"a(b)c\"</code>）呢？"),
   "把 <code>else: stack.append(ch)</code> 改成只在 <code>ch in \"([{\"</code> 時才 push，"
   "其他字元直接忽略。一行的差別，但如果不改，字母也會被推進堆疊，結果全錯。",
   ("h", "追問二：如果要回傳「最長的合法子字串長度」呢？"),
   "那是第 32 題（Longest Valid Parentheses），難度跳到 Hard。"
   "堆疊還是主角，但要改成<strong>存索引而不是存字元</strong>，"
   "而且要在堆疊底部放一個「上一個不合法位置」的哨兵。",
   ("h", "追問三：如果允許用 <code>'*'</code> 當萬用字元（可以是 <code>'('</code>、<code>')'</code> 或空）呢？"),
   "那是第 678 題（Valid Parenthesis String）。"
   "堆疊不夠用了，因為 <code>'*'</code> 有三種可能。"
   "標準解法是<strong>維護「可能的左括號數量」的區間 [lo, hi]</strong>："
   "遇到 <code>'('</code> 兩者都 +1，<code>')'</code> 都 −1，<code>'*'</code> 則 lo −1、hi +1。"
   "過程中 hi 不能變負，lo 要夾在 0 以上，結束時 lo 必須是 0。"
   "<strong>「用區間代替列舉所有可能」是一個很強大的技巧。</strong>",
   ("h", "追問四：這題和編譯器有什麼關係？"),
   "括號匹配是<strong>語法分析（parsing）的最小範例</strong>。"
   "「合法的括號序列」是一個典型的<strong>上下文無關語言</strong>，"
   "而它<strong>不是</strong>正規語言 —— 這就是為什麼你不能用正規表示式檢查括號配對"
   "（有限狀態機沒有記憶體記住巢狀深度，但堆疊有）。"
   "這個觀察是計算理論裡的經典結果（用 pumping lemma 可以證明）。",
 ],
 "related": [
   "<strong>第 22 題 Generate Parentheses</strong> —— 反過來，生成所有合法序列",
   "<strong>第 32 題 Longest Valid Parentheses</strong> —— Hard 版",
   "<strong>第 678 題 Valid Parenthesis String</strong> —— 加上萬用字元",
   "<strong>第 155 題 Min Stack</strong>、<strong>第 150 題 Evaluate RPN</strong> —— 堆疊的其他經典應用",
 ],
 "check": [
   "為什麼字典要寫成「右括號 → 左括號」而不是反過來？",
   "如果忘記最後的 <code>return not stack</code> 而直接 <code>return True</code>，哪一筆測資會錯？",
   "<code>if not stack or stack.pop() != PAIR[ch]</code> 的兩個條件能不能交換順序？為什麼？",
   "為什麼正規表示式無法檢查括號配對？這和堆疊有什麼關係？",
 ],
})
print("P20 written")
