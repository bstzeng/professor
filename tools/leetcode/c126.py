# -*- coding: utf-8 -*-
"""第 126–130 題。"""
import random, string, itertools
from collections import deque, defaultdict
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(126)

# ==================== 127. Word Ladder ====================
S["p127_bfs"] = '''from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0                        # 終點不在字典裡，直接不可能

        L = len(beginWord)
        dq = deque([beginWord])
        seen = {beginWord}
        step = 1

        while dq:
            for _ in range(len(dq)):
                w = dq.popleft()
                if w == endWord:
                    return step
                # 枚舉「改一個位置成 a..z」的所有鄰居
                for i in range(L):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        nxt = w[:i] + c + w[i + 1:]
                        if nxt in words and nxt not in seen:
                            seen.add(nxt)
                            dq.append(nxt)
            step += 1

        return 0'''

S["p127_bidi"] = '''class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        L = len(beginWord)
        front, back = {beginWord}, {endWord}    # 從兩端同時往中間搜
        seen = {beginWord, endWord}
        step = 1

        while front and back:
            if len(front) > len(back):          # 永遠從比較小的那一邊擴展
                front, back = back, front

            nxt = set()
            for w in front:
                for i in range(L):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        cand = w[:i] + c + w[i + 1:]
                        if cand in back:
                            return step + 1     # 兩邊碰頭了
                        if cand in words and cand not in seen:
                            seen.add(cand)
                            nxt.add(cand)
            front = nxt
            step += 1

        return 0'''

S["p127_pattern"] = '''from collections import deque, defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        # 先建「萬用字元桶」：h*t -> [hot, hit, ...]
        buckets = defaultdict(list)
        for w in wordList:
            for i in range(L):
                buckets[w[:i] + "*" + w[i + 1:]].append(w)

        dq = deque([(beginWord, 1)])
        seen = {beginWord}
        while dq:
            w, step = dq.popleft()
            if w == endWord:
                return step
            for i in range(L):
                for nxt in buckets[w[:i] + "*" + w[i + 1:]]:
                    if nxt not in seen:
                        seen.add(nxt)
                        dq.append((nxt, step + 1))

        return 0'''


def _p127_ref(begin, end, wl):
    """獨立參考解：建完整的圖，再用最樸素的 BFS。"""
    words = list(dict.fromkeys([begin] + list(wl)))
    if end not in set(wl):
        return 0
    def adj(a, b):
        return len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1
    g = {w: [v for v in words if v != w and adj(w, v)] for w in words}
    dist = {begin: 1}
    q = deque([begin])
    while q:
        w = q.popleft()
        if w == end:
            return dist[w]
        for v in g[w]:
            if v not in dist:
                dist[v] = dist[w] + 1
                q.append(v)
    return 0


_p127 = [S.load(k) for k in ("p127_bfs", "p127_bidi", "p127_pattern")]

for b, e, wl, want in [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"], 5),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0),
    ("a", "c", ["a", "b", "c"], 2),
    ("hot", "dog", ["hot", "dog"], 0),
]:
    assert _p127_ref(b, e, wl) == want, ("P127 ref", b, e, wl, _p127_ref(b, e, wl))
    for sol in _p127:
        assert sol.ladderLength(b, e, list(wl)) == want, ("P127", b, e, wl, sol)

for _ in range(1500):
    L = random.choice([2, 3])
    alpha = "abc"
    allw = ["".join(p) for p in itertools.product(alpha, repeat=L)]
    wl = random.sample(allw, random.randrange(1, len(allw) + 1))
    b = random.choice(allw)
    e = random.choice([w for w in allw if w != b])   # 題目保證 begin != end
    want = _p127_ref(b, e, wl)
    for sol in _p127:
        got = sol.ladderLength(b, e, list(wl))
        assert got == want, ("P127 random", b, e, wl, want, got, sol)
print("P127 solutions OK")

_P127_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">把每個單字當成一個節點，「差一個字母」就連一條邊 —— 問題變成圖上的最短路徑。</text>
            <g font-size="13" text-anchor="middle">
              <ellipse cx="80" cy="80" rx="34" ry="19" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="80" y="85" fill="var(--gold)">hit</text>
              <ellipse cx="210" cy="80" rx="34" ry="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="210" y="85" fill="var(--accent)">hot</text>
              <ellipse cx="340" cy="46" rx="34" ry="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="340" y="51" fill="var(--accent)">dot</text>
              <ellipse cx="340" cy="120" rx="34" ry="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="340" y="125" fill="var(--accent)">lot</text>
              <ellipse cx="470" cy="46" rx="34" ry="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="470" y="51" fill="var(--accent)">dog</text>
              <ellipse cx="470" cy="120" rx="34" ry="19" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="470" y="125" fill="var(--accent)">log</text>
              <ellipse cx="580" cy="80" rx="34" ry="19" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="580" y="85" fill="#ff8a65">cog</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="114" y1="80" x2="176" y2="80"/>
              <line x1="240" y1="72" x2="308" y2="53"/><line x1="240" y1="88" x2="308" y2="113"/>
              <line x1="374" y1="46" x2="436" y2="46"/><line x1="374" y1="120" x2="436" y2="120"/>
              <line x1="340" y1="65" x2="340" y2="101"/><line x1="470" y1="65" x2="470" y2="101"/>
              <line x1="504" y1="53" x2="548" y2="72"/><line x1="504" y1="113" x2="548" y2="88"/>
            </g>
            <text x="20" y="176" fill="var(--gold)" font-size="12">最短路徑：hit → hot → dot → dog → cog，共 5 個單字。</text>
            <line x1="20" y1="198" x2="620" y2="198" stroke="var(--border)"/>
            <text x="20" y="224" fill="var(--accent)" font-size="13">★ 怎麼找「鄰居」？兩個方法，複雜度差很多：</text>
            <text x="40" y="252" fill="#ff8a65" font-size="12">方法 A：拿目前的字和字典裡【每一個】字比對　→　每次 O(N·L)，總共 O(N²·L)</text>
            <text x="40" y="280" fill="var(--gold)" font-size="12">方法 B：枚舉「改第 i 位成 a..z」，檢查在不在集合裡　→　每次 O(26·L)，總共 O(N·26·L)</text>
            <text x="40" y="308" fill="var(--text-muted)" font-size="12">N = 5000、L = 10 時：A 約 2.5 億次，B 約 130 萬次 —— 差了 200 倍。</text>
            <text x="20" y="344" fill="var(--accent)" font-size="12">方法 C（萬用字元桶）：先把每個字拆成 h*t、*ot、ho* 建索引，查鄰居就是查一個 dict。</text>
            <text x="40" y="368" fill="var(--text-muted)" font-size="12">預處理 O(N·L)，之後每次查 O(L)。當字母表很大（不只 26 個）時，這個比 B 好。</text>
            <text x="20" y="402" fill="var(--gold)" font-size="12">雙向 BFS：從兩端同時擴展，搜尋樹的大小從 b^d 降到 2·b^(d/2) —— 常常快好幾倍。</text>'''

emit({
 "num": 127, "slug": "word-ladder",
 "en": [
   "A <strong>transformation sequence</strong> from word <code>beginWord</code> to word "
   "<code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words "
   "<code>beginWord -&gt; s₁ -&gt; s₂ -&gt; ... -&gt; sₖ</code> such that:",
   ("raw", "<ul><li>Every adjacent pair of words differs by a single letter.</li>"
           "<li>Every <code>sᵢ</code> for <code>1 &lt;= i &lt;= k</code> is in "
           "<code>wordList</code>. Note that <code>beginWord</code> does not need to be in "
           "<code>wordList</code>.</li>"
           "<li><code>sₖ == endWord</code></li></ul>"),
   "Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary "
   "<code>wordList</code>, return <em>the <strong>number of words</strong> in the "
   "<strong>shortest transformation sequence</strong></em>, or <code>0</code> if no such "
   "sequence exists.",
 ],
 "zh": [
   "給你兩個單字 <code>beginWord</code>、<code>endWord</code> 和一個字典 <code>wordList</code>。",
   "一個<strong>轉換序列</strong>是 "
   "<code>beginWord → s₁ → s₂ → … → sₖ</code>，其中：",
   ("ul", [
     "<strong>相鄰兩個單字只差一個字母</strong>。",
     "每一個 <code>sᵢ</code> 都必須在 <code>wordList</code> 裡"
     "（<strong><code>beginWord</code> 不需要在裡面</strong>）。",
     "<code>sₖ</code> 就是 <code>endWord</code>。",
   ]),
   "回傳<strong>最短轉換序列裡的單字個數</strong>；如果不存在這樣的序列，回傳 <code>0</code>。",
 ],
 "pre": [
   ("note", "這是一個偽裝成字串題的圖論題", [
     ("c", """把每個單字看成【圖上的一個節點】，
「只差一個字母」的兩個單字之間連一條【無權邊】。

    問題就變成：求 beginWord 到 endWord 的最短路徑長度。

【無權圖的最短路徑 = BFS】

    因為 BFS 一層一層擴散，
    第一次走到某個節點時，走的一定是最短路徑。

    （有權重的話就要 Dijkstra，
      有負權要 Bellman-Ford —— 但這題全部的邊都是「一步」。）

【注意答案數的是「單字個數」不是「步數」】

    hit -> hot -> dot -> dog -> cog
    步數 4，單字 5 個 -> 答案是 5

    所以 step 從 1 開始，不是 0。

【本題真正的難點不是 BFS，而是「怎麼快速找鄰居」。】
    直接兩兩比對是 O(N²·L)，在 N = 5000 時會逾時。
    下面會講三種做法。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：beginWord = "hit", endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]
  輸出：5
  說明：hit -> hot -> dot -> dog -> cog，共 5 個單字。

範例 2
  輸入：beginWord = "hit", endWord = "cog",
        wordList = ["hot","dot","dog","lot","log"]
  輸出：0
  說明：endWord "cog" 不在字典裡，不可能到達。""",
 "constraints": [
   "1 ≤ <code>beginWord.length</code> ≤ 10",
   "<code>endWord.length == beginWord.length</code>",
   "1 ≤ <code>wordList.length</code> ≤ 5000",
   "<code>wordList[i].length == beginWord.length</code>",
   "所有單字只包含<strong>小寫英文字母</strong>",
   "<code>beginWord != endWord</code>",
   "<code>wordList</code> 裡<strong>沒有重複</strong>",
 ],
 "idea": [
   ("fig", _P127_FIG, "0 0 640 420"),
   ("c", """BFS 的標準骨架（第 102 題那個）+ 一個「找鄰居」的方法。

    dq = deque([beginWord])
    seen = {beginWord}
    step = 1
    while dq:
        for _ in range(len(dq)):        # 處理一整層
            w = dq.popleft()
            if w == endWord: return step
            for nxt in 鄰居(w):
                if nxt not in seen:
                    seen.add(nxt); dq.append(nxt)
        step += 1
    return 0

【★ 三種「找鄰居」的方法】

    A. 和字典裡每一個字比對
       每次 O(N·L)，總共 O(N²·L)
       N=5000, L=10 -> 2.5 億 ✘ 太慢

    B. 枚舉「把第 i 位改成 a..z」，查集合
       每次 O(26·L)，總共 O(N·26·L)
       N=5000, L=10 -> 130 萬 ✔

    C. 萬用字元桶：預先把每個字拆成 h*t, *ot, ho*
       建索引 O(N·L)，查鄰居 O(L + 桶大小)

    【B 是最常見的答案。】
    C 在「字母表很大」時比較好（B 的 26 會變成字母表大小）。

【★ seen 一定要在「入隊時」加，不是「出隊時」】

    出隊時才加的話，同一個節點可能被重複放進佇列很多次 ——
    最壞會退化成指數級。

    這是 BFS 最常見的效能 bug。"""),
 ],
 "approaches": [
   ap("解法一", "BFS + 枚舉 26 個字母（標準答案）", [
     ("c", S["p127_bfs"]),
     ("h", "為什麼一開始要檢查 <code>endWord not in words</code>？"),
     "因為<strong>題目允許 <code>endWord</code> 不在字典裡</strong>，"
     "那樣就<strong>絕對不可能到達</strong>（序列的最後一個必須在字典裡）。",
     "<strong>不檢查的話 BFS 會白跑一整趟才回 0</strong> —— 答案正確，但浪費。",
     ("h", "<code>w[:i] + c + w[i+1:]</code> 的成本"),
     ("c", """每次建立一個新字串是 O(L)。

    總成本：N 個單字 × L 個位置 × 26 個字母 × O(L) 建字串
          = O(N · L² · 26)

    N=5000, L=10 -> 1300 萬 —— 還行。

【如果 L 很大，這個 L² 會變成瓶頸】，
    那時可以改用「萬用字元桶」（解法三），
    它把 26 這個因子換成「桶裡的單字數」。

【Python 小技巧】：
    "abcdefghijklmnopqrstuvwxyz" 可以寫成
        import string; string.ascii_lowercase

    後者比較清楚，但前者不用 import。""",),
     ("h", "為什麼 <code>step</code> 從 1 開始？"),
     "因為答案數的是<strong>「單字個數」</strong>："
     "只有 <code>beginWord</code> 一個字時就是 1。",
     "<strong>如果 <code>beginWord == endWord</code>（題目保證不會）"
     "應該回 1 —— 這個版本會正確處理。</strong>",
     "<strong>時間 O(N · L² · 26)、空間 O(N · L)。</strong>",
   ], "O(N·L²·26)", "O(N·L)", "每個單字擴展一次", "集合 + 佇列", optimal=True),

   ap("解法二", "雙向 BFS（實測快很多）", [
     ("c", S["p127_bidi"]),
     ("h", "★ 為什麼雙向 BFS 會快這麼多？"),
     ("c", """設分支因子（每個節點的鄰居數）是 b，最短距離是 d。

    單向 BFS：要展開 O(b^d) 個節點
    雙向 BFS：兩邊各走 d/2 -> O(2 · b^(d/2))

    b = 10, d = 6：
        單向：10^6 = 100 萬
        雙向：2 × 10^3 = 2000        【差 500 倍】

    【指數的一半，效果是天差地別。】

    這也是為什麼「兩個人從兩端往中間挖隧道」
    比「一個人從頭挖到尾」快得多。

【★ 關鍵優化：永遠從比較小的那一邊擴展】

    if len(front) > len(back):
        front, back = back, front

    這樣可以避免「某一邊爆炸性成長」把優勢吃掉。

    少了這一行，雙向 BFS 可能比單向還慢。

【★ 相遇的判斷】

    if cand in back:
        return step + 1

    注意是檢查【對面那一層】，不是檢查 seen。

    step 是「front 這一邊已經走了幾個字」，
    碰到 back 裡的字就是再加一個 -> step + 1 ✔"""),
     ("h", "雙向 BFS 的適用條件"),
     ("ul", [
       "<strong>必須知道終點</strong>（不能是「找任何一個滿足條件的」）。",
       "<strong>邊必須是無向的</strong>（或者你能反向走）。",
       "<strong>要能判斷「兩邊碰頭了」</strong>。",
     ]),
     "<strong>這三個條件在這題都滿足</strong>。"
     "<strong>第 126、752、773 題也都可以用雙向 BFS 加速。</strong>",
   ], "O(N·L²·26) 最壞", "O(N·L)", "實測常快數倍", "兩個集合"),

   ap("解法三", "萬用字元桶（字母表很大時最好）", [
     ("c", S["p127_pattern"]),
     ("c", """預處理：把每個單字拆成 L 個「模式」

    hot -> "*ot", "h*t", "ho*"
    dot -> "*ot", "d*t", "do*"

    buckets["*ot"] = ["hot", "dot", "lot"]

    「差一個字母」⟺「至少共用一個模式」✔

查鄰居：
    for i in range(L):
        for nxt in buckets[w[:i] + "*" + w[i+1:]]:
            ...

【複雜度】：
    預處理 O(N · L²)（建 N·L 個長度 L 的字串）
    查詢   O(L + 該模式下的單字數)

    總共 O(N · L²)，【和字母表大小無關】✔

【什麼時候比解法一好？】

    解法一是 O(N · L² · 26)
    解法三是 O(N · L²)

    字母表越大，差距越明顯：
        小寫英文（26）：解法三快約 26 倍（常數上）
        Unicode：      解法一根本不可行

    但解法三要多花 O(N·L²) 的記憶體存桶。

【這是「預處理換查詢」的典型取捨】——
    如果要多次查詢（例如第 126 題要重建路徑），
    預處理的成本更划算。""",),
     "<strong>注意這個版本沒有「分層」</strong>（用 <code>(word, step)</code> 打包），"
     "<strong>兩種寫法都對</strong>。",
   ], "O(N·L²)", "O(N·L²)", "與字母表大小無關", "萬用字元索引"),
 ],
 "compare": (["解法", "時間", "空間", "實測速度", "備註"],
   [["一、BFS + 枚舉 26 字母", "O(N·L²·26)", "O(N·L)", "中", "標準答案"],
    ["二、雙向 BFS", "O(N·L²·26) 最壞", "O(N·L)", "最快", "指數減半"],
    ["三、萬用字元桶", "O(N·L²)", "O(N·L²)", "中", "字母表大時最好"]]),
 "edges": [
   "<strong><code>endWord</code> 不在字典裡</strong> → <code>0</code>。"
   "<strong>一定要先檢查，這是範例 2。</strong>",
   "<strong><code>beginWord</code> 不在字典裡</strong> → 沒關係，題目允許。",
   "<strong>一步就到</strong>（<code>beginWord</code> 和 <code>endWord</code> 差一個字母）→ <code>2</code>。",
   "<strong>完全連不到</strong> → <code>0</code>。",
   "<strong>字典裡有 <code>beginWord</code></strong> → 要記得把它加進 <code>seen</code>，否則會繞回來。",
   "<strong><code>seen</code> 在出隊時才加</strong> → "
   "<strong>同一個節點被重複入隊，最壞退化成指數級。BFS 第一名的效能 bug。</strong>",
   "<strong>用「兩兩比對」找鄰居</strong> → N = 5000 時 O(N²·L) = 2.5 億，逾時。",
   "<strong><code>step</code> 從 0 開始</strong> → 答案少 1（題目要的是單字數）。",
   "<strong>雙向 BFS 忘了「從小的那邊擴展」</strong> → 可能比單向還慢。",
   "<strong><code>beginWord == endWord</code></strong>（題目保證不會）→ "
   "<strong>單向 BFS 回 1，雙向 BFS 回 2 —— 兩者在這個輸入上不一致。</strong>"
   "雙向版是先擴展一層才檢查相遇，所以看不到「起點就是終點」。"
   "如果要讓它安全，開頭加一行 <code>if beginWord == endWord: return 1</code>。",
 ],
 "follow": [
   ("h", "追問一：如果要輸出「所有最短路徑」呢？"),
   "<strong>第 126 題（單詞接龍 II）</strong> —— 那是 Hard，"
   "<strong>要先用 BFS 建出「最短路徑 DAG」，再用 DFS 回溯列出所有路徑。</strong>",
   "<strong>關鍵是不能在 BFS 時就記錄路徑</strong>（路徑數可能是指數級的），"
   "<strong>而要記錄「每個節點的所有前驅」。</strong>",
   ("h", "追問二：為什麼不能用 DFS？"),
   ("c", """DFS 找到的第一條路徑【不保證最短】。

    要用 DFS 求最短路，就得走遍所有路徑再取最小 ——
    那是指數級的。

【無權圖求最短路，BFS 是唯一合理的選擇。】

    對照表：
        無權圖       -> BFS            O(V + E)
        非負權重     -> Dijkstra       O(E log V)
        有負權       -> Bellman-Ford   O(V·E)
        全點對       -> Floyd-Warshall O(V³)
        有啟發函數   -> A*             實務上最快

    這題如果要用 A*，啟發函數可以是
    「和 endWord 不同的字母數」——
    那是一個可採納（admissible）的下界 ✔""",),
   ("h", "追問三：能不能估計一下這個圖有多少邊？"),
   ("c", """最壞情況：所有 N 個單字兩兩相差一個字母
    -> O(N²) 條邊

    但實際上，一個單字最多只有 L × 25 個「差一個字母」的候選，
    所以每個節點的度數 <= 25L = 250（L=10）。

    邊數 <= N × 25L / 2 = 5000 × 250 / 2 = 62.5 萬

【所以這個圖是「稀疏」的】——
    這正是為什麼「枚舉 26 個字母」比「兩兩比對」好：
    前者的成本和「可能的鄰居數」成正比，
    後者和「所有節點數」成正比。

    【在稀疏圖上，永遠不要用「檢查所有節點」的方式找鄰居。】"""),
   ("h", "追問四：如果單字可以有不同長度呢？"),
   "<strong>題目保證都一樣長</strong>。如果不一樣長，"
   "<strong>「差一個字母」的定義就要改成「編輯距離為 1」</strong>"
   "（允許插入、刪除、替換）。",
   "<strong>那時找鄰居要枚舉「插入一個字母」「刪除一個字母」「替換一個字母」</strong>，"
   "<strong>候選數變成 O(L·26 + L + (L+1)·26)</strong>。"
   "<strong>BFS 的骨架完全不用改 —— 這就是「把問題抽象成圖」的好處。</strong>",
 ],
 "related": [
   "<strong>第 126 題 Word Ladder II</strong> —— 輸出所有最短路徑",
   "<strong>第 433 題 Minimum Genetic Mutation</strong> —— 一模一樣的題，換成基因序列",
   "<strong>第 752 題 Open the Lock</strong> —— 同樣適合雙向 BFS",
   "<strong>第 102 題 Level Order Traversal</strong> —— BFS 分層的骨架",
   "<strong>第 200 題 Number of Islands</strong> —— 格子圖上的 BFS",
 ],
 "check": [
   "為什麼答案是「單字個數」而不是「步數」？<code>step</code> 該從幾開始？",
   "「兩兩比對找鄰居」和「枚舉 26 個字母」的複雜度差多少？",
   "<code>seen</code> 為什麼一定要在入隊時加而不是出隊時？",
   "雙向 BFS 為什麼快？「從比較小的那一邊擴展」為什麼重要？",
 ],
})
print("P127 written")

# ==================== 126. Word Ladder II ====================
S["p126"] = '''from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []

        L = len(beginWord)
        # ---- 第一階段：BFS 分層，記錄每個字的「所有前驅」 ----
        parents = defaultdict(set)
        level = {beginWord}
        found = False

        while level and not found:
            words -= level                  # 這一層用過的字，下面不能再用
            nxt = set()
            for w in level:
                for i in range(L):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        cand = w[:i] + c + w[i + 1:]
                        if cand in words:
                            nxt.add(cand)
                            parents[cand].add(w)   # ★ 記所有前驅，不是只記一個
                            if cand == endWord:
                                found = True
            level = nxt

        if not found:
            return []

        # ---- 第二階段：從 endWord 沿著 parents 回溯，列出所有路徑 ----
        res = []

        def back(word, path):
            if word == beginWord:
                res.append(path[::-1])      # path 是倒著建的
                return
            for p in parents[word]:
                back(p, path + [p])

        back(endWord, [endWord])
        return res'''

S["p126_bfs_paths"] = '''from collections import deque

class Solution:
    # 【只適合小輸入】：直接在 BFS 的佇列裡存整條路徑
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in words:
            return []

        L = len(beginWord)
        dq = deque([[beginWord]])
        seen = {beginWord}
        res = []

        while dq and not res:
            # 這一層走過的字，等這一層全部處理完才一起標記
            used = set()
            for _ in range(len(dq)):
                path = dq.popleft()
                w = path[-1]
                for i in range(L):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        cand = w[:i] + c + w[i + 1:]
                        if cand in words and cand not in seen:
                            if cand == endWord:
                                res.append(path + [cand])
                            used.add(cand)
                            dq.append(path + [cand])
            seen |= used

        return res'''


def _p126_ref(begin, end, wl):
    """獨立參考解：列舉所有簡單路徑，取最短的那些。"""
    words = set(wl)
    if end not in words:
        return []
    nodes = list(dict.fromkeys([begin] + list(wl)))
    def adj(a, b):
        return sum(x != y for x, y in zip(a, b)) == 1
    g = {w: [v for v in nodes if v != w and adj(w, v) and v in words] for w in nodes}
    best = [None]
    out = []
    def go(w, path, seen):
        if best[0] is not None and len(path) > best[0]:
            return
        if w == end:
            if best[0] is None or len(path) < best[0]:
                best[0] = len(path); out.clear()
            if len(path) == best[0]:
                out.append(list(path))
            return
        for v in g[w]:
            if v not in seen:
                seen.add(v); path.append(v)
                go(v, path, seen)
                path.pop(); seen.discard(v)
    go(begin, [begin], {begin})
    return out


def _norm(paths):
    return sorted(tuple(p) for p in paths)


_p126 = [S.load(k) for k in ("p126", "p126_bfs_paths")]

for b, e, wl, want in [
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"],
     [["hit", "hot", "dot", "dog", "cog"], ["hit", "hot", "lot", "log", "cog"]]),
    ("hit", "cog", ["hot", "dot", "dog", "lot", "log"], []),
    ("a", "c", ["a", "b", "c"], [["a", "c"]]),
]:
    assert _norm(_p126_ref(b, e, wl)) == _norm(want), ("P126 ref", b, e, wl)
    for sol in _p126:
        assert _norm(sol.findLadders(b, e, list(wl))) == _norm(want), ("P126", b, e, wl, sol)

for _ in range(900):
    L = random.choice([2, 3])
    allw = ["".join(p) for p in itertools.product("abc", repeat=L)]
    wl = random.sample(allw, random.randrange(1, len(allw) + 1))
    b = random.choice(allw)
    e = random.choice([w for w in allw if w != b])
    want = _norm(_p126_ref(b, e, wl))
    for sol in _p126:
        got = _norm(sol.findLadders(b, e, list(wl)))
        assert got == want, ("P126 random", b, e, wl, want, got, sol)
print("P126 solutions OK")

_P126_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">兩階段：先 BFS 建出「最短路徑 DAG」（每個字記住所有前驅），再 DFS 回溯列出全部路徑。</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">階段一：BFS 分層，每層記下「我是從誰來的」</text>
            <g font-size="12" text-anchor="middle">
              <ellipse cx="80" cy="96" rx="32" ry="17" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="80" y="101" fill="var(--gold)">hit</text>
              <ellipse cx="200" cy="96" rx="32" ry="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="200" y="101" fill="var(--accent)">hot</text>
              <ellipse cx="330" cy="64" rx="32" ry="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="330" y="69" fill="var(--accent)">dot</text>
              <ellipse cx="330" cy="130" rx="32" ry="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="330" y="135" fill="var(--accent)">lot</text>
              <ellipse cx="450" cy="64" rx="32" ry="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="450" y="69" fill="var(--accent)">dog</text>
              <ellipse cx="450" cy="130" rx="32" ry="17" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="450" y="135" fill="var(--accent)">log</text>
              <ellipse cx="560" cy="96" rx="32" ry="17" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="560" y="101" fill="#ff8a65">cog</text>
            </g>
            <g stroke="var(--accent)" stroke-width="1.5">
              <line x1="112" y1="96" x2="166" y2="96"/><polygon points="166,96 158,92 158,100" fill="var(--accent)"/>
              <line x1="228" y1="88" x2="296" y2="70"/><polygon points="296,70 288,68 290,76" fill="var(--accent)"/>
              <line x1="228" y1="104" x2="296" y2="124"/><polygon points="296,124 288,118 288,126" fill="var(--accent)"/>
              <line x1="362" y1="64" x2="416" y2="64"/><polygon points="416,64 408,60 408,68" fill="var(--accent)"/>
              <line x1="362" y1="130" x2="416" y2="130"/><polygon points="416,130 408,126 408,134" fill="var(--accent)"/>
              <line x1="482" y1="70" x2="528" y2="88"/><polygon points="528,88 520,82 518,90" fill="var(--accent)"/>
              <line x1="482" y1="124" x2="528" y2="104"/><polygon points="528,104 518,102 520,110" fill="var(--accent)"/>
            </g>
            <text x="560" y="166" fill="#ff8a65" font-size="11" text-anchor="middle">parents[cog] = {dog, log}</text>
            <line x1="20" y1="192" x2="620" y2="192" stroke="var(--border)"/>
            <text x="20" y="220" fill="var(--gold)" font-size="13">階段二：從 cog 沿著箭頭【逆向】走，走出每一條路</text>
            <text x="40" y="248" fill="var(--text-muted)" font-size="12">cog ← dog ← dot ← hot ← hit　　　反轉 → [hit, hot, dot, dog, cog]</text>
            <text x="40" y="272" fill="var(--text-muted)" font-size="12">cog ← log ← lot ← hot ← hit　　　反轉 → [hit, hot, lot, log, cog]</text>
            <line x1="20" y1="296" x2="620" y2="296" stroke="var(--border)"/>
            <text x="20" y="324" fill="#ff8a65" font-size="12">★ 為什麼不能在 BFS 時就把整條路徑存在佇列裡？</text>
            <text x="20" y="348" fill="var(--text-muted)" font-size="12">因為最短路徑的條數可能是【指數級】的 —— 佇列會爆掉。記「前驅」只要 O(V+E) 空間，</text>
            <text x="20" y="372" fill="var(--text-muted)" font-size="12">路徑則是在最後才一條一條「長」出來，該多大就多大，不會提早佔滿記憶體。</text>
            <text x="20" y="402" fill="var(--accent)" font-size="12">★ 另一個關鍵：words -= level —— 用過的整層要一起刪掉，不能邊走邊刪，</text>
            <text x="20" y="426" fill="var(--accent)" font-size="12">否則同一層裡「互為鄰居」的兩個字會互相擋住對方，漏掉路徑。</text>'''

emit({
 "num": 126, "slug": "word-ladder-ii",
 "en": [
   "A <strong>transformation sequence</strong> from word <code>beginWord</code> to word "
   "<code>endWord</code> using a dictionary <code>wordList</code> is a sequence of words "
   "<code>beginWord -&gt; s₁ -&gt; s₂ -&gt; ... -&gt; sₖ</code> such that every adjacent pair "
   "differs by a single letter, every <code>sᵢ</code> is in <code>wordList</code>, and "
   "<code>sₖ == endWord</code>.",
   "Given two words, <code>beginWord</code> and <code>endWord</code>, and a dictionary "
   "<code>wordList</code>, return <em>all the <strong>shortest transformation sequences</strong></em>. "
   "If no such sequence exists, return an empty list. Each sequence should be returned as a "
   "list of words <code>[beginWord, s₁, s₂, ..., sₖ]</code>.",
 ],
 "zh": [
   "規則和第 127 題完全相同，但這次要回傳<strong>所有最短的轉換序列</strong>"
   "（不只是長度）。",
   "如果不存在，回傳空 list。每條序列都要包含 <code>beginWord</code> 和 <code>endWord</code>。",
 ],
 "pre": [
   ("note", "★ 為什麼不能「在 BFS 的佇列裡直接存路徑」？", [
     ("c", """最直覺的想法：佇列裡不放單字，放整條路徑。

    dq = deque([[beginWord]])
    ...
    dq.append(path + [cand])

    能動（解法二就是這樣），但有兩個嚴重問題：

【問題一：記憶體爆炸】

    最短路徑的條數可能是【指數級】的。

    例如字典裡有很多「平行的」轉換路線時，
    路徑數可以到 2^(d/2) 條。

    每條路徑又有 d 個單字 -> 佇列會撐爆記憶體。

【問題二：重複複製】

    path + [cand] 每次都複製整條路徑 -> O(d) 時間。
    走過的節點數 × d -> 常數變得很大。

【正確的做法：只記「前驅」】

    parents[cand] = {所有能一步走到 cand 的前一個字}

    這只要 O(V + E) 空間 —— 和路徑數無關 ✔

    然後在最後用 DFS 沿著 parents 回溯，
    路徑是「需要時才長出來」的。

【這個「BFS 建 DAG + DFS 回溯」的兩階段結構，
  是所有「求全部最短路徑」問題的標準解法。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：beginWord = "hit", endWord = "cog",
        wordList = ["hot","dot","dog","lot","log","cog"]
  輸出：[["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]]

  說明：有兩條長度同為 5 的最短路徑，兩條都要回傳。
        （順序不限。）

範例 2
  輸入：beginWord = "hit", endWord = "cog",
        wordList = ["hot","dot","dog","lot","log"]
  輸出：[]""",
 "constraints": [
   "1 ≤ <code>beginWord.length</code> ≤ 10",
   "<code>endWord.length == beginWord.length</code>",
   "1 ≤ <code>wordList.length</code> ≤ 500",
   "所有單字只包含<strong>小寫英文字母</strong>",
   "<code>beginWord != endWord</code>",
   "<code>wordList</code> 裡<strong>沒有重複</strong>",
   "答案的<strong>總長度不超過 10⁵</strong>",
 ],
 "mid": [
   ("note", "注意最後那個限制", [
     "<strong>「答案的總長度不超過 10⁵」</strong>是題目在保證"
     "<strong>「路徑數不會爆炸」</strong>。",
     "<strong>沒有這個保證的話，光是輸出就不可能完成</strong> —— "
     "因為最短路徑數在最壞情況下是指數級的。",
     "<strong>但你的演算法仍然不應該在「中間過程」就佔用指數級的記憶體</strong>，"
     "這正是「記前驅」比「存路徑」好的理由。",
   ]),
 ],
 "idea": [
   ("fig", _P126_FIG, "0 0 640 444"),
   ("c", """【階段一：BFS 分層，建立「最短路徑 DAG」】

    level = {beginWord}
    while level and not found:
        words -= level                 ★ 整層一起從候選集刪掉
        nxt = set()
        for w in level:
            for 每個鄰居 cand in words:
                nxt.add(cand)
                parents[cand].add(w)   ★ 記【所有】前驅
                if cand == endWord: found = True
        level = nxt

【階段二：從 endWord 沿著 parents 回溯】

    def back(word, path):
        if word == beginWord:
            res.append(path[::-1])
            return
        for p in parents[word]:
            back(p, path + [p])

    back(endWord, [endWord])

【★★ 為什麼是 words -= level（整層一起刪）而不是邊走邊刪？】

    如果在 for 迴圈裡就 words.discard(cand)：

        同一層裡的兩個字 A 和 B，
        如果 A 和 B 都能走到 C，
        那麼第一個處理的（假設是 A）會把 C 從 words 刪掉，
        B 就看不到 C 了 -> parents[C] 少了 B ✘

        -> 漏掉「經過 B」的那些路徑。

    整層處理完再一起刪，就能保證
    「這一層的每個字都有機會把自己登記成 C 的前驅」✔

【★ 為什麼要刪？（不刪會怎樣）】

    不刪的話會走回上一層，
    parents 裡會出現「反方向」的邊 -> DFS 回溯時無窮迴圈。

    刪掉「已經走過的層」等於「只保留往前的邊」——
    這樣 parents 構成的就是一個 DAG ✔

【★ 為什麼 found 了還要把這一層走完？】

    因為同一層裡可能有【多條】路徑同時到達 endWord。

    while level and not found 是在「這一層全部處理完」之後
    才檢查 found —— 所以不會漏 ✔"""),
 ],
 "approaches": [
   ap("解法一", "BFS 建 DAG + DFS 回溯（標準答案）", [
     ("c", S["p126"]),
     ("h", "兩階段的複雜度"),
     ("c", """階段一（BFS）：
    每個單字被擴展一次，每次枚舉 L × 26 個候選
    -> O(N · L² · 26)

階段二（DFS 回溯）：
    O(所有路徑的總長度) = O(答案的大小)

    題目保證答案總長度 <= 10^5，所以這一步是可控的 ✔

【總空間】：
    parents 最多 O(V + E) = O(N · L · 26)
    —— 和「路徑數」完全無關 ✔

    這就是比「佇列存路徑」好的地方。""",),
     ("h", "為什麼 <code>parents</code> 用 <code>set</code> 而不是 <code>list</code>？"),
     "<strong>因為同一個前驅可能被加入多次</strong>"
     "（例如同一層的 <code>w</code> 透過不同的字母位置變成同一個 <code>cand</code>）。",
     "<strong>用 <code>list</code> 的話會產生重複路徑</strong> —— "
     "<strong>答案裡會有一模一樣的兩條序列。</strong>",
     ("h", "<code>path[::-1]</code> 別忘了"),
     "<strong>回溯是從 <code>endWord</code> 往回走的，所以 <code>path</code> 是倒著建的。</strong>"
     "<strong>忘記反轉的話，每條路徑都是反的。</strong>",
     "<strong>也可以改成「從 <code>beginWord</code> 正著 DFS」</strong>，"
     "但那要先把 <code>parents</code> 反轉成 <code>children</code> —— 多一步，不如直接反轉路徑。",
   ], "O(N·L²·26 + 答案大小)", "O(N·L·26)", "BFS + 回溯", "前驅圖（與路徑數無關）", optimal=True),

   ap("解法二", "BFS 佇列直接存路徑（只適合小輸入）", [
     ("c", S["p126_bfs_paths"]),
     ("c", """優點：不用兩階段，一個迴圈寫完。
缺點：最壞情況下佇列會存指數級的路徑。

【★ 注意 seen 的處理方式】

    used = set()
    for ...（這一層）:
        ...
        used.add(cand)
    seen |= used                  ← 整層處理完才一起標記

    和解法一的 words -= level 是同一個道理：

        如果在迴圈裡就 seen.add(cand)，
        同一層的其他路徑就找不到 cand 了 -> 漏路徑 ✘

【★ while dq and not res】

    一旦 res 非空（找到了最短長度），
    就不再往下一層走 —— 因為更深的路徑一定更長。

【什麼時候可以用這個版本？】

    ✔ 字典很小（本題 N <= 500，其實勉強可以）
    ✔ 你確定路徑數不多
    ✔ 寫比賽、追求快速寫完

    ✘ 正式面試（面試官會問空間複雜度）
    ✘ 路徑數可能爆炸的場合""",),
     "<strong>本題 <code>N ≤ 500</code> 且題目保證答案總長度 <code>≤ 10⁵</code>，"
     "所以這個版本實際上會過。</strong>"
     "<strong>但它的最壞空間複雜度說不出口。</strong>",
   ], "O(N·L²·26 + 答案大小)", "O(路徑數 × L)", "同上", "佇列裡的所有路徑"),
 ],
 "compare": (["解法", "時間", "空間", "最壞會爆嗎", "備註"],
   [["一、BFS 建 DAG + DFS", "O(N·L²·26 + 答案)", "O(N·L·26)", "✘", "標準答案"],
    ["二、佇列存路徑", "O(N·L²·26 + 答案)", "O(路徑數 × L)", "✔", "小輸入可用"]]),
 "edges": [
   "<strong><code>endWord</code> 不在字典裡</strong> → <code>[]</code>。",
   "<strong>一步就到</strong> → <code>[[begin, end]]</code>。",
   "<strong>有多條等長最短路徑</strong> → 全部都要回傳（範例 1）。",
   "<strong>完全連不到</strong> → <code>[]</code>。",
   "<strong>邊走邊刪 <code>words</code>（而不是整層一起刪）</strong> → "
   "<strong>漏掉路徑。本題第一名的 bug，而且只在「同層互為鄰居」時才出現。</strong>",
   "<strong>完全不刪 <code>words</code></strong> → "
   "<code>parents</code> 出現反向邊，DFS 回溯時無窮迴圈。",
   "<strong><code>parents</code> 用 <code>list</code> 而不是 <code>set</code></strong> → 產生重複路徑。",
   "<strong>忘了 <code>path[::-1]</code></strong> → 每條路徑都是反的。",
   "<strong>找到 <code>endWord</code> 就立刻 <code>break</code> 出這一層</strong> → "
   "漏掉同一層的其他路徑。",
 ],
 "follow": [
   ("h", "追問一：這個「兩階段」結構還能用在哪裡？"),
   ("c", """任何「求全部最優解」的最短路徑問題：

  126  單詞接龍 II            （本題）
  1129 顏色交替的最短路徑     記前驅，回溯
  1857 有向圖中最大顏色值     DAG 上的 DP

  一般化：
    Dijkstra 求「所有最短路」-> 同樣記前驅
    （只是要判斷 dist[v] == dist[u] + w(u,v) 才算前驅）

【核心觀念】：

    「最短路徑 DAG」= 只保留「在某條最短路上」的那些邊。

    建好之後，
        數路徑數 -> DAG 上的 DP，O(V+E)
        列出路徑 -> DFS，O(答案大小)
        求最小/最大某個屬性 -> DAG 上的 DP

    【把「最短路」和「列舉路徑」分成兩階段，
      是處理這類問題的通用架構。】""",),
   ("h", "追問二：能不能用雙向 BFS？"),
   "<strong>可以，而且會快很多</strong> —— 但<strong>實作複雜度大幅上升</strong>。",
   "<strong>難點在於「兩邊碰頭時，要把兩側的前驅圖正確接起來」</strong>，"
   "而且<strong>要分清楚哪一邊是正向、哪一邊是反向</strong>（路徑方向會反）。",
   "<strong>面試時提一句「可以用雙向 BFS 加速，但接前驅圖的細節很多」就夠了</strong> —— "
   "<strong>沒有人會要求你在白板上寫出來。</strong>",
   ("h", "追問三：如果要「數有幾條最短路徑」而不是列出來呢？"),
   "<strong>那就簡單多了 —— 在 BFS 時順便做計數 DP</strong>：",
   ("c", """count[beginWord] = 1
處理 cand 時：
    count[cand] += count[w]        （對所有前驅 w 累加）

答案 = count[endWord]

O(V + E)，【完全不需要第二階段】。

【「數數量」永遠比「列出來」便宜得多】——
    前者是多項式，後者可能是指數。

    第 95/96 題（生成所有 BST vs 數 BST）
    是同一個對比。""",),
   ("h", "追問四：為什麼 <code>words -= level</code> 要放在迴圈開頭而不是結尾？"),
   ("c", """放開頭：
    words -= level        # 先把「這一層自己」刪掉
    for w in level: ...   # 再去找鄰居

    這樣找鄰居時，level 裡的字已經不在 words 了
    -> 不會走回同一層 ✔

放結尾（先找鄰居再刪）：
    for w in level:
        for cand in ...:
            if cand in words: ...    ← level 裡的字還在 words！

    -> 同一層的字會互相當成鄰居
    -> parents 裡出現「同層之間的邊」
    -> 那不是最短路徑的一部分 ✘

【「什麼時候把節點標記成已訪問」
  是 BFS 最容易出錯的細節，
  而在「求全部路徑」時尤其致命。】"""),
 ],
 "related": [
   "<strong>第 127 題 Word Ladder</strong> —— 只要長度，先學那題",
   "<strong>第 433 題 Minimum Genetic Mutation</strong> —— 同一題換皮",
   "<strong>第 1129 題 Shortest Path with Alternating Colors</strong> —— 同樣記前驅",
   "<strong>第 113 題 Path Sum II</strong> —— DFS 回溯列出所有路徑",
 ],
 "check": [
   "為什麼不能在 BFS 的佇列裡直接存整條路徑？",
   "<code>words -= level</code> 為什麼要「整層一起刪」而不是邊走邊刪？會漏掉什麼？",
   "<code>parents</code> 為什麼用 <code>set</code> 而不是 <code>list</code>？",
   "如果只要「數有幾條最短路徑」，該怎麼改？複雜度差多少？",
 ],
})
print("P126 written")

# ==================== 128. Longest Consecutive Sequence ====================
S["p128"] = '''class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for x in s:
            if x - 1 in s:
                continue                # ★ 不是序列的起點，跳過
            # x 是某段連續序列的開頭，往右數到底
            y = x
            while y + 1 in s:
                y += 1
            best = max(best, y - x + 1)

        return best'''

S["p128_sort"] = '''class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))        # 去重後排序
        best = cur = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur += 1
                best = max(best, cur)
            else:
                cur = 1
        return best'''

S["p128_union"] = '''class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        parent = {}
        size = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]   # 路徑壓縮
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:             # 按大小合併
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]

        for x in nums:
            if x in parent:
                continue
            parent[x] = x
            size[x] = 1
            for nb in (x - 1, x + 1):
                if nb in parent:
                    union(x, nb)

        return max(size[find(x)] for x in parent) if parent else 0'''


def _p128_ref(nums):
    """獨立參考解：排序去重後掃一遍。"""
    if not nums:
        return 0
    a = sorted(set(nums))
    best = cur = 1
    for i in range(1, len(a)):
        cur = cur + 1 if a[i] == a[i - 1] + 1 else 1
        best = max(best, cur)
    return best


_p128 = [S.load(k) for k in ("p128", "p128_sort", "p128_union")]

for nums, want in [
    ([100, 4, 200, 1, 3, 2], 4),
    ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ([], 0),
    ([1], 1),
    ([1, 1, 1], 1),
    ([-3, -2, -1, 5], 3),
]:
    assert _p128_ref(nums) == want, ("P128 ref", nums)
    for sol in _p128:
        assert sol.longestConsecutive(list(nums)) == want, ("P128", nums, sol)

for _ in range(6000):
    n = random.randrange(0, 20)
    nums = [random.randint(-12, 12) for _ in range(n)]
    want = _p128_ref(nums)
    for sol in _p128:
        assert sol.longestConsecutive(list(nums)) == want, ("P128 random", nums, want, sol)
print("P128 solutions OK")

_P128_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ O(n) 的關鍵：只從「序列的起點」開始往右數。起點 = 集合裡沒有 x−1 的那個 x。</text>
            <text x="20" y="50" fill="var(--gold)" font-size="13">nums = [100, 4, 200, 1, 3, 2]　→　set = {1, 2, 3, 4, 100, 200}</text>
            <g font-size="13" text-anchor="middle">
              <rect x="60" y="72" width="52" height="30" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="86" y="92" fill="var(--gold)">1</text>
              <rect x="122" y="72" width="52" height="30" fill="none" stroke="var(--border)"/><text x="148" y="92" fill="var(--text-muted)">2</text>
              <rect x="184" y="72" width="52" height="30" fill="none" stroke="var(--border)"/><text x="210" y="92" fill="var(--text-muted)">3</text>
              <rect x="246" y="72" width="52" height="30" fill="none" stroke="var(--border)"/><text x="272" y="92" fill="var(--text-muted)">4</text>
              <rect x="330" y="72" width="62" height="30" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="361" y="92" fill="var(--gold)">100</text>
              <rect x="430" y="72" width="62" height="30" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="461" y="92" fill="var(--gold)">200</text>
            </g>
            <text x="86" y="124" fill="var(--gold)" font-size="11" text-anchor="middle">起點 ✔</text>
            <text x="148" y="124" fill="var(--text-muted)" font-size="11" text-anchor="middle">1 在 → 跳過</text>
            <text x="210" y="124" fill="var(--text-muted)" font-size="11" text-anchor="middle">2 在 → 跳過</text>
            <text x="272" y="124" fill="var(--text-muted)" font-size="11" text-anchor="middle">3 在 → 跳過</text>
            <text x="361" y="124" fill="var(--gold)" font-size="11" text-anchor="middle">起點 ✔</text>
            <text x="461" y="124" fill="var(--gold)" font-size="11" text-anchor="middle">起點 ✔</text>
            <text x="20" y="160" fill="var(--accent)" font-size="12">從 1 往右數：1→2→3→4，長度 4。從 100 數：長度 1。從 200 數：長度 1。答案 = 4</text>
            <line x1="20" y1="184" x2="620" y2="184" stroke="var(--border)"/>
            <text x="20" y="212" fill="#ff8a65" font-size="13">★ 為什麼總時間是 O(n) 而不是 O(n²)？</text>
            <text x="20" y="240" fill="var(--text-muted)" font-size="12">看起來有巢狀迴圈（外層 for、內層 while），很像 O(n²)。但關鍵是：</text>
            <text x="40" y="268" fill="var(--accent)" font-size="12">內層 while 只在「x 是起點」時才會跑。</text>
            <text x="40" y="294" fill="var(--accent)" font-size="12">而每一段連續序列只有【一個】起點，內層恰好把那一段走完一次。</text>
            <text x="40" y="320" fill="var(--gold)" font-size="12">所以所有內層迴圈的總步數 = 所有段的長度總和 = n。</text>
            <text x="20" y="352" fill="var(--text-muted)" font-size="12">外層 O(n) + 內層總共 O(n) = O(n) ✔　這又是一次「總量分析」（和第 103 題一樣）。</text>
            <text x="20" y="386" fill="#ff8a65" font-size="12">拿掉那一行 if x - 1 in s: continue，就真的變成 O(n²) —— 例如 [1,2,3,…,n]：</text>
            <text x="20" y="410" fill="#ff8a65" font-size="12">從 1 數 n 步、從 2 數 n−1 步、… 總共 n(n+1)/2 步。一行之差，天壤之別。</text>'''

emit({
 "num": 128, "slug": "longest-consecutive-sequence",
 "en": [
   "Given an unsorted array of integers <code>nums</code>, return <em>the length of the longest "
   "consecutive elements sequence</em>.",
   "You must write an algorithm that runs in <code>O(n)</code> time.",
 ],
 "zh": [
   "給你一個<strong>沒有排序</strong>的整數陣列 <code>nums</code>，"
   "找出<strong>最長的連續數字序列</strong>的長度。",
   "（「連續」是指數值上連續，例如 <code>1,2,3,4</code>；"
   "<strong>它們在陣列裡的位置不需要相鄰</strong>。）",
   "<strong>你必須寫出時間複雜度 <code>O(n)</code> 的演算法。</strong>",
 ],
 "pre": [
   ("note", "★ 「必須 O(n)」把排序解排除了", [
     ("c", """排序後掃一遍是最直覺的做法（解法二），
O(n log n)，而且很短。

    但題目明確要求 O(n) ——
    所以排序解【雖然能通過 LeetCode 的評測】，
    卻不是題目想要的答案。

【面試時一定要寫 O(n) 的版本。】

    可以先說「排序是 O(n log n)，但題目要 O(n)，
    我用雜湊集合來做」，然後寫解法一。

【O(n) 的關鍵洞察】：

    把所有數字丟進 set（查詢 O(1)）。

    然後對每個數字 x，往右數 x+1, x+2, ...
    —— 但【只從「起點」開始數】。

    x 是起點 ⟺ x - 1 不在 set 裡

    這一行 if x - 1 in s: continue
    就是 O(n) 和 O(n²) 的分界線。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：nums = [100,4,200,1,3,2]
  輸出：4
  說明：最長的連續序列是 [1,2,3,4]，長度 4。
        注意它們在陣列裡的位置是 4, 1, 3, 2 —— 完全不相鄰。

範例 2
  輸入：nums = [0,3,7,2,5,8,4,6,0,1]
  輸出：9
  說明：0..8 共 9 個數（0 出現兩次，只算一次）。""",
 "constraints": [
   "0 ≤ <code>nums.length</code> ≤ 10⁵",
   "−10⁹ ≤ <code>nums[i]</code> ≤ 10⁹",
 ],
 "mid": [
   ("note", "數值範圍 ±10⁹ 排除了「開一個大陣列」的作法", [
     "<strong>不能開一個 <code>bool[2×10⁹]</code> 的桶。</strong>",
     "<strong>必須用雜湊集合</strong>（<code>set</code> / <code>HashSet</code>），"
     "它的空間只和「實際有幾個數字」成正比。",
     "<strong>另外注意「陣列可以是空的」</strong> → 答案 0。",
   ]),
 ],
 "idea": [
   ("fig", _P128_FIG, "0 0 640 430"),
   ("c", """s = set(nums)
for x in s:
    if x - 1 in s:      ★ 不是起點就跳過
        continue
    y = x
    while y + 1 in s:
        y += 1
    best = max(best, y - x + 1)

【★★ 為什麼這是 O(n)？（這是本題唯一的考點）】

    表面上看是「for 裡面包 while」-> 像 O(n²)

    但：
        內層 while 只在「x 是某段的起點」時才執行。
        每一段連續序列【只有一個起點】。
        從那個起點出發，while 恰好走過「這一段的長度」步。

    所以所有 while 的總步數
        = Σ 每一段的長度
        = n            ✔

    外層 O(n) + 內層總共 O(n) = O(n)

    【每個數字最多被內層 while 訪問【一次】。】

【這叫做「總量分析」（aggregate analysis）】——

    和第 103 題（每層反轉）、
    第 99 題（Morris 走訪）、
    第 84 題（單調堆疊）用的是同一種論證。

    看到「巢狀迴圈但總量有界」，
    不要直接下 O(n²) 的結論。

【★ 拿掉那一行會怎樣？】

    nums = [1, 2, 3, ..., n]

    從 1 數 n 步、從 2 數 n-1 步、…、從 n 數 1 步
    -> n(n+1)/2 = O(n²)

    n = 10⁵ 時是 50 億步 -> 一定逾時。

    【一行 continue，就是 O(n) 和 O(n²) 的差別。】"""),
 ],
 "approaches": [
   ap("解法一", "雜湊集合 + 只從起點數（標準答案）", [
     ("c", S["p128"]),
     "<strong>九行，O(n) 時間、O(n) 空間。</strong>"
     "<strong>這是題目要的答案。</strong>",
     ("h", "為什麼迴圈跑 <code>s</code> 而不是 <code>nums</code>？"),
     ("c", """for x in s:      ✔ 遍歷去重後的集合
for x in nums:   也對，但會重複處理相同的數字

    nums = [1, 1, 1, ..., 1]（10^5 個 1）

    跑 nums：外層跑 10^5 次（雖然每次都很快）
    跑 s：   外層只跑 1 次

    兩者都是 O(n)，但跑 s 的常數小很多。

【而且跑 s 語意更清楚】：
    「對每個【不同的】數字，檢查它是不是起點」。""",),
     ("h", "重複數字會不會出問題？"),
     "<strong>不會</strong> —— <code>set</code> 自動去重。",
     "<strong>範例 2 的 <code>0</code> 出現兩次，但只算一個</strong> —— "
     "<strong>「連續序列」數的是不同的數值。</strong>",
     ("h", "空陣列"),
     "<code>s</code> 是空的 → 迴圈不跑 → 回傳 <code>best = 0</code> ✔ "
     "<strong>不用特判。</strong>",
   ], "O(n)", "O(n)", "每個數字最多被內層訪問一次", "雜湊集合", optimal=True),

   ap("解法二", "排序後掃一遍（不符合題目要求，但值得會）", [
     ("c", S["p128_sort"]),
     "<strong>O(n log n) 時間、O(n) 空間（去重的 set）。</strong>",
     ("c", """【為什麼要先 set 去重？】

    nums = [1, 1, 2]

    不去重：排序後 [1, 1, 2]
        i=1: nums[1] == nums[0] + 1? 1 == 2? 否 -> cur = 1  ✘ 斷掉了
        i=2: nums[2] == nums[1] + 1? 2 == 2? 是 -> cur = 2

        答案 2 —— 碰巧對了。

    但 nums = [1, 1, 1, 2]：
        重複的 1 會一直把 cur 重設成 1，
        最後還是能得到 2 —— 也碰巧對。

    其實不去重也可以，只要把「相等」的情況特別處理：

        if a[i] == a[i-1]: continue          # 跳過重複
        elif a[i] == a[i-1] + 1: cur += 1
        else: cur = 1

    但先去重比較乾淨，也不容易寫錯。

【這個解法什麼時候比較好？】

    ✔ 記憶體很緊（sorted 可以原地）
    ✔ 資料本來就排好了 -> O(n)
    ✔ 你不需要嚴格的 O(n)

    ✘ 題目明確要求 O(n)（本題）""",),
   ], "O(n log n)", "O(n)", "排序主導", "去重的集合"),

   ap("解法三", "並查集（想法完整，但殺雞用牛刀）", [
     ("c", S["p128_union"]),
     ("h", "把「連續」看成「連通」"),
     ("c", """把每個數字當成一個節點，
把 x 和 x+1 之間連一條邊 ——
那麼「最長連續序列」就是「最大連通塊的大小」。

    用並查集維護連通塊：
        每讀進一個 x，就和 x-1、x+1 合併（如果它們存在）。

    最後取最大的 size。

【複雜度】：
    帶「路徑壓縮 + 按大小合併」的並查集，
    每次操作的攤還成本是 O(α(n))，
    α 是反阿克曼函數 —— 對任何實際的 n 都 <= 4。

    所以總共是 O(n · α(n)) ≈ O(n) ✔

【為什麼還是不建議寫這個？】

    ✘ 程式碼是解法一的三倍長
    ✘ 常數比較大（雜湊 + 路徑壓縮）
    ✘ 這題根本不需要「動態合併」的能力

【但它有一個獨特的優勢】：

    如果題目改成「數字是【一個一個】進來的，
    每次都要回答目前的最長連續長度」——

    那就【必須】用並查集（或類似的動態結構），
    因為解法一每次都要重算。

    【選資料結構時，要看「有沒有動態更新的需求」。】"""),
     "<strong>放在這裡是為了展示「連續 ⟺ 連通」這個視角</strong>，"
     "<strong>以及並查集的標準寫法（路徑壓縮 + 按大小合併）。</strong>",
   ], "O(n·α(n))", "O(n)", "並查集的攤還成本", "parent + size"),
 ],
 "compare": (["解法", "時間", "空間", "符合題目要求", "備註"],
   [["一、集合 + 只從起點數", "O(n)", "O(n)", "✔", "標準答案，九行"],
    ["二、排序後掃描", "O(n log n)", "O(n)", "✘", "最好想"],
    ["三、並查集", "O(n·α(n))", "O(n)", "✔", "動態版才需要"]]),
 "edges": [
   "<strong>空陣列</strong> → <code>0</code>。<strong>解法一不用特判，解法二要。</strong>",
   "<strong>單一元素</strong> → <code>1</code>。",
   "<strong>全部相同</strong> <code>[1,1,1]</code> → <code>1</code>（去重後只有一個數）。",
   "<strong>完全不連續</strong> <code>[1,3,5]</code> → <code>1</code>。",
   "<strong>有負數</strong> <code>[-3,-2,-1,5]</code> → <code>3</code>。"
   "<strong>負數完全不影響邏輯（用的是 <code>x-1 in s</code> 而不是索引）。</strong>",
   "<strong>拿掉 <code>if x - 1 in s: continue</code></strong> → "
   "<strong><code>[1..10⁵]</code> 上退化成 O(n²)，逾時。本題唯一的考點。</strong>",
   "<strong>用 <code>list</code> 而不是 <code>set</code> 做 <code>in</code> 查詢</strong> → "
   "<strong><code>in</code> 變成 O(n)，整體 O(n²)。</strong>",
   "<strong>數值到 ±10⁹</strong> → 不能開桶陣列，必須用雜湊。",
 ],
 "follow": [
   ("h", "追問一：如果要輸出「那一段序列」而不是長度呢？"),
   "<strong>在更新 <code>best</code> 時記下 <code>(x, y)</code></strong>，"
   "最後回傳 <code>list(range(x, y+1))</code>。",
   "<strong>幾乎不增加成本</strong> —— <strong>因為起點和終點在計算過程中本來就有了。</strong>",
   ("h", "追問二：如果要「最長的等差數列」呢？"),
   ("c", """那難很多。

    「連續」= 公差固定是 1 -> 可以用 x+1 in s 直接跳。
    「等差」= 公差未知     -> 要枚舉公差。

    第 1027 題（最長等差數列）的解法是 DP：
        dp[i][d] = 以 nums[i] 結尾、公差 d 的最長長度

        dp[i][d] = dp[j][d] + 1   （nums[i] - nums[j] == d）

    O(n²) 時間、O(n²) 空間。

【為什麼差這麼多？】

    公差固定時，「下一個是誰」是【確定的】-> O(1) 查表。
    公差未知時，要對每一對 (i, j) 都考慮 -> O(n²)。

    【「有沒有唯一的下一步」常常決定一個問題的難度。】""",),
   ("h", "追問三：如果數字是「串流」進來的，每次都要回答呢？"),
   "<strong>那就必須用並查集（解法三）</strong> —— "
   "<strong>它支援「增量加入」，每次 O(α(n))。</strong>",
   ("c", """也可以用「區間端點映射」的技巧：

    用一個 dict 記錄「以某個數為端點的區間長度」

    加入 x 時：
        left  = d.get(x - 1, 0)      左邊那段有多長
        right = d.get(x + 1, 0)      右邊那段有多長
        total = left + right + 1

        d[x] = total                  （其實不重要）
        d[x - left] = total           ★ 更新左端點
        d[x + right] = total          ★ 更新右端點

        best = max(best, total)

【只需要更新「兩個端點」，中間的值不會被查到】——
    因為任何新來的數字，只可能接在某段的【端點】旁邊。

    O(1) 每次插入，比並查集還簡單。
    這是第 128 題的一個很漂亮的變體解法。""",),
   ("h", "追問四：「總量分析」還有哪些例子？"),
   ("ul", [
     "<strong>本題</strong>：內層 while 的總步數 = n",
     "<strong>第 84 題 柱狀圖最大矩形</strong>：單調堆疊，每個元素進出各一次",
     "<strong>第 99/114 題 Morris 走訪</strong>：每條邊最多被走常數次",
     "<strong>第 103 題 鋸齒層序</strong>：每層反轉的總成本 = n",
     "<strong>動態陣列的 append</strong>：偶爾 O(n) 擴容，攤還 O(1)",
   ]),
   "<strong>共同特徵：「單次可能很貴，但總量有上界」。</strong>"
   "<strong>看到巢狀迴圈時，先問「內層總共會跑幾次」而不是「內層最多跑幾次」。</strong>",
 ],
 "related": [
   "<strong>第 1027 題 Longest Arithmetic Subsequence</strong> —— 公差未知的版本",
   "<strong>第 300 題 Longest Increasing Subsequence</strong> —— 遞增但不要求連續",
   "<strong>第 200 題 Number of Islands</strong> —— 另一個可用並查集的題",
   "<strong>第 84 題 Largest Rectangle in Histogram</strong> —— 同樣的總量分析",
 ],
 "check": [
   "<code>if x - 1 in s: continue</code> 這一行為什麼是 O(n) 和 O(n²) 的分界？",
   "為什麼「for 裡面包 while」在這裡還是 O(n)？請用總量分析說明。",
   "重複的數字為什麼不影響答案？",
   "如果數字是串流進來的、每次都要回答，該用什麼結構？",
 ],
})
print("P128 written")

# ==================== 129. Sum Root to Leaf Numbers ====================
def _build(spec):
    if spec is None:
        return None
    v, l, r = spec
    return TreeNode(v, _build(l), _build(r))


def _rand_digit_tree(n):
    if n == 0:
        return None
    left = random.randrange(0, n)
    return TreeNode(random.randint(0, 9), _rand_digit_tree(left), _rand_digit_tree(n - 1 - left))


S["p129_dfs"] = '''class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def go(node, cur: int) -> int:
            if not node:
                return 0
            cur = cur * 10 + node.val       # 把自己接到數字後面
            if not node.left and not node.right:
                return cur                  # 走到葉節點，這就是一個完整的數字
            return go(node.left, cur) + go(node.right, cur)

        return go(root, 0)'''

S["p129_iter"] = '''class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        total = 0
        stack = [(root, root.val)]
        while stack:
            node, cur = stack.pop()
            if not node.left and not node.right:
                total += cur
            if node.left:
                stack.append((node.left, cur * 10 + node.left.val))
            if node.right:
                stack.append((node.right, cur * 10 + node.right.val))

        return total'''

S["p129_paths"] = '''class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # 先收集所有「根到葉」的數字字串，再加起來（最直白）
        nums = []

        def go(node, path):
            if not node:
                return
            path = path + str(node.val)
            if not node.left and not node.right:
                nums.append(int(path))
                return
            go(node.left, path)
            go(node.right, path)

        go(root, "")
        return sum(nums)'''


def _p129_ref(root):
    """獨立參考解：列出所有根到葉的數字字串。"""
    if root is None:
        return 0
    out = []
    def go(nd, path):
        path = path + str(nd.val)
        if not nd.left and not nd.right:
            out.append(int(path)); return
        if nd.left:
            go(nd.left, path)
        if nd.right:
            go(nd.right, path)
    go(root, "")
    return sum(out)


_p129 = [S.load(k) for k in ("p129_dfs", "p129_iter", "p129_paths")]

for spec, want in [
    ([1, [2, None, None], [3, None, None]], 25),
    ([4, [9, [5, None, None], [1, None, None]], [0, None, None]], 1026),
    ([0, None, None], 0),
    ([1, [0, None, None], None], 10),
    (None, 0),
]:
    t = _build(spec)
    assert _p129_ref(t) == want, ("P129 ref", spec, _p129_ref(t))
    for sol in _p129:
        assert sol.sumNumbers(_build(spec)) == want, ("P129", spec, sol)

for _ in range(5000):
    t = _rand_digit_tree(random.randrange(0, 11))
    want = _p129_ref(t)
    for sol in _p129:
        assert sol.sumNumbers(t) == want, ("P129 random", want, sol)
print("P129 solutions OK")

emit({
 "num": 129, "slug": "sum-root-to-leaf-numbers",
 "en": [
   "You are given the <code>root</code> of a binary tree containing digits from <code>0</code> "
   "to <code>9</code> only.",
   "Each root-to-leaf path in the tree represents a number.",
   ("raw", "<ul><li>For example, the root-to-leaf path <code>1 -&gt; 2 -&gt; 3</code> "
           "represents the number <code>123</code>.</li></ul>"),
   "Return <em>the total sum of all root-to-leaf numbers</em>. Test cases are generated so that "
   "the answer will fit in a <strong>32-bit</strong> integer.",
   "A <strong>leaf</strong> node is a node with no children.",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，每個節點的值都是 <code>0</code> 到 <code>9</code> 的數字。",
   "<strong>每一條從根到葉的路徑，都代表一個數字</strong>"
   "（例如路徑 <code>1 → 2 → 3</code> 代表數字 <code>123</code>）。",
   "回傳<strong>所有這些數字的總和</strong>。測資保證答案能裝進 32 位元整數。",
 ],
 "pre": [
   ("note", "「把路徑當成數字往下傳」", [
     ("c", """核心只有一行：

    cur = cur * 10 + node.val

    這就是「在數字後面接一位」的標準寫法。

    根是 1        -> cur = 0*10 + 1 = 1
    走到 2        -> cur = 1*10 + 2 = 12
    走到 3        -> cur = 12*10 + 3 = 123    ✔

【為什麼用整數而不是字串？】

    字串版（解法三）：path = path + str(node.val)，最後 int(path)

    整數版：cur = cur * 10 + node.val

    整數版：
        ✔ 不用建字串（省時省空間）
        ✔ 不用最後再轉換
        ✔ 沒有前導零的問題（0 * 10 + 5 = 5）

    字串版：
        ✔ 比較直白
        ✘ 每層都建新字串 -> O(h) 每次

【「cur * 進位 + 新的一位」是所有進位制轉換的基本動作】——

    第 8 題（字串轉整數）、
    第 171 題（Excel 欄位序號）、
    第 2 題（兩數相加）
    用的都是它。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,2,3]

        1
       / \\
      2   3

  輸出：25
  說明：路徑 1->2 代表 12，路徑 1->3 代表 13。
        12 + 13 = 25

範例 2
  輸入：root = [4,9,0,5,1]

          4
         / \\
        9   0
       / \\
      5   1

  輸出：1026
  說明：495 + 491 + 40 = 1026""",
 "constraints": [
   "樹的節點數在 <code>[1, 1000]</code> 之間",
   "0 ≤ <code>Node.val</code> ≤ 9",
   "樹的深度不超過 <code>10</code>",
 ],
 "mid": [
   ("note", "「深度不超過 10」這個限制在說什麼", [
     "<strong>所以每個數字最多 10 位</strong> —— "
     "最大約 <code>9999999999</code>，已經超過 <code>2³¹</code>。",
     "<strong>但題目又說「答案裝得進 32 位元整數」</strong> —— "
     "這表示測資不會真的給出 10 位數的路徑。",
     "<strong>在 Java / C++ 裡還是要小心</strong>；Python 的整數無限大，不受影響。",
     "<strong>深度 ≤ 10 也保證了遞迴不會太深。</strong>",
   ]),
 ],
 "idea": [
   ("c", """DFS，把「目前累積的數字」當參數往下傳：

    def go(node, cur):
        if not node: return 0
        cur = cur * 10 + node.val
        if 是葉節點: return cur          ← 一條完整的路徑
        return go(left, cur) + go(right, cur)

【★ 三個 base case 的分工】

    1. not node       -> 0
       「此路不通」，對加法來說 0 是單位元素 ✔

    2. 是葉節點       -> cur
       一條完整的路徑，貢獻這個數字

    3. 其他           -> 左邊的和 + 右邊的和

【為什麼空節點回 0 而不是 cur？】

    因為「走到 None」不代表「完成了一條路徑」。

    例如：
        1
       /
      2

    go(1, 0) -> cur = 1，不是葉節點
        -> go(2, 1) + go(None, 1)
             ^^^^^^^   ^^^^^^^^^^
             = 12       必須是 0，不能是 1

    回傳 cur 的話會多算一個 1 -> 答案變成 13 ✘

    【這和第 112 題「走到 None ≠ 走到葉節點」是完全同一個陷阱。】

    對照表（base case 該回什麼）：
        求和      -> 0     （加法的單位元素）
        求存在性  -> False （or 的單位元素）
        求最小值  -> +∞    （min 的單位元素）
        求最大值  -> -∞    （max 的單位元素）
        求乘積    -> 1     （乘法的單位元素）"""),
 ],
 "approaches": [
   ap("解法一", "DFS 往下傳累積值（標準答案）", [
     ("c", S["p129_dfs"]),
     "<strong>七行，O(n) 時間、O(h) 空間。</strong>",
     ("h", "手動走一遍範例 2"),
     ("c", """          4
         / \\
        9   0
       / \\
      5   1

go(4, 0):  cur = 4，不是葉
    go(9, 4): cur = 49，不是葉
        go(5, 49): cur = 495，是葉 -> 495
        go(1, 49): cur = 491，是葉 -> 491
        -> 986
    go(0, 4): cur = 40，是葉 -> 40
    -> 986 + 40 = 1026 ✔"""),
     ("h", "為什麼不需要「回溯」（撤銷）？"),
     ("c", """因為 cur 是【傳值】的參數，不是共享的可變狀態。

    cur = cur * 10 + node.val

    這一行只改了【這一層的區域變數】，
    父節點的 cur 完全沒動 ✔

    所以左右子樹各自拿到「父節點的 cur」，互不干擾。

【對照第 113 題（路徑總和 II）】：
    那題用共享的 list path，所以必須 append / pop 回溯。

    這題用不可變的 int，所以不用。

    【只要狀態是「值」而不是「參考」，就不用回溯。】

    這也是為什麼第 113 題的「解法二」（不可變 path）
    也不需要 pop —— 同一個道理。"""),
   ], "O(n)", "O(h)", "每個節點一次", "遞迴堆疊", optimal=True),

   ap("解法二", "迭代 + 堆疊", [
     ("c", S["p129_iter"]),
     "<strong>把 <code>(節點, 累積值)</code> 一起打包進堆疊 —— 「遞迴改迭代」的標準手法。</strong>",
     ("c", """注意這裡的 cur 語意和遞迴版稍有不同：

    遞迴版：go(node, cur) 的 cur 是「走到 node【之前】的值」
            然後在函式裡才加上 node.val

    迭代版：stack 裡的 cur 是「【已經包含】node 自己的值」
            所以初始是 (root, root.val)

    兩種都對，但【不能混用】——
    混用就會差一位數。

【建議在註解裡寫清楚】：
    # (節點, 【已包含這個節點】的累積值)

    這類「狀態的時間點」的歧義，
    是「遞迴改迭代」時最容易出錯的地方
    （第 112 題也提過同一件事）。""",),
     "<strong>沒有遞迴深度問題</strong>（雖然本題深度 ≤ 10，用不到）。",
   ], "O(n)", "O(h)", "每個節點一次", "顯式堆疊"),

   ap("解法三", "收集字串再加總（最直白）", [
     ("c", S["p129_paths"]),
     ("c", """優點：一眼看得懂「每條路徑代表一個數字」。

缺點：
    ✘ 每層都建新字串 -> O(h) 每次，總共 O(n·h)
    ✘ 存所有數字 -> O(葉節點數) 額外空間
    ✘ 最後 int(path) 又掃一遍字串

【但它有一個獨特的優勢】：

    如果題目改成「每個節點的值可能超過一位數」
    （例如節點值是 0..99），
    那「cur * 10 + val」就【不對】了 ——

        節點 1 和節點 23 -> 應該是 "123" -> 123
        但 1 * 10 + 23 = 33  ✘

    字串版完全不受影響 ✔

    【整數版依賴「每個節點剛好一位數」這個前提。
      前提被打破時，字串版才是對的。】

    這又是一次「短但依賴前提 vs 長但通用」的取捨
    （和第 116/117 題一樣）。"""),
   ], "O(n·h)", "O(n)", "建字串的成本", "所有路徑字串"),
 ],
 "compare": (["解法", "時間", "空間", "節點值可超過一位嗎", "備註"],
   [["一、DFS 傳累積值", "O(n)", "O(h)", "✘", "標準答案"],
    ["二、堆疊迭代", "O(n)", "O(h)", "✘", "避免遞迴"],
    ["三、收集字串", "O(n·h)", "O(n)", "✔", "通用但慢"]]),
 "edges": [
   "<strong>單一節點</strong> <code>[0]</code> → <code>0</code>。",
   "<strong><code>[1,2,3]</code></strong> → <code>25</code>。",
   "<strong><code>[1,0]</code></strong>（只有左孩子 0）→ <code>10</code>，<strong>不是 1</strong>。"
   "<strong>根不是葉節點。</strong>",
   "<strong>節點值是 0</strong> → <code>cur * 10 + 0</code> 正確處理"
   "（<strong>不要用 <code>if node.val</code> 判斷節點存在</strong>）。",
   "<strong>把空節點的 base case 寫成 <code>return cur</code></strong> → "
   "<strong>單邊的節點會被多算一次。本題第一名的 bug。</strong>",
   "<strong>用共享的變數累積 <code>cur</code> 而忘了回溯</strong> → "
   "右子樹會拿到左子樹留下的值。",
   "<strong>迭代版和遞迴版的 <code>cur</code> 語意混用</strong> → 差一位數。",
   "<strong>深度 10 的滿樹</strong> → 1023 個節點、512 條路徑，每條 10 位數。",
 ],
 "follow": [
   ("h", "追問一：如果要「所有路徑數字的最大值」呢？"),
   "<strong>把 <code>+</code> 換成 <code>max</code>，base case 從 0 換成 <code>-inf</code></strong>。",
   ("c", """def go(node, cur):
    if not node: return float('-inf')     ← 單位元素換了
    cur = cur * 10 + node.val
    if 是葉節點: return cur
    return max(go(left, cur), go(right, cur))

【又是「base case 要填對單位元素」】——

    求和 -> 0
    求最大 -> -inf

    這個原則在第 111、112、124 題都出現過。
    值得當成反射動作。""",),
   ("h", "追問二：如果數字是「從葉到根」讀的呢？"),
   "<strong>那就不能邊走邊累積了</strong> —— "
   "因為<strong>「個位數」要等走到葉節點才知道</strong>。",
   ("c", """兩種做法：

    (a) 傳「目前的位數」，往下時乘上 10^depth
        go(node, cur, place):
            cur += node.val * place
            go(child, cur, place * 10)

        —— 但這樣 place 會依賴深度，而深度不固定。

    (b) 收集路徑，到葉節點時反轉再算
        —— 最簡單，就是解法三加一個 [::-1]

【「從哪一端開始累積」會完全改變演算法的形狀】——

    從根開始（本題）：可以邊走邊算 ✔
    從葉開始：        必須先知道長度，或者收集後再處理

    這和第 2 題（兩數相加，低位在前）vs
    第 445 題（兩數相加 II，高位在前）的差別是同一回事。""",),
   ("h", "追問三：如果節點值可能是多位數呢？"),
   "<strong><code>cur * 10 + val</code> 就錯了</strong> —— "
   "要改成 <code>cur * 10^(val 的位數) + val</code>，或者直接用字串（解法三）。",
   "<strong>「每個節點剛好一位數」是整數版的隱含前提</strong>，"
   "<strong>題目用 <code>0 ≤ Node.val ≤ 9</code> 明確保證了它。</strong>"
   "<strong>讀題時注意這種「限定值域」的條件 —— 它們常常是某個技巧成立的基礎。</strong>",
   ("h", "追問四：如果樹很深（例如 10⁵），數字會很大怎麼辦？"),
   "<strong>在 Python 裡沒問題（大整數），但會慢</strong> —— "
   "<strong>大整數的乘法不是 O(1)。</strong>",
   "<strong>實務上會要求「對某個數取模」</strong>："
   "<code>cur = (cur * 10 + node.val) % MOD</code>。"
   "<strong>因為加法和乘法都和取模可交換，所以這樣算出來的結果是對的。</strong>",
 ],
 "related": [
   "<strong>第 112/113 題 Path Sum I/II</strong> —— 同樣的「根到葉」骨架",
   "<strong>第 257 題 Binary Tree Paths</strong> —— 輸出所有路徑字串",
   "<strong>第 988 題 Smallest String Starting From Leaf</strong> —— 從葉到根的版本",
   "<strong>第 2 題 Add Two Numbers</strong> —— 同樣的「進位累積」",
 ],
 "check": [
   "<code>cur = cur * 10 + node.val</code> 在做什麼？為什麼不用字串？",
   "空節點的 base case 為什麼是 0 而不是 <code>cur</code>？寫錯會在哪個測資出問題？",
   "為什麼這題不需要「回溯」，而第 113 題需要？",
   "如果節點值可能是兩位數，哪一個解法還是對的？",
 ],
})
print("P129 written")

# ==================== 130. Surrounded Regions ====================
S["p130_dfs"] = '''class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m, n = len(board), len(board[0])

        def mark(i, j):
            """把和邊界相連的 O 標記成 #（安全的）"""
            if not (0 <= i < m and 0 <= j < n) or board[i][j] != "O":
                return
            board[i][j] = "#"
            mark(i + 1, j); mark(i - 1, j)
            mark(i, j + 1); mark(i, j - 1)

        # 只從【四條邊界】上的 O 出發
        for i in range(m):
            mark(i, 0); mark(i, n - 1)
        for j in range(n):
            mark(0, j); mark(m - 1, j)

        # 剩下的 O 都是被圍住的 -> 翻成 X；# 是安全的 -> 翻回 O
        for i in range(m):
            for j in range(n):
                board[i][j] = "O" if board[i][j] == "#" else "X"'''

S["p130_bfs"] = '''from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m, n = len(board), len(board[0])

        dq = deque()
        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == "O":
                    board[i][j] = "#"
                    dq.append((i, j))
        for j in range(n):
            for i in (0, m - 1):
                if board[i][j] == "O":
                    board[i][j] = "#"
                    dq.append((i, j))

        while dq:
            i, j = dq.popleft()
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    board[x][y] = "#"
                    dq.append((x, y))

        for i in range(m):
            for j in range(n):
                board[i][j] = "O" if board[i][j] == "#" else "X"'''

S["p130_union"] = '''class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m, n = len(board), len(board[0])
        # 多開一個「虛擬節點」代表邊界外面
        OUT = m * n
        parent = list(range(m * n + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra

        for i in range(m):
            for j in range(n):
                if board[i][j] != "O":
                    continue
                if i in (0, m - 1) or j in (0, n - 1):
                    union(OUT, i * n + j)       # 在邊界上 -> 連到虛擬節點
                for di, dj in ((1, 0), (0, 1)):  # 只看右和下，避免重複
                    x, y = i + di, j + dj
                    if x < m and y < n and board[x][y] == "O":
                        union(i * n + j, x * n + y)

        root_out = find(OUT)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and find(i * n + j) != root_out:
                    board[i][j] = "X"'''


def _p130_ref(board):
    """獨立參考解：BFS 從邊界出發標記，回傳新的 board。"""
    if not board:
        return board
    m, n = len(board), len(board[0])
    safe = [[False] * n for _ in range(m)]
    q = deque()
    for i in range(m):
        for j in range(n):
            if (i in (0, m - 1) or j in (0, n - 1)) and board[i][j] == "O":
                safe[i][j] = True
                q.append((i, j))
    while q:
        i, j = q.popleft()
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = i + di, j + dj
            if 0 <= x < m and 0 <= y < n and board[x][y] == "O" and not safe[x][y]:
                safe[x][y] = True
                q.append((x, y))
    return [["O" if safe[i][j] else ("X" if board[i][j] in "OX" else board[i][j])
             for j in range(n)] for i in range(m)]


_p130 = [S.load(k) for k in ("p130_dfs", "p130_bfs", "p130_union")]

_CASES130 = [
    [list("XXXX"), list("XOOX"), list("XXOX"), list("XOXX")],
    [list("X")],
    [list("O")],
    [list("OO"), list("OO")],
    [list("XOX"), list("OXO"), list("XOX")],
]
for b in _CASES130:
    want = _p130_ref([r[:] for r in b])
    for sol in _p130:
        g = [r[:] for r in b]
        sol.solve(g)
        assert g == want, ("P130", b, want, g, sol)

for _ in range(3000):
    m = random.randrange(1, 6)
    n = random.randrange(1, 6)
    b = [[random.choice("OX") for _ in range(n)] for _ in range(m)]
    want = _p130_ref([r[:] for r in b])
    for sol in _p130:
        g = [r[:] for r in b]
        sol.solve(g)
        assert g == want, ("P130 random", b, want, g, sol)
print("P130 solutions OK")

_P130_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 反過來想：不要找「被圍住的 O」，而是找「碰得到邊界的 O」—— 剩下的就是被圍住的。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">原始盤面</text>
            <g font-size="14" text-anchor="middle">
              <rect x="40" y="66" width="34" height="34" fill="none" stroke="var(--border)"/><text x="57" y="89" fill="var(--text-muted)">X</text>
              <rect x="74" y="66" width="34" height="34" fill="none" stroke="var(--border)"/><text x="91" y="89" fill="var(--text-muted)">X</text>
              <rect x="108" y="66" width="34" height="34" fill="none" stroke="var(--border)"/><text x="125" y="89" fill="var(--text-muted)">X</text>
              <rect x="142" y="66" width="34" height="34" fill="none" stroke="var(--border)"/><text x="159" y="89" fill="var(--text-muted)">X</text>
              <rect x="40" y="100" width="34" height="34" fill="none" stroke="var(--border)"/><text x="57" y="123" fill="var(--text-muted)">X</text>
              <rect x="74" y="100" width="34" height="34" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="91" y="123" fill="#ff8a65">O</text>
              <rect x="108" y="100" width="34" height="34" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="125" y="123" fill="#ff8a65">O</text>
              <rect x="142" y="100" width="34" height="34" fill="none" stroke="var(--border)"/><text x="159" y="123" fill="var(--text-muted)">X</text>
              <rect x="40" y="134" width="34" height="34" fill="none" stroke="var(--border)"/><text x="57" y="157" fill="var(--text-muted)">X</text>
              <rect x="74" y="134" width="34" height="34" fill="none" stroke="var(--border)"/><text x="91" y="157" fill="var(--text-muted)">X</text>
              <rect x="108" y="134" width="34" height="34" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="125" y="157" fill="#ff8a65">O</text>
              <rect x="142" y="134" width="34" height="34" fill="none" stroke="var(--border)"/><text x="159" y="157" fill="var(--text-muted)">X</text>
              <rect x="40" y="168" width="34" height="34" fill="none" stroke="var(--border)"/><text x="57" y="191" fill="var(--text-muted)">X</text>
              <rect x="74" y="168" width="34" height="34" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="91" y="191" fill="var(--gold)">O</text>
              <rect x="108" y="168" width="34" height="34" fill="none" stroke="var(--border)"/><text x="125" y="191" fill="var(--text-muted)">X</text>
              <rect x="142" y="168" width="34" height="34" fill="none" stroke="var(--border)"/><text x="159" y="191" fill="var(--text-muted)">X</text>
            </g>
            <text x="210" y="130" fill="var(--gold)" font-size="22">→</text>
            <text x="260" y="52" fill="var(--gold)" font-size="13">結果</text>
            <g font-size="14" text-anchor="middle">
              <rect x="260" y="66" width="34" height="34" fill="none" stroke="var(--border)"/><text x="277" y="89" fill="var(--text-muted)">X</text>
              <rect x="294" y="66" width="34" height="34" fill="none" stroke="var(--border)"/><text x="311" y="89" fill="var(--text-muted)">X</text>
              <rect x="328" y="66" width="34" height="34" fill="none" stroke="var(--border)"/><text x="345" y="89" fill="var(--text-muted)">X</text>
              <rect x="362" y="66" width="34" height="34" fill="none" stroke="var(--border)"/><text x="379" y="89" fill="var(--text-muted)">X</text>
              <rect x="260" y="100" width="34" height="34" fill="none" stroke="var(--border)"/><text x="277" y="123" fill="var(--text-muted)">X</text>
              <rect x="294" y="100" width="34" height="34" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="311" y="123" fill="var(--accent)">X</text>
              <rect x="328" y="100" width="34" height="34" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="345" y="123" fill="var(--accent)">X</text>
              <rect x="362" y="100" width="34" height="34" fill="none" stroke="var(--border)"/><text x="379" y="123" fill="var(--text-muted)">X</text>
              <rect x="260" y="134" width="34" height="34" fill="none" stroke="var(--border)"/><text x="277" y="157" fill="var(--text-muted)">X</text>
              <rect x="294" y="134" width="34" height="34" fill="none" stroke="var(--border)"/><text x="311" y="157" fill="var(--text-muted)">X</text>
              <rect x="328" y="134" width="34" height="34" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="345" y="157" fill="var(--accent)">X</text>
              <rect x="362" y="134" width="34" height="34" fill="none" stroke="var(--border)"/><text x="379" y="157" fill="var(--text-muted)">X</text>
              <rect x="260" y="168" width="34" height="34" fill="none" stroke="var(--border)"/><text x="277" y="191" fill="var(--text-muted)">X</text>
              <rect x="294" y="168" width="34" height="34" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="311" y="191" fill="var(--gold)">O</text>
              <rect x="328" y="168" width="34" height="34" fill="none" stroke="var(--border)"/><text x="345" y="191" fill="var(--text-muted)">X</text>
              <rect x="362" y="168" width="34" height="34" fill="none" stroke="var(--border)"/><text x="379" y="191" fill="var(--text-muted)">X</text>
            </g>
            <text x="430" y="130" fill="var(--gold)" font-size="11" text-anchor="start">最後一列的 O 在邊界上</text>
            <text x="430" y="152" fill="var(--gold)" font-size="11" text-anchor="start">→ 沒有被圍住，保留</text>
            <text x="430" y="182" fill="#ff8a65" font-size="11" text-anchor="start">中間那三個 O 四面都是 X</text>
            <text x="430" y="204" fill="#ff8a65" font-size="11" text-anchor="start">→ 被圍住，翻成 X</text>
            <line x1="20" y1="226" x2="620" y2="226" stroke="var(--border)"/>
            <text x="20" y="254" fill="var(--accent)" font-size="13">為什麼要「反過來找」？</text>
            <text x="20" y="282" fill="var(--text-muted)" font-size="12">正著找「被圍住的 O」很難：你必須確認整塊區域【沒有任何一格】碰到邊界 ——</text>
            <text x="20" y="306" fill="var(--text-muted)" font-size="12">走到一半發現碰到邊界，前面標記的全部都要撤銷。</text>
            <text x="20" y="336" fill="var(--gold)" font-size="12">反過來找「安全的 O」就沒有這個問題：從邊界出發，能走到的都安全，一次就定案。</text>
            <text x="20" y="366" fill="var(--accent)" font-size="12">三個狀態要用三個符號：O（還沒判定）、#（確定安全）、X（牆或已翻）。</text>
            <text x="20" y="390" fill="#ff8a65" font-size="12">用兩個符號會分不清「本來就是 X」和「安全的 O」——這是本題最常見的實作 bug。</text>'''

emit({
 "num": 130, "slug": "surrounded-regions",
 "en": [
   "You are given an <code>m x n</code> matrix <code>board</code> containing "
   "<strong>letters</strong> <code>'X'</code> and <code>'O'</code>, <strong>capture regions</strong> "
   "that are <strong>surrounded</strong>:",
   ("raw", "<ul><li><strong>Connect</strong>: A cell is connected to adjacent cells "
           "horizontally or vertically.</li>"
           "<li><strong>Region</strong>: To form a region <strong>connect every</strong> "
           "<code>'O'</code> cell.</li>"
           "<li><strong>Surround</strong>: The region is surrounded with <code>'X'</code> cells "
           "if you can <strong>connect the region</strong> with <code>'X'</code> cells and none "
           "of the region cells are on the edge of the <code>board</code>.</li></ul>"),
   "To capture a <strong>surrounded region</strong>, replace all <code>'O'</code>s with "
   "<code>'X'</code>s <strong>in-place</strong> in the original board.",
 ],
 "zh": [
   "給你一個 <code>m × n</code> 的矩陣 <code>board</code>，裡面只有 "
   "<code>'X'</code> 和 <code>'O'</code>。",
   "找出所有<strong>被 <code>'X'</code> 完全圍住</strong>的 <code>'O'</code> 區域，"
   "把它們<strong>原地</strong>翻成 <code>'X'</code>。",
   ("ul", [
     "<strong>相連</strong>：只算<strong>上下左右</strong>四個方向（不算斜的）。",
     "<strong>區域</strong>：所有互相連通的 <code>'O'</code> 算同一塊。",
     "<strong>被圍住</strong>：整塊區域<strong>沒有任何一格在邊界上</strong>。",
   ]),
 ],
 "pre": [
   ("note", "★ 這題的全部：反過來想", [
     ("c", """【正著做】：找出「被圍住的 O」

    對每一塊 O 區域，走一遍，檢查有沒有碰到邊界。
        沒碰到 -> 全部翻成 X
        碰到了 -> 【前面走過的都要撤銷】

    問題：你在走到一半時還不知道結論，
    所以要嘛先收集整塊再決定，
    要嘛標記了再撤銷 —— 兩種都很麻煩。

【反著做】：找出「安全的 O」

    「被圍住」的反面是「連得到邊界」。

    所以：
        1. 從【四條邊界上】的每個 O 出發，DFS/BFS
        2. 走得到的所有 O 都標記成「安全」（用 # ）
        3. 掃全盤：
             # -> 翻回 O（安全的）
             O -> 翻成 X（沒被走到 = 被圍住）
             X -> 保持 X

    【一次定案，完全不用撤銷。】✔

【「正著難、反著易」是很常見的模式】：

    130  被圍繞的區域    找「連得到邊界的」而不是「被圍住的」  （本題）
    1020 飛地的數量      同樣從邊界出發
    417  太平洋大西洋    從兩個海洋反向往內流
    1254 封閉島嶼的數目  同樣的反向思路

    【看到「完全被包圍 / 不能到達外面」，
      就反過來從外面開始搜。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]

  輸出：       [["X","X","X","X"],
                ["X","X","X","X"],
                ["X","X","X","X"],
                ["X","O","X","X"]]

  說明：中間那三個 O 四周都是 X -> 被圍住，翻成 X。
        最後一列的 O 在【邊界上】 -> 沒有被圍住，保留。

範例 2
  輸入：board = [["X"]]
  輸出：[["X"]]""",
 "constraints": [
   "<code>m == board.length</code>",
   "<code>n == board[i].length</code>",
   "1 ≤ <code>m</code>, <code>n</code> ≤ 200",
   "<code>board[i][j]</code> 是 <code>'X'</code> 或 <code>'O'</code>",
 ],
 "idea": [
   ("fig", _P130_FIG, "0 0 640 408"),
   ("c", """三個步驟：

    1. 從【四條邊界】上的 O 出發做 DFS/BFS，
       把走得到的全部標記成 '#'

    2. 掃全盤：
           '#' -> 'O'     （安全的，翻回來）
           'O' -> 'X'     （沒被標記 = 被圍住）
           'X' -> 'X'     （不變）

【★ 為什麼要用第三個符號 '#'？】

    如果只用兩個符號（把安全的 O 直接留著、其他翻 X），
    你就【分不清】：

        「這格是本來就是 X」還是「這格是我剛翻掉的 O」？

    更糟的是：在標記階段，你無法區分
        「還沒判定的 O」和「已判定安全的 O」
    -> DFS 會無限繞圈（走回已經走過的格子）。

    用 '#' 當【中間狀態】，一切都清楚了：

        O = 還沒判定
        # = 確定安全
        X = 牆，或者已經定案

    【「用一個額外的標記值表示中間狀態」
      是格子圖 DFS 的標準手法，
      它同時充當了「visited 陣列」。】

    第 200 題（島嶼數量）也是同一招
    （把走過的 '1' 改成 '0'）。

【★ 邊界的走法】

    for i in range(m): mark(i, 0); mark(i, n-1)    左右兩欄
    for j in range(n): mark(0, j); mark(m-1, j)    上下兩列

    四個角落會被處理兩次 —— 沒關係，
    第二次進去時那格已經是 '#'，會立刻 return ✔

複雜度：O(m·n) 時間（每格最多被訪問常數次）、
        O(m·n) 空間（最壞情況的遞迴深度 / 佇列大小）"""),
 ],
 "approaches": [
   ap("解法一", "從邊界 DFS 標記（標準答案）", [
     ("c", S["p130_dfs"]),
     ("h", "<code>mark</code> 的三個 <code>return</code> 條件合成一行"),
     ("c", """if not (0 <= i < m and 0 <= j < n) or board[i][j] != "O":
    return

    這一行同時處理了：
        1. 越界
        2. 這格是 'X'（牆）
        3. 這格已經是 '#'（走過了）

    【把「越界檢查」放在遞迴函式的開頭，
      而不是在呼叫之前檢查】——

        mark(i+1, j)                    ✔ 直接呼叫，讓它自己判斷
        if i+1 < m: mark(i+1, j)        ✘ 四個方向都要寫一次

    前者程式碼短很多，而且不容易漏。

    代價是多幾次無謂的函式呼叫 —— 完全可以接受。

【注意 Python 的 or 會短路】：
    先檢查越界，確定安全了才去存取 board[i][j] ✔
    順序反過來就會 IndexError。""",),
     ("h", "★ 遞迴深度的風險"),
     ("c", """最壞情況：整個盤面都是 O（200 × 200 = 40000 格）。

    DFS 可能一路遞迴 40000 層 ->
    Python 預設上限 1000 -> RecursionError ✘

    LeetCode 的 Python 環境通常調高了上限，
    所以這題實測大多會過。

    但【正式面試要主動說出來】：
        「如果盤面很大，我會改用 BFS（解法二）避免堆疊溢位。」

    這比寫出哪個版本更重要。

【格子圖的 DFS 遞迴深度 = O(m·n)】，
    不像樹的 O(h) —— 因為格子圖可以「蛇行」走過每一格。

    這是格子圖題目普遍偏好 BFS 的原因。""",),
     "<strong>時間 O(m·n)、空間 O(m·n)（遞迴堆疊）。</strong>",
   ], "O(m × n)", "O(m × n)", "每格最多訪問常數次", "遞迴堆疊", optimal=True),

   ap("解法二", "從邊界 BFS（避免遞迴深度問題）", [
     ("c", S["p130_bfs"]),
     "<strong>和解法一完全等價，只是把遞迴換成佇列。</strong>",
     ("c", """【注意入隊時就要標記】：

    if board[i][j] == "O":
        board[i][j] = "#"       ← 標記
        dq.append((i, j))       ← 再入隊

    順序反過來（先入隊、出隊才標記）的話，
    同一格可能被重複入隊很多次 ——
    這是 BFS 最常見的效能 bug（第 127 題也提過）。

【四個方向的寫法】：

    for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
        x, y = i + di, j + dj

    這個「方向陣列」的寫法比寫四次 if 好太多：
        ✔ 短
        ✔ 要改成八方向（含斜的）只要加四筆
        ✔ 不會漏掉某個方向

    【格子圖題目一律用方向陣列。】

    八方向版：
        ((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))

    或者用 itertools：
        [(a,b) for a in (-1,0,1) for b in (-1,0,1) if (a,b) != (0,0)]"""),
     "<strong>空間 O(m·n)（佇列），但沒有堆疊溢位的風險。</strong>"
     "<strong>對 200×200 的盤面，這是比較穩的選擇。</strong>",
   ], "O(m × n)", "O(m × n)", "每格進出佇列一次", "佇列"),

   ap("解法三", "並查集 + 虛擬節點（想法漂亮）", [
     ("c", S["p130_union"]),
     ("h", "★ 「虛擬節點」這個技巧"),
     ("c", """多開一個編號 m*n 的節點，代表「盤面外面」。

    然後：
        邊界上的 O  -> union(OUT, 它)
        相鄰的兩個 O -> union 起來

    最後：
        find(格子) == find(OUT)  -> 安全 ✔
        否則                      -> 被圍住，翻成 X

【虛擬節點（virtual / super node）的用途】：

    把「一組節點都連到同一個東西」這件事，
    變成「它們都和同一個虛擬節點連通」。

    這樣「判斷是否屬於某一類」就變成一次 find。

    其他用法：
        - 多源最短路：加一個超級源點，連到所有起點
        - 多個匯點：加一個超級匯點
        - 第 803 題（打磚塊）：屋頂當虛擬節點

【為什麼只 union 「右」和「下」？】

    for di, dj in ((1, 0), (0, 1)):

    因為 union 是對稱的 —— (i,j) 和 (i+1,j) 連起來時，
    等一下處理 (i+1,j) 就不用再往上連一次。

    每條邊只處理一次，省一半的工作。

【這個解法值得會嗎？】

    這題用並查集是【殺雞用牛刀】——
    DFS/BFS 更短也更快。

    但如果題目變成「動態地把某些 X 改成 O，
    每次都要問哪些區域被圍住」，
    那並查集就是唯一合理的選擇
    （第 803 題就是這種動態版本）。"""),
   ], "O(m·n·α)", "O(m × n)", "並查集的攤還成本", "parent 陣列"),
 ],
 "compare": (["解法", "時間", "空間", "會堆疊溢位嗎", "備註"],
   [["一、邊界 DFS", "O(mn)", "O(mn)", "✔ 大盤面有風險", "最短"],
    ["二、邊界 BFS", "O(mn)", "O(mn)", "✘", "最穩"],
    ["三、並查集 + 虛擬節點", "O(mn·α)", "O(mn)", "✘", "動態版才需要"]]),
 "edges": [
   "<strong>1×1 的盤面</strong> <code>[[\"O\"]]</code> → 保持 <code>O</code>"
   "（它自己就在邊界上）。",
   "<strong>全部是 O</strong> → 全部保留（都連得到邊界）。",
   "<strong>全部是 X</strong> → 不變。",
   "<strong>只有一列或一欄</strong> → 每一格都在邊界上，全部保留。",
   "<strong>棋盤格 <code>[[\"XOX\"],[\"OXO\"],[\"XOX\"]]</code></strong> → "
   "四個 O 都在邊界上，全部保留。",
   "<strong>只用兩個符號（不用 <code>#</code>）</strong> → "
   "<strong>分不清「本來的 X」和「翻掉的 O」，而且 DFS 會無限繞圈。本題第一名的 bug。</strong>",
   "<strong>BFS 出隊時才標記</strong> → 同一格重複入隊，效能爆炸。",
   "<strong>忘了處理四個角落</strong> → 其實不會漏（左右欄和上下列都掃了），"
   "<strong>但角落會被走兩次 —— 無害。</strong>",
   "<strong>200×200 全是 O</strong> → DFS 遞迴 4 萬層，可能 <code>RecursionError</code>。",
 ],
 "follow": [
   ("h", "追問一：如果連通算八個方向（含斜的）呢？"),
   "<strong>把方向陣列從 4 個改成 8 個</strong>，其他完全不用動。",
   "<strong>但要注意：這樣「被圍住」會變得更難</strong> —— "
   "<strong>斜向也能逃出去，所以會有更多 O 被保留。</strong>"
   "<strong>「連通的定義」是格子圖題目一定要先問清楚的事。</strong>",
   ("h", "追問二：如果要「數有幾塊被圍住的區域」呢？"),
   "<strong>標記完安全的 <code>#</code> 之後，對剩下的 <code>O</code> 再做一次連通塊計數</strong>"
   "（就是第 200 題）。",
   "<strong>或者在第一次掃描時就順便記錄每塊的編號</strong> —— "
   "<strong>那樣一趟就能同時知道「有幾塊」和「哪些被圍住」。</strong>",
   ("h", "追問三：這題和第 200 題（島嶼數量）有什麼不同？"),
   ("c", """第 200 題：數有幾塊 '1' 的連通區域
第 130 題：找出「不碰邊界」的 'O' 連通區域

    骨架完全相同（格子圖的 DFS/BFS 洪水填充），
    差別只在「從哪裡開始」和「要記錄什麼」。

    200：從每一格沒走過的 '1' 開始，每開始一次計數 +1
    130：只從邊界開始，記錄「走得到」

【洪水填充（flood fill）的通用骨架】：

    for 每個起點:
        if 該格符合條件 and 沒走過:
            DFS/BFS 把整塊標記起來
            <做點事：計數 / 記錄大小 / 記錄顏色>

    200 島嶼數量、130 被圍繞的區域、733 圖像渲染、
    695 島嶼的最大面積、1254 封閉島嶼、417 太平洋大西洋
    —— 六題一個骨架。""",),
   ("h", "追問四：如果盤面很大（10⁴ × 10⁴）放不進記憶體呢？"),
   "<strong>可以分塊處理（tiling）</strong>：把盤面切成小塊，"
   "<strong>用並查集記錄「跨塊邊界的連通關係」</strong>。",
   "<strong>這是真實影像處理（例如衛星影像的連通區域標記）的做法</strong> —— "
   "<strong>叫做「兩遍掃描連通元件標記」（two-pass CCL），"
   "第一遍給臨時標籤、用並查集記等價關係，第二遍統一標籤。</strong>",
 ],
 "related": [
   "<strong>第 200 題 Number of Islands</strong> —— 同一個洪水填充骨架",
   "<strong>第 1020 題 Number of Enclaves</strong> —— 幾乎一模一樣的反向思路",
   "<strong>第 417 題 Pacific Atlantic Water Flow</strong> —— 從兩個邊界反向搜",
   "<strong>第 1254 題 Number of Closed Islands</strong> —— 數「被圍住的島」",
   "<strong>第 803 題 Bricks Falling When Hit</strong> —— 動態版，非用並查集不可",
 ],
 "check": [
   "為什麼要「反過來找安全的 O」而不是「正著找被圍住的 O」？",
   "為什麼一定要用第三個符號 <code>#</code>？只用兩個會怎樣？",
   "BFS 版為什麼要「入隊時就標記」而不是「出隊時才標記」？",
   "200×200 全是 O 的盤面，DFS 版有什麼風險？",
 ],
})
print("P130 written")
