# -*- coding: utf-8 -*-
from typing import List
import random, itertools

class S1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

class S2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = sorted((v, i) for i, v in enumerate(nums))
        lo, hi = 0, len(pairs) - 1
        while lo < hi:
            s = pairs[lo][0] + pairs[hi][0]
            if s == target:
                return sorted([pairs[lo][1], pairs[hi][1]])
            if s < target:
                lo += 1
            else:
                hi -= 1
        return []

class S3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {v: i for i, v in enumerate(nums)}
        for i, v in enumerate(nums):
            j = pos.get(target - v)
            if j is not None and j != i:
                return [i, j]
        return []

class S4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            need = target - v
            if need in seen:
                return [seen[need], i]
            seen[v] = i
        return []

sols = [S1(), S2(), S3(), S4()]
cases = [([2,7,11,15],9), ([3,2,4],6), ([3,3],6), ([0,4,3,0],0), ([-1,-2,-3,-4,-5],-8), ([1,2],3)]
for nums, t in cases:
    outs = [s.twoSum(list(nums), t) for s in sols]
    ok = []
    for o in outs:
        assert len(o)==2 and o[0]!=o[1], (nums,t,o)
        ok.append(nums[o[0]] + nums[o[1]] == t)
    print(nums, t, outs, 'all valid:', all(ok))

# random stress: all four must find *a* valid pair
random.seed(7)
for _ in range(3000):
    n = random.randint(2, 8)
    nums = [random.randint(-20, 20) for _ in range(n)]
    i, j = random.sample(range(n), 2)
    t = nums[i] + nums[j]
    for s in sols:
        o = s.twoSum(list(nums), t)
        assert len(o) == 2 and o[0] != o[1] and nums[o[0]] + nums[o[1]] == t, (type(s).__name__, nums, t, o)
print("stress OK")
