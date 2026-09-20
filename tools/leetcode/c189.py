# -*- coding: utf-8 -*-
"""第 189、190、191、198、199、200 題。"""
import random, itertools
from collections import deque
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(189)


def _build(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _build(l), _build(r))


def _rand_tree(n, lo=-9, hi=9):
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi), _rand_tree(left, lo, hi), _rand_tree(n - 1 - left, lo, hi))


# ==================== 189. Rotate Array ====================
S["p189"] = '''class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n                      # ★ k 可能比 n 大
        if k == 0:
            return

        def rev(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        rev(0, n - 1)               # 整個反轉
        rev(0, k - 1)               # 前 k 個轉回來
        rev(k, n - 1)               # 後 n-k 個轉回來'''

S["p189_cyclic"] = '''class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        count = 0                   # 已經歸位的元素個數
        start = 0
        while count < n:
            cur, val = start, nums[start]
            while True:
                nxt = (cur + k) % n
                nums[nxt], val = val, nums[nxt]
                cur = nxt
                count += 1
                if cur == start:    # 繞回起點，這一圈結束
                    break
            start += 1              # 換下一圈'''

S["p189_slice"] = '''class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[n - k:] + nums[:n - k]   # ★ nums[:] 才是原地覆寫'''


def _p189_ref(nums, k):
    n = len(nums)
    k %= n
    return nums[n - k:] + nums[:n - k]


_p189 = [S.load(x) for x in ("p189", "p189_cyclic", "p189_slice")]

for nums, k, want in [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
    ([1], 0, [1]),
    ([1], 5, [1]),
    ([1, 2], 3, [2, 1]),
    ([1, 2, 3, 4, 5, 6], 3, [4, 5, 6, 1, 2, 3]),
]:
    assert _p189_ref(nums, k) == want, ("P189 ref", nums, k)
    for sol in _p189:
        a = list(nums)
        assert sol.rotate(a, k) is None, "P189 要回傳 None"
        assert a == want, ("P189", nums, k, want, a, sol)

for _ in range(4000):
    n = random.randrange(1, 13)
    nums = [random.randint(-20, 20) for _ in range(n)]
    k = random.randrange(0, 30)
    want = _p189_ref(nums, k)
    for sol in _p189:
        a = list(nums)
        sol.rotate(a, k)
        assert a == want, ("P189 random", nums, k, want, a, sol)
print("P189 solutions OK")

_P189_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 三次反轉：整個反轉一次，再把兩段各自轉回來。nums = [1,2,3,4,5,6,7]、k = 3</text>
            <g font-size="13" text-anchor="middle">
              <text x="20" y="56" fill="var(--text-muted)" font-size="12" text-anchor="start">原始</text>
              <g fill="var(--accent)">
                <text x="130" y="56">1</text><text x="180" y="56">2</text><text x="230" y="56">3</text><text x="280" y="56">4</text>
              </g>
              <g fill="var(--gold)">
                <text x="330" y="56">5</text><text x="380" y="56">6</text><text x="430" y="56">7</text>
              </g>
              <text x="20" y="96" fill="var(--text-muted)" font-size="12" text-anchor="start">全部反轉</text>
              <g fill="var(--gold)">
                <text x="130" y="96">7</text><text x="180" y="96">6</text><text x="230" y="96">5</text>
              </g>
              <g fill="var(--accent)">
                <text x="280" y="96">4</text><text x="330" y="96">3</text><text x="380" y="96">2</text><text x="430" y="96">1</text>
              </g>
              <text x="20" y="136" fill="var(--text-muted)" font-size="12" text-anchor="start">前 3 個轉回</text>
              <g fill="var(--gold)">
                <text x="130" y="136">5</text><text x="180" y="136">6</text><text x="230" y="136">7</text>
              </g>
              <g fill="var(--accent)">
                <text x="280" y="136">4</text><text x="330" y="136">3</text><text x="380" y="136">2</text><text x="430" y="136">1</text>
              </g>
              <text x="20" y="176" fill="var(--text-muted)" font-size="12" text-anchor="start">後 4 個轉回</text>
              <g fill="var(--gold)">
                <text x="130" y="176">5</text><text x="180" y="176">6</text><text x="230" y="176">7</text>
              </g>
              <g fill="var(--accent)">
                <text x="280" y="176">1</text><text x="330" y="176">2</text><text x="380" y="176">3</text><text x="430" y="176">4</text>
              </g>
            </g>
            <rect x="110" y="156" width="140" height="28" fill="none" stroke="var(--gold)" stroke-width="1.5"/>
            <rect x="258" y="156" width="196" height="28" fill="none" stroke="var(--accent)" stroke-width="1.5"/>
            <text x="480" y="176" fill="var(--text-muted)" font-size="12">✔ 完成</text>
            <line x1="20" y1="204" x2="620" y2="204" stroke="var(--border)"/>
            <text x="20" y="232" fill="#ff8a65" font-size="13">★ 為什麼「反轉兩次」等於「搬移」？</text>
            <text x="40" y="262" fill="var(--text-muted)" font-size="12">把陣列看成 A·B 兩段（A = 前 n−k 個，B = 後 k 個）。目標是 B·A。</text>
            <text x="40" y="288" fill="var(--accent)" font-size="12">reverse(A·B) = reverse(B)·reverse(A)</text>
            <text x="40" y="314" fill="var(--gold)" font-size="12">再各自反轉一次 → reverse(reverse(B))·reverse(reverse(A)) = B·A ✔</text>
            <text x="40" y="344" fill="var(--text-muted)" font-size="12">這個恆等式對任何「整段搬移」都成立 —— 字串旋轉、雙端佇列平移都用它。</text>'''

emit({
 "num": 189, "slug": "rotate-array",
 "en": [
   "Given an integer array <code>nums</code>, rotate the array to the right by "
   "<code>k</code> steps, where <code>k</code> is non-negative.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，把它<strong>向右輪轉 <code>k</code> 步</strong>"
   "（<code>k</code> 是非負整數）。",
   "「向右輪轉」的意思是：<strong>每個元素往右移 <code>k</code> 格，超出尾端的繞回開頭。</strong>",
 ],
 "pre": [
   ("note", "★ 這題的重點是「原地、O(1) 額外空間」", [
     ("c", """【如果可以用額外空間，這題是一行】：

    nums[:] = nums[n-k:] + nums[:n-k]

    O(n) 時間、O(n) 空間 ——
    面試官會說「很好，現在請你用 O(1) 空間再做一次」。

【O(1) 空間的做法有兩種】：

    1. 【三次反轉】—— 好寫、好記、不會錯 ✔
    2. 【環狀替換】—— 要處理 gcd 的圈數，容易寫錯

    【面試時寫第一種】，
    然後說「還有一種環狀替換法，它的圈數是 gcd(n, k)」——
    展示你知道，但選了不會出錯的那個。

【三個必踩的坑】：

    1. 【k 可能比 n 大】-> 一定要先 k %= n
    2. 【k % n == 0 時】-> 什麼都不用做（有些寫法會爆）
    3. 【回傳值是 None】-> 題目要求【原地修改】

       寫 return nums[n-k:] + nums[:n-k] 會【整題判錯】——
       它建立了新物件，呼叫端的 nums 沒有變 ✘"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,4,5,6,7], k = 3
  輸出：[5,6,7,1,2,3,4]
  說明：向右輪轉 1 步：[7,1,2,3,4,5,6]
        向右輪轉 2 步：[6,7,1,2,3,4,5]
        向右輪轉 3 步：[5,6,7,1,2,3,4]

範例 2
  輸入：nums = [-1,-100,3,99], k = 2
  輸出：[3,99,-1,-100]

範例 3
  輸入：nums = [1,2], k = 3
  輸出：[2,1]
  說明：k = 3 > n = 2，實際上只轉了 3 % 2 = 1 步。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
   "0 ≤ <code>k</code> ≤ 10⁵",
 ],
 "mid": [
   ("note", "題目的追問把難度整個拉高了", [
     "<strong>「Try to come up with as many solutions as you can — there are at least "
     "three different ways to solve this problem.」</strong>",
     "<strong>「Could you do it in-place with O(1) extra space?」</strong>",
     "<strong>這是 LeetCode 少數在題目裡就明講「請給我三種解法」的題目。</strong>"
     "下面三種都寫出來了。",
   ]),
 ],
 "idea": [
   ("fig", _P189_FIG, "0 0 640 368"),
   ("c", """【先把 k 正規化】

    k %= n

    為什麼？因為轉 n 步等於沒轉。
    k = 10^5、n = 3 時，實際上只轉了 10^5 % 3 = 2 步。

    【不做這一步】：
        三次反轉法 rev(0, k-1) 會越界 ✘
        環狀替換法 (cur + k) % n 其實還是對的（因為有 % n）
        切片法 nums[n-k:] 在 k > n 時會拿到整個陣列 ✘

【三次反轉的推導】

    把陣列切成兩段：
        A = nums[0 : n-k]   （要搬到後面的）
        B = nums[n-k : n]   （要搬到前面的）

    目標：A·B  ->  B·A

    【恆等式】：reverse(A·B) = reverse(B)·reverse(A)

    所以：
        step 1: reverse(整個)  -> reverse(B)·reverse(A)
        step 2: reverse(前 k)  -> B·reverse(A)
        step 3: reverse(後 n-k) -> B·A ✔

    【三行，每行都是標準的雙指標反轉。】

【複雜度】

    每個元素被碰到【剛好兩次】（一次在 step 1，
    一次在 step 2 或 step 3）。

    -> O(n) 時間、O(1) 空間 ✔"""),
 ],
 "approaches": [
   ap("解法一", "三次反轉（面試首選）", [
     ("c", S["p189"]),
     "<strong>十行，O(n) 時間、O(1) 空間，而且幾乎不可能寫錯。</strong>",
     ("h", "★ 三個容易錯的地方"),
     ("c", """1. 【k %= n 要放在最前面】

   忘了的話，k = 10 而 n = 3 時
   rev(0, 9) 會存取到不存在的索引 ✘

2. 【k == 0 要早退】

   k = 0 時 rev(0, -1) ——
   在 Python 裡 -1 是「最後一個」，
   while 0 < -1 不成立所以其實沒事，
   但 rev(0, n-1) 已經白做了一次整個反轉，
   再 rev(0, -1) 不做事、rev(0, n-1) 又轉回來 ——

   【結果碰巧是對的】，但多做了兩趟。
   早退比較乾淨，而且在別的語言裡（負索引會爆）是必要的。

3. 【函式要回傳 None】

   題目說「Do not return anything, modify nums in-place instead.」

   寫成 return 新陣列 -> 判錯 ✘""",),
     ("h", "如果直接用內建的 reverse 呢？"),
     ("c", """Python：
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])

【也對，但 nums[:k] 會先建立一個長度 k 的新 list】
    -> 空間變成 O(n) ✘

    面試時如果強調 O(1)，就自己寫 rev ——
    那才真的是原地 ✔""",),
   ], "O(n)", "O(1)", "每個元素碰兩次", "只有幾個索引變數", optimal=True),

   ap("解法二", "環狀替換（gcd 圈數）", [
     ("c", S["p189_cyclic"]),
     ("h", "★ 為什麼需要「外層 start 迴圈」？"),
     ("c", """從索引 0 出發，一直跳 +k（mod n）：

    0 -> k -> 2k -> 3k -> ... -> 回到 0

    這條軌跡會走過幾個位置？

    【答案是 n / gcd(n, k) 個】。

    例子：n = 6, k = 2, gcd = 2
        0 -> 2 -> 4 -> 0    只走到偶數位！
        奇數位 1, 3, 5 【完全沒被碰到】 ✘

    所以要從 start = 1 再走一圈：
        1 -> 3 -> 5 -> 1 ✔

    【總共 gcd(n, k) 圈，每圈 n/gcd 個元素，
      合計剛好 n 個 ✔】

【程式碼裡怎麼知道走完了？】

    用 count 計數，count == n 就結束。

    這比「算 gcd 再跑 gcd 圈」更好寫，
    而且不用 import math ✔

【為什麼這題會出現 gcd？】

    「每次跳 k 步、模 n」形成的子群，
    它的大小是 n / gcd(n, k) ——
    這是【循環群的基本性質】。

    同樣的結構出現在：
        - 約瑟夫問題的變形
        - 「每隔 k 個人出列」的跳格子問題
        - 時鐘指針重合問題

    【看到「固定步長繞圈」就想到 gcd。】""",),
     ("h", "為什麼不推薦？"),
     ("ul", [
       "<strong>三次反轉是 O(2n) 次寫入，環狀替換是 O(n) 次</strong> —— 理論上快一倍，",
       "<strong>但環狀替換的記憶體存取是跳躍的</strong>（<code>+k</code> 一路跳），"
       "<strong>快取命中率極差</strong> —— 實測反而比三次反轉慢。",
       "<strong>而且它容易寫錯</strong>（漏了 <code>start</code> 迴圈、或用 <code>while cur != start</code> "
       "當條件導致第一圈不執行）。",
     ]),
   ], "O(n)", "O(1)", "每個元素剛好寫一次", "只有幾個索引變數"),

   ap("解法三", "切片（違反 O(1) 空間，但要知道）", [
     ("c", S["p189_slice"]),
     ("h", "★ <code>nums[:] = ...</code> 和 <code>nums = ...</code> 的差別"),
     ("c", """nums = nums[n-k:] + nums[:n-k]
    -> 只是把【區域變數】指向新的 list
    -> 呼叫端的陣列【完全沒變】 ✘

nums[:] = nums[n-k:] + nums[:n-k]
    -> 【切片賦值】，把新內容寫回原本的 list 物件
    -> 呼叫端看得到 ✔

【這是 Python 初學者最常見的陷阱之一】，
    而且 LeetCode 的判題方式剛好會抓到它。

    同樣的道理：
        nums.sort()      原地 ✔
        nums = sorted(nums)  不是原地 ✘
        nums[:] = sorted(nums)  原地 ✔

【空間】：右邊先算出一個長度 n 的新 list -> O(n) ✘

    所以這個寫法【不符合追問的要求】，
    但它一行、不會錯，適合當「先求有再求好」的第一版。""",),
   ], "O(n)", "O(n)", "切片", "額外一份陣列"),
 ],
 "compare": (["解法", "時間", "空間", "寫入次數", "備註"],
   [["一、三次反轉", "O(n)", "O(1)", "2n", "面試首選 ✔"],
    ["二、環狀替換", "O(n)", "O(1)", "n", "跳躍存取，實測較慢"],
    ["三、切片", "O(n)", "O(n)", "n", "一行，但不符追問"]]),
 "edges": [
   "<strong><code>k = 0</code></strong> → 不動。",
   "<strong><code>k</code> 是 <code>n</code> 的倍數</strong> → <code>k %= n</code> 之後是 0，不動。",
   "<strong><code>k > n</code></strong>（例如 <code>n = 2, k = 3</code>）→ "
   "<strong>沒有 <code>k %= n</code> 會越界。</strong>",
   "<strong><code>n = 1</code></strong> → 永遠不動（<code>k % 1 == 0</code>）。",
   "<strong>回傳新陣列而不是原地修改</strong> → <strong>判錯。</strong>",
   "<strong><code>nums = ...</code> 寫成沒有 <code>[:]</code></strong> → 呼叫端看不到變化。",
   "<strong>環狀替換忘了外層 <code>start</code> 迴圈</strong> → "
   "<strong><code>gcd(n,k) &gt; 1</code> 時漏掉大半元素。</strong>",
 ],
 "follow": [
   ("h", "追問一：向左輪轉 k 步怎麼寫？"),
   ("c", """【向左 k 步 = 向右 (n - k) 步】

    def rotateLeft(nums, k):
        rotate(nums, (-k) % len(nums))

    或者直接改三次反轉的切點：

        向右 k：rev(全部); rev(0, k-1); rev(k, n-1)
        向左 k：rev(0, k-1); rev(k, n-1); rev(全部)
                ^^^^^^^^^^^^^^^^^^^^^^^^ 順序反過來

    【兩者互為逆操作】 ✔

【驗算】nums = [1,2,3,4,5], k = 2

    向右 2 -> [4,5,1,2,3]
    向左 2 -> [3,4,5,1,2]

    向左 2 == 向右 3 == 向右 (5-2) ✔""",),
   ("h", "追問二：為什麼環狀替換的圈數剛好是 gcd(n, k)？"),
   ("c", """從 0 出發跳 k 步（模 n），走到的位置是：

    {0, k, 2k, 3k, ...} mod n
      = {0·k mod n, 1·k mod n, 2·k mod n, ...}

【這是 k 在 Z_n 裡生成的子群】。

    子群的大小 = n / gcd(n, k)
    （這是循環群的標準結果）

    所以一圈走 n/gcd 個位置，
    要走 n ÷ (n/gcd) = 【gcd(n, k) 圈】才蓋滿 ✔

【直觀理解】：

    設 d = gcd(n, k)。
    從 0 出發，每次 +k，只能走到 d 的倍數
    （因為 k 和 n 都是 d 的倍數）。

    d 的倍數在 0..n-1 裡有 n/d 個 -> 就是一圈的長度。
    剩下的 d-1 個「餘數類」各需要一圈 ✔

【驗算】

    n = 6, k = 2, d = 2
        圈 1：0 -> 2 -> 4 -> 0（3 個）
        圈 2：1 -> 3 -> 5 -> 1（3 個）
        2 圈 × 3 = 6 ✔

    n = 6, k = 3, d = 3
        0->3->0, 1->4->1, 2->5->2
        3 圈 × 2 = 6 ✔

    n = 7, k = 3, d = 1
        0->3->6->2->5->1->4->0
        1 圈 × 7 = 7 ✔""",),
   ("h", "追問三：如果是「輪轉鏈結串列」（第 61 題）呢？"),
   ("c", """鏈結串列不能用反轉法（反轉鏈結串列要 O(n) 且改指標很麻煩）。

【標準做法】：

    1. 走一趟算長度 n，順便找到尾節點
    2. 【把尾巴接回頭】變成環
    3. k %= n，新的尾巴在第 (n - k - 1) 個節點
    4. 走到那裡，斷開 ✔

    【時間 O(n)、空間 O(1)】

【和陣列版的共同點】：

    都要先 k %= n ✔
    都是「找到切點，重新接」

【不同點】：

    陣列：元素要【搬動】
    鏈結串列：只要【改兩個指標】——
              這正是鏈結串列的優勢 ✔""",),
   ("h", "追問四：如果 k 每次都不一樣，要查詢很多次呢？"),
   ("c", """【不要真的搬動】——

    維護一個【偏移量 offset】：

        class RotatableArray:
            def __init__(self, nums):
                self.a = nums
                self.off = 0

            def rotate(self, k):
                self.off = (self.off + k) % len(self.a)   # O(1)

            def get(self, i):
                return self.a[(i - self.off) % len(self.a)]  # O(1)

    【rotate 從 O(n) 降到 O(1)】 ✔

【這就是「環狀緩衝區（ring buffer）」的核心想法】：

    不搬資料，搬「起點」。

    collections.deque 的 rotate() 就是這樣做的 ——
    它是 O(k) 而不是 O(n)，因為它是雙向串列。

【什麼時候該用哪個？】

    只轉一次、之後大量隨機存取 -> 真的搬（連續記憶體，快取友善）
    轉很多次 -> 記 offset ✔""",),
 ],
 "related": [
   "<strong>第 61 題 旋轉鏈結串列</strong> —— 同樣的 <code>k %= n</code>，但改指標",
   "<strong>第 48 題 旋轉圖像</strong> —— 「先轉置再反轉」，同樣是「兩次簡單操作 = 一次複雜操作」",
   "<strong>第 796 題 旋轉字串</strong> —— <code>s in t+t</code> 一行解",
   "<strong>第 186 題 反轉字串中的單詞 II</strong> —— 反轉恆等式的另一個應用",
 ],
 "check": [
   "為什麼 <code>reverse(A·B) = reverse(B)·reverse(A)</code>？三次反轉怎麼從它推出來？",
   "<code>k %= n</code> 不寫會發生什麼事？",
   "環狀替換為什麼需要外層 <code>start</code> 迴圈？圈數為什麼是 <code>gcd(n, k)</code>？",
   "<code>nums[:] = ...</code> 和 <code>nums = ...</code> 差在哪？",
 ],
})
print("P189 written")

# ==================== 190. Reverse Bits ====================
S["p190"] = '''class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)   # 把 n 的最低位推進 res 的最低位
            n >>= 1
        return res'''

S["p190_early"] = '''class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            if n == 0:                   # ★ 剩下全是 0，直接補位
                return res << (32 - i)
            res = (res << 1) | (n & 1)
            n >>= 1
        return res'''

S["p190_dc"] = '''class Solution:
    def reverseBits(self, n: int) -> int:
        # 分治：先兩兩交換，再四四、八八、十六十六
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)   # 相鄰 1 位
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)   # 相鄰 2 位
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)   # 相鄰 4 位
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)   # 相鄰 8 位
        return ((n >> 16) | (n << 16)) & 0xFFFFFFFF             # 前後 16 位'''

S["p190_cache"] = '''class Solution:
    _table = None

    def reverseBits(self, n: int) -> int:
        if Solution._table is None:      # 256 個位元組的反轉表，只算一次
            Solution._table = [
                int(format(b, '08b')[::-1], 2) for b in range(256)
            ]
        t = Solution._table
        return (t[n & 0xFF] << 24 | t[(n >> 8) & 0xFF] << 16 |
                t[(n >> 16) & 0xFF] << 8 | t[(n >> 24) & 0xFF])'''


def _p190_ref(n):
    return int(format(n, "032b")[::-1], 2)


_p190 = [S.load(x) for x in ("p190", "p190_early", "p190_dc", "p190_cache")]

for n, want in [
    (0b00000010100101000001111010011100, 964176192),
    (0b11111111111111111111111111111101, 3221225471),
    (0, 0),
    (1, 1 << 31),
    (1 << 31, 1),
    (0xFFFFFFFF, 0xFFFFFFFF),
]:
    assert _p190_ref(n) == want, ("P190 ref", n, _p190_ref(n))
    for sol in _p190:
        assert sol.reverseBits(n) == want, ("P190", n, want, sol.reverseBits(n), sol)

for _ in range(4000):
    n = random.randrange(0, 1 << 32)
    want = _p190_ref(n)
    for sol in _p190:
        got = sol.reverseBits(n)
        assert got == want, ("P190 random", n, want, got, sol)
    # 反轉兩次要回到自己
    assert _p190[0].reverseBits(want) == n, ("P190 involution", n)
print("P190 solutions OK")


# ==================== 191. Number of 1 Bits ====================
S["p191"] = '''class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1        # ★ 消去最低位的那個 1
            count += 1
        return count'''

S["p191_shift"] = '''class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for _ in range(32):
            count += n & 1
            n >>= 1
        return count'''

S["p191_swar"] = '''class Solution:
    def hammingWeight(self, n: int) -> int:
        # SWAR：分治求和，每一步把「相鄰兩組的計數」加起來
        n = n - ((n >> 1) & 0x55555555)                  # 每 2 位存該 2 位的 1 個數
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)   # 每 4 位
        n = (n + (n >> 4)) & 0x0F0F0F0F                  # 每 8 位
        return ((n * 0x01010101) & 0xFFFFFFFF) >> 24     # 四個位元組加總（要截回 32 位）'''


def _p191_ref(n):
    return bin(n).count("1")


_p191 = [S.load(x) for x in ("p191", "p191_shift", "p191_swar")]

for n, want in [(0, 0), (11, 3), (128, 1), (0xFFFFFFFF, 32), (1, 1), (1 << 31, 1)]:
    assert _p191_ref(n) == want, ("P191 ref", n)
    for sol in _p191:
        assert sol.hammingWeight(n) == want, ("P191", n, want, sol)

for _ in range(6000):
    n = random.randrange(0, 1 << 32)
    want = _p191_ref(n)
    for sol in _p191:
        got = sol.hammingWeight(n)
        assert got == want, ("P191 random", n, want, got, sol)
print("P191 solutions OK")

_P190_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 逐位反轉：像倒水一樣，把 n 的最低位一位一位「倒」進 res 的最低位。</text>
            <g font-family="monospace" font-size="13">
              <text x="20" y="54" fill="var(--text-muted)">n   = 1 0 1 1 ...</text>
              <text x="320" y="54" fill="var(--text-muted)">res = 0</text>
              <text x="20" y="82" fill="var(--accent)">取 n&amp;1 = 1 →</text>
              <text x="320" y="82" fill="var(--gold)">res = 1</text>
              <text x="20" y="110" fill="var(--accent)">取 n&amp;1 = 1 →</text>
              <text x="320" y="110" fill="var(--gold)">res = 1 1</text>
              <text x="20" y="138" fill="var(--accent)">取 n&amp;1 = 0 →</text>
              <text x="320" y="138" fill="var(--gold)">res = 1 1 0</text>
              <text x="20" y="166" fill="var(--accent)">取 n&amp;1 = 1 →</text>
              <text x="320" y="166" fill="var(--gold)">res = 1 1 0 1</text>
            </g>
            <text x="20" y="200" fill="var(--text-muted)" font-size="12">res 每次先左移騰出一格，再把新的位塞進最低位 —— 先進來的被推到最高位 ✔</text>
            <line x1="20" y1="220" x2="620" y2="220" stroke="var(--border)"/>
            <text x="20" y="248" fill="#ff8a65" font-size="13">★ 分治版：交換相鄰 1 位 → 2 位 → 4 位 → 8 位 → 16 位，五步搞定</text>
            <g font-family="monospace" font-size="12">
              <text x="40" y="278" fill="var(--accent)">abcdefgh</text>
              <text x="180" y="278" fill="var(--text-muted)">→ 兩兩交換 →</text>
              <text x="340" y="278" fill="var(--gold)">badcfehg</text>
              <text x="40" y="304" fill="var(--accent)">badcfehg</text>
              <text x="180" y="304" fill="var(--text-muted)">→ 四四交換 →</text>
              <text x="340" y="304" fill="var(--gold)">dcbahgfe</text>
              <text x="40" y="330" fill="var(--accent)">dcbahgfe</text>
              <text x="180" y="330" fill="var(--text-muted)">→ 八八交換 →</text>
              <text x="340" y="330" fill="var(--gold)">hgfedcba ✔</text>
            </g>
            <text x="20" y="364" fill="var(--text-muted)" font-size="12">0x55555555 = 0101…（偶數位）、0x33333333 = 0011…（每 4 位的低 2 位）、0x0F0F0F0F = 每位元組的低 4 位。</text>'''

emit({
 "num": 190, "slug": "reverse-bits",
 "en": [
   "Reverse bits of a given 32 bits unsigned integer.",
   "<strong>Note:</strong> In some languages, such as Java, there is no unsigned integer type. "
   "In this case, both input and output will be given as a signed integer type. They should not "
   "affect your implementation, as the integer's internal binary representation is the same "
   "whether it is signed or unsigned.",
 ],
 "zh": [
   "把一個 <strong>32 位元無號整數</strong>的二進位表示<strong>整個顛倒過來</strong>，回傳顛倒後的數字。",
   "<strong>注意：</strong>是把 32 個位元前後對調"
   "（第 0 位換到第 31 位、第 1 位換到第 30 位……），"
   "<strong>不是</strong>把 0 變 1、1 變 0。",
 ],
 "pre": [
   ("note", "★ 這題在 Python 裡有一個特別的坑", [
     ("c", """【Python 的整數是任意精度的】——
    它沒有「32 位元」這個概念。

    所以：
        1. 【一定要自己固定跑 32 圈】

           while n: 這種寫法在 C 裡可以（會自然停），
           但在 Python 裡輸入 1 會只跑一圈 -> 得到 1 ✘
           正確答案是 1 << 31 = 2147483648

        2. 【左移之後要自己遮罩】

           n << 16 在 Python 不會溢位，
           所以分治法最後一定要 & 0xFFFFFFFF ✘ 否則答案超過 32 位

        3. 【負數不會出現】

           題目說是無號數，LeetCode 傳進來的就是 0 ~ 2^32-1。
           （Java 版才要處理符號位。）

【最短的「作弊解」】：

    return int(format(n, '032b')[::-1], 2)

    【面試官會說「不要用字串」】——
    因為這題考的就是位元運算。

    但把它當成【驗算用的參考解】很好用 ✔"""),
   ]),
 ],
 "examples": """範例 1
  輸入：n = 00000010100101000001111010011100
  輸出：   964176192 (00111001011110000010100101000000)
  說明：輸入代表無號整數 43261596，
        顛倒後代表無號整數 964176192。

範例 2
  輸入：n = 11111111111111111111111111111101
  輸出：  3221225471 (10111111111111111111111111111111)

範例 3（邊界）
  輸入：n = 1        (00000000000000000000000000000001)
  輸出：  2147483648 (10000000000000000000000000000000)
  說明：★ 最低位跑到最高位。
        如果你寫 while n: 這一題就會錯。""",
 "constraints": [
   "輸入是一個長度為 32 的二進位字串（即 0 ≤ <code>n</code> &lt; 2³²）",
 ],
 "mid": [
   ("note", "追問：如果這個函式會被呼叫很多次呢？", [
     "<strong>題目明講了：「If this function is called many times, how would you optimize it?」</strong>",
     "<strong>答案是查表法</strong> —— 預先算好 256 個位元組的反轉結果，"
     "<strong>每次呼叫只要四次查表加三次位移。</strong>見解法四。",
   ]),
 ],
 "idea": [
   ("fig", _P190_FIG, "0 0 640 384"),
   ("c", """【核心一行】

    res = (res << 1) | (n & 1)
    n >>= 1

    讀法：
        n & 1      取出 n 的【最低位】
        res << 1   把 res 整個左移，最低位空出來
        |          把剛取出的位填進去
        n >>= 1    n 丟掉最低位，換下一位

【為什麼這樣就是反轉？】

    第一個被取出的（n 的第 0 位）
    被後面 31 次左移推到最高位 -> 第 31 位 ✔

    最後一個被取出的（n 的第 31 位）
    沒有再被推，停在最低位 -> 第 0 位 ✔

    【先進來的跑最遠 —— 這就是反轉。】

【和「用堆疊反轉字串」是同一件事】：
    push 進去、pop 出來，順序自然顛倒。
    這裡 res 就是那個堆疊。

【一定要跑滿 32 圈】

    for _ in range(32):    ✔
    while n:               ✘ 在 Python 裡會少補前導 0

    例：n = 1
        跑滿 32 圈 -> res = 1 << 31 ✔
        while n 只跑 1 圈 -> res = 1 ✘

【複雜度】

    O(32) = O(1) 時間、O(1) 空間。

    這題的「優化」不是改變複雜度，
    而是把【常數】從 32 降到 5（分治）或 4（查表）。"""),
 ],
 "approaches": [
   ap("解法一", "逐位反轉（標準答案）", [
     ("c", S["p190"]),
     "<strong>五行，一定要會背。</strong>",
     ("h", "★ 為什麼 <code>range(32)</code> 不能換成 <code>while n</code>？"),
     ("c", """因為【前導 0 也要反轉】。

    n = 1 的 32 位表示是
        00000000000000000000000000000001
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 這 31 個 0 也要跑到後面去

    反轉後：
        10000000000000000000000000000000 = 2^31 ✔

    while n 在第一圈之後 n 就變 0 了 -> 停 -> res = 1 ✘

【在 C/Java 裡也一樣】——
    那邊 int 有固定 32 位，但迴圈次數還是要自己寫 32。

【這是這題最常見的錯誤】，而且範例 1、2 都測不出來
    （它們的最高位都不是 0），
    只有 n = 1 這種小數字會露餡。""",),
   ], "O(32) = O(1)", "O(1)", "固定 32 圈", "幾個變數", optimal=True),

   ap("解法二", "提早結束（剩下全是 0 就補位）", [
     ("c", S["p190_early"]),
     ("h", "省下來的是什麼？"),
     ("c", """如果 n 在第 i 圈就變成 0，
    代表【剩下的 32-i 位全是 0】。

    那些 0 反轉後還是 0，只要把 res 左移 (32-i) 位補齊就好 ✔

【什麼時候有用？】

    n 很小的時候（高位都是 0）。
    n = 1 -> 只跑 1 圈就結束。

【什麼時候沒用？】

    n 的最高位是 1 -> 還是要跑滿 32 圈。

【值不值得寫？】

    最壞情況一樣是 32，
    多了一個 if 判斷 ——

    【面試時提一下就好，不用真的寫】。
    真的要優化就直接跳到解法三或四。""",),
   ], "O(32) = O(1)", "O(1)", "最壞 32 圈", "幾個變數"),

   ap("解法三", "分治交換（五步）", [
     ("c", S["p190_dc"]),
     ("h", "★ 怎麼讀那些魔術數字？"),
     ("c", """把它們寫成二進位就很清楚：

    0x55555555 = 0101 0101 ... 【偶數位】（第 0, 2, 4, ... 位）
    0xAAAAAAAA = 1010 1010 ... 【奇數位】
    0x33333333 = 0011 0011 ... 【每 4 位的低 2 位】
    0xCCCCCCCC = 1100 1100 ... 【每 4 位的高 2 位】
    0x0F0F0F0F = 0000 1111 ... 【每個位元組的低 4 位】
    0xF0F0F0F0 = 1111 0000 ... 【每個位元組的高 4 位】
    0x00FF00FF = 每 16 位的低 8 位
    0xFF00FF00 = 每 16 位的高 8 位

【每一行在做什麼？】

    ((n & 高位遮罩) >> d) | ((n & 低位遮罩) << d)
       ^^^^^^^^^^^^^^^^^     ^^^^^^^^^^^^^^^^^
       高的搬到低             低的搬到高

    = 【把每一對相鄰的 d 位互換】

【為什麼交換 1,2,4,8,16 位就等於整個反轉？】

    以 8 位 abcdefgh 為例：

        兩兩交換：badcfehg
        四四交換：dcbahgfe
        八八交換：hgfedcba ✔

    【每一步都把「區塊內已經反轉好的部分」
      整塊搬到對稱位置】——
    這是標準的分治：
        reverse(X·Y) = reverse(Y)·reverse(X)

    和第 189 題的三次反轉是【同一個恆等式】✔

【★ 最後一定要 & 0xFFFFFFFF】

    Python 的 n << 16 不會溢位，
    高位會一路長出去 -> 答案錯 ✘

    C/Java 靠 uint32 自然截斷，Python 要自己來。

【速度】

    5 次運算 vs 32 次迴圈 -> 快約 6 倍。
    而且沒有分支，CPU 的管線很喜歡。""",),
   ], "5 步 = O(1)", "O(1)", "無迴圈、無分支", "幾個常數"),

   ap("解法四", "查表（回答「呼叫很多次」的追問）", [
     ("c", S["p190_cache"]),
     ("h", "★ 這才是追問要的答案"),
     ("c", """【把 32 位切成 4 個位元組】，
    每個位元組的反轉結果【預先算好放進表裡】。

    表的大小：256 個項目（每個位元組只有 256 種可能）。

    查詢時：
        4 次查表 + 3 次位移/或 -> 【O(1) 且常數極小】✔

【★ 位元組的順序要整個顛倒】

    原本的第 0 個位元組（最低）
    -> 反轉後要放到【最高】

    所以：
        t[n & 0xFF]        << 24   最低位元組 -> 最高
        t[(n >> 8) & 0xFF] << 16
        t[(n >> 16) & 0xFF] << 8
        t[(n >> 24) & 0xFF]        最高位元組 -> 最低

    【不只每個位元組內部要反轉，
      位元組之間的順序也要反轉】——
    這是最容易漏掉的一半 ✘

【表要怎麼算？】

    int(format(b, '08b')[::-1], 2)

    建表時用字串沒關係 —— 只做 256 次，一次性成本。
    【真正被反覆呼叫的那段沒有字串操作】 ✔

【還可以更快嗎？】

    切成 2 個 16 位 -> 只要 2 次查表，
    但表變成 65536 項（256 KB）——
    【快取放不下，反而變慢】。

    【256 項（1 KB 以內）剛好塞進 L1 快取】 ✔
    這是「查表法」的甜蜜點。

【一般化】：

    這就是【空間換時間 + 分塊預算】的標準套路。
    CRC32、Base64 編碼、UTF-8 解碼都用同樣的結構。""",),
   ], "建表 O(256)，之後 O(1)", "O(256)", "4 次查表", "1 KB 的表"),
 ],
 "compare": (["解法", "每次呼叫的運算量", "空間", "備註"],
   [["一、逐位", "32 圈", "O(1)", "標準答案 ✔"],
    ["二、提早結束", "最壞 32 圈", "O(1)", "小數字快一點"],
    ["三、分治", "5 步", "O(1)", "無分支，快 6 倍"],
    ["四、查表", "4 次查表", "O(256)", "回答追問用 ✔"]]),
 "edges": [
   "<strong><code>n = 0</code></strong> → <code>0</code>。",
   "<strong><code>n = 1</code></strong> → <code>2³¹ = 2147483648</code>。"
   "<strong>用 <code>while n</code> 的寫法會在這裡錯成 1。</strong>",
   "<strong><code>n = 2³¹</code></strong> → <code>1</code>（另一個方向）。",
   "<strong><code>n = 0xFFFFFFFF</code></strong> → <code>0xFFFFFFFF</code>（全 1，反轉還是自己）。",
   "<strong>分治法忘了 <code>&amp; 0xFFFFFFFF</code></strong> → "
   "<strong>Python 不會溢位，答案會大於 2³²。</strong>",
   "<strong>查表法只反轉位元組內部、忘了顛倒位元組順序</strong> → 只做對了一半。",
   "<strong>反轉兩次要回到自己</strong> —— <code>reverseBits(reverseBits(n)) == n</code>，"
   "這是最好用的自我驗算。",
 ],
 "follow": [
   ("h", "追問一：如果函式會被呼叫很多次，怎麼優化？"),
   ("c", """【這是題目明寫的追問，答案是查表法（解法四）】。

    完整的回答應該包含三層：

    1. 【分塊預算】：把 32 位切成 4 個位元組，
       預先算好 256 項的反轉表。

    2. 【為什麼是 256 項而不是 65536 項】：
       1 KB 的表塞得進 L1 快取，
       256 KB 的表會不斷 cache miss。

    3. 【如果輸入有重複】：
       再加一層 memoization（dict）——
       但只在「同樣的輸入真的會重複出現」時才划算，
       否則 dict 的雜湊成本比 4 次查表還高。

【面試官想聽到的是第 2 點】——
    「更大的表不一定更快」這個認知
    比「我知道要查表」更有價值 ✔""",),
   ("h", "追問二：怎麼反轉任意 k 位（不是 32 位）？"),
   ("c", """【逐位法】：把 range(32) 換成 range(k) ✔

    def reverseBits(n, k):
        res = 0
        for _ in range(k):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res

【分治法】：k 必須是 2 的冪，
    而且遮罩要跟著改 ——
    不是 2 的冪的話最後一層會對不齊 ✘

    所以【通用版只能用逐位法或查表法】。

【一個常見需求：反轉 n 的「有效位數」】

    例如 n = 0b1011 (11)，只反轉這 4 位 -> 0b1101 (13)。

    k = n.bit_length()

    注意 n = 0 時 bit_length() 是 0 -> 結果 0 ✔

    【這和本題不同】——
    本題一定要補滿 32 位的前導 0。""",),
   ("h", "追問三：Java 沒有無號整數，怎麼處理？"),
   ("c", """Java 的 int 是【有號 32 位】，
    最高位是符號位。

【兩個要點】：

    1. 【右移要用 >>> 而不是 >>】

       >>  是算術右移，會複製符號位（負數的高位補 1）✘
       >>> 是邏輯右移，高位補 0 ✔

    2. 【不用管溢位】

       int 天生就是 32 位，
       左移超出去的部分自動丟掉 ——
       反而比 Python 省事（不用 & 0xFFFFFFFF）✔

    public int reverseBits(int n) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            res = (res << 1) | (n & 1);
            n >>>= 1;                  // 注意三個 >
        }
        return res;
    }

【Python 的相反】：

    Python 沒有 >>> ——
    因為它的整數沒有固定寬度，
    正數右移本來就補 0 ✔
    （負數在 Python 裡是「無限多個 1」的補數，
      但本題輸入保證非負，不會遇到。）""",),
   ("h", "追問四：這題和第 191 題（數 1 的個數）有什麼關係？"),
   ("c", """【它們是同一個家族的兩種操作】：

    190：位元的【位置】重排（反轉）
    191：位元的【數量】統計（popcount）

    兩題都有三種層次的解法：

        逐位迴圈  -> 32 步
        分治      -> 5 步（190 的遮罩交換 / 191 的 SWAR）
        查表      -> 4 次

    【而且分治用的遮罩一模一樣】：
        0x55555555, 0x33333333, 0x0F0F0F0F ...

【差別】：

    190 的分治是「交換」：(a >> d) | (b << d)
    191 的分治是「相加」：(a) + (b >> d)

    【一個搬位置，一個做加法】——
    但都是「把問題切成兩半、分別解決、再合併」✔

【這組遮罩值得背起來】，
    位元運算題有一半會用到它們。""",),
 ],
 "related": [
   "<strong>第 191 題 位元 1 的個數</strong> —— 同一組遮罩，把交換換成相加",
   "<strong>第 338 題 位元計數</strong> —— <code>dp[i] = dp[i &gt;&gt; 1] + (i &amp; 1)</code>",
   "<strong>第 7 題 整數反轉</strong> —— 十進位版的反轉",
   "<strong>第 189 題 輪轉陣列</strong> —— 同一個 <code>reverse(A·B) = reverse(B)·reverse(A)</code>",
 ],
 "check": [
   "為什麼一定要跑滿 32 圈？<code>n = 1</code> 時 <code>while n</code> 會錯成什麼？",
   "<code>res = (res &lt;&lt; 1) | (n &amp; 1)</code> 為什麼能達成反轉？",
   "<code>0x55555555</code>、<code>0x33333333</code> 的二進位長什麼樣？",
   "查表法為什麼用 256 項而不是 65536 項？",
 ],
})
print("P190 written")

_P191_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ n &amp;= n − 1 每做一次，就消掉「最低位的那個 1」。做了幾次，就有幾個 1。</text>
            <g font-family="monospace" font-size="13">
              <text x="20" y="58" fill="var(--text-muted)">n     =</text>
              <text x="110" y="58" fill="var(--accent)">1 0 1 1 1 0 0 0</text>
              <text x="360" y="58" fill="var(--text-muted)">count = 0</text>
              <text x="20" y="86" fill="var(--text-muted)">n − 1 =</text>
              <text x="110" y="86" fill="var(--gold)">1 0 1 1 0 1 1 1</text>
              <text x="360" y="86" fill="var(--text-muted)">最低的 1 變 0，它右邊全變 1</text>
              <text x="20" y="114" fill="var(--text-muted)">n &amp; (n−1)</text>
              <text x="110" y="114" fill="#ff8a65">1 0 1 1 0 0 0 0</text>
              <text x="360" y="114" fill="var(--gold)">count = 1 ✔ 少了一個 1</text>
            </g>
            <line x1="20" y1="136" x2="620" y2="136" stroke="var(--border)"/>
            <g font-family="monospace" font-size="13">
              <text x="20" y="166" fill="var(--text-muted)">10111000</text>
              <text x="140" y="166" fill="var(--text-muted)">→</text>
              <text x="180" y="166" fill="var(--accent)">10110000</text>
              <text x="300" y="166" fill="var(--text-muted)">→</text>
              <text x="340" y="166" fill="var(--accent)">10100000</text>
              <text x="460" y="166" fill="var(--text-muted)">→</text>
              <text x="500" y="166" fill="var(--accent)">10000000</text>
              <text x="180" y="194" fill="var(--text-muted)">→</text>
              <text x="220" y="194" fill="var(--gold)">00000000</text>
              <text x="360" y="194" fill="var(--gold)">共 4 步 → 答案 4 ✔</text>
            </g>
            <text x="20" y="226" fill="var(--text-muted)" font-size="12">★ 迴圈次數 = 1 的個數，不是 32 —— 稀疏的數字特別快。</text>
            <line x1="20" y1="246" x2="620" y2="246" stroke="var(--border)"/>
            <text x="20" y="274" fill="#ff8a65" font-size="13">★ 為什麼 n − 1 剛好翻掉「最低的 1 以及它右邊的所有 0」？</text>
            <text x="40" y="304" fill="var(--text-muted)" font-size="12">把 n 寫成 　X 1 0 0 0（X 是任意高位，後面是最低的 1 和 k 個 0）</text>
            <text x="40" y="330" fill="var(--text-muted)" font-size="12">減 1 要向上借位，一路借到那個 1 → 　X 0 1 1 1</text>
            <text x="40" y="358" fill="var(--accent)" font-size="12">兩者 AND：高位 X 不變，低位全部相反 → 　X 0 0 0 0 ✔</text>
            <text x="40" y="386" fill="var(--gold)" font-size="12">高位完全沒動，所以「只消掉一個 1」這件事是精確的。</text>'''

emit({
 "num": 191, "slug": "number-of-1-bits",
 "en": [
   "Write a function that takes the binary representation of a positive integer and returns "
   "the number of set bits it has (also known as the "
   "<a href=\"https://en.wikipedia.org/wiki/Hamming_weight\">Hamming weight</a>).",
 ],
 "zh": [
   "給你一個正整數 <code>n</code>，回傳它的二進位表示中<strong>有幾個 1</strong>"
   "（這個數字叫做<strong>漢明重量 Hamming weight</strong>）。",
 ],
 "pre": [
   ("note", "★ 一句話解法：n &= n - 1", [
     ("c", """while n:
    n &= n - 1
    count += 1

【每執行一次，就消掉最低位的那個 1】。

    所以【執行了幾次，就有幾個 1】 ✔

【為什麼會這樣？】

    設 n 的最低位 1 在第 k 位：

        n     = X 1 000...0    （k 個 0）
        n - 1 = X 0 111...1    （借位，那個 1 變 0，右邊全變 1）
        ------------------------
        n & (n-1) = X 0 000...0

    【高位 X 完全沒動，只有那一個 1 被消掉】 ✔

【迴圈次數 = 1 的個數，不是 32】

    n = 2^31（只有一個 1）-> 跑 1 圈
    n = 0xFFFFFFFF（32 個 1）-> 跑 32 圈

    【稀疏的數字特別快】 —— 這是它比「逐位右移」好的地方。

【n & (n-1) 這個技巧的其他用途】：

    - 【判斷是不是 2 的冪】：n > 0 and n & (n-1) == 0
      （2 的冪只有一個 1，消掉之後就是 0）
    - 【消掉最低位的 1】：本題
    - 【取出最低位的 1】：n & -n（另一個常用式子）
    - 【枚舉所有子集】：sub = (sub - 1) & mask"""),
   ]),
 ],
 "examples": """範例 1
  輸入：n = 11    （二進位 1011）
  輸出：3

範例 2
  輸入：n = 128   （二進位 10000000）
  輸出：1

範例 3
  輸入：n = 2147483645  （二進位 1111111111111111111111111111101）
  輸出：30""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "mid": [
   ("note", "追問：如果會被呼叫很多次呢？", [
     "<strong>題目問：「If this function is called many times, how would you optimize it?」</strong>",
     "<strong>和第 190 題一樣，答案是查表</strong>（或者直接用 CPU 的 <code>POPCNT</code> 指令 —— "
     "<code>int.bit_count()</code> 在 CPython 3.10+ 就是它）。",
   ]),
 ],
 "idea": [
   ("fig", _P191_FIG, "0 0 640 410"),
   ("c", """【三種層次】

    1. 【逐位右移】：跑滿 32 圈，每圈看最低位

       for _ in range(32):
           count += n & 1
           n >>= 1

       最直白，但不管 n 多小都要跑 32 圈。

    2. 【n &= n-1】：跑「1 的個數」圈 ✔

       while n:
           n &= n - 1
           count += 1

       【這是標準答案】。

    3. 【SWAR 分治】：固定 4 步，無迴圈無分支

       用和第 190 題一樣的遮罩，
       但把「交換」換成「相加」。

【怎麼選？】

    面試 -> 寫第 2 種，提第 3 種
    競賽 -> 直接 bin(n).count('1') 或 n.bit_count()
    寫底層 -> 第 3 種（或 CPU 的 POPCNT）

【複雜度】

    三種都是 O(1)（因為位數固定 32）。

    差別在【常數】：
        逐位：32
        消 1：popcount(n)，最壞 32、平均 16
        SWAR：4

    以及【分支數】：
        前兩種有迴圈（分支預測會失敗）
        SWAR 完全沒有分支 -> CPU 最喜歡"""),
 ],
 "approaches": [
   ap("解法一", "n &amp;= n - 1 消去最低位的 1", [
     ("c", S["p191"]),
     "<strong>六行，面試標準答案。</strong>",
     ("h", "★ 一定要能當場證明「為什麼只消掉一個 1」"),
     ("c", """把 n 依「最低位的 1」切開：

    n = [高位部分 X] [1] [k 個 0]

減 1 時：
    最右邊是 0，不夠減 -> 向左借
    一路借到第一個 1 為止

    n-1 = [高位部分 X] [0] [k 個 1]
          ^^^^^^^^^^^^ 完全沒被動到

AND 起來：
    高位 X & X = X          （不變）
    [1] & [0] = 0           （最低的 1 被消掉）
    [0...0] & [1...1] = 0   （本來就是 0）

    n & (n-1) = [X] [0] [k 個 0] ✔

【恰好少一個 1，高位一個都沒少。】

【所以迴圈次數 = 1 的個數】 ✔

【延伸：n & -n 取出最低位的 1】

    -n 在補數表示下等於 ~n + 1

    n    = X 1 000
    -n   = ~X 1 000   （高位全部取反，最低位的 1 及其右邊不變）
    n&-n = 0 1 000    ★ 只剩最低位的那個 1

    【這兩個式子（n&(n-1) 消去、n&-n 取出）
      是位元運算的兩大基石】——
    樹狀陣列（Fenwick Tree）的 lowbit 就是 n & -n ✔""",),
     ("h", "Python 3.10+ 有內建"),
     ("c", """n.bit_count()      # Python 3.10+
bin(n).count('1')  # 任何版本

【競賽時直接用】。

    bit_count() 在 CPython 底層會用 CPU 的 POPCNT 指令，
    【一個 CPU 週期就算完】 ——
    比任何手寫版本都快。

【面試時不要直接用】——
    面試官問的是「你懂不懂位元運算」，
    不是「你知不知道標準函式庫」。

    但【寫完手動版之後提一句
    「實務上我會用 n.bit_count()」】
    會加分 ✔""",),
   ], "O(popcount(n)) ≤ O(32)", "O(1)", "1 越少越快", "幾個變數", optimal=True),

   ap("解法二", "逐位右移（最直白）", [
     ("c", S["p191_shift"]),
     ("h", "和解法一的差別"),
     ("ul", [
       "<strong>永遠跑 32 圈</strong>，不管 <code>n</code> 多小。",
       "<strong>但沒有資料相依的分支</strong> —— 迴圈次數固定，"
       "<strong>在某些情境下反而對分支預測更友善。</strong>",
       "<strong>在 Python 裡可以寫成 <code>while n:</code></strong>（正數右移會自然歸零），"
       "<strong>但那樣就要小心 <code>n</code> 是不是負數</strong>；"
       "本題保證 <code>n ≥ 1</code>，兩種都可以。",
       "<strong>如果題目改成「反轉位元」（第 190 題），<code>while n</code> 就會錯</strong> —— "
       "那裡前導 0 有意義，這裡沒有。",
     ]),
   ], "O(32) = O(1)", "O(1)", "固定 32 圈", "幾個變數"),

   ap("解法三", "SWAR 分治求和（4 步，無分支）", [
     ("c", S["p191_swar"]),
     ("h", "★ 逐行解讀"),
     ("c", """【SWAR = SIMD Within A Register】
    「在一個暫存器裡同時對很多小欄位做運算」。

【想法】：
    把 32 位切成 16 個 2 位的欄位，
    每個欄位存「這 2 位裡有幾個 1」（0~2，2 位夠裝）。
    然後兩兩相加 -> 8 個 4 位欄位（0~4）
    再兩兩相加 -> 4 個 8 位欄位（0~8）
    最後把 4 個位元組加起來 ✔

【第 1 行】n = n - ((n >> 1) & 0x55555555)

    這是「每 2 位求和」的【壓縮寫法】。

    正常寫法是：
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)

    但有一個恆等式：對 2 位的 ab 來說
        a + b = ab - a
    （驗算：00->0-0=0 ✔  01->1-0=1 ✔
            10->2-1=1 ✔  11->3-1=2 ✔）

    所以可以省一次 AND ✔

【第 2 行】n = (n & 0x33333333) + ((n >> 2) & 0x33333333)

    每 4 位求和。
    【這裡不能用第 1 行的技巧】——
    因為 4 位的值最大是 4，會進位到隔壁欄位 ✘
    所以老老實實做兩次 AND。

【第 3 行】n = (n + (n >> 4)) & 0x0F0F0F0F

    每 8 位求和。
    【這裡可以先加再遮罩】——
    因為每個 4 位欄位最大是 4，
    相加最大 8，【不會溢出 4 位（最大 15）】✔
    所以髒資料可以事後一次清掉。

【第 4 行】(n * 0x01010101) >> 24

    0x01010101 = 每個位元組都是 1。

    乘法等於「把四個位元組錯開相加」——
    最高的那個位元組剛好是【四個位元組的總和】✔

    右移 24 位取出來。

    ★ Python 要先 & 0xFFFFFFFF ——
      C 的 uint32 會自然截斷，Python 不會 ✘

【這四行是工業界的標準 popcount】，
    在沒有 POPCNT 指令的平台上就是用它。""",),
   ], "4 步 = O(1)", "O(1)", "無迴圈無分支", "幾個常數"),
 ],
 "compare": (["解法", "運算量", "分支", "備註"],
   [["一、n &amp;= n−1", "popcount(n) 圈", "有", "面試標準答案 ✔"],
    ["二、逐位右移", "32 圈", "有（固定）", "最直白"],
    ["三、SWAR", "4 步", "無", "工業界標準"],
    ["內建 bit_count()", "1 個 CPU 指令", "無", "實務首選"]]),
 "edges": [
   "<strong><code>n = 0</code></strong> → <code>0</code>（<code>while n</code> 一圈都不跑）。"
   "本題保證 <code>n ≥ 1</code>，但函式本身要能處理。",
   "<strong><code>n = 1</code></strong> → <code>1</code>。",
   "<strong><code>n = 2³¹ − 1</code></strong> → <code>31</code>（31 個 1）。",
   "<strong><code>n = 0xFFFFFFFF</code></strong> → <code>32</code>（解法一跑滿 32 圈）。",
   "<strong>SWAR 在 Python 忘了 <code>&amp; 0xFFFFFFFF</code></strong> → "
   "<strong>乘法結果不會截斷，右移 24 之後會多出高位垃圾。</strong>",
   "<strong>負數輸入</strong>（Java 的有號 int）→ <strong>右移要用 <code>&gt;&gt;&gt;</code>，"
   "否則符號位一直補 1 會無窮迴圈。</strong><code>n &amp;= n-1</code> 的版本沒這個問題。",
 ],
 "follow": [
   ("h", "追問一：如果會被呼叫很多次，怎麼優化？"),
   ("c", """和第 190 題一樣的三層回答：

    1. 【查表】：預先算好 0~255 的 popcount，
       每次 4 次查表相加。

       TABLE = [bin(i).count('1') for i in range(256)]

       def hammingWeight(n):
           return (TABLE[n & 0xFF] + TABLE[(n >> 8) & 0xFF] +
                   TABLE[(n >> 16) & 0xFF] + TABLE[n >> 24])

       ★ 這裡【不用顛倒順序】（和 190 不同）——
         因為加法沒有位置的概念 ✔

    2. 【SWAR】：4 步，不用表、不吃快取。

    3. 【CPU 指令】：x86 的 POPCNT、ARM 的 CNT。
       Python 3.10+ 的 n.bit_count() 會用它。

【哪個最快？】

    POPCNT > SWAR > 查表 > n&(n-1) > 逐位

    查表輸給 SWAR 是因為【記憶體存取比算術慢】——
    L1 快取命中也要 ~4 個週期，
    而 SWAR 的 4 步算術只要 ~4 個週期但可以管線化。

    【「查表一定比較快」在現代 CPU 上已經不成立了。】""",),
   ("h", "追問二：怎麼算 0 到 n 每個數字的 1 的個數？（第 338 題）"),
   ("c", """【對每個數字都跑一次 popcount 是 O(n log n)】。

【DP 只要 O(n)】：

    dp[i] = dp[i >> 1] + (i & 1)

    讀法：i 的 1 的個數
        = (i 去掉最低位之後的 1 的個數) + (最低位是不是 1)

    dp[0] = 0

【另一個寫法（用 n & (n-1)）】：

    dp[i] = dp[i & (i-1)] + 1

    讀法：消掉一個 1 之後的個數，再加 1 ✔

    【這個版本更直接體現本題的核心式子。】

【兩個都對，都是 O(n) 時間、O(n) 空間。】

【驗算】i = 6 (110)
    dp[6] = dp[3] + 0 = 2 + 0 = 2 ✔
    dp[6] = dp[6 & 5] + 1 = dp[4] + 1 = 1 + 1 = 2 ✔""",),
   ("h", "追問三：n &amp; -n 是什麼？和 n &amp; (n-1) 有什麼關係？"),
   ("c", """【n & (n-1)】= 【消掉】最低位的 1
【n & -n】    = 【取出】最低位的 1

    n      = 1011 1000
    n-1    = 1011 0111
    n&(n-1)= 1011 0000   ★ 少了那個 1

    -n     = 0100 1000   （~n + 1）
    n&-n   = 0000 1000   ★ 只剩那個 1

【兩者相加剛好還原】：

    (n & (n-1)) | (n & -n) == n ✔

【n & -n 的經典用途】：

    1. 【樹狀陣列的 lowbit】

       i += i & -i    往上走
       i -= i & -i    往下走

    2. 【枚舉 bitmask 的每一個 1】

       while mask:
           low = mask & -mask
           bit = low.bit_length() - 1
           ...處理第 bit 位...
           mask ^= low

    3. 【判斷 2 的冪】

       n & -n == n   <=>   n 只有一個 1

【為什麼 -n 長那樣？】

    補數：-n = ~n + 1

    ~n 把每一位翻轉：
        n  = X 1 000
        ~n = ~X 0 111
    +1 之後低位進位：
        -n = ~X 1 000

    最低位的 1 及其右邊【和 n 一模一樣】，
    高位全部相反 -> AND 之後只剩那一位 ✔""",),
   ("h", "追問四：兩個數字有幾位不同？（漢明距離，第 461 題）"),
   ("c", """【一行】：

    def hammingDistance(x, y):
        return bin(x ^ y).count('1')

    或用本題的解法：

        return hammingWeight(x ^ y)

【為什麼是 XOR？】

    XOR 的定義就是「兩邊不同時為 1」——
    所以 x ^ y 的每個 1
    就代表【x 和 y 在那一位不同】✔

    數一數有幾個 1 = 有幾位不同 ✔

【延伸：一組數字兩兩的漢明距離總和（第 477 題）】

    暴力 O(n²) 會超時。

    【按位統計】：
        對第 k 位，設有 c 個數字是 1、n-c 個是 0
        -> 這一位貢獻 c × (n-c) 對

        總和 = Σ_k c_k × (n - c_k)

    O(32n) ✔

    【「按位拆開統計」是位元題最常用的降維手法】。""",),
 ],
 "related": [
   "<strong>第 190 題 顛倒二進位位元</strong> —— 同一組遮罩，交換版",
   "<strong>第 338 題 位元計數</strong> —— <code>dp[i] = dp[i &amp; (i-1)] + 1</code>",
   "<strong>第 231 題 2 的冪</strong> —— <code>n &gt; 0 and n &amp; (n-1) == 0</code>",
   "<strong>第 461 題 漢明距離</strong> —— <code>popcount(x ^ y)</code>",
   "<strong>第 477 題 漢明距離總和</strong> —— 按位統計",
 ],
 "check": [
   "為什麼 <code>n &amp; (n-1)</code> 剛好消掉一個 1？請用借位的過程解釋。",
   "<code>n &amp; -n</code> 做什麼？和 <code>n &amp; (n-1)</code> 的關係是什麼？",
   "SWAR 的第 1 行為什麼可以用減法代替一次 AND？第 2 行為什麼不行？",
   "查表版的 popcount 為什麼不用顛倒位元組順序（但第 190 題要）？",
 ],
})
print("P191 written")

# ==================== 198. House Robber ====================
S["p198"] = '''class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, cur = 0, 0        # prev = f(i-2), cur = f(i-1)
        for x in nums:
            prev, cur = cur, max(cur, prev + x)
        return cur'''

S["p198_dp"] = '''class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n            # dp[i] = 只考慮前 i+1 間房的最大金額
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1],          # 不偷第 i 間
                        dp[i - 2] + nums[i])  # 偷第 i 間
        return dp[n - 1]'''

S["p198_state"] = '''class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_it, skip_it = 0, 0   # 這一間偷 / 這一間不偷，各自的最大金額
        for x in nums:
            rob_it, skip_it = skip_it + x, max(rob_it, skip_it)
        return max(rob_it, skip_it)'''


def _p198_ref(nums):
    """獨立參考解：枚舉所有「沒有兩個相鄰」的子集。"""
    n = len(nums)
    best = 0
    for mask in range(1 << n):
        if mask & (mask << 1):
            continue
        best = max(best, sum(nums[i] for i in range(n) if mask >> i & 1))
    return best


_p198 = [S.load(x) for x in ("p198", "p198_dp", "p198_state")]

for nums, want in [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([5], 5),
    ([2, 1], 2),
    ([0], 0),
    ([2, 1, 1, 2], 4),
]:
    assert _p198_ref(nums) == want, ("P198 ref", nums, _p198_ref(nums))
    for sol in _p198:
        assert sol.rob(list(nums)) == want, ("P198", nums, want, sol)

for _ in range(3000):
    n = random.randrange(1, 15)
    nums = [random.randint(0, 40) for _ in range(n)]
    want = _p198_ref(nums)
    for sol in _p198:
        got = sol.rob(list(nums))
        assert got == want, ("P198 random", nums, want, got, sol)
print("P198 solutions OK")


# ==================== 199. Binary Tree Right Side View ====================
S["p199"] = '''from collections import deque


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res, q = [], deque([root])
        while q:
            res.append(q[-1].val)        # ★ 這一層最右邊那個
            for _ in range(len(q)):      # 把整層換成下一層
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res'''

S["p199_dfs"] = '''class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):        # ★ 這一層第一次被走到
                res.append(node.val)
            dfs(node.right, depth + 1)   # ★ 先右後左
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res'''

S["p199_iter"] = '''class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], [(root, 0)]
        while stack:
            node, depth = stack.pop()
            if not node:
                continue
            if depth == len(res):
                res.append(node.val)
            stack.append((node.left, depth + 1))   # 後進先出：先推左
            stack.append((node.right, depth + 1))  # 再推右 → 右先被彈出
        return res'''


def _p199_ref(root):
    """獨立參考解：老實做層序走訪，每層取最後一個。"""
    out, level = [], [root] if root else []
    while level:
        out.append(level[-1].val)
        nxt = []
        for nd in level:
            if nd.left:
                nxt.append(nd.left)
            if nd.right:
                nxt.append(nd.right)
        level = nxt
    return out


_p199 = [S.load(x) for x in ("p199", "p199_dfs", "p199_iter")]

for spec, want in [
    ((1, (2, None, (5, None, None)), (3, None, (4, None, None))), [1, 3, 4]),
    ((1, None, (3, None, None)), [1, 3]),
    ((1, (2, (4, None, None), None), (3, None, None)), [1, 3, 4]),
    ((1, (2, None, None), None), [1, 2]),
    ((1, None, None), [1]),
]:
    t = _build(spec)
    assert _p199_ref(t) == want, ("P199 ref", spec, _p199_ref(t))
    for sol in _p199:
        assert sol.rightSideView(_build(spec)) == want, ("P199", spec, want, sol)

for sol in _p199:
    assert sol.rightSideView(None) == [], "P199 空樹"

for _ in range(3000):
    t = _rand_tree(random.randrange(1, 14))
    want = _p199_ref(t)
    for sol in _p199:
        got = sol.rightSideView(t)
        assert got == want, ("P199 random", want, got, sol)
print("P199 solutions OK")

# ==================== 200. Number of Islands ====================
S["p200"] = '''class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        def sink(i: int, j: int) -> None:
            stack = [(i, j)]
            grid[i][j] = '0'                    # ★ 推進堆疊時就標記
            while stack:
                r, c = stack.pop()
                for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        stack.append((nr, nc))

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    sink(i, j)
        return count'''

S["p200_rec"] = '''class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        def sink(i: int, j: int) -> None:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '0'                    # ★ 先淹掉，再往四周走
            sink(i + 1, j)
            sink(i - 1, j)
            sink(i, j + 1)
            sink(i, j - 1)

        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    sink(i, j)
        return count'''

S["p200_bfs"] = '''from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                count += 1
                grid[i][j] = '0'
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()
                    for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                        if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'   # ★ 入隊時標記，不是出隊時
                            q.append((nr, nc))
        return count'''

S["p200_uf"] = '''class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])

        parent = list(range(m * n))
        count = sum(row.count('1') for row in grid)   # 先當成各自獨立

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]         # 路徑減半
                x = parent[x]
            return x

        def union(a: int, b: int) -> None:
            nonlocal count
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[ra] = rb
                count -= 1                            # ★ 每合併一次少一座島

        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                for ni, nj in ((i + 1, j), (i, j + 1)):   # 只看右和下就夠
                    if ni < m and nj < n and grid[ni][nj] == '1':
                        union(i * n + j, ni * n + nj)
        return count'''

S["p200_keep"] = '''class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        seen = set()                                  # ★ 不改動 grid
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1' or (i, j) in seen:
                    continue
                count += 1
                stack = [(i, j)]
                seen.add((i, j))
                while stack:
                    r, c = stack.pop()
                    for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                        if (0 <= nr < m and 0 <= nc < n
                                and grid[nr][nc] == '1' and (nr, nc) not in seen):
                            seen.add((nr, nc))
                            stack.append((nr, nc))
        return count'''


def _p200_ref(grid):
    """獨立參考解：反覆掃描，用「標籤傳播」到穩定為止，再數不同標籤。"""
    m, n = len(grid), len(grid[0]) if grid else 0
    lab = [[-1] * n for _ in range(m)]
    nxt = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                lab[i][j] = nxt
                nxt += 1
    changed = True
    while changed:
        changed = False
        for i in range(m):
            for j in range(n):
                if lab[i][j] < 0:
                    continue
                for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                    if 0 <= ni < m and 0 <= nj < n and lab[ni][nj] >= 0:
                        lo = min(lab[i][j], lab[ni][nj])
                        if lab[i][j] != lo or lab[ni][nj] != lo:
                            lab[i][j] = lab[ni][nj] = lo
                            changed = True
    return len({lab[i][j] for i in range(m) for j in range(n) if lab[i][j] >= 0})


_p200 = [S.load(x) for x in ("p200", "p200_rec", "p200_bfs", "p200_uf", "p200_keep")]

_G1 = [list("11110"), list("11010"), list("11000"), list("00000")]
_G2 = [list("11000"), list("11000"), list("00100"), list("00011")]
for g, want in [(_G1, 1), (_G2, 3), ([list("0")], 0), ([list("1")], 1),
                ([list("101"), list("010"), list("101")], 5)]:
    assert _p200_ref(g) == want, ("P200 ref", g, _p200_ref(g))
    for sol in _p200:
        assert sol.numIslands([row[:] for row in g]) == want, ("P200", want, sol)

# p200_keep 不可以改動 grid
_snap = [row[:] for row in _G1]
_p200[4].numIslands(_snap)
assert _snap == _G1, "P200 解法五不該改動 grid"

for _ in range(1500):
    m = random.randrange(1, 7)
    n = random.randrange(1, 7)
    g = [[random.choice("01") for _ in range(n)] for _ in range(m)]
    want = _p200_ref(g)
    for sol in _p200:
        got = sol.numIslands([row[:] for row in g])
        assert got == want, ("P200 random", g, want, got, sol)
print("P200 solutions OK")

_P198_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 到第 i 間房為止的最大金額，只有兩種可能：不偷這間（沿用 i−1），或偷這間（i−2 的錢 + nums[i]）。</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="48" width="70" height="36" fill="none" stroke="var(--border)" stroke-width="1.5"/><text x="75" y="72" fill="var(--text-muted)">f(i−2)</text>
              <rect x="170" y="48" width="70" height="36" fill="none" stroke="var(--border)" stroke-width="1.5"/><text x="205" y="72" fill="var(--text-muted)">f(i−1)</text>
              <rect x="300" y="48" width="70" height="36" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="335" y="72" fill="var(--gold)">f(i)</text>
            </g>
            <g stroke="var(--accent)" stroke-width="1.5" fill="none">
              <path d="M 240 66 L 294 66"/><polygon points="294,66 286,62 286,70" fill="var(--accent)"/>
              <path d="M 75 48 C 100 6 300 6 330 44"/><polygon points="330,44 322,36 337,36" fill="var(--accent)"/>
            </g>
            <text x="252" y="58" fill="var(--accent)" font-size="11" text-anchor="middle">不偷</text>
            <text x="200" y="18" fill="var(--accent)" font-size="11" text-anchor="middle">偷（+ nums[i]）</text>
            <text x="400" y="72" fill="var(--text-muted)" font-size="12">f(i) = max(f(i−1), f(i−2) + nums[i])</text>
            <line x1="20" y1="104" x2="620" y2="104" stroke="var(--border)"/>
            <text x="20" y="132" fill="#ff8a65" font-size="13">★ nums = [2, 7, 9, 3, 1] 的推演</text>
            <g font-family="monospace" font-size="12">
              <text x="40" y="162" fill="var(--text-muted)">nums   =　 2 　 7 　 9 　 3 　 1</text>
              <text x="40" y="188" fill="var(--accent)">f　　　=　 2 　 7 　11 　11 　12</text>
              <text x="40" y="220" fill="var(--text-muted)">f(2) = max(f(1), f(0)+9) = max(7, 2+9) = 11　偷第 0 和第 2 間</text>
              <text x="40" y="246" fill="var(--text-muted)">f(3) = max(f(2), f(1)+3) = max(11, 7+3) = 11　不偷第 3 間</text>
              <text x="40" y="272" fill="var(--gold)">f(4) = max(f(3), f(2)+1) = max(11, 11+1) = 12　偷 0、2、4 ✔</text>
            </g>
            <line x1="20" y1="296" x2="620" y2="296" stroke="var(--border)"/>
            <text x="20" y="324" fill="var(--accent)" font-size="13">★ 為什麼「貪心拿最大的」是錯的？</text>
            <text x="40" y="354" fill="var(--text-muted)" font-size="12">nums = [2, 1, 1, 2]：貪心先拿 2（index 0），再拿 2（index 3）→ 4，碰巧對。</text>
            <text x="40" y="380" fill="#ff8a65" font-size="12">nums = [2, 3, 2]：貪心先拿 3 → 兩邊的 2 都不能拿 → 3 ✘　正解是 2 + 2 = 4。</text>
            <text x="40" y="406" fill="var(--gold)" font-size="12">「當下最好」會鎖死未來的選擇 → 要 DP，不能貪心。</text>'''

emit({
 "num": 198, "slug": "house-robber",
 "en": [
   "You are a professional robber planning to rob houses along a street. Each house has a "
   "certain amount of money stashed, the only constraint stopping you from robbing each of them "
   "is that adjacent houses have security systems connected and "
   "<strong>it will automatically contact the police if two adjacent houses were broken into on "
   "the same night</strong>.",
   "Given an integer array <code>nums</code> representing the amount of money of each house, "
   "return <em>the maximum amount of money you can rob tonight <strong>without alerting the "
   "police</strong></em>.",
 ],
 "zh": [
   "你是一個小偷，要偷一整排房子。每間房子裡有一定數量的錢。",
   "唯一的限制是：<strong>相鄰的兩間房子裝了連動的保全系統</strong> —— "
   "同一晚偷了相鄰的兩間就會自動報警。",
   "給你陣列 <code>nums</code>（每間房子的金額），"
   "回傳<strong>在不驚動警察的前提下，今晚最多能偷到多少錢</strong>。",
 ],
 "pre": [
   ("note", "★ 這是「動態規劃」的入門第一題", [
     ("c", """【問題的本質】：

    從一排數字裡挑出一些，【不能挑相鄰的】，求最大和。

【最重要的觀念：不能用貪心】

    「先拿最大的那個」是錯的：

        nums = [2, 3, 2]

        貪心：拿 3 -> 左右的 2 都不能拿 -> 3 ✘
        正解：拿 2 + 2 = 4 ✔

    【因為「當下最好的選擇」會鎖死未來】——
    這正是「需要 DP 而不是貪心」的訊號。

【DP 的三個步驟】：

    1. 【定義狀態】
       f(i) = 只考慮前 i+1 間房時，能偷到的最大金額

    2. 【寫轉移式】
       對第 i 間房，只有兩種選擇：

           不偷 -> f(i-1)
           偷   -> f(i-2) + nums[i]
                   ^^^^^^ 不能是 f(i-1)，因為 i-1 可能被偷了

           f(i) = max(f(i-1), f(i-2) + nums[i])

    3. 【處理初始值】
       f(0) = nums[0]
       f(1) = max(nums[0], nums[1])

    答案是 f(n-1) ✔

【然後發現只用到前兩項 -> 滾動成兩個變數 -> O(1) 空間 ✔】

    【「寫出 DP 陣列 -> 觀察只用到最近幾項 -> 滾動」
      這個流程，在 DP 題裡會用上百次。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,2,3,1]
  輸出：4
  說明：偷第 0 間（1）和第 2 間（3）-> 1 + 3 = 4。
        不能偷第 1 和第 2 間（相鄰）。

範例 2
  輸入：nums = [2,7,9,3,1]
  輸出：12
  說明：偷第 0、2、4 間 -> 2 + 9 + 1 = 12。

        ★ 注意不是「2 + 9 = 11」也不是「7 + 3 = 10」——
          要偷三間才最多。

範例 3（貪心會錯的例子）
  輸入：nums = [2,3,2]
  輸出：4
  說明：偷第 0 和第 2 間 -> 2 + 2 = 4。
        貪心拿最大的 3，反而只有 3。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 100",
   "0 ≤ <code>nums[i]</code> ≤ 400",
 ],
 "mid": [
   ("note", "注意：金額可以是 0", [
     "<strong><code>nums[i]</code> 的下界是 0，不是 1。</strong>",
     "<strong>這代表「偷一間 0 元的房子」和「不偷」的金額一樣</strong> —— "
     "不影響答案，但如果你想順便記錄「偷了哪幾間」，答案就不唯一了。",
     "<strong>另外因為金額非負，<code>f(i)</code> 一定單調不減</strong> —— "
     "這保證了「用不滿」的情況自動被涵蓋。",
   ]),
 ],
 "idea": [
   ("fig", _P198_FIG, "0 0 640 430"),
   ("c", """【狀態定義是關鍵】

    f(i) = 「只考慮前 i+1 間房」的最大金額

    ★ 注意它【不要求一定要偷第 i 間】——
      它是「到目前為止的最好結果」。

    如果定義成「一定偷第 i 間」，
    那答案就要在最後取 max(f(n-1), f(n-2))，
    多一個步驟、多一個出錯機會。

    【選一個讓最後答案最單純的定義。】

【轉移式的推導】

    對第 i 間房，做決策：

        情況 A：不偷第 i 間
            -> 前 i 間可以隨便偷 -> f(i-1)

        情況 B：偷第 i 間
            -> 第 i-1 間【一定不能偷】
            -> 只能從前 i-1 間（也就是 f(i-2)）接上來
            -> f(i-2) + nums[i]

    兩種取大的：

        f(i) = max(f(i-1), f(i-2) + nums[i])

【★ 為什麼情況 B 是 f(i-2) 而不是「f(i-1) 減掉第 i-1 間」？】

    因為 f(i-1) 只是一個【數字】，
    我們不知道它有沒有偷第 i-1 間 ——
    沒辦法「減掉」。

    【f(i-2) 才保證「第 i-1 間沒被偷」】 ✔

    這是初學者最常卡住的地方。

【滾動變數】

    f(i) 只用到 f(i-1) 和 f(i-2)
    -> 兩個變數就夠：

        prev, cur = cur, max(cur, prev + x)

    ★ 這一行的 prev 和 cur 是【同時】取值的
      （Python 的 tuple 賦值先算右邊）——
      不用擔心覆蓋順序 ✔

    寫成兩行就要小心：
        tmp = cur
        cur = max(cur, prev + x)
        prev = tmp          ← 不能寫成 prev = cur ✘

【初始值】

    prev = cur = 0

    這代表「一間房都沒有時金額是 0」——
    自然涵蓋了 n = 1 的情況，
    【不用特判】 ✔

【複雜度】O(n) 時間、O(1) 空間"""),
 ],
 "approaches": [
   ap("解法一", "滾動兩個變數（最精簡）", [
     ("c", S["p198"]),
     "<strong>五行，O(n) 時間、O(1) 空間。這一題的最終形態。</strong>",
     ("h", "★ 為什麼不用特判 <code>n == 1</code>？"),
     ("c", """因為 prev = cur = 0 已經把「空陣列」的情況定義好了。

    n = 1, nums = [5]：
        第一圈：prev, cur = 0, max(0, 0 + 5) = 0, 5
        回傳 cur = 5 ✔

    n = 0（題目保證不會，但）：
        迴圈不跑，回傳 0 ✔

    【好的初始值可以消掉所有特判】——
    這是寫 DP 的一個小技巧：
    把「什麼都沒有」也當成一個合法狀態。

【解法二（陣列版）就必須特判】

    dp[1] = max(nums[0], nums[1])

    n = 1 時 nums[1] 會越界 ✘

    -> 所以解法二開頭要寫 if n == 1: return nums[0]

    【這就是為什麼滾動版更好】。""",),
     ("h", "一行版（炫技用，不建議面試寫）"),
     ("c", """from functools import reduce

def rob(nums):
    return reduce(lambda a, x: (a[1], max(a[1], a[0] + x)), nums, (0, 0))[1]

【對，但沒人看得懂】。

    面試時清楚 > 精簡。
    五行的版本已經夠短了 ✔""",),
   ], "O(n)", "O(1)", "掃一次", "兩個變數", optimal=True),

   ap("解法二", "DP 陣列（最好理解）", [
     ("c", S["p198_dp"]),
     ("h", "什麼時候該寫這個版本？"),
     ("ul", [
       "<strong>第一次想這題的時候</strong> —— 陣列版把每一步的中間結果都留著，好除錯。",
       "<strong>需要「回溯出偷了哪幾間」的時候</strong> —— "
       "<strong>滾動版把中間結果丟掉了，沒辦法回溯。</strong>",
       "<strong>面試時先寫這個，再說「只用到前兩項，可以滾動成 O(1) 空間」然後改</strong> —— "
       "<strong>展示思考過程比直接給最終答案更好。</strong>",
     ]),
     ("h", "★ 怎麼從 dp 陣列回溯出「偷了哪幾間」？"),
     ("c", """從後往前走：

    i = n - 1
    picked = []
    while i >= 0:
        if i == 0 or dp[i] != dp[i-1]:
            # dp[i] 比 dp[i-1] 大 -> 一定偷了第 i 間
            picked.append(i)
            i -= 2
        else:
            i -= 1
    picked.reverse()

【原理】：

    dp[i] != dp[i-1]  <=>  「偷第 i 間」比「不偷」好
                       ->  第 i 間被偷了 -> 跳兩格

    dp[i] == dp[i-1]  ->  不偷第 i 間也能達到 -> 跳一格

【注意】金額可能是 0，
    這時「偷」和「不偷」金額相同 -> dp[i] == dp[i-1]
    -> 回溯會選「不偷」。

    【答案仍然是最大的，只是方案不唯一】 ✔""",),
   ], "O(n)", "O(n)", "掃一次", "dp 陣列"),

   ap("解法三", "兩個狀態（狀態機寫法）", [
     ("c", S["p198_state"]),
     ("h", "和解法一是同一件事，但語意更清楚"),
     ("c", """rob_it  = 「這一間【偷】」時，到目前為止的最大金額
skip_it = 「這一間【不偷】」時，到目前為止的最大金額

轉移：
    新的 rob_it  = 舊的 skip_it + x
                   ^^^^^^^^^^^^ 上一間一定沒偷

    新的 skip_it = max(舊的 rob_it, 舊的 skip_it)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 上一間偷不偷都行

答案 = max(rob_it, skip_it)

【為什麼這個寫法值得學？】

    因為它【可以直接推廣】：

    - 第 213 題（環形）：跑兩次，分別排除頭和尾
    - 第 337 題（樹形）：每個節點回傳 (偷, 不偷) 兩個值
    - 第 121/122/123/188 題（股票）：同樣是「持有 / 不持有」

    【「為每種決策狀態各開一個變數」
      是狀態機 DP 的通用寫法】 ✔

    解法一的 prev/cur 比較精簡，
    但語意不如這個直白 ——
    【一旦問題變複雜（多一個狀態），
      狀態機寫法就完勝】。""",),
   ], "O(n)", "O(1)", "掃一次", "兩個變數"),
 ],
 "compare": (["解法", "時間", "空間", "能否回溯方案", "備註"],
   [["一、滾動變數", "O(n)", "O(1)", "否", "最精簡 ✔"],
    ["二、DP 陣列", "O(n)", "O(n)", "可以", "最好理解"],
    ["三、狀態機", "O(n)", "O(1)", "否", "最好推廣 ✔"]]),
 "edges": [
   "<strong><code>n = 1</code></strong> → <code>nums[0]</code>。"
   "<strong>解法一靠 <code>prev = cur = 0</code> 自動處理；解法二必須特判。</strong>",
   "<strong><code>n = 2</code></strong> → <code>max(nums[0], nums[1])</code>。",
   "<strong>全部是 0</strong> → <code>0</code>。",
   "<strong><code>[2,3,2]</code></strong> → <code>4</code>。"
   "<strong>貪心拿最大的會得到 3 —— 這是必測的反例。</strong>",
   "<strong><code>[2,1,1,2]</code></strong> → <code>4</code>（偷頭尾）。"
   "<strong>測「跳兩格」的路徑。</strong>",
   "<strong>遞增序列 <code>[1,2,3,4,5]</code></strong> → <code>9</code>（偷 1、3、5 → 1+3+5）。",
   "<strong>滾動變數寫成兩行、順序寫反</strong> → "
   "<strong><code>prev</code> 拿到已經更新過的 <code>cur</code> → 答案偏大。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果房子排成一個環呢？（第 213 題）"),
   ("c", """【第 0 間和第 n-1 間變成相鄰】。

【關鍵觀察】：
    第 0 間和第 n-1 間【最多只能偷一間】。

    所以拆成兩個線性子問題：

        情況 A：不偷第 n-1 間 -> rob(nums[0 : n-1])
        情況 B：不偷第 0 間   -> rob(nums[1 : n])

        答案 = max(A, B)

    def rob(nums):
        if len(nums) == 1:
            return nums[0]
        return max(linear(nums[:-1]), linear(nums[1:]))

【為什麼這樣是對的？】

    最佳解一定屬於以下三種之一：
        1. 偷第 0 間、不偷第 n-1 間 -> 被 A 涵蓋
        2. 不偷第 0 間、偷第 n-1 間 -> 被 B 涵蓋
        3. 兩間都不偷 -> A 和 B 都涵蓋（重複計算沒關係，取 max）

    【沒有遺漏，也沒有非法解】 ✔

    ★ 注意 A 和 B 都【允許】兩間都不偷 ——
      重複不影響 max ✔

【n = 1 一定要特判】

    nums[:-1] 和 nums[1:] 都是空的 -> 兩邊都回 0 ✘
    正確答案是 nums[0]。

【這個「拆成兩個線性問題」的手法很通用】——
    環形問題常常可以用「固定某個元素的取捨」來拆。""",),
   ("h", "追問二：如果房子排成一棵樹呢？（第 337 題）"),
   ("c", """【樹形 DP】：每個節點回傳兩個值。

    def dfs(node):
        if not node:
            return (0, 0)        # (偷這個, 不偷這個)
        l = dfs(node.left)
        r = dfs(node.right)

        rob_it  = node.val + l[1] + r[1]   # 偷了就不能偷小孩
        skip_it = max(l) + max(r)          # 不偷，小孩隨意
        return (rob_it, skip_it)

    return max(dfs(root))

【和解法三（狀態機）一模一樣的結構】——
    只是「上一間」換成「兩個小孩」✔

【為什麼不能只回傳一個值？】

    因為父節點需要知道
    「小孩【沒被偷】時的最大值」——
    單一個 max 值沒有這個資訊。

    【這是樹形 DP 的核心：
      回傳一個「狀態向量」而不是單一數字。】

【複雜度】O(n)，每個節點走一次 ✔""",),
   ("h", "追問三：如果不能偷「距離 k 以內」的房子呢？"),
   ("c", """【轉移式變成】：

    f(i) = max(f(i-1), f(i-k-1) + nums[i])
                       ^^^^^^^^ 往前跳 k+1 格

    k = 1 就是本題 ✔

【還是 O(n)，但空間變成 O(k)】
    （要記住最近 k+1 項）。

    用一個長度 k+1 的環狀陣列就好。

【如果 k 很大（接近 n）】：

    那幾乎只能偷一間 -> 答案是 max(nums) ——
    可以特判掉。

【另一個變形：最多偷 m 間】

    f(i, j) = 前 i 間、最多偷 j 間的最大金額
            = max(f(i-1, j), f(i-2, j-1) + nums[i])

    O(nm) 時間、O(m) 空間（滾動掉 i）✔

    【多一個限制就多一維】——
    這是 DP 的通則。""",),
   ("h", "追問四：為什麼這題不能用貪心？怎麼判斷一題該用貪心還是 DP？"),
   ("c", """【反例】nums = [2, 3, 2]

    貪心（每次拿當前最大的可用值）：
        拿 3 -> 左右的 2 都被封鎖 -> 總共 3 ✘

    正解：2 + 2 = 4 ✔

【判斷準則】：

    貪心成立需要【「貪心選擇性質」】——
    「當下的最佳選擇一定屬於某個全域最佳解」。

    這題不成立：
        拿走 3 會【封鎖兩個鄰居】，
        代價可能超過收益 ✘

【什麼時候貪心會成立？】

    - 第 122 題（股票無限次）：每次上漲都拿，
      拿了【不會影響別的機會】 -> 貪心 ✔

    - 第 55 題（跳躍遊戲）：維護最遠可達點，
      【單調擴張，沒有取捨】 -> 貪心 ✔

【一句話判準】：

    「這個選擇會不會【排除】掉其他選擇？」

        不會 -> 通常可以貪心
        會   -> 要 DP（把「排除的代價」算進狀態裡）

【安全做法】：
    先想一個小反例試試看貪心。
    想不出反例，再嘗試證明；
    證不出來就寫 DP ——
    【DP 幾乎不會錯，只是慢一點】。""",),
 ],
 "related": [
   "<strong>第 213 題 打家劫舍 II</strong> —— 環形，拆成兩個線性問題",
   "<strong>第 337 題 打家劫舍 III</strong> —— 樹形 DP，回傳 (偷, 不偷)",
   "<strong>第 740 題 刪除並獲得點數</strong> —— 換個包裝的同一題",
   "<strong>第 70 題 爬樓梯</strong> —— 同樣是 <code>f(i)</code> 只依賴前兩項",
   "<strong>第 121/122/123/188 題 股票系列</strong> —— 狀態機 DP 的推廣",
 ],
 "check": [
   "為什麼「偷第 i 間」要接 <code>f(i-2)</code> 而不能從 <code>f(i-1)</code> 減掉？",
   "<code>nums = [2,3,2]</code> 為什麼貪心會錯？",
   "為什麼滾動版不用特判 <code>n == 1</code>，陣列版卻要？",
   "環形版（第 213 題）為什麼「跑兩次、各去掉一端」是完備的？",
 ],
})
print("P198 written")

_P199_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 從右邊看過去，每一層只看得到「最右邊那一個」——注意不一定是右子樹的節點。</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="300" cy="62" r="18" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="300" y="67" fill="var(--gold)">1</text>
              <circle cx="200" cy="132" r="18" fill="none" stroke="var(--border)" stroke-width="1.5"/><text x="200" y="137" fill="var(--text-muted)">2</text>
              <circle cx="400" cy="132" r="18" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="400" y="137" fill="var(--gold)">3</text>
              <circle cx="140" cy="202" r="18" fill="none" stroke="var(--border)" stroke-width="1.5"/><text x="140" y="207" fill="var(--text-muted)">4</text>
              <circle cx="260" cy="202" r="18" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="260" y="207" fill="var(--gold)">5</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="288" y1="76" x2="212" y2="118"/><line x1="312" y1="76" x2="388" y2="118"/>
              <line x1="188" y1="146" x2="152" y2="188"/><line x1="212" y1="146" x2="248" y2="188"/>
            </g>
            <g font-size="12">
              <text x="470" y="67" fill="var(--gold)">← 看得到 1</text>
              <text x="470" y="137" fill="var(--gold)">← 看得到 3</text>
              <text x="470" y="207" fill="var(--gold)">← 看得到 5</text>
              <text x="20" y="62" fill="var(--text-muted)">第 0 層</text>
              <text x="20" y="132" fill="var(--text-muted)">第 1 層</text>
              <text x="20" y="202" fill="var(--text-muted)">第 2 層</text>
            </g>
            <text x="20" y="246" fill="#ff8a65" font-size="13">★ 答案是 [1, 3, 5]——第 2 層看得到的是 5，它在節點 2 的右邊，不在節點 3 底下（節點 3 沒有小孩）。</text>
            <text x="20" y="274" fill="var(--text-muted)" font-size="12">所以「一路往右走」是錯的：右子樹可能提早結束，這時左子樹的深層節點就露出來了。</text>
            <line x1="20" y1="296" x2="620" y2="296" stroke="var(--border)"/>
            <text x="20" y="324" fill="var(--accent)" font-size="13">★ 兩種正確解法</text>
            <text x="40" y="354" fill="var(--gold)" font-size="12">BFS：一層一層走，每層取佇列裡的最後一個 → q[-1].val</text>
            <text x="40" y="382" fill="var(--gold)" font-size="12">DFS：先右後左，每個深度「第一次」被走到的節點就是答案 → if depth == len(res)</text>'''

emit({
 "num": 199, "slug": "binary-tree-right-side-view",
 "en": [
   "Given the <code>root</code> of a binary tree, imagine yourself standing on the "
   "<strong>right side</strong> of it, return <em>the values of the nodes you can see ordered "
   "from top to bottom</em>.",
 ],
 "zh": [
   "給你一棵二元樹的根節點 <code>root</code>，"
   "想像你站在這棵樹的<strong>右邊</strong>往左看，"
   "回傳<strong>你看得到的節點值，由上到下排列</strong>。",
 ],
 "pre": [
   ("note", "★ 最大的陷阱：不是「一路往右走」", [
     ("c", """很多人第一反應是：

    while node:
        res.append(node.val)
        node = node.right

    【這是錯的】 ✘

【反例】：

            1
           / \\
          2   3
           \\
            5

    一路往右：1 -> 3 -> 停（3 沒有右小孩）-> [1, 3] ✘

    正確答案是 [1, 3, 5] ——
    第 2 層只有節點 5，它【在節點 2 的右子樹】，
    但因為節點 3 那一支已經結束了，
    從右邊看就會看到 5 ✔

【正確的理解】：

    「右視圖」= 【每一層最右邊的那個節點】

    -> 這是一個【按層】的問題，不是「按路徑」的問題。

【兩種標準解法】：

    1. 【BFS】一層一層走，每層取最後一個 —— 最直白 ✔
    2. 【DFS 先右後左】每個深度第一次被走到的就是答案 —— 最精簡 ✔

    兩種都要會。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,2,3,null,5,null,4]

            1
           / \\
          2   3
           \\   \\
            5   4

  輸出：[1,3,4]

範例 2
  輸入：root = [1,null,3]
  輸出：[1,3]

範例 3
  輸入：root = []
  輸出：[]

範例 4（一路往右會錯的例子）
  輸入：root = [1,2,3,null,5]

            1
           / \\
          2   3
           \\
            5

  輸出：[1,3,5]
  說明：★ 第 2 層看得到的是 5 ——
        它在左子樹底下，但節點 3 沒有小孩，
        所以 5 從右邊看得到。""",
 "constraints": [
   "節點數量在 <code>[0, 100]</code> 範圍內",
   "−100 ≤ <code>Node.val</code> ≤ 100",
 ],
 "mid": [
   ("note", "換個角度：左視圖只要改一個字", [
     "<strong>BFS 版</strong>：<code>q[-1]</code> 改成 <code>q[0]</code>。",
     "<strong>DFS 版</strong>：先走 <code>left</code> 再走 <code>right</code>。",
     "<strong>兩種解法都是「每層取一個」的框架，改的只是「取哪一個」。</strong>",
   ]),
 ],
 "idea": [
   ("fig", _P199_FIG, "0 0 640 400"),
   ("c", """【解法一：BFS（層序走訪）】

    每一層開始時，佇列裡【剛好是這一層的所有節點】。

        res.append(q[-1].val)      取最後一個 ✔
        for _ in range(len(q)):    ★ 先記下長度！
            彈出一個，推入它的小孩

    ★ 為什麼要先記 len(q)？

      因為迴圈裡會往 q 推新節點 ——
      不先固定次數的話，會把下一層也一起處理掉 ✘

      這是層序走訪的【標準寫法】，
      第 102、103、107 題都是同一個骨架。

【解法二：DFS（先右後左）】

    def dfs(node, depth):
        if not node: return
        if depth == len(res):     ★ 這一層第一次被走到
            res.append(node.val)
        dfs(node.right, depth+1)  ★ 先右
        dfs(node.left,  depth+1)

    【為什麼 depth == len(res) 就代表「第一次」？】

        res 的長度永遠等於「已經記錄過的層數」。

        depth < len(res)  -> 這一層已經有人了
        depth == len(res) -> 這一層還沒有人 -> 現在這個是第一個 ✔
        depth > len(res)  -> 不可能（DFS 是逐層加深的）

    【為什麼「第一個」就是最右邊的？】

        因為我們【先走右子樹】——
        在同一個深度上，右邊的節點一定比左邊的先被走到 ✔

【兩者比較】

    BFS：直觀、不會 stack overflow、空間 O(寬度)
    DFS：五行、空間 O(高度)

    【樹很深很窄 -> BFS 省空間
      樹很寬很淺 -> DFS 省空間】

    面試時兩種都提，說明取捨 ✔

【複雜度】

    兩者都是 O(n) 時間（每個節點走一次）。
    空間：BFS O(最大寬度)、DFS O(最大深度)。"""),
 ],
 "approaches": [
   ap("解法一", "BFS 層序走訪，每層取最後一個", [
     ("c", S["p199"]),
     "<strong>十二行，語意和題目一字對應：「每層最右邊的」。</strong>",
     ("h", "★ <code>for _ in range(len(q))</code> 是整段的靈魂"),
     ("c", """【錯誤寫法】：

    while q:
        res.append(q[-1].val)
        node = q.popleft()          ✘ 只彈一個
        ...

    這樣層和層會混在一起 ——
    q 裡面同時有這一層剩下的和下一層新加的，
    q[-1] 拿到的就不是「這一層」的最後一個了 ✘

【正確寫法】：

    先用 len(q) 把「這一層有幾個」固定下來，
    再跑剛好那麼多次 ✔

    這樣每次外層 while 的開頭，
    q 裡【剛好】是完整的一層 ——
    這個不變量讓 q[-1] 一定正確。

【這個骨架可以直接改出很多題】：

    第 102 題（層序走訪）：收集整層
    第 103 題（鋸齒層序）：奇數層反轉
    第 107 題（自底向上）：最後把結果反轉
    第 199 題（本題）：每層取 q[-1]
    第 637 題（每層平均）：每層求平均
    第 515 題（每層最大值）：每層取 max

    【背這一個骨架，六題通吃 ✔】

【為什麼用 deque 而不是 list？】

    list.pop(0) 是 O(n)（要搬動所有元素）
    deque.popleft() 是 O(1) ✔

    n = 100 時看不出差別，
    但這是【應該養成的習慣】。""",),
   ], "O(n)", "O(w)", "每個節點一次", "w = 最大寬度", optimal=True),

   ap("解法二", "DFS 先右後左（最精簡）", [
     ("c", S["p199_dfs"]),
     "<strong>九行。<code>depth == len(res)</code> 這個判斷是全題最漂亮的一行。</strong>",
     ("h", "★ 為什麼 <code>depth == len(res)</code> 等於「這一層第一次被走到」？"),
     ("c", """【不變量】：res 的長度 = 已經記錄過的層數。

    一開始 res = []，長度 0 -> 還沒記過任何一層。

    走到 depth = 0 的根節點：
        0 == 0 ✔ -> 記錄 -> len(res) 變成 1

    走到 depth = 1 的節點：
        1 == 1 ✔ -> 記錄 -> len(res) 變成 2

    再走到另一個 depth = 1 的節點：
        1 != 2 ✘ -> 不記錄 ✔

【為什麼 depth 不會跳過某一層？】

    因為 DFS 是【一層一層往下】的 ——
    要到 depth = d+1，必須先經過 depth = d 的父節點。

    所以 depth 最多只會是 len(res)，不會更大 ✔

【★ 先右後左才是關鍵】

    if depth == len(res) 只是「取這一層的第一個」。

    要讓「第一個」= 「最右邊的」，
    就必須【先走右子樹】 ✔

    把 dfs(node.right) 和 dfs(node.left) 對調 ——
    答案就變成【左視圖】了。

    【一行之差，兩題。】

【遞迴深度】

    最壞情況（退化成鏈）是 O(n)。
    本題 n <= 100，完全沒問題。

    n 到 10^5 時要改成解法三（迭代）或解法一（BFS）✔""",),
   ], "O(n)", "O(h)", "每個節點一次", "h = 樹高（遞迴堆疊）", optimal=True),

   ap("解法三", "DFS 迭代版（明確堆疊）", [
     ("c", S["p199_iter"]),
     ("h", "★ 推入順序要反過來"),
     ("c", """堆疊是【後進先出】——

    想要「右邊先被處理」，就要【後推右邊】：

        stack.append(左)    先推
        stack.append(右)    後推 -> 先彈出 ✔

    【這和遞迴版的順序剛好相反】，
    是改寫時最常錯的地方 ✘

【為什麼要寫迭代版？】

    1. 【避免遞迴深度限制】

       Python 預設遞迴上限 1000，
       樹退化成鏈且節點數 > 1000 時會 RecursionError ✘

    2. 【面試官可能會指定】

       「不用遞迴再寫一次」是常見的追問。

【為什麼可以把 None 推進堆疊？】

    彈出時用 if not node: continue 擋掉 ——
    這樣就不用在推入前判斷，程式碼比較短。

    【代價】：堆疊裡會多出一些 None，
    空間常數稍微大一點，但複雜度不變 ✔

    想省的話就在 append 前加 if node。""",),
   ], "O(n)", "O(h)", "每個節點一次", "明確堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "遞迴", "備註"],
   [["一、BFS", "O(n)", "O(w)", "否", "語意最直白 ✔"],
    ["二、DFS 先右後左", "O(n)", "O(h)", "是", "最精簡 ✔"],
    ["三、DFS 迭代", "O(n)", "O(h)", "否", "避開遞迴上限"]]),
 "edges": [
   "<strong>空樹</strong> → <code>[]</code>。<strong>BFS 版一定要先擋 <code>if not root</code></strong>，"
   "否則 <code>deque([None])</code> 會在 <code>q[-1].val</code> 爆掉。",
   "<strong>只有根節點</strong> → <code>[root.val]</code>。",
   "<strong>一路往左的鏈</strong>（<code>1→2→3</code> 全是左小孩）→ <code>[1,2,3]</code>。"
   "<strong>「一路往右走」的錯誤解法在這裡只會回 <code>[1]</code>。</strong>",
   "<strong>右子樹比左子樹淺</strong>（範例 4）→ <strong>深層看到的是左子樹的節點。</strong>"
   "<strong>這是最重要的測資。</strong>",
   "<strong>BFS 忘了先記 <code>len(q)</code></strong> → 層和層混在一起，<code>q[-1]</code> 拿錯。",
   "<strong>DFS 寫成先左後右</strong> → 變成左視圖。",
   "<strong>迭代版推入順序沒反過來</strong> → 也變成左視圖。",
   "<strong>節點值可能是負數或 0</strong> → <strong>不能用「值是不是 0」來判斷有沒有節點。</strong>",
 ],
 "follow": [
   ("h", "追問一：左視圖怎麼寫？"),
   ("c", """【BFS 版】：q[-1] 改成 q[0] ✔

    res.append(q[0].val)

【DFS 版】：先左後右 ✔

    dfs(node.left, depth + 1)
    dfs(node.right, depth + 1)

【迭代版】：推入順序對調 ✔

    stack.append((node.right, depth + 1))   先推右
    stack.append((node.left, depth + 1))    後推左

【一行之差】。

【★ 如果要同時求左視圖和右視圖？】

    BFS 一趟就好：

        left_view.append(q[0].val)
        right_view.append(q[-1].val)

    DFS 要兩個陣列、判斷要分開：

        if depth == len(right_view): right_view.append(...)
        # 左視圖要「最後一個」，不能用同樣的判斷

    -> 【這時 BFS 明顯比較方便】 ✔

    （DFS 版可以改成「直接覆寫」：
      left[depth] = node.val 每次都寫 ——
      先右後左的話最後寫進去的是最左邊的 ✔）""",),
   ("h", "追問二：如果要求「俯視圖」（垂直投影）呢？（第 314 題）"),
   ("c", """【那就完全是另一種座標系】——

    給每個節點一個【欄位座標 col】：

        根節點 col = 0
        左小孩 col = 父 - 1
        右小孩 col = 父 + 1

    然後按 col 分組 ✔

    from collections import defaultdict, deque

    cols = defaultdict(list)
    q = deque([(root, 0)])
    while q:
        node, c = q.popleft()
        cols[c].append(node.val)
        if node.left:  q.append((node.left, c - 1))
        if node.right: q.append((node.right, c + 1))

    return [cols[c] for c in sorted(cols)]

【★ 一定要用 BFS 而不是 DFS】

    因為同一欄裡要【按層由上到下】排序 ——
    BFS 天然保證這個順序 ✔

    DFS 的話同一欄的順序會亂掉，
    要額外記錄 (row, col) 再排序。

【第 987 題（垂直走訪）更嚴格】：

    同一個 (row, col) 的節點還要【按值排序】——
    那就一定要收集 (col, row, val) 三元組再 sort ✔

【三題的關係】：

    199：按【層】分組，每組取一個
    314：按【欄】分組，每組全要
    987：按【欄】分組，組內還要排序""",),
   ("h", "追問三：BFS 和 DFS 的空間怎麼選？"),
   ("c", """【BFS 的空間 = 最大寬度 w】
【DFS 的空間 = 最大深度 h】

    完全二元樹（n 個節點）：
        w ≈ n/2   ✘ BFS 很吃空間
        h ≈ log n ✔ DFS 省很多

    退化成鏈：
        w = 1     ✔ BFS 只要 O(1)
        h = n     ✘ DFS 會 stack overflow

【所以】：

    樹【寬而淺】 -> 用 DFS
    樹【窄而深】 -> 用 BFS

    【不知道形狀】 -> 用 BFS（迭代，不會爆堆疊）
                     或 DFS 迭代版

【本題 n <= 100】，兩種都完全沒差 ——
    但面試時能說出這個取捨會加分 ✔

【一個實務上的細節】：

    Python 的遞迴有固定上限（預設 1000），
    而且每層遞迴的成本比迴圈高很多。

    【在 Python 裡，能寫迭代就寫迭代】。""",),
   ("h", "追問四：如果樹的節點很多，只要前 k 層的右視圖呢？"),
   ("c", """【BFS 版最自然】：

    走完 k 層就 break ✔

        depth = 0
        while q and depth < k:
            res.append(q[-1].val)
            for _ in range(len(q)):
                ...
            depth += 1

    【複雜度變成 O(前 k 層的節點數)】——
    不用走完整棵樹 ✔

【DFS 版就沒這麼好剪】：

    要在 dfs 裡加 if depth >= k: return

        def dfs(node, depth):
            if not node or depth >= k:
                return
            ...

    【也對，而且一樣是 O(前 k 層)】 ✔

    只是 DFS 會在深度方向上「衝到底再回頭」，
    對快取不友善。

【這類「只要前面一部分」的需求，
  通常是 BFS 佔優勢】——

    因為 BFS 的走訪順序【本身就是按層】，
    天然支援「提早停止」✔

    同樣的道理：找最短路徑用 BFS，
    因為第一次碰到目標就一定是最短的。""",),
 ],
 "related": [
   "<strong>第 102 題 二元樹層序走訪</strong> —— 同一個 BFS 骨架",
   "<strong>第 103 題 鋸齒形層序走訪</strong> —— 奇數層反轉",
   "<strong>第 515 題 每層最大值</strong> —— 每層取 max",
   "<strong>第 314 題 垂直走訪</strong> —— 按欄分組",
   "<strong>第 116 題 填充每個節點的下一個右側指標</strong> —— 同樣是「層內的左右關係」",
 ],
 "check": [
   "為什麼「一路往右走」是錯的？請舉一個反例。",
   "BFS 版 <code>for _ in range(len(q))</code> 為什麼不能省略？",
   "DFS 版 <code>depth == len(res)</code> 為什麼等於「這一層第一次被走到」？",
   "要改成左視圖，三種解法各要改哪一行？",
 ],
})
print("P199 written")

_P200_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 掃過每一格，遇到還沒淹掉的 &#39;1&#39; 就「答案 +1」，然後把整座島一次淹光。</text>
            <g font-family="monospace" font-size="15">
              <text x="40" y="58" fill="var(--text-muted)">1 1 0 0 0</text>
              <text x="40" y="84" fill="var(--text-muted)">1 1 0 0 0</text>
              <text x="40" y="110" fill="var(--text-muted)">0 0 1 0 0</text>
              <text x="40" y="136" fill="var(--text-muted)">0 0 0 1 1</text>
              <text x="200" y="98" fill="var(--text-muted)" font-size="13">→ 掃到 (0,0) →</text>
              <text x="360" y="58" fill="#ff8a65">· · 0 0 0</text>
              <text x="360" y="84" fill="#ff8a65">· · 0 0 0</text>
              <text x="360" y="110" fill="var(--gold)">0 0 1 0 0</text>
              <text x="360" y="136" fill="var(--gold)">0 0 0 1 1</text>
              <text x="510" y="72" fill="#ff8a65" font-size="12">第 1 座</text>
              <text x="510" y="98" fill="var(--text-muted)" font-size="12">淹掉</text>
            </g>
            <text x="20" y="172" fill="var(--text-muted)" font-size="12">繼續掃 → 碰到 (2,2) 是第 2 座、(3,3) 是第 3 座 → 答案 3 ✔</text>
            <line x1="20" y1="194" x2="620" y2="194" stroke="var(--border)"/>
            <text x="20" y="222" fill="#ff8a65" font-size="13">★ 最常見的錯：出隊（或彈出）時才標記</text>
            <text x="40" y="252" fill="var(--text-muted)" font-size="12">同一格可能從上下左右被多次推進佇列 —— 如果出隊時才標記，它會被處理很多次。</text>
            <text x="40" y="278" fill="var(--gold)" font-size="12">★ 正確做法：入隊的當下就標記成 &#39;0&#39;，保證每格只進去一次 → O(mn) ✔</text>
            <text x="40" y="304" fill="#ff8a65" font-size="12">寫錯的話最壞會退化成指數級，大測資直接超時。</text>
            <line x1="20" y1="326" x2="620" y2="326" stroke="var(--border)"/>
            <text x="20" y="354" fill="var(--accent)" font-size="13">★ 三種走法，同一個骨架</text>
            <text x="40" y="384" fill="var(--text-muted)" font-size="12">DFS（遞迴／堆疊）：一路往深處淹　BFS（佇列）：一圈一圈往外淹</text>
            <text x="40" y="410" fill="var(--text-muted)" font-size="12">並查集：先當成 mn 座島，每合併一次相鄰的 &#39;1&#39; 就減一 → 適合「邊加邊問」</text>'''

emit({
 "num": 200, "slug": "number-of-islands",
 "en": [
   "Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of "
   "<code>'1'</code>s (land) and <code>'0'</code>s (water), return <em>the number of islands</em>.",
   "An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands "
   "horizontally or vertically. You may assume all four edges of the grid are all surrounded by "
   "water.",
 ],
 "zh": [
   "給你一個 <code>m × n</code> 的二維格子 <code>grid</code>，"
   "<code>'1'</code> 代表陸地、<code>'0'</code> 代表水，回傳<strong>島嶼的數量</strong>。",
   "<strong>島嶼</strong>是由<strong>水平或垂直方向</strong>相鄰的陸地連成的"
   "（<strong>斜角不算相鄰</strong>），而且四周都被水包圍。"
   "你可以假設格子的四個邊界外面都是水。",
 ],
 "pre": [
   ("note", "★ 這是「洪水填充 / 連通分量」的標準範本題", [
     ("c", """【一句話解法】：

    掃過每一格；
    碰到還沒處理過的 '1' -> 答案 +1，然後【把整座島淹掉】。

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                sink(i, j)      # 把這座島全部變成 '0'

【為什麼「淹掉」就對了？】

    淹掉之後，同一座島的其他格子
    在後面的掃描中都是 '0' -> 不會被重複計算 ✔

    所以【count 增加的次數 = 島的座數】 ✔

【sink 有三種寫法】：

    1. DFS 遞迴 —— 最短，但可能爆堆疊
    2. DFS 迭代（堆疊）—— 安全 ✔
    3. BFS（佇列）—— 也安全

    【三種都是 O(mn)】，選哪個都可以。

【★ 全題最重要的一行】：

    【標記要在「推進容器的當下」做，不是「取出來的時候」】。

    寫錯的話同一格會被推進去很多次 ——
    最壞會退化成指數級 ✘

【另一個角度：並查集】

    把每個 '1' 當成一個節點，
    相鄰的 '1' union 起來，
    最後數有幾個集合 ✔

    【一般情況下比 DFS/BFS 慢】，
    但如果題目改成「動態加陸地、每次問島數」
    （第 305 題），那就【非並查集不可】。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
  ]
  輸出：1
  說明：★ 左上角那一大塊是連通的（(0,3) 透過 (0,2)、(0,1) 連到左邊）。

範例 2
  輸入：grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
  輸出：3

範例 3（斜角不算相鄰）
  輸入：grid = [
    ["1","0","1"],
    ["0","1","0"],
    ["1","0","1"]
  ]
  輸出：5
  說明：★ 五個 '1' 兩兩都只是斜角相鄰 -> 各自獨立。""",
 "constraints": [
   "<code>m == grid.length</code>、<code>n == grid[i].length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 300",
   "<code>grid[i][j]</code> 是 <code>'0'</code> 或 <code>'1'</code>"
   "（<strong>字元，不是整數</strong>）",
 ],
 "mid": [
   ("note", "★ 是字元 '1' 不是整數 1", [
     "<strong><code>grid[i][j] == 1</code> 永遠是 <code>False</code></strong> —— "
     "會回傳 0，而且不會報錯。",
     "<strong>這是本題最容易「靜悄悄答錯」的地方。</strong>"
     "同理，淹掉時要寫 <code>grid[i][j] = '0'</code> 而不是 <code>0</code>"
     "（雖然寫 <code>0</code> 也能達到「不等於 <code>'1'</code>」的效果，但不一致很容易出錯）。",
   ]),
 ],
 "idea": [
   ("fig", _P200_FIG, "0 0 640 434"),
   ("c", """【框架：外層掃描 + 內層淹沒】

    count = 0
    for 每一格 (i, j):
        if grid[i][j] == '1':      # 一座還沒數過的島
            count += 1
            淹掉整座島
    return count

【複雜度為什麼是 O(mn) 而不是更糟？】

    因為【每一格最多被淹一次】——
    淹掉之後就變 '0'，不會再被處理。

    外層掃描 O(mn) + 所有淹沒加起來 O(mn)
    = O(mn) ✔

【★ 標記時機（全題最容易錯的地方）】

    【錯誤】：出隊時才標記

        q = deque([(i, j)])
        while q:
            r, c = q.popleft()
            if grid[r][c] == '0': continue
            grid[r][c] = '0'
            for 四個方向:
                if 是 '1': q.append(...)

        問題：同一格可以【從上下左右四個方向】
              各被推進去一次 ——
              佇列會膨脹，最壞 O(4^k) ✘

    【正確】：入隊時就標記

        grid[i][j] = '0'
        q = deque([(i, j)])
        while q:
            r, c = q.popleft()
            for 四個方向:
                if 是 '1':
                    grid[nr][nc] = '0'   ★ 這裡
                    q.append(...)

        每格【只可能被推進去一次】 ✔
        佇列大小 <= mn ✔

    【DFS 遞迴版沒有這個問題】——
    因為它進函式的第一件事就是標記。

【邊界檢查】

    0 <= nr < m and 0 <= nc < n

    ★ 在 Python 裡【絕對不能省】——
      nr = -1 不會報錯，它會繞到最後一列 ✘
      （這是 Python 負索引的陷阱。）

【四個方向的寫法】

    for nr, nc in ((r+1,c), (r-1,c), (r,c+1), (r,c-1)):

    或者用方向陣列：

        DIRS = ((1,0), (-1,0), (0,1), (0,-1))
        for dr, dc in DIRS:
            nr, nc = r + dr, c + dc

    【後者在「八方向」或「要記錄方向」時更好擴充】。"""),
 ],
 "approaches": [
   ap("解法一", "DFS 迭代（堆疊）", [
     ("c", S["p200"]),
     "<strong>面試首選：O(mn)、不會爆堆疊、標記時機正確。</strong>",
     ("h", "★ 為什麼推薦迭代而不是遞迴？"),
     ("c", """題目的 m, n <= 300 -> 最多 90000 格。

    如果整張圖都是 '1'，
    遞迴深度最壞會到 90000 ——

    【Python 預設遞迴上限是 1000】 ✘ RecursionError

    LeetCode 上這題的遞迴版【通常會過】
    （因為測資的島沒那麼大），
    但那是運氣，不是正確性 ✔

【要用遞迴的話】：

    import sys
    sys.setrecursionlimit(300 * 300 + 10)

    【但這只是把問題往後推】——
    真正的深遞迴還是可能撐爆 C 層的堆疊。

【面試時的說法】：

    「我先寫遞迴版因為比較短，
      但如果格子很大我會改成迭代版避免堆疊溢位」

    然後【真的寫出迭代版】 ✔""",),
     ("h", "為什麼堆疊版也要「推入時標記」？"),
     ("c", """和 BFS 一樣的道理。

    如果只在 pop 之後才標記，
    同一格可能同時在堆疊裡出現好幾次 ——

        堆疊大小最壞 O(mn) 變成 O(4mn)，
        而且每一份都要重新展開一次 ✘

    【推入時標記 -> 每格只進去一次 ✔】

    程式碼裡有兩處要標記：
        1. sink 的第一行（起點）
        2. 迴圈裡 append 之前（鄰居）

    【兩處都要，漏一處就會重複。】""",),
   ], "O(mn)", "O(mn)", "每格處理一次", "最壞整張圖進堆疊", optimal=True),

   ap("解法二", "DFS 遞迴（最短）", [
     ("c", S["p200_rec"]),
     "<strong>十五行，是最好記的版本。</strong>",
     ("h", "★ 「先淹再走」的順序"),
     ("c", """def sink(i, j):
    if 越界 or grid[i][j] != '1':
        return
    grid[i][j] = '0'        ★ 先淹掉
    sink(i+1, j)            再往四周
    sink(i-1, j)
    sink(i, j+1)
    sink(i, j-1)

【如果順序反過來（先走再淹）】：

    sink(i+1, j)
    ...
    grid[i][j] = '0'        ✘

    -> 鄰居會走回來，發現 (i,j) 還是 '1'
    -> 【無窮遞迴】 ✘

【這個模式叫「進入時標記」】，
    是所有圖走訪的通則：

        visit(node):
            mark(node)          ★ 第一件事
            for 鄰居:
                if not marked:
                    visit(鄰居)

    【先標記再展開 —— 圖走訪的鐵律。】

【把「越界」和「不是 1」合併判斷】

    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':

    這樣呼叫端就完全不用檢查 ——
    程式碼乾淨很多 ✔

    【代價】：多了四次沒必要的函式呼叫
    （對越界的鄰居）—— 常數稍大，可忽略。""",),
   ], "O(mn)", "O(mn)", "每格處理一次", "遞迴堆疊最壞 mn"),

   ap("解法三", "BFS（佇列）", [
     ("c", S["p200_bfs"]),
     ("h", "★ <code>grid[nr][nc] = '0'</code> 一定要寫在 <code>append</code> 前面"),
     ("c", """這是 BFS 版【唯一】的陷阱，但它很致命。

【錯誤版】：

    while q:
        r, c = q.popleft()
        if grid[r][c] == '0':      # 出隊才檢查
            continue
        grid[r][c] = '0'
        for 四方向:
            if grid[nr][nc] == '1':
                q.append((nr, nc))

    考慮一整片 '1'：
        每一格都會被它的【四個鄰居】各推一次
        -> 佇列裡最多 4mn 個項目

    這個版本【還是 O(mn)】（因為有 continue 擋著），
    但【空間變成 4 倍】，而且常數很大。

    ★ 真正會爆的是【連 continue 都沒有】的版本 ——
      那就會無窮迴圈 ✘

【正確版】：入隊前就標記

        if grid[nr][nc] == '1':
            grid[nr][nc] = '0'      ★ 先改
            q.append((nr, nc))

    每格【只可能被推一次】 ✔
    佇列大小 <= mn ✔

【BFS vs DFS 的空間】

    DFS：最壞 O(mn)（一條蛇形的島）
    BFS：最壞 O(min(m,n))（如果島是規則的）
         但最壞情況（整張圖是島）也是 O(mn)

    【實務上差不多】，選你順手的 ✔

【什麼時候一定要用 BFS？】

    如果題目改成「島上任兩點的最短距離」
    或「最近的水有多遠」（第 542、1162 題）——
    那就【非 BFS 不可】，因為要的是層數 ✔""",),
   ], "O(mn)", "O(mn)", "每格處理一次", "佇列最壞整張圖"),

   ap("解法四", "並查集（為第 305 題鋪路）", [
     ("c", S["p200_uf"]),
     ("h", "★ 「先當成全部獨立，每合併一次減一」"),
     ("c", """count = '1' 的總數      # 一開始每格自成一島

每次成功 union 兩個不同的集合：
    count -= 1              # 兩座島合併成一座 ✔

最後的 count 就是答案。

【為什麼只檢查「右」和「下」？】

    每一對相鄰的格子會被檢查【剛好一次】：

        (i,j) 和 (i,j+1) -> 在處理 (i,j) 時檢查「右」✔
        (i,j) 和 (i+1,j) -> 在處理 (i,j) 時檢查「下」✔

    如果四個方向都檢查，
    每一對會被檢查兩次 ——
    【答案還是對的】（第二次 find 相同不會再減），
    只是多做一倍的工 ✔

【二維座標怎麼變成一維編號？】

    id(i, j) = i * n + j

    n 是【行寬】（列數），不是 m ——
    這裡寫錯是常見 bug ✘

    驗算：(0,0) -> 0、(0,n-1) -> n-1、(1,0) -> n ✔

【路徑減半（path halving）】

    while parent[x] != x:
        parent[x] = parent[parent[x]]   ★ 指向祖父
        x = parent[x]

    比「完整路徑壓縮」（遞迴）短，
    效果幾乎一樣，而且【不用遞迴】 ✔

【複雜度】

    O(mn · α(mn))，α 是反阿克曼函數 ——
    實務上 < 5，可以當成常數。

    【但常數比 DFS 大】（每次 find 要走幾步指標），
    所以【純粹解本題時 DFS 更快】。

【★ 那為什麼要學並查集版？】

    因為【第 305 題（島嶼數量 II）】：

        「陸地是一個一個加上去的，
          每加一個就要回報當前的島數」

    DFS 每次都要重掃整張圖 -> O(k · mn) ✘
    並查集每次只要 O(α) -> O(k · α) ✔

    【「動態加邊、隨時查詢連通分量數」
      是並查集的殺手級應用】——
    DFS/BFS 完全做不到。""",),
   ], "O(mn·α)", "O(mn)", "α ≈ 常數", "parent 陣列"),

   ap("解法五", "不修改輸入（用 visited 集合）", [
     ("c", S["p200_keep"]),
     ("h", "★ 面試官很可能會問「你可以不改動輸入嗎？」"),
     ("c", """前面四種解法都【把 grid 改壞了】——

    呼叫端拿回去的是一張全是 '0' 的圖 ✘

【什麼時候這是問題？】

    1. 【呼叫端還要用這張圖】
    2. 【函式被要求是「純函式」】（沒有副作用）
    3. 【多執行緒共用同一張圖】
    4. 【輸入是唯讀的】（例如它其實是資料庫的快取）

【解法】：用一個 seen 集合代替「改成 '0'」✔

【代價】：

    空間從 O(1) 額外（改原圖）
    變成 O(mn)（seen 集合）

    而且 set 的雜湊比陣列存取慢 ——
    實測大約慢 2~3 倍。

【折衷方案】：

    先 copy 一份再淹：

        g = [row[:] for row in grid]

    空間一樣 O(mn)，
    但存取是陣列而不是雜湊 -> 快很多 ✔

    【如果只是「不想改動呼叫端的資料」，
      copy 比 set 好；
      如果 grid 大到 copy 不划算，
      才用 set。】

【面試時的完整回答】：

    「我這個版本會修改輸入，
      這通常在面試題裡是可以接受的、而且省空間；
      如果不允許，我可以用 visited 集合或先複製一份，
      代價是 O(mn) 的額外空間。」

    ★ 【主動說出來】比【被問到才想到】好得多 ✔""",),
   ], "O(mn)", "O(mn)", "雜湊常數較大", "seen 集合"),
 ],
 "compare": (["解法", "時間", "額外空間", "改動輸入", "適用場景"],
   [["一、DFS 迭代", "O(mn)", "O(mn)", "是", "面試首選 ✔"],
    ["二、DFS 遞迴", "O(mn)", "O(mn)", "是", "最短，但可能爆堆疊"],
    ["三、BFS", "O(mn)", "O(mn)", "是", "要層數時必用"],
    ["四、並查集", "O(mn·α)", "O(mn)", "否", "動態加陸地（第 305 題）"],
    ["五、visited 集合", "O(mn)", "O(mn)", "否", "輸入唯讀時"]]),
 "edges": [
   "<strong>全是 <code>'0'</code></strong> → <code>0</code>。",
   "<strong>全是 <code>'1'</code></strong> → <code>1</code>（整張圖是一座島）。"
   "<strong>這是遞迴版最容易爆堆疊的測資。</strong>",
   "<strong>1 × 1 的格子</strong> → <code>0</code> 或 <code>1</code>。",
   "<strong>棋盤格</strong>（<code>101/010/101</code>）→ <code>5</code>。"
   "<strong>測「斜角不算相鄰」。</strong>",
   "<strong>把 <code>'1'</code> 寫成整數 <code>1</code></strong> → "
   "<strong>永遠回 0，而且不會報錯。</strong>",
   "<strong>忘了邊界檢查</strong> → <strong>Python 的 <code>-1</code> 會繞到最後一列/行，"
   "把不相鄰的島連起來。</strong>",
   "<strong>BFS 在出隊時才標記</strong> → 同一格重複入隊，空間膨脹。",
   "<strong>遞迴版「先走再淹」</strong> → <strong>無窮遞迴。</strong>",
   "<strong>並查集的 <code>i * n + j</code> 寫成 <code>i * m + j</code></strong> → "
   "<strong><code>m ≠ n</code> 時編號重疊，答案錯。</strong>",
 ],
 "follow": [
   ("h", "追問一：如果陸地是一格一格動態加上去的呢？（第 305 題）"),
   ("c", """【每加一格就重新掃一次】-> O(k · mn) ✘

【並查集】-> 每次 O(α) ✔

    def numIslands2(m, n, positions):
        parent = {}
        count = 0
        res = []

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for r, c in positions:
            idx = r * n + c
            if idx in parent:        # ★ 重複加同一格
                res.append(count)
                continue
            parent[idx] = idx
            count += 1               # 先當成新的一座島
            for nr, nc in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
                nidx = nr * n + nc
                if 0 <= nr < m and 0 <= nc < n and nidx in parent:
                    a, b = find(idx), find(nidx)
                    if a != b:
                        parent[a] = b
                        count -= 1   # 合併，少一座
            res.append(count)
        return res

【兩個關鍵】：

    1. 【用 dict 而不是陣列】——
       只有已經變成陸地的格子才在裡面 ✔

    2. 【要處理重複加同一格】——
       測資裡真的有，不擋的話 count 會多算 ✘

【這就是「為什麼要學並查集版」的答案】：

    DFS/BFS 是【靜態】的工具（一次掃完），
    並查集是【增量】的工具（可以邊加邊問）。

    【一旦題目出現「動態」兩個字，先想並查集。】""",),
   ("h", "追問二：如果斜角也算相鄰呢？"),
   ("c", """【把四方向改成八方向】：

    DIRS = ((1,0),(-1,0),(0,1),(0,-1),
            (1,1),(1,-1),(-1,1),(-1,-1))

    【其他完全不用改】 ✔

【島數會變少】（更容易連通）：

    棋盤格 101/010/101：
        四方向 -> 5 座
        八方向 -> 1 座 ✔

【★ 並查集版要小心】

    四方向版只檢查「右」和「下」就夠，
    因為每一對相鄰格子都會被覆蓋到。

    八方向版要檢查【右、下、右下、左下】四個 ——

        右：  (i, j+1)
        下：  (i+1, j)
        右下：(i+1, j+1)
        左下：(i+1, j-1)   ★ 這個容易漏

    【漏掉「左下」的話，
      從右上到左下的斜線就連不起來】 ✘

    （原則：對每一對，只在「掃描順序較早」的那一格檢查。
      掃描順序是由上到下、由左到右，
      所以要檢查的是「同列右邊」和「下一列的三個」。）""",),
   ("h", "追問三：如果格子大到放不進記憶體呢？"),
   ("c", """【假設是一個 10^6 × 10^6 的圖，只能一列一列讀進來。】

【用「兩列滾動 + 並查集」】：

    1. 讀進第 i 列
    2. 【列內】：相鄰的 '1' 合併
    3. 【跨列】：和第 i-1 列的對應位置合併
    4. 丟掉第 i-1 列，只保留它的「集合代表」

    -> 記憶體只要 O(n)（一列的寬度）✔

【這是「連通分量標記（Connected Component Labeling）」
  的標準串流演算法】，
    影像處理裡的【兩遍掃描法】就是它。

【另一個思路：分塊 + 邊界合併】

    把大圖切成很多塊，
    每塊各自算連通分量（可以平行），
    再把【跨塊邊界】上的分量合併起來 ✔

    這是 MapReduce / Spark 上處理超大圖的標準做法。

【面試時不用寫完整程式碼】——
    說出「滾動兩列 + 並查集」或「分塊 + 邊界合併」
    這個架構就夠了 ✔""",),
   ("h", "追問四：相關的變形題有哪些？"),
   ("c", """【同一個洪水填充骨架，換個統計方式】：

    第 695 題（島嶼最大面積）：
        sink 回傳淹掉的格子數，取 max ✔

    第 1254 題（封閉島嶼）：
        先從邊界的 '0' 開始淹（那些通到外海），
        剩下的 '0' 連通塊才是封閉島 ✔

    第 130 題（被圍繞的區域）：
        同樣的「先淹邊界」技巧 ✔

    第 463 題（島嶼周長）：
        不用 DFS，直接數：
        每個 '1' 貢獻 4，每一對相鄰的 '1' 扣 2 ✔

    第 694 題（不同島嶼的數量）：
        DFS 時記錄【相對於起點的座標序列】當作簽名，
        放進 set 去重 ✔

    第 1020 題（飛地的數量）：
        先淹邊界，再數剩下的 '1' ✔

【三個反覆出現的技巧】：

    1. 【先淹邊界】—— 處理「通到外面」的連通塊
       （第 130、1020、1254 題）

    2. 【sink 回傳一個值】—— 面積、周長、簽名
       （第 695、694 題）

    3. 【不用走訪，直接數貢獻】—— 周長類
       （第 463 題）

    【把本題的骨架背熟，這一整類題都會寫。】""",),
 ],
 "related": [
   "<strong>第 695 題 島嶼的最大面積</strong> —— <code>sink</code> 回傳格子數",
   "<strong>第 130 題 被圍繞的區域</strong> —— 先淹邊界",
   "<strong>第 305 題 島嶼數量 II</strong> —— 動態加陸地，非並查集不可",
   "<strong>第 547 題 省份數量</strong> —— 同樣是連通分量，但輸入是鄰接矩陣",
   "<strong>第 994 題 腐爛的橘子</strong> —— 多源 BFS，要的是層數",
   "<strong>第 463 題 島嶼的周長</strong> —— 直接數貢獻，不用走訪",
 ],
 "check": [
   "為什麼「碰到 <code>'1'</code> 就 +1 然後淹掉」不會重複計算？",
   "BFS 版的標記為什麼一定要寫在 <code>append</code> 前面？寫在後面會怎樣？",
   "遞迴版如果「先走鄰居再淹自己」會發生什麼事？",
   "並查集版為什麼只要檢查「右」和「下」兩個方向？八方向版要檢查哪幾個？",
   "什麼情況下必須用並查集而不能用 DFS？",
 ],
})
print("P200 written")
