# -*- coding: utf-8 -*-
"""第 93–96 題。"""
import random, itertools, functools
from authoring import emit, ap
from runner import Src, TreeNode

S = Src()
random.seed(93)

# ==================== 93. Restore IP Addresses ====================
S["p93"] = '''class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n < 4 or n > 12:          # 四段各 1~3 個字元
            return []

        out = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == 4:
                if start == n:       # 剛好用完所有字元
                    out.append(".".join(path))
                return

            # 剪枝：剩下的字元數必須夠（也不能太多）
            remain_segments = 4 - len(path)
            remain_chars = n - start
            if not (remain_segments <= remain_chars <= remain_segments * 3):
                return

            for length in (1, 2, 3):
                if start + length > n:
                    break
                seg = s[start:start + length]
                # 前導零：長度 > 1 就不能以 '0' 開頭
                if length > 1 and seg[0] == "0":
                    break
                if int(seg) > 255:
                    break            # 3 位數超過 255，更長也不用試
                path.append(seg)
                backtrack(start + length)
                path.pop()

        backtrack(0)
        return out'''

S["p93_loops"] = '''class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        out = []

        def ok(seg: str) -> bool:
            if not (1 <= len(seg) <= 3):
                return False
            if len(seg) > 1 and seg[0] == "0":
                return False
            return int(seg) <= 255

        # 直接枚舉三個切點（因為固定就是四段）
        for i in range(1, min(4, n)):
            for j in range(i + 1, min(i + 4, n)):
                for k in range(j + 1, min(j + 4, n)):
                    a, b, c, d = s[:i], s[i:j], s[j:k], s[k:]
                    if ok(a) and ok(b) and ok(c) and ok(d):
                        out.append(a + "." + b + "." + c + "." + d)

        return out'''

_p93 = [S.load(k) for k in ("p93", "p93_loops")]


def _p93_ref(s):
    n = len(s)
    res = []

    def ok(seg):
        return (1 <= len(seg) <= 3 and not (len(seg) > 1 and seg[0] == "0")
                and int(seg) <= 255)

    for i in range(1, n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                parts = [s[:i], s[i:j], s[j:k], s[k:]]
                if all(ok(p) for p in parts):
                    res.append(".".join(parts))
    return sorted(res)


for s_ in ["25525511135", "0000", "101023", "1111", "010010", "1", "", "255255255255",
           "000256", "9999999999999"]:
    e = _p93_ref(s_)
    for sol in _p93:
        g = sorted(sol.restoreIpAddresses(s_))
        assert g == e, ("P93", s_, sol, g, e)
for _ in range(3000):
    s_ = "".join(random.choice("0125") for _ in range(random.randint(0, 13)))
    e = _p93_ref(s_)
    for sol in _p93:
        g = sorted(sol.restoreIpAddresses(s_))
        assert g == e, ("P93", s_, sol, g, e)
print("P93 solutions OK")

_P93_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">s = &quot;25525511135&quot;：在 11 個字元裡放三個切點，切成四段</text>
            <g font-family="monospace" font-size="16" text-anchor="middle">
              <text x="70" y="64" fill="var(--accent)">2</text>
              <text x="110" y="64" fill="var(--accent)">5</text>
              <text x="150" y="64" fill="var(--accent)">5</text>
              <text x="190" y="64" fill="var(--gold)">2</text>
              <text x="230" y="64" fill="var(--gold)">5</text>
              <text x="270" y="64" fill="var(--gold)">5</text>
              <text x="310" y="64" fill="#ff8a65">1</text>
              <text x="350" y="64" fill="#ff8a65">1</text>
              <text x="390" y="64" fill="var(--accent)">1</text>
              <text x="430" y="64" fill="var(--accent)">3</text>
              <text x="470" y="64" fill="var(--accent)">5</text>
            </g>
            <g stroke="var(--gold)" stroke-width="2" stroke-dasharray="4 3">
              <line x1="170" y1="44" x2="170" y2="78"/>
              <line x1="290" y1="44" x2="290" y2="78"/>
              <line x1="370" y1="44" x2="370" y2="78"/>
            </g>
            <text x="300" y="100" fill="var(--gold)" font-size="13" text-anchor="middle">255 . 255 . 11 . 135 ✔</text>
            <line x1="20" y1="120" x2="620" y2="120" stroke="var(--border)"/>
            <text x="20" y="148" fill="var(--text-muted)" font-size="12">每一段的三個合法條件：</text>
            <g font-size="12">
              <text x="50" y="176" fill="var(--accent)">① 長度 1–3</text>
              <text x="230" y="176" fill="var(--text-muted)">&quot;1234&quot; ✘</text>
              <text x="50" y="202" fill="var(--accent)">② 數值 ≤ 255</text>
              <text x="230" y="202" fill="var(--text-muted)">&quot;256&quot; ✘</text>
              <text x="50" y="228" fill="var(--accent)">③ 沒有前導零（除非就是 &quot;0&quot;）</text>
              <text x="300" y="228" fill="var(--text-muted)">&quot;01&quot; ✘、&quot;0&quot; ✔</text>
            </g>
            <line x1="20" y1="248" x2="620" y2="248" stroke="var(--border)"/>
            <text x="20" y="276" fill="var(--gold)" font-size="12">長度剪枝：剩下 k 段時，剩餘字元數必須在 [k, 3k] 之間</text>
            <text x="20" y="300" fill="var(--text-muted)" font-size="12">例：已放 2 段、剩 5 個字元 → 剩 2 段最多裝 6 個、最少 2 個 → 5 在範圍內，繼續</text>
            <text x="20" y="324" fill="var(--text-muted)" font-size="12">總長度必須在 [4, 12] —— 不在這個範圍直接回空清單</text>'''

emit({
 "num": 93, "slug": "restore-ip-addresses",
 "en": [
   "A <strong>valid IP address</strong> consists of exactly four integers separated by single "
   "dots. Each integer is between <code>0</code> and <code>255</code> "
   "(<strong>inclusive</strong>) and <strong>cannot have leading zeros</strong>.",
   "Given a string <code>s</code> containing only digits, return <em>all possible valid IP "
   "addresses that can be formed by inserting dots into </em><code>s</code>. You are "
   "<strong>not</strong> allowed to reorder or remove any digits in <code>s</code>.",
 ],
 "zh": [
   "<strong>有效的 IP 位址</strong>由四個整數組成，用單一個點分隔。"
   "每個整數在 <code>0</code> 到 <code>255</code> 之間（含），"
   "而且<strong>不能有前導零</strong>。",
   "給你一個只含數字的字串 <code>s</code>，"
   "回傳所有「在 <code>s</code> 裡插入三個點」能得到的有效 IP 位址。"
   "<strong>不能</strong>重排或刪除任何數字。",
 ],
 "pre": [
   ("note", "三個合法條件，第三個最容易漏", [
     ("c", """每一段必須同時滿足：

  ① 長度 1 到 3
  ② 數值 0 到 255
  ③ 【沒有前導零】—— 長度 > 1 時不能以 '0' 開頭

    "0"    ✔ 合法
    "00"   ✘ 前導零
    "01"   ✘ 前導零
    "255"  ✔
    "256"  ✘ > 255
    "1234" ✘ 長度 > 3

條件 ③ 為什麼存在？
    因為真實的 IP 位址不會寫成 "192.168.001.1"。
    而且如果允許前導零，"0000" 就會有很多種切法
    （"0.0.0.0"、"0.0.00.0"…），答案變得沒有意義。

長度的必要條件：
    四段各 1~3 個字元 -> 總長度必須在 [4, 12]
    不在這個範圍 -> 直接回空清單

    "1"              長度 1 < 4  -> []
    "9999999999999"  長度 13 > 12 -> []"""),
     "<strong>「0.0.0.0」是合法的 IP</strong>（<code>\"0000\"</code> → <code>[\"0.0.0.0\"]</code>），"
     "而 <code>\"010010\"</code> 有兩種切法（<code>\"0.10.0.10\"</code> 和 <code>\"0.100.1.0\"</code>）—— "
     "這兩筆是最能抓出前導零 bug 的測資。",
   ]),
 ],
 "examples": """範例 1
  輸入：s = "25525511135"
  輸出：["255.255.11.135","255.255.111.35"]

範例 2
  輸入：s = "0000"
  輸出：["0.0.0.0"]

範例 3
  輸入：s = "101023"
  輸出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 20",
   "<code>s</code> 只含數字",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>長度到 20</strong>，但<strong>只有 4 到 12 的長度才可能有答案</strong>。"
       "第一行就可以擋掉大部分輸入。",
       "<strong>答案的數量很少</strong>：最多就是 "
       "<code>C(11, 3) = 165</code> 種切法（長度 12 時），再扣掉不合法的。"
       "所以<strong>暴力枚舉三個切點完全可行</strong>。",
       "<strong>只含數字</strong>，不用處理其他字元。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P93_FIG, "0 0 640 338"),
   "兩種寫法：<strong>回溯</strong>（通用，可以推廣到「k 段」）"
   "或<strong>三層迴圈枚舉切點</strong>（因為段數固定是 4，可以寫死）。",
 ],
 "approaches": [
   ap("解法一", "回溯 + 長度剪枝（最推薦）", [
     ("c", S["p93"]),
     ("h", "終止條件的兩個部分"),
     ("c", """if len(path) == 4:
    if start == n:
        out.append(".".join(path))
    return

兩個條件缺一不可：
    len(path) == 4   剛好四段
    start == n       剛好用完所有字元

    "25525511135" 切成 "2.5.5.2" 之後 len(path) == 4，
    但 start 只到 4，還剩 "5511135" 沒用 -> 不合法 ✘

注意即使 start != n 也要 return ——
不能繼續往下切（已經四段了）。"""),
     ("h", "長度剪枝"),
     ("c", """remain_segments = 4 - len(path)      還要切幾段
remain_chars = n - start             還剩幾個字元

每段 1~3 個字元，所以：
    remain_segments <= remain_chars <= remain_segments * 3

不在這個範圍就直接 return。

    已放 1 段、剩 10 個字元、還要 3 段：
        3 <= 10 <= 9 ？  10 > 9 -> 不可能 -> 剪掉 ✔

    已放 3 段、剩 0 個字元、還要 1 段：
        1 <= 0 ？ 不成立 -> 剪掉 ✔

這個剪枝大幅減少了無用的搜尋。
（雖然這題規模很小，剪不剪都會過，
  但它是一個很好的「可行性剪枝」練習。）"""),
     ("h", "三個 <code>break</code>（不是 <code>continue</code>）"),
     ("c", """for length in (1, 2, 3):
    if start + length > n:
        break              # 更長只會更越界

    seg = s[start:start+length]
    if length > 1 and seg[0] == "0":
        break              # 開頭是 '0' 的話，更長也一定有前導零

    if int(seg) > 255:
        break              # 3 位數超過 255，更長只會更大

三個都用 break 而不是 continue，
因為「length 再大只會更糟」——
這是單調性帶來的剪枝。

第二個 break 特別值得注意：
    seg[0] == '0' 且 length > 1 -> 這一段有前導零
    而 length = 3 時 seg 還是以 '0' 開頭 -> 一樣不合法
    所以可以直接 break ✔

    （length = 1 時 "0" 是合法的，
      而它已經在 length = 1 那一輪被試過了。）"""),
     "<strong>這個版本可以直接推廣到「切成 k 段」</strong> —— "
     "把 4 換成參數即可。<strong>回溯的通用性就在這裡。</strong>",
   ], "O(3⁴) = O(1)", "O(1)", "最多 81 種切法", "path + 遞迴深度 4", optimal=True),

   ap("解法二", "三層迴圈枚舉切點（因為段數固定）", [
     "既然一定是四段，就<strong>直接枚舉三個切點的位置</strong>。",
     ("c", S["p93_loops"]),
     ("c", """三個切點 i < j < k 把字串切成：
    s[:i]  s[i:j]  s[j:k]  s[k:]

每一段的長度限制在 1~3，所以：
    i ∈ [1, min(4, n))         第一段長度 1~3
    j ∈ [i+1, min(i+4, n))     第二段長度 1~3
    k ∈ [j+1, min(j+4, n))     第三段長度 1~3
    第四段是 s[k:]，長度由 ok() 檢查

迴圈次數最多 3 × 3 × 3 = 27 次 —— 常數時間。

好處：沒有遞迴，扁平、好讀。
壞處：只適用於「段數固定」的情況。
      如果題目改成「切成 k 段」，就得改回回溯。"""),
     "<strong>把 <code>ok()</code> 抽成一個函式</strong>，"
     "讓「合法性檢查」和「枚舉切點」分開 —— "
     "這樣三個條件只寫一次，不會在四個地方各抄一遍。",
     "<strong>在「段數固定且很小」的情況下，這個版本比回溯清楚。</strong>",
   ], "O(1)", "O(1)", "最多 27 次迴圈", "只有輸出"),
 ],
 "compare": (["解法", "時間", "推廣到 k 段？", "好讀程度", "備註"],
   [["一、回溯 + 剪枝", "O(3⁴)", "✔ 改一個參數", "★★★★☆", "通用，面試預設"],
    ["二、三層迴圈", "O(27)", "✘", "★★★★★", "段數固定時最清楚"]]),
 "edges": [
   "<strong>長度不足或過長</strong>：<code>\"1\"</code>、<code>\"9999999999999\"</code> → <code>[]</code>。",
   "<strong>全是 0</strong>：<code>\"0000\"</code> → <code>[\"0.0.0.0\"]</code>（只有一種）。"
   "<strong>沒有前導零檢查的話會產生很多種。</strong>",
   "<strong>前導零的關鍵測資</strong>：<code>\"010010\"</code> → "
   "<code>[\"0.10.0.10\", \"0.100.1.0\"]</code>（兩種）。",
   "<strong>超過 255</strong>：<code>\"000256\"</code> → <code>[]</code>。",
   "<strong>剛好 12 個字元</strong>：<code>\"255255255255\"</code> → "
   "<code>[\"255.255.255.255\"]</code>（只有一種，每段都必須是 3 個字元）。",
   "<strong>多種答案</strong>：<code>\"101023\"</code> → 5 種。",
   "<strong>沒有答案但長度合法</strong>：<code>\"1111\"</code> → <code>[\"1.1.1.1\"]</code>（有一種）。",
 ],
 "follow": [
   ("h", "追問一：如果要支援 IPv6 呢？"),
   "IPv6 是<strong>八段</strong>，每段是 <strong>1 到 4 個十六進位數字</strong>，"
   "而且<strong>允許前導零</strong>（<code>\"0001\"</code> 是合法的）。"
   "還有 <code>\"::\"</code> 可以縮寫連續的全零段 —— 那讓解析複雜非常多。",
   "<strong>回溯版只要改三個參數</strong>（段數 4→8、最大長度 3→4、合法性檢查），"
   "三層迴圈版就得整個重寫成八層 —— "
   "<strong>這就是通用解法的價值。</strong>",
   ("h", "追問二：這和第 468 題（驗證 IP 位址）的關係？"),
   "第 468 題是「給你一個字串，判斷它是 IPv4、IPv6、還是都不是」—— "
   "<strong>它只需要驗證，不需要枚舉切法</strong>（點已經在那裡了）。",
   "<strong>兩題共用同一個 <code>ok()</code> 函式</strong>，"
   "但一個是「驗證」、一個是「生成」。"
   "<strong>「驗證」和「生成」是一對常見的對照</strong>（見第 54/59 題、第 12/13 題）。",
   ("h", "追問三：這題的剪枝為什麼值得寫？"),
   "在 n ≤ 20 的規模下，剪不剪都會過。"
   "<strong>但「長度剪枝」是一個極通用的模式</strong>：",
   ("c", """「還需要 k 個，每個佔 [lo, hi] 個單位，剩下 m 個單位」
    可行的必要條件：k × lo <= m <= k × hi

這個檢查在很多題目都適用：
    第 93 題   切成四段，每段 1~3 個字元
    第 131 題  回文分割（切成任意段）
    第 77 題   從 n 個選 k 個（剩下的數字夠不夠）
    第 39 題   組合總和（剩下的最小值 × 個數 <= target）

它的成本是 O(1)，卻能砍掉整棵子樹 ——
【最划算的剪枝，永遠是那些 O(1) 就能判斷的必要條件】。""",),
   ("h", "追問四：為什麼真實的 IP 解析比這題複雜？"),
   ("ul", [
     "<strong>歷史包袱</strong>：<code>inet_aton</code> 接受 "
     "<code>\"127.1\"</code>（= 127.0.0.1）、八進位（<code>\"0177.0.0.1\"</code>）、"
     "十六進位（<code>\"0x7f.0.0.1\"</code>）—— 這些都是合法的",
     "<strong>前導零的歧義</strong>：<code>\"010\"</code> 在某些解析器裡是八進位的 8，"
     "在另一些裡是十進位的 10 —— <strong>這造成過真實的安全漏洞</strong>"
     "（SSRF 繞過、存取控制清單被繞過）",
     "<strong>不同函式庫的行為不一致</strong>",
   ]),
   "<strong>「不要自己寫 IP 解析器」是資安界的常見建議</strong> —— "
   "而這題的「禁止前導零」正是在避開那整個地雷區。",
 ],
 "related": [
   "<strong>第 468 題 Validate IP Address</strong> —— 驗證而不是生成",
   "<strong>第 131 題 Palindrome Partitioning</strong> —— 同樣是「切成若干段」的回溯",
   "<strong>第 139／140 題 Word Break</strong> —— 字串分割的另一類",
   "<strong>第 22／39／78 題</strong> —— 回溯家族",
 ],
 "check": [
   "三個合法條件是什麼？哪一個最容易漏？<code>\"010010\"</code> 的答案是什麼？",
   "終止條件為什麼需要同時檢查 <code>len(path) == 4</code> 和 <code>start == n</code>？",
   "三個 <code>break</code> 為什麼不能寫成 <code>continue</code>？",
   "長度剪枝的不等式是什麼？它為什麼是「最划算的剪枝」？",
 ],
})
print("P93 written")

# ==================== 94. Binary Tree Inorder Traversal ====================
S["p94_rec"] = '''class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)      # 左
            out.append(node.val)  # 根
            dfs(node.right)     # 右

        dfs(root)
        return out'''

S["p94_stack"] = '''class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        stack = []
        cur = root

        while cur or stack:
            # 一路往左走到底，沿途把節點壓進堆疊
            while cur:
                stack.append(cur)
                cur = cur.left
            # 彈出最深的左節點 -> 它就是下一個「根」
            cur = stack.pop()
            out.append(cur.val)
            # 轉向右子樹
            cur = cur.right

        return out'''

S["p94_morris"] = '''class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Morris 走訪：O(1) 空間，靠「暫時借用空的 right 指標」記路
        out = []
        cur = root

        while cur:
            if not cur.left:
                out.append(cur.val)     # 沒有左子樹 -> 直接輸出，往右
                cur = cur.right
            else:
                # 找左子樹的「最右節點」（中序的前驅）
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right

                if not pred.right:
                    pred.right = cur    # 建一條「回來的線」
                    cur = cur.left
                else:
                    pred.right = None   # 線已經用過了，拆掉還原
                    out.append(cur.val)
                    cur = cur.right

        return out'''

_p94 = [S.load(k) for k in ("p94_rec", "p94_stack", "p94_morris")]


def _build(vals):
    """用 LeetCode 的層序（含 None）格式建樹。"""
    if not vals or vals[0] is None:
        return None
    root = TreeNode(vals[0])
    q = [root]
    i = 1
    while q and i < len(vals):
        node = q.pop(0)
        if i < len(vals):
            v = vals[i]; i += 1
            if v is not None:
                node.left = TreeNode(v); q.append(node.left)
        if i < len(vals):
            v = vals[i]; i += 1
            if v is not None:
                node.right = TreeNode(v); q.append(node.right)
    return root


def _inorder_ref(node):
    return (_inorder_ref(node.left) + [node.val] + _inorder_ref(node.right)
            if node else [])


def _random_tree(n, lo=0):
    """隨機建一棵有 n 個節點的樹，回傳根節點。"""
    if n == 0:
        return None
    left_n = random.randint(0, n - 1)
    root = TreeNode(random.randint(0, 99))
    root.left = _random_tree(left_n)
    root.right = _random_tree(n - 1 - left_n)
    return root


for vals in [[1, None, 2, 3], [], [1], [1, 2], [1, None, 2],
             [3, 1, 4, None, 2], [1, 2, 3, 4, 5, 6, 7]]:
    root = _build(vals)
    e = _inorder_ref(root)
    for sol in _p94:
        r2 = _build(vals)
        assert sol.inorderTraversal(r2) == e, ("P94", vals, sol)
        # Morris 會暫時改樹，確認它有還原
        assert _inorder_ref(r2) == e, ("P94 樹被改壞了", vals, sol)
for _ in range(2000):
    n = random.randint(0, 9)
    root = _random_tree(n)
    e = _inorder_ref(root)
    for sol in _p94:
        assert sol.inorderTraversal(root) == e, ("P94", e, sol)
        assert _inorder_ref(root) == e, ("P94 樹被改壞了", sol)
print("P94 solutions OK")

_P94_FIG = '''            <text x="20" y="20" fill="var(--text-muted)" font-size="12">中序走訪：左 → 根 → 右。對二元搜尋樹來說，輸出剛好是遞增的。</text>
            <g font-size="14" text-anchor="middle">
              <circle cx="320" cy="60" r="20" fill="none" stroke="var(--gold)" stroke-width="2"/><text x="320" y="65" fill="var(--gold)">4</text>
              <circle cx="220" cy="126" r="20" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="220" y="131" fill="var(--accent)">2</text>
              <circle cx="420" cy="126" r="20" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="420" y="131" fill="#ff8a65">6</text>
              <circle cx="160" cy="192" r="20" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="160" y="197" fill="var(--accent)">1</text>
              <circle cx="280" cy="192" r="20" fill="none" stroke="var(--accent)" stroke-width="2"/><text x="280" y="197" fill="var(--accent)">3</text>
              <circle cx="360" cy="192" r="20" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="360" y="197" fill="#ff8a65">5</text>
              <circle cx="480" cy="192" r="20" fill="none" stroke="#ff8a65" stroke-width="2"/><text x="480" y="197" fill="#ff8a65">7</text>
            </g>
            <g stroke="var(--border)" stroke-width="1.5">
              <line x1="305" y1="74" x2="235" y2="112"/>
              <line x1="335" y1="74" x2="405" y2="112"/>
              <line x1="206" y1="140" x2="174" y2="178"/>
              <line x1="234" y1="140" x2="266" y2="178"/>
              <line x1="406" y1="140" x2="374" y2="178"/>
              <line x1="434" y1="140" x2="466" y2="178"/>
            </g>
            <text x="20" y="242" fill="var(--gold)" font-size="13">中序： 1, 2, 3, 4, 5, 6, 7　（遞增 ✔）</text>
            <text x="20" y="268" fill="var(--text-muted)" font-size="12">前序（根左右）： 4, 2, 1, 3, 6, 5, 7</text>
            <text x="20" y="292" fill="var(--text-muted)" font-size="12">後序（左右根）： 1, 3, 2, 5, 7, 6, 4</text>
            <line x1="20" y1="310" x2="620" y2="310" stroke="var(--border)"/>
            <text x="20" y="338" fill="var(--accent)" font-size="12">三種走訪的差別只在「輸出根節點的時機」——</text>
            <text x="20" y="362" fill="var(--text-muted)" font-size="12">前序：進入時輸出　中序：從左子樹回來時輸出　後序：從右子樹回來時輸出</text>'''

emit({
 "num": 94, "slug": "binary-tree-inorder-traversal",
 "en": [
   "Given the <code>root</code> of a binary tree, return <em>the inorder traversal of its "
   "nodes' values</em>.",
   "<strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?",
 ],
 "zh": [
   "給你一個二元樹的根節點 <code>root</code>，回傳它的<strong>中序走訪</strong>結果。",
   "<strong>中序</strong>的順序是：<strong>左子樹 → 根 → 右子樹</strong>。",
   "<strong>進階：</strong>遞迴版太簡單了，你能用<strong>迭代</strong>的方式做嗎？",
 ],
 "pre": [
   ("note", "三種走訪，差別只在「什麼時候輸出根」", [
     ("c", """前序（preorder）：  根 → 左 → 右
中序（inorder）：   左 → 根 → 右
後序（postorder）： 左 → 右 → 根

    def dfs(node):
        if not node: return
        # 【前序】在這裡輸出
        dfs(node.left)
        # 【中序】在這裡輸出
        dfs(node.right)
        # 【後序】在這裡輸出

三行遞迴呼叫的位置都一樣，
只有「輸出」那一行的位置不同。

為什麼中序特別重要？
    對【二元搜尋樹（BST）】做中序走訪，輸出剛好是【遞增】的。

    這個性質讓中序成為 BST 相關題目的核心工具：
        第 98 題  驗證 BST（檢查中序是不是遞增）
        第 99 題  復原 BST（找出中序裡「亂序」的那兩個）
        第 230 題 BST 裡第 k 小的元素（中序的第 k 個）
        第 173 題 BST 迭代器（就是中序走訪的迭代版）"""),
   ]),
 ],
 "examples": """範例 1
  輸入：root = [1,null,2,3]
        1
         \\
          2
         /
        3
  輸出：[1,3,2]

範例 2
  輸入：root = []
  輸出：[]

範例 3
  輸入：root = [1]
  輸出：[1]""",
 "constraints": [
   "樹的節點數在 <code>[0, 100]</code> 範圍內",
   "−100 ≤ <code>Node.val</code> ≤ 100",
   "<strong>進階：</strong>能不能用迭代（而非遞迴）？",
 ],
 "mid": [
   ("note", "先看懂限制在說什麼", [
     ("ul", [
       "<strong>樹可以是空的</strong> → 回傳 <code>[]</code>。",
       "<strong>節點數只有 100</strong>，所以遞迴深度不是問題。"
       "（但如果是 10⁵ 個節點的「一條鏈」，Python 會 RecursionError。）",
       "<strong>進階要求迭代</strong> —— 這才是這題真正的考點。"
       "遞迴版三行就寫完了。",
     ]),
   ]),
 ],
 "idea": [
   ("fig", _P94_FIG, "0 0 640 376"),
 ],
 "approaches": [
   ap("解法一", "遞迴（三行）", [
     ("c", S["p94_rec"]),
     "<strong>直接把定義翻成程式碼。</strong>"
     "「左、根、右」三行，順序就是答案。",
     "<strong>空間 O(h)</strong>（h 是樹高）—— 遞迴堆疊。"
     "平衡樹是 O(log n)，退化成一條鏈時是 O(n)。",
     "<strong>題目說「遞迴版太簡單」</strong>，所以面試時要準備迭代版。",
   ], "O(n)", "O(h)", "每個節點訪問一次", "遞迴堆疊"),

   ap("解法二", "堆疊迭代（進階要求的標準答案）", [
     ("c", S["p94_stack"]),
     ("h", "兩層迴圈在做什麼"),
     ("c", """外層 while cur or stack：
    只要「還有節點沒走」或「堆疊裡還有待處理的」就繼續

內層 while cur：
    一路往左走到底，沿途把經過的節點都壓進堆疊

    這模擬了遞迴版的 dfs(node.left) ——
    「先深入左邊，把沿路的節點記下來等下要回來」

彈出：
    cur = stack.pop()       最深的那個左節點
    out.append(cur.val)     輸出它（這就是「根」的時機）
    cur = cur.right         轉向右子樹

追一遍：
        4
       / \\
      2   6
     / \\
    1   3

  cur=4: 內層壓 4, 2, 1，cur=None
         pop 1 -> 輸出 1，cur = 1.right = None
  cur=None, stack=[4,2]:
         內層不跑
         pop 2 -> 輸出 2，cur = 2.right = 3
  cur=3:  內層壓 3，cur=None
         pop 3 -> 輸出 3，cur = None
  cur=None, stack=[4]:
         pop 4 -> 輸出 4，cur = 4.right = 6
  cur=6:  內層壓 6，cur=None
         pop 6 -> 輸出 6，cur = None
  stack 空，cur 空 -> 結束

  輸出 [1, 2, 3, 4, 6] ✔"""),
     ("h", "為什麼外層條件是 <code>cur or stack</code>（不是 <code>and</code>）？"),
     ("c", """兩種情況都還要繼續：

    cur 非空：還有一棵子樹要往左鑽
    stack 非空：還有節點等著被輸出

    只有「兩者都空」才真的結束。

寫成 and 的話：
    第一次 pop 之後如果 cur.right 是 None，
    cur 變成 None，迴圈就停了 —— 但 stack 裡還有東西 ✘

這個 or 是整個迭代版最容易寫錯的地方。"""),
     "<strong>這個「一路往左壓堆疊」的骨架，可以直接改成 BST 迭代器</strong>"
     "（第 173 題）—— 把它拆成 <code>next()</code> 和 <code>hasNext()</code> 兩個方法，"
     "就能「一次取一個」而不用一次算完。",
   ], "O(n)", "O(h)", "每個節點 push/pop 各一次", "堆疊", optimal=True),

   ap("解法三", "Morris 走訪（O(1) 空間）", [
     "堆疊版的空間是 O(h)。"
     "<strong>Morris 走訪把它降到 O(1)</strong> —— "
     "靠的是「暫時借用葉節點空著的 <code>right</code> 指標」來記住回來的路。",
     ("c", S["p94_morris"]),
     ("h", "核心想法：線索二元樹（threaded binary tree）"),
     ("c", """遞迴／堆疊為什麼需要 O(h) 空間？
    因為走進左子樹之後，需要記住「等下要回到哪個節點」。

Morris 的做法：
    【把「回去的路」寫在樹裡】

    對於節點 cur，它在中序裡的【前驅】是
        「左子樹的最右節點」（記作 pred）

    而 pred 的 right 指標一定是空的（它是最右節點）——
    所以我們可以暫時把 pred.right 指向 cur。

    這樣走完左子樹之後，自然就會沿著這條線回到 cur ✔

    回到 cur 之後，再把那條線拆掉（還原樹的結構）。

每個節點的處理：
    沒有左子樹 -> 直接輸出，往右走
    有左子樹：
        找 pred（左子樹的最右）
        pred.right 是 None -> 第一次來，建線，往左走
        pred.right 是 cur  -> 第二次來（從左子樹回來的），
                              拆線、輸出 cur、往右走"""),
     ("h", "為什麼是 O(n) 時間（而不是 O(n log n)）？"),
     ("c", """看起來每個節點都要「找左子樹的最右節點」，像是 O(h) 一次。

但實際上：
    每一條邊最多被走過【兩次】——
    一次是「找 pred」時往下走，
    一次是「沿著線回來」時。

    樹有 n-1 條邊 -> 總共 O(n) 步 ✔

這是又一個攤還分析的例子。"""),
     ("h", "代價與風險"),
     ("ul", [
       "<strong>會暫時修改樹的結構</strong> —— 走訪到一半時，樹裡有「假的」right 指標。"
       "<strong>如果在走訪過程中有另一個執行緒讀這棵樹，會看到錯誤的結構。</strong>",
       "<strong>如果中途拋出例外或提前 return，樹就壞了</strong>（線沒拆掉）。",
       "<strong>常數比堆疊版大</strong>（要反覆找 pred）。",
     ]),
     "<strong>實務上幾乎不用</strong>，但它是一個很漂亮的想法 —— "
     "<strong>「把狀態存在資料結構本身，而不是另開空間」</strong>，"
     "和第 41、73 題的「借用輸入」是同一個哲學。",
     "<strong>面試時提到它會加分</strong>，但要主動說明它的副作用。",
   ], "O(n)", "O(1)", "每條邊最多走兩次", "不用額外空間，但會暫時改樹"),
 ],
 "compare": (["解法", "時間", "空間", "會改樹？", "備註"],
   [["一、遞迴", "O(n)", "O(h)", "✘", "三行，但不符合進階"],
    ["二、堆疊", "O(n)", "O(h)", "✘", "進階的標準答案"],
    ["三、Morris", "O(n)", "O(1)", "✔ 暫時", "最省空間，但有副作用"]]),
 "edges": [
   "<strong>空樹</strong>：<code>[]</code> → <code>[]</code>。",
   "<strong>單一節點</strong>：<code>[1]</code> → <code>[1]</code>。",
   "<strong>只有左子樹（一條鏈）</strong>：遞迴深度 = n。"
   "n 很大時會 RecursionError。",
   "<strong>只有右子樹</strong>：<code>[1,null,2]</code> → <code>[1,2]</code>。"
   "堆疊版的內層 while 一次只壓一個。",
   "<strong>範例中的斜樹</strong>：<code>[1,null,2,3]</code> → <code>[1,3,2]</code>。"
   "<strong>注意 3 是 2 的左子節點，所以先輸出 3。</strong>",
   "<strong>完整二元樹</strong>：<code>[1,2,3,4,5,6,7]</code> → <code>[4,2,5,1,6,3,7]</code>。",
   "<strong>Morris 沒有拆線</strong>：樹會留下錯誤的 right 指標，"
   "第二次走訪會無限迴圈。<strong>測試時一定要檢查「走訪後樹有沒有還原」。</strong>",
 ],
 "follow": [
   ("h", "追問一：前序和後序的迭代版怎麼寫？"),
   ("c", """前序（根左右）—— 最簡單：
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            out.append(node.val)
            stack.append(node.right)    # 先壓右
            stack.append(node.left)     # 後壓左（先被彈出）

後序（左右根）—— 有一個取巧的做法：
    做「根右左」的前序走訪，然後把結果反轉
    （因為 reverse(根右左) = 左右根）

    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            out.append(node.val)
            stack.append(node.left)     # 順序反過來
            stack.append(node.right)
    return out[::-1]

真正的後序迭代（不反轉）比較麻煩 ——
需要記錄「這個節點的右子樹處理完了沒」。

三者的難度：前序 < 中序 < 後序。""",),
   ("h", "追問二：中序走訪在 BST 上的應用？"),
   ("c", """對 BST 做中序走訪，輸出是【遞增】的 ——
這是 BST 定義的直接推論。

    第 98 題  驗證 BST
              檢查中序輸出是不是嚴格遞增（或邊走邊比較前一個值）

    第 99 題  復原 BST（有兩個節點被交換了）
              中序輸出裡會有一或兩個「逆序對」，找出來交換回去

    第 230 題 BST 中第 k 小的元素
              中序走到第 k 個就 return（不用走完）

    第 173 題 BST 迭代器
              把堆疊版拆成 next() / hasNext()，
              做到「均攤 O(1) 的 next()、O(h) 空間」

    第 285 題 BST 中的中序後繼

「中序 = 排序」是 BST 最重要的性質。""",),
   ("h", "追問三：如果樹非常深（10⁵ 個節點的鏈）呢？"),
   "<strong>遞迴版會 RecursionError</strong>（Python 預設上限 1000）。"
   "<strong>堆疊版沒問題</strong>（用的是堆積記憶體，不是呼叫堆疊）。"
   "<strong>Morris 版也沒問題，而且空間 O(1)。</strong>",
   "<strong>這就是「迭代版」在實務上的真正價值</strong> —— "
   "不是為了快，而是為了<strong>不受呼叫堆疊深度的限制</strong>。",
   ("h", "追問四：Morris 走訪的名字從哪來？"),
   "J. H. Morris 在 1979 年提出。"
   "它建立在更早的<strong>「線索二元樹」（threaded binary tree，Perlis &amp; Thornton, 1960）</strong>概念上 —— "
   "那是一種「永久」把空指標拿來指向前驅／後繼的樹，"
   "讓走訪不需要堆疊。",
   "<strong>Morris 的貢獻是：不需要永久修改樹，可以邊走邊建、邊走邊拆。</strong>",
 ],
 "related": [
   "<strong>第 144／145 題</strong> —— 前序／後序走訪",
   "<strong>第 98 題 Validate BST</strong> —— 中序遞增的應用",
   "<strong>第 230 題 Kth Smallest in BST</strong> —— 中序走到第 k 個",
   "<strong>第 173 題 BST Iterator</strong> —— 堆疊版拆成迭代器",
   "<strong>第 99 題 Recover BST</strong> —— Morris 走訪的經典應用",
 ],
 "check": [
   "前序、中序、後序的程式碼差在哪一行？",
   "堆疊版的外層條件為什麼是 <code>cur or stack</code> 而不是 <code>and</code>？",
   "Morris 走訪怎麼「記住回來的路」？為什麼可以借用 <code>pred.right</code>？",
   "中序走訪在 BST 上有什麼特別的性質？列出三題用到它的題目。",
 ],
})
print("P94 written")
