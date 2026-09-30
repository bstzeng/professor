# -*- coding: utf-8 -*-
"""第 440、441、442、443、445、446 題。"""
import random
import itertools
from collections import defaultdict
from authoring import emit, ap
from runner import Src, to_list, from_list

S = Src()
random.seed(440)


# ==================== 440. K-th Smallest in Lexicographical Order ====================
S["p440"] = '''class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def subtree_size(prefix: int) -> int:
            # 以 prefix 開頭、而且 <= n 的數有幾個（十叉樹中 prefix 這棵子樹的大小）
            size, lo, hi = 0, prefix, prefix
            while lo <= n:
                size += min(hi, n) - lo + 1       # 這一層：[lo, hi] 和 [1, n] 的交集
                lo, hi = lo * 10, hi * 10 + 9     # 往下一層
            return size

        cur = 1
        k -= 1                                    # cur = 1 本身算第 1 個
        while k:
            s = subtree_size(cur)
            if s <= k:                            # ★ 整棵子樹都在第 k 個之前：直接跳過
                k -= s
                cur += 1                          # 換到右邊的兄弟
            else:                                 # 答案在這棵子樹裡：往下走一層
                k -= 1
                cur *= 10
        return cur'''

_p440 = S.load("p440")
for n in range(1, 400):
    order = sorted(range(1, n + 1), key=str)
    for k in range(1, n + 1):
        assert _p440.findKthNumber(n, k) == order[k - 1], (n, k)
for _ in range(30):
    n = random.randint(1, 200000)
    order = sorted(range(1, n + 1), key=str)
    for k in random.sample(range(1, n + 1), min(n, 50)):
        assert _p440.findKthNumber(n, k) == order[k - 1]
print("P440 OK")

_P440_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">n = 13：字典序 = 十叉樹的前序遍歷；整棵子樹可以一次跳過</text>
            <g font-size="12" text-anchor="middle">
              <circle cx="120" cy="60" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="120" y="64" fill="var(--accent)">1</text>
              <circle cx="300" cy="60" r="16" fill="none" stroke="var(--text-muted)"/><text x="300" y="64" fill="var(--text)">2</text>
              <circle cx="360" cy="60" r="16" fill="none" stroke="var(--text-muted)"/><text x="360" y="64" fill="var(--text)">3</text>
              <text x="420" y="64" fill="var(--text-muted)">…</text>
              <circle cx="480" cy="60" r="16" fill="none" stroke="var(--text-muted)"/><text x="480" y="64" fill="var(--text)">9</text>
              <circle cx="40" cy="140" r="16" fill="none" stroke="var(--accent)"/><text x="40" y="144" fill="var(--accent)">10</text>
              <circle cx="93" cy="140" r="16" fill="none" stroke="var(--accent)"/><text x="93" y="144" fill="var(--accent)">11</text>
              <circle cx="146" cy="140" r="16" fill="none" stroke="var(--accent)"/><text x="146" y="144" fill="var(--accent)">12</text>
              <circle cx="199" cy="140" r="16" fill="none" stroke="var(--accent)"/><text x="199" y="144" fill="var(--accent)">13</text>
            </g>
            <g stroke="var(--text-muted)"><line x1="112" y1="74" x2="48" y2="126"/><line x1="116" y1="76" x2="96" y2="124"/><line x1="124" y1="76" x2="143" y2="124"/><line x1="128" y1="74" x2="192" y2="126"/></g>
            <rect x="18" y="38" width="204" height="126" rx="10" fill="none" stroke="var(--gold)" stroke-dasharray="5 4"/>
            <text x="20" y="186" fill="var(--gold)" font-size="12">以 1 開頭的子樹：1, 10, 11, 12, 13 共 5 個</text>
            <text x="20" y="220" fill="var(--text)" font-size="12">k = 7：子樹「1」有 5 個 ≤ 6 → 整棵跳過（k 剩 1），換到兄弟 2；</text>
            <text x="20" y="242" fill="var(--text)" font-size="12">子樹「2」只有 1 個 ≤ 1 → 跳過（k 剩 0），停在 3。答案 3。</text>'''

emit({
 "num": 440, "slug": "k-th-smallest-in-lexicographical-order",
 "en": [
   "Given two integers <code>n</code> and <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>lexicographically smallest integer in the range</em> <code>[1, n]</code>.",
 ],
 "zh": [
   "給你兩個整數 <code>n</code> 和 <code>k</code>，回傳 <code>[1, n]</code> 中<strong>字典序</strong>第 <code>k</code> 小的整數。",
 ],
 "examples": """範例 1
  輸入：n = 13, k = 2
  輸出：10
  說明：字典序是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]。

範例 2
  輸入：n = 1, k = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>k ≤ n</code> ≤ 10⁹",
 ],
 "idea": [
   ("fig", _P440_FIG, "0 0 640 256"),
   ("c", """【第 386 題的進階版】
    第 386 題把所有數依字典序列出來 —— n = 10⁹ 時不可能一個一個走。

【字典序 = 十叉樹的前序遍歷】
    節點 x 的孩子是 x0, x1, ..., x9。
    要找前序中的第 k 個節點。

【一次跳過整棵子樹】
    在節點 cur：
        算出 cur 這棵子樹有幾個節點（<= n 的）：size
        size <= k -> 答案不在這棵子樹，整棵跳過：k -= size，cur 換到右兄弟 cur + 1
        size >  k -> 答案在這棵子樹裡：往下走，k -= 1（cur 本身），cur = cur × 10

【子樹大小怎麼算？】
    一層一層往下：
        第 0 層：[cur, cur]
        第 1 層：[cur×10, cur×10 + 9]
        第 2 層：[cur×100, cur×100 + 99]
    每層和 [1, n] 取交集的長度加起來。

【複雜度】
    每次往下或往右，最多 O(10 × 位數) 步，每步算子樹大小 O(位數)
    -> O(log² n)。"""),
 ],
 "approaches": [
   ap("解法", "十叉樹上的跳躍", [
     ("c", S["p440"]),
   ], "O(log² n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>k = 1</strong> → 1。",
   "<strong>n = 10⁹</strong> → 不能列舉，必須跳過子樹。",
   "<strong>子樹大小剛好等於 k</strong> → 跳過（第 k 個在後面）。",
 ],
 "follow": [
   ("h", "「計算子樹大小、跳過整塊」"),
   ("c", "第 60 題（第 k 個排列）也是同樣的想法：每一位確定時，跳過整組 (n−1)! 個排列。"),
 ],
 "related": [
   "<strong>第 386 題 字典序排數</strong>",
   "<strong>第 60 題 排列序列</strong>",
 ],
 "check": [
   "字典序和十叉樹有什麼關係？",
   "怎麼計算以 prefix 開頭、≤ n 的數有幾個？",
   "什麼時候往右、什麼時候往下？",
 ],
})


# ==================== 441. Arranging Coins ====================
S["p441"] = '''class Solution:
    def arrangeCoins(self, n: int) -> int:
        # ★ 找最大的 k 使 k(k+1)/2 <= n：解二次不等式
        return (math.isqrt(8 * n + 1) - 1) // 2'''

S["p441_bs"] = '''class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi + 1) // 2           # 偏右，避免 lo = mid 時卡住
            if mid * (mid + 1) // 2 <= n:
                lo = mid
            else:
                hi = mid - 1
        return lo'''

_p441 = [S.load(x) for x in ("p441", "p441_bs")]
for n in list(range(0, 5000)) + [2 ** 31 - 1]:
    k = 0
    while (k + 1) * (k + 2) // 2 <= n:
        k += 1
    for sol in _p441:
        assert sol.arrangeCoins(n) == k, n
print("P441 OK")

emit({
 "num": 441, "slug": "arranging-coins",
 "en": [
   "You have <code>n</code> coins and you want to build a staircase with these coins. The staircase consists of <code>k</code> rows where the <code>i<sup>th</sup></code> row has exactly <code>i</code> coins. The last row of the staircase <strong>may be</strong> incomplete.",
   "Given the integer <code>n</code>, return <em>the number of <strong>complete rows</strong> of the staircase you will build</em>.",
 ],
 "zh": [
   "你有 <code>n</code> 枚硬幣，要排成階梯：第 <code>i</code> 列放 <code>i</code> 枚。最後一列可能放不滿。",
   "回傳能排出幾列<strong>完整</strong>的階梯。",
 ],
 "examples": """範例 1
  輸入：n = 5
  輸出：2
  說明：第 3 列只有 2 枚，不完整。

範例 2
  輸入：n = 8
  輸出：3""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【要找最大的 k，使 1 + 2 + ... + k = k(k+1)/2 <= n】

【方法一：二分搜尋】
    k(k+1)/2 隨 k 遞增 -> 二分。

【方法二：解二次不等式】
    k² + k - 2n <= 0
    k <= (-1 + √(1 + 8n)) / 2
    取整數部分。

【浮點數的陷阱】
    n 很大時，math.sqrt 的浮點誤差可能讓結果差 1。
    用 math.isqrt（精確的整數平方根）就沒有這個問題。"""),
 ],
 "approaches": [
   ap("解法一", "二分搜尋", [
     ("c", S["p441_bs"]),
   ], "O(log n)", "O(1)", "", ""),

   ap("解法二", "公式（整數平方根）", [
     ("c", S["p441"]),
   ], "O(1)", "O(1)", "isqrt 本身是 O(log n) 位元運算", "", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、二分", "O(log n)", "通用"],
    ["二、公式", "O(1)", "用 isqrt 避免浮點誤差 ✔"]]),
 "edges": [
   "<strong>n = 1</strong> → 1。",
   "<strong>n 剛好是三角數</strong>（1, 3, 6, 10…）→ 最後一列剛好滿。",
   "<strong>n 很大</strong> → 8n + 1 在其他語言要用 64 位元。",
 ],
 "follow": [
   ("h", "二分的「偏右」寫法"),
   ("c", "找「最後一個滿足條件的」時，mid 要取 (lo + hi + 1) // 2，否則 lo = mid 時區間不會縮小，陷入無窮迴圈。"),
 ],
 "related": [
   "<strong>第 69 題 x 的平方根</strong>",
   "<strong>第 367 題 有效的完全平方數</strong>",
 ],
 "check": [
   "k 列完整階梯需要幾枚硬幣？",
   "為什麼要用 math.isqrt 而不是 math.sqrt？",
   "二分時為什麼 mid 要偏右？",
 ],
})


# ==================== 442. Find All Duplicates in an Array ====================
S["p442"] = '''class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            i = abs(x) - 1                    # 值 x 對應到索引 x-1
            if nums[i] < 0:                   # ★ 已經被標記過：x 第二次出現
                res.append(abs(x))
            else:
                nums[i] = -nums[i]            # 用正負號當作「看過」的標記
        return res'''

_p442 = S.load("p442")
for _ in range(3000):
    n = random.randrange(1, 12)
    pool = list(range(1, n + 1))
    random.shuffle(pool)
    dup_k = random.randrange(0, n // 2 + 1)
    nums = pool[:n - dup_k] + pool[:dup_k]
    random.shuffle(nums)
    want = sorted(x for x in set(nums) if nums.count(x) == 2)
    assert sorted(_p442.findDuplicates(list(nums))) == want
print("P442 OK")

emit({
 "num": 442, "slug": "find-all-duplicates-in-an-array",
 "en": [
   "Given an integer array <code>nums</code> of length <code>n</code> where all the integers of <code>nums</code> are in the range <code>[1, n]</code> and each integer appears <strong>at most</strong> <strong>twice</strong>, return <em>an array of all the integers that appears <strong>twice</strong></em>.",
   "You must write an algorithm that runs in <code>O(n)</code> time and uses only <em>constant</em> auxiliary space, excluding the space needed to store the output.",
 ],
 "zh": [
   "給你一個長度為 <code>n</code> 的整數陣列，每個數都在 <code>[1, n]</code> 之間，而且每個數<strong>最多出現兩次</strong>。回傳所有出現兩次的數。",
   "必須 <code>O(n)</code> 時間、只用常數額外空間（輸出不算）。",
 ],
 "examples": """範例 1
  輸入：nums = [4,3,2,7,8,2,3,1]
  輸出：[2,3]

範例 2
  輸入：nums = [1,1,2]
  輸出：[1]""",
 "constraints": [
   "<code>n == nums.length</code>",
   "1 ≤ <code>n</code> ≤ 10⁵",
   "1 ≤ <code>nums[i]</code> ≤ n",
   "每個數出現一次或兩次",
 ],
 "idea": [
   ("c", """【值域是 [1, n]，陣列長度也是 n】
    -> 可以把陣列本身當雜湊表：值 x 對應到索引 x-1。

【用正負號標記】
    讀到 x：看 nums[x-1]
        是正的 -> 第一次看到 x，把它變成負的（標記）
        是負的 -> 之前已經看過 x -> x 重複了
    因為數字本身可能已經被改成負的，取值時要用 abs(x)。

【為什麼不會破壞資料？】
    正負號只是「附加」的資訊，abs 之後原本的值還在。"""),
 ],
 "approaches": [
   ap("解法", "原地正負號標記", [
     ("c", S["p442"]),
   ], "O(n)", "O(1)", "", "會修改輸入", optimal=True),
 ],
 "edges": [
   "<strong>沒有重複</strong> → 空陣列。",
   "<strong>讀到被標記過的數</strong> → 用 abs 取原值。",
 ],
 "follow": [
   ("h", "「陣列當雜湊表」家族"),
   ("c", "第 448 題（找消失的數：沒被標記的位置）、第 41 題（缺失的第一個正數：原地交換到正確位置）、第 645 題（錯誤的集合：一個重複一個缺少）。"),
 ],
 "related": [
   "<strong>第 448 題 找到所有陣列中消失的數字</strong>",
   "<strong>第 41 題 缺失的第一個正數</strong>",
   "<strong>第 287 題 尋找重複數</strong> —— 不能修改陣列",
 ],
 "check": [
   "為什麼可以把陣列本身當成雜湊表？",
   "讀到一個數時為什麼要先取絕對值？",
 ],
})


# ==================== 443. String Compression ====================
S["p443"] = '''class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0                               # 寫入位置
        read = 0                                # 讀取位置
        n = len(chars)
        while read < n:
            ch = chars[read]
            start = read
            while read < n and chars[read] == ch:   # 找出這一段的長度
                read += 1
            chars[write] = ch
            write += 1
            count = read - start
            if count > 1:
                for d in str(count):            # ★ 次數可能是多位數，逐位寫入
                    chars[write] = d
                    write += 1
        return write'''

_p443 = S.load("p443")


def _comp(chs):
    out = []
    for k, g in itertools.groupby(chs):
        L = len(list(g))
        out.append(k)
        if L > 1:
            out += list(str(L))
    return out


for _ in range(3000):
    chars = [random.choice("aab") for _ in range(random.randrange(1, 30))]
    want = _comp(chars)
    arr = list(chars)
    k = _p443.compress(arr)
    assert arr[:k] == want
assert _p443.compress(list("a" + "b" * 12)) == 4
print("P443 OK")

emit({
 "num": 443, "slug": "string-compression",
 "en": [
   "Given an array of characters <code>chars</code>, compress it using the following algorithm:",
   "Begin with an empty string <code>s</code>. For each group of <strong>consecutive repeating characters</strong> in <code>chars</code>:",
   ("ul", ["If the group's length is <code>1</code>, append the character to <code>s</code>.",
           "Otherwise, append the character followed by the group's length."]),
   "The compressed string <code>s</code> <strong>should not be returned separately</strong>, but instead, be stored <strong>in the input character array <code>chars</code></strong>. Note that group lengths that are <code>10</code> or longer will be split into multiple characters in <code>chars</code>.",
   "After you are done <strong>modifying the input array</strong>, return <em>the new length of the array</em>.",
   "You must write an algorithm that uses only constant extra space.",
 ],
 "zh": [
   "給你一個字元陣列 <code>chars</code>，用以下規則壓縮：每一段<strong>連續相同的字元</strong>，長度是 1 就只寫字元，否則寫「字元 + 長度」。",
   "壓縮結果要<strong>原地</strong>寫回 <code>chars</code>；長度 ≥ 10 時要拆成多個數字字元。回傳壓縮後的長度。",
   "只能使用常數額外空間。",
 ],
 "examples": """範例 1
  輸入：chars = ["a","a","b","b","c","c","c"]
  輸出：6，前 6 個字元是 ["a","2","b","2","c","3"]

範例 2
  輸入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
  輸出：4，前 4 個字元是 ["a","b","1","2"]""",
 "constraints": [
   "1 ≤ <code>chars.length</code> ≤ 2000",
   "<code>chars[i]</code> 是英文字母、數字或符號",
 ],
 "idea": [
   ("c", """【讀寫雙指標】
    read：往前掃，找出每一段連續相同字元
    write：把壓縮結果寫回陣列

【為什麼不會蓋掉還沒讀的資料？】
    每一段長度 L 的字元，壓縮後長度是 1 + (L 的位數)，
    L >= 2 時 1 + 位數 <= L；L = 1 時就是 1。
    所以 write 永遠不會超過 read。

【多位數的長度】
    12 要寫成 "1"、"2" 兩個字元 —— 用 str(count) 逐位寫入。"""),
 ],
 "approaches": [
   ap("解法", "讀寫雙指標", [
     ("c", S["p443"]),
   ], "O(n)", "O(1)", "", "str(count) 最多 4 個字元", optimal=True),
 ],
 "edges": [
   "<strong>只有一個字元</strong> → 長度 1。",
   "<strong>長度 ≥ 10</strong> → 拆成多個數字字元。",
   "<strong>沒有連續重複</strong> → 陣列不變。",
 ],
 "follow": [
   ("h", "游程編碼（Run-Length Encoding）"),
   ("c", "這就是 RLE：傳真機、早期的 BMP、PCX 影像格式都用它壓縮大片同色區域。第 38 題「外觀數列」也是反覆做 RLE。"),
 ],
 "related": [
   "<strong>第 38 題 外觀數列</strong>",
   "<strong>第 26 題 刪除有序陣列中的重複項</strong> —— 讀寫雙指標",
 ],
 "check": [
   "為什麼寫入指標不會超過讀取指標？",
   "長度 12 要怎麼寫入？",
 ],
})


# ==================== 445. Add Two Numbers II ====================
S["p445"] = '''class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:                          # ★ 高位在前：用堆疊把順序反過來
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        head = None
        carry = 0
        while s1 or s2 or carry:
            d = carry + (s1.pop() if s1 else 0) + (s2.pop() if s2 else 0)
            head = ListNode(d % 10, head)  # 從低位往高位算，新節點插在最前面
            carry = d // 10
        return head'''

_p445 = S.load("p445")
for _ in range(3000):
    a, b = random.randint(0, 10 ** random.randint(0, 12)), random.randint(0, 10 ** random.randint(0, 12))
    got = from_list(_p445.addTwoNumbers(to_list(list(map(int, str(a)))), to_list(list(map(int, str(b))))))
    assert got == list(map(int, str(a + b)))
print("P445 OK")

emit({
 "num": 445, "slug": "add-two-numbers-ii",
 "en": [
   "You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.",
   "You may assume the two numbers do not contain any leading zero, except the number 0 itself.",
   "<strong>Follow up:</strong> Could you solve it without reversing the input lists?",
 ],
 "zh": [
   "給你兩個非空的鏈結串列，各代表一個非負整數，<strong>最高位在前</strong>，每個節點一位數字。把兩個數相加，以相同格式回傳。",
   "<strong>進階：</strong>能不反轉輸入串列嗎？",
 ],
 "examples": """範例 1
  輸入：l1 = [7,2,4,3], l2 = [5,6,4]
  輸出：[7,8,0,7]
  說明：7243 + 564 = 7807

範例 2
  輸入：l1 = [0], l2 = [0]
  輸出：[0]""",
 "constraints": [
   "每個串列的節點數在 <code>[1, 100]</code> 之間",
   "0 ≤ <code>Node.val</code> ≤ 9",
   "沒有前導零（0 本身除外）",
 ],
 "idea": [
   ("c", """【第 2 題是低位在前，這題是高位在前】
    加法必須從低位開始算（進位往高位傳）。

【用堆疊反轉順序（不改動輸入）】
    把兩個串列的數字分別推進堆疊，
    pop 出來就是從低位到高位。

【結果也要高位在前】
    從低位算起，每算出一位就「插在最前面」：
        head = ListNode(digit, head)
    最後 head 就是最高位。

【別忘了最後的進位】"""),
 ],
 "approaches": [
   ap("解法", "兩個堆疊 + 頭插法", [
     ("c", S["p445"]),
   ], "O(m + n)", "O(m + n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>長度不同</strong> → 堆疊空了就當 0。",
   "<strong>最高位進位</strong>（99 + 1）→ 多一個節點。",
   "<strong>0 + 0</strong> → [0]。",
 ],
 "follow": [
   ("h", "其他做法"),
   ("c", "反轉兩個串列 → 用第 2 題的方法相加 → 反轉結果。或先算出兩個串列的長度差，遞迴從低位回傳進位。"),
 ],
 "related": [
   "<strong>第 2 題 兩數相加</strong>",
   "<strong>第 415 題 字串相加</strong>",
   "<strong>第 206 題 反轉鏈結串列</strong>",
 ],
 "check": [
   "為什麼需要堆疊？",
   "結果串列為什麼用「插在最前面」的方式建立？",
 ],
})


# ==================== 446. Arithmetic Slices II - Subsequence ====================
S["p446"] = '''class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][d]：以 nums[i] 結尾、公差為 d、長度 >= 2 的子序列個數
        dp = [collections.defaultdict(int) for _ in range(n)]
        total = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                cnt = dp[j][d]            # 以 nums[j] 結尾、公差 d 的（長度 >= 2）
                total += cnt              # ★ 接上 nums[i] 之後長度 >= 3：計入答案
                dp[i][d] += cnt + 1       # +1 是新的長度 2 子序列 [nums[j], nums[i]]
        return total'''

_p446 = S.load("p446")
for nums, want in [([2, 4, 6, 8, 10], 7), ([7, 7, 7, 7, 7], 16)]:
    assert _p446.numberOfArithmeticSlices(nums) == want
for _ in range(500):
    a = [random.randint(-3, 3) for _ in range(random.randrange(1, 10))]
    want = 0
    for r in range(3, len(a) + 1):
        for idx in itertools.combinations(range(len(a)), r):
            v = [a[i] for i in idx]
            if len({v[t + 1] - v[t] for t in range(r - 1)}) == 1:
                want += 1
    assert _p446.numberOfArithmeticSlices(a) == want, a
print("P446 OK")

emit({
 "num": 446, "slug": "arithmetic-slices-ii-subsequence",
 "en": [
   "Given an integer array <code>nums</code>, return <em>the number of all the <strong>arithmetic subsequences</strong> of</em> <code>nums</code>.",
   "A sequence of numbers is called arithmetic if it consists of <strong>at least three elements</strong> and if the difference between any two consecutive elements is the same.",
   "A <strong>subsequence</strong> of an array is a sequence that can be formed by removing some elements (possibly none) of the array.",
   "The test cases are generated so that the answer fits in <strong>32-bit</strong> integer.",
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，回傳其中<strong>等差子序列</strong>的個數（至少三個元素、相鄰差相同；子序列可以不連續）。",
   "不同位置的元素組成的子序列視為不同（即使數值相同）。",
 ],
 "examples": """範例 1
  輸入：nums = [2,4,6,8,10]
  輸出：7
  說明：[2,4,6] [4,6,8] [6,8,10] [2,4,6,8] [4,6,8,10] [2,4,6,8,10] [2,6,10]

範例 2
  輸入：nums = [7,7,7,7,7]
  輸出：16
  說明：任選至少三個位置都可以：C(5,3)+C(5,4)+C(5,5) = 10+5+1 = 16。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 1000",
   "−2³¹ ≤ <code>nums[i]</code> ≤ 2³¹ − 1",
 ],
 "idea": [
   ("c", """【子序列不連續 -> 需要知道「公差」】
    dp[i][d] = 以 nums[i] 結尾、公差為 d 的子序列個數

【長度 >= 3 的限制怎麼處理？】
    技巧：dp 記錄「長度 >= 2」的個數（稱為「弱等差子序列」）。
    對每一對 j < i，d = nums[i] - nums[j]：
        所有以 nums[j] 結尾、公差 d 的弱等差子序列（dp[j][d] 個），
        接上 nums[i] 之後長度 >= 3 -> 都是合格的，加進答案
        dp[i][d] += dp[j][d] + 1
                              └ 新的長度 2：[nums[j], nums[i]]

【為什麼用雜湊表？】
    公差的範圍可能到 2³²，不能開陣列；
    每個 i 最多只有 i 種公差 -> 總狀態數 O(n²)。"""),
 ],
 "approaches": [
   ap("解法", "dp[i][公差] 的雜湊表 DP", [
     ("c", S["p446"]),
   ], "O(n²)", "O(n²)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>全部相同</strong> → 公差 0，任選 ≥ 3 個位置。",
   "<strong>長度 &lt; 3</strong> → 0。",
   "<strong>差值很大</strong> → Python 沒有溢位；其他語言要用 long 當鍵。",
 ],
 "follow": [
   ("h", "相關的 dp[i][d]"),
   ("c", "第 1027 題（最長等差子序列：dp[i][d] 存長度而不是個數）、第 1218 題（公差固定的最長等差子序列）。"),
 ],
 "related": [
   "<strong>第 413 題 等差數列劃分</strong> —— 子陣列版",
   "<strong>第 1027 題 最長等差數列</strong>",
 ],
 "check": [
   "dp 為什麼要多一個「公差」的維度？",
   "為什麼 dp 記錄長度 ≥ 2 而不是 ≥ 3？",
   "dp[i][d] += dp[j][d] + 1 中的 +1 代表什麼？",
 ],
})
