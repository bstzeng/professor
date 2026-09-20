# -*- coding: utf-8 -*-
"""第 21–23 題。"""
import random, heapq
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(21)

# ==================== 21. Merge Two Sorted Lists ====================
S["p21_iter"] = '''class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # 虛擬頭：省掉「第一個節點從哪來」的判斷
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:      # <= 而不是 < ：維持穩定性
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # 其中一條走完了，把另一條剩下的整段接上去
        tail.next = list1 if list1 else list2

        return dummy.next'''

S["p21_rec"] = '''class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2'''

_p21 = [S.load(k) for k in ("p21_iter", "p21_rec")]
for a, b in [([1, 2, 4], [1, 3, 4]), ([], []), ([], [0]), ([5], [1, 2, 4]),
             ([1, 1, 1], [1, 1])]:
    e = sorted(a + b)
    for sol in _p21:
        assert from_list(sol.mergeTwoLists(to_list(a), to_list(b))) == e, ("P21", a, b, sol)
for _ in range(4000):
    a = sorted(random.randint(-8, 8) for _ in range(random.randint(0, 6)))
    b = sorted(random.randint(-8, 8) for _ in range(random.randint(0, 6)))
    e = sorted(a + b)
    for sol in _p21:
        assert from_list(sol.mergeTwoLists(to_list(a), to_list(b))) == e, ("P21", a, b, sol)
print("P21 solutions OK")

emit({
 "num": 21, "slug": "merge-two-sorted-lists",
 "en": [
   "You are given the heads of two sorted linked lists <code>list1</code> and "
   "<code>list2</code>.",
   "Merge the two lists into one <strong>sorted</strong> list. The list should be made by "
   "splicing together the nodes of the first two lists. Return the head of the merged "
   "linked list.",
 ],
 "zh": [
   "給你兩條<strong>已排序</strong>的鏈結串列的頭節點 <code>list1</code> 和 <code>list2</code>。",
   "把它們合併成一條<strong>仍然有序</strong>的串列。"
   "合併時要<strong>重新接原本的節點</strong>（splice），不是建新節點。回傳合併後的頭節點。",
 ],
 "pre": [
   ("note", "這是 merge sort 的「merge」步驟", [
     "如果你寫過合併排序，這題就是它的核心步驟搬到鏈結串列上。",
     ("c", """list1: 1 -> 2 -> 4
list2: 1 -> 3 -> 4

兩個指標各指一條的開頭，每次挑小的接到結果後面：

    比 1 vs 1  -> 接 list1 的 1（<= 所以選前面那條）
    比 2 vs 1  -> 接 list2 的 1
    比 2 vs 3  -> 接 2
    比 4 vs 3  -> 接 3
    比 4 vs 4  -> 接 list1 的 4
    list1 空了 -> 把 list2 剩下的 4 整段接上

結果： 1 -> 1 -> 2 -> 3 -> 4 -> 4"""),
     "<strong>鏈結串列版本比陣列版本更漂亮</strong>：陣列要開一個新陣列存結果，"
     "串列只要改指標，<strong>額外空間是 O(1)</strong>。這正是題目說「splice together」的意思。",
   ]),
 ],
 "examples": """範例 1
  輸入：list1 = [1,2,4], list2 = [1,3,4]
  輸出：[1,1,2,3,4,4]

範例 2
  輸入：list1 = [], list2 = []
  輸出：[]

範例 3
  輸入：list1 = [], list2 = [0]
  輸出：[0]""",
 "constraints": [
   "兩條串列的節點數都在 <code>[0, 50]</code> 範圍內（<strong>可以是空的</strong>）",
   "−100 ≤ <code>Node.val</code> ≤ 100",
   "<code>list1</code> 和 <code>list2</code> 都是<strong>非遞減排序</strong>的",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>兩條都可能是空的</strong>。三種情況（兩空、一空、都不空）都要對。",
       "<strong>是「非遞減」不是「嚴格遞增」</strong>，所以值可以重複。"
       "這就是為什麼比較要用 <code>&lt;=</code> 而不是 <code>&lt;</code>（見下面的說明）。",
       "規模只有 50，效率不是重點。這題考的是<strong>指標操作的乾淨度</strong>，"
       "是鏈結串列題的入門必修。",
     ]),
   ]),
 ],
 "idea": [
   "迴圈版和遞迴版都很短，兩個都應該會。"
   "迴圈版空間 O(1)、遞迴版 O(n)，但遞迴版只有 8 行且完全不需要 dummy。",
 ],
 "approaches": [
   ap("解法一", "迴圈 + 虛擬頭節點（標準解）", [
     ("c", S["p21_iter"]),
     ("h", "dummy 到底省掉了什麼？"),
     ("c", """沒有 dummy 的寫法：

    if not list1: return list2
    if not list2: return list1
    if list1.val <= list2.val:
        head = list1; list1 = list1.next
    else:
        head = list2; list2 = list2.next
    tail = head
    while ...

    要先決定「頭是誰」，寫四行只為了處理第一個節點。

有 dummy 的寫法：
    dummy = ListNode(); tail = dummy
    while ...

    第一個節點和後面的節點走完全一樣的邏輯，
    最後 return dummy.next 就好。

dummy 的本質：製造一個「一定存在的前一個節點」，
讓「頭」不再是特例。"""),
     ("h", "最後那一行 <code>tail.next = list1 if list1 else list2</code>"),
     "迴圈結束表示至少有一條走完了。剩下的那條<strong>本身就已經排好序，而且全部都比已接上的大</strong>，"
     "所以可以<strong>整段直接接上</strong>，不用一個一個接。"
     "這是鏈結串列相對於陣列的優勢 —— O(1) 的「接上剩下全部」。",
     "如果兩條都走完了，<code>list1</code> 和 <code>list2</code> 都是 <code>None</code>，"
     "接上 <code>None</code> 剛好就是正確的結尾。<strong>這一行同時處理了三種情況。</strong>",
     ("h", "為什麼是 <code>&lt;=</code> 而不是 <code>&lt;</code>？"),
     ("c", """值相等時：
    <= ：選 list1 的  ->  穩定（stable）
    <  ：選 list2 的  ->  不穩定

在這題（只比數值）兩者的輸出完全一樣，看不出差別。

但如果節點帶著其他資料（例如 (分數, 學生名字)），
「穩定」表示分數相同時，原本排在前面的那條串列的元素仍然排在前面。

merge sort 之所以是穩定排序，關鍵就在這個 <=。
改成 < 就會變成不穩定排序 —— 一個字元的差別。"""),
   ], "O(m+n)", "O(1)", "每個節點處理一次", "只用幾個指標，沒有新節點", optimal=True),

   ap("解法二", "遞迴（最短的寫法）", [
     ("c", S["p21_rec"]),
     "遞迴式的語意非常直白：<strong>「兩個頭裡比較小的那個，就是合併結果的頭；"
     "它的 next 是『剩下的部分合併起來』。」</strong>",
     ("c", """merge([1,2,4], [1,3,4])
  1 <= 1 -> 取 list1 的 1
  1.next = merge([2,4], [1,3,4])
             2 > 1 -> 取 list2 的 1
             1.next = merge([2,4], [3,4])
                        2 <= 3 -> 取 2
                        2.next = merge([4], [3,4])
                                   4 > 3 -> 取 3
                                   3.next = merge([4], [4])
                                              4 <= 4 -> 取 list1 的 4
                                              4.next = merge([], [4])
                                                         list1 空 -> return [4]
結果：1 -> 1 -> 2 -> 3 -> 4 -> 4 ✔"""),
     "<strong>不需要 dummy</strong>，因為「頭是誰」就是遞迴函式的回傳值。",
     "<strong>缺點是 O(m+n) 的遞迴堆疊。</strong>"
     "這題節點數只有 50，完全不是問題；但如果是 10⁵ 個節點，Python 會 "
     "<code>RecursionError</code>。面試時主動提這一點。",
   ], "O(m+n)", "O(m+n)", "每個節點一層遞迴", "遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、迴圈 + dummy", "O(m+n)", "O(1)", "14", "面試預設；O(1) 空間"],
    ["二、遞迴", "O(m+n)", "O(m+n)", "8", "最短最好讀；注意堆疊深度"]]),
 "edges": [
   "<strong>兩條都空</strong>：<code>([], [])</code> → <code>[]</code>。",
   "<strong>一條空</strong>：<code>([], [0])</code>、<code>([0], [])</code> → <code>[0]</code>。",
   "<strong>完全不重疊</strong>：<code>([5], [1,2,4])</code> → <code>[1,2,4,5]</code>。"
   "驗證「一條走完後整段接上」。",
   "<strong>全部相同</strong>：<code>([1,1,1], [1,1])</code> → <code>[1,1,1,1,1]</code>。"
   "驗證 <code>&lt;=</code> 不會死循環。",
   "<strong>長度差很多</strong>：<code>([1], [2,3,4,5,6])</code>。",
   "<strong>負數</strong>：<code>([-100], [100])</code>。值域有負數，不要用 0 當哨兵。",
 ],
 "follow": [
   ("h", "追問一：合併 k 條呢？"),
   "第 23 題。三種做法：兩兩依序合併 O(kn)、<strong>分治兩兩配對</strong> O(n log k)、"
   "<strong>最小堆</strong> O(n log k)。詳見下一題。",
   ("h", "追問二：如果不能修改原本的節點（要建新的）呢？"),
   "把 <code>tail.next = list1</code> 改成 <code>tail.next = ListNode(list1.val)</code>，"
   "並且最後不能整段接上、要一個一個複製。"
   "空間從 O(1) 變成 O(m+n)。<strong>題目明說可以 splice，所以我們用 O(1) 的版本。</strong>",
   ("h", "追問三：這個 merge 和陣列版的 merge 有什麼不同？"),
   ("c", """陣列版：
    需要一個大小 m+n 的新陣列（不能就地做，會蓋掉還沒讀的資料）
    空間 O(m+n)

串列版：
    只改指標，空間 O(1)
    而且「把剩下的整段接上」是 O(1) 而不是 O(剩餘長度)

這就是為什麼 merge sort 在鏈結串列上特別漂亮：
陣列版的 merge sort 需要 O(n) 額外空間，
串列版只需要 O(log n)（遞迴堆疊），
而且不需要隨機存取 —— 這也是外部排序（資料大到放不進記憶體）
用 merge sort 而不是 quick sort 的原因。"""),
 ],
 "related": [
   "<strong>第 23 題 Merge k Sorted Lists</strong> —— 推廣到 k 條",
   "<strong>第 88 題 Merge Sorted Array</strong> —— 陣列版，要從後往前寫",
   "<strong>第 148 題 Sort List</strong> —— 用這個 merge 實作串列的 merge sort",
 ],
 "check": [
   "dummy node 具體省掉了哪幾行程式碼？沒有它要怎麼寫？",
   "最後一行 <code>tail.next = list1 if list1 else list2</code> 處理了哪三種情況？",
   "<code>&lt;=</code> 改成 <code>&lt;</code> 會讓輸出改變嗎？「穩定性」在什麼情況下才看得出差別？",
   "遞迴版的空間是 O(m+n)，迴圈版是 O(1)。什麼時候這個差別會變成真正的問題？",
 ],
})
print("P21 written")

# ==================== 22. Generate Parentheses ====================
S["p22_backtrack"] = '''class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        path = []

        def backtrack(open_used: int, close_used: int) -> None:
            if len(path) == 2 * n:
                out.append("".join(path))
                return

            # 規則 1：左括號還沒用完就可以放
            if open_used < n:
                path.append("(")
                backtrack(open_used + 1, close_used)
                path.pop()

            # 規則 2：右括號數量必須「嚴格少於」左括號，才可以放
            if close_used < open_used:
                path.append(")")
                backtrack(open_used, close_used + 1)
                path.pop()

        backtrack(0, 0)
        return out'''

S["p22_bruteforce"] = '''class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def valid(s: str) -> bool:
            bal = 0
            for ch in s:
                bal += 1 if ch == "(" else -1
                if bal < 0:          # 右括號比左括號多 -> 不合法
                    return False
            return bal == 0

        out = []

        def gen(cur: str) -> None:
            if len(cur) == 2 * n:
                if valid(cur):
                    out.append(cur)
                return
            gen(cur + "(")
            gen(cur + ")")

        gen("")
        return out'''

S["p22_closure"] = '''class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 每個合法序列都能唯一分解成  "(" + A + ")" + B
        # 其中 A 有 i 對、B 有 n-1-i 對
        memo = {0: [""]}

        def gen(k: int) -> List[str]:
            if k in memo:
                return memo[k]
            res = []
            for i in range(k):
                for a in gen(i):            # 第一個括號「裡面」的部分
                    for b in gen(k - 1 - i):  # 第一個括號「後面」的部分
                        res.append("(" + a + ")" + b)
            memo[k] = res
            return res

        return gen(n)'''

_p22 = [S.load(k) for k in ("p22_backtrack", "p22_bruteforce", "p22_closure")]
_CAT = [1, 1, 2, 5, 14, 42, 132, 429, 1430]
for n in range(0, 8):
    e = sorted(_p22[0].generateParenthesis(n))
    assert len(e) == _CAT[n], ("P22 count", n, len(e), _CAT[n])
    for sol in _p22:
        g = sorted(sol.generateParenthesis(n))
        assert g == e, ("P22", n, sol, len(g), len(e))
assert sorted(_p22[0].generateParenthesis(3)) == sorted(
    ["((()))", "(()())", "(())()", "()(())", "()()()"])
print("P22 solutions OK")

_P22_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">n = 2 的搜尋樹：灰色虛線是被剪掉的分支（右括號不能超過左括號）</text>
            <g font-size="12" text-anchor="middle" font-family="monospace">
              <text x="320" y="46" fill="var(--gold)">&quot;&quot;</text>
              <text x="190" y="96" fill="var(--accent)">&quot;(&quot;</text>
              <text x="470" y="96" fill="var(--text-muted)" opacity="0.45">&quot;)&quot;</text>
              <text x="110" y="146" fill="var(--accent)">&quot;((&quot;</text>
              <text x="280" y="146" fill="var(--accent)">&quot;()&quot;</text>
              <text x="110" y="196" fill="var(--text-muted)" opacity="0.45">&quot;((( &quot;</text>
              <text x="200" y="196" fill="var(--accent)">&quot;(()&quot;</text>
              <text x="280" y="196" fill="var(--accent)">&quot;()(&quot;</text>
              <text x="370" y="196" fill="var(--text-muted)" opacity="0.45">&quot;())&quot;</text>
              <text x="200" y="246" fill="#ff8a65">&quot;(())&quot;</text>
              <text x="310" y="246" fill="#ff8a65">&quot;()()&quot;</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.4">
              <line x1="306" y1="54" x2="204" y2="84"/>
              <line x1="180" y1="104" x2="120" y2="134"/>
              <line x1="200" y1="104" x2="272" y2="134"/>
              <line x1="112" y1="154" x2="196" y2="184"/>
              <line x1="282" y1="154" x2="282" y2="184"/>
              <line x1="202" y1="204" x2="202" y2="234"/>
              <line x1="288" y1="204" x2="306" y2="234"/>
            </g>
            <g stroke="var(--border)" stroke-width="1.2" stroke-dasharray="4 4" opacity="0.5">
              <line x1="336" y1="54" x2="456" y2="84"/>
              <line x1="105" y1="154" x2="105" y2="184"/>
              <line x1="292" y1="154" x2="362" y2="184"/>
            </g>
            <text x="512" y="96" fill="var(--text-muted)" font-size="11">✘ 開頭不能是 )</text>
            <text x="110" y="216" fill="var(--text-muted)" font-size="11">✘ 左括號超過 n</text>
            <text x="402" y="196" fill="var(--text-muted)" font-size="11">✘ 右 &gt; 左</text>
            <text x="20" y="282" fill="var(--gold)" font-size="12">n = 2 的答案只有 2 個。若不剪枝，要生成 2⁴ = 16 個字串再逐一驗證。</text>'''

emit({
 "num": 22, "slug": "generate-parentheses",
 "en": [
   "Given <code>n</code> pairs of parentheses, write a function to generate all combinations "
   "of <strong>well-formed</strong> parentheses.",
 ],
 "zh": [
   "給你 <code>n</code> 對括號，寫一個函式生成所有<strong>合法</strong>的括號組合。",
 ],
 "pre": [
   ("note", "合法的判準只有兩條", [
     ("c", """一個由 n 個 '(' 和 n 個 ')' 組成的字串，合法的充要條件是：

  1. 從左到右掃描時，任何前綴裡「右括號數量 ≤ 左括號數量」
  2. 總數相等（各 n 個）

第 1 條就是「不能先關一個還沒開的括號」。

  "(()"   前綴都合法，但總數不對（第 2 條不滿足）
  "())("  掃到第 3 個字元時右 > 左（第 1 條不滿足）
  "(())"  兩條都滿足 ✔

把這兩條直接寫進「什麼時候可以放括號」的條件裡，
就不會生出任何不合法的字串 —— 這就是剪枝。"""),
     "<strong>這題和第 20 題（Valid Parentheses）是一體兩面</strong>："
     "第 20 題是「驗證」，這題是「生成」。"
     "而且因為只有一種括號，驗證的堆疊退化成一個計數器。",
   ]),
 ],
 "examples": """範例 1
  輸入：n = 3
  輸出：["((()))","(()())","(())()","()(())","()()()"]

範例 2
  輸入：n = 1
  輸出：["()"]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 8",
 ],
 "mid": [
   ("note", "答案有幾個？卡塔蘭數", [
     ("c", """n 對括號的合法組合數 = 第 n 個卡塔蘭數（Catalan number）

    C_n = C(2n, n) / (n + 1)

    n:   0   1   2   3   4    5    6    7     8
    C_n: 1   1   2   5   14   42   132  429   1430

所以 n = 8 時只有 1430 個答案 —— 非常小。

如果不剪枝，要生成 2^(2n) = 2^16 = 65536 個字串再過濾，
浪費了 97.8% 的工作量。這就是剪枝的價值。

卡塔蘭數會出現在一大票「遞迴結構」的計數問題裡：
  - n 對括號的合法組合數
  - n 個節點的不同二元搜尋樹數量（第 96 題）
  - 凸多邊形三角剖分的方法數
  - n×n 網格中不越過對角線的路徑數
它們之所以答案相同，是因為底層都是同一個遞迴結構。"""),
   ]),
 ],
 "idea": [
   ("fig", _P22_FIG, "0 0 640 294"),
 ],
 "approaches": [
   ap("解法一", "生成全部再過濾（基準線）", [
     "最笨的做法：生成所有 2^(2n) 個由 <code>(</code> 和 <code>)</code> 組成的字串，逐一驗證。",
     ("c", S["p22_bruteforce"]),
     "n = 8 時要生成 65536 個字串、驗證 65536 次，"
     "而答案只有 1430 個 —— <strong>98% 的工作是白費的</strong>。",
     "但它有一個價值：<code>valid()</code> 函式把「合法的定義」寫得清清楚楚，"
     "而解法二就是把這個定義<strong>提前</strong>到生成的時候去檢查。"
     "<strong>「把事後驗證改成事前剪枝」是所有回溯優化的通用套路。</strong>",
   ], "O(2^(2n) · n)", "O(n)", "生成 4ⁿ 個 × 驗證 O(n)", "遞迴深度 2n"),

   ap("解法二", "回溯 + 剪枝（標準解）", [
     "不要生成之後再檢查，而是<strong>只在「放下去仍然可能合法」的時候才放</strong>。",
     ("c", S["p22_backtrack"]),
     ("h", "兩個條件，各自對應一條合法規則"),
     ("c", """if open_used < n:          可以放左括號
      對應「總共只有 n 個左括號」

if close_used < open_used:  可以放右括號
      對應「任何前綴裡右括號不能超過左括號」

      注意是「嚴格小於」。
      如果寫成 <=，就會允許 close_used == open_used 時再放一個右括號，
      產生 "()" 之後接 ")" 變成 "())" —— 不合法。

終止條件 len(path) == 2*n：
      這時候一定是 open_used == close_used == n，
      因為兩個條件保證了 close_used <= open_used <= n，
      而 open_used + close_used == 2n 只有在都等於 n 時才成立。
      所以不需要額外驗證，走到底的一定合法。"""),
     "<strong>「走到底的一定合法」是這個解法最漂亮的地方。</strong>"
     "剪枝不只是加快速度 —— 它讓「驗證」這個步驟完全消失了。",
     ("h", "複雜度為什麼是 O(4ⁿ / √n)？"),
     "答案數量是卡塔蘭數 C_n，而 C_n 的漸近式是 4ⁿ / (n^1.5 · √π)。"
     "每個答案要花 O(n) 組字串，所以總共約 O(4ⁿ / √n)。"
     "<strong>這已經是最優的 —— 因為光是輸出答案就要這麼多時間。</strong>"
     "面試時能說出「這題的下界就是答案的總大小」會很加分。",
   ], "O(4ⁿ / √n)", "O(n)", "剛好走過所有合法序列", "遞迴深度 2n；不算輸出", optimal=True),

   ap("解法三", "遞迴分解（閉合數 closure number）", [
     "換一個角度：<strong>每個合法序列都能<em>唯一</em>分解成 "
     "<code>\"(\" + A + \")\" + B</code></strong>，"
     "其中第一個 <code>(</code> 和「與它配對的 <code>)</code>」之間是 A，後面是 B。",
     ("c", """"(())()"  分解成：
    "(" + "()" + ")" + "()"
          ^A          ^B
    A 有 1 對，B 有 1 對，加上外層這一對 = 3 對 ✔

"()(())"  分解成：
    "(" + ""  + ")" + "(())"
          ^A          ^B
    A 有 0 對，B 有 2 對 ✔

分解是唯一的，因為「與第一個 ( 配對的 )」只有一個。

所以：
    f(n) = 聯集，對所有 i = 0..n-1：
             { "(" + a + ")" + b  :  a ∈ f(i), b ∈ f(n-1-i) }

這個遞迴式直接給出卡塔蘭數的遞迴定義：
    C_n = Σ C_i · C_(n-1-i)"""),
     ("c", S["p22_closure"]),
     "<strong>它比回溯慢</strong>（字串拼接多，而且要存所有中間結果），"
     "但它揭示了這題的<strong>數學結構</strong>。"
     "如果面試官問「這題的答案數量是多少」，這個分解就是推導卡塔蘭數遞迴式的方法。",
     "<strong>而且這個分解思路能直接搬到第 95 題</strong>（不同的二元搜尋樹 II）："
     "枚舉根節點，左子樹用前 i 個、右子樹用後 n−1−i 個。一模一樣的結構。",
   ], "O(4ⁿ / √n)", "O(4ⁿ / √n)", "同上，但常數大很多", "memo 存所有中間結果"),
 ],
 "compare": (["解法", "時間", "空間", "浪費的工作", "備註"],
   [["一、生成再過濾", "O(4ⁿ·n)", "O(n)", "98%", "當基準線"],
    ["二、回溯剪枝", "O(4ⁿ/√n)", "O(n)", "0%", "標準解"],
    ["三、遞迴分解", "O(4ⁿ/√n)", "O(4ⁿ/√n)", "0%", "揭示卡塔蘭結構"]]),
 "edges": [
   "<strong>n = 1</strong> → <code>[\"()\"]</code>。",
   "<strong>n = 2</strong> → <code>[\"(())\", \"()()\"]</code>（2 個）。",
   "<strong>n = 3</strong> → 5 個。<strong>n = 8</strong> → 1430 個。答案數要對得上卡塔蘭數。",
   "<strong>剪枝條件寫成 <code>close_used &lt;= open_used</code></strong>："
   "會生出 <code>\"())(\"</code> 這類不合法的字串，而且長度統計會出錯。",
   "<strong>忘記 <code>path.pop()</code></strong>：<code>path</code> 會一路變長，"
   "產生的字串全部錯誤。",
   "<strong>n = 0</strong>（題目不會給，但值得想）：應該是 <code>[\"\"]</code>，"
   "因為空序列是合法的。回溯版會正確產生它。",
 ],
 "follow": [
   ("h", "追問一：如果有多種括號（<code>()[]{}</code>）呢？"),
   "分支數從 2 變成 6，而且「可以放右括號」的條件變成"
   "「堆疊頂端是對應的左括號」—— 要維護一個真正的堆疊，不能只用計數器。"
   "答案數量也會爆炸得更快。",
   ("h", "追問二：如果只要第 k 個（字典序）呢？"),
   "不需要全部生成。在每個節點上<strong>計算「走左分支能產生多少個答案」</strong>"
   "（這可以用卡塔蘭數的變形算出來），"
   "如果 k 小於那個數量就走左邊，否則 k 減掉它再走右邊。"
   "這樣可以在 O(n) 步內直接定位到第 k 個。"
   "<strong>同樣的技巧見第 60 題（Permutation Sequence）。</strong>",
   ("h", "追問三：為什麼卡塔蘭數會同時出現在括號、二元樹、多邊形剖分裡？"),
   "因為它們的遞迴結構同構。都可以寫成"
   "<code>C_n = Σ_{i=0}^{n-1} C_i · C_(n-1-i)</code>：",
   ("ul", [
     "<strong>括號</strong>：第一對括號「裡面」有 i 對、「後面」有 n−1−i 對",
     "<strong>二元樹</strong>：根的左子樹有 i 個節點、右子樹有 n−1−i 個",
     "<strong>多邊形剖分</strong>：一條固定邊所在的三角形把多邊形切成兩塊",
   ]),
   "<strong>「不同的問題有相同的遞迴結構，所以有相同的答案」—— "
   "這是組合數學裡最有力的想法之一。</strong>",
 ],
 "related": [
   "<strong>第 20 題 Valid Parentheses</strong> —— 驗證版",
   "<strong>第 95／96 題 Unique Binary Search Trees</strong> —— 同樣是卡塔蘭數",
   "<strong>第 17／39／46／78 題</strong> —— 回溯模板家族",
 ],
 "check": [
   "剪枝條件為什麼是 <code>close_used &lt; open_used</code> 而不是 <code>&lt;=</code>？舉一個會生出的不合法字串。",
   "為什麼「走到底的字串一定合法」？請從兩個剪枝條件推導出來。",
   "n = 4 的答案有幾個？不剪枝的話要生成幾個字串？",
   "解法三的唯一分解為什麼成立？請把 <code>\"(())()\"</code> 和 <code>\"()(())\"</code> 各分解一次。",
 ],
})
print("P22 written")
