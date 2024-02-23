# Bit manipulation solution: Time: linear, Space: O(1)
from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result


print(Solution().singleNumber([4, 1, 2, 1, 2]))


# hashmap solution: time: linear, space: O(n)


class Solution2:
    def singleNumber(self, nums: list[int]) -> int:
        themap = Counter(nums)
        for k, v in themap.items():
            if v == 1:
                return k


# print(Solution2().singleNumber([4, 1, 2, 1, 2]))
