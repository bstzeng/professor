# -*- coding: utf-8 -*-
"""第 122–125 題。"""
import random, itertools, re
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(122)


def _build(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _build(l), _build(r))


def _rand_tree(n, lo=-6, hi=6):
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi), _rand_tree(left, lo, hi), _rand_tree(n - 1 - left, lo, hi))


# ==================== 122. Best Time to Buy and Sell Stock II ====================
S["p122_greedy"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 把所有「上漲的日子」通通賺下來
        return sum(max(0, prices[i] - prices[i - 1])
                   for i in range(1, len(prices)))'''

S["p122_dp"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hold, free = float('-inf'), 0

        for p in prices:
            hold = max(hold, free - p)      # 【free - p】：賣掉之後還能再買
            free = max(free, hold + p)

        return free'''

S["p122_peak"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 找出每一段「谷 -> 峰」，把差價加起來
        n = len(prices)
        i, profit = 0, 0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1                      # 下坡：一路走到谷底
            valley = prices[i]
            while i < n - 1 and prices[i] <= prices[i + 1]:
                i += 1                      # 上坡：一路走到峰頂
            profit += prices[i] - valley
        return profit'''


def _p122_ref(prices):
    """獨立參考解：DP over (天, 是否持股)，逐格枚舉。"""
    n = len(prices)
    NEG = float("-inf")
    hold, free = NEG, 0
    for p in prices:
        nh = max(hold, free - p)
        nf = max(free, (hold + p) if hold != NEG else NEG)
        hold, free = nh, nf
    return free


def _p122_brute(prices):
    """更獨立的參考：枚舉每一天「買/賣/不動」的所有序列（只對極小輸入）。"""
    n = len(prices)
    best = [0]
    def go(i, holding, cash):
        if i == n:
            if not holding:
                best[0] = max(best[0], cash)
            return
        go(i + 1, holding, cash)                        # 不動
        if holding:
            go(i + 1, False, cash + prices[i])          # 賣
        else:
            go(i + 1, True, cash - prices[i])           # 買
    go(0, False, 0)
    return best[0]


_p122 = [S.load(k) for k in ("p122_greedy", "p122_dp", "p122_peak")]

for pr, want in [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
    ([1], 0),
    ([3, 3], 0),
]:
    assert _p122_brute(pr) == want, ("P122 brute", pr)
    for sol in _p122:
        assert sol.maxProfit(pr) == want, ("P122", pr, sol)

for _ in range(1500):
    n = random.randrange(1, 11)
    pr = [random.randint(0, 12) for _ in range(n)]
    want = _p122_brute(pr)
    assert _p122_ref(pr) == want, ("P122 ref", pr)
    for sol in _p122:
        assert sol.maxProfit(pr) == want, ("P122 random", pr, want, sol)
for _ in range(3000):
    pr = [random.randint(0, 100) for _ in range(random.randrange(1, 60))]
    want = _p122_ref(pr)
    for sol in _p122:
        assert sol.maxProfit(pr) == want, ("P122 big", pr, want, sol)
print("P122 solutions OK")

_P122_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">無限次交易時，「低買高賣一整段」和「每天賺一點」的總利潤完全相同 —— 望遠鏡求和。</text>
            <g stroke="var(--border)" stroke-width="1"><line x1="60" y1="210" x2="330" y2="210"/></g>
            <g font-size="12" text-anchor="middle">
              <circle cx="90" cy="180" r="5" fill="var(--accent)"/><text x="90" y="200" fill="var(--accent)">a=1</text>
              <circle cx="190" cy="120" r="5" fill="var(--text-muted)"/><text x="190" y="140" fill="var(--text-muted)">b=4</text>
              <circle cx="290" cy="60" r="5" fill="#ff8a65"/><text x="290" y="82" fill="#ff8a65">c=7</text>
            </g>
            <polyline points="90,180 190,120 290,60" fill="none" stroke="var(--border)" stroke-width="1.5"/>
            <text x="60" y="242" fill="var(--gold)" font-size="12" text-anchor="start">整段做： c − a = 7 − 1 = 6</text>
            <text x="60" y="266" fill="var(--gold)" font-size="12" text-anchor="start">拆開做： (b−a) + (c−b) = 3 + 3 = 6　← 完全一樣</text>
            <text x="60" y="292" fill="var(--text-muted)" font-size="12" text-anchor="start">中間的 b 被加一次又減一次，抵銷掉了。</text>
            <line x1="360" y1="40" x2="360" y2="300" stroke="var(--border)"/>
            <text x="385" y="60" fill="#ff8a65" font-size="13" text-anchor="start">下跌的日子怎麼辦？</text>
            <text x="385" y="86" fill="var(--text-muted)" font-size="12" text-anchor="start">prices = [7, 1, 5, 3, 6, 4]</text>
            <text x="385" y="112" fill="var(--text-muted)" font-size="12" text-anchor="start">漲跌 = −6, +4, −2, +3, −2</text>
            <text x="385" y="142" fill="var(--gold)" font-size="12" text-anchor="start">只收正的： 4 + 3 = 7 ✔</text>
            <text x="385" y="172" fill="var(--text-muted)" font-size="12" text-anchor="start">下跌的日子「不持股」就好 ——</text>
            <text x="385" y="196" fill="var(--text-muted)" font-size="12" text-anchor="start">不做交易的自由，讓我們能</text>
            <text x="385" y="220" fill="var(--text-muted)" font-size="12" text-anchor="start">獨立挑選每一天要不要賺。</text>
            <text x="385" y="254" fill="var(--accent)" font-size="12" text-anchor="start">這就是貪心成立的理由：</text>
            <text x="385" y="278" fill="var(--accent)" font-size="12" text-anchor="start">每一天的決定互不干擾。</text>
            <line x1="20" y1="320" x2="620" y2="320" stroke="var(--border)"/>
            <text x="20" y="346" fill="#ff8a65" font-size="12">對照第 121 題（只能一次）：那裡的決定【互相干擾】——買了這次就不能買下次，</text>
            <text x="20" y="370" fill="#ff8a65" font-size="12">所以不能各自貪心，必須全域比較。一個限制條件，就讓問題的性質完全不同。</text>'''

emit({
 "num": 122, "slug": "best-time-to-buy-and-sell-stock-ii",
 "en": [
   "You are given an integer array <code>prices</code> where <code>prices[i]</code> is the "
   "price of a given stock on the <code>i</code><sup>th</sup> day.",
   "On each day, you may decide to buy and/or sell the stock. You can only hold "
   "<strong>at most one</strong> share of the stock at any time. However, you can buy it then "
   "immediately sell it on the <strong>same day</strong>.",
   "Find and return <em>the <strong>maximum</strong> profit you can achieve</em>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>prices</code>，<code>prices[i]</code> 是第 <code>i</code> 天的股價。",
   "每一天你都可以決定買入和／或賣出。"
   "你<strong>最多只能同時持有一股</strong>，"
   "但<strong>可以在同一天買了又賣</strong>。",
   "回傳你能獲得的<strong>最大利潤</strong>。",
 ],
 "pre": [
   ("note", "和第 121 題只差一個限制，但解法完全不同", [
     ("c", """第 121 題：只能交易【一次】  -> 必須全域比較「哪一對買賣最好」
第 122 題：可以交易【無限次】-> 每一天可以獨立決定

【關鍵差別：決定之間有沒有互相干擾。】

    121：買了這一次，就不能買另一次 -> 決定互相排斥
         -> 不能貪心，要比較所有可能

    122：今天賺不賺這一段漲幅，完全不影響明天
         -> 決定互相獨立
         -> 可以貪心 ✔

【這是判斷「能不能貪心」最重要的一個問題】：

    「我現在做的這個選擇，會不會限制未來的選擇？」

    會 -> 通常要 DP
    不會 -> 常常可以貪心

    第 134 題（加油站）、第 135 題（分發糖果）、
    第 55 題（跳躍遊戲）的貪心都可以這樣檢驗。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：prices = [7,1,5,3,6,4]
  輸出：7
  說明：第 2 天買（1）第 3 天賣（5），賺 4
        第 4 天買（3）第 5 天賣（6），賺 3
        總共 7。

範例 2
  輸入：prices = [1,2,3,4,5]
  輸出：4
  說明：第 1 天買、第 5 天賣，賺 4。
        也可以每天買賣一次：1+1+1+1 = 4 —— 【一樣多】。

範例 3
  輸入：prices = [7,6,4,3,1]
  輸出：0
  說明：一路下跌，不交易。""",
 "constraints": [
   "1 ≤ <code>prices.length</code> ≤ 3 × 10⁴",
   "0 ≤ <code>prices[i]</code> ≤ 10⁴",
 ],
 "idea": [
   ("fig", _P122_FIG, "0 0 640 388"),
   ("c", """【一行解】：

    profit = Σ max(0, prices[i] - prices[i-1])

    「把每一天的漲幅（如果是正的）都收下來。」

【為什麼這樣一定最優？兩個方向的證明】

    (1) 貪心不會比最優解差（貪心是可達的）

        對每一段連續上漲 prices[i] < prices[i+1]，
        我們可以真的「第 i 天買、第 i+1 天賣」。

        這些交易互不衝突（每天最多持一股，
        而且可以當天賣了又買）。

        所以貪心算出的利潤是【真的做得到的】✔

    (2) 最優解不會比貪心好（貪心是上界）

        任何一筆交易「第 i 天買、第 j 天賣」，
        利潤 = prices[j] - prices[i]
             = Σ_{k=i+1..j} (prices[k] - prices[k-1])     望遠鏡求和
             <= Σ_{k=i+1..j} max(0, prices[k] - prices[k-1])
             <= 貪心的總和

        所以任何策略的利潤都 <= 貪心 ✔

    兩邊夾擊 -> 貪心就是最優 ✔

【這個「拆成每日漲跌」的觀點，
  也解釋了為什麼「同一天可以買了又賣」這個條件很重要】——

    它讓「每天獨立決定」變成合法的策略。
    沒有這個條件，相鄰兩段交易就會衝突。"""),
 ],
 "approaches": [
   ap("解法一", "貪心：把所有漲幅加起來（標準答案）", [
     ("c", S["p122_greedy"]),
     "<strong>一行。O(n) 時間、O(1) 空間。</strong>",
     ("h", "常見的誤解：「這樣不是每天都在交易嗎？」"),
     ("c", """是的，但【總利潤和「最少次數的最優策略」完全相同】。

    prices = [1, 2, 3, 4, 5]

    貪心：每天買賣 -> 1+1+1+1 = 4
    人類：第一天買、最後一天賣 -> 5-1 = 4

    【一樣。】

    因為題目【不限制交易次數，也沒有手續費】。

    如果加上手續費（第 714 題），
    貪心就會壞掉 —— 那時「少交易幾次」就有價值了，
    必須用狀態機 DP。

【這也提醒我們：
  貪心的正確性總是依賴題目的某個具體條件。
  條件一變，貪心就可能失效。】

    這題依賴的是「無限次 + 無手續費 + 可當日買賣」。"""),
     ("h", "為什麼寫 <code>max(0, ...)</code> 而不是 <code>if ... > 0</code>？"),
     "<strong>兩者等價</strong>，<code>max(0, x)</code> 在生成式裡比較短。",
     "<strong>也可以寫成 <code>sum(b - a for a, b in zip(prices, prices[1:]) if b > a)</code></strong> —— "
     "<code>zip(prices, prices[1:])</code> 是「取相鄰配對」的 Python 慣用寫法。",
   ], "O(n)", "O(1)", "掃一遍", "沒有額外空間", optimal=True),

   ap("解法二", "狀態機 DP（能推廣到 123、188、309、714）", [
     ("c", S["p122_dp"]),
     ("h", "★ 和第 121 題只差一個 <code>free</code>"),
     ("c", """第 121 題（一次）： hold = max(hold, 0 - p)
第 122 題（無限次）：hold = max(hold, free - p)
                                     ^^^^

    多了 free，意思是「我可以用【賣掉之後的現金】再買」。

    第 121 題只能用 0（從來沒交易過的現金），
    因為買入之前一定沒有任何交易。

【一個變數的差別，就是「一次」和「無限次」。】

    這個狀態機還能繼續長：

    714（手續費）：
        free = max(free, hold + p - fee)

    309（冷凍期，賣出後要休息一天）：
        需要第三個狀態 cooldown
        hold = max(hold, cooldown - p)     不能用剛賣完的 free
        free = max(free, hold + p)
        cooldown = 上一輪的 free

    123 / 188（最多 k 次）：
        2k 個狀態，用迴圈跑

【六題一個框架。這就是為什麼要學狀態機版，
  即使本題有一行的貪心解。】"""),
     ("h", "注意 <code>hold</code> 和 <code>free</code> 的更新順序"),
     ("c", """hold = max(hold, free - p)      # 先更新 hold
free = max(free, hold + p)      # 再用【新的】hold 更新 free

    這裡用了新的 hold —— 意思是「今天買了又賣」。

    對這題來說沒問題（題目明說可以當天買賣，
    而且當天買賣的利潤是 0，不會讓答案變大）。

    但在【有手續費】的第 714 題，
    當天買賣會虧手續費，所以答案還是不受影響（不會被選中）。

    在【有冷凍期】的第 309 題，
    順序就會影響正確性 —— 那題必須用「上一輪的值」。

    【安全的寫法是先把舊值存起來】：

        new_hold = max(hold, free - p)
        new_free = max(free, hold + p)
        hold, free = new_hold, new_free

    這樣不管題目怎麼變都對。"""),
   ], "O(n)", "O(1)", "掃一遍", "兩個變數"),

   ap("解法三", "找「谷 → 峰」（最貼近直覺，但最長）", [
     ("c", S["p122_peak"]),
     ("c", """這是「人類交易員」的思路：
    找到一個谷底，買進；找到一個峰頂，賣出；重複。

    利潤和貪心完全相同 ——
    因為「一段連續上漲的總漲幅」= 「谷到峰的差」。

【為什麼還是要寫貪心？】

    這個版本：
        ✘ 三層巢狀迴圈（雖然總共還是 O(n)）
        ✘ 邊界條件多（i < n-1 要寫四次）
        ✘ 平坦區間（prices[i] == prices[i+1]）要小心
           —— 用 >= 和 <= 才不會卡住

    貪心版：
        ✔ 一行
        ✔ 沒有邊界

【但這個版本有一個獨特的價值】：
    如果題目要問「實際上要在哪幾天買賣」，
    這個版本可以直接輸出 (valley, peak) 的清單 ——
    而且是【交易次數最少】的那一組方案。

    貪心版算得出總利潤，卻給不出「最少次數」的方案。""",),
   ], "O(n)", "O(1)", "每個元素被走一次", "幾個變數"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "能推廣嗎"],
   [["一、貪心加漲幅", "O(n)", "O(1)", "1", "✘ 加手續費就壞"],
    ["二、狀態機 DP", "O(n)", "O(1)", "6", "✔ 六題通用"],
    ["三、找谷峰", "O(n)", "O(1)", "12", "△ 能輸出交易方案"]]),
 "edges": [
   "<strong>只有一天</strong> → <code>0</code>（<code>range(1, 1)</code> 是空的 ✔）。",
   "<strong>一路下跌</strong> → <code>0</code>。",
   "<strong>一路上漲</strong> <code>[1,2,3,4,5]</code> → <code>4</code>。",
   "<strong>全部相同</strong> <code>[3,3,3]</code> → <code>0</code>。"
   "<strong>解法三如果用 <code>&gt;</code> 而不是 <code>&gt;=</code> 會卡在原地無窮迴圈。</strong>",
   "<strong>鋸齒狀</strong> <code>[1,5,1,5]</code> → <code>8</code>（兩段各賺 4）。",
   "<strong>誤以為「只能做一次大交易」</strong> → 會得到第 121 題的答案（偏小）。",
   "<strong>忘了 <code>max(0, ...)</code></strong> → 把下跌也加進去，答案偏小甚至變負。",
   "<strong>3 × 10⁴ 天</strong> → O(n) 完全沒壓力。",
 ],
 "follow": [
   ("h", "追問一：如果每筆交易要付手續費呢？"),
   "<strong>第 714 題。貪心會壞掉</strong> —— "
   "因為「多做一筆交易」現在有成本了，"
   "<strong>「每天賺一點」會被手續費吃光。</strong>",
   ("c", """狀態機版只要改一行：

    hold = max(hold, free - p)
    free = max(free, hold + p - fee)      # 賣出時扣手續費
                              ^^^^^

    【這就是為什麼要學狀態機版】——
    題目一變，貪心要重想，狀態機只要改一個字。""",),
   ("h", "追問二：如果賣出後要冷凍一天呢？"),
   "<strong>第 309 題。需要第三個狀態</strong>：",
   ("c", """hold      今天結束時持股
free      今天結束時空手，【而且不在冷凍期】
cooled    今天剛賣掉（明天不能買）

    new_hold   = max(hold, free - p)       # 只能用「非冷凍」的現金買
    new_cooled = hold + p                  # 今天賣掉
    new_free   = max(free, cooled)         # 昨天冷凍的，今天解凍

【注意這裡一定要用「上一輪的值」】——
    因為 new_hold 用的 free 必須是昨天的（今天剛解凍的那個）。

    這就是解法二裡「先存舊值」那個建議的實際用處。"""),
   ("h", "追問三：如果最多只能交易 k 次呢？"),
   "<strong>第 188 題。<code>2k</code> 個狀態，用迴圈跑。</strong>",
   "<strong>而且有一個重要的優化</strong>："
   "<strong>當 <code>k >= n // 2</code> 時，限制等於沒有限制</strong>"
   "（因為最多也只能做 <code>n//2</code> 筆交易），"
   "<strong>可以直接退化成本題的貪心 —— 從 <code>O(nk)</code> 降到 <code>O(n)</code>。</strong>",
   ("h", "追問四：如果可以同時持有多股呢？"),
   "<strong>那就沒有上限了 —— 在最低點買進無限多股，在最高點全賣掉。</strong>",
   "<strong>「最多持有一股」這個限制，是讓問題有限的關鍵。</strong>"
   "<strong>讀題時要特別注意這類「看起來是廢話」的限制條件 —— 它們常常是問題的核心。</strong>",
 ],
 "related": [
   "<strong>第 121 題 …I</strong> —— 只能一次，不能貪心",
   "<strong>第 123/188 題 …III/IV</strong> —— 最多兩次 / k 次",
   "<strong>第 309 題 含冷凍期</strong> —— 三個狀態",
   "<strong>第 714 題 含手續費</strong> —— 貪心失效的例子",
   "<strong>第 55 題 Jump Game</strong> —— 另一個「決定互不干擾」的貪心",
 ],
 "check": [
   "為什麼這題可以貪心，第 121 題不行？判斷依據是什麼？",
   "「拆成每日漲跌」的望遠鏡求和，怎麼證明貪心是上界？",
   "狀態機版和第 121 題只差一個字，是哪一個？意思是什麼？",
   "加上手續費之後，貪心為什麼會壞掉？",
 ],
})
print("P122 written")

# ==================== 123. Best Time to Buy and Sell Stock III ====================
S["p123_states"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 四個狀態：第一次買完 / 第一次賣完 / 第二次買完 / 第二次賣完 之後的最大現金
        buy1 = buy2 = float('-inf')
        sell1 = sell2 = 0

        for p in prices:
            buy1 = max(buy1, -p)            # 第一次買（本金 0）
            sell1 = max(sell1, buy1 + p)    # 第一次賣
            buy2 = max(buy2, sell1 - p)     # 第二次買（用第一次賣完的錢）
            sell2 = max(sell2, buy2 + p)    # 第二次賣

        return sell2'''

S["p123_split"] = '''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # left[i]  = 在 prices[0..i] 裡只做一次交易的最大利潤
        left = [0] * n
        low = prices[0]
        for i in range(1, n):
            low = min(low, prices[i])
            left[i] = max(left[i - 1], prices[i] - low)

        # right[i] = 在 prices[i..n-1] 裡只做一次交易的最大利潤
        right = [0] * (n + 1)
        high = prices[-1]
        for i in range(n - 2, -1, -1):
            high = max(high, prices[i])
            right[i] = max(right[i + 1], high - prices[i])

        # 枚舉分割點：前半做一次、後半做一次
        return max(left[i] + right[i + 1] for i in range(n))'''

S["p123_k"] = '''class Solution:
    def maxProfit(self, prices: List[int], k: int = 2) -> int:
        # 通用版：2k 個狀態，k=2 就是本題
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for p in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - p)
                sell[j] = max(sell[j], buy[j] + p)

        return sell[k]'''


def _p123_ref(prices, k=2):
    """獨立參考解：枚舉最多 k 段不重疊的區間（只對小輸入）。"""
    n = len(prices)
    best = 0
    # 枚舉 0、1、2 筆交易的所有 (買日, 賣日)
    for t in range(0, k + 1):
        for days in itertools.combinations(range(n), 2 * t):
            ok = True
            profit = 0
            for x in range(t):
                b, s = days[2 * x], days[2 * x + 1]
                profit += prices[s] - prices[b]
            if ok:
                best = max(best, profit)
    return best


_p123 = [S.load(k) for k in ("p123_states", "p123_split", "p123_k")]

for pr, want in [
    ([3, 3, 5, 0, 0, 3, 1, 4], 6),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
    ([1], 0),
    ([], 0),
]:
    if pr:
        assert _p123_ref(pr) == want, ("P123 ref", pr, _p123_ref(pr))
    for sol in _p123:
        assert sol.maxProfit(pr) == want, ("P123", pr, sol)

for _ in range(1200):
    n = random.randrange(1, 10)
    pr = [random.randint(0, 15) for _ in range(n)]
    want = _p123_ref(pr)
    for sol in _p123:
        assert sol.maxProfit(pr) == want, ("P123 random", pr, want, sol)
# 大輸入：三種解法互相對照
for _ in range(2000):
    pr = [random.randint(0, 200) for _ in range(random.randrange(1, 70))]
    vals = [sol.maxProfit(pr) for sol in _p123]
    assert len(set(vals)) == 1, ("P123 disagree", pr, vals)
print("P123 solutions OK")

emit({
 "num": 123, "slug": "best-time-to-buy-and-sell-stock-iii",
 "en": [
   "You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a "
   "given stock on the <code>i</code><sup>th</sup> day.",
   "Find the maximum profit you can achieve. You may complete <strong>at most two "
   "transactions</strong>.",
   "<strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., "
   "you must sell the stock before you buy again).",
 ],
 "zh": [
   "給你一個陣列 <code>prices</code>，<code>prices[i]</code> 是第 <code>i</code> 天的股價。",
   "求你能獲得的最大利潤，但<strong>最多只能完成兩筆交易</strong>。",
   "<strong>注意：</strong>你不能同時持有多筆交易 —— "
   "<strong>必須先賣掉，才能再買</strong>。",
 ],
 "pre": [
   ("note", "從「一次」「無限次」到「最多兩次」", [
     ("c", """121（一次）：    一趟掃描記最低價                O(n)
122（無限次）：  貪心加漲幅                      O(n)
123（最多兩次）：？                             ← 本題

【為什麼這題突然變 Hard？】

    121 之所以簡單，是因為「只有一次」讓問題退化成
    「找最大差值」。

    122 之所以簡單，是因為「無限次」讓每天的決定獨立。

    123 卡在中間 ——
        有限制（不能無限次）-> 貪心失效
        限制又不夠緊（不只一次）-> 121 的技巧也不夠

    【這是演算法題常見的模式：
      「太鬆」和「太緊」都簡單，中間才難。】

    解法有兩條路：
        A. 四個狀態變數（推薦，也能推廣到 k 次）
        B. 枚舉分割點，左右各做一次 121"""),
   ]),
 ],
 "examples": """範例 1
  輸入：prices = [3,3,5,0,0,3,1,4]
  輸出：6
  說明：第 4 天買（0）第 6 天賣（3），賺 3
        第 7 天買（1）第 8 天賣（4），賺 3
        總共 6。

範例 2
  輸入：prices = [1,2,3,4,5]
  輸出：4
  說明：一路上漲，只要做一筆（第 1 天買、第 5 天賣）就夠了。
        【「最多兩次」不代表「一定要兩次」。】

範例 3
  輸入：prices = [7,6,4,3,1]
  輸出：0""",
 "constraints": [
   "1 ≤ <code>prices.length</code> ≤ 10⁵",
   "0 ≤ <code>prices[i]</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【方法 A：四個狀態變數】

    把「一筆交易」拆成「買」和「賣」兩個事件，
    兩筆交易就是四個事件，按時間順序：

        買1 -> 賣1 -> 買2 -> 賣2

    對每一天，維護「走到這一步時的最大現金」：

        buy1  = max(buy1,  0     - p)     第一次買（本金 0）
        sell1 = max(sell1, buy1  + p)     第一次賣
        buy2  = max(buy2,  sell1 - p)     第二次買（用賣1 的錢）
        sell2 = max(sell2, buy2  + p)     第二次賣

    答案 = sell2

【★ 為什麼可以在同一個迴圈裡依序更新？】

    看起來有問題：buy1 剛更新完，sell1 就用了新的 buy1 ——
    這不就是「同一天買又賣」嗎？

    是的，但【同一天買又賣的利潤是 0】，
    不會讓答案變大，所以無害 ✔

    而且「允許同日買賣」剛好對應到
    「其實只做一筆交易」的情況：
        buy1 -> sell1（真交易）-> buy2 -> sell2（同日，賺 0）

    所以「最多兩次」自動涵蓋了「一次」和「零次」✔

    【這個「順序更新其實安全」的論證值得想清楚 ——
      面試官很可能會問。】

【方法 B：枚舉分割點】

    兩筆交易一定可以被一個分割點 i 分開：
        第一筆完全在 [0, i]，第二筆完全在 [i, n-1]

    left[i]  = [0..i] 裡做一次交易的最大利潤   （第 121 題，正著掃）
    right[i] = [i..n-1] 裡做一次交易的最大利潤 （第 121 題，倒著掃）

    答案 = max over i of (left[i] + right[i+1])

    O(n) 時間、O(n) 空間。

    【比較好想，但空間多了 O(n)，也不好推廣到 k 次。】"""),
 ],
 "approaches": [
   ap("解法一", "四個狀態變數（標準答案）", [
     ("c", S["p123_states"]),
     "<strong>八行，O(n) 時間、O(1) 空間。</strong>",
     ("h", "初始值為什麼是這些？"),
     ("c", """buy1 = buy2 = -inf      一開始「不可能」已經買了
sell1 = sell2 = 0       一開始「什麼都沒做」，現金 0

    sell 初始成 0 的意思是「零筆交易」也是合法答案 ——
    這自動處理了「一路下跌就不交易」的情況 ✔

    buy 初始成 -inf 是為了讓第一次的 max 一定取到 -p。

    【也可以初始成 -prices[0]，然後從第 1 天開始掃】——
    但那樣要特判空陣列，不如用 -inf 乾淨。

【驗算 prices = [1, 2]】：

    p=1: buy1=max(-inf,-1)=-1
         sell1=max(0,-1+1)=0
         buy2=max(-inf,0-1)=-1
         sell2=max(0,-1+1)=0

    p=2: buy1=max(-1,-2)=-1
         sell1=max(0,-1+2)=1     ✔ 賺 1
         buy2=max(-1,1-2)=-1
         sell2=max(0,-1+2)=1     ✔

    答案 1 ✔"""),
     ("h", "為什麼答案是 <code>sell2</code> 而不是 <code>max(sell1, sell2)</code>？"),
     "因為 <code>sell2 >= sell1</code> <strong>永遠成立</strong> —— "
     "<strong>「做完第一筆之後，第二筆可以同日買賣賺 0」</strong>，"
     "所以 <code>sell2</code> 至少能達到 <code>sell1</code> 的水準。",
     "<strong>寫 <code>max(sell1, sell2)</code> 也對，只是多餘。</strong>",
   ], "O(n)", "O(1)", "掃一遍，每天四次更新", "四個變數", optimal=True),

   ap("解法二", "枚舉分割點（最好想）", [
     ("c", S["p123_split"]),
     ("h", "兩個方向各掃一次"),
     ("c", """left[i] = 在 [0..i] 裡做【一次】交易的最大利潤
    -> 正著掃，維護「歷史最低價」（就是第 121 題）

right[i] = 在 [i..n-1] 裡做【一次】交易的最大利潤
    -> 倒著掃，維護「未來最高價」

    注意 right 的長度是 n+1，
    多出來的 right[n] = 0 代表「後半段是空的」——
    這樣 left[n-1] + right[n] 就自然表示「只做一筆」✔

    【多開一格當哨兵，省掉一個邊界特判 ——
      這個技巧在前綴和、後綴陣列裡非常常見。】

答案 = max over i of (left[i] + right[i+1])

    i 代表「第一筆在 i 之前（含）完成，第二筆在 i 之後開始」。

    因為 left[i] 和 right[i+1] 的區間不重疊，
    所以兩筆交易一定合法 ✔"""),
     ("h", "為什麼「兩筆交易一定能被一個點分開」？"),
     "因為題目說<strong>「必須先賣掉才能再買」</strong> —— "
     "<strong>所以兩筆交易的時間區間不重疊</strong>，"
     "<strong>一定存在一個分割點落在它們中間。</strong>",
     "<strong>如果允許同時持有多筆（題目特別排除了），這個分解就不成立。</strong>",
     "<strong>O(n) 時間、O(n) 空間。</strong>"
     "<strong>思路最直白，但不好推廣到 k 次</strong>"
     "（k 次要枚舉 k-1 個分割點，變成 <code>O(n^(k-1))</code>）。",
   ], "O(n)", "O(n)", "三趟掃描", "兩個輔助陣列"),

   ap("解法三", "通用的 k 次版本（第 188 題的解法）", [
     ("c", S["p123_k"]),
     ("c", """把四個變數換成兩個長度 k+1 的陣列：

    buy[j]  = 完成 j-1 筆交易、且第 j 次已買入時的最大現金
    sell[j] = 完成 j 筆交易時的最大現金

    for j in 1..k:
        buy[j]  = max(buy[j],  sell[j-1] - p)
        sell[j] = max(sell[j], buy[j]    + p)

    k = 2 時就是解法一（buy[1]=buy1, sell[1]=sell1, ...）。

【★ j 為什麼要正著跑？】

    buy[j] 用到 sell[j-1]（這一輪【已經更新過】的值）。

    這代表「第 j-1 筆和第 j 筆可以在同一天完成」——
    同樣地，那樣的利潤是 0，無害 ✔

    倒著跑也對（那樣用的是上一輪的 sell[j-1]），
    只是語意變成「不能同日」——答案一樣。

【複雜度 O(nk)】

    k = 2 時是 O(2n)，和解法一相同。

    第 188 題的 k 可以很大，那時要加上優化：
        if k >= n // 2: 直接退化成第 122 題的貪心

    因為最多也只能做 n//2 筆交易
    （每筆至少佔兩天）。"""),
     "<strong>寫這個版本的好處是「一份程式碼解四題」</strong>"
     "（121 是 k=1、122 是 k=∞、123 是 k=2、188 是任意 k）。",
   ], "O(n·k)", "O(k)", "每天跑 k 次", "兩個長度 k 的陣列"),
 ],
 "compare": (["解法", "時間", "空間", "能推廣到 k 次", "備註"],
   [["一、四個狀態", "O(n)", "O(1)", "△ 要手動展開", "標準答案"],
    ["二、枚舉分割點", "O(n)", "O(n)", "✘", "最好想"],
    ["三、通用 k 次", "O(nk)", "O(k)", "✔", "一份程式碼解四題"]]),
 "edges": [
   "<strong>只有一天</strong> → <code>0</code>。",
   "<strong>空陣列</strong>（題目保證不會）→ <code>0</code>。"
   "<strong>解法二要特判 <code>n &lt; 2</code>，解法一、三自然正確。</strong>",
   "<strong>一路上漲</strong> <code>[1,2,3,4,5]</code> → <code>4</code>。"
   "<strong>「最多兩次」不代表要湊滿兩次。</strong>",
   "<strong>一路下跌</strong> → <code>0</code>。"
   "<strong><code>sell</code> 初始成 <code>-inf</code> 會回傳負數。</strong>",
   "<strong><code>[3,3,5,0,0,3,1,4]</code></strong> → <code>6</code>（要真的做兩筆）。",
   "<strong>兩段漲幅一大一小</strong>，例如 <code>[1,100,1,2]</code> → "
   "<code>100</code>（第二筆只賺 1，但不做也沒差）。",
   "<strong>把 <code>buy2</code> 的來源寫成 <code>-p</code> 而不是 <code>sell1 - p</code></strong> → "
   "<strong>變成「兩筆交易各自獨立、可以重疊」，答案偏大。</strong>",
   "<strong>10⁵ 天</strong> → O(n) 和 O(2n) 都輕鬆。",
 ],
 "follow": [
   ("h", "追問一：四個狀態依序更新，為什麼不會「同一天做完兩筆」而算錯？"),
   ("c", """會「同一天做完」，但那樣的利潤是 0，所以不會讓答案偏大。

    嚴格地說：

        sell2 = max(sell2, buy2 + p)
              = max(sell2, max(buy2_old, sell1 - p) + p)
              = max(sell2, buy2_old + p, sell1)

    最後那一項 sell1 就是「第二筆同日買賣，賺 0」。

    而 sell1 本來就是一個合法的答案（只做一筆），
    所以把它納入 max 完全正確 ✔

【這個論證的一般形式】：

    「允許退化的選項」只要不會產生【非法】或【偏大】的值，
    就可以放心納入 —— 它會自動涵蓋「用不滿限制」的情況。

    第 188 題的 k 次版本、
    背包問題的「可以不裝滿」版本，
    用的都是同一個技巧。"""),
   ("h", "追問二：如果最多 k 次呢？"),
   "<strong>第 188 題</strong>，就是解法三。"
   "<strong>記得加上 <code>k >= n // 2</code> 時退化成貪心的優化</strong>，"
   "否則 <code>k = 10⁹</code> 時 <code>O(nk)</code> 會爆。",
   ("h", "追問三：如果要輸出「哪四天買賣」呢？"),
   "<strong>解法二比較容易</strong> —— 找到最佳分割點 <code>i</code> 之後，"
   "在 <code>[0,i]</code> 和 <code>[i+1,n-1]</code> 各跑一次第 121 題的「記錄買賣日」版本。",
   "<strong>解法一要輸出方案就麻煩了</strong> —— "
   "<strong>狀態機壓縮掉了「是在哪一天做的」這個資訊，要額外記錄。</strong>"
   "<strong>「空間優化」和「能否回溯方案」常常是互相衝突的。</strong>",
   ("h", "追問四：如果兩筆交易可以重疊（同時持有兩股）呢？"),
   "<strong>那就是「找兩段不一定不重疊的最大差」</strong> —— "
   "<strong>答案會變成「兩倍的第 121 題答案」</strong>"
   "（同一段最好的交易做兩次）。",
   "<strong>題目特別寫「必須先賣掉才能再買」，就是為了排除這個退化情況。</strong>"
   "<strong>這又是一個「看起來是廢話的限制其實是核心」的例子。</strong>",
 ],
 "related": [
   "<strong>第 121 題 …I</strong> —— k = 1",
   "<strong>第 122 題 …II</strong> —— k = ∞，貪心",
   "<strong>第 188 題 …IV</strong> —— 任意 k，就是解法三",
   "<strong>第 309/714 題</strong> —— 冷凍期 / 手續費",
 ],
 "check": [
   "為什麼「一次」和「無限次」都簡單，「最多兩次」反而難？",
   "四個狀態依序更新，為什麼「同一天做完兩筆」不會讓答案出錯？",
   "<code>buy2</code> 的來源為什麼是 <code>sell1 - p</code> 而不是 <code>-p</code>？",
   "解法二為什麼「兩筆交易一定能被一個分割點分開」？依賴哪個條件？",
 ],
})
print("P123 written")

# ==================== 124. Binary Tree Maximum Path Sum ====================
S["p124"] = '''class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')

        def gain(node) -> int:
            """回傳：從 node 往下延伸【一條】路徑能拿到的最大和（可以選擇不往下）"""
            if not node:
                return 0

            # 負的貢獻不如不要，所以和 0 取 max
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)

            # 【答案】：在 node 這裡「拐彎」，左邊 + 自己 + 右邊
            self.best = max(self.best, node.val + left + right)

            # 【回傳值】：給父節點用的，只能選一邊（否則就不是一條路徑了）
            return node.val + max(left, right)

        gain(root)
        return self.best'''

S["p124_nonlocal"] = '''class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float('-inf')

        def gain(node):
            nonlocal best
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        gain(root)
        return best'''

S["p124_wrong"] = '''class Solution:
    # 【這是錯的，不要抄】
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def gain(node):
            if not node:
                return 0
            left = max(gain(node.left), 0)
            right = max(gain(node.right), 0)
            return node.val + left + right   # ← 直接回傳「拐彎」的值
        return gain(root)'''


def _p124_ref(root):
    """獨立參考解：枚舉所有節點對之間的路徑（樹上任兩點路徑唯一）。"""
    nodes = []
    def collect(nd):
        if nd:
            nodes.append(nd); collect(nd.left); collect(nd.right)
    collect(root)
    if not nodes:
        return None
    # 對每個節點，算出「以它為最高點」的所有路徑
    best = float("-inf")
    def down(nd):
        """從 nd 往下所有單邊路徑的和（含空）"""
        if not nd:
            return [0]
        out = [nd.val]
        for kid in (nd.left, nd.right):
            for v in down(kid):
                if kid:
                    out.append(nd.val + v)
        return out
    for nd in nodes:
        ls = down(nd.left) if nd.left else [0]
        rs = down(nd.right) if nd.right else [0]
        # 單邊也可以是「不走」
        ls = ls + [0]
        rs = rs + [0]
        for a in ls:
            for b in rs:
                best = max(best, nd.val + a + b)
    return best


_p124 = [S.load(k) for k in ("p124", "p124_nonlocal")]
_p124_bad = S.load("p124_wrong")

for spec, want in [
    ([1, [2, None, None], [3, None, None]], 6),
    ([-10, [9, None, None], [20, [15, None, None], [7, None, None]]], 42),
    ([-3, None, None], -3),
    ([2, [-1, None, None], None], 2),
    ([-2, [-1, None, None], None], -1),
]:
    t = _build(spec)
    assert _p124_ref(t) == want, ("P124 ref", spec, _p124_ref(t))
    for sol in _p124:
        assert sol.maxPathSum(_build(spec)) == want, ("P124", spec, sol)

# 錯誤寫法在「路徑不該經過根」時答錯
_bad = _build([-10, [9, None, None], [20, [15, None, None], [7, None, None]]])
assert _p124_bad.maxPathSum(_bad) != 42, "P124 wrong-demo"

for _ in range(4000):
    t = _rand_tree(random.randrange(1, 10))
    want = _p124_ref(t)
    for sol in _p124:
        assert sol.maxPathSum(t) == want, ("P124 random", want, sol)
print("P124 solutions OK")

_P124_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 這題的核心：「回傳給父節點的值」和「答案」是兩件不同的東西。</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="180" cy="72" r="19" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="180" y="77" fill="#ff8a65">-10</text>
              <circle cx="100" cy="142" r="19" fill="none" stroke="var(--text-muted)" stroke-width="2"/><text x="100" y="147" fill="var(--text-muted)">9</text>
              <circle cx="260" cy="142" r="19" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="260" y="147" fill="var(--gold)">20</text>
              <circle cx="205" cy="212" r="19" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="205" y="217" fill="var(--gold)">15</text>
              <circle cx="315" cy="212" r="19" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="315" y="217" fill="var(--gold)">7</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="166" y1="86" x2="114" y2="128"/><line x1="194" y1="86" x2="246" y2="128"/>
            </g>
            <g stroke="var(--gold)" stroke-width="3">
              <line x1="246" y1="156" x2="219" y2="198"/><line x1="274" y1="156" x2="301" y2="198"/>
            </g>
            <text x="380" y="150" fill="var(--gold)" font-size="12" text-anchor="start">答案 = 15 + 20 + 7 = 42</text>
            <text x="380" y="176" fill="var(--text-muted)" font-size="12" text-anchor="start">這條路徑在 20 這裡【拐彎】，</text>
            <text x="380" y="200" fill="var(--text-muted)" font-size="12" text-anchor="start">而且完全【不經過根節點】。</text>
            <line x1="20" y1="250" x2="620" y2="250" stroke="var(--border)"/>
            <text x="20" y="278" fill="var(--accent)" font-size="13">在節點 20 這裡，兩個值同時被算出來：</text>
            <text x="40" y="306" fill="var(--gold)" font-size="12">① 更新答案： 20 + max(15,0) + max(7,0) = 42　　「左 + 我 + 右」，可以拐彎</text>
            <text x="40" y="332" fill="var(--accent)" font-size="12">② 回傳給父： 20 + max(15, 7) = 35　　　　　　「我 + 較好的一邊」，不能拐彎</text>
            <text x="20" y="366" fill="#ff8a65" font-size="12">為什麼回傳時只能選一邊？因為父節點要把它接到【自己這條路徑】上 ——</text>
            <text x="20" y="390" fill="#ff8a65" font-size="12">如果回傳「左+我+右」，父節點接上去就會變成一個有分岔的形狀，那不是一條路徑。</text>
            <text x="20" y="420" fill="var(--gold)" font-size="12">max(gain(kid), 0) 的 0：子樹的貢獻是負的話，寧可不走那一邊（路徑可以只有一個節點）。</text>'''

emit({
 "num": 124, "slug": "binary-tree-maximum-path-sum",
 "en": [
   "A <strong>path</strong> in a binary tree is a sequence of nodes where each pair of adjacent "
   "nodes in the sequence has an edge connecting them. A node can only appear in the sequence "
   "<strong>at most once</strong>. Note that the path does not need to pass through the root.",
   "The <strong>path sum</strong> of a path is the sum of the node's values in the path.",
   "Given the <code>root</code> of a binary tree, return <em>the maximum <strong>path sum</strong> "
   "of any <strong>non-empty</strong> path</em>.",
 ],
 "zh": [
   "二元樹裡的一條<strong>路徑</strong>，是指一串節點，"
   "其中<strong>相鄰的兩個節點之間都有邊相連</strong>，"
   "而且<strong>每個節點最多出現一次</strong>。",
   "<strong>路徑不一定要經過根節點。</strong>",
   "一條路徑的<strong>路徑和</strong>，就是路徑上所有節點值的總和。",
   "給你一個二元樹的根節點 <code>root</code>，"
   "回傳<strong>任意一條非空路徑</strong>的<strong>最大路徑和</strong>。",
 ],
 "pre": [
   ("note", "★ 先搞清楚「路徑」長什麼樣", [
     ("c", """合法的路徑：

    (a) 單一節點                    5

    (b) 一條往下的鏈                5
                                     \\
                                      3
                                       \\
                                        2

    (c) 【在某個節點拐彎】           5
                                   /   \\
                                  3     2      <- 3 -> 5 -> 2

【不合法的】：

    (d) 有分岔的形狀                  5
                                   /  |  \\
                                  3   2   7

        因為那不是「一串相鄰節點」，
        節點 5 會出現兩次（走到 3 再回來走 2 再回來走 7）。

【所以每條路徑「最多在一個節點拐彎」】——

    這個觀察是整題的關鍵：

        每條路徑都有一個【最高點】（離根最近的那個節點），
        在那個點左右兩邊各往下延伸（可以是空的）。

    於是只要【對每個節點，算出「以它為最高點的最佳路徑」】，
    再取全部的最大值，就是答案 ✔"""),
   ]),
   ("note", "★★ 本題真正的考點：回傳值 ≠ 答案", [
     ("c", S["p124_wrong"]),
     ("c", """這段程式碼看起來很合理，但錯得很徹底。

    它回傳 node.val + left + right（「拐彎」的值），
    然後父節點又把這個值接上去 ——

    結果就造出了「有分岔的形狀」，那不是路徑 ✘

    而且它只回傳 gain(root)，
    所以【只能找到「以根為最高點」的路徑】——

    範例 2 的答案 42 完全不經過根，它根本找不到。

【正確的做法要同時維護兩個量】：

    ① 答案（全域）：node.val + left + right
       —— 在這裡拐彎，左右都用上

    ② 回傳值（給父節點）：node.val + max(left, right)
       —— 只能選一邊，因為父節點要接上去

    【把這兩件事分開，是這題（和第 543 題）的全部內容。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,2,3]

          1
         / \\
        2   3

  輸出：6
  說明：2 -> 1 -> 3，和 = 6（在節點 1 拐彎）。

範例 2
  輸入：root = [-10,9,20,null,null,15,7]

          -10
          /  \\
         9    20
             /  \\
            15   7

  輸出：42
  說明：15 -> 20 -> 7 = 42。
        【這條路徑完全不經過根節點 -10。】
        如果硬要經過根：9 + (-10) + (20+15) = 34，比較差。""",
 "constraints": [
   "樹的節點數在 <code>[1, 3 × 10⁴]</code> 之間",
   "−1000 ≤ <code>Node.val</code> ≤ 1000",
 ],
 "mid": [
   ("note", "節點值可以是負數 —— 這是本題的另一半難度", [
     "<strong>所以答案可能是負的</strong>（例如整棵樹只有一個 <code>-3</code>）。",
     "<strong><code>best</code> 一定要初始化成 <code>-inf</code> 而不是 0</strong> —— "
     "<strong>初始化成 0 的話，全負的樹會回傳 0（但題目要求「非空路徑」）。</strong>",
     "而且<strong>「子樹的貢獻是負的就不要」</strong>這個剪枝變得必要 —— "
     "那就是 <code>max(gain(kid), 0)</code> 的那個 <code>0</code>。",
   ]),
 ],
 "idea": [
   ("fig", _P124_FIG, "0 0 640 438"),
   ("c", """gain(node)：「從 node 往下延伸【一條】路徑，最大能拿多少？」

    left  = max(gain(node.left),  0)      負的就不要
    right = max(gain(node.right), 0)

    ① 更新答案（在這裡拐彎）：
        best = max(best, node.val + left + right)

    ② 回傳給父節點（只能選一邊）：
        return node.val + max(left, right)

【為什麼 max(..., 0)？】

    如果左子樹往下最多只能拿 -5，
    那不如【不走左邊】（貢獻 0）。

    因為路徑可以只有一個節點 ——
    「不往那邊延伸」永遠是合法的。

    注意這個 0 不代表「加上一個空節點」，
    而是「這一邊不延伸」。

【為什麼回傳時只能選一邊？】

    父節點會把回傳值接到「自己這條路徑」上。

    如果回傳「左 + 我 + 右」，
    父節點接上去之後，我這個節點就會有三條邊 ——
    那是分岔，不是路徑 ✘

【為什麼 base case 回 0 而不是 -inf？】

    gain(None) 代表「這一邊不延伸」，貢獻就是 0。

    回 -inf 的話，max(gain(None), 0) 還是 0 ——
    所以兩種寫法結果相同。

    但回 0 比較直白：「空的那一邊貢獻 0」。

【複雜度】：每個節點呼叫一次 gain -> O(n) ✔"""),
 ],
 "approaches": [
   ap("解法一", "後序遞迴，同時維護「答案」和「回傳值」（標準答案）", [
     ("c", S["p124"]),
     ("h", "逐行對照範例 2"),
     ("c", """          -10
          /  \\
         9    20
             /  \\
            15   7

gain(9):
    left = right = 0
    best = max(-inf, 9+0+0) = 9
    return 9

gain(15):  best = 15, return 15
gain(7):   best = 15, return 7

gain(20):
    left  = max(15, 0) = 15
    right = max(7, 0)  = 7
    best = max(15, 20+15+7) = 42      ★ 答案在這裡產生
    return 20 + max(15, 7) = 35        ← 只選一邊

gain(-10):
    left  = max(9, 0)  = 9
    right = max(35, 0) = 35
    best = max(42, -10+9+35) = max(42, 34) = 42   ✔ 沒被 34 蓋掉
    return -10 + 35 = 25

答案 42 ✔

【注意 gain(-10) 回傳 25，但那不是答案】——
    答案早在 gain(20) 那一步就被記下來了。

    這就是「全域變數 best」存在的理由：
    答案可能在任何一個節點產生，
    而不一定在最後回傳的那個值裡。"""),
     ("h", "<code>self.best</code> vs <code>nonlocal best</code>"),
     "<strong>兩者等價</strong>。<code>nonlocal</code>（解法二）比較乾淨，"
     "因為<strong>不會把狀態掛在物件上</strong>（LeetCode 的 <code>Solution</code> 實例可能被重用）。",
     "<strong>也可以讓 <code>gain</code> 回傳 tuple <code>(答案, 單邊最大)</code></strong>，"
     "完全避開共享狀態 —— <strong>那是最「函數式」的寫法，但程式碼會長一點。</strong>",
     "<strong>時間 O(n)、空間 O(h)。</strong>",
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊", optimal=True),

   ap("解法二", "<code>nonlocal</code> 版（推薦的寫法）", [
     ("c", S["p124_nonlocal"]),
     ("c", """和解法一完全相同，只是用 nonlocal 取代 self.best。

【為什麼 nonlocal 比較好？】

    LeetCode 會對同一個 Solution 實例呼叫多次
    （不同的測資）。

    用 self.best 的話，如果忘記在函式開頭重設，
    上一筆測資的答案會殘留下來 ——
    這是很隱密的 bug。

    本文的解法一有在開頭寫 self.best = -inf，所以安全。
    但 nonlocal 版【結構上就不可能出這個問題】。

【一般原則】：
    能用區域狀態就不要用物件狀態。
    「作用域越小越好」是減少 bug 最有效的習慣之一。""",),
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "狀態放哪", "備註"],
   [["一、self.best", "O(n)", "O(h)", "物件屬性", "要記得重設"],
    ["二、nonlocal", "O(n)", "O(h)", "閉包", "結構上更安全"]]),
 "post": [
   ("note", "「回傳值 ≠ 答案」這個模式的其他題目", [
     ("c", """共同結構：

    def go(node):
        if not node: return <單位元素>
        L = go(node.left)
        R = go(node.right)
        answer = max(answer, <把 L 和 R 都用上的組合>)   ← 全域答案
        return <只能選一邊的值>                           ← 給父節點

  124  最大路徑和    答案 = 左+根+右       回傳 = 根 + max(左,右)   （本題）
  543  直徑          答案 = 左高+右高      回傳 = 1 + max(左,右)
  687  最長同值路徑  答案 = 左長+右長      回傳 = 1 + max(左,右)
  1373 BST 最大和    答案 = 整棵子樹的和   回傳 = (是否 BST, 和, min, max)

【辨認訊號】：

    「答案可以在任何一個節點『拐彎』，
      但往上傳遞時只能走一條路」

    看到這個形狀，就知道要分開兩個量。

【最常見的錯誤】：
    把「答案」直接回傳給父節點 ——
    那會造出分岔的形狀，而且只找得到「經過根」的答案。"""),
   ]),
 ],
 "edges": [
   "<strong>單一節點</strong> <code>[-3]</code> → <code>-3</code>。"
   "<strong><code>best</code> 初始成 0 會回傳 0 ✘（題目要求非空路徑）。</strong>",
   "<strong>全部是負數</strong> <code>[-2,-1]</code> → <code>-1</code>（只取那個最大的單一節點）。",
   "<strong><code>[1,2,3]</code></strong> → <code>6</code>（在根拐彎）。",
   "<strong><code>[-10,9,20,null,null,15,7]</code></strong> → <code>42</code>。"
   "<strong>答案不經過根 —— 這是本題的核心測資。</strong>",
   "<strong>直接回傳 <code>node.val + left + right</code></strong> → "
   "<strong>造出分岔形狀，而且只找得到經過根的路徑。本題第一名的 bug。</strong>",
   "<strong>忘了 <code>max(gain(kid), 0)</code></strong> → 負的子樹會把答案拉低。",
   "<strong><code>best</code> 初始成 0</strong> → 全負樹回傳 0。",
   "<strong>3 × 10⁴ 個節點的鏈狀樹</strong> → 遞迴深度 3 萬，Python 會 <code>RecursionError</code>。",
 ],
 "follow": [
   ("h", "追問一：如果要輸出「那條路徑」呢？"),
   "<strong>在更新 <code>best</code> 時，記下「是哪個節點、走了哪兩邊」</strong>，"
   "然後<strong>從那個節點往下追</strong>（每步選 <code>gain</code> 較大的孩子）。",
   "<strong>需要額外記錄每個節點的 <code>gain</code> 值</strong>（一個 dict），"
   "<strong>空間從 O(h) 變成 O(n)</strong>。",
   ("h", "追問二：這和第 543 題（直徑）有什麼關係？"),
   ("c", """第 543 題：求「任兩個節點之間最長路徑的【邊數】」

    完全同一個骨架，只是：
        gain 回傳的是「高度」而不是「路徑和」
        答案是「左高 + 右高」而不是「左 + 根 + 右」

    def height(node):
        if not node: return 0
        L, R = height(node.left), height(node.right)
        self.best = max(self.best, L + R)      # 邊數 = 左高 + 右高
        return 1 + max(L, R)

【差別在於「節點值」】：
    543 題每個節點的「值」固定是 1（算邊數），
    而且一定是正的 -> 不需要 max(..., 0) 這個剪枝。

    124 題有負數 -> 必須剪枝。

【所以 543 是 124 的「全部值都是 1」的特例】。
    先弄懂 543，再看 124 會容易很多。""",),
   ("h", "追問三：如果限制「路徑必須經過根節點」呢？"),
   "<strong>那就簡單多了 —— 答案直接就是 <code>root.val + left + right</code></strong>，"
   "<strong>不需要全域變數。</strong>",
   "<strong>「不一定要經過根」這個條件，就是這題從 Medium 變 Hard 的原因。</strong>"
   "<strong>它逼你意識到「答案可能在任何地方產生」。</strong>",
   ("h", "追問四：如果是一般的圖而不是樹呢？"),
   ("c", """在一般的【有環】圖上，
「最大路徑和」（不重複節點）是 NP-hard 的 ——
它包含了「最長路徑問題」，而那個問題本身就是 NP-hard。

    （取全部邊權為 1，就變成「找最長的簡單路徑」，
      而那可以用來解漢米爾頓路徑問題。）

【樹之所以可解，是因為「任兩點之間的路徑唯一」】——
    沒有選擇，也就沒有搜尋空間。

    如果是【有向無環圖（DAG）】，
    最長路徑可以用拓撲排序 + DP 在 O(V+E) 解決。

【「樹 -> 容易、DAG -> 還可以、一般圖 -> NP-hard」
  是圖論問題的常見階梯。】"""),
 ],
 "related": [
   "<strong>第 543 題 Diameter of Binary Tree</strong> —— 本題的「值全是 1」版本，先學這個",
   "<strong>第 687 題 Longest Univalue Path</strong> —— 同一個骨架",
   "<strong>第 110 題 Balanced Binary Tree</strong> —— 「後序回傳一包」的入門",
   "<strong>第 53 題 Maximum Subarray</strong> —— 陣列上的同類問題",
 ],
 "check": [
   "「回傳給父節點的值」和「答案」為什麼是兩件事？各自的公式是什麼？",
   "<code>max(gain(kid), 0)</code> 裡的 <code>0</code> 代表什麼意思？",
   "為什麼 <code>best</code> 不能初始化成 0？",
   "這題和第 543 題（直徑）的骨架一樣，差別在哪裡？",
 ],
})
print("P124 written")

# ==================== 125. Valid Palindrome ====================
S["p125_two"] = '''class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1                      # 左邊跳過非英數字元
            while i < j and not s[j].isalnum():
                j -= 1                      # 右邊跳過非英數字元

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True'''

S["p125_clean"] = '''class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 先過濾再比較：最短，但用了 O(n) 額外空間
        t = [c.lower() for c in s if c.isalnum()]
        return t == t[::-1]'''

S["p125_regex"] = '''import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = re.sub(r'[^a-z0-9]', '', s.lower())
        return t == t[::-1]'''


def _p125_ref(s):
    t = "".join(c.lower() for c in s if c.isalnum())
    return t == t[::-1]


_p125 = [S.load(k) for k in ("p125_two", "p125_clean", "p125_regex")]

for s, want in [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("", True),
    (".,", True),
    ("0P", False),
    ("a.", True),
    ("ab_a", True),
]:
    assert _p125_ref(s) is want, ("P125 ref", s)
    for sol in _p125:
        assert sol.isPalindrome(s) is want, ("P125", s, sol)

_POOL = "abAB01 ,.:;!?_-"
for _ in range(8000):
    s = "".join(random.choice(_POOL) for _ in range(random.randrange(0, 14)))
    want = _p125_ref(s)
    for sol in _p125:
        assert sol.isPalindrome(s) is want, ("P125 random", repr(s), want, sol)
print("P125 solutions OK")

emit({
 "num": 125, "slug": "valid-palindrome",
 "en": [
   "A phrase is a <strong>palindrome</strong> if, after converting all uppercase letters into "
   "lowercase letters and removing all non-alphanumeric characters, it reads the same forward "
   "and backward. Alphanumeric characters include letters and numbers.",
   "Given a string <code>s</code>, return <code>true</code> <em>if it is a <strong>palindrome</strong>, "
   "or </em><code>false</code><em> otherwise</em>.",
 ],
 "zh": [
   "把一個字串裡的<strong>大寫全部轉成小寫</strong>、"
   "並<strong>刪掉所有非英數字元</strong>之後，"
   "如果正著讀和反著讀一樣，它就是<strong>回文</strong>。",
   "（英數字元指的是英文字母和數字。）",
   "給你一個字串 <code>s</code>，判斷它是不是回文。",
 ],
 "pre": [
   ("note", "三個容易忽略的細節", [
     ("c", """1. 【空字串算回文】

   s = " " -> 過濾後變成 "" -> 是回文 -> True ✔

   題目的範例 2 就是這個。

2. 【數字也算「英數字元」】

   s = "0P" -> 過濾後是 "0p" -> 不是回文 -> False

   如果你只保留字母（漏掉數字），
   "0P" 會變成 "p" -> 誤判成 True ✘

   這是 LeetCode 這題的著名陷阱測資。

3. 【底線 _ 不是英數字元】

   Python 的 str.isalnum() 對 "_" 回傳 False ✔

   但如果你用正規表達式 \\w，那會【包含底線】✘

       \\w  =  [a-zA-Z0-9_]     ← 含底線
       正確的應該是 [a-zA-Z0-9]

   s = "ab_a" -> 正確答案是 True（過濾後 "aba"）
                 用 \\w 會得到 "ab_a" -> False ✘

【這三個細節，各自都能讓一份「看起來對」的程式碼掛掉。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "A man, a plan, a canal: Panama"
  輸出：true
  說明：過濾後是 "amanaplanacanalpanama"，正反相同。

範例 2
  輸入：s = "race a car"
  輸出：false
  說明：過濾後是 "raceacar"，反過來是 "racaecar"，不同。

範例 3
  輸入：s = " "
  輸出：true
  說明：過濾後是空字串 ""，空字串是回文。""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 2 × 10⁵",
   "<code>s</code> 只包含可列印的 ASCII 字元",
 ],
 "idea": [
   ("c", """兩條路：

【A. 先過濾再比較】（解法二、三）

    t = 只留英數字元、全轉小寫
    return t == t[::-1]

    兩行，最好懂。
    但要花 O(n) 額外空間存過濾後的字串。

【B. 雙指標原地比較】（解法一）

    i 從左邊、j 從右邊往中間走，
    各自跳過非英數字元，然後比較。

    O(1) 額外空間 ✔

    這是面試官想聽到的答案 ——
    因為它展示你會處理「跳過不要的東西」這個模式。

【雙指標的三個細節】：

    1. 內層跳過迴圈也要寫 i < j
       否則全是標點的字串（例如 ".,"）會越界。

    2. 比較時記得 .lower()
       （或者 .upper()，但兩邊要一致）

    3. 比較完之後 i += 1, j -= 1 不能忘
       否則無窮迴圈。"""),
 ],
 "approaches": [
   ap("解法一", "雙指標（O(1) 空間，標準答案）", [
     ("c", S["p125_two"]),
     ("h", "★ 內層迴圈為什麼也要寫 <code>i &lt; j</code>？"),
     ("c", """while i < j and not s[i].isalnum():
      ^^^^^^^

    考慮 s = ".,"（全是標點）：

    不寫 i < j 的話：
        i 會一路右移，跳過 '.'、','，
        然後 i = 2 -> s[2] 索引越界 ✘

    寫了 i < j：
        i 移到 1 時 i < j 不成立（j 也是 1）-> 停 ✔
        外層 while i < j 也不成立 -> 回 True ✔

【「內層迴圈也要檢查邊界」是雙指標題的通用陷阱】——

    只在外層檢查是不夠的，
    因為內層可能把指標推過頭。

    第 26、27、80、283 題（原地刪除）
    也都有同樣的注意事項。"""),
     ("h", "<code>isalnum()</code> 的 Unicode 行為"),
     ("c", """Python 的 str.isalnum() 是【Unicode 感知】的：

    "ａ".isalnum()   -> True   （全形 a）
    "三".isalnum()   -> True   （中文數字）
    "½".isalnum()    -> True   （分數符號）
    "_".isalnum()    -> False  ✔

    本題保證只有 ASCII，所以沒差。

    但如果輸入可能有 Unicode，
    「英數字元」的定義就要講清楚 ——
    isalnum() 可能比你想的寬鬆很多。

    嚴格只要 ASCII 的話：
        c.isascii() and c.isalnum()

【這種「函式的行為比你以為的寬」的情況，
  在字串處理裡非常常見。
  用之前先想想：它對邊界輸入會怎麼反應？】""",),
     "<strong>時間 O(n)、空間 O(1)。</strong>"
     "<strong>每個字元最多被 <code>i</code> 或 <code>j</code> 訪問一次。</strong>",
   ], "O(n)", "O(1)", "兩個指標各走一遍", "沒有額外空間", optimal=True),

   ap("解法二", "先過濾再比較（最短）", [
     ("c", S["p125_clean"]),
     "<strong>兩行。<code>t == t[::-1]</code> 是 Python 判斷回文最直接的寫法。</strong>",
     ("c", """時間 O(n)、空間 O(n)。

【面試時可以寫，但要主動說】：
    「這用了 O(n) 額外空間，如果要 O(1) 我會用雙指標。」

    然後寫解法一。

【為什麼用 list 而不是字串相加？】

    t = ""
    for c in s:
        if c.isalnum():
            t += c.lower()      ✘ 每次都建立新字串 -> O(n²)

    Python 的字串是不可變的，
    所以 += 會複製整個字串。

    正確的做法是 list 生成式 + "".join()，
    或者像本文一樣直接比較 list（list 也支援 [::-1] 和 ==）。

【「迴圈裡用 += 拼字串」是 Python 最常見的效能陷阱之一。】"""),
   ], "O(n)", "O(n)", "過濾 + 反轉", "過濾後的副本"),

   ap("解法三", "正規表達式（★ 注意 <code>\\w</code> 的陷阱）", [
     ("c", S["p125_regex"]),
     ("h", "★ 為什麼不能用 <code>\\w</code>？"),
     ("c", """re.sub(r'[^a-z0-9]', '', s.lower())    ✔ 正確
re.sub(r'\\W', '', s.lower())           ✘ 會保留底線！

    \\w 的定義是 [a-zA-Z0-9_] —— 【包含底線】。
    \\W 是它的補集，所以 \\W 不會刪掉底線。

    s = "ab_a"
        正確答案：過濾成 "aba" -> True
        用 \\W：  過濾成 "ab_a" -> False ✘

【而且 Python 3 的 \\w 預設是 Unicode 模式】：
    中文、日文、重音字母都算 \\w。

    要限定 ASCII 要加 re.ASCII 旗標：
        re.sub(r'\\W', '', s, flags=re.ASCII)

    ——但那還是會留下底線。

【結論：這題老老實實寫 [^a-z0-9] 最安全。】

    正規表達式很方便，
    但它的「簡寫類別」（\\w \\d \\s）的確切定義
    在不同語言、不同旗標下都不一樣。

    【在乎正確性的地方，寫出完整的字元類別。】"""),
     "<strong>先 <code>lower()</code> 再過濾</strong>，"
     "所以只要寫 <code>[^a-z0-9]</code>（不用寫 <code>A-Z</code>）。"
     "<strong>順序反過來就要寫 <code>[^a-zA-Z0-9]</code>。</strong>",
   ], "O(n)", "O(n)", "正規替換 + 反轉", "過濾後的副本"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "陷阱"],
   [["一、雙指標", "O(n)", "O(1)", "12", "內層要檢查 i < j"],
    ["二、過濾後比較", "O(n)", "O(n)", "2", "不要用 += 拼字串"],
    ["三、正規表達式", "O(n)", "O(n)", "2", "不能用 \\w"]]),
 "edges": [
   "<strong><code>\" \"</code></strong>（一個空格）→ <code>True</code>（過濾後是空字串）。",
   "<strong><code>\".,\"</code></strong>（全是標點）→ <code>True</code>。"
   "<strong>雙指標版的內層迴圈沒檢查 <code>i &lt; j</code> 會索引越界。</strong>",
   "<strong><code>\"0P\"</code></strong> → <code>False</code>。"
   "<strong>只保留字母（漏掉數字）會誤判成 True —— 著名陷阱測資。</strong>",
   "<strong><code>\"ab_a\"</code></strong> → <code>True</code>。"
   "<strong>用 <code>\\w</code> 會誤判成 False。</strong>",
   "<strong><code>\"a.\"</code></strong> → <code>True</code>。",
   "<strong>單一字元</strong> → 永遠是 <code>True</code>。",
   "<strong>忘了 <code>.lower()</code></strong> → <code>\"Aa\"</code> 會誤判成 False。",
   "<strong>忘了 <code>i += 1; j -= 1</code></strong> → 無窮迴圈。",
   "<strong>用 <code>t += c</code> 拼字串</strong> → 2×10⁵ 時 O(n²)，會逾時。",
 ],
 "follow": [
   ("h", "追問一：如果允許刪掉「最多一個字元」呢？"),
   "<strong>第 680 題（驗證回文 II）</strong>。雙指標碰到不相等時，"
   "<strong>試「跳過左邊」和「跳過右邊」兩種，只要其中一種能走完就算過</strong>。",
   ("c", """def validPalindrome(s):
    def ok(i, j):
        while i < j:
            if s[i] != s[j]: return False
            i += 1; j -= 1
        return True

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return ok(i+1, j) or ok(i, j-1)     # 只有這一次機會
        i += 1; j -= 1
    return True

【為什麼只要在「第一次不匹配」時分岔就夠？】

    因為在那之前的所有配對都是相等的 ——
    刪掉它們之中的任何一個，只會破壞已經對好的部分。

    所以最優的刪除位置一定在「第一次衝突」的那兩個之中。

    這是一個很漂亮的貪心論證。""",),
   ("h", "追問二：如果要「最少插入幾個字元才能變成回文」呢？"),
   "<strong>第 1312 題。答案 = <code>n - LPS(s)</code></strong>，"
   "其中 <code>LPS</code> 是<strong>最長回文子序列</strong>（第 516 題）。",
   "<strong>而 <code>LPS(s) = LCS(s, reverse(s))</code></strong> —— "
   "<strong>又回到第 1143 題（最長公共子序列）的二維 DP。</strong>"
   "<strong>「回文」和「和自己的反轉做 LCS」是一組很有用的等價。</strong>",
   ("h", "追問三：<code>isalnum()</code> 在其他語言裡一樣嗎？"),
   ("c", """C 的 isalnum()：只看 ASCII（而且受 locale 影響）
Java 的 Character.isLetterOrDigit()：Unicode 感知
JavaScript：沒有內建，通常用 /[a-z0-9]/i 或 \\p{L}\\p{N}
Python 的 str.isalnum()：Unicode 感知

【所以「英數字元」這個概念在跨語言時完全不可移植。】

    面試時如果用了 isalnum()，
    主動說一句「這在 Python 裡是 Unicode 感知的，
    本題只有 ASCII 所以沒差」——
    會顯示你知道自己在用什麼。""",),
   ("h", "追問四：2×10⁵ 的字串，三種解法實測差多少？"),
   "<strong>通常解法二（過濾後比較）反而最快</strong> —— "
   "<strong>因為 <code>[::-1]</code> 和 <code>==</code> 都是 C 層實作，</strong>"
   "<strong>而雙指標的 Python 迴圈每一步都有直譯器開銷。</strong>",
   "<strong>這是「理論複雜度相同時，常數因子由實作語言決定」的典型例子。</strong>"
   "<strong>但面試要的是 O(1) 空間的那個 —— 因為那才是他們在考的東西。</strong>",
 ],
 "related": [
   "<strong>第 680 題 Valid Palindrome II</strong> —— 允許刪一個字元",
   "<strong>第 5 題 Longest Palindromic Substring</strong> —— 找最長回文子字串",
   "<strong>第 516 題 Longest Palindromic Subsequence</strong> —— 子序列版",
   "<strong>第 234 題 Palindrome Linked List</strong> —— 鏈結串列上的回文",
   "<strong>第 9 題 Palindrome Number</strong> —— 數字版",
 ],
 "check": [
   "空字串為什麼算回文？哪個測資會考這個？",
   "雙指標版的<strong>內層</strong>迴圈為什麼也要檢查 <code>i &lt; j</code>？",
   "為什麼不能用正規表達式的 <code>\\w</code>？",
   "<code>\"0P\"</code> 這個測資在考什麼？",
 ],
})
print("P125 written")
