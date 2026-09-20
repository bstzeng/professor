# -*- coding: utf-8 -*-
"""第 4–9 題所有解法的正確性測試（含隨機壓力測試）。"""
import random, bisect

# ---------------- 4. Median of Two Sorted Arrays ----------------
def med_merge(a, b):
    m = sorted(a + b); n = len(m)
    return m[n // 2] if n % 2 else (m[n // 2 - 1] + m[n // 2]) / 2

def med_partition(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    half = (m + n + 1) // 2
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        l1 = nums1[i - 1] if i > 0 else float("-inf")
        r1 = nums1[i] if i < m else float("inf")
        l2 = nums2[j - 1] if j > 0 else float("-inf")
        r2 = nums2[j] if j < n else float("inf")
        if l1 <= r2 and l2 <= r1:
            if (m + n) % 2:
                return float(max(l1, l2))
            return (max(l1, l2) + min(r1, r2)) / 2
        if l1 > r2:
            hi = i - 1
        else:
            lo = i + 1
    raise ValueError

def med_kth(nums1, nums2):
    def kth(a, i, b, j, k):
        if i >= len(a): return b[j + k - 1]
        if j >= len(b): return a[i + k - 1]
        if k == 1: return min(a[i], b[j])
        half = k // 2
        va = a[i + half - 1] if i + half - 1 < len(a) else float("inf")
        vb = b[j + half - 1] if j + half - 1 < len(b) else float("inf")
        if va <= vb:
            return kth(a, i + half, b, j, k - half)
        return kth(a, i, b, j + half, k - half)
    t = len(nums1) + len(nums2)
    if t % 2:
        return float(kth(nums1, 0, nums2, 0, t // 2 + 1))
    return (kth(nums1, 0, nums2, 0, t // 2) + kth(nums1, 0, nums2, 0, t // 2 + 1)) / 2

# ---------------- 5. Longest Palindromic Substring ----------------
def lps_brute(s):
    best = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub
    return best

def lps_dp(s):
    n = len(s)
    if n < 2: return s
    dp = [[False] * n for _ in range(n)]
    start, length = 0, 1
    for i in range(n): dp[i][i] = True
    for ln in range(2, n + 1):
        for i in range(n - ln + 1):
            j = i + ln - 1
            if s[i] != s[j]: continue
            if ln == 2 or dp[i + 1][j - 1]:
                dp[i][j] = True
                if ln > length: start, length = i, ln
    return s[start:start + length]

def lps_center(s):
    if not s: return ""
    start, end = 0, 0
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return l + 1, r - 1
    for i in range(len(s)):
        for l, r in (expand(i, i), expand(i, i + 1)):
            if r - l > end - start:
                start, end = l, r
    return s[start:end + 1]

def lps_manacher(s):
    if not s: return ""
    t = "#" + "#".join(s) + "#"
    n = len(t)
    pal = [0] * n
    center = right = 0
    for i in range(n):
        if i < right:
            pal[i] = min(right - i, pal[2 * center - i])
        while (i - pal[i] - 1 >= 0 and i + pal[i] + 1 < n
               and t[i - pal[i] - 1] == t[i + pal[i] + 1]):
            pal[i] += 1
        if i + pal[i] > right:
            center, right = i, i + pal[i]
    k = max(range(n), key=lambda i: pal[i])
    length = pal[k]
    start = (k - length) // 2
    return s[start:start + length]

# ---------------- 6. Zigzag Conversion ----------------
def zig_sim(s, numRows):
    if numRows == 1: return s
    rows = [[] for _ in range(numRows)]
    r, step = 0, 1
    for ch in s:
        rows[r].append(ch)
        if r == 0: step = 1
        elif r == numRows - 1: step = -1
        r += step
    return "".join("".join(x) for x in rows)

def zig_formula(s, numRows):
    if numRows == 1: return s
    n = len(s); cycle = 2 * numRows - 2
    out = []
    for r in range(numRows):
        for base in range(r, n, cycle):
            out.append(s[base])
            second = base + cycle - 2 * r
            if r != 0 and r != numRows - 1 and second < n:
                out.append(s[second])
    return "".join(out)

# ---------------- 7. Reverse Integer ----------------
INT_MIN, INT_MAX = -2**31, 2**31 - 1

def rev_str(x):
    sign = -1 if x < 0 else 1
    r = sign * int(str(abs(x))[::-1])
    return 0 if r < INT_MIN or r > INT_MAX else r

def rev_digit(x):
    sign = -1 if x < 0 else 1
    x = abs(x); r = 0
    while x:
        d = x % 10; x //= 10
        # 模擬 32 位元語言的「事前檢查」
        if r > (INT_MAX - d) // 10:
            return 0
        r = r * 10 + d
    r *= sign
    return 0 if r < INT_MIN or r > INT_MAX else r

# ---------------- 8. String to Integer (atoi) ----------------
def atoi_step(s):
    i, n = 0, len(s)
    while i < n and s[i] == " ": i += 1
    if i == n: return 0
    sign = 1
    if s[i] in "+-":
        if s[i] == "-": sign = -1
        i += 1
    num = 0
    while i < n and s[i].isdigit():
        num = num * 10 + int(s[i]); i += 1
        if sign == 1 and num > INT_MAX: return INT_MAX
        if sign == -1 and -num < INT_MIN: return INT_MIN
    return sign * num

def atoi_ref(s):
    import re
    m = re.match(r"\s*([+-]?\d+)", s)
    if not m: return 0
    v = int(m.group(1))
    return max(INT_MIN, min(INT_MAX, v))

# ---------------- 9. Palindrome Number ----------------
def pal_str(x):
    return str(x) == str(x)[::-1]

def pal_half(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    rev = 0
    while x > rev:
        rev = rev * 10 + x % 10
        x //= 10
    return x == rev or x == rev // 10

# ================= 測試 =================
random.seed(2024)

# P4
cases4 = [([1,3],[2]), ([1,2],[3,4]), ([],[1]), ([2],[]), ([0,0],[0,0]), ([1,1,1],[1,1])]
for a, b in cases4:
    e = med_merge(a, b)
    assert abs(med_partition(a,b) - e) < 1e-9, ("P4 partition", a, b)
    assert abs(med_kth(a,b) - e) < 1e-9, ("P4 kth", a, b)
for _ in range(4000):
    la, lb = random.randint(0,7), random.randint(0,7)
    if la + lb == 0: continue
    a = sorted(random.randint(-15,15) for _ in range(la))
    b = sorted(random.randint(-15,15) for _ in range(lb))
    e = med_merge(a,b)
    assert abs(med_partition(a,b)-e) < 1e-9, ("P4 partition", a, b, med_partition(a,b), e)
    assert abs(med_kth(a,b)-e) < 1e-9, ("P4 kth", a, b)
print("P4 OK")

# P5
for s in ["babad","cbbd","","a","ac","aaaa","forgeeksskeegfor","abacdfgdcaba"]:
    e = lps_brute(s)
    for f in (lps_dp, lps_center, lps_manacher):
        g = f(s)
        assert len(g) == len(e) and g == g[::-1] and g in s, (f.__name__, s, g, e)
for _ in range(2000):
    s = "".join(random.choice("abc") for _ in range(random.randint(0,12)))
    e = lps_brute(s)
    for f in (lps_dp, lps_center, lps_manacher):
        g = f(s)
        assert len(g) == len(e) and g == g[::-1] and g in s, (f.__name__, s, g, e)
print("P5 OK")

# P6
for s, r in [("PAYPALISHIRING",3), ("PAYPALISHIRING",4), ("A",1), ("AB",1), ("ABC",5)]:
    assert zig_sim(s,r) == zig_formula(s,r), (s,r,zig_sim(s,r),zig_formula(s,r))
for _ in range(3000):
    s = "".join(random.choice("ABCDEFG") for _ in range(random.randint(1,20)))
    r = random.randint(1,6)
    assert zig_sim(s,r) == zig_formula(s,r), (s,r)
print("P6 OK")

# P7
for x in [123,-123,120,0,1534236469,-2147483648,2147483647,1463847412,-1463847412]:
    assert rev_str(x) == rev_digit(x), (x, rev_str(x), rev_digit(x))
for _ in range(5000):
    x = random.randint(INT_MIN, INT_MAX)
    assert rev_str(x) == rev_digit(x), (x, rev_str(x), rev_digit(x))
print("P7 OK")

# P8
for s in ["42","   -42","4193 with words","words and 987","-91283472332",
          "+1","+-12","  +0 123","00000-42a1234","   ","-2147483649","2147483648",".1","3.14"]:
    assert atoi_step(s) == atoi_ref(s), (s, atoi_step(s), atoi_ref(s))
alpha = " +-0123456789abc."
for _ in range(5000):
    s = "".join(random.choice(alpha) for _ in range(random.randint(0,10)))
    assert atoi_step(s) == atoi_ref(s), (repr(s), atoi_step(s), atoi_ref(s))
print("P8 OK")

# P9
for x in [121,-121,10,0,1,11,1221,12321,100,1000021]:
    assert pal_str(x) == pal_half(x), (x, pal_str(x), pal_half(x))
for _ in range(5000):
    x = random.randint(-100000, 100000)
    assert pal_str(x) == pal_half(x), (x, pal_str(x), pal_half(x))
print("P9 OK")
print("=== batch 4-9 all pass ===")
