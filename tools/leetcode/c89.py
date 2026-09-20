# -*- coding: utf-8 -*-
"""第 89–92 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(89)

# ==================== 89. Gray Code ====================
S["p89_formula"] = '''class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 第 i 個格雷碼 = i XOR (i >> 1)
        return [i ^ (i >> 1) for i in range(1 << n)]'''

S["p89_mirror"] = '''class Solution:
    def grayCode(self, n: int) -> List[int]:
        # 鏡射法（reflect-and-prefix）：
        # G(k+1) = G(k) 原序 ++ G(k) 反序且每個前面加上 1<<k
        res = [0]
        for k in range(n):
            high = 1 << k
            res += [high | v for v in reversed(res)]
        return res'''

_p89 = [S.load(k) for k in ("p89_formula", "p89_mirror")]


def _check_gray(seq, n):
    assert len(seq) == 1 << n, ("長度不對", n, len(seq))
    assert sorted(seq) == list(range(1 << n)), ("不是 0..2^n-1 的排列", n)
    assert seq[0] == 0, ("第一個不是 0", seq[:3])
    for a, b in zip(seq, seq[1:]):
        assert bin(a ^ b).count("1") == 1, ("相鄰不只差一位", a, b)
    # 首尾也必須只差一位（循環格雷碼）
    assert bin(seq[0] ^ seq[-1]).count("1") == 1, ("首尾差不只一位", seq[0], seq[-1])


for n in range(1, 13):
    for sol in _p89:
        _check_gray(sol.grayCode(n), n)
assert _p89[0].grayCode(2) == [0, 1, 3, 2]
assert _p89[0].grayCode(1) == [0, 1]
assert _p89[0].grayCode(3) == [0, 1, 3, 2, 6, 7, 5, 4]
print("P89 solutions OK")

_P89_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">n = 3 的格雷碼：相鄰兩個（含首尾）只差一個位元</text>
            <g font-family="monospace" font-size="13">
              <text x="50" y="52" fill="var(--text-muted)">i</text>
              <text x="130" y="52" fill="var(--text-muted)">i 的二進位</text>
              <text x="280" y="52" fill="var(--text-muted)">i &gt;&gt; 1</text>
              <text x="410" y="52" fill="var(--text-muted)">i ^ (i&gt;&gt;1)</text>
              <text x="540" y="52" fill="var(--text-muted)">十進位</text>
            </g>
            <line x1="40" y1="62" x2="600" y2="62" stroke="var(--border)"/>
            <g font-family="monospace" font-size="13">
              <text x="50" y="86" fill="var(--accent)">0</text><text x="130" y="86" fill="var(--text-muted)">000</text>
              <text x="280" y="86" fill="var(--text-muted)">000</text><text x="410" y="86" fill="var(--gold)">000</text><text x="540" y="86" fill="#ff8a65">0</text>

              <text x="50" y="110" fill="var(--accent)">1</text><text x="130" y="110" fill="var(--text-muted)">001</text>
              <text x="280" y="110" fill="var(--text-muted)">000</text><text x="410" y="110" fill="var(--gold)">001</text><text x="540" y="110" fill="#ff8a65">1</text>

              <text x="50" y="134" fill="var(--accent)">2</text><text x="130" y="134" fill="var(--text-muted)">010</text>
              <text x="280" y="134" fill="var(--text-muted)">001</text><text x="410" y="134" fill="var(--gold)">011</text><text x="540" y="134" fill="#ff8a65">3</text>

              <text x="50" y="158" fill="var(--accent)">3</text><text x="130" y="158" fill="var(--text-muted)">011</text>
              <text x="280" y="158" fill="var(--text-muted)">001</text><text x="410" y="158" fill="var(--gold)">010</text><text x="540" y="158" fill="#ff8a65">2</text>

              <text x="50" y="182" fill="var(--accent)">4</text><text x="130" y="182" fill="var(--text-muted)">100</text>
              <text x="280" y="182" fill="var(--text-muted)">010</text><text x="410" y="182" fill="var(--gold)">110</text><text x="540" y="182" fill="#ff8a65">6</text>

              <text x="50" y="206" fill="var(--accent)">5</text><text x="130" y="206" fill="var(--text-muted)">101</text>
              <text x="280" y="206" fill="var(--text-muted)">010</text><text x="410" y="206" fill="var(--gold)">111</text><text x="540" y="206" fill="#ff8a65">7</text>

              <text x="50" y="230" fill="var(--accent)">6</text><text x="130" y="230" fill="var(--text-muted)">110</text>
              <text x="280" y="230" fill="var(--text-muted)">011</text><text x="410" y="230" fill="var(--gold)">101</text><text x="540" y="230" fill="#ff8a65">5</text>

              <text x="50" y="254" fill="var(--accent)">7</text><text x="130" y="254" fill="var(--text-muted)">111</text>
              <text x="280" y="254" fill="var(--text-muted)">011</text><text x="410" y="254" fill="var(--gold)">100</text><text x="540" y="254" fill="#ff8a65">4</text>
            </g>
            <line x1="40" y1="268" x2="600" y2="268" stroke="var(--border)"/>
            <text x="20" y="296" fill="var(--gold)" font-size="12">000 → 001 → 011 → 010 → 110 → 111 → 101 → 100 → (回到 000)</text>
            <text x="20" y="320" fill="var(--text-muted)" font-size="12">每一步都只有一個位元翻轉，而且最後一個 100 回到 000 也只差一位 ✔</text>'''

emit({
 "num": 89, "slug": "gray-code",
 "en": [
   "An <strong>n-bit gray code sequence</strong> is a sequence of <code>2ⁿ</code> integers "
   "where: every integer is in the <strong>inclusive</strong> range "
   "<code>[0, 2ⁿ - 1]</code>; the first integer is <code>0</code>; an integer appears "
   "<strong>no more than once</strong> in the sequence; the binary representation of every "
   "pair of <strong>adjacent</strong> integers differs by <strong>exactly one bit</strong>; "
   "and the binary representation of the <strong>first and last</strong> integers differs by "
   "<strong>exactly one bit</strong>.",
   "Given an integer <code>n</code>, return <em>any valid n-bit gray code sequence</em>.",
 ],
 "zh": [
   "<strong>n 位元格雷碼序列</strong>是一個由 <code>2ⁿ</code> 個整數組成的序列，滿足："
   "（1）每個整數都在 <code>[0, 2ⁿ − 1]</code> 之間；"
   "（2）第一個是 <code>0</code>；"
   "（3）每個整數<strong>最多出現一次</strong>；"
   "（4）<strong>相鄰</strong>兩個整數的二進位表示<strong>恰好差一個位元</strong>；"
   "（5）<strong>首尾</strong>兩個整數也<strong>恰好差一個位元</strong>。",
   "給你一個整數 <code>n</code>，回傳<strong>任何一個</strong>有效的格雷碼序列。",
 ],
 "pre": [
   ("note", "格雷碼是什麼，以及它為什麼重要", [
     ("c", """一般的二進位計數，相鄰兩個數可能差很多位元：

    3 = 011
    4 = 100      三個位元同時翻轉！

格雷碼重新排列這些數，讓相鄰的只差一位：

    000 -> 001 -> 011 -> 010 -> 110 -> 111 -> 101 -> 100
     0      1      3      2      6      7      5      4

    而且最後一個（100）回到第一個（000）也只差一位 ——
    所以它是一個【循環】格雷碼。

為什麼重要？（真實應用）

  1. 旋轉編碼器（rotary encoder）
     機械軸上刻著二進位編碼，用光學或磁性感測器讀取。
     如果用一般二進位，從 011 轉到 100 時，
     三個感測器不可能【完全同時】切換 ——
     中間可能讀到 111、001、101 等亂七八糟的值。

     用格雷碼的話，每次只有一個位元變 ——
     就算讀取的時機不準，最壞也只是「讀到前一個或後一個值」，
     不會讀到完全無關的數字。

  2. 卡諾圖（Karnaugh map）
     數位邏輯化簡時，行列的標籤用格雷碼排列，
     這樣「相鄰的格子」就代表「只差一個變數」，
     可以直接圈起來合併。

  3. 錯誤更正碼、遺傳演算法的編碼、
     超立方體（hypercube）網路的節點編號

格雷碼是 Frank Gray 在 1947 年為貝爾實驗室的
脈衝碼調變（PCM）系統申請的專利。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：n = 2
  輸出：[0,1,3,2]
  說明：
    00 -> 0
    01 -> 1
    11 -> 3
    10 -> 2
    相鄰都只差一位，而且 10 和 00 也只差一位。
    [0,2,3,1] 也是有效答案。

範例 2
  輸入：n = 1
  輸出：[0,1]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 16",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 16</strong>，所以最多 <code>2¹⁶ = 65536</code> 個數。"
       "<strong>輸出的大小就是 2ⁿ，所以複雜度下界是 O(2ⁿ)。</strong>",
       "<strong>「回傳任何一個有效序列」</strong> —— 答案不唯一。"
       "<code>n = 2</code> 時 <code>[0,1,3,2]</code> 和 <code>[0,2,3,1]</code> 都對。",
       "<strong>包含「首尾也要差一位」這條</strong> —— "
       "這讓它是「循環格雷碼」。標準的反射格雷碼天然滿足這一條。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P89_FIG, "0 0 640 334"),
 ],
 "approaches": [
   ap("解法一", "公式 <code>i ^ (i &gt;&gt; 1)</code>（一行）", [
     ("c", S["p89_formula"]),
     ("h", "為什麼這個公式是對的？"),
     ("c", """設 g(i) = i ^ (i >> 1)

要證明：g(i) 和 g(i+1) 恰好差一個位元。

    g(i) ^ g(i+1)
      = (i ^ (i>>1)) ^ ((i+1) ^ ((i+1)>>1))
      = (i ^ (i+1)) ^ ((i>>1) ^ ((i+1)>>1))

觀察 i ^ (i+1)：
    加一的效果是「把最低的那串 1 變成 0，然後最低的 0 變成 1」。

    i   = ...x 0 1 1 1
    i+1 = ...x 1 0 0 0
    XOR = 000 1 1 1 1     -> 是一串連續的 1（從第 0 位到第 k 位）

    設 i ^ (i+1) = 2^(k+1) - 1（k+1 個 1）

同理 (i>>1) ^ ((i+1)>>1) = (i ^ (i+1)) >> 1 = 2^k - 1（k 個 1）

    （因為右移和 XOR 可交換）

所以 g(i) ^ g(i+1) = (2^(k+1) - 1) ^ (2^k - 1)
                    = 2^k         <- 只有第 k 位是 1 ✔

恰好一個位元 ✔

而 g 是一個【雙射】（0..2ⁿ-1 -> 0..2ⁿ-1）：
    因為它有反函數（下面的追問會給），
    所以每個值恰好出現一次 ✔

首尾：
    g(0) = 0
    g(2ⁿ-1) = (2ⁿ-1) ^ (2^(n-1)-1) = 2^(n-1)
    0 ^ 2^(n-1) = 2^(n-1) -> 只有一個位元 ✔"""),
     "<strong>一行、O(2ⁿ) 時間、沒有任何遞迴或額外資料結構。</strong>"
     "<strong>但如果你不知道這個公式，是想不出來的</strong> —— "
     "所以面試時通常會先寫解法二（鏡射法），再說「其實有一個公式」。",
   ], "O(2ⁿ)", "O(1)（不算輸出）", "每個值一次位元運算",
      "只有輸出", optimal=True),

   ap("解法二", "鏡射法（reflect-and-prefix）—— 最能講清楚的構造", [
     "從 <code>n = 0</code> 的 <code>[0]</code> 開始，"
     "<strong>每一輪把現有序列「反過來抄一份」，並在抄的那份前面補上一個 1。</strong>",
     ("c", S["p89_mirror"]),
     ("c", """n = 0:  [0]

n = 1:  [0]  ++  [0] 反過來，每個加上 1<<0 = 1
        = [0]  ++  [1]
        = [0, 1]

n = 2:  [0, 1]  ++  [1, 0] 每個加上 1<<1 = 2
        = [0, 1]  ++  [3, 2]
        = [0, 1, 3, 2]

n = 3:  [0,1,3,2]  ++  [2,3,1,0] 每個加上 1<<2 = 4
        = [0,1,3,2]  ++  [6,7,5,4]
        = [0,1,3,2,6,7,5,4]  ✔

為什麼這樣構造出來的一定合法？

  1. 【前半段】內部：由歸納假設，相鄰只差一位 ✔

  2. 【後半段】內部：它是前半段的反序，每個都加了同一個 high。
     反序不改變「相鄰關係」，加同一個數也不改變 XOR ——
     所以相鄰仍然只差一位 ✔

  3. 【接縫處】：前半段的最後一個是 res[-1]（設為 x），
     後半段的第一個是 high | x（因為反序的第一個就是原本的最後一個）。
     兩者的差別只有 high 這一位 ✔

  4. 【首尾】：第一個是 0，最後一個是 high | 0 = high。
     0 ^ high = high -> 只有一位 ✔

四個條件都成立 -> 歸納完成 ✔

這個構造法叫做【反射二進位碼（reflected binary code）】，
也就是格雷碼的正式名稱。"""),
     "<strong>這個解法的價值在於它是「可以推導出來的」</strong> —— "
     "面試時你可以從 <code>n = 1, 2, 3</code> 觀察出規律，"
     "然後說明為什麼歸納成立。"
     "<strong>而公式法只能「知道或不知道」。</strong>",
     "<strong>複雜度</strong>：每一輪把長度加倍，總共 "
     "<code>1 + 2 + 4 + ... + 2ⁿ⁻¹ = 2ⁿ - 1</code> 次操作 —— O(2ⁿ) ✔",
   ], "O(2ⁿ)", "O(2ⁿ)", "總操作數 = 2ⁿ − 1", "結果陣列"),
 ],
 "compare": (["解法", "時間", "行數", "能推導出來？", "備註"],
   [["一、公式 <code>i ^ (i&gt;&gt;1)</code>", "O(2ⁿ)", "1", "✘ 要知道", "最短，也最快"],
    ["二、鏡射構造", "O(2ⁿ)", "6", "✔ 可觀察歸納", "面試建議先講這個"]]),
 "edges": [
   "<strong>n = 1</strong> → <code>[0, 1]</code>。",
   "<strong>n = 2</strong> → <code>[0, 1, 3, 2]</code>（或其他合法答案）。",
   "<strong>n = 16</strong> → 65536 個數。確認不會 TLE 或 MLE。",
   "<strong>驗證條件（五條都要檢查）</strong>：長度是 2ⁿ、是 0..2ⁿ−1 的排列、"
   "第一個是 0、相鄰差一位、<strong>首尾也差一位</strong>。"
   "<strong>最後一條最常被漏掉。</strong>",
   "<strong>相鄰差一位的檢查</strong>：<code>bin(a ^ b).count(\"1\") == 1</code>。",
   "<strong>n = 0</strong>（題目不會給）：應該是 <code>[0]</code>。兩種解法都自然正確。",
 ],
 "follow": [
   ("h", "追問一：怎麼從格雷碼還原成原本的數字？"),
   ("c", """正向： g = i ^ (i >> 1)

反向： i = g ^ (g>>1) ^ (g>>2) ^ (g>>4) ^ (g>>8) ^ ...

    或者用迴圈：
        i = g
        shift = 1
        while shift < bits:
            i ^= i >> shift
            shift <<= 1

    更直觀的逐位版本：
        原數的最高位 = 格雷碼的最高位
        原數的第 k 位 = 原數的第 k+1 位 XOR 格雷碼的第 k 位

    （因為 g_k = i_k ^ i_{k+1}，移項得 i_k = g_k ^ i_{k+1}）

驗算：g = 0b110 = 6
    i_2 = g_2 = 1
    i_1 = i_2 ^ g_1 = 1 ^ 1 = 0
    i_0 = i_1 ^ g_0 = 0 ^ 0 = 0
    i = 0b100 = 4 ✔（對照上面的表：i=4 -> g=6）""",),
   ("h", "追問二：格雷碼和「漢彌爾頓迴圈」有什麼關係？"),
   ("c", """把 n 位元的每個數當成一個節點，
「只差一個位元」的兩個數之間連一條邊 ——
得到的圖就是 n 維【超立方體（hypercube）】Qₙ。

    n=1: 一條線段（2 個節點）
    n=2: 一個正方形（4 個節點）
    n=3: 一個立方體（8 個節點）

「格雷碼序列」= 在這個超立方體上的一條【漢彌爾頓迴圈】
（走遍每個節點恰好一次，最後回到起點）。

所以「n 位元循環格雷碼存在」等價於
「n 維超立方體有漢彌爾頓迴圈」——
而鏡射構造法正是這個定理的建構式證明。

一般圖的漢彌爾頓迴圈問題是 NP-complete 的，
但超立方體有這麼漂亮的構造 —— 這是一個很好的對照。""",),
   ("h", "追問三：如果要第 k 個格雷碼，不想生成整個序列呢？"),
   "<strong>公式法本來就是 O(1)</strong>：<code>k ^ (k &gt;&gt; 1)</code>。"
   "這正是公式法勝過鏡射法的地方 —— "
   "它給出的是「第 i 個是什麼」的<strong>直接對應</strong>，"
   "而鏡射法只能一個一個生成。",
   "<strong>「有封閉形式的 unranking 函式」是很有價值的性質</strong> —— "
   "和第 60 題（第 k 個排列）、第 22 題（第 k 個括號序列）是同一類問題。",
   ("h", "追問四：格雷碼和「河內塔」有關係嗎？"),
   "<strong>有，而且很漂亮。</strong>"
   "n 層河內塔的最短解法中，<strong>第 i 步要移動的圓盤編號</strong>，"
   "等於「<code>i</code> 的二進位表示裡最低位的 1 在第幾位」—— "
   "而這正好也是「格雷碼序列中，第 i 步翻轉的是第幾個位元」。",
   "<strong>兩個看起來毫無關係的問題，共用同一個底層結構。</strong>"
   "（數學上說：兩者都對應到同一個「位元翻轉序列」。）",
 ],
 "related": [
   "<strong>第 1238 題 Circular Permutation in Binary Representation</strong> —— 指定起點的格雷碼",
   "<strong>第 78 題 Subsets</strong> —— 同樣是「枚舉 2ⁿ 個位元遮罩」",
   "<strong>第 191／338 題</strong> —— 位元運算的基本功",
   "<strong>第 60 題 Permutation Sequence</strong> —— 另一個有 unranking 公式的枚舉",
 ],
 "check": [
   "請驗證 <code>i ^ (i &gt;&gt; 1)</code> 對 <code>i = 3</code> 和 <code>i = 4</code> "
   "算出來的兩個值確實只差一位。",
   "鏡射法的四個歸納條件（前半、後半、接縫、首尾）各是怎麼成立的？",
   "「首尾也要差一位」這條容易被漏掉 —— 你的驗證程式有檢查它嗎？",
   "格雷碼和 n 維超立方體的漢彌爾頓迴圈是什麼關係？",
 ],
})
print("P89 written")

# ==================== 90. Subsets II ====================
S["p90"] = '''class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()              # 讓相同的值相鄰，去重才做得到
        out = []
        path = []

        def backtrack(start: int) -> None:
            out.append(path[:])
            for i in range(start, len(nums)):
                # 同一層裡，相同的值只取第一個
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return out'''

S["p90_counter"] = '''from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 另一個角度：對每個「不同的值」決定「要取幾個」
        items = sorted(Counter(nums).items())
        out = []

        def backtrack(idx: int, path: List[int]) -> None:
            if idx == len(items):
                out.append(path)
                return
            value, cnt = items[idx]
            for take in range(cnt + 1):          # 取 0 個、1 個、…、cnt 個
                backtrack(idx + 1, path + [value] * take)

        backtrack(0, [])
        return out'''

S["p90_iter"] = '''class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = [[]]
        start = 0                # 上一輪「新增的那些子集」的起點

        for i, x in enumerate(nums):
            # 如果 x 和前一個相同，只能接在「上一輪新增的」後面
            # 否則會產生重複
            begin = start if i > 0 and nums[i] == nums[i - 1] else 0
            start = len(out)
            out += [out[j] + [x] for j in range(begin, start)]

        return out'''

_p90 = [S.load(k) for k in ("p90", "p90_counter", "p90_iter")]


def _p90_ref(nums):
    found = set()
    for r in range(len(nums) + 1):
        for c in itertools.combinations(sorted(nums), r):
            found.add(c)
    return sorted(found)


for c in [[1, 2, 2], [0], [1, 1], [1, 1, 1], [4, 4, 4, 1, 4], [], [1, 2, 3]]:
    e = _p90_ref(c)
    for sol in _p90:
        g = sorted(tuple(sorted(x)) for x in sol.subsetsWithDup(list(c)))
        assert g == e, ("P90", c, sol, g, e)
        assert len(g) == len(set(g)), ("P90 dup", c, sol)
for _ in range(2000):
    c = [random.randint(1, 3) for _ in range(random.randint(0, 7))]
    e = _p90_ref(c)
    for sol in _p90:
        g = sorted(tuple(sorted(x)) for x in sol.subsetsWithDup(list(c)))
        assert g == e, ("P90", c, sol, g, e)
print("P90 solutions OK")

emit({
 "num": 90, "slug": "subsets-ii",
 "en": [
   "Given an integer array <code>nums</code> that may contain duplicates, return "
   "<em>all possible subsets (the power set)</em>.",
   "The solution set <strong>must not</strong> contain duplicate subsets. Return the solution "
   "in <strong>any order</strong>.",
 ],
 "zh": [
   "給你一個<strong>可能含有重複元素</strong>的整數陣列 <code>nums</code>，"
   "回傳它的所有子集（冪集合）。",
   "答案裡<strong>不能有重複的子集</strong>，順序不拘。",
 ],
 "pre": [
   ("note", "重複元素讓 2ⁿ 個子集裡出現重複", [
     ("c", """nums = [1, 2, 2]

如果照第 78 題（不去重）跑，會得到 2³ = 8 個：
    []      [1]     [2ₐ]    [1,2ₐ]
    [2ᵦ]    [1,2ᵦ]  [2ₐ,2ᵦ] [1,2ₐ,2ᵦ]

但 [2ₐ] 和 [2ᵦ] 的「值」相同，[1,2ₐ] 和 [1,2ᵦ] 也是。

不重複的子集只有 6 個：
    []  [1]  [2]  [1,2]  [2,2]  [1,2,2]

一般公式：
    每個不同的值 v 出現 cᵥ 次，
    不重複的子集數 = ∏ (cᵥ + 1)

    [1,2,2]：1 出現 1 次、2 出現 2 次
             (1+1) × (2+1) = 2 × 3 = 6 ✔

去重的兩種思路（和第 40、47 題完全一樣）：
    (a) 排序 + 同層跳過
    (b) 用 Counter 把相同的值合併，改成「決定取幾個」"""),
     "<strong>先算出「答案應該有幾個」，是驗證去重是否正確最快的方法。</strong>",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,2,2]
  輸出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

範例 2
  輸入：nums = [0]
  輸出：[[],[0]]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10",
   "−10 ≤ <code>nums[i]</code> ≤ 10",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 10</strong>，最多 <code>2¹⁰ = 1024</code> 個子集（去重後更少）。",
       "<strong>可能有重複元素</strong> —— 這是和第 78 題唯一的差別。",
       "<strong>沒說輸入已排序</strong>，所以<strong>要自己排</strong>（去重的前提）。",
     ]),
   ]),
 ],
 "idea": [
   ("t", ["解法", "去重方式", "和哪一題同構"],
     [["一、排序 + 同層跳過", "搜尋時判斷", "第 40 題（組合總和 II）"],
      ["二、Counter 決定取幾個", "資料結構保證", "第 40 題解法二"],
      ["三、迭代 + 控制起點", "只接在「新增的」後面", "第 78 題解法四的變形"]]),
 ],
 "approaches": [
   ap("解法一", "排序 + 同層去重（標準解）", [
     ("c", S["p90"]),
     ("h", "和第 78 題只差兩行"),
     ("c", """第 78 題（無重複）：
    def backtrack(start):
        out.append(path[:])
        for i in range(start, n):
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

第 90 題（有重複）：
    nums.sort()                                    <- 多這一行
    def backtrack(start):
        out.append(path[:])
        for i in range(start, n):
            if i > start and nums[i] == nums[i-1]: <- 多這一行
                continue
            ...

去重條件 i > start（不是 i > 0）的理由，
和第 40 題完全一樣：

    i == start  ->  這一層的第一個，永遠可以選
    i > start 且值和前一個相同  ->  這一層已經試過同樣的值了，跳過

    但【不同層】可以選相同的值 ——
    那代表「取了兩個 2」，是合法的子集。

    nums = [1, 2, 2]
    第 1 層（start=1）：i=1 選 2ₐ  -> path = [2ₐ]
        第 2 層（start=2）：i=2，i == start，不跳過
                            選 2ᵦ -> path = [2ₐ, 2ᵦ] = [2,2] ✔
    第 1 層：i=2，i > start(1) 且 nums[2]==nums[1] -> 跳過 ✔
             （否則會產生另一個 [2]，重複）"""),
     "<strong>強制「相同的值必須按陣列順序取」</strong>，"
     "所以每個「值的多重集合」只有唯一一條生成路徑 —— 不重不漏 ✔",
   ], "O(2ⁿ × n)", "O(n)", "去重後遠少於 2ⁿ",
      "path + 遞迴深度；不算輸出", optimal=True),

   ap("解法二", "Counter：對每個值決定「取幾個」", [
     ("c", S["p90_counter"]),
     ("c", """nums = [1, 2, 2]  ->  items = [(1, 1), (2, 2)]

  對 (1, 1)：取 0 個 或 1 個
  對 (2, 2)：取 0 個、1 個 或 2 個

  2 × 3 = 6 種組合 ✔ 剛好就是答案數

  遞迴樹：
      取 0 個 1 -> 取 0 個 2 -> []
                -> 取 1 個 2 -> [2]
                -> 取 2 個 2 -> [2,2]
      取 1 個 1 -> 取 0 個 2 -> [1]
                -> 取 1 個 2 -> [1,2]
                -> 取 2 個 2 -> [1,2,2]

每個葉子就是一個答案，而且【天然不會重複】——
因為「取幾個」這個決定對每個值只做一次。"""),
     "<strong>優點</strong>：",
     ("ul", [
       "<strong>不需要記 <code>i &gt; start</code> 這個容易寫錯的條件</strong>",
       "<strong>搜尋樹的大小剛好等於答案數</strong>（沒有任何被剪掉的分支）",
       "<strong>在重複值很多時快得多</strong>："
       "<code>[1]×10</code> 只有 11 個葉子，而解法一要走 11 條路徑但檢查了更多分支",
     ]),
     "<strong>缺點</strong>：產生的順序取決於 <code>sorted(Counter(...).items())</code>，"
     "而且 <code>path + [value] * take</code> 每層都複製一次 list。"
     "在 n ≤ 10 完全無所謂。",
     "<strong>我更推薦這個版本</strong> —— 它把「去重」從「搜尋時的判斷」"
     "變成「問題的重新表述」，比較不容易出錯。",
   ], "O(答案數 × n)", "O(n)", "沒有無用分支", "Counter + 遞迴深度"),

   ap("解法三", "迭代擴張 + 控制起點", [
     "第 78 題的迭代版（每加一個元素就把所有已知子集複製一份）"
     "<strong>在有重複值時會產生重複</strong>。修法是：<strong>重複的值只能接在"
     "「上一輪新增的那些子集」後面。</strong>",
     ("c", S["p90_iter"]),
     ("c", """nums = [1, 2, 2]（已排序）

  初始： out = [[]]

  i=0, x=1（第一個，begin=0）
      start = 1
      新增 [[] + [1]] = [[1]]
      out = [[], [1]]

  i=1, x=2（和前一個 1 不同，begin=0）
      start = 2
      新增 out[0..1] 各加 2 = [[2], [1,2]]
      out = [[], [1], [2], [1,2]]

  i=2, x=2（和前一個 2 相同！begin = start = 2）
      start = 4
      只從 out[2..3] 開始加 = [[2,2], [1,2,2]]
      out = [[], [1], [2], [1,2], [2,2], [1,2,2]]  ✔ 6 個

  如果 begin 錯誤地設成 0：
      會新增 [[2], [1,2], [2,2], [1,2,2]]
      -> [2] 和 [1,2] 重複了 ✘

關鍵：重複的值只能「接在上一輪剛產生的子集」後面，
      這樣才不會製造出「同樣個數的 2」的兩份。"""),
     "<strong>不用遞迴</strong>，但 <code>begin</code> 和 <code>start</code> 的關係"
     "要想很清楚。<strong>面試時不建議寫這個版本</strong>（解釋成本太高）。",
   ], "O(答案數 × n)", "O(答案數 × n)", "每個子集建一次", "所有中間結果"),
 ],
 "compare": (["解法", "要排序？", "去重方式", "有無用分支？", "推薦度"],
   [["一、同層跳過", "✔", "搜尋時判斷", "有（被 continue 掉）", "★★★★☆"],
    ["二、Counter", "✘（Counter 不在乎）", "重新表述問題", "沒有", "★★★★★"],
    ["三、迭代 + begin", "✔", "控制起點", "沒有", "★★☆☆☆"]]),
 "edges": [
   "<strong>全部相同</strong>：<code>[1,1,1]</code> → 4 個（<code>[]、[1]、[1,1]、[1,1,1]</code>）。"
   "<strong>最能抓出去重 bug 的測資。</strong>",
   "<strong>成對重複</strong>：<code>[1,2,2]</code> → 6 個。",
   "<strong>沒有重複</strong>：<code>[1,2,3]</code> → 8 個。退化成第 78 題。",
   "<strong>單一元素</strong>：<code>[0]</code> → <code>[[], [0]]</code>。",
   "<strong>沒排序的輸入</strong>：<code>[4,4,4,1,4]</code> → 應該是 "
   "<code>(4+1) × (1+1) = 10</code> 個。"
   "<strong>忘記排序的話會產生大量重複。</strong>",
   "<strong>答案數量</strong>：<code>∏ (cᵥ + 1)</code>。"
   "<strong>先算這個數再檢查程式輸出。</strong>",
 ],
 "follow": [
   ("h", "追問一：三個「同層去重」的題目有什麼共同點？"),
   ("c", """第 40 題 Combination Sum II（組合 + 和的條件）
    if i > start and candidates[i] == candidates[i-1]: continue

第 47 題 Permutations II（排列）
    if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue

第 90 題 Subsets II（子集）
    if i > start and nums[i] == nums[i-1]: continue

三者在說同一件事：
    「同一層裡，相同的值只選第一次出現的那個」

差別只在「怎麼判斷『同一層』」：
    有 start 的（組合、子集）-> i > start
    沒有 start 的（排列）    -> not used[i-1]

而且三者都【必須先排序】。

一句話記住：
    「讓每個答案只有唯一一條生成路徑」

    做法：強制「相同的值必須按陣列順序被使用」。""",),
   ("h", "追問二：為什麼位元遮罩法（第 78 題解法三）在這裡失效？"),
   ("c", """nums = [1, 2, 2]

  mask = 0b010 -> 選 nums[1] = 2  -> [2]
  mask = 0b100 -> 選 nums[2] = 2  -> [2]   重複！

  位元遮罩枚舉的是「選哪些【位置】」，
  而不是「選哪些【值】」。

  位置不同但值相同 -> 產生重複的子集。

  只能事後用 set 去重 —— 但那就浪費了 2ⁿ 的搜尋。

所以「有重複元素」的版本只能用回溯（或 Counter）。""",),
   ("h", "追問三：答案的數量怎麼算？"),
   "<code>∏ (cᵥ + 1)</code>，其中 <code>cᵥ</code> 是值 <code>v</code> 出現的次數。",
   ("c", """[1,2,2]：      (1+1)(2+1) = 6
[1,1,1]：      (3+1) = 4
[1,2,3]：      2×2×2 = 8
[4,4,4,1,4]：  (4+1)(1+1) = 10

直覺：對每個不同的值，獨立決定「要取 0 個、1 個、…、cᵥ 個」。

這也正是解法二（Counter 版）搜尋樹的葉子數 ——
所以那個版本【一個無用的節點都沒有】。

寫完程式之後先用這個公式算一遍，是最快的驗證。""",),
 ],
 "related": [
   "<strong>第 78 題 Subsets</strong> —— 無重複元素的版本",
   "<strong>第 40 題 Combination Sum II</strong> —— 組合的同層去重",
   "<strong>第 47 題 Permutations II</strong> —— 排列的同層去重",
   "<strong>第 77 題 Combinations</strong> —— 限定大小的子集",
 ],
 "check": [
   "去重條件為什麼是 <code>i &gt; start</code> 而不是 <code>i &gt; 0</code>？"
   "請用 <code>[1,2,2]</code> 說明後者會漏掉什麼。",
   "為什麼位元遮罩枚舉法在有重複元素時會失效？",
   "<code>[4,4,4,1,4]</code> 應該有幾個子集？用公式算一遍。",
   "Counter 版本的搜尋樹為什麼「一個無用的節點都沒有」？",
 ],
})
print("P90 written")
