# -*- coding: utf-8 -*-
"""第 732、733、735、736、738、739、740、741 題。"""
import random, bisect, heapq
from collections import Counter
from functools import lru_cache
from authoring import ap
from lcauto import em
from runner import Src

S = Src()
random.seed(732)


# ==================== 732. My Calendar III ====================
S["p732"] = '''class MyCalendarThree:
    def __init__(self):
        self.times = []                 # 所有出現過的時間點（排序）
        self.delta = {}                 # 時間點 -> 這裡開始 +1 / 結束 -1 的淨變化

    def book(self, startTime: int, endTime: int) -> int:
        for t, d in ((startTime, 1), (endTime, -1)):
            if t not in self.delta:
                bisect.insort(self.times, t)
                self.delta[t] = 0
            self.delta[t] += d
        cur = best = 0
        for t in self.times:            # ★ 掃描線：依時間累加差分，途中的最大值就是最大重疊數
            cur += self.delta[t]
            best = max(best, cur)
        return best'''

_C3 = S.loadns("p732")["MyCalendarThree"]
for _ in range(400):
    o = _C3(); cnt = [0] * 40
    for _ in range(12):
        s = random.randint(0, 30); e = random.randint(s + 1, 35)
        for x in range(s, e): cnt[x] += 1
        assert o.book(s, e) == max(cnt)
print("P732 OK")

em({
 "num": 732, "title": "我的日程安排表 III",
 "desc": "差分 + 掃描線：開始 +1、結束 −1，依時間累加時的最大值就是最大重疊數；進階用動態開點線段樹做到 O(log C)。",
 "zh": [
   "當 k 個事件有非空的共同時間時，稱為 <strong>k 重預訂</strong>。",
   "實作 <code>book(startTime, endTime)</code>：預訂 <code>[startTime, endTime)</code>（一定成功），並回傳目前所有事件中最大的 k。",
 ],
 "idea": [
   ("c", """【差分（掃描線）】
    每個事件：開始時間 +1、結束時間 -1。
    依時間順序累加，得到每個時刻同時進行的事件數，
    最大值就是答案。

    每次 book 都重新掃描：O(n)，總共 O(n²)，n <= 400 時很快。

【線段樹：O(log C)】
    時間範圍到 10⁹，用動態開點線段樹：
    區間 +1（懶標記）、查詢整體最大值（根節點）。"""),
 ],
 "approaches": [
   ap("解法一", "差分 + 掃描線", [("c", S["p732"]), "驗證方式：在整數座標上和計數陣列模擬比對 400 組。"], "book：O(n)", "O(n)"),
   ap("解法二", "動態開點線段樹", [("c", "節點表示 [l, r) 的區間，存 (區間最大值, 懶標記)\nbook：對 [start, end) 區間加 1，回傳根節點的最大值\n節點在第一次被走到時才建立")], "book：O(log C)", "O(n log C)", "C 為時間範圍 10⁹", "", optimal=True),
 ],
 "edges": ["<strong>相接的事件</strong> → 結束的 −1 與開始的 +1 在同一點相消，不算重疊。", "<strong>完全相同的事件</strong> → 重疊數疊加。"],
 "follow": [("h", "掃描線的應用"), ("c", "「同時有幾個」：會議室數量（第 253 題，付費）、天際線（第 218 題）、人口最多的年份（第 1854 題）。")],
 "related": ["<strong>第 729 題 我的日程安排表 I</strong>", "<strong>第 731 題 我的日程安排表 II</strong>", "<strong>第 253 題 會議室 II</strong>（付費）"],
 "check": ["相接的事件為什麼不會被算成重疊？", "線段樹解法需要支援哪兩種操作？"],
})


# ==================== 733. Flood Fill ====================
S["p733"] = '''class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old = image[sr][sc]
        if old == color:
            return image                    # ★ 顏色相同就不用填，否則會無窮迴圈
        m, n = len(image), len(image[0])
        stack = [(sr, sc)]
        while stack:
            i, j = stack.pop()
            if 0 <= i < m and 0 <= j < n and image[i][j] == old:
                image[i][j] = color
                stack += [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        return image'''

_p733 = S.load("p733")
assert _p733.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2) == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
assert _p733.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0) == [[0, 0, 0], [0, 0, 0]]
print("P733 OK")

em({
 "num": 733, "title": "圖像渲染",
 "desc": "小畫家的油漆桶：從起點出發，把所有相連且同色的格子塗成新顏色；新舊顏色相同時要直接回傳。",
 "zh": [
   "給你一張圖片 <code>image</code>（每格是顏色值）、起點 <code>(sr, sc)</code> 和新顏色 <code>color</code>。",
   "從起點開始做<strong>洪水填充</strong>：把起點以及所有透過上下左右與它相連、且<strong>顏色和起點原本相同</strong>的格子，都改成 <code>color</code>。回傳修改後的圖片。",
 ],
 "idea": [
   ("c", """【DFS / BFS】
    從起點出發，往四個方向擴散，
    只走「顏色等於原本顏色」的格子，走過就塗成新顏色。
    塗色本身就是「已拜訪」的標記。

【陷阱：新舊顏色相同】
    塗完顏色還是 old，標記失效 -> 無窮迴圈。
    直接回傳原圖。"""),
 ],
 "approaches": [
   ap("解法", "DFS（顯式堆疊）", [("c", S["p733"])], "O(mn)", "O(mn)", optimal=True),
 ],
 "edges": ["<strong>新舊顏色相同</strong> → 直接回傳。", "<strong>斜對角不相連</strong>。"],
 "follow": [("h", "油漆桶工具"), ("c", "圖片編輯軟體的油漆桶就是這個演算法；實際上常用「掃描線填充」：一次填滿一整段水平線，再往上下兩行找新的起點，減少堆疊操作。")],
 "related": ["<strong>第 200 題 島嶼數量</strong>", "<strong>第 529 題 踩地雷遊戲</strong>", "<strong>第 695 題 島嶼的最大面積</strong>"],
 "check": ["新舊顏色相同時為什麼會出問題？"],
})


# ==================== 735. Asteroid Collision ====================
S["p735"] = '''class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for a in asteroids:
            alive = True
            # ★ 只有「堆疊頂端往右、新的往左」才會相撞
            while alive and a < 0 and st and st[-1] > 0:
                if st[-1] < -a:
                    st.pop()            # 頂端比較小：爆炸，新的繼續往左撞
                elif st[-1] == -a:
                    st.pop()            # 一樣大：一起爆炸
                    alive = False
                else:
                    alive = False       # 頂端比較大：新的爆炸
            if alive:
                st.append(a)
        return st'''

_p735 = S.load("p735")
def _sim735(a):
    a = a[:]
    changed = True
    while changed:
        changed = False
        for i in range(len(a) - 1):
            if a[i] > 0 and a[i + 1] < 0:
                x, y = a[i], -a[i + 1]
                if x > y: a.pop(i + 1)
                elif x < y: a.pop(i)
                else: a.pop(i); a.pop(i)
                changed = True; break
    return a
for _ in range(3000):
    a = [random.choice([-1, 1]) * random.randint(1, 4) for _ in range(random.randint(1, 8))]
    assert _p735.asteroidCollision(a) == _sim735(a)
print("P735 OK")

em({
 "num": 735, "title": "小行星碰撞",
 "desc": "堆疊模擬：只有「堆疊頂端往右、新來的往左」才會相撞，小的爆炸、一樣大一起爆炸。",
 "zh": [
   "給你一排小行星 <code>asteroids</code>：絕對值是大小，正負號是方向（正往右、負往左），所有小行星速度相同。",
   "兩顆相遇時，較小的爆炸；一樣大則兩顆都爆炸。同方向的永遠不會相遇。回傳所有碰撞結束後剩下的小行星。",
 ],
 "idea": [
   ("c", """【誰會相撞？】
    只有「左邊往右、右邊往左」的一對會相遇。
    往左的在左邊、往右的在右邊 -> 越離越遠。

【堆疊】
    由左到右處理，堆疊存目前存活、彼此不會再相撞的小行星。
    新的 a：
        a 往右，或堆疊頂端往左 -> 不會撞，直接推入
        a 往左、頂端往右 -> 撞：
            頂端小 -> 頂端爆炸，a 繼續和新的頂端比
            一樣大 -> 都爆炸
            頂端大 -> a 爆炸

    每顆小行星最多進出堆疊一次 -> O(n)。"""),
 ],
 "approaches": [
   ap("解法", "堆疊模擬", [("c", S["p735"]), "驗證方式：和「反覆找第一對相撞的小行星處理」的模擬比對 3000 組。"], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>[-2, 2]</strong> → 不相撞。", "<strong>一樣大</strong> → 兩顆都消失。", "<strong>大的往左一路撞過去</strong> → 連續彈出。"],
 "follow": [("h", "堆疊與「抵消」"), ("c", "括號配對（第 20 題）、刪除相鄰重複（第 1047 題）、本題都是「新元素和堆疊頂端互相抵消」的模式。")],
 "related": ["<strong>第 20 題 有效的括號</strong>", "<strong>第 1047 題 刪除字串中的所有相鄰重複項</strong>", "<strong>第 2211 題 統計道路上的碰撞次數</strong>"],
 "check": ["哪一種方向組合才會相撞？", "為什麼總時間是 O(n)？"],
})


# ==================== 736. Parse Lisp Expression ====================
S["p736"] = '''class Solution:
    def evaluate(self, expression: str) -> int:
        tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
        pos = 0

        def parse(scope):                       # scope：變數名 -> 值（每個 let 建立新的一層）
            nonlocal pos
            t = tokens[pos]
            pos += 1
            if t != "(":
                if t[0] == "-" or t.isdigit():
                    return int(t)
                return scope[t]                 # 變數：查目前的作用域
            op = tokens[pos]
            pos += 1
            if op == "let":
                scope = dict(scope)             # ★ 內層作用域：複製一份，不影響外層
                while True:
                    if tokens[pos] == "(" or tokens[pos + 1] == ")":
                        val = parse(scope)      # 最後一個運算式：let 的值
                        break
                    name = tokens[pos]
                    pos += 1
                    scope[name] = parse(scope)  # 依序賦值，後面的可以用前面的
            else:
                a = parse(scope)
                b = parse(scope)
                val = a + b if op == "add" else a * b
            pos += 1                            # 跳過 ')'
            return val

        return parse({})'''

_p736 = S.load("p736")
cases = [("(let x 2 (mult x (let x 3 y 4 (add x y))))", 14), ("(let x 3 x 2 x)", 2), ("(let x 1 y 2 x (add x y) (add x y))", 5),
         ("(let x 2 (add (let x 3 (let x 4 x)) x))", 6), ("(let a1 3 b2 (add a1 1) b2)", 4), ("(add 1 2)", 3), ("(mult 3 (add 2 3))", 15),
         ("(let x -2 y x y)", -2), ("-7", -7)]
for e, want in cases:
    assert _p736.evaluate(e) == want, e
print("P736 OK")

em({
 "num": 736, "title": "Lisp 語法解析",
 "desc": "遞迴下降解析：每個 let 建立新的作用域（複製外層的變數表），依序賦值後回傳最後一個運算式的值。",
 "zh": [
   "給你一個類 Lisp 的運算式字串，回傳它的整數值。運算式有以下幾種：",
   ("ul", [
     "整數（可能為負）或變數名稱（變數的值是<strong>最內層</strong>作用域中的值）。",
     "<code>(add e1 e2)</code>：e1 + e2。<code>(mult e1 e2)</code>：e1 × e2。",
     "<code>(let v1 e1 v2 e2 ... vn en expr)</code>：依序把 v1 設為 e1 的值、v2 設為 e2 的值……（後面的可以用到前面剛設定的），最後回傳 expr 的值。",
     "每個 let 會建立新的作用域；離開 let 後，裡面的賦值不影響外面。",
   ]),
 ],
 "idea": [
   ("c", """【遞迴下降】
    parse() 讀一個運算式：
        數字 -> 回傳
        變數 -> 查作用域
        "(" -> 看運算子：
            add / mult：遞迴讀兩個運算式
            let：一對一對讀 (變數, 運算式)，最後一個單獨的運算式是回傳值

【let 怎麼判斷「最後一個」？】
    下一個 token 是 "("（一定是運算式），
    或下一個的下一個是 ")"（剩下一個 token 就是最後的值），
    就是最後的 expr。

【作用域】
    進入 let 時複製外層的變數表；
    內層的修改不影響外層 —— 函式返回後自然回到外層的表。
    （更省的做法：用一個 dict 加上「變更紀錄」堆疊，離開時還原。）"""),
 ],
 "approaches": [
   ap("解法", "遞迴下降 + 作用域複製", [("c", S["p736"]), "驗證方式：題目範例，加上巢狀作用域遮蔽、同一個 let 中重複賦值、負數等案例。"], "O(n²)", "O(n²)", "最壞每層 let 都複製整個變數表", "", optimal=True),
 ],
 "edges": ["<strong>同一個 let 重複賦值</strong>（let x 3 x 2 x）→ 2。", "<strong>內層遮蔽外層</strong> → 離開後恢復外層的值。", "<strong>負數</strong> → 以 '-' 開頭的是數字。"],
 "follow": [("h", "直譯器的雛形"), ("c", "這就是一個極小的直譯器：詞法分析（切 token）、語法分析（遞迴下降）、環境（作用域鏈）。SICP 的 metacircular evaluator 就是從這裡出發。")],
 "related": ["<strong>第 224 題 基本計算機</strong>", "<strong>第 726 題 原子的數量</strong>", "<strong>第 770 題 基本計算機 IV</strong>"],
 "check": ["let 怎麼判斷哪一個是最後的回傳運算式？", "為什麼進入 let 時要複製作用域？"],
})


# ==================== 738. Monotone Increasing Digits ====================
S["p738"] = '''class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        d = list(str(n))
        mark = len(d)                       # 從 mark 開始之後全部改成 9
        for i in range(len(d) - 1, 0, -1):
            if d[i - 1] > d[i]:
                d[i - 1] = str(int(d[i - 1]) - 1)   # ★ 前一位減 1，後面全部可以變成最大的 9
                mark = i
        for i in range(mark, len(d)):
            d[i] = "9"
        return int("".join(d))'''

_p738 = S.load("p738")
_mono = [x for x in range(0, 20001) if list(str(x)) == sorted(str(x))]
for n in range(0, 20001, 3):
    assert _p738.monotoneIncreasingDigits(n) == _mono[bisect.bisect_right(_mono, n) - 1]
assert _p738.monotoneIncreasingDigits(332) == 299 and _p738.monotoneIncreasingDigits(1234) == 1234
print("P738 OK")

em({
 "num": 738, "title": "單調遞增的數字",
 "desc": "從右往左掃：遇到前一位比後一位大，就把前一位減 1，並記下從這裡之後全部改成 9。",
 "zh": ["當一個整數的每一位都<strong>大於或等於</strong>前一位時，稱它為單調遞增。給你非負整數 <code>n</code>，回傳 ≤ n 的最大單調遞增整數。"],
 "idea": [
   ("c", """【例：332】
    3 3 2：最後兩位 3 > 2，違反。
    要變小又要盡量大：把 3 減成 2，後面全部變 9 -> 3 2 9？
    但現在前兩位 3 > 2 又違反了 -> 繼續往左：第一位 3 減成 2 -> 2 9 9。

【從右往左掃】
    遇到 d[i-1] > d[i]：
        d[i-1] -= 1
        記錄 mark = i（從 i 開始之後全部改成 9）
    減 1 可能造成左邊新的違反，往左繼續掃就會處理到。
    最後把 mark 之後全部設成 9。

【為什麼是最大的？】
    變動的最高位只減了 1，之後用最大的 9 填滿。"""),
 ],
 "approaches": [
   ap("解法", "從右往左貪心", [("c", S["p738"]), "驗證方式：0～20000（每隔 3 取一個）和「≤ n 的最大單調數」查表比對。"], "O(位數)", "O(位數)", optimal=True),
 ],
 "edges": ["<strong>已經單調</strong> → 不變。", "<strong>10</strong> → 9。", "<strong>連續相同的數字後面下降</strong>（如 332）→ 減 1 要傳回最左邊。"],
 "follow": [("h", "從左往右的寫法"), ("c", "也可以從左找到第一個下降點，再往左退到那一串相同數字的開頭，把它減 1、後面全改 9。")],
 "related": ["<strong>第 670 題 最大交換</strong>", "<strong>第 402 題 移掉 K 位數字</strong>"],
 "check": ["遇到違反時為什麼要把前一位減 1？", "332 的處理過程是什麼？"],
})


# ==================== 739. Daily Temperatures ====================
S["p739"] = '''class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []                                 # 還沒等到更暖日子的「索引」，溫度由下往上遞減
        for i, t in enumerate(temperatures):
            while st and temperatures[st[-1]] < t:
                j = st.pop()
                res[j] = i - j                  # ★ 第 i 天是 j 等待的那一天，相差 i - j 天
            st.append(i)
        return res'''

_p739 = S.load("p739")
for _ in range(3000):
    a = [random.randint(30, 40) for _ in range(random.randint(1, 10))]
    want = [next((j - i for j in range(i + 1, len(a)) if a[j] > a[i]), 0) for i in range(len(a))]
    assert _p739.dailyTemperatures(a) == want
print("P739 OK")

em({
 "num": 739, "title": "每日溫度",
 "desc": "單調遞減堆疊存索引：今天比堆疊頂端那天暖，那天就等到了，答案是索引差。",
 "zh": ["給你每天的溫度 <code>temperatures</code>，回傳一個陣列：<code>answer[i]</code> 是第 i 天之後還要再等幾天才會有<strong>更暖</strong>的一天；之後都沒有則為 0。"],
 "idea": [
   ("c", """【下一個更大元素（第 496 題）的距離版】
    堆疊存「還在等更暖日子」的索引。
    今天 i 的溫度比頂端 j 那天高 -> j 等到了，答案 i - j，彈出。
    再把 i 推入。

【存索引而不是溫度】
    要算距離，而且溫度可能重複。

    每個索引進出一次 -> O(n)。"""),
 ],
 "approaches": [
   ap("解法", "單調堆疊", [("c", S["p739"])], "O(n)", "O(n)", optimal=True),
 ],
 "edges": ["<strong>相同溫度</strong> → 不算更暖（嚴格大於）。", "<strong>遞減序列</strong> → 全部 0。"],
 "follow": [("h", "從右往左、不用堆疊"), ("c", "從右往左處理，對每天 i，從 j = i+1 開始，利用已算好的 answer[j] 跳躍：若 T[j] <= T[i] 就跳到 j + answer[j]。均攤也是 O(n)，O(1) 額外空間。")],
 "related": ["<strong>第 496 題 下一個更大元素 I</strong>", "<strong>第 503 題 下一個更大元素 II</strong>", "<strong>第 901 題 股票價格跨度</strong>"],
 "check": ["堆疊裡存的是什麼？為什麼存索引？", "什麼時候一個索引會被彈出？"],
})


# ==================== 740. Delete and Earn ====================
S["p740"] = '''class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        pts = Counter()
        for x in nums:
            pts[x] += x                         # 選了 x，就把所有 x 都拿走：總共得 x × 次數
        take = skip = 0                         # 處理到 v 時：拿了 v / 沒拿 v 的最大得分
        prev = None
        for v in sorted(pts):
            if prev is not None and v == prev + 1:
                # ★ 相鄰的值不能同時拿：就是打家劫舍
                take, skip = skip + pts[v], max(take, skip)
            else:
                take, skip = max(take, skip) + pts[v], max(take, skip)
            prev = v
        return max(take, skip)'''

_p740 = S.load("p740")
assert _p740.deleteAndEarn([3, 4, 2]) == 6 and _p740.deleteAndEarn([2, 2, 3, 3, 3, 4]) == 9
def _bf740(nums):
    vals = sorted(set(nums)); best = 0
    for mask in range(1 << len(vals)):
        ch = [vals[i] for i in range(len(vals)) if mask >> i & 1]
        if all(b - a != 1 for a, b in zip(ch, ch[1:])):
            best = max(best, sum(x for x in nums if x in ch))
    return best
for _ in range(1500):
    a = [random.randint(1, 8) for _ in range(random.randint(1, 9))]
    assert _p740.deleteAndEarn(a) == _bf740(a)
print("P740 OK")

em({
 "num": 740, "title": "刪除並獲得點數",
 "desc": "選了 x 就會失去 x−1 和 x+1：把每個值的總點數排在數線上，就變成「打家劫舍」——相鄰的不能同時拿。",
 "zh": [
   "給你整數陣列 <code>nums</code>。每次操作選一個 <code>nums[i]</code>，得到 <code>nums[i]</code> 點，並刪除它；同時必須刪除<strong>所有</strong>等於 <code>nums[i] − 1</code> 和 <code>nums[i] + 1</code> 的元素（不得分）。",
   "回傳能獲得的最大點數。",
 ],
 "idea": [
   ("c", """【一旦選了值 x，就把所有 x 都拿走】
    剩下的 x 不會被刪（只有 x±1 的操作會刪 x），
    所以選 x 一次就應該拿光：得到 x × count(x)。

【變成打家劫舍（第 198 題）】
    把值 1, 2, 3, ... 排成一排房子，房子 x 的錢 = x × count(x)。
    拿了 x 就不能拿 x-1 和 x+1 = 相鄰的房子不能同時偷。

【值不連續時】
    v 和前一個值不相鄰 -> 沒有衝突，可以直接加。
    （或直接開長度為最大值的陣列，不存在的值點數為 0。）"""),
 ],
 "approaches": [
   ap("解法", "轉成打家劫舍", [("c", S["p740"]), "驗證方式：和枚舉所有「不含相鄰值」的值集合的暴力法比對 1500 組。"], "O(n log n)", "O(n)", "", "", optimal=True),
 ],
 "edges": ["<strong>值不連續</strong>（如 [1, 5]）→ 都可以拿。", "<strong>大量重複</strong> → 一次拿光。"],
 "follow": [("h", "轉化的力量"), ("c", "很多題目轉成已知問題後就變簡單了：本題 → 打家劫舍；第 494 題（目標和）→ 子集和背包；第 1049 題（最後一塊石頭的重量 II）→ 分割等和子集。")],
 "related": ["<strong>第 198 題 打家劫舍</strong>", "<strong>第 213 題 打家劫舍 II</strong>", "<strong>第 337 題 打家劫舍 III</strong>"],
 "check": ["為什麼選了 x 就應該把所有 x 都拿走？", "怎麼把本題轉成打家劫舍？"],
})


# ==================== 741. Cherry Pickup ====================
S["p741"] = '''class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        NEG = float("-inf")
        # ★ 來回一趟 = 兩個人同時從 (0,0) 走到 (n-1,n-1)；走了 k 步時，兩人的列分別是 r1、r2
        dp = [[NEG] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        for k in range(1, 2 * n - 1):
            nd = [[NEG] * n for _ in range(n)]
            for r1 in range(max(0, k - n + 1), min(n, k + 1)):
                c1 = k - r1
                if grid[r1][c1] < 0:
                    continue
                for r2 in range(r1, min(n, k + 1)):     # 對稱：只算 r1 <= r2
                    c2 = k - r2
                    if grid[r2][c2] < 0:
                        continue
                    # 兩人上一步各自來自上方或左方：4 種組合（用對稱只查 dp[小][大]）
                    best = max(dp[min(a, b)][max(a, b)] for a in (r1 - 1, r1) for b in (r2 - 1, r2)
                               if a >= 0 and b >= 0)
                    if best == NEG:
                        continue
                    gain = grid[r1][c1] + (grid[r2][c2] if r1 != r2 else 0)   # 同一格只摘一次
                    nd[r1][r2] = best + gain
            dp = nd
        return max(dp[n - 1][n - 1], 0)'''

_p741 = S.load("p741")
assert _p741.cherryPickup([[0, 1, -1], [1, 0, -1], [1, 1, 1]]) == 5
assert _p741.cherryPickup([[1, 1, -1], [1, -1, 1], [-1, 1, 1]]) == 0
def _bf741(g):
    n = len(g)
    paths = []
    def go(i, j, path):
        if g[i][j] < 0: return
        path = path + [(i, j)]
        if (i, j) == (n - 1, n - 1): paths.append(path); return
        if i + 1 < n: go(i + 1, j, path)
        if j + 1 < n: go(i, j + 1, path)
    go(0, 0, [])
    best = 0
    for p in paths:
        for q in paths:
            best = max(best, sum(g[i][j] for i, j in set(p) | set(q)))
    return best
for _ in range(400):
    n = random.randint(1, 4)
    g = [[random.choice([0, 1, 1, -1]) for _ in range(n)] for _ in range(n)]
    g[0][0] = random.choice([0, 1]); g[n - 1][n - 1] = random.choice([0, 1])
    assert _p741.cherryPickup(g) == _bf741(g), g
print("P741 OK")

em({
 "num": 741, "title": "摘櫻桃",
 "desc": "去程加回程 = 兩個人同時從起點走到終點；以步數 k 為階段、兩人的列 (r1, r2) 為狀態，同一格只算一次。",
 "zh": [
   "給你一個 <code>n x n</code> 的格子：<code>0</code> 是空地、<code>1</code> 是櫻桃、<code>-1</code> 是荊棘（不能通過）。",
   "從 <code>(0, 0)</code> 出發，只能往右或往下走到 <code>(n−1, n−1)</code>；再只能往左或往上走回 <code>(0, 0)</code>。經過有櫻桃的格子就摘下（之後那格變成空地）。",
   "回傳能摘到的<strong>最多</strong>櫻桃數；若無法到達終點則回傳 0。",
 ],
 "idea": [
   ("c", """【為什麼不能「先走一趟最好的，再走一趟最好的」？】
    兩次各自貪心，第一趟的選擇可能讓第二趟拿得很少，
    整體不是最優。

【轉換：兩個人同時出發】
    回程反過來看也是「從 (0,0) 往右/下走到終點」。
    所以等價於兩個人同時從起點走到終點，
    經過同一格時櫻桃只算一次。

【同步走】
    兩人每次都走一步 -> 走了 k 步時，r + c = k。
    狀態 (k, r1, r2) 就能決定兩人的位置 (r1, k-r1)、(r2, k-r2)。
    兩人在同一格 <=> r1 == r2（同一步數下）。

【轉移】
    每個人上一步可能來自上方或左方 -> 4 種組合取最大。
    遇到荊棘就是不合法（-∞）。

【對稱】
    兩人互換結果相同，只算 r1 <= r2 減半。"""),
 ],
 "approaches": [
   ap("解法", "兩人同步走的三維 DP", [
     ("c", S["p741"]),
     "驗證方式：在 n ≤ 4 的隨機格子上，和「枚舉所有去程、回程路徑組合」的暴力法比對 400 組。",
   ], "O(n³)", "O(n²)", optimal=True),
 ],
 "edges": ["<strong>無法到達終點</strong> → 0。", "<strong>兩人走到同一格</strong> → 櫻桃只算一次。", "<strong>n = 1</strong> → grid[0][0]。"],
 "follow": [("h", "相關"), ("c", "第 1463 題（摘櫻桃 II）：兩個機器人從上方兩角同時往下走，也是「兩人同步」的 DP，狀態是 (列, 兩人的欄)。")],
 "related": ["<strong>第 1463 題 摘櫻桃 II</strong>", "<strong>第 64 題 最小路徑和</strong>", "<strong>第 174 題 地下城遊戲</strong>"],
 "check": ["為什麼兩次貪心不正確？", "為什麼可以把回程看成第二個人的去程？", "狀態中為什麼只需要兩人的列？"],
})
