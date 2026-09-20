# -*- coding: utf-8 -*-
"""第 146–150 題。"""
import random, math, itertools
from collections import OrderedDict
from fractions import Fraction
from authoring import emit, ap
from runner import Src, ListNode, to_list, from_list

S = Src()
random.seed(146)

# ==================== 146. LRU Cache ====================
S["p146_dll"] = '''class Node:
    """雙向鏈結串列的節點"""
    __slots__ = ("key", "val", "prev", "next")

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.table = {}                     # key -> Node

        # 兩個虛擬節點，省掉所有「頭尾」的特判
        self.head = Node()                  # head.next 是【最近用過的】
        self.tail = Node()                  # tail.prev 是【最久沒用的】
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        node = self.table[key]
        self._remove(node)                  # 用過了 -> 搬到最前面
        self._add_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            node.val = value
            self._remove(node)
            self._add_front(node)
            return

        if len(self.table) == self.cap:     # 滿了 -> 淘汰最久沒用的
            lru = self.tail.prev
            self._remove(lru)
            del self.table[lru.key]         # ★ 這就是節點要存 key 的理由

        node = Node(key, value)
        self.table[key] = node
        self._add_front(node)'''

S["p146_od"] = '''from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = OrderedDict()             # 它本身就記得插入順序

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)            # 搬到尾端（代表最近用過）
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
        self.od[key] = value
        if len(self.od) > self.cap:
            self.od.popitem(last=False)     # 丟掉最前面（最久沒用的）'''


class _RefLRU(object):
    """獨立參考實作：用 list 維護使用順序（O(n) 但一定正確）。"""
    def __init__(self, cap):
        self.cap = cap
        self.order = []
        self.d = {}

    def get(self, k):
        if k not in self.d:
            return -1
        self.order.remove(k)
        self.order.append(k)
        return self.d[k]

    def put(self, k, v):
        if k in self.d:
            self.order.remove(k)
        elif len(self.d) == self.cap:
            old = self.order.pop(0)
            del self.d[old]
        self.d[k] = v
        self.order.append(k)


_p146ns = [S.loadns(k) for k in ("p146_dll", "p146_od")]

for ns in _p146ns:
    LRU = ns["LRUCache"]
    c = LRU(2)
    c.put(1, 1); c.put(2, 2)
    assert c.get(1) == 1
    c.put(3, 3)
    assert c.get(2) == -1
    c.put(4, 4)
    assert c.get(1) == -1
    assert c.get(3) == 3
    assert c.get(4) == 4

for _ in range(1200):
    cap = random.randrange(1, 5)
    ref = _RefLRU(cap)
    impls = [ns["LRUCache"](cap) for ns in _p146ns]
    for _ in range(40):
        if random.random() < 0.5:
            k = random.randrange(0, 6)
            want = ref.get(k)
            for im in impls:
                assert im.get(k) == want, ("P146 get", cap, k, want)
        else:
            k, v = random.randrange(0, 6), random.randrange(0, 100)
            ref.put(k, v)
            for im in impls:
                im.put(k, v)
print("P146 solutions OK")

_P146_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">雜湊表負責「O(1) 找到節點」，雙向鏈結串列負責「O(1) 搬動與刪除」—— 兩個結構各補對方的短處。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">雜湊表 table：key → 節點的位址</text>
            <g font-size="12" text-anchor="middle">
              <rect x="40" y="70" width="70" height="26" fill="none" stroke="var(--accent)"/><text x="75" y="88" fill="var(--accent)">1 → ●</text>
              <rect x="118" y="70" width="70" height="26" fill="none" stroke="var(--accent)"/><text x="153" y="88" fill="var(--accent)">2 → ●</text>
              <rect x="196" y="70" width="70" height="26" fill="none" stroke="var(--accent)"/><text x="231" y="88" fill="var(--accent)">3 → ●</text>
            </g>
            <text x="20" y="140" fill="var(--gold)" font-size="13">雙向鏈結串列：由「最近用過」排到「最久沒用」</text>
            <g font-size="12" text-anchor="middle">
              <rect x="40" y="158" width="58" height="34" fill="none" stroke="var(--text-muted)" stroke-dasharray="4 3"/><text x="69" y="180" fill="var(--text-muted)">head</text>
              <rect x="120" y="158" width="58" height="34" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="149" y="180" fill="#ff8a65">3</text>
              <rect x="200" y="158" width="58" height="34" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="229" y="180" fill="var(--accent)">1</text>
              <rect x="280" y="158" width="58" height="34" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="309" y="180" fill="var(--accent)">2</text>
              <rect x="360" y="158" width="58" height="34" fill="none" stroke="var(--text-muted)" stroke-dasharray="4 3"/><text x="389" y="180" fill="var(--text-muted)">tail</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="98" y1="170" x2="116" y2="170"/><line x1="116" y1="182" x2="98" y2="182"/>
              <line x1="178" y1="170" x2="196" y2="170"/><line x1="196" y1="182" x2="178" y2="182"/>
              <line x1="258" y1="170" x2="276" y2="170"/><line x1="276" y1="182" x2="258" y2="182"/>
              <line x1="338" y1="170" x2="356" y2="170"/><line x1="356" y1="182" x2="338" y2="182"/>
            </g>
            <text x="149" y="214" fill="#ff8a65" font-size="11" text-anchor="middle">最近用過</text>
            <text x="309" y="214" fill="var(--accent)" font-size="11" text-anchor="middle">最久沒用 → 滿了先丟它</text>
            <line x1="20" y1="238" x2="620" y2="238" stroke="var(--border)"/>
            <text x="20" y="266" fill="var(--accent)" font-size="13">為什麼非得是【雙向】串列？</text>
            <text x="40" y="294" fill="var(--text-muted)" font-size="12">要把某個節點從中間「拔出來」，必須改它前一個的 next。</text>
            <text x="40" y="320" fill="var(--text-muted)" font-size="12">單向串列只知道 next，要找前一個就得從頭走一遍 → O(n)。</text>
            <text x="40" y="346" fill="var(--gold)" font-size="12">雙向串列有 prev，拔節點只要四行指標操作 → O(1) ✔</text>
            <text x="20" y="382" fill="var(--accent)" font-size="13">為什麼要兩個虛擬節點（head / tail）？</text>
            <text x="40" y="410" fill="var(--text-muted)" font-size="12">有了它們，任何真實節點都保證「前後都有東西」——</text>
            <text x="40" y="436" fill="var(--gold)" font-size="12">_remove 和 _add_front 就完全不用判斷「是不是第一個 / 最後一個」。</text>
            <text x="20" y="470" fill="#ff8a65" font-size="12">★ 節點裡為什麼要存 key？淘汰時只拿得到節點，但要 del table[key] —— 沒存 key 就找不回去。</text>'''

emit({
 "num": 146, "slug": "lru-cache",
 "en": [
   "Design a data structure that follows the constraints of a "
   "<strong>Least Recently Used (LRU) cache</strong>.",
   "Implement the <code>LRUCache</code> class:",
   ("raw", "<ul>"
           "<li><code>LRUCache(int capacity)</code> Initialize the LRU cache with "
           "<strong>positive</strong> size <code>capacity</code>.</li>"
           "<li><code>int get(int key)</code> Return the value of the <code>key</code> if the "
           "<code>key</code> exists, otherwise return <code>-1</code>.</li>"
           "<li><code>void put(int key, int value)</code> Update the value of the "
           "<code>key</code> if the <code>key</code> exists. Otherwise, add the "
           "<code>key-value</code> pair to the cache. If the number of keys exceeds the "
           "<code>capacity</code> from this operation, <strong>evict</strong> the least recently "
           "used key.</li></ul>"),
   "The functions <code>get</code> and <code>put</code> must each run in <code>O(1)</code> "
   "average time complexity.",
 ],
 "zh": [
   "設計一個<strong>最近最少使用（LRU）快取</strong>。",
   ("ul", [
     "<code>LRUCache(capacity)</code>：用一個<strong>正整數</strong>容量初始化。",
     "<code>get(key)</code>：存在就回傳值，不存在回傳 <code>-1</code>。",
     "<code>put(key, value)</code>：key 存在就更新值；不存在就新增。"
     "如果因此超過容量，<strong>淘汰最久沒被使用的那一筆</strong>。",
   ]),
   "<strong><code>get</code> 和 <code>put</code> 都必須是平均 <code>O(1)</code>。</strong>",
   ("note", "什麼算「使用過」？", [
     "<strong><code>get</code> 和 <code>put</code> 都算</strong> —— "
     "只要碰到某個 key，它就變成「最近使用過」。",
     "<strong>包括「<code>put</code> 一個已存在的 key」</strong>（更新值也算使用）。",
     "<strong>失敗的 <code>get</code>（回傳 -1）不算</strong>，因為那個 key 根本不在快取裡。",
   ]),
 ],
 "pre": [
   ("note", "★ 為什麼要「兩個資料結構」？", [
     ("c", """需求有兩個，而且沒有單一結構能同時做到：

    (a) 用 key 快速找到值           -> 雜湊表 O(1) ✔
                                       但雜湊表【沒有順序】✘

    (b) 快速知道「誰最久沒用」+ 快速調整順序
                                    -> 鏈結串列有順序 ✔
                                       但用 key 查找要 O(n) ✘

【解法：兩個結構搭在一起】

    雜湊表：key -> 節點的【位址】
    雙向鏈結串列：維護「使用順序」

    get(key)：
        1. 雜湊表 O(1) 找到節點
        2. 把節點從串列裡拔出來，插到最前面（O(1)）

    put 滿了：
        1. 串列的最後一個就是「最久沒用的」
        2. 拔掉它，並從雜湊表刪掉（O(1)）

【★ 為什麼必須是「雙向」串列？】

    要把節點從【中間】拔出來，需要改「前一個的 next」。

    單向串列只知道 next，
    要找前一個得從頭走 -> O(n) ✘

    雙向串列有 prev -> O(1) ✔

【★ 為什麼節點裡要存 key？】

    淘汰時，我們是從【串列尾端】拿到節點的，
    但還要 del table[key] ——

    如果節點只存 value，就不知道該刪雜湊表的哪一筆 ✘

    【這是本題最常見的漏寫。】"""),
   ]),
 ],
 "examples": """範例
  輸入：
    ["LRUCache","put","put","get","put","get","put","get","get","get"]
    [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

  輸出：
    [null,null,null,1,null,-1,null,-1,3,4]

  說明（容量 = 2）：
    put(1,1)   快取 = {1=1}
    put(2,2)   快取 = {1=1, 2=2}
    get(1)     回傳 1，  快取 = {2=2, 1=1}   （1 變成最近使用）
    put(3,3)   超過容量 -> 淘汰 key 2
               快取 = {1=1, 3=3}
    get(2)     回傳 -1（已被淘汰）
    put(4,4)   淘汰 key 1，快取 = {3=3, 4=4}
    get(1)     回傳 -1
    get(3)     回傳 3
    get(4)     回傳 4""",
 "constraints": [
   "1 ≤ <code>capacity</code> ≤ 3000",
   "0 ≤ <code>key</code> ≤ 10⁴",
   "0 ≤ <code>value</code> ≤ 10⁵",
   "最多會呼叫 2 × 10⁵ 次 <code>get</code> 和 <code>put</code>",
 ],
 "idea": [
   ("fig", _P146_FIG, "0 0 640 490"),
   ("c", """【資料結構】

    table: dict     key -> Node
    雙向串列：       head <-> ... <-> tail

        head.next = 最近使用過的
        tail.prev = 最久沒使用的

【兩個虛擬節點（dummy head / tail）】

    有了它們，任何真實節點都保證「前後都有東西」。

    _remove(node):
        node.prev.next = node.next
        node.next.prev = node.prev
        -> 完全不用判斷「是不是第一個 / 最後一個」✔

    沒有虛擬節點的話，這兩行會有四種特例要處理
    （是頭 / 是尾 / 又是頭又是尾 / 都不是）。

    【虛擬節點是鏈結串列題的萬用技巧】——
    第 2、21、24、82、86、117、148 題全都用它。

【get(key)】
    不在 -> -1
    在   -> 拔出來、插到最前面、回傳值

【put(key, value)】
    已存在 -> 更新值、拔出來、插到最前面
    不存在 -> 若滿了先淘汰 tail.prev，再插到最前面

【複雜度】：兩個操作都是 O(1) ✔"""),
 ],
 "approaches": [
   ap("解法一", "雜湊表 + 雙向鏈結串列（標準答案）", [
     ("c", S["p146_dll"]),
     ("h", "<code>_remove</code> 和 <code>_add_front</code> 的四行指標操作"),
     ("c", """def _remove(self, node):
    node.prev.next = node.next
    node.next.prev = node.prev

    「讓前後兩個直接牽起手」——
    node 就被跳過了。

def _add_front(self, node):
    node.next = self.head.next      ① node 指向原本的第一個
    node.prev = self.head           ② node 指回 head
    self.head.next.prev = node      ③ 原本的第一個指回 node
    self.head.next = node           ④ head 指向 node

    【★ ③ 一定要在 ④ 之前】——
    ④ 執行之後 self.head.next 就變成 node 了，
    ③ 就會變成 node.prev = node（自環）✘

    這又是「動指標前先用完舊值」的鐵律。

【背下這兩個四行函式】，
    LRU、LFU、以及任何「要 O(1) 搬動元素」的設計題都用得上。""",),
     ("h", "<code>__slots__</code> 這一行是做什麼的？"),
     ("c", """__slots__ = ("key", "val", "prev", "next")

    告訴 Python「這個類別只有這四個屬性」，
    於是它就【不用替每個實例建一個 __dict__】。

    好處：
        ✔ 記憶體省很多（每個實例省掉一個字典，約 50 bytes+）
        ✔ 屬性存取略快

    壞處：
        ✘ 不能動態加屬性
        ✘ 不能多重繼承有 __slots__ 的類別

【本題最多 3000 個節點，其實不加也沒差】。

    但在「會建立大量小物件」的場合
    （例如圖的節點、遊戲的粒子），
    __slots__ 是很划算的優化。

    面試時加上它會顯示你在意實務細節。""",),
     ("h", "<code>put</code> 的三種情況"),
     ("c", """1. key 已存在
       -> 更新 val、搬到最前面
       【不會觸發淘汰】（總數沒變）

2. key 不存在、還沒滿
       -> 直接新增到最前面

3. key 不存在、已經滿了
       -> 先淘汰 tail.prev，再新增

【常見的 bug】：
    把「已存在」的情況也走「檢查是否滿了」的路徑
    -> 更新一個已存在的 key 時卻淘汰了別人 ✘

    所以要用 return 提早結束（本文的寫法），
    或者用 if/elif 分清楚。""",),
     "<strong>兩個操作都是 O(1)，空間 O(capacity)。</strong>",
   ], "O(1) 每次操作", "O(capacity)", "雜湊 + 指標都是 O(1)", "表 + 串列", optimal=True),

   ap("解法二", "<code>OrderedDict</code>（Python 的捷徑）", [
     ("c", S["p146_od"]),
     ("c", """collections.OrderedDict 本身就是
【雜湊表 + 雙向鏈結串列】的組合 ——

    它記得插入順序，而且提供：

        move_to_end(key)        把某個 key 搬到尾端    O(1)
        popitem(last=False)     彈出【最前面】的       O(1)

    正好就是 LRU 需要的兩個操作 ✔

【八行解完。】

【面試時可以用嗎？】

    要看情況：

    ✔ 如果面試官想看「你會不會用工具」-> 可以
    ✘ 如果面試官想看「你懂不懂資料結構」-> 不行

    【最好的做法】：
        先寫 OrderedDict 版（三十秒），
        然後說「這底層就是雜湊表 + 雙向串列，
        我可以手刻一個給你看」，
        再寫解法一。

    這樣兩邊都照顧到了。

【Python 3.7+ 的普通 dict 也記得插入順序】，
    但它【沒有 move_to_end 和 popitem(last=False)】——
    所以還是要用 OrderedDict。

    （普通 dict 可以用 del + 重新插入來模擬 move_to_end，
      但那樣就沒有 O(1) 的保證了… 
      實際上 CPython 的 dict 刪除+插入也是 O(1) 攤還，
      所以也行，只是語意不清楚。）""",),
     "<strong>兩個操作都是 O(1)，程式碼只有解法一的三分之一。</strong>",
   ], "O(1) 每次操作", "O(capacity)", "同解法一", "OrderedDict"),
 ],
 "compare": (["解法", "get", "put", "行數", "面試評價"],
   [["一、手刻雜湊 + 雙向串列", "O(1)", "O(1)", "45", "★★★ 展示基本功"],
    ["二、OrderedDict", "O(1)", "O(1)", "15", "★★☆ 要能說出底層"]]),
 "edges": [
   "<strong><code>capacity = 1</code></strong> → 每次 <code>put</code> 新 key 都會淘汰前一個。",
   "<strong><code>get</code> 不存在的 key</strong> → <code>-1</code>，"
   "<strong>而且不改變任何順序。</strong>",
   "<strong><code>put</code> 已存在的 key</strong> → "
   "<strong>更新值 + 變成最近使用，但【不淘汰任何東西】。</strong>"
   "<strong>把這個情況也走「檢查滿了」的路徑是本題最常見的 bug。</strong>",
   "<strong>淘汰時忘了 <code>del table[key]</code></strong> → "
   "<strong>雜湊表越積越大，而且會查到已經被拔掉的節點。</strong>",
   "<strong>節點裡沒存 <code>key</code></strong> → 淘汰時不知道要刪雜湊表的哪一筆。",
   "<strong><code>_add_front</code> 的第 ③④ 行順序寫反</strong> → 產生自環。",
   "<strong>用單向串列</strong> → 拔節點要 O(n)，不滿足 O(1) 的要求。",
   "<strong>2 × 10⁵ 次操作</strong> → O(1) 每次，總共 20 萬次，輕鬆。",
 ],
 "follow": [
   ("h", "追問一：LFU 快取（第 460 題）要怎麼做？"),
   ("c", """LRU：淘汰「最久沒用的」
LFU：淘汰「使用次數最少的」（次數相同時淘汰最久沒用的）

【LFU 的結構】：

    table:  key -> 節點
    freq_map: 次數 -> 一條雙向串列（那個次數的所有 key，按 LRU 排序）
    min_freq: 目前最小的次數

    get / put 時：
        1. 把節點從 freq_map[f] 移到 freq_map[f+1]
        2. 如果 freq_map[min_freq] 空了，min_freq += 1

    淘汰時：
        取 freq_map[min_freq] 的最後一個

【關鍵洞察：min_freq 只會 +1 或在插入時歸 1】——
    所以不用「找最小值」，O(1) 維護 ✔

    LFU 比 LRU 難不少，但結構是同一套思路：
    【用「多個串列 + 一個索引」維護複合的順序】。""",),
   ("h", "追問二：真實系統裡用的是 LRU 嗎？"),
   ("c", """很少用【精確】的 LRU，因為：

    ✘ 每次讀取都要改鏈結串列 -> 在多執行緒下要加鎖，
       而那個鎖會變成瓶頸
    ✘ 對「掃描型」存取很不利
       （一次大掃描會把有用的東西全部擠出去）

【實務上的替代方案】：

    Clock / Second-Chance：
        用一個環形陣列 + reference bit，近似 LRU，
        但不用每次讀取都改結構。
        （作業系統的分頁置換用這個。）

    Segmented LRU / 2Q：
        分成「新來的」和「常用的」兩區，
        抗掃描能力強很多。

    TinyLFU / W-TinyLFU：
        用 Count-Min Sketch 估計頻率，
        只有「比要被淘汰的那個更常用」才准進來。
        （Caffeine、Redis 的近似 LRU 都是這一類。）

【面試題是 LRU，真實系統是它的各種近似與改良】——
    知道這個差距本身就是加分項。""",),
   ("h", "追問三：如果要支援「多執行緒」呢？"),
   "<strong>最簡單：整個 <code>get</code>/<code>put</code> 加一把大鎖</strong> —— "
   "正確但吞吐量差（所有執行緒排隊）。",
   "<strong>更好的做法</strong>："
   "<strong>分片（sharding）</strong> —— 把 key 依雜湊值分成 N 個獨立的 LRU，"
   "每個有自己的鎖。<strong>N 個執行緒可以同時操作不同的分片。</strong>",
   "<strong>代價：淘汰不再是「全域最久沒用」，而是「該分片裡最久沒用」</strong> —— "
   "<strong>近似，但實務上完全可以接受。</strong>",
   ("h", "追問四：為什麼用「雙向串列」而不是「陣列」或「堆」？"),
   ("c", """陣列：
    搬到最前面要移動所有元素 -> O(n) ✘

堆（heap）：
    如果用「時間戳」當優先權，
    取最小是 O(1)，但【更新某個元素的優先權】要 O(log n)
    而且要能「找到那個元素在堆裡的位置」（需要額外索引）
    -> O(log n)，不滿足 O(1) ✘

雙向串列：
    拔出 + 插入頭部都是 O(1) ✔
    而且「最久沒用的」永遠在尾端，取出也是 O(1) ✔

【選資料結構的思路】：

    列出所有需要的操作，
    然後找「每一個操作都夠快」的結構。

    這題需要：
        依 key 查找     -> 雜湊表
        調整順序        -> 雙向串列
        取出「最舊的」  -> 雙向串列的尾端

    沒有單一結構全包 -> 組合兩個。

    【「組合資料結構」是設計題的核心能力。】""",),
 ],
 "related": [
   "<strong>第 460 題 LFU Cache</strong> —— 按使用次數淘汰，更難",
   "<strong>第 155 題 Min Stack</strong> —— 另一個「組合結構」的設計題",
   "<strong>第 380 題 O(1) 時間插入刪除和取隨機元素</strong> —— 雜湊表 + 陣列",
   "<strong>第 707 題 設計鏈結串列</strong> —— 雙向串列的基本操作",
 ],
 "check": [
   "為什麼需要「雜湊表」和「雙向串列」兩個結構？各自解決什麼問題？",
   "為什麼必須是<strong>雙向</strong>串列？單向會慢在哪裡？",
   "節點裡為什麼要存 <code>key</code>？不存會在哪一步卡住？",
   "<code>put</code> 一個<strong>已存在</strong>的 key 時，會不會淘汰別人？",
 ],
})
print("P146 written")

# ==================== 147. Insertion Sort List ====================
S["p147"] = '''class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)                 # 虛擬頭：省掉「插在最前面」的特判
        cur = head

        while cur:
            nxt = cur.next                  # ★ 先存起來（等一下 cur.next 會被改）

            # 從頭找插入位置：第一個「下一個比 cur 大」的地方
            p = dummy
            while p.next and p.next.val <= cur.val:
                p = p.next

            cur.next = p.next               # 把 cur 插進 p 後面
            p.next = cur
            cur = nxt

        return dummy.next'''

S["p147_opt"] = '''class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        last = head                         # 已排序部分的最後一個節點
        cur = head.next if head else None

        while cur:
            if last.val <= cur.val:
                last = last.next            # 已經有序 -> 直接延伸，不用找位置
            else:
                p = dummy
                while p.next.val <= cur.val:
                    p = p.next
                last.next = cur.next        # 把 cur 從原位拔掉
                cur.next = p.next           # 插到 p 後面
                p.next = cur
            cur = last.next

        return dummy.next'''

S["p147_array"] = '''class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 把值倒進陣列排序，再寫回去（能過，但沒在練這題想考的東西）
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        vals.sort()
        cur = head
        for v in vals:
            cur.val = v
            cur = cur.next

        return head'''


_p147 = [S.load(k) for k in ("p147", "p147_opt", "p147_array")]

for vals in [[4, 2, 1, 3], [-1, 5, 3, 4, 0], [], [1], [1, 1, 1], [3, 2, 1]]:
    want = sorted(vals)
    for sol in _p147:
        h = sol.insertionSortList(to_list(vals))
        assert from_list(h) == want, ("P147", vals, want, from_list(h), sol)

for _ in range(4000):
    n = random.randrange(0, 15)
    vals = [random.randint(-30, 30) for _ in range(n)]
    want = sorted(vals)
    for sol in _p147:
        h = sol.insertionSortList(to_list(vals))
        assert from_list(h) == want, ("P147 random", vals, want, sol)
print("P147 solutions OK")

emit({
 "num": 147, "slug": "insertion-sort-list",
 "en": [
   "Given the <code>head</code> of a singly linked list, sort the list using "
   "<strong>insertion sort</strong>, and return <em>the sorted list's head</em>.",
   "The steps of the <strong>insertion sort</strong> algorithm:",
   ("raw", "<ul>"
           "<li>Insertion sort iterates, consuming one input element each repetition and "
           "growing a sorted output list.</li>"
           "<li>At each iteration, insertion sort removes one element from the input data, "
           "finds the location it belongs within the sorted list and inserts it there.</li>"
           "<li>It repeats until no input elements remain.</li></ul>"),
 ],
 "zh": [
   "給你一條單向鏈結串列，用<strong>插入排序</strong>把它排好，回傳排序後的頭節點。",
   "<strong>插入排序</strong>的步驟：",
   ("ul", [
     "維護一段「已排序」的部分，每次從輸入取一個元素。",
     "在已排序的部分裡<strong>找到它該待的位置</strong>，插進去。",
     "重複到輸入用完。",
   ]),
 ],
 "pre": [
   ("note", "插入排序在鏈結串列上，反而比在陣列上「自然」", [
     ("c", """【陣列的插入排序】：

    找到位置之後，要把後面的元素【全部往後搬一格】
    -> 每次插入 O(n) 的搬移

【串列的插入排序】：

    找到位置之後，【改兩個指標】就好
    -> 每次插入 O(1) ✔

    （但「找位置」還是要 O(n)，所以總共還是 O(n²)。）

【所以串列版省掉了「搬移」這件事】——
    這是鏈結串列相對於陣列的經典優勢：
    「在中間插入 / 刪除是 O(1)（只要你已經在那個位置）」。

    代價是「找到那個位置」要 O(n)（不能隨機存取）。

【本題的核心技巧】：

    (a) 虛擬頭節點（dummy）—— 省掉「插在最前面」的特判
    (b) 先存 cur.next 再改指標 —— 鏈結串列的鐵律
    (c) 「已經有序就跳過」的優化（解法二）"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [4,2,1,3]
  輸出：[1,2,3,4]

  過程：
    已排序 []        取 4  -> [4]
    已排序 [4]       取 2  -> [2,4]
    已排序 [2,4]     取 1  -> [1,2,4]
    已排序 [1,2,4]   取 3  -> [1,2,3,4]

範例 2
  輸入：head = [-1,5,3,4,0]
  輸出：[-1,0,3,4,5]""",
 "constraints": [
   "串列的節點數在 <code>[1, 5000]</code> 之間",
   "−5000 ≤ <code>Node.val</code> ≤ 5000",
 ],
 "mid": [
   ("note", "節點數只有 5000 —— 這是在說「O(n²) 可以接受」", [
     "<strong>5000² = 2500 萬</strong>，在時限內。",
     "<strong>如果上限是 5 × 10⁴（像第 148 題那樣），O(n²) 就會逾時</strong> —— "
     "<strong>那時就必須用歸併排序。</strong>",
     "<strong>看到「題目指定演算法」+「不大的 n」，就知道它真的要你寫那個演算法。</strong>",
   ]),
 ],
 "idea": [
   ("c", """【基本版】

    dummy = ListNode(0)         虛擬頭，已排序的部分掛在它後面
    cur = head

    while cur:
        nxt = cur.next          ★ 先存起來

        p = dummy               從頭找插入位置
        while p.next and p.next.val <= cur.val:
            p = p.next

        cur.next = p.next       插進 p 後面
        p.next = cur

        cur = nxt

    return dummy.next

【★ 為什麼要先存 nxt？】

    cur.next = p.next 這一行會【覆蓋掉 cur.next】。

    不先存的話，cur = cur.next 就會跳到錯的地方
    （跳進已排序的部分，造成無窮迴圈或亂序）。

    【動指標之前先把要用的存起來 —— 鏈結串列第一鐵律。】

【★ 為什麼需要 dummy？】

    如果 cur 比所有已排序的都小，它要插在【最前面】。

    沒有 dummy 的話，「插在最前面」和「插在中間」
    是兩段不同的程式碼（要改 head 這個變數）。

    有了 dummy，「最前面」也只是「dummy 後面」——
    完全一樣的程式碼 ✔

【★ 為什麼是 <= 而不是 <？】

    p.next.val <= cur.val -> 繼續往後

    用 <= 的話，相同的值會讓 cur 插在【後面】
    -> 排序是【穩定的】（相同元素保持原本的相對順序）✔

    用 < 的話會插在前面 -> 不穩定。

    這題不要求穩定，但「預設寫成穩定的」是好習慣。

【複雜度】：最壞 O(n²)（每次都要從頭找）、O(1) 額外空間。"""),
 ],
 "approaches": [
   ap("解法一", "虛擬頭 + 每次從頭找位置（標準答案）", [
     ("c", S["p147"]),
     "<strong>十二行，O(n²) 時間、O(1) 空間。</strong>",
     ("h", "為什麼「從 <code>dummy</code> 開始找」而不是從上次的位置？"),
     ("c", """因為新來的 cur 可能比【任何】已排序的元素都小 ——
必須從頭開始檢查。

    只有在「輸入已經接近有序」時，
    「從上次的位置繼續」才划算（那就是解法二的優化）。

【最壞情況】：輸入是【降序】的

    [5, 4, 3, 2, 1]

    每個元素都要插到最前面，
    但我們是從 dummy 往後找 ——
    第 k 個元素要走 0 步就找到（因為它最小）。

    等等，降序輸入時每次都插在最前面，
    反而是【最快】的（每次 O(1)）？

    對！降序輸入時，插入排序在串列上是 O(n)。

【真正的最壞情況是【升序】輸入】：

    [1, 2, 3, 4, 5]

    每個元素都要插到最後面 ->
    第 k 個要走 k 步 -> 總共 O(n²) ✘

    【這和陣列版的插入排序【相反】】：
        陣列版：升序輸入最快（不用搬移），降序最慢
        串列版：降序輸入最快（都插在頭），升序最慢

    因為串列只能「從頭往後找」，沒有「從後往前比」的能力。

【解法二的優化正是針對這個】——
    「已經有序就不用找」，讓升序輸入變成 O(n)。""",),
     ("h", "<code>while p.next and ...</code> 的兩個條件"),
     "<code>p.next</code> <strong>是 <code>None</code> 代表已經走到已排序部分的尾端</strong> —— "
     "<strong><code>cur</code> 就插在那裡（最大的位置）。</strong>",
     "<strong>少檢查這個會 <code>AttributeError</code>。</strong>",
   ], "O(n²)", "O(1)", "每次找位置 O(n)", "幾個指標", optimal=True),

   ap("解法二", "加上「已經有序就跳過」的優化", [
     ("c", S["p147_opt"]),
     ("h", "★ 一個判斷，讓「接近有序」的輸入變成 O(n)"),
     ("c", """if last.val <= cur.val:
    last = last.next        # 已經在正確位置 -> 不用找，直接延伸
else:
    ...從頭找位置並插入...

    last 是「已排序部分的最後一個」。

    如果 cur >= last，代表 cur 本來就該在最後面 ——
    完全不用搜尋 ✔

【效果】：

    完全升序的輸入 [1,2,3,4,5]：
        每次都走 if 分支 -> O(1)
        總共 O(n) ✔       （解法一是 O(n²)）

    完全降序的輸入：
        每次都走 else 分支，但都插在最前面 -> O(1)
        總共 O(n) ✔

    隨機輸入：
        平均還是 O(n²)，但常數小很多。

【這個優化叫做「自然插入排序」的思路】——

    真實世界的資料常常是「接近有序」的
    （例如日誌、時間序列、部分更新過的清單）。

    對這類輸入，插入排序反而比快速排序快 ——
    這就是為什麼 Timsort（Python 的 sort）
    在小分段上用的是插入排序。

【★ 這個版本的 last.next = cur.next 那一行】

    要把 cur 從【原本的位置】拔掉，
    才能插到前面去。

    解法一不用這一步，因為它是「一個一個從輸入取」，
    而這個版本是「原地調整」。

    兩種寫法的結構不同，不要混。""",),
     "<strong>最壞仍是 O(n²)，但對「接近有序」的輸入是 O(n)。</strong>",
   ], "O(n²) 最壞 / O(n) 接近有序", "O(1)", "有序時不搜尋", "幾個指標"),

   ap("解法三", "倒進陣列排序（能過，但沒在解這題）", [
     ("c", S["p147_array"]),
     ("c", """把值倒進 list、呼叫 sort()、再寫回去。

    O(n log n) 時間、O(n) 空間 ——
    【比插入排序還快】。

【但這完全不是題目想要的】：

    題目明確說「用插入排序」。

    寫這個等於回答「我不做你要的事，我用內建函式」。

【什麼時候這樣寫是對的？】

    ✔ 真實工程裡（除非有特殊理由，用內建排序永遠是對的）
    ✔ 題目沒有指定演算法（例如第 148 題只說「排序」）

    ✘ 題目明確指定演算法（本題）
    ✘ 面試官想看你會不會操作指標

【放在這裡是為了指出這個區別】：

    「能通過測試」和「解決了題目要考的問題」
    是兩件不同的事。

    第 148 題（排序串列）就允許這個做法，
    但那題的進階要求是 O(1) 空間 —— 又把它排除了。""",),
   ], "O(n log n)", "O(n)", "內建排序", "值的陣列"),
 ],
 "compare": (["解法", "時間", "空間", "符合題意", "備註"],
   [["一、虛擬頭 + 從頭找", "O(n²)", "O(1)", "✔", "標準答案"],
    ["二、加上有序跳過", "O(n²) / O(n)", "O(1)", "✔", "接近有序時快很多"],
    ["三、倒進陣列排序", "O(n log n)", "O(n)", "✘", "沒在解這題"]]),
 "edges": [
   "<strong>空串列</strong>（題目保證不會）→ <code>dummy.next</code> 是 <code>None</code> ✔ 自然正確。",
   "<strong>單一節點</strong> → 不變。",
   "<strong>已經有序</strong> <code>[1,2,3]</code> → "
   "<strong>解法一是 O(n²)（最壞情況），解法二是 O(n)。</strong>",
   "<strong>完全降序</strong> <code>[3,2,1]</code> → "
   "<strong>每次都插在最前面，兩個解法都是 O(n)。</strong>",
   "<strong>全部相同</strong> <code>[1,1,1]</code> → "
   "<strong>用 <code>&lt;=</code> 的話走到最後才插（穩定）。</strong>",
   "<strong>忘了先存 <code>nxt = cur.next</code></strong> → "
   "<strong>改完指標後跳進已排序的部分，無窮迴圈或亂序。本題第一名的 bug。</strong>",
   "<strong>沒用 <code>dummy</code></strong> → 「插在最前面」要額外寫一段。",
   "<strong><code>while p.next.val &lt;= ...</code> 忘了檢查 <code>p.next</code></strong> → "
   "<code>AttributeError</code>。",
   "<strong>5000 個節點</strong> → 最壞 2500 萬次比較，在時限內。",
 ],
 "follow": [
   ("h", "追問一：如果 <code>n</code> 是 5 × 10⁴ 呢？"),
   "<strong>O(n²) = 25 億，一定逾時。</strong>"
   "<strong>那就是第 148 題（Sort List）—— 必須用 O(n log n) 的歸併排序。</strong>",
   "<strong>為什麼是歸併而不是快排？</strong>"
   "<strong>因為快排需要「隨機存取」來做 partition，而串列做不到；</strong>"
   "<strong>歸併只需要「循序走訪」和「切一半」，正好適合串列。</strong>",
   ("h", "追問二：插入排序什麼時候比 O(n log n) 的排序好？"),
   ("ul", [
     "<strong>n 很小</strong>（通常 < 32）→ 常數小，實測更快。"
     "<strong>Timsort、introsort 都在小分段上切換成插入排序。</strong>",
     "<strong>資料接近有序</strong> → 解法二是 O(n)，比任何 O(n log n) 都快。",
     "<strong>需要「穩定」而且不能用額外空間</strong> → 插入排序天然穩定且原地。",
     "<strong>線上（online）排序</strong> → 資料一筆一筆來，插入排序可以「邊來邊排」，"
     "而歸併/快排必須先看到全部。",
   ]),
   "<strong>「O(n²) 的演算法永遠比較差」是錯的</strong> —— "
   "<strong>漸進複雜度只描述「n 很大時」的行為。</strong>",
   ("h", "追問三：這題的插入排序是穩定的嗎？"),
   ("c", """是的 —— 只要比較寫成 <= 就穩定。

    while p.next and p.next.val <= cur.val:
        p = p.next

    「已排序部分裡和 cur 相等的元素」會被跳過，
    所以 cur 插在它們【後面】——
    保持了原本的相對順序 ✔

    改成 < 的話，cur 會插在相等元素的【前面】-> 不穩定。

【穩定性什麼時候重要？】

    當你要「先按 A 排序，再按 B 排序」而且
    希望 B 相同時保持 A 的順序時。

    例如：先按姓名排，再按部門排
    -> 穩定排序能讓同部門的人仍然按姓名排好 ✔

    Python 的 sorted 和 list.sort 都是穩定的（Timsort），
    所以可以安心地「多次排序」。

    C++ 的 std::sort【不保證穩定】（要用 stable_sort）。""",),
   ("h", "追問四：能不能在串列上做「二分插入排序」？"),
   "<strong>不行 —— 二分搜尋需要 O(1) 隨機存取，而串列沒有。</strong>",
   "<strong>在陣列上，「二分找位置 + 線性搬移」可以把【比較次數】降到 O(n log n)，"
   "但【搬移次數】還是 O(n²) —— 所以總複雜度不變。</strong>",
   "<strong>在串列上，「找位置」本來就是 O(n)，二分幫不上忙；</strong>"
   "<strong>但「插入」是 O(1)（不用搬移）—— 剛好和陣列相反。</strong>",
   "<strong>兩種結構的優缺點正好互補，這個對照值得記住。</strong>",
 ],
 "related": [
   "<strong>第 148 題 Sort List</strong> —— n 更大時要用歸併排序",
   "<strong>第 21 題 Merge Two Sorted Lists</strong> —— 虛擬頭 + tail 的原型",
   "<strong>第 86 題 Partition List</strong> —— 兩個虛擬頭",
   "<strong>第 708 題 Insert into a Sorted Circular Linked List</strong> —— 環狀版的插入",
 ],
 "check": [
   "為什麼一定要先存 <code>nxt = cur.next</code>？",
   "<code>dummy</code> 省掉了什麼特判？",
   "串列版的插入排序，最壞情況是「升序輸入」還是「降序輸入」？為什麼和陣列版相反？",
   "比較寫成 <code>&lt;=</code> 還是 <code>&lt;</code>，對穩定性有什麼影響？",
 ],
})
print("P147 written")

# ==================== 148. Sort List ====================
S["p148_topdown"] = '''class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head                     # 0 或 1 個節點，本來就有序

        # 快慢指標找中點（slow 停在前半的最後一個）
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None                    # ★ 切斷，變成兩條獨立的串列

        left = self.sortList(head)
        right = self.sortList(mid)
        return self._merge(left, right)

    def _merge(self, a, b):
        dummy = tail = ListNode(0)
        while a and b:
            if a.val <= b.val:              # <= 保證穩定
                tail.next = a
                a = a.next
            else:
                tail.next = b
                b = b.next
            tail = tail.next
        tail.next = a or b                  # 接上剩下的那一條
        return dummy.next'''

S["p148_bottomup"] = '''class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先數長度
        n, p = 0, head
        while p:
            n += 1
            p = p.next

        dummy = ListNode(0, head)
        size = 1
        while size < n:                     # 每輪把「長度 size」的相鄰兩段合併
            prev, cur = dummy, dummy.next
            while cur:
                left = cur
                right = self._split(left, size)     # 切出左段，回傳右段的頭
                cur = self._split(right, size)      # 切出右段，回傳下一組的頭
                prev = self._merge_to(prev, left, right)
            size *= 2

        return dummy.next

    def _split(self, node, size):
        """往前走 size-1 步，切斷，回傳後面那一段的頭"""
        for _ in range(size - 1):
            if not node:
                break
            node = node.next
        if not node:
            return None
        rest = node.next
        node.next = None
        return rest

    def _merge_to(self, prev, a, b):
        """把 a 和 b 合併之後接在 prev 後面，回傳新的尾巴"""
        cur = prev
        while a and b:
            if a.val <= b.val:
                cur.next = a; a = a.next
            else:
                cur.next = b; b = b.next
            cur = cur.next
        cur.next = a or b
        while cur.next:
            cur = cur.next
        return cur'''

S["p148_array"] = '''class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 倒進陣列排序再寫回（O(n) 空間，但最短也最快）
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        vals.sort()
        cur = head
        for v in vals:
            cur.val = v
            cur = cur.next

        return head'''


_p148 = [S.load(k) for k in ("p148_topdown", "p148_bottomup", "p148_array")]

for vals in [[4, 2, 1, 3], [-1, 5, 3, 4, 0], [], [1], [2, 1],
             [1, 1, 1], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]]:
    want = sorted(vals)
    for sol in _p148:
        h = sol.sortList(to_list(vals))
        assert from_list(h) == want, ("P148", vals, want, from_list(h), sol)

for _ in range(3000):
    n = random.randrange(0, 25)
    vals = [random.randint(-40, 40) for _ in range(n)]
    want = sorted(vals)
    for sol in _p148:
        h = sol.sortList(to_list(vals))
        assert from_list(h) == want, ("P148 random", vals, want, sol)
print("P148 solutions OK")

_P148_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">為什麼串列要用【歸併】而不是快排？因為歸併只需要「循序走訪」和「切一半」——串列都做得到。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">自頂向下（遞迴）：切一半 → 各自排好 → 合併</text>
            <g font-size="12" text-anchor="middle">
              <rect x="230" y="70" width="180" height="26" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="320" y="88" fill="var(--gold)">[4, 2, 1, 3]</text>
              <rect x="120" y="126" width="120" height="26" fill="none" stroke="var(--accent)"/><text x="180" y="144" fill="var(--accent)">[4, 2]</text>
              <rect x="400" y="126" width="120" height="26" fill="none" stroke="var(--accent)"/><text x="460" y="144" fill="var(--accent)">[1, 3]</text>
              <rect x="70" y="182" width="70" height="26" fill="none" stroke="var(--text-muted)"/><text x="105" y="200" fill="var(--text-muted)">[4]</text>
              <rect x="160" y="182" width="70" height="26" fill="none" stroke="var(--text-muted)"/><text x="195" y="200" fill="var(--text-muted)">[2]</text>
              <rect x="410" y="182" width="70" height="26" fill="none" stroke="var(--text-muted)"/><text x="445" y="200" fill="var(--text-muted)">[1]</text>
              <rect x="500" y="182" width="70" height="26" fill="none" stroke="var(--text-muted)"/><text x="535" y="200" fill="var(--text-muted)">[3]</text>
              <rect x="120" y="240" width="120" height="26" fill="none" stroke="var(--accent)"/><text x="180" y="258" fill="var(--accent)">[2, 4]</text>
              <rect x="400" y="240" width="120" height="26" fill="none" stroke="var(--accent)"/><text x="460" y="258" fill="var(--accent)">[1, 3]</text>
              <rect x="230" y="296" width="180" height="26" fill="none" stroke="var(--gold)" stroke-width="3"/><text x="320" y="314" fill="var(--gold)">[1, 2, 3, 4]</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="280" y1="96" x2="200" y2="120"/><line x1="360" y1="96" x2="440" y2="120"/>
              <line x1="160" y1="152" x2="120" y2="176"/><line x1="200" y1="152" x2="200" y2="176"/>
              <line x1="440" y1="152" x2="450" y2="176"/><line x1="480" y1="152" x2="525" y2="176"/>
            </g>
            <g stroke="var(--gold)" stroke-width="1.5">
              <line x1="115" y1="208" x2="160" y2="234"/><line x1="195" y1="208" x2="195" y2="234"/>
              <line x1="450" y1="208" x2="450" y2="234"/><line x1="530" y1="208" x2="490" y2="234"/>
              <line x1="200" y1="266" x2="280" y2="290"/><line x1="440" y1="266" x2="360" y2="290"/>
            </g>
            <line x1="20" y1="342" x2="620" y2="342" stroke="var(--border)"/>
            <text x="20" y="370" fill="var(--accent)" font-size="12">★ 為什麼串列的歸併排序可以 O(1) 空間，而陣列的不行？</text>
            <text x="40" y="398" fill="var(--text-muted)" font-size="12">陣列合併兩段有序區間時，必須先複製到暫存陣列 → O(n) 空間。</text>
            <text x="40" y="424" fill="var(--gold)" font-size="12">串列只要【改指標】把節點重新串起來 → O(1) 空間 ✔</text>
            <text x="20" y="456" fill="#ff8a65" font-size="12">但自頂向下（遞迴）還是要 O(log n) 的堆疊 —— 真正的 O(1) 要用自底向上（解法二）。</text>'''

emit({
 "num": 148, "slug": "sort-list",
 "en": [
   "Given the <code>head</code> of a linked list, return <em>the list after sorting it in "
   "<strong>ascending order</strong></em>.",
   "<strong>Follow up:</strong> Can you sort the linked list in <code>O(n logn)</code> time and "
   "<code>O(1)</code> memory (i.e. constant space)?",
 ],
 "zh": [
   "給你一條鏈結串列，把它<strong>升序排好</strong>並回傳。",
   "<strong>進階：</strong>你能在 <code>O(n log n)</code> 時間、"
   "<code>O(1)</code> 空間內完成嗎？",
 ],
 "pre": [
   ("note", "★ 為什麼串列排序要用「歸併」而不是「快排」？", [
     ("c", """【快速排序需要什麼？】

    partition：選一個 pivot，把小的放左邊、大的放右邊。

    在陣列上，這靠「兩個指標從兩端往中間夾」做到 ——
    需要【隨機存取】和【從後往前走】。

    串列做不到（只能往前走）✘

    （硬要做的話，可以用「三條子串列」的方式 partition，
      但那樣就不是原地的，而且 pivot 選不好會退化成 O(n²)。）

【歸併排序需要什麼？】

    1. 把序列切成兩半        -> 快慢指標，O(n) ✔
    2. 遞迴排序兩半          -> ✔
    3. 合併兩段有序序列      -> 循序走訪 + 改指標，O(n) ✔

    【三件事串列都做得到，而且第 3 步比陣列還省空間】——

        陣列合併要先複製到暫存陣列 -> O(n) 空間
        串列合併只要改指標        -> O(1) 空間 ✔

【結論】：
    陣列的最佳排序是快排（原地、常數小）
    串列的最佳排序是歸併（不用額外空間、而且穩定）

    【資料結構決定演算法的選擇。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：head = [4,2,1,3]
  輸出：[1,2,3,4]

範例 2
  輸入：head = [-1,5,3,4,0]
  輸出：[-1,0,3,4,5]

範例 3
  輸入：head = []
  輸出：[]""",
 "constraints": [
   "串列的節點數在 <code>[0, 5 × 10⁴]</code> 之間",
   "−10⁵ ≤ <code>Node.val</code> ≤ 10⁵",
 ],
 "mid": [
   ("note", "5 × 10⁴ 這個上限在說什麼", [
     "<strong>O(n²) = 25 億 —— 一定逾時。</strong>"
     "<strong>所以第 147 題的插入排序在這裡行不通。</strong>",
     "<strong>必須是 O(n log n)</strong>：5×10⁴ × 16 ≈ 80 萬，輕鬆。",
     "<strong>而進階要求的 O(1) 空間，排除了「倒進陣列」和「遞迴」兩種做法。</strong>",
   ]),
 ],
 "idea": [
   ("fig", _P148_FIG, "0 0 640 478"),
   ("c", """【自頂向下（遞迴歸併）】

    1. 快慢指標找中點，切成兩條
    2. 遞迴排序兩條
    3. 合併

    O(n log n) 時間、O(log n) 空間（遞迴堆疊）

    【★ 切斷那一步不能忘】：
        slow.next = None

        不切的話，左半的遞迴會一直走到整條串列的尾巴
        -> 無窮遞迴 ✘

【自底向上（迭代歸併）】

    不遞迴，而是「一層一層」由小到大合併：

        size = 1: 合併相鄰的「1 個 + 1 個」
        size = 2: 合併相鄰的「2 個 + 2 個」
        size = 4: 合併相鄰的「4 個 + 4 個」
        ...

    O(n log n) 時間、O(1) 空間 ✔ 滿足進階要求

    【這是本題進階要求的答案，也是它被列為 Medium 的原因。】

【合併兩條有序串列（兩個版本共用）】

    dummy = tail = ListNode(0)
    while a and b:
        if a.val <= b.val: tail.next = a; a = a.next
        else:              tail.next = b; b = b.next
        tail = tail.next
    tail.next = a or b          ★ 接上剩下的那一條
    return dummy.next

    【a or b 這個寫法】：
        a 不是 None 就回 a，否則回 b。
        剛好處理「其中一條先用完」的情況 ✔"""),
 ],
 "approaches": [
   ap("解法一", "自頂向下歸併（遞迴，最好寫）", [
     ("c", S["p148_topdown"]),
     "<strong>O(n log n) 時間、O(log n) 空間（遞迴堆疊）。</strong>"
     "<strong>面試時先寫這個。</strong>",
     ("h", "★ 三個必須寫對的地方"),
     ("c", """1. 【base case 是 not head or not head.next】

   0 個或 1 個節點時直接回傳。

   只寫 not head 的話，單一節點會無窮遞迴：
       slow = head, fast = head.next = None
       mid = slow.next = None
       sortList(head) -> 又是同一個單節點 ✘

2. 【slow, fast = head, head.next】（錯開一步）

   這樣 n = 2 時 slow 停在第一個 -> 切成 [1] 和 [1] ✔

   如果 fast 也從 head 出發：
       n = 2 時 slow 停在第二個 -> 切成 [兩個] 和 [空] ✘
       -> 左半永遠是整條 -> 無窮遞迴

   【這個錯誤會直接 RecursionError，很好發現。】

3. 【slow.next = None】（切斷）

   不切的話兩條會黏在一起 -> 遞迴永遠切不完。

【這三個錯誤的共同症狀都是「無窮遞迴」】——
    看到 RecursionError 時，先檢查這三個地方。""",),
     ("h", "為什麼空間是 O(log n) 而不是 O(n)？"),
     "<strong>因為遞迴樹的深度是 <code>log n</code></strong>（每次切一半）。",
     "<strong>而「合併」這一步完全不用額外空間（只改指標）</strong> —— "
     "<strong>這就是串列相對於陣列的優勢。</strong>",
     "<strong>陣列的歸併排序是 O(n) 空間（暫存陣列）。</strong>",
   ], "O(n log n)", "O(log n)", "遞迴樹深度 log n", "遞迴堆疊", optimal=True),

   ap("解法二", "自底向上歸併（O(1) 空間，滿足進階）", [
     ("c", S["p148_bottomup"]),
     ("h", "★ 「一層一層由小到大合併」"),
     ("c", """size = 1, 2, 4, 8, ... 直到 >= n

    每一輪：
        把串列切成「size 個一組」，
        相鄰兩組合併成一組（長度 2·size）。

    例如 [4, 2, 1, 3]：

        size=1: 合併 (4)(2) -> (2,4)
                合併 (1)(3) -> (1,3)
                結果 [2, 4, 1, 3]

        size=2: 合併 (2,4)(1,3) -> (1,2,3,4) ✔

        size=4 >= n，結束。

【為什麼這樣就不用遞迴了？】

    遞迴歸併是「先切到底，再往上合併」。

    自底向上是「直接從最底層開始合併」——
    完全不需要「記住切了哪些」-> 不用堆疊 ✔

【三個輔助函式】

    _split(node, size)：
        往前走 size-1 步，切斷，回傳後面那段的頭
        （如果不夠長，回傳 None）

    _merge_to(prev, a, b)：
        合併 a 和 b，接在 prev 後面，
        回傳【合併後的尾巴】（好讓下一組接上去）

    這兩個函式是自底向上版最容易寫錯的地方 ——
    特別是「不夠長」的邊界。

【複雜度】

    外層 log n 輪，每輪掃過整條串列 O(n)
    -> O(n log n) 時間 ✔

    只用幾個指標 -> O(1) 空間 ✔

【這是真正滿足進階要求的解法】，
    但它比遞迴版長兩倍，而且邊界很多。

    面試時的順序：
        1. 寫遞迴版，講清楚思路
        2. 說「遞迴用了 O(log n) 堆疊，
           要真正的 O(1) 我會改成自底向上」
        3. 如果時間夠，再寫出來""",),
   ], "O(n log n)", "O(1)", "log n 輪，每輪 O(n)", "只用指標"),

   ap("解法三", "倒進陣列排序（最短，但不滿足進階）", [
     ("c", S["p148_array"]),
     ("c", """O(n log n) 時間、O(n) 空間。

【和第 147 題不同，這題【沒有】指定演算法】——
    所以這個做法在「只求 AC」的意義下是合法的。

    而且實測通常【最快】：
        Python 的 sort 是 C 實作的 Timsort，
        常數比手寫的歸併小很多。

【但它不滿足進階要求的 O(1) 空間。】

【面試時的判斷】：

    ✔ 如果面試官說「隨便你怎麼排」-> 寫這個，三十秒搞定
    ✘ 如果題目/面試官提到 O(1) 空間 -> 必須寫解法二

    而且無論如何，要能說出
    「這是 O(n) 空間，如果要 O(1) 我會用自底向上的歸併」。

【一個中間選項】：
    把【節點】倒進陣列（而不是值），
    用 key=lambda x: x.val 排序，再重新串起來。

    這樣就不用「改值」（有些題目禁止改值），
    空間仍然是 O(n)。""",),
   ], "O(n log n)", "O(n)", "內建 Timsort", "值的陣列"),
 ],
 "compare": (["解法", "時間", "空間", "滿足進階", "行數"],
   [["一、自頂向下歸併", "O(n log n)", "O(log n)", "✘ 差一點", "22"],
    ["二、自底向上歸併", "O(n log n)", "O(1)", "✔", "40"],
    ["三、倒進陣列", "O(n log n)", "O(n)", "✘", "12"]]),
 "edges": [
   "<strong>空串列</strong> → <code>None</code>。<strong>base case 要擋。</strong>",
   "<strong>單一節點</strong> → 不變。"
   "<strong>base case 只寫 <code>not head</code> 會無窮遞迴。</strong>",
   "<strong>兩個節點</strong> <code>[2,1]</code> → <code>[1,2]</code>。"
   "<strong>考驗快慢指標的停法。</strong>",
   "<strong>已經有序</strong> → 歸併排序仍然是 O(n log n)（不會變快）。",
   "<strong>完全降序</strong> → 同上。",
   "<strong>全部相同</strong> → <code>&lt;=</code> 保證穩定。",
   "<strong>忘了 <code>slow.next = None</code></strong> → "
   "<strong>無窮遞迴。本題第一名的 bug。</strong>",
   "<strong><code>fast</code> 從 <code>head</code> 而不是 <code>head.next</code> 出發</strong> → "
   "<strong>兩個節點時切不開，無窮遞迴。</strong>",
   "<strong>5 × 10⁴ 個節點</strong> → 遞迴深度只有 16，安全；"
   "<strong>但 O(n²) 的插入排序會逾時。</strong>",
 ],
 "follow": [
   ("h", "追問一：為什麼歸併排序是「穩定」的？"),
   ("c", """合併時用 <= 而不是 <：

    if a.val <= b.val:
        取 a       ← 相等時優先取【左邊那一條】

    而左邊那一條在原本的串列裡就在前面 ->
    相等元素的相對順序被保持 ✔

    如果寫成 a.val < b.val，相等時會取 b（右邊的）
    -> 順序被交換 -> 不穩定 ✘

【一個字的差別。】

    歸併排序天然可以是穩定的，
    而快速排序【天然不穩定】（partition 會交換遠處的元素）。

    這也是為什麼：
        Python 的 sorted / list.sort -> Timsort（歸併的變形）-> 穩定
        C++ 的 std::sort -> introsort（快排 + 堆排）-> 不穩定
        C++ 的 std::stable_sort -> 歸併 -> 穩定""",),
   ("h", "追問二：能不能在串列上做快速排序？"),
   ("c", """可以，但不好：

    partition 時把節點分成三條子串列：
        小於 pivot、等於 pivot、大於 pivot

    然後遞迴排序第一和第三條，最後接起來。

    O(n log n) 平均、O(n²) 最壞
    O(log n) 空間（遞迴）

【為什麼不好？】

    ✘ 最壞情況 O(n²)（已排序的輸入 + 固定選第一個當 pivot）
    ✘ 沒辦法「隨機選 pivot」（要 O(n) 才能走到隨機位置）
    ✘ 沒有比歸併省空間

    【快排在陣列上的所有優勢（原地、快取友善、常數小）
      在串列上全部消失。】

    這就是「資料結構決定演算法」的最好例子。""",),
   ("h", "追問三：自底向上版為什麼真的是 O(1) 空間？"),
   "<strong>因為它完全不遞迴，只用幾個指標變數</strong>"
   "（<code>prev</code>、<code>cur</code>、<code>left</code>、<code>right</code>、<code>size</code>）。",
   "<strong>合併時也只是改指標，不配置任何新節點</strong>"
   "（<code>dummy</code> 只有一個，而且是在函式開頭建的）。",
   "<strong>「O(1) 空間」的嚴格定義是「額外空間不隨 n 成長」</strong> —— "
   "<strong>常數個變數完全符合。</strong>",
   ("h", "追問四：Timsort 是怎麼運作的？"),
   ("c", """Python 的 sorted / list.sort 用的排序演算法：

    1. 掃描輸入，找出天然的「已排序區段」（run）
       —— 遞增或遞減（遞減的就地反轉）

    2. 太短的 run 用【二分插入排序】擴充到最小長度
       （通常是 32~64）

    3. 把這些 run 用【歸併】合併起來，
       並用一套規則維持「堆疊上的 run 長度平衡」

【為什麼這樣快？】

    ✔ 真實資料常常「部分有序」-> 第 1 步直接撿到便宜
    ✔ 小分段用插入排序 -> 常數小
    ✔ 歸併 -> 穩定，而且最壞仍是 O(n log n)

    完全有序的輸入：O(n) ✔
    隨機輸入：      O(n log n)

【Timsort 是「理論最優」和「實務調校」結合的典範】——
    它的最壞複雜度和歸併一樣，
    但在真實資料上快得多。

    Java、Android、V8（JavaScript）也都採用了它。""",),
 ],
 "related": [
   "<strong>第 147 題 Insertion Sort List</strong> —— n 小時的 O(n²) 版",
   "<strong>第 21 題 Merge Two Sorted Lists</strong> —— 合併那一步",
   "<strong>第 23 題 Merge k Sorted Lists</strong> —— 合併 k 條",
   "<strong>第 876 題 Middle of the Linked List</strong> —— 找中點",
   "<strong>第 143 題 Reorder List</strong> —— 同樣的「找中點 + 切斷」",
 ],
 "check": [
   "為什麼串列適合歸併排序而不適合快速排序？",
   "為什麼串列的歸併合併不需要額外空間，而陣列的需要？",
   "base case 只寫 <code>not head</code> 會發生什麼？",
   "自底向上版為什麼能做到真正的 O(1) 空間？",
 ],
})
print("P148 written")

# ==================== 149. Max Points on a Line ====================
S["p149_slope"] = '''from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        best = 1
        for i in range(n):
            x1, y1 = points[i]
            slopes = defaultdict(int)
            for j in range(i + 1, n):
                dx = points[j][0] - x1
                dy = points[j][1] - y1

                # ★ 用「最簡分數」當 key，不要用浮點數 dy/dx
                g = gcd(dx, dy)             # gcd(0, k) == abs(k)
                dx, dy = dx // g, dy // g

                # 正規化方向：讓 (1,2) 和 (-1,-2) 算同一個斜率
                if dx < 0 or (dx == 0 and dy < 0):
                    dx, dy = -dx, -dy

                slopes[(dx, dy)] += 1
                best = max(best, slopes[(dx, dy)] + 1)   # +1 是 points[i] 自己

        return best'''

S["p149_cross"] = '''class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        best = 2
        for i in range(n):
            for j in range(i + 1, n):
                # 固定一條直線（過 points[i] 和 points[j]），數有幾個點在上面
                x1, y1 = points[i]
                x2, y2 = points[j]
                cnt = 0
                for k in range(n):
                    x3, y3 = points[k]
                    # 共線判斷：外積為 0（完全用整數，不會有精度問題）
                    if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1):
                        cnt += 1
                best = max(best, cnt)

        return best'''

S["p149_float"] = '''class Solution:
    # 【有精度風險，不建議】：用浮點斜率當 key
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        best = 1
        for i in range(n):
            slopes = {}
            for j in range(n):
                if i == j:
                    continue
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                k = float('inf') if dx == 0 else dy / dx   # 垂直線特判
                slopes[k] = slopes.get(k, 0) + 1
                best = max(best, slopes[k] + 1)

        return best'''


def _p149_ref(points):
    """獨立參考解：枚舉所有點對定義的直線，用整數外積數共線點。"""
    n = len(points)
    if n <= 2:
        return n
    best = 2
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]; x2, y2 = points[j]
            c = sum(1 for (x3, y3) in points
                    if (x2 - x1) * (y3 - y1) == (y2 - y1) * (x3 - x1))
            best = max(best, c)
    return best


_p149 = [S.load(k) for k in ("p149_slope", "p149_cross", "p149_float")]

for pts, want in [
    ([[1, 1], [2, 2], [3, 3]], 3),
    ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
    ([[0, 0]], 1),
    ([[0, 0], [1, 1]], 2),
    ([[0, 0], [0, 1], [0, 2]], 3),
    ([[0, 0], [1, 1], [-1, -1]], 3),     # 相反方向：沒正規化就會答 2
]:
    assert _p149_ref(pts) == want, ("P149 ref", pts, _p149_ref(pts))
    for sol in _p149:
        assert sol.maxPoints([p[:] for p in pts]) == want, ("P149", pts, want, sol)

_GRID = [[x, y] for x in range(-4, 5) for y in range(-4, 5)]
for _ in range(1500):
    n = random.randrange(1, 9)
    # 題目保證「點互不相同」，所以從格點裡取樣不重複的
    pts = [p[:] for p in random.sample(_GRID, n)]
    want = _p149_ref(pts)
    for sol in _p149:
        got = sol.maxPoints([p[:] for p in pts])
        assert got == want, ("P149 random", pts, want, got, sol)
# 大座標：浮點版在這裡會出問題，前兩個解法不會
_big = [[0, 0], [10 ** 8, 10 ** 8 + 1], [2 * 10 ** 8, 2 * 10 ** 8 + 2]]
assert _p149_ref(_big) == 3
for sol in _p149[:2]:
    assert sol.maxPoints([p[:] for p in _big]) == 3, ("P149 big coords", sol)
print("P149 solutions OK")

_P149_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">★ 兩個點決定一條線。固定一個點，看其他點相對它的「方向」—— 方向相同的就共線。</text>
            <g stroke="var(--border)" stroke-width="1">
              <line x1="60" y1="240" x2="330" y2="240"/><line x1="60" y1="60" x2="60" y2="240"/>
            </g>
            <g font-size="12" text-anchor="middle">
              <circle cx="100" cy="200" r="6" fill="var(--gold)"/><text x="100" y="224" fill="var(--gold)">(1,1)</text>
              <circle cx="180" cy="160" r="5" fill="var(--accent)"/><text x="180" y="146" fill="var(--accent)">(3,2)</text>
              <circle cx="260" cy="120" r="5" fill="var(--accent)"/><text x="260" y="106" fill="var(--accent)">(5,3)</text>
              <circle cx="220" cy="200" r="5" fill="var(--text-muted)"/><text x="228" y="224" fill="var(--text-muted)">(4,1)</text>
              <circle cx="140" cy="120" r="5" fill="var(--text-muted)"/><text x="140" y="106" fill="var(--text-muted)">(2,3)</text>
              <circle cx="100" cy="80" r="5" fill="var(--text-muted)"/><text x="100" y="68" fill="var(--text-muted)">(1,4)</text>
            </g>
            <line x1="90" y1="205" x2="290" y2="105" stroke="var(--gold)" stroke-width="2" stroke-dasharray="5 3"/>
            <text x="20" y="272" fill="var(--gold)" font-size="12">固定 (1,1)：(3,2) 的方向是 (2,1)，(5,3) 的方向是 (4,2) → 約分後都是 (2,1) ✔ 共線</text>
            <line x1="360" y1="40" x2="360" y2="260" stroke="var(--border)"/>
            <text x="380" y="62" fill="#ff8a65" font-size="13" text-anchor="start">為什麼不能用浮點斜率？</text>
            <text x="380" y="92" fill="var(--text-muted)" font-size="12" text-anchor="start">dy / dx 是浮點除法，會有誤差。</text>
            <text x="380" y="118" fill="var(--text-muted)" font-size="12" text-anchor="start">座標到 10⁴ 時，兩條【不同】的線</text>
            <text x="380" y="142" fill="var(--text-muted)" font-size="12" text-anchor="start">可能算出【完全相同】的浮點斜率。</text>
            <text x="380" y="174" fill="var(--gold)" font-size="12" text-anchor="start">而且垂直線（dx = 0）要特判 inf。</text>
            <text x="380" y="206" fill="var(--accent)" font-size="12" text-anchor="start">改用【最簡分數 (dx, dy)】當 key：</text>
            <text x="380" y="230" fill="var(--accent)" font-size="12" text-anchor="start">全程整數，零誤差，也不用特判。</text>
            <line x1="20" y1="292" x2="620" y2="292" stroke="var(--border)"/>
            <text x="20" y="320" fill="#ff8a65" font-size="13">★ 兩個約分的細節</text>
            <text x="40" y="348" fill="var(--text-muted)" font-size="12">① gcd(0, k) 在 Python 裡等於 abs(k) —— 所以垂直線 (0, 5) 會被約成 (0, 1) ✔</text>
            <text x="40" y="374" fill="var(--text-muted)" font-size="12">　 水平線 (7, 0) 會被約成 (1, 0) ✔　兩種特例都自動處理好了。</text>
            <text x="40" y="404" fill="var(--gold)" font-size="12">② 方向要正規化：(2,1) 和 (−2,−1) 是同一條線，必須算成同一個 key。</text>
            <text x="60" y="430" fill="var(--text-muted)" font-size="12">規則：讓 dx &gt; 0；dx == 0 時讓 dy &gt; 0。沒做這步會把一條線拆成兩半。</text>'''

emit({
 "num": 149, "slug": "max-points-on-a-line",
 "en": [
   "Given an array of <code>points</code> where <code>points[i] = [xi, yi]</code> represents a "
   "point on the <strong>X-Y</strong> plane, return <em>the maximum number of points that lie "
   "on the same straight line</em>.",
 ],
 "zh": [
   "給你一組平面上的點 <code>points</code>，其中 <code>points[i] = [xi, yi]</code>。",
   "回傳<strong>同一條直線上最多能有幾個點</strong>。",
 ],
 "pre": [
   ("note", "★ 這題唯一的難點：不要用浮點斜率", [
     ("c", """最直覺的做法：固定一個點，算出其他點對它的斜率 dy/dx，
用雜湊表數「哪個斜率出現最多次」。

【但浮點數會出事】：

    (a) 精度誤差
        兩條【不同】的直線，算出來的浮點斜率可能相同。

        例如 (0,0)-(10^8, 10^8+1) 和 (0,0)-(2·10^8, 2·10^8+2)：
            斜率分別是 1.00000001 和 1.00000001
            —— double 的有效位數約 15~16 位，
               這兩個數在浮點下【可能相等也可能不等】，
               取決於實作。

        本題座標只到 10^4，所以【實際上不會出錯】——
        但這是運氣，不是設計。

    (b) 垂直線
        dx = 0 -> 除以零 -> 要特判成 inf

    (c) 0.0 和 -0.0
        在 Python 裡 0.0 == -0.0 是 True，
        但在某些語言/雜湊實作裡它們是不同的 key ✘

【正確做法：用「最簡分數」(dx, dy) 當 key】

    全程整數，零誤差 ✔
    垂直線自然變成 (0, 1)，不用特判 ✔

【這是「用精確的表示法取代浮點」的經典例子】——

    同樣的原則在：
        分數運算 -> 用 Fraction 或 (分子, 分母)
        金額計算 -> 用整數的「分」而不是浮點的「元」
        角度比較 -> 用向量外積而不是 atan2

    【只要能用整數表達，就不要用浮點。】"""),
   ]),
 ],
 "examples": """範例 1
  輸入：points = [[1,1],[2,2],[3,3]]
  輸出：3
  說明：三個點都在 y = x 這條線上。

範例 2
  輸入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
  輸出：4
  說明：(1,4), (2,3), (3,2), (4,1) 四個點在 x + y = 5 這條線上。""",
 "constraints": [
   "1 ≤ <code>points.length</code> ≤ 300",
   "<code>points[i].length == 2</code>",
   "−10⁴ ≤ <code>xi</code>, <code>yi</code> ≤ 10⁴",
   "<code>points</code> 裡的點<strong>互不相同</strong>",
 ],
 "mid": [
   ("note", "n ≤ 300 —— O(n²) 甚至 O(n³) 都可以", [
     "<strong>O(n²) = 9 萬</strong>（解法一）。",
     "<strong>O(n³) = 2700 萬</strong>（解法二）—— 也在時限內，只是慢一點。",
     "<strong>所以這題考的不是「怎麼變快」，而是「怎麼把共線判斷寫對」。</strong>",
   ]),
 ],
 "idea": [
   ("fig", _P149_FIG, "0 0 640 450"),
   ("c", """【核心觀察】

    一條直線至少需要兩個點決定。

    所以：【固定一個點 i，看其他所有點相對它的「方向」】。

    方向相同的那些點，就和 i 在同一條直線上 ✔

    對每個 i 都做一次，取最大值。

【怎麼表示「方向」？】

    (dx, dy) = (xj - xi, yj - yi)

    但 (2, 1) 和 (4, 2) 是同一個方向 ——
    要【約分】成最簡分數：

        g = gcd(dx, dy)
        dx, dy = dx // g, dy // g

    【Python 的 gcd 很貼心】：
        gcd(0, 5) = 5    -> 垂直線 (0, 5) 約成 (0, 1) ✔
        gcd(7, 0) = 7    -> 水平線 (7, 0) 約成 (1, 0) ✔

        兩個特例都自動處理好了。

        （gcd(0, 0) = 0 會除以零，但題目保證點互不相同，
          所以 dx 和 dy 不會同時是 0。）

【★ 方向要正規化】

    (2, 1) 和 (-2, -1) 是【同一條線】的兩個方向，
    但約分後是不同的 tuple ✘

    所以要規定一個「標準方向」：

        if dx < 0 or (dx == 0 and dy < 0):
            dx, dy = -dx, -dy

    「讓 dx > 0；dx == 0 時讓 dy > 0」

    這樣一條線只會有一個 key ✔

    【不做這一步的話，一條線上的點會被拆成兩組
      -> 答案偏小。】

    （不過本文的解法一只看 j > i，
      所以其實不會同時遇到兩個相反方向...
      但加上正規化更安全，而且改成 j 跑全部也不會錯。）

【複雜度】：O(n²) 時間、O(n) 空間。"""),
 ],
 "approaches": [
   ap("解法一", "固定一點 + 最簡分數當 key（標準答案）", [
     ("c", S["p149_slope"]),
     "<strong>O(n²) 時間、O(n) 空間。全程整數，沒有精度問題。</strong>",
     ("h", "為什麼內層是 <code>range(i+1, n)</code> 而不是 <code>range(n)</code>？"),
     ("c", """因為「i 和 j 共線」這件事是對稱的 ——
    固定 i=0 時已經考慮過所有經過 points[0] 的線。

    等到 i=1 時，「經過 points[0] 和 points[1] 的線」
    已經在 i=0 那一輪算過了，不用重算。

    所以只看 j > i 就夠了，省一半時間 ✔

【但要注意 best 的初始值】

    n == 1 時，迴圈裡的內層不跑，best 保持 1 ✔
    （所以一開始要設 best = 1 而不是 0。）

    題目開頭的 if n <= 2: return n 也處理了這個。

【+1 是什麼？】

    slopes[(dx,dy)] 數的是「除了 points[i] 之外，
    有幾個點在這個方向上」。

    加上 points[i] 自己 -> +1 ✔""",),
     ("h", "「點互不相同」這個條件很重要"),
     ("c", """如果允許重複的點：

    (0,0) 和 (0,0) 的 dx, dy 都是 0
    -> gcd(0, 0) = 0 -> 除以零 ✘

    而且「重複的點」在任何線上都算 ——
    要另外數「和 points[i] 完全相同的點有幾個」，
    最後加上去。

    LeetCode 這題【保證互不相同】，
    所以不用處理。

    但如果面試官問「如果有重複的點呢」，
    要知道：
        1. 先數重複的點 same
        2. 其餘的照常算斜率
        3. 答案 = max(斜率計數) + same

【讀題時要注意「互不相同」這種條件】——
    它常常是「某段程式碼可以省略」的理由。""",),
   ], "O(n²)", "O(n)", "每一對點算一次", "斜率雜湊表", optimal=True),

   ap("解法二", "枚舉兩點定線 + 整數外積（最直白）", [
     ("c", S["p149_cross"]),
     ("h", "★ 外積判共線：完全用整數"),
     ("c", """三個點 A, B, C 共線
  ⟺ 向量 AB 和 AC 平行
  ⟺ 它們的【外積】為 0

    AB = (x2-x1, y2-y1)
    AC = (x3-x1, y3-y1)

    外積（2D 的「叉積」）= (x2-x1)(y3-y1) - (y2-y1)(x3-x1)

    等於 0 就共線 ✔

【為什麼這樣最安全？】

    ✔ 全程整數乘法和減法 —— 零誤差
    ✔ 不用約分、不用處理垂直線
    ✔ 不用正規化方向

    這是計算幾何裡【判斷共線／方向】的標準工具。

【外積的幾何意義】：

    2D 外積 = 兩向量張成的平行四邊形的【有號面積】

        > 0 -> C 在 AB 的左邊（逆時針）
        = 0 -> 三點共線
        < 0 -> C 在 AB 的右邊（順時針）

    這個「有號」的性質在凸包（第 587 題）、
    線段相交判斷裡都是核心工具。

【複雜度 O(n³)】

    n = 300 -> 2700 萬次 —— 在 Python 下大約幾秒，
    可能會逾時（LeetCode 的 Python 時限通常比較寬鬆）。

    但它【一定正確】，而且是驗證解法一的最好工具 ——
    本文的測試就是用它當參考實作。""",),
     "<strong>面試時可以先講這個（思路最清楚），再優化到解法一。</strong>",
   ], "O(n³)", "O(1)", "每三個點檢查一次", "不用額外空間"),

   ap("解法三", "浮點斜率（示範它的風險）", [
     ("c", S["p149_float"]),
     ("c", """【本題座標只到 10^4，所以這個版本實際上會過。】

    但它有三個結構性的問題：

    1. 【精度】
       dy/dx 是浮點除法。
       座標大一點（例如 10^8）時，
       兩條不同的線可能算出相同的 double。

       本文的測試裡有一組大座標的案例
       （(0,0), (10^8, 10^8+1), (2·10^8, 2·10^8+2)），
       解法一和二都對，浮點版就不保證。

    2. 【垂直線】
       dx = 0 要特判成 inf —— 多一個分支。

    3. 【-0.0】
       在 Python 裡 hash(0.0) == hash(-0.0)，所以沒事。
       但在 C++ 的 unordered_map 裡，
       0.0 和 -0.0 的 bit pattern 不同 ->
       如果用位元當 hash 就會變成兩個 key ✘

【教訓】：

    「這題的測資剛好過得了」
    和「這個做法是對的」是兩件事。

    面試時寫浮點版，面試官幾乎一定會問
    「浮點誤差怎麼辦」——
    能主動說出「我改用最簡分數」才是滿分答案。""",),
   ], "O(n²)", "O(n)", "同解法一", "斜率雜湊表"),
 ],
 "compare": (["解法", "時間", "空間", "有精度問題嗎", "備註"],
   [["一、最簡分數當 key", "O(n²)", "O(n)", "✘", "標準答案"],
    ["二、整數外積", "O(n³)", "O(1)", "✘", "最直白，驗證用"],
    ["三、浮點斜率", "O(n²)", "O(n)", "✔", "本題能過，但有風險"]]),
 "edges": [
   "<strong>只有一個點</strong> → <code>1</code>。",
   "<strong>只有兩個點</strong> → <code>2</code>（任兩點必共線）。",
   "<strong>垂直線</strong> <code>[[0,0],[0,1],[0,2]]</code> → <code>3</code>。"
   "<strong>浮點版要特判 <code>dx = 0</code>；分數版自動處理。</strong>",
   "<strong>水平線</strong> → 同上，<code>(7,0)</code> 約成 <code>(1,0)</code>。",
   "<strong>沒有正規化方向</strong> → 一條線被拆成兩組，答案偏小。",
   "<strong>忘了 <code>+1</code>（<code>points[i]</code> 自己）</strong> → 答案少 1。",
   "<strong><code>best</code> 初始成 0</strong> → 單一點時回傳 0 而不是 1。",
   "<strong>用浮點斜率 + 大座標</strong> → 可能把不同的線算成同一條。",
   "<strong>300 個點</strong> → O(n²) 是 9 萬，O(n³) 是 2700 萬。",
 ],
 "follow": [
   ("h", "追問一：如果點可以重複呢？"),
   ("c", """題目保證互不相同，但如果可以：

    for i in range(n):
        same = 0            # 和 points[i] 完全相同的點
        slopes = defaultdict(int)
        for j in range(n):
            if i == j: continue
            dx = xj - xi; dy = yj - yi
            if dx == 0 and dy == 0:
                same += 1           # ★ 重複的點單獨數
                continue
            ...約分、計數...
        best = max(best, max(slopes.values(), default=0) + same + 1)

【為什麼重複的點要單獨處理？】

    (a) gcd(0, 0) = 0 -> 除以零會 crash
    (b) 重複的點在【任何】經過 points[i] 的線上都算

【而且全部的點都重複時】：
    答案是 n（它們都在同一個位置，任何線都能穿過）。

    這種退化情況要特別驗證。""",),
   ("h", "追問二：能不能比 O(n²) 更快？"),
   ("c", """【一般情況下不行。】

    這個問題和「3SUM 是否有解」屬於同一個複雜度類別
    （3SUM-hard）。

    「找出是否有三點共線」（degenerate triangle problem）
    被證明是 3SUM-hard 的 ——
    而 3SUM 目前最好的演算法是 O(n²/polylog n)，
    沒有已知的 O(n^(2-ε)) 演算法。

【所以 O(n²) 基本上就是這題的極限。】

    （有一個「對偶變換」的 O(n²) 演算法，
      把點轉成線、線轉成點，然後找「線段排列」中的交點 ——
      同樣是 O(n²)，但概念很漂亮。）

【面試時的回答】：
    「這是 3SUM-hard 的問題，O(n²) 應該是最優的。」

    能說出這句話會很加分 ——
    它顯示你知道「什麼時候該停止優化」。""",),
   ("h", "追問三：外積還有哪些用途？"),
   ("ul", [
     "<strong>判斷點在線的哪一邊</strong>（外積的符號）",
     "<strong>凸包演算法</strong>（Graham scan、Andrew monotone chain）"
     "—— 用外積判斷「是不是往左轉」",
     "<strong>線段相交判斷</strong> —— 四次外積",
     "<strong>多邊形面積</strong>（鞋帶公式）—— 外積的總和除以 2",
     "<strong>判斷多邊形的方向</strong>（順時針 / 逆時針）",
     "<strong>點在多邊形內</strong>（凸多邊形的話，看是否都在同一邊）",
   ]),
   "<strong>2D 外積是計算幾何的「瑞士刀」</strong> —— "
   "<strong>它是唯一一個「用整數就能表達方向關係」的工具，所以完全沒有精度問題。</strong>",
   ("h", "追問四：為什麼要正規化方向？舉個會出錯的例子。"),
   ("c", """考慮三個點：A(0,0)、B(1,1)、C(-1,-1)

    如果固定 i = A，內層跑【全部】的 j：

        B 相對 A 的方向：(1, 1)   約分後 (1, 1)
        C 相對 A 的方向：(-1, -1) 約分後 (-1, -1)

        兩個不同的 key -> 各算一次
        -> 最大計數是 1 -> 答案 = 1 + 1 = 2 ✘

        但 A, B, C 明明共線 -> 答案應該是 3

    加上正規化之後：
        (-1, -1) -> 翻轉成 (1, 1) ✔
        兩個點都記在 (1,1) 這個 key 下 -> 計數 2
        -> 答案 = 2 + 1 = 3 ✔

【本文的解法一因為只跑 j > i，
  不會在同一輪遇到相反方向的兩個點嗎？】

    會的！上面的例子裡，如果 points 的順序是 [A, B, C]，
    i = 0（A）時 j 會跑到 B 和 C ——
    正好是相反的兩個方向。

    【所以正規化是必要的，不是可有可無的保險。】""",),
 ],
 "related": [
   "<strong>第 587 題 Erect the Fence</strong> —— 凸包，同樣用外積",
   "<strong>第 15 題 3Sum</strong> —— 和本題同一個複雜度類別",
   "<strong>第 963 題 Minimum Area Rectangle II</strong> —— 另一個計算幾何題",
   "<strong>第 1232 題 Check If It Is a Straight Line</strong> —— 本題的簡化版",
 ],
 "check": [
   "為什麼不能用浮點斜率 <code>dy/dx</code> 當雜湊表的 key？列出三個問題。",
   "<code>gcd(0, 5)</code> 等於多少？這讓垂直線的處理變得如何？",
   "為什麼要「正規化方向」？請舉出一個不做會出錯的例子。",
   "三點共線的整數判斷式是什麼？它的幾何意義是什麼？",
 ],
})
print("P149 written")

# ==================== 150. Evaluate Reverse Polish Notation ====================
S["p150"] = '''class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in ("+", "-", "*", "/"):
                b = stack.pop()             # ★ 先彈出的是【右】運算元
                a = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))  # ★ 往零截斷，不是 Python 的 //
            else:
                stack.append(int(t))

        return stack[0]'''

S["p150_ops"] = '''import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b),   # 往零截斷
        }

        stack = []
        for t in tokens:
            if t in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[t](a, b))
            else:
                stack.append(int(t))

        return stack[0]'''

S["p150_wrong"] = '''class Solution:
    # 【除法是錯的，不要抄】
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ("+", "-", "*", "/"):
                b, a = stack.pop(), stack.pop()
                if t == "+":   stack.append(a + b)
                elif t == "-": stack.append(a - b)
                elif t == "*": stack.append(a * b)
                else:          stack.append(a // b)   # ← Python 的 // 是向下取整
            else:
                stack.append(int(t))
        return stack[0]'''


def _p150_ref(tokens):
    """獨立參考解：遞迴地從尾端往前解析。"""
    idx = [len(tokens) - 1]
    def go():
        t = tokens[idx[0]]
        idx[0] -= 1
        if t not in ("+", "-", "*", "/"):
            return int(t)
        b = go()        # 後序：倒著讀時先拿到的是右運算元
        a = go()
        if t == "+":
            return a + b
        if t == "-":
            return a - b
        if t == "*":
            return a * b
        return int(a / b)
    return go()


_p150 = [S.load(k) for k in ("p150", "p150_ops")]
_p150_bad = S.load("p150_wrong")

for tk, want in [
    (["2", "1", "+", "3", "*"], 9),
    (["4", "13", "5", "/", "+"], 6),
    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    (["3"], 3),
    (["-7", "2", "/"], -3),          # 往零截斷：-3 而不是 -4
    (["7", "-2", "/"], -3),
    (["-7", "-2", "/"], 3),
]:
    assert _p150_ref(tk) == want, ("P150 ref", tk, _p150_ref(tk))
    for sol in _p150:
        assert sol.evalRPN(list(tk)) == want, ("P150", tk, want, sol)

# 錯誤寫法確實在負數除法上答錯
assert _p150_bad.evalRPN(["-7", "2", "/"]) == -4 and _p150_ref(["-7", "2", "/"]) == -3


def _rand_rpn(depth):
    """隨機產生一個合法的逆波蘭式（避免除以零）。"""
    if depth == 0 or random.random() < 0.35:
        return [str(random.randint(-9, 9))], None
    left, _ = _rand_rpn(depth - 1)
    right, _ = _rand_rpn(depth - 1)
    op = random.choice(["+", "-", "*", "/"])
    if op == "/":
        # 確保右運算元不是 0
        try:
            if _p150_ref(right) == 0:
                op = "+"
        except ZeroDivisionError:
            op = "+"
    return left + right + [op], None


for _ in range(4000):
    tk, _ = _rand_rpn(random.randrange(0, 5))
    try:
        want = _p150_ref(tk)
    except ZeroDivisionError:
        continue
    if not (-2 ** 31 <= want < 2 ** 31):
        continue
    for sol in _p150:
        assert sol.evalRPN(list(tk)) == want, ("P150 random", tk, want, sol)
print("P150 solutions OK")

_P150_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">逆波蘭式（後序）把運算子放在運算元後面 —— 完全不需要括號，也不需要優先順序規則。</text>
            <text x="20" y="52" fill="var(--gold)" font-size="13">tokens = [&quot;2&quot;, &quot;1&quot;, &quot;+&quot;, &quot;3&quot;, &quot;*&quot;]　　（等同於中綴的 (2 + 1) × 3）</text>
            <g font-size="12" text-anchor="middle">
              <text x="70" y="90" fill="var(--text-muted)" text-anchor="start">讀到</text>
              <text x="250" y="90" fill="var(--text-muted)" text-anchor="start">動作</text>
              <text x="450" y="90" fill="var(--text-muted)" text-anchor="start">堆疊</text>
            </g>
            <g font-size="12">
              <text x="70" y="120" fill="var(--accent)">&quot;2&quot;</text><text x="250" y="120" fill="var(--text-muted)">是數字 → push</text><text x="450" y="120" fill="var(--gold)">[2]</text>
              <text x="70" y="148" fill="var(--accent)">&quot;1&quot;</text><text x="250" y="148" fill="var(--text-muted)">是數字 → push</text><text x="450" y="148" fill="var(--gold)">[2, 1]</text>
              <text x="70" y="176" fill="#ff8a65">&quot;+&quot;</text><text x="250" y="176" fill="var(--text-muted)">pop 1（右）、pop 2（左）→ push 2+1</text><text x="450" y="176" fill="var(--gold)">[3]</text>
              <text x="70" y="204" fill="var(--accent)">&quot;3&quot;</text><text x="250" y="204" fill="var(--text-muted)">是數字 → push</text><text x="450" y="204" fill="var(--gold)">[3, 3]</text>
              <text x="70" y="232" fill="#ff8a65">&quot;*&quot;</text><text x="250" y="232" fill="var(--text-muted)">pop 3（右）、pop 3（左）→ push 3×3</text><text x="450" y="232" fill="var(--gold)">[9]</text>
            </g>
            <text x="20" y="266" fill="var(--gold)" font-size="12">堆疊只剩一個元素 9 —— 那就是答案 ✔</text>
            <line x1="20" y1="288" x2="620" y2="288" stroke="var(--border)"/>
            <text x="20" y="316" fill="#ff8a65" font-size="13">★ 兩個必錯的細節</text>
            <text x="40" y="346" fill="var(--accent)" font-size="12">① 先 pop 的是【右】運算元</text>
            <text x="60" y="372" fill="var(--text-muted)" font-size="12">　 b = pop(); a = pop(); 算 a − b　　寫反的話減法和除法全錯。</text>
            <text x="40" y="404" fill="var(--accent)" font-size="12">② 除法要「往零截斷」，不是 Python 的 //</text>
            <text x="60" y="430" fill="#ff8a65" font-size="12">　 −7 // 2 = −4　（向下取整）　✘</text>
            <text x="60" y="454" fill="var(--gold)" font-size="12">　 int(−7 / 2) = −3　（往零截斷）　✔　題目要的是這個</text>'''

emit({
 "num": 150, "slug": "evaluate-reverse-polish-notation",
 "en": [
   "You are given an array of strings <code>tokens</code> that represents an arithmetic "
   "expression in a <a href=\"https://en.wikipedia.org/wiki/Reverse_Polish_notation\" "
   "target=\"_blank\" rel=\"noopener\">Reverse Polish Notation</a>.",
   "Evaluate the expression. Return <em>an integer that represents the value of the "
   "expression</em>.",
   "<strong>Note</strong> that:",
   ("raw", "<ul><li>The valid operators are <code>'+'</code>, <code>'-'</code>, "
           "<code>'*'</code>, and <code>'/'</code>.</li>"
           "<li>Each operand may be an integer or another expression.</li>"
           "<li>The division between two integers always <strong>truncates toward "
           "zero</strong>.</li>"
           "<li>There will not be any division by zero.</li>"
           "<li>The input represents a valid arithmetic expression in a reverse polish "
           "notation.</li>"
           "<li>The answer and all the intermediate calculations can be represented in a "
           "<strong>32-bit</strong> integer.</li></ul>"),
 ],
 "zh": [
   "給你一個字串陣列 <code>tokens</code>，代表一個<strong>逆波蘭表示法</strong>"
   "（後綴表示法）的算式。求它的值。",
   ("ul", [
     "合法的運算子是 <code>+</code>、<code>-</code>、<code>*</code>、<code>/</code>。",
     "<strong>整數除法一律「往零截斷」</strong>（truncate toward zero）。",
     "<strong>不會有除以零的情況。</strong>",
     "輸入保證是合法的逆波蘭式。",
     "答案和所有中間結果都能裝進 32 位元整數。",
   ]),
 ],
 "pre": [
   ("note", "什麼是「逆波蘭表示法」？", [
     ("c", """【中綴（infix）】：我們平常寫的     (2 + 1) * 3
【後綴（postfix / 逆波蘭）】：        2 1 + 3 *
【前綴（prefix / 波蘭）】：           * + 2 1 3

【逆波蘭的兩個好處】：

    ✔ 【完全不需要括號】
        中綴的 (2+1)*3 和 2+(1*3) 要靠括號區分，
        後綴是 "2 1 + 3 *" 和 "2 1 3 * +" —— 天生不同 ✔

    ✔ 【完全不需要運算子優先順序】
        因為順序已經編碼在序列裡了。

【它和「後序走訪」是同一件事】：

    把算式看成一棵【運算式樹】：

            *
           / \\
          +   3
         / \\
        2   1

    後序走訪（左右根）= 2, 1, +, 3, * ✔

    所以「求值逆波蘭式」= 「後序走訪一棵運算式樹並求值」。

    這就是為什麼它用【堆疊】就能算 ——
    後序走訪的迭代版本質上就是堆疊操作（第 145 題）。

【實務上的用途】：
    HP 的工程計算機、PostScript、Forth 語言、
    以及大部分虛擬機器的位元組碼（JVM、CPython）
    都是基於堆疊的後綴運算。"""),
   ]),
 ],
 "examples": """範例 1
  輸入：tokens = ["2","1","+","3","*"]
  輸出：9
  說明：((2 + 1) * 3) = 9

範例 2
  輸入：tokens = ["4","13","5","/","+"]
  輸出：6
  說明：(4 + (13 / 5)) = 4 + 2 = 6
        【13 / 5 = 2.6，往零截斷是 2】

範例 3
  輸入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
  輸出：22
  說明：((10 * (6 / ((9 + 3) * -11))) + 17) + 5
       = ((10 * (6 / -132)) + 17) + 5
       = ((10 * 0) + 17) + 5          【6 / -132 = -0.045… 往零截斷是 0】
       = 22""",
 "constraints": [
   "1 ≤ <code>tokens.length</code> ≤ 10⁴",
   "<code>tokens[i]</code> 是 <code>\"+\"</code>、<code>\"-\"</code>、"
   "<code>\"*\"</code>、<code>\"/\"</code>，或一個範圍在 <code>[-200, 200]</code> 的整數",
 ],
 "idea": [
   ("fig", _P150_FIG, "0 0 640 478"),
   ("c", """【堆疊求值】

    for t in tokens:
        if t 是運算子:
            b = stack.pop()     ★ 先彈出的是【右】運算元
            a = stack.pop()
            stack.append(a op b)
        else:
            stack.append(int(t))

    return stack[0]

【★ 為什麼先 pop 的是右運算元？】

    push 的順序是「先左後右」（因為後綴式裡左運算元在前）。

    堆疊是後進先出 -> 先 pop 出來的是【後 push 的】= 右運算元 ✔

    寫反的話：
        "5 3 -" 應該是 5 - 3 = 2
        寫反變成 3 - 5 = -2 ✘

    【加法和乘法看不出來（可交換），
      減法和除法會直接錯。】

【★ 除法要「往零截斷」】

    Python 的 // 是【向下取整】（floor division）：
        -7 // 2 = -4        （往負無窮）

    題目要的是【往零截斷】（truncate toward zero）：
        -7 -> -3.5 -> -3    （往 0 的方向）

    正確寫法：
        int(a / b)          先算浮點除法，int() 會往零截斷 ✔

    或者：
        import math
        math.trunc(a / b)

    或者純整數（避免浮點）：
        q = abs(a) // abs(b)
        q = -q if (a < 0) != (b < 0) else q

    【本題數值範圍在 32 位元內，
      float 有 53 位精度，所以 int(a/b) 是安全的。】

    但如果數字可能超過 2^53，就必須用純整數的版本。

【複雜度】：O(n) 時間、O(n) 空間（堆疊）。"""),
 ],
 "approaches": [
   ap("解法一", "堆疊求值（標準答案）", [
     ("c", S["p150"]),
     "<strong>十五行，O(n) 時間、O(n) 空間。</strong>",
     ("h", "★ Python 的整數除法有三種，別搞混"),
     ("c", """a // b          向下取整（floor）      -7 // 2 = -4
int(a / b)      往零截斷（truncate）    int(-7/2) = -3
divmod(a, b)    回傳 (商, 餘數)，商是 floor

【大部分語言的 / 對整數是「往零截斷」】：
    C、C++、Java、Go、Rust、JavaScript 的 Math.trunc

【Python 特立獨行，用 floor】：
    因為 Python 想保證 a == (a // b) * b + (a % b)
    而且 a % b 的符號跟著 b（方便做「環狀索引」）。

        -7 % 2 == 1      （Python）
        -7 % 2 == -1     （C）

    Python 的選擇在「取模運算」上更好用
    （例如 (i - 1) % n 永遠是合法索引），
    但在「模擬其他語言的整數除法」時就要小心。

【這題明確要求往零截斷】-> 一定要用 int(a / b)。

    這是本題第一名的 bug，而且只有在
    「被除數或除數是負數」時才會出現 ——
    很容易漏測。""",),
     ("h", "為什麼最後回傳 <code>stack[0]</code>？"),
     ("c", """輸入保證是合法的逆波蘭式，
所以處理完之後堆疊裡【剛好剩一個元素】——
那就是整個算式的值 ✔

    也可以寫 stack.pop() 或 stack[-1]，
    三者在「合法輸入」下完全等價。

【如果輸入不合法呢？】

    "1 2" （少一個運算子）-> 堆疊剩 [1, 2]
    "1 +" （少一個運算元）-> pop 空堆疊 -> IndexError

    題目保證合法，所以不用檢查。

    但如果要寫一個真實的計算機，
    就必須驗證「堆疊最後剛好剩一個」——
    那是最簡單的合法性檢查。""",),
   ], "O(n)", "O(n)", "每個 token 處理一次", "堆疊", optimal=True),

   ap("解法二", "用字典把運算子映射到函式", [
     ("c", S["p150_ops"]),
     ("c", """ops = {"+": operator.add, "-": operator.sub,
       "*": operator.mul, "/": lambda a, b: int(a / b)}

    if t in ops:
        b = stack.pop(); a = stack.pop()
        stack.append(ops[t](a, b))

【好處】：
    ✔ 沒有一長串的 if/elif
    ✔ 要加新運算子（例如 "%" 或 "^"）只要在字典裡加一筆
    ✔ 「判斷是不是運算子」和「取得對應的函式」用同一個字典

【operator 模組】：
    operator.add / sub / mul / truediv / floordiv / mod / pow
    比 lambda a, b: a + b 快（C 實作），也更清楚。

【這個「用字典派發（dispatch table）」的模式很通用】：

    - 直譯器 / 虛擬機的指令分派
    - 狀態機的轉移表
    - 命令模式（Command pattern）

    它把「控制流程」變成「資料」——
    程式碼更短，而且擴充時不用改邏輯，只要改資料。

【注意除法不能直接用 operator.truediv】
    （那會回傳浮點數）
    也不能用 operator.floordiv（那是向下取整）——
    必須自己包一個 lambda。""",),
   ], "O(n)", "O(n)", "同解法一", "堆疊 + 派發表"),

   ap("解法三", "用 <code>//</code> 的錯誤版本（示範那個 bug）", [
     ("c", S["p150_wrong"]),
     ("c", """只有除法那一行不同：

    stack.append(a // b)        ✘ 向下取整
    stack.append(int(a / b))    ✔ 往零截斷

【什麼時候會出錯？】

    只有在【商是負數而且除不盡】時：

        -7 // 2  = -4    但正確答案是 -3
         7 // -2 = -4    但正確答案是 -3
        -7 // -2 = 3     ✔ 剛好一樣（商是正的）
         6 // 4  = 1     ✔ 剛好一樣（商是正的）

    【所以如果測資裡沒有「負數除法且除不盡」，
      這個 bug 完全不會被發現。】

    這是最危險的一種 bug ——
    它在 90% 的情況下都對。

【怎麼避免這類 bug？】

    看到「除法」就問自己三件事：
        1. 會不會除以零？
        2. 負數怎麼處理（向下 vs 往零）？
        3. 會不會溢位（INT_MIN / -1）？

    這題的題目已經幫你回答了 1 和 3，
    而且【明確指定】了 2 —— 讀題時不能跳過。""",),
     "<strong>本文的測試特別包含 <code>[\"-7\",\"2\",\"/\"]</code> 這一組</strong>，"
     "<strong>而且驗證了錯誤版本確實會答 -4。</strong>",
   ], "O(n)", "O(n)", "同解法一", "堆疊"),
 ],
 "compare": (["解法", "時間", "空間", "行數", "備註"],
   [["一、堆疊 + if/elif", "O(n)", "O(n)", "15", "標準答案"],
    ["二、堆疊 + 派發表", "O(n)", "O(n)", "16", "好擴充"],
    ["三、用 //", "O(n)", "O(n)", "14", "負數除法會錯"]]),
 "edges": [
   "<strong>只有一個數字</strong> <code>[\"3\"]</code> → <code>3</code>。",
   "<strong>負數的 token</strong> <code>[\"-11\"]</code> → "
   "<strong><code>int(\"-11\")</code> 正確處理；但如果用 "
   "<code>t.isdigit()</code> 判斷「是不是數字」就會誤判成運算子。</strong>",
   "<strong><code>[\"-7\",\"2\",\"/\"]</code></strong> → "
   "<strong><code>-3</code>（往零截斷），不是 <code>-4</code>。本題第一名的 bug。</strong>",
   "<strong><code>[\"7\",\"-2\",\"/\"]</code></strong> → <code>-3</code>。",
   "<strong><code>[\"-7\",\"-2\",\"/\"]</code></strong> → <code>3</code>（商是正的，"
   "<code>//</code> 也剛好對）。",
   "<strong>除法的結果是 0</strong>（範例 3 的 <code>6 / -132</code>）→ <code>0</code>。",
   "<strong><code>b</code> 和 <code>a</code> 的 pop 順序寫反</strong> → "
   "<strong>減法和除法全錯，加法和乘法看不出來。</strong>",
   "<strong>10⁴ 個 token</strong> → O(n) 輕鬆。",
 ],
 "follow": [
   ("h", "追問一：為什麼不能用 <code>t.isdigit()</code> 判斷是不是數字？"),
   ("c", """"-11".isdigit() 回傳 False！
（因為有負號，不是純數字字元。）

    所以 "-11" 會被當成運算子 -> 找不到對應的運算 ✘

【三種正確的判斷方式】：

    (a) if t in ("+", "-", "*", "/"):      ✔ 本文用這個
        —— 明確列出運算子

    (b) if t in ops:                        ✔ 解法二
        —— 用派發表當作判斷

    (c) if t.lstrip("-").isdigit():         能動但囉唆

【為什麼 (a)(b) 比較好？】

    因為「運算子只有四個，而數字有無限多種」——
    列舉少的那一邊永遠比較安全。

    這是一個很實用的原則：
    【判斷「屬於哪一類」時，檢查【集合較小】的那一類。】""",),
   ("h", "追問二：如果要處理「中綴表示法」呢？"),
   ("c", """那就是第 224 / 227 題（基本計算器）。

    中綴需要處理【括號】和【運算子優先順序】——
    難得多。

【兩條路】：

    (a) 【調度場演算法】（Shunting-yard，Dijkstra 發明）
        用兩個堆疊（數字 + 運算子），
        把中綴【轉成】後綴，然後用本題的方法求值。

        遇到運算子時，先把堆疊裡「優先順序 >= 它」的
        全部彈出來運算。

    (b) 【遞迴下降解析】
        expr   := term (('+' | '-') term)*
        term   := factor (('*' | '/') factor)*
        factor := number | '(' expr ')'

        每一層處理一個優先順序 ——
        這是編譯器前端的標準做法。

【逆波蘭式之所以簡單，就是因為它已經把
  「優先順序」和「括號」的資訊編碼掉了】——

    那些困難被移到了「產生逆波蘭式」的那一步。

    而堆疊求值只是「後序走訪」而已。""",),
   ("h", "追問三：如果數字可能很大（超過 2⁵³）呢？"),
   "<strong><code>int(a / b)</code> 就不安全了</strong> —— "
   "<strong><code>a / b</code> 是浮點除法，會損失精度。</strong>",
   ("c", """純整數的「往零截斷」除法：

    def trunc_div(a, b):
        q = abs(a) // abs(b)
        return -q if (a < 0) != (b < 0) else q

    或者利用 Python 的 // 和 % 的關係：

        q = a // b
        if q < 0 and q * b != a:      # 商是負數且除不盡
            q += 1
        return q

【本題保證「所有中間結果都在 32 位元內」】，
    所以 int(a/b) 完全安全（float 有 53 位精度）。

    但在寫「通用的計算機」時，
    要用純整數的版本。

    【知道「什麼時候浮點是安全的」比「一律避免浮點」更重要。】""",),
   ("h", "追問四：這題和第 145 題（後序走訪）的關係是什麼？"),
   ("c", """逆波蘭式【就是】運算式樹的後序走訪結果。

    所以：
        「求值逆波蘭式」= 「後序走訪並求值」

    本文的參考實作 _p150_ref 就是用遞迴做的：

        倒著讀 tokens（後序的反序是「根右左」），
        遇到運算子就先解析右邊、再解析左邊。

    而堆疊版是它的迭代形式 ——
    就像第 145 題的堆疊版是遞迴版的迭代形式。

【反過來：從逆波蘭式建出運算式樹】

    用同樣的堆疊，
    但 push 的是【節點】而不是【數值】：

        遇到數字 -> push 葉節點
        遇到運算子 -> pop 兩個當左右孩子，push 新的內部節點

    最後堆疊裡剩下的就是樹根 ✔

    這正是第 105/106 題「從走訪序列建樹」的特例 ——
    只是這裡的「樹」是運算式樹。""",),
 ],
 "related": [
   "<strong>第 145 題 Postorder Traversal</strong> —— 逆波蘭式就是後序走訪",
   "<strong>第 224 題 Basic Calculator</strong> —— 中綴 + 括號",
   "<strong>第 227 題 Basic Calculator II</strong> —— 中綴 + 優先順序",
   "<strong>第 20 題 Valid Parentheses</strong> —— 堆疊的入門",
   "<strong>第 1006 題 Clumsy Factorial</strong> —— 另一個運算順序題",
 ],
 "check": [
   "為什麼先 <code>pop</code> 出來的是<strong>右</strong>運算元？寫反會在哪些運算上出錯？",
   "Python 的 <code>//</code> 和題目要的除法差在哪裡？請舉出一個會出錯的例子。",
   "為什麼不能用 <code>t.isdigit()</code> 判斷「是不是數字」？",
   "逆波蘭式和「後序走訪」是什麼關係？",
 ],
})
print("P150 written")
