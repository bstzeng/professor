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


class Src(dict):
    def load(self, key, name="Solution"):
        ns = dict(NS)
        exec(compile(self[key], "<%s>" % key, "exec"), ns)
        return ns[name]()

    def loadns(self, key):
        ns = dict(NS)
        exec(compile(self[key], "<%s>" % key, "exec"), ns)
        return ns
