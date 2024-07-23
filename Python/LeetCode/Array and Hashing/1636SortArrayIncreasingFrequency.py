from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        sorted_nums = sorted(nums, key=lambda x: (count[x], -x))
        return sorted_nums


print(Solution().frequencySort(nums=[1, 1, 2, 2, 2, 3]))
