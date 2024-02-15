class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        nums.sort()
        prfx = [0]*(len(nums)+1)
        maxx = 0
        for j in range(len(nums)):
            prfx[j+1] = prfx[j]+nums[j]
            if prfx[j] > nums[j]:
                maxx = max(maxx, j+1)
        return prfx[maxx] if maxx != 0 else -1


print(Solution().largestPerimeter(nums=[1, 12, 1, 2, 5, 50, 3]))
print(Solution().largestPerimeter([5, 5, 5]))
