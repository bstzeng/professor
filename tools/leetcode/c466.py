# -*- coding: utf-8 -*-
"""第 466、467、468、470、472、473 題。"""
import random
import itertools
import functools
from collections import Counter
from authoring import emit, ap
from runner import Src

S = Src()
random.seed(466)


# ==================== 466. Count The Repetitions ====================
S["p466"] = '''class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if any(c not in s1 for c in set(s2)):
            return 0
        # 一次掃過一整個 s1，看看 s2 能走多遠
        j = 0                      # 目前在 s2 中配對到的位置
        count = 0                  # 已經配對完幾個完整的 s2
        seen = {}                  # 「掃完第 k 個 s1 時 j 的值」-> (k, count)
        k = 0
        while k < n1:
            for ch in s1:
                if ch == s2[j]:
                    j += 1
                    if j == len(s2):
                        j = 0
                        count += 1
            k += 1
            if j in seen:          # ★ 同一個 j 又出現：從這裡開始會循環
                k0, c0 = seen[j]
                cycle_len, cycle_cnt = k - k0, count - c0
                cycles = (n1 - k) // cycle_len
                k += cycles * cycle_len          # 一次跳過很多個完整的循環
                count += cycles * cycle_cnt
                seen = {}                        # 剩下不到一個循環，直接模擬
            else:
                seen[j] = (k, count)
        return count // n2'''

S["p466_brute"] = '''class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        j = count = 0
        for _ in range(n1):                    # 直接掃 n1 次 s1
            for ch in s1:
                if ch == s2[j]:
                    j += 1
                    if j == len(s2):
                        j, count = 0, count + 1
        return count // n2'''

_p466 = [S.load(x) for x in ("p466", "p466_brute")]
for a, n1, b, n2, want in [("acb", 4, "ab", 2, 2), ("acb", 1, "acb", 1, 1), ("aaa", 3, "aa", 1, 4)]:
    for sol in _p466:
        assert sol.getMaxRepetitions(a, n1, b, n2) == want
for _ in range(3000):
    a = "".join(random.choice("abc") for _ in range(random.randrange(1, 6)))
    b = "".join(random.choice("abc") for _ in range(random.randrange(1, 6)))
    n1, n2 = random.randint(1, 60), random.randint(1, 5)
    x, y = (sol.getMaxRepetitions(a, n1, b, n2) for sol in _p466)
    assert x == y, (a, n1, b, n2)
assert _p466[0].getMaxRepetitions("abc" * 30, 10 ** 6, "cba", 7) > 0
print("P466 OK")

emit({
 "num": 466, "slug": "count-the-repetitions",
 "en": [
   "We define <code>str = [s, n]</code> as the string <code>str</code> which consists of the string <code>s</code> concatenated <code>n</code> times.",
   ("ul", ["For example, <code>str == [\"abc\", 3] ==\"abcabcabc\"</code>."]),
   "We define that string <code>s1</code> can be obtained from string <code>s2</code> if we can remove some characters from <code>s2</code> such that it becomes <code>s1</code>.",
   ("ul", ["For example, <code>s1 = \"abc\"</code> can be obtained from <code>s2 = \"ab<strong><u>dbe</u></strong>c\"</code> based on our definition by removing the bolded underlined characters."]),
   "You are given two strings <code>s1</code> and <code>s2</code> and two integers <code>n1</code> and <code>n2</code>. You have the two strings <code>str1 = [s1, n1]</code> and <code>str2 = [s2, n2]</code>.",
   "Return <em>the maximum integer</em> <code>m</code> <em>such that</em> <code>str = [str2, m]</code> <em>can be obtained from</em> <code>str1</code>.",
 ],
 "zh": [
   "定義 <code>[s, n]</code> 為字串 <code>s</code> 重複 <code>n</code> 次，例如 <code>[\"abc\", 3] = \"abcabcabc\"</code>。",
   "如果從 <code>s2</code> 刪掉一些字元能得到 <code>s1</code>（<code>s1</code> 是 <code>s2</code> 的子序列），就說 <code>s1</code> 可以從 <code>s2</code> 得到。",
   "給你 <code>s1</code>、<code>n1</code>、<code>s2</code>、<code>n2</code>，令 <code>str1 = [s1, n1]</code>、<code>str2 = [s2, n2]</code>。回傳最大的 <code>m</code>，使 <code>[str2, m]</code> 可以從 <code>str1</code> 得到。",
 ],
 "examples": """範例 1
  輸入：s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
  輸出：2
  說明：str1 = "acbacbacbacb" 裡可以找出 4 個 "ab"，也就是 2 個 str2。

範例 2
  輸入：s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
  輸出：1""",
 "constraints": [
   "1 ≤ <code>s1.length, s2.length</code> ≤ 100",
   "1 ≤ <code>n1, n2</code> ≤ 10⁶",
   "只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【先算：str1 裡能貪心配對出幾個 s2】
    答案 = 這個數量 // n2。
    子序列配對用貪心就好：掃過 str1，遇到 s2 的下一個字元就配對。

【直接模擬】
    str1 長度 = 100 × 10⁶ = 10⁸，Python 太慢。

【找循環】
    每掃完一整個 s1，記錄「目前在 s2 中配到第幾個字元」j。
    j 只有 len(s2) 種可能 ->
    最多掃 len(s2) + 1 個 s1 之後，一定會出現重複的 j。
    從上一次出現同一個 j 到現在，是一個「循環」：
        每 cycle_len 個 s1，就多配對出 cycle_cnt 個 s2。
    剩下的 s1 可以整批跳過，最後不到一個循環的部分再模擬。

【複雜度】
    模擬最多 O(len(s2)) 個 s1 -> O(|s1| × |s2|)，和 n1 無關。"""),
 ],
 "approaches": [
   ap("解法一", "直接模擬", [
     ("c", S["p466_brute"]),
   ], "O(|s1| · n1)", "O(1)", "n1 = 10⁶ 時太慢", ""),

   ap("解法二", "找循環後跳躍", [
     ("c", S["p466"]),
     "驗證方式：和直接模擬的版本比對三千組隨機輸入。",
   ], "O(|s1| · |s2|)", "O(|s2|)", "", "", optimal=True),
 ],
 "compare": (["解法", "時間", "備註"],
   [["一、模擬", "O(|s1|·n1)", "可能到 10⁸"],
    ["二、找循環", "O(|s1|·|s2|)", "和 n1 無關 ✔"]]),
 "edges": [
   "<strong>s2 有 s1 沒有的字元</strong> → 0。",
   "<strong>循環出現在很後面</strong> → 最多 |s2| + 1 個 s1 內一定出現。",
   "<strong>n1 很小</strong> → 還沒找到循環就結束，直接模擬即可。",
 ],
 "follow": [
   ("h", "「狀態有限 → 必有循環」"),
   ("c", "只要每一步的「狀態」只有有限種，而且下一步只由目前狀態決定，就一定會進入循環。第 957 題（N 天後的牢房）、第 1041 題（困於環中的機器人）都用這個性質。"),
 ],
 "related": [
   "<strong>第 392 題 判斷子序列</strong>",
   "<strong>第 957 題 N 天後的牢房</strong>",
 ],
 "check": [
   "為什麼答案是「str1 中能配對出幾個 s2」再除以 n2？",
   "為什麼一定會出現循環？循環的「狀態」是什麼？",
   "找到循環後怎麼跳過？",
 ],
})


# ==================== 467. Unique Substrings in Wraparound String ====================
S["p467"] = '''class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        longest = [0] * 26            # longest[c]：以字母 c 結尾的合格子字串，最長多長
        run = 0
        for i, ch in enumerate(s):
            if i and (ord(ch) - ord(s[i - 1])) % 26 == 1:   # 接續前一個字母（z 後面接 a）
                run += 1
            else:
                run = 1
            c = ord(ch) - 97
            longest[c] = max(longest[c], run)
        # ★ 以 c 結尾、長度 L 的合格子字串有 L 種（長度 1..L），而且彼此不同
        return sum(longest)'''

_p467 = S.load("p467")
_BASE = "abcdefghijklmnopqrstuvwxyz" * 4
for s, want in [("a", 1), ("cac", 2), ("zab", 6)]:
    assert _p467.findSubstringInWraproundString(s) == want
for _ in range(2000):
    s = "".join(random.choice("abcyz") for _ in range(random.randrange(1, 10)))
    subs = {s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)}
    want = sum(1 for t in subs if t in _BASE)
    assert _p467.findSubstringInWraproundString(s) == want, s
print("P467 OK")

emit({
 "num": 467, "slug": "unique-substrings-in-wraparound-string",
 "en": [
   "We define the string <code>base</code> to be the infinite wraparound string of <code>\"abcdefghijklmnopqrstuvwxyz\"</code>, so <code>base</code> will look like this:",
   ("ul", ["<code>\"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....\"</code>."]),
   "Given a string <code>s</code>, return <em>the number of <strong>unique non-empty substrings</strong> of</em> <code>s</code> <em>are present in</em> <code>base</code>.",
 ],
 "zh": [
   "<code>base</code> 是把 <code>\"abcdefghijklmnopqrstuvwxyz\"</code> 無限重複的字串（z 後面接 a）。",
   "給你字串 <code>s</code>，回傳 <code>s</code> 有幾個<strong>不同</strong>的非空子字串也出現在 <code>base</code> 裡。",
 ],
 "examples": """範例 1
  輸入：s = "a"
  輸出：1

範例 2
  輸入：s = "cac"
  輸出：2
  說明："a"、"c"

範例 3
  輸入：s = "zab"
  輸出：6
  說明："z"、"a"、"b"、"za"、"ab"、"zab\"""",
 "constraints": [
   "1 ≤ <code>s.length</code> ≤ 10⁵",
   "<code>s</code> 只包含小寫英文字母",
 ],
 "idea": [
   ("c", """【合格的子字串 = 字母連續遞增（z 接 a）】
    例如 "xyzab"。

【去重的關鍵觀察】
    合格的子字串由「結尾字母」和「長度」唯一決定：
    以 'b' 結尾、長度 3 的合格子字串一定是 "zab"。

    所以只要知道：以每個字母 c 結尾的合格子字串，最長有多長（longest[c]）。
    以 c 結尾、長度 1..longest[c] 的子字串都存在，而且互不相同 ->
    貢獻 longest[c] 個。

    答案 = Σ longest[c]

【計算 longest】
    掃過 s，run = 以目前字元結尾的連續遞增長度，
    和前一個字元連續就 +1，否則重設為 1。"""),
 ],
 "approaches": [
   ap("解法", "以每個字母結尾的最長長度", [
     ("c", S["p467"]),
   ], "O(n)", "O(1)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>z 接 a</strong> → 用 (差值) % 26 == 1 判斷。",
   "<strong>重複的片段</strong>（\"abcabc\"）→ 取最長，避免重複計算。",
 ],
 "follow": [
   ("h", "「用某個特徵唯一決定」來去重"),
   ("c", "去重時如果能找到一個簡單的「身分證」（這裡是結尾字母 + 長度），就不用真的把字串存進集合。"),
 ],
 "related": [
   "<strong>第 413 題 等差數列劃分</strong> —— 以 i 結尾的連續段",
   "<strong>第 1180 題 統計只含單一字母的子字串</strong>（付費）",
 ],
 "check": [
   "為什麼合格的子字串可以由「結尾字母 + 長度」唯一決定？",
   "longest[c] 的意義是什麼？為什麼答案是它們的總和？",
 ],
})


# ==================== 468. Validate IP Address ====================
S["p468"] = '''class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def ipv4(part: str) -> bool:
            # 1～3 位數字、不能有前導零、值 <= 255
            return (part.isdigit() and part.isascii() and 1 <= len(part) <= 3
                    and (part == "0" or part[0] != "0") and int(part) <= 255)

        def ipv6(part: str) -> bool:
            # 1～4 位十六進位數字（大小寫都可以，前導零可以）
            return 1 <= len(part) <= 4 and all(c in "0123456789abcdefABCDEF" for c in part)

        if queryIP.count(".") == 3 and all(ipv4(p) for p in queryIP.split(".")):
            return "IPv4"
        if queryIP.count(":") == 7 and all(ipv6(p) for p in queryIP.split(":")):
            return "IPv6"
        return "Neither"'''

_p468 = S.load("p468")
import ipaddress as _ip


def _ip_ref(q):
    parts4 = q.split(".")
    if len(parts4) == 4 and all(p.isdigit() and p.isascii() and len(p) <= 3 and (p == "0" or p[0] != "0") and int(p) <= 255 for p in parts4):
        return "IPv4"
    parts6 = q.split(":")
    if len(parts6) == 8 and all(1 <= len(p) <= 4 and all(c in "0123456789abcdefABCDEF" for c in p) for p in parts6):
        return "IPv6"
    return "Neither"


for q, want in [("172.16.254.1", "IPv4"), ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"), ("256.256.256.256", "Neither"),
                ("01.01.01.01", "Neither"), ("1.1.1.", "Neither"), ("2001:0db8:85a3::8A2E:037j:7334", "Neither"),
                ("1e1.4.5.6", "Neither"), ("0.0.0.0", "IPv4"), ("12..33.4", "Neither"), ("02001:0db8:85a3:0000:0000:8a2e:0370:7334", "Neither")]:
    assert _p468.validIPAddress(q) == want, q
for _ in range(5000):
    if random.random() < 0.5:
        q = ".".join(random.choice(["0", "1", "01", "255", "256", "99", "", "a", "300", "1234"]) for _ in range(random.choice([3, 4, 4, 5])))
    else:
        q = ":".join(random.choice(["0", "0db8", "FFFF", "", "g1", "12345", "aB", "0000"]) for _ in range(random.choice([7, 8, 8, 9])))
    assert _p468.validIPAddress(q) == _ip_ref(q), q
    if _p468.validIPAddress(q) == "IPv4":
        _ip.IPv4Address(q)          # 標準函式庫也認得
print("P468 OK")

emit({
 "num": 468, "slug": "validate-ip-address",
 "en": [
   "Given a string <code>queryIP</code>, return <code>\"IPv4\"</code> if IP is a valid IPv4 address, <code>\"IPv6\"</code> if IP is a valid IPv6 address or <code>\"Neither\"</code> if IP is not a correct IP of any type.",
   "<strong>A valid IPv4</strong> address is an IP in the form <code>\"x<sub>1</sub>.x<sub>2</sub>.x<sub>3</sub>.x<sub>4</sub>\"</code> where <code>0 &lt;= x<sub>i</sub> &lt;= 255</code> and <code>x<sub>i</sub></code> <strong>cannot contain</strong> leading zeros. For example, <code>\"192.168.1.1\"</code> and <code>\"192.168.1.0\"</code> are valid IPv4 addresses while <code>\"192.168.01.1\"</code>, <code>\"192.168.1.00\"</code>, and <code>\"192.168@1.1\"</code> are invalid IPv4 addresses.",
   "<strong>A valid IPv6</strong> address is an IP in the form <code>\"x<sub>1</sub>:x<sub>2</sub>:x<sub>3</sub>:x<sub>4</sub>:x<sub>5</sub>:x<sub>6</sub>:x<sub>7</sub>:x<sub>8</sub>\"</code> where:",
   ("ul", ["<code>1 &lt;= x<sub>i</sub>.length &lt;= 4</code>",
           "<code>x<sub>i</sub></code> is a <strong>hexadecimal string</strong> which may contain digits, lowercase English letter (<code>'a'</code> to <code>'f'</code>) and upper-case English letters (<code>'A'</code> to <code>'F'</code>).",
           "Leading zeros are allowed in <code>x<sub>i</sub></code>."]),
   "For example, \"<code>2001:0db8:85a3:0000:0000:8a2e:0370:7334</code>\" and \"<code>2001:db8:85a3:0:0:8A2E:0370:7334</code>\" are valid IPv6 addresses, while \"<code>2001:0db8:85a3::8A2E:037j:7334</code>\" and \"<code>02001:0db8:85a3:0000:0000:8a2e:0370:7334</code>\" are invalid IPv6 addresses.",
 ],
 "zh": [
   "給你一個字串 <code>queryIP</code>，判斷它是合法的 IPv4、合法的 IPv6，還是都不是（回傳 <code>\"IPv4\"</code>、<code>\"IPv6\"</code> 或 <code>\"Neither\"</code>）。",
   "<strong>IPv4</strong>：<code>x1.x2.x3.x4</code>，每段是 0–255 的十進位數，<strong>不能有前導零</strong>（<code>\"01\"</code> 不行，<code>\"0\"</code> 可以）。",
   "<strong>IPv6</strong>：<code>x1:x2:…:x8</code>，每段是 1–4 位的十六進位數字（大小寫皆可），<strong>可以有前導零</strong>。不支援 <code>::</code> 縮寫。",
 ],
 "examples": """範例 1
  輸入：queryIP = "172.16.254.1"
  輸出："IPv4"

範例 2
  輸入：queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
  輸出："IPv6"

範例 3
  輸入：queryIP = "256.256.256.256"
  輸出："Neither\"""",
 "constraints": [
   "<code>queryIP</code> 只包含英文字母、數字、<code>'.'</code>、<code>':'</code>",
 ],
 "idea": [
   ("c", """【純粹的規則檢查，重點是不漏條件】

【IPv4】
    剛好 4 段（剛好 3 個點）
    每段：
        1 到 3 個字元，全部是數字
        沒有前導零（"0" 本身可以）
        值 <= 255

【IPv6】
    剛好 8 段（剛好 7 個冒號）
    每段：1 到 4 個字元，每個都是 0-9、a-f、A-F

【常見漏洞】
    "1.1.1."    -> split 會得到空字串 ""，要檢查長度 >= 1
    "1e1.1.1.1" -> int("1e1") 會出錯，要先檢查全是數字
    Python 的 isdigit() 對某些 Unicode 數字（例如 "²"）也回傳 True，
    加上 isascii() 更保險。"""),
   ("t", ["輸入", "結果", "原因"],
    [["192.168.1.1", "IPv4", ""],
     ["192.168.01.1", "Neither", "前導零"],
     ["256.1.1.1", "Neither", "超過 255"],
     ["1.1.1.", "Neither", "最後一段是空的"],
     ["2001:db8:85a3:0:0:8A2E:370:7334", "IPv6", "可以省略前導零、大小寫混用"],
     ["2001:db8::7334", "Neither", "不支援 ::"]]),
 ],
 "approaches": [
   ap("解法", "逐段檢查", [
     ("c", S["p468"]),
   ], "O(n)", "O(n)", "", "", optimal=True),
 ],
 "edges": [
   "<strong>空段</strong>（連續的點或結尾有點）→ Neither。",
   "<strong>前導零</strong> → IPv4 不行、IPv6 可以。",
   "<strong>段數不對</strong> → Neither。",
   "<strong>非十六進位字元</strong>（g、j）→ Neither。",
 ],
 "follow": [
   ("h", "實務上"),
   ("c", "不要自己寫——用 Python 的 <code>ipaddress</code> 模組。但注意它接受 IPv6 的 <code>::</code> 縮寫，和本題的規則不同。"),
 ],
 "related": [
   "<strong>第 93 題 復原 IP 位址</strong>",
   "<strong>第 65 題 有效數字</strong> —— 另一題規則檢查",
 ],
 "check": [
   "IPv4 每一段要檢查哪些條件？",
   "IPv4 和 IPv6 對前導零的規定有什麼不同？",
   "\"1.1.1.\" 為什麼容易被誤判？",
 ],
})


# ==================== 470. Implement Rand10() Using Rand7() ====================
S["p470"] = '''# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self) -> int:
        while True:
            # ★ 兩次 rand7 組成 1..49 的均勻分布
            x = (rand7() - 1) * 7 + rand7()
            if x <= 40:                    # 只接受前 40 個（10 的倍數），其餘重來
                return (x - 1) % 10 + 1'''

_calls = [0]


def _rand7():
    _calls[0] += 1
    return random.randint(1, 7)


_s = S.load("p470", extra={"rand7": _rand7})
N = 200000
cnt = Counter(_s.rand10() for _ in range(N))
assert set(cnt) == set(range(1, 11)) and all(abs(c - N / 10) < N / 10 * 0.05 for c in cnt.values()), cnt
assert 2.3 < _calls[0] / N < 2.6            # 期望呼叫次數 = 2 × 49/40 ≈ 2.45
print("P470 OK")

emit({
 "num": 470, "slug": "implement-rand10-using-rand7",
 "en": [
   "Given the <strong>API</strong> <code>rand7()</code> that generates a uniform random integer in the range <code>[1, 7]</code>, write a function <code>rand10()</code> that generates a uniform random integer in the range <code>[1, 10]</code>. You can only call the API <code>rand7()</code>, and you shouldn't call any other API. Please <strong>do not</strong> use a language's built-in random API.",
   "<strong>Follow up:</strong>",
   ("ul", ["What is the <a href=\"https://en.wikipedia.org/wiki/Expected_value\">expected value</a> for the number of calls to <code>rand7()</code> function?",
           "Could you minimize the number of calls to <code>rand7()</code>?"]),
 ],
 "zh": [
   "給你一個 API <code>rand7()</code>，會均勻產生 <code>[1, 7]</code> 的整數。只用它寫出 <code>rand10()</code>，均勻產生 <code>[1, 10]</code> 的整數。",
   "<strong>進階：</strong>呼叫 <code>rand7()</code> 的期望次數是多少？能再減少嗎？",
 ],
 "examples": """範例
  輸入：n = 3（呼叫 rand10 三次）
  輸出：例如 [3,8,10]""",
 "constraints": [
   "1 ≤ <code>n</code> ≤ 10⁵",
 ],
 "idea": [
   ("c", """【一次 rand7 只有 7 種結果，不夠 10 種】
    (rand7() + rand7()) 不均勻（和的分布是三角形）✘

【兩次 rand7 組成一個「二位數」】
    x = (rand7() - 1) × 7 + rand7()
    第一次決定「十位」（0..6），第二次決定「個位」（1..7）
    -> x 均勻分布在 1..49，每個機率 1/49 ✔

【拒絕抽樣（rejection sampling）】
    49 不是 10 的倍數。
    只接受 1..40（每個數字對應 4 個 x），41..49 就重來。
    被接受時，1..40 仍然是均勻的 -> (x - 1) % 10 + 1 均勻落在 1..10。

【期望呼叫次數】
    每一輪呼叫 2 次，被接受的機率 40/49。
    期望輪數 = 49/40 -> 期望呼叫 2 × 49/40 ≈ 2.45 次。

【進一步優化】
    被拒絕的 41..49 還有 9 種均勻的結果，
    可以再乘上一次 rand7 變成 1..63，取前 60 個……
    把「剩下的隨機性」回收利用，期望次數可以降到約 2.2。"""),
 ],
 "approaches": [
   ap("解法", "組合成 1..49 + 拒絕抽樣", [
     ("c", S["p470"]),
     "驗證方式：二十萬次抽樣，每個數字的次數都在期望值 ±5% 以內，平均呼叫 rand7 約 2.45 次。",
   ], "期望 O(1)", "O(1)", "期望呼叫 rand7 約 2.45 次", "", optimal=True),
 ],
 "edges": [
   "<strong>不能用加法</strong> → 兩個均勻變數的和不均勻。",
   "<strong>拒絕的範圍</strong> → 一定要是完整的「10 的倍數」才接受。",
 ],
 "follow": [
   ("h", "拒絕抽樣的其他應用"),
   ("c", "在圓內均勻取點（第 478 題）：在外接正方形均勻取點，落在圓外就重來，接受率 π/4。"),
 ],
 "related": [
   "<strong>第 478 題 在圓內隨機生成點</strong>",
   "<strong>第 384 題 打亂陣列</strong>",
 ],
 "check": [
   "為什麼 rand7() + rand7() 不均勻？",
   "(rand7() − 1) × 7 + rand7() 為什麼是均勻的？",
   "為什麼要拒絕 41 到 49？期望呼叫次數是多少？",
 ],
})


# ==================== 472. Concatenated Words ====================
S["p472"] = '''class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)

        def can_form(w: str) -> bool:
            n = len(w)
            # dp[i]：w[:i] 能不能由字典中的單字組成（至少一個）
            dp = [True] + [False] * n
            for i in range(1, n + 1):
                for j in range(i):
                    # ★ j == 0 且 i == n 代表整個 w 本身，不算（要兩個以上的單字）
                    if dp[j] and (j, i) != (0, n) and w[j:i] in words_set:
                        dp[i] = True
                        break
            return dp[n]

        return [w for w in words if w and can_form(w)]'''

_p472 = S.load("p472")


def _cw_ref(words):
    ws = set(words)
    res = []
    for w in words:
        if not w:
            continue

        @functools.lru_cache(None)
        def f(i, parts):
            if i == len(w):
                return parts >= 2
            return any(w[i:j] in ws and f(j, min(parts + 1, 2)) for j in range(i + 1, len(w) + 1))
        if f(0, 0):
            res.append(w)
    return res


for words, want in [(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"], ["catsdogcats", "dogcatsdog", "ratcatdogcat"]),
                    (["cat", "dog", "catdog"], ["catdog"])]:
    assert sorted(_p472.findAllConcatenatedWordsInADict(words)) == sorted(want)
for _ in range(800):
    base = ["".join(random.choice("ab") for _ in range(random.randint(1, 3))) for _ in range(4)]
    words = list(set(base + ["".join(random.choice(base) for _ in range(random.randint(1, 3))) for _ in range(5)]))
    assert sorted(_p472.findAllConcatenatedWordsInADict(words)) == sorted(_cw_ref(words)), words
print("P472 OK")

emit({
 "num": 472, "slug": "concatenated-words",
 "en": [
   "Given an array of strings <code>words</code> (<strong>without duplicates</strong>), return <em>all the <strong>concatenated words</strong> in the given list of</em> <code>words</code>.",
   "A <strong>concatenated word</strong> is defined as a string that is comprised entirely of at least two shorter words (not necessarily distinct) in the given array.",
 ],
 "zh": [
   "給你一個<strong>沒有重複</strong>的字串陣列 <code>words</code>，回傳其中所有的<strong>連接詞</strong>。",
   "<strong>連接詞</strong>：完全由陣列中<strong>至少兩個</strong>（可以相同的）更短的單字串接而成的字串。",
 ],
 "examples": """範例 1
  輸入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
  輸出：["catsdogcats","dogcatsdog","ratcatdogcat"]

範例 2
  輸入：words = ["cat","dog","catdog"]
  輸出：["catdog"]""",
 "constraints": [
   "1 ≤ <code>words.length</code> ≤ 10⁴",
   "1 ≤ <code>words[i].length</code> ≤ 30",
   "所有字串互不相同，總長度不超過 10⁵",
 ],
 "idea": [
   ("c", """【對每個單字做一次「單字拆分」（第 139 題）】
    dp[i] = w 的前 i 個字元能不能由字典中的單字拼成。
    dp[i] = 存在 j < i，dp[j] 為真而且 w[j:i] 在字典裡。

【至少兩個單字】
    字典裡本來就有 w 自己 ->
    必須排除「整個 w 就是一個單字」的那種拆法（j = 0 且 i = n）。

【另一種寫法：依長度排序】
    由短到長處理，只用「比自己短、已經處理過的」單字當字典，
    自然排除了 w 自己。"""),
 ],
 "approaches": [
   ap("解法", "每個單字做單字拆分 DP", [
     ("c", S["p472"]),
   ], "O(Σ L³)", "O(N · L)", "L ≤ 30，每次切片 O(L)", "", optimal=True),
 ],
 "edges": [
   "<strong>空字串</strong>（有些版本會出現）→ 不算連接詞，而且不能當拼接材料造成誤判。",
   "<strong>同一個單字用多次</strong>（\"catcat\"）→ 可以。",
   "<strong>只由自己組成</strong> → 不算。",
 ],
 "follow": [
   ("h", "Trie 優化"),
   ("c", "把所有單字放進 Trie，DP 時從位置 j 沿 Trie 往下走，一次找出所有「從 j 開始的字典單字」，省掉切片和雜湊的成本。"),
 ],
 "related": [
   "<strong>第 139 題 單字拆分</strong>",
   "<strong>第 140 題 單字拆分 II</strong>",
 ],
 "check": [
   "dp[i] 的意義是什麼？",
   "怎麼確保至少用了兩個單字？",
 ],
})


# ==================== 473. Matchsticks to Square ====================
S["p473"] = '''class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4:
            return False
        side = total // 4
        sticks = sorted(matchsticks, reverse=True)     # ★ 長的先放：更早發現放不下
        if sticks[0] > side:
            return False
        edges = [0] * 4

        def dfs(i: int) -> bool:
            if i == len(sticks):
                return True                            # 總和剛好，前三邊滿了第四邊一定也滿
            for k in range(4):
                if edges[k] + sticks[i] <= side:
                    edges[k] += sticks[i]
                    if dfs(i + 1):
                        return True
                    edges[k] -= sticks[i]
                if edges[k] == 0:                      # 剪枝：放進空的邊都失敗，放別的空邊也一樣
                    break
            return False

        return dfs(0)'''

_p473 = S.load("p473")


def _sq_ref(a):
    s = sum(a)
    if s % 4:
        return False
    side = s // 4
    for assign in itertools.product(range(4), repeat=len(a)):
        e = [0] * 4
        for x, k in zip(a, assign):
            e[k] += x
        if e == [side] * 4:
            return True
    return False


for a, want in [([1, 1, 2, 2, 2], True), ([3, 3, 3, 3, 4], False)]:
    assert _p473.makesquare(a) == want
for _ in range(400):
    a = [random.randint(1, 6) for _ in range(random.randrange(1, 8))]
    assert _p473.makesquare(a) == _sq_ref(a), a
print("P473 OK")

emit({
 "num": 473, "slug": "matchsticks-to-square",
 "en": [
   "You are given an integer array <code>matchsticks</code> where <code>matchsticks[i]</code> is the length of the <code>i<sup>th</sup></code> matchstick. You want to use <strong>all the matchsticks</strong> to make one square. You <strong>should not break</strong> any stick, but you can link them up, and each matchstick must be used <strong>exactly one time</strong>.",
   "Return <code>true</code> if you can make this square and <code>false</code> otherwise.",
 ],
 "zh": [
   "給你一組火柴棒的長度 <code>matchsticks</code>，要用<strong>所有</strong>火柴棒拼成一個正方形。不能折斷，但可以首尾相接，每根火柴都要<strong>恰好用一次</strong>。",
   "判斷能不能拼成。",
 ],
 "examples": """範例 1
  輸入：matchsticks = [1,1,2,2,2]
  輸出：true
  說明：邊長 2：[2]、[2]、[2]、[1,1]

範例 2
  輸入：matchsticks = [3,3,3,3,4]
  輸出：false""",
 "constraints": [
   "1 ≤ <code>matchsticks.length</code> ≤ 15",
   "1 ≤ <code>matchsticks[i]</code> ≤ 10⁸",
 ],
 "idea": [
   ("c", """【把火柴分成四組，每組和 = 總和 / 4】
    這是第 698 題「劃分為 k 個相等的子集」k = 4 的特例。

【回溯：每根火柴放進四條邊之一】
    最多 4¹⁵ ≈ 10⁹ 種，需要剪枝：
    1. 總和不是 4 的倍數 -> false
    2. 最長的火柴比邊長還長 -> false
    3. 由長到短放：長的火柴選擇少，越早失敗越好
    4. 放進某條邊之後邊長超過 -> 不用試
    5. 對稱剪枝：如果放進一條「空的」邊失敗了，
       放進其他空的邊也一定失敗（四條空邊是等價的）-> 直接停

【位元遮罩 DP】
    另一種做法：dp[mask] = 用了 mask 這些火柴後，目前這條邊的長度（mod side）。
    O(2ⁿ · n)。"""),
 ],
 "approaches": [
   ap("解法", "排序 + 回溯 + 剪枝", [
     ("c", S["p473"]),
     "驗證方式：和窮舉 4ⁿ 種分配的暴力版本比對四百組。",
   ], "最壞 O(4ⁿ)", "O(n)", "剪枝後實際很快", "", optimal=True),
 ],
 "edges": [
   "<strong>少於 4 根</strong> → 一定拼不成（每條邊至少要一根火柴）。",
   "<strong>總和不是 4 的倍數</strong> → false。",
   "<strong>有一根特別長</strong> → false。",
 ],
 "follow": [
   ("h", "k 個子集"),
   ("c", "第 698 題把 4 換成 k；第 2305 題（公平分發餅乾）是「讓最大的一組最小」的版本。"),
 ],
 "related": [
   "<strong>第 698 題 劃分為 k 個相等的子集</strong>",
   "<strong>第 416 題 分割等和子集</strong>",
   "<strong>第 2305 題 公平分發餅乾</strong>",
 ],
 "check": [
   "有哪些提前判斷可以直接回傳 false？",
   "為什麼要由長到短放？",
   "「空邊剪枝」為什麼成立？",
 ],
})
