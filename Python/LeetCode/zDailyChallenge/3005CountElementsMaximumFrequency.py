from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        mapp = Counter(nums)

        maxx = max(mapp.values())
        vv = list(mapp.values())
        return vv.count(maxx)*maxx


print(Solution().maxFrequencyElements([1, 2, 3, 4, 5]))
print(Solution().maxFrequencyElements([1, 1, 2, 2, 3, 5]))
print(Solution().maxFrequencyElements([10, 12, 11, 9, 6, 19, 11]))
