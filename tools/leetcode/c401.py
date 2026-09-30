# -*- coding: utf-8 -*-
"""第 401–406 題。"""
import random
import itertools
import functools
from authoring import emit, ap
from runner import Src
from lchelp import lv, rand_tree

S = Src()
random.seed(401)


# ==================== 401. Binary Watch ====================
S["p401"] = '''class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for h in range(12):                     # ★ 反過來列舉所有時間，數亮了幾顆燈
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    res.append(f"{h}:{m:02d}")
        return res'''

S["p401_bits"] = '''class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for mask in range(1 << 10):              # 10 顆燈的所有亮滅組合
            if bin(mask).count("1") != turnedOn:
                continue
            h, m = mask >> 6, mask & 0b111111    # 高 4 位是小時，低 6 位是分鐘
            if h < 12 and m < 60:
                res.append(f"{h}:{m:02d}")
        return res'''

_p401 = [S.load(x) for x in ("p401", "p401_bits")]
for k in range(0, 11):
    a, b = (sorted(sol.readBinaryWatch(k)) for sol in _p401)
    assert a == b, k
assert sorted(_p401[0].readBinaryWatch(1)) == sorted(["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"])
assert _p401[0].readBinaryWatch(9) == []
print("P401 OK")

emit({
 "num": 401, "slug": "binary-watch",
 "en": [
   "A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.",
   "Given an integer <code>turnedOn</code> which represents the number of LEDs that are currently on (ignoring the PM), return <em>all possible times the watch could represent</em>. You may return the answer in <strong>any order</strong>.",
   "The hour must not contain a leading zero (e.g. <code>\"01:00\"</code> is not valid, it should be <code>\"1:00\"</code>). "
   "The minute must consist of two digits and may contain a leading zero (e.g. <code>\"10:2\"</code> is not valid, it should be <code>\"10:02\"</code>).",
 ],
 "zh": [
   "二進位手錶上排有 4 顆燈表示小時（0–11），下排 6 顆燈表示分鐘（0–59），每顆燈代表一個位元（最右邊是最低位）。",
   "給你目前亮著的燈數 <code>turnedOn</code>，回傳手錶可能顯示的所有時間，順序不限。",
   "小時不能有前導零（寫 <code>\"1:00\"</code> 不寫 <code>\"01:00\"</code>）；分鐘必須兩位數（寫 <code>\"10:02\"</code>）。",
 ],
 "examples": """範例 1
  輸入：turnedOn = 1
  輸出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

範例 2
  輸入：turnedOn = 9
  輸出：[]""",
 "constraints": [
   "0 ≤ <code>turnedOn</code> ≤ 10",
 ],
 "idea": [
   ("c", """【正著想：從 10 顆燈裡選 turnedOn 顆】
    要處理「小時 > 11、分鐘 > 59」的不合法組合。

【反著想：列舉所有合法時間】
    只有 12 × 60 = 720 種時間，
    對每一種數它亮了幾顆燈（小時和分鐘的 1 的個數相加），
    等於 turnedOn 就收下。
    720 很小，簡單又不會出錯。

【格式】
    f"{h}:{m:02d}" -> 分鐘補零成兩位。"""),
 ],
 "approaches": [
   ap("解法一", "列舉 10 位元的遮罩", [
     ("c", S["p401_bits"]),
   ], "O(2¹⁰)", "O(1)", "", "不計輸出"),

   ap("解法二", "列舉所有合法時間", [
     ("c", S["p401"]),
   ], "O(720)", "O(1)", "", "不計輸出", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、遮罩", "O(1024)", "要濾掉不合法時間"],
    ["二、列舉時間", "O(720)", "最不容易錯 ✔"]]),
 "edges": [
   "<strong>turnedOn = 0</strong> → <code>[\"0:00\"]</code>。",
   "<strong>turnedOn ≥ 9</strong> → 空陣列（最多 3 + 5 = 8 顆：11 = 1011、59 = 111011）。",
 ],
 "follow": [
   ("h", "「反向列舉」的思維"),
   ("c", "當「合法答案」的集合很小時，直接列舉所有答案再檢查，往往比從條件去構造更簡單。"),
 ],
 "related": [
   "<strong>第 17 題 電話號碼的字母組合</strong>",
   "<strong>第 191 題 位元 1 的個數</strong>",
 ],
 "check": [
   "為什麼列舉 720 種時間比從燈號組合出發簡單？",
   "turnedOn 最大合法值是多少？",
 ],
})


# ==================== 402. Remove K Digits ====================
S["p402"] = '''class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for d in num:
            # ★ 前面的數字比現在的大，而且還能刪 -> 刪掉它，讓小的往前
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
        if k:                                  # 還沒刪完：剩下的是遞增的，刪尾巴
            stack = stack[:-k]
        return "".join(stack).lstrip("0") or "0"'''

_p402 = S.load("p402")


def _rk_ref(num, k):
    best = None
    for keep in itertools.combinations(range(len(num)), len(num) - k):
        v = int("".join(num[i] for i in keep) or "0")
        best = v if best is None else min(best, v)
    return str(best)


for num, k, want in [("1432219", 3, "1219"), ("10200", 1, "200"), ("10", 2, "0"), ("9", 1, "0"), ("112", 1, "11")]:
    assert _p402.removeKdigits(num, k) == want
for _ in range(2000):
    num = str(random.randint(1, 9)) + "".join(random.choice("0123456789") for _ in range(random.randrange(0, 7)))
    k = random.randint(1, len(num))
    assert _p402.removeKdigits(num, k) == _rk_ref(num, k), (num, k)
print("P402 OK")

_P402_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">num = "1432219"，k = 3：單調遞增堆疊</text>
            <g font-size="12">
              <text x="30" y="52" fill="var(--text-muted)">讀入</text><text x="90" y="52" fill="var(--text-muted)">堆疊</text><text x="200" y="52" fill="var(--text-muted)">k</text><text x="240" y="52" fill="var(--text-muted)">說明</text>
              <text x="30" y="76" fill="var(--text)">1</text><text x="90" y="76" fill="var(--text)">1</text><text x="200" y="76" fill="var(--text)">3</text>
              <text x="30" y="98" fill="var(--text)">4</text><text x="90" y="98" fill="var(--text)">1 4</text><text x="200" y="98" fill="var(--text)">3</text>
              <text x="30" y="120" fill="var(--text)">3</text><text x="90" y="120" fill="var(--text)">1 3</text><text x="200" y="120" fill="var(--accent)">2</text><text x="240" y="120" fill="var(--accent)">4 &gt; 3 → 刪 4</text>
              <text x="30" y="142" fill="var(--text)">2</text><text x="90" y="142" fill="var(--text)">1 2</text><text x="200" y="142" fill="var(--accent)">1</text><text x="240" y="142" fill="var(--accent)">3 &gt; 2 → 刪 3</text>
              <text x="30" y="164" fill="var(--text)">2</text><text x="90" y="164" fill="var(--text)">1 2 2</text><text x="200" y="164" fill="var(--text)">1</text>
              <text x="30" y="186" fill="var(--text)">1</text><text x="90" y="186" fill="var(--text)">1 2 1</text><text x="200" y="186" fill="var(--accent)">0</text><text x="240" y="186" fill="var(--accent)">2 &gt; 1 → 刪 2（只刪一個，k 用完）</text>
              <text x="30" y="208" fill="var(--text)">9</text><text x="90" y="208" fill="var(--gold)">1 2 1 9</text><text x="200" y="208" fill="var(--text)">0</text><text x="240" y="208" fill="var(--gold)">答案 "1219"</text>
            </g>'''

emit({
 "num": 402, "slug": "remove-k-digits",
 "en": [
   "Given string num representing a non-negative integer <code>num</code>, and an integer <code>k</code>, return <em>the smallest possible integer after removing</em> <code>k</code> <em>digits from</em> <code>num</code>.",
 ],
 "zh": [
   "給你一個代表非負整數的字串 <code>num</code> 和整數 <code>k</code>，從中刪掉 <code>k</code> 位數字，使剩下的數字最小，回傳結果（不能有前導零；全刪光回傳 <code>\"0\"</code>）。",
 ],
 "examples": """範例 1
  輸入：num = "1432219", k = 3
  輸出："1219"

範例 2
  輸入：num = "10200", k = 1
  輸出："200"
  說明：刪掉 1，剩下 "0200"，去掉前導零。

範例 3
  輸入：num = "10", k = 2
  輸出："0\"""",
 "constraints": [
   "1 ≤ <code>k</code> ≤ <code>num.length</code> ≤ 10⁵",
   "<code>num</code> 只包含數字，沒有前導零（除非本身就是 0）",
 ],
 "idea": [
   ("fig", _P402_FIG, "0 0 640 222"),
   ("c", """【數字越高位越重要】
    兩個等長的數，第一個不同的位置決定大小。
    所以要讓前面的位盡量小。

【貪心：遇到「下降」就刪前面那個】
    如果 num[i] > num[i+1]，刪掉 num[i] 會讓這一位變小 ——
    這是當下最划算的一刀。

【單調遞增堆疊】
    由左到右讀，堆疊保持遞增：
        新數字比堆疊頂端小，而且還有刪除額度 -> 彈出頂端
    讀完後如果 k 還沒用完，
    剩下的已經是遞增的 -> 刪最後 k 位。

【收尾】
    去掉前導零；全部刪光要回傳 "0"。"""),
 ],
 "approaches": [
   ap("解法", "單調遞增堆疊", [
     ("c", S["p402"]),
   ], "O(n)", "O(n)", "每個數字最多進出堆疊一次", "", optimal=True),
 ],
 "edges": [
   "<strong>刪完剩前導零</strong>（<code>\"10200\"</code>）→ 去掉。",
   "<strong>k = 長度</strong> → <code>\"0\"</code>。",
   "<strong>整個字串遞增</strong>（<code>\"12345\"</code>）→ 迴圈中不刪，最後刪尾巴。",
   "<strong>重複數字</strong> → 相等時不刪（用 <code>&gt;</code> 不用 <code>&gt;=</code>）。",
 ],
 "follow": [
   ("h", "同一個單調堆疊"),
   ("c", "第 316 題（去除重複字母）、第 321 題（拼接最大數，方向相反）、第 1673 題（找出最具競爭力的子序列）都是這個模板。"),
 ],
 "related": [
   "<strong>第 316 題 去除重複字母</strong>",
   "<strong>第 321 題 拼接最大數</strong>",
   "<strong>第 1673 題 找出最具競爭力的子序列</strong>",
 ],
 "check": [
   "為什麼遇到「前面比後面大」就刪前面那個？",
   "迴圈結束後 k 還有剩，要刪哪些？為什麼？",
   "結果為什麼要處理前導零？",
 ],
})


# ==================== 403. Frog Jump ====================
S["p403"] = '''class Solution:
    def canCross(self, stones: List[int]) -> bool:
        # reach[s]：能以哪些「最後一跳的距離」到達石頭 s
        reach = {s: set() for s in stones}
        reach[0].add(0)
        for s in stones:
            for k in reach[s]:
                for step in (k - 1, k, k + 1):     # ★ 下一跳可以是 k-1、k、k+1
                    if step > 0 and s + step in reach:
                        reach[s + step].add(step)
        return bool(reach[stones[-1]])'''

S["p403_memo"] = '''class Solution:
    def canCross(self, stones: List[int]) -> bool:
        pos = set(stones)
        last = stones[-1]

        @functools.lru_cache(None)
        def dfs(s: int, k: int) -> bool:           # 在石頭 s、上一跳是 k
            if s == last:
                return True
            return any(step > 0 and s + step in pos and dfs(s + step, step)
                       for step in (k + 1, k, k - 1))   # 先試大步，通常更快到終點
        return dfs(0, 0)'''

_p403 = [S.load(x) for x in ("p403", "p403_memo")]
for st, want in [([0, 1, 3, 5, 6, 8, 12, 17], True), ([0, 1, 2, 3, 4, 8, 9, 11], False), ([0, 2], False), ([0, 1], True)]:
    for sol in _p403:
        assert sol.canCross(st) == want
for _ in range(1500):
    st = [0, 1] + sorted(random.sample(range(2, 25), random.randrange(0, 10)))
    a, b = (sol.canCross(st) for sol in _p403)
    assert a == b, st
print("P403 OK")

emit({
 "num": 403, "slug": "frog-jump",
 "en": [
   "A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.",
   "Given a list of <code>stones</code> positions (in units) in sorted <strong>ascending order</strong>, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be <code>1</code> unit.",
   "If the frog's last jump was <code>k</code> units, its next jump must be either <code>k - 1</code>, <code>k</code>, or <code>k + 1</code> units. The frog can only jump in the forward direction.",
 ],
 "zh": [
   "一隻青蛙要過河。河被分成許多格，有些格子上有石頭。青蛙只能跳到石頭上，不能掉進水裡。",
   "給你遞增排序的石頭位置 <code>stones</code>，判斷青蛙能不能跳到最後一顆石頭。青蛙一開始在第一顆石頭（位置 0），<strong>第一跳必須是 1 格</strong>。",
   "如果上一跳是 <code>k</code> 格，下一跳只能是 <code>k − 1</code>、<code>k</code> 或 <code>k + 1</code> 格，而且只能往前跳。",
 ],
 "examples": """範例 1
  輸入：stones = [0,1,3,5,6,8,12,17]
  輸出：true
  說明：0 →1→ 1 →2→ 3 →2→ 5 →3→ 8 →4→ 12 →5→ 17

範例 2
  輸入：stones = [0,1,2,3,4,8,9,11]
  輸出：false
  說明：4 和 8 之間的空隙太大。""",
 "constraints": [
   "2 ≤ <code>stones.length</code> ≤ 2000",
   "0 ≤ <code>stones[i]</code> ≤ 2³¹ − 1",
   "<code>stones[0] == 0</code>，而且嚴格遞增",
 ],
 "idea": [
   ("c", """【狀態 = (在哪顆石頭, 上一跳多遠)】
    只知道位置不夠：同一顆石頭，上一跳 2 和上一跳 5 能到的地方不同。

【方法一：由前往後推（DP）】
    reach[s] = 能到達石頭 s 時，「最後一跳」可能的距離集合
    從第一顆石頭（上一跳視為 0）開始，
    對每個 (s, k)，嘗試跳 k-1、k、k+1，落在石頭上就記錄。
    最後看最後一顆石頭的集合是否非空。

【方法二：記憶化 DFS】
    dfs(s, k) = 從石頭 s、上一跳 k 出發能不能到終點。

【狀態數】
    第 i 顆石頭的跳躍距離最多 i（每跳最多比上一跳多 1）
    -> 狀態數 O(n²)，n = 2000 可以接受。

【第一跳必須是 1】
    從 (0, 0) 出發：k-1 = -1、k = 0 都不合法，只剩 1 ✔"""),
 ],
 "approaches": [
   ap("解法一", "記憶化 DFS", [
     ("c", S["p403_memo"]),
   ], "O(n²)", "O(n²)", "", ""),

   ap("解法二", "雜湊表 DP（由前往後推）", [
     ("c", S["p403"]),
   ], "O(n²)", "O(n²)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、記憶化 DFS", "O(n²)", "O(n²)"],
    ["二、DP", "O(n²)", "O(n²) ✔"]]),
 "edges": [
   "<strong>第二顆石頭不在位置 1</strong> → false。",
   "<strong>石頭間距很大</strong> → 第 i 跳最多 i 格，可以提早判斷。",
   "<strong>位置很大</strong>（2³¹）→ 用集合/字典存，不能開陣列。",
 ],
 "follow": [
   ("h", "剪枝"),
   ("c", "若 stones[i] − stones[i−1] &gt; i，第 i 顆石頭一定到不了（到第 i−1 顆最多跳了 i−1 格）→ 直接 false。"),
 ],
 "related": [
   "<strong>第 55 題 跳躍遊戲</strong>",
   "<strong>第 1340 題 跳躍遊戲 V</strong>",
 ],
 "check": [
   "為什麼狀態必須包含「上一跳的距離」？",
   "狀態總數大約是多少？",
   "第一跳必須是 1 格的限制怎麼自然地被處理？",
 ],
})


# ==================== 404. Sum of Left Leaves ====================
S["p404"] = '''class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, is_left: bool) -> int:
            if node is None:
                return 0
            if not node.left and not node.right:
                return node.val if is_left else 0     # ★ 只有「左邊的葉子」算
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)                        # 根本身不算左葉'''

_p404 = S.load("p404")


def _ll_ref(nd, left=False):
    if nd is None:
        return 0
    if not nd.left and not nd.right:
        return nd.val if left else 0
    return _ll_ref(nd.left, True) + _ll_ref(nd.right, False)


for vals, want in [([3, 9, 20, None, None, 15, 7], 24), ([1], 0), ([1, 2], 2)]:
    assert _p404.sumOfLeftLeaves(lv(vals)) == want
for _ in range(1000):
    t = rand_tree(random.randrange(1, 20), -9, 9)
    assert _p404.sumOfLeftLeaves(t) == _ll_ref(t)
print("P404 OK")

emit({
 "num": 404, "slug": "sum-of-left-leaves",
 "en": [
   "Given the <code>root</code> of a binary tree, return <em>the sum of all left leaves.</em>",
   "A <strong>leaf</strong> is a node with no children. A <strong>left leaf</strong> is a leaf that is the left child of another node.",
 ],
 "zh": [
   "給你二元樹的根節點 <code>root</code>，回傳所有<strong>左葉子</strong>的值的總和。",
   "<strong>葉子</strong>是沒有孩子的節點；<strong>左葉子</strong>是某個節點的<strong>左孩子</strong>，而且是葉子。",
 ],
 "examples": """範例 1
  輸入：root = [3,9,20,null,null,15,7]
  輸出：24
  說明：左葉子是 9 和 15。

範例 2
  輸入：root = [1]
  輸出：0
  說明：根不是任何節點的左孩子。""",
 "constraints": [
   "節點數在 <code>[1, 1000]</code> 之間",
   "−1000 ≤ <code>Node.val</code> ≤ 1000",
 ],
 "idea": [
   ("c", """【判斷「左葉子」需要兩個資訊】
    1. 它是葉子（自己看得出來）
    2. 它是左孩子（自己看不出來，要父節點告訴它）

【遞迴時多傳一個參數 is_left】
    往左走傳 True，往右走傳 False。
    走到葉子時，is_left 為 True 才算。

【根不算】
    只有一個節點的樹，根雖然是葉子，但不是任何人的左孩子 -> 0。"""),
 ],
 "approaches": [
   ap("解法", "DFS 帶著「是否為左孩子」", [
     ("c", S["p404"]),
   ], "O(n)", "O(h)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>只有根</strong> → 0。",
   "<strong>左孩子不是葉子</strong> → 繼續往下找。",
   "<strong>右邊的葉子</strong> → 不算。",
 ],
 "follow": [
   ("h", "資訊從上往下傳"),
   ("c", "「父節點知道、子節點不知道」的資訊（深度、方向、路徑和）就當參數往下傳——第 112、129、988 題都是這樣。"),
 ],
 "related": [
   "<strong>第 112 題 路徑總和</strong>",
   "<strong>第 513 題 找樹左下角的值</strong>",
 ],
 "check": [
   "為什麼需要額外的參數？",
   "只有一個節點時答案是什麼？",
 ],
})


# ==================== 405. Convert a Number to Hexadecimal ====================
S["p405"] = '''class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        num &= 0xFFFFFFFF                     # ★ 負數：轉成 32 位元的二補數
        digits = "0123456789abcdef"
        out = []
        while num:
            out.append(digits[num & 15])      # 每次取最低 4 位
            num >>= 4
        return "".join(reversed(out))'''

_p405 = S.load("p405")
for n in list(range(-3000, 3000)) + [2 ** 31 - 1, -2 ** 31, 26, -1]:
    assert _p405.toHex(n) == format(n & 0xFFFFFFFF, "x"), n
print("P405 OK")

emit({
 "num": 405, "slug": "convert-a-number-to-hexadecimal",
 "en": [
   "Given a 32-bit integer <code>num</code>, return <em>a string representing its hexadecimal representation</em>. For negative integers, two's complement method is used.",
   "All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.",
   "<strong>Note:</strong> You are not allowed to use any built-in library method to directly solve this problem.",
 ],
 "zh": [
   "給你一個 32 位元整數 <code>num</code>，回傳它的<strong>十六進位</strong>字串。負數用<strong>二補數</strong>表示。",
   "字母用小寫，不能有前導零（0 本身除外）。不能用內建函式直接轉換。",
 ],
 "examples": """範例 1
  輸入：num = 26
  輸出："1a"

範例 2
  輸入：num = -1
  輸出："ffffffff\"""",
 "constraints": [
   "−2³¹ ≤ <code>num</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【一個十六進位位數 = 4 個位元】
    反覆取最低 4 位（num & 15）對應到 0-9a-f，
    然後右移 4 位，直到 num 變 0。

【負數：二補數】
    32 位元的 -1 = 0xFFFFFFFF。
    Python 的整數沒有位數限制，-1 右移永遠是 -1 ->
    先 num &= 0xFFFFFFFF 轉成對應的非負數（二補數的位元樣式）。

【0 要特判】
    迴圈一次都不跑，會得到空字串。"""),
   ("t", ["num", "二進位（32 位）", "十六進位"],
    [["26", "…0001 1010", "1a"],
     ["−1", "1111 … 1111", "ffffffff"],
     ["−2³¹", "1000 … 0000", "80000000"]]),
 ],
 "approaches": [
   ap("解法", "每次取 4 位元", [
     ("c", S["p405"]),
   ], "O(1)", "O(1)", "最多 8 位", "", optimal=True),
 ],
 "edges": [
   "<strong>0</strong> → \"0\"。",
   "<strong>−1</strong> → \"ffffffff\"。",
   "<strong>Python 負數</strong> → 一定要先遮罩成 32 位元，否則右移會無窮迴圈。",
 ],
 "follow": [
   ("h", "進位轉換"),
   ("c", "第 504 題（七進位）、第 168 題（Excel 欄位名稱，沒有 0 的 26 進位）、第 1017 題（負二進位）。"),
 ],
 "related": [
   "<strong>第 504 題 七進位數</strong>",
   "<strong>第 168 題 Excel 表列名稱</strong>",
   "<strong>第 1017 題 負二進位轉換</strong>",
 ],
 "check": [
   "一個十六進位位數對應幾個位元？",
   "Python 中負數為什麼要先和 0xFFFFFFFF 做 AND？",
 ],
})


# ==================== 406. Queue Reconstruction by Height ====================
S["p406"] = '''class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # ★ 高的先排；同樣高度時 k 小的先排
        people.sort(key=lambda p: (-p[0], p[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)          # 前面剛好有 k 個不比他矮的人 -> 插在位置 k
        return queue'''

_p406 = S.load("p406")


def _valid_q(q):
    return all(sum(1 for j in range(i) if q[j][0] >= q[i][0]) == q[i][1] for i in range(len(q)))


for people, want in [([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]], [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])]:
    assert _p406.reconstructQueue([p[:] for p in people]) == want
for _ in range(2000):
    q = [[random.randint(1, 6), 0] for _ in range(random.randrange(1, 9))]
    for i in range(len(q)):
        q[i][1] = sum(1 for j in range(i) if q[j][0] >= q[i][0])
    shuffled = [p[:] for p in q]
    random.shuffle(shuffled)
    got = _p406.reconstructQueue(shuffled)
    assert _valid_q(got) and sorted(got) == sorted(q)
print("P406 OK")

_P406_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">由高到矮依序插入：矮的人插進去，不會影響高的人的 k</text>
            <g font-size="12">
              <text x="30" y="52" fill="var(--text-muted)">處理</text><text x="110" y="52" fill="var(--text-muted)">插到位置</text><text x="200" y="52" fill="var(--text-muted)">佇列</text>
              <text x="30" y="76" fill="var(--text)">[7,0]</text><text x="110" y="76" fill="var(--text)">0</text><text x="200" y="76" fill="var(--text)">[7,0]</text>
              <text x="30" y="98" fill="var(--text)">[7,1]</text><text x="110" y="98" fill="var(--text)">1</text><text x="200" y="98" fill="var(--text)">[7,0] [7,1]</text>
              <text x="30" y="120" fill="var(--text)">[6,1]</text><text x="110" y="120" fill="var(--text)">1</text><text x="200" y="120" fill="var(--text)">[7,0] [6,1] [7,1]</text>
              <text x="30" y="142" fill="var(--text)">[5,0]</text><text x="110" y="142" fill="var(--text)">0</text><text x="200" y="142" fill="var(--text)">[5,0] [7,0] [6,1] [7,1]</text>
              <text x="30" y="164" fill="var(--text)">[5,2]</text><text x="110" y="164" fill="var(--text)">2</text><text x="200" y="164" fill="var(--text)">[5,0] [7,0] [5,2] [6,1] [7,1]</text>
              <text x="30" y="186" fill="var(--text)">[4,4]</text><text x="110" y="186" fill="var(--text)">4</text><text x="200" y="186" fill="var(--gold)">[5,0] [7,0] [5,2] [6,1] [4,4] [7,1]</text>
            </g>
            <text x="20" y="218" fill="var(--text)" font-size="12">插入 [h, k] 時，佇列裡所有人都 ≥ h → 插在位置 k，前面剛好 k 個人 ≥ h ✔</text>
            <text x="20" y="240" fill="var(--gold)" font-size="12">★ 之後插入的人都比較矮，看不見（不算進任何高個子的 k），所以已經排好的人不受影響。</text>'''

emit({
 "num": 406, "slug": "queue-reconstruction-by-height",
 "en": [
   "You are given an array of people, <code>people</code>, which are the attributes of some people in a queue (not necessarily in order). Each <code>people[i] = [h<sub>i</sub>, k<sub>i</sub>]</code> represents the <code>i<sup>th</sup></code> person of height <code>h<sub>i</sub></code> with <strong>exactly</strong> <code>k<sub>i</sub></code> other people in front who have a height greater than or equal to <code>h<sub>i</sub></code>.",
   "Reconstruct and return <em>the queue that is represented by the input array</em> <code>people</code>. The returned queue should be formatted as an array <code>queue</code>, where <code>queue[j] = [h<sub>j</sub>, k<sub>j</sub>]</code> is the attributes of the <code>j<sup>th</sup></code> person in the queue (<code>queue[0]</code> is the person at the front of the queue).",
 ],
 "zh": [
   "給你一群人的資訊 <code>people</code>（順序被打亂），<code>people[i] = [h, k]</code> 代表這個人身高 <code>h</code>，而且在佇列中他<strong>前面恰好有 <code>k</code> 個人</strong>身高 <strong>≥ h</strong>。",
   "請重建並回傳這個佇列（<code>queue[0]</code> 是最前面的人）。",
 ],
 "examples": """範例 1
  輸入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
  輸出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

範例 2
  輸入：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
  輸出：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]""",
 "constraints": [
   "1 ≤ <code>people.length</code> ≤ 2000",
   "0 ≤ <code>h<sub>i</sub></code> ≤ 10⁶",
   "0 ≤ <code>k<sub>i</sub></code> &lt; <code>people.length</code>",
   "保證可以重建出佇列",
 ],
 "idea": [
   ("fig", _P406_FIG, "0 0 640 254"),
   ("c", """【關鍵：矮的人對高的人「隱形」】
    k 只數身高 >= 自己的人，
    所以矮的人站在哪裡，都不影響高的人的 k。

【貪心：從高到矮依序插入】
    處理 [h, k] 時，佇列裡的人都 >= h（先處理的都比較高或一樣高），
    把他插在位置 k -> 前面剛好 k 個人 >= h ✔
    之後插入的人都比他矮，不會改變他的 k ✔

【同樣身高時 k 小的先處理】
    [5,0] 和 [5,2]：
    先插 [5,0]，再插 [5,2] 時，[5,0] 也算在「>= 5」裡面，位置正確。
    如果順序反過來，[5,2] 插完後 [5,0] 插到它前面，
    [5,2] 前面的 >= 5 就變成 3 個 ✘"""),
 ],
 "approaches": [
   ap("解法", "排序 + 依 k 插入", [
     ("c", S["p406"]),
   ], "O(n²)", "O(n)", "list.insert 是 O(n)", "", optimal=True),
 ],
 "edges": [
   "<strong>所有人一樣高</strong> → 依 k 排序。",
   "<strong>k = 0 的最矮的人</strong> → 最後被插到最前面。",
 ],
 "follow": [
   ("h", "更快的做法"),
   ("c", "從矮到高處理，每個人放在「第 k+1 個空位」；用樹狀陣列或線段樹找第 k 個空位，O(n log n)（同樣身高要 k 大的先處理）。"),
 ],
 "related": [
   "<strong>第 315 題 計算右側小於當前元素的個數</strong>",
   "<strong>第 1996 題 遊戲中弱角色的數量</strong> —— 同樣的「一維遞減、一維遞增」排序技巧",
 ],
 "check": [
   "為什麼要從高到矮處理？",
   "同樣高度時為什麼 k 小的先處理？",
   "插入 [h, k] 時為什麼插在位置 k 就對了？",
 ],
})
