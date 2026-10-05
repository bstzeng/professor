# -*- coding: utf-8 -*-
"""把「頁面上顯示的程式碼」和「被測試的程式碼」綁成同一份。

用法：
    S = Src()
    S["merge"] = '''class Solution: ...'''
    sol = S.load("merge")          # exec 後拿到 Solution 實例
    ...測試 sol...
    ("c", S["merge"])              # 頁面顯示的就是剛剛測過的那一份
"""
from typing import List, Optional, Dict, Tuple, Set
import collections, heapq, bisect, math, itertools, functools, re, random


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def to_list(vals):
    head = tail = None
    for v in vals:
        n = ListNode(v)
        if head is None:
            head = tail = n
        else:
            tail.next = n; tail = n
    return head


def from_list(node):
    out = []
    seen = set()
    while node is not None:
        assert id(node) not in seen, "cycle in list"
        seen.add(id(node))
        out.append(node.val)
        node = node.next
    return out


NS = dict(globals())
# LeetCode 的 Python 環境預先匯入了這些名稱
from collections import deque, Counter, defaultdict, OrderedDict
from functools import cache, lru_cache, reduce
from itertools import accumulate, permutations, combinations, product
from math import gcd, inf, comb, isqrt
from bisect import bisect_left, bisect_right, insort
import string, operator
NS.update(deque=deque, Counter=Counter, defaultdict=defaultdict, OrderedDict=OrderedDict, cache=cache,
          lru_cache=lru_cache, reduce=reduce, accumulate=accumulate, permutations=permutations,
          combinations=combinations, product=product, gcd=gcd, inf=inf, comb=comb, isqrt=isqrt,
          bisect_left=bisect_left, bisect_right=bisect_right, insort=insort, string=string, operator=operator)


class Src(dict):
    def load(self, key, name="Solution", extra=None):
        """extra 用來補上題目自帶、但頁面上不會顯示的型別（例如第 116 題的 Node）。"""
        ns = dict(NS)
        if extra:
            ns.update(extra)
        exec(compile(self[key], "<%s>" % key, "exec"), ns)
        return ns[name]()

    def loadns(self, key, extra=None):
        ns = dict(NS)
        if extra:
            ns.update(extra)
        exec(compile(self[key], "<%s>" % key, "exec"), ns)
        return ns
