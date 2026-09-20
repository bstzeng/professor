# -*- coding: utf-8 -*-
"""第 188、189、190、191 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(188)

# ==================== 188. Best Time to Buy and Sell Stock IV ====================
S["p188"] = '''class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0

        # ★ 每筆交易至少佔兩天，所以 k >= n//2 時等於「無限次」
        if k >= n // 2:
            return sum(max(0, b - a) for a, b in zip(prices, prices[1:]))

        # buy[j]  = 完成 j-1 筆交易、且第 j 次已買入時的最大現金
        # sell[j] = 完成 j 筆交易時的最大現金
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)

        for p in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - p)
                sell[j] = max(sell[j], buy[j] + p)

        return sell[k]'''

S["p188_2d"] = '''class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        if k >= n // 2:
            return sum(max(0, b - a) for a, b in zip(prices, prices[1:]))

        # dp[j][i] = 前 i 天、最多 j 筆交易的最大利潤
        dp = [[0] * n for _ in range(k + 1)]

        for j in range(1, k + 1):
            # best = max over m < i of (dp[j-1][m] - prices[m])
            best = dp[j - 1][0] - prices[0]
            for i in range(1, n):
                dp[j][i] = max(dp[j][i - 1], prices[i] + best)
                best = max(best, dp[j - 1][i] - prices[i])

        return dp[k][n - 1]'''


def _p188_ref(k, prices):
    """獨立參考解：枚舉最多 k 段不重疊的區間（只對小輸入）。"""
    n = len(prices)
    best = 0
    for t in range(0, min(k, n // 2) + 1):
        for days in itertools.combinations(range(n), 2 * t):
            profit = 0
            for x in range(t):
                b, s = days[2 * x], days[2 * x + 1]
                profit += prices[s] - prices[b]
            best = max(best, profit)
    return best


_p188 = [S.load(k) for k in ("p188", "p188_2d")]

for k, pr, want in [
    (2, [2, 4, 1], 2),
    (2, [3, 2, 6, 5, 0, 3], 7),
    (0, [1, 3], 0),
    (1, [1], 0),
    (2, [1, 2, 3, 4, 5], 4),
    (100, [3, 2, 6, 5, 0, 3], 7),
]:
    assert _p188_ref(k, pr) == want, ("P188 ref", k, pr, _p188_ref(k, pr))
    for sol in _p188:
        assert sol.maxProfit(k, list(pr)) == want, ("P188", k, pr, want, sol)

for _ in range(1200):
    n = random.randrange(1, 9)
    pr = [random.randint(0, 12) for _ in range(n)]
    k = random.randrange(0, 4)
    want = _p188_ref(k, pr)
    for sol in _p188:
        got = sol.maxProfit(k, list(pr))
        assert got == want, ("P188 random", k, pr, want, got, sol)
# 大輸入：兩種解法互相對照，並和第 122 題的貪心對照
for _ in range(1500):
    pr = [random.randint(0, 100) for _ in range(random.randrange(2, 50))]
    k = random.randrange(0, 30)
    vals = [sol.maxProfit(k, list(pr)) for sol in _p188]
    assert len(set(vals)) == 1, ("P188 disagree", k, pr, vals)
    if k >= len(pr) // 2:
        greedy = sum(max(0, b - a) for a, b in zip(pr, pr[1:]))
        assert vals[0] == greedy, ("P188 vs greedy", k, pr)
print("P188 solutions OK")

_P188_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 把「一筆交易」拆成「買」和「賣」兩個事件，k 筆就是 2k 個狀態，按時間順序串起來。</text>
            <g font-size="12" text-anchor="middle">
              <rect x="40" y="56" width="90" height="30" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="85" y="76" fill="var(--accent)">buy[1]</text>
              <rect x="170" y="56" width="90" height="30" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="215" y="76" fill="var(--gold)">sell[1]</text>
              <rect x="300" y="56" width="90" height="30" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="345" y="76" fill="var(--accent)">buy[2]</text>
              <rect x="430" y="56" width="90" height="30" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="475" y="76" fill="var(--gold)">sell[2]</text>
              <text x="550" y="76" fill="var(--text-muted)">…</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="130" y1="71" x2="164" y2="71"/><polygon points="164,71 156,67 156,75" fill="var(--border)"/>
              <line x1="260" y1="71" x2="294" y2="71"/><polygon points="294,71 286,67 286,75" fill="var(--border)"/>
              <line x1="390" y1="71" x2="424" y2="71"/><polygon points="424,71 416,67 416,75" fill="var(--border)"/>
            </g>
            <text x="20" y="116" fill="var(--accent)" font-size="12">buy[j]　= max(buy[j],　sell[j−1] − p)　　用「完成 j−1 筆之後的錢」去買第 j 次</text>
            <text x="20" y="142" fill="var(--gold)" font-size="12">sell[j] = max(sell[j], buy[j]　　+ p)　　賣掉第 j 次</text>
            <line x1="20" y1="168" x2="620" y2="168" stroke="var(--border)"/>
            <text x="20" y="196" fill="#ff8a65" font-size="13">★ 關鍵優化：k 很大時要退化成貪心</text>
            <text x="40" y="226" fill="var(--text-muted)" font-size="12">每筆交易至少要佔兩天（一天買、一天賣），所以最多只能做 ⌊n/2⌋ 筆。</text>
            <text x="40" y="254" fill="var(--gold)" font-size="12">k ≥ n/2 時，「最多 k 筆」等於「無限次」→ 直接用第 122 題的貪心，O(n) ✔</text>
            <text x="40" y="284" fill="#ff8a65" font-size="12">沒有這個優化的話，題目給 k = 10⁹ 時 O(nk) 會直接爆掉。</text>
            <line x1="20" y1="308" x2="620" y2="308" stroke="var(--border)"/>
            <text x="20" y="336" fill="var(--accent)" font-size="13">★ 為什麼內層 j 可以正著跑？</text>
            <text x="40" y="366" fill="var(--text-muted)" font-size="12">buy[j] 用到 sell[j−1]（這一輪已經更新過的值）——</text>
            <text x="40" y="392" fill="var(--text-muted)" font-size="12">這代表「第 j−1 筆和第 j 筆可以在同一天完成」。</text>
            <text x="40" y="420" fill="var(--gold)" font-size="12">同一天買又賣的利潤是 0，不會讓答案變大 → 無害，而且剛好涵蓋「用不滿 k 筆」的情況 ✔</text>'''

emit({
 "num": 188, "slug": "best-time-to-buy-and-sell-stock-iv",
 "en": [
   "You are given an integer array <code>prices</code> where <code>prices[i]</code> is the price "
   "of a given stock on the <code>i</code><sup>th</sup> day, and an integer <code>k</code>.",
   "Find the maximum profit you can achieve. You may complete at most <code>k</code> "
   "transactions: i.e. you may buy at most <code>k</code> times and sell at most <code>k</code> "
   "times.",
   "<strong>Note:</strong> You may not engage in multiple transactions simultaneously (i.e., you "
   "must sell the stock before you buy again).",
 ],
 "zh": [
   "給你一個陣列 <code>prices</code>（第 <code>i</code> 天的股價）和一個整數 <code>k</code>。",
   "求你能獲得的最大利潤，但<strong>最多只能完成 <code>k</code> 筆交易</strong>。",
   "<strong>注意：</strong>不能同時持有多筆 —— 必須先賣掉才能再買。",
 ],
 "pre": [
   ("note", "★ 這是「買賣股票」系列的通用版", [
     ("c", """121（一次）    = 本題的 k = 1
122（無限次）  = 本題的 k = ∞
123（最多兩次）= 本題的 k = 2
188（本題）    = 任意 k

【所以這題的解法可以解掉前面三題】——
    寫一份程式碼，四題通用 ✔

【狀態機的推廣】

    第 123 題用四個變數（buy1, sell1, buy2, sell2）。

    這題把它們換成兩個長度 k+1 的陣列：

        buy[j]  = 完成 j-1 筆交易、且第 j 次已買入時的最大現金
        sell[j] = 完成 j 筆交易時的最大現金

    for p in prices:
        for j in 1..k:
            buy[j]  = max(buy[j],  sell[j-1] - p)
            sell[j] = max(sell[j], buy[j]    + p)

    答案是 sell[k]。

【★ 但直接這樣寫會超時】

    複雜度 O(nk)。

    題目的 k 可以到 10^9 —— 那是 10^14 次運算 ✘

    【所以必須加上一個關鍵優化】，見下方。"""),
   ]),
   ("note", "★ 關鍵優化：k ≥ n/2 時退化成貪心", [
     ("c", """【每筆交易至少佔兩天】（一天買、一天賣，不能同一天）。

    所以 n 天最多只能做 ⌊n/2⌋ 筆交易。

    如果 k >= n//2，那「最多 k 筆」這個限制【等於沒有限制】——

    -> 直接用第 122 題的貪心：
       把所有上漲的日子加起來，O(n) ✔

【沒有這個優化會怎樣？】

    k = 10^9, n = 1000
    -> O(nk) = 10^12 ✘ 直接超時

    加上之後：
        k >= 500 -> 走貪心 O(n)
        k <  500 -> 走 DP  O(nk) <= 500 × 1000 = 5×10^5 ✔

    【兩條路都很快。】

【這種「參數大到某個門檻就退化」的優化，
  在 DP 題裡很常見】：

    - 背包問題：容量超過所有物品總重時，全部裝進去
    - 第 322 題（零錢兌換）：金額很小時直接暴力
    - 本題：k 超過 n/2 時限制失效

    【看到「參數範圍異常大」時，先問自己：
      「它大到什麼程度就沒有意義了？」】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：k = 2, prices = [2,4,1]
  輸出：2
  說明：第 1 天買（2），第 2 天賣（4），利潤 2。
        只做一筆就夠了（「最多兩筆」不代表要做滿）。

範例 2
  輸入：k = 2, prices = [3,2,6,5,0,3]
  輸出：7
  說明：第 2 天買（2）第 3 天賣（6），賺 4
        第 5 天買（0）第 6 天賣（3），賺 3
        總共 7。""",
 "constraints": [
   "1 ≤ <code>k</code> ≤ 100",
   "1 ≤ <code>prices.length</code> ≤ 1000",
   "0 ≤ <code>prices[i]</code> ≤ 1000",
 ],
 "mid": [
   ("note", "本題的 k ≤ 100，但那個優化仍然重要", [
     "<strong>k = 100、n = 1000 時，O(nk) = 10⁵ —— 其實不加優化也能過。</strong>",
     "<strong>但「k ≥ n/2 就退化」這個觀察本身是這題的核心洞察</strong>，"
     "而且<strong>它讓同一份程式碼能處理 k = ∞（第 122 題）</strong>。",
     "<strong>面試時一定要說出來</strong> —— 那是面試官在找的東西。",
   ]),
 ],
 "idea": [
   ("fig", _P188_FIG, "0 0 640 444"),
   ("c", """【狀態】

    buy[j]  = 「完成 j-1 筆交易、目前持有第 j 次買進的股票」時的最大現金
    sell[j] = 「完成 j 筆交易、目前空手」時的最大現金

【轉移】

    buy[j]  = max(buy[j],  sell[j-1] - p)
              ^^^^^^       ^^^^^^^^^^^^^
              昨天就持股    今天才買（用完成 j-1 筆之後的錢）

    sell[j] = max(sell[j], buy[j] + p)
              ^^^^^^^      ^^^^^^^^^^
              昨天就空手    今天賣掉第 j 筆

【初始值】

    buy[j] = -inf   （一開始不可能已經持股）
    sell[j] = 0     （一筆都沒做，現金 0）

    sell[0] = 0 特別重要 —— buy[1] 要用它 ✔

【答案】sell[k]

    （sell[k] >= sell[k-1] >= ... >= sell[0] = 0，
      所以「用不滿 k 筆」的情況自動被涵蓋 ✔）

【★ 內層 j 為什麼可以正著跑？】

    buy[j] 用到 sell[j-1] ——
    那是【這一輪已經更新過】的值。

    這代表「第 j-1 筆和第 j 筆可以在【同一天】完成」。

    而「同一天買又賣」的利潤是 0，
    不會讓答案變大 -> 無害 ✔

    倒著跑也對（那樣用的是上一輪的 sell[j-1]，
    語意變成「不能同日」）—— 答案相同。

【複雜度】

    k >= n//2 -> O(n)
    否則      -> O(nk)，而 k < n/2 -> O(n²) 上界

    n = 1000 -> 最多 5×10^5，輕鬆 ✔"""),
 ],
 "approaches": [
   ap("解法一", "2k 個狀態變數（標準答案）", [
     ("c", S["p188"]),
     "<strong>十五行，一份程式碼解掉第 121、122、123、188 四題。</strong>",
     ("h", "★ 三個必須寫對的地方"),
     ("c", """1. 【k >= n//2 時退化成貪心】

   不寫的話，k 很大時會超時。
   而且這一行讓程式碼能處理「k = 無限」的情況。

2. 【sell[0] = 0】

   buy[1] = max(buy[1], sell[0] - p) = max(buy[1], -p)

   sell[0] 代表「零筆交易」的現金 -> 0 ✔

   陣列 sell = [0] * (k+1) 自動處理了 ✔

3. 【n < 2 或 k == 0 要擋】

   n < 2：一天以內不可能交易
   k == 0：不准交易

   兩個都回 0。

   不擋的話：
       n = 1 時 zip(prices, prices[1:]) 是空的 -> sum = 0 ✔ 其實也對
       k = 0 時 range(1, 1) 是空的 -> sell[0] = 0 ✔ 也對

   所以其實不擋也不會錯，但寫了更明確。""",),
     ("h", "為什麼 <code>buy</code> 初始成 <code>-inf</code>？"),
     "<strong>因為「一開始就持股」是不可能的狀態。</strong>",
     "<strong>用 <code>-inf</code> 保證第一次的 <code>max</code> 一定取到 <code>sell[j-1] - p</code> ✔</strong>",
     "<strong>初始成 0 的話，會讓「不花錢就持股」變成合法狀態 → 答案偏大。</strong>",
   ], "O(n·k) / O(n)", "O(k)", "k 大時退化成 O(n)", "兩個長度 k 的陣列", optimal=True),

   ap("解法二", "二維 DP + 「最佳買入點」優化", [
     ("c", S["p188_2d"]),
     ("h", "從 O(n²k) 優化到 O(nk)"),
     ("c", """【最直白的二維 DP】：

    dp[j][i] = 前 i 天、最多 j 筆交易的最大利潤

    dp[j][i] = max(dp[j][i-1],                       今天不賣
                   max over m<i of
                       (prices[i] - prices[m] + dp[j-1][m]))   今天賣

    內層的 max over m 要 O(n) -> 總共 O(n²k) ✘

【優化：把 max over m 提出來增量維護】

    prices[i] - prices[m] + dp[j-1][m]
      = prices[i] + (dp[j-1][m] - prices[m])
                    ^^^^^^^^^^^^^^^^^^^^^^^
                    和 i 無關！

    所以維護：
        best = max over m < i of (dp[j-1][m] - prices[m])

    每次 i 往前走時，best = max(best, dp[j-1][i] - prices[i]) ✔

    -> 內層變成 O(1) -> 總共 O(nk) ✔

【★ 這個「把不含 i 的部分提出來」的技巧非常通用】：

    看到 max/min over m of (f(i) + g(m))，
    就把 g(m) 的最佳值增量維護起來。

    第 121 題（記錄歷史最低價）就是它的最簡形式：
        best = max over m of (-prices[m])

    第 123 題、本題、
    以及很多「區間 DP 的優化」都用這一招。

【這個版本的空間是 O(nk)】（二維表），
    比解法一差 —— 但它展示了「怎麼從樸素的 DP 優化過來」，
    在面試裡講出這個推導過程很有價值。""",),
   ], "O(n·k)", "O(n·k)", "增量維護最佳買入點", "二維表"),
 ],
 "compare": (["解法", "時間", "空間", "能解哪幾題", "備註"],
   [["一、2k 個狀態", "O(nk) / O(n)", "O(k)", "121/122/123/188", "標準答案"],
    ["二、二維 DP + 優化", "O(nk)", "O(nk)", "123/188", "展示優化推導"]]),
 "edges": [
   "<strong><code>k = 0</code></strong> → <code>0</code>（不准交易）。",
   "<strong>只有一天</strong> → <code>0</code>。",
   "<strong><code>k = 2, prices = [2,4,1]</code></strong> → <code>2</code>。"
   "<strong>「最多兩筆」不代表要做滿。</strong>",
   "<strong>一路下跌</strong> → <code>0</code>。<strong><code>sell</code> 初始成 0 保證這一點。</strong>",
   "<strong><code>k</code> 很大</strong>（<code>k ≥ n/2</code>）→ 退化成第 122 題的貪心。"
   "<strong>沒有這個優化，<code>k = 10⁹</code> 時會超時。</strong>",
   "<strong><code>buy</code> 初始成 0 而不是 <code>-inf</code></strong> → "
   "<strong>「不花錢就持股」變成合法，答案偏大。</strong>",
   "<strong>忘了 <code>sell[0] = 0</code></strong> → <code>buy[1]</code> 算錯。",
   "<strong>k = 100、n = 1000</strong> → O(nk) = 10⁵，輕鬆。",
 ],
 "follow": [
   ("h", "追問一：這一份程式碼怎麼解掉第 121、122、123 題？"),
   ("c", """第 121 題（一次）：   maxProfit(1, prices)
第 122 題（無限次）： maxProfit(len(prices)//2, prices)
                     （或直接走貪心那一支）
第 123 題（兩次）：   maxProfit(2, prices)
第 188 題（k 次）：   maxProfit(k, prices)

【一份程式碼，四題通用 ✔】

【但每一題還是有它自己的「最佳解」】：

    121：一趟掃描記最低價 —— O(n)、O(1)，最短
    122：貪心加漲幅 —— 一行
    123：四個變數 —— 不用陣列

    通用版的常數比較大（陣列存取、內層迴圈）。

【面試時的策略】：

    先寫該題的最佳解（展示你看出了特殊結構），
    再說「這其實是 k 次交易的特例，通用版是這樣」。

    兩邊都照顧到 ✔""",),
   ("h", "追問二：如果加上「手續費」或「冷凍期」呢？"),
   ("c", """【手續費（第 714 題）】：

    sell[j] = max(sell[j], buy[j] + p - fee)

    一個減號 ✔

【冷凍期（第 309 題）】：

    需要第三個狀態（「今天剛賣掉」），
    而且 buy 不能用「剛賣完」的 sell：

        new_buy[j]  = max(buy[j], cool[j-1] - p)
        new_cool[j] = sell[j]           （昨天賣掉的，今天冷凍）
        new_sell[j] = max(sell[j], buy[j] + p)

    【而且一定要用「上一輪的值」】——
    不能像本題那樣在同一輪裡串接 ✘

    （因為「同一天賣了又買」在有冷凍期時是非法的。）

【這是本題「內層 j 可以正著跑」那個論證的邊界】：

    它成立的前提是「同日買賣是合法的、而且利潤 0」。

    冷凍期打破了這個前提 -> 論證失效 ✔

    【所以「這個優化在什麼條件下成立」比
      「這個優化長什麼樣」更重要。】""",),
   ("h", "追問三：「把不含 i 的部分提出來」還能用在哪？"),
   ("ul", [
     "<strong>第 121 題</strong>：<code>best = max(-prices[m])</code> —— 就是歷史最低價",
     "<strong>第 123 題</strong>：四個變數的 <code>buy2 = max(buy2, sell1 - p)</code> 就是把 <code>sell1</code> 當成增量維護的 <code>g(m)</code>",
     "<strong>第 1014 題 最佳觀光組合</strong>：<code>values[i]+values[j]+i-j</code> "
     "拆成 <code>(values[i]+i) + (values[j]-j)</code>",
     "<strong>第 121/122/123/188 題</strong>：本系列",
     "<strong>單調佇列優化 DP</strong>：當「最佳的 m」有範圍限制時",
   ]),
   ("c", """【一般形式】：

    dp[i] = max over m<i of (f(i) + g(m))
          = f(i) + max over m<i of g(m)

    只要 f 和 g 可以分離，
    就能把 O(n) 的內層降到 O(1) ✔

【如果 m 有範圍限制（例如 i-k <= m < i）】：

    那就要用【單調佇列】維護滑動視窗的最大值
    -> 仍然是攤還 O(1)

    第 239 題（滑動視窗最大值）、
    第 1425 題（帶限制的子序列和）用的是這一招。

【辨認訊號】：

    DP 的轉移式裡有「max/min over 某個範圍」
    -> 問自己「被 max 的東西能不能拆成 f(i) + g(m)？」

    能拆 -> 增量維護 g 的最佳值
    不能 -> 可能要用其他優化（斜率優化、四邊形不等式…）""",),
   ("h", "追問四：為什麼「每筆交易至少佔兩天」？"),
   ("c", """因為題目說「不能同時持有多筆」——
    必須先賣掉才能再買。

    而「買」和「賣」不能是同一天嗎？

    【其實可以】（第 122 題明確允許），
    但那樣的利潤是 0 —— 沒有意義。

    所以【有意義的交易】至少要跨兩天 ✔

    n 天最多有 ⌊n/2⌋ 筆有意義的交易。

【嚴格一點的論證】：

    每筆有意義的交易佔用「一個買入日」和「一個賣出日」，
    而且這些日子【互不重疊】（不能同時持有多筆）。

    n 天最多能配出 ⌊n/2⌋ 對 ✔

【所以 k >= n//2 時，限制確實失效】。

    注意是 n//2 而不是 (n-1)//2 或 n//2 + 1 ——
    邊界要驗算：

        n = 4: 最多 2 筆（第 0 天買第 1 天賣，第 2 天買第 3 天賣）✔
               4 // 2 = 2 ✔
        n = 5: 最多 2 筆 ✔ 5 // 2 = 2 ✔

    ✔ 正確""",),
 ],
 "related": [
   "<strong>第 121/122/123 題</strong> —— k = 1 / ∞ / 2 的特例",
   "<strong>第 309 題 含冷凍期</strong> —— 需要第三個狀態",
   "<strong>第 714 題 含手續費</strong> —— 一個減號",
   "<strong>第 1014 題 最佳觀光組合</strong> —— 同樣的「拆成 f(i)+g(m)」",
 ],
 "check": [
   "<code>k ≥ n//2</code> 時為什麼可以退化成貪心？「每筆至少兩天」怎麼論證？",
   "<code>buy[j]</code> 為什麼要初始成 <code>-inf</code>？",
   "內層 <code>j</code> 正著跑代表什麼語意？為什麼無害？",
   "解法二怎麼把 O(n²k) 優化成 O(nk)？",
 ],
})
print("P188 written")
