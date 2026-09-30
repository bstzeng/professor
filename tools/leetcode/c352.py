# -*- coding: utf-8 -*-
"""第 352、354、355、357、363、365 題。"""
import random
import math
import itertools
from collections import deque, defaultdict
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(352)


# ==================== 352. Data Stream as Disjoint Intervals ====================
S["p352"] = '''class SummaryRanges:
    def __init__(self):
        self.starts = []              # 各區間的起點（排序）
        self.ends = []                # 對應的終點

    def addNum(self, value: int) -> None:
        s, e = self.starts, self.ends
        i = bisect.bisect_right(s, value)          # 起點 <= value 的最後一個區間是 i-1
        if i and e[i - 1] >= value:                # 已經被某個區間涵蓋
            return
        join_left = i > 0 and e[i - 1] == value - 1          # 能接在左邊區間的尾巴
        join_right = i < len(s) and s[i] == value + 1        # 能接在右邊區間的頭
        if join_left and join_right:               # ★ 兩個區間被 value 連起來
            e[i - 1] = e[i]
            del s[i], e[i]
        elif join_left:
            e[i - 1] = value
        elif join_right:
            s[i] = value
        else:                                      # 自成一個新區間
            s.insert(i, value)
            e.insert(i, value)

    def getIntervals(self) -> List[List[int]]:
        return [[a, b] for a, b in zip(self.starts, self.ends)]'''

S["p352_set"] = '''class SummaryRanges:
    def __init__(self):
        self.seen = set()

    def addNum(self, value: int) -> None:
        self.seen.add(value)                       # O(1)

    def getIntervals(self) -> List[List[int]]:
        res = []
        for x in sorted(self.seen):                # 查詢時才排序、合併
            if res and res[-1][1] == x - 1:
                res[-1][1] = x
            else:
                res.append([x, x])
        return res'''

for key in ("p352", "p352_set"):
    cls = S.loadns(key)["SummaryRanges"]
    for _ in range(500):
        sr, seen = cls(), set()
        for _ in range(random.randrange(1, 30)):
            v = random.randrange(0, 20)
            sr.addNum(v)
            seen.add(v)
            want = []
            for x in sorted(seen):
                if want and want[-1][1] == x - 1:
                    want[-1][1] = x
                else:
                    want.append([x, x])
            assert sr.getIntervals() == want, key
print("P352 OK")

emit({
 "num": 352, "slug": "data-stream-as-disjoint-intervals",
 "en": [
   "Given a data stream input of non-negative integers <code>a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub></code>, summarize the numbers seen so far as a list of disjoint intervals.",
   "Implement the <code>SummaryRanges</code> class:",
   ("ul", ["<code>SummaryRanges()</code> Initializes the object with an empty stream.",
           "<code>void addNum(int value)</code> Adds the integer <code>value</code> to the stream.",
           "<code>int[][] getIntervals()</code> Returns a summary of the integers in the stream currently as a list of disjoint intervals <code>[start<sub>i</sub>, end<sub>i</sub>]</code>. The answer should be sorted by <code>start<sub>i</sub></code>."]),
   "<strong>Follow up:</strong> What if there are lots of merges and the number of disjoint intervals is small compared to the size of the data stream?",
 ],
 "zh": [
   "資料流不斷送來非負整數，請隨時把目前看過的數字整理成<strong>不相交的區間</strong>。",
   ("ul", ["<code>addNum(value)</code>：加入一個整數。",
           "<code>getIntervals()</code>：回傳目前所有區間 <code>[start, end]</code>，依起點排序。"]),
   "<strong>進階：</strong>如果合併很頻繁，區間數量遠小於資料流長度，要怎麼設計？",
 ],
 "examples": """範例
  addNum(1)  -> [[1,1]]
  addNum(3)  -> [[1,1],[3,3]]
  addNum(7)  -> [[1,1],[3,3],[7,7]]
  addNum(2)  -> [[1,3],[7,7]]
  addNum(6)  -> [[1,3],[6,7]]""",
 "constraints": [
   "0 ≤ <code>value</code> ≤ 10⁴",
   "<code>addNum</code> 與 <code>getIntervals</code> 最多共呼叫 3 × 10⁴ 次",
   "<code>getIntervals</code> 最多呼叫 10² 次",
 ],
 "idea": [
   ("c", """【方法一：只存數字，查詢時才整理】
    addNum O(1)，getIntervals 排序 O(n log n)。
    題目中 getIntervals 呼叫次數很少，這樣其實很划算。

【方法二：隨時維護排序好的區間】
    加入 value 時，用二分找到它左右兩邊的區間，分四種情況：
        1. 已經被某個區間涵蓋 -> 不動
        2. 剛好把左右兩個區間連起來（左尾 = value-1、右頭 = value+1）-> 合併成一個
        3. 只能接在左邊區間的尾巴 -> 左區間 end = value
        4. 只能接在右邊區間的頭   -> 右區間 start = value
        5. 都不能 -> 插入新區間 [value, value]

【進階問題】
    區間數 k 很少時，方法二的空間只和 k 有關（不是 n）。
    用平衡樹（Java TreeMap、C++ map）存區間，每次 addNum O(log k)。
    Python 用 list + bisect，插入刪除是 O(k)，但 k 小時很快。"""),
   ("c", """  區間：[1,1] [3,3]         加入 2
  左邊區間 [1,1] 尾巴 = 1 = 2-1 ✔
  右邊區間 [3,3] 開頭 = 3 = 2+1 ✔
  -> 合併成 [1,3]"""),
 ],
 "approaches": [
   ap("解法一", "集合 + 查詢時排序", [
     ("c", S["p352_set"]),
   ], "add O(1)，查詢 O(n log n)", "O(n)", "", ""),

   ap("解法二", "維護排序區間 + 二分", [
     ("c", S["p352"]),
   ], "add O(k)，查詢 O(k)", "O(k)", "k = 區間數；用平衡樹 add 可到 O(log k)", "", optimal=True),
 ],
 "compare": (["解法", "addNum", "getIntervals", "空間"],
   [["一、集合", "O(1)", "O(n log n)", "O(n)"],
    ["二、排序區間", "O(k)", "O(k)", "O(k) ✔"]]),
 "edges": [
   "<strong>重複加入同一個數</strong> → 已經被涵蓋，不動。",
   "<strong>value 連接兩個區間</strong> → 合併、刪掉一個。",
   "<strong>0</strong> → 沒有左邊，i = 0 要處理。",
 ],
 "follow": [
   ("h", "區間資料結構"),
   ("c", "第 715 題「Range 模組」：新增、刪除、查詢區間，是本題的強化版。第 2276 題「統計區間中的整數數目」也是維護不相交區間。"),
 ],
 "related": [
   "<strong>第 228 題 彙總區間</strong> —— 靜態版本",
   "<strong>第 57 題 插入區間</strong>",
   "<strong>第 715 題 Range 模組</strong>",
 ],
 "check": [
   "加入一個數時，有哪幾種情況？",
   "什麼情況下兩個區間會被合併？",
   "如果查詢很少，哪個方法比較好？",
 ],
})


# ==================== 354. Russian Doll Envelopes ====================
S["p354"] = '''class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # ★ 寬度遞增；寬度相同時高度「遞減」—— 讓同寬度的信封不可能互相套
        envelopes.sort(key=lambda e: (e[0], -e[1]))
        tails = []                                # 對高度做 LIS（第 300 題）
        for _, h in envelopes:
            i = bisect.bisect_left(tails, h)
            if i == len(tails):
                tails.append(h)
            else:
                tails[i] = h
        return len(tails)'''

S["p354_dp"] = '''class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        n = len(envelopes)
        dp = [1] * n                              # dp[i]：以第 i 個信封為最外層的最多層數
        for i in range(n):
            for j in range(i):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)'''

_p354 = [S.load(x) for x in ("p354", "p354_dp")]
for env, want in [([[5, 4], [6, 4], [6, 7], [2, 3]], 3), ([[1, 1], [1, 1], [1, 1]], 1)]:
    for sol in _p354:
        assert sol.maxEnvelopes([e[:] for e in env]) == want
for _ in range(2000):
    env = [[random.randint(1, 6), random.randint(1, 6)] for _ in range(random.randrange(1, 10))]
    assert _p354[0].maxEnvelopes([e[:] for e in env]) == _p354[1].maxEnvelopes([e[:] for e in env]), env
print("P354 OK")

emit({
 "num": 354, "slug": "russian-doll-envelopes",
 "en": [
   "You are given a 2D array of integers <code>envelopes</code> where <code>envelopes[i] = [w<sub>i</sub>, h<sub>i</sub>]</code> represents the width and the height of an envelope.",
   "One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.",
   "Return <em>the maximum number of envelopes you can Russian doll (i.e., put one inside the other)</em>.",
   "<strong>Note:</strong> You cannot rotate an envelope.",
 ],
 "zh": [
   "給你一個二維陣列 <code>envelopes</code>，<code>envelopes[i] = [w<sub>i</sub>, h<sub>i</sub>]</code> 是信封的寬和高。",
   "一個信封能放進另一個信封，當且僅當它的寬和高都<strong>嚴格小於</strong>另一個。",
   "回傳最多能有幾個信封像俄羅斯套娃一樣一層套一層。<strong>信封不能旋轉。</strong>",
 ],
 "examples": """範例 1
  輸入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
  輸出：3
  說明：[2,3] => [5,4] => [6,7]

範例 2
  輸入：envelopes = [[1,1],[1,1],[1,1]]
  輸出：1""",
 "constraints": [
   "1 ≤ <code>envelopes.length</code> ≤ 10⁵",
   "<code>envelopes[i].length == 2</code>",
   "1 ≤ <code>w<sub>i</sub>, h<sub>i</sub></code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【二維的最長遞增子序列】
    如果只有一個維度，就是第 300 題 LIS。
    兩個維度都要嚴格遞增 -> 先用排序處理掉一個維度。

【按寬度排序，對高度做 LIS】
    寬度遞增之後，只要高度也嚴格遞增就能套 ——
    但寬度「相同」的信封不能互套！

【關鍵技巧：寬度相同時，高度遞減排】
    [6, 4], [6, 7]：寬度相同
    如果高度遞增排：4, 7 -> LIS 會把它們都選進去 ✘
    如果高度遞減排：7, 4 -> 遞減的兩個數不可能同時在遞增序列裡 ✔

    這樣同寬度的信封最多只會被選一個，
    剩下的問題就是純粹的一維 LIS，可以用 O(n log n) 的二分解法。"""),
   ("c", """  排序後（寬遞增、同寬時高遞減）：
  [2,3] [5,4] [6,7] [6,4]
  高度：  3     4     7     4
  LIS：3, 4, 7 -> 長度 3 ✔
  若同寬時高度遞增排（[6,4] 在 [6,7] 前），高度 3, 4, 4, 7 可能把兩個寬 6 的都選進去 ✘"""),
 ],
 "approaches": [
   ap("解法一", "排序 + O(n²) DP", [
     ("c", S["p354_dp"]),
     "n = 10⁵ 時會超時。",
   ], "O(n²)", "O(n)", "", ""),

   ap("解法二", "特殊排序 + 二分 LIS", [
     ("c", S["p354"]),
   ], "O(n log n)", "O(n)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、DP", "O(n²)", "O(n)"],
    ["二、排序 + LIS", "O(n log n)", "O(n) ✔"]]),
 "edges": [
   "<strong>寬度相同</strong> → 不能互套；排序技巧處理。",
   "<strong>高度相同</strong> → 不能互套；LIS 用 bisect_left（嚴格遞增）處理。",
   "<strong>完全相同的信封</strong> → 只能選一個。",
 ],
 "follow": [
   ("h", "三維呢？"),
   ("c", "第 1691 題「堆疊長方體的最大高度」：長方體可以旋轉，每個先排序三個邊，再按一個維度排序後做 O(n²) DP。三維 LIS 沒有簡單的 O(n log n) 解（需要 CDQ 分治等進階技巧）。"),
 ],
 "related": [
   "<strong>第 300 題 最長遞增子序列</strong>",
   "<strong>第 1691 題 堆疊長方體的最大高度</strong>",
   "<strong>第 646 題 最長數對鏈</strong>",
 ],
 "check": [
   "排序後為什麼可以只看高度？",
   "寬度相同時為什麼要把高度遞減排序？",
 ],
})


# ==================== 355. Design Twitter ====================
S["p355"] = '''class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)       # 使用者 -> [(時間, tweetId), ...]（依時間遞增）
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}      # 自己的貼文也要算
        # ★ 多路合併：每個人的貼文已經依時間排序，只取最新的 10 則
        heap = []
        for u in users:
            if self.tweets[u]:
                i = len(self.tweets[u]) - 1
                t, tid = self.tweets[u][i]
                heap.append((-t, tid, u, i))
        heapq.heapify(heap)
        feed = []
        while heap and len(feed) < 10:
            t, tid, u, i = heapq.heappop(heap)
            feed.append(tid)
            if i > 0:                                  # 同一人的上一則
                t2, tid2 = self.tweets[u][i - 1]
                heapq.heappush(heap, (-t2, tid2, u, i - 1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)'''

_cls = S.loadns("p355", {"defaultdict": defaultdict})["Twitter"]
for _ in range(300):
    tw, posts, fol = _cls(), [], defaultdict(set)
    tid = 0
    for _ in range(80):
        r = random.random()
        u, v = random.randrange(5), random.randrange(5)
        if r < 0.35:
            tid += 1
            tw.postTweet(u, tid)
            posts.append((u, tid))
        elif r < 0.55:
            tw.follow(u, v)
            if u != v:
                fol[u].add(v)
        elif r < 0.7:
            tw.unfollow(u, v)
            fol[u].discard(v)
        else:
            want = [t for (a, t) in reversed(posts) if a == u or a in fol[u]][:10]
            assert tw.getNewsFeed(u) == want
print("P355 OK")

emit({
 "num": 355, "slug": "design-twitter",
 "en": [
   "Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the <code>10</code> most recent tweets in the user's news feed.",
   "Implement the <code>Twitter</code> class:",
   ("ul", ["<code>Twitter()</code> Initializes your twitter object.",
           "<code>void postTweet(int userId, int tweetId)</code> Composes a new tweet with ID <code>tweetId</code> by the user <code>userId</code>. Each call to this function will be made with a unique <code>tweetId</code>.",
           "<code>List&lt;Integer&gt; getNewsFeed(int userId)</code> Retrieves the <code>10</code> most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be <strong>ordered from most recent to least recent</strong>.",
           "<code>void follow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started following the user with ID <code>followeeId</code>.",
           "<code>void unfollow(int followerId, int followeeId)</code> The user with ID <code>followerId</code> started unfollowing the user with ID <code>followeeId</code>."]),
 ],
 "zh": [
   "設計一個簡化版的 Twitter：使用者可以發文、追蹤／取消追蹤別人，並看到動態牆上最新的 <code>10</code> 則貼文。",
   ("ul", ["<code>postTweet(userId, tweetId)</code>：使用者發一則新貼文（tweetId 不重複）。",
           "<code>getNewsFeed(userId)</code>：回傳動態牆上最新的 10 則貼文 ID——來自自己或自己追蹤的人，<strong>由新到舊</strong>。",
           "<code>follow(followerId, followeeId)</code>：開始追蹤。",
           "<code>unfollow(followerId, followeeId)</code>：取消追蹤。"]),
 ],
 "examples": """範例
  postTweet(1, 5)
  getNewsFeed(1)   -> [5]
  follow(1, 2)
  postTweet(2, 6)
  getNewsFeed(1)   -> [6, 5]
  unfollow(1, 2)
  getNewsFeed(1)   -> [5]""",
 "constraints": [
   "1 ≤ <code>userId, followerId, followeeId</code> ≤ 500",
   "0 ≤ <code>tweetId</code> ≤ 10⁴",
   "所有 tweetId 互不相同",
   "最多呼叫 3 × 10⁴ 次",
   "<code>followerId != followeeId</code>",
 ],
 "idea": [
   ("c", """【資料結構】
    tweets[user]    = 這個人發過的貼文，依時間遞增（加上全域時間戳）
    following[user] = 他追蹤的人（集合，追蹤／取消都是 O(1)）

【getNewsFeed = 合併 k 個有序串列，只取前 10】
    每個人的貼文串列都已依時間排序。
    把每個人「最新的一則」放進最大堆積（以時間為鍵），
    彈出最新的一則，再把同一個人的「上一則」放進去 ——
    這就是第 23 題「合併 K 個有序串列」。
    只需要彈 10 次。

【細節】
    - 自己的貼文也要出現在動態牆
    - 不能追蹤自己（避免重複）
    - 取消追蹤一個沒追蹤的人：discard 不會報錯

【複雜度】
    k = 追蹤人數
    建堆 O(k)，彈 10 次 O(10 log k)。"""),
 ],
 "approaches": [
   ap("解法", "雜湊表 + 最大堆積多路合併", [
     ("c", S["p355"]),
   ], "getNewsFeed O(k + 10 log k)", "O(使用者 + 貼文 + 追蹤關係)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>沒有追蹤任何人</strong> → 只看到自己的貼文。",
   "<strong>貼文少於 10 則</strong> → 回傳全部。",
   "<strong>取消追蹤不存在的關係</strong> → 不報錯。",
   "<strong>同一時間戳</strong> → 用全域遞增的計數器，保證唯一。",
 ],
 "follow": [
   ("h", "真實世界：推模式 vs 拉模式"),
   ("c", """本解法是「拉（pull）」：讀取時才合併，寫入便宜、讀取貴。
「推（push）」：發文時直接寫進每個追蹤者的動態牆，讀取便宜、寫入貴。
真正的 Twitter 混合使用：一般使用者用推，名人（百萬粉絲）用拉，避免一則貼文要寫一百萬次。"""),
 ],
 "related": [
   "<strong>第 23 題 合併 K 個排序鏈結串列</strong>",
   "<strong>第 373 題 查找和最小的 K 對數字</strong> —— 同樣的多路合併",
 ],
 "check": [
   "getNewsFeed 為什麼可以看成「合併 K 個有序串列」？",
   "為什麼需要全域的時間戳？",
   "推模式和拉模式各有什麼優缺點？",
 ],
})


# ==================== 357. Count Numbers with Unique Digits ====================
S["p357"] = '''class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1                          # 只有 0
        total = 10                            # 一位數：0..9
        cur = 9                               # 恰好 k 位的個數（k 從 1 開始是 9 個：1..9）
        for k in range(2, n + 1):
            cur *= 10 - (k - 1)               # ★ 第 k 位有 10-(k-1) 種選擇（不和前面重複）
            total += cur
        return total'''

_p357 = S.load("p357")
for n in range(0, 7):
    want = sum(1 for x in range(10 ** n) if len(set(str(x))) == len(str(x)))
    assert _p357.countNumbersWithUniqueDigits(n) == want, n
assert _p357.countNumbersWithUniqueDigits(8) == 2345851
print("P357 OK")

emit({
 "num": 357, "slug": "count-numbers-with-unique-digits",
 "en": [
   "Given an integer <code>n</code>, return the count of all numbers with unique digits, <code>x</code>, where <code>0 &lt;= x &lt; 10<sup>n</sup></code>.",
 ],
 "zh": [
   "給你一個整數 <code>n</code>，計算 <code>0 ≤ x &lt; 10<sup>n</sup></code> 範圍內，<strong>各位數字都不重複</strong>的整數 <code>x</code> 有幾個。",
 ],
 "examples": """範例 1
  輸入：n = 2
  輸出：91
  說明：0 到 99 共 100 個數，扣掉 11, 22, 33, 44, 55, 66, 77, 88, 99。

範例 2
  輸入：n = 0
  輸出：1""",
 "constraints": [
   "0 ≤ <code>n</code> ≤ 8",
 ],
 "idea": [
   ("c", """【按位數分開數：排列組合】
    恰好 1 位：0..9 共 10 個
    恰好 2 位：第一位 1..9（9 種），第二位 0..9 扣掉第一位（9 種）-> 81
    恰好 3 位：9 × 9 × 8 = 648
    恰好 k 位：9 × 9 × 8 × ... × (11 - k)

    第一位不能是 0（否則就不是 k 位數），所以是 9 種；
    之後每一位都要避開前面已用過的數字。

【總和】
    n = 2：10 + 81 = 91
    n = 3：91 + 648 = 739

【n > 10】
    超過 10 位一定有重複數字（只有 10 種數字），增加 0。"""),
   ("t", ["n", "0", "1", "2", "3", "4", "5"],
    [["恰好 n 位", "—", "10", "81", "648", "4536", "27216"],
     ["累計", "1", "10", "91", "739", "5275", "32491"]]),
 ],
 "approaches": [
   ap("解法", "排列計數", [
     ("c", S["p357"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>n = 0</strong> → 只有 0，答案 1。",
   "<strong>n = 1</strong> → 10（包含 0）。",
   "<strong>n ≥ 11</strong> → 和 n = 10 相同（本題 n ≤ 8）。",
 ],
 "follow": [
   ("h", "上限不是 10ⁿ 時？"),
   ("c", "第 2376 題「統計特殊整數」：數 1..n 中各位數字不重複的整數，要用數位 DP（第 233 題的模板）加上「已用數字」的位元遮罩。"),
 ],
 "related": [
   "<strong>第 2376 題 統計特殊整數</strong>",
   "<strong>第 1012 題 至少有 1 位重複的數字</strong> —— 補集",
   "<strong>第 233 題 數字 1 的個數</strong> —— 數位 DP",
 ],
 "check": [
   "恰好 k 位且數字不重複的數有幾個？為什麼第一位只有 9 種？",
   "n 超過 10 時答案會怎麼變化？",
 ],
})


# ==================== 363. Max Sum of Rectangle No Larger Than K ====================
S["p363"] = '''class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        if m > n:                                   # 讓 m 是較小的維度（枚舉的那一維）
            matrix = [list(r) for r in zip(*matrix)]
            m, n = n, m
        best = -float("inf")
        for top in range(m):
            col = [0] * n                           # 第 top..bottom 列、每一欄的總和
            for bottom in range(top, m):
                for j in range(n):
                    col[j] += matrix[bottom][j]
                # ★ 一維問題：col 中和 <= k 的最大子陣列和
                seen = [0]                          # 已出現的前綴和（排序）
                prefix = 0
                for x in col:
                    prefix += x
                    # 要找最小的 P[i] >= prefix - k，使 prefix - P[i] <= k 且盡量大
                    i = bisect.bisect_left(seen, prefix - k)
                    if i < len(seen):
                        best = max(best, prefix - seen[i])
                        if best == k:
                            return k                # 不可能更好了
                    bisect.insort(seen, prefix)
        return best'''

S["p363_brute"] = '''class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]   # 二維前綴和（第 304 題）
        for i in range(m):
            for j in range(n):
                P[i + 1][j + 1] = P[i][j + 1] + P[i + 1][j] - P[i][j] + matrix[i][j]
        best = -float("inf")
        for r1 in range(m):
            for r2 in range(r1, m):
                for c1 in range(n):
                    for c2 in range(c1, n):
                        s = P[r2 + 1][c2 + 1] - P[r1][c2 + 1] - P[r2 + 1][c1] + P[r1][c1]
                        if s <= k:
                            best = max(best, s)
        return best'''

_p363 = [S.load(x) for x in ("p363", "p363_brute")]
for M, k, want in [([[1, 0, 1], [0, -2, 3]], 2, 2), ([[2, 2, -1]], 3, 3)]:
    for sol in _p363:
        assert sol.maxSumSubmatrix(M, k) == want
for _ in range(800):
    m, n = random.randrange(1, 5), random.randrange(1, 5)
    M = [[random.randint(-5, 5) for _ in range(n)] for _ in range(m)]
    mn = min(min(r) for r in M)
    k = random.randint(mn, 15)
    assert _p363[0].maxSumSubmatrix(M, k) == _p363[1].maxSumSubmatrix(M, k), (M, k)
print("P363 OK")

emit({
 "num": 363, "slug": "max-sum-of-rectangle-no-larger-than-k",
 "en": [
   "Given an <code>m x n</code> matrix <code>matrix</code> and an integer <code>k</code>, return <em>the max sum of a rectangle in the matrix such that its sum is no larger than</em> <code>k</code>.",
   "It is <strong>guaranteed</strong> that there will be a rectangle with a sum no larger than <code>k</code>.",
   "<strong>Follow up:</strong> What if the number of rows is much larger than the number of columns?",
 ],
 "zh": [
   "給你一個 <code>m x n</code> 的矩陣和整數 <code>k</code>，找出矩陣中總和<strong>不超過 <code>k</code></strong> 的矩形，回傳這種矩形的最大總和。",
   "保證至少存在一個總和不超過 <code>k</code> 的矩形。",
   "<strong>進階：</strong>如果列數遠大於行數呢？",
 ],
 "examples": """範例 1
  輸入：matrix = [[1,0,1],[0,-2,3]], k = 2
  輸出：2
  說明：矩形 [[0,1],[-2,3]] 的和是 2，是不超過 2 的最大值。

範例 2
  輸入：matrix = [[2,2,-1]], k = 3
  輸出：3""",
 "constraints": [
   "1 ≤ <code>m, n</code> ≤ 100",
   "−100 ≤ <code>matrix[i][j]</code> ≤ 100",
   "−10⁵ ≤ <code>k</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【把二維壓成一維】
    枚舉矩形的上邊 top 和下邊 bottom（O(m²) 種），
    把這幾列「壓扁」：col[j] = matrix[top..bottom][j] 的和。
    問題變成：一維陣列 col 中，和 <= k 的最大子陣列和。

【一維子問題：前綴和 + 有序集合】
    子陣列和 = P[j] - P[i]（i < j）
    要 P[j] - P[i] <= k 而且盡量大
    <=> P[i] >= P[j] - k，而且 P[i] 盡量小
    -> 在已出現的前綴和中，二分找「第一個 >= P[j] - k」的。

    Kadane（第 53 題）在這裡不能用 ——
    它求的是「最大」，沒有「不超過 k」的限制。

【進階：列數遠大於行數】
    讓「枚舉的那一維」是比較小的那個。
    m 小、n 大：枚舉上下邊 O(m²)，一維處理 O(n log n)
    總共 O(m² · n log n)。"""),
 ],
 "approaches": [
   ap("解法一", "二維前綴和 + 枚舉所有矩形", [
     ("c", S["p363_brute"]),
   ], "O(m² n²)", "O(mn)", "", ""),

   ap("解法二", "壓縮成一維 + 有序前綴和", [
     ("c", S["p363"]),
     "Python 的 <code>insort</code> 插入是 O(n)，嚴格來說一維部分是 O(n²)；用平衡樹（或 <code>sortedcontainers</code>）才是 O(n log n)。n ≤ 100 時影響不大。",
   ], "O(min² · max · log max)", "O(max)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、枚舉所有矩形", "O(m²n²)", "O(mn)"],
    ["二、壓縮 + 有序集合", "O(m²·n log n)", "O(n) ✔"]]),
 "edges": [
   "<strong>剛好等於 k</strong> → 可以提早結束。",
   "<strong>全部是負數</strong> → 答案可能是某個單一格子。",
   "<strong>只有一列</strong> → 直接做一維。",
 ],
 "follow": [
   ("h", "組合了哪些題"),
   ("c", "二維壓一維：第 85 題（最大矩形）、第 1074 題（元素和為目標值的子矩陣數量）。一維「不超過 k 的最大子陣列和」：前綴和 + 有序集合，和第 220 題、第 327 題同一套工具。"),
 ],
 "related": [
   "<strong>第 53 題 最大子陣列和</strong>",
   "<strong>第 304 題 二維區域和檢索</strong>",
   "<strong>第 1074 題 元素和為目標值的子矩陣數量</strong>",
 ],
 "check": [
   "怎麼把二維問題轉成一維？",
   "一維時，為什麼要找「第一個 ≥ P[j] − k 的前綴和」？",
   "為什麼 Kadane 演算法不適用？",
   "列數遠大於行數時，應該枚舉哪一個維度？",
 ],
})


# ==================== 365. Water and Jug Problem ====================
S["p365"] = '''class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:                    # 兩個壺加起來都裝不下
            return False
        # ★ 裴蜀定理：能量出的水量恰好是 gcd(x, y) 的倍數
        return target % math.gcd(x, y) == 0'''

S["p365_bfs"] = '''class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        seen = {(0, 0)}
        q = deque([(0, 0)])
        while q:
            a, b = q.popleft()                # 兩個壺目前的水量
            if a + b == target:
                return True
            pour_ab = min(a, y - b)           # a 倒進 b 能倒多少
            pour_ba = min(b, x - a)
            for nxt in ((x, b), (a, y), (0, b), (a, 0),          # 裝滿、倒掉
                        (a - pour_ab, b + pour_ab), (a + pour_ba, b - pour_ba)):   # 互倒
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
        return False'''

_p365 = [S.load("p365"), S.load("p365_bfs", extra={"deque": deque})]
for x, y, t, want in [(3, 5, 4, True), (2, 6, 5, False), (1, 2, 3, True)]:
    for sol in _p365:
        assert sol.canMeasureWater(x, y, t) == want
for x in range(1, 12):
    for y in range(1, 12):
        for t in range(0, 25):
            assert _p365[0].canMeasureWater(x, y, t) == _p365[1].canMeasureWater(x, y, t), (x, y, t)
print("P365 OK")

emit({
 "num": 365, "slug": "water-and-jug-problem",
 "en": [
   "You are given two jugs with capacities <code>x</code> liters and <code>y</code> liters. You have an infinite water supply. Return whether the total amount of water in both jugs may reach <code>target</code> using the following operations:",
   ("ul", ["Fill either jug completely with water.",
           "Completely empty either jug.",
           "Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty."]),
 ],
 "zh": [
   "有兩個容量分別為 <code>x</code> 公升和 <code>y</code> 公升的水壺，水源無限。只能做以下操作，問兩個壺裡的<strong>水量總和</strong>能不能剛好等於 <code>target</code>：",
   ("ul", ["把任一個壺裝滿。",
           "把任一個壺倒空。",
           "把一個壺的水倒進另一個，直到對方滿了或自己空了為止。"]),
 ],
 "examples": """範例 1
  輸入：x = 3, y = 5, target = 4
  輸出：true
  說明：（《終極警探 3》裡的經典謎題）
    裝滿 5 -> 倒進 3（5 壺剩 2）-> 倒空 3 -> 2 倒進 3
    -> 裝滿 5 -> 倒進 3 直到滿（倒 1）-> 5 壺剩 4 ✔

範例 2
  輸入：x = 2, y = 6, target = 5
  輸出：false

範例 3
  輸入：x = 1, y = 2, target = 3
  輸出：true""",
 "constraints": [
   "1 ≤ <code>x, y, target</code> ≤ 10³",
 ],
 "idea": [
   ("c", """【方法一：BFS 窮舉狀態】
    狀態 = (壺 A 的水量, 壺 B 的水量)，共 (x+1)(y+1) 種。
    每個狀態有 6 種操作：裝滿 A/B、倒空 A/B、A 倒 B、B 倒 A。
    BFS 看能不能到達「總和 = target」的狀態。

【方法二：數學（裴蜀定理）】
    每次操作後，總水量的變化量只可能是 ±x 或 ±y（倒來倒去不改變總量）。
    所以能量出的總量都是 a·x + b·y 的形式（a、b 是整數）。

    裴蜀定理：a·x + b·y 能表示的數，恰好是 gcd(x, y) 的所有倍數。

    結論：target 能量出 <=>
        target <= x + y（壺裝得下）
        而且 target 是 gcd(x, y) 的倍數

【範例】x = 3, y = 5：gcd = 1，任何 <= 8 的量都可以。
        x = 2, y = 6：gcd = 2，奇數都不行 -> 5 不行。"""),
 ],
 "approaches": [
   ap("解法一", "BFS 狀態搜尋", [
     ("c", S["p365_bfs"]),
   ], "O(x · y)", "O(x · y)", "", ""),

   ap("解法二", "裴蜀定理", [
     ("c", S["p365"]),
   ], "O(log min(x, y))", "O(1)", "輾轉相除法", "", optimal=True),
 ],
 "compare": (["解法", "時間", "空間"],
   [["一、BFS", "O(xy)", "O(xy)"],
    ["二、gcd", "O(log min(x,y))", "O(1) ✔"]]),
 "edges": [
   "<strong>target &gt; x + y</strong> → 裝不下，false。",
   "<strong>target = x + y</strong> → 兩個都裝滿，true。",
   "<strong>target = 0</strong> → 什麼都不做就是 0（本題 target ≥ 1）。",
 ],
 "follow": [
   ("h", "裴蜀定理的其他應用"),
   ("c", "第 1250 題「檢查好陣列」：能不能用整數係數組合出 1 ⟺ 所有數的 gcd 是 1。"),
 ],
 "related": [
   "<strong>第 1250 題 檢查「好陣列」</strong>",
   "<strong>第 914 題 卡牌分組</strong> —— gcd",
 ],
 "check": [
   "BFS 的狀態是什麼？有哪幾種操作？",
   "為什麼總水量的變化只可能是 ±x 或 ±y？",
   "裴蜀定理說了什麼？",
 ],
})
