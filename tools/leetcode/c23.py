# -*- coding: utf-8 -*-
"""第 23–25 題。"""
import random, heapq
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(23)

# ==================== 23. Merge k Sorted Lists ====================
S["p23_naive"] = '''class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2(a, b):
            dummy = ListNode()
            tail = dummy
            while a and b:
                if a.val <= b.val:
                    tail.next, a = a, a.next
                else:
                    tail.next, b = b, b.next
                tail = tail.next
            tail.next = a if a else b
            return dummy.next

        result = None
        for lst in lists:                # 一條一條併進去
            result = merge2(result, lst)
        return result'''

S["p23_divide"] = '''class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2(a, b):
            dummy = ListNode()
            tail = dummy
            while a and b:
                if a.val <= b.val:
                    tail.next, a = a, a.next
                else:
                    tail.next, b = b, b.next
                tail = tail.next
            tail.next = a if a else b
            return dummy.next

        if not lists:
            return None

        # 每一輪把相鄰兩條配對合併，數量減半，直到只剩一條
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge2(a, b))
            lists = merged

        return lists[0]'''

S["p23_heap"] = '''import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 堆裡永遠只放「每條串列目前的第一個節點」，最多 k 個
        # 第二個元素 i 是 tie-breaker：ListNode 本身無法比大小
        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)

        dummy = ListNode()
        tail = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next'''

_p23 = [S.load(k) for k in ("p23_naive", "p23_divide", "p23_heap")]
for lists in [[[1, 4, 5], [1, 3, 4], [2, 6]], [], [[]], [[], []], [[1]],
              [[], [1], []], [[-10, -9], [-5], [4], [-4], [-1], [-10, 0]]]:
    e = sorted(v for l in lists for v in l)
    for sol in _p23:
        g = from_list(sol.mergeKLists([to_list(l) for l in lists]))
        assert g == e, ("P23", lists, sol, g, e)
for _ in range(2000):
    k = random.randint(0, 5)
    lists = [sorted(random.randint(-9, 9) for _ in range(random.randint(0, 4)))
             for _ in range(k)]
    e = sorted(v for l in lists for v in l)
    for sol in _p23:
        g = from_list(sol.mergeKLists([to_list(l) for l in lists]))
        assert g == e, ("P23", lists, sol, g, e)
print("P23 solutions OK")

_P23_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">分治合併：k = 8 條，每一輪兩兩配對，log₂8 = 3 輪就完成</text>
            <g font-size="11" text-anchor="middle">
              <g fill="var(--accent)">
                <rect x="30" y="40" width="58" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="59" y="57">L0</text>
                <rect x="100" y="40" width="58" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="129" y="57">L1</text>
                <rect x="170" y="40" width="58" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="199" y="57">L2</text>
                <rect x="240" y="40" width="58" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="269" y="57">L3</text>
                <rect x="310" y="40" width="58" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="339" y="57">L4</text>
                <rect x="380" y="40" width="58" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="409" y="57">L5</text>
                <rect x="450" y="40" width="58" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="479" y="57">L6</text>
                <rect x="520" y="40" width="58" height="26" rx="4" fill="none" stroke="var(--accent)"/><text x="549" y="57">L7</text>
              </g>
              <g fill="var(--gold)">
                <rect x="65" y="106" width="58" height="26" rx="4" fill="none" stroke="var(--gold)"/><text x="94" y="123">01</text>
                <rect x="205" y="106" width="58" height="26" rx="4" fill="none" stroke="var(--gold)"/><text x="234" y="123">23</text>
                <rect x="345" y="106" width="58" height="26" rx="4" fill="none" stroke="var(--gold)"/><text x="374" y="123">45</text>
                <rect x="485" y="106" width="58" height="26" rx="4" fill="none" stroke="var(--gold)"/><text x="514" y="123">67</text>
              </g>
              <g fill="#ff8a65">
                <rect x="135" y="172" width="58" height="26" rx="4" fill="none" stroke="#ff8a65"/><text x="164" y="189">0123</text>
                <rect x="415" y="172" width="58" height="26" rx="4" fill="none" stroke="#ff8a65"/><text x="444" y="189">4567</text>
              </g>
              <rect x="275" y="238" width="90" height="26" rx="4" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="320" y="255" fill="var(--accent)">全部合併完成</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.3">
              <line x1="59" y1="66" x2="88" y2="104"/><line x1="129" y1="66" x2="100" y2="104"/>
              <line x1="199" y1="66" x2="228" y2="104"/><line x1="269" y1="66" x2="240" y2="104"/>
              <line x1="339" y1="66" x2="368" y2="104"/><line x1="409" y1="66" x2="380" y2="104"/>
              <line x1="479" y1="66" x2="508" y2="104"/><line x1="549" y1="66" x2="520" y2="104"/>
              <line x1="94" y1="132" x2="158" y2="170"/><line x1="234" y1="132" x2="170" y2="170"/>
              <line x1="374" y1="132" x2="438" y2="170"/><line x1="514" y1="132" x2="450" y2="170"/>
              <line x1="164" y1="198" x2="300" y2="236"/><line x1="444" y1="198" x2="340" y2="236"/>
            </g>
            <text x="20" y="292" fill="var(--gold)" font-size="12">每個節點總共被搬動 log k 次（不是 k 次）→ 總時間 O(n log k)，n 是所有節點的總數</text>'''

emit({
 "num": 23, "slug": "merge-k-sorted-lists",
 "en": [
   "You are given an array of <code>k</code> linked-lists <code>lists</code>, each linked-list "
   "is sorted in ascending order.",
   "<em>Merge all the linked-lists into one sorted linked-list and return it.</em>",
 ],
 "zh": [
   "給你一個長度為 <code>k</code> 的陣列 <code>lists</code>，"
   "裡面每一個元素都是一條<strong>已排序</strong>的鏈結串列。",
   "把它們全部合併成<strong>一條有序的串列</strong>並回傳。",
 ],
 "pre": [
   ("note", "先把兩個變數分清楚", [
     ("c", """k = 串列的條數
n = 所有節點的「總數」（不是每條的長度）

三種解法的複雜度：
    一、依序兩兩併    O(n · k)
    二、分治兩兩配對   O(n · log k)
    三、最小堆        O(n · log k)

注意「依序」和「分治」的差別非常大：

    依序：把第 1 條併進結果、再把第 2 條併進結果…
          結果串列越來越長，每次都要重新走一遍
          第 i 次合併要走 O(i · 平均長度)
          總共 1 + 2 + ... + k = O(k²· 平均長度) = O(n·k)

    分治：兩兩配對，每一輪串列數減半
          每個節點在每一輪最多被搬一次，共 log k 輪
          總共 O(n · log k)

k = 10⁴ 時，O(n·k) 和 O(n·log k) 差了 700 倍以上。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：lists = [[1,4,5],[1,3,4],[2,6]]
  輸出：[1,1,2,3,4,4,5,6]

範例 2
  輸入：lists = []
  輸出：[]

範例 3
  輸入：lists = [[]]
  輸出：[]
  說明：有一條串列，但它是空的。""",
 "constraints": [
   "<code>k == lists.length</code>，0 ≤ <code>k</code> ≤ 10⁴",
   "每條串列的長度在 <code>[0, 500]</code> 之間",
   "−10⁴ ≤ <code>lists[i][j]</code> ≤ 10⁴",
   "每條串列都是<strong>升序</strong>排好的",
   "所有串列的長度總和不超過 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>k 可以到 10⁴，但總節點數 n 也只有 10⁴。</strong>"
       "這表示可能有一萬條串列，大部分是空的或只有一兩個節點。"
       "<strong>所以「k 很大」是真實的威脅，O(n·k) 會 TLE。</strong>",
       "<strong><code>lists</code> 本身可以是空陣列</strong>（<code>k == 0</code>），"
       "<strong>裡面的串列也可以是空的</strong>（<code>[[]]</code>、<code>[[], []]</code>）。"
       "這兩個邊界都要處理。",
       "<strong>值域有負數</strong>，堆的初始值不能用 0。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P23_FIG, "0 0 640 304"),
 ],
 "approaches": [
   ap("解法一", "依序兩兩合併（會 TLE 的基準線）", [
     ("c", S["p23_naive"]),
     ("h", "為什麼是 O(n·k) 而不是 O(n)？"),
     ("c", """假設 k 條串列各有 m 個節點（n = k·m）

第 1 次合併：結果 0 個 + 第 1 條 m 個   -> 走 m 步
第 2 次合併：結果 m 個 + 第 2 條 m 個   -> 走 2m 步
第 3 次合併：結果 2m 個 + 第 3 條 m 個  -> 走 3m 步
...
第 k 次合併：結果 (k-1)m + 第 k 條 m   -> 走 km 步

總共 m(1 + 2 + ... + k) = m · k(k+1)/2 = O(m·k²) = O(n·k)

問題出在：早期合併好的節點，在後面每一輪都被重新走一遍。
節點 1 被走了 k 次！"""),
     "<strong>這就是「重複工作」的典型症狀。</strong>"
     "分治法的所有價值，就在於把「每個節點被走 k 次」降到「被走 log k 次」。",
   ], "O(n·k)", "O(1)", "早期的節點被反覆走過", "只用指標"),

   ap("解法二", "分治：兩兩配對合併（最推薦）", [
     "不要一條一條併進同一個結果，而是<strong>讓所有串列平等地兩兩配對</strong>，"
     "每一輪串列數減半。",
     ("c", S["p23_divide"]),
     ("h", "為什麼是 O(n log k)？"),
     ("c", """第 1 輪： k 條 -> k/2 條，每個節點被搬 1 次，共 O(n)
第 2 輪： k/2 -> k/4，每個節點被搬 1 次，共 O(n)
...
第 log k 輪：2 -> 1，共 O(n)

一共 log k 輪，每輪 O(n)  ->  O(n log k)

關鍵：每一輪裡，每個節點「最多」只被搬動一次
      （它只出現在一次 merge2 呼叫裡）。
      而依序合併時，同一個節點會在多次 merge2 裡被重複走。"""),
     "<strong>這個迴圈版本（而不是遞迴版本）有一個好處</strong>："
     "不吃遞迴堆疊，而且邏輯很直白 —— 就是「反覆對半」。",
     "<strong>要小心的邊界</strong>：串列數是奇數時，最後一條沒有配對的對象，"
     "<code>b = None</code>，而 <code>merge2(a, None)</code> 會正確回傳 <code>a</code>。"
     "這也是為什麼 <code>merge2</code> 要能處理 <code>None</code>。",
   ], "O(n log k)", "O(1)", "log k 輪 × 每輪 O(n)",
      "不算 merged 陣列的話是 O(1)；merged 最多 k/2 個指標", optimal=True),

   ap("解法三", "最小堆（k-way merge 的標準工具）", [
     "維護一個大小最多 <code>k</code> 的最小堆，裡面永遠是「每條串列目前最前面的節點」。"
     "每次取出最小的接到結果後面，再把它的下一個節點推進去。",
     ("c", S["p23_heap"]),
     ("h", "那個 <code>i</code> 是什麼？為什麼一定要有？"),
     ("c", """Python 的 heapq 比較 tuple 時是「逐項比較」：
    先比第 0 項，相等才比第 1 項，依此類推。

如果只放 (node.val, node)：
    當兩個節點的 val 相同時，Python 會去比較 node 本身，
    而 ListNode 沒有定義 __lt__ ->
        TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'

加上 i（串列的索引）當第二項就解決了：
    i 在每條串列裡是固定的，而且各不相同，
    所以 (val, i) 這個 pair 永遠可以比出大小，
    永遠輪不到第三項去比 node。

這是 Python 用 heapq 放物件時的標準做法，
面試時忘記加 i 會直接 runtime error。

另一種做法是給 ListNode 定義 __lt__：
    ListNode.__lt__ = lambda self, other: self.val < other.val
但那是在修改別人的類別，不太乾淨。"""),
     ("h", "為什麼堆的大小最多是 k？"),
     "因為每條串列在任何時刻<strong>只有一個節點在堆裡</strong>。"
     "取出一個就推進它的後繼一個，數量守恆。"
     "所以空間是 O(k)，而不是 O(n)。",
     ("h", "和分治法怎麼選？"),
     ("c", """複雜度完全一樣：O(n log k) 時間。

分治法：  空間 O(1)，常數小，但要自己寫 merge2
堆：      空間 O(k)，常數大（堆操作有額外負擔），但概念最直白

實務上的重要差別：
  堆的做法可以處理「串列是無限長的串流」——
  它不需要知道總長度，隨時可以停下來。
  分治法必須先看到所有資料。

這正是資料庫做 k 路歸併排序（external merge sort）時
用「堆」而不是「分治」的原因。"""),
   ], "O(n log k)", "O(k)", "n 次 pop/push，每次 O(log k)", "堆裡最多 k 個節點"),
 ],
 "compare": (["解法", "時間", "空間", "k=10⁴ 能過？", "適合的場景"],
   [["一、依序合併", "O(n·k)", "O(1)", "✘", "只當反例"],
    ["二、分治配對", "O(n log k)", "O(1)", "✔", "一次性、資料都在手上"],
    ["三、最小堆", "O(n log k)", "O(k)", "✔", "串流、外部排序"]]),
 "edges": [
   "<strong><code>lists</code> 是空陣列</strong>：<code>[]</code> → <code>[]</code>。"
   "分治版的 <code>if not lists: return None</code> 就是為它；堆版本的 heap 是空的，自然回 <code>None</code>。",
   "<strong>只有一條串列</strong>：<code>[[1]]</code> → <code>[1]</code>。分治版的 while 一次都不跑。",
   "<strong>所有串列都是空的</strong>：<code>[[], []]</code> → <code>[]</code>。",
   "<strong>部分為空</strong>：<code>[[], [1], []]</code> → <code>[1]</code>。"
   "堆版本的 <code>if node</code> 過濾就是為它。",
   "<strong>值相同跨串列</strong>：<code>[[1],[1],[1]]</code> → <code>[1,1,1]</code>。"
   "堆版本沒加 tie-breaker <code>i</code> 的話會在這裡 TypeError。",
   "<strong>k 很大但節點很少</strong>：10000 條空串列 + 1 條有 1 個節點。"
   "分治版要跑 log(10000) ≈ 14 輪，每輪幾乎什麼都不做 —— 仍然很快。",
   "<strong>負數</strong>：<code>[[-10,-9],[-5],[4]]</code>。",
 ],
 "follow": [
   ("h", "追問一：如果串列是無限長的串流呢？"),
   "只能用堆。分治法需要「知道整條串列」才能合併，"
   "而堆隨時只看每條串列的第一個元素。"
   "<strong>這是資料庫和搜尋引擎做 k 路歸併的標準架構</strong>："
   "k 個已排序的檔案（或 posting list），用一個大小 k 的堆邊讀邊輸出。",
   ("h", "追問二：如果是陣列而不是串列呢？"),
   "堆的做法完全一樣（把「節點」換成「(陣列索引, 位置)」）。"
   "分治的做法要小心：陣列的 merge 需要 O(m+n) 的額外空間，"
   "所以總空間會是 O(n) 而不是 O(1)。",
   ("h", "追問三：有沒有辦法做到比 O(n log k) 更快？"),
   "<strong>沒有（在比較模型下）。</strong>"
   "因為 k 路歸併可以拿來排序：把 n 個元素各自當成一條長度 1 的串列，"
   "k = n，複雜度就是 O(n log n) —— 這正好是比較排序的下界。"
   "所以 O(n log k) 是最優的。"
   "<strong>「用歸約（reduction）證明下界」是很漂亮的論證，面試時講出來會加分。</strong>",
   ("h", "追問四：如果 k 條串列的長度差很多呢？"),
   "分治法會有一點浪費（短的很快就併完，但還是要參與每一輪配對）。"
   "更好的做法是<strong>哈夫曼式的合併</strong>：每次挑「目前最短的兩條」來合併。"
   "這能讓總搬動次數最小 —— 和哈夫曼編碼是同一個貪婪原理。"
   "不過在 LeetCode 的測資上差別不大。",
 ],
 "related": [
   "<strong>第 21 題 Merge Two Sorted Lists</strong> —— 這題的基本單元",
   "<strong>第 148 題 Sort List</strong> —— 用 merge 做串列排序",
   "<strong>第 378 題 Kth Smallest in Sorted Matrix</strong> —— 堆的 k 路歸併變形",
   "<strong>第 373 題 Find K Pairs with Smallest Sums</strong> —— 同樣的堆技巧",
 ],
 "check": [
   "「依序合併」和「分治合併」都是做 k−1 次 merge2，為什麼複雜度差這麼多？",
   "堆版本裡的 <code>i</code> 如果拿掉，什麼輸入會 TypeError？為什麼？",
   "堆的大小為什麼最多是 k 而不是 n？",
   "為什麼 O(n log k) 是這題的下界？（提示：把它歸約到排序）",
 ],
})
print("P23 written")

# ==================== 24. Swap Nodes in Pairs ====================
S["p24_iter"] = '''class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        # 只要還有「兩個」節點可以交換
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # 三條線重接：prev -> second -> first -> (second 原本的下一個)
            first.next = second.next
            second.next = first
            prev.next = second

            prev = first        # first 現在在後面，它是下一對的「前一個」

        return dummy.next'''

S["p24_rec"] = '''class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 不足兩個就不用換
        if not head or not head.next:
            return head

        second = head.next
        head.next = self.swapPairs(second.next)   # 後面的先換好，再接上來
        second.next = head

        return second        # 換完之後 second 變成這一段的頭'''

S["p24_valswap"] = '''class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 只交換「值」而不動指標 —— 題目通常不允許，這裡列出來當對照
        node = head
        while node and node.next:
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head'''

_p24 = [S.load(k) for k in ("p24_iter", "p24_rec", "p24_valswap")]


def _p24_ref(vals):
    out = list(vals)
    for i in range(0, len(out) - 1, 2):
        out[i], out[i + 1] = out[i + 1], out[i]
    return out


for vals in [[1, 2, 3, 4], [], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4, 5]]:
    e = _p24_ref(vals)
    for sol in _p24:
        assert from_list(sol.swapPairs(to_list(vals))) == e, ("P24", vals, sol)
for _ in range(3000):
    vals = list(range(random.randint(0, 9)))
    e = _p24_ref(vals)
    for sol in _p24:
        assert from_list(sol.swapPairs(to_list(vals))) == e, ("P24", vals, sol)
print("P24 solutions OK")

_P24_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">交換一對節點：三條指標要按正確順序重接</text>
            <text x="20" y="48" fill="var(--text-muted)" font-size="12">交換前</text>
            <g font-size="14" text-anchor="middle">
              <rect x="60" y="62" width="64" height="38" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/>
              <text x="92" y="86" fill="var(--text-muted)" font-size="11">prev</text>
              <rect x="180" y="62" width="64" height="38" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="212" y="87" fill="var(--accent)">1</text>
              <rect x="300" y="62" width="64" height="38" rx="6" fill="none" stroke="var(--gold)" stroke-width="2"/>
              <text x="332" y="87" fill="var(--gold)">2</text>
              <rect x="420" y="62" width="64" height="38" rx="6" fill="none" stroke="var(--border)"/>
              <text x="452" y="87" fill="var(--text-muted)">3</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.6">
              <line x1="124" y1="81" x2="176" y2="81"/>
              <line x1="244" y1="81" x2="296" y2="81"/>
              <line x1="364" y1="81" x2="416" y2="81"/>
            </g>
            <text x="212" y="116" fill="var(--accent)" font-size="11" text-anchor="middle">first</text>
            <text x="332" y="116" fill="var(--gold)" font-size="11" text-anchor="middle">second</text>

            <text x="20" y="162" fill="var(--text-muted)" font-size="12">交換後</text>
            <g font-size="14" text-anchor="middle">
              <rect x="60" y="176" width="64" height="38" rx="6" fill="none" stroke="var(--border)" stroke-dasharray="4 3"/>
              <text x="92" y="200" fill="var(--text-muted)" font-size="11">prev</text>
              <rect x="180" y="176" width="64" height="38" rx="6" fill="none" stroke="var(--gold)" stroke-width="2"/>
              <text x="212" y="201" fill="var(--gold)">2</text>
              <rect x="300" y="176" width="64" height="38" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="332" y="201" fill="var(--accent)">1</text>
              <rect x="420" y="176" width="64" height="38" rx="6" fill="none" stroke="var(--border)"/>
              <text x="452" y="201" fill="var(--text-muted)">3</text>
            </g>
            <g stroke="var(--gold)" stroke-width="1.8">
              <line x1="124" y1="195" x2="176" y2="195"/>
              <line x1="244" y1="195" x2="296" y2="195"/>
              <line x1="364" y1="195" x2="416" y2="195"/>
            </g>
            <text x="332" y="230" fill="var(--accent)" font-size="11" text-anchor="middle">prev 的新位置</text>
            <text x="20" y="266" fill="var(--gold)" font-size="12">① first.next = second.next（1→3）　② second.next = first（2→1）　③ prev.next = second</text>
            <text x="20" y="288" fill="#ff8a65" font-size="12">順序不能亂：先做 ③ 的話就找不到原本的 first 了。</text>'''

emit({
 "num": 24, "slug": "swap-nodes-in-pairs",
 "en": [
   "Given a linked list, swap every two adjacent nodes and return its head.",
   "You must solve the problem without modifying the values in the list's nodes "
   "(i.e., only nodes themselves may be changed).",
 ],
 "zh": [
   "給你一條鏈結串列，<strong>兩兩交換</strong>相鄰的節點，回傳交換後的頭節點。",
   "<strong>你不能修改節點的值</strong>，只能改變節點之間的連接（也就是必須真的動指標）。",
 ],
 "pre": [
   ("note", "「不能改值」這句話就是全題的重點", [
     "如果可以改值，這題兩行就結束了（見解法三）。"
     "題目特別禁止，是因為它想考<strong>指標重接</strong>。",
     ("c", """為什麼真實世界會在意這個限制？

在很多場景裡，「節點」不只是一個值：
  - 節點可能很大（裡面有一整筆記錄），複製成本高
  - 可能有外部指標指向某個節點，交換值會讓那些指標指錯東西
  - 節點可能是不可變的（immutable）

所以「重接指標」是 O(1) 的操作，
「複製整個節點的內容」可能是 O(節點大小)。

這個區別在資料庫的 B-tree、作業系統的 free list 裡都很關鍵。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [1,2,3,4]
  輸出：[2,1,4,3]

範例 2
  輸入：head = []
  輸出：[]

範例 3
  輸入：head = [1]
  輸出：[1]
  說明：只有一個節點，沒有對象可以交換。

範例 4
  輸入：head = [1,2,3]
  輸出：[2,1,3]
  說明：最後落單的 3 保持原位。""",
 "constraints": [
   "節點數在 <code>[0, 100]</code> 範圍內（<strong>可以是空串列</strong>）",
   "0 ≤ <code>Node.val</code> ≤ 100",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>節點數可以是 0</strong>，所以不能無條件存取 <code>head.val</code>。",
       "<strong>節點數可以是奇數</strong>，最後那個落單的節點<strong>保持原位</strong>，不動它。",
       "規模只有 100，效率完全不是重點。這題純粹考<strong>指標操作</strong>。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P24_FIG, "0 0 640 300"),
   "迴圈版和遞迴版都很短。遞迴版只有 6 行，但迴圈版是 O(1) 空間 —— 兩個都該會。",
 ],
 "approaches": [
   ap("解法一", "迴圈 + dummy（標準解）", [
     ("c", S["p24_iter"]),
     ("h", "三條線的重接順序"),
     ("c", """交換前：  prev -> first -> second -> rest

① first.next = second.next      first -> rest       （先保住 rest）
② second.next = first           second -> first
③ prev.next = second            prev -> second

交換後：  prev -> second -> first -> rest  ✔

為什麼順序不能亂？

  如果先做 ③（prev.next = second），
  那 prev 就不再指向 first 了 ——
  但我們已經把 first 存在區域變數裡，其實還找得到。

  真正致命的是：如果先做 ②（second.next = first），
  就會蓋掉 second 原本指向的 rest，
  ① 再去讀 second.next 就會拿到 first，形成一個環！

    first -> first -> first -> ...  無限迴圈

實務上的安全做法：先把所有「等下會用到的指標」存進區域變數，
再開始改。上面的程式碼就是這樣寫的（first、second 都先存好）。"""),
     ("h", "為什麼結束後 <code>prev = first</code> 而不是 <code>prev = second</code>？"),
     "因為交換之後 <code>first</code> 跑到了後面。"
     "下一對的「前一個節點」是 <code>first</code>，不是 <code>second</code>。"
     "<strong>這是最容易寫錯的一行</strong> —— 寫成 <code>second</code> 的話 <code>prev</code> 沒有前進，會變成無限迴圈。",
     ("h", "while 條件為什麼要檢查兩個？"),
     "<code>prev.next</code>：還有節點嗎？<code>prev.next.next</code>：還有<strong>第二個</strong>節點嗎？"
     "少了任一個，奇數長度的串列或空串列就會崩潰。"
     "而且順序不能顛倒 —— Python 的 <code>and</code> 短路求值保證了"
     "<code>prev.next</code> 是 <code>None</code> 時不會去讀 <code>.next</code>。",
   ], "O(n)", "O(1)", "每個節點處理一次", "只用幾個指標", optimal=True),

   ap("解法二", "遞迴（最短）", [
     ("c", S["p24_rec"]),
     "語意非常清楚：<strong>「換掉前兩個，然後把『後面換好的結果』接到第一個節點後面。」</strong>",
     ("c", """swapPairs([1,2,3,4])
    second = 2
    head(1).next = swapPairs([3,4])
                     second = 4
                     head(3).next = swapPairs([]) = None
                     4.next = 3
                     return 4   ->  [4,3]
    所以 1.next = [4,3] 的頭，也就是 4
    2.next = 1
    return 2   ->  [2,1,4,3] ✔"""),
     "<strong>終止條件 <code>not head or not head.next</code></strong> 同時處理了"
     "「空串列」和「只剩一個節點」，回傳 <code>head</code> 本身 —— 不足兩個就原封不動。",
     "<strong>不需要 dummy</strong>，因為「這一段的新頭是誰」就是回傳值。",
     "缺點一樣是 O(n) 的堆疊深度。n = 100 沒問題。",
   ], "O(n)", "O(n)", "每對一層遞迴", "遞迴堆疊"),

   ap("解法三", "只交換值（題目禁止，列出來當對照）", [
     ("c", S["p24_valswap"]),
     "<strong>兩行就結束。</strong>邏輯上「輸出」完全正確，"
     "但它違反了題目的要求，而且在真實場景下可能有嚴重問題（見最上面的說明）。",
     "<strong>為什麼還要看它？</strong>因為它讓你清楚看出：<strong>這題的難度完全來自那條限制。</strong>"
     "拿掉限制，問題是 Easy；加上限制，才需要練指標重接。"
     "面試時值得主動說一句「如果可以改值的話兩行就好，但題目不允許」—— "
     "這顯示你理解了限制存在的理由。",
   ], "O(n)", "O(1)", "掃一遍", "只用一個指標"),
 ],
 "compare": (["解法", "時間", "空間", "符合題目要求？", "備註"],
   [["一、迴圈 + dummy", "O(n)", "O(1)", "✔", "標準解"],
    ["二、遞迴", "O(n)", "O(n)", "✔", "最短最好讀"],
    ["三、交換值", "O(n)", "O(1)", "✘", "只當對照"]]),
 "edges": [
   "<strong>空串列</strong>：<code>[]</code> → <code>[]</code>。",
   "<strong>只有一個</strong>：<code>[1]</code> → <code>[1]</code>。",
   "<strong>剛好兩個</strong>：<code>[1,2]</code> → <code>[2,1]</code>。",
   "<strong>奇數長度</strong>：<code>[1,2,3]</code> → <code>[2,1,3]</code>。最後一個不動。",
   "<strong>偶數長度</strong>：<code>[1,2,3,4]</code> → <code>[2,1,4,3]</code>。",
   "<strong><code>prev = second</code> 的錯誤</strong>：會造成無限迴圈（<code>prev</code> 沒前進）。",
   "<strong>重接順序錯誤</strong>：先寫 <code>second.next = first</code> 會製造出自環，"
   "<code>from_list</code> 之類的檢查會卡死。",
 ],
 "follow": [
   ("h", "追問一：如果是每 k 個一組反轉呢？"),
   "那就是第 25 題（Reverse Nodes in k-Group），Hard。"
   "這題是 k = 2 的特例。"
   "一般化之後不能再用「三條線」硬寫，要先數夠 k 個，再反轉那一段，"
   "然後把前後接回去。<strong>建議把這兩題連著練。</strong>",
   ("h", "追問二：如果最後不足 k 個要反轉呢？"),
   "第 25 題的變體。差別只在「數不夠 k 個」時是 return 還是照樣反轉。"
   "面試時一定要先問清楚這一點。",
   ("h", "追問三：為什麼題目要禁止交換值？"),
   "除了前面說的「節點可能很大／可能有外部參照」之外，"
   "還有一個教學上的理由：<strong>指標重接是鏈結串列的核心技能</strong>，"
   "而交換值會讓你完全繞過它。"
   "第 25、92、206 這些題都在練同一件事 —— "
   "<strong>在只能往前走的結構上，安全地改變連接順序</strong>。",
 ],
 "related": [
   "<strong>第 25 題 Reverse Nodes in k-Group</strong> —— 一般化版本",
   "<strong>第 206 題 Reverse Linked List</strong> —— 指標重接的最基本練習",
   "<strong>第 92 題 Reverse Linked List II</strong> —— 反轉中間一段",
   "<strong>第 328 題 Odd Even Linked List</strong> —— 另一種重接練習",
 ],
 "check": [
   "三條指標的重接如果先做 <code>second.next = first</code>，會發生什麼？請畫出結果。",
   "迴圈結束時為什麼是 <code>prev = first</code>？寫成 <code>prev = second</code> 會怎樣？",
   "while 的兩個條件各自防的是哪一種輸入？能不能交換順序？",
   "遞迴版為什麼不需要 dummy node？",
 ],
})
print("P24 written")
