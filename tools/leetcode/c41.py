# -*- coding: utf-8 -*-
"""第 41–43 題。"""
import random
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(41)

# ==================== 41. First Missing Positive ====================
S["p41_set"] = '''class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)                 # O(n) 額外空間 —— 不符合進階要求
        i = 1
        while i in seen:
            i += 1
        return i'''

S["p41_cycle"] = '''class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 目標：讓 nums[i] == i + 1（也就是數字 v 待在位置 v-1）
        for i in range(n):
            # while 而不是 if：換過來的那個數字也要繼續歸位
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]

        # 第一個「沒歸位」的位置，就是缺失的數字
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1        # 1..n 都在，答案是 n+1'''

S["p41_sign"] = '''class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 第 1 步：把所有「不在 1..n 範圍內」的數字統一換成 n+1
        # （它們不可能是答案，也不該干擾後面的標記）
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # 第 2 步：看到數字 v（1 <= v <= n）就把 nums[v-1] 標成負的
        for i in range(n):
            v = abs(nums[i])
            if v <= n:
                nums[v - 1] = -abs(nums[v - 1])    # 已經是負的也不會變回來

        # 第 3 步：第一個「還是正的」位置，表示那個數字沒出現過
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1'''

_p41 = [S.load(k) for k in ("p41_set", "p41_cycle", "p41_sign")]


def _p41_ref(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i


for c in [[1, 2, 0], [3, 4, -1, 1], [7, 8, 9, 11, 12], [1], [2], [],
          [1, 1], [2, 2, 2], [1, 2, 3, 4, 5]]:
    e = _p41_ref(c)
    for sol in _p41:
        assert sol.firstMissingPositive(list(c)) == e, ("P41", c, sol)
for _ in range(5000):
    c = [random.randint(-3, 8) for _ in range(random.randint(0, 9))]
    e = _p41_ref(c)
    for sol in _p41:
        assert sol.firstMissingPositive(list(c)) == e, ("P41", c, sol)
print("P41 solutions OK")

_P41_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">原地雜湊：把數字 v 放到索引 v−1 的位置上（「蘿蔔蹲」）</text>
            <text x="20" y="50" fill="var(--text-muted)" font-size="12">nums = [3, 4, −1, 1]</text>
            <g font-size="14" text-anchor="middle">
              <rect x="60" y="64" width="64" height="38" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="92" y="89" fill="#ff8a65">3</text>
              <rect x="140" y="64" width="64" height="38" rx="6" fill="none" stroke="var(--border)"/><text x="172" y="89" fill="var(--text-muted)">4</text>
              <rect x="220" y="64" width="64" height="38" rx="6" fill="none" stroke="var(--border)"/><text x="252" y="89" fill="var(--text-muted)">−1</text>
              <rect x="300" y="64" width="64" height="38" rx="6" fill="none" stroke="var(--border)"/><text x="332" y="89" fill="var(--text-muted)">1</text>
            </g>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="92" y="118">0</text><text x="172" y="118">1</text>
              <text x="252" y="118">2</text><text x="332" y="118">3</text>
            </g>
            <text x="400" y="89" fill="#ff8a65" font-size="12">3 應該去索引 2</text>
            <g font-size="14" text-anchor="middle">
              <rect x="60" y="140" width="64" height="38" rx="6" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="92" y="165" fill="#ff8a65">−1</text>
              <rect x="140" y="140" width="64" height="38" rx="6" fill="none" stroke="var(--border)"/><text x="172" y="165" fill="var(--text-muted)">4</text>
              <rect x="220" y="140" width="64" height="38" rx="6" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="252" y="165" fill="var(--gold)">3</text>
              <rect x="300" y="140" width="64" height="38" rx="6" fill="none" stroke="var(--border)"/><text x="332" y="165" fill="var(--text-muted)">1</text>
            </g>
            <text x="400" y="165" fill="var(--text-muted)" font-size="12">−1 不在 1..4，停在這格</text>
            <g font-size="14" text-anchor="middle">
              <rect x="60" y="216" width="64" height="38" rx="6" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="92" y="241" fill="var(--gold)">1</text>
              <rect x="140" y="216" width="64" height="38" rx="6" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="172" y="241" fill="var(--gold)">−1</text>
              <rect x="220" y="216" width="64" height="38" rx="6" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="252" y="241" fill="var(--gold)">3</text>
              <rect x="300" y="216" width="64" height="38" rx="6" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="332" y="241" fill="var(--gold)">4</text>
            </g>
            <text x="400" y="241" fill="var(--text-muted)" font-size="12">全部歸位完成</text>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="92" y="270">應該是 1 ✔</text><text x="172" y="270">應該是 2 ✘</text>
              <text x="252" y="270">3 ✔</text><text x="332" y="270">4 ✔</text>
            </g>
            <text x="20" y="302" fill="var(--gold)" font-size="12">索引 1 沒歸位 → 答案是 1 + 1 = 2</text>'''

emit({
 "num": 41, "slug": "first-missing-positive",
 "en": [
   "Given an unsorted integer array <code>nums</code>, return the smallest positive integer "
   "that is <strong>not present</strong> in <code>nums</code>.",
   "You must implement an algorithm that runs in <code>O(n)</code> time and uses "
   "<code>O(1)</code> auxiliary space.",
 ],
 "zh": [
   "給你一個<strong>未排序</strong>的整數陣列 <code>nums</code>，"
   "找出其中<strong>沒有出現過的最小正整數</strong>。",
   "你的演算法必須是 <code>O(n)</code> 時間，而且只能用 <code>O(1)</code> 額外空間。",
 ],
 "pre": [
   ("note", "最關鍵的觀察：答案一定在 1 到 n+1 之間", [
     ("c", """設陣列長度是 n。

答案的上界是 n + 1。為什麼？

    最好的情況是陣列剛好裝了 1, 2, 3, ..., n
    這時候答案是 n + 1。

    任何其他情況（有負數、有 0、有重複、有 > n 的數），
    都表示 1..n 裡至少缺了一個，答案會 <= n。

所以：
    所有 <= 0 的數字     -> 和答案無關，忽略
    所有 > n 的數字      -> 和答案無關，忽略
    只有 1..n 的數字才重要，而且它們剛好有 n 個位置可以放。

這個觀察是整題的樞紐：
    它把「無限的值域」壓縮成「n 個格子」，
    讓我們能把「陣列本身」當成雜湊表用 —— 這就是 O(1) 空間的來源。"""),
     "<strong>如果沒有 O(1) 空間的要求，這題是 Easy</strong>（丟進 set 再從 1 數上去）。"
     "那條限制才是它被標成 Hard 的原因。",
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1,2,0]
  輸出：3

範例 2
  輸入：nums = [3,4,-1,1]
  輸出：2

範例 3
  輸入：nums = [7,8,9,11,12]
  輸出：1
  說明：連 1 都沒有。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>值域是完整的 32 位元整數</strong>，而陣列只有 10⁵ 個元素。"
       "所以「開一個值域大小的陣列」完全不可行 —— 這也是在暗示「把陣列本身當雜湊表」。",
       "<strong>有負數、有 0、可能有重複</strong>。三種干擾都要處理。",
       "<strong>O(n) 時間 + O(1) 空間</strong>。"
       "排序（O(n log n)）不符合時間要求；set（O(n) 空間）不符合空間要求。"
       "<strong>唯一的出路是原地改寫 <code>nums</code>。</strong>",
       "<strong>題目沒說不能改 <code>nums</code></strong> —— 這很重要。"
       "如果不能改，O(1) 空間是不可能的（要有地方存資訊）。面試時值得確認這一點。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P41_FIG, "0 0 640 314"),
   "兩種 O(1) 空間的做法：<strong>把數字換到它該在的位置</strong>（原地雜湊），"
   "或<strong>用正負號當標記</strong>。兩者都是「把陣列本身當成儲存空間」的變體。",
 ],
 "approaches": [
   ap("解法一", "用 set（先確認答案，但不符合要求）", [
     ("c", S["p41_set"]),
     "四行，絕對正確，O(n) 時間 —— <strong>但 O(n) 空間</strong>。",
     "面試時可以先講這個「暖身」，然後說「但題目要 O(1) 空間，所以要換做法」。"
     "<strong>而且它是驗證後面兩個解法的標準答案。</strong>",
     "<code>while i in seen</code> 最多跑 n+1 次（因為答案 ≤ n+1），所以確實是 O(n)。",
   ], "O(n)", "O(n)", "set 查詢 O(1)", "不符合題目要求"),

   ap("解法二", "原地雜湊：把數字換回它該在的位置（最推薦）", [
     "目標很明確：<strong>讓數字 <code>v</code>（1 ≤ v ≤ n）待在索引 <code>v-1</code> 上。</strong>"
     "整理完之後，第一個「沒對上」的位置就是答案。",
     ("c", S["p41_cycle"]),
     ("h", "為什麼是 <code>while</code> 而不是 <code>if</code>？"),
     ("c", """因為換過來的那個數字「也可能不在自己的位置上」，要繼續換。

nums = [3, 4, -1, 1]，i = 0

  if 版（錯）：
      nums[0]=3，該去索引 2。交換 -> [-1, 4, 3, 1]
      i 前進到 1，但位置 0 現在是 -1（剛好不用處理，這裡看不出錯）

      換一個例子 nums = [3, 1, 2]，i = 0
      nums[0]=3 -> 和索引 2 交換 -> [2, 1, 3]
      if 版：i 前進，位置 0 的 2 沒有歸位  ->  最後答案錯

  while 版（對）：
      [3,1,2] i=0: 3 換到索引 2 -> [2,1,3]
              i=0: 2 換到索引 1 -> [1,2,3]
              i=0: 1 已經在索引 0 -> 停
      完全歸位 ✔"""),
     ("h", "交換條件為什麼是 <code>nums[nums[i]-1] != nums[i]</code>？"),
     ("c", """直覺會寫成 nums[i] != i + 1（「我不在我的位置上」）。
但那樣在「有重複值」時會死循環：

    nums = [1, 1]，i = 1
        nums[1] = 1，該去索引 0
        條件 nums[1] != 2 成立 -> 交換 nums[1] 和 nums[0]
        但兩個都是 1，交換等於沒換 -> 無限迴圈 ✘

正確的條件是「目標位置上還不是這個值」：
        nums[nums[i] - 1] != nums[i]

    nums = [1, 1]，i = 1
        nums[1] = 1，目標位置 nums[0] = 1
        nums[0] == nums[1] -> 條件不成立，不交換 ✔

一句話：「如果目標位置已經有正確的值了，就不用換」——
這同時處理了「已歸位」和「重複值」兩種情況。"""),
     ("h", "為什麼交換要寫 <code>target = nums[i] - 1</code> 再交換？"),
     ("c", """Python 的多重賦值是「先算右邊全部，再依序賦值左邊」。

    nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]

    右邊先算好沒問題，但左邊是「依序」賦值：
      1. 先做 nums[i] = 舊的 nums[nums[i]-1]
      2. 再做 nums[nums[i] - 1] = 舊的 nums[i]
         ^^^^^^^^^^^^^^^ 這裡的 nums[i] 已經被第 1 步改掉了！

    索引算錯 -> 值被寫到錯的地方。

先把索引存進區域變數就完全避開這個陷阱：
    target = nums[i] - 1
    nums[i], nums[target] = nums[target], nums[i]

這是 Python 特有的坑，在 C/Java 裡用 temp 變數交換反而不會遇到。"""),
     ("h", "為什麼總複雜度是 O(n) 而不是 O(n²)？"),
     "外層 <code>for</code> 跑 n 次，內層 <code>while</code> 看起來可能跑很多次 —— "
     "但<strong>每一次成功的交換，都會讓「至少一個數字永久歸位」</strong>。"
     "歸位的數字不會再被換走（條件會擋住），"
     "所以整個過程中交換的總次數最多是 n 次。"
     "<strong>攤還下來還是 O(n)。</strong>",
   ], "O(n)", "O(1)", "總交換次數 ≤ n（攤還分析）",
      "只用幾個變數，原地修改", optimal=True),

   ap("解法三", "用正負號當標記", [
     "另一種「把陣列當儲存空間」的方式：<strong>不搬動數字，而是用每一格的正負號記錄"
     "「這個索引對應的數字出現過沒有」。</strong>",
     ("c", S["p41_sign"]),
     ("h", "三個步驟的分工"),
     ("c", """步驟 1：清理
    把所有 <= 0 或 > n 的數字換成 n+1。
    為什麼要換？因為步驟 2 要用「負號」當標記，
    而原本就是負數的格子會造成誤判。
    換成 n+1（一個正數，而且不在 1..n 裡）就乾淨了。

步驟 2：標記
    看到數字 v，就把 nums[v-1] 變成負的。
    用 -abs(...) 而不是 *= -1 ——
    因為同一個位置可能被標記兩次（有重複值），
    *= -1 會把它變回正的 ✘

步驟 3：讀取
    nums[i] > 0  表示數字 i+1 從來沒被標記過 -> 它就是答案。

nums = [3, 4, -1, 1]，n = 4
  步驟 1： [3, 4, 5, 1]        （-1 換成 5）
  步驟 2：
      v=3 -> nums[2] = -5      [3, 4, -5, 1]
      v=4 -> nums[3] = -1      [3, 4, -5, -1]
      v=5 -> 5 > 4，跳過
      v=1 -> nums[0] = -3      [-3, 4, -5, -1]
  步驟 3：
      nums[0] = -3 < 0  跳過
      nums[1] = 4 > 0   -> 回傳 2 ✔"""),
     ("h", "兩種解法怎麼選？"),
     ("t", ["", "解法二（交換）", "解法三（正負號）"],
       [["掃幾遍", "2", "3"],
        ["資料保留", "順序被打亂，但值都在", "值被改成負數，需要 abs 還原"],
        ["容易寫錯的地方", "交換的索引、while 條件", "重複標記、步驟 1 的清理"],
        ["能處理 0 嗎", "能（不在 1..n 就跳過）", "能（步驟 1 換掉）"]]),
     "<strong>解法二比較常見，也比較好解釋</strong>（「每個數字回到自己的座位」是很好的比喻）。"
     "解法三的優點是<strong>不搬動資料</strong>，在「元素很大、搬移成本高」時有意義。",
   ], "O(n)", "O(1)", "掃三遍", "原地修改，只用符號位"),
 ],
 "compare": (["解法", "時間", "空間", "符合要求？", "備註"],
   [["一、set", "O(n)", "O(n)", "✘", "當基準線"],
    ["二、原地交換", "O(n)", "O(1)", "✔", "最常見；注意 while 和交換順序"],
    ["三、正負號標記", "O(n)", "O(1)", "✔", "不搬資料；注意重複標記"]]),
 "edges": [
   "<strong>答案是 1</strong>：<code>[7,8,9,11,12]</code> → 1。全部都 &gt; n。",
   "<strong>答案是 n+1</strong>：<code>[1,2,3,4,5]</code> → 6。完美填滿。",
   "<strong>有負數和 0</strong>：<code>[3,4,-1,1]</code> → 2；<code>[1,2,0]</code> → 3。",
   "<strong>有重複值</strong>：<code>[1,1]</code> → 2。"
   "<strong>交換條件寫錯會在這裡死循環。</strong>",
   "<strong>全部相同</strong>：<code>[2,2,2]</code> → 1。",
   "<strong>單一元素</strong>：<code>[1]</code> → 2；<code>[2]</code> → 1。",
   "<strong>空陣列</strong>：→ 1。題目保證不會，但兩個解法都自然正確（回 <code>n+1 = 1</code>）。",
   "<strong>極端值</strong>：<code>[2147483647]</code> → 1。"
   "解法三的步驟 1 要能處理（換成 n+1 = 2）。",
 ],
 "follow": [
   ("h", "追問一：如果不能修改 <code>nums</code> 呢？"),
   "<strong>那 O(1) 空間是不可能的。</strong>"
   "直覺的論證：你必須記錄「1..n 裡哪些出現過」，這是 n 位元的資訊，"
   "而 O(1) 空間放不下。唯一的出路就是借用 <code>nums</code> 本身。",
   "所以面試時<strong>一定要先問「可以修改輸入嗎」</strong> —— "
   "這個問題本身就展示了你抓到了重點。",
   ("h", "追問二：如果要找「第 k 個缺失的正整數」呢？"),
   "第 1539 題。如果陣列已排序，可以用二分搜尋在 O(log n) 解決："
   "位置 <code>i</code> 前面缺了 <code>nums[i] - (i+1)</code> 個數，"
   "這個量是單調的，可以二分。"
   "未排序的話還是得先整理。",
   ("h", "追問三：這個「原地雜湊」的技巧還能用在哪？"),
   ("c", """條件：值域剛好和索引範圍對得上（或能對上）

    第 41 題   缺失的第一個正數        值域 1..n
    第 442 題  找出所有重複的數字       值域 1..n
    第 448 題  找出所有消失的數字       值域 1..n
    第 268 題  缺失的數字              值域 0..n
    第 287 題  尋找重複數              值域 1..n，但不能改陣列
                                       -> 改用 Floyd 判圈法

看到「n 個數字，值域也是 n」就該想到這個技巧。
它是「用資料結構本身當雜湊表」的經典案例。"""),
   ("h", "追問四：為什麼這題常被認為是「最難的 Hard Easy 題」？"),
   "因為<strong>去掉 O(1) 空間的限制之後它是 Easy</strong>，"
   "但加上限制之後需要一個不太直覺的洞察（答案在 1..n+1）"
   "加上一個容易寫錯的實作（while 條件、交換順序）。"
   "<strong>它考的不是「你會不會」，而是「你能不能在限制下重新設計」</strong> —— "
   "這正是實務工程最常見的情境。",
 ],
 "related": [
   "<strong>第 268 題 Missing Number</strong> —— 值域 0..n 的簡化版",
   "<strong>第 442 題 Find All Duplicates</strong> —— 同一個原地雜湊技巧",
   "<strong>第 448 題 Find All Numbers Disappeared</strong> —— 同上",
   "<strong>第 287 題 Find the Duplicate Number</strong> —— 不能改陣列，要用判圈法",
 ],
 "check": [
   "為什麼答案一定在 1 到 n+1 之間？請說明上界的理由。",
   "交換條件為什麼寫 <code>nums[nums[i]-1] != nums[i]</code> 而不是 <code>nums[i] != i+1</code>？"
   "用 <code>[1,1]</code> 說明。",
   "為什麼內層是 <code>while</code> 而不是 <code>if</code>？請用 <code>[3,1,2]</code> 追一遍。",
   "解法三的步驟 2 為什麼要用 <code>-abs(...)</code> 而不是 <code>*= -1</code>？",
 ],
})
print("P41 written")
