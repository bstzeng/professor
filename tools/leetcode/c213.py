# -*- coding: utf-8 -*-
"""第 213–218 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(213)


# ==================== 213. House Robber II ====================
S["p213"] = '''class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(a: List[int]) -> int:        # 第 198 題：排成一直線
            take = skip = 0                       # 搶/不搶 目前這間 的最大金額
            for x in a:
                take, skip = skip + x, max(take, skip)
            return max(take, skip)

        if len(nums) == 1:
            return nums[0]                        # ★ 只有一間，頭尾是同一間
        # ★ 頭尾不能同時搶 -> 拆成「不含最後一間」和「不含第一間」
        return max(rob_line(nums[:-1]), rob_line(nums[1:]))'''

S["p213_dp"] = '''class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        def best(lo: int, hi: int) -> int:        # nums[lo..hi] 排成直線
            dp = [0] * (hi - lo + 2)              # dp[i]：前 i 間的最大金額
            for i in range(lo, hi + 1):
                k = i - lo + 1
                dp[k] = max(dp[k - 1], (dp[k - 2] if k >= 2 else 0) + nums[i])
            return dp[-1]

        return max(best(0, n - 2), best(1, n - 1))'''

_p213 = [S.load(k) for k in ("p213", "p213_dp")]


def _p213_ref(nums):
    n = len(nums)
    best = 0
    for mask in range(1 << n):
        ok = all(not (mask >> i & 1 and mask >> ((i + 1) % n) & 1) for i in range(n)) if n > 1 else True
        if ok:
            best = max(best, sum(nums[i] for i in range(n) if mask >> i & 1))
    return best


for nums, want in [([2, 3, 2], 3), ([1, 2, 3, 1], 4), ([1, 2, 3], 3), ([5], 5), ([1, 7], 7), ([0, 0], 0)]:
    for sol in _p213:
        assert sol.rob(nums) == want, ("P213", nums, sol)
for _ in range(2000):
    nums = [random.randint(0, 20) for _ in range(random.randrange(1, 11))]
    want = _p213_ref(nums)
    for sol in _p213:
        assert sol.rob(nums) == want, ("P213 rand", nums)
print("P213 OK")

_P213_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">房子排成一圈：第一間和最後一間相鄰，不能同時搶</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="110" cy="110" r="60" fill="none" stroke="var(--border)"/>
              <circle cx="110" cy="50" r="15" fill="var(--surface)" stroke="#ff8a65"/><text x="110" y="55" fill="#ff8a65">0</text>
              <circle cx="167" cy="91" r="15" fill="var(--surface)" stroke="var(--text-muted)"/><text x="167" y="96" fill="var(--text)">1</text>
              <circle cx="145" cy="159" r="15" fill="var(--surface)" stroke="var(--text-muted)"/><text x="145" y="164" fill="var(--text)">2</text>
              <circle cx="75" cy="159" r="15" fill="var(--surface)" stroke="var(--text-muted)"/><text x="75" y="164" fill="var(--text)">3</text>
              <circle cx="53" cy="91" r="15" fill="var(--surface)" stroke="#ff8a65"/><text x="53" y="96" fill="#ff8a65">4</text>
            </g>
            <text x="60" y="205" fill="#ff8a65" font-size="12">0 和 4 相鄰 ✘</text>
            <text x="230" y="70" fill="var(--text)" font-size="12">★ 最佳解不可能同時包含 0 和 4，所以它一定屬於下面其中一種：</text>
            <g font-size="13" text-anchor="middle">
              <text x="250" y="112" fill="var(--text-muted)" font-size="12" text-anchor="start">情況一：不搶 4</text>
              <rect x="380" y="96" width="36" height="24" fill="none" stroke="var(--accent)"/><text x="398" y="113" fill="var(--accent)">0</text>
              <rect x="420" y="96" width="36" height="24" fill="none" stroke="var(--accent)"/><text x="438" y="113" fill="var(--accent)">1</text>
              <rect x="460" y="96" width="36" height="24" fill="none" stroke="var(--accent)"/><text x="478" y="113" fill="var(--accent)">2</text>
              <rect x="500" y="96" width="36" height="24" fill="none" stroke="var(--accent)"/><text x="518" y="113" fill="var(--accent)">3</text>
              <text x="250" y="152" fill="var(--text-muted)" font-size="12" text-anchor="start">情況二：不搶 0</text>
              <rect x="420" y="136" width="36" height="24" fill="none" stroke="var(--gold)"/><text x="438" y="153" fill="var(--gold)">1</text>
              <rect x="460" y="136" width="36" height="24" fill="none" stroke="var(--gold)"/><text x="478" y="153" fill="var(--gold)">2</text>
              <rect x="500" y="136" width="36" height="24" fill="none" stroke="var(--gold)"/><text x="518" y="153" fill="var(--gold)">3</text>
              <rect x="540" y="136" width="36" height="24" fill="none" stroke="var(--gold)"/><text x="558" y="153" fill="var(--gold)">4</text>
            </g>
            <text x="230" y="196" fill="var(--text)" font-size="12">兩種情況都是「排成一直線」的第 198 題，答案取較大者。</text>'''

emit({
 "num": 213, "slug": "house-robber-ii",
 "en": [
   "A thief plans to rob houses arranged in a <strong>circle</strong>, so the first house is adjacent to the last one. "
   "Each house <code>i</code> holds <code>nums[i]</code> money. Robbing two adjacent houses on the same night triggers the alarm.",
   "Return the maximum amount of money that can be stolen without triggering the alarm.",
 ],
 "zh": [
   "小偷要搶一排<strong>圍成一圈</strong>的房子，所以第一間和最後一間是相鄰的。第 <code>i</code> 間房子裡有 <code>nums[i]</code> 元。"
   "同一晚搶了兩間<strong>相鄰</strong>的房子就會觸發警報。",
   "請回傳在不觸發警報的情況下，最多能搶到多少錢。",
 ],
 "examples": """範例 1
  輸入：nums = [2,3,2]
  輸出：3
  說明：第 0 間和第 2 間相鄰，不能都搶，所以只搶中間的 3。

範例 2
  輸入：nums = [1,2,3,1]
  輸出：4
  說明：搶第 0 間（1）和第 2 間（3）。

範例 3
  輸入：nums = [1,2,3]
  輸出：3""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 100",
   "0 ≤ <code>nums[i]</code> ≤ 1000",
 ],
 "idea": [
   ("fig", _P213_FIG, "0 0 640 220"),
   ("c", """【和第 198 題的差別只有一個】：頭尾相鄰。

【把「環」拆成兩條「線」】
    最佳解一定不會同時搶第 0 間和第 n-1 間，所以它屬於：
        情況一：不搶最後一間 -> nums[0 .. n-2] 是一條線
        情況二：不搶第一間   -> nums[1 .. n-1] 是一條線
    兩種情況各用第 198 題的方法求最大值，答案取較大者 ✔

【為什麼兩種情況重疊沒關係？】
    「兩間都不搶」的方案同時屬於兩種情況 ——
    我們取的是最大值，重複算不影響正確性。

【唯一的特例：n = 1】
    nums[:-1] 和 nums[1:] 都是空的，會回傳 0 ✘
    但只有一間房子時，它雖然「和自己相鄰」，當然可以搶。"""),
 ],
 "approaches": [
   ap("解法一", "拆成兩次直線 DP（滾動變數）", [
     ("c", S["p213"]),
     ("c", """【rob_line 的狀態】
    take：搶了目前這間的最大金額
    skip：沒搶目前這間的最大金額

    下一間 x：
        新 take = 舊 skip + x        （上一間不能搶）
        新 skip = max(舊 take, 舊 skip)"""),
   ], "O(n)", "O(n)", "兩次線性掃描", "切片複製；改用索引可降為 O(1)", optimal=True),

   ap("解法二", "DP 陣列版（用索引區間）", [
     ("c", S["p213_dp"]),
     "用索引區間代替切片，比較接近其他語言的寫法。<code>dp[k]</code> 表示「只看區間內前 k 間」的最大金額。",
   ], "O(n)", "O(n)", "", "dp 陣列"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、兩次直線（滾動）", "O(n)", "O(n) / O(1)", "簡潔 ✔"],
    ["二、DP 陣列", "O(n)", "O(n)", "狀態比較直觀"]]),
 "edges": [
   "<strong>只有一間</strong> → 直接回傳 <code>nums[0]</code>（最常漏掉的特例）。",
   "<strong>兩間</strong> → 只能搶一間，取較大者。",
   "<strong>三間</strong> → 任兩間都相鄰，只能搶一間。",
   "<strong>全部是 0</strong> → 回傳 0。",
 ],
 "follow": [
   ("h", "追問：房子排成一棵樹呢？"),
   ("c", """這是第 337 題。對每個節點回傳 (搶它的最大值, 不搶它的最大值)：
    搶它   = 它的錢 + 左子不搶 + 右子不搶
    不搶它 = max(左子兩種) + max(右子兩種)
後序遍歷一次，O(n)。"""),
 ],
 "related": [
   "<strong>第 198 題 打家劫舍</strong> —— 直線版",
   "<strong>第 337 題 打家劫舍 III</strong> —— 樹狀版",
   "<strong>第 740 題 刪除並獲得點數</strong> —— 換皮的打家劫舍",
 ],
 "check": [
   "為什麼可以把環拆成「不含第一間」和「不含最後一間」兩種情況？",
   "兩種情況有重疊，為什麼不影響答案？",
   "<code>n = 1</code> 為什麼要特別處理？",
 ],
})


# ==================== 214. Shortest Palindrome ====================
S["p214_kmp"] = '''class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = s + "#" + s[::-1]               # ★ '#' 不會出現在 s 裡，防止匹配跨界
        pi = [0] * len(t)                   # KMP 的失敗函數（前綴函數）
        for i in range(1, len(t)):
            k = pi[i - 1]
            while k and t[i] != t[k]:
                k = pi[k - 1]
            if t[i] == t[k]:
                k += 1
            pi[i] = k
        keep = pi[-1]                       # s 的「最長回文前綴」長度
        return s[keep:][::-1] + s'''

S["p214_brute"] = '''class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            # s[:n-i] 是回文 <=> 它等於 r[i:]
            if s.startswith(r[i:]):
                return r[:i] + s
        return ""'''

S["p214_hash"] = '''class Solution:
    def shortestPalindrome(self, s: str) -> str:
        B, M = 131, (1 << 61) - 1
        fwd = bwd = 0                        # s[:i+1] 的正向雜湊、反向雜湊
        power = 1
        best = 0
        for i, ch in enumerate(s):
            c = ord(ch)
            fwd = (fwd * B + c) % M
            bwd = (bwd + c * power) % M
            power = power * B % M
            if fwd == bwd:                   # 可能是回文前綴（雜湊可能碰撞）
                best = i + 1
        return s[best:][::-1] + s'''

_p214 = [S.load(k) for k in ("p214_kmp", "p214_brute", "p214_hash")]
for s, want in [("aacecaaa", "aaacecaaa"), ("abcd", "dcbabcd"), ("", ""), ("a", "a"), ("aa", "aa"), ("aba", "aba"), ("ab", "bab")]:
    for sol in _p214:
        assert sol.shortestPalindrome(s) == want, ("P214", s, sol)
for _ in range(4000):
    s = "".join(random.choice("ab") for _ in range(random.randrange(0, 14)))
    want = _p214[1].shortestPalindrome(s)
    for sol in _p214:
        got = sol.shortestPalindrome(s)
        assert got == want, ("P214 rand", s, got, want)
print("P214 OK")

emit({
 "num": 214, "slug": "shortest-palindrome",
 "en": [
   "You are given a string <code>s</code>. You may only add characters to the <strong>front</strong> of it to turn it into a palindrome.",
   "Return the shortest palindrome that can be obtained this way.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，你只能在它的<strong>前面</strong>加字元，把它變成回文。",
   "請回傳用這種方式能得到的<strong>最短回文</strong>。",
 ],
 "examples": """範例 1
  輸入：s = "aacecaaa"
  輸出："aaacecaaa"

範例 2
  輸入：s = "abcd"
  輸出："dcbabcd\"""",
 "constraints": [
   "0 ≤ <code>s.length</code> ≤ 5 × 10⁴",
   "<code>s</code> 只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【問題轉換】
    只能在前面加字元 ->
    s 的某個「前綴」會成為回文的中心部分，
    剩下的後綴反轉後補到前面。

    s = "aacecaaa"
          最長回文前綴 = "aacecaa"（長度 7）
          剩下的後綴   = "a"
          答案 = reverse("a") + s = "a" + "aacecaaa" ✔

【所以這題 = 找 s 的「最長回文前綴」】
    保留得越長，前面要補的就越少。

【怎麼快速找最長回文前綴？】

    s[:k] 是回文  <=>  s[:k] == reverse(s)[n-k:]
                   <=>  s 的前綴 等於 reverse(s) 的後綴

    「一個字串的前綴 = 另一個字串的後綴」
    正是 KMP 前綴函數擅長的事：
        t = s + "#" + reverse(s)
        pi[最後] = t 的「最長相等前後綴」長度
                 = s 的最長回文前綴長度 ✔

【為什麼要加 '#'？】
    如果沒有分隔字元，前後綴的匹配可能跨過 s 的邊界，
    例如 s = "aa" 時 t = "aaaa"，pi[-1] = 3 > len(s) ✘"""),
 ],
 "approaches": [
   ap("解法一", "暴力找最長回文前綴", [
     ("c", S["p214_brute"]),
     ("c", """【s.startswith(r[i:]) 在檢查什麼？】
    r = reverse(s)，r[i:] 的長度是 n - i。
    s 以 r[i:] 開頭 <=> s[:n-i] == reverse(s[:n-i]) 的樣子
                   <=> s[:n-i] 是回文。
    i 從 0 開始 -> 第一個成立的就是最長的回文前綴。

【最壞情況】s = "aaaa…ab"：每次比較都要 O(n)，總共 O(n²)。
    n = 5×10^4 時，Python 的 startswith 是 C 實作，
    其實勉強能過，但不是面試想要的答案。"""),
   ], "O(n²)", "O(n)", "", ""),

   ap("解法二", "KMP 前綴函數", [
     ("c", S["p214_kmp"]),
     ("c", """【前綴函數 pi[i]】
    t[0..i] 中，「既是前綴、又是後綴」的最長真子字串長度。

【模擬】s = "abab"
    t = "abab#baba"
    pi = [0,0,1,2,0,0,1,2,3]
    pi[-1] = 3 -> 最長回文前綴 "aba"
    答案 = reverse("b") + "abab" = "babab" ✔"""),
   ], "O(n)", "O(n)", "", "", optimal=True),

   ap("解法三", "滾動雜湊", [
     ("c", S["p214_hash"]),
     ("c", """【同時維護兩個雜湊】
    fwd = s[0..i] 從左往右的雜湊
    bwd = s[0..i] 從右往左的雜湊（新字元放在最高位）
    兩者相等 -> s[0..i] 很可能是回文。

【碰撞】
    雜湊相等不保證字串相等。
    模數取 2^61 - 1 這種大質數，碰撞機率極低；
    要絕對保險，可以在最後用切片確認一次。"""),
   ], "O(n)", "O(n)", "", "輸出字串"),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、暴力", "O(n²)", "簡單"],
    ["二、KMP", "O(n)", "確定性、最佳 ✔"],
    ["三、滾動雜湊", "O(n)", "機率性，好寫"]]),
 "edges": [
   "<strong>空字串</strong> → 回傳空字串。",
   "<strong>本身就是回文</strong> → 原樣回傳。",
   "<strong>全部相同字元</strong>（<code>\"aaaa\"</code>）→ 原樣回傳。",
   "<strong>KMP 沒加分隔字元</strong> → 保留長度可能超過 <code>len(s)</code>。",
 ],
 "follow": [
   ("h", "追問：如果只能在「後面」加字元呢？"),
   ("c", """對稱的問題：找 s 的「最長回文後綴」，把前面剩下的反轉補到後面。
把 s 反轉之後，就變成本題。"""),
 ],
 "related": [
   "<strong>第 28 題 找出字串中第一個匹配項的索引</strong> —— KMP",
   "<strong>第 5 題 最長回文子字串</strong>",
   "<strong>第 336 題 回文對</strong> —— 回文前綴／後綴的組合",
   "<strong>第 459 題 重複的子字串</strong> —— 前綴函數的另一個應用",
 ],
 "check": [
   "為什麼這題可以轉換成「找最長回文前綴」？",
   "<code>s[:k]</code> 是回文，等價於 <code>s</code> 和 <code>reverse(s)</code> 之間的什麼關係？",
   "KMP 解法中為什麼要加 <code>'#'</code>？",
   "滾動雜湊怎麼同時算正向和反向的雜湊？",
 ],
})


# ==================== 215. Kth Largest Element in an Array ====================
S["p215_heap"] = '''class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)                  # 大小為 k 的最小堆積
        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x)   # 踢掉目前第 k 大（最小的那個）
        return heap[0]                       # ★ 堆頂就是第 k 大'''

S["p215_qs"] = '''class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def select(a: List[int], k: int) -> int:
            pivot = random.choice(a)         # ★ 隨機樞紐，避免最壞情況
            big = [x for x in a if x > pivot]
            eq = [x for x in a if x == pivot]
            if k <= len(big):
                return select(big, k)
            if k <= len(big) + len(eq):
                return pivot                 # ★ 三路切分：大量重複值也不會退化
            small = [x for x in a if x < pivot]
            return select(small, k - len(big) - len(eq))
        return select(nums, k)'''

S["p215_count"] = '''class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo = min(nums)
        cnt = [0] * (max(nums) - lo + 1)     # 值域只有 2×10^4 + 1 種
        for x in nums:
            cnt[x - lo] += 1
        for v in range(len(cnt) - 1, -1, -1):  # 從大到小數
            k -= cnt[v]
            if k <= 0:
                return v + lo'''

S["p215_sort"] = '''class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]'''

_p215 = [S.load(k) for k in ("p215_heap", "p215_qs", "p215_count", "p215_sort")]
for nums, k, want in [([3, 2, 1, 5, 6, 4], 2, 5), ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4), ([1], 1, 1), ([2, 2, 2], 2, 2), ([-1, -5, 3], 3, -5)]:
    for sol in _p215:
        assert sol.findKthLargest(list(nums), k) == want, ("P215", nums, k, sol)
for _ in range(3000):
    nums = [random.randint(-20, 20) for _ in range(random.randrange(1, 20))]
    k = random.randrange(1, len(nums) + 1)
    want = sorted(nums)[-k]
    for sol in _p215:
        assert sol.findKthLargest(list(nums), k) == want, ("P215 rand", nums, k, sol)
_big = [7] * 100000
assert _p215[1].findKthLargest(_big, 50000) == 7
print("P215 OK")

emit({
 "num": 215, "slug": "kth-largest-element-in-an-array",
 "en": [
   "Given an integer array <code>nums</code> and an integer <code>k</code>, return the <code>k</code>-th largest element of the array.",
   "This means the <code>k</code>-th largest in sorted order, counting duplicates — not the <code>k</code>-th largest distinct value.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code> 和整數 <code>k</code>，回傳陣列中<strong>第 <code>k</code> 大</strong>的元素。",
   "這裡指的是排序後的第 <code>k</code> 大（重複的值要分開算），不是「第 <code>k</code> 大的不同值」。",
 ],
 "examples": """範例 1
  輸入：nums = [3,2,1,5,6,4], k = 2
  輸出：5

範例 2
  輸入：nums = [3,2,3,1,2,4,5,5,6], k = 4
  輸出：4
  說明：由大到小是 6,5,5,4,…，第 4 個是 4。""",
 "constraints": [
   "1 ≤ <code>k</code> ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁴ ≤ <code>nums[i]</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "題目的追問", [
     "<strong>「Can you solve it without sorting?」</strong>",
     "排序是 O(n log n)。這題想看你會不會用<strong>堆積（O(n log k)）</strong>或<strong>快速選擇（平均 O(n)）</strong>。",
   ]),
 ],
 "idea": [
   ("c", """【三個方向】

1. 排序：最簡單，O(n log n)。

2. 大小為 k 的最小堆積：
       堆裡永遠保存「目前看過的最大 k 個」。
       新元素比堆頂（這 k 個裡最小的）大，就替換掉堆頂。
       最後堆頂 = 第 k 大 ✔
       O(n log k)，k 小時很快。

3. 快速選擇（Quickselect）：
       快速排序的分割，但只遞迴「答案所在的那一邊」。
       平均 O(n)，最壞 O(n²)（樞紐每次都選到極端值）。
       用隨機樞紐 + 三路切分避免最壞情況。

4. 計數：
       值域只有 [-10^4, 10^4]，可以直接數每個值出現幾次。
       O(n + 值域)。

【三路切分為什麼重要？】
    nums 全部是同一個數時，兩路切分每次只能分出 1 個元素 ->
    退化成 O(n²)。
    三路切分把「等於樞紐」的全部放在中間，一次就結束 ✔"""),
 ],
 "approaches": [
   ap("解法一", "排序", [
     ("c", S["p215_sort"]),
     "一行解。面試時可以先說出來，再說明追問要求更快的做法。",
   ], "O(n log n)", "O(n)", "", ""),

   ap("解法二", "大小為 k 的最小堆積", [
     ("c", S["p215_heap"]),
     ("c", """【為什麼用「最小」堆積找「第 k 大」？】
    我們要保留最大的 k 個，
    需要隨時能踢掉「這 k 個裡最小的」——
    最小堆積的堆頂正好就是它。

【heapreplace 比 heappop + heappush 快】
    一次完成「彈出堆頂、放入新元素」。"""),
   ], "O(n log k)", "O(k)", "", "", optimal=True),

   ap("解法三", "快速選擇（三路切分 + 隨機樞紐）", [
     ("c", S["p215_qs"]),
     "每次期望把問題規模縮小一個常數比例：n + n/2 + n/4 + … = <strong>平均 O(n)</strong>。"
     "這個寫法用額外的 list 讓邏輯清楚；原地版本（Hoare / Lomuto 分割）空間更省，但更容易寫錯。",
   ], "平均 O(n)", "O(n)", "最壞 O(n²)，機率極低", "切分用的 list"),

   ap("解法四", "計數（利用值域很小）", [
     ("c", S["p215_count"]),
     "只有在值域有界時才能用。這題值域只有 20001 種，<strong>O(n + 值域)</strong>，實測非常快。",
   ], "O(n + V)", "O(V)", "V = 值域大小", ""),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、排序", "O(n log n)", "O(n)", "最簡單"],
    ["二、最小堆積", "O(n log k)", "O(k)", "也適用於資料串流 ✔"],
    ["三、快速選擇", "平均 O(n)", "O(n)", "要三路切分防退化"],
    ["四、計數", "O(n + V)", "O(V)", "值域小時最快"]]),
 "edges": [
   "<strong>有重複值</strong> → 重複的要分開算（範例 2）。",
   "<strong><code>k = 1</code></strong> → 最大值；<strong><code>k = n</code></strong> → 最小值。",
   "<strong>全部相同</strong> → 兩路切分的快速選擇會退化成 O(n²)。",
   "<strong>用最大堆積彈 k 次</strong> → 也對，O(n + k log n)；Python 要把值取負號。",
 ],
 "follow": [
   ("h", "追問：如果資料是串流，要隨時回答第 k 大？"),
   ("c", """用解法二的大小為 k 的最小堆積，每來一個數 O(log k) 更新，
堆頂隨時就是答案 —— 這就是第 703 題。"""),
 ],
 "related": [
   "<strong>第 703 題 資料串流中的第 K 大元素</strong>",
   "<strong>第 347 題 前 K 個高頻元素</strong> —— 堆積或快速選擇",
   "<strong>第 973 題 最接近原點的 K 個點</strong>",
   "<strong>第 295 題 資料串流的中位數</strong> —— 兩個堆積",
 ],
 "check": [
   "為什麼找「第 k 大」要用「最小」堆積？",
   "快速選擇的平均複雜度為什麼是 O(n)？",
   "為什麼要用三路切分？全部元素相同時會發生什麼事？",
   "計數解法在什麼條件下才能用？",
 ],
})


# ==================== 216. Combination Sum III ====================
S["p216"] = '''class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res, path = [], []

        def dfs(start: int, remain: int) -> None:
            if len(path) == k:
                if remain == 0:
                    res.append(path[:])
                return
            for d in range(start, 10):
                if d > remain:              # ★ 剪枝：後面只會更大
                    break
                path.append(d)
                dfs(d + 1, remain - d)      # 下一個數字要更大 -> 不重複
                path.pop()

        dfs(1, n)
        return res'''

S["p216_comb"] = '''class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [list(c) for c in itertools.combinations(range(1, 10), k) if sum(c) == n]'''

S["p216_mask"] = '''class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        for mask in range(1 << 9):          # 9 個數字，每個選或不選
            if bin(mask).count("1") != k:
                continue
            nums = [d + 1 for d in range(9) if mask >> d & 1]
            if sum(nums) == n:
                res.append(nums)
        return res'''

_p216 = [S.load(k) for k in ("p216", "p216_comb", "p216_mask")]
for k, n, want in [(3, 7, [[1, 2, 4]]), (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]), (4, 1, []), (9, 45, [list(range(1, 10))]), (2, 18, [])]:
    for sol in _p216:
        assert sorted(sol.combinationSum3(k, n)) == want, ("P216", k, n, sol)
for k in range(2, 10):
    for n in range(1, 61):
        want = sorted(_p216[1].combinationSum3(k, n))
        for sol in _p216:
            assert sorted(sol.combinationSum3(k, n)) == want, ("P216 all", k, n)
print("P216 OK")

emit({
 "num": 216, "slug": "combination-sum-iii",
 "en": [
   "Find all valid combinations of <code>k</code> numbers that add up to <code>n</code>, under these rules:",
   ("ul", ["Only the digits <code>1</code> through <code>9</code> may be used.",
           "Each digit may be used at most once."]),
   "Return a list of all such combinations. The list must not contain the same combination twice, "
   "and the combinations may be returned in any order.",
 ],
 "zh": [
   "找出所有由 <code>k</code> 個數字組成、總和為 <code>n</code> 的組合，規則如下：",
   ("ul", ["只能使用數字 <code>1</code> 到 <code>9</code>。",
           "每個數字<strong>最多用一次</strong>。"]),
   "回傳所有符合條件的組合。<strong>不能有重複的組合</strong>，順序不限。",
 ],
 "examples": """範例 1
  輸入：k = 3, n = 7
  輸出：[[1,2,4]]

範例 2
  輸入：k = 3, n = 9
  輸出：[[1,2,6],[1,3,5],[2,3,4]]

範例 3
  輸入：k = 4, n = 1
  輸出：[]
  說明：4 個不同的正整數，最小的和是 1+2+3+4 = 10 > 1。""",
 "constraints": [
   "2 ≤ <code>k</code> ≤ 9",
   "1 ≤ <code>n</code> ≤ 60",
 ],
 "idea": [
   ("c", """【這是組合題的標準回溯模板】

    從 1 開始，依序決定「下一個要選的數字」，
    而且每次只從「比上一個大」的數字裡選 ->
    自然不會出現 [1,2,4] 和 [2,1,4] 這種重複 ✔

【兩個剪枝】
    1. 已經選滿 k 個 -> 不管和是多少都要停。
    2. 數字從小到大試，某個數字 d > 剩下的和 ->
       後面的數字更大，一定也不行 -> break。

【搜尋空間其實很小】
    只有 1~9 共 9 個數字，所有子集合只有 2^9 = 512 個。
    所以這題用暴力列舉也完全可以，
    重點是練習回溯的寫法（第 39、40、77 題都是同一個模板）。"""),
 ],
 "approaches": [
   ap("解法一", "回溯 + 剪枝", [
     ("c", S["p216"]),
     ("c", """【path[:] 為什麼要複製？】
    path 之後會被 pop 改掉；直接 append(path) 放進去的是同一個物件，
    最後 res 裡全部會變成空 list ✘"""),
   ], "O(C(9, k) · k)", "O(k)", "最多 C(9,k) 個組合", "遞迴深度 k", optimal=True),

   ap("解法二", "itertools.combinations", [
     ("c", S["p216_comb"]),
     "列出所有 C(9, k) 種組合再過濾，最多 126 種。<strong>一行，實務上很好用。</strong>",
   ], "O(C(9, k) · k)", "O(C(9, k) · k)", "", ""),

   ap("解法三", "位元遮罩列舉", [
     ("c", S["p216_mask"]),
     "512 個遮罩逐一檢查。這個想法在「選或不選、元素很少」的題目裡很常用。",
   ], "O(2⁹ · 9)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、回溯 + 剪枝", "O(C(9,k)·k)", "可推廣的模板 ✔"],
    ["二、combinations", "O(C(9,k)·k)", "最短"],
    ["三、位元遮罩", "O(512·9)", "小規模萬用"]]),
 "edges": [
   "<strong><code>n</code> 太小</strong>（小於 1+2+…+k）→ 空陣列。",
   "<strong><code>n</code> 太大</strong>（大於最大 k 個數之和）→ 空陣列。",
   "<strong><code>k = 9, n = 45</code></strong> → 唯一解 <code>[1..9]</code>。",
   "<strong>放進結果時沒有複製 <code>path</code></strong> → 結果全部變成空的。",
 ],
 "follow": [
   ("h", "追問：這題和第 39、40、77 題有什麼不同？"),
   ("t", ["題號", "候選數字", "可以重複用？", "限制"],
    [["39", "給定陣列", "可以", "和為 target"],
     ["40", "給定陣列（有重複值）", "不行", "和為 target，結果不能重複"],
     ["77", "1..n", "不行", "選 k 個"],
     ["216", "1..9", "不行", "選 k 個且和為 n"]]),
 ],
 "related": [
   "<strong>第 39 題 組合總和</strong>",
   "<strong>第 40 題 組合總和 II</strong>",
   "<strong>第 77 題 組合</strong>",
   "<strong>第 377 題 組合總和 IV</strong> —— 其實是排列數的 DP",
 ],
 "check": [
   "回溯時為什麼「只從比上一個大的數字裡選」就不會重複？",
   "這題有哪兩個剪枝？",
   "為什麼放進結果時要用 <code>path[:]</code>？",
   "為什麼這題用暴力列舉也可以？",
 ],
})


# ==================== 217. Contains Duplicate ====================
S["p217_set"] = '''class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True          # ★ 一發現就提早結束
            seen.add(x)
        return False'''

S["p217_len"] = '''class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)'''

S["p217_sort"] = '''class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)          # 排序後，相同的值一定相鄰
        return any(nums[i] == nums[i + 1] for i in range(len(nums) - 1))'''

_p217 = [S.load(k) for k in ("p217_set", "p217_len", "p217_sort")]
for nums, want in [([1, 2, 3, 1], True), ([1, 2, 3, 4], False), ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True), ([5], False)]:
    for sol in _p217:
        assert sol.containsDuplicate(nums) == want, ("P217", nums, sol)
for _ in range(3000):
    nums = [random.randint(-10, 10) for _ in range(random.randrange(1, 12))]
    want = len(set(nums)) < len(nums)
    for sol in _p217:
        assert sol.containsDuplicate(nums) == want
print("P217 OK")

emit({
 "num": 217, "slug": "contains-duplicate",
 "en": [
   "Given an integer array <code>nums</code>, return <code>true</code> if some value occurs at least twice, "
   "and <code>false</code> if all values are distinct.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>。如果有任何值出現<strong>至少兩次</strong>，回傳 <code>true</code>；"
   "如果每個值都不同，回傳 <code>false</code>。",
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,1]
  輸出：true

範例 2
  輸入：nums = [1,2,3,4]
  輸出：false

範例 3
  輸入：nums = [1,1,1,3,3,4,3,2,4,2]
  輸出：true""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
 ],
 "idea": [
   ("c", """【三種思路，對應三種時間/空間取捨】

    1. 雜湊集合：邊走邊記，看到見過的就回傳 true。
       O(n) 時間、O(n) 空間。
    2. 排序：相同的值會相鄰，檢查相鄰元素。
       O(n log n) 時間、O(1)~O(n) 空間（看排序是否原地）。
    3. 兩兩比較：O(n²)，n = 10^5 時超時 ✘

【面試時值得說出來的】
    - 集合法可以「提早結束」：第一對重複出現就停。
      len(set(nums)) 的寫法則一定會處理完整個陣列。
    - 如果不能用額外空間，就原地排序（nums.sort()），
      但這會改動輸入 —— 要先確認可不可以。"""),
 ],
 "approaches": [
   ap("解法一", "雜湊集合，邊走邊查", [
     ("c", S["p217_set"]),
   ], "O(n)", "O(n)", "", "", optimal=True),

   ap("解法二", "比較集合大小（一行）", [
     ("c", S["p217_len"]),
     "最簡潔，但<strong>一定會建完整個集合</strong>——即使前兩個元素就重複了。",
   ], "O(n)", "O(n)", "", ""),

   ap("解法三", "排序後比較相鄰", [
     ("c", S["p217_sort"]),
     "<code>sorted</code> 會建立新陣列（O(n) 空間）；改用 <code>nums.sort()</code> 可以原地排序，但會改到輸入。",
   ], "O(n log n)", "O(1)~O(n)", "", "看排序是否原地"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、集合邊走邊查", "O(n)", "O(n)", "可提早結束 ✔"],
    ["二、集合大小", "O(n)", "O(n)", "一行"],
    ["三、排序", "O(n log n)", "O(1)~O(n)", "不能用額外空間時"]]),
 "edges": [
   "<strong>只有一個元素</strong> → <code>false</code>。",
   "<strong>負數、很大的數</strong> → 集合法不受影響。",
   "<strong>全部相同</strong> → <code>true</code>，集合法在第二個元素就結束。",
 ],
 "follow": [
   ("h", "追問：如果只看距離不超過 k 的重複呢？"),
   ("c", """這是第 219 題：維護一個大小為 k 的滑動視窗集合。
再進一步，「值相差不超過 t」是第 220 題（分桶）。"""),
 ],
 "related": [
   "<strong>第 219 題 存在重複元素 II</strong> —— 距離限制",
   "<strong>第 220 題 存在重複元素 III</strong> —— 距離 + 值差限制",
   "<strong>第 1 題 兩數之和</strong> —— 同樣是「邊走邊查」的雜湊表",
 ],
 "check": [
   "集合「邊走邊查」和 <code>len(set(nums))</code> 有什麼差別？",
   "排序法為什麼可行？它的代價是什麼？",
 ],
})


# ==================== 218. The Skyline Problem ====================
S["p218"] = '''class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 事件：左邊界 (x, -h, right) 代表「開始」；右邊界 (x, 0, 0) 代表「檢查要不要結束」
        events = [(L, -H, R) for L, R, H in buildings]
        events += [(R, 0, 0) for _, R, _ in buildings]
        events.sort()                        # ★ 同一個 x：高的先進，進的先於出

        res = []
        heap = [(0, float("inf"))]           # (−高度, 結束位置)，放一個永遠在的地面
        for x, neg_h, R in events:
            if neg_h:                        # 建築開始
                heapq.heappush(heap, (neg_h, R))
            while heap[0][1] <= x:           # ★ 延遲刪除：已經結束的從堆頂清掉
                heapq.heappop(heap)
            h = -heap[0][0]
            if not res or res[-1][1] != h:   # 高度改變才記錄
                res.append([x, h])
        return res'''

S["p218_brute"] = '''class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        xs = sorted({x for L, R, _ in buildings for x in (L, R)})
        res = []
        for x in xs:
            # 在 x 這一點，涵蓋 [L, R) 的建築中最高的
            h = max((H for L, R, H in buildings if L <= x < R), default=0)
            if not res or res[-1][1] != h:
                res.append([x, h])
        return res'''

_p218 = [S.load(k) for k in ("p218", "p218_brute")]
for b, want in [([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
                 [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]),
                ([[0, 2, 3], [2, 5, 3]], [[0, 3], [5, 0]]),
                ([[1, 2, 1], [1, 2, 2], [1, 2, 3]], [[1, 3], [2, 0]])]:
    for sol in _p218:
        assert sol.getSkyline(b) == want, ("P218", b, sol)
for _ in range(3000):
    bs = []
    for _ in range(random.randrange(1, 7)):
        L = random.randrange(0, 10)
        bs.append([L, L + random.randrange(1, 6), random.randrange(1, 6)])
    bs.sort()
    want = _p218[1].getSkyline(bs)
    assert _p218[0].getSkyline(bs) == want, ("P218 rand", bs)
print("P218 OK")

_P218_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">範例 1：天際線只在「最高高度改變」的地方留下關鍵點</text>
            <line x1="30" y1="220" x2="620" y2="220" stroke="var(--text-muted)"/>
            <g fill="var(--accent)" fill-opacity="0.12" stroke="var(--accent)" stroke-opacity="0.5">
              <rect x="60" y="120" width="140" height="100"/>
              <rect x="80" y="70" width="80" height="150"/>
              <rect x="130" y="100" width="140" height="120"/>
              <rect x="330" y="120" width="100" height="100"/>
              <rect x="410" y="140" width="100" height="80"/>
            </g>
            <path d="M60 220 V120 H80 V70 H160 V100 H270 V220 H330 V120 H430 V140 H510 V220" fill="none" stroke="#ff8a65" stroke-width="2.5"/>
            <g fill="#ff8a65">
              <circle cx="60" cy="120" r="4"/><circle cx="80" cy="70" r="4"/><circle cx="160" cy="100" r="4"/>
              <circle cx="270" cy="220" r="4"/><circle cx="330" cy="120" r="4"/><circle cx="430" cy="140" r="4"/><circle cx="510" cy="220" r="4"/>
            </g>
            <g font-size="11" fill="var(--text)">
              <text x="36" y="114">[2,10]</text><text x="84" y="64">[3,15]</text><text x="166" y="96">[7,12]</text>
              <text x="276" y="212">[12,0]</text><text x="336" y="114">[15,10]</text><text x="436" y="134">[20,8]</text><text x="516" y="212">[24,0]</text>
            </g>
            <text x="20" y="250" fill="var(--gold)" font-size="12">★ 關鍵點 = 每一個「目前最高高度」改變的 x 座標，以及新的高度。</text>'''

emit({
 "num": 218, "slug": "the-skyline-problem",
 "en": [
   "A city's <em>skyline</em> is the outer contour formed by all its buildings when viewed from far away. "
   "Each building is given as <code>buildings[i] = [left<sub>i</sub>, right<sub>i</sub>, height<sub>i</sub>]</code>: "
   "a rectangle standing on flat ground at height <code>0</code>, spanning x-coordinates <code>left<sub>i</sub></code> to <code>right<sub>i</sub></code>.",
   "Return the skyline as a list of <em>key points</em> <code>[x, y]</code> sorted by <code>x</code>. Each key point is the left end "
   "of a horizontal segment of the skyline; the final key point always has <code>y = 0</code> and marks where the rightmost building ends.",
   "The output must not contain consecutive horizontal segments of equal height — "
   "for example <code>[...,[2,3],[4,5],[7,5],[11,5],[12,7],...]</code> is invalid and should be "
   "<code>[...,[2,3],[4,5],[12,7],...]</code>.",
 ],
 "zh": [
   "城市的<strong>天際線</strong>是從遠處看所有建築物時，形成的外輪廓。每棟建築以 "
   "<code>[left<sub>i</sub>, right<sub>i</sub>, height<sub>i</sub>]</code> 表示：一個立在高度 0 的地面上、"
   "從 x = <code>left<sub>i</sub></code> 延伸到 x = <code>right<sub>i</sub></code> 的矩形。",
   "請以<strong>關鍵點</strong> <code>[x, y]</code> 的列表回傳天際線，依 <code>x</code> 排序。每個關鍵點是天際線中一段水平線段的左端點；"
   "最後一個關鍵點的 <code>y</code> 一定是 0，標示最右邊的建築在哪裡結束。",
   "輸出中<strong>不能有連續兩段高度相同的水平線段</strong>，高度相同的要合併成一段。",
 ],
 "examples": """範例 1
  輸入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
  輸出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

範例 2
  輸入：buildings = [[0,2,3],[2,5,3]]
  輸出：[[0,3],[5,0]]
  說明：兩棟等高的建築緊鄰，x = 2 處高度沒有改變，不產生關鍵點。""",
 "constraints": [
   "1 ≤ <code>buildings.length</code> ≤ 10⁴",
   "0 ≤ <code>left<sub>i</sub></code> &lt; <code>right<sub>i</sub></code> ≤ 2³¹ − 1",
   "1 ≤ <code>height<sub>i</sub></code> ≤ 2³¹ − 1",
   "<code>buildings</code> 依 <code>left<sub>i</sub></code> 非遞減排序",
 ],
 "idea": [
   ("fig", _P218_FIG, "0 0 640 264"),
   ("c", """【天際線只會在建築的左右邊界改變】
    所以只需要在每個邊界 x 上問一個問題：
        「此刻還『站著』的建築裡，最高的是多高？」
    這個最高值和前一個不同 -> 新的關鍵點。

【掃描線 + 最大堆積】
    從左到右掃過所有邊界：
        碰到左邊界 -> 這棟建築加入「站著的集合」
        碰到右邊界 -> 這棟建築離開
    需要隨時知道集合中的最大高度 -> 最大堆積。

【堆積不能刪除中間的元素怎麼辦？延遲刪除】
    堆裡存 (高度, 結束位置)。
    不急著刪已經結束的建築，
    只在「它跑到堆頂」時才檢查：結束位置 <= x 就彈掉。
    堆頂以下的過期建築不影響最大值，可以晚點再處理 ✔

【同一個 x 上的事件順序很重要】
    範例：[[1,2,1],[1,2,2],[1,2,3]] 三棟同起同止。
    如果先處理低的，會產生 [1,1],[1,2],[1,3] 三個點 ✘
    事件排序鍵 (x, -h)：同一個 x 高的先進 -> 只產生 [1,3] ✔
    「進」的 -h 是負數，「出」是 0 -> 同一個 x 先進後出，
    範例 2 在 x = 2 不會先掉到 0 再升回 3 ✔"""),
 ],
 "approaches": [
   ap("解法一", "逐點計算最大高度（O(n²)）", [
     ("c", S["p218_brute"]),
     "對每個邊界座標，掃過所有建築算最大高度。<strong>n = 10⁴ 時是 2×10⁸ 次，會超時</strong>，但它是驗證正確性的好工具。",
     "注意區間是 <code>[L, R)</code>：在 <code>x = R</code> 這一點建築已經結束了。",
   ], "O(n²)", "O(n)", "", ""),

   ap("解法二", "掃描線 + 最大堆積（延遲刪除）", [
     ("c", S["p218"]),
     ("c", """【堆裡為什麼先放一個 (0, inf)？】
    代表地面，永遠不會過期。
    所有建築都結束時，堆頂就是它 -> 高度 0，
    也不用擔心對空堆取 heap[0] ✔

【while heap[0][1] <= x】
    結束位置 <= x 的建築在 x 已經不算數（區間是 [L, R)）。

【複雜度】
    2n 個事件，每棟建築進堆出堆各一次 -> O(n log n)"""),
   ], "O(n log n)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、逐點計算", "O(n²)", "O(n)", "超時，但好驗證"],
    ["二、掃描線 + 堆積", "O(n log n)", "O(n)", "標準解 ✔"]]),
 "edges": [
   "<strong>兩棟等高建築緊鄰</strong>（範例 2）→ 中間不能產生關鍵點。",
   "<strong>多棟建築同一個 x 開始</strong> → 只能產生一個關鍵點（高的先處理）。",
   "<strong>一棟建築完全被更高的包住</strong> → 它不產生任何關鍵點。",
   "<strong>建築之間有空隙</strong> → 要產生高度 0 的關鍵點。",
   "<strong>座標到 2³¹ − 1</strong> → 不能開一個以座標為索引的陣列。",
 ],
 "follow": [
   ("h", "追問：有沒有不用堆積的做法？"),
   ("c", """【分治】：把建築分成左右兩半，各自求天際線，再像合併排序那樣合併兩條天際線。
合併時同時掃兩條線，記住兩邊「目前高度」，取 max 即可。
同樣是 O(n log n)。

【有序容器】：用可以刪除任意元素的有序集合（例如 sortedcontainers.SortedList）
代替堆積，就不需要延遲刪除。"""),
 ],
 "related": [
   "<strong>第 253 題 會議室 II</strong>（付費）—— 掃描線 + 堆積",
   "<strong>第 699 題 掉落的方塊</strong> —— 區間最大高度",
   "<strong>第 850 題 矩形面積 II</strong> —— 掃描線",
 ],
 "check": [
   "為什麼天際線只會在建築的左右邊界改變？",
   "什麼是延遲刪除？為什麼可以只清除堆頂的過期元素？",
   "同一個 x 上的事件要用什麼順序處理？為什麼？",
   "堆裡預先放的 <code>(0, inf)</code> 有什麼作用？",
 ],
})
