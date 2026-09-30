# -*- coding: utf-8 -*-
"""第 388、389、390、391、392、393 題。"""
import random
from collections import Counter
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(388)


# ==================== 388. Longest Absolute File Path ====================
S["p388"] = '''class Solution:
    def lengthLongestPath(self, input: str) -> int:
        depth_len = {0: 0}           # depth_len[d]：深度 d 的「父目錄路徑」長度（含結尾的 /）
        best = 0
        for line in input.split("\\n"):
            name = line.lstrip("\\t")
            depth = len(line) - len(name)          # 前面有幾個 \\t = 深度
            if "." in name:                        # 檔案：計算完整路徑長度
                best = max(best, depth_len[depth] + len(name))
            else:                                  # ★ 目錄：記錄下一層的前綴長度（覆蓋同深度的舊值）
                depth_len[depth + 1] = depth_len[depth] + len(name) + 1
        return best'''

_p388 = S.load("p388")


def _lp_ref(inp):
    stack, best = [], 0
    for line in inp.split("\n"):
        name = line.lstrip("\t")
        d = len(line) - len(name)
        stack = stack[:d] + [name]
        if "." in name:
            best = max(best, len("/".join(stack)))
    return best


for inp, want in [("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext", 20),
                  ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext", 32),
                  ("a", 0), ("file1.txt\nfile2.txt\nlongfile.txt", 12)]:
    assert _p388.lengthLongestPath(inp) == want


def _rtree(d=0):
    lines = []
    for _ in range(random.randrange(1, 4)):
        if d < 3 and random.random() < 0.5:
            lines.append("\t" * d + random.choice(["a", "dir", "xy"]))
            lines += _rtree(d + 1)
        else:
            lines.append("\t" * d + random.choice(["f.t", "long.ext", "q.p"]))
    return lines


for _ in range(2000):
    inp = "\n".join(_rtree())
    assert _p388.lengthLongestPath(inp) == _lp_ref(inp), inp
print("P388 OK")

emit({
 "num": 388, "slug": "longest-absolute-file-path",
 "en": [
   "Suppose we have a file system that stores both files and directories. The file system is represented as a string where <code>'\\n'</code> separates entries and the number of <code>'\\t'</code> characters before a name indicates its depth. For example:",
   ("c", "dir\n    subdir1\n        file1.ext\n        subsubdir1\n    subdir2\n        subsubdir2\n            file2.ext"),
   "Every file and directory has a unique <strong>absolute path</strong> in the file system, which is the order of directories that must be opened to reach the file/directory itself, all concatenated by <code>'/'s</code>. "
   "In the example above, the absolute path to <code>file2.ext</code> is <code>\"dir/subdir2/subsubdir2/file2.ext\"</code>. Each directory name consists of letters, digits, and/or spaces. "
   "Each file name is of the form <code>name.extension</code>, where <code>name</code> and <code>extension</code> consist of letters, digits, and/or spaces.",
   "Given a string <code>input</code> representing the file system in the explained format, return <em>the length of the <strong>longest absolute path</strong> to a <strong>file</strong> in the abstracted file system</em>. If there is no file in the system, return <code>0</code>.",
 ],
 "zh": [
   "一個檔案系統用字串表示：<code>'\\n'</code> 分隔每一項，名稱前面 <code>'\\t'</code> 的個數代表它的深度。",
   "每個檔案或目錄都有唯一的<strong>絕對路徑</strong>：從根開始經過的目錄名稱用 <code>'/'</code> 串起來。例如上面 <code>file2.ext</code> 的絕對路徑是 <code>\"dir/subdir2/subsubdir2/file2.ext\"</code>。",
   "檔案名稱的格式是 <code>name.extension</code>（有 <code>.</code>）；目錄名稱沒有 <code>.</code>。",
   "回傳<strong>檔案</strong>最長的絕對路徑長度；沒有任何檔案時回傳 <code>0</code>。",
 ],
 "examples": """範例 1
  輸入：input = "dir\\n\\tsubdir1\\n\\tsubdir2\\n\\t\\tfile.ext"
  輸出：20
  說明："dir/subdir2/file.ext" 長度 20。

範例 2
  輸入：input = "dir\\n\\tsubdir1\\n\\t\\tfile1.ext\\n\\t\\tsubsubdir1\\n\\tsubdir2\\n\\t\\tsubsubdir2\\n\\t\\t\\tfile2.ext"
  輸出：32
  說明："dir/subdir2/subsubdir2/file2.ext" 長度 32。

範例 3
  輸入：input = "a"
  輸出：0
  說明：沒有檔案。""",
 "constraints": [
   "1 ≤ <code>input.length</code> ≤ 10⁴",
   "<code>input</code> 可能包含英文字母、數字、<code>'\\n'</code>、<code>'\\t'</code>、<code>'.'</code>、空白",
   "所有檔案和目錄名稱的長度都是正數",
 ],
 "idea": [
   ("c", """【一行一行讀：深度 = 開頭的 \\t 個數】
    讀到深度 d 的項目時，它的父目錄一定是「最近一個深度 d-1 的目錄」。
    這正是堆疊的性質：深度變淺時，比它深的目錄都已經結束了。

【只需要記住每個深度的「路徑前綴長度」】
    depth_len[d] = 深度 d 的項目，前面的路徑長度（例如 "dir/subdir2/" 是 12）
    目錄：depth_len[d + 1] = depth_len[d] + len(名稱) + 1（加上 '/'）
    檔案：候選答案 = depth_len[d] + len(名稱)

    同一個深度的新目錄會直接覆蓋舊值 ——
    舊的那個目錄已經結束了，它底下不會再有東西。

【判斷檔案】
    名稱中有 '.' 就是檔案。"""),
   ("t", ["行", "深度", "類型", "depth_len 更新", "候選"],
    [["dir", "0", "目錄", "[1] = 4（\"dir/\"）", ""],
     ["\\tsubdir1", "1", "目錄", "[2] = 12", ""],
     ["\\tsubdir2", "1", "目錄", "[2] = 12（覆蓋）", ""],
     ["\\t\\tfile.ext", "2", "檔案", "", "12 + 8 = 20"]]),
 ],
 "approaches": [
   ap("解法", "逐行 + 每個深度的前綴長度", [
     ("c", S["p388"]),
   ], "O(n)", "O(d)", "", "d = 最大深度", optimal=True),
 ],
 "edges": [
   "<strong>沒有檔案</strong> → 0。",
   "<strong>檔案在根目錄</strong>（深度 0）→ 路徑就是檔名本身。",
   "<strong>名稱包含空白</strong> → 空白算長度，不影響判斷。",
   "<strong>深度變淺</strong> → 用覆蓋的方式自動「彈出」舊目錄。",
 ],
 "follow": [
   ("h", "相關題"),
   ("c", "第 71 題「簡化路徑」：用堆疊處理 '..' 和 '.'；第 588 題（付費）設計記憶體檔案系統。"),
 ],
 "related": [
   "<strong>第 71 題 簡化路徑</strong>",
   "<strong>第 609 題 在系統中查找重複檔案</strong>",
 ],
 "check": [
   "怎麼從一行字判斷它的深度？",
   "depth_len[d] 代表什麼？",
   "為什麼同深度的新目錄可以直接覆蓋舊值？",
 ],
})


# ==================== 389. Find the Difference ====================
S["p389"] = '''class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        x = 0
        for ch in s + t:                       # ★ 成對的字元 XOR 後抵銷，只剩多出來的那個
            x ^= ord(ch)
        return chr(x)'''

S["p389_sum"] = '''class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))   # 字元碼總和的差'''

S["p389_counter"] = '''class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return next(iter(collections.Counter(t) - collections.Counter(s)))'''

_p389 = [S.load(x) for x in ("p389", "p389_sum", "p389_counter")]
for _ in range(3000):
    s = "".join(random.choice("abcz") for _ in range(random.randrange(0, 8)))
    c = random.choice("abcz")
    t = list(s + c)
    random.shuffle(t)
    t = "".join(t)
    for sol in _p389:
        assert sol.findTheDifference(s, t) == c
print("P389 OK")

emit({
 "num": 389, "slug": "find-the-difference",
 "en": [
   "You are given two strings <code>s</code> and <code>t</code>.",
   "String <code>t</code> is generated by random shuffling string <code>s</code> and then add one more letter at a random position.",
   "Return the letter that was added to <code>t</code>.",
 ],
 "zh": [
   "給你兩個字串 <code>s</code> 和 <code>t</code>。<code>t</code> 是把 <code>s</code> 隨機打亂後，再在隨機位置多加一個字母得到的。",
   "回傳多加的那個字母。",
 ],
 "examples": """範例 1
  輸入：s = "abcd", t = "abcde"
  輸出："e"

範例 2
  輸入：s = "", t = "y"
  輸出："y\"""",
 "constraints": [
   "0 ≤ <code>s.length</code> ≤ 1000",
   "<code>t.length == s.length + 1</code>",
   "只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【三種想法，都是「抵銷」】
    計數：t 的計數 - s 的計數，剩下的那個。
    求和：t 所有字元碼的和 - s 所有字元碼的和 = 多出來的字元碼。
    XOR：把 s 和 t 所有字元碼全部 XOR，
         成對的 x ^ x = 0 抵銷，只剩多出來的那一個
         （第 136 題「只出現一次的數字」的同一招）。"""),
 ],
 "approaches": [
   ap("解法一", "計數", [
     ("c", S["p389_counter"]),
   ], "O(n)", "O(1)", "", "最多 26 種"),

   ap("解法二", "字元碼求和", [
     ("c", S["p389_sum"]),
   ], "O(n)", "O(1)", "", ""),

   ap("解法三", "XOR", [
     ("c", S["p389"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、計數", "O(n)", "O(1)"],
    ["二、求和", "O(n)", "O(1)"],
    ["三、XOR", "O(n)", "O(1) ✔"]]),
 "edges": [
   "<strong>s 是空字串</strong> → t 就是答案。",
   "<strong>多出來的字母和已有的重複</strong> → 計數、求和、XOR 都照樣正確。",
 ],
 "follow": [
   ("h", "XOR 抵銷家族"),
   ("c", "第 136 題、第 268 題、第 389 題：「成對出現、只有一個落單」→ 全部 XOR。"),
 ],
 "related": [
   "<strong>第 136 題 只出現一次的數字</strong>",
   "<strong>第 268 題 遺失的數字</strong>",
 ],
 "check": [
   "為什麼 XOR 可以找出多出來的字元？",
   "如果多加的字母和原本的某個字母相同，哪些方法還正確？",
 ],
})


# ==================== 390. Elimination Game ====================
S["p390"] = '''class Solution:
    def lastRemaining(self, n: int) -> int:
        head, step, remaining = 1, 1, n     # 剩下的數是等差數列：head, head+step, ...
        left_to_right = True
        while remaining > 1:
            # ★ 從左邊開始刪、或從右邊刪但剩奇數個 -> 開頭會被刪掉
            if left_to_right or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right
        return head'''

S["p390_sim"] = '''class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = list(range(1, n + 1))            # 直接模擬（n 大時太慢）
        left = True
        while len(arr) > 1:
            arr = arr[1::2] if left else arr[::-1][1::2][::-1]
            left = not left
        return arr[0]'''

_p390 = [S.load(x) for x in ("p390", "p390_sim")]
for n in range(1, 600):
    assert _p390[0].lastRemaining(n) == _p390[1].lastRemaining(n), n
assert _p390[0].lastRemaining(9) == 6
print("P390 OK")

emit({
 "num": 390, "slug": "elimination-game",
 "en": [
   "You have a list <code>arr</code> of all integers in the range <code>[1, n]</code> sorted in a strictly increasing order. Apply the following algorithm on <code>arr</code>:",
   ("ul", ["Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.",
           "Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.",
           "Keep repeating the steps again, alternating left to right and right to left, until a single number remains."]),
   "Given the integer <code>n</code>, return <em>the last number that remains in</em> <code>arr</code>.",
 ],
 "zh": [
   "有一個陣列 <code>arr</code>，包含 <code>1</code> 到 <code>n</code> 的所有整數（遞增）。重複以下步驟：",
   ("ul", ["從左到右：刪掉第一個數，然後每隔一個刪一個，直到結尾。",
           "從右到左：刪掉最右邊的數，然後每隔一個刪一個。",
           "左右交替，直到只剩一個數。"]),
   "回傳最後剩下的數。",
 ],
 "examples": """範例 1
  輸入：n = 9
  輸出：6
  說明：
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    arr = [2, 4, 6, 8]       （從左刪）
    arr = [2, 6]             （從右刪）
    arr = [6]                （從左刪）

範例 2
  輸入：n = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 10⁹",
 ],
 "idea": [
   ("c", """【剩下的數永遠是一個等差數列】
    只要記住：開頭 head、公差 step、個數 remaining。
    每一輪：
        個數減半（remaining //= 2）
        公差加倍（step *= 2）
        開頭可能改變

【開頭什麼時候會被刪掉？】
    從左邊刪：第一個一定被刪 -> head += step
    從右邊刪：
        剩奇數個 -> 從右邊隔一個刪，會一路刪到最左邊那個 -> head += step
        剩偶數個 -> 最左邊的留下來 -> head 不變

【範例 n = 9】
    head=1, step=1, remaining=9, 從左   -> head=2, step=2, rem=4
    從右，rem=4 是偶數                   -> head=2, step=4, rem=2
    從左                                 -> head=6, step=8, rem=1
    答案 6 ✔

【複雜度】每輪個數減半 -> O(log n)。"""),
 ],
 "approaches": [
   ap("解法一", "直接模擬", [
     ("c", S["p390_sim"]),
     "n = 10⁹ 時陣列太大，只能用來驗證。",
   ], "O(n)", "O(n)", "", ""),

   ap("解法二", "只追蹤等差數列的開頭", [
     ("c", S["p390"]),
   ], "O(log n)", "O(1)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、模擬", "O(n)", "O(n)"],
    ["二、追蹤開頭", "O(log n)", "O(1) ✔"]]),
 "edges": [
   "<strong>n = 1</strong> → 1。",
   "<strong>從右邊刪、個數是偶數</strong> → 開頭不變。",
 ],
 "follow": [
   ("h", "約瑟夫問題"),
   ("c", "第 1823 題「找出遊戲的獲勝者」是約瑟夫問題：n 個人圍成圈每數 k 個淘汰一個，f(n) = (f(n−1) + k) mod n。同樣是「每輪規模變小，只追蹤關鍵位置」。"),
 ],
 "related": [
   "<strong>第 1823 題 找出遊戲的獲勝者</strong>",
   "<strong>第 2211 題 統計道路上的碰撞次數</strong>",
 ],
 "check": [
   "為什麼剩下的數永遠是等差數列？",
   "什麼情況下開頭的數會被刪掉？",
 ],
})


# ==================== 391. Perfect Rectangle ====================
S["p391"] = '''class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        area = 0
        corners = set()
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            for p in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                corners ^= {p}                 # ★ 出現偶數次的角抵銷（對稱差）
        X1 = min(r[0] for r in rectangles)
        Y1 = min(r[1] for r in rectangles)
        X2 = max(r[2] for r in rectangles)
        Y2 = max(r[3] for r in rectangles)
        # 條件 1：面積總和 = 外框面積
        # 條件 2：只出現奇數次的角，剛好是外框的四個角
        return (area == (X2 - X1) * (Y2 - Y1)
                and corners == {(X1, Y1), (X1, Y2), (X2, Y1), (X2, Y2)})'''

_p391 = S.load("p391")


def _cover_ref(rects):
    cells = Counter()
    for x1, y1, x2, y2 in rects:
        for x in range(x1, x2):
            for y in range(y1, y2):
                cells[(x, y)] += 1
    X1 = min(r[0] for r in rects); Y1 = min(r[1] for r in rects)
    X2 = max(r[2] for r in rects); Y2 = max(r[3] for r in rects)
    return all(cells[(x, y)] == 1 for x in range(X1, X2) for y in range(Y1, Y2)) and sum(cells.values()) == (X2 - X1) * (Y2 - Y1)


def _split(x1, y1, x2, y2, depth):
    if depth == 0 or (x2 - x1 < 2 and y2 - y1 < 2) or random.random() < 0.25:
        return [[x1, y1, x2, y2]]
    if x2 - x1 >= 2 and (y2 - y1 < 2 or random.random() < 0.5):
        m = random.randint(x1 + 1, x2 - 1)
        return _split(x1, y1, m, y2, depth - 1) + _split(m, y1, x2, y2, depth - 1)
    m = random.randint(y1 + 1, y2 - 1)
    return _split(x1, y1, x2, m, depth - 1) + _split(x1, m, x2, y2, depth - 1)


for rects, want in [([[1, 1, 3, 3], [3, 1, 4, 2], [3, 2, 4, 4], [1, 3, 2, 4], [2, 3, 3, 4]], True),
                    ([[1, 1, 2, 3], [1, 3, 2, 4], [3, 1, 4, 2], [3, 2, 4, 4]], False),
                    ([[1, 1, 3, 3], [3, 1, 4, 2], [1, 3, 2, 4], [2, 2, 4, 4]], False)]:
    assert _p391.isRectangleCover(rects) == want
for _ in range(3000):
    rects = _split(0, 0, random.randint(1, 5), random.randint(1, 5), 4)
    r = random.random()
    if r < 0.3 and len(rects) > 1:
        rects.pop(random.randrange(len(rects)))            # 挖洞
    elif r < 0.6:
        x1, y1 = random.randint(0, 4), random.randint(0, 4)
        rects.append([x1, y1, x1 + random.randint(1, 2), y1 + random.randint(1, 2)])   # 重疊或外凸
    assert _p391.isRectangleCover(rects) == _cover_ref(rects), rects
print("P391 OK")

emit({
 "num": 391, "slug": "perfect-rectangle",
 "en": [
   "Given an array <code>rectangles</code> where <code>rectangles[i] = [x<sub>i</sub>, y<sub>i</sub>, a<sub>i</sub>, b<sub>i</sub>]</code> represents an axis-aligned rectangle. "
   "The bottom-left point of the rectangle is <code>(x<sub>i</sub>, y<sub>i</sub>)</code> and the top-right point of it is <code>(a<sub>i</sub>, b<sub>i</sub>)</code>.",
   "Return <code>true</code> <em>if all the rectangles together form an exact cover of a rectangular region</em>.",
 ],
 "zh": [
   "給你一個陣列 <code>rectangles</code>，每個元素 <code>[x, y, a, b]</code> 是一個邊與座標軸平行的矩形，左下角 <code>(x, y)</code>、右上角 <code>(a, b)</code>。",
   "判斷這些矩形是否<strong>剛好</strong>拼成一個完整的大矩形——沒有重疊、也沒有空隙。",
 ],
 "examples": """範例 1
  輸入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
  輸出：true

範例 2
  輸入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
  輸出：false
  說明：中間有空隙。

範例 3
  輸入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
  輸出：false
  說明：有重疊。""",
 "constraints": [
   "1 ≤ <code>rectangles.length</code> ≤ 2 × 10⁴",
   "<code>rectangles[i].length == 4</code>",
   "−10⁵ ≤ <code>x<sub>i</sub> &lt; a<sub>i</sub></code> ≤ 10⁵",
   "−10⁵ ≤ <code>y<sub>i</sub> &lt; b<sub>i</sub></code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【兩個必要條件，合起來就充分】

【條件 1：面積】
    所有小矩形面積總和 = 外框（最小包圍矩形）面積
    只看面積不夠：一處重疊 + 一處空隙，面積可能剛好抵銷。

【條件 2：角點】
    把每個小矩形的 4 個角都丟進一個集合，出現第二次就移除（對稱差）。
    完美拼接時：
        內部的點：被 2 個或 4 個矩形共用 -> 偶數次 -> 消失
        外框的 4 個角：只屬於 1 個矩形 -> 奇數次 -> 留下
    所以最後集合裡必須「剛好是」外框的 4 個角。

【為什麼兩個條件合起來就夠？】
    有重疊時，重疊區域的角會以奇數次出現（或面積會超出），
    有空隙時，空隙的角也會以奇數次出現（或面積不足）。
    嚴格證明較長，但可以用大量隨機測試驗證（本頁就這樣做了）。"""),
 ],
 "approaches": [
   ap("解法", "面積 + 角點奇偶", [
     ("c", S["p391"]),
     "驗證方式：隨機把大矩形切成小塊、再隨機挖洞或加重疊，和「逐格計數」的暴力版本比對三千次。",
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>只有一個矩形</strong> → true。",
   "<strong>重疊 + 空隙面積剛好抵銷</strong> → 角點條件抓得到。",
   "<strong>完全重複的兩個矩形</strong> → 面積超出外框。",
 ],
 "follow": [
   ("h", "掃描線做法"),
   ("c", "另一種 O(n log n) 做法：沿 x 軸掃描，維護目前被覆蓋的 y 區間（有序集合），檢查不重疊而且涵蓋完整——比較直觀但難寫很多。"),
 ],
 "related": [
   "<strong>第 223 題 矩形面積</strong>",
   "<strong>第 850 題 矩形面積 II</strong> —— 掃描線",
 ],
 "check": [
   "只檢查面積為什麼不夠？",
   "完美拼接時，內部的角點會出現幾次？外框的角呢？",
 ],
})


# ==================== 392. Is Subsequence ====================
S["p392"] = '''class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:                         # ★ 貪心：t 中遇到 s[i] 就盡早配對
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)'''

S["p392_bs"] = '''class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 進階：大量的 s 對同一個 t 查詢 -> 預處理每個字元在 t 中出現的位置
        pos = collections.defaultdict(list)
        for i, ch in enumerate(t):
            pos[ch].append(i)
        cur = -1                             # 上一個配對到的位置
        for ch in s:
            lst = pos[ch]
            j = bisect.bisect_right(lst, cur)    # 第一個 > cur 的位置
            if j == len(lst):
                return False
            cur = lst[j]
        return True'''

_p392 = [S.load(x) for x in ("p392", "p392_bs")]


def _subseq_ref(s, t):
    it = iter(t)
    return all(c in it for c in s)


for _ in range(4000):
    s = "".join(random.choice("abc") for _ in range(random.randrange(0, 5)))
    t = "".join(random.choice("abc") for _ in range(random.randrange(0, 9)))
    want = _subseq_ref(s, t)
    for sol in _p392:
        assert sol.isSubsequence(s, t) == want, (s, t)
print("P392 OK")

emit({
 "num": 392, "slug": "is-subsequence",
 "en": [
   "Given two strings <code>s</code> and <code>t</code>, return <code>true</code> <em>if</em> <code>s</code> <em>is a <strong>subsequence</strong> of</em> <code>t</code><em>, or</em> <code>false</code> <em>otherwise</em>.",
   "A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.",
   "<strong>Follow up:</strong> Suppose there are lots of incoming <code>s</code>, say <code>s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub></code> where <code>k &gt;= 10<sup>9</sup></code>, and you want to check one by one to see if <code>t</code> has its subsequence. In this scenario, how would you change your code?",
 ],
 "zh": [
   "給你兩個字串 <code>s</code> 和 <code>t</code>，判斷 <code>s</code> 是不是 <code>t</code> 的<strong>子序列</strong>（從 <code>t</code> 刪掉一些字元、不改變剩餘字元的順序得到）。",
   "<strong>進階：</strong>如果有超過 10⁹ 個不同的 <code>s</code> 要對同一個 <code>t</code> 查詢，要怎麼改？",
 ],
 "examples": """範例 1
  輸入：s = "abc", t = "ahbgdc"
  輸出：true

範例 2
  輸入：s = "axc", t = "ahbgdc"
  輸出：false""",
 "constraints": [
   "0 ≤ <code>s.length</code> ≤ 100",
   "0 ≤ <code>t.length</code> ≤ 10⁴",
   "只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【貪心雙指標】
    掃過 t，遇到和 s[i] 相同的字元就配對，i 前進。
    最後 i 走完 s 就是子序列。

    為什麼盡早配對一定不吃虧？
    配對得越早，剩下可以用的 t 越長 —— 不會比晚配對差。

【進階：大量查詢】
    每次都掃一遍 t 要 O(|t|)。
    預處理：每個字元在 t 中出現的所有位置（遞增）。
    查詢時，對 s 的每個字元，二分找「上一個配對位置之後」的第一次出現。
    每次查詢 O(|s| log |t|)，和 t 的長度幾乎無關。

    （更快的做法：next[i][c] = t 中位置 i 之後第一個 c 的位置，
     預處理 O(26|t|)，查詢 O(|s|)。）"""),
 ],
 "approaches": [
   ap("解法一", "貪心雙指標", [
     ("c", S["p392"]),
   ], "O(|t|)", "O(1)", "", "", optimal=True),

   ap("解法二", "預處理位置 + 二分（大量查詢）", [
     ("c", S["p392_bs"]),
   ], "預處理 O(|t|)，查詢 O(|s| log |t|)", "O(|t|)", "", ""),
 ],
 "compare": (["解法", "單次查詢", "適用"],
   [["一、雙指標", "O(|t|)", "少量查詢 ✔"],
    ["二、位置 + 二分", "O(|s| log |t|)", "大量查詢"]]),
 "edges": [
   "<strong>s 是空字串</strong> → true。",
   "<strong>t 是空字串</strong> → 只有 s 也空時為 true。",
   "<strong>s 比 t 長</strong> → false。",
 ],
 "follow": [
   ("h", "子序列家族"),
   ("c", "第 792 題「匹配子序列的單字數」就是進階問題：大量單字對同一個 t。第 1143 題（最長公共子序列）則需要 DP。"),
 ],
 "related": [
   "<strong>第 792 題 匹配子序列的單字數</strong>",
   "<strong>第 1143 題 最長公共子序列</strong>",
   "<strong>第 115 題 不同的子序列</strong>",
 ],
 "check": [
   "為什麼盡早配對不會吃虧？",
   "大量查詢時要怎麼預處理？",
 ],
})


# ==================== 393. UTF-8 Validation ====================
S["p393"] = '''class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        need = 0                              # 還需要幾個「延續位元組」（10xxxxxx）
        for byte in data:
            byte &= 0xFF                      # 只看最低 8 位
            if need == 0:
                if byte >> 7 == 0b0:          # 0xxxxxxx：1 位元組字元
                    continue
                elif byte >> 5 == 0b110:      # 110xxxxx：後面還有 1 個
                    need = 1
                elif byte >> 4 == 0b1110:     # 1110xxxx：後面還有 2 個
                    need = 2
                elif byte >> 3 == 0b11110:    # 11110xxx：後面還有 3 個
                    need = 3
                else:                         # 10xxxxxx 開頭，或 11111xxx：不合法
                    return False
            else:
                if byte >> 6 != 0b10:         # ★ 延續位元組必須是 10xxxxxx
                    return False
                need -= 1
        return need == 0                      # 最後不能還缺位元組'''

_p393 = S.load("p393")


def _utf8_ref(data):
    try:
        bytes(b & 0xFF for b in data).decode("utf-8")
        return True
    except UnicodeDecodeError:
        return None          # Python 的解碼器更嚴格（過長編碼、代理區等），僅用結構檢查比對


def _struct_ref(data):
    i = 0
    data = [b & 0xFF for b in data]
    while i < len(data):
        b = data[i]
        if b < 0x80:
            k = 0
        elif 0xC0 <= b < 0xE0:
            k = 1
        elif 0xE0 <= b < 0xF0:
            k = 2
        elif 0xF0 <= b < 0xF8:
            k = 3
        else:
            return False
        if i + k >= len(data):                 # 延續位元組不夠
            return False
        for j in range(1, k + 1):
            if not (0x80 <= data[i + j] < 0xC0):
                return False
        i += k + 1
    return True


for data, want in [([197, 130, 1], True), ([235, 140, 4], False), ([145], False), ([240, 162, 138, 147], True), ([250, 145, 145, 145, 145], False)]:
    assert _p393.validUtf8(data) == want
for _ in range(20000):
    data = [random.choice([0x41, 0x7F, 0x80, 0xBF, 0xC3, 0xDF, 0xE2, 0xEF, 0xF0, 0xF4, 0xF8, 0xFF, random.randrange(256)]) for _ in range(random.randrange(1, 7))]
    assert _p393.validUtf8(data) == _struct_ref(data), data
    if _utf8_ref(data):                        # Python 能解碼的，結構一定合法
        assert _p393.validUtf8(data)
for ch in "aé中😀":
    assert _p393.validUtf8(list(ch.encode("utf-8")))
print("P393 OK")

_P393_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">UTF-8 的四種長度（x 是實際資料位元）</text>
            <g font-family="monospace" font-size="13">
              <text x="30" y="56" fill="var(--text-muted)">1 位元組</text><text x="130" y="56" fill="var(--accent)">0</text><text x="139" y="56" fill="var(--text)">xxxxxxx</text>
              <text x="30" y="84" fill="var(--text-muted)">2 位元組</text><text x="130" y="84" fill="var(--accent)">110</text><text x="157" y="84" fill="var(--text)">xxxxx</text><text x="230" y="84" fill="#ff8a65">10</text><text x="248" y="84" fill="var(--text)">xxxxxx</text>
              <text x="30" y="112" fill="var(--text-muted)">3 位元組</text><text x="130" y="112" fill="var(--accent)">1110</text><text x="166" y="112" fill="var(--text)">xxxx</text><text x="230" y="112" fill="#ff8a65">10</text><text x="248" y="112" fill="var(--text)">xxxxxx</text><text x="330" y="112" fill="#ff8a65">10</text><text x="348" y="112" fill="var(--text)">xxxxxx</text>
              <text x="30" y="140" fill="var(--text-muted)">4 位元組</text><text x="130" y="140" fill="var(--accent)">11110</text><text x="175" y="140" fill="var(--text)">xxx</text><text x="230" y="140" fill="#ff8a65">10</text><text x="248" y="140" fill="var(--text)">xxxxxx</text><text x="330" y="140" fill="#ff8a65">10</text><text x="348" y="140" fill="var(--text)">xxxxxx</text><text x="430" y="140" fill="#ff8a65">10</text><text x="448" y="140" fill="var(--text)">xxxxxx</text>
            </g>
            <text x="30" y="176" fill="var(--accent)" font-size="12">第一個位元組：開頭有幾個 1，這個字元就佔幾個位元組（0 個 1 = 單一位元組）</text>
            <text x="30" y="198" fill="#ff8a65" font-size="12">後面的延續位元組一律以 10 開頭</text>
            <text x="30" y="222" fill="var(--text-muted)" font-size="12">例：「中」= E4 B8 AD = 1110 0100 | 10 111000 | 10 101101</text>'''

emit({
 "num": 393, "slug": "utf-8-validation",
 "en": [
   "Given an integer array <code>data</code> representing the data, return whether it is a valid <strong>UTF-8</strong> encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).",
   "A character in <strong>UTF-8</strong> can be from <strong>1 to 4 bytes</strong> long, subjected to the following rules:",
   ("ol", ["For a <strong>1-byte</strong> character, the first bit is a <code>0</code>, followed by its Unicode code.",
           "For an <strong>n-bytes</strong> character, the first <code>n</code> bits are all one's, the <code>n + 1</code> bit is <code>0</code>, followed by <code>n - 1</code> bytes with the most significant <code>2</code> bits being <code>10</code>."]),
   "<strong>Note:</strong> The input is an array of integers. Only the <strong>least significant 8 bits</strong> of each integer is used to store the data. This means each integer represents only 1 byte of data.",
 ],
 "zh": [
   "給你一個整數陣列 <code>data</code>，判斷它是不是合法的 <strong>UTF-8</strong> 編碼。",
   "UTF-8 的一個字元佔 <strong>1 到 4 個位元組</strong>，規則是：",
   ("ol", ["<strong>1 位元組</strong>的字元：最高位是 <code>0</code>。",
           "<strong>n 位元組</strong>的字元：第一個位元組的前 <code>n</code> 位都是 1、第 <code>n+1</code> 位是 0；後面接 <code>n − 1</code> 個位元組，每個的最高兩位都是 <code>10</code>。"]),
   "每個整數只使用<strong>最低 8 位</strong>，代表一個位元組。",
 ],
 "examples": """範例 1
  輸入：data = [197,130,1]
  輸出：true
  說明：11000101 10000010 00000001
        一個 2 位元組字元 + 一個 1 位元組字元。

範例 2
  輸入：data = [235,140,4]
  輸出：false
  說明：11101011 10001100 00000100
        第一個位元組說是 3 位元組字元，但第三個不是 10 開頭。""",
 "constraints": [
   "1 ≤ <code>data.length</code> ≤ 2 × 10⁴",
   "0 ≤ <code>data[i]</code> ≤ 255",
 ],
 "idea": [
   ("fig", _P393_FIG, "0 0 640 236"),
   ("c", """【狀態機：need = 還需要幾個延續位元組】
    need == 0（等待新字元的第一個位元組）：
        0xxxxxxx -> 單一位元組，need 保持 0
        110xxxxx -> need = 1
        1110xxxx -> need = 2
        11110xxx -> need = 3
        其他（10xxxxxx 或 11111xxx）-> 不合法
    need > 0（等待延續位元組）：
        必須是 10xxxxxx，need -= 1

    結束時 need 必須是 0（不能字元只寫了一半）。

【用右移判斷前綴】
    byte >> 5 == 0b110   <=>  前三位是 110
    byte >> 6 == 0b10    <=>  前兩位是 10

【注意】
    這題只檢查「結構」。真正的 UTF-8 還禁止過長編碼（例如用兩個位元組表示 'A'）、
    代理區 D800–DFFF、以及大於 U+10FFFF 的碼位 ——
    Python 的 bytes.decode 會拒絕這些，但本題不要求。"""),
 ],
 "approaches": [
   ap("解法", "狀態機逐位元組檢查", [
     ("c", S["p393"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>以 10xxxxxx 開頭</strong> → 延續位元組不能當字元開頭，false。",
   "<strong>11111xxx</strong> → 超過 4 位元組，false。",
   "<strong>最後字元不完整</strong> → need 不為 0，false。",
   "<strong>data[i] 超過 255</strong>（其他版本的題目）→ 只看最低 8 位。",
 ],
 "follow": [
   ("h", "為什麼 UTF-8 這樣設計？"),
   ("c", """1. 相容 ASCII：0–127 的編碼和 ASCII 完全一樣。
2. 自我同步：延續位元組都以 10 開頭，從任何位置往回找，最多 3 步就能找到字元的開頭。
3. 不會出現 0x00（除了真的 NUL 字元），C 語言的字串函式可以直接用。
這是 Ken Thompson 和 Rob Pike 在 1992 年一個晚上設計出來的。"""),
 ],
 "related": [
   "<strong>第 468 題 驗證 IP 位址</strong> —— 另一題格式驗證",
   "<strong>第 190 題 顛倒二進位位</strong>",
 ],
 "check": [
   "第一個位元組怎麼決定這個字元佔幾個位元組？",
   "延續位元組長什麼樣？",
   "為什麼最後還要檢查 need == 0？",
 ],
})
