# -*- coding: utf-8 -*-
"""第 17–20 題。"""
import random, itertools
from authoring import emit, ap
from runner import Src, to_list, from_list, ListNode

S = Src()
random.seed(17)

# ==================== 17. Letter Combinations of a Phone Number ====================
S["p17_backtrack"] = '''class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []              # 空輸入回空 list，不是 [""]

        PAD = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        out = []
        path = []                  # 目前已經選到的字母

        def backtrack(i: int) -> None:
            if i == len(digits):
                out.append("".join(path))
                return
            for ch in PAD[digits[i]]:
                path.append(ch)    # 選
                backtrack(i + 1)   # 往下一位
                path.pop()         # 取消選擇（回溯）

        backtrack(0)
        return out'''

S["p17_bfs"] = '''class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        PAD = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        out = [""]                 # 從一個空字串開始
        for d in digits:
            out = [prefix + ch for prefix in out for ch in PAD[d]]
        return out'''

S["p17_product"] = '''from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        PAD = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        # 笛卡兒積：product("abc", "def") -> ('a','d'), ('a','e'), ...
        return ["".join(t) for t in product(*(PAD[d] for d in digits))]'''

_p17 = [S.load(k) for k in ("p17_backtrack", "p17_bfs", "p17_product")]
_PAD = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
for d in ["", "2", "23", "79", "234", "9999"]:
    e = [] if not d else sorted("".join(t) for t in itertools.product(*(_PAD[c] for c in d)))
    for sol in _p17:
        g = sorted(sol.letterCombinations(d))
        assert g == e, ("P17", d, sol, g[:5], e[:5])
assert _p17[0].letterCombinations("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
for _ in range(300):
    d = "".join(random.choice("23456789") for _ in range(random.randint(0, 4)))
    e = [] if not d else sorted("".join(t) for t in itertools.product(*(_PAD[c] for c in d)))
    for sol in _p17:
        assert sorted(sol.letterCombinations(d)) == e, ("P17", d, sol)
print("P17 solutions OK")

_P17_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">digits = &quot;23&quot; 的搜尋樹：深度 = 位數，分支 = 該數字對應的字母數</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="320" cy="48" r="18" fill="none" stroke="var(--gold)" stroke-width="2"/>
              <text x="320" y="53" fill="var(--gold)" font-size="11">&quot;&quot;</text>

              <circle cx="140" cy="126" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="140" y="131" fill="var(--accent)">a</text>
              <circle cx="320" cy="126" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="320" y="131" fill="var(--accent)">b</text>
              <circle cx="500" cy="126" r="18" fill="none" stroke="var(--accent)" stroke-width="2"/>
              <text x="500" y="131" fill="var(--accent)">c</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="306" y1="60" x2="154" y2="112"/>
              <line x1="320" y1="66" x2="320" y2="108"/>
              <line x1="334" y1="60" x2="486" y2="112"/>
            </g>
            <g font-size="11" fill="var(--text-muted)" text-anchor="middle">
              <text x="210" y="82">2→a</text><text x="340" y="92">2→b</text><text x="432" y="82">2→c</text>
            </g>
            <g font-size="12" text-anchor="middle">
              <rect x="42" y="190" width="56" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="70" y="210" fill="#ff8a65">ad</text>
              <rect x="112" y="190" width="56" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="140" y="210" fill="#ff8a65">ae</text>
              <rect x="182" y="190" width="56" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="210" y="210" fill="#ff8a65">af</text>
              <rect x="252" y="190" width="56" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="280" y="210" fill="#ff8a65">bd</text>
              <rect x="322" y="190" width="56" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="350" y="210" fill="#ff8a65">be</text>
              <rect x="392" y="190" width="56" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="420" y="210" fill="#ff8a65">bf</text>
              <rect x="462" y="190" width="56" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="490" y="210" fill="#ff8a65">cd</text>
              <rect x="532" y="190" width="56" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="560" y="210" fill="#ff8a65">ce</text>
              <rect x="532" y="228" width="56" height="30" rx="5" fill="none" stroke="#ff8a65"/><text x="560" y="248" fill="#ff8a65">cf</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.2">
              <line x1="130" y1="142" x2="76" y2="186"/>
              <line x1="140" y1="144" x2="140" y2="186"/>
              <line x1="150" y1="142" x2="204" y2="186"/>
              <line x1="310" y1="142" x2="286" y2="186"/>
              <line x1="320" y1="144" x2="345" y2="186"/>
              <line x1="332" y1="142" x2="414" y2="186"/>
              <line x1="490" y1="142" x2="486" y2="186"/>
              <line x1="500" y1="144" x2="548" y2="186"/>
              <line x1="510" y1="142" x2="556" y2="224"/>
            </g>
            <text x="20" y="284" fill="var(--gold)" font-size="12">共 3 × 3 = 9 條路徑。一般來說是各位數字母數的乘積 —— 最多 4⁴ = 256 種（全是 7 或 9）。</text>'''

emit({
 "num": 17, "slug": "letter-combinations-of-a-phone-number",
 "en": [
   "Given a string containing digits from <code>2-9</code> inclusive, return all possible "
   "letter combinations that the number could represent. Return the answer in "
   "<strong>any order</strong>.",
   "A mapping of digits to letters (just like on the telephone buttons) is given below. "
   "Note that <code>1</code> does not map to any letters.",
 ],
 "zh": [
   "給你一個只含數字 <code>2</code>–<code>9</code> 的字串，回傳它在電話按鍵上"
   "<strong>所有可能的字母組合</strong>。答案<strong>順序不拘</strong>。",
   "對應關係就是老式手機鍵盤：2→abc、3→def、4→ghi、5→jkl、6→mno、7→pqrs、8→tuv、9→wxyz。"
   "注意 <code>1</code> 不對應任何字母（所以輸入裡不會出現）。",
 ],
 "pre": [
   ("note", "組合數學：答案有幾個？", [
     ("c", """digits = "23"  ->  3 × 3 = 9 種
digits = "79"  ->  4 × 4 = 16 種
digits = "234" ->  3 × 3 × 3 = 27 種

一般公式：所有位數對應字母數的乘積。

最壞情況 digits = "7777"（長度 4，每位 4 個字母）：
    4⁴ = 256 種

所以答案的總量是 O(4ⁿ)，n ≤ 4。
這是一道「輸出本身就是指數大」的題目 ——
不可能有比 O(4ⁿ) 更快的演算法，因為光是印出答案就要那麼久。

換句話說：這題不考「怎麼變快」，考的是「怎麼把所有組合有系統地枚舉出來」。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：digits = "23"
  輸出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

範例 2
  輸入：digits = ""
  輸出：[]
  說明：空輸入回空陣列，不是 [""]。

範例 3
  輸入：digits = "2"
  輸出：["a","b","c"]""",
 "constraints": [
   "0 ≤ <code>digits.length</code> ≤ 4",
   "<code>digits[i]</code> 是 <code>'2'</code> 到 <code>'9'</code> 之間的數字",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>空字串要回 <code>[]</code>，不是 <code>[\"\"]</code>。</strong>"
       "這是本題唯一的陷阱，而且會直接讓你 WA。"
       "所有「從空字串開始逐步擴充」的寫法（解法二、三）都必須在最前面擋掉它。",
       "<strong>長度最多 4</strong>，答案最多 256 個。規模小到不需要任何優化。",
       "<strong>輸入保證只有 2–9</strong>，不會有 <code>'0'</code>、<code>'1'</code> 或非數字，"
       "所以查表時不用擔心 KeyError。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P17_FIG, "0 0 640 296"),
   "三種寫法，對應三種思考方式：<strong>深度優先（回溯）、廣度優先（逐層擴充）、"
   "數學（笛卡兒積）</strong>。三個都值得會 —— 回溯是最通用的，"
   "但另外兩個在這題更短更清楚。",
 ],
 "approaches": [
   ap("解法一", "回溯（backtracking）—— 最通用的模板", [
     "把它想成一棵樹：第 <code>i</code> 層對應第 <code>i</code> 個數字，"
     "每個節點的分支數 = 那個數字有幾個字母。走到葉子就收一條答案。",
     ("c", S["p17_backtrack"]),
     ("h", "回溯的三步驟模板"),
     ("c", """for 每個選擇:
    做選擇      path.append(ch)
    往下遞迴    backtrack(i + 1)
    撤銷選擇    path.pop()      <- 這一行是「回溯」這個名字的由來

為什麼要撤銷？
因為 path 是共用的一份。走完 'a' 那條分支回來之後，
path 裡還留著 'a'，如果不 pop 掉，接下來走 'b' 分支
就會變成 "ab..." 而不是 "b..."。

替代寫法：把 path 當成不可變的參數傳下去
    def backtrack(i, path):
        ...
        backtrack(i + 1, path + ch)    # 每層都建新字串，不用 pop

這樣不用手動 pop，但每層都複製一次字串。
在這題（長度 ≤ 4）完全無所謂，
但在深度大的題目上，append/pop 的版本會明顯省記憶體。"""),
     ("h", "為什麼一定要學這個模板？"),
     "因為它是<strong>第 22、39、40、46、47、51、77、78、79、90、93 題的共同骨架</strong>。"
     "這題是最單純的版本（沒有剪枝、沒有去重、沒有狀態），"
     "最適合拿來把模板刻進肌肉記憶。",
   ], "O(4ⁿ · n)", "O(n)", "最多 4ⁿ 條路徑，每條組字串 O(n)",
      "遞迴深度 n；不算輸出", optimal=True),

   ap("解法二", "逐層擴充（BFS / 迭代）", [
     "不用遞迴。維護一個「目前所有半成品」的清單，每處理一個數字就把每個半成品都擴充一輪。",
     ("c", """digits = "23"

初始：       [""]
處理 '2'：   ["a", "b", "c"]
處理 '3'：   ["ad","ae","af", "bd","be","bf", "cd","ce","cf"]

每一輪清單長度乘以「該數字的字母數」。"""),
     ("c", S["p17_bfs"]),
     "整個核心只有<strong>一行 list comprehension</strong>。"
     "<code>out = [prefix + ch for prefix in out for ch in PAD[d]]</code> "
     "的兩個 for 順序不能顛倒 —— 外層是舊清單，內層是新字母。",
     "<strong>為什麼初值是 <code>[\"\"]</code> 而不是 <code>[]</code>？</strong>"
     "因為 <code>[]</code> 的話第一輪的 list comprehension 產生不出任何東西，結果永遠是空的。"
     "空字串是這個「連接」運算的<strong>單位元</strong>，"
     "就像求和從 0 開始、求積從 1 開始一樣。"
     "<strong>但這也正是為什麼空輸入必須在最前面擋掉</strong> —— "
     "否則會回傳 <code>[\"\"]</code>。",
   ], "O(4ⁿ · n)", "O(4ⁿ · n)", "同上", "中間結果全部存在清單裡"),

   ap("解法三", "itertools.product（Python 專用）", [
     "認出這題的本質：<strong>它就是一個笛卡兒積</strong>。",
     ("c", S["p17_product"]),
     ("c", """product("abc", "def") 產生：
    ('a','d') ('a','e') ('a','f')
    ('b','d') ('b','e') ('b','f')
    ('c','d') ('c','e') ('c','f')

product(*(PAD[d] for d in digits)) 就是把每個數字的字母集合
當成一個維度，展開所有組合。

順序也剛好符合題目範例（最後一個維度變化最快）。"""),
     "<strong>面試時可以寫，但要先講出解法一。</strong>"
     "面試官問這題通常是想看回溯模板；直接 <code>product</code> 秒殺會讓他沒東西可以評。"
     "正確的順序是：先寫回溯、跑通、講清楚，再補一句「Python 裡其實 <code>itertools.product</code> 一行就好」。",
   ], "O(4ⁿ · n)", "O(4ⁿ · n)", "同上", "product 是惰性的，但 list comprehension 會全部展開"),
 ],
 "compare": (["解法", "時間", "額外空間", "通用性", "備註"],
   [["一、回溯", "O(4ⁿ·n)", "O(n)", "★★★★★", "10+ 題的共同模板"],
    ["二、逐層擴充", "O(4ⁿ·n)", "O(4ⁿ·n)", "★★★☆☆", "不吃遞迴深度"],
    ["三、product", "O(4ⁿ·n)", "O(4ⁿ·n)", "★☆☆☆☆", "最短，但學不到東西"]]),
 "edges": [
   "<strong>空字串</strong> → <code>[]</code>。<strong>不是 <code>[\"\"]</code></strong>。所有解法都要在最前面擋。",
   "<strong>單一數字</strong>：<code>\"2\"</code> → <code>[\"a\",\"b\",\"c\"]</code>。",
   "<strong>4 個字母的按鍵</strong>：<code>\"7\"</code> → <code>[\"p\",\"q\",\"r\",\"s\"]</code>；"
   "<code>\"9\"</code> → <code>[\"w\",\"x\",\"y\",\"z\"]</code>。這兩個最容易在打表時打錯。",
   "<strong>最長輸入</strong>：<code>\"7777\"</code> → 256 個答案。",
   "<strong>重複的數字</strong>：<code>\"22\"</code> → 9 個答案（<code>aa, ab, ac, ba, ...</code>）。"
   "數字重複<strong>不代表答案重複</strong>，這題不需要去重。",
 ],
 "follow": [
   ("h", "追問一：如果要求答案必須是字典序呢？"),
   "如果 <code>PAD</code> 裡每個字串本身就是字典序（<code>\"abc\"</code>、<code>\"pqrs\"</code>），"
   "那回溯和 product 產生的順序<strong>天生就是字典序</strong> —— 什麼都不用做。"
   "因為回溯是深度優先，先固定高位再變低位，這正是字典序的定義。",
   ("h", "追問二：如果要求只回傳「是英文單字」的組合呢？"),
   "這就是<strong>加剪枝</strong>的時機。把字典建成一棵 Trie，"
   "回溯時每走一步就檢查「目前的 prefix 在 Trie 裡還有路嗎」，沒有就立刻剪掉整棵子樹。"
   "這正是 T9 輸入法的原理，也是第 212 題（Word Search II）的核心技巧。",
   ("h", "追問三：如果數字很長（例如 20 位），要怎麼辦？"),
   "<strong>沒辦法。</strong>答案數量是 4²⁰ ≈ 10¹²，光是印出來就不可能。"
   "這時候問題一定要改：改成「回傳第 k 個組合」（可以用進位制直接算，"
   "類似第 60 題 Permutation Sequence），或「回傳前 100 個」（用產生器惰性求值）。"
   "<strong>當輸出是指數大的時候，正確的回應是質疑問題本身，而不是優化演算法。</strong>",
 ],
 "related": [
   "<strong>第 22 題 Generate Parentheses</strong> —— 回溯 + 剪枝",
   "<strong>第 39／40 題 Combination Sum</strong> —— 回溯 + 去重",
   "<strong>第 46／47 題 Permutations</strong> —— 回溯 + 使用狀態",
   "<strong>第 78／90 題 Subsets</strong> —— 回溯的另一種分支方式",
 ],
 "check": [
   "空字串為什麼要回 <code>[]</code> 而不是 <code>[\"\"]</code>？解法二如果不擋會回傳什麼？",
   "回溯裡的 <code>path.pop()</code> 如果忘了寫，<code>\"23\"</code> 會輸出什麼？",
   "解法二的初值為什麼是 <code>[\"\"]</code>？它在這個運算裡扮演什麼角色？",
   "<code>\"7777\"</code> 有幾個答案？如果輸入長度放寬到 20，這題還有意義嗎？",
 ],
})
print("P17 written")

# ==================== 18. 4Sum ====================
S["p18_nested"] = '''class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        out = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 剪枝：這一層可能的最小值已經超過 target
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 剪枝：這一層可能的最大值還不到 target
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                lo, hi = j + 1, n - 1
                need = target - nums[i] - nums[j]
                while lo < hi:
                    s = nums[lo] + nums[hi]
                    if s < need:
                        lo += 1
                    elif s > need:
                        hi -= 1
                    else:
                        out.append([nums[i], nums[j], nums[lo], nums[hi]])
                        while lo < hi and nums[lo] == nums[lo + 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi - 1]:
                            hi -= 1
                        lo += 1
                        hi -= 1

        return out'''

S["p18_ksum"] = '''class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        def two_sum(start: int, target: int) -> List[List[int]]:
            """在 nums[start:] 上用雙指標找所有和為 target 的「兩個數」。"""
            res = []
            lo, hi = start, len(nums) - 1
            while lo < hi:
                s = nums[lo] + nums[hi]
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
            return res

        def k_sum(start: int, target: int, k: int) -> List[List[int]]:
            """在 nums[start:] 上找所有和為 target 的 k 個數。"""
            if k == 2:
                return two_sum(start, target)

            res = []
            n = len(nums)
            for i in range(start, n - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # 剪枝：剩下最小的 k 個都太大 / 最大的 k 個都太小
                if nums[i] * k > target:
                    break
                if nums[n - 1] * k < target:
                    break
                for rest in k_sum(i + 1, target - nums[i], k - 1):
                    res.append([nums[i]] + rest)
            return res

        return k_sum(0, target, 4)'''


def _p18_ref(nums, target):
    found = set()
    for c in itertools.combinations(sorted(nums), 4):
        if sum(c) == target:
            found.add(c)
    return sorted(found)


_p18 = [S.load(k) for k in ("p18_nested", "p18_ksum")]
for c, t in [([1, 0, -1, 0, -2, 2], 0), ([2, 2, 2, 2, 2], 8), ([], 0), ([1, 2], 3),
             ([0, 0, 0, 0], 0), ([-3, -1, 0, 2, 4, 5], 0),
             ([1000000000] * 4, 4000000000)]:
    e = _p18_ref(c, t)
    for sol in _p18:
        g = sorted(tuple(sorted(x)) for x in sol.fourSum(list(c), t))
        assert g == e, ("P18", c, t, sol, g, e)
for _ in range(2000):
    c = [random.randint(-5, 5) for _ in range(random.randint(0, 9))]
    t = random.randint(-8, 8)
    e = _p18_ref(c, t)
    for sol in _p18:
        g = sorted(tuple(sorted(x)) for x in sol.fourSum(list(c), t))
        assert g == e, ("P18", c, t, sol, g, e)
print("P18 solutions OK")

emit({
 "num": 18, "slug": "4sum",
 "en": [
   "Given an array <code>nums</code> of <code>n</code> integers, return an array of all the "
   "<strong>unique</strong> quadruplets <code>[nums[a], nums[b], nums[c], nums[d]]</code> "
   "such that <code>a, b, c, d</code> are distinct indices and "
   "<code>nums[a] + nums[b] + nums[c] + nums[d] == target</code>.",
   "You may return the answer in any order.",
 ],
 "zh": [
   "給你一個長度為 <code>n</code> 的整數陣列 <code>nums</code> 和一個目標值 <code>target</code>，"
   "找出所有<strong>不重複</strong>的四元組，使四個數相加等於 <code>target</code>。",
   "四個索引必須互不相同，答案順序不拘。",
 ],
 "pre": [
   ("note", "這題就是 3Sum 再包一層", [
     "如果你已經把第 15 題寫熟了，這題只是把同一套邏輯往外多包一層迴圈。"
     "<strong>去重的方式、雙指標的移動、剪枝的想法，全部一模一樣。</strong>",
     ("c", """kSum 的通用降維：

  4Sum  ->  固定一個數，剩下就是 3Sum
        ->  固定兩個數，剩下就是 2Sum（雙指標，O(n)）

  複雜度：O(n³)

  一般地：kSum = O(n^(k-1))
    2Sum: O(n)      （排序後雙指標）
    3Sum: O(n²)
    4Sum: O(n³)
    5Sum: O(n⁴)
    ..."""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [1, 0, -1, 0, -2, 2], target = 0
  輸出：[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]

範例 2
  輸入：nums = [2, 2, 2, 2, 2], target = 8
  輸出：[[2,2,2,2]]
  說明：雖然有多種索引組合，但值都一樣，只算一組。""",
 "constraints": [
   "1 ≤ <code>nums.length</code> ≤ 200",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
   "−10⁹ ≤ <code>target</code> ≤ 10⁹",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>n ≤ 200</strong>。O(n³) 是 8 × 10⁶ —— 輕鬆過。"
       "O(n⁴) 是 1.6 × 10⁹ —— 太慢。所以目標是 O(n³)。",
       "<strong>數值和 target 都到 ±10⁹。</strong>四個數相加最大可到 4 × 10⁹，"
       "<strong>超過 32 位元有號整數的範圍</strong>。"
       "Python 不受影響，但在 C++／Java 裡累加時<strong>必須用 64 位元</strong>，"
       "否則會溢位。這是這題相對於第 15 題新增的唯一陷阱。",
       "<strong>陣列長度可能小於 4</strong>（最小是 1）。"
       "<code>range(n-3)</code> 在 n &lt; 4 時是空的，自然就對了 —— 不必額外檢查。",
     ]),
   ]),
 ],
 "idea": [
   "兩種寫法：<strong>直接寫死兩層迴圈</strong>（好懂、好 debug），"
   "或<strong>寫成遞迴的 kSum</strong>（優雅、可以直接推廣到 5Sum、6Sum）。"
   "面試時建議寫第一種，但能講出第二種會加分很多。",
 ],
 "approaches": [
   ap("解法一", "兩層迴圈 + 雙指標（直接寫）", [
     ("c", S["p18_nested"]),
     ("h", "去重要處理三個位置"),
     ("c", """i 層：  if i > 0     and nums[i] == nums[i-1]:   continue
j 層：  if j > i + 1 and nums[j] == nums[j-1]:   continue
lo/hi： 找到答案後跳過重複值（兩個 while）

注意 j 層的邊界是 j > i + 1，不是 j > 0！
  因為 j 的起點是 i + 1，我們要允許「j 的第一個位置」，
  只跳過它之後的重複。
  寫成 j > 0 的話，當 i 變大時 nums[i+1] 可能剛好等於 nums[i]，
  就會被錯誤地跳掉。

這個 off-by-one 是 4Sum 相對 3Sum 最容易寫錯的地方。"""),
     ("h", "四個剪枝，兩兩對稱"),
     ("c", """對每一層（以 i 層為例）：

  最小可能和 = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
      > target  ->  break     （後面的 i 只會更大，整層結束）

  最大可能和 = nums[i] + nums[n-3] + nums[n-2] + nums[n-1]
      < target  ->  continue  （這個 i 沒救，但更大的 i 可能有）

一個是 break 一個是 continue，這個不對稱很容易搞反：
  「最小值都太大」-> 越往後越大 -> 全部沒救 -> break
  「最大值都太小」-> 換個更大的 i 可能有救 -> continue

沒有這四個剪枝，n=200 時也能過，
但在「大量相同值」或「target 極端」的測資上會慢好幾倍。"""),
   ], "O(n³)", "O(log n)", "兩層迴圈 × 雙指標", "排序本身；不算輸出", optimal=True),

   ap("解法二", "遞迴 kSum（優雅，可推廣）", [
     "把「固定一個數，剩下遞迴解」這個想法直接寫成程式碼。"
     "<strong>base case 是 k == 2，用雙指標 O(n) 解決。</strong>",
     ("c", S["p18_ksum"]),
     ("h", "這個寫法的好處"),
     ("ul", [
       "<strong>去重邏輯只寫兩次</strong>（<code>k_sum</code> 裡一次、<code>two_sum</code> 裡一次），"
       "而不是每一層都抄一遍。抄得越少，寫錯的機會越少。",
       "<strong>改成 5Sum 只要改最後一行</strong>：<code>k_sum(0, target, 5)</code>。",
       "<strong>剪枝也統一了</strong>：<code>nums[i] * k &gt; target</code> 表示"
       "「就算剩下 k 個都取最小的 <code>nums[i]</code>，和也太大」。",
     ]),
     ("h", "剪枝 <code>nums[i] * k &gt; target</code> 為什麼對？"),
     ("c", """排序後，從位置 i 開始取 k 個數，最小的可能和是
    nums[i] + nums[i+1] + ... + nums[i+k-1]
而每一項都 ≥ nums[i]，所以這個和 ≥ nums[i] * k。

如果 nums[i] * k > target，那最小可能和也 > target -> 沒救。
而且之後的 i 只會讓 nums[i] 更大 -> break。

這是一個「比實際最小值寬鬆」的下界，
所以它剪得沒有解法一的精確剪枝那麼多，
但它只需要一次乘法，而且對任何 k 都成立。"""),
     "<strong>什麼時候該寫這個版本？</strong>"
     "面試官明確問「如果是 kSum 呢」的時候。"
     "一開始就寫遞迴版可能會被認為是在炫技，而且遞迴的去重邊界（<code>i &gt; start</code>）"
     "比迴圈版更容易寫錯。",
   ], "O(n^(k−1))", "O(k)", "k=4 時是 O(n³)", "遞迴深度 k；不算輸出"),
 ],
 "compare": (["解法", "時間", "空間", "推廣到 kSum", "好寫程度"],
   [["一、兩層迴圈 + 雙指標", "O(n³)", "O(log n)", "要手動抄一層", "★★★★☆"],
    ["二、遞迴 kSum", "O(n^(k−1))", "O(k)", "改一個參數", "★★★☆☆"]]),
 "edges": [
   "<strong>長度不足 4</strong>：<code>[]</code>、<code>[1,2]</code> → <code>[]</code>。",
   "<strong>全部相同</strong>：<code>([2,2,2,2,2], 8)</code> → <code>[[2,2,2,2]]</code>（只有一組）。"
   "這是最能抓出去重 bug 的測資。",
   "<strong>四個 0</strong>：<code>([0,0,0,0], 0)</code> → <code>[[0,0,0,0]]</code>。",
   "<strong>溢位測資</strong>：<code>([10⁹,10⁹,10⁹,10⁹], 4×10⁹)</code> → 有答案。"
   "在 Java/C++ 裡用 int 累加會溢位成負數而算不出來。",
   "<strong>沒有答案</strong>：<code>([1,2,3,4], 100)</code> → <code>[]</code>。驗證剪枝不會誤判。",
   "<strong>j 層去重的邊界</strong>：<code>([-3,-1,0,2,4,5], 0)</code> 這類含重複的測資，"
   "把 <code>j &gt; i+1</code> 誤寫成 <code>j &gt; 0</code> 會漏掉答案。",
 ],
 "follow": [
   ("h", "追問一：有沒有比 O(n³) 更快的做法？"),
   "有一個 <strong>O(n²)</strong> 的做法，但代價是 O(n²) 的記憶體："
   "把所有「兩個數的和」連同它們的索引存進一個雜湊表（共 n²/2 筆），"
   "然後對每一對 <code>(a, b)</code> 去查 <code>target − a − b</code> 有沒有對應的配對，"
   "同時檢查四個索引不重疊。",
   "<strong>但實務上通常不值得</strong>：n = 200 時 O(n³) = 8 × 10⁶ 已經很快，"
   "而雜湊表版本要處理「索引不重疊」和「去重」兩個相當麻煩的問題，"
   "程式碼會長得多、錯的機會也高得多。"
   "面試時值得提出來當作「知道有這條路」，但不建議真的寫。",
   ("h", "追問二：k 很大的時候（例如 kSum 中 k = 10）呢？"),
   "O(n⁹) 完全不可行。這時候要改用<strong>中間相遇（meet in the middle）</strong>："
   "把 k 個數分成兩半，各自枚舉所有 C(n, k/2) 種組合的和，"
   "存進雜湊表後配對。複雜度大約是 O(n^(k/2))，"
   "對 k = 10、n = 40 這種規模是可行的。"
   "這也是子集合和（Subset Sum）問題的經典技巧。",
   ("h", "追問三：為什麼一定要排序？"),
   "排序在這題同時做了<strong>三件事</strong>：",
   ("ul", [
     "讓雙指標能用（需要單調性）",
     "讓相同的值相鄰，去重才能用「和前一個比」這種 O(1) 的方式做",
     "讓剪枝能用（知道「往後只會更大」）",
   ]),
   "而排序只要 O(n log n)，遠小於 O(n³)。<strong>這是一筆非常划算的交易。</strong>",
 ],
 "related": [
   "<strong>第 1 題 Two Sum</strong>、<strong>第 15 題 3Sum</strong>、"
   "<strong>第 16 題 3Sum Closest</strong> —— 同一家族",
   "<strong>第 454 題 4Sum II</strong> —— 四個獨立陣列各取一個，可以用雜湊表做到 O(n²)",
 ],
 "check": [
   "j 層的去重為什麼寫 <code>j &gt; i + 1</code> 而不是 <code>j &gt; 0</code>？請舉一個會出錯的輸入。",
   "為什麼「最小值太大」是 break 而「最大值太小」是 continue？",
   "在 Java 裡這題有什麼陷阱是第 15 題沒有的？",
   "kSum 的複雜度為什麼是 O(n^(k−1)) 而不是 O(n^k)？最後那一層省在哪裡？",
 ],
})
print("P18 written")
