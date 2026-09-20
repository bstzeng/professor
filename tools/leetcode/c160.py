# -*- coding: utf-8 -*-
"""第 160、162、164、165、166 題。"""
import random, math
from authoring import emit, ap
from runner import Src, ListNode, to_list, from_list

S = Src()
random.seed(160)

# ==================== 160. Intersection of Two Linked Lists ====================
S["p160_switch"] = '''class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        a, b = headA, headB
        while a is not b:
            # 走到底就換到另一條的頭 —— 兩人走的總長度會一樣
            a = a.next if a else headB
            b = b.next if b else headA

        return a            # 相遇點就是交點（沒有交點時兩人同時變成 None）'''

S["p160_len"] = '''class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(node):
            n = 0
            while node:
                n += 1
                node = node.next
            return n

        la, lb = length(headA), length(headB)

        # 讓比較長的那條先走 |la - lb| 步，之後兩人就「對齊」了
        a, b = headA, headB
        for _ in range(la - lb):
            a = a.next
        for _ in range(lb - la):
            b = b.next

        while a is not b:
            a = a.next
            b = b.next
        return a'''

S["p160_set"] = '''class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        while headA:
            seen.add(headA)         # ★ 存節點物件，不是 val
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next
        return None'''


def _make_y(a_only, b_only, common):
    """造一個 Y 字形：兩條前綴 + 共用的尾巴。回傳 (headA, headB, 交點)。"""
    tail = to_list(common) if common else None
    def prefix(vals):
        if not vals:
            return tail
        h = to_list(vals)
        p = h
        while p.next:
            p = p.next
        p.next = tail
        return h
    return prefix(a_only), prefix(b_only), tail


_p160 = [S.load(k) for k in ("p160_switch", "p160_len", "p160_set")]

for a_only, b_only, common in [
    ([4, 1], [5, 6, 1], [8, 4, 5]),
    ([1, 9, 1], [3], [2, 4]),
    ([2, 6, 4], [1, 5], []),
    ([], [], [1]),
    ([1], [], [2]),
    ([], [1], [2]),
]:
    hA, hB, want = _make_y(a_only, b_only, common)
    for sol in _p160:
        a2, b2, w2 = _make_y(a_only, b_only, common)
        assert sol.getIntersectionNode(a2, b2) is w2, ("P160", a_only, b_only, common, sol)

for _ in range(4000):
    a_only = [random.randint(0, 9) for _ in range(random.randrange(0, 6))]
    b_only = [random.randint(0, 9) for _ in range(random.randrange(0, 6))]
    common = [random.randint(0, 9) for _ in range(random.randrange(0, 5))]
    for sol in _p160:
        hA, hB, want = _make_y(a_only, b_only, common)
        if hA is None or hB is None:
            continue
        assert sol.getIntersectionNode(hA, hB) is want, \
            ("P160 random", a_only, b_only, common, sol)
print("P160 solutions OK")

_P160_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 兩個指標「換軌道」：走到自己的底就跳到對方的頭。兩人走的總距離一定相同 → 必在交點相遇。</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="70" cy="80" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="70" y="85" fill="var(--accent)">4</text>
              <circle cx="140" cy="80" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="140" y="85" fill="var(--accent)">1</text>
              <circle cx="70" cy="180" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="70" y="185" fill="#ff8a65">5</text>
              <circle cx="140" cy="180" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="140" y="185" fill="#ff8a65">6</text>
              <circle cx="210" cy="180" r="16" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="210" y="185" fill="#ff8a65">1</text>
              <circle cx="300" cy="130" r="18" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="300" y="135" fill="var(--gold)">8</text>
              <circle cx="380" cy="130" r="16" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="380" y="135" fill="var(--gold)">4</text>
              <circle cx="460" cy="130" r="16" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="460" y="135" fill="var(--gold)">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="86" y1="80" x2="122" y2="80"/>
              <line x1="156" y1="88" x2="283" y2="122"/>
              <line x1="86" y1="180" x2="122" y2="180"/><line x1="156" y1="180" x2="192" y2="180"/>
              <line x1="226" y1="172" x2="283" y2="142"/>
              <line x1="318" y1="130" x2="362" y2="130"/><line x1="396" y1="130" x2="444" y2="130"/>
            </g>
            <text x="300" y="100" fill="var(--gold)" font-size="11" text-anchor="middle">交點</text>
            <text x="20" y="80" fill="var(--accent)" font-size="11" text-anchor="start">A：</text>
            <text x="20" y="180" fill="#ff8a65" font-size="11" text-anchor="start">B：</text>
            <line x1="20" y1="226" x2="620" y2="226" stroke="var(--border)"/>
            <text x="20" y="254" fill="var(--accent)" font-size="13">為什麼「換軌道」一定會相遇？</text>
            <text x="40" y="284" fill="var(--text-muted)" font-size="12">設 A 獨有部分長 a、B 獨有部分長 b、共用的尾巴長 c。</text>
            <text x="40" y="312" fill="var(--gold)" font-size="12">指標 A 走的路：a + c（走完 A）+ b（換到 B 走到交點）= a + b + c</text>
            <text x="40" y="338" fill="var(--gold)" font-size="12">指標 B 走的路：b + c（走完 B）+ a（換到 A 走到交點）= a + b + c</text>
            <text x="40" y="368" fill="var(--accent)" font-size="12">兩者走的步數【完全相同】→ 同一時刻抵達交點 ✔</text>
            <text x="20" y="402" fill="#ff8a65" font-size="12">★ 沒有交點時呢？c = 0，兩人各走 a + b 步之後【同時】變成 None —— 迴圈結束，回傳 None ✔</text>
            <text x="20" y="428" fill="var(--text-muted)" font-size="12">所以「沒有交點」不需要特判 —— 它自然被這個機制涵蓋了。這是本解法最漂亮的地方。</text>'''

emit({
 "num": 160, "slug": "intersection-of-two-linked-lists",
 "en": [
   "Given the heads of two singly linked-lists <code>headA</code> and <code>headB</code>, return "
   "<em>the node at which the two lists intersect</em>. If the two linked lists have no "
   "intersection at all, return <code>null</code>.",
   "The test cases are generated such that there are no cycles anywhere in the entire linked "
   "structure.",
   "<strong>Note</strong> that the linked lists must <strong>retain their original structure</strong> "
   "after the function returns.",
   "<strong>Follow up:</strong> Could you write a solution that runs in <code>O(m + n)</code> "
   "time and use only <code>O(1)</code> memory?",
 ],
 "zh": [
   "給你兩條單向鏈結串列的頭節點 <code>headA</code> 和 <code>headB</code>，"
   "回傳它們<strong>相交的那個節點</strong>；如果不相交，回傳 <code>None</code>。",
   "測資保證整個結構裡<strong>沒有環</strong>。",
   "<strong>函式回傳之後，兩條串列必須保持原本的結構。</strong>",
   "<strong>進階：</strong>能不能做到 <code>O(m+n)</code> 時間、<code>O(1)</code> 空間？",
   ("note", "「相交」是指「同一個節點物件」", [
     "<strong>不是「值相同」，而是「就是同一個節點」</strong> —— "
     "所以比較時要用 <code>is</code> 而不是 <code>==</code>。",
     "<strong>而且一旦相交，後面就完全共用</strong>（因為每個節點只有一個 <code>next</code>）—— "
     "所以兩條串列會形成一個「Y」字形，而不是「X」形。",
   ]),
 ],
 "pre": [
   ("note", "★ 「Y 字形」這個結構是所有解法的基礎", [
     ("c", """單向串列的每個節點只有【一個】next。

    所以一旦兩條串列在某個節點相交，
    從那個節點開始，它們就【完全重合】了 ——

        A: a1 -> a2 -> ↘
                        c1 -> c2 -> c3 -> None
        B: b1 -> b2 -> b3 -> ↗

    這是 Y 形，不可能是 X 形（分開又合起來）。

【這帶來兩個重要的推論】：

    1. 兩條串列的【尾巴一定相同】（如果相交的話）
       -> 可以用來快速判斷「有沒有相交」

    2. 如果從「尾端對齊」往前走，
       交點就是「第一個相同的節點」
       -> 但單向串列不能往前走 ✘

       所以改成「從頭端對齊」：
       讓長的那條先走 |la - lb| 步（解法二）

【本題的三種解法】：

    (a) 雜湊集合：記住 A 的所有節點，走 B 找第一個重複的
        O(m+n) 時間、O(m) 空間

    (b) 先算長度，對齊後同步走
        O(m+n) 時間、O(1) 空間 ✔

    (c) 【換軌道】：走到底就跳到對方的頭
        O(m+n) 時間、O(1) 空間 ✔ 而且只有五行"""),
   ]),
 ],
 "examples": """範例 1
  輸入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5],
        skipA = 2, skipB = 3

        A: 4 -> 1 ↘
                   8 -> 4 -> 5
        B: 5 -> 6 -> 1 ↗

  輸出：值為 8 的那個節點
  說明：A 從交點往前數有 2 個節點，B 有 3 個。

範例 2
  輸入：listA = [2,6,4], listB = [1,5]，不相交
  輸出：null""",
 "constraints": [
   "<code>listA</code> 的節點數在 <code>[1, 3 × 10⁴]</code> 之間",
   "<code>listB</code> 的節點數在 <code>[1, 3 × 10⁴]</code> 之間",
   "1 ≤ <code>Node.val</code> ≤ 10⁵",
   "整個結構裡<strong>沒有環</strong>",
 ],
 "idea": [
   ("fig", _P160_FIG, "0 0 640 448"),
   ("c", """【換軌道法（解法一）】

    a, b = headA, headB
    while a is not b:
        a = a.next if a else headB      # 走到底就跳到 B 的頭
        b = b.next if b else headA      # 走到底就跳到 A 的頭
    return a

【★ 為什麼一定會相遇？】

    設：
        a = A 獨有部分的長度
        b = B 獨有部分的長度
        c = 共用尾巴的長度

    指標 A 的路徑：
        走完 A（a + c 步）-> 跳到 B 的頭 -> 走 b 步到交點
        總共 a + c + b 步

    指標 B 的路徑：
        走完 B（b + c 步）-> 跳到 A 的頭 -> 走 a 步到交點
        總共 b + c + a 步

    【完全相同！】所以它們在第 a+b+c 步時【同時】抵達交點 ✔

【★ 沒有交點的情況】

    c = 0（沒有共用部分）。

    指標 A 走 a + b 步之後變成 None
    指標 B 走 b + a 步之後變成 None

    【同時變成 None】-> a is b（都是 None）-> 迴圈結束 -> 回傳 None ✔

    【完全不用特判！】這是這個解法最漂亮的地方。

【★ 為什麼不能寫成 a = a.next.next 之類的？】

    每個指標每輪【恰好走一步】，這樣總步數才會相等。

    而且「走到底就換軌道」必須寫成
        a = a.next if a else headB

    不能寫成
        if a.next: a = a.next
        else: a = headB

    因為後者【永遠不會讓 a 變成 None】——
    沒有交點時就會無窮迴圈 ✘

    【必須讓指標「經過 None 這個狀態」，
      沒有交點的情況才會終止。】"""),
 ],
 "approaches": [
   ap("解法一", "換軌道（最短，五行）", [
     ("c", S["p160_switch"]),
     "<strong>五行，O(m+n) 時間、O(1) 空間。</strong>"
     "<strong>這是本題的經典答案。</strong>",
     ("h", "★ <code>a = a.next if a else headB</code> 的細節"),
     ("c", """這一行做了兩件事：
    a 還沒走到底 -> 往前一步
    a 已經是 None -> 跳到 headB

【★ 順序很重要：先檢查 a 是不是 None】

    寫成 a = a.next.next if ... 或
    「先判斷 a.next 是不是 None」都會出錯。

    正確的語意是：
        「這一輪，a 從目前位置往前一步；
          如果目前位置是 None（上一輪剛走完），
          就改成從 headB 開始。」

    這樣 a 會【經過 None 這個狀態】——
    而那正是「沒有交點時能終止」的關鍵。

【驗證「沒有交點」的情況】

    A = [1], B = [2]（不相交）

    起始：a=節點1, b=節點2
    輪 1：a is not b ✔
          a = 節點1.next = None
          b = 節點2.next = None
    輪 2：a is b（都是 None）-> 迴圈結束
    回傳 None ✔

    【兩步就結束，完全正確。】""",),
     ("h", "為什麼要先檢查 <code>not headA or not headB</code>？"),
     "<strong>題目保證兩條都至少有一個節點，所以其實不用。</strong>",
     "<strong>但如果允許空串列，<code>headB</code> 是 <code>None</code> 時 "
     "<code>a</code> 會在「跳到 <code>headB</code>」時卡住</strong> —— "
     "<strong>實際上它會變成 <code>None</code>，然後 <code>a is b</code> 成立，回傳 <code>None</code> ✔</strong>",
     "<strong>所以其實不特判也對，但寫了更明確。</strong>",
   ], "O(m + n)", "O(1)", "每個指標走 m+n 步", "兩個指標", optimal=True),

   ap("解法二", "先對齊長度再同步走（最直白）", [
     ("c", S["p160_len"]),
     ("c", """1. 分別算出兩條的長度 la、lb
2. 讓長的那條先走 |la - lb| 步
   -> 現在兩個指標「距離終點一樣遠」
3. 同步往前走，第一個相同的節點就是交點

【為什麼「距離終點一樣遠」就對了？】

    因為交點到終點的距離對兩條來說是一樣的（共用的尾巴）。

    對齊之後，如果有交點，
    兩個指標會【同時】抵達它 ✔

【那兩個 for 迴圈的技巧】

    for _ in range(la - lb): a = a.next
    for _ in range(lb - la): b = b.next

    la > lb 時，第一個跑 (la-lb) 次，第二個 range 是負的 -> 不跑 ✔
    la < lb 時，反過來 ✔
    相等時，兩個都不跑 ✔

    【用 range(負數) 自動變成空迴圈，
      省掉了 if la > lb ... else ... 的分支。】

    這是一個很實用的小技巧。

【這個解法比較好解釋】——
    「對齊起點」的直覺比「換軌道」自然得多。

    面試時可以先講這個，再說「還有一個更短的寫法」。""",),
     "<strong>O(m+n) 時間（三趟掃描）、O(1) 空間。</strong>",
   ], "O(m + n)", "O(1)", "三趟掃描", "幾個指標"),

   ap("解法三", "雜湊集合（最直白，但不滿足進階）", [
     ("c", S["p160_set"]),
     "<strong>O(m+n) 時間、O(m) 空間。</strong>",
     ("h", "★ 一定要存「節點物件」而不是 <code>val</code>"),
     ("c", """seen.add(headA)         ✔ 存節點
seen.add(headA.val)     ✘ 存值

    題目說值的範圍是 1 到 10^5，
    完全可能有【值相同但不是同一個節點】的情況。

    例如：
        A: 1 -> 2 -> 3
        B: 1 -> 4 -> 5      （不相交）

        存值的話，B 的第一個節點（值 1）
        會被誤判成交點 ✘

【Python 的物件預設可雜湊（用 id）】，
    所以直接 add(node) 就對了 ✔

    Java 的 HashSet<ListNode> 也一樣
    （用預設的 identity hash）。

【這個「存物件 vs 存值」的區別，
  在第 133、138、141 題都出現過】——

    只要題目說「同一個節點」而不是「值相同」，
    就必須用物件（或 id）當 key。""",),
     "<strong>面試時先寫這個，然後說「這是 O(m) 空間，我可以做到 O(1)」。</strong>",
   ], "O(m + n)", "O(m)", "每個節點一次", "雜湊集合"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "滿足進階"],
   [["一、換軌道", "O(m+n)", "O(1)", "5", "✔"],
    ["二、對齊長度", "O(m+n)", "O(1)", "16", "✔"],
    ["三、雜湊集合", "O(m+n)", "O(m)", "8", "✘"]]),
 "edges": [
   "<strong>不相交</strong> → <code>None</code>。"
   "<strong>換軌道法自然處理（兩人同時變 <code>None</code>），完全不用特判。</strong>",
   "<strong>交點就是 <code>headA</code></strong>（A 完全被包含在 B 裡）→ 回傳 <code>headA</code>。",
   "<strong>兩條完全相同</strong>（<code>headA is headB</code>）→ 迴圈一次都不跑，直接回傳 <code>headA</code>。",
   "<strong>兩條長度差很多</strong> → 解法二的對齊步驟要跑很多次，但仍是 O(m+n)。",
   "<strong>值相同但不是同一個節點</strong> → "
   "<strong>用 <code>==</code> 或存 <code>val</code> 會誤判。本題第一名的 bug。</strong>",
   "<strong>換軌道寫成「<code>if a.next: a = a.next else: a = headB</code>」</strong> → "
   "<strong>指標永遠不會是 <code>None</code>，不相交時無窮迴圈。</strong>",
   "<strong>3 × 10⁴ 個節點</strong> → 換軌道法最多走 6 萬步，輕鬆。",
 ],
 "follow": [
   ("h", "追問一：如果串列裡「可能有環」呢？"),
   "<strong>題目保證沒有環。如果有的話，問題會複雜很多</strong>：",
   ("ul", [
     "<strong>兩條都沒環</strong> → 本題的做法。",
     "<strong>一條有環、一條沒有</strong> → <strong>不可能相交</strong>"
     "（相交的話兩條都會進入那個環）。",
     "<strong>兩條都有環</strong> → 要判斷「是不是同一個環」："
     "先用第 142 題找出各自的環入口，如果入口相同 → 在環外相交（用本題的方法，"
     "把環入口當成「終點」）；如果不同 → 看能不能從一個入口繞到另一個，"
     "能的話就是「在環上相交」。",
   ]),
   "<strong>這是一個很經典的面試延伸問題，需要把第 141、142、160 三題組合起來。</strong>",
   ("h", "追問二：換軌道法能不能推廣到三條串列？"),
   ("c", """不能直接推廣。

    兩條的漂亮之處在於「a+b+c 對兩者相同」——
    三條的話，A 要走 a + c + b + c + ... 就對不齊了。

【三條的做法】：

    (a) 先求 A 和 B 的交點 X
    (b) 再求 X 和 C 的交點

    因為「相交」是可傳遞的（都是同一條尾巴）✔

    或者更直接：分別算三條的長度，
    對齊到「距離終點最短的那條」的起點，然後同步走。

【一般化的思路】：
    「對齊 + 同步走」可以推廣到任意條，
    「換軌道」只是兩條的特殊技巧。

    【漂亮的技巧常常不好推廣 ——
      這是選解法時要考慮的事。】""",),
   ("h", "追問三：為什麼「值相同」不算相交？"),
   ("c", """因為題目問的是【記憶體上的同一個物件】。

    這在真實程式裡是有意義的：

        兩個資料結構「共用」一段記憶體，
        改動其中一個會影響另一個。

    「值相同」則只是巧合 ——
    改動一個完全不影響另一個。

【這個區別在很多地方都重要】：

    Python：  is vs ==
    Java：    == vs .equals()
    C++：     指標比較 vs 值比較

    【面試時如果題目說「同一個節點」，
      一定要用 identity 比較。】

    而且要主動說出來 ——
    「我用 is 而不是 == 因為題目要的是同一個節點物件」
    會顯示你讀懂了題目。""",),
   ("h", "追問四：「不能修改串列」這個限制排除了什麼做法？"),
   ("c", """有一個很取巧的做法：

    把 A 的尾巴接到 A 的頭，變成一個環，
    然後用第 142 題的方法從 B 找環的入口 ——
    那就是交點 ✔

    O(m+n) 時間、O(1) 空間。

【但它【修改了串列】】——
    雖然可以在最後還原，但：
        ✘ 過程中資料是壞的（多執行緒不安全）
        ✘ 如果中途拋出例外，串列就永遠壞了
        ✘ 題目明確禁止

【換軌道法達到同樣的複雜度，而且完全不修改】——
    所以它嚴格優於那個取巧的做法。

    【「達到同樣效果但沒有副作用」的解法永遠更好。】""",),
 ],
 "related": [
   "<strong>第 141/142 題 環形鏈結串列 I/II</strong> —— 追問一和四會用到",
   "<strong>第 19 題 刪除倒數第 N 個節點</strong> —— 同樣的「先走 k 步再同步」",
   "<strong>第 876 題 Middle of the Linked List</strong> —— 雙指標的另一個用法",
 ],
 "check": [
   "「換軌道」法為什麼一定會相遇？請算出兩個指標各走幾步。",
   "沒有交點時，換軌道法為什麼會自動終止？",
   "為什麼要用 <code>is</code> 而不是 <code>==</code>？存 <code>val</code> 會在什麼測資上出錯？",
   "<code>for _ in range(la - lb)</code> 這個寫法省掉了什麼分支？",
 ],
})
print("P160 written")

# ==================== 162. Find Peak Element ====================
S["p162"] = '''class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid + 1]:
                lo = mid + 1        # 右邊在上坡 -> 右半一定有峰
            else:
                hi = mid            # mid 可能就是峰，不能丟掉

        return lo'''

S["p162_scan"] = '''class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(n)：第一個「比下一個大」的位置就是峰
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1        # 一路遞增 -> 最後一個是峰'''


def _is_peak(nums, i):
    n = len(nums)
    left = float("-inf") if i == 0 else nums[i - 1]
    right = float("-inf") if i == n - 1 else nums[i + 1]
    return left < nums[i] > right


_p162 = [S.load(k) for k in ("p162", "p162_scan")]

for nums in [[1, 2, 3, 1], [1, 2, 1, 3, 5, 6, 4], [1], [1, 2], [2, 1],
             [1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]:
    for sol in _p162:
        i = sol.findPeakElement(list(nums))
        assert 0 <= i < len(nums) and _is_peak(nums, i), ("P162", nums, i, sol)

for _ in range(6000):
    n = random.randrange(1, 14)
    # 題目保證 nums[i] != nums[i+1]
    nums = [random.randint(-20, 20)]
    while len(nums) < n:
        v = random.randint(-20, 20)
        if v != nums[-1]:
            nums.append(v)
    for sol in _p162:
        i = sol.findPeakElement(list(nums))
        assert 0 <= i < n and _is_peak(nums, i), ("P162 random", nums, i, sol)
print("P162 solutions OK")

_P162_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 陣列完全沒有排序，卻能二分搜尋 —— 因為「往高處走」一定能走到一個峰。</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">nums = [1, 2, 1, 3, 5, 6, 4]　　（兩端可以想成 −∞）</text>
            <g stroke="var(--border)" stroke-width="1"><line x1="50" y1="230" x2="570" y2="230"/></g>
            <g font-size="12" text-anchor="middle">
              <circle cx="90" cy="210" r="5" fill="var(--text-muted)"/><text x="90" y="250" fill="var(--text-muted)">1</text>
              <circle cx="160" cy="190" r="6" fill="#ff8a65"/><text x="160" y="250" fill="#ff8a65">2</text>
              <circle cx="230" cy="210" r="5" fill="var(--text-muted)"/><text x="230" y="250" fill="var(--text-muted)">1</text>
              <circle cx="300" cy="170" r="5" fill="var(--text-muted)"/><text x="300" y="250" fill="var(--text-muted)">3</text>
              <circle cx="370" cy="130" r="5" fill="var(--text-muted)"/><text x="370" y="250" fill="var(--text-muted)">5</text>
              <circle cx="440" cy="110" r="7" fill="var(--gold)"/><text x="440" y="250" fill="var(--gold)">6</text>
              <circle cx="510" cy="150" r="5" fill="var(--text-muted)"/><text x="510" y="250" fill="var(--text-muted)">4</text>
            </g>
            <polyline points="90,210 160,190 230,210 300,170 370,130 440,110 510,150" fill="none" stroke="var(--border)" stroke-width="1.5"/>
            <text x="160" y="172" fill="#ff8a65" font-size="11" text-anchor="middle">峰 ✔</text>
            <text x="440" y="90" fill="var(--gold)" font-size="11" text-anchor="middle">峰 ✔</text>
            <text x="20" y="278" fill="var(--text-muted)" font-size="12">索引 1 和索引 5 都是合法答案 —— 題目說「回傳任何一個峰」即可。</text>
            <line x1="20" y1="300" x2="620" y2="300" stroke="var(--border)"/>
            <text x="20" y="328" fill="var(--accent)" font-size="13">★ 為什麼沒排序也能二分？</text>
            <text x="40" y="358" fill="var(--gold)" font-size="12">看 nums[mid] 和 nums[mid+1]：</text>
            <text x="60" y="386" fill="var(--accent)" font-size="12">nums[mid] &lt; nums[mid+1]（上坡）→ 右半【一定】有峰 → lo = mid + 1</text>
            <text x="60" y="412" fill="var(--accent)" font-size="12">nums[mid] &gt; nums[mid+1]（下坡）→ 左半（含 mid）【一定】有峰 → hi = mid</text>
            <text x="40" y="444" fill="var(--text-muted)" font-size="12">理由：從一個上坡的位置一路往右走，要嘛碰到下坡（那裡就是峰），</text>
            <text x="40" y="470" fill="var(--text-muted)" font-size="12">要嘛走到最右端（而右端外面是 −∞，所以它也是峰）。兩種情況都保證有峰 ✔</text>'''

emit({
 "num": 162, "slug": "find-peak-element",
 "en": [
   "A peak element is an element that is strictly greater than its neighbors.",
   "Given a <strong>0-indexed</strong> integer array <code>nums</code>, find a peak element, and "
   "return its index. If the array contains multiple peaks, return the index to "
   "<strong>any of the peaks</strong>.",
   "You may imagine that <code>nums[-1] = nums[n] = -∞</code>. In other words, an element is "
   "always considered to be strictly greater than a neighbor that is outside the array.",
   "You must write an algorithm that runs in <code>O(log n)</code> time.",
 ],
 "zh": [
   "「峰值」是指<strong>嚴格大於左右兩個鄰居</strong>的元素。",
   "給你一個整數陣列 <code>nums</code>，找出<strong>任何一個</strong>峰值，回傳它的索引。",
   "你可以把兩端外面想成 <code>nums[-1] = nums[n] = -∞</code> —— "
   "也就是說，<strong>陣列外面的鄰居永遠比較小</strong>。",
   "<strong>必須是 <code>O(log n)</code> 的演算法。</strong>",
 ],
 "pre": [
   ("note", "★ 這題最反直覺的地方：沒排序也能二分", [
     ("c", """一般人對二分搜尋的印象是「陣列要先排序」。

    但二分搜尋真正需要的只是：
        【能在 O(1) 內判斷「答案在哪一半」】

【這題怎麼判斷？】

    看 nums[mid] 和 nums[mid + 1]：

    情況 A：nums[mid] < nums[mid+1]（右邊在上坡）

        從 mid+1 開始往右走：
            如果一路上升到最後 -> 最後一個元素是峰
                （因為 nums[n] = -∞）✔
            如果中途開始下降 -> 那個轉折點是峰 ✔

        【右半一定有峰】-> lo = mid + 1

    情況 B：nums[mid] > nums[mid+1]（右邊在下坡）

        對稱地，從 mid 往左走一定能找到峰。
        （mid 自己也可能就是。）

        【左半（含 mid）一定有峰】-> hi = mid

    兩種情況都能砍掉一半 ✔

【★ 關鍵在於「一定有峰」這個保證】

    它來自兩個條件：
        (a) 陣列有限（不會無限上升）
        (b) 兩端外面是 -∞（邊界也可以是峰）

    少了 (b)，「一路遞增」的陣列就沒有峰了 ——
    那時二分就不成立。

【所以「nums[-1] = nums[n] = -∞」不是廢話】，
    它是這個演算法能成立的基石。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,1]
  輸出：2
  說明：nums[2] = 3 大於左邊的 2 和右邊的 1。

範例 2
  輸入：nums = [1,2,1,3,5,6,4]
  輸出：5（或 1）
  說明：索引 1（值 2）和索引 5（值 6）都是峰值，
        回傳任何一個都算對。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 1000",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
   "對所有有效的 <code>i</code>，<code>nums[i] != nums[i + 1]</code>"
   "（<strong>相鄰元素一定不相等</strong>）",
 ],
 "mid": [
   ("note", "★ 「相鄰元素不相等」這個條件很關鍵", [
     "<strong>它保證了「上坡」和「下坡」永遠能分清楚</strong> —— "
     "不會有「平地」讓你不知道往哪邊走。",
     "<strong>如果允許相等（例如 <code>[1,2,2,2,1]</code>），"
     "二分就會失效</strong> —— 和第 154 題的情況一模一樣。",
     "<strong>那時最壞情況會退化成 O(n)。</strong>",
   ]),
 ],
 "idea": [
   ("fig", _P162_FIG, "0 0 640 492"),
   ("c", """lo, hi = 0, n - 1
while lo < hi:
    mid = (lo + hi) // 2
    if nums[mid] < nums[mid + 1]:
        lo = mid + 1        # 上坡 -> 往右
    else:
        hi = mid            # 下坡 -> 往左（含 mid）
return lo

【★ 為什麼 mid + 1 不會越界？】

    while lo < hi 保證 lo < hi，
    而 mid = (lo + hi) // 2 -> mid < hi（因為是向下取整）

    所以 mid + 1 <= hi <= n - 1 ✔ 永遠安全

    【如果迴圈條件寫成 lo <= hi，mid 就可能等於 hi = n-1，
      mid + 1 就會越界 ✘】

    這是「收斂型二分」比「查找型二分」安全的一個例子。

【★ 不變量】

    「[lo, hi] 這個區間裡一定有一個峰值。」

    初始：[0, n-1] 涵蓋全部，而且「一定有峰」（見上面的論證）✔

    每一步：
        上坡 -> 右半一定有峰 -> [mid+1, hi] ✔
        下坡 -> 左半一定有峰 -> [lo, mid] ✔

    結束時 lo == hi，區間只剩一個元素 -> 它就是峰 ✔

【★ 為什麼不用檢查 nums[mid-1]？】

    很多人會想寫「三個條件」：

        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
            return mid
        elif ...

    那樣要處理 mid = 0 和 mid = n-1 的邊界，
    而且分支變多。

    【只比較 mid 和 mid+1 就夠了】——
    因為我們不需要「確認 mid 是不是峰」，
    只需要「決定往哪一半走」。

    最後收斂到單一元素時，它必然是峰（由不變量保證）✔

    【這是「收斂型二分」的思維：
      不要在中途判斷答案，讓區間自己收斂。】

【複雜度】：O(log n) 時間、O(1) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "二分搜尋（標準答案）", [
     ("c", S["p162"]),
     "<strong>八行，O(log n) 時間、O(1) 空間。</strong>",
     ("h", "手動走一遍 <code>[1,2,1,3,5,6,4]</code>"),
     ("c", """lo=0, hi=6
    mid=3: nums[3]=3 < nums[4]=5 ✔ 上坡 -> lo=4

lo=4, hi=6
    mid=5: nums[5]=6 < nums[6]=4? 否，下坡 -> hi=5

lo=4, hi=5
    mid=4: nums[4]=5 < nums[5]=6 ✔ 上坡 -> lo=5

lo=5 == hi -> 回傳 5

    驗證：nums[5] = 6 > nums[4] = 5 ✔ 且 > nums[6] = 4 ✔
    確實是峰 ✔

【注意它找到的是索引 5，不是索引 1】——
    兩個都是合法答案，二分的路徑決定它找到哪一個。

    【題目說「任何一個」，所以不用擔心。】

    如果題目要「最大的那個峰」，二分就不成立了 ——
    那要 O(n) 掃一遍。""",),
     ("h", "為什麼答案可能不唯一？"),
     ("c", """因為「峰」的定義是【局部】的 ——
只看左右兩個鄰居。

    [1,2,1,3,5,6,4] 有兩個局部最大值。

    二分會找到「其中一個」，
    但【無法保證是哪一個】——
    它取決於 mid 的計算方式。

【這也是為什麼題目要說「回傳任何一個」】：

    如果要求「全域最大」，就必須看過每個元素 -> O(n)

    【「局部最優」可以二分，「全域最優」不行】——

    這個區別在很多問題裡都出現：
        找任一峰值     -> O(log n)
        找最大值       -> O(n)
        找任一逆序對   -> O(n)
        找所有逆序對   -> O(n log n)""",),
   ], "O(log n)", "O(1)", "每次砍一半", "兩個索引", optimal=True),

   ap("解法二", "線性掃描（O(n)，但值得看）", [
     ("c", S["p162_scan"]),
     ("c", """「找第一個【比下一個大】的位置」。

    for i in range(n - 1):
        if nums[i] > nums[i+1]:
            return i
    return n - 1

【為什麼這樣一定對？】

    如果在位置 i 第一次「開始下降」，
    那代表 nums[0] < nums[1] < ... < nums[i]（一路上升）
    而且 nums[i] > nums[i+1]

    -> nums[i] 比左右都大 -> 是峰 ✔

    如果從來沒有下降，代表一路遞增 ->
    最後一個元素比左邊大，而右邊是 -∞ -> 是峰 ✔

【它會找到「最左邊的峰」】。

【這個解法不滿足題目的 O(log n) 要求】，
    但它有兩個價值：

    1. 【它是二分解法的「直覺版本」】——
       二分其實就是「用跳躍的方式找第一個下降點」。

    2. 【它是驗證二分的最好工具】——
       本文的測試用 _is_peak 驗證任何回傳的索引，
       兩個解法都要通過。

【n <= 1000 時，O(n) 其實完全夠快】。

    題目要求 O(log n)，純粹是為了考「沒排序也能二分」這個觀念。""",),
   ], "O(n)", "O(1)", "掃一遍", "不用額外空間"),
 ],
 "compare": (["解法", "時間", "空間", "找到哪個峰", "符合要求"],
   [["一、二分搜尋", "O(log n)", "O(1)", "不確定", "✔"],
    ["二、線性掃描", "O(n)", "O(1)", "最左邊的", "✘"]]),
 "edges": [
   "<strong>單一元素</strong> <code>[1]</code> → <code>0</code>（兩邊都是 −∞）。"
   "<strong>迴圈一次都不跑。</strong>",
   "<strong>兩個元素</strong> <code>[1,2]</code> → <code>1</code>；<code>[2,1]</code> → <code>0</code>。",
   "<strong>一路遞增</strong> <code>[1,2,3,4,5]</code> → <code>4</code>（最後一個）。",
   "<strong>一路遞減</strong> <code>[5,4,3,2,1]</code> → <code>0</code>（第一個）。",
   "<strong>多個峰</strong> → 回傳任何一個都對，<strong>判題器會驗證「它確實是峰」</strong>。",
   "<strong>迴圈條件寫成 <code>lo &lt;= hi</code></strong> → "
   "<strong><code>mid + 1</code> 可能越界，而且會無窮迴圈。</strong>",
   "<strong><code>hi = mid - 1</code></strong> → <strong>可能丟掉唯一的峰。</strong>",
   "<strong>比較 <code>nums[mid]</code> 和 <code>nums[mid-1]</code></strong> → "
   "<code>mid = 0</code> 時越界（負索引在 Python 裡不會報錯，但會拿到最後一個元素 —— 更糟）。",
 ],
 "follow": [
   ("h", "追問一：如果相鄰元素可以相等呢？"),
   ("c", """二分就失效了 —— 和第 154 題一樣的問題。

    nums[mid] == nums[mid+1] 時，無法判斷往哪走：

        [1, 2, 2, 2, 1]     峰在中間某處
        [2, 2, 2, 2, 1]     峰在最左邊

        在 mid 和 mid+1 的位置上長得一樣，
        但答案在相反方向 ✘

【只能退回 O(n) 的線性掃描】，
    或者用「相等時兩邊都試」的分治（最壞仍是 O(n)）。

【所以「相鄰元素不相等」這個條件，
  和第 153 題的「元素互不相同」扮演同樣的角色】——

    它保證了「比較永遠能提供資訊」。

    讀題時看到這種條件，要意識到：
    「它可能是某個 O(log n) 演算法的前提」。""",),
   ("h", "追問二：如果是二維的「峰值」呢？"),
   "<strong>第 1901 題（尋找峰值 II）</strong>。"
   "<strong>可以做到 O(m log n)</strong>：",
   ("c", """對【每一欄】做二分：

    1. 取中間那一欄 mid
    2. 找出那一欄的最大值所在的列 r
    3. 比較 matrix[r][mid] 和左右兩欄的鄰居：
           比左邊小 -> 峰在左半
           比右邊小 -> 峰在右半
           都比較大 -> 它就是峰 ✔

    每次砍掉一半的欄 -> O(log n) 輪
    每輪要找一欄的最大值 -> O(m)

    總共 O(m log n) ✔

【為什麼「那一欄的最大值」是好的候選？】

    因為它在【垂直方向】上已經是最大的了 ——
    只要它在【水平方向】上也是最大的，就是峰。

    如果不是，就往「比較大的那一邊」走 ——
    那一邊一定有峰（和一維的論證相同）。

【這個推廣很漂亮】：
    「在一個維度上取最大，在另一個維度上二分」。""",),
   ("h", "追問三：這個「沒排序也能二分」的觀念還能用在哪？"),
   ("ul", [
     "<strong>第 153/154 題</strong>：旋轉排序陣列（兩段各自有序）",
     "<strong>第 852 題 山脈陣列的峰頂</strong>：先升後降，二分找轉折",
     "<strong>第 875 題 愛吃香蕉的珂珂</strong>：對「答案」二分",
     "<strong>第 410 題 分割陣列的最大值</strong>：同上",
     "<strong>第 4 題 兩個有序陣列的中位數</strong>：對「分割點」二分",
   ]),
   ("c", """【共同條件】：

    存在一個【單調的判定函式】check(x)：
        x < 答案 -> False
        x >= 答案 -> True

    就能二分。

【這題的 check 是什麼？】

    check(i) = 「[i, n-1] 這個區間裡有峰」

    嚴格來說它不是單調的（整個陣列都有峰），
    但我們用的是另一個形式：

    「nums[i] < nums[i+1]」這個判定
    告訴我們「峰在右邊」——

    而所有「第一個下降點」之前的位置都滿足它，
    之後都不滿足 -> 【是單調的】✔

    二分找的就是那個分界點。

【把問題轉化成「找一個單調判定的分界點」，
  是使用二分搜尋的通用方法。】""",),
   ("h", "追問四：為什麼題目說「回傳任何一個」而不是「最大的」？"),
   "<strong>因為「找全域最大」必須看過每個元素 —— 一定是 O(n)。</strong>",
   "<strong>如果題目要最大值，就不可能有 O(log n) 的解</strong>"
   "（任何沒看過的位置都可能藏著更大的值）。",
   "<strong>「回傳任何一個峰」這個放寬，正是 O(log n) 能成立的原因</strong> —— "
   "<strong>題目的每一個字都是設計過的。</strong>",
 ],
 "related": [
   "<strong>第 153/154 題 旋轉排序陣列的最小值</strong> —— 同樣是「非全序也能二分」",
   "<strong>第 852 題 Peak Index in a Mountain Array</strong> —— 保證只有一個峰",
   "<strong>第 1901 題 Find a Peak Element II</strong> —— 二維版",
   "<strong>第 33 題 Search in Rotated Sorted Array</strong> —— 另一個變形二分",
 ],
 "check": [
   "為什麼「沒有排序」也能二分？判斷「往哪一半走」的依據是什麼？",
   "「兩端外面是 −∞」這個條件為什麼是演算法成立的基石？",
   "為什麼只比較 <code>nums[mid]</code> 和 <code>nums[mid+1]</code> 就夠，不用看 <code>mid-1</code>？",
   "如果相鄰元素可以相等，這個演算法為什麼會失效？",
 ],
})
print("P162 written")

# ==================== 164. Maximum Gap ====================
S["p164_bucket"] = '''class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        lo, hi = min(nums), max(nums)
        if lo == hi:
            return 0                        # 全部相同

        # 桶的大小：讓「同一個桶內的差」一定小於答案
        size = max(1, (hi - lo) // (n - 1))
        cnt = (hi - lo) // size + 1

        # 每個桶只記錄「桶內的最小值和最大值」
        bmin = [None] * cnt
        bmax = [None] * cnt
        for x in nums:
            k = (x - lo) // size
            bmin[k] = x if bmin[k] is None else min(bmin[k], x)
            bmax[k] = x if bmax[k] is None else max(bmax[k], x)

        # 答案只可能出現在「相鄰兩個非空桶」之間
        best, prev = 0, None
        for k in range(cnt):
            if bmin[k] is None:
                continue                    # 空桶跳過
            if prev is not None:
                best = max(best, bmin[k] - prev)
            prev = bmax[k]

        return best'''

S["p164_sort"] = '''class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()                         # O(n log n)，不滿足進階要求
        return max(b - a for a, b in zip(nums, nums[1:]))'''

S["p164_radix"] = '''class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        # 基數排序：一次處理 8 個位元，跑 4 輪（32 位元整數）
        a = list(nums)
        buf = [0] * n
        for shift in (0, 8, 16, 24):
            cnt = [0] * 256
            for x in a:
                cnt[(x >> shift) & 255] += 1
            for i in range(1, 256):
                cnt[i] += cnt[i - 1]        # 前綴和 -> 每個桶的結束位置
            for x in reversed(a):           # 倒著走才穩定
                cnt[(x >> shift) & 255] -= 1
                buf[cnt[(x >> shift) & 255]] = x
            a, buf = buf, a

        return max(b - c for c, b in zip(a, a[1:]))'''


def _p164_ref(nums):
    if len(nums) < 2:
        return 0
    a = sorted(nums)
    return max(b - c for c, b in zip(a, a[1:]))


_p164 = [S.load(k) for k in ("p164_bucket", "p164_sort", "p164_radix")]

for nums, want in [
    ([3, 6, 9, 1], 3),
    ([10], 0),
    ([1, 1, 1], 0),
    ([1, 10000000], 9999999),
    ([1, 3, 100], 97),
    ([], 0),
]:
    assert _p164_ref(nums) == want, ("P164 ref", nums)
    for sol in _p164:
        assert sol.maximumGap(list(nums)) == want, ("P164", nums, want, sol)

for _ in range(4000):
    n = random.randrange(0, 15)
    nums = [random.randint(0, 60) for _ in range(n)]
    want = _p164_ref(nums)
    for sol in _p164:
        assert sol.maximumGap(list(nums)) == want, ("P164 random", nums, want, sol)
for _ in range(600):
    n = random.randrange(2, 40)
    nums = [random.randint(0, 10 ** 8) for _ in range(n)]
    want = _p164_ref(nums)
    for sol in _p164:
        assert sol.maximumGap(list(nums)) == want, ("P164 big", want, sol)
print("P164 solutions OK")

_P164_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 鴿籠原理：把 n 個數丟進「間距 &lt; 平均間距」的桶裡，答案一定跨在【兩個桶之間】。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">nums = [1, 3, 9, 20]　n = 4，min = 1、max = 20</text>
            <text x="20" y="80" fill="var(--text-muted)" font-size="12">桶的大小 = (20 − 1) / (4 − 1) = 6（取下整）　→　桶數 = (20 − 1) / 6 + 1 = 4</text>
            <g font-size="12" text-anchor="middle">
              <rect x="60" y="100" width="120" height="50" fill="none" stroke="var(--accent)"/><text x="120" y="120" fill="var(--accent)">桶 0：[1, 7)</text><text x="120" y="140" fill="var(--gold)">1, 3</text>
              <rect x="180" y="100" width="120" height="50" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/><text x="240" y="120" fill="var(--text-muted)">桶 1：[7, 13)</text><text x="240" y="140" fill="var(--gold)">9</text>
              <rect x="300" y="100" width="120" height="50" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/><text x="360" y="120" fill="var(--text-muted)">桶 2：[13, 19)</text><text x="360" y="140" fill="var(--text-muted)">（空）</text>
              <rect x="420" y="100" width="120" height="50" fill="none" stroke="var(--accent)"/><text x="480" y="120" fill="var(--accent)">桶 3：[19, 25)</text><text x="480" y="140" fill="var(--gold)">20</text>
            </g>
            <text x="20" y="182" fill="var(--text-muted)" font-size="12">相鄰非空桶之間的差：9 − 3 = 6　　20 − 9 = 11　→　答案 = 11 ✔</text>
            <line x1="20" y1="206" x2="620" y2="206" stroke="var(--border)"/>
            <text x="20" y="234" fill="var(--accent)" font-size="13">★ 為什麼「答案一定跨桶」？</text>
            <text x="40" y="264" fill="var(--text-muted)" font-size="12">n 個數分布在 [min, max] 之間，共有 n − 1 個間隙。</text>
            <text x="40" y="290" fill="var(--gold)" font-size="12">所以【最大間隙 ≥ 平均間隙 = (max − min) / (n − 1)】—— 這就是鴿籠原理。</text>
            <text x="40" y="320" fill="var(--text-muted)" font-size="12">而我們把桶的大小設成「平均間隙（取下整）」，所以：</text>
            <text x="60" y="348" fill="var(--accent)" font-size="12">同一個桶裡的兩個數，差 &lt; 桶大小 ≤ 最大間隙</text>
            <text x="60" y="374" fill="var(--gold)" font-size="12">→ 最大間隙【不可能】在同一個桶裡 → 一定跨桶 ✔</text>
            <text x="20" y="408" fill="#ff8a65" font-size="12">★ 所以每個桶只要記「桶內的最小值和最大值」就夠 —— 桶裡其他的數完全不用管。</text>
            <text x="20" y="434" fill="var(--text-muted)" font-size="12">這讓空間從「存所有數」降到 O(桶數) = O(n)，而且不用排序 → 總共 O(n) ✔</text>'''

emit({
 "num": 164, "slug": "maximum-gap",
 "en": [
   "Given an integer array <code>nums</code>, return <em>the maximum difference between two "
   "successive elements in its sorted form</em>. If the array contains less than two elements, "
   "return <code>0</code>.",
   "You must write an algorithm that runs in linear time and uses linear extra space.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，"
   "把它排序之後，找出<strong>相鄰兩個元素的最大差值</strong>。",
   "如果陣列少於兩個元素，回傳 <code>0</code>。",
   "<strong>必須是線性時間、線性額外空間的演算法。</strong>",
 ],
 "pre": [
   ("note", "★ 「線性時間」把排序排除了", [
     ("c", """最直覺的做法：排序、掃一遍相鄰差。

    nums.sort()
    return max(b - a for a, b in zip(nums, nums[1:]))

    兩行，O(n log n) ——【能通過 LeetCode】。

    但題目明確要求【線性時間】。

【怎麼可能不排序就知道「排序後的相鄰差」？】

    關鍵洞察：【我們不需要完整的排序】。

    答案是「最大的間隙」——
    而最大的間隙一定【比平均間隙大】（鴿籠原理）。

    所以：
        把數值範圍切成「寬度 < 平均間隙」的桶，
        那麼【同一個桶裡的兩個數，它們的差一定小於答案】
        -> 答案一定跨在【兩個桶之間】✔

    於是每個桶只要記「最小值」和「最大值」就夠 ——
    桶內的其他數完全不影響答案。

【這就是「桶排序」思想的精髓】：

    不是「把東西排好」，
    而是「把東西分組，讓我們只需要看組與組之間」。

【另一條路：基數排序】（解法三）

    O(d·n) 時間，d 是位數（32 位元整數下 d = 4，如果一次處理 8 位）。

    它真的把陣列排序了，但不用比較 -> 突破了 O(n log n) 的下界。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [3,6,9,1]
  輸出：3
  說明：排序後是 [1,3,6,9]，相鄰差是 2, 3, 3，最大是 3。

範例 2
  輸入：nums = [10]
  輸出：0
  說明：少於兩個元素。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "0 ≤ <code>nums[i]</code> ≤ 10⁹",
 ],
 "idea": [
   ("fig", _P164_FIG, "0 0 640 456"),
   ("c", """【鴿籠原理（pigeonhole principle）】

    n 個數分布在 [min, max] 之間，
    排序後有 n - 1 個間隙，總和是 max - min。

    所以【最大間隙 >= (max - min) / (n - 1)】

    （因為「最大值 >= 平均值」。）

【桶的設計】

    size = max(1, (max - min) // (n - 1))    ← 桶的寬度
    cnt  = (max - min) // size + 1           ← 桶的數量

    把 x 放進桶 (x - min) // size。

    【同一個桶裡的兩個數，差最多是 size - 1 < size <= 最大間隙】

    -> 最大間隙【不可能】發生在同一個桶內 ✔
    -> 它一定是「某個桶的最大值」到「下一個非空桶的最小值」

【所以每個桶只要記兩個數】：

    bmin[k]、bmax[k]

    其他的數完全不用管 -> 空間 O(桶數) = O(n) ✔

【掃描時要跳過空桶】

    prev = 上一個非空桶的最大值
    for 每個非空桶 k:
        best = max(best, bmin[k] - prev)
        prev = bmax[k]

【★ 為什麼 size 要 max(1, ...)？】

    如果 max - min < n - 1（數字很密集），
    (max-min)//(n-1) 會是 0 -> 除以零 ✘

    設成 1 的話，每個桶剛好裝一個數值 ——
    這時「桶」退化成「計數陣列」，但演算法仍然正確 ✔

【複雜度】：O(n) 時間、O(n) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "桶 + 鴿籠原理（標準答案）", [
     ("c", S["p164_bucket"]),
     "<strong>O(n) 時間、O(n) 空間。</strong>"
     "<strong>這是題目要的答案。</strong>",
     ("h", "★ 為什麼「同桶內的差」一定小於答案？"),
     ("c", """設 g = 最大間隙，size = (max-min) // (n-1)。

    由鴿籠原理：g >= (max-min) / (n-1) >= size

    （第二個 >= 是因為 size 是向下取整。）

    同一個桶的寬度是 size，
    所以桶內兩個數的差【最多是 size - 1】。

    size - 1 < size <= g

    -> 桶內的差【嚴格小於】最大間隙 ✔

    -> 最大間隙必然跨桶 ✔

【★ 一個容易忽略的邊界】

    如果 size = 1（數字很密集），
    桶內只能有【相同的數】（差是 0）——
    仍然滿足「桶內差 < g」（除非 g = 0，那時全部相同，答案就是 0 ✔）。

    所以 max(1, ...) 這個保護不只是防除零，
    它在邏輯上也是正確的。

【★ 為什麼不用擔心「桶太多」？】

    cnt = (max-min) // size + 1
        <= (max-min) // ((max-min)//(n-1)) + 1
        ≈ n

    所以桶數是 O(n) ✔

    （size = 1 時 cnt = max-min+1，
      但那只在 max-min < n 時發生，所以 cnt < n + 1 ✔）""",),
     ("h", "為什麼要特判 <code>lo == hi</code>？"),
     "<strong>全部相同時 <code>max - min = 0</code>，"
     "<code>size = max(1, 0) = 1</code>，<code>cnt = 1</code></strong> —— "
     "<strong>只有一個桶，掃描時 <code>prev</code> 一直是 <code>None</code>，回傳 0 ✔</strong>",
     "<strong>所以其實不特判也對，但寫了更清楚（而且省掉一趟）。</strong>",
   ], "O(n)", "O(n)", "分桶 + 掃桶", "兩個桶陣列", optimal=True),

   ap("解法二", "排序（O(n log n)，不滿足要求但最短）", [
     ("c", S["p164_sort"]),
     "<strong>兩行。實測通常最快（Timsort 是 C 實作的）。</strong>",
     ("c", """【它能通過 LeetCode，但不是題目要的答案。】

    面試時寫這個，面試官一定會說
    「現在做到線性時間」。

【zip(nums, nums[1:]) 這個寫法】

    產生相鄰的配對：(a0,a1), (a1,a2), ...

    比 for i in range(len(nums)-1) 好讀很多，
    是 Python 處理「相鄰元素」的慣用法。

    （和第 114、118 題用的是同一招。）

【什麼時候「不滿足要求但最短」的解法是對的？】

    ✔ 真實工作（除非有效能瓶頸，用內建排序永遠對）
    ✔ 先確保有一個正確答案，再優化

    ✘ 題目明確要求線性時間（本題）

    【但一定要先寫出它】——
    它是驗證線性解法的參考實作。""",),
   ], "O(n log n)", "O(1) 或 O(n)", "排序主導", "視排序實作而定"),

   ap("解法三", "基數排序（真的線性，但常數大）", [
     ("c", S["p164_radix"]),
     ("h", "★ 基數排序：不用比較的排序"),
     ("c", """比較排序的下界是 Ω(n log n)
（因為 n! 種排列需要 log(n!) = Ω(n log n) 次比較來區分）。

【基數排序不用比較，所以能突破這個下界】：

    它按「每一位數」分組，從低位到高位，
    每一輪都用【穩定的】計數排序。

    做完所有位數之後，整個陣列就排好了 ✔

【為什麼「從低位到高位」而且必須穩定？】

    最後一輪（最高位）決定主要順序。
    而「最高位相同」的元素，它們的相對順序
    是【前一輪（次高位）排好的】——

    只有【穩定排序】才能保留這個順序 ✔

    這就是為什麼那個迴圈要 for x in reversed(a)：
        cnt 是「結束位置」，從後往前填才穩定。

【複雜度】

    每輪 O(n + 256)，共 4 輪（32 位元，每次 8 位）
    -> O(4(n + 256)) = O(n) ✔

    空間 O(n + 256) = O(n) ✔

【實務上快嗎？】

    在 Python 裡【比內建 sort 慢很多】——
    因為那是純 Python 迴圈，而 sort 是 C。

    在 C/C++ 裡，對大量整數，基數排序確實比快排快。

【基數排序的限制】：
    ✘ 只能排「能拆成固定位數」的東西（整數、固定長度字串）
    ✘ 需要 O(n) 額外空間
    ✘ 對浮點數、自訂物件不適用（除非能編碼成整數）

【這題用桶的解法（解法一）更貼近題目的精神】——
    它根本不排序，只是「分組」。""",),
   ], "O(d·n)", "O(n)", "d = 4 輪", "輔助陣列 + 計數"),
 ],
 "compare": (["解法", "時間", "空間", "符合要求", "實測速度（Python）"],
   [["一、桶 + 鴿籠", "O(n)", "O(n)", "✔", "中"],
    ["二、排序", "O(n log n)", "O(n)", "✘", "最快"],
    ["三、基數排序", "O(d·n)", "O(n)", "✔", "最慢（純 Python 迴圈）"]]),
 "edges": [
   "<strong>少於兩個元素</strong> → <code>0</code>。",
   "<strong>全部相同</strong> <code>[1,1,1]</code> → <code>0</code>。"
   "<strong><code>max - min = 0</code>，要防除零。</strong>",
   "<strong>兩個元素</strong> <code>[1, 10000000]</code> → <code>9999999</code>。"
   "<strong><code>n - 1 = 1</code>，<code>size</code> 就是整個範圍。</strong>",
   "<strong>數字很密集</strong>（<code>max - min &lt; n - 1</code>）→ "
   "<strong><code>size</code> 會是 0，必須用 <code>max(1, ...)</code> 保護。</strong>",
   "<strong>有空桶</strong> → <strong>掃描時一定要跳過，否則 <code>bmin[k]</code> 是 "
   "<code>None</code> 會 crash。</strong>",
   "<strong>數值到 10⁹</strong> → 不能開「值域大小」的桶陣列（10⁹ 個格子）；"
   "<strong>桶數是 O(n) 才可行。</strong>",
   "<strong>10⁵ 個元素</strong> → O(n log n) 其實也只要 170 萬次，實測會過。",
 ],
 "follow": [
   ("h", "追問一：鴿籠原理還能用在哪些題目？"),
   ("ul", [
     "<strong>第 287 題 尋找重複數</strong>：n+1 個數在 1..n 裡 → 一定有重複",
     "<strong>第 268 題 缺失的數字</strong>：同一類的計數論證",
     "<strong>第 41 題 第一個缺失的正數</strong>：答案一定在 1..n+1 之間",
     "<strong>生日悖論</strong>：23 個人就有 50% 機率同天生日",
     "<strong>雜湊碰撞必然存在</strong>：輸入空間比輸出空間大",
   ]),
   ("c", """【鴿籠原理的標準形式】：

    把 n 個物品放進 m 個盒子，如果 n > m，
    那至少有一個盒子裝了 2 個以上。

【本題用的是「平均版」】：

    n 個數的總和是 S，那至少有一個數 >= S/n。

    這裡：n-1 個間隙的總和是 max-min，
    所以至少有一個間隙 >= (max-min)/(n-1) ✔

【辨認訊號】：

    「一定存在某個東西滿足某個下界」
    而且那個下界是「總量 / 數量」——
    八成就是鴿籠原理。

    它常常能把「需要精確計算」的問題
    變成「只要分組就好」。""",),
   ("h", "追問二：為什麼比較排序有 Ω(n log n) 的下界？"),
   ("c", """【決策樹論證】：

    任何「只靠比較」的排序演算法，
    可以畫成一棵【二元決策樹】：
        每個內部節點是一次比較（兩個結果）
        每個葉節點是一種可能的排列

    n 個元素有 n! 種排列 -> 至少要 n! 個葉節點

    一棵高度 h 的二元樹最多有 2^h 個葉節點

        2^h >= n!
        h >= log₂(n!)
          ≈ n log₂ n - n log₂ e     （史特林近似）
          = Ω(n log n) ✔

【所以任何比較排序，最壞情況至少要 n log n 次比較。】

【基數排序、計數排序、桶排序怎麼繞過？】

    它們【不比較元素】——
    而是直接用「值本身」當索引。

    代價：
        ✘ 只適用於「值可以當索引」的資料（整數、固定長度字串）
        ✘ 複雜度依賴值域大小或位數

    【下界只對「比較模型」成立 ——
      換一個計算模型，下界就不一樣了。】

    這是理論計算機科學很重要的一課。""",),
   ("h", "追問三：桶的大小可以設成別的值嗎？"),
   ("c", """可以，只要滿足【桶寬 <= 最大間隙】。

    常見的選擇：
        size = (max-min) // (n-1)        本文用的（最精確）
        size = (max-min) // n + 1        也常見
        size = ceil((max-min) / (n-1))   ✘ 【這個不行！】

【為什麼向上取整不行？】

    如果 size > 最大間隙，
    那麼最大間隙就【可能發生在同一個桶內】——
    我們就會漏掉它 ✘

    例如 nums = [1, 2, 10]：
        max-min = 9, n-1 = 2
        向下取整：size = 4 -> 桶 [1,5), [5,9), [9,13)
                  1,2 在桶 0；10 在桶 2
                  答案 = 10 - 2 = 8 ✔
        向上取整：size = 5 -> 桶 [1,6), [6,11)
                  1,2 在桶 0；10 在桶 1
                  答案 = 10 - 2 = 8 ✔ 剛好也對

    這個例子看不出差別，但一般情況下向上取整會有風險。

【安全的原則：桶寬要【不大於】平均間隙】。

    向下取整保證了這一點 ✔""",),
   ("h", "追問四：這題在真實世界有什麼對應？"),
   "<strong>「找出資料裡最大的空隙」是異常偵測和分群的基本操作</strong> —— "
   "<strong>例如「把數值分成兩群，切在最大的空隙處」（Jenks natural breaks 的一維特例）。</strong>",
   "<strong>而「用桶而不是排序」的思路，在處理大量資料時很重要</strong> —— "
   "<strong>例如計算近似分位數（t-digest、HdrHistogram）時，"
   "也是「分桶 + 只記桶的統計量」，而不是存下所有資料。</strong>",
 ],
 "related": [
   "<strong>第 287 題 Find the Duplicate Number</strong> —— 另一個鴿籠原理的應用",
   "<strong>第 41 題 First Missing Positive</strong> —— 值域受限的原地技巧",
   "<strong>第 912 題 Sort an Array</strong> —— 各種排序演算法的練習場",
   "<strong>第 220 題 存在重複元素 III</strong> —— 同樣用「桶」的思路",
 ],
 "check": [
   "鴿籠原理在這題說了什麼？為什麼「最大間隙 ≥ 平均間隙」？",
   "為什麼「同一個桶內的差」一定小於答案？",
   "<code>size</code> 為什麼要 <code>max(1, ...)</code>？向上取整為什麼有風險？",
   "為什麼基數排序能突破 O(n log n) 的下界？它的代價是什麼？",
 ],
})
print("P164 written")

# ==================== 165. Compare Version Numbers ====================
S["p165_split"] = '''class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a = version1.split(".")
        b = version2.split(".")

        # 短的那邊補 0（"1.0" 和 "1" 是相等的）
        for i in range(max(len(a), len(b))):
            x = int(a[i]) if i < len(a) else 0
            y = int(b[i]) if i < len(b) else 0
            if x != y:
                return 1 if x > y else -1

        return 0'''

S["p165_zip"] = '''from itertools import zip_longest

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for x, y in zip_longest(version1.split("."), version2.split("."),
                                fillvalue="0"):
            x, y = int(x), int(y)
            if x != y:
                return 1 if x > y else -1
        return 0'''

S["p165_two"] = '''class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        i, j = 0, 0
        m, n = len(version1), len(version2)

        while i < m or j < n:
            # 邊走邊把這一段的數字算出來（不切割字串 -> O(1) 額外空間）
            x = 0
            while i < m and version1[i] != ".":
                x = x * 10 + int(version1[i])
                i += 1
            y = 0
            while j < n and version2[j] != ".":
                y = y * 10 + int(version2[j])
                j += 1

            if x != y:
                return 1 if x > y else -1

            i += 1          # 跳過 "."（走到底時 i 會超出範圍，但迴圈條件會擋）
            j += 1

        return 0'''


def _p165_ref(v1, v2):
    a = [int(x) for x in v1.split(".")]
    b = [int(x) for x in v2.split(".")]
    n = max(len(a), len(b))
    a += [0] * (n - len(a))
    b += [0] * (n - len(b))
    return (a > b) - (a < b)


_p165 = [S.load(k) for k in ("p165_split", "p165_zip", "p165_two")]

for v1, v2, want in [
    ("1.2", "1.10", -1),
    ("1.01", "1.001", 0),
    ("1.0", "1.0.0.0", 0),
    ("1", "1.1", -1),
    ("0.1", "1.1", -1),
    ("1.0.1", "1", 1),
    ("7.5.2.4", "7.5.3", -1),
    ("1.0.0", "1", 0),
]:
    assert _p165_ref(v1, v2) == want, ("P165 ref", v1, v2, _p165_ref(v1, v2))
    for sol in _p165:
        assert sol.compareVersion(v1, v2) == want, ("P165", v1, v2, want, sol)


def _rand_ver():
    k = random.randrange(1, 5)
    parts = []
    for _ in range(k):
        v = random.randrange(0, 12)
        s = str(v)
        if random.random() < 0.3:
            s = "0" * random.randrange(1, 3) + s     # 隨機加前導零
        parts.append(s)
    return ".".join(parts)


for _ in range(8000):
    v1, v2 = _rand_ver(), _rand_ver()
    want = _p165_ref(v1, v2)
    for sol in _p165:
        assert sol.compareVersion(v1, v2) == want, ("P165 random", v1, v2, want, sol)
print("P165 solutions OK")

emit({
 "num": 165, "slug": "compare-version-numbers",
 "en": [
   "Given two <strong>version strings</strong>, <code>version1</code> and <code>version2</code>, "
   "compare them. A version string consists of <strong>revisions</strong> separated by dots "
   "<code>'.'</code>. The <strong>value of the revision</strong> is its "
   "<strong>integer conversion</strong> ignoring leading zeros.",
   "To compare version strings, compare their revision values in "
   "<strong>left-to-right order</strong>. If one of the version strings has fewer revisions, "
   "treat the missing revision values as <code>0</code>.",
   "Return the following:",
   ("raw", "<ul><li>If <code>version1 &lt; version2</code>, return <code>-1</code>.</li>"
           "<li>If <code>version1 &gt; version2</code>, return <code>1</code>.</li>"
           "<li>Otherwise, return <code>0</code>.</li></ul>"),
 ],
 "zh": [
   "給你兩個<strong>版本號字串</strong> <code>version1</code> 和 <code>version2</code>，比較它們的大小。",
   "版本號由若干個<strong>修訂號</strong>組成，中間用點 <code>.</code> 隔開。"
   "每個修訂號的<strong>值</strong>是把它<strong>轉成整數</strong>（<strong>忽略前導零</strong>）。",
   "比較時<strong>從左到右</strong>逐個修訂號比。"
   "如果其中一個比較短，<strong>缺少的修訂號一律當成 0</strong>。",
   ("ul", [
     "<code>version1 &lt; version2</code> → 回傳 <code>-1</code>",
     "<code>version1 &gt; version2</code> → 回傳 <code>1</code>",
     "相等 → 回傳 <code>0</code>",
   ]),
 ],
 "pre": [
   ("note", "★ 三個一定要處理對的細節", [
     ("c", """1. 【不能直接比較字串】

   "1.10" 和 "1.2" 的字串比較會得到 "1.10" < "1.2"
   （因為 '1' < '2'）

   但版本號的意義是 1.10 > 1.2（第 10 版比第 2 版新）✘

   【必須把每一段轉成【整數】再比。】

2. 【前導零要忽略】

   "1.01" 和 "1.001" 是【相等】的（都是 1.1）

   int("01") == int("001") == 1 ✔
   Python 的 int() 自動處理 ✔

3. 【長度不同要補 0】

   "1.0" 和 "1.0.0.0" 是【相等】的

   短的那邊缺少的部分一律當成 0 ✔

【這三個細節都是「版本號」這個概念的語意，
  而不是演算法的難度】——

    這題考的是「讀題細心度」和「邊界處理」，
    不是演算法。

    但它非常實用 ——
    任何處理版本號、IP 位址、日期的程式碼
    都會遇到同樣的問題。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：version1 = "1.2", version2 = "1.10"
  輸出：-1
  說明：1.2 的修訂號是 [1, 2]，1.10 是 [1, 10]。
        第二個修訂號 2 < 10 -> version1 比較小。
        【注意：字串比較會得到相反的答案！】

範例 2
  輸入：version1 = "1.01", version2 = "1.001"
  輸出：0
  說明：忽略前導零之後，兩者都是 [1, 1]。

範例 3
  輸入：version1 = "1.0", version2 = "1.0.0.0"
  輸出：0
  說明：version1 是 [1, 0]，version2 是 [1, 0, 0, 0]。
        補 0 之後 version1 變成 [1, 0, 0, 0] -> 相等。""",
 "constraints": [
   "1 ≤ <code>version1.length</code>, <code>version2.length</code> ≤ 500",
   "<code>version1</code> 和 <code>version2</code> 只包含數字和 <code>'.'</code>",
   "兩者都是<strong>合法的版本號</strong>",
   "版本號裡的每個修訂號都能裝進 32 位元整數",
 ],
 "idea": [
   ("c", """【方法 A：切割 + 補零】

    a = version1.split(".")
    b = version2.split(".")

    for i in range(max(len(a), len(b))):
        x = int(a[i]) if i < len(a) else 0      ← 補 0
        y = int(b[i]) if i < len(b) else 0
        if x != y:
            return 1 if x > y else -1

    return 0

    O(n) 時間、O(n) 空間（切出來的 list）。

【方法 B：雙指標，不切割字串】

    邊走邊把數字算出來：

        x = 0
        while i < m and version1[i] != ".":
            x = x * 10 + int(version1[i])
            i += 1

    走到 "." 或字串結尾就停 -> x 是這一段的值 ✔

    【x = x * 10 + digit 是「字串轉整數」的標準寫法】——
    和第 8 題、第 129 題、第 171 題是同一招。

    O(n) 時間、O(1) 額外空間 ✔

【★ 迴圈條件是 while i < m or j < n（用 or 不是 and）】

    因為兩條可能不一樣長 ——
    短的那條走完之後，x 會保持 0（內層迴圈不跑），
    這正好就是「補 0」的效果 ✔

    用 and 的話，短的走完就停了 ->
    "1" 和 "1.0.0.1" 會被判成相等 ✘

【回傳值的寫法】

    return 1 if x > y else -1

    或者用 Python 的技巧：
        return (x > y) - (x < y)

    布林值在算術裡是 0/1，所以：
        x > y  -> 1 - 0 = 1
        x < y  -> 0 - 1 = -1
        相等   -> 0 - 0 = 0 ✔

    一行涵蓋三種情況（這就是 C 的 strcmp 的語意）。"""),
 ],
 "approaches": [
   ap("解法一", "<code>split</code> + 補零（最清楚）", [
     ("c", S["p165_split"]),
     "<strong>十行，O(n) 時間、O(n) 空間。</strong>"
     "<strong>面試時寫這個 —— 每一步的意圖都很明顯。</strong>",
     ("h", "<code>int()</code> 自動處理前導零"),
     ("c", """int("01")   == 1
int("001")  == 1
int("0")    == 0
int("000")  == 0

    Python 的 int() 對前導零完全沒問題 ✔

【但要小心其他語言】：

    JavaScript 的 parseInt("010") 在舊版會被當成八進位 -> 8 ✘
    （現代 JS 已經修正，但 parseInt("010", 10) 更安全。）

    C 的 strtol 也要明確指定 base = 10。

【而且不要用「去掉前導零再比字串」的做法】：

    "01" -> "1"，"001" -> "1" ✔ 這樣也對

    但「長度不同就直接比長度」的優化會出錯：
        "10" vs "9" -> 長度 2 > 1 -> 10 > 9 ✔ 對
        但如果沒去乾淨前導零就會錯。

    【直接轉整數最安全。】""",),
     ("h", "為什麼用 <code>range(max(len(a), len(b)))</code>？"),
     "<strong>因為要比較「補 0 之後」的版本，長度取兩者的最大值。</strong>",
     "<strong>只跑 <code>min</code> 的話，<code>\"1\"</code> 和 <code>\"1.1\"</code> "
     "會被判成相等 ✘</strong>",
   ], "O(n)", "O(n)", "切割 + 逐段比較", "切出來的 list", optimal=True),

   ap("解法二", "<code>zip_longest</code>（最短）", [
     ("c", S["p165_zip"]),
     ("c", """from itertools import zip_longest

zip_longest(a, b, fillvalue="0")

    普通的 zip 會在【較短的】結束時停止；
    zip_longest 會跑到【較長的】結束，
    短的那邊用 fillvalue 補上 ✔

    正好就是這題要的「補 0」語意。

【zip_longest 的其他用途】：

    - 合併長度不同的資料列
    - 「每 n 個一組」的分塊（配合 iter 技巧）
    - 處理「可選欄位」的表格

【注意 fillvalue 是字串 "0" 而不是整數 0】——
    因為後面會對它呼叫 int()。

    寫成 fillvalue=0 的話，int(0) 也對（int 接受 int），
    所以兩種都能動。但型別一致比較好。

【這個版本六行，而且沒有索引】——
    在 Python 裡，「能不用索引就不用索引」通常是對的。""",),
   ], "O(n)", "O(n)", "同解法一", "切出來的 list"),

   ap("解法三", "雙指標，不切割字串（O(1) 額外空間）", [
     ("c", S["p165_two"]),
     ("h", "★ <code>while i &lt; m or j &lt; n</code> 用 <code>or</code> 不是 <code>and</code>"),
     ("c", """用 or 的話，只要【還有任何一邊沒走完】就繼續。

    短的那邊走完之後：
        內層 while 的條件 i < m 不成立 -> 不跑
        -> x 保持 0 ✔

    這正是「補 0」的效果 ✔

【用 and 會怎樣？】

    version1 = "1"，version2 = "1.0.0.1"

    第一輪：x = 1, y = 1，相等
    i = 1（超出 m = 1），j = 2
    while 1 < 1 and 2 < 7 -> False -> 迴圈結束
    回傳 0 ✘

    正確答案是 -1（因為 version2 最後有個 1）

【「用 or 讓短的那邊自動補 0」
  是這個解法最漂亮的地方。】

【★ i += 1 跳過 "." 可能超出範圍】

    走到字串結尾時，i 會變成 m + 1。

    但下一輪的 while i < m 會直接是 False ->
    不會存取 version1[i] -> 安全 ✔

    （Python 的索引越界會 IndexError，
      所以這裡真的要確認邏輯正確。）""",),
     "<strong>O(n) 時間、O(1) 額外空間</strong>"
     "（不算輸入字串本身）。",
     "<strong>在 <code>n = 500</code> 的情況下，空間差異完全不重要</strong> —— "
     "<strong>但這個「邊走邊解析」的技巧在處理大檔案時是必要的。</strong>",
   ], "O(n)", "O(1)", "邊走邊算", "幾個變數"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、split + 補零", "O(n)", "O(n)", "10", "最清楚"],
    ["二、zip_longest", "O(n)", "O(n)", "6", "最短"],
    ["三、雙指標", "O(n)", "O(1)", "20", "不切割字串"]]),
 "edges": [
   "<strong><code>\"1.2\"</code> vs <code>\"1.10\"</code></strong> → <code>-1</code>。"
   "<strong>直接比字串會得到相反的答案。</strong>",
   "<strong><code>\"1.01\"</code> vs <code>\"1.001\"</code></strong> → <code>0</code>（前導零）。",
   "<strong><code>\"1.0\"</code> vs <code>\"1.0.0.0\"</code></strong> → <code>0</code>（補零）。",
   "<strong><code>\"1\"</code> vs <code>\"1.1\"</code></strong> → <code>-1</code>。"
   "<strong>迴圈只跑 <code>min</code> 長度會誤判成 0。</strong>",
   "<strong><code>\"1.0.1\"</code> vs <code>\"1\"</code></strong> → <code>1</code>。",
   "<strong>單一修訂號</strong> <code>\"1\"</code> vs <code>\"2\"</code> → <code>-1</code>。",
   "<strong>修訂號是 0</strong> <code>\"0.1\"</code> vs <code>\"1.1\"</code> → <code>-1</code>。",
   "<strong>雙指標版用 <code>and</code> 而不是 <code>or</code></strong> → "
   "<strong>短的那邊走完就停，會誤判成相等。</strong>",
   "<strong>用字串比較</strong> → <strong>本題第一名的 bug。</strong>",
 ],
 "follow": [
   ("h", "追問一：真實的版本號比這個複雜多少？"),
   ("c", """【語意化版本（Semantic Versioning, semver）】：

    MAJOR.MINOR.PATCH[-prerelease][+build]

    例如：1.2.3-alpha.1+20240115

    比較規則：
        1. 先比 MAJOR.MINOR.PATCH（就是本題）
        2. 【有 prerelease 的版本比沒有的【小】】
           1.0.0-alpha < 1.0.0
        3. prerelease 內部逐段比：
           數字段按數值比，非數字段按 ASCII 比，
           數字段 < 非數字段
        4. build metadata（+ 後面的）【完全忽略】

    所以：
        1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta
                    < 1.0.0-beta < 1.0.0-rc.1 < 1.0.0

【還有其他系統】：

    Debian 的版本比較（epoch:version-revision）更複雜
    Python 的 PEP 440（有 .dev、.post、a/b/rc）
    Maven 的版本排序規則

【教訓】：
    「比較版本號」看起來簡單，
    但真實世界的規則充滿特例。

    【永遠用現成的函式庫】
    （Python 的 packaging.version、
      Node 的 semver 套件）。""",),
   ("h", "追問二：<code>(x &gt; y) - (x &lt; y)</code> 這個寫法是什麼？"),
   ("c", """Python 的 bool 是 int 的子類別：
    True == 1, False == 0

    所以：
        x > y  -> (1) - (0) = 1
        x < y  -> (0) - (1) = -1
        x == y -> (0) - (0) = 0

    一行涵蓋三種情況 ✔

【這是 C 的 strcmp / qsort 比較器的標準語意】：

    負數 -> 第一個比較小
    0    -> 相等
    正數 -> 第一個比較大

【Python 2 有內建的 cmp(a, b)】，
    但 Python 3 移除了它（因為 sort 改用 key 而不是 cmp）。

    要用的話：
        from operator import sub
        cmp = lambda a, b: (a > b) - (a < b)

    或者 functools.cmp_to_key 可以把 cmp 轉成 key。

【在這題裡，本文用的 1 if x > y else -1 更明確】——
    因為我們已經確定 x != y 了。""",),
   ("h", "追問三：如果修訂號可能非常大（超過 64 位元）呢？"),
   "<strong>Python 的 <code>int</code> 無限大，完全不受影響 ✔</strong>",
   "<strong>其他語言就要用「字串比較」的技巧</strong>："
   "<strong>先去掉前導零，長度不同的話長的比較大；長度相同再逐字元比。</strong>",
   ("c", """def cmp_bignum(a, b):
    a = a.lstrip("0") or "0"
    b = b.lstrip("0") or "0"
    if len(a) != len(b):
        return 1 if len(a) > len(b) else -1
    return (a > b) - (a < b)      # 同長度時，字典序 == 數值序

【注意 or "0"】：
    "000".lstrip("0") == ""（全部被去掉）
    要補回一個 "0" ✔

【「同長度的數字字串，字典序等於數值序」】
    這個性質很有用 ——
    它是「補零對齊後可以直接比字串」的基礎。""",),
   ("h", "追問四：這題的「補 0」語意在哪裡還會出現？"),
   ("ul", [
     "<strong>IP 位址比較</strong>：<code>192.168.1</code> 不合法，但解析時常要補 0",
     "<strong>日期比較</strong>：<code>2024-1</code> vs <code>2024-01-01</code>",
     "<strong>檔案路徑排序</strong>：<code>file2</code> vs <code>file10</code>"
     "（自然排序 / natural sort）",
     "<strong>資料庫的多欄位排序</strong>：NULL 當成什麼值？",
   ]),
   "<strong>共同問題：「缺少的部分」該當成什麼？</strong>"
   "<strong>這題明確說「當成 0」，但在別的場合可能是「當成最小」「當成最大」或「不可比較」——</strong>"
   "<strong>這是設計 API 時一定要講清楚的事。</strong>",
 ],
 "related": [
   "<strong>第 8 題 String to Integer (atoi)</strong> —— 同樣的「邊走邊算」",
   "<strong>第 468 題 驗證 IP 位址</strong> —— 同樣的切割與驗證",
   "<strong>第 171 題 Excel 表欄位序號</strong> —— 另一個進位制轉換",
   "<strong>第 179 題 Largest Number</strong> —— 另一個「自訂比較」的題目",
 ],
 "check": [
   "為什麼不能直接用字串比較？請舉出一個會錯的例子。",
   "「補 0」的語意是什麼？迴圈只跑 <code>min</code> 長度會在哪個測資出錯？",
   "雙指標版的迴圈條件為什麼用 <code>or</code> 而不是 <code>and</code>？",
   "<code>(x &gt; y) - (x &lt; y)</code> 為什麼能一行涵蓋三種情況？",
 ],
})
print("P165 written")

# ==================== 166. Fraction to Recurring Decimal ====================
S["p166"] = '''class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        out = []
        # 符號：兩者異號才是負的（用 ^ 判斷正負號是否不同）
        if (numerator < 0) != (denominator < 0):
            out.append("-")

        n, d = abs(numerator), abs(denominator)

        out.append(str(n // d))             # 整數部分
        r = n % d
        if r == 0:
            return "".join(out)             # 整除，沒有小數

        out.append(".")
        seen = {}                           # 餘數 -> 它在小數部分的位置
        frac = []

        while r:
            if r in seen:                   # ★ 餘數重複出現 -> 找到循環節
                i = seen[r]
                return "".join(out) + "".join(frac[:i]) + "(" + "".join(frac[i:]) + ")"
            seen[r] = len(frac)
            r *= 10
            frac.append(str(r // d))
            r %= d

        return "".join(out) + "".join(frac)'''

S["p166_divmod"] = '''class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = "-" if (numerator < 0) != (denominator < 0) else ""
        n, d = abs(numerator), abs(denominator)

        q, r = divmod(n, d)
        if r == 0:
            return sign + str(q)

        frac, seen = [], {}
        while r and r not in seen:
            seen[r] = len(frac)
            digit, r = divmod(r * 10, d)
            frac.append(str(digit))

        if r:                               # 因為「餘數重複」而停 -> 有循環節
            i = seen[r]
            body = "".join(frac[:i]) + "(" + "".join(frac[i:]) + ")"
        else:                               # 因為「餘數為 0」而停 -> 有限小數
            body = "".join(frac)

        return sign + str(q) + "." + body'''


def _p166_ref(num, den):
    """獨立參考解：用 Fraction 驗證「輸出的字串代表同一個有理數」。"""
    from fractions import Fraction
    return Fraction(num, den)


def _parse_decimal(s):
    """把輸出的字串解析回 Fraction，用來驗證正確性。"""
    from fractions import Fraction
    sign = 1
    if s.startswith("-"):
        sign = -1
        s = s[1:]
    if "." not in s:
        return sign * Fraction(int(s))
    whole, frac = s.split(".")
    val = Fraction(int(whole))
    if "(" in frac:
        pre, rep = frac.split("(")
        rep = rep.rstrip(")")
        if pre:
            val += Fraction(int(pre), 10 ** len(pre))
        # 循環節：rep / (10^len(pre) * (10^len(rep) - 1))
        val += Fraction(int(rep), (10 ** len(pre)) * (10 ** len(rep) - 1))
    else:
        val += Fraction(int(frac), 10 ** len(frac))
    return sign * val


_p166 = [S.load(k) for k in ("p166", "p166_divmod")]

for num, den, want in [
    (1, 2, "0.5"),
    (2, 1, "2"),
    (4, 333, "0.(012)"),
    (1, 3, "0.(3)"),
    (-50, 8, "-6.25"),
    (7, -12, "-0.58(3)"),
    (0, 5, "0"),
    (1, 6, "0.1(6)"),
    (-1, -2, "0.5"),
    (-2147483648, -1, "2147483648"),
]:
    for sol in _p166:
        got = sol.fractionToDecimal(num, den)
        assert got == want, ("P166", num, den, want, got, sol)

for _ in range(6000):
    den = random.choice([d for d in range(-40, 41) if d != 0])
    num = random.randint(-200, 200)
    outs = [sol.fractionToDecimal(num, den) for sol in _p166]
    assert len(set(outs)) == 1, ("P166 disagree", num, den, outs)
    # 解析回去，必須等於原本的分數
    assert _parse_decimal(outs[0]) == _p166_ref(num, den), \
        ("P166 value", num, den, outs[0], _p166_ref(num, den))
print("P166 solutions OK")

_P166_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 長除法時，只要【餘數重複出現】，接下來的數字就一定會完全重複 —— 那就是循環節的起點。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">4 ÷ 333 的長除法過程</text>
            <g font-size="12">
              <text x="60" y="86" fill="var(--text-muted)">餘數 r</text>
              <text x="200" y="86" fill="var(--text-muted)">r × 10 ÷ 333</text>
              <text x="380" y="86" fill="var(--text-muted)">商（小數位）</text>
              <text x="520" y="86" fill="var(--text-muted)">新餘數</text>
            </g>
            <g font-size="12">
              <text x="60" y="116" fill="var(--gold)">4</text>
              <text x="200" y="116" fill="var(--text-muted)">40 ÷ 333</text>
              <text x="380" y="116" fill="var(--accent)">0</text>
              <text x="520" y="116" fill="var(--text-muted)">40</text>
              <text x="60" y="144" fill="var(--text-muted)">40</text>
              <text x="200" y="144" fill="var(--text-muted)">400 ÷ 333</text>
              <text x="380" y="144" fill="var(--accent)">1</text>
              <text x="520" y="144" fill="var(--text-muted)">67</text>
              <text x="60" y="172" fill="var(--text-muted)">67</text>
              <text x="200" y="172" fill="var(--text-muted)">670 ÷ 333</text>
              <text x="380" y="172" fill="var(--accent)">2</text>
              <text x="520" y="172" fill="var(--text-muted)">4</text>
              <text x="60" y="200" fill="#ff8a65">4 ← 重複了！</text>
              <text x="200" y="200" fill="#ff8a65">（接下來會一模一樣）</text>
            </g>
            <text x="20" y="236" fill="var(--gold)" font-size="13">餘數 4 在位置 0 出現過 → 從位置 0 開始都是循環節 → &quot;0.(012)&quot; ✔</text>
            <line x1="20" y1="260" x2="620" y2="260" stroke="var(--border)"/>
            <text x="20" y="288" fill="var(--accent)" font-size="13">為什麼「餘數重複」就代表「數字重複」？</text>
            <text x="40" y="318" fill="var(--text-muted)" font-size="12">長除法的每一步，【完全由當前的餘數決定】：</text>
            <text x="60" y="344" fill="var(--gold)" font-size="12">下一位數字 = (r × 10) ÷ d　　新餘數 = (r × 10) mod d</text>
            <text x="40" y="374" fill="var(--text-muted)" font-size="12">所以只要 r 一樣，後面的一切就完全一樣 → 進入循環 ✔</text>
            <text x="20" y="408" fill="#ff8a65" font-size="12">★ 而且循環【一定會發生】（除非整除）：餘數只有 0 到 d−1 共 d 種可能，</text>
            <text x="20" y="432" fill="var(--text-muted)" font-size="12">做了 d 步之後必然有重複（鴿籠原理）—— 所以循環節長度最多 d−1。</text>
            <text x="20" y="462" fill="var(--accent)" font-size="12">這也證明了：任何有理數的小數展開，不是有限的就是循環的。</text>'''

emit({
 "num": 166, "slug": "fraction-to-recurring-decimal",
 "en": [
   "Given two integers representing the <code>numerator</code> and <code>denominator</code> of "
   "a fraction, return <em>the fraction in string format</em>.",
   "If the fractional part is repeating, enclose the repeating part in parentheses.",
   "If multiple answers are possible, return <strong>any of them</strong>.",
   "It is <strong>guaranteed</strong> that the length of the answer string is less than "
   "<code>10⁴</code> for all the given inputs.",
 ],
 "zh": [
   "給你一個分數的<strong>分子</strong>和<strong>分母</strong>，"
   "回傳它的<strong>小數形式（字串）</strong>。",
   "如果小數部分<strong>會循環</strong>，就把<strong>循環的那一段用括號括起來</strong>。",
   "題目保證答案的長度小於 <code>10⁴</code>。",
 ],
 "pre": [
   ("note", "★ 核心洞察：餘數重複 ⟹ 數字開始循環", [
     ("c", """長除法的每一步：

    下一位數字 = (r × 10) // d
    新的餘數   = (r × 10) %  d

    【完全由當前的餘數 r 決定】—— 和之前的歷史無關。

    所以只要某個餘數 r 【第二次出現】，
    接下來的所有數字就會和上次【一模一樣】✔

    -> 那就是循環的開始。

【所以演算法是】：

    用一個 dict 記錄「每個餘數第一次出現在小數的第幾位」。

    每一步：
        如果 r 已經在 dict 裡 -> 找到循環節，從 dict[r] 開始加括號
        如果 r == 0          -> 除盡了，是有限小數
        否則                  -> 記下 r 的位置，繼續除

【★ 為什麼循環一定會發生（除非整除）？】

    餘數只有 0, 1, ..., d-1 共 d 種可能。

    如果做了 d 步都還沒出現 0，
    那 d 個非零餘數裡必然有重複（鴿籠原理）✔

    -> 循環節的長度最多是 d - 1

【這同時證明了一個數學事實】：

    【任何有理數的小數展開，不是有限的就是循環的。】

    （反過來也成立：任何循環小數都是有理數。）

    這題其實是在讓你「用程式重現」這個定理的證明。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：numerator = 1, denominator = 2
  輸出："0.5"

範例 2
  輸入：numerator = 2, denominator = 1
  輸出："2"

範例 3
  輸入：numerator = 4, denominator = 333
  輸出："0.(012)"
  說明：4/333 = 0.012012012...，循環節是 "012"。""",
 "constraints": [
   "−2³¹ ≤ <code>numerator</code>, <code>denominator</code> ≤ 2³¹ − 1",
   "<code>denominator != 0</code>",
 ],
 "mid": [
   ("note", "★ 注意這個數值範圍：<code>-2³¹</code> 除以 <code>-1</code> 會溢位", [
     ("c", """numerator = -2147483648 (= -2^31)
denominator = -1

    答案是 2147483648 = 2^31

    但 32 位元有號整數的上限是 2^31 - 1 ——
    【溢位！】

【在 C++ / Java 裡】：
    abs(-2147483648) 仍然是 -2147483648（溢位繞回）✘

    必須先轉成 long：
        long n = labs((long)numerator);

【在 Python 裡完全沒問題】（整數無限大）——
    但面試時要主動指出這個陷阱。

【這是「32 位元整數的不對稱性」】：

    範圍是 [-2^31, 2^31 - 1]
    負數比正數多一個 ->
    「取絕對值」對最小的負數會溢位。

    同樣的陷阱在第 7 題（整數反轉）、
    第 29 題（兩數相除）也會出現。""",),
   ]),
 ],
 "idea": [
   ("fig", _P166_FIG, "0 0 640 484"),
   ("c", """【完整流程】

    1. 特判 numerator == 0 -> "0"
       （不然會輸出 "-0" 或 "0." 之類的）

    2. 決定符號
       (numerator < 0) != (denominator < 0)
       -> 兩者【異號】才是負的

       用 != 比較兩個布林值，等於 XOR ✔

    3. 取絕對值，算整數部分和第一個餘數
       q, r = divmod(abs(n), abs(d))

    4. r == 0 -> 整除，直接回傳

    5. 長除法迴圈：
       while r:
           if r 在 seen 裡 -> 找到循環節，加括號後回傳
           seen[r] = 目前小數的長度
           r *= 10
           記下 r // d 這位數字
           r %= d

    6. 迴圈自然結束（r 變 0）-> 有限小數

【★ 三個容易錯的地方】

  (a) numerator == 0 要特判
      否則符號判斷會產生 "-0"（如果 denominator < 0）

  (b) 符號要用 XOR 判斷，不能用 n * d < 0
      （乘法可能溢位，而且 0 的情況要另外想）

  (c) seen 記錄的是「位置」不是「有沒有出現過」
      因為要知道「從哪裡開始加括號」"""),
 ],
 "approaches": [
   ap("解法一", "長除法 + 餘數雜湊表（標準答案）", [
     ("c", S["p166"]),
     "<strong>O(d) 時間（最多 d 步就會循環或除盡）、O(d) 空間。</strong>",
     ("h", "★ 符號判斷：<code>(a &lt; 0) != (b &lt; 0)</code>"),
     ("c", """這是「XOR」的寫法：兩者的正負【不同】時為 True。

【為什麼不用 n * d < 0？】

    ✘ 乘法可能溢位（在 C++/Java 裡）
    ✘ 其中一個是 0 時，乘積是 0（但這題 numerator 可能是 0）

【為什麼不用 (n < 0) ^ (d < 0)？】

    在 Python 裡 ^ 對 bool 也是 XOR，所以也可以 ✔
    （bool 是 int 的子類別，True ^ False == 1）

    但 != 更明確「這是在比較兩個布林值」。

【★ numerator == 0 必須先特判】

    如果 numerator = 0, denominator = -5：
        符號判斷：(False) != (True) -> True -> 加上 "-"
        整數部分：0 // 5 = 0
        結果："-0" ✘

    正確答案是 "0"。

    【所以 if numerator == 0: return "0" 要放在最前面。】""",),
     ("h", "<code>seen</code> 為什麼要記「位置」而不只是「有沒有出現過」？"),
     ("c", """因為找到循環時，要知道【從哪一位開始加括號】。

    1/6 = 0.1666...

        r=1: seen[1]=0, 數字 "1", r=4
        r=4: seen[4]=1, 數字 "6", r=4
        r=4: 【已經在 seen 裡，位置是 1】

        -> frac = ['1', '6']
        -> 前面不循環的是 frac[:1] = "1"
        -> 循環節是 frac[1:] = "6"
        -> 答案 "0.1(6)" ✔

    如果 seen 只存「出現過」，
    就不知道要從哪裡切 ——
    會寫成 "0.(16)" ✘（那是 0.161616...）

【這是「用 dict 存位置而不是用 set 存存在性」的典型理由】。

    第 3 題（無重複字元的最長子字串）、
    第 1 題（兩數之和）也都是存位置而不是存存在性。""",),
   ], "O(d)", "O(d)", "最多 d 步就循環", "餘數雜湊表", optimal=True),

   ap("解法二", "用 <code>divmod</code> 的版本（結構更清楚）", [
     ("c", S["p166_divmod"]),
     ("c", """把「除法」和「取餘」合成一次 divmod 呼叫：

    q, r = divmod(n, d)             # 整數部分
    digit, r = divmod(r * 10, d)    # 每一位小數

【divmod 的好處】：
    ✔ 一次運算同時得到商和餘數（底層只做一次除法）
    ✔ 語意清楚：「這是一次帶餘除法」
    ✔ 不會寫錯（用 // 和 % 分兩行時，容易忘記更新 r）

【迴圈的結構也更清楚】：

    while r and r not in seen:
        ...

    if r:   # 因為「重複」而停 -> 有循環
    else:   # 因為「r == 0」而停 -> 有限小數

    【把「為什麼停下來」明確分成兩種情況】，
    比在迴圈裡 return 更好讀。

【一般原則】：

    「迴圈有兩種結束方式」時，
    與其在迴圈裡 return，
    不如讓迴圈自然結束，再用一個 if 分辨。

    這樣比較容易看出「所有情況都被處理了」。""",),
     "<strong>複雜度和解法一完全相同。</strong>"
     "<strong>挑一個順手的寫就好。</strong>",
   ], "O(d)", "O(d)", "同解法一", "餘數雜湊表"),
 ],
 "compare": (["解法", "時間", "空間", "結構", "備註"],
   [["一、迴圈裡 return", "O(d)", "O(d)", "緊湊", "標準寫法"],
    ["二、divmod + 事後分辨", "O(d)", "O(d)", "清楚", "比較好讀"]]),
 "edges": [
   "<strong><code>numerator = 0</code></strong> → <code>\"0\"</code>。"
   "<strong>不特判的話，分母是負數時會輸出 <code>\"-0\"</code>。</strong>",
   "<strong>整除</strong> <code>(2, 1)</code> → <code>\"2\"</code>（沒有小數點）。",
   "<strong>有限小數</strong> <code>(1, 2)</code> → <code>\"0.5\"</code>。",
   "<strong>純循環</strong> <code>(1, 3)</code> → <code>\"0.(3)\"</code>。",
   "<strong>混循環</strong> <code>(1, 6)</code> → <code>\"0.1(6)\"</code>。"
   "<strong>前面有不循環的部分 —— 所以 <code>seen</code> 要記位置。</strong>",
   "<strong>負數</strong> <code>(7, -12)</code> → <code>\"-0.58(3)\"</code>。",
   "<strong>兩個都是負數</strong> <code>(-1, -2)</code> → <code>\"0.5\"</code>（正的）。",
   "<strong><code>(-2³¹, -1)</code></strong> → <code>\"2147483648\"</code>。"
   "<strong>在 C++/Java 裡 <code>abs</code> 會溢位。</strong>",
   "<strong>用 <code>n * d &lt; 0</code> 判斷符號</strong> → 可能溢位，而且 0 的情況要另外處理。",
 ],
 "follow": [
   ("h", "追問一：循環節的長度最多多少？"),
   ("c", """【最多是 d - 1】（d 是分母）。

    因為餘數只有 1..d-1 這 d-1 種非零可能，
    做了 d-1 步之後必然重複（鴿籠原理）。

【實際的長度是多少？】

    設 d = 2^a · 5^b · m（m 和 10 互質）。

    - 「不循環的前綴」長度 = max(a, b)
      （因為 2 和 5 是 10 的質因數，可以被「除盡」）

    - 「循環節」的長度 = 【10 對 m 的乘法階】
      也就是最小的 k 使得 10^k ≡ 1 (mod m)

    例子：
        1/6  = 1/(2·3)：前綴 1 位，循環節 1 位 -> 0.1(6) ✔
        1/7  ：m = 7，10^6 ≡ 1 (mod 7)，循環節 6 位
               -> 0.(142857) ✔
        1/333：333 = 3^2 · 37，循環節 3 位 -> 0.(003) ✔

【1/7 = 0.(142857) 是最有名的例子】——
    142857 這個數有很多神奇的性質
    （乘以 1~6 都是同樣六個數字的循環排列）。

【題目保證答案長度 < 10^4】，
    所以循環節不會太長 ——
    但理論上 d 接近 2^31 時，循環節可以到 2^31 - 1。""",),
   ("h", "追問二：怎麼反過來（循環小數轉分數）？"),
   ("c", """【純循環】0.(abc) = abc / 999

    設 x = 0.(abc)
    1000x = abc.(abc)
    1000x - x = abc
    x = abc / 999 ✔

【混循環】0.p(q)（p 是 k 位前綴，q 是 m 位循環節）

    x = [pq - p] / [(10^m - 1) × 10^k]

    例如 0.1(6)：
        p = "1"（k=1），q = "6"（m=1）
        x = (16 - 1) / (9 × 10) = 15/90 = 1/6 ✔

【本文的測試就是用這個公式驗證的】：

    把輸出的字串解析回 Fraction，
    檢查它是否等於原本的 numerator/denominator ✔

    【這種「往返驗證」（round-trip testing）比
      「比對硬寫的期望字串」可靠得多】——

    因為它驗證的是【語意】而不是【格式】。""",),
   ("h", "追問三：如果要求「最短的循環節」呢？"),
   "<strong>本文的演算法已經給出最短的了。</strong>",
   ("c", """因為我們在【餘數第一次重複】時就停下來 ——
    那個位置就是循環的最小起點。

    如果繼續跑，會得到「循環節重複兩次」之類的答案
    （例如 0.(3) 變成 0.(33)）——
    那也是對的，但不是最短的。

【題目說「如果有多個答案，回傳任何一個」】，
    所以理論上 0.(33) 也算對。

    但實務上一定要給最短的 ——
    而本文的做法自然就是最短 ✔

【為什麼「第一次重複」就是最短？】

    因為「餘數序列」進入循環的第一個點，
    就是「數字序列」開始循環的第一個點
    （兩者一一對應）。

    這其實是 Floyd 判圈法裡「環的入口」那個概念 ——
    只是這裡我們用了 O(d) 空間的雜湊表，
    而不是 O(1) 空間的快慢指標。

    【理論上可以用 Floyd 把空間降到 O(1)】，
    但那樣要重跑除法，而且程式碼複雜很多 ——
    不值得。""",),
   ("h", "追問四：為什麼「有理數 ⟺ 有限或循環小數」？"),
   ("c", """【有理數 ⟹ 有限或循環】

    就是本題的演算法：
        餘數只有有限種（0 到 d-1），
        所以要嘛碰到 0（有限），要嘛重複（循環）✔

【有限或循環 ⟹ 有理數】

    有限小數：0.abc = abc / 1000 ✔ 顯然是有理數

    循環小數：用追問二的公式 ✔

【所以無理數的小數展開既不有限也不循環】。

    這給了一個「證明某個數是無理數」的方法：
        證明它的小數展開不循環。

    例如 Champernowne 常數
        0.12345678910111213...
    （把所有正整數接起來）
    顯然不循環 -> 無理數 ✔

【這題把一個數學定理變成了可執行的程式碼】——
    這是我覺得它最有趣的地方。""",),
 ],
 "related": [
   "<strong>第 29 題 兩數相除</strong> —— 同樣的溢位陷阱",
   "<strong>第 7 題 整數反轉</strong> —— 同樣的 32 位元邊界",
   "<strong>第 142 題 環形鏈結串列 II</strong> —— 「找循環的起點」的另一種形式",
   "<strong>第 3 題 無重複字元的最長子字串</strong> —— 同樣「用 dict 存位置」",
 ],
 "check": [
   "為什麼「餘數重複」就代表「數字開始循環」？",
   "為什麼循環一定會發生（除非整除）？循環節最長多少？",
   "<code>seen</code> 為什麼要記「位置」而不只是「出現過」？",
   "<code>numerator = 0</code> 為什麼一定要特判？",
 ],
})
print("P166 written")
