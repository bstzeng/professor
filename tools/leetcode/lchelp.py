# -*- coding: utf-8 -*-
"""測試用的小工具：樹的建立與序列化（不會出現在頁面上）。"""
import random
from collections import deque
from runner import TreeNode, ListNode


def lv(vals):
    """LeetCode 的層序表示 -> 樹。"""
    if not vals or vals[0] is None:
        return None
    it = iter(vals)
    root = TreeNode(next(it))
    q = deque([root])
    while q:
        nd = q.popleft()
        for side in ("left", "right"):
            v = next(it, None)
            if v is not None:
                setattr(nd, side, TreeNode(v))
                q.append(getattr(nd, side))
    return root


def ser(root):
    out, q = [], deque([root])
    while q:
        nd = q.popleft()
        if nd is None:
            out.append(None)
            continue
        out.append(nd.val)
        q.append(nd.left)
        q.append(nd.right)
    while out and out[-1] is None:
        out.pop()
    return out


def rand_tree(n, lo=0, hi=9):
    if n == 0:
        return None
    k = random.randrange(0, n)
    return TreeNode(random.randint(lo, hi), rand_tree(k, lo, hi), rand_tree(n - 1 - k, lo, hi))


def bst(vals):
    root = None
    for v in vals:
        if root is None:
            root = TreeNode(v)
            continue
        nd = root
        while True:
            side = "left" if v < nd.val else "right"
            if getattr(nd, side) is None:
                setattr(nd, side, TreeNode(v))
                break
            nd = getattr(nd, side)
    return root


def nodes(root):
    out, st = [], [root] if root else []
    while st:
        nd = st.pop()
        out.append(nd)
        st += [c for c in (nd.left, nd.right) if c]
    return out
