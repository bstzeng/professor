# -*- coding: utf-8 -*-
"""第 51–53 題。"""
import random
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(51)

# ==================== 51. N-Queens ====================
S["p51_sets"] = '''class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        cols = set()        # 已被佔用的「行」
        diag1 = set()       # 已被佔用的「↘ 對角線」，識別碼 r - c
        diag2 = set()       # 已被佔用的「↙ 對角線」，識別碼 r + c
        queens = []         # queens[r] = 第 r 列的皇后放在哪一行

        def backtrack(r: int) -> None:
            if r == n:
                out.append(["." * c + "Q" + "." * (n - c - 1) for c in queens])
                return

            for c in range(n):
                if c in cols or (r - c) in diag1 or (r + c) in diag2:
                    continue

                cols.add(c); diag1.add(r - c); diag2.add(r + c)
                queens.append(c)

                backtrack(r + 1)

                queens.pop()
                cols.remove(c); diag1.remove(r - c); diag2.remove(r + c)

        backtrack(0)
        return out'''

S["p51_bits"] = '''class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        out = []
        queens = []

        def backtrack(r: int, cols: int, d1: int, d2: int) -> None:
            if r == n:
                out.append(["." * c + "Q" + "." * (n - c - 1) for c in queens])
                return

            # 這一列還能放的位置（1 表示可放），只保留低 n 位
            avail = ~(cols | d1 | d2) & ((1 << n) - 1)

            while avail:
                bit = avail & -avail        # 取最低位的 1
                avail -= bit
                c = bit.bit_length() - 1    # 這個位元對應第幾行

                queens.append(c)
                # 往下一列時，對角線的遮罩要左右各平移一格
                backtrack(r + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1)
                queens.pop()

        backtrack(0, 0, 0, 0)
        return out'''

_p51 = [S.load(k) for k in ("p51_sets", "p51_bits")]
_COUNTS = [1, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724]


def _valid_board(board, n):
    pos = []
    for r, row in enumerate(board):
        assert len(row) == n and row.count("Q") == 1, ("bad row", row)
        pos.append(row.index("Q"))
    assert len(board) == n
    for a in range(n):
        for b in range(a + 1, n):
            assert pos[a] != pos[b], ("same col", board)
            assert abs(pos[a] - pos[b]) != b - a, ("diagonal", board)


for n in range(1, 9):
    for sol in _p51:
        res = sol.solveNQueens(n)
        assert len(res) == _COUNTS[n], ("P51 count", n, len(res), _COUNTS[n])
        assert len(set(map(tuple, res))) == len(res), ("P51 dup", n)
        for b in res:
            _valid_board(b, n)
    a = sorted(map(tuple, _p51[0].solveNQueens(n)))
    b = sorted(map(tuple, _p51[1].solveNQueens(n)))
    assert a == b, ("P51 mismatch", n)
print("P51 solutions OK")

_P51_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">兩條對角線的識別碼：↘ 用 r − c、↙ 用 r + c（同一條線上的格子，值都相同）</text>
            <g font-size="13" text-anchor="middle">
              <text x="150" y="52" fill="var(--accent)" font-size="12">r − c（↘ 方向）</text>
              <rect x="70" y="64" width="40" height="40" fill="none" stroke="var(--border)"/><text x="90" y="90" fill="var(--accent)">0</text>
              <rect x="110" y="64" width="40" height="40" fill="none" stroke="var(--border)"/><text x="130" y="90" fill="var(--text-muted)">−1</text>
              <rect x="150" y="64" width="40" height="40" fill="none" stroke="var(--border)"/><text x="170" y="90" fill="var(--text-muted)">−2</text>
              <rect x="190" y="64" width="40" height="40" fill="none" stroke="var(--border)"/><text x="210" y="90" fill="var(--text-muted)">−3</text>
              <rect x="70" y="104" width="40" height="40" fill="none" stroke="var(--border)"/><text x="90" y="130" fill="var(--text-muted)">1</text>
              <rect x="110" y="104" width="40" height="40" fill="none" stroke="var(--border)"/><text x="130" y="130" fill="var(--accent)">0</text>
              <rect x="150" y="104" width="40" height="40" fill="none" stroke="var(--border)"/><text x="170" y="130" fill="var(--text-muted)">−1</text>
              <rect x="190" y="104" width="40" height="40" fill="none" stroke="var(--border)"/><text x="210" y="130" fill="var(--text-muted)">−2</text>
              <rect x="70" y="144" width="40" height="40" fill="none" stroke="var(--border)"/><text x="90" y="170" fill="var(--text-muted)">2</text>
              <rect x="110" y="144" width="40" height="40" fill="none" stroke="var(--border)"/><text x="130" y="170" fill="var(--text-muted)">1</text>
              <rect x="150" y="144" width="40" height="40" fill="none" stroke="var(--border)"/><text x="170" y="170" fill="var(--accent)">0</text>
              <rect x="190" y="144" width="40" height="40" fill="none" stroke="var(--border)"/><text x="210" y="170" fill="var(--text-muted)">−1</text>
              <rect x="70" y="184" width="40" height="40" fill="none" stroke="var(--border)"/><text x="90" y="210" fill="var(--text-muted)">3</text>
              <rect x="110" y="184" width="40" height="40" fill="none" stroke="var(--border)"/><text x="130" y="210" fill="var(--text-muted)">2</text>
              <rect x="150" y="184" width="40" height="40" fill="none" stroke="var(--border)"/><text x="170" y="210" fill="var(--text-muted)">1</text>
              <rect x="190" y="184" width="40" height="40" fill="none" stroke="var(--border)"/><text x="210" y="210" fill="var(--accent)">0</text>
            </g>
            <g font-size="13" text-anchor="middle">
              <text x="450" y="52" fill="#ff8a65" font-size="12">r + c（↙ 方向）</text>
              <rect x="370" y="64" width="40" height="40" fill="none" stroke="var(--border)"/><text x="390" y="90" fill="var(--text-muted)">0</text>
              <rect x="410" y="64" width="40" height="40" fill="none" stroke="var(--border)"/><text x="430" y="90" fill="var(--text-muted)">1</text>
              <rect x="450" y="64" width="40" height="40" fill="none" stroke="var(--border)"/><text x="470" y="90" fill="#ff8a65">2</text>
              <rect x="490" y="64" width="40" height="40" fill="none" stroke="var(--border)"/><text x="510" y="90" fill="var(--text-muted)">3</text>
              <rect x="370" y="104" width="40" height="40" fill="none" stroke="var(--border)"/><text x="390" y="130" fill="var(--text-muted)">1</text>
              <rect x="410" y="104" width="40" height="40" fill="none" stroke="var(--border)"/><text x="430" y="130" fill="#ff8a65">2</text>
              <rect x="450" y="104" width="40" height="40" fill="none" stroke="var(--border)"/><text x="470" y="130" fill="var(--text-muted)">3</text>
              <rect x="490" y="104" width="40" height="40" fill="none" stroke="var(--border)"/><text x="510" y="130" fill="var(--text-muted)">4</text>
              <rect x="370" y="144" width="40" height="40" fill="none" stroke="var(--border)"/><text x="390" y="170" fill="#ff8a65">2</text>
              <rect x="410" y="144" width="40" height="40" fill="none" stroke="var(--border)"/><text x="430" y="170" fill="var(--text-muted)">3</text>
              <rect x="450" y="144" width="40" height="40" fill="none" stroke="var(--border)"/><text x="470" y="170" fill="var(--text-muted)">4</text>
              <rect x="490" y="144" width="40" height="40" fill="none" stroke="var(--border)"/><text x="510" y="170" fill="var(--text-muted)">5</text>
              <rect x="370" y="184" width="40" height="40" fill="none" stroke="var(--border)"/><text x="390" y="210" fill="var(--text-muted)">3</text>
              <rect x="410" y="184" width="40" height="40" fill="none" stroke="var(--border)"/><text x="430" y="210" fill="var(--text-muted)">4</text>
              <rect x="450" y="184" width="40" height="40" fill="none" stroke="var(--border)"/><text x="470" y="210" fill="var(--text-muted)">5</text>
              <rect x="490" y="184" width="40" height="40" fill="none" stroke="var(--border)"/><text x="510" y="210" fill="var(--text-muted)">6</text>
            </g>
            <text x="20" y="252" fill="var(--gold)" font-size="12">所以「這一格的對角線被佔了嗎」只要查兩個集合：(r − c) ∈ diag1？(r + c) ∈ diag2？</text>
            <text x="20" y="276" fill="var(--text-muted)" font-size="12">而「列」不用檢查 —— 因為我們一列只放一個皇后，逐列往下走。</text>'''

emit({
 "num": 51, "slug": "n-queens",
 "en": [
   "The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an "
   "<code>n x n</code> chessboard such that no two queens attack each other.",
   "Given an integer <code>n</code>, return <em>all distinct solutions to the "
   "<strong>n-queens puzzle</strong></em>. You may return the answer in any order.",
   "Each solution contains a distinct board configuration, where <code>'Q'</code> and "
   "<code>'.'</code> both indicate a queen and an empty space, respectively.",
 ],
 "zh": [
   "<strong>N 皇后問題</strong>：在 <code>n × n</code> 的西洋棋盤上放 <code>n</code> 個皇后，"
   "使得任意兩個皇后<strong>不會互相攻擊</strong>。",
   "皇后可以攻擊<strong>同一列、同一行、以及兩條對角線</strong>上的任何棋子。",
   "給你一個整數 <code>n</code>，回傳所有不同的擺法。"
   "每個解用一個字串陣列表示，<code>'Q'</code> 代表皇后，<code>'.'</code> 代表空格。",
 ],
 "pre": [
   ("note", "三個約束，各有各的編碼方式", [
     ("c", """皇后互不攻擊 = 任兩個皇后不在同一列、同一行、同一對角線

約束 1：列（row）
    我們「逐列往下放，每列剛好放一個」——
    這個約束就自動滿足了，完全不用檢查。

約束 2：行（column）
    用一個集合 cols 記錄「哪些行已經有皇后」。

約束 3：對角線
    ↘ 方向（左上到右下）：同一條線上 r - c 是定值
        (0,0) (1,1) (2,2) 的 r-c 都是 0
    ↙ 方向（右上到左下）：同一條線上 r + c 是定值
        (0,2) (1,1) (2,0) 的 r+c 都是 2

    所以用兩個集合 diag1（存 r-c）和 diag2（存 r+c）。

這個「用一個數字識別一條對角線」的技巧，
是所有棋盤類問題的基本功。"""),
     "<strong>N 皇后是回溯法的教科書範例</strong>（Wirth 1976 年的《Algorithms + Data Structures = Programs》裡就有），"
     "也是「約束滿足問題（CSP）」最經典的例子。",
   ]),
 ],
 "examples": """範例 1
  輸入：n = 4
  輸出：[[".Q..","...Q","Q...","..Q."],
        ["..Q.","Q...","...Q",".Q.."]]
  說明：4 皇后有兩組解。

        . Q . .        . . Q .
        . . . Q        Q . . .
        Q . . .        . . . Q
        . . Q .        . Q . .

範例 2
  輸入：n = 1
  輸出：[["Q"]]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 9",
 ],
 "mid": [
   ("note", "解的數量（值得記住，用來驗證程式）", [
     ("c", """n:     1   2   3   4   5    6   7    8    9     10
解數:  1   0   0   2   10   4   40   92   352   724

注意 n = 2 和 n = 3 是「無解」——
這不是 bug，是真的放不下。

n = 8（標準西洋棋盤）有 92 組解，
這是高斯在 1850 年就算出來的著名數字。
（他一開始還算錯了，說是 76 組。）

如果考慮旋轉和鏡射的對稱性，
n = 8 只有 12 組「本質上不同」的解。

n 到 27 為止的解數都已經被算出來（2016 年），
n = 27 有 234,907,967,154,122,528 組 ——
用了大量的平行運算才算完。
沒有已知的公式可以直接算出解數。"""),
   ]),
 ],
 "idea": [
   ("fig", _P51_FIG, "0 0 640 288"),
 ],
 "approaches": [
   ap("解法一", "回溯 + 三個集合（標準解）", [
     ("c", S["p51_sets"]),
     ("h", "為什麼不用檢查「列」？"),
     "因為 <code>backtrack(r)</code> 的語意就是「現在要在第 <code>r</code> 列放一個皇后」，"
     "而且放完就往 <code>r + 1</code> 走。"
     "<strong>「每列剛好一個」是由程式結構保證的，不需要額外的資料結構。</strong>",
     "<strong>這是一個很值得學的設計</strong>：把一個約束「編進演算法的結構裡」，"
     "而不是「用一個檢查去維護」。少一個資料結構，就少一個出錯的地方。",
     ("h", "撤銷必須完全對稱"),
     ("c", """做：
    cols.add(c); diag1.add(r - c); diag2.add(r + c)
    queens.append(c)

撤銷：
    queens.pop()
    cols.remove(c); diag1.remove(r - c); diag2.remove(r + c)

四個「做」對應四個「撤銷」，一個都不能少。

一個實用的檢查習慣：
    在 backtrack 的開頭和結尾各印一次三個集合的大小，
    它們應該完全相同。
    （正式程式碼裡可以寫成 assert。）"""),
     ("h", "產生輸出的那一行"),
     ("c", """["." * c + "Q" + "." * (n - c - 1) for c in queens]

queens[r] = c 表示第 r 列的皇后在第 c 行。
把它轉成字串：c 個點 + 一個 Q + (n-c-1) 個點。

例：n = 4, queens = [1, 3, 0, 2]
    r=0, c=1 -> ".Q.."
    r=1, c=3 -> "...Q"
    r=2, c=0 -> "Q..."
    r=3, c=2 -> "..Q."

只在「找到完整解」時才建字串，
所以字串建構的成本只和「解的數量」成正比，
不會拖慢搜尋本身。"""),
     ("h", "複雜度"),
     "理論上界是 O(n!)（第一列 n 種、第二列最多 n−1 種…），"
     "但剪枝讓實際搜尋的節點數遠低於此。"
     "n = 9 時只有 352 組解，整個搜尋在毫秒內完成。",
   ], "O(n!) 上界", "O(n)", "剪枝後遠低於上界",
      "三個集合 + queens + 遞迴深度；不算輸出", optimal=True),

   ap("解法二", "位元遮罩（更快，也更漂亮）", [
     "把三個集合換成三個整數的位元遮罩。"
     "<strong>對角線的部分有一個很巧妙的處理：不用算 <code>r ± c</code>，"
     "而是讓遮罩本身「跟著往下平移」。</strong>",
     ("c", S["p51_bits"]),
     ("h", "為什麼對角線遮罩要左移／右移？"),
     ("c", """假設第 r 列在第 c 行放了皇后。

它的 ↘ 對角線威脅到第 r+1 列的第 c+1 行、
                  第 r+2 列的第 c+2 行、…

所以「往下一列時，這個威脅的位置往右移一格」——
    d1 = (d1 | bit) << 1

同理 ↙ 對角線往左移：
    d2 = (d2 | bit) >> 1

而「行」的威脅位置不會變：
    cols = cols | bit

這個做法的漂亮之處：
    不需要計算 r - c 或 r + c，
    也不需要處理負數索引或偏移量，
    威脅的「傳播」直接由位移表示。

而且 << 1 之後超出 n 位的部分，
會被下一層的 & ((1 << n) - 1) 自動切掉 ——
對應「對角線走出棋盤外就消失了」。"""),
     ("h", "三個位元技巧"),
     ("c", """avail = ~(cols | d1 | d2) & ((1 << n) - 1)
    「三種威脅的聯集」取補集，再切到 n 位
    -> 這一列所有「可以放」的位置

bit = avail & -avail
    取出最低位的 1（二補數的經典技巧）
    -x = ~x + 1，所以 x & -x 只留下最低位的 1
    例：0b1011000 & -0b1011000 = 0b0001000

avail -= bit
    清掉剛剛取出的那一位
    也可以寫 avail &= avail - 1

c = bit.bit_length() - 1
    1 << k 的 bit_length() 是 k + 1
    所以減 1 就得到 k（第幾行）"""),
     ("h", "快多少？"),
     "在 n = 9 時，位元版大約比集合版快 3–5 倍"
     "（集合的雜湊運算比位元運算慢得多）。"
     "在 n = 14、15 這種「只數解、不列出」的場景，差距會到 10 倍以上。",
     "<strong>面試時先寫解法一</strong>（好解釋），"
     "再說「可以用位元遮罩加速，而且對角線可以用位移傳播」。"
     "這個「位移傳播」的想法通常會讓面試官眼睛一亮。",
   ], "O(n!) 上界", "O(n)", "位元運算取代雜湊", "三個整數 + 遞迴深度"),
 ],
 "compare": (["解法", "約束的表示", "速度", "好解釋？", "備註"],
   [["一、三個集合", "set of int", "基準", "★★★★★", "面試預設"],
    ["二、位元遮罩", "三個 int", "快 3–5 倍", "★★★☆☆", "對角線用位移傳播"]]),
 "edges": [
   "<strong>n = 1</strong> → <code>[[\"Q\"]]</code>（一組解）。",
   "<strong>n = 2、n = 3</strong> → <code>[]</code>（<strong>無解</strong>）。"
   "這不是 bug，要確認程式回傳空 list 而不是崩潰。",
   "<strong>n = 4</strong> → 2 組。最小的有解的非平凡情況。",
   "<strong>n = 8</strong> → 92 組。經典答案，拿來驗證。",
   "<strong>n = 9</strong> → 352 組。本題的上限。",
   "<strong>撤銷不完整</strong>：漏掉任一個 <code>remove</code>，"
   "後續搜尋會基於錯的狀態，通常會少找到很多解。",
   "<strong>對角線識別碼弄反</strong>："
   "<code>r - c</code> 和 <code>r + c</code> 互換不會出錯（兩個集合是對稱的），"
   "但如果兩個都用 <code>r - c</code>，就會漏檢查一個方向。",
 ],
 "follow": [
   ("h", "追問一：如果只要「有幾組解」而不要列出來呢？"),
   "第 52 題（N-Queens II）。"
   "把 <code>out.append(...)</code> 改成 <code>count += 1</code>，"
   "並且拿掉 <code>queens</code> 這個 list —— 就這樣。"
   "<strong>位元版在這裡優勢最大</strong>，因為完全不用建字串。",
   ("h", "追問二：能不能利用對稱性加速？"),
   "可以。棋盤有 8 種對稱（4 種旋轉 × 2 種鏡射）。"
   "<strong>只搜尋「第一列的皇后在左半邊」的情況，"
   "再把結果鏡射過去</strong>，可以省掉接近一半的搜尋。"
   "n 是奇數時中間那一行要特別處理（它鏡射到自己）。"
   "這是計算大 n 的解數時的標準技巧。",
   ("h", "追問三：n 很大時（例如 n = 1000）呢？"),
   "<strong>如果只要「找出一組解」而不是「全部」，有 O(n) 的構造法。</strong>",
   ("c", """對 n > 3，存在直接的構造公式（依 n mod 6 分情況）：

  n mod 6 不是 2 也不是 3：
      偶數列放 2, 4, 6, ..., n
      奇數列放 1, 3, 5, ..., n-1

  其他情況要做一些調整。

這是 1969 年 Hoffman 等人給出的結果。

所以「找一組解」是 O(n)，
但「找出所有解」或「數出解的數量」仍然沒有多項式演算法 ——
這是一個很好的對比：
    「存在性」和「計數」可以有天差地遠的難度。""",),
   ("h", "追問四：N 皇后是 NP-complete 嗎？"),
   "<strong>「找一組解」不是</strong>（有 O(n) 構造法）。"
   "但一個相關的問題 —— <strong>「給定一個已經放了幾個皇后的殘局，"
   "能不能補完？」</strong> —— 在 2017 年被證明是 NP-complete"
   "（Gent、Jefferson、Nightingale）。",
   "<strong>這是一個很好的提醒</strong>：問題的微小變化可以徹底改變它的複雜度。",
 ],
 "related": [
   "<strong>第 52 題 N-Queens II</strong> —— 只數數量",
   "<strong>第 37 題 Sudoku Solver</strong> —— 另一個 CSP + 位元遮罩",
   "<strong>第 46／47 題 Permutations</strong> —— 「每列一個」其實就是一個排列",
   "<strong>第 79 題 Word Search</strong> —— 網格上的回溯",
 ],
 "check": [
   "為什麼不需要檢查「同一列」這個約束？",
   "為什麼 <code>r - c</code> 能識別一條 ↘ 對角線？<code>r + c</code> 呢？",
   "位元版為什麼對角線遮罩要 <code>&lt;&lt; 1</code> 和 <code>&gt;&gt; 1</code>？它在表達什麼？",
   "<code>avail &amp; -avail</code> 在做什麼？為什麼它能取出最低位的 1？",
 ],
})
print("P51 written")

# ==================== 52. N-Queens II ====================
S["p52_bits"] = '''class Solution:
    def totalNQueens(self, n: int) -> int:
        FULL = (1 << n) - 1

        def backtrack(cols: int, d1: int, d2: int) -> int:
            if cols == FULL:            # n 個皇后都放好了
                return 1

            count = 0
            avail = ~(cols | d1 | d2) & FULL
            while avail:
                bit = avail & -avail
                avail -= bit
                count += backtrack(cols | bit,
                                   (d1 | bit) << 1 & FULL,
                                   (d2 | bit) >> 1)
            return count

        return backtrack(0, 0, 0)'''

S["p52_sym"] = '''class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return 1
        FULL = (1 << n) - 1

        def backtrack(cols: int, d1: int, d2: int) -> int:
            if cols == FULL:
                return 1
            count = 0
            avail = ~(cols | d1 | d2) & FULL
            while avail:
                bit = avail & -avail
                avail -= bit
                count += backtrack(cols | bit,
                                   (d1 | bit) << 1 & FULL,
                                   (d2 | bit) >> 1)
            return count

        # 鏡射對稱：第一列放在左半邊的解，鏡射過去就是右半邊的解
        total = 0
        for c in range(n // 2):
            bit = 1 << c
            total += backtrack(bit, bit << 1, bit >> 1)
        total *= 2

        # n 是奇數時，第一列放正中間的情況要單獨算（它鏡射到自己）
        if n % 2:
            bit = 1 << (n // 2)
            total += backtrack(bit, bit << 1, bit >> 1)

        return total'''

_p52 = [S.load(k) for k in ("p52_bits", "p52_sym")]
_COUNTS52 = [None, 1, 0, 0, 2, 10, 4, 40, 92, 352]
for n in range(1, 10):
    for sol in _p52:
        assert sol.totalNQueens(n) == _COUNTS52[n], ("P52", n, sol, sol.totalNQueens(n))
print("P52 solutions OK")

emit({
 "num": 52, "slug": "n-queens-ii",
 "en": [
   "The <strong>n-queens</strong> puzzle is the problem of placing <code>n</code> queens on an "
   "<code>n x n</code> chessboard such that no two queens attack each other.",
   "Given an integer <code>n</code>, return <em>the number of distinct solutions to the "
   "<strong>n-queens puzzle</strong></em>.",
 ],
 "zh": [
   "<strong>N 皇后問題</strong>：在 <code>n × n</code> 棋盤上放 <code>n</code> 個皇后，"
   "使得任兩個不會互相攻擊。",
   "給你一個整數 <code>n</code>，回傳<strong>不同解法的數量</strong>（不需要列出棋盤）。",
 ],
 "pre": [
   ("note", "和第 51 題只差一行", [
     ("c", """第 51 題：out.append(棋盤字串)
第 52 題：count += 1

其他完全一樣。

但「只要數量」讓我們可以做兩個第 51 題做不到的優化：

  ① 完全不用維護 queens 這個 list，也不用建字串
     -> 省掉大量的記憶體配置

  ② 可以利用「鏡射對稱」：
     把棋盤左右翻轉，一組解會變成另一組解。
     所以「第一列放在左半邊」的解，數量和「放在右半邊」的一樣。
     只算一半再乘 2 -> 搜尋量減半。

     （第 51 題也能用，但要把每組解鏡射回去，
       程式碼變複雜，而且省下的時間被建字串吃掉了。）"""),
   ]),
 ],
 "examples": """範例 1
  輸入：n = 4
  輸出：2

範例 2
  輸入：n = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 9",
 ],
 "mid": [
   ("note", "答案表（用來驗證）", [
     ("c", """n:     1   2   3   4   5    6   7    8    9
解數:  1   0   0   2   10   4   40   92   352

n = 2、3 無解。
n = 6 只有 4 組，比 n = 5 的 10 組還少 ——
解數不是單調遞增的，這常讓人以為程式寫錯了。"""),
   ]),
 ],
 "idea": [
   "既然第 51 題已經講完了回溯和位元遮罩的原理，這裡直接看兩個優化版本。",
 ],
 "approaches": [
   ap("解法一", "位元遮罩計數（標準解）", [
     ("c", S["p52_bits"]),
     ("h", "終止條件用 <code>cols == FULL</code> 而不是 <code>r == n</code>"),
     ("c", """因為我們連「現在是第幾列」都不需要記！

    cols 是「已經被佔用的行」的遮罩。
    每放一個皇后就多佔一行。
    所以 cols 的 1 位元個數 == 已經放了幾個皇后 == 目前在第幾列。

    cols == FULL（全部 n 位都是 1）
        <=> 放了 n 個皇后
        <=> 走到底了 ✔

這讓遞迴函式只需要三個參數，完全不用傳 r。
是位元表示法的一個附帶好處。"""),
     ("h", "<code>(d1 | bit) &lt;&lt; 1 &amp; FULL</code> 的 <code>&amp; FULL</code>"),
     "左移之後可能超出 n 位，<code>&amp; FULL</code> 把超出的部分切掉 —— "
     "對應「對角線走出棋盤右邊就消失了」。"
     "<strong>不切的話遮罩會無限變大</strong>，"
     "在 Python 裡不會出錯（任意精度整數）但會愈來愈慢；"
     "在 C/Java 裡則會影響正確性。",
     "<code>(d2 | bit) &gt;&gt; 1</code> 不用切，因為右移只會讓位元變少。",
   ], "O(n!) 上界", "O(n)", "純位元運算，沒有字串建構", "三個整數 + 遞迴深度", optimal=True),

   ap("解法二", "再加上鏡射對稱（搜尋量減半）", [
     "把棋盤<strong>左右鏡射</strong>，一組合法解會變成另一組合法解"
     "（攻擊關係在鏡射下保持不變）。",
     ("c", S["p52_sym"]),
     ("c", """n = 8，第一列可以放在第 0..7 行。

    第一列放第 0 行的解數  ==  第一列放第 7 行的解數
    第一列放第 1 行的解數  ==  第一列放第 6 行的解數
    第一列放第 2 行的解數  ==  第一列放第 5 行的解數
    第一列放第 3 行的解數  ==  第一列放第 4 行的解數

    所以只要算 c = 0, 1, 2, 3 這四種，再 × 2 就好。
    搜尋量剛好減半。

n = 9（奇數）：
    c = 0..3 算完 × 2，
    再單獨加上 c = 4（正中間）的解數 ——
    因為它鏡射之後還是自己，不能乘 2。

驗證 n = 8：
    c=0: 4 組    c=1: 8 組    c=2: 16 組    c=3: 18 組
    (4+8+16+18) × 2 = 46 × 2 = 92 ✔"""),
     "<strong>只能用鏡射，不能用旋轉。</strong>"
     "旋轉 90° 也會把解變成解，但<strong>它會改變「第一列的皇后在哪」這個分類</strong>，"
     "沒辦法簡單地用「乘以 4」來計數（有些解在旋轉下是自己，要扣掉重複）。"
     "正確處理旋轉對稱要用 Burnside 引理，複雜很多。",
     "<strong>左右鏡射是安全的</strong>，因為它保持「第一列」還是第一列，"
     "只是把行號 <code>c</code> 變成 <code>n-1-c</code>。",
   ], "O(n!) 上界，常數減半", "O(n)", "只搜一半的第一列",
      "三個整數 + 遞迴深度"),
 ],
 "compare": (["解法", "搜尋量", "n=9 相對耗時", "備註"],
   [["第 51 題的集合版 + 計數", "100%", "最慢", "會建 queens list"],
    ["一、位元遮罩", "100%", "約 1/4", "不建字串"],
    ["二、位元 + 鏡射", "50%", "約 1/8", "n 是奇數時要處理中間"]]),
 "edges": [
   "<strong>n = 1</strong> → 1。<strong>鏡射版要特判</strong>："
   "<code>n // 2 = 0</code>，for 迴圈不跑，只有「奇數的中間」那一段會執行，"
   "剛好算對 —— 但寫 <code>if n == 1: return 1</code> 更保險也更清楚。",
   "<strong>n = 2、3</strong> → 0。搜尋會全部失敗，回傳 0。",
   "<strong>n = 6</strong> → 4。比 n = 5 的 10 還少，不要以為寫錯了。",
   "<strong>n = 8</strong> → 92。經典驗證值。",
   "<strong>n 是奇數</strong>：鏡射版一定要單獨處理中間那一行，"
   "否則 n = 5 會算出 8 而不是 10。",
   "<strong>忘記 <code>&amp; FULL</code></strong>：在 Python 裡答案仍然正確"
   "（因為 <code>avail</code> 那一行也有 <code>&amp; FULL</code>），"
   "但 <code>d1</code> 會無限制地變大，愈來愈慢。",
 ],
 "follow": [
   ("h", "追問一：n 更大時能算到多少？"),
   ("c", """用本題的位元 + 對稱剪枝，在一般電腦上：

    n = 15   約 0.1 秒（2,279,184 組）
    n = 18   約 10 秒（666,090,624 組）
    n = 20   約 10 分鐘

再往上就需要更強的技巧：
    - 完整的 8 重對稱（要用 Burnside 引理處理自對稱的解）
    - 位元平行（一次算多個分支）
    - GPU / 分散式運算

目前的世界紀錄是 n = 27（2016 年），
用了 FPGA 叢集算了好幾個月。

n = 27 的答案：234,907,967,154,122,528

沒有已知的公式，也沒有多項式演算法 ——
這是一個「看起來簡單，但計數極難」的問題。""",),
   ("h", "追問二：這個問題的計數難度屬於哪一類？"),
   "N 皇后的計數問題被認為是 <strong>#P-hard</strong>（讀作 sharp-P hard）。"
   "<strong>#P 是「計數版的 NP」</strong> —— "
   "NP 問「有沒有解」，#P 問「有幾組解」。"
   "有些問題「找一組解」很容易但「數出所有解」極難 —— "
   "N 皇后正是這樣（有 O(n) 的構造法，但計數沒有多項式演算法）。",
   ("h", "追問三：為什麼這題只到 n = 9？"),
   "因為 LeetCode 的時間限制。n = 9 只有 352 組解，毫秒級完成。"
   "如果放到 n = 15，樸素的集合版可能會 TLE，而位元版還能過。"
   "<strong>題目的上限往往反映了「出題者預期的解法」</strong> —— "
   "n ≤ 9 表示「寫得出正確的回溯就好」。",
 ],
 "related": [
   "<strong>第 51 題 N-Queens</strong> —— 列出所有解",
   "<strong>第 37 題 Sudoku Solver</strong> —— 同樣的 CSP + 位元遮罩",
   "<strong>第 1349 題 Maximum Students Taking Exam</strong> —— 位元遮罩 DP 的棋盤題",
 ],
 "check": [
   "為什麼終止條件可以用 <code>cols == FULL</code> 而不需要記「現在第幾列」？",
   "<code>(d1 | bit) &lt;&lt; 1 &amp; FULL</code> 裡的 <code>&amp; FULL</code> 在做什麼？拿掉會怎樣？",
   "鏡射對稱為什麼安全，旋轉對稱為什麼不能簡單地乘 4？",
   "n = 5 用鏡射版時，如果忘記處理「中間那一行」，會算出多少？",
 ],
})
print("P52 written")
