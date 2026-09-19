# -*- coding: utf-8 -*-
from typing import Optional
import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build(digits):
    head = ListNode()
    cur = head
    for d in digits:
        cur.next = ListNode(d); cur = cur.next
    return head.next

def dump(node):
    out = []
    while node:
        out.append(node.val); node = node.next
    return out

def to_int(digits):   # digits are reversed (least significant first)
    return int("".join(map(str, reversed(digits)))) if digits else 0

class S1:  # iterative + dummy head
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy
        carry = 0
        while l1 or l2 or carry:
            s = carry
            if l1:
                s += l1.val; l1 = l1.next
            if l2:
                s += l2.val; l2 = l2.next
            carry, digit = divmod(s, 10)
            cur.next = ListNode(digit)
            cur = cur.next
        return dummy.next

class S2:  # recursive
    def addTwoNumbers(self, l1, l2, carry=0):
        if not l1 and not l2 and not carry:
            return None
        s = carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)
        carry, digit = divmod(s, 10)
        node = ListNode(digit)
        node.next = self.addTwoNumbers(l1.next if l1 else None,
                                       l2.next if l2 else None,
                                       carry)
        return node

class S3:  # convert to int (works in Python, discouraged)
    def addTwoNumbers(self, l1, l2):
        def num(node):
            v, p = 0, 1
            while node:
                v += node.val * p; p *= 10; node = node.next
            return v
        total = num(l1) + num(l2)
        dummy = ListNode(); cur = dummy
        while True:
            total, d = divmod(total, 10)
            cur.next = ListNode(d); cur = cur.next
            if total == 0:
                break
        return dummy.next

sols = [S1(), S2(), S3()]
cases = [([2,4,3],[5,6,4]), ([0],[0]), ([9,9,9,9,9,9,9],[9,9,9,9]), ([5],[5]), ([1],[9,9,9])]
for a, b in cases:
    exp = [int(c) for c in str(to_int(a) + to_int(b))][::-1]
    outs = [dump(s.addTwoNumbers(build(a), build(b))) for s in sols]
    print(a, "+", b, "=", outs[0], "expected", exp, "all agree:", all(o == exp for o in outs))
    assert all(o == exp for o in outs), outs

random.seed(11)
for _ in range(3000):
    la = random.randint(1, 12); lb = random.randint(1, 12)
    a = [random.randint(0,9) for _ in range(la)]
    b = [random.randint(0,9) for _ in range(lb)]
    if len(a) > 1 and a[-1] == 0: a[-1] = random.randint(1,9)
    if len(b) > 1 and b[-1] == 0: b[-1] = random.randint(1,9)
    exp = [int(c) for c in str(to_int(a) + to_int(b))][::-1]
    for s in sols:
        assert dump(s.addTwoNumbers(build(a), build(b))) == exp, (type(s).__name__, a, b)
print("stress OK")

# recursion depth check
import sys
print("default recursion limit:", sys.getrecursionlimit())
big = [9]*100
try:
    dump(S2().addTwoNumbers(build(big), build(big)))
    print("recursive OK at n=100")
except RecursionError:
    print("RecursionError at n=100")
