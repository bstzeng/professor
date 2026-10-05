# -*- coding: utf-8 -*-
"""第 530、532、535、537、538、539、540、541 題。"""
import random
from collections import Counter
from authoring import ap
from lcauto import em
from runner import Src
from lchelp import lv, bst, nodes, ser

S = Src()
random.seed(530)


def _inorder(t):
    out = []
    def go(n):
        if n:
            go(n.left); out.append(n.val); go(n.right)
    go(t)
    return out


# ==================== 530. Minimum Absolute Difference in BST ====================
S["p530"] = '''class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res, prev = float("inf"), None
        def inorder(nd):
            nonlocal res, prev
            if not nd:
                return
            inorder(nd.left)
            if prev is not None:
                res = min(res, nd.val - prev)   # ★ 中序有序：最小差一定出現在相鄰兩個值之間
            prev = nd.val
            inorder(nd.right)
        inorder(root)
        return res'''

_p530 = S.load("p530")
for _ in range(1500):
    vals = random.sample(range(100), random.randint(2, 12))
    s = sorted(vals)
    assert _p530.getMinimumDifference(bst(vals)) == min(b - a for a, b in zip(s, s[1:]))
print("P530 OK")

em({
 "num": 530, "title": "二元搜尋樹的最小絕對差",
 "desc": "排序後最小差一定出現在相鄰元素之間；BST 的中序走訪就是排序結果。",
 "zh": ["給你一棵二元搜尋樹的根節點，回傳樹中<strong>任意兩個不同節點值</strong>之差的最小值。", "（本題與第 783 題相同。）"],
 "idea": [
   ("c", """【排序陣列的最小差】
    排好序後，最小差一定出現在某對相鄰元素之間
    （隔一個的差 = 兩段相鄰差的和，只會更大）。

【BST 的中序走訪就是排序】
    中序走訪時記住上一個值 prev，
    每個節點和 prev 比較，更新最小差。
    不需要真的把序列存下來。"""),
 ],
 "approaches": [
   ap("解法", "中序走訪 + 相鄰差", [("c", S["p530"])], "O(n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>只有兩個節點</strong> → 它們的差。", "<strong>非相鄰的節點</strong>（例如根和左子樹最右節點）→ 中序走訪會自然處理。"],
 "follow": [("h", "如果不是 BST？"), ("c", "一般二元樹：先收集所有值再排序，O(n log n)。BST 讓我們省掉排序。")],
 "related": ["<strong>第 783 題 二元搜尋樹節點最小距離</strong>", "<strong>第 501 題 BST 中的眾數</strong>", "<strong>第 98 題 驗證二元搜尋樹</strong>"],
 "check": ["為什麼最小差一定在相鄰元素之間？", "prev 的初始值應該怎麼設？"],
})


# ==================== 532. K-diff Pairs in an Array ====================
S["p532"] = '''class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        if k == 0:
            return sum(c >= 2 for c in cnt.values())   # ★ 差為 0：同一個值至少出現兩次
        return sum(x + k in cnt for x in cnt)          # 以較小的值 x 為代表，避免重複計算'''

_p532 = S.load("p532", extra={"Counter": Counter})
for _ in range(3000):
    a = [random.randint(0, 6) for _ in range(random.randint(1, 8))]; k = random.randint(0, 4)
    want = len({(a[i], a[j]) for i in range(len(a)) for j in range(len(a)) if i != j and a[j] - a[i] == k})
    assert _p532.findPairs(a, k) == want
print("P532 OK")

em({
 "num": 532, "title": "陣列中的 k-diff 數對",
 "desc": "以「值」而非索引計算不同的數對：k > 0 時檢查 x + k 是否存在，k = 0 時看值是否重複。",
 "zh": [
   "給你整數陣列 <code>nums</code> 和整數 <code>k</code>，回傳<strong>不同的</strong> k-diff 數對的數量。",
   "k-diff 數對 <code>(nums[i], nums[j])</code> 需滿足 <code>i != j</code> 且 <code>|nums[i] − nums[j]| == k</code>。數對以「值」區分：(1, 3) 和 (3, 1) 算同一對。",
 ],
 "idea": [
   ("c", """【數對以值區分 -> 先去重計數】
    cnt = 每個值的出現次數。

【k > 0】
    每一對 (x, x + k) 用較小的 x 代表，只數一次：
    答案 = 有多少個不同的 x 使得 x + k 也存在。

【k = 0】
    (x, x) 需要兩個不同的索引 -> x 至少出現兩次。

【注意】
    k = 0 時若套用 k > 0 的公式，每個值都會和自己配成一對，錯誤。"""),
 ],
 "approaches": [
   ap("解法", "雜湊表計數", [("c", S["p532"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>k = 0</strong> → 只數重複出現的值。", "<strong>重複值</strong> → [1,1,3], k=2 只算 1 對。"],
 "follow": [("h", "排序 + 雙指標"), ("c", "排序後用雙指標找差為 k 的數對，跳過重複值。O(n log n)、O(1) 額外空間。")],
 "related": ["<strong>第 1 題 兩數之和</strong>", "<strong>第 2006 題 差的絕對值為 K 的數對數目</strong>"],
 "check": ["為什麼 k = 0 要特別處理？", "怎麼確保每一對只被數一次？"],
})


# ==================== 535. Encode and Decode TinyURL ====================
S["p535"] = '''class Codec:
    alphabet = string.ascii_letters + string.digits

    def __init__(self):
        self.code2url = {}
        self.url2code = {}

    def encode(self, longUrl: str) -> str:
        if longUrl not in self.url2code:            # 同一個網址重複編碼時回傳相同結果
            while True:
                code = "".join(random.choice(self.alphabet) for _ in range(6))   # 62⁶ ≈ 568 億種
                if code not in self.code2url:       # ★ 碰撞就重抽
                    break
            self.code2url[code] = longUrl
            self.url2code[longUrl] = code
        return "http://tinyurl.com/" + self.url2code[longUrl]

    def decode(self, shortUrl: str) -> str:
        return self.code2url[shortUrl.rsplit("/", 1)[1]]'''

import string
_c535 = S.loadns("p535", extra={"string": string})["Codec"]()
urls = ["https://leetcode.com/problems/design-tinyurl", "https://a.b/c?d=e", "x"] + ["u%d" % i for i in range(500)]
for u in urls:
    assert _c535.decode(_c535.encode(u)) == u
assert _c535.encode(urls[0]) == _c535.encode(urls[0])
print("P535 OK")

em({
 "num": 535, "title": "TinyURL 的加密與解密",
 "desc": "系統設計小題：隨機短碼 + 兩個雜湊表，處理碰撞與重複網址；比較自增 ID、雜湊等方案。",
 "zh": [
   "TinyURL 是一個縮網址服務：輸入長網址，得到一個短網址。設計 <code>encode</code>（長→短）和 <code>decode</code>（短→長）。",
   "演算法沒有限制，只要短網址能還原成原本的長網址即可。",
 ],
 "idea": [
   ("c", """【核心：短碼 -> 長網址 的對照表】
    decode 只是查表。重點在 encode 怎麼產生短碼。

【方案比較】
    自增 ID（0, 1, 2…轉 62 進位）：
        簡單、不會碰撞，但可以被猜出下一個網址、洩漏總量。
    雜湊（例如取 MD5 前幾位）：
        同一個網址總是同一個碼，但截短後可能碰撞。
    隨機 6 碼（62⁶ ≈ 568 億種）：
        難以猜測；碰撞時重抽即可。

【額外的反查表】
    url2code：同一個長網址重複編碼時給同一個短碼，不浪費空間。"""),
 ],
 "approaches": [
   ap("解法", "隨機短碼 + 雙向雜湊表", [("c", S["p535"])], "encode / decode：O(L)", "O(總網址長度)", optimal=True),
 ],
 "edges": ["<strong>碰撞</strong> → 重抽。", "<strong>同一網址多次編碼</strong> → 回傳同一個短網址。"],
 "follow": [("h", "真實系統還要考慮"), ("c", "分散式下如何產生不碰撞的 ID（例如每台機器預先領一段 ID 區間）、過期與刪除、快取熱門短網址、302 轉址與點擊統計。")],
 "related": ["<strong>第 380 題 O(1) 插入、刪除與隨機取得</strong>", "<strong>第 297 題 二元樹的序列化與反序列化</strong>"],
 "check": ["自增 ID 方案有什麼缺點？", "為什麼要多一張 url2code？"],
})


# ==================== 537. Complex Number Multiplication ====================
S["p537"] = '''class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        def parse(s):
            a, b = s[:-1].split("+")        # 去掉結尾的 i，再用 + 切開
            return int(a), int(b)
        a, b = parse(num1)
        c, d = parse(num2)
        # ★ (a + bi)(c + di) = (ac - bd) + (ad + bc)i，因為 i² = -1
        return "%d+%di" % (a * c - b * d, a * d + b * c)'''

_p537 = S.load("p537")
for _ in range(3000):
    a, b, c, d = (random.randint(-100, 100) for _ in range(4))
    z = complex(a, b) * complex(c, d)
    assert _p537.complexNumberMultiply("%d+%di" % (a, b), "%d+%di" % (c, d)) == "%d+%di" % (z.real, z.imag)
print("P537 OK")

em({
 "num": 537, "title": "複數乘法",
 "desc": "解析 \"a+bi\" 字串，套用 (a+bi)(c+di) = (ac−bd) + (ad+bc)i。",
 "zh": [
   "複數可以寫成字串 <code>\"real+imaginaryi\"</code>，例如 <code>\"1+-1i\"</code>（實部與虛部都是 [−100, 100] 的整數）。",
   "給你兩個這種格式的複數 <code>num1</code>、<code>num2</code>，回傳它們乘積的字串（同樣格式）。",
 ],
 "idea": [
   ("c", """【解析】
    "a+bi"：去掉最後的 'i'，用 '+' 切成兩段。
    負虛部寫成 "1+-1i"，切開後 int("-1") 照樣能轉。

【乘法】
    (a + bi)(c + di) = ac + adi + bci + bd·i²
                     = (ac - bd) + (ad + bc)i
    （i² = -1）"""),
 ],
 "approaches": [
   ap("解法", "解析 + 公式", [("c", S["p537"])], "O(1)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>負數</strong> → \"1+-1i\" 的 split('+') 仍是兩段。", "<strong>結果的虛部為負</strong> → 輸出 \"0+-2i\" 這種格式。"],
 "follow": [("h", "Python 內建複數"), ("c", "Python 有 complex 型別（1+2j），但輸入格式用 i 不用 j，而且輸出格式也固定，所以手動解析比較直接。")],
 "related": ["<strong>第 592 題 分數加減運算</strong>", "<strong>第 43 題 字串相乘</strong>"],
 "check": ["(a+bi)(c+di) 的展開式是什麼？", "負的虛部怎麼解析？"],
})


# ==================== 538. Convert BST to Greater Tree ====================
S["p538"] = '''class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        def rev_inorder(nd):            # ★ 反向中序（右 -> 根 -> 左）：由大到小走訪
            nonlocal total
            if nd:
                rev_inorder(nd.right)
                total += nd.val         # total = 所有 >= 目前值的節點和
                nd.val = total
                rev_inorder(nd.left)
        rev_inorder(root)
        return root'''

_p538 = S.load("p538")
for _ in range(1500):
    vals = random.sample(range(-20, 40), random.randint(1, 12))
    want = sorted(sum(y for y in vals if y >= x) for x in vals)
    assert sorted(n.val for n in nodes(_p538.convertBST(bst(vals)))) == want
t = bst([4, 1, 6, 0, 2, 5, 7, 3, 8])
assert ser(_p538.convertBST(t)) == [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]
print("P538 OK")

em({
 "num": 538, "title": "把二元搜尋樹轉換為累加樹",
 "desc": "反向中序走訪（右、根、左）由大到小經過每個節點，邊走邊累加。",
 "zh": [
   "給你一棵二元搜尋樹（節點值互不相同），把它轉成<strong>累加樹</strong>：每個節點的新值 = 原樹中<strong>大於或等於</strong>它的所有節點值之和。",
   "（本題與第 1038 題相同。）",
 ],
 "idea": [
   ("c", """【需要「所有比我大的值的和」】
    如果由大到小走訪，走到每個節點時，
    已經走過的節點正好是所有比它大的 ->
    維護一個累加和 total，加上自己後寫回。

【由大到小 = 反向中序】
    中序（左、根、右）是由小到大；
    反過來（右、根、左）就是由大到小。"""),
 ],
 "approaches": [
   ap("解法", "反向中序走訪", [("c", S["p538"])], "O(n)", "O(h)", optimal=True),
 ],
 "edges": ["<strong>最大的節點</strong> → 值不變。", "<strong>負數節點</strong> → 累加照樣正確。"],
 "follow": [("h", "O(1) 空間"), ("c", "反向的 Morris 走訪：把「左右」對調，借用後繼節點的空左指標當線索。")],
 "related": ["<strong>第 1038 題 從 BST 到更大和樹</strong>", "<strong>第 94 題 二元樹的中序走訪</strong>"],
 "check": ["為什麼反向中序是由大到小？", "total 在走訪到某節點時代表什麼？"],
})


# ==================== 539. Minimum Time Difference ====================
S["p539"] = '''class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) > 1440:
            return 0                                # 鴿籠原理：一天只有 1440 分鐘，一定有重複
        mins = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        res = min(b - a for a, b in zip(mins, mins[1:]))
        return min(res, mins[0] + 1440 - mins[-1])  # ★ 跨過午夜：最早的 + 24 小時 - 最晚的'''

_p539 = S.load("p539")
assert _p539.findMinDifference(["23:59", "00:00"]) == 1 and _p539.findMinDifference(["00:00", "23:59", "00:00"]) == 0
for _ in range(2000):
    ts = [random.randrange(1440) for _ in range(random.randint(2, 6))]
    want = min(min(abs(a - b), 1440 - abs(a - b)) for i, a in enumerate(ts) for b in ts[i + 1:])
    assert _p539.findMinDifference(["%02d:%02d" % divmod(t, 60) for t in ts]) == want
print("P539 OK")

em({
 "num": 539, "title": "最小時間差",
 "desc": "轉成分鐘後排序，比較相鄰的差，別忘了跨午夜的那一對；超過 1440 個時間點必有重複。",
 "zh": ["給你一組 24 小時制的時間點 <code>\"HH:MM\"</code>，回傳任意兩個時間點之間的<strong>最小分鐘差</strong>。"],
 "idea": [
   ("c", """【轉成分鐘 + 排序】
    "HH:MM" -> HH*60 + MM，範圍 [0, 1440)。
    排序後，最小差一定在相鄰兩個之間……

【環形！】
    時間是一圈：23:59 和 00:00 只差 1 分鐘。
    所以還要比較「最早 + 1440 - 最晚」這一對。

【鴿籠原理】
    一天只有 1440 個不同的分鐘，
    超過 1440 個時間點一定有重複 -> 直接回傳 0。"""),
 ],
 "approaches": [
   ap("解法", "排序 + 相鄰差 + 跨午夜", [("c", S["p539"])], "O(n log n)", "O(n)", "", "", optimal=True),
 ],
 "edges": ["<strong>重複時間</strong> → 0。", "<strong>跨午夜</strong> → 23:59 與 00:00 差 1。"],
 "follow": [("h", "O(n) 做法"), ("c", "用長度 1440 的布林陣列標記出現過的分鐘（重複就回傳 0），再依序掃一遍取相鄰差，相當於計數排序。")],
 "related": ["<strong>第 530 題 BST 的最小絕對差</strong>", "<strong>第 164 題 最大間距</strong>"],
 "check": ["為什麼還要比較最早和最晚的時間？", "什麼時候可以直接回傳 0？"],
})


# ==================== 540. Single Element in a Sorted Array ====================
S["p540"] = '''class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid % 2 == 1:
                mid -= 1                    # 讓 mid 對齊成偶數：成對的元素應該在 (偶, 偶+1)
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2                # ★ 配對沒被打亂 -> 單一元素在右邊
            else:
                hi = mid                    # 配對亂了 -> 單一元素在 mid 或左邊
        return nums[lo]'''

_p540 = S.load("p540")
for _ in range(3000):
    k = random.randint(0, 8)
    vals = sorted(random.sample(range(50), k + 1))
    single = random.choice(vals)
    a = sorted(v for v in vals for _ in range(1 if v == single else 2))
    assert _p540.singleNonDuplicate(a) == single
print("P540 OK")

em({
 "num": 540, "title": "有序陣列中的單一元素",
 "desc": "單一元素出現前，配對從偶數索引開始；出現後就錯位。用這個性質二分，O(log n)。",
 "zh": ["給你一個<strong>已排序</strong>的整數陣列，其中每個元素都恰好出現兩次，只有一個元素出現一次。找出它。要求 <code>O(log n)</code> 時間、<code>O(1)</code> 空間。"],
 "idea": [
   ("c", """【異或可以做到 O(n)，但要求 O(log n)】

【觀察配對的位置】
    [1,1,2,3,3,4,4,8,8]
     0 1 2 3 4 5 6 7 8
    單一元素 2 之前：配對在 (0,1) —— 從偶數索引開始。
    單一元素之後：配對在 (3,4)、(5,6)、(7,8) —— 從奇數索引開始。

【二分】
    把 mid 調成偶數，看 nums[mid] == nums[mid+1]：
        相等：mid 之前沒被打亂 -> 單一元素在 mid+2 之後
        不等：已經錯位 -> 單一元素在 mid 或更左
    區間每次縮小一半。"""),
 ],
 "approaches": [
   ap("解法", "對偶數索引二分", [("c", S["p540"])], "O(log n)", "O(1)", optimal=True),
 ],
 "edges": ["<strong>只有一個元素</strong> → 直接回傳。", "<strong>單一元素在頭或尾</strong> → 二分照樣收斂。"],
 "follow": [("h", "異或的寫法"), ("c", "也可以寫成：比較 nums[mid] 和 nums[mid ^ 1]。mid 是偶數時 mid^1 = mid+1，奇數時 mid^1 = mid−1——正好是「應該配對的夥伴」。")],
 "related": ["<strong>第 136 題 只出現一次的數字</strong>", "<strong>第 162 題 尋找峰值</strong>"],
 "check": ["單一元素前後，配對的起始索引有什麼差別？", "為什麼要把 mid 調成偶數？"],
})


# ==================== 541. Reverse String II ====================
S["p541"] = '''class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2 * k):          # 每 2k 個字元一段
            a[i:i + k] = reversed(a[i:i + k])     # ★ 反轉每段的前 k 個（不足 k 個就全部反轉）
        return "".join(a)'''

_p541 = S.load("p541")
assert _p541.reverseStr("abcdefg", 2) == "bacdfeg" and _p541.reverseStr("abcd", 2) == "bacd"
for _ in range(2000):
    s = "".join(random.choice("abcdef") for _ in range(random.randint(1, 15))); k = random.randint(1, 6)
    out = ""
    for i in range(0, len(s), 2 * k):
        out += s[i:i + k][::-1] + s[i + k:i + 2 * k]
    assert _p541.reverseStr(s, k) == out
print("P541 OK")

em({
 "num": 541, "title": "反轉字串 II",
 "desc": "每 2k 個字元一段，反轉每段的前 k 個；切片會自動處理不足 k 個的結尾。",
 "zh": [
   "給你字串 <code>s</code> 和整數 <code>k</code>，從頭開始每 <code>2k</code> 個字元一段，反轉每段的前 <code>k</code> 個字元。",
   "剩下不足 <code>k</code> 個字元時，全部反轉；剩下介於 <code>k</code> 到 <code>2k</code> 個時，反轉前 <code>k</code> 個，其餘不動。",
 ],
 "idea": [
   ("c", """【規則其實只有一條】
    每段起點 i = 0, 2k, 4k, ...，反轉 s[i : i+k]。
    「不足 k 個全部反轉」「k 到 2k 之間反轉前 k 個」
    都被切片 s[i:i+k] 自動處理了（切片超出範圍會截短）。"""),
 ],
 "approaches": [
   ap("解法", "每 2k 一段反轉前 k 個", [("c", S["p541"])], "O(n)", "O(n)", "", "Python 字串不可變，需要轉成 list", optimal=True),
 ],
 "edges": ["<strong>k 大於字串長度</strong> → 整個反轉。", "<strong>k = 1</strong> → 不變。"],
 "follow": [("h", "相關"), ("c", "第 344 題反轉整個字串；第 557 題反轉每個單字；本題反轉固定長度的區塊。")],
 "related": ["<strong>第 344 題 反轉字串</strong>", "<strong>第 557 題 反轉字串中的單字 III</strong>"],
 "check": ["為什麼切片可以自動處理結尾不足的情況？"],
})
