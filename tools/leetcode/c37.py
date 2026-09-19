# -*- coding: utf-8 -*-
"""第 37–39 題。"""
import random, collections, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(37)

# ==================== 37. Sudoku Solver ====================
S["p37_plain"] = '''class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def ok(r: int, c: int, ch: str) -> bool:
            for i in range(9):
                if board[r][i] == ch or board[i][c] == ch:
                    return False
            br, bc = (r // 3) * 3, (c // 3) * 3
            for i in range(br, br + 3):
                for j in range(bc, bc + 3):
                    if board[i][j] == ch:
                        return False
            return True

        def solve(pos: int) -> bool:
            if pos == 81:
                return True
            r, c = divmod(pos, 9)
            if board[r][c] != ".":
                return solve(pos + 1)

            for ch in "123456789":
                if ok(r, c, ch):
                    board[r][c] = ch
                    if solve(pos + 1):
                        return True
                    board[r][c] = "."      # 回溯
            return False

        solve(0)'''

S["p37_bitmask"] = '''class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        FULL = 0x1FF                       # 0b111111111，9 個候選全開

        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empties = []

        # 初始化：把已知的數字記進三組遮罩，並收集空格
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    empties.append((r, c))
                else:
                    bit = 1 << (int(v) - 1)
                    rows[r] |= bit
                    cols[c] |= bit
                    boxes[(r // 3) * 3 + c // 3] |= bit

        def solve(k: int) -> bool:
            if k == len(empties):
                return True

            # MRV（minimum remaining values）：
            # 在還沒填的格子裡挑「候選最少」的那一格先填
            best_i, best_mask, best_cnt = -1, 0, 10
            for i in range(k, len(empties)):
                r, c = empties[i]
                b = (r // 3) * 3 + c // 3
                mask = FULL & ~(rows[r] | cols[c] | boxes[b])
                cnt = bin(mask).count("1")
                if cnt < best_cnt:
                    best_i, best_mask, best_cnt = i, mask, cnt
                    if cnt <= 1:
                        break              # 不可能更好了
            if best_cnt == 0:
                return False               # 有格子無解，整個分支剪掉

            empties[k], empties[best_i] = empties[best_i], empties[k]
            r, c = empties[k]
            b = (r // 3) * 3 + c // 3

            mask = best_mask
            while mask:
                bit = mask & -mask         # 取最低位的 1
                mask -= bit

                rows[r] |= bit; cols[c] |= bit; boxes[b] |= bit
                board[r][c] = str(bit.bit_length())

                if solve(k + 1):
                    return True

                rows[r] ^= bit; cols[c] ^= bit; boxes[b] ^= bit
                board[r][c] = "."

            empties[k], empties[best_i] = empties[best_i], empties[k]
            return False

        solve(0)'''

_p37 = [S.load(k) for k in ("p37_plain", "p37_bitmask")]
_PUZ = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
_SOL = ["534678912", "672195348", "198342567", "859761423", "426853791",
        "713924856", "961537284", "287419635", "345286179"]
# 「世界最難數獨」之一，用來驗證剪枝
_HARD = [list(row) for row in
         ["8........", "..36.....", ".7..9.2..", ".5...7...", "....457..",
          "...1...3.", "..1....68", "..85...1.", ".9....4.."]]


def _check_solved(b):
    for i in range(9):
        assert sorted(b[i]) == list("123456789"), ("row", i, b[i])
        assert sorted(b[r][i] for r in range(9)) == list("123456789"), ("col", i)
    for br in range(0, 9, 3):
        for bc in range(0, 9, 3):
            cells = [b[br + i][bc + j] for i in range(3) for j in range(3)]
            assert sorted(cells) == list("123456789"), ("box", br, bc)


for sol in _p37:
    b = [row[:] for row in _PUZ]
    sol.solveSudoku(b)
    assert ["".join(r) for r in b] == _SOL, ("P37 easy", sol)
# 難題只用位元版測（純版會很慢）
b = [row[:] for row in _HARD]
_p37[1].solveSudoku(b)
_check_solved(b)
for r in range(9):
    for c in range(9):
        assert _HARD[r][c] in (".", b[r][c]), ("P37 hard 改動了原有數字", r, c)
print("P37 solutions OK")

emit({
 "num": 37, "slug": "sudoku-solver",
 "en": [
   "Write a program to solve a Sudoku puzzle by filling the empty cells.",
   "A sudoku solution must satisfy <strong>all of the following rules</strong>: each of the "
   "digits <code>1-9</code> must occur exactly once in each row, each column, and each of the "
   "nine <code>3 x 3</code> sub-boxes.",
   "The <code>'.'</code> character indicates empty cells. It is guaranteed that the input "
   "board has <strong>only one solution</strong>.",
 ],
 "zh": [
   "寫一個程式填滿數獨的空格，把它解出來。",
   "解答必須滿足：<strong>每一列、每一行、每個 3×3 宮格</strong>，"
   "數字 1–9 都<strong>恰好出現一次</strong>。",
   "<code>'.'</code> 表示空格。題目保證輸入<strong>恰好只有一組解</strong>。",
 ],
 "pre": [
   ("note", "回溯 = 深度優先搜尋 + 撤銷", [
     ("c", """基本框架只有四行邏輯：

    for 每個候選:
        填進去
        遞迴解剩下的
        如果成功 -> 回報成功
        否則把它拿掉（撤銷）
    全部試完都不行 -> 回報失敗

難的不是框架，是「怎麼讓它夠快」。

盲目回溯的搜尋空間有多大？
    最壞情況 9^(空格數)。
    一個典型數獨有 50 個空格 -> 9^50 ≈ 5 × 10^47

顯然不可能窮舉。能在毫秒內解完，完全靠「剪枝」：

    剪枝 1：只試「合法」的候選（而不是 1-9 全試）
    剪枝 2：優先填「候選最少」的格子（MRV 啟發式）

剪枝 1 是必須的，剪枝 2 是把「某些難題要跑好幾秒」
變成「所有題目都在毫秒內」的關鍵。"""),
   ]),
 ],
 "examples": """輸入（. 是空格）
  5 3 . | . 7 . | . . .
  6 . . | 1 9 5 | . . .
  . 9 8 | . . . | . 6 .
  ------+-------+------
  8 . . | . 6 . | . . 3
  4 . . | 8 . 3 | . . 1
  7 . . | . 2 . | . . 6
  ------+-------+------
  . 6 . | . . . | 2 8 .
  . . . | 4 1 9 | . . 5
  . . . | . 8 . | . 7 9

輸出（原地修改 board）
  5 3 4 | 6 7 8 | 9 1 2
  6 7 2 | 1 9 5 | 3 4 8
  1 9 8 | 3 4 2 | 5 6 7
  ------+-------+------
  8 5 9 | 7 6 1 | 4 2 3
  4 2 6 | 8 5 3 | 7 9 1
  7 1 3 | 9 2 4 | 8 5 6
  ------+-------+------
  9 6 1 | 5 3 7 | 2 8 4
  2 8 7 | 4 1 9 | 6 3 5
  3 4 5 | 2 8 6 | 1 7 9""",
 "constraints": [
   "<code>board.length == 9</code>，<code>board[i].length == 9</code>",
   "<code>board[i][j]</code> 是 <code>'1'</code>–<code>'9'</code> 或 <code>'.'</code>",
   "<strong>保證輸入只有一組解</strong>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>「只有一組解」是一個很大的簡化。</strong>"
       "找到就可以立刻 return True 一路傳回去，不用繼續搜。"
       "如果要「找出所有解」，就不能提早結束，複雜度會高很多。",
       "<strong>必須原地修改 <code>board</code></strong>，函式回傳 <code>None</code>。"
       "在 Python 裡記得用 <code>board[r][c] = ch</code> 而不是重新綁定。",
       "<strong>沒有時間限制的明文要求</strong>，但 LeetCode 的測資包含一些"
       "刻意設計的難題（空格多、線索少）。"
       "<strong>沒有 MRV 剪枝的版本在某些測資上會 TLE。</strong>",
     ]),
   ]),
 ],
 "idea": [
   ("c", """兩個版本：

一、樸素回溯
    - 每次檢查候選時掃 9+9+9 格
    - 按順序填格子（左上到右下）
    - 好寫、好懂，一般題目能過

二、位元遮罩 + MRV
    - 候選檢查是三次位元運算
    - 每次挑「候選最少」的格子先填
    - 快幾十到幾百倍，難題也能瞬間解完

建議：面試時寫版本一並說明，
      主動提到「可以用位元遮罩加速、用 MRV 剪枝」。
      如果面試官有興趣再寫版本二。"""),
 ],
 "approaches": [
   ap("解法一", "樸素回溯（先把框架寫對）", [
     ("c", S["p37_plain"]),
     ("h", "用 <code>pos</code>（0..80）而不是 <code>(r, c)</code> 的好處"),
     "只要一個整數就能表示進度，遞迴呼叫是 <code>solve(pos + 1)</code>，"
     "不用處理「行走到底要換列」的邏輯。"
     "<code>r, c = divmod(pos, 9)</code> 一行還原。",
     ("h", "「撤銷」那一行為什麼不能省？"),
     ("c", """board[r][c] = ch
if solve(pos + 1):
    return True
board[r][c] = "."        <- 這一行

如果不寫，失敗的嘗試會留在盤面上，
後面的檢查就會被這些「假資料」誤導。

一個直觀的檢驗：
    回溯函式應該滿足「進去時盤面是什麼樣，
    失敗回來時盤面還是那樣」。
    這叫做「狀態的可逆性」，
    是所有回溯演算法的正確性基礎。"""),
     ("h", "為什麼 <code>ok()</code> 不用檢查 <code>board[r][c]</code> 自己？"),
     "因為呼叫 <code>ok()</code> 的時候那一格還是 <code>'.'</code>，不會和 <code>ch</code> 相等。"
     "如果改成「先填再檢查」的寫法，就必須排除自己 —— 那樣比較容易寫錯。",
     "<strong>複雜度</strong>：理論上界是 O(9^m)（m = 空格數），"
     "但實際上剪枝（只試合法候選）讓它遠遠低於這個數。"
     "<strong>對「數獨」這個特定的固定大小問題，談漸近複雜度意義不大</strong> —— "
     "真正重要的是實測：這個版本解一般難度的題目大約幾毫秒，"
     "解刻意設計的難題可能要幾秒。",
   ], "最壞 O(9^m)", "O(m)", "m = 空格數；剪枝後遠低於上界", "遞迴深度 m"),

   ap("解法二", "位元遮罩 + MRV 啟發式（快幾十倍）", [
     ("c", S["p37_bitmask"]),
     ("h", "改進 1：位元遮罩取代逐格掃描"),
     ("c", """樸素版檢查一個候選要掃 27 格。
位元版只要：

    b = (r // 3) * 3 + c // 3
    candidates = FULL & ~(rows[r] | cols[c] | boxes[b])

一次算出「這一格可以填哪些數字」，三次位元運算。

用到的技巧：
    FULL = 0x1FF = 0b111111111     九個候選全開
    mask & -mask                   取出最低位的 1
    mask -= bit                    清掉那一位（也可以寫 mask &= mask - 1）
    bit.bit_length()               1<<0 -> 1, 1<<8 -> 9，剛好是數字本身

    rows[r] ^= bit                 撤銷（XOR 當切換用）"""),
     ("h", "改進 2：MRV（minimum remaining values）"),
     ("c", """不要按順序填格子，而是每次都挑「候選最少」的那一格。

為什麼有效？
    假設有兩個空格：
        格 A 有 7 個候選
        格 B 有 2 個候選

    先填 A：搜尋樹這一層有 7 個分支
    先填 B：只有 2 個分支

    而且先填 B 之後，B 的值會進一步限制 A 的候選 ——
    可能讓 A 從 7 個降到 3 個。

    反過來先填 A 的話，每個分支都還要再面對 B。

這是約束滿足問題（CSP）裡最有名的啟發式，
也叫「fail-first principle」：
    優先處理最受限制的變數，
    因為如果這條路走不通，越早發現越好。

特例：候選數 == 1 -> 唯一解，直接填，不用分支（這叫 naked single）
      候選數 == 0 -> 這一格無解，整個分支立刻剪掉

程式碼裡 if cnt <= 1: break 就是在利用第一種情況 ——
找到「只有一個候選」的格子就不必再比了，它一定是最好的選擇。"""),
     ("h", "為什麼用「交換」而不是重新排序？"),
     ("c", """empties[k], empties[best_i] = empties[best_i], empties[k]

把選中的格子換到位置 k，
這樣 empties[k:] 永遠是「還沒填的格子」。

遞迴回來之後要換回去 —— 這也是「撤銷」的一部分。
（實際上換不換回去對正確性沒有影響，
  因為 empties[k:] 的「集合」不變，只是順序。
  但換回去讓「狀態可逆」的性質完整，比較不容易出錯。）

這個「選中的元素換到前面」的技巧，
在選擇排序、快速選擇、以及所有「每次挑一個最好的」的演算法裡都會用到。"""),
     ("h", "實測差距"),
     ("c", """在「世界最難數獨」之一（只有 21 個線索）上：

    樸素回溯：      數秒到數十秒（視實作而定）
    位元 + MRV：    數毫秒

差距主要來自 MRV ——
它讓搜尋樹的分支因子從平均 3~4 降到接近 1，
搜尋樹從「寬而深」變成「幾乎是一條線」。

位元遮罩則是把每個節點的成本從 27 次比較降到 3 次運算，
帶來大約 5~10 倍的常數加速。"""),
   ], "實測毫秒級", "O(m)", "MRV 讓分支因子接近 1", "三組遮罩 + 遞迴深度 m", optimal=True),
 ],
 "compare": (["解法", "候選檢查", "填格順序", "難題表現", "行數"],
   [["一、樸素回溯", "掃 27 格", "左上到右下", "可能數秒", "25"],
    ["二、位元 + MRV", "3 次位元運算", "候選最少優先", "毫秒", "55"]]),
 "post": [
   ("note", "還能再加的剪枝（如果你想寫一個真正的數獨引擎）", [
     ("ul", [
       "<strong>Hidden single</strong>：某個數字在一列／行／宮裡只剩一個位置能放 —— 直接填。"
       "這是人類解數獨最常用的技巧，比 naked single 更有威力。",
       "<strong>Constraint propagation</strong>：每填一格就把影響傳播出去，"
       "反覆套用 naked/hidden single 直到不動為止，才進入下一層搜尋。"
       "Peter Norvig 的著名數獨程式就是這個架構，"
       "它能在不搜尋的情況下解掉大部分題目。",
       "<strong>Dancing Links（DLX）</strong>：把數獨轉成「精確覆蓋問題」"
       "（exact cover），用 Knuth 的 Algorithm X + 雙向十字鏈結串列求解。"
       "這是理論上最優雅的做法 —— 數獨的 729 個「可能的填法」對上 324 個約束，"
       "解數獨就變成「選出一組列，讓每個約束恰好被覆蓋一次」。"
       "<strong>但實作複雜度高很多，面試絕對不會要求。</strong>",
     ]),
   ]),
 ],
 "edges": [
   "<strong>盤面已經填滿</strong>：<code>empties</code> 是空的，<code>solve(0)</code> 立刻回 True。",
   "<strong>幾乎全空</strong>：只有一兩個線索。MRV 在這裡最有價值（樸素版會很慢）。",
   "<strong>刻意設計的難題</strong>：17 個線索是「有唯一解的最少線索數」（2012 年被證明）。"
   "這類題目是測試剪枝效果的標準測資。",
   "<strong>撤銷不完整</strong>：忘記 <code>board[r][c] = \".\"</code> 或漏了某個遮罩的 XOR，"
   "會得到錯誤的解或無限搜尋。<strong>撤銷必須和「做」完全對稱。</strong>",
   "<strong>修改到原有的數字</strong>：<code>empties</code> 只收集 <code>'.'</code> 的位置，"
   "所以原有數字不會被動到。樸素版靠 <code>if board[r][c] != \".\": return solve(pos+1)</code>。",
 ],
 "follow": [
   ("h", "追問一：如果要找出「所有」解呢？"),
   "把 <code>if solve(k+1): return True</code> 改成 <code>solve(k+1)</code>（不提早結束），"
   "並在 <code>k == len(empties)</code> 時記錄一份盤面的複本。"
   "<strong>但要注意：解的數量可能非常大</strong>（完全空的盤面有約 6.67 × 10²¹ 種解），"
   "所以通常會限制「最多找 N 個」。",
   ("h", "追問二：怎麼判斷一個盤面有幾組解？"),
   "同上，但找到第 2 組就可以停 —— 「唯一解」只要證明「不存在第 2 組」。"
   "這是數獨出題程式的核心：挖掉一個數字，檢查是否仍然唯一解，不唯一就放回去。",
   ("h", "追問三：解數獨是 NP-complete 嗎？"),
   "<strong>一般化的 n²×n² 數獨是 NP-complete 的</strong>（1周2003 年由 Yato 和 Seta 證明）。"
   "但 9×9 是固定大小，理論上是 O(1) —— "
   "所以「數獨是 NP-complete」這句話只在談一般化版本時才有意義。",
   "<strong>這是一個很好的提醒：漸近複雜度只對「規模可以變大」的問題有意義。</strong>"
   "對固定大小的問題，唯一有意義的指標是實測。",
   ("h", "追問四：這題的技巧還能用在哪？"),
   "任何<strong>約束滿足問題（CSP）</strong>："
   "N 皇后（第 51 題）、圖著色、課表排程、拼圖、"
   "以及各種「把東西放進格子且不能衝突」的問題。"
   "<strong>「位元遮罩表示候選集合」+「MRV 選變數」是這一整類問題的通用武器。</strong>",
 ],
 "related": [
   "<strong>第 36 題 Valid Sudoku</strong> —— 這題的前置，同一套遮罩",
   "<strong>第 51／52 題 N-Queens</strong> —— 另一個 CSP + 位元遮罩的經典",
   "<strong>第 79 題 Word Search</strong> —— 網格上的回溯",
   "<strong>第 39／40／46／47 題</strong> —— 回溯家族",
 ],
 "check": [
   "「撤銷」那幾行如果漏掉一個，會發生什麼？請說明為什麼「狀態可逆」是回溯的正確性基礎。",
   "MRV 為什麼能大幅縮小搜尋樹？請用「A 有 7 個候選、B 有 2 個候選」的例子說明。",
   "<code>mask & -mask</code> 在做什麼？<code>bit.bit_length()</code> 為什麼剛好是那個數字？",
   "如果要找出所有解，要改哪幾行？為什麼通常要加上數量上限？",
 ],
})
print("P37 written")

# ==================== 38. Count and Say ====================
S["p38_loop"] = '''class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            out = []
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:   # 數這一段有幾個相同的
                    j += 1
                out.append(str(j - i))               # 幾個
                out.append(s[i])                     # 什麼
                i = j
            s = "".join(out)
        return s'''

S["p38_groupby"] = '''from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            # groupby 會把「連續相同」的元素分成一組，正是我們要的
            s = "".join(str(len(list(g))) + ch for ch, g in groupby(s))
        return s'''

S["p38_regex"] = '''import re

class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            # (.)\\1* = 一個字元，後面接任意多個「和它一樣」的字元
            s = re.sub(r"(.)\\1*", lambda m: str(len(m.group(0))) + m.group(1), s)
        return s'''

_p38 = [S.load(k) for k in ("p38_loop", "p38_groupby", "p38_regex")]
_EXPECT = ["1", "11", "21", "1211", "111221", "312211", "13112221", "1113213211"]
for i, e in enumerate(_EXPECT, start=1):
    for sol in _p38:
        assert sol.countAndSay(i) == e, ("P38", i, sol, sol.countAndSay(i), e)
for n in range(1, 25):
    vals = set(sol.countAndSay(n) for sol in _p38)
    assert len(vals) == 1, ("P38 mismatch", n, vals)
print("P38 solutions OK")

emit({
 "num": 38, "slug": "count-and-say",
 "en": [
   "The <strong>count-and-say</strong> sequence is a sequence of digit strings defined by the "
   "recursive formula: <code>countAndSay(1) = \"1\"</code>, and "
   "<code>countAndSay(n)</code> is the way you would \"say\" the digit string from "
   "<code>countAndSay(n-1)</code>.",
   "To determine how you \"say\" a digit string, split it into the <strong>minimal</strong> "
   "number of substrings such that each substring contains exactly <strong>one unique digit</strong>. "
   "Then for each substring, say the number of digits, then say the digit.",
   "Given a positive integer <code>n</code>, return the <code>n</code>-th term of the "
   "count-and-say sequence.",
 ],
 "zh": [
   "<strong>外觀數列</strong>的定義是遞迴的："
   "<code>countAndSay(1) = \"1\"</code>，"
   "而 <code>countAndSay(n)</code> 就是把 <code>countAndSay(n-1)</code> "
   "<strong>「讀出來」</strong>的結果。",
   "所謂「讀出來」：把字串切成<strong>最少</strong>的幾段，讓每一段都只含<strong>同一個數字</strong>；"
   "然後對每一段，先說<strong>有幾個</strong>，再說<strong>是什麼數字</strong>。",
   "給你一個正整數 <code>n</code>，回傳外觀數列的第 <code>n</code> 項。",
 ],
 "pre": [
   ("note", "先把前幾項唸出來", [
     ("c", """n=1:  "1"
          讀作「一個 1」

n=2:  "11"
          讀作「兩個 1」

n=3:  "21"
          讀作「一個 2、一個 1」

n=4:  "1211"
          讀作「一個 1、一個 2、兩個 1」

n=5:  "111221"
          讀作「三個 1、兩個 2、一個 1」

n=6:  "312211"
          讀作「一個 3、一個 1、兩個 2、兩個 1」

n=7:  "13112221"

n=8:  "1113213211"

重點：這是「描述上一項長什麼樣」，不是任何數學運算。
所以它有時候被叫做「look-and-say sequence」。

常見誤解：以為 n=4 的 "1211" 要唸成「一千二百一十一」——
不是的，是逐字元讀「1、2、1、1」然後分組。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：n = 1
  輸出："1"

範例 2
  輸入：n = 4
  輸出："1211"
  說明：
    countAndSay(1) = "1"
    countAndSay(2) = 讀 "1" = 一個 1 = "11"
    countAndSay(3) = 讀 "11" = 兩個 1 = "21"
    countAndSay(4) = 讀 "21" = 一個 2、一個 1 = "1211\"""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 30",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 30</strong>。為什麼是 30？因為<strong>字串長度成指數成長</strong>。"
       "第 30 項有 5808 個字元，第 40 項會有大約 7 萬個，第 60 項超過 800 萬個。",
       "<strong>沒有捷徑。</strong>要算第 n 項就必須先算出前 n−1 項 —— "
       "這是一個純粹的模擬題，沒有公式可以直接跳到第 n 項。",
       "<strong>輸出是字串不是數字。</strong>"
       "第 30 項有 5808 位數，遠超任何整數型別。",
     ]),
   ]),
 ],
 "idea": [
   "核心操作叫做 <strong>run-length encoding（連續長度編碼，RLE）</strong>："
   "把「連續相同的一段」壓縮成「數量 + 內容」。",
   ("c", """RLE 在真實世界的應用：

    傳真機（Group 3/4 fax）     壓縮黑白掃描的長條紋
    BMP / TIFF / PCX 圖檔       壓縮大面積同色區域
    遊戲的點陣圖                同上
    資料庫的欄式儲存             壓縮排序後大量重複的欄位

這題等於是「對同一個字串反覆做 RLE」。
有趣的是：RLE 本來是用來「壓縮」的，
但在這裡它反而讓字串越來越長 ——
因為輸入的重複性不夠高（每段平均只有 1.x 個字元）。

這是一個很好的提醒：
壓縮演算法只在「資料有它預期的那種冗餘」時才有效。"""),
 ],
 "approaches": [
   ap("解法一", "手寫分組（面試該寫的版本）", [
     ("c", S["p38_loop"]),
     ("h", "雙指標分組的標準骨架"),
     ("c", """i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1
    # 此時 s[i:j] 是一整段相同的字元
    處理這一段
    i = j

這個骨架在所有「把連續相同的元素分組」的題目都會用到。

追一遍 s = "111221"：
    i=0: j 跑到 3（三個 1）  -> 輸出 "31"，i=3
    i=3: j 跑到 5（兩個 2）  -> 輸出 "22"，i=5
    i=5: j 跑到 6（一個 1）  -> 輸出 "11"，i=6
    結果 "312211" ✔"""),
     "<strong>用 list + join 而不是字串相加</strong>："
     "Python 的字串不可變，<code>out += x</code> 每次都會複製整條字串，"
     "在第 30 項（5808 字元）時會慢上許多。",
     "<strong>迴圈跑 <code>n - 1</code> 次</strong>，因為 <code>s</code> 的初值已經是第 1 項了。"
     "<code>n = 1</code> 時迴圈不跑，直接回 <code>\"1\"</code> ✔",
   ], "O(總輸出長度)", "O(最後一項的長度)", "每一項掃一遍",
      "只存目前和下一項", optimal=True),

   ap("解法二", "itertools.groupby（Python 的一行版）", [
     ("c", S["p38_groupby"]),
     ("c", """groupby("111221") 產生：
    ('1', <三個 '1' 的迭代器>)
    ('2', <兩個 '2' 的迭代器>)
    ('1', <一個 '1' 的迭代器>)

注意 groupby 只分「連續相同」的組，不會把分散的相同元素合併 ——
這正好就是 RLE 要的語意。

（如果要把所有相同的合併，得先排序，那是另一回事。）

len(list(g)) 要把迭代器轉成 list 才能數長度。
不能用 len(g) —— g 是迭代器，沒有長度。
也要注意 g 只能消耗一次。"""),
     "<strong>一行寫完，而且語意精確。</strong>"
     "面試時可以寫，但建議先寫解法一 —— "
     "<code>groupby</code> 是 Python 特有的，換成別的語言就沒有了。",
   ], "O(總輸出長度)", "O(最後一項的長度)", "同上", "同上"),

   ap("解法三", "正規表示式（最短，也最炫技）", [
     ("c", S["p38_regex"]),
     ("h", "<code>(.)\\1*</code> 逐字拆解"),
     ("c", """(.)      擷取任意一個字元，存成群組 1
\\1       反向參照（backreference）：「和群組 1 一樣的字元」
*        零個或多個

所以 (.)\\1* 匹配「一個字元 + 它自己的任意多個重複」
    = 一整段連續相同的字元

對 "111221" 的匹配結果：
    "111"  group(1) = "1"
    "22"   group(1) = "2"
    "1"    group(1) = "1"

替換函式：
    lambda m: str(len(m.group(0))) + m.group(1)
              ^整段的長度            ^那個字元
    "111" -> "31"
    "22"  -> "22"
    "1"   -> "11\""""),
     "<strong>反向參照 <code>\\1</code> 是關鍵</strong>，"
     "它讓 regex 能表達「和前面一樣」這種依賴關係。"
     "<strong>注意：有反向參照的正規表示式不再是「正規語言」</strong> —— "
     "它超出了有限狀態機的能力，所以只能用回溯式引擎實作"
     "（RE2 和 Go 的 <code>regexp</code> 就不支援反向參照）。",
     "面試時寫這個要能解釋清楚，否則會被認為是背來的。"
     "而且它比解法一慢（regex 引擎有額外負擔）。",
   ], "O(總輸出長度)", "O(最後一項的長度)", "regex 引擎掃一遍", "同上"),
 ],
 "compare": (["解法", "行數", "可移植性", "速度", "備註"],
   [["一、手寫分組", "13", "★★★★★", "最快", "面試預設"],
    ["二、groupby", "5", "★★☆☆☆", "快", "Python 專用，語意精確"],
    ["三、regex", "5", "★★★☆☆", "較慢", "反向參照的好例子"]]),
 "edges": [
   "<strong><code>n = 1</code></strong> → <code>\"1\"</code>。迴圈一次都不跑。",
   "<strong><code>n = 2</code></strong> → <code>\"11\"</code>。第一次迭代。",
   "<strong><code>n = 30</code></strong> → 5808 個字元。要確認不會 TLE（字串相加的寫法可能會）。",
   "<strong>長度為 1 的段</strong>：<code>\"21\"</code> → <code>\"1211\"</code>。"
   "每一段都是一個字元，考驗分組邏輯。",
   "<strong>長度 ≥ 3 的段</strong>：<code>\"111221\"</code> → <code>\"312211\"</code>。",
   "<strong>絕對不會出現 4 個以上連續相同</strong>（這是這個數列的一個已知性質），"
   "所以「數量」永遠是一位數。但你的程式不應該假設這件事。",
 ],
 "follow": [
   ("h", "追問一：字串長度是怎麼成長的？"),
   "<strong>每一項的長度大約是上一項的 1.303577 倍。</strong>"
   "這個常數叫做 <strong>Conway 常數</strong>，"
   "它是一個 71 次多項式的唯一正實根。",
   "John Conway（就是發明「生命遊戲」的那位）在 1986 年研究了這個數列，"
   "證明了一個驚人的結果：<strong>宇宙定理（Cosmological Theorem）</strong> —— "
   "無論起始字串是什麼（除了 <code>\"22\"</code>），"
   "數列最終都會分解成 <strong>92 個「基本元素」</strong>的組合，"
   "而且它們永遠不會互相干擾。"
   "Conway 用化學元素的名字（氫、氦、鋰…鈾）替這 92 個字串命名，"
   "所以這個理論真的被叫做「look-and-say 的化學」。",
   ("h", "追問二：<code>\"22\"</code> 為什麼特別？"),
   "因為 <code>\"22\"</code> 讀作「兩個 2」= <code>\"22\"</code> —— "
   "<strong>它是唯一的不動點</strong>，永遠不會變。"
   "是這個數列裡唯一不會成長的起始值。",
   ("h", "追問三：這個數列裡會出現哪些數字？"),
   "從 <code>\"1\"</code> 開始的話，<strong>只會出現 1、2、3</strong>。"
   "因為可以證明「連續相同的字元最多 3 個」。"
   "（直覺：如果出現 <code>\"1111\"</code>，那它的前一項要讀出「一個 1、一個 1」這種形式，"
   "但相鄰的兩個「一個 1」會被合併成「兩個 1」—— 矛盾。"
   "完整的證明要枚舉幾種情況。）",
   ("h", "追問四：能不能用 DP 或矩陣快速冪跳到第 n 項？"),
   "<strong>如果只要「長度」可以</strong> —— "
   "利用 Conway 的 92 個元素，可以寫出一個 92×92 的轉移矩陣，"
   "用矩陣快速冪在 O(92³ log n) 算出第 n 項的長度。"
   "但如果要<strong>完整的字串</strong>，就沒辦法 —— 輸出本身就是指數大的。",
 ],
 "related": [
   "<strong>第 443 題 String Compression</strong> —— 原地做 RLE",
   "<strong>第 271 題 Encode and Decode Strings</strong> —— 另一種編碼設計",
 ],
 "check": [
   "<code>countAndSay(5)</code> 是什麼？請從 <code>\"1\"</code> 一步一步推出來。",
   "雙指標分組的骨架是什麼？為什麼內層 while 的條件是 <code>s[j] == s[i]</code> 而不是 <code>s[j] == s[j-1]</code>？",
   "為什麼要用 <code>list</code> + <code>join</code> 而不是字串相加？在 n = 30 時差多少？",
   "<code>(.)\\1*</code> 裡的 <code>\\1</code> 是什麼？為什麼它讓這個 pattern 不再是「正規」的？",
 ],
})
print("P38 written")
