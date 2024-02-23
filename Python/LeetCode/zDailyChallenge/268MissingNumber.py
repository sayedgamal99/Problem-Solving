# solution one: manipulating with values:
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        nums.append(n+1)
        for i in range(n):
            nums[abs(nums[i])] *= -1
        return nums.index(max(nums))


# print(Solution().missingNumber(nums=[8, 6, 4, 2, 3, 5, 7, 1]))


# Solution 2 with math using summation:

class Solution2:
    def missingNumber(self, nums: list[int]) -> int:
        summ = len(nums)*(len(nums)+1)//2
        return summ - sum(nums)


print(Solution2().missingNumber(nums=[8, 6, 4, 2, 3, 5, 7, 1]))
