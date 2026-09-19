# -*- coding: utf-8 -*-
"""第 25–28 題。"""
import random
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(25)

# ==================== 25. Reverse Nodes in k-Group ====================
S["p25_iter"] = '''class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy          # 這一組「前面」那個節點

        while True:
            # 1. 先數夠不夠 k 個；不夠就整個結束
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            group_next = kth.next   # 下一組的第一個（反轉前先記下來）

            # 2. 反轉這一組：把 [group_prev.next .. kth] 反過來
            prev, cur = group_next, group_prev.next
            while cur is not group_next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # 3. 接回去。反轉後 kth 變成這一組的頭，原本的頭變成尾
            tail = group_prev.next          # 原本的頭 = 反轉後的尾
            group_prev.next = kth
            group_prev = tail               # 下一組的「前面」就是這個尾

        return dummy.next'''

S["p25_rec"] = '''class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 先確認剩下的節點夠不夠 k 個
        node = head
        for _ in range(k):
            if node is None:
                return head          # 不足 k 個，原封不動
            node = node.next
        # 此時 node 指向「下一組的第一個」

        # 2. 反轉前 k 個。prev 從「下一組反轉好的結果」開始，
        #    這樣反轉完自動就接好了
        prev = self.reverseKGroup(node, k)
        cur = head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev                  # 反轉後的新頭'''

_p25 = [S.load(k) for k in ("p25_iter", "p25_rec")]


def _p25_ref(vals, k):
    out = []
    for i in range(0, len(vals), k):
        chunk = vals[i:i + k]
        out.extend(chunk[::-1] if len(chunk) == k else chunk)
    return out


for vals, k in [([1, 2, 3, 4, 5], 2), ([1, 2, 3, 4, 5], 3), ([1, 2, 3, 4, 5], 1),
                ([1, 2, 3, 4, 5], 5), ([1, 2, 3, 4, 5], 6), ([], 1), ([1], 1), ([1], 2)]:
    e = _p25_ref(vals, k)
    for sol in _p25:
        assert from_list(sol.reverseKGroup(to_list(vals), k)) == e, ("P25", vals, k, sol)
for _ in range(3000):
    vals = list(range(random.randint(0, 10)))
    k = random.randint(1, 6)
    e = _p25_ref(vals, k)
    for sol in _p25:
        assert from_list(sol.reverseKGroup(to_list(vals), k)) == e, ("P25", vals, k, sol)
print("P25 solutions OK")

_P25_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">k = 3，list = 1→2→3→4→5。第一組反轉，剩下 2 個不足 k → 保持原樣</text>
            <text x="20" y="48" fill="var(--text-muted)" font-size="12">反轉前，先把四個關鍵位置標出來</text>
            <g font-size="14" text-anchor="middle">
              <rect x="34" y="62" width="58" height="36" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/>
              <text x="63" y="85" fill="var(--text-muted)" font-size="10">dummy</text>
              <rect x="120" y="62" width="58" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="149" y="86" fill="var(--accent)">1</text>
              <rect x="206" y="62" width="58" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="235" y="86" fill="var(--accent)">2</text>
              <rect x="292" y="62" width="58" height="36" rx="6" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="321" y="86" fill="var(--gold)">3</text>
              <rect x="378" y="62" width="58" height="36" rx="6" fill="none" stroke="var(--border)"/><text x="407" y="86" fill="var(--text-muted)">4</text>
              <rect x="464" y="62" width="58" height="36" rx="6" fill="none" stroke="var(--border)"/><text x="493" y="86" fill="var(--text-muted)">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="92" y1="80" x2="116" y2="80"/><line x1="178" y1="80" x2="202" y2="80"/>
              <line x1="264" y1="80" x2="288" y2="80"/><line x1="350" y1="80" x2="374" y2="80"/>
              <line x1="436" y1="80" x2="460" y2="80"/>
            </g>
            <g font-size="10" text-anchor="middle">
              <text x="63" y="116" fill="var(--text-muted)">group_prev</text>
              <text x="149" y="116" fill="var(--accent)">組頭（會變組尾）</text>
              <text x="321" y="116" fill="var(--gold)">kth（會變組頭）</text>
              <text x="407" y="116" fill="var(--text-muted)">group_next</text>
            </g>
            <text x="20" y="158" fill="var(--text-muted)" font-size="12">反轉後</text>
            <g font-size="14" text-anchor="middle">
              <rect x="34" y="172" width="58" height="36" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/>
              <text x="63" y="195" fill="var(--text-muted)" font-size="10">dummy</text>
              <rect x="120" y="172" width="58" height="36" rx="6" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="149" y="196" fill="var(--gold)">3</text>
              <rect x="206" y="172" width="58" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="235" y="196" fill="var(--accent)">2</text>
              <rect x="292" y="172" width="58" height="36" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="321" y="196" fill="var(--accent)">1</text>
              <rect x="378" y="172" width="58" height="36" rx="6" fill="none" stroke="var(--border)"/><text x="407" y="196" fill="var(--text-muted)">4</text>
              <rect x="464" y="172" width="58" height="36" rx="6" fill="none" stroke="var(--border)"/><text x="493" y="196" fill="var(--text-muted)">5</text>
            </g>
            <g stroke="var(--gold)" stroke-width="1.8">
              <line x1="92" y1="190" x2="116" y2="190"/><line x1="178" y1="190" x2="202" y2="190"/>
              <line x1="264" y1="190" x2="288" y2="190"/><line x1="350" y1="190" x2="374" y2="190"/>
              <line x1="436" y1="190" x2="460" y2="190"/>
            </g>
            <text x="321" y="226" fill="var(--accent)" font-size="10" text-anchor="middle">新的 group_prev</text>
            <text x="20" y="262" fill="var(--gold)" font-size="12">下一輪從節點 1 往後數 3 個：4、5、None → 數不到 3 個 → return，4→5 保持原樣</text>'''

emit({
 "num": 25, "slug": "reverse-nodes-in-k-group",
 "en": [
   "Given the <code>head</code> of a linked list, reverse the nodes of the list "
   "<code>k</code> at a time, and return the modified list.",
   "<code>k</code> is a positive integer and is less than or equal to the length of the "
   "linked list. If the number of nodes is not a multiple of <code>k</code> then left-out "
   "nodes, in the end, should remain as it is.",
   "You may not alter the values in the list's nodes, only nodes themselves may be changed.",
 ],
 "zh": [
   "給你一條鏈結串列的頭節點 <code>head</code>，請<strong>每 <code>k</code> 個節點一組</strong>"
   "進行反轉，回傳修改後的串列。",
   "<code>k</code> 是正整數，且不超過串列長度。"
   "如果節點總數<strong>不是 <code>k</code> 的倍數</strong>，那麼最後剩下的不足 <code>k</code> 個節點"
   "<strong>保持原本的順序</strong>。",
   "<strong>不能修改節點的值</strong>，只能改變節點之間的連接。",
 ],
 "pre": [
   ("note", "這題是第 24 題的一般化，難度跳三級", [
     ("c", """第 24 題（k = 2）：
    交換一對只要重接三條線，可以硬寫。

第 25 題（一般 k）：
    必須先「數夠 k 個」才能動手，
    而且反轉之後要把「新頭」和「新尾」分別接回前後兩段。

list = 1 -> 2 -> 3 -> 4 -> 5，k = 3

    第一組 [1,2,3] -> 反轉成 3 -> 2 -> 1
    剩下 [4,5] 只有 2 個 < 3  ->  不反轉，原樣保留

    答案：3 -> 2 -> 1 -> 4 -> 5

如果 k = 2：
    [1,2] -> 2,1
    [3,4] -> 4,3
    [5]   -> 不足，保留
    答案：2 -> 1 -> 4 -> 3 -> 5"""),
     "<strong>「先數夠再動手」是本題的第一個關鍵</strong> —— "
     "因為你必須在反轉<strong>之前</strong>就知道這一組夠不夠，"
     "反轉到一半才發現不夠是救不回來的（單向串列無法回頭）。",
   ]),
 ],
 "examples": """範例 1
  輸入：head = [1,2,3,4,5], k = 2
  輸出：[2,1,4,3,5]

範例 2
  輸入：head = [1,2,3,4,5], k = 3
  輸出：[3,2,1,4,5]

範例 3
  輸入：head = [1,2,3,4,5], k = 1
  輸出：[1,2,3,4,5]
  說明：每組只有一個節點，反轉等於沒動。""",
 "constraints": [
   "節點數 <code>n</code> 在 <code>[1, 5000]</code> 範圍內",
   "0 ≤ <code>Node.val</code> ≤ 1000",
   "1 ≤ <code>k</code> ≤ <code>n</code>",
   "<strong>進階：</strong>能不能用 <code>O(1)</code> 額外空間？",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong><code>k</code> 可以等於 1</strong>：每組一個，反轉等於沒變。程式要能正確處理（不能死循環）。",
       "<strong><code>k</code> 可以等於 <code>n</code></strong>：整條反轉，只有一組。",
       "<strong>n 可以到 5000</strong>，遞迴解法的深度是 <code>n/k</code>。"
       "當 <code>k = 1</code> 時深度是 5000 —— <strong>超過 Python 預設的遞迴上限 1000，會 RecursionError</strong>。"
       "這是本題選擇迴圈解法的實際理由，不只是理論上的。",
       "<strong>進階要求 O(1) 空間</strong> —— 明確排除遞迴。迴圈版才是完整答案。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P25_FIG, "0 0 640 276"),
   "每一組的處理可以拆成三步：<strong>數夠 k 個 → 反轉這一段 → 把頭尾接回去</strong>。"
   "難的是第三步 —— 要同時管好四個指標。",
 ],
 "approaches": [
   ap("解法一", "迴圈（O(1) 空間，完整答案）", [
     ("c", S["p25_iter"]),
     ("h", "四個關鍵指標"),
     ("c", """group_prev  這一組「前面」那個節點（第一組時是 dummy）
kth         這一組的「第 k 個」節點（反轉後會變成組頭）
group_next  下一組的第一個（也就是 kth.next，反轉前必須先存）
tail        這一組原本的頭（反轉後會變成組尾）

反轉前：  group_prev -> [A -> B -> C] -> group_next
                        ^tail        ^kth

反轉後：  group_prev -> [C -> B -> A] -> group_next
                        ^kth         ^tail

所以：
    group_prev.next = kth        接上新頭
    tail.next = group_next       已經在反轉迴圈裡做掉了（見下）
    group_prev = tail            tail 是下一組的「前面」"""),
     ("h", "反轉迴圈的巧思：<code>prev</code> 從 <code>group_next</code> 開始"),
     ("c", """一般的串列反轉：
    prev = None
    while cur:
        nxt = cur.next; cur.next = prev; prev = cur; cur = nxt

這題的版本：
    prev = group_next            <- 不是 None！
    cur = group_prev.next
    while cur is not group_next: <- 終止條件也不是 None
        nxt = cur.next; cur.next = prev; prev = cur; cur = nxt

為什麼 prev 要從 group_next 開始？

    因為第一次迴圈時 cur 是組頭（反轉後會變組尾），
    cur.next = prev 這一行就直接把「組尾 -> 下一組」接好了。

    如果照一般寫法 prev = None，反轉完組尾會指向 None，
    整條串列從這裡斷掉，還要多寫一行 tail.next = group_next 補回去。

    從 group_next 開始，等於「把接回去這件事融進反轉迴圈裡」。
    少一行，也少一個出錯的機會。

終止條件用 cur is not group_next 而不是 cur is not None：
    因為我們只要反轉這一組，不能一路反轉到底。"""),
     ("h", "「先數夠」的寫法"),
     ("c", """kth = group_prev
for _ in range(k):
    kth = kth.next
    if kth is None:
        return dummy.next     # 不足 k 個，整個結束

從 group_prev 走 k 步，剛好停在這一組的第 k 個。
走到一半變成 None 就表示不夠 —— 這時候「剩下的保持原樣」，
而它們本來就沒被動過，所以直接 return 就對了。

這也是為什麼這一步必須在反轉之前做：
反轉到一半才發現不夠，前面已經被改壞了。"""),
     "<strong>為什麼 <code>while True</code> 而不是有條件的 while？</strong>"
     "因為結束條件（數不夠 k 個）在迴圈中間才會知道，"
     "寫成 <code>while True</code> + 內部 <code>return</code> 比硬湊一個前置條件清楚得多。",
   ], "O(n)", "O(1)", "每個節點被走兩次（數一次、反轉一次）",
      "只用幾個指標", optimal=True),

   ap("解法二", "遞迴（好懂，但不符合進階要求）", [
     ("c", S["p25_rec"]),
     ("h", "為什麼 <code>prev</code> 從遞迴結果開始？"),
     ("c", """prev = self.reverseKGroup(node, k)

node 是「下一組的第一個」，
遞迴回傳的是「下一組（以及之後全部）處理完的新頭」。

然後反轉前 k 個時：
    第一次迴圈 cur = head（這一組的組頭，反轉後變組尾）
    cur.next = prev  ->  組尾直接指向「後面處理好的部分」

和迴圈版的 prev = group_next 是完全一樣的巧思，
只是這裡的「後面」已經先被遞迴處理好了。

這種「先處理後面，再處理自己」的順序，
在串列的遞迴題裡非常常見（第 24、206、234 題都是）。"""),
     ("h", "致命缺點：遞迴深度"),
     ("c", """遞迴深度 = n / k

n = 5000, k = 1  ->  深度 5000
Python 預設遞迴上限是 1000  ->  RecursionError

可以 sys.setrecursionlimit(10000) 繞過，
但那是在掩蓋問題，而且真的很深的時候會 segfault
（Python 的遞迴限制是為了保護 C 層的堆疊）。

題目明講了「進階：O(1) 空間」——
這句話就是在說「請寫迴圈版」。"""),
     "遞迴版適合<strong>在面試時先講思路</strong>（因為它把邏輯講得最清楚），"
     "然後說「但深度是 n/k，k=1 時會爆，所以我寫迴圈版」，再開始寫解法一。",
   ], "O(n)", "O(n/k)", "每個節點處理一次", "遞迴深度 n/k"),
 ],
 "compare": (["解法", "時間", "空間", "k=1, n=5000 可用？", "備註"],
   [["一、迴圈", "O(n)", "O(1)", "✔", "符合進階要求，標準答案"],
    ["二、遞迴", "O(n)", "O(n/k)", "✘ RecursionError", "思路最清楚，講解用"]]),
 "edges": [
   "<strong><code>k = 1</code></strong>：<code>([1,2,3,4,5], 1)</code> → 原樣。"
   "每一組只有一個節點，反轉迴圈只跑一次。要確認不會死循環。",
   "<strong><code>k = n</code></strong>：<code>([1,2,3,4,5], 5)</code> → <code>[5,4,3,2,1]</code>。只有一組。",
   "<strong><code>k &gt; n</code></strong>：<code>([1], 2)</code> → <code>[1]</code>。"
   "題目保證 k ≤ n，但寫成能處理比較安全。",
   "<strong>剛好整除</strong>：<code>([1,2,3,4], 2)</code> → <code>[2,1,4,3]</code>。最後沒有殘餘。",
   "<strong>有殘餘</strong>：<code>([1,2,3,4,5], 2)</code> → <code>[2,1,4,3,5]</code>。"
   "最後的 5 不動。",
   "<strong>殘餘剛好 k−1 個</strong>：<code>([1,2,3,4,5], 3)</code> → <code>[3,2,1,4,5]</code>。",
   "<strong>單一節點</strong>：<code>([1], 1)</code> → <code>[1]</code>。",
 ],
 "follow": [
   ("h", "追問一：如果最後不足 k 個「也要」反轉呢？"),
   "把「數夠 k 個」的檢查從 <code>return</code> 改成<strong>記下實際數量，反轉那麼多個</strong>。"
   "程式碼會變長一點（因為終止條件不再是固定的 k），但結構一樣。"
   "<strong>面試時一定要先問清楚這一點</strong> —— 兩種規格的程式碼差很多。",
   ("h", "追問二：如果 k 很大而串列很長，能平行處理嗎？"),
   "理論上每一組是獨立的，可以平行反轉，最後再串起來。"
   "但實務上鏈結串列<strong>無法隨機存取</strong>，你得先走一遍才知道每組的邊界在哪 —— "
   "那一遍本身就是 O(n) 的序列操作。"
   "<strong>這是鏈結串列相對於陣列的根本劣勢</strong>：對陣列，切成 k 段是 O(1)；對串列，是 O(n)。",
   ("h", "追問三：這題的三個「前置」技巧分別是什麼？"),
   ("ul", [
     "<strong>dummy node</strong>（第 19、21 題）—— 讓頭節點不再是特例",
     "<strong>串列反轉</strong>（第 206 題）—— <code>prev / cur / nxt</code> 三指標",
     "<strong>先量再動</strong>（本題新增）—— 在破壞性操作之前先確認前提",
   ]),
   "<strong>三個都熟的話，這題只是把它們組合起來。</strong>"
   "如果卡住，通常是其中一個不夠熟 —— 回去單練那一題會比硬磨這題有效。",
 ],
 "related": [
   "<strong>第 24 題 Swap Nodes in Pairs</strong> —— k = 2 的特例",
   "<strong>第 206 題 Reverse Linked List</strong> —— 反轉的基本功",
   "<strong>第 92 題 Reverse Linked List II</strong> —— 反轉中間指定的一段",
   "<strong>第 61 題 Rotate List</strong> —— 另一種整段重接",
 ],
 "check": [
   "為什麼「數夠 k 個」一定要在反轉之前做？反轉到一半才發現不夠會怎樣？",
   "反轉迴圈裡 <code>prev = group_next</code>（而不是 <code>None</code>）省掉了哪一行？",
   "迴圈結束後為什麼 <code>group_prev = tail</code> 而不是 <code>kth</code>？",
   "遞迴版在 <code>k = 1</code>、<code>n = 5000</code> 時會發生什麼？為什麼題目的「進階」要求排除了它？",
 ],
})
print("P25 written")

# ==================== 26. Remove Duplicates from Sorted Array ====================
S["p26_two"] = '''class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1                      # 下一個「要寫入」的位置；nums[0] 一定保留
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:     # 和「最後寫進去的那個」不同才寫
                nums[k] = nums[i]
                k += 1
        return k'''

S["p26_prev"] = '''class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        prev = None                # 值域是 -100..100，所以用 None 當「還沒有」
        for x in nums:
            if x != prev:
                nums[k] = x
                k += 1
                prev = x
        return k'''

_p26 = [S.load(k) for k in ("p26_two", "p26_prev")]
for c in [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [], [1], [1, 1, 1],
          [-100, -100, 100]]:
    e = sorted(set(c))
    for sol in _p26:
        a = list(c)
        k = sol.removeDuplicates(a)
        assert k == len(e) and a[:k] == e, ("P26", c, sol, k, a[:k], e)
for _ in range(4000):
    c = sorted(random.randint(-4, 4) for _ in range(random.randint(0, 10)))
    e = sorted(set(c))
    for sol in _p26:
        a = list(c)
        k = sol.removeDuplicates(a)
        assert k == len(e) and a[:k] == e, ("P26", c, sol)
print("P26 solutions OK")

emit({
 "num": 26, "slug": "remove-duplicates-from-sorted-array",
 "en": [
   "Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, "
   "remove the duplicates <strong>in-place</strong> such that each unique element appears only "
   "<strong>once</strong>. The relative order of the elements should be kept the same.",
   "Return <code>k</code> after placing the final result in the first <code>k</code> slots of "
   "<code>nums</code>. It does not matter what you leave beyond the first <code>k</code> elements.",
 ],
 "zh": [
   "給你一個<strong>非遞減排序</strong>的整數陣列 <code>nums</code>，"
   "請<strong>原地</strong>刪除重複的元素，讓每個不同的值只出現<strong>一次</strong>，"
   "並保持原本的相對順序。",
   "回傳去重後的長度 <code>k</code>，而且 <code>nums</code> 的<strong>前 <code>k</code> 個位置</strong>"
   "必須存放最終結果。第 <code>k</code> 個之後的內容是什麼都無所謂。",
 ],
 "pre": [
   ("note", "「原地」和「前 k 個」是兩個獨立的要求", [
     ("c", """輸入：  nums = [0,0,1,1,1,2,2,3,3,4]
輸出：  k = 5
        nums 的前 5 格必須是 [0,1,2,3,4]
        第 6 格之後是什麼都不檢查（通常標記成 _）

        nums = [0,1,2,3,4,_,_,_,_,_]   ✔

常見誤解：
  ✘ 以為要回傳新陣列  -> 不行，必須原地改 nums
  ✘ 以為要把後面清空  -> 不用，後面是什麼都不檢查
  ✘ 用 nums = [...] 重新綁定  -> 沒用！那只改了區域變數，
     呼叫端拿到的還是原本的 list

在 Python 裡要真的「原地」修改，只能用
    nums[i] = x        （逐格賦值）
    nums[:] = [...]    （切片賦值，會改動原物件）
不能寫 nums = [...]。這是 Python 特有的陷阱。"""),
     "<strong>因為陣列已經排序，所有相同的值一定相鄰</strong> —— "
     "所以只要和「前一個保留下來的值」比較就夠了，不需要 set，也不需要 O(n) 額外空間。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,1,2]
  輸出：k = 2，nums = [1,2,_]

範例 2
  輸入：nums = [0,0,1,1,1,2,2,3,3,4]
  輸出：k = 5，nums = [0,1,2,3,4,_,_,_,_,_]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 3 × 10⁴",
   "−100 ≤ <code>nums[i]</code> ≤ 100",
   "<code>nums</code> 已經依<strong>非遞減順序</strong>排好",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>已經排序</strong> —— 這是整題的關鍵。"
       "相同的值一定相鄰，所以「去重」退化成「和前一個比」。"
       "如果沒有排序，就得用 set 或先排序，複雜度和空間都會變。",
       "<strong>長度至少 1</strong>，但寫成能處理空陣列比較安全。",
       "<strong>值域是 −100 到 100</strong>，所以<strong>不能用 0 或 −1 當哨兵</strong>。"
       "解法二用 <code>None</code> 就是為了這個。",
     ]),
   ]),
 ],
 "idea": [
   "<strong>快慢雙指標</strong>：一個負責「讀」（掃過每個元素），一個負責「寫」（記錄下一個要放的位置）。"
   "這是所有「原地過濾」題目的共同模板。",
   ("c", """nums = [0,0,1,1,1,2,2,3,3,4]
         k 指向「下一個要寫入的位置」

i=1: nums[1]=0 == nums[k-1]=nums[0]=0  -> 跳過        k=1
i=2: nums[2]=1 != nums[0]=0            -> nums[1]=1   k=2
i=3: nums[3]=1 == nums[1]=1            -> 跳過        k=2
i=4: nums[4]=1 == nums[1]=1            -> 跳過        k=2
i=5: nums[5]=2 != nums[1]=1            -> nums[2]=2   k=3
i=6: nums[6]=2 == nums[2]=2            -> 跳過        k=3
i=7: nums[7]=3 != nums[2]=2            -> nums[3]=3   k=4
i=8: nums[8]=3 == nums[3]=3            -> 跳過        k=4
i=9: nums[9]=4 != nums[3]=3            -> nums[4]=4   k=5

結果 nums = [0,1,2,3,4,2,3,3,4] 前 5 格正確，回傳 5 ✔
（第 6 格之後是垃圾，但題目不檢查）

注意「寫」永遠不會超前「讀」（k <= i），
所以不會覆蓋掉還沒讀到的資料 —— 這是原地演算法安全的關鍵。"""),
 ],
 "approaches": [
   ap("解法一", "快慢指標，和「最後寫入的值」比較", [
     ("c", S["p26_two"]),
     ("h", "為什麼是 <code>nums[k-1]</code> 而不是 <code>nums[i-1]</code>？"),
     ("c", """兩者在這一題「剛好」都對，但意義不同，而且推廣時會分家。

nums[i-1]：和「原陣列的前一個」比
nums[k-1]：和「已經保留下來的最後一個」比

因為輸入是排序的，兩者等價。
但如果輸入沒有排序，nums[k-1] 的語意才是對的
（「我已經收了哪些」而不是「原本前面是誰」）。

更重要的是第 80 題（每個值最多保留兩次）：
    那題的條件是 nums[i] != nums[k-2]，
    也就是「和已保留的『倒數第二個』比」。
    這時候就完全不能用 i 了。

所以養成用 k 的習慣，推廣時會順很多。"""),
     "<strong><code>k</code> 從 1 開始</strong>，因為第一個元素一定要保留 —— "
     "它沒有「前一個」可以比。",
     "<strong>「寫」永遠不超前「讀」</strong>（<code>k ≤ i</code> 恆成立），"
     "所以 <code>nums[k] = nums[i]</code> 絕不會覆蓋掉還沒讀到的資料。"
     "<strong>這個不變量是所有原地雙指標演算法的安全保證</strong>，值得每次都確認一次。",
   ], "O(n)", "O(1)", "掃一遍", "只用一個下標", optimal=True),

   ap("解法二", "記住上一個值（更容易推廣）", [
     ("c", S["p26_prev"]),
     "語意上更直白：「掃過每個元素，和上一個不同就收下來」。"
     "而且不需要 <code>if not nums</code> 的特判 —— 空陣列的迴圈跑 0 次，直接回 0。",
     "<strong>用 <code>None</code> 而不是某個數字當初值，是刻意的。</strong>"
     "值域包含 −100 到 100，任何具體數字都可能是真實資料。"
     "在 C/Java 裡沒有 <code>None</code>，常見做法是多一個 bool 旗標，"
     "或是像解法一那樣從第二個元素開始跑。",
     "這個版本很容易改成「去重但不要求排序、保留首次出現順序」—— "
     "把 <code>prev</code> 換成一個 <code>set</code> 即可（但那樣就是 O(n) 空間了）。",
   ], "O(n)", "O(1)", "掃一遍", "兩個變數"),
 ],
 "compare": (["解法", "時間", "空間", "需要特判空陣列？", "推廣性"],
   [["一、和 nums[k−1] 比", "O(n)", "O(1)", "要", "容易改成第 80 題"],
    ["二、記住 prev", "O(n)", "O(1)", "不用", "容易改成無序去重"]]),
 "edges": [
   "<strong>空陣列</strong>：<code>[]</code> → 0。題目保證不會有，但別讓程式崩潰。",
   "<strong>只有一個</strong>：<code>[1]</code> → 1。",
   "<strong>全部相同</strong>：<code>[1,1,1]</code> → 1，前 1 格是 <code>[1]</code>。",
   "<strong>完全沒有重複</strong>：<code>[1,2,3]</code> → 3。每一格都會被寫入（寫到自己身上，無害）。",
   "<strong>負數</strong>：<code>[-100,-100,100]</code> → 2。哨兵不能用 0 或 −1。",
   "<strong>Python 陷阱</strong>：寫 <code>nums = [...]</code> 不會改到呼叫端的 list。"
   "要用 <code>nums[i] = x</code> 或 <code>nums[:] = [...]</code>。",
 ],
 "follow": [
   ("h", "追問一：如果每個值最多保留兩次呢？"),
   "第 80 題。只要把條件從 <code>nums[i] != nums[k-1]</code> 改成 "
   "<code>k &lt; 2 or nums[i] != nums[k-2]</code>。"
   "<strong>一般化成「最多保留 m 次」就是 <code>k &lt; m or nums[i] != nums[k-m]</code></strong> —— "
   "同一個模板改一個數字。",
   ("h", "追問二：如果陣列沒有排序呢？"),
   "「保留首次出現順序」的話要用 <code>set</code> 記錄看過的值，空間變 O(n)。"
   "或者先排序（O(n log n)）再用本題的方法 —— 但那樣會破壞原本的順序。"
   "<strong>「已排序」這個前提值多少，從這裡就看得出來。</strong>",
   ("h", "追問三：Python 裡怎麼真的「原地」修改？"),
   ("c", """def f(nums):
    nums = [1, 2, 3]       # ✘ 只改了區域變數，呼叫端看不到

def f(nums):
    nums[:] = [1, 2, 3]    # ✔ 切片賦值，改的是原物件

def f(nums):
    nums[0] = 1            # ✔ 逐格賦值

這個區別在所有「原地」的 LeetCode 題都會遇到
（第 27、80、75、88、189 題…）。
背後是 Python 的「名字綁定 vs 物件變異」——
賦值 (=) 是重新綁定名字，索引賦值 ([i]=) 才是改物件。"""),
 ],
 "related": [
   "<strong>第 27 題 Remove Element</strong> —— 同一個雙指標模板",
   "<strong>第 80 題 Remove Duplicates II</strong> —— 改一個數字的推廣",
   "<strong>第 283 題 Move Zeroes</strong> —— 同樣的「讀寫指標」",
   "<strong>第 283、75、88 題</strong> —— 原地操作家族",
 ],
 "check": [
   "為什麼比較的對象是 <code>nums[k-1]</code> 而不是 <code>nums[i-1]</code>？在什麼題目上會分家？",
   "為什麼 <code>k ≤ i</code> 恆成立？這保證了什麼？",
   "在 Python 裡 <code>nums = [...]</code> 和 <code>nums[:] = [...]</code> 有什麼差別？",
   "如果值域包含所有整數，解法二的 <code>prev</code> 初值該怎麼設？",
 ],
})
print("P26 written")
