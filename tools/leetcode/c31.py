# -*- coding: utf-8 -*-
"""第 31–33 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(31)

# ==================== 31. Next Permutation ====================
S["p31"] = '''class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # 第 1 步：從右往左找第一個「下降點」i，滿足 nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 第 2 步：若找到了，在 i 右邊找「剛好比 nums[i] 大」的最小值，交換
        if i >= 0:
            # i 右邊是非遞增的，所以從右往左第一個 > nums[i] 的就是答案
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 第 3 步：把 i 右邊反轉（從非遞增變成非遞減 = 最小）
        # 若第 1 步沒找到（i == -1），整個反轉 -> 回到最小的排列
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1'''

_p31 = S.load("p31")


def _p31_ref(nums):
    """用「列出所有排列」的方式求下一個 —— 只能用在小陣列上。"""
    perms = sorted(set(itertools.permutations(nums)))
    cur = tuple(nums)
    idx = perms.index(cur)
    return list(perms[(idx + 1) % len(perms)])


for c in [[1, 2, 3], [3, 2, 1], [1, 1, 5], [1], [1, 3, 2], [2, 3, 1],
          [1, 5, 1], [5, 4, 7, 5, 3, 2]]:
    a = list(c)
    _p31.nextPermutation(a)
    assert a == _p31_ref(c), ("P31", c, a, _p31_ref(c))
for _ in range(3000):
    c = [random.randint(1, 3) for _ in range(random.randint(1, 6))]
    a = list(c)
    _p31.nextPermutation(a)
    assert a == _p31_ref(c), ("P31", c, a, _p31_ref(c))
print("P31 solutions OK")

_P31_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">nums = [1, 5, 8, 4, 7, 6, 5, 3, 1] 的下一個排列</text>
            <text x="20" y="50" fill="var(--text-muted)" font-size="12">步驟 1：從右往左找第一個「下降點」</text>
            <g font-size="14" text-anchor="middle">
              <rect x="40" y="64" width="54" height="36" rx="5" fill="none" stroke="var(--border)"/><text x="67" y="88" fill="var(--text-muted)">1</text>
              <rect x="102" y="64" width="54" height="36" rx="5" fill="none" stroke="var(--border)"/><text x="129" y="88" fill="var(--text-muted)">5</text>
              <rect x="164" y="64" width="54" height="36" rx="5" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="191" y="88" fill="var(--gold)">4</text>
              <rect x="226" y="64" width="54" height="36" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="253" y="88" fill="var(--accent)">7</text>
              <rect x="288" y="64" width="54" height="36" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="315" y="88" fill="var(--accent)">6</text>
              <rect x="350" y="64" width="54" height="36" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="377" y="88" fill="#ff8a65">5</text>
              <rect x="412" y="64" width="54" height="36" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="439" y="88" fill="var(--accent)">3</text>
              <rect x="474" y="64" width="54" height="36" rx="5" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="501" y="88" fill="var(--accent)">1</text>
            </g>
            <text x="191" y="118" fill="var(--gold)" font-size="11" text-anchor="middle">i（4 &lt; 7）</text>
            <text x="377" y="118" fill="#ff8a65" font-size="11" text-anchor="middle">j（最右邊 &gt; 4 的）</text>
            <text x="560" y="88" fill="var(--text-muted)" font-size="11">← 這段非遞增</text>
            <text x="20" y="150" fill="var(--text-muted)" font-size="12">步驟 2：交換 nums[i] 與 nums[j]</text>
            <g font-size="14" text-anchor="middle">
              <rect x="40" y="164" width="54" height="36" rx="5" fill="none" stroke="var(--border)"/><text x="67" y="188" fill="var(--text-muted)">1</text>
              <rect x="102" y="164" width="54" height="36" rx="5" fill="none" stroke="var(--border)"/><text x="129" y="188" fill="var(--text-muted)">5</text>
              <rect x="164" y="164" width="54" height="36" rx="5" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="191" y="188" fill="var(--gold)">5</text>
              <rect x="226" y="164" width="54" height="36" rx="5" fill="none" stroke="var(--accent)"/><text x="253" y="188" fill="var(--accent)">7</text>
              <rect x="288" y="164" width="54" height="36" rx="5" fill="none" stroke="var(--accent)"/><text x="315" y="188" fill="var(--accent)">6</text>
              <rect x="350" y="164" width="54" height="36" rx="5" fill="none" stroke="var(--accent)"/><text x="377" y="188" fill="var(--accent)">4</text>
              <rect x="412" y="164" width="54" height="36" rx="5" fill="none" stroke="var(--accent)"/><text x="439" y="188" fill="var(--accent)">3</text>
              <rect x="474" y="164" width="54" height="36" rx="5" fill="none" stroke="var(--accent)"/><text x="501" y="188" fill="var(--accent)">1</text>
            </g>
            <text x="377" y="218" fill="var(--text-muted)" font-size="11" text-anchor="middle">交換後這段「仍然」非遞增</text>
            <text x="20" y="250" fill="var(--text-muted)" font-size="12">步驟 3：把 i 右邊整段反轉 → 變成該前綴下最小的排列</text>
            <g font-size="14" text-anchor="middle">
              <rect x="40" y="264" width="54" height="36" rx="5" fill="none" stroke="var(--border)"/><text x="67" y="288" fill="var(--text-muted)">1</text>
              <rect x="102" y="264" width="54" height="36" rx="5" fill="none" stroke="var(--border)"/><text x="129" y="288" fill="var(--text-muted)">5</text>
              <rect x="164" y="264" width="54" height="36" rx="5" fill="none" stroke="var(--gold)" stroke-width="2.5"/><text x="191" y="288" fill="var(--gold)">5</text>
              <rect x="226" y="264" width="54" height="36" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="253" y="288" fill="#ff8a65">1</text>
              <rect x="288" y="264" width="54" height="36" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="315" y="288" fill="#ff8a65">3</text>
              <rect x="350" y="264" width="54" height="36" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="377" y="288" fill="#ff8a65">4</text>
              <rect x="412" y="264" width="54" height="36" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="439" y="288" fill="#ff8a65">6</text>
              <rect x="474" y="264" width="54" height="36" rx="5" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="501" y="288" fill="#ff8a65">7</text>
            </g>
            <text x="20" y="326" fill="var(--gold)" font-size="12">答案：[1, 5, 5, 1, 3, 4, 6, 7]　整個過程 O(n) 時間、O(1) 空間，只用交換與反轉。</text>'''

emit({
 "num": 31, "slug": "next-permutation",
 "en": [
   "A <strong>permutation</strong> of an array of integers is an arrangement of its members "
   "into a sequence or linear order.",
   "The <strong>next permutation</strong> of an array of integers is the next "
   "lexicographically greater permutation of its integer. If such an arrangement is not "
   "possible, the array must be rearranged as the lowest possible order "
   "(i.e., sorted in ascending order).",
   "Given an array of integers <code>nums</code>, <em>find the next permutation of "
   "<code>nums</code></em>. The replacement must be <strong>in place</strong> and use only "
   "constant extra memory.",
 ],
 "zh": [
   "一個整數陣列的<strong>排列</strong>，就是把它的元素排成某個順序。",
   "<strong>下一個排列</strong>指的是：在所有排列按<strong>字典序</strong>排好之後，"
   "緊接在目前這個排列後面的那一個。"
   "如果目前已經是最大的排列（完全遞減），就把它變成<strong>最小的排列</strong>（升序）。",
   "請<strong>原地</strong>修改 <code>nums</code>，而且只能用<strong>常數額外空間</strong>。",
 ],
 "pre": [
   ("note", "先用小例子建立直覺", [
     ("c", """[1,2,3] 的所有排列按字典序排：

    123  ->  132  ->  213  ->  231  ->  312  ->  321  ->  (回到 123)

觀察每一次「進位」發生了什麼：

    123 -> 132 ：最後兩位交換（3 和 2）
    132 -> 213 ：從右邊找不到可以小幅調整的了，
                  只好動第 0 位：1 換成 2，後面補最小 -> 213
    231 -> 312 ：同理，2 換成 3，後面補最小 -> 312
    321 -> 123 ：已經是最大，整個重來

這很像十進位數字加一：
    從個位開始往上找「還能變大的那一位」，
    把它變大一點點，然後後面全部歸零（變成最小）。

差別在於：這裡不能隨便填，只能用手上現有的數字重排。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3]
  輸出：[1,3,2]

範例 2
  輸入：nums = [3,2,1]
  輸出：[1,2,3]
  說明：已經是最大的排列，回到最小。

範例 3
  輸入：nums = [1,1,5]
  輸出：[1,5,1]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 100",
   "0 ≤ <code>nums[i]</code> ≤ 100",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>值可以重複</strong>（<code>[1,1,5]</code>）。"
       "這會影響第 2 步的比較要用 <code>&lt;=</code> 還是 <code>&lt;</code> —— 見下面的說明。",
       "<strong>必須原地、常數空間</strong>。"
       "所以不能「生成所有排列再找下一個」（那是 O(n!)），"
       "也不能複製一份陣列出來排序。",
       "<strong>長度可以是 1</strong>。此時只有一種排列，答案就是它自己。"
       "程式要能正確處理（第 1 步找不到下降點，第 3 步反轉長度 1 的區段，等於沒動）。",
     ]),
   ]),
 ],
 "idea": [
   "<strong>三個步驟，每一步都有明確的理由。</strong>",
   ("fig", _P31_FIG, "0 0 640 340"),
 ],
 "approaches": [
   ap("解法", "找下降點 → 交換 → 反轉尾段（唯一解）", [
     ("c", S["p31"]),
     ("h", "步驟 1：為什麼要找「從右往左第一個下降點」？"),
     ("c", """設 i 是「最右邊」滿足 nums[i] < nums[i+1] 的位置。

這表示 nums[i+1..n-1] 這一段是「非遞增」的
（否則會有更右邊的下降點）。

非遞增 = 這一段已經是它自己所有排列裡「最大」的那個
       = 光動這一段沒辦法變得更大

所以「要變大」就一定得動到 nums[i] 或更左邊。
而我們要的是「下一個」（最小的變大），
所以動到的位置要「越右邊越好」-> 就是 i。

例：[1,5,4,7,6,5,3,1]
    從右往左：1<3? 否。3<5? 否。5<6? 否。6<7? 否。7>4 -> i 指向 4
    所以 i = 2（值 4），右邊 [7,6,5,3,1] 是非遞增的 ✔"""),
     ("h", "步驟 2：為什麼從右往左找第一個 &gt; nums[i] 的？"),
     ("c", """我們要把 nums[i] 換成「右邊比它大的數裡，最小的那一個」。

因為 nums[i+1..] 是「非遞增」的，
從右往左掃的時候數字是「非遞減」的，
所以第一個碰到的 > nums[i] 的，就是「大於 nums[i] 的最小值」。

    [7, 6, 5, 3, 1]，要找 > 4 的最小值
    從右往左：1 ✘  3 ✘  5 ✔  -> 就是 5

不需要排序，也不需要二分 —— 單調性已經送給我們了。

為什麼條件寫 nums[j] <= nums[i] 而不是 <？
    因為要找「嚴格大於」nums[i] 的。
    遇到相等的要繼續往左走。

    [1, 5, 1]：i = 0（1 < 5），
    從右往左找 > 1 的：nums[2]=1 <= 1 跳過，nums[1]=5 > 1 ✔
    交換 -> [5, 1, 1]，反轉後面 -> [5, 1, 1]

    如果誤寫成 <，j 會停在 nums[2]=1，
    交換後還是 [1,5,1]，完全沒變。"""),
     ("h", "步驟 3：為什麼交換之後直接反轉就對了？"),
     ("c", """關鍵引理：交換之後，nums[i+1..] 仍然是「非遞增」的。

為什麼？
  原本 nums[i+1..] 非遞增，而 nums[j] 是「> nums[i] 的最小值」。
  換進去的 nums[i]（舊值）滿足：
      nums[j-1] >= nums[j] > nums[i] >= nums[j+1]
      （最後一個不等式：因為 j 是從右往左「第一個」> nums[i] 的，
        所以 j 右邊的全都 <= nums[i]）
  把 nums[i] 放到位置 j，剛好塞在正確的位置上，
  非遞增的性質完好無損。

既然它是非遞增（= 最大的排法），
我們要「後面補最小」，
反轉一下就變成非遞減（= 最小的排法）。

不需要排序！反轉是 O(n)，排序是 O(n log n)。"""),
     ("h", "步驟 1 找不到下降點的情況"),
     "表示整個陣列是非遞增的（例如 <code>[3,2,1]</code>），已經是最大的排列。"
     "此時 <code>i == -1</code>，第 2 步被 <code>if i &gt;= 0</code> 跳過，"
     "第 3 步的 <code>left = i + 1 = 0</code> —— <strong>整個陣列反轉</strong>，"
     "剛好變成最小的排列。"
     "<strong>一個變數同時處理了正常情況和邊界情況，非常漂亮。</strong>",
   ], "O(n)", "O(1)", "最多掃三遍", "只用幾個下標", optimal=True),
 ],
 "compare": (["步驟", "做什麼", "為什麼", "複雜度"],
   [["1. 找下降點 i", "從右往左找 <code>nums[i] &lt; nums[i+1]</code>",
     "i 右邊非遞增 = 已是最大，必須動 i", "O(n)"],
    ["2. 找 j 並交換", "從右往左找第一個 <code>&gt; nums[i]</code>",
     "非遞增保證它是「大於 nums[i] 的最小值」", "O(n)"],
    ["3. 反轉 i 右邊", "頭尾對調", "把非遞增變成非遞減 = 最小", "O(n)"]]),
 "post": [
   ("note", "這就是 C++ 的 std::next_permutation", [
     "C++ 標準庫的 <code>std::next_permutation</code> 就是這個演算法，"
     "而且它回傳一個 bool 表示「有沒有繞回最小」。",
     ("c", """// C++ 的標準用法：列出所有排列
std::sort(v.begin(), v.end());       // 先排成最小
do {
    process(v);
} while (std::next_permutation(v.begin(), v.end()));

先排序很重要 —— 否則會從中間開始，繞一圈就停，
漏掉字典序比初始值小的那些排列。

Python 沒有內建的 next_permutation，
itertools.permutations 是「一次全部生成」，
在 n 大的時候會爆記憶體（除非用它的惰性特性）。"""),
   ]),
 ],
 "edges": [
   "<strong>已經是最大</strong>：<code>[3,2,1]</code> → <code>[1,2,3]</code>。<code>i == -1</code> 的路徑。",
   "<strong>單一元素</strong>：<code>[1]</code> → <code>[1]</code>。",
   "<strong>兩個元素</strong>：<code>[1,2]</code> → <code>[2,1]</code>；<code>[2,1]</code> → <code>[1,2]</code>。",
   "<strong>有重複值</strong>：<code>[1,1,5]</code> → <code>[1,5,1]</code>；<code>[1,5,1]</code> → <code>[5,1,1]</code>。"
   "步驟 2 的 <code>&lt;=</code> 寫成 <code>&lt;</code> 會在這裡出錯。",
   "<strong>全部相同</strong>：<code>[2,2,2]</code> → <code>[2,2,2]</code>。找不到下降點，反轉後還是一樣。",
   "<strong>只有最後兩個要換</strong>：<code>[1,2,3]</code> → <code>[1,3,2]</code>。i 在倒數第二格。",
   "<strong>複雜的情況</strong>：<code>[5,4,7,5,3,2]</code> → <code>[5,5,2,3,4,7]</code>。",
 ],
 "follow": [
   ("h", "追問一：怎麼求「上一個排列」？"),
   "把所有比較反過來就好：",
   ("ul", [
     "步驟 1 找 <code>nums[i] &gt; nums[i+1]</code>（上升點變下降點）",
     "步驟 2 找從右往左第一個 <code>&lt; nums[i]</code> 的",
     "步驟 3 一樣反轉",
   ]),
   "這就是 C++ 的 <code>std::prev_permutation</code>。",
   ("h", "追問二：怎麼求「第 k 個排列」？"),
   "不需要跑 k 次 next_permutation（那是 O(k·n)）。"
   "用<strong>階乘進位制（factorial number system）</strong>可以 O(n²) 直接算出來："
   "第一位是 <code>k // (n-1)!</code> 個候選，然後 <code>k %= (n-1)!</code>，遞迴下去。"
   "這是第 60 題（Permutation Sequence）。",
   ("h", "追問三：這個演算法的名字和歷史？"),
   "一般叫做 <strong>Narayana Pandita 演算法</strong>，"
   "最早記載於 14 世紀印度數學家 Narayana Pandita 的著作。"
   "同樣的想法在 17 世紀被歐洲的變位鐘（change ringing）傳統重新發現。"
   "<strong>它是最古老、仍在標準庫裡日日運行的演算法之一。</strong>",
 ],
 "related": [
   "<strong>第 46／47 題 Permutations</strong> —— 生成所有排列",
   "<strong>第 60 題 Permutation Sequence</strong> —— 直接算第 k 個",
   "<strong>第 556 題 Next Greater Element III</strong> —— 這題套用在數字上",
 ],
 "check": [
   "為什麼「從右往左第一個下降點」右邊的那一段一定是非遞增的？",
   "步驟 2 的條件寫成 <code>nums[j] &lt; nums[i]</code> 會在哪一筆輸入上出錯？",
   "為什麼步驟 3 可以用「反轉」而不需要「排序」？",
   "當 <code>i == -1</code> 時，三個步驟各自做了什麼？為什麼結果剛好正確？",
 ],
})
print("P31 written")

# ==================== 32. Longest Valid Parentheses ====================
S["p32_stack"] = '''class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 堆疊存「索引」，底部放一個哨兵：最後一個「不合法」的位置
        stack = [-1]
        best = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    # 目前這段合法區間是 (stack[-1], i]
                    best = max(best, i - stack[-1])
                else:
                    # 堆疊空了 -> 這個 ')' 沒人配，它成為新的哨兵
                    stack.append(i)

        return best'''

S["p32_dp"] = '''class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        # dp[i] = 「以 s[i] 結尾」的最長合法子字串長度
        # 只有 s[i] == ')' 時才可能 > 0
        dp = [0] * n
        best = 0

        for i in range(1, n):
            if s[i] != ")":
                continue

            if s[i - 1] == "(":
                # 形如 "....()"  ->  前面的長度 + 2
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
            else:
                # 形如 "....))"  ->  看內層合法段前面那個字元是不是 '('
                inner = dp[i - 1]
                j = i - inner - 1          # 內層合法段前面那一格
                if j >= 0 and s[j] == "(":
                    dp[i] = inner + 2 + (dp[j - 1] if j >= 1 else 0)

            best = max(best, dp[i])

        return best'''

S["p32_scan"] = '''class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0

        # 從左往右：left 多的時候還有救，right 超過 left 就重來
        left = right = 0
        for ch in s:
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                best = max(best, 2 * right)
            elif right > left:
                left = right = 0

        # 從右往左：對稱處理「左括號比較多」的情況，例如 "(()"
        left = right = 0
        for ch in reversed(s):
            if ch == "(":
                left += 1
            else:
                right += 1
            if left == right:
                best = max(best, 2 * left)
            elif left > right:
                left = right = 0

        return best'''

_p32 = [S.load(k) for k in ("p32_stack", "p32_dp", "p32_scan")]


def _p32_ref(s):
    n = len(s)
    best = 0
    for i in range(n):
        bal = 0
        for j in range(i, n):
            bal += 1 if s[j] == "(" else -1
            if bal < 0:
                break
            if bal == 0:
                best = max(best, j - i + 1)
    return best


for s_ in ["(()", ")()())", "", "()", "()(()", "(()())", ")(", "()(())",
           "((((((", "))))))", "()()()"]:
    e = _p32_ref(s_)
    for sol in _p32:
        assert sol.longestValidParentheses(s_) == e, ("P32", s_, sol, sol.longestValidParentheses(s_), e)
for _ in range(4000):
    s_ = "".join(random.choice("()") for _ in range(random.randint(0, 14)))
    e = _p32_ref(s_)
    for sol in _p32:
        assert sol.longestValidParentheses(s_) == e, ("P32", s_, sol, sol.longestValidParentheses(s_), e)
print("P32 solutions OK")

emit({
 "num": 32, "slug": "longest-valid-parentheses",
 "en": [
   "Given a string containing just the characters <code>'('</code> and <code>')'</code>, "
   "return <em>the length of the longest valid (well-formed) parentheses substring</em>.",
 ],
 "zh": [
   "給你一個只含 <code>'('</code> 和 <code>')'</code> 的字串，"
   "回傳其中<strong>最長的合法括號子字串</strong>的長度。",
 ],
 "pre": [
   ("note", "注意是「子字串」不是「子序列」", [
     ("c", """s = "()(()"

  子字串（必須連續）：
      "()"   長度 2  ✔
      "(()"  不合法
      最長合法子字串 = 2

  如果是子序列（可以跳過）：
      取索引 0,1,3,4 -> "()()" 長度 4
      那會是另一題（而且簡單很多：答案就是 2 × min(左括號數, 右括號數) 的某種計算）

本題要的是「連續」的那一段。"""),
     "<strong>這題是第 20 題（Valid Parentheses）的 Hard 版。</strong>"
     "第 20 題只要回答「整串合不合法」，這題要找出「最長的合法區段有多長」。"
     "難度的來源是：<strong>合法區段可以拼接</strong>（<code>\"()()\"</code> 長度是 4 不是 2），"
     "所以不能只記「這一段合不合法」，還要能把相鄰的合法段接起來。",
   ]),
 ],
 "examples": """範例 1
  輸入：s = "(()"
  輸出：2
  說明：最長的合法子字串是 "()"。

範例 2
  輸入：s = ")()())"
  輸出：4
  說明：最長的是中間的 "()()"。

範例 3
  輸入：s = ""
  輸出：0""",
 "constraints": [
   "0 ≤ <code>s.length</code> ≤ 3 × 10⁴",
   "<code>s[i]</code> 是 <code>'('</code> 或 <code>')'</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>字串可以是空的</strong> → 答案 0。所有解法都要能處理。",
       "<strong>n 到 3 × 10⁴</strong>。O(n²)（枚舉所有子字串再驗證）是 9 × 10⁸ —— 太慢。"
       "必須是 O(n)。",
       "<strong>答案一定是偶數</strong>（合法括號的長度必為偶數）。"
       "這可以當作一個 sanity check。",
     ]),
   ]),
 ],
 "idea": [
   "三種 O(n) 解法，思路完全不同：",
   ("t", ["解法", "核心想法", "空間", "特點"],
     [["一、堆疊存索引", "底部放哨兵，用索引差算長度", "O(n)", "最直觀"],
      ["二、DP", "dp[i] = 以 i 結尾的最長合法長度", "O(n)", "最能推廣"],
      ["三、雙向計數", "左右各掃一遍，用計數器", "O(1)", "空間最省"]]),
 ],
 "approaches": [
   ap("解法一", "堆疊存「索引」+ 哨兵（最直觀）", [
     "第 20 題的堆疊存的是「字元」，這題要存「索引」—— 因為我們要算長度。",
     ("c", S["p32_stack"]),
     ("h", "哨兵 −1 在做什麼？"),
     ("c", """堆疊底部永遠放著「最後一個不合法位置」的索引。

初始放 -1，表示「在字串開始之前」有一個虛擬的不合法位置。

這樣 i - stack[-1] 就直接是「從那個不合法位置之後到 i」的長度。

追一遍 s = ")()())"

  i=0 ')' : pop 掉 -1，堆疊空了 -> push 0（0 成為新哨兵）
            stack = [0]
  i=1 '(' : push 1          stack = [0, 1]
  i=2 ')' : pop 掉 1，stack = [0]
            best = max(0, 2 - 0) = 2
  i=3 '(' : push 3          stack = [0, 3]
  i=4 ')' : pop 掉 3，stack = [0]
            best = max(2, 4 - 0) = 4
  i=5 ')' : pop 掉 0，堆疊空了 -> push 5
            stack = [5]

  答案 4 ✔（中間的 "()()"）

關鍵：i=4 時算出 4 而不是 2 ——
因為哨兵 0 記住了「從索引 1 開始都是合法的」，
所以 "()()"  被當成一整段算，而不是兩個 "()"。
這就是「拼接」自然發生的地方。"""),
     ("h", "為什麼是「先 pop 再檢查空不空」？"),
     "遇到 <code>')'</code> 一律先 pop。"
     "如果 pop 完還有東西，表示剛剛 pop 掉的是一個配對的 <code>'('</code>（或哨兵之上的某個），"
     "此時 <code>stack[-1]</code> 就是「這段合法區間的前一格」。"
     "如果 pop 完空了，表示這個 <code>')'</code> 沒人配 —— 它自己成為新的哨兵。",
     "<strong>堆疊裡永遠只有：一個哨兵 + 若干個還沒配對的 <code>'('</code> 的索引。</strong>"
     "理解這個不變量，這個解法就再也不會忘。",
   ], "O(n)", "O(n)", "每個字元 push/pop 各一次", "最壞（全是左括號）堆疊有 n 個", optimal=True),

   ap("解法二", "動態規劃（最能推廣）", [
     "定義 <code>dp[i]</code> = <strong>以 <code>s[i]</code> 結尾</strong>的最長合法子字串長度。"
     "因為合法子字串一定以 <code>')'</code> 結尾，所以 <code>s[i] == '('</code> 時 <code>dp[i] = 0</code>。",
     ("c", S["p32_dp"]),
     ("h", "兩種情況"),
     ("c", """情況 A： s[i-1] == '('，也就是形如 "...()"

        dp[i] = dp[i-2] + 2

        那個 "()" 貢獻 2，
        再加上它前面「以 s[i-2] 結尾」的合法長度（可以拼接）。

        例： "()()"
             dp[1] = 0 + 2 = 2
             dp[3] = dp[1] + 2 = 4 ✔

情況 B： s[i-1] == ')'，也就是形如 "...))"

        s[i] 要配對的是「內層合法段」前面那一個字元。

        內層長度 = dp[i-1]
        內層的前一格 j = i - dp[i-1] - 1

        如果 s[j] == '('，配對成功：
            dp[i] = dp[i-1] + 2 + dp[j-1]
                    ^內層      ^這一對  ^再前面能接上的

        例： "(())"
             i=2: s[1]=='(' -> dp[2] = dp[0] + 2 = 2
             i=3: s[2]==')' -> 內層 dp[2]=2，j = 3-2-1 = 0
                  s[0]=='(' ✔  dp[3] = 2 + 2 + 0 = 4 ✔

        例： "()(())"
             dp[1] = 2
             dp[3] = 0（s[3]=='(' ）
             dp[4] = dp[2] + 2 = 0 + 2 = 2
             dp[5]: 內層 dp[4]=2，j = 5-2-1 = 2，s[2]=='(' ✔
                    dp[5] = 2 + 2 + dp[1] = 2 + 2 + 2 = 6 ✔"""),
     "<strong><code>+ dp[j-1]</code> 這一項是最容易漏的。</strong>"
     "它負責「把前面已經合法的那一段接上來」—— 沒有它，"
     "<code>\"()(())\"</code> 會算成 4 而不是 6。",
     "DP 的好處是<strong>它能回答更多問題</strong>："
     "有了 <code>dp</code> 陣列，你可以直接知道「每個位置結尾的最長合法段」，"
     "進而找出所有合法段的位置、數量、總長度等等。堆疊解法要多做一些工作才能回答這些。",
   ], "O(n)", "O(n)", "掃一遍", "dp 陣列"),

   ap("解法三", "雙向計數（O(1) 空間）", [
     "只用兩個計數器，掃兩遍。",
     ("c", S["p32_scan"]),
     ("h", "為什麼一遍不夠？"),
     ("c", """從左往右掃，維護 left（左括號數）和 right（右括號數）：

    left == right  ->  找到一段合法的，長度 2*right
    right > left   ->  這個 ')' 沒救了，歸零重來

這樣可以正確處理 ")()())"：
    ')' : right=1 > left=0 -> 歸零
    '(' : left=1
    ')' : right=1，相等 -> best = 2
    '(' : left=2
    ')' : right=2，相等 -> best = 4
    ')' : right=3 > left=2 -> 歸零
    答案 4 ✔

但處理不了 "(()"：
    '(' : left=1
    '(' : left=2
    ')' : right=1，left=2 > right -> 既不相等也不歸零
    迴圈結束，best 還是 0  ✘ 應該是 2

問題出在：「左括號比較多」的情況永遠等不到相等。
從右往左再掃一遍（把判斷條件對調）就能補上：
    ')' : right=1
    '(' : left=1，相等 -> best = 2 ✔
    '(' : left=2 > right=1 -> 歸零

兩個方向合起來，涵蓋所有情況。"""),
     "<strong>這是三個解法裡唯一 O(1) 空間的</strong>，"
     "而且程式碼最短。缺點是<strong>最不直觀</strong> —— "
     "「為什麼要掃兩遍」這件事如果講不清楚，面試官會懷疑你是背來的。",
     "建議：面試時<strong>先寫堆疊版</strong>（好解釋），"
     "再說「還有一個 O(1) 空間的雙向掃描解法」並說明為什麼需要兩個方向。",
   ], "O(n)", "O(1)", "掃兩遍", "四個計數器"),
 ],
 "compare": (["解法", "時間", "空間", "直觀程度", "能回答更多問題？"],
   [["一、堆疊 + 哨兵", "O(n)", "O(n)", "★★★★★", "普通"],
    ["二、DP", "O(n)", "O(n)", "★★★☆☆", "✔ 有完整的 dp 表"],
    ["三、雙向計數", "O(n)", "O(1)", "★★☆☆☆", "✘"]]),
 "edges": [
   "<strong>空字串</strong>：<code>\"\"</code> → 0。",
   "<strong>全是左括號</strong>：<code>\"((((((\"</code> → 0。",
   "<strong>全是右括號</strong>：<code>\"))))))\"</code> → 0。",
   "<strong>只有右括號在前</strong>：<code>\")(\"</code> → 0。",
   "<strong>需要拼接</strong>：<code>\"()()()\"</code> → 6。"
   "DP 漏掉 <code>dp[i-2]</code> 或堆疊沒有哨兵的話會得到 2。",
   "<strong>巢狀 + 拼接</strong>：<code>\"()(())\"</code> → 6。"
   "DP 漏掉 <code>dp[j-1]</code> 會得到 4。",
   "<strong>前面有垃圾</strong>：<code>\")()())\"</code> → 4。考驗哨兵的更新。",
   "<strong>左括號比較多</strong>：<code>\"(()\"</code> → 2。"
   "解法三只掃一遍的話會得到 0。",
 ],
 "follow": [
   ("h", "追問一：如果要回傳那一段的起始位置呢？"),
   "堆疊版最方便：更新 <code>best</code> 時一併記下 <code>stack[-1] + 1</code>（起點）。"
   "DP 版則是 <code>i - dp[i] + 1</code>。兩者都不增加複雜度。",
   ("h", "追問二：如果要算「有幾個合法子字串」呢？"),
   "用 DP 比較好做：所有合法子字串的數量和 <code>dp</code> 陣列有關，"
   "但要小心「一段長度 2k 的合法字串裡有多少個合法子字串」不只是 k —— "
   "巢狀結構會產生更多。這其實是一個相當不同的計數問題。",
   ("h", "追問三：如果有多種括號呢？"),
   "計數器法完全失效（不能只數數量），"
   "DP 也會變複雜。堆疊法還能用，但要同時存「索引」和「字元類型」，"
   "而且配對失敗時整段都要作廢。難度會顯著上升。",
   ("h", "追問四：這三個解法背後有什麼共通點？"),
   "都在回答同一個問題：<strong>「這個 <code>')'</code> 往左最遠能合法配到哪裡？」</strong>",
   ("ul", [
     "堆疊：用 <code>stack[-1]</code> 直接記住那個邊界",
     "DP：用 <code>dp[i]</code> 遞推出那個距離",
     "計數器：用「left == right」的時刻隱含地標記那個邊界",
   ]),
   "<strong>看出不同解法在回答同一個問題，是把題目真正學會的標誌。</strong>",
 ],
 "related": [
   "<strong>第 20 題 Valid Parentheses</strong> —— 驗證版，這題的基礎",
   "<strong>第 22 題 Generate Parentheses</strong> —— 生成版",
   "<strong>第 84 題 Largest Rectangle in Histogram</strong> —— 另一個「堆疊存索引」的經典",
   "<strong>第 921／1249 題</strong> —— 讓括號合法的最小插入／刪除",
 ],
 "check": [
   "堆疊底部的哨兵 −1 代表什麼？如果初始化成空堆疊，<code>\"()\"</code> 會算出什麼？",
   "DP 的情況 B 裡，<code>j = i - dp[i-1] - 1</code> 這個位置是什麼？為什麼要檢查它是不是 <code>'('</code>？",
   "DP 漏掉 <code>+ dp[j-1]</code> 的話，<code>\"()(())\"</code> 會算出多少？",
   "解法三為什麼一定要掃兩遍？只從左往右掃，哪一類輸入會漏？",
 ],
})
print("P32 written")
