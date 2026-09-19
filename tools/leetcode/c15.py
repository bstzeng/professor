# -*- coding: utf-8 -*-
"""第 15–18 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(15)

# ==================== 15. 3Sum ====================
S["p15_brute"] = '''class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        found = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        found.add(tuple(sorted((nums[i], nums[j], nums[k]))))
        return [list(t) for t in found]'''

S["p15_hash"] = '''class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []

        for i in range(n - 2):
            if nums[i] > 0:                      # 最小的都大於 0，不可能湊出 0
                break
            if i > 0 and nums[i] == nums[i - 1]: # 第一個數去重
                continue

            seen = set()
            target = -nums[i]
            j = i + 1
            while j < n:
                if target - nums[j] in seen:
                    out.append([nums[i], target - nums[j], nums[j]])
                    # 第三個數去重：跳過所有重複的 nums[j]
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        return out'''

S["p15_two"] = '''class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                 # 排序是一切的前提：去重和雙指標都靠它
        n = len(nums)
        out = []

        for i in range(n - 2):
            # 剪枝：排序後 nums[i] 是三個裡最小的，它 > 0 就沒救了
            if nums[i] > 0:
                break
            # 去重：i 這一層只取「這個值的第一次出現」
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]

                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    out.append([nums[i], nums[lo], nums[hi]])
                    # 找到一組後，兩邊都要跳過重複值
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1

        return out'''

_p15 = [S.load(k) for k in ("p15_brute", "p15_hash", "p15_two")]


def _norm(res):
    return sorted(tuple(sorted(t)) for t in res)


for c in [[-1, 0, 1, 2, -1, -4], [0, 1, 1], [0, 0, 0], [], [0],
          [0, 0, 0, 0], [-2, 0, 1, 1, 2], [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]]:
    e = _norm(_p15[0].threeSum(list(c)))
    for sol in _p15[1:]:
        g = _norm(sol.threeSum(list(c)))
        assert g == e, ("P15", c, sol, g, e)
        assert len(g) == len(set(g)), ("P15 dup", c, sol, g)
for _ in range(2500):
    c = [random.randint(-6, 6) for _ in range(random.randint(0, 10))]
    e = _norm(_p15[0].threeSum(list(c)))
    for sol in _p15[1:]:
        g = _norm(sol.threeSum(list(c)))
        assert g == e, ("P15", c, sol, g, e)
        assert len(g) == len(set(g)), ("P15 dup", c, sol, g)
print("P15 solutions OK")

_P15_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">排序後 nums = [−4, −1, −1, 0, 1, 2]，固定 i = 1（值 −1），在右邊用雙指標找和為 +1 的一對</text>
            <g font-size="14" text-anchor="middle">
              <rect x="50" y="42" width="72" height="40" rx="6" fill="none" stroke="var(--border)" stroke-width="1" stroke-dasharray="4 3"/>
              <text x="86" y="68" fill="var(--text-muted)" opacity="0.55">−4</text>
              <rect x="134" y="42" width="72" height="40" rx="6" fill="none" stroke="var(--gold)" stroke-width="2.5"/>
              <text x="170" y="68" fill="var(--gold)">−1</text>
              <rect x="218" y="42" width="72" height="40" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="254" y="68" fill="var(--accent)">−1</text>
              <rect x="302" y="42" width="72" height="40" rx="6" fill="none" stroke="var(--border)" stroke-width="2"/>
              <text x="338" y="68" fill="var(--text-muted)">0</text>
              <rect x="386" y="42" width="72" height="40" rx="6" fill="none" stroke="var(--border)" stroke-width="2"/>
              <text x="422" y="68" fill="var(--text-muted)">1</text>
              <rect x="470" y="42" width="72" height="40" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/>
              <text x="506" y="68" fill="#ff8a65">2</text>
            </g>
            <text x="170" y="102" fill="var(--gold)" font-size="11" text-anchor="middle">i（固定）</text>
            <text x="254" y="102" fill="var(--accent)" font-size="11" text-anchor="middle">lo</text>
            <text x="506" y="102" fill="#ff8a65" font-size="11" text-anchor="middle">hi</text>
            <text x="20" y="136" fill="var(--text-muted)" font-size="12">−1 + (−1) + 2 = 0 ✔ 收錄 [−1, −1, 2]，兩邊同時往內縮</text>
            <g font-size="14" text-anchor="middle">
              <rect x="50" y="152" width="72" height="40" rx="6" fill="none" stroke="var(--border)" stroke-width="1" stroke-dasharray="4 3"/>
              <text x="86" y="178" fill="var(--text-muted)" opacity="0.55">−4</text>
              <rect x="134" y="152" width="72" height="40" rx="6" fill="none" stroke="var(--gold)" stroke-width="2.5"/>
              <text x="170" y="178" fill="var(--gold)">−1</text>
              <rect x="218" y="152" width="72" height="40" rx="6" fill="none" stroke="var(--border)" stroke-width="1" stroke-dasharray="4 3"/>
              <text x="254" y="178" fill="var(--text-muted)" opacity="0.55">−1</text>
              <rect x="302" y="152" width="72" height="40" rx="6" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="338" y="178" fill="var(--accent)">0</text>
              <rect x="386" y="152" width="72" height="40" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/>
              <text x="422" y="178" fill="#ff8a65">1</text>
              <rect x="470" y="152" width="72" height="40" rx="6" fill="none" stroke="var(--border)" stroke-width="1" stroke-dasharray="4 3"/>
              <text x="506" y="178" fill="var(--text-muted)" opacity="0.55">2</text>
            </g>
            <text x="338" y="212" fill="var(--accent)" font-size="11" text-anchor="middle">lo</text>
            <text x="422" y="212" fill="#ff8a65" font-size="11" text-anchor="middle">hi</text>
            <text x="20" y="246" fill="var(--text-muted)" font-size="12">−1 + 0 + 1 = 0 ✔ 收錄 [−1, 0, 1]，再縮就 lo ≥ hi，這一層結束</text>
            <text x="20" y="274" fill="var(--gold)" font-size="12">下一輪 i = 2 的值也是 −1，和 i = 1 重複 → 直接 continue，這就是去重</text>'''

emit({
 "num": 15, "slug": "3sum",
 "en": [
   "Given an integer array <code>nums</code>, return all the triplets "
   "<code>[nums[i], nums[j], nums[k]]</code> such that "
   "<code>i != j</code>, <code>i != k</code>, <code>j != k</code>, and "
   "<code>nums[i] + nums[j] + nums[k] == 0</code>.",
   "Notice that the solution set must <strong>not contain duplicate triplets</strong>.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，找出所有<strong>不重複</strong>的三元組 "
   "<code>[nums[i], nums[j], nums[k]]</code>，滿足 <code>i</code>、<code>j</code>、"
   "<code>k</code> 互不相同，且三個數相加等於 <code>0</code>。",
   "注意：答案裡<strong>不能有重複的三元組</strong>（順序不同但內容相同算重複）。",
 ],
 "pre": [
   ("note", "這題真正的難點是「去重」，不是「找到」", [
     "找出和為 0 的三個數並不難。難的是<strong>同一組答案不能出現兩次</strong>。",
     ("c", """nums = [-1, 0, 1, 2, -1, -4]

和為 0 的三元組（依索引）：
    (0, 1, 2) -> [-1,  0,  1]
    (1, 2, 4) -> [ 0,  1, -1]     <- 值和上面一樣！
    (0, 3, 4) -> [-1,  2, -1]
    (2, 3, 4) -> [ 1,  2, -1]     <- 值和上面一樣！

題目要的答案只有兩組：
    [[-1, -1, 2], [-1, 0, 1]]

注意「不重複」指的是「值的多重集合不重複」，不是索引不重複。
[-1, 0, 1] 和 [0, 1, -1] 是同一組。

而且 [-1, -1, 2] 是合法的 —— 陣列裡確實有兩個 -1，
它們是不同的位置，只是值一樣。
「不能重複用同一個位置」≠「不能有相同的值」。"""),
     "很多人的第一反應是「先全部找出來，再丟進 set 去重」。"
     "那樣會過，但<strong>會被追問「能不能在找的時候就避免產生重複」</strong> —— "
     "那才是這題想教的東西。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [-1, 0, 1, 2, -1, -4]
  輸出：[[-1, -1, 2], [-1, 0, 1]]
  說明：順序不重要，但兩組都要有，而且不能重複。

範例 2
  輸入：nums = [0, 1, 1]
  輸出：[]
  說明：湊不出 0。

範例 3
  輸入：nums = [0, 0, 0]
  輸出：[[0, 0, 0]]
  說明：只有一組（雖然三個 0 可以有多種索引組合）。""",
 "constraints": [
   "3 ≤ <code>nums.length</code> ≤ 3000",
   "−10⁵ ≤ <code>nums[i]</code> ≤ 10⁵",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 3000</strong>。O(n³) 是 2.7 × 10¹⁰ —— TLE。"
       "O(n²) 是 9 × 10⁶ —— 輕鬆過。所以目標很明確：<strong>O(n²)</strong>。",
       "<strong>值域到 ±10⁵，但陣列長度只有 3000</strong>。"
       "這表示不能用「開一個值域大小的陣列」那種計數技巧（會浪費，而且值域其實也不算大但沒必要）。",
       "<strong>沒說陣列是排序的</strong>，所以我們可以自己排 —— "
       "排序只要 O(n log n)，遠小於 O(n²)，等於免費。<strong>而排序是去重的關鍵。</strong>",
     ]),
   ]),
 ],
 "idea": [
   "<strong>核心降維：把 3Sum 變成「固定一個數 + 2Sum」。</strong>",
   ("c", """要找 a + b + c = 0

固定 a = nums[i]，問題變成：在 i 右邊找兩個數，和為 -a。
那就是第 1 題 Two Sum。

  用雜湊表解 2Sum  -> O(n)  -> 總共 O(n²)，但去重比較麻煩
  用雙指標解 2Sum  -> O(n)  -> 總共 O(n²)，而且排序後去重很自然

雙指標需要「有序」這個前提 ——
而我們本來就想排序（為了去重），所以這個前提是免費的。"""),
   ("fig", _P15_FIG, "0 0 640 288"),
 ],
 "approaches": [
   ap("解法一", "三重迴圈 + set 去重（基準線）", [
     ("c", S["p15_brute"]),
     "<code>tuple(sorted(...))</code> 是去重的關鍵：把三個值排序後當成 key，"
     "這樣 <code>[-1,0,1]</code> 和 <code>[0,1,-1]</code> 會映射到同一個 tuple。",
     "O(n³) 在 n = 3000 時必定 TLE，但它是最可靠的正確性基準 —— 本篇的壓力測試就是拿它對答案。",
   ], "O(n³)", "O(答案數)", "三層迴圈", "set 存所有答案"),

   ap("解法二", "固定一個數 + 雜湊表解 2Sum", [
     "把第 1 題的雜湊表解法套進來：固定 <code>nums[i]</code>，在右邊找兩個數和為 <code>-nums[i]</code>。",
     ("c", S["p15_hash"]),
     ("h", "去重要處理兩層，不是一層"),
     ("ul", [
       "<strong>第一層（<code>i</code>）</strong>：<code>if i &gt; 0 and nums[i] == nums[i-1]: continue</code>。"
       "同一個值只當一次「第一個數」。",
       "<strong>第三層（<code>j</code>）</strong>：找到答案後要跳過所有重複的 <code>nums[j]</code>。"
       "否則 <code>[0,0,0,0]</code> 會產生兩組 <code>[0,0,0]</code>。",
     ]),
     "這個解法能用，但<strong>去重的邏輯比雙指標版本彆扭</strong> —— "
     "因為雜湊表沒有「位置」的概念，你得額外小心哪些重複該跳、哪些不該。"
     "所以雖然複雜度一樣，實務上大家還是寫雙指標。",
   ], "O(n²)", "O(n)", "外層 n 次 × 內層 O(n)", "每一輪的 seen 集合"),

   ap("解法三", "排序 + 雙指標（標準解）", [
     ("c", S["p15_two"]),
     ("h", "三個關鍵設計，逐一拆解"),
     ("h", "① 剪枝：<code>if nums[i] &gt; 0: break</code>"),
     ("c", """排序後 nums[i] ≤ nums[lo] ≤ nums[hi]。
如果 nums[i] > 0，那三個數全是正的，和一定 > 0，不可能是 0。
而且後面的 i 只會更大 —— 所以是 break（整個結束），不是 continue（跳過這一輪）。

這個剪枝在「大部分是正數」的測資上能省掉很多時間。
寫 continue 也會對，只是慢一點。"""),
     ("h", "② 第一層去重：<code>if i &gt; 0 and nums[i] == nums[i-1]: continue</code>"),
     ("c", """排序後 nums = [-1, -1, 0, 1, 2]

i = 0（值 -1）：會找出 [-1, -1, 2] 和 [-1, 0, 1]
i = 1（值 -1）：nums[1] == nums[0]，跳過

為什麼可以跳過？
  因為 i=1 能找到的所有答案，i=0 一定也找得到
  （i=0 的搜尋範圍 [1, n-1] 完整包含 i=1 的範圍 [2, n-1]）。
  所以 i=1 只會產生重複，不會產生新東西。

注意 i > 0 這個條件不能少 ——
否則 i=0 時會存取 nums[-1]（Python 不會報錯，但會拿到最後一個元素，邏輯就錯了）。
這是 Python 特有的陷阱：負索引不會 IndexError。"""),
     ("h", "③ 找到答案後的雙邊去重"),
     ("c", """nums = [-2, 0, 0, 2, 2]，i = 0（值 -2），找和為 2 的一對

lo = 1(0), hi = 4(2)：-2 + 0 + 2 = 0 ✔ 收錄 [-2, 0, 2]

如果只是單純地 lo += 1; hi -= 1：
    lo = 2(0), hi = 3(2)：-2 + 0 + 2 = 0 ✔ 又收錄一次 [-2, 0, 2]  ✘ 重複！

所以收錄之後要先把兩邊的重複值跳完：
    while lo < hi and nums[lo] == nums[lo+1]: lo += 1   # lo 停在最後一個 0
    while lo < hi and nums[hi] == nums[hi-1]: hi -= 1   # hi 停在第一個 2
    lo += 1; hi -= 1                                     # 再各跨一步

跳完之後 lo = 3, hi = 2，lo < hi 不成立，這一層結束 ✔

注意 while 裡的 lo < hi 條件不能省，
否則 [0,0,0,0] 這種全同的輸入會讓 lo 衝過 hi 而越界。"""),
     ("h", "為什麼不用先收集再去重？"),
     "可以，但有兩個代價：（1）要多一份 O(答案數) 的記憶體；"
     "（2）最壞情況答案數是 O(n²)，全部存下來再去重會拖慢常數。"
     "更重要的是 —— <strong>面試官問這題，就是想看你能不能在「生成的當下」就避免重複</strong>。"
     "這個技巧在所有「找出所有不重複組合」的題目（第 40、47、90 題）都會再遇到。",
   ], "O(n²)", "O(log n) 或 O(n)", "排序 O(n log n) + 雙層 O(n²)",
      "排序本身的空間；不算輸出", optimal=True),
 ],
 "compare": (["解法", "時間", "額外空間", "去重方式", "n=3000 能過？"],
   [["一、三重迴圈", "O(n³)", "O(答案數)", "事後 set", "✘"],
    ["二、固定 + 雜湊", "O(n²)", "O(n)", "排序 + 跳過重複", "✔ 但寫法彆扭"],
    ["三、排序 + 雙指標", "O(n²)", "O(log n)", "排序 + 跳過重複", "✔ 標準解"]]),
 "edges": [
   "<strong>長度不足 3</strong>：<code>[]</code>、<code>[0]</code>、<code>[0,0]</code> → <code>[]</code>。"
   "<code>range(n-2)</code> 在 n &lt; 3 時是空的，自然就對了。",
   "<strong>全部是 0</strong>：<code>[0,0,0,0]</code> → 只有一組 <code>[[0,0,0]]</code>。"
   "這是最能抓出去重 bug 的測資。",
   "<strong>剛好三個 0</strong>：<code>[0,0,0]</code> → <code>[[0,0,0]]</code>。",
   "<strong>沒有答案</strong>：<code>[0,1,1]</code>、<code>[1,2,3]</code> → <code>[]</code>。",
   "<strong>大量重複值</strong>：<code>[-2,0,1,1,2]</code> → <code>[[-2,0,2],[-2,1,1]]</code>。"
   "<code>[-2,1,1]</code> 用到兩個不同位置的 1，是合法的。",
   "<strong>全是正數 / 全是負數</strong>：<code>[1,2,3]</code>、<code>[-1,-2,-3]</code> → <code>[]</code>。驗證剪枝。",
   "<strong>Python 負索引陷阱</strong>：忘記 <code>i &gt; 0</code> 的話，"
   "<code>nums[-1]</code> 不會報錯而是回傳最後一個元素 —— 錯得很安靜，很難查。",
 ],
 "follow": [
   ("h", "追問一：4Sum 呢？kSum 呢？"),
   "第 18 題就是 4Sum。做法是<strong>再包一層迴圈</strong>：固定兩個數，剩下用雙指標，O(n³)。",
   "更一般地，kSum 可以寫成遞迴：<strong>固定一個數，遞迴解 (k−1)Sum，"
   "直到 k == 2 時改用雙指標</strong>。複雜度 O(n^(k−1))。"
   "每一層的去重邏輯完全一樣（跳過與前一個相同的值），所以寫成遞迴反而更不容易錯。",
   ("h", "追問二：如果要的是「有幾組」而不是「列出來」呢？"),
   "如果不要求去重，用雜湊表統計配對數會更快。"
   "但如果要求「不重複的組數」，還是得走一樣的流程 —— "
   "因為你必須能區分「值相同的不同位置」。",
   ("h", "追問三：能不能做到比 O(n²) 更快？"),
   "<strong>目前沒有人知道怎麼做。</strong>"
   "3SUM 是計算複雜度理論裡的一個著名問題，"
   "有一整類問題被稱為「<strong>3SUM-hard</strong>」—— "
   "如果你能在 O(n^(2−ε)) 解 3SUM，就能同時加速一大票計算幾何問題。"
   "目前最好的結果只比 O(n²) 快了一個 log 的因子。"
   "所以面試時如果被問「能不能更快」，正確答案是："
   "<strong>「在一般情況下不行，這是 3SUM 猜想」</strong> —— 而不是硬想。",
 ],
 "related": [
   "<strong>第 1 題 Two Sum</strong> —— 降維後的子問題",
   "<strong>第 16 題 3Sum Closest</strong> —— 同樣的骨架，改成找最接近的",
   "<strong>第 18 題 4Sum</strong> —— 再包一層",
   "<strong>第 259 題 3Sum Smaller</strong> —— 雙指標的計數變形",
 ],
 "check": [
   "<code>[0,0,0,0]</code> 的正確答案是什麼？如果拿掉「找到後跳過重複」那兩個 while，會輸出什麼？",
   "第一層去重為什麼要寫 <code>i &gt; 0</code>？在 Python 裡漏掉它會發生什麼（提示：不會報錯）？",
   "<code>if nums[i] &gt; 0: break</code> 為什麼是 break 而不是 continue？",
   "為什麼排序是「免費」的？它在這題裡同時解決了哪兩個問題？",
 ],
})
print("P15 written")

# ==================== 16. 3Sum Closest ====================
S["p16_brute"] = '''class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    s = nums[i] + nums[j] + nums[k]
                    if abs(s - target) < abs(best - target):
                        best = s
        return best'''

S["p16_two"] = '''class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]      # 先拿任意一組當初值

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue                         # 相同的 i 不會給出新結果

            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]

                if abs(total - target) < abs(best - target):
                    best = total

                if total == target:              # 不可能更接近了
                    return target
                if total < target:
                    lo += 1                      # 想要更大 -> 左指標右移
                else:
                    hi -= 1                      # 想要更小 -> 右指標左移

        return best'''

S["p16_pruned"] = '''class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 這一層能達到的最小值：nums[i] 配最左邊兩個
            lo_sum = nums[i] + nums[i + 1] + nums[i + 2]
            if lo_sum > target:
                # 連最小值都已經超過 target，之後的 i 只會更大 -> 收工
                if abs(lo_sum - target) < abs(best - target):
                    best = lo_sum
                break

            # 這一層能達到的最大值：nums[i] 配最右邊兩個
            hi_sum = nums[i] + nums[n - 2] + nums[n - 1]
            if hi_sum < target:
                # 連最大值都還不到 target，這一層最好的就是 hi_sum
                if abs(hi_sum - target) < abs(best - target):
                    best = hi_sum
                continue

            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if abs(total - target) < abs(best - target):
                    best = total
                if total == target:
                    return target
                if total < target:
                    lo += 1
                else:
                    hi -= 1

        return best'''

_p16 = [S.load(k) for k in ("p16_brute", "p16_two", "p16_pruned")]
for c, t in [([-1, 2, 1, -4], 1), ([0, 0, 0], 1), ([1, 1, 1, 0], -100),
             ([4, 0, 5, -5, 3, 3, 0, -4, -5], -2), ([0, 2, 1, -3], 1)]:
    e = _p16[0].threeSumClosest(list(c), t)
    for sol in _p16[1:]:
        assert sol.threeSumClosest(list(c), t) == e, ("P16", c, t, sol, sol.threeSumClosest(list(c), t), e)
for _ in range(4000):
    c = [random.randint(-10, 10) for _ in range(random.randint(3, 9))]
    t = random.randint(-15, 15)
    e = _p16[0].threeSumClosest(list(c), t)
    for sol in _p16[1:]:
        g = sol.threeSumClosest(list(c), t)
        assert abs(g - t) == abs(e - t), ("P16", c, t, sol, g, e)
print("P16 solutions OK")

emit({
 "num": 16, "slug": "3sum-closest",
 "en": [
   "Given an integer array <code>nums</code> of length <code>n</code> and an integer "
   "<code>target</code>, find three integers in <code>nums</code> such that the sum is "
   "closest to <code>target</code>.",
   "Return <em>the sum of the three integers</em>. You may assume that each input would "
   "have exactly one solution.",
 ],
 "zh": [
   "給你一個長度為 <code>n</code> 的整數陣列 <code>nums</code> 和一個整數 <code>target</code>，"
   "找出三個數，讓它們的和<strong>最接近</strong> <code>target</code>。",
   "回傳<strong>這三個數的和</strong>（不是三個數本身）。可以假設每筆輸入<strong>恰好只有一個答案</strong>。",
 ],
 "pre": [
   ("note", "和第 15 題的三個差異", [
     ("c", """第 15 題 3Sum                    第 16 題 3Sum Closest
------------------------        ------------------------
和要「等於」0                     和要「最接近」target
回傳所有三元組                    只回傳一個整數（那個和）
必須去重                          不必去重（答案是數字，不是組合）

差異的後果：
  1. 找到 total == target 可以立刻 return（不可能更好了）
  2. 雙指標的移動邏輯從「三分支」變成「一樣是三分支，但中間那支是提前結束」
  3. 去重從「必要」降級成「純優化」"""),
     "<strong>「恰好只有一個答案」是什麼意思？</strong>"
     "指的是「最接近的那個<strong>和</strong>」唯一，不是「三元組」唯一。"
     "例如 target = 1、可能的和有 0 和 2 時，兩者距離都是 1 —— "
     "題目保證這種情況不會出現，所以你不用煩惱平手時要回哪一個。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [-1, 2, 1, -4], target = 1
  輸出：2
  說明：最接近的和是 (-1) + 2 + 1 = 2。

範例 2
  輸入：nums = [0, 0, 0], target = 1
  輸出：0
  說明：只有一種選法。""",
 "constraints": [
   "3 ≤ <code>nums.length</code> ≤ 500",
   "−1000 ≤ <code>nums[i]</code> ≤ 1000",
   "−10⁴ ≤ <code>target</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 500</strong>。O(n³) 是 1.25 × 10⁸ —— 在 Python 裡會很吃力（可能 TLE），"
       "在 C++ 裡勉強能過。O(n²) 是 2.5 × 10⁵ —— 瞬間完成。",
       "<strong>target 的範圍比「三個數能湊出的最大值」（3000）還大。</strong>"
       "所以可能出現「怎麼湊都差很遠」的情況，例如 <code>target = 10000</code>。"
       "這時答案就是最大的三個數之和 —— 你的程式要能正確處理，不能因為「差太多」而出錯。",
       "<strong>陣列至少 3 個元素</strong>，所以 <code>nums[0]+nums[1]+nums[2]</code> "
       "當初值一定安全。",
     ]),
   ]),
 ],
 "idea": [
   "骨架和第 15 題一模一樣：<strong>排序 → 固定一個 → 雙指標</strong>。"
   "唯一要換的是「判斷式」：從「等於 0 才收」改成「比目前更近就更新」。",
   ("c", """雙指標的移動邏輯為什麼還是對的？

排序後，固定 nums[i]，我們要在 [lo, hi] 裡找一對，使總和最接近 target。

  total < target  ->  和太小，需要更大的數
                      左指標右移（nums[lo] 變大）是唯一能變大的方向
                      （右移 hi 只會讓和更小，離 target 更遠）

  total > target  ->  和太大，需要更小的數
                      右指標左移

  total == target ->  距離 0，不可能更好，直接 return

每一步都排除掉一個指標位置，所以是 O(n)。"""),
 ],
 "approaches": [
   ap("解法一", "三重迴圈（基準線）", [
     ("c", S["p16_brute"]),
     "<code>best</code> 的初值要用一組<strong>真實存在</strong>的和，"
     "不能用 <code>float(\"inf\")</code> —— 因為我們最後要回傳的是「某三個數的和」，"
     "不是距離。用 inf 當初值的話，如果所有比較都沒通過（不會發生，但邏輯上要乾淨），"
     "會回傳一個不存在的值。",
   ], "O(n³)", "O(1)", "n = 500 時約 2 × 10⁷ 組", "只有一個 best"),

   ap("解法二", "排序 + 雙指標（標準解）", [
     ("c", S["p16_two"]),
     ("h", "追一遍 nums = [-4, -1, 1, 2]（已排序），target = 1"),
     ("c", """best 初值 = (-4) + (-1) + 1 = -4    |best - 1| = 5

i = 0（-4）：
  lo=1(-1), hi=3(2)：total = -4-1+2 = -3   |−3−1| = 4 < 5  -> best = -3
                     -3 < 1 -> lo++
  lo=2(1),  hi=3(2)：total = -4+1+2 = -1   |−1−1| = 2 < 4  -> best = -1
                     -1 < 1 -> lo++
  lo=3, hi=3 -> 結束

i = 1（-1）：
  lo=2(1), hi=3(2)：total = -1+1+2 = 2     |2−1| = 1 < 2   -> best = 2
                     2 > 1 -> hi--
  lo=2, hi=2 -> 結束

回傳 2 ✔"""),
     ("h", "<code>if total == target: return target</code> 值得寫嗎？"),
     "值得。距離 0 是絕對最小值，不可能更好，直接結束可以省下剩餘所有迴圈。"
     "在「答案剛好命中」的測資上，這一行可能把執行時間砍掉九成。",
     ("h", "去重那一行還需要嗎？"),
     "<strong>不是必需的</strong>（答案是一個數字，重複計算同樣的 <code>i</code> 只會得到同樣的結果），"
     "但保留它是純粹的優化：相同的 <code>nums[i]</code> 走第二遍會得到完全相同的搜尋過程。"
     "在有大量重複值的測資上能省不少時間。",
   ], "O(n²)", "O(log n)", "排序 + 雙層", "排序本身的空間", optimal=True),

   ap("解法三", "加上區間剪枝（面試加分）", [
     "固定 <code>i</code> 之後，這一層能產生的<strong>和的範圍</strong>是固定的：",
     ("c", """最小值：nums[i] + nums[i+1] + nums[i+2]    （配最左邊兩個）
最大值：nums[i] + nums[n-2] + nums[n-1]    （配最右邊兩個）

情況 A：最小值已經 > target
    這一層所有的和都 > target，最接近的就是最小值本身。
    而且因為 nums 已排序，之後的 i 只會讓最小值更大、離 target 更遠
    -> 記錄之後直接 break，整個迴圈結束。

情況 B：最大值還 < target
    這一層所有的和都 < target，最接近的就是最大值本身。
    但之後的 i 還可能更接近 -> 記錄之後 continue，跳過雙指標。

情況 C：target 落在 [最小值, 最大值] 之間
    才真的需要跑雙指標。"""),
     ("c", S["p16_pruned"]),
     "<strong>複雜度還是 O(n²)</strong>（最壞情況每一層都落在情況 C），"
     "但在 target 極大或極小的測資上，這個剪枝能把大部分層直接跳掉。",
     "面試時的正確做法：<strong>先寫解法二，跑通之後再說「還可以加上區間剪枝」</strong>。"
     "一開始就寫解法三容易把自己繞暈，而且三個分支都要寫對才不會出錯。",
   ], "O(n²) 最壞", "O(log n)", "多數情況遠低於 n²", "排序本身的空間"),
 ],
 "compare": (["解法", "時間", "空間", "n=500 能過？", "備註"],
   [["一、三重迴圈", "O(n³)", "O(1)", "Python 吃力", "基準線"],
    ["二、排序 + 雙指標", "O(n²)", "O(log n)", "✔", "面試預設"],
    ["三、加區間剪枝", "O(n²) 最壞", "O(log n)", "✔ 更快", "加分項，別一開始就寫"]]),
 "edges": [
   "<strong>剛好三個元素</strong>：<code>([0,0,0], 1)</code> → 0。沒有選擇餘地。",
   "<strong>target 遠大於所有可能的和</strong>：<code>([1,1,1,0], 100)</code> → 3。答案是最大的三個之和。",
   "<strong>target 遠小於所有可能的和</strong>：<code>([1,1,1,0], -100)</code> → 1。答案是最小的三個之和。",
   "<strong>剛好命中</strong>：<code>([0,2,1,-3], 0)</code> → 0。驗證提前 return。",
   "<strong>全部相同</strong>：<code>([5,5,5,5], 1)</code> → 15。去重的 continue 要能正確跳過。",
   "<strong>負數與正數混合</strong>：<code>([4,0,5,-5,3,3,0,-4,-5], -2)</code> → −2。",
   "<strong>best 初值</strong>：不能用 0 或 inf，必須是一組真實的和。"
   "用 0 的話 <code>([1,1,1], 100)</code> 會錯誤地回傳 0。",
 ],
 "follow": [
   ("h", "追問一：如果要回傳那三個數，而不是它們的和？"),
   "在更新 <code>best</code> 時一併記下 <code>(nums[i], nums[lo], nums[hi])</code> 即可。"
   "但要先問清楚：<strong>如果有多組三元組達到同樣的最佳和，要回哪一組？</strong>"
   "題目目前只保證「和」唯一，沒保證三元組唯一。",
   ("h", "追問二：如果平手時要回傳比較小的那個和呢？"),
   "把更新條件從 <code>&lt;</code> 改成「距離更小，或距離相同但和更小」：",
   ("c", """d_new, d_old = abs(total - target), abs(best - target)
if d_new < d_old or (d_new == d_old and total < best):
    best = total

這種「主要鍵 + 次要鍵」的比較在實務上很常見，
寫成 tuple 比較會更清楚：
    if (d_new, total) < (d_old, best):
        best = total"""),
   ("h", "追問三：kSum Closest 呢？"),
   "一樣可以遞迴降維：固定一個數，遞迴解 (k−1)Sum Closest，k == 2 時用雙指標。"
   "複雜度 O(n^(k−1))。但要注意<strong>「最接近」沒有 3Sum 那種「剪掉就不會漏」的性質</strong> —— "
   "區間剪枝要小心寫，不能像 3Sum 那樣看到 <code>nums[i] &gt; 0</code> 就直接 break。",
 ],
 "related": [
   "<strong>第 15 題 3Sum</strong> —— 一模一樣的骨架",
   "<strong>第 18 題 4Sum</strong> —— 多一層迴圈",
   "<strong>第 259 題 3Sum Smaller</strong> —— 雙指標的計數變形",
 ],
 "check": [
   "為什麼 <code>best</code> 的初值不能用 0 或 <code>float(\"inf\")</code>？各舉一個會出錯的輸入。",
   "當 <code>total &lt; target</code> 時為什麼一定是移動 <code>lo</code>？移動 <code>hi</code> 會怎樣？",
   "第 15 題的去重是「必要的」，這題的去重是「可選的」。為什麼？",
   "解法三的情況 A 是 break、情況 B 是 continue。為什麼不對稱？",
 ],
})
print("P16 written")
