# -*- coding: utf-8 -*-
"""第 382、383、384、385、386、387 題。"""
import random
from collections import Counter
from authoring import emit, ap
from runner import Src, to_list

S = Src()
random.seed(382)


# ==================== 382. Linked List Random Node ====================
S["p382"] = '''class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        # ★ 蓄水池抽樣：第 i 個節點以 1/i 的機率取代目前的答案
        node, i, chosen = self.head, 1, None
        while node:
            if random.randrange(i) == 0:        # 機率 1/i
                chosen = node.val
            node = node.next
            i += 1
        return chosen'''

S["p382_arr"] = '''class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.vals = []
        while head:                             # 先把所有值存起來
            self.vals.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.vals)'''

for key in ("p382", "p382_arr"):
    cls = S.loadns(key)["Solution"]
    obj = cls(to_list([1, 2, 3, 4]))
    cnt = Counter(obj.getRandom() for _ in range(40000))
    assert set(cnt) == {1, 2, 3, 4} and all(9000 < c < 11000 for c in cnt.values()), (key, cnt)
    assert cls(to_list([7])).getRandom() == 7
print("P382 OK")

_P382_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">蓄水池抽樣：第 i 個元素以 1/i 的機率取代目前的答案</text>
            <g font-size="13" text-anchor="middle">
              <rect x="40" y="44" width="60" height="30" fill="none" stroke="var(--accent)"/><text x="70" y="64" fill="var(--accent)">1</text>
              <rect x="130" y="44" width="60" height="30" fill="none" stroke="var(--accent)"/><text x="160" y="64" fill="var(--accent)">2</text>
              <rect x="220" y="44" width="60" height="30" fill="none" stroke="var(--accent)"/><text x="250" y="64" fill="var(--accent)">3</text>
              <rect x="310" y="44" width="60" height="30" fill="none" stroke="var(--accent)"/><text x="340" y="64" fill="var(--accent)">4</text>
              <text x="70" y="94" fill="var(--text-muted)" font-size="11">取代機率 1</text>
              <text x="160" y="94" fill="var(--text-muted)" font-size="11">1/2</text>
              <text x="250" y="94" fill="var(--text-muted)" font-size="11">1/3</text>
              <text x="340" y="94" fill="var(--text-muted)" font-size="11">1/4</text>
            </g>
            <text x="40" y="132" fill="var(--text)" font-size="12">最後答案是 2 的機率 = 在第 2 步被選中 × 之後沒被取代</text>
            <text x="60" y="156" fill="var(--gold)" font-size="13">= 1/2 × (1 − 1/3) × (1 − 1/4) = 1/2 × 2/3 × 3/4 = 1/4 ✔</text>
            <text x="40" y="188" fill="var(--text-muted)" font-size="12">一般地：第 i 個最後留下的機率 = 1/i × i/(i+1) × … × (n−1)/n = 1/n，連乘會一路消去。</text>
            <text x="40" y="212" fill="var(--text-muted)" font-size="12">不需要事先知道 n，也不需要額外空間 —— 適合長度未知、只能讀一遍的資料流。</text>'''

emit({
 "num": 382, "slug": "linked-list-random-node",
 "en": [
   "Given a singly linked list, return a random node's value from the linked list. Each node must have the <strong>same probability</strong> of being chosen.",
   "Implement the <code>Solution</code> class:",
   ("ul", ["<code>Solution(ListNode head)</code> Initializes the object with the head of the singly-linked list <code>head</code>.",
           "<code>int getRandom()</code> Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen."]),
   "<strong>Follow up:</strong> What if the linked list is extremely large and its length is unknown to you? Could you solve this efficiently without using extra space?",
 ],
 "zh": [
   "給你一個單向鏈結串列，每次呼叫 <code>getRandom()</code> 時隨機回傳一個節點的值，每個節點被選中的<strong>機率必須相同</strong>。",
   "<strong>進階：</strong>如果串列非常長、而且不知道長度，能不用額外空間有效率地完成嗎？",
 ],
 "examples": """範例
  Solution([1, 2, 3])
  getRandom() -> 1、2、3 各 1/3 機率""",
 "constraints": [
   "節點數在 <code>[1, 10⁴]</code> 之間",
   "−10⁴ ≤ <code>Node.val</code> ≤ 10⁴",
   "最多呼叫 10⁴ 次 <code>getRandom</code>",
 ],
 "idea": [
   ("fig", _P382_FIG, "0 0 640 226"),
   ("c", """【簡單做法：先存成陣列】
    建構時 O(n) 存起來，之後每次 O(1)。
    但要 O(n) 額外空間，而且要事先讀完整條串列。

【蓄水池抽樣（Reservoir Sampling）】
    只走一遍，不需要知道長度：
        第 i 個元素（從 1 開始），以 1/i 的機率取代目前的答案。
    走完之後，每個元素被選中的機率都是 1/n。

【證明】
    第 i 個元素最後留下 =
        它被選中（1/i）
        × 第 i+1 個沒取代它（i/(i+1)）
        × 第 i+2 個沒取代它（(i+1)/(i+2)）
        × ...
        × 第 n 個沒取代它（(n-1)/n）
    = 1/n ✔（分子分母一路消去）

【推廣：抽 k 個】
    先放前 k 個進蓄水池；
    第 i 個（i > k）以 k/i 的機率，隨機取代池中的一個。"""),
 ],
 "approaches": [
   ap("解法一", "存成陣列", [
     ("c", S["p382_arr"]),
   ], "建構 O(n)，查詢 O(1)", "O(n)", "", ""),

   ap("解法二", "蓄水池抽樣", [
     ("c", S["p382"]),
   ], "查詢 O(n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "getRandom", "空間", "適用"],
   [["一、陣列", "O(1)", "O(n)", "查詢很多次"],
    ["二、蓄水池", "O(n)", "O(1)", "長度未知、資料流 ✔"]]),
 "edges": [
   "<strong>只有一個節點</strong> → 永遠回傳它。",
   "<strong>重複的值</strong> → 每個「節點」機率相同，重複的值加總機率較高。",
 ],
 "follow": [
   ("h", "實際應用"),
   ("c", "從巨大的日誌檔、網路串流中均勻抽樣，而不需要先知道總量；資料庫的隨機抽樣（TABLESAMPLE）也用類似的想法。"),
 ],
 "related": [
   "<strong>第 398 題 隨機數索引</strong> —— 同樣是蓄水池抽樣",
   "<strong>第 384 題 打亂陣列</strong>",
   "<strong>第 528 題 按權重隨機選擇</strong>",
 ],
 "check": [
   "蓄水池抽樣中，第 i 個元素取代答案的機率是多少？",
   "證明每個元素最後被選中的機率都是 1/n。",
   "什麼情況下蓄水池抽樣比存成陣列好？",
 ],
})


# ==================== 383. Ransom Note ====================
S["p383"] = '''class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt = [0] * 26
        for ch in magazine:                   # 雜誌提供的字母
            cnt[ord(ch) - 97] += 1
        for ch in ransomNote:                 # 信需要的字母
            i = ord(ch) - 97
            cnt[i] -= 1
            if cnt[i] < 0:                    # ★ 不夠用了
                return False
        return True'''

S["p383_counter"] = '''class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Counter 相減會丟掉 <= 0 的項：剩下的就是「不夠的字母」
        return not (collections.Counter(ransomNote) - collections.Counter(magazine))'''

_p383 = [S.load(x) for x in ("p383", "p383_counter")]
for _ in range(3000):
    r = "".join(random.choice("abc") for _ in range(random.randrange(1, 6)))
    m = "".join(random.choice("abc") for _ in range(random.randrange(1, 8)))
    want = all(r.count(c) <= m.count(c) for c in set(r))
    for sol in _p383:
        assert sol.canConstruct(r, m) == want
print("P383 OK")

emit({
 "num": 383, "slug": "ransom-note",
 "en": [
   "Given two strings <code>ransomNote</code> and <code>magazine</code>, return <code>true</code> <em>if</em> <code>ransomNote</code> <em>can be constructed by using the letters from</em> <code>magazine</code> <em>and</em> <code>false</code> <em>otherwise</em>.",
   "Each letter in <code>magazine</code> can only be used once in <code>ransomNote</code>.",
 ],
 "zh": [
   "給你兩個字串 <code>ransomNote</code>（勒索信）和 <code>magazine</code>（雜誌），判斷能不能用雜誌上剪下來的字母拼出勒索信。",
   "雜誌上的每個字母只能用一次。",
 ],
 "examples": """範例 1
  輸入：ransomNote = "a", magazine = "b"
  輸出：false

範例 2
  輸入：ransomNote = "aa", magazine = "ab"
  輸出：false

範例 3
  輸入：ransomNote = "aa", magazine = "aab"
  輸出：true""",
 "constraints": [
   "1 ≤ <code>ransomNote.length, magazine.length</code> ≤ 10⁵",
   "只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【每種字母：雜誌提供的數量 >= 信需要的數量】

【計數】
    先數雜誌裡每個字母有幾個（庫存），
    再逐字扣掉信需要的，任何一種扣到負數就不夠。

【Counter 的寫法】
    Counter(信) - Counter(雜誌)：
    相減之後只保留正數 -> 剩下的是「還缺的字母」，
    空的代表不缺。"""),
 ],
 "approaches": [
   ap("解法一", "Counter 相減", [
     ("c", S["p383_counter"]),
   ], "O(m + n)", "O(1)", "", "最多 26 種字母"),

   ap("解法二", "26 格計數陣列", [
     ("c", S["p383"]),
   ], "O(m + n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、Counter", "O(m + n)", "O(1)"],
    ["二、26 格陣列", "O(m + n)", "O(1) ✔"]]),
 "edges": [
   "<strong>信比雜誌長</strong> → 一定 false（可以先檢查提早結束）。",
   "<strong>重複字母</strong> → 數量要夠。",
 ],
 "follow": [
   ("h", "計數比較的家族"),
   ("c", "第 242 題（異位詞：兩邊計數完全相等）、第 383 題（一邊包含另一邊）、第 1160 題（能拼出哪些單字）都是同一個 26 格計數。"),
 ],
 "related": [
   "<strong>第 242 題 有效的字母異位詞</strong>",
   "<strong>第 1160 題 拼寫單字</strong>",
 ],
 "check": [
   "什麼條件下可以拼出勒索信？",
   "Counter 相減的結果代表什麼？",
 ],
})


# ==================== 384. Shuffle an Array ====================
S["p384"] = '''class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.arr = nums[:]

    def reset(self) -> List[int]:
        self.arr = self.original[:]
        return self.arr

    def shuffle(self) -> List[int]:
        a = self.arr
        # ★ Fisher–Yates：從後往前，每個位置和「自己或前面的任一位置」交換
        for i in range(len(a) - 1, 0, -1):
            j = random.randint(0, i)             # 包含 i 本身
            a[i], a[j] = a[j], a[i]
        return a'''

S["p384_wrong"] = '''class Solution:
    def __init__(self, nums: List[int]):
        self.arr = nums[:]

    def shuffle(self) -> List[int]:
        a = self.arr
        n = len(a)
        for i in range(n):                       # ✘ 每個位置和「任意位置」交換
            j = random.randrange(n)
            a[i], a[j] = a[j], a[i]
        return a'''

_cls = S.loadns("p384")["Solution"]
obj = _cls([1, 2, 3])
cnt = Counter(tuple(obj.shuffle()) for _ in range(60000))
assert len(cnt) == 6 and all(9000 < c < 11000 for c in cnt.values()), cnt
assert obj.reset() == [1, 2, 3]
_w = S.loadns("p384_wrong")["Solution"]
cntw = Counter()
for _ in range(60000):
    cntw[tuple(_w([1, 2, 3]).shuffle())] += 1
assert max(cntw.values()) > 10800 and min(cntw.values()) < 9200     # 錯誤版本明顯不均勻
print("P384 OK")

emit({
 "num": 384, "slug": "shuffle-an-array",
 "en": [
   "Given an integer array <code>nums</code>, design an algorithm to randomly shuffle the array. All permutations of the array should be <strong>equally likely</strong> as a result of the shuffling.",
   "Implement the <code>Solution</code> class:",
   ("ul", ["<code>Solution(int[] nums)</code> Initializes the object with the integer array <code>nums</code>.",
           "<code>int[] reset()</code> Resets the array to its original configuration and returns it.",
           "<code>int[] shuffle()</code> Returns a random shuffling of the array."]),
 ],
 "zh": [
   "給你一個整數陣列 <code>nums</code>，設計一個演算法把它隨機打亂——<strong>每一種排列出現的機率都必須相同</strong>。",
   ("ul", ["<code>reset()</code>：恢復成原本的陣列並回傳。",
           "<code>shuffle()</code>：回傳隨機打亂後的陣列。"]),
 ],
 "examples": """範例
  Solution([1, 2, 3])
  shuffle() -> 例如 [3, 1, 2]（6 種排列各 1/6 機率）
  reset()   -> [1, 2, 3]
  shuffle() -> 例如 [1, 3, 2]""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 50",
   "−10⁶ ≤ <code>nums[i]</code> ≤ 10⁶",
   "<code>nums</code> 中的元素互不相同",
   "最多呼叫 10⁴ 次",
 ],
 "idea": [
   ("c", """【Fisher–Yates（Knuth）洗牌】
    從最後一個位置開始往前：
        位置 i 和 [0, i] 中隨機一個位置 j 交換（j 可以等於 i）。
    相當於：從還沒決定的牌中隨機抽一張，放到位置 i。

    位置 n-1：從 n 張中選 -> n 種
    位置 n-2：從剩下 n-1 張中選 -> n-1 種
    ...
    總共 n! 種執行路徑，每種對應一個不同的排列 -> 均勻 ✔

【常見的錯誤寫法】
    for i in range(n):
        j = random.randrange(n)     # 和「任意」位置交換 ✘
    執行路徑有 n^n 種，而 n! 通常不整除 n^n
    （n = 3：27 種路徑，6 種排列，27 / 6 不是整數）
    -> 某些排列一定比較常出現。

【只能交換「還沒固定的」部分】
    j 的範圍必須是 [0, i]，不能是 [0, n-1]。"""),
   ("t", ["排列", "123", "132", "213", "231", "312", "321"],
    [["Fisher–Yates", "1/6", "1/6", "1/6", "1/6", "1/6", "1/6"],
     ["錯誤版（27 條路徑）", "4/27", "5/27", "5/27", "5/27", "4/27", "4/27"]]),
 ],
 "approaches": [
   ap("錯誤示範", "和任意位置交換", [
     ("c", S["p384_wrong"]),
     "隨機測試六萬次，某些排列出現次數明顯偏多（約 5/27），某些偏少（約 4/27）。",
   ]),

   ap("解法", "Fisher–Yates 洗牌", [
     ("c", S["p384"]),
     "Python 的 <code>random.shuffle</code> 就是 Fisher–Yates。",
   ], "shuffle O(n)", "O(n)", "", "保存原始陣列", optimal=True),
 ],
 "edges": [
   "<strong>只有一個元素</strong> → 永遠不變。",
   "<strong>reset 之後</strong> → 要回傳原始陣列的副本，避免之後 shuffle 改到原始資料。",
 ],
 "follow": [
   ("h", "驗證洗牌是否均勻"),
   ("c", "統計大量 shuffle 的結果，對 n! 種排列做卡方檢定。本頁的程式碼就用六萬次抽樣，驗證正確版本均勻、錯誤版本偏斜。"),
 ],
 "related": [
   "<strong>第 382 題 鏈結串列隨機節點</strong>",
   "<strong>第 398 題 隨機數索引</strong>",
   "<strong>第 519 題 隨機翻轉矩陣</strong> —— 部分的 Fisher–Yates",
 ],
 "check": [
   "Fisher–Yates 中，位置 i 要和哪個範圍的位置交換？",
   "為什麼和「任意位置」交換不均勻？",
   "為什麼 Fisher–Yates 產生每種排列的機率都是 1/n!？",
 ],
})


# ==================== 385. Mini Parser ====================
class _NestedInteger:
    """題目提供的 NestedInteger（測試用的最小實作）。"""

    def __init__(self, value=None):
        self._int = value
        self._list = [] if value is None else None

    def isInteger(self):
        return self._int is not None

    def add(self, elem):
        if self._list is None:
            self._list, self._int = [], None
        self._list.append(elem)

    def setInteger(self, value):
        self._int, self._list = value, None

    def getInteger(self):
        return self._int

    def getList(self):
        return self._list


def _to_py(ni):
    return ni.getInteger() if ni.isInteger() else [_to_py(x) for x in ni.getList()]


S["p385"] = '''class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":                          # 單一個整數
            return NestedInteger(int(s))
        stack = []
        num = None                               # 正在讀的數字（字串形式）
        for ch in s:
            if ch == "[":
                stack.append(NestedInteger())    # ★ 開一個新的串列
            elif ch == "-" or ch.isdigit():
                num = (num or "") + ch
            else:                                # "," 或 "]"：結束目前的數字
                if num is not None:
                    stack[-1].add(NestedInteger(int(num)))
                    num = None
                if ch == "]" and len(stack) > 1:  # 串列結束：加進上一層
                    inner = stack.pop()
                    stack[-1].add(inner)
        return stack[0]'''

S["p385_rec"] = '''class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        i = 0

        def parse() -> NestedInteger:
            nonlocal i
            if s[i] == "[":
                i += 1                           # 跳過 "["
                ni = NestedInteger()
                while s[i] != "]":
                    ni.add(parse())
                    if s[i] == ",":
                        i += 1
                i += 1                           # 跳過 "]"
                return ni
            j = i                                # 讀一個整數
            while i < len(s) and (s[i] == "-" or s[i].isdigit()):
                i += 1
            return NestedInteger(int(s[j:i]))

        return parse()'''

_p385 = [S.load(x, extra={"NestedInteger": _NestedInteger}) for x in ("p385", "p385_rec")]


def _rnest(d=0):
    if d > 2 or random.random() < 0.4:
        return random.randint(-120, 120)
    return [_rnest(d + 1) for _ in range(random.randrange(0, 4))]


for s, want in [("324", 324), ("[123,[456,[789]]]", [123, [456, [789]]]), ("[]", []), ("[-1,[]]", [-1, []]), ("-7", -7)]:
    for sol in _p385:
        assert _to_py(sol.deserialize(s)) == want, (s, sol)
for _ in range(2000):
    v = _rnest()
    s = str(v).replace(" ", "")
    for sol in _p385:
        assert _to_py(sol.deserialize(s)) == v, s
print("P385 OK")

emit({
 "num": 385, "slug": "mini-parser",
 "en": [
   "Given a string <code>s</code> represents the serialization of a nested list, implement a parser to deserialize it and return <em>the deserialized</em> <code>NestedInteger</code>.",
   "Each element is either an integer or a list whose elements may also be integers or other lists.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，是巢狀串列的序列化結果，請實作一個解析器把它還原成 <code>NestedInteger</code> 物件。",
   "每個元素要嘛是整數，要嘛是另一個串列（元素又可以是整數或串列）。",
   "<code>NestedInteger</code> 提供：<code>NestedInteger()</code> 建立空串列、<code>NestedInteger(value)</code> 建立整數、<code>add(elem)</code> 加入元素。",
 ],
 "examples": """範例 1
  輸入：s = "324"
  輸出：324

範例 2
  輸入：s = "[123,[456,[789]]]"
  輸出：[123,[456,[789]]]""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 5 × 10⁴",
   "<code>s</code> 由數字、<code>'['</code>、<code>']'</code>、<code>'-'</code>、<code>','</code> 組成",
   "<code>s</code> 是合法的 <code>NestedInteger</code> 序列化結果",
   "所有值都在 <code>[−10⁶, 10⁶]</code> 之間",
 ],
 "idea": [
   ("c", """【括號結構 -> 堆疊（或遞迴）】

【堆疊做法】
    '['：開一個新的空串列，推進堆疊
    數字（含負號）：累積到 num
    ','：數字結束 -> 加進堆疊頂端的串列
    ']'：數字結束（如果有）-> 加進頂端；
         然後這個串列結束 -> 彈出，加進下一層的串列
    最後堆疊底部就是答案。

【遞迴下降做法】
    parse()：
        看到 '[' -> 建立串列，反覆 parse() 子元素，直到 ']'
        否則     -> 讀一個整數
    和第 224 題、第 394 題是同一種遞迴結構。

【細節】
    - 整個字串只是一個數字（沒有括號）要特別處理
    - 空串列 "[]" 不能加入任何數字
    - 負號是數字的一部分"""),
 ],
 "approaches": [
   ap("解法一", "堆疊", [
     ("c", S["p385"]),
   ], "O(n)", "O(n)", "", "", optimal=True),

   ap("解法二", "遞迴下降", [
     ("c", S["p385_rec"]),
   ], "O(n)", "O(d)", "", "d = 巢狀深度"),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、堆疊", "O(n)", "O(n) ✔"],
    ["二、遞迴下降", "O(n)", "O(d)"]]),
 "edges": [
   "<strong>只有一個整數</strong>（\"324\"、\"-7\"）→ 直接回傳整數物件。",
   "<strong>空串列</strong>（\"[]\"）→ 空的 NestedInteger。",
   "<strong>負數</strong> → '-' 是數字的一部分。",
 ],
 "follow": [
   ("h", "解析器家族"),
   ("c", "第 224 題（計算機）、第 394 題（字串解碼）、第 726 題（原子的數量）、第 1106 題（解析布林運算式）都是「遇到左括號進一層、右括號退一層」。"),
 ],
 "related": [
   "<strong>第 341 題 扁平化巢狀串列迭代器</strong>",
   "<strong>第 394 題 字串解碼</strong>",
   "<strong>第 224 題 基本計算器</strong>",
 ],
 "check": [
   "遇到 ']' 時要做哪兩件事？",
   "數字什麼時候結束？",
   "整個字串沒有括號時怎麼處理？",
 ],
})


# ==================== 386. Lexicographical Numbers ====================
S["p386"] = '''class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        x = 1
        for _ in range(n):
            res.append(x)
            if x * 10 <= n:              # ★ 優先往下一層走（在後面加 0）
                x *= 10
            else:
                while x % 10 == 9 or x + 1 > n:   # 走不下去：退回上一層
                    x //= 10
                x += 1                    # 同一層的下一個
        return res'''

S["p386_dfs"] = '''class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(x: int) -> None:          # 前序走訪一棵十叉樹
            if x > n:
                return
            res.append(x)
            for d in range(10):
                if x * 10 + d > n:
                    break
                dfs(x * 10 + d)

        for first in range(1, 10):
            dfs(first)
        return res'''

_p386 = [S.load(x) for x in ("p386", "p386_dfs")]
for n in list(range(1, 400)) + [5000, 50000]:
    want = sorted(range(1, n + 1), key=str)
    for sol in _p386:
        assert sol.lexicalOrder(n) == want, n
print("P386 OK")

emit({
 "num": 386, "slug": "lexicographical-numbers",
 "en": [
   "Given an integer <code>n</code>, return all the numbers in the range <code>[1, n]</code> sorted in lexicographical order.",
   "You must write an algorithm that runs in <code>O(n)</code> time and uses <code>O(1)</code> extra space.",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，回傳 <code>1</code> 到 <code>n</code> 所有整數，依<strong>字典序</strong>（當成字串比較）排列。",
   "必須 <code>O(n)</code> 時間、<code>O(1)</code> 額外空間。",
 ],
 "examples": """範例 1
  輸入：n = 13
  輸出：[1,10,11,12,13,2,3,4,5,6,7,8,9]

範例 2
  輸入：n = 2
  輸出：[1,2]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 5 × 10⁴",
 ],
 "idea": [
   ("c", """【字典序 = 十叉樹的前序遍歷】
              (root)
       /   /   ...   \\
      1    2          9
    / | \\
  10 11 ... 19
  / \\
100 101 ...
    前序：1, 10, 100, ..., 101, ..., 11, ..., 2, ...

【O(1) 空間的迭代】
    從 x = 1 開始，每一步找「前序的下一個」：
    1. 能往下走（x × 10 <= n）-> x = x × 10
    2. 不能往下 -> 往右邊的兄弟（x + 1）
       但如果 x 的個位是 9（沒有右兄弟），或 x + 1 > n，
       就先退回父節點（x // 10），重複檢查，再 + 1。

【範例 n = 13】
    1 -> 10（往下）
    10 -> 11 -> 12 -> 13（兄弟）
    13 + 1 = 14 > 13 -> 退回 1 -> 2（兄弟）
    2 -> 20 > 13 不能往下 -> 3 -> ... -> 9"""),
 ],
 "approaches": [
   ap("解法一", "DFS 前序遍歷", [
     ("c", S["p386_dfs"]),
   ], "O(n)", "O(log n)", "", "遞迴深度 ≤ 5"),

   ap("解法二", "迭代找「下一個」", [
     ("c", S["p386"]),
   ], "O(n)", "O(1)", "攤銷；退回父節點的總次數 ≤ n", "不計輸出", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["排序（key=str）", "O(n log n)", "O(n)"],
    ["一、DFS", "O(n)", "O(log n)"],
    ["二、迭代", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>n &lt; 10</strong> → 1..n 本身就是字典序。",
   "<strong>x 的個位是 9</strong> → 沒有右兄弟，要退回上一層。",
   "<strong>x + 1 &gt; n</strong> → 也要退回上一層。",
 ],
 "follow": [
   ("h", "只要第 k 個？"),
   ("c", "第 440 題「字典序的第 K 小數字」（Hard）：不能一個一個走，要計算每個子樹的大小，整棵子樹一次跳過。"),
 ],
 "related": [
   "<strong>第 440 題 字典序的第 K 小數字</strong>",
   "<strong>第 1415 題 長度為 n 的開心字串中字典序第 k 小的字串</strong>",
 ],
 "check": [
   "字典序和十叉樹有什麼關係？",
   "什麼時候往下走、什麼時候往右走、什麼時候退回上一層？",
 ],
})


# ==================== 387. First Unique Character in a String ====================
S["p387"] = '''class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = collections.Counter(s)           # 第一趟：計數
        for i, ch in enumerate(s):             # 第二趟：依原順序找第一個次數為 1 的
            if cnt[ch] == 1:
                return i
        return -1'''

S["p387_pos"] = '''class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 只看 26 個字母：出現一次的字母中，位置最前面的那個
        best = len(s)
        for ch in "abcdefghijklmnopqrstuvwxyz":
            i = s.find(ch)
            if i != -1 and i == s.rfind(ch):   # ★ 第一次出現 == 最後一次出現 -> 只出現一次
                best = min(best, i)
        return best if best < len(s) else -1'''

_p387 = [S.load(x) for x in ("p387", "p387_pos")]
for s, want in [("leetcode", 0), ("loveleetcode", 2), ("aabb", -1)]:
    for sol in _p387:
        assert sol.firstUniqChar(s) == want
for _ in range(3000):
    s = "".join(random.choice("abcd") for _ in range(random.randrange(1, 10)))
    want = next((i for i, c in enumerate(s) if s.count(c) == 1), -1)
    for sol in _p387:
        assert sol.firstUniqChar(s) == want
print("P387 OK")

emit({
 "num": 387, "slug": "first-unique-character-in-a-string",
 "en": [
   "Given a string <code>s</code>, find the <strong>first</strong> non-repeating character in it and return its index. If it does not exist, return <code>-1</code>.",
 ],
 "zh": [
   "給你一個字串 <code>s</code>，找出<strong>第一個不重複</strong>的字元，回傳它的索引；不存在的話回傳 <code>-1</code>。",
 ],
 "examples": """範例 1
  輸入：s = "leetcode"
  輸出：0

範例 2
  輸入：s = "loveleetcode"
  輸出：2

範例 3
  輸入：s = "aabb"
  輸出：-1""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁵",
   "<code>s</code> 只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【兩趟掃描】
    第一趟：數每個字元出現幾次
    第二趟：依原本的順序，找第一個次數為 1 的

    為什麼不能一趟？讀到某個字元時，還不知道它後面會不會再出現。

【只有 26 種字母的技巧】
    對每個字母，用 find 找第一次出現、rfind 找最後一次出現。
    兩者相同 -> 只出現一次。
    在所有只出現一次的字母中，取位置最小的。
    26 × O(n)，但 find / rfind 是 C 實作，實際上很快。"""),
 ],
 "approaches": [
   ap("解法一", "計數 + 第二趟找", [
     ("c", S["p387"]),
   ], "O(n)", "O(1)", "", "最多 26 種字元", optimal=True),

   ap("解法二", "find == rfind", [
     ("c", S["p387_pos"]),
   ], "O(26 · n)", "O(1)", "", ""),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、計數", "O(n)", "O(1) ✔"],
    ["二、find / rfind", "O(26n)", "O(1)"]]),
 "edges": [
   "<strong>全部重複</strong> → −1。",
   "<strong>只有一個字元</strong> → 0。",
 ],
 "follow": [
   ("h", "資料流版本"),
   ("c", "字元一個一個送來，隨時要回答「目前第一個不重複的字元」：用有序字典（或佇列 + 計數），重複的從前面移除——每次查詢攤銷 O(1)。"),
 ],
 "related": [
   "<strong>第 451 題 根據字元出現頻率排序</strong>",
   "<strong>第 1297 題 子字串的最大出現次數</strong>",
 ],
 "check": [
   "為什麼需要兩趟掃描？",
   "find 和 rfind 的結果相同代表什麼？",
 ],
})
