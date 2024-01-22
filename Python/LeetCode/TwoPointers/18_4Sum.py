class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:

        nums.sort()
        sol = set()
        for jj in range(len(nums)):

            for i in range(jj+1, len(nums)):

                l, r = i+1, len(nums)-1

                while (l < r):
                    if nums[jj]+nums[i]+nums[l]+nums[r] > target:
                        r -= 1
                    elif nums[jj]+nums[i]+nums[l]+nums[r] < target:
                        l += 1
                    elif nums[jj]+nums[i]+nums[l]+nums[r] == target:
                        print(jj, i, l, r)
                        sol.add((nums[jj], nums[i], nums[l], nums[r]))
                        l += 1
                        r -= 1

        return [kn for kn in sol]


# print(Solution().fourSum([1, 0,-1,0,-2,2],0))
# print(Solution().fourSum([2,2,2,2,2],8))
print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
