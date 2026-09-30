# -*- coding: utf-8 -*-
"""第 207–212 題。"""
import random, itertools
from collections import deque
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(207)


def _rand_dag_or_not(n, m):
    edges = set()
    for _ in range(m):
        a, b = random.randrange(n), random.randrange(n)
        if a != b:
            edges.add((a, b))
    return [list(e) for e in edges]


def _has_cycle(n, pre):
    g = [[] for _ in range(n)]
    for a, b in pre:
        g[b].append(a)
    state = [0] * n

    def dfs(u):
        state[u] = 1
        for v in g[u]:
            if state[v] == 1 or (state[v] == 0 and dfs(v)):
                return True
        state[u] = 2
        return False
    return any(state[u] == 0 and dfs(u) for u in range(n))


# ==================== 207. Course Schedule ====================
S["p207_kahn"] = '''class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:        # 先修 b 才能修 a：邊 b -> a
            graph[b].append(a)
            indeg[a] += 1

        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        taken = 0
        while q:
            u = q.popleft()
            taken += 1
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:         # ★ 所有先修都修完了，可以修
                    q.append(v)
        return taken == numCourses        # 有環的課永遠進不了佇列'''

S["p207_dfs"] = '''class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        # 0 = 沒看過，1 = 正在目前的 DFS 路徑上，2 = 已確認沒有環
        state = [0] * numCourses

        def has_cycle(u: int) -> bool:
            state[u] = 1
            for v in graph[u]:
                if state[v] == 1:                         # ★ 回到路徑上的點 = 環
                    return True
                if state[v] == 0 and has_cycle(v):
                    return True
            state[u] = 2
            return False

        return not any(state[u] == 0 and has_cycle(u) for u in range(numCourses))'''

_DQ = {"deque": deque}
_p207 = [S.load(k, extra=_DQ) for k in ("p207_kahn", "p207_dfs")]
for n, pre, want in [(2, [[1, 0]], True), (2, [[1, 0], [0, 1]], False), (1, [], True),
                     (3, [[1, 0], [2, 1], [0, 2]], False), (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True)]:
    for sol in _p207:
        assert sol.canFinish(n, pre) == want, ("P207", n, pre, sol)
for _ in range(3000):
    n = random.randrange(1, 8)
    pre = _rand_dag_or_not(n, random.randrange(0, 12))
    want = not _has_cycle(n, pre)
    for sol in _p207:
        assert sol.canFinish(n, pre) == want, ("P207 rand", n, pre)
print("P207 OK")

_P207_FIG = '''            <text x="20" y="18" fill="var(--text-muted)" font-size="12">Kahn 演算法：每次拿出「入度 = 0」（沒有未完成先修）的課</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="80" cy="80" r="20" fill="none" stroke="var(--accent)"/><text x="80" y="85" fill="var(--accent)">0</text>
              <circle cx="200" cy="52" r="20" fill="none" stroke="var(--text-muted)"/><text x="200" y="57" fill="var(--text)">1</text>
              <circle cx="200" cy="120" r="20" fill="none" stroke="var(--text-muted)"/><text x="200" y="125" fill="var(--text)">2</text>
              <circle cx="320" cy="80" r="20" fill="none" stroke="var(--text-muted)"/><text x="320" y="85" fill="var(--text)">3</text>
              <text x="80" y="118" fill="var(--text-muted)" font-size="11">入度 0</text>
              <text x="248" y="46" fill="var(--text-muted)" font-size="11">入度 1</text>
              <text x="200" y="158" fill="var(--text-muted)" font-size="11">入度 1</text>
              <text x="320" y="118" fill="var(--text-muted)" font-size="11">入度 2</text>
            </g>
            <g stroke="var(--text-muted)" stroke-width="1.3">
              <line x1="99" y1="74" x2="180" y2="55"/><line x1="99" y1="86" x2="180" y2="115"/>
              <line x1="219" y1="55" x2="300" y2="74"/><line x1="219" y1="115" x2="300" y2="86"/>
            </g>
            <text x="400" y="54" fill="var(--text)" font-size="12">① 取出 0，1 與 2 的入度 → 0</text>
            <text x="400" y="78" fill="var(--text)" font-size="12">② 取出 1，3 的入度 → 1</text>
            <text x="400" y="102" fill="var(--text)" font-size="12">③ 取出 2，3 的入度 → 0</text>
            <text x="400" y="126" fill="var(--text)" font-size="12">④ 取出 3。共取出 4 門 ✔</text>
            <text x="20" y="196" fill="#ff8a65" font-size="12">★ 如果有環（例如 1 → 3 → 1），環上的課入度永遠降不到 0，永遠不會被取出。</text>
            <text x="20" y="220" fill="var(--gold)" font-size="12">所以只要「取出的數量 &lt; 課程總數」，就代表有環，修不完。</text>'''

emit({
 "num": 207, "slug": "course-schedule",
 "en": [
   "There are <code>numCourses</code> courses labeled <code>0</code> to <code>numCourses - 1</code>. "
   "You are given an array <code>prerequisites</code> where <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> "
   "means course <code>b<sub>i</sub></code> must be completed before course <code>a<sub>i</sub></code> can be taken.",
   "Return <code>true</code> if it is possible to complete every course, otherwise return <code>false</code>.",
 ],
 "zh": [
   "有 <code>numCourses</code> 門課，編號 <code>0</code> 到 <code>numCourses - 1</code>。"
   "陣列 <code>prerequisites</code> 中的 <code>[a<sub>i</sub>, b<sub>i</sub>]</code> 表示："
   "<strong>要修課程 <code>a<sub>i</sub></code>，必須先修完課程 <code>b<sub>i</sub></code></strong>。",
   "如果有辦法修完所有課程，回傳 <code>true</code>；否則回傳 <code>false</code>。",
 ],
 "examples": """範例 1
  輸入：numCourses = 2, prerequisites = [[1,0]]
  輸出：true
  說明：先修 0，再修 1。

範例 2
  輸入：numCourses = 2, prerequisites = [[1,0],[0,1]]
  輸出：false
  說明：修 1 要先修 0，修 0 又要先修 1 —— 互相卡住。""",
 "constraints": [
   "1 ≤ <code>numCourses</code> ≤ 2000",
   "0 ≤ <code>prerequisites.length</code> ≤ 5000",
   "<code>prerequisites[i].length == 2</code>",
   "0 ≤ <code>a<sub>i</sub>, b<sub>i</sub></code> &lt; <code>numCourses</code>",
   "所有的 <code>[a<sub>i</sub>, b<sub>i</sub>]</code> 都<strong>互不相同</strong>",
 ],
 "idea": [
   ("fig", _P207_FIG, "0 0 640 236"),
   ("c", """【把課程看成有向圖】

    [a, b]：先修 b 才能修 a  ->  畫一條 b -> a 的邊

    能不能修完所有課？
    = 這張有向圖有沒有環？
    = 能不能排出一個「拓撲排序」？

【兩種找環的方法】

    1. Kahn（BFS）：從沒有先修的課開始，一門一門修掉，
       修掉一門就把它指向的課的「剩餘先修數」減 1。
       最後修掉的數量 = numCourses 才代表沒有環。

    2. DFS 三色標記：
       白 0 = 沒走過
       灰 1 = 正在目前這條遞迴路徑上
       黑 2 = 已經確認從它出發不會有環
       走到灰色的點 = 走回自己的路徑 = 有環。

【方向要搞清楚】
    [a, b] 是「b 先、a 後」。
    邊的方向畫反了，在「判斷有沒有環」這題不影響答案
    （反轉所有邊，環還是環），
    但第 210 題要輸出順序時就會整個反過來 ✘"""),
 ],
 "approaches": [
   ap("解法一", "Kahn 演算法（BFS 拓撲排序）", [
     ("c", S["p207_kahn"]),
     ("c", """【為什麼 taken == numCourses 就沒有環？】

    環上的每一門課，都至少有一門先修也在環上。
    環上的課沒有一門能先被修掉 ->
    它們的入度永遠不會降到 0 ->
    永遠不會進佇列 -> taken < numCourses。

【複雜度】
    建圖 O(E)；每個點進出佇列一次、每條邊被處理一次 -> O(V + E)"""),
   ], "O(V + E)", "O(V + E)", "V = 課程數，E = 先修關係數", "鄰接串列與入度陣列", optimal=True),

   ap("解法二", "DFS 三色標記", [
     ("c", S["p207_dfs"]),
     ("c", """【為什麼需要三種顏色，兩種不夠？】

    如果只有「看過 / 沒看過」：
        0 -> 1, 0 -> 2, 1 -> 3, 2 -> 3
    從 0 走 1 走 3（標記看過），回來再走 2 走到 3——
    3 已經看過，但這【不是環】，只是兩條路匯合 ✘

    「灰色」專門代表「在目前這條路徑上」：
        走到灰色 -> 真的繞回自己 -> 環 ✔
        走到黑色 -> 那裡早就確認安全 -> 不用再走

【遞迴深度】
    最多 2000 層，超過 Python 預設的 1000。
    LeetCode 有調高上限；要保險可以 sys.setrecursionlimit，
    或改用解法一。"""),
   ], "O(V + E)", "O(V + E)", "", "遞迴堆疊最深 V"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、Kahn（BFS）", "O(V+E)", "O(V+E)", "不用遞迴，順便得到修課順序 ✔"],
    ["二、DFS 三色", "O(V+E)", "O(V+E)", "遞迴深度可能較深"]]),
 "edges": [
   "<strong>沒有任何先修</strong> → 一定修得完。",
   "<strong>課程自己指向自己</strong>（<code>[1, 1]</code>）→ 自環，修不完；兩種解法都能正確處理。",
   "<strong>圖不連通</strong> → Kahn 一開始就把所有入度 0 的點放進佇列；DFS 要對每個點都嘗試出發。",
   "<strong>DFS 只用兩種顏色</strong> → 會把「匯合」誤判成「環」。",
 ],
 "follow": [
   ("h", "追問一：如果要輸出修課順序？"),
   ("c", """就是第 210 題：Kahn 演算法中「出佇列的順序」就是一個合法的修課順序。
DFS 的話，是「後序（變黑的順序）」反轉過來。"""),
   ("h", "追問二：如果要知道「最少要幾個學期」修完（每學期不限門數）？"),
   ("c", """Kahn 演算法一次處理「一整層」入度為 0 的課，
層數就是學期數（第 1136 題，付費題）。"""),
 ],
 "related": [
   "<strong>第 210 題 課程表 II</strong> —— 輸出拓撲排序",
   "<strong>第 802 題 找到最終的安全狀態</strong> —— 三色標記",
   "<strong>第 1462 題 課程表 IV</strong> —— 查詢先修關係",
 ],
 "check": [
   "這題為什麼等價於「判斷有向圖有沒有環」？",
   "Kahn 演算法中，為什麼有環的課永遠不會進佇列？",
   "DFS 為什麼需要「灰色」這個狀態？",
   "<code>[a, b]</code> 應該畫成哪個方向的邊？",
 ],
})


# ==================== 208. Implement Trie ====================
S["p208"] = '''class Trie:
    def __init__(self):
        self.root = {}                       # 每個節點是一個 dict：字元 -> 子節點

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})   # 沒有就建立
        node["$"] = True                     # ★ 結束標記：有一個單字在這裡結束

    def _walk(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and "$" in node   # ★ 要走得到，而且是單字結尾

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None'''

S["p208_arr"] = '''class TrieNode:
    __slots__ = ("children", "end")

    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            i = ord(ch) - 97
            if node.children[i] is None:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.end = True

    def _walk(self, s: str):
        node = self.root
        for ch in s:
            node = node.children[ord(ch) - 97]
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.end

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None'''

S["p208_set"] = '''class Trie:
    def __init__(self):
        self.words = set()

    def insert(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        return word in self.words

    def startsWith(self, prefix: str) -> bool:
        return any(w.startswith(prefix) for w in self.words)   # ✘ 每次掃過全部單字'''

for key in ("p208", "p208_arr", "p208_set"):
    t = S.load(key, "Trie")
    t.insert("apple")
    assert t.search("apple") and not t.search("app") and t.startsWith("app")
    t.insert("app")
    assert t.search("app")
for _ in range(300):
    ts = [S.load(k, "Trie") for k in ("p208", "p208_arr", "p208_set")]
    words = set()
    for _ in range(40):
        w = "".join(random.choice("abc") for _ in range(random.randrange(1, 5)))
        op = random.randrange(3)
        if op == 0:
            words.add(w)
            for t in ts:
                t.insert(w)
        elif op == 1:
            for t in ts:
                assert t.search(w) == (w in words)
        else:
            want = any(x.startswith(w) for x in words)
            for t in ts:
                assert t.startsWith(w) == want
print("P208 OK")

_P208_FIG = '''            <text x="20" y="22" fill="var(--text-muted)" font-size="12">插入 "app"、"apple"、"bat" 之後的字典樹（粗框 = 有單字在這裡結束）</text>
            <g font-size="13" text-anchor="middle">
              <circle cx="300" cy="55" r="16" fill="none" stroke="var(--text-muted)"/><text x="300" y="60" fill="var(--text-muted)">·</text>
              <circle cx="200" cy="105" r="16" fill="none" stroke="var(--text-muted)"/><text x="200" y="110" fill="var(--text)">a</text>
              <circle cx="400" cy="105" r="16" fill="none" stroke="var(--text-muted)"/><text x="400" y="110" fill="var(--text)">b</text>
              <circle cx="200" cy="155" r="16" fill="none" stroke="var(--text-muted)"/><text x="200" y="160" fill="var(--text)">p</text>
              <circle cx="400" cy="155" r="16" fill="none" stroke="var(--text-muted)"/><text x="400" y="160" fill="var(--text)">a</text>
              <circle cx="200" cy="205" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="200" y="210" fill="var(--accent)">p</text>
              <circle cx="400" cy="205" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="400" y="210" fill="var(--accent)">t</text>
              <circle cx="200" cy="255" r="16" fill="none" stroke="var(--text-muted)"/><text x="200" y="260" fill="var(--text)">l</text>
              <circle cx="200" cy="305" r="16" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="200" y="310" fill="var(--accent)">e</text>
            </g>
            <g stroke="var(--text-muted)" stroke-width="1.2">
              <line x1="288" y1="66" x2="212" y2="94"/><line x1="312" y1="66" x2="388" y2="94"/>
              <line x1="200" y1="121" x2="200" y2="139"/><line x1="400" y1="121" x2="400" y2="139"/>
              <line x1="200" y1="171" x2="200" y2="189"/><line x1="400" y1="171" x2="400" y2="189"/>
              <line x1="200" y1="221" x2="200" y2="239"/><line x1="200" y1="271" x2="200" y2="289"/>
            </g>
            <text x="240" y="210" fill="var(--accent)" font-size="12">← "app" 在這裡結束</text>
            <text x="440" y="210" fill="var(--accent)" font-size="12">← "bat"</text>
            <text x="228" y="266" fill="var(--accent)" font-size="12">↓ "apple" 在下面結束</text>
            <text x="300" y="296" fill="var(--text)" font-size="12">search("ap")：走得到，但不是結束節點 → false</text>
            <text x="300" y="318" fill="var(--text)" font-size="12">startsWith("ap")：走得到 → true</text>'''

emit({
 "num": 208, "slug": "implement-trie-prefix-tree",
 "en": [
   "A <em>trie</em> (prefix tree) is a tree-shaped structure for storing strings so that lookups by "
   "prefix are fast. Implement the <code>Trie</code> class:",
   ("ul", [
     "<code>Trie()</code> creates an empty trie.",
     "<code>void insert(String word)</code> adds <code>word</code> to the trie.",
     "<code>boolean search(String word)</code> returns <code>true</code> if <code>word</code> was inserted before.",
     "<code>boolean startsWith(String prefix)</code> returns <code>true</code> if some previously inserted word begins with <code>prefix</code>.",
   ]),
 ],
 "zh": [
   "<strong>字典樹</strong>（Trie，又叫前綴樹）是一種用來存字串的樹狀結構，能很快地依前綴查詢。請實作 <code>Trie</code> 類別：",
   ("ul", [
     "<code>Trie()</code>：建立一棵空的字典樹。",
     "<code>insert(word)</code>：插入單字 <code>word</code>。",
     "<code>search(word)</code>：如果 <code>word</code> 之前插入過，回傳 <code>true</code>。",
     "<code>startsWith(prefix)</code>：如果有任何插入過的單字以 <code>prefix</code> 開頭，回傳 <code>true</code>。",
   ]),
 ],
 "examples": """範例
  操作：["Trie","insert","search","search","startsWith","insert","search"]
  參數：[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
  輸出：[null,null,true,false,true,null,true]

  說明：
    insert("apple")
    search("apple")    -> true
    search("app")      -> false（"app" 只是前綴，沒有被插入過）
    startsWith("app")  -> true
    insert("app")
    search("app")      -> true""",
 "constraints": [
   "1 ≤ <code>word.length, prefix.length</code> ≤ 2000",
   "<code>word</code> 和 <code>prefix</code> 只包含小寫英文字母",
   "<code>insert</code>、<code>search</code>、<code>startsWith</code> 合計最多呼叫 3 × 10⁴ 次",
 ],
 "idea": [
   ("fig", _P208_FIG, "0 0 640 330"),
   ("c", """【字典樹的核心】

    每條邊代表一個字元，從根走到某個節點的路徑 = 一個前綴。
    有共同前綴的單字共用同一條路（"app" 和 "apple" 共用 a-p-p）。

【為什麼需要「結束標記」？】

    插入 "apple" 之後，路徑 a-p-p 也存在。
    如果 search("app") 只看「走不走得到」，會誤判成 true ✘
    所以每個節點要記錄：「有沒有單字剛好在這裡結束」。

【search 和 startsWith 唯一的差別】
    search     ：走得到 + 是結束節點
    startsWith ：走得到 就好

【複雜度】
    每個操作只和字串長度 L 有關，和已經存了多少單字無關 ✔
    這是字典樹相對於「把所有單字放進 list 一個一個比」的最大優勢。"""),
 ],
 "approaches": [
   ap("解法一", "巢狀 dict（Python 最簡潔）", [
     ("c", S["p208"]),
     ("c", """【用 "$" 當結束標記】
    因為單字只含小寫字母，"$" 不會和任何字元衝突。
    這個寫法在 Python 裡非常常見，第 211、212 題都會沿用。

【setdefault(ch, {})】
    ch 存在 -> 回傳原本的子節點
    ch 不存在 -> 建立空 dict、存進去、回傳它
    一行完成「走下去或建立」✔"""),
   ], "O(L)", "O(總字元數)", "每個操作", "", optimal=True),

   ap("解法二", "固定長度 26 的子節點陣列", [
     ("c", S["p208_arr"]),
     "這是 C++ / Java 最常見的寫法。<code>__slots__</code> 讓每個節點少佔一些記憶體。"
     "<strong>缺點</strong>：每個節點固定 26 個欄位，字元很稀疏時浪費空間；在 Python 裡通常也沒有比 dict 快。",
   ], "O(L)", "O(26 × 節點數)", "", ""),

   ap("解法三", "集合（startsWith 太慢）", [
     ("c", S["p208_set"]),
     "<code>insert</code>、<code>search</code> 都是 O(L)，但 <code>startsWith</code> 要掃過所有單字——"
     "最壞 3×10⁴ 個單字 × 3×10⁴ 次查詢，<strong>這正是字典樹要解決的問題。</strong>",
   ], "startsWith O(N·L)", "O(總字元數)", "N = 單字數", ""),
 ],
 "compare": (["解法", "insert / search", "startsWith", "備註"],
   [["一、巢狀 dict", "O(L)", "O(L)", "推薦 ✔"],
    ["二、長度 26 陣列", "O(L)", "O(L)", "其他語言的標準寫法"],
    ["三、集合", "O(L)", "O(N·L)", "前綴查詢太慢 ✘"]]),
 "edges": [
   "<strong>搜尋一個只是前綴的字</strong>（插入 \"apple\"、搜尋 \"app\"）→ <code>false</code>。",
   "<strong>重複插入同一個字</strong> → 沒有影響。",
   "<strong><code>startsWith</code> 的前綴剛好等於整個單字</strong> → <code>true</code>。",
   "<strong>忘了結束標記</strong> → <code>search</code> 會把前綴當成單字。",
 ],
 "follow": [
   ("h", "追問一：怎麼支援刪除？"),
   ("c", """1. 走到單字的結束節點，拿掉結束標記。
2. 從底部往上，如果節點既不是結束節點、也沒有子節點，就把它從父節點刪掉。
可以在每個節點記一個「經過次數」讓判斷更簡單。"""),
   ("h", "追問二：怎麼列出所有以某個前綴開頭的單字？"),
   ("c", """先走到前綴的節點，再從那裡 DFS 收集所有結束節點。
這就是搜尋引擎「自動完成」的基本原理（第 642、1268 題）。"""),
 ],
 "related": [
   "<strong>第 211 題 添加與搜尋單字</strong> —— 支援萬用字元 '.'",
   "<strong>第 212 題 單詞搜尋 II</strong> —— 字典樹 + 回溯",
   "<strong>第 648 題 單字替換</strong> —— 找最短前綴",
   "<strong>第 1268 題 搜尋推薦系統</strong> —— 前綴自動完成",
 ],
 "check": [
   "字典樹為什麼讓前綴查詢和「存了多少單字」無關？",
   "為什麼需要結束標記？",
   "<code>search</code> 和 <code>startsWith</code> 的差別是什麼？",
   "巢狀 dict 和長度 26 陣列各有什麼優缺點？",
 ],
})


# ==================== 209. Minimum Size Subarray Sum ====================
S["p209_window"] = '''class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float("inf")
        total = left = 0
        for right, x in enumerate(nums):
            total += x
            while total >= target:                   # ★ 夠了就試著縮左邊
                best = min(best, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if best == float("inf") else best'''

S["p209_bs"] = '''class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre = [0]
        for x in nums:
            pre.append(pre[-1] + x)                  # 前綴和嚴格遞增（元素都 > 0）
        best = float("inf")
        for i in range(len(nums)):
            # 找最小的 j 使 pre[j] - pre[i] >= target
            j = bisect.bisect_left(pre, pre[i] + target)
            if j <= len(nums):
                best = min(best, j - i)
        return 0 if best == float("inf") else best'''

S["p209_brute"] = '''class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float("inf")
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                if total >= target:
                    best = min(best, j - i + 1)
                    break                              # 再往右只會更長
        return 0 if best == float("inf") else best'''

_p209 = [S.load(k) for k in ("p209_window", "p209_bs", "p209_brute")]
for t, nums, want in [(7, [2, 3, 1, 2, 4, 3], 2), (4, [1, 4, 4], 1), (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
                      (15, [1, 2, 3, 4, 5], 5), (1, [1], 1)]:
    for sol in _p209:
        assert sol.minSubArrayLen(t, nums) == want, ("P209", t, nums, sol)
for _ in range(3000):
    nums = [random.randint(1, 9) for _ in range(random.randrange(1, 15))]
    t = random.randint(1, 60)
    want = _p209[2].minSubArrayLen(t, nums)
    for sol in _p209[:2]:
        assert sol.minSubArrayLen(t, nums) == want, ("P209 rand", t, nums)
print("P209 OK")

emit({
 "num": 209, "slug": "minimum-size-subarray-sum",
 "en": [
   "Given an array of positive integers <code>nums</code> and a positive integer <code>target</code>, "
   "find the length of the shortest contiguous subarray whose sum is <strong>greater than or equal to</strong> "
   "<code>target</code>. If no such subarray exists, return <code>0</code>.",
 ],
 "zh": [
   "給你一個<strong>正整數</strong>陣列 <code>nums</code> 和一個正整數 <code>target</code>，"
   "找出總和<strong>大於等於</strong> <code>target</code> 的<strong>最短連續子陣列</strong>，回傳它的長度。"
   "如果不存在這樣的子陣列，回傳 <code>0</code>。",
 ],
 "examples": """範例 1
  輸入：target = 7, nums = [2,3,1,2,4,3]
  輸出：2
  說明：子陣列 [4,3] 的和是 7，長度 2 是最短的。

範例 2
  輸入：target = 4, nums = [1,4,4]
  輸出：1

範例 3
  輸入：target = 11, nums = [1,1,1,1,1,1,1,1]
  輸出：0""",
 "constraints": [
   "1 ≤ <code>target</code> ≤ 10⁹",
   "1 ≤ <code>nums.length</code> ≤ 10⁵",
   "1 ≤ <code>nums[i]</code> ≤ 10⁴",
 ],
 "mid": [
   ("note", "題目的追問", [
     "<strong>「If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).」</strong>",
     "少見的「做出最佳解之後，請再做一個比較慢的」——目的是練習前綴和 + 二分搜尋。",
   ]),
 ],
 "idea": [
   ("c", """【關鍵：所有元素都是正數】

    正數代表：
        視窗往右擴 -> 和一定變大
        視窗左邊縮 -> 和一定變小

    這個「單調性」讓滑動視窗成立：
        右指標一路往右加；
        一旦和 >= target，就記錄長度，然後盡量縮左邊。

【為什麼左指標不需要往回走？】

    假設以 right 結尾時，最短合法的起點是 left。
    right 往右移之後，新的最短起點只會 >= left
    （往右擴只會讓和變大，起點不需要往左）。
    所以 left 只會往右，總共最多移動 n 次 -> O(n) ✔

【如果有負數呢？】
    單調性消失，滑動視窗不成立 ->
    要改用「前綴和 + 單調佇列」（第 862 題，Hard）。

【模擬】target = 7, nums = [2,3,1,2,4,3]

    right=3：[2,3,1,2]=8 ≥ 7，長度 4；縮掉 2 -> [3,1,2]=6
    right=4：[3,1,2,4]=10 ≥ 7，長度 4；縮掉 3 -> [1,2,4]=7，長度 3；
             縮掉 1 -> [2,4]=6
    right=5：[2,4,3]=9 ≥ 7，長度 3；縮掉 2 -> [4,3]=7，長度 2 ✔"""),
 ],
 "approaches": [
   ap("解法一", "暴力列舉起點", [
     ("c", S["p209_brute"]),
     "每個起點往右加到夠為止。<strong>最壞 O(n²)</strong>，n = 10⁵ 時是 10¹⁰ 次，超時。",
   ], "O(n²)", "O(1)", "", ""),

   ap("解法二", "前綴和 + 二分搜尋（追問要求的 O(n log n)）", [
     ("c", S["p209_bs"]),
     ("c", """【前綴和】pre[k] = nums[0] + … + nums[k-1]
    子陣列 nums[i..j-1] 的和 = pre[j] - pre[i]

【要找】最小的 j，使 pre[j] >= pre[i] + target
    因為元素都是正數，pre 嚴格遞增 -> 可以二分 ✔

【bisect_left 回傳 len(pre) 代表找不到】
    這時 j = n + 1 > n，要跳過。"""),
   ], "O(n log n)", "O(n)", "n 次二分", "前綴和陣列"),

   ap("解法三", "滑動視窗", [
     ("c", S["p209_window"]),
     ("c", """【內層 while 看起來是巢狀迴圈，為什麼是 O(n)？】

    left 在整個過程中只往右移，最多移 n 次。
    所以 while 的「總」執行次數 ≤ n，
    加上外層 n 次 -> O(2n) = O(n) ✔

【為什麼是 while 而不是 if？】
    加進一個大數之後，可能可以一次縮掉好幾個左邊的元素。"""),
   ], "O(n)", "O(1)", "每個元素進出視窗各一次", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、暴力", "O(n²)", "O(1)", "超時 ✘"],
    ["二、前綴和 + 二分", "O(n log n)", "O(n)", "追問要求"],
    ["三、滑動視窗", "O(n)", "O(1)", "最佳 ✔"]]),
 "edges": [
   "<strong>全部加起來都不夠</strong> → 回傳 0（別回傳 <code>inf</code>）。",
   "<strong>單一元素就夠</strong> → 回傳 1。",
   "<strong>「大於等於」而不是「等於」</strong> → 別寫成 <code>== target</code>。",
   "<strong>用 <code>if</code> 代替 <code>while</code> 縮左邊</strong> → 會漏掉更短的答案。",
 ],
 "follow": [
   ("h", "追問：如果陣列裡有負數？"),
   ("c", """滑動視窗失效，因為縮左邊不一定讓和變小。
正確做法：前綴和 + 單調遞增的雙端佇列（第 862 題）：
    對每個 j，從佇列前端彈出所有 pre[j] - pre[front] >= target 的 i 並更新答案；
    從佇列後端彈出所有 pre[back] >= pre[j] 的 i（它們不可能比 j 更好）。
整體 O(n)。"""),
 ],
 "related": [
   "<strong>第 862 題 和至少為 K 的最短子陣列</strong> —— 有負數的版本",
   "<strong>第 3 題 無重複字元的最長子字串</strong> —— 滑動視窗",
   "<strong>第 76 題 最小覆蓋子字串</strong> —— 滑動視窗找最短",
   "<strong>第 713 題 乘積小於 K 的子陣列</strong> —— 同樣靠正數的單調性",
 ],
 "check": [
   "「所有元素都是正數」對滑動視窗為什麼重要？",
   "滑動視窗中的 <code>while</code> 為什麼不會讓複雜度變成 O(n²)？",
   "前綴和 + 二分的做法中，為什麼前綴和可以二分？",
   "如果有負數，要改用什麼方法？",
 ],
})


# ==================== 210. Course Schedule II ====================
S["p210_kahn"] = '''class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses
        for a, b in prerequisites:          # 先修 b -> 才能修 a
            graph[b].append(a)
            indeg[a] += 1

        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        order = []
        while q:
            u = q.popleft()
            order.append(u)                 # ★ 出佇列的順序就是修課順序
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return order if len(order) == numCourses else []'''

S["p210_dfs"] = '''class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses            # 0 白、1 灰、2 黑
        post = []                           # 後序：一門課「之後的課」全部處理完才加入

        def dfs(u: int) -> bool:            # 回傳 True 代表發現環
            state[u] = 1
            for v in graph[u]:
                if state[v] == 1 or (state[v] == 0 and dfs(v)):
                    return True
            state[u] = 2
            post.append(u)
            return False

        for u in range(numCourses):
            if state[u] == 0 and dfs(u):
                return []
        return post[::-1]                   # ★ 後序反轉 = 拓撲排序'''

_p210 = [S.load(k, extra=_DQ) for k in ("p210_kahn", "p210_dfs")]


def _p210_valid(n, pre, order):
    if sorted(order) != list(range(n)):
        return False
    pos = {c: i for i, c in enumerate(order)}
    return all(pos[b] < pos[a] for a, b in pre)


for n, pre in [(2, [[1, 0]]), (4, [[1, 0], [2, 0], [3, 1], [3, 2]]), (1, [])]:
    for sol in _p210:
        assert _p210_valid(n, pre, sol.findOrder(n, pre)), ("P210", n, pre, sol)
for sol in _p210:
    assert sol.findOrder(2, [[1, 0], [0, 1]]) == []
for _ in range(3000):
    n = random.randrange(1, 8)
    pre = _rand_dag_or_not(n, random.randrange(0, 12))
    cyc = _has_cycle(n, pre)
    for sol in _p210:
        got = sol.findOrder(n, pre)
        if cyc:
            assert got == [], ("P210 cyc", n, pre)
        else:
            assert _p210_valid(n, pre, got), ("P210 rand", n, pre, got)
print("P210 OK")

emit({
 "num": 210, "slug": "course-schedule-ii",
 "en": [
   "There are <code>numCourses</code> courses labeled <code>0</code> to <code>numCourses - 1</code>. "
   "Each pair <code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> means course "
   "<code>b<sub>i</sub></code> has to be taken before course <code>a<sub>i</sub></code>.",
   "Return any ordering of the courses that lets you finish all of them. If no such ordering exists, "
   "return an empty array.",
 ],
 "zh": [
   "有 <code>numCourses</code> 門課，編號 <code>0</code> 到 <code>numCourses - 1</code>。"
   "<code>prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> 表示<strong>修 <code>a<sub>i</sub></code> 之前必須先修 <code>b<sub>i</sub></code></strong>。",
   "請回傳一個能修完所有課程的順序；如果有多種，回傳<strong>任意一種</strong>都可以。"
   "如果不可能修完，回傳<strong>空陣列</strong>。",
 ],
 "examples": """範例 1
  輸入：numCourses = 2, prerequisites = [[1,0]]
  輸出：[0,1]

範例 2
  輸入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  輸出：[0,2,1,3]
  說明：[0,1,2,3] 也是正確答案。

範例 3
  輸入：numCourses = 1, prerequisites = []
  輸出：[0]""",
 "constraints": [
   "1 ≤ <code>numCourses</code> ≤ 2000",
   "0 ≤ <code>prerequisites.length</code> ≤ <code>numCourses × (numCourses − 1)</code>",
   "<code>prerequisites[i].length == 2</code>",
   "0 ≤ <code>a<sub>i</sub>, b<sub>i</sub></code> &lt; <code>numCourses</code>，且 <code>a<sub>i</sub> ≠ b<sub>i</sub></code>",
   "所有的 <code>[a<sub>i</sub>, b<sub>i</sub>]</code> 互不相同",
 ],
 "idea": [
   ("c", """【這題 = 第 207 題 + 把順序輸出】

    第 207 題問「有沒有環」；
    這題要把「拓撲排序」本身交出來。

【Kahn 演算法】
    出佇列的順序本身就是一個合法順序：
    一門課出佇列時，它所有的先修課都已經出佇列了。

【DFS】
    一門課的後序（它之後的課全部處理完才輪到它）
    會「晚於」它的所有後續課程。
    所以把後序【反轉】，每門課就排在它的後續課程之前 ✔

【方向陷阱】
    [a, b] 是「b 在前」。
    如果邊畫成 a -> b，Kahn 會輸出【完全顛倒】的順序 ✘
    第 207 題不會發現這個錯，這題會。

【答案不唯一】
    範例 2 的 [0,1,2,3] 和 [0,2,1,3] 都對 ——
    判題程式會驗證順序是否合法，而不是比對固定答案。"""),
 ],
 "approaches": [
   ap("解法一", "Kahn 演算法（BFS）", [
     ("c", S["p210_kahn"]),
     "和第 207 題幾乎一模一樣，只是把 <code>taken += 1</code> 換成 <code>order.append(u)</code>。",
   ], "O(V + E)", "O(V + E)", "", "", optimal=True),

   ap("解法二", "DFS 後序反轉", [
     ("c", S["p210_dfs"]),
     ("c", """【為什麼後序反轉是拓撲排序？】

    對每條邊 u -> v：
        如果 DFS 先碰到 u，會在 u 結束前先走完 v -> v 先進 post
        如果 DFS 先碰到 v，v 會先完整結束（u 還沒被走到）-> v 先進 post
    無論哪種，v 都在 u 之前進入 post。
    反轉之後，u 在 v 之前 ✔

【為什麼不直接用前序？】
    前序只保證「從同一個起點出發」的順序，
    跨起點時會出錯。"""),
   ], "O(V + E)", "O(V + E)", "", "遞迴堆疊最深 V"),
 ],
 "compare": (["解法", "時間", "空間", "備註"],
   [["一、Kahn", "O(V+E)", "O(V+E)", "直觀，無遞迴 ✔"],
    ["二、DFS 後序反轉", "O(V+E)", "O(V+E)", "要記得反轉"]]),
 "edges": [
   "<strong>有環</strong> → 回傳 <code>[]</code>，不是部分順序。",
   "<strong>沒有先修</strong> → 任何排列都行，例如 <code>[0, 1, …, n-1]</code>。",
   "<strong>邊的方向畫反</strong> → 輸出完全顛倒的順序。",
   "<strong>DFS 忘了反轉 <code>post</code></strong> → 順序顛倒。",
 ],
 "follow": [
   ("h", "追問：如果要字典序最小的修課順序？"),
   ("c", """把 Kahn 演算法的佇列換成最小堆積（heapq），
每次取出編號最小的入度 0 課程。複雜度變成 O((V + E) log V)。"""),
 ],
 "related": [
   "<strong>第 207 題 課程表</strong> —— 只判斷能不能修完",
   "<strong>第 269 題 外星文字典</strong>（付費）—— 從字典序推出字母順序",
   "<strong>第 2115 題 從給定原料找到所有可以做出的菜</strong> —— 拓撲排序",
 ],
 "check": [
   "Kahn 演算法中，出佇列的順序為什麼是合法的修課順序？",
   "DFS 為什麼要把後序反轉？",
   "邊的方向畫反會發生什麼事？",
   "要字典序最小的順序，要怎麼改？",
 ],
})


# ==================== 211. Design Add and Search Words Data Structure ====================
S["p211"] = '''class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(node: dict, i: int) -> bool:
            if i == len(word):
                return "$" in node
            ch = word[i]
            if ch == ".":                           # ★ 萬用字元：每個子節點都試
                return any(dfs(child, i + 1)
                           for key, child in node.items() if key != "$")
            return ch in node and dfs(node[ch], i + 1)
        return dfs(self.root, 0)'''

S["p211_len"] = '''class WordDictionary:
    def __init__(self):
        self.by_len = defaultdict(set)              # 長度 -> 這個長度的單字

    def addWord(self, word: str) -> None:
        self.by_len[len(word)].add(word)

    def search(self, word: str) -> bool:
        cands = self.by_len[len(word)]
        if "." not in word:
            return word in cands                    # 沒有萬用字元：O(L)
        return any(all(p == "." or p == c for p, c in zip(word, w))
                   for w in cands)'''

_P211_EXTRA = {"defaultdict": __import__("collections").defaultdict}
for key in ("p211", "p211_len"):
    d = S.load(key, "WordDictionary", _P211_EXTRA)
    for w in ("bad", "dad", "mad"):
        d.addWord(w)
    assert [d.search(x) for x in ("pad", "bad", ".ad", "b..")] == [False, True, True, True]
for _ in range(300):
    ds = [S.load(k, "WordDictionary", _P211_EXTRA) for k in ("p211", "p211_len")]
    words = set()
    for _ in range(40):
        if random.random() < 0.5:
            w = "".join(random.choice("ab") for _ in range(random.randrange(1, 4)))
            words.add(w)
            for d in ds:
                d.addWord(w)
        else:
            q = "".join(random.choice("ab.") for _ in range(random.randrange(1, 4)))
            want = any(len(w) == len(q) and all(p == "." or p == c for p, c in zip(q, w)) for w in words)
            for d in ds:
                assert d.search(q) == want, ("P211", q, words)
print("P211 OK")

emit({
 "num": 211, "slug": "design-add-and-search-words-data-structure",
 "en": [
   "Design a data structure that stores words and lets you check whether a query matches any stored word. "
   "Implement the <code>WordDictionary</code> class:",
   ("ul", [
     "<code>WordDictionary()</code> creates an empty dictionary.",
     "<code>void addWord(word)</code> stores <code>word</code>.",
     "<code>bool search(word)</code> returns <code>true</code> if some stored word matches <code>word</code>. "
     "The query may contain the character <code>'.'</code>, which matches any single letter.",
   ]),
 ],
 "zh": [
   "設計一個資料結構，可以存入單字，並查詢某個字串是否能和已存的單字匹配。請實作 <code>WordDictionary</code> 類別：",
   ("ul", [
     "<code>WordDictionary()</code>：建立空的字典。",
     "<code>addWord(word)</code>：存入 <code>word</code>。",
     "<code>search(word)</code>：如果有已存的單字能匹配 <code>word</code>，回傳 <code>true</code>。"
     "查詢字串中的 <code>'.'</code> 可以匹配<strong>任意一個字母</strong>。",
   ]),
 ],
 "examples": """範例
  操作：["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
  參數：[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
  輸出：[null,null,null,null,false,true,true,true]""",
 "constraints": [
   "1 ≤ <code>word.length</code> ≤ 25",
   "<code>addWord</code> 的 <code>word</code> 只包含小寫英文字母",
   "<code>search</code> 的 <code>word</code> 包含 <code>'.'</code> 或小寫英文字母",
   "每次 <code>search</code> 的查詢字串中，<code>'.'</code> 最多出現 2 個",
   "<code>addWord</code> 和 <code>search</code> 合計最多呼叫 10⁴ 次",
 ],
 "idea": [
   ("c", """【沒有 '.' 的話，這就是第 208 題的字典樹】

【遇到 '.' 怎麼辦？】
    '.' 可以是任何字母 ->
    在字典樹的這一層，【每個子節點都要試一次】。
    只要有一條路能走到結尾而且是結束節點，就回傳 true。

    這自然是一個 DFS（回溯）：
        dfs(節點, 查詢位置 i)
            i 走完 -> 看是不是結束節點
            字母   -> 只走那一個子節點
            '.'    -> 每個子節點都試

【最壞複雜度】
    每個 '.' 讓分支變成最多 26 倍。
    題目限制 '.' 最多 2 個 -> 最多 26² = 676 條路，
    每條路長度 ≤ 25 -> 一次查詢最多幾萬步，完全可接受 ✔"""),
 ],
 "approaches": [
   ap("解法一", "字典樹 + DFS", [
     ("c", S["p211"]),
     ("c", """【key != "$" 那個條件】
    "$" 是結束標記，不是字元，走 '.' 時要跳過它，
    否則會試圖把 True 當成節點往下走 ✘

【any(...) 會短路】
    找到一條能成功的路就立刻停止，不會浪費時間試剩下的。"""),
   ], "add O(L)，search 最壞 O(26ᵈ · L)", "O(總字元數)", "d = '.' 的個數（≤ 2）", "", optimal=True),

   ap("解法二", "依長度分組 + 逐一比對", [
     ("c", S["p211_len"]),
     "只和長度相同的單字比。<strong>沒有 '.' 時是 O(L)</strong>，有 '.' 時要掃過所有同長度的單字。"
     "在這題的限制下也能通過，但如果單字很多，字典樹比較穩。",
   ], "search 最壞 O(N·L)", "O(總字元數)", "N = 同長度的單字數", ""),
 ],
 "compare": (["解法", "addWord", "search（有 '.'）", "備註"],
   [["一、字典樹 + DFS", "O(L)", "O(26ᵈ·L)", "與單字數量無關 ✔"],
    ["二、依長度分組", "O(1)", "O(N·L)", "單字多時變慢"]]),
 "edges": [
   "<strong>查詢全是 '.'</strong>（例如 <code>\"...\"</code>）→ 只要有任何長度 3 的單字就是 <code>true</code>。",
   "<strong>查詢比所有單字都長</strong> → 走不到底，<code>false</code>。",
   "<strong>查詢只是某個單字的前綴</strong> → 不是結束節點，<code>false</code>。",
   "<strong>'.' 時沒跳過結束標記</strong> → 程式出錯。",
 ],
 "follow": [
   ("h", "追問：如果 '.' 的數量沒有限制？"),
   ("c", """最壞情況（查詢全是 '.'）會走遍整棵字典樹中所有長度 L 的路徑 ——
這在所有做法中都是無法避免的，因為答案本來就可能依賴任何一個單字。
可以額外在每個節點記錄「以下有沒有長度剛好是 k 的單字」來剪枝。"""),
 ],
 "related": [
   "<strong>第 208 題 實作字典樹</strong>",
   "<strong>第 212 題 單詞搜尋 II</strong> —— 字典樹 + 網格 DFS",
   "<strong>第 10 題 正規表示式匹配</strong> —— 更一般的萬用字元",
 ],
 "check": [
   "遇到 '.' 時，字典樹要怎麼搜尋？",
   "為什麼題目限制 '.' 最多 2 個很重要？",
   "走 '.' 分支時為什麼要跳過結束標記？",
 ],
})


# ==================== 212. Word Search II ====================
S["p212"] = '''class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        for w in words:                      # 1. 把所有單字建成字典樹
            node = root
            for ch in w:
                node = node.setdefault(ch, {})
            node["$"] = w                    # ★ 結束節點直接存整個單字

        m, n = len(board), len(board[0])
        found = []

        def dfs(r: int, c: int, parent: dict) -> None:
            ch = board[r][c]
            node = parent[ch]
            if "$" in node:
                found.append(node.pop("$"))  # ★ 找到就拿掉，避免重複加入
            board[r][c] = "#"                # 標記走過
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in node:
                    dfs(nr, nc, node)
            board[r][c] = ch                 # 回溯：還原
            if not node:                     # ★ 剪枝：這個分支已經沒有單字了
                parent.pop(ch)

        for r in range(m):
            for c in range(n):
                if board[r][c] in root:
                    dfs(r, c, root)
        return found'''

S["p212_each"] = '''class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])

        def exist(word: str) -> bool:        # 第 79 題的解法，每個單字各做一次
            def dfs(r, c, i):
                if i == len(word):
                    return True
                if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[i]:
                    return False
                board[r][c] = "#"
                ok = any(dfs(r + dr, c + dc, i + 1)
                         for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
                board[r][c] = word[i]
                return ok
            return any(dfs(r, c, 0) for r in range(m) for c in range(n))

        return [w for w in words if exist(w)]'''

_p212 = [S.load(k) for k in ("p212", "p212_each")]
B1 = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
for sol in _p212:
    assert sorted(sol.findWords([r[:] for r in B1], ["oath", "pea", "eat", "rain"])) == ["eat", "oath"]
    assert sol.findWords([["a", "b"], ["c", "d"]], ["abcb"]) == []
    assert sorted(sol.findWords([["a", "a"]], ["a", "aa", "aaa"])) == ["a", "aa"]
for _ in range(400):
    m, n = random.randrange(1, 4), random.randrange(1, 4)
    board = [[random.choice("ab") for _ in range(n)] for _ in range(m)]
    words = list({"".join(random.choice("ab") for _ in range(random.randrange(1, 6))) for _ in range(6)})
    want = sorted(_p212[1].findWords([r[:] for r in board], words))
    b2 = [r[:] for r in board]
    got = sorted(_p212[0].findWords(b2, words))
    assert got == want, ("P212", board, words, got, want)
    assert b2 == board, "P212 棋盤要還原"
print("P212 OK")

emit({
 "num": 212, "slug": "word-search-ii",
 "en": [
   "You are given an <code>m x n</code> grid of letters <code>board</code> and a list of distinct strings "
   "<code>words</code>. Return every word from the list that can be found on the board.",
   "A word is formed by a path of horizontally or vertically adjacent cells. Each cell may be used "
   "at most once within the same word. The answer can be returned in any order.",
 ],
 "zh": [
   "給你一個 <code>m x n</code> 的字母網格 <code>board</code>，以及一個由不重複字串組成的清單 <code>words</code>。"
   "請回傳所有<strong>能在網格中找到</strong>的單字。",
   "單字必須由<strong>上下左右相鄰</strong>的格子依序組成，<strong>同一個單字中每個格子最多用一次</strong>。答案順序不限。",
 ],
 "examples": """範例 1
  輸入：board = [["o","a","a","n"],
                 ["e","t","a","e"],
                 ["i","h","k","r"],
                 ["i","f","l","v"]],
        words = ["oath","pea","eat","rain"]
  輸出：["eat","oath"]

範例 2
  輸入：board = [["a","b"],["c","d"]], words = ["abcb"]
  輸出：[]
  說明：b 要用兩次，不行。""",
 "constraints": [
   "<code>m == board.length</code>，<code>n == board[i].length</code>",
   "1 ≤ <code>m, n</code> ≤ 12",
   "<code>board[i][j]</code> 是小寫英文字母",
   "1 ≤ <code>words.length</code> ≤ 3 × 10⁴",
   "1 ≤ <code>words[i].length</code> ≤ 10",
   "<code>words[i]</code> 只包含小寫英文字母，且所有單字<strong>互不相同</strong>",
 ],
 "idea": [
   ("c", """【第 79 題（單詞搜尋）一次找一個單字】
    對 3×10^4 個單字各做一次網格 DFS ->
    每次最多 12×12 個起點 × 4^10 條路 ✘ 超時

【關鍵想法：一次 DFS 同時找所有單字】
    把所有單字建成字典樹。
    網格 DFS 的時候，同時沿著字典樹往下走：
        - 目前的路徑不是任何單字的前綴 -> 立刻停（剪枝）
        - 走到結束節點 -> 找到一個單字

    這樣共同前綴只會被探索一次，
    而且「不可能的方向」在第一個字母就被砍掉 ✔

【三個讓它真的夠快的細節】
    1. 結束節點直接存整個單字 -> 找到時不用重建字串
    2. 找到後把單字從字典樹拿掉 -> 不會重複加入，也不會重複搜尋
    3. 回溯時，如果子節點已經空了，就從父節點刪掉 ->
       已經找完的分支再也不會被走進去（這個剪枝讓速度差非常多）"""),
 ],
 "approaches": [
   ap("解法一", "每個單字各跑一次第 79 題（超時）", [
     ("c", S["p212_each"]),
     "邏輯正確，但單字多時會重複探索大量相同的前綴。<strong>3×10⁴ 個單字時會超時。</strong>",
   ], "O(W · m·n · 4^L)", "O(L)", "W = 單字數，L = 單字長度", "遞迴深度"),

   ap("解法二", "字典樹 + 回溯 + 剪枝", [
     ("c", S["p212"]),
     ("c", """【dfs(r, c, parent) 為什麼傳「父節點」？】
    因為最後要能從父節點把空掉的子節點刪掉（剪枝），
    所以需要父節點的參照。

【進入 dfs 之前就檢查 board[nr][nc] in node】
    不在字典樹裡的方向根本不進遞迴，
    也順便排除了已經走過的格子（'#' 不在字典樹裡）。

【回溯時一定要還原 board[r][c]】
    否則其他起點的搜尋會看到被改掉的棋盤 ✘"""),
   ], "O(m·n · 4 · 3^(L−1))", "O(總字元數)", "每條路徑第一步 4 個方向，之後最多 3 個", "字典樹", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、逐一單字", "O(W · m·n · 4^L)", "超時 ✘"],
    ["二、字典樹 + 剪枝", "O(m·n · 4 · 3^(L−1))", "與單字數量無關 ✔"]]),
 "edges": [
   "<strong>同一個單字在網格中出現好幾次</strong> → 只能回傳一次（找到後從字典樹拿掉）。",
   "<strong>單字需要重複使用格子</strong>（範例 2）→ 找不到。",
   "<strong>一個單字是另一個的前綴</strong>（<code>\"a\"</code> 和 <code>\"aa\"</code>）→ 兩個都要找到，不能找到第一個就停。",
   "<strong>忘了還原棋盤</strong> → 後續搜尋出錯。",
 ],
 "follow": [
   ("h", "追問：為什麼「刪除空掉的分支」能讓速度差那麼多？"),
   ("c", """網格常常很「重複」（例如整片都是 'a'），
而單字清單可能有很多共同前綴。
沒有刪除分支時，已經找完的單字所在的路徑，
每個起點都還會再走一次。
刪除之後，找完的部分從字典樹上消失，
之後的起點在第一步就被擋下。"""),
 ],
 "related": [
   "<strong>第 79 題 單詞搜尋</strong> —— 只找一個單字",
   "<strong>第 208 題 實作字典樹</strong>",
   "<strong>第 211 題 添加與搜尋單字</strong>",
 ],
 "check": [
   "為什麼要先把所有單字建成字典樹，而不是每個單字各搜一次？",
   "找到單字後為什麼要把它從字典樹拿掉？",
   "回溯時刪除空分支有什麼效果？",
   "為什麼 DFS 結束時一定要還原棋盤？",
 ],
})
