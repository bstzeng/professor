# -*- coding: utf-8 -*-
"""第 75–78 題。"""
import random, collections, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(75)

# ==================== 75. Sort Colors ====================
S["p75_dutch"] = '''class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 荷蘭國旗問題：三個指標把陣列分成四段
        # [0, low)      全是 0
        # [low, mid)    全是 1
        # [mid, high]   還沒看過
        # (high, n-1]   全是 2
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1          # 換過來的一定是 1（或就是自己），可以安全前進
            elif nums[mid] == 1:
                mid += 1          # 已經在正確的區段，直接過
            else:                 # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # mid 不動！換過來的還沒看過，要重新檢查'''

S["p75_count"] = '''class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 計數排序：掃兩遍，第一遍數數量，第二遍重寫
        count = [0, 0, 0]
        for v in nums:
            count[v] += 1

        i = 0
        for color in range(3):
            for _ in range(count[color]):
                nums[i] = color
                i += 1'''

_p75 = [S.load(k) for k in ("p75_dutch", "p75_count")]
for c in [[2, 0, 2, 1, 1, 0], [2, 0, 1], [0], [1], [2], [], [2, 2, 2],
          [0, 0, 0], [1, 0], [2, 1, 0]]:
    e = sorted(c)
    for sol in _p75:
        a = list(c)
        sol.sortColors(a)
        assert a == e, ("P75", c, sol, a, e)
for _ in range(6000):
    c = [random.randint(0, 2) for _ in range(random.randint(0, 12))]
    e = sorted(c)
    for sol in _p75:
        a = list(c)
        sol.sortColors(a)
        assert a == e, ("P75", c, sol, a, e)
print("P75 solutions OK")

_P75_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">三指標把陣列切成四段，中間那段是「還沒看過」的區域</text>
            <g>
              <rect x="60" y="60" width="120" height="44" fill="var(--accent)" opacity="0.18"/>
              <rect x="180" y="60" width="110" height="44" fill="var(--gold)" opacity="0.18"/>
              <rect x="290" y="60" width="180" height="44" fill="var(--border)" opacity="0.3"/>
              <rect x="470" y="60" width="110" height="44" fill="#ff8a65" opacity="0.18"/>
              <rect x="60" y="60" width="520" height="44" fill="none" stroke="var(--text-muted)"/>
              <line x1="180" y1="60" x2="180" y2="104" stroke="var(--text-muted)"/>
              <line x1="290" y1="60" x2="290" y2="104" stroke="var(--text-muted)"/>
              <line x1="470" y1="60" x2="470" y2="104" stroke="var(--text-muted)"/>
            </g>
            <g font-size="14" text-anchor="middle">
              <text x="120" y="88" fill="var(--accent)">全是 0</text>
              <text x="235" y="88" fill="var(--gold)">全是 1</text>
              <text x="380" y="88" fill="var(--text-muted)">還沒看過</text>
              <text x="525" y="88" fill="#ff8a65">全是 2</text>
            </g>
            <g font-size="12" text-anchor="middle">
              <text x="180" y="128" fill="var(--accent)">low</text>
              <text x="290" y="128" fill="var(--gold)">mid</text>
              <text x="470" y="128" fill="#ff8a65">high</text>
            </g>
            <line x1="20" y1="150" x2="620" y2="150" stroke="var(--border)"/>
            <g font-size="13">
              <text x="40" y="180" fill="var(--accent)">nums[mid] == 0：和 nums[low] 交換，low++、mid++</text>
              <text x="90" y="202" fill="var(--text-muted)" font-size="12">換過來的一定是 1（或就是自己）→ 已檢查過，mid 可以前進</text>
              <text x="40" y="232" fill="var(--gold)">nums[mid] == 1：mid++</text>
              <text x="90" y="254" fill="var(--text-muted)" font-size="12">已經在正確的區段，什麼都不用做</text>
              <text x="40" y="284" fill="#ff8a65">nums[mid] == 2：和 nums[high] 交換，high−−，mid 不動</text>
              <text x="90" y="306" fill="var(--text-muted)" font-size="12">換過來的來自「還沒看過」的區域 → 必須重新檢查</text>
            </g>
            <text x="20" y="340" fill="var(--gold)" font-size="12">「mid 在 0 的情況前進、在 2 的情況不動」是全題唯一需要想清楚的地方。</text>'''

emit({
 "num": 75, "slug": "sort-colors",
 "en": [
   "Given an array <code>nums</code> with <code>n</code> objects colored red, white, or blue, "
   "sort them <strong>in-place</strong> so that objects of the same color are adjacent, with "
   "the colors in the order red, white, and blue.",
   "We will use the integers <code>0</code>, <code>1</code>, and <code>2</code> to represent "
   "the color red, white, and blue, respectively.",
   "You must solve this problem <strong>without</strong> using the library's sort function. "
   "<strong>Follow up:</strong> Could you come up with a one-pass algorithm using only "
   "constant extra space?",
 ],
 "zh": [
   "給你一個只含 <code>0</code>、<code>1</code>、<code>2</code> 的陣列"
   "（分別代表紅、白、藍三種顏色），請<strong>原地</strong>把它們排好，"
   "讓相同顏色相鄰，順序是紅（0）、白（1）、藍（2）。",
   "<strong>不能</strong>使用標準庫的排序函式。",
   "<strong>進階：</strong>能不能只用<strong>一趟掃描</strong>加<strong>常數空間</strong>？",
 ],
 "pre": [
   ("note", "這是經典的「荷蘭國旗問題」", [
     ("c", """1976 年 Dijkstra 提出的「Dutch National Flag Problem」：

    把一堆紅、白、藍的球排成荷蘭國旗的順序
    （紅在上、白在中、藍在下）。

它的重要性遠超過這一題本身 ——
【三路快速排序（3-way quicksort）】的分割步驟就是它。

    一般的 quicksort 把陣列分成「< pivot」和「>= pivot」兩段。
    當資料有大量重複值時，這會退化成 O(n²)。

    三路分割分成「< pivot」「== pivot」「> pivot」三段，
    中間那段直接跳過不用再遞迴 ——
    在「大量重複值」的資料上快非常多。

    Java 的 Arrays.sort（對基本型別）用的
    dual-pivot quicksort 就是這個想法的變形。

所以：這題不只是一個 LeetCode 題，
      它是一個在標準庫裡日日運行的演算法。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [2,0,2,1,1,0]
  輸出：[0,0,1,1,2,2]

範例 2
  輸入：nums = [2,0,1]
  輸出：[0,1,2]""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 300",
   "<code>nums[i]</code> 是 <code>0</code>、<code>1</code> 或 <code>2</code>",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>只有三種值</strong> —— 這讓「計數排序」變得可行（只要三個計數器）。",
       "<strong>要求「一趟 + O(1) 空間」</strong> —— "
       "這排除了計數排序（它要掃兩遍）。"
       "<strong>雖然兩遍在實務上完全可以接受，但題目明說要一遍。</strong>",
       "<strong>不能用內建排序</strong>。"
       "<code>nums.sort()</code> 在 Python 裡會過，但那完全繞過了題目。",
       "<strong>n 只有 300</strong>，效率不是重點 —— 考的是「你會不會三路分割」。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P75_FIG, "0 0 640 354"),
 ],
 "approaches": [
   ap("解法一", "三指標（荷蘭國旗，一趟 O(1) 空間）", [
     ("c", S["p75_dutch"]),
     ("h", "四段不變量（loop invariant）"),
     ("c", """任何時刻，陣列被三個指標切成四段：

    [0, low)      已確定全是 0
    [low, mid)    已確定全是 1
    [mid, high]   還沒檢查
    (high, n-1]   已確定全是 2

初始：low = mid = 0, high = n-1
      -> 前兩段是空的，第三段是全部，第四段是空的 ✔

終止：mid > high
      -> 第三段（還沒檢查）是空的 -> 全部都分類好了 ✔

迴圈條件是 while mid <= high（不是 mid < high）——
因為 mid == high 時，那一格還沒被檢查過。"""),
     ("h", "最關鍵的一點：為什麼 <code>nums[mid] == 2</code> 時 <code>mid</code> 不能前進？"),
     ("c", """情況 A：nums[mid] == 0
    和 nums[low] 交換。

    nums[low] 原本是什麼？
        由不變量，[low, mid) 全是 1。
        所以 nums[low] 要嘛是 1（若 low < mid），
        要嘛就是 nums[mid] 自己（若 low == mid）。

    換過來的值一定是 1 或 0 —— 兩種都「已經檢查過」，
    所以 mid 可以安全前進 ✔

情況 C：nums[mid] == 2
    和 nums[high] 交換。

    nums[high] 原本是什麼？
        由不變量，[mid, high] 是「還沒檢查」的區域。
        所以 nums[high] 可能是 0、1、2 —— 完全未知！

    換過來的值還沒被檢查，
    如果 mid 前進，就會跳過它 ✘

    所以 mid 必須不動，下一輪重新檢查這一格。

如果寫錯（兩種情況都 mid++）：
    nums = [2, 0, 1]
    mid=0: nums[0]=2，和 nums[2] 換 -> [1,0,2]，high=1，(錯誤地) mid=1
    mid=1: nums[1]=0，和 nums[0] 換 -> [0,1,2]，low=1, mid=2
    mid=2 > high=1 -> 結束
    結果 [0,1,2] —— 碰巧對了！

    再試 nums = [1, 2, 0]
    mid=0: nums[0]=1 -> mid=1
    mid=1: nums[1]=2，和 nums[2] 換 -> [1,0,2]，high=1，(錯誤地) mid=2
    mid=2 > high=1 -> 結束
    結果 [1,0,2] ✘ 錯了！

    正確版本：mid 不動，下一輪檢查 nums[1]=0，
              和 nums[0] 換 -> [0,1,2] ✔"""),
     ("h", "為什麼這是「一趟」？"),
     "每一輪迴圈，要嘛 <code>mid</code> 前進，要嘛 <code>high</code> 後退 —— "
     "而 <code>mid</code> 和 <code>high</code> 的距離單調縮小。"
     "所以總共最多 <code>n</code> 輪。"
     "<strong>每個元素最多被「檢查」兩次（一次是原本在 mid、一次是從 high 換過來）</strong>，"
     "但總步數還是 O(n)。",
   ], "O(n)", "O(1)", "一趟，最多 n 輪", "三個指標", optimal=True),

   ap("解法二", "計數排序（兩趟，但更好懂）", [
     ("c", S["p75_count"]),
     "第一遍數出每種顏色有幾個，第二遍照著重寫。"
     "<strong>三行邏輯，幾乎不可能寫錯。</strong>",
     "<strong>不符合「一趟」的要求</strong>，但它的實務價值很高：",
     ("ul", [
       "<strong>推廣性更好</strong>：k 種顏色就開 k 個計數器，"
       "而三指標法只對「恰好三種」有效（四種就要四個指標，邏輯會爆炸）。",
       "<strong>更快（實測）</strong>：兩趟簡單的線性掃描，"
       "比一趟帶交換和分支的掃描，對 CPU 的分支預測器和快取更友善。",
       "<strong>穩定</strong>（如果元素帶額外資料的話，要改寫成標準的計數排序）。",
     ]),
     "<strong>面試時：先寫這個確認邏輯，再說「但題目要一趟，所以我改用三指標」。</strong>",
   ], "O(n)", "O(1)", "掃兩遍", "三個計數器"),
 ],
 "compare": (["解法", "趟數", "空間", "推廣到 k 種顏色？", "備註"],
   [["一、三指標", "1", "O(1)", "✘ 很難", "符合進階要求；三路快排的核心"],
    ["二、計數排序", "2", "O(1)", "✔ 容易", "更好懂、實測更快"]]),
 "edges": [
   "<strong>單一元素</strong>：<code>[0]</code>、<code>[1]</code>、<code>[2]</code> → 原樣。",
   "<strong>全部同色</strong>：<code>[2,2,2]</code>、<code>[0,0,0]</code> → 原樣。"
   "<code>[2,2,2]</code> 會讓 <code>high</code> 一路後退，<code>mid</code> 完全不動。",
   "<strong>已經排好</strong>：<code>[0,1,2]</code> → 原樣。",
   "<strong>完全反序</strong>：<code>[2,1,0]</code> → <code>[0,1,2]</code>。",
   "<strong>兩個元素</strong>：<code>[1,0]</code> → <code>[0,1]</code>。",
   "<strong><code>[1,2,0]</code></strong> → <code>[0,1,2]</code>。"
   "<strong>「nums[mid] == 2 時 mid 也前進」的錯誤版本會在這裡失敗。</strong>",
   "<strong>迴圈條件寫成 <code>mid &lt; high</code></strong>："
   "最後一格不會被檢查，<code>[1,0]</code> 會保持原樣。",
 ],
 "follow": [
   ("h", "追問一：如果有 k 種顏色呢？"),
   "<strong>計數排序</strong>：開 k 個計數器，O(n + k)。這是最好的做法。",
   "三指標法無法優雅地推廣 —— k = 4 需要三個分界點和更複雜的交換邏輯，"
   "而且沒有明顯的正確性保證。"
   "<strong>「荷蘭國旗」之所以優雅，正是因為它剛好是三段。</strong>",
   ("h", "追問二：這和 quicksort 有什麼關係？"),
   ("c", """三路快速排序（3-way quicksort）：

    def quicksort(a, lo, hi):
        if lo >= hi: return
        pivot = a[隨機選一個]
        lt, i, gt = lo, lo, hi

        while i <= gt:                      # 這就是荷蘭國旗！
            if a[i] < pivot:
                a[lt], a[i] = a[i], a[lt]; lt += 1; i += 1
            elif a[i] > pivot:
                a[i], a[gt] = a[gt], a[i]; gt -= 1
            else:
                i += 1

        quicksort(a, lo, lt - 1)
        quicksort(a, gt + 1, hi)            # 中間 [lt, gt] 全等於 pivot，跳過

為什麼重要？
    資料 = [5]*1000000（一百萬個相同的值）

    一般 quicksort（兩路分割）：
        每次只能切掉一個元素 -> O(n²) -> 幾小時

    三路 quicksort：
        第一次分割就把全部歸到「== pivot」段 -> O(n) -> 瞬間

這就是為什麼 Java、C++ 的標準排序都用了某種形式的三路分割
（或 introsort 的其他防退化機制）。""",),
   ("h", "追問三：「不變量」為什麼是理解這類演算法的關鍵？"),
   "因為三指標法的每一行程式碼，都只是在「維持那四段的定義」。"
   "<strong>一旦把不變量寫清楚，正確性就是自明的</strong>；"
   "反過來，如果只記「0 的時候換 low、2 的時候換 high」而不知道為什麼，"
   "就一定會在「mid 該不該前進」上卡住。",
   "<strong>寫任何指標操作的演算法時，先在註解裡寫下不變量</strong> —— "
   "這是最有效的除錯預防措施。",
 ],
 "related": [
   "<strong>第 26／27／80 題</strong> —— 原地雙指標家族",
   "<strong>第 215 題 Kth Largest Element</strong> —— quickselect，同樣用分割",
   "<strong>第 148 題 Sort List</strong> —— 另一個排序題",
   "<strong>第 283 題 Move Zeroes</strong> —— 兩段版的荷蘭國旗",
 ],
 "check": [
   "請寫出三指標法的四段不變量。",
   "為什麼 <code>nums[mid] == 0</code> 時 <code>mid</code> 可以前進，"
   "而 <code>nums[mid] == 2</code> 時不行？",
   "迴圈條件為什麼是 <code>mid &lt;= high</code> 而不是 <code>&lt;</code>？",
   "三路快速排序解決了一般 quicksort 的什麼問題？",
 ],
})
print("P75 written")

# ==================== 76. Minimum Window Substring ====================
S["p76"] = '''from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        need = Counter(t)          # 還「缺」多少個（可以是負的，表示多了）
        missing = len(t)           # 還缺幾個字元（含重複）
        best = (float("inf"), 0, 0)
        left = 0

        for right, ch in enumerate(s):
            # 只有「還缺這個字元」時才減少 missing
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1

            if missing == 0:
                # 視窗已經涵蓋 t，開始從左邊收縮
                while need[s[left]] < 0:      # 這個字元是多餘的
                    need[s[left]] += 1
                    left += 1

                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)

                # 把左端點吐掉一個，繼續找下一個可行窗
                need[s[left]] += 1
                missing += 1
                left += 1

        return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]'''

S["p76_two_counter"] = '''from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        need = Counter(t)
        window = Counter()
        required = len(need)       # 需要「滿足」幾種不同的字元
        formed = 0                 # 目前滿足了幾種

        best = (float("inf"), 0, 0)
        left = 0

        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1        # 這一種字元「剛好」湊夠

            while formed == required:
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)

                lch = s[left]
                window[lch] -= 1
                if lch in need and window[lch] < need[lch]:
                    formed -= 1    # 吐掉之後就不夠了
                left += 1

        return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]'''

_p76 = [S.load(k) for k in ("p76", "p76_two_counter")]


def _p76_ref(s, t):
    """暴力：枚舉所有子字串，找最短的可行窗。"""
    if not t:
        return ""
    need = collections.Counter(t)
    n = len(s)
    best = ""
    for i in range(n):
        cnt = collections.Counter()
        for j in range(i, n):
            cnt[s[j]] += 1
            if all(cnt[c] >= need[c] for c in need):
                if not best or j - i + 1 < len(best):
                    best = s[i:j + 1]
                break
    return best


for s_, t_ in [("ADOBECODEBANC", "ABC"), ("a", "a"), ("a", "aa"), ("", "a"),
               ("ab", "b"), ("bba", "ab"), ("cabwefgewcwaefgcf", "cae")]:
    e = _p76_ref(s_, t_)
    for sol in _p76:
        g = sol.minWindow(s_, t_)
        assert len(g) == len(e), ("P76 len", s_, t_, sol, g, e)
        if g:
            assert not (collections.Counter(t_) - collections.Counter(g)), \
                ("P76 invalid", s_, t_, g)
            assert g in s_, ("P76 not substring", s_, g)
for _ in range(3000):
    s_ = "".join(random.choice("abc") for _ in range(random.randint(0, 12)))
    t_ = "".join(random.choice("abc") for _ in range(random.randint(1, 4)))
    e = _p76_ref(s_, t_)
    for sol in _p76:
        g = sol.minWindow(s_, t_)
        assert len(g) == len(e), ("P76", repr(s_), repr(t_), sol, g, e)
        if g:
            assert not (collections.Counter(t_) - collections.Counter(g)), \
                ("P76 invalid", s_, t_, g)
print("P76 solutions OK")

_P76_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">s = &quot;ADOBECODEBANC&quot;，t = &quot;ABC&quot;　滑動視窗：右邊擴張直到可行，左邊收縮直到不可行</text>
            <g font-family="monospace" font-size="15" text-anchor="middle">
              <text x="60" y="66" fill="var(--text-muted)">A</text>
              <text x="100" y="66" fill="var(--text-muted)">D</text>
              <text x="140" y="66" fill="var(--text-muted)">O</text>
              <text x="180" y="66" fill="var(--text-muted)">B</text>
              <text x="220" y="66" fill="var(--text-muted)">E</text>
              <text x="260" y="66" fill="var(--text-muted)">C</text>
              <text x="300" y="66" fill="var(--text-muted)">O</text>
              <text x="340" y="66" fill="var(--text-muted)">D</text>
              <text x="380" y="66" fill="var(--text-muted)">E</text>
              <text x="420" y="66" fill="var(--text-muted)">B</text>
              <text x="460" y="66" fill="var(--text-muted)">A</text>
              <text x="500" y="66" fill="var(--text-muted)">N</text>
              <text x="540" y="66" fill="var(--text-muted)">C</text>
            </g>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="60" y="86">0</text><text x="180" y="86">3</text><text x="260" y="86">5</text>
              <text x="420" y="86">9</text><text x="460" y="86">10</text><text x="540" y="86">12</text>
            </g>
            <g>
              <rect x="44" y="104" width="232" height="26" rx="4" fill="var(--accent)" opacity="0.2"/>
              <text x="300" y="122" fill="var(--accent)" font-size="12">[0, 5] &quot;ADOBEC&quot; 長度 6　第一個可行窗</text>

              <rect x="164" y="140" width="352" height="26" rx="4" fill="var(--gold)" opacity="0.2"/>
              <text x="530" y="158" fill="var(--gold)" font-size="12">[3, 10] 長度 8</text>

              <rect x="404" y="176" width="152" height="26" rx="4" fill="#ff8a65" opacity="0.28"/>
              <text x="570" y="194" fill="#ff8a65" font-size="12">[9, 12]</text>
            </g>
            <text x="20" y="232" fill="#ff8a65" font-size="13">最短的可行窗是 [9, 12] = &quot;BANC&quot;，長度 4</text>
            <line x1="20" y1="250" x2="620" y2="250" stroke="var(--border)"/>
            <text x="20" y="278" fill="var(--gold)" font-size="12">為什麼是 O(n)：left 和 right 都只往右走，各走 n 步 —— 每個字元最多進出視窗各一次。</text>'''

emit({
 "num": 76, "slug": "minimum-window-substring",
 "en": [
   "Given two strings <code>s</code> and <code>t</code> of lengths <code>m</code> and "
   "<code>n</code> respectively, return <em>the <strong>minimum window substring</strong> of "
   "<code>s</code> such that every character in <code>t</code> (<strong>including "
   "duplicates</strong>) is included in the window</em>. If there is no such substring, "
   "return the empty string <code>\"\"</code>.",
   "The testcases will be generated such that the answer is <strong>unique</strong>.",
   "<strong>Follow up:</strong> Could you find an algorithm that runs in <code>O(m + n)</code> "
   "time?",
 ],
 "zh": [
   "給你兩個字串 <code>s</code> 和 <code>t</code>，"
   "找出 <code>s</code> 裡<strong>最短的子字串</strong>，"
   "使它<strong>涵蓋 <code>t</code> 的所有字元（含重複次數）</strong>。"
   "如果不存在，回傳空字串 <code>\"\"</code>。",
   "測資保證答案是<strong>唯一</strong>的。",
   "<strong>進階：</strong>能不能做到 <code>O(m + n)</code>？",
 ],
 "pre": [
   ("note", "「含重複」這三個字改變了一切", [
     ("c", """t = "AABC"  表示視窗裡必須有【兩個】A、一個 B、一個 C。

    "ABC"    ✘ 只有一個 A
    "AABC"   ✔
    "ABAC"   ✔ 順序不重要，只要數量夠

所以不能用 set，必須用 Counter（多重集合）。

視窗「可行」的定義：
    對每一個字元 c，  window[c] >= need[c]

滑動視窗的標準流程：
    1. right 往右擴張，直到視窗「可行」
    2. left 往右收縮，只要收縮後還「可行」就繼續收
    3. 記錄這個「極小可行窗」的長度
    4. 再吐掉一個左端點（變成不可行），回到步驟 1

    重複直到 right 走到底。

為什麼這樣不會漏掉答案？
    對每一個 right，我們都找出了「以 right 為右端點的最短可行窗」。
    答案一定是某個 right 的最短可行窗，所以全部取 min 就對了。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：s = "ADOBECODEBANC", t = "ABC"
  輸出："BANC"
  說明：最短的涵蓋 A、B、C 的子字串。

範例 2
  輸入：s = "a", t = "a"
  輸出："a"

範例 3
  輸入：s = "a", t = "aa"
  輸出：""
  說明：s 裡只有一個 a，湊不出兩個。""",
 "constraints": [
   "<code>m == s.length</code>，<code>n == t.length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 10⁵",
   "<code>s</code> 和 <code>t</code> 由英文字母（大小寫）組成",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>m, n 到 10⁵</strong>。O(m·n) 是 10¹⁰ —— 必定 TLE。"
       "<strong>必須 O(m + n)。</strong>",
       "<strong><code>t</code> 可能比 <code>s</code> 長</strong> → 直接回 <code>\"\"</code>。",
       "<strong>大小寫有分</strong>：<code>'A'</code> 和 <code>'a'</code> 是不同的字元。",
       "<strong>t 可能有重複字元</strong> —— 這是本題的核心難點。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P76_FIG, "0 0 640 292"),
 ],
 "approaches": [
   ap("解法一", "單一 Counter + missing 計數（最精簡）", [
     ("c", S["p76"]),
     ("h", "<code>need</code> 的值可以是負的 —— 這是最巧妙的地方"),
     ("c", """need = Counter(t)     一開始是「還缺多少」

每讀一個字元 ch：
    need[ch] -= 1

    need[ch] > 0   還缺這個字元
    need[ch] == 0  剛好夠
    need[ch] < 0   多了 |need[ch]| 個（可以吐掉）

而 missing 是「還缺幾個字元（含重複）」：
    只有在 need[ch] > 0（真的還缺）時才 missing -= 1。

    如果 need[ch] <= 0（已經夠了，或不在 t 裡），
    missing 不變 —— 因為多拿一個並不會讓我們「更接近目標」。

    對於不在 t 裡的字元，need[ch] 初始是 0（Counter 的預設），
    減下去會變負 —— 自動被歸類成「多餘的」✔

missing == 0  <=>  所有字元都湊夠了  <=>  視窗可行"""),
     ("h", "收縮迴圈 <code>while need[s[left]] &lt; 0</code>"),
     ("c", """need[s[left]] < 0 表示「這個字元在視窗裡是多餘的」
-> 吐掉它不會破壞可行性 -> 可以安全收縮。

一路收到 need[s[left]] == 0，
表示左端點那個字元是「剛好夠用」的 —— 再吐就不行了。

此時的視窗就是「以 right 為右端點的最短可行窗」✔

收完之後記錄答案，然後：
    need[s[left]] += 1     把左端點吐掉
    missing += 1           現在又缺一個了
    left += 1

這樣視窗變成不可行，迴圈繼續往右找下一個。"""),
     ("h", "為什麼是 O(m + n)？"),
     "<strong><code>left</code> 和 <code>right</code> 都只會往右走，而且都不會超過 <code>m</code>。</strong>"
     "所以總步數是 O(m)。加上建 <code>Counter(t)</code> 的 O(n) —— "
     "總共 <strong>O(m + n)</strong> ✔",
     "<strong>「兩個指標都單調前進」是滑動視窗能達到線性的根本原因</strong> —— "
     "雖然內層有 while 迴圈，但它的總執行次數受 <code>left</code> 的移動次數限制（攤還分析）。",
   ], "O(m + n)", "O(字元集大小)", "left 和 right 各走 m 步",
      "一個 Counter", optimal=True),

   ap("解法二", "兩個 Counter + formed 計數（最好講解）", [
     ("c", S["p76_two_counter"]),
     ("h", "<code>formed</code> 和 <code>required</code>"),
     ("c", """required = len(need)   需要滿足「幾種」不同的字元
formed              目前滿足了「幾種」

    注意這裡數的是「種類」而不是「個數」。

    t = "AABC"
        need = {A:2, B:1, C:1}
        required = 3（三種字元）

    視窗 = "AAB"
        window = {A:2, B:1}
        A 滿足（2 >= 2）✔，B 滿足（1 >= 1）✔，C 不滿足
        formed = 2 != 3  ->  不可行

只有在「剛好湊夠」的那一刻才 formed += 1：
    if window[ch] == need[ch]:
        formed += 1

    用 == 而不是 >= 是關鍵 ——
    如果用 >=，同一種字元會被重複計算很多次。

同理，收縮時：
    if window[lch] < need[lch]:
        formed -= 1

    只有「掉到不夠」時才減。"""),
     ("h", "兩種寫法怎麼選？"),
     ("t", ["", "解法一（單 Counter）", "解法二（雙 Counter）"],
       [["變數個數", "2（need, missing）", "4（need, window, required, formed）"],
        ["核心技巧", "允許 Counter 有負值", "只在「剛好夠／剛好不夠」時更新"],
        ["好講解", "★★★☆☆", "★★★★★"],
        ["程式碼長度", "較短", "較長"]]),
     "<strong>解法二的語意更直白</strong>（「有幾種字元已經湊夠了」），"
     "面試時比較容易一邊寫一邊解釋。"
     "<strong>解法一更精簡</strong>，但「Counter 可以是負的」這個技巧需要多解釋幾句。",
     "<strong>兩個都該會 —— 它們是同一個滑動視窗骨架的兩種記帳方式。</strong>",
   ], "O(m + n)", "O(字元集大小)", "同上", "兩個 Counter"),
 ],
 "compare": (["解法", "時間", "空間", "變數", "備註"],
   [["一、單 Counter + missing", "O(m+n)", "O(Σ)", "2", "最精簡"],
    ["二、雙 Counter + formed", "O(m+n)", "O(Σ)", "4", "最好講解"],
    ["暴力枚舉", "O(m²·n)", "O(Σ)", "—", "會 TLE，只當基準"]]),
 "edges": [
   "<strong>t 比 s 長</strong>：<code>(\"a\", \"aa\")</code> → <code>\"\"</code>。",
   "<strong>剛好相等</strong>：<code>(\"a\", \"a\")</code> → <code>\"a\"</code>。",
   "<strong>沒有答案</strong>：<code>(\"ab\", \"c\")</code> → <code>\"\"</code>。",
   "<strong>t 有重複字元</strong>：<code>(\"aa\", \"aa\")</code> → <code>\"aa\"</code>；"
   "<code>(\"a\", \"aa\")</code> → <code>\"\"</code>。"
   "<strong>用 set 而不是 Counter 會在這裡錯。</strong>",
   "<strong>答案在最後面</strong>：<code>(\"ADOBECODEBANC\", \"ABC\")</code> → <code>\"BANC\"</code>。"
   "<strong>不能找到第一個可行窗就 return。</strong>",
   "<strong>答案就是整個 s</strong>：<code>(\"abc\", \"abc\")</code> → <code>\"abc\"</code>。",
   "<strong>s 有大量不相關的字元</strong>：<code>(\"cabwefgewcwaefgcf\", \"cae\")</code> → <code>\"cwae\"</code>。",
   "<strong>大小寫</strong>：<code>(\"a\", \"A\")</code> → <code>\"\"</code>。",
 ],
 "follow": [
   ("h", "追問一：如果要「最長」的可行窗呢？"),
   "<strong>問題的結構完全不同。</strong>"
   "「最短可行窗」的可行性是<strong>單調的</strong>（窗變大只會更可行），"
   "所以「擴張到可行、收縮到極小」的策略有效。",
   "如果要「最長」，而條件也是「涵蓋 t」，那答案就是整個 <code>s</code>（如果可行）—— 沒有意義。"
   "<strong>有意義的「最長」題目通常是「最多包含 k 種不同字元」</strong>（第 340 題）"
   "或「最多 k 個 0」（第 1004 題）—— "
   "那類條件是「窗變大會變不可行」，所以策略反過來：<strong>擴張到不可行，收縮到可行</strong>。",
   ("c", """兩種滑動視窗的對照：

  求最短可行窗（本題）：
      while 可行:
          記錄答案
          收縮左邊

  求最長可行窗（第 3、340、424、1004 題）：
      while 不可行:
          收縮左邊
      記錄答案

    差別在「記錄答案」的位置，以及 while 的條件方向。

    判斷方法：問自己「窗變大，會變得更可行還是更不可行？」""",),
   ("h", "追問二：如果字元集很大（例如 Unicode）呢？"),
   "空間從 O(52) 變成 O(|t| 的不同字元數)。"
   "<code>Counter</code>（雜湊表）本來就只存出現過的字元，所以不用改。"
   "<strong>但如果用「長度 52 的陣列」實作就要改回雜湊表。</strong>",
   ("h", "追問三：這個滑動視窗骨架能解哪些題？"),
   ("c", """求最短：
    第 76 題   最小覆蓋子串（本題）
    第 209 題  長度最小的子陣列（和 >= target）
    第 862 題  和至少為 K 的最短子陣列（有負數，要用單調佇列）

求最長：
    第 3 題    無重複字元的最長子字串
    第 340 題  至多包含 K 種不同字元的最長子字串
    第 424 題  替換後的最長重複字元
    第 1004 題 最大連續 1 的個數 III

固定長度：
    第 438 題  找所有字母異位詞
    第 567 題  字串的排列
    第 30 題   串聯所有單詞的子串（分組滑動視窗）

共同結構：
    for right in range(n):
        把 s[right] 加入視窗
        while <該收縮的條件>:
            從視窗移除 s[left]
            left += 1
        <在適當的位置記錄答案>

    差別只在「該收縮的條件」和「記錄答案的位置」。""",),
 ],
 "related": [
   "<strong>第 3 題 Longest Substring Without Repeating</strong> —— 求最長的版本",
   "<strong>第 209 題 Minimum Size Subarray Sum</strong> —— 數值版的「求最短」",
   "<strong>第 438／567 題</strong> —— 固定長度的滑動視窗",
   "<strong>第 30 題 Substring with Concatenation of All Words</strong> —— 分組滑動視窗",
   "<strong>第 239 題 Sliding Window Maximum</strong> —— 單調佇列",
 ],
 "check": [
   "為什麼要用 <code>Counter</code> 而不是 <code>set</code>？舉一個會錯的輸入。",
   "解法一裡 <code>need[ch]</code> 可以是負的，這代表什麼？"
   "為什麼只在 <code>need[ch] &gt; 0</code> 時才 <code>missing -= 1</code>？",
   "解法二裡為什麼 <code>formed += 1</code> 的條件用 <code>==</code> 而不是 <code>&gt;=</code>？",
   "「求最短可行窗」和「求最長可行窗」的滑動視窗骨架差在哪兩個地方？",
 ],
})
print("P76 written")
