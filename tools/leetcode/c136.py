# -*- coding: utf-8 -*-
"""第 136–140 題。"""
import random, functools
from collections import Counter
from authoring import emit, ap
from runner import Src, ListNode

S = Src()
random.seed(136)

# ==================== 136. Single Number ====================
S["p136_xor"] = '''class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res ^= x            # 成對的會互相抵銷，剩下的就是答案
        return res'''

S["p136_reduce"] = '''from functools import reduce
from operator import xor

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)'''

S["p136_math"] = '''class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 2 × (不重複的總和) − (全部的總和) = 那個落單的數
        return 2 * sum(set(nums)) - sum(nums)'''


def _p136_ref(nums):
    c = Counter(nums)
    return [k for k, v in c.items() if v == 1][0]


_p136 = [S.load(k) for k in ("p136_xor", "p136_reduce", "p136_math")]

for nums, want in [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4), ([1], 1), ([0, 1, 0], 1)]:
    assert _p136_ref(nums) == want
    for sol in _p136:
        assert sol.singleNumber(list(nums)) == want, ("P136", nums, sol)

for _ in range(5000):
    k = random.randrange(0, 8)
    vals = random.sample(range(-40, 40), k + 1)
    nums = [vals[0]] + [v for v in vals[1:] for _ in (0, 1)]
    random.shuffle(nums)
    want = vals[0]
    assert _p136_ref(nums) == want
    for sol in _p136:
        assert sol.singleNumber(list(nums)) == want, ("P136 random", nums, want, sol)
print("P136 solutions OK")

_P136_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">XOR（互斥或）的三個性質，合起來就是這一題的完整解答。</text>
            <g font-size="13">
              <text x="40" y="56" fill="var(--gold)">① a ^ a = 0　　　　　 自己和自己抵銷</text>
              <text x="40" y="84" fill="var(--gold)">② a ^ 0 = a　　　　　 0 是單位元素</text>
              <text x="40" y="112" fill="var(--gold)">③ 可交換、可結合　　  順序完全不影響結果</text>
            </g>
            <text x="20" y="150" fill="var(--accent)" font-size="12">有了 ③，就可以把所有數字【重新排列】成「成對的排前面」：</text>
            <text x="40" y="180" fill="var(--text-muted)" font-size="12">4 ^ 1 ^ 2 ^ 1 ^ 2　=　(1 ^ 1) ^ (2 ^ 2) ^ 4　=　0 ^ 0 ^ 4　=　4 ✔</text>
            <line x1="20" y1="204" x2="620" y2="204" stroke="var(--border)"/>
            <text x="20" y="232" fill="var(--accent)" font-size="13">逐位元來看為什麼成立：</text>
            <g font-size="12" text-anchor="middle">
              <text x="120" y="262" fill="var(--text-muted)" text-anchor="start">數字　二進位</text>
              <text x="120" y="288" fill="var(--text-muted)" text-anchor="start">4　　 1 0 0</text>
              <text x="120" y="312" fill="var(--text-muted)" text-anchor="start">1　　 0 0 1</text>
              <text x="120" y="336" fill="var(--text-muted)" text-anchor="start">2　　 0 1 0</text>
              <text x="120" y="360" fill="var(--text-muted)" text-anchor="start">1　　 0 0 1</text>
              <text x="120" y="384" fill="var(--text-muted)" text-anchor="start">2　　 0 1 0</text>
              <line x1="180" y1="396" x2="290" y2="396" stroke="var(--border)"/>
              <text x="120" y="420" fill="var(--gold)" text-anchor="start">XOR　 1 0 0　= 4 ✔</text>
            </g>
            <text x="330" y="288" fill="var(--text-muted)" font-size="12" text-anchor="start">XOR 在每一個位元上獨立運作，</text>
            <text x="330" y="312" fill="var(--text-muted)" font-size="12" text-anchor="start">它算的是「這一位有幾個 1」的【奇偶性】。</text>
            <text x="330" y="344" fill="var(--accent)" font-size="12" text-anchor="start">出現兩次的數，在每一位都貢獻</text>
            <text x="330" y="368" fill="var(--accent)" font-size="12" text-anchor="start">偶數個 1 → 對奇偶性沒有影響。</text>
            <text x="330" y="400" fill="var(--gold)" font-size="12" text-anchor="start">所以最後剩下的，就是那個</text>
            <text x="330" y="424" fill="var(--gold)" font-size="12" text-anchor="start">只出現一次的數字。</text>'''

emit({
 "num": 136, "slug": "single-number",
 "en": [
   "Given a <strong>non-empty</strong> array of integers <code>nums</code>, every element "
   "appears <em>twice</em> except for one. Find that single one.",
   "You must implement a solution with a linear runtime complexity and use only constant extra "
   "space.",
 ],
 "zh": [
   "給你一個<strong>非空</strong>的整數陣列 <code>nums</code>，"
   "裡面<strong>每個數字都出現兩次，只有一個出現一次</strong>。找出那一個。",
   "<strong>要求：時間 <code>O(n)</code>、額外空間 <code>O(1)</code>。</strong>",
 ],
 "pre": [
   ("note", "★ 兩個要求把「顯而易見」的做法都排除了", [
     ("c", """用雜湊表數次數：O(n) 時間，但 O(n) 空間 ✘
先排序再找：      O(1) 空間（原地排序），但 O(n log n) 時間 ✘

    題目要【同時】滿足 O(n) 時間和 O(1) 空間 ——
    這就強迫你去想「位元運算」。

【看到「O(n) 時間 + O(1) 空間 + 找落單的數字」，
  反射動作就是 XOR。】

    這是一個非常標準的訊號組合。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [2,2,1]
  輸出：1

範例 2
  輸入：nums = [4,1,2,1,2]
  輸出：4

範例 3
  輸入：nums = [1]
  輸出：1""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 3 × 10⁴",
   "−3 × 10⁴ ≤ <code>nums[i]</code> ≤ 3 × 10⁴",
   "除了某一個元素只出現一次外，<strong>其餘每個元素都恰好出現兩次</strong>",
 ],
 "idea": [
   ("fig", _P136_FIG, "0 0 640 442"),
   ("c", """XOR（^，互斥或）的三個性質：

    ① a ^ a = 0        自己和自己抵銷
    ② a ^ 0 = a        0 是單位元素
    ③ 可交換、可結合    a ^ b = b ^ a，(a^b)^c = a^(b^c)

有了 ③，就可以把所有數字重新排列：

    4 ^ 1 ^ 2 ^ 1 ^ 2
      = 4 ^ (1 ^ 1) ^ (2 ^ 2)      （重排）
      = 4 ^ 0 ^ 0                  （用 ①）
      = 4                          （用 ②）✔

【為什麼 XOR 有這些性質？】

    XOR 在【每一個位元上獨立運作】，
    而它算的是「這一位上有幾個 1」的【奇偶性】：

        奇數個 1 -> 結果是 1
        偶數個 1 -> 結果是 0

    出現兩次的數，在每一位都貢獻偶數個 1
    -> 對奇偶性完全沒有影響 ✔

    所以剩下的就是那個落單的數字。

【一行解，O(n) 時間、O(1) 空間。】"""),
 ],
 "approaches": [
   ap("解法一", "XOR 全部（標準答案）", [
     ("c", S["p136_xor"]),
     "<strong>四行，O(n) 時間、O(1) 空間。</strong>"
     "<strong>不可能有更好的解。</strong>",
     ("h", "<code>res</code> 為什麼初始成 0？"),
     "<strong>因為 0 是 XOR 的單位元素</strong>（<code>0 ^ x = x</code>）。",
     "<strong>這和「求和初始成 0」「求積初始成 1」是同一個原則</strong> —— "
     "<strong>base case 要填對「該運算的單位元素」。</strong>"
     "<strong>（第 111、112、124、129 題都出現過這個原則。）</strong>",
     ("h", "負數會有問題嗎？"),
     ("c", """不會。

    XOR 是「逐位元」的運算，
    對補數表示的負數一樣正確。

    例如 (-3) ^ (-3) = 0 ✔

【Python 的整數是「無限位元」的，
  負數用「概念上無限延伸的 1」表示】——

    但 XOR 的抵銷性質不受影響，
    因為 a ^ a = 0 對任何 a 都成立。

    在 C/Java 裡也一樣（32 位元補數）。

【唯一要小心的是「右移」】：
    Python 的 >> 對負數是算術右移（補 1），
    而且沒有無號右移（>>>）。
    這在第 190 題（顛倒位元）會變成問題。"""),
   ], "O(n)", "O(1)", "掃一遍", "一個變數", optimal=True),

   ap("解法二", "<code>reduce</code> 一行版", [
     ("c", S["p136_reduce"]),
     ("c", """from functools import reduce
from operator import xor
return reduce(xor, nums)

    reduce(f, [a, b, c]) 等於 f(f(a, b), c)

    這裡就是 a ^ b ^ c ✔

【為什麼不寫 reduce(lambda a, b: a ^ b, nums)？】

    operator.xor 是 C 層實作的，比 lambda 快得多。

    operator 模組有一整套：
        add, sub, mul, and_, or_, xor, lt, gt, itemgetter, ...

    需要「把運算子當成函式傳」時，優先用它。

【reduce 沒有初始值時，會拿第一個元素當初始值】——
    對空序列會丟 TypeError。

    題目保證非空，所以沒問題。
    要保險的話：reduce(xor, nums, 0)""",),
     "<strong>和解法一完全等價，只是更短。</strong>"
     "<strong>面試時寫解法一（明確展示你懂 XOR），提一句「也可以用 reduce」。</strong>",
   ], "O(n)", "O(1)", "掃一遍", "一個變數"),

   ap("解法三", "數學：<code>2×sum(set) − sum</code>（不滿足空間要求）", [
     ("c", S["p136_math"]),
     ("c", """設落單的是 x，其餘每個數 y 都出現兩次。

    sum(nums)      = x + 2·(y1 + y2 + ...)
    sum(set(nums)) = x + (y1 + y2 + ...)

    2·sum(set) - sum
      = 2x + 2·(Σy) - x - 2·(Σy)
      = x  ✔

【很漂亮，但它用了 O(n) 空間（那個 set）】——
    不滿足題目的 O(1) 要求。

【不過這個技巧在別的題目很有用】：

    第 268 題（缺失的數字）：
        答案 = n(n+1)/2 - sum(nums)

    第 448 題（找到所有消失的數字）
    第 41 題（第一個缺失的正數）

    【「用總和的差」來找出缺失 / 多餘的元素，
      是一個標準手法。】

    缺點是「可能溢位」（在 C/Java 裡），
    而 XOR 版完全沒有這個問題 ——
    這也是 XOR 版更好的一個理由。""",),
   ], "O(n)", "O(n)", "掃兩遍", "去重的集合"),
 ],
 "compare": (["解法", "時間", "空間", "符合要求", "備註"],
   [["一、XOR", "O(n)", "O(1)", "✔", "標準答案，四行"],
    ["二、reduce", "O(n)", "O(1)", "✔", "一行"],
    ["三、2×sum(set)−sum", "O(n)", "O(n)", "✘", "技巧本身很有用"]]),
 "edges": [
   "<strong>只有一個元素</strong> <code>[1]</code> → <code>1</code>。<code>0 ^ 1 = 1</code> ✔",
   "<strong>落單的是 0</strong> <code>[0,1,1]</code> → <code>0</code>。"
   "<strong>用「真假值」判斷會出錯，XOR 不會。</strong>",
   "<strong>有負數</strong> → XOR 一樣正確。",
   "<strong><code>res</code> 初始成別的值</strong> → 答案會被那個值污染。",
   "<strong>3 × 10⁴ 個元素</strong> → O(n) 輕鬆。",
 ],
 "follow": [
   ("h", "追問一：如果每個數出現【三次】，只有一個出現一次呢？"),
   "<strong>第 137 題</strong>。XOR 就不夠了 —— "
   "<strong>因為 <code>a ^ a ^ a = a</code>（三個抵銷不掉）。</strong>",
   "<strong>要改成「逐位數 mod 3」或「兩個狀態變數的位元魔法」</strong>，見下一題。",
   ("h", "追問二：如果有【兩個】數各出現一次呢？"),
   "<strong>第 260 題（Single Number III）。分兩步</strong>：",
   ("c", """1. 全部 XOR 起來，得到 x ^ y（那兩個落單的數的 XOR）

2. 找出 x ^ y 裡【任何一個是 1 的位元】
       diff = xor_all & (-xor_all)        取最低位的 1

   那一位是 1，代表 x 和 y 在那一位【不同】。

3. 按照「那一位是 0 還是 1」把所有數字分成兩組，
   每組各自 XOR -> 分別得到 x 和 y ✔

   （成對的數一定會被分到同一組，因為它們完全相同。）

【x & (-x) 取出最低位的 1】：

    x     = 0b1011000
    -x    = 0b0101000   （補數：取反加一）
    x & -x = 0b0001000  ✔

    這是位元技巧裡最常用的一招，
    在樹狀陣列（Fenwick Tree）裡也是核心。""",),
   ("h", "追問三：XOR 還有哪些經典用途？"),
   ("ul", [
     "<strong>交換兩個變數不用暫存</strong>：<code>a^=b; b^=a; a^=b</code>"
     "（但實務上別這樣寫 —— <code>a</code> 和 <code>b</code> 是同一個變數時會歸零）。",
     "<strong>第 268 題 缺失的數字</strong>：把 <code>0..n</code> 和陣列全部 XOR。",
     "<strong>第 389 題 找不同</strong>：兩個字串全部 XOR。",
     "<strong>Nim 遊戲與 SG 函數</strong>：組合賽局的必勝判斷用 XOR。",
     "<strong>RAID 5 的同位檢查</strong>：一顆硬碟壞了，用其他硬碟 XOR 還原。",
     "<strong>一次性密碼本（one-time pad）</strong>：<code>明文 ^ 金鑰 = 密文</code>，"
     "<code>密文 ^ 金鑰 = 明文</code>。",
   ]),
   "<strong>共同性質：XOR 是「自己的反運算」</strong>（<code>(a^b)^b = a</code>）—— "
   "<strong>這讓它在「可逆的組合」場合特別有用。</strong>",
   ("h", "追問四：為什麼題目要保證「非空」？"),
   "<strong>因為空陣列時「那個落單的數」不存在。</strong>",
   "<strong>但 XOR 版會回傳 0</strong>（初始值）—— "
   "<strong>那是一個「看起來合理但其實無意義」的答案。</strong>"
   "<strong>這種「錯誤輸入回傳合法值」的情況，比直接 crash 更危險 —— "
   "因為呼叫者不會發現有問題。</strong>",
 ],
 "related": [
   "<strong>第 137 題 Single Number II</strong> —— 出現三次的版本",
   "<strong>第 260 題 Single Number III</strong> —— 兩個落單的數",
   "<strong>第 268 題 Missing Number</strong> —— 同樣可用 XOR",
   "<strong>第 389 題 Find the Difference</strong> —— 字串版",
   "<strong>第 191 題 Number of 1 Bits</strong> —— 另一個位元運算經典",
 ],
 "check": [
   "XOR 的哪三個性質讓這題成立？",
   "為什麼 <code>res</code> 要初始成 0？",
   "落單的數字是 0 時，這個解法還對嗎？",
   "如果每個數出現三次，XOR 為什麼就不夠了？",
 ],
})
print("P136 written")

# ==================== 137. Single Number II ====================
S["p137_bits"] = '''class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for b in range(32):
            # 數所有數字在第 b 位上有幾個 1
            cnt = sum((x >> b) & 1 for x in nums)
            if cnt % 3:                     # 不是 3 的倍數 -> 答案在這一位是 1
                res |= 1 << b

        # Python 的整數沒有位寬，要自己處理負數
        return res - (1 << 32) if res >= (1 << 31) else res'''

S["p137_state"] = '''class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ones / twos：每一位上「目前看過 1 的次數 mod 3」的兩位元編碼
        #   (twos, ones) = (0,0) -> 看過 0 次
        #                  (0,1) -> 看過 1 次
        #                  (1,0) -> 看過 2 次
        ones = twos = 0

        for x in nums:
            ones = (ones ^ x) & ~twos       # 先更新 ones
            twos = (twos ^ x) & ~ones       # 再用【新的】ones 更新 twos

        return ones'''

S["p137_counter"] = '''from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 最直白：數次數（但用了 O(n) 空間）
        for k, v in Counter(nums).items():
            if v == 1:
                return k
        return -1'''


def _p137_ref(nums):
    c = Counter(nums)
    return [k for k, v in c.items() if v == 1][0]


_p137 = [S.load(k) for k in ("p137_bits", "p137_state", "p137_counter")]

for nums, want in [
    ([2, 2, 3, 2], 3),
    ([0, 1, 0, 1, 0, 1, 99], 99),
    ([1], 1),
    ([-2, -2, 1, -2], 1),
    ([-4, -4, -4, 7], 7),
    ([5, 5, 5, -7], -7),
]:
    assert _p137_ref(nums) == want, ("P137 ref", nums)
    for sol in _p137:
        assert sol.singleNumber(list(nums)) == want, ("P137", nums, want, sol.singleNumber(list(nums)), sol)

for _ in range(5000):
    k = random.randrange(0, 7)
    vals = random.sample(range(-(2 ** 20), 2 ** 20), k + 1)
    nums = [vals[0]] + [v for v in vals[1:] for _ in range(3)]
    random.shuffle(nums)
    want = vals[0]
    for sol in _p137:
        got = sol.singleNumber(list(nums))
        assert got == want, ("P137 random", want, got, sol)
print("P137 solutions OK")

_P137_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">XOR 在這題不夠用：a ^ a ^ a = a，三個一樣的數抵銷不掉。要換一套「模 3」的計數法。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">方法一：逐位元數 1 的個數，再對 3 取餘數</text>
            <text x="20" y="80" fill="var(--text-muted)" font-size="12">nums = [2, 2, 3, 2]　　二進位： 010, 010, 011, 010</text>
            <g font-size="13" text-anchor="middle">
              <text x="150" y="112" fill="var(--text-muted)">第 2 位</text><text x="280" y="112" fill="var(--text-muted)">第 1 位</text><text x="410" y="112" fill="var(--text-muted)">第 0 位</text>
              <text x="150" y="140" fill="var(--text-muted)">0 個 1</text><text x="280" y="140" fill="var(--text-muted)">4 個 1</text><text x="410" y="140" fill="var(--text-muted)">1 個 1</text>
              <text x="150" y="168" fill="var(--accent)">0 mod 3 = 0</text><text x="280" y="168" fill="var(--accent)">4 mod 3 = 1</text><text x="410" y="168" fill="var(--accent)">1 mod 3 = 1</text>
            </g>
            <text x="20" y="202" fill="var(--gold)" font-size="12">答案的二進位 = 0 1 1 = 3 ✔</text>
            <text x="20" y="228" fill="var(--text-muted)" font-size="12">出現三次的數在每一位都貢獻 0 或 3 個 1 → 對「mod 3」完全沒有影響。</text>
            <line x1="20" y1="252" x2="620" y2="252" stroke="var(--border)"/>
            <text x="20" y="280" fill="var(--gold)" font-size="13">方法二：用兩個變數當「每一位的模 3 計數器」</text>
            <text x="20" y="308" fill="var(--text-muted)" font-size="12">一位元只能存 0/1，但我們要數到 0/1/2 —— 所以用【兩個】變數合起來當兩位元：</text>
            <g font-size="12" text-anchor="middle">
              <rect x="120" y="326" width="120" height="26" fill="none" stroke="var(--border)"/><text x="180" y="344" fill="var(--text-muted)">(twos, ones)</text>
              <rect x="260" y="326" width="100" height="26" fill="none" stroke="var(--border)"/><text x="310" y="344" fill="var(--text-muted)">看過幾次</text>
              <rect x="120" y="352" width="120" height="26" fill="none" stroke="var(--accent)"/><text x="180" y="370" fill="var(--accent)">(0, 0)</text>
              <rect x="260" y="352" width="100" height="26" fill="none" stroke="var(--accent)"/><text x="310" y="370" fill="var(--accent)">0 次</text>
              <rect x="120" y="378" width="120" height="26" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="180" y="396" fill="var(--gold)">(0, 1)</text>
              <rect x="260" y="378" width="100" height="26" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="310" y="396" fill="var(--gold)">1 次 ← 答案</text>
              <rect x="120" y="404" width="120" height="26" fill="none" stroke="var(--accent)"/><text x="180" y="422" fill="var(--accent)">(1, 0)</text>
              <rect x="260" y="404" width="100" height="26" fill="none" stroke="var(--accent)"/><text x="310" y="422" fill="var(--accent)">2 次</text>
            </g>
            <text x="390" y="370" fill="var(--text-muted)" font-size="11" text-anchor="start">第三次出現時，狀態從</text>
            <text x="390" y="392" fill="var(--text-muted)" font-size="11" text-anchor="start">(1,0) 轉回 (0,0) —— 歸零。</text>
            <text x="390" y="420" fill="var(--gold)" font-size="11" text-anchor="start">所以最後 ones 就是答案。</text>
            <text x="20" y="456" fill="#ff8a65" font-size="12">★ 兩行更新的順序不能換：twos 那一行用的是【已經更新過】的 ones。</text>'''

emit({
 "num": 137, "slug": "single-number-ii",
 "en": [
   "Given an integer array <code>nums</code> where every element appears <strong>three "
   "times</strong> except for one, which appears <strong>exactly once</strong>. "
   "<em>Find the single element and return it</em>.",
   "You must implement a solution with a linear runtime complexity and use only constant extra "
   "space.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，"
   "裡面<strong>每個數字都出現三次，只有一個恰好出現一次</strong>。找出那一個。",
   "<strong>要求：時間 <code>O(n)</code>、額外空間 <code>O(1)</code>。</strong>",
 ],
 "pre": [
   ("note", "★ 為什麼第 136 題的 XOR 在這裡失效", [
     ("c", """XOR 之所以能解第 136 題，是因為 a ^ a = 0。

    但 a ^ a ^ a = (a ^ a) ^ a = 0 ^ a = a  ✘

    三個相同的數 XOR 起來還是它自己，抵銷不掉。

【本質原因】：

    XOR 算的是「1 的個數 mod 2」。

    這題需要的是「1 的個數 mod 3」——
    而 XOR 沒有這個能力。

【所以要自己造一個「mod 3 的計數器」】：

    方法一：真的逐位去數（解法一）
        對每一位，數所有數字在那一位有幾個 1，
        然後對 3 取餘數。

    方法二：用兩個變數編碼「mod 3 的狀態」（解法二）
        因為 0/1/2 需要兩位元，所以用兩個整數變數，
        讓它們在【每一位上】合起來表示狀態。

【推廣】：
    每個數出現 k 次、一個出現一次
    -> 逐位數 mod k，或者用 ⌈log₂ k⌉ 個狀態變數。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [2,2,3,2]
  輸出：3

範例 2
  輸入：nums = [0,1,0,1,0,1,99]
  輸出：99""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 3 × 10⁴",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
   "除了某一個元素只出現一次外，<strong>其餘每個元素都恰好出現三次</strong>",
 ],
 "mid": [
   ("note", "★ Python 的整數沒有位寬 —— 這題會被咬到", [
     ("c", """題目說數字範圍是 32 位元有號整數（−2³¹ 到 2³¹−1）。

    但 Python 的整數是【任意精度】的，
    負數在概念上有「無限多個前導 1」。

    所以解法一「逐位數 32 位」之後，
    如果答案的第 31 位是 1（代表它是負數），
    直接回傳會得到一個【很大的正數】而不是負數。

    例如 −7 在 32 位元下是 0xFFFFFFF9 = 4294967289，
    直接回傳就是這個大正數 ✘

【修正】：

    return res - (1 << 32) if res >= (1 << 31) else res

    「如果最高位（符號位）是 1，就減掉 2³²」——
    這就是「把無號數轉回有號數」的標準做法。

【解法二（狀態機）沒有這個問題】，
    因為它從頭到尾都在做位元運算，
    負數的表示被完整保留下來 ✔

【這是 Python 做位元題目最常見的坑】，
    第 190 題（顛倒位元）、第 371 題（不用加號的加法）
    也都會遇到。"""),
   ]),
 ],
 "idea": [
   ("fig", _P137_FIG, "0 0 640 474"),
   ("c", """【方法一：逐位元數 mod 3】

    for b in 0..31:
        cnt = 有幾個數字的第 b 位是 1
        if cnt % 3 != 0:
            答案的第 b 位是 1

    為什麼對？
        出現三次的數，在每一位都貢獻 0 或 3 個 1
        -> 對 mod 3 沒有影響 ✔

        所以剩下的餘數，完全來自那個落單的數。

    O(32n) = O(n) 時間、O(1) 空間 ✔

【方法二：兩個狀態變數】

    想像每一位上有一個「mod 3 計數器」，
    它的值是 0、1、2。

    兩位元可以表示這三個狀態：

        (twos, ones) = (0,0) -> 看過 0 次
                       (0,1) -> 看過 1 次
                       (1,0) -> 看過 2 次
                       (1,1) -> 【不會出現】

    轉移（當這一位出現一個 1 時）：
        (0,0) -> (0,1) -> (1,0) -> (0,0) -> ...

    用位元運算實現這個狀態機：

        ones = (ones ^ x) & ~twos
        twos = (twos ^ x) & ~ones

    最後 ones 就是「看過 1 次」的那些位 = 答案 ✔

    【這兩行很難自己推出來，但可以驗證它是對的 ——
      見解法二的逐狀態檢查。】"""),
 ],
 "approaches": [
   ap("解法一", "逐位元數 mod 3（最好懂）", [
     ("c", S["p137_bits"]),
     "<strong>七行，O(32n) 時間、O(1) 空間。</strong>"
     "<strong>面試時寫這個 —— 它的正確性一句話就能說清楚。</strong>",
     ("h", "★ 最後那行負數處理"),
     ("c", """return res - (1 << 32) if res >= (1 << 31) else res

    res >= 2^31 代表「第 31 位（符號位）是 1」-> 這是個負數。

    32 位元補數的解讀方式：
        無號值 u 對應的有號值是 u - 2^32（當 u >= 2^31 時）

    驗算 −7：
        32 位元補數 = 0xFFFFFFF9 = 4294967289
        4294967289 - 4294967296 = -7  ✔

【在 C/Java 裡不用這一行】——
    因為 int 本來就是 32 位元，溢位會自動繞回來。

    這純粹是 Python「整數無限大」帶來的副作用。

【要怎麼記住這件事？】

    反射：在 Python 裡做「固定位寬」的位元運算時，
          如果結果可能是負數，最後一定要手動轉換。

    另一個常見寫法：
        res = res & 0xFFFFFFFF          先截斷成 32 位
        if res >= 0x80000000:
            res -= 0x100000000"""),
     ("h", "為什麼用 <code>range(32)</code> 而不是動態決定位數？"),
     "<strong>因為題目保證是 32 位元整數。</strong>"
     "<strong>如果範圍更大（例如 64 位元），就要改成 <code>range(64)</code>。</strong>",
     "<strong>「固定 32 位」讓複雜度是 O(32n) 而不是 O(n log(max))</strong> —— "
     "<strong>對這題來說兩者一樣，但在「數值範圍很大」時要注意。</strong>",
   ], "O(32n)", "O(1)", "32 位 × n 個數", "幾個變數", optimal=True),

   ap("解法二", "兩個狀態變數（位元魔法，O(n) 一趟）", [
     ("c", S["p137_state"]),
     ("h", "★ 逐狀態驗證這兩行"),
     ("c", """ones = (ones ^ x) & ~twos
twos = (twos ^ x) & ~ones      ← 用【新的】ones

    只看某一位，設 x 在這一位是 b（0 或 1）。

【情況 b = 0】（這個數在這一位是 0）：

    ones' = (ones ^ 0) & ~twos = ones & ~twos
    因為 (twos, ones) 不會同時是 1，ones & ~twos = ones
    -> ones 不變 ✔

    twos' = (twos ^ 0) & ~ones' = twos & ~ones
    -> twos 不變 ✔

    （出現 0，狀態不該變 ✔）

【情況 b = 1】：

    狀態 (0,0)「0 次」：
        ones' = (0 ^ 1) & ~0 = 1 & 1 = 1
        twos' = (0 ^ 1) & ~1 = 1 & 0 = 0
        -> (0,1)「1 次」 ✔

    狀態 (0,1)「1 次」：
        ones' = (1 ^ 1) & ~0 = 0 & 1 = 0
        twos' = (0 ^ 1) & ~0 = 1 & 1 = 1
        -> (1,0)「2 次」 ✔

    狀態 (1,0)「2 次」：
        ones' = (0 ^ 1) & ~1 = 1 & 0 = 0
        twos' = (1 ^ 1) & ~0 = 0 & 1 = 0
        -> (0,0)「0 次」 ✔ 歸零

    三個狀態循環，完全正確 ✔

【★ 順序不能換】

    twos 那一行用的是【新算出來的 ones】。

    換成用舊的 ones，狀態 (0,1) 那一格就會算錯：
        twos' = (0 ^ 1) & ~1 = 0   ✘ 應該是 1

    【這是本解法第一名的 bug。】""",),
     ("h", "為什麼最後回傳 <code>ones</code>？"),
     "<strong>因為落單的數字只出現一次，它的每一位（是 1 的那些）"
     "最後都停在「1 次」的狀態，也就是 <code>ones</code> 裡的 1。</strong>",
     "<strong>而出現三次的數字，每一位都回到了「0 次」—— 不會留在 <code>ones</code> 裡 ✔</strong>",
     ("h", "Python 的 <code>~</code> 對負數安全嗎？"),
     ("c", """~x 在 Python 裡是 -(x+1)（概念上無限延伸的補數）。

    看起來很可怕，但【對這個演算法是安全的】——

    因為所有運算都是 & ^ ~ 的組合，
    它們在「無限位元」的模型下和「32 位元」的模型
    在【每一個實際的位元上】行為完全相同 ✔

    而輸入的負數本身就帶著正確的無限延伸表示，
    所以輸出也會是正確的負數。

    【這就是為什麼解法二不需要最後那行轉換，
      而解法一需要 ——

      解法一「重新組裝」了一個數（從 0 開始 |=），
      失去了原本的符號資訊；
      解法二從頭到尾都在「加工原本的數」，
      符號資訊一路被保留。】""",),
     "<strong>O(n) 一趟、O(1) 空間，常數比解法一小 32 倍。</strong>"
     "<strong>但它幾乎不可能在面試現場推導出來 —— 屬於「知道就會、不知道就想不到」的技巧。</strong>",
   ], "O(n)", "O(1)", "一趟掃描", "兩個變數"),

   ap("解法三", "<code>Counter</code>（不滿足空間要求，但先講）", [
     ("c", S["p137_counter"]),
     "<strong>三行。O(n) 時間、O(n) 空間。</strong>",
     "<strong>面試時可以先寫它把問題確認清楚，然後說"
     "「這用了 O(n) 空間，我可以用位元運算做到 O(1)」。</strong>",
     ("c", """【Counter 的其他寫法】：

    # 找出計數為 1 的那個
    return next(k for k, v in Counter(nums).items() if v == 1)

    # 或者用 most_common（但那要排序，比較慢）
    return Counter(nums).most_common()[-1][0]

【next(生成式) 這個寫法很好用】：
    「找出第一個滿足條件的元素」——
    而且是【惰性】的，找到就停。

    比 [x for x in ... if cond][0] 好，
    後者會把整個 list 建出來。""",),
   ], "O(n)", "O(n)", "數次數", "雜湊表"),
 ],
 "compare": (["解法", "時間", "空間", "要處理負數嗎", "好推導嗎"],
   [["一、逐位數 mod 3", "O(32n)", "O(1)", "✔ Python 要", "★★★"],
    ["二、兩個狀態變數", "O(n)", "O(1)", "✘", "★☆☆"],
    ["三、Counter", "O(n)", "O(n)", "✘", "★★★"]]),
 "edges": [
   "<strong>只有一個元素</strong> <code>[1]</code> → <code>1</code>。",
   "<strong>落單的是 0</strong> <code>[1,1,1,0]</code> → <code>0</code>。",
   "<strong>落單的是負數</strong> <code>[5,5,5,-7]</code> → <code>-7</code>。"
   "<strong>解法一沒有最後那行轉換的話會回傳 4294967289。本題在 Python 下的第一名陷阱。</strong>",
   "<strong>出現三次的是負數</strong> <code>[-2,-2,-2,1]</code> → <code>1</code>。",
   "<strong>解法二兩行順序寫反</strong> → 狀態機錯，答案錯。",
   "<strong>用 XOR</strong> → 三個抵銷不掉，答案完全錯。",
   "<strong>3 × 10⁴ 個元素</strong> → 解法一要 96 萬次運算，完全沒問題。",
 ],
 "follow": [
   ("h", "追問一：如果每個數出現 <code>k</code> 次呢？"),
   ("c", """【逐位數 mod k】（解法一的推廣）：

    for b in range(32):
        cnt = sum((x >> b) & 1 for x in nums)
        if cnt % k:
            res |= 1 << b

    完全一樣，只是把 3 換成 k ✔

    O(32n) 時間、O(1) 空間。

【狀態變數版】：
    需要 ⌈log₂ k⌉ 個變數來編碼 0..k-1 的狀態。

    k = 3 -> 2 個變數（本題）
    k = 5 -> 3 個變數
    k = 7 -> 3 個變數

    但轉移式會變得非常複雜，
    實務上直接用逐位數 mod k 就好。

【★ 注意 k 是偶數時】：

    如果 k 是偶數（例如 4），
    那「落單的數」和「出現 k 次的數」
    在 mod 2 下無法區分 —— 但 mod k 仍然可以 ✔

    不過這時 XOR 反而又可以用了（k 是偶數 -> 抵銷）。""",),
   ("h", "追問二：如果有【兩個】數各出現一次、其餘出現三次呢？"),
   "<strong>逐位數 mod 3 就不夠了</strong> —— "
   "<strong>因為兩個落單的數可能在同一位都是 1（餘數變成 2），"
   "也可能一個 1 一個 0（餘數 1）。</strong>",
   "<strong>可以先用「餘數不是 0 的那些位」把數字分成兩組"
   "（類似第 260 題的做法），但要更小心 —— 這是很少見的變形。</strong>",
   ("h", "追問三：解法二的兩行式是怎麼被發現的？"),
   ("c", """通常是這樣推的：

    1. 寫出狀態轉移表（我們上面驗證的那三格）
    2. 把它當成「兩個布林函數」：
           ones' = f(ones, twos, x)
           twos' = g(ones, twos, x)
    3. 用卡諾圖（Karnaugh map）化簡

    這是【數位邏輯設計】的標準流程 ——
    和設計一個實體電路是同一件事。

【所以這個技巧的來源其實是硬體設計】，
    不是「聰明的程式設計師靈光一閃」。

    知道這個背景，就不會覺得「想不到」是自己的問題。

    面試時如果被問到，
    誠實說「這個我是背下來的，推導要靠卡諾圖」
    比硬掰一個「直覺」好。""",),
   ("h", "追問四：為什麼題目要限制「32 位元整數」？"),
   "<strong>因為解法一的迴圈次數直接由位寬決定。</strong>",
   "<strong>如果沒有這個限制（例如可以是任意大的整數），"
   "複雜度就會變成 O(n · log(max))，而且無法預先決定迴圈次數。</strong>",
   "<strong>「限定數值範圍」常常是為了讓某個「看起來是常數」的因子真的是常數。</strong>",
 ],
 "related": [
   "<strong>第 136 題 Single Number</strong> —— 出現兩次，XOR 就夠",
   "<strong>第 260 題 Single Number III</strong> —— 兩個落單的數",
   "<strong>第 190 題 Reverse Bits</strong> —— 同樣要注意 Python 的位寬",
   "<strong>第 371 題 Sum of Two Integers</strong> —— 同樣的負數處理問題",
 ],
 "check": [
   "為什麼第 136 題的 XOR 在這題會失效？",
   "「逐位數 mod 3」為什麼是對的？出現三次的數為什麼不影響？",
   "在 Python 裡，解法一最後那行負數轉換為什麼必要？解法二為什麼不用？",
   "解法二的兩行更新為什麼不能交換順序？",
 ],
})
print("P137 written")

# ==================== 138. Copy List with Random Pointer ====================
class RNode(object):
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


_RN = {"Node": RNode}

S["p138_map"] = '''class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # 第一遍：只建節點，先不管指標
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # 第二遍：用對照表把 next 和 random 接起來
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next

        return old_to_new[head]'''

S["p138_onepass"] = '''class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        def get(node):
            """要用到某個節點的複本時，沒有就先建一個空殼"""
            if node is None:
                return None
            if node not in old_to_new:
                old_to_new[node] = Node(node.val)
            return old_to_new[node]

        cur = head
        while cur:
            copy = get(cur)
            copy.next = get(cur.next)
            copy.random = get(cur.random)
            cur = cur.next

        return get(head) if head else None'''

S["p138_weave"] = '''class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 第一步：把複本「交錯插入」原串列  A -> A' -> B -> B' -> ...
        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        # 第二步：接 random —— A' 就在 A 後面，所以 A'.random = A.random.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 第三步：把兩條串列拆開（要把原串列還原）
        new_head = head.next
        cur = head
        while cur:
            copy = cur.next
            cur.next = copy.next
            copy.next = copy.next.next if copy.next else None
            cur = cur.next

        return new_head'''


def _make_rlist(vals, rnd):
    """vals 是值，rnd[i] 是第 i 個節點的 random 指向的索引（None 代表 null）。"""
    nodes = [RNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, j in enumerate(rnd):
        nodes[i].random = nodes[j] if j is not None else None
    return nodes[0] if nodes else None


def _read_rlist(head):
    """讀回 (值序列, random 指向的索引序列)，並檢查沒有環。"""
    nodes, idx, cur = [], {}, head
    while cur:
        assert id(cur) not in idx, "cycle in next chain"
        idx[id(cur)] = len(nodes)
        nodes.append(cur)
        cur = cur.next
    vals = [n.val for n in nodes]
    rnd = [idx[id(n.random)] if n.random is not None else None for n in nodes]
    return vals, rnd


def _ids(head):
    out, cur = set(), head
    while cur:
        out.add(id(cur)); cur = cur.next
    return out


_p138 = [S.load(k, extra=_RN) for k in ("p138_map", "p138_onepass", "p138_weave")]

_CASES138 = [
    ([7, 13, 11, 10, 1], [None, 0, 4, 2, 0]),
    ([1, 2], [1, 1]),
    ([3, 3, 3], [None, 0, None]),
    ([], []),
    ([1], [None]),
    ([1], [0]),
]
for vals, rnd in _CASES138:
    want = _read_rlist(_make_rlist(vals, rnd)) if vals else ([], [])
    for sol in _p138:
        src = _make_rlist(vals, rnd)
        out = sol.copyRandomList(src)
        assert _read_rlist(out) == want, ("P138", vals, rnd, sol)
        # 原串列必須保持原狀（交錯法會暫時破壞它）
        assert _read_rlist(src) == want, ("P138 原串列被改壞", vals, rnd, sol)
        # 必須是深拷貝
        assert not (_ids(out) & _ids(src)), ("P138 淺拷貝", vals, rnd, sol)

for _ in range(3000):
    n = random.randrange(0, 9)
    vals = [random.randint(-20, 20) for _ in range(n)]
    rnd = [random.choice([None] + list(range(n))) for _ in range(n)]
    want = _read_rlist(_make_rlist(vals, rnd)) if n else ([], [])
    for sol in _p138:
        src = _make_rlist(vals, rnd)
        out = sol.copyRandomList(src)
        assert _read_rlist(out) == want, ("P138 random", vals, rnd, sol)
        assert _read_rlist(src) == want, ("P138 原串列被改壞", vals, rnd, sol)
        assert not (_ids(out) & _ids(src)), ("P138 淺拷貝", vals, rnd, sol)
print("P138 solutions OK")

_P138_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">O(1) 空間的技巧：把複本「交錯插入」原串列，就不需要對照表了。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">第一步：每個節點後面插一個自己的複本</text>
            <g font-size="12" text-anchor="middle">
              <rect x="50" y="70" width="52" height="28" fill="none" stroke="var(--text-muted)"/><text x="76" y="89" fill="var(--text-muted)">A</text>
              <rect x="122" y="70" width="52" height="28" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="148" y="89" fill="var(--gold)">A&#39;</text>
              <rect x="194" y="70" width="52" height="28" fill="none" stroke="var(--text-muted)"/><text x="220" y="89" fill="var(--text-muted)">B</text>
              <rect x="266" y="70" width="52" height="28" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="292" y="89" fill="var(--gold)">B&#39;</text>
              <rect x="338" y="70" width="52" height="28" fill="none" stroke="var(--text-muted)"/><text x="364" y="89" fill="var(--text-muted)">C</text>
              <rect x="410" y="70" width="52" height="28" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="436" y="89" fill="var(--gold)">C&#39;</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="102" y1="84" x2="118" y2="84"/><line x1="174" y1="84" x2="190" y2="84"/>
              <line x1="246" y1="84" x2="262" y2="84"/><line x1="318" y1="84" x2="334" y2="84"/>
              <line x1="390" y1="84" x2="406" y2="84"/>
            </g>
            <text x="20" y="128" fill="var(--accent)" font-size="12">現在每個複本都「剛好在它的本尊後面」—— 也就是 X&#39; = X.next</text>
            <line x1="20" y1="150" x2="620" y2="150" stroke="var(--border)"/>
            <text x="20" y="178" fill="var(--gold)" font-size="13">★ 第二步：接 random —— 這就是整個技巧的關鍵</text>
            <text x="40" y="208" fill="var(--text-muted)" font-size="12">假設 A.random 指向 C。那 A&#39;.random 應該指向 C&#39;。</text>
            <text x="40" y="236" fill="var(--gold)" font-size="12">而 C&#39; 就是 C.next，也就是 A.random.next ——</text>
            <text x="40" y="264" fill="var(--accent)" font-size="13">　　A.next.random = A.random.next</text>
            <text x="40" y="292" fill="var(--text-muted)" font-size="12">完全不需要對照表：「本尊在哪，複本就在它隔壁」這件事本身就是一張表。</text>
            <line x1="20" y1="316" x2="620" y2="316" stroke="var(--border)"/>
            <text x="20" y="344" fill="var(--gold)" font-size="13">第三步：把兩條串列拆開</text>
            <text x="40" y="372" fill="var(--text-muted)" font-size="12">A → B → C（原串列，必須還原）　　A&#39; → B&#39; → C&#39;（新串列，回傳這條）</text>
            <text x="20" y="404" fill="#ff8a65" font-size="12">★ 拆的時候要小心最後一個節點：copy.next 可能是 None，不能直接 .next。</text>
            <text x="20" y="430" fill="#ff8a65" font-size="12">★ 而且一定要把原串列【還原】—— 留著交錯狀態會讓呼叫者拿到壞掉的資料。</text>'''

emit({
 "num": 138, "slug": "copy-list-with-random-pointer",
 "en": [
   "A linked list of length <code>n</code> is given such that each node contains an additional "
   "random pointer, which could point to any node in the list, or <code>null</code>.",
   "Construct a <strong>deep copy</strong> of the list. The deep copy should consist of exactly "
   "<code>n</code> <strong>brand new</strong> nodes, where each new node has its value set to "
   "the value of its corresponding original node. Both the <code>next</code> and "
   "<code>random</code> pointer of the new nodes should point to new nodes in the copied list "
   "such that the pointers in the original list and copied list represent the same list state. "
   "<strong>None of the pointers in the new list should point to nodes in the original list.</strong>",
 ],
 "zh": [
   "給你一條長度為 <code>n</code> 的鏈結串列，每個節點除了 <code>next</code> 之外，"
   "還多了一個 <strong><code>random</code> 指標</strong>，"
   "它可以指向串列裡的<strong>任何一個節點</strong>，也可以是 <code>None</code>。",
   "請做出這條串列的<strong>深拷貝</strong>：",
   ("ul", [
     "新串列必須是 <code>n</code> 個<strong>全新的節點</strong>。",
     "新節點的 <code>next</code> 和 <code>random</code> "
     "都必須指向<strong>新串列裡的節點</strong>。",
     "<strong>新串列裡不能有任何一個指標指向原串列的節點。</strong>",
   ]),
 ],
 "pre": [
   ("note", "★ 難在哪裡？<code>random</code> 可能指向「還沒複製的節點」", [
     ("c", """如果只有 next，複製很簡單：從頭走到尾，一路建新節點。

    但 random 可以指向【任何地方】——
    包括「後面還沒走到的節點」，甚至「自己」。

    A -> B -> C
    A.random = C        ← 複製 A 時，C' 還不存在！

【兩條路解決這個問題】：

    (a) 【兩遍掃描 + 對照表】（解法一）
        第一遍：只建節點（不管指標）
        第二遍：所有節點都存在了，再把指標接起來 ✔

        這就是第 133 題（複製圖）的「先建殼、再填內容」。

    (b) 【交錯插入】（解法三）
        把 A' 插在 A 後面 -> A' 永遠是 A.next

        那麼「A.random 的複本」就是 A.random.next ✔

        不需要對照表 -> O(1) 額外空間。

【(b) 是一個非常漂亮的技巧】——
    它用「位置關係」取代了「雜湊表」。

    但它只在【串列】上可行，圖上做不到
    （圖沒有「插在旁邊」這個概念）。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]

        每一項是 [val, random_index]：
            節點 0：值 7，  random 指向 null
            節點 1：值 13， random 指向節點 0
            節點 2：值 11， random 指向節點 4
            節點 3：值 10， random 指向節點 2
            節點 4：值 1，  random 指向節點 0

  輸出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
        （結構完全相同，但全部是新節點）

範例 2
  輸入：head = [[1,1],[2,1]]
  輸出：[[1,1],[2,1]]
        兩個節點的 random 都指向節點 1。

範例 3
  輸入：head = []
  輸出：[]""",
 "constraints": [
   "0 ≤ <code>n</code> ≤ 1000",
   "−10⁴ ≤ <code>Node.val</code> ≤ 10⁴",
   "<code>Node.random</code> 是 <code>null</code> 或串列中的某個節點",
 ],
 "idea": [
   ("fig", _P138_FIG, "0 0 640 452"),
   ("c", """【方法 A：對照表（兩遍或一遍）】

    old_to_new = {原節點: 新節點}

    第一遍：for 每個節點: old_to_new[cur] = Node(cur.val)
    第二遍：for 每個節點:
                new.next   = old_to_new.get(cur.next)
                new.random = old_to_new.get(cur.random)

    用 .get() 而不是 [] —— 因為 next/random 可能是 None，
    而 None 不在表裡。get(None) 回傳 None ✔

    O(n) 時間、O(n) 空間。

【方法 B：交錯插入（O(1) 空間）】

    三步：

    1. 交錯插入
        A -> A' -> B -> B' -> C -> C'

        此時 X' 永遠等於 X.next

    2. 接 random
        A'.random = A.random.next

        因為 A' = A.next，寫成：
            cur.next.random = cur.random.next

        ★ 要先檢查 cur.random 不是 None

    3. 拆開兩條串列
        把 next 指標還原成
            A -> B -> C     （原串列）
            A' -> B' -> C'  （新串列）

        ★ 一定要把原串列還原，否則呼叫者拿到的是壞掉的資料。

    O(n) 時間、O(1) 額外空間 ✔

【第 2 步是整個技巧的精髓】：

    「複本在本尊隔壁」這個【位置不變量】
    本身就扮演了對照表的角色。

    這是「用結構取代資料結構」的漂亮例子。"""),
 ],
 "approaches": [
   ap("解法一", "對照表 + 兩遍掃描（標準答案）", [
     ("c", S["p138_map"]),
     "<strong>十五行，O(n) 時間、O(n) 空間。</strong>"
     "<strong>最好懂、最不容易錯，面試時先寫這個。</strong>",
     ("h", "<code>.get()</code> 而不是 <code>[]</code>"),
     ("c", """old_to_new.get(cur.next)

    cur.next 可能是 None（最後一個節點），
    而 None 不是表裡的 key。

    用 [] 會 KeyError，用 .get() 回傳 None ✔

    【而 None 正是我們要的值】——
    新節點的 next 也該是 None。

【小技巧】：也可以預先放一筆 old_to_new[None] = None，
    這樣就能一律用 []：

        old_to_new = {None: None}
        ...
        old_to_new[cur].next = old_to_new[cur.next]

    這是「用哨兵值消除特例」的另一個例子
    （和 dummy head 同一個精神）。""",),
     ("h", "為什麼要分成兩遍？"),
     "<strong>因為第一遍結束時，所有節點才都存在</strong> —— "
     "<strong>這樣第二遍接 <code>random</code> 時，目標一定找得到。</strong>",
     "<strong>解法二用「需要時才建」的方式，可以一遍完成。</strong>",
   ], "O(n)", "O(n)", "兩遍掃描", "對照表", optimal=True),

   ap("解法二", "對照表 + 一遍掃描（<code>get</code> 時才建）", [
     ("c", S["p138_onepass"]),
     ("c", """核心是那個 get() 函式：

    def get(node):
        if node is None: return None
        if node not in old_to_new:
            old_to_new[node] = Node(node.val)   ← 需要時才建
        return old_to_new[node]

    這樣就不用「先建完所有節點」——
    要用到誰，就當場確保它存在。

【和第 133 題（複製圖）的 DFS 版是同一個想法】：
    「先登記一個空殼，之後再填它的內容」。

    差別是這題不用遞迴（串列是線性的）。

【複雜度和解法一完全相同】，
    只是掃描次數從 2 變成 1 ——
    常數上略快，但漸進一樣。

【哪個比較好？】

    解法一：結構更清楚（「建節點」和「接指標」分開）
    解法二：少一遍掃描，而且 get() 的封裝很乾淨

    兩個都可以。我個人偏好解法一，
    因為「分階段」的程式碼更容易在出錯時定位問題。""",),
   ], "O(n)", "O(n)", "一遍掃描", "對照表"),

   ap("解法三", "交錯插入（O(1) 額外空間）", [
     ("c", S["p138_weave"]),
     ("h", "★ 第三步的拆開最容易寫錯"),
     ("c", """new_head = head.next            ← 先存起來！（等一下 head.next 會被改掉）

cur = head
while cur:
    copy = cur.next
    cur.next = copy.next                    還原原串列
    copy.next = copy.next.next if copy.next else None    接新串列
    cur = cur.next

【為什麼 copy.next 要判 None？】

    最後一對是 ... -> Z -> Z' -> None

    處理 Z 時：
        copy = Z'
        cur.next = copy.next = None          ✔ Z 變成最後一個
        copy.next = copy.next.next           ✘ None.next -> AttributeError

    所以要寫成：
        copy.next = copy.next.next if copy.next else None

【另一種寫法（比較不容易錯）】：

    cur = head
    while cur:
        copy = cur.next
        nxt = copy.next                # 原串列的下一個
        cur.next = nxt
        copy.next = nxt.next if nxt else None
        cur = nxt

    先把 nxt 存起來，讀起來清楚很多。

【★ 一定要還原原串列】

    題目雖然沒明說，但「修改呼叫者傳進來的資料」
    是嚴重的副作用 ——
    LeetCode 的判題器也會檢查原串列。

    本文的測試就有這一條：
        assert _read_rlist(src) == want   # 原串列必須保持原狀"""),
     ("h", "第二步為什麼要檢查 <code>cur.random</code>？"),
     ("c", """if cur.random:
    cur.next.random = cur.random.next

    如果 cur.random 是 None，
    cur.random.next 會 AttributeError。

    而 cur.next.random 本來就是 None（新節點的預設值），
    所以什麼都不用做 ✔

【也可以寫成】：
    cur.next.random = cur.random.next if cur.random else None

    明確一點，但效果相同。""",),
     "<strong>O(n) 時間、O(1) 額外空間</strong>（不算輸出的 n 個新節點）。"
     "<strong>這是本題「進階」想要的答案。</strong>",
     "<strong>但它有三個獨立的迴圈、而且每一個都有邊界陷阱</strong> —— "
     "<strong>面試時先寫解法一，被問到空間再寫這個。</strong>",
   ], "O(n)", "O(1)", "三趟掃描", "不用對照表"),
 ],
 "compare": (["解法", "時間", "額外空間", "會動到原串列嗎", "好寫嗎"],
   [["一、對照表 + 兩遍", "O(n)", "O(n)", "✘", "★★★"],
    ["二、對照表 + 一遍", "O(n)", "O(n)", "✘", "★★★"],
    ["三、交錯插入", "O(n)", "O(1)", "✔ 但會還原", "★☆☆"]]),
 "edges": [
   "<strong>空串列</strong> → <code>None</code>。<strong>三種解法都要擋。</strong>",
   "<strong>單一節點、<code>random</code> 是 <code>None</code></strong> → 一個新節點。",
   "<strong>單一節點、<code>random</code> 指向自己</strong> <code>[[1,0]]</code> → "
   "<strong>新節點的 <code>random</code> 要指向它自己（新的那個）。</strong>",
   "<strong>所有 <code>random</code> 都指向同一個節點</strong> → 都要指向新串列裡的那一個。",
   "<strong><code>random</code> 指向前面的節點</strong> → 對照表法沒問題。",
   "<strong><code>random</code> 指向後面還沒複製的節點</strong> → "
   "<strong>「邊走邊建、邊接指標」的天真做法會在這裡掛掉。</strong>",
   "<strong>用 <code>[]</code> 而不是 <code>.get()</code></strong> → "
   "<code>next</code> 是 <code>None</code> 時 <code>KeyError</code>。",
   "<strong>交錯法沒有還原原串列</strong> → 呼叫者拿到交錯的壞資料。",
   "<strong>交錯法拆開時沒判最後一個的 <code>None</code></strong> → <code>AttributeError</code>。",
 ],
 "follow": [
   ("h", "追問一：這和第 133 題（複製圖）有什麼關係？"),
   ("c", """對照表法完全相同 —— 都是「先建殼、登記、再填內容」。

    差別：
        133：圖，要 DFS/BFS 走訪（有環）
        138：串列，線性走訪就好

    而【交錯插入法只有串列能用】：

        圖沒有「插在旁邊」這個概念 ——
        你無法把 A' 放在「A 的隔壁」讓所有指向 A 的邊
        都能 O(1) 找到 A'。

    串列可以，是因為它有 next 這個「唯一的下一個」。

【一般原則】：
    結構越「規則」，能用的技巧越多。

    陣列 > 串列 > 樹 > DAG > 一般圖
    （能用的原地技巧依序遞減）""",),
   ("h", "追問二：如果節點值可能重複，用 <code>val</code> 當 key 行嗎？"),
   "<strong>不行</strong> —— 兩個 <code>val</code> 相同的不同節點會被當成同一個。",
   "<strong>必須用「節點物件」當 key</strong>（Python 的物件預設可雜湊，用 <code>id</code>）。",
   "<strong>這和第 133 題的注意事項一模一樣。</strong>"
   "<strong>「用什麼當 key」是雜湊表題最容易被忽略的設計決定。</strong>",
   ("h", "追問三：交錯插入法的三個迴圈能不能合併？"),
   ("c", """第一步和第二步【不能合併】：

    接 random 時需要「所有複本都已經插好了」——
    否則 cur.random.next 可能還是原串列的節點 ✘

    例如 A.random = C，但 C' 還沒插進去時，
    C.next 還是 D 而不是 C' ✘

第二步和第三步【可以合併】（小心一點的話），
    但那樣程式碼會更難讀，而且更容易錯。

【三個迴圈都是 O(n)，合併起來還是 O(n)】——
    省的只有常數，不值得用正確性去換。

    【「能不能合併迴圈」的判斷標準：
      後面的步驟有沒有依賴前面步驟的【全域完成狀態】。】""",),
   ("h", "追問四：如果 <code>random</code> 可以指向串列外的節點呢？"),
   "<strong>那對照表法會在 <code>.get()</code> 時拿到 <code>None</code></strong> —— "
   "<strong>等於把那個指標丟掉了。</strong>",
   "<strong>交錯法會更糟</strong>：<code>cur.random.next</code> 會指向串列外某個節點的 "
   "<code>next</code>，<strong>產生完全錯誤的連結。</strong>",
   "<strong>題目保證 <code>random</code> 只指向串列內的節點或 <code>null</code></strong>，"
   "<strong>交錯法的正確性完全依賴這個前提。</strong>",
 ],
 "related": [
   "<strong>第 133 題 Clone Graph</strong> —— 同樣的「先建殼再填」",
   "<strong>第 2 題 Add Two Numbers</strong> —— 串列上的基本操作",
   "<strong>第 206 題 Reverse Linked List</strong> —— 「先存起來再改指標」",
   "<strong>第 143 題 Reorder List</strong> —— 另一個多步驟的串列改造",
 ],
 "check": [
   "為什麼「邊走邊建、邊接 <code>random</code>」的天真做法會失敗？",
   "對照表法為什麼要用 <code>.get()</code> 而不是 <code>[]</code>？",
   "交錯插入法裡，<code>A'.random = A.random.next</code> 為什麼成立？",
   "為什麼交錯法一定要把原串列還原？拆開時最容易在哪裡出錯？",
 ],
})
print("P138 written")

# ==================== 139. Word Break ====================
S["p139_dp"] = '''class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        # dp[i] = s 的前 i 個字能不能被完全拆開
        dp = [False] * (n + 1)
        dp[0] = True                        # 空字串永遠可以

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break                   # 找到一種就夠了

        return dp[n]'''

S["p139_len"] = '''class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        lens = sorted({len(w) for w in words})   # 只試字典裡真正有的長度
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for L in lens:
                if L > i:
                    break                   # 更長的不用試了
                if dp[i - L] and s[i - L:i] in words:
                    dp[i] = True
                    break

        return dp[n]'''

S["p139_memo"] = '''from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)

        @lru_cache(maxsize=None)
        def go(start: int) -> bool:
            """s[start:] 能不能被拆開"""
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in words and go(end):
                    return True
            return False

        ans = go(0)
        go.cache_clear()
        return ans'''

S["p139_greedy"] = '''class Solution:
    # 【這是錯的，不要抄】：貪心地「每次切最長的那一段」
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        i = 0
        while i < len(s):
            for j in range(len(s), i, -1):      # 從最長開始試
                if s[i:j] in words:
                    i = j
                    break
            else:
                return False
        return True'''


def _p139_ref(s, wd):
    """獨立參考解：樸素的記憶化搜尋。"""
    words = set(wd)
    n = len(s)
    memo = {}
    def go(i):
        if i == n:
            return True
        if i in memo:
            return memo[i]
        memo[i] = any(s[i:j] in words and go(j) for j in range(i + 1, n + 1))
        return memo[i]
    return go(0)


_p139 = [S.load(k) for k in ("p139_dp", "p139_len", "p139_memo")]
_p139_bad = S.load("p139_greedy")

for s, wd, want in [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ("a", ["a"], True),
    ("ab", ["a"], False),
    ("aaaaaaa", ["aaa", "aaaa"], True),
]:
    assert _p139_ref(s, wd) is want, ("P139 ref", s, wd)
    for sol in _p139:
        assert sol.wordBreak(s, list(wd)) is want, ("P139", s, wd, sol)

# 貪心「每次切最長」確實會答錯（這就是題解裡用的那個反例）
assert _p139_bad.wordBreak("aaab", ["aa", "aaa", "ab"]) is False
assert _p139_ref("aaab", ["aa", "aaa", "ab"]) is True

for _ in range(3000):
    s = "".join(random.choice("ab") for _ in range(random.randrange(1, 13)))
    pool = ["a", "b", "aa", "ab", "ba", "bb", "aaa", "aba", "bab"]
    wd = random.sample(pool, random.randrange(1, 6))
    want = _p139_ref(s, wd)
    for sol in _p139:
        assert sol.wordBreak(s, list(wd)) is want, ("P139 random", s, wd, want, sol)
print("P139 solutions OK")

_P139_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">dp[i] = 「s 的前 i 個字能不能完全拆成字典裡的單字」。每一格問：最後一段從哪裡開始？</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">s = &quot;leetcode&quot;　　字典 = {leet, code}</text>
            <g font-size="12" text-anchor="middle">
              <text x="60" y="84" fill="var(--text-muted)" text-anchor="start">i：</text>
              <text x="120" y="84" fill="var(--text-muted)">0</text><text x="172" y="84" fill="var(--text-muted)">1</text><text x="224" y="84" fill="var(--text-muted)">2</text><text x="276" y="84" fill="var(--text-muted)">3</text><text x="328" y="84" fill="var(--text-muted)">4</text><text x="380" y="84" fill="var(--text-muted)">5</text><text x="432" y="84" fill="var(--text-muted)">6</text><text x="484" y="84" fill="var(--text-muted)">7</text><text x="536" y="84" fill="var(--text-muted)">8</text>
              <text x="60" y="114" fill="var(--text-muted)" text-anchor="start">s：</text>
              <text x="146" y="114" fill="var(--text-muted)">l</text><text x="198" y="114" fill="var(--text-muted)">e</text><text x="250" y="114" fill="var(--text-muted)">e</text><text x="302" y="114" fill="var(--text-muted)">t</text><text x="354" y="114" fill="var(--text-muted)">c</text><text x="406" y="114" fill="var(--text-muted)">o</text><text x="458" y="114" fill="var(--text-muted)">d</text><text x="510" y="114" fill="var(--text-muted)">e</text>
              <text x="60" y="148" fill="var(--gold)" text-anchor="start">dp：</text>
              <text x="120" y="148" fill="var(--accent)">T</text><text x="172" y="148" fill="var(--text-muted)">F</text><text x="224" y="148" fill="var(--text-muted)">F</text><text x="276" y="148" fill="var(--text-muted)">F</text><text x="328" y="148" fill="var(--accent)">T</text><text x="380" y="148" fill="var(--text-muted)">F</text><text x="432" y="148" fill="var(--text-muted)">F</text><text x="484" y="148" fill="var(--text-muted)">F</text><text x="536" y="148" fill="var(--gold)" font-size="16">T</text>
            </g>
            <text x="120" y="176" fill="var(--accent)" font-size="11" text-anchor="middle">空字串</text>
            <text x="328" y="176" fill="var(--accent)" font-size="11" text-anchor="middle">&quot;leet&quot; ✔</text>
            <text x="536" y="176" fill="var(--gold)" font-size="11" text-anchor="middle">答案</text>
            <path d="M 120 158 Q 224 200 328 158" fill="none" stroke="var(--accent)" stroke-width="1.5" stroke-dasharray="4 3"/>
            <path d="M 328 158 Q 432 200 536 158" fill="none" stroke="var(--gold)" stroke-width="2" stroke-dasharray="4 3"/>
            <text x="224" y="214" fill="var(--accent)" font-size="11" text-anchor="middle">dp[0] and &quot;leet&quot; 在字典</text>
            <text x="432" y="214" fill="var(--gold)" font-size="11" text-anchor="middle">dp[4] and &quot;code&quot; 在字典</text>
            <line x1="20" y1="240" x2="620" y2="240" stroke="var(--border)"/>
            <text x="20" y="268" fill="#ff8a65" font-size="13">★ 為什麼貪心（每次切最長的）一定會錯？</text>
            <text x="20" y="296" fill="var(--gold)" font-size="12">s = &quot;aaab&quot;　　字典 = {aa, aaa, ab}</text>
            <text x="40" y="324" fill="#ff8a65" font-size="12">貪心（切最長）：先切 &quot;aaa&quot; → 剩下 &quot;b&quot; 不在字典 → 卡死，答 False ✘</text>
            <text x="40" y="352" fill="var(--accent)" font-size="12">正解：切 &quot;aa&quot; + &quot;ab&quot; → True ✔</text>
            <text x="20" y="384" fill="var(--text-muted)" font-size="12">貪心看不到「現在讓一步（少切一個字元），後面才走得通」。</text>
            <text x="20" y="414" fill="var(--text-muted)" font-size="12">切最短也一樣會錯：s = &quot;aab&quot;、字典 = {a, aab} → 切最短得到 a + a + &quot;b&quot; ✘，</text>
            <text x="20" y="438" fill="#ff8a65" font-size="12">而正解是整個 &quot;aab&quot; ✔。兩個方向的貪心都錯 —— 這題沒有「局部最優」可言。</text>'''

emit({
 "num": 139, "slug": "word-break",
 "en": [
   "Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, return "
   "<code>true</code> if <code>s</code> can be segmented into a space-separated sequence of one "
   "or more dictionary words.",
   "<strong>Note</strong> that the same word in the dictionary may be reused multiple times in "
   "the segmentation.",
 ],
 "zh": [
   "給你一個字串 <code>s</code> 和一個單字字典 <code>wordDict</code>，"
   "判斷 <code>s</code> 能不能被<strong>完全拆成</strong>字典裡的單字"
   "（中間用空格隔開）。",
   "<strong>注意：字典裡的單字可以重複使用。</strong>",
 ],
 "pre": [
   ("note", "★ 貪心一定會錯", [
     ("c", S["p139_greedy"]),
     ("c", """「每次切最長的那一段」看起來很合理，但是錯的。

反例：s = "aaab"，字典 = {"aa", "aaa", "ab"}

    貪心：
        從位置 0 開始，最長能切 "aaa" -> 跳到位置 3
        剩下 "b" 不在字典裡 -> 卡死 -> False ✘

    正解：
        切 "aa" + "ab" ✔ -> True

【為什麼貪心會錯？】

    「現在切長一點」會限制「後面能怎麼切」——
    決定之間【互相干擾】。

    （對照第 122 題：那裡的決定互不干擾，所以貪心對。）

【切最短的呢？】也錯。

    s = "aaa"，字典 = {"a", "aaa"}
        切最短：a + a + a ✔ 剛好對

    s = "aab"，字典 = {"a", "aab"}
        切最短：a + a + ? 剩下 "b" ✘
        正解：  "aab" ✔

    【兩個方向的貪心都會錯 ——
      因為這題根本沒有「局部最優」可言。】

    所以必須考慮【所有切法】-> DP 或記憶化搜尋。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "leetcode", wordDict = ["leet","code"]
  輸出：true
  說明："leetcode" 可以拆成 "leet code"。

範例 2
  輸入：s = "applepenapple", wordDict = ["apple","pen"]
  輸出：true
  說明：拆成 "apple pen apple"。
        【注意 "apple" 用了兩次 —— 字典裡的單字可以重複使用。】

範例 3
  輸入：s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
  輸出：false
  說明：
        "cats" + "and" + "og"? -> "og" 不在字典
        "cat" + "sand" + "og"? -> 同上
        怎麼切都會剩下 "og"。""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 300",
   "1 ≤ <code>wordDict.length</code> ≤ 1000",
   "1 ≤ <code>wordDict[i].length</code> ≤ 20",
   "<code>s</code> 和 <code>wordDict[i]</code> 只包含小寫英文字母",
   "<code>wordDict</code> 裡的單字<strong>互不相同</strong>",
 ],
 "idea": [
   ("fig", _P139_FIG, "0 0 640 456"),
   ("c", """【狀態】
    dp[i] = s 的前 i 個字能不能被完全拆開

【轉移】
    dp[i] = OR over j (0 <= j < i) of (dp[j] and s[j:i] in words)

    意思是：「最後一段是 s[j:i]，而前面的 s[0:j] 也能拆開」。

【邊界】
    dp[0] = True     空字串永遠可以拆（切成 0 個單字）

    【設成 False 的話整個 dp 都是 False】——
    和第 115、118、95 題的 base case 是同一類。

【答案】dp[n]

【複雜度】
    兩層迴圈 O(n²)，每次切片 + 查集合 O(k)
    -> O(n² · k)，其中 k 是平均單字長度

    n = 300 -> 9 萬次，完全沒問題。

【★ 優化：只試「字典裡真正有的長度」】（解法二）

    題目說單字長度 <= 20。
    所以 j 不用從 0 掃到 i-1，
    只要試 i - 20 到 i - 1 這 20 個位置就夠了。

    更好的做法：先收集字典裡所有出現過的長度
    （可能只有兩三種），只試那些。

    -> O(n · |不同長度|) 而不是 O(n²)

    這在 n 很大時差很多。"""),
 ],
 "approaches": [
   ap("解法一", "一維 DP（標準答案）", [
     ("c", S["p139_dp"]),
     "<strong>十行。O(n²·k) 時間、O(n) 空間。</strong>",
     ("h", "<code>break</code> 的意義"),
     ("c", """if dp[j] and s[j:i] in words:
    dp[i] = True
    break               ← 找到一種切法就夠了

    因為我們只問「能不能」，不問「有幾種」。

    第 140 題（要列出所有切法）就不能 break ——
    那裡要把所有可能的 j 都收集起來。

【如果改成「有幾種切法」】：

    dp[i] += dp[j]      （不 break，全部累加）

    【布林 -> 計數的萬用轉換：
      or 變 +，and 變 ×（或者條件過濾）。】

    和第 97、115 題的追問是同一個模式。"""),
     ("h", "為什麼要先 <code>set(wordDict)</code>？"),
     "<strong><code>list</code> 的 <code>in</code> 是 O(m)，<code>set</code> 的是 O(1)。</strong>",
     "<strong>字典有 1000 個單字，不轉 <code>set</code> 的話每次查詢慢 1000 倍。</strong>"
     "<strong>「要反覆查詢成員關係就先轉 set」是基本反射。</strong>",
     ("h", "<code>dp[0] = True</code> 的意義"),
     "<strong>「空字串可以被拆成 0 個單字」</strong> —— "
     "和「空集合的子集有 1 個」「0! = 1」是同一類約定。",
     "<strong>設成 <code>False</code> 的話 <code>dp[1]</code> 就永遠是 <code>False</code>，整串都垮。</strong>",
   ], "O(n² · k)", "O(n)", "兩層迴圈 + 切片", "dp 陣列", optimal=True),

   ap("解法二", "只試字典裡有的長度（實測快很多）", [
     ("c", S["p139_len"]),
     ("c", """lens = sorted({len(w) for w in words})

    例如字典是 {"apple", "pen"}，
    lens = [3, 5] —— 只有兩種長度。

    那 dp[i] 就只要檢查兩個 j（i-3 和 i-5），
    而不是 i 個。

    -> O(n · |lens|) 而不是 O(n²)

    |lens| <= 20（因為單字長度 <= 20），
    而且實務上通常只有幾種。

【for L in lens: if L > i: break】

    lens 是排序過的，
    所以一旦 L 超過 i 就可以停（後面只會更長）。

【什麼時候這個優化才重要？】

    n = 300 時兩者都很快（9 萬 vs 6000）。

    但如果 n = 10^5（有些變形題會這樣），
    O(n²) = 10^10 ✘ 而 O(20n) = 2×10^6 ✔

    【「字典單字有長度上限」這個條件，
      就是在暗示這個優化。讀限制條件時要注意。】""",),
     "<strong>複雜度 O(n · |lens| · k)。</strong>"
     "<strong>面試時先寫解法一，然後說「可以只試字典裡出現過的長度」。</strong>",
   ], "O(n · |lens| · k)", "O(n)", "只試有效長度", "dp 陣列 + 長度集合"),

   ap("解法三", "記憶化遞迴（自頂向下）", [
     ("c", S["p139_memo"]),
     ("c", """go(start) = 「s[start:] 能不能拆開」

    和 dp 版是同一個狀態，只是方向相反：
        dp 版：從前往後填
        記憶化：從 0 往後遞迴

【為什麼一定要記憶化？】

    不加 @lru_cache 的話：

        s = "aaaa...a"（n 個 a），字典 = {"a", "aa"}

        go(0) 會展開成指數級的遞迴樹 -> O(2^n) ✘

    加了之後，go(start) 只有 n 個不同的參數
    -> 最多算 n 次 -> O(n²) ✔

    【這是「指數 -> 多項式」最經典的一步。】

【遞迴深度】：最壞 O(n) = 300，安全 ✔

【go.cache_clear()】：
    lru_cache 掛在內層函式上，每次呼叫 wordBreak
    都是新的快取，所以其實不清也沒事。
    清掉是釋放記憶體的好習慣。""",),
     "<strong>複雜度和解法一相同。</strong>"
     "<strong>如果你比較習慣「從暴力解加記憶化」的思路，這個版本最自然。</strong>",
   ], "O(n² · k)", "O(n)", "每個狀態算一次", "快取 + 遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、一維 DP", "O(n²·k)", "O(n)", "10", "標準答案"],
    ["二、只試有效長度", "O(n·|lens|·k)", "O(n)", "12", "n 很大時關鍵"],
    ["三、記憶化遞迴", "O(n²·k)", "O(n)", "14", "從暴力解最好改"]]),
 "edges": [
   "<strong><code>s = \"a\", wordDict = [\"a\"]</code></strong> → <code>True</code>。",
   "<strong><code>s = \"ab\", wordDict = [\"a\"]</code></strong> → <code>False</code>。",
   "<strong>單字要重複使用</strong> <code>\"applepenapple\"</code> → <code>True</code>。",
   "<strong>貪心會錯的測資</strong> <code>s=\"aaab\", dict={\"aa\",\"aaa\",\"ab\"}</code> → "
   "<strong><code>True</code>，但「每次切最長」會答 False。</strong>",
   "<strong><code>dp[0]</code> 設成 <code>False</code></strong> → 整串都是 <code>False</code>。",
   "<strong>沒有把 <code>wordDict</code> 轉成 <code>set</code></strong> → 查詢慢 1000 倍。",
   "<strong>字典裡有 <code>s</code> 沒有的字元</strong> → 沒關係，永遠匹配不到。",
   "<strong>n = 300、字典 1000 個單字</strong> → O(n²) 是 9 萬次，輕鬆。",
 ],
 "follow": [
   ("h", "追問一：如果要列出「所有的拆法」呢？"),
   "<strong>第 140 題（Word Break II）</strong> —— 那是 Hard。",
   "<strong>關鍵是先用本題的 DP 做「可行性剪枝」</strong>："
   "<strong>先算出 <code>dp</code>，再回溯時只走 <code>dp[j]</code> 為 <code>True</code> 的分支。</strong>",
   "<strong>沒有剪枝的話，<code>\"aaaa...a\"</code> 這種輸入會指數爆炸。</strong>",
   ("h", "追問二：如果字典非常大（例如 10⁶ 個單字）呢？"),
   ("c", """用【字典樹（Trie）】取代 set：

    dp[i] = True 時，從位置 i 開始沿著 Trie 往下走，
    每走到一個「單字結尾」就標記 dp[那個位置] = True

    好處：
        ✔ 不用做字串切片（s[j:i] 會複製 O(k) 的資料）
        ✔ 一次走訪就能找出「從 i 開始的所有匹配」
        ✔ 空間是 O(字典總字元數) 而不是 O(字典總大小 × 平均長度)

    複雜度變成 O(n · maxlen)。

【Trie 的核心價值是「共用前綴」】——
    apple、app、apply 三個單字共用 "app" 這一段。

    字典越大、前綴重複越多，Trie 的優勢越明顯。

    第 208、211、212 題會把 Trie 講透。""",),
   ("h", "追問三：布林 DP 改成計數 DP 要怎麼寫？"),
   ("c", """dp = [0] * (n + 1)
dp[0] = 1                       ← 從 True 換成 1

for i in range(1, n + 1):
    for j in range(i):
        if s[j:i] in words:
            dp[i] += dp[j]      ← 從 or 換成 +，而且不 break

return dp[n]

【布林 / 計數 / 最優 三種 DP 的對照】：

    問「能不能」 -> dp 存 bool，用 or，可以 break
    問「有幾種」 -> dp 存 int， 用 +， 不能 break
    問「最少幾段」-> dp 存 int， 用 min，不能 break

    【同一個轉移結構，換一個「合併運算」就是另一題。】

    這個模式在第 91、97、115、131、132、139 題
    反覆出現。""",),
   ("h", "追問四：為什麼這題不能像第 122 題那樣貪心？"),
   "<strong>因為「這一段切多長」會限制「下一段能怎麼切」</strong> —— "
   "<strong>決定之間互相干擾。</strong>",
   "<strong>判斷能不能貪心的問題永遠是：</strong>"
   "<strong>「我現在做的選擇，會不會讓未來的選擇變少？」</strong>",
   "<strong>會 → 通常要 DP；不會 → 可能可以貪心（但仍然要證明）。</strong>",
 ],
 "related": [
   "<strong>第 140 題 Word Break II</strong> —— 列出所有拆法",
   "<strong>第 131/132 題 分割回文串 I/II</strong> —— 同一個「切字串」骨架",
   "<strong>第 91 題 Decode Ways</strong> —— 同上，改成計數",
   "<strong>第 208 題 Implement Trie</strong> —— 字典很大時的優化",
   "<strong>第 472 題 Concatenated Words</strong> —— 本題的進階版",
 ],
 "check": [
   "「每次切最長」的貪心為什麼會錯？請舉出反例。",
   "<code>dp[0] = True</code> 的意義是什麼？設成 <code>False</code> 會怎樣？",
   "<code>break</code> 在這題可以用，在第 140 題為什麼不行？",
   "如果改成「有幾種拆法」，轉移式要怎麼改？",
 ],
})
print("P139 written")

# ==================== 140. Word Break II ====================
S["p140"] = '''from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        n = len(s)

        # ★ 先用第 139 題的 DP 做可行性剪枝：ok[i] = s[i:] 能不能拆開
        ok = [False] * (n + 1)
        ok[n] = True
        for i in range(n - 1, -1, -1):
            ok[i] = any(s[i:j] in words and ok[j] for j in range(i + 1, n + 1))

        if not ok[0]:
            return []

        res, path = [], []

        def back(start: int):
            if start == n:
                res.append(" ".join(path))
                return
            for end in range(start + 1, n + 1):
                if s[start:end] in words and ok[end]:   # ★ 只走「後面走得通」的分支
                    path.append(s[start:end])
                    back(end)
                    path.pop()

        back(0)
        return res'''

S["p140_memo"] = '''from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        @lru_cache(maxsize=None)
        def go(start: int):
            """s[start:] 的所有拆法（每一種是一個字串）"""
            if start == len(s):
                return [""]                 # 空字串：一種拆法（什麼都不接）
            out = []
            for end in range(start + 1, len(s) + 1):
                w = s[start:end]
                if w in words:
                    for rest in go(end):
                        out.append(w if rest == "" else w + " " + rest)
            return out

        ans = list(go(0))
        go.cache_clear()
        return ans'''

S["p140_nopruning"] = '''class Solution:
    # 【會 TLE 的版本】：沒有剪枝、也沒有記憶化的純回溯
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        n = len(s)
        res, path = [], []

        def back(start):
            if start == n:
                res.append(" ".join(path))
                return
            for end in range(start + 1, n + 1):
                if s[start:end] in words:
                    path.append(s[start:end])
                    back(end)
                    path.pop()

        back(0)
        return res'''


def _p140_ref(s, wd):
    """獨立參考解：枚舉所有切點組合。"""
    words = set(wd)
    n = len(s)
    out = []
    for mask in range(1 << max(0, n - 1)):
        parts, prev = [], 0
        for i in range(n - 1):
            if mask >> i & 1:
                parts.append(s[prev:i + 1]); prev = i + 1
        parts.append(s[prev:])
        if all(p in words for p in parts):
            out.append(" ".join(parts))
    return out


_p140 = [S.load(k) for k in ("p140", "p140_memo", "p140_nopruning")]

for s, wd, want in [
    ("catsanddog", ["cat", "cats", "and", "sand", "dog"],
     ["cats and dog", "cat sand dog"]),
    ("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"],
     ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
    ("a", ["a"], ["a"]),
]:
    assert sorted(_p140_ref(s, wd)) == sorted(want), ("P140 ref", s, wd, _p140_ref(s, wd))
    for sol in _p140:
        assert sorted(sol.wordBreak(s, list(wd))) == sorted(want), ("P140", s, wd, sol)

for _ in range(1500):
    s = "".join(random.choice("ab") for _ in range(random.randrange(1, 11)))
    pool = ["a", "b", "aa", "ab", "ba", "bb", "aaa", "aba"]
    wd = random.sample(pool, random.randrange(1, 5))
    want = sorted(_p140_ref(s, wd))
    for sol in _p140:
        assert sorted(sol.wordBreak(s, list(wd))) == want, ("P140 random", s, wd, want, sol)
print("P140 solutions OK")

emit({
 "num": 140, "slug": "word-break-ii",
 "en": [
   "Given a string <code>s</code> and a dictionary of strings <code>wordDict</code>, add spaces "
   "in <code>s</code> to construct a sentence where each word is a valid dictionary word. "
   "Return all such possible sentences in <strong>any order</strong>.",
   "<strong>Note</strong> that the same word in the dictionary may be reused multiple times in "
   "the segmentation.",
 ],
 "zh": [
   "給你一個字串 <code>s</code> 和一個單字字典 <code>wordDict</code>，"
   "在 <code>s</code> 裡加上空格，使得<strong>每一段都是字典裡的單字</strong>。",
   "回傳<strong>所有可能的句子</strong>（順序不限）。",
   "<strong>注意：字典裡的單字可以重複使用。</strong>",
 ],
 "pre": [
   ("note", "★ 為什麼「直接回溯」會逾時", [
     ("c", S["p140_nopruning"]),
     ("c", """這段程式碼是對的，但會在某些測資上逾時。

【致命的測資】：

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"   （30 個 a 加一個 b）
    wordDict = ["a","aa","aaa","aaaa","aaaaa",...,"aaaaaaaaaa"]

    答案是【空的】—— 因為結尾的 "b" 不在字典裡。

    但回溯要把 30 個 a 的【所有切法】都試過
    才發現「每一條路最後都卡在 b」。

    30 個 a 的切法數是指數級的 -> 直接 TLE ✘

【★ 關鍵洞察】：

    這些搜尋【全部都是白做的】——
    只要一開始就知道「從某個位置開始走不通」，
    就可以完全不進去。

【解法：先用第 139 題的 DP 算出可行性】

    ok[i] = s[i:] 能不能被拆開

    然後回溯時只走 ok[end] 為 True 的分支 ——
    保證【每一條走進去的路都一定會產出答案】✔

    這樣總時間就變成 O(答案的大小)，
    而不是 O(搜尋樹的大小)。

【「先算可行性、再搜尋」是回溯剪枝最有效的一招。】

    它的價值在於：把「可能白做的搜尋」
    變成「保證有收穫的搜尋」。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "catsanddog",
        wordDict = ["cat","cats","and","sand","dog"]
  輸出：["cats and dog","cat sand dog"]

範例 2
  輸入：s = "pineapplepenapple",
        wordDict = ["apple","pen","applepen","pine","pineapple"]
  輸出：["pine apple pen apple",
        "pineapple pen apple",
        "pine applepen apple"]

範例 3
  輸入：s = "catsandog",
        wordDict = ["cats","dog","sand","and","cat"]
  輸出：[]
  說明：怎麼切都會剩下 "og"。""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 20",
   "1 ≤ <code>wordDict.length</code> ≤ 1000",
   "1 ≤ <code>wordDict[i].length</code> ≤ 10",
   "<code>s</code> 和 <code>wordDict[i]</code> 只包含小寫英文字母",
   "<code>wordDict</code> 裡的單字<strong>互不相同</strong>",
   "輸入保證答案的<strong>總數不超過 10⁵</strong>",
 ],
 "mid": [
   ("note", "注意 s 的長度只有 20（第 139 題是 300）", [
     "<strong>因為這題的輸出可能是指數級的</strong>（最多 <code>2¹⁹</code> 種切法）。",
     "<strong>而且題目額外保證「答案總數不超過 10⁵」</strong> —— "
     "這是在告訴你「輸出不會爆炸」。",
     "<strong>但你的演算法仍然不能在「中間搜尋」時爆炸</strong> —— "
     "<strong>那正是「先剪枝」要解決的問題。</strong>",
   ]),
 ],
 "idea": [
   ("c", """兩階段：

【階段一：算可行性（第 139 題的 DP）】

    ok[i] = s[i:] 能不能被完全拆開

    ok[n] = True
    for i from n-1 down to 0:
        ok[i] = any(s[i:j] in words and ok[j] for j in i+1..n)

    如果 ok[0] 是 False -> 直接回傳 []（連試都不用試）

【階段二：回溯，但只走「走得通」的分支】

    def back(start):
        if start == n:
            res.append(" ".join(path))
            return
        for end in start+1..n:
            if s[start:end] in words and ok[end]:
                                          ^^^^^^^  ★ 剪枝
                path.append(s[start:end])
                back(end)
                path.pop()

【★ 加上 ok[end] 這個條件之後的保證】：

    每一次遞迴進去，都【一定】會產出至少一個答案。

    -> 搜尋樹的每一條路徑都對應到一個真實答案
    -> 總時間 = O(答案的總長度) ✔

    沒有這個條件的話，搜尋樹可能有指數級的「死路」。

【複雜度】

    階段一：O(n² · k)
    階段二：O(答案的總長度)，題目保證 <= 10^5 × 20

    兩者都可控 ✔"""),
 ],
 "approaches": [
   ap("解法一", "可行性 DP + 剪枝回溯（標準答案）", [
     ("c", S["p140"]),
     "<strong>兩階段，各十行。</strong>"
     "<strong><code>ok[end]</code> 那一個條件就是這題從 TLE 變成 AC 的關鍵。</strong>",
     ("h", "為什麼 <code>ok</code> 要「從後往前」算？"),
     ("c", """ok[i] 的定義是「s[i:] 能不能拆開」，
它依賴 ok[j]，其中 j > i（更後面的位置）。

    所以要先算好後面的 -> i 從大到小 ✔

【對照第 139 題】：

    那題的 dp[i] 是「s[:i] 能不能拆開」（前綴），
    依賴 dp[j] 其中 j < i -> i 從小到大。

    兩題的方向相反，因為狀態的定義相反。

    【「從哪一端定義狀態」決定了迴圈的方向。】

    這題用「後綴」是因為回溯是「從前往後切」的 ——
    我們需要在位置 i 時知道「後面走不走得通」。""",),
     ("h", "<code>if not ok[0]: return []</code> 這一行"),
     "<strong>不寫也對</strong>（回溯會找不到任何答案，自然回傳 <code>[]</code>），"
     "<strong>但寫了更清楚，而且省掉整趟回溯。</strong>",
     ("h", "為什麼收集時是 <code>\" \".join(path)</code> 而不是 <code>path[:]</code>？"),
     "<strong>因為題目要的是「句子字串」而不是「單字 list」。</strong>",
     "<code>\" \".join(path)</code> <strong>本身就產生一個新字串</strong>，"
     "所以<strong>不需要額外複製</strong> —— "
     "<strong>這和第 113 題的 <code>path[:]</code> 是同一個問題的不同解法。</strong>",
     "<strong>時間 O(n²·k + 答案總長度)、空間 O(n)（不算輸出）。</strong>",
   ], "O(n²·k + 答案)", "O(n)", "剪枝後不做白工", "ok 陣列 + 路徑", optimal=True),

   ap("解法二", "記憶化遞迴（回傳「所有句子」）", [
     ("c", S["p140_memo"]),
     ("h", "記憶化在這題真的有用嗎？"),
     ("c", """有用，但要看情況。

    go(start) 只有 n 個不同的參數 -> 最多算 n 次。

    考慮 s = "aaaa...ab"（答案是空的）：

        go(n-1) 會發現 "b" 不在字典 -> 回 []
        go(n-2) 呼叫 go(n-1) 得到 [] -> 自己也是 []
        ...

        每個 go(i) 只算一次 ✔ 不會指數爆炸

    【所以記憶化也能解決 TLE 問題】——
    和「先算可行性再剪枝」達到同樣的效果。

【兩者的差別】：

    解法一：先算一張布林表，回溯時「看表決定要不要走」
    解法二：直接快取「每個位置的所有答案」

    空間：
        解法一 O(n)
        解法二 O(所有子答案的總大小) —— 可能很大

    因為 go(i) 存的是「s[i:] 的所有拆法」，
    而那本身可能是指數級的。

    【但題目保證答案總數 <= 10^5，所以還可以接受。】

【base case 是 [""] 不是 []】

    [""] 代表「空字串有一種拆法：空句子」
    []   代表「空字串拆不開」✘

    寫成 [] 的話所有答案都會消失 ——
    和第 95、131 題是同一個坑。""",),
     ("h", "<code>w if rest == \"\" else w + \" \" + rest</code>"),
     "<strong>處理「最後一個單字後面不要加空格」。</strong>",
     "<strong>也可以先收集成 list 再 <code>join</code></strong>（像解法一那樣），"
     "<strong>那樣就不用這個特判。</strong>"
     "<strong>「用 list 收集、最後 join」通常比「邊走邊拼字串」乾淨。</strong>",
   ], "O(n²·k + 答案)", "O(答案總大小)", "每個狀態算一次", "快取所有子答案"),

   ap("解法三", "純回溯（會 TLE，但值得看）", [
     ("c", S["p140_nopruning"]),
     ("c", """這段程式碼【邏輯完全正確】，只是會逾時。

【它慢在哪裡？】

    s = 30 個 a + "b"，字典 = {"a", "aa", ..., "aaaaaaaaaa"}

    答案是空的，但回溯要走遍所有切法才知道。

    30 個 a 的切法數 ≈ 2^29 ≈ 5 億條路徑 ✘

【為什麼這個例子這麼有教育意義？】

    因為「答案很小」（是空的），
    但「搜尋樹很大」（指數級）。

    【搜尋的成本和答案的大小【完全脫鉤】】——
    這正是回溯類問題最危險的地方。

    加上 ok[end] 剪枝之後：
        每一條路徑都保證有收穫
        -> 搜尋成本 = 答案大小 ✔

【一般原則】：

    寫回溯時，永遠要問：
        「有沒有可能走進一條【一定沒有答案】的路？」

    如果有，就想辦法先算出來、提前擋掉。

    這叫做【可行性剪枝】（feasibility pruning），
    是回溯優化最有效的一招。""",),
     "<strong>放在這裡是為了對照</strong> —— "
     "<strong>它和解法一只差一個 <code>and ok[end]</code>。</strong>",
   ], "O(2ⁿ) 最壞", "O(n)", "會走進死路", "路徑"),
 ],
 "compare": (["解法", "時間", "空間", "會 TLE 嗎", "備註"],
   [["一、可行性 DP + 剪枝回溯", "O(n²k + 答案)", "O(n)", "✘", "標準答案"],
    ["二、記憶化遞迴", "O(n²k + 答案)", "O(答案總大小)", "✘", "空間較大"],
    ["三、純回溯", "O(2ⁿ) 最壞", "O(n)", "✔", "只差一個條件"]]),
 "edges": [
   "<strong>無解</strong> <code>\"catsandog\"</code> → <code>[]</code>（不是 <code>None</code>）。",
   "<strong>單一字元</strong> <code>s=\"a\", dict=[\"a\"]</code> → <code>[\"a\"]</code>。",
   "<strong>有多種拆法</strong> → 全部都要回傳，順序不限。",
   "<strong>致命測資</strong>：<code>\"aaaa...ab\"</code>（30 個 a）配上全是 a 的字典 → "
   "<strong>沒有剪枝的回溯要走 5 億條路，TLE。</strong>",
   "<strong>記憶化版 base case 寫成 <code>[]</code></strong> → 所有答案消失。",
   "<strong>忘了 <code>path.pop()</code></strong> → 路徑越積越長。",
   "<strong>句子結尾多一個空格</strong> → 判題失敗（要用 <code>join</code> 或特判）。",
   "<strong>沒有把 <code>wordDict</code> 轉成 <code>set</code></strong> → 每次查詢慢 1000 倍。",
 ],
 "follow": [
   ("h", "追問一：這題的複雜度到底怎麼算？"),
   ("c", """加了剪枝之後：

    階段一（算 ok）：O(n² · k)
        兩層迴圈，每次切片 + 查集合

    階段二（回溯）：O(答案的總長度)
        因為每條路徑都保證產出答案，
        而產出一個答案的成本是 O(n)（join）

    總共：O(n²·k + |答案| · n)

【但要小心「答案總數」本身可能是指數級的】：

    s = "aaaa...a"（20 個 a），字典 = {"a", "aa"}

    切法數 = 費氏數列 F(21) = 10946 種

    如果字典是 {"a","aa","aaa"}，就是三階費氏數列，
    成長更快。

    【題目保證「答案總數 <= 10^5」，
      就是在幫你把這個上界壓住。】

    沒有這個保證的話，任何演算法都不可能在時限內完成 ——
    因為光是輸出就做不完。""",),
   ("h", "追問二：剪枝和記憶化，哪一個比較好？"),
   ("c", """【剪枝（解法一）】
    ✔ 空間只要 O(n)
    ✔ 概念清楚：「先確認走得通，再走」
    ✘ 要寫兩個階段

【記憶化（解法二）】
    ✔ 一個函式寫完
    ✔ 從暴力解改過來只要加一行 @lru_cache
    ✘ 空間是 O(所有子答案的總大小)，可能很大

【實務上】：

    如果「子答案」很小（例如只是一個數字、一個布林值）
    -> 記憶化很划算

    如果「子答案」本身是一個大集合（像這題）
    -> 剪枝比較好，因為它只快取「布林值」

    【這是一個很好的判斷準則：
      看「要快取的東西有多大」。】""",),
   ("h", "追問三：如果字典非常大呢？"),
   "<strong>用 Trie 取代 <code>set</code></strong>（和第 139 題的追問一樣）。",
   "<strong>好處是「從位置 <code>start</code> 開始，一次走訪就能找出所有匹配的單字」</strong>，"
   "<strong>而不用對每個 <code>end</code> 都做一次切片 + 查詢。</strong>",
   ("h", "追問四：「可行性剪枝」還能用在哪些題目？"),
   ("ul", [
     "<strong>第 140 題</strong>：先算 <code>ok[]</code>，只走走得通的分支（本題）",
     "<strong>第 51 題 N 皇后</strong>：用「這一列還有沒有安全格」提前放棄",
     "<strong>第 37 題 解數獨</strong>：先算每格的候選數，從候選最少的開始填",
     "<strong>第 126 題 單詞接龍 II</strong>：先 BFS 算出最短距離，DFS 只走「距離剛好減一」的邊",
     "<strong>第 212 題 單字搜尋 II</strong>：用 Trie 提前判斷「這個前綴根本不存在」",
   ]),
   "<strong>共同模式：先用一個便宜的計算（DP / BFS / 預處理）"
   "算出「哪些分支一定沒有答案」，然後在搜尋時跳過它們。</strong>",
   "<strong>剪枝不會改變「最壞情況」的漸進複雜度，"
   "但它常常讓「實際上會遇到的輸入」從 TLE 變成瞬間完成。</strong>",
 ],
 "related": [
   "<strong>第 139 題 Word Break</strong> —— 本題的可行性階段，先學那題",
   "<strong>第 131 題 Palindrome Partitioning</strong> —— 同一個回溯骨架",
   "<strong>第 126 題 Word Ladder II</strong> —— 同樣是「先算可行性、再列舉」",
   "<strong>第 93 題 Restore IP Addresses</strong> —— 另一個切字串的回溯",
   "<strong>第 472 題 Concatenated Words</strong> —— 本題的進階版",
 ],
 "check": [
   "沒有剪枝的回溯，在什麼測資上會爆炸？為什麼「答案很小」也可能很慢？",
   "<code>ok[i]</code> 為什麼要從後往前算，而第 139 題的 <code>dp[i]</code> 從前往後？",
   "記憶化版的 base case 為什麼是 <code>[\"\"]</code> 而不是 <code>[]</code>？",
   "「剪枝」和「記憶化」在這題各有什麼優缺點？",
 ],
})
print("P140 written")
