# Basic Solution:
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i]*nums[i]
        nums.sort()
        return nums


# Two pointer solution O(n):

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums)-1
        i = len(nums)-1
        res = [0]*(i+1)
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                res[i] = nums[l]**2
                l += 1
            else:
                res[i] = nums[r]**2
                r -= 1
            i -= 1
        return res


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))
