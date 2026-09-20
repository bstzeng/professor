# -*- coding: utf-8 -*-
"""第 79–82 題。"""
import random, collections
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(79)

# ==================== 79. Word Search ====================
S["p79"] = '''class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(r: int, c: int, k: int) -> bool:
            if k == len(word):
                return True                    # 整個 word 都配完了
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[k]:
                return False

            # 就地標記「這一格已經在目前的路徑上」，避免同一格用兩次
            tmp, board[r][c] = board[r][c], "#"

            found = (dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or
                     dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1))

            board[r][c] = tmp                  # 回溯：把格子還原
            return found

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))'''

S["p79_pruned"] = '''from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # 剪枝 1：board 裡每個字母的數量，必須夠 word 用
        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)
        if any(word_count[ch] > board_count[ch] for ch in word_count):
            return False

        # 剪枝 2：如果 word 的「結尾字母」比「開頭字母」稀有，就反過來找
        # （稀有的字母當起點，能砍掉更多分支）
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        def dfs(r: int, c: int, k: int) -> bool:
            if k == len(word):
                return True
            if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[k]:
                return False

            tmp, board[r][c] = board[r][c], "#"
            found = (dfs(r + 1, c, k + 1) or dfs(r - 1, c, k + 1) or
                     dfs(r, c + 1, k + 1) or dfs(r, c - 1, k + 1))
            board[r][c] = tmp
            return found

        return any(dfs(i, j, 0) for i in range(m) for j in range(n))'''

_p79 = [S.load(k) for k in ("p79", "p79_pruned")]
_B = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]


def _p79_ref(board, word):
    """暴力 DFS（用 set 記錄走過的格子）當基準。"""
    m, n = len(board), len(board[0])

    def go(r, c, k, seen):
        if k == len(word):
            return True
        if not (0 <= r < m and 0 <= c < n):
            return False
        if (r, c) in seen or board[r][c] != word[k]:
            return False
        seen.add((r, c))
        ok = any(go(r + dr, c + dc, k + 1, seen)
                 for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        seen.discard((r, c))
        return ok

    return any(go(i, j, 0, set()) for i in range(m) for j in range(n))


for w, e in [("ABCCED", True), ("SEE", True), ("ABCB", False), ("A", True),
             ("Z", False), ("ASFCCE", True), ("ADEEC", False),
             ("ABCESEEEFS", False)]:
    assert _p79_ref([r[:] for r in _B], w) is e, ("P79 ref", w, e)
    for sol in _p79:
        g = sol.exist([r[:] for r in _B], w)
        assert g is e, ("P79", w, sol, g, e)
for _ in range(2000):
    m_, n_ = random.randint(1, 4), random.randint(1, 4)
    b = [[random.choice("abc") for _ in range(n_)] for _ in range(m_)]
    w = "".join(random.choice("abc") for _ in range(random.randint(1, 5)))
    e = _p79_ref([r[:] for r in b], w)
    for sol in _p79:
        snapshot = [r[:] for r in b]
        g = sol.exist(b, w)
        assert g is e, ("P79", b, w, sol, g, e)
        assert b == snapshot, ("P79 board 被破壞了", b, snapshot)
print("P79 solutions OK")

_P79_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">board 找 &quot;ABCCED&quot;：從 (0,0) 出發，四個方向 DFS，走過的格子暫時標記成 #</text>
            <g font-size="16" text-anchor="middle">
              <rect x="120" y="48" width="56" height="46" fill="none" stroke="#ff8a65" stroke-width="2.5"/><text x="148" y="79" fill="#ff8a65">A</text>
              <rect x="176" y="48" width="56" height="46" fill="none" stroke="#ff8a65" stroke-width="2.5"/><text x="204" y="79" fill="#ff8a65">B</text>
              <rect x="232" y="48" width="56" height="46" fill="none" stroke="#ff8a65" stroke-width="2.5"/><text x="260" y="79" fill="#ff8a65">C</text>
              <rect x="288" y="48" width="56" height="46" fill="none" stroke="var(--border)"/><text x="316" y="79" fill="var(--text-muted)">E</text>
              <rect x="120" y="94" width="56" height="46" fill="none" stroke="var(--border)"/><text x="148" y="125" fill="var(--text-muted)">S</text>
              <rect x="176" y="94" width="56" height="46" fill="none" stroke="var(--border)"/><text x="204" y="125" fill="var(--text-muted)">F</text>
              <rect x="232" y="94" width="56" height="46" fill="none" stroke="#ff8a65" stroke-width="2.5"/><text x="260" y="125" fill="#ff8a65">C</text>
              <rect x="288" y="94" width="56" height="46" fill="none" stroke="var(--border)"/><text x="316" y="125" fill="var(--text-muted)">S</text>
              <rect x="120" y="140" width="56" height="46" fill="none" stroke="var(--border)"/><text x="148" y="171" fill="var(--text-muted)">A</text>
              <rect x="176" y="140" width="56" height="46" fill="none" stroke="#ff8a65" stroke-width="2.5"/><text x="204" y="171" fill="#ff8a65">D</text>
              <rect x="232" y="140" width="56" height="46" fill="none" stroke="#ff8a65" stroke-width="2.5"/><text x="260" y="171" fill="#ff8a65">E</text>
              <rect x="288" y="140" width="56" height="46" fill="none" stroke="var(--border)"/><text x="316" y="171" fill="var(--text-muted)">E</text>
            </g>
            <g stroke="#ff8a65" stroke-width="2" fill="none">
              <path d="M148 71 L204 71 L260 71 L260 117 L260 163 L204 163"/>
            </g>
            <g font-size="11" fill="#ff8a65" text-anchor="middle">
              <text x="148" y="40">1</text><text x="204" y="40">2</text><text x="260" y="40">3</text>
              <text x="300" y="120">4</text><text x="300" y="166">5</text><text x="204" y="200">6</text>
            </g>
            <text x="380" y="80" fill="#ff8a65" font-size="13">A → B → C → C → E → D ✔</text>
            <text x="380" y="106" fill="var(--text-muted)" font-size="12">路徑不能重複經過同一格</text>
            <text x="380" y="132" fill="var(--text-muted)" font-size="12">所以要「標記 → 遞迴 → 還原」</text>
            <line x1="20" y1="216" x2="620" y2="216" stroke="var(--border)"/>
            <text x="20" y="244" fill="var(--gold)" font-size="12">就地標記（board[r][c] = &quot;#&quot;）比另開一個 visited 陣列省空間，</text>
            <text x="20" y="266" fill="var(--text-muted)" font-size="12">但一定要在遞迴回來之後還原 —— 否則後續的搜尋會看到殘留的 #。</text>'''

emit({
 "num": 79, "slug": "word-search",
 "en": [
   "Given an <code>m x n</code> grid of characters <code>board</code> and a string "
   "<code>word</code>, return <code>true</code> <em>if</em> <code>word</code> "
   "<em>exists in the grid</em>.",
   "The word can be constructed from letters of sequentially adjacent cells, where adjacent "
   "cells are horizontally or vertically neighboring. <strong>The same letter cell may not be "
   "used more than once.</strong>",
 ],
 "zh": [
   "給你一個 <code>m × n</code> 的字元網格 <code>board</code> 和一個字串 <code>word</code>，"
   "判斷 <code>word</code> 是否存在於網格中。",
   "單字必須由<strong>相鄰的格子</strong>依序連成（上下左右相鄰，不含對角線），"
   "而且<strong>同一個格子不能重複使用</strong>。",
 ],
 "pre": [
   ("note", "網格回溯的標準三步驟", [
     ("c", """1. 標記：把目前這一格標成「已在路徑上」
2. 遞迴：往四個方向繼續找
3. 還原：不管成不成功，把標記拿掉

第 3 步是「回溯」的精髓。
如果不還原，後續從別的起點出發的搜尋，
會誤以為那些格子還被佔用著。

為什麼一定要標記？
    因為「同一格不能重複使用」。

    board = [["A","B"],
             ["C","D"]]
    word = "ABA"

    如果不標記：A(0,0) -> B(0,1) -> 回到 A(0,0)  ->  回傳 True ✘
    正確答案是 False（只有一個 A）。

標記的兩種做法：
    (a) 另開一個 visited 陣列        —— O(mn) 額外空間
    (b) 就地把 board[r][c] 改成 '#'  —— O(1) 額外空間

    (b) 更省空間，但「破壞輸入」——
    所以【還原】變得絕對必要，不只是為了正確性，
    也是為了不留下副作用。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：board = [["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]], word = "ABCCED"
  輸出：true

範例 2
  輸入：同上，word = "SEE"
  輸出：true

範例 3
  輸入：同上，word = "ABCB"
  輸出：false
  說明：兩個 B 是同一格，不能重複使用。""",
 "constraints": [
   "<code>m == board.length</code>，<code>n == board[i].length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 6",
   "1 ≤ <code>word.length</code> ≤ 15",
   "<code>board</code> 和 <code>word</code> 只含大小寫英文字母",
   "<strong>進階：</strong>能不能加上剪枝，讓最壞情況更快？",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>網格只有 6 × 6 = 36 格，word 最長 15</strong>。"
       "這個規模小得刻意 —— 因為<strong>最壞情況是指數級的</strong>。",
       "<strong>複雜度分析</strong>：從每個起點出發，"
       "第一步有 4 個方向，之後每步最多 3 個（不能回頭）—— "
       "所以是 <code>O(mn × 4 × 3^(L-1))</code>，L 是 word 長度。"
       "L = 15 時 <code>3¹⁴ ≈ 478 萬</code>，再乘 36 個起點 ——"
       "<strong>約 1.7 億，在最壞情況下確實會很慢</strong>，"
       "這就是「進階：加剪枝」的理由。",
       "<strong>word 至少 1 個字元</strong>，所以不用處理空字串。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P79_FIG, "0 0 640 280"),
 ],
 "approaches": [
   ap("解法一", "DFS + 就地標記回溯（標準解）", [
     ("c", S["p79"]),
     ("h", "為什麼把「越界」和「字元不符」放在函式的開頭？"),
     ("c", """兩種寫法：

  (A) 呼叫前檢查：
      for 每個方向:
          if 在界內 and board[nr][nc] == word[k+1]:
              dfs(nr, nc, k+1)

  (B) 進函式才檢查（本文用的）：
      def dfs(r, c, k):
          if k == len(word): return True
          if 越界 or board[r][c] != word[k]: return False
          ...

(B) 的好處：
    - 四個方向的呼叫長得一模一樣，不用each 都寫一次檢查
    - 最外層的 any(dfs(i, j, 0) ...) 也不用先檢查 board[i][j] == word[0]
    - 邊界邏輯只寫一次 -> 只有一個地方會寫錯

(A) 的好處：少一層函式呼叫（常數稍快）。

在網格 DFS 裡，(B) 幾乎總是比較好的選擇。"""),
     ("h", "終止條件的順序不能換"),
     ("c", """if k == len(word):
    return True
if 越界 or board[r][c] != word[k]:
    return False

必須先檢查 k == len(word)！

    因為當 k == len(word) 時，word[k] 會 IndexError。

    而且語意上也對：「整個 word 都配完了」就是成功，
    此時 (r, c) 是什麼根本不重要。

追一遍 word = "A"，board = [["A"]]：
    dfs(0, 0, 0): k=0 != 1，不越界，board[0][0] == 'A' ✔
                  標記，然後四個方向都 dfs(..., 1)
                  其中 dfs(1, 0, 1): k == 1 == len(word) -> True ✔
    回傳 True ✔

    咦？dfs(1, 0, 1) 的 (1,0) 明明越界了，為什麼回傳 True？
    因為 k == len(word) 的檢查在越界檢查之前 ——
    我們已經配完整個 word 了，位置不重要。

    這不是 bug，是刻意的設計。"""),
     ("h", "還原那一行的重要性"),
     "<code>board[r][c] = tmp</code> 讓函式<strong>沒有副作用</strong> —— "
     "不管成功失敗，離開時盤面和進來時一樣。",
     "<strong>如果忘了還原</strong>：",
     ("ul", [
       "從別的起點出發的搜尋會看到殘留的 <code>#</code>，錯誤地失敗",
       "而且<strong>函式會破壞呼叫端的資料</strong> —— "
       "在真實的程式裡這是很嚴重的問題",
     ]),
     "<strong>本篇的測試除了檢查答案，還會檢查「board 有沒有被改壞」</strong> —— "
     "這是驗證回溯正確性的好習慣。",
   ], "O(mn × 3^L)", "O(L)", "L = word 長度；遞迴深度 L",
      "遞迴堆疊；就地標記不用額外空間", optimal=True),

   ap("解法二", "加上兩個剪枝（進階要求）", [
     ("c", S["p79_pruned"]),
     ("h", "剪枝 1：字母數量檢查"),
     ("c", """如果 word 需要 3 個 'X'，而整個 board 只有 2 個 ——
那不管怎麼搜都不可能成功。

    board_count = Counter(所有格子的字母)
    word_count = Counter(word)
    if any(word_count[ch] > board_count[ch] for ch in word_count):
        return False

成本：O(mn + L)，一次就好。
效益：在「word 含有 board 沒有（或不夠）的字母」時，
      直接把 O(mn × 3^L) 變成 O(mn)。

LeetCode 上有一筆著名的測資：
    board 是 6×6 全是 'a'，只有右下角是 'b'
    word = "aaaaaaaaaaaaaaab"（15 個 a + 1 個 b）

    不剪枝的話會搜很久。
    （這一筆剪枝 1 擋不住，要靠剪枝 2 和搜尋本身。）"""),
     ("h", "剪枝 2：從稀有的那一端開始搜"),
     ("c", """if board_count[word[0]] > board_count[word[-1]]:
    word = word[::-1]

為什麼有效？
    搜尋的起點是「所有等於 word[0] 的格子」。
    起點越少，要展開的搜尋樹就越少。

    board = 35 個 'a' + 1 個 'b'
    word = "aaaa...b"

    正著搜：起點是 35 個 'a' -> 35 棵搜尋樹
    反著搜：起點是 1 個 'b'  -> 1 棵搜尋樹

    快 35 倍！

為什麼可以反著搜？
    因為「路徑」是無向的 ——
    如果 board 裡存在一條路徑拼出 word，
    那反過來走同一條路徑就拼出 reversed(word)。

    兩者的存在性完全等價 ✔

這是一個很漂亮的剪枝：
    它不改變演算法，只改變「從哪一端開始」。

    同樣的想法出現在雙向 BFS、
    以及資料庫的 join 順序優化（先掃小表）。"""),
     "<strong>還可以加的剪枝</strong>（本文沒寫，但值得知道）：",
     ("ul", [
       "<strong>剩餘長度檢查</strong>：如果 <code>len(word) - k</code> 大於「從這一格可達的格子數」，"
       "就剪掉。但算「可達格子數」本身有成本。",
       "<strong>連通性檢查</strong>：如果 <code>word</code> 的長度超過整個 board 的格子數，直接 false。"
       "（這被剪枝 1 涵蓋了。）",
     ]),
   ], "最壞仍是 O(mn × 3^L)", "O(L + Σ)", "多數情況快很多",
      "遞迴堆疊 + 兩個 Counter"),
 ],
 "compare": (["解法", "最壞時間", "剪枝", "破壞輸入？", "備註"],
   [["一、DFS + 就地標記", "O(mn·3^L)", "無", "✘（有還原）", "面試預設"],
    ["二、加兩個剪枝", "O(mn·3^L)", "字母數量 + 反向搜", "✘", "進階要求"]]),
 "edges": [
   "<strong>單一格子</strong>：<code>([[\"A\"]], \"A\")</code> → true；"
   "<code>([[\"A\"]], \"B\")</code> → false。",
   "<strong>不能重複使用同一格</strong>：<code>\"ABCB\"</code> → false。"
   "<strong>沒有標記的話會錯誤地回 true。</strong>",
   "<strong>word 比整個 board 還長</strong>：直接 false（剪枝 1 會擋）。",
   "<strong>需要轉彎的路徑</strong>：<code>\"ABCCED\"</code> → true。",
   "<strong>需要往回走（上）</strong>：<code>\"ASFCCE\"</code> → true（A→S→F→C→往上的 C→E）。"
   "<strong>只寫「右」和「下」兩個方向會錯。</strong>",
   "<strong>board 被破壞</strong>：忘記還原的話，"
   "第二次呼叫同一個 <code>exist</code> 會得到錯誤的結果。",
   "<strong>長度 1 的 word</strong>：只要 board 裡有那個字母就 true。",
 ],
 "follow": [
   ("h", "追問一：如果要同時找「很多個單字」呢？"),
   "第 212 題（Word Search II）。"
   "<strong>對每個單字各跑一次 DFS 是 O(單字數 × mn × 3^L)，太慢。</strong>",
   ("c", """標準解法：把所有單字建成一棵 Trie（字典樹），
然後在 board 上只做【一次】DFS，同時沿著 Trie 往下走。

    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node.children:
            return                     # Trie 上沒有這條路 -> 剪掉整棵子樹
        nxt = node.children[ch]
        if nxt.word:
            找到一個單字
        ...四個方向遞迴...

這樣所有單字「共用」同一趟搜尋 ——
而且 Trie 提供了極強的剪枝：
    只要目前的前綴不是任何單字的前綴，立刻停。

這是「Trie + 回溯」最經典的組合，
也是第 79 題真正想引導你去的地方。""",),
   ("h", "追問二：如果允許對角線（八個方向）呢？"),
   "把方向陣列從 4 個改成 8 個。"
   "<strong>但複雜度會從 O(3^L) 變成 O(7^L)</strong> —— "
   "L = 15 時是 <code>7¹⁴ ≈ 6.8 × 10¹¹</code>，完全不可行。"
   "<strong>所以八方向的版本一定要有很強的剪枝（例如 Trie）。</strong>",
   ("h", "追問三：這題是 NP-hard 嗎？"),
   "<strong>一般化的版本是。</strong>"
   "「在網格上找一條不重複經過任何格子的路徑，使它拼出指定字串」"
   "本質上是<strong>尋找哈密頓路徑（Hamiltonian path）</strong>的變形 —— "
   "當 <code>word</code> 的長度等於格子總數時，它就是在問「有沒有哈密頓路徑」，"
   "而那是 NP-complete 的。",
   "<strong>這就是為什麼題目把 board 限制在 6×6</strong> —— "
   "沒有多項式演算法，只能靠剪枝硬搜。",
   ("h", "追問四：「就地標記」vs「visited 陣列」怎麼選？"),
   ("t", ["", "就地標記", "visited 陣列"],
     [["額外空間", "O(1)", "O(mn)"],
      ["破壞輸入", "會（但有還原）", "不會"],
      ["能平行化", "✘（共用 board）", "✔（每個執行緒一份 visited）"],
      ["需要保留值", "✔（要一個不會出現的字元）", "✘"]]),
   "<strong>如果字元集是完整的 Unicode，就找不到安全的標記字元</strong> —— "
   "那時只能用 <code>visited</code> 陣列。"
   "本題只有英文字母，所以 <code>'#'</code> 是安全的。",
 ],
 "related": [
   "<strong>第 212 題 Word Search II</strong> —— 多個單字，要用 Trie",
   "<strong>第 200 題 Number of Islands</strong> —— 網格 DFS 的入門題",
   "<strong>第 37／51 題</strong> —— 回溯家族",
   "<strong>第 208 題 Implement Trie</strong> —— 第 212 題的前置",
 ],
 "check": [
   "為什麼 <code>if k == len(word)</code> 必須放在越界檢查之前？",
   "忘記 <code>board[r][c] = tmp</code> 會有哪兩個後果？",
   "剪枝 2（從稀有的那一端搜）為什麼是正確的？",
   "為什麼複雜度是 <code>3^L</code> 而不是 <code>4^L</code>？",
 ],
})
print("P79 written")

# ==================== 80. Remove Duplicates from Sorted Array II ====================
S["p80"] = '''class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0                    # 下一個要寫入的位置
        for x in nums:
            # 保留的條件：還不足兩個，或和「已保留的倒數第二個」不同
            if k < 2 or x != nums[k - 2]:
                nums[k] = x
                k += 1
        return k'''

S["p80_general"] = '''class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self._keep_at_most(nums, 2)

    def _keep_at_most(self, nums: List[int], m: int) -> int:
        """每個值最多保留 m 次 —— 把 2 抽成參數的通用版"""
        k = 0
        for x in nums:
            if k < m or x != nums[k - m]:
                nums[k] = x
                k += 1
        return k'''

S["p80_count"] = '''class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 比較直白的版本：明確數「目前這個值已經寫了幾次」
        if not nums:
            return 0

        k = 1
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            if count <= 2:
                nums[k] = nums[i]
                k += 1
        return k'''

_p80 = [S.load(k) for k in ("p80", "p80_general", "p80_count")]


def _p80_ref(nums):
    out = []
    for x in nums:
        if len(out) < 2 or x != out[-2]:
            out.append(x)
    return out


for c in [[1, 1, 1, 2, 2, 3], [0, 0, 1, 1, 1, 1, 2, 3, 3], [], [1], [1, 1],
          [1, 1, 1], [1, 2, 3], [1, 1, 2, 2, 3, 3]]:
    e = _p80_ref(c)
    for sol in _p80:
        a = list(c)
        k = sol.removeDuplicates(a)
        assert k == len(e) and a[:k] == e, ("P80", c, sol, k, a[:k], e)
for _ in range(5000):
    c = sorted(random.randint(0, 4) for _ in range(random.randint(0, 12)))
    e = _p80_ref(c)
    for sol in _p80:
        a = list(c)
        k = sol.removeDuplicates(a)
        assert k == len(e) and a[:k] == e, ("P80", c, sol)
print("P80 solutions OK")

emit({
 "num": 80, "slug": "remove-duplicates-from-sorted-array-ii",
 "en": [
   "Given an integer array <code>nums</code> sorted in <strong>non-decreasing order</strong>, "
   "remove some duplicates <strong>in-place</strong> such that each unique element appears "
   "<strong>at most twice</strong>. The relative order of the elements should be kept the same.",
   "Return <code>k</code> after placing the final result in the first <code>k</code> slots of "
   "<code>nums</code>.",
 ],
 "zh": [
   "給你一個<strong>非遞減排序</strong>的整數陣列 <code>nums</code>，"
   "請<strong>原地</strong>刪除重複的元素，讓每個值<strong>最多出現兩次</strong>，"
   "並保持原本的相對順序。",
   "回傳處理後的長度 <code>k</code>，而且前 <code>k</code> 個位置要存放結果。",
 ],
 "pre": [
   ("note", "和第 26 題只差一個數字", [
     ("c", """第 26 題（每個值最多 1 次）：
    if k < 1 or x != nums[k - 1]:

第 80 題（每個值最多 2 次）：
    if k < 2 or x != nums[k - 2]:

一般化（每個值最多 m 次）：
    if k < m or x != nums[k - m]:

為什麼是「和 nums[k-m] 比」？

    nums[k-m] 是「已經保留下來的、倒數第 m 個」。

    如果 x 和它相同，表示「已經有 m 個和 x 一樣的值被保留了」
    （因為輸入已排序，相同的值一定連續）
    -> 不能再收 ✘

    如果不同，表示保留的相同值不到 m 個 -> 可以收 ✔

    而 k < m 的檢查，處理「還沒收滿 m 個」的開頭情況
    （此時 nums[k-m] 是負索引，在 Python 裡不會報錯但語意錯）。

這就是為什麼第 26 題我們堅持寫 nums[k-1] 而不是 nums[i-1]：
    用 k 的版本可以一般化，用 i 的版本不行。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,1,1,2,2,3]
  輸出：k = 5，nums 的前 5 格是 [1,1,2,2,3]

範例 2
  輸入：nums = [0,0,1,1,1,1,2,3,3]
  輸出：k = 7，前 7 格是 [0,0,1,1,2,3,3]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 3 × 10⁴",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
   "<code>nums</code> 已依<strong>非遞減順序</strong>排好",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>已經排序</strong> —— 這是關鍵。相同的值一定連續，"
       "所以「已保留幾個相同的」可以從 <code>nums[k-2]</code> 讀出來。",
       "<strong>必須原地</strong>，而且只檢查前 k 格。",
       "<strong>值域有負數</strong>，不能用某個數字當哨兵。",
       "<strong>n ≥ 1</strong>，但寫成能處理空陣列比較安全。",
     ]),
   ]),
 ],
 "idea": [
   ("c", """雙指標：一個讀（for 迴圈的 x）、一個寫（k）。

nums = [1,1,1,2,2,3]

  x=1: k=0 < 2           -> nums[0]=1, k=1
  x=1: k=1 < 2           -> nums[1]=1, k=2
  x=1: nums[0]=1 == 1    -> 跳過（已經有兩個 1 了）
  x=2: nums[0]=1 != 2    -> nums[2]=2, k=3
  x=2: nums[1]=1 != 2    -> nums[3]=2, k=4
  x=3: nums[2]=2 != 3    -> nums[4]=3, k=5

  nums = [1,1,2,2,3,3]，前 5 格 = [1,1,2,2,3] ✔ 回傳 5

注意第 6 格還是舊資料（3），但題目不檢查。

安全性：k <= i 恆成立（寫的位置永遠不超前讀的位置），
        所以 nums[k] = x 不會覆蓋掉還沒讀的資料 ✔"""),
 ],
 "approaches": [
   ap("解法一", "和「倒數第二個保留值」比較（最推薦）", [
     ("c", S["p80"]),
     ("h", "為什麼 <code>nums[k-2]</code> 能正確表達「已經有兩個了」？"),
     ("c", """因為輸入是【排序】的，所以：

    如果 nums[k-2] == x，
    那麼 nums[k-2] 和 nums[k-1] 一定都等於 x
    （排序後，介於兩個 x 之間的值也只能是 x）

    -> 已經保留了至少兩個 x -> 不能再收 ✔

    如果 nums[k-2] != x，
    那麼保留的 x 最多只有一個（就是 nums[k-1]，如果它等於 x 的話）
    -> 還可以再收一個 ✔

如果輸入沒有排序，這個推理就不成立 ——
例如 [1, 2, 1, 2, 1]，nums[k-2] 的值和「x 出現幾次」完全無關。

所以「已排序」這個前提，
讓我們不需要任何計數器就能知道「已經收了幾個」。"""),
     ("h", "<code>k &lt; 2</code> 這個檢查"),
     "處理開頭：前兩個元素<strong>無條件保留</strong>（因為最多允許兩個）。"
     "而且它擋住了 <code>nums[k-2]</code> 的負索引 —— "
     "<strong>在 Python 裡負索引不會報錯</strong>（會拿到陣列尾端的值），"
     "所以這個檢查是必要的，不然會安靜地算錯。",
     "<strong>三行核心邏輯</strong>，而且和第 26 題只差一個數字。",
   ], "O(n)", "O(1)", "掃一遍", "只用一個下標", optimal=True),

   ap("解法二", "把 2 抽成參數（一般化）", [
     ("c", S["p80_general"]),
     "<strong>同一份程式碼同時解了第 26 題（m=1）和第 80 題（m=2）。</strong>",
     "<strong>這是一個很好的習慣</strong>：當你發現「這題和那題只差一個常數」時，"
     "就把那個常數抽出來。"
     "在真實的程式碼裡，這會變成一個可重用的函式；"
     "在面試時，它顯示你看到了問題的結構而不只是表面。",
     "<strong>而且它讓「為什麼是 k-m」這件事變得明顯</strong> —— "
     "當 m 是變數時，你不可能把它誤寫成 <code>i - m</code>。",
   ], "O(n)", "O(1)", "同上", "同上"),

   ap("解法三", "明確用計數器（最直白）", [
     ("c", S["p80_count"]),
     "<strong>語意最直白</strong>：「數一數目前這個值連續出現幾次，超過 2 就不收」。",
     "<strong>缺點</strong>：多一個變數、多一個 if，而且推廣到 m 次時"
     "要改的地方比解法一多（雖然也只是把 2 換成 m）。",
     "<strong>但它有一個優勢</strong>：<strong>它不依賴「已排序」這個前提</strong>來判斷計數"
     "（雖然仍然依賴排序來讓相同的值連續）。"
     "如果題目改成「相同的值不一定連續」，這個版本比較容易改成用 <code>Counter</code>。",
     "<strong>如果解法一的 <code>nums[k-2]</code> 讓你覺得不踏實，寫這個版本也完全可以。</strong>"
     "面試時清楚正確 &gt; 精簡炫技。",
   ], "O(n)", "O(1)", "掃一遍", "兩個變數"),
 ],
 "compare": (["解法", "行數", "推廣到「最多 m 次」", "依賴已排序？", "備註"],
   [["一、和 nums[k−2] 比", "6", "改一個數字", "✔ 強烈依賴", "最精簡"],
    ["二、抽成參數", "9", "改參數", "✔", "一份程式碼解兩題"],
    ["三、計數器", "13", "改一個數字", "✔（較弱）", "最直白"]]),
 "edges": [
   "<strong>空陣列</strong>：<code>[]</code> → 0。解法一自然處理（迴圈不跑）。",
   "<strong>長度 1 或 2</strong>：<code>[1]</code> → 1；<code>[1,1]</code> → 2。"
   "<strong><code>k &lt; 2</code> 的檢查就是為了它們。</strong>",
   "<strong>全部相同</strong>：<code>[1,1,1]</code> → 2，前 2 格是 <code>[1,1]</code>。",
   "<strong>完全沒有重複</strong>：<code>[1,2,3]</code> → 3。每一格都會被寫（寫到自己身上）。",
   "<strong>剛好每個兩次</strong>：<code>[1,1,2,2,3,3]</code> → 6（全部保留）。",
   "<strong>混合</strong>：<code>[0,0,1,1,1,1,2,3,3]</code> → 7。",
   "<strong>忘記 <code>k &lt; 2</code></strong>：在 Python 裡 <code>nums[-2]</code> "
   "會拿到陣列的倒數第二個元素 —— <strong>不會報錯，但答案會錯。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果每個值最多保留 m 次呢？"),
   "就是解法二。<code>if k &lt; m or x != nums[k - m]</code>，一個參數搞定。",
   ("h", "追問二：如果輸入沒有排序呢？"),
   "「已排序」這個前提被拿掉之後，就得用 <code>Counter</code> 記錄「每個值已經收了幾次」：",
   ("c", """from collections import Counter

def keep_at_most(nums, m):
    seen = Counter()
    k = 0
    for x in nums:
        if seen[x] < m:
            nums[k] = x
            k += 1
            seen[x] += 1
    return k

空間從 O(1) 變成 O(不同值的個數)。

「已排序」這個前提值多少？它省下了整個雜湊表。""",),
   ("h", "追問三：這個「原地過濾」模板還能用在哪？"),
   ("c", """通用形式：
    k = 0
    for x in nums:
        if <保留的條件>:
            nums[k] = x
            k += 1
    return k

第 26 題  條件：x != nums[k-1]              去重（最多 1 次）
第 27 題  條件：x != val                    移除特定值
第 80 題  條件：k < 2 or x != nums[k-2]     最多 2 次
第 283 題 條件：x != 0                      移動零（之後再補零）

共同的安全保證：
    k <= i 恆成立（寫不超前讀）
    -> nums[k] = x 永遠不會覆蓋掉還沒讀到的資料

這是所有「原地過濾」演算法的正確性基礎，
也是 C++ 的 std::remove_if 的實作方式。""",),
   ("h", "追問四：為什麼第 26 題我們堅持用 <code>nums[k-1]</code> 而不是 <code>nums[i-1]</code>？"),
   "<strong>因為那個選擇在這一題才顯出價值。</strong>"
   "第 26 題裡兩者等價（都對），但只有 <code>nums[k-1]</code> 的版本"
   "能直接一般化成 <code>nums[k-m]</code>。",
   "<strong>這是一個很好的例子：寫程式時的「小選擇」，"
   "會在推廣的時候顯出高下。</strong>"
   "養成「用語意正確的那個變數」的習慣（這裡是「已保留的」而不是「原本的」），"
   "在之後的變形題上會省很多力氣。",
 ],
 "related": [
   "<strong>第 26 題 Remove Duplicates from Sorted Array</strong> —— m = 1 的版本",
   "<strong>第 27 題 Remove Element</strong> —— 同一個過濾模板",
   "<strong>第 283 題 Move Zeroes</strong> —— 過濾 + 補零",
   "<strong>第 82／83 題</strong> —— 鏈結串列版的去重",
 ],
 "check": [
   "為什麼比較的對象是 <code>nums[k-2]</code>（已保留的倒數第二個）而不是 <code>nums[i-2]</code>？",
   "<code>k &lt; 2</code> 這個檢查如果拿掉，在 Python 裡會發生什麼（提示：不會報錯）？",
   "這個解法為什麼強烈依賴「輸入已排序」？沒排序的話要怎麼改？",
   "「最多保留 m 次」的通用條件是什麼？",
 ],
})
print("P80 written")
