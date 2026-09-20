# -*- coding: utf-8 -*-
"""第 141–145 題。"""
import random
from authoring import emit, ap
from runner import Src, ListNode, TreeNode, to_list, from_list

S = Src()
random.seed(141)


def _make_cycle(vals, pos):
    """建一條串列；pos >= 0 時把尾巴接回第 pos 個節點形成環。"""
    if not vals:
        return None
    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos >= 0:
        nodes[-1].next = nodes[pos]
    return nodes[0], nodes


# ==================== 141. Linked List Cycle ====================
S["p141_floyd"] = '''class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next            # 一次走一步
            fast = fast.next.next       # 一次走兩步
            if slow is fast:            # 追上了 -> 有環
                return True
        return False                    # fast 走到頭 -> 沒有環'''

S["p141_set"] = '''class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:            # 走過的節點又出現 -> 有環
                return True
            seen.add(head)
            head = head.next
        return False'''

S["p141_count"] = '''class Solution:
    # 【能過但不好】：走超過「節點數上限」就判定有環
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        limit = 10 ** 4 + 1             # 題目說節點數 <= 10^4
        steps = 0
        while head:
            steps += 1
            if steps > limit:
                return True
            head = head.next
        return False'''


def _p141_ref(head):
    seen = set()
    while head:
        if id(head) in seen:
            return True
        seen.add(id(head))
        head = head.next
    return False


_p141 = [S.load(k) for k in ("p141_floyd", "p141_set", "p141_count")]

for vals, pos, want in [
    ([3, 2, 0, -4], 1, True),
    ([1, 2], 0, True),
    ([1], -1, False),
    ([1], 0, True),
    ([1, 2, 3], -1, False),
]:
    h, _ = _make_cycle(vals, pos)
    assert _p141_ref(h) is want, ("P141 ref", vals, pos)
    for sol in _p141:
        h2, _ = _make_cycle(vals, pos)
        assert sol.hasCycle(h2) is want, ("P141", vals, pos, sol)
for sol in _p141:
    assert sol.hasCycle(None) is False, ("P141 empty", sol)

for _ in range(4000):
    n = random.randrange(1, 12)
    vals = [random.randint(-9, 9) for _ in range(n)]
    pos = random.choice([-1] + list(range(n)))
    h, _ = _make_cycle(vals, pos)
    want = pos >= 0
    for sol in _p141:
        h2, _ = _make_cycle(vals, pos)
        assert sol.hasCycle(h2) is want, ("P141 random", vals, pos, want, sol)
print("P141 solutions OK")

_P141_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">快慢指標（Floyd 判圈法）：一個一次走一步，一個一次走兩步。有環的話，快的一定會從後面追上慢的。</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="80" cy="90" r="20" fill="none" stroke="var(--text-muted)" stroke-width="2"/><text x="80" y="95" fill="var(--text-muted)">3</text>
              <circle cx="180" cy="90" r="20" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="180" y="95" fill="var(--gold)">2</text>
              <circle cx="290" cy="90" r="20" fill="none" stroke="var(--text-muted)" stroke-width="2"/><text x="290" y="95" fill="var(--text-muted)">0</text>
              <circle cx="290" cy="180" r="20" fill="none" stroke="var(--text-muted)" stroke-width="2"/><text x="290" y="185" fill="var(--text-muted)">-4</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="100" y1="90" x2="158" y2="90"/><polygon points="158,90 150,86 150,94" fill="var(--border)"/>
              <line x1="200" y1="90" x2="268" y2="90"/><polygon points="268,90 260,86 260,94" fill="var(--border)"/>
              <line x1="290" y1="110" x2="290" y2="158"/><polygon points="290,158 286,150 294,150" fill="var(--border)"/>
            </g>
            <path d="M 270 180 Q 180 180 180 112" fill="none" stroke="var(--gold)" stroke-width="2"/>
            <polygon points="180,112 176,120 184,120" fill="var(--gold)"/>
            <text x="180" y="146" fill="var(--gold)" font-size="11" text-anchor="middle">尾巴接回這裡</text>
            <line x1="380" y1="40" x2="380" y2="220" stroke="var(--border)"/>
            <text x="400" y="62" fill="var(--accent)" font-size="13" text-anchor="start">為什麼快的一定追得上？</text>
            <text x="400" y="92" fill="var(--text-muted)" font-size="12" text-anchor="start">兩個都進入環之後，</text>
            <text x="400" y="116" fill="var(--text-muted)" font-size="12" text-anchor="start">每走一輪，快的就「多走一步」——</text>
            <text x="400" y="140" fill="var(--gold)" font-size="12" text-anchor="start">兩者的距離每輪【減 1】。</text>
            <text x="400" y="170" fill="var(--text-muted)" font-size="12" text-anchor="start">距離是 0 到 L−1 之間的整數，</text>
            <text x="400" y="194" fill="var(--accent)" font-size="12" text-anchor="start">每輪減 1 → 一定會變成 0 ✔</text>
            <line x1="20" y1="240" x2="620" y2="240" stroke="var(--border)"/>
            <text x="20" y="268" fill="#ff8a65" font-size="12">★ 為什麼步差是 1 很重要？如果快的一次走 3 步，距離每輪減 2 ——</text>
            <text x="20" y="292" fill="var(--text-muted)" font-size="12">距離是奇數而環長是偶數時，就可能【永遠跳過】對方，繞不到相遇。</text>
            <text x="20" y="318" fill="var(--text-muted)" font-size="12">（實際上因為是在模 L 的環上，步差 k 時只要 gcd(k−1, L) 整除初始距離才會相遇。）</text>
            <text x="20" y="348" fill="var(--gold)" font-size="12">步差 1 是唯一「保證對任何環長都成立」的選擇 —— 這就是 Floyd 用 1 和 2 的原因。</text>
            <text x="20" y="378" fill="var(--accent)" font-size="12">★ 用 is 而不是 == 比較：我們要的是「同一個節點物件」，不是「值相同」。</text>
            <text x="20" y="402" fill="#ff8a65" font-size="12">值可能重複（範例裡就有兩個相同的值），用 == 會誤判。</text>'''

emit({
 "num": 141, "slug": "linked-list-cycle",
 "en": [
   "Given <code>head</code>, the head of a linked list, determine if the linked list has a cycle "
   "in it.",
   "There is a cycle in a linked list if there is some node in the list that can be reached "
   "again by continuously following the <code>next</code> pointer. Internally, <code>pos</code> "
   "is used to denote the index of the node that tail's <code>next</code> pointer is connected "
   "to. <strong>Note that <code>pos</code> is not passed as a parameter</strong>.",
   "Return <code>true</code> <em>if there is a cycle in the linked list</em>. Otherwise, return "
   "<code>false</code>.",
   "<strong>Follow up:</strong> Can you solve it using <code>O(1)</code> (i.e. constant) memory?",
 ],
 "zh": [
   "給你一條鏈結串列的頭節點 <code>head</code>，判斷它裡面<strong>有沒有環</strong>。",
   "「有環」的意思是：<strong>一直沿著 <code>next</code> 走，會回到某個走過的節點</strong>。",
   "<strong>注意 <code>pos</code>（環的接入點）不會當成參數傳給你</strong> —— 它只是用來描述測資。",
   "<strong>進階：</strong>你能用 <code>O(1)</code> 空間解決嗎？",
 ],
 "pre": [
   ("note", "★ 為什麼「有環」這麼麻煩", [
     ("c", """沒有環的串列，走到底會碰到 None -> 天然的終止條件。

    有環的話，while head: 會【永遠跑不完】。

    所以任何對「可能有環」的串列做的操作，
    都必須自己想辦法終止。

【三條路】：

    (a) 記住走過的節點（雜湊集合）-> O(n) 空間
    (b) 數步數，超過上限就判定有環 -> 依賴題目的上限，很醜
    (c) 快慢指標（Floyd）-> O(1) 空間 ✔

    進階要求 O(1) 空間，所以答案是 (c)。

【Floyd 判圈法（龜兔賽跑）】：

    slow 一次走一步，fast 一次走兩步。

    沒有環 -> fast 會先走到 None
    有環   -> fast 一定會從後面追上 slow

    這個演算法優雅到它有自己的名字，
    而且是所有「環偵測」問題的標準答案。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [3,2,0,-4], pos = 1

        3 -> 2 -> 0 -> -4
             ^           |
             +-----------+

  輸出：true
  說明：尾巴接回索引 1（值為 2 的節點）。

範例 2
  輸入：head = [1,2], pos = 0
  輸出：true

範例 3
  輸入：head = [1], pos = -1
  輸出：false
  說明：pos = -1 代表沒有環。""",
 "constraints": [
   "串列的節點數在 <code>[0, 10⁴]</code> 之間",
   "−10⁵ ≤ <code>Node.val</code> ≤ 10⁵",
   "<code>pos</code> 是 <code>-1</code> 或串列中的一個<strong>有效索引</strong>",
 ],
 "idea": [
   ("fig", _P141_FIG, "0 0 640 420"),
   ("c", """【Floyd 判圈法】

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

【★ 為什麼 fast 一定追得上 slow？】

    假設 slow 進入環的時候，fast 已經在環裡，
    兩者在環上的距離是 d（fast 落後 slow d 步，0 <= d < L）。

    每走一輪：
        slow 前進 1 步
        fast 前進 2 步
        -> 兩者的距離【減 1】

    距離是 0 到 L-1 之間的整數，每輪減 1
    -> 最多 L 輪之後一定變成 0 -> 相遇 ✔

【★ 為什麼「步差必須是 1」？】

    如果 fast 一次走 3 步，距離每輪減 2。

    距離是奇數、而每次減 2 -> 可能永遠跳過 0
    （在模 L 的意義下，要 gcd(2, L) 整除 d 才會相遇）。

    步差 1 時 gcd(1, L) = 1，整除任何數 ✔
    -> 【保證對任何環長、任何初始距離都會相遇】

    這就是為什麼標準寫法是「1 步 vs 2 步」。

【★ 迴圈條件 while fast and fast.next】

    兩個都要檢查：
        fast 是 None      -> 已經走到尾巴（沒有環）
        fast.next 是 None -> 再走一步就出界

    少檢查一個就會 AttributeError。

    奇數個節點時是 fast 變 None，
    偶數個節點時是 fast.next 變 None ——
    兩種情況都要擋。

【複雜度】

    時間 O(n)：
        沒有環 -> fast 走 n/2 步就到尾
        有環   -> slow 最多走 n 步（進環最多 n 步，環裡最多 L 步）

    空間 O(1) ✔"""),
 ],
 "approaches": [
   ap("解法一", "Floyd 快慢指標（標準答案）", [
     ("c", S["p141_floyd"]),
     "<strong>六行，O(n) 時間、O(1) 空間。</strong>"
     "<strong>這是進階要求的答案。</strong>",
     ("h", "★ 用 <code>is</code> 而不是 <code>==</code>"),
     ("c", """if slow is fast:        ✔ 同一個【物件】
if slow == fast:        ✘ 值相同就算（如果有定義 __eq__）

    對 LeetCode 的 ListNode 來說，
    沒有定義 __eq__，所以 == 會退化成 is ——
    兩者碰巧等價。

    但【不要依賴這個】：
        ✘ 語意不清楚
        ✘ 如果節點類別定義了 __eq__（例如比較 val），就會誤判

    範例 1 的串列裡沒有重複值，
    但題目沒有保證值互不相同。

【一般原則】：
    比較「是不是同一個物件」-> is
    比較「值相不相等」       -> ==

    比較 None 也一律用 is（PEP 8 的建議）。""",),
     ("h", "為什麼 <code>slow</code> 和 <code>fast</code> 都從 <code>head</code> 開始？"),
     ("c", """也可以寫成 slow = head; fast = head.next（錯開一步）。

    那樣的話迴圈條件和判斷位置都要跟著調整，
    而且要特判 head 是 None。

    【從同一點出發的版本】：
        ✔ 不用特判空串列（while 條件就擋掉了）
        ✔ 迴圈裡「先走再比」，邏輯清楚
        ✔ 而且這個版本能直接延伸到第 142 題（找環的入口）

    所以標準寫法是兩個都從 head 開始。""",),
   ], "O(n)", "O(1)", "slow 最多走 n 步", "兩個指標", optimal=True),

   ap("解法二", "雜湊集合（最直白，但不滿足進階）", [
     ("c", S["p141_set"]),
     "<strong>五行。O(n) 時間、O(n) 空間。</strong>",
     ("c", """【把「節點物件」放進 set】

    Python 的物件預設可雜湊（用 id），
    所以可以直接 seen.add(head) ✔

    在 Java 裡也一樣（HashSet<ListNode> 用預設的 identity hash）。

    【不要放 head.val】——
    值可能重複，會誤判成有環。

【面試時的說法】：

    「用集合記錄走過的節點，O(n) 時間、O(n) 空間。
      如果要 O(1) 空間，我會用快慢指標。」

    然後寫解法一。

    先給一個正確解、再優化，永遠是對的節奏。""",),
   ], "O(n)", "O(n)", "每個節點一次", "雜湊集合"),

   ap("解法三", "數步數（能過，但不該寫）", [
     ("c", S["p141_count"]),
     ("c", """「走超過 10^4 步還沒到底 -> 一定繞回來了」。

    能通過 LeetCode，但這是【投機】而不是解法：

    ✘ 完全依賴題目給的節點數上限
    ✘ 上限一改就壞
    ✘ 在真實程式裡，你根本不知道串列有多長
    ✘ 面試官會覺得你在鑽漏洞

【放在這裡是為了指出它的問題】：

    「利用測資的限制」和「解決問題」是兩件事。

    有時候前者能過關，
    但它不會讓你學到任何東西，
    也不會在面試裡得分。

【什麼時候「用限制」是合理的？】

    當限制是【問題本身的一部分】時，
    例如「數值範圍 0..9 所以可以用計數排序」——
    那是在利用問題結構。

    而「節點數 <= 10^4 所以走 10^4 步」
    利用的是「測資規模」，不是問題結構。

    這個區別值得記住。""",),
   ], "O(n)", "O(1)", "依賴節點數上限", "一個計數器"),
 ],
 "compare": (["解法", "時間", "空間", "滿足進階", "備註"],
   [["一、Floyd 快慢指標", "O(n)", "O(1)", "✔", "標準答案"],
    ["二、雜湊集合", "O(n)", "O(n)", "✘", "最直白"],
    ["三、數步數", "O(n)", "O(1)", "△", "投機，不該寫"]]),
 "edges": [
   "<strong>空串列</strong> → <code>False</code>。"
   "<strong><code>while fast and fast.next</code> 天然擋掉，不用特判 ✔</strong>",
   "<strong>單一節點、沒有環</strong> → <code>False</code>。",
   "<strong>單一節點、自己指向自己</strong> <code>pos = 0</code> → <code>True</code>。",
   "<strong>兩個節點互指</strong> → <code>True</code>。",
   "<strong>環就是整條串列</strong>（尾接頭）→ <code>True</code>。",
   "<strong>迴圈條件只寫 <code>while fast</code></strong> → "
   "<strong><code>fast.next.next</code> 會 <code>AttributeError</code>。</strong>",
   "<strong>用 <code>==</code> 而不是 <code>is</code></strong> → "
   "節點類別若定義了 <code>__eq__</code> 就會誤判。",
   "<strong>值有重複</strong> → 用值判斷的話會誤判成有環。",
 ],
 "follow": [
   ("h", "追問一：如果要找出「環的入口」呢？"),
   "<strong>第 142 題</strong>。相遇之後，"
   "<strong>把一個指標移回 <code>head</code>，然後兩個都一次走一步 —— "
   "它們會在環的入口相遇。</strong>",
   "<strong>這個結論非常不直觀，但有漂亮的證明</strong>（見第 142 題）。",
   ("h", "追問二：如果要算出「環有多長」呢？"),
   ("c", """相遇之後，讓其中一個指標繞環走一圈：

    count = 1
    p = slow.next
    while p is not slow:
        count += 1
        p = p.next

    count 就是環長 ✔

【因為相遇點一定在環上】——
    從它出發繞回自己，走過的步數就是環長。

    O(L) 時間、O(1) 空間。""",),
   ("h", "追問三：Floyd 判圈法還能用在哪裡？"),
   ("ul", [
     "<strong>第 142 題</strong>：找環的入口",
     "<strong>第 287 題 尋找重複數</strong>：把陣列當成函數 <code>i -> nums[i]</code>，"
     "重複的數就是環的入口 —— <strong>非常漂亮的轉換</strong>",
     "<strong>第 202 題 快樂數</strong>：判斷數字變換會不會進入循環",
     "<strong>偽隨機數產生器的週期偵測</strong>",
     "<strong>Pollard's rho 質因數分解</strong>：用 Floyd 找模 n 下的循環",
   ]),
   "<strong>共同結構：有一個「函數 f」和一個起點，反覆套用 f 會走出一條路徑。"
   "如果狀態空間有限，路徑必然進入循環（鴿籠原理）—— Floyd 就是用 O(1) 空間找出那個循環。</strong>",
   ("h", "追問四：有沒有比 Floyd 更好的判圈法？"),
   ("c", """【Brent 演算法】（又叫「指數搜尋」判圈法）：

    固定 slow，讓 fast 走 1, 2, 4, 8, ... 步，
    每一輪結束就把 slow 移到 fast 的位置。

    優點：
        ✔ 平均比 Floyd 快約 25%（實測）
        ✔ 直接得到環長（不用再繞一圈）

    缺點：
        ✘ 比較難記
        ✘ 找「環的入口」要多一步

【實務上（例如 Pollard's rho）常用 Brent】，
    但面試講 Floyd 就好 —— 它更廣為人知，
    而且第 142 題的入口定理只在 Floyd 的架構下成立。""",),
 ],
 "related": [
   "<strong>第 142 題 Linked List Cycle II</strong> —— 找環的入口",
   "<strong>第 287 題 Find the Duplicate Number</strong> —— 陣列版的 Floyd",
   "<strong>第 202 題 Happy Number</strong> —— 數字版的判圈",
   "<strong>第 876 題 Middle of the Linked List</strong> —— 快慢指標的另一個用途",
 ],
 "check": [
   "為什麼 <code>fast</code> 一定會追上 <code>slow</code>？請說出那個「距離每輪減 1」的論證。",
   "為什麼步差一定要是 1（也就是 1 步 vs 2 步）？走 3 步會有什麼問題？",
   "迴圈條件為什麼要寫 <code>while fast and fast.next</code>？少一個會怎樣？",
   "為什麼要用 <code>is</code> 而不是 <code>==</code>？",
 ],
})
print("P141 written")

# ==================== 142. Linked List Cycle II ====================
S["p142_floyd"] = '''class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # 第一階段：找相遇點
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                # 第二階段：一個指標回到 head，兩個都一次走一步
                p = head
                while p is not slow:
                    p = p.next
                    slow = slow.next
                return p                # 相遇的地方就是環的入口

        return None                     # 沒有環'''

S["p142_set"] = '''class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        while head:
            if head in seen:
                return head             # 第一個重複出現的節點就是入口
            seen.add(head)
            head = head.next
        return None'''


def _p142_ref(head):
    seen = {}
    while head:
        if id(head) in seen:
            return seen[id(head)]
        seen[id(head)] = head
        head = head.next
    return None


_p142 = [S.load(k) for k in ("p142_floyd", "p142_set")]

for vals, pos in [
    ([3, 2, 0, -4], 1), ([1, 2], 0), ([1], -1), ([1], 0), ([1, 2, 3], -1),
    ([1, 2, 3, 4, 5], 4), ([1, 2, 3, 4, 5], 0),
]:
    h, nodes = _make_cycle(vals, pos)
    want = nodes[pos] if pos >= 0 else None
    assert _p142_ref(h) is want, ("P142 ref", vals, pos)
    for sol in _p142:
        h2, nodes2 = _make_cycle(vals, pos)
        got = sol.detectCycle(h2)
        exp = nodes2[pos] if pos >= 0 else None
        assert got is exp, ("P142", vals, pos, sol)
for sol in _p142:
    assert sol.detectCycle(None) is None

for _ in range(4000):
    n = random.randrange(1, 13)
    vals = [random.randint(-9, 9) for _ in range(n)]
    pos = random.choice([-1] + list(range(n)))
    for sol in _p142:
        h, nodes = _make_cycle(vals, pos)
        got = sol.detectCycle(h)
        exp = nodes[pos] if pos >= 0 else None
        assert got is exp, ("P142 random", vals, pos, sol)
print("P142 solutions OK")

_P142_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 兩階段：先用快慢指標找相遇點，再把一個指標移回 head，兩個都走一步 —— 會在入口相遇。</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="70" cy="96" r="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="70" y="101" fill="var(--accent)">H</text>
              <circle cx="150" cy="96" r="17" fill="none" stroke="var(--text-muted)"/><text x="150" y="101" fill="var(--text-muted)"> </text>
              <circle cx="230" cy="96" r="17" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="230" y="101" fill="var(--gold)">E</text>
              <circle cx="330" cy="60" r="17" fill="none" stroke="var(--text-muted)"/>
              <circle cx="410" cy="96" r="17" fill="none" stroke="#ff8a65" stroke-width="3"/><text x="410" y="101" fill="#ff8a65">M</text>
              <circle cx="330" cy="140" r="17" fill="none" stroke="var(--text-muted)"/>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="87" y1="96" x2="130" y2="96"/><polygon points="130,96 122,92 122,100" fill="var(--border)"/>
              <line x1="167" y1="96" x2="210" y2="96"/><polygon points="210,96 202,92 202,100" fill="var(--border)"/>
              <line x1="243" y1="87" x2="314" y2="66"/><polygon points="314,66 306,64 308,72" fill="var(--border)"/>
              <line x1="346" y1="66" x2="396" y2="88"/><polygon points="396,88 388,84 386,92" fill="var(--border)"/>
              <line x1="398" y1="108" x2="348" y2="132"/><polygon points="348,132 356,132 354,124" fill="var(--border)"/>
              <line x1="314" y1="134" x2="245" y2="108"/><polygon points="245,108 253,108 251,116" fill="var(--border)"/>
            </g>
            <text x="150" y="132" fill="var(--accent)" font-size="11" text-anchor="middle">a 步</text>
            <text x="70" y="128" fill="var(--accent)" font-size="11" text-anchor="middle">起點</text>
            <text x="230" y="134" fill="var(--gold)" font-size="11" text-anchor="middle">環的入口 E</text>
            <text x="450" y="101" fill="#ff8a65" font-size="11" text-anchor="start">相遇點 M</text>
            <text x="330" y="40" fill="var(--text-muted)" font-size="11" text-anchor="middle">b 步</text>
            <text x="330" y="176" fill="var(--text-muted)" font-size="11" text-anchor="middle">c 步（M 走回 E）</text>
            <line x1="20" y1="198" x2="620" y2="198" stroke="var(--border)"/>
            <text x="20" y="226" fill="var(--accent)" font-size="13">推導（設環長 L = b + c）：</text>
            <text x="40" y="254" fill="var(--text-muted)" font-size="12">slow 走的距離 = a + b</text>
            <text x="40" y="278" fill="var(--text-muted)" font-size="12">fast 走的距離 = a + b + k·L　（k 是 fast 多繞的圈數，k ≥ 1）</text>
            <text x="40" y="306" fill="var(--gold)" font-size="12">而 fast 的距離是 slow 的兩倍：　2(a + b) = a + b + k·L</text>
            <text x="40" y="332" fill="var(--gold)" font-size="12">　　　　　　　　　　　　　　　　a + b = k·L</text>
            <text x="40" y="358" fill="var(--gold)" font-size="12">　　　　　　　　　　　　　　　　a = k·L − b = (k−1)·L + (L − b) = (k−1)·L + c</text>
            <line x1="20" y1="380" x2="620" y2="380" stroke="var(--border)"/>
            <text x="20" y="408" fill="#ff8a65" font-size="13">a = (k−1)·L + c　的意思是：</text>
            <text x="20" y="436" fill="var(--text-muted)" font-size="12">「從 head 走 a 步到入口」和「從相遇點 M 走 c 步（再繞 k−1 圈）到入口」——</text>
            <text x="20" y="460" fill="var(--accent)" font-size="12">兩者走的步數【模 L 之後完全相同】。所以兩個指標同時一步一步走，一定在入口 E 相遇 ✔</text>'''

emit({
 "num": 142, "slug": "linked-list-cycle-ii",
 "en": [
   "Given the <code>head</code> of a linked list, return <em>the node where the cycle begins. If "
   "there is no cycle, return </em><code>null</code>.",
   "There is a cycle in a linked list if there is some node in the list that can be reached "
   "again by continuously following the <code>next</code> pointer. Internally, <code>pos</code> "
   "is used to denote the index of the node that tail's <code>next</code> pointer is connected "
   "to (<strong>0-indexed</strong>). It is <code>-1</code> if there is no cycle. "
   "<strong>Note that <code>pos</code> is not passed as a parameter.</strong>",
   "<strong>Do not modify</strong> the linked list.",
   "<strong>Follow up:</strong> Can you solve it using <code>O(1)</code> (i.e. constant) memory?",
 ],
 "zh": [
   "給你一條鏈結串列的頭節點 <code>head</code>，"
   "回傳<strong>環的入口節點</strong>；如果沒有環，回傳 <code>None</code>。",
   "<strong>不能修改這條串列。</strong>",
   "<strong>進階：</strong>你能用 <code>O(1)</code> 空間解決嗎？",
 ],
 "pre": [
   ("note", "★ 第 141 題只問「有沒有」，這題問「在哪裡」", [
     ("c", """用雜湊集合的話，這題和第 141 題一樣簡單 ——
第一個「重複出現」的節點就是入口 ✔

    但那是 O(n) 空間。

【O(1) 空間的做法非常不直觀】：

    1. 用快慢指標找到【相遇點 M】
    2. 把一個指標移回 head
    3. 兩個指標【都一次走一步】
    4. 它們會在【環的入口】相遇

    第 4 步為什麼成立？

    這需要一個推導，而那個推導是本題的全部內容。
    下面會完整證明一次。

【這是少數「結論漂亮但完全看不出來」的演算法】——
    第一次看到一定會覺得「這怎麼可能」。
    但推導只有五行，而且很值得親手算一遍。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [3,2,0,-4], pos = 1
  輸出：索引 1 的節點（值為 2）

範例 2
  輸入：head = [1,2], pos = 0
  輸出：索引 0 的節點（值為 1）

範例 3
  輸入：head = [1], pos = -1
  輸出：null""",
 "constraints": [
   "串列的節點數在 <code>[0, 10⁴]</code> 之間",
   "−10⁵ ≤ <code>Node.val</code> ≤ 10⁵",
   "<code>pos</code> 是 <code>-1</code> 或串列中的一個<strong>有效索引</strong>",
 ],
 "idea": [
   ("fig", _P142_FIG, "0 0 640 478"),
   ("c", """【符號約定】

    a = 從 head 到【環的入口 E】的距離
    L = 環的長度
    b = 從 E 到【相遇點 M】的距離（沿著環的方向）
    c = 從 M 回到 E 的距離        （所以 b + c = L）

【第一階段：找相遇點】

    slow 和 fast 從 head 出發，1 步 vs 2 步。

    相遇時：
        slow 走了 a + b 步
        fast 走了 a + b + k·L 步    （k >= 1，fast 多繞了 k 圈）

    因為 fast 的速度是兩倍：
        fast 走的 = 2 × slow 走的

        a + b + k·L = 2(a + b)
        k·L = a + b
        a = k·L - b

    而 L = b + c，所以：
        a = k·L - b
          = (k-1)·L + L - b
          = (k-1)·L + c           ★★★

【★★ 這個式子的意思】

    a = (k-1)·L + c

    左邊：「從 head 走到入口 E」要 a 步
    右邊：「從相遇點 M 走 c 步到 E，再繞 k-1 圈」也是 a 步

    所以：
        一個指標從 head 出發
        另一個指標從 M 出發
        兩個【都一次走一步】

        走了 a 步之後：
            第一個到達 E ✔
            第二個走了 (k-1)·L + c 步，也就是「繞 k-1 圈再走 c 步」
                                     -> 也到達 E ✔

    【它們在 E 相遇。】

【★ 為什麼是「第一次」相遇就在 E？】

    在 E 之前，第一個指標還沒進環，
    而第二個指標一直在環上 ——
    兩者不可能在環外相遇。

    所以第一次相遇必然在 E（或更後面），
    而我們證明了 a 步時兩者都在 E ->
    第一次相遇就是 E ✔"""),
 ],
 "approaches": [
   ap("解法一", "Floyd 兩階段（標準答案）", [
     ("c", S["p142_floyd"]),
     "<strong>十二行，O(n) 時間、O(1) 空間。</strong>"
     "<strong>這是進階要求的答案。</strong>",
     ("h", "為什麼第二階段的 <code>while</code> 條件是 <code>p is not slow</code>？"),
     ("c", """兩個指標同步往前走，直到指到同一個節點。

    while p is not slow:
        p = p.next
        slow = slow.next
    return p

【如果 a = 0 呢？】（入口就是 head）

    那 p 和 slow 一開始就相等嗎？

    不一定 —— slow 目前在相遇點 M，而 p 在 head = E。
    如果 M 剛好也是 E，那迴圈一次都不跑，直接回 head ✔
    如果 M 不是 E，就走 a = 0... 

    等等，a = 0 時公式說 (k-1)·L + c = 0，
    也就是 k = 1 且 c = 0 -> M 就是 E ✔

    所以 a = 0 時 M 一定等於 E，迴圈不跑，直接回傳 ✔
    完全不用特判。

【驗證一下最小的例子】：

    單一節點自己指自己（a=0, L=1）：
        slow=fast=head
        一輪後：slow=head, fast=head -> 相遇，M = head
        第二階段：p = head，p is slow -> 直接回 head ✔""",),
     ("h", "為什麼可以在 <code>while</code> 裡面 <code>return</code>？"),
     "因為<strong>相遇只會發生一次</strong>（發生了就立刻處理完回傳）。",
     "<strong>如果 <code>fast</code> 走到 <code>None</code>，代表沒有環，迴圈自然結束，回傳 <code>None</code> ✔</strong>",
     ("h", "「不能修改串列」這個要求"),
     "<strong>Floyd 完全不碰任何指標，只是讀取</strong> ✔",
     "<strong>有些「破壞性」的做法（例如邊走邊把 <code>next</code> 設成 <code>None</code>）"
     "也能偵測環，但題目明確禁止。</strong>",
   ], "O(n)", "O(1)", "兩階段各 O(n)", "兩個指標", optimal=True),

   ap("解法二", "雜湊集合（最直白）", [
     ("c", S["p142_set"]),
     "<strong>五行，O(n) 時間、O(n) 空間。</strong>",
     ("c", """第一個「已經在 seen 裡」的節點就是入口 ——
因為我們是照順序走的，
第一次「回到走過的節點」必然是繞完一圈回到入口 ✔

【為什麼這個解法這麼簡單，Floyd 卻那麼難？】

    因為雜湊集合用 O(n) 空間「記住了整段歷史」。

    Floyd 只有兩個指標，沒有記憶 ——
    它必須靠【數學關係】推出入口的位置。

    【空間換簡單度】是非常常見的取捨。

【面試時的節奏】：

    1. 先寫這個（三十秒，一定對）
    2. 說「這是 O(n) 空間，我可以做到 O(1)」
    3. 寫 Floyd，並【推導一次那個等式】

    第 3 步的推導才是這題真正在考的東西。""",),
   ], "O(n)", "O(n)", "每個節點一次", "雜湊集合"),
 ],
 "compare": (["解法", "時間", "空間", "滿足進階", "好推導嗎"],
   [["一、Floyd 兩階段", "O(n)", "O(1)", "✔", "★☆☆ 要會證"],
    ["二、雜湊集合", "O(n)", "O(n)", "✘", "★★★"]]),
 "edges": [
   "<strong>空串列</strong> → <code>None</code>。",
   "<strong>沒有環</strong> → <code>None</code>。<code>fast</code> 走到底，迴圈結束。",
   "<strong>單一節點自己指自己</strong>（<code>a = 0, L = 1</code>）→ 回傳 <code>head</code>。"
   "<strong>第二階段的迴圈一次都不跑，完全不用特判 ✔</strong>",
   "<strong>入口就是 <code>head</code></strong>（<code>a = 0</code>）→ "
   "<strong>公式保證此時相遇點就是 <code>head</code>，直接回傳。</strong>",
   "<strong>環就是整條串列</strong>（尾接頭）→ 入口是 <code>head</code>。",
   "<strong>環在最後一個節點</strong>（<code>pos = n-1</code>）→ 入口是最後一個節點。",
   "<strong>第二階段忘了「兩個都走一步」</strong>（只動一個）→ 答案錯。",
   "<strong>第二階段用 <code>fast</code> 而不是 <code>slow</code></strong> → "
   "<strong><code>fast</code> 和 <code>slow</code> 相遇時在同一個位置，所以其實一樣對 ✔</strong>",
 ],
 "follow": [
   ("h", "追問一：這個「a = (k−1)·L + c」的推導能不能講得更直觀？"),
   ("c", """換一個說法：

    相遇時 slow 走了 a + b 步，fast 走了 2(a + b) 步。

    兩者的差是 (a + b) 步，
    而這個差【必然是環長的整數倍】（因為 fast 就是多繞了幾圈）：

        a + b = k·L

    現在想像：讓 slow 【再走 a 步】。

        它會走到 a + b + a = 2a + b 的位置...

    不夠直觀。換成從 M 出發的說法：

        從 M 再走 c 步就到 E（定義）。
        從 M 再走 c + L 步也到 E（多繞一圈）。
        從 M 再走 c + 2L 步也到 E。
        ...

        也就是「從 M 走 c + mL 步」都會到 E。

    而 a = (k-1)L + c 正是這種形式（m = k-1）✔

    【所以「從 head 走 a 步」和「從 M 走 a 步」
      都會到達 E。】

【一句話版本】：
    「a 和 c 在模 L 的意義下相等，
      所以從 head 和從 M 同步走，會在入口相遇。」""",),
   ("h", "追問二：這個技巧在陣列上的應用？"),
   "<strong>第 287 題（尋找重複數）</strong> —— 這是 Floyd 最漂亮的應用之一。",
   ("c", """給一個長度 n+1 的陣列，元素都在 1..n，
保證恰好有一個重複的數字。要求 O(1) 空間、不修改陣列。

【轉換】：把陣列看成一個函數
    f(i) = nums[i]

    從 index 0 出發，反覆套用 f，會走出一條路徑：
        0 -> nums[0] -> nums[nums[0]] -> ...

    因為值域是 1..n 而定義域是 0..n（多一個），
    根據鴿籠原理，這條路徑【一定會進入循環】。

    而【重複的那個數字就是環的入口】！

        因為「兩個不同的 i 指向同一個值」
        = 「兩條路徑匯入同一個節點」
        = 「那個節點是環的入口」

    所以直接套用第 142 題的兩階段 Floyd ✔

【這個轉換非常漂亮】——
    它把「陣列裡找重複」變成「串列裡找環的入口」。

    看到「O(1) 空間 + 不能修改 + 值域受限」，
    就該想到這一招。""",),
   ("h", "追問三：如果要同時回傳「入口」和「環長」呢？"),
   "<strong>找到入口 <code>E</code> 之後，從 <code>E</code> 繞一圈數回來</strong>：",
   ("c", """count = 1
p = E.next
while p is not E:
    count += 1
    p = p.next

或者在第一階段結束時（相遇點 M）就數：
    因為 M 也在環上，從 M 繞回 M 就是環長。

兩種都是 O(L)，總複雜度不變 ✔""",),
   ("h", "追問四：為什麼「不能修改串列」這個限制存在？"),
   "<strong>因為有一個很簡單的破壞性解法</strong>："
   "<strong>邊走邊把每個節點的 <code>next</code> 指向自己（或某個哨兵）—— "
   "下一次走到「已經指向自己」的節點就是入口。</strong>",
   "<strong>O(1) 空間、O(n) 時間，而且很好想。</strong>",
   "<strong>題目禁止它，是為了逼出 Floyd 那個有數學內容的解法。</strong>"
   "<strong>（而且在真實程式裡，破壞輸入資料通常是不可接受的。）</strong>",
 ],
 "related": [
   "<strong>第 141 題 Linked List Cycle</strong> —— 只問有沒有環，先學那題",
   "<strong>第 287 題 Find the Duplicate Number</strong> —— 陣列版，Floyd 最漂亮的應用",
   "<strong>第 202 題 Happy Number</strong> —— 數字版的判圈",
   "<strong>第 160 題 Intersection of Two Linked Lists</strong> —— 另一個「兩個指標同步走」的技巧",
 ],
 "check": [
   "請推導一次 <code>a = (k−1)·L + c</code>。每個符號代表什麼？",
   "為什麼第二階段要「兩個指標都一次走一步」？",
   "<code>a = 0</code>（入口就是 head）時，為什麼不用特判？",
   "第 287 題怎麼把「陣列找重複」轉成「串列找環入口」？",
 ],
})
print("P142 written")

# ==================== 143. Reorder List ====================
S["p143"] = '''class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 第一步：快慢指標找中點（slow 會停在「前半的最後一個」）
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 第二步：把後半段反轉，並從中間切斷
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # prev 現在是反轉後的後半段的頭

        # 第三步：兩條交錯合併
        first, second = head, prev
        while second:
            f_next, s_next = first.next, second.next
            first.next = second
            second.next = f_next
            first, second = f_next, s_next'''

S["p143_array"] = '''class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # 把節點倒進陣列，就能 O(1) 隨機存取
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i == j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None'''

S["p143_stack"] = '''class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        # 用堆疊拿到「從後往前」的節點
        stack = []
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        n = len(stack)
        cur = head
        for _ in range(n // 2):
            tail = stack.pop()
            nxt = cur.next
            cur.next = tail
            tail.next = nxt
            cur = nxt

        cur.next = None'''


def _p143_ref(vals):
    """獨立參考解：直接算出重排後的值序列。"""
    out = []
    i, j = 0, len(vals) - 1
    while i < j:
        out.append(vals[i]); i += 1
        out.append(vals[j]); j -= 1
    if i == j:
        out.append(vals[i])
    return out


_p143 = [S.load(k) for k in ("p143", "p143_array", "p143_stack")]

for vals in [[1, 2, 3, 4], [1, 2, 3, 4, 5], [1], [1, 2], [1, 2, 3], []]:
    want = _p143_ref(vals)
    for sol in _p143:
        h = to_list(vals)
        sol.reorderList(h)
        assert from_list(h) == want, ("P143", vals, want, from_list(h), sol)

for _ in range(4000):
    n = random.randrange(0, 15)
    vals = [random.randint(-20, 20) for _ in range(n)]
    want = _p143_ref(vals)
    for sol in _p143:
        h = to_list(vals)
        sol.reorderList(h)
        assert from_list(h) == want, ("P143 random", vals, want, sol)
print("P143 solutions OK")

_P143_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">三個基本功的組合：找中點 → 反轉後半 → 交錯合併。每一步都是一道獨立的經典題。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">① 找中點並切斷</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="60" cy="90" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="60" y="95" fill="var(--accent)">1</text>
              <circle cx="130" cy="90" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="130" y="95" fill="var(--accent)">2</text>
              <circle cx="200" cy="90" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="200" y="95" fill="var(--accent)">3</text>
              <circle cx="300" cy="90" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="300" y="95" fill="#ff8a65">4</text>
              <circle cx="370" cy="90" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="370" y="95" fill="#ff8a65">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="76" y1="90" x2="112" y2="90"/><line x1="146" y1="90" x2="182" y2="90"/>
              <line x1="316" y1="90" x2="352" y2="90"/>
            </g>
            <line x1="240" y1="70" x2="260" y2="110" stroke="var(--gold)" stroke-width="2"/>
            <text x="250" y="130" fill="var(--gold)" font-size="11" text-anchor="middle">切</text>
            <text x="430" y="95" fill="var(--text-muted)" font-size="11" text-anchor="start">前半 [1,2,3]　後半 [4,5]</text>
            <text x="20" y="162" fill="var(--gold)" font-size="13">② 反轉後半</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="300" cy="196" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="300" y="201" fill="#ff8a65">5</text>
              <circle cx="370" cy="196" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="370" y="201" fill="#ff8a65">4</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5"><line x1="316" y1="196" x2="352" y2="196"/></g>
            <text x="430" y="201" fill="var(--text-muted)" font-size="11" text-anchor="start">後半變成 [5,4]</text>
            <text x="20" y="252" fill="var(--gold)" font-size="13">③ 交錯合併</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="60" cy="292" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="60" y="297" fill="var(--accent)">1</text>
              <circle cx="130" cy="292" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="130" y="297" fill="#ff8a65">5</text>
              <circle cx="200" cy="292" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="200" y="297" fill="var(--accent)">2</text>
              <circle cx="270" cy="292" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="270" y="297" fill="#ff8a65">4</text>
              <circle cx="340" cy="292" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="340" y="297" fill="var(--accent)">3</text>
            </g>
            <g stroke="var(--gold)" stroke-width="1.5">
              <line x1="76" y1="292" x2="112" y2="292"/><line x1="146" y1="292" x2="182" y2="292"/>
              <line x1="216" y1="292" x2="252" y2="292"/><line x1="286" y1="292" x2="322" y2="292"/>
            </g>
            <text x="420" y="297" fill="var(--gold)" font-size="11" text-anchor="start">完成：1 → 5 → 2 → 4 → 3</text>
            <line x1="20" y1="326" x2="620" y2="326" stroke="var(--border)"/>
            <text x="20" y="354" fill="#ff8a65" font-size="12">★ 為什麼 slow 要從 head 出發、fast 從 head.next 出發（錯開一步）？</text>
            <text x="20" y="380" fill="var(--text-muted)" font-size="12">這樣偶數長度時 slow 會停在【前半的最後一個】，切出來的前半剛好不短於後半。</text>
            <text x="20" y="404" fill="var(--text-muted)" font-size="12">n=4：slow 停在 2 → 前半 [1,2]、後半 [3,4] ✔　（都從 head 出發的話 slow 會停在 3，切錯邊）</text>
            <text x="20" y="434" fill="var(--accent)" font-size="12">★ 一定要 slow.next = None 把兩條切斷 —— 不切的話交錯合併會接出一個環。</text>'''

emit({
 "num": 143, "slug": "reorder-list",
 "en": [
   "You are given the head of a singly linked-list. The list can be represented as:",
   ("c", "L0 → L1 → … → Ln-1 → Ln"),
   "<em>Reorder the list to be on the following form:</em>",
   ("c", "L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …"),
   "You may not modify the values in the list's nodes. Only nodes themselves may be changed.",
 ],
 "zh": [
   "給你一條單向鏈結串列 <code>L0 → L1 → … → Ln-1 → Ln</code>，"
   "把它<strong>重新排列</strong>成：",
   ("c", "L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …"),
   "也就是<strong>「頭一個、尾一個」交錯著來</strong>。",
   "<strong>不能修改節點的值，只能改指標。</strong>",
 ],
 "pre": [
   ("note", "★ 三個基本功的組合", [
     ("c", """這題本身沒有新東西 —— 它是三道經典題串起來：

    ① 找中點        （第 876 題：快慢指標）
    ② 反轉串列      （第 206 題：prev / cur / next 三指標）
    ③ 交錯合併兩條  （第 21 題的變形）

【為什麼這樣就對了？】

    目標順序是 L0, Ln, L1, Ln-1, L2, ...

    拆開來看：
        奇數位置：L0, L1, L2, ...        -> 就是【前半段】
        偶數位置：Ln, Ln-1, Ln-2, ...    -> 就是【後半段的反轉】

    所以：把串列切成兩半、後半反轉、然後交錯接起來 ✔

【這種「把難題拆成幾個已知子問題」的能力，
  比任何單一技巧都重要。】

    面試時明確說出這三步，
    比直接開始寫程式更能展示你的思路。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [1,2,3,4]
  輸出：[1,4,2,3]

  說明：前半 [1,2]，後半 [3,4] 反轉成 [4,3]
        交錯：1, 4, 2, 3 ✔

範例 2
  輸入：head = [1,2,3,4,5]
  輸出：[1,5,2,4,3]

  說明：前半 [1,2,3]，後半 [4,5] 反轉成 [5,4]
        交錯：1, 5, 2, 4, 3 ✔
        【前半比後半多一個，多的那個放最後。】""",
 "constraints": [
   "串列的節點數在 <code>[1, 5 × 10⁴]</code> 之間",
   "1 ≤ <code>Node.val</code> ≤ 1000",
 ],
 "idea": [
   ("fig", _P143_FIG, "0 0 640 452"),
   ("c", """【第一步：找中點】

    slow, fast = head, head.next        ★ fast 錯開一步
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    這樣 slow 會停在【前半的最後一個節點】：

        n = 4: 1 2 | 3 4   -> slow 停在 2 ✔
        n = 5: 1 2 3 | 4 5 -> slow 停在 3 ✔

    【如果 fast 也從 head 出發】：
        n = 4 時 slow 會停在 3 -> 前半 [1,2,3]、後半 [4]
        那樣前半比後半多【兩個】，交錯就會亂掉。

    所以這裡要「錯開一步」。

    （第 876 題「找中間節點」要的是另一種停法，
      兩者的初始化不同 —— 要看題目需要哪一邊。）

【第二步：反轉後半 + 切斷】

    second = slow.next
    slow.next = None            ★ 切斷！

    prev = None
    while second:
        nxt = second.next
        second.next = prev
        prev = second
        second = nxt

    【不切斷的話】：
        前半的最後一個還指著後半的第一個，
        交錯合併時就會接出一個【環】-> 無窮迴圈。

【第三步：交錯合併】

    first, second = head, prev
    while second:
        f_next, s_next = first.next, second.next   ★ 先存起來
        first.next = second
        second.next = f_next
        first, second = f_next, s_next

    【為什麼迴圈條件是 while second？】

        前半的長度 >= 後半，所以 second 會先用完 ✔
        用 while first 的話，最後一輪 second 會是 None，
        second.next 就爆了。

【複雜度】：三步各 O(n)，總共 O(n) 時間、O(1) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "找中點 + 反轉 + 交錯（標準答案）", [
     ("c", S["p143"]),
     "<strong>O(n) 時間、O(1) 空間。</strong>"
     "<strong>三步各十行左右，每一步都是獨立的經典操作。</strong>",
     ("h", "★ 指標題的鐵律：動之前先存起來"),
     ("c", """f_next, s_next = first.next, second.next
first.next = second
second.next = f_next

    如果不先存 f_next：

        first.next = second       ← first.next 被蓋掉了
        second.next = first.next  ← 這時 first.next 已經是 second
                                     -> second.next = second -> 自環 ✘

    【「先把要用的存起來，再改指標」
      是所有鏈結串列題的第一鐵律。】

    反轉那一段也是同樣的道理：
        nxt = second.next      ← 先存
        second.next = prev     ← 再改

    第 206、24、25、61、138 題全部都要注意這件事。""",),
     ("h", "為什麼要特判 <code>not head.next</code>？"),
     ("c", """單一節點時：

    slow, fast = head, head.next = head, None
    while fast and fast.next  -> fast 是 None，不跑

    second = slow.next = None
    slow.next = None           （本來就是 None）

    反轉迴圈不跑，prev = None
    交錯迴圈 while second（= None）不跑

    結果：串列不變 ✔ 其實不用特判也對。

    但寫了更明確，而且【空串列（head = None）一定要擋】——
    否則 head.next 會 AttributeError。

    題目保證至少一個節點，但養成防禦的習慣。""",),
   ], "O(n)", "O(1)", "三趟掃描", "幾個指標", optimal=True),

   ap("解法二", "倒進陣列 + 雙指標（最好寫）", [
     ("c", S["p143_array"]),
     ("c", """把節點倒進 list，就能【隨機存取】——
問題瞬間變成「兩個指標往中間夾」。

    i 從左、j 從右，交替接起來。

【★ 最後的邊界處理】

    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i == j: break            ★ 奇數長度時，中間那個不用再接
        nodes[j].next = nodes[i]
        j -= 1
    nodes[i].next = None            ★ 最後一個要斷尾

    【如果忘了 nodes[i].next = None】：
        最後一個節點還指著原本的下一個 -> 接出一個環 ✘

    這是這個解法第一名的 bug。

【複雜度】：O(n) 時間、O(n) 空間。

    5×10^4 個節點的 list 只有幾百 KB —— 完全可以接受。

【什麼時候選這個？】

    ✔ 面試時間緊迫（這個十分鐘就能寫對）
    ✔ 你對指標操作沒把握

    ✘ 面試官明確要求 O(1) 空間

【這個「把串列倒進陣列」的手法很通用】——
    第 109、148、234 題都可以這樣簡化。
    代價永遠是 O(n) 空間。""",),
   ], "O(n)", "O(n)", "兩趟", "節點陣列"),

   ap("解法三", "堆疊（概念上最貼近題意）", [
     ("c", S["p143_stack"]),
     ("c", """把所有節點壓進堆疊，
然後「從前面拿一個、從堆疊頂拿一個」交替接。

    堆疊頂 = 最後一個節點 ✔

【迴圈跑 n // 2 次】：

    每一輪接一對（前面一個 + 後面一個）。

    n = 4: 跑 2 輪 -> 接 (1,4) 和 (2,3) ✔
    n = 5: 跑 2 輪 -> 接 (1,5) 和 (2,4)，
           剩下 3 自己在中間 ✔

【最後 cur.next = None 斷尾】

    迴圈結束時 cur 指向「中間那個節點」
    （偶數長度時是後半的第一個），
    它的 next 還指著舊的下一個 -> 要清掉。

    忘了就會接出環。

【和解法二本質相同】（都是 O(n) 空間），
    只是用堆疊表達「從後往前」這件事。

    我覺得解法二的雙指標更清楚，
    但堆疊版更貼近「交錯」的直覺。""",),
   ], "O(n)", "O(n)", "兩趟", "節點堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "好寫嗎", "備註"],
   [["一、中點+反轉+交錯", "O(n)", "O(1)", "★☆☆", "標準答案"],
    ["二、倒進陣列", "O(n)", "O(n)", "★★★", "最快寫對"],
    ["三、堆疊", "O(n)", "O(n)", "★★☆", "概念直觀"]]),
 "edges": [
   "<strong>單一節點</strong> → 不變。",
   "<strong>兩個節點</strong> <code>[1,2]</code> → <code>[1,2]</code>（不變）。",
   "<strong>三個節點</strong> <code>[1,2,3]</code> → <code>[1,3,2]</code>。",
   "<strong>偶數長度</strong> <code>[1,2,3,4]</code> → <code>[1,4,2,3]</code>。",
   "<strong>奇數長度</strong> <code>[1,2,3,4,5]</code> → <code>[1,5,2,4,3]</code>。"
   "<strong>中間那個留在最後。</strong>",
   "<strong>忘了 <code>slow.next = None</code>（切斷）</strong> → "
   "<strong>接出一個環，<code>from_list</code> 會無窮迴圈。本題第一名的 bug。</strong>",
   "<strong>解法二忘了 <code>nodes[i].next = None</code></strong> → 同樣接出環。",
   "<strong>交錯時沒有「先存再改」</strong> → 產生自環。",
   "<strong><code>fast</code> 從 <code>head</code> 而不是 <code>head.next</code> 出發</strong> → "
   "<strong>偶數長度時切錯邊，前半比後半少一個。</strong>",
   "<strong>交錯迴圈用 <code>while first</code></strong> → 最後一輪 <code>second</code> 是 "
   "<code>None</code>，<code>second.next</code> 爆炸。",
 ],
 "follow": [
   ("h", "追問一：「找中點」有幾種停法？怎麼選？"),
   ("c", """【寫法 A】slow = fast = head

    while fast and fast.next:
        slow = slow.next; fast = fast.next.next

    n 偶數 -> slow 停在【後半的第一個】（n=4 停在 3）
    n 奇數 -> slow 停在【正中間】（n=5 停在 3）

    適合：第 876 題（回傳中間節點，偶數時要後面那個）

【寫法 B】slow, fast = head, head.next    （本題用的）

    n 偶數 -> slow 停在【前半的最後一個】（n=4 停在 2）
    n 奇數 -> slow 停在【正中間】（n=5 停在 3）

    適合：需要「從 slow 後面切開」的場合
          （本題、第 148 題排序串列）

【寫法 C】用 prev 記住 slow 的前一個

    適合：需要「在 slow 之前切開」的場合

【選擇標準】：
    問自己「我要在哪裡切？切完兩半要多長？」
    然後用 n = 2, 3, 4 手動驗一次。

    【快慢指標的停法不背，用小例子驗。】""",),
   ("h", "追問二：能不能用遞迴？"),
   ("c", """可以，但空間是 O(n)（遞迴堆疊），失去了 O(1) 的優勢。

    一種寫法：遞迴到底，回來時「從外往內」接。

    def go(first, n):
        「處理 first 開始的 n 個節點，回傳處理完之後的尾巴」

    但這個寫法很繞，而且 5×10^4 的深度會 RecursionError。

【樹的題目遞迴自然，串列的題目迭代自然】——

    因為串列的操作通常是「線性推進 + 改指標」，
    而遞迴帶來的「回來時做事」在這裡用處不大。

    例外：第 206 題（反轉串列）的遞迴版很漂亮，
    第 234 題（回文串列）的遞迴版也有它的巧思。""",),
   ("h", "追問三：如果要「反過來」（從 <code>L0 → Ln → L1 → …</code> 還原成原順序）呢？"),
   "<strong>把三個步驟倒過來做</strong>："
   "<strong>先「解交錯」成兩條（奇數位置一條、偶數位置一條），</strong>"
   "<strong>再把第二條反轉，最後接回第一條後面。</strong>",
   "<strong>「解交錯」就是第 328 題（奇偶鏈結串列）。</strong>"
   "<strong>三個步驟各自都有對應的反操作 —— 這是「可逆變換」的好性質。</strong>",
   ("h", "追問四：為什麼題目要說「不能修改節點的值」？"),
   ("c", """因為有一個作弊解法：
    把所有值倒進陣列，重排，再寫回去。

    def reorderList(head):
        vals = []
        cur = head
        while cur: vals.append(cur.val); cur = cur.next
        新順序 = 交錯(vals)
        cur = head
        for v in 新順序: cur.val = v; cur = cur.next

    O(n) 時間、O(n) 空間，而且【完全不用碰指標】。

【題目禁止它，是為了逼你練習指標操作。】

    在真實工程裡，「只改值不改指標」有時反而是對的 ——
    因為外部可能持有某些節點的參考，
    改指標會讓那些參考指向錯的位置。

    【「能不能改值 / 能不能改結構」
      在真實 API 設計裡是重要的契約。】""",),
 ],
 "related": [
   "<strong>第 876 題 Middle of the Linked List</strong> —— 第一步",
   "<strong>第 206 題 Reverse Linked List</strong> —— 第二步",
   "<strong>第 21 題 Merge Two Sorted Lists</strong> —— 第三步的變形",
   "<strong>第 234 題 Palindrome Linked List</strong> —— 同樣的「找中點 + 反轉後半」",
   "<strong>第 328 題 Odd Even Linked List</strong> —— 「解交錯」",
 ],
 "check": [
   "這題拆成哪三個子問題？各自對應哪一道經典題？",
   "<code>fast</code> 為什麼要從 <code>head.next</code> 出發？從 <code>head</code> 出發會怎樣？",
   "為什麼一定要 <code>slow.next = None</code>？不切會發生什麼？",
   "交錯合併時為什麼要「先把 <code>next</code> 存起來」？",
 ],
})
print("P143 written")

# ==================== 144 / 145. Preorder / Postorder Traversal ====================
def _bt(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _bt(l), _bt(r))


def _rand_bt(n, lo=-9, hi=9):
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi), _rand_bt(left, lo, hi), _rand_bt(n - 1 - left, lo, hi))


def _shape_bt(nd):
    return "#" if nd is None else "(%s|%s)" % (_shape_bt(nd.left), _shape_bt(nd.right))


S["p144_rec"] = '''class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def go(node):
            if not node:
                return
            res.append(node.val)        # 根
            go(node.left)               # 左
            go(node.right)              # 右

        go(root)
        return res'''

S["p144_stack"] = '''class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # 【先 push 右，後 push 左】—— 這樣 pop 出來才是「先左後右」
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res'''

S["p144_morris"] = '''class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, cur = [], root

        while cur:
            if not cur.left:
                res.append(cur.val)     # 沒有左子樹：直接輸出，往右走
                cur = cur.right
            else:
                pre = cur.left          # 找左子樹的最右節點（中序前驅）
                while pre.right and pre.right is not cur:
                    pre = pre.right

                if not pre.right:       # 第一次來：架線，【在這裡輸出】
                    res.append(cur.val)
                    pre.right = cur
                    cur = cur.left
                else:                   # 第二次來：拆線，往右走
                    pre.right = None
                    cur = cur.right

        return res'''


def _pre_ref(nd):
    return [] if nd is None else [nd.val] + _pre_ref(nd.left) + _pre_ref(nd.right)


_p144 = [S.load(k) for k in ("p144_rec", "p144_stack", "p144_morris")]

for spec in [[1, None, [2, [3, None, None], None]], None, [1, None, None],
             [1, [2, None, None], [3, None, None]]]:
    want = _pre_ref(_bt(spec))
    for sol in _p144:
        t = _bt(spec)
        shape = _shape_bt(t)
        assert sol.preorderTraversal(t) == want, ("P144", spec, sol)
        assert _shape_bt(t) == shape, ("P144 樹被改壞", spec, sol)

for _ in range(4000):
    t = _rand_bt(random.randrange(0, 13))
    want = _pre_ref(t)
    shape = _shape_bt(t)
    for sol in _p144:
        assert sol.preorderTraversal(t) == want, ("P144 random", want, sol)
        assert _shape_bt(t) == shape, ("P144 樹被改壞", sol)
print("P144 solutions OK")

S["p145_rec"] = '''class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def go(node):
            if not node:
                return
            go(node.left)               # 左
            go(node.right)              # 右
            res.append(node.val)        # 根

        go(root)
        return res'''

S["p145_rev"] = '''class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # 後序（左右根）的反序 = 根右左，那正好是「前序但先走右邊」
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:               # 【先 push 左】-> pop 出來先右後左
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]                # 最後整個反轉'''

S["p145_strict"] = '''class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        cur, last = root, None          # last = 上一個被輸出的節點

        while cur or stack:
            while cur:                  # 一路往左沉到底
                stack.append(cur)
                cur = cur.left

            node = stack[-1]            # 先看，不要急著 pop
            if node.right and node.right is not last:
                cur = node.right        # 右子樹還沒走 -> 去走它
            else:
                res.append(node.val)    # 左右都走完了 -> 輸出自己
                stack.pop()
                last = node

        return res'''


def _post_ref(nd):
    return [] if nd is None else _post_ref(nd.left) + _post_ref(nd.right) + [nd.val]


_p145 = [S.load(k) for k in ("p145_rec", "p145_rev", "p145_strict")]

for spec in [[1, None, [2, [3, None, None], None]], None, [1, None, None],
             [1, [2, None, None], [3, None, None]]]:
    want = _post_ref(_bt(spec))
    for sol in _p145:
        t = _bt(spec)
        shape = _shape_bt(t)
        assert sol.postorderTraversal(t) == want, ("P145", spec, sol)
        assert _shape_bt(t) == shape, ("P145 樹被改壞", spec, sol)

for _ in range(4000):
    t = _rand_bt(random.randrange(0, 13))
    want = _post_ref(t)
    shape = _shape_bt(t)
    for sol in _p145:
        assert sol.postorderTraversal(t) == want, ("P145 random", want, sol)
        assert _shape_bt(t) == shape, ("P145 樹被改壞", sol)
print("P145 solutions OK")

_P144_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">三種走訪的差別，只在於「什麼時候輸出根節點」。DFS 的路線完全一樣。</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="320" cy="64" r="19" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="320" y="69" fill="var(--gold)">1</text>
              <circle cx="220" cy="132" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="220" y="137" fill="var(--accent)">2</text>
              <circle cx="420" cy="132" r="19" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="420" y="137" fill="#ff8a65">3</text>
              <circle cx="160" cy="200" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="160" y="205" fill="var(--accent)">4</text>
              <circle cx="280" cy="200" r="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="280" y="205" fill="var(--accent)">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="306" y1="78" x2="234" y2="118"/><line x1="334" y1="78" x2="406" y2="118"/>
              <line x1="206" y1="146" x2="174" y2="186"/><line x1="234" y1="146" x2="266" y2="186"/>
            </g>
            <text x="20" y="252" fill="var(--gold)" font-size="13">前序（根左右）： 1, 2, 4, 5, 3　　【進入節點時輸出】</text>
            <text x="20" y="282" fill="var(--accent)" font-size="13">中序（左根右）： 4, 2, 5, 1, 3　　【從左子樹回來時輸出】</text>
            <text x="20" y="312" fill="#ff8a65" font-size="13">後序（左右根）： 4, 5, 2, 3, 1　　【從右子樹回來時輸出】</text>
            <line x1="20" y1="336" x2="620" y2="336" stroke="var(--border)"/>
            <text x="20" y="364" fill="var(--accent)" font-size="12">★ 迭代版的難度排序：前序 &lt; 中序 &lt;&lt; 後序</text>
            <text x="40" y="392" fill="var(--text-muted)" font-size="12">前序：一 pop 就輸出 —— 最簡單。先 push 右、後 push 左，pop 出來就是左先右後。</text>
            <text x="40" y="418" fill="var(--text-muted)" font-size="12">中序：一路往左沉，pop 的時候輸出，然後轉向右。</text>
            <text x="40" y="444" fill="#ff8a65" font-size="12">後序：要「左右都走完」才能輸出自己 —— 必須知道「右子樹到底走了沒」。</text>
            <text x="20" y="476" fill="var(--gold)" font-size="12">取巧解法：後序的【反序】是「根右左」，那就是「前序但先走右邊」→ 做完再 reverse。</text>'''

emit({
 "num": 144, "slug": "binary-tree-preorder-traversal",
 "en": [
   "Given the <code>root</code> of a binary tree, return <em>the preorder traversal of its "
   "nodes' values</em>.",
   "<strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，回傳它的<strong>前序走訪</strong>結果。",
   "<strong>前序</strong>的順序是：<strong>根 → 左子樹 → 右子樹</strong>。",
   "<strong>進階：</strong>遞迴版太簡單了，你能用<strong>迭代</strong>的方式做嗎？",
 ],
 "pre": [
   ("note", "三種走訪，差別只在「什麼時候輸出根」", [
     ("c", """def dfs(node):
    if not node: return
    # 【前序】在這裡輸出        <- 進入節點時
    dfs(node.left)
    # 【中序】在這裡輸出        <- 從左子樹回來時
    dfs(node.right)
    # 【後序】在這裡輸出        <- 從右子樹回來時

    【DFS 走的路線完全相同】，
    差別只是「在路線的哪一個時刻記下這個節點」。

    每個節點都會被「經過」三次：
        第一次：剛進來（前序的時機）
        第二次：左子樹回來了（中序的時機）
        第三次：右子樹也回來了（後序的時機）

【這個觀察是理解三種走訪的關鍵】——
    它們不是三個演算法，是【同一個演算法的三個輸出時機】。

【迭代版的難度】：
    前序 < 中序 << 後序

    因為前序「一進來就輸出」，不用記住任何額外狀態；
    後序要「等左右都走完」，必須知道「右子樹走了沒」。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,null,2,3]

        1
         \\
          2
         /
        3

  輸出：[1,2,3]

範例 2
  輸入：root = []
  輸出：[]

範例 3
  輸入：root = [1]
  輸出：[1]""",
 "constraints": [
   "樹的節點數在 <code>[0, 100]</code> 之間",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "idea": [
   ("fig", _P144_FIG, "0 0 640 494"),
   ("c", """【迭代版的核心：先 push 右，後 push 左】

    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right: stack.append(node.right)
        if node.left:  stack.append(node.left)

【為什麼順序要反過來？】

    堆疊是【後進先出】——
    後 push 的會先被 pop。

    我們要「先處理左、再處理右」，
    所以要【後 push 左】。

    驗證：
        push 1
        pop 1 -> 輸出 1，push 3（右），push 2（左）
        stack = [3, 2]
        pop 2 -> 輸出 2 ✔ （左先）
        ...

【這是前序迭代版唯一的技巧】，
    也是它比中序、後序都簡單的原因 ——
    一 pop 就輸出，不用記任何狀態。

【對照中序迭代版】（第 94 題）：

    while stack or node:
        while node:                 一路往左沉
            stack.append(node); node = node.left
        node = stack.pop()          彈出時輸出
        res.append(node.val)
        node = node.right           轉向右

    它需要「先沉到底」這個額外的內層迴圈 ——
    因為「輸出的時機」在「左子樹處理完之後」。"""),
 ],
 "approaches": [
   ap("解法一", "遞迴（三行）", [
     ("c", S["p144_rec"]),
     "<strong>直接把定義翻成程式碼。</strong>"
     "<strong>「根、左、右」三行，順序就是答案。</strong>",
     "<strong>時間 O(n)、空間 O(h)</strong>（遞迴堆疊）。",
     "<strong>本題 n ≤ 100，遞迴完全安全。</strong>",
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊"),

   ap("解法二", "堆疊迭代（進階要求的答案）", [
     ("c", S["p144_stack"]),
     "<strong>十行，而且是三種走訪裡最好寫的迭代版。</strong>",
     ("h", "為什麼這個版本這麼簡單？"),
     ("c", """因為前序「一進入節點就輸出」——
沒有「等子樹回來」這回事，所以不需要記錄狀態。

    堆疊的角色只是「待處理的節點清單」，
    而不是「回家的路」。

【對照後序】：
    後序必須知道「這個節點的右子樹走完了沒」，
    所以要嘛記 last（解法三），
    要嘛在堆疊裡存 (節點, 狀態)。

【一個常見的變體寫法】：

    stack = []
    node = root
    while node or stack:
        while node:
            res.append(node.val)        # 一路往左，沿路輸出
            stack.append(node)
            node = node.left
        node = stack.pop().right        # 回頭轉向右

    這個版本和中序的骨架一樣，
    只是把「輸出」從 pop 之後移到 push 之前。

    【兩種寫法都對。第一種更短，第二種和中序共用骨架。】""",),
     "<strong>空間 O(h)</strong>（堆疊最多存一條路徑上的節點）。",
   ], "O(n)", "O(h)", "每個節點進出堆疊一次", "顯式堆疊", optimal=True),

   ap("解法三", "Morris 前序走訪（O(1) 空間）", [
     ("c", S["p144_morris"]),
     ("h", "和中序 Morris（第 94 題）只差一行的位置"),
     ("c", """中序 Morris：在【拆線時】輸出
前序 Morris：在【架線時】輸出

    if not pre.right:
        res.append(cur.val)     ★ 前序在這裡輸出
        pre.right = cur
        cur = cur.left
    else:
        pre.right = None
        # 中序在這裡輸出
        cur = cur.right

【為什麼？】

    「架線」發生在【第一次造訪這個節點】時 -> 前序的時機 ✔
    「拆線」發生在【左子樹走完回來】時     -> 中序的時機 ✔

    又一次印證了「三種走訪只是三個輸出時機」。

【後序也能用 Morris 嗎？】

    可以，但複雜很多 ——
    需要「反轉右邊緣再輸出再轉回來」的技巧。

    面試幾乎不會考，知道「存在但很麻煩」就好。

【O(1) 空間、O(n) 時間（攤還）】

    和第 94、99、114 題的 Morris 是同一套分析：
    每條邊最多被走常數次。

【注意它會暫時修改樹】——
    走完之後會還原，但過程中樹是壞的。
    多執行緒或唯讀樹不能用。""",),
     "<strong>本題 n ≤ 100，完全不需要 O(1) 空間</strong> —— "
     "<strong>這個版本是為了「和第 94、99、114 題連起來」而寫的。</strong>",
   ], "O(n)", "O(1)", "攤還每條邊常數次", "只用兩個指標"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、遞迴", "O(n)", "O(h)", "8", "最短"],
    ["二、堆疊迭代", "O(n)", "O(h)", "12", "進階要求的答案"],
    ["三、Morris", "O(n)", "O(1)", "18", "和 94/99/114 同一套"]]),
 "edges": [
   "<strong><code>root = None</code></strong> → <code>[]</code>。"
   "<strong>迭代版要擋（<code>stack = [root]</code> 會放進 <code>None</code>）。</strong>",
   "<strong>單一節點</strong> → <code>[val]</code>。",
   "<strong>只有右子樹的鏈</strong> <code>[1,null,2,3]</code> → <code>[1,2,3]</code>。",
   "<strong>迭代版先 push 左、後 push 右</strong> → "
   "<strong>變成「根右左」，答案順序錯。</strong>",
   "<strong>把 <code>None</code> 也 push 進堆疊</strong> → <code>node.val</code> 爆炸。",
   "<strong>Morris 版中途 <code>return</code></strong> → 樹上留下沒拆的線。",
   "<strong>100 個節點的鏈狀樹</strong> → 遞迴深度 100，安全。",
 ],
 "follow": [
   ("h", "追問一：三種走訪的迭代版能不能共用一個骨架？"),
   ("c", """可以 —— 用「著色法」（顏色標記法）：

    WHITE, GRAY = 0, 1
    stack = [(WHITE, root)]
    while stack:
        color, node = stack.pop()
        if not node: continue
        if color == WHITE:
            # 按照【想要的順序的反序】push
            # 前序（根左右）-> push 右、左、根
            stack.append((WHITE, node.right))
            stack.append((WHITE, node.left))
            stack.append((GRAY,  node))
        else:
            res.append(node.val)

    改成中序：push 右、根、左
    改成後序：push 根、右、左

    【只要改三行 push 的順序，就能切換三種走訪。】

【這個寫法的代價】：
    每個節點進出堆疊兩次（WHITE 一次、GRAY 一次），
    常數比專用版大。

    但它【統一】了三種走訪，而且非常好記 ——
    在需要「快速寫出後序迭代」時特別有用。""",),
   ("h", "追問二：為什麼前序的迭代版比中序簡單？"),
   "<strong>因為前序「一進入就輸出」—— 堆疊只需要記「還沒處理的節點」。</strong>",
   "<strong>中序要「左子樹處理完才輸出自己」—— 堆疊必須記「回家的路」，"
   "所以要先「一路往左沉到底」。</strong>",
   "<strong>後序更糟：要「左右都處理完」，所以還要額外記錄「右子樹走了沒」。</strong>",
   ("h", "追問三：前序走訪有什麼實際用途？"),
   ("ul", [
     "<strong>複製一棵樹</strong>：先建根，再建左右子樹（第 226 題的翻轉也是）",
     "<strong>序列化</strong>：帶空節點記號的前序可以唯一還原一棵樹（第 297 題）",
     "<strong>檔案系統走訪</strong>：先印目錄名，再印裡面的東西",
     "<strong>運算式樹轉前綴表示法</strong>（波蘭表示法）",
     "<strong>第 105 題</strong>：從前序 + 中序建樹",
   ]),
   "<strong>共同特徵：「先處理自己、再處理子部分」的任務都適合前序。</strong>"
   "<strong>反過來，「需要先知道子部分的結果」的任務（求高度、求和）就要用後序。</strong>",
   ("h", "追問四：如果樹非常深（10⁵ 個節點的鏈）呢？"),
   "<strong>遞迴會 <code>RecursionError</code></strong> —— 要用解法二（堆疊）或解法三（Morris）。",
   "<strong>解法二的堆疊也會有 10⁵ 個元素，但那是 heap 上的 list，不是呼叫堆疊 —— 沒問題。</strong>",
   "<strong>解法三（Morris）連 O(h) 都不用，是唯一真正的 O(1) 空間解。</strong>",
 ],
 "related": [
   "<strong>第 94 題 Inorder Traversal</strong> —— 中序，迭代版稍難",
   "<strong>第 145 題 Postorder Traversal</strong> —— 後序，迭代版最難",
   "<strong>第 102 題 Level Order Traversal</strong> —— BFS 版的走訪",
   "<strong>第 589 題 N-ary Tree Preorder</strong> —— N 元樹版",
   "<strong>第 297 題 Serialize and Deserialize</strong> —— 前序的實際應用",
 ],
 "check": [
   "三種走訪的差別是什麼？「DFS 的路線」有沒有不同？",
   "迭代版為什麼要「先 push 右、後 push 左」？",
   "前序的 Morris 版和中序的差在哪一行？為什麼？",
   "為什麼前序的迭代版比中序、後序都簡單？",
 ],
})
print("P144 written")

_P145_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 後序迭代最難，因為「輸出自己」必須等到左右都走完 —— 要記住「右子樹到底走了沒」。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">取巧解法：把「後序」倒過來看</text>
            <g font-size="13">
              <text x="40" y="84" fill="var(--text-muted)">後序 = 左 → 右 → 根</text>
              <text x="40" y="112" fill="var(--accent)">把它整個反轉 = 根 → 右 → 左</text>
              <text x="40" y="140" fill="var(--gold)">而「根 → 右 → 左」就是【前序，但先走右邊】——</text>
              <text x="40" y="168" fill="var(--gold)">那個用堆疊寫起來超簡單（第 144 題那個，只是 push 順序反過來）。</text>
            </g>
            <text x="20" y="206" fill="var(--accent)" font-size="12">所以：用前序的骨架跑出「根右左」，最後 res[::-1] —— 就是後序 ✔</text>
            <line x1="20" y1="230" x2="620" y2="230" stroke="var(--border)"/>
            <text x="20" y="258" fill="#ff8a65" font-size="13">嚴格版（不反轉）：用 last 記住「上一個輸出的節點」</text>
            <g font-size="12">
              <text x="40" y="288" fill="var(--text-muted)">while cur: 一路往左沉，把路徑壓進堆疊</text>
              <text x="40" y="314" fill="var(--text-muted)">node = stack[-1]　　★ 先【看】不要 pop —— 可能還要回來</text>
              <text x="40" y="342" fill="var(--accent)">if node.right and node.right is not last:</text>
              <text x="60" y="368" fill="var(--accent)">cur = node.right　　右子樹還沒走 → 去走它（node 留在堆疊上）</text>
              <text x="40" y="396" fill="var(--gold)">else:</text>
              <text x="60" y="422" fill="var(--gold)">輸出 node、pop 掉、last = node　　左右都走完了</text>
            </g>
            <text x="20" y="456" fill="#ff8a65" font-size="12">★ last 的作用：區分「還沒走右子樹」和「剛從右子樹回來」——</text>
            <text x="20" y="480" fill="var(--text-muted)" font-size="12">沒有它的話，走完右子樹回到 node 時會【又跑去走一次右子樹】，變成無窮迴圈。</text>'''

emit({
 "num": 145, "slug": "binary-tree-postorder-traversal",
 "en": [
   "Given the <code>root</code> of a binary tree, return <em>the postorder traversal of its "
   "nodes' values</em>.",
   "<strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，回傳它的<strong>後序走訪</strong>結果。",
   "<strong>後序</strong>的順序是：<strong>左子樹 → 右子樹 → 根</strong>。",
   "<strong>進階：</strong>遞迴版太簡單了，你能用<strong>迭代</strong>的方式做嗎？",
 ],
 "pre": [
   ("note", "★ 為什麼後序的迭代版是三種裡面最難的", [
     ("c", """前序：一進入節點就輸出       -> 不用記任何狀態
中序：左子樹走完就輸出       -> 要記「回家的路」（堆疊）
後序：左【和】右都走完才輸出 -> 還要記「右子樹走了沒」

【問題出在哪裡？】

    當你從堆疊 pop 出一個節點時，
    你不知道它是：
        (a) 第一次被看到（左右都還沒走）
        (b) 左子樹剛走完（右邊還沒走）
        (c) 右子樹也走完了（可以輸出了）

    前序和中序只需要區分兩種狀態（靠堆疊的結構就夠），
    後序需要區分三種 -> 必須額外記錄。

【三條解法】：

    (a) 記 last = 上一個輸出的節點（解法三，最嚴格）
    (b) 在堆疊裡存 (節點, 訪問次數) 這樣的狀態
    (c) 【取巧】：算出「根右左」，最後反轉（解法二）

    (c) 最簡單，也是面試最常見的答案。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,null,2,3]

        1
         \\
          2
         /
        3

  輸出：[3,2,1]

範例 2
  輸入：root = []
  輸出：[]

範例 3
  輸入：root = [1]
  輸出：[1]""",
 "constraints": [
   "樹的節點數在 <code>[0, 100]</code> 之間",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "idea": [
   ("fig", _P145_FIG, "0 0 640 498"),
   ("c", """【取巧解法（解法二）：反向前序】

    後序      = 左 → 右 → 根
    它的反序  = 根 → 右 → 左

    而「根 → 右 → 左」就是【前序，但先走右邊】——
    那個用堆疊寫起來超簡單（第 144 題的骨架，push 順序反過來）。

    所以：
        1. 用前序的骨架跑出「根右左」
        2. 最後 res[::-1]

    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:  stack.append(node.left)     ★ 先 push 左
        if node.right: stack.append(node.right)    ★ 後 push 右
    return res[::-1]

    【push 順序和前序【相反】，最後再反轉。】

【嚴格解法（解法三）：用 last 記住進度】

    cur, last = root, None
    while cur or stack:
        while cur:                      一路往左沉
            stack.append(cur); cur = cur.left

        node = stack[-1]                ★ 只看，不 pop
        if node.right and node.right is not last:
            cur = node.right            右子樹還沒走
        else:
            res.append(node.val)        輸出
            stack.pop()
            last = node

【★ last 的作用】

    走完右子樹回到 node 時，
    node.right is last 成立 -> 知道「剛從右邊回來」
    -> 可以輸出自己了 ✔

    沒有 last 的話，會【又跑去走一次右子樹】-> 無窮迴圈。

【★ 為什麼是 stack[-1] 而不是 stack.pop()？】

    因為這個節點可能還要「回來」一次（去走右子樹之後）。
    先 pop 的話就回不來了。"""),
 ],
 "approaches": [
   ap("解法一", "遞迴（三行）", [
     ("c", S["p145_rec"]),
     "<strong>「左、右、根」三行。</strong>"
     "<strong>和前序、中序只差 <code>res.append</code> 那一行的位置。</strong>",
     "<strong>時間 O(n)、空間 O(h)。</strong>",
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊"),

   ap("解法二", "反向前序 + 反轉（最推薦的迭代版）", [
     ("c", S["p145_rev"]),
     ("h", "為什麼這樣就對了？"),
     ("c", """設後序序列是 P = [左子樹的後序] [右子樹的後序] [根]

    反轉之後：
        P[::-1] = [根] [右子樹的後序的反轉] [左子樹的後序的反轉]

    由歸納法，「某棵子樹的後序的反轉」= 那棵子樹的「根右左」序列。

    所以 P[::-1] = 根 → (右子樹的根右左) → (左子樹的根右左)
                 = 整棵樹的「根右左」序列 ✔

    而「根右左」用堆疊做，只要把前序版的 push 順序反過來。

【這個技巧的價值】：

    它把「最難的迭代版」變成「最簡單的迭代版 + 一次反轉」。

    反轉的成本是 O(n)，總複雜度不變 ✔

【面試時的說法】：

    「後序的反序是『根右左』，那就是前序但先走右邊 ——
      我用那個骨架跑完再 reverse。」

    講得出這句話，就不用寫解法三了。""",),
     ("h", "和前序版逐行對照"),
     ("c", """前序（第 144 題）：           後序（本題）：

    if node.right:                if node.left:
        stack.append(node.right)      stack.append(node.left)
    if node.left:                 if node.right:
        stack.append(node.left)       stack.append(node.right)

    return res                    return res[::-1]

    【push 順序對調 + 最後反轉】—— 就這兩個差別。""",),
     "<strong>O(n) 時間、O(h) 空間。</strong>"
     "<strong>程式碼和前序版幾乎一樣長 —— 這就是為什麼它是最推薦的版本。</strong>",
   ], "O(n)", "O(h)", "每個節點一次 + 反轉", "顯式堆疊", optimal=True),

   ap("解法三", "嚴格的後序迭代（用 <code>last</code> 記進度）", [
     ("c", S["p145_strict"]),
     ("h", "★ 三個容易錯的地方"),
     ("c", """1. 【node = stack[-1] 而不是 stack.pop()】

   這個節點可能還要「回來」（走完右子樹之後），
   所以先看不 pop。

   只有在「確定要輸出」時才 pop。

2. 【node.right is not last 的 is】

   要比較「是不是同一個節點物件」，不是值。
   值可能重複 -> 用 == 會誤判。

3. 【last 一定要更新】

   忘了 last = node 的話，
   下一次回到父節點時會誤以為「右子樹還沒走」
   -> 無窮迴圈。

【為什麼這個版本值得會？】

    ✔ 它是「真正的後序走訪」——
       節點是【按後序的順序被處理的】

    ✘ 解法二是「先算出反序再翻過來」——
       如果你需要「邊走邊做事」（例如釋放記憶體），
       解法二就不行了，因為它的處理順序是反的。

【實際例子】：
    要「後序地釋放一棵樹的記憶體」（先釋放子節點再釋放父節點），
    就必須用解法三 ——
    解法二會先釋放父節點，然後子節點就找不到了。

    【「順序本身有意義」時，不能用「算完再反轉」的取巧。】""",),
     "<strong>O(n) 時間、O(h) 空間。</strong>"
     "<strong>比解法二長，但它是真正按後序順序處理節點的版本。</strong>",
   ], "O(n)", "O(h)", "每個節點最多進出堆疊兩次", "顯式堆疊 + last"),
 ],
 "compare": (["解法", "時間", "空間", "處理順序是後序嗎", "備註"],
   [["一、遞迴", "O(n)", "O(h)", "✔", "最短"],
    ["二、反向前序 + 反轉", "O(n)", "O(h)", "✘ 是反的", "最推薦的迭代版"],
    ["三、嚴格後序迭代", "O(n)", "O(h)", "✔", "順序有意義時才需要"]]),
 "edges": [
   "<strong><code>root = None</code></strong> → <code>[]</code>。"
   "<strong>解法二要擋，解法三的 <code>while cur or stack</code> 天然擋掉 ✔</strong>",
   "<strong>單一節點</strong> → <code>[val]</code>。",
   "<strong>只有右子樹的鏈</strong> <code>[1,null,2,3]</code> → <code>[3,2,1]</code>。",
   "<strong>解法二忘了 <code>[::-1]</code></strong> → 得到「根右左」，完全反了。",
   "<strong>解法二的 push 順序沒對調</strong> → 得到「根左右」的反序 = 「右左根」，錯。",
   "<strong>解法三用 <code>stack.pop()</code> 而不是 <code>stack[-1]</code></strong> → "
   "<strong>節點回不來，右子樹永遠走不到。</strong>",
   "<strong>解法三忘了更新 <code>last</code></strong> → <strong>無窮迴圈。</strong>",
   "<strong>解法三用 <code>==</code> 而不是 <code>is</code></strong> → 值重複時誤判。",
 ],
 "follow": [
   ("h", "追問一：後序走訪有什麼實際用途？"),
   ("ul", [
     "<strong>釋放樹的記憶體</strong>：必須先釋放子節點（父節點釋放後就找不到子節點了）",
     "<strong>計算子樹的統計量</strong>：高度、節點數、和 —— 都需要先知道子樹的結果",
     "<strong>第 110 題 平衡二元樹</strong>、<strong>第 124 題 最大路徑和</strong>：都是後序",
     "<strong>運算式樹求值</strong>：先算出左右運算元，再套用運算子",
     "<strong>逆波蘭表示法</strong>（第 150 題）就是運算式樹的後序走訪",
   ]),
   "<strong>共同特徵：「需要先知道子部分的結果」的任務。</strong>"
   "<strong>這就是為什麼「後序回傳一包資訊」是樹題最重要的範式（第 110 題講過）。</strong>",
   ("h", "追問二：「算完再反轉」的取巧什麼時候不能用？"),
   ("c", """當【處理的順序本身有副作用】時。

    例子一：釋放記憶體
        必須真的先釋放子節點 ——
        「算出順序再反轉」的話，
        在算的過程中你已經（按錯誤的順序）碰過節點了。

    例子二：邊走邊修改樹
        解法二在走的時候是「根右左」，
        如果你在那個時機修改節點，順序就錯了。

    例子三：需要提早結束
        解法二必須走完整棵樹才能反轉，
        沒辦法「找到就停」。

【只要求「得到一個 list」的話，解法二完全沒問題 ✔】

    這題就是這種情況，所以解法二是最佳答案。

【一般原則】：
    「先算出結果再調整」的取巧，
    只在「過程沒有副作用」時安全。""",),
   ("h", "追問三：用「著色法」統一三種走訪？"),
   ("c", """WHITE, GRAY = 0, 1
stack = [(WHITE, root)]
while stack:
    color, node = stack.pop()
    if not node: continue
    if color == WHITE:
        # 按【想要的順序的反序】push
        stack.append((WHITE, node.right))   # 後序：根、右、左 的反序
        stack.append((WHITE, node.left))
        stack.append((GRAY,  node))
        # ↑ 這樣 pop 出來是 根、左、右 —— 那是前序！

    # 後序要 push：根、右、左（反序），pop 出來是 左、右、根 ✔
    #   stack.append((GRAY,  node))
    #   stack.append((WHITE, node.right))
    #   stack.append((WHITE, node.left))
    else:
        res.append(node.val)

【規則】：想要什麼順序，就按【反序】push。

    前序（根左右）-> push 右、左、根
    中序（左根右）-> push 右、根、左
    後序（左右根）-> push 根、右、左

    【只改三行，就能切換三種走訪。】

    代價：每個節點進出堆疊兩次，常數較大。
    好處：不用記三套不同的技巧。""",),
   ("h", "追問四：後序的 Morris 版長什麼樣？"),
   "<strong>非常複雜</strong> —— 需要「走完一段左邊緣之後，把它反轉、輸出、再反轉回來」。",
   ("c", """大致流程：
    用中序 Morris 的骨架，
    但在「拆線」的時候，
    輸出「從 cur.left 到 pre」這一段【右邊緣的反轉】。

    反轉是原地做的（像反轉鏈結串列），
    輸出完再反轉回來。

    O(n) 時間、O(1) 空間，但程式碼大約 40 行。

【面試絕對不會考這個。】

    知道「後序 Morris 存在，但要用『反轉右邊緣』的技巧」
    就足夠了。

    第 114 題（展開為鏈結串列）的 Morris 版
    用的是相關但簡單得多的技巧。""",),
 ],
 "related": [
   "<strong>第 144 題 Preorder Traversal</strong> —— 解法二的骨架來源",
   "<strong>第 94 題 Inorder Traversal</strong> —— 中序，難度居中",
   "<strong>第 110/124 題</strong> —— 後序「回傳一包資訊」的實際應用",
   "<strong>第 150 題 逆波蘭表達式求值</strong> —— 後序的實際應用",
   "<strong>第 590 題 N-ary Tree Postorder</strong> —— N 元樹版",
 ],
 "check": [
   "為什麼後序的迭代版比前序、中序都難？它需要多記什麼？",
   "「後序的反序是根右左」怎麼證明？為什麼這讓問題變簡單？",
   "解法三為什麼要用 <code>stack[-1]</code> 而不是 <code>stack.pop()</code>？",
   "什麼情況下不能用「算完再反轉」的取巧？",
 ],
})
print("P145 written")
