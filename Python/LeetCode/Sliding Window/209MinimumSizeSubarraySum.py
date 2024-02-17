class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, r = 0, 0
        cumSum = 0
        minlength = float('inf')
        while r < len(nums):
            cumSum += nums[r]
            while cumSum >= target:
                minlength = min(minlength, r-l+1)
                cumSum -= nums[l]
                l += 1
            r += 1
        return minlength if minlength != float('inf') else 0


print(Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
print(Solution().minSubArrayLen(target=11, nums=[1, 2, 3, 4, 5]))
