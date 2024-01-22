# two pointer solution, time: n^2
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        sol = []
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -1*n
            l, r = i+1, len(nums)-1

            while (l < r):
                if nums[l]+nums[r] > target:
                    r -= 1
                elif nums[l]+nums[r] < target:
                    l += 1
                else:
                    sol.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return sol


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
