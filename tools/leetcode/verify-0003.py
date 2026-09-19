# -*- coding: utf-8 -*-
import random, string

class S1:  # brute force O(n^3)
    def lengthOfLongestSubstring(self, s: str) -> int:
        def ok(sub):
            return len(set(sub)) == len(sub)
        n = len(s); best = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                if ok(s[i:j]):
                    best = max(best, j - i)
        return best

class S2:  # O(n^2) with set, early break
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s); best = 0
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
            best = max(best, len(seen))
        return best

class S3:  # sliding window with set
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0; best = 0
        for right, ch in enumerate(s):
            while ch in window:
                window.remove(s[left]); left += 1
            window.add(ch)
            best = max(best, right - left + 1)
        return best

class S4:  # sliding window with last-index dict (jump)
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0; best = 0
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)
        return best

class S5:  # fixed-size array instead of dict
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128
        left = 0; best = 0
        for right, ch in enumerate(s):
            c = ord(ch)
            if last[c] >= left:
                left = last[c] + 1
            last[c] = right
            best = max(best, right - left + 1)
        return best

sols = [S1(), S2(), S3(), S4(), S5()]
cases = ["abcabcbb", "bbbbb", "pwwkew", "", " ", "au", "dvdf", "abba", "tmmzuxt", "abcdefg"]
for c in cases:
    outs = [s.lengthOfLongestSubstring(c) for s in sols]
    print(repr(c), outs, "agree:", len(set(outs)) == 1)
    assert len(set(outs)) == 1, (c, outs)

random.seed(13)
alpha = "abcd"
for _ in range(4000):
    n = random.randint(0, 14)
    c = "".join(random.choice(alpha) for _ in range(n))
    outs = [s.lengthOfLongestSubstring(c) for s in sols]
    assert len(set(outs)) == 1, (c, outs)
print("stress OK")

# the 'abba' trap: naive jump without the `>= left` guard
def buggy(s):
    last = {}; left = 0; best = 0
    for right, ch in enumerate(s):
        if ch in last:
            left = last[ch] + 1      # missing the >= left guard
        last[ch] = right
        best = max(best, right - left + 1)
    return best
print("abba -> correct", S4().lengthOfLongestSubstring("abba"), "| buggy", buggy("abba"))
print("tmmzuxt -> correct", S4().lengthOfLongestSubstring("tmmzuxt"), "| buggy", buggy("tmmzuxt"))
